
# ACTA 79. VUELTA 80, lote 5 (`marquet_turn_the_ship`), **CLASE INSERCION, ULTIMA TANDA DE LA CAMPANIA**: **LAS `20` FICHAS DE MARQUET ENTRARON UNA POR VEZ, EN SU ORDEN, SIN SOLAPARSE Y CON LOS BYTES QUE SE LEYERON; SUS `52` LINEAS SON LAS PREPARADAS LETRA A LETRA, LAS FILAS DE MI BARRIDO AL DIGITO Y MIS CLASES SELLADAS; LA UNICA ARISTA ES MI `SOSTENGO`, CABLEADA ENTRE LA FILA `5` Y LA `6`; NINGUN NODO VIEJO CAMBIA. `d183` ESCRIBE LA FRONTERA DE GROVE TAL CUAL Y `d104` SE PAGA SIN TOCAR EL GRAFO: LAS DOS SE SOSTIENEN. EL TAG `primer-equipo-completo` APUNTA A `69d407da`, EL COMMIT DEL GRAFO COMPLETO, Y ESTA EMPUJADO. SUS CUATRO DISCUTIBLES SE SOSTIENEN, LA MUESTRA DE LOS SANO `11` DE `11`, CERO CAIDAS SUYAS Y CERO MIAS: LAS CINCO RACHAS EN CERO. `MUNDO 11 COMPLETO`: `479` NODOS EN OCHO CLAVES, `220` ARISTAS, `1` ENTRE LIBROS. CAMPANIA CONSUMADA: `PARA_ALEXIS.md` DE CIERRE Y `PROMPT_SIGUIENTE.md` VACIO**

*Auditor `claude-opus-5-5`, 26 sep 2026, turno normal de la vuelta que el arnes numera `4` en la corrida que arranco el 26 a las
`09:27`. Linea **serial**, rama `extraccion-mundo-11`, hash auditado `d09a152a` (cierre del extractor, mas `67f2bee3` con la salida
del hook, sin trabajo nuevo), arbol en `c7e3796b` con mi apertura sellada. Modo austero (`D.47`). Toda mi evidencia de este turno
esta en `.v80aud/normal/`, y la de mi fase ciega en `.v80aud/`. **Cada bloque `$` de esta acta lo pega `.v80aud/normal/generar.py`
corriendo la orden al generarla**; las salidas largas (la suite, el cierre estricto) se corrieron antes, en serie, y se pegan con `cat`
de su fichero.*

## 79.0. **HUECO DE ACTA Y HERENCIA** (`1.0`, `D.40`)

**NO HAY HUECO.** La `ACTA 78` cubre la vuelta `79`; esta cubre la `80` entera: el turno del extractor (de `fcb1cdc9` a `67f2bee3`,
`17:32` a `21:22` del 26) y mi fase ciega, sellada en `c7e3796b`, que solo toca sus dos ficheros. Lo que la vuelta movio desde mi acta
(`0da1d2b7`, la salida del hook de la `ACTA 78`):

@@CMD git log --format="%h" 0da1d2b7..67f2bee3 | wc -l; git log --format="%h %an %cI %s" 0da1d2b7..67f2bee3 | grep -v "fila [0-9]*:" | cut -c1-120@@
@@CMD git diff --name-status 0da1d2b7 67f2bee3 | grep -v "\.v80ext/" | sed -E 's|(cuarentena/)[^/]+/[^/]+\.json.*|\1...json|' | sort | uniq -c@@
@@CMD git diff --name-status 0da1d2b7 67f2bee3 -- .v80ext | awk '{print $1}' | sort | uniq -c; git log --format="%h" 0da1d2b7..67f2bee3 -- src tests scripts forja.py config esquema fuentes .v78ext .v78aud .v79ext | wc -l; git diff 0da1d2b7 67f2bee3 -- dataset bitacora censos | grep -cE "^-[^-]"@@

**LECTURA:** **la vuelta movio lo que una insercion mueve y nada mas**: el grafo, la bitacora, `censos/denominaciones.md` (que escribe la
aduana al insertar), `docs/loop/DEUDA.jsonl` (los dos pagos), las `20` fichas de la bandeja renombradas a `_insertados`, su reporte, los
ficheros del arnes y su carpeta `.v80ext/` (todo ficheros nuevos). **En el dato no hay ni una linea quitada**: `0` lineas `-` en
`dataset`, `bitacora` y `censos`. **Ni `src/`, `tests/`, `scripts/`, `config/`, `esquema/`, `fuentes/`, ni `.v78ext/`, `.v78aud/` y
`.v79ext/`**, que son las sedes de lo que se leyo y se firmo.

**HEREDADO 1, `R5` del extractor: CUMPLIDO.** Con mis copias sacadas con `sed` de los originales `.v64ext/pegado64.py` y
`.v64aud/normal/bloques_mudos.py`, no de las suyas, con la cabecera cambiada a la `80`; y las mismas sobre el reporte cortado en la
linea `68856`, justo antes de su propio bloque de `R5`:

@@CMD diff --strip-trailing-cr .v64ext/pegado64.py .v80aud/normal/pegado80_aud.py | grep -c "^>"; diff --strip-trailing-cr .v64aud/normal/bloques_mudos.py .v80aud/normal/bloques_mudos80_aud.py | grep -c "^>"@@
@@CMD python .v80aud/normal/pegado80_aud.py; python .v80aud/normal/bloques_mudos80_aud.py@@
@@CMD python .v80aud/normal/pegado80_sin_su_bloque.py; python .v80aud/normal/bloques_mudos80_sin_su_bloque.py@@

**`0` y `0` sobre el tramo entero** (`72` comandos en `37` bloques). **Su `80.5.g` publica `70` y `36`**, y es la cuenta del tramo **sin el
bloque que la publica**, que es lo unico que un bloque no puede contarse a si mismo: cortado antes de el, da `70` y `36` al digito. **No es
cifra falsa.** Y `R5` no es todo: que cada comando tenga salida no dice que sea la suya, y eso lo mido en `79.1`.

**HEREDADO 2, `R6`, y HEREDADO 3, `R7`, mios: CUMPLIDOS** en la fase ciega (`APERTURA_CIEGA.md` `0` y `8`) **y en esta acta**: los pasos
de la muestra los imprime `.v67aud/normal/pasos_ciego.py` (`79.4`), y cada instrumento mio de este turno que reparte un total en clases
imprime su `suma` (`lineas54.py`, `cierre_campania.py`, `reproducir.py`). **HEREDADO 4, `R8`, mio: CUMPLIDO en el encargo de la `80`**
(`APERTURA_CIEGA.md` `6`), **y sin objeto sobre la `81`: no hay encargo** (`79.10`). **HEREDADO 5, `R9` del extractor: NO APLICA, y la
salida lo sostiene**: la vuelta no escribio ni marco ninguna fila de fidelidad; la cuenta de PUENTE que publica (`80.5.b`) sale de
`.v78ext/fidelidad.tsv`, que la `78` cruzo con `R9` y que nadie toco (el bloque de arriba: `0` commits sobre `.v78ext/`):

@@CMD ls .v80ext | grep -ci "fidel"; git diff --name-only 0da1d2b7 67f2bee3 | grep -ci "fidelidad"@@

**HEREDADO 6, `R10`, mio: CUMPLIDO** al cerrar la `ACTA 78` (`78.13`) y medido en mi fase ciega (`APERTURA_CIEGA.md` `0`); **y en esta
acta**, `79.12`.

## 79.1. **LO QUE VERIFICO, CON MIS PROPIOS COMANDOS** (`1.1`)

Corridos en serie por `.v80aud/normal/guardas.sh`, cada uno con su `rc`, **con el arbol en `c7e3796b`**:

@@CMD cat .v80aud/normal/gate.txt .v80aud/normal/guiones.txt .v80aud/normal/resolutor.txt@@
@@CMD grep 'total:' .v80aud/normal/suite.txt; tail -1 .v80aud/normal/suite.txt; cat .v80aud/normal/suite_hora.txt@@

**EL CENSO, MI CUENTA DEL DATASET Y DE LA BITACORA:**

@@CMD wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl@@
@@CMD for d in cuarentena/marquet_turn_the_ship cuarentena/_insertados/marquet_turn_the_ship; do echo "$d $(find $d -maxdepth 1 -name '*.json' | wc -l)"; done; echo "procesos $(ls -A procesos/ | wc -l)"; python .v70aud/poblacion.py@@

**EL CIERRE ESTRICTO, CORRIDO POR MI**, en serie despues de la suite, con `procesos/` vacio al terminar:

@@CMD grep -nE '^(CIERRE|CENSO|TALLADO|TABLA DE CIERRE)|DIFIEREN|CAEN  ' .v80aud/normal/cerrar_reporte.txt; tail -1 .v80aud/normal/cerrar_reporte.txt; cat .v80aud/normal/cerrar_hora.txt .v80aud/normal/procesos_al_acabar.txt@@

**LECTURA:** **gate, guiones, resolutor, la suite y el cierre estricto, VERDES**, con el grafo en `479`. **El censo de su `80.5.a` al
digito** (`479`, `1226`, `1`; bandeja de Marquet `0`, insertados `20`; poblacion `479`, toda en el grafo) **y el de mi apertura sellada**
(`APERTURA_CIEGA.md` `2`). Mi cierre cuenta las rutas del arbol de hoy, que no es el de su corrida final (despues entraron la salida de
su hook y mi apertura); **ninguna cae**, y no descompongo la diferencia.

**LO QUE REPRODUZCO DE SU TRAMO**: cada linea `$` de diez ficheros de evidencia de `.v80ext/`, vuelta a correr hoy con `bash` y su salida
comparada con la guardada, salvo las que escriben (`--pagar`, `corregir`, `arista`, `git tag`, `git push` y las que redirigen a
`.v80ext/`), que no se corren:

@@CMD cat .v80aud/normal/reproducir.txt | grep -v "^     " @@

**LECTURA de las siete distintas, una a una: las siete son las esperadas**, porque miden un registro que la propia vuelta volvio a
escribir despues de pegarlas, en el orden de su reporte: la deuda pendiente de `d183` y la clase con `45` (antes de pagar `d183`, que la
baja a `44`); `sha1sum -c` sobre la bandeja, que hoy esta vacia porque las `20` se movieron a `_insertados` (mi `huellas_hoy.py` de la
fase ciega las encontro alli con la misma huella, `APERTURA_CIEGA.md` `2`); y cuatro cuentas de la bitacora tomadas antes de la linea
`1226` de `corregir` (`53` registros, `1225` lineas, el `Counter` sin `CORREGIDO`). **Ninguna es una salida que su comando no diera
cuando se pego.** Las `23` que se pueden reproducir hoy salen identicas, y entre ellas el tablero, el censo por libro, el `diff` vacio
desde `69d407da`, los relojes, `nodos_viejos.py` y la tabla de `pasos_inventados.py`. De `aristas_vuelta.py` cambia solo su primera linea
(`53` registros hoy `54`, por la de `corregir`); sus lineas de aristas salen iguales.

## 79.2. **EL REPORTE, AFIRMACION POR AFIRMACION** (`5.2`)

| afirmacion del reporte | sale | sede | especie |
|---|---|---|---|
| cabecera y tabla de tareas: `PRIMER EQUIPO COMPLETO` en `69d407da`, `479` y el censo por libro; `T1` a `T5` cerradas; censo `459`, `1172`, `1`, `20`, `0` y `479`, `1226`, `1`, `0`, `20`; `3` PUENTE y `0` que entraron | **cierta, celda a celda** (`79.1`, `79.5`, `79.10`) | TABLA y CABECERA | |
| `80.0`: `fcb1cdc9`, gate con `459`, el censo, `LIBRE` con `46`, poblacion `479`, huellas identicas | **cierta** (`79.0`; el censo de apertura es el de mi `ACTA 78` `78.1`) | bloque | |
| `80.1`: los registros de la `ACTA 78`; `d104` pagada citando `78.3` por sus lineas, sin tocar el grafo; `46` a `45` | **cierta** (`79.3`, `79.1`) | tabla y bloque | |
| `80.2`: las huellas identicas, `110` pasos, `18` y `2`, `21` huellas sin queja | **cierta** (`79.1`, reproducida salvo el `sha1sum` que hoy mide una bandeja vacia) | bloque | |
| `80.3`: las `20` filas, cada una con su aduana, sus vecinos y su comparacion con la `78`; la arista en la fila `5`; los tramos de la bitacora | **cierta, fila a fila** (`79.3`: las `52` lineas, el orden y los relojes) | tablas y bloques | |
| `80.3.b`: `1` arista esperada y viva, `0` viejos cambiados, `20` `.fin` en `0`, `52` lineas, `53` registros, relojes | **cierta** (`79.1`, `79.3`) | bloques | |
| `80.4`: `corregir` en la `1226`, `3296` y `498` caracteres, `2300` mas `1` mas `3296`; `d183` pagada; `44` | **cierta** (`APERTURA_CIEGA.md` `3`, `79.3`) | bloques | |
| `80.5.a` a `80.5.e`: censo, `PASOS INVENTADOS` por capitulo, `D.61`, `R5` con `52` y `29`, guardas con `382` | **cierta** (`79.0`, `79.1`, `79.5`) | bloques y tablas | |
| `80.5.f` y `80.5.g`: tablero, censo por libro, `220` aristas y `1` entre libros, `diff` vacio, tag en `69d407da` y en `origin`; `R5` con `70` y `36`; cierre verde | **cierta** (`79.1`, `79.0`, `79.10`) | bloques y prosa | |

**NINGUNA CAIDA SUYA.** **LA RELECTURA AL DOBLE no aplica**: no hay caida de `REPORTE` en el tramo. **Una nota, no una caida:** el `como`
de `d183` dice *3296 anadidos* y `corregir` imprime *se aniaden 3297 caracteres*; los dos son ciertos, porque `corregir` cuenta el
separador y el `como` cuenta la linea `ANADE`, y su `80.4` lo escribe entero (`5597` es `2300` mas `1` mas `3296`).

## 79.3. **LA RELECTURA DE LA TANDA** (`1.2`, `5.1`, `6.1`)

**SUS CUATRO DISCUTIBLES, POR NUMERO** (`D.47`):

| | su marca | adjudico |
|---|---|---|
| `D80.1` | el metodo de la `77`: un `insertar` por proceso, esperado en primer plano hasta su `.fin` | **SE SOSTIENE**, medido abajo: `20` de `20` con el siguiente lanzado despues del fin del anterior y su commit entre los dos |
| `D80.2` | `insertar.py` comprueba que el id es el de su fila | **SE SOSTIENE**: no cambia lo que entra ni las lineas; el orden del grafo es el del encargo (`APERTURA_CIEGA.md` `4`) |
| `D80.3` | la frontera de Grove despues de la fila `20`, no justo despues de la `16` | **SE SOSTIENE**: mi letra (*cuando viva en el grafo, y no antes*) fija el suelo y no el techo; escribirla en medio podia mover la senial de un nodo que las filas `17` a `20` median contra mi barrido. El texto es el mismo (`APERTURA_CIEGA.md` `3`) |
| `D80.4` | la cabecera empieza por `# VUELTA 80 DE LA LINEA SERIAL:` y lleva `PRIMER EQUIPO COMPLETO` detras | **SE SOSTIENE**: el encargo pedia que el tramo abriera con esas palabras, el hash y el censo, y abre asi; el prefijo es el que encuentran los instrumentos de `R5` |

**LAS `54` LINEAS NUEVAS DE LA BITACORA, UNA A UNA**, contra las tres sedes de la preparacion: la linea preparada (veredicto y razon,
letra a letra), mi fila dirigida del barrido de la `78` (su senial y sus tres cifras) y mi clase sellada del par:

@@CMD python .v80aud/normal/lineas54.py@@

**Y LA DE LA ARISTA**, contra mi fila `SOSTENGO` (`.v78ext/aristas_lectura.txt` linea `28`, que la `ACTA 77` `77.4` cruzo con la mia):

@@CMD python .v80aud/normal/arista_linea.py@@

**EL ORDEN Y LOS RELOJES**, de `.v80ext/insertar_*.txt` y de las horas de commit de `git`:

@@CMD python .v80aud/normal/orden_tiempo.py | tail -7@@

(Las `20` filas con su inicio, su fin y su commit, en `.v80aud/normal/orden_tiempo.txt`.) **LECTURA:** **las `52` lineas son las
preparadas, las filas de mi barrido y mis clases**, sin ninguna de mas ni de menos; **la de la arista es mi `SOSTENGO` con su razon tal
cual, su paso `7` y el veredicto de lectura que mi encargo pedia** (`CONTINUA`, `D.53`); y **cada `insertar` volvio con `0` antes de
lanzarse el siguiente**, su commit entre los dos, la arista entre la fila `5` y la `6`, y `corregir` despues de la `20`. **Ninguna aduana
levanto un vecino fuera de mi barrido** (las `20` comparaciones de su `80.3` y mi cuenta de filas: `0` sin linea). **Lo que mi fase ciega
dejo para aqui sobre la arista** (`APERTURA_CIEGA.md` `5`: con que veredicto y que razon) **esta resuelto**: `CONTINUA` y mi razon.

**LOS DOS PAGOS**, contra la `ACTA 78` `78.3`:

@@CMD python .v80aud/normal/comos.py | grep -v "^  como"@@

- **`d104`, SE SOSTIENE.** Su `como` cita `78.3` por sus lineas (`52103` a `52128`, que son las de la adjudicacion), dice las dos razones
  como las escribi (por `D.37` no, porque nombra sin contar y ninguna parte existe; por `D.29` no, porque nombrar no es procedimentar y
  ninguno usa el producto de la madre), y **el grafo no se toco por ella** (`APERTURA_CIEGA.md` `2`, `(a)` y `(b)`).
- **`d183`, SE SOSTIENE.** El texto y la razon de la linea `1226` son byte a byte las dos lineas de `.v79ext/frontera_grove.txt`, que firme
  en `78.3` contra mis dos posiciones; los pasos del nodo no cambian y el resumen viejo sigue entero (`APERTURA_CIEGA.md` `3`). La de Zhuo
  no se escribe, como cerro `78.3`.

**DENTRO CONTRA FUERA DEL MARCADO:** cuatro marcados, **cuatro se sostienen**. **Fuera del marcado**: las `52` lineas, la arista, los dos
pagos y la muestra de `79.4`, **ninguna cae**.

## 79.4. **LA MUESTRA PINEADA DE LOS SANO** (`7`)

Semilla `80`, registrada en mi fase ciega (`APERTURA_CIEGA.md` `7`, punto `4`); el tamanio, el mayor entre `3` y el `20` por ciento
redondeado hacia arriba, con techo de `20`; la poblacion, toda linea `SANO` que la vuelta anadio:

@@CMD python .v80aud/normal/muestra_sano.py@@

**PRIMERO LOS PASOS, DESPUES SU RAZON.** Los de los catorce nodos, en `.v80aud/normal/pasos_muestra.txt` por `pasos_ciego.py`. **Mi lectura,
escrita antes de destapar, con la vara `6.1` y solo esa:**

- `1174`: **SANO**, ajenos: conservar la plantilla y cambiar como interactua contra la practica de escuchar tres minutos (Scott). La
  senial es de forma verbal.
- `1191` y `1197`: **SANO**, hermanos de `cap_03`: cuatro lecturas distintas del recien llegado (la reunion, el tablero de mensajes, el
  recorrido con linterna, la formacion desde la ultima fila); ninguna usa el producto de otra.
- `1199` y `1200`: **SANO**, ajenos: el reporte de cierre de jornada contra la destreza minima y los seis conteos de Gerber.
- `1208`, `1219`, `1223` y `1224`: **SANO**, hermanos de CONTROL con procedimiento propio en los dos lados: la frase de intencion, el
  reparto de la decision por urgencia, los inspectores de fuera y el ritual de pausar y senialar. El paso `2` de `tomar_accion` **nombra**
  al inspector sin procedimentar nada suyo.
- `1220` y `1222`: **SANO**, ajenos: los principios guia en premios, y el recorrido con linterna, contra los inspectores de fuera; la
  palabra *inspeccion* es comun y el procedimiento no.

Destapadas despues (`.v80aud/normal/razones_muestra.txt`): **las once razones dicen lo mismo con el libro citado.**

@@CMD python .v80aud/normal/banda_muestra.py@@

**LO QUE PESA SOBRE ESTA RELECTURA, Y LO DIGO:** para ver el formato de `.v78ext/veredictos_listos.txt` imprimi su cabeza **antes** de sacar
la muestra, y en ella salian, cortadas, las razones de las seis lineas de `acoger_inspectores`, entre ellas las de `1219`, `1220` y `1222`.
**Mis clases de esos pares son las de mi lectura sellada de la `78`** (`.v78aud/mis_clases.tsv`, que `lineas54.py` cruza), no las de hoy;
**pero no puedo probar que esas tres relecturas no las empujo lo que lei.** Las otras ocho las lei sin su razon delante.

## 79.5. **FIDELIDAD Y `PASOS INVENTADOS POR CAPITULO`, DE LO QUE ENTRO** (`D.30`, `D.58`, `8`, `8.2`, `8.3`)

**La relectura de fidelidad de `D.58` sobre lo que entra es mi lectura entera de la `78`** (`.v78aud/fidelidad.tsv`, una fila por paso),
**porque lo que entro es byte a byte lo que lei**. Contado por mi, sobre el grafo de hoy, un capitulo por fila; es el instrumento de mi fase
ciega, corrido otra vez:

@@CMD python .v80aud/entra_lo_leido.py | sed -n '2p;6,$p'@@

**`PASOS INVENTADOS POR CAPITULO`, FIRMADA POR MI:** **`0` PUENTE que entraron en los trece capitulos, `0` de `110`**. Sobre el texto de al
abrir la `78` el peor capitulo fue `cap_04` (*Whatever They Tell Me to Do!*), `2` de `5`, y `cap_03` `1` de `53`: los `3` PUENTE que la
`78` corrigio en la bandeja antes de mi barrido, que es su columna de *PUENTE marcados* (`80.5.b`) y la de mi `ACTA 77` `77.3`. **Su tabla
y la mia cuentan lo mismo, capitulo a capitulo**: pasos por capitulo iguales, y `0` que entraron en las dos. **Cruce `8.3`:** mis `T` son
de mi lectura paso a paso contra su parrafo, no de las suyas, y mis dos `D` de `cap_03` las cerro `T` la `77.5`. **No dimensiona nada**: no
queda lote de extraccion (`PARALELO.md` `8` punto `3`).

## 79.6. **LAS CUATRO GUARDAS DE DATO** (`D.55`)

| guarda | estado | medida |
|---|---|---|
| `gate` | **VERDE** | `79.1` |
| el cerrojo (`D.44`) | **VERDE**: `20` `insertar`, uno por vez; `procesos/` vacio | `79.1`, `79.3` |
| censo no decreciente | **VERDE**: `459` a `479` y `1172` a `1226`, `0` lineas quitadas | `79.0`, `79.1` |
| fidelidad `D.30` con puente | **VERDE**: `0` PUENTE en lo que entro | `79.5` |

**Ninguna en rojo: esta acta no deja tarea bloqueante** (`D.55`), y ademas no hay vuelta siguiente (`79.10`).

## 79.7. **EL CREDITO DE LA LINEA `serial`** (`5.3`, `D.48`)

Al abrir, y despues de anotar mi tanda:

@@CMD sed -n '5,11p' .v80aud/normal/credito_abrir.txt@@
@@CMD python forja.py credito | sed -n '5,13p'@@

| especie | tanda `ACTA 79` | racha | el motivo, medido |
|---|---|---|---|
| **`CLASE`** | **LIMPIA** | `0 de 2` | las `52` lineas son mis clases selladas, la arista es mi `SOSTENGO`, la muestra `11` de `11` (`79.3`, `79.4`) |
| **`CIFRA PUBLICADA`** | **LIMPIA** | `0 de 2` | no escribio en `docs/` fuera de `docs/loop/`, ni en `config/`, `esquema/` ni `src/` (`79.0`) |
| **`DATO MOVIDO`** | **LIMPIA** | `0 de 2` | el dato se movio solo por lo que el encargo mandaba: `20` filas, `54` lineas, `1` `corregir`, `2` pagos; `0` nodos viejos cambiados (`79.0`, `APERTURA_CIEGA.md` `2`) |
| **`REPORTE`** | **LIMPIA** | `0 de 3` | ninguna caida en el tramo (`79.2`) |
| **`AUDITOR`** | **LIMPIA** | `0 de 3` | `79.9`: ninguna cifra mia falsa ni remedio roto |

## 79.8. **EL COSTE** (`D.55`)

@@CMD python .v78aud/normal/coste.py; grep "extractor listo\|auditor ciego listo" docs/loop/loop.log | tail -2@@

**Los dos turnos por debajo de `10` USD: no hay desglose que declarar.** **LECTURA:** el extractor corrio `13892` s de reloj para `855` s de
API, y la mayor parte de la diferencia son los `20` `insertar` esperados en primer plano (`10557` s de suma, su `80.3.b`, reproducida en `79.1`).

## 79.9. **MI PROPIA TANDA** (`D.38.2`)

**LAS CIFRAS DE MI APERTURA SELLADA, CONTRA LO MEDIDO HOY:** el censo (`479`, `1226`, `1`, `0`, `20`, `procesos/` vacio), la poblacion
(`479`), el censo por libro con `20` de Marquet y su suma, las `220` aristas con `1` entre libros, la bitacora esperada `1226`, la arista
esperada viva por los dos lados, el orden de entrada y las siete restricciones, los `110` pasos y `0` PUENTE que entraron, y la etiqueta en
`69d407da` (`79.1`, `79.3`, `79.5`, `79.10`). **Todas cuadran.** **Ningun remedio mio roto** (`79.0`).

**LO QUE MI APERTURA DEJO PARA QUE SE JUZGUE, Y LO QUE HAGO CON ELLO:** la linea `L42` del encargo de la `80` (*`1173` en adelante*,
`APERTURA_CIEGA.md` `6`). **La sigo leyendo como identificador** (el numero de una linea de la bitacora, que la `1172` medida de su misma
frase da), no como cifra de medida, y por eso **no me la cargo**; queda escrita para el fundador. **Y lo que dije que pesaba** (los asuntos de
los commits leidos antes de medir, `APERTURA_CIEGA.md` `1`) **no movio ninguna clase**: todas son las de mis ficheros de la `78`.

**LO QUE MI APERTURA DIJO QUE HARIA EN EL TURNO NORMAL** (su seccion `7`, ocho puntos) **esta todo aqui**: `R5` y `R9` en `79.0`; las
`54` lineas en `79.3`; los `insertar`, su orden y la arista en `79.3`; la muestra en `79.4`; los pagos en `79.3`; el tag en `79.10`; el
censo con `git`, las guardas, el cierre estricto y el coste en `79.0`, `79.1` y `79.8`; y el cierre de la campania con `R10` en `79.10` y
`79.12`.

**UN ERROR MIO DE METODO, DICHO:** la cabeza de `veredictos_listos.txt` leida antes de la muestra (`79.4`). No mueve ninguna cifra ni clase.

## 79.10. **LAS CONDICIONES DE PARADA, UNA A UNA: CAMPANIA CONSUMADA** (`3`, `D.49`, `PARALELO.md` `4.c` y `8`)

| condicion | se cumple | como lo mido |
|---|---|---|
| doctrina nueva | **NO** | los discutibles, los pagos y la arista los cubren `6.1`, `D.29`, `D.37` y `D.53` (`79.3`) |
| contradiccion | **NO** | ninguna cifra ni clase contradice a otra (`79.2`, `79.3`) |
| decision de Alexis | **NO por si sola** | insertar Marquet y el tag estaban ordenados (`PARALELO.md` `8` punto `4`); lo que viene despues si es suyo, y va en `PARA_ALEXIS.md` |
| fallo tecnico repetido | **NO** | gate, guiones, resolutor, suite y cierre estricto en verde (`79.1`) |
| credito roto | **NO** | las cinco rachas en cero (`79.7`) |
| **campania consumada** | **SI** | el tablero da los siete libros del corte `INSERTADOS`; el tag esta en el commit del grafo completo y en `origin`; todo en verde (abajo) |

@@CMD python forja.py tablero | sed -n '6,16p;24,27p'@@
Y la etiqueta, medida con `git` en este turno (`.v80aud/normal/tag.txt`, con sus lineas `$` escritas al correrlas):

@@FILE .v80aud/normal/tag.txt@@

**LECTURA:** **`primer-equipo-completo` es un tag anotado que apunta a `69d407da`**, en local y en `origin`; la fila `20` (`e4d88c5f`) es
anterior a el, y **desde ahi el dato no cambio** (`0` lineas de `diff` sobre `dataset`, `bitacora`, `censos`, `cuarentena`, `config` y
`src`), asi que **es el commit en que el grafo quedo completo**, que es lo que mi encargo pedia. **La rama remota esta en `67f2bee3`**: mi
apertura sellada (`c7e3796b`) y esta acta se empujan al cerrar.

**LAS TRES COSAS QUE `PARALELO.md` `4.c` PIDE AL `PARA_ALEXIS` DE CIERRE, MEDIDAS POR MI:**

@@CMD python .v80aud/normal/cierre_campania.py@@

**LECTURA:** **`479` nodos en ocho claves**, que son los siete libros del corte y `manual_sistema_conocimiento` (los `2` nodos semilla de
la casa), **con su suma igual a las filas del fichero** y ningun nodo con dos fuentes; **`220` aristas, todas escritas por los dos lados, y
`1` entre libros** (de Zhuo a Scott, la misma de mi `ACTA 78` `78.10`: la tanda de Marquet no cruzo a otro libro). **Los tres del corte
siguen en `fuentes/` con sus capitulos, sin un nodo en el grafo ni una ficha en cuarentena**, con el motivo de `config/frentes.json`; **la
ficha de `bernerslee_bananas` tiene el anio `PENDIENTE`** y su nota dice que hay que cerrarla antes de insertar su primer nodo.

**SE CUMPLE LA PARADA FELIZ** (`3`, *campania consumada*; `PARALELO.md` `8` punto `5`): escribo `docs/loop/PARA_ALEXIS.md` de cierre con
esas tres cosas, el estado exacto y lo que se necesita del fundador, **pidiendo el merge sin hacerlo** (`3`: *el bucle no funde ramas*), y
**dejo `docs/loop/PROMPT_SIGUIENTE.md` vacio**. El arnes lo lee al abrir la vuelta siguiente y se detiene.

## 79.11. **LOS REMEDIOS**

| # | de quien | estado al cerrar la campania |
|---|---|---|
| `R5` | del extractor | **Cumplido** de la `65` a la `80` (`79.0`). Sin vuelta siguiente; queda escrito con su letra |
| `R6` | del auditor | **Cumplido** en la fase ciega de la `80` y en `79.4`. Queda escrito |
| `R7` | del auditor | **Cumplido** en la fase ciega de la `80` y en esta acta. Queda escrito |
| `R8` | del auditor | **Cumplido** en el encargo de la `80`; **sin encargo de la `81` que medir** |
| `R9` | del extractor | **No aplico en la `80`**: no marco fidelidad (`79.0`). Queda escrito |
| `R10` | del auditor | **Cumplido en esta acta** sobre `PARA_ALEXIS.md` (`79.12`) |

**Ningun remedio nuevo.** Si el fundador reabre la linea, los seis siguen con su letra y el que la reabra los hereda por `D.40`.

## 79.12. **`R10` SOBRE LO QUE PEGO FUERA DEL ACTA**

**`PROMPT_SIGUIENTE.md` queda vacio, asi que no pega nada.** **`PARA_ALEXIS.md` si pega salidas** (el credito, el censo, las aristas, los
tres libros, la cola y las deudas), y las genera `.v80aud/normal/generar.py` **despues** de mi anotacion en `CREDITO_serial.jsonl`, que
es mi ultima escritura en un registro; antes del commit las vuelvo a correr y las comparo, con `.v80aud/normal/r10.sh`, cuya salida
queda en `.v80aud/normal/r10.txt` y en el mensaje del commit del acta.

## 79.13. **LO QUE ANOTO AL CERRAR**

- **`docs/loop/CREDITO_serial.jsonl`**: las cinco lineas de la tanda `ACTA 79` (`79.7`), todas con `--limpia`.
- **`docs/loop/DEUDA.jsonl`**: **nada**. Ninguna lectura de esta acta abre deuda; las `44` que esperan van en `PARA_ALEXIS.md` para el
  fundador, y la cola de doctrina (`11` preguntas, ninguna bloquea) tambien.
- **`docs/loop/PARA_ALEXIS.md`**: el cierre de la campania de nodos, **MUNDO 11 COMPLETO**.
- **`docs/loop/PROMPT_SIGUIENTE.md`**: **vacio**.
- **`.v80aud/`**: mi evidencia de las dos fases, commiteada con `docs/loop/`.
