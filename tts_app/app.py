import os, uuid, json, re, threading, time, importlib, subprocess, shutil, tempfile
import numpy as np
import soundfile as sf
import pymupdf
import torch
from flask import Flask, request, jsonify, send_file, render_template, send_from_directory, after_this_request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def convert_to_mp3(wav_path, mp3_path, sample_rate=24000):
    subprocess.run(
        ['ffmpeg', '-y', '-i', wav_path,
         '-codec:a', 'libmp3lame', '-b:a', '64k', '-ar', str(sample_rate), '-ac', '1', mp3_path],
        capture_output=True, check=True
    )
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

    # Strategy 1: search_for with various whitespace normalizations
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

    # Strategy 2: word-level matching fallback
    # Build a word-level representation of the page to handle whitespace/encoding mismatches
    norm_text = re.sub(r'\s+', ' ', text).strip()
    try:
        words = page.get_text("words")
    except Exception:
        words = []
    if words and norm_text:
        # words: [(x0,y0,x1,y1,"word",block_no,line_no,word_no), ...]
        word_strs = [w[4] for w in words]
        # Build normalized page text with separator tracking
        sep = [' '] * len(word_strs)
        page_norm = ''
        word_spans = []  # (start_char, end_char, rect)
        for i, ws in enumerate(word_strs):
            start = len(page_norm)
            if page_norm and not page_norm[-1].isspace():
                page_norm += ' '
                start += 1
            page_norm += ws
            end = len(page_norm)
            word_spans.append((start, end, (words[i][0], words[i][1], words[i][2], words[i][3])))

        # Try to find the normalized text in the page text
        idx = page_norm.find(norm_text)
        if idx >= 0:
            end_idx = idx + len(norm_text)
            # Collect rects for words overlapping with [idx, end_idx)
            result = []
            for ws in word_spans:
                if ws[0] < end_idx and ws[1] > idx:
                    result.append(list(ws[2]))
            if result:
                return result

        # Try fuzzy matching with shorter substrings
        for length in (120, 80, 50, 30):
            snippet = norm_text[:length].strip()
            if not snippet:
                continue
            idx = page_norm.find(snippet)
            if idx >= 0:
                end_idx = idx + len(snippet)
                result = []
                for ws in word_spans:
                    if ws[0] < end_idx and ws[1] > idx:
                        result.append(list(ws[2]))
                if result:
                    return result

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
    os.makedirs(page_dir, exist_ok=True)

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
    total_segments = len(segments)

    all_audio = []
    segment_meta = []
    cumulative_time = 0.0
    sample_rate = 24000

    for idx, seg in enumerate(segments):
        text = seg['text']
        audio_data = []
        for result in get_pipeline()(text, voice=voice, speed=speed):
            if result.audio is not None:
                audio_data.append(result.audio)
        if audio_data:
            if hasattr(audio_data[0], 'cpu'):
                full_audio = torch.cat(audio_data).cpu().numpy()
            else:
                full_audio = np.concatenate(audio_data)
            duration = len(full_audio) / sample_rate
            all_audio.append(full_audio)
        else:
            duration = 0

        start_time = cumulative_time
        cumulative_time += duration

        segment_meta.append({
            'index': idx,
            'text': text,
            'rects': seg['rects'],
            'duration': duration,
            'start_time': start_time,
            'end_time': cumulative_time,
        })

        with open(status_path, 'w') as f:
            json.dump({'status': 'generating', 'progress': idx + 1, 'total': total_segments}, f)

    if all_audio:
        combined = np.concatenate(all_audio)
        temp_wav = os.path.join(page_dir, 'page_audio.wav')
        sf.write(temp_wav, combined, sample_rate)
        mp3_path = os.path.join(page_dir, 'page_audio.mp3')
        convert_to_mp3(temp_wav, mp3_path, sample_rate)
        os.remove(temp_wav)
        audio_url = f'/static/sessions/{session_id}/pages/{page_num}/page_audio.mp3'
    else:
        audio_url = None
        cumulative_time = 0

    page_data = {
        'page': page_num,
        'segments': segment_meta,
        'total_segments': total_segments,
        'status': 'ready',
        'audio_url': audio_url,
        'total_duration': cumulative_time,
    }

    page_data_path = os.path.join(page_dir, 'page.json')
    with open(page_data_path, 'w') as f:
        json.dump(page_data, f)

    with open(status_path, 'w') as f:
        json.dump({'status': 'ready', 'progress': total_segments, 'total': total_segments}, f)

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

# ─── Chat / RAG helpers ───

STRIP_ARTIFACTS_RE = re.compile(
    r'[\u2500-\u257F\u2580-\u259F\u2800-\u28FF]'
    r'|[█▀▁▂▃▄▅▆▇▉▊▋▌▍▎▏▔▕▖▗▘▙▚▛▜▝▞▟]'
    r'|[⠁-⣿]'
    r'|[\u2300-\u23FF]'
    r'|[⟳⟲↻↺○◌◍◎●◉⏳⏰⌛⌚]'
    r'|[▓▒░]'
    r'|\x1b\[[0-9;?]*[a-zA-Z]'
    r'|\x1b\][^\x07]*\x07'
    r'|\x1b\[\?[0-9;]*[a-zA-Z]'
    r'|\x1b\[>[0-9;]*[a-zA-Z]'
)
ANSI_RE = re.compile(r'\x1b\[[0-9;?]*[a-zA-Z]|\x1b\][^\x07]*\x07|\x1b\[\?[0-9;]*[a-zA-Z]|\x1b\[>[0-9;]*[a-zA-Z]')

def strip_artifacts(text: str) -> str:
    if not text:
        return ''
    text = ANSI_RE.sub('', text)
    text = STRIP_ARTIFACTS_RE.sub('', text)
    text = re.sub(r'[ \t]+\n', '\n', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'^\s+$', '', text, flags=re.MULTILINE)
    return text.strip()

CHAT_DIR_NAME = 'chats'
PDF_TEXT_NAME = 'pdf_text.txt'
PDF_TEXT_MAX_CHARS = 80_000
PDF_TEXT_HEAD = 60_000
PDF_TEXT_TAIL = 20_000

def chat_dir(pdf_session_id: str) -> str:
    d = os.path.join(get_session_dir(pdf_session_id), CHAT_DIR_NAME)
    os.makedirs(d, exist_ok=True)
    return d

def chat_path(pdf_session_id: str, chat_id: str) -> str:
    return os.path.join(chat_dir(pdf_session_id), f'{chat_id}.json')

def load_chat(pdf_session_id: str, chat_id: str):
    p = chat_path(pdf_session_id, chat_id)
    if not os.path.exists(p):
        return None
    with open(p) as f:
        return json.load(f)

def save_chat(chat: dict):
    pdf_sid = chat['pdf_session_id']
    p = chat_path(pdf_sid, chat['id'])
    with open(p, 'w') as f:
        json.dump(chat, f, ensure_ascii=False, indent=2)

def extract_full_pdf_text(pdf_path: str) -> str:
    doc = pymupdf.open(pdf_path)
    parts = []
    try:
        for page in doc:
            parts.append(page.get_text("text"))
    finally:
        doc.close()
    return '\n\n'.join(parts).strip()

def get_cached_pdf_text(pdf_session_id: str) -> dict:
    session = load_session(pdf_session_id)
    if not session:
        return None
    sdir = get_session_dir(pdf_session_id)
    text_path = os.path.join(sdir, PDF_TEXT_NAME)
    if not os.path.exists(text_path):
        full = extract_full_pdf_text(session['pdf_path'])
        with open(text_path, 'w') as f:
            f.write(full)
    else:
        with open(text_path) as f:
            full = f.read()
    truncated = False
    text = full
    if len(full) > PDF_TEXT_MAX_CHARS:
        text = full[:PDF_TEXT_HEAD] + '\n\n[... middle truncated for context window ...]\n\n' + full[-PDF_TEXT_TAIL:]
        truncated = True
    return {
        'chars': len(full),
        'truncated': truncated,
        'text': text,
        'pages': session.get('total_pages', 0),
        'filename': session.get('filename', 'document.pdf'),
    }

def build_rag_prompt(pdf_meta: dict, history: list, user_msg: str, focus: str = '', system_action: str = '') -> str:
    sys_lines = [
        'You are a helpful assistant discussing a PDF with the user.',
        f'The PDF "{pdf_meta["filename"]}" has {pdf_meta["pages"]} pages and {pdf_meta["chars"]} characters of text.',
        'The full PDF text is included below as context. Answer questions about it accurately.',
        'If the user has selected a passage, it is marked with >>> ... <<< markers — pay special attention to it.',
        'Use markdown formatting. Be concise. Do not invent facts not present in the PDF.',
    ]
    if pdf_meta.get('truncated'):
        sys_lines.append(
            'NOTE: The PDF was very large; the middle portion was truncated to fit the context window. '
            'Pages at the start and end are intact. If the user asks about a middle section you don\'t have, '
            'say so and suggest they re-select that passage as context.'
        )
    if system_action:
        sys_lines.append('')
        sys_lines.append(f'TASK: {system_action}')
    sys_block = '\n'.join(sys_lines)

    pdf_block = f'=== PDF: {pdf_meta["filename"]} ===\n{pdf_meta["text"]}\n=== END PDF ==='

    history_lines = []
    for m in history[-12:]:
        role = 'User' if m.get('role') == 'user' else 'Assistant'
        history_lines.append(f'{role}: {m.get("content", "")}')
    history_block = '\n'.join(history_lines) if history_lines else '(no prior messages)'

    user_block = user_msg
    if focus and focus.strip():
        user_block = f'>>> FOCUSED PASSAGE FROM PDF <<<\n{focus.strip()}\n>>> END FOCUS <<<\n\n{user_block}'

    return (
        f'{sys_block}\n\n{pdf_block}\n\n'
        f'--- Conversation so far ---\n{history_block}\n\n'
        f'User: {user_block}\nAssistant:'
    )

def list_chat_models() -> list:
    try:
        out = subprocess.check_output(['opencode', 'models'], stderr=subprocess.PIPE, timeout=20)
        out = out.decode('utf-8', 'ignore')
    except Exception as e:
        print(f'[chat] opencode models failed: {e!r}', flush=True)
        return [{'id': 'opencode/big-pickle', 'name': 'big-pickle (default)'}]
    models = []
    seen = set()
    for line in out.splitlines():
        s = line.strip()
        if not s or s.startswith('"') or s.lower().startswith('model'):
            continue
        for token in re.findall(r'[\w.\-]+/[\w.\-]+', s):
            if token in seen:
                continue
            seen.add(token)
            name = token.split('/', 1)[1] if '/' in token else token
            models.append({'id': token, 'name': name})
    if not models:
        return [{'id': 'opencode/big-pickle', 'name': 'big-pickle (default)'}]
    return models

def opencode_stream_chat(prompt: str, model: str, opencode_session_id: str = None):
    """Yield ('text'|'reasoning'|'done'|'error'|'session', payload) tuples from opencode run."""
    args = [
        'opencode', 'run',
        '--format', 'json',
        '--thinking',
        '--dangerously-skip-permissions',
        '--model', model,
    ]
    if opencode_session_id:
        args += ['--session', opencode_session_id]
    prompt = prompt.replace('\x00', '')
    args.append(prompt)
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
    first_session_id = opencode_session_id
    try:
        while True:
            line = proc.stdout.readline()
            if not line:
                break
            line = line.strip()
            if not line:
                continue
            try:
                evt = json.loads(line)
            except Exception:
                continue
            sid = evt.get('sessionID')
            if sid and not first_session_id:
                first_session_id = sid
                yield ('session', {'sessionID': sid})
            etype = evt.get('type')
            part = evt.get('part') or {}
            if etype in ('text',):
                chunk = part.get('text') or evt.get('text') or evt.get('content') or ''
                if chunk:
                    yield ('text', strip_artifacts(chunk))
            elif etype in ('reasoning',):
                chunk = part.get('text') or ''
                if chunk:
                    yield ('reasoning', strip_artifacts(chunk))
            elif etype in ('step-finish', 'step_finish'):
                if first_session_id:
                    yield ('done', {'sessionID': first_session_id})
                else:
                    yield ('done', {})
                return
            elif etype in ('error',):
                err = part.get('error') or evt.get('error') or 'opencode error'
                yield ('error', str(err))
        stderr = (proc.stderr.read() or '').strip() if proc.stderr else ''
        if proc.poll() not in (0, None) and stderr:
            yield ('error', strip_artifacts(stderr)[:500])
        if first_session_id:
            yield ('done', {'sessionID': first_session_id})
    finally:
        try:
            if proc.poll() is None:
                proc.kill()
        except Exception:
            pass

def find_chat_by_id(chat_id: str):
    """Locate a chat file by id across all pdf sessions."""
    base = app.config['SESSIONS_FOLDER']
    if not os.path.isdir(base):
        return None, None
    for pdf_sid in os.listdir(base):
        candidate = os.path.join(base, pdf_sid, CHAT_DIR_NAME, f'{chat_id}.json')
        if os.path.exists(candidate):
            with open(candidate) as f:
                return json.load(f), pdf_sid
    return None, None

def chat_to_meta(chat: dict) -> dict:
    return {
        'id': chat['id'],
        'pdf_session_id': chat['pdf_session_id'],
        'title': chat.get('title', 'New chat'),
        'model': chat.get('model'),
        'opencode_session_id': chat.get('opencode_session_id'),
        'created_at': chat.get('created_at'),
        'updated_at': chat.get('updated_at'),
        'message_count': len(chat.get('messages', [])),
    }

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

@app.route('/api/clear-session-audio', methods=['POST'])
def clear_session_audio():
    data = request.get_json()
    session_id = data.get('session_id')
    if not session_id:
        return jsonify({'error': 'Missing session_id'}), 400
    pages_dir = os.path.join(get_session_dir(session_id), 'pages')
    if os.path.exists(pages_dir):
        for entry in os.listdir(pages_dir):
            p = os.path.join(pages_dir, entry)
            if os.path.isdir(p):
                shutil.rmtree(p)
    session = load_session(session_id)
    if session:
        session['generated_pages'] = {}
        save_session(session)
    return jsonify({'status': 'cleared'})

@app.route('/api/voices')
def list_voices():
    return jsonify([
        'af_heart','af_bella','af_sarah','af_sky','af_nicole',
        'af_alloy','af_aoede','af_jessica','af_kore','af_nova','af_river',
        'am_adam','am_echo','am_eric','am_fenrir','am_liam','am_michael',
        'am_onyx','am_puck','am_santa',
    ])

# ─── Chat endpoints ───

_chat_send_locks = {}
_chat_send_locks_mu = threading.Lock()

def _get_chat_lock(chat_id: str) -> threading.Lock:
    with _chat_send_locks_mu:
        lk = _chat_send_locks.get(chat_id)
        if lk is None:
            lk = threading.Lock()
            _chat_send_locks[chat_id] = lk
        return lk

@app.route('/api/chat/models')
def chat_models():
    return jsonify({'models': list_chat_models()})

@app.route('/api/chat/pdf-text/<pdf_session_id>')
def chat_pdf_text(pdf_session_id):
    meta = get_cached_pdf_text(pdf_session_id)
    if not meta:
        return jsonify({'error': 'PDF session not found'}), 404
    return jsonify({
        'chars': meta['chars'],
        'pages': meta['pages'],
        'truncated': meta['truncated'],
        'filename': meta['filename'],
    })

@app.route('/api/chat/sessions', methods=['POST'])
def create_chat_session():
    data = request.get_json(silent=True) or {}
    pdf_sid = data.get('pdf_session_id')
    if not pdf_sid or not load_session(pdf_sid):
        return jsonify({'error': 'pdf_session_id required'}), 400
    chat_id = str(uuid.uuid4())[:12]
    model = data.get('model') or 'opencode/big-pickle'
    now = time.time()
    chat = {
        'id': chat_id,
        'pdf_session_id': pdf_sid,
        'title': data.get('title') or 'New chat',
        'model': model,
        'opencode_session_id': None,
        'created_at': now,
        'updated_at': now,
        'messages': [],
    }
    save_chat(chat)
    return jsonify({'chat': chat_to_meta(chat)}), 201

@app.route('/api/chat/sessions/<pdf_session_id>')
def list_chat_sessions(pdf_session_id):
    if not load_session(pdf_session_id):
        return jsonify({'error': 'PDF session not found'}), 404
    d = chat_dir(pdf_session_id)
    out = []
    for fn in sorted(os.listdir(d), reverse=True):
        if not fn.endswith('.json'):
            continue
        try:
            with open(os.path.join(d, fn)) as f:
                c = json.load(f)
            out.append(chat_to_meta(c))
        except Exception:
            pass
    out.sort(key=lambda c: c.get('updated_at') or 0, reverse=True)
    return jsonify({'chats': out})

@app.route('/api/chat/session/<chat_id>')
def get_chat_session(chat_id):
    chat, pdf_sid = find_chat_by_id(chat_id)
    if not chat:
        return jsonify({'error': 'Chat not found'}), 404
    return jsonify({'chat': chat, 'meta': chat_to_meta(chat), 'pdf_session_id': pdf_sid})

@app.route('/api/chat/session/<chat_id>', methods=['DELETE'])
def delete_chat_session(chat_id):
    chat, pdf_sid = find_chat_by_id(chat_id)
    if not chat:
        return jsonify({'error': 'Chat not found'}), 404
    p = chat_path(pdf_sid, chat_id)
    try:
        os.remove(p)
    except FileNotFoundError:
        pass
    return jsonify({'ok': True})

@app.route('/api/chat/session/<chat_id>', methods=['PATCH'])
def patch_chat_session(chat_id):
    chat, pdf_sid = find_chat_by_id(chat_id)
    if not chat:
        return jsonify({'error': 'Chat not found'}), 404
    data = request.get_json(silent=True) or {}
    if 'title' in data and isinstance(data['title'], str):
        chat['title'] = data['title'].strip()[:120] or chat['title']
    if 'model' in data and isinstance(data['model'], str):
        chat['model'] = data['model']
    chat['updated_at'] = time.time()
    save_chat(chat)
    return jsonify({'meta': chat_to_meta(chat)})

@app.route('/api/chat/send', methods=['POST'])
def chat_send():
    data = request.get_json(silent=True) or {}
    chat_id = data.get('chat_id')
    user_msg = (data.get('message') or '').strip()
    focus = (data.get('focus') or '').strip()
    action = (data.get('action') or '').strip()
    if not chat_id or not user_msg:
        return jsonify({'error': 'chat_id and message required'}), 400

    chat, pdf_sid = find_chat_by_id(chat_id)
    if not chat:
        return jsonify({'error': 'Chat not found'}), 404

    pdf_meta = get_cached_pdf_text(pdf_sid)
    if not pdf_meta:
        return jsonify({'error': 'PDF session not found'}), 404

    def gen():
        with _get_chat_lock(chat_id):
            now = time.time()
            user_entry = {
                'id': f'm_{int(now*1000)}_u',
                'role': 'user',
                'content': user_msg,
                'focus': focus[:4000] if focus else None,
                'action': action or None,
                'timestamp': now,
            }
            chat['messages'].append(user_entry)
            chat['updated_at'] = now
            if chat.get('title') in (None, '', 'New chat'):
                first = (user_msg[:60] + ('…' if len(user_msg) > 60 else ''))
                chat['title'] = first
            save_chat(chat)

            yield f"event: meta\ndata: {json.dumps({'chat_id': chat_id, 'user_message_id': user_entry['id'], 'title': chat['title']})}\n\n"

            prompt = build_rag_prompt(
                pdf_meta=pdf_meta,
                history=chat['messages'][:-1],
                user_msg=user_msg,
                focus=focus,
                system_action=action,
            )
            model = chat.get('model') or 'opencode/big-pickle'

            full_text = ''
            full_reasoning = ''
            sid = chat.get('opencode_session_id')
            try:
                for kind, payload in opencode_stream_chat(prompt, model, sid):
                    if kind == 'text':
                        full_text += payload
                        yield f"event: text\ndata: {json.dumps({'chunk': payload})}\n\n"
                    elif kind == 'reasoning':
                        full_reasoning += payload
                        yield f"event: reasoning\ndata: {json.dumps({'chunk': payload})}\n\n"
                    elif kind == 'session':
                        chat['opencode_session_id'] = payload['sessionID']
                    elif kind == 'done':
                        if payload.get('sessionID'):
                            chat['opencode_session_id'] = payload['sessionID']
                    elif kind == 'error':
                        yield f"event: error\ndata: {json.dumps({'error': payload})}\n\n"
                        break
            except Exception as e:
                yield f"event: error\ndata: {json.dumps({'error': str(e)})}\n\n"

            full_text = strip_artifacts(full_text)
            if full_text or full_reasoning:
                now2 = time.time()
                assistant_entry = {
                    'id': f'm_{int(now2*1000)}_a',
                    'role': 'assistant',
                    'content': full_text,
                    'reasoning': strip_artifacts(full_reasoning) or None,
                    'timestamp': now2,
                }
                chat['messages'].append(assistant_entry)
                chat['updated_at'] = now2
                save_chat(chat)
                yield f"event: assistant\ndata: {json.dumps({'message': assistant_entry})}\n\n"
            yield "event: done\ndata: {}\n\n"

    headers = {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache, no-transform',
        'X-Accel-Buffering': 'no',
        'Connection': 'keep-alive',
    }
    return app.response_class(gen(), mimetype='text/event-stream', headers=headers)

import tempfile

@app.route('/api/download-annotated/<session_id>', methods=['POST'])
def download_annotated(session_id):
    session = load_session(session_id)
    if not session:
        return jsonify({'error': 'Session not found'}), 404

    data = request.get_json(silent=True) or {}
    highlights = data.get('highlights', [])
    notes = data.get('notes', [])
    client_scale = float(data.get('scale', 1.5))

    doc = pymupdf.open(session['pdf_path'])

    for hl in highlights:
        page_num = hl.get('page', 0)
        text = hl.get('text', '')
        color_hex = hl.get('color', '#FFFF00')
        viewport_rects = hl.get('rects', [])
        if page_num < 0 or page_num >= len(doc):
            continue
        page = doc[page_num]
        r, g, b = _hex_to_rgb(color_hex)

        # Strategy 1: find text via search
        rects = find_segment_rects(page, text)

        # Strategy 2: use frontend viewport rects converted to PDF coords
        if not rects and viewport_rects:
            pdf_page_height = page.rect.height
            for vr in viewport_rects:
                x0 = vr.get('x', 0) / client_scale
                y0_viewport = vr.get('y', 0)
                w = vr.get('w', 0) / client_scale
                h = vr.get('h', 0) / client_scale
                # Convert viewport coords (y-down from top) to PDF coords (y-down from top)
                # In the frontend, y is measured from the top of the page-wrapper
                # In PDF coords, y is also from the top, so just divide by scale
                y0 = y0_viewport / client_scale
                rects.append([x0, y0, x0 + w, y0 + h])

        for rect in rects:
            try:
                r_obj = pymupdf.Rect(rect)
                annot = page.add_highlight_annot(r_obj)
                if annot:
                    annot.set_colors(stroke=(r, g, b))
                    annot.set_info(content=text[:2000], title="Kokoro Reader")
                    annot.update()
            except Exception as e:
                print(f'[download] highlight error: {e}', flush=True)

    for note in notes:
        page_num = note.get('page', 0)
        if page_num < 0 or page_num >= len(doc):
            continue
        page = doc[page_num]
        note_text = note.get('text', '')
        viewport_x = note.get('x', 50)
        viewport_y = note.get('y', 50)
        pdf_page_height = page.rect.height
        pdf_x = viewport_x / client_scale
        pdf_y = pdf_page_height - (viewport_y / client_scale)
        pdf_y = max(20, min(pdf_page_height - 20, pdf_y))
        pdf_x = max(20, min(page.rect.width - 20, pdf_x))
        try:
            annot = page.add_text_annot((pdf_x, pdf_y), note_text)
            if annot:
                annot.set_info(title="Kokoro Reader", content=note_text[:2000])
                annot.set_colors(stroke=(1, 1, 0))
                annot.update()
        except Exception as e:
            print(f'[download] note error: {e}', flush=True)

    tmp = tempfile.NamedTemporaryFile(suffix='.pdf', delete=False, dir='/tmp')
    try:
        doc.save(tmp.name)
        doc.close()
        tmp.close()
        @after_this_request
        def cleanup(response):
            try:
                os.unlink(tmp.name)
            except Exception:
                pass
            return response
        return send_file(
            tmp.name,
            mimetype='application/pdf',
            as_attachment=True,
            download_name=f'annotated_{session.get("filename", "document.pdf")}'
        )
    except Exception as e:
        doc.close()
        try:
            os.unlink(tmp.name)
        except Exception:
            pass
        return jsonify({'error': str(e)}), 500


def _hex_to_rgb(hex_color):
    h = hex_color.lstrip('#')
    return tuple(int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4))


@app.route('/static/sessions/<path:filename>')
def serve_session_file(filename):
    return send_from_directory(app.config['SESSIONS_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=False, threaded=True)

def create_app():
    import flask
    return app
