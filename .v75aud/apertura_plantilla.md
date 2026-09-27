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

@@RUN:0::cat .git/HEAD; cat .git/refs/heads/extraccion-mundo-11@@

**Y LO QUE ESA LIMITACION NO ME QUITA, porque lo mido por el dato** (seccion `2`): el grafo de hoy, con las `7` filas quitadas y las
tres operaciones de la TAREA `2` deshechas por lo que su codigo escribe, **es byte a byte el grafo que barri en la `73`**.

## 0. **LA HERENCIA** (`D.40`)

ACTA ANTERIOR LEIDA: c32dfaf57eb26b8cc4617f8e925e695b3a9b58c5

**Comprobada sin git**: es el blob de `docs/loop/ACTA_AUDITOR.md` tal como esta hoy en el arbol, calculado como lo calcula git. **La
`ACTA 73` la lei entera**, de su linea de cabecera a la ultima del fichero:

@@RUN:0::python .v75aud/huella_acta.py@@

HEREDADO 1: CUMPLIDO. **La TAREA BLOQUEANTE de mi `ACTA 73` `73.6`**, con la guarda `D.30` en rojo: los dos puentes de
`dar_elogio_disciplina_igual_critica` fuera del campo por `D.54`, primero `forja.py corregir` y despues `retirar_paso.py` sobre el
`17` y luego sobre el `8`. **La mido sobre el dato y no sobre el reporte**, que no tengo: los `18` pasos de hoy son los `20` que yo
imprimi en la `74` sin el `8` y sin el `17`, texto a texto; los dos literales retirados son esos dos; las tres operaciones estan en el
resumen **en el orden que pedi**; la correccion trae, literal, cada cosa que le pedi; y **ninguna retirada declarada sigue
viva en el campo**. Todo en la seccion `3`; aqui, la guarda y la linea del instrumento:

@@RUN:0::python scripts/retirar_paso.py --ver; echo "rc=$?"@@
@@RUN:0::python .v75aud/dar_elogio.py | sed -n '1,3p'@@

**LO QUE DE ELLA NO PUEDO MEDIR AQUI, Y LO DIGO:** que el `gate` saliera verde **despues de cada una** de las tres operaciones (hoy
sale verde, seccion `2`, pero el intermedio vive en su reporte), y la `--razon` de `corregir`, que va a la bitacora y **no la abro**
en esta fase. Las dos, en mi turno normal.

HEREDADO 2: NO APLICA en esta fase. **Motivo:** `R5` es un remedio **del extractor** y se mide **sobre su reporte de la `75`**
(`ACTA 73` `73.11`: *el reporte de la `75`, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera cambiada a
la `75`*), y el reporte **no esta en el arbol**: el arnes lo retiro para esta fase (`D.34.2`) y no lo he recuperado por ninguna via.
**Se mide en mi turno normal**, con los dos instrumentos sacados otra vez de los originales y no de las copias del extractor. Lo que
si esta en mi mano lo cumplo en mi pagina: cada bloque `$` lleva la salida del comando que abre, y nada mas.

@@RUN:0::ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl@@
@@RUN:0::grep -n "VUELTA 4 : APERTURA CIEGA" docs/loop/loop.log | tail -1@@

HEREDADO 3: CUMPLIDO. **`R6`, mio** (`ACTA 73` `73.11`): en esta fase los pasos de cualquier nodo los imprime
`.v67aud/normal/pasos_ciego.py`, que no ensenia `previos` ni `siguientes`, y **el unico bloque de pasos de esta pagina lo corre**
(seccion `6`). Los instrumentos mios de esta fase que **nombran** esas claves en su codigo:

@@RUN:0::grep -l -E "previos|siguientes" .v75aud/*.py@@

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

@@RUN:0::ls docs/loop/REPORTE.md@@

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

@@RUN:0::grep -n "VUELTA 4 : EXTRACTOR\|extractor listo" docs/loop/loop.log | tail -2@@

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

@@RUN:0::wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl@@
@@RUN:0::for d in cuarentena/grove_high_output cuarentena/_insertados/grove_high_output cuarentena/gerber_emyth cuarentena/marquet_turn_the_ship; do echo "$d $(find $d -maxdepth 1 -name '*.json' | wc -l)"; done; echo "procesos $(ls -A procesos/ | wc -l)"@@
@@RUN:0::python .v70aud/poblacion.py@@
@@RUN:0::python forja.py gate | head -2@@

**Sin `git`, lo que cambio desde que escribi mi encargo, por tres instrumentos.** Primero, **cualquier fichero** del dato, de las
bandejas, del codigo o de la configuracion con fecha de escritura posterior a mi encargo (las fichas de una misma carpeta, juntas):

@@RUN:0::ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, $7, $9}'@@
@@RUN:0::find cuarentena dataset bitacora censos config fuentes esquema src scripts tests forja.py -type f -newer docs/loop/PROMPT_SIGUIENTE.md | sed 's|/[^/]*\.json$|/*.json|' | sort | uniq -c@@

Segundo, **las `50` huellas que tome al lanzar mi barrido de la `73`** (las fichas de las tres bandejas y el grafo) contra los ficheros
de hoy, buscando en `_insertados` la ficha que ya no esta en la bandeja:

@@RUN:0::python .v75aud/huellas_hoy.py@@

Tercero, **el grafo**: si al de hoy le quito las `7` filas de la tanda, y ademas los ids de las `7` de las listas de los nodos viejos,
y ademas **deshago en `dar_elogio` las tres operaciones de la TAREA `2`** por lo que su codigo escribe (`src/correccion.py` solo
agrega al final del resumen; `scripts/retirar_paso.py` saca el paso y agrega al final del resumen su literal), sale el fichero que
barri, byte a byte. **La vuelta `74` no movio ningun dato** (mi `ACTA 73` `73.1`, con `git diff`), asi que ese fichero es tambien el
de la apertura de la `75`:

@@RUN:0::python .v75aud/grafo_sin_tanda.py@@

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

@@RUN:0::python .v75aud/dar_elogio.py@@

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

@@RUN:0::python .v75aud/cap13_despues.py@@

**Y el tramo literal del libro de cada coincidencia**, con un patron que escribo yo leyendo su linea (una fila por coincidencia, en el
orden del `grep`):

@@RUN:0::python .v75aud/r9_tramos.py@@

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

@@RUN:0::python .v75aud/entra_lo_leido.py@@

**Y `R9` con su letra sobre los `42` pasos que entraron**, con el mismo patron (importado del instrumento de la seccion `3`, no
copiado) y el tramo literal de cada coincidencia:

@@RUN:0::python .v75aud/r9_grove.py@@

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

@@RUN:0::python .v75aud/esperado_75.py@@

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

@@RUN:0::python .v75aud/orden_grafo.py@@

**LECTURA:** **las `7` entraron en el orden de pieza del libro de mi instrumento sellado**, y **las `5` restricciones se cumplen**: las
`3` que obligan (cada madre antes que su hijo), la que salia de mi `CONTINUA` caido a `SANO` y ya no obliga, y la `D.36` de un solo
lado, informativa. **Que ese orden sea el de `.v73ext/orden.txt` fila a fila** lo dice el bloque de mi propio encargo (`TAREA 4`), que
lo pega de ese fichero; que cada `insertar` volviera antes de lanzar el siguiente **lo miro en mi turno normal**.

## 6. **MI CLASIFICACION DE CADA CANDIDATO, Y LAS TRES ARISTAS RELEIDAS** (`6.1`, y solo la vara `6.1`)

**Las `7`, una por una**, de mis ficheros sellados: las lineas del libro que sus pasos transcriben, las filas dirigidas de mi barrido en
las que es candidata, sus pares sin orden por clase con la correccion de `D73.9` (cuenta los pares en los que esta de cualquiera de los
dos lados, y por eso puede pasar de sus filas), y las aristas que mi lectura le espera como hija y cuantas como madre:

@@RUN:0::python .v75aud/clasificacion_7.py@@

**LECTURA: LAS `7` SON NODO**, con la clase de cada par que selle en la `73` y la unica correccion adjudicada en la `ACTA 72`. **No
cambio ninguna**: lo que entro es byte a byte lo que lei (secciones `2` y `4`).

**Las tres aristas son las que el extractor cablea en el acto**, y **por eso las releo hoy con el libro y los pasos delante**. Las
lineas del libro que las sostienen, y la del par de `D73.9`:

@@RUN:0::python .v75aud/lineas_fuente.py@@

Y el final de `L111`, que el corte de `480` deja fuera y la primera arista necesita:

@@RUN:0::sed -n 111p fuentes/grove_high_output/cap_15.md | grep -o "Don.t try to change his mind[^.]*\. After he.s said all he has to say[^.]*\."@@

Y los pasos de sus cinco nodos, por `pasos_ciego.py` (`R6`), que hoy los encuentra en el grafo:

@@RUN:0::python .v67aud/normal/pasos_ciego.py responder_primer_aviso_renuncia_subordinado gestionar_retencion_subordinado_valioso_renuncia priorizar_lista_entrenamiento_subordinados desarrollar_primer_curso_entrenamiento pedir_critica_anonima_curso_entrenamiento_dictado@@

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

@@RUN:0::head -1 docs/loop/PROMPT_SIGUIENTE.md | cut -c1-100; ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, $7, $9}'@@
@@RUN:0::python .v74aud/normal/r8_encargo75.py | diff - .v74aud/normal/r8_encargo75.txt && echo "IDENTICO a .v74aud/normal/r8_encargo75.txt, la salida de la ACTA 73 73.12"; python .v74aud/normal/r8_encargo75.py | tail -1@@

Las lineas de prosa con numero y **sin** seccion, cada una con los numeros que el instrumento le ve:

@@RUN:0::python .v74aud/normal/r8_encargo75.py | grep -E "^  L[0-9]+ - " | sed -E 's/\] \|.*$/]/'@@

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

@@RUN:0::grep -n -i -w -E "uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|veinte|treinta|cero|mil|cien|ambas|ambos" docs/loop/PROMPT_SIGUIENTE.md | cut -c1-120@@

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

@@RUN:0::grep -c -E "^    +(previos|siguientes|nodos_previos|nodos_siguientes)" docs/loop/APERTURA_CIEGA.md@@
@@RUN:0::python .v75aud/r7_pagina.py@@
@@RUN:0::grep -c -P "\x{2014}|\x{2013}" docs/loop/APERTURA_CIEGA.md@@
