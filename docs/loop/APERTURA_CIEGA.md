# APERTURA CIEGA DEL AUDITOR, VUELTA 32 DEL BUCLE

> Escrita **antes** de que el arnes exponga `docs/loop/REPORTE.md`. **`D.38.3`:
> toda cifra sale de un instrumento corrido en esta fase, con su salida pegada; lo
> que sale de mis ojos va en celda `POR ADJUDICAR` y su numero en linea `LECTURA`.**
>
> **ESCRITA EN MODO AUSTERO (`D.47`), que llego a mitad de esta misma fase** (ver
> `1`). Se recorta el parrafo de acompaniamiento; **quedan intactas la cifra con su
> instrumento, la tabla pegada y la ruta que sostiene.**

---

## 0. LA DECLARACION DE HERENCIA (`D.40`)

    ACTA ANTERIOR LEIDA: f6c76f63bd9b6aeea7b1d5a9d485977d2d61f593
    HEREDADO 1: CUMPLIDO
    HEREDADO 2: CUMPLIDO
    HEREDADO 3: CUMPLIDO
    HEREDADO 4: CUMPLIDO

**La huella no la copio del prompt: la mido, y la remido despues de que HEAD se
moviera bajo mis pies:**

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    f6c76f63bd9b6aeea7b1d5a9d485977d2d61f593

### 0.1. `HEREDADO 1`: **CUMPLIDO**

> *Ninguna celda de mi apertura sellada lleva un numero que salga de una lectura
> mia; si lo produzco yo leyendo, la celda dice `POR ADJUDICAR`.*

Las cifras en celda de las secciones `1`, `3`, `4`, `5` y `6` **llevan su comando
encima**. La unica tabla de cuenta que nace de mis ojos es la de `6.4`, y **sus
celdas dicen `POR ADJUDICAR`**.

### 0.2. `HEREDADO 2`: **CUMPLIDO**

> *La relectura ciega destapa una razon por vez, y despues de escribir mi clase a
> fichero.* Correccion declarada `ACTA 30` `7.3`: **el acta publica la hora del
> fichero de clases, anterior a la primera corrida que IMPRIMA UNA RAZON.**

    $ ls --time-style=full-iso -l .v33aud/mis_clases.txt
    -rw-r--r-- 1 AlexDesk 197609 3975 2026-09-16 20:44:07.726858400 -0400 .v33aud/mis_clases.txt

**Y no lo digo de palabra: lo mido.** `.v33aud/sin_razones.py` saca las razones de
`bitacora/VEREDICTOS.jsonl`, **no las imprime**, y cuenta cuantas salen en la
salida de la corrida que se le pase:

    $ python .v33aud/sin_razones.py python forja.py rancios
    razones distintas en la bitacora (primeros 40 caracteres): 304
    de ellas, IMPRESAS por "python forja.py rancios": 0

    $ python .v33aud/sin_razones.py python .v33aud/cifras.py
    de ellas, IMPRESAS por "python .v33aud/cifras.py": 0

    $ python .v33aud/sin_razones.py git diff --stat 74ddc8c HEAD
    de ellas, IMPRESAS por "git diff --stat 74ddc8c HEAD": 0

| lo medido | cifra |
|---|---:|
| razones distintas en la bitacora | **304** |
| razones impresas por las corridas de esta fase | **0** |

**Mi primer intento de esta guarda era `rancios | grep -c "razon"`, que da 3 y no
0.** Los tres son la palabra suelta: una linea fija del instrumento y dos ids que
llevan dentro `razonamiento`. **Contar la palabra no era contar la cosa**; lo
corrijo aqui en vez de publicar el `0` de la version mala.

**El fichero de clases tiene DOS bloques**: el primero escrito **antes** del
barrido, el segundo **despues del barrido y antes de destapar nada**. No corregi
el primero en su sitio: **corregirlo habria borrado la prueba de que fue ciego.**

### 0.3. `HEREDADO 3`: **CUMPLIDO**

> *Toda cifra que firmo como mia la corro yo en esta vuelta.*

No hay una sola cifra aqui que no venga de un comando mio pegado debajo. **Y lo
declaro con su margen: `REPORTE.md` no esta en el arbol, asi que no habia de donde
copiar.** Un remedio que solo se cumple cuando es imposible incumplirlo no esta
probado, y quien lea esto tiene derecho a saberlo.

### 0.4. `HEREDADO 4`: **CUMPLIDO**

> *Una tabla que publico como de instrumento no lleva una constante tecleada
> dentro.*

    $ for f in .v33aud/*.py; do python .v33aud/ids_tecleados.py "$f"; done
    .v33aud/aristas.py: 0 literal(es) que son un id de la nomina (511 ids en la nomina)
    .v33aud/cifras.py: 0 literal(es) que son un id de la nomina (511 ids en la nomina)
    .v33aud/formula.py: 0 literal(es) que son un id de la nomina (511 ids en la nomina)
    .v33aud/ids_tecleados.py: 0 literal(es) que son un id de la nomina (511 ids en la nomina)
    .v33aud/sin_razones.py: 0 literal(es) que son un id de la nomina (511 ids en la nomina)

    $ grep -c -F -f <(nomina de 511 ids generada de dataset/ y cuarentena/) .v33aud/barrido.sh
    0

**La nomina de 511 ids tampoco la tecleo: sale de `dataset/` y de `cuarentena/`.
La tanda la saca `git diff --name-only` del propio dato.**

---

## 1. EL ARBOL SE MOVIO BAJO MIS PIES A MITAD DE LA FASE, Y ESO MANDA SOBRE TODO LO DEMAS

**No lo buscaba. Lo encontre porque un instrumento dejo de reproducir su propia
salida de veinte minutos antes.**

| momento | `git rev-parse HEAD` |
|---|---|
| al abrir mi fase | `4ca7c58919606f172583cc35d3761a3fa15c757f` |
| a las **20:50** de la misma fase | `afc18f8faee51f847c0423b2989fed8ea998b639` |

    $ git log --oneline -3
    afc18f8 PARALELO: el paso que faltaba, copiar el corpus al arbol del frente
    269c068 D.45 el paralelo extrae y el serial inserta, D.47 modo austero, y el manual del paralelo
    4ca7c58 VUELTA 32 CIERRE: cap_11 CERRADO EN INSERCION 14 de 14 ...

### 1.1. Lo primero que comprobe: si se movio lo que audito

    $ git diff --stat 4ca7c58 afc18f8 -- dataset/ bitacora/ config/ cuarentena/ fuentes/
    (sin salida)

    $ git diff --stat 4ca7c58 afc18f8
     docs/loop/AUDITOR_FORJA.md |  27 +++++++
     docs/loop/EXTRACTOR.md     |  18 +++++
     docs/loop/PARALELO.md      | 195 +++++++++++++++++++++++++++++++++++++++++++++
     scripts/censar_rutas.py    |  27 ++++++-
     scripts/tallar_reporte.py  |  15 ++--
     tests/prueba_arnes.sh      |   1 +
     tests/test_aceptacion.py   |  17 ++++
     7 files changed, 293 insertions(+), 7 deletions(-)

| lo medido | resultado |
|---|---|
| `dataset/`, `bitacora/`, `config/`, `cuarentena/`, `fuentes/` entre los dos hashes | **cero cambios** |
| `docs/loop/ACTA_AUDITOR.md` entre los dos hashes | **cero cambios**, huella intacta |
| lo que si cambia | **doctrina y arnes**: dos protocolos, un manual nuevo, dos guardas y las pruebas |

> **LECTURA:** **todas mis cifras de estado valen**, porque el dato que audito no
> se toco. **Lo que si cambio, y hay que decirlo con las dos medidas delante, es el
> color de dos guardas.**

### 1.2. Las guardas, medidas en los dos hashes

**Corrido por mi a las 20:20, con el arbol en `4ca7c58`:**

    $ python tests/test_aceptacion.py
      total: 200 pruebas, 4 fallos, 0 errores
    FAILED (failures=4, skipped=1)

    $ python scripts/censar_rutas.py
    rutas publicadas y censadas : 114
      pasan                     : 113
      CAEN                      : 1
    CAE  docs\loop\ACTA_AUDITOR.md linea 14622, celda 1
         ruta : docs/loop/ultimo_apertura.json
         esta y esta VACIA, y la celda no lleva la marca 'VACIA A PROPOSITO: <motivo>'
    CENSO EN ROJO: 1 ruta(s) publicadas como sede de una cifra no sostienen nada.

**Corrido por mi a las 20:50, con el arbol en `afc18f8`:**

    $ python tests/test_aceptacion.py
      total: 201 pruebas, 0 fallos, 0 errores

    $ python scripts/censar_rutas.py
    rutas publicadas y censadas : 119
      pasan                     : 119
      CAEN                      : 0
          PATRON                           10
          VACIA A PROPOSITO                3
          con contenido                    101
          vacia por protocolo              5
    CENSO VERDE: las 119 rutas publicadas sostienen lo que dicen sostener.

| guarda | en `4ca7c58`, que es lo que audito | en `afc18f8`, hoy |
|---|---|---|
| `tests/test_aceptacion.py` | **200** pruebas, **4** fallos | **201** pruebas, **0** fallos |
| `scripts/censar_rutas.py` | **ROJO**, 1 de 114 | **VERDE**, 0 de 119 |
| `python forja.py gate` | **VERDE**, 270 nodos | **VERDE**, 270 nodos |
| `python forja.py guiones` | **VERDE** | **VERDE** |

### 1.3. La causa de las cuatro caidas, medida y no supuesta

**En `4ca7c58` la comprobacion de `D.34.2` vivia dentro de `texto_informe`**, que
recibe los dictamenes de quien sea y miraba la ruta REAL del arbol en vez de la
raiz que se le pasa. Por eso tres pruebas que montan su propio taller no podian
pasar mientras durase la fase ciega, y la cuarta cae porque el arbol esta sucio
**con los borrados del propio arnes**:

    $ git show 4ca7c58:scripts/tallar_reporte.py | grep -n "SIN OBJETO"
    427:        return ("TALLADO SIN OBJETO: docs/loop/REPORTE.md no esta en el arbol." ...

    $ grep -n "SIN OBJETO" -B4 scripts/tallar_reporte.py
    533-    # y no en `texto_informe`, porque ese recibe los dictamenes de quien sea (una
    534-    # prueba en su taller, por ejemplo) y no tiene por que mirar el arbol de verdad.
    535-    if not any(os.path.exists(d) for d in DOCUMENTOS):
    536:        print("TALLADO SIN OBJETO: ninguna sede de tablas esta en el arbol.")

| prueba que caia en `4ca7c58` | lo que imprimia al caer |
|---|---|
| `test_caso_positivo_una_ruta_de_CERO_BYTES_es_caida_de_cifra` | `'TALLADO EN ROJO' not found in 'TALLADO SIN OBJETO: ...'` |
| `test_el_estricto_tumba_lo_que_el_hook_deja_pasar` | `'EN ROJO (estricto)' not found in 'TALLADO SIN OBJETO: ...'` |
| `test_el_informe_nombra_la_fila_y_manda_regenerar` | `'TALLADO EN ROJO' not found in 'TALLADO SIN OBJETO: ...'` |
| `test_e_guion_largo_rompe_el_hook` | `AssertionError: 1 != 0 : el repo ha de estar limpio antes de ensuciarlo` |

> **LECTURA, y es el hallazgo que mas me importa de esta fase:** el corte viejo
> **descartaba los dictamenes que se le acababan de entregar** y en su lugar
> imprimia *esto NO es un fallo*, con caidas `RUTA VACIA` dentro. La cosecha `7.C`
> dice que **una guarda publicada como mordiendo que no muerde es cifra publicada
> falsa**; ahi la guarda **no podia morder durante toda la fase ciega**, que es
> cuando mas falta hace.
>
> **Y lo digo entero: `269c068` ya lo arreglo, y lo arreglo mientras yo lo
> diagnosticaba.** El comentario de las lineas `533` y `534` dice exactamente la
> razon que yo habia escrito en mi fichero de clases a ciegas. **Lo mismo con el
> censo: `vacia por protocolo` pasa de `4` a `5` y `ultimo_apertura.json` deja de
> caer.** No lo reclamo como remedio mio; lo publico porque **una guarda que cambia
> de color a mitad de una auditoria hay que publicarla con sus dos medidas**, o la
> siguiente acta no sabra cual leia.

### 1.4. La doctrina que llego a mitad de fase, y que aplico desde ya

| regla nueva | lo que me obliga |
|---|---|
| **`D.47`, MODO AUSTERO** | recorto tinta, no control. **Esta pagina esta reescrita bajo el, y las cifras y las tablas pegadas quedan enteras** |
| **`D.45`, EN PARALELO UNA PREGUNTA DE DOCTRINA ES PARADA** | ninguna sesion toca `src/`, el banco, el arnes ni los protocolos. **Mis dos propuestas de arnes se retiran: ya estan arregladas, y aunque no lo estuvieran no serian mias de encargar** |

---

## 3. EL ESTADO, MEDIDO POR MI

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 270
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python forja.py resolutor
    nodos vivos: 270
    nodos deprecados (archivo): 0
    alias registrados: 0

    $ python .v33aud/cifras.py
    nodos en dataset/nodos.jsonl            : 270
    pasos totales del grafo                 : 2181
      nodos con fuente manual_sistema_conocimiento: 2
      nodos con fuente onu_consumidor          : 6
      nodos con fuente scott_radical_candor    : 67
      nodos con fuente smart_who               : 59
      nodos con fuente zhuo_manager            : 136
    bandeja cuarentena/scott_radical_candor : 75 ficheros, 1016 pasos
    archivados _insertados/scott_radical_candor: 67 ficheros
    TANDA DE LA VUELTA AUDITADA (del dato)  : 3 ficheros
      debatir_decidir_asuntos_cultura_evitar_delegar        6 pasos
      montar_tablero_kanban_medir_actividades              10 pasos
      pasear_organizacion_hallar_problemas_pequenios        9 pasos
    pasos de la tanda                       : 25
    lineas en bitacora/VEREDICTOS.jsonl     : 396

| lo medido | cifra |
|---|---:|
| nodos en el grafo | **270** |
| pasos del grafo | **2.181** |
| nodos con fuente `scott_radical_candor` | **67** |
| archivados en `_insertados/scott_radical_candor` | **67** |
| bandeja del lote 4 | **75** ficheros, **1.016** pasos |
| lineas de bitacora | **396** |
| ficheros de la tanda | **3** |
| pasos de la tanda | **25** |

**Los 67 del grafo y los 67 archivados cuadran por sus dos mitades.**

### 3.1. Lo que la vuelta movio, contra `74ddc8c`

    $ python .v33aud/aristas.py
    nodos antes (74ddc8c): 267   nodos hoy (HEAD): 270
    ids NUEVOS: 3
      + montar_tablero_kanban_medir_actividades
      + pasear_organizacion_hallar_problemas_pequenios
      + debatir_decidir_asuntos_cultura_evitar_delegar
    aristas por SIGUIENTES/PREVIOS antes: (102, 102)   hoy: (105, 105)
    --- nodos preexistentes que CAMBIARON ---
      ~ decidir_quien_comunica_cada_cuanto        (nodos_siguientes: 6 hijos a 9)
      ~ recorrer_rueda_conscientemente_cultura_equipo (nodos_previos y resumen_teorico)

| lo medido | `74ddc8c` | `4ca7c58` |
|---|---:|---:|
| nodos | **267** | **270** |
| aristas por `nodos_siguientes` | **102** | **105** |
| aristas por `nodos_previos` | **102** | **105** |
| lineas de bitacora | **391** | **396** |
| nodos preexistentes modificados | | **2** |

**Las dos columnas de aristas cuadran por los dos extremos en las dos fechas.**

### 3.2. El bloque de vigencia `D.15` sube **4**, y los cuatro son del mismo nodo

    $ FORJA_DATASET=.v33aud/antes/nodos.jsonl FORJA_VEREDICTOS=.v33aud/antes/VEREDICTOS.jsonl python forja.py rancios
    BLOQUE DE VIGENCIA: 34 hallazgo(s) sobre 377 veredicto(s) y 0 cita(s).
      RANCIO 26, SIN HUELLA 8
      lineas declaradas NO CONSUMADAS y por eso no medidas: 14

    $ python forja.py rancios
    BLOQUE DE VIGENCIA: 38 hallazgo(s) sobre 382 veredicto(s) y 0 cita(s).
      RANCIO 30, SIN HUELLA 8
      lineas declaradas NO CONSUMADAS y por eso no medidas: 14

    $ python forja.py rancios | grep -c "recorrer_rueda_conscientemente_cultura_equipo' cambio"
    4

| lo medido | `74ddc8c` | `4ca7c58` |
|---|---:|---:|
| hallazgos de vigencia | **34** | **38** |
| `RANCIO` | **26** | **30** |
| `SIN HUELLA` | **8** | **8** |
| `NO CONSUMADAS`, no medidas | **14** | **14** |
| rancios que nombran `recorrer_rueda_conscientemente_cultura_equipo` | | **4** |

> **LECTURA:** `D.15` dice que esto es **cola de trabajo y no guarda que tumbe el
> cierre**, asi que no es rojo de nadie. **Pero es cola que esta vuelta creo** al
> reescribir el `resumen_teorico` de ese nodo, y un rancio no se cita como vigente.
> **Reparar una fila mala a costa de cuatro rancios es el precio correcto; no
> decirlo no lo seria.**

---

## 4. MI BARRIDO DE VECINOS, SOBRE GRAFO MAS BANDEJAS

**Metodo vigente (`D.38.5`), no el viejo:** se le entrega a la aduana la poblacion
del **grafo menos el propio candidato** (exclusion de la `ACTA 18`) y **ella pone
las bandejas**. La receta antigua las contaria dos veces.

    FORJA_DATASET=.v33aud/pob/<id>.jsonl python forja.py informe .v33aud/cand/<id>.json

    $ python .v33aud/formula.py
      bandeja marquet_turn_the_ship        3
      bandeja scott_radical_candor         75
    poblacion: 270 del grafo mas 78 en bandejas = 348

    $ (del informe de la aduana, las tres corridas)
    poblacion del barrido       : 347   (269 del grafo mas 78 que esperan en bandejas)

| poblacion | mi cuenta | la de la aduana |
|---|---:|---:|
| del grafo | **270** | **269** (270 menos el candidato) |
| en bandejas | **78** | **78** |
| total | **348** | **347** |

**Cuadran al digito y la diferencia es la exclusion, que es doctrina y no errata.**
Es lo que `D.38.5` prometia: hoy son comparables y cuadran.

| candidato | salida de la aduana | vecinos |
|---|---|---:|
| `debatir_decidir_asuntos_cultura_evitar_delegar` | **ENTRARIA** | **0** |
| `montar_tablero_kanban_medir_actividades` | **BLOQUEARIA** | **1** |
| `pasear_organizacion_hallar_problemas_pequenios` | **ENTRARIA** | **0** |

    $ (barrido de montar_tablero_kanban_medir_actividades, literal)
    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 1
      por candidato bloqueado          : menor 1, mediana 1, mayor 1
      que señal levanta cada vecindad  : paso_contra_nodo 1

    [BLOQUEARIA] montar_tablero_kanban_medir_actividades
        vecino repartir_notas_publicar_reparto_esperado  [levantada por: paso_contra_nodo]
          similitud_texto 0.234 | familia_id 0.000 | paso_contra_nodo 0.607
          paso 4 del candidato contra paso 3 de repartir_notas_publicar_reparto_esperado

---

## 5. MIS CLASES, ADJUDICADAS A CIEGAS CON LA VARA

### 5.1. Las tres, y la unica que hubo que leer

| candidato | tramo del libro | **MI CLASE** |
|---|---|---|
| `debatir_decidir_asuntos_cultura_evitar_delegar` | `cap_11.md` `L301` a `L305` | **SANO** |
| `pasear_organizacion_hallar_problemas_pequenios` | `cap_11.md` `L255` a `L267` | **SANO** |
| `montar_tablero_kanban_medir_actividades` | `cap_11.md` `L239` a `L249` | **SANO** |

**`debatir_decidir`:** su inventario es una lista cerrada del libro (la fiesta, el
arbol, el candelabro, el alcohol, la ropa interior, la patada) mas los dos destinos
que el texto nombra. **El unico nodo del capitulo que lo roza es la cabeza
cultural, y su propio tramo excluye expresamente `L301` a `L305`**, que es lo que
lo hace no contiguo.

**`pasear_organizacion`:** lo que podria confundirlo es
`montar_reuniones_solas_mentalidad_frecuencia`. **El propio `L255` los separa**:
escuchar a quien te reporta directamente es una cosa y escuchar hondo siendo jefe
de jefes es otra. **Esa frontera la escribe el libro, no yo.**

### 5.2. El par que la aduana levanto: **MI CLASE ES SANO**

| | |
|---|---|
| **par** | `montar_tablero_kanban_medir_actividades` contra `repartir_notas_publicar_reparto_esperado` |
| **donde vive el vecino** | **en la bandeja**, sin insertar |
| **señal** | `paso_contra_nodo` **0.607**, umbral **0.60** |
| **donde muerde** | **paso 4** del candidato contra **paso 3** del vecino |
| **MI CLASE** | **SANO** |

**Los dos pasos, impresos primero, que es el orden que mi protocolo manda:**

    paso 4 del candidato:
      "Usalo para lo que el texto dice que sirve al momento: ver rapidamente
       quien es el cuello de botella."

    paso 3 del vecino:
      "Cuenta con lo que el texto dice que es lo mas importante en general:
       el proceso de calibracion."

**MI RAZON, LEIDA DE LOS PASOS Y NO DE LA SEÑAL** (`D.19`): lo unico que comparten
es el molde de redaccion `lo que el texto dice que`. Fuera de el no queda un solo
elemento comun: **`cap_11` contra `cap_14`, condiciones distintas, entregables
distintos, inventarios de medios sin interseccion.** No es hijo, no es gemelo, no
es solape.

    $ python .v33aud/formula.py
    pasos en la poblacion                       : 3214
    pasos que llevan la formula "lo que el texto dice que": 66
    nodos que la usan al menos una vez          : 50 de 348

| lo medido | cifra |
|---|---:|
| pasos de la poblacion de 348 | **3.214** |
| pasos con el molde `lo que el texto dice que` | **66** |
| nodos que lo usan al menos una vez | **50** |

> **LECTURA:** la señal mordio **en el molde de redaccion del extractor, no en el
> procedimiento del libro**. Con **66** pasos en **50** nodos usando la misma
> formula, **este falso positivo no sera el ultimo: es el primero que se ve.** No
> lo cargo como caida: `6.4` dice que la señal hizo su trabajo al decir donde
> mirar, y lo hizo.

---

## 6. FIDELIDAD `D.30`, LOS 25 PASOS CONTRA SU LINEA

### 6.1. `montar_tablero_kanban_medir_actividades`, 10 pasos

| paso | linea que lo sostiene | mi clase |
|---:|---|---|
| 1 | `L239` *you put up a board with three columns: To Do, In Progress, and Done* | **TRANSCRIPCION** |
| 2 | `L239` *you buy a bunch of Post-its in different colors. The different colors represent different people or teams* | **TRANSCRIPCION** |
| 3 | `L239` *They write their tasks on their color of Post-it and move them around* | **TRANSCRIPCION** |
| 4 | `L239` *You can quickly see who's the bottleneck* | **TRANSCRIPCION** |
| 5 | `L239` *A Kanban board is different from a dashboard because it focuses activities and work in progress* | **TRANSCRIPCION** |
| 6 | `L241` *Making progress visible to everyone gives more, not less, autonomy* | **TRANSCRIPCION** |
| 7 | `L243` *it's hard to tell from the results who's along for the ride and who's actually making things happen* | **TRANSCRIPCION** |
| 8 | `L245` *will push you and your team to make sure you really understand how what you all do drives success* | **TRANSCRIPCION** |
| 9 | `L247` *Measuring activities will also create more respect between teams* | **TRANSCRIPCION** |
| 10 | `L249` *tends to lead to ratings and promotions that more consistently reward the top performers* | **TRANSCRIPCION** |

**MI DISCUTIBLE, marcado y no cargado:** el `nombre_largo` dice *las **cinco**
cosas*. **El libro no escribe esa cifra**: sale de contar los cinco parrafos
`L241`, `L243`, `L245`, `L247`, `L249`. **El contraste esta en el mismo capitulo:**
el nodo del paseo dice *las tres cosas* y ahi el libro **si** escribe `First`,
`Second`, `Third`. Me quedo en `TRANSCRIPCION` porque `D.30` cuenta **pasos** y esa
cifra vive en el `nombre_largo`, **pero es la misma familia que la correccion de la
vuelta 25 sobre las escaleras de puesto.**

### 6.2. `pasear_organizacion_hallar_problemas_pequenios`, 9 pasos

| paso | linea que lo sostiene | mi clase |
|---:|---|---|
| 1 | `L255` *if you are a manager of managers, listening "deep"* ... *the same three cranks week after week* | **TRANSCRIPCION** |
| 2 | `L259` *Schedule an hour a week of walking-around time* | **TRANSCRIPCION** |
| 3 | `L259` *a tried-and-true technique* ... *It's not complicated to do* | **TRANSCRIPCION** |
| 4 | `L261` *Notice the things you don't notice when you're buried in work at your desk* | **TRANSCRIPCION** |
| 5 | `L261` *Ask people who catch your attention, ideally, people you haven't talked to in a while* | **TRANSCRIPCION** |
| 6 | `L261` *Find some small problems and treat them like "the universe through a grain of sand"* | **TRANSCRIPCION** |
| 7 | `L263` *First they'll help you find the devil in the details* | **TRANSCRIPCION** |
| 8 | `L265` *Second, being aware of small problems and maybe even rolling up your sleeves* | **TRANSCRIPCION** |
| 9 | `L267` *Third, when you show that you care about the small things* | **TRANSCRIPCION** |

**Lo que deja fuera y no es puente:** `L257` (Dick Costolo) y la procedencia de
`L259` (Lincoln, Hewlett Packard). **Omitir no es inventar.**

### 6.3. `debatir_decidir_asuntos_cultura_evitar_delegar`, 6 pasos

| paso | linea que lo sostiene | mi clase |
|---:|---|---|
| 1 | `L303` *debates and decisions that you are going to be tempted to "delegate to HR"* | **TRANSCRIPCION** |
| 2 | `L303` *"holiday party"* ... *Christmas tree* ... *A menorah* ... *alcohol* ... *bras and panties* ... *kicked another in the butt* | **TRANSCRIPCION** |
| 3 | `L303` *Who's going to decide how to deal with it?* | **TRANSCRIPCION** |
| 4 | `L305` *without your humanizing influence will push your culture in a "the law is an ass" direction* | **TRANSCRIPCION** |
| 5 | `L305` *If nobody makes a decision, you wind up in Lord of the Flies territory* | **TRANSCRIPCION** |
| 6 | `L305` *Neither is the culture you want* | **TRANSCRIPCION** |

**Compresion que miro y dejo pasar:** el paso 2 dice *ropa interior* donde el libro
escribe *bras and panties and a jock strap*. **Comprimir tres prendas en una
categoria no aniade procedimiento.**

### 6.4. La cuenta, en `POR ADJUDICAR` porque es lectura mia

| capitulo | pasos del tramo | `TRANSCRIPCION` | `PUENTE` | `PASOS INVENTADOS` |
|---|---:|---:|---:|---:|
| `cap_11`, tramo de esta vuelta | **25** (instrumento, `3`) | `POR ADJUDICAR` | `POR ADJUDICAR` | `POR ADJUDICAR` |

> **LECTURA:** de los **25** pasos, **los 25 me salen `TRANSCRIPCION` y ninguno
> `PUENTE`**, asi que **`PASOS INVENTADOS` del tramo me da `0,00 por ciento`.** La
> cifra **25** es de instrumento; **el reparto entre las dos clases es mio, y por
> eso su celda dice `POR ADJUDICAR` hasta que la firme en el acta.**
>
> **Y digo lo que no es:** `8.4` dice que esta metrica **no es de castigo y no entra
> en la metrica de credito**. Un `0,00` no absuelve a nadie: dice que **en 25 pasos
> el libro tenia inventario propio.**

---

## 7. EL REMEDIO QUE YO MISMO ENCARGUE, MEDIDO ANTES DE VER EL REPORTE

**La `ACTA 30` encargo como tarea bloqueante que el mapeo de rotulo a nodo de la
cabeza de `cap_11` saliera del dato**, porque su fila 10 ponia un id por otro y
**lo tecleado estaba dentro del instrumento, en su constante.**

    $ python .v33aud/ids_tecleados.py .v31/cabeza.py
    .v31/cabeza.py: 10 literal(es) que son un id de la nomina (511 ids en la nomina)
      L12   decidir_quien_comunica_cada_cuanto
      L17   montar_reuniones_solas_mentalidad_frecuencia
      L18   conducir_reunion_equipo_agenda_tres_bloques
      L19   bloquear_tiempo_pensar_calendario
      L20   montar_reunion_gran_debate
      L21   montar_reunion_gran_decision
      L22   montar_reunion_general_presentaciones_preguntas
      L24   montar_tablero_kanban_medir_actividades
      L25   pasear_organizacion_hallar_problemas_pequenios
      L26   debatir_decidir_asuntos_cultura_evitar_delegar

    $ python .v33aud/ids_tecleados.py .v32/cabeza.py
    .v32/cabeza.py: 1 literal(es) que son un id de la nomina (511 ids en la nomina)
      L30   decidir_quien_comunica_cada_cuanto

| lo medido | `.v31/cabeza.py` (vieja) | `.v32/cabeza.py` (el remedio) |
|---|---:|---:|
| ids de la nomina tecleados dentro | **10** | **1** |
| de ellos, celdas del mapeo | **9** | **0** |
| de ellos, el sujeto del instrumento | **1** | **1** |

> **LECTURA: el remedio esta entregado en sustancia.** Las nueve celdas del mapeo,
> que son las que podian romperse y la que se rompio, **ya no estan tecleadas**. Y
> la fila mala aparece en la medida: **`L26` del fichero viejo es literalmente
> `debatir_decidir_asuntos_cultura_evitar_delegar`**, el id equivocado que cace.
> **La medida confirma mi diagnostico sin que yo tenga que citarme.**

**MI DISCUTIBLE, marcado ahora para no poder ajustarlo despues:** el instrumento
nuevo publica en su aviso *cero nodos tecleados en este instrumento* y yo **mido
1**. Ese 1 es la **cabeza**, el sujeto del instrumento y no una celda de su tabla.
**Me inclino a que la frase sobra y la sustancia esta bien**, y lo dejo escrito
antes de abrir el reporte.

---

## 8. LO QUE ESPERO ENCONTRAR, ESCRITO ANTES DE ABRIRLO

| # | lo que espero | contra que lo comparo |
|---:|---|---|
| **1** | insercion de **3** candidatos, `cap_11` cerrado **14 de 14** | `3` de la tanda, `67` archivados |
| **2** | **105** aristas por los dos extremos y **396** lineas de bitacora | `3.1` |
| **3** | que el par del kanban **tenga su razon escrita**, porque `D.8` dice que un `SANO` sin razon es caida aunque acierte | una razon por vez, en mi turno |
| **4** | que declare los **4** rancios que su propia correccion creo | `3.2` |
| **5** | que su `PASOS INVENTADOS` de `cap_11` coincida con mi `0,00` sobre **25** pasos | `6.4` |

**Las tres formas en que esto puede salir, y digo las tres:** que coincidamos y la
tanda salga limpia; que el reporte traiga cifras que yo no medi, **y entonces las
corro yo** (`HEREDADO 3`); o que discrepemos en el par del kanban o en la cuenta de
puentes, **y entonces gana quien leyo los pasos y publico frontera** (`P.17`), no
quien argumento por señal (`D.19`).

### 8.1. Propuestas

| # | propuesta | de donde sale | estado |
|---:|---|---|---|
| **1** | el molde `lo que el texto dice que`, en **66** pasos de **50** nodos, como fuente de falsos positivos de `paso_contra_nodo` | `5.2` | **viva** |
| ~~2~~ | ~~que `texto_informe` respete la raiz que se le pasa~~ | `1.3` | **RETIRADA: `269c068` ya la arreglo, y `D.45` me prohibe tocar el arnes** |
| ~~3~~ | ~~que `censar_rutas.py` sepa de la fase ciega~~ | `1.2` | **RETIRADA por lo mismo: `vacia por protocolo` paso de 4 a 5** |

---

## 9. CIERRE

| | |
|---|---:|
| candidatos clasificados por mi a ciegas | **3** |
| de ellos, `SANO` | **3** |
| pares levantados por la aduana y adjudicados por mi | **1** |
| pasos releidos contra el libro, uno a uno | **25** |
| discutibles mios marcados antes de abrir el reporte | **3** |
| propuestas vivas | **1** |
| guardas en rojo **por causa del extractor**, en los dos hashes | **0** |
| hashes distintos que ha tenido el arbol durante mi fase | **2** |

**Nada de esta pagina se ha escrito con el reporte delante.**

**ACTA ANTERIOR LEIDA: `f6c76f63bd9b6aeea7b1d5a9d485977d2d61f593`. HEREDADO 1:
CUMPLIDO. HEREDADO 2: CUMPLIDO. HEREDADO 3: CUMPLIDO. HEREDADO 4: CUMPLIDO.**
