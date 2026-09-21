
## G7.6. EL CIERRE

### G7.6.a. La tabla de cierre de la vuelta `7`, pegada PRIMERO

*Remedio de `d030`/`d112` (`ACTA G6`, `G6.4`): mi tabla se pega ANTES de correr `--escribir`, para que
`docs/loop/TABLA_DE_CIERRE.txt` traiga MIS filas y no las de la vuelta anterior.*

| # | tarea | como cerro |
|---:|---|---|
| `1` | `TAREA 1`: registros de apertura y correccion declarada de `d117` | **CERRADA en `G7.1`**: credito y deuda medidos (`42`/`36` de apertura, discrepancia contra la cabecera del encargo declarada), correccion tachada sin borrar en el bloque de la vuelta `6`, `d117` pagada |
| `2` | `TAREA 2`: `cap_18`, frontera y tres candidatos con su aduana en el acto | **CERRADA en `G7.3`**: frontera `11` piezas, `5396` palabras al digito, `3` candidatos, `0 CAERIA` en las tres aduanas, `2` discutibles marcados y cerrados |
| `3` | `TAREA 3`: pagar `d110` leyendo `cap_17` `L189` a `L221` junto a la apertura de `cap_18` | **CERRADA en `G7.2`**: el autor SI saca el Operations Manual del caso, el discutible `5` de la vuelta `5` reabierto y resuelto, `d110` pagada |
| `4` | `TAREA 4`: `cap_19` si el techo lo permite, y cuanto queda de `d111` | **CERRADA en `G7.4`**: techo en `3` de `30`, `cap_19` minado (frontera `10` piezas, `4431` palabras al digito, `3` candidatos, `0 CAERIA`), `d111` medida en `0` de `7` sin decidir |
| `5` | `TAREA 5`: el cierre, `PASOS INVENTADOS POR CAPITULO` con poblacion de verdad | **CERRADA en `G7.5` y aqui mismo (`G7.6`)**: `0,00` por ciento en las dos filas y en el lote, muestra de fidelidad con semilla `gerber_v7` sin disparador |

### G7.6.b. El instrumento, corrido DESPUES de pegar la tabla propia

    $ python scripts/tabla_de_cierre.py --escribir

<!-- TALLADO: script=scripts/tabla_de_cierre.py salida=docs/loop/TABLA_DE_CIERRE.txt -->

Salida guardada en `.gerber_v7/tabla_de_cierre_salida.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/tabla_de_cierre_salida.txt -->

### G7.6.c. Comprobacion: el fichero trae MIS filas, no las de otra vuelta

    $ cat docs/loop/TABLA_DE_CIERRE.txt

Salida guardada en `.gerber_v7/tabla_de_cierre_cat.txt`:

<!-- TALLADO: salida=.gerber_v7/tabla_de_cierre_cat.txt -->

### G7.6.d. Las tres guardas de la vuelta, corridas HOY, con su salida

Salida de `python forja.py gate`, guardada en `.gerber_v7/gate.txt`:

<!-- TALLADO: salida=.gerber_v7/gate.txt -->

    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

**`346` NODOS: EL MISMO NUMERO DE LA APERTURA, PORQUE ESTA VUELTA NO INSERTA (`MODO_INSERCION=cuarentena`,
`D.39`).**

Salida de `python forja.py guiones`, guardada en `.gerber_v7/guiones.txt`:

<!-- TALLADO: salida=.gerber_v7/guiones.txt -->

    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

**CORRECCION DECLARADA EN EL ACTO, NO EN UNA VUELTA POSTERIOR:** el primer barrido de esta vuelta dio
`8` hallazgos, los ocho guiones largos (U+2014) copiados verbatim del propio libro dentro de mis
ficheros de cita (`.gerber_v7/cita_cap18_L137_L166.txt`, `.gerber_v7/cita_cap19_L141_L153.txt`,
`.gerber_v7/cita_cap19_L33_L45.txt`). `fuentes/` es bandeja de entrada y no se barre; mis copias de
evidencia si, porque viven fuera de esa bandeja. Se corrigieron sustituyendo el guion largo por el
guion corto normal en esas tres copias (la palabra no cambia, solo el ancho del trazo), y el barrido
volvio a `VERDE` antes de seguir.

Salida de `python tests/test_aceptacion.py`, guardada en `.gerber_v7/test_aceptacion.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/test_aceptacion.txt -->

    total: 350 pruebas, 0 fallos, 0 errores

**LAS `d103` TRES LINEAS DE `gate` SE SOSTIENEN, EL BARRIDO DE GUIONES QUEDA VERDE TRAS SU CORRECCION
DECLARADA, Y LAS `350` PRUEBAS DE ACEPTACION PASAN, `0` FALLOS.**

### G7.6.e. El tallado y el censo, corridos HOY

Salida de `python scripts/tallar_reporte.py`, guardada en `.gerber_v7/tallado.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/tallado.txt -->

    TALLADO VERDE: las 172 tabla(s) comprobables son las de su instrumento, celda a celda.

**CORRECCION DECLARADA (`D.41`), YA CONTADA EN `G7.3.b` Y `G7.4.c`:** las dos tablas de frontera de esta
vuelta llegaron a un primer commit con la columna *que es* resumida a mano, el hook las marco `DIFIERE`
(`11` celdas en la de `cap_18`, `10` en la de `cap_19`), y las dos se regeneraron con
`python scripts/tallar_reporte.py --arreglar`, nunca tecleando la celda buena.

Salida de `python scripts/censar_rutas.py`, guardada en `.gerber_v7/censo_rutas.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/censo_rutas.txt -->

    CENSO VERDE: las 1085 rutas publicadas sostienen lo que dicen sostener.

**CORRECCION DECLARADA (`D.42`):** la celda de `G7.5.b` que cita mis seis ficheros de evidencia de
fidelidad los nombraba primero como dos PATRONES (`.gerber_v7/cita_cap18_*.txt` y
`.gerber_v7/cita_cap19_*.txt`) en la misma linea; el censo solo reconoce el primer `PATRON:` de cada
unidad y marco el segundo `CAE`. Se corrigio nombrando los seis ficheros por su ruta exacta en vez de
por un patron, y el censo volvio a `VERDE`.
