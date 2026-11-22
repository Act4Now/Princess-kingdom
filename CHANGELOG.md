# Princess Kingdom V50 — 2026-11-21

## Family Adventure, Learning and Accessibility Expansion

- Princess Mode now presents individualized reflection questions with three discussion choices and explanatory feedback. The questions are open-ended by design: children are invited to explain their thinking rather than being marked wrong for a reasonable opinion.
- Optional 30/60/90-second charades timer with pause/reset; expiry does not skip a challenge.
- Family Team Mode supports 2–4 teams, rotating turns and saved scores.
- Up to four local player profiles keep Classic and Princess progress separate.
- Parent Challenge Editor adds, edits and deletes custom Classic Mode challenges; custom challenge data is included in V50 backup export/import.
- Drawing Gallery uses IndexedDB, migrates existing localStorage drawings, supports larger collections, titles, dates, search and sorting, and retains a localStorage fallback.
- Five-region Kingdom Adventure Map unlocks from current profile/mode completion.
- Printable achievement certificates use the browser Print dialog (choose Save as PDF to export a PDF).
- Accessibility settings include text scaling, high contrast, reduced motion and adjustable speech speed.
- Added browser smoke tests and release integrity checks (static release suite executed; browser smoke runner supplied for an environment with browser access).

## Preserved

- 600 Classic and 150 Princess base challenges.
- All 50 Princess portraits, Princess Album and unlock rules.
- Drawing canvas, stamps, gallery previews, music, Romanian/English UI, progress backup and offline PWA shell.
- Existing V49 progress is retained and imported into the default local player profile on first V50 launch.

## V51 — 2026-11-22
- Added delete-selected-player control with confirmation; the final remaining player cannot be deleted. Deleting a player removes that profile's Classic and Princess progress snapshots.
- Added a persistent active-player label on the gameplay screen.
- Kept all existing princess artwork references intact; princess image files are intentionally omitted from this update ZIP because they are already present in the V50 installation.
