# TAREA 5. `cap_07` Y `cap_08`, DOS CAPITULOS Y NO TRES (`8.1`, `ACTA M2` `4.4`)

> **EL TRAMO DE ESTA LINEA BAJA A `DOS` CAPITULOS POR VUELTA.** `cap_06` dio `11,11` por encima del
> tope de `10` (seccion 1.b): se baja un escalon desde los tres con los que corrio la vuelta 2. Y por
> el otro camino se llega al mismo sitio: la `ACTA M2` `4.4` ya lo habia dejado en `DOS` por el `15,09`
> de `cap_03`, encargo que nunca llego a esta linea (`ACTA M3` `M3.2`).

**EL BORDE IZQUIERDO HEREDADO:** `cap_06` queda minado entero, cuerpo `L8` a `L139`, `2905` palabras,
`51` piezas, `0` residuo sin asignar (`ACTA M3` `M3.4`). `cap_07` vive en otro fichero
(`fuentes/marquet_turn_the_ship/cap_07.md`), asi que no hay linea que continuar entre los dos.

## 5.a. `cap_07` (Cap. 11, *I Intend To . . .*)

### 5.a.1. La unidad que se mina

| | | de donde sale |
|---|---|---|
| fichero | `fuentes/marquet_turn_the_ship/cap_07.md` | encargo, seccion 2 |
| unidad que el fichero declara | Cap. 11 | `sed -n '4p' fuentes/marquet_turn_the_ship/cap_07.md` |
| titulo textual | *"I Intend To . . ."* | `sed -n '5p' fuentes/marquet_turn_the_ship/cap_07.md` |
| lineas del fichero | 127 | `wc -l fuentes/marquet_turn_the_ship/cap_07.md` |
| palabras del fichero entero | 2222 | `wc -w fuentes/marquet_turn_the_ship/cap_07.md`, coincide con el encargo |
| cuerpo, desde `L8` | 2189 | `sed -n '8,$p' fuentes/marquet_turn_the_ship/cap_07.md \| wc -w` |

### 5.a.2. LA FRONTERA ENTERA, PIEZA A PIEZA

<!-- TALLADO: parcial salida=.v3m/frontera/cap_07_bruta.txt -->

La columna de palabras por linea sale de `awk 'NR>=8 && NF>0{print NR": "NF}' cap_07.md`, guardada
entera en `.v3m/frontera/cap_07_bruta.txt`; la columna *que es* y *clase* es lectura, no instrumento.

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| R1 | L9 | 6 | rotulo del titulo *"I Intend To . . ."* | RESIDUO: rotulo |
| R2 | L11 | 19 | pregunta de apertura sobre proactividad y el lenguaje | POSTURA |
| R3 | L13 | 10 | fecha, sitio y cuenta atras al despliegue | RESIDUO: rotulo de fecha |
| R4 | L15 | 27 | escena: aviso de reactor scram | CASO |
| R5 | L17 | 81 | cuatro dias de entrenamiento antes de la inspeccion | CASO |
| R6 | L19 | 137 | la mentalidad de inspeccion, ORSE y TRE | POSTURA |
| R7 | L21 | 95 | Weps y Eng arman el programa del simulacro | CASO |
| R8 | L23 | 84 | descripcion del simulacro de perdida de propulsion | CASO |
| R9 | L25 | 53 | montaje del simulacro | CASO |
| R10 | L27 | 109 | el OOD Bill Greene hace todo correctamente | CASO |
| R11 | L29 | 77 | el capitan sugiere subir la velocidad en el EPM | CASO |
| R12 | L31 | 5 | "Ahead two thirds" ordenado | CASO |
| R13 | L33 | 2 | "Nothing happened" | CASO |
| R14 | L35 | 67 | el timonel se remueve incomodo | CASO |
| R15 | L37 | 72 | la excusa del capitan (no conocia el submarino) | CASO |
| R16 | L39 | 29 | aplaude al timonel, pregunta a Bill | CASO |
| R17 | L41 | 4 | "Yes, Captain, I did" | CASO |
| R18 | L43 | 9 | "Well, why did you order it?" | CASO |
| R19 | L45 | 5 | "Because you told me to" | CASO |
| R20 | L47 | 1 | "What?" | CASO |
| R21 | L49 | 16 | "secreto aprendido en la escuela de PCO" | CASO |
| R22 | L51 | 88 | reflexion: modelo de mando y control, todos van al precipicio | POSTURA |
| R23 | L53 | 50 | origen del habito en el USS Sunfish | CASO: origen narrativo del mecanismo |
| **P1** | **L55, L73 a L93** | **165** | **NODO: declarar intencion con frases activas en vez de pedir permiso, y responder con aprobacion simple (ver 5.a.3 y DISCUTIBLE 1)** | **NODO** |
| R24 | L57 | 15 | rotulo *"Mechanism: Use 'I Intend to . . .' to Turn Passive Followers into Active Leaders"* | RESIDUO: rotulo de mecanismo |
| R25 | L59 | 36 | framing: mecanismo incretiblemente poderoso, desplaza la propiedad del plan | POSTURA |
| R26 | L61 | 83 | regla propia de Santa Fe: solo aplica cuando el capitan esta despierto | CASO: regla operativa de esa nave |
| R27 | L63 | 72 | visita de Stephen Covey al puente de Santa Fe | CASO |
| R28 | L65 | 39 | ejemplo: "Captain, I intend to submerge the ship..." | CASO/ejemplo |
| R29 | L67 | 2 | "Very well." | CASO (continuacion del ejemplo) |
| R30 | L69 | 51 | referencia al libro de Covey, *The 7 Habits* | RESIDUO: referencia externa |
| R31 | L71 | 4 | subrotulo *"The Power of Words"* | RESIDUO: rotulo |
| R32 | L95 | 21 | referencia al libro de Covey, *The 8th Habit* | RESIDUO: referencia externa |
| R33 | L97 | 5 | "Then we extended the concept." | POSTURA: transicion |
| R34 | L99 | 32 | frecuentemente no se limitaba a decir "very well" | POSTURA, DISCUTIBLE 2 (ver 5.a.4) |
| R35 | L101 | 31 | un dia se dio cuenta, pregunto al OOD que creia que pensaba | CASO |
| R36 | L103 | 14 | respuesta del OOD: "you are wondering if it's safe and appropriate" | CASO |
| R37 | L105 | 26 | "Correct. So why don't you just tell me..." | CASO |
| R38 | L107 | 66 | la meta pasa a ser un reporte completo para que la respuesta sea aprobacion simple | POSTURA, DISCUTIBLE 2 |
| R39 | L109 | 110 | beneficio: pensar en el nivel superior de mando | POSTURA |
| R40 | L111 | 51 | 135 lideres independientes en vez de un capitan dando ordenes | POSTURA |
| R41 | L113 | 132 | anecdota del amigo de la escuela PCO, "good ships" | CASO/POSTURA |
| R42 | L115 | 34 | se recompensa el liderazgo centrado en la personalidad | POSTURA |
| R43 | L117 | 76 | por que dio esa orden: la atraccion seductora del poder | POSTURA |
| R44 | L119 | 3 | rotulo *QUESTIONS TO CONSIDER* | RESIDUO: rotulo |
| R45 | L121 | 12 | pregunta 1 | PENDIENTE DE DOCTRINA, vuelta 25 |
| R46 | L123 | 25 | pregunta 2 | PENDIENTE DE DOCTRINA |
| R47 | L125 | 20 | pregunta 3 | PENDIENTE DE DOCTRINA |
| R48 | L127 | 18 | pregunta 4 | PENDIENTE DE DOCTRINA |
| **el cuerpo entero** | **L8 a L127** | **2189** | **suma de las piezas: 2189** | **residuo sin asignar: 0** |

    piezas: 49   lineas solapadas: 0   cuerpo 2189   suma 2189   residuo 0   lineas con palabras sin cubrir: 0

**LA FRONTERA CIERRA AL DIGITO: cuerpo `2189`, suma de piezas `2189`, residuo `0`, cero solapes y cero
lineas con palabras sin cubrir.** Una sola pieza se mina, `P1`, compuesta de dos tramos no contiguos;
las otras 48 filas son residuo, postura o caso.

### 5.a.3. LA CITA DE LA PIEZA QUE SE MINA, CON SU `sed` PEGADO (`D.35`)

| linea | la salida de `sed`, pegada | veredicto |
|---|---|---|
| L55 | `That's what we decided to do on Santa Fe... Officers would state their intentions with "I intend to . . ." and I would say, "Very well." Then each man wo...` | NODO, paso 3 (respuesta) |
| L73 | `The key to your team becoming more proactive rests in the language subordinates and superiors use. Here is a short list of "disempowered phrases" that pa...` | NODO, intro lista 1 |
| L75 | `Request permission to . . .` | NODO, paso 1 |
| L77 | `I would like to . . .` | NODO, paso 1 |
| L79 | `What should I do about . . .` | NODO, paso 1 |
| L81 | `Do you think we should . . .` | NODO, paso 1 |
| L83 | `Could we . . .` | NODO, paso 1 |
| L85 | `Here is a short list of "empowered phrases" that active doers use:` | NODO, intro lista 2 |
| L87 | `I intend to . . .` | NODO, paso 2 |
| L89 | `I plan on . . .` | NODO, paso 2 |
| L91 | `I will . . .` | NODO, paso 2 |
| L93 | `We will . . .` | NODO, paso 2 |

### 5.a.4. LOS DISCUTIBLES 1 Y 2, MARCADOS ANTES DE SABER SI ACIERTO

**DISCUTIBLE 1** (`P1`): la pieza junta `L55` con `L73` a `L93`, saltandose `L57` a `L71` (rotulo,
framing, la regla de Santa Fe y la visita de Covey). Lo sostengo como UNA sola pieza porque las dos
mitades desarrollan el mismo mecanismo nombrado en el rotulo de `L57`: la respuesta simple (`L55`) y el
vocabulario concreto que la hace posible (`L73` a `L93`, bajo el subrotulo *The Power of Words* de
`L71`, que es la misma seccion). **Si el auditor lee que son dos mecanismos distintos, esto se parte en
dos candidatos.**

**DISCUTIBLE 2** (`R33`, `R34`, `R38`, `L97` a `L107`, ver tambien la cabecera de esta vuelta): la extension del mecanismo, donde Marquet deja
de hacer preguntas y pide que el reporte de intencion ya venga con el razonamiento completo, **NO se
mina como nodo propio** porque no lleva su propio rotulo de "Mechanism:" (a diferencia de `L57`) y sus
pasos habria que inferirlos del dialogo entre el capitan y el OOD (`L101` a `L107`), no transcribirlos:
`EXTRACTOR.md` 15.4 pide desconfiar de los pasos propios cuando el parrafo no trae su propio inventario.
**Se sostiene como POSTURA.**

### 5.a.5. EL CANDIDATO, ESCRITO Y PASADO POR LA ADUANA EN SECO EN EL MISMO ACTO

`cuarentena/marquet_turn_the_ship/declarar_intencion_reemplazar_peticion_permiso.json`, con
`UNIDAD DE ORIGEN: fuentes/marquet_turn_the_ship/cap_07.md` en su `resumen_teorico`. **3 pasos, 3
TRANSCRIPCION, 0 PUENTE** (relectura de fidelidad `D.30` en el acto, seccion 5.a.3 arriba cita cada
linea). El informe de aduana en seco esta en la seccion 5.c, guardado en `.v3m/aduana/c3.txt`.

## 5.b. `cap_08` (Cap. 12, *Up Scope!*)

### 5.b.1. La unidad que se mina

| | | de donde sale |
|---|---|---|
| fichero | `fuentes/marquet_turn_the_ship/cap_08.md` | encargo, seccion 2 |
| unidad que el fichero declara | Cap. 12 | `sed -n '4p' fuentes/marquet_turn_the_ship/cap_08.md` |
| titulo textual | *Up Scope!* | `sed -n '5p' fuentes/marquet_turn_the_ship/cap_08.md` |
| lineas del fichero | 131 | `wc -l fuentes/marquet_turn_the_ship/cap_08.md` |
| palabras del fichero entero | 2253 | `wc -w fuentes/marquet_turn_the_ship/cap_08.md`, coincide con el encargo |
| cuerpo, desde `L8` | 2224 | `sed -n '8,$p' fuentes/marquet_turn_the_ship/cap_08.md \| wc -w` |

### 5.b.2. LA FRONTERA ENTERA, PIEZA A PIEZA

<!-- TALLADO: parcial salida=.v3m/frontera/cap_08_bruta.txt -->

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| R1 | L9 | 2 | rotulo del titulo *Up Scope!* | RESIDUO: rotulo |
| R2 | L11 | 19 | pregunta de apertura sobre ayudar a llegar a la respuesta correcta | POSTURA |
| R3 | L13 | 10 | fecha, sitio y cuenta atras al despliegue | RESIDUO: rotulo de fecha |
| R4 | L15 | 45 | escena: la mesa de cartas de navegacion abarrotada | CASO |
| R5 | L17 | 27 | hacia donde iba el enemigo | CASO |
| R6 | L19 | 58 | "Here, we need to be here at 0600" | CASO |
| R7 | L21 | 81 | medianoche, exhausto, necesita dormir | CASO |
| R8 | L23 | 30 | mira alrededor, no hay preguntas | CASO |
| R9 | L25 | 96 | un enfoque mas ilustrado habria sido discutir, pero no tenia energia | CASO/POSTURA |
| R10 | L27 | 11 | subrotulo de fecha, "January 28" | RESIDUO: rotulo de fecha |
| R11 | L29 | 111 | se levanta y descubren que estan fuera de posicion | CASO |
| R12 | L31 | 37 | el comodoro Kenny observa; el capitan asume el fallo como propio | CASO |
| R13 | L33 | 181 | reaccion inmediata de controlar todo mas de cerca; reflexion sobre el control | POSTURA |
| R14 | L35 | 53 | trabajan hacia una mejor posicion tactica | CASO |
| R15 | L37 | 22 | "Up scope", el OOD sube el periscopio | CASO |
| R16 | L39 | 63 | Santa Fe justo bajo la superficie | CASO |
| R17 | L41 | 31 | las etapas finales del juego del gato y el raton | CASO |
| R18 | L43 | 82 | el enemigo eligio esta zona deliberadamente | CASO |
| R19 | L45 | 84 | el torpedo Mk 48 ADCAP | CASO |
| R20 | L47 | 33 | "Target!", el OOD ve el periscopio enemigo | CASO |
| R21 | L49 | 65 | "recommend firing point procedures!" | CASO |
| R22 | L51 | 9 | "Very well, Weps" | CASO |
| R23 | L53 | 14 | ordena el ataque | CASO |
| R24 | L55 | 7 | se limpia el sudor de la frente | CASO |
| R25 | L57 | 26 | la letania estandar que sigue a la orden | CASO |
| R26 | L59 | 9 | solicitud de subir la antena BRA-34 | CASO |
| R27 | L61 | 5 | "What? Raise the radio antenna?" | CASO |
| R28 | L63 | 48 | fin del ciclo de doce horas de transmision | CASO |
| R29 | L65 | 71 | resiste el impulso de un berrinche, mira al comodoro Kenny | CASO |
| R30 | L67 | 26 | al senalar el mapa y dar la solucion, empeoro las cosas | POSTURA |
| R31 | L69 | 48 | tentado a ladrar ordenes, mira sus zapatos, "we're not going to do that" | CASO |
| R32 | L71 | 7 | espera varios segundos, funciono | CASO |
| R33 | L73 | 74 | los jefes de departamento entran en una discusion rapida | CASO |
| R34 | L75 | 6 | "recommend continuing with the attack!" | CASO |
| R35 | L77 | 1 | "Voila!" | CASO |
| R36 | L79 | 38 | "final bearing and shoot", el periscopio sube | CASO |
| R37 | L81 | 13 | "Set!" | CASO |
| R38 | L83 | 24 | "Shoot!" anuncia Dave Adams | CASO |
| R39 | L85 | 28 | "Woosh!", la sacudida del lanzamiento | CASO |
| R40 | L87 | 5 | "Unit running normally, wire good!" | CASO |
| R41 | L89 | 9 | "Unit has merged on the bearing of the target" | CASO |
| R42 | L91 | 6 | los reportes normales llegaban | CASO |
| R43 | L93 | 35 | ahora esperaban a que el torpedo viera al enemigo | CASO |
| R44 | L95 | 23 | "Detect!" lo vio | CASO |
| R45 | L97 | 4 | "Acquire!" lo tenian | CASO |
| R46 | L99 | 19 | "Loud explosion", simulada por el inspector | CASO |
| R47 | L101 | 11 | vitores en la sala de control, primer exito | CASO |
| R48 | L103 | 7 | rotulo *"Mechanism: Resist the Urge to Provide Solutions"* | RESIDUO: rotulo de mecanismo |
| R49 | L105 | 32 | reflexiono que debio dejar que sus oficiales resolvieran | POSTURA |
| **P1** | **L107, L115 a L121** | **252** | **NODO: resistir dar la solucion y clasificar la decision del equipo segun su urgencia (ver 5.b.3 y DISCUTIBLE 2)** | **NODO** |
| R50 | L109 | 86 | anecdota del simulador de entrenamiento: treinta minutos en linea recta | CASO |
| R51 | L111 | 3 | separador de seccion | RESIDUO: separador |
| R52 | L113 | 68 | cuantas veces surgen decisiones de improviso; organizacion reactiva | POSTURA |
| R53 | L123 | 3 | rotulo *QUESTIONS TO CONSIDER* | RESIDUO: rotulo |
| R54 | L125 | 13 | pregunta 1 | PENDIENTE DE DOCTRINA, vuelta 25 |
| R55 | L127 | 15 | pregunta 2 | PENDIENTE DE DOCTRINA |
| R56 | L129 | 15 | pregunta 3 | PENDIENTE DE DOCTRINA |
| R57 | L131 | 23 | pregunta 4 | PENDIENTE DE DOCTRINA |
| **el cuerpo entero** | **L8 a L131** | **2224** | **suma de las piezas: 2224** | **residuo sin asignar: 0** |

    piezas: 58   lineas solapadas: 0   cuerpo 2224   suma 2224   residuo 0   lineas con palabras sin cubrir: 0

**LA FRONTERA CIERRA AL DIGITO: cuerpo `2224`, suma de piezas `2224`, residuo `0`, cero solapes y cero
lineas con palabras sin cubrir.** Una sola pieza se mina, `P1`, compuesta de dos tramos no contiguos
(`L107` y `L115` a `L121`); las otras 57 filas son residuo, postura o caso.

### 5.b.3. LA CITA DE LA PIEZA QUE SE MINA, CON SU `sed` PEGADO (`D.35`)

| linea | la salida de `sed`, pegada | veredicto |
|---|---|---|
| L107 | `Emergency situations required snap decision making and clear orders... you have to create a space for open decision by the entire team, even if that spac...` | NODO, pasos 1 y 2 |
| L115 | `You need to change that cycle. Here are a few ways to try to get your team thinking for themselves:` | NODO, intro inventario |
| L117 | `If the decision needs to be made urgently, make it, then have the team "red-team" the decision and evaluate it.` | NODO, paso 3 |
| L119 | `If the decision needs to be made reasonably soon, ask for team input, even briefly, then make the decision.` | NODO, paso 4 |
| L121 | `If the decision can be delayed, then force the team to provide inputs. Do not force the team to come to consensus; that results in whitewashing differenc...` | NODO, paso 5 |

### 5.b.4. EL DISCUTIBLE 3, MARCADO ANTES DE SABER SI ACIERTO

La pieza junta `L107` con `L115` a `L121`, saltandose `L109` a `L113` (la anecdota del simulador de
entrenamiento y la reflexion sobre organizaciones reactivas). Lo sostengo como UNA sola pieza porque las
dos mitades desarrollan el mismo mecanismo nombrado en el rotulo de `L103` (*Resist the Urge to Provide
Solutions*): el marco general de dar espacio para decidir (`L107`) y la clasificacion concreta por
urgencia que lo opera (`L115` a `L121`). **Si el auditor lee que son dos mecanismos distintos (uno de
dar espacio, otro de clasificar por urgencia), esto se parte en dos candidatos.**

### 5.b.5. EL CANDIDATO, ESCRITO Y PASADO POR LA ADUANA EN SECO EN EL MISMO ACTO

`cuarentena/marquet_turn_the_ship/resistir_dar_solucion_clasificar_decision_urgencia.json`, con
`UNIDAD DE ORIGEN: fuentes/marquet_turn_the_ship/cap_08.md` en su `resumen_teorico`. **5 pasos, 5
TRANSCRIPCION, 0 PUENTE** (relectura de fidelidad `D.30` en el acto, seccion 5.b.3 arriba cita cada
linea). El informe de aduana en seco esta en la seccion 5.c, guardado en `.v3m/aduana/c4.txt`.

