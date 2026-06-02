import os
import uuid
import json
import re
import io
import wave
import numpy as np
import soundfile as sf
import pymupdf
import torch
from flask import Flask, request, jsonify, send_file, render_template, url_for
from flask_cors import CORS
from kokoro import KPipeline

app = Flask(__name__)
CORS(app)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'static', 'uploads')
app.config['AUDIO_FOLDER'] = os.path.join(BASE_DIR, 'static', 'audio')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['AUDIO_FOLDER'], exist_ok=True)

_pipeline = None
def get_pipeline():
    global _pipeline
    if _pipeline is None:
        _pipeline = KPipeline(lang_code='a')
    return _pipeline

def extract_lines(pdf_path, max_chars=300):
    doc = pymupdf.open(pdf_path)
    lines = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("blocks")
        for block in blocks:
            text = block[4].strip()
            if not text:
                continue
            block_lines = text.split('\n')
            for bl in block_lines:
                bl = bl.strip()
                if not bl:
                    continue
                lines.append({
                    'page': page_num + 1,
                    'text': bl
                })
    return lines

def group_lines(lines, max_chars=300):
    groups = []
    current = []
    current_text = ""
    for line in lines:
        candidate = (current_text + " " + line['text']).strip() if current_text else line['text']
        if len(candidate) <= max_chars:
            current.append(line)
            current_text = candidate
        else:
            if current:
                groups.append({'lines': current, 'text': current_text})
            current = [line]
            current_text = line['text']
    if current:
        groups.append({'lines': current, 'text': current_text})
    return groups

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    session_id = str(uuid.uuid4())[:8]
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], f'{session_id}.pdf')
    file.save(pdf_path)

    raw_lines = extract_lines(pdf_path)
    total_chars = sum(len(l['text']) for l in raw_lines)
    total_lines = len(raw_lines)

    return jsonify({
        'session_id': session_id,
        'total_lines': total_lines,
        'total_chars': total_chars,
        'message': 'PDF uploaded. Proceed to generate audio.'
    })

@app.route('/api/generate', methods=['POST'])
def generate_audio():
    data = request.get_json()
    session_id = data.get('session_id')
    if not session_id:
        return jsonify({'error': 'No session_id'}), 400

    voice = data.get('voice', 'af_heart')
    speed = float(data.get('speed', 1.0))

    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], f'{session_id}.pdf')
    if not os.path.exists(pdf_path):
        return jsonify({'error': 'PDF not found. Upload first.'}), 400

    raw_lines = extract_lines(pdf_path)
    groups = group_lines(raw_lines, max_chars=300)

    segments = []
    audio_dir = os.path.join(app.config['AUDIO_FOLDER'], session_id)
    os.makedirs(audio_dir, exist_ok=True)

    total = len(groups)
    for idx, group in enumerate(groups):
        text = group['text']
        audio_path = os.path.join(audio_dir, f'seg_{idx:04d}.wav')

        audio_data = []
        for result in get_pipeline()(text, voice=voice, speed=speed):
            if result.audio is not None:
                audio_data.append(result.audio)
        if audio_data:
            if hasattr(audio_data[0], 'cpu'):
                full_audio = torch.cat(audio_data).cpu().numpy()
            else:
                full_audio = np.concatenate(audio_data)
        else:
            continue

        sf.write(audio_path, full_audio, 24000)
        duration = len(full_audio) / 24000

        seg_lines = [{'page': l['page'], 'text': l['text']} for l in group['lines']]
        segments.append({
            'index': idx,
            'text': text,
            'lines': seg_lines,
            'audio_url': f'/static/audio/{session_id}/seg_{idx:04d}.wav',
            'duration': duration
        })

    manifest = {'session_id': session_id, 'segments': segments, 'total_segments': len(segments)}
    manifest_path = os.path.join(audio_dir, 'manifest.json')
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f)

    return jsonify(manifest)

@app.route('/api/load/<session_id>')
def load_session(session_id):
    manifest_path = os.path.join(app.config['AUDIO_FOLDER'], session_id, 'manifest.json')
    if os.path.exists(manifest_path):
        with open(manifest_path) as f:
            return jsonify(json.load(f))
    return jsonify({'error': 'Session not found'}), 404

@app.route('/api/voices')
def list_voices():
    voices = [
        'af_heart','af_bella','af_sarah','af_sky','af_nicole','af_alloy','af_aoede','af_jessica','af_kore','af_nova','af_river',
        'am_adam','am_echo','am_eric','am_fenrir','am_liam','am_michael','am_onyx','am_puck','am_santa',
    ]
    return jsonify(voices)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=False)
