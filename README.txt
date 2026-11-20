PRINCESS KINGDOM — PWA

Conținut:
- index.html: aplicația completă, cu 600 de provocări și muzica inclusă local
- manifest.webmanifest: configurarea PWA
- sw.js: cache offline și actualizare automată a cache-ului
- icon-192.png / icon-512.png: pictograme PWA

Modificări în această versiune:
- un singur fundal continuu pentru joc și progresul categoriilor; nu se mai afișează imaginea duplicat în #game
- fundalul este extins sub bara de progres; secțiunea de progres este transparentă
- eliminarea butoanelor vechi „Am reușit! Următoarea” și „Altă provocare” din interfață și din artwork
- un singur buton principal adaptiv: „Provocare nouă” / „Am reușit”
- „Ajutor pentru adult” și „Joc nou” împart același oval, cu un singur separator
- măștile categoriilor sunt aliniate la dimensiunile butoanelor ilustrate
- layout adaptiv după dimensiunea viewport-ului; în landscape este permis scroll vertical
- cardurile decorative din progres au fost eliminate; rămân etichetele și barele esențiale
- cod CSS consolidat, fără blocuri duplicate; service worker activ pe origini HTTPS/HTTP

Instalare:
1. Încarcă toate fișierele din arhivă în același director pe un hosting HTTPS (de exemplu GitHub Pages).
2. Deschide adresa aplicației în browser.
3. Folosește „Instalează aplicația” / „Adaugă la ecranul principal”, dacă browserul oferă opțiunea.

Notă:
- Progresul este salvat local în browserul/dispozitivul utilizat.
- Service worker-ul funcționează pe HTTPS sau localhost; nu se activează la deschiderea directă ca file:// sau content://.
