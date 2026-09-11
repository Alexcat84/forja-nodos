# APERTURA CIEGA DE LA VUELTA 12

**Lote 3, `zhuo_manager`. Tramo: Cap. 5 (`cap_06.md`), una unidad**, mas los dos candidatos
que la TAREA 1 de la vuelta corrigio y que salen de `cap_05.md`.

*Escrita por el auditor en la fase de apertura ciega de `D.34`, con `docs/loop/REPORTE.md`
retirado del arbol por el arnes. **No lo he recuperado de git ni por ninguna otra via.**
Esta es la lectura que despues se compara con la del extractor: mientras no se compare,
**no es una adjudicacion y no mueve credito de nadie.***

---

## 0. QUE VI Y QUE NO VI ANTES DE LEER, Y UNA CAIDA PROPIA MIA AL PRINCIPIO

### 0.1. CAIDA PROPIA, DECLARADA ANTES QUE NADA: **ABRI `ultimo_extractor.json`**

**Lo hice en mi segundo comando, buscando de que capitulo era el lote, y ese fichero trae el
mensaje final del extractor entero.** No es el reporte y el arnes no lo retira, pero **el
efecto practico es el mismo en los puntos que ahi vienen**, y el auditor de la vuelta pasada
escribio expresamente en su seccion 10 que NO lo habia leido. **Rompi un habito escrito por mi
propia sede, y lo digo yo, que soy el perjudicado por decirlo.**

**Lo que ese fichero me enseno, dicho exacto, para que nadie tenga que adivinar el alcance:**

| lo que vi ahi | efecto sobre esta lectura |
|---|---|
| que el tramo es el Cap. 5, 18 candidatos, 162 pasos | **ninguno: lo he medido yo aparte, seccion 2** |
| que el extractor cuenta **6 puentes de encuadre, cuatro de ellos en el paso 1** | **CONTAMINADO. Mi cifra de la seccion 8 no vale como lectura independiente en su banda** |
| que su DISCUTIBLE 4 es la escena de apertura, sostenida sobre **una linea de las once** | **CONTAMINADO. Mi DISCUTIBLE 1 coincide, y por tanto NO cuenta como coincidencia** |
| que su DISCUTIBLE 6 calcula **26,5 por ciento** si `Ten delante` y `Cuenta con` cuentan | **CONTAMINADO en la banda ancha** |
| que declara discrepancia viva en tasa de atribucion y en el reloj | no toco ninguna de las dos aqui |

**POR TANTO, Y ESTO ES LO QUE IMPORTA:** de esta apertura, **lo unico que puede alegarse como
lectura ciega de verdad son las secciones 3, 4, 5, 6, 7 y 9**, que son el inventario pieza a
pieza, la clase de cada candidato, los pares, las aristas y los hallazgos. **La seccion 8 va
escrita igual, con sus tres bandas y su comando, pero va marcada CONTAMINADA en las dos bandas
donde el extractor ya me dijo su numero.** Una cifra que coincide despues de haber visto la
ajena no es una medida: es un eco.

### 0.2. El orden real de mis actos, sin maquillar

| lo que consulte, en orden | ciega? |
|---|---|
| `AUDITOR_FORJA.md` entero | protocolo mio |
| `ls` de `cuarentena/`, `fuentes/`, `docs/loop/` | **NO: vi los 68 nombres de fichero, y un id dice de que va un nodo** |
| `loop.log`, `ORDEN_DE_LOTES.md`, `git status`, `git log` | estado |
| **`ultimo_extractor.json`** | **NO, y es la caida de 0.1** |
| `git show --stat` de los commits de la vuelta | me dio el corte exacto: **18 ficheros nuevos en `5576c21`**, 2 modificados en `5efd637` |
| `APERTURA_CIEGA.md` de la vuelta 10, por `git show HEAD:` | **sede mia**, la abri por el formato y por mi propia vara de `D.30` |
| **`cuarentena/zhuo_manager/listar_fuerzas_propias_cuatro_preguntas.json` entero** | **NO, Y ES LA UNICA DEL LOTE: la abri de muestra para aprender el esquema ANTES de leer el capitulo** |
| **`cap_06.md` entero, de `L1` a `L477`** | **aqui escribi el inventario de la seccion 3** |
| solo DESPUES, los 18 candidatos con sus 162 pasos | |
| `dataset/nodos.jsonl`, los 52 ids, y tres candidatos viejos de la bandeja | estado, para los cruces de la seccion 5 |

**`listar_fuerzas_propias_cuatro_preguntas` esta contaminado y no lo cuento como lectura
independiente.** `L75` a `L93` habria dado nodo en mi inventario de todas formas, porque el
libro declara ahi su propio inventario (*ask yourself the following questions*), **pero eso lo
digo yo despues de haberlo visto, y una razon dada despues no vale lo que una dada antes.**

---

## 1. MI CRITERIO, ESCRITO ANTES DE CLASIFICAR Y NO DESPUES

**a. Para PIEZA CON NODO O SIN NODO.** Manual seccion 4 y la vara de `AUDITOR_FORJA.md` 6.1.
Una pieza saca nodo propio si trae **disparador propio, acto propio y entregable propio**.
`P.5.1`: **nombrar no es procedimentar.** Una cabeza de serie solo vale como nodo si trae
doctrina suya ademas de los nombres de sus hijos. **Y una advertencia es linea:** una postura
no ejecuta una busqueda.

**b. Para CONTINUA O REPITE.** Con direccion y sin bascula: se pregunta **que aniade el hijo a
la madre**, y decide **si lo que queda fuera es procedimiento en los dos lados**, no el tamanio
del solape. **La arista no exculpa**, y su ausencia tampoco condena: en `MODO_INSERCION=cuarentena`
los candidatos no las traen escritas (`D.26`).

**c. Para TRANSCRIPCION O PUENTE (`D.30`), y la fijo ANTES de contar**, con la misma vara que
publique en la apertura de la vuelta 10, **sin estrecharla y sin ensancharla**:

> **ES PUENTE** un paso que manda algo que el libro **no manda en sentido**, y en particular el
> paso en imperativo levantado sobre **narracion en primera persona del pasado** o sobre **una
> cita de un tercero que cuenta y no ordena**.
>
> **ES TRANSCRIPCION** el cambio de modo verbal sobre un consejo que el libro ya dirige al
> lector en segunda persona, aunque venga en condicional o en enunciado.

**Y AQUI ANIADO LA PREGUNTA QUE ESTE TRAMO OBLIGA A HACERSE, porque el tramo es casi todo eso:**
que hacer con un paso cuyo verbo de cabeza es **`Ten delante`, `Cuenta con`, `Ten claro`,
`Parte de`, `Mira`, `Fijate`, `Usalo`**, seguido de contenido fiel y **con la atribucion
escrita dentro**. No lo resuelvo inventando doctrina. **Lo mido en tres bandas separadas
(seccion 8) y digo cual es cual**, porque de cual se elija sale el volumen del lote 4.

---

## 2. LO QUE MEDI YO, CON SU COMANDO AL LADO

    $ awk 'NR>7' fuentes/zhuo_manager/cap_06.md | wc -w        9617
    $ wc -l < fuentes/zhuo_manager/cap_06.md                    477

**LOS DOS BORDES, comprobados por mi hoy:**

| borde | lo que leo |
|---|---|
| `cap_06.md` cabecera | `unidad: Cap. 5`, `titulo_textual: Managing Yourself`, `L9: Chapter Five` |
| `cap_06.md` ultima con texto | **`L477` de 477**, cierre de capitulo: *no masks or pretenses needed* |
| `cap_07.md` cabecera | `unidad: Cap. 6`, `titulo_textual: Amazing Meetings`. **Abre unidad nueva: el borde esta limpio por los dos lados** |

**PASOS Y CANDIDATOS, contados por mi sobre los ficheros de cuarentena** (seccion 8.3.1: la
cifra la cuento yo, no la copio):

| unidad | fichero | palabras | candidatos | pasos escritos | candidatos por mil palabras |
|---|---|---:|---:|---:|---:|
| **Cap. 5** | `cap_06.md` | **9.617** | **18** | **162** | **1,87** |

**Es un capitulo, asi que la fila de la seccion 8.2 y el total del lote de esta vuelta son la
misma cifra, y lo digo para que no parezca que oculto un desglose.**

**Y LA COMPROBACION QUE SALE CERO SE ESCRIBE CERO:**

    $ bandeja zhuo_manager: 68 ficheros, 68 ids unicos, 68 de 68 con id igual al nombre de fichero
    $ dataset/nodos.jsonl: 52 nodos. Choques bandeja contra dataset: 0
    $ los 18 del tramo: 18 de 18 con nodos_previos vacio y nodos_siguientes vacio, correcto en D.26
    $ los 18 del tramo: 18 de 18 con fuente unica zhuo_manager, fecha 2026-09-11

---

## 3. MI INVENTARIO DEL Cap. 5, `cap_06.md`, PIEZA A PIEZA

**Escrito leyendo el fichero entero de un tiron, con la bandeja cerrada.**

| # | pieza | lineas | mi lectura a ciegas |
|---:|---|---|---|
| 1 | Los rotulos AVOID y ASPIRE | `L13` a `L15` | **SIN NODO.** Son el arte del capitulo, no texto |
| 2 | La escena de Stacy y el informe de veinte paginas | `L17` a `L35` | **SIN NODO.** Narracion en primera persona del pasado de cabo a rabo. No manda nada, y lo que ensenia ya es el hijo que viene despues |
| 3 | La tesis del capitulo | `L37` | **ES UNA LINEA, NO UNA PIEZA, y es la unica que ordena algo en toda la apertura.** *No matter what obstacles you face, you first need to get deep with knowing you*, y nombra cinco objetos. **Nombrar no es procedimentar: los cinco objetos son el indice del capitulo** |
| 4 | EVERYBODY FEELS LIKE AN IMPOSTER SOMETIMES | `L39` a `L61` | **SIN NODO, y es la ausencia mas gorda del tramo.** Seccion titulada por el libro, con la cita de Linda Hill, **las dos razones por las que pega fuerte al directivo** (`L51` y `L55`) y `L57`: *Management isn't an innate skill*. **Es doctrina, no es procedimiento**, y por eso acepto que no saque nodo. **Pero define el termino que seis nodos del lote usan sin definir** |
| 5 | La receta, la nevera y los lideres de molde distinto | `L65` a `L73` | **SIN NODO.** Metafora y galeria de ejemplos. Correcto dejarla fuera |
| 6 | Conocer tus fuerzas, con cuatro preguntas | `L75` a `L93` | **NODO.** `L75` declara su propio inventario: *jot down the first thing that comes to mind when you ask yourself the following questions* |
| 7 | Conocer tus debilidades y disparadores, con cuatro preguntas | `L95` a `L113` | **NODO APARTE.** El libro lo ata por la sede (`L95`: *Right beneath your list of strengths*) y le da inventario propio y distinto |
| 8 | La calibracion y las tres tacticas | `L115` a `L139` | **NODO.** Tres tacticas con destinatario distinto cada una, el guion del correo literal en `L129` y tres peticiones concretas en `L133` a `L137` |
| 9 | Pedir opinion cuesta, y las dos mentalidades de Dweck | `L141` a `L187` | **NODO.** `L149` declara el inventario (*Observe the difference*) y los cuatro escenarios traen sus dos lecturas escritas |
| 10 | Tu mejor entorno, tus habitos y las tres preguntas | `L191` a `L231` | **NODO.** `L225` declara el inventario (*ask yourself the following*) |
| 11 | Los disparadores y las cuatro preguntas | `L233` a `L257` | **NODO.** `L233` trae el criterio que separa disparador de reaccion normal, y `L247` declara el inventario |
| 12 | El Pozo, y su escena | `L259` a `L269` | **SIN NODO.** Define el termino y cuenta el caso del colega. **Misma especie que la pieza 4: define lo que seis nodos usan** |
| 13 | Don't Beat Yourself Up for Feeling Bad | `L271` a `L277` | **NODO.** Subtitulo del libro, dos tacticas numeradas por el propio libro |
| 14 | The Story I Have in My Head Is Probably Irrational | `L279` a `L301` | **NODO.** Trae dato propio: las tres respuestas de `L289` a `L293` y la excepcion de `L295` |
| 15 | Close Your Eyes and Visualize | `L303` a `L323` | **NODO.** Cinco ejercicios con guion, `L311` declara el inventario |
| 16 | Ask for Help from People You Can Be Real With | `L325` a `L335` | **NODO.** `L335` trae los cuatro sitios y los dos usos |
| 17 | Celebrate the Little Wins | `L337` a `L347` | **NODO.** El diario y sus tres ejemplos de entrada |
| 18 | Practice Self-Care by Establishing Boundaries | `L349` a `L357` | **NODO.** `L353` manda con verbo propio (*Resist this*, *Set boundaries by carving out time*) |
| 19 | El doble de bueno, con su escena del escenario | `L359` a `L373` | **SIN NODO, Y ES LA SEGUNDA AUSENCIA QUE DISCUTO.** `L373` es la cabeza declarada de las cinco vias: *set a lofty goal for yourself: How can I be twice as good? Then maximize your learning through the following* |
| 20 | Ask for Feedback | `L375` a `L381` | **NODO.** Primera via |
| 21 | Treat Your Manager as a Coach | `L383` a `L397` | **NODO.** Segunda via, con tres movimientos y sus frases literales |
| 22 | Make a Mentor Out of Everyone | `L399` a `L411` | **NODO.** Tercera via, con el guion de `L409` |
| 23 | Set Aside Time to Reflect and Set Goals | `L413` a `L451` | **NODO.** Cuarta via, la unica con cadencia fija |
| 24 | Take Advantage of Formal Training | `L453` a `L467` | **NODO.** Quinta via, con la cuenta del retorno de `L459` |
| 25 | El cierre del capitulo | `L469` a `L477` | **SIN NODO.** Correcto |

**MI CUENTA DE PIEZAS: 25 piezas, 18 con nodo y 7 sin nodo.** Y el reparto no deja hueco: las
piezas con nodo cubren `L75` a `L467` sin solapes, y los huecos son `L13` a `L15`,
`L17` a `L35`, `L37`, `L39` a `L73`, `L189`, `L259` a `L269`, `L359` a `L373` y `L469` a `L477`.

---

## 4. MI CLASE PARA CADA UNO DE LOS 18 CANDIDATOS

**Leidos DESPUES del capitulo. Clase, pasos contados por mi, y la linea que la sostiene.**

| candidato | pasos | pieza | mi clase a ciegas |
|---|---:|---|---|
| `listar_fuerzas_propias_cuatro_preguntas` | 9 | 6 | **SANO.** Contaminado por 0.2, no lo alego |
| `listar_debilidades_disparadores_propios` | 7 | 7 | **SANO, y el mas limpio del lote.** 6 de 7 pasos son el inventario del libro palabra por palabra |
| `calibrar_vision_propia_opinion_ajena` | 11 | 8 | **SANO.** 8 de 11 pasos tienen verbo del libro (`L119` *we must confront*, `L121` *Ask your manager*, `L127` *Pick three to seven*, `L139` *Ask for task-specific feedback*) |
| `cambiar_mentalidad_fija_crecimiento` | 11 | 9 | **SANO CON RESERVA.** Los cuatro escenarios son transcripcion limpia. **Los pasos 4 y 5 cambian el sujeto**: `L145` y `L147` hablan de ella en primera persona y el paso los pone en segunda |
| `disenar_entorno_rendir_mejor` | 10 | 10 | **SANO.** Y lo hace bien donde es facil fallar: los doce items de `L193` a `L219` van marcados *son suyas*, no como receta |
| `identificar_disparadores_propios_reaccion` | 14 | 11 | **SANO.** El nodo mas largo del lote y aun asi 8 de sus 14 pasos son inventario o criterio del libro |
| `evitar_doble_impuesto_malestar` | 6 | 13 | **SANO, Y EL MEJOR DEL LOTE POR DENSIDAD.** 4 de 6 pasos llevan verbo del libro: `L275` *Recognize*, *give yourself permission*, *Don't pay the double tax* |
| `cuestionar_historia_irracional_cabeza` | 8 | 14 | **SANO.** `L281` *Remember*, `L299` *step back and question* son del libro, y las tres respuestas de `L289` a `L293` estan con su excepcion de `L295`, que es lo que impide leerlo como consuelo |
| `visualizar_recuperar_confianza` | 11 | 15 | **SANO.** Los cinco *Imagine* de `L313` a `L321` son del libro, y `L323` *Develop the habit* tambien |
| `pedir_ayuda_grupo_apoyo` | 7 | 16 | **SANO CON RESERVA.** El contenido es fiel, pero **5 de sus 7 pasos son encuadre** y el mandato entero vive en `L335`. Es el nodo con peor proporcion del lote |
| `celebrar_pequenias_victorias` | 6 | 17 | **SANO.** El paso 5 monta el diario sobre `L345`, que es primera persona del pasado, **pero `L347` lo ordena al lector** (*remember to do the same*). Se sostiene por `L347`, no por `L345` |
| `establecer_limites_cuidado_personal` | 7 | 18 | **SANO.** `L353` *Resist this* y *Set boundaries*, `L357` *take care of yourself*, los tres del libro |
| `pedir_opinion_otros_mejorar` | 8 | 20 | **SANO.** 6 de 8 pasos con verbo del libro, y el paso 1 conserva la remision al capitulo anterior que el libro escribe en `L377` |
| `tratar_jefe_entrenador` | 11 | 21 | **SANO CON RESERVA.** Los tres movimientos salen de `L395` con sus frases literales. **El paso 11 levanta un imperativo sobre `L397`, que es primera persona del pasado** |
| `convertir_cualquiera_mentor` | 10 | 22 | **SANO.** `L401` *ask for specific advice instead*, `L409` *don't be afraid to ask*, `L411` *Keep in mind* y *Thank them anyway*, los cuatro del libro |
| `reservar_tiempo_reflexion_metas` | 11 | 23 | **DISCUTIBLE, Y ES MI UNICO PUENTE.** Ver seccion 8 |
| `aprovechar_formacion_reglada` | 8 | 24 | **SANO.** `L455` *take it* y `L465` *the question to ask isn't... but rather* son del libro. **6 de 8 pasos son encuadre**, segunda peor proporcion |
| `conocer_fuerzas_valores_sesgos_propios` | 7 | 2 y 3 | **DISCUTIBLE 1. Mi lectura es que esta pieza NO daba nodo.** Ver seccion 7 |

**LOS DOS CORREGIDOS POR LA TAREA 1, que salen de `cap_05.md` y no de este tramo:**

| candidato | que se toco | mi lectura |
|---|---|---|
| `mover_rapido_persona_papel_equivocado` paso 1 | reescrito | **EL REMEDIO SE SOSTIENE Y LO FIRMO.** Era el unico puente que yo encontre en la vuelta 10. La redaccion nueva devuelve lo que `L283` y `L285` dicen de verdad, y marca la narracion como narracion. **Ahora es TRANSCRIPCION** |
| `dar_mala_noticia_decision_tomada` paso 8 | **borrado** | **EL REMEDIO CIERRA MI DISCUTIBLE Y ABRE UN AGUJERO, y lo digo aunque el discutible fuera mio.** Yo escribi que el contenido estaba bien y el sitio no. La rama elegida fue sacarlo, no moverlo, asi que **`L283` de `cap_05.md` no esta hoy en ningun nodo de la bandeja**: `grep -rl "flores fragiles" cuarentena/` y `grep -rl "guantes de seda" cuarentena/` **no devuelven nada** |

---

## 5. LOS PARES QUE MIRE POR CONTINUA O REPITE, Y COMO LOS ADJUDICO

**Ninguno es REPITE. Los cuatro CONTINUAN, y en los cuatro queda procedimiento propio a los
dos lados, que es lo que la vara 6.1 manda mirar.**

**a. `listar_debilidades_disparadores_propios` contra `identificar_disparadores_propios_reaccion`.**
**Es el par con mas riesgo de duplicado de todo el lote, y el libro define DISPARADOR dos
veces**: `L105` (*a situation that gets me more worked up than it should*) y `L233` (*they have
an outsize effect on you specifically*). Los dos nodos piden listar disparadores con preguntas.
**CONTINUA:** el hijo aniade el criterio de separacion, el uso (`L237`: cazarte y esperar cinco
minutos), la tactica de compartirlos (`L239` a `L241`) y la ubicacion del asunto (`L245`). Lo que
queda fuera en la madre tambien es procedimiento: la mitad de las debilidades, la pregunta del
critico interior, la del hada, y la regla de sede de `L95`. **Piden arista, y no la traen.**

**b. `calibrar_vision_propia_opinion_ajena` contra `pedir_opinion_otros_mejorar`.**
Los dos mandan pedir opinion sobre ti, y **los dos traen la misma pregunta de seguimiento de una
presentacion** (`L139` y `L379`). **Es el libro el que se repite**, a 240 lineas de distancia.
**CONTINUA:** el hijo aniade las dos clases, el contraste entre la pregunta inutil y la util, y
la regla de cierre de `L381` con su razon. La madre conserva los guiones, los destinatarios y el
correo entero. **Procedimiento en los dos lados, luego no hay bascula que valga.**

**c. `calibrar_vision_propia_opinion_ajena` paso 6 contra `tratar_jefe_entrenador` paso 8.**
`L123` pregunta al jefe *What opportunities do you see for me to do more of what I do well?* y
`L395` pregunta *What skills do you think I should work on in order to have more impact?*
**Dos lineas de dos secciones del mismo capitulo con la misma peticion al mismo destinatario.**
**CONTINUA los dos:** en `L123` la peticion es de calibracion y trae su segunda pregunta con
escala de uno a cinco; en `L395` es de aprendizaje y trae los otros dos movimientos.

**d. `disenar_entorno_rendir_mejor` paso 4 contra `reservar_tiempo_reflexion_metas` paso 5.**
`L219` y `L421` dicen **el mismo repaso de seis meses con metas nuevas**, en dos secciones
separadas por doscientas lineas. **Es la misma especie que el racimo del despido de mi apertura
anterior: el libro se repite y los dos nodos lo recogen.** **CONTINUA los dos**, y **piden
arista.**

**CONTRA EL GRAFO Y CONTRA LA BANDEJA VIEJA, lo que mire y sale limpio:**
`recoger_opinion_360_grados` (Cap. 4) recoge opinion **sobre tu persona a cargo**;
`calibrar_vision_propia_opinion_ajena` la recoge **sobre ti**. **No es duplicado, es espejo**, y
`L119` lo dice con sus propias palabras: *In the same way that you gather feedback for your
reports, you can learn about yourself through the following tactics.*

---

## 6. LAS ARISTAS QUE ESTA LECTURA RECLAMA, CON LA LINEA DEL LIBRO QUE LAS NOMBRA

**No las encargo aqui: las dejo escritas como lectura, porque las aristas viven en el reporte y
el reporte no lo he visto.** Las cuatro estan nombradas por el propio libro, que es lo que las
hace citables sin doctrina nueva:

| de | a | la linea que la nombra |
|---|---|---|
| `pedir_opinion_otros_mejorar` | los nodos de opinion del Cap. 4 | `L377`: *After an entire chapter on the importance of giving feedback to your reports* |
| `calibrar_vision_propia_opinion_ajena` | `recoger_opinion_360_grados` | `L119`: *In the same way that you gather feedback for your reports* |
| `listar_debilidades_disparadores_propios` | `identificar_disparadores_propios_reaccion` | `L233`: *The flip side of the coin*, que remite a la pieza anterior |
| `listar_fuerzas_propias_cuatro_preguntas` | `listar_debilidades_disparadores_propios` | `L95`: *Right beneath your list of strengths* |

**Y UNA ASIMETRIA QUE NOMBRO PORQUE ES DEL EXTRACTOR Y NO DEL LIBRO:** el paso 1 de
`pedir_opinion_otros_mejorar` **conserva** la remision de `L377`; el paso 4 de
`calibrar_vision_propia_opinion_ajena` **deja caer** la de `L119`, que es la misma especie de
frase. **Dos remisiones del libro y solo una escrita.**

---

## 7. LOS DISCUTIBLES QUE YO MARCO

*Los marco antes de ver el reporte, que es lo unico que hace informativa a la metrica
(`AUDITOR_FORJA.md` 5.1). **El 1 va marcado CONTAMINADO por 0.1** y por tanto no cuenta como
coincidencia si el extractor marco el mismo.*

### DISCUTIBLE 1 (CONTAMINADO). `conocer_fuerzas_valores_sesgos_propios`: siete pasos sobre una sola linea

**Mi lectura a ciegas es que esta pieza NO daba nodo**, y la sostengo asi:

> De sus siete pasos, **solo el paso 2 recoge algo que el libro ordena**, y sale de `L37`:
> *you first need to get deep with knowing you: your strengths, your values, your comfort
> zones, your blind spots, and your biases.* **Los pasos 4, 5, 6 y 7 no ordenan nada**: son
> `L17` a `L35` contados, y son narracion en primera persona del pasado de la que el propio
> nodo dice *el caso es suyo y no tuyo*. **Los pasos 1 y 3 son la misma linea `L37` partida.**

**Y la vara tiene un nombre exacto para esto: `P.5.1`, NOMBRAR NO ES PROCEDIMENTAR.** Los cinco
objetos que `L37` nombra **son el indice del capitulo**: fuerzas va a `listar_fuerzas_propias`,
debilidades y sesgos a `listar_debilidades_disparadores`, puntos ciegos a
`calibrar_vision_propia`, zonas de confort a `disenar_entorno_rendir_mejor`. **Una cabeza de
serie solo vale si trae doctrina suya ademas de los nombres de sus hijos**, y la unica doctrina
que aqui queda, pedirle a alguien de fuera que entreviste a tus cercanos, **ya es su propio hijo
`calibrar_vision_propia_opinion_ajena`, que lo trae con guion y con destinatarios.**

**Lo que pesa en contra de mi propia lectura, y lo escribo yo:** `L37` es la unica linea de
apertura del capitulo que ordena con *you first need to*, y dejarla sin nodo la perderia
entera. **Si la casa decide que si es nodo, entonces el remedio no es el nodo de siete pasos:
es un nodo de dos.**

### DISCUTIBLE 2. `L39` a `L61` y `L259` a `L269`: seis nodos usan dos terminos que ningun nodo define

**`sindrome del impostor` aparece en `cambiar_mentalidad_fija_crecimiento` y en
`cuestionar_historia_irracional_cabeza`. `el Pozo` aparece en SEIS candidatos.** Y las dos
piezas que los definen no tienen nodo:

    $ grep -ril "impostor" cuarentena/zhuo_manager/      2 ficheros
    $ grep -ril "Pozo" cuarentena/zhuo_manager/          7 ficheros
    $ grep -ril "Linda Hill" cuarentena/zhuo_manager/    ninguno

**Acepto que ninguna de las dos piezas es procedimiento**, y por eso NO digo que falte un nodo.
**Lo que digo es que un nodo que arranca su condicion de activacion con *Cuando estas en el
Pozo* esta apoyandose en un termino que el grafo no contiene**, y eso en un grafo que se lee
por nodo suelto es una dependencia invisible. **Es material de `D.29`, y lo dejo nombrado sin
cifra**, no como encargo.

### DISCUTIBLE 3. `pedir_ayuda_grupo_apoyo`: cinco pasos de encuadre y dos de mandato

**El contenido es fiel de principio a fin y no discuto ni una linea de traduccion.** Discuto la
proporcion: los pasos 1 a 5 son `L327` a `L333`, que es el error que ella cometio, la razon, el
dato del ochenta y dos por ciento y el circulo de Lean In. **Todo el mandato del nodo vive en
`L335`**, y lo recogen los pasos 6 y 7. **Un nodo cuyo entregable cabe en dos pasos y trae cinco
de contexto no esta mal escrito, pero esta mal repartido**, y es el sitio donde la banda ancha
de la seccion 8 muerde mas fuerte.

### DISCUTIBLE 4. El paso 8 borrado de `dar_mala_noticia_decision_tomada`, que es consecuencia de un discutible MIO

Lo escribo aqui y no solo en la seccion 4 porque **es mi propio discutible de la vuelta 10 el
que produjo este agujero**, y la seccion 5.3 me obliga a declarar mis errores con mi nombre
igual que los ajenos. Yo dije *el contenido bien, el sitio no*. **La rama elegida saco la linea
sin darle sitio nuevo, asi que `L283` de `cap_05.md` no esta hoy en ningun candidato.** Un
discutible que quita texto del libro y no lo recoloca **no es un discutible resuelto: es una
perdida de catalogo con mi firma detras.**

---

## 8. MI CUENTA DE `PASOS INVENTADOS POR CAPITULO`, EN TRES BANDAS

**Lei los 162 pasos contra su parrafo.** Y este tramo obliga a publicar bandas porque **casi la
mitad de sus pasos abren con un verbo de encuadre que el libro no escribe**:

    $ pasos totales del Cap. 5                                          162
    $ pasos que ABREN con marca de encuadre del extractor, mecanico      78   48,1 por ciento
        Ten delante 22 | Cuenta con 17 | Ten claro 9 | El libro 5 | Parte de 5
        Ten presente 4 | Usalo 4 | Mira 3 | Contrasta 2 | otros 7

| banda | que cuenta | Cap. 5 | tasa | contaminada? |
|---|---|---:|---:|---|
| **ESTRECHA**, mi vara de 1.c sin tocar | imperativo levantado sobre narracion en primera persona del pasado | **1** de 162 | **0,62 por ciento** | **no** |
| **MEDIA**, la estrecha mas los fronterizos del cambio de sujeto | lo anterior mas los pasos que ponen en segunda persona lo que el libro dice en primera | **9** de 162 | **5,56 por ciento** | **no** |
| **ANCHA**, todo verbo de encuadre que el libro no escribe | los 78 mecanicos menos 1 que si esta en el libro (`L411` *Keep in mind*) | **77** de 162 | **47,5 por ciento** | **SI, por 0.1** |

**EL UNICO PUENTE DE LA BANDA ESTRECHA, con su cita:**

> **`reservar_tiempo_reflexion_metas`, paso 8.** Ordena *Al final de cada seis meses, saca tus
> metas y evalua como lo hiciste.* **`L447` no ordena eso: lo cuenta en primera persona del
> futuro habitual**: *At the end of every six months, I'll pull up my goals and evaluate how I
> did.* Y la pieza entera de `L447` a `L449` esta en primera persona: *The important thing isn't
> the grade but what I learned. If I didn't succeed... why was that?*
>
> **Es la misma especie que el puente que encontre en la vuelta 10** y que la TAREA 1 de esta
> vuelta corrigio: imperativo levantado sobre narracion propia de la autora. **A favor del
> extractor, y lo escribo: el titulo de la pieza es imperativo del libro (`L413`, *Set Aside
> Time to Reflect and Set Goals*) y `L373` manda *maximize your learning through the following*.
> La seccion es prescriptiva en su cabeza. Lo que no es prescriptivo es el como de `L447`.**

**LOS OCHO FRONTERIZOS DE LA BANDA MEDIA, que es donde cambian de sujeto sin cambiar de modo:**

| paso | linea | que hace |
|---|---|---|
| `cambiar_mentalidad` 4 y 5 | `L145`, `L147` | *If I saw every challenge...* pasa a *Si ves cada reto...* |
| `reservar_tiempo` 9 y 10 | `L447`, `L449` | sus preguntas de balance pasan a preguntas del lector |
| `tratar_jefe_entrenador` 11 | `L397` | *When I started to see 1:1s...* pasa a *saca mas partido de las reuniones a solas* |
| `establecer_limites` 5 | `L355` | *one exercise I turn to* pasa a *Usa el ejercicio* |
| `celebrar_pequenias_victorias` 5 | `L345` | *I started a journal* pasa a *Monta un diario*. **Se salva por `L347`** |
| `convertir_cualquiera_mentor` 7 | `L407` | enunciado que pasa a prohibicion |

**Y AHORA LO QUE LA SECCION 8.3 ME OBLIGA A DECIR:**

> **LA ELECCION DE BANDA DECIDE EL VOLUMEN DEL LOTE 4, Y NO ES UN DETALLE DE REDACCION.** La
> linea base es el 36 por ciento. **Con la banda estrecha (0,62) o la media (5,56), el lote 4
> corre a un capitulo mas por vuelta. Con la ancha (47,5), el techo vuelve a UNO.** El mismo
> tramo, los mismos 162 pasos, y dos volumenes opuestos.
>
> **Mi banda media cae en 5,56, que es exactamente un valor de la serie reciente** (3,09 / 5,00
> / 5,56 / 3,80 / 5,26). **Eso me dice que la banda media es la que reproduce la serie
> historica**, y que mi banda estrecha de la vuelta 10 (0,43) ya iba baja por la misma razon.
>
> **NO FIRMO NINGUNA DE LAS TRES COMO LA CIFRA DEL ACTA, y en la ancha ni siquiera la alego**,
> porque `ultimo_extractor.json` me dijo su numero antes de que yo contara el mio. La seccion
> 8.3 dice: **si no puedes verificarla, lo dices y no la publicas como tuya.** Lo digo.

**Y LO QUE NO ES DUDA, SINO MEDIDA LIMPIA:** este tramo **cambia de estilo** respecto a los
anteriores. 78 pasos de 162 abriendo con un aparato de atribucion es una mano distinta de la
que escribio los 231 pasos del tramo anterior. **Eso es un hecho contable, no una opinion**, y
es lo que hay que reconciliar en el turno normal.

---

## 9. LO QUE ESTA LECTURA ENCUENTRA Y NO ES UN DISCUTIBLE

**El lote entero es hijo de una sola linea, y esa linea es la que yo discuto en la seccion 7.**
`L37` nombra cinco objetos y el capitulo escribe un nodo por cada uno:

    fuerzas          ->  listar_fuerzas_propias_cuatro_preguntas
    valores          ->  (el capitulo no vuelve sobre ellos: es el unico de los cinco sin hijo)
    zonas de confort ->  disenar_entorno_rendir_mejor
    puntos ciegos    ->  calibrar_vision_propia_opinion_ajena
    sesgos           ->  listar_debilidades_disparadores_propios e identificar_disparadores

**Cuatro de los cinco objetos tienen hijo y uno no.** Lo dejo escrito como lectura, no como
encargo: **es material de `D.29`, y la comprobacion de `D.37` hay que correrla abriendo el paso
de la madre, que es justo el nodo que yo discuto.**

---

## 10. LO QUE NO HE HECHO EN ESTA FASE, DICHO PARA QUE NO SE ME CUENTE COMO HECHO

- **No he corrido `forja.py`, ni el gate, ni las pruebas de aceptacion.** Esta fase es lectura.
  Van en el turno normal, y **ninguna cifra de aduana la cito hasta recomputarla.**
- **No he verificado las aristas del tramo**, porque los candidatos no las traen escritas
  (18 de 18 con `nodos_previos` y `nodos_siguientes` vacios) y viven en el reporte, que no he
  visto.
- **No he abierto `docs/loop/REPORTE.md` ni lo he recuperado de git.** **Si abri
  `ultimo_extractor.json`, y esta declarado en 0.1 como caida propia con su alcance exacto.**
- **No he tocado ningun candidato ni ningun fichero de `fuentes/`.**
- **No he contado veredictos ni sanos**, porque `MODO_INSERCION=cuarentena` y este lote no ha
  pasado por la aduana con veredicto escrito. **Las clases de la seccion 4 son MI lectura, no
  veredictos del sistema.**
- **No he adjudicado nada.** Una apertura ciega sin su comparacion no adjudica y no mueve
  credito de nadie.

**Y ESTE FICHERO NO SE VUELVE A TOCAR.** Lo sella el arnes, y el sello se verifica al terminar
mi turno (`D.34`).
