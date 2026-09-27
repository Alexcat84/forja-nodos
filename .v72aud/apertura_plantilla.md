# APERTURA CIEGA DE LA VUELTA 72, lote 7 (`grove_high_output`), **CLASE INSERCION**

*Auditor `claude-opus-5-5`, fase ciega, 26 sep 2026, la que el arnes numera `VUELTA 1` en la corrida que arranco el 25 a
las `21:43`. Linea **serial**, rama `extraccion-mundo-11`. Modo austero (`D.47`). Todo lo de esta pagina sale de `.v72aud/`,
escrito y corrido en esta fase; cada bloque `$` lo pega `.v72aud/generar_apertura.py` corriendo el comando en el momento de
escribirla. **No hay ninguna tabla en esta pagina**, a proposito, como en la `70` y la `71`.*

**UNA CAIDA DE METODO MIA, DICHA ANTES DE NADA: EN ESTA FASE CORRI `git` UNA VEZ.** Al abrir, para saber el tamaño del acta,
corri en la carpeta viva `git -C . log -1 --format=%H`, que imprimio **solo** el hash del ultimo commit
(`f5bba45a2edb332bb597b71dd0b943274cbe56f8`), ningun asunto, ningun fichero y nada retirado. **Va contra lo que yo mismo
escribi en la `71`** (*la carpeta de una linea viva es solo del arnes*, `PARALELO.md` `7`), y lo digo aqui para que se juzgue.
**No recupere nada**: los cuatro retirados siguen sin estar (seccion `0`). Despues, el commit lo leo de los ficheros de
`.git/` sin correr `git`, y da el mismo:

@@RUN:0::cat .git/HEAD; cat .git/refs/heads/extraccion-mundo-11@@

## 0. **LA HERENCIA** (`D.40`)

ACTA ANTERIOR LEIDA: 99aaf1437e0189f273b01c6c1f1d9c0d24f78706

**Comprobada sin git**: es el blob de `docs/loop/ACTA_AUDITOR.md` tal como esta hoy en el arbol, calculado a mano como lo
calcula git. La `ACTA 70` la lei entera, de su linea de cabecera a la ultima del fichero:

@@RUN:0::python .v72aud/huella_acta.py@@

HEREDADO 1: NO APLICA en esta fase. **Motivo:** `R5` es un remedio **del extractor** y se mide **sobre su reporte de la
`72`** (`ACTA 70` `70.12`: *el reporte de la `72`, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py`, los dos con
la cabecera del tramo cambiada a la `72`*), y el reporte **no esta en el arbol**: el arnes lo retiro para esta fase (`D.34.2`)
y no lo he recuperado por ninguna via. **Se mide en mi turno normal**, con los dos instrumentos sacados otra vez de los
originales y no de las copias del extractor. Lo que si esta en mi mano lo cumplo en mi pagina: cada bloque `$` lleva la salida
del comando que abre, y nada mas.

@@RUN:0::ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl@@
@@RUN:0::grep -n "VUELTA 1 : APERTURA CIEGA" docs/loop/loop.log | tail -1@@

HEREDADO 2: CUMPLIDO. **`R6`, mio** (`ACTA 70` `70.12`): en esta fase los pasos de cualquier nodo los imprime
`.v67aud/normal/pasos_ciego.py`, que no enseña `previos` ni `siguientes`, y **el unico bloque de pasos de esta pagina lo corre**
(seccion `5`). Ningun instrumento mio de esta fase nombra esas claves:

@@RUN:0::grep -l -E "previos|siguientes" .v72aud/*.py | wc -l@@

**Y DIGO LO UNICO QUE SE ACERCA, para que se juzgue:** `.v72aud/grafo_sin_tanda.py` (seccion `2`), copia del de la `70`, quita
los ids de las `20` de **cualquier lista** de los nodos viejos, sin nombrar ninguna clave, y **cuenta** cuantos nodos viejos
tenian alguno: imprime una cuenta y un `SI` o un `NO`, **ninguna clave ni ningun id de relacion**. Y `.v72aud/r8_encargo.py`
(seccion `6`) imprime lineas de mi encargo, que nombra una clave de relacion en su linea `99`: esa linea **no la imprime**,
porque no trae cifra. El cumplimiento de la pagina entera lo mide un `grep` sobre ella al cerrarla (seccion `8`).

HEREDADO 3: CUMPLIDO. **`R7`, mio** (`ACTA 70` `70.12`): toda linea de esta pagina que reparte un total en clases la imprime un
instrumento que cuenta **todas** las clases con el mismo predicado y **dice su `suma`**: los de `.v72aud/` la traen desde que
nacen, y el que reuso de la `70` (`poblacion.py`) ya la traia. **Medido sobre la pagina misma** en la seccion `8`, con la copia
de `.v70aud/r7_pagina.py`.

HEREDADO 4: NO APLICA a lo que esta fase escribe, porque no escribe ningun encargo; Y NO LO DOY POR CUMPLIDO: medido sobre su primera sede, mi encargo de la `72`, lo rompo en tres cifras (seccion `6`). **Motivo del `NO APLICA`:** `R8`
(`ACTA 70` `70.12`) manda sobre las cifras de medida que escribo en `docs/loop/PROMPT_SIGUIENTE.md`, y se comprueba en *el
encargo de la `72` (este mismo turno) y el de la `73`*. **El de la `73` lo escribo en mi turno normal, y esta fase no toca ese
fichero.** Pero el de la `72` ya esta escrito, es mio y lo puedo medir aqui, **y lo mido**: la salida entera y la lectura, cifra
por cifra, en la seccion `6`. El bloque que sostiene el motivo, que el fichero es el que escribi al cerrar la `ACTA 70`:

@@RUN:0::head -3 docs/loop/PROMPT_SIGUIENTE.md | cut -c1-120; ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, $7, $9}'@@

## 1. **LO QUE VI SIN BUSCARLO, Y LO DIGO ANTES DE MEDIR** (`d146`)

**La foto de `git status` que el entorno me pone delante trae los asuntos de los cinco ultimos commits del extractor, y dos
traen conclusiones de esta vuelta**, que lei antes de medir nada:

- `4b6382a0` *Vuelta 72, T5: el cierre (censo 430/1081/1/7/85, PASOS INVENTADOS 0 que entraron, D.61 sin abiertos, R5, guardas
  y cierre estricto en verde)*;
- `b9d02af4` *Vuelta 72, T4: las 6 aristas de la tanda en el grafo, adjudicadas; ningun nodo viejo cambia*;
- y `f5bba45a`, `25856653` y `d81a1b91`, sin cifras (*la salida del hook*, *R5 con el reporte entero*, *fila 20: su fila en el
  reporte*).

**Tambien lei la cola de `docs/loop/loop.log`**, que no se retira (el turno del extractor: `13455` s y `7,03` USD), **mi propio
encargo** (`docs/loop/PROMPT_SIGUIENTE.md`, que es mio), la ultima linea de `.v71ext/orden.txt` (la cifra `6` que mi encargo
cita, seccion `6`; es de la vuelta que ya audite), y del codigo, para saber que cambio (seccion `2`), el docstring de
`src/presupuesto.py` y las lineas de `src/aduana.py` que lo nombran. Las lineas del `loop.log` que lei y cito:

@@RUN:0::grep -n "VUELTA 1 : EXTRACTOR\|extractor listo" docs/loop/loop.log | tail -2@@

**LO QUE ESO LE HACE A ESTA PAGINA, SIN REBAJARLO:**

1. **Mis clases de la tanda no las decido hoy**: son las de mis ficheros sellados de la `71` (`.v71aud/mis_clases.tsv` y
   `.v71aud/aristas_lectura.tsv`), mas la unica correccion que la `ACTA 70` `70.5` adjudico (mis dos `CONTINUA` de
   `cerrar_brecha_dos_preguntas_estrategia` caen a `SANO`), declarada dentro de `.v72aud/esperado_72.py`.
2. **Ninguna cifra de esta pagina sale de esos asuntos**; todas salen de un instrumento corrido en esta fase, y **donde
   coinciden lo digo como coincidencia y no como fuente**.
3. **No he abierto nada de `.v72ext/`**, ni `bitacora/VEREDICTOS.jsonl` ni `docs/loop/DEUDA.jsonl` por dentro: de la bitacora
   solo cuento lineas.

## 2. **EL CENSO, Y QUE LA POBLACION DE LA ADUANA ES LA DE MI BARRIDO DE LA `71`** (`D.38.4`, `D.38.5`)

La vuelta es **de insercion** (mi encargo): las `20` filas de `.v71ext/orden.txt`, una por vez.

@@RUN:0::wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl@@
@@RUN:0::for d in cuarentena/grove_high_output cuarentena/_insertados/grove_high_output cuarentena/gerber_emyth cuarentena/marquet_turn_the_ship; do echo "$d $(ls $d/*.json | wc -l)"; done; echo "procesos $(ls -A procesos/ | wc -l)"@@
@@RUN:0::python forja.py gate | head -2@@

**Sin `git`, lo que cambio desde mi barrido de la `71`, por tres instrumentos.** Primero, **cualquier fichero** del dato, de las
bandejas, del codigo o de la configuracion con fecha de escritura posterior a las huellas que tome al lanzarlo (las fichas de
una misma carpeta, juntas):

@@RUN:0::ls -l --time-style=full-iso .v71aud/huellas_al_barrer.txt | awk '{print $6, $7, $9}'@@
@@RUN:0::find cuarentena dataset bitacora censos config fuentes esquema src scripts -type f -newer .v71aud/huellas_al_barrer.txt | sed 's|/[^/]*\.json$|/*.json|' | sort | uniq -c@@
@@RUN:0::ls -l --time-style=full-iso src/aduana.py src/presupuesto.py scripts/lanzar_linea.ps1 scripts/prioridad_baja.ps1 | awk '{print $6, $7, $9}'@@

Segundo, **las `70` huellas de entonces** (las fichas de las tres bandejas y el grafo) contra los ficheros de hoy, buscando en
`_insertados` la ficha que ya no esta en la bandeja:

@@RUN:0::python .v72aud/huellas_hoy.py@@

Tercero, **el grafo**: si al de hoy le quito las `20` filas de la tanda, y ademas los ids de las `20` de las listas de los nodos
viejos, sale el fichero que barri, byte a byte:

@@RUN:0::python .v72aud/grafo_sin_tanda.py@@
@@RUN:0::python .v70aud/poblacion.py@@

**LECTURA:**

- **El grafo tiene `430` filas, la bandeja de Grove `7`, sus insertados `85`, los pares mutuos `1`, la bitacora `1081` lineas,
  y `procesos/` esta vacio.** Coincide con el `430/1081/1/7/85` del asunto de `4b6382a0`, y lo digo como coincidencia. Gerber y
  Marquet siguen en `22` y `20`, con la huella de mi barrido.
- **Las `20` fichas movidas a `_insertados` son las `20` de mi lista, con la huella que tenian cuando las barri**, y las `7`
  que quedan en la bandeja, tambien.
- **Los `410` nodos viejos son byte a byte los que barri, SIN QUITAR NINGUN ID**: ningun nodo viejo tiene un id de la tanda en
  ninguna lista, y el fichero sin las `20` filas ya tiene la huella de mi barrido. **Es lo que mi lectura espera**: ninguna de
  mis `6` aristas tiene un extremo fuera de las `20` (seccion `4`). Coincide con el *ningun nodo viejo cambia* de `b9d02af4`.
  Las `20` son las ultimas filas del fichero.
- **La poblacion de hoy es `479`**, la de mi barrido, con `20` en otra sede.
- **LO QUE CAMBIO Y NO PUEDO MEDIR SIN `git`: `src/aduana.py`, `src/presupuesto.py` y dos guiones de `scripts/` se escribieron el
  25 a las `21:43:35`, despues de mi barrido** (`19:57`) y trece segundos antes de que el arnes abriera el turno del extractor
  (`21:43:48` en `docs/loop/loop.log`, seccion `1`), y `src/presupuesto.py` se presenta en su docstring como *decision del
  fundador, 25 sep 2026* (el bloque de abajo). **LECTURA, y es lectura:** por el
  docstring de `src/presupuesto.py` y las lineas de `src/aduana.py` que lo nombran (`from . import presupuesto`, el reparto de
  procesos y la `PlazaPropia` de la senial `3`), el cambio reparte **cuantos procesos** calculan, no **que** se mide; y la `ACTA
  70` `70.1` ya midio que repartir la senial `1` no cambia ni pares ni cifras. **Pero no he visto el diff**, y por eso lo que la
  aduana de hoy levanto no lo doy por igual a mi barrido por el codigo: lo compruebo **por el dato**, par a par, en mi turno
  normal (seccion `7`). El indicio de aqui es solo de cuenta: la bitacora tiene las lineas que mi barrido espera (seccion `4`).

@@RUN:0::sed -n 2p src/presupuesto.py; grep -c "presupuesto" src/aduana.py@@
- **Lo que se escribio despues de mis huellas en el dato** es el grafo, la bitacora y dos censos (`atribuciones.md` y
  `denominaciones.md`), que es lo que escribe una insercion; **nada en `config/`, `esquema/`, `fuentes/` ni en las bandejas**.

## 3. **LAS `20`: LO QUE ENTRO ES LO QUE SE LEYO** (`D.58`), **Y SUS PASOS INVENTADOS** (`8`, `8.2`)

Cada nodo del grafo contra su ficha de `_insertados` (cuya huella es la leida, seccion `2`) en titulo, condiciones, pasos,
entregable y resumen; y sus pasos contra **mi** lectura entera sellada en la `71`, `.v71aud/fidelidad_fuente.txt`, una fila por
paso:

@@RUN:0::python .v72aud/entra_lo_leido.py@@

**LECTURA:** las `20` viven en el grafo **con los textos que se leyeron**, y cada una con tantos pasos como filas tiene mi
lectura. **`PASOS INVENTADOS` de lo que ENTRO: `0` en los seis capitulos** (`cap_07` `0` de `53`, `cap_10` `0` de `8`, `cap_11`
`0` de `17`, `cap_12` `0` de `11`, `cap_13` `0` de `14` y `cap_14` `0` de `18`), que son las cifras que la `ACTA 70` `70.6` firmo
como *PUENTE que entrara*: los `4` PUENTE de la preparacion se corrigieron en la bandeja **antes** de mi barrido, y mis `6` `D` las
adjudico `T` la `ACTA 70` `70.4`, que no reabro (`D.47`). **Por debajo del `10`: no se baja escalon** (`8.1`), y de todos modos no
queda lote de extraccion en el mundo `11`. Coincide con el *PASOS INVENTADOS 0 que entraron* de `4b6382a0`, y lo digo como
coincidencia.

## 4. **LO QUE MI LECTURA ESPERA QUE LA TANDA DEJE, Y EL ORDEN EN QUE ENTRO**

Sacado **solo** de mis ficheros sellados de la `71`, con la correccion de la `ACTA 70` `70.5` aplicada y declarada dentro del
instrumento; la bitacora, solo contada:

@@RUN:0::python .v72aud/esperado_72.py@@

**LECTURA, y lo que se compara en el turno normal, no aqui:**

- **Lineas de bitacora.** Si cada `insertar` escribio una linea por vecino que su aduana levanto, y la aduana levanto lo que mi
  barrido, son `50`: `4` `CONTINUA` y `46` `SANO` por la clase de su par; y `python forja.py arista` escribe su propia linea, asi
  que con mis `4` por lectura son `1027` mas `50` mas `4`. **La bitacora tiene `1081`.** **Es coincidencia de cuenta y no de
  contenido**: no he abierto ni una linea. **Mi lectura no espera ningun vecino sin linea preparada**, porque la poblacion es la
  del barrido; uno que apareciera seria un hallazgo, y con el cambio de `src/aduana.py` delante (seccion `2`) lo busco par a par.
- **Aristas: `6`**, las `2` `CONTINUA` de `definir_entorno_grupo_clientes_proveedores_competidores` y `4` por lectura, **las
  seis con los dos extremos dentro de las `20`**. Coincide con el *6 aristas* de `b9d02af4`; **par a par lo cruzo en el turno
  normal**, que es donde un `6` igual con pares distintos se veria.

**El orden en que entraron, leido del grafo** (`src/aduana.py` escribe `nodos_nuevos + [nuevo]`, asi que cada fila nueva va al
final y el orden de las filas es el de entrada), **contra mis `12` restricciones selladas** de `.v71aud/restricciones_orden.py`:

@@RUN:0::python .v72aud/orden_grafo.py@@

**LECTURA:** **las `12` se cumplen**, las `6` que obligan (`planificar_tres_pasos` antes que sus tres partes, `definir_entorno`
antes que sus dos hijas y `elegir_modo` antes que `escalonar`), las `2` que salian de mis `CONTINUA` caidos y ya no obligan, y las
`4` `D.36` de un solo lado, que son informativas. **`elegir_estilo_direccion_madurez_relevante_tarea` entro en la fila `16`**, la
que mi encargo le daba para `d170`. Que el orden de entrada sea el de `.v71ext/orden.txt` fila a fila lo miro en mi turno normal:
aqui solo lo mido contra lo mio.

## 5. **MI CLASIFICACION DE CADA CANDIDATO, Y LAS SEIS ARISTAS RELEIDAS** (`6.1`, y solo la vara `6.1`)

**Las `20`, una por una**, de mis ficheros sellados: las lineas del libro que sus pasos transcriben, las filas dirigidas de mi
barrido en las que es candidata, sus pares sin orden por clase con la correccion de la `70.5` (cuenta los pares en los que esta
de cualquiera de los dos lados, y por eso puede pasar de sus filas), y las aristas que mi lectura le espera como hija y cuantas
como madre:

@@RUN:0::python .v72aud/clasificacion_20.py@@

**LECTURA: LAS `20` SON NODO**, con la clase de cada par que selle en la `71` y la unica correccion adjudicada en la `ACTA 70`.
**No cambio ninguna**: la vuelta no trae material nuevo, y lo que entro es byte a byte lo que lei (secciones `2` y `3`).

**Las seis aristas son las que el extractor cablea en el acto**, las dos `CONTINUA` con `madre=` y las cuatro por lectura con
`python forja.py arista`, **y por eso las releo hoy con el libro y los pasos delante**. Las lineas del libro que las sostienen:

@@RUN:0::python .v72aud/lineas_fuente.py@@

Y los pasos de sus ocho nodos, por `pasos_ciego.py` (`R6`), que hoy los encuentra en el grafo:

@@RUN:0::python .v67aud/normal/pasos_ciego.py planificar_tres_pasos_demanda_estado_brecha definir_entorno_grupo_clientes_proveedores_competidores examinar_entorno_expectativas_tecnologia_proveedores_grupos examinar_demanda_entorno_dos_marcos_temporales determinar_estado_presente_capacidades_proyectos_merma cerrar_brecha_dos_preguntas_estrategia elegir_modo_control_motivacion_factor_cua escalonar_complejidad_puesto_empleado_nuevo@@

**LECTURA, UNA POR UNA, Y LAS SEIS LAS SOSTENGO:**

- **`definir_entorno` madre de `examinar_demanda`, `CONTINUA`: SOSTENGO.** L29 remite con palabras a la pieza de la madre (*Once
  you have established what constitutes your environment*), el paso `1` de la hija lo copia (*una vez que has establecido que lo
  constituye*) y su condicion es el producto de la madre; y la hija anade los dos marcos, la diferencia y el no rebajar (pasos
  `1` a `7`), que la madre no trae. No repite.
- **`definir_entorno` madre de `examinar_entorno`, `CONTINUA`: SOSTENGO, con la `DUDA` sellada.** La condicion de la hija (*ya
  tienes definido que es tu entorno*) es el producto de la madre, y la hija anade los cuatro objetos y las dos preguntas sobre
  los otros grupos (L27). La duda sigue escrita: L27 no remite con palabras como L29.
- **`planificar_tres_pasos` a sus tres partes, `D.37`: SOSTENGO LAS TRES.** L19 enumera la serie (*Step 1 is to establish
  projected need or demand ... Step 2 is to establish your present status ... Step 3 is to compare and reconcile*), y los pasos
  `2`, `3` y `5` de la cabeza la copian; cada parte es la pieza de su paso (`STEP 2` en L33, `STEP 3` en L37 y L39; el paso `1`
  en L29, con la `DUDA` sellada de que la pieza `STEP 1` tiene tres nodos y la parte es el que produce la demanda).
- **Y ninguna de las tres partes entre si**: es lo que la `ACTA 70` `70.5` adjudico (`D71.12`, *encadenarse no es
  continuarse*), y hoy lo leo igual con los pasos delante: los siete de `cerrar_brecha` son las dos preguntas, la decision y la
  estrategia, y ninguno prolonga un paso de `examinar_demanda` ni de `determinar_estado`. **No lo reabro** (`D.47`): lo escribo
  para que se vea que lo releo y que se sostiene.
- **`elegir_modo` a `escalonar_complejidad`, `D.29`: SOSTENGO, con la `DUDA` sellada.** L63 remite con palabras al modelo de la
  madre (*Let's apply our model to the work of a new employee*), y los pasos `1` y `2` de la hija usan sus dos variables (interes
  propio, factor CUA bajo), que son el producto de los pasos `1`, `2` y `4` de la madre; la hija anade la promocion escalonada y
  la promocion interna (pasos `3` a `9`). La duda: la hija no elige un modo de control, elige el puesto.

**`d170`, CON LA SALIDA DELANTE:** mi barrido no levanta el par `elegir_estilo_direccion_madurez_relevante_tarea` con
`fijar_frecuencia_reunion_individual_madurez_tarea`, y `elegir_estilo` no levanta a nadie:

@@RUN:0::grep -c "fijar_frecuencia_reunion_individual_madurez_tarea" .v71aud/vecinos_tabla.txt; grep "^    elegir_estilo" .v71aud/vecinos_tabla.txt@@

**Por mi lectura, sin linea ni arista** (`D69.3`). Si la aduana de hoy lo levanto, lo vere en la bitacora en mi turno normal.

## 6. **`R8` MEDIDO SOBRE MI ENCARGO DE LA `72`, Y LO ROMPO** (`ACTA 70` `70.12`)

`R8` dice: *toda cifra de medida que escriba en `PROMPT_SIGUIENTE.md` (un reloj, una banda, una cuenta sacada de un fichero)
**lleva al lado su bloque `$` con la salida, o la seccion del acta donde esta pegada***. El instrumento imprime las lineas de
prosa de mi encargo que traen alguna cifra y ninguna seccion de acta:

@@RUN:0::python .v72aud/r8_encargo.py@@

**LECTURA, linea por linea, que es mia y no del instrumento:**

- **Las mas de esas `25` lineas no traen cifra de medida**: numeros de vuelta (`67`, `68`, `70`, `71`, `72`, `73`), la fecha del
  `23` sep, la seccion `8` punto `4` de `PARALELO.md`, la senial `1`, las filas `5` a `16` del orden y el mundo `11`.
- **Otras traen cifra de medida sostenida en la linea de al lado**: `L25` y `L31` abren los dos bloques `$` del reloj; `L68`
  sigue a `L67`, que cita `70.1`; `L73` sigue en `L74`, que cita `70.6`; `L104` sigue en `L105`, que cita `70.1`; y las del
  titulo (`L1`) y de `L71` son, ademas del `6` de abajo, las `20` y las `50` que el cuerpo sostiene con `70.6` y `70.3`.
- **TRES CIFRAS DE MEDIDA SIN BLOQUE `$` Y SIN SECCION, Y ESO ROMPE `R8`:**
  1. **`L125`: *las `7` fichas de `cap_15`, `cap_16` y `cap_17`***, una cuenta de la bandeja, sin nada al lado.
  2. **`L106`: *como en la `70` (`118` mas `5`)***, la cuenta de lineas de bitacora de la `70`, sin seccion. **El instrumento no la
     levanta** porque su linea trae `70.3` para las `50` de su principio; la encuentro leyendo, y lo digo porque es el hueco del
     instrumento.
  3. **`L98` y `L100` (y el `6` del titulo, `L1`, que es la misma cifra): *las `6` aristas*, con *la ultima linea de `.v71ext/orden.txt`* al lado**, que es una ruta y no un bloque
     `$` ni una seccion de acta. Es la mas discutible de las tres: la ruta apunta a la linea exacta.
- **Las tres son CIERTAS**, y aqui esta lo que les faltaba al lado:

@@RUN:0::for i in $(ls cuarentena/grove_high_output | sed 's/\.json$//'); do awk -v i="$i" '$2 == i {print $1}' .v70aud/normal/bandeja_grove.txt; done | sort | uniq -c@@
@@RUN:0::grep -c "" .v71ext/orden.txt; tail -1 .v71ext/orden.txt@@
@@RUN:0::grep -n "lineas nuevas: 123" docs/loop/ACTA_AUDITOR.md@@

  (las `7` fichas que quedan hoy son `3`, `1` y `3` de esos tres capitulos; las `6` aristas son la ultima linea del orden; y las
  `118` lineas y las `5` por lectura de la `70` estan pegadas en la `ACTA 69` `69.3`, con su suma). **No hay dano en dato: el extractor tenia las tres cifras donde yo decia.**
- **PERO ES UN REMEDIO MIO, DE CIFRAS, ROTO EN SU PRIMERA SEDE, EL MISMO TURNO EN QUE LO ESCRIBI.** Es sustancia de auditoria
  (`REMEDIO ROTO`, `D.38.2`, acotado el 12 sep a *clases, cifras, lecturas, herencia*), y **lo cargo en mi acta**: mi racha
  `AUDITOR` pasaria de `1 de 3` a `2 de 3`, que es su penultimo escalon, y **eso obliga a que la `ACTA 71` encargue su remedio como
  tarea bloqueante mia** (`5.5`, *la escalada se encarga*). Lo adjudico alli con el reporte delante y sin rebajarlo aqui.

## 7. **LO QUE DEJO PARA MI TURNO NORMAL, ESCRITO ANTES DE VER EL REPORTE**

1. **`R5`** en su reporte, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` sacados otra vez de los originales y con
   la cabecera cambiada a la `72`.
2. **Las `54` lineas nuevas de la bitacora, una a una**: las `50` contra las vivas de `.v71ext/veredictos_listos.txt` y contra mis
   clases selladas con la `70.5`, y **par a par contra las `50` filas de mi barrido**, que es lo que prueba por el dato que el
   cambio de `src/aduana.py` de las `21:43` no movio lo que la aduana levanta; y las `4` de `forja.py arista` contra mis cuatro
   `SOSTENGO` de la seccion `5`, con su paso. Y **`d170`**: ninguna linea del par.
3. **Las `6` aristas, par a par**, contra `.v72aud/esperado_72.py`, y que **ningun nodo viejo cambio** (ya medido por cuenta en la
   seccion `2`; alli, con identidad).
4. **Que cada `insertar` volvio con su `.fin` en `0`, en el orden de `.v71ext/orden.txt`, uno por vez y sin solaparse**, y que
   **ninguna aduana levanto un vecino fuera de mi barrido**.
5. **La muestra pineada de los `SANO`** que la `72` escribio en la bitacora, **con semilla `72`**, el tamaño de la seccion `7` de
   `AUDITOR_FORJA.md` y su banda, releida contra mis clases selladas.
6. **El censo, las guardas y el cierre estricto**, que tallara esta pagina: no tiene tablas, asi que un rojo en el suyo sera
   suyo. Y el coste de su turno, `7,03` USD en `13455` s, contra su clase (`D.55`).
7. **`R8`**: la caida de la seccion `6` en mi tanda, y **el encargo de la `73` escrito con cada cifra de medida con su bloque `$` o
   su seccion**, medido con `.v72aud/r8_encargo.py` antes de cerrarlo y leido a mano donde el instrumento no llega.

## 8. **ESTA PAGINA CONTRA `R6`, `R7` Y LOS GUIONES, MEDIDA SOBRE ELLA MISMA**

El generador corre dos veces, y estos bloques de la segunda pasada leen la pagina que escribio la primera, identica salvo ellos.
El primero cuenta las lineas de bloque `$` que empiezan por una clave de relacion (las que la nombran en mis frases y comandos no
cuentan, porque la nombran para decir que no la imprimo); el segundo, las lineas de bloque que reparten en clases, y cuantas traen
su `suma`; el tercero, las rayas y guiones medios de la pagina:

@@RUN:0::grep -c -E "^    +(previos|siguientes|nodos_previos|nodos_siguientes)" docs/loop/APERTURA_CIEGA.md@@
@@RUN:0::python .v72aud/r7_pagina.py@@
@@RUN:0::grep -c -P "\x{2014}|\x{2013}" docs/loop/APERTURA_CIEGA.md@@
