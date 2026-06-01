---
name: cram-notes
description: Generate ultra-compressed night-before-exam cram notes from a book or long document. Use when the user says "cram this book", "night before exam notes", "make a cheat sheet from <book>", "exam summary", "study guide for tomorrow", "compress this book to one page", or asks for a "very short version" of a book. Reads every chapter and returns a tight Markdown file of must-know facts, key terms, formulas, dates, and likely exam questions.
license: MIT
compatibility: opencode
metadata:
  audience: students
  workflow: study
---

## What I do

- Accept a book or long document in any common format (`.txt`, `.md`, `.pdf`, `.epub`, or a URL)
- Detect and list all chapters
- Read each chapter one at a time (never the whole file at once)
- Compress every chapter into a few high-yield bullet points
- Produce a single short Markdown cram sheet: a Top-20 must-know list, a chapter-by-chapter micro-summary, key terms/glossary, formulas/dates/people, and 5-10 likely exam questions with one-line answers

## When to use me

Use this when the user wants the *shortest possible* version of a book that still contains the answers a teacher could plausibly test. The output is meant to be readable in 20-30 minutes the night before an exam.

Trigger phrases:
- "cram this book", "night before exam notes", "exam cram"
- "cheat sheet from <book>", "study guide for tomorrow"
- "compress this to one page", "ultra short summary"
- "give me the must-knows from <book>"

Do **not** use this when the user wants a deep, faithful summary or a full book report. For those, use a `book-summary` style workflow instead.

## Input

Ask the user to clarify only if the source is ambiguous. Default to: "Point me at the book (path or URL) and tell me the subject and exam format if you can."

If they provide no path, ask once. Never invent book content.

## Workflow

### Step 1 — Acquire the book

| Source | Action |
|---|---|
| `.txt` / `.md` | Read directly with offset/limit |
| `.pdf` | Use the `pdf` skill to extract text, or `python3 -c "from pypdf import PdfReader; print('\\n'.join(p.extract_text() for p in PdfReader('file.pdf').pages))"` |
| `.epub` | `python3 -c "import ebooklib, bs4; from ebooklib import epub; b=epub.read_epub('file.epub'); [print(c.get_content().decode() if isinstance(c.get_content(),bytes) else c.get_content()) for c in b.get_items_of_type(ebooklib.ITEM_DOCUMENT)]"` then strip HTML |
| URL | `curl -sL <url> | python3 -c "import sys,re; print(re.sub(r'<[^>]+>',' ',sys.stdin.read()))"` |

Save the cleaned text next to the original as `<book>.clean.txt` for reuse.

### Step 2 — Map the structure

Scan the first ~500 lines to find the table of contents or chapter headings. Build a chapter index: `[(number, title, start_line, end_line)]`. If the book has no detectable chapters, fall back to splitting into 10-15 equal parts.

### Step 3 — Confirm scope with the user

If the book has more than ~20 chapters, ask which subset to prioritize (whole book, exam-relevant sections, or last-N chapters).

### Step 4 — Read and compress each chapter

For each chapter:
1. Extract the slice with offset/limit
2. Identify the 3-5 most exam-worthy points: definitions, named theories, dates, formulas, cause/effect chains, contrasts
3. Drop examples, anecdotes, and repetition
4. Note any cross-chapter links

Target: each chapter compresses to **5-10 bullet points** or roughly 150-250 words. Aggressive compression is the whole point.

### Step 5 — Write the cram sheet

Save as `cram-notes-<book-title>-<YYYY-MM-DD>.md` with this structure:

```markdown
# Cram Notes: <Book Title>

> Generated <date>. Read time: ~20-30 min.

## Top 20 Must-Knows
1. ...
2. ...
...
20. ...

## Chapter Micro-Summaries
### Ch. 1 — <Title>
- ...
- ...

### Ch. 2 — <Title>
- ...

## Key Terms & Glossary
- **Term**: one-line definition
- ...

## Formulas / Dates / People to Memorize
- ...
- ...

## Likely Exam Questions
1. **Q:** ...  **A:** one-line answer
2. ...
```

### Step 6 — Verify before saving

Re-read the output and check:
- Is every chapter covered? (count must match the index)
- Are quotes verbatim if any are included?
- Is the total length under ~1500 words? (If longer, tighten the Top-20 list.)
- Did you flag any section where the source was unclear?

## Rules

- **Never invent content.** If a chapter is missing or unreadable, say so in the output.
- **Compress aggressively.** If a chapter can be one bullet, make it one bullet.
- **Preserve the author's framing** for theories and definitions — paraphrase only connective tissue.
- **Surface exam signals**: things the author repeats, puts in bold, places in summaries, or frames as "key" / "important" / "remember" are almost always testable.
- **Respect copyright.** Do not reproduce long verbatim passages. Brief quotes (<=25 words) for definitions are fine.
- **No filler.** No "in this chapter we learned...". No "as discussed earlier". Just the facts.

## Large book strategy

Books over ~2000 lines must be processed in chunks:
1. **Scan** the first 500 lines to identify structure.
2. **Locate** all chapter headings and their line numbers.
3. **Extract** one chapter at a time using offset/limit.
4. **Discard** chapter text after compression — only the bullets go into the final file.

This keeps token usage bounded and works for any book length.
