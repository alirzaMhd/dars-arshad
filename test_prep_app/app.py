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
