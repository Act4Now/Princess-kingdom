# Princess Kingdom — Changelog

## V24 — 2026-11-20
- Eliminated horizontal light/yellow artifacts from the lower embedded artwork.
- Replaced the vertically stretched lower background with a naturally scaled repeating garden/paving extension.
- Restored a gold-framed footer while keeping the garden/paving visible behind it.
- Added `version.json` and `version.txt`; the footer reads its version label from `version.json` when available.
- Added an in-app update notice for installed PWAs while a new Service Worker version is installing.
- Kept automatic update checks, offline fallback and saved progress.

## V23 — 2026-11-20
- Compact footer and lower garden/paving continuation.
- Automatic Service Worker update checks and cache cleanup.
- Category buttons are all enabled when no challenge is active; active-category styling appears during a challenge.

## V22 — 2026-11-20
- Automatic update mechanism and category-button state corrections.

## V21 — 2026-11-20
- Initial automatic PWA update mechanism.

## V20 — 2026-11-20
- Compact footer.

## V25 — 2026-11-20

- Changed Service Worker app-shell strategy to cache-first so installed game opens from the local cache without waiting for network.
- Moved Service Worker update checks to a quiet background task after the page becomes interactive; checks are skipped while offline.
- Removed the startup network request for version.json; the footer version is embedded in the app shell and remains available offline.
- Redesigned 192px and 512px PWA icons with the Princess Kingdom castle emblem and the family-play motto for the installed-app launch screen.
- Replaced the blurred horizontal lower-artwork bands with a floral garden and clean pink cobblestone continuation.
- Updated the installed-app update notice with the new logo and family-play motto.
- Preserved the 600 challenge bank and local game progress.


## V26 — 2026-11-20
- Refined category button overlay corner geometry to match the illustrated buttons.
- Kept the selected orange frame inside the category button bounds.
- Shortened and centered the journal progress bar beneath its label and counter.
- Preserved all game behavior and offline-first update handling.


## V27 — 2026-11-20
- Fixed inconsistent version identifiers found in V26.
- `index.html` application-version metadata is now `27`; the footer reads this metadata instead of a stale hard-coded JavaScript value.
- Synchronized `version.json`, `version.txt`, Service Worker cache name, and update-reload session key to V27.
- Preserved all V26 layout and game functionality.
