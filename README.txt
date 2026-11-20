PRINCESS KINGDOM — PWA V18

Fișiere:
- index.html — aplicația completă și cele 600 de provocări
- manifest.webmanifest — configurarea PWA
- sw.js — cache offline
- icon-192.png / icon-512.png — pictograme

Modificări V18:
1. Structură separată pentru secțiunile dinamice:
   - Scena ilustrată (#game) rămâne o suprafață fixă, cu raportul original 1152:2120.
   - Butoanele categoriilor, jurnalul, provocarea, butonul principal, Ajutor pentru adult și Joc nou rămân ancorate la coordonatele ilustrației.
   - Ajutorul pentru adult și raportul pe categorii sunt elemente-soră, în afara scenei ilustrate.

2. Flux adaptiv:
   - Ajutorul apare imediat sub butonul „Ajutor pentru adult”.
   - Raportul pe categorii este în flux normal și se deplasează numai cu înălțimea necesară.
   - La închiderea ajutorului, raportul revine la distanța inițială.
   - Nicio poziție a butoanelor sau a elementelor fixe din scenă nu este recalculată în funcție de deschiderea ajutorului.

3. Textul ajutorului:
   - Afișează provocarea, întrebarea sau răspunsul orientativ, în funcție de categorie.
   - Secvențele literale \\n sunt normalizate la rânduri noi.

4. Păstrat:
   - Ilustrația, aspectul butoanelor și logica de selectare automată a categoriei.
   - Toate cele 600 de provocări: 200 Desen, 200 Mimă și 200 Întrebări.

Verificări V18:
- Sintaxă JavaScript: fără erori.
- Parsare CSS: fără erori.
- ID-uri HTML duplicate: niciunul.
- Teste Chromium la 360x800, 390x844, 430x932, 720x1280 și 844x390.
- În toate cele 5 dimensiuni: elementele fixe au rămas în aceleași coordonate când ajutorul a fost deschis; ajutorul a apărut înaintea raportului; fără erori JavaScript și fără secvențe literale \\n.


Versiune: V19
Footer de identificare: „Creat cu magie pentru a fi jucat în familie” + marcaj V19.
