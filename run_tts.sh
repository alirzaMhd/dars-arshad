#!/usr/bin/env python3
"""Run the Kokoro TTS PDF Reader with cloudflared tunnel."""
import subprocess
import sys
import os
import time
import signal
import re
import atexit

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APP_PATH = os.path.join(BASE_DIR, 'tts_app', 'app.py')

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
    [sys.executable, APP_PATH],
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
)
processes.append(flask_proc)

time.sleep(2)

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
        print(line, end='')
        m = re.search(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com', line)
        if m:
            url = m.group(0)
            break

if url:
    print("\n" + "=" * 60)
    print(f"✅ READY: Open this URL in your browser:")
    print(f"   {url}")
    print("=" * 60)
    print("Press Ctrl+C to stop the server.\n")
else:
    print("Failed to get cloudflared URL. Check logs.")
    sys.exit(1)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nShutting down...")
