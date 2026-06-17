# Test Prep App — Design Spec

## Overview

A standalone Flask web application for exam test preparation. Users enter their lesson's chapter structure and exam history, the app recommends how many practice questions to solve per chapter based on past exam frequency, then generates an interactive printable answer sheet with 1/2/3/4 ovals.

## Architecture

### Folder Structure

```
test_prep_app/
├── app.py                  # Flask server (routes + JSON persistence)
├── data/
│   └── lessons/
│       └── <lesson_id>.json
├── static/
│   ├── style.css
│   └── app.js
└── templates/
    └── index.html          # Single-page wizard
```

### Tech Stack

- **Backend**: Flask (Python), JSON file persistence
- **Frontend**: Vanilla HTML/CSS/JS (no frameworks)
- **Port**: 8082 (separate from tts_app on 8081)

## Data Model

### Lesson JSON Schema

```json
{
  "id": "string (slug from lesson name + timestamp)",
  "name": "string (e.g., 'Algorithm')",
  "chapters": [
    {
      "number": "int (1-indexed)",
      "name": "string (e.g., 'Chapter 1')",
      "questions_in_book": "int (user input)",
      "questions_in_exams": "int (user input, 0-10)",
      "recommended": "int (auto-calculated, user-overridable)",
      "selected_count": "int (final count to use)",
      "selected_distribution": "string (one of: center, spaced_start, spaced_end, normal)",
      "question_numbers": "int[] (computed from distribution)",
      "answers": "object (map of question_number -> selected answer 1-4)"
    }
  ],
  "created_at": "ISO timestamp",
  "updated_at": "ISO timestamp"
}
```

### Recommendation Formula

```
frequency = questions_in_exams / 10
recommended = max(5, round(frequency * questions_in_book))
recommended = min(recommended, questions_in_book)
```

- Minimum floor: **5 questions** (even if chapter had 0 exam appearances)
- Maximum cap: total questions in book
- Example: 2 exam questions, 25 in book → `max(5, round(0.2 × 25))` = 5
- Example: 5 exam questions, 30 in book → `max(5, round(0.5 × 30))` = 15

## UI Flow

### Step 1 — Lesson Setup

- Input field: lesson name (e.g., "Algorithm")
- Number input: chapter count
- "Start" button → generates chapter data table for Step 2

### Step 2 — Chapter Data Table

Table with one row per chapter:

| Chapter | Questions in Book | Questions in Past 10 Exams | Recommended |
|---------|-------------------|----------------------------|-------------|
| Ch 1    | [number input]    | [number input]             | [auto-calc] |
| Ch 2    | [number input]    | [number input]             | [auto-calc] |
| ...     |                   |                            |             |

- "Recommended" column updates live as user types in book/exam columns
- User can click and override the recommended value directly (the override becomes `selected_count`)
- If user does not override, `selected_count` = `recommended`
- "Generate Answer Sheet" button at bottom (enabled when all rows have valid data)

### Step 3 — Answer Sheet

**Chapter selector**: tabs or dropdown to switch between chapters

**Distribution options** (radio buttons per chapter):
- **Center of each group** (default) — divide N questions into K groups, pick center of each
- **Evenly spaced from 1** — start at 1, step = N/K
- **Evenly spaced ending at last** — end at N, step = N/K
- **Normal distribution** — bell-curve weighted, more selections from middle

**Question number cards**: horizontal row showing selected question numbers as clickable cards. Active card is highlighted.

**Oval grid**: for the active question, show 4 ovals labeled 1, 2, 3, 4
- Click oval → fills in (selected)
- Click different oval → switches selection
- Click same oval again → deselects (empty)

**Navigation**: "Prev" / "Next" buttons or click question number cards to jump

**Print**: "Print Answer Sheet" button → `window.print()` with `@media print` CSS that shows only the clean answer sheet layout

## Question Distribution Algorithms

Given N total questions in a chapter, selecting K questions:

### Center of Each Group (default)
```
group_size = N / K
for i in 0..K-1:
    position = round(i * group_size + group_size / 2)
    clamp to [1, N]
```
Example: N=25, K=5 → positions 3, 8, 13, 18, 23

### Evenly Spaced from 1
```
step = N / K (rounded)
positions = [1, 1+step, 1+2*step, ...]
```
Example: N=25, K=5 → 1, 6, 11, 16, 21

### Evenly Spaced Ending at Last
```
step = N / K (rounded)
positions = [N-K*step+step, ..., N]
```
Example: N=25, K=5 → 5, 10, 15, 20, 25

### Normal Distribution
```
mean = N / 2
stddev = N / 6
for i in 0..K-1:
    # K evenly-spaced quantiles of a normal distribution
    p = (i + 0.5) / K
    z = inverse_normal_cdf(p)  # or approximate via Box-Muller
    position = round(mean + z * stddev)
    clamp to [1, N]
sort positions, deduplicate
```
Example: N=25, K=7 → biased toward positions 8-18, with fewer at edges

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Serve index.html |
| GET | `/api/lessons` | List all saved lessons |
| POST | `/api/lessons` | Create new lesson |
| GET | `/api/lessons/<id>` | Get lesson data |
| PUT | `/api/lessons/<id>` | Update lesson (chapters, answers) |
| DELETE | `/api/lessons/<id>` | Delete lesson |
| POST | `/api/lessons/<id>/compute` | Recompute question numbers for a chapter |

## Persistence

- Lessons saved as JSON files in `data/lessons/<lesson_id>.json`
- Created on Step 1, updated on each step
- Answer selections saved in real-time
- Lesson listing reads from the data directory

## Print Styling

`@media print` CSS:
- Hide: navigation buttons, distribution controls, sidebar
- Show: lesson name, chapter labels, question numbers with empty 1/2/3/4 ovals
- Black and white, clean layout
- Ovals: unfilled circles with numbers inside
