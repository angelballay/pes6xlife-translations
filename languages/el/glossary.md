# Glosario griego (el) para la traducción de PES6

Fija los términos que se repiten, para que todas las tandas digan lo mismo. Si un término no está acá, se usan la referencia (fr, es, de, it) y el sentido común del fútbol en griego.

## Estilo
- **Griego moderno monotónico:** tonos y diéresis donde corresponde (ά έ ή ί ό ύ ώ ϊ ϋ ΐ ΰ) y **ς** al final de palabra. Nada de politónico.
- **Trato:** formal, en plural: «Επιλέξτε…», «Πατήστε…», «Αποθηκεύστε…», «σας».
- **Etiquetas de menú y botones:** cortas, con sustantivo: «Αποθήκευση», «Φόρτωση», «Διαγραφή», «Έξοδος».
- **Mayúsculas:** si el inglés está TODO en mayúsculas, el griego también, y **sin tonos** («ΕΠΙΛΟΓΗ ΟΜΑΔΑΣ», «ΗΜΙΧΡΟΝΟ»), como manda la ortografía griega. La diéresis se conserva («ΕΥΡΩΠΑΪΚΟ»), pero un diptongo con tono no la lleva («παίκτης» → «ΠΑΙΚΤΗΣ»). En mayúscula inicial normal, el tono va («Έξοδος», «Άμυνα»).
- **Puntuación:**
  - la pregunta va con **`;` ASCII** («Αποθήκευση δεδομένων;»), nunca U+037E;
  - **sin** «·» (ano teleia, U+0387 o U+00B7): se usa coma o punto;
  - comillas «»;
  - sin keraia (U+0374): los ordinales van con número («1η Κατηγορία», «2ος αγώνας»).
- **No se traducen:** nombres de jugadores, de clubes ni marcas (PES, KONAMI, Kitserver), ni siglas técnicas (ID, MVP, i.LINK). «Master League» tampoco (ver abajo).
- **Países y competiciones:** se traducen («Γερμανία», «Ευρωπαϊκό Πρωτάθλημα»).
- **Largo:** el griego ocupa más que el inglés. Si el texto supera `maxLength`, se abrevia con punto, cortando después de consonante y antes de vocal: «Ακρίβ. ντρίμπλας», «Ταχ. πάσας», «Επιθ.».
- **Números:** quedan como en el inglés (los `%d`, `%f` no se tocan).

## Modos y menús
| EN | EL |
|---|---|
| Master League | Master League (nombre propio, en latín) |
| Exhibition Match / Exhibition | Φιλικός αγώνας / Φιλικό |
| League / Cup | Πρωτάθλημα / Κύπελλο |
| Edit (modo y verbo) / Modify | Επεξεργασία / Τροποποίηση |
| Training | Προπόνηση |
| Options | Επιλογές |
| Settings / General Settings | Ρυθμίσεις / Γενικές ρυθμίσεις |
| Gallery | Γκαλερί |
| Network | Δίκτυο |
| Save / Load | Αποθήκευση / Φόρτωση |
| Option file | Αρχείο ρυθμίσεων |
| Folder | Φάκελος |
| Hard disk | Σκληρός δίσκος |
| Data | Δεδομένα |
| Mode Select menu | Μενού λειτουργιών («Στο μενού λειτουργιών») |
| Exit / Quit / Back / Next | Έξοδος / Έξοδος / Πίσω / Επόμενο |
| Yes / No | Ναι / Όχι |
| On / Off | Ενεργό / Ανενεργό; con `max ≤ 4`: Ναι / Όχι |
| Confirm / Cancel / Delete / Copy | Επιβεβαίωση / Ακύρωση / Διαγραφή / Αντιγραφή |
| Close / Clear / Sort / Move | Κλείσιμο / Εκκαθάριση / Ταξινόμηση / Μετακίνηση |
| Default / Normal / Manual | Προεπιλογή / Κανονικό / Χειροκίνητο |
| Button / Cursor (marca del jugador) / Controller | Κουμπί / Δείκτης / Χειριστήριο |
| Button Configuration / Controls | Ρύθμιση κουμπιών / Χειρισμός |
| COM | Η/Υ |
| BGM / Sound Settings | Μουσική / Ρυθμίσεις ήχου |
| Replay | Επανάληψη |
| Language / Commentary Language | Γλώσσα / Γλώσσα περιγραφής |

## Partido
| EN | EL |
|---|---|
| Match / Kick off | Αγώνας / Έναρξη |
| Home / Away (etiqueta corta) | Εντός / Εκτός |
| HOME / AWAY (marcador) | ΕΝΤΟΣ / ΕΚΤΟΣ |
| Home team / Away team | Γηπεδούχος / Φιλοξενούμενος |
| Free kick (la jugada) / Foul | Ελεύθερο / Φάουλ |
| Free kick accuracy / Free kick shooting (habilidad, ejecución) | Ακρίβεια φάουλ / Εκτέλεση φάουλ |
| Corner (Kick) / Penalty (PK) | Κόρνερ / Πέναλτι (ΠΕΝ) |
| Penalties (tanda) | Πέναλτι; «Διαδικασία πέναλτι» si entra |
| Throw in / Goal kick / Offside | Πλάγιο άουτ / Λάκτισμα τέρματος / Οφσάιντ |
| Yellow card / Red card | Κίτρινη κάρτα / Κόκκινη κάρτα |
| Pass / Short Pass / Long Pass / Through Pass | Πάσα / Κοντή πάσα / Μακριά πάσα / Κάθετη πάσα |
| Shot, Shoot / Chip shot | Σουτ / Λόμπα |
| Dribble, Dribbling / Trap | Ντρίμπλα / Κοντρόλ |
| Cross, Centre / Crossing | Σέντρα / Σέντρες |
| Header | Κεφαλιά |
| Formation / Set Formation / Strategy / Tactics | Διάταξη / Ρύθμιση διάταξης / Στρατηγική / Τακτική |
| Substitution | Αλλαγή |
| 1st half / 2nd half / Extra time | 1ο ημίχρονο / 2ο ημίχρονο / Παράταση |
| 1Ex. / 2Ex. (prórroga, max 5) / EX | Π1 / Π2 / ΠΑΡ |
| 1st leg / 2nd leg | 1ος αγώνας / 2ος αγώνας |
| Win / Draw / Loss (W/D/L) | Νίκη / Ισοπαλία / Ήττα (Ν/Ι/Η) |
| GS / GC / GD | ΓΥ / ΓΚ / ΔΓ (γκολ υπέρ, γκολ κατά, διαφορά) |
| Points (tabla) / Pts. | Βαθμοί / Βαθ. |
| Ball possession / Pressure | Κατοχή μπάλας / Πίεση |
| Goal / Assists | Γκολ / Ασίστ |
| Stadium | Γήπεδο |

## Equipos, jugadores y Liga Master
| EN | EL |
|---|---|
| Player / Team / Club | Παίκτης / Ομάδα / Σύλλογος |
| National Teams / Club Teams | Εθνικές ομάδες / Σύλλογοι |
| Strip / 1st Strip / 2nd Strip | Εμφάνιση / 1η εμφάνιση / 2η εμφάνιση |
| Emblem / Logo / Colour | Έμβλημα / Λογότυπο / Χρώμα |
| Condition (estado físico, flecha) | Φόρμα |
| Stronger foot / Left / Right | Δυνατό πόδι / Αριστερό / Δεξί |
| Age / Height / Weight / Nationality | Ηλικία / Ύψος / Βάρος / Εθνικότητα |
| Position / Number / No. | Θέση / Αριθμός / Αρ. |
| Rank / Ranking | Κατάταξη |
| Injury | Τραυματισμός |
| Season / Division 1 / Division 2 | Σεζόν / 1η Κατηγορία / 2η Κατηγορία |
| Pre-season match | Φιλικό προετοιμασίας |
| Transfer / Negotiations / Contract | Μεταγραφή / Διαπραγματεύσεις / Συμβόλαιο |
| Salary / Points (dinero de la ML) | Μισθός / Πόντοι |
| Stock (guardar jugadores aparte) | Αποθήκη |
| Youth | Ακαδημία |
| Created player | Δημιουργημένος παίκτης |
| Commentary | Περιγραφή |

## Posiciones (máximo 3 letras)
Esquema: primera letra Α = αριστερός, Δ = δεξιός, Κ = κεντρικός, Π = πλάγιος; última letra Α = αμυντικός, Μ = μέσος, Ε = επιθετικός.

| EN | EL | | EN | EL |
|---|---|---|---|---|
| GK | ΤΦ | | AMF | ΕΜ |
| CWP | ΛΙΜ | | WB / LWB / RWB | ΑΚ / ΑΑΚ / ΔΑΚ |
| ASW | ΕΛΙ | | FW | ΕΠΙ |
| CB | ΚΑ | | CF | ΚΕ |
| SB / LB / RB | ΠΑ / ΑΑ / ΔΑ | | WF / LWF / RWF | ΕΞ / ΑΕ / ΔΕ |
| DF | ΑΜΥ | | SS | ΣΕ |
| MF | ΜΕΣ | | WG | ΕΞ |
| DMF | ΑΜΜ | | CMF | ΚΜ |
| SMF / LMF / RMF | ΠΜ / ΑΜ / ΔΜ | | | |

## Habilidades
| EN | EL | | EN | EL |
|---|---|---|---|---|
| Attack | Επίθεση | | Shot accuracy | Ακρίβεια σουτ |
| Defence | Άμυνα | | Shot power | Δύναμη σουτ |
| Balance | Ισορροπία | | Shot technique | Τεχνική σουτ |
| Stamina | Αντοχή | | Free kick accuracy | Ακρίβεια φάουλ |
| Top speed | Μέγ. ταχύτητα | | Swerve | Φάλτσο |
| Acceleration | Επιτάχυνση | | Heading | Κεφαλιές |
| Response | Αντίδραση | | Jump | Άλμα |
| Agility | Ευκινησία | | Technique | Τεχνική |
| Dribble accuracy | Ακρίβ. ντρίμπλας | | Aggression | Επιθετικότητα |
| Dribble speed | Ταχ. ντρίμπλας | | Mentality | Νοοτροπία |
| Short pass accuracy | Ακρίβ. κοντής πάσας | | Goal keeping skills | Ικαν. τερματοφύλακα |
| Short pass speed | Ταχ. κοντής πάσας | | Teamwork | Ομαδικότητα |
| Long pass accuracy | Ακρίβ. μακριάς πάσας | | Consistency | Σταθερότητα |
| Long pass speed | Ταχ. μακριάς πάσας | | Weak foot accuracy | Ακρίβ. αδύνατου ποδιού |
| Injury tolerance | Αντοχή σε τραυμ. | | Weak foot frequency | Συχν. αδύνατου ποδιού |

Habilidades especiales: Long throw → Μακρύ πλάγιο · 1-on-1 stopper → Απόκρουση 1 με 1 · Penalty stopper → Απόκρουση πέναλτι.

Abreviaturas de habilidades: ATT ΕΠΙ · DEF ΑΜΥ · SPD ΤΑΧ · POW ΔΥΝ · STA ΑΝΤ · TWK ΟΜΑ.

## Fijados de antemano (lo que en el ruso hubo que unificar después)
- **Modos:** International Challenge → Διεθνής Πρόκληση; Challenge (entrenamiento) → Πρόκληση.
- **Competiciones:** European Masters Cup → Ευρωπαϊκό Κύπελλο Μάστερς; European Championship → Ευρωπαϊκό Πρωτάθλημα; Northern / Southern / Eastern / Western League %s → Βόρειο / Νότιο / Ανατολικό / Δυτικό Πρωτάθλημα %s.
- **Liga Master:** Memorial Match → Αποχαιρετιστήριος αγώνας; Records room → Αίθουσα ρεκόρ; Topics → Νέα; Loan / Release / Trade → Δανεισμός / Αποδέσμευση / Ανταλλαγή.
- **Reglas:** Away goal → Γκολ εκτός έδρας (AG → ΓΕΕ); Golden / Silver goal → Χρυσό γκολ / Ασημένιο γκολ.
- **Dificultad:** Beginner / Amateur / Regular / Professional / Top Player / Super Star → Αρχάριος / Ερασιτέχνης / Κανονικός / Επαγγελματίας / Κορυφαίος / Σούπερ σταρ.
- **Mismo texto, misma traducción:** si un texto inglés tiene las mismas traducciones oficiales en todas sus apariciones, lleva una sola traducción griega (`lotes.py unir` lo hace solo).

## Fijados al unificar la primera pasada (2026-11-20)

Las 8 tandas decidieron por su cuenta varios términos que no estaban en el glosario. `lotes.py unir` unificó 141 grupos de textos repetidos, y a mano se corrigieron 82 textos más. Quedaron así:
- **Edición de jugador y equipación:**
  - Appearance → Εμφάνιση (igual que Strip; el contexto los separa);
  - Shorts → σορτς (no se declina);
  - Costume → Στολή / στολές;
  - Boots → Παπούτσια.
- **Controles:**
  - Dash → Σπριντ; Dash dribble → Ντρίμπλα με σπριντ;
  - 1-Touch / Direct pass → Πάσα με την πρώτη; Direct shot → Σουτ από πρώτη;
  - Feed → Τροφοδότηση;
  - Step over → Ψαλίδι; Through feint → Προσποίηση αφήματος;
  - Lead throw in → Πλάγιο στην κίνηση;
  - Sliding tackle (etiqueta) → Τάκλιν; en las ayudas, γλιστερό τάκλιν;
  - Crossing: la acción es Σέντρα; la habilidad, Σέντρες.
- **Tiro libre:** la jugada y las pruebas de entrenamiento («Free kick - long pass») → Ελεύθερο; la habilidad y la ejecución → φάουλ. Free kick pass → Πάσα από ελεύθερο. Abreviaturas: FK → ΕΛ / Ελεύθ.
- **Táctica:** Strategy Plan A/B → Στρατηγικό πλάνο Α/Β (letras griegas).
- **Entrenamiento:**
  - Challenge Training → Προπόνηση Πρόκλησης;
  - Original dribble challenge → Προσαρμοσμένη πρόκληση ντρίμπλας;
  - Step-by-step Training → Προπόνηση βήμα-βήμα.
- **Competiciones:** Knock-out → νοκ άουτ; Group / Group League → Όμιλος / Φάση ομίλων; Play-off → Μπαράζ; Qualifiers → Προκριματικά; 3rd place play-off → Μικρός τελικός; Allstar → All-Star.
- **Liga Master:** D1 / D2 → Κ1 / Κ2; Division %d → %dη Κατηγορία; Newcomers → Νέες αφίξεις; Off season → εκτός σεζόν.
- **Red:**
  - Group (comunidad) → Όμιλος, igual que en los torneos;
  - Block Chat → Αποκλεισμός συνομιλίας;
  - Personal key → Προσωπικός κωδικός;
  - Owner (sala) → Οικοδεσπότης;
  - Chat (etiqueta de 7 letras) → Chat; en frases, Συνομιλία.
- **Cámara:** Bird's-eye → Από ψηλά.
- **Tablas:** Rank (puesto) → Θέση; Ranking → Κατάταξη; Pt → Β; Pts. → Βαθ.
- **«Nice %s!»** → «Μπράβο: %s!»: el `%s` puede ser femenino (πάσα) o neutro (σουτ).
- **Gramática:** «την ντρίμπλα», no «τη ντρίμπλα» (la ν se conserva ante ντ).
- **Quedan en inglés, como en los idiomas oficiales:** Club House, los textos del menú de idiomas `52:135`–`52:164` (el armador escribe `52:136` y `52:138`), nombres de comentaristas, Konami ID, UPnP y STUN.
- **Fast / Slow (`108:20`, `108:21`):** francés, alemán, italiano y español los tienen al revés que el inglés; el polaco coincide con el inglés. Se siguió a los cuatro (Fast → Αργό), porque el polaco parece traducido del inglés. Hay que mirarlo en el juego.
- **Revisión automática (2026-11-20):** sin tuteo, sin «ς» en medio de palabra, mayúsculas sin tonos, y toda palabra polisílaba con su tono (las que no lo llevan, como «πιο», «μιας», «ποιοι» y «γεια», se leen en una sílaba).
- **«Cleared»** (`109:42`, `23:41`, 2026-11-21): es un desafío de entrenamiento superado (Ολοκλ., como `109:38`). La primera pasada siguió el «Despeje» del español, que es un error de Konami; corregido y `el_text.afs` rearmado.
