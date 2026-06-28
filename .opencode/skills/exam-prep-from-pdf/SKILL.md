---
name: exam-prep-from-pdf
description: Use when generating exam study materials from PDF textbooks with question-answer analysis. Extracts tricky questions, hidden tips not in explanations, and basic questions. Creates interactive HTML files with creative design for exam preparation.
---

# Exam Prep from PDF

## Overview

Analyzes PDF textbook chapters by cross-referencing questions with their answer sheets and the textbook explanation section. Identifies three categories of study material:
1. **Tricky Questions** - questions with common traps, counterintuitive answers, or frequently misunderstood concepts
2. **Hidden Tips & Points** - important concepts in answers that are NOT explained in the textbook section
3. **Basic Questions** - fundamental questions every student must solve for the chapter

Outputs everything in a visually creative, interactive HTML file.

## When to Use

- User has a PDF with questions (exercises) and wants exam preparation materials
- User wants to identify tricky questions before an exam
- User wants to find concepts in answers that the textbook doesn't explain
- User wants a curated list of must-solve basic questions
- User says "analyze this chapter's questions", "exam prep from questions", "find tricky questions"

**Do NOT use when:**
- User wants full study notes (use `cram-notes` instead)
- User wants topic explanations only (use `textbook-to-html` instead)
- PDF contains no questions or answer sheets

## Input Requirements

The user must provide:

| Input | Description | Required |
|-------|-------------|----------|
| **PDF file** | Path to the textbook PDF | Yes |
| **Chapter name** | Name/title of the chapter | Yes |
| **Chapter pages** | Page range containing the questions/exercises | Yes |
| **Textbook section** | Page range containing the explanation/theory for this chapter | Yes |
| **Answer sheet** (optional) | Page range or separate file with full answers | Recommended |

## Workflow

```dot
digraph exam_prep {
    "Collect Inputs" [shape=box];
    "Extract Text from PDF" [shape=box];
    "Parse Questions" [shape=box];
    "Parse Answers" [shape=box];
    "Parse Explanation Section" [shape=box];
    "Analyze Each Question" [shape=box];
    "Classify: Tricky / Hidden-Tip / Basic" [shape=box];
    "Generate HTML Report" [shape=box];
    "Verify Completeness" [shape=box];
    "Deliver to User" [shape=doublecircle];

    "Collect Inputs" -> "Extract Text from PDF";
    "Extract Text from PDF" -> "Parse Questions";
    "Extract Text from PDF" -> "Parse Answers";
    "Extract Text from PDF" -> "Parse Explanation Section";
    "Parse Questions" -> "Analyze Each Question";
    "Parse Answers" -> "Analyze Each Question";
    "Parse Explanation Section" -> "Analyze Each Question";
    "Analyze Each Question" -> "Classify: Tricky / Hidden-Tip / Basic";
    "Classify: Tricky / Hidden-Tip / Basic" -> "Generate HTML Report";
    "Generate HTML Report" -> "Verify Completeness";
    "Verify Completeness" -> "Deliver to User";
}
```

## Phase 1: Extract Content from PDF

### Extract Questions
```bash
python3 -c "
from pypdf import PdfReader
reader = PdfReader('textbook.pdf')
for i, page_num in enumerate(range(QUESTION_START-1, QUESTION_END)):
    print(f'=== QUESTION PAGE {page_num+1} ===')
    print(reader.pages[page_num].extract_text())
" > questions_extracted.txt
```

### Extract Answers
```bash
python3 -c "
from pypdf import PdfReader
reader = PdfReader('textbook.pdf')
for i, page_num in enumerate(range(ANSWER_START-1, ANSWER_END)):
    print(f'=== ANSWER PAGE {page_num+1} ===')
    print(reader.pages[page_num].extract_text())
" > answers_extracted.txt
```

### Extract Explanation Section
```bash
python3 -c "
from pypdf import PdfReader
reader = PdfReader('textbook.pdf')
for i, page_num in enumerate(range(EXPLANATION_START-1, EXPLANATION_END)):
    print(f'=== EXPLANATION PAGE {page_num+1} ===')
    print(reader.pages[page_num].extract_text())
" > explanation_extracted.txt
```

**Read all three files completely before proceeding.**

## Phase 2: Parse and Structure

### Questions Parser
For each question, extract:
- **Question number** (e.g., Q1, Q2, Exercise 3.1)
- **Full question text** (verbatim)
- **Topic/concept** being tested
- **Difficulty indicators** (multi-step, requires synthesis, uses edge case)

### Answers Parser
For each answer, extract:
- **Question number** (matched to question)
- **Full solution/description** (complete reasoning)
- **Key steps** in the solution
- **Common mistakes** mentioned or implied
- **Formulas/concepts** used

### Explanation Section Parser
For each concept in the explanation, extract:
- **Concept name**
- **Full explanation text**
- **Examples provided**
- **Key formulas/rules stated**
- **Tips or warnings explicitly given**

## Phase 3: Analyze Each Question

For EVERY question, perform this analysis:

### 1. Tricky Question Detection

A question is **tricky** if it has ANY of:
- **Counterintuitive answer** - the correct answer contradicts common intuition
- **Common trap** - most students pick a specific wrong answer for a known reason
- **Misread potential** - question wording easily leads to wrong interpretation
- **Exception handling** - the answer depends on an edge case or special condition
- **Multi-concept trap** - requires combining concepts where students typically miss one
- **Notation trap** - uses similar notation for different things, or ambiguous notation
- **Boundary condition** - answer changes at specific boundary values
- **Assumption trap** - correct answer requires noticing an unstated assumption

**Score each tricky indicator:**
- `tricky_score` = count of indicators present (0-8)
- `tricky_reasons` = list of which indicators are present

### 2. Hidden Tips Detection

For each question's answer, compare against the explanation section:

```
For each concept C in answer:
    If C is NOT fully explained in textbook section:
        → This is a HIDDEN TIP
        → Record: concept, where it appears, why it matters
```

**Hidden tip types:**
- **Unstated prerequisite** - knowledge assumed but not taught in this chapter
- **Extended formula** - formula used in answer but not derived in explanation
- **Shortcut method** - efficient approach not covered in theory
- **Real-world application** - practical use not mentioned in textbook
- **Deeper insight** - reasoning that goes beyond surface explanation
- **Cross-topic connection** - links to concepts from other chapters
- **Intuition builder** - mental model not provided in textbook

### 3. Basic Question Detection

A question is **basic** (must-solve) if it:
- Tests a core concept that appears in >50% of exam patterns
- Is explicitly labeled as fundamental/important in the textbook
- Has a straightforward solution using only chapter's main formulas
- Is a prerequisite for understanding harder questions in the chapter
- Tests a definition, formula, or process that must be memorized
- Appears in multiple past exams or is referenced as "classic"

**Score basic importance:**
- `basic_score` = 1-5 scale (5 = absolutely must solve)
- `basic_reasons` = why this is fundamental

## Phase 4: Generate HTML Report

### HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exam Prep: [Chapter Name]</title>
    <style>
        /* Creative dark theme with neon accents */
        :root {
            --bg-primary: #0a0a1a;
            --bg-secondary: #12122a;
            --bg-card: #1a1a3a;
            --text-primary: #e0e0ff;
            --text-secondary: #8888aa;
            --accent-tricky: #ff4466;
            --accent-hidden: #44ff88;
            --accent-basic: #4488ff;
            --accent-gold: #ffaa00;
            --glow-tricky: 0 0 20px rgba(255,68,102,0.3);
            --glow-hidden: 0 0 20px rgba(68,255,136,0.3);
            --glow-basic: 0 0 20px rgba(68,136,255,0.3);
        }
        /* ... full CSS ... */
    </style>
</head>
<body>
    <!-- Header with chapter stats -->
    <!-- Tab navigation: Tricky | Hidden Tips | Basic | All Questions -->
    <!-- Question cards with expandable details -->
    <!-- Summary statistics -->
</body>
</html>
```

### Creative Design Elements

1. **Animated Background** - subtle particle effect or gradient animation
2. **Color-Coded Cards** - red for tricky, green for hidden tips, blue for basic
3. **Glowing Borders** - neon glow effect on hover for each category
4. **Progress Tracker** - visual checklist of questions analyzed
5. **Difficulty Meter** - animated gauge showing tricky_score
6. **Collapsible Sections** - click to expand question details
7. **Search/Filter** - filter by category, difficulty, topic
8. **Print Mode** - clean layout for printing
9. **Dark/Light Toggle** - theme switcher
10. **Statistics Dashboard** - pie chart of question categories

### Required Sections in HTML

#### Section 1: Dashboard Header
```
Chapter: [Name]
Total Questions: N
Tricky: N (XX%)
Hidden Tips: N
Basic Must-Solve: N
Analysis Date: [Date]
```

#### Section 2: Tricky Questions (Red Theme)
For each tricky question:
```html
<div class="question-card tricky">
    <div class="card-header">
        <span class="badge">TRICKY</span>
        <span class="difficulty">Difficulty: ●●●○○</span>
        <span class="question-num">Q3</span>
    </div>
    <div class="question-text">
        [Full question text]
    </div>
    <div class="tricky-reasons">
        <h4>Why This Is Tricky:</h4>
        <ul>
            <li>Counterintuitive answer</li>
            <li>Common trap: most students pick B</li>
        </ul>
    </div>
    <div class="answer-walkthrough">
        <h4>Full Solution:</h4>
        [Complete step-by-step solution]
    </div>
    <div class="key-insight">
        <h4>Key Insight:</h4>
        [The one thing to remember]
    </div>
</div>
```

#### Section 3: Hidden Tips (Green Theme)
For each hidden tip:
```html
<div class="question-card hidden-tip">
    <div class="card-header">
        <span class="badge">HIDDEN TIP</span>
        <span class="tip-type">Unstated Prerequisite</span>
    </div>
    <div class="tip-content">
        <h4>What the textbook doesn't explain:</h4>
        [Concept not in explanation section]
    </div>
    <div class="appears-in">
        <h4>Appears in these questions:</h4>
        <span class="question-ref">Q5, Q12, Q18</span>
    </div>
    <div class="why-it-matters">
        <h4>Why This Matters:</h4>
        [Why you need to know this]
    </div>
</div>
```

#### Section 4: Basic Must-Solve (Blue Theme)
For each basic question:
```html
<div class="question-card basic">
    <div class="card-header">
        <span class="badge">BASIC - MUST SOLVE</span>
        <span class="importance">Importance: ★★★★★</span>
    </div>
    <div class="question-text">
        [Full question text]
    </div>
    <div class="why-basic">
        <h4>Why This Is Fundamental:</h4>
        [Reason it's a must-solve]
    </div>
    <div class="solution">
        <h4>Solution:</h4>
        [Step-by-step solution]
    </div>
    <div class="memorize">
        <h4>Memorize This:</h4>
        [Key formula or concept to memorize]
    </div>
</div>
```

#### Section 5: Statistics & Summary
```html
<div class="stats-dashboard">
    <div class="stat-card">
        <div class="stat-number">12</div>
        <div class="stat-label">Tricky Questions</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">8</div>
        <div class="stat-label">Hidden Tips</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">15</div>
        <div class="stat-label">Basic Must-Solve</div>
    </div>
</div>
```

## Phase 5: Verification Checklist

Before delivering, verify:

- [ ] Every question from the chapter is analyzed
- [ ] Every tricky question has: question text, reasons, full solution, key insight
- [ ] Every hidden tip has: concept, which questions it appears in, why it matters
- [ ] Every basic question has: importance rating, solution, memorize-this item
- [ ] HTML renders correctly in browser
- [ ] All interactive elements work (tabs, expand/collapse, filter)
- [ ] Statistics match actual counts
- [ ] No question is left uncategorized

## Rules

- **Never skip questions.** Analyze EVERY question from the chapter.
- **Be specific with reasons.** "Tricky" is not enough — explain WHY.
- **Include full solutions.** Don't just say "see answer" — write out the complete solution.
- **Cross-reference thoroughly.** Check every answer concept against the explanation section.
- **Creative but readable.** Design should enhance, not distract from content.
- **Print-friendly.** Ensure the HTML prints cleanly for offline study.
- **Mobile responsive.** Must work on phones for studying on the go.

## Example Usage

```
User: "Analyze chapter 3 questions from data-structures.pdf"
User: "Chapter name: Linked Lists"
User: "Question pages: 45-52"
User: "Explanation section: 38-44"
User: "Answers: pages 200-205"

Agent:
1. Extract questions from pages 45-52
2. Extract answers from pages 200-205
3. Extract explanation from pages 38-44
4. Analyze each question against answers and explanation
5. Classify: 8 tricky, 5 hidden tips, 12 basic must-solve
6. Generate linked-lists-exam-prep.html with creative design
7. Deliver: "Created exam prep with 25 analyzed questions"
```

## File Naming

`[chapter-name]-exam-prep.html`

Examples:
- `linked-lists-exam-prep.html`
- `binary-trees-exam-prep.html`
- `graph-algorithms-exam-prep.html`

## Integration

- Use with `cram-notes` for comprehensive study notes
- Use with `textbook-to-html` for topic explanations
- Use with `algorithm-animation` for interactive algorithm demos
