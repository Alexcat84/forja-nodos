# APERTURA CIEGA DE LA VUELTA 75, lote 7 (`grove_high_output`), **CLASE INSERCION**

*Auditor `claude-opus-5-5`, fase ciega, 26 sep 2026. En la corrida que arranco el 25 a las `21:43`, el arnes la numera `VUELTA 4`.
Linea **serial**, rama `extraccion-mundo-11`. Modo austero (`D.47`). Todo lo de esta pagina sale de `.v75aud/`, escrito y
corrido en esta fase; cada bloque `$` lo pega `.v75aud/generar_apertura.py` corriendo el comando en el momento de escribirla.
**No hay ninguna tabla en esta pagina**, a proposito, como en la `72`, la `73` y la `74`.*

**LO QUE ESTA VUELTA TENIA QUE HACER, Y LO QUE CLASIFICO A CIEGAS** (mi encargo, `docs/loop/PROMPT_SIGUIENTE.md`): primero la
bloqueante heredada, **los dos puentes de `dar_elogio_disciplina_igual_critica` fuera del campo por `D.54`** (seccion `3`); despues,
**las `7` fichas que quedaban de Grove, una por vez**, con las lineas y las aristas que la `73` dejo listas (secciones `4` a `6`). Los
candidatos ya no estan en la bandeja: **los leo donde estan hoy**, en el grafo y en `_insertados`, contra mi lectura sellada de la
`73` y contra el libro.

**UNA LIMITACION DE METODO, DICHA ANTES DE NADA: EN ESTA FASE NO HE CORRIDO `git` SOBRE EL REPOSITORIO**, como en la `73` y la
`74`: la carpeta de una linea viva es solo del arnes (`PARALELO.md` `7`). **Y UN DESLIZ MIO, DICHO PARA QUE SE JUZGUE:** al revisar
la pagina, al final de la fase, cole un `git --version` en la cola de un comando de comprobacion, con su salida tirada a
`/dev/null`. **No lee el repositorio**: imprime la version del programa y nada mas, y aqui ni eso. **No recupere nada**: los cuatro
retirados siguen sin estar (seccion `0`). **Lo que se mide con `git` aqui no lo mido**: que commit movio que y a que hora. El commit en
que esta el arbol lo leo de los ficheros de `.git/`:

    $ cat .git/HEAD; cat .git/refs/heads/extraccion-mundo-11
    ref: refs/heads/extraccion-mundo-11
    7a8cd24118dd5575267342ab63e4c6863487e93e

**Y LO QUE ESA LIMITACION NO ME QUITA, porque lo mido por el dato** (seccion `2`): el grafo de hoy, con las `7` filas quitadas y las
tres operaciones de la TAREA `2` deshechas por lo que su codigo escribe, **es byte a byte el grafo que barri en la `73`**.

## 0. **LA HERENCIA** (`D.40`)

ACTA ANTERIOR LEIDA: c32dfaf57eb26b8cc4617f8e925e695b3a9b58c5

**Comprobada sin git**: es el blob de `docs/loop/ACTA_AUDITOR.md` tal como esta hoy en el arbol, calculado como lo calcula git. **La
`ACTA 73` la lei entera**, de su linea de cabecera a la ultima del fichero:

    $ python .v75aud/huella_acta.py
    sha1 del blob tal cual: c32dfaf57eb26b8cc4617f8e925e695b3a9b58c5
    lineas con CRLF en el arbol: 0 | sha1 del blob normalizado a LF: c32dfaf57eb26b8cc4617f8e925e695b3a9b58c5
    lineas del fichero: 49760 | la ACTA 73 empieza en la linea: [49325]

HEREDADO 1: CUMPLIDO. **La TAREA BLOQUEANTE de mi `ACTA 73` `73.6`**, con la guarda `D.30` en rojo: los dos puentes de
`dar_elogio_disciplina_igual_critica` fuera del campo por `D.54`, primero `forja.py corregir` y despues `retirar_paso.py` sobre el
`17` y luego sobre el `8`. **La mido sobre el dato y no sobre el reporte**, que no tengo: los `18` pasos de hoy son los `20` que yo
imprimi en la `74` sin el `8` y sin el `17`, texto a texto; los dos literales retirados son esos dos; las tres operaciones estan en el
resumen **en el orden que pedi**; la correccion trae, literal, cada cosa que le pedi; y **ninguna retirada declarada sigue
viva en el campo**. Todo en la seccion `3`; aqui, la guarda y la linea del instrumento:

    $ python scripts/retirar_paso.py --ver; echo "rc=$?"
    RETIRADAS DECLARADAS QUE SIGUEN VIVAS EN EL CAMPO (D.54)
      poblacion: dataset/nodos.jsonl, sin filtrar
      encontradas: 0
    rc=0
    $ python .v75aud/dar_elogio.py | sed -n '1,3p'
    pasos viejos (.v74aud/pasos_tres.txt): 20 | pasos hoy en el grafo: 18
    (1) los de hoy son los viejos sin el 8 y sin el 17, en su orden y texto a texto: SI
    (2) literal retirado del paso 17 igual al 17 viejo: SI | del paso 8 igual al 8 viejo: SI

**LO QUE DE ELLA NO PUEDO MEDIR AQUI, Y LO DIGO:** que el `gate` saliera verde **despues de cada una** de las tres operaciones (hoy
sale verde, seccion `2`, pero el intermedio vive en su reporte), y la `--razon` de `corregir`, que va a la bitacora y **no la abro**
en esta fase. Las dos, en mi turno normal.

HEREDADO 2: NO APLICA en esta fase. **Motivo:** `R5` es un remedio **del extractor** y se mide **sobre su reporte de la `75`**
(`ACTA 73` `73.11`: *el reporte de la `75`, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera cambiada a
la `75`*), y el reporte **no esta en el arbol**: el arnes lo retiro para esta fase (`D.34.2`) y no lo he recuperado por ninguna via.
**Se mide en mi turno normal**, con los dos instrumentos sacados otra vez de los originales y no de las copias del extractor. Lo que
si esta en mi mano lo cumplo en mi pagina: cada bloque `$` lleva la salida del comando que abre, y nada mas.

    $ ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl
    ls: cannot access 'docs/loop/REPORTE.md': No such file or directory
    ls: cannot access 'docs/loop/ultimo_extractor.json': No such file or directory
    ls: cannot access 'docs/loop/ultimo_auditor.json': No such file or directory
    ls: cannot access 'docs/loop/CREDITO_serial.jsonl': No such file or directory
    $ grep -n "VUELTA 4 : APERTURA CIEGA" docs/loop/loop.log | tail -1
    8045:[2026-09-26 06:03:52] VUELTA 4 : APERTURA CIEGA (claude-opus-5-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl

HEREDADO 3: CUMPLIDO. **`R6`, mio** (`ACTA 73` `73.11`): en esta fase los pasos de cualquier nodo los imprime
`.v67aud/normal/pasos_ciego.py`, que no ensenia `previos` ni `siguientes`, y **el unico bloque de pasos de esta pagina lo corre**
(seccion `6`). Los instrumentos mios de esta fase que **nombran** esas claves en su codigo:

    $ grep -l -E "previos|siguientes" .v75aud/*.py
    .v75aud/esperado_75.py

**Y LO DIGO PARA QUE SE JUZGUE:** `esperado_75.py` (seccion `5`) **las nombra para leer las aristas de la tanda en el grafo**, y
**no imprime ninguna clave ni ningun id de relacion**: imprime dos cuentas y dos `SI` o `NO` (cuantas aristas tiene escritas la
madre, cuantas el hijo, si las dos listas dicen lo mismo y si el conjunto es el que mi lectura sellada esperaba, que el mismo
instrumento imprime **antes** de mirar el grafo). `grafo_sin_tanda.py` (seccion `2`) quita los ids de la tanda de **cualquier** lista
sin nombrar ninguna clave, y solo cuenta. **No vi ninguna clave de relacion con su valor de ningun nodo en esta fase.** El
cumplimiento de la pagina entera lo mide un `grep` sobre ella al cerrarla (seccion `9`).

HEREDADO 4: CUMPLIDO. **`R7`, mio** (`ACTA 73` `73.11`): toda linea de esta pagina que reparte un total en clases la imprime un
instrumento que cuenta **todas** las clases con el mismo predicado y **dice su `suma`**: los de `.v75aud/` la traen desde que nacen,
y los que reuso (`.v70aud/poblacion.py`, `.v73aud/restricciones_orden.py` y el de `R8` de la `ACTA 73`) ya la traian. **Medido sobre
la pagina misma** en la seccion `9`, con la copia de `.v74aud/r7_pagina.py`.

HEREDADO 5: CUMPLIDO. **`R8`, mio** (`ACTA 73` `73.11`): se comprueba **aqui**, en mi fase ciega, sobre el encargo de la `75`, **con
el mismo instrumento con el que lo medi al cerrarlo** (`.v74aud/normal/r8_encargo75.py`), sin copiarlo, y leyendo sus lineas otra
vez. Su salida de hoy es identica a la que la `ACTA 73` `73.12` guardo, y la lectura, con las cuentas en letra buscadas aparte, esta en
la seccion `7`. El encargo de la `76` lo escribo en mi turno normal y se mide alli.

HEREDADO 6: NO APLICA en esta fase. **Motivo:** `R9` es un remedio **del extractor**, nuevo en mi `ACTA 73` `73.11`, y se comprueba
en *el reporte de la `75` y siguientes que marquen fidelidad; en la `75`, sobre la correccion de `dar_elogio`*. **Ese reporte no esta
en el arbol** (el bloque de `ls` del `HEREDADO 2`, que es el mismo fichero), y no lo he recuperado. **Se mide en mi turno normal.**
**Lo que si hago aqui es aplicar su letra a mi propia lectura**: el `grep` de clausulas que comparan o califican la prueba, sobre los
`68` pasos de `cap_13` de Scott que quedan y sobre los `42` de Grove que entraron, **cada coincidencia con su tramo literal del libro**
(secciones `3` y `4`). La salida que sostiene que el reporte no esta:

    $ ls docs/loop/REPORTE.md
    ls: cannot access 'docs/loop/REPORTE.md': No such file or directory

## 1. **LO QUE VI SIN BUSCARLO, Y LO DIGO ANTES DE MEDIR** (`d146`)

**La foto de `git status` que el entorno me pone delante trae los asuntos de los cinco ultimos commits del extractor de la `75`, y
dos traen cifras y conclusiones de su vuelta**, que lei antes de medir nada:

- `d02ed219` *Vuelta 75, T5: el cierre (censo 430/1081/1/7/85 al abrir y 437/1111/1/0/92 al cerrar; las 7 de Grove dentro con 0
  PUENTE que entraron; cap_13 de Scott sin puente vivo en el grafo; D.61 sin abiertos; R5, guardas y cierre estricto en verde)*;
- `4f3f21a3` *Vuelta 75, T4: las 7 de Grove insertadas, las 3 aristas esperadas en el grafo, ningun nodo viejo cambiado fuera de la
  TAREA 2*;
- y `7a8cd241`, `3651efd4` y `11a630db`, sin cifras de medida (*la salida del hook*, *fila 7: su fila en el reporte*, y la fila `7`
  insertada por la aduana y movida a `_insertados`).

**Y CUATRO COSAS MAS, DEL MISMO TIPO, QUE SON MIAS:**

1. un `ls .v75ext` me ensenio **los nombres** de los ficheros de su carpeta (entre ellos `t2_op1_corregir.txt`, `t2_op2_retirar17.txt`,
   `t2_op3_retirar8.txt`, `t2_ver.txt`, `r9.txt`, `r9_tramos.txt`, `cap13_scott.txt`, `aristas_vuelta.txt`, `nodos_viejos.txt`, un
   `contra_0N.txt`, un `insertar_0N_<id>.txt` y su `.fin` por fila, del `01` al `07`), **no su contenido**;
2. la cola de `docs/loop/loop.log`, que no se retira, con el coste y el reloj del turno del extractor:

    $ grep -n "VUELTA 4 : EXTRACTOR\|extractor listo" docs/loop/loop.log | tail -2
    8043:[2026-09-26 04:30:59] VUELTA 4 : EXTRACTOR (claude-opus-5-5, esfuerzo high)
    8044:[2026-09-26 06:03:52] extractor listo (USD 5.9120888), 5572s, intento 1 de 7

3. **el `resumen_teorico` entero de `dar_elogio` en el grafo**, que lei para escribir el instrumento que lo mide: trae el texto de la
   correccion y de las dos retiradas **que el extractor escribio en esta vuelta**. Es dato del grafo y no reporte, y es justo lo que la
   bloqueante le mandaba escribir; **pero es prosa suya**, y lo digo;
4. el codigo de `src/correccion.py` y de `scripts/retirar_paso.py`, para saber **que escribe cada operacion** y poder deshacerla en mi
   reconstruccion (seccion `2`). Tambien lei mi `ACTA 73` entera, mi encargo y `AUDITOR_FORJA.md` entero.

**LO QUE HAGO CON ELLO:** ninguna cifra de esta pagina sale de esos asuntos; todas salen de un instrumento corrido en esta fase, y
**donde coinciden lo digo como coincidencia y no como fuente**. **No he abierto nada de `.v75ext/` por dentro**, **ni
`bitacora/VEREDICTOS.jsonl` por dentro**: de la bitacora solo cuento lineas. **Mis clases de la tanda no las decido hoy**: son las de
mis ficheros sellados de la `73`, con la unica correccion que la `ACTA 72` `72.5` adjudico (`D73.9`), declarada dentro de cada
instrumento que la aplica.

## 2. **EL CENSO, Y QUE LO UNICO QUE SE MOVIO ES LO QUE EL ENCARGO MANDABA** (`D.38.4`, `D.38.5`)

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        437 dataset/nodos.jsonl
       1111 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1549 total
    $ for d in cuarentena/grove_high_output cuarentena/_insertados/grove_high_output cuarentena/gerber_emyth cuarentena/marquet_turn_the_ship; do echo "$d $(find $d -maxdepth 1 -name '*.json' | wc -l)"; done; echo "procesos $(ls -A procesos/ | wc -l)"
    cuarentena/grove_high_output 0
    cuarentena/_insertados/grove_high_output 92
    cuarentena/gerber_emyth 22
    cuarentena/marquet_turn_the_ship 20
    procesos 0
    $ python .v70aud/poblacion.py
    poblacion: 479 | por sede: {'grafo': 437, 'bandeja': 42} | suma: 479
    $ python forja.py gate | head -2
    GATE VERDE.
      nodos verificados: 437

**Sin `git`, lo que cambio desde que escribi mi encargo, por tres instrumentos.** Primero, **cualquier fichero** del dato, de las
bandejas, del codigo o de la configuracion con fecha de escritura posterior a mi encargo (las fichas de una misma carpeta, juntas):

    $ ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, $7, $9}'
    2026-09-26 04:27:25.592730100 docs/loop/PROMPT_SIGUIENTE.md
    $ find cuarentena dataset bitacora censos config fuentes esquema src scripts tests forja.py -type f -newer docs/loop/PROMPT_SIGUIENTE.md | sed 's|/[^/]*\.json$|/*.json|' | sort | uniq -c
          1 bitacora/VEREDICTOS.jsonl
          1 censos/denominaciones.md
          1 dataset/nodos.jsonl

Segundo, **las `50` huellas que tome al lanzar mi barrido de la `73`** (las fichas de las tres bandejas y el grafo) contra los ficheros
de hoy, buscando en `_insertados` la ficha que ya no esta en la bandeja:

    $ python .v75aud/huellas_hoy.py
    huellas: 50 | suma: 50
      gerber_emyth, en su sitio, misma huella: 22
      grafo, aparte: 1
      grove_high_output, movida a _insertados, misma huella: 7
      marquet_turn_the_ship, en su sitio, misma huella: 20
    movidas a _insertados: 7 | son las 7 de .v73aud/los7.txt: SI | fuera de ellas: []
    ficheros que no cuadran: []

Tercero, **el grafo**: si al de hoy le quito las `7` filas de la tanda, y ademas los ids de las `7` de las listas de los nodos viejos,
y ademas **deshago en `dar_elogio` las tres operaciones de la TAREA `2`** por lo que su codigo escribe (`src/correccion.py` solo
agrega al final del resumen; `scripts/retirar_paso.py` saca el paso y agrega al final del resumen su literal), sale el fichero que
barri, byte a byte. **La vuelta `74` no movio ningun dato** (mi `ACTA 73` `73.1`, con `git diff`), asi que ese fichero es tambien el
de la apertura de la `75`:

    $ python .v75aud/grafo_sin_tanda.py
    filas del grafo hoy: 437 | la reconstruccion reproduce el fichero de hoy: SI
    de las 7 de la tanda en el grafo: 7 | filas que quedan sin ellas: 430
    las 7 son las ultimas filas del fichero: SI
    (a) sin las 7 filas, sha1 igual a la huella de mi barrido de la 73: NO
    (b) nodos viejos con algun id de las 7 en alguna lista: 0 | sin esos ids, sha1 igual a la huella: NO
    (c) en dar_elogio: pasos hoy 18 | retiradas escritas en su resumen despues de la primera correccion del 26 sep: 2, en este orden: paso 17 (de 20 a 19), paso 8 (de 19 a 18)
        deshechas: pasos 20 | caracteres del resumen quitados del final: 4008 de 9390
        y con dar_elogio deshecho, sha1 igual a la huella de mi barrido de la 73: SI

**LECTURA:**

- **El grafo tiene `437` filas, la bandeja de Grove `0`, sus insertados `92`, los pares mutuos `1`, la bitacora `1111` lineas, y
  `procesos/` esta vacio.** Gerber y Marquet siguen en `22` y `20`, **con la huella de mi barrido de la `73`**, que es lo que el
  encargo pedia (*no tocas*). Coincide con el `437/1111/1/0/92` del asunto de `d02ed219`, y lo digo como coincidencia.
- **Las `7` fichas movidas a `_insertados` son las `7` de mi lista, con la huella que tenian cuando las barri**, y son las ultimas `7`
  filas del grafo.
- **(a) y (b) salen `NO`, y tienen que salir `NO`**: `dar_elogio` cambio por mandato. **(c) sale `SI`**: con las tres operaciones
  deshechas, **los `430` nodos viejos son byte a byte los que barri**, y eso dice cuatro cosas a la vez: **ningun nodo viejo tiene un
  id de la tanda en ninguna lista** (las `3` aristas son entre nodos de la tanda, seccion `5`); **ningun otro nodo del grafo cambio**;
  **en `dar_elogio` no cambio nada mas** que los dos pasos y el final del resumen (ni el titulo, ni la condicion, ni el entregable, ni
  un caracter del resumen viejo); y **las dos retiradas se aplicaron sobre el `17` y despues sobre el `8`**, porque reponiendolas al
  reves sale la huella. Coincide con el *ningun nodo viejo cambiado fuera de la TAREA 2* de `4f3f21a3`, y lo digo como coincidencia.
- **La poblacion de hoy es `479`**, la de mi barrido de la `73`, con `7` en otra sede.
- **Lo que se escribio despues de mi encargo en el dato** es el grafo, la bitacora y `censos/denominaciones.md`, que es lo que escriben
  una insercion y una correccion; **nada en `config/`, `esquema/`, `fuentes/`, `src/`, `scripts/` ni `tests/`**. Las fichas movidas no
  salen en el `find` porque mover no cambia la fecha de escritura; las mide el segundo instrumento.

## 3. **LA TAREA `2`: LOS DOS PUENTES DE `dar_elogio` FUERA DEL CAMPO** (`HEREDADO 1`; `D.30`, `D.54`; `ACTA 73` `73.5`, `73.6`)

El instrumento lee los `20` pasos viejos de mi fase ciega de la `74` (`.v74aud/pasos_tres.txt`, impresos con `pasos_ciego.py`) y los
de hoy del grafo, y busca **literal** en la correccion cada cosa que mi encargo le pidio:

    $ python .v75aud/dar_elogio.py
    pasos viejos (.v74aud/pasos_tres.txt): 20 | pasos hoy en el grafo: 18
    (1) los de hoy son los viejos sin el 8 y sin el 17, en su orden y texto a texto: SI
    (2) literal retirado del paso 17 igual al 17 viejo: SI | del paso 8 igual al 8 viejo: SI
    (3) posicion en el resumen: corregir 5383, retirar 17 7762, retirar 8 8628 | en el orden corregir, 17, 8: SI
    (4) lo que el encargo pedia a la correccion, frase por frase: {'esta': 11} | suma: 11
    (5) tramos del libro pegados en la correccion: 3, lineas [273, 283, 283] | por estado: {'en su linea': 3} | suma: 3
        las dos razones de retirar_paso.py traen la fecha de hoy y la ACTA 73 73.5: ['SI', 'SI']

**LECTURA:** **la bloqueante esta cumplida por el dato.** Los `18` pasos son los viejos sin el `8` y sin el `17`; los dos literales
estan escritos en el nodo y son los que eran; **la correccion va antes de las dos retiradas y la del `17` antes que la del `8`**, que es
el orden que pedi para que el numero del segundo no se moviera; y la correccion trae, **literal**, que los dos son `PUENTE` de clausula,
la `73.5`, las dos lineas del libro, que parte de cada paso es del libro, la cuenta `18` y `2` en lugar de `20` y `0`, y la tabla de
numeros vieja contra nueva. **Los tres tramos del libro que pega estan en su linea del capitulo.** Las dos razones de
`retirar_paso.py` traen la fecha de hoy y la `73.5`, **ademas** de la fecha fija de `D.54` que el instrumento escribe (`17 sep 2026`),
que es lo que el encargo avisaba.

**`PASOS INVENTADOS` de `cap_13` DESPUES DE LA TAREA `2`**, desde **mi** lectura sellada de la `74` (`.v74aud/fidelidad.tsv`) con las
cinco adjudicaciones de la `ACTA 73` `73.5` aplicadas y declaradas en el instrumento, quitadas las filas de los dos pasos que salieron y
cruzada cada fila que queda con su paso de hoy, texto a texto. Y **`R9` con su letra aplicada a mi propia lectura**: el `grep` de
clausulas que comparan, contrastan o califican la prueba, sobre los pasos de hoy:

    $ python .v75aud/cap13_despues.py
    adjudicaciones de la ACTA 73 73.5 aplicadas: {'D a T (73.5)': 4, 'dar_elogio 17, T a P (73.5)': 1} | suma: 5
    contar_cuatro_historias_propias_ver_hueco_intencion  pasos hoy 17 | mis filas que quedan 17, cada una su paso de hoy texto a texto: SI | por marca: {'T': 17} | suma: 17 | PUENTE 0 de 17
    dar_elogio_disciplina_igual_critica                  pasos hoy 18 | mis filas que quedan 18, cada una su paso de hoy texto a texto: SI | por marca: {'T': 18} | suma: 18 | PUENTE 0 de 18
    medir_critica_respuesta_oyente_brujula               pasos hoy 33 | mis filas que quedan 33, cada una su paso de hoy texto a texto: SI | por marca: {'T': 33} | suma: 33 | PUENTE 0 de 33
    cap_13, los tres, despues de la TAREA 2: pasos 68 | por marca: {'T': 68, 'P': 0} | suma: 68 | PUENTE 0 de 68 = 0.00 por ciento
    R9, clausulas que comparan o califican la prueba en los pasos de hoy: 19 coincidencias
      contar_cuatro_historias_ paso 4 (viejo 4) L45: ...que haces a la vez al mostrar algo de vulnerabilidad contandola: una, demuestras consciencia de ti mismo y humildad; dos, ensenias...
      contar_cuatro_historias_ paso 8 (viejo 8) L49: ...o la del libro, y el texto da la razon: tu historia es por definicion mejor que la del correo grosero sobre los sitios desordenad...
      contar_cuatro_historias_ paso 13 (viejo 13) L53: ...ladora: cuando no le dijiste a una persona un problema directamente y en cambio se lo contaste a otros? O le dijiste que su traba...
      contar_cuatro_historias_ paso 15 (viejo 15) L55: ...Desempaqueta tus historias y compartelas con tu equipo, porque el texto dice que ahi es cu...
      dar_elogio_disciplina_ig paso 1 (viejo 1) L251: ...acelerador. Si quieres ir a algun sitio tienes que usar el acelerador mas que el freno, y si no usas nunca el freno te estrella...
      dar_elogio_disciplina_ig paso 1 (viejo 1) L251: ...eres ir a algun sitio tienes que usar el acelerador mas que el freno, y si no usas nunca el freno te estrellas y no llegas a ni...
      dar_elogio_disciplina_ig paso 2 (viejo 2) L267: ...ticando. Y la meta de la guia es ayudar a los demas a tener exito, no demostrar lo listo que eres tu....
      dar_elogio_disciplina_ig paso 4 (viejo 4) L269: ...gio sea concreto y sincero, y que inspire a los demas en vez de hacer comparaciones odiosas....
      dar_elogio_disciplina_ig paso 10 (viejo 11) L273: ...Y cuenta con lo que el elogio hace que lo vuelve practico y no solo agradable: revela lo que funciona y lo hace usabl...
      dar_elogio_disciplina_ig paso 10 (viejo 11) L273: ... puede llevar al exito y como se puede construir un exito sobre otro, demuestra que te importa personalmente, y desafia directame...
      dar_elogio_disciplina_ig paso 15 (viejo 16) L283: ...Practicalo asi: emparejate con un companiero y compartid un elogio concreto cada uno....
      medir_critica_respuesta_ paso 1 (viejo 1) L291: ...el texto trae aqui para ponerla en accion: la franqueza radical no se mide en tu boca, sino en el oido de la otra persona....
      medir_critica_respuesta_ paso 1 (viejo 1) L291: ...i para ponerla en accion: la franqueza radical no se mide en tu boca, sino en el oido de la otra persona....
      medir_critica_respuesta_ paso 6 (viejo 6) L297: ... con la regla que el texto pone por encima: la manera en que escuchas importa mas que la manera en que hablas....
      medir_critica_respuesta_ paso 7 (viejo 7) L297: ...Cuando ofrezcas franqueza compasiva, empieza suave y despues mide la respuesta del otro: escucha lo que dice, obser...
      medir_critica_respuesta_ paso 20 (viejo 20) L309: ...Si en cambio la persona sencillamente no te oye, porque esta a...
      medir_critica_respuesta_ paso 26 (viejo 26) L315: ...Y si aun asi no te oye, prueba a preguntar: solo para asegurarme de que estamos ...
      medir_critica_respuesta_ paso 28 (viejo 28) L315: ...O prueba con: puedo ser mucho mas directo contigo?...
      medir_critica_respuesta_ paso 33 (viejo 33) L321: ... primero, di algo como: antes de meternos muy a fondo en esto, quiero compartir contigo varios ejemplos mas para que veas el patr...

**Y el tramo literal del libro de cada coincidencia**, con un patron que escribo yo leyendo su linea (una fila por coincidencia, en el
orden del `grep`):

    $ python .v75aud/r9_tramos.py
      contar_cuatro 4, demuestras                L45: you are demonstrating self-awareness and humility
      contar_cuatro 8, mejor que                 L49: Your story is by definition better than the story Kim tells
      contar_cuatro 13, en cambio                L53: but you instead talked to others
      contar_cuatro 15, compartelas              L55: share them
      dar_elogio 1, mas que el freno             L251: use your accelerator more than your brake
      dar_elogio 1, y si no usas                 L251: If you never use your brake
      dar_elogio 2, no demostrar                 L267: not to prove how smart you are
      dar_elogio 4, en vez de comparaciones      L269: rather than making odious comparisons
      dar_elogio 10, y no solo agradable         L273: Giving praise doesn't just make people feel good, it's practical
      dar_elogio 10, demuestra que te importa    L273: Praise shows that you care personally
      dar_elogio 15, compartid                   L283: share one specific piece of praise
      medir_critica 1, no se mide                L291: measured not at your mouth
      medir_critica 1, sino en el oido           L291: but at the other person's ear
      medir_critica 6, importa mas que           L297: The way you listen is more important than the way you talk
      medir_critica 7, mide la respuesta         L297: gauge the other person's response
      medir_critica 20, si en cambio             L309: Other times, you'll work up the courage to give someone feedback, but then they just don't hear you
      medir_critica 26, prueba a preguntar       L315: Another thing that can help when you've told someone something and they just aren't hearing you is to ask
      medir_critica 28, prueba con               L315: Or you can try saying
      medir_critica 33, compartir                L321: share
    coincidencias del grep R9 con su tramo literal: {'tramo hallado': 19} | suma: 19

**LECTURA:**

- **`cap_13` de Scott queda en `0` PUENTE de `68`**: los tres nodos de `d084`, `17`, `18` y `33` pasos, **cada fila mia cruzada con su
  paso de hoy**. La guarda `D.30` que mi `ACTA 73` `73.6` puso en rojo **esta en verde por el dato**. Coincide con el *cap_13 de Scott
  sin puente vivo en el grafo* de `d02ed219`, y lo digo como coincidencia.
- **`R9` sobre mi lectura: `19` coincidencias, las `19` con su tramo literal.** **Las que son de forma y no de clausula, una por
  una**: `compartelas`, `compartid` y `compartir` son *share*, no *compare*; los dos `prueba` de `medir_critica` pasos `26` y `28` son
  *try*, no *proof* (`L315`, *is to ask* y *you can try saying*); y el *y si no usas* de `dar_elogio` paso `1` es una condicional
  (*If you never use your brake*), no un contraste. **Todas las demas son clausulas que el libro pone**, y la que mas se parece a las dos
  que salieron es `dar_elogio` paso `10` (el `11` viejo): *practico y no solo agradable* y *demuestra que te importa*, que `L273` dice
  con todas sus letras (*doesn't just make people feel good, it's practical* y *Praise shows that you care personally*). **No
  encuentro otro puente** en los `68`.
- **Lo que el `grep` no ve, y lo digo:** es un `grep` de forma. Una comparacion sin *que* (*pesa mas*) solo la ve porque le anadi ese
  patron al leer Grove (seccion `4`); una calificacion de la prueba con un verbo que no este en la lista (*confirma*, *se sabe*) no la
  ve. **No es una relectura**: la relectura de estos `68` es la de mi fase ciega de la `74`, firmada en la `ACTA 73`, y no la rehago
  (`D.47`).

## 4. **LAS `7`: LO QUE ENTRO ES LO QUE SE LEYO** (`D.58`), **Y SUS PASOS INVENTADOS** (`8`, `8.2`)

Cada nodo del grafo contra su ficha de `_insertados` (cuya huella es la leida, seccion `2`) en titulo, condiciones, pasos, entregable y
resumen; y sus pasos contra **mi** lectura entera sellada en la `73`, `.v73aud/fidelidad_fuente.txt`, una fila por paso:

    $ python .v75aud/entra_lo_leido.py
    las 7 por sede hoy: {'grafo y _insertados': 7} | suma: 7
    nodos del grafo contra su ficha, cinco campos: {'igual': 7} | suma: 7
    nodos con descuadre entre sus pasos en el grafo y mis filas selladas: 0 []
    cap_15 lo que ENTRO: candidatos 3 | pasos 22 | mis marcas: {'T': 21, 'P': 0, 'D': 1} | suma: 22 | PUENTE 0 de 22 = 0.00 por ciento | con la D adjudicada T (ACTA 72 72.5): T 22, P 0, suma 22
    cap_16 lo que ENTRO: candidatos 1 | pasos 4 | mis marcas: {'T': 4, 'P': 0, 'D': 0} | suma: 4 | PUENTE 0 de 4 = 0.00 por ciento | con la D adjudicada T (ACTA 72 72.5): T 4, P 0, suma 4
    cap_17 lo que ENTRO: candidatos 3 | pasos 16 | mis marcas: {'T': 16, 'P': 0, 'D': 0} | suma: 16 | PUENTE 0 de 16 = 0.00 por ciento | con la D adjudicada T (ACTA 72 72.5): T 16, P 0, suma 16
    los tres: candidatos 7 | pasos 42 | mis marcas: {'T': 41, 'P': 0, 'D': 1} | suma: 42 | PUENTE 0 de 42

**Y `R9` con su letra sobre los `42` pasos que entraron**, con el mismo patron (importado del instrumento de la seccion `3`, no
copiado) y el tramo literal de cada coincidencia:

    $ python .v75aud/r9_grove.py
      cap_15 gestionar_retencion_subord paso 6 L121: ... con la gente con la que trabaja a diario, y que el segundo pesa mas....
          el libro: commitments he has made to the people he has been working with daily are far stronger than one made to a casual new acquaintance
      cap_16 reciclar_empleado_ascendid paso 2 L49: ...Toma medidas deliberadas y directas para colocar a la persona ...
          el libro: take forthright and deliberate steps
      cap_15 responder_primer_aviso_ren paso 6 L111: ...No intentes cambiarle la idea en este momento, sino compra tiempo: cuando haya dicho todo lo que tien...
          el libro: Don't try to change his mind at this point, but buy time
    pasos leidos: 42 | coincidencias por capitulo: {'cap_15': 2, 'cap_16': 1} | suma: 3
    coincidencias con su tramo literal: {'tramo hallado': 3} | suma: 3

**LECTURA:**

- **Las `7` viven en el grafo con los textos que se leyeron**, cada una con tantos pasos como filas tiene mi lectura. **`PASOS
  INVENTADOS` de lo que ENTRO: `0` en los tres capitulos** (`cap_15` `0` de `22`, `cap_16` `0` de `4`, `cap_17` `0` de `16`), que son
  las cifras que la `ACTA 72` `72.4` firmo como *PUENTE que entrara*: los PUENTE de la preparacion (`72.4`) se corrigieron en la bandeja
  **antes** de mi barrido, y mi unica `D` la adjudico `T` la `72.5`, que no reabro (`D.47`). **Por debajo del `10`: no se baja
  escalon** (`8.1`), y de todos modos no queda lote de extraccion en el mundo `11`. Coincide con el *0 PUENTE que entraron* de
  `d02ed219`, y lo digo como coincidencia.
- **`R9` sobre Grove: `3` coincidencias, las `3` con su tramo.** `medidas` es *steps* (`cap_16` `L49`), de forma. *Sino compra tiempo*
  es *but buy time* (`cap_15` `L111`). **Y `gestionar_retencion` paso `6`, *el segundo pesa mas***, contra *commitments he has made to
  the people he has been working with daily are far stronger than one made to a casual new acquaintance* (`cap_15` `L121`): el paso
  junta en el segundo compromiso al jefe y a la gente de cada dia, y el libro compara solo el de la gente con el del conocido nuevo.
  **Es mi `D` sellada de la `73`, la que la `ACTA 72` `72.5` adjudico `T`** (*la misma comparacion leida de corrido, sin medio nuevo*),
  **y no la reabro** (`D.47`); la dejo escrita porque es exactamente la figura de `R9` y el que la lea en el turno normal debe saber que
  ya tiene adjudicacion.

## 5. **LO QUE MI LECTURA ESPERA QUE LA VUELTA DEJE, Y EL ORDEN EN QUE ENTRO**

Sacado **solo** de mis ficheros sellados de la `73`, con la correccion de la `ACTA 72` `72.5` aplicada y declarada dentro del
instrumento; la bitacora, solo contada; **y las aristas del grafo, solo en cuentas y `SI` o `NO`, despues de imprimir las esperadas**:

    $ python .v75aud/esperado_75.py
    pares sellados: 20 | con la correccion de la ACTA 72 72.5 aplicada: 1
    filas dirigidas de mi barrido con candidato de las 7: 29 | por vecino: {'vecino en la tanda': 19, 'vecino fuera de la tanda': 10} | suma: 29
    lineas de veredicto esperadas, por la clase de su par: {'CONTINUA': 6, 'SANO': 23} | suma: 29
    SOSTENGO de mi lectura: {'cae en una CONTINUA': 3, 'es el par corregido a SANO': 1} | suma: 4
    aristas esperadas: 3, todas CONTINUA con madre=
      desarrollar_primer_curso_entrenamiento > pedir_critica_anonima_curso_entrenamiento_dictado
      priorizar_lista_entrenamiento_subordinados > desarrollar_primer_curso_entrenamiento
      responder_primer_aviso_renuncia_subordinado > gestionar_retencion_subordinado_valioso_renuncia
    extremos de esas aristas que no son de las 7: 0
    bitacora esperada: 1081 + 29 + 1 = 1111 | hoy (lineas): 1111 | IGUAL
    aristas del grafo con algun extremo en las 7: escritas en la madre 3 | en el hijo 3 | las dos listas dicen lo mismo: SI | el conjunto es el esperado: SI

**LECTURA, y lo que se compara en el turno normal, no aqui:**

- **Lineas de bitacora.** Si cada `insertar` escribio una linea por fila dirigida que su aduana levanto, y la aduana levanto lo que mi
  barrido, son `29`: `6` `CONTINUA` y `23` `SANO` por la clase de su par; y `corregir` escribe **una** mas. **La bitacora tiene las
  `1111` que eso da.** **Es coincidencia de cuenta y no de contenido**: no he abierto ni una linea. `retirar_paso.py` no escribe en la
  bitacora (su codigo, seccion `1`), y la cuenta lo confirma. **Mi lectura no espera ningun vecino sin linea preparada**, porque la
  poblacion es la del barrido (seccion `2`); uno que apareciera seria un hallazgo, y lo busco par a par en el turno normal.
- **Aristas: `3`, las tres `CONTINUA` con `madre=` y las tres con los dos extremos dentro de las `7`.** Mis cuatro `SOSTENGO` sellados
  **no son aristas aparte**: tres son esas mismas `CONTINUA` y el cuarto es el par que `D73.9` dejo en `SANO`. **Y el grafo tiene
  exactamente esas `3`, escritas por los dos lados.** Coincide con el *las 3 aristas esperadas en el grafo* de `4f3f21a3`, y lo digo
  como coincidencia.

**El orden en que entraron, leido del grafo** (`src/aduana.py` escribe `nodos + [nuevo]`, asi que el orden de las filas es el de
entrada), contra el orden de pieza del libro y las `5` restricciones que imprime **mi** `.v73aud/restricciones_orden.py`, sellado en la
`73`:

    $ python .v75aud/orden_grafo.py
    orden de entrada leido del grafo: 7 filas
       1 usar_banco_nueve_preguntas_entrevista
       2 responder_primer_aviso_renuncia_subordinado
       3 gestionar_retencion_subordinado_valioso_renuncia
       4 reciclar_empleado_ascendido_mas_alla_capacidad
       5 priorizar_lista_entrenamiento_subordinados
       6 desarrollar_primer_curso_entrenamiento
       7 pedir_critica_anonima_curso_entrenamiento_dictado
    el orden de entrada es el orden de pieza del libro de mi instrumento sellado: SI
      cumple    6 desarrollar_primer_curso_entrenamiento               antes que 7 pedir_critica_anonima_curso_entrenamiento_dictado    obliga
      cumple    5 priorizar_lista_entrenamiento_subordinados           antes que 6 desarrollar_primer_curso_entrenamiento               obliga
      cumple    2 responder_primer_aviso_renuncia_subordinado          antes que 3 gestionar_retencion_subordinado_valioso_renuncia     obliga
      cumple    5 priorizar_lista_entrenamiento_subordinados           antes que 7 pedir_critica_anonima_curso_entrenamiento_dictado    caida a SANO en la ACTA 72 72.5
      cumple    3 gestionar_retencion_subordinado_valioso_renuncia     antes que 7 pedir_critica_anonima_curso_entrenamiento_dictado    D.36 de un solo lado
    restricciones: {'obliga, la cumple': 3, 'caida a SANO en la ACTA 72 72.5, la cumple': 1, 'D.36 de un solo lado, la cumple': 1} | suma: 5

**LECTURA:** **las `7` entraron en el orden de pieza del libro de mi instrumento sellado**, y **las `5` restricciones se cumplen**: las
`3` que obligan (cada madre antes que su hijo), la que salia de mi `CONTINUA` caido a `SANO` y ya no obliga, y la `D.36` de un solo
lado, informativa. **Que ese orden sea el de `.v73ext/orden.txt` fila a fila** lo dice el bloque de mi propio encargo (`TAREA 4`), que
lo pega de ese fichero; que cada `insertar` volviera antes de lanzar el siguiente **lo miro en mi turno normal**.

## 6. **MI CLASIFICACION DE CADA CANDIDATO, Y LAS TRES ARISTAS RELEIDAS** (`6.1`, y solo la vara `6.1`)

**Las `7`, una por una**, de mis ficheros sellados: las lineas del libro que sus pasos transcriben, las filas dirigidas de mi barrido en
las que es candidata, sus pares sin orden por clase con la correccion de `D73.9` (cuenta los pares en los que esta de cualquiera de los
dos lados, y por eso puede pasar de sus filas), y las aristas que mi lectura le espera como hija y cuantas como madre:

    $ python .v75aud/clasificacion_7.py
    1 cap_17 desarrollar_primer_curso_entrenamiento             NODO | L53 a L59 | filas 2 | pares {'CONTINUA': 2} suma 2 | hija: CONTINUA de priorizar_lista_entrenamiento_subordinados | madre de: 1
    2 cap_15 gestionar_retencion_subordinado_valioso_renuncia   NODO | L113 a L121 | filas 3 | pares {'CONTINUA': 1, 'SANO': 3} suma 4 | hija: CONTINUA de responder_primer_aviso_renuncia_subordinado | madre de: 0
    3 cap_17 pedir_critica_anonima_curso_entrenamiento_dictado  NODO | L61 a L61 | filas 7 | pares {'CONTINUA': 1, 'SANO': 6} suma 7 | hija: CONTINUA de desarrollar_primer_curso_entrenamiento | madre de: 0
    4 cap_17 priorizar_lista_entrenamiento_subordinados         NODO | L49 a L51 | filas 3 | pares {'CONTINUA': 1, 'SANO': 2} suma 3 | hija: ninguna | madre de: 1
    5 cap_16 reciclar_empleado_ascendido_mas_alla_capacidad     NODO | L49 a L49 | filas 1 | pares {'SANO': 1} suma 1 | hija: ninguna | madre de: 0
    6 cap_15 responder_primer_aviso_renuncia_subordinado        NODO | L111 a L111 | filas 7 | pares {'CONTINUA': 1, 'SANO': 6} suma 7 | hija: ninguna | madre de: 1
    7 cap_15 usar_banco_nueve_preguntas_entrevista              NODO | L39 a L55 | filas 6 | pares {'SANO': 6} suma 6 | hija: ninguna | madre de: 0

**LECTURA: LAS `7` SON NODO**, con la clase de cada par que selle en la `73` y la unica correccion adjudicada en la `ACTA 72`. **No
cambio ninguna**: lo que entro es byte a byte lo que lei (secciones `2` y `4`).

**Las tres aristas son las que el extractor cablea en el acto**, y **por eso las releo hoy con el libro y los pasos delante**. Las
lineas del libro que las sostienen, y la del par de `D73.9`:

    $ python .v75aud/lineas_fuente.py
    cap_15 L111 (968 caracteres): Drop what you are doing. Sit him down and ask him why he is quitting. Let him talk (raya) don’t argue about anything with him. Believe me, he’s rehearsed his speech countless times during more than one sleepless night. After he’s finished going through all his reasons for wanting to leave (they won’t be good ones), ask him more questions. Make him talk, because after the prepared points are delivered, the real issues may come out. Don’t argue, don’t lecture, and don’t panic. Remembe [...]
    cap_15 L113 (481 caracteres): What’s your next move? Because you have a major problem, you go to your supervisor for help and advice. He no doubt is also on his way to an important meeting…He, like you, will try to put things off, and most probably not because he doesn’t care, but because the situation affects you more than your supervisor (raya) after all, it is your subordinate who has decided to quit. It is up to you to make it your supervisor’s problem and make him participate in the solution to your problem [...]
    cap_17 L51 (187 caracteres): Having done this, take an inventory of the manager-teachers and instructional materials available to help deliver training on items on your list. Then assign priorities among these items.
    cap_17 L53 (493 caracteres): Especially if you haven’t done this sort of thing before, start very unambitiously (raya) like developing one short course (three to four lectures) on the most urgent subject. You will find that skills that you have had for years (raya) things that you could do in your sleep, as it were (raya) are much harder to explain than to practice. You may find that in your attempt to explain things, you’ll be tempted to go into more and more background until this begins to obscure the original objective of [...]
    cap_17 L57 (603 caracteres): Develop the second lecture after you have given the first. Regard the first time you teach the course as a throwaway (raya) it won’t be great, because no matter how hard you try, you’ll have to go through one version that won’t be. Rather than agonize over it, accept the inevitability of the first time being unsatisfactory and consider it the path to a more satisfactory second round. To make sure that your first attempt causes no damage, teach this course to the more knowledgeable o [...]
    cap_17 L61 (524 caracteres): After you’ve given the course, ask for anonymous critiques from the employees in your class. Prompt them with a form that asks for numerical ratings but that also poses some open-ended questions. Study and consider the responses, but understand that you will never be able to please all members of your class: typical feedback will be that the course was too detailed, too superficial, and just right, in about equal balance. Your ultimate aim should be to satisfy yourself that y [...]

Y el final de `L111`, que el corte de `480` deja fuera y la primera arista necesita:

    $ sed -n 111p fuentes/grove_high_output/cap_15.md | grep -o "Don.t try to change his mind[^.]*\. After he.s said all he has to say[^.]*\."
    Don’t try to change his mind at this point, but buy time. After he’s said all he has to say, ask for whatever time you feel is necessary to prepare yourself for the next round.

Y los pasos de sus cinco nodos, por `pasos_ciego.py` (`R6`), que hoy los encuentra en el grafo:

    $ python .v67aud/normal/pasos_ciego.py responder_primer_aviso_renuncia_subordinado gestionar_retencion_subordinado_valioso_renuncia priorizar_lista_entrenamiento_subordinados desarrollar_primer_curso_entrenamiento pedir_critica_anonima_curso_entrenamiento_dictado
    ===== responder_primer_aviso_renuncia_subordinado | grafo
      titulo: Responder al primer momento en que un subordinado valioso avisa que quiere renunciar: dejar lo que haces, escucharlo sin discutir y comprarte tiempo antes de actuar
      fuente: ['grove_high_output']
      cond: Cuando un subordinado valioso y estimado se acerca al mando y anuncia, de pasada, que ha decidido dejar la empresa.
      P1. Deja lo que estas haciendo en cuanto el subordinado te avisa de que quiere renunciar, en vez de posponer la conversacion para mas tarde.
      P2. Sientalo y preguntale por que se va.
      P3. Dejalo hablar sin discutir nada de lo que diga, aunque sus razones no te parezcan buenas.
      P4. Cuando haya terminado de exponer sus razones, hazle mas preguntas para que los asuntos de fondo puedan salir a la luz.
      P5. No discutas, no sermonees y no entres en panico durante esta primera conversacion.
      P6. No intentes cambiarle la idea en este momento, sino compra tiempo: cuando haya dicho todo lo que tiene que decir, pide el tiempo que necesites para prepararte para el siguiente encuentro.
      P7. Cumple despues con lo que te hayas comprometido a hacer en esta primera conversacion.
    ===== gestionar_retencion_subordinado_valioso_renuncia | grafo
      titulo: Gestionar la retencion de un subordinado valioso tras su primer aviso de renuncia: escalar al propio jefe, perseguir cada via para conservarlo y volver con una solucion a sus razones reales
      fuente: ['grove_high_output']
      cond: Cuando, tras la primera conversacion en la que un subordinado valioso anuncio que queria renunciar, el mando tiene que buscarle una salida que lo retenga en la empresa.
      P1. Lleva el problema a tu propio jefe en busca de ayuda y consejo y, aunque el tambien intente posponerlo, haz que sea problema suyo y que participe de la solucion.
      P2. Persigue con energia cada via disponible para retener al subordinado en la empresa, incluida la de transferirlo a otro departamento.
      P3. Si la transferencia parece la salida mas probable, asume tu mismo el papel de gestor de ese proyecto hasta que quede resuelto del todo.
      P4. Vuelve al subordinado con una solucion que atienda sus razones reales para querer irse y que ademas beneficie a la empresa.
      P5. Haz que se sienta comodo con el nuevo arreglo; puedes decirle algo como que no les arranco por chantaje nada que no debieran haber hecho igual, que al estar a punto de irse les hizo ver su error, y que solo hacen lo que debieron hacer sin que pasara nada de esto.
      P6. Si el subordinado dice que ya acepto un puesto en otra empresa, hazle ver que tiene dos compromisos distintos, uno con un futuro empleador que apenas conoce y otro contigo y con la gente con la que trabaja a diario, y que el segundo pesa mas.
    ===== priorizar_lista_entrenamiento_subordinados | grafo
      titulo: Priorizar la lista de en que hay que entrenar a los subordinados, tras preguntarles e inventariar los medios disponibles
      fuente: ['grove_high_output']
      cond: Cuando el mando decide abrazar el entrenamiento como tarea propia y necesita decidir por donde empezar, antes de desarrollar ningun curso.
      P1. Haz una lista de las cosas en que crees que tus subordinados o los miembros de tu departamento deberian entrenarse, sin limitar el alcance de la lista.
      P2. Incluye items que van desde lo que parece simple, como entrenar a la persona que atiende el telefono, hasta cosas mas generales y elevadas, como los objetivos y los sistemas de valores de tu departamento, tu planta y tu empresa.
      P3. Pregunta a la gente que trabaja para ti que siente que necesita: es probable que te sorprenda contandote necesidades que nunca supiste que existian.
      P4. Hecho esto, toma inventario de los mando maestros y los materiales instructivos disponibles para ayudar a impartir el entrenamiento de los items de tu lista.
      P5. Asigna prioridades entre esos items.
    ===== desarrollar_primer_curso_entrenamiento | grafo
      titulo: Desarrollar el primer curso de entrenamiento en siete pasos, desde el alcance sin ambicion hasta decidir si hacen falta mas instructores
      fuente: ['grove_high_output']
      cond: Cuando el mando ya priorizó en que entrenar a sus subordinados y elige el tema mas urgente para desarrollar su primer curso propio.
      P1. Empieza sin ambicion: desarrolla un curso corto, de tres a cuatro clases, sobre el tema mas urgente de tu lista.
      P2. Fija un calendario para el curso, con plazos, y comprometete con el para no atascarte en la preparacion.
      P3. Crea un esquema para el curso entero.
      P4. Desarrolla solo la primera clase, y dictala.
      P5. Desarrolla la segunda clase despues de haber dado la primera.
      P6. Trata la primera vez que enseñas el curso como un desechable: enseñaselo a los subordinados mas informados, que te ayudaran a perfeccionarlo con su interaccion y su critica.
      P7. Preguntate si podras cubrir tu solo a toda la organizacion o si, por su tamaño, hace falta que prepares a unos cuantos instructores con tu primer set de clases.
    ===== pedir_critica_anonima_curso_entrenamiento_dictado | grafo
      titulo: Pedir critica anonima tras dictar un curso de entrenamiento, con formulario numerico y preguntas abiertas
      fuente: ['grove_high_output']
      cond: Cuando el mando ya dicto su curso de entrenamiento y quiere saber si esta cumpliendo el proposito que se propuso.
      P1. Despues de dar el curso, pide criticas anonimas a los empleados de tu clase.
      P2. Usa un formulario que pida calificaciones numericas y que ademas plantee algunas preguntas abiertas.
      P3. Estudia y considera las respuestas, entendiendo que nunca podras complacer a todos los miembros de tu clase.
      P4. Ten como objetivo ultimo satisfacerte a ti mismo de que estas logrando lo que te propusiste.

**LECTURA, UNA POR UNA, Y LAS TRES LAS SOSTENGO:**

- **`responder_primer_aviso` madre de `gestionar_retencion`, `CONTINUA`: SOSTENGO.** La condicion del hijo (*tras la primera
  conversacion en la que un subordinado valioso anuncio que queria renunciar*) es el producto de la madre, y `L113` encadena con
  palabras la segunda ronda a la primera (*What's your next move?*), despues de que `L111` cierre la primera con *buy time* y *the
  next round*, que es el paso `6` de la madre. **El hijo anade** escalar al propio jefe, perseguir cada via, la transferencia, la
  solucion a las razones reales y los dos compromisos (pasos `1` a `6`), que la madre no trae. **No repite.** Mi duda sellada de
  hermanas la cerro la `ACTA 72` `72.5` (`D73.8`) y no la reabro.
- **`priorizar_lista` madre de `desarrollar_primer_curso`, `CONTINUA`: SOSTENGO.** El paso `1` del hijo arranca *sobre el tema mas
  urgente de tu lista*, que es el producto del paso `5` de la madre (*Asigna prioridades entre esos items*); `L53` sigue a `L51` en el
  libro (*assign priorities* y *the most urgent subject*). **Procedimiento en los dos lados fuera del solape, sin bascula** (`6.1`):
  la madre lista, pregunta e inventaria; el hijo calendariza, esquematiza y dicta.
- **`desarrollar_primer_curso` madre de `pedir_critica_anonima`, `CONTINUA`: SOSTENGO.** La condicion del hijo (*ya dicto su curso*) es
  el producto de los pasos `4` a `6` de la madre, y `L61` abre con *After you've given the course*. La critica del paso `6` de la madre
  (los subordinados mas informados, en la primera vuelta) y el formulario anonimo del hijo son **publico, instrumento y momento
  distintos**: el hijo procedimenta, no nombra.
- **Y `priorizar_lista` con `pedir_critica_anonima` sin arista**, abuela y nieta: ningun paso del hijo usa la lista ni las prioridades,
  y su condicion es el producto de `desarrollar`. Es `D73.9`, adjudicado en la `ACTA 72` `72.5`, **y con los pasos delante lo leo
  igual**.

## 7. **`R8` MEDIDO SOBRE MI ENCARGO DE LA `75`, CON EL MISMO INSTRUMENTO** (`ACTA 73` `73.11`, `73.12`)

`R8` dice: *toda cifra de medida que escriba en `PROMPT_SIGUIENTE.md` (un reloj, una banda, una cuenta que solo se comprueba abriendo un
fichero, en digito o en letra) va DENTRO de un bloque `$` con su salida, o lleva EN SU MISMA LINEA la seccion del acta donde esta
pegada*. Que el fichero es el encargo que escribi al cerrar la `ACTA 73`, y el instrumento de la `73.12` corrido sin copiarlo, con su
salida de hoy contra la que guardo aquella acta:

    $ head -1 docs/loop/PROMPT_SIGUIENTE.md | cut -c1-100; ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, $7, $9}'
    # ENCARGO DE LA VUELTA 75: **PRIMERO LOS DOS PUENTES DE `dar_elogio_disciplina_igual_critica` SALEN
    2026-09-26 04:27:25.592730100 docs/loop/PROMPT_SIGUIENTE.md
    $ python .v74aud/normal/r8_encargo75.py | diff - .v74aud/normal/r8_encargo75.txt && echo "IDENTICO a .v74aud/normal/r8_encargo75.txt, la salida de la ACTA 73 73.12"; python .v74aud/normal/r8_encargo75.py | tail -1
    IDENTICO a .v74aud/normal/r8_encargo75.txt, la salida de la ACTA 73 73.12
    lineas del encargo: {'linea de bloque sangrado': 22, 'prosa con numero, con seccion de la ACTA 73': 18, 'prosa con numero, sin seccion de la ACTA 73': 53, 'prosa sin digito ni palabra de numero': 60} | suma: 153

Las lineas de prosa con numero y **sin** seccion, cada una con los numeros que el instrumento le ve:

    $ python .v74aud/normal/r8_encargo75.py | grep -E "^  L[0-9]+ - " | sed -E 's/\] \|.*$/]/'
      L3 - ['11', '73', '74'] []
      L4 - ['1.4'] []
      L14 - ['0'] []
      L23 - ['18'] []
      L24 - ['8', '4'] []
      L31 - ['72', '72'] []
      L32 - ['73', '75', '72'] []
      L34 - ['76'] []
      L35 - ['72'] []
      L42 - ['1', '73'] []
      L44 - ['47'] []
      L57 - ['30', '54', '13'] []
      L60 - ['1'] []
      L61 - ['8', '17'] []
      L63 - ['8'] []
      L64 - ['17'] []
      L67 - ['1', '7'] []
      L68 - ['9', '16', '8', '15', '18', '20', '16', '18'] []
      L70 - ['2', '17', '8'] []
      L72 - ['54'] []
      L73 - ['3'] ['tres']
      L76 - ['4'] []
      L77 - ['7', '55'] []
      L80 - ['74'] []
      L82 - ['3'] []
      L84 - ['73', '73'] []
      L88 - ['4', '73'] []
      L105 - ['1', '1'] []
      L106 - ['73'] []
      L107 - ['3', '6', '7'] []
      L108 - ['73.9', '72', '72.5'] []
      L109 - ['2', '031'] []
      L110 - ['73', '72', '73'] []
      L111 - ['6.1'] ['dos']
      L113 - ['3', '72'] []
      L114 - ['73', '31'] []
      L115 - ['4'] []
      L117 - ['2'] []
      L119 - ['5'] []
      L122 - ['2'] []
      L123 - ['4', '2'] []
      L124 - ['15', '16', '17'] []
      L125 - ['73', '72', '72.4'] ['cero']
      L127 - ['61'] []
      L128 - ['5', '64', '64', '64'] []
      L129 - ['75', '9'] []
      L130 - ['4', '59', '59.18'] []
      L134 - ['75'] []
      L141 - ['2'] []
      L142 - ['8', '17'] []
      L143 - ['4.2'] []
      L146 - ['7', '55'] []
      L152 - [] ['Cero', 'cero']

**LECTURA, grupo a grupo, que es mia y no del instrumento; las volvi a leer una a una y no copio la de la `73.12`:**

- **Numeros de vuelta, de acta, de rama, de mundo o de carpeta de la casa**: `L3`, `L31`, `L32`, `L34`, `L35`, `L80`, `L84`, `L106`,
  `L110`, `L114`, `L134`, el `72` de `L113` y el `75` de `L129`; y las actas y carpetas de `L42`, `L88`, `L108`, `L125` y `L130`, que
  ademas llevan en su misma linea la seccion de la `ACTA 72` o de la `ACTA 59` que citan (`72.5`, `72.4`, `59.18`).
- **Secciones, reglas, deudas, remedios y numeros de tarea, de punto o de lista**: `L4`, `L14`, `L24` (`PARALELO.md` `8` punto `4`),
  `L44`, `L60`, `L72`, `L73`, `L76`, `L77`, `L82`, `L109`, `L111`, `L113`, `L115`, `L117`, `L119`, `L122`, `L123`, `L127`, `L128`,
  `L141`, `L143`, `L146`, el `R9` de `L129` y el `R4` de `L130`, y los numeros de tarea de `L42` y `L88`.
- **Identificadores de capitulo, de fila o de paso**: `cap_18` en `L23`; `cap_15` a `cap_17` en `L124`; el `P13` del precedente en
  `L57`; las filas `1`, `3`, `6` y `7` de `L105` y `L107`; los pasos `8` y `17` en `L61`, `L63`, `L64`, `L70` y `L142`; y **la tabla de
  numeros de paso de `L67` y `L68`**, aritmetica de esos dos identificadores sobre los `20` pasos que la misma TAREA cita con su
  seccion.
- **Las cifras de medida** van dentro de un bloque `$` (la clase, el tablero, el reloj de la `72`, las filas y las aristas de la tanda,
  las lineas preparadas) o llevan su seccion de la `ACTA 73` en la misma linea (las lineas con seccion del instrumento).

**LAS CUENTAS EN LETRA**, que el instrumento ve por palabra y que busco tambien con un `grep` mas ancho:

    $ grep -n -i -w -E "uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|veinte|treinta|cero|mil|cien|ambas|ambos" docs/loop/PROMPT_SIGUIENTE.md | cut -c1-120
    1:# ENCARGO DE LA VUELTA 75: **PRIMERO LOS DOS PUENTES DE `dar_elogio_disciplina_igual_critica` SALEN DEL GRAFO POR `D.5
    48:| **Tu vuelta, reproducida**: no movio dato; tus instrumentos dan lo que pegaste y tus cuatro `como` estan en el regi
    49:| **Tus ocho discutibles se sostienen**, `D74.1` a `D74.8`; en `D74.6` gana tu `P` y cae la lectura ciega del auditor
    54:## TAREA 2: **BLOQUEANTE (`D.55`), CON LA GUARDA `D.30` EN ROJO: LOS DOS PUENTES DE `dar_elogio_disciplina_igual_crit
    56:**Antes de ningun `insertar`.** La guarda, los dos pasos y sus lineas estan en la `ACTA 73` `73.5` y `73.6`. **La via
    73:3. **Despues de cada una de las tres operaciones, `python forja.py gate`, pegado.** Al terminar, **pegados**: los pas
    101:      CONTINUA con madre= (aristas distintas): 3 | SOSTENGO por lectura: 0 | solapes entre las dos: 0 | aristas espe
    109:2. **La puerta es la aduana de `insertar`, no la lista** (`d031`). **Al volver cada uno, su vecindad de hoy contra l
    111:   sin linea, lo lees con los pasos de los dos delante, escribes su veredicto por la vara `6.1` y solo esa, **y lo m
    125:  `.v73ext/fidelidad.tsv` con los PUENTE ya corregidos en la bandeja, que la `ACTA 72` `72.4` firmo en cero que entr
    126:  `cap_13` de Scott** despues de la TAREA 2, con los dos pasos fuera (`73.4`, `73.5`). No a ojo.
    131:  parada**, y las dos ultimas caidas vivieron en celdas de tabla (`73.7`).
    152:**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo t

**LECTURA, linea a linea:** `L101` esta **dentro de un bloque `$`**; `L1` (*los dos puentes*) lleva `73.5` y `73.1` en su misma
linea; `L109` (*al volver cada uno*) es **una manera**, no una cuenta;
`L48` (*tus cuatro `como`*) y `L49` (*tus ocho discutibles*) son filas de tabla con su seccion (`73.1` y `73.5`) en la misma linea;
`L54` (*los dos puentes*, titulo de la TAREA `2`) lleva `73.6`; `L56` (*los dos pasos*) lleva `73.5` y `73.6`; `L126` (*los dos pasos
fuera*) lleva `73.4` y `73.5`; `L131` (*las dos ultimas caidas*) lleva `73.7`; `L125` (*en cero que entran*) lleva `72.4`; `L73` (*las
tres operaciones*) son las que la misma TAREA enumera; `L111` (*los dos*) son los dos nodos de un par; y `L152` (*cero guiones*) es
**la meta de la frase fija de cierre**. **Ninguna linea de prosa trae una cifra de medida sin su bloque o su seccion en la misma
linea: `R8` CUMPLIDO en el encargo de la `75`.**

## 8. **LO QUE DEJO PARA MI TURNO NORMAL, ESCRITO ANTES DE VER EL REPORTE**

1. **`R5`** en su reporte, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` sacados otra vez de los originales y con la
   cabecera cambiada a la `75`; y **`R9`** en su reporte: su `grep` de clausulas sobre la correccion de `dar_elogio` y sobre lo que
   marque `T`, **contra el mio de las secciones `3` y `4`**, coincidencia a coincidencia.
2. **La TAREA `2` con su reporte y con `git`**: el `gate` verde **despues de cada una** de las tres operaciones, la `--razon` de
   `corregir` en su linea de la bitacora, y que ningun `insertar` se lanzo antes de cerrarla.
3. **Las lineas nuevas de la bitacora, una a una** (seccion `5`): las de veredicto contra las vivas de `.v73ext/veredictos_listos.txt` y contra mis
   clases selladas con `D73.9`, y **par a par contra las filas de mi barrido**; y la de `corregir`, contra su correccion.
4. **Que cada `insertar` volvio con su `.fin` en `0`, en el orden de `.v73ext/orden.txt`, uno por vez y sin solaparse**, y que **ninguna
   aduana levanto un vecino fuera de mi barrido**.
5. **La muestra pineada de los `SANO`** que la `75` escribio en la bitacora, **con semilla `75`**, el tamanio de la seccion `7` de
   `AUDITOR_FORJA.md` y su banda, releida contra mis clases selladas.
6. **Las aristas par a par y por los dos lados, con sus ids**, contra las `3` de la seccion `5`, que aqui solo medi en cuentas (`R6`).
7. **El censo con `git diff`, las guardas y el cierre estricto**, que tallara esta pagina: no tiene tablas, asi que un rojo en el suyo
   sera suyo. Y el coste de su turno (seccion `1`) contra su clase (`D.55`).
8. **`R8`** sobre el encargo de la `76`, medido antes de cerrarlo, con las cuentas en letra incluidas.

## 9. **ESTA PAGINA CONTRA `R6`, `R7` Y LOS GUIONES, MEDIDA SOBRE ELLA MISMA**

El generador corre dos veces, y estos bloques de la segunda pasada leen la pagina que escribio la primera, identica salvo estos
bloques. El primero cuenta las lineas de bloque `$` que empiezan por una clave de relacion; el segundo, con la copia de
`.v74aud/r7_pagina.py`, cuenta las lineas de bloque que reparten una cifra en clases y cuantas traen su `suma`; el tercero cuenta
guiones largos y medios:

    $ grep -c -E "^    +(previos|siguientes|nodos_previos|nodos_siguientes)" docs/loop/APERTURA_CIEGA.md
    0
    $ python .v75aud/r7_pagina.py
    lineas de bloque que reparten en clases: 30 | por estado: {'con suma': 30} | suma: 30
    $ grep -c -P "\x{2014}|\x{2013}" docs/loop/APERTURA_CIEGA.md
    0
