# APERTURA CIEGA DE LA VUELTA 14

*Escrita por el **auditor** ANTES de que el arnes le exponga el reporte del extractor
(`D.34`, ampliada el 11 sep 2026, `AUDITOR_FORJA.md` seccion 1 punto 5). Esta es la
lectura que despues se compara con la del extractor. **El arnes sella este fichero y lo
commitea el: yo no lo commiteo y no lo vuelvo a tocar.***

**Alcance de la vuelta que abro:** lote 4, `scott_radical_candor`, unidades `cap_00.md` a
`cap_03.md`, que es lo que el encargo de la ACTA 13 TAREA 3 manda correr.

---

## 0. LOS CUATRO FICHEROS RETIRADOS, Y QUE NO HE HECHO NADA POR RECUPERARLOS

El arnes retiro del arbol `docs/loop/REPORTE.md`, `docs/loop/loop.log`,
`docs/loop/ultimo_extractor.json` y `docs/loop/ultimo_auditor.json`. **No los he
recuperado de git, ni por `git show`, ni por `git checkout`, ni por el reflog, ni por
ninguna otra via.** Lo declaro yo aqui porque el arnes lo vigila por su cuenta.

**Y ME HE RETIRADO DOS MAS QUE NADIE ME RETIRO, y digo por que.** En la raiz del repo hay
`.informe_lote.txt` y `.informe_lote4.txt`, sin seguimiento de git y escritos a las 15:32
y 15:37 de hoy, o sea **dentro del turno del extractor de la vuelta 14**. No los he
abierto. La razon es la misma que la de la ampliacion de `D.34`: **un borrador de trabajo
del extractor escrito durante su turno es, con alta probabilidad, un resumen de lo que yo
vengo a leer a ciegas.** Prefiero declarar que existen a leerlos y tener que declarar que
los lei.

    $ git status --short docs/loop/
     D docs/loop/REPORTE.md
     D docs/loop/loop.log
     D docs/loop/ultimo_auditor.json
     D docs/loop/ultimo_extractor.json

## 1. LO QUE SI HE LEIDO, Y LA CONTAMINACION QUE DECLARO YO MISMO

He leido: `docs/loop/AUDITOR_FORJA.md` entero, `docs/loop/PROMPT_SIGUIENTE.md` (mi propio
encargo, escrito por mi antes del turno del extractor), la ACTA 13 dentro de
`docs/loop/ACTA_AUDITOR.md`, `docs/loop/ORDEN_DE_LOTES.md`,
`fuentes/FUENTES_CANONICAS.json`, las quince unidades de `fuentes/scott_radical_candor/`
en lo que toca a su cabecera y las cuatro del alcance enteras, los dos candidatos de
`cuarentena/scott_radical_candor/` y `dataset/nodos.jsonl`.

> ### **MI CEGUERA NO ES TOTAL Y NO LA VOY A VENDER COMO TOTAL**
>
> `docs/loop/ORDEN_DE_LOTES.md` **esta en el arbol y lleva dentro la fila del lote 4 que
> el extractor cerro hoy** (commit `67eacdb`, hecho a las 15:41). Esa fila ya dice **4 de
> 15 ficheros minados**, **2 candidatos**, y que las cuatro unidades son material de
> frente que no declara `Cap. N`. **Asi que he entrado sabiendo CUANTOS candidatos hay y
> DE DONDE salen.**
>
> **Lo que sigue siendo ciego, que es lo que la regla protege, es el POR QUE:** no se que
> clase les puso el extractor, ni que vecinos levanto, ni que marco discutible, ni que
> piezas descarto ni con que razon, ni que cifra de puentes publico. **Mi clasificacion
> de abajo es mia y esta hecha contra el texto fuente, no contra su cuenta.**
>
> **Lo digo yo y antes de que se me pregunte**, porque una apertura que se declara mas
> ciega de lo que fue vale menos que una que declara su rendija.

## 2. LA FRONTERA QUE CORTO YO, PIEZA A PIEZA

*Cortada por mi contra el texto, sin ver la del extractor. La unidad de cuenta es la
**linea de cuerpo no vacia**, que es la unica que se puede citar con `sed`. Las siete
primeras lineas de cada fichero son el frontmatter y no son cuerpo.*

### 2.1. `cap_00.md`, `unidad: Copyright Page`, 25 lineas de cuerpo

| lineas | pieza | mi clase |
|---|---|---|
| 9 a 31 | reclamo del ebook: Begin Reading, indice, sobre la autora, alta en boletines, avisos por correo | **SIN NODO.** Cero procedimiento de gestion |
| 33 | aviso legal de uso personal y de como notificar una infraccion | **SIN NODO.** Es una instruccion, pero al lector como comprador y no al jefe como jefe: fuera del dominio |
| 35 a 55 | bloque COPYRIGHT: editorial, sello, direccion, web, cubierta, fotografia, Library of Congress, tres ISBN, ventas a granel | **SIN NODO, Y SI FICHA.** Es el sosten documental de `FUENTES_CANONICAS.json` |
| 57 | First Edition: October 2019 | **SIN NODO, Y SI FICHA** |

**LA UNIDAD ENTERA DA CERO NODOS, Y ESO NO ES PARADA.** La condicion de parada que yo
mismo reescribi en el encargo tiene sujeto medible: *un fichero que declara `unidad: Cap.
N` en su cabecera y no da ni un procedimiento.* **`cap_00.md` declara `unidad: Copyright
Page`**, asi que se juzga, se dice que da cero y se sigue.

**Y LA FICHA LA HE CONTRASTADO CONTRA SU FUENTE PRIMARIA, que es lo unico comprobable de
esta unidad.** `FUENTES_CANONICAS.json` dice `2019`, St. Martin's Press como sello de St.
Martin's Publishing Group, Nueva York, ISBN `978-1-250-23537-4` en tapa dura y
`978-1-250-23538-1` en ebook. **Las cuatro casan linea a linea con `cap_00.md:39`, `:37`,
`:49` y `:51`.** Cero discrepancias.

**UNA IRREGULARIDAD DEL RECORTE QUE DECLARO Y NO TOCO:** `cap_00.md` es la unica unidad
de las quince cuyo frontmatter dice `libro: Radical Candor` en vez de `libro: Scott,
Radical Candor`, y cuyo campo `edicion:` no arrastra editorial ni fecha. **Las fuentes son
sagradas y no las edita el bucle** (manual principio 8): lo dejo escrito, no lo arreglo.

### 2.2. `cap_01.md`, `unidad: Preface`, 36 lineas de cuerpo

| lineas | pieza | mi clase |
|---|---|---|
| 9 | titulo de la unidad | SIN NODO |
| 11 a 23 | la parodia de Silicon Valley y lo que le enseño: algunos usaban el termino como licencia para portarse como imbeciles | **SIN NODO.** Narrativa y diagnostico del problema, sin un solo imperativo |
| 25 a 27 | la tira de Dilbert y el credito de sindicacion | **SIN NODO** |
| 29 a 33 | la palabra *radical*, y el contraste expreso con la Transparencia Radical de Ray Dalio | **SIN NODO.** Posicion doctrinal sin pasos. **`6.1`: una postura no ejecuta una busqueda** |
| **35 a 37** | **desplegar el marco: usarlo, recortarlo, fotocopiarlo, colocarlo, repartirlo, mas la regla de uso y las dos prohibiciones** | **NODO.** Es la unica pieza de la unidad con inventario de medios propio |
| 39 a 47 | COMPASSIONATE CANDOR: Paul Bloom, Joan Halifax, Jeff Weiner y el Dalai Lama | **SIN NODO.** Distincion conceptual entre empatia y compasion, sin procedimiento |
| 49 a 59 | PUT YOUR PHONE AWAY: Candor Inc., las tres versiones del software y su cierre | **SIN NODO.** Narrativa. La leccion (*guardar el movil y hablar*) es postura, no pasos |
| 61 a 69 | DIVERSITY AND INCLUSION, y las preguntas que deja para su libro siguiente | **SIN NODO.** Aqui esta la maxima *Radical Candor gets measured not at the speaker's mouth but at the listener's ear* (`:65`), **que es criterio y no procedimiento** |
| 71 a 75 | DON'T LET YOUR CULTURE BECOME TOXIC: como una cultura joven degenera en pelotear hacia arriba y patear hacia abajo | **SIN NODO, Y ES EL MAS DISCUTIBLE DE LA UNIDAD.** Ver 2.5 |
| 77 a 79 | cierre de la unidad | SIN NODO |

### 2.3. `cap_02.md`, `unidad: Introduction`, 50 lineas de cuerpo

| lineas | pieza | mi clase |
|---|---|---|
| 9 | titulo de la unidad | SIN NODO |
| 11 a 17 | el jefe terrible, la fundacion de Juice, y la llegada de Bob | SIN NODO. Narrativa |
| 19 a 39 | el caso Bob entero: el documento incoherente, los tres motivos para no decirlo, los diez meses, el contagio al equipo, el despido y la caida de Juice | **SIN NODO.** `:37` enumera sus tres omisiones, pero **en pasado y sobre si misma**: es una autopsia, no un procedimiento |
| 41 a 45 | GOOGLE: la llamada a Sheryl Sandberg y las veintisiete entrevistas | SIN NODO. Narrativa |
| 47 a 51 | Matt Cutts gritandole a Larry Page, y la sonrisa de Larry | **SIN NODO.** Es el ejemplar que motiva la doctrina, sin pasos propios |
| 53 a 59 | lo que probo en su equipo: no decidir en la reunion de staff, semanas de arreglo del directivo, sesiones de opinion sobre el directivo | **SIN NODO, Y ES EL MAS DISCUTIBLE DEL LOTE.** Ver 2.5 |
| 61 a 69 | APPLE: la clase Managing at Apple, y las estrellas de roca frente a las superestrellas | **SIN NODO, Y EL SEGUNDO MAS DISCUTIBLE.** Ver 2.5 |
| 71 a 77 | Google de abajo arriba frente a la leyenda de Jobs, y `:77` mas escuchar que decir | **SIN NODO.** `:77` es una lista de posturas comparadas, sin un solo medio |
| 79 a 93 | YOUR RELATIONSHIPS ARE CORE: Jobs sobre la critica, el *tu no eres Steve Jobs*, y el incidente de Eslovaquia con Jared Smith | **SIN NODO.** `:93` pide construir confianza y contratar a quien se adapte a tu estilo, **pero los nombra sin procedimentarlos** (`P.5.1`) |
| 95 a 107 | Silicon Valley como banco de pruebas, el impuesto del imbecil, y *las relaciones no escalan pero la cultura si* | **SIN NODO.** Tesis del libro |

**LA UNIDAD DA CERO NODOS Y LA CUENTA ES DELIBERADA, no un descuido mio.** `cap_02.md` es
la unidad mas larga de las cuatro (3.908 palabras) y **la mas rica en material que PARECE
nodo**. Ver 2.5.

### 2.4. `cap_03.md`, `unidad: How to Use This Book`, 11 lineas de cuerpo

| lineas | pieza | mi clase |
|---|---|---|
| 9 | titulo de la unidad | SIN NODO |
| 11 | a quien escribe el libro y por que cuenta tantas historias personales | SIN NODO |
| 13 | que hace la Parte I: tranquilizarte | SIN NODO. Descripcion de la estructura del libro |
| 15 | que hace la Parte II: el manual paso a paso | SIN NODO. Descripcion de la estructura del libro |
| **17** | **el reparto de la semana de cuarenta horas: diez de gestion, quince bloqueadas de trabajo propio, quince restantes** | **NODO.** Unica pieza con cifras y con un bloqueo de calendario ordenado |
| 19 | el libro tambien mira al jefe de tu jefe y a la gente de RRHH y de formacion | SIN NODO |
| 21 | diversidad y liderazgo: las diferencias hacen mas dificil la franqueza | SIN NODO. Postura |
| 23 a 29 | `PART I`, `A NEW MANAGEMENT PHILOSOPHY`, `1.`, `BUILD RADICALLY CANDID RELATIONSHIPS` | **SIN NODO, Y ES CORTE DEL RECORTE, no contenido de la unidad** |

**SOBRE ESAS CUATRO LINEAS DE COLA, y lo compruebo en vez de suponerlo.** Son los
encabezados de la parte siguiente, arrastrados al final de `cap_03.md` por donde cayo el
corte. **Podrian haber sido un solape con `cap_04.md`, y no lo son:** `cap_04.md` empieza
su cuerpo en `:9` con el subtitulo *Bringing your whole self to work*, y esos encabezados
solo viven en su frontmatter (`unidad: Cap. 1`, `titulo_textual: Build Radically Candid
Relationships`). **Cero texto de cuerpo repetido entre las dos unidades.**

    $ sed -n '9,11p' fuentes/scott_radical_candor/cap_04.md
    Bringing your whole self to work

    IT'S CALLED MANAGEMENT, AND IT'S YOUR JOB

### 2.5. LAS TRES PIEZAS QUE CASI SON NODO, Y POR QUE DECIDO QUE NO

*Las escribo con nombre porque **si el extractor saco nodo de alguna de las tres, la
discrepancia es mia y quiero que se vea de donde sale**, no inventarme despues una razon.*

**A. `cap_02.md:53`, las tres tecnicas de Google.** El texto nombra *no tomar ninguna
decision en mi reunion de staff y empujarlas a quien esta mas cerca de los hechos*,
*semanas de arreglo del directivo* y *sesiones de opinion sobre el directivo cuidadosamente
diseñadas*. **Son tres procedimientos reales y el libro se los guarda:** `:55` dice, con
todas las letras, *I'll explain all these techniques and more in the second half of this
book*. **`P.5.1` congelada: nombrar no es procedimentar.** Un nodo aqui seria un nodo de
tres titulos sin un solo medio, y ademas seria la madre condenada a ser duplicado de los
capitulos que si los explican. **SIN NODO, y con la fecha de vencimiento puesta: esto
vuelve en `cap_04` a `cap_11`.**

**B. `cap_02.md:67`, estrellas de roca y superestrellas.** Trae la distincion entera y
trae su consecuencia (*She was explicit about needing a balance of both*), y la autora
declara que en Google habia infravalorado a las primeras. **Pero no dice como se
identifican, ni como se equilibran, ni que se hace distinto con unas y con otras.** Es un
instrumento de diagnostico anunciado, no ejecutable. **SIN NODO.**

**C. `cap_01.md:73`, la deriva de la cultura a toxica.** Es la pieza mejor construida de
las tres: tiene mecanismo con direccion (el equipo crece, el desafio directo se hace
incomodo, se retrocede a la empatia ruinosa, la agresion odiosa gana porque es mas eficaz
que la empatia ruinosa, los demas se refugian en la insinceridad manipuladora, y sale el
pelotear hacia arriba y patear hacia abajo). **Y aun asi no manda hacer nada.** `6.1` lo
zanja: *un mapa sin sentidos no es medio mapa.* **SIN NODO.**

**LAS TRES SON DE LA MISMA ESPECIE Y ESO ME DA CONFIANZA EN EL CORTE:** material de frente
que anuncia doctrina que el libro procedimenta despues. **Un lote 4 cuyas cuatro primeras
unidades dan dos nodos de dieciseis pasos no es un lote pobre: es un prologo haciendo de
prologo.**

### 2.6. COBERTURA, MEDIDA A MAQUINA Y CON RESIDUO

*La forma que yo mismo encargue en la TAREA 1.d: total, filtrado y residuo, los tres
pegados. Me la aplico a mi.*

    $ python ...  # cuenta lineas de cuerpo no vacias por unidad
    cap_00.md  totales   58  frontmatter 7  cuerpo   51  no vacias   25  vacias   26
    cap_01.md  totales   80  frontmatter 7  cuerpo   73  no vacias   36  vacias   37
    cap_02.md  totales  108  frontmatter 7  cuerpo  101  no vacias   50  vacias   51
    cap_03.md  totales   30  frontmatter 7  cuerpo   23  no vacias   11  vacias   12
    lineas de cuerpo NO VACIAS en cap_00..cap_03 : 122

| unidad | lineas | cubiertas por mis piezas | con nodo | sin nodo |
|---|---:|---:|---:|---:|
| `cap_00.md` | 25 | 25 | 0 | 25 |
| `cap_01.md` | 36 | 36 | 2 | 34 |
| `cap_02.md` | 50 | 50 | 0 | 50 |
| `cap_03.md` | 11 | 11 | 1 | 10 |
| **total** | **122** | **122** | **3** | **119** |

**122 de 122, cero huecos y cero solapes en MI corte**, y **3 mas 119 son 122**, que es el
residuo que hace comprobable la cifra.

## 3. LOS DOS CANDIDATOS: MI CLASE, POR LECTURA Y NO POR SEÑAL

### 3.0. LOS OBJETOS CON LOS QUE BUSQUE VECINOS, Y LA LISTA VA PUBLICADA

*Remedio mecanico que me escribi en la ACTA 13 seccion 6.3, adoptado del extractor: **la
busqueda va por los OBJETOS DEL CAPITULO sobre los 135 titulos, no por las palabras del
candidato**, y la lista de objetos se publica para que se pueda comprobar que no elegi los
que me convenian. **Una busqueda negativa solo se puede citar junto al criterio con el que
se hizo.***

**Diecisiete objetos, barridos sobre los 135 titulos de `dataset/nodos.jsonl`**, y estos
son los cubos con sus tamaños: marco de dos ejes o cuadrantes (3), opinion darla pedirla
medirla (12), recordatorio a la vista o difundir un texto (4), conversacion individual (4),
relacion y confianza con la persona a cargo (7), cultura y su deriva (5), tiempo del jefe y
calendario (10), trabajo propio de experto frente a gestion (5), equipo que crece y
transicion (8), juzgar o clasificar personas en casillas (12), diversidad y sesgo (4),
ambicion y ritmo de crecimiento (6), bajo rendimiento y despido (7), elogio frente a
critica (5), contratar a quien encaja con tu estilo (13), empujar la decision a quien esta
cerca de los hechos (7), ficha bibliografica y fuente canonica (2).

**De ahi saque los ocho vecinos cuyos pasos abri enteros antes de adjudicar:**
`planificar_reduccion_trabajo_individual`, `reservar_media_hora_semanal_talento`,
`reservar_tiempo_reflexion_metas`, `establecer_limites_cuidado_personal`,
`repartir_tiempo_atencion_mejores_equipo`, `elegir_forma_inspirar_cambio_conducta`,
`calificar_tarjeta_puntuacion_habilidad_voluntad`, `comunicar_vision_jugadores_organizacion`.
**Imprimi sus pasos PRIMERO y adjudique despues**, que es el orden que manda `1.2`.

### 3.1. `desplegar_marco_franqueza_radical`, de `cap_01.md:35` y `:37`

**MI CLASE: `SANO`.**

**LA LECTURA DE FIDELIDAD, PASO A PASO CONTRA SU LINEA.** Nueve pasos escritos, y los
nueve los pongo contra el texto:

| paso | linea que lo sostiene |
|---:|---|
| 1 usar la version nueva del marco | `:35` *use this new version of the Radical Candor framework* |
| 2 recortarlo del libro, version mayor en la pagina 297 | `:35` *You can cut it right out of this book (see page 297 for a larger version)* |
| 3 hacer fotocopias | `:35` *make photocopies* |
| 4 ponerlas en la nevera, sobre la mesa o donde sea, de recordatorio | `:35` *put them on your refrigerator, over your desk, or anywhere for a reminder* |
| 5 repartir copias a los colegas | `:35` *You can also share copies with your colleagues* |
| 6 usarlo como brujula de conversaciones concretas | `:37` *like a compass to guide individual conversations to a better place* |
| 7 no usarlo como test de personalidad | `:37` *do NOT use it as a personality test to judge yourself or others* |
| 8 no escribir nombres en las casillas | `:37` *Don't write names in boxes* |
| 9 todos caemos en cada cuadrante varias veces al dia | `:37` *We all fall into each quadrant multiple times a day* |

**Nueve de nueve TRANSCRIPCION. Cero puentes.** Y la condicion de activacion tambien es
transcripcion (`:35`, *if you are rolling out Radical Candor, and you think there might be
some confusion about what it means*).

**EL FORMULARIO DE LA ACTA 13 SECCION 6.2, que escribo aunque la clase sea `SANO`.** El
remedio solo obliga a rellenarlo cuando la clase NO es `SANO`; **lo relleno igual, porque
el hueco de la PRUEBA 2 es exactamente lo que me hizo caer dos veces en la vuelta 13 y
dejarlo en blanco cuando sale `SANO` es volver a no aplicarla.**

    PRUEBA 1 (descarta REPITE): fuera del solape hay procedimiento en los dos lados? SI.
      El vecino mas cercano por objeto es comunicar_vision_jugadores_organizacion (lanzar
      un mensaje y reforzarlo en cada comunicacion). Fuera del solape, la madre tiene
      tres formulaciones de mensaje y el respaldo con actos; el hijo tiene recorte,
      fotocopia, colocacion, reparto y dos prohibiciones. Procedimiento en los dos lados.
    PRUEBA 2 (decide SANO/CONTINUA): que linea de la madre ejecuta el hijo, y en cuantos
      pasos? NINGUNA. No puedo nombrar una linea concreta de comunicar_vision... ni de
      formular_codigo_comercializacion_empresarial ni de elegir_forma_inspirar_cambio_
      conducta que este candidato ejecute. La madre de Who difunde UN MENSAJE por la via
      de repetirlo; este difunde UN OBJETO FISICO por la via de fotocopiarlo. Y la de
      Zhuo clasifica CUATRO PRACTICAS DE OPINION, no cuatro modos de conducta.
      Sin linea que nombrar, la clase es SANO.

### 3.2. `repartir_semana_cuarenta_horas_jefe`, de `cap_03.md:17`

**MI CLASE: `SANO`.**

**LA LECTURA DE FIDELIDAD.** Siete pasos, los siete contra la misma linea `:17`, que es
una linea larga y da para los siete:

| paso | fragmento que lo sostiene, todo en `cap_03.md:17` |
|---:|---|
| 1 puede que te sientas abrumado; respira hondo | *you might occasionally feel overwhelmed... Take a deep breath* |
| 2 la meta es ahorrarte tiempo, no llenarte el calendario | *My goal is to save you time, not to litter your calendar with meetings* |
| 3 tiempo con tus personas a cargo si, todo tu tiempo no | *You do need to spend time with your direct reports... but you don't need to spend ALL your time with them* |
| 4 diez horas semanales si aplicas cada idea, herramienta y tecnica | *approximately ten hours a week* |
| 5 esas diez horas te ahorran despues tiempo perdido y quebraderos | *those ten hours should save you enormous lost time and headaches later* |
| 6 bloquear unas quince horas de trabajo propio de experto | *block out about fifteen hours a week for you to think and execute independently* |
| 7 las otras quince, y la mayoria se van en lo imprevisible | *That leaves another fifteen hours in a forty-hour work week... deal with the unpredictable* |

**Siete de siete TRANSCRIPCION. Cero puentes.** **Y la aritmetica tampoco es puente**: es
el propio texto el que cierra la suma, *That leaves another fifteen hours in a forty-hour
work week*. Diez mas quince mas quince son cuarenta, **y el que suma es el libro**.

**LA ATRIBUCION QUE EL CANDIDATO TRAE, verificada por mi.** Dice `fecha_corte: "no consta
la fecha en el texto: la unidad no data la cifra, y este recorte no incluye las notas del
libro"`. **Las dos mitades son ciertas y las dos las he comprobado:** `cap_03.md` no data
la cifra en ninguna de sus once lineas, y **el recorte no tiene unidad de notas**, cosa que
se ve recorriendo las quince cabeceras (`cap_12` es `Getting Started`, `cap_13` es
`Afterword`, `cap_14` es `Bonus Chapter`; no hay `Notes`, ni `Index`, ni
`Acknowledgments`).

    PRUEBA 1 (descarta REPITE): fuera del solape hay procedimiento en los dos lados? SI.
      El vecino mas cercano por objeto es planificar_reduccion_trabajo_individual (Zhuo).
      Fuera del solape la madre tiene su disparador con numero (cuando el equipo llega a
      cuatro o cinco personas) y el error que vigila; el hijo tiene las tres partidas
      cifradas y el bloqueo de calendario. Procedimiento en los dos lados.
    PRUEBA 2 (decide SANO/CONTINUA): que linea de la madre ejecuta el hijo, y en cuantos
      pasos? NINGUNA, y aqui esta la trampa que casi me come. La madre manda REDUCIR el
      trabajo de contribuidor individual segun crece el equipo; el hijo le RESERVA quince
      horas fijas a perpetuidad. El hijo no ejecuta el paso 3 de la madre: no lleva mas
      lejos ese plan de reduccion, describe otro reparto con otro sujeto (el jefe ya
      asentado, no el directivo nuevo en transicion). Sin linea que nombrar, SANO.
      Y lo mismo contra reservar_media_hora_semanal_talento, reservar_tiempo_reflexion_
      metas, establecer_limites_cuidado_personal y repartir_tiempo_atencion_mejores_
      equipo: los cinco comparten la FORMA (reservar tiempo en el calendario con una
      cifra) y ninguno comparte el OBJETO. La forma es señal, y D.19 dice que una
      discrepancia nunca se adjudica citando una señal.

### 3.3. LOS DOS ROCES QUE EXAMINE Y QUE **NO** SON FRONTERA DECLARADA

*Los escribo porque `6.1` dice que una frontera se pierde por poda, y **declarar de mas
tambien la estropea**: si llamo frontera a todo roce, la palabra deja de significar.*

**ROCE 1: `cap_01.md:37` contra `calificar_tarjeta_puntuacion_habilidad_voluntad` (Who).**
Scott prohibe escribir nombres en las casillas de su marco de dos ejes; Smart califica a
las personas con A, B o C sobre un marco de dos ejes (habilidad y voluntad). **Parece la
misma palanca y no lo es**, y la razon la da la propia Scott en la linea siguiente: *We all
fall into each quadrant multiple times a day.* **Sus cuadrantes clasifican MOMENTOS DE
CONVERSACION, no personas**; los de Smart califican **el encaje de un candidato con una
tarjeta de puesto concreta**, para una decision de contratacion. **Prohibir clasificar
personas con un marco de conducta no contradice calificar candidatos con un marco de
encaje. NO ES FRONTERA.**

**ROCE 2: `cap_03.md:17` contra `planificar_reduccion_trabajo_individual` (Zhuo).** Zhuo
manda reducir el trabajo de contribuidor individual; Scott reserva quince horas semanales
para pensar y ejecutar por tu cuenta en tu area de especialidad. **Suena a contradiccion y
no lo es:** lo que Zhuo manda soltar es la entrega del equipo hecha por el jefe, y lo que
Scott bloquea es tiempo de pensar y de aportar como experto. **Pueden ser verdad las dos a
la vez en la misma semana. NO ES FRONTERA**, y lo dejo escrito por si `cap_04` a `cap_11`
lo tensan de verdad, que es donde esperaria la frontera si la hay.

**Y LA FRONTERA QUE YA ESTA DECLARADA NO SE REABRE.** El encargo dejo escrito que
`revisar_incentivos_trampas_equipo` contra `reconocer_recompensar_uso_metodo` es FRONTERA
DECLARADA sobre atar dinero a un numero, y que **si en `scott_radical_candor` aparece un
tercer libro tirando de esa palanca, se le añade y no se reabre.** **En `cap_00` a `cap_03`
no aparece:** ninguna de las 122 lineas habla de retribucion variable ni de atar dinero a
una tasa.

## PUENTES SUPERVIVIENTES EN LOS FICHEROS (poblacion ciega; NO es PASOS INVENTADOS POR CAPITULO)

*Encabezado literal obligatorio, ACTA 13 seccion 6.1. **La poblacion va en la misma linea
del titulo**: lo que cuento son los puentes que SOBREVIVEN en los dos ficheros commiteados
de `cuarentena/scott_radical_candor/`, que es lo unico medible a ciegas. **La cifra del
extractor, que cuenta tambien los puentes que el mismo cazo y corrigio dentro de su turno,
es otra poblacion y se firma en mi turno normal con el reporte delante.***

    $ python ... # cuenta pasos por candidato, con residuo
    desplegar_marco_franqueza_radical          pasos   9
    repartir_semana_cuarenta_horas_jefe        pasos   7
    TOTAL de pasos escritos en el lote 4 hasta hoy : 16
      de ellos TRANSCRIPCION (casan linea a linea) : 16
      de ellos PUENTE (sin linea que los sostenga) : 0
      residuo 16 + 0 = 16  == 16  True

| unidad | candidatos | pasos escritos | puentes supervivientes | por ciento |
|---|---:|---:|---:|---|
| `cap_00.md` Copyright Page | 0 | 0 | 0 | **sin definir, denominador cero** |
| `cap_01.md` Preface | 1 | 9 | 0 | **0,00** |
| `cap_02.md` Introduction | 0 | 0 | 0 | **sin definir, denominador cero** |
| `cap_03.md` How to Use This Book | 1 | 7 | 0 | **0,00** |
| **las cuatro juntas** | **2** | **16** | **0** | **0,00** |

**CERO PUENTES SUPERVIVIENTES EN LOS DIECISEIS PASOS**, comprobados uno a uno contra su
linea en las tablas 3.1 y 3.2. **Y digo lo que esta cifra NO puede decir a ciegas:** no se
cuantos puentes escribio el extractor y corrigio dentro de su propio turno, porque eso solo
vive en su reporte. **Si su reporte declara puentes propios cazados, su cifra sera mas alta
que mi 0,00 y las dos seran ciertas**, porque miden poblaciones distintas. **Lo mismo paso
en la vuelta 13 y lo escribo antes de mirar, no despues.**

**EL FRENO NO SE DISPARA CON LO QUE YO VEO.** El tope es 10 por ciento sobre el **peor
capitulo** (`8.1`, `8.2`), y el peor capitulo con denominador no nulo mide **0,00**.

## 4. MIS CIFRAS, CADA UNA CON EL COMANDO QUE LA SACO

*`1.1`: el instrumento manda, y toda cifra que publico se lee de una corrida de ESTA
vuelta. Estas son mias y las firmo.*

| cifra | valor | de donde sale |
|---|---:|---|
| lineas de cuerpo no vacias en `cap_00` a `cap_03` | **122** | corrida de 2.6, desglosada 25 + 36 + 50 + 11 |
| piezas en que corto esas lineas | **32** | tablas 2.1 a 2.4 |
| piezas con nodo | **2** | `cap_01.md:35` a `:37` y `cap_03.md:17` |
| candidatos en la bandeja del lote 4 | **2** | `ls cuarentena/scott_radical_candor/*.json \| wc -l` |
| pasos escritos en esos candidatos | **16** | 9 + 7, corrida de la seccion de puentes |
| puentes supervivientes | **0** | tablas 3.1 y 3.2, paso a paso contra su linea |
| nodos vivos en el grafo | **135** | `wc -l dataset/nodos.jsonl` |
| palabras del recorte entero | **108.161** | recuento propio sobre las quince unidades |
| palabras de `cap_04` a `cap_11` | **81.508** | mismo recuento |
| palabras de `cap_00` a `cap_03` | **7.599** | mismo recuento |

**LAS PALABRAS LLEVAN RESIDUO Y POR ESO SON COMPROBABLES:** 7.599 mas 81.508 mas 19.054 de
`cap_12` a `cap_14` dan **108.161** exactos. **Esto verifica de paso dos cifras que
`ORDEN_DE_LOTES.md` publica** (las 108.161 del lote y las 81.508 de los ocho capitulos
numerados) **contra mi propio recuento, y casan las dos.**

**Y VERIFICO UNA TERCERA AFIRMACION DE ESA FILA, la de los sujetos:** las cuatro unidades
del alcance declaran `Copyright Page`, `Preface`, `Introduction` y `How to Use This Book`,
y **ninguna declara `Cap. N`**; los ocho que si lo declaran son `cap_04` a `cap_11`,
`Cap. 1` a `Cap. 8`. **Leido de las quince cabeceras, no copiado de la fila.**

## 5. LO QUE NO PUEDO VERIFICAR A CIEGAS, Y NO LO PUBLICO COMO MIO

*`8.3`: si no puedes verificarla, lo dices y no la publicas como tuya.*

1. **La cifra de puentes del extractor**, que incluye los que cazo y corrigio en su turno.
   Poblacion distinta de la mia. **A verificar con el reporte delante.**
2. **Si los dos candidatos pasaron la aduana en el acto en que se escribieron** o al final,
   que es lo que el encargo pedia. **No se ve en el fichero: se ve en el reporte.**
3. **Si el extractor levanto los mismos vecinos que yo**, y si marco discutible alguno de
   los dos. **Mis dos `SANO` salen sin saberlo.**
4. **Si `cap_00.md` tiene palabras declaradas en el MANIFIESTO del mundo 11**, que
   `FUENTES_CANONICAS.json` dice que no. **Mi recuento le da 218 palabras de cuerpo y esas
   218 estan dentro de las 108.161**, asi que la frase de la ficha y mi total conviven solo
   si el manifiesto y el total se cuentan distinto. **Lo dejo marcado y lo traigo al turno
   normal; no lo llamo caida sin haber abierto el manifiesto.**
5. **El total de puentes del lote 3 y su tabla de doce capitulos**, que la TAREA 2.c
   encargaba. **No es material de esta apertura: se firma con el reporte.**

## 6. LO QUE ESPERO ENCONTRAR EN EL REPORTE, ESCRITO ANTES DE VERLO

*Para que la comparacion mida algo, la prediccion tiene que estar sellada antes.*

- **Dos candidatos y no mas**, de `cap_01` y de `cap_03`. **Confianza alta**, y con la
  rendija de la seccion 1 declarada.
- **`cap_00` y `cap_02` con cero nodos y juzgados sin parar.** **Confianza alta en
  `cap_00`**, que es pagina de copyright. **Media en `cap_02`**, porque `:53` y `:67` son
  material que un extractor razonable podria haber convertido en nodo. **Si saco nodo de
  `:53`, el discutible es bueno y yo defiendo mi SIN NODO citando `:55` y `P.5.1`.**
- **Los dos candidatos sin vecino que los absorba.** Espero que su aduana levante vecinos
  (con 135 nodos los levanta siempre) **y que los resuelva en `SANO` los dos**. **Si me
  trae un `CONTINUA` sobre `planificar_reduccion_trabajo_individual`, ese es el choque de
  la vuelta**, y mi PRUEBA 2 de 3.2 es lo que llevo a esa mesa.
- **Cero puentes supervivientes.** Si declara puentes propios cazados dentro del turno,
  **eso no me contradice y es la regla funcionando** (`8.4`).
- **El aviso de alcance cumplido:** el encargo mandaba cuatro unidades y hay cuatro
  minadas. **No espero tareas abiertas por corte de turno**, que es lo que rompio la
  vuelta 13.

---

**FIN DE LA APERTURA CIEGA DE LA VUELTA 14.** No he leido el reporte, no lo he recuperado
de git, y no he abierto los dos borradores sin seguimiento del turno del extractor. **No
commiteo: sella y commitea el arnes.** Y no vuelvo a tocar este fichero, porque el sello se
verifica al terminar mi turno y un sello roto detiene la corrida.
