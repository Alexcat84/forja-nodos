
# ACTA 77. VUELTA 78, lote 5 (`marquet_turn_the_ship`), **CLASE INSERCION, VUELTA DE PREPARACION**: **LAS `20` FICHAS DE MARQUET QUEDAN LISTAS Y NINGUNA ENTRO. SU FIDELIDAD, SU BARRIDO, SUS `52` LINEAS, SU ARISTA POR LECTURA Y SU ORDEN SON, PAR A PAR Y PASO A PASO, LOS DE MI LECTURA SELLADA: `105` PASOS `T` EN LOS DOS LADOS, SUS `3` PUENTE SON LOS `3` QUE YO LEI `P` EN EL TEXTO VIEJO Y ESTAN CORREGIDOS, `52` FILAS DIRIGIDAS IGUALES EN SEDE Y SENIAL, `52` `SANO` QUE SON MIS CLASES, LA MISMA ARISTA `observar` A `seguir` CON SU DIRECCION, Y MIS SIETE RESTRICCIONES DE ORDEN CUMPLIDAS. SUS CATORCE DISCUTIBLES SE SOSTIENEN Y MIS DOS DUDAS SE CIERRAN `T`. FUERA DEL MARCADO, DOS FRONTERAS DECLARADAS: LA DE GROVE SE SOSTIENE Y SE AGENDA (`d183`), LA DE ZHUO VA A RELECTURA CONJUNTA. CERO CAIDAS SUYAS Y MIAS: LAS CINCO RACHAS EN CERO. LA `79` ES DE SANEAMIENTO POR CADENCIA, Y MARQUET ENTRA EN LA `80`**

*Auditor `claude-opus-5-5`, 26 sep 2026, turno normal de la vuelta que el arnes numera `2` en la corrida que arranco el 26 a las
`09:27`. Linea **serial**, rama `extraccion-mundo-11`, hash auditado `91bf4863` (cierre del extractor, mas `463248f5` con la salida
del hook, sin trabajo nuevo), arbol en `e92b1f85` con mi apertura sellada. Modo austero (`D.47`). Toda mi evidencia de este turno
esta en `.v78aud/normal/`, y la de mi fase ciega en `.v78aud/`.*

## 77.0. **HUECO DE ACTA Y HERENCIA** (`1.0`, `D.40`)

**NO HAY HUECO.** La `ACTA 76` cubre la vuelta `77`; esta cubre la `78` entera: el turno del extractor (de `e9d03092` a `463248f5`,
`13:29` a `15:02` del 26) y mi fase ciega, sellada en `e92b1f85`, que solo toca sus dos ficheros. Lo que la vuelta movio desde mi
acta (`90457524`), con quien lo escribio:

@@RUN:0::git log --format="%h %an %cI %s" 90457524..e92b1f85 | cut -c1-140@@
@@RUN:0::git diff --name-status 90457524 463248f5 | grep -v "\.v78ext/" | awk '{print $1, $NF}' | sed "s|/[^/]*\.json$|/*.json|" | sort | uniq -c@@
@@RUN:0::git diff --name-status 90457524 463248f5 -- .v78ext | awk '{print $1}' | sort | uniq -c; git diff --name-only 463248f5 e92b1f85@@
@@RUN:0::git log --format="%h %an" 90457524..e92b1f85 -- src tests scripts forja.py config esquema fuentes dataset bitacora censos | wc -l; git diff 90457524 463248f5 -- docs/loop/DEUDA.jsonl | grep -c "^[-+]{"@@
@@RUN:0::git diff --stat=200 90457524 463248f5 -- cuarentena/; git diff --stat 90457524 e9d03092 -- docs/loop/TABLERO.jsonl | tail -1; git diff --stat e9d03092 e92b1f85 -- docs/loop/TABLERO.jsonl | wc -l@@

**LECTURA:** **la vuelta movio lo que una preparacion mueve y nada mas**: las `2` fichas corregidas de la bandeja de Marquet, su
carpeta `.v78ext/` (todo ficheros nuevos) y los de `docs/loop/`; **ni el grafo, ni la bitacora, ni los censos, ni `src/`, `tests/`,
`scripts/` o `config/`, y ninguna linea de `DEUDA.jsonl`**. La linea de `TABLERO.jsonl` la movio solo `e9d03092`, que es *lo pendiente
del arnes antes de tocar nada*, y despues nadie.

**HEREDADO 1, `R5` del extractor: CUMPLIDO.** Con mis copias sacadas con `sed` de los originales `.v64ext/pegado64.py` y
`.v64aud/normal/bloques_mudos.py`, no de las suyas, con la cabecera cambiada a la `78`:

@@RUN:0::diff --strip-trailing-cr .v64ext/pegado64.py .v78aud/normal/pegado78_aud.py | grep -c "^>"; diff --strip-trailing-cr .v64aud/normal/bloques_mudos.py .v78aud/normal/bloques_mudos78_aud.py | grep -c "^>"@@
@@RUN:0::python .v78aud/normal/pegado78_aud.py; python .v78aud/normal/bloques_mudos78_aud.py@@

**Es lo que su `78.5.g` publica sobre el reporte entero, al digito** (`27` comandos en `17` bloques, `0` y `0`). **HEREDADO 2, `R6`, y
HEREDADO 3, `R7`, mios: CUMPLIDOS** en la fase ciega (`APERTURA_CIEGA.md` `0` y `10`) **y `R7` en esta acta**: cada instrumento mio de
este turno que reparte un total en clases imprime su `suma`. **HEREDADO 4, `R8`, mio: CUMPLIDO en el encargo de la `78`**
(`APERTURA_CIEGA.md` `8`) **y medido sobre el de la `79`** en `77.12`. **HEREDADO 5, `R9` del extractor: CUMPLIDO**: su `grep` de clausulas
va pegado en `78.2.1`, antes de la cuenta de PUENTE de `78.2.3`, con su lectura paso a paso de los `18` que casan; y su patron contra el
mio, en `77.3`. **HEREDADO 6, `R10`, mio: CUMPLIDO en el encargo de la `78`** (`APERTURA_CIEGA.md` `0`) **y en esta acta** (`77.13`).

## 77.1. **LO QUE VERIFICO, CON MIS PROPIOS COMANDOS** (`1.1`)

Corridos en serie por `.v78aud/normal/guardas.sh`, cada uno con su `rc`:

@@RUN:0::cat .v78aud/normal/gate.txt .v78aud/normal/guiones.txt .v78aud/normal/resolutor.txt@@
@@RUN:0::grep 'total:' .v78aud/normal/suite.txt; tail -1 .v78aud/normal/suite.txt; cat .v78aud/normal/suite_hora.txt@@
@@RUN:0::wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl@@
@@RUN:0::for d in cuarentena/marquet_turn_the_ship cuarentena/_insertados/marquet_turn_the_ship cuarentena/gerber_emyth cuarentena/_insertados/gerber_emyth; do echo "$d $(find $d -maxdepth 1 -name "*.json" 2>/dev/null | wc -l)"; done; echo "procesos $(ls -A procesos/ | wc -l)"@@
@@RUN:0::python .v70aud/poblacion.py@@

**LECTURA:** **el censo de su `78.0` y su `78.5.a` al digito** (`459`, `1172`, `1`; bandeja de Marquet `20`, insertados `0`; poblacion
`479`, `459` mas `20`) **y el de mi apertura sellada** (`APERTURA_CIEGA.md` `2`). La suite cuenta `382`, lo mismo que su `78.5.f` y que
mi `ACTA 76` `76.1`.

**EL CIERRE ESTRICTO, CORRIDO POR MI**, en serie despues de la suite, con `procesos/` vacio al terminar:

@@RUN:0::grep -nE '^(CIERRE|CENSO|TALLADO|TABLA DE CIERRE)|DIFIEREN|CAEN  ' .v78aud/normal/cerrar_reporte.txt; tail -1 .v78aud/normal/cerrar_reporte.txt; cat .v78aud/normal/cerrar_hora.txt .v78aud/normal/procesos_al_acabar.txt@@

**VERDE, `rc=0`.** Cuenta `1090` rutas contra `1086` de su corrida de `78.5.g` y `1087` de su hook del cierre (`.v78ext/hook_t5.txt`):
**no descompongo la diferencia**, el arbol no es el mismo (despues entraron la salida de su hook y mi apertura), y ninguna cae.

**LO QUE REPRODUZCO DE SU TRAMO**, corriendo sus nueve instrumentos contra sus salidas guardadas con `diff`, en el arbol de hoy, cuyas
fichas son byte a byte las de su cierre (`77.4`):

@@RUN:0::grep -v '^\$ ' .v78aud/normal/reproduce.txt@@

(Los comandos de cada linea estan en `.v78aud/normal/reproduce.cmds`. `validar.py` recibe los ids por argumento; su reporte no dice
como lo llamo, y con los `20` de su propia salida da su salida.)

## 77.2. **EL REPORTE, AFIRMACION POR AFIRMACION** (`5.2`)

| afirmacion del reporte | sale | sede | especie |
|---|---|---|---|
| cabecera y las dos tablas de tareas: `110` pasos, `3` PUENTE corregidos, `cap_04` releido; `20` de `20`, poblacion `479`, `52` pares; `52` lineas `SANO`, `1` arista, `D.36` en cero; el censo al abrir y al cerrar | **cierta, celda a celda** (`77.1`, `77.3`, `77.4`) | TABLA y CABECERA | |
| `78.0`: `e9d0309`, gate con `459`, el censo, `LIBRE` con `50` deudas, poblacion `479`, `20` fichas y `110` pasos | **cierta** (`77.0`, `77.1`) | bloque | |
| `78.1` y `78.D`: los registros de la `ACTA 76`; `D78.1` y `D78.2` | **cierta** (`77.5`) | tablas | |
| `78.D bis` y `78.D ter`: `D78.3` a `D78.14`, marcados al escribir cada fila | **cierta como marca**: `D78.3` a `D78.10` son las `11` filas marcadas `DISCUTIBLE` de su fidelidad (`77.3`), y `D78.11` a `D78.14` estan marcados en su fichero de aristas (`77.5`) | tablas | |
| `78.2`: ningun paso cita un capitulo que no sea el de su ficha | **cierta** (`77.3`) | prosa | |
| `78.2.1`: `110` citas en su linea; `R9`, `107` pasos `T` y `18` que casan, cada uno con su tramo | **cierta** (`citas.sh` y `r9.py` reproducidos, `77.1`; los dos patrones, `77.3`) | bloques y prosa | |
| `78.2.2`: la tabla de las `3` correcciones, `2` fichas en el `diff`, `20` validas | **cierta en la tabla y en el `diff`** (`77.0`, `77.1`, `77.3`); las cifras que cada correccion escribe en su `resumen_teorico` (`5`, `3` y `2`; `8`, `7` y `1`) son las de su fichero de filas | tabla y bloques | |
| `78.2.3` y `78.5.b`: trece filas, peor `cap_04` con `2` de `5`, el `40,0`, releido entero; `cap_03` `1` de `53` | **cierta** (`contar_fidelidad.py` reproducido, `77.1`; mi cuenta, `77.3`) | bloque y tabla | |
| `78.2.4`: la fila de `cap_03` para `d150`, sin pagar | **cierta** (`77.3`) | bloque | |
| `78.3`: `20` de `20` con `rc=0`, de `13:44:27` a `14:43:48`, de `398` a `1225` s, poblacion `479`; `16` con vecinos; `52` filas, `42` de bandeja y `10` del grafo; los del grafo por veces; `51` y `1` por senial; `19` por encima de `0,4`, la mayor `0,464` | **cierta, cifra a cifra** (`77.4`, `cifras_reporte.py`; el reloj, de su log) | bloques y prosa | |
| `78.4.1`: `52` lineas para `52` vecinos, todas `SANO` | **cierta** (`77.4`) | bloque | |
| `78.4.2`: `1` `SOSTENGO` y `21` `NO SOSTENGO`, `5` con madre en el grafo, `2` de ellas frontera | **cierta como cuenta de su fichero** (`77.4`); la adjudicacion, en `77.5` | prosa | |
| `78.4.3`: las tres comprobaciones en cero; `1` arista esperada; los dos movimientos que `D.36` obliga | **cierta** (`orden.py` reproducido, `77.1`; contra mis restricciones, `77.4`) | bloque y prosa | |
| `78.5.a` a `78.5.g`: censo, huellas `18` iguales y `2` distintas, `D.61` sin abiertos, `R5`, guardas, cierre estricto | **cierta** (`77.0`, `77.1`, `77.4`) | bloques y tabla | |

**NINGUNA CAIDA DE `REPORTE`.** Lo que mire para ver si alguna celda de prosa escondia una cifra de teclado: las dos tablas de tareas
y la de pasos inventados, celda a celda contra su instrumento; los *diecinueve pares por encima de `0,4`* y los *`16` de `20`* de su
`78.3`, contados sobre mi barrido sellado; y las cifras que sus dos correcciones escriben dentro de las fichas. **La ultima columna de
su tabla de `78.5.b`** no sale de ningun instrumento y lo dice su propia marca `parcial`; es la cuenta sobre el texto de hoy, y la mia
la da igual (`77.3`).

## 77.3. **LA FIDELIDAD, `R9` CRUZADO, `PASOS INVENTADOS POR CAPITULO` Y `d150`** (`D.30`, `D.58`, `8`, `8.2`, `8.3`)

**MI LECTURA SELLADA CONTRA LA SUYA, PASO A PASO.** La mia marca el texto de HOY, despues de sus correcciones (`APERTURA_CIEGA.md`
`3`); la suya, el texto de AL ABRIR:

@@RUN:0::python .v78aud/normal/fidelidad_cruce.py@@

**LECTURA:**

- **En `105` pasos los dos leemos `T`.** **Sus `3` `P` son los `3` que corrigio**, y su texto de hoy lo leo `T` en los tres: **las
  correcciones se sostienen.** **Sobre sus textos viejos** (`APERTURA_CIEGA.md` `3`, leidos despues de contar) **mi lectura da `P` a
  los tres**, con la misma razon que la suya. **Ningun `T` suyo lo leo `P`: no hay puente que se le escapara.**
- **Mis dos `D` son su `D78.6`**, la misma figura en los dos pasos, y se cierran `T` en `77.5`.
- **La unica linea distinta es de cita, no de marca**: `contar_firmas_cadena_tramite_parado` paso `10` lo sostienen `L41` y `L43` en las
  dos filas; yo pongo delante la `43` y el la `41`.
- **Todos los pasos de cada ficha citan el capitulo de su ficha** en mi fichero y en el suyo (`78.2`):

@@RUN:0::awk -F'\t' 'NR>1{print $1, $4}' .v78aud/fidelidad.tsv | sort -u | awk '{print $1}' | uniq -c | awk '$1>1' | wc -l; grep -v "^#" .v78ext/fidelidad.tsv | awk -F'|' '{print $4}' | grep -c ":"@@

**`R9`, SU PATRON Y EL MIO SOBRE LOS `110` PASOS DE HOY**, leidos de sus ficheros y no copiados (el suyo es el de la `76` sin tocar,
como dice su cabecera):

@@RUN:0::diff <(sed -n '/PAT = re.compile(/,/re.I)/p' .v76ext/r9.py) <(sed -n '/PAT = re.compile(/,/re.I)/p' .v78ext/r9.py) && echo "su patron de la 78: IDENTICO al de la 76"@@
@@RUN:0::python .v78aud/normal/r9_cruce.py@@

**LECTURA:** **el mio casa un solo paso que el suyo no casa**, `reforzar_principios_guia_lenguaje_prueba_conocimiento` paso `2`, por
*prueba*, que ahi es *poner a prueba* y no la prueba del libro: el paso manda preguntar a las tres primeras personas que veas, que es
`cap_14` `L99` letra a letra, y *si son reales* es el *make them real* de `L89`. **`T`, y lo lei `T` a ciegas.** **`R9` no levanta
puente.**

**`PASOS INVENTADOS POR CAPITULO`**, contado por mi desde los dos ficheros, con el titulo de cada capitulo leido de su fichero:

@@RUN:0::python .v78aud/normal/pasos_inventados.py@@

| capitulo | que es | candidatos | pasos | PUENTE sobre el texto de al abrir | por ciento | PUENTE que entrara |
|---|---|---:|---:|---:|---:|---:|
| `cap_01` | *Introduction* | `1` | `6` | `0` | `0,00` | `0` |
| `cap_02` | *Change of Course* | `2` | `10` | `0` | `0,00` | `0` |
| `cap_03` | *Call to Action* | `6` | `53` | `1` | `1,89` | `0` |
| `cap_04` | *Whatever They Tell Me to Do!* | `1` | `5` | `2` | `40,00` | `0` |
| `cap_06` | *Change, in a Word* | `2` | `8` | `0` | `0,00` | `0` |
| `cap_07` | *I Intend To* | `1` | `3` | `0` | `0,00` | `0` |
| `cap_08` | *Up Scope!* | `1` | `5` | `0` | `0,00` | `0` |
| `cap_09` | *Who's Responsible?* | `1` | `2` | `0` | `0,00` | `0` |
| `cap_10` | *We Have a Problem* | `1` | `3` | `0` | `0,00` | `0` |
| `cap_11` | *Mistakes Just Happen!* | `1` | `3` | `0` | `0,00` | `0` |
| `cap_12` | *We Learn* | `1` | `8` | `0` | `0,00` | `0` |
| `cap_13` | *All Present and Accounted For* | `1` | `2` | `0` | `0,00` | `0` |
| `cap_14` | *Leadership at Every Level* | `1` | `2` | `0` | `0,00` | `0` |
| **el lote** | | **`20`** | **`110`** | **`3`** | **`2,73`** | **`0`** |

**LECTURA:** **el peor capitulo es `cap_04`, *Whatever They Tell Me to Do!*, con `2` de `5`**, y es el unico por encima del `10`: **se
releyo entero antes de seguir** (`D.58`), por el (`78.2.3`) y por mi (lei enteros los trece, `APERTURA_CIEGA.md` `3`). **El por ciento lo
hace el denominador**: una ficha de cinco pasos con una clausula puesta en dos de ellos. Es la cifra de una mineria de frente en regimen
ligero, con muestra y no con lectura entera, y **es la regla funcionando** (`8.4`): los `3` se cazaron y se corrigieron antes de entrar.
**No dimensiona nada**: no queda lote de extraccion en el mundo `11` (`PARALELO.md` `8` punto `3`). Los titulos van sin sus comillas
tipograficas y sin los puntos suspensivos de `cap_07`; la ultima columna es la columna *PUENTE en el texto de hoy* de mi instrumento.

**`d150`, FIRMADA EN SU SUSTANCIA.** Su texto pedia la fila de `cap_03` que el frente publico en `0,00` y la `ACTA M2` recontro: **su
fila de `78.2.4` es `1` PUENTE de `53` sobre el texto de la mineria, `1,89` por ciento, y `0` despues de la correccion**, y la mia, sobre
el texto de hoy, `0` de `53` con las dos `D` cerradas `T` (arriba). **FIRMO la fila.** Lo que queda de su letra (las tareas `2` y `3`
del reporte archivado de la vuelta `1` del frente) **no se reescribe**: la relectura entera de la `78` lo sustituye. Se paga en la
`79` (su encargo, TAREA `3`), con `.vm01/` medido antes:

@@RUN:0::find .vm01 -type f | wc -l; git status --short -- .vm01 | wc -l@@

## 77.4. **EL BARRIDO, LAS CLASES, LAS ARISTAS, EL ORDEN Y LAS HUELLAS, PAR A PAR** (`APERTURA_CIEGA.md` `4` a `7`)

**Su barrido contra el mio sellado, fila dirigida a fila dirigida, y sus lineas contra mis clases selladas, par a par:**

@@RUN:0::python .v78aud/normal/barrido_cruce.py@@

**Las cifras de prosa de su `78.3`, contadas sobre mi barrido:**

@@RUN:0::python .v78aud/normal/cifras_reporte.py@@

**Sus aristas por lectura contra las mias selladas, con direccion:**

@@RUN:0::python .v78aud/normal/aristas_cruce.py@@

**Su orden contra mis siete restricciones selladas** (`APERTURA_CIEGA.md` `7`):

@@RUN:0::python .v78aud/normal/orden_contra_restricciones.py@@

**Y las huellas**: las de mi fase ciega, tomadas antes de barrer, y los blobs que su `78.5.c` sella, contra las fichas de hoy:

@@RUN:0::sha1sum -c --quiet .v78aud/huellas_al_barrer.txt && echo "las 20 fichas y el grafo de hoy: mismas huellas que al barrer en mi fase ciega"@@
@@RUN:0::for f in $(awk '$1 ~ /^[0-9]+$/ {print $2}' .v78ext/pasos_y_huellas.txt); do h=$(git hash-object cuarentena/marquet_turn_the_ship/$f.json | cut -c1-10); grep -q "$f .* $h " .v78ext/pasos_y_huellas.txt && echo igual || echo "DISTINTA $f"; done | sort | uniq -c@@

**LECTURA:**

- **Las `52` filas dirigidas son las mias**, en sede, en sus tres seniales al milesimo y en quien las levanta, y la poblacion es la
  misma en las `20` (`459` mas `20`). **Sus `52` lineas son esas `52` filas y todas son `SANO`, que es mi clase en los `34` pares.**
- **Su unica `SOSTENGO` es la mia, con la misma direccion**: `observar_reunion_rutinaria_senales_plantilla` madre de
  `seguir_frustrado_preguntar_implantacion_ideas`, por el paso `7` de la madre y `cap_03` `L21` y `L23`. **Las demas filas, suyas o mias,
  descartan**: en `2` pares descartamos los dos; `3` de mis descartes no los miro y `19` de los suyos no los mire yo, **y ninguno da una
  arista**. La que yo marque con duda y el no miro, `aplicar_ejercicio` a `identificar_temas_formacion`, la releo en `77.5`.
- **Su orden cumple mis siete restricciones**, la que obliga (`observar` antes que `seguir`) y las seis de `D.36` de un solo lado,
  **incluidas las dos que el orden del libro violaba**: `recorrer` baja detras de `inspeccionar` y `reforzar` sube delante de `declarar`,
  que son los dos movimientos que su `78.4.3` declara.
- **Las `20` fichas de hoy son las que barri yo y las que el sello**: ninguna cambio despues de su barrido (`d031`).

## 77.5. **LA RELECTURA** (`1.2`, `5.1`, `6.1`, `7`)

**SUS CATORCE DISCUTIBLES, POR NUMERO** (`D.47`), con los pasos y las lineas del libro leidos otra vez en este turno:

| | su marca | adjudico |
|---|---|---|
| `D78.1` y `D78.2` | el barrido una vez, con las `20`, despues de la ultima correccion; cinco a la vez con el presupuesto de `6` plazas | **SE SOSTIENEN**: el commit de las correcciones es de las `13:42:08` (`77.0`) y el barrido arranco a las `13:44:27` (su log); `20` de `20` en `rc=0`, y sus fichas barridas son las de hoy (`77.4`) |
| `D78.3` | `auditar_formacion` paso `8`, *familias* por el *no wives* de `L55`, va `T` | **SE SOSTIENE**: el paso nombra la categoria y su ejemplo es la esposa del libro; no anade ningun control que `L55` no haga. Lo lei `T` a ciegas |
| `D78.4` | `recorrer` paso `6`, *como dato y no como examen*, va `T` | **SE SOSTIENE**: *It wasn't supposed to be a test* y *I figured this was what Commodore Kenny was talking about*, los dos en `L15` |
| `D78.5` | `seguir_frustrado` paso `2`, *sin pregunta y sin acusacion*, va `P` | **SE SOSTIENE**: son dos prohibiciones que `L25` no da, la figura de `D76.8` con su *No contrates*. Lo lei `P` en el texto viejo (`77.3`) |
| `D78.6` | `seguir_frustrado` paso `3` y `auditar_formacion` paso `6`, *hasta el final* y *entera*, van `T` | **SE SOSTIENE, Y CIERRA MIS DOS DUDAS `T`**: son verbos de marco sobre lo que el libro registra, el *As I listened* de `L27` y la respuesta de dos mitades de `L57`, cuya segunda mitad es el hallazgo del libro (*With leader-follower it didn't matter*); la figura de `D76.8` con su *Comprueba*, que la `ACTA 75` `75.5` sostuvo |
| `D78.7` | `informar_cierre`: paso `1` `T`; pasos `2` y `4` `P` | **SE SOSTIENE**: la prohibicion del `1` la da el libro, que pone la pregunta de `L31` como el problema y la sustituye en `L35` (*it should go more like this*); el `2` y el `4` anaden *con signo positivo* y *sin disculpa vacia*, que `L35` no dice. Lo lei asi a ciegas |
| `D78.8` a `D78.10` | `asignar_responsable` `2`, `eliminar_seguimiento` `2` y `declarar_intencion` `1` van `T` | **SE SOSTIENEN**: *more important than* de `cap_06` `L127`; *He shouldn't* de `cap_09` `L57` y *without the overhead* de `L73`; y las *disempowered phrases* de `cap_07` `L73`, que el capitulo sustituye por las de intencion. Los lei `T` a ciegas |
| `D78.11` y `D78.12` | `ceder_control` sin arista a los nueve mecanismos | **SE SOSTIENEN**: es mi descarte `D.37` sellado (`APERTURA_CIEGA.md` `6`), con la misma razon (`D68.7`) |
| `D78.13` | `observar` madre de `seguir` por `D.29`; `recorrer` sin arista a `contar_firmas`, `inspeccionar` ni `auditar` | **SE SOSTIENE ENTERO**: la arista es la mia y en su direccion, y `recorrer` a `contar_firmas` es uno de mis descartes con duda, que su lectura cierra igual (calendario, `ACTA M2` `3.5`) |
| `D78.14` | `contar_firmas` sin arista a `aplicar_ejercicio` | **SE SOSTIENE**: `cap_06` `L85` cambia la regla de la papeleta que `cap_03` `L39` cuenta, pero el ejercicio de `L99` a `L111` es generico y no parte de la cadena contada |

**Y MI DESCARTE QUE EL NO MIRO**, `aplicar_ejercicio_codigo_genetico_control` a `identificar_temas_formacion_tarjetas_decision`: **se
queda descartado**. `cap_06` `L113` nombra la preocupacion de competencia, pero el hijo no usa las tarjetas del ejercicio; su fila de
`aplicar_ejercicio` a `asignar_responsable` lo lee igual, como siguiente iteracion y no despliegue.

**FUERA DEL MARCADO, SUS DOS FRONTERAS DECLARADAS** (`6.1`, fila *dos doctrinas legitimas*), que su fichero de aristas escribe y no marca:

@@RUN:0::grep -n "FRONTERA DECLARADA" .v78ext/aristas_lectura.txt | cut -d'|' -f2,3 | sed 's/^/  /'@@

- **Grove, `delegar_tarea_base_comun_seguimiento` contra `eliminar_seguimiento_descendente_responsabilizar_dueno`: SE SOSTIENE.** Mi fase
  ciega no leyo este par. Leido hoy con los pasos de los dos delante: Grove manda supervisar la tarea delegada porque *delegar sin
  seguimiento es abdicar* y el que delega sigue respondiendo (pasos `6` a `8`); Marquet manda que cada dueno vigile lo suyo, *You are
  responsible, not me and not the XO* (`cap_09` `L71`), y suprime el sistema con el que el de arriba vigila los pendientes del de abajo,
  conservando solo la medicion que informa sin juzgar (`L85`). **Son dos doctrinas con sus fuentes, y ninguna es madre de la otra.**
  **Lo que 6.1 manda es escribir las dos posiciones con sus fuentes** (precedente `ACTA 50` `50.5`), y hoy solo estan en un fichero de
  `.v78ext/`: **va a `DEUDA.jsonl` como `d183`**, para escribirla con `forja.py corregir` en el nodo de Marquet **despues de que entre**,
  y no en la ficha, que cambiaria despues de su barrido (`d031`). La `79` deja el texto preparado.
- **Zhuo, `comunicar_valores_diez_formas` contra `repetir_mensaje_invariable_diario_reunion_evento`: DISCREPA DE MI LECTURA SELLADA, Y VA
  A RELECTURA CONJUNTA** (`1.3`). **Mi caso, con su evidencia**: mi fase ciega lo leyo *sin contradiccion* (`APERTURA_CIEGA.md` `5`,
  ultimo parrafo). Zhuo, paso `3`: *para que el mensaje cale hay que oirlo diez veces distintas y decirlo de diez formas distintas*;
  Marquet, `cap_13` `L119`: *Repeat the same message day after day, meeting after meeting, event after event* y *Changing the message?
  That results in confusion*. **Los dos mandan repetir el mismo mensaje**; lo que Zhuo varia es la forma y la via (su paso `5` son
  cuatro vias), y lo que Marquet prohibe cambiar es el mensaje, que es el contenido. **Leo convergencia, no dos doctrinas.** **La
  lectura contraria, escrita**: *de diez formas distintas* contra *no cambies el mensaje* puede leerse como la misma cosa dicha al reves,
  y una frontera se pierde por poda, no por fusion. **Decide el extractor con la vara** en la `79`; ninguna de las dos lecturas mueve
  una clase, una linea ni una arista.

**DENTRO CONTRA FUERA DEL MARCADO:** catorce marcados, **catorce se sostienen**. **Fuera del marcado**: sus dos fronteras (una se
sostiene, la otra a la conjunta) y mi descarte que no miro (se queda). **Ninguna caida de `CLASE`**: nada entro en la bitacora, y sus
`52` lineas son mis clases.

**LA MUESTRA PINEADA DE LOS SANO** (`7`): **esta vuelta no escribe en la bitacora**, asi que no hay `SANO` de la tanda y **no se
inventa una muestra donde no hay poblacion**. Lo que si hay: **sus `52` lineas `SANO` preparadas, cruzadas todas contra mis `34` pares
leidos a ciegas** (`77.4`), y las `52` coinciden. Los `SANO` de las `20` se muestrean con su semilla cuando entren, en la `ACTA 79`.

## 77.6. **LAS CUATRO GUARDAS DE DATO** (`D.55`)

| guarda | estado | medida |
|---|---|---|
| `gate` | **VERDE** | `77.1` |
| el cerrojo (`D.44`) | **VERDE**: ningun `insertar`, `procesos/` vacio | `77.1` |
| censo no decreciente | **VERDE**: `459` y `1172` al abrir y al cerrar | `77.1` |
| fidelidad `D.30` con puente | **VERDE**: los `3` PUENTE, corregidos en la bandeja; `0` en el texto que entrara | `77.3` |

**Ninguna en rojo: esta acta no deja tarea bloqueante** (`D.55`).

## 77.7. **EL CREDITO DE LA LINEA `serial`** (`5.3`, `D.48`)

Al abrir, y despues de anotar mi tanda:

@@RUN:0::sed -n '5,11p' .v78aud/normal/credito_abrir.txt@@
@@RUN:0::python forja.py credito | sed -n "5,11p"@@

| especie | tanda `ACTA 77` | racha | el motivo, medido |
|---|---|---|---|
| **`CLASE`** | **LIMPIA** | `0 de 2` | nada entro en la bitacora; sus `52` lineas preparadas son mis clases selladas y su arista la mia (`77.4`); sus catorce discutibles se sostienen (`77.5`) |
| **`CIFRA PUBLICADA`** | **LIMPIA** | `0 de 2` | no escribio en `docs/` fuera de `docs/loop/`, ni en `config/`, `esquema/` ni `src/` (`77.0`) |
| **`DATO MOVIDO`** | **LIMPIA** | `0 de 2` | movio las `2` fichas que la correccion manda y nada mas; el grafo, la bitacora y los censos, intactos (`77.0`, `77.4`) |
| **`REPORTE`** | **LIMPIA** | `0 de 3` | `77.2`: ninguna cifra falsa en tabla, cabecera ni conclusion |
| **`AUDITOR`** | **LIMPIA** | `0 de 3` | `77.9`: ninguna cifra mia falsa ni remedio roto |

## 77.8. **EL COSTE** (`D.55`)

@@RUN:0::python .v78aud/normal/coste.py@@
@@RUN:0::grep "extractor listo\|auditor ciego listo" docs/loop/loop.log | tail -2@@

**LOS DOS TURNOS PASAN DE `10` USD Y LA VUELTA NO ES DE SANEAMIENTO: EL DESGLOSE** (`D.55`), leido de la misma salida y de las horas
de sus commits (`77.0`):

- **El extractor, `14,82` USD.** Salida `141938` tokens, `46461` de pensamiento; `134` turnos que releen un contexto grande (`41,3`
  millones de cache leida). **En que se fue, por tramos de reloj**: de `13:29` a `13:42` la fidelidad entera, `110` filas contra trece
  capitulos leidos enteros, con su `R9` y las tres correcciones; de `13:44` a `14:43` el barrido, esperado dentro del turno como se le
  mando, mientras escribia `52` lineas con su razon y `22` filas de arista; y hasta las `15:01` el cierre con el cierre estricto. **Es
  un turno del mismo orden que el de la `76`**, que preparo `22` fichas de Gerber por `15,97` USD (`ACTA 75` `75.8`). **No es gasto
  sin motivo**: es la lectura entera que `D.58` manda antes de insertar.
- **Mi fase ciega, `10,02` USD**, dos centimos por encima. Salida `106667` tokens, `38246` de pensamiento; la misma lectura entera de
  los trece capitulos por mi cuenta (`110` filas con su tramo literal comprobado), un barrido de `20` fichas esperado dentro del turno
  (`15:05` a `16:05`), `34` pares leidos y la pagina generada dos veces para medirse a si misma.

## 77.9. **MI PROPIA TANDA** (`D.38.2`)

**LAS CIFRAS DE MI APERTURA SELLADA, CONTRA LO MEDIDO HOY:** el censo y la poblacion (`77.1`); las `2` fichas cambiadas y las `18`
iguales (`77.0`); mis `110` filas y sus `3` `P` sobre el texto viejo (`77.3`); las `52` filas, los `34` pares, los `8` nodos de fuera y
las `4` fichas sin vecinos (`77.4`); las `34` clases `SANO` y la unica `SOSTENGO` (`77.4`); las siete restricciones (`77.4`). **Todas
cuadran.** **Ningun remedio mio roto** (`77.0`).

**LO QUE MI APERTURA DIJO QUE PESABA, Y LO DIGO OTRA VEZ:** lei los asuntos de sus commits antes de medir, con *52 pares*, *52
veredictos SANO* y *1 arista por lectura* dentro (`APERTURA_CIEGA.md` `1`). **Mis cifras cuadran con esos asuntos y con su reporte**,
y por eso no puedo probar que no me empujaron; **lo que si puedo decir es que la arista, que el asunto no nombraba, es la misma par a
par y con su direccion** (`77.4`).

**MI LECTURA QUE NO GANA SOLA:** la frontera de Zhuo va a la conjunta con mi caso escrito (`77.5`); si la pierdo, se corrige alli por
correccion declarada, sin borrar esta.

**LO QUE MI APERTURA DIJO QUE HARIA EN EL TURNO NORMAL** (su seccion `9`, ocho puntos) **esta todo aqui**: `R5` y `R9` en `77.0` y
`77.3`; el censo con `git` en `77.0`; la fidelidad y `d150` en `77.3`; el barrido, las clases y la arista en `77.4`; el orden en `77.4`;
las huellas en `77.4`; la muestra en `77.5`; `R8` y `R10` en `77.12` y `77.13`.

## 77.10. **LAS CONDICIONES DE PARADA, UNA A UNA, Y LO QUE SIGUE** (`3`, `D.32`, `D.49`)

| condicion | se cumple | como lo mido |
|---|---|---|
| doctrina nueva | **NO** | los discutibles los cubren `6.1`, `D.29`, `D.37`, `D.53` y el precedente `D76.8`; las fronteras, la fila de `6.1` y el precedente `ACTA 50` `50.5` (`77.5`) |
| contradiccion | **NO** | ninguna cifra ni clase contradice a otra (`77.2`, `77.4`); la frontera de Zhuo es una discrepancia de lectura y va a la conjunta, que es la regla de correccion existente (`1.3`) |
| decision de Alexis | **NO** | insertar Marquet esta ordenado (`PARALELO.md` seccion `8` punto `4`); el tag y la parada son de la vuelta que meta su ultima ficha |
| fallo tecnico repetido | **NO** | gate, guiones, suite y cierre estricto en verde (`77.1`) |
| credito roto | **NO** | las cinco rachas en cero (`77.7`) |
| campania consumada | **NO**: faltan las `20` de Marquet | |

@@RUN:0::sed -n '11,13p;24p' .v78aud/normal/tablero.txt@@
@@RUN:0::python scripts/deuda.py --clase 79@@

**LECTURA:** **el unico libro del corte que falta es Marquet**, `COSECHADO` con su bandeja llena y lista. **La `79` es de SANEAMIENTO
por cadencia**, y el arnes no deja que el encargo diga otra cosa (`D.58`): **no inserta y no toca la bandeja**. Paga lo que la campania
puede pagar sin tocar `src/`: `d150` con la fila firmada arriba, `d180` con el tablero de hoy (grove y gerber salen `INSERTADO`, bloque de
arriba), y los punteros de Gerber (`d098`, `d104`, `d099`, `d135`), que con el libro entero en el grafo se contestan midiendo; y hace la
relectura conjunta de la frontera de Zhuo y deja preparado el texto de `d183`. **Sin bloqueante.** Tiene que declararse con `deuda.py
--saneamiento --vuelta 79` (`d085`), o la `80` vuelve a salir de saneamiento.

**Y LO DIGO PARA QUE NADIE SE SORPRENDA:** **la `80` inserta las `20` de Marquet**, y **es la ultima tanda de la campania**: su encargo,
que escribe la `ACTA 78`, lleva lo que `PARALELO.md` seccion `8` puntos `4` y `5` mandan (el tag `primer-equipo-completo` con todo en
verde, `PARA_ALEXIS.md` de cierre y `PROMPT_SIGUIENTE.md` vacio) y el pago de `d183` despues de que entre `eliminar_seguimiento`.

## 77.11. **LOS REMEDIOS**

| # | de quien | remedio | donde se comprueba |
|---|---|---|---|
| `R5` | del extractor | **Sigue vivo con su letra**, cumplido de la `65` a la `78` | el reporte de la `79`, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera cambiada a la `79` |
| `R6` | del auditor | **Sigue vivo con su letra** | la apertura ciega de la `79` |
| `R7` | del auditor | **Sigue vivo con su letra** | la apertura ciega de la `79` y la `ACTA 78` |
| `R8` | del auditor | **Sigue vivo con su letra y su criterio**; instrumento de esta vuelta, `.v78aud/normal/r8_encargo79.py` | mi fase ciega de la `79`, sobre el encargo de la `79` (`77.12`); y el encargo de la `80` |
| `R9` | del extractor | **Sigue vivo con su letra**; en la `79` solo tiene objeto si marca fidelidad | el reporte de la `79`, si publica una cuenta de PUENTE |
| `R10` | del auditor | **Sigue vivo con su letra** | esta acta (`77.13`) y la `ACTA 78` |

## 77.12. **`R8` MEDIDO SOBRE MI ENCARGO DE LA `79`, ANTES DE CERRARLO** (`77.11`)

@@RUN:0::python .v78aud/normal/r8_encargo79.py | tail -1@@

(Las lineas con numero, cada una con sus digitos y sus palabras de numero, en `.v78aud/normal/r8_encargo79.txt`.) **LECTURA, grupo a
grupo, de las que no traen seccion, leidas una a una:**

- **Numeros de vuelta, de acta, de mundo o de carpeta de la casa**: `77`, `78`, `79`, `80`, `11`, `.v64ext/`, `.v64aud/`, `.v78ext/`,
  `.v79ext/`, `.vm01/`, y la `ACTA G9` y la `ACTA 78` como sedes.
- **Secciones, reglas, deudas, remedios y numeros de tarea, de punto o de lista**: `1.4`, `6.1`, `D.47`, `D.58`, `D.61`, `D.37`, `7.F`,
  `D.55`, `d031`, `d085`, `d098`, `d099`, `d104`, `d135`, `d150`, `d180`, `d183`, `R5`, las secciones `8` puntos `3` a `5` de
  `PARALELO.md`, y los de tarea y de punto.
- **Identificadores de capitulo y de linea del libro**: `cap_03`, `cap_05` `L29`, `cap_12` `L21`, `cap_13` `L119`, `cap_17`, `cap_18`
  `L345` a `L349`.
- **Palabras de numero sin seccion**: *los dos delante* (los dos nodos de un par), *las dos posiciones* (las de una frontera), *los
  dos nodos de Marquet* (los dos que la TAREA `2` nombra), y *cero guiones* (la frase fija).
- **Las cifras de medida** van dentro de un bloque `$` (la clase, el tablero y las siete deudas) o llevan su seccion de la `ACTA 77` en
  la misma linea: las `2` fichas corregidas y los nueve instrumentos (`77.0`, `77.1`), los catorce discutibles y las dos fronteras
  (`77.5`), el censo de apertura (`77.1`).

**Cuatro lineas las reescribi al medir**, antes de cerrar: *las `20` fichas* que la `78` dejo listas, *las tres fases* y *las tres
palabras* de los punteros de Gerber, y *tres tramos* de `d135` salieron de la frase; y una afirmacion que no habia medido (*Gerber entro
sin ninguna ficha de `cap_03`*) se cambio por una medida que la `79` hace. **`R8` CUMPLIDO EN EL ENCARGO DE LA `79`, medido.** Lo vuelve
a medir mi fase ciega (`77.11`).

## 77.13. **LO QUE ANOTO AL CERRAR**

- **`docs/loop/DEUDA.jsonl`**: **`d183`**, la frontera de Grove sin escribir (`77.5`), anotada con `--especie relectura`.
- **`docs/loop/CREDITO_serial.jsonl`**: las cinco lineas de la tanda `ACTA 77` (`77.7`), todas con `--limpia`. **Las dos anotaciones van
  ANTES de correr las salidas que pego en el encargo** (`R10`), y comparadas despues:

@@RUN:0::cat .v78aud/normal/r10.txt@@

- **`docs/loop/PROMPT_SIGUIENTE.md`**: el encargo de la vuelta `79`, **SANEAMIENTO**: la conjunta de Zhuo, el texto de `d183`
  preparado, y `d150`, `d180`, `d098`, `d104`, `d099` y `d135`; sin insertar, sin tocar la bandeja y sin bloqueante.
- **`.v78aud/`**: mi evidencia de las dos fases, commiteada con `docs/loop/`.
