PRINCESS KINGDOM — PWA V29

Fișiere:
- index.html — aplicația completă și cele 600 de provocări
- manifest.webmanifest — configurarea PWA
- sw.js — cache offline
- icon-192.png / icon-512.png — pictograme

Modificări V23:
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

Verificări V23:
- Sintaxă JavaScript: fără erori.
- Parsare CSS: fără erori.
- ID-uri HTML duplicate: niciunul.
- Teste Chromium la 360x800, 390x844, 430x932, 720x1280 și 844x390.
- În toate cele 5 dimensiuni: elementele fixe au rămas în aceleași coordonate când ajutorul a fost deschis; ajutorul a apărut înaintea raportului; fără erori JavaScript și fără secvențe literale \\n.


Versiune: V23
Footer de identificare: „Creat cu magie pentru a fi jucat în familie” + marcaj V23.


Modificări V23:
- Footer redus la o singură linie, cu înălțime compactă.
- Fundalul footer-ului este transparent, fără separator sau umbră, pentru a se îmbina cu fundalul roz al paginii.
- Spațiul inferior suplimentar al secțiunilor dinamice a fost eliminat, astfel încât footer-ul să urmeze direct raportul pe categorii.
- Marcajul de versiune din colțul dreapta-jos este V23.
- Cache offline actualizat la princess-kingdom-v20-compact-footer.


Modificări V23 — actualizări automate:
- Footer-ul identifică versiunea V23.
- Înregistrarea Service Worker folosește updateViaCache: 'none'.
- Aplicația verifică actualizările la pornire, la revenirea în prim-plan și periodic (o dată pe oră).
- Service Worker-ul nou activează imediat versiunea pregătită și elimină cache-urile vechi princess-kingdom-*.
- Pagina principală și manifestul folosesc strategie network-first cu cache: 'no-store', astfel încât browserul să nu servească versiuni HTML vechi din HTTP cache.
- Resursele statice folosesc cache-first pentru performanță și funcționare offline.
- La actualizarea unei aplicații deja controlate de un Service Worker vechi, pagina se reîncarcă o singură dată după preluarea controlului de către versiunea nouă.
- Datele de progres din localStorage nu sunt șterse de actualizare.
- Dacă dispozitivul este offline, jocul folosește ultima versiune salvată local; versiunea nouă necesită conexiune.


Modificări V23 — categorii disponibile fără provocare + actualizare automată:
- Când nu există provocare activă (la pornire și în ecranul de felicitări), toate cele patru butoane de categorie sunt afișate color, fără efectul grayscale și fără conturul portocaliu de selecție.
- Efectele de categorie activă (contur portocaliu pentru categoria provocării și grayscale pentru celelalte) apar numai cât timp există o provocare activă.
- La selectarea unei categorii și generarea provocării, evidențierea se aplică automat categoriei provocării.
- Păstrat mecanismul V23 de actualizare automată: updateViaCache:none, verificare la pornire/revenire în prim-plan/orar, network-first pentru app shell, ștergerea cache-urilor vechi și păstrarea progresului din localStorage.
- Footer-ul identifică versiunea V23.


VERSIUNE V24 — 2026-11-20
- version.json: metadate structurate ale versiunii curente.
- version.txt: identificator simplu, ușor de verificat.
- CHANGELOG.md: istoricul modificărilor.
- garden-extension.jpg: continuare grafică fără întindere verticală.
- Footer-ul citește versiunea din version.json când fișierul este disponibil.
- La actualizarea unei aplicații instalate apare mesajul „Regatul se pregătește!”.


V26 — Pornire offline-first și identitate nouă pentru ecranul de lansare
- Pagina instalată este servită direct din cache; nu așteaptă rețeaua la pornire.
- Verificarea actualizărilor rulează discret în fundal și este omisă când dispozitivul este offline.
- Footer-ul afișează V26 fără să aștepte descărcarea version.json.
- Pictogramele PWA au fost redesenate cu emblema Princess Kingdom și mesajul „Creat cu magie pentru a fi jucat în familie”.
- Fundalul inferior cu dungi neclare a fost înlocuit cu flori și pavaj roz curat.


V29 — Sincronizarea identificatorilor versiunii
- Sursa pentru versiunea afișată în footer este meta[name="application-version"] din index.html.
- version.json și version.txt sunt sincronizate la V29 pentru controlul distribuției.
- Service Worker cache: princess-kingdom-v29-kingdom-wide-next.
- Cheia de sesiune pentru reîncărcarea după actualizare este pk-v28-update-reloaded.
- Păstrează funcționalitățile V26 și progresul local.

V29 — Verificarea provocărilor și excluderea celor completate
- 200 de provocări distincte în fiecare categorie.
- Provocările completate nu mai revin până la apăsarea butonului Joc nou.
- Progresul se păstrează local.

V29 — Provocare nouă la nivelul întregului regat
- Butonul principal „Provocare nouă” alege aleatoriu din toate categoriile, indiferent de categoria selectată anterior.
- Butoanele individuale de categorie continuă să aleagă numai din categoria respectivă.
- Provocările completate rămân excluse până la apăsarea „Joc nou”.
