"""Optional end-to-end smoke test. Requires `pip install playwright` and `playwright install chromium`.
Run from the project root: python tests/run_browser_smoke.py
"""
from contextlib import closing
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread
import socket
import os

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
with closing(socket.socket()) as sock:
    sock.bind(('127.0.0.1', 0))
    PORT = sock.getsockname()[1]
server = ThreadingHTTPServer(('127.0.0.1', PORT), SimpleHTTPRequestHandler)
thread = Thread(target=server.serve_forever, daemon=True)
thread.start()
errors = []
try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 390, 'height': 844})
        page.on('pageerror', lambda exc: errors.append(str(exc)))
        response = page.goto(f'http://127.0.0.1:{PORT}/', wait_until='networkidle')
        assert response and response.ok
        assert page.locator('#footer-version').inner_text() == 'V51'
        assert page.locator('#app').evaluate('(e)=>e.getBoundingClientRect().width') <= 390

        page.locator('#menu-toggle').click()
        assert page.locator('#v51-profile option').count() >= 1
        page.locator('#v51-team-open').click()
        assert page.locator('#v51-team-form').count() == 1
        page.locator('#v51-modal-close').click()

        page.locator('#menu-toggle').click()
        page.locator('#princess-mode-toggle').click()
        page.locator('#questions').click()
        assert page.locator('#v51-quiz').is_visible()
        assert page.locator('#v51-quiz [data-choice]').count() == 3
        page.locator('#v51-quiz [data-choice="0"]').click()
        assert page.locator('#v51-quiz-feedback').is_visible()

        page.locator('#menu-toggle').click()
        page.locator('#v51-adventure-open').click()
        assert page.locator('.v51-map-card').count() == 5
        page.locator('#v51-modal-close').click()

        page.locator('#menu-toggle').click()
        page.locator('#princess-mode-toggle').click()
        page.locator('#questions').click()
        page.locator('#adaptive-action').click()
        page.locator('#adaptive-action').click()
        page.locator('#menu-toggle').click()
        page.locator('#v51-certificate-open').click()
        assert page.locator('#v51-certificate-form').count() == 1
        page.locator('#v51-modal-close').click()

        page.locator('#menu-toggle').click()
        page.locator('#v51-editor-open').click()
        assert page.locator('#v51-custom-form').count() == 1
        page.locator('#v51-custom-form [name=label]').fill('A custom castle')
        page.locator('#v51-custom-form [name=task]').fill('Draw a castle with three towers.')
        page.locator('#v51-custom-form button[type=submit]').click()
        assert page.locator('#v51-custom-back').count() == 1
        assert not errors, errors
        browser.close()
finally:
    server.shutdown()
    server.server_close()
print('V51 browser smoke test passed.')
