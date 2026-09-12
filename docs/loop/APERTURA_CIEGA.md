# APERTURA CIEGA DE LA VUELTA 18, escrita por el auditor ANTES de ver el reporte

*`D.34` (10 sep 2026, ampliada el 11 sep). Las dos reglas que mandan en esta fase son
`D.38.3` (aqui se publican CLASES Y LECTURAS, y toda cifra va con su instrumento pegado
al lado) y `D.38.4` (el barrido de vecinos se hace sobre GRAFO MAS BANDEJAS).*

**Rama `extraccion-mundo-11`. `HEAD` en el momento de abrir:**

    $ git log -1 --format="%H"
    9493c6c88868ee8fd81a3d4e75905bf86519f9dd

---

## 0. QUE NO HE MIRADO, Y LO DIGO PRIMERO

`docs/loop/REPORTE.md`, `docs/loop/loop.log`, `docs/loop/ultimo_extractor.json` y
`docs/loop/ultimo_auditor.json` **no estan en el arbol y no los he recuperado.** No he
corrido `git show`, ni `git checkout`, ni `git cat-file` contra ninguno de los cuatro, ni
he leido ningun cuerpo de commit. **Lo unico del turno del extractor que ha entrado por
mis ojos son los ASUNTOS de los tres ultimos commits**, que el arnes me puso delante en el
estado de git al arrancar y que no puedo des ver. Los nombro para que quede escrito:
hablan de `cap_07` con *33 piezas, 22 nodos, 11 tramos*, de la pieza 12 de `cap_05` y de
la `TAREA 1` y la `TAREA 2`. **No he usado ninguna de esas cifras para construir las
mias:** mi frontera la he contado con mi propio guion sobre el fichero fuente, y **donde
no coincidimos lo digo en la seccion 2.3.**

**Lo que si he leido, y es todo del repo y no del turno ajeno:** `AUDITOR_FORJA.md`
entero, `docs/loop/PROMPT_SIGUIENTE.md` (que es mi propia sede, `5.6`),
`docs/loop/ORDEN_DE_LOTES.md`, `D.27`, `D.30`, `D.35` y `D.38.4` del banco,
**`fuentes/scott_radical_candor/cap_07.md` entero**, y los 50 ficheros de
`cuarentena/scott_radical_candor/`.

---

## 1. EL ESTADO, MEDIDO EN ESTA FASE Y CON SU SALIDA PEGADA

    $ wc -l dataset/nodos.jsonl
    203 dataset/nodos.jsonl

    $ ls cuarentena/scott_radical_candor/*.json | wc -l
    50

    $ git status --porcelain cuarentena/scott_radical_candor/ | awk '{print $1}' | sort | uniq -c
         24 ??

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 203

    $ python forja.py rancios
    BLOQUE DE VIGENCIA VERDE.
      veredictos comprobados: 148
      citas de enlace mutuo comprobadas: 0

    $ python forja.py resolutor | tail -4
    nodos vivos: 203
    nodos deprecados (archivo): 0
    alias registrados: 0

    $ python forja.py guiones cuarentena/scott_radical_candor
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python tests/test_aceptacion.py | tail -2
      total: 77 pruebas, 0 fallos, 0 errores

**La prueba de aceptacion NO salio asi la primera vez que la corri, y la caida era MIA.**
Esta declarada entera en la seccion 9. **Esta salida verde es la de despues de limpiar lo
mio**, y las dos salidas estan pegadas alli.

### 1.1. Que capitulo trae este lote, medido y no supuesto

    $ grep -o "cap_[0-9][0-9]" cuarentena/scott_radical_candor/*.json | cut -d: -f2 | sort | uniq -c
          1 cap_04
          1 cap_05
         24 cap_07

    $ grep -l "cap_08\|cap_09\|cap_10" cuarentena/scott_radical_candor/*.json | wc -l
    0

    $ python -c "pasos de los 24 que citan cap_07"
    nodos de cap_07: 24 | pasos: 216

**El encargo de la vuelta 17 pedia `cap_07`, `cap_08`, `cap_09` y `cap_10`, en ese orden.
El arbol trae `cap_07` y nada de los otros tres.** Lo digo con la reserva que yo mismo
escribi en `ORDEN_DE_LOTES.md`: **un capitulo minado que no da nodos no deja marca en el
repo**, asi que esta medida prueba que `cap_08` a `cap_10` no han producido candidatos,
**no** que no se hayan abierto. La regla de corte que yo mismo escribi (*cierras los que
quepan ENTEROS y lo dices con su cifra*) **da por buena esta salida**; lo que compruebo en
el turno normal es que la cifra este dicha.

### 1.2. Lo que el arbol tiene sin commitear en el momento de abrir

    $ git log -1 --format="%ci"
    2026-09-12 04:29:57 -0400

    $ ls -la --time-style=+%H:%M:%S cuarentena/scott_radical_candor/recorrer_rueda_hacer_cosas_equipo.json
    04:31:02

**Los 24 candidatos de `cap_07` se escribieron DESPUES del ultimo commit y siguen sin
commitear**, junto con cinco fragmentos `.frag_*.md` de las 04:44 a las 04:49. **No lo
llamo incumplimiento del *un commit por capitulo***: el ultimo commit toca solo
`REPORTE.md` y su asunto dice que publica la frontera **antes de cortar**, que es
exactamente el orden que `D.35` manda. **Lo dejo medido para el turno normal**, donde
comprobare si el capitulo se cerro con su commit o si se quedo a medias.

---

## 2. MI FRONTERA DE `cap_07`, LEIDA POR MI Y CONTADA POR UN GUION

**He leido el capitulo entero** (433 lineas, `13.678` palabras de cuerpo medidas con
`sed -n '8,$p' | wc -w`) **y he declarado mi frontera pieza a pieza en
`.frontera_auditor_v18.py`**, que la imprime con el `sed` de cada rotulo y la cuenta el.
No he contado a ojo.

    $ python .frontera_auditor_v18.py | tail -4
    PIEZAS QUE MI LECTURA CUENTA EN cap_07: 34
      SI (yo escribiria nodo): 26
      NO (yo no extraeria)   : 8
    lineas con contenido de L8 en adelante NO cubiertas por mi frontera: 0 []

**Las cero lineas sin cubrir son la mitad que importa:** una frontera con un hueco es la
averia que costo la vuelta 7 (`D.35`), y por eso el guion la comprueba el en vez de
prometerlo yo.

### 2.1. Las 8 piezas que YO NO extraeria, con su `sed`

| lineas | `sed -n '<n>p'` | por que NO |
|---|---|---|
| L9 a L43 | `Telling people what to do doesn't work` | caso de AdSense. Diagnostico y moraleja, sin inventario de medios. `D.27` restriccion 1 |
| L45 a L63 | `TELLING PEOPLE WHAT TO DO DIDN'T WORK FOR STEVE JOBS EITHER` | tres anecdotas de Jobs. Igual que la anterior |
| L79 a L89 | `LISTEN` | cabecera de seccion: su inventario **son los dos modelos que vienen detras**, y los dos son nodo. Nombrar no es procedimentar |
| L165 a L179 | `CLARIFY` | cabecera. Ver 3.3: su contenido SI se extrajo, dentro de otro nodo |
| L213 a L223 | `DEBATE` | cabecera del bulto de rocas. `L223` dice literalmente *here are some ideas*, y esas ideas son los seis nodos siguientes |
| L303 a L321 | `PERSUADE` | cabecera. Su inventario son emocion, credibilidad y logica, que son tres nodos |
| L421 a L429 | `PART II` | material de frente de la parte II del libro |
| L431 a L433 | `5.` | cabecera del capitulo siguiente |

### 2.2. Las 26 piezas que YO SI extraeria

Son las 24 que el arbol trae **mas dos**, y las dos diferencias van con nombre:

| # | mi pieza | que hay en la bandeja |
|---|---|---|
| 1 | **L155 a L163, `Adapt to a culture of listening`** | **NADA. Es el nodo que yo escribiria y el arbol no tiene** |
| 2 | **L245 a L249 y L251 a L257 como DOS piezas** | **UN solo nodo, `fijar_fecha_cierre_debate_equipo`, que las funde** |

**26 menos las 2 diferencias son 24, que es lo que la bandeja trae.** En todo lo demas mi
corte y el suyo caen en la misma linea.

### 2.3. Mi cuenta de piezas y la del asunto del commit

El asunto del ultimo commit dice **33 piezas** y **11 tramos no extraidos**; mi guion dice
**34** y **8**. **No lo llamo discrepancia todavia y digo por que:** una *pieza* no es una
unidad definida en ninguna regla escrita, asi que **dos lecturas honradas pueden partir el
mismo capitulo en 33 o en 34 sin que ninguna mienta.** Lo que si es comparable es donde
cae el corte, y eso esta en 2.2. **Esto se resuelve en el turno normal leyendo su tabla,
no aqui.**

---

## 3. MI CLASIFICACION DE LOS 24 CANDIDATOS

### 3.1. Los punteros: 24 de 24 caen en su rotulo

*Es la guarda de `D.35` corrida por mi sobre todo el lote, no sobre una muestra.*

    $ python -c "para cada candidato, sed -n de la primera linea que declara"
    L65  a L77   recorrer_rueda_hacer_cosas_equipo      -> THE ART OF GETTING STUFF DONE WITHOUT TELLING PEOPLE WHAT TO DO
    L91  a L111  escuchar_callado...                    -> Quiet listening
    L113 a L129  escuchar_ruidoso...                    -> Loud listening
    L131 a L153  crear_cultura_escucha_equipo           -> Create a culture of listening
    L181 a L195  crear_espacio_seguro...                -> Be clear in your own mind
    L197 a L211  explicar_idea_facil...                 -> Be clear to others
    L225 a L229  centrar_debate_ideas_fuera_egos        -> Keep the conversation focused on ideas not egos
    L231 a L233  crear_obligacion_disentir_equipo       -> Create an obligation to dissent
    L235 a L237  parar_debate_emocion_agotamiento       -> Pause for emotion/exhaustion
    L239 a L243  abrir_debate_humor...                  -> Use humor and have fun
    L245 a L257  fijar_fecha_cierre_debate_equipo       -> Be clear when the debate will end
    L259 a L289  repartir_decision_cercanos_hechos      -> DECIDE
    L291 a L293  pedir_hechos_decision...               -> The decider should get facts, not recommendations
    L295 a L301  bajar_detalle_organizacion...          -> Go spelunking
    L303 a L347  persuadir_emocion_oyente_no_propia     -> PERSUADE
    L349 a L357  establecer_credibilidad...             -> Credibility
    L359 a L365  compartir_logica...                    -> Logic
    L367 a L373  minimizar_impuesto_colaboracion_equipo -> EXECUTE
    L375 a L379  proteger_tiempo_equipo_jefe            -> Don't waste your team's time
    L381 a L383  mantener_manos_trabajo_real_equipo     -> Keep the "dirt under your fingernails"
    L385 a L387  reservar_calendario_tiempo_ejecutar    -> Block time to execute
    L389 a L401  aprender_resultados...                 -> LEARN
    L403 a L407  cambiar_posicion_hechos...             -> Pressure to be consistent
    L409 a L419  cuidarse_agotamiento_centro_rueda      -> Burnout

**Cero punteros desplazados.** La averia de la vuelta 7 eran tres punteros a ocho lineas
de distancia; aqui **el `sed` de cada cita cae sobre el rotulo que el candidato dice**.

### 3.2. Mi clase de cada candidato

| candidato | pasos | mi clase |
|---|---:|---|
| `recorrer_rueda_hacer_cosas_equipo` | 12 | **SE SOSTIENE.** Cabeza de la rueda, pero `P1`, `P9`, `P10`, `P11` y `P12` son acto propio y no nombre de otro |
| `escuchar_callado_equipo_tranquilizar_incomodo` | 11 | **SE SOSTIENE.** Inventario duro: diez minutos, cara neutra, tres costes, cuatro remedios |
| `escuchar_ruidoso_opinion_fuerte_pedir_agujeros` | 13 | **SE SOSTIENE.** Idem, con la peticion de agujeros literal del libro |
| `crear_cultura_escucha_equipo` | 17 | **SE SOSTIENE.** Las tres claves del libro nombradas una a una en `P1` a `P3` |
| `crear_espacio_seguro_madurar_ideas_nuevas` | 14 | **SE SOSTIENE.** Ver 3.3 por su cabecera de tramo |
| `explicar_idea_facil_comprender_oyente` | 13 | **SE SOSTIENE** |
| `centrar_debate_ideas_fuera_egos` | 10 | **SE SOSTIENE** |
| `crear_obligacion_disentir_equipo` | 5 | **SE SOSTIENE.** Cinco pasos y cuatro son acto |
| `parar_debate_emocion_agotamiento` | 5 | **SE SOSTIENE, estrecho.** `P1`, `P3` y `P5` son *cuenta con*; los actos son `P2` y `P4` |
| `abrir_debate_humor_explicar_proposito` | 7 | **SE SOSTIENE, estrecho.** El libro lo salva con la segunda mitad, la explicacion por delante |
| `fijar_fecha_cierre_debate_equipo` | 11 | **SE SOSTIENE, y es mi DISCUTIBLE 2.** Funde dos rotulos con cuerpo propio cada uno |
| `repartir_decision_cercanos_hechos` | 11 | **SE SOSTIENE.** Absorbe la cabecera `DECIDE` y **lo declara** |
| `pedir_hechos_decision_evitar_recomendaciones` | 5 | **SE SOSTIENE, estrecho.** Dos actos y tres razones |
| `bajar_detalle_organizacion_fuente_hechos` | 9 | **SE SOSTIENE** |
| `persuadir_emocion_oyente_no_propia` | 11 | **SE SOSTIENE, y es mi DISCUTIBLE 3.** El marco de los tres elementos vive dentro de UNO de los tres |
| `establecer_credibilidad_pericia_humildad` | 9 | **SE SOSTIENE.** Ver 3.3 |
| `compartir_logica_mostrar_razonamiento` | 6 | **SE SOSTIENE** |
| `minimizar_impuesto_colaboracion_equipo` | 4 | **SE SOSTIENE AL BORDE, y es mi DISCUTIBLE 1.** Ver seccion 4 |
| `proteger_tiempo_equipo_jefe` | 9 | **SE SOSTIENE.** Es el mas denso en actos del tramo `EXECUTE` |
| `mantener_manos_trabajo_real_equipo` | 8 | **SE SOSTIENE** |
| `reservar_calendario_tiempo_ejecutar` | 4 | **EL MAS DEBIL DEL LOTE, y es mi DISCUTIBLE 4.** Ver seccion 7 |
| `aprender_resultados_vencer_dos_presiones` | 6 | **SE SOSTIENE.** Cabeza que nombra a sus dos hijos en `P6`, pero `P2`, `P3` y `P4` son acto propio |
| `cambiar_posicion_hechos_explicar_cambio` | 9 | **SE SOSTIENE** |
| `cuidarse_agotamiento_centro_rueda` | 7 | **SE SOSTIENE** |

**Y el nodo de la `TAREA 3`, que es de `cap_05` y lo encargue yo:**

| candidato | pasos | mi clase |
|---|---:|---|
| `reparar_mal_comportamiento_evitar_disculpa_falsa` | 8 | **SE SOSTIENE, y sostiene mi lectura ciega de la vuelta 17.** Los cuatro actos que yo lei en `L187` estan en `P4` a `P8`, **en secuencia** (callarse, entender, resolver, admitir al final), **y el caso de Larry va NOMBRADO dentro del `P6`**, que era la condicion con la que se admitio `TRANSCRIPCION DE CASO` |

### 3.3. Dos candidatos citan lineas fuera del tramo de su cabecera

    $ python -c "lineas citadas por los pasos FUERA del tramo declarado en la cabecera"
    crear_espacio_seguro_madurar_ideas_nuevas   cabecera L181-195  | pasos citan FUERA: [177, 179]
    establecer_credibilidad_pericia_humildad    cabecera L349-357  | pasos citan FUERA: [313]

    candidatos con cabecera y desglose: 25 | con citas fuera del tramo de cabecera: 2

**No es una caida de fidelidad y lo digo antes de nada: el desglose `D.30` de los dos SI
dice la linea buena** (*P4 y P5 de la 177; P6 de la 179* en el primero, *P1 de la linea
313* en el segundo), **y las tres lineas existen y dicen lo que el paso dice:**

    $ grep -n "Take the time to help your direct reports explain what they mean"  -> linea 177
    $ grep -n "push the people on your team to clarify their thinking"            -> linea 179
    $ grep -n "recipe for terrible results"                                       -> linea 313

**Lo que falla es la cabecera del tramo, y su consecuencia es de FRONTERA:** quien lea
*lineas 181 a 195* en una tabla de frontera **contara `L165` a `L179` como tramo no
extraido**, y no lo es. **Es la misma familia de averia que `D.35` vino a cazar**, un
puntero que dice menos de lo que el nodo hizo, solo que aqui el desglose lo salva dos
frases mas abajo.

---

## 4. LAS SIETE CABECERAS DE SECCION RECIBEN TRES TRATOS DISTINTOS

**Es mi lectura principal de esta apertura.** `cap_07` esta construido en tres pisos: la
rueda, las siete fases, y las tecnicas de cada fase. **Los nodos salieron del piso uno y
del piso tres. El piso dos, que son las siete cabeceras, recibio tres tratos diferentes:**

| seccion | cabecera | trato |
|---|---|---|
| `LISTEN` | L79 a L89 | **no extraida**, y `L85` y `L87` no las cita ningun paso de ningun candidato |
| `CLARIFY` | L165 a L179 | **absorbida** en `crear_espacio_seguro` (`P4` y `P5` de `L177`, `P6` de `L179`) **sin que su cabecera de tramo lo diga** |
| `DEBATE` | L213 a L223 | **no extraida**, y `L221` y `L223` no las cita ningun paso |
| `DECIDE` | L259 a L263 | **absorbida** en `repartir_decision_cercanos_hechos`, **y declarada** (tramo `L259` a `L289`, `P1` de `L261`) |
| `PERSUADE` | L303 a L321 | **absorbida** en `persuadir_emocion`, **y ademas en `establecer_credibilidad`** (`P1` de `L313`) sin que la cabecera de este lo diga |
| `EXECUTE` | L367 a L369 | **NODO PROPIO**: `minimizar_impuesto_colaboracion_equipo` |
| `LEARN` | L389 a L401 | **NODO PROPIO**: `aprender_resultados_vencer_dos_presiones` |

**Lo mido, no lo supongo:**

    $ python -c "lineas con contenido de cap_07 citadas por algun paso"
    lineas con contenido en cap_07 (de L8 en adelante): 213
    lineas citadas por algun paso: 73
    lineas con contenido NO citadas por ningun paso: 140

y dentro de esas 140 estan `L85`, `L87`, `L171`, `L221` y `L223`, que son las cabeceras
caidas:

    $ sed -n '221p' fuentes/scott_radical_candor/cap_07.md
    Your job as a boss is to turn on that "rock tumbler." Too many bosses think their role
    is to turn it off, to avoid all the friction by simply making a decision and sparing
    the team the pain of debate. It's not. [...]

**MI LECTURA, Y ES UNA PREGUNTA DE FRONTERA, NO DE CLASE.** Las siete cabeceras son
estructuralmente la misma cosa, y **tres tratos para siete piezas iguales es una frontera
sin regla**. Yo no pido que se extraigan las siete: **pido que la regla sea una.** Con la
vara que hay escrita (`D.27` mas *nombrar no es procedimentar*) la salida que yo defiendo
es **la de `LISTEN` y `DEBATE`**, es decir, la cabecera que solo anuncia a sus hijos no es
nodo; **y entonces `EXECUTE` y `LEARN` sobran como nodo propio y su unico contenido propio
tendria que bajar a sus hijos.** Lo traigo, no lo decido aqui.

---

## 5. EL BARRIDO DE VECINOS, `D.38.4`, GRAFO MAS BANDEJAS

### 5.1. La poblacion, con su `wc -l` pegado

    $ ls cuarentena/*/*.json | grep -v _insertados | grep -v _derivadas | wc -l
    213
    $ wc -l dataset/nodos.jsonl
    203 dataset/nodos.jsonl
    $ python -c "grafo + bandejas, descartando _insertados y _derivadas"
    grafo: 203
    bandejas: 213
    poblacion total: 416

**Y el reparto de esas 213, porque la cifra no se entiende sin el:**

    cuarentena/_derivadas/                  2   (descartada por D.38.4)
    cuarentena/_insertados/                 0   (descartada por D.38.4)
    cuarentena/ensayo_referencia_163/     163
    cuarentena/onu_consumidor/              0
    cuarentena/scott_radical_candor/       50
    cuarentena/smart_who/                   0
    cuarentena/zhuo_manager/                0

> **DIGO UNA DUDA MIA SOBRE ESTA POBLACION EN VEZ DE ESCONDERLA.** `D.38.4` dice
> `cuarentena/<libro>/`, y **`ensayo_referencia_163` no es un libro de la campania**: no
> esta en `ORDEN_DE_LOTES.md`. Sus 163 ficheros son **el 39 por ciento de mi poblacion**.
> Barro **con** ellos porque asi se barrio en la vuelta 17 (mi propio encargo publico
> `391`, que es `203 + 163 + 25`) **y una poblacion que cambia de definicion entre vueltas
> no compara nada.** Publico las dos:
>
>     con el ensayo    : 416
>     sin el ensayo    : 253
>     $ python -c "203 + len(glob('cuarentena/scott_radical_candor/*.json'))"
>     253
>
> **Que la definicion se cierre por escrito es cosa del turno normal, no de esta fase.**

### 5.2. El barrido, uno contra 415, dejandose fuera a si mismo

Cada candidato se barre contra la poblacion **menos el propio candidato**, porque si no la
guarda *el id ya vive en el grafo* lo tumba antes de comparar nada. Comprobado:

    $ FORJA_DATASET=poblacion(416) python forja.py informe recorrer_rueda_hacer_cosas_equipo.json
    [CAERIA] recorrer_rueda_hacer_cosas_equipo
        guarda: el id ya vive en el grafo

El barrido bueno, ya con el *leave one out*:

    $ python .barrido_v18/barrer.py   (y .barrido_v18/barrer2.py para los 11 que faltaban)
    BARRIDO D.38.4 COMPLETO. candidatos: 24 | faltan: []

    SIN NINGUN VECINO: 4 | CON VECINO: 20
    PARES LEVANTADOS EN TOTAL: 110
    pares por senial: {'similitud_texto': 100, 'paso_contra_nodo': 4, 'familia_id': 6}
    pares NO ordenados distintos: 70
    PARES CONTRA UN NODO QUE YA VIVE EN EL GRAFO: 5

**Los cuatro que entrarian sin que nadie lea nada:**

    ENTRARIA     crear_espacio_seguro_madurar_ideas_nuevas          vecinos= 0
    ENTRARIA     escuchar_callado_equipo_tranquilizar_incomodo      vecinos= 0
    ENTRARIA     escuchar_ruidoso_opinion_fuerte_pedir_agujeros     vecinos= 0
    ENTRARIA     recorrer_rueda_hacer_cosas_equipo                  vecinos= 0

### 5.3. Los 5 pares contra el grafo, con mi clase puesta ANTES de destapar nada

    centrar_debate_ideas_fuera_egos       vs rechazar_candidato_razones_relevantes [paso_contra_nodo]
    crear_cultura_escucha_equipo          vs juzgar_cultura_renuncias_equipo       [familia_id]
    crear_cultura_escucha_equipo          vs crear_plan_creible_equipo             [familia_id]
    crear_obligacion_disentir_equipo      vs crear_plan_creible_equipo             [familia_id]
    reservar_calendario_tiempo_ejecutar   vs reservar_tiempo_reflexion_metas       [familia_id]

| par | mi clase | por que |
|---|---|---|
| `centrar_debate` vs `rechazar_candidato_razones_relevantes` | **SANO** | uno conduce un debate, el otro descarta a un aspirante. La senial la levanta *atente a los hechos* contra *redirigelos a los hechos*, que es la misma palabra en dos trabajos distintos |
| `crear_cultura_escucha` vs `juzgar_cultura_renuncias_equipo` | **SANO** | uno **monta** un sistema de ideas y quejas; el otro **juzga** una cultura ajena por lo que esta dispuesta a ceder. La senial es `familia_id`: comparten *cultura* y *equipo* en el id |
| `crear_cultura_escucha` vs `crear_plan_creible_equipo` | **SANO** | comparten *crear* y *equipo* en el id y nada mas |
| `crear_obligacion_disentir` vs `crear_plan_creible_equipo` | **SANO** | igual que el anterior |
| `reservar_calendario_tiempo_ejecutar` vs `reservar_tiempo_reflexion_metas` | **SANO CON RESERVA, y es el unico de los cinco que releeria entero** | **el medio es el mismo**: el `P4` de la de Zhuo dice *reservar una hora en el calendario*, y el unico acto del candidato es *bloquea ese tiempo*. Lo que los separa es el OBJETO (reflexionar sobre tu trayectoria contra ejecutar un plan ya decidido) y la fase de la rueda. **Digo la parte incomoda: si mi DISCUTIBLE 4 acierta y ese candidato no es nodo, este par desaparece solo** |

**Y una lectura sobre las seniales, que es `D.19` otra vez:** **cuatro de los cinco pares
contra el grafo los levanta `familia_id`**, y los cuatro son SANO para mi. **105 de los 110
pares son `cap_07` contra `cap_07`.** Un capitulo entero sobre una sola rueda satura la
similitud de texto contra si mismo.

### 5.4. LA CIFRA QUE MAS ME IMPORTA: 12 ARISTAS QUE EL LIBRO ESCRIBE, 11 QUE NADIE VE

Tres candidatos son cabezas que **nombran a sus hijos dentro de sus propios pasos**: la
rueda nombra las siete fases, `EXECUTE` nombra sus tres tecnicas en su `P4`, y `LEARN`
nombra sus dos presiones en su `P6`. Eso son **doce aristas madre a hijo que el libro pone
por escrito**. Cruzadas contra el barrido:

    $ python -c "cruce de las cabezas contra los 70 pares del barrido"
    == LA RUEDA (L65-77) nombra las 7 fases
       escuchar_callado_equipo_tranquilizar_incomodo    -> NINGUNA SENIAL LO LEVANTA
       crear_espacio_seguro_madurar_ideas_nuevas        -> NINGUNA SENIAL LO LEVANTA
       centrar_debate_ideas_fuera_egos                  -> NINGUNA SENIAL LO LEVANTA
       repartir_decision_cercanos_hechos                -> NINGUNA SENIAL LO LEVANTA
       persuadir_emocion_oyente_no_propia               -> NINGUNA SENIAL LO LEVANTA
       minimizar_impuesto_colaboracion_equipo           -> NINGUNA SENIAL LO LEVANTA
       aprender_resultados_vencer_dos_presiones         -> NINGUNA SENIAL LO LEVANTA
    == EXECUTE (L367-373) nombra sus 3 hijos
       proteger_tiempo_equipo_jefe                      -> la senial SI lo levanta
       mantener_manos_trabajo_real_equipo               -> NINGUNA SENIAL LO LEVANTA
       reservar_calendario_tiempo_ejecutar              -> NINGUNA SENIAL LO LEVANTA
    == LEARN (L389-401) nombra sus 2 hijos
       cambiar_posicion_hechos_explicar_cambio          -> NINGUNA SENIAL LO LEVANTA
       cuidarse_agotamiento_centro_rueda                -> NINGUNA SENIAL LO LEVANTA

    aristas madre-hijo que el libro escribe: 12 | que ninguna senial levanta: 11

**`recorrer_rueda_hacer_cosas_equipo` sale del barrido con CERO vecinos.** Es la madre de
practicamente todo el capitulo **y entraria sin que nadie leyera nada**. Esto es
exactamente el caso de `D.29` (*la arista que la senial no levanta se declara por lectura*)
**multiplicado por once, y en un solo capitulo.** Lo dejo escrito aqui, en bloque
titulado, **antes de saber si el reporte las trae**: si las trae, es merito suyo; si no,
es la cola de arista mas grande que ha tenido esta casa.

---

## 6. MUESTRA DE FIDELIDAD, CON SEMILLA ESCRITA

Los 24 ficheros declaran dentro de si mismos **216 pasos, 216 TRANSCRIPCION, 0 PUENTE**:

    $ python -c "D.30 declarado DENTRO de los propios ficheros"
    cap_05    declara 8 pasos, 8 TRANSCRIPCION, 0 PUENTE  -> 0.00% inventado
    cap_07    declara 216 pasos, 216 TRANSCRIPCION, 0 PUENTE  -> 0.00% inventado

**Un cero sobre 216 es precisamente la cifra que `AUDITOR_FORJA.md` 8.3 manda no firmar
sin mirar**, porque el error que la metrica invita a cometer es marcar un puente como
transcripcion. **Asi que he mirado, aqui y no en el turno normal.** Muestra al azar, no a
ojo:

    $ python -c "random.seed(18); random.sample(pool, 8)"
    poblacion de pasos de cap_07: 216

| paso | linea que lo dice | mi veredicto |
|---|---|---|
| `compartir_logica` P6 | `grep -n "flaw in his reasoning"` da **365** | **TRANSCRIPCION** |
| `centrar_debate` P1 | `grep -n "I'm going to win this argument"` da **227** | **TRANSCRIPCION**, casi literal |
| `persuadir_emocion` P1 | `grep -n "recipe for terrible results"` da **313** | **TRANSCRIPCION** |
| `establecer_credibilidad` P1 | `grep -n "Don't forget to establish your credibility"` da **357** | **TRANSCRIPCION** |
| `cuidarse_agotamiento` P3 | `grep -n "easier said than done"` da **411** | **TRANSCRIPCION**, y ver la nota de abajo |
| `crear_cultura_escucha` P15 | `grep -n "without waiting for management"` da **147** | **TRANSCRIPCION** |
| `crear_cultura_escucha` P4 | `grep -n "help fix those things"` da **133** | **TRANSCRIPCION** |
| `explicar_idea_facil` P3 | `grep -n "stupid"` da **203** | **TRANSCRIPCION** |

**8 de 8 se sostienen, y las 8 lineas caen DENTRO del tramo que su candidato declara.**
Sobre esta muestra no tengo ninguna caida que ponerle al extractor.

> **PERO LA MUESTRA ME ENSENIA OTRA COSA, Y ES UNA LIMITACION DE LA METRICA, NO UNA CAIDA
> DE NADIE.** El `P3` de `cuidarse_agotamiento` dice *cuenta con que esto se dice mas facil
> de lo que se hace*, y la linea 411 lo dice palabra por palabra. **Es transcripcion
> perfecta y no es un paso: nadie lo ejecuta.** `D.30` mide si el paso esta en el libro;
> **no mide si es un paso.** Eso lo mide `D.27`, que es otra vara y no entra en esta cifra.
> **Un capitulo puede dar 0 por ciento de puentes y a la vez dar pasos que no son
> procedimiento**, y `cap_07` tiene unos cuantos *cuenta con* de esa especie. **No propongo
> tocar ninguna de las dos varas**: lo digo para que un `0,00` no se lea como lo que no es.

---

## 7. MIS CUATRO DISCUTIBLES, PUESTOS ANTES DE VER LOS SUYOS

**DISCUTIBLE 1. `minimizar_impuesto_colaboracion_equipo` es una cabeza cuyo inventario son
los nombres de sus hijos.** Cuatro pasos: `P2` y `P3` son *cuenta con*, y **`P4` es
literalmente la lista de los tres nodos hermanos** (*no malgastes el tiempo de tu equipo,
manten la tierra bajo tus unias, y reserva tiempo para ejecutar*). **Solo `P1` trae acto
propio.** Es el ejemplar mas limpio de *nombrar no es procedimentar* (`P.5.1`) que he visto
en este lote. **Mi clase: se sostiene al borde por `P1`**, y su verdadero problema es el de
la seccion 4.

**DISCUTIBLE 2. `fijar_fecha_cierre_debate_equipo` funde dos rotulos que el libro separa
con cuerpo propio.** No es lo mismo que la fusion de `crear_espacio_seguro`, y lo
compruebo:

    $ sed -n '181,183p'   -> "Be clear in your own mind" / (vacia) / "Create a safe space..."
    $ sed -n '245,251p'   -> "Be clear when the debate will end" / (vacia) / parrafo propio /
                             (vacia) / parrafo propio / (vacia) / "Don't grab a decision..."

**En `L181` la fusion la fuerza el libro, que no pone ni una linea entre los dos rotulos.
En `L245` no: las dos piezas tienen cuerpo.** Dicho eso, **el remedio que `L257` da para la
segunda ES la fecha de decidir de la primera**, asi que la fusion tiene una razon de fondo.
**Mi clase: admisible, pero es la unica fusion no forzada del capitulo y quiero su razon
escrita.**

**DISCUTIBLE 3. `persuadir_emocion_oyente_no_propia` mete el marco de los tres elementos
dentro de uno de los tres.** `L303` a `L321` es la cabecera que presenta emocion,
credibilidad y logica; los tres son hermanos. **Al fundirla con `Emotion`, el marco de los
tres vive dentro del primero**, y se nota porque **`establecer_credibilidad` tiene que ir a
buscar su `P1` a la linea 313**, que pertenece al tramo del hermano. **Mi clase: la de la
seccion 4.**

**DISCUTIBLE 4. `reservar_calendario_tiempo_ejecutar` es el nodo mas debil del lote.** Su
fuente son tres lineas (`L385` a `L387`), tiene cuatro pasos y **solo `P4` es acto**; los
otros tres son el sesgo del calendario y la responsabilidad del jefe. Con `D.27` delante:
el libro pone el mandato y el medio (el calendario) **y ningun inventario**. **Mi clase: yo
lo habria marcado discutible al escribirlo**, y arrastra ademas el unico par de 5.3 que
merece relectura.

**Y LA PIEZA QUE YO SI EXTRAERIA Y EL ARBOL NO TRAE: `L155` a `L163`, `Adapt to a culture
of listening`.** La traigo con la vara delante y no por gusto:

    $ sed -n '163p' fuentes/scott_radical_candor/cap_07.md
    By taking time to get to know people and by just listening she was able to build trust
    and show she cared deeply about the peace process. [...]

El libro nombra **cinco medios, uno a uno**: pasar meses solo escuchando, hacer citas
*sueltas* y no encadenadas, acudir a los actos publicos, dejar de programar a la gente
seguida, y **tener comida de verdad cuando tu invitas**. **Son medios, no metas ni fines**,
asi que la restriccion 1 de `D.27` no los tumba; **y no hay adjetivo de adecuacion en el
sitio del criterio**, asi que la restriccion 2 tampoco. **Y el caso ajeno no la tumba: este
mismo lote admitio `TRANSCRIPCION DE CASO` para el caso de Larry**, con el caso nombrado
dentro del paso. **Mi lectura: ahi hay nodo.** Si el reporte dice por que no, lo leere; si
no lo nombra, es un tramo no declarado.

---

## 8. LO QUE NO HE PODIDO MEDIR EN ESTA FASE, Y NO LO PUBLICO COMO MEDIDO

- **La tabla de `PASOS INVENTADOS POR CAPITULO` NO la firmo aqui.** Tengo el denominador
  contado por mi (`216` pasos de `cap_07`, `8` de `cap_05`) y tengo lo que los ficheros
  declaran (`0` puentes), **pero el numerador de verdad sale de releer la muestra contra su
  parrafo**, y he releido **8 de 216**. La cifra firmada va en el acta, no aqui.
- **Si `cap_08` a `cap_10` se abrieron y no dieron nodos, el arbol no lo puede decir.** Lo
  medido es que no hay candidatos suyos.
- **Las clases de 3.2 son mias y ciegas.** No he abierto `bitacora/VEREDICTOS.jsonl` para
  ninguno de los 24, porque ninguno esta insertado y por tanto no tiene veredicto. **Lo que
  si mire, y lo digo, fueron los 12 `arista_corregida` de la `TAREA 2`**, que son registro
  de datos y no lectura de par:

      $ grep -c arista_corregida bitacora/VEREDICTOS.jsonl
      12
      $ python -c "las 12 corregidas contra las aristas del grafo por par ORDENADO"
      aristas distintas en el grafo (par ORDENADO): 79
      de las 12 corregidas: cuadran con el grafo = 12 | no cuadran = 0
      CONTINUA revisados: 79 | sin arista por par ORDENADO: 0
      $ grep -n '"arista"' src/aduana.py src/arista.py
      src/aduana.py:1036:            "arista": ("%s > %s" % (madre, hijo))
      src/arista.py:184:        "arista": "%s > %s" % (madre, hijo),

  **Las doce cuadran y el campo viejo sigue donde estaba.** La `TAREA 2` se cerro como la
  encargue; que la prueba **muerda** lo compruebo por mutacion en el turno normal, que es
  lo que `5.5` manda y aqui no he hecho.

---

## 9. MI PROPIA CAIDA DE ESTA FASE, DECLARADA CONTRA MI

**LA PRIMERA VEZ QUE CORRI LA PRUEBA DE ACEPTACION EN ESTA FASE, SALIO EN ROJO, Y LA CAUSA
ERA MIA:**

    $ python tests/test_aceptacion.py | tail -2
      total: 77 pruebas, 1 fallos, 0 errores

    FAIL: test_e_guion_largo_rompe_el_hook
    AssertionError: 1 != 0 : el repo ha de estar limpio antes de ensuciarlo:
    BARRIDO DE GUIONES EN ROJO: 18 hallazgo(s)
      .barrido_v18/pob.jsonl linea 301 columna 1687: guion largo (U+2014)
      poblacion_apertura_v18.jsonl linea 275 columna 1687: guion largo (U+2014)
      ... los 18 hallazgos, en dos ficheros mios

**Los 18 hallazgos eran de dos ficheros de usar y tirar que yo escribi DENTRO del repo**
para montar la poblacion del barrido. `D.38.4` escribe su ejemplo en `/tmp/poblacion.jsonl`,
**fuera del arbol, y yo lo puse dentro.** Los guiones venian de cinco ficheros de
`cuarentena/ensayo_referencia_163/`, que el barrido no mira por regla, **y mi copia los
saco de la bandeja y los puso donde el barrido si mira.**

**Lo corregi borrando lo mio, y vuelvo a medir:**

    $ rm -f poblacion_apertura_v18.jsonl .barrido_v18/pob.jsonl .barrido_v18/pob2.jsonl .barrido_v18/*.line
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python tests/test_aceptacion.py | tail -2
      total: 77 pruebas, 0 fallos, 0 errores

**PARA QUE NO SE ME CUELE COMO CAIDA AJENA, QUE ES EXACTAMENTE LO QUE ME PASO EN LA VUELTA
16:** el rojo **no lo produjo ningun fichero del extractor**, y lo compruebo por separado:

    $ python -c "guiones largos o medios dentro de las bandejas"
    ficheros de bandeja con guion largo o medio: 5
      cuarentena/ensayo_referencia_163/estrategia_multicanal_bienvenida.json  2
      cuarentena/ensayo_referencia_163/metas_vs_proposito.json  2
      cuarentena/ensayo_referencia_163/mitos_stage_gate.json  2
      cuarentena/ensayo_referencia_163/restricciones_extremas_como_innovacion.json  2
      cuarentena/ensayo_referencia_163/sistemas_alta_confiabilidad_hro.json  1
    de esos, del lote 4 scott_radical_candor: 0

**Cero en el lote 4.** La especie de esta caida mia la adjudico en el acta con la tabla de
`D.38.2` delante; **la dejo escrita aqui, que es donde ocurrio, y no espero a que me la
encuentre nadie.**

---

## 10. LOS TESTIGOS DE ESTA FASE, CON SU TAMANIO

*Porque una ruta publicada como prueba es CIFRA (`5.5`), y un testigo en cero bytes es un
turno mudo.*

    $ wc -c .frontera_auditor_v18.py .barrido_v18/BARRIDO_NUEVOS.txt .barrido_v18/BARRIDO_RESTO.txt .barrido_v18/barrer.py
      1335 .frontera_auditor_v18.py
     57302 .barrido_v18/BARRIDO_NUEVOS.txt
     14942 .barrido_v18/BARRIDO_RESTO.txt
      1103 .barrido_v18/barrer.py
     74682 total

**Ninguno en cero bytes.** `.barrido_v18/BARRIDO_NUEVOS.txt` trae 13 de los 24 candidatos y
`.barrido_v18/BARRIDO_RESTO.txt` los 11 restantes, **y el corte en dos es culpa mia**: el
primer guion que escribi para barrer se quedo enganchado, tuve que rehacerlo, y por eso el
primer fichero tiene bloques repetidos. **Quien lo cruce debe deduplicar por id**, que es
lo que hace el guion que imprime el resumen de 5.2, y con esa deduplicacion la cuenta sale:

    $ python -c "merge de los dos ficheros, deduplicando por id"
    candidatos con bloque: 24 | faltan: []
    sin vecino: 4
    pares totales: 110

---

**FIN DE LA APERTURA CIEGA.** No toco este fichero a partir de aqui: el sello del arnes se
verifica al cerrar mi turno y un sello roto detiene la corrida.
