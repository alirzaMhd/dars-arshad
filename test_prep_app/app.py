import os
import json
from flask import Flask, render_template
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

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=False, threaded=True)
