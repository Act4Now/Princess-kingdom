# Princess Kingdom — Changelog

## V37 — 2026-11-21
- Added a compact, localized reset-statistics control beside on-device statistics.
- Reset requires confirmation and clears cumulative device statistics only; current game progress, completed challenges, and active challenge remain unchanged.
- Statistics display shows cumulative completed challenges only, without a remaining-count figure.
- Preserved the V36 layout, artwork, bilingual interface, drawing board, challenge bank, and offline assets.


## V36 — 2026-11-21
- Layout rebuilt: one continuous illustrated background (scene.jpg) with category buttons and journal anchored to the artwork and everything below the frame in normal flow. No hit-areas are positioned over blurred or leftover artwork any more.
- Category labels painted in the artwork were removed from the image and are now HTML text, so RO/EN labels sit exactly on the original buttons; the original crown/palette/masks/question-mark icons are kept.
- Journal is one opaque pill (label, counter and bar share the same data); challenge text auto-fits inside the ornamental frame.
- Primary action, "Desenează" board button, "Ajutor pentru adult" and "Joc nou" are a clean two-row grid; the board button only exists for Desen challenges.
- Fixed: a JavaScript error at startup (`$('.drawing-toolbar')`) that stopped the script before the service worker, drawing board and version label were initialised.
- Question challenges now show "Roagă un adult să citească întrebarea!" instead of an empty space; the question stays in the adult help.
- "Joc nou" needs a second tap (3.5 s window) before it erases progress.
- The active challenge and category survive a reload.
- Performance: artwork and music moved out of index.html (3.8 MB → ~175 KB); music re-encoded to 96 kbps; scene.jpg and music.mp3 are precached for offline use; service worker answers Range requests so audio also plays offline on Safari.
- "Online" chip is shown only when the device is offline.
- Progress, statistics, drawing board, 600 challenges and IDs are unchanged.

## V33 — 2026-11-21
- Equalized category-button hit-target heights and refined the selected orange frame so it remains inside the button bounds without an oversized outer glow.
- Extended the journal progress track to align more closely with the counter area.
- Expanded the „Ajutor pentru adult” and „Joc nou” hit areas to match the width of the category-progress card above.
- Preserved the V32 drawing board, 600 challenges, bilingual interface, local-only statistics, and offline-first behavior.

## V31 — 2026-11-21
- Combined the planned V31–V34 improvements into one release.
- Improved random selection using crypto.getRandomValues when available; unfinished challenges remain protected from repeats within the current shuffle cycle.
- Added responsive refinements for narrow screens, landscape mode, safe areas and touch interaction.
- Added a Romanian/English interface switch (Romanian default). Challenge-bank wording remains in its original Romanian text.
- Added cumulative completion and remaining-challenge statistics stored only in localStorage on this device. No analytics or cloud transmission is added.
- Hardened offline updates: the new worker precaches the full app shell before activation; failed installs do not replace the currently active worker.
- Preserved the 600 challenge IDs, existing completion progress, artwork and PWA assets.

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


## V28 — 2026-11-20
- Audited challenge inventory: 200 Desen, 200 Mimă, 200 Întrebări; all 600 IDs are unique.
- Replaced repeated Questions prompts and repeated answers; all 200 question prompts and answers are now distinct.
- Completed challenge IDs are excluded from future draws until Joc nou resets the game.
- Random shuffle cycles repeat only among unfinished challenges; completed categories show a completion state.
- Synchronized version metadata, footer, Service Worker cache, and update-reload key to V28.


## V29 — 2026-11-20
- The main „Provocare nouă” action now draws randomly from all unfinished challenges across all three categories, even after a category was selected.
- The category buttons remain category-specific; their selection behavior is unchanged.
- Completed challenges remain excluded until „Joc nou” resets the progress.
- Synchronized footer, metadata, version files, Service Worker cache, and update session key to V29.

## V30 — 2026-11-21
- Added explicit accessible names and button types to the game controls.
- Added visible keyboard focus indicators, including for the visually hidden „Joc nou” control.
- Added expanded-state and controlled-panel semantics to „Ajutor pentru adult”.
- Added accessible progress bars with current values for each category.
- Preserved the original artwork, challenge bank, local progress and offline-first launch behavior.


## V32 — 2026-11-21
- Added an accessible full-screen drawing board for Desen challenges, shown only when canvas and Pointer Events are supported.
- Added pen color/size, eraser, undo (maximum 10 snapshots), clear, Done and PNG download.
- Added DPR-aware canvas rendering, pointer input for mouse/touch/stylus, pressure-based width and animation-frame stroke rendering.
- Drawings and optional draft recovery remain local; no upload or sharing requests are made.
- Completing a challenge closes the board and clears in-game/draft data; previously downloaded PNGs remain on the device.
- Synchronized app version metadata and Service Worker cache to V32.


## V34 — 2026-11-21
- Added English translations for all 600 challenges, including drawing prompts, charades prompts, questions and answers.
- Replaced Romanian labels baked into the category and action artwork with accessible HTML labels that switch immediately between Romanian and English.
- Localized congratulations, category completion, adult help, drawing-board controls, update notice, progress labels, footer and on-device statistics.
- Statistics now use a single language-specific template with completed and remaining placeholders.
- The document `lang` attribute follows the selected language.
- Pencil and Eraser now have distinct selected styling, mutually exclusive `aria-pressed` states and a live selected-tool label.
- Preserved local progress, language preference, 600 challenge IDs, drawing-board behavior and offline-first update handling.


## V35 — 2026-11-21
- Fully opaque, symmetrically positioned HTML controls now cover the legacy adult-help/new-game artwork strip; only translated interactive controls remain visible.
- Footer fallback and runtime version display synchronized to V35.
- Synchronized application metadata, version files, Service Worker cache and update-reload key.
- Preserved V34 translations, challenge bank, local statistics, drawing board and offline-first behavior.
