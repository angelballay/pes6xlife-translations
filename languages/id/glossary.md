# Glosario indonesio (id) para la traducción de PES6

Fija los términos que se repiten, para que todas las tandas digan lo mismo. Si un término no está acá, se usan la referencia (fr, es, de, it) y el sentido común del fútbol en Indonesia: las transmisiones, la prensa deportiva (Bola, detik) y, sobre todo, los términos que **Konami usa en eFootball en indonesio** (konami.com/efootball/id), que es la referencia oficial más cercana.

Por qué indonesio: la comunidad de PES6 en Indonesia sigue muy activa (patches con la liga indonesia y relato en indonesio en 2026). Del menú solo hubo un e_text «versi Indonesia v3.6 BETA» de 2011 que reemplazaba el inglés y nunca se terminó. Se escribe con el alfabeto latino básico: no le falta ninguna letra a la fuente (`letras.py`).

## Cómo es el idioma (lo que importa para traducir PES6)
- **Sin casos, sin género, sin conjugación:** «tim %s», «pemain %s», «3 gol», «10 gol» no cambian. Los `%s` y `%d` van donde haga falta, sin reescribir la frase.
- **El plural no se marca** después de un número («5 pemain», nunca «5 pemain-pemain»).
- **El adjetivo va después del sustantivo:** «Tendangan Bebas» (patada libre), «Umpan Pendek» (pase corto).
- **Afijos verbales** (me-, di-, ber-, -kan, -i): «menyimpan» (guardar), «disimpan» (guardado), «simpan» (forma corta de botón).
- **Más largo que el inglés** (alrededor de un 30 %): en las etiquetas cortas se abrevia con punto.

## Estilo
- **Indonesio estándar** (bahasa baku), con los préstamos que se usan de verdad en el fútbol de Indonesia y en eFootball: «Kick-off», «Offside», «Dribel», «Penalti».
- **Trato:** neutro y cortés, como en eFootball:
  - en las frases, imperativo con la raíz del verbo: «Pilih tim.», «Tekan tombol {k:a}.»; el pronombre es «Anda», siempre con mayúscula;
  - en los **botones y entradas de menú**, la raíz del verbo: «Simpan», «Muat», «Hapus», «Batal», «OK»;
  - las confirmaciones, como pregunta corta: «Simpan data?», «Hapus pemain ini?».
- **Mayúsculas:** los nombres de menús y opciones van con cada palabra principal en mayúscula, como en eFootball («Pengaturan Suara», «Laga Persahabatan»); las frases, normales. Si el inglés está TODO en mayúsculas, el indonesio también («PILIH TIM»).
- **Ordinales:** con «ke-»: «Babak ke-2», «Peringkat ke-%d»; en etiquetas cortas, número con punto: «1.», «2.».
- **Puntuación:** «?» y «!» normales; comillas “ ”; sin espacio antes de «:», «?» ni «!».
- **No se traducen:** nombres de jugadores, de clubes ni marcas (PES, KONAMI, Kitserver), ni siglas técnicas (ID, MVP, i.LINK, UPnP).
- **Países y competiciones:** se traducen («Jerman», «Kejuaraan Eropa»).
- **Largo:** si el texto supera `maxLength`, se abrevia con punto: «Akr. Tembakan», «Kec. Maks.», «Bertahan» → «Brthn.» solo si no entra otra cosa.
- **Números:** quedan como en el inglés (los `%d`, `%f` no se tocan).

## Modos y menús
| EN | ID |
|---|---|
| Master League | Master League |
| Exhibition Match / Exhibition | Laga Persahabatan |
| League / Cup | Liga / Piala |
| Edit (modo) / Edit (botón) / Modify | Edit / Edit / Ubah |
| Training | Latihan |
| Options | Opsi |
| Settings / General Settings | Pengaturan / Pengaturan Umum |
| Gallery | Galeri |
| Network | Jaringan |
| Save / Load (botón) | Simpan / Muat |
| Saving / Loading (proceso) | Menyimpan… / Memuat… |
| Option file | File Opsi |
| File / Folder | File / Folder |
| Hard disk | Hard Disk |
| Data | Data |
| Screen | Layar |
| Mode Select menu | Menu Pilih Mode |
| Exit / Quit / Back / Next | Keluar / Keluar / Kembali / Berikutnya |
| Yes / No | Ya / Tidak |
| On / Off | Aktif / Nonaktif |
| OK / Confirm / Cancel / Delete / Copy | OK / Konfirmasi / Batal / Hapus / Salin |
| Close / Clear / Sort / Move | Tutup / Bersihkan / Urutkan / Pindahkan |
| Default / Normal / Manual | Default / Normal / Manual |
| Button / Cursor (marca del jugador) / Controller | Tombol / Kursor / Kontroler |
| Button Configuration / Controls | Konfigurasi Tombol / Kontrol |
| COM / Computer | CPU / Komputer |
| BGM / Sound Settings | Musik / Pengaturan Suara |
| Replay | Tayangan Ulang |
| Language / Commentary Language | Bahasa / Bahasa Komentar |
| Menu / Main Menu | Menu / Menu Utama |

## Partido
| EN | ID |
|---|---|
| Football | Sepak bola |
| Match / Kick off | Laga (en frases también «pertandingan») / Kick-off |
| Home / Away (etiqueta corta) | Kandang / Tandang |
| HOME / AWAY (marcador) | KANDANG / TANDANG |
| Home team / Away team | Tim Tuan Rumah / Tim Tamu |
| Free kick / Foul | Tendangan Bebas / Pelanggaran |
| Corner (Kick) / Penalty (PK) | Tendangan Sudut / Penalti (PEN) |
| Penalties (tanda) | Adu Penalti |
| Throw in / Goal kick / Offside | Lemparan ke Dalam / Tendangan Gawang / Offside |
| Yellow card / Red card | Kartu Kuning / Kartu Merah |
| Pass / Short Pass / Long Pass / Through Pass | Umpan / Umpan Pendek / Umpan Panjang / Umpan Terobosan |
| Shot, Shoot / Chip shot | Tembakan / Tembakan Cip |
| Dribble, Dribbling / Trap | Dribel / Kontrol Bola |
| Feint (movimiento) | Tipuan |
| Cross, Centre / Crossing (habilidad) | Umpan Silang / Umpan Silang |
| Header | Sundulan |
| Formation / Set Formation / Strategy / Tactics | Formasi / Atur Formasi / Strategi / Taktik |
| Substitution | Pergantian Pemain |
| 1st half / 2nd half / Extra time | Babak Pertama / Babak Kedua / Perpanjangan Waktu |
| 1Ex. / 2Ex. (prórroga, max 5) / EX | P1 / P2 / PW |
| 1st leg / 2nd leg | Leg Pertama / Leg Kedua |
| Win / Draw / Loss (W/D/L) | Menang / Seri / Kalah (M/S/K) |
| GS / GC / GD | GM / GK / SG (gol memasukkan, gol kemasukan, selisih gol) |
| Points (tabla) / Pts. | Poin / Poin |
| Ball possession / Pressure | Penguasaan Bola / Tekanan |
| Goal / Assists | Gol / Assist |
| Stadium | Stadion |
| Week | Minggu (abreviado: mg.) |
| Referee | Wasit |
| Own goal | Gol Bunuh Diri |
| Counter attack | Serangan Balik |
| Save (del arquero) | Penyelamatan |

## Equipos, jugadores y Liga Master
| EN | ID |
|---|---|
| Player / Team / Club | Pemain / Tim / Klub |
| National Teams / Club Teams | Tim Nasional / Klub |
| Strip / 1st Strip / 2nd Strip | Seragam / Seragam 1 / Seragam 2 |
| Shirt / Shorts / Socks / Boots | Kaus / Celana / Kaus Kaki / Sepatu |
| Emblem / Logo / Colour | Lambang / Logo / Warna |
| Condition (estado físico, flecha) | Kondisi |
| Stronger foot / Left / Right | Kaki Terkuat / Kiri / Kanan |
| Age / Height / Weight / Nationality | Usia / Tinggi / Berat / Kebangsaan |
| Position / Number / No. | Posisi / Nomor / No. |
| Rank (puesto) / Ranking | Peringkat / Peringkat |
| Injury | Cedera |
| Season / Division 1 / Division 2 | Musim / Divisi 1 / Divisi 2 |
| D1 / D2 · Division %d | D1 / D2 · Divisi %d |
| Pre-season match | Laga Pramusim |
| Transfer / Negotiations / Contract | Transfer / Negosiasi / Kontrak |
| Salary / Points (dinero de la ML) | Gaji / Poin |
| Loan / Release / Trade | Pinjaman / Lepas / Tukar |
| Stock (guardar una imagen o un jugador aparte) | Simpan (verbo) / Simpanan |
| Youth | Pemain Muda |
| Created player | Pemain Buatan |
| Manager / Coach | Manajer / Pelatih |
| Commentary | Komentar |
| Substitutes / Bench | Cadangan |

## Posiciones
Se dejan las **siglas inglesas** (GK, CB, SB, DMF, CMF, SMF, AMF, WB, WF, SS, CF, CWP…): la comunidad de PES en Indonesia las usa así, y no hay unas siglas indonesias de 3 letras establecidas. Los nombres largos sí se traducen: Kiper, Libero, Bek Tengah, Bek Sayap (Kiri / Kanan), Gelandang Bertahan, Gelandang Tengah, Gelandang Sayap, Gelandang Serang, Bek Sayap Menyerang (wing back), Sayap (winger), Penyerang Bayangan, Penyerang Tengah, Penyerang.

## Habilidades
| EN | ID | | EN | ID |
|---|---|---|---|---|
| Attack | Menyerang | | Shot accuracy | Akurasi Tembakan |
| Defence | Bertahan | | Shot power | Kekuatan Tembakan |
| Balance | Keseimbangan | | Shot technique | Teknik Tembakan |
| Stamina | Stamina | | Free kick accuracy | Akurasi Tend. Bebas |
| Top speed | Kecepatan Maks. | | Swerve | Efek Lengkung |
| Acceleration | Akselerasi | | Heading | Sundulan |
| Response | Reaksi | | Jump | Lompatan |
| Agility | Kelincahan | | Technique | Teknik |
| Dribble accuracy | Akurasi Dribel | | Aggression | Agresivitas |
| Dribble speed | Kecepatan Dribel | | Mentality | Mentalitas |
| Short pass accuracy | Akurasi Umpan Pendek | | Goal keeping skills | Kemampuan Kiper |
| Short pass speed | Kec. Umpan Pendek | | Teamwork | Kerja Sama Tim |
| Long pass accuracy | Akurasi Umpan Panjang | | Consistency | Konsistensi |
| Long pass speed | Kec. Umpan Panjang | | Weak foot accuracy | Akurasi Kaki Lemah |
| Injury tolerance | Ketahanan Cedera | | Weak foot frequency | Frekuensi Kaki Lemah |
| Condition (estadística) | Kondisi Fisik | | | |

Habilidades especiales: Long throw → Lemparan Jauh · 1-on-1 stopper → Spesialis Satu Lawan Satu · Penalty stopper → Penghenti Penalti.

Abreviaturas de habilidades: ATT SRG · DEF BTH · SPD KEC · POW KKT · STA STM · TWK TIM.

## Fijados de antemano (lo que en los idiomas anteriores hubo que unificar después)
- **Modos:** International Challenge → Tantangan Internasional; Challenge (entrenamiento) → Tantangan; Challenge Training → Latihan Tantangan; Step-by-step Training → Latihan Bertahap.
- **Competiciones:**
  - European Masters Cup → Piala Master Eropa; European Championship → Kejuaraan Eropa;
  - Northern / Southern / Eastern / Western League %s → Liga Utara / Selatan / Timur / Barat %s;
  - Knock-out (Stage) → Sistem Gugur (Babak Gugur); Group / Group League → Grup / Fase Grup; Round robin → Sistem Liga; Play-off → Play-off; Qualifiers → Kualifikasi; 3rd place play-off → Perebutan Tempat Ketiga;
  - Draw (sorteo) → Undian; Table → Klasemen; Fixtures → Jadwal;
  - Semi / Quarter final → Semifinal / Perempat Final; Top scorer → Top Skor.
- **Liga Master:** Memorial Match → Laga Perpisahan; Records room → Ruang Rekor; Topics → Berita; Newcomers → Pendatang Baru; Off season → Jeda Musim; Funds → Dana.
- **Reglas:** Away goal → Gol Tandang; Golden / Silver goal → Gol Emas / Gol Perak.
- **Dificultad:** Beginner / Amateur / Regular / Professional / Top Player / Super Star → Pemula / Amatir / Reguler / Profesional / Top Player / Superstar.
- **Tiempo:** Fine / Rainy / Snow → Cerah / Hujan / Salju; Season (tiempo) → Musim; Day / Night → Siang / Malam.
- **Controles (los de eFootball):**
  - Dash → Lari; Dash dribble → Dribel Sprint; 1-Touch / Direct pass → Umpan Satu Sentuhan; Direct shot → Tembakan Satu Sentuhan;
  - 1-2 pass → Umpan 1-2; Step over → Step Over; Marseille Roulette → Marseille Turn; Sliding tackle → Sleding Tekel; Tackle → Tekel;
  - Controlled shot → Tembakan Terkontrol; Gauge (barra de potencia) → Pengukur Kekuatan; Quick Restart → Mulai Ulang Cepat;
  - Set Piece → Bola Mati; Feed → Umpan.
- **Red:** Rating → Rating; User ID → ID Pengguna; Password → Kata Sandi; Lobby → Lobi; Room → Ruang; Server → Server; Prohibited Word List → Daftar Kata Terlarang; Chat → Obrolan. Las frases del chat entre jugadores van informales, como se hablan los jugadores.
- **«Cleared»** (`109:42`, `23:41`, `109:38`): desafío superado (Selesai). El «Despeje» del español es un error de Konami.
- **Cámara:** Bird's-eye → Pandangan Atas.
- **«Nice %s!»** → «%s yang bagus!».
- **Quedan en inglés, como en los idiomas oficiales:** Club House, los textos del menú de idiomas `52:135`–`52:138` y `52:164` (el armador escribe `52:136` y `52:138`), nombres de comentaristas, Konami ID, UPnP y STUN.
- **Fast / Slow (`108:20`, `108:21`):** al revés que el inglés, como en francés, alemán, italiano y español y en los otros idiomas nuestros (Fast → Lambat). Los otros Fast/Slow (`24:255`, `24:256`) van normales.
- **Letras del ejecutor** (`286:72`, `286:133`–`136`): [J] tiro libre lejano (jauh), [D] cercano (dekat), [KI] córner izquierdo, [KA] córner derecho, [PEN]; se mira en el juego.
- **Mismo texto, misma traducción:** si un texto inglés tiene las mismas traducciones oficiales en todas sus apariciones, lleva una sola traducción (`lotes.py unir` lo hace solo).

## Fijados al unificar la primera pasada (2026-11-21)

Las 8 tandas tradujeron 7 958 textos con 0 errores. `lotes.py unir` unificó 116 grupos de textos repetidos, y a mano se corrigieron 118 textos más (`unificar_id.py`, que se frena si un reemplazo no aplica). Quedaron así:
- **Etiquetas cortas de tablas:**
  - Rank (puesto) → Pos. y Rk → Pos (las tablas de Indonesia dicen «Pos»); con lugar, Peringkat;
  - Foul / Fouls → Faul (también en el tutorial); en las frases, pelanggaran;
  - 1st / 2nd (mitades, junto a 1Ex. / 2Ex. = P1 / P2) → B1 / B2; 1st leg / 2nd leg en tablas → Leg 1 / Leg 2;
  - Home / Away team con max 9 → Kandang / Tandang; con lugar, Tim Tuan Rumah / Tim Tamu;
  - Own goal con max 8 → Bunuh Diri; con lugar, Gol Bunuh Diri;
  - Shots on goal / on target → Tepat Sasaran; Av Goals Scored / conceded → Rerata Gol / Rerata Kebobolan;
  - Cleared (éxitos, es «Exitos») → Sukses; los desafíos superados siguen en Selesai.
- **Botones:** No → Tidak (nunca «Tdk.»); On / Off con max 3–4 → On / Off, como el español y el francés; con lugar, Aktif / Nonaktif; Next con max 7–9 → Lanjut.
- **Datos:** Edited → Hasil Edit (una sola forma: nada de «Diedit» ni «editan» como adjetivo); Edited data manager → Pengelola Data Edit; Game data → Data Permainan; Game Level → Level Permainan; games (partidos jugados) → laga; Registration code → Kode Pendaftaran; Reset prevention → Fitur Pencegah Reset; Fuzzy search → Pencarian Fleksibel.
- **Competiciones:** First / Second round → Babak Pertama / Kedua; Eligible Teams → Tim Peserta; Fixture (jornada) → Pekan; Final Eight / Four, Best 16 → 8 Besar / 4 Besar / 16 Besar.
- **Controles y jugadas:** Clear (despeje) → Sapuan; Super cancel → Super Cancel; Drop kick → Drop Kick; Through feint → Tipuan Membiarkan Bola; Kicker 2 kicks → Penendang 2 Menendang.
- **Habilidades y táctica:** Playmaking → Pengatur Serangan (Pengatur Srg.); Line positioning → Penempatan Lini; Outside → Luar Kaki; Both feet → Dua Kaki; Marking (habilidad) → Penjagaan; Mark Settings → Atur Penjagaan; Man-marking / Mark Zone → Kawal Individu / Kawal Zona.
- **Las ayudas citan la etiqueta tal cual:** [Tim Peserta], [Pemain Rahasia/Klasik], [Fitur Pencegah Reset], [Serang Otomatis]. Lo que queda distinto son etiquetas abreviadas que la ayuda escribe enteras («Srg. Tengah» → [Serangan Tengah]).
- **Revisión automática (2026-11-21):** «boleh» y «perlawanan» son indonesio estándar (el script los marcaba como malayo); «Anda» siempre con mayúscula; comillas “ ”; 0 letras faltantes en la fuente de HD Text.
