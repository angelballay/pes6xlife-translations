# Glosario turco (tr) para la traducción de PES6

Fija los términos que se repiten, para que todas las tandas digan lo mismo. Si un término no está acá, se usan la referencia (fr, es, de, it) y el sentido común del fútbol en turco: las palabras que usan en Turquía la transmisión de los partidos y la comunidad de PES.

Por qué turco: lo pidió NIGHTFOX en el hilo de PES6 HD Text (Evoweb), y la comunidad turca de PES6 sigue activa. Todas las letras turcas están en la fuente (`letras.py`).

## Estilo
- **Letras turcas:** ç ğ ı İ ö ş ü (y Ç Ğ Ö Ş Ü). El circunflejo (â î û) solo donde la ortografía lo pide para distinguir («hâlâ», «kâr»); si no, sin él.
- **La i con punto y la i sin punto son letras distintas:** i ↔ İ, ı ↔ I. En mayúsculas, «i» pasa a «İ» y «ı» a «I»: «Çıkış» → «ÇIKIŞ», «Lig» → «LİG», «Bilgi» → «BİLGİ». Nunca se escribe «I» por «İ».
- **Trato:** formal, con siz:
  - en las frases, imperativo formal: «Seçin», «Basın», «Kaydedin», «Bekleyin»;
  - en las preguntas de confirmación, pasiva con «-sın mı?»: «Veriler kaydedilsin mi?», «Oyuncu silinsin mi?»;
  - en los **botones y entradas de menú**, la raíz del verbo, como en los programas en turco: «Kaydet», «Yükle», «Sil», «Kopyala», «İptal», «Tamam». Los nombres de modos y pantallas van con sustantivo («Ayarlar», «Antrenman»).
- **Mayúsculas:** si el inglés está TODO en mayúsculas, el turco también, con la regla de la i de arriba. `lotes.py verificar` lo controla.
- **Sufijos y `%s`/`%d`:** el sufijo turco cambia según la palabra (armonía vocálica: «Barcelona'yı», «Milan'ı», «5'te», «6'da»), y el juego no sabe qué va en el `%s`. **Nunca se pega un sufijo de caso a `%s` o `%d`.** Se reescribe la frase para que el sufijo vaya en una palabra fija:
  - con dos puntos: «Sıradaki rakip: %s»;
  - con un sustantivo detrás: «%s takımına karşı», «%s adlı oyuncu», «%s sezonunda», «%d dakikada» → mejor «Dakika: %d»;
  - el genitivo y el posesivo, igual: «%s takımının oyuncuları».
  - Con nombres propios o números escritos (no `%s`), el sufijo va con apóstrofo: «PES 6'da», «2006'da».
- **Ordinales:** número con punto: «1. yarı», «2. forma», «%d. hafta», «%d. Lig».
- **Porcentaje:** en turco el signo va antes del número: «%%50», «%%%d» (el verificador acepta que `%%` y `%d` cambien de orden).
- **Puntuación:** «?» y «!» normales; comillas “ ” (no «»); sin espacio antes de «:», «?» ni «!».
- **No se traducen:** nombres de jugadores, de clubes ni marcas (PES, KONAMI, Kitserver), ni siglas técnicas (ID, MVP, i.LINK, UPnP).
- **Países y competiciones:** se traducen («Almanya», «Avrupa Şampiyonası»).
- **Largo:** el turco ocupa más que el inglés. Si el texto supera `maxLength`, se abrevia con punto: «S. vuruş isabeti», «Maks. hız», «Dep.».
- **Números:** quedan como en el inglés (los `%d`, `%f` no se tocan).

## Modos y menús
| EN | TR |
|---|---|
| Master League | Master Lig |
| Exhibition Match / Exhibition | Hazırlık maçı / Hazırlık |
| League / Cup | Lig / Kupa |
| Edit (modo) / Edit (verbo) / Modify | Düzenleme / Düzenle / Değiştir |
| Training | Antrenman |
| Options | Seçenekler |
| Settings / General Settings | Ayarlar / Genel ayarlar |
| Gallery | Galeri |
| Network | Ağ |
| Save / Load (botón) | Kaydet / Yükle |
| Saving / Loading (proceso) | Kaydediliyor / Yükleniyor |
| Option file | Ayar dosyası |
| Folder | Klasör |
| Hard disk | Sabit disk |
| Data | Veri |
| Mode Select menu | Mod seçim menüsü |
| Exit / Quit / Back / Next | Çıkış / Çıkış / Geri / İleri |
| Yes / No | Evet / Hayır |
| On / Off | Açık / Kapalı |
| OK / Confirm / Cancel / Delete / Copy | Tamam / Onayla / İptal / Sil / Kopyala |
| Close / Clear / Sort / Move | Kapat / Temizle / Sırala / Taşı |
| Default / Normal / Manual | Varsayılan / Normal / Manuel |
| Button / Cursor (marca del jugador) / Controller | Tuş / İmleç / Kontrolcü |
| Button Configuration / Controls | Tuş ayarları / Kontroller |
| COM | CPU (en frases: «bilgisayar») |
| BGM / Sound Settings | Müzik / Ses ayarları |
| Replay | Tekrar |
| Language / Commentary Language | Dil / Spiker dili |

## Partido
| EN | TR |
|---|---|
| Match / Kick off | Maç / Başlama vuruşu (como entrada de menú: «Başla») |
| Home / Away (etiqueta corta) | Ev / Dep. |
| HOME / AWAY (marcador) | EV / DEP |
| Home team / Away team | Ev sahibi / Deplasman takımı |
| Free kick / Foul | Serbest vuruş / Faul |
| Free kick accuracy | Serbest vuruş isabeti (corto: S. vuruş isabeti) |
| Corner (Kick) / Penalty (PK) | Korner / Penaltı (PEN) |
| Penalties (tanda) | Penaltı atışları |
| Throw in / Goal kick / Offside | Taç atışı / Kale vuruşu / Ofsayt |
| Yellow card / Red card | Sarı kart / Kırmızı kart |
| Pass / Short Pass / Long Pass / Through Pass | Pas / Kısa pas / Uzun pas / Ara pası |
| Shot, Shoot / Chip shot | Şut / Aşırtma |
| Dribble, Dribbling / Trap | Top sürme / Top kontrolü |
| Feint (movimiento) | Çalım |
| Cross, Centre / Crossing (habilidad) | Orta / Orta açma |
| Header | Kafa vuruşu |
| Formation / Set Formation / Strategy / Tactics | Diziliş / Diziliş ayarla / Strateji / Taktik |
| Substitution | Oyuncu değişikliği (corto: Değişiklik) |
| 1st half / 2nd half / Extra time | İlk yarı / İkinci yarı / Uzatma |
| 1Ex. / 2Ex. (prórroga, max 5) / EX | U1 / U2 / UZT |
| 1st leg / 2nd leg | İlk maç / Rövanş |
| Win / Draw / Loss (W/D/L) | Galibiyet / Beraberlik / Mağlubiyet (G/B/M) |
| GS / GC / GD | AG / YG / AV (atılan gol, yenen gol, averaj) |
| Points (tabla) / Pts. | Puan / P |
| Ball possession / Pressure | Topa sahip olma / Pres |
| Goal / Assists | Gol / Asist |
| Stadium | Stadyum |

## Equipos, jugadores y Liga Master
| EN | TR |
|---|---|
| Player / Team / Club | Oyuncu / Takım / Kulüp |
| National Teams / Club Teams | Milli takımlar / Kulüp takımları |
| Strip / 1st Strip / 2nd Strip | Forma / 1. forma / 2. forma |
| Emblem / Logo / Colour | Arma / Logo / Renk |
| Condition (estado físico, flecha) | Form |
| Stronger foot / Left / Right | Güçlü ayak / Sol / Sağ |
| Age / Height / Weight / Nationality | Yaş / Boy / Kilo / Uyruk |
| Position / Number / No. | Mevki / Numara / No. |
| Rank (puesto) / Ranking | Sıra / Sıralama |
| Injury / Injury tolerance | Sakatlık / Sakatlık direnci |
| Season / Division 1 / Division 2 | Sezon / 1. Lig / 2. Lig |
| D1 / D2 · Division %d | L1 / L2 · %d. Lig |
| Pre-season match | Sezon öncesi maçı |
| Transfer / Negotiations / Contract | Transfer / Görüşmeler / Sözleşme |
| Salary / Points (dinero de la ML) | Maaş / Puan |
| Stock (guardar una imagen o un jugador aparte) | Depola (verbo) / Depo |
| Youth | Altyapı |
| Created player | Oluşturulan oyuncu |
| Commentary | Maç anlatımı |

## Posiciones (máximo 3 letras)
Esquema: SL = sol, SĞ = sağ; K = kanat bek (lateral que sube), A = açık (extremo); OS = orta saha. La «Ğ» cuenta como una letra.

| EN | TR | | EN | TR |
|---|---|---|---|---|
| GK | KL | | AMF | OOS |
| CWP / ASW | LİB | | WB / LWB / RWB | KB / SLK / SĞK |
| CB | STP | | FW | FOR |
| SB / LB / RB | BEK / SLB / SĞB | | CF | SNT |
| DF | DEF | | WF / LWF / RWF | AÇK / SLA / SĞA |
| MF | OS | | WG | AÇK |
| DMF | DOS | | SS | GF |
| CMF | MOS | | SMF / LMF / RMF | KOS / SLO / SĞO |

CWP y ASW van los dos como LİB, igual que en el español oficial (LIB / LIB).

## Habilidades
| EN | TR | | EN | TR |
|---|---|---|---|---|
| Attack | Hücum | | Shot accuracy | Şut isabeti |
| Defence | Savunma | | Shot power | Şut gücü |
| Balance | Denge | | Shot technique | Şut tekniği |
| Stamina | Dayanıklılık | | Free kick accuracy | S. vuruş isabeti |
| Top speed | Maks. hız | | Swerve | Falso |
| Acceleration | İvmelenme | | Heading | Kafa vuruşu |
| Response | Tepki | | Jump | Sıçrama |
| Agility | Çeviklik | | Technique | Teknik |
| Dribble accuracy | Top sürme isabeti | | Aggression | Agresiflik |
| Dribble speed | Top sürme hızı | | Mentality | Mentalite |
| Short pass accuracy | Kısa pas isabeti | | Goal keeping skills | Kalecilik |
| Short pass speed | Kısa pas hızı | | Teamwork | Takım oyunu |
| Long pass accuracy | Uzun pas isabeti | | Consistency | İstikrar |
| Long pass speed | Uzun pas hızı | | Weak foot accuracy | Zayıf ayak isabeti |
| Injury tolerance | Sakatlık direnci | | Weak foot frequency | Zayıf ayak kullanımı |

Habilidades especiales: Long throw → Uzun taç · 1-on-1 stopper → Bire bir uzmanı · Penalty stopper → Penaltı uzmanı.

Abreviaturas de habilidades: ATT HÜC · DEF SAV · SPD HIZ · POW GÜÇ · STA DAY · TWK TKM.

## Fijados de antemano (lo que en el ruso y el griego hubo que unificar después)
- **Modos:** International Challenge → Uluslararası Mücadele; Challenge (entrenamiento) → Mücadele; Challenge Training → Mücadele antrenmanı; Step-by-step Training → Adım adım antrenman; Original dribble challenge → Özel top sürme mücadelesi.
- **Competiciones:**
  - European Masters Cup → Avrupa Masters Kupası; European Championship → Avrupa Şampiyonası;
  - Northern / Southern / Eastern / Western League %s → Kuzey / Güney / Doğu / Batı Ligi %s;
  - Knock-out → Eleme; Group / Group League → Grup / Grup aşaması; Play-off → Play-off; Qualifiers → Elemeler; 3rd place play-off → Üçüncülük maçı; Allstar → All-Star.
- **Liga Master:** Memorial Match → Jübile maçı; Records room → Rekorlar odası; Topics → Haberler; Loan / Release / Trade → Kiralık / Serbest bırak / Takas; Newcomers → Yeni gelenler; Off season → Sezon arası.
- **Reglas:** Away goal → Deplasman golü (AG → DG); Golden / Silver goal → Altın gol / Gümüş gol.
- **Dificultad:** Beginner / Amateur / Regular / Professional / Top Player / Super Star → Acemi / Amatör / Normal / Profesyonel / Üst düzey / Süperstar.
- **Edición de jugador:** Appearance → Görünüm (Strip es Forma); Shorts → Şort; Costume → Kıyafet; Boots → Krampon.
- **Controles:**
  - Dash → Depar; Dash dribble → Depar ile top sürme;
  - 1-Touch / Direct pass → Tek dokunuş pas; Direct shot → Gelişine şut;
  - Feed → Topu besleme; Step over → Makas; Through feint → Topu bırakma çalımı;
  - Lead throw in → Koşu yoluna taç;
  - Sliding tackle → Kayarak müdahale.
- **Táctica:** Strategy Plan A/B → Strateji planı A/B.
- **Red:** Group (comunidad) → Grup; Block Chat → Sohbeti engelle; Personal key → Kişisel anahtar; Owner (sala) → Oda sahibi; Chat → Sohbet.
- **Cámara:** Bird's-eye → Kuş bakışı.
- **«Nice %s!»** → «Güzel %s!» (el `%s` es una jugada: «Güzel pas!»).
- **Quedan en inglés, como en los idiomas oficiales:** Club House, los textos del menú de idiomas `52:135`–`52:164` (el armador escribe `52:136` y `52:138`), nombres de comentaristas, Konami ID, UPnP y STUN.
- **Fast / Slow (`108:20`, `108:21`):** francés, alemán, italiano y español los tienen al revés que el inglés; en el griego se siguió a esos cuatro. Acá se hace lo mismo (Fast → Yavaş), para que coincida con el griego.
- **Mismo texto, misma traducción:** si un texto inglés tiene las mismas traducciones oficiales en todas sus apariciones, lleva una sola traducción turca (`lotes.py unir` lo hace solo).

## Fijados al unificar la primera pasada (2026-11-20)

Las 8 tandas tradujeron 7 958 textos con 0 errores. `lotes.py unir` unificó 118 grupos de textos repetidos, y a mano se corrigieron 41 textos más. Quedaron así:
- **Manager** (el del club) → Antrenör; «Menajer» es el representante del jugador. Coach Mode → Antrenör modu.
- **Tiempo:** Fine / Rainy / Snow → Güneşli / Yağmurlu / Karlı («Açık» queda para On). Season (tiempo) → Mevsim; Season (competición) → Sezon. Day / Night → Gündüz / Gece.
- **Equipación:** Socks → Tozluk; Shirt → Forma; Captain's armband → Kaptanlık pazubandı.
- **Competiciones:**
  - Knock-out Stage → Eleme aşaması; Round robin → Lig usulü; Tournament (formato) → Eleme usulü;
  - Draw (sorteo) → Kura; Table → Puan durumu; Fixtures → Fikstür;
  - 1st leg / 2nd leg → İlk maç / Rövanş; Semi / Quarter final → Yarı final / Çeyrek final; Best 16 → Son 16;
  - Top scorer / Most assists → Gol kralı / Asist kralı.
- **Liga Master:** Bonus points → Bonus puan; Champion Bonus → Şampiyonluk primi; Funds → Bütçe (Insufficient funds → Yetersiz bütçe); Balance → Bakiye; My Best Eleven → En iyi 11'im.
- **Red:** Rating → Reyting; User ID → Kullanıcı kimliği; Demonstration phrase → Gösteri ifadesi; Lobby → Lobi; Room → Oda.
- **Jugador:** Commentary name → Anons adı; Player Settings → Kişisel ayarlar; Both feet → Çift ayak (B → Çift / ÇA); Condition (estadística, es «Estabilidad») → Kondisyon.
- **Habilidades especiales:** Covering → Kademe; Line positioning → Hat pozisyonu alma; Penalties → Penaltıcı; Marking → Markaj; Playmaking → Oyun kurma; Post player → Pivot oyuncu.
- **Controles:** 1-2 pass → Verkaç; Marseille Roulette → Marsilya dönüşü; Controlled shot → Plase şut; Quick Restart → Hızlı başlatma; FK (corto) → SV; Penalty kick → Penaltı atışı.
- **Ortografía:** santrafor (TDK). «Oyun verileri» va en minúscula en medio de la frase.
- **Letras del ejecutor** (`286:72`, `286:133`–`136`): las ayudas usan [U] (tiro libre lejano), [Y] (cercano), [SL] y [SĞ] (córners) y [PEN], igual que el griego cambió las suyas. No hay un texto con esas letras: si en pantalla salen en inglés (L, S, R), hay que volver a las letras inglesas en esas ayudas.
- **Revisión automática (2026-11-20):**
  - sin sufijos pegados a `%s`/`%d` (los `%dKB` son unidades);
  - sin tuteo, sin «I» por «İ» (KONAMI queda como marca) y sin comillas «»;
  - en las 93 etiquetas con varias traducciones, la diferencia es de contexto («Close»: Kapat / Yakın; «Goal»: Gol / Kale).
