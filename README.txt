PRINCESS KINGDOM — PWA

Pachetul conține:
- index.html — aplicația și cele 600 de provocări
- manifest.webmanifest — configurarea PWA
- sw.js — cache offline
- icon-192.png și icon-512.png — pictograme
- README.txt — instrucțiuni

Modificări incluse:
- Fundal unic, continuu, cu castel, grădină, trandafiri și pavaj extins până sub progresul categoriilor.
- Modelul cu romburi din zona inferioară a fost înlocuit cu pavajul continuu.
- Ovalul „Ajutor pentru adult” + „Joc nou” folosește designul aprobat: aceeași placă crem, contur auriu, font serif mov, pictogramă și separator central.
- Textul și pictograma „Joc nou” sunt integrate în ilustrație; butonul HTML rămâne zonă interactivă invizibilă pentru accesibilitate și funcționalitate.
- Butoanele de categorii inactive folosesc grayscale direct pe buton; categoria activă rămâne colorată și evidențiată.
- Butonul principal adaptiv păstrează stările „Provocare nouă” și „Am reușit”.
- Progresul pe categorii rămâne transparent, fără carduri decorative suplimentare.
- Layout adaptiv la viewport; derularea verticală este permisă când e necesară.
- Cache Service Worker actualizat la v13.

Instalare:
1. Încarcă toate fișierele în același director pe un hosting HTTPS (de exemplu GitHub Pages).
2. Deschide pagina în browser.
3. Pentru actualizare pe un dispozitiv cu o versiune instalată, închide aplicația complet și redeschide-o după ce hostingul a publicat fișierele noi.

Notă:
- Progresul jocului este salvat local în browser/dispozitiv.
- Service Worker necesită HTTPS sau localhost; nu funcționează la deschiderea directă ca file:// ori content://.
