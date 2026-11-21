PRINCESS KINGDOM — PWA V40

Fișiere
- index.html — aplicația și cele 600 de provocări (RO/EN)
- scene.jpg — fundalul ilustrat continuu
- music.mp3 — muzica de fundal (volum mic, pornește după prima atingere)
- sw.js — cache offline (scene.jpg, music.mp3 și restul sunt precache-uite)
- manifest.webmanifest, icon-192.png, icon-512.png — instalare PWA
- version.json / version.txt / CHANGELOG.md — versiune și istoric

Publicare: încarcă toate fișierele în același folder, servit prin HTTPS. Service worker-ul nu rulează de pe file://.
Progresul și provocarea curentă se salvează local (localStorage), iar actualizarea nu îl șterge.
Prima deschidere cu internet descarcă tot jocul; apoi funcționează offline.
