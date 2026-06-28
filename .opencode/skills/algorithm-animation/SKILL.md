---
name: algorithm-animation
description: Create interactive, step-by-step algorithm animation HTML files. Use when the user asks to 'visualize an algorithm', 'animate an algorithm', 'show algorithm steps', 'create algorithm demo', 'interactive algorithm', 'DP visualization', 'graph algorithm animation', 'sorting visualization', or wants a self-contained HTML file that demonstrates how any algorithm works with playback controls and explanations.
version: "1.0.0"
tags:
  - algorithm
  - animation
  - visualization
  - dynamic-programming
  - interactive
  - html
allowed-tools: Bash, Read, Write, Glob, Grep
---

# Algorithm Animation Generator

Create self-contained, single-file HTML animations that demonstrate algorithms step-by-step with a dark-theme, two-column layout, sidebar explanations, and playback controls.

## When to Use

- User asks to visualize/animate/show how an algorithm works
- User wants an interactive demo of any algorithm (DP, graphs, sorting, searching, strings, trees, etc.)
- User references "algorithm animation", "step-by-step", "DP table filling", "interactive demo"
- User provides algorithm pseudocode and wants it brought to life

## Output Format

- **Single `.html` file**, no external dependencies, no build step
- File name: `<algorithm-name>-animation.html`
- Works by opening directly in any browser

---

## Layout Structure

Every animation uses this exact two-column layout:

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[ALGORITHM-NAME] Animation</title>
  <style>/* all CSS here */</style>
</head>
<body>

  <h1>[ALGORITHM-NAME]</h1>
  <p class="subtitle">[Category] — [Full Name]</p>

  <div class="layout">
    <div class="main-panel">
      <!-- 1. Algorithm-specific visual display -->
      <!-- 2. Controls -->
      <!-- 3. Info panel -->
      <!-- 4. Step counter -->
      <!-- 5. DP/data tables -->
      <!-- 6. Optional extras (accumulator, canvas, etc.) -->
      <!-- 7. Result section (hidden until done) -->
    </div>

    <div class="sidebar" id="sidebar">
      <h2>📖 Step-by-Step Explanation</h2>
      <div class="step-phase" id="sidebarPhase">Algorithm idle — press Play or Step to begin.</div>
      <div id="explainArea">
        <!-- Initial problem setup explanation -->
      </div>
    </div>
  </div>

  <script>/* all JavaScript here */</script>
</body>
</html>
```

### Document Flow (main-panel, in order)

1. **Algorithm-specific display** — visual element at the top (varies by category, see below)
2. **Controls** — Play, Pause, Step, Reset, Speed slider (identical in all files)
3. **Info panel** — Algorithm name, parameters, current phase, current computation
4. **Step counter** — `Step X / Y`
5. **Table section(s)** — One or more DP/data tables with titles
6. **Optional extras** — LCS accumulator, BST canvas tree, etc.
7. **Result section** — Hidden until animation completes

---

## Color Palette

### Semantic Meanings

| Color | Meaning |
|-------|---------|
| `#00ff88` (green) | Success, completion, filled/done states, final results |
| `#ff6600` (orange) | Active/current focus, being computed, sidebar headings |
| `#00ccff` (cyan) | Informational, formula text, table headers, structural labels |
| `#ffcc00` (yellow) | Explanation headings, split/root decisions, info panel values |
| `#ffff00` (bright yellow) | Temporary "in-progress" computation state |
| `#ff9944` (warm orange) | Data parameter highlights (`.dim` class) |
| `#ff66ff` (magenta) | BST dummy keys, trying states; LCS trace cells |
| `#aaa` (gray) | Default table cell text, notes |
| `#888` (dark gray) | Labels, counters, inactive UI |
| `#555` (darker gray) | Disabled elements, arrows, indices |

### Exact Hex Values

**Backgrounds:**
| Hex | Usage |
|-----|-------|
| `#0a0a1a` | `body` background |
| `#0d0d20` | `.sidebar` background |
| `#111` | `.info-panel`, `.matrix-box`, `.char-box`, `.lcs-accumulator`, scrollbar-track |
| `#111128` | `.explain-section` background (inactive) |
| `#1a1a2e` | `th` background, `.btn` background |
| `#0d0d1a` | `td` default background |
| `#0a0a18` | `.formula-line` background |
| `#0a0a12` | Disabled/empty cell background |
| `#0a1a12` | `td.filled` background, `.result-section` background |

**State highlights:**
| Hex | Usage |
|-----|-------|
| `#1a1020` | `.explain-section.active` background |
| `#1a0a00` | `td.current` background, `.active-x` background |
| `#001a0a` | `.match` background |
| `#002a1a` | `.btn.primary` background, `td.trace-match` background |
| `#1a1a00` | `td.computing` background |
| `#1a0030` | `td.trace-cell` background |

**Text:**
| Hex | Usage |
|-----|-------|
| `#e0e0e0` | `body` text, `.btn` text |
| `#00ff88` | `h1`, `.result-line`, `td.filled` text, `.btn.primary` text |
| `#888` | `.subtitle`, `.info-panel .label`, `.speed-control` |
| `#ff6600` | `.sidebar h2`, `td.current` text, `.step-counter .count` |
| `#00ccff` | `.step-phase`, `.formula-line` text, `th` text, `.table-title` |
| `#ffcc00` | `.explain-section h3`, `.info-panel .value`, `.split-info` |
| `#ccc` | `.explain-section p` text |
| `#aaa` | `td` default text, `.note` text |
| `#555` | `.char-index`, `td.diagonal` text, disabled text |
| `#ff9944` | `.dim` text |
| `#ffff00` | `td.computing` text |
| `#fff` | Result display text |

**Borders:**
| Hex | Usage |
|-----|-------|
| `#333` | `th/td` borders, `.info-panel` border |
| `#444` | `.btn`/`.matrix-box`/`.char-box` border, `.explain-section` inactive border |
| `#2a2a44` | `.sidebar` border |
| `#00ff88` | `.result-section` border, `.btn.primary` border, `td.filled` border-color |

**Shadows/Glows (appended to box-shadow):**
| Hex | Usage |
|-----|-------|
| `#00ff8855` | `h1` text-shadow, `td.filled` border-color |
| `#ff660044` | `.current` box-shadow |
| `#00ff8844` | `.match` box-shadow |
| `#00ff8833` | `.btn:hover` box-shadow |
| `#ffff0033` | `td.computing` box-shadow |

---

## CSS Classes Reference

### Global

```css
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  background: #0a0a1a;
  color: #e0e0e0;
  font-family: 'Courier New', monospace;
  min-height: 100vh;
}
```

### Title

```css
h1 {
  text-align: center;
  font-size: 1.6em;
  color: #00ff88;
  margin: 20px 0 5px;
  text-shadow: 0 0 20px #00ff8855;
  letter-spacing: 2px;
}
.subtitle {
  text-align: center;
  color: #888;
  font-size: 0.9em;
  margin-bottom: 20px;
}
```

### Layout

```css
.layout {
  display: flex;
  gap: 0;
  max-width: 1600px;
  margin: 0 auto;
  padding: 0 15px 30px;
}
.main-panel {
  flex: 1;
  min-width: 0;
  padding-right: 15px;
}
.sidebar {
  width: 420px;
  min-width: 420px;
  max-height: calc(100vh - 100px);
  overflow-y: auto;
  position: sticky;
  top: 10px;
  background: #0d0d20;
  border: 1px solid #2a2a44;
  border-radius: 12px;
  padding: 20px;
}
.sidebar::-webkit-scrollbar { width: 5px; }
.sidebar::-webkit-scrollbar-track { background: #111; }
.sidebar::-webkit-scrollbar-thumb { background: #444; border-radius: 3px; }
@media (max-width: 1100px) {
  .layout { flex-direction: column; }
  .sidebar {
    width: 100%;
    min-width: unset;
    max-height: none;
    position: static;
    margin-top: 20px;
  }
}
```

### Sidebar

```css
.sidebar h2 {
  color: #ff6600;
  font-size: 1.05em;
  margin-bottom: 12px;
  padding-bottom: 8px;
  border-bottom: 1px solid #333;
}
.sidebar .step-phase {
  color: #00ccff;
  font-size: 0.85em;
  margin-bottom: 10px;
}
.explain-section {
  margin-bottom: 18px;
  padding: 12px;
  background: #111128;
  border-radius: 8px;
  border-left: 3px solid #444;
  font-size: 0.85em;
  line-height: 1.7;
}
.explain-section.active {
  border-left-color: #ff6600;
  background: #1a1020;
}
.explain-section h3 {
  color: #ffcc00;
  font-size: 0.95em;
  margin-bottom: 6px;
}
.explain-section p {
  color: #ccc;
  margin: 4px 0;
}
.explain-section .formula-line {
  color: #00ccff;
  background: #0a0a18;
  padding: 6px 10px;
  border-radius: 4px;
  margin: 6px 0;
  font-size: 0.95em;
  display: block;
  overflow-x: auto;
  white-space: nowrap;
}
.explain-section .result-line {
  color: #00ff88;
  font-weight: bold;
  margin: 6px 0;
}
.explain-section .note {
  color: #aaa;
  font-style: italic;
  font-size: 0.9em;
  margin-top: 4px;
}
.explain-section .dim { color: #ff9944; }
.explain-section .split-info { color: #ffcc00; margin-top: 4px; }
```

### Info Panel

```css
.info-panel {
  background: #111;
  border: 1px solid #333;
  border-radius: 10px;
  padding: 15px;
  margin: 15px 0;
  font-size: 0.85em;
  line-height: 1.8;
}
.info-panel .label { color: #888; }
.info-panel .value { color: #ffcc00; font-weight: bold; }
.info-panel .highlight { color: #00ff88; }
```

### Tables

```css
.table-section { margin: 20px 0; }
.table-title {
  font-size: 1em;
  color: #00ccff;
  margin-bottom: 10px;
}
.table-wrapper {
  overflow-x: auto;
  padding: 5px;
}
table {
  border-collapse: collapse;
  margin: 0 auto;
}
th, td {
  width: 72px;
  height: 38px;
  text-align: center;
  border: 1px solid #333;
  font-size: 0.78em;
  transition: all 0.3s;
}
th {
  background: #1a1a2e;
  color: #00ccff;
  font-weight: bold;
}
td {
  background: #0d0d1a;
  color: #aaa;
}
td.filled {
  background: #0a1a12;
  color: #00ff88;
  border-color: #00ff8855;
}
td.current {
  background: #1a0a00 !important;
  color: #ff6600 !important;
  border-color: #ff6600 !important;
  box-shadow: 0 0 15px #ff660044;
  transform: scale(1.05);
  font-weight: bold;
}
td.computing {
  background: #1a1a00 !important;
  color: #ffff00 !important;
  border-color: #ffff00 !important;
  box-shadow: 0 0 10px #ffff0033;
}
```

### Controls

```css
.controls {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin: 18px 0;
  flex-wrap: wrap;
}
.btn {
  padding: 8px 18px;
  border: 2px solid #444;
  background: #1a1a2e;
  color: #e0e0e0;
  border-radius: 8px;
  cursor: pointer;
  font-family: 'Courier New', monospace;
  font-size: 0.85em;
  transition: all 0.3s;
}
.btn:hover {
  border-color: #00ff88;
  color: #00ff88;
  box-shadow: 0 0 15px #00ff8833;
}
.btn:active { transform: scale(0.95); }
.btn.primary {
  background: #002a1a;
  border-color: #00ff88;
  color: #00ff88;
}
.speed-control {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #888;
  font-size: 0.85em;
}
.speed-control input {
  width: 80px;
  accent-color: #00ff88;
}
```

### Step Counter

```css
.step-counter {
  text-align: center;
  color: #888;
  font-size: 0.85em;
  margin: 8px 0;
}
.step-counter .count { color: #ff6600; font-weight: bold; }
```

### Result

```css
.result-section {
  background: #0a1a12;
  border: 2px solid #00ff88;
  border-radius: 12px;
  padding: 20px;
  margin: 25px 0;
  text-align: center;
}
.result-section h2 {
  color: #00ff88;
  font-size: 1.2em;
  margin-bottom: 12px;
}
```

---

## HTML Controls Block (exact, reuse in every file)

```html
<div class="controls">
  <button class="btn primary" onclick="startAnimation()">▶ Play</button>
  <button class="btn" onclick="pauseAnimation()">⏸ Pause</button>
  <button class="btn" onclick="stepForward()">⏭ Step</button>
  <button class="btn" onclick="resetAnimation()">↺ Reset</button>
  <div class="speed-control">
    <label>Speed:</label>
    <input type="range" id="speedSlider" min="1" max="10" value="5">
    <span id="speedLabel">5x</span>
  </div>
</div>
```

---

## JavaScript Architecture

### Global State

```javascript
let steps = [];
let currentStep = 0;
let animating = false;
let animTimer = null;
// + algorithm-specific data arrays (m, s, c, b, e, w, root, etc.)
```

### Core Functions (required in every file)

| Function | Purpose |
|----------|---------|
| `precomputeAll()` | Compute all answers upfront, return result arrays |
| `buildSteps()` | Clear `steps=[]`, iterate algorithm, push step objects |
| `buildXxxExplanation(...)` | Return HTML string for one step's sidebar explanation |
| `buildFinishedExplanation()` | Return HTML string for completion sidebar |
| `initTables()` | Build table DOM HTML and insert into document |
| `applyStep(step)` | Apply one step to DOM: update cells, highlights, info panel, sidebar |
| `clearHighlights()` | Remove all highlight classes from all elements |
| `processStep()` | Guard check, update stepNum, call applyStep, increment |
| `startAnimation()` | Set `animating=true`, start `setInterval` with `getSpeed()` |
| `getSpeed()` | Convert slider to delay: `1200 - parseInt(value) * 100` |
| `pauseAnimation()` | Set `animating=false`, `clearInterval` |
| `stepForward()` | Call `pauseAnimation()` then `processStep()` |
| `resetAnimation()` | Full reset: pause, reset counters, re-init tables, rebuild steps |
| `finishAnimation()` | Show results, update sidebar with completion HTML |

### Animation Loop (exact, reuse)

```javascript
function startAnimation() {
  if (currentStep >= steps.length) return;
  animating = true;
  animTimer = setInterval(() => {
    if (!animating || currentStep >= steps.length) {
      clearInterval(animTimer);
      if (currentStep >= steps.length) finishAnimation();
      return;
    }
    processStep();
  }, getSpeed());
}

function getSpeed() {
  return 1200 - parseInt(document.getElementById('speedSlider').value) * 100;
}

function pauseAnimation() {
  animating = false;
  clearInterval(animTimer);
}

function stepForward() {
  pauseAnimation();
  processStep();
}
```

### Speed Slider Listener (exact, reuse)

```javascript
document.getElementById('speedSlider').addEventListener('input', function() {
  document.getElementById('speedLabel').textContent = this.value + 'x';
  if (animating) {
    clearInterval(animTimer);
    animTimer = setInterval(() => {
      if (!animating || currentStep >= steps.length) {
        clearInterval(animTimer);
        if (currentStep >= steps.length) finishAnimation();
        return;
      }
      processStep();
    }, getSpeed());
  }
});
```

### processStep (exact, reuse)

```javascript
function processStep() {
  if (currentStep >= steps.length) { finishAnimation(); return; }
  document.getElementById('stepNum').textContent = currentStep + 1;
  applyStep(steps[currentStep]);
  currentStep++;
}
```

### Sidebar Update Pattern (inside applyStep)

```javascript
document.getElementById('sidebarPhase').textContent =
  `Step ${currentStep + 1} / ${steps.length} — [phase description]`;
document.getElementById('explainArea').innerHTML = step.explanation;
document.getElementById('sidebar').scrollTop = 0;
```

### Initialization (bottom of script)

```javascript
buildSteps();
initTables();
document.getElementById('totalSteps').textContent = steps.length;
```

---

## Step Object Protocol

Every step pushed into `steps[]` must have these fields:

```javascript
{
  type: string,          // Step type name (e.g., 'diagonal', 'compute', 'set', 'trace_match')
  i: number,             // Primary index (row)
  j: number,             // Secondary index (column)
  explanation: string,   // HTML string for sidebar — built by explanation builder function
  // + algorithm-specific data fields
}
```

### Step Type Naming Convention

Use descriptive names that indicate what the step does:
- `diagonal`, `base` — base case initialization
- `compute` — computing a cell value (trying candidates)
- `set` — finalizing a cell with the best value
- `trace_start`, `trace_match`, `trace_up`, `trace_left`, `trace_done` — reconstruction/traceback
- `try_root`, `try_candidate` — trying alternatives before selecting best

---

## Algorithm Category Guides

### DP Table Filling (Matrix Chain, Knapsack, Edit Distance, etc.)

**Visual display:** Algorithm-specific element at top (matrix chain boxes, input arrays, etc.)

**Table pattern:** Fill by increasing chain/subproblem length:
1. Diagonal/base case steps first (`m[i,i] = 0`)
2. For each chain length `l = 2..n`:
   - For each starting position `i`:
     - Compute `j = i + l - 1`
     - Try each split/candidate `k` → push `compute` step
     - Select best → push `set` step

**Step types:** `diagonal` → `compute` (multiple per cell) → `set` (one per cell)

**Table cell states:**
- `td.filled` (green) — base case or finalized
- `td.current` (orange, scaled) — just set, about to move on
- `td.computing` (yellow) — being evaluated

### Graph Algorithms (BFS, DFS, Dijkstra, etc.)

**Visual display:** SVG or canvas-based graph with nodes and edges

**Table pattern:** Track distances/parents as algorithm progresses

**Step types:** `init`, `visit`, `relax`, `extract_min`, `done`

**Extra elements:** Node highlight classes for `current`, `visited`, `frontier`, `path`

### Sorting Algorithms (QuickSort, MergeSort, etc.)

**Visual display:** Bar chart or array boxes with value labels

**Table pattern:** Not always needed; the visual display IS the main content

**Step types:** `compare`, `swap`, `partition`, `merge`, `sorted`

**Extra elements:** Bar height proportional to value, color for comparing/swapping/sorted

### String Algorithms (KMP, Rabin-Karp, Trie, etc.)

**Visual display:** Character boxes with pointer indices (like LCS string display)

**Pattern:**
```css
.char-box {
  width: 40px; height: 40px;
  display: flex; align-items: center; justify-content: center;
  border: 2px solid #444; border-radius: 6px;
  font-size: 1em; font-weight: bold;
  transition: all 0.4s; background: #111;
}
.char-box.active { border-color: #ff6600; /* orange highlight */ }
.char-box.match { border-color: #00ff88; /* green match */ }
```

**Step types:** `init`, `compare`, `shift`, `match`, `mismatch`, `found`

### Tree Algorithms (BST, AVL, Trie, etc.)

**Visual display:** HTML5 canvas for tree drawing (600×350px)

**Canvas drawing pattern:**
```javascript
function drawNode(x, y, text, color) {
  ctx.beginPath();
  ctx.arc(x, y, 18, 0, Math.PI*2);
  ctx.fillStyle = '#111';
  ctx.fill();
  ctx.strokeStyle = color;
  ctx.lineWidth = 2;
  ctx.stroke();
  ctx.fillStyle = color;
  ctx.font = 'bold 13px Courier New';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(text, x, y);
}
function drawEdge(x1, y1, x2, y2) {
  ctx.beginPath();
  ctx.moveTo(x1, y1+18);
  ctx.lineTo(x2, y2-18);
  ctx.strokeStyle = '#555';
  ctx.lineWidth = 1.5;
  ctx.stroke();
}
```

**Node colors:** `#00ccff` for key nodes, `#ff66ff` for dummy/leaf nodes

### Reconstruction / Traceback (LCS, Edit Distance, etc.)

After the main DP fill, add traceback steps:

**Step types:** `trace_start` → `trace_match`/`trace_up`/`trace_left` (repeated) → `trace_done`

**Visual additions:**
- LCS accumulator bar with pop-in animation
- Trace cell highlight classes (purple/green glow)
- Characters highlighted in string display during traceback

**Accumulator CSS pattern:**
```css
.lcs-accumulator {
  display: flex; justify-content: center; align-items: center;
  gap: 10px; margin: 15px 0; padding: 15px;
  background: #111; border: 1px solid #333; border-radius: 10px;
}
.lcs-acc-char {
  width: 36px; height: 36px;
  display: flex; align-items: center; justify-content: center;
  border: 2px solid #00ff88; border-radius: 6px;
  font-size: 1em; font-weight: bold; color: #00ff88;
  background: #0a1a12;
  animation: lcsPop 0.3s ease;
}
@keyframes lcsPop {
  0% { transform: scale(0); opacity: 0; }
  60% { transform: scale(1.2); }
  100% { transform: scale(1); opacity: 1; }
}
```

**Trace cell CSS:**
```css
td.trace-cell {
  background: #1a0030 !important; color: #ff99ff !important;
  border-color: #ff66ff !important;
  box-shadow: 0 0 12px #ff66ff55;
  transform: scale(1.08); font-weight: bold;
}
td.trace-match {
  background: #002a1a !important; color: #00ff88 !important;
  border-color: #00ff88 !important;
  box-shadow: 0 0 14px #00ff8855;
  transform: scale(1.1); font-weight: bold;
}
```

---

## Sidebar Explanation Writing Guide

### Initial "Problem Setup" (shown before animation starts)

```html
<div class="explain-section active">
  <h3>Problem Setup</h3>
  <p>[1-2 sentence problem description with <b>bold</b> key terms]</p>
  <p>[Input data with <span class="dim">highlighted</span> parameters]</p>
  <h3 style="margin-top:10px;">Key Formula</h3>
  <span class="formula-line">[recurrence relation or key equation]</span>
  <p class="note">[optional base case note]</p>
  <p class="note">Press Play or Step to begin.</p>
</div>
```

### Per-Step Explanation

Each step's `explanation` property must return an HTML string:

```html
<div class="explain-section active">
  <h3>[Step Title — e.g., "Computing m[2,5] with k=3"]</h3>
  <p>[What is being computed and why]</p>
  <p style="margin-left:8px;">• [bullet point with <span class="dim">highlighted</span> values]</p>
  <span class="formula-line">[formula with actual numbers substituted]</span>
  <p>Store <span class="split-info">s[i,j] = k</span> for reconstruction.</p>
  <p class="note">[optional insight about why this step matters]</p>
</div>
```

### Completion Explanation

```html
<div class="explain-section active" style="border-left-color:#00ff88;">
  <h3>✅ Algorithm Complete!</h3>
  <p>The full DP table is filled. The answer is in <span class="result-line" style="display:inline;">[answer]</span>.</p>
  <h3 style="margin-top:10px;">[Reconstruction / Result section]</h3>
  <p>[How to read the result]</p>
  <h3 style="margin-top:10px;">Complexity</h3>
  <p><span class="dim">Time:</span> [complexity with brief justification]</p>
  <p><span class="dim">Space:</span> [complexity]</p>
</div>
```

### Explanation class usage

| Class | Use for |
|-------|---------|
| `.dim` | Data values, parameter names, algorithm terms |
| `.split-info` | Split points, root choices, decision results |
| `.formula-line` | Any formula, computation, or code-like expression |
| `.result-line` | Final answers, computed values being reported |
| `.note` | Insights, clarifications, "why this matters" |

---

## Reset Pattern (exact, reuse)

```javascript
function resetAnimation() {
  pauseAnimation();
  currentStep = 0;
  // Reset all data arrays to initial state
  document.getElementById('resultSection').style.display = 'none';
  document.getElementById('phaseDisplay').textContent = 'Ready — Press Play';
  document.getElementById('computingDisplay').textContent = '—';
  document.getElementById('stepNum').textContent = '0';
  document.getElementById('sidebarPhase').textContent = 'Algorithm idle — press Play or Step to begin.';
  document.getElementById('explainArea').innerHTML = `[Problem Setup HTML - same as initial]`;
  clearHighlights();
  buildSteps();
  initTables();
  document.getElementById('totalSteps').textContent = steps.length;
}
```

---

## Finish Pattern (exact, reuse)

```javascript
function finishAnimation() {
  animating = false;
  let results = precomputeAll();
  document.getElementById('phaseDisplay').textContent = '✓ Complete!';
  document.getElementById('computingDisplay').textContent = `[final answer]`;
  document.getElementById('resultSection').style.display = 'block';
  document.getElementById('finalCost').textContent = [answer];
  document.getElementById('resultDisplay').innerHTML = [formatted result];
  document.getElementById('sidebarPhase').textContent =
    `Step ${steps.length} / ${steps.length} — ✅ Complete`;
  document.getElementById('explainArea').innerHTML = buildFinishedExplanation();
  document.getElementById('sidebar').scrollTop = 0;
}
```

---

## Quality Checklist

Before delivering the animation file, verify:

- [ ] **All brackets balanced** — `{}`, `()`, `[]` counts match
- [ ] **Speed slider works** — changing slider during playback updates interval
- [ ] **Reset fully works** — returns to initial state, all highlights cleared
- [ ] **Step counter accurate** — shows correct current/total
- [ ] **Result section hidden until done** — `style.display = 'none'` initially
- [ ] **Sidebar scrolls to top** on each new step
- [ ] **No external dependencies** — pure HTML/CSS/JS in one file
- [ ] **Responsive** — stacks vertically below 1100px
- [ ] **Explanation text is clear** — explains what AND why, not just what
- [ ] **Algorithm is correct** — verify output matches known correct answers

---

## Existing Reference Files

These files in the workspace demonstrate the exact style and can be referenced:

- `matrix-chain-animation.html` — DP table filling with split points, parenthesization result
- `lcs-length-animation.html` — String display, direction arrows, traceback with accumulator
- `optimal-bst-animation.html` — Probability display, canvas tree drawing, weight table

Use these as ground truth for styling, structure, and behavior when creating new animations.
