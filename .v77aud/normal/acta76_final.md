
# ACTA 76. VUELTA 77, lote 9 (`gerber_emyth`), **CLASE INSERCION**: **LA RELECTURA CONJUNTA SE CIERRA: LAS DOS PIEZAS LAS GANA LA LECTURA DE LA `ACTA 75` Y EL EXTRACTOR LAS EJECUTO ANTES DEL PRIMER `insertar`. LAS `22` FICHAS DE GERBER ENTRARON UNA POR VEZ, SIN SOLAPARSE, EN SU ORDEN Y CON LOS BYTES QUE SE LEYERON; SUS `54` LINEAS DE VEREDICTO SON LAS PREPARADAS LETRA A LETRA, LAS FILAS DE MI BARRIDO Y MIS CLASES SELLADAS; SUS `7` ARISTAS POR LECTURA SON SUS FILAS `SOSTENGO` CON SU PASO, Y LAS `10` ARISTAS DE LA TANDA SON MIS `10`, POR LOS DOS LADOS; NINGUN NODO VIEJO CAMBIA. GERBER QUEDA ENTERO EN EL GRAFO. SUS CUATRO DISCUTIBLES SE SOSTIENEN, `d111` Y `d108` SE FIRMAN, LA MUESTRA DE LOS SANO SE SOSTIENE `11` DE `11`, CERO CAIDAS SUYAS Y CERO MIAS: LAS CINCO RACHAS EN CERO. LA `78` PREPARA MARQUET, EL ULTIMO LIBRO DEL CORTE**

*Auditor `claude-opus-5-5`, 26 sep 2026, turno normal de la vuelta que el arnes numera `1` en la corrida que arranco el 26 a las
`09:27`. Linea **serial**, rama `extraccion-mundo-11`, hash auditado `b2d27bbc` (cierre del extractor, mas `a70bdf05` con la salida
del hook, sin trabajo nuevo), arbol en `78ed0408` con mi apertura sellada. Modo austero (`D.47`). Toda mi evidencia de este turno
esta en `.v77aud/normal/`, y la de mi fase ciega en `.v77aud/`.*

## 76.0. **HUECO DE ACTA Y HERENCIA** (`1.0`, `D.40`)

**NO HAY HUECO.** La `ACTA 75` cubre la vuelta `76`; esta cubre la `77` entera: el turno del extractor (de `70a827c9` a `a70bdf05`,
`09:27` a `12:55` del 26) y mi fase ciega, sellada en `78ed0408`, que solo toca sus dos ficheros. Lo que la vuelta movio desde mi
acta (`658d4018`), con quien lo escribio; las `45` de fila van aparte, por su asunto:

    $ cat .v77aud/normal/censo_git.txt
    $ git log --format="%h %an %cI %s" 658d4018..78ed0408 | grep -v ", fila [0-9]*: " | cut -c1-140
    78ed0408 alexcat84 2026-09-26T13:07:30-04:00 Apertura ciega de la vuelta 1, sellada antes de exponer el reporte
    a70bdf05 alexcat84 2026-09-26T12:55:29-04:00 Vuelta 77: la salida del hook del commit del cierre
    b2d27bbc alexcat84 2026-09-26T12:54:18-04:00 Vuelta 77, T5: el cierre (censo 459, 1172, 1, 0, 22; 8 PUENTE marcados y 0 que entraron; gate, 
    bd29146f alexcat84 2026-09-26T12:38:14-04:00 Vuelta 77, T4 cerrada: las 22 de Gerber dentro, las 10 aristas esperadas en el grafo por los do
    d967b0e4 alexcat84 2026-09-26T09:36:32-04:00 Vuelta 77, T3: las huellas de las 22, identicas a las de la 76; el censo antes de la TAREA 4
    e6f46ffb alexcat84 2026-09-26T09:33:46-04:00 Vuelta 77, T1 y T2: los registros de la ACTA 75 y la relectura conjunta (el par de la contratac
    70a827c9 alexcat84 2026-09-26T09:27:37-04:00 Vuelta 77: lo pendiente del arnes antes de tocar nada
    9fa5c94b alexcat84 2026-09-26T09:26:48-04:00 Paradas: el presupuesto baja a 6 plazas por la regla del fundador del 25 sep (mediana en uso 4,
    $ git log --format="%s" 658d4018..78ed0408 | grep -c ", fila [0-9]*: "
    45
    $ git diff --name-status 658d4018 a70bdf05 | grep -v "\.v77ext/" | awk '{print $1, $NF}' | sed "s|/[^/]*\.json$|/*.json|" | sort | uniq -c
          1 A docs/loop/paradas/2026-09-26-seis-plazas-NOTA.md
          1 M bitacora/VEREDICTOS.jsonl
          1 M censos/atribuciones.md
          1 M censos/denominaciones.md
          1 M dataset/nodos.jsonl
          2 M docs/loop/*.json
          1 M docs/loop/DEUDA.jsonl
          1 M docs/loop/loop.log
          1 M docs/loop/REPORTE.md
         22 R100 cuarentena/_insertados/gerber_emyth/*.json
    $ git diff --name-only a70bdf05 78ed0408
    docs/loop/APERTURA_CIEGA.md
    docs/loop/SELLOS_APERTURA.jsonl
    $ git log --format="%h %an" 658d4018..78ed0408 -- src tests scripts forja.py config esquema fuentes | wc -l
    0
    $ git status --short -- dataset bitacora censos config esquema fuentes src scripts tests cuarentena forja.py | wc -l
    0

**LECTURA:** **`9fa5c94b` no es del extractor**: es la nota de la sesion que opera la linea, commiteada con la linea parada a las
`09:26:48`, antes del primer commit del extractor, y solo anade su fichero de `docs/loop/paradas/`. **La vuelta movio lo que una
insercion mueve y nada mas**: el grafo, la bitacora, los dos `censos/` que la aduana escribe, las `22` fichas renombradas a
`_insertados` byte a byte (`R100`) y dos lineas de pago en `DEUDA.jsonl`; **ni `src/`, ni `tests/`, ni `scripts/`, ni `config/`**, y nada
queda sin commitear en el dato. Las dos lineas de `DEUDA.jsonl`, y ninguna borrada:

    $ cat .v77aud/normal/deuda_diff.txt
    $ git diff 658d4018 a70bdf05 -- docs/loop/DEUDA.jsonl | grep -c "^-{"
    0
    $ git diff 658d4018 a70bdf05 -- docs/loop/DEUDA.jsonl | grep "^+{" | grep -o '"id": "d[0-9]*", "linea": "[a-z]*", "tipo": "[a-z]*", "vuelta": "[0-9]*"'
    "id": "d111", "linea": "serial", "tipo": "pago", "vuelta": "77"
    "id": "d108", "linea": "serial", "tipo": "pago", "vuelta": "77"

**HEREDADO 1, `R5` del extractor: CUMPLIDO.** Con mis copias sacadas con `sed` de los originales `.v64ext/pegado64.py` y
`.v64aud/normal/bloques_mudos.py`, no de las suyas, con la cabecera cambiada a la `77`:

    $ cat .v77aud/normal/r5.txt
    $ diff --strip-trailing-cr .v64ext/pegado64.py .v77aud/normal/pegado77_aud.py | grep -c "^>"; diff --strip-trailing-cr .v64aud/normal/bloques_mudos.py .v77aud/normal/bloques_mudos77_aud.py | grep -c "^>"
    3
    2
    $ python .v77aud/normal/pegado77_aud.py; python .v77aud/normal/bloques_mudos77_aud.py
    bloques abiertos con `$` en el tramo de la vuelta 77 : 70
    bloques que ROMPEN R1 (ACTA 60 60.15)                : 0
    bloques abiertos con `$`: 47 | comandos `$`: 70 | comandos sin ninguna linea de salida en su bloque: 0

**Es lo que su `77.5.g` publica, al digito** (`70` comandos en `47` bloques, `0` y `0`). **HEREDADO 2, `R6`, y HEREDADO 3, `R7`, mios:
CUMPLIDOS** en la fase ciega (`APERTURA_CIEGA.md` `0` y `8`) **y `R7` en esta acta**: cada instrumento mio de este turno que reparte un
total en clases imprime su `suma` (el de `solape.py` la gano en este turno, antes de pegarlo). **HEREDADO 4, `R8`, mio: CUMPLIDO en el
encargo de la `77`** (`APERTURA_CIEGA.md` `6`) **y medido sobre el de la `78`** en `76.13`. **HEREDADO 5, `R9` del extractor: SIN
OBJETO EN ESTA VUELTA**: su letra es *si marca fidelidad sobre algo que la aduana levante en el acto*, y la aduana no levanto ningun
vecino fuera del barrido de la `76` (`76.4`), asi que no hubo nada que marcar; `.v77ext/` no tiene ningun fichero de fidelidad:

    $ ls .v77ext | grep -i -c "fidel"
    0

**HEREDADO 6, `R10`, mio: CUMPLIDO en el encargo de la `77`** (`APERTURA_CIEGA.md` `0`) **y en esta acta** (`76.14`).

## 76.1. **LO QUE VERIFICO, CON MIS PROPIOS COMANDOS** (`1.1`)

    $ cat .v77aud/normal/gate.txt .v77aud/normal/guiones.txt .v77aud/normal/resolutor.txt
    GATE VERDE.
      nodos verificados: 459
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece
    rc=0
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    rc=0
    nodos vivos: 459
    nodos deprecados (archivo): 0
    alias registrados: 0
    rc=0
    $ grep 'total:' .v77aud/normal/suite.txt; tail -1 .v77aud/normal/suite.txt; cat .v77aud/normal/suite_hora.txt
      total: 382 pruebas, 0 fallos, 0 errores
    rc=0
    INICIO SUITE 13:09:10
    FIN SUITE 13:13:12
    $ cat .v77aud/normal/censo.txt
    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        459 dataset/nodos.jsonl
       1172 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1632 total
    $ for d in cuarentena/gerber_emyth cuarentena/_insertados/gerber_emyth cuarentena/marquet_turn_the_ship; do echo "$d $(find $d -maxdepth 1 -name "*.json" 2>/dev/null | wc -l)"; done; echo "procesos $(ls -A procesos/ | wc -l)"
    cuarentena/gerber_emyth 0
    cuarentena/_insertados/gerber_emyth 22
    cuarentena/marquet_turn_the_ship 20
    procesos 0
    $ python .v70aud/poblacion.py
    poblacion: 479 | por sede: {'grafo': 459, 'bandeja': 20} | suma: 479

**LECTURA:** **el censo de su `77.5.a` al digito** (`459`, `1172`, `1`, `0`, `22`; poblacion `479`, `459` mas `20`) **y el de mi
apertura sellada** (`APERTURA_CIEGA.md` `2`). La suite cuenta `382`, lo mismo que su `77.5.e` y que mi `ACTA 75` `75.1`.

**EL CIERRE ESTRICTO, CORRIDO POR MI**, en serie despues de la suite, con `procesos/` vacio al terminar (bloque de arriba):

    $ grep -nE '^(CIERRE|CENSO|TALLADO|TABLA DE CIERRE)|DIFIEREN|CAEN  ' .v77aud/normal/cerrar_reporte.txt; tail -1 .v77aud/normal/cerrar_reporte.txt; cat .v77aud/normal/cerrar_hora.txt
    2:TALLADO DEL REPORTE (D.41): la tabla que dice ser de instrumento
    6:  que DIFIEREN de su instrumento: 0
    286:TALLADO VERDE: las 157 tabla(s) comprobables son las de su instrumento, celda a celda.
    288:CENSO DE RUTAS (D.42): la unidad de la ruta es la celda
    292:  CAEN                      : 0
    298:CENSO VERDE: las 1078 rutas publicadas sostienen lo que dicen sostener.
    300:TABLA DE CIERRE DE TAREAS (D.52): toda tabla del reporte declara su instrumento
    310:TABLA DE CIERRE VERDE: ninguna celda medible difiere del dato.
    489:CIERRE VERDE: las cuatro guardas que muerden, el tallado y el censo. La vigencia corrio y publico su cuenta arriba: es cola, no guarda (D.15).
    rc=0
    13:13:28
    13:17:56

**VERDE, `rc=0`.** Cuenta `1078` rutas contra `1074` de su corrida y `1079` de su hook: **no descompongo la diferencia**, el arbol no es
el mismo (despues entro mi apertura, sin tablas ni rutas de reporte), y ninguna cae.

**LO QUE REPRODUZCO DE SU TRAMO**, corriendo sus instrumentos contra sus salidas guardadas con `diff`. `orden.py` lee la bandeja, que hoy
esta vacia, asi que lo corro sobre el arbol de `d967b0e4` (la TAREA 3, antes del primer `insertar`) sacado con `git archive` a una
carpeta fuera del repositorio:

    $ grep -v "^\$ " .v77aud/normal/reproduce.txt
    aristas_vuelta.py: IDENTICO a .v77ext/aristas_vuelta.txt
    nodos_viejos.py: IDENTICO a .v77ext/nodos_viejos.txt
    pasos_inventados.py: IDENTICO a .v77ext/pasos_inventados.txt
    relojes.py: IDENTICO a .v77ext/relojes.txt
    censo.sh: IDENTICO a .v77ext/censo_cierre.txt
    pasos_y_huellas.py de hoy: IDENTICO a .v76ext/pasos_y_huellas.txt salvo la columna de la sede
         22 _insertados
          1 las
    orden.py sobre el arbol de d967b0e4 (T3, antes del primer insertar): IDENTICO a .v77ext/orden.txt

(Los comandos de cada linea estan en el propio fichero; la linea `1 las` es la de resumen de `pasos_y_huellas.py`, cuya tercera
columna no es una sede. `orden.py` sobre el arbol de hoy cae con `FileNotFoundError` por la bandeja vacia, y por eso lo corro sobre
`d967b0e4`.) **Las huellas de hoy de las
`22` son las de `.v76ext/pasos_y_huellas.txt` salvo la columna de la sede**, que es lo que su `77.5.a` publica, y lo que mi apertura
midio por otro camino (`APERTURA_CIEGA.md` `2`, `huellas_hoy.py`).

## 76.2. **EL REPORTE, AFIRMACION POR AFIRMACION** (`5.2`)

| afirmacion del reporte | sale | sede | especie |
|---|---|---|---|
| cabecera y tablas de tareas: `T2` de `8` a `10` aristas; `T4` `22` insertadas, `54` lineas, `10` aristas; `T5` el censo al abrir y al cerrar, `8` PUENTE marcados y `0` que entraron | **cierta, celda a celda** (`76.1`, `76.4`, `76.6`) | TABLA y CABECERA | |
| `77.0`: `70a827c`, gate con `437`, el censo, `LIBRE` con `52` deudas, poblacion `479`, `0` retiradas vivas, huellas identicas | **cierta** (`76.0`; el hash, en `censo_git.txt`) | bloque | |
| `77.1`: la cifra buena de la `76`, `8` de `176` | **cierta** (`ACTA 75` `75.2`) | bloque y tabla | |
| `77.D`: `D77.1` a `D77.3`, marcados antes de insertar | **cierta**: su commit es `e6f46ffb`, de las `09:33:46`, antes del primer arranque (`76.4`) | tabla | |
| `77.2`: los pasos de los cuatro nodos, las lineas del libro con su `grep`, la decision en las dos piezas y el `diff` de su orden | **cierta** (`76.3`; `orden.py` reproducido, `76.1`) | bloques y prosa | |
| `77.2.2`: *el barrido no levanta el par en ningun sentido*, `0` vecinos de `fingir` | **cierta** (`76.3`, `vecinos_par_d29.txt`) | prosa | |
| `77.3`: huellas identicas a las de la `76`, `22` fichas, `176` pasos, `16` iguales a su blob de `2407dbb` y `6` distintas | **cierta** (`76.1`; las `6` son las que la `76` corrigio, `ACTA 75` `75.1`) | bloque | |
| `77.4`: las `22` filas, su aduana, su comparacion con la `76`, sus lineas, sus aristas, su commit y la bitacora de cada fila | **cierta, fila a fila** (`76.4`) | tablas, bloques y prosa | |
| `77.4.5` y la fila `19`: los pagos de `d111` y `d108`, de `52` a `50` deudas | **cierta** (`76.0`, `76.3`) | bloques | |
| `77.4.6`: `61` registros, `13` con arista, `10` distintas y en el grafo, `0` sin veredicto; `437` viejos sin cambio y `22` nuevos | **cierta** (`76.4`) | bloques y prosa | |
| `77.5.a`: la tabla del censo; `22` `R100` y `4` `M`; `19` y `3` escrituras de `censos/`, las `3` en las filas `9`, `10` y `11` | **cierta** (`76.0`; las escrituras de `censos/`, contadas con `grep` sobre `.v77ext/insertar_*.txt`) | tabla y bloques | |
| `77.5.b`: la tabla de pasos inventados, `8` marcados y `0` que entraron | **cierta** (reproducida, `76.1`; mia, `76.6`) | bloque y tabla | |
| `77.5.c`: `D77.1` a `D77.4` ejecutados o cerrados | **cierta** (`76.3`, `76.4`) | tabla | |
| `77.5.d`: `22` relojes, mediana `419,2` s; las filas `8` y `21` por encima de `580` s | **cierta** (reproducida, `76.1`; `598,4` y `782,4` s son los dos unicos por encima, `76.4`) | bloque y prosa | |
| `77.5.e` a `77.5.g`: guardas, suite, cierre estricto, su primer rojo declarado, `R5`, y los `1079` del hook | **cierta** (`76.0`, `76.1`; el hook, en `.v77ext/hook_t5.txt`) | bloques | |

**NINGUNA CAIDA DE `REPORTE`.** Lo que mire para ver si alguna celda de prosa escondia una cifra de teclado, que es donde vivio su
ultima caida (`ACTA 75` `75.2`): las dos tablas de tareas, la del censo y la del `D.61`, cada celda contra su instrumento; los ordinales
*primera* a *decima* de las `10` aristas contra el orden de las filas (`6`, `8`, `9`, `12`, `13`, `18`, `19`, `20`, `20` y `22`); y las
cifras de las copias (`3` y `2` lineas en `R5`; el `diff` de `insertar.py`, `contra_barrido.py` y `censo.sh` contra sus originales, que
cambia solo rutas, rotulos y comentarios). **La mediana de `77.5.d` es la de su instrumento** (el elemento `12` de los `22` ordenados,
que el propio `relojes.py` declara en su cabecera), no la media de los dos centrales; **no es cifra falsa** porque el instrumento dice cual
imprime.

## 76.3. **LA RELECTURA CONJUNTA Y SUS DISCUTIBLES, ADJUDICADOS** (`1.3`, `6.1`)

| | su marca | adjudico |
|---|---|---|
| `D77.1` | el par de la contratacion pasa a `CONTINUA`, madre `construir_estrategia_gente_cuatro_componentes` | **SE SOSTIENE: ES MI LECTURA DE LA `ACTA 75` `75.4`**, que mantuve en mi fase ciega con los pasos delante (`APERTURA_CIEGA.md` `5`). Su razon nueva no copia la mia: la madre compone el Objetivo Estrategico, la Organizational Strategy y el Position Contract (`L119`) y los pasos `10` y `11` del hijo los entregan y los repasan (`L267`, `L269`); *sin la madre hecha, esos dos pasos no se pueden ejecutar*. **Su duda** (`2` de `12` pasos consumen el producto) **la resuelve `6.1` sin bascula**, como el mismo escribe. Las dos lineas en la bitacora son `CONTINUA` y la arista vive por la aduana (`76.4`) |
| `D77.2` | la arista `fingir_prototipo_cinco_mil_replicas` a `recorrer_siete_pasos_programa_desarrollo_negocio` por `D.29`, veredicto de la lectura `CONTINUA`, paso `1` | **SE SOSTIENE ENTERA**: la arista, el paso y el veredicto. **El paso `1`** es el que la condicion del hijo cita con sus palabras (*cuando ya finges*, `cap_11` `L35`), y es el que mi lectura ciega nombro; el `4` (*juega con las reglas*) es de la serie de las seis, que el hijo no continua. **El veredicto `CONTINUA`** es el de la lectura (`D.53`): el hijo parte del producto de la madre, y no hay linea de aduana que lo diga porque el barrido no levanta el par (`vecinos_par_d29.txt`, abajo) |
| `D77.3` | el metodo de espera de la `75` | **SE SOSTIENE**: `22` arranques, cada uno despues del `.fin` y del commit de la fila anterior, y el primero despues del commit de la TAREA `2` (`76.4`) |
| `D77.4` | la `cita_del_veredicto` de la arista `fingir` a `recorrer` dice *adjudicada en la ACTA 75 seccion 75.4* | **SE SOSTIENE SU DECLARACION, Y LA CITA QUEDA CIERTA DESDE ESTA ACTA. SIN ESPECIE.** La `75.4` es donde se escribio la lectura que gano y desde donde la mande a la conjunta; **esta acta la adjudica tal como la `75.4` la escribio**, asi que la cita apunta a la sede de la lectura adjudicada, que es lo que la `ACTA 69` sostuvo en `D70.3` (*son las secciones donde se adjudicaron y donde la conjunta las dejo*). **La lectura contraria, escrita**: `DATO MOVIDO`, porque la bitacora gano una palabra adelantada un acta. **No la elijo**: `DATO MOVIDO` es una operacion que mueve el dato sin veredicto mal puesto, y aqui la operacion es la mandada, el veredicto es el bueno, y la palabra no mueve ninguna cifra ni ninguna clase; y lo declaro el antes de que nadie lo leyera |

    $ cat .v77aud/normal/vecinos_par_d29.txt
    fingir_prototipo_cinco_mil_replicas 0 []
    recorrer_siete_pasos_programa_desarrollo_negocio 1 ['construir_estrategia_gente_cuatro_componentes']

**LA CONJUNTA, CERRADA SIN DISCREPANCIA:** las dos piezas las decidio el extractor por la vara `6.1` con los pasos delante, en el
sentido de mi lectura; **no hay caida de nadie**, porque las lineas preparadas de la `76` vivian en `.v76ext/`, que no es sede de
`CLASE` (`ACTA 75` `75.4`), y la bitacora solo tiene las corregidas (`76.4`). Las aristas esperadas pasan de `8` a `10`, que es lo que la
`75.4` dijo antes.

**LOS DOS PAGOS, FIRMADOS**, con su `--como` leido entero en `DEUDA.jsonl` (lineas `181` y `182`):

- **`d111`**: la arista `recorrer` a `construir` vive (`76.4`), con el paso `8` de la cabeza; *la cabeza entra con una parte de
  siete* es lo que la `75.4` adjudico, y el reparto de las otras seis es el de la ficha de `d111` (partes `1` y `2` por la `ACTA G5`
  `6.2`, `3` y `4` sin candidato, la `6` apartada en el reservado, que el tablero da `ANULADO`) mas `D76.13` para la `7`. **FIRMO.**
- **`d108`**: la ficha `responder_8_preguntas_construir_primary_aim` entro con la huella de la `76` (`76.1`), sin segundo nodo; la razon
  del pago (`L27` y `L117` son el mismo cuestionario del mismo Primary Aim) es la que la ficha de `d108` escribio como la que el
  auditor de la `ACTA G4` si daba, y la que mi `75.4` firmo. **FIRMO.**

**`d098` y `d104` siguen vivas**, como el encargo pedia (`APERTURA_CIEGA.md` `2`, `deudas_encargo.py`).

## 76.4. **LAS LINEAS, LAS ARISTAS, EL ORDEN Y LOS `insertar`, UNA A UNA** (`APERTURA_CIEGA.md` `7`, puntos `2` a `4` y `6`)

**Las `61` lineas nuevas de la bitacora, una a una**, contra su sede de lineas (`.v77ext/veredictos_listos.txt`, sin las `#`), contra las
filas dirigidas de mi barrido de la `76` y contra mis clases selladas con la adjudicacion `(i)` de la `75.4` y la conjunta como la gane;
y las de arista, contra sus filas `SOSTENGO`:

    $ python .v77aud/normal/bitacora_tanda.py
    (1) lineas desde la 1112: 61 | por tipo: {'veredicto de insertar': 54, 'arista por lectura': 7} | suma: 61
    (2) lineas de veredicto contra su sede: {'igual en clase y razon': 54} | suma: 54 | distintas: []
        lineas de la sede sin linea en la bitacora: 0
        filas dirigidas: bitacora 54 (distintas 54) | mi barrido 54 | iguales: SI
    (3) contra mis clases selladas (con 75.4 (i) y la conjunta como la mantengo): {'mi clase y madre': 54} | suma: 54 | distintas: []
        lineas de veredicto por clase: {'SANO': 48, 'CONTINUA': 6} | suma: 54
          CONTINUA cambiar_saludo_cliente_dos_ramas ~ cuantificar_impacto_innovacion_6_pasos | arista: cambiar_saludo_cliente_dos_ramas > cuantificar_impacto_innovacion_6_pasos
          CONTINUA cuantificar_impacto_innovacion_6_pasos ~ cambiar_saludo_cliente_dos_ramas | arista: cambiar_saludo_cliente_dos_ramas > cuantificar_impacto_innovacion_6_pasos
          CONTINUA aplicar_seis_pasos_sistema_venta ~ medir_sistema_venta_trece_indicadores_benchmark | arista: aplicar_seis_pasos_sistema_venta > medir_sistema_venta_trece_indicadores_benchmark
          CONTINUA medir_sistema_venta_trece_indicadores_benchmark ~ aplicar_seis_pasos_sistema_venta | arista: aplicar_seis_pasos_sistema_venta > medir_sistema_venta_trece_indicadores_benchmark
          CONTINUA construir_estrategia_gente_cuatro_componentes ~ aplicar_cinco_pasos_proceso_contratacion | arista: construir_estrategia_gente_cuatro_componentes > aplicar_cinco_pasos_proceso_contratacion
          CONTINUA aplicar_cinco_pasos_proceso_contratacion ~ construir_estrategia_gente_cuatro_componentes | arista: construir_estrategia_gente_cuatro_componentes > aplicar_cinco_pasos_proceso_contratacion
        SANO      paso  5 | fingir_prototipo_cinco_mil_replicas > dar_valor_constante_cuatro_publicos | fila SOSTENGO paso 5
        SANO      paso  6 | fingir_prototipo_cinco_mil_replicas > operar_modelo_gente_destreza_minima | fila SOSTENGO paso 6
        SANO      paso 10 | fingir_prototipo_cinco_mil_replicas > unificar_color_forma_vestuario_modelo | fila SOSTENGO paso 10
        CONTINUA  paso  1 | fingir_prototipo_cinco_mil_replicas > recorrer_siete_pasos_programa_desarrollo_negocio | fila SOSTENGO paso 1
        SANO      paso  8 | recorrer_siete_pasos_programa_desarrollo_negocio > construir_estrategia_gente_cuatro_componentes | fila SOSTENGO paso 8
        SANO      paso  8 | fingir_prototipo_cinco_mil_replicas > documentar_trabajo_manual_operaciones | fila SOSTENGO paso 8
        SANO      paso  5 | construir_estrategia_gente_cuatro_componentes > documentar_trabajo_manual_operaciones | fila SOSTENGO paso 5
    (4) aristas por lectura: 7 | {'con su fila SOSTENGO y su paso': 7} | suma: 7 | filas SOSTENGO en la sede: 7

**Las aristas del grafo con algun extremo en las `22`, con sus ids y por los dos lados**, contra las `10` que mi apertura sello; y los
nodos viejos, linea a linea contra el grafo de `70a827c9`:

    $ python .v77aud/normal/aristas_grafo.py
      aplicar_seis_pasos_sistema_venta                 > medir_sistema_venta_trece_indicadores_benchmark        | en la madre: SI | en el hijo: SI | esperada: SI
      cambiar_saludo_cliente_dos_ramas                 > cuantificar_impacto_innovacion_6_pasos                 | en la madre: SI | en el hijo: SI | esperada: SI
      construir_estrategia_gente_cuatro_componentes    > aplicar_cinco_pasos_proceso_contratacion               | en la madre: SI | en el hijo: SI | esperada: SI
      construir_estrategia_gente_cuatro_componentes    > documentar_trabajo_manual_operaciones                  | en la madre: SI | en el hijo: SI | esperada: SI
      fingir_prototipo_cinco_mil_replicas              > dar_valor_constante_cuatro_publicos                    | en la madre: SI | en el hijo: SI | esperada: SI
      fingir_prototipo_cinco_mil_replicas              > documentar_trabajo_manual_operaciones                  | en la madre: SI | en el hijo: SI | esperada: SI
      fingir_prototipo_cinco_mil_replicas              > operar_modelo_gente_destreza_minima                    | en la madre: SI | en el hijo: SI | esperada: SI
      fingir_prototipo_cinco_mil_replicas              > recorrer_siete_pasos_programa_desarrollo_negocio       | en la madre: SI | en el hijo: SI | esperada: SI
      fingir_prototipo_cinco_mil_replicas              > unificar_color_forma_vestuario_modelo                  | en la madre: SI | en el hijo: SI | esperada: SI
      recorrer_siete_pasos_programa_desarrollo_negocio > construir_estrategia_gente_cuatro_componentes          | en la madre: SI | en el hijo: SI | esperada: SI
    aristas con extremo en las 22: 10 | por los dos lados: 10 | esperadas: 10 | esperadas presentes: 10 | no esperadas: 0
    grafo al abrir la 77: 437 | hoy: 459 | viejos que faltan hoy: 0 | viejos que cambian: 0 [] | nuevos: 22 | nuevos que son las 22: SI
    las 22 ultimas filas del fichero, en su orden: 1:hacer_trabajo_futu 2:dictar_ritmo_creci 3:construir_empresa_ 4:trazar_modelo_nego 5:fingir_prototipo_c 6:dar_valor_constant 7:interrogar_negocio 8:operar_modelo_gent 9:unificar_color_for 10:cambiar_saludo_cli 11:probar_traje_azul_ 12:cuantificar_impact 13:recorrer_siete_pas 14:responder_8_pregun 15:responder_4_pregun 16:distinguir_tres_ti 17:aplicar_seis_pasos 18:medir_sistema_vent 19:construir_estrateg 20:documentar_trabajo 21:aplicar_ocho_regla 22:aplicar_cinco_paso

**Los `insertar`, uno por vez**: el arranque de cada uno es su fin menos su duracion, leidos de la ultima linea de su salida; las horas
de commit, de `git log`:

    $ python .v77aud/normal/solape.py | sed -n '1p;$p'; python .v77aud/normal/solape.py | tail -2 | head -1
    commit de T1 y T2: 09:33:46 | de T3: 09:36:32 | arranque del insertar 1: 09:37:06 | despues de los dos: SI
    ficheros .fin: 22 | su contenido: ['0']
    insertar: 22 | codigos: {'0': 22} | suma: 22 | con solape o sin commit antes del siguiente: 0

(Las `22` filas, con su arranque, su fin, sus commits y si el siguiente arranca despues, en `.v77aud/normal/solape.txt`.) **Y la
bitacora de cada fila en el ultimo commit de su fila, contra la cifra *Bitacora de X a Y* de su nota**, por `.v77aud/normal/por_fila.sh`:

    $ cut -d' ' -f2,4- .v77aud/normal/por_fila.txt
    1 grafo 438 bitacora 1112 | el reporte: Bitacora de 1111 a 1112
    2 grafo 439 bitacora 1120 | el reporte: Bitacora de 1112 a 1120
    3 grafo 440 bitacora 1121 | el reporte: Bitacora de 1120 a 1121
    4 grafo 441 bitacora 1122 | el reporte: Bitacora de 1121 a 1122
    5 grafo 442 bitacora 1122 | el reporte: Bitacora sin movimiento: 1122
    6 grafo 443 bitacora 1126 | el reporte: Bitacora de 1122 a 1126
    7 grafo 444 bitacora 1127 | el reporte: Bitacora de 1126 a 1127
    8 grafo 445 bitacora 1132 | el reporte: Bitacora de 1127 a 1132
    9 grafo 446 bitacora 1135 | el reporte: Bitacora de 1132 a 1135
    10 grafo 447 bitacora 1141 | el reporte: Bitacora de 1135 a 1141
    11 grafo 448 bitacora 1144 | el reporte: Bitacora de 1141 a 1144
    12 grafo 449 bitacora 1149 | el reporte: Bitacora de 1144 a 1149
    13 grafo 450 bitacora 1151 | el reporte: Bitacora de 1149 a 1151
    14 grafo 451 bitacora 1152 | el reporte: Bitacora de 1151 a 1152
    15 grafo 452 bitacora 1154 | el reporte: Bitacora de 1152 a 1154
    16 grafo 453 bitacora 1157 | el reporte: Bitacora de 1154 a 1157
    17 grafo 454 bitacora 1159 | el reporte: Bitacora de 1157 a 1159
    18 grafo 455 bitacora 1161 | el reporte: Bitacora de 1159 a 1161
    19 grafo 456 bitacora 1166 | el reporte: Bitacora de 1161 a 1166
    20 grafo 457 bitacora 1170 | el reporte: Bitacora de 1166 a 1170
    21 grafo 458 bitacora 1170 | el reporte: Bitacora sin movimiento: 1170
    22 grafo 459 bitacora 1172 | el reporte: Bitacora de 1170 a 1172

**LECTURA:**

- **Las `54` lineas de veredicto son las preparadas letra a letra** (clase y razon), **las `54` filas dirigidas de mi barrido** y **mis
  clases selladas, las `54`**: `48` `SANO` y `6` `CONTINUA`, que son las `6` que mi apertura esperaba (`APERTURA_CIEGA.md` `4`). **El par
  de la contratacion entro por el primer camino que mi apertura dejo abierto**, la linea `CONTINUA` con `madre=`, y no por un `SANO` mas
  una arista por lectura: la bitacora no tiene la linea de mas que el segundo camino daria.
- **Las `7` de arista son las `7` filas `SOSTENGO` de su sede, con su paso**, y su veredicto es el de la lectura: `SANO` en las seis de
  `D.37` y `CONTINUA` en la de `D.29` (`76.3`).
- **Las `10` aristas de la tanda son mis `10`, por los dos lados, y ninguna de mas**; **los `437` nodos viejos, linea a linea iguales** a
  los del grafo de la apertura: ninguna madre de la tanda es vieja, y ningun nodo viejo gano ni un id.
- **Los `22` entraron en el orden de `.v76ext/orden.txt`**, que es el de mi encargo (`APERTURA_CIEGA.md` `4`), **uno por vez**: cada uno
  arranco despues del `.fin` y del ultimo commit de la fila anterior, el primero despues del commit de la TAREA `2`, y los `22` volvieron
  con `0`. **Ninguna aduana levanto un vecino fuera del barrido de la `76`**: las `22` comparaciones de su `77.4` dicen *nuevos hoy: 0* y
  *que ya no levantan: 0*, y las vuelvo a correr hoy, las `22`:

      $ for f in .v77ext/insertar_*.txt; do n=$(basename $f .txt | cut -d_ -f2); id=$(basename $f .txt | cut -d_ -f3-); python .v77ext/contra_barrido.py $n $id; done | grep -c "nuevos hoy: 0 | que ya no levantan: 0 | con senial distinta: 0"
      22

  **La bitacora de cada fila es la de su nota** (columna `bitacora` contra *el reporte*, fila a fila).

## 76.5. **LA RELECTURA: LA MUESTRA PINEADA DE LOS SANO** (`1.2`, `5.1`, `7`)

**Los discutibles marcados** son los cuatro de `76.3`, adjudicados arriba. **LA MUESTRA**, semilla `77` registrada en mi fase ciega
(`APERTURA_CIEGA.md` `7`, punto `5`); el tamanio es el mayor entre `3` y el `20` por ciento redondeado hacia arriba, con techo de `20`, y
la poblacion es la de las actas anteriores, toda linea `SANO` que la vuelta anadio, las de arista `D.37` incluidas:

    $ python .v77aud/normal/muestra_sano.py
    lineas de la 77: 61 | SANO: 54 | muestra: 11 | semilla 77
    linea 1119  dictar_ritmo_crecimiento_preguntas_escritas | cambiar_saludo_cliente_dos_ramas
    linea 1124  dar_valor_constante_cuatro_publicos | documentar_trabajo_manual_operaciones
    linea 1127  interrogar_negocio_cinco_preguntas | dictar_ritmo_crecimiento_preguntas_escritas
    linea 1128  operar_modelo_gente_destreza_minima | interrogar_negocio_cinco_preguntas
    linea 1130  operar_modelo_gente_destreza_minima | dictar_ritmo_crecimiento_preguntas_escritas
    linea 1132  operar_modelo_gente_destreza_minima | fingir_prototipo_cinco_mil_replicas
    linea 1143  probar_traje_azul_seis_semanas | cambiar_saludo_cliente_dos_ramas
    linea 1149  cuantificar_impacto_innovacion_6_pasos | entregar_evaluacion_desempeno_tres_claves
    linea 1154  responder_4_preguntas_estandares_objetivo_estrategico | probar_traje_azul_seis_semanas
    linea 1168  documentar_trabajo_manual_operaciones | unificar_color_forma_vestuario_modelo
    linea 1169  documentar_trabajo_manual_operaciones | fingir_prototipo_cinco_mil_replicas

**PRIMERO LOS PASOS, DESPUES SU RAZON.** Los de los once nodos, en `.v77aud/normal/pasos_muestra.txt` por `pasos_ciego.py`, y los de
`fingir`, en mi `APERTURA_CIEGA.md` `5`. **Mi lectura, escrita antes de destapar:**

- `1119`, `1127` y `1130`: **SANO los tres.** Dictar el ritmo de crecimiento con tres conocimientos y un plan escrito (`cap_07`) contra un
  saludo con dos ramas, cinco preguntas para trabajar sobre el negocio y la regla `2` del prototipo: todos preguntan o planifican, y
  ninguno usa el producto de otro.
- `1124` y `1168`: **SANO**, hermanos: reglas `1`, `4` y `6` de la misma cabeza; ninguna parte continua a otra parte.
- `1128`: **SANO.** La segunda pregunta de `interrogar` (*que mi gente trabaje sin mi interferencia*) toca el tema de la regla `2` pero no
  nombra la destreza minima ni el sistema de herramientas.
- `1132` y `1169`: **SANO con arista `D.37`**, pasos `6` y `8` de la cabeza (`D.53`).
- `1143`: **SANO**, hermanos de `cap_12`: dos innovaciones distintas, el test del traje y el saludo; ninguna mide ni usa la otra.
- `1149`: **SANO**, ajenos: una innovacion cuantificada contra la entrega de una evaluacion de Grove.
- `1154`: **SANO**: el paso `5` de `responder_4` nombra el vestuario como estandar, y nombrar no es procedimentar la prueba del traje.

Destapadas despues (`.v77aud/normal/razones_muestra.txt`): **las once razones dicen lo mismo con el libro citado.**

    $ python .v77aud/normal/banda_muestra.py
    SANO de la vuelta: 54 | sin razon escrita: 0
    releidos 11 | se sostienen 11 | caen 0 | tasa 0.0 por ciento | banda Wilson 95: 0.0 a 25.9 por ciento

**DENTRO CONTRA FUERA DEL MARCADO:** cuatro marcados, cuatro se sostienen; **fuera del marcado**, las `11` de la muestra y las `54` lineas
contra mis clases selladas, **ninguna cae**. **LA RELECTURA AL DOBLE** no aplica: ninguna caida de `REPORTE` en el tramo (`76.2`).

## 76.6. **LA FIDELIDAD Y `PASOS INVENTADOS POR CAPITULO`, DE LO QUE ENTRO** (`D.30`, `D.58`, `8`, `8.2`, `8.3`)

**La relectura de fidelidad de `D.58` sobre lo que entra es mi lectura entera de la `76`**, firmada en la `ACTA 75` `75.3`), porque lo que
entro es byte a byte lo que lei; lo mido otra vez hoy contra el grafo:

    $ python .v77aud/entra_lo_leido.py
    las 22 por sede hoy: {'grafo y _insertados': 22} | suma: 22
    nodos del grafo contra su ficha, cinco campos: {'igual': 22} | suma: 22
    nodos con descuadre entre sus pasos en el grafo y mis filas selladas: 0 []
    cap_04 lo que ENTRO: candidatos 1 | pasos 7 | mis marcas: {'T': 7, 'P': 0, 'D': 0} | suma: 7 | PUENTE 0 de 7 = 0.00 por ciento
    cap_07 lo que ENTRO: candidatos 1 | pasos 8 | mis marcas: {'T': 8, 'P': 0, 'D': 0} | suma: 8 | PUENTE 0 de 8 = 0.00 por ciento
    cap_08 lo que ENTRO: candidatos 2 | pasos 17 | mis marcas: {'T': 17, 'P': 0, 'D': 0} | suma: 17 | PUENTE 0 de 17 = 0.00 por ciento
    cap_11 lo que ENTRO: candidatos 6 | pasos 57 | mis marcas: {'T': 57, 'P': 0, 'D': 0} | suma: 57 | PUENTE 0 de 57 = 0.00 por ciento
    cap_12 lo que ENTRO: candidatos 3 | pasos 12 | mis marcas: {'T': 11, 'P': 0, 'D': 1} | suma: 12 | PUENTE 0 de 12 = 0.00 por ciento
    cap_13 lo que ENTRO: candidatos 1 | pasos 10 | mis marcas: {'T': 10, 'P': 0, 'D': 0} | suma: 10 | PUENTE 0 de 10 = 0.00 por ciento
    cap_14 lo que ENTRO: candidatos 1 | pasos 9 | mis marcas: {'T': 9, 'P': 0, 'D': 0} | suma: 9 | PUENTE 0 de 9 = 0.00 por ciento
    cap_15 lo que ENTRO: candidatos 1 | pasos 5 | mis marcas: {'T': 5, 'P': 0, 'D': 0} | suma: 5 | PUENTE 0 de 5 = 0.00 por ciento
    cap_18 lo que ENTRO: candidatos 3 | pasos 26 | mis marcas: {'T': 26, 'P': 0, 'D': 0} | suma: 26 | PUENTE 0 de 26 = 0.00 por ciento
    cap_19 lo que ENTRO: candidatos 3 | pasos 25 | mis marcas: {'T': 25, 'P': 0, 'D': 0} | suma: 25 | PUENTE 0 de 25 = 0.00 por ciento
    los diez: candidatos 22 | pasos 176 | mis marcas: {'T': 175, 'P': 0, 'D': 1} | suma: 176 | PUENTE 0 de 176 | con la D adjudicada T (ACTA 75 75.3): T 176, P 0, suma 176

| capitulo | que es | candidatos que entraron | pasos | PUENTE marcados en la preparacion | por ciento | PUENTE que entro |
|---|---|---:|---:|---:|---:|---:|
| `cap_04` | *The Entrepreneur the Manager, and the Technician* | `1` | `7` | `0` | `0,00` | `0` |
| `cap_07` | *Beyond the Comfort Zone* | `1` | `8` | `1` | `12,50` | `0` |
| `cap_08` | *Maturity and the Entrepreneurial Perspective* | `2` | `17` | `0` | `0,00` | `0` |
| `cap_11` | *Working On Your Business, Not In It* | `6` | `57` | `1` | `1,75` | `0` |
| `cap_12` | *The Business Development Process* | `3` | `12` | `4` | `33,33` | `0` |
| `cap_13` | *Your Business Development Program* | `1` | `10` | `0` | `0,00` | `0` |
| `cap_14` | *Your Primary Aim* | `1` | `9` | `0` | `0,00` | `0` |
| `cap_15` | *Your Strategic Objective* | `1` | `5` | `0` | `0,00` | `0` |
| `cap_18` | *Your People Strategy* | `3` | `26` | `2` | `7,69` | `0` |
| `cap_19` | *Your Systems Strategy* | `3` | `25` | `0` | `0,00` | `0` |
| **el lote** | | **`22`** | **`176`** | **`8`** | **`4,55`** | **`0`** |

**LECTURA:** **la columna que manda es la ultima: `0` PUENTE entro en los diez capitulos**, que es lo que la `ACTA 75` `75.3` firmo
*que entrara*. Las columnas de marca son las de su `77.5.b`, reproducida (`76.1`), y las de mi `ACTA 75` `75.3`; los titulos, de alli.
**El peor capitulo de la preparacion es `cap_12`, *The Business Development Process***, con `4` de `12`, releido entero en la `76` por el
y por mi. **No dimensiona nada**: no queda lote de extraccion en el mundo `11` (`PARALELO.md` seccion `8` punto `3`).

## 76.7. **LAS CUATRO GUARDAS DE DATO** (`D.55`)

| guarda | estado | medida |
|---|---|---|
| `gate` | **VERDE** | `76.1` |
| el cerrojo (`D.44`) | **VERDE**: los `22` `insertar` uno por vez, `procesos/` vacio | `76.1`, `76.4` |
| censo no decreciente | **VERDE**: `437` a `459` y `1111` a `1172`; ningun nodo viejo falta | `76.1`, `76.4` |
| fidelidad `D.30` con puente | **VERDE**: `0` PUENTE entro | `76.6` |

**Ninguna en rojo: esta acta no deja tarea bloqueante** (`D.55`).

## 76.8. **EL CREDITO DE LA LINEA `serial`** (`5.3`, `D.48`)

Al abrir, y despues de anotar mi tanda:

    $ sed -n '5,12p' .v77aud/normal/credito_abrir.txt
      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA 75
      CIFRA PUBLICADA    0 de 2     ACTA 75
      CLASE              0 de 2     ACTA 75
      DATO MOVIDO        0 de 2     ACTA 75
      REPORTE            1 de 3     ACTA 75
    
    $ python forja.py credito | sed -n "5,11p"
      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA 76
      CIFRA PUBLICADA    0 de 2     ACTA 76
      CLASE              0 de 2     ACTA 76
      DATO MOVIDO        0 de 2     ACTA 76
      REPORTE            0 de 3     ACTA 76

| especie | tanda `ACTA 76` | racha | el motivo, medido |
|---|---|---|---|
| **`CLASE`** | **LIMPIA** | `0 de 2` | las `54` lineas son mis clases selladas y las `7` de arista sus filas `SOSTENGO` (`76.4`); la conjunta, sin discrepancia (`76.3`); la muestra `11` de `11` (`76.5`) |
| **`CIFRA PUBLICADA`** | **LIMPIA** | `0 de 2` | no escribio en `docs/` fuera de `docs/loop/`, ni en `config/`, `esquema/` ni `src/` (`76.0`) |
| **`DATO MOVIDO`** | **LIMPIA** | `0 de 2` | movio lo que la insercion manda y nada mas; ningun nodo viejo cambia (`76.0`, `76.4`); `D77.4` sin especie (`76.3`) |
| **`REPORTE`** | **LIMPIA** | **`0 de 3`** | `76.2`: ninguna cifra falsa en tabla, cabecera ni conclusion; **la racha vuelve a cero** por `5.4` |
| **`AUDITOR`** | **LIMPIA** | `0 de 3` | `76.10`: ninguna cifra mia falsa ni remedio roto |

## 76.9. **EL COSTE** (`D.55`)

    $ cat .v77aud/normal/coste.txt
    $ python .v77aud/normal/coste.py
    ultimo_extractor.json | USD 9.73 | 775 s de API | turnos 179 | entrada 294 | cache escrita 285707 | cache leida 28779007 | salida 84499 (pensamiento 15456)
    ultimo_apertura.json | USD 4.87 | 567 s de API | turnos 50 | entrada 98 | cache escrita 259126 | cache leida 7754353 | salida 62244 (pensamiento 21040)
    $ grep "extractor listo\|auditor ciego listo" docs/loop/loop.log | tail -2
    [2026-09-26 12:56:09] extractor listo (USD 9.732613400000002), 12547s, intento 1 de 7
    [2026-09-26 13:07:10] auditor ciego listo (USD 4.869150600000001), 659s, intento 1 de 7

**Ninguno de los dos turnos pasa de `10` USD: no hay desglose que declarar.** El del extractor duro mas de tres horas de reloj por los
`22` `insertar` en serie (`2,61` h de aduana, su `77.5.d`), y costo menos que el de la `76` (`ACTA 75` `75.8`).

## 76.10. **MI PROPIA TANDA** (`D.38.2`)

**LAS CIFRAS DE MI APERTURA SELLADA, CONTRA LO MEDIDO HOY:** el censo, la poblacion y el tablero (`76.1`, `76.11`); las `22` movidas con
su huella y los `437` viejos intactos (`76.1`, `76.4`); los `0` PUENTE por capitulo (`76.6`); las `54` lineas esperadas, `6` y `48`, las
`7` de arista y la bitacora en `1172` (`76.4`); las `10` aristas (`76.4`); el orden y las `16` restricciones (el orden, `76.4`; las
restricciones no cambian con el); y los pagos de `d111` y `d108` en la `77` (`76.0`). **Todas cuadran.** **Ningun remedio mio roto**
(`76.0`).

**LO QUE MI APERTURA DIJO QUE PESABA, Y LO DIGO OTRA VEZ:** vi el nombre del fichero de la arista de `fingir` a `recorrer` antes de
releer esa pieza (`APERTURA_CIEGA.md` `1`). **Mi `SOSTENGO` era el de la `76` y el de la `ACTA 75`**, y el extractor la sostuvo por su
lado con su razon (`76.3`), asi que ese nombre no decidio nada que no estuviera ya escrito; **pero la duda que dejo en mi fase ciega
queda a la vista**, no absuelta.

**LO QUE MI APERTURA DIJO QUE HARIA EN EL TURNO NORMAL** (su seccion `7`, nueve puntos) **esta todo aqui**: `R5` y `R9` en `76.0`; la
conjunta en `76.3`; las lineas una a una en `76.4`; los `insertar` y su orden en `76.4`; la muestra en `76.5`; las aristas con sus ids en
`76.4`; los pagos en `76.3`; el censo con `git`, las guardas, el cierre estricto y el coste en `76.0`, `76.1`, `76.7` y `76.9`; `R8` y `R10`
en `76.13` y `76.14`.

## 76.11. **LAS CONDICIONES DE PARADA, UNA A UNA, Y EL LIBRO QUE SIGUE** (`3`, `D.32`, `D.49`)

| condicion | se cumple | como lo mido |
|---|---|---|
| doctrina nueva | **NO** | los discutibles los cubren `6.1`, `D.29`, `D.37`, `D.53` y el precedente `D70.3` (`76.3`) |
| contradiccion | **NO** | ninguna cifra ni clase contradice a otra (`76.2`, `76.4`) |
| decision de Alexis | **NO** | insertar Marquet esta ordenado (`PARALELO.md` seccion `8` punto `4`); el tag y la parada son de la vuelta que meta su ultima ficha |
| fallo tecnico repetido | **NO** | gate, guiones, suite y cierre estricto en verde (`76.1`) |
| credito roto | **NO** | las cinco rachas en cero (`76.8`) |
| campania consumada | **NO**: falta Marquet, abajo | |

    $ sed -n '11,13p;24p' .v77aud/normal/tablero.txt
      1    7    grove_high_output              INSERTADO              NINGUNO                  0  cap_18
      2    9    gerber_emyth                   INSERTADO              NINGUNO                  0  cap_22
      3    5    marquet_turn_the_ship          COSECHADO              NINGUNO                 20  cap_17
      MUNDO 11: faltan 1 de 7 libros del corte (marquet_turn_the_ship)
    $ cat .v77aud/normal/clase78.txt
    $ python scripts/deuda.py --clase 78
    LIBRE
      van 4 de 5 desde la ultima de saneamiento (la 74), con 50 deuda(s) esperando
    $ python forja.py tablero --puedo marquet_turn_the_ship
    LINEA 'serial', LIBRO 'marquet_turn_the_ship': SI
      'marquet_turn_the_ship' esta COSECHADO y sin dueño: su trabajo ya llego a esta rama, asi que se continua desde el capitulo siguiente al ultimo minado (cap_17), citando su frontera. D.50.
    $ python .v77aud/normal/bandeja_marquet.py | tail -2
    fichas por capitulo: {'cap_01': 1, 'cap_02': 2, 'cap_03': 6, 'cap_04': 1, 'cap_06': 2, 'cap_07': 1, 'cap_08': 1, 'cap_09': 1, 'cap_10': 1, 'cap_11': 1, 'cap_12': 1, 'cap_13': 1, 'cap_14': 1} | suma: 20
    pasos por capitulo: {'cap_01': 6, 'cap_02': 10, 'cap_03': 53, 'cap_04': 5, 'cap_06': 8, 'cap_07': 3, 'cap_08': 5, 'cap_09': 2, 'cap_10': 3, 'cap_11': 3, 'cap_12': 8, 'cap_13': 2, 'cap_14': 2} | suma: 110
    $ ls fuentes/marquet_turn_the_ship | wc -l; grep -c "marquet_turn_the_ship" fuentes/FUENTES_CANONICAS.json
    17
    2

**LECTURA:** **Gerber sale `INSERTADO`** y **el unico libro del corte que falta es Marquet**, `COSECHADO` con su bandeja llena. **Las dos
medidas de apertura de `D.32`, publicadas aunque ya no abran lote** (`PARALELO.md` seccion `8` punto `3`): su material esta en
`fuentes/marquet_turn_the_ship/` y su clave en la tabla canonica. **NO ESCRIBO `PARA_ALEXIS.md`.** **La `78` es LIBRE y prepara
Marquet**, como la `76` preparo Gerber: la fidelidad entera, el barrido, los veredictos, las aristas y el orden, **sin insertar**; su
bandeja, del bloque de arriba, tiene su mayor capitulo en `cap_03`. **Y LO DIGO PARA QUE NADIE SE SORPRENDA:** la cadencia hace de
saneamiento a la vuelta siguiente a la `78` (la ultima fue la `74`, y la `78` ya es la cuarta de cinco); la insercion de Marquet cae,
por eso, despues de esa:

    $ python scripts/deuda.py --clase 79
    SANEAMIENTO
      han pasado 5 vuelta(s) desde la ultima de saneamiento (la 74) y la cadencia es 5, con 50 deuda(s) pendientes

**Sin bloqueante.** La frase de *continuar desde `cap_17`* es de extraccion y no aplica.

**`d150`, de Marquet, entra en el encargo para prepararse** (su texto, pegado alli): pide la fila de fidelidad de `cap_03` que el frente
nunca publico bien, y la fidelidad entera de la `78` la da. Se paga en la vuelta que inserte.

## 76.12. **LOS REMEDIOS**

| # | de quien | remedio | donde se comprueba |
|---|---|---|---|
| `R5` | del extractor | **Sigue vivo con su letra**, cumplido de la `65` a la `77` | el reporte de la `78`, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera cambiada a la `78` |
| `R6` | del auditor | **Sigue vivo con su letra** | la apertura ciega de la `78` |
| `R7` | del auditor | **Sigue vivo con su letra** | la apertura ciega de la `78` y la `ACTA 77` |
| `R8` | del auditor | **Sigue vivo con su letra y su criterio**; instrumento de esta vuelta, `.v77aud/normal/r8_encargo78.py` | mi fase ciega de la `78`, sobre el encargo de la `78` (`76.13`); y el encargo de la `79` |
| `R9` | del extractor | **Sigue vivo con su letra**, y en la `78` tiene objeto: la vuelta marca fidelidad entera | el reporte de la `78`, en su cuenta de PUENTE |
| `R10` | del auditor | **Sigue vivo con su letra** | esta acta (`76.14`) y la `ACTA 77` |

## 76.13. **`R8` MEDIDO SOBRE MI ENCARGO DE LA `78`, ANTES DE CERRARLO** (`76.12`)

    $ python .v77aud/normal/r8_encargo78.py | tail -1
    lineas del encargo: {'linea de bloque sangrado': 13, 'prosa con numero, con seccion de la ACTA 76': 14, 'prosa con numero, sin seccion de la ACTA 76': 57, 'prosa sin digito ni palabra de numero': 69} | suma: 153

(Las lineas con numero, cada una con sus digitos y sus palabras de numero, en `.v77aud/normal/r8_encargo78.txt`.) **LECTURA, grupo a
grupo, de las que no traen seccion, leidas una a una:**

- **Numeros de vuelta, de acta, de mundo, de fecha o de carpeta de la casa**: `77`, `76`, `78`, `75`, `11`, el `23` y el `26` sep, y
  `.v64ext/`, `.v64aud/`, `.v70aud/`, `.v76ext/`, `.v77aud/`, `.v77ext/`, `.v78ext/`.
- **Secciones, reglas, deudas, remedios y numeros de tarea, de punto o de lista**: `1.4`, `6.1`, `8.2`, `62.5`, `D.29`, `D.30`, `D.36`,
  `D.37`, `D.38.4`, `D.47`, `D.53`, `D.55`, `D.58`, `D.61`, `D68.7`, `7.F`, `d031`, `d150`, `R5`, `R9`, y los de tarea y de punto.
- **Identificadores**: `cap_17` y `cap_03`; el nombre del fichero `2026-09-26-seis-plazas-NOTA.md`; el titulo *Los tres del mundo 11* de
  `PARALELO.md`; y la `ACTA 75` `75.4` citada como sede de una adjudicacion, no como medida.
- **Umbrales y topes de regla, no medidas**: *cinco a la vez como mucho* (dos veces) y el `10` por ciento.
- **Palabras de numero sin seccion**: *los dos delante* (los dos nodos de un par), *esas dos rutas* (las dos del censo), *las
  comprobaciones en cero* (la meta) y *cero guiones* (la frase fija).
- **Las cifras de medida** van dentro de un bloque `$` (la clase, el tablero, el reloj del barrido de la `76` y el texto de `d150`) o
  llevan su seccion de la `ACTA 76` en la misma linea: Marquet ultimo libro del corte y `cap_03` el de mas fichas (`76.11`), Gerber
  entero (`76.1`), las `22` de Gerber (`76.4`), los cuatro discutibles y las dos piezas (`76.3`), la bandeja de Marquet (`76.11`), la
  poblacion y el censo de apertura (`76.1`).

**Dos lineas las reescribi al medir**, antes de cerrar: *cinco fichas a la vez* del barrido de la `76` (una cuenta que solo se comprueba
abriendo su `barrer.sh`) salio de la frase, y *la fila de `cap_03` sigue publicada en cero* se cambio por el texto de `d150` pegado en su
bloque. Tambien cambie *tres asientos* del `23` sep y *seis plazas* por frases sin cuenta. **`R8` CUMPLIDO EN EL ENCARGO DE LA `78`,
medido.** Lo vuelve a medir mi fase ciega (`76.12`).

## 76.14. **LO QUE ANOTO AL CERRAR**

- **`docs/loop/CREDITO_serial.jsonl`**: las cinco lineas de la tanda `ACTA 76` (`76.8`), todas con `--limpia`. **Anotadas ANTES de
  correr las salidas que pego en el encargo** (`R10`).
- **`docs/loop/DEUDA.jsonl`**: **nada**. `d111` y `d108` las pago el extractor y aqui se firman (`76.3`). Las salidas pegadas en el
  encargo, vueltas a correr despues de la ultima escritura en `CREDITO_serial.jsonl` y comparadas, en `.v77aud/normal/r10.txt`.
- **`docs/loop/PROMPT_SIGUIENTE.md`**: el encargo de la vuelta `78`, **LIBRE**: la preparacion de las fichas de Marquet, sin insertar
  y sin bloqueante.
- **`.v77aud/`**: mi evidencia de las dos fases, commiteada con `docs/loop/`.
