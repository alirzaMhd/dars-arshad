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
    if (p <= 0) return -4;
    if (p >= 1) return 4;
    if (p < 0.5) return -normalInverse(1 - p);
    const t = Math.sqrt(-2 * Math.log(1 - p));
    const c0 = 2.515517, c1 = 0.802853, c2 = 0.010328;
    const d1 = 1.432788, d2 = 0.189269, d3 = 0.001308;
    return t - (c0 + c1 * t + c2 * t * t) / (1 + d1 * t + d2 * t * t + d3 * t * t * t);
}
