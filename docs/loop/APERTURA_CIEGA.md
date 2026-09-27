# APERTURA CIEGA DE LA VUELTA 80, lote 5 (`marquet_turn_the_ship`), **CLASE INSERCION**

*Auditor `claude-opus-5-5`, fase ciega, 26 sep 2026. En la corrida que arranco el 26 a las `09:27`, el arnes la numera `VUELTA 4`.
Linea **serial**, rama `extraccion-mundo-11`. Modo austero (`D.47`). Todo lo de esta pagina sale de `.v80aud/`, escrito y
corrido en esta fase; cada bloque `$` lo pega `.v80aud/generar_apertura.py` corriendo el comando en el momento de escribirla.
**No hay ninguna tabla en esta pagina**, a proposito, como de la `75` a la `79`.*

**LO QUE ESTA VUELTA TENIA QUE HACER, Y LO QUE CLASIFICO A CIEGAS** (mi encargo, `docs/loop/PROMPT_SIGUIENTE.md`): **las `20` fichas
de Marquet dentro, una por vez, en el orden** de `.v78ext/orden.txt`, con las `52` lineas y la unica arista que la `78` dejo listas;
**`d183`**, la frontera de Grove escrita con `corregir` despues de que entre su nodo; **`d104`**, pagada sin tocar el grafo; y si todo
entraba en verde, **el tag `primer-equipo-completo`**. Los candidatos ya no estan en la bandeja: **los leo donde estan hoy**, en el grafo
y en `_insertados`, contra mi lectura sellada de la `78` (que la `ACTA 77` `77.4` y `77.5` sostuvo entera) y contra el libro, y **releo la
unica arista con los pasos y las lineas delante** (seccion `5`).

**UNA LIMITACION DE METODO, DICHA ANTES DE NADA: EN ESTA FASE NO HE CORRIDO `git` SOBRE EL REPOSITORIO**, ni una vez, como de la `73`
a la `79`: la carpeta de una linea viva es solo del arnes (`PARALELO.md` `7`). **Lo que se mide con `git` aqui no lo mido**: que commit
movio que y a que hora, si cada `insertar` volvio antes de lanzarse el siguiente, y si el commit etiquetado tiene el mismo grafo que
`HEAD`. Lo que si mido sin `git` es el dato contra mis propias huellas de la `78` (seccion `2`). El commit en que esta el arbol, y la
etiqueta, los leo de los ficheros de `.git/`:

    $ cat .git/HEAD; cat .git/refs/heads/extraccion-mundo-11
    ref: refs/heads/extraccion-mundo-11
    67f2bee367eadc6630a3bf8886803792aff3675a
    $ python .v80aud/tag.py
    referencia de la etiqueta: d80dda756f082d45a03563e787b41365ebb5295c (suelta en refs/tags)
    objeto: tag 541
      object 69d407da4de8389a4f624b2126064e16ff11b3fb
      type commit
      tag primer-equipo-completo
      tagger alexcat84 <alexcat84@users.noreply.github.com> 1790471763 -0400
    HEAD de la rama: 67f2bee367eadc6630a3bf8886803792aff3675a

**NO HAY HUECO DE ACTA** (`1.0`): la ultima acta escrita es la `78`, que cubre la vuelta `79`, y la que viene a auditarse es la `80`, la
de mi encargo:

    $ grep -n "^# ACTA 7[6-9]\. VUELTA" docs/loop/ACTA_AUDITOR.md | cut -c1-60
    50764:# ACTA 76. VUELTA 77, lote 9 (`gerber_emyth`), **CLASE
    51329:# ACTA 77. VUELTA 78, lote 5 (`marquet_turn_the_ship`)
    51881:# ACTA 78. VUELTA 79, lote 5 (`marquet_turn_the_ship`)
    $ grep -n "VUELTA 4 : EXTRACTOR\|extractor listo\|VUELTA 4 : APERTURA CIEGA" docs/loop/loop.log | tail -3
    9755:[2026-09-26 17:31:48] VUELTA 4 : EXTRACTOR (claude-opus-5-5, esfuerzo high)
    9756:[2026-09-26 21:23:20] extractor listo (USD 9.213453000000001), 13892s, intento 1 de 7
    9757:[2026-09-26 21:23:21] VUELTA 4 : APERTURA CIEGA (claude-opus-5-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl

## 0. **LA HERENCIA** (`D.40`)

ACTA ANTERIOR LEIDA: 114462873410c8d9f0ea924c69bc7f002207b38d

**Comprobada sin git**: es el blob de `docs/loop/ACTA_AUDITOR.md` tal como esta hoy en el arbol, calculado como lo calcula git. **La
`ACTA 78` la lei entera**, de su linea de cabecera a la ultima del fichero, y con ella el encargo que me deje:

    $ python .v80aud/huella_acta.py
    sha1 del blob tal cual: 4a8a96002a8ba1572f1a3779377b42ea4905777b
    lineas con CRLF en el arbol: 466 | sha1 del blob normalizado a LF: 114462873410c8d9f0ea924c69bc7f002207b38d
    lineas del fichero: 52318 | la ACTA 78 empieza en la linea: [51881]

HEREDADO 1: NO APLICA en esta fase. **Motivo:** `R5` es un remedio **del extractor** y se mide **sobre su reporte de la `80`**
(`ACTA 78` `78.11`: *el reporte de la `80`, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera cambiada a
la `80`*), y el reporte **no esta en el arbol**: el arnes lo retiro para esta fase (`D.34.2`) y no lo he recuperado por ninguna via.
**Se mide en mi turno normal**, con los dos instrumentos sacados otra vez de los originales y no de las copias del extractor. Lo que
si esta en mi mano lo cumplo en mi pagina: cada bloque `$` lleva la salida del comando que abre, y nada mas.

    $ ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl
    ls: cannot access 'docs/loop/REPORTE.md': No such file or directory
    ls: cannot access 'docs/loop/ultimo_extractor.json': No such file or directory
    ls: cannot access 'docs/loop/ultimo_auditor.json': No such file or directory
    ls: cannot access 'docs/loop/CREDITO_serial.jsonl': No such file or directory

HEREDADO 2: CUMPLIDO. **`R6`, mio** (`ACTA 78` `78.11`): en esta fase los pasos de cualquier nodo los imprime
`.v67aud/normal/pasos_ciego.py`, que no ensenia `previos` ni `siguientes`, y **el unico bloque de pasos de esta pagina lo corre** (seccion
`5`). Los instrumentos mios de esta fase que **nombran** esas claves en su codigo:

    $ grep -l -E "previos|siguientes" .v80aud/*.py
    .v80aud/censo_libros.py
    .v80aud/esperado.py

**Y LO DIGO PARA QUE SE JUZGUE:** `esperado.py` (seccion `4`) **las nombra para leer las aristas del grafo con algun extremo en las
`20`**, y `censo_libros.py` (seccion `2`) **para contar las aristas entre libros**; **ninguno imprime una clave ni un id de relacion
leido del grafo**: imprimen cuentas y `SI` o `NO`, y `esperado.py` imprime las aristas esperadas **antes**, sacadas de mis ficheros y no
del grafo. `grafo_sin_tanda.py` (seccion `2`) quita los ids de la tanda de **cualquier** lista sin nombrar ninguna clave, y solo cuenta.
**No vi ninguna clave de relacion con su valor de ningun nodo en esta fase.** La pagina entera la mide un `grep` sobre ella al cerrarla
(seccion `8`).

HEREDADO 3: CUMPLIDO. **`R7`, mio** (`ACTA 78` `78.11`): toda linea de esta pagina que reparte un total en clases la imprime un
instrumento que cuenta **todas** las clases con el mismo predicado y **dice su `suma`**: los de `.v80aud/` la traen desde que nacen, y el
que reuso sin copiar (`.v70aud/poblacion.py`) ya la traia. **Medido sobre la pagina misma** en la seccion `8`, con la copia de
`.v79aud/r7_pagina.py`.

HEREDADO 4: CUMPLIDO. **`R8`, mio** (`ACTA 78` `78.11`, *mi fase ciega de la `80`, sobre el encargo de la `80`*): **lo mido aqui con
el mismo instrumento de la `78.12`, `.v79aud/normal/r8_encargo80.py`, sin copiarlo**, y su salida de hoy es identica a la que aquella acta
guardo; la lectura, linea a linea y mia, en la seccion `6`. **No hay encargo de la `81` que medir**: si la `ACTA 79` cierra la campania,
deja `PROMPT_SIGUIENTE.md` vacio (`ACTA 78` `78.10`).

HEREDADO 5: NO APLICA en esta fase. **Motivo:** `R9` es un remedio **del extractor** y se comprueba **en el reporte de la `80`, si
publica una cuenta de PUENTE** (`ACTA 78` `78.11`), y ese reporte **no esta en el arbol** (el bloque de `ls` del HEREDADO `1`, que es el
mismo fichero); no lo he recuperado. **Se mide en mi turno normal.** **Lo que si hago aqui es la mitad que es mia**: los pasos que
entraron son, byte a byte, los que lei en la `78` y la `ACTA 77` `77.3` cruzo con `R9` sobre esos mismos `110` pasos (seccion `3`), asi
que no hay texto nuevo sobre el que correr su `grep`. La salida que sostiene que el reporte no esta:

    $ ls docs/loop/REPORTE.md
    ls: cannot access 'docs/loop/REPORTE.md': No such file or directory

HEREDADO 6: CUMPLIDO. **`R10`, mio** (`ACTA 78` `78.11`, *esta acta, `78.13`, y la `ACTA 79`*): toda salida pegada en
`PROMPT_SIGUIENTE.md` se corre despues de la ultima escritura del auditor en el registro que mide, o se vuelve a correr antes del commit y
se compara. **Se cumplio al cerrar la `ACTA 78`**: sus cinco comparaciones, guardadas en `.v79aud/normal/r10.txt`, se corrieron despues de
mi ultima anotacion en `CREDITO_serial.jsonl` y despues del encargo (primera parte del bloque). **Lo que mido hoy**: los tres bloques del
encargo que miden ficheros que nadie volvio a escribir, corridos otra vez e identicos. **Una limitacion, dicha:** la clase `80` y el
tablero `--puedo` miden `DEUDA.jsonl` y el tablero, que la vuelta movio al pagar y al insertar (seccion `2`), y hoy ya no son
comparables; y `CREDITO_serial.jsonl` esta retirado. **Y UNA DIFERENCIA MIA, para que se juzgue:** el bloque de `78.13` pega *ahora:
17:28:48* y el fichero guardado dice *17:27:51*; **no es la misma corrida**: el generador de aquella acta corre cada orden al escribirla
(la cabecera de `.v79aud/normal/generar.py` lo dice), y las dos son posteriores al credito (`17:26:58`) y al encargo (`17:27:31`). **La
otra mitad de su sitio, la `ACTA 79`, es de mi turno normal.**

    $ bash .v80aud/r10.sh
    (1) la salida de la ACTA 78 78.13, guardada:
        clase 80: IDENTICA a la pegada
        tablero --puedo: IDENTICO al pegado
        relojes: IDENTICOS a los pegados
        orden: IDENTICO al pegado
        aristas esperadas y lineas: IDENTICAS a las pegadas
        2026-09-26 17:26:58 docs/loop/CREDITO_serial.jsonl
        2026-09-26 17:27:31 docs/loop/PROMPT_SIGUIENTE.md
        ahora: 2026-09-26 17:27:51
        2026-09-26 17:27:51 .v79aud/normal/r10.txt
        2026-09-26 17:27:31 docs/loop/PROMPT_SIGUIENTE.md
    (2) los bloques comparables, hoy:
        relojes: IDENTICOS a los pegados
        orden: IDENTICO al pegado
        aristas esperadas y lineas: IDENTICAS a las pegadas
    $ head -4 .v79aud/normal/generar.py | tail -3
    """ACTA 78: rellena una plantilla. Cada linea @@CMD <orden>@@ se sustituye por el bloque `    $ <orden>` con la salida de la orden,
    corrida con bash en el momento de generar; cada @@FILE <ruta>@@ pega el fichero tal cual, sangrado (ficheros que ya traen sus
    lineas `$` con su salida, escritos por tee al correrlas). Uso: python generar.py <plantilla> <salida>"""

## 1. **LO QUE VI SIN BUSCARLO, Y LO DIGO ANTES DE MEDIR** (`d146`)

**La foto de `git status` que el entorno me pone delante trae los asuntos de los ultimos commits del extractor de la `80`, y traen
cifras y conclusiones de su vuelta**, que lei antes de medir nada:

- `d09a152a` *Vuelta 80, T5: PRIMER EQUIPO COMPLETO. Las 20 de Marquet dentro, d104 y d183 pagadas, el censo por libro (479) y la arista
  entre libros; tag primer-equipo-completo en 69d407da; el cierre estricto en verde*;
- `395f5a70` *Vuelta 80, T5: censo, pasos inventados de lo que entro, D.61, R5 y las guardas en verde; el cierre estricto en verde*;
- `69d407da` *Vuelta 80, T4: d183 pagada, la frontera de Grove escrita por corregir en
  eliminar_seguimiento_descendente_responsabilizar_dueno (linea 1226 de la bitacora). El grafo, completo*;
- `2449c555` *Vuelta 80, T3 cerrada: las 20 de Marquet dentro, sus 52 lineas pasadas y la arista por lectura en el grafo; ningun nodo
  viejo cambiado*;
- y `67f2bee3`, sin cifras (*la salida del hook del commit del cierre*).

Es el mismo hueco de `d146` que declararon las aperturas de la `65` a la `79`, y no lo arreglo yo (`D.45`).

**Y LO DEMAS DEL MISMO TIPO, QUE ES MIO:**

1. la cola de `docs/loop/loop.log`, que no se retira, con el reloj y el coste del turno del extractor (bloque de la cabecera);
2. **cuantos** ficheros tiene `.v80ext/` (un `ls | wc -l`, dos veces, sin sus nombres), y el `ls` de `cuarentena/` y de `docs/loop/` al
   abrir la fase, que ensenian nombres de carpetas y ficheros y nada de dentro;
3. en `docs/loop/DEUDA.jsonl` imprimi **las claves** de las lineas de `d104` y `d183`, que dicen que **cada una tiene una linea de pago de
   la vuelta `80`**; **de esas lineas no lei su `como`** (seccion `2` lo mide por campo);
4. `python forja.py tablero`, que `D.49` manda leer y citar (seccion `2`). Tambien lei mi `ACTA 78` entera, mi encargo,
   `AUDITOR_FORJA.md` entero, las secciones `77.3` a `77.5` de mi `ACTA 77` y la plantilla de mi fase ciega de la `77`, que es el metodo
   de esta.

**LO QUE HAGO CON ELLO:** ninguna cifra de esta pagina sale de esos asuntos; todas salen de un instrumento corrido en esta fase, y
**donde coinciden lo digo como coincidencia y no como fuente**. **No he abierto nada de `.v80ext/` por dentro**, **ni
`bitacora/VEREDICTOS.jsonl` por dentro salvo una linea, por campo**: la `CORREGIDO` de `d183`, de la que solo imprimo su numero, sus dos
cuentas de caracteres y si su texto y su razon son las dos lineas de `.v79ext/frontera_grove.txt` (un texto que ya firme en la `ACTA 78`
`78.3`). **Mis clases de la tanda no las decido hoy**: son las de mis ficheros sellados de la `78`, que la `ACTA 77` sostuvo sin mover
ninguna. **Y ESTO SI PESA SOBRE MI LECTURA, Y LO DIGO:** el asunto de `2449c555` me dijo que la arista por lectura esta en el grafo
**antes** de releerla (seccion `5`); mi `SOSTENGO` es el que selle en la `78` y el que la `ACTA 77` `77.4` cruzo, y lo releo con el libro
delante, **pero no puedo probar que no me empujo**.

## 2. **EL CENSO, Y QUE LO UNICO QUE SE MOVIO ES LO QUE EL ENCARGO MANDABA** (`D.38.4`, `D.38.5`, `D.49`)

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        479 dataset/nodos.jsonl
       1226 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1706 total
    $ for d in cuarentena/marquet_turn_the_ship cuarentena/_insertados/marquet_turn_the_ship cuarentena/gerber_emyth cuarentena/_insertados/gerber_emyth; do echo "$d $(find $d -maxdepth 1 -name '*.json' 2>/dev/null | wc -l)"; done; echo "procesos $(ls -A procesos/ | wc -l)"
    cuarentena/marquet_turn_the_ship 0
    cuarentena/_insertados/marquet_turn_the_ship 20
    cuarentena/gerber_emyth 0
    cuarentena/_insertados/gerber_emyth 22
    procesos 0
    $ python .v70aud/poblacion.py
    poblacion: 479 | por sede: {'grafo': 479} | suma: 479
    $ python forja.py gate | head -2
    GATE VERDE.
      nodos verificados: 479
    $ python forja.py tablero | sed -n '11,13p;24p'
      1    7    grove_high_output              INSERTADO              NINGUNO                  0  cap_18
      2    9    gerber_emyth                   INSERTADO              NINGUNO                  0  cap_22
      3    5    marquet_turn_the_ship          INSERTADO              NINGUNO                  0  cap_17
      MUNDO 11 COMPLETO: los 7 libros del corte estan INSERTADOS (D.60).
    $ python .v80aud/censo_libros.py
    nodos por libro: {'manual_sistema_conocimiento': 2, 'onu_consumidor': 6, 'smart_who': 59, 'zhuo_manager': 136, 'scott_radical_candor': 142, 'grove_high_output': 92, 'gerber_emyth': 22, 'marquet_turn_the_ship': 20} | suma: 479
    aristas del grafo: 220 | entre libros distintos: 1 | dentro de un libro: 219 | suma: 220
    las aristas entre libros son la unica de la ACTA 78 78.10: SI

**Sin `git`, lo que cambio desde que escribi mi encargo, por tres instrumentos.** Primero, **cualquier fichero** del dato, de las
bandejas, del codigo, de la configuracion o de los dos registros de la linea con fecha de escritura posterior a mi encargo (las fichas
de una misma carpeta, juntas):

    $ find cuarentena dataset bitacora censos config fuentes esquema src scripts tests forja.py docs/loop/DEUDA.jsonl docs/loop/TABLERO.jsonl -type f -newer docs/loop/PROMPT_SIGUIENTE.md | sed 's|/[^/]*\.json$|/*.json|' | sort | uniq -c
          1 bitacora/VEREDICTOS.jsonl
          1 censos/denominaciones.md
          1 dataset/nodos.jsonl
          1 docs/loop/DEUDA.jsonl
          1 docs/loop/TABLERO.jsonl

Segundo, **las huellas que tome al lanzar mi barrido de la `78`** (las `20` fichas de Marquet y el grafo) contra los ficheros de hoy,
buscando en `_insertados` la ficha que ya no esta en la bandeja:

    $ python .v80aud/huellas_hoy.py
    huellas: 21 | {'grafo, aparte': 1, 'movida a _insertados, misma huella': 20} | suma: 21
    movidas a _insertados: 20 | son las 20 de .v78aud/las20.txt: SI | fichas en _insertados de Marquet fuera de ellas: []
    fichas que quedan en la bandeja de Marquet: 0
    ficheros que no cuadran: []

Tercero, **el grafo**: si al de hoy le quito las `20` filas de la tanda, y ademas los ids de las `20` de las listas de los nodos viejos,
sale el fichero que barri, byte a byte. **La vuelta `79` no movio el grafo** (mi `ACTA 78` `78.0` y `78.1`, con `git diff` y con estas
mismas huellas), asi que ese fichero es tambien el de la apertura de la `80`:

    $ python .v80aud/grafo_sin_tanda.py
    filas del grafo hoy: 479 | la reconstruccion reproduce el fichero de hoy: SI
    de las 20 de la tanda en el grafo: 20 | filas que quedan sin ellas: 459
    las 20 son las ultimas filas del fichero: SI
    (a) sin las 20 filas, sha1 igual a la huella de mi barrido de la 78: SI
    (b) nodos viejos con algun id de las 20 en alguna lista: 0 | sin esos ids, sha1 igual a la huella: SI

**Y las dos deudas que mi encargo manda pagar**, por campo y sin su prosa:

    $ python .v80aud/deudas_encargo.py
    d104 | anotada: SI | lineas de pago: 1, en la vuelta ['80'] | mi encargo la quiere pagada en la 80
    d183 | anotada: SI | lineas de pago: 1, en la vuelta ['80'] | mi encargo la quiere pagada en la 80
    lineas de DEUDA.jsonl con vuelta 80 (el campo es texto), por tipo e id: {'pago d104': 1, 'pago d183': 1} | suma: 2

**LECTURA:**

- **El grafo tiene `479` filas, la bitacora `1226` lineas, los pares mutuos `1`, la bandeja de Marquet `0` y sus insertados `20`, y
  `procesos/` esta vacio.** El tablero da a Marquet `INSERTADO` y **el mundo `11` completo**, y el censo por libro da `20` de Marquet
  sobre `479`. **Coincide con el *censo por libro (479)* del asunto de `d09a152a`**, y lo digo como coincidencia.
- **Las `20` fichas movidas a `_insertados` son las `20` de mi lista, con la huella que tenian cuando las barri**, y son las ultimas `20`
  filas del grafo.
- **(a) sale `SI`**: **los `459` nodos viejos son byte a byte los que barri**, sin quitarles nada; (b) lo confirma con `0` nodos viejos
  que tengan un id de la tanda en una lista. Dice tres cosas a la vez: **la arista de la tanda es entre dos nodos de la tanda** (seccion
  `4`), **ningun otro nodo del grafo cambio**, y **`d104` no toco el grafo**, que es lo que el encargo mandaba (*no toques el grafo por
  ella*). Coincide con el *ningun nodo viejo cambiado* de `2449c555`, y lo digo como coincidencia.
- **Las aristas entre libros siguen siendo una, la de la `ACTA 78` `78.10`**: la tanda no cablea nada con otro libro, y la arista nueva
  del grafo (`220` contra los `219` de aquella seccion) es la de dentro de Marquet.
- **La poblacion de hoy es `479`**, la de mi barrido de la `78`, toda ya en el grafo.
- **Lo que se escribio despues de mi encargo** es el grafo, la bitacora, un fichero de `censos/` y los dos registros de la linea: lo que
  escriben una insercion, un `corregir`, dos pagos y el arnes al arrancar; **nada en `config/`, `esquema/`, `fuentes/`, `src/`,
  `scripts/` ni `tests/`**. Las fichas movidas no salen en el `find` porque mover no cambia la fecha de escritura; las mide el segundo
  instrumento.
- **`d104` y `d183` tienen su linea de pago, en la `80`, y no hay ningun otro pago con esa vuelta**, que es lo que el encargo pedia
  (*no pagas ninguna deuda fuera de `d104` y `d183`*). **Lo que dice cada `--como`** lo firmo o no en mi turno normal, con la `ACTA 78`
  `78.3` delante.
- **La etiqueta existe y apunta a `69d407da`** (cabecera), el commit que el asunto de su T4 dice que dejo el grafo completo. **Que el
  grafo de ese commit sea el de `HEAD`** (`git diff --stat` vacio sobre el dato) **es `git`, y va a mi turno normal.**

## 3. **LAS `20`: LO QUE ENTRO ES LO QUE SE LEYO** (`D.58`), **`d183` Y SUS PASOS INVENTADOS** (`8`, `8.2`)

Cada nodo del grafo contra su ficha de `_insertados` (cuya huella es la leida, seccion `2`) en titulo, condiciones, pasos, entregable y
resumen, con la correccion de `d183` comprobada letra a letra; la linea `CORREGIDO` de la bitacora, por campo; y sus pasos contra **mi**
lectura entera sellada en la `78`, `.v78aud/fidelidad.tsv`, una fila por paso con su capitulo:

    $ python .v80aud/entra_lo_leido.py
    las 20 por sede hoy: {'grafo y _insertados': 20} | suma: 20
    nodos del grafo contra su ficha, cinco campos: {'igual en los cinco': 19, 'igual salvo el resumen, que es el de la ficha mas la linea ANADE de d183': 1} | suma: 20
    nodos con descuadre entre sus pasos en el grafo y mis filas selladas: 0 []
    lineas CORREGIDO de la bitacora sobre eliminar_seguimiento_descendente_responsabilizar_dueno: 1 | en la linea: [1226]
      linea 1226: texto anadido igual a la linea ANADE de .v79ext/frontera_grove.txt: SI | razon igual a la linea RAZON: SI | caracteres antes 2300, despues 5597
    cap_01 lo que ENTRO: candidatos 1 | pasos 6 | mis marcas: {'T': 6, 'P': 0, 'D': 0} | suma: 6 | PUENTE 0 de 6 = 0.00 por ciento
    cap_02 lo que ENTRO: candidatos 2 | pasos 10 | mis marcas: {'T': 10, 'P': 0, 'D': 0} | suma: 10 | PUENTE 0 de 10 = 0.00 por ciento
    cap_03 lo que ENTRO: candidatos 6 | pasos 53 | mis marcas: {'T': 51, 'P': 0, 'D': 2} | suma: 53 | PUENTE 0 de 53 = 0.00 por ciento
    cap_04 lo que ENTRO: candidatos 1 | pasos 5 | mis marcas: {'T': 5, 'P': 0, 'D': 0} | suma: 5 | PUENTE 0 de 5 = 0.00 por ciento
    cap_06 lo que ENTRO: candidatos 2 | pasos 8 | mis marcas: {'T': 8, 'P': 0, 'D': 0} | suma: 8 | PUENTE 0 de 8 = 0.00 por ciento
    cap_07 lo que ENTRO: candidatos 1 | pasos 3 | mis marcas: {'T': 3, 'P': 0, 'D': 0} | suma: 3 | PUENTE 0 de 3 = 0.00 por ciento
    cap_08 lo que ENTRO: candidatos 1 | pasos 5 | mis marcas: {'T': 5, 'P': 0, 'D': 0} | suma: 5 | PUENTE 0 de 5 = 0.00 por ciento
    cap_09 lo que ENTRO: candidatos 1 | pasos 2 | mis marcas: {'T': 2, 'P': 0, 'D': 0} | suma: 2 | PUENTE 0 de 2 = 0.00 por ciento
    cap_10 lo que ENTRO: candidatos 1 | pasos 3 | mis marcas: {'T': 3, 'P': 0, 'D': 0} | suma: 3 | PUENTE 0 de 3 = 0.00 por ciento
    cap_11 lo que ENTRO: candidatos 1 | pasos 3 | mis marcas: {'T': 3, 'P': 0, 'D': 0} | suma: 3 | PUENTE 0 de 3 = 0.00 por ciento
    cap_12 lo que ENTRO: candidatos 1 | pasos 8 | mis marcas: {'T': 8, 'P': 0, 'D': 0} | suma: 8 | PUENTE 0 de 8 = 0.00 por ciento
    cap_13 lo que ENTRO: candidatos 1 | pasos 2 | mis marcas: {'T': 2, 'P': 0, 'D': 0} | suma: 2 | PUENTE 0 de 2 = 0.00 por ciento
    cap_14 lo que ENTRO: candidatos 1 | pasos 2 | mis marcas: {'T': 2, 'P': 0, 'D': 0} | suma: 2 | PUENTE 0 de 2 = 0.00 por ciento
    los trece: candidatos 20 | pasos 110 | mis marcas: {'T': 108, 'P': 0, 'D': 2} | suma: 110 | PUENTE 0 de 110 | con las D cerradas T (ACTA 77 77.5): T 110, P 0, suma 110

**LECTURA:**

- **Las `20` viven en el grafo con los textos que se leyeron**, cada una con tantos pasos como filas tiene mi lectura. **La unica
  diferencia con su ficha es la que el encargo mandaba**: el resumen de `eliminar_seguimiento_descendente_responsabilizar_dueno` es el de
  su ficha, un espacio y **la linea `ANADE` de `.v79ext/frontera_grove.txt` tal cual**, que es el texto que la `ACTA 78` `78.3` firmo contra
  mis dos posiciones selladas de la `79`. **Su linea `CORREGIDO` es una sola**, la `1226`, con el texto y la razon del fichero, **y
  `corregir` rechaza un nodo que no vive en el grafo** (`src/correccion.py`, *no vive en el grafo*), asi que se escribio despues de que
  entrara la fila `16`. Coincide con el *linea 1226 de la bitacora* de `69d407da`, y lo digo como coincidencia.
- **`PASOS INVENTADOS` de lo que ENTRO: `0` en los trece capitulos**, que es la columna *PUENTE que entrara* que mi `ACTA 77` `77.3`
  firmo: los `3` PUENTE de la preparacion se corrigieron en la bandeja **antes** de mi barrido, y mis dos `D` (`cap_03`) las cerro `T` la
  `77.5` (`D78.6`), que no reabro (`D.47`). **Por debajo del `10`: no se baja escalon** (`8.1`), y de todos modos no queda lote de
  extraccion en el mundo `11`. **La relectura de fidelidad de `D.58` sobre lo que entra es esa lectura entera de la `78`**, porque lo que
  entro es byte a byte lo que lei; `R9` sobre esos `110` pasos lo cruzo la `77.3`. **`d183` no anade ningun paso**: `corregir` solo toca el
  resumen.

## 4. **LO QUE MI LECTURA ESPERA QUE LA VUELTA DEJE, Y EL ORDEN EN QUE ENTRO**

Sacado **solo** de mis ficheros sellados de la `78`; la bitacora, solo contada; **y las aristas del grafo, solo en cuentas y `SI` o `NO`,
despues de imprimir las esperadas**:

    $ python .v80aud/esperado.py
    pares sellados: 34 | por clase: {'SANO': 34} | suma: 34
    filas dirigidas de mi barrido con candidato de las 20: 52 | por vecino: {'vecino en la tanda': 42, 'vecino fuera de la tanda': 10} | suma: 52
    lineas de veredicto esperadas, por la clase de su par: {'SANO': 52} | suma: 52
    filas de mi lectura de aristas: {'SOSTENGO, arista por lectura': 1, 'DESCARTO': 5} | suma: 6
    aristas esperadas: 1 | CONTINUA con madre= 0 | por lectura 1 | en las dos: 0
      LECTURA   observar_reunion_rutinaria_senales_plantilla > seguir_frustrado_preguntar_implantacion_ideas
    extremos de esas aristas que no son de las 20: 0
    bitacora esperada: 1172 + 52 + 1 + 1 (d183) = 1226 | hoy (lineas): 1226 | IGUAL
    aristas del grafo con algun extremo en las 20: escritas en la madre 1 | en el hijo 1 | las dos listas dicen lo mismo: SI | el conjunto es el esperado: SI
    de las 1 esperadas, en el grafo por los dos lados: 1 | en el grafo y no esperadas: 0

**LECTURA, y lo que se compara en el turno normal, no aqui:**

- **Aristas: `1`, por lectura, `observar_reunion_rutinaria_senales_plantilla` madre de `seguir_frustrado_preguntar_implantacion_ideas`,
  con los dos extremos dentro de las `20`.** **Y el grafo tiene exactamente esa, escrita por los dos lados, ninguna de mas.** Coincide
  con el *la arista por lectura en el grafo* de `2449c555`, y lo digo como coincidencia.
- **Lineas de bitacora.** Si cada `insertar` escribio una linea por fila dirigida que su aduana levanto, y la aduana levanto lo que mi
  barrido, son `52`, todas `SANO` por la clase de su par; la arista por lectura escribe **una** mas, y `corregir` **otra**. **La bitacora
  tiene las `1226` que eso da.** **Es coincidencia de cuenta y no de contenido**: de las `54` nuevas solo he abierto la de `corregir`, y
  por campo. **Mi lectura no espera ningun vecino sin linea preparada**, porque la poblacion es la del barrido (seccion `2`); uno que
  apareciera seria un hallazgo, y la cuenta no deja sitio para el.

**El orden en que entraron, leido del grafo** (`src/aduana.py` escribe `nodos + [nuevo]`, asi que el orden de las filas es el de entrada),
contra el bloque de orden de mi encargo y contra las siete restricciones que selle en la `78`, leidas de su instrumento:

    $ python .v80aud/orden_grafo.py
    orden de entrada leido del grafo: 20 filas | el del bloque de mi encargo: 20 filas | fila a fila iguales: SI
       1 ceder_control_reforzar_competencia_claridad
       2 cambiar_forma_trabajar_conservar_plantilla
       3 encargar_meta_especifica_dejar_libre_metodo
       4 observar_reunion_rutinaria_senales_plantilla
       5 seguir_frustrado_preguntar_implantacion_ideas
       6 contar_firmas_cadena_tramite_parado
       7 inspeccionar_reparto_informacion_notas_jefe
       8 recorrer_organizacion_escuchar_plantilla
       9 auditar_formacion_premios_ultima_fila
      10 informar_cierre_jornada_conservar_propiedad_trabajo
      11 aplicar_ejercicio_codigo_genetico_control
      12 asignar_responsable_unico_evolucion_planificada
      13 reforzar_principios_guia_lenguaje_prueba_conocimiento
      14 declarar_intencion_reemplazar_peticion_permiso
      15 resistir_dar_solucion_clasificar_decision_urgencia
      16 eliminar_seguimiento_descendente_responsabilizar_dueno
      17 acoger_inspectores_externos_fuente_aprendizaje
      18 tomar_accion_deliberada_pausar_vocalizar_gesticular
      19 identificar_temas_formacion_tarjetas_decision
      20 repetir_mensaje_invariable_diario_reunion_evento
      cumple  4 observar_reunion_rutinaria_senales_plantilla         antes que  5 seguir_frustrado_preguntar_implantacion_ideas        obliga
      cumple  5 seguir_frustrado_preguntar_implantacion_ideas        antes que 17 acoger_inspectores_externos_fuente_aprendizaje       D.36 de un solo lado
      cumple  8 recorrer_organizacion_escuchar_plantilla             antes que 17 acoger_inspectores_externos_fuente_aprendizaje       D.36 de un solo lado
      cumple  8 recorrer_organizacion_escuchar_plantilla             antes que  9 auditar_formacion_premios_ultima_fila                D.36 de un solo lado
      cumple 10 informar_cierre_jornada_conservar_propiedad_trabajo  antes que 14 declarar_intencion_reemplazar_peticion_permiso       D.36 de un solo lado
      cumple 13 reforzar_principios_guia_lenguaje_prueba_conocimiento antes que 14 declarar_intencion_reemplazar_peticion_permiso       D.36 de un solo lado
      cumple  7 inspeccionar_reparto_informacion_notas_jefe          antes que  8 recorrer_organizacion_escuchar_plantilla             D.36 de un solo lado
    restricciones: 7 | {'obliga, la cumple': 1, 'D.36 de un solo lado, la cumple': 6} | suma: 7

**LECTURA:** **las `20` entraron en el orden que mi encargo pego, fila a fila**, y **las siete restricciones se cumplen**: la que obliga
(`observar` antes que `seguir`, filas `4` y `5`) y las seis de `D.36` de un solo lado, informativas. **Que cada `insertar` volviera antes
de lanzar el siguiente, y que la arista se declarara justo despues de la fila `5`, lo miro en mi turno normal.**

## 5. **MI CLASIFICACION DE CADA CANDIDATO, Y LA UNICA ARISTA RELEIDA** (`6.1`, y solo la vara `6.1`)

**Las `20`, una por una, en su orden de entrada**, de mis ficheros sellados: las lineas del libro que sus pasos transcriben, las filas
dirigidas de mi barrido en las que es candidata, sus pares sin orden por clase, y las aristas que mi lectura le espera como hija y
cuantas como madre:

    $ python .v80aud/clasificacion_20.py
     1 cap_01 ceder_control_reforzar_competencia_claridad            NODO | L97 a L97 | filas 1 | pares {'SANO': 1} suma 1 | hija: ninguna | madre de: 0
     2 cap_02 cambiar_forma_trabajar_conservar_plantilla             NODO | L25 a L29 | filas 2 | pares {'SANO': 2} suma 2 | hija: ninguna | madre de: 0
     3 cap_02 encargar_meta_especifica_dejar_libre_metodo            NODO | L33 a L49 | filas 3 | pares {'SANO': 3} suma 3 | hija: ninguna | madre de: 0
     4 cap_03 observar_reunion_rutinaria_senales_plantilla           NODO | L17 a L21 | filas 3 | pares {'SANO': 3} suma 3 | hija: ninguna | madre de: 1
     5 cap_03 seguir_frustrado_preguntar_implantacion_ideas          NODO | L23 a L29 | filas 6 | pares {'SANO': 7} suma 7 | hija: LECTURA de observar_reunion_rutinar | madre de: 0
     6 cap_03 contar_firmas_cadena_tramite_parado                    NODO | L37 a L43 | filas 2 | pares {'SANO': 2} suma 2 | hija: ninguna | madre de: 0
     7 cap_03 inspeccionar_reparto_informacion_notas_jefe            NODO | L45 a L53 | filas 2 | pares {'SANO': 3} suma 3 | hija: ninguna | madre de: 0
     8 cap_03 recorrer_organizacion_escuchar_plantilla               NODO | L11 a L15 | filas 3 | pares {'SANO': 5} suma 5 | hija: ninguna | madre de: 0
     9 cap_03 auditar_formacion_premios_ultima_fila                  NODO | L55 a L57 | filas 2 | pares {'SANO': 2} suma 2 | hija: ninguna | madre de: 0
    10 cap_04 informar_cierre_jornada_conservar_propiedad_trabajo    NODO | L35 a L35 | filas 6 | pares {'SANO': 7} suma 7 | hija: ninguna | madre de: 0
    11 cap_06 aplicar_ejercicio_codigo_genetico_control              NODO | L101 a L111 | filas 1 | pares {'SANO': 1} suma 1 | hija: ninguna | madre de: 0
    12 cap_06 asignar_responsable_unico_evolucion_planificada        NODO | L127 a L127 | filas 0 | pares {} suma 0 | hija: ninguna | madre de: 0
    13 cap_14 reforzar_principios_guia_lenguaje_prueba_conocimiento  NODO | L89 a L99 | filas 3 | pares {'SANO': 4} suma 4 | hija: ninguna | madre de: 0
    14 cap_07 declarar_intencion_reemplazar_peticion_permiso         NODO | L55 a L87 | filas 4 | pares {'SANO': 4} suma 4 | hija: ninguna | madre de: 0
    15 cap_08 resistir_dar_solucion_clasificar_decision_urgencia     NODO | L107 a L121 | filas 5 | pares {'SANO': 5} suma 5 | hija: ninguna | madre de: 0
    16 cap_09 eliminar_seguimiento_descendente_responsabilizar_dueno NODO | L71 a L73 | filas 0 | pares {} suma 0 | hija: ninguna | madre de: 0
    17 cap_10 acoger_inspectores_externos_fuente_aprendizaje         NODO | L45 a L49 | filas 6 | pares {'SANO': 6} suma 6 | hija: ninguna | madre de: 0
    18 cap_11 tomar_accion_deliberada_pausar_vocalizar_gesticular    NODO | L75 a L95 | filas 3 | pares {'SANO': 3} suma 3 | hija: ninguna | madre de: 0
    19 cap_12 identificar_temas_formacion_tarjetas_decision          NODO | L125 a L139 | filas 0 | pares {} suma 0 | hija: ninguna | madre de: 0
    20 cap_13 repetir_mensaje_invariable_diario_reunion_evento       NODO | L119 a L119 | filas 0 | pares {} suma 0 | hija: ninguna | madre de: 0

**LECTURA: LAS `20` SON NODO**, con la clase de cada par que selle en la `78` y que la `ACTA 77` `77.4` encontro igual en sus `52` lineas
preparadas. **No cambio ninguna**: lo que entro es byte a byte lo que lei (secciones `2` y `3`). **Cuatro no tienen vecino en la
poblacion** (`asignar_responsable`, `eliminar_seguimiento`, `identificar_temas` y `repetir_mensaje`), y por eso no escriben linea.
**`eliminar_seguimiento_descendente_responsabilizar_dueno` no tiene vecino en el barrido y si una frontera declarada con Grove**: el
barrido no levanta `delegar_tarea_base_comun_seguimiento`, y la `ACTA 77` `77.5` la leyo como *dos doctrinas legitimas* (`6.1`), que
no se funden: se escriben sus dos posiciones, y eso es lo que `d183` escribio (seccion `3`).

**LA UNICA ARISTA, RELEIDA HOY CON EL LIBRO Y LOS PASOS DELANTE.** Las lineas que cita mi fila sellada, y la que abre la reunion y la
que sigue:

    $ python .v80aud/lineas_fuente.py
    cap_03 L19 (557 caracteres): I looked around at the four department heads. These were the key individuals I would go to war with, entrust the lives of the 135 crew members to, and possibly die with. I felt bad for these guys: the attendees wandered in late, and the captain stayed away until everyone was assembled. Then he was invited. The meeting started late. It might seem like a little thing, but on board a nuclear submarine, little things like lack of punctuality are indicative of much, much bigger problems. At this particular meeting, everyone was waiting for someone else.
    cap_03 L21 (584 caracteres): The meeting started. Lieutenant Dave Adams, the weapons officer (Weps), briefed a problem with the vertical launch system (VLS) in the bow of the sub. There was a long discussion about O-rings, seals, and retests. I probably should have paid attention to the technical issues because this missile system wasn't on the Olympia so I hadn't paid attention to it during my training, but instead I observed the people in the room. Dave was earnest and forthright but frustrated and defensive about all the questions he needed to answer. The other department heads and chiefs were bored.
    cap_03 L23 (54 caracteres): After the meeting I followed Dave to his stateroom.
    cap_03 L25 (39 caracteres): "Weps, you seemed a bit frustrated."

Y los pasos de sus dos nodos, por `pasos_ciego.py` (`R6`), que hoy los encuentra en el grafo:

    $ python .v67aud/normal/pasos_ciego.py observar_reunion_rutinaria_senales_plantilla seguir_frustrado_preguntar_implantacion_ideas
    ===== observar_reunion_rutinaria_senales_plantilla | grafo
      titulo: Sentarse en una reunion rutinaria que ya existe y leerla por sus senales de gente en vez de por su asunto tecnico
      fuente: ['marquet_turn_the_ship']
      cond: Cuando entras nuevo en una organizacion y tienes delante una de sus reuniones de repaso rutinarias, de las que ya existen y no convocas tu.
      P1. Asiste a una reunion rutinaria de repaso de la organizacion. La del texto es una reunion de jefes de departamento, un repaso rutinario de asuntos de mantenimiento.
      P2. No atiendas al asunto tecnico: observa a la gente de la sala. El texto lo escribe como eleccion deliberada, y dice incluso que probablemente deberia haber atendido a lo tecnico porque ese sistema de misiles no estaba en su barco anterior y no lo habia mirado en su instruccion.
      P3. Mira quien llega tarde y como llega. En el texto los asistentes iban entrando tarde.
      P4. Mira si el jefe se queda fuera hasta que estan todos reunidos y entra despues, invitado. Es lo que el texto describe.
      P5. Mira si la reunion empieza tarde.
      P6. Mira a quien esta esperando cada uno. En esa reunion, dice el texto, todos estaban esperando a algun otro.
      P7. Mira como esta el que expone. El texto describe al suyo serio y directo, pero frustrado y a la defensiva ante todas las preguntas que tenia que contestar.
      P8. Mira como estan los demas. Los otros jefes de departamento y los suboficiales estaban aburridos.
      P9. Lee la falta de puntualidad con la regla que el texto escribe: puede parecer una cosa pequena, pero a bordo de un submarino nuclear las cosas pequenas como la falta de puntualidad son indicativas de problemas mucho, mucho mayores.
    ===== seguir_frustrado_preguntar_implantacion_ideas | grafo
      titulo: Seguir al que viste frustrado en una reunion y preguntarle, idea por idea, como la implanto
      fuente: ['marquet_turn_the_ship']
      cond: Cuando acabas de ver en una reunion a un responsable frustrado o a la defensiva y quieres saber si la causa esta en el o en el sistema en que trabaja.
      P1. Al acabar la reunion, siguelo a su sitio de trabajo. El texto lo dice asi: despues de la reunion segui a Dave a su camarote.
      P2. Nombrale lo que viste. La frase del texto es que parecias un poco frustrado.
      P3. Dejale contar la vision que tiene de como quiere que funcione lo suyo, y escuchale hasta el final. El texto registra que al escucharle se fue poniendo cada vez mas entusiasmado e impresionado, y que a el lo estaban ignorando.
      P4. Segun vaya desgranando las ideas que tiene para mejorar su area, pregunta por cada una como la implanto.
      P5. Fijate en si la respuesta es siempre la misma. En el texto lo fue todas las veces: alguien mas arriba en la cadena de mando no habia apoyado la iniciativa, asi que no paso nada.
      P6. Mira si lo mismo pasa un piso mas abajo. El texto registra que los suboficiales que trabajaban para el tampoco parecian dispuestos a salir con ideas propias.
      P7. Quedate con el ejemplo concreto que salga de ahi. El del texto es el adiestramiento de ataque con misiles Tomahawk que habia querido dar a los oficiales varias veces, con el examen de enero por delante, y que o no se llego a programar nunca o se cancelo.
      P8. Lee el resultado como el texto lo lee: en esencia te estaba describiendo un problema propio del modelo de lider a seguidores, aunque no usara esas palabras.

**LECTURA: MANTENGO `observar_reunion_rutinaria_senales_plantilla` MADRE DE `seguir_frustrado_preguntar_implantacion_ideas`, arista por
lectura `D.29`.** Lo que el hijo anade a la madre (`6.1`, con direccion): la madre **mira** la reunion por su gente y deja visto, en su
paso `7`, **al que expone frustrado y a la defensiva** (`L21`, *frustrated and defensive about all the questions he needed to answer*); la
condicion del hijo **es ese producto con sus palabras** (*Cuando acabas de ver en una reunion a un responsable frustrado o a la
defensiva*), y su paso `1` arranca donde la madre acaba (`L23`, *After the meeting I followed Dave to his stateroom*). **El hijo anade** lo
que la madre no trae: nombrar lo visto (`L25`), escuchar y preguntar idea por idea como se implanto, y leer el patron. **Procedimiento en
los dos lados fuera del solape, sin bascula**, y ningun paso repetido: no es `REPITE`. **El barrido no levanta el par** en ningun sentido (el bloque
de abajo, sobre mi tabla de vecinos y mis clases selladas), y por eso va por `D.29` y no por linea (`D.53`). **La lectura contraria, escrita como la escribi en la
`78`:** si el paso `7` se lee como una senial entre ocho y no como producto, el par seria `SANO` con esta misma arista; **no cambia nada
del grafo**, y la `ACTA 77` `77.4` la sostuvo en su direccion.

    $ grep -c -E "observar_reunion_rutinaria_senales_plantilla +[>~] +seguir_frustrado|seguir_frustrado_preguntar_implantacion_ideas +[>~] +observar_reunion" .v78aud/vecinos_tabla.txt; grep -c -E "observar_reunion_rutinaria_senales_plantilla.seguir_frustrado|seguir_frustrado_preguntar_implantacion_ideas.observar_reunion" .v78aud/mis_clases.tsv
    0
    0

**Y LO QUE ESTA RELECTURA NO PUEDE DECIR:** con que veredicto de lectura se escribio su linea en la bitacora (mi encargo le pedia
`CONTINUA`, `D.53`) y que razon puso. **La arista vive** (seccion `4`), y lo decido con su reporte y su linea delante, en mi turno normal.

## 6. **`R8` MEDIDO SOBRE MI ENCARGO DE LA `80`, CON EL MISMO INSTRUMENTO** (`ACTA 78` `78.11`, `78.12`)

`R8` dice: *toda cifra de medida que escriba en `PROMPT_SIGUIENTE.md` (un reloj, una banda, una cuenta que solo se comprueba abriendo
un fichero, en digito o en letra) va DENTRO de un bloque `$` con su salida, o lleva EN SU MISMA LINEA la seccion del acta donde esta
pegada: ni la de la linea de al lado, ni una ruta de fichero*. El fichero es el encargo que escribi al cerrar la `ACTA 78`, y el
instrumento es el de la `78.12`, corrido sin copiarlo, con su salida de hoy contra la que guardo aquella acta:

    $ head -1 docs/loop/PROMPT_SIGUIENTE.md | cut -c1-100; ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, $7, $9}'
    # ENCARGO DE LA VUELTA 80: **LAS `20` FICHAS DE MARQUET DENTRO, UNA POR VEZ, EN SU ORDEN, CON LAS LI
    2026-09-26 17:27:31.821392600 docs/loop/PROMPT_SIGUIENTE.md
    $ python .v79aud/normal/r8_encargo80.py | diff - .v79aud/normal/r8_encargo80.txt && echo "IDENTICO a .v79aud/normal/r8_encargo80.txt, la salida de la ACTA 78 78.12"; python .v79aud/normal/r8_encargo80.py | tail -1
    IDENTICO a .v79aud/normal/r8_encargo80.txt, la salida de la ACTA 78 78.12
    lineas del encargo: {'linea de bloque sangrado': 40, 'prosa con numero, con seccion de la ACTA 78': 17, 'prosa con numero, sin seccion de la ACTA 78': 58, 'prosa sin digito ni palabra de numero': 60} | suma: 175

Las lineas de prosa con numero y **sin** seccion, cada una con los numeros que el instrumento le ve:

    $ python .v79aud/normal/r8_encargo80.py | grep -E "^  L[0-9]+ - " | sed -E 's/\] \|.*$/]/'
      L3 - ['11', '78', '79'] []
      L4 - ['1.4'] []
      L14 - ['0'] []
      L23 - ['17'] []
      L24 - ['11', '8', '3', '78'] []
      L30 - ['77', '80'] []
      L32 - ['77', '78'] []
      L33 - ['78', '80'] []
      L34 - ['78'] []
      L36 - ['78', '77', '77.4', '77.5'] []
      L37 - ['29', '75', '75.4', '77'] []
      L38 - ['77', '53'] []
      L39 - ['77', '77.4'] []
      L42 - ['1173', '78', '78'] []
      L46 - ['81', '77', '75'] []
      L54 - ['1', '78', '104'] []
      L56 - ['47'] []
      L67 - ['104', '104', '80', '80', '104'] []
      L69 - ['29'] []
      L71 - ['2'] []
      L73 - ['78', '78'] []
      L75 - ['1', '78', '78'] []
      L77 - ['3', '20', '78', '77', '77.4'] []
      L106 - ['1', '1'] []
      L107 - ['78'] []
      L108 - ['2', '29'] ['dos']
      L109 - ['7'] []
      L110 - ['5'] []
      L111 - ['3', '031'] []
      L112 - ['78'] ['dos']
      L113 - ['6.1'] []
      L115 - ['4', '77', '78'] []
      L116 - ['31'] []
      L117 - ['5'] []
      L118 - [] ['dos']
      L123 - ['16'] []
      L124 - [] ['dos']
      L125 - ['79', '183'] []
      L126 - ['183', '80', '78'] []
      L129 - ['5', '8', '4', '5'] []
      L134 - ['78'] []
      L135 - ['77', '77.3'] ['cero']
      L136 - ['61'] []
      L137 - ['5', '64', '64', '64'] []
      L138 - ['80', '9'] []
      L144 - ['1', '11'] []
      L146 - ['2', '80'] []
      L148 - ['3'] []
      L151 - ['4'] []
      L154 - ['80'] []
      L155 - ['79'] []
      L156 - ['8', '5'] []
      L163 - ['183', '4'] []
      L165 - ['3.3'] []
      L167 - ['7', '55'] []
      L169 - ['104', '183'] []
      L170 - ['183'] []
      L174 - [] ['Cero', 'cero']

**LECTURA, grupo a grupo, que es mia y no del instrumento; las volvi a leer una a una y no copio la de la `78.12`, aunque llego al
mismo reparto:**

- **Numeros de vuelta, de acta, de mundo o de carpeta de la casa**: `L3`, `L24`, `L30`, `L32` a `L34`, `L46`, `L73`, `L75`, `L107`,
  `L112`, `L115`, `L125`, `L126`, `L134`, `L137`, `L138`, `L146`, `L154`, `L155` (`75`, `77`, `78`, `79`, `80`, `81`, `11`, y
  `.v64ext/`, `.v64aud/`, `.v77ext/`, `.v78ext/`, `.v78aud/`, `.v79ext/`, `.v80ext/`).
- **Secciones, reglas, deudas, remedios y numeros de tarea, de punto o de lista**: `L4`, `L14`, `L24`, `L36` a `L39`, `L54`, `L56`,
  `L67`, `L69`, `L71`, `L77`, `L106`, `L108`, `L111`, `L113`, `L115` a `L117`, `L123`, `L125`, `L126`, `L129`, `L135` a `L137`, `L144`,
  `L146`, `L148`, `L151`, `L156`, `L163`, `L165`, `L167`, `L169`, `L170` (`1.4`, `0`, `3.3`, `6.1`, `75.4`, `77.4`, `77.5`, `D.29`,
  `D.31`, `D.47`, `D.53`, `D.55`, `D.61`, `7.F`, `d031`, `d104`, `d183`, `R5`, `R9`, las secciones `8` puntos `3` a `5` de `PARALELO.md`, y
  los numeros de tarea y de punto). **`L77` trae *las `20` filas* con la `ACTA 77` `77.4` en su misma linea**, que pega *filas del
  orden: 20*; el instrumento solo busca secciones de la `ACTA 78`, y la cabecera del encargo admite las dos actas.
- **Identificadores**: `cap_17` (`L23`), el *paso `7`* de la madre (`L109`), las *filas* `1`, `5` y `16` de `.v78ext/orden.txt` (`L106`,
  `L110`, `L123`, que el bloque de la TAREA `3` imprime), y la linea `1173` de la bitacora (`L42`).
- **Palabras de numero sin seccion**: *los dos extremos* (`L108`, los de una arista), *los dos delante* (`L112`, los dos nodos de un par),
  *los dos lados* (`L118`, los extremos de una arista), *las dos lineas de* `.v79ext/frontera_grove.txt` (`L124`, que son la de `ANADE` y
  la de `RAZON`, nombradas en esa misma linea), *en cero que entran* (`L135`, con la `ACTA 77` `77.3` en su misma linea) y *cero guiones*
  (`L174`, la frase fija). **Ninguna es una cuenta de fichero sin su sitio.**

**LA QUE MAS SE ACERCA, Y LA DEJO ESCRITA PARA QUE SE JUZGUE:** `L42`, *`1173` en adelante*. Es el numero de una linea de la bitacora, no
una cuenta, y sale de la `1172` medida, que la linea `L41` lleva con su `78.1` dentro del mismo parentesis que se cierra en `L42`; la
`78.12` lo leyo igual. **Pero la letra de `R8` dice *en su misma linea*, y `1173` no trae la suya.** Lo cuento como identificador, como
aquella acta, y no como cifra de medida; si se juzga cifra, **es un `R8` roto mio en el encargo de la `80`**, y lo cargaria mi turno normal.

**LAS CUENTAS EN LETRA**, que el instrumento ve por palabra y que busco tambien con un `grep` mas ancho:

    $ grep -n -i -w -E "uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|veinte|treinta|cero|mil|cien|ambas|ambos" docs/loop/PROMPT_SIGUIENTE.md | cut -c1-120
    62:| **Tu texto de Grove es el de las dos posiciones del auditor**, y queda listo tal cual | `78.3` |
    63:| **Tus cuatro discutibles se sostienen**, `D79.1` a `D79.4`; **`d104`, adjudicada**: ni `D.37` ni `D.29` dan arista,
    65:| **Una caida tuya de `REPORTE` que no acumula**: el bloque de `79.3.1` pega un `grep` con comillas invertidas entre
    103:      CONTINUA con madre= (aristas distintas): 0 | SOSTENGO por lectura: 1 | solapes entre las dos: 0 | aristas espe
    108:2. **La arista por lectura se declara EN EL ACTO DE INSERTAR EL HIJO** (`D.29`), con los dos extremos ya vivos: `obs
    111:3. **La puerta es la aduana de `insertar`, no la lista** (`d031`). **Al volver cada uno, su vecindad de hoy contra l
    112:   `78`** con tu copia de `contra_barrido.py`, pegada en su fila. Si levanta un vecino sin linea, lo lees con los pa
    118:   esperaban, cuantas viven por los dos lados, ninguna sin adjudicar, y que ningun nodo viejo cambio fuera del `nodo
    124:eliminar_seguimiento_descendente_responsabilizar_dueno --anade "<la linea de ANADE>" --razon "<la linea de RAZON>"`
    135:  corregidos en la bandeja, que la `ACTA 77` `77.3` firmo en cero que entran. No a ojo.
    163:- **NO CORRIGES NINGUN NODO DEL GRAFO** fuera de `d183` (TAREA `4`). Si una lectura de vecino te ensenia un defecto
    174:**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo t

**LECTURA, linea a linea:** `L103` esta **dentro de un bloque `$`**; `L62` (*las dos posiciones*) y `L63` (*cuatro discutibles*) son filas
de la tabla de la TAREA `1` con su `78.3` al final de su misma linea, y `L65` (*las cinco rachas siguen en cero*) es otra fila
de esa tabla, con `78.1`, `78.2` y `78.7` al final de la suya; `L108`, `L112`, `L118`, `L124`, `L135` y `L174` son los de la lista
de arriba; `L111` (*al volver cada uno*) es **una manera**, no una cuenta, y `L163` (*en uno*) es un pronombre. **Ninguna linea
de prosa trae una cifra de medida sin su bloque o su seccion en la misma linea, con la salvedad escrita de `L42`: `R8` CUMPLIDO en
el encargo de la `80`.**

## 7. **LO QUE DEJO PARA MI TURNO NORMAL, ESCRITO ANTES DE VER EL REPORTE**

1. **`R5`** en su reporte, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` sacados otra vez de los originales y con la
   cabecera cambiada a la `80`; y **`R9`**, si publica una cuenta de PUENTE, **contra la seccion `3`**.
2. **Las `54` lineas nuevas de la bitacora, una a una** (seccion `4`): las `52` de veredicto contra `.v78ext/veredictos_listos.txt` y contra
   mis clases selladas, **par a par contra las filas de mi barrido**; la de la arista, con su paso `7` y su veredicto de lectura (`D.53`); y
   la de `corregir`.
3. **Que cada `insertar` volvio con su `.fin` en `0`, en el orden, uno por vez y sin solaparse**; que **ninguna aduana levanto un vecino
   fuera de mi barrido**; y que la arista se declaro justo despues de la fila `5`.
4. **La muestra pineada de los `SANO`** que la `80` escribio en la bitacora, **con semilla `80`**, el tamanio de la seccion `7` de
   `AUDITOR_FORJA.md` y su banda, releida contra mis clases selladas, que es lo que la `ACTA 78` `78.5` dejo para la `ACTA 79`.
5. **Los pagos de `d104` y `d183`**: lo que dice cada `--como`, contra la `ACTA 78` `78.3`, para firmarlos o no.
6. **El tag**: que `69d407da` sea el commit en que el grafo quedo completo (la ultima fila o `d183`, el posterior), con `git diff --stat`
   vacio contra `HEAD` sobre el dato, y que este empujado.
7. **El censo con `git diff`, las guardas y el cierre estricto**, que tallara esta pagina: no tiene tablas, asi que un rojo en el suyo
   sera suyo. Y el coste de su turno (bloque de la cabecera) contra su clase (`D.55`).
8. **Si la tanda se sostiene, el cierre de la campania**: `PARA_ALEXIS.md` con lo que `PARALELO.md` `4.c` pide y `PROMPT_SIGUIENTE.md`
   vacio (`ACTA 78` `78.10`); y **`R10`** en la `ACTA 79`.

## 8. **ESTA PAGINA CONTRA `R6`, `R7` Y LOS GUIONES, MEDIDA SOBRE ELLA MISMA**

El generador corre dos veces, y estos bloques de la segunda pasada leen la pagina que escribio la primera, identica salvo estos
bloques. El primero cuenta las lineas de bloque `$` que empiezan por una clave de relacion; el segundo, con la copia de
`.v79aud/r7_pagina.py`, cuenta las lineas de bloque que reparten una cifra en clases y cuantas traen su `suma`; el tercero cuenta
guiones largos y medios:

    $ grep -c -E "^    +(previos|siguientes|nodos_previos|nodos_siguientes)" docs/loop/APERTURA_CIEGA.md
    0
    $ python .v80aud/r7_pagina.py
    lineas de bloque que reparten en clases: 43 | por estado: {'con suma': 43} | suma: 43
    $ grep -c -P "\x{2014}|\x{2013}" docs/loop/APERTURA_CIEGA.md
    0
