# APERTURA CIEGA DE LA VUELTA 33, lote 4 (`scott_radical_candor`), insercion de `cap_08`

*Escrita antes de que el arnes me exponga `docs/loop/REPORTE.md`. Los cuatro ficheros que
`D.34.2` retira (`REPORTE.md`, `loop.log`, `ultimo_extractor.json`, `ultimo_auditor.json`)
**no estan en el arbol y no los he recuperado de git ni por ninguna otra via**. Si he abierto
`docs/loop/ACTA_AUDITOR.md`, que es obra mia y no del extractor y que `D.40` manda leer.*

    ACTA ANTERIOR LEIDA: 6e911728e6b1151e6e4d32d4d60fd84a09e75572
    HEREDADO 1: CUMPLIDO
    HEREDADO 2: CUMPLIDO
    HEREDADO 3: CUMPLIDO
    HEREDADO 4: CUMPLIDO

**LAS CUATRO SON `CUMPLIDO`, ASI QUE NINGUNA NECESITA EL MOTIVO NI LA SALIDA PEGADA QUE `D.40`
EXIGE A UN `NO APLICA`.** Cada una lleva igualmente debajo, en `0.1`, el comando que la sostiene.

---

## 0.1. LOS CUATRO HEREDADOS, CON LA PRUEBA DEBAJO Y NO SOLO LA PALABRA

### **HEREDADO 1: CUMPLIDO.** Toda cifra de esta pagina dice, en su encabezado, la poblacion y el estado del arbol que el instrumento midio

**Es el remedio que me escribi yo por el encabezado de la `ACTA 31` `1.2`**, que nombraba un
hash cuyo clon limpio daba otra cosa. Aqui el encabezado de cada tabla nombra **el arbol
`1ae327e` SUCIO**, con los cuatro ficheros del arnes fuera, y **la poblacion exacta** de la
corrida de debajo, y las dos las mide un instrumento y no yo:

    $ python .v33a/poblacion.py
    POBLACION MEDIDA HOY. arbol: 1ae327e  ficheros con cambio sin commitear: 7

      dataset/nodos.jsonl            :  282 nodos
      bitacora/VEREDICTOS.jsonl      :  410 lineas
      config/pares_mutuos.jsonl      :    1 lineas

      cuarentena/ensayo_referencia_163        bandeja 163   _insertados   0
      cuarentena/marquet_turn_the_ship        bandeja   3   _insertados   0
      cuarentena/onu_consumidor               bandeja   0   _insertados   6
      cuarentena/scott_radical_candor         bandeja  63   _insertados  79
      cuarentena/smart_who                    bandeja   0   _insertados  59
      cuarentena/zhuo_manager                 bandeja   0   _insertados 136
      TOTAL de cuarentena/                    bandeja 229   _insertados 280

**LOS `7` FICHEROS SIN COMMITEAR SON LOS DEL PROPIO ARNES**, y los pego porque forman parte del
estado del arbol que todas estas cifras midieron:

    $ git status --porcelain
     D docs/loop/APERTURA_CIEGA.md
     D docs/loop/REPORTE.md
     D docs/loop/loop.log
     M docs/loop/ultimo_apertura.json
     D docs/loop/ultimo_auditor.json
     D docs/loop/ultimo_extractor.json
    ?? .v33a/

### **HEREDADO 2: CUMPLIDO.** Todo recuento con el que contrasto una tabla ajena lo genero del dato

El ejemplar es `5.1`: el `resumen_teorico` de un nodo dice que tres capitulos no estan minados,
y **no lo compruebo leyendo ese resumen ni ninguna tabla: abro `dataset/nodos.jsonl` y cuento**.

    $ python .v33a/capitulos.py
    NODOS DE scott_radical_candor EN EL GRAFO, por capitulo del fichero fuente
      (el capitulo se saca del patron cap_NN.md dentro del resumen_teorico; dataset de 282 nodos)

      fichero      en fuentes/     nodos    pasos
      cap_00.md    SI                  0        0
      cap_01.md    SI                  1        9
      cap_02.md    SI                  0        0
      cap_03.md    SI                  1       10
      cap_04.md    SI                  5       41
      cap_05.md    SI                  8       76
      cap_06.md    SI                 10      117
      cap_07.md    SI                 25      225
      cap_08.md    SI                 12      102
      cap_09.md    SI                  0        0
      cap_10.md    SI                  0        0
      cap_11.md    SI                 16      187
      cap_12.md    SI                  0        0
      cap_13.md    SI                  0        0
      cap_14.md    SI                  0        0

      nodos de scott en el grafo: 79   sin capitulo legible en su resumen: 1

**LA FILA DE `cap_11` ES LA CIFRA QUE MI PROPIA `ACTA 31` `4.1` CORRIGIO**, `187` pasos en `16`
nodos, **y la vuelvo a generar del dato en vez de copiarla de mi acta**, que es justo lo que este
remedio pide.

### **HEREDADO 3: CUMPLIDO.** Mis clases estan escritas a fichero ANTES de la primera corrida que imprime una razon, y lo mido

    $ cat .v33a/hora_clases.txt
    FICHERO DE CLASES ESCRITO: .v33a/mis_clases.txt
    HORA DEL FICHERO (mtime): 2026-09-17 08:17:27
    bytes: 5809
    SEGUNDO BLOQUE ANEXADO. hora del fichero: 2026-09-17 08:22:57   bytes: 10827

    $ python .v33a/destapar.py 5 | head -1
    == DESTAPADA LA RAZON 5 DE 14, a las 2026-09-17 08:23:12 ==

**`08:22:57` es anterior a `08:23:12`, y las dos horas las estampa la maquina y no yo.** Entre
una y otra no hay ninguna corrida que imprima una razon: los dos instrumentos que leen la
bitacora antes de esa hora (`.v33a/bitacora.py` y `.v33a/pares.py`) **imprimen el par, el
veredicto y la senial, y de la razon solo su longitud en caracteres**, que es exactamente lo que
`AUDITOR_FORJA.md` `1.2` deja mirar antes de adjudicar.

### **HEREDADO 4: CUMPLIDO.** Ningun instrumento mio lleva una lista de ids tecleada, y su primera linea lo dice

    $ head -2 .v33a/tanda.py
    # PRIMERA LINEA (HEREDADO 4): CERO IDS TECLEADOS. La tanda sale de git diff entre
    # ef3e7f9 (commit anterior a la apertura de la vuelta 33) y HEAD, sobre el dato.

Los doce ids de la tanda salen de un `git diff` del dataset; los capitulos, de un patron buscado
dentro del propio dato; los rotulos del capitulo, del fichero fuente por forma; los vecinos, del
campo `vecino` de la bitacora. **Lo unico tecleado en toda la fase son dos cosas, y las dos son
el SUJETO del instrumento y no una celda de su mapeo:** el nombre del fichero fuente
`fuentes/scott_radical_candor/cap_08.md`, y la huella `ef3e7f9`, que es el punto de corte que el
propio prompt define como *antes de la vuelta 33*.

---

## 1. EL ARBOL QUE MIDO, Y EL PUNTO DE CORTE

| | **medido hoy, arbol `1ae327e` sucio con los `7` del arnes** |
|---|---|
| `HEAD` | `1ae327e30a96dff65c7edc9b3a3c35a1b4d1f261` |
| **antes de la vuelta 33** | `ef3e7f9d498fe8afee4decd57981d853e2a4458b`, el commit anterior a `9b36072`, que es la apertura del arnes |
| rama | `extraccion-mundo-11` |

    $ git rev-parse 9b36072^
    ef3e7f9d498fe8afee4decd57981d853e2a4458b

**HUECO DE ACTA (`AUDITOR_FORJA.md` 1.0): NO HAY.** Mi ultima acta es la `ACTA 31` y cubre la
**vuelta 32**; la vuelta que voy a auditar es la **33**, la inmediatamente siguiente. **No tengo
ninguna vuelta sin acta que recoger.**

---

## 2. LA TANDA, SACADA DEL DATO Y NO DE UNA LISTA

**Encabezado (`HEREDADO 1`): `dataset/nodos.jsonl` entre `ef3e7f9` y `1ae327e`, de `270` a `282`
nodos.**

    $ python .v33a/tanda.py
    NODOS QUE ENTRAN AL GRAFO EN LA VUELTA 33 (dataset/nodos.jsonl, ef3e7f9 -> HEAD)
      antes: 270 nodos   ahora: 282 nodos   ENTRAN: 12   salen: 0
       1  integrar_trabajo_vida_mejor_version
       2  definir_receta_propia_mantenerse_centrado
       3  agendar_cuidados_propios_cumplirlos
       4  ceder_autoridad_unilateral_equipo
       5  dominar_arte_socializar_trabajo
       6  evitar_presion_social_actos_equipo
       7  construir_confianza_equipo_tiempo_solas
       8  vivir_valores_propios_evitar_listarlos
       9  demostrar_apertura_visiones_distintas
      10  manejar_contacto_fisico_regla_platino
      11  reconocer_emociones_propias_avisar_equipo
      12  dominar_reacciones_emociones_ajenas

    FICHEROS DE cuarentena/ QUE SE MUEVEN EN LA VUELTA 33: 12 lineas de git diff --name-status

**Encabezado (`HEREDADO 1`): los mismos `12` ids leidos de `dataset/nodos.jsonl` con `282` nodos,
arbol `1ae327e`.**

    $ python .v33a/procedencia.py
      id                                           pasos  fuente                   localizador
      integrar_trabajo_vida_mejor_version              5  scott_radical_candor     (sin localizador)
      definir_receta_propia_mantenerse_centrado        9  scott_radical_candor     (sin localizador)
      agendar_cuidados_propios_cumplirlos              5  scott_radical_candor     (sin localizador)
      ceder_autoridad_unilateral_equipo               15  scott_radical_candor     (sin localizador)
      dominar_arte_socializar_trabajo                  9  scott_radical_candor     (sin localizador)
      evitar_presion_social_actos_equipo               6  scott_radical_candor     (sin localizador)
      construir_confianza_equipo_tiempo_solas          7  scott_radical_candor     (sin localizador)
      vivir_valores_propios_evitar_listarlos           9  scott_radical_candor     (sin localizador)
      demostrar_apertura_visiones_distintas           10  scott_radical_candor     (sin localizador)
      manejar_contacto_fisico_regla_platino            9  scott_radical_candor     (sin localizador)
      reconocer_emociones_propias_avisar_equipo        7  scott_radical_candor     (sin localizador)
      dominar_reacciones_emociones_ajenas             11  scott_radical_candor     (sin localizador)

      TOTAL de pasos_accionables en los 12 nodos que entran: 102

> **`LECTURA`, marcada aparte de la cifra (`D.38.3` ensanchada, 16 sep 2026):** el campo
> `fuentes` de un nodo **no guarda el capitulo**, solo la clave del libro. El capitulo hay que
> sacarlo del `resumen_teorico`, que es prosa. **Lo digo porque es lo que obligo a mi instrumento
> a casar por patron en vez de por campo**, y porque una casa que publica `PASOS INVENTADOS POR
> CAPITULO` en cada acta no tiene el capitulo en ningun campo del esquema.

---

## 3. EL CAPITULO, LEIDO ENTERO ANTES QUE LOS NODOS

`fuentes/scott_radical_candor/cap_08.md`, `189` lineas, cuyo frontmatter declara **`unidad: Cap.
5`, `titulo_textual: Relationships`, `fidelidad: verbatim`**. Lo he leido entero.

**Encabezado (`HEREDADO 1`): rotulos sacados por forma del fichero de `189` lineas; los nodos que
los cubren, de `dataset/nodos.jsonl` con `282` nodos, arbol `1ae327e`.**

    $ python .v33a/rotulos.py
      linea rotulo                                               cuerpo nodo del grafo que lo cubre
      L9    An approach to establishing trust with your direct r 5      --- NINGUNO ---
      L15   STAY CENTERED                                        9      --- NINGUNO ---
      L25   Work-life integration                                3      integrar_trabajo_vida_mejor_version
      L29   Figure out your recipe to stay centered and stick    7      definir_receta_propia_mantenerse_centrado
      L37   Calendar                                             3      agendar_cuidados_propios_cumplirlos
      L41   Show up for yourself                                 3      agendar_cuidados_propios_cumplirlos
      L45   FREE AT WORK                                         21     ceder_autoridad_unilateral_equipo
      L67   MASTER THE ART OF SOCIALIZING AT WORK                9      dominar_arte_socializar_trabajo
      L77   Even non-mandatory events can feel mandatory         5      evitar_presion_social_actos_equipo
      L83   Booze                                                5      --- NINGUNO ---
      L89   RESPECT BOUNDARIES                                   3      --- NINGUNO ---
      L93   Building trust                                       3      construir_confianza_equipo_tiempo_solas
      L97   Sharing values                                       7      vivir_valores_propios_evitar_listarlos
      L105  Demonstrating openness                               17     demostrar_apertura_visiones_distintas
      L123  Physical space                                       9      manejar_contacto_fisico_regla_platino
      L133  Were you weirded out that a strange man hugged and   17     manejar_contacto_fisico_regla_platino
      L151  Recognizing your own emotions                        9      reconocer_emociones_propias_avisar_equipo
      L161  Master your reactions to others emotions             27     dominar_reacciones_emociones_ajenas
      L189  GUIDANCE                                             0      --- NINGUNO ---

      rotulos cubiertos por un nodo: 14   sin nodo: 5
      nodos distintos de cap_08 en el grafo: 12

> **`LECTURA`, marcada aparte de la cifra:** de los `19` que el instrumento saca por forma,
> **tres NO son piezas del capitulo, y los descarto yo leyendo y no la maquina**: `L9` es el
> subtitulo del capitulo, `L133` es una linea de dialogo dentro del tramo de `Physical space`, y
> `L189` es el titulo del capitulo SIGUIENTE. **Quedan `16` rotulos de rango de pieza**, de los
> cuales **`13` tienen nodo** y **`12` nodos los cubren**, porque `L37` y `L41` caen en el mismo.
> **Y quedan TRES rotulos de pieza SIN nodo: `L15` `STAY CENTERED`, `L83` `Booze` y `L89`
> `RESPECT BOUNDARIES`.** Los tres los clasifico yo en `5.3`.

---

## 4. MI CLASE PARA CADA UNO DE LOS DOCE, ESCRITA A CIEGAS

**El fichero es `.v33a/mis_clases.txt`, con su hora publicada en `0.1`, y va pegado aqui sin
tocarlo.**

    $ sed -n '13,26p' .v33a/mis_clases.txt
     1 integrar_trabajo_vida_mejor_version          MI CLASE: SANO
     2 definir_receta_propia_mantenerse_centrado    MI CLASE: SANO
     3 agendar_cuidados_propios_cumplirlos          MI CLASE: SANO
     4 ceder_autoridad_unilateral_equipo            MI CLASE: SANO
     5 dominar_arte_socializar_trabajo              MI CLASE: SANO
     6 evitar_presion_social_actos_equipo           MI CLASE: SANO, con arista D.29 a su madre, la 5
     7 construir_confianza_equipo_tiempo_solas      MI CLASE: SANO, con arista de lectura a cap_11
     8 vivir_valores_propios_evitar_listarlos       MI CLASE: SANO
     9 demostrar_apertura_visiones_distintas        MI CLASE: SANO
    10 manejar_contacto_fisico_regla_platino        MI CLASE: SANO, con atribucion
    11 reconocer_emociones_propias_avisar_equipo    MI CLASE: SANO
    12 dominar_reacciones_emociones_ajenas          MI CLASE: SANO

**LO QUE LO SOSTIENE, Y NO ES UNA SENIAL (`D.19`):** `cap_08` es un capitulo de rotulos, y cada
uno de los doce sale de un rotulo distinto del fichero, con **una sola fusion**, el `3`, que
junta `L37` `Calendar` con `L41` `Show up for yourself`. **Ninguno REPITE a otro de los once ni a
nada que yo reconozca del grafo: lo que comparten es el libro, no el procedimiento.**

---

## 5. LA FIDELIDAD `D.30`, PASO A PASO Y CONTRA SU LINEA DEL LIBRO

**Encabezado (`HEREDADO 1`): los `102` pasos de los `12` nodos de `dataset/nodos.jsonl` (`282`
nodos, arbol `1ae327e`), leidos uno a uno contra `fuentes/scott_radical_candor/cap_08.md` (`189`
lineas). No es una muestra: son los `102`.**

| # | nodo | pasos | `TRANSCRIPCION` | `PUENTE` | lineas del libro que los sostienen |
|---:|---|---:|---:|---:|---|
| 1 | `integrar_trabajo_vida_mejor_version` | 5 | **5** | **0** | `L27` |
| 2 | `definir_receta_propia_mantenerse_centrado` | 9 | **9** | **0** | `L29`, `L31`, `L33`, `L35` |
| 3 | `agendar_cuidados_propios_cumplirlos` | 5 | **5** | **0** | `L39`, `L43` |
| 4 | `ceder_autoridad_unilateral_equipo` | 15 | **15** | **0** | `L47` a `L65`, una linea por paso |
| 5 | `dominar_arte_socializar_trabajo` | 9 | **9** | **0** | `L69`, `L71`, `L73`, `L75` |
| 6 | `evitar_presion_social_actos_equipo` | 6 | **6** | **0** | `L79`, `L81` |
| 7 | `construir_confianza_equipo_tiempo_solas` | 7 | **7** | **0** | `L95`, los siete |
| 8 | `vivir_valores_propios_evitar_listarlos` | 9 | **9** | **0** | `L99`, `L101`, `L103` |
| 9 | `demostrar_apertura_visiones_distintas` | 10 | **10** | **0** | `L107`, `L109`, `L111`, `L115`, `L119`, `L121` |
| 10 | `manejar_contacto_fisico_regla_platino` | 9 | **9** | **0** | `L125`, `L127`, `L131`, `L139`, `L141`, `L143`, `L145`, `L149` |
| 11 | `reconocer_emociones_propias_avisar_equipo` | 7 | **7** | **0** | `L153`, `L155`, `L157`, `L159` |
| 12 | `dominar_reacciones_emociones_ajenas` | 11 | **11** | **0** | `L163`, y `L167` a `L181` |
| | **`cap_08` ENTERO** | **102** | **102** | **0** | **`0,00` por ciento de `PASOS INVENTADOS`** |

**LAS TRES TRAMPAS DEL CAPITULO, QUE ES DONDE YO HABRIA BUSCADO UN PUENTE, Y LAS TRES AGUANTAN:**

| donde | por que era trampa | que leo |
|---|---|---|
| las **ocho horas de suenio** (`L27`, nodo `1` `P4`) | escribirlas como norma para el lector seria un puente de la especie `PERIODO` | **el libro las escribe en condicional y al lector**, *If you need to get eight hours of sleep to stay centered*, y el paso las escribe asi |
| la **receta de la autora** (`L35`, nodo `2` `P6` y `P7`) | ocho horas, cuarenta y cinco minutos, una novela a la semana, cuatro fines de semana, dos semanas de vacaciones: cinco periodos de golpe | **los cinco van DENTRO de pasos que dicen que son SUYOS**, y el propio libro dice en `L31` y `L33` que lo de uno es basura para otro |
| **`regularmente`** (`L95`, nodo `7` `P4` y `P5`) | el libro dice *on a regular basis* y *regular 1:1s*, y **no dice cada cuanto** | **el paso tampoco lo dice.** El unico periodo escrito es el `P7`, y lo lleva porque el libro escribe *annual* |

**LA UNICA CIFRA DE AUTOR DEL CAPITULO ESTA PUESTA DONDE VA, Y NO EN UN PASO:**

    $ python .v33a/aristas.py       (dataset de 282 nodos, arbol 1ae327e)
      manejar_contacto_fisico_regla_platino   previos 0 []  siguientes 0 []  atribuciones 1
        ATRIBUCION: {"autor": "Gretchen Rubin, en The Happiness Project, citada por Kim Scott",
        "cifra": "para que el flujo de oxitocina y de serotonina ... sea lo mas eficaz posible,
        hay que aguantar un abrazo al menos seis segundos",
        "fecha_corte": "2019, que es la fecha de la edicion citada de Radical Candor; el libro
        no fecha la investigacion de la que sale la cifra", "fuente": "scott_radical_candor"}

### 5.1. **MI DISCUTIBLE CIEGO 1, Y ES EL MAS GORDO QUE TRAIGO:** una sede duradera dice que tres capitulos no estan minados, y uno de los tres lo esta entero

**QUE DICE LA SEDE.** `dataset/nodos.jsonl`, nodo `construir_confianza_equipo_tiempo_solas`,
campo `resumen_teorico`:

> *Los tres reenvios del libro no se convierten en pasos inventados: la linea 95 manda a `1:1
> Conversations` del capitulo ocho, a `Soliciting Impromptu Guidance` del capitulo seis y al
> capitulo siete para las conversaciones de carrera.* **`Esos tres capitulos NO estan minados
> todavia`**, *asi que los pasos 5, 6 y 7 transcriben lo que esta linea dice de cada uno y ni una
> palabra mas.*

**QUE MIDO YO, DEL DATO Y NO DE ESA FRASE (`HEREDADO 2`).** `cap_08.md` declara en su frontmatter
`unidad: Cap. 5`, asi que **el capitulo OCHO del libro es el fichero `cap_11.md`**. Y entonces:

    $ python .v33a/capitulos.py           (dataset de 282 nodos, arbol 1ae327e)
      cap_09.md    SI                  0        0        <- capitulo SEIS del libro
      cap_10.md    SI                  0        0        <- capitulo SIETE del libro
      cap_11.md    SI                 16      187        <- capitulo OCHO del libro

    $ python .v33a/bandeja_caps.py        (cuarentena/scott_radical_candor, 63 candidatos, arbol 1ae327e)
      cap_09.md    20 candidatos
      cap_10.md    14 candidatos

**DOS DE LOS TRES ESTAN SIN MINAR Y EL TERCERO ESTA MINADO ENTERO**, con `16` nodos y `187` pasos
dentro del grafo. **Y quien lo prueba es la propia vuelta 33**: ese mismo nodo lleva escrita la
arista a `montar_reuniones_solas_mentalidad_frecuencia`, que **es de `cap_11`**.

    $ cat .v33a/madre_1a1.txt
    ID: montar_reuniones_solas_mentalidad_frecuencia   pasos: 22
    previos: ['decidir_quien_comunica_cada_cuanto', 'construir_confianza_equipo_tiempo_solas']
    RESUMEN: UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_11.md, unidad Cap. 8, Results.

> **`LECTURA`, marcada aparte de la cifra:** **la frase es falsa para uno de sus tres, y la vuelta
> que la escribio lo sabia**, porque en la misma tanda cablo la arista a ese capitulo. **NO LE
> PONGO ESPECIE AQUI, Y DIGO POR QUE:** `5.2` da el dataset como sede de `CLASE`, y aqui **ningun
> veredicto esta mal puesto**; la fila `DATO MOVIDO` del 16 sep cubre *una operacion que cambia
> `dataset/` sin que ningun veredicto este mal puesto*, y **mi propia `ACTA 31` `7.2` ya cargo
> ahi una falsedad tecleada a mano dentro de `dataset/` y de `bitacora/`**. **Esa es la lectura
> que traigo. La adjudico en el turno normal, con el reporte delante, y no aqui**, porque
> adjudicar no es medir (`AUDITOR_FORJA.md` 2).

### 5.2. **MI DISCUTIBLE CIEGO 2:** `las cuatro conversaciones` donde yo cuento tres

El `nombre_largo` de `construir_confianza_equipo_tiempo_solas` dice **`las cuatro conversaciones
con las que el libro dice que se empieza`**. Leyendo `L95`, yo cuento **TRES conversaciones con
nombre**: las reuniones a solas periodicas, pedir critica, y las conversaciones anuales de
carrera. La cuarta solo sale si se cuenta *spend a little time alone*, que no es una conversacion
con nombre sino la practica general de la que cuelgan las otras. **El libro NO escribe la cifra
cuatro en ningun sitio de esa linea.**

**ES LA SEGUNDA VUELTA SEGUIDA CON LA MISMA FIGURA, Y POR ESO LA TRAIGO:** mi `ACTA 31`
discutible `1` fue *las cinco cosas* del kanban, y aquella la adjudique **REGISTRADA Y NO
CARGADA**, porque `D.30` cuenta **pasos** y esa cifra vive en el `nombre_largo`. **Me aplico mi
propia adjudicacion: marcada y no cargada.** Lo que anoto es **la repeticion**, que es lo unico
nuevo.

### 5.3. **MI DISCUTIBLE CIEGO 3:** los tres rotulos de pieza sin nodo, clasificados por mi

| rotulo | cuerpo | **mi clase** | lo que la sostiene |
|---|---|---|---|
| `L15` **`STAY CENTERED`** | `L17` a `L23` | **NO EXTRAIBLE, bien dejado fuera** | es postura, y remata en la pregunta que presenta a sus hijos, *What am I recommending you do about it?*. No nombra ni un acto |
| `L89` **`RESPECT BOUNDARIES`** | `L91` | **NO EXTRAIBLE, bien dejado fuera** | la formula literal *Here are some things I have learned about walking this line* es un anuncio de hijos. Lo unico con olor a acto, *negotiate boundaries differently with each person*, no trae medio |
| `L83` **`Booze`** | `L85` a `L87` | **NO EXTRAIBLE, y lo marco igual** | `L85` es una frase de aviso y `L87` una lista de desastres. Ni un acto que el lector pueda ejecutar |

> **`LECTURA`, marcada aparte:** **lo que marco de `Booze` no es que falte el nodo: es que la
> cabeza publica una serie de DOS con UN solo hijo.** `L75` nombra las dos advertencias y el paso
> `9` del nodo `5` las escribe las dos; en el grafo solo una tiene hijo cableado. **La vara dice
> `UNA ADVERTENCIA ES LINEA`, y por eso me pare a mirarla**: aguanta, porque una advertencia es
> linea **de su nodo**, y `L83` a `L87` no traen nada que no este ya en el paso `9` de su madre.
> **Lo dejo escrito para que el siguiente no tenga que volver a decidirlo.**

### 5.4. **MI DISCUTIBLE CIEGO 4:** el `resumen_teorico` del grafo habla del reporte de su vuelta

Tres de los doce `resumen_teorico` traen, **dentro de `dataset/nodos.jsonl`**, frases del tipo
**`VA MARCADO DISCUTIBLE EN EL REPORTE DE ESTA VUELTA`**. El dataset es sede duradera; el
reporte, dice la tabla de `5.2`, **se reescribe cada vuelta**. Dentro de diez vueltas esa frase
apuntara a un fichero que dice otra cosa.

> **`LECTURA`, marcada aparte:** **esto le toca a mi fase antes que a nadie.** Mi apertura ciega
> **no puede leer el dataset sin leer con el lo que el reporte dice de si mismo**, y leer el
> reporte es exactamente lo que `D.34.2` me retira. **No lo cargo**: lo declaro como cosa de
> forma y lo subo, porque el remedio tocaria `EXTRACTOR.md`, que esta bajo la moratoria de `D.45`.

### 5.5. **LO QUE SI REPRODUCE AL DIGITO, Y LO PUBLICO PORQUE ESTABA BUSCANDO QUE NO**

El `resumen_teorico` de `ceder_autoridad_unilateral_equipo` publica **`1.156 palabras de cuerpo
de las 6.140`**. Mi primer instrumento dio `1154` y `6162`, y estuve a un paso de marcarlo. **No
es caida: es la forma de contar, y lo mido en vez de suponerlo.**

    $ python .v33a/palabras2.py       (sobre fuentes/scott_radical_candor/cap_08.md, 189 lineas)
    cuerpo entero tras el frontmatter (L8 al final)
        split() a secas                        6140
        regex [A-Za-z0-9 apostrofo guion]      6162
        regex solo letras y digitos            6393
    tramo FREE AT WORK con su rotulo (L45 a L66)
        split() a secas                        1156
        regex [A-Za-z0-9 apostrofo guion]      1157
        regex solo letras y digitos            1197

**`str.split()` saca las dos EXACTAS.** La cifra es reproducible y digo con que instrumento.
**Lo dejo escrito porque una cifra que se comprueba y aguanta vale lo mismo que una que cae**, y
porque el remedio `2` que me escribi pide precisamente esto: generarla del dato antes de hablar.

---

## 6. EL BARRIDO DE VECINOS, SOBRE GRAFO MAS BANDEJAS (`D.38.4`)

**Encabezado (`HEREDADO 1`): `12` corridas de `forja.py informe` EN SECO, cero inserciones. La
poblacion de cada una es `dataset/nodos.jsonl` de `282` nodos MENOS el propio candidato, mas las
bandejas de `cuarentena/`, que las pone la aduana sola. Arbol `1ae327e`.**

    $ sh .v33a/barrido.sh   (12 corridas, resumidas por .v33a/resumen_barrido.py)
      candidato                                      poblacion ENTRARIA  BLOQUEA   CAE
      integrar_trabajo_vida_mejor_version            347       1         0         0
      definir_receta_propia_mantenerse_centrado      347       1         0         0
      agendar_cuidados_propios_cumplirlos            347       1         0         0
      ceder_autoridad_unilateral_equipo              347       1         0         0
      dominar_arte_socializar_trabajo                347       1         0         0
      evitar_presion_social_actos_equipo             347       0         1         0
      construir_confianza_equipo_tiempo_solas        347       0         1         0
      vivir_valores_propios_evitar_listarlos         347       0         1         0
      demostrar_apertura_visiones_distintas          347       1         0         0
      manejar_contacto_fisico_regla_platino          347       1         0         0
      reconocer_emociones_propias_avisar_equipo      347       0         1         0
      dominar_reacciones_emociones_ajenas            347       1         0         0

      poblacion, literal de la aduana: 347  (281 del grafo mas 66 que esperan en bandejas)

### 6.1. **Y AQUI ES DONDE `D.38.5` COBRA: MI BARRIDO Y EL DE LA MAQUINA SALEN IGUALES, VECINO A VECINO**

`D.38.5` dice que desde el 12 sep la aduana mide **la misma poblacion que yo**, y que **si no
cuadran es una discrepancia de verdad y no de metodo**. Cuadran, y lo mido en vez de afirmarlo:

    $ python .v33a/vecinos_barrido.py
      integrar_trabajo_vida_mejor_version           yo 0   la maquina de la vuelta 0   IGUALES
      definir_receta_propia_mantenerse_centrado     yo 0   la maquina de la vuelta 0   IGUALES
      agendar_cuidados_propios_cumplirlos           yo 0   la maquina de la vuelta 0   IGUALES
      ceder_autoridad_unilateral_equipo             yo 0   la maquina de la vuelta 0   IGUALES
      dominar_arte_socializar_trabajo               yo 0   la maquina de la vuelta 0   IGUALES
      evitar_presion_social_actos_equipo            yo 3   la maquina de la vuelta 3   IGUALES
      construir_confianza_equipo_tiempo_solas       yo 3   la maquina de la vuelta 3   IGUALES
      vivir_valores_propios_evitar_listarlos        yo 1   la maquina de la vuelta 1   IGUALES
      demostrar_apertura_visiones_distintas         yo 0   la maquina de la vuelta 0   IGUALES
      manejar_contacto_fisico_regla_platino         yo 0   la maquina de la vuelta 0   IGUALES
      reconocer_emociones_propias_avisar_equipo     yo 4   la maquina de la vuelta 4   IGUALES
      dominar_reacciones_emociones_ajenas           yo 0   la maquina de la vuelta 0   IGUALES

      TOTAL vecinos levantados: yo 11, la vuelta 11

**LOS `12` DE `12` SALEN `IGUALES`, Y NO SOLO EN LA CUENTA: SALEN LOS MISMOS IDS.** Y las
seniales tambien salen al milesimo; las dos que mas cerca pasan del umbral son las que pego,
sacadas de mi corrida y no de su bitacora:

    $ grep -A2 'BLOQUEARIA]' .v33a/barrido.txt
    [BLOQUEARIA] construir_confianza_equipo_tiempo_solas
        vecino decidir_quien_comunica_cada_cuanto  [levantada por: paso_contra_nodo]
          similitud_texto 0.244 | familia_id 0.000 | paso_contra_nodo 0.619
    [BLOQUEARIA] vivir_valores_propios_evitar_listarlos
        vecino sostener_contacto_oferta_aceptacion  [levantada por: paso_contra_nodo]
          similitud_texto 0.112 | familia_id 0.000 | paso_contra_nodo 0.606

> **`LECTURA`, marcada aparte de la cifra:** **es la primera vez que puedo decir esto con las dos
> cifras delante.** Mi `ACTA 14` barrio `135` titulos donde el extractor barrio `203`, y de ahi
> salio `D.38.4`. Hoy barremos `347` los dos y **levantamos los mismos `11` vecinos**. Lo que
> `D.38.5` prometio esta cumplido, y lo digo porque **un metodo que ya cuadra deja de ser
> sospechoso y pasa a ser instrumento**.

### 6.2. **MI DISCUTIBLE CIEGO 5, Y ES DE LOS QUE LA MAQUINA NO LEVANTA**

**`agendar_cuidados_propios_cumplirlos` no levanta vecino ni en mi barrido ni en el suyo**, y aun
asi me pare a mirarlo, porque su `P1` dice *pon en tu calendario las cosas que necesitas hacer
para ti, igual que pondrias una reunion importante*, y `cuidarse_agotamiento_centro_rueda`, que
lleva en el grafo desde `cap_07`, lleva su `P7` *bloquea en tu calendario tiempo de pensar todos
los dias*.

**MI CLASE PARA ESE PAR ES `SANO`, Y DIGO SOBRE QUE:** el objeto de uno es **la cita contigo
mismo de tu receta** y el del otro es **el tiempo de pensar**; lo que queda fuera del solape es
procedimiento en los dos lados (el desplazamiento, el tren y que otros no te la pisen de un lado;
declinar invitaciones y el humor a tu costa del otro). **`6.1` de la vara: no hay bascula, y lo
que decide es si lo que queda fuera es procedimiento en los dos lados.** Lo es.

**LO MARCO PORQUE NINGUNA SENIAL LO LEVANTO, no porque crea que esta mal puesto**, y porque esta
casa mide tambien el error de dejar pasar (`AUDITOR_FORJA.md` 7).

---

## 7. LOS TRECE PARES, ADJUDICADOS POR MI ANTES DE DESTAPAR NI UNA RAZON

**Encabezado (`HEREDADO 1`): las `14` lineas que `bitacora/VEREDICTOS.jsonl` gana entre `ef3e7f9`
(`396` lineas) y `1ae327e` (`410` lineas). Trece son pares; la catorceava es una correccion
declarada y va en `7.2`.**

    $ python .v33a/bitacora.py
    bitacora/VEREDICTOS.jsonl   antes de la vuelta 33: 396 lineas   ahora: 410   ENTRAN: 14
      clase CONTINUA       2
      clase CORREGIDO      1
      clase SANO          11
      lineas nuevas SIN razon escrita (D.8): 0 de 14

**`D.8` EN VERDE: `0` de `14` sin razon escrita.** *Un `SANO` sin razon escrita es una caida
aunque acierte*, y no hace falta releerlo para verlo: se ve en la bitacora. No hay ninguno.

**MI TABLA, PEGADA DE `.v33a/mis_clases.txt` SIN TOCARLA, Y LA SUYA AL LADO:**

| # | candidato | vecino | **MI CLASE, a ciegas** | la de la vuelta |
|---:|---|---|---|---|
| 2 | `evitar_presion_social_actos_equipo` | `contar_cuatro_historias_propias` (BANDEJA) | **SANO** | SANO |
| 3 | `evitar_presion_social_actos_equipo` | `proteger_tiempo_equipo_jefe` | **SANO** | SANO |
| 4 | `evitar_presion_social_actos_equipo` | `crear_obligacion_disentir_equipo` | **SANO** | SANO |
| 5 | `evitar_presion_social_actos_equipo` | `dominar_arte_socializar_trabajo` | **CONTINUA** | CONTINUA |
| 6 | `construir_confianza_equipo_tiempo_solas` | `decidir_quien_comunica_cada_cuanto` | **SANO** | SANO |
| 7 | `construir_confianza_equipo_tiempo_solas` | `reconocer_emociones_propias_avisar_equipo` | **SANO** | SANO |
| 8 | `construir_confianza_equipo_tiempo_solas` | `minimizar_impuesto_colaboracion_equipo` | **SANO** | SANO |
| 9 | `montar_reuniones_solas_mentalidad_frecuencia` | `construir_confianza_equipo_tiempo_solas` | **CONTINUA** | CONTINUA |
| 10 | `vivir_valores_propios_evitar_listarlos` | `sostener_contacto_oferta_aceptacion` | **SANO** | SANO |
| 11 | `reconocer_emociones_propias_avisar_equipo` | `minimizar_impuesto_colaboracion_equipo` | **SANO** | SANO |
| 12 | `reconocer_emociones_propias_avisar_equipo` | `centrar_debate_ideas_fuera_egos` | **SANO** | SANO |
| 13 | `reconocer_emociones_propias_avisar_equipo` | `cuidarse_agotamiento_centro_rueda` | **SANO** | SANO |
| 14 | `reconocer_emociones_propias_avisar_equipo` | `construir_confianza_equipo_tiempo_solas` | **SANO** | SANO |

> # **`13` DE `13`. NI UNA DISCREPANCIA DE CLASE EN ESTA TANDA.**

**MIS DOS `CONTINUA`, CON SU DIRECCION, QUE ES LO QUE LA VARA `6.1` PIDE** (que anade el HIJO a la
MADRE, nunca al reves), y escritos antes de destapar nada:

| par | **MADRE**, que NOMBRA | **HIJO**, que PROCEDIMENTA |
|---|---|---|
| `5` | `dominar_arte_socializar_trabajo`, cuyo `P9` nombra las dos advertencias de `L75` | `evitar_presion_social_actos_equipo`, que despliega la primera en seis pasos (`L79` y `L81`) |
| `9` | `construir_confianza_equipo_tiempo_solas`, cuyo `P5` nombra las reuniones a solas periodicas de `L95` | `montar_reuniones_solas_mentalidad_frecuencia`, que las despliega en `22` pasos desde `cap_11` |

**`NOMBRAR NO ES PROCEDIMENTAR` (`P.5.1`), y en los dos casos es literalmente eso: la madre las
nombra en una linea y el hijo trae el procedimiento que la madre no tiene.**

**LOS ONCE `SANO`, EN UNA LINEA Y SIN REABRIR EL ARGUMENTO (`D.47` austero):** en los once, lo
que queda FUERA del solape es procedimiento **en los dos lados**, que es lo que `6.1` manda mirar,
y en ninguno hay bascula que valga. Los dos que mas cerca pasan y por que aguantan:

- **par `6`**, la senial mas alta de la tanda (`paso_contra_nodo 0,619`): los dos apuntan a la
  reunion a solas, pero `decidir_quien_comunica` decide **que reuniones hay y a que coste**, y
  `construir_confianza` **construye confianza**. Y la prueba de que la casa lo vio bien es el par
  `9`: **la MADRE del procedimiento del `1:1` es `montar_reuniones_solas`, no este.**
- **par `10`**, `paso_contra_nodo 0,606` entre *no montar un ejercicio de valores* y *sostener el
  contacto entre la oferta y la aceptacion*. **Es un homonimo castellano**, *mantener el contacto*
  en dos sentidos que no se tocan, con las otras dos seniales en el suelo (`0,112` y `0,000`), y
  **ni siquiera son del mismo libro**. `D.19`: una senial dice donde mirar y ahi acaba su trabajo.

### 7.1. **LA MUESTRA PINEADA DE LOS `SANO` (`AUDITOR_FORJA.md` 7): NO HAY MUESTRA, PORQUE LEI LA POBLACION ENTERA**

| | |
|---|---|
| **`SANO` de la tanda** | **`11`**, medidos por `.v33a/bitacora.py` sobre las `14` lineas nuevas |
| **lo que la regla pide** | el mayor entre `TRES` y el `20` por ciento de `11`, que es `2,2`. **Pide `3`**, con techo de `20` |
| **lo que relei** | **los `11`**, uno a uno y con los pasos de los dos extremos delante |
| **semilla** | **no hay, y no es un olvido**: una semilla elige una muestra, y aqui **no hay muestra que elegir**. `7` lo dice con todas las letras: *no se inventa una muestra donde no hay poblacion*, y la simetrica vale igual |
| **cuantos caen** | **`0` de `11`** |
| **tasa con su banda** | **`0` caidas sobre `11` releidos, `0,0` por ciento, banda de Wilson al `95` por ciento de `0,0` a `25,9`** |

    $ python .v33a/banda.py 0
    MUESTRA PINEADA DE LOS SANO (AUDITOR_FORJA.md 7)
      SANO nuevos de la tanda, contados de bitacora/VEREDICTOS.jsonl: 11
      releidos: 11 de 11 (la poblacion entera, no una muestra)
      caen: 0
      tasa: 0.0 por ciento
      banda de Wilson al 95 por ciento: de 0.0 a 25.9 por ciento

> **`LECTURA`, marcada aparte de la cifra:** **una tasa sin banda es media cifra, y con `11`
> puestos la banda llega al `25,9` por ciento.** Lo que esta cifra dice es que **en estos once no
> encontre ninguno mal puesto**, no que el error de dejar pasar sea cero: con esta poblacion, el
> instrumento no puede distinguir un sistema perfecto de uno que falla uno de cada cuatro.

---

## 8. LAS GUARDAS, CORRIDAS POR MI EN ESTA MISMA FASE

**Encabezado (`HEREDADO 1`): arbol `1ae327e` SUCIO, con los `7` ficheros del arnes fuera y `.v33a/`
sin seguir. `dataset/nodos.jsonl` con `282` nodos.**

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 282
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada,
      vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta,
      guiones, censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python tests/test_aceptacion.py
      total: 251 pruebas, 0 fallos, 0 errores

    $ python forja.py resolutor
    nodos vivos: 282
    nodos deprecados (archivo): 0
    alias registrados: 0

> **`LECTURA`, marcada aparte de la cifra, y es sobre mi:** **mi apertura de la `ACTA 31` publico
> `4` pruebas en rojo, y esta publica `0`** sobre un arbol igual de sucio. La cifra de entonces la
> cito de mi propia sede y no de una tabla ajena: `ACTA 31` `6`, *las `4` pruebas en rojo eran de
> mi fase ciega*, adjudicado alli **CIERTO** contra un clon limpio. **No me lo apunto como
> merito: lo apunto porque el remedio `1` que me escribi obliga a decir el estado del arbol junto
> a la cifra, y este es justo el caso donde las dos cifras solo se entienden con el arbol al
> lado.** `251` es la poblacion de pruebas de HOY, medida arriba, y no la comparo con ninguna
> cifra vieja de poblacion porque no la he vuelto a generar del dato.

### 8.1. **LA COLA DE VIGENCIA `D.15`, QUE NO PONE NADA EN ROJO PERO SI CUENTA**

    $ python forja.py rancios
    BLOQUE DE VIGENCIA: 40 hallazgo(s) sobre 396 veredicto(s) y 0 cita(s).
      RANCIO 32, SIN HUELLA 8
      lineas declaradas NO CONSUMADAS y por eso no medidas: 14

    $ python forja.py rancios | grep '\[RANCIO\]' | grep -c 'recorrer_rueda_conscientemente_cultura_equipo'
    6

> **`LECTURA`, marcada aparte:** **`6` de los `32` rancios los produce la `TAREA 1` de esta misma
> vuelta.** Corregir el `resumen_teorico` de `recorrer_rueda_conscientemente_cultura_equipo` le
> cambio la huella, y con ella quedaron rancios los seis veredictos que lo citaban. **No es una
> caida: `D.15` dice que un rancio es COLA DE TRABAJO y no guarda que tumbe el cierre.** Lo
> publico porque **es el precio de la `TAREA 1`, y el precio de una tarea bloqueante se dice.**

### 8.2. **EL CERROJO, QUE ES LA CAIDA QUE LA VUELTA SE DECLARO A SI MISMA**

    $ git ls-files | grep -i cerrojo
    docs/loop/paradas/2026-09-16-el-cerrojo-y-el-testigo-DECISION.md
    src/cerrojo.py

    $ grep -i cerrojo .gitignore
    # EL CERROJO DE INSERCION NUNCA ENTRA EN GIT (D.44).
    # Commiteado, un checkout entrega un cerrojo de un proceso que ya no existe y la
    *.cerrojo

    $ ls -a dataset/
    .  ..  nodos.jsonl

**NINGUN `.cerrojo` ESTA EN EL INDICE HOY, Y LA REGLA QUE LO IMPIDE ESTA ESCRITA.** Lo mido
porque el registro de credito de esta linea dice que el cerrojo **entro** al indice en la vuelta
33 y que **se reparo**. **La reparacion esta, y la compruebo del arbol y no de la linea que lo
cuenta** (`HEREDADO 2`).

---

## 9. DOS COSAS DE LA PROPIA FASE CIEGA QUE TENGO QUE DECLARAR, PORQUE ME PASARON A MI HOY

### 9.1. **LA SEDE QUE `D.48` ME MANDA LEER AL ABRIR TRAE DENTRO CONCLUSIONES DEL REPORTE**

`D.48` (17 sep 2026) manda **leer el credito al abrir**, y dice que la sede es
`docs/loop/CREDITO_serial.jsonl`. **Y aqui va la mitad que me favorece, dicha primero para que no
parezca que la escondo: el instrumento NO filtra nada.** `python forja.py credito` imprime una
tabla de especie, racha y tanda, y ni una cita:

    $ python forja.py credito
      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA 31
      CIFRA PUBLICADA    0 de 2     ACTA 32
      CLASE              1 de 2     ACTA 32
      DATO MOVIDO        2 de 2     ACTA 32  TOPE
      REPORTE            0 de 3     ACTA 32

      CREDITO ROTO: DATO MOVIDO en su tope.

**LO QUE FILTRA ES LA SEDE, Y LA SEDE ES LO QUE `D.48` NOMBRA.** Dentro del campo `cita` de las
cuatro lineas que la vuelta 33 escribio esta **el contenido de las secciones del reporte que
vengo a leer a ciegas**:

    $ tail -3 docs/loop/CREDITO_serial.jsonl
    {..."cita": "REPORTE.md Z.4: dataset/nodos.jsonl.cerrojo, fichero vivo, entro al indice en mi
     commit 504cd38 por un git add -A; declarado y reparado por la otra sesion en 1954005",
     "especie": "DATO MOVIDO", "racha": "2 de 2", "tanda": "ACTA 32"...}
    {..."cita": "REPORTE.md Z.3.a: 12 veredictos razonados, 11 SANO y ninguna clase que yo sepa
     mal puesta; mis dudas van marcadas a ciegas en Z.5", "especie": "CLASE"...}
    {..."cita": "REPORTE.md Z.8: toda tabla pegada de su fichero, tallado y censo en verde en cada
     commit, y la fila +31 de pruebas publicada diciendo que no es mia", "especie": "CIFRA
     PUBLICADA"...}

> **`LECTURA`, marcada aparte, y esta es contra el arnes y no contra nadie:** **`D.34.2` retira
> cuatro ficheros para que yo no lea el reporte, y `D.48` me manda leer una sede que lleva tres de
> sus conclusiones copiadas dentro.** **Y me paso a mi hoy, con su hora:** abri
> `CREDITO_serial.jsonl` al empezar, y la segunda de esas citas me dijo **`11 SANO`** antes de que
> yo contara los mios. **Lo declaro porque el motivo de toda esta fase es que mi lectura sea
> independiente de la suya, y hoy no lo fue del todo.**
>
> **LO QUE SI PUEDO DECIR EN MI DESCARGO, Y ES MEDIBLE:** mi fichero de clases (`08:17:27`)
> escribe los doce a mano **antes de abrir la bitacora**, y el barrido de `6.1` levanta los mismos
> `11` vecinos por su cuenta, con la aduana y no conmigo. **La cita no me dio ninguna clase: me
> dio una cuenta.** Aun asi, **el que la cuenta estuviera ahi es la averia**, y no la arreglo yo:
> `D.48` y la retirada de `D.34.2` viven las dos en el arnes, que `D.45` me prohibe tocar. **Sube.**
>
> **Y LO QUE NO ES AVERIA, PARA QUE NADIE LO ARREGLE DE MAS:** el instrumento `forja.py credito`
> **no filtra nada**, y su tabla, pegada arriba, es la que la apertura necesita. Lo que filtra es
> el campo `cita` del fichero. **Quien mire esto tiene que mirar la sede, no el instrumento.**

### 9.2. **MI DISCUTIBLE CIEGO 6: la bitacora estampa `(D.37)` en aristas que son `D.29`, y el rotulo esta tecleado en el codigo**

Las dos lineas `CONTINUA` de la bitacora llevan escrito
`operacion: arista declarada por lectura (D.37)`. Los `resumen_teorico` de los dos nodos del par
`5` dicen, con todas las letras, **que esa arista es `D.29` y NO `D.37`**. **No es contradiccion
del extractor: el rotulo esta tecleado en el codigo y se estampa igual en toda arista declarada
por lectura.**

    $ grep -rn 'arista declarada por lectura' src/
    src/arista.py:187:        "operacion": "arista declarada por lectura (D.37)",

> **`LECTURA`, marcada aparte:** **quien lea la bitacora contando aristas `D.37` va a contar
> tambien las `D.29`, y no hay campo que las separe.** **Lo marco y no lo toco**: `src/` esta bajo
> la moratoria de `D.45` mientras el frente `grove` este vivo, y una pregunta de doctrina **se
> declara, se para y sube al fundador**.

---

## 10. LO QUE DEJO `POR ADJUDICAR` PARA MI TURNO NORMAL, CON EL REPORTE DELANTE

**Nada de esta lista lo adjudico aqui, porque adjudicar no es medir (`AUDITOR_FORJA.md` 2) y
porque la mitad de estas preguntas son de doctrina y `D.45` manda pararlas.**

| # | lo que dejo abierto | donde esta medido |
|---:|---|---|
| 1 | la frase del `resumen_teorico` que dice que `cap_11` no esta minado cuando tiene `16` nodos y `187` pasos. **Que especie es una falsedad tecleada dentro de `dataset/` sin veredicto mal puesto** | `5.1` |
| 2 | `las cuatro conversaciones` que yo cuento tres. **Segunda vuelta seguida con la misma figura** | `5.2` |
| 3 | la serie de `L75` con dos advertencias y un solo hijo cableado | `5.3` |
| 4 | el `resumen_teorico` que cita `EL REPORTE DE ESTA VUELTA` desde una sede duradera | `5.4` |
| 5 | `agendar_cuidados_propios_cumplirlos` contra `cuidarse_agotamiento_centro_rueda`, que **ninguna senial levanta** | `6.2` |
| 6 | el `(D.37)` tecleado en `src/arista.py` que se estampa sobre aristas `D.29` | `9.2` |
| 7 | **`D.48` contra `D.34.2`**: el instrumento que la apertura esta obligada a correr le enseña conclusiones del reporte | `9.1` |
| 8 | los `6` rancios que produce la `TAREA 1`, y si la cola se encarga o se declara | `8.1` |

---

## 11. LO QUE ESTA APERTURA AFIRMA, EN UNA TABLA, CON SU INSTRUMENTO AL LADO

**Encabezado (`HEREDADO 1`): todas las filas, sobre el arbol `1ae327e` sucio con los `7` del arnes,
`dataset/nodos.jsonl` de `282` nodos, `bitacora/VEREDICTOS.jsonl` de `410` lineas, bandejas de
`229` candidatos.**

| lo que afirmo | cifra | **instrumento que la saco** |
|---|---:|---|
| nodos que entran en la vuelta 33 | **12** | `.v33a/tanda.py`, del `git diff` del dataset |
| pasos de esos 12 | **102** | `.v33a/procedencia.py` |
| de ellos `PUENTE` | **0**, `0,00` por ciento | mi relectura de los `102` contra `cap_08.md`, tabla de `5` |
| rotulos de pieza del capitulo | **16**, `13` con nodo, `3` sin | `.v33a/rotulos.py`, mas mi descarte de `3` falsos positivos |
| lineas nuevas de bitacora | **14**: `11 SANO`, `2 CONTINUA`, `1 CORREGIDO` | `.v33a/bitacora.py` |
| `SANO` sin razon escrita (`D.8`) | **0** de `14` | `.v33a/bitacora.py` |
| vecinos que levanta la tanda | **11**, y mi barrido levanta **los mismos 11** | `.v33a/barrido.sh` y `.v33a/vecinos_barrido.py` |
| poblacion de mi barrido | **347** = `281` de grafo mas `66` de bandejas | la propia aduana, en `.v33a/barrido.txt` |
| pares que adjudico igual que la vuelta | **13 de 13** | `.v33a/mis_clases.txt`, escrito a las `08:22:57` |
| `SANO` releidos de la tanda | **11 de 11**, `0` caen, banda de `0,0` a `25,9` por ciento | `7.1` |
| `gate` | **VERDE**, `282` nodos | `forja.py gate` |
| `guiones` | **VERDE** | `forja.py guiones` |
| pruebas de aceptacion | **251**, `0` fallos | `tests/test_aceptacion.py` |
| cola de vigencia `D.15` | **32** rancios, `8` sin huella, de los cuales **6** los produce la `TAREA 1` | `forja.py rancios` |
| lote 4, bandeja mas archivados | **63 + 79 = 142** | `.v33a/cerrojo.txt` |
| discutibles ciegos que traigo | **6** | `5.1`, `5.2`, `5.3`, `5.4`, `6.2` y `9.2` |

---

---

## 12. **LAS RUTAS QUE PUBLICO COMO PRUEBA, COMPROBADAS CONTRA EL DISCO** (cosecha `7.B`)

*`LA RUTA QUE PROMETE PRUEBA ES CIFRA`: si apunta a un fichero inexistente o de cero bytes, es
caida de cifra en su sede, y esta pagina es mi sede. Asi que la compruebo yo antes de entregarla,
y con un instrumento que saca las rutas del propio fichero por patron y no de una lista mia.*

    $ python .v33a/rutas.py
      rutas publicadas: 37   en rojo: 4

      NO EXISTE        -  docs/loop/REPORTE.md
      CERO BYTES       0  docs/loop/ultimo_apertura.json
      NO EXISTE        -  docs/loop/ultimo_auditor.json
      NO EXISTE        -  docs/loop/ultimo_extractor.json

**LAS `33` RESTANTES ESTAN LAS `33`, Y NINGUNA EN CERO BYTES**, incluidos los `21` instrumentos
mios de `.v33a/` que sostienen cada cifra de esta pagina.

> **Y DIGO POR QUE SON `37` Y NO `36`, QUE ES LO QUE DIO LA PRIMERA CORRIDA:** el instrumento saca
> las rutas **del propio fichero**, y al escribir esta seccion el fichero paso a citar tambien
> `.v33a/rutas.py`. **La primera corrida era cierta para la pagina de entonces y falsa para esta**,
> asi que la volvi a correr contra la pagina que entrego. **Lo dejo escrito en vez de cambiar el
> numero y callarme**, que es exactamente la especie de celda que mi remedio `1` persigue: una
> cifra cuyo encabezado no dice la poblacion que midio.

> **`LECTURA`, marcada aparte, y la escribo porque si no alguien contara cuatro rojos contra mi:**
> **las cuatro en rojo son exactamente los cuatro ficheros del arnes**, tres que `D.34.2` retira y
> el cuarto, `ultimo_apertura.json`, que el arnes deja en cero bytes hasta que sella. **No las
> publico como prueba de ninguna corrida: las nombro en la cabecera para decir que NO estan en el
> arbol y que no las he recuperado.** Una ruta que se nombra para declarar una ausencia no es una
> ruta que promete prueba, y la diferencia se ve en que **ninguna cifra de esta pagina cuelga de
> ninguna de las cuatro.**

---

**APERTURA CIEGA CERRADA. NO LA TOCO MAS: el arnes la sella y el sello se verifica al terminar mi
turno.** No he commiteado nada.
