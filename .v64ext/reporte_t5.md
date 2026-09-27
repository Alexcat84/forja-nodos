
## 64.6. TAREA 5: EL CIERRE

### 64.6.a. LA VUELTA DE SANEAMIENTO, DECLARADA EN EL REGISTRO, Y LO QUE SE PAGA

**La declaracion que falto en la `49` y en la `59` (`d085`), hecha esta vez por la propia vuelta**, y los tres
pagos, cada uno porque su condicion se cumplio entera en esta vuelta. **El texto entero de cada `--como` esta en
`docs/loop/DEUDA.jsonl`**; en el bloque va abreviado en la linea del comando, no en la salida:

<!-- TALLADO: parcial salida=.v64ext/cierre_deuda.txt -->

    $ python scripts/deuda.py --clase 64
    SANEAMIENTO
      han pasado 5 vuelta(s) desde la ultima de saneamiento (la 59) y la cadencia es 5, con 54 deuda(s) pendientes
    $ python scripts/deuda.py --saneamiento --vuelta 64
    DECLARADA vuelta de SANEAMIENTO: 64
    $ python scripts/deuda.py --pagar d005 --vuelta 64 --como "..."
    PAGADA d005 en la vuelta 64
    $ python scripts/deuda.py --pagar d140 --vuelta 64 --como "..."
    PAGADA d140 en la vuelta 64
    $ python scripts/deuda.py --pagar d141 --vuelta 64 --como "..."
    PAGADA d141 en la vuelta 64

| deuda | su condicion | se cumple | donde |
|---|---|---|---|
| `d005` | los seis con fidelidad leida y veredictos listos | **SI**: `41` pasos leidos, `2` PUENTE reescritos; `6` bloques de veredicto, cero que falten | `64.2`, `64.3`, `64.5.a` |
| `d140` | los nueve con sus veredictos listos | **SI**: `9` bloques, los de `detectar` reutilizados; relectura conjunta hecha en su orden | `64.3`, `64.4` |
| `d141` | los pares escritos o cerrados, y la tabla del orden publicada | **SI**: los cuatro pares de `d141` sostenidos, cuatro mas sostenidos y cinco cerrados; la tabla, impresa y comprobada | `64.5.b`, `64.5.c` |

**Quedan `51` pendientes** (`54` menos las tres), medido al cierre en `.v64ext/cierre_censo.txt`.

### 64.6.b. `PASOS INVENTADOS POR CAPITULO`, CONTADOS POR UN INSTRUMENTO

**Una fila, los seis de `d005`, todos de `cap_03`**. Los pasos los cuenta `.v64ext/contar_fidelidad.py` abriendo
las fichas, y exige una fila de lectura por paso (cero sin fila, cero sobrantes):

<!-- TALLADO: parcial salida=.v64ext/contar_fidelidad.txt -->

    $ python .v64ext/contar_fidelidad.py | tail -2
    PASOS INVENTADOS POR CAPITULO, los seis de d005
    cap_03  candidatos 6  pasos 41  T 39  P 2  inventado 4,9 por ciento

**`4,9` por ciento, por debajo del `10`.** Con los dos discutibles de fidelidad contados en contra (`D64.1` y
`D64.2`), `9,8`: todavia por debajo.

### 64.6.c. `D.61`: CADA DISCUTIBLE, EJECUTADO O CERRADO

| | que | como queda |
|---|---|---|
| `D64.1` | `archivar...` paso `1`, su coda sin mandato, contada `T` | **CERRADO** en `T`, con el criterio de la `ACTA 62` `62.5` escrito al lado |
| `D64.2` | ejemplos del libro en imperativo (`elegir_fabricar` paso `9`, `construir_grafico` paso `5`), contados `T` en su contenido | **CERRADO** en `T`; la unica clausula inventada del paso `5` (*debajo*) si cuenta y esta **EJECUTADA** (reescrita) |
| `D64.3` | tres pares con texto por encima de `0,4` leidos SANO | **CERRADO** en SANO, con la banda sin tocar |
| `D64.4` | `dimensionar_inventario` CONTINUA de `detectar` | **CERRADO** en CONTINUA, y es la unica discrepancia con la apertura sellada (`64.4`) |
| `D64.5` | `construir_grafico` contra `construir_indicador_tendencia` SANO, contra lo que la ficha anunciaba | **CERRADO** en SANO |
| `D64.6` | `construir_grafico` madre de `casar_flujo`, sin rebajarla | **CERRADO**: sostenida en `ARISTAS POR LECTURA` |
| `D64.7` | `representar_actividad_caja_negra` madre de `construir_indicador_tendencia` | **CERRADO**: sostenida en `ARISTAS POR LECTURA` |

**Ninguno abierto.**

### 64.6.d. `R5` EN CADA BLOQUE `$` DE ESTE TRAMO

Medido con el instrumento de la `ACTA 62`, copiado con la cabecera del tramo cambiada (`62.13` lo manda asi):

<!-- TALLADO: parcial salida=.v64ext/pegado64.txt -->

    $ python .v64ext/pegado64.py
    bloques abiertos con `$` en el tramo de la vuelta 64 : 37
    bloques que ROMPEN R1 (ACTA 60 60.15)                : 0

**Los cortes de esta vuelta van en el propio comando** (`grep -n -o`, `grep -v`, `tail`, `sed -n`), y el unico
corte de bloque, el de la apertura, lleva la formula dentro.

### 64.6.e. EL CENSO, ANTES Y DESPUES: IGUAL, PORQUE ESTA VUELTA NO INSERTA

<!-- TALLADO: parcial salida=.v64ext/cierre_censo.txt -->

    $ wc -l bitacora/VEREDICTOS.jsonl dataset/nodos.jsonl config/pares_mutuos.jsonl
        740 bitacora/VEREDICTOS.jsonl
        346 dataset/nodos.jsonl
          1 config/pares_mutuos.jsonl
       1087 total
    $ ls cuarentena/grove_high_output/*.json | wc -l
    91
    $ git diff --stat 1034222 -- dataset/ bitacora/ censos/ config/pares_mutuos.jsonl | wc -l
    0
    $ ls procesos/
    nodos.jsonl.218e43e4.cerrojo
    nodos.jsonl.679b2259.cerrojo
    nodos.jsonl.e52fd5d2.cerrojo

| | apertura (`64.0`) | cierre | el encargo |
|---|---:|---:|---:|
| nodos | `346` | `346` | `346` |
| veredictos | `740` | `740` | `740` |
| pares mutuos | `1` | `1` | `1` |
| bandeja de Grove | `91` | `91` | `91` |

**Cero lineas de diff sobre `dataset/`, `bitacora/`, `censos/` y los pares desde el commit de apertura.** Ni un
`insertar`, ni un veredicto en la bitacora, ni una arista. **Los tres cerrojos siguen como estaban, sin tocar.**

### 64.6.f. LAS GUARDAS, EN VERDE Y PEGADAS

<!-- TALLADO: parcial salida=.v64ext/cierre_censo.txt -->

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

<!-- TALLADO: parcial salida=.v64ext/cierre_tests.txt -->

    $ python tests/test_aceptacion.py | tail -2
      total: 379 pruebas, 0 fallos, 0 errores
    ========================================================================

`python scripts/cerrar_reporte.py`, corrido despues de anexar este tramo, en `64.6.h`.

### 64.6.g. LO QUE PROPONGO Y LO QUE DEJO DICHO (`EXTRACTOR.md` 14: propongo, no me adjudico)

1. **La nota de una correccion declarada mueve la senial de los vecinos, no solo la de su ficha.** Mis cinco
   notas hicieron bloquear a dos candidatos que no toque (`equilibrar`, `elegir_inspeccion`) y levantaron nueve
   sentidos nuevos dentro de los `22` (`64.5.a`). Es `d031` y `d058` a la vez. **No lo anoto como deuda nueva**:
   lo cubren esas dos, y el mecanismo de la casa lo absorbe (el `insertar` de la `65` bloquea y pide leer).
2. **Lo que no medi, dicho otra vez para el encargo de la `65`**: los vecinos NUEVOS de las cinco fichas
   corregidas **fuera de los `22`**. El barrido no cabia en el turno (`64.2.c`). Si el `insertar` de la `65` los
   levanta, bloquea, y se leen entonces.
3. **Tres cerrojos en `procesos/` y el encargo nombra uno.** No toque ninguno; el primer `insertar` de la `65`
   dira cuales son de este arbol.
4. **No escribo `PARA_ALEXIS.md`**: nada me obligo a parar.
