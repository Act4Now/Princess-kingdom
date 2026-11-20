PRINCESS KINGDOM — PWA pentru GitHub Pages

Fișiere:
- index.html — aplicația completă, cu 600 de provocări și designul ilustrat
- manifest.webmanifest — nume, pictograme și setări de instalare
- sw.js — cache pentru funcționare offline după prima încărcare
- icon-192.png și icon-512.png — pictograme PWA

PUBLICARE PE GITHUB PAGES
1. Creează un repository Public (de exemplu princess-kingdom).
2. Încarcă toate fișierele de mai sus direct în rădăcina repository-ului.
3. Commit changes.
4. Deschide Settings → Pages.
5. La Build and deployment alege Deploy from a branch.
6. Branch: main; Folder: /(root); Save.
7. După publicare, deschide URL-ul HTTPS primit de GitHub Pages.
8. Pe Android, în Chrome: ⋮ → Install app (sau Add to Home screen).

IMPORTANT:
- Nu încărca ZIP-ul ca atare în repository; dezarhivează-l și încarcă fișierele.
- Service worker și instalarea PWA funcționează pe HTTPS (GitHub Pages oferă HTTPS).
- Modificările ulterioare devin disponibile după redeploy; cache-ul PWA se actualizează la următoarea activare a versiunii noi.
