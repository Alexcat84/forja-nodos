# APERTURA CIEGA DE LA VUELTA 31, escrita por el auditor ANTES de ver el reporte

*Fase ciega de `D.34.2`. Los cuatro ficheros que el arnes retira (`REPORTE.md`, `loop.log`,
`ultimo_extractor.json`, `ultimo_auditor.json`) NO se han abierto ni se han recuperado de git en esta
fase. Lo que si he abierto, y lo digo porque es obra mia y no del extractor: `docs/loop/ACTA_AUDITOR.md`
y `docs/loop/PROMPT_SIGUIENTE.md`, que son sede del auditor por `AUDITOR_FORJA.md` 5.6.*

---

## 0. LA DECLARACION QUE EL ARNES EXIGE (`D.40`)

    ACTA ANTERIOR LEIDA: 5ddb0d9f61253f785e3878cee54a9b17173d8731
    HEREDADO 1: CUMPLIDO
    HEREDADO 2: CUMPLIDO
    HEREDADO 3: CUMPLIDO

**La huella no la copio del prompt: la recomputo aqui, en esta fase**, que es lo que `src/herencia.py`
dice que se comprueba (*"El `<hash>` es el de `git hash-object` sobre el acta: no vale decir que se
leyo"*, linea 64 de ese fichero).

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    5ddb0d9f61253f785e3878cee54a9b17173d8731

    $ python forja.py herencia
      acta anterior : ACTA 29. VUELTA 30, lote 4 (`scott_radical_candor`), `cap_07` CERRADO ...
      su huella     : 5ddb0d9f61253f785e3878cee54a9b17173d8731
      heredados     : 3

**Y de paso queda comprobada la `TAREA 2` BLOQUEANTE que yo mismo encargue**: el instrumento devuelve
hoy **los tres remedios de la tabla `8.5` de la `ACTA 29`**, no secciones que solo mencionan la
palabra. Era la mitad del encargo y la mitad se sostiene. **Lo que NO firmo todavia es el caso
positivo contra las `ACTAS 27` y `28`**, que me lo llevo al turno normal.

### 0.1. `HEREDADO 1`: ninguna celda de mi apertura lleva un numero que salga de una lectura mia

**CUMPLIDO, y se ve en la seccion 2 y en la seccion 3.** Cada celda con cifra de esta apertura lleva
debajo el comando que la produjo, con su salida literal. **Las cifras que salen de mi lectura y no de
un instrumento tienen su celda en `POR ADJUDICAR`** y el numero va en la frase, marcado `LECTURA`.
Son tres y las nombro aqui para que se puedan contar: los puentes de `D.30` del tramo (seccion 3.5),
los rotulos cableables hoy (seccion 4.1) y la clase de cada par de la seccion 3.

### 0.2. `HEREDADO 2`: mi clase se escribe a fichero ANTES de tocar la bitacora

**CUMPLIDO EN LO QUE ORDENA, Y CON UNA PRECISION QUE DECLARO YO PORQUE ME PERJUDICA.**

    $ stat -c '%n  %y' .v31c/mis_clases_pineada.txt
    .v31c/mis_clases_pineada.txt  2026-09-16 18:50:31.445313400 -0400

    $ wc -l .v31c/mis_clases_pineada.txt
    127 .v31c/mis_clases_pineada.txt

**LA PRECISION:** el remedio dice *"que sea anterior a la primera consulta de la bitacora"*, y a las
`18:42` yo ya habia corrido `python forja.py rancios`, que es la guarda de `D.15` y **abre
`bitacora/VEREDICTOS.jsonl`**. Asi que la comprobacion mecanica, leida al pie de la letra, no cuadra,
y lo digo antes de que lo diga nadie. **Lo que el remedio ORDENA si se cumplio, y lo mido en vez de
afirmarlo: esa corrida no destapo ni una sola razon.**

    $ python forja.py rancios > .v31c/rancios.txt ; python - (cuenta cuantas de las 391 razones
      de la bitacora asoman en esa salida)
    lineas de bitacora con campo razon           : 391
    razones que asoman en la salida de rancios   : 0
    lineas de la salida de rancios               : 42

**Ninguna razon de la bitacora estaba delante de mis ojos cuando escribi mis clases.** Las clases de
la seccion 3 de esta apertura son las del fichero de las `18:50:31`, sin una coma cambiada, salvo un
`POR ADJUDICAR` que cierro en la seccion 3.4 y que digo que cierro.

### 0.3. `HEREDADO 3`: toda regla que cito la leo en su sede en esta misma fase

**CUMPLIDO.** Las reglas que cito en esta apertura, con la sede que abri hoy y la linea donde vive:

| regla | sede leida en esta fase | linea |
|---|---|---:|
| `D.27`, la prueba del inventario | `docs/BANCO_DE_REGLAS.md` | `674` |
| `D.29`, la arista que la senial no levanta | `docs/BANCO_DE_REGLAS.md` | `780` |
| `D.30`, la fidelidad la caza otro lector | `docs/BANCO_DE_REGLAS.md` | `830` |
| `D.34.2`, la apertura ciega en codigo | `docs/BANCO_DE_REGLAS.md` | `1135` |
| `D.37`, la serie que dice cuantas partes tiene | `docs/BANCO_DE_REGLAS.md` | `1241` |
| `D.38.3`, `D.38.4` y `D.38.5` | `docs/loop/AUDITOR_FORJA.md` seccion 1 punto 5 | `160` a `190` |
| la vara, `NOMBRAR NO ES PROCEDIMENTAR` | `docs/loop/AUDITOR_FORJA.md` seccion 6.1 | `538` |
| cosecha `7.B` y `7.C` | `docs/loop/AUDITOR_FORJA.md` seccion 5.5 | `447` a `457` |

Y pego las dos que mas trabajo hacen aqui, porque en ellas se apoya toda la seccion 4:

> **`D.37`** (`BANCO_DE_REGLAS.md` linea `1259`): *"dice cuantas partes hay y las nombra -> `D.37`,
> arista por lectura, citando el paso. Solo enumera sin decir cuantas -> `D.29`, con razon escrita:
> es una lectura que hay que argumentar, no una transcripcion."*

> **La vara, 6.1:** *"NOMBRAR NO ES PROCEDIMENTAR: una segunda linea solo cuenta como expansion si
> trae procedimiento propio, no solo el nombre de otro."*

---

## 1. QUE VUELTA AUDITO, Y SI HAY HUECO DE ACTA

**NO HAY HUECO.** La ultima acta cubre la vuelta `30` y el arbol trae seis commits de la vuelta `31`.

    $ grep -o "^# ACTA [0-9]*\. VUELTA [0-9]*" docs/loop/ACTA_AUDITOR.md | tail -4
    # ACTA 26. VUELTA 26
    # ACTA 27. VUELTA 27
    # ACTA 28. VUELTA 28
    # ACTA 29. VUELTA 30

    $ git log --oneline | grep -c "VUELTA 31"
    6

    $ git rev-parse HEAD
    74ddc8cb114f5c25716ec1595fbafb5baebfc737

**LO QUE LA VUELTA MOVIO, contado contra el commit con que abrio** (`9d10f80`, *ARNES: estado del
bucle al abrir la vuelta 31*), **por diferencia de ids y no por su palabra**:

    $ git show 9d10f80:dataset/nodos.jsonl | (ids) | sort > .v31c/ids_antes.txt
    $ (ids de dataset/nodos.jsonl hoy) | sort > .v31c/ids_ahora.txt
    $ wc -l .v31c/ids_antes.txt .v31c/ids_ahora.txt
      256 .v31c/ids_antes.txt
      267 .v31c/ids_ahora.txt

    $ comm -13 .v31c/ids_antes.txt .v31c/ids_ahora.txt      (los que entraron)
    conducir_reunion_equipo_agenda_tres_bloques
    decidir_quien_comunica_cada_cuanto
    escribir_apuntes_sala_estudio_equipo
    leer_seniales_fallo_jefe_reunion_solas
    montar_reunion_general_presentaciones_preguntas
    montar_reunion_gran_debate
    montar_reunion_gran_decision
    montar_reuniones_solas_mentalidad_frecuencia
    nutrir_ideas_nuevas_reunion_solas
    pelear_proliferacion_reuniones_bloquear_ejecucion
    preguntar_seguimiento_hallar_huecos

    $ comm -23 .v31c/ids_antes.txt .v31c/ids_ahora.txt      (los que desaparecieron)
    (vacio)

**ONCE entraron y CERO se perdieron.** El tramo es `cap_11` del lote 4 (`scott_radical_candor`).

---

## 2. EL ESTADO, MEDIDO CON INSTRUMENTO EN ESTA MISMA FASE (`D.38.3`)

**Ninguna cifra de esta tabla es un recuerdo ni una copia del encargo. Todas salen de un comando
corrido hoy, y el comando esta debajo.**

| | cifra | instrumento |
|---|---:|---|
| nodos en `dataset/nodos.jsonl` | **267** | `wc -l` |
| veredictos en `bitacora/VEREDICTOS.jsonl` | **391** | `wc -l` |
| aristas por `nodos_siguientes` | **102** | contador propio |
| aristas por `nodos_previos` | **102** | contador propio |
| candidatos en bandeja, lote 4 | **78** | `ls | wc -l` |
| candidatos en bandeja, lote 5 | **3** | `ls | wc -l` |
| archivados en `_insertados`, lote 4 | **64** | `ls | wc -l` |
| poblacion del barrido de vecinos | **348** | la aduana en seco |
| pruebas de aceptacion | **200**, con **4 fallos** | `tests/test_aceptacion.py` |
| gate | **VERDE** | `forja.py gate` |
| barrido de guiones | **VERDE** | `forja.py guiones` |
| censo de rutas | **ROJO, 1 hallazgo** | `scripts/censar_rutas.py` |
| cola de vigencia `D.15` | **8 lineas SIN HUELLA** | `forja.py rancios` |
| puentes `D.30` del tramo de once | **POR ADJUDICAR** | seccion 3.5, `LECTURA` |
| rotulos de la cabeza cableables hoy | **POR ADJUDICAR** | seccion 4.1, `LECTURA` |

Las salidas, en el orden de la tabla:

    $ wc -l dataset/nodos.jsonl
    267 dataset/nodos.jsonl

    $ wc -l bitacora/VEREDICTOS.jsonl
    391 bitacora/VEREDICTOS.jsonl

    $ python - (contador de aristas por los dos extremos)
    aristas contadas por nodos_siguientes : 102
    aristas contadas por nodos_previos    : 102
    pares distintos por union             : 102

    $ for d in cuarentena/*/; do ls $d*.json | wc -l; done
      cuarentena/ensayo_referencia_163/ 163
      cuarentena/marquet_turn_the_ship/ 3
      cuarentena/scott_radical_candor/ 78
      cuarentena/_insertados/scott_radical_candor/ 64

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 267
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta,
      cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones,
      censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python forja.py resolutor
    nodos vivos: 267
    nodos deprecados (archivo): 0
    alias registrados: 0

**LAS DOS COSAS QUE NO ESTAN EN VERDE AHORA MISMO, Y LAS DOS SON DE LA FASE CIEGA. Las publico enteras
porque mi predecesor cayo justo aqui: publico `guardas en rojo: 2` cuando eran `3`.**

**(a) EL CENSO DE RUTAS ESTA EN ROJO, CON UN HALLAZGO, Y LA CELDA ES MIA.**

    $ python scripts/censar_rutas.py
    CAE  docs\loop\ACTA_AUDITOR.md linea 14622, celda 1
         ruta : docs/loop/ultimo_apertura.json
         esta y esta VACIA, y la celda no lleva la marca 'VACIA A PROPOSITO: <motivo>'
    CENSO EN ROJO: 1 ruta(s) publicadas como sede de una cifra no sostienen nada.

    $ ls -l docs/loop/ultimo_apertura.json
    -rw-r--r-- 1 AlexDesk 197609 0 Sep 16 18:39 docs/loop/ultimo_apertura.json

    $ git show HEAD:docs/loop/ultimo_apertura.json | wc -c
    4479

**Y LO VUELVO A CORRER CON ESTA APERTURA YA ESCRITA, porque las rutas que yo publico aqui son cifra
mia** (cosecha `7.B`):

    $ python scripts/censar_rutas.py          (con docs/loop/APERTURA_CIEGA.md en el arbol)
    rutas publicadas y censadas : 118
      pasan                     : 117
      CAEN                      : 1

**Mi apertura anade `21` rutas al censo y las `21` resuelven. El unico hallazgo sigue siendo el de la
linea `14622` del acta.**

**LA LEO ASI, y es lectura mia:** la ruta la publica **mi propia acta**, el fichero **existe en
`HEAD` con `4479` bytes**, y esta vacio **porque el arnes lo vacio a las `18:39` para abrir mi fase
ciega**. No es una ruta que dejo de resolver: es la ruta que esta fase deja en cero por construccion.
**No la cargo contra nadie y no la arreglo desde aqui**, porque tocar el acta en la fase ciega no es
mio. **Me la llevo al turno normal con su cifra.**

**(b) LAS PRUEBAS DE ACEPTACION DAN `4` FALLOS, Y LOS CUATRO TIENEN LA MISMA CAUSA.**

    $ python tests/test_aceptacion.py ; echo exit=$?
      total: 200 pruebas, 4 fallos, 0 errores
    FAILED (failures=4, skipped=1)
    exit=1

    FAIL: test_caso_positivo_una_ruta_de_CERO_BYTES_es_caida_de_cifra
    FAIL: test_el_estricto_tumba_lo_que_el_hook_deja_pasar
    FAIL: test_el_informe_nombra_la_fila_y_manda_regenerar
      AssertionError: 'TALLADO EN ROJO' not found in 'TALLADO SIN OBJETO: docs/loop/REPORTE.md no
      esta en el arbol. La fase ciega lo retira A PROPOSITO (D.34.2), asi que no hay ninguna tabla
      que tallar y esto NO es un fallo.'

    FAIL: test_e_guion_largo_rompe_el_hook
      AssertionError: 1 != 0 : el repo ha de estar limpio antes de ensuciarlo

**LO QUE MIDO:** las tres primeras montan su propio fixture y esperan `TALLADO EN ROJO`; el tallado
**corta antes, mirando el `REPORTE.md` de verdad**, que esta fase retira. La cuarta pide el repo
limpio, y esta fase lo ensucia borrando cuatro ficheros versionados.

**`LECTURA`:** las tres primeras son **los casos positivos** que prueban que la guarda del tallado
muerde, que es lo que la cosecha `7.C` exige (*una guarda publicada como mordiendo que no muerde es
cifra publicada falsa*). **Durante la fase ciega esa guarda no se puede demostrar mordiendo.** Esto
**no es una caida del extractor**: su vuelta corrio con los cuatro ficheros en el arbol. **Es del
arnes, y es mio llevarlo.** No lo arreglo aqui: la moratoria de maquinaria (`5.6`) pide una caida de
dato con su cita, y esta no mueve ni un dato.

**EL BARRIDO DE VECINOS SE HACE SOBRE GRAFO MAS BANDEJAS** (`D.38.4`), y lo hace la aduana, que desde
`D.38.5` mide la misma poblacion que yo:

    $ python forja.py informe cuarentena/scott_radical_candor/<candidato>.json
    poblacion del barrido       : 348   (267 del grafo mas 81 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

**`267` mas `81` son `348`, y `81` son `78` del lote 4 mas `3` del lote 5. Me cuadra al digito con mi
propio conteo de bandejas, asi que no hay discrepancia de poblacion que declarar.**

---

## 3. MI LECTURA A CIEGAS DE `cap_11`, CANDIDATO POR CANDIDATO

**Lo que lei:** las `333` lineas de `fuentes/scott_radical_candor/cap_11.md`, los `17` ficheros de
candidato que declaran `cap_11` como unidad de origen, y los nodos del grafo que les hacen de vecino.

    $ wc -l fuentes/scott_radical_candor/cap_11.md
    333 fuentes/scott_radical_candor/cap_11.md

    $ (inventario propio: ficheros de cuarentena cuyo resumen declara cap_11)
    TOTAL ficheros cap_11: 17      (13 en _insertados, 4 en bandeja)

**De los `4` de bandeja, uno NO es de `cap_11`**: `integrar_peticion_critica_rutina_existente` declara
`cap_13` y solo nombra `cap_11` dentro de una comparacion. **Lo comprobe antes de contarlo**, y por eso
digo `3` y no `4`.

    $ grep -o ".\{120\}cap_11.\{120\}" cuarentena/scott_radical_candor/integrar_peticion_critica_rutina_existente.json
    ... SU PAR CON montar_reuniones_solas_mentalidad_frecuencia (cap_11) ES SANO ...

### 3.1. El mapa de la frontera que yo leo, rotulo por rotulo

    $ awk 'NR>=17 && NR<=35 && NF' fuentes/scott_radical_candor/cap_11.md
    L17  1:1 Conversations
    L19  Staff Meetings
    L21  Think Time
    L23  "Big Debate" Meetings
    L25  "Big Decision" Meetings
    L27  All-Hands Meetings
    L29  Meeting-Free Zones
    L31  Kanban Boards
    L33  Walk Around
    L35  Be Conscious of Culture

| rotulo del indice | cuerpo que le corresponde | nodo | donde vive |
|---|---|---|---|
| 1:1 Conversations | `L37` a `L127` | cuatro nodos, seccion 3.2 | grafo |
| Staff Meetings | `L129` a `L163` | dos nodos, seccion 3.3 | grafo |
| Think Time | `L165` a `L173` | `bloquear_tiempo_pensar_calendario` | grafo, vuelta 30 |
| "Big Debate" | `L175` a `L193` | `montar_reunion_gran_debate` | grafo |
| "Big Decision" | `L195` a `L203` | `montar_reunion_gran_decision` | grafo |
| All-Hands | `L205` a `L221` | `montar_reunion_general_presentaciones_preguntas` | grafo |
| Meeting-Free Zones | **NO TIENE CUERPO** | ninguno | ninguno |
| Kanban Boards | `L235` a `L249` | `montar_tablero_kanban_medir_actividades` | bandeja |
| Walk Around | `L251` a `L269` | `pasear_organizacion_hallar_problemas_pequenios` | bandeja |
| Be Conscious of Culture | `L271` a `L299` y `L307` a `L333` | `recorrer_rueda_conscientemente_cultura_equipo` | **grafo** |

**QUE EL ROTULO `Meeting-Free Zones` NO TIENE CUERPO LO MIDO, NO LO SUPONGO:**

    $ grep -n -i "meeting-free\|execution time" fuentes/scott_radical_candor/cap_11.md
    29:Meeting-Free Zones
    223:EXECUTION TIME

**Aparece UNA vez en las 333 lineas, y es la linea del indice.** El hueco que deja lo ocupa
`EXECUTION TIME` (`L223` a `L233`), que es de donde sale
`pelear_proliferacion_reuniones_bloquear_ejecucion`. **El indice promete diez secciones y el capitulo
escribe nueve mas una con otro nombre.**

### 3.2. Los cuatro nodos de las reuniones a solas, y el corte que sostengo con otra razon

**MI CLASE, la misma del fichero de las `18:50:31`:**

| par | mi clase a ciegas |
|---|---|
| `montar_reuniones_solas_mentalidad_frecuencia` contra `dirigir_reunion_individual_semanal` (zhuo) | **NO ES DUPLICADO** |
| `montar_reuniones_solas_mentalidad_frecuencia` contra `preguntar_conducir_reunion_individual` (zhuo) | **NO ES DUPLICADO** |
| `preguntar_seguimiento_hallar_huecos` contra `preguntar_conducir_reunion_individual` (zhuo) | **NO ES DUPLICADO** |
| `nutrir_ideas_nuevas_reunion_solas` contra `crear_espacio_seguro_madurar_ideas_nuevas` | **CONTINUA** |
| `leer_seniales_fallo_jefe_reunion_solas` | **PROCEDIMIENTO, no advertencia** |

**Y LA RAZON, con la vara 6.1 delante** (*no tiene bascula: decide si lo que queda fuera es
procedimiento en los dos lados*): en el primer par, fuera del solape, aquel pone las cuatro ideas de
preparacion y el criterio de si la reunion sirvio, y este pone **la aritmetica de capacidad del jefe**
que decide cuantas personas puede tener a cargo, la cuenta de cancelaciones y el protocolo de agenda.
**Procedimiento en los dos lados, asi que no es duplicado.**

**LO QUE SI LEVANTO, Y ES CONTRA EL CORTE Y NO CONTRA EL NODO.** El resumen de
`montar_reuniones_solas_mentalidad_frecuencia` funde cuatro rotulos interiores y escribe su razon asi:
*"la linea 45 los encadena ella misma con una sola frase"*. **Corri la linea 45 y sus rotulos, y esa
razon prueba de mas:**

    $ sed -n '45p' fuentes/scott_radical_candor/cap_11.md
    Here are a few things you can do to make sure you and each of your reports are getting the most
    out of these 1:1 meetings:

    $ awk 'NR>=45 && NR<=128 && NF && length($0)<80' fuentes/scott_radical_candor/cap_11.md
    L47  Mind-set
    L51  Frequency
    L59  Show up!
    L63  Your direct report's agenda, not yours
    L67  Some good follow-up questions
    L99  Encourage new ideas in the 1:1.
    L115 Signs you'll get from 1:1s that you're failing as a boss
    (mas las preguntas sueltas de L71 a L95 y L107, que son cuerpo y no rotulo)

**`LECTURA`: la linea 45 encadena SIETE rotulos, no cuatro.** Los tres ultimos salieron en nodo propio
(`preguntar_seguimiento_hallar_huecos`, `nutrir_ideas_nuevas_reunion_solas`,
`leer_seniales_fallo_jefe_reunion_solas`). **El corte lo sostengo igual, pero por otra razon**: los
cuatro primeros comparten una condicion de activacion y un entregable (montar la reunion), y los tres
ultimos tienen los suyos propios. **La cadena de la linea 45 no separa nada: aplicada como esta
escrita, mandaria fundir los siete en uno.** No es caida de clase, porque ningun veredicto queda mal
puesto; **es una razon mas ancha que su conclusion, y de esas ya se cayo una regla en esta casa**
(`D.37`, cuyo titular era mas ancho que su cuerpo).

### 3.3. La reunion de equipo y los apuntes de sala de estudio

| par | mi clase a ciegas |
|---|---|
| `conducir_reunion_equipo_agenda_tres_bloques` contra `dirigir_reunion_revision_trabajo` y `dirigir_reunion_informativa` (zhuo) | **NO ES DUPLICADO** |
| `escribir_apuntes_sala_estudio_equipo` como nodo propio y no paso del anterior | **NODO PROPIO** |

Aquellas son reuniones por proposito; esta es la reunion de equipo con su agenda de tres bloques y sus
tiempos escritos. Y los apuntes traen protocolo entero propio (cinco a siete minutos para escribir
tres a cinco cosas, cinco a siete para leer, prohibicion de conversaciones laterales, documento
compartido, publicos si eres jefe de jefes, documento confidencial acotado). **La arista
`conducir_reunion_equipo` a `escribir_apuntes` la sostengo: el bloque `Listen` de la agenda la nombra.**

### 3.4. Los tres que siguen en bandeja, y la aduana en seco sobre los tres

**Aqui cierro el unico `POR ADJUDICAR` que mi fichero de clases dejo abierto**
(`pasear_organizacion_hallar_problemas_pequenios`, que a las `18:50` no habia leido entero). **Lo digo
para que se vea que se cerro despues y no antes.**

| candidato | mi clase a ciegas | que dice la aduana en seco |
|---|---|---|
| `montar_tablero_kanban_medir_actividades` | **PROCEDIMIENTO** | `BLOQUEARIA`, `1` vecino |
| `pasear_organizacion_hallar_problemas_pequenios` | **PROCEDIMIENTO** | `ENTRARIA` sin leer nada |
| `debatir_decidir_asuntos_cultura_evitar_delegar` | **NODO PROPIO, corte discutible** | `ENTRARIA` sin leer nada |

    $ python forja.py informe cuarentena/scott_radical_candor/montar_tablero_kanban_medir_actividades.json
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 1
      vecinos levantados en total      : 1
    [BLOQUEARIA] montar_tablero_kanban_medir_actividades
        vecino repartir_notas_publicar_reparto_esperado  [levantada por: paso_contra_nodo]
          similitud_texto 0.234 | familia_id 0.000 | paso_contra_nodo 0.607

    $ python forja.py informe cuarentena/scott_radical_candor/pasear_organizacion_hallar_problemas_pequenios.json
      ENTRARIAN sin leer nada          : 1
    [ENTRARIA] pasear_organizacion_hallar_problemas_pequenios

    $ python forja.py informe cuarentena/scott_radical_candor/debatir_decidir_asuntos_cultura_evitar_delegar.json
      ENTRARIAN sin leer nada          : 1
    [ENTRARIA] debatir_decidir_asuntos_cultura_evitar_delegar

**Las tres razones, con `D.27` delante** (*una linea normativa se vuelve procedimentable cuando el
libro pone su propio inventario, nombrados uno a uno por el texto*): el kanban trae el inventario de
medios literal en `L239` (tablero, tres columnas nombradas, notas de color, el acto de moverlas); el
paseo trae el acto con su periodo escrito en `L259` y el inventario de actos en `L261`; y
`debatir_decidir` trae **su propio inventario de objetos de trabajo**, los asuntos nombrados uno a uno
en `L303`, que la seccion madre no le da a ninguna otra de sus etapas.

### 3.5. Fidelidad `D.30` del tramo de once: la firmo yo y no la copio

**El instrumento cuenta los pasos. La conclusion sobre su contenido va aparte y marcada, que es lo
que `D.38.3` ensanchada manda desde el 16 sep.**

    $ python - (pasos de los once nodos que entraron en esta vuelta)
      decidir_quien_comunica_cada_cuanto                     6 pasos
      montar_reuniones_solas_mentalidad_frecuencia          22 pasos
      preguntar_seguimiento_hallar_huecos                   16 pasos
      nutrir_ideas_nuevas_reunion_solas                     10 pasos
      leer_seniales_fallo_jefe_reunion_solas                 6 pasos
      conducir_reunion_equipo_agenda_tres_bloques           22 pasos
      escribir_apuntes_sala_estudio_equipo                  14 pasos
      montar_reunion_gran_debate                            13 pasos
      montar_reunion_gran_decision                          14 pasos
      montar_reunion_general_presentaciones_preguntas       11 pasos
      pelear_proliferacion_reuniones_bloquear_ejecucion      8 pasos
      nodos nuevos en esta vuelta: 11      pasos escritos: 142

**LO QUE EL INSTRUMENTO MIDIO: `11` nodos y `142` pasos escritos.**

**`LECTURA`: de esos `142` no encuentro ni un puente. `PASOS INVENTADOS` de `cap_11` en esta vuelta,
por mi lectura, `0,00` por ciento.** Y digo como lo lei, para que se pueda romper:

- **comprobe una a una las cifras que los pasos llevan**, que es la especie que la vuelta 21 se cazo
  veintidos veces: los `20`, `15` y `30` minutos de la agenda (`L139` a `L143`); las veinte personas
  del corte (`L159` y `L161`); los cinco a siete minutos y las tres a cinco cosas (`L153`); los diez o
  menos y los cien o mas (`L209`); el veinticinco por ciento (`L231`); y los cincuenta minutos, cinco
  horas, cinco personas, veinticinco minutos, diez y veinte personas a cargo, dos o tres de cada
  trece, siete u ocho y tres o cuatro por trimestre (`L53`, `L55` y `L61`);
- **conte los inventarios contra el libro**: las catorce preguntas de `preguntar_seguimiento` son
  catorce en `L71` a `L97`; las seis de `nutrir_ideas` son seis en `L103` a `L113`; las cinco seniales
  de `leer_seniales` son cinco en `L119` a `L127`; los tres propositos del gran debate son tres en
  `L181`, `L183` y `L185`;
- **y busque lo que NO viaja**: el caso de Sheryl Sandberg de `L43`, el del consejero delegado que
  paseaba y los platos sucios de `L269` no aparecen en ningun paso, que es lo que manual `3.5` pide.

**LA UNICA FRASE QUE NO ES LITERAL, y la dejo escrita porque si la callo viaja de acta en acta:** el
paso `6` de `decidir_quien_comunica_cada_cuanto` llama a los diez rotulos *"las herramientas que el
texto enumera para sacar cosas adelante juntos"*. **La lista de `L17` a `L35` no lleva esa frase
delante**: la frase sale del subtitulo del capitulo, en `L9`. **Es un empalme de dos sitios, no un paso
inventado**, y por eso no la cuento como puente. **Que se cuente o no se cuente lo adjudico en el acta,
con el reporte delante.**

---

## 4. LO QUE MI LECTURA LEVANTA Y NINGUNA SENIAL LEVANTO

### 4.1. LA SEPTIMA ARISTA DE LA CABEZA EXISTE HOY Y NO ESTA CABLEADA

**El paso `6` de la cabeza nombra diez rotulos. Seis estan cableados. El decimo tiene su nodo EN EL
GRAFO y no lo esta.**

    $ python - (la cabeza, su paso 6 y sus nodos_siguientes)
    CABEZA: decidir_quien_comunica_cada_cuanto
    PASO 6, literal:
        Y ten delante las herramientas que el texto enumera para sacar cosas adelante juntos, que son
        las reuniones a solas, las reuniones de equipo, el tiempo para pensar, las reuniones de gran
        debate, las reuniones de gran decision, las reuniones generales, las zonas libres de
        reuniones, los tableros kanban, pasear por la organizacion y ser consciente de la cultura.

    SUS nodos_siguientes CABLEADOS: 6
       - montar_reuniones_solas_mentalidad_frecuencia
       - conducir_reunion_equipo_agenda_tres_bloques
       - montar_reunion_gran_debate
       - montar_reunion_gran_decision
       - montar_reunion_general_presentaciones_preguntas
       - bloquear_tiempo_pensar_calendario

    recorrer_rueda_conscientemente_cultura_equipo   vive en el grafo: True | cableado: False
    montar_tablero_kanban_medir_actividades         vive en el grafo: False | cableado: False
    pasear_organizacion_hallar_problemas_pequenios  vive en el grafo: False | cableado: False

    recorrer_rueda_conscientemente_cultura_equipo  nodos_previos: []
       rango declarado: las lineas 271 a 299 y de las lineas 307 a 333, bajo el rotulo
       BE CONSCIOUS OF CULTURE

**`LECTURA`: los cableables hoy son SIETE y no seis.** El decimo rotulo, `Be Conscious of Culture`, es
exactamente el tramo que `recorrer_rueda_conscientemente_cultura_equipo` declara como suyo, y ese nodo
**ya vivia en el grafo antes de esta vuelta**. La arista que falta es:

    madre : decidir_quien_comunica_cada_cuanto        paso 6, "ser consciente de la cultura"
    hija  : recorrer_rueda_conscientemente_cultura_equipo

**ES `D.29` Y NO `D.37`, y lo digo con el cuerpo de la regla delante:** la lista de `L17` a `L35`
**nombra** los rotulos pero **no dice cuantos son**, y `D.37` exige las dos cosas. Es la misma lectura
con la que se cablearon las otras seis y la misma con la que la vuelta 31 cableo la arista de
`cuidarse_agotamiento_centro_rueda`.

**Y NO LA TAPA `debatir_decidir_asuntos_cultura_evitar_delegar`, que espera en bandeja:** ese es el
rotulo interior `Debate and decide explicitly` de `L301` a `L305`, **no la seccion entera**. Si alguien
conto ese candidato como el decimo rotulo, conto una parte por el todo. **Lo adjudico en el acta, con
el reporte delante, y si el reporte lo declaro y yo no lo vi, lo dire.**

### 4.2. DOS ARISTAS MAS CON FECHA DE CADUCIDAD, Y ESTA VEZ LAS MIDO ANTES

**Las dos que quedan de la cabeza apuntan a candidatos que siguen en bandeja, y la aduana en seco dice
que NINGUNA SENIAL las va a levantar cuando entren:**

| arista que se pierde si entra sin declararla | que dice la aduana del hijo |
|---|---|
| `decidir_quien_comunica_cada_cuanto` paso 6 a `montar_tablero_kanban_medir_actividades` | `1` vecino, y **no es la cabeza**: es `repartir_notas_publicar_reparto_esperado` |
| `decidir_quien_comunica_cada_cuanto` paso 6 a `pasear_organizacion_hallar_problemas_pequenios` | `0` vecinos, `ENTRARIA sin leer nada` |

**Es la misma figura de mi `TAREA 4.d` de la vuelta pasada**, que se cumplio: la arista de
`pelear_proliferacion` entro declarada en el acto porque se dijo antes. **Estas dos van al acta igual,
y con el mismo aviso: si entran sin la declaracion, no habra ninguna corrida que vuelva a ponerlos
juntos** (`D.29`: *una arista que solo vive en la prosa de un reporte se pierde*).

**Y una tercera que NO propongo, para que se vea que no cablea todo el que lee:**
`debatir_decidir_asuntos_cultura_evitar_delegar` cuelga por contenido de
`recorrer_rueda_conscientemente_cultura_equipo`, pero **quien lo nombra es el resumen de la madre, no
un paso suyo**, y `D.37` dice que la arista se declara **citando el paso**. **Sin paso que lo nombre,
no la declaro.**

### 4.3. UNA ARISTA QUE LEVANTE YO LEYENDO Y QUE YO MISMO RETIRO

El paso `7` de `pelear_proliferacion_reuniones_bloquear_ejecucion` dice *"por la misma razon por la que
bloqueaste el tiempo para pensar"*, y eso nombra a `bloquear_tiempo_pensar_calendario`, que vive en el
grafo. **La levante y la miro con `D.29` delante: no la declaro.** El paso no enumera al otro como
parte suya ni la hija despliega ese paso; es **una cita de precedente** (`L233` del libro). `D.29` pide
una lectura argumentada, y la mia dice que no. **Lo escribo porque una arista que se descarta en
silencio es indistinguible de una que no se vio.**

### 4.4. EL PAR MAS DISCUTIBLE DEL TRAMO, Y LO MARCO YO ANTES DE VER SI EL EXTRACTOR LO MARCO

`montar_reunion_gran_debate` (cap_11) y `centrar_debate_ideas_fuera_egos` (cap_07) **comparten dos
procedimientos, no uno**: dejar los egos en la puerta y cambiar de papel a mitad del debate. En cap_07
son los pasos `8`, `9` y `10`; en cap_11 son los pasos `10` y `12`.

**MI CLASE: NO ES DUPLICADO**, por la vara `6.1`: fuera del solape, alli queda intervenir cuando
aparece el ego y redirigir a los hechos, y aqui quedan los tres propositos, la logistica de
convocatoria y el producto unico del debate. **Procedimiento en los dos lados.** Pero es el par mas
estrecho del tramo y quiero ver que veredicto se le puso.

### 4.5. EL PASO QUE NO ES PROCEDIMIENTO DENTRO DE UN NODO QUE SI LO ES

`decidir_quien_comunica_cada_cuanto` se sostiene sobre sus pasos `1` a `5`, que salen enteros de `L15`
y ordenan algo. **Su paso `6` no es procedimiento: es la lista del indice**, y la vara `6.1` dice que
nombrar no es procedimentar. **No propongo retirarlo**, porque es el paso que sostiene las aristas de
la cabeza y sin el no hay linea que citar. **Lo dejo dicho como lo que es: un paso de indice dentro de
un nodo que se sostiene sin el.**

---

## 5. LO QUE ME LLEVO AL TURNO NORMAL, PARA CONTRASTARLO CON EL REPORTE

1. **La septima arista de la cabeza** (seccion 4.1): si el reporte la declara y no la cableo, es una
   cosa; si no la vio, es otra; si conto `debatir_decidir` como el decimo rotulo, es una tercera.
2. **Las dos aristas con fecha de caducidad** (seccion 4.2), que van al encargo si el reporte no las
   trae.
3. **La razon de la linea 45** (seccion 3.2), que prueba de mas.
4. **El par del gran debate contra `centrar_debate_ideas_fuera_egos`** (seccion 4.4): ver si esta
   entre los discutibles marcados, porque eso decide si una discrepancia mia cuenta (`7.G`).
5. **Mi `0,00` por ciento de puentes** (seccion 3.5) contra el que el reporte publique.
6. **Las `16` lineas nuevas de bitacora y las `10` aristas nuevas**, que ya conte por metadato y sin
   abrir una sola razon.
7. **El censo de rutas en rojo y los `4` fallos de las pruebas** (seccion 2), que son de la fase ciega
   y son mios de llevar, no del extractor.
8. **La mitad pendiente de la `TAREA 2`**: el caso positivo de `forja.py herencia` contra las
   `ACTAS 27` y `28`.
9. **Commitear `.v31c/` en mi turno normal.** Las rutas que esta apertura publica como prueba viven
   ahi y hoy estan sin versionar (`git ls-files .v31c` devuelve `0`). Mi predecesor versiono sus `37`
   ficheros de `.v30c` y por el mismo motivo: **una ruta que prueba una corrida y no viaja al repo
   deja de probar nada en cuanto otro clone** (cosecha `7.B`).

---

*Escrito en la fase ciega de la vuelta 31. **No he abierto `REPORTE.md`, `loop.log`,
`ultimo_extractor.json` ni `ultimo_auditor.json`, y no los he recuperado de git.** Mis ficheros de
trabajo de esta fase viven en `.v31c/`. No commiteo: el arnes sella.*
