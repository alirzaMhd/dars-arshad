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

Before asking, count the total number of lines in the book file (e.g., `wc -l <book>.txt`) and tell the user: **"The book is approximately <N> lines long. For 20/20 exam readiness, a comprehensive guide typically runs 1.5–3× the book's line count."**

Then ask: **"How many lines would you like the study guide to be approximately?"** Offer these options:
- **Comprehensive (no limit)** — extract everything, no compression (default, strongly recommended for 20/20)
- **~2000 lines** — trimmed (only suitable for short books or last-minute review)
- **~1000 lines** — concise (NOT suitable for 20/20, only for overview)
- **Custom** — let them type a number

**IMPORTANT**: If the user selects anything other than "Comprehensive", add a warning: *"Shorter guides skip worked examples, end-of-chapter material, edge cases, visual diagrams, mnemonics, self-test templates, and cross-chapter links — which are essential for 20/20 exam readiness. Recommend Comprehensive unless this is a last-minute review."* Store their final choice as `$OUTPUT_LINES`.

If they choose "Comprehensive" (or don't specify), extract everything with no length limit — every primitive, every example, every formula, every exercise. If they choose a specific number, respect that target but NEVER skip primitives wholesale; instead, be more concise within each primitive rather than dropping primitives.

Update the study guide header to include: `> طول هدف: <value> خط.`

**Hard rule: A study guide under 500 lines cannot achieve 20/20 coverage for any book over 200 lines. If you are producing a guide that short, inform the user that it will be insufficient for full exam preparation.**

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
2. Run the **universal extraction checklist** below. **Check every category.** If a category has zero content in that chapter, write `None in this chapter.` rather than skipping. This systematic sweep ensures nothing examinable is missed.
3. **Include all content**, not just highlights. Every named entity, every process step, every formula, every comparison, every edge case, every case study — extract it all.
4. **Keep examples and anecdotes** if they help understand the concept. Do not drop them aggressively — only remove truly redundant repetition.
5. Note any cross-chapter links discovered

**Minimum primitive requirements per chapter:**
- Every chapter MUST include at least **10 of the 17 primitives** populated with real content (not "None").
- The following 8 primitives are **MANDATORY in every chapter** and may only be skipped if genuinely zero content exists in the source:
  1. Named Entities
  2. Sequential Processes
  3. Classifications / Hierarchies
  4. Comparisons / Trade-offs
  5. Formulas & Equations (or Rules/Laws/Theorems for non-quantitative chapters)
  6. Edge Cases / Traps
  7. Visual Patterns (text-described diagrams)
  8. End-of-Chapter Material
- A chapter with fewer than 8 primitives populated is a **quality failure**. Re-read the chapter and extract more deeply.
- For CS chapters, Data Structures & Types (#7) is also mandatory.

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

**Quality benchmark**: A student should be able to read ONLY this guide and score 20/20 on the exam. If any section would force the student to open the original book, you need more detail.

### Step 5 — Write the comprehensive study guide (in Persian)

**IMPORTANT: All output text must be written in Persian (Farsi).** Technical terms (e.g., algorithm names, variable names, keywords) should be kept in their original English/Latin form for clarity, but all surrounding explanation, definitions, descriptions, section headers, and commentary must be in Persian.

Save as `راهنمای-مطالعه-<book-title>-<YYYY-MM-DD>.md` with the template below. **Every chapter MUST use ALL the following sections** (in this exact order). For any section with no content, write `None in this chapter.` — do NOT skip or remove the section. Do NOT reorder sections by content heaviness; use the prescribed order.

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
- **مثال**: یک مثال عینی با **اعداد مشخص** (نه متغیر) ارائه شود

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
- **محاسبه نمونه**: با اعداد مشخص، عملیات حسابی نشان داده شود

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

#### ارتباطات بین‌فصلی
- **نیازمند دانش**: فصل X (مفهوم)، فصل Y (الگوریتم)
- **ارجاع در فصول بعدی**: فصل Z
- **پتانسیل تلفیق**: سؤالات امتحانی ممکن است این فصل را با فصل X و Y ترکیب کنند

### فصل ۲ — <عنوان>
... (همان ساختار، بایستی شامل تمام بخش‌های بالا باشد)

---

## موضوعات بین‌بخشی

### پارادایم‌های طراحی و روش‌های فراتر
(استخراج‌شده از تمام فصول، با ارجاع به فصل‌ها)

### الگوهای اثبات و استدلال
(استخراج‌شده از تمام فصول، با ارجاع به فصل‌ها)

### مبانی احتمال و آمار
(استخراج‌شده از تمام فصول)

### فنون حافظه و کمک‌حافظه‌ها
(استخراج‌شده از تمام فصول)

### افراد و تاریخ‌ها
(استخراج‌شده از تمام فصول)

---

## سؤالات امتحانی بر اساس نوع

حداقل تولید شود:
- **۱۰ سؤال چندگزینه‌ای (MCQ)**
- **۵ سؤال پاسخ کوتاه**
- **۵ سؤال ردیابی / اعمال** (با راه‌حل کامل)
- **۵ سؤال برچسب‌گذاری نمودار** (با معیار نمره‌دهی)
- **۵ سؤال مقاله / پاسخ بلند** (با نکات کلیدی)

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

### Step 6 — Verify before saving — PASS/FAIL CHECKLIST

Run through EVERY item below. If any item FAILs, fix the issue before saving.

**Coverage checks:**
- [ ] Every chapter in the book is covered (count matches the index) — **FAIL if any chapter missing**
- [ ] Every chapter has at least 10 of 17 primitives populated with real content — **FAIL if any chapter has fewer**
- [ ] Cross-Chapter Links section exists in every chapter — **FAIL if missing from any**
- [ ] All explanatory text is in Persian (Farsi) — **FAIL if English used for non-technical content**

**Primitive depth checks (per chapter):**
- [ ] All process steps are complete (not truncated) — a student could follow them without the original book — **FAIL if any step is vague or incomplete**
- [ ] Every worked example uses specific numeric values, not variables — **FAIL if any example uses only variables**
- [ ] Every formula has every variable defined with units/constraints — **FAIL if any variable is undefined**
- [ ] Comparisons use identical dimensions across both sides — **FAIL if dimensions differ**
- [ ] Case studies include all four: What, Method, Results (with numbers), Significance — **FAIL if any is missing**
- [ ] End-of-chapter material is fully reproduced (bolded terms, review questions, exercises) — **FAIL if any exercise is missing**
- [ ] At least one visual/text diagram per chapter (search trees, pathways, architectures, etc.) — **FAIL if absent**

**Cross-cutting checks:**
- [ ] Design Paradigms section exists with chapter references — **FAIL if missing**
- [ ] Proof & Argument Patterns section exists with chapter references — **FAIL if missing**
- [ ] Probability & Statistics section exists (if source uses any stats) — **FAIL if missing**
- [ ] Mnemonics section exists with at least 5 mnemonics — **FAIL if fewer**
- [ ] People & Dates section exists — **FAIL if missing**
- [ ] Ethics topics are extracted wherever present in the source — **FAIL if ethics content is ignored**

**Exam questions checks:**
- [ ] At least 10 MCQ with correct answers and distractor explanations — **FAIL if fewer**
- [ ] At least 5 Short Answer with rubrics — **FAIL if fewer**
- [ ] At least 5 Trace/Apply with full worked solutions — **FAIL if fewer**
- [ ] At least 5 Diagram Label prompts — **FAIL if fewer**
- [ ] At least 5 Essay questions with key points — **FAIL if fewer**

**Self-containment check:**
- [ ] **No section forces a student to open the original book** — if any section would be unclear without the source, add more detail — **FAIL if any such section exists**
- [ ] End-of-chapter exercises include solutions — **FAIL if solutions are missing**

After passing all checks, save the file. If any check FAILs, go back and fix the content, then re-run the full checklist.

### Step 7 — Line count conformance (if target was specified)

If the user chose a specific line target (not "Comprehensive"):

1. **Count the output**: `wc -l <study-guide-file>`
2. **Check against target**: The output must be within ±10% of the target (e.g., ~2000 target → 1800–2200 lines acceptable).
3. **If over target**: Trim by applying these rules in order (start from the least critical):
   - First: condense verbose explanations and narrative prose (keep facts, cut fluff)
   - Second: remove redundant examples (keep the clearest one per concept)
   - Third: shorten Exam Questions section (minimum floor: 5 MCQ, 3 Short Answer, 3 Trace, 3 Diagram, 3 Essay)
   - Fourth: shorten worked examples (keep the math, trim the narrative walkthrough)
   - **NEVER remove**: entire primitives, end-of-chapter material, or any chapter's Cross-Chapter Links
   - **NEVER drop below 8 primitives per chapter** — if trimming would violate this, inform the user that the target is too low for 20/20 quality
4. **If under target by more than 50%**: this signals insufficient depth. Re-read the book and add missing content rather than padding.
5. **Re-run Step 6 checklist** after trimming to ensure no pass condition was violated.

### Step 8 — 20/20 certification check (FINAL GATE)

Before delivering the study guide to the user, run this certification as an independent self-check. Every item MUST pass:

```
╔══════════════════════════════════════════════════════════╗
║              20/20 STUDY GUIDE CERTIFICATION            ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  [  PASS / FAIL  ]  All chapters from the book are       ║
║                     covered (count matches index)        ║
║                                                          ║
║  [  PASS / FAIL  ]  Every chapter has ≥10 of 17          ║
║                     primitives with real content         ║
║                                                          ║
║  [  PASS / FAIL  ]  Every chapter has 8 mandatory        ║
║                     primitives (Named Entities,          ║
║                     Processes, Classifications,          ║
║                     Comparisons, Formulas/Rules,         ║
║                     Edge Cases, Visuals, End-of-Chapter) ║
║                                                          ║
║  [  PASS / FAIL  ]  Every process has complete steps     ║
║                     — a student can follow them          ║
║                     without the original book            ║
║                                                          ║
║  [  PASS / FAIL  ]  Every algorithm/formula/process      ║
║                     has ≥1 worked example with           ║
║                     specific numeric values              ║
║                                                          ║
║  [  PASS / FAIL  ]  Every formula has all variables      ║
║                     defined with units/constraints       ║
║                                                          ║
║  [  PASS / FAIL  ]  Every chapter has a text-described   ║
║                     visual diagram (ASCII or structured) ║
║                                                          ║
║  [  PASS / FAIL  ]  Every chapter has Cross-Chapter      ║
║                     Links section                        ║
║                                                          ║
║  [  PASS / FAIL  ]  Every chapter has End-of-Chapter     ║
║                     material (key terms, review          ║
║                     questions, exercises with solutions) ║
║                                                          ║
║  [  PASS / FAIL  ]  Cross-cutting sections exist:        ║
║                     Design Paradigms, Proof Patterns,    ║
║                     Probability & Stats, Mnemonics (≥5), ║
║                     People & Dates                       ║
║                                                          ║
║  [  PASS / FAIL  ]  Exam questions meet minimums:        ║
║                     10 MCQ, 5 Short Answer, 5 Trace,     ║
║                     5 Diagram, 5 Essay                   ║
║                                                          ║
║  [  PASS / FAIL  ]  No section requires the original     ║
║                     book — fully self-contained          ║
║                                                          ║
║  [  PASS / FAIL  ]  Line count matches user's target     ║
║                     (if specified, within ±10%)          ║
║                                                          ║
║  [  PASS / FAIL  ]  Ethics content captured wherever     ║
║                     present in source                    ║
║                                                          ║
║  [  PASS / FAIL  ]  All text is in Persian (Farsi),     ║
║                     technical terms may remain English   ║
║                                                          ║
║══════════════════════════════════════════════════════════║
║                                                          ║
║  OVERALL: [  CERTIFIED 20/20  /  NOT YET  ]             ║
║                                                          ║
║  If NOT YET: list each FAIL reason, fix the content,     ║
║  re-run Steps 6–8 from scratch. Do NOT deliver until     ║
║  OVERALL = CERTIFIED 20/20.                              ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

Copy this certification block into the final delivery message to the user, filled in with PASS/FAIL results for each row and the OVERALL result. This makes the quality assessment transparent and auditable.

## Rules

- **Never invent content.** If a chapter is missing or unreadable, say so in the output.
- **Systematic extraction is mandatory.** Run every category in the universal checklist against every chapter. Do not skip categories preemptively — let the content decide.
- **Minimum 10 primitives per chapter.** Every chapter MUST have at least 10 of 17 primitives with substantial content. Chapters with fewer are quality failures — re-read and extract deeper.
- **Be comprehensive, not compressed.** Include every named entity, every process step, every formula, every comparison, every edge case. The goal is that the reader can learn solely from the study guide without needing the original book.
- **Self-containment is the test.** If a student would need to open the original book to understand any concept, formula, or process, the guide is insufficient. Add more detail.
- **Preserve the author's framing** for theories, definitions, and named items — paraphrase only connective tissue.
- **Surface exam signals**: repetition, bold text, summary boxes, "key" / "important" / "remember" — these are almost always testable.
- **Reproduce end-of-chapter material verbatim in every chapter.** Bolded terms, key points boxes, review questions, and exercises are the single most exam-relevant content in any textbook. Include them fully with solutions.
- **Generate mnemonics proactively.** If a list of 5+ items must be memorized (e.g., Big-O ordering, Krebs cycle intermediates, Kings of England), invent an acronym, rhyme, or chunk for it. Add to the Mnemonics cross-cutting section.
- **Generate self-test templates for any process/algorithm with ≥5 steps.** Leave blanks for key steps, inputs, or outputs so the student can fill them from memory. Reference the answer location.
- **Capture ethics wherever present.** If the source discusses ethics (AI safety, animal testing, informed consent, dual-use), extract it as a dedicated item in the relevant chapter and in the cross-cutting topics.
- **Prioritize technical content** over narrative. Include both the formula and the explanatory context needed to understand it.
- **Every algorithm, formula, or process MUST have at least one concrete worked example with specific numeric values.** Variables alone are insufficient. Show the arithmetic.
- **Every chapter MUST have a text-described visual diagram** (ASCII art or structured text description) that can be redrawn from memory.
- **Every chapter MUST have explicit Cross-Chapter Links** noting dependencies and forward references.
- **Respect copyright.** Do not reproduce long verbatim passages. Brief quotes (≤25 words) for definitions are fine. Pseudocode and small code snippets (≤15 lines) that are idiomatic/canonical are fine. End-of-chapter material is typically short enough to include.
- **No filler.** No "in this chapter we learned...". No "as discussed earlier". Just the facts.
- **Structured over prose.** Use lists, tables, ASCII diagrams, and equations. Minimize paragraphs.
- **There is no length limit.** Do not truncate or abbreviate content to save space. If coverage of a chapter requires 200 bullets, write 200 bullets. A 20/20 study guide for a 1000-page textbook may be 5000+ lines.
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
