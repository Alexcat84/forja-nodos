
## KK.3. TAREA 3. **`d024` EN SU PRIMER TRAMO, Y EL TRAMO CIERRA EN `2` DE `3`**

**`d024` dice que los `7` candidatos de `cap_02` de `grove_high_output` no tienen informe de aduana
por candidato, y que lo unico que los midio fue un informe de lote.** Hoy dejan de ser siete sin
medir.

### KK.3.a. **EL ORDEN DEL LIBRO, QUE ES EL ORDEN EN QUE SE CORREN, NO TECLEADO**

<!-- TALLADO: script=.v49/orden_cap02.py salida=.v49/orden_cap02.txt -->

    $ python .v49/orden_cap02.py
    LOS 7 DE cap_02, EN EL ORDEN DEL LIBRO:
      1  P2    construir_flujo_produccion_paso_limitante
      2  P5    clasificar_trabajo_proceso_montaje_prueba
      3  P6    rehacer_flujo_paso_limitante_capacidad
      4  P7    equilibrar_capacidad_personal_inventario_plazo
      5  P9    preferir_inspeccion_proceso_prueba_destructiva
      6  P10   dimensionar_inventario_materia_prima_reposicion
      7  P11   detectar_arreglar_fallo_etapa_menor_valor

    total: 7

### KK.3.b. **LOS DOS INFORMES CORRIDOS, UNO POR VEZ, CON SU RELOJ**

<!-- TALLADO: parcial salida=.v49/informe_cap02_1.txt -->

    $ time python forja.py informe cuarentena/grove_high_output/construir_flujo_produccion_paso_limitante.json
    poblacion del barrido       : 390   (346 del grafo mas 44 que esperan en bandejas)
    EL SALDO
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0
    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 3
      por candidato bloqueado          : menor 3, mediana 3, mayor 3
      que señal levanta cada vecindad  : familia_id 1, paso_contra_nodo 1, similitud_texto 2
    real	14m15.821s

<!-- TALLADO: parcial salida=.v49/informe_cap02_2.txt -->

    $ time python forja.py informe cuarentena/grove_high_output/clasificar_trabajo_proceso_montaje_prueba.json
    poblacion del barrido       : 390   (346 del grafo mas 44 que esperan en bandejas)
    EL SALDO
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0
    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 1
      por candidato bloqueado          : menor 1, mediana 1, mayor 1
      que señal levanta cada vecindad  : similitud_texto 1
    real	19m34.408s

**`0 CAERIA` EN LOS DOS, asi que no hay averia y no paro** (el encargo pone ahi el liston). Los dos
`BLOQUEARIA` son **cola de lectura y no rechazo**, y **hoy no se leen ni se les escribe veredicto**:
un veredicto se escribe **al insertar**, y la puerta de `D.39` mide cerrada (`KK.0.a`).

### KK.3.c. **LOS CUATRO VECINOS QUE ESTOS DOS INFORMES LEVANTAN, QUE ES LO QUE `d024` COMPRABA**

| candidato | vecino | quien lo levanta | la cifra que lo levanta |
|---|---|---|---:|
| `construir_flujo_produccion_paso_limitante` | `retirar_barreras_politicas_metodo` | `paso_contra_nodo` | `0.614` |
| `construir_flujo_produccion_paso_limitante` | `rehacer_flujo_paso_limitante_capacidad` | `similitud_texto`, `familia_id` | `0.412` y `0.429` |
| `construir_flujo_produccion_paso_limitante` | `preferir_inspeccion_proceso_prueba_destructiva` | `similitud_texto` | `0.397` |
| `clasificar_trabajo_proceso_montaje_prueba` | `preferir_inspeccion_proceso_prueba_destructiva` | `similitud_texto` | `0.372` |

**Y LO QUE ESTA TABLA ENSENIA, que es justo lo que un informe de lote no podia ver:** **tres de los
cuatro vecinos son companeros del propio `cap_02`** (`rehacer_flujo_paso_limitante_capacidad` y
`preferir_inspeccion_proceso_prueba_destructiva`, dos veces). Es el caso que `EXTRACTOR.md` 12 nombra
por su nombre: **un capitulo entero en la misma familia no es senial de duplicado, es senial de que
el libro trata un tema**, y la cola larga es su precio. **No propongo tocar ningun umbral.**

**Y UNO DE LOS CUATRO NO ES DE LA FAMILIA Y ES EL QUE MAS ALTO SUENA:**
`retirar_barreras_politicas_metodo` a `0.614` de `paso_contra_nodo`, **por encima del umbral de
`0.60`**, con `similitud_texto` en `0.108`. `EXTRACTOR.md` 11 dice que `paso_contra_nodo` cerca de
`1,0` significa que el material ya vive en el grafo; **`0.614` no esta cerca de `1,0`**, y con la
similitud de texto en `0.108` **el par huele a hermano y no a gemelo**. Lo dejo dicho **como cola de
lectura, no como veredicto**: el veredicto se escribe al insertar y con los dos textos delante.

### KK.3.d. **EL TRAMO CIERRA CORTO EN `2` DE `3`, Y SE DECLARA CON SUS TRES PIEZAS**

**EL NUMERO:** `2` de los `3` informes que el encargo pide, y **`4` pasadas de aduana** de las `5`
del techo.

**EL RELOJ:** `4.069,0` s gastados en pasadas (`559,4` mas `1.479,4` mas `855,8` mas `1.174,4`)
contra un techo de `4.949` s, o sea **`880` s libres**, y la `TAREA 4` tiene presupuestados `432` s.
**La quinta pasada no cabe:** las cuatro de hoy han costado **`1.017,3` s de media** y la mas barata
`559,4` s, asi que **ninguna entra en `880` menos `432`**, que son `448` s.

**LO QUE QUEDA NOMBRADO, uno a uno, que es lo que convierte un pago parcial en deuda medida:**

| # | pieza | candidato de `cap_02` sin informe propio |
|---:|---|---|
| 3 | `P6` | `rehacer_flujo_paso_limitante_capacidad` |
| 4 | `P7` | `equilibrar_capacidad_personal_inventario_plazo` |
| 5 | `P9` | `preferir_inspeccion_proceso_prueba_destructiva` |
| 6 | `P10` | `dimensionar_inventario_materia_prima_reposicion` |
| 7 | `P11` | `detectar_arreglar_fallo_etapa_menor_valor` |

**`d024` NO SE MARCA PAGADA: pasa de `7` sin medir a `5` sin medir**, y **son `5` y no `4`** porque
el tramo cerro en `2` y no en `3`. **La deuda de hoy baja de `16` a `14` por `d027` y `d032`, y
`d024` sigue abierta**, que es lo que el propio encargo manda.

**Y POR QUE SE CORTO AQUI Y NO EN LA `TAREA 4`, dicho para que se pueda discutir:** el encargo
autoriza el corte **en la pasada** (*si no cabe, cierra corto en la pasada*) y `d024` **ya nace
parcial y con sus restantes nombrados**; `d033`, en cambio, **pide una tasa, y una tasa con `13`
corridas en vez de `20` es otra tasa**. **Cortar el que esta disenado para cortarse cuesta menos que
estrechar el que no.**

| tarea | que pide | estado |
|---|---|---|
| `KK.3` | pagar `d024` en su primer tramo: `3` de los `7` de `cap_02`, uno por vez, en el orden del libro, con reloj, y los que queden nombrados | **CERRADA CORTA en `KK.3`**: `2` de `3` corridos (`P2` y `P5`), **`0 CAERIA` en los dos**, relojes `855,8` s y `1.174,4` s, los `4` vecinos de la cola tabulados, **el corte declarado con sus tres piezas** y los **`5`** que quedan nombrados uno a uno |
