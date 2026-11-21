#!/usr/bin/env python3
"""Synchronize generated release-version references from the canonical VERSION file."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
if not VERSION.isdigit():
    raise SystemExit("VERSION must contain a numeric release version.")

version_path = ROOT / "version.json"
data = json.loads(version_path.read_text(encoding="utf-8"))
data["version"] = VERSION
version_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(ROOT / "version.txt").write_text(VERSION + "\n", encoding="utf-8")

index_path = ROOT / "index.html"
html = index_path.read_text(encoding="utf-8")
html, count = re.subn(
    r'(<meta name="application-version" content=")[0-9]+(">)',
    lambda m: m.group(1) + VERSION + m.group(2), html, count=1
)
if count != 1:
    raise SystemExit("Could not locate application-version meta tag.")
html, count = re.subn(
    r'(id="footer-version" data-version=")[0-9]+(">V)[0-9]+(</span>)',
    lambda m: m.group(1) + VERSION + m.group(2) + VERSION + m.group(3), html, count=1
)
if count != 1:
    raise SystemExit("Could not locate footer version label.")
index_path.write_text(html, encoding="utf-8")

sw_path = ROOT / "sw.js"
sw = sw_path.read_text(encoding="utf-8")
sw = re.sub(r"Princess Kingdom V[0-9]+", f"Princess Kingdom V{VERSION}", sw, count=1)
sw = re.sub(
    r"(const CACHE_NAME = 'princess-kingdom-v)[0-9]+(-release';)",
    lambda m: m.group(1) + VERSION + m.group(2), sw, count=1
)
sw = re.sub(r"(scene[.]jpg[?]v=)[0-9]+", lambda m: m.group(1) + VERSION, sw)
sw = re.sub(r"(music[.]mp3[?]v=)[0-9]+", lambda m: m.group(1) + VERSION, sw)
sw_path.write_text(sw, encoding="utf-8")
print(f"Synchronized Princess Kingdom version {VERSION}.")
