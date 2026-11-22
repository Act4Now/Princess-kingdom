PRINCESS KINGDOM — PWA V50

The archive contains the complete deployable project at its root. Upload all files and folders to the same GitHub Pages directory; do not omit v50-enhancements.js.

V50 features:
- 600 Classic + 150 Princess base challenges and all V49 portraits/album features.
- Princess Mode reflection quiz with discussion choices.
- Optional charades timer.
- Family Team Mode (2–4 teams).
- Up to four local player profiles with separate progress by game mode.
- Parent Challenge Editor (custom challenges in Classic Mode).
- IndexedDB drawing gallery with localStorage migration/fallback.
- Five-region Adventure Map.
- Printable achievement certificates (Print > Save as PDF).
- Accessibility controls: text scale, high contrast, reduced motion and speech speed.

Release files:
- index.html — main app shell and original challenge banks.
- v50-enhancements.js — V50 feature implementation.
- sw.js — offline service worker; includes the V50 enhancement script in its cache.
- VERSION — canonical release version.
- version.json, version.txt — generated release metadata.
- tests/ — release integrity and browser smoke tests.

Publish over HTTPS. Service workers do not run from file://.

Run release checks:
  python scripts/sync_version.py
  python -m unittest discover -s tests -v
  python tests/run_browser_smoke.py  (optional; requires Playwright + Chromium)

For browser smoke tests, install Playwright for Python and Chromium. The test suite will skip browser-only checks if Playwright is unavailable.

V51 UPDATE NOTES
- Upload/replace index.html, v50-enhancements.js, sw.js, version.json, version.txt and CHANGELOG.md.
- Princess artwork files are intentionally not included. Keep the existing princess-*.webp, princess-*.svg and princess-fallback.svg files from your V50 installation. The service worker continues to reference these existing files.
- Existing profile IDs and saved data are preserved. Use the new delete button in the player menu to remove a profile and its saved progress.
