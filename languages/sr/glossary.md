# Glosario serbio (sr, latinica) para la traducción de PES6

Fija los términos que se repiten, para que todas las tandas digan lo mismo. Si un término no está acá, se usan la referencia (fr, es, de, it) y el sentido común del fútbol en Serbia: las palabras de las transmisiones y de la comunidad de PES.

Por qué serbio: lo pidieron en el hilo de PES6 HD Text (Evoweb) Franespe19 y Μητρογκόλ, en **latinica**. Todas las letras (č ć đ š ž) están en la fuente (`letras.py`). El croata se saca después de esta traducción (`glosario/hr.md`).

## Estilo
- **Alfabeto latino (latinica):** č ć đ š ž (Č Ć Đ Š Ž); dž, lj, nj son dos letras. Nada de cirílico.
- **Ekavski:** la variante de Serbia: vreme, poluvreme, pobeda, nerešeno, sledeći, mleko (no vrijeme, pobjeda…).
- **Trato:** formal, con Vi:
  - en las frases, imperativo formal: «Izaberite», «Pritisnite», «Sačuvajte»;
  - en las preguntas de confirmación, infinitivo: «Sačuvati podatke?», «Obrisati igrača?»;
  - en los **botones y entradas de menú**, la forma corta de los programas en serbio: «Sačuvaj», «Učitaj», «Obriši», «Otkaži», «U redu». Los modos y pantallas van con sustantivo («Podešavanja», «Trening»).
- **`%s` y los casos:** el serbio declina los sustantivos (7 casos), y el juego no sabe qué nombre va en el `%s`. **El `%s` siempre va en nominativo**: la frase se arma para que el caso caiga en una palabra fija.
  - Con dos puntos: «Sledeći protivnik: %s».
  - Con un sustantivo antes: «protiv tima %s», «igrač %s», «u sezoni %s».
- **`%d` y el plural:** el sustantivo cambia de forma según el número (1 gol, 2 gola, 5 golova), y el juego no sabe qué número va. **Nunca un sustantivo declinado detrás de `%d`.**
  - El número va al final, con dos puntos: «Golovi: %d», «Oporavak: %d ned.».
  - Si no, con una abreviatura que no se declina: «%d min.», «%d bod.».
- **Género:** el pasado concuerda con el sujeto. Con `%s` de un jugador va el masculino («%s je postigao gol»); con un equipo, «tim %s je pobedio».
- **Mayúsculas:** si el inglés está TODO en mayúsculas, el serbio también («IZBOR TIMA»). `lotes.py verificar` lo controla.
- **Ordinales:** número con punto: «1. poluvreme», «%d. kolo», «2. dres».
- **Puntuación:** «?» y «!» normales; comillas „…“; sin espacio antes de «:», «?» ni «!».
- **No se traducen:** nombres de jugadores, de clubes ni marcas (PES, KONAMI, Kitserver), ni siglas técnicas (ID, MVP, i.LINK, UPnP).
- **Países y competiciones:** se traducen («Nemačka», «Evropsko prvenstvo»).
- **Largo:** el serbio ocupa más que el inglés. Si el texto supera `maxLength`, se abrevia con punto: «Prec. šuta», «Maks. brzina», «Odbr.».
- **Números:** quedan como en el inglés (los `%d`, `%f` no se tocan).

## Modos y menús
| EN | SR |
|---|---|
| Master League | Master liga |
| Exhibition Match / Exhibition | Prijateljska utakmica / Prijateljska |
| League / Cup | Liga / Kup |
| Edit (modo) / Edit (verbo) / Modify | Uređivanje / Uredi / Izmeni |
| Training | Trening |
| Options | Opcije |
| Settings / General Settings | Podešavanja / Opšta podešavanja |
| Gallery | Galerija |
| Network | Mreža |
| Save / Load (botón) | Sačuvaj / Učitaj |
| Saving / Loading (proceso) | Čuvanje… / Učitavanje… |
| Option file | Fajl sa podešavanjima |
| File / Folder | Fajl / Folder |
| Hard disk | Hard disk |
| Data | Podaci |
| Screen | Ekran |
| Mode Select menu | Meni za izbor moda |
| Exit / Quit / Back / Next | Izlaz / Izlaz / Nazad / Dalje |
| Yes / No | Da / Ne |
| On / Off | Uključeno / Isključeno |
| OK / Confirm / Cancel / Delete / Copy | U redu / Potvrdi / Otkaži / Obriši / Kopiraj |
| Close / Clear / Sort / Move | Zatvori / Očisti / Sortiraj / Premesti |
| Default / Normal / Manual | Podrazumevano / Normalno / Ručno |
| Button / Cursor (marca del jugador) / Controller | Taster / Kursor / Kontroler |
| Button Configuration / Controls | Podešavanje tastera / Kontrole |
| COM / Computer | CPU / Računar |
| BGM / Sound Settings | Muzika / Podešavanja zvuka |
| Replay | Snimak |
| Language / Commentary Language | Jezik / Jezik komentara |

## Partido
| EN | SR |
|---|---|
| Football | Fudbal |
| Match / Kick off | Utakmica / Početni udarac (como entrada de menú: «Počni») |
| Home / Away (etiqueta corta) | Domaćin / Gost |
| HOME / AWAY (marcador) | DOMAĆIN / GOST |
| Home team / Away team | Domaći tim / Gostujući tim |
| Free kick / Foul | Slobodan udarac / Faul |
| Corner (Kick) / Penalty (PK) | Korner / Penal (PEN) |
| Penalties (tanda) | Penali |
| Throw in / Goal kick / Offside | Aut / Gol-aut / Ofsajd |
| Yellow card / Red card | Žuti karton / Crveni karton |
| Pass / Short Pass / Long Pass / Through Pass | Pas / Kratak pas / Dugi pas / Prodorni pas |
| Shot, Shoot / Chip shot | Šut / Lob |
| Dribble, Dribbling / Trap | Dribling / Primanje lopte |
| Feint (movimiento) | Finta |
| Cross, Centre / Crossing (habilidad) | Centaršut / Centaršutevi |
| Header | Udarac glavom |
| Formation / Set Formation / Strategy / Tactics | Formacija / Podesi formaciju / Strategija / Taktika |
| Substitution | Izmena |
| 1st half / 2nd half / Extra time | 1. poluvreme / 2. poluvreme / Produžeci |
| 1Ex. / 2Ex. (prórroga, max 5) / EX | P1 / P2 / PRO |
| 1st leg / 2nd leg | Prva utakmica / Revanš |
| Win / Draw / Loss (W/D/L) | Pobeda / Nerešeno / Poraz (P/N/I) |
| GS / GC / GD | DG / PG / GR (dati golovi, primljeni golovi, gol-razlika) |
| Points (tabla) / Pts. | Bodovi / Bod. |
| Ball possession / Pressure | Posed lopte / Presing |
| Goal / Assists | Gol / Asistencije |
| Stadium | Stadion |
| Week | Nedelja (abreviado: ned.) |

## Equipos, jugadores y Liga Master
| EN | SR |
|---|---|
| Player / Team / Club | Igrač / Tim / Klub |
| National Teams / Club Teams | Reprezentacije / Klubovi |
| Strip / 1st Strip / 2nd Strip | Dres / 1. dres / 2. dres |
| Shirt / Shorts / Socks / Boots | Dres / Šorc / Štucne / Kopačke |
| Emblem / Logo / Colour | Grb / Logo / Boja |
| Condition (estado físico, flecha) | Forma |
| Stronger foot / Left / Right | Jača noga / Leva / Desna |
| Age / Height / Weight / Nationality | Godine / Visina / Težina / Nacionalnost |
| Position / Number / No. | Pozicija / Broj / Br. |
| Rank (puesto) / Ranking | Mesto / Rang-lista |
| Injury | Povreda |
| Season / Division 1 / Division 2 | Sezona / 1. liga / 2. liga |
| D1 / D2 · Division %d | L1 / L2 · %d. liga |
| Pre-season match | Pripremna utakmica |
| Transfer / Negotiations / Contract | Transfer / Pregovori / Ugovor |
| Salary / Points (dinero de la ML) | Plata / Poeni |
| Loan / Release / Trade | Pozajmica / Otpust / Razmena |
| Stock (guardar una imagen o un jugador aparte) | Arhiviraj (verbo) / Arhiva |
| Youth | Omladinska škola |
| Created player | Kreirani igrač |
| Manager / Coach | Trener |
| Commentary | Komentar |

## Posiciones
Se dejan las **siglas inglesas** (GK, CB, SB, DMF, CMF, SMF, AMF, WB, WF, SS, CF, CWP…), como las usa la comunidad de PES en Serbia y en Croacia. Así son iguales en las dos traducciones. Los nombres largos sí se traducen: golman, štoper, bek (levi / desni), defanzivni vezni, centralni vezni, bočni vezni, ofanzivni vezni, krilni bek, krilo, polušpic, centarfor, libero.

## Habilidades
| EN | SR | | EN | SR |
|---|---|---|---|---|
| Attack | Napad | | Shot accuracy | Preciznost šuta |
| Defence | Odbrana | | Shot power | Snaga šuta |
| Balance | Ravnoteža | | Shot technique | Tehnika šuta |
| Stamina | Izdržljivost | | Free kick accuracy | Prec. slob. udarca |
| Top speed | Maks. brzina | | Swerve | Falš |
| Acceleration | Ubrzanje | | Heading | Igra glavom |
| Response | Reakcija | | Jump | Skok |
| Agility | Okretnost | | Technique | Tehnika |
| Dribble accuracy | Preciznost driblinga | | Aggression | Agresivnost |
| Dribble speed | Brzina driblinga | | Mentality | Mentalitet |
| Short pass accuracy | Prec. kratkog pasa | | Goal keeping skills | Golmanske veštine |
| Short pass speed | Brzina kratkog pasa | | Teamwork | Timska igra |
| Long pass accuracy | Prec. dugog pasa | | Consistency | Konstantnost |
| Long pass speed | Brzina dugog pasa | | Weak foot accuracy | Prec. slabije noge |
| Injury tolerance | Otpornost na povrede | | Weak foot frequency | Upotreba slabije noge |
| Condition (estadística) | Kondicija | | | |

Habilidades especiales: Long throw → Dugi aut · 1-on-1 stopper → Stručnjak za 1 na 1 · Penalty stopper → Branilac penala.

Abreviaturas de habilidades: ATT NAP · DEF ODB · SPD BRZ · POW SNG · STA IZD · TWK TIM.

## Fijados de antemano (lo que en el ruso, el griego y el turco hubo que unificar después)
- **Modos:** International Challenge → Međunarodni izazov; Challenge (entrenamiento) → Izazov; Challenge Training → Trening izazova; Step-by-step Training → Trening korak po korak.
- **Competiciones:**
  - European Masters Cup → Evropski Masters kup; European Championship → Evropsko prvenstvo;
  - Northern / Southern / Eastern / Western League %s → Severna / Južna / Istočna / Zapadna liga %s;
  - Knock-out (Stage) → Nokaut faza; Group / Group League → Grupa / Grupna faza; Round robin → Liga sistem; Play-off → Plej-of; Qualifiers → Kvalifikacije; 3rd place play-off → Utakmica za 3. mesto;
  - Draw (sorteo) → Žreb; Table → Tabela; Fixtures → Raspored;
  - Semi / Quarter final → Polufinale / Četvrtfinale; Top scorer → Najbolji strelac.
- **Liga Master:** Memorial Match → Oproštajna utakmica; Records room → Soba rekorda; Topics → Vesti; Newcomers → Pridošlice; Off season → Van sezone; Bonus → Bonus; Funds → Budžet.
- **Reglas:** Away goal → Gol u gostima; Golden / Silver goal → Zlatni gol / Srebrni gol.
- **Dificultad:** Beginner / Amateur / Regular / Professional / Top Player / Super Star → Početnik / Amater / Normalno / Profesionalac / Vrhunski igrač / Superzvezda.
- **Tiempo:** Fine / Rainy / Snow → Sunčano / Kišovito / Sneg; Season (tiempo) → Godišnje doba; Day / Night → Dan / Noć.
- **Edición de jugador:** Appearance → Izgled; Costume → Kostim; Commentary name → Ime za komentar; Player Settings → Lična podešavanja; Both feet → Obe noge.
- **Controles:**
  - Dash → Sprint; 1-Touch / Direct pass → Pas iz prve; Direct shot → Šut iz prve;
  - 1-2 pass → Dupli pas; Step over → Makaze; Marseille Roulette → Marsejski rulet; Sliding tackle → Klizeći start;
  - Feed → Upućivanje lopte.
- **Red:** Rating → Rejting; User ID → Korisnički ID; Password → Lozinka; Lobby → Lobi; Room → Soba; Block Chat → Blokiraj ćaskanje; Chat → Ćaskanje.
- **Cámara:** Bird's-eye → Iz ptičje perspektive.
- **«Nice %s!»** → «Lep potez: %s!» (el `%s` puede ser femenino o masculino).
- **Quedan en inglés, como en los idiomas oficiales:** Club House, los textos del menú de idiomas `52:135`–`52:164` (el armador escribe `52:136` y `52:138`), nombres de comentaristas, Konami ID, UPnP y STUN.
- **Fast / Slow (`108:20`, `108:21`):** al revés que el inglés, como en francés, alemán, italiano y español, y como en el griego y el turco (Fast → Sporo). Los otros Fast/Slow (`24:255`, `24:256`) van normales.
- **Letras del ejecutor** (`286:72`, `286:133`–`136`): como en el turco, letras serbias en las ayudas: [DU] tiro libre lejano (dugi), [KR] cercano (kratki), [L] córner izquierdo, [D] córner derecho, [PEN]; se mira en el juego.
- **Mismo texto, misma traducción:** si un texto inglés tiene las mismas traducciones oficiales en todas sus apariciones, lleva una sola traducción (`lotes.py unir` lo hace solo).

## Fijados al unificar la primera pasada (2026-11-21)

Las 8 tandas tradujeron 7 958 textos con 0 errores. `lotes.py unir` unificó 146 grupos de textos repetidos, y a mano se corrigieron 48 textos. Quedaron así:
- **Gramática:** Marseille Roulette → Marsejski rulet («rulet» es masculino; el glosario decía «Marsejska»).
- **Controles:**
  - Gauge (indicador de potencia) → indikator, en todos sus casos;
  - Super cancel → Super poništavanje;
  - Trap → Primanje lopte; Through feint → Propuštanje lopte; Clear → Izbijanje; Drop kick → Izbijanje iz ruku.
- **Táctica:**
  - Strategy Plan A/B → Strateški plan A/B; Counter Attack → Kontranapad; Offside Trap → Ofsajd zamka;
  - Covering / Mark Zone / Man-marking → Pokrivanje / Zonsko čuvanje / Čovek na čoveka.
- **Habilidades especiales:**
  - Playmaking → Organizacija igre; Scoring → Realizacija; Passing → Pasovi; Post player → Igra leđima ka golu;
  - Marking → Čuvanje; D-Line control → Kontrola linije odbrane; Both feet feint → Finta obema nogama.
- **Partido:**
  - Defender → Defanzivac; Own goal → Autogol; Scorer → Strelac; Penalty area → šesnaesterac; Goal box → Golmanski prostor; Touchline → Bočna linija;
  - 1st / 2nd (tiempos, max 4) → 1.PV / 2.PV; Stoppage time → Nadoknada vremena;
  - Rating (nota del partido) → Ocena; en la red, Rejting.
- **Datos:** Formation Data Manager → Upravljanje podacima formacija; Save mode / Delete mode → Režim čuvanja / Režim brisanja; Stock data → arhivirani podaci / Arhiva.
- **Red:**
  - Division → liga (1. liga, Liga 3A); Prohibited Word List → Lista zabranjenih reči;
  - las frases del chat entre jugadores van con «ti», porque es un jugador que le habla a otro.
- **Liga Master:** Points earned → Zarađeni poeni; Transfer In / Out → Dolazak / Odlazak; Funds → Budžet.
- **«Cleared»** (`109:42`, `23:41`): es un desafío de entrenamiento superado (Savladano). El «Despeje» del español es un error de Konami.
- **Letra del modo amistoso** (`43:8`, inglés F) → P.
- **Revisión automática (2026-11-21):**
  - sin cirílico ni formas ijekavski;
  - ningún `%s` declinado ni sustantivo declinado detrás de `%d` (lo que marca son verbos: «%d nije», «%d ili»);
  - comillas „…“.
