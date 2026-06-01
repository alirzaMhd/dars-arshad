---
name: cram-notes-fa
description: Generate comprehensive full-coverage exam study notes in Persian (Farsi) from a book or long document. Use when the user wants a complete Persian study guide. Reads every chapter and returns a thorough Markdown file written in Persian covering every examinable concept, term, process, formula, case study, and likely exam question in detail.
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
- Systematically extract **every examinable primitive** from each chapter using a universal taxonomy that works for any discipline (CS, Biology, Math, Physics, Chemistry, Medicine, Engineering, Law, History, etc.)
- Produce a comprehensive Markdown study guide **written entirely in Persian (Farsi)** covering: definitions, procedures/algorithms/pathways, formulas, classifications/comparisons, rules/laws/theorems, data structures, proof/argument patterns, design paradigms (DP, greedy, CRISPR, PCR), visual diagrams (text), edge cases, evidence, case studies, cross-chapter dependencies, mnemonics, probability & statistics foundation, self-test fill-in templates, ethics, and likely exam questions
- **No length limit — every examinable item is included.** The goal is that a student who reads the output cover-to-cover should be prepared for any question on the exam (score 20/20).

## When to use me

Use this when the user wants a **complete study guide in Persian** from a book — not a quick cram sheet, but thorough coverage that leaves nothing out.

Trigger phrases (English):
- "cram this book in persian", "persian study guide", "farsi notes"
- "full summary in persian from <book>", "complete study guide in farsi"

Trigger phrases (Persian):
- "کتاب را به فارسی خلاصه کن", "جزوه کامل فارسی از کتاب", "نکات امتحانی فارسی"
- "خلاصه جامع کتاب", "راهنمای مطالعه کامل فارسی"

Do **not** use this when the user wants an ultra-short one-page cheat sheet.

## Input

Ask the user to clarify only if the source is ambiguous. Default to: "Point me at the book (path or URL), tell me the subject, and the exam format (MCQ / short answer / essay / problem-solving / mixed) if you know it."

- **Subject** determines extraction bias (see Domain Heuristics below).
- **Exam format** adjusts how exam questions are written (MCQ → include distractors; problem-solving → include trace-through problems).

If they provide no path, ask once. Never invent book content.

## Output Length Preference

Before asking, count the total number of lines in the book file (e.g., `wc -l <book>.txt`) and tell the user: **"The book is approximately <N> lines long."**

Then ask: **"How many lines would you like the study guide to be approximately?"** Offer these options:
- **Comprehensive (no limit)** — extract everything (default)
- **~2000 lines** — thorough but trimmed
- **~1000 lines** — concise
- **~500 lines** — compact
- **Custom** — let them type a number

Store their choice as `$OUTPUT_LINES`. If they choose "Comprehensive" or don't specify, extract everything with no length limit. If they choose a specific number, respect that target by prioritizing the most exam-relevant content per chapter (focus on definitions, key processes, formulas, comparisons, and end-of-chapter material; trim examples and narrative).

Update the study guide header to include: `> طول هدف: <value> خط.`

## Workflow

### Step 1 — Acquire the book

| Source | Action |
|---|---|
| `.txt` / `.md` | Read directly with offset/limit |
| `.pdf` | Use the `pdf` skill to extract text, or `python3 -c "from pypdf import PdfReader; print('\\n'.join(p.extract_text() for p in PdfReader('file.pdf').pages))"` |
| `.epub` | `python3 -c "import ebooklib, bs4; from ebooklib import epub; b=epub.read_epub('file.epub'); [print(c.get_content().decode() if isinstance(c.get_content(),bytes) else c.get_content()) for c in b.get_items_of_type(ebooklib.ITEM_DOCUMENT)]"` then strip HTML |
| URL | `curl -sL <url> \| python3 -c "import sys,re; print(re.sub(r'<[^>]+>',' ',sys.stdin.read()))"` |

Save the cleaned text next to the original as `<book>.clean.txt` for reuse.

### Step 2 — Map the structure

Scan the first ~500 lines to find the table of contents or chapter headings. Build a chapter index: `[(number, title, start_line, end_line)]`. If the book has no detectable chapters, fall back to splitting into 10–15 equal parts.

Build a preliminary **cross-chapter dependency map** by noting forward references as you scan.

### Step 3 — Confirm scope with the user

If the book has >20 chapters, ask which subset to prioritize (whole book, exam-relevant sections, or last-N chapters).

### Step 4 — Read and extract from each chapter (universal checklist) — comprehensively

For each chapter:
1. Extract the slice with offset/limit
2. Run the **universal extraction checklist** below. **Check every category.** If a category has zero content in that chapter, skip it. This systematic sweep ensures nothing examinable is missed.
3. **Include all content**, not just highlights. Every named entity, every process step, every formula, every comparison, every edge case, every case study — extract it all.
4. **Keep examples and anecdotes** if they help understand the concept. Do not drop them aggressively — only remove truly redundant repetition.
5. Note any cross-chapter links discovered

#### Universal Extraction Checklist

| # | Primitive | What to look for | Applies to |
|---|-----------|------------------|------------|
| 1 | **Named Entities** | Terms, concepts, phenomena, species, organelles, compounds, diseases, algorithms, data structures, protocols — any named thing with a definition | All domains |
| 2 | **Sequential Processes** | Step-by-step procedures: algorithms, metabolic pathways, signaling cascades, protocols, methods, workflows, cycles (Krebs, cell cycle, fetch-decode-execute) — **list every step with full detail** | CS, Bio, Chem, Medicine, Engineering |
| 3 | **Hierarchies / Classifications** | Taxonomies, type systems, categorization schemes, complexity classes, Linnaean ranks, disease classifications, protein families — **reproduce the full hierarchy, not just the top levels** | All domains |
| 4 | **Comparisons / Trade-offs** | A vs B, pros/cons, before/after, strengths/weaknesses — anything that contrasts two or more things | All domains |
| 5 | **Formulas & Equations** | Mathematical expressions, statistical tests, chemical equations, Big-O bounds, reaction rate laws, Hardy-Weinberg, enzyme kinetics — **include every formula with all variable definitions and units** | CS, Math, Physics, Chem, Bio, Engineering |
| 6 | **Rules, Laws & Theorems** | Named principles: laws, theorems, rules of thumb, design principles, biological laws (Mendel, Hardy-Weinberg), legal doctrines — **include full statement and conditions** | All domains |
| 7 | **Data Structures & Types** (CS-specific section) | Properties, supported operations, time/space complexity, trade-offs, when to use each — **include all variants and implementations discussed** | CS |
| 8 | **Visual Patterns** (text-described) | Diagrams, graphs, charts, pathways, architectures, cycles — describe them in text so they can be re-drawn from memory | All domains (critical for Bio pathways, CS graphs, Engineering diagrams) |
| 9 | **Edge Cases / Exceptions / Traps** | Gotchas, degenerate inputs, worst-case scenarios, atypical presentations, contraindications, non-examples | All domains |
| 10 | **Empirical Evidence / Key Results** | Experimental findings, benchmark results, case studies, statistical significance, key experiments — **include numbers, sample sizes, and conclusions** | CS (benchmarks), Bio/Chem (experiments), Medicine (trials) |
| 11 | **Cross-Chapter Dependencies** | "This requires Ch X", "as we saw in Ch Y", forward references | All domains |
| 12 | **Dates & People** | Discoverers, inventors, landmark dates, historical context | All domains (critical for History, Medicine, CS pioneers) |
| 13 | **Proof & Argument Patterns** | Induction, contradiction, loop invariants, exchange argument, greedy stays ahead, reduction, experimental reasoning (controls, variables, statistical significance), phylogenetic inference — **include the full proof structure** | CS, Math, Bio, Medicine |
| 14 | **Design Paradigms / Meta-Methods** | Cross-cutting methodologies: divide & conquer, dynamic programming, greedy, backtracking, branch & bound (CS); PCR, gel electrophoresis, Western blot, CRISPR, sequencing (Bio); any reusable technique referenced across multiple chapters — **describe each in detail with when/why/how** | CS, Bio, Chem, Medicine, Engineering |
| 15 | **Case Studies / Classic Examples** | Famous named experiments or systems: Mendel's peas, Meselson-Stahl, Hershey-Chase, HeLa cells, Pavlov's dogs (Bio); Turing test, CAP theorem, Winograd schema (CS); landmark legal cases (Law) — **include full details: what was done, results, significance** | All domains |
| 16 | **Ethics & Professional Practice** | AI ethics principles, animal testing guidelines, informed consent, CRISPR ethics, data privacy, dual-use concerns, professional codes of conduct | CS, Bio, Medicine, Engineering, Law |
| 17 | **Chapter Summaries / End-of-Chapter Material** | Bolded terms, review questions, key points boxes, exercises — **extract all of these verbatim; they are the most exam-relevant content** | All domains |

Target: each chapter should yield **enough content to fully cover the chapter's material**. There is no upper limit on bullets or word count. A dense textbook chapter may yield 100+ bullets. Prefer structured formats over prose, but include enough detail that the reader can learn the material without referring back to the original book.

### Step 5 — Write the comprehensive study guide (in Persian)

**IMPORTANT: All output text must be written in Persian (Farsi).** Technical terms (e.g., algorithm names, variable names, keywords) should be kept in their original English/Latin form for clarity, but all surrounding explanation, definitions, descriptions, section headers, and commentary must be in Persian.

Save as `راهنمای-مطالعه-<book-title>-<YYYY-MM-DD>.md` with this template. **Include every section that has content.** Reorder sections so the most content-heavy ones come first. Skip empty sections entirely.

```markdown
# راهنمای مطالعه: <عنوان کتاب>

> تاریخ تولید <date>. موضوع: <domain>. فرمت امتحان: <format>. پوشش: جامع.

## تفکیک فصل‌به‌فصل

### فصل ۱ — <عنوان>

#### موجودیت‌های نام‌گذاری‌شده (اصطلاحات و تعاریف)
- **اصطلاح**: تعریف کامل با زمینه
- ...

#### فرایندها / الگوریتم‌ها / مسیرها
##### <نام>
- **نوع**: الگوریتم / مسیر / چرخه / پروتکل / گردش کار
- **هدف**: ...
- **مراحل**: (۱) ... (۲) ... (۳) ... (N) ... — **هر مرحله با جزئیات کامل شرح داده شود**
- **ورودی**: ... **خروجی**: ...
- **شرایط / نام‌تغییرها**: ...
- **پیچیدگی** (در صورت وجود): زمان O(?) فضا O(?)
- **حالات مرزی**: ...
- **مثال**: یک مثال عینی با اعداد ارائه شود

#### طبقه‌بندی‌ها و سلسله‌مراتب
- **نام سلسله‌مراتب**:
  - سطح ۱: ...
    - سطح ۲: ...
      - سطح ۳: ...

#### مقایسه‌ها و بده‌بستان‌ها
| بعد | A | B |
|---|---|---|
| ویژگی | مقدار | مقدار |
| مزیت | ... | ... |
| عیب | ... | ... |

#### فرمول‌ها و معادلات
##### <نام>
`معادله`
- *متغیر* = تعریف [واحد]
- *متغیر* = تعریف [واحد]
- **زمان استفاده**: ...
- **محدودیت‌ها**: ...
- **محاسبه نمونه**: ...

#### قوانین، اصول و قضایا
##### <نام>
- **بیان**: بیان کامل
- **شرایط / مفروضات**: ...
- **پیامدها**: ...
- **طرح اثبات**: ...
- **اشتباه رایج**: ...

#### حالات مرزی و دام‌های رایج
- **موقعیت**: ... **چرا به دام می‌اندازد**: ... **چگونه اجتناب کنیم**: ... **مثال**: ...

#### مطالعات موردی و مثال‌ها
##### <نام>
- **چه بود**: شرح مفصل مطالعه/آزمایش
- **روش**: نحوه انجام
- **نتایج**: چه یافته‌هایی (با اعداد)
- **اهمیت**: چرا مهم است
- **زاویه امتحانی**: چه سؤالی ممکن است بپرسند

#### نمودارها و تصاویر
```
نمودار ASCII / متن
```
- **برچسب‌ها**: ...
- **جریان**: ...
- **نقاط کلیدی**: ...

#### مطالب پایان فصل
- **اصطلاحات کلیدی** (بازتولید شده از فصل): ...
- **سؤالات مرور** (با پاسخ): ...
- **تمرینات** (با راه‌حل‌های ساده): ...

### فصل ۲ — <عنوان>
... (همان ساختار)

---

## موضوعات بین‌بخشی

### پارادایم‌های طراحی و روش‌های فراتر
(استخراج‌شده از تمام فصول)

### الگوهای اثبات و استدلال
(استخراج‌شده از تمام فصول)

### مبانی احتمال و آمار
(استخراج‌شده از تمام فصول)

### فنون حافظه و کمک‌حافظه‌ها
(استخراج‌شده از تمام فصول)

### افراد و تاریخ‌ها
(استخراج‌شده از تمام فصول)

---

## سؤالات امتحانی بر اساس نوع

### چندگزینه‌ای (MCQ)
1. **س:** ...  **پ:** ...  **گزینه انحرافی:** ... (چرا اشتباه است)
2. **س:** ...  **پ:** ...  **گزینه انحرافی:** ...

### پاسخ کوتاه
1. **س:** ...  **نمره‌دهی:** نکته ۱، نکته ۲، نکته ۳

### ردیابی / اعمال
1. **ورودی:** ... **اعمال <الگوریتم/فرایند>** → **خروجی مورد انتظار:** ... **دلیل:** ...

### برچسب‌گذاری نمودار
1. **نمودار:** <توضیح متنی> **برچسب:** عنصر A، عنصر B، عنصر C

### مقاله / پاسخ بلند
1. **س:** ...  **نکات کلیدی برای ذکر:** ...، ...، ...
```

### Step 6 — Verify before saving

Re-read the output and check:
- Is every chapter covered? (count must match the index)
- Were all 17 universal primitives checked against each chapter? (no category skipped without consideration)
- For each chapter, have you extracted **all** named entities, process steps, formulas, comparisons, edge cases, case studies, and end-of-chapter material?
- Are all process steps complete (not truncated) — could a student follow them without the original book?
- Are formulas given with every variable defined plus units/constraints?
- Are comparisons fair (same dimensions used across both sides)?
- Are case studies described with enough detail (method, results, significance) for an essay question?
- Is the end-of-chapter material (bold terms, review questions, exercises) fully reproduced?
- Are design paradigms and meta-methods extracted and consolidated from across all chapters?
- Are proof/argument patterns captured with full structure + classic example?
- Is the probability & statistics section present (if the source uses any stats)?
- Are ethics topics captured (if the source covers ethics)?
- Are exam questions formatted per the user's specified exam type?
- **Is there any section where a reader would need to go back to the original book? If so, add more detail.**
- Did you flag any section where the source was unclear?
- **Is all explanatory text written in Persian (Farsi)?** Technical terms may remain in English, but everything else must be Persian.

## Rules

- **Never invent content.** If a chapter is missing or unreadable, say so in the output.
- **Systematic extraction is mandatory.** Run every category in the universal checklist against every chapter. Do not skip categories preemptively — let the content decide.
- **Be comprehensive, not compressed.** Include every named entity, every process step, every formula, every comparison, every edge case. The goal is that the reader can learn solely from the study guide without needing the original book.
- **Preserve the author's framing** for theories, definitions, and named items — paraphrase only connective tissue.
- **Surface exam signals**: repetition, bold text, summary boxes, "key" / "important" / "remember" — these are almost always testable.
- **Reproduce end-of-chapter material verbatim.** Bolded terms, key points boxes, review questions, and exercises are the single most exam-relevant content in any textbook. Include them fully.
- **Generate mnemonics proactively.** If a list of 5+ items must be memorized (e.g., Big-O ordering, Krebs cycle intermediates, Kings of England), invent an acronym, rhyme, or chunk for it.
- **Generate self-test templates for any process/algorithm with ≥5 steps.** Leave blanks for key steps, inputs, or outputs so the student can fill them from memory. Reference the answer location.
- **Capture ethics wherever present.** If the source discusses ethics (AI safety, animal testing, informed consent, dual-use), extract it as a dedicated item.
- **Prioritize technical content** over narrative. Include both the formula and the explanatory context needed to understand it.
- **Walk through examples.** For any algorithm, formula, or process, include at least one concrete worked example with values.
- **Respect copyright.** Do not reproduce long verbatim passages. Brief quotes (≤25 words) for definitions are fine. Pseudocode and small code snippets (≤15 lines) that are idiomatic/canonical are fine. End-of-chapter material is typically short enough to include.
- **No filler.** No "in this chapter we learned...". No "as discussed earlier". Just the facts.
- **Structured over prose.** Use lists, tables, ASCII diagrams, and equations. Minimize paragraphs.
- **There is no length limit.** Do not truncate or abbreviate content to save space. If coverage of a chapter requires 200 bullets, write 200 bullets.
- **Output language: Persian (Farsi).** All explanatory text, definitions, descriptions, and section headers must be in Persian. Technical terms (algorithm names, variable names, code, keywords, formulas) may remain in their original form for clarity.
- **Filename:** Use Persian naming: `راهنمای-مطالعه-<book-title>-<YYYY-MM-DD>.md`

## Large book strategy

Books over ~2000 lines must be processed in chunks:
1. **Scan** the first 500 lines to identify structure.
2. **Locate** all chapter headings and their line numbers.
3. **Extract** one chapter at a time using offset/limit — extract **all** examinable primitives before moving on.
4. **Append** the extracted material to the study guide. Do not discard chapter text until you have fully extracted every primitive from it.

This keeps token usage bounded while still achieving comprehensive coverage for any book length.

## Domain-specific attention areas

When the subject is known, **pay extra attention** to these primitives — they tend to carry the most exam weight in that field. But still extract **all 17 categories** from every chapter; these are just the ones that are most likely to have rich content:

| Domain | Especially rich in these primitives |
|---|---|
| CS / Programming | Sequential Processes (algorithms), Data Structures, Comparisons (trade-offs), Formulas (Big-O), Design Paradigms (DP, greedy, divide & conquer), Proof Patterns (induction, invariants, reductions), Visuals (architectures), Edge Cases, Case Studies, People/Dates, Empirical Evidence, Ethics |
| Biology | Sequential Processes (pathways, cycles), Hierarchies (taxonomies), Comparisons (e.g. mitosis vs meiosis), Visuals (pathway diagrams), Named Entities (species, organelles), Design Paradigms (PCR, CRISPR, sequencing), Case Studies (Mendel, Meselson-Stahl), Mnemonics, Self-Test Templates, Formulas, Edge Cases, Proof Patterns |
| Math | Formulas, Laws/Theorems, Sequential Processes (proof patterns), Proof Patterns (induction, contradiction), Hierarchies (number systems, function classes), Comparisons, People/Dates, Empirical Evidence, Ethics |
| Physics | Formulas, Laws/Theorems, Sequential Processes (derivations), Visuals (free-body, circuits), Edge Cases (limiting behavior), Proof Patterns, People/Dates, Hierarchies, Ethics |
| Chemistry | Formulas (reactions), Sequential Processes (syntheses), Hierarchies (periodic trends), Visuals (mechanisms), Named Entities (compounds), Design Paradigms (spectroscopy, chromatography), Comparisons, Empirical Evidence, Ethics |
| Medicine | Sequential Processes (pathways, diagnostic algorithms), Hierarchies (disease classifications), Comparisons (differential diagnosis), Edge Cases (atypical presentations), Empirical Evidence (trials), Case Studies, Ethics (informed consent, animal testing), Formulas, Visuals, Proof Patterns |
| Engineering | Formulas (design equations), Sequential Processes (methods), Comparisons (material trade-offs), Edge Cases (failure modes), Visuals (schematics), Design Paradigms, Named Entities, People/Dates, Ethics |
| Law | Rules/Laws/Theorems (doctrines), Hierarchies (court system), Comparisons (burden of proof standards), People/Dates (landmark cases), Edge Cases (exceptions), Case Studies, Formulas, Sequential Processes, Ethics |
| History / Social Sciences | People/Dates, Sequential Processes (causation chains), Comparisons (ideologies, regimes), Hierarchies (government structures), Empirical Evidence (statistics), Case Studies, Ethics, Formulas, Visuals, Proof Patterns |
