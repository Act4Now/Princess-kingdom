# Princess Kingdom — Artwork Credits (V50; artwork carried forward from V49)

## Princess Mode portrait inventory

All 50 Princess Mode subjects have an explicit image path stored on each challenge record. The same portrait is reused for that subject's Drawing, Charades, and Questions challenges.

### Previously supplied assets (15 files)

The following assets were already present in the supplied V48 archive (added in V47). The archive does not include original source URLs, creator names, licenses, or attribution records. Their original provenance and redistribution permissions are therefore **unverified**; confirm these before public or commercial distribution.

- `princess-anna.webp` — supplied in the V48 project archive; original source/license not documented.
- `princess-ariel.webp` — supplied in the V48 project archive; original source/license not documented.
- `princess-aurora.webp` — supplied in the V48 project archive; original source/license not documented.
- `princess-belle.webp` — supplied in the V48 project archive; original source/license not documented.
- `princess-cinderella.webp` — supplied in the V48 project archive; original source/license not documented.
- `princess-elsa.webp` — supplied in the V48 project archive; original source/license not documented.
- `princess-flower-tale.webp` — supplied in the V48 project archive; original source/license not documented.
- `princess-jasmine.webp` — supplied in the V48 project archive; original source/license not documented.
- `princess-merida.webp` — supplied in the V48 project archive; original source/license not documented.
- `princess-moana.webp` — supplied in the V48 project archive; original source/license not documented.
- `princess-mulan.webp` — supplied in the V48 project archive; original source/license not documented.
- `princess-pocahontas.webp` — supplied in the V48 project archive; original source/license not documented.
- `princess-rapunzel.webp` — supplied in the V48 project archive; original source/license not documented.
- `princess-snow-white.webp` — supplied in the V48 project archive; original source/license not documented.
- `princess-tiana.webp` — supplied in the V48 project archive; original source/license not documented.

### New V49 assets (35 files)

Thirty-four portraits were generated as original fantasy-princess artwork for this release using OpenAI image generation, then individually cropped from the retained source sheet `artwork-source-princess-grid.png` (a 5×7 contact sheet) and upscaled for app display. One portrait (`princess-raya.svg`) is an original vector illustration authored for this release. These are not official studio character assets. The app's character names and challenge text remain separate from the artwork.

- `princess-eilonwy.webp` — new V49 artwork; generated/original vector as described above.
- `princess-elena-of-avalor.webp` — new V49 artwork; generated/original vector as described above.
- `princess-giselle.webp` — new V49 artwork; generated/original vector as described above.
- `princess-kida.webp` — new V49 artwork; generated/original vector as described above.
- `princess-megara.webp` — new V49 artwork; generated/original vector as described above.
- `princess-rapunzel-from-the-tale.webp` — new V49 artwork; generated/original vector as described above.
- `princess-raya.svg` — new V49 artwork; generated/original vector as described above.
- `princess-sofia.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-brave-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-butterfly-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-crystal-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-dancing-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-dream-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-enchanted-castle-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-forest-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-frog-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-ice-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-moon-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-pearl-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-princess-and-the-pea.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-princess-and-the-unicorn.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-princess-of-hearts.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-rainbow-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-rose-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-sea-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-secret-garden-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-singing-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-snow-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-star-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-storybook-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-sun-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-swan-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-tower-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-the-traveling-princess.webp` — new V49 artwork; generated/original vector as described above.
- `princess-vanellope.webp` — new V49 artwork; generated/original vector as described above.

### Fallback artwork

- `princess-fallback.svg` — original generic vector fallback authored for this release. Used only when a portrait asset fails to load or an older record has no explicit image.

## Asset handling

- Every challenge stores its own exact `image` filename; runtime matching by substring in a princess name is not used.
- All 50 subject portraits and the fallback are listed in `sw.js` for offline availability.
- This file records the provenance known from the supplied archive and the V49 creation process. It does not replace a formal license review of previously supplied assets.


## V50 artwork note

V50 adds no new external artwork files. The 50 dedicated Princess Mode portraits, fallback SVG, background scene and PWA icons are carried forward from the supplied V49 archive. The V50 family features use native HTML/CSS/JavaScript controls and do not add third-party image or font dependencies.
