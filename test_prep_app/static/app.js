let currentLesson = null;
let currentChapterIndex = 0;

// Ensure question_numbers are recomputed when loading a saved lesson
if (currentLesson) {
    currentLesson.chapters.forEach(ch => {
        if (!ch.question_numbers || ch.question_numbers.length === 0) {
            ch.question_numbers = computeDistribution(ch.questions_in_book, ch.selected_count, ch.selected_distribution);
        }
    });
}

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

loadLessons();

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

document.getElementById('backToStep1').addEventListener('click', () => {
    showStep('list');
    loadLessons();
});
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

document.getElementById('backToStep2').addEventListener('click', async () => {
    await saveLesson();
    showStep(2);
});

document.getElementById('printSheet').addEventListener('click', () => {
    const ch = currentLesson.chapters[activeChapterIdx];
    document.getElementById('printLessonName').textContent = currentLesson.name;
    document.getElementById('printChapterName').textContent = ch.name;
    document.querySelector('.print-header').style.display = 'block';
    window.print();
    document.querySelector('.print-header').style.display = 'none';
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
