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
