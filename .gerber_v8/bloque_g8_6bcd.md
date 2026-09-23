
### G8.6.b. El instrumento, corrido DESPUES de pegar la tabla propia

    $ python scripts/tabla_de_cierre.py --escribir

<!-- TALLADO: script=scripts/tabla_de_cierre.py salida=docs/loop/TABLA_DE_CIERRE.txt -->

Salida guardada en `.gerber_v8/tabla_de_cierre_salida.txt`:

<!-- TALLADO: parcial salida=.gerber_v8/tabla_de_cierre_salida.txt -->

    TABLA DE CIERRE DE TAREAS (D.52): toda tabla del reporte declara su instrumento
    filas             : 5
    SIN COMPROBAR  `1` a `5`  ninguna afirmacion de la forma 'N de M del capitulo' con su cap_NN
    TABLA DE CIERRE VERDE: ninguna celda medible difiere del dato.

**LAS CINCO FILAS SALEN `SIN COMPROBAR`, Y ES LO ESPERADO:** ninguna de mis cinco celdas trae la forma
`N de M del capitulo` (el instrumento solo mide esa figura exacta); mis cifras de esta vuelta son de
palabras y piezas de frontera, no de nodos por capitulo, porque los tres capitulos cerraron en cero
candidatos. **`SIN COMPROBAR` no es `DIFIERE`: es una fila que el instrumento no sabe medir y copia tal
cual, sin inventar** (la propia doctrina del script, citada en `G8.6.a`).

### G8.6.c. Comprobacion: el fichero trae MIS filas, no las de otra vuelta

    $ cat docs/loop/TABLA_DE_CIERRE.txt

Salida guardada en `.gerber_v8/tabla_de_cierre_cat.txt`:

<!-- TALLADO: salida=.gerber_v8/tabla_de_cierre_cat.txt -->

    $ python scripts/tabla_de_cierre.py --escribir
    poblacion: dataset/nodos.jsonl entero, libro gerber_emyth
    criterio : un nodo sale de un capitulo si cita gerber_emyth/<cap>.md

    | # | tarea | como cerro |
    |---:|---|---|
    | `1` | `TAREA 1`: registros de apertura y correccion declarada de `d123` | **CERRADA en `G8.1`**: credito y deuda medidos (`45`/`38` de apertura, al digito con la cabecera del encargo), correccion tachada sin borrar en la celda de `G7.4.e`, `d123` pagada |
    | `2` | `TAREA 2`: `cap_20`, frontera y veredicto | **CERRADA en `G8.2`**: frontera `3` piezas, `1841` palabras al digito, residuo `0`; cero candidatos, capitulo minado por ser una carta sin inventario propio; cero discutibles |
    | `3` | `TAREA 3`: `cap_21`, frontera y veredicto | **CERRADA en `G8.3`**: frontera `5` piezas, `1851` palabras al digito, residuo `0`; cero candidatos, capitulo minado, el Epilogue sin inventario propio; cero discutibles |
    | `4` | `TAREA 4`: `cap_22`, frontera, veredicto y estado del lote `9` | **CERRADA en `G8.4`**: frontera `8` piezas, `904` palabras al digito, residuo `0`; cero candidatos, un discutible marcado y cerrado en el acto; lote `9` medido minado entero salvo `d094` (`3` de `22` unidades sin minar, las tres reservadas) |
    | `5` | `TAREA 5`: el cierre, con los punteros `D.37` para la vuelta que inserte | **CERRADA en `G8.5` y aqui mismo (`G8.6`)**: sin poblacion de pasos que medir (cero candidatos en el lote), muestra de fidelidad corrida con semilla `gerber_v8` sin disparador posible, tabla de punteros `D.37` publicada sin declarar aristas nuevas |

**LAS CINCO FILAS SON LAS MIAS, DE ESTA VUELTA `8`.** No hay arrastre de la tabla de la vuelta `7`.

### G8.6.d. Las tres guardas de la vuelta, corridas HOY, con su salida

Salida de `python forja.py gate`, guardada en `.gerber_v8/gate.txt`:

<!-- TALLADO: salida=.gerber_v8/gate.txt -->

    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

**`346` NODOS: EL MISMO NUMERO DE LA APERTURA, PORQUE ESTA VUELTA NO INSERTA (`MODO_INSERCION=cuarentena`,
`D.39`).** `d103` sostenida: las tres lineas de siempre.

Salida de `python forja.py guiones`, guardada en `.gerber_v8/guiones.txt`:

<!-- TALLADO: salida=.gerber_v8/guiones.txt -->

    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

**VERDE AL PRIMER INTENTO, SIN CORRECCION QUE DECLARAR ESTA VEZ** (a diferencia de la vuelta `7`, que
tuvo que corregir ocho guiones largos copiados de sus citas): esta vuelta no copia bloques largos de
prosa del libro en las citas de evidencia (los tramos citados con `sed` son frases cortas), y `d124`
sigue como cola sin nuevo ejemplar.

Salida de `python tests/test_aceptacion.py`, guardada en `.gerber_v8/test_aceptacion.txt`:

<!-- TALLADO: parcial salida=.gerber_v8/test_aceptacion.txt -->

    total: 350 pruebas, 0 fallos, 0 errores

**LAS TRES GUARDAS VERDES: GATE, GUIONES Y ACEPTACION, LAS `350` PRUEBAS EN VERDE, `0` FALLOS.**
