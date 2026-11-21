# Glosario portugués de Brasil (pt-br) para la traducción de PES6

Fija los términos que se repiten, para que todas las tandas digan lo mismo. Si un término no está acá, se usan la referencia (fr, es, de, it) y el sentido común del fútbol en Brasil: las palabras de las transmisiones (Globo, SporTV) y de la comunidad brasileña de PES, que es la más grande del juego en PC.

Por qué portugués de Brasil: es la comunidad más grande de PES6 PC, y sus traducciones viejas reemplazaban el inglés (`e_text`). Esta es la séptima opción del menú y no pisa nada. Todas las letras (á â ã à ç é ê í ó ô õ ú ü, ª º) están en la fuente (`letras.py`).

## Estilo
- **Portugués de Brasil**, no de Portugal: «time», «goleiro», «arquivo», «tela», «salvar», «você» (pt-PT: «equipa», «guarda-redes», «ficheiro», «ecrã», «gravar», «tu»).
- **Trato:** «você», como en los juegos y programas en Brasil:
  - en las frases, imperativo con «você»: «Selecione», «Pressione», «Salve»;
  - en los **botones y entradas de menú**, infinitivo: «Salvar», «Carregar», «Excluir», «Cancelar», «OK»;
  - las confirmaciones, con «Deseja…?» o infinitivo: «Deseja salvar os dados?», «Excluir o jogador?».
- **`%s` y el género:** el portugués concuerda artículos y adjetivos con el género, y el juego no sabe qué nombre va en el `%s` (o time, a seleção). **Nunca un artículo o una contracción pegados a `%s`** («do %s», «a %s»): se reescribe con dos puntos («Próximo adversário: %s») o con un sustantivo fijo («o time %s», «o jogador %s»).
- **`%d` y el plural:** 1 gol / 2 gols. **Nunca un sustantivo que cambie con el número detrás de `%d`**: el número va al final con dos puntos («Gols: %d», «Recuperação: %d sem.») o con una abreviatura que no cambia («%d min.», «%d pts.»).
- **Mayúsculas:** si el inglés está TODO en mayúsculas, el portugués también, con sus tildes («SELEÇÃO DE TIME»). `lotes.py verificar` lo controla.
- **Ordinales:** con º / ª: «1º tempo», «2ª divisão», «%dº lugar».
- **Puntuación:** «?» y «!» normales; comillas “ ”; sin espacio antes de «:», «?» ni «!».
- **No se traducen:** nombres de jugadores, de clubes ni marcas (PES, KONAMI, Kitserver), ni siglas técnicas (ID, MVP, i.LINK, UPnP). Términos que en Brasil se usan en inglés en PES: Replay, Top Player, Superstar.
- **Países y competiciones:** se traducen («Alemanha», «Campeonato Europeu»).
- **Largo:** el portugués ocupa más que el inglés. Si el texto supera `maxLength`, se abrevia con punto: «Prec. de chute», «Vel. máx.», «Def.».
- **Números:** quedan como en el inglés (los `%d`, `%f` no se tocan).

## Modos y menús
| EN | PT-BR |
|---|---|
| Master League | Liga Master |
| Exhibition Match / Exhibition | Amistoso |
| League / Cup | Liga / Copa |
| Edit (modo) / Edit (botón) / Modify | Editar / Editar / Modificar |
| Training | Treino |
| Options | Opções |
| Settings / General Settings | Configurações / Configurações gerais |
| Gallery | Galeria |
| Network | Rede |
| Save / Load (botón) | Salvar / Carregar |
| Saving / Loading (proceso) | Salvando… / Carregando… |
| Option file | Arquivo de opções |
| File / Folder | Arquivo / Pasta |
| Hard disk | Disco rígido |
| Data | Dados |
| Screen | Tela |
| Mode Select menu | Menu de seleção de modo |
| Exit / Quit / Back / Next | Sair / Sair / Voltar / Avançar |
| Yes / No | Sim / Não |
| On / Off | Ligado / Desligado (con `max ≤ 4`: Sim / Não) |
| OK / Confirm / Cancel / Delete / Copy | OK / Confirmar / Cancelar / Excluir / Copiar |
| Close / Clear / Sort / Move | Fechar / Limpar / Ordenar / Mover |
| Default / Normal / Manual | Padrão / Normal / Manual |
| Button / Cursor (marca del jugador) / Controller | Botão / Cursor / Controle |
| Button Configuration / Controls | Configuração de botões / Controles |
| COM / Computer | CPU / Computador |
| BGM / Sound Settings | Música / Configurações de som |
| Replay | Replay |
| Language / Commentary Language | Idioma / Idioma da narração |
| Menu / Main Menu | Menu / Menu principal |

## Partido
| EN | PT-BR |
|---|---|
| Football | Futebol |
| Match / Kick off | Partida / Pontapé inicial (como entrada de menú: «Começar») |
| Home / Away (etiqueta corta) | Casa / Fora |
| HOME / AWAY (marcador) | CASA / FORA |
| Home team / Away team | Mandante / Visitante |
| Free kick / Foul | Falta (cobrança de falta) / Falta |
| Corner (Kick) / Penalty (PK) | Escanteio / Pênalti (PEN) |
| Penalties (tanda) | Pênaltis (disputa de pênaltis) |
| Throw in / Goal kick / Offside | Lateral / Tiro de meta / Impedimento |
| Yellow card / Red card | Cartão amarelo / Cartão vermelho |
| Pass / Short Pass / Long Pass / Through Pass | Passe / Passe curto / Passe longo / Passe em profundidade |
| Shot, Shoot / Chip shot | Chute / Cavadinha |
| Dribble, Dribbling / Trap | Drible / Domínio |
| Feint (movimiento) | Finta |
| Cross, Centre / Crossing (habilidad) | Cruzamento / Cruzamentos |
| Header | Cabeceio |
| Formation / Set Formation / Strategy / Tactics | Formação / Ajustar formação / Estratégia / Tática |
| Substitution | Substituição |
| 1st half / 2nd half / Extra time | 1º tempo / 2º tempo / Prorrogação |
| 1Ex. / 2Ex. (prórroga, max 5) / EX | 1ºP / 2ºP / PRO |
| 1st leg / 2nd leg | Jogo de ida / Jogo de volta |
| Win / Draw / Loss (W/D/L) | Vitória / Empate / Derrota (V/E/D) |
| GS / GC / GD | GP / GC / SG (gols pró, gols contra, saldo de gols) |
| Points (tabla) / Pts. | Pontos / Pts. |
| Ball possession / Pressure | Posse de bola / Pressão |
| Goal / Assists | Gol / Assistências |
| Stadium | Estádio |
| Week | Semana (abreviado: sem.) |
| Referee | Árbitro |

## Equipos, jugadores y Liga Master
| EN | PT-BR |
|---|---|
| Player / Team / Club | Jogador / Time / Clube |
| National Teams / Club Teams | Seleções / Clubes |
| Strip / 1st Strip / 2nd Strip | Uniforme / Uniforme 1 / Uniforme 2 |
| Shirt / Shorts / Socks / Boots | Camisa / Calção / Meião / Chuteira |
| Emblem / Logo / Colour | Escudo / Logotipo / Cor |
| Condition (estado físico, flecha) | Forma |
| Stronger foot / Left / Right | Pé preferido / Esquerdo / Direito |
| Age / Height / Weight / Nationality | Idade / Altura / Peso / Nacionalidade |
| Position / Number / No. | Posição / Número / Nº |
| Rank (puesto) / Ranking | Posição / Classificação |
| Injury | Lesão |
| Season / Division 1 / Division 2 | Temporada / 1ª divisão / 2ª divisão |
| D1 / D2 · Division %d | D1 / D2 · %dª divisão |
| Pre-season match | Jogo de pré-temporada |
| Transfer / Negotiations / Contract | Transferência / Negociações / Contrato |
| Salary / Points (dinero de la ML) | Salário / Pontos |
| Loan / Release / Trade | Empréstimo / Dispensar / Troca |
| Stock (guardar una imagen o un jugador aparte) | Armazenar (verbo) / Armazenamento |
| Youth | Categorias de base |
| Created player | Jogador criado |
| Manager / Coach | Técnico |
| Commentary | Narração |

## Posiciones (máximo 3 letras)
Las siglas que usa PES en portugués de Brasil:

| EN | PT-BR | | EN | PT-BR |
|---|---|---|---|---|
| GK | GO | | AMF | MAT |
| CWP / ASW | LIB | | WB / LWB / RWB | ALA / ALE / ALD |
| CB | ZAG | | FW | ATA |
| SB / LB / RB | LAT / LE / LD | | CF | CA |
| DF | DEF | | WF / LWF / RWF | PON / PE / PD |
| MF | MEI | | WG | PON |
| DMF | VOL | | SS | SA |
| CMF | MC | | SMF / LMF / RMF | ML / ME / MD |

Nombres largos: goleiro, líbero, zagueiro, lateral (esquerdo / direito), volante, meio-campista, meia lateral, meia-atacante, ala, ponta, segundo atacante, centroavante.

## Habilidades
| EN | PT-BR | | EN | PT-BR |
|---|---|---|---|---|
| Attack | Ataque | | Shot accuracy | Precisão do chute |
| Defence | Defesa | | Shot power | Força do chute |
| Balance | Equilíbrio | | Shot technique | Técnica de chute |
| Stamina | Resistência | | Free kick accuracy | Precisão em faltas |
| Top speed | Velocidade máx. | | Swerve | Curva |
| Acceleration | Aceleração | | Heading | Cabeceio |
| Response | Reação | | Jump | Impulsão |
| Agility | Agilidade | | Technique | Técnica |
| Dribble accuracy | Precisão do drible | | Aggression | Agressividade |
| Dribble speed | Velocidade do drible | | Mentality | Mentalidade |
| Short pass accuracy | Prec. do passe curto | | Goal keeping skills | Habilidade de goleiro |
| Short pass speed | Vel. do passe curto | | Teamwork | Trabalho em equipe |
| Long pass accuracy | Prec. do passe longo | | Consistency | Regularidade |
| Long pass speed | Vel. do passe longo | | Weak foot accuracy | Precisão do pé fraco |
| Injury tolerance | Resistência a lesões | | Weak foot frequency | Uso do pé fraco |
| Condition (estadística) | Condição física | | | |

Habilidades especiales: Long throw → Lateral longo · 1-on-1 stopper → Especialista no mano a mano · Penalty stopper → Pegador de pênaltis.

Abreviaturas de habilidades: ATT ATQ · DEF DEF · SPD VEL · POW FOR · STA RES · TWK EQP.

## Fijados de antemano (lo que en los idiomas anteriores hubo que unificar después)
- **Modos:** International Challenge → Desafio Internacional; Challenge (entrenamiento) → Desafio; Challenge Training → Treino de desafio; Step-by-step Training → Treino passo a passo.
- **Competiciones:**
  - European Masters Cup → Copa Masters Europeia; European Championship → Campeonato Europeu;
  - Northern / Southern / Eastern / Western League %s → Liga Norte / Sul / Leste / Oeste %s;
  - Knock-out (Stage) → Mata-mata (fase de mata-mata); Group / Group League → Grupo / Fase de grupos; Round robin → Pontos corridos; Play-off → Repescagem; Qualifiers → Eliminatórias; 3rd place play-off → Disputa de 3º lugar;
  - Draw (sorteo) → Sorteio; Table → Classificação; Fixtures → Tabela de jogos;
  - Semi / Quarter final → Semifinal / Quartas de final; Top scorer → Artilheiro.
- **Liga Master:** Memorial Match → Jogo de despedida; Records room → Sala de recordes; Topics → Notícias; Newcomers → Recém-chegados; Off season → Pré-temporada; Funds → Orçamento.
- **Reglas:** Away goal → Gol fora de casa; Golden / Silver goal → Gol de ouro / Gol de prata.
- **Dificultad:** Beginner / Amateur / Regular / Professional / Top Player / Super Star → Iniciante / Amador / Normal / Profissional / Top Player / Superstar.
- **Tiempo:** Fine / Rainy / Snow → Ensolarado / Chuvoso / Neve; Season (tiempo) → Estação; Day / Night → Dia / Noite.
- **Controles:**
  - Dash → Arrancada; 1-Touch / Direct pass → Passe de primeira; Direct shot → Chute de primeira;
  - 1-2 pass → Tabela; Step over → Pedalada; Marseille Roulette → Roleta (de Marselha); Sliding tackle → Carrinho;
  - Gauge (barra de potencia) → barra de força; Super cancel → Supercancelar.
- **Red:** Rating → Rating; User ID → ID de usuário; Password → Senha; Lobby → Lobby; Room → Sala; Server → Servidor; Prohibited Word List → Lista de palavras proibidas; Chat → Chat; las frases del chat entre jugadores van con «você» informal, como se habla entre jugadores.
- **«Cleared»** (`109:42`, `23:41`, `109:38`): desafío superado (Concluído). El «Despeje» del español es un error de Konami.
- **Cámara:** Bird's-eye → Visão aérea.
- **«Nice %s!»** → «Belo lance: %s!».
- **Quedan en inglés, como en los idiomas oficiales:** Club House, los textos del menú de idiomas `52:135`–`52:164` (el armador escribe `52:136` y `52:138`), nombres de comentaristas, Konami ID, UPnP y STUN.
- **Fast / Slow (`108:20`, `108:21`):** al revés que el inglés, como en francés, alemán, italiano y español, y como en los otros idiomas nuestros (Fast → Lento). Los otros Fast/Slow (`24:255`, `24:256`) van normales.
- **Letras del ejecutor** (`286:72`, `286:133`–`136`): [L] tiro libre lejano (longa), [C] cercano (curta), [E] córner izquierdo, [D] córner derecho, [PEN]; se mira en el juego.
- **Mismo texto, misma traducción:** si un texto inglés tiene las mismas traducciones oficiales en todas sus apariciones, lleva una sola traducción (`lotes.py unir` lo hace solo).

## Fijados al unificar la primera pasada (2026-11-21)

Las 8 tandas tradujeron 7 958 textos con 0 errores. `lotes.py unir` unificó 128 grupos de textos repetidos, y a mano se corrigieron 27 textos más. Quedaron así:
- **Datos:** Save mode / Delete mode → Modo salvar / Modo excluir (como los citan las ayudas); Player Settings → Configurações pessoais; Formation Settings → Ajustes de formação; Team management → Gestão do time.
- **Controles y jugadas:**
  - Feed → Passe; Wall defence → Defesa com barreira;
  - Drop kick (del arquero) → Reposição com o pé; Through feint → Corta-luz;
  - Tackle → Desarme; Clear → Afastar.
- **Táctica:** Strategy Plan A/B → Plano estrat. A/B; Lineup Auto Select → Escalação automática.
- **Partido:** Goal box / Penalty box → Pequena área / Grande área; Far / Near side → Segundo / Primeiro pau; Stoppage Time → Acréscimos.
- **Red:** Owner → Dono; One-on-one Chat → Chat privado; Room → Sala; Rating de la red → Rating.
- **Jugador:** Both feet / L&R → Ambidestro / Ambos; Costume → Traje (las etiquetas de 7 letras no admiten «Fantasia»); Scoring → Finalização; Post player → Pivô; Outside → Trivela.
- **Liga Master:** Release → Dispensar; Promotion / Relegation → Acesso / Rebaixamento; Goal ranking → Artilharia; Win ave. → Aproveitamento.
- **Revisión automática (2026-11-21):**
  - sin formas de Portugal (el script marcaba «carregue», que en Brasil es el imperativo de «carregar»);
  - ningún artículo pegado a `%s` ni sustantivo detrás de `%d` (lo que marca son «%d ou», «%d para», «%d a»);
  - comillas “ ”.
