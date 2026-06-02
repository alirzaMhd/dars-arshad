import os, uuid, json, re, threading, time, importlib
import numpy as np
import soundfile as sf
import pymupdf
import torch
from flask import Flask, request, jsonify, send_file, render_template, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'static', 'uploads')
app.config['AUDIO_FOLDER'] = os.path.join(BASE_DIR, 'static', 'audio')
app.config['SESSIONS_FOLDER'] = os.path.join(BASE_DIR, 'static', 'sessions')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['AUDIO_FOLDER'], exist_ok=True)
os.makedirs(app.config['SESSIONS_FOLDER'], exist_ok=True)

_pipeline = None
_pipeline_lock = threading.Lock()

def get_pipeline():
    global _pipeline
    if _pipeline is None:
        with _pipeline_lock:
            if _pipeline is None:
                from kokoro import KPipeline
                _pipeline = KPipeline(lang_code='a')
    return _pipeline

def get_session_dir(session_id):
    return os.path.join(app.config['SESSIONS_FOLDER'], session_id)

def load_session(session_id):
    path = os.path.join(get_session_dir(session_id), 'session.json')
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return None

def save_session(session_data):
    d = get_session_dir(session_data['session_id'])
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, 'session.json'), 'w') as f:
        json.dump(session_data, f)

def extract_page_text(pdf_path, page_num):
    doc = pymupdf.open(pdf_path)
    if page_num < 0 or page_num >= len(doc):
        return []
    page = doc[page_num]
    blocks = page.get_text("blocks")
    paragraphs = []
    for block in blocks:
        text = block[4].strip()
        if not text:
            continue
        for p in re.split(r'\n\s*\n', text):
            p = p.strip()
            if p:
                paragraphs.append(p)
    doc.close()
    return paragraphs

def find_segment_rects(page, text):
    """Locate a text snippet on the page and return rects in PDF point coords."""
    if not text or not text.strip():
        return []
    queries = [text.strip(), re.sub(r'\s+', ' ', text).strip()]
    for q in queries:
        try:
            found = page.search_for(q)
        except Exception:
            found = []
        if found:
            return [[float(r.x0), float(r.y0), float(r.x1), float(r.y1)] for r in found]
    for length in (120, 80, 50, 30):
        snippet = re.sub(r'\s+', ' ', text).strip()[:length].strip()
        if not snippet:
            continue
        try:
            found = page.search_for(snippet)
        except Exception:
            found = []
        if found:
            return [[float(r.x0), float(r.y0), float(r.x1), float(r.y1)] for r in found]
    return []

def extract_page_segments(pdf_path, page_num, max_chars=300):
    """Return segments with text + bounding boxes in PDF point coordinates."""
    doc = pymupdf.open(pdf_path)
    if page_num < 0 or page_num >= len(doc):
        doc.close()
        return []
    page = doc[page_num]
    blocks = page.get_text("blocks")
    raw_paragraphs = []
    for block in blocks:
        text = block[4].strip()
        if not text:
            continue
        for p in re.split(r'\n\s*\n', text):
            p = p.strip()
            if p:
                raw_paragraphs.append(p)
    segments_text = split_paragraphs(raw_paragraphs, max_chars)
    segments = []
    for text in segments_text:
        rects = find_segment_rects(page, text)
        segments.append({'text': text, 'rects': rects})
    doc.close()
    return segments

def split_paragraphs(paragraphs, max_chars=300):
    groups = []
    for p in paragraphs:
        if len(p) <= max_chars:
            groups.append(p)
        else:
            sentences = re.split(r'(?<=[.!?])\s+', p)
            current = ''
            for s in sentences:
                if len(current) + len(s) + 1 <= max_chars:
                    current = (current + ' ' + s).strip()
                else:
                    if current:
                        groups.append(current)
                    current = s
            if current:
                groups.append(current)
    return groups

def generate_page_audio(session_id, page_num, voice, speed):
    session = load_session(session_id)
    if not session:
        return None

    pdf_path = session['pdf_path']
    page_dir = os.path.join(get_session_dir(session_id), 'pages', str(page_num))
    audio_dir = os.path.join(page_dir, 'audio')
    os.makedirs(audio_dir, exist_ok=True)

    page_data = {'page': page_num, 'segments': [], 'total_segments': 0, 'status': 'generating'}
    status_path = os.path.join(page_dir, 'status.json')
    with open(status_path, 'w') as f:
        json.dump({'status': 'generating', 'progress': 0, 'total': 0}, f)

    paragraphs = extract_page_text(pdf_path, page_num)
    text_segments = split_paragraphs(paragraphs)

    doc = pymupdf.open(pdf_path)
    page = doc[page_num]
    segments = []
    for text in text_segments:
        rects = find_segment_rects(page, text)
        segments.append({'text': text, 'rects': rects})
    doc.close()
    page_data['total_segments'] = len(segments)

    for idx, seg in enumerate(segments):
        text = seg['text']
        audio_path = os.path.join(audio_dir, f'seg_{idx:04d}.wav')
        audio_data = []
        for result in get_pipeline()(text, voice=voice, speed=speed):
            if result.audio is not None:
                audio_data.append(result.audio)
        if audio_data:
            if hasattr(audio_data[0], 'cpu'):
                full_audio = torch.cat(audio_data).cpu().numpy()
            else:
                full_audio = np.concatenate(audio_data)
            sf.write(audio_path, full_audio, 24000)
            duration = len(full_audio) / 24000
        else:
            duration = 0

        page_data['segments'].append({
            'index': idx,
            'text': text,
            'rects': seg['rects'],
            'audio_url': f'/static/sessions/{session_id}/pages/{page_num}/audio/seg_{idx:04d}.wav',
            'duration': duration
        })

        with open(status_path, 'w') as f:
            json.dump({'status': 'generating', 'progress': idx + 1, 'total': len(segments)}, f)

    page_data['status'] = 'ready'
    page_data_path = os.path.join(page_dir, 'page.json')
    with open(page_data_path, 'w') as f:
        json.dump(page_data, f)

    with open(status_path, 'w') as f:
        json.dump({'status': 'ready', 'progress': len(segments), 'total': len(segments)}, f)

    if 'generated_pages' not in session:
        session['generated_pages'] = {}
    session['generated_pages'][str(page_num)] = 'ready'
    save_session(session)

    return page_data

def prefetch_pages(session_id, current_page, voice, speed, n_ahead=3):
    session = load_session(session_id)
    if not session:
        return
    total = session['total_pages']
    for p in range(current_page + 1, min(current_page + 1 + n_ahead, total)):
        page_dir = os.path.join(get_session_dir(session_id), 'pages', str(p))
        page_data_path = os.path.join(page_dir, 'page.json')
        if os.path.exists(page_data_path):
            continue
        print(f'[prefetch] Pre-generating page {p+1}...')
        try:
            generate_page_audio(session_id, p, voice, speed)
        except Exception as e:
            print(f'[prefetch] Error on page {p+1}: {e}')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    session_id = str(uuid.uuid4())[:8]
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], f'{session_id}.pdf')
    file.save(pdf_path)

    doc = pymupdf.open(pdf_path)
    total_pages = len(doc)
    page_sizes = []
    for i in range(total_pages):
        rect = doc[i].rect
        page_sizes.append({'width': rect.width, 'height': rect.height})
    doc.close()

    session = {
        'session_id': session_id,
        'filename': file.filename,
        'total_pages': total_pages,
        'pdf_path': pdf_path,
        'page_sizes': page_sizes,
        'generated_pages': {},
        'current_voice': 'af_heart',
        'current_speed': 1.0
    }
    save_session(session)

    return jsonify({
        'session_id': session_id,
        'filename': file.filename,
        'total_pages': total_pages,
        'page_sizes': page_sizes
    })

@app.route('/api/session/<session_id>')
def get_session(session_id):
    session = load_session(session_id)
    if not session:
        return jsonify({'error': 'Session not found'}), 404
    return jsonify({
        'session_id': session['session_id'],
        'filename': session['filename'],
        'total_pages': session['total_pages'],
        'page_sizes': session['page_sizes'],
        'generated_pages': session.get('generated_pages', {})
    })

@app.route('/api/pdf/<session_id>')
def serve_pdf(session_id):
    session = load_session(session_id)
    if not session:
        return jsonify({'error': 'Session not found'}), 404
    return send_file(session['pdf_path'], mimetype='application/pdf')

@app.route('/api/generate-page', methods=['POST'])
def generate_page():
    data = request.get_json()
    session_id = data.get('session_id')
    page_num = data.get('page_num')
    voice = data.get('voice', 'af_heart')
    speed = float(data.get('speed', 1.0))

    if not session_id or page_num is None:
        return jsonify({'error': 'Missing session_id or page_num'}), 400

    session = load_session(session_id)
    if not session:
        return jsonify({'error': 'Session not found'}), 404

    page_dir = os.path.join(get_session_dir(session_id), 'pages', str(page_num))
    page_data_path = os.path.join(page_dir, 'page.json')
    status_path = os.path.join(page_dir, 'status.json')

    if os.path.exists(page_data_path):
        with open(page_data_path) as f:
            page_data = json.load(f)
        threading.Thread(target=prefetch_pages, args=(session_id, page_num, voice, speed), daemon=True).start()
        return jsonify(page_data)

    if os.path.exists(status_path):
        with open(status_path) as f:
            st = json.load(f)
        if st['status'] == 'generating':
            return jsonify({'status': 'generating', 'page': page_num, 'progress': st['progress'], 'total': st['total']})

    threading.Thread(target=generate_and_prefetch, args=(session_id, page_num, voice, speed), daemon=True).start()
    return jsonify({'status': 'generating', 'page': page_num, 'progress': 0, 'total': 0})

def generate_and_prefetch(session_id, page_num, voice, speed):
    generate_page_audio(session_id, page_num, voice, speed)
    prefetch_pages(session_id, page_num, voice, speed)

@app.route('/api/page-status/<session_id>/<int:page_num>')
def page_status(session_id, page_num):
    page_dir = os.path.join(get_session_dir(session_id), 'pages', str(page_num))
    page_data_path = os.path.join(page_dir, 'page.json')
    status_path = os.path.join(page_dir, 'status.json')

    if os.path.exists(page_data_path):
        with open(page_data_path) as f:
            data = json.load(f)
        return jsonify({'status': 'ready', 'total_segments': data['total_segments']})

    if os.path.exists(status_path):
        with open(status_path) as f:
            st = json.load(f)
        return jsonify({'status': st['status'], 'progress': st['progress'], 'total': st['total']})

    return jsonify({'status': 'not_generated', 'total_segments': 0})

@app.route('/api/page-data/<session_id>/<int:page_num>')
def page_data(session_id, page_num):
    page_dir = os.path.join(get_session_dir(session_id), 'pages', str(page_num))
    page_data_path = os.path.join(page_dir, 'page.json')
    if os.path.exists(page_data_path):
        with open(page_data_path) as f:
            return jsonify(json.load(f))
    return jsonify({'error': 'Page data not found'}), 404

@app.route('/api/generate-next-pages', methods=['POST'])
def generate_next_pages():
    data = request.get_json()
    session_id = data.get('session_id')
    current_page = data.get('current_page')
    voice = data.get('voice', 'af_heart')
    speed = float(data.get('speed', 1.0))
    n_ahead = int(data.get('n_ahead', 3))

    threading.Thread(target=prefetch_pages, args=(session_id, current_page, voice, speed, n_ahead), daemon=True).start()
    return jsonify({'status': 'prefetch_started'})

@app.route('/api/voices')
def list_voices():
    return jsonify([
        'af_heart','af_bella','af_sarah','af_sky','af_nicole',
        'af_alloy','af_aoede','af_jessica','af_kore','af_nova','af_river',
        'am_adam','am_echo','am_eric','am_fenrir','am_liam','am_michael',
        'am_onyx','am_puck','am_santa',
    ])

@app.route('/static/sessions/<path:filename>')
def serve_session_file(filename):
    return send_from_directory(app.config['SESSIONS_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=False, threaded=True)

def create_app():
    import flask
    return app
