# VUELTA 61, lote 7 (`grove_high_output`), CLASE EXTRACCION

*Corro con `claude-sonnet-5`. El auditor sigue en Opus 5. Encargo escrito por el auditor al cerrar la `ACTA 59`.*

## 61.X. CIERRE DE LA VUELTA: QUE QUEDO HECHO Y QUE NO
aduanas cerradas con su salida guardada : 2 de 3 (priorizar_lista_entrenamiento_subordinados, desarrollar_primer_curso_entrenamiento)
candidatos en la bandeja al cerrar      : 91
la cuenta del libro (TAREA 3)           : NO HECHA
el tablero reescrito (TAREA 4)          : NO
lo que queda para la vuelta 62          : ...

## 61.0. LA APERTURA, MEDIDA ANTES DE LA PRIMERA OPERACION (`EXTRACTOR.md` 4)

**Lo primero, `EXTRACTOR.md` 1: commitear lo pendiente antes de tocar nada.** No habia candidatos ni
restos de intento mudo esta vez, solo los cuatro ficheros que el arnes toca cada vuelta:

    $ git add docs/loop/TABLERO.jsonl docs/loop/loop.log docs/loop/ultimo_auditor.json docs/loop/ultimo_extractor.json
    $ git commit -m "Sincroniza loop.log, TABLERO.jsonl, ultimo_auditor.json y ultimo_extractor.json antes de abrir la vuelta 61"
    $ git push
    GATE VERDE.
      nodos verificados: 346
    [extraccion-mundo-11 7aaaa78] Sincroniza loop.log, TABLERO.jsonl, ultimo_auditor.json y ultimo_extractor.json antes de abrir la vuelta 61
     4 files changed, 14 insertions(+), 2 deletions(-)
    To https://github.com/Alexcat84/forja-nodos.git
       15b7ed3..7aaaa78  extraccion-mundo-11 -> extraccion-mundo-11

**LA IDENTIDAD, LEIDA DE GIT** (`EXTRACTOR.md` 5):

    $ git rev-parse HEAD && git log -1 --format=%cI && git rev-parse --abbrev-ref HEAD
    7aaaa78d530de91bdb30204abe087340748e0cad
    2026-09-21T04:47:35-04:00
    extraccion-mundo-11

**EL ESTADO, MEDIDO ANTES DE LA PRIMERA OPERACION PROPIA DE ESTA VUELTA** (`EXTRACTOR.md` 4), justo
tras el commit de sincronizacion de arriba y antes de tocar la bandeja de `grove_high_output`:

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta,
               cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones,
               censo_no_decrece

    $ wc -l bitacora/VEREDICTOS.jsonl dataset/nodos.jsonl config/pares_mutuos.jsonl
      740 bitacora/VEREDICTOS.jsonl
      346 dataset/nodos.jsonl
        1 config/pares_mutuos.jsonl

    $ ls cuarentena/grove_high_output/*.json | wc -l
    90

**`346`, `740`, `1` y `90` coinciden con lo que el encargo de la `61` da como cierre de la `60`,
medido por el auditor** (*al cerrar la 60 era 346 nodos, 740 veredictos, 1 par mutuo y 90 en la
bandeja de grove*). Nadie toco el grafo entre una vuelta y otra, tal como `D.39` promete mientras el
lote `7` siga abierto.

## 61.1. TAREA 1. LOS REGISTROS (`ACTA 59` `59.7` a `59.11`)

**Lei `ACTA 59` secciones `59.7` a `59.11` enteras.** Lo que dicen, en una linea cada una, citando
sin repetir el argumento (modo austero, `D.47`):

- `59.7`: el reporte de la `60` termina en la TAREA `2` y no declara el cierre corto que
  `EXTRACTOR.md` `12.4` obliga a declarar. Caida de especie `REPORTE`.
- `59.8`: la cabecera de la `60` prometia *la mineria del libro CERRADA* y *las citas de fidelidad
  pegadas*, y ninguna de las dos estaba. Sede que acumula (`5.2`).
- `59.9`: la fila `P21` de `cap_18` decia *cap_01 a cap_09 ya insertadas en dataset* cuando el grafo
  trae un solo nodo de grove (`revisar_tres_preguntas_valor_carrera`). No toca la adjudicacion, solo
  donde dice que vive el procedimiento.
- `59.10`: el auditor corrio el `forja.py informe` del candidato `1`
  (`priorizar_lista_entrenamiento_subordinados`) que nadie habia guardado, con salida en
  `.v61aud/informe_1_priorizar.txt`: `BLOQUEARIA` con `4` vecinos sobre poblacion `439`. Adjudica en
  `59.10.a` el par `priorizar` contra `desarrollar` como `CONTINUA` (no `REPITE`), leido por los
  pasos, no por la senial.
- `59.11`: el tablero se quedo en `cap_16` porque la `60` no corrio `tablero --escribir`. Es la TAREA
  `4` de esta vuelta.

**LOS REGISTROS DE LA TANDA `ACTA 59`, YA ESCRITOS POR EL AUDITOR, LEIDOS Y CITADOS SIN
REESCRIBIR** (`EXTRACTOR.md`, encargo de la `61`):

    $ tail -2 docs/loop/CREDITO_serial.jsonl
    {"cae": true, ..., "especie": "REPORTE", "racha": "2 de 3", "tanda": "ACTA 59", "vuelta": 60}
    {"cae": true, ..., "especie": "AUDITOR", "racha": "2 de 3", "tanda": "ACTA 59", "vuelta": 60}

**`REPORTE` sube a `2 de 3`** por lo de `59.7` a `59.9`, y **`AUDITOR` sube a `2 de 3`** por el techo
de reloj sin medir y la banda publicada como punto (`59.10`, tercera fila de su tabla). Las dos
tandas anteriores (`ACTA 58`, `59.13` de esta) siguen `0 de 2` para `CLASE`, `CIFRA PUBLICADA` y
`DATO MOVIDO`: la `60` no escribio veredicto ni toco sede duradera.

    $ tail -2 docs/loop/DEUDA.jsonl
    d088 (vuelta 60): capitulos_minados registra los capitulos que PRODUJERON candidato, no los que
      se LEYERON. Congelada por D.56, no se abre.
    d089 (vuelta 60): la 60 corrio la aduana del candidato 1 y no guardo su salida (D.33: ningun
      ultimo_*.json es sede). Tercera vez que se pierde una medicion por no redirigir el informe a
      fichero. Remedio encargado en la TAREA 2 de esta vuelta 61.

**`d089` es exactamente la TAREA `2` de esta vuelta**, y por eso cada informe de abajo se guarda a
fichero antes de tocarlo.

## 61.2. TAREA 2. CIERRA LA ADUANA DE LOS TRES CANDIDATOS, DE UNO EN UNO Y GUARDANDO CADA SALIDA

**LO PRIMERO, DE COHERENCIA: DEVUELVE EL TERCERO A LA BANDEJA.** Los tres candidatos de `cap_17`
estaban igual de sin verificar y dos se habian quedado dentro de `cuarentena/grove_high_output/` y
uno fuera, en `.v60ext/pendientes/` (`ACTA 59` `59.10` final). `D.39` deja los tres en cuarentena
mientras el lote `7` siga abierto, asi que la bandeja es su sitio:

    $ ls -la --time-style=full-iso .v60ext/pendientes/pedir_critica_anonima_curso_entrenamiento_dictado.json
    -rw-r--r-- 1 AlexDesk 197609 4539 2026-09-21 04:01:23.861730600 -0400 .v60ext/pendientes/pedir_critica_anonima_curso_entrenamiento_dictado.json

    $ git mv .v60ext/pendientes/pedir_critica_anonima_curso_entrenamiento_dictado.json cuarentena/grove_high_output/pedir_critica_anonima_curso_entrenamiento_dictado.json

    $ ls -la --time-style=full-iso cuarentena/grove_high_output/pedir_critica_anonima_curso_entrenamiento_dictado.json
    -rw-r--r-- 1 AlexDesk 197609 4539 2026-09-21 04:01:23.861730600 -0400 cuarentena/grove_high_output/pedir_critica_anonima_curso_entrenamiento_dictado.json

    $ ls cuarentena/grove_high_output/*.json | wc -l
    91

**`91` es `90` mas el candidato devuelto.** El contenido no se toco (mismo tamano, misma marca de
fecha, solo `git mv`). Los tres estan ahora dentro de la misma bandeja, y por eso el vecindario que
mide cada informe de abajo va a ser el mismo para los tres: poblacion `440` (`346` del grafo mas
`94` que esperan en bandejas: `91` de grove, `3` de `marquet_turn_the_ship`).

**CERO INSERCIONES en esta tarea.** `MODO_INSERCION=cuarentena` y `D.39` mientras el lote `7` siga
abierto. **No se escribe ningun veredicto en `bitacora/VEREDICTOS.jsonl`**: `BLOQUEARIA` es cola de
lectura, no rechazo, y esa cola se resuelve el dia de la insercion.

**LO YA ADJUDICADO Y NO SE DERIVA** (`ACTA 59` `59.10.a`): el par
`priorizar_lista_entrenamiento_subordinados` contra `desarrollar_primer_curso_entrenamiento`, el
unico vecino por encima de `0,4` que el auditor midio, queda `CONTINUA` (no `REPITE`), leido por los
pasos: la madre produce una lista priorizada de en que entrenar, el hijo produce un curso dictado, y
lo que queda fuera del solape es procedimiento propio en los dos lados. Se cita, no se reabre.

### 61.2.a. INFORME DEL CANDIDATO 1, `priorizar_lista_entrenamiento_subordinados`

    $ date
    2026-09-21 04:51:07 inicio
    $ python forja.py informe cuarentena/grove_high_output/priorizar_lista_entrenamiento_subordinados.json > .v61ext/informe_1_priorizar.txt 2>&1
    $ date
    2026-09-21 04:59:34 fin   (507 s, poblacion 440)

    ============================================================================
    INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
    ============================================================================
    candidatos revisados        : 1
    poblacion del barrido       : 440   (346 del grafo mas 94 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

    EL SALDO
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0

    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 5
      por candidato bloqueado          : menor 5, mediana 5, mayor 5
      que señal levanta cada vecindad  : similitud_texto 5

    [BLOQUEARIA] priorizar_lista_entrenamiento_subordinados
        vecino pedir_critica_anonima_curso_entrenamiento_dictado  [levantada por: similitud_texto]
          similitud_texto 0.497 | familia_id 0.111 | paso_contra_nodo 0.460
        vecino desarrollar_primer_curso_entrenamiento  [levantada por: similitud_texto]
          similitud_texto 0.411 | familia_id 0.143 | paso_contra_nodo 0.401
        vecino responder_primer_aviso_renuncia_subordinado  [levantada por: similitud_texto]
          similitud_texto 0.351 | familia_id 0.125 | paso_contra_nodo 0.403
        vecino gestionar_retencion_subordinado_valioso_renuncia  [levantada por: similitud_texto]
          similitud_texto 0.355 | familia_id 0.125 | paso_contra_nodo 0.394
        vecino reciclar_empleado_ascendido_mas_alla_capacidad  [levantada por: similitud_texto]
          similitud_texto 0.355 | familia_id 0.000 | paso_contra_nodo 0.384

    NADA SE INSERTO. Este informe es de SOLO LECTURA.

**SALIDA GUARDADA EN `.v61ext/informe_1_priorizar.txt`** (42 lineas), a diferencia del intento mudo
de la `60` (`d089`). **UN VECINO NUEVO SOBRE `0,4` QUE NI LA `60` NI LA `ACTA 59` VIERON**:
`pedir_critica_anonima_curso_entrenamiento_dictado` a `0,497`, y aparece solo ahora porque es la
primera corrida con los tres candidatos dentro de la misma bandeja a la vez (`d077`, `ACTA 56`,
`ACTA 59`: el orden de escribir y el de medir cambian la vecindad).

**DISCUTIBLE, MARCADO ANTES DE SABER SI ACIERTO** (`EXTRACTOR.md` 8): lei los pasos de los dos.
`priorizar` entrega una lista priorizada de temas (`L49 a L51`); `pedir_critica` entrega una critica
anonima recogida tras dictar el curso (`L61`), que en el propio libro ocurre DESPUES de
`desarrollar_primer_curso_entrenamiento` (`L53 a L59`). Los tres candidatos traen ademas, cada uno
en su propio `resumen_teorico`, el mismo discutible autoescrito: que un lector podria fundir los tres
momentos sucesivos del mismo proceso de entrenar (priorizar que enseñar, desarrollar el curso,
pedir critica tras dictarlo) en un solo nodo. **Mi lectura de hoy es la misma que la del auditor para
el otro par de esta cadena (`59.10.a`): `CONTINUA`, no `REPITE`.** Cada eslabon tiene su propio
entregable (lista priorizada / curso dictado / critica recogida) y su propia condicion de activacion
(antes de desarrollar el curso / una vez elegido el tema / despues de dictarlo), y lo que queda fuera
del solape de vocabulario (*entrenamiento*, *curso*, *subordinados*) es procedimiento propio en los
dos lados: `priorizar` no dicta ni pide critica, `pedir_critica` no prioriza ni desarrolla. **No
escribo veredicto** (`bitacora/VEREDICTOS.jsonl` se toca el dia de la insercion, `D.39`): dejo la
lectura para quien escriba ese veredicto, igual que hizo el auditor con el par anterior.

### 61.2.b. INFORME DEL CANDIDATO 2, `desarrollar_primer_curso_entrenamiento`

    $ date
    2026-09-21 05:00:29 inicio
    $ python forja.py informe cuarentena/grove_high_output/desarrollar_primer_curso_entrenamiento.json > .v61ext/informe_2_desarrollar.txt 2>&1
    $ date
    2026-09-21 05:11:37 fin   (667 s, poblacion 440)

    ============================================================================
    INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
    ============================================================================
    candidatos revisados        : 1
    poblacion del barrido       : 440   (346 del grafo mas 94 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

    EL SALDO
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0

    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 2
      por candidato bloqueado          : menor 2, mediana 2, mayor 2
      que señal levanta cada vecindad  : similitud_texto 2

    [BLOQUEARIA] desarrollar_primer_curso_entrenamiento
        vecino pedir_critica_anonima_curso_entrenamiento_dictado  [levantada por: similitud_texto]
          similitud_texto 0.478 | familia_id 0.250 | paso_contra_nodo 0.451
        vecino priorizar_lista_entrenamiento_subordinados  [levantada por: similitud_texto]
          similitud_texto 0.409 | familia_id 0.143 | paso_contra_nodo 0.394

    NADA SE INSERTO. Este informe es de SOLO LECTURA.

**SALIDA GUARDADA EN `.v61ext/informe_2_desarrollar.txt`** (33 lineas): a diferencia del intento de
la `60`, que dejo el mismo fichero en `0` bytes (`59.10`, `d089`). **UN TERCER VECINO SOBRE `0,4`**:
`desarrollar` contra `pedir_critica_anonima_curso_entrenamiento_dictado` a `0,478`. **Con este
informe quedan cerrados los TRES pares posibles entre los tres candidatos de `cap_17`**, y los tres
salen sobre `0,4`: `priorizar`-`desarrollar` (`0,411`, adjudicado `CONTINUA` por el auditor en
`59.10.a`), `priorizar`-`pedir_critica` (`0,497`, leido arriba en `61.2.a`) y
`desarrollar`-`pedir_critica` (`0,478`, aqui).

**MISMA LECTURA QUE LOS DOS ANTERIORES, POR LA MISMA VARA** (`6.1`): `desarrollar` entrega un curso
dictado con su segunda clase lista y la decision de si hacen falta mas instructores (`L53 a L59`);
`pedir_critica` entrega una critica anonima recogida DESPUES de dictar ese curso (`L61`), y el propio
paso `1` de `pedir_critica` (*despues de dar el curso, pide criticas anonimas*) presupone como hecho
lo que `desarrollar` todavia esta construyendo. **`CONTINUA`, no `REPITE`**: lo que queda fuera del
solape es procedimiento propio en los dos lados (las siete etapas de construccion del curso en uno,
el formulario y el estudio de las respuestas en el otro). **No escribo veredicto**, por la misma
razon de `D.39` citada arriba.

**LOS TRES CANDIDATOS DE `cap_17` FORMAN UNA CADENA DE TRES ESLABONES, NO UN CIRCULO DE GEMELOS**:
priorizar entrenamiento, desarrollar el curso, pedir critica tras dictarlo. El propio libro los narra
en ese orden (`L49` a `L61`), y los tres candidatos lo declaran ellos mismos como discutible en su
`resumen_teorico` desde que se escribieron. **Lo dejo leido y citado para el dia de la insercion; no
lo adjudico yo con veredicto, que no es mi sede hoy.**
