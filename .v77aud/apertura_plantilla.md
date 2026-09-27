# APERTURA CIEGA DE LA VUELTA 77, lote 9 (`gerber_emyth`), **CLASE INSERCION**

*Auditor `claude-opus-5-5`, fase ciega, 26 sep 2026. En la corrida que arranco el 26 a las `09:27`, el arnes la numera `VUELTA 1`.
Linea **serial**, rama `extraccion-mundo-11`. Modo austero (`D.47`). Todo lo de esta pagina sale de `.v77aud/`, escrito y
corrido en esta fase; cada bloque `$` lo pega `.v77aud/generar_apertura.py` corriendo el comando en el momento de escribirla.
**No hay ninguna tabla en esta pagina**, a proposito, como en la `73`, la `75` y la `76`.*

**LO QUE ESTA VUELTA TENIA QUE HACER, Y LO QUE CLASIFICO A CIEGAS** (mi encargo, `docs/loop/PROMPT_SIGUIENTE.md`): primero **la
relectura conjunta** de las dos piezas que la `ACTA 75` `75.4` dejo abiertas (el par de la contratacion y la arista de `fingir` a
`recorrer`); despues, **las `22` fichas de Gerber dentro, una por vez, en el orden**, con las lineas y las aristas que la `76` dejo
listas. Los candidatos ya no estan en la bandeja: **los leo donde estan hoy**, en el grafo y en `_insertados`, contra mi lectura
sellada de la `76` (con las adjudicaciones de la `ACTA 75`) y contra el libro, y **releo las dos piezas de la conjunta con los pasos
y las lineas delante** (seccion `5`).

**UNA LIMITACION DE METODO, DICHA ANTES DE NADA: EN ESTA FASE NO HE CORRIDO `git` SOBRE EL REPOSITORIO**, ni una vez, como en la
`73`, la `75` y la `76`: la carpeta de una linea viva es solo del arnes (`PARALELO.md` `7`). **Lo que se mide con `git` aqui no lo
mido**: que commit movio que y a que hora, y si cada `insertar` volvio antes de lanzarse el siguiente. Lo que si mido sin `git` es
el dato contra mis propias huellas de la `76` (seccion `2`). El commit en que esta el arbol lo leo de los ficheros de `.git/`:

@@RUN:0::cat .git/HEAD; cat .git/refs/heads/extraccion-mundo-11@@

**NO HAY HUECO DE ACTA** (`1.0`): la ultima acta escrita es la `75`, que cubre la vuelta `76`, y la vuelta que viene a auditarse es
la `77`, la de mi encargo; el arnes arranco esta corrida en modo de insercion:

@@RUN:0::grep -n "^# ACTA 7[3-9]\. VUELTA" docs/loop/ACTA_AUDITOR.md | cut -c1-60@@
@@RUN:0::grep -n "arranque: rama\|VUELTA 1 : EXTRACTOR\|extractor listo\|VUELTA 1 : APERTURA CIEGA" docs/loop/loop.log | tail -4@@

## 0. **LA HERENCIA** (`D.40`)

ACTA ANTERIOR LEIDA: 277d08beb156cc3b336c626140a9b15b46e9b1a9

**Comprobada sin git**: es el blob de `docs/loop/ACTA_AUDITOR.md` tal como esta hoy en el arbol, calculado como lo calcula git. **La
`ACTA 75` la lei entera**, de su linea de cabecera a la ultima del fichero, y con ella el encargo que me deje:

@@RUN:0::python .v77aud/huella_acta.py@@

HEREDADO 1: NO APLICA en esta fase. **Motivo:** `R5` es un remedio **del extractor** y se mide **sobre su reporte de la `77`**
(`ACTA 75` `75.11`: *el reporte de la `77`, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera cambiada a
la `77`*), y el reporte **no esta en el arbol**: el arnes lo retiro para esta fase (`D.34.2`) y no lo he recuperado por ninguna via.
**Se mide en mi turno normal**, con los dos instrumentos sacados otra vez de los originales y no de las copias del extractor. Lo que
si esta en mi mano lo cumplo en mi pagina: cada bloque `$` lleva la salida del comando que abre, y nada mas.

@@RUN:0::ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl@@

HEREDADO 2: CUMPLIDO. **`R6`, mio** (`ACTA 75` `75.11`): en esta fase los pasos de cualquier nodo los imprime
`.v67aud/normal/pasos_ciego.py`, que no ensenia `previos` ni `siguientes`, y **el unico bloque de pasos de esta pagina lo corre**
(seccion `5`). Los instrumentos mios de esta fase que **nombran** esas claves en su codigo:

@@RUN:0::grep -l -E "previos|siguientes" .v77aud/*.py@@

**Y LO DIGO PARA QUE SE JUZGUE:** `esperado_77.py` (seccion `4`) **las nombra para leer las aristas de la tanda en el grafo**, y
**no imprime ninguna clave ni ningun id de relacion leido del grafo**: imprime cuentas y `SI` o `NO` (cuantas aristas tiene escritas
la madre, cuantas el hijo, si las dos listas dicen lo mismo, si el conjunto es el que mi lectura esperaba, y cuantas de las esperadas
estan y cuantas sobran), **despues** de imprimir las esperadas, que salen de mis ficheros y no del grafo. `grafo_sin_tanda.py` (seccion
`2`) quita los ids de la tanda de **cualquier** lista sin nombrar ninguna clave, y solo cuenta. **No vi ninguna clave de relacion con
su valor de ningun nodo en esta fase.** **Lo unico que se acerca, para que se juzgue:** el bloque de palabras de numero de la seccion
`6` copia la `L136` de mi encargo, que **nombra** `nodos_siguientes`; es texto mio de la `ACTA 75` y no el valor de ningun nodo. La
pagina entera la mide un `grep` sobre ella al cerrarla (seccion `8`).

HEREDADO 3: CUMPLIDO. **`R7`, mio** (`ACTA 75` `75.11`): toda linea de esta pagina que reparte un total en clases la imprime un
instrumento que cuenta **todas** las clases con el mismo predicado y **dice su `suma`**: los de `.v77aud/` la traen desde que nacen,
y los que reuso sin copiar (`.v70aud/poblacion.py` y el de `R8`) ya la traian. **Medido sobre la pagina misma** en la seccion `8`,
con la copia de `.v76aud/r7_pagina.py`.

HEREDADO 4: CUMPLIDO. **`R8`, mio** (`ACTA 75` `75.11`, *mi fase ciega de la `77`, sobre el encargo de la `77`*): **lo mido aqui con
el mismo instrumento de la `75.12`, sin copiarlo**, y su salida de hoy es identica a la que aquella acta guardo; la lectura, linea a
linea, en la seccion `6`. El encargo de la `78` lo escribo en mi turno normal y se mide alli.

HEREDADO 5: NO APLICA en esta fase. **Motivo:** `R9` es un remedio **del extractor** y se comprueba **en el reporte de la `77`, si
marca fidelidad sobre algo que la aduana levante en el acto** (`ACTA 75` `75.11`), y ese reporte **no esta en el arbol** (el bloque
de `ls` del HEREDADO `1`, que es el mismo fichero); no lo he recuperado. **Se mide en mi turno normal.** **Lo que si hago aqui es
aplicar su letra a mi propia lectura**: el `grep` de clausulas que comparan o califican la prueba, sobre los pasos de las `22` que
entraron, **cada coincidencia con su tramo literal del libro** (seccion `3`). La salida que sostiene que el reporte no esta:

@@RUN:0::ls docs/loop/REPORTE.md@@

HEREDADO 6: CUMPLIDO. **`R10`, mio** (`ACTA 75` `75.11`, *esta acta, `75.13`, y la `ACTA 76`*): toda salida pegada en
`PROMPT_SIGUIENTE.md` se corre despues de la ultima escritura del auditor en el registro que mide, o se vuelve a correr antes del
commit y se compara. **Lo mido sobre el encargo de la `77`**: las dos salidas pegadas (la clase y el tablero) **se volvieron a correr
despues de escribir el encargo y salieron identicas**, que es lo que guarda `.v76aud/normal/r10.txt`, escrito a las `09:17:58` contra
un encargo de las `09:16:28`. **No las vuelvo a correr hoy contra el encargo**, y lo digo: `DEUDA.jsonl` y `TABLERO.jsonl` cambiaron
despues (el pago de dos deudas y la escritura del arnes al arrancar, seccion `2`), asi que hoy saldrian distintas **sin que eso diga
nada del encargo**. **La otra mitad de su sitio, la `ACTA 76`, es de mi turno normal.**

@@RUN:0::cat .v76aud/normal/r10.txt@@
@@RUN:0::ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md .v76aud/normal/r10.txt docs/loop/DEUDA.jsonl docs/loop/TABLERO.jsonl | awk '{print $6, substr($7,1,8), $9}'@@

## 1. **LO QUE VI SIN BUSCARLO, Y LO DIGO ANTES DE MEDIR** (`d146`)

**La foto de `git status` que el entorno me pone delante trae los asuntos de los ultimos commits del extractor de la `77`, y
varios traen cifras y conclusiones de su vuelta**, que lei antes de medir nada:

- `b2d27bbc` *Vuelta 77, T5: el cierre (censo 459, 1172, 1, 0, 22; 8 PUENTE marcados y 0 que entraron; gate, guiones, suite y cierre
  estricto en verde; R5 en cero; tablero con gerber_emyth INSERTADO)*;
- `bd29146f` *Vuelta 77, T4 cerrada: las 22 de Gerber dentro, las 10 aristas esperadas en el grafo por los dos lados, ningun nodo viejo
  cambiado; d108 pagada*;
- `ddfc1d08` *Vuelta 77, fila 22: aplicar_cinco_pasos_proceso_contratacion insertado por la aduana, movido a _insertados*;
- y `a70bdf05` y `7f14a790`, sin cifras de medida (*la salida del hook del commit del cierre* y *fila 22: su fila en el reporte*).

Es el mismo hueco de `d146` que declararon las aperturas de la `65` a la `76`, y no lo arreglo yo (`D.45`).

**Y LO DEMAS DEL MISMO TIPO, QUE ES MIO:**

1. un `ls .v77ext` me ensenio **los nombres** de los ficheros de su carpeta, **no su contenido**: entre ellos un
   `arista_<madre>__<hijo>.txt` por arista declarada, y **uno es el de `fingir` a `recorrer`**, que me dice que **la arista de la
   conjunta que yo sostengo se declaro**; un `hook_NN.txt` y un `hook_fila_NN.txt` por fila, `aristas_vuelta.txt`, `censo_cierre.txt`,
   `cierre_reporte.txt`, `huellas_apertura.txt`, `contra_barrido.py`, `esperar.py` y `fila.py`. Los de arista, que son los que pesan,
   vueltos a listar por su nombre y nada mas:

@@RUN:0::ls .v77ext | grep "^arista_.*__"@@

2. la cola de `docs/loop/loop.log`, que no se retira, con el coste y el reloj del turno del extractor (bloque de la cabecera);
3. un `grep` de `d111` y `d108` en `docs/loop/DEUDA.jsonl`, que mi encargo manda pagar, **me enseno el principio de sus dos lineas
   de pago**: *La arista recorrer_siete_pasos_programa_desarrollo_negocio > construir_estrategia_gente_cuatro_componentes*
   y *Releida con las dos delante en la vuelta 76 (REPORTE 76.4.2, D76.19) y firmada por el auditor en la ACTA 7*. **Es prosa suya**, y
   lo digo; despues las medi **por campo** y sin su prosa (seccion `2`);
4. `python forja.py tablero`, que `D.49` manda leer y citar (seccion `2`). Tambien lei mi `ACTA 75` entera, mi encargo y
   `AUDITOR_FORJA.md` entero.

**LO QUE HAGO CON ELLO:** ninguna cifra de esta pagina sale de esos asuntos; todas salen de un instrumento corrido en esta fase, y
**donde coinciden lo digo como coincidencia y no como fuente**. **No he abierto nada de `.v77ext/` por dentro**, **ni
`bitacora/VEREDICTOS.jsonl` por dentro**: de la bitacora solo cuento lineas. **Mis clases de la tanda no las decido hoy**: son las de
mis ficheros sellados de la `76`, con las adjudicaciones de la `ACTA 75` `75.4` declaradas dentro de cada instrumento que las aplica.
**Y ESTO SI PESA SOBRE MI LECTURA, Y LO DIGO:** el nombre del fichero de la arista de `fingir` a `recorrer` lo vi **antes** de releer
esa pieza (seccion `5`). Mi `SOSTENGO` es el que selle en la `76` y el que mantuve en la `ACTA 75`, y lo releo con el libro delante;
**pero no puedo probar que no me empujo**.

## 2. **EL CENSO, Y QUE LO UNICO QUE SE MOVIO ES LO QUE EL ENCARGO MANDABA** (`D.38.4`, `D.38.5`, `D.49`)

@@RUN:0::wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl@@
@@RUN:0::for d in cuarentena/gerber_emyth cuarentena/_insertados/gerber_emyth cuarentena/_insertados/grove_high_output cuarentena/marquet_turn_the_ship; do echo "$d $(find $d -maxdepth 1 -name '*.json' 2>/dev/null | wc -l)"; done; echo "procesos $(ls -A procesos/ | wc -l)"@@
@@RUN:0::python .v70aud/poblacion.py@@
@@RUN:0::python forja.py gate | head -2@@
@@RUN:0::python forja.py tablero | sed -n '11,13p;24p'@@

**Sin `git`, lo que cambio desde que escribi mi encargo, por tres instrumentos.** Primero, **cualquier fichero** del dato, de las
bandejas, del codigo, de la configuracion o de los dos registros de la linea con fecha de escritura posterior a mi encargo (las fichas
de una misma carpeta, juntas):

@@RUN:0::find cuarentena dataset bitacora censos config fuentes esquema src scripts tests forja.py docs/loop/DEUDA.jsonl docs/loop/TABLERO.jsonl -type f -newer docs/loop/PROMPT_SIGUIENTE.md | sed 's|/[^/]*\.json$|/*.json|' | sort | uniq -c@@

Segundo, **las huellas que tome al lanzar mi barrido de la `76`** (las fichas de Gerber y de Marquet y el grafo) contra los ficheros de
hoy, buscando en `_insertados` la ficha que ya no esta en la bandeja:

@@RUN:0::python .v77aud/huellas_hoy.py@@

Tercero, **el grafo**: si al de hoy le quito las `22` filas de la tanda, y ademas los ids de las `22` de las listas de los nodos viejos,
sale el fichero que barri, byte a byte. **La vuelta `76` no movio el grafo** (mi `ACTA 75` `75.1`, con `git diff`), asi que ese
fichero es tambien el de la apertura de la `77`:

@@RUN:0::python .v77aud/grafo_sin_tanda.py@@

**Y las cuatro deudas que nombra mi encargo** (TAREA `4.5`), por campo y sin su prosa:

@@RUN:0::python .v77aud/deudas_encargo.py@@

**LECTURA:**

- **El grafo tiene `459` filas, la bitacora `1172` lineas, los pares mutuos `1`, la bandeja de Gerber `0` y sus insertados `22`, y
  `procesos/` esta vacio.** Marquet sigue en `20`, **con la huella de mi barrido de la `76`**, que es lo que el encargo pedia (*no
  tocas*). El tablero da a Gerber `INSERTADO` y deja a Marquet como el unico libro del corte que falta. **Coincide con el *censo 459,
  1172, 1, 0, 22* y el *tablero con gerber_emyth INSERTADO* del asunto de `b2d27bbc`**, y lo digo como coincidencia.
- **Las `22` fichas movidas a `_insertados` son las `22` de mi lista, con la huella que tenian cuando las barri**, y son las ultimas
  `22` filas del grafo.
- **(a) y (b) salen `SI`**, y el conteo de (b) es `0`: **los `437` nodos viejos son byte a byte los que barri**, y **ningun nodo viejo
  tiene un id de la tanda en ninguna lista**. Dice dos cosas a la vez: **las aristas de la tanda son todas entre nodos de la tanda**
  (seccion `4`), y **ningun otro nodo del grafo cambio**. Coincide con el *ningun nodo viejo cambiado* de `bd29146f`, y lo digo como
  coincidencia.
- **La poblacion de hoy es `479`**, la de mi barrido de la `76`, con `22` en otra sede.
- **Lo que se escribio despues de mi encargo** es el grafo, la bitacora, los dos `censos/` y los dos registros de la linea: lo que
  escriben una insercion, un pago de deuda y el arnes al arrancar; **nada en `config/`, `esquema/`, `fuentes/`, `src/`, `scripts/` ni
  `tests/`**. Las fichas movidas no salen en el `find` porque mover no cambia la fecha de escritura; las mide el segundo instrumento.
- **`d111` y `d108` tienen su linea de pago, en la `77`, y `d098` y `d104` siguen vivas**, que es lo que el encargo pedia. **Lo que
  cada pago dice** (su `--como`) **lo firmo o no en mi turno normal**, con la `ACTA 75` `75.4` delante.

## 3. **LAS `22`: LO QUE ENTRO ES LO QUE SE LEYO** (`D.58`), **Y SUS PASOS INVENTADOS** (`8`, `8.2`)

Cada nodo del grafo contra su ficha de `_insertados` (cuya huella es la leida, seccion `2`) en titulo, condiciones, pasos, entregable y
resumen; y sus pasos contra **mi** lectura entera sellada en la `76`, `.v76aud/fidelidad.tsv`, una fila por paso con su capitulo:

@@RUN:0::python .v77aud/entra_lo_leido.py@@

**Y `R9` con su letra sobre los pasos que entraron**, con el patron de mi `.v75aud/cap13_despues.py` (importado, no copiado) y el
tramo literal de cada coincidencia en la linea que mi fila le da:

@@RUN:0::python .v77aud/r9_gerber.py@@

**LECTURA:**

- **Las `22` viven en el grafo con los textos que se leyeron**, cada una con tantos pasos como filas tiene mi lectura. **`PASOS
  INVENTADOS` de lo que ENTRO: `0` en los diez capitulos**, que es la columna *PUENTE que entrara* que mi `ACTA 75` `75.3` firmo: los
  PUENTE de la preparacion se corrigieron en la bandeja **antes** de mi barrido, y mi unica `D` (`cap_12`, el paso `4` de
  `cuantificar_impacto_innovacion_6_pasos`) la adjudique `T` en la `75.3`, que no reabro (`D.47`). **Por debajo del `10`: no se baja
  escalon** (`8.1`), y de todos modos no queda lote de extraccion en el mundo `11`. **La relectura de fidelidad de `D.58` sobre lo que
  entra es esa lectura entera de la `76`**, porque lo que entro es byte a byte lo que lei. Coincide con el *0 que entraron* de
  `b2d27bbc`, y lo digo como coincidencia.
- **`R9` sobre Gerber: las coincidencias, todas con su tramo literal.** **Las de forma, una por una**: *prueba a preguntar* es el *try*
  de `cap_12` `L51`, no una prueba; *base de datos* es el *database* de `cap_19` `L337`; y el *a diferencia de* de
  `trazar_modelo_negocio_cliente_primero` paso `8` casa dentro de *la diferencia del*. **Las demas son clausulas que el libro pone**:
  *no hay nada peor que fingir* (`cap_18` `L165`), *no solo ... sino* (`cap_11` `L65`), *cualquier plan es mejor que ningun plan*
  (`cap_07` `L287`), *no casi iguales, sino iguales* (`cap_11` `L39`), *no del retrato del negocio sino del cliente* (`cap_08` `L119`) y
  *los estudios de mercado* (`cap_11` `L215`). **La que mas se acerca a un marco puesto, y la dejo escrita:** el mismo paso `8` de
  `trazar_modelo` cierra con *que es lo que el texto pone como la diferencia del modelo emprendedor*; el libro no escribe *difference*
  en `L119`, pero su *Thus, the Entrepreneurial Model does not start with* **es** la diferencia que el capitulo traza contra el modelo
  del tecnico, y el paso no anade procedimiento ni prueba. **Es mi `T` sellado de la `76`, firmado en la `75.3`, y no lo reabro.**
- **Lo que el `grep` no ve, y lo digo:** es un `grep` de forma, y una calificacion de la prueba con un verbo que no este en su lista no
  la ve. **No es una relectura**: la relectura de estos pasos es la de mi fase ciega de la `76`, firmada en la `ACTA 75`, y no la rehago
  (`D.47`).

## 4. **LO QUE MI LECTURA ESPERA QUE LA VUELTA DEJE, Y EL ORDEN EN QUE ENTRO**

Sacado **solo** de mis ficheros sellados de la `76`, con las tres adjudicaciones de la `ACTA 75` `75.4` aplicadas y declaradas dentro
del instrumento, y **con mi lectura en las dos piezas de la conjunta** (seccion `5`); la bitacora, solo contada; **y las aristas del
grafo, solo en cuentas y `SI` o `NO`, despues de imprimir las esperadas**:

@@RUN:0::python .v77aud/esperado_77.py@@

**LECTURA, y lo que se compara en el turno normal, no aqui:**

- **Aristas: `10`, las tres `CONTINUA` con `madre=` y las siete por lectura, todas con los dos extremos dentro de las `22`.** **Y el
  grafo tiene exactamente esas `10`, escritas por los dos lados, ninguna de mas.** Eso incluye **las dos de la conjunta tal como yo las
  leo**: `construir` a `aplicar_cinco` y `fingir` a `recorrer`. Coincide con el *las 10 aristas esperadas en el grafo por los dos
  lados* de `bd29146f`, y lo digo como coincidencia.
- **Lineas de bitacora.** Si cada `insertar` escribio una linea por fila dirigida que su aduana levanto, y la aduana levanto lo que mi
  barrido, son `54`: `6` `CONTINUA` y `48` `SANO` por la clase de su par; y cada arista por lectura escribe **una** mas. **La bitacora
  tiene las `1172` que eso da.** **Es coincidencia de cuenta y no de contenido**: no he abierto ni una linea. **Y LO QUE LA CUENTA NO
  DECIDE, dicho para que se mire:** la arista de `construir` a `aplicar_cinco` puede vivir por dos caminos, la linea `CONTINUA` con
  `madre=` que mi lectura pide, o una linea `SANO` mas una arista por lectura (`D.53`); **el segundo camino daria una linea mas**, y la
  cuenta no la tiene, **pero una cuenta que cuadra no prueba el contenido**: lo leo par a par en mi turno normal. **Mi lectura no espera
  ningun vecino sin linea preparada**, porque la poblacion es la del barrido (seccion `2`); uno que apareciera seria un hallazgo.

**El orden en que entraron, leido del grafo** (`src/aduana.py` escribe `nodos + [nuevo]`, asi que el orden de las filas es el de
entrada), contra el bloque de orden de mi encargo y contra las `16` restricciones de la `ACTA 75` `75.4`, leidas de su instrumento:

@@RUN:0::python .v77aud/orden_grafo.py@@

**LECTURA:** **las `22` entraron en el orden que mi encargo pego, fila a fila**, y **las `16` restricciones se cumplen**: las que obligan
(madre antes que hijo, las dos de la conjunta incluidas), las dos de mis `D.29` que cayeron en la `75.4` y ya no obligan, y las cuatro
de `D.36` de un solo lado, informativas. **Que cada `insertar` volviera antes de lanzar el siguiente lo miro en mi turno normal.**

## 5. **MI CLASIFICACION DE CADA CANDIDATO, Y LAS DOS PIEZAS DE LA CONJUNTA RELEIDAS** (`6.1`, y solo la vara `6.1`)

**Las `22`, una por una, en su orden de entrada**, de mis ficheros sellados: las lineas del libro que sus pasos transcriben, las filas
dirigidas de mi barrido en las que es candidata, sus pares sin orden por clase con la adjudicacion `(i)` de la `75.4`, y las aristas que
mi lectura le espera como hija y cuantas como madre:

@@RUN:0::python .v77aud/clasificacion_22.py@@

**LECTURA: LAS `22` SON NODO**, con la clase de cada par que selle en la `76` y las adjudicaciones de la `ACTA 75`. **No cambio
ninguna**: lo que entro es byte a byte lo que lei (secciones `2` y `3`). **`aplicar_ocho_reglas_juego_personas`** no levanta a nadie
ni la levanta nadie, y **`fingir_prototipo_cinco_mil_replicas`** solo esta en el par que levanta la contratacion: por eso la serie de
las seis reglas va por lectura (`D.37`), como la `ACTA 75` `75.4` firmo.

**LAS DOS PIEZAS DE LA CONJUNTA, RELEIDAS HOY CON EL LIBRO Y LOS PASOS DELANTE.** Las lineas que citan mis filas selladas:

@@RUN:0::python .v77aud/lineas_fuente.py@@

Y los pasos de sus cuatro nodos, por `pasos_ciego.py` (`R6`), que hoy los encuentra en el grafo:

@@RUN:0::python .v67aud/normal/pasos_ciego.py construir_estrategia_gente_cuatro_componentes aplicar_cinco_pasos_proceso_contratacion fingir_prototipo_cinco_mil_replicas recorrer_siete_pasos_programa_desarrollo_negocio@@

**LECTURA, UNA POR UNA, Y LAS DOS LAS MANTENGO:**

- **`construir_estrategia_gente_cuatro_componentes` madre de `aplicar_cinco_pasos_proceso_contratacion`, `CONTINUA`: MANTENGO.** Lo
  que el hijo anade a la madre (`6.1`, con direccion): la madre define la estrategia como **la forma de comunicar la idea** (su paso `1`,
  `L117`) y **compone** el Primary Aim, el Objetivo Estrategico, la Organizational Strategy con sus Position Contracts y los Operations
  Manuals (pasos `2` a `5`, `L119`); el hijo es **el primer medio de comunicarla** (su condicion, con las palabras de `L245`) y **usa
  el producto de la madre**: sus pasos `10` y `11` entregan el Manual de Operaciones y lo repasan *incluyendo el Objetivo Estrategico, la
  Organizational Strategy y el Position Contract de su propio puesto* (`L267` y `L269`), que es lo que la madre escribio en sus pasos
  `3` a `5`. **El libro los encadena con palabras**: `L245` abre la contratacion como medio de la idea que `L117` define, y `L247`
  abre la lista de sus componentes. **Procedimiento en los dos lados fuera del solape, sin bascula**: la madre compone documentos; el hijo
  presenta, entrevista, notifica y recibe (pasos `1` a `12`), y **no repite ningun paso de la madre**, asi que no es `REPITE`. **Lo que
  la madre no hace es nombrar al hijo**, y esa es la razon del `SANO` que `D76.15` escribio (`ACTA 75` `75.4`); **nombrar es la vara de
  la expansion, no la de la continuacion**, y la pregunta de `6.1` es la otra: que anade el hijo a lo que la madre deja hecho.
- **`fingir_prototipo_cinco_mil_replicas` madre de `recorrer_siete_pasos_programa_desarrollo_negocio`, arista por lectura `D.29`:
  MANTENGO.** La condicion del hijo es **el producto de la madre con sus palabras** (*Cuando ya finges que tu negocio es el prototipo
  de 5.000 replicas*, que es el paso `1` de la madre, `cap_11` `L35`); su paso `2` hace del programa **el vehiculo** con el que se
  construye ese prototipo (`cap_13` `L41`), y `cap_13` `L21` abre el capitulo **con la tarea que deja `cap_11`** (*Now you understand
  the task ahead*). **El hijo anade** el programa de siete pasos que la madre no trae; la madre pone el fingimiento y las seis reglas.
  **El barrido no levanta el par en ningun sentido** (`ACTA 75` `75.4`), y por eso va por `D.29` y no por linea. **No es `D.37`**: la
  madre no enumera los siete pasos ni el hijo es una de sus seis reglas.

**Y LO QUE ESTA RELECTURA NO PUEDE DECIR:** con que clase entro la linea del par de la contratacion en la bitacora, y que razon
escribio el extractor en la conjunta. **La arista vive** (seccion `4`), y eso es compatible con mi `CONTINUA` y con un `SANO` con arista
por lectura; lo decido con su reporte y su linea delante, en mi turno normal.

## 6. **`R8` MEDIDO SOBRE MI ENCARGO DE LA `77`, CON EL MISMO INSTRUMENTO** (`ACTA 75` `75.11`, `75.12`)

`R8` dice: *toda cifra de medida que escriba en `PROMPT_SIGUIENTE.md` (un reloj, una banda, una cuenta que solo se comprueba abriendo
un fichero, en digito o en letra) va DENTRO de un bloque `$` con su salida, o lleva EN SU MISMA LINEA la seccion del acta donde esta
pegada: ni la de la linea de al lado, ni una ruta de fichero*. El fichero es el encargo que escribi al cerrar la `ACTA 75`, y el
instrumento es el de la `75.12`, corrido sin copiarlo, con su salida de hoy contra la que guardo aquella acta:

@@RUN:0::head -1 docs/loop/PROMPT_SIGUIENTE.md | cut -c1-100; ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, $7, $9}'@@
@@RUN:0::python .v76aud/normal/r8_encargo77.py | diff - .v76aud/normal/r8_encargo77.txt && echo "IDENTICO a .v76aud/normal/r8_encargo77.txt, la salida de la ACTA 75 75.12"; python .v76aud/normal/r8_encargo77.py | tail -1@@

Las lineas de prosa con numero y **sin** seccion, cada una con los numeros que el instrumento le ve:

@@RUN:0::python .v76aud/normal/r8_encargo77.py | grep -E "^  L[0-9]+ - " | sed -E 's/\] \|.*$/]/'@@

**LECTURA, grupo a grupo, que es mia y no del instrumento; las volvi a leer una a una y no copio la de la `75.12`, aunque llego al
mismo reparto:**

- **Numeros de vuelta, de acta, de mundo o de carpeta de la casa**: `L3`, `L24`, `L30`, `L31`, `L32`, `L34`, `L42`, `L61`, `L64`,
  `L66`, `L70`, `L75`, `L120`, `L126`, `L129`, `L130`, `L145`, `L148`, `L149`, `L155` (`77`, `76`, `75`, `78`, `72`, `11`, y
  `.v64ext/`, `.v64aud/`, `.v72ext/`, `.v75ext/`, `.v76ext/` y `.v77ext/`).
- **Secciones, reglas, deudas, remedios y numeros de tarea, de punto o de lista**: `L4`, `L14`, `L44`, `L57`, `L59`, `L63`, `L65`,
  `L73`, `L117`, `L118`, `L119`, `L121`, `L122`, `L125`, `L127`, `L131`, `L135`, `L139`, `L147`, `L148`, `L162`, `L164`, `L165`,
  `L167`, `L169` (`1.4`, `1.3`, `6.1`, `2.2`, `4.3`, `4.5`, `D.29`, `D.31`, `D.37`, `D.47`, `D.53`, `D.55`, `D.61`, `D76.15`, `7.F`,
  `d031`, `d108`, `d111`, `R5`, `R9`, y los numeros de tarea, de punto y de fila).
- **Identificadores de capitulo o de punto de otro documento**: `cap_22` y el `8` punto `3` de `PARALELO.md` en `L23`.
- **Palabras de numero sin seccion**: *las dos piezas* (`L57`, los dos puntos numerados que siguen), *los dos extremos* (`L119`, los de
  una arista), *los dos delante* (`L127`, los dos nodos de un par), *por los dos lados* (`L136`, los dos extremos de una arista) y
  *cero guiones* (`L173`, la frase fija). **Ninguna es una cuenta de fichero.**

**LAS CUENTAS EN LETRA**, que el instrumento ve por palabra y que busco tambien con un `grep` mas ancho:

@@RUN:0::grep -n -i -w -E "uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|veinte|treinta|cero|mil|cien|ambas|ambos" docs/loop/PROMPT_SIGUIENTE.md | cut -c1-120@@

**LECTURA, linea a linea:** `L113` esta **dentro de un bloque `$`**; `L52` (*cuatro lecturas*), `L60` (*las dos lineas del par*),
`L69` (*ninguna de las dos*), `L123` (*las cuatro de `fingir`*), `L132` (*una parte de siete*) y `L146` (*en cero que entran*) llevan en
su misma linea su seccion de la `ACTA 75` (`75.9`, `75.4` y `75.3`); `L56` (*los dos delante*) lleva `75.4`; `L57` (*las dos piezas*)
son los dos puntos numerados que la siguen; `L119`, `L127` y `L136` son los dos extremos de una arista o los dos nodos de un par;
`L125` (*al volver cada uno*) es **una manera**, no una cuenta; `L163` (*en uno*) es un articulo; y `L173` (*cero guiones*) es **la meta
de la frase fija de cierre**. **Ninguna linea de prosa trae una cifra de medida sin su bloque o su seccion en la misma linea: `R8`
CUMPLIDO en el encargo de la `77`.**

## 7. **LO QUE DEJO PARA MI TURNO NORMAL, ESCRITO ANTES DE VER EL REPORTE**

1. **`R5`** en su reporte, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` sacados otra vez de los originales y con la
   cabecera cambiada a la `77`; y **`R9`** en su reporte, donde marque fidelidad sobre algo que la aduana levante en el acto, **contra
   el mio de la seccion `3`**.
2. **La conjunta** (TAREA `2`): su decision y su razon en las dos piezas, contra mi lectura de la seccion `5`; las lineas del par de la
   contratacion **en la bitacora**, con su clase y su `madre=`; la fila `SOSTENGO` o `NO SOSTENGO` de `fingir` a `recorrer`; y que el
   commit de la tarea sea anterior al primer `insertar`.
3. **Las lineas nuevas de la bitacora, una a una** (seccion `4`): las de veredicto contra las de `.v76ext/veredictos_listos.txt` o su
   copia corregida y contra mis clases selladas, **par a par contra las filas de mi barrido**; y las de arista por lectura, con su paso de
   madre.
4. **Que cada `insertar` volvio con su `.fin` en `0`, en el orden de `.v76ext/orden.txt`, uno por vez y sin solaparse**, y que **ninguna
   aduana levanto un vecino fuera de mi barrido**.
5. **La muestra pineada de los `SANO`** que la `77` escribio en la bitacora, **con semilla `77`**, el tamanio de la seccion `7` de
   `AUDITOR_FORJA.md` y su banda, releida contra mis clases selladas, que es lo que la `ACTA 75` `75.5` dejo para la `ACTA 76`.
6. **Las aristas par a par y por los dos lados, con sus ids**, contra las `10` de la seccion `4`, que aqui solo medi en cuentas (`R6`).
7. **Los pagos de `d111` y `d108`**: lo que dice cada `--como`, contra la `ACTA 75` `75.4`, para firmarlos o no.
8. **El censo con `git diff`, las guardas y el cierre estricto**, que tallara esta pagina: no tiene tablas, asi que un rojo en el suyo
   sera suyo. Y el coste de su turno (bloque de la cabecera) contra su clase (`D.55`).
9. **`R8`** sobre el encargo de la `78`, medido antes de cerrarlo, con las cuentas en letra incluidas; y **`R10`** en la `ACTA 76`.

## 8. **ESTA PAGINA CONTRA `R6`, `R7` Y LOS GUIONES, MEDIDA SOBRE ELLA MISMA**

El generador corre dos veces, y estos bloques de la segunda pasada leen la pagina que escribio la primera, identica salvo estos
bloques. El primero cuenta las lineas de bloque `$` que empiezan por una clave de relacion; el segundo, con la copia de
`.v76aud/r7_pagina.py`, cuenta las lineas de bloque que reparten una cifra en clases y cuantas traen su `suma`; el tercero cuenta
guiones largos y medios:

@@RUN:0::grep -c -E "^    +(previos|siguientes|nodos_previos|nodos_siguientes)" docs/loop/APERTURA_CIEGA.md@@
@@RUN:0::python .v77aud/r7_pagina.py@@
@@RUN:0::grep -c -P "\x{2014}|\x{2013}" docs/loop/APERTURA_CIEGA.md@@
