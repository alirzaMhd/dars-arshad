#!/usr/bin/env python3
"""Run the Kokoro TTS PDF Reader with Flask + cloudflared tunnel."""
import subprocess
import sys
import os
import time
import signal
import re
import atexit
import socket

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(BASE_DIR, 'tts_app')
os.chdir(APP_DIR)

processes = []

def cleanup():
    for p in processes:
        try:
            p.terminate()
            p.wait(timeout=3)
        except:
            try:
                p.kill()
            except:
                pass

atexit.register(cleanup)
signal.signal(signal.SIGINT, lambda *a: sys.exit(0))
signal.signal(signal.SIGTERM, lambda *a: sys.exit(0))

print("=" * 60)
print("Kokoro TTS PDF Reader")
print("=" * 60)

flask_proc = subprocess.Popen(
    [sys.executable, 'app.py'],
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
)
processes.append(flask_proc)

print("Waiting for Flask server...", end='', flush=True)
start = time.time()
while time.time() - start < 60:
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect(('localhost', 8081))
        s.close()
        print(" READY")
        break
    except:
        print('.', end='', flush=True)
        time.sleep(0.5)
else:
    print("\nServer failed to start.")
    sys.exit(1)

cloudflared_proc = subprocess.Popen(
    ['cloudflared', 'tunnel', '--url', 'http://localhost:8081'],
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
)
processes.append(cloudflared_proc)

url = None
start = time.time()
while url is None and time.time() - start < 30:
    line = cloudflared_proc.stdout.readline()
    if line:
        m = re.search(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com', line)
        if m:
            url = m.group(0)
            break

if url:
    print("\n" + "=" * 60)
    print(f"✅ READY: Open this URL in your browser:")
    print(f"   {url}")
    print("=" * 60)
    print("* Upload a PDF to start")
    print("* Navigate pages with arrow keys or toolbar buttons")
    print("* Click '🎧 Read Aloud' to listen paragraph by paragraph")
    print("* Audio auto-generates for next pages in background")
    print("* Supports zoom, dark mode, fit to width\n")
else:
    print("Failed to get cloudflared URL. Check logs.")
    print("Make sure cloudflared is installed:")
    print("  dpkg -i /content/cloudflared-linux-amd64.deb")
    sys.exit(1)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nShutting down...")
