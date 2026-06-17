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
