# Test Prep App Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a standalone Flask web app for exam test preparation with a single-page wizard that recommends practice question counts per chapter and generates an interactive printable answer sheet.

**Architecture:** Single-page Flask app with vanilla JS frontend. JSON file persistence. Three-step wizard: lesson setup → chapter data table → answer sheet with oval selection.

**Tech Stack:** Flask, vanilla HTML/CSS/JS, JSON files, Python 3

## Global Constraints

- Port 8082 (separate from tts_app on 8081)
- Minimum 5 questions per chapter regardless of exam frequency
- 4 distribution algorithms: center, spaced_start, spaced_end, normal
- Answer sheet uses 1/2/3/4 ovals (not A/B/C/D)
- Print-friendly via `@media print` CSS
- No external JS frameworks — vanilla JS only

---

## File Structure

| File | Responsibility |
|------|---------------|
| `test_prep_app/app.py` | Flask server, routes, JSON persistence |
| `test_prep_app/data/lessons/` | Directory for lesson JSON files |
| `test_prep_app/static/style.css` | All styles including print |
| `test_prep_app/static/app.js` | Wizard logic, distribution algorithms, oval interaction |
| `test_prep_app/templates/index.html` | Single-page wizard HTML |
| `test_prep_app/requirements.txt` | Python dependencies (flask, flask-cors) |

---

### Task 1: Project Scaffolding

**Files:**
- Create: `test_prep_app/app.py`
- Create: `test_prep_app/requirements.txt`
- Create: `test_prep_app/data/lessons/` (directory)

**Interfaces:**
- Consumes: none
- Produces: running Flask server on port 8082, `GET /` returns 200

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p test_prep_app/data/lessons test_prep_app/static test_prep_app/templates
```

- [ ] **Step 2: Create requirements.txt**

```
flask>=3.0
flask-cors>=4.0
```

- [ ] **Step 3: Create minimal app.py**

```python
import os
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data', 'lessons')
os.makedirs(DATA_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=False, threaded=True)
```

- [ ] **Step 4: Install dependencies and verify server starts**

```bash
pip install -r test_prep_app/requirements.txt
```

Run: `python test_prep_app/app.py &` then `curl -s http://localhost:8082/`
Expected: 200 response (will fail with template not found — that's OK, confirms server runs)

- [ ] **Step 5: Create minimal index.html template**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Prep</title>
</head>
<body>
    <h1>Test Prep App</h1>
</body>
</html>
```

Write to: `test_prep_app/templates/index.html`

- [ ] **Step 6: Verify server serves the page**

```bash
curl -s http://localhost:8082/
```

Expected: HTML with "Test Prep App" heading

- [ ] **Step 7: Commit**

```bash
git add test_prep_app/
git commit -m "feat(test-prep): project scaffolding with Flask server"
```

---

### Task 2: JSON Persistence Layer

**Files:**
- Modify: `test_prep_app/app.py` (add persistence functions)

**Interfaces:**
- Consumes: Flask app from Task 1
- Produces: `save_lesson(data)`, `load_lesson(id)`, `list_lessons()`, `delete_lesson(id)` functions

- [ ] **Step 1: Write the failing test**

Create: `test_prep_app/test_persistence.py`

```python
import os
import sys
import json
import tempfile
import shutil

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from app import save_lesson, load_lesson, list_lessons, delete_lesson, DATA_DIR

def test_save_and_load():
    test_dir = tempfile.mkdtemp()
    import app
    original = app.DATA_DIR
    app.DATA_DIR = test_dir
    try:
        lesson = {
            'id': 'test-1',
            'name': 'Algorithm',
            'chapters': [],
            'created_at': '2026-06-17',
            'updated_at': '2026-06-17'
        }
        save_lesson(lesson)
        loaded = load_lesson('test-1')
        assert loaded is not None
        assert loaded['name'] == 'Algorithm'
        assert loaded['id'] == 'test-1'
    finally:
        app.DATA_DIR = original
        shutil.rmtree(test_dir)

def test_list_lessons():
    test_dir = tempfile.mkdtemp()
    import app
    original = app.DATA_DIR
    app.DATA_DIR = test_dir
    try:
        for i in range(3):
            save_lesson({'id': f'les-{i}', 'name': f'Lesson {i}', 'chapters': [], 'created_at': '', 'updated_at': ''})
        lessons = list_lessons()
        assert len(lessons) == 3
    finally:
        app.DATA_DIR = original
        shutil.rmtree(test_dir)

def test_delete_lesson():
    test_dir = tempfile.mkdtemp()
    import app
    original = app.DATA_DIR
    app.DATA_DIR = test_dir
    try:
        save_lesson({'id': 'del-me', 'name': 'Delete', 'chapters': [], 'created_at': '', 'updated_at': ''})
        assert load_lesson('del-me') is not None
        delete_lesson('del-me')
        assert load_lesson('del-me') is None
    finally:
        app.DATA_DIR = original
        shutil.rmtree(test_dir)

if __name__ == '__main__':
    test_save_and_load()
    test_list_lessons()
    test_delete_lesson()
    print('All persistence tests passed!')
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python test_prep_app/test_persistence.py`
Expected: FAIL with ImportError (functions don't exist yet)

- [ ] **Step 3: Implement persistence functions**

Add to `test_prep_app/app.py` after the `DATA_DIR` line:

```python
def save_lesson(lesson_data):
    path = os.path.join(DATA_DIR, f"{lesson_data['id']}.json")
    with open(path, 'w') as f:
        json.dump(lesson_data, f, indent=2, ensure_ascii=False)

def load_lesson(lesson_id):
    path = os.path.join(DATA_DIR, f"{lesson_id}.json")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)

def list_lessons():
    lessons = []
    if not os.path.isdir(DATA_DIR):
        return lessons
    for fn in os.listdir(DATA_DIR):
        if fn.endswith('.json'):
            with open(os.path.join(DATA_DIR, fn)) as f:
                lessons.append(json.load(f))
    lessons.sort(key=lambda x: x.get('updated_at', ''), reverse=True)
    return lessons

def delete_lesson(lesson_id):
    path = os.path.join(DATA_DIR, f"{lesson_id}.json")
    if os.path.exists(path):
        os.remove(path)
```

Also add `import json` at the top of app.py if not already there.

- [ ] **Step 4: Run test to verify it passes**

Run: `python test_prep_app/test_persistence.py`
Expected: "All persistence tests passed!"

- [ ] **Step 5: Commit**

```bash
git add test_prep_app/app.py test_prep_app/test_persistence.py
git commit -m "feat(test-prep): JSON persistence layer for lessons"
```

---

### Task 3: API Routes

**Files:**
- Modify: `test_prep_app/app.py` (add route handlers)

**Interfaces:**
- Consumes: persistence functions from Task 2
- Produces: REST API endpoints for CRUD operations

- [ ] **Step 1: Write the failing test**

Create: `test_prep_app/test_api.py`

```python
import os
import sys
import json
import tempfile
import shutil

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import app as flask_app

flask_app.app.config['TESTING'] = True
client = flask_app.app.test_client()

def test_list_lessons_empty():
    resp = client.get('/api/lessons')
    assert resp.status_code == 200
    data = resp.get_json()
    assert 'lessons' in data

def test_create_lesson():
    resp = client.post('/api/lessons', json={
        'name': 'Algorithm',
        'chapters_count': 3
    })
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['lesson']['name'] == 'Algorithm'
    assert len(data['lesson']['chapters']) == 3
    return data['lesson']['id']

def test_get_lesson():
    lid = test_create_lesson()
    resp = client.get(f'/api/lessons/{lid}')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['lesson']['name'] == 'Algorithm'

def test_update_lesson():
    lid = test_create_lesson()
    resp = client.put(f'/api/lessons/{lid}', json={
        'chapters': [
            {'number': 1, 'name': 'Ch 1', 'questions_in_book': 25, 'questions_in_exams': 2, 'recommended': 5, 'selected_count': 5, 'selected_distribution': 'center', 'question_numbers': [], 'answers': {}}
        ]
    })
    assert resp.status_code == 200
    data = resp.get_json()
    assert len(data['lesson']['chapters']) == 1

def test_delete_lesson():
    lid = test_create_lesson()
    resp = client.delete(f'/api/lessons/{lid}')
    assert resp.status_code == 200
    resp = client.get(f'/api/lessons/{lid}')
    assert resp.status_code == 404

if __name__ == '__main__':
    test_list_lessons_empty()
    test_create_lesson()
    test_get_lesson()
    test_update_lesson()
    test_delete_lesson()
    print('All API tests passed!')
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python test_prep_app/test_api.py`
Expected: FAIL with 404 on `/api/lessons`

- [ ] **Step 3: Implement API routes**

Add to `test_prep_app/app.py`:

```python
import uuid
from flask import request, jsonify

@app.route('/api/lessons')
def api_list_lessons():
    lessons = list_lessons()
    summaries = [
        {
            'id': l['id'],
            'name': l['name'],
            'chapter_count': len(l.get('chapters', [])),
            'created_at': l.get('created_at'),
            'updated_at': l.get('updated_at')
        }
        for l in lessons
    ]
    return jsonify({'lessons': summaries})

@app.route('/api/lessons', methods=['POST'])
def api_create_lesson():
    data = request.get_json()
    name = data.get('name', 'Untitled')
    chapters_count = data.get('chapters_count', 0)
    lesson_id = f"{name.lower().replace(' ', '-')}-{uuid.uuid4().hex[:6]}"
    chapters = []
    for i in range(chapters_count):
        chapters.append({
            'number': i + 1,
            'name': f'Chapter {i + 1}',
            'questions_in_book': 0,
            'questions_in_exams': 0,
            'recommended': 5,
            'selected_count': 5,
            'selected_distribution': 'center',
            'question_numbers': [],
            'answers': {}
        })
    from datetime import datetime
    now = datetime.now().isoformat()
    lesson = {
        'id': lesson_id,
        'name': name,
        'chapters': chapters,
        'created_at': now,
        'updated_at': now
    }
    save_lesson(lesson)
    return jsonify({'lesson': lesson}), 201

@app.route('/api/lessons/<lesson_id>')
def api_get_lesson(lesson_id):
    lesson = load_lesson(lesson_id)
    if not lesson:
        return jsonify({'error': 'Lesson not found'}), 404
    return jsonify({'lesson': lesson})

@app.route('/api/lessons/<lesson_id>', methods=['PUT'])
def api_update_lesson(lesson_id):
    lesson = load_lesson(lesson_id)
    if not lesson:
        return jsonify({'error': 'Lesson not found'}), 404
    data = request.get_json()
    from datetime import datetime
    for key in ('name', 'chapters'):
        if key in data:
            lesson[key] = data[key]
    lesson['updated_at'] = datetime.now().isoformat()
    save_lesson(lesson)
    return jsonify({'lesson': lesson})

@app.route('/api/lessons/<lesson_id>', methods=['DELETE'])
def api_delete_lesson(lesson_id):
    lesson = load_lesson(lesson_id)
    if not lesson:
        return jsonify({'error': 'Lesson not found'}), 404
    delete_lesson(lesson_id)
    return jsonify({'ok': True})
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python test_prep_app/test_api.py`
Expected: "All API tests passed!"

- [ ] **Step 5: Commit**

```bash
git add test_prep_app/app.py test_prep_app/test_api.py
git commit -m "feat(test-prep): REST API routes for lesson CRUD"
```

---

### Task 4: Frontend HTML Skeleton + CSS

**Files:**
- Create: `test_prep_app/templates/index.html` (replace skeleton)
- Create: `test_prep_app/static/style.css`

**Interfaces:**
- Consumes: API routes from Task 3
- Produces: complete HTML structure with all three wizard steps laid out

- [ ] **Step 1: Create the HTML skeleton**

Write to `test_prep_app/templates/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Prep</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <div class="app-container">
        <header>
            <h1>Test Prep</h1>
            <div class="step-indicator">
                <span class="step active" data-step="1">1. Lesson Setup</span>
                <span class="step" data-step="2">2. Chapter Data</span>
                <span class="step" data-step="3">3. Answer Sheet</span>
            </div>
        </header>

        <main>
            <!-- Step 1: Lesson Setup -->
            <section id="step1" class="wizard-step active">
                <h2>Lesson Setup</h2>
                <div class="form-group">
                    <label for="lessonName">Lesson Name</label>
                    <input type="text" id="lessonName" placeholder="e.g., Algorithm">
                </div>
                <div class="form-group">
                    <label for="chapterCount">Number of Chapters</label>
                    <input type="number" id="chapterCount" min="1" max="50" value="1">
                </div>
                <button id="startBtn" class="btn primary">Start</button>
            </section>

            <!-- Step 2: Chapter Data Table -->
            <section id="step2" class="wizard-step">
                <h2>Chapter Data</h2>
                <div class="table-container">
                    <table id="chapterTable">
                        <thead>
                            <tr>
                                <th>Chapter</th>
                                <th>Questions in Book</th>
                                <th>Questions in Past 10 Exams</th>
                                <th>Recommended</th>
                            </tr>
                        </thead>
                        <tbody id="chapterBody"></tbody>
                    </table>
                </div>
                <div class="step-actions">
                    <button id="backToStep1" class="btn secondary">Back</button>
                    <button id="generateSheet" class="btn primary">Generate Answer Sheet</button>
                </div>
            </section>

            <!-- Step 3: Answer Sheet -->
            <section id="step3" class="wizard-step">
                <h2>Answer Sheet</h2>
                <div class="chapter-tabs" id="chapterTabs"></div>
                <div class="distribution-options" id="distributionOptions">
                    <label><input type="radio" name="dist" value="center" checked> Center of group</label>
                    <label><input type="radio" name="dist" value="spaced_start"> Spaced from 1</label>
                    <label><input type="radio" name="dist" value="spaced_end"> Spaced to last</label>
                    <label><input type="radio" name="dist" value="normal"> Normal dist</label>
                </div>
                <div class="question-cards" id="questionCards"></div>
                <div class="oval-grid" id="ovalGrid"></div>
                <div class="step-actions">
                    <button id="backToStep2" class="btn secondary">Back</button>
                    <button id="printSheet" class="btn primary">Print Answer Sheet</button>
                </div>
            </section>
        </main>
    </div>
    <script src="/static/app.js"></script>
</body>
</html>
```

- [ ] **Step 2: Create the CSS file**

Write to `test_prep_app/static/style.css`:

```css
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f5f5f5; color: #333; }
.app-container { max-width: 900px; margin: 0 auto; padding: 20px; }
header { text-align: center; margin-bottom: 30px; }
header h1 { margin-bottom: 15px; color: #2c3e50; }
.step-indicator { display: flex; justify-content: center; gap: 10px; }
.step { padding: 8px 16px; border-radius: 20px; background: #ddd; color: #666; font-size: 14px; }
.step.active { background: #3498db; color: white; }
.wizard-step { display: none; background: white; border-radius: 8px; padding: 30px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
.wizard-step.active { display: block; }
.form-group { margin-bottom: 20px; }
.form-group label { display: block; margin-bottom: 5px; font-weight: 600; }
.form-group input { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px; font-size: 16px; }
.btn { padding: 10px 24px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
.btn.primary { background: #3498db; color: white; }
.btn.primary:hover { background: #2980b9; }
.btn.secondary { background: #ddd; color: #333; }
.btn.secondary:hover { background: #ccc; }
.table-container { overflow-x: auto; margin-bottom: 20px; }
table { width: 100%; border-collapse: collapse; }
th, td { padding: 12px; text-align: left; border-bottom: 1px solid #eee; }
th { background: #f8f9fa; font-weight: 600; }
td input[type="number"] { width: 80px; padding: 6px; border: 1px solid #ddd; border-radius: 4px; font-size: 14px; }
.step-actions { display: flex; gap: 10px; justify-content: flex-end; margin-top: 20px; }
.chapter-tabs { display: flex; gap: 5px; margin-bottom: 20px; flex-wrap: wrap; }
.chapter-tab { padding: 8px 16px; border: 1px solid #ddd; border-radius: 4px; cursor: pointer; background: white; }
.chapter-tab.active { background: #3498db; color: white; border-color: #3498db; }
.distribution-options { display: flex; gap: 15px; margin-bottom: 20px; flex-wrap: wrap; }
.distribution-options label { cursor: pointer; font-size: 14px; }
.question-cards { display: flex; gap: 8px; margin-bottom: 20px; flex-wrap: wrap; }
.question-card { width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; border: 2px solid #ddd; border-radius: 6px; cursor: pointer; font-weight: 600; }
.question-card.active { border-color: #3498db; background: #ebf5fb; }
.question-card.answered { background: #27ae60; color: white; border-color: #27ae60; }
.oval-grid { display: flex; gap: 15px; justify-content: center; margin: 30px 0; }
.oval { width: 60px; height: 40px; border: 2px solid #333; border-radius: 20px; display: flex; align-items: center; justify-content: center; cursor: pointer; font-size: 16px; font-weight: 600; user-select: none; }
.oval:hover { background: #f0f0f0; }
.oval.selected { background: #333; color: white; }
.oval-label { text-align: center; margin-top: 5px; font-size: 12px; color: #666; }
```

- [ ] **Step 3: Verify page loads with styles**

```bash
curl -s http://localhost:8082/
```

Expected: HTML with CSS link, page renders with styled wizard steps

- [ ] **Step 4: Commit**

```bash
git add test_prep_app/templates/index.html test_prep_app/static/style.css
git commit -m "feat(test-prep): HTML skeleton and CSS for wizard UI"
```

---

### Task 5: Step 1 — Lesson Setup Logic

**Files:**
- Create: `test_prep_app/static/app.js`

**Interfaces:**
- Consumes: `POST /api/lessons` from Task 3
- Produces: lesson created, wizard advances to Step 2

- [ ] **Step 1: Write app.js with Step 1 logic**

Write to `test_prep_app/static/app.js`:

```javascript
let currentLesson = null;
let currentChapterIndex = 0;

function showStep(stepNum) {
    document.querySelectorAll('.wizard-step').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.step').forEach(s => s.classList.remove('active'));
    document.getElementById(`step${stepNum}`).classList.add('active');
    document.querySelector(`.step[data-step="${stepNum}"]`).classList.add('active');
}

function calculateRecommended(book, exams) {
    const frequency = exams / 10;
    const rec = Math.round(frequency * book);
    return Math.min(Math.max(5, rec), book || 5);
}

document.getElementById('startBtn').addEventListener('click', async () => {
    const name = document.getElementById('lessonName').value.trim();
    const count = parseInt(document.getElementById('chapterCount').value);
    if (!name || !count || count < 1) {
        alert('Please enter a lesson name and valid chapter count.');
        return;
    }
    const resp = await fetch('/api/lessons', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({name, chapters_count: count})
    });
    const data = await resp.json();
    currentLesson = data.lesson;
    showStep(2);
    renderChapterTable();
});
```

- [ ] **Step 2: Add renderChapterTable function**

Append to `app.js`:

```javascript
function renderChapterTable() {
    const tbody = document.getElementById('chapterBody');
    tbody.innerHTML = '';
    currentLesson.chapters.forEach((ch, i) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${ch.name}</td>
            <td><input type="number" min="1" value="${ch.questions_in_book || ''}" data-field="questions_in_book" data-index="${i}"></td>
            <td><input type="number" min="0" max="10" value="${ch.questions_in_exams || ''}" data-field="questions_in_exams" data-index="${i}"></td>
            <td class="recommended-cell"><input type="number" min="1" value="${ch.recommended}" data-field="selected_count" data-index="${i}"></td>
        `;
        tbody.appendChild(tr);
    });

    tbody.querySelectorAll('input').forEach(input => {
        input.addEventListener('input', (e) => {
            const idx = parseInt(e.target.dataset.index);
            const field = e.target.dataset.field;
            const val = parseInt(e.target.value) || 0;
            currentLesson.chapters[idx][field] = val;

            if (field === 'questions_in_book' || field === 'questions_in_exams') {
                const ch = currentLesson.chapters[idx];
                ch.recommended = calculateRecommended(ch.questions_in_book, ch.questions_in_exams);
                ch.selected_count = ch.recommended;
                tbody.querySelector(`input[data-field="selected_count"][data-index="${idx}"]`).value = ch.recommended;
            }
        });
    });
}
```

- [ ] **Step 3: Add back/forward navigation**

Append to `app.js`:

```javascript
document.getElementById('backToStep1').addEventListener('click', () => showStep(1));
document.getElementById('generateSheet').addEventListener('click', async () => {
    const allValid = currentLesson.chapters.every(ch => ch.questions_in_book > 0);
    if (!allValid) {
        alert('Please fill in questions in book for all chapters.');
        return;
    }
    await saveLesson();
    showStep(3);
    renderAnswerSheet();
});

async function saveLesson() {
    await fetch(`/api/lessons/${currentLesson.id}`, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({chapters: currentLesson.chapters})
    });
}
```

- [ ] **Step 4: Test in browser**

Open `http://localhost:8082`, enter lesson name + chapter count, click Start. Verify table appears with correct number of rows. Verify Recommended column auto-calculates when typing in book/exam fields.

- [ ] **Step 5: Commit**

```bash
git add test_prep_app/static/app.js
git commit -m "feat(test-prep): Step 1 lesson setup and Step 2 chapter table with live recommendations"
```

---

### Task 6: Distribution Algorithms

**Files:**
- Modify: `test_prep_app/static/app.js` (add distribution functions)

**Interfaces:**
- Consumes: chapter data (questions_in_book, selected_count)
- Produces: `computeDistribution(n, k, type)` returning array of question numbers

- [ ] **Step 1: Add distribution functions**

Append to `app.js`:

```javascript
function computeDistribution(n, k, type) {
    if (k >= n) return Array.from({length: n}, (_, i) => i + 1);
    if (k <= 0) return [];

    switch (type) {
        case 'center': return distributionCenter(n, k);
        case 'spaced_start': return distributionSpacedStart(n, k);
        case 'spaced_end': return distributionSpacedEnd(n, k);
        case 'normal': return distributionNormal(n, k);
        default: return distributionCenter(n, k);
    }
}

function distributionCenter(n, k) {
    const groupSize = n / k;
    const positions = [];
    for (let i = 0; i < k; i++) {
        const pos = Math.round(i * groupSize + groupSize / 2);
        positions.push(Math.min(Math.max(1, pos), n));
    }
    return [...new Set(positions)].sort((a, b) => a - b);
}

function distributionSpacedStart(n, k) {
    const step = Math.round(n / k);
    const positions = [];
    for (let i = 0; i < k; i++) {
        positions.push(1 + i * step);
    }
    return [...new Set(positions)].filter(p => p >= 1 && p <= n).sort((a, b) => a - b);
}

function distributionSpacedEnd(n, k) {
    const step = Math.round(n / k);
    const positions = [];
    for (let i = 0; i < k; i++) {
        positions.push(n - (k - 1 - i) * step);
    }
    return [...new Set(positions)].filter(p => p >= 1 && p <= n).sort((a, b) => a - b);
}

function distributionNormal(n, k) {
    const mean = n / 2;
    const stddev = n / 6;
    const positions = [];
    for (let i = 0; i < k; i++) {
        const p = (i + 0.5) / k;
        const z = normalInverse(p);
        const pos = Math.round(mean + z * stddev);
        positions.push(Math.min(Math.max(1, pos), n));
    }
    return [...new Set(positions)].sort((a, b) => a - b);
}

function normalInverse(p) {
    // Rational approximation for the inverse normal CDF (Abramowitz & Stegun)
    if (p <= 0) return -4;
    if (p >= 1) return 4;
    if (p < 0.5) return -normalInverse(1 - p);
    const t = Math.sqrt(-2 * Math.log(1 - p));
    const c0 = 2.515517, c1 = 0.802853, c2 = 0.010328;
    const d1 = 1.432788, d2 = 0.189269, d3 = 0.001308;
    return t - (c0 + c1 * t + c2 * t * t) / (1 + d1 * t + d2 * t * t + d3 * t * t * t);
}
```

- [ ] **Step 2: Test in browser console**

Open browser console and verify:
```javascript
computeDistribution(25, 5, 'center')       // [3, 8, 13, 18, 23]
computeDistribution(25, 5, 'spaced_start') // [1, 6, 11, 16, 21]
computeDistribution(25, 5, 'spaced_end')   // [5, 10, 15, 20, 25]
computeDistribution(25, 7, 'normal')       // biased toward 8-18
```

- [ ] **Step 3: Commit**

```bash
git add test_prep_app/static/app.js
git commit -m "feat(test-prep): question distribution algorithms (center, spaced, normal)"
```

---

### Task 7: Step 3 — Answer Sheet with Oval Grid

**Files:**
- Modify: `test_prep_app/static/app.js` (add answer sheet rendering)

**Interfaces:**
- Consumes: `computeDistribution()` from Task 6, lesson chapters
- Produces: interactive answer sheet with oval selection

- [ ] **Step 1: Add answer sheet rendering**

Append to `app.js`:

```javascript
let activeChapterIdx = 0;
let activeQuestionIdx = 0;

function renderAnswerSheet() {
    renderChapterTabs();
    renderDistributionOptions();
    renderActiveChapter();
}

function renderChapterTabs() {
    const container = document.getElementById('chapterTabs');
    container.innerHTML = '';
    currentLesson.chapters.forEach((ch, i) => {
        const tab = document.createElement('div');
        tab.className = `chapter-tab ${i === activeChapterIdx ? 'active' : ''}`;
        tab.textContent = ch.name;
        tab.addEventListener('click', () => {
            activeChapterIdx = i;
            activeQuestionIdx = 0;
            renderAnswerSheet();
        });
        container.appendChild(tab);
    });
}

function renderDistributionOptions() {
    const ch = currentLesson.chapters[activeChapterIdx];
    document.querySelectorAll('input[name="dist"]').forEach(radio => {
        radio.checked = radio.value === (ch.selected_distribution || 'center');
        radio.addEventListener('change', (e) => {
            ch.selected_distribution = e.target.value;
            updateQuestionNumbers();
            renderActiveChapter();
        });
    });
}

function updateQuestionNumbers() {
    const ch = currentLesson.chapters[activeChapterIdx];
    ch.question_numbers = computeDistribution(
        ch.questions_in_book,
        ch.selected_count,
        ch.selected_distribution
    );
}

function renderActiveChapter() {
    const ch = currentLesson.chapters[activeChapterIdx];
    if (!ch.question_numbers || ch.question_numbers.length === 0) {
        updateQuestionNumbers();
    }

    const cardsContainer = document.getElementById('questionCards');
    cardsContainer.innerHTML = '';
    ch.question_numbers.forEach((qNum, i) => {
        const card = document.createElement('div');
        card.className = `question-card ${i === activeQuestionIdx ? 'active' : ''} ${ch.answers[qNum] ? 'answered' : ''}`;
        card.textContent = qNum;
        card.addEventListener('click', () => {
            activeQuestionIdx = i;
            renderActiveChapter();
        });
        cardsContainer.appendChild(card);
    });

    const ovalGrid = document.getElementById('ovalGrid');
    const currentQ = ch.question_numbers[activeQuestionIdx];
    const currentAnswer = ch.answers[currentQ] || null;
    ovalGrid.innerHTML = '';

    for (let choice = 1; choice <= 4; choice++) {
        const wrapper = document.createElement('div');
        wrapper.style.textAlign = 'center';
        const oval = document.createElement('div');
        oval.className = `oval ${currentAnswer === choice ? 'selected' : ''}`;
        oval.textContent = choice;
        oval.addEventListener('click', () => {
            if (ch.answers[currentQ] === choice) {
                delete ch.answers[currentQ];
            } else {
                ch.answers[currentQ] = choice;
            }
            saveLesson();
            renderActiveChapter();
        });
        const label = document.createElement('div');
        label.className = 'oval-label';
        label.textContent = choice;
        wrapper.appendChild(oval);
        wrapper.appendChild(label);
        ovalGrid.appendChild(wrapper);
    }
}
```

- [ ] **Step 2: Add navigation for prev/next question**

Append to `app.js`:

```javascript
document.getElementById('backToStep2').addEventListener('click', async () => {
    await saveLesson();
    showStep(2);
});

document.getElementById('printSheet').addEventListener('click', () => {
    window.print();
});

// Keyboard navigation
document.addEventListener('keydown', (e) => {
    if (document.getElementById('step3').classList.contains('active')) {
        const ch = currentLesson.chapters[activeChapterIdx];
        if (e.key === 'ArrowRight' && activeQuestionIdx < ch.question_numbers.length - 1) {
            activeQuestionIdx++;
            renderActiveChapter();
        } else if (e.key === 'ArrowLeft' && activeQuestionIdx > 0) {
            activeQuestionIdx--;
            renderActiveChapter();
        } else if (e.key >= '1' && e.key <= '4') {
            const choice = parseInt(e.key);
            const q = ch.question_numbers[activeQuestionIdx];
            if (ch.answers[q] === choice) {
                delete ch.answers[q];
            } else {
                ch.answers[q] = choice;
            }
            saveLesson();
            renderActiveChapter();
        }
    }
});
```

- [ ] **Step 3: Test in browser**

Complete full flow: create lesson → enter chapter data → generate answer sheet. Verify:
- Chapter tabs switch between chapters
- Distribution radio buttons change question numbers
- Clicking ovals selects/deselects answers
- Question cards show answered state (green)
- Arrow keys navigate, number keys select answers

- [ ] **Step 4: Commit**

```bash
git add test_prep_app/static/app.js
git commit -m "feat(test-prep): interactive answer sheet with oval selection and keyboard nav"
```

---

### Task 8: Print Styling

**Files:**
- Modify: `test_prep_app/static/style.css` (add print styles)

**Interfaces:**
- Consumes: answer sheet HTML from Task 7
- Produces: clean printable layout

- [ ] **Step 1: Add print CSS**

Append to `test_prep_app/static/style.css`:

```css
@media print {
    body { background: white; }
    header, .step-indicator, .chapter-tabs, .distribution-options,
    .step-actions, .oval-label { display: none !important; }
    .wizard-step { display: block !important; box-shadow: none; padding: 0; }
    .question-cards { justify-content: center; }
    .question-card { border-color: black; }
    .oval-grid { margin: 20px 0; }
    .oval { border-color: black; }
    .oval.selected { background: black; color: white; print-color-adjust: exact; -webkit-print-color-adjust: exact; }
    .print-header { display: block !important; text-align: center; margin-bottom: 20px; }
    .print-header h2 { font-size: 18px; }
    .print-header p { font-size: 14px; color: #666; }
}
```

- [ ] **Step 2: Add print header div to HTML**

Add inside `<section id="step3">` in `index.html`, right after the `<h2>Answer Sheet</h2>`:

```html
<div class="print-header" style="display:none;">
    <h2 id="printLessonName"></h2>
    <p id="printChapterName"></p>
</div>
```

- [ ] **Step 3: Update print button handler**

Replace the `printSheet` click handler in `app.js`:

```javascript
document.getElementById('printSheet').addEventListener('click', () => {
    const ch = currentLesson.chapters[activeChapterIdx];
    document.getElementById('printLessonName').textContent = currentLesson.name;
    document.getElementById('printChapterName').textContent = ch.name;
    document.querySelector('.print-header').style.display = 'block';
    window.print();
    document.querySelector('.print-header').style.display = 'none';
});
```

- [ ] **Step 4: Test print preview**

Open browser print preview (Ctrl+P). Verify:
- Only answer sheet content visible
- Lesson name and chapter shown at top
- Question numbers with ovals
- No navigation UI visible

- [ ] **Step 5: Commit**

```bash
git add test_prep_app/static/style.css test_prep_app/templates/index.html test_prep_app/static/app.js
git commit -m "feat(test-prep): print styling for answer sheet"
```

---

### Task 9: Lesson Listing & Resume

**Files:**
- Modify: `test_prep_app/static/app.js` (add lesson listing)
- Modify: `test_prep_app/templates/index.html` (add lesson list section)

**Interfaces:**
- Consumes: `GET /api/lessons` from Task 3
- Produces: lesson listing on page load, ability to resume a saved lesson

- [ ] **Step 1: Add lesson list to HTML**

Add before `<section id="step1">` in `index.html`:

```html
<section id="lessonList" class="wizard-step active">
    <h2>Your Lessons</h2>
    <div id="lessonsContainer"></div>
    <button id="newLessonBtn" class="btn primary" style="margin-top: 15px;">New Lesson</button>
</section>
```

- [ ] **Step 2: Add lesson listing logic**

Add to `app.js`:

```javascript
async function loadLessons() {
    const resp = await fetch('/api/lessons');
    const data = await resp.json();
    const container = document.getElementById('lessonsContainer');
    container.innerHTML = '';
    if (data.lessons.length === 0) {
        container.innerHTML = '<p style="color:#666;">No saved lessons yet.</p>';
        return;
    }
    data.lessons.forEach(l => {
        const div = document.createElement('div');
        div.className = 'lesson-item';
        div.style.cssText = 'padding:12px; border:1px solid #ddd; border-radius:6px; margin-bottom:8px; cursor:pointer; display:flex; justify-content:space-between; align-items:center;';
        div.innerHTML = `
            <div>
                <strong>${l.name}</strong>
                <span style="color:#666; margin-left:10px;">${l.chapter_count} chapters</span>
            </div>
            <button class="btn secondary delete-lesson" data-id="${l.id}" style="padding:4px 12px; font-size:12px;">Delete</button>
        `;
        div.addEventListener('click', async (e) => {
            if (e.target.classList.contains('delete-lesson')) {
                e.stopPropagation();
                if (confirm('Delete this lesson?')) {
                    await fetch(`/api/lessons/${l.id}`, {method: 'DELETE'});
                    loadLessons();
                }
                return;
            }
            const resp = await fetch(`/api/lessons/${l.id}`);
            const data = await resp.json();
            currentLesson = data.lesson;
            document.getElementById('lessonList').classList.remove('active');
            showStep(2);
            renderChapterTable();
        });
        container.appendChild(div);
    });
}

document.getElementById('newLessonBtn').addEventListener('click', () => {
    document.getElementById('lessonList').classList.remove('active');
    showStep(1);
});

// Override showStep to handle lessonList
const originalShowStep = showStep;
showStep = function(stepNum) {
    document.querySelectorAll('.wizard-step').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.step').forEach(s => s.classList.remove('active'));
    if (stepNum === 'list') {
        document.getElementById('lessonList').classList.add('active');
        loadLessons();
        return;
    }
    document.getElementById(`step${stepNum}`).classList.add('active');
    document.querySelector(`.step[data-step="${stepNum}"]`).classList.add('active');
};
```

- [ ] **Step 3: Update back button on Step 2**

Change the `backToStep1` click handler:

```javascript
document.getElementById('backToStep1').addEventListener('click', () => {
    showStep('list');
    loadLessons();
});
```

- [ ] **Step 4: Test lesson listing**

Refresh page → see "Your Lessons" list. Create a lesson → it appears in the list. Click a lesson → resumes at Step 2. Delete a lesson → removed from list.

- [ ] **Step 5: Commit**

```bash
git add test_prep_app/static/app.js test_prep_app/templates/index.html
git commit -m "feat(test-prep): lesson listing and resume from saved state"
```

---

### Task 10: Cleanup & Final Integration

**Files:**
- Modify: `test_prep_app/app.py` (add CORS for static files, clean up)
- Modify: `test_prep_app/static/app.js` (edge cases)

**Interfaces:**
- Consumes: all previous tasks
- Produces: polished, production-ready app

- [ ] **Step 1: Add input validation**

Append to `app.py`:

```python
@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Internal server error'}), 500
```

- [ ] **Step 2: Add edge case handling to app.js**

Add at the top of app.js:

```javascript
// Ensure question_numbers are recomputed when loading a saved lesson
if (currentLesson) {
    currentLesson.chapters.forEach(ch => {
        if (!ch.question_numbers || ch.question_numbers.length === 0) {
            ch.question_numbers = computeDistribution(ch.questions_in_book, ch.selected_count, ch.selected_distribution);
        }
    });
}
```

- [ ] **Step 3: Verify full flow end-to-end**

1. Open `http://localhost:8082`
2. Create new lesson "Algorithm" with 4 chapters
3. Enter: Ch1: 25 book / 2 exams, Ch2: 30 book / 5 exams, Ch3: 20 book / 0 exams, Ch4: 15 book / 8 exams
4. Verify recommendations: Ch1: 5, Ch2: 15, Ch3: 5, Ch4: 12
5. Generate answer sheet
6. Test all 4 distribution modes
7. Select answers for several questions
8. Print preview
9. Go back, verify answers are preserved
10. Reload page, verify lesson appears in list, click to resume

- [ ] **Step 4: Commit**

```bash
git add test_prep_app/
git commit -m "feat(test-prep): final integration, validation, and edge case handling"
```
