#!/usr/bin/env python3
"""
Server locale per il Libro Inglese AR.
Esegui con: python server.py
Poi apri: http://localhost:8000
"""
import http.server, socketserver, os, pathlib, webbrowser, threading, sys

PORT = 8000
SERVE_DIR = pathlib.Path(__file__).resolve().parent.parent
os.chdir(SERVE_DIR)

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        super().end_headers()
    def log_message(self, format, *args):
        pass

def open_browser():
    import time; time.sleep(1)
    webbrowser.open(f"http://localhost:{PORT}/webapp/index.html")

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
print(f"""
+------------------------------------------+
|   The Magic English Book  AR             |
+------------------------------------------+
|  Server avviato!                         |
|  Apri: http://localhost:{PORT}/webapp/    |
|  Premi CTRL+C per fermare               |
+------------------------------------------+
""")

threading.Thread(target=open_browser, daemon=True).start()
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
