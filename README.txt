PRINCESS KINGDOM — PWA V49

All application files are in this folder; the archive contains no nested project folder.
Upload the contents of this folder to the desired GitHub Pages directory.

Main files:
- index.html — app and challenge banks (600 Classic + 150 Princess)
- princess-*.webp / princess-*.svg — 50 dedicated Princess Mode portraits plus a fallback
- scene.jpg, music.mp3 — background artwork and music
- sw.js — offline cache and service worker
- manifest.webmanifest and icon-*.png — PWA installation assets
- VERSION — canonical release version; scripts/sync_version.py synchronizes generated version metadata
- version.json, version.txt — release metadata
- CHANGELOG.md — release history
- CREDITS.md — artwork provenance and licensing notes
- tests/test_release.py — automated release integrity tests

Publish through HTTPS. The service worker does not run through file://.
Game progress is stored locally and separately for Classic and Princess modes.

V43 introduced Princess Mode (150 challenges) and separate mode progress.
V49 completes the 50-subject Princess Mode image set, adds the Princess Album and automated release checks.

Release maintenance:
- Run `python scripts/sync_version.py` after changing VERSION to synchronize generated version references.
- Run `python -m unittest discover -s tests -v` to execute the release integrity suite.
