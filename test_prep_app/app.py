import os
import json
import uuid
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data', 'lessons')
os.makedirs(DATA_DIR, exist_ok=True)

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

def sanitize_lesson_id(name):
    import re
    sanitized = re.sub(r'[^a-zA-Z0-9\s-]', '', name)
    sanitized = re.sub(r'\s+', '-', sanitized.strip())
    return sanitized.lower()

@app.route('/api/lessons', methods=['POST'])
def api_create_lesson():
    data = request.get_json()
    name = data.get('name', 'Untitled')
    chapters_count = data.get('chapters_count', 0)
    lesson_id = f"{sanitize_lesson_id(name)}-{uuid.uuid4().hex[:6]}"
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
        'total_intended': 20,
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
    for key in ('name', 'chapters', 'total_intended'):
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

@app.route('/api/lessons/<lesson_id>/compute', methods=['POST'])
def api_compute_questions(lesson_id):
    lesson = load_lesson(lesson_id)
    if not lesson:
        return jsonify({'error': 'Lesson not found'}), 404
    data = request.get_json()
    chapter_index = data.get('chapter_index')
    distribution = data.get('distribution', 'center')
    if chapter_index is None or not isinstance(chapter_index, int):
        return jsonify({'error': 'chapter_index required (int)'}), 400
    chapters = lesson.get('chapters', [])
    if chapter_index < 0 or chapter_index >= len(chapters):
        return jsonify({'error': 'Invalid chapter_index'}), 400
    ch = chapters[chapter_index]
    n = ch.get('questions_in_book', 0)
    k = ch.get('selected_count', 5)

    def compute(n, k, dist):
        if k >= n:
            return list(range(1, n + 1))
        if k <= 0:
            return []
        if dist == 'center':
            groupSize = n / k
            positions = []
            for i in range(k):
                pos = round(i * groupSize + groupSize / 2)
                positions.append(min(max(1, pos), n))
            return sorted(set(positions))
        elif dist == 'spaced_start':
            step = round(n / k)
            positions = [1 + i * step for i in range(k)]
            return sorted(set(p for p in positions if 1 <= p <= n))
        elif dist == 'spaced_end':
            step = round(n / k)
            positions = [n - (k - 1 - i) * step for i in range(k)]
            return sorted(set(p for p in positions if 1 <= p <= n))
        else:
            import math
            mean = n / 2
            stddev = n / 6
            positions = []
            for i in range(k):
                p_val = (i + 0.5) / k
                if p_val <= 0:
                    z = -4
                elif p_val >= 1:
                    z = 4
                else:
                    if p_val < 0.5:
                        p_comp = 1 - p_val
                        t = math.sqrt(-2 * math.log(p_comp))
                        z_raw = t - (2.515517 + 0.802853 * t + 0.010328 * t * t) / (1 + 1.432788 * t + 0.189269 * t * t + 0.001308 * t * t * t)
                        z = -z_raw
                    else:
                        t = math.sqrt(-2 * math.log(1 - p_val))
                        z = t - (2.515517 + 0.802853 * t + 0.010328 * t * t) / (1 + 1.432788 * t + 0.189269 * t * t + 0.001308 * t * t * t)
                pos = round(mean + z * stddev)
                positions.append(min(max(1, pos), n))
            return sorted(set(positions))

    question_numbers = compute(n, k, distribution)
    ch['question_numbers'] = question_numbers
    ch['selected_distribution'] = distribution
    lesson['updated_at'] = __import__('datetime').datetime.now().isoformat()
    save_lesson(lesson)
    return jsonify({'question_numbers': question_numbers})

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=False, threaded=True)
