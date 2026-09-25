# APERTURA CIEGA DE LA VUELTA 70, lote 7 (`grove_high_output`), **CLASE INSERCION**

*Auditor `claude-opus-5-5`, fase ciega, 25 sep 2026, la que el arnes numera `VUELTA 6` en la corrida que arranco el
23 a las `21:50`. Linea **serial**, rama `extraccion-mundo-11`. Modo austero (`D.47`). Todo lo de esta pagina sale de
`.v70aud/`, escrito y corrido en esta fase; cada bloque `$` lo pega `.v70aud/generar_apertura.py` corriendo el
comando en el momento de escribirla. **No hay ninguna tabla en esta pagina**, a proposito, como en la `66`, la `68` y la
`69`. **En esta fase no corro `git`** (ni `log`, ni `diff`, ni `status`, ni `hash-object`): mido el arbol por sus
ficheros, sus huellas y sus fechas, y donde eso no alcanza lo digo como limitacion.*

## 0. **LA HERENCIA** (`D.40`)

ACTA ANTERIOR LEIDA: a2ad919527f64c4aefe1fee58278246df8191c74

**Y esta vez la compruebo sin git**: es el blob de `docs/loop/ACTA_AUDITOR.md` tal como esta hoy en el arbol,
calculado a mano como lo calcula git, con los finales de linea pasados a LF como manda `.gitattributes`. Tal cual no
cuadra y normalizado si, y lo pego las dos cosas para que se vea por que. La `ACTA 68` la lei entera, de su linea de
cabecera a la ultima del fichero:

@@RUN:0::python .v70aud/huella_acta.py@@

HEREDADO 1: NO APLICA en esta fase. **Motivo:** `R5` es un remedio **del extractor** y se mide **sobre su
reporte de la `70`** (`ACTA 68` `68.12`: *el reporte de la `70`, con `.v64ext/pegado64.py` y
`.v64aud/normal/bloques_mudos.py`, los dos con la cabecera del tramo cambiada a la `70`*), y el reporte **no esta
en el arbol**: el arnes lo retiro para esta fase (`D.34.2`) y no lo he recuperado por ninguna via. **Se mide en mi
turno normal**, con los dos instrumentos sacados otra vez de los originales y no de sus copias. Lo que si esta en mi
mano lo cumplo en mi pagina: cada bloque `$` lleva la salida del comando que abre, y nada mas.

@@RUN:0::ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl@@
@@RUN:0::grep -n "VUELTA 6 : APERTURA CIEGA" docs/loop/loop.log | tail -1@@

HEREDADO 2: CUMPLIDO. **`R6`, mio** (`ACTA 68` `68.12`): en esta fase los pasos de cualquier nodo los imprime
`.v67aud/normal/pasos_ciego.py`, que no enseña `previos` ni `siguientes`, y **el unico bloque de pasos de esta pagina lo
corre** (seccion `5`). Ningun instrumento mio de esta fase nombra esas claves:

@@RUN:0::grep -l -E "previos|siguientes" .v70aud/*.py | wc -l@@

**Y DIGO LO UNICO QUE SE ACERCA, para que se juzgue:** `.v70aud/grafo_sin_tanda.py` (seccion `2`) quita los ids de las
`20` de **cualquier lista** de los nodos viejos, sin nombrar ninguna clave, para reconstruir el grafo que barri en la
`68`, y **cuenta** cuantos nodos viejos tenian alguno. **No imprime ninguna clave ni ningun id de relacion**: una cuenta y
un `SI` o un `NO`. Es la misma cuenta que la `67` publico sacandola de `git` (*reescritos solo en claves de relacion*), y
como alli es **cuenta y no identidad**: que nodos son lo miro en el turno normal. El cumplimiento de la pagina entera lo
mide un `grep` sobre ella al cerrarla (seccion `7`).

HEREDADO 3: CUMPLIDO. **`R7`, mio** (`ACTA 68` `68.12`): toda linea de esta pagina que reparte un total en clases la
imprime un instrumento que cuenta **todas** las clases con el mismo predicado y **dice su `suma`**: los nuevos de
`.v70aud/` la traen desde que nacen (`huellas_hoy.py`, `entra_lo_leido.py`, `esperado_70.py`, `clasificacion_20.py`), y
los que reuso de la `69` ya la traian (`poblacion.py`, `aristas_70.py`). **Medido sobre la pagina misma** en la
seccion `7`, con `.v70aud/r7_pagina.py`.

## 1. **LO QUE VI SIN BUSCARLO, Y LO DIGO ANTES DE MEDIR** (`d146`)

**La foto de `git status` que el entorno me pone delante trae los asuntos de los cinco ultimos commits del extractor,
y tres traen sus conclusiones de esta vuelta**, que lei antes de leer nada:

- `6c40696` *Vuelta 70, T3 a T5: las 20 filas de cap_05 y cap_06 dentro, 7 de 7 aristas en el grafo, censo
  410/1027/1/27/65, 0 de 84 y 0 de 62, guardas en verde*;
- `4a10a65` *Vuelta 70: el cierre estricto en verde y la tabla de tareas al cerrar*;
- `d58cd8c` *Vuelta 70, fila 20: decidir_nivel_competente_inferior insertado por la aduana, movido a _insertados*;
- y `a34a1f7` y `cfcbbb6`, sin cifras (*fila 20: su fila en el reporte* y *la salida del hook del cierre*).

**Tambien lei la cola de `docs/loop/loop.log`**, que no se retira (el turno del extractor, su coste y su duracion), **mi
propio encargo** (`docs/loop/PROMPT_SIGUIENTE.md`, que es mio) y, para calcular la huella, `.gitattributes`; y busque con
`grep` una clave de fin de linea en el fichero `.git/config` **leyendolo como texto**, sin correr git, y no salio nada. Es
el mismo hueco de `d146` que declararon las aperturas de la `65` a la `69`, y no lo arreglo yo (`D.45`).

**LO QUE ESO LE HACE A ESTA PAGINA, SIN REBAJARLO:**

1. **Mis clases de la tanda no las decido hoy**: son las de mis ficheros sellados de la `68` (`.v68aud/mis_clases.tsv` y
   `.v68aud/aristas_lectura.tsv`), que la conjunta de la `69` dejo iguales en los `70` pares (`ACTA 68` `68.3`), mas la
   unica correccion que yo mismo adjudique en la `ACTA 67` `67.4.d`, declarada dentro de `.v69aud/aristas_70.py`.
2. **Ninguna cifra de esta pagina sale de esos asuntos**; todas salen de un instrumento corrido en esta fase, y **donde
   coinciden lo digo como coincidencia y no como fuente**.
3. **No he abierto nada de `.v70ext/`, `.v69ext/` ni `.v68ext/`**, ni `bitacora/VEREDICTOS.jsonl` por dentro: de ella solo
   cuento lineas.
4. **Lo que `d58cd8c` quiere decir con *insertado por la aduana* no lo se**, y no lo adivino: lo leo en el reporte.

## 2. **EL CENSO, Y QUE LA POBLACION DE LA ADUANA ES LA DE MI BARRIDO DE LA `68`** (`D.38.4`, `D.38.5`)

La vuelta es **de insercion** (mi encargo, seccion `0`): las `20` filas de `cap_05` y `cap_06`, una por vez.

@@RUN:0::wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl@@
@@RUN:0::ls cuarentena/grove_high_output/*.json | wc -l@@
@@RUN:0::ls cuarentena/_insertados/grove_high_output/*.json | wc -l@@
@@RUN:0::ls cuarentena/gerber_emyth/*.json cuarentena/marquet_turn_the_ship/*.json | wc -l@@
@@RUN:0::ls -A procesos/ | wc -l@@
@@RUN:0::python forja.py gate | head -2@@

**Sin `git`, lo que cambio desde mi barrido de la `68`, por tres instrumentos.** Primero, **cualquier fichero** del dato,
de las bandejas, del codigo o de la configuracion con fecha de escritura posterior a las huellas que tome al lanzarlo,
uno por linea:

@@RUN:0::ls -l --time-style=full-iso .v68aud/huellas_al_barrer.txt | awk '{print $6, $7, $9}'@@
@@RUN:0::find cuarentena dataset bitacora censos config fuentes esquema src scripts -type f -newer .v68aud/huellas_al_barrer.txt | sort@@

Segundo, **las `50` huellas de entonces** (las `47` fichas de Grove, las dos filas de `cap_04` y el grafo) contra los
ficheros de hoy, buscando en `_insertados` la ficha que ya no esta en la bandeja:

@@RUN:0::python .v70aud/huellas_hoy.py@@

Tercero, **el grafo**: si al de hoy le quito las `20` filas de la tanda, y ademas los ids de las `20` de las listas de los
nodos viejos, sale el fichero que barri, byte a byte:

@@RUN:0::python .v70aud/grafo_sin_tanda.py@@
@@RUN:0::python .v70aud/poblacion.py@@

**LECTURA:**

- **El grafo tiene `410` filas, la bandeja de Grove `27`, sus insertados `65`, los pares mutuos `1` y `procesos/` esta
  vacio.** Coincide con el `410/1027/1/27/65` del asunto de `6c40696`, y lo digo como coincidencia.
- **Las `20` fichas movidas a `_insertados` son las `20` de mi lista, con la huella que tenian cuando las barri**, y las
  `27` que quedan en la bandeja y las dos filas de `cap_04`, tambien.
- **Los `390` nodos viejos son byte a byte los que barri, salvo `3` que ganaron algun id de la tanda en alguna lista**: sin
  esos ids, el fichero reconstruido tiene la huella de mi barrido. Quitando solo las filas no la tiene, y eso es lo que
  se espera si la tanda cableo madres viejas. **La cuenta `3` coincide con las `3` madres viejas que mi lectura espera**
  (seccion `4`), y es **cuenta y no identidad**. Las `20` son las ultimas filas del fichero.
- **Ningun fichero de `src/`, `scripts/`, `config/`, `esquema/`, `fuentes/` ni de ninguna bandeja se escribio despues
  de mis huellas**; lo que se escribio es el grafo, la bitacora y dos censos, que es lo que escribe una insercion. **Lo que
  no veo:** Gerber y Marquet no estan en mis huellas, asi que de ellas **mido la fecha y no el contenido**.
- **La poblacion de hoy es `479`**, la de mi barrido, con `20` en otra sede. Con el codigo, los umbrales y los textos
  iguales, **la aduana de cada `insertar` tuvo delante lo que tuvo mi barrido**, porque mover una ficha de la bandeja al
  grafo no la saca de la poblacion, y `buscar_vecinos` y `medir` miden titulo, resumen, pasos, id y dominio, **no las claves
  de relacion** (`src/aduana.py` y `texto_comparable` de `src/comun.py`, que lei).

## 3. **LAS `20`: LO QUE ENTRO ES LO QUE SE LEYO** (`D.58`), **Y SUS PASOS INVENTADOS** (`8`, `8.2`)

Cada nodo del grafo contra su ficha de `_insertados` (cuya huella es la leida, seccion `2`) en titulo, condiciones,
pasos, entregable y resumen; y sus pasos contra **mi** lectura entera sellada en la `68`, `.v68aud/fidelidad_fuente.txt`,
una fila por paso:

@@RUN:0::python .v70aud/entra_lo_leido.py@@

**LECTURA:** las `20` viven en el grafo **con los textos que se leyeron**, y cada una con tantos pasos como filas tiene mi
lectura. **`PASOS INVENTADOS` de lo que ENTRO: `cap_05` `0` de `84` y `cap_06` `0` de `62`**, las cifras firmadas en la
`ACTA 67` `67.5` y la `ACTA 68` `68.6`; mis `D` las adjudico `T` la `ACTA 67` `67.4.a`, y no lo reabro (`D.47`). **Por debajo
del `10`: no se baja escalon** (`8.1`). Coincide con el *0 de 84 y 0 de 62* de `6c40696`, y lo digo como coincidencia.

## 4. **LO QUE MI LECTURA ESPERA QUE LA TANDA DEJE**

Sacado **solo** de mis ficheros sellados de la `68` y de `.v69aud/aristas_70.py`; la bitacora, solo contada:

@@RUN:0::python .v70aud/esperado_70.py@@
@@RUN:0::python .v69aud/aristas_70.py@@

**LECTURA, y lo que se compara en el turno normal, no aqui:**

- **Lineas de bitacora.** Si cada `insertar` escribio una linea por vecino que su aduana levanto, y la aduana levanto lo
  que mi barrido (seccion `2`), son `118`: `4` `CONTINUA` y `114` `SANO` por la clase sellada de su par; y `python forja.py
  arista` escribe su propia linea, asi que con mis `5` por lectura son `904` mas `118` mas `5`. **La bitacora tiene `1027`.** **Es
  coincidencia de cuenta y no de contenido**: no he abierto ni una linea. **Mi lectura no espera ningun vecino sin linea
  preparada**, porque la poblacion es la del barrido; uno que apareciera seria un hallazgo.
- **Aristas: `7`**, las `2` `CONTINUA` de las notas y `5` por lectura, **ninguna con madre
  `usar_tres_clases_reunion_proceso`**, y `3` de ellas con madre vieja (`buscar_regularidad` y `agrupar_tareas` a
  `infundir`, y `agrupar_interrupciones` a `acumular`). Coincide con el *7 de 7* de `6c40696`, y con la cuenta `3` de la
  seccion `2`: **par a par lo cruzo en el turno normal**, que es donde un `7` igual con pares distintos se veria.

## 5. **MI CLASIFICACION DE CADA CANDIDATO, Y LAS CINCO ARISTAS POR LECTURA RELEIDAS** (`6.1`, y solo la vara `6.1`)

**Las `20`, una por una**, de mis ficheros sellados: las lineas del libro que sus pasos transcriben, las filas dirigidas
de mi barrido en las que es candidata, sus pares sin orden por clase (cuenta los pares en los que esta de cualquiera de
los dos lados, y por eso puede pasar de sus filas) y las aristas que mi lectura le espera como hija:

@@RUN:0::python .v70aud/clasificacion_20.py@@

**LECTURA: LAS `20` SON NODO**, con la clase de cada par que selle en la `68`. De la `68` a hoy no he cambiado ninguna: la
conjunta de la `69` las dejo como estaban (`ACTA 68` `68.3`).

**Las cinco aristas por lectura son las que el extractor cablea a mano con `python forja.py arista`**, y por eso las releo
hoy con el libro y los pasos delante. Las lineas del libro que las sostienen (tambien las de las dos `CONTINUA`):

@@RUN:0::python .v70aud/lineas_fuente.py@@

Y los pasos de sus ocho nodos, por `pasos_ciego.py` (`R6`):

@@RUN:0::python .v67aud/normal/pasos_ciego.py conducir_etapas_modelo_ideal_decision ejercer_poder_posicion_etapa_decision_clara cortar_discusion_libre_momento_justo agrupar_interrupciones_subordinados_reuniones_regulares acumular_asuntos_importantes_fichero_espera buscar_regularidad_bloques_iguales_trabajo_mando agrupar_tareas_semejantes_aprovechar_preparacion infundir_regularidad_reunion_proceso@@

**LECTURA, UNA POR UNA, Y LAS CINCO LAS SOSTENGO:**

- **`conducir_etapas` a `ejercer_poder`: SOSTENGO.** La condicion de la hija (*ninguna cantidad de discusion va a producir
  consenso y el momento de decidir ha llegado claramente*) es el producto del paso `5` de la madre, **pasar a la etapa de
  decision clara**; y la hija anade lo que la madre no dice, **quien decide y con que autoridad** (sus pasos `2` a `5`, L61:
  *legitimate ... if the clear decision stage is reached and no consensus has developed*). No repite: la madre no nombra
  el poder de posicion.
- **`conducir_etapas` a `cortar_discusion`: SOSTENGO.** La condicion de la hija (*diriges una discusion libre y tienes que
  decidir si ya es momento de pasar a la decision*) es el paso `1` de la madre ya en marcha, que desemboca en su paso `5`; y
  la hija anade **el criterio del momento** (L63, *don't push for a decision prematurely* y *if you feel that you have
  already heard everything*), que la madre no trae. **Las dos hijas son hermanas entre si** (mi `NO, DUDA` de
  `cortar_discusion` a `ejercer_poder`, sellado): las dos parten de la frontera entre la etapa `1` y la `2`, una por el
  cuando y otra por el quien.
- **`agrupar_interrupciones` a `acumular`: SOSTENGO.** L51 remite con palabras a la pieza de la madre (*which constitute
  the interruptions we considered earlier*); la condicion de la hija (*entre una reunion individual y la siguiente
  aparecen asuntos*) parte del producto de la madre, las interrupciones acumuladas para las reuniones regulares (sus pasos
  `2` y `3`), y la hija anade **el fichero compartido por las dos partes** y el filtro de lo importante y no urgente.
- **`buscar_regularidad` a `infundir`: SOSTENGO, con la `DUDA` sellada.** La condicion de la hija (*una reunion de las que
  se repiten en un calendario fijo*) es el producto de los pasos `8` y `9` de la madre, **los mismos bloques de tiempo para
  las actividades iguales**, con el lunes de los grupos de planificacion; y la hija anade la regularidad **dentro** de la
  reunion (sus pasos `2` a `4`) y el pronostico (`6` y `7`). La duda sigue escrita: se pueden leer como el mismo principio
  aplicado a la jornada y a la reunion.
- **`agrupar_tareas` a `infundir`: SOSTENGO, por la adjudicacion de la `ACTA 67` `67.4.d`**, que dio la razon al extractor
  dentro de mi `DUDA`. El paso `5` de la hija **procedimenta** la tanda (*usar el mismo tiempo y esfuerzo de preparacion ...
  para atender muchas tareas de mando semejantes*, L21), no solo la nombra, y eso es usar el producto de `agrupar_tareas`
  (su paso `3`, el mismo esfuerzo de preparacion aplicado a un grupo). **No la reabro** (`D.47`): la escribo para que se vea
  que la releo y que se sostiene.

## 6. **LO QUE DEJO PARA MI TURNO NORMAL, ESCRITO ANTES DE VER EL REPORTE**

1. **`R5`** en su reporte, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` sacados otra vez de los
   originales y con la cabecera cambiada a la `70`.
2. **Las lineas nuevas de la bitacora**, una a una: las `118` contra las vivas de `.v68ext/veredictos_listos.txt`
   (con las corregidas por la conjunta de la `69` y sin ninguna de las que quedaron en comentario) y contra mis clases
   selladas, y las `5` de `forja.py arista` contra mis cinco `SOSTENGO` de la seccion `5`, con su paso.
3. **Las `7` aristas, par a par**, contra `.v69aud/aristas_70.py`; que los `3` nodos viejos reescritos son las `3` madres
   viejas y que **solo** cambiaron sus claves de relacion; y **ninguna con madre `usar_tres_clases_reunion_proceso`**.
4. **Que cada `insertar` volvio con su `.fin` en `0`, en el orden de `.v69aud/restricciones_orden.py`, uno por vez y sin
   solaparse**, y que **ninguna aduana levanto un vecino fuera de mi barrido**; y que quiere decir `d58cd8c` con *insertado
   por la aduana* en la fila `20` (seccion `1`, punto `4`).
5. **La muestra pineada de los SANO** que la `70` escribio en la bitacora, **con semilla `70`**, el tamaño de la seccion
   `7` y su banda, releida contra mis clases selladas.
6. **El censo, las guardas y el cierre estricto**, que tallara esta pagina: no tiene tablas, asi que un rojo en el suyo
   sera suyo. Y el coste de su turno, del `loop.log`, contra su clase (`D.55`).

## 7. **ESTA PAGINA CONTRA `R6` Y `R7`, MEDIDA SOBRE ELLA MISMA**

El generador corre dos veces, y estos bloques de la segunda pasada leen la pagina que escribio la primera, identica
salvo ellos. El primero cuenta las lineas de bloque `$` que empiezan por una clave de relacion (las que la nombran en
mis frases y comandos no cuentan, porque la nombran para decir que no la imprimo); el segundo, las lineas de bloque que
reparten en clases, y cuantas traen su `suma`; el tercero, las rayas y guiones medios de la pagina:

@@RUN:0::grep -c -E "^    +(previos|siguientes|nodos_previos|nodos_siguientes)" docs/loop/APERTURA_CIEGA.md@@
@@RUN:0::python .v70aud/r7_pagina.py@@
@@RUN:0::grep -c -P "\x{2014}|\x{2013}" docs/loop/APERTURA_CIEGA.md@@
