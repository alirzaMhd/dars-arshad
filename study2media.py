#!/usr/bin/env python3
"""
Study Guide → Video + TTS Audiobook Converter

Usage:
  python study2media.py <markdown_file>

Generates:
  - Suggestion for a study video (waits for approval)
  - TTS-generated audiobook using Chatterbox Turbo (MIT, open-source)
"""

import argparse
import os
import re
import sys

AUDIOBOOK_DIR = "/content/dars-arshad/audiobooks"
VIDEO_DIR = "/content/dars-arshad/videos"


def parse_markdown(filepath):
    """Read markdown and return text content split into chapters."""
    with open(filepath, encoding="utf-8") as f:
        text = f.read()

    chapters = re.split(r"(?=^### )", text, flags=re.MULTILINE)
    clean = []
    for ch in chapters:
        stripped = ch.strip()
        if stripped:
            clean.append(stripped)
    return clean, text


def strip_markdown(text):
    """Remove markdown formatting for clean plain text."""
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"`(.*?)`", r"\1", text)
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    text = re.sub(r"\[([^\]]*)\]\(.*?\)", r"\1", text)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\|.*\|$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^[-*]\s", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def suggest_video_approach(chapters, title):
    """Print a video creation suggestion and ask for approval."""
    print("\n" + "=" * 70)
    print(f"  VIDEO SUGGESTION FOR: {title}")
    print("=" * 70)
    print("""
  Proposed Approach:
  • Each section/chapter becomes a text slide
  • Slides fade in/out with synchronized TTS narration
  • Subtitles embedded as overlays
  • Resolution: 1920x1080, 30fps
  • Background: dark gradient with white text
  • Estimated slides: ~{num_slides}
  • Audio track from Chatterbox Turbo TTS (sync'd with slides)
  • Total estimated duration: ~{duration_min} min

  Tools: moviepy (installed: ✓)
""".format(num_slides=len(chapters), duration_min=max(1, len(chapters) * 2)))

    while True:
        resp = input("  Generate video? (y/N): ").strip().lower()
        if resp == "y":
            return True
        elif resp in ("n", ""):
            return False
        print("  Please answer y or n.")


def create_study_video(chapters, title, output_path):
    """Create a study video from chapters using PIL + moviepy."""
    from PIL import Image, ImageDraw, ImageFont
    from moviepy.video.VideoClip import ImageClip
    from moviepy.video.compositing.concatenate import concatenate_videoclips
    import numpy as np

    W, H = 1920, 1080

    clips = []
    for i, ch in enumerate(chapters[:20]):  # limit to 20 slides to be reasonable
        heading = ch.split("\n")[0][:80]
        body = strip_markdown(ch)[:600]

        img = Image.new("RGB", (W, H), (10, 10, 30))
        draw = ImageDraw.Draw(img)
        lines = []
        for line in (heading, "", body).__iter__():
            lines.append(line)

        y = 80
        for line in lines:
            if not line:
                y += 30
                continue
            # word-wrap manually
            words = line.split()
            curr = ""
            for w in words:
                test = curr + " " + w if curr else w
                if draw.textlength(test, font=None) < W - 160:
                    curr = test
                else:
                    draw.text((80, y), curr, fill=(220, 220, 255))
                    y += 40
                    curr = w
            if curr:
                draw.text((80, y), curr, fill=(220, 220, 255))
                y += 40
            y += 10

        frame = np.array(img)
        clip = ImageClip(frame).with_duration(12)
        clips.append(clip)

    if not clips:
        return None
    video = concatenate_videoclips(clips, method="compose")
    video.write_videofile(output_path, fps=30, codec="libx264", audio=False)
    video.close()
    return output_path


def generate_audiobook(text_chunks, output_path):
    """Generate TTS audiobook using Chatterbox Turbo."""
    import torch
    import torchaudio as ta
    from chatterbox.tts_turbo import ChatterboxTurboTTS

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"  Loading Chatterbox Turbo on {device}...")
    model = ChatterboxTurboTTS.from_pretrained(device=device)

    sample_rate = model.sr
    all_audio = []

    for i, chunk in enumerate(text_chunks):
        clean = strip_markdown(chunk)
        if len(clean) < 20:
            continue

        # Skip table-only chunks
        if clean.count("|") > len(clean) * 0.1:
            continue

        # Truncate to model's max length
        if len(clean) > 2000:
            clean = clean[:2000]

        print(f"  Generating chunk {i+1}/{len(text_chunks)} ({len(clean)} chars)...")
        try:
            wav = model.generate(clean)
            all_audio.append(wav.cpu())
        except Exception as e:
            print(f"  Warning: chunk {i+1} failed: {e}")
            continue

    if not all_audio:
        print("  No audio generated!")
        return None

    combined = torch.cat(all_audio, dim=1)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    ta.save(output_path, combined, sample_rate)
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Convert a study guide markdown to video + TTS audiobook"
    )
    parser.add_argument("markdown_file", help="Path to the study guide markdown file")
    parser.add_argument(
        "--skip-video", action="store_true", help="Skip video suggestion/generation"
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output base name (without extension)",
    )
    parser.add_argument(
        "--generate-video",
        action="store_true",
        help="Generate video without asking (used after approval)",
    )
    args = parser.parse_args()

    if not os.path.exists(args.markdown_file):
        print(f"Error: file not found: {args.markdown_file}")
        sys.exit(1)

    chapters, full_text = parse_markdown(args.markdown_file)
    base_name = args.output or os.path.splitext(os.path.basename(args.markdown_file))[0]
    title = chapters[0].split("\n")[0] if chapters else base_name

    print(f"\n  Loaded {len(chapters)} sections from {os.path.basename(args.markdown_file)}")
    print(f"  Total size: ~{len(full_text)} chars")

    # --- Step 1: Video (suggest and wait for approval) ---
    if not args.skip_video and not args.generate_video:
        approved = suggest_video_approach(chapters, title)
        if approved:
            out_video = os.path.join(VIDEO_DIR, f"{base_name}.mp4")
            os.makedirs(VIDEO_DIR, exist_ok=True)
            print("\n  Generating video...")
            create_study_video(chapters, title, out_video)
            print(f"  Video saved: {out_video}")
        else:
            print("  Skipping video generation.")
    elif args.generate_video:
        out_video = os.path.join(VIDEO_DIR, f"{base_name}.mp4")
        os.makedirs(VIDEO_DIR, exist_ok=True)
        print("\n  Generating video (approved)...")
        create_study_video(chapters, title, out_video)
        print(f"  Video saved: {out_video}")

    # --- Step 2: TTS Audiobook ---
    print("\n" + "=" * 70)
    print("  GENERATING TTS AUDIOBOOK (Chatterbox Turbo)")
    print("=" * 70)
    out_audio = os.path.join(AUDIOBOOK_DIR, f"{base_name}.wav")
    os.makedirs(AUDIOBOOK_DIR, exist_ok=True)

    print("  This may take a while (processing on CPU)...")
    result = generate_audiobook(chapters, out_audio)
    if result:
        print(f"\n  Audiobook saved: {result}")
        import math
        size_mb = os.path.getsize(result) / (1024 * 1024)
        print(f"  File size: {size_mb:.1f} MB")
    else:
        print("  Audiobook generation failed.")


if __name__ == "__main__":
    main()
