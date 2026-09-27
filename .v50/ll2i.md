
### LL.2.i. **CANDIDATO `3` DE `3`: `P44`, `canalizar_interrupciones_cartel_hora_oficina`**

| | |
|---|---|
| **pieza y rango** | `P44`, `L321 a L323`, **`201` palabras**, las de `HH.2.c` y recomputadas en `LL.2.d` |
| **frontera dentro del nodo** | L321 y L323, con L322 en blanco. **Cero solapes**, y **no toma nada de L319**, que es `P43` y no tiene nodo por `P.19` |
| **pasos** | **`8`** |
| **fidelidad `D.30` en el acto** | **`8` TRANSCRIPCION, `0` PUENTE** |
| **el texto del cartel** | **TRANSCRIPCION, y lo digo por su nombre** porque el encargo lo pide: el libro escribe el cartel entero entre comillas y el paso `3` lo traslada entero, **incluida la hora**. NO lo reescribo, y por eso no es puente |
| **puentes que estuve a punto de escribir** | **`2`, declarados dentro de la ficha**: EL PERIODO (cada cuanto y cuanto dura la hora de oficina abierta) y EL DESTINATARIO (acordar el cartel con el equipo o avisar al jefe) |

**LA FIDELIDAD, PASO A PASO Y CONTRA SU RENGLON**, con el `sed` pegado en `LL.2.c` filas `3` y `4`:

| paso | linea | de donde sale | veredicto |
|---:|---|---|---|
| 1 | L321 | `If the people who interrupt you knew how much they were disturbing you, they would probably police themselves more closely and cut down on the number of times they felt they had to talk to you right away` | **TRANSCRIPCION** |
| 2 | L321 | `In any case, a manager should try to force his frequent interrupters to make an active decision about whether an issue can wait` | **TRANSCRIPCION** |
| 3 | L321 | `So, instead of going into hiding, a manager can hang a sign on his door that says, I am doing individual work. Please do not interrupt me unless it really cannot wait until 2:00` | **TRANSCRIPCION**, con el texto del cartel dentro |
| 4 | L321 | `Then hold an open office hour, and be completely receptive to anybody who wants to see you` | **TRANSCRIPCION** |
| 5 | L321 | `The key is this: understand that interrupters have legitimate problems that need to be handled. That is why they are bringing them to you` | **TRANSCRIPCION** |
| 6 | L321 | `But you can channel the time needed to deal with them into organized, scheduled form by providing an alternative to interruption, a scheduled meeting or an office hour` | **TRANSCRIPCION** |
| 7 | L323 | `The point is to impose a pattern on the way a manager copes with problems` | **TRANSCRIPCION** |
| 8 | L323 | `To make something regular that was once irregular is a fundamental production principle, and that is how you should try to handle the interruptions that plague you` | **TRANSCRIPCION** |

> **LA MISMA LICENCIA QUE EN `LL.2.g`, DECLARADA:** las contracciones del libro (`don't`, `can't`,
> `That's`, `they're`, `that's`) van desatadas en esta tabla por mecanica de escritura. **El renglon
> literal esta pegado sin tocar en la ficha** y sus lineas enteras estan en `LL.2.c`.

**LA PASADA DE ADUANA, CON SU RELOJ:**

<!-- TALLADO: parcial salida=.v50/informe_03.txt -->

    $ python forja.py informe cuarentena/grove_high_output/canalizar_interrupciones_cartel_hora_oficina.json
    poblacion del barrido       : 393   (346 del grafo mas 47 que esperan en bandejas)
    EL SALDO
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0
    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 3
      por candidato bloqueado          : menor 3, mediana 3, mayor 3
      que senial levanta cada vecindad  : similitud_texto 3

<!-- TALLADO: parcial salida=.v50/reloj_c03.txt -->

    reloj del candidato 3 (P44), pasada de aduana propia
    segundos: 410.0

### LL.2.j. **LOS TRES VECINOS DE `P44`: LOS TRES SON DE LA MISMA SECCION DEL LIBRO**

<!-- TALLADO: parcial salida=.v50/informe_03.txt -->

    [BLOQUEARIA] canalizar_interrupciones_cartel_hora_oficina
        vecino preparar_respuestas_estandar_interrupciones_repetidas  [levantada por: similitud_texto]
          similitud_texto 0.385 | familia_id 0.111 | paso_contra_nodo 0.472
          paso 5 del candidato contra paso 4 de preparar_respuestas_estandar_interrupciones_repetidas
        vecino buscar_regularidad_bloques_iguales_trabajo_mando  [levantada por: similitud_texto]
          similitud_texto 0.371 | familia_id 0.000 | paso_contra_nodo 0.471
          paso 8 del candidato contra paso 4 de buscar_regularidad_bloques_iguales_trabajo_mando
        vecino agrupar_interrupciones_subordinados_reuniones_regulares  [levantada por: similitud_texto]
          similitud_texto 0.408 | familia_id 0.111 | paso_contra_nodo 0.422
          paso 8 del candidato contra paso 2 de agrupar_interrupciones_subordinados_reuniones_regulares

| vecino | senial | mi lectura |
|---|---:|---|
| `agrupar_interrupciones_subordinados_reuniones_regulares` (`P42`) | `0,408` de senial `1` | **HERMANO, y la arista es mas fuerte que la de hermano suelto**: mi paso `6` ofrece como alternativa *una reunion programada*, y quien despliega esa reunion programada como operacion propia es `P42`. **Este la nombra y no repite sus pasos** |
| `preparar_respuestas_estandar_interrupciones_repetidas` (`P41`) | `0,385` de senial `1` | **HERMANO.** Tercer remedio contra primer remedio de la misma seccion, sin un paso en comun |
| `buscar_regularidad_bloques_iguales_trabajo_mando` (`P39`) | `0,371` de senial `1` | **HERMANO.** Mi paso `8` manda volver regular lo que era irregular, y aquel es donde esa regularidad se ejecuta sobre el calendario propio |

**LOS TRES ESTAN POR DEBAJO DE `0,4` SALVO UNO, Y NINGUNO PASA LA SENIAL `3`.** Y lo que dice esta
vecindad no es una sospecha de duplicado: **es que un capitulo trata un tema.** `EXTRACTOR.md` 12 lo
escribe con esas palabras, y **lo que NO se hace es subir un umbral para que la cola se acorte.**

### LL.2.k. **`cap_04` CIERRA: `22` DE `22`, Y LA PUERTA SE VUELVE A MEDIR**

**Los tres candidatos salieron `0 CAERIA` y `0` choques dentro del lote**, asi que no hay averia
que declarar (encargo, `TAREA 2`: un `CAERIA` si lo seria).

| | |
|---|---:|
| nodos que la frontera de `HH.2.c` da en `cap_04` | **`22`** |
| fichas de `cap_04` en la bandeja al cerrar esta tarea | **`22`** |
| pasos escritos hoy | **`19`** (`6` mas `5` mas `8`) |
| `PUENTE` de esos `19` | **`0`** |
| pasadas de aduana gastadas | **`3` de un techo de `3`** |

**Y LO QUE ESTO NO ES: NO CIERRA EL LOTE 7.** `grove_high_output` tiene `18` capitulos y lleva
**cuatro** minados (`cap_01` a `cap_04`). **La puerta de `D.39` sigue midiendo `False`** en
`LL.0.a`, asi que **cero inserciones**, y meter uno de estos tres antes de que el lote cierre
**seria una caida de dato y no un adelanto** (`EXTRACTOR.md` 15.7).

| tarea | que pide | estado |
|---|---|---|
| `LL.2` | cerrar `cap_04` con `P41`, `P42` y `P44`, con su frontera dentro, su fidelidad paso a paso y su aduana en el acto | **CERRADA ENTERA en `LL.2`**: `3` de `3` escritos y pasados, `0 CAERIA`, `0` choques, `19` pasos con `0` PUENTE, `12` vecindades leidas una a una, relojes `639,0`, `335,0` y `410,0` s, y `cap_04` en `22` de `22` |
