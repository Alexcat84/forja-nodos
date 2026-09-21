# APERTURA CIEGA DE LA VUELTA 48, AUDITOR

**Corrida `VUELTA 4` del `loop.log`, lote 7 (`grove_high_output`), `cap_04`.**
Esta pagina se escribe **antes** de que el arnes me exponga `docs/loop/REPORTE.md`, y el
arnes la sella. Todo lo que hay aqui es lectura mia sobre el material, con el instrumento
que la mide pegado al lado (`D.38.3`).

---

## 48.0. LA DECLARACION QUE EL ARNES EXIGE (`D.40`)

    ACTA ANTERIOR LEIDA: a658c0097bb958805b552777defc86bcae1f3434
    HEREDADO 1: CUMPLIDO
    HEREDADO 2: CUMPLIDO

**LA HUELLA NO LA COPIO DEL PROMPT: LA MIDO.**

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    a658c0097bb958805b552777defc86bcae1f3434
    (la huella que el prompt me entrega: a658c0097bb958805b552777defc86bcae1f3434)

**`HEREDADO 1`, el de los superlativos.** Me obliga a que **todo superlativo que yo publique
lleve debajo la LISTA ORDENADA ENTERA** salida de un instrumento mio corrido en esta misma
fase. **Aplica y lo cumplo:** esta pagina publica sus superlativos con su lista entera
debajo, en `48.2` y `48.5` (los cuatro tramos de la tanda ordenados por palabras, que es la
lista que desmiente el superlativo del extractor) y en `48.7` (los ocho vecinos mas proximos
de cada candidato, lista entera, con su umbral y con su poblacion declarada). **Ningun
superlativo de esta pagina esta desnudo**, y donde no he podido ordenar la lista entera **no
escribo el superlativo: escribo la limitacion** (`48.1`).

**`HEREDADO 2`, el de la tabla fuera de cita.** Me obliga a que mis remedios salgan por
`src/herencia.py` en vez de depender de que yo relea mi acta. **Aplica, se comprueba con el
instrumento que el propio remedio nombra, y sale CUMPLIDO:**

    $ python forja.py herencia | grep -E "^  (su huella|heredados)|^HEREDADO"
      su huella     : a658c0097bb958805b552777defc86bcae1f3434
      heredados     : 2
    HEREDADO 1   [REMEDIO, linea 35926 del acta]
    HEREDADO 2   [REMEDIO, linea 35927 del acta]

(el `grep` recorta solo la linea de resumen del acta anterior, que ocupa un parrafo entero y
que el prompt ya me entrega igual; lo que se comprueba aqui son la huella y el `2`)

**El remedio decia literalmente *si entrega `0`, roto*. Entrega `2`.** Las dos filas salen de
`46.10.a`, que escribi en TABLA y fuera de bloque de cita, que es exactamente lo que el
remedio me obligaba a hacer.

---

## 48.1. LO QUE NO VEO, Y LO QUE POR ESO NO AFIRMO

**LA LINEA DEL ARNES, COMPROBADA EN SU SEDE.** `loop.log` no se retira, asi que lo abro:

    $ tail -3 docs/loop/loop.log
    [2026-09-19 08:39:03] VUELTA 4 : APERTURA CIEGA (claude-opus-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl
    [2026-09-19 08:39:03]   hereda 2 remedio(s) del acta anterior, entregados en el prompt (D.40)
    [2026-09-19 08:39:03]   y solo eso: remedios con su motivo, sin cifras ni conclusiones (D.52)

**NO RECUPERO NINGUNO DE LOS CUATRO.** No he corrido `git show` ni `git checkout` sobre
`docs/loop/REPORTE.md`, `ultimo_extractor.json`, `ultimo_auditor.json` ni
`CREDITO_serial.jsonl`, y **no he abierto ningun fichero de `.v48/`**, que es la carpeta de
trabajo del extractor: sus `informe_0N.txt`, sus `reloj_cN.txt` y su `tanda_cap_04.txt` son
**su** medida, y leerlos seria leer a ojo lo que vengo a leer a ciegas.

**LO QUE SI HE VISTO Y LO DIGO EN VEZ DE CALLARLO:** para saber **que fichas nacieron en esta
vuelta** he corrido `git show --name-status HEAD`, y la salida de `git` trae el **asunto y el
cuerpo del commit de cabeza**, que resumen lo que el extractor dice haber hecho. **No es
ninguno de los cuatro retirados**, y `AUDITOR_FORJA.md` `5.6` dice que el asunto de un commit
no es sede de cifra, **pero lo he leido y callarlo seria peor que declararlo.** Lo que hago
con el: **ni una cifra de esta pagina sale de ahi.** Las cinco fichas, los `42` pasos, las
palabras de cada tramo, los `18` ids de arista y los vecinos **los he contado yo con los
instrumentos de `.v48aud/`**; donde mi cuenta coincide con la suya lo digo, y donde no
coincide lo digo tambien (`48.5`).

**LAS TRES COSAS QUE NO PUEDO COMPROBAR EN ESTA FASE, Y QUE POR ESO NO AFIRMO** (`1.1`: una
busqueda negativa no se puede citar):

| lo que no puedo | por que | que escribo en su lugar |
|---|---|---|
| **si la frontera de `cap_04` adjudico `0` nodos a `L287` y a `L291`** | la tabla de las `44` filas de la frontera vive en `docs/loop/REPORTE.md`, retirado | mido **quien cita cada renglon hoy** (`48.4`), que no depende del reporte |
| **si `P38` es el quinto tramo del capitulo entero** | ordenar los `44` tramos exige esa misma tabla. Mi instrumento del turno anterior, `.v47aud/44_tramos.py`, **lee `REPORTE.md` y hoy no puede correr** | ordeno **los cuatro tramos de esta tanda**, que salen de las propias fichas (`48.2`) |
| **si el puesto `36 de 44` de `P36` es correcto** | lo mismo | lo dejo **a verificar** en mi turno normal |

---

## 48.2. LA MESA: QUE MATERIAL HAY, MEDIDO

**LAS FICHAS QUE NACIERON EN ESTA VUELTA, SACADAS DE `git` Y NO DE NINGUN REPORTE:**

    $ sh .v48aud/02_candidatos_nuevos.sh
    cuarentena/grove_high_output/buscar_regularidad_bloques_iguales_trabajo_mando.json
    cuarentena/grove_high_output/decir_no_trabajo_excede_capacidad.json
    cuarentena/grove_high_output/dimensionar_numero_subordinados_medio_dia_semanal.json
    cuarentena/grove_high_output/llevar_inventario_proyectos_discrecionales.json
    cuarentena/grove_high_output/usar_calendario_herramienta_planificacion_produccion.json
    --- total ---
    5

**LOS PASOS, CONTADOS POR MI, QUE SON EL DENOMINADOR DE TODA LA FIDELIDAD `D.30`:**

    $ python .v48aud/04_pasos.py
    PASOS POR FICHA, LISTA ORDENADA ENTERA de mas a menos:
       11 pasos    2 atribuciones   previos 0  siguientes 0   dimensionar_numero_subordinados_medio_dia_semanal
       10 pasos    0 atribuciones   previos 0  siguientes 0   decir_no_trabajo_excede_capacidad
        9 pasos    0 atribuciones   previos 0  siguientes 0   buscar_regularidad_bloques_iguales_trabajo_mando
        7 pasos    0 atribuciones   previos 0  siguientes 0   usar_calendario_herramienta_planificacion_produccion
        5 pasos    0 atribuciones   previos 0  siguientes 0   llevar_inventario_proyectos_discrecionales

    TOTAL de pasos escritos en la tanda: 42 en 5 fichas

**LOS TRAMOS DEL LIBRO DE LOS QUE SALEN, CONTADOS SOBRE EL TEXTO FUENTE.** Los rangos de
linea los declara cada ficha en su `resumen_teorico`; **las palabras las cuento yo del
`.md`**, no de ninguna tabla:

    $ python .v48aud/01_palabras_tramos.py
    LOS TRAMOS DE LA TANDA DE LA VUELTA 48, LISTA ORDENADA ENTERA de mas a menos palabras:
       P34   L273 a L285   469 palabras   candidatos usar_calendario... y decir_no...
       P38   L293 a L301   396 palabras   candidato dimensionar_numero_subordinados...
       P39   L303 a L307   242 palabras   candidato buscar_regularidad_bloques_iguales...
       P36   L289 a L289   101 palabras   candidato llevar_inventario_proyectos_discrecionales

**LECTURA:** `4` tramos dan `5` fichas porque `P34` da dos, y **las dos fichas de `P34`
declaran su frontera interna antes de cortar**: `L277` mas `L283` mas `L285` a una, `L273`
mas `L275` mas `L281` a la otra, y `L279` (la frase que numera las dos responsabilidades)
**compartida a proposito**. Es la unica linea que las dos citan, y lo he comprobado leyendo
las dos fichas y el renglon.

---

## 48.3. MI LECTURA, CANDIDATO A CANDIDATO, ADJUDICADA ANTES DE VER EL REPORTE

**COMO LA HAGO:** imprimo cada paso al lado del renglon del libro que su propia ficha cita,
con un instrumento mio, y leo los dos textos juntos. Ninguno de los `42` se quedo sin
renglon:

    $ python .v48aud/13_pasos_contra_renglon.py | tail -1
    pasos impresos junto a su renglon: 42
    $ grep -c "cita L??" .v48aud/13_pasos_contra_renglon.out
    0

Y el renglon lo leo del libro, no de la ficha:

    $ awk 'NR>=273 && NR<=307' fuentes/grove_high_output/cap_04.md

### 48.3.a. `usar_calendario_herramienta_planificacion_produccion` (`7` pasos, `P34` primera mitad)

| | mi clase |
|---|---|
| **es nodo** | **SI.** El libro pone su propio inventario de actos (`run by forecast and not by individual order`, `forecasting those things you can and setting yourself up to do them`, `use his calendar as a production planning tool`, `taking a firm initiative to schedule work that is not time-critical between those limiting steps`) y el criterio **no** es un adjetivo de adecuacion: dice **que** se coloca (lo no critico en tiempo) y **donde** (entre los pasos limitantes). Prueba del inventario de `EXTRACTOR.md` `9.1`, cara positiva |
| **fidelidad `D.30`** | **`7` de `7` TRANSCRIPCION, `0` PUENTE**, leidos uno a uno contra `L273`, `L275`, `L279` y `L281` |
| **vara `6.1` contra su vecino de dentro del libro** | **CONTINUA**, no repite, a `identificar_paso_limitante_jornada_desfases` |

**LA LECTURA DE LA VARA, ESCRITA ANTES DE DESTAPAR NADA.** El solape existe y lo nombro: el
paso `6` de este nodo (*programar el trabajo que no es critico en tiempo entre los pasos
limitantes*) y el paso `4` de `identificar_paso_limitante_jornada_desfases` (*crea desfases y
programa el resto de tu trabajo alrededor de ese paso limitante*) **mandan el mismo acto**.
La vara `6.1` dice que **el tamanio del solape no decide** y que decide **si lo que queda
fuera es procedimiento en los dos lados**. Lo que queda fuera aqui: el pronostico como marco,
el calendario como medio, el diagnostico del calendario como deposito pasivo, y la
responsabilidad numerada `1`. Lo que queda fuera alli: **como se encuentra** el paso limitante
(la pregunta del huevo, el calendario absoluto). **Procedimiento propio en los dos lados: no
es duplicado.**

**MI DISCUTIBLE, MARCADO ANTES DE SABER SI ACIERTO:** el paso `1` convierte en imperativo una
frase que el libro escribe **como pregunta** (`What makes running a factory different from
running a job shop?`). Es fiel en contenido y cambiado en modo. Lo sostengo porque el
contraste fabrica contra taller lo escribe `L273` entero, **pero lo marco yo y no me lo
callo**.

### 48.3.b. `decir_no_trabajo_excede_capacidad` (`10` pasos, `P34` segunda mitad)

| | mi clase |
|---|---|
| **es nodo** | **SI.** Inventario propio del libro, de objetos y de etapas: los indicadores de capacidad, el nivel de entrada, las tres actividades cuyo tiempo se estima, el momento del no (`at the outset`) y las dos formas del no. El criterio es **de etapa**, no un adjetivo |
| **fidelidad `D.30`** | **`10` de `10` TRANSCRIPCION, `0` PUENTE**, contra `L277`, `L279`, `L283` y `L285` |
| **vara `6.1`** | **FRONTERA DECLARADA** con su hermano `usar_calendario...`: comparten `L279` y ni un paso |

**LO QUE ME PARECE LO MEJOR DE ESTA FICHA, Y LO DIGO PORQUE SE LO VOY A COBRAR SI FALLA EN
OTRA:** declara que **estuvo a punto de escribir un paso de MEDIR la capacidad** y no lo
escribio, porque `L277` dice lo contrario (*you may not know precisely, but you surely have a
feel*). Lo he comprobado en el renglon: **el libro no manda medir**, manda explotar una
sensacion. Un paso de medicion habria sido un **PUENTE**. Mi lectura coincide con la suya.

**MI DISCUTIBLE:** los pasos `1` y `2` son el paralelo de fabrica, o sea un caso de otro
dominio puesto como pasos. Sostengo que entran, porque `L277` escribe el acto del mando con
un `Instead` que **solo tiene sentido contra ese paralelo**.

### 48.3.c. `llevar_inventario_proyectos_discrecionales` (`5` pasos, `P36` = `L289`, un solo renglon)

| | mi clase |
|---|---|
| **es nodo** | **SI, y es el caso justo de `9.1`.** El libro nombra el inventario (`raw material inventory in terms of projects`), lo separa de otro (`work-in-process`), y **pone su criterio exacto** de que entra (`things you need to do but don't need to finish right away`) y para que (`to increase his group's productivity over the long term`). **No hay adjetivo de adecuacion en el sitio del criterio** |
| **fidelidad `D.30`** | **`5` de `5` TRANSCRIPCION, `0` PUENTE**, los cinco contra `L289` |
| **vara `6.1`** | **CONTINUA** a `dimensionar_inventario_materia_prima_reposicion` de `cap_02`: alli el inventario se dimensiona por reposicion, aqui se llena por criterio. Cero pasos comunes |

**MI DISCUTIBLE, EL MISMO QUE LA FICHA SE MARCA:** el paso `5` es una **consecuencia** y no un
acto. Lo sostengo, y con el mismo argumento que ella: es la frase de cierre literal del
renglon y es lo unico que dice **para que** se lleva el inventario. **Que coincidamos no lo
valida**, y lo apunto para releerlo con el reporte delante.

### 48.3.d. `dimensionar_numero_subordinados_medio_dia_semanal` (`11` pasos, `P38`)

| | mi clase |
|---|---|
| **es nodo** | **SI, y con el inventario mas explicito de los cinco**: el libro pone **su propia cifra** (`six to eight`), sus dos bordes malos (`three or four`, `ten`), la guia de la que sale (`about a half day per week`) y los dos contrastes de esa guia (`two days a week`, `an hour a week`) |
| **fidelidad `D.30`** | **`11` de `11` TRANSCRIPCION, `0` PUENTE**, contra `L295`, `L297`, `L299` y `L301` |
| **cifras del autor** | **BIEN PUESTAS**: las dos van en `atribuciones` con autor, fuente y fecha de corte, que es lo que los principios `5` y `8` mandan. Contadas por mi: `2` atribuciones (`48.2`) |
| **vara `6.1`** | **CONTINUA** a `dimensionar_plantilla_administrativa_pronostico` de `cap_02`: alli se dimensiona una plantilla contra un pronostico de carga, aqui un reparto contra una guia de tiempo por persona |

**MI DISCUTIBLE:** el paso `10` convierte en instruccion (*colocalo de forma que...*) lo que
`L299` escribe como **descripcion de un arreglo** (*The arrangement, shown below, does not
have the engineers appearing...*). El libro **constata** y la ficha **manda**. Lo marco yo:
es el sitio mas fino de los `42` pasos y es donde mirare primero cuando tenga el reporte.

**Y AQUI ESTAN LAS DOS COSAS QUE NO ME CUADRAN, QUE VAN EN `48.5` Y EN `48.6`.**

### 48.3.e. `buscar_regularidad_bloques_iguales_trabajo_mando` (`9` pasos, `P39`)

| | mi clase |
|---|---|
| **es nodo** | **SI.** Inventario propio de medios, nombrados uno a uno por el libro: alisar la carga, dar al trabajo las caracteristicas de una fabrica, impedir los parones y arranques, abrir ventanas en la caja negra, coordinar con los demas mandos, y usar los mismos bloques para las actividades iguales |
| **fidelidad `D.30`** | **`9` de `9` TRANSCRIPCION, `0` PUENTE**, contra `L305` y `L307` |
| **vara `6.1`** | **CONTINUA** a `agrupar_tareas_semejantes_aprovechar_preparacion`. Los dos tocan *actividades iguales* y **el objeto es distinto**: alli el objeto es el **tiempo de preparacion** que se reutiliza, aqui la **regularidad del bloque** y su coordinacion con otros mandos. Cero pasos comunes, leidos los seis de alla y los nueve de aca |

**EL SITIO DONDE UN PUENTE ERA FACIL Y NO ESTA:** el paso `9` mete el lunes de Intel **como
ejemplo nombrado** y **no** como periodo a seguir. Comprobado en `L307`: el libro escribe
`For example, at Intel`, y la regla que enuncia (`the same blocks of time must be used for
like activities`) **no trae ni cuantos bloques, ni cuan largos, ni cada cuanto**. Un paso que
mandara *reserva un bloque semanal* habria sido un puente de la especie del periodo. **No
esta.** Manual `3.5`, el caso dentro de la doctrina: **bien aplicado.**

**MI DISCUTIBLE:** el paso `9` es un caso y no un acto, y el paso `6` es una consecuencia. Los
dos los marca tambien la ficha. Los sostengo los dos.

### 48.3.f. EL SALDO DE MI LECTURA CIEGA

| | |
|---|---|
| **fichas que para mi SI son nodo** | **`5` de `5`** |
| **pasos que para mi son PUENTE** | **`0` de `42`**, contados los `42` por mi (`48.2`) y leidos los `42` contra su renglon |
| **pares que para mi son DUPLICADO** | **`0`**. Cuatro proximidades reales nombradas arriba, **las cuatro CONTINUA por la vara `6.1`** |
| **discutibles que marco yo** | **`2` propios** (el imperativo sobre pregunta de `48.3.a` y la instruccion sobre descripcion de `48.3.d`), mas los que las fichas ya se marcan |

---

## 48.4. EL RENGLON QUE NO RECLAMA NADIE: `L287`

**LO QUE MIDO, Y ES UNA MEDIDA DE SEDE Y NO UNA OPINION:** que renglones de `cap_04` cita
**algun nodo que exista hoy**, en el grafo o en la bandeja. No toca el reporte:

    $ python .v48aud/05_lineas_cubiertas.py
    fichas leidas (grafo + bandejas): 553
    renglones NO VACIOS de cap_04 entre L265 y L310, y quien los cita:
      L265  74 palabras  CITADO por identificar_paso_limitante_jornada_desfases
      L267  122 palabras  CITADO por identificar_paso_limitante_jornada_desfases, subir_productividad_gerencial_tres_vias
      L269  117 palabras  CITADO por agrupar_tareas_semejantes_aprovechar_preparacion
      L271  95 palabras  CITADO por agrupar_tareas_semejantes_aprovechar_preparacion
      L273  112 palabras  CITADO por decir_no_trabajo_excede_capacidad, usar_calendario_herramienta_planificacion_produccion
      L275  86 palabras  CITADO por decir_no_trabajo_excede_capacidad, usar_calendario_herramienta_planificacion_produccion
      L277  131 palabras  CITADO por decir_no_trabajo_excede_capacidad, usar_calendario_herramienta_planificacion_produccion
      L279  15 palabras  CITADO por decir_no_trabajo_excede_capacidad, usar_calendario_herramienta_planificacion_produccion
      L281  27 palabras  CITADO por decir_no_trabajo_excede_capacidad, usar_calendario_herramienta_planificacion_produccion
      L283  15 palabras  CITADO por decir_no_trabajo_excede_capacidad, usar_calendario_herramienta_planificacion_produccion
      L285  83 palabras  CITADO por decir_no_trabajo_excede_capacidad, usar_calendario_herramienta_planificacion_produccion
      L287  132 palabras  >>> SIN CITA DE NINGUN NODO
      L289  101 palabras  CITADO por llevar_inventario_proyectos_discrecionales, usar_calendario_herramienta_planificacion_produccion
      L291  108 palabras  >>> SIN CITA DE NINGUN NODO
      L293   8 palabras  CITADO por dimensionar_numero_subordinados_medio_dia_semanal
      L295  110 palabras  CITADO por dimensionar_numero_subordinados_medio_dia_semanal
      L297  120 palabras  CITADO por dimensionar_numero_subordinados_medio_dia_semanal
      L299  143 palabras  CITADO por dimensionar_numero_subordinados_medio_dia_semanal
      L301  15 palabras  CITADO por dimensionar_numero_subordinados_medio_dia_semanal
      L303   5 palabras  CITADO por buscar_regularidad_bloques_iguales_trabajo_mando, usar_calendario_herramienta_planificacion_produccion
      L305  162 palabras  CITADO por buscar_regularidad_bloques_iguales_trabajo_mando
      L307  75 palabras  CITADO por buscar_regularidad_bloques_iguales_trabajo_mando
      L309  51 palabras  >>> SIN CITA DE NINGUN NODO

**LECTURA, Y ES MIA:** de los tres renglones sin cita, **dos estan bien sin ella y uno no me
lo explico.**

- **`L309` (`51` palabras)**: es el montaje de un experimento (*About twenty middle managers
  at Intel were once asked to be part of an experiment*). **No pone procedimiento: no es
  nodo.**
- **`L291` (`108` palabras)**: *A final principle*, la consistencia de los metodos. Lo he
  leido entero y **no pone inventario propio de medios, etapas ni objetos**: pone un mandato
  (`we should work to change that`) y una advertencia sobre donde vive el valor de un
  procedimiento administrativo. Por `EXTRACTOR.md` `9.1` y por la tabla de `9`, **eso es
  POSTURA, no nodo.**
- **`L287` (`132` palabras), Y ESTE SI ME CHIRRIA**: es el principio de produccion de la
  **holgura**. Abre igual que los otros de la serie (*The next production principle you can
  apply is to allow slack*), y **pone un criterio que no es un adjetivo de adecuacion**:
  `with enough slack built in so that one unanticipated phone call will not ruin your
  schedule for the rest of the day`. Eso es una **prueba concreta**, que es justo lo que
  `9.1` pide para separar procedimiento de postura.

**LA COMPARACION QUE LO CONVIERTE EN PREGUNTA Y NO EN CAPRICHO MIO:** `L289` **si** tiene nodo
en esta misma tanda, es de **la misma serie de principios de produccion**, abre con la misma
formula, y **es mas corto**:

| renglon | palabras | como abre | nodo hoy |
|---|---|---|---|
| `L287` | **`132`** | *The next production principle you can apply is to allow slack* | **NINGUNO** |
| `L289` | **`101`** | *Another production principle is very nearly the opposite* | `llevar_inventario_proyectos_discrecionales`, `5` pasos |

**LO QUE NO AFIRMO:** **no digo que el extractor se lo saltara.** La frontera de la vuelta
`46` pudo adjudicarle `0` nodos con su motivo escrito, y **esa tabla vive en `REPORTE.md`, que
hoy no puedo abrir** (`48.1`). **Lo que si afirma esta pagina, porque lo he medido:** hoy,
`19` de septiembre de `2026`, **ningun nodo del grafo ni de ninguna bandeja cita `L287`**, y
`L287` no esta entre los tres renglones que las fichas declaran pendientes para la vuelta
`49`, que son `L315`, `L317` y `L321`.

**ESTO ES LO PRIMERO QUE VOY A MIRAR EN EL REPORTE.**

---

## 48.5. UN SUPERLATIVO DE LA TANDA QUE MI CUENTA DESMIENTE

**DONDE ESTA.** En el `resumen_teorico` de `dimensionar_numero_subordinados_medio_dia_semanal`,
sobre su tramo `P38`:

> *Es el tramo mas rico de esta tanda y el quinto del capitulo entero, medido por
> `.v47aud/44_tramos.py` corrido por mi en esta vuelta.*

**MI MEDIDA, CONTADA DEL TEXTO FUENTE, CON LA LISTA ORDENADA ENTERA DEBAJO** (que es
exactamente lo que mi `HEREDADO 1` me obliga a poner, y lo que aqui falta):

    $ python .v48aud/01_palabras_tramos.py
    LOS TRAMOS DE LA TANDA DE LA VUELTA 48, LISTA ORDENADA ENTERA de mas a menos palabras:
       P34   L273 a L285   469 palabras   candidatos usar_calendario... y decir_no...
       P38   L293 a L301   396 palabras   candidato dimensionar_numero_subordinados...
       P39   L303 a L307   242 palabras   candidato buscar_regularidad_bloques_iguales...
       P36   L289 a L289   101 palabras   candidato llevar_inventario_proyectos_discrecionales

**`P34` tiene `469` palabras y `P38` tiene `396`.** Y `P34` **es de esta misma tanda**: da dos
de los cinco candidatos (`usar_calendario...` y `decir_no...`), y las dos fichas lo escriben
en su propia primera linea. **El tramo mas rico de esta tanda es `P34`, no `P38`.**

**Y NO ES UNA DISCREPANCIA DE METODO:** mi instrumento cuenta palabras del `.md` y le salen
`469` para `P34`, `396` para `P38`, `242` para `P39` y `101` para `P36`, **los cuatro numeros
identicos a los que las cuatro fichas declaran**. Medimos igual. **Lo que falla es la frase,
no la cifra**, que es la figura exacta de `D.38.3` ensanchada: *contar campos y publicar una
frase sobre contenido es caida de cifra*.

**ES LA MISMA CAIDA QUE LE CARGUE EN `46.6`**, con otro tramo y otra vuelta: alli `P27` con
`347` publicado como el mas rico cuando `P24` tenia `356`; aqui `P38` con `396` publicado como
el mas rico cuando `P34` tiene `469`. **Dos vueltas seguidas, la misma especie de frase.**

**Y HAY UN AGRAVANTE DE FORMA QUE PUEDO COMPROBAR SIN EL REPORTE, PORQUE EL GUION ES MIO Y
ESTA EN EL ARBOL.** La ficha dice que la medida sale de `.v47aud/44_tramos.py`. Ese guion lo
escribi yo y **lo primero que imprime es la lista ordenada entera**:

    $ head -14 .v47aud/44_tramos.py | tail -2
    print("LOS 44 TRAMOS ORDENADOS POR PALABRAS, LISTA ENTERA, de mas a menos:")
    for p, w, n in sorted(filas, key=lambda f: -f[1]):

**El instrumento que se cita no da un numero suelto: da el orden entero.** Quien lo corriera
tenia `P34` y `P38` en la misma lista, uno encima del otro. **Y aun asi el superlativo se
publico sin la lista debajo**, que es exactamente el remedio que yo me impuse para esta vuelta
y la razon de que me lo impusiera.

**LO QUE NO ADJUDICO HOY, Y POR QUE.** La especie y la sede las decido en mi turno normal, con
el reporte delante: si la frase vive **solo** en `docs/loop/REPORTE.md` es `REPORTE`, y `5.2`
manda mirar si esta en tabla, cabecera o conclusion; **pero esta frase esta escrita dentro del
`resumen_teorico` de una ficha de `cuarentena/`**, y una ficha de cuarentena esta a un paso de
ser `dataset/`, que si es sede duradera. **Traigo la pregunta de sede medida, no resuelta.**

**Y LA SEGUNDA MITAD DE LA FRASE NO LA JUZGO:** *el quinto del capitulo entero* exige ordenar
los `44` tramos, y esa tabla vive en el fichero retirado. **A verificar en mi turno normal**,
igual que el *puesto `36` de `44`* que declara `llevar_inventario_proyectos_discrecionales`.

---

## 48.6. EL CINCO DE LOS CINCO INGENIEROS: UN MOTIVO QUE EL LIBRO DESMIENTE

**LA FICHA DE `dimensionar_numero_subordinados_medio_dia_semanal` ESCRIBE:**

> *`L299` dice `So the plant manager will actually have six direct reports: five engineers and
> the manufacturing manager`, pero ese cinco sale del dibujo que el libro pone debajo (`the
> arrangement, shown below`) y el dibujo NO esta en el fichero de texto. Un numero que solo se
> sostiene en una figura que no tengo delante es media cifra, y media cifra no se publica.*

**MI COMPROBACION:**

    $ grep -o "So the plant manager.\{0,150\}" fuentes/grove_high_output/cap_04.md
    So the plant manager will actually have six direct reports: five engineers and the manufacturing manager. The arrangement, shown below, does not have the engineers appear

(y la linea es la `L299`, la misma que la ficha cita:
`$ grep -n "five engineers" fuentes/grove_high_output/cap_04.md` responde `299:`)

**EL `cinco` Y EL `seis` ESTAN EN LA PROSA DEL RENGLON, NO EN EL DIBUJO.** `the arrangement,
shown below` es **la frase siguiente** y se refiere al esquema; los numeros los escribe el
texto.

**LO QUE ESTO ES Y LO QUE NO ES.** **La decision de no publicar el `cinco` no me parece mal**:
es prudente y no mete ninguna cifra falsa en la ficha. **Lo que esta mal es el motivo
escrito**, que afirma sobre el libro algo que el libro desmiente en la misma linea. Es prosa
dentro de un `resumen_teorico` y no una cifra publicada, asi que **lo registro aqui y no lo
cuento como caida en esta pagina**: la especie la adjudico en mi turno normal.

---

## 48.7. BARRIDO DE VECINOS SOBRE GRAFO MAS BANDEJAS (`D.38.4`)

**COMO LO CORRO.** La cifra que publico **es la de la casa**: sale de
`src.aduana.senal_similitud_texto` sobre `comun.texto_comparable`, la misma funcion que corre
la aduana. **No la reimplemento, no la aproximo y no recorto**: mido los `389` vecinos de cada
candidato **uno a uno**. La poblacion es `dataset/nodos.jsonl` mas las bandejas de
`cuarentena/` descartando `_insertados` y `_derivadas`, con el filtro canonico de mi
`ACTA 45` `45.5.a`, que es lo que `D.38.4` manda barrer.

    $ python .v48aud/03_barrido.py 0      (y 1, 2, 3, 4: un candidato por proceso)

**LA UNICA COSA QUE RECORTO DE ESTE PEGADO, Y LA DIGO:** las lineas de `poblacion barrida` y
de `umbral de la casa` **son identicas en las cinco salidas**, asi que las dejo una vez, en el
candidato `1`. **Ni una fila de vecino se recorta**, y las cinco salidas enteras estan en el
arbol.

    ==============================================================================
    CANDIDATO 1: buscar_regularidad_bloques_iguales_trabajo_mando   (9 pasos)
      poblacion barrida: 390 nodos (grafo + bandejas, filtro canonico)
      medidos al digito con src.aduana.senal_similitud_texto: 389 de 389; descartados: 0
      umbral de la casa (config/umbrales.json): 0.35
      LOS 8 VECINOS MAS PROXIMOS, LISTA ORDENADA ENTERA:
        0.3904  [bandeja/grove_high_output] llevar_inventario_proyectos_discrecionales  <-- nacido en esta vuelta
        0.3422  [bandeja/grove_high_output] dimensionar_numero_subordinados_medio_dia_semanal  <-- nacido en esta vuelta
        0.3379  [bandeja/grove_high_output] identificar_paso_limitante_jornada_desfases
        0.3332  [bandeja/grove_high_output] agrupar_tareas_semejantes_aprovechar_preparacion
        0.3254  [bandeja/grove_high_output] decir_no_trabajo_excede_capacidad  <-- nacido en esta vuelta
        0.3140  [bandeja/grove_high_output] usar_calendario_herramienta_planificacion_produccion  <-- nacido en esta vuelta
        0.3068  [bandeja/grove_high_output] delegar_tarea_base_comun_seguimiento
        0.2944  [bandeja/grove_high_output] transmitir_objetivos_prioridades_preferencias
      vecinos por encima del umbral 0.35: 1
    ==============================================================================
    CANDIDATO 2: decir_no_trabajo_excede_capacidad   (10 pasos)
      medidos al digito: 389 de 389; descartados: 0
      LOS 8 VECINOS MAS PROXIMOS, LISTA ORDENADA ENTERA:
        0.3759  [bandeja/grove_high_output] llevar_inventario_proyectos_discrecionales  <-- nacido en esta vuelta
        0.3655  [bandeja/grove_high_output] usar_calendario_herramienta_planificacion_produccion  <-- nacido en esta vuelta
        0.3641  [bandeja/grove_high_output] identificar_paso_limitante_jornada_desfases
        0.3544  [bandeja/grove_high_output] agrupar_tareas_semejantes_aprovechar_preparacion
        0.3276  [bandeja/grove_high_output] delegar_tarea_base_comun_seguimiento
        0.3254  [bandeja/grove_high_output] buscar_regularidad_bloques_iguales_trabajo_mando  <-- nacido en esta vuelta
        0.3087  [bandeja/grove_high_output] programar_visita_area_observar_despachar
        0.3064  [bandeja/grove_high_output] detectar_palanca_negativa_actividad_mando
      vecinos por encima del umbral 0.35: 4
    ==============================================================================
    CANDIDATO 3: dimensionar_numero_subordinados_medio_dia_semanal   (11 pasos)
      medidos al digito: 389 de 389; descartados: 0
      LOS 8 VECINOS MAS PROXIMOS, LISTA ORDENADA ENTERA:
        0.3349  [bandeja/grove_high_output] buscar_regularidad_bloques_iguales_trabajo_mando  <-- nacido en esta vuelta
        0.3268  [bandeja/grove_high_output] llevar_inventario_proyectos_discrecionales  <-- nacido en esta vuelta
        0.2899  [bandeja/grove_high_output] supervisar_tarea_delegada_etapa_menor_valor
        0.2746  [bandeja/grove_high_output] supervisar_decision_delegada_preguntas_concretas
        0.2695  [bandeja/grove_high_output] agrupar_tareas_semejantes_aprovechar_preparacion
        0.2653  [bandeja/grove_high_output] decidir_aceptar_rechazar_material_defectuoso
        0.2653  [bandeja/grove_high_output] decir_no_trabajo_excede_capacidad  <-- nacido en esta vuelta
        0.2608  [bandeja/grove_high_output] delegar_tarea_base_comun_seguimiento
      vecinos por encima del umbral 0.35: 0
    ==============================================================================
    CANDIDATO 4: llevar_inventario_proyectos_discrecionales   (5 pasos)
      medidos al digito: 389 de 389; descartados: 0
      LOS 8 VECINOS MAS PROXIMOS, LISTA ORDENADA ENTERA:
        0.3986  [bandeja/grove_high_output] buscar_regularidad_bloques_iguales_trabajo_mando  <-- nacido en esta vuelta
        0.3935  [bandeja/grove_high_output] identificar_paso_limitante_jornada_desfases
        0.3772  [bandeja/grove_high_output] decir_no_trabajo_excede_capacidad  <-- nacido en esta vuelta
        0.3680  [bandeja/grove_high_output] agrupar_tareas_semejantes_aprovechar_preparacion
        0.3283  [bandeja/grove_high_output] dimensionar_numero_subordinados_medio_dia_semanal  <-- nacido en esta vuelta
        0.3239  [bandeja/grove_high_output] delegar_tarea_base_comun_seguimiento
        0.3145  [bandeja/grove_high_output] archivar_indicadores_resolver_problemas
        0.3100  [bandeja/grove_high_output] transmitir_objetivos_prioridades_preferencias
      vecinos por encima del umbral 0.35: 4
    ==============================================================================
    CANDIDATO 5: usar_calendario_herramienta_planificacion_produccion   (7 pasos)
      medidos al digito: 389 de 389; descartados: 0
      LOS 8 VECINOS MAS PROXIMOS, LISTA ORDENADA ENTERA:
        0.3712  [bandeja/grove_high_output] decir_no_trabajo_excede_capacidad  <-- nacido en esta vuelta
        0.3264  [bandeja/grove_high_output] buscar_regularidad_bloques_iguales_trabajo_mando  <-- nacido en esta vuelta
        0.3219  [bandeja/grove_high_output] reunir_informacion_gerencial_vias_variadas
        0.3121  [bandeja/grove_high_output] identificar_paso_limitante_jornada_desfases
        0.3097  [bandeja/grove_high_output] transmitir_objetivos_prioridades_preferencias
        0.3081  [bandeja/grove_high_output] escalonar_fuentes_informacion_gerencial
        0.2887  [bandeja/grove_high_output] dimensionar_plantilla_administrativa_pronostico
        0.2879  [bandeja/grove_high_output] agrupar_tareas_semejantes_aprovechar_preparacion
      vecinos por encima del umbral 0.35: 1

(las cinco salidas enteras, sin recortar la cabecera de ninguna, estan en
`.v48aud/03_barrido_c0.out` a `.v48aud/03_barrido_c4.out`)

### 48.7.a. LO QUE LEO EN ESAS CINCO LISTAS

**LOS `40` VECINOS MAS PROXIMOS DE LOS CINCO CANDIDATOS ESTAN LOS `40` EN LA BANDEJA, Y
NINGUNO EN EL GRAFO.** La lista ordenada entera que lo sostiene es la de arriba, y la cuenta
sale de contarla, no de mirarla:

    $ sh .v48aud/20_sede_de_los_vecinos.sh
    filas de vecino publicadas en total : 40
    de ellas en [grafo]                 : 0
    de ellas en [bandeja/...]           : 40
    medidas por encima del umbral 0.35  : 10

El grafo, con sus `346` nodos, no coloca ni uno. **LECTURA:** este libro se esta midiendo
contra si mismo, que es lo
que cabe esperar de un lote que no ha insertado nada todavia, **y es la razon exacta por la
que `D.38.4` manda barrer bandejas y no solo grafo**: un barrido de solo grafo habria dado
cero vecinos en los cinco candidatos y habria parecido limpio.

**POR ENCIMA DEL UMBRAL `0.35` SALEN `10` MEDIDAS**, que son **`7` pares distintos** al quitar
los que aparecen en las dos listas:

| par | el digito en los dos sentidos | mi clase con la vara `6.1` |
|---|---|---|
| `llevar_inventario` con `buscar_regularidad` | `0.3904` / `0.3986` | **CONTINUA.** Uno llena un inventario de proyectos que no urgen, el otro alisa la carga y coordina bloques. Cero pasos comunes |
| `llevar_inventario` con `identificar_paso_limitante` | `0.3935` / `0.4010` | **CONTINUA.** Alli se busca el paso inamovible, aqui se prepara el material con el que se rellena alrededor |
| `llevar_inventario` con `decir_no` | `0.3759` / `0.3772` | **CONTINUA.** Los dos son principios de produccion de la misma serie y de objeto distinto: el inventario contra la capacidad |
| `llevar_inventario` con `agrupar_tareas` | `0.3680` / `0.3665` | **CONTINUA.** Agrupar por preparacion no es llevar inventario de proyectos |
| `decir_no` con `usar_calendario` | `0.3655` / `0.3712` | **FRONTERA DECLARADA.** Las dos responsabilidades numeradas de `L279`, con `L281` a una y `L283` mas `L285` a la otra |
| `decir_no` con `identificar_paso_limitante` | `0.3641` / `0.3693` | **CONTINUA.** Rechazar de salida no es encontrar el paso limitante |
| `decir_no` con `agrupar_tareas` | `0.3544` / `0.3578` | **CONTINUA.** Cero pasos comunes |

**`0` DUPLICADOS EN LOS SIETE PARES.** Y lo adjudico **leyendo los pasos de los dos lados**,
no por el digito: `D.19` dice que **una discrepancia nunca se adjudica citando una senial**, y
la senial aqui solo me dijo donde mirar.

### 48.7.b. LA SENIAL DE LA CASA NO ES SIMETRICA, Y LO COMPRUEBO ANTES DE ESCRIBIR NINGUN *EL MAS PROXIMO*

    $ python .v48aud/19_senial_no_es_simetrica.py
    los 7 pares distintos que mi barrido deja por encima del umbral 0.35, medidos en los DOS sentidos:
       0.3904  contra  0.3986   (-0.0082)   buscar_regularidad_bloques_iguales  <->  llevar_inventario_proyectos_discre
       0.3655  contra  0.3712   (-0.0057)   decir_no_trabajo_excede_capacidad  <->  usar_calendario_herramienta_planif
       0.3759  contra  0.3772   (-0.0014)   decir_no_trabajo_excede_capacidad  <->  llevar_inventario_proyectos_discre
       0.3641  contra  0.3693   (-0.0051)   decir_no_trabajo_excede_capacidad  <->  identificar_paso_limitante_jornada
       0.3544  contra  0.3578   (-0.0035)   decir_no_trabajo_excede_capacidad  <->  agrupar_tareas_semejantes_aprovech
       0.3935  contra  0.4010   (-0.0075)   llevar_inventario_proyectos_discre  <->  identificar_paso_limitante_jornada
       0.3680  contra  0.3665   (+0.0014)   llevar_inventario_proyectos_discre  <->  agrupar_tareas_semejantes_aprovech

    pares en los que el digito cambia al invertir el orden: 7 de 7

**Y NO ES UN DETALLE DE ADORNO: EN ESTA TANDA CAMBIA UN SUPERLATIVO.** El vecino mas proximo
de `llevar_inventario_proyectos_discrecionales` **depende del sentido en que se mida**:

| sentido | primero | segundo |
|---|---|---|
| midiendo desde `llevar_inventario` | `buscar_regularidad` **`0.3986`** | `identificar_paso_limitante` `0.3935` |
| midiendo desde el otro lado | `identificar_paso_limitante` **`0.4010`** | `buscar_regularidad` `0.3904` |

**Los dos primeros puestos se intercambian.** Por eso **no escribo *el vecino mas proximo de
llevar_inventario es X* en ninguna parte de esta pagina**: escribo la lista ordenada con su
sentido declarado, que es lo que mi `HEREDADO 1` me obliga a hacer y lo que la caida que
cargue en `46.6` fue exactamente.

### 48.7.c. LO QUE MI CIFRA DE COLA **NO** ES, Y HAY QUE DECIRLO ANTES DE COMPARARLA

Mi barrido mide **la poblacion final**, con los cinco candidatos ya escritos. La aduana del
extractor corre **en el mismo acto en que se escribe cada candidato** (`EXTRACTOR.md` `16`),
asi que **su poblacion crece a lo largo de la tanda**: su candidato `1` no pudo ver a los
cuatro que aun no existian. **Mis `7` pares y los suyos, sean los que sean, no son la misma
medida**, y si no cuadran **eso no es por si solo una discrepancia**. Lo digo aqui, con el
reporte todavia sin abrir, para no poder acomodarlo despues.

---

## 48.8. LAS SEDES DE DATO, Y LA PUERTA QUE DECIDE SI SE INSERTA

**EL GATE, CORRIDO POR MI EN ESTA FASE:**

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

**LAS SEDES DE DATO NO SE HAN MOVIDO EN ESTA VUELTA**, comprobado por diferencia y no
supuesto:

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl

    $ git diff --stat HEAD~1 HEAD -- dataset/ bitacora/ config/ censos/
    (sin salida = la vuelta 48 no movio ni una linea de esas cuatro sedes)

**LA PUERTA `D.39`, MEDIDA Y NO SUPUESTA.** Si `grove_high_output` no esta declarado cerrado
en extraccion, sus candidatos esperan en bandeja y **cero inserciones es lo correcto**:

    $ python .v48aud/10_puerta.py
    cerrados_en_extraccion, LISTA ENTERA (3):
       smart_who                      cita: ACTA 8 seccion 10
       zhuo_manager                   cita: ACTA 13 seccion 8.1
       scott_radical_candor           cita: ACTA 24

    grove_high_output esta en cerrados_en_extraccion: False

**LECTURA:** la puerta esta cerrada para este libro, asi que **una vuelta que no inserta nada
no esta fallando: esta cumpliendo `D.39`.** Lo mido yo porque es la clase de cosa que se da
por sabida y luego resulta que cambio.

**Y DE AHI SALE UNA CONSECUENCIA QUE DIGO AHORA PARA NO TENER QUE INVENTARLA DESPUES:** si
`bitacora/VEREDICTOS.jsonl` no se ha movido (`740` contra `740`, por diferencia), **esta tanda
no emitio ni un veredicto**, y por tanto **no hay poblacion de `SANO` que muestrear**. La
muestra pineada de `AUDITOR_FORJA.md` `7` **no se inventa donde no hay poblacion**, que es lo
que esa misma seccion manda decir con su cifra.

**EL TABLERO (`D.49`), LEIDO EN ESTA APERTURA:**

    $ python forja.py tablero | grep -E "grove_high_output |CON DUEÑO|MUNDO 11|COLA DE DOCTRINA"
      1    7    grove_high_output              COSECHADO              NINGUNO                 41  cap_04
      libros CON DUEÑO ahora mismo: 0
      MUNDO 11: faltan 3 de 3 libros del corte (grove_high_output, gerber_emyth, marquet_turn_the_ship)
      COLA DE DOCTRINA (D.56): 11 pregunta(s), 0 bloquea(n)

**Las `41` fichas en bandeja que el tablero cuenta son las que hay en el arbol**, y las `5` de
esta vuelta estan dentro: `36` mas `5` igual a `41`.

**CUANTO LLEVA `cap_04`, CONTADO POR MI Y NO COPIADO:**

    $ python .v48aud/18_nodos_cap04.py | head -1
    nodos que dicen salir de cap_04, LISTA ENTERA (19):
    $ python .v48aud/18_nodos_cap04.py | tail -1
    nacidos en esta vuelta: 5   ya estaban: 14

La lista entera de las `19` filas, con su sede y con las `5` de esta vuelta marcadas, esta en
`.v48aud/18_nodos_cap04.out`.

**LECTURA:** `19` nodos de `cap_04` viven hoy, **los `19` en bandeja y ninguno en el grafo**,
que es lo que la puerta `D.39` cerrada obliga. Los `14` anteriores son el denominador de toda
cuenta de fidelidad que hable del capitulo entero, y **ese `14` lo he contado yo**.

**LAS ARISTAS QUE LAS CINCO FICHAS DECLARAN POR LECTURA APUNTAN A IDS QUE EXISTEN**,
comprobado contra la poblacion real de hoy y no contra una lista:

    $ python .v48aud/06_aristas_citadas.py | tail -2
    ids nombrados que no existen en ninguna sede: 0
    ids nombrados en total por las cinco fichas: 18

**LECTURA:** `18` ids nombrados en las cinco fichas, **los `18` vivos**, `0` colgados. Es la
averia que la vuelta `47` dejo abierta (una arista escrita hacia un id que aun no existia), y
**en esta tanda no se repite**.

---

## 48.9. LA MEDIDA DE FORMA, REGISTRADA Y NO ADJUDICADA (`D.56`)

En `46.7` registre que `13` de los `45` pasos de la tanda `47` abrian **declarando** en vez de
ejecutando. La repito con **el mismo criterio, letra por letra**, porque cambiar el criterio y
comparar seria trampa mia:

    $ python .v48aud/16_forma_pasos_mismo_criterio.py | grep -E "^== |ABREN declarando"
    == tanda de la vuelta 48 : 42 pasos
       pasos que ABREN declarando y no ejecutando: 10 de 42 = 23.8 por ciento
    == tanda de la vuelta 47 : 45 pasos
       pasos que ABREN declarando y no ejecutando: 13 de 45 = 28.9 por ciento
    == tanda de la vuelta 46 : 50 pasos
       pasos que ABREN declarando y no ejecutando: 12 de 50 = 24.0 por ciento

**LECTURA:** la proporcion **baja** respecto a la vuelta `47`. **`D.56` congela la doctrina,
asi que esto se registra y no abre nada**, igual que en `46.7`.

**Y ME CAZO A MI MISMO UNA:** mi primer instrumento de esta fase
(`.v48aud/15_forma_pasos.py`) uso una lista de verbos **mas ancha** que la de `.v47aud` y daba
`14 de 42`, que habria parecido una **subida**. **La cifra que publico es la del criterio
comparable**, y dejo el primer instrumento en el arbol para que se vea la diferencia. Volver a
correr, y no releer, es lo que me lo ha evitado.

---

## 48.10. LO QUE LLEVO A MI TURNO NORMAL, EN ORDEN

| # | lo que traigo medido de esta fase | que busco en el reporte |
|---|---|---|
| **1** | **`L287` (`132` palabras) no lo cita ningun nodo de ninguna sede**, y `L289` (`101`) si tiene nodo en esta tanda | si la frontera de la vuelta `46` le adjudico `0` nodos **y con que motivo escrito** |
| **2** | **`P34` igual a `469` palabras contra `P38` igual a `396`**, con la lista entera de los cuatro tramos | si el superlativo esta tambien en `REPORTE.md` o solo en la ficha. **De eso depende la sede, y de la sede la especie** |
| **3** | el `cinco` de los cinco ingenieros **esta en la prosa de `L299`**, no en el dibujo | si el motivo falso viaja tambien al reporte |
| **4** | **`0` PUENTE de `42` pasos**, contados y leidos por mi | si su denominador es el mismo `42`, y si su desglose por capitulo existe (`8.3`: sin desglose, caida de `REPORTE`) |
| **5** | **`5` de `5` son nodo, `0` duplicados, `4` proximidades CONTINUA** | cuales marco el como discutibles **antes** de saber si acertaba (`5.1`) |
| **6** | `0` aristas colgadas de `18` ids nombrados | si declara esas mismas `18` |
| **7** | `gate` verde, `346` nodos, `740` veredictos, `0` lineas movidas en las sedes de dato | si su cierre dice lo mismo |
| **8** | **`10` medidas por encima del umbral, que son `7` pares distintos**, con la senial de la casa medida en los dos sentidos y **asimetrica en los `7`** | cuantos pares de cola declara. **Y si los numeros no cuadran, primero miro si es por la poblacion creciente de `48.7.c`, no si es por una discrepancia** |
| **9** | los `40` vecinos mas proximos de los cinco **estan los `40` en bandeja y `0` en el grafo** | si su informe vio la misma poblacion (`D.38.5`) |

**NO COMMITEO NADA.** El arnes sella esta pagina y la commitea el. **Y no la vuelvo a tocar
despues**, porque el sello se verifica al terminar mi turno.
