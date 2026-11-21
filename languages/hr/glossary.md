# Glosario croata (hr) para la traducción de PES6

El croata se saca **de la traducción serbia** (`salida/sr.json`): cada tanda recibe el inglés, las referencias y el serbio, y adapta el serbio al croata estándar. No es buscar y reemplazar: además de las palabras cambian la variante (ijekavski), algunas construcciones y los países. Todo lo que no está acá sigue `glosario/sr.md` (incluida su sección «Fijados al unificar»): estilo, trato con Vi, `%s` en nominativo, nada declinado detrás de `%d`, mayúsculas, ordinales con punto, posiciones con siglas inglesas.

Pedido del usuario (2026-11-21): «una copia en croata con el cambio de palabras».

## Lo que cambia siempre
- **Ijekavski:** vrijeme, poluvrijeme, pobjeda, neriješeno, sljedeći, mjesto, uvjet, cijena, lijevi, vještine, ozljeda (sr: vreme, pobeda, nerešeno, sledeći, mesto, uslov, cena, levi, veštine, povreda). Ojo con las que no cambian: «pravilo», «sezona».
- **Infinitivo en vez de «da» + presente:** «Želite li spremiti podatke?» (sr: «Da li želite da sačuvate podatke?»); «Možete odabrati…» (sr: «Možete da izaberete…»).
- **Preguntas:** «…li» al lado del verbo («Želite li…», «Je li…»), nunca «Da li…».
- **Futuro:** «spremit ću» / «bit će» (sr: «sačuvaću» / «biće»).
- **Comillas:** „…“, igual que el serbio.
- **Países:** los nombres croatas: Njemačka, Španjolska, Nizozemska, Švicarska, Rumunjska, Grčka, Engleska, Francuska, Italija, Sjedinjene Američke Države…
- **Meses** (si aparecen): siječanj, veljača, ožujak, travanj, svibanj, lipanj, srpanj, kolovoz, rujan, listopad, studeni, prosinac.

## Palabras
| EN | SR | HR |
|---|---|---|
| Football | Fudbal | Nogomet |
| Team (deportivo) | Tim | Momčad (en compuestos: «Momčadska igra»; «tim» solo en la red) |
| Goalkeeper / GK skills | Golman / Golmanske veštine | Vratar / Vratarske vještine |
| Penalty / Penalties (tanda) | Penal / Penali | Jedanaesterac (corto: 11 m) / Izvođenje jedanaesteraca |
| Corner | Korner | Udarac iz kuta (corto: Kut) |
| Offside | Ofsajd | Zaleđe |
| Foul | Faul | Prekršaj |
| Free kick | Slobodan udarac | Slobodni udarac |
| Goal kick | Gol-aut | Udarac s vrata |
| Pass | Pas | Dodavanje (en compuestos: «kratko dodavanje», «prodorno dodavanje») |
| Cross | Centaršut | Ubačaj |
| Substitution | Izmena | Izmjena |
| Save (botón) / Saving | Sačuvaj / Čuvanje | Spremi / Spremanje |
| Cancel / Back / Next | Otkaži / Nazad / Dalje | Odustani / Natrag / Dalje |
| Delete | Obriši | Izbriši |
| Choose / Select | Izaberite | Odaberite |
| Settings / Options | Podešavanja / Opcije | Postavke / Opcije |
| Default | Podrazumevano | Zadano |
| File / Folder / Option file | Fajl / Folder / Fajl sa podešavanjima | Datoteka / Mapa / Datoteka postavki |
| Hard disk | Hard disk | Tvrdi disk |
| Screen | Ekran | Zaslon |
| Computer | Računar | Računalo |
| Button | Taster | Tipka |
| Replay | Snimak | Snimka |
| Week | Nedelja (ned.) | Tjedan (tj.) |
| Training | Trening | Trening |
| Salary / Points (dinero de la ML) | Plata / Poeni | Plaća / Bodovi |
| Loan / Trade | Pozajmica / Razmena | Posudba / Razmjena |
| Injury / Injury tolerance | Povreda / Otpornost na povrede | Ozljeda / Otpornost na ozljede |
| Defence | Odbrana | Obrana |
| Consistency | Konstantnost | Postojanost |
| Teamwork | Timska igra | Momčadska igra |
| Mentality | Mentalitet | Mentalitet |
| Exhibition | Prijateljska utakmica | Prijateljska utakmica |
| Master League | Master liga | Master liga |
| Superstar | Superzvezda | Superzvijezda |
| History / Records | Istorija / Rekordi | Povijest / Rekordi |
| Europe / European | Evropa / Evropski | Europa / Europski |
| General | Opšti | Opći |
| Accuracy | Preciznost | Preciznost |
| Thousand | Hiljada | Tisuća |
| Chat | Ćaskanje | Čavrljanje |
| Password / User ID | Lozinka / Korisnički ID | Lozinka / Korisnički ID |
| Level | Nivo | Razina |
| Fast / Slow | Brzo / Sporo | Brzo / Sporo |

El nombre del idioma en el menú: «Hrvatski»; el título de la pantalla: «Jezik».

## Fijados al unificar la primera pasada (2026-11-21)

Las 8 tandas adaptaron los 7 958 textos desde el serbio con 0 errores. `lotes.py unir` unificó 49 grupos de textos repetidos, y a mano se corrigieron 48 textos más. Quedaron así:
- **Menús:** Menu → izbornik (Glavni izbornik; en las etiquetas de 4–5 letras, «Izb.»); Mode → način (Način spremanja / Način brisanja, izbornik/odabir načina igre).
- **Competiciones:**
  - Group → grupa, grupna faza (igual que el serbio; se descartó «skupina»);
  - Playoff → doigravanje; 2nd leg → uzvrat; Draw (sorteo) → ždrijeb;
  - Round robin → ligaški sustav; Knock-out → nokaut sustav / nokaut faza;
  - Ranking → ljestvica; Table → tablica; Competition → natjecanje.
- **Partido:**
  - PK en etiquetas → 11 m; Penalties (modo, tanda) → jedanaesterci;
  - Foul en etiquetas cortas → Prekr.;
  - Shots (estadística) → udarci; Defender → branič; Second Striker → Polušpica.
- **Controles:** Step over → Škarice; Counter attack → Protunapad; Offside trap → zamka zaleđa; 1-2 pass → dupli pas.
- **Red:** Server → poslužitelj (en la etiqueta de 8 letras `503:60`, «Server»); Lobby → lobi; List → popis; Prohibited Word List → popis zabranjenih riječi.
- **Equipación:** Shorts → hlačice; Captain's armband → kapetanska vrpca.
- **Revisión automática (2026-11-21):**
  - sin cirílico, sin formas ekavski ni palabras solo serbias;
  - lo que marca son genitivos correctos («vremena», «poluvremena») y «s tim» como pronombre.
- **Diferencia con el serbio:** el 40 % de los textos (3 219 de 7 958) quedó igual (nombres, siglas, números y palabras comunes); el resto cambió por la variante, las palabras o la gramática.
