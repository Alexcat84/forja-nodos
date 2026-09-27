
# ACTA M4. VUELTA 3 DEL FRENTE `marquet_turn_the_ship`, `cap_07` y `cap_08`, **CLASE EXTRACCION EN REGIMEN LIGERO**: **LAS DOS FRONTERAS ME CIERRAN AL DIGITO, LOS CUATRO DISCUTIBLES SE SOSTIENEN LOS CUATRO, Y LO QUE SE CAE ES QUE EL REGISTRO DE CREDITO DICE LO CONTRARIO QUE LA TABLA QUE LO DOCUMENTA**. Le recompongo **las `107` filas de las dos fronteras** contra el fichero y me salen **al digito** (`2189` y `2224` palabras, `0` solapes, `0` lineas sin cubrir, `0` discrepancias fila a fila); **cuento yo los `16` pasos de las cuatro fichas vivas del libro contra su linea y firmo su `0` PUENTE**; **coteju la muestra de fidelidad con la semilla `m3` del reporte y me sale IDENTICA**, `diff` vacio; **reproduzco su aduana de banda ALTA byte a byte con mi propia corrida**; y **los cuatro discutibles se sostienen los cuatro**, incluido el par de `0,468` y `0,451`, que NO son gemelos. Y aun asi: **las cuatro lineas que la vuelta escribio en `docs/loop/CREDITO_marquet_turn_the_ship.jsonl` llevan `cae: true` mientras la tabla `7.d` que las documenta dice *no cae* cuatro veces**, y tres de esas cuatro caidas son falsas medidas por mi (`CLASE`: cero veredictos escritos; `DATO MOVIDO`: `git diff` vacio sobre `dataset/`, `bitacora/`, `censos/` y `config/`; `REPORTE`: sin caida que acumule). **`CIFRA PUBLICADA` sube de `0 de 2` a `1 de 2`** por esa contradiccion en sede duradera. **`REPORTE` BAJA de `1 de 3` a `0 de 3`** por `D.38.1`: sus tres caidas de esta tanda son erratas de celda que no acumulan (`sed ... | wc -l` pegado como `13` donde da `24`; *`40` `CASO`, `8` `POSTURA`* donde hay `29` y `12`; y cinco referencias a una *seccion `6`* y una *seccion `8`* que ese reporte no tiene). `CLASE` y `DATO MOVIDO` salen **LIMPIAS y medidas**. **Y MI PROPIO TURNO ANTERIOR SALIO MUDO**: corrio `1483` segundos, cobro `10,065` USD, anoto credito y deuda y **no escribio acta**; lo declaro con mi nombre, reparo sus cinco citas huerfanas, y **no acumula**, porque ninguna de mis dos especies lo cubre. **NO HAY PARADA**, y las seis condiciones van medidas una a una en `M4.17`. **El tramo de la vuelta `4` SUBE a TRES capitulos** por `8.1`, con el peor capitulo de esta vuelta en `0,00`.

## M4.0. **LO PRIMERO: ESTE TURNO NO TIENE FASE CIEGA, Y EL ANTERIOR DE MI ROL SALIO MUDO**

**`D.58` lo dice y el arnes lo registro**: en `MODO_INSERCION=cuarentena` no hay fase ciega, no hay sello y no hay testigo, porque no hay ninguna cifra sobre el grafo que proteger.

    $ grep "SIN FASE CIEGA" docs/loop/loop.log | tail -1
    [2026-09-21 20:32:24] VUELTA 2 : SIN FASE CIEGA (D.58: en cuarentena no hay cifra sobre el grafo que proteger)

**Y LO SEGUNDO, QUE ES MIO Y VA AQUI ARRIBA PORQUE CONDICIONA LO QUE ME ENCUENTRO EN EL ARBOL:**

    $ tail -2 docs/loop/loop.log
    [2026-09-21 20:57:07] auditor: TURNO MUDO, el turno corrio 1483s y cobro "10.065328500000003" pero docs/loop/ACTA_AUDITOR.md quedo identico, intento 1 de 7
    [2026-09-21 20:57:07] fallo "auditor mudo"; espero 1800 segundos y reintento

**ESTE ES EL REINTENTO.** Aquel turno dejo trabajo en el arbol sin commitear: `.m4aud/` con doce ficheros, tres lineas en `docs/loop/CREDITO_marquet_turn_the_ship.jsonl` y dos en `docs/loop/DEUDA.jsonl`, **todas citando secciones de una `ACTA M4` que no existia**. **No las copio: las verifico con mis propios instrumentos corridos en este turno**, y las sostengo o las corrijo una a una. Las secciones que esas citas prometen las escribo aqui con su contenido medido, que es lo unico que las hace ciertas. **Mi caida propia va en `M4.15`.**

## M4.1. **HUECO DE ACTA (`1.0`): NO HAY HUECO**

La `ACTA M3` cubre la vuelta `2` de este frente; esta cubre la `3`, que es la inmediatamente anterior. **Una sola vuelta, sin saltos.**

    $ git log --oneline -3
    34aed47 VUELTA 3 del frente marquet_turn_the_ship: paga el puente vivo de cap_06, ...
    9656eba Registra el estado de arnes pendiente antes de abrir la vuelta 3 ...
    f265593 ACTA M3 del frente marquet_turn_the_ship, VUELTA 2: ...

## M4.2. **LA HERENCIA (`D.40`): CERO, Y LA HUELLA ES LA DEL INSTRUMENTO**

    ACTA ANTERIOR LEIDA: d435fc76c8c2c8d17065fc36495f152cbbdc5336

    $ python forja.py herencia | grep -E "su huella|heredados"
      su huella     : d435fc76c8c2c8d17065fc36495f152cbbdc5336
      heredados     : 0

**El acta anterior no dejo ninguna tarea bloqueante ni ningun remedio escrito**, y lo dice el instrumento por su cuenta. **No hay `HEREDADO 1` que declarar porque no hay heredado.**

## M4.3. **LO QUE VERIFICO CON MIS PROPIOS COMANDOS** (`1.1`)

| instrumento, corrido en ESTE turno | lo que MIDE, con su salida | lo que el reporte dice |
|---|---|---|
| `python forja.py gate` | `GATE VERDE.` / `nodos verificados: 346` | `346`, coincide |
| `python forja.py guiones` | `BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.` | verde, coincide |
| `python tests/test_aceptacion.py` | `total: 356 pruebas, 0 fallos, 0 errores` | `356`, coincide |
| `python forja.py resolutor` | `nodos vivos: 346` / `nodos deprecados (archivo): 0` / `alias registrados: 0` | no la publica |
| `wc -l dataset/nodos.jsonl` | `346`, y `346` ids unicos de esas `346` lineas | `346`, coincide |
| `wc -l bitacora/VEREDICTOS.jsonl` | `740` | no la publica |
| `wc -l config/pares_mutuos.jsonl` | `1` | no la publica |
| `ls cuarentena/marquet_turn_the_ship/*.json \| wc -l` | `14` | `14`, coincide |
| `ls fuentes/marquet_turn_the_ship/*.md \| wc -l` | `17` | `17`, coincide |
| `python scripts/censar_rutas.py` | `CENSO VERDE: las 944 rutas publicadas sostienen lo que dicen sostener.` / `CAEN: 0` | no la publica |
| `python scripts/cerrar_reporte.py` | `CIERRE VERDE: las cuatro guardas que muerden, el tallado y el censo.` | verde, coincide |
| `python forja.py credito --revisar` | `REPLAY VERDE en la linea 'marquet_turn_the_ship': las 12 tanda(s) vigilables suman lo que declaran.` | no la publica |
| `python scripts/deuda.py --clase 4` | `LIBRE` / `van 2 de 5 ... con 34 deuda(s) esperando` | su apertura mide `1 de 5` y `32`, antes de las dos que se anotan hoy |

**EL CENSO DE RUTAS EN VERDE ES LA GUARDA QUE CIERRA `7.B` DE LA COSECHA**: las `944` rutas que esta casa publica como prueba existen y tienen contenido, y entre ellas van las cuatro del tramo (`.v3m/aduana/c1.txt` a `c4.txt`, de `1092`, `1104`, `1845` y `1825` bytes). **Ninguna promete prueba y apunta a cero bytes**, que es lo que la vuelta `2` si hizo y la `ACTA M3` `M3.10` le conto.

**LA VIGENCIA (`D.15`) TIENE COLA Y NO PONE NADA EN ROJO**, y lo digo porque corrio: los rancios que `forja.py rancios` lista son de `scott_radical_candor` y `grove_high_output`. **Ninguno de este libro**, que no tiene ni un nodo en el grafo.

## M4.4. **LAS DOS FRONTERAS, RECOMPUESTAS POR MI FILA A FILA: `107` FILAS Y ME CIERRAN AL DIGITO**

*No reuso el script del turno mudo: escribo el mio, parseo la tabla del reporte, expando cada rango de lineas, sumo con la cuenta de palabras por linea del fichero del libro y comparo celda a celda. Queda en `.m4b/frontera.py`.*

    $ python .m4b/frontera.py cap_07 fuentes/marquet_turn_the_ship/cap_07.md 58190 58255
    FRONTERA DE cap_07, RECOMPUESTA POR EL AUDITOR DE LA ACTA M4
      filas de la tabla del reporte  : 49
      suma de palabras DECLARADA     : 2189
      cuerpo real L8+ (suma wc -w)   : 2189
      lineas con palabras SIN CUBRIR : 0  []
      DISCREPANCIAS fila a fila      : 0

    $ python .m4b/frontera.py cap_08 fuentes/marquet_turn_the_ship/cap_08.md 58309 58380
    FRONTERA DE cap_08, RECOMPUESTA POR EL AUDITOR DE LA ACTA M4
      filas de la tabla del reporte  : 58
      suma de palabras DECLARADA     : 2224
      cuerpo real L8+ (suma wc -w)   : 2224
      lineas con palabras SIN CUBRIR : 0  []
      DISCREPANCIAS fila a fila      : 0

**Y LAS CABECERAS DE LAS DOS UNIDADES, RECONTADAS UNA A UNA:**

| | `cap_07` declara | mi `wc` | `cap_08` declara | mi `wc` |
|---|---:|---:|---:|---:|
| lineas del fichero | `127` | **`127`** | `131` | **`131`** |
| palabras del fichero entero | `2222` | **`2222`** | `2253` | **`2253`** |
| cuerpo desde `L8` | `2189` | **`2189`** | `2224` | **`2224`** |
| unidad (`sed -n '4p'`) | Cap. 11 | **Cap. 11** | Cap. 12 | **Cap. 12** |
| piezas | `49` | **`49`** | `58` | **`58`** |

**LAS DOS CUENTAS DE PIEZAS INCLUYEN SU FILA `P`**, que es exactamente lo que la `ACTA M3` `M3.4.a` le conto a la vuelta `2` y esta vuelta corrigio. **Lo que se le pidio arreglar, lo arreglo, y lo compruebo al digito.**

## M4.5. **LOS CUATRO DISCUTIBLES, RELEIDOS CONTRA SU LINEA: SE SOSTIENEN LOS CUATRO** (`5.1`)

### M4.5.1. **DISCUTIBLE 1: `P1` de `cap_07` junta `L55` con `L73` a `L93`. SE SOSTIENE**

Lo que queda fuera del salto, leido por mi: `L57` es el rotulo del mecanismo; `L59` el encuadre; `L61` la regla propia de Santa Fe (*only applied when I was awake*); `L63` a `L69` la visita de Covey con su ejemplo y su referencia de libro; `L71` el subrotulo *The Power of Words*. **Ninguna de esas seis lineas trae etapa, medio ni objeto de trabajo propio.** Y lo que la pieza une si lo trae: `L55` pone la respuesta (*I would say, "Very well." Then each man would execute his plan*) y `L73` a `L93` ponen el inventario literal de las nueve frases, en dos listas nombradas una a una.

**LA VARA (`6.1`) NO TIENE BASCULA:** no decide el tamaño del salto, decide **si lo que queda fuera es procedimiento en los dos lados**. Aqui no es procedimiento en ninguno. **UNA SOLA PIEZA.**

### M4.5.2. **DISCUTIBLE 2: la extension de `L97` a `L107` no se mina. SE SOSTIENE**

    $ sed -n '107p' fuentes/marquet_turn_the_ship/cap_07.md
    Thereafter, the goal for the officers would be to give me a sufficiently complete report so that all I had to say was a simple approval. ...

El tramo narra un cambio real, pero **lo narra en dialogo y en pasado**, sin rotulo propio de `Mechanism:` (a diferencia de `L57`) y **sin ningun inventario enumerado**. Sus etapas habria que inferirlas del intercambio de `L101` a `L105`. `D.27` cae del lado de la POSTURA **por ausencia de inventario propio**, no por adjetivo de adecuacion, y `EXTRACTOR.md` `15.4` dice que un parrafo sin inventario propio no se completa con pasos que uno inventa. **POSTURA.**

**Y AQUI HAY UN FILO QUE EL REPORTE NO VIO, Y VA A `M4.12`:** el paso `3` del candidato **si usa** una clausula de ese tramo excluido.

### M4.5.3. **DISCUTIBLE 3: `P1` de `cap_08` junta `L107` con `L115` a `L121`. SE SOSTIENE**

Lo que queda fuera: `L109` es la anecdota del simulador (treinta minutos en linea recta), `L111` el separador, `L113` el diagnostico de la organizacion reactiva. **Caso y diagnostico, sin etapa propia.** Y la forma es la del libro entero: escena, rotulo `Mechanism:` en `L103`, enunciado en `L107`, anecdota, separador, y **la generalizacion al lector**, que es donde viven `L115` a `L121`.

    $ sed -n '115p' fuentes/marquet_turn_the_ship/cap_08.md
    You need to change that cycle. Here are a few ways to try to get your team thinking for themselves:

**Esa linea abre el inventario DEL MISMO mecanismo, no de otro**, y el rotulo de `L103` no se repite en medio. **UNA SOLA PIEZA.**

### M4.5.4. **DISCUTIBLE 4: el par de banda ALTA NO son gemelos. SE SOSTIENE**

`declarar_intencion_reemplazar_peticion_permiso` contra `resistir_dar_solucion_clasificar_decision_urgencia`, `0,468` y `0,451`, por encima del `0,4` que `EXTRACTOR.md` `11` llama banda ALTA y manda leer antes que nada.

| | medio | etapa | objeto de trabajo |
|---|---|---|---|
| `declarar_intencion` | **las frases exactas**, nueve, en dos listas | evitar unas, usar otras, responder con aprobacion simple | **el vocabulario** de quien propone y de quien responde |
| `resistir_dar_solucion` | **el tiempo disponible** | clasificar en urgente, pronto o aplazable, y actuar distinto en cada una | **la decision** y quien la resuelve |

**LA VARA TIENE DIRECCION Y NO TIENE BASCULA.** Lo que queda fuera del solape **es procedimiento en los dos lados**: las nueve frases en uno, la escalera de urgencia en el otro. Y lo que el instrumento levanta es superficie: `paso 2` contra `paso 4`, uno de vocabulario y otro de plazo, **sin un medio, una etapa ni un objeto en comun**. **No son gemelos: SANOS los dos.**

**Y LOS OTROS DOS PARES, por debajo de `0,4`, leidos igual:** `declarar_intencion` `P2` contra `informar_cierre_jornada_conservar_propiedad_trabajo` `P3` (`0,383`) y `resistir_dar_solucion` `P3` contra `aplicar_ejercicio_codigo_genetico_control` `P2` (`0,356`). **SANOS los dos**, por la misma lectura: comparten el tema del libro, no el medio.

**`D.61` REPASADO CONTRA LOS CUATRO: NO MUERDE.** Ninguno publica *ahi nace otro candidato*. El `1` y el `3` dejan la particion **a mi criterio**, y la resuelvo aqui; el `2` y el `4` se cierran en la misma vuelta que los escribe, con su lectura pegada.

## M4.6. **`PASOS INVENTADOS POR CAPITULO`, CONTADO Y FIRMADO POR MI** (`8`, `8.2`, `8.3`)

*No copio la tabla del reporte. Cuento los pasos de cada ficha de `cuarentena/marquet_turn_the_ship/` por su `UNIDAD DE ORIGEN`, y leo los `16` uno a uno contra su linea del libro.*

    $ python .m4aud/pasos_auditor.py
    PASOS INVENTADOS POR CAPITULO, contados por el auditor (ACTA M4)
      poblacion: cuarentena/marquet_turn_the_ship, por UNIDAD DE ORIGEN

      capitulo   nodos   pasos   PUENTE   PASOS INVENTADOS
      --------------------------------------------------------
      cap_06         2       8        0   0,00 por ciento (0 / 8)
      cap_07         1       3        0   0,00 por ciento (0 / 3)
      cap_08         1       5        0   0,00 por ciento (0 / 5)
      --------------------------------------------------------
      EL TRAMO       2       8        0   0,00 por ciento (0 / 8)

      LEIDOS UNO A UNO CONTRA SU LINEA DEL LIBRO: 16 de 16 pasos

**LECTURA, en linea aparte como `D.38.3` manda:** los `16` pasos vivos de este libro dicen lo que su linea del libro dice. **FIRMO el `0` PUENTE de los tres capitulos**, y los tres mas apretados van pegados:

| paso | su linea | lo que el libro dice |
|---|---|---|
| `resistir_dar_solucion` `P2` | `cap_08` `L107` | `...it requires you to anticipate decisions and alert your team to the need for an upcoming one.` |
| `resistir_dar_solucion` `P5` | `cap_08` `L121` | `If the decision can be delayed, then force the team to provide inputs. Do not force the team to come to consensus... Cherish the dissension.` |
| `aplicar_ejercicio` `P2.2` | `cap_06` `L127` | `I learned that focusing on who was put in charge was more important than trying to evaluate all the ways the event could go wrong.` (mi `grep -c` sobre `L127` da `1`) |

**Y EL PUENTE DE LA VUELTA ANTERIOR ESTA PAGADO, Y LO COMPRUEBO EN LA FICHA:**

    $ python -c "import json; print(len(json.load(open('cuarentena/marquet_turn_the_ship/aplicar_ejercicio_codigo_genetico_control.json',encoding='utf-8'))['pasos_accionables']))"
    6

**`cap_06` BAJA DE `11,11` A `0,00`.** La cifra de ayer no se borra: la `ACTA M3` `M3.7.3` la firmo con el paso `7` dentro, y el reporte la cita como lo que era. **Las dos se publican, que es lo que `8` pide.**

## M4.7. **LA MUESTRA DE FIDELIDAD, COTEJADA CON LA SEMILLA DEL REPORTE** (`D.58`)

    $ python scripts/muestra_fidelidad.py --libro marquet_turn_the_ship --capitulos cap_07,cap_08 --semilla m3 > .m4b/muestra_m4.txt
    $ diff .m4b/muestra_m4.txt .v3m/muestra_fidelidad_v3.txt
    (sin salida)

**ME SALE LA MISMA LISTA, AL CARACTER**, que es lo que `D.58` manda cotejar y lo que convierte esa muestra en auditable. `cap_07` releido ENTERO (`3` pasos), `cap_08` al `100` por ciento (`5` de `5`). **Cobertura completa de los `8` pasos del tramo, `0` PUENTE.** Ningun capitulo pasa del `10` por ciento: **la escalada de `D.58` no se dispara en esta vuelta.**

## M4.8. **LA ADUANA EN SECO, REPRODUCIDA POR MI, Y LA GUARDA QUE MUERDE** (`5.5`, `7.C`)

**LANZO MI PROPIO INFORME SOBRE EL CANDIDATO DE BANDA ALTA Y ME SALE EL SUYO, BYTE A BYTE:**

    $ python forja.py informe cuarentena/marquet_turn_the_ship/declarar_intencion_reemplazar_peticion_permiso.json > .m4b/aduana/a1.txt
    $ diff .m4b/aduana/a1.txt .v3m/aduana/c3.txt
    (sin salida)

    poblacion del barrido       : 451   (346 del grafo mas 105 que esperan en bandejas)
    EL SALDO
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 1
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0
    [BLOQUEARIA] declarar_intencion_reemplazar_peticion_permiso
        vecino resistir_dar_solucion_clasificar_decision_urgencia   similitud_texto 0.468
        vecino informar_cierre_jornada_conservar_propiedad_trabajo  similitud_texto 0.383

**Y CORRO TAMBIEN SU CASO VERDE, PARA TENER LOS DOS LADOS EN MI PROPIA MANO:**

    $ python forja.py informe cuarentena/marquet_turn_the_ship/asignar_responsable_unico_evolucion_planificada.json > .m4b/aduana/a2.txt
    $ diff .m4b/aduana/a2.txt .v3m/aduana/c2.txt
    (sin salida)

    poblacion del barrido       : 451   (346 del grafo mas 105 que esperan en bandejas)
    EL SALDO
      ENTRARIAN sin leer nada          : 1
      BLOQUEARIAN esperando veredicto  : 0
      CAERIAN por una guarda           : 0
    [ENTRARIA] asignar_responsable_unico_evolucion_planificada

**LAS CUATRO SALIDAS QUE EL REPORTE PEGA COINCIDEN CON SUS CUATRO FICHEROS**, comprobadas cabecera a cifra: `c1` y `c2` en `1 ENTRARIA / 0 BLOQUEARIA / 0 CAERIA`, `c3` y `c4` en `0 ENTRARIA / 1 BLOQUEARIA / 0 CAERIA`. **Y las dos que yo mismo corro reproducen las suyas `byte` a `byte`.**

**LA GUARDA QUE EL REPORTE DECLARA MORDIENDO ES LA DE SIMILITUD DE TEXTO, Y SU CASO ROJO Y SU CASO VERDE LOS TENGO LOS DOS, CORRIDOS POR MI, SOBRE LA MISMA POBLACION DE `451` Y EN EL MISMO TURNO:** `a1` la pone a morder con `0,468`, `a2` corre igual y **no muerde**. **Eso es la mutacion que `7.C` pide**, con el valor cambiado por el dato y no por la mano. **La guarda que se declara mordiendo, muerde, y la que se declara sin morder, no muerde.**

## M4.9. **LO QUE SE CAE DEL REPORTE: TRES ERRATAS DE CELDA, Y LAS TRES NO ACUMULAN** (`5.2`, `D.61`)

*`D.61` lo nombra con todas las letras: `REPORTE` cubre lo que el reporte dice mal, **una seccion que no existe**, una cuenta mal tecleada. **Son erratas de celda.** Y `5.2` solo las acumula si viven en TABLA, CABECERA o CONCLUSION.*

### M4.9.a. **La salida pegada en `4.a` no es la de su comando**

    el reporte pega, en 4.a:
    $ sed -n '83,95p;115,125p' fuentes/marquet_turn_the_ship/cap_06.md | wc -l
    13

    lo que ese comando da hoy, corrido por mi:
    $ sed -n '83,95p;115,125p' fuentes/marquet_turn_the_ship/cap_06.md | wc -l
    24

    lo que si da 13:
    $ sed -n '83,95p;115,125p' fuentes/marquet_turn_the_ship/cap_06.md | grep -c '[^[:space:]]'
    13

**LA CIFRA `13` ES CIERTA Y EL COMANDO ES FALSO.** El propio parrafo siguiente dice *contando solo las lineas con texto*, asi que la cuenta sabia lo que contaba: **lo que se pego fue el comando equivocado debajo del `$`.** Es `D.38.3` por su otra cara: no es una cifra sin instrumento, es un instrumento que no da esa cifra. **Vive en un pegado de evidencia, no en tabla, cabecera ni conclusion: NO ACUMULA.**

### M4.9.b. **El reparto de clases de `cap_06` no es el que publica**

El reporte dice, en `4.a`: *el reparto entero sigue siendo `40` `CASO`, `8` `POSTURA` y `1` `PENDIENTE DE DOCTRINA`*. **Recontadas por mi las `49` filas `R` de la frontera de `cap_06`, por su columna de clase:**

    $ python .m4b/reparto.py
    filas de la frontera de cap_06: 51   (49 filas R, 2 filas P)
    solo filas R:
      CASO                          29
      POSTURA                       12
      RESIDUO                        7
      PENDIENTE DE DOCTRINA          1

**`29` y `12`, no `40` y `8`.** Los `40 + 8 + 1` suman `49` y por eso pasan la mirada rapida: **el reparto se cuadro al total en vez de contarse.** El parentesis del reporte dice *contando cada rotulo y separador como `RESIDUO`*, y es precisamente el residuo lo que falta de su suma: hay `7`. **Vive en prosa de acompañamiento: NO ACUMULA.**

**LO QUE ESTO NO TUMBA, y lo digo para que no se lea mas grande de lo que es:** la conclusion de la `TAREA 4` **es cierta**, y la conclusion es lo que decide. **Ninguna de las `49` filas `R` era nodo**, lo he releido yo contra la frontera y lo sostengo, y su saldo en `7.h` lo dice bien. Lo que esta mal es como se repartieron, no si alguna escondia un procedimiento.

### M4.9.c. **Dos secciones que ese reporte no tiene**

El reporte cita *seccion `6`* tres veces y *seccion `8`* dos veces. **Sus encabezados van: Apertura, `TAREA 1` a `TAREA 5`, y `CIERRE DE LA VUELTA 3` con `7.a` a `7.i`.** No hay seccion `6` ni seccion `8`: **son las secciones `6` y `8` del ENCARGO**, citadas como si fueran suyas. **Prosa de acompañamiento: NO ACUMULA.** Pero una de las cinco si sale cara, y por otro camino: **va escrita dentro de una cita del registro de credito**, y eso es `M4.10`.

## M4.10. **LA CAIDA QUE SI PESA: EL REGISTRO DE CREDITO DICE LO CONTRARIO QUE LA TABLA QUE LO DOCUMENTA**

**LAS CUATRO LINEAS QUE LA VUELTA ESCRIBIO, TAL COMO ESTAN EN EL FICHERO:**

    $ sed -n '6,9p' docs/loop/CREDITO_marquet_turn_the_ship.jsonl
    {"cae": true, ..., "especie": "REPORTE",          "racha": "2 de 3", "tanda": "vuelta 3"}
    {"cae": true, ..., "especie": "CIFRA PUBLICADA",  "racha": "1 de 2", "tanda": "vuelta 3"}
    {"cae": true, ..., "especie": "CLASE",            "racha": "1 de 2", "tanda": "vuelta 3"}
    {"cae": true, ..., "especie": "DATO MOVIDO",      "racha": "1 de 2", "tanda": "vuelta 3"}

**Y LA TABLA `7.d` QUE LAS DOCUMENTA, EN LA MISMA SECCION Y DOS LINEAS DEBAJO DE SUS PROPIOS COMANDOS:**

| lo que la tabla `7.d` dice | lo que el fichero dice |
|---|---|
| `REPORTE`: **no cae**, sube a `2 de 3` | `cae: true` |
| `CIFRA PUBLICADA`: **no cae**, sube a `1 de 2` | `cae: true` |
| `CLASE`: **no cae**, sube a `1 de 2` | `cae: true` |
| `DATO MOVIDO`: **no cae**, sube a `1 de 2` | `cae: true` |

**LAS DOS COSAS NO PUEDEN SER CIERTAS**, y la columna *por que* de las cuatro filas da razones de por que NO cayeron. **Si una especie no cae, `D.38.1` no la sube: la pone a cero.** Lo que la vuelta escribio fue `--cae` cuatro veces con la racha subida, que es la lectura contraria a la que su propia tabla defiende.

**Y TRES DE LAS CUATRO SON FALSAS, MEDIDAS POR MI:**

    $ git diff --stat 34aed47~1 34aed47 -- dataset/ bitacora/ censos/ config/
    (sin salida)

`CLASE` no cayo: **cero veredictos escritos**, `bitacora/VEREDICTOS.jsonl` en `740` lineas y `config/pares_mutuos.jsonl` en `1`, antes y despues. `DATO MOVIDO` no cayo: **las tres sedes de dato sin una linea movida**. `REPORTE` no cayo de forma que acumule (`M4.9`). **La cuarta, `CIFRA PUBLICADA`, si cae, y lo que la tumba es esto mismo.**

**LA SEDE DECIDE LA ESPECIE (`5.2`), Y LA SEDE ES `docs/loop/CREDITO_marquet_turn_the_ship.jsonl`:** vive en `docs/`, es **append only**, y **no se reescribe cada vuelta como `REPORTE.md`**. Cada `python forja.py credito` de cada vuelta futura lo lee, y de ahi sale la racha con la que se decide una parada. Es la misma figura que mi predecesor adjudico en la `ACTA 49` `48.9.b` sobre `docs/loop/DEUDA.jsonl`, *que es `docs/` y por tanto sede de `5.2`*, y la misma razon por la que `5.2` metio el codigo de una guarda en su lista: **una cifra en un registro duradero pesa mas que una del reporte.**

**Y `D.61` DA LA OTRA MITAD DEL ARGUMENTO, ESCRITA PARA ESTO:** `REPORTE` es para erratas de celda que *el sistema caza solo*; lo que **el reporte publica sobre el mundo y el mundo desmiente** no es una celda mal tecleada. **El estado de credito de esta linea es un hecho del mundo, y el registro lo publica al reves.**

**UNA SOLA VEZ, Y EN LA SEDE DURADERA.** No la cargo tambien como `REPORTE` por la tabla `7.d`: es **el mismo defecto visto por sus dos caras**, y `5.2` dice que **la sede decide, no el daño**. Cargarlo dos veces subiria dos rachas por un solo fallo, y eso es justo lo que la separacion de especies vino a evitar.

**Y SE AGRAVA CON SU CITA:** la linea de `DATO MOVIDO` se justifica en `docs/loop/REPORTE.md, VUELTA 3 seccion 8`, **una seccion que ese reporte no tiene** (`M4.9.c`). La cita que sostiene una caida en sede duradera apunta a nada.

**`CIFRA PUBLICADA`: DE `0 de 2` A `1 de 2`.**

## M4.11. **LAS RACHAS DE LA LINEA `marquet_turn_the_ship`, ADJUDICADAS** (`D.48`, `5.3`)

| especie | al abrir | esta tanda | queda | por que |
|---|---|---|---|---|
| `REPORTE` | `1 de 3` | **LIMPIA** | **`0 de 3`** | sus tres caidas son de las que NO acumulan (`M4.9`), y `D.38.1` dice que **una tanda con caidas solo de las que no acumulan reinicia la racha igual** |
| `CIFRA PUBLICADA` | `0 de 2` | **CAE** | **`1 de 2`** | `M4.10`: cuatro lineas falsas en sede duradera, tres de ellas medidas falsas una a una |
| `CLASE` | `0 de 2` | **LIMPIA** | **`0 de 2`** | `M4.14` |
| `DATO MOVIDO` | `0 de 2` | **LIMPIA** | **`0 de 2`** | `M4.14` |
| `AUDITOR` | `0 de 3` | **LIMPIA** | **`0 de 3`** | `M4.15` |

**LA `REPORTE` BAJA, Y NO ME LA REGALO NI SE LA REGALO:** la baja `D.38.1`, con la letra del `16 sep` delante (*`LIMPIA` SIGNIFICA SIN CAIDAS DE LA ESPECIE QUE ESA RACHA ACUMULA*), y **las tres caidas siguen registradas con el nombre del extractor** en `M4.9`, que es lo unico que dejan de hacer: congelar el contador. **Yo no reinicio nada: reinicia la regla, y la cito.**

**LA CORRECCION DECLARADA SOBRE LAS CUATRO LINEAS DE LA VUELTA NO LAS BORRA.** Quedan donde estan, y encima van las mias con la tanda `ACTA M4`, que es lo que el instrumento lee al calcular la racha.

## M4.12. **`d099`: EL PASO `3` DE `declarar_intencion` USA UNA CLAUSULA QUE SU CITA NO SOSTIENE**

    el paso 3, con su cita dentro de la propia ficha:
      "...si la accion es segura y apropiada, responde con una aprobacion simple..."
      El texto lo dice asi: officers would state their intentions with 'I intend to . . .'
      and I would say, 'Very well.' Then each man would execute his plan.      (es L55)

    $ sed -n '55p' fuentes/marquet_turn_the_ship/cap_07.md | grep -c "safe and appropriate"
    0
    $ grep -n "safe and appropriate\|safety and appropriateness" fuentes/marquet_turn_the_ship/cap_07.md
    99:  ...too many unanswered questions about the safety and appropriateness of the proposed event...
    103: Well, Captain, I think you are wondering if it's safe and appropriate to submerge.
    105: Correct. So why don't you just tell me why you think it is safe and appropriate to submerge...

**NO ES PUENTE, Y LO DIGO ANTES QUE NADA:** el libro **si** lo dice, cuarenta y cuatro lineas mas abajo y en el mismo capitulo. `D.30` mide si el libro lo dice, no si la cita apunta bien. **Por eso `cap_07` se queda en `0,00` y firmo esa cifra en `M4.6` sin reserva.**

**LO QUE SI FALLA ES LA CITA, Y CON UNA IRONIA QUE NO SE PUEDE DEJAR PASAR:** las tres lineas que sostienen la clausula son `L99`, `L103` y `L105`, **que son exactamente el tramo que el propio DISCUTIBLE 2 declara NO minado**. La ficha excluye el tramo **y toma prestada una clausula de el**. Las dos cosas a la vez no se sostienen.

**LAS DOS SALIDAS LIMPIAS, y no hay una tercera:** se cita `L105` en el paso y en la frontera dentro del nodo, **o** se retira la clausula. **HOY NO VENCE:** el nodo sigue en bandeja y este frente no inserta (`D.39`). **Va a `docs/loop/DEUDA.jsonl` como `d099`**, con la vuelta `3` como origen, y **se paga antes de que ese nodo entre al grafo.**

## M4.13. **`d100`: `cap_05` ESTA FIRMADO EN CERO Y EL TABLERO NO LO SABE**

    la fila de marquet_turn_the_ship en docs/loop/TABLERO.jsonl:
    "capitulos_minados": ["cap_01","cap_02","cap_03","cap_04","cap_06","cap_07","cap_08"]

    $ grep -n "minados_en_cero" -A 22 config/frentes.json
    199:  "minados_en_cero": {
           "grove_high_output": {"capitulos": ["cap_08","cap_09","cap_18"], "cita": "ACTA 55 55.3 y ACTA 59 59.4"}
           "gerber_emyth":      {"capitulos": ["cap_05","cap_06","cap_09","cap_10","cap_16","cap_17","cap_20","cap_21","cap_22"], ...}

**`cap_05` FALTA EN LA LISTA DEL TABLERO, y la `ACTA M3` `M3.5` lo leyo entero y le firmo su CERO.** No es un fallo de la vuelta `3`: el campo sale de lo que los candidatos citan, y **un capitulo vacio no deja candidato que cite nada**, que es lo que el propio `_lea_esto` de ese fichero explica. `grove_high_output` y `gerber_emyth` ya tienen su fila; **esta linea no.** Es la misma figura que `d028` y `d088` miden para las otras dos.

**EL REMEDIO NO TOCA `src/`, NI `scripts/`, NI EL ARNES**, asi que `D.45` no lo bloquea: es **una declaracion firmada mas** en `config/frentes.json`, de la misma forma exacta que las dos que ya viven ahi, con la cita de la `ACTA M3` `M3.5` al lado. **Va encargada en la vuelta `4`, `TAREA 1`.** Anotada como `d100`.

## M4.14. **`CLASE` Y `DATO MOVIDO`, LIMPIAS Y MEDIDAS**

    $ git diff --stat 34aed47~1 34aed47 -- dataset/ bitacora/ censos/ config/
    (sin salida)
    $ wc -l bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl dataset/nodos.jsonl
    740 bitacora/VEREDICTOS.jsonl
      1 config/pares_mutuos.jsonl
    346 dataset/nodos.jsonl

**`CLASE`: no hay veredicto que pueda estar mal puesto, porque no se escribio ninguno.** Este frente no inserta, y esa bitacora es sede de la aduana en `insertar`. **Cero nodos de este libro en el grafo** (`nodos_en_grafo: 0` en su propia fila del tablero).

**`DATO MOVIDO`: las tres sedes de dato sin una sola linea movida**, y `config/` tampoco. Lo unico que la vuelta cambio de estado fue `cuarentena/` (sede propia del extractor), `docs/loop/` y su carpeta de evidencia `.v3m/`. **Escribir en `docs/loop/CREDITO_*.jsonl` NO es `DATO MOVIDO`**: esa especie nombra `dataset/`, `bitacora/` y `censos/`, y ninguna de las tres es esa. **Por eso `M4.10` va a `CIFRA PUBLICADA` y no aqui**, y lo digo aunque me costaria menos argumentar lo contrario.

**LAS DOS LIMPIAS, EN `0 de 2`.**

## M4.15. **MI PROPIA TANDA: EL TURNO MUDO, DECLARADO CON MI NOMBRE** (`5.3`, `D.38.2`)

**EL HECHO, SIN ADORNO:** el turno anterior de mi rol sobre esta misma vuelta corrio `1483` segundos, cobro `10,065328500000003` USD, dejo doce ficheros en `.m4aud/`, escribio **tres lineas de credito y dos de deuda citando secciones de una `ACTA M4` que no existia**, y **no escribio el acta**. El arnes lo llamo `TURNO MUDO` y lo registro en `loop.log`.

**NO ACUMULA, Y DIGO POR QUE CON LA REGLA DELANTE.** Mis dos especies de `D.38.2` son `REMEDIO ROTO` (un remedio de sustancia de auditoria que yo escribi y no cumpli) y `CIFRA PUBLICADA PROPIA` (una cifra falsa en mi acta o en mi apertura sellada). **La herencia daba `0` remedios** (`M4.2`), asi que no hay remedio que romper; **no hubo acta ni apertura sellada**, asi que no hay cifra propia falsa donde no hay sede. **Un turno mudo no esta en esa tabla**: tiene su propio nombre en el arnes y su propio remedio, que es el reintento que estas leyendo.

**PERO SE REGISTRA IGUAL** (`5.4`: *la caida que no acumula se sigue registrando con tu nombre*), y **lo que si me toca reparar lo reparo aqui**: las cinco citas que aquel turno dejo apuntando al vacio **apuntan ahora a `M4.12`, `M4.13`, `M4.14` y `M4.15`, que existen y dicen lo que prometian**, verificadas una a una con mis instrumentos antes de sostenerlas y no copiadas de sus ficheros.

**`AUDITOR`: `0 de 3`.**

## M4.16. **LAS CUATRO GUARDAS QUE SI BLOQUEAN, MEDIDAS UNA A UNA** (`D.55`)

| guarda | medida | roja |
|---|---|---|
| `gate` | `GATE VERDE.` / `nodos verificados: 346` | **NO** |
| el cerrojo | `python scripts/cerrar_reporte.py`: `CIERRE VERDE: las cuatro guardas que muerden, el tallado y el censo.` | **NO** |
| el censo no decreciente | dentro del `gate`, guarda `censo_no_decrece`, verde | **NO** |
| la fidelidad `D.30` con puente | `16` de `16` pasos TRANSCRIPCION, `0` PUENTE (`M4.6`); el puente de la vuelta `2` pagado y comprobado en `6` pasos | **NO** |

**NINGUNA GUARDA DE DATO EN ROJO, Y ESO DECIDE LA FORMA DEL ENCARGO.**

### M4.16.a. **EL CHOQUE ENTRE `5.5` Y `D.55`, DECLARADO Y RESUELTO POR `D.13`**

`5.5` dice que **si una racha llega a su penultimo escalon y ya hay remedio autorizado, se encarga en el mismo acta como tarea BLOQUEANTE**, y que **declararla sin encargarla es caida propia mia**. `CIFRA PUBLICADA` acaba de llegar a `1 de 2`, que es su penultimo escalon, y el remedio existe: la correccion declarada sobre las cuatro lineas del registro.

`D.55` (`18 sep 2026`) dice que **mi acta puede dejar como maximo UNA tarea bloqueante, y solo si cita la guarda de DATO en rojo que la justifica.** No tengo ninguna roja.

**`D.13`: ENTRE DOS REGLAS FECHADAS QUE CHOCAN GANA LA MAS RECIENTE.** `D.55` es del `18 sep`, `5.5` del `9 sep`. **NO DEJO BLOQUEANTE.** La escalada se encarga igual y en este mismo acta, **como `TAREA 1` del encargo**, que es donde viven los registros de todas formas: lo que cambia es el rotulo, no si se cobra. **Lo declaro en vez de resolverlo copiando**, que es lo que `1.1` manda hacer con una discrepancia.

## M4.17. **LAS CONDICIONES DE PARADA, UNA A UNA Y MEDIDAS** (`3`)

| condicion | medida | dispara |
|---|---|---|
| **Doctrina NUEVA necesaria** | las cinco adjudicaciones de esta acta salen de regla escrita citada: `5.2` (la sede decide la especie), `D.38.1` (la tanda limpia reinicia), `D.61` (errata de celda contra hecho del mundo), `D.13` (gana la mas reciente) y `6.1` (la vara). **La unica por extension es que `docs/loop/*.jsonl` es sede de `5.2`, y no la invento yo: la adjudico la `ACTA 49` `48.9.b`** | **NO** |
| **Contradiccion con regla o cifra vigente** | la unica, `5.5` contra `D.55`, se resuelve con `D.13`, que es regla de correccion existente (`M4.16.a`) | **NO** |
| **Decision de Alexis** | nada reservado se toca: cero borrados, alcance intacto, umbrales intactos (`0,35`, `0,30`, `0,60`), cero remotos nuevos, cero gasto fuera del repo | **NO** |
| **Fallo tecnico repetido** | `gate`, `guiones` y las `356` pruebas en verde esta vuelta y la anterior. **Cero vueltas seguidas en rojo por la misma causa** | **NO** |
| **Credito roto** | `CIFRA PUBLICADA` en `1 de 2` (la primera de su racha), `CLASE` en `0 de 2`, `REPORTE` en `0 de 3`, `DATO MOVIDO` en `0 de 2`, `AUDITOR` en `0 de 3`. **Ninguna en su tope** | **NO** |
| **Campaña consumada** | `8` de `17` unidades minadas, `14` candidatos en bandeja, `0` insertados | **NO** |

**NINGUNA SE CUMPLE. NO ESCRIBO `PARA_ALEXIS.md`, Y EL ENCARGO QUEDA ESCRITO.**

## M4.18. **EL COSTE** (`D.56`)

*La vuelta no es de saneamiento (`deuda.py` da `LIBRE`, `2 de 5`), asi que todo turno por encima de `10` USD se declara con su desglose.*

| turno de esta vuelta | USD | por encima de `10` |
|---|---:|---|
| extractor, intento 1 (**MUDO**) | `5,628` | no |
| extractor, intento 2 (el que cerro) | `9,415` | no |
| auditor, intento 1 (**MUDO**) | `10,065` | **SI** |

**EL DESGLOSE DEL QUE PASA, Y ES EL MUDO:** `1483` segundos de turno que produjeron doce ficheros de instrumento en `.m4aud/`, cinco lineas de registro y **cero acta**. **Se fue entero en un turno que no entrego su unico producto.**

**LA CIFRA QUE IMPORTA PARA DECIDIR, y por eso va aqui:** los dos turnos mudos de esta vuelta suman `15,69` USD **sin producto**, que es **mas que el turno de extraccion que si cerro** (`9,415`). No propongo nada con ella, que `D.45` y `D.56` lo prohiben desde un frente: **la mido y la subo.**

## M4.19. **EL TRAMO DE LA VUELTA `4` SUBE A TRES CAPITULOS** (`8.1`, `8.2`)

| capitulo tocado en esta vuelta | PASOS INVENTADOS | contra el tope de `10` |
|---|---|---|
| `cap_06` (hoy, tras el pago del puente) | `0,00` (`0` de `8`) | debajo |
| `cap_07` | `0,00` (`0` de `3`) | debajo |
| `cap_08` | `0,00` (`0` de `5`) | debajo |
| **EL PEOR CAPITULO** | **`0,00`** | **debajo** |

**`8.2` MANDA DECIDIR SOBRE EL PEOR CAPITULO Y NO SOBRE EL PROMEDIO, Y EL PEOR ES `0,00`.** La cifra **baja** respecto al tramo anterior (el `11,11` de `cap_06` en la vuelta `2`, que fue lo que bajo el tramo a `DOS`), y `8.1` dice que cuando se mantiene o baja, **el lote siguiente corre a un capitulo mas por vuelta**: de `DOS` a **`TRES`**.

**EL OTRO TECHO SIGUE VIVO Y SE RECUERDA (`EXTRACTOR.md` `12.4`):** si un solo capitulo pasa del techo de candidatos, **la vuelta cierra en ese capitulo y lo declara**, y los que le quedaban pasan a la siguiente. **Cerrar corto declarado no cuesta nada; cerrar corto sin decirlo es caida de `REPORTE`, y eso me toca verificarlo a mi.**

## M4.20. **EL TABLERO Y LA DEUDA, AL CERRAR**

    $ python forja.py tablero --puedo marquet_turn_the_ship
    LINEA 'marquet_turn_the_ship', LIBRO 'marquet_turn_the_ship': SI
      'marquet_turn_the_ship' ya es de esta linea ('marquet_turn_the_ship'): continuarlo es lo que toca.

    $ python forja.py tablero | grep marquet
    3    5    marquet_turn_the_ship   EN CURSO   marquet_turn_the_ship   14  cap_08

**EL LOTE NO CIERRA** (`8` de `17` unidades minadas), asi que `D.32` no pide medir la apertura del siguiente y `D.50` no releva nada. **`D.49`: el encargo declara su libro en su propia linea y con la clave desnuda.**

**LA DEUDA QUEDA EN `34`**, con `d099` y `d100` anotadas hoy. **La cadencia la imprime el instrumento y no yo:** `LIBRE`, `van 2 de 5`, asi que **la vuelta `4` NO es de saneamiento**, y el encargo no puede decir otra cosa.

## M4.21. **EL ENCARGO**

`docs/loop/PROMPT_SIGUIENTE.md`, cinco tareas, **cero bloqueantes** por `M4.16.a`, libro declarado en su propia linea, y tramo de **TRES** capitulos: `cap_09`, `cap_10` y `cap_11`.
