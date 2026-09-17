# APERTURA CIEGA del auditor, frente `grove_high_output`

**Abro a las `05:43` del 17 sep 2026** y cierro esta escritura a la hora que firma
la ultima seccion. **Mientras escribo corren otros frentes en el mismo arbol**, asi
que **toda cifra de estado de este fichero lleva la hora a la que la medi**
(`HEREDADO 2`), y la prueba de que hay mas de un escritor esta pegada en `1.2`.

**LO QUE NO HE ABIERTO, Y LO DIGO ANTES DE NADA.** No he abierto
`docs/loop/REPORTE.md`, ni `docs/loop/loop.log`, ni `docs/loop/ultimo_extractor.json`,
ni `docs/loop/ultimo_auditor.json`, **ni los he recuperado de git ni por ninguna
otra via**. No estan en el arbol y los dejo donde estan. **Si he abierto
`docs/loop/ACTA_AUDITOR.md`**, que es obra mia y no del extractor, y no es ninguno
de los cuatro que `D.34.2` retira.

---

## 0. LAS CUATRO DECLARACIONES DE HERENCIA (`D.40`)

    ACTA ANTERIOR LEIDA: dea8d91127926fcadf2273a0af887e8b58249a86
    HEREDADO 1: CUMPLIDO
    HEREDADO 2: CUMPLIDO
    HEREDADO 3: CUMPLIDO
    HEREDADO 4: CUMPLIDO

**Ninguna de las cuatro va como `NO APLICA`**, asi que ninguna necesita el motivo
escrito con su salida pegada que `D.40` ensanchada del 16 sep exige. **Aun asi las
cuatro llevan su instrumento debajo**, porque una declaracion de cumplimiento sin
nada corrido al lado vale lo mismo que el `NO APLICA` que la regla vino a cazar.

### 0.1. `HEREDADO 1`: la cifra de poblacion con la cita literal de su criterio

> **`HEREDADO 1`:** *UNA CIFRA DE POBLACION NO SE PUBLICA SIN LEER HASTA EL FINAL LA
> REGLA QUE LA DEFINE. Si cito una regla por su numero para justificar una
> poblacion, pego en la apertura la linea de esa regla que dice que entra y que no.*

**LA CAIDA QUE LO OBLIGO ES MIA:** mi apertura de la vuelta anterior publico `511`
donde la doctrina ponia `348`, y la diferencia son exactamente los `163` de
`cuarentena/ensayo_referencia_163/`, **que la regla excluye en su ultimo parrafo**.

**LA LINEA LITERAL DE `D.38.5` QUE DICE QUE ENTRA Y QUE NO**, copiada de
`docs/BANCO_DE_REGLAS.md`, seccion *Lo que entra en la poblacion, y el criterio NO
es una lista de carpetas*:

> **ENTRA EN LA POBLACION EL CANDIDATO CUYAS FUENTES ESTAN TODAS EN LA TABLA
> CANONICA VIGENTE.** Se descartan ademas `_insertados` (ya viven en el grafo,
> `D.31`) y `_derivadas`.

**Y LA LINEA QUE EXPLICA POR QUE `ensayo_referencia_163` NO ENTRA**, de la misma
regla y del mismo parrafo:

> `cuarentena/` tambien aloja `ensayo_referencia_163/`, que son **163 nodos de un
> catalogo de referencia ajeno** puestos ahi para calibrar la aduana. **Esos no
> esperan juicio: no van a entrar nunca en este grafo.**

**MI INSTRUMENTO APLICA ESE CRITERIO Y NO UNA LISTA DE CARPETAS**, medido a las
`05:43`:

    $ python .v3g/poblacion.py
    claves canonicas                      : 12
    nodos en dataset/nodos.jsonl          : 270
    ficheros .json bajo cuarentena/       : 264
      EXCLUIDO   163  fuente FUERA de la tabla canonica en cuarentena/ensayo_referencia_163
    candidatos de bandeja que ENTRAN      : 101
        bandeja grove_high_output          23
        bandeja marquet_turn_the_ship      3
        bandeja scott_radical_candor       75
    POBLACION DEL BARRIDO (grafo+bandejas): 371
       menos el propio candidato (ACTA 18): 370

**Y LA MAQUINA MIDE LO MISMO QUE YO**, que es lo que `D.38.5` prometio y lo que
convierte cualquier diferencia en discrepancia de verdad y no de metodo. Corrida a
las `05:46`, la aduana en seco publica su propia poblacion:

    $ python forja.py informe cuarentena/grove_high_output/revisar_tres_preguntas_valor_carrera.json
    poblacion del barrido       : 371   (270 del grafo mas 101 que esperan en bandejas)

**`371` contra `371`, y su reparto `270` mas `101` contra `270` mas `101`. Cuadra
al digito.**

### 0.2. `HEREDADO 2`: la hora pegada a cada cifra de estado

> **`HEREDADO 2`:** *TODA CIFRA DE ESTADO QUE PUBLIQUE LLEVA LA HORA A LA QUE LA
> MEDI, mientras corran frentes en paralelo.*

**La condicion se cumple: el arbol tiene mas de un escritor**, y la salida esta en
`1.2`. Cada cifra de estado de este fichero lleva su hora en la linea que la
introduce o en el `$ date` pegado encima de su comando.

### 0.3. `HEREDADO 3`: la clase escrita a fichero antes de destapar ninguna razon

> **`HEREDADO 3`:** *LA RELECTURA CIEGA DESTAPA UNA RAZON POR VEZ, Y DESPUES DE
> ESCRIBIR MI CLASE A FICHERO.*

**MI FICHERO DE CLASES ES `.v3g/mi_clase.tsv` Y SU HORA ES LAS `05:56`:**

    $ ls -la --time-style=+%H:%M .v3g/mi_clase.tsv
    -rw-r--r-- 1 AlexDesk 197609 1292 05:56 .v3g/mi_clase.tsv

**Y NO HE DESTAPADO NINGUNA RAZON, ni antes ni despues, porque este frente no ha
insertado nada y por tanto no hay ni una razon escrita que destapar.** La medida,
a las `05:52`:

    $ python -c "veredictos por libro"
    lineas de bitacora/VEREDICTOS.jsonl por clave:
      (sin campo libro)            396
    lineas que contienen la cadena grove: 0

**LECTURA:** las `396` lineas de la bitacora son del serial; **para
`grove_high_output` no hay ninguna**, que es lo coherente con `D.45` (este frente
extrae y no inserta). Asi que el remedio se cumple **por su forma** (clase a
fichero primero, a las `05:56`) y **su otra mitad no tiene poblacion esta vuelta**,
lo cual digo con su instrumento en vez de callarlo.

### 0.4. `HEREDADO 4`: ninguna constante tecleada en mis instrumentos

> **`HEREDADO 4`:** *UNA TABLA QUE PUBLICO COMO DE INSTRUMENTO NO LLEVA UNA
> CONSTANTE TECLEADA DENTRO, Y SI LA LLEVA LO DICE EN SU PRIMERA LINEA.*

**El barrido casa los ids contra el dato en vez de teclearlos**, medido a las
`05:53`:

    $ python .v3g/sin_ids_tecleados.py
    ids del grafo mas las bandejas, casados del dato: 534
    instrumentos de .v3g/ barridos              : 4
      censo_lote.py                      ids tecleados dentro: 0
      poblacion.py                       ids tecleados dentro: 0
      sin_ids_tecleados.py               ids tecleados dentro: 0
      volcar.py                          ids tecleados dentro: 0
    TOTAL DE IDS TECLEADOS EN MIS INSTRUMENTOS: 0

**LO QUE ESA CIFRA `534` MIDIO, y lo separo de la de `0.1` para que nadie las
confunda:** son los ids del grafo mas **todos** los ficheros de `cuarentena/` sin
descartar por fuente, que es la poblacion correcta **para este barrido** (busco
ids tecleados, no vecinos). **No es la poblacion del barrido de vecinos**, que es
`371` y lleva la exclusion de `ensayo_referencia_163` puesta.

**Y HAY UN INSTRUMENTO MIO QUE SI LLEVA CONSTANTES TECLEADAS DENTRO, Y LO DIGO EN
SU PRIMERA LINEA COMO LA REGLA MANDA:** `.v3g/mi_clase.tsv` lleva tecleados los
`23` ids del lote con **mi veredicto** al lado. **Lo tecleado ahi no es dato: son
mis clases**, que no existen en ningun fichero del que casarlas. **Los
denominadores de su tabla no se teclean**: `.v3g/cuentas_mi_clase.py` lee el numero
de pasos y el capitulo de cada candidato del propio JSON, y ademas comprueba que mi
lista y la bandeja coincidan candidato a candidato (`en la bandeja y SIN mi clase: 0`,
`con mi clase y NO en la bandeja: 0`).

**Y el barrido de estilo sobre mis instrumentos, a las `05:52`:**

    $ python forja.py guiones .v3g
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

---

## 1. QUE AUDITO Y QUE TENGO DELANTE

### 1.1. La vuelta que me toca, y el hueco que arrastro

**El ultimo commit del frente, a las `05:40` de hoy**, cierra la **vuelta 2 de
`grove_high_output`** sobre `cap_03`. Mi acta anterior, la `ACTA 31`, cubrio la
vuelta `32` del serial y **lo publicado de la vuelta 1 de este frente, que no
estaba cerrada y seguia escribiendo mientras yo firmaba**, y asi lo dice su propia
cabecera.

> **HAY HUECO Y LO DECLARO (seccion 1.0 del protocolo):** el CIERRE de la **vuelta
> 1** de este frente (`6933b64`, 16 sep `22:22`) **no lo cubre ninguna acta**, y la
> **vuelta 2** entera tampoco. **Esta apertura ciega clasifica las dos: los `8`
> candidatos de `cap_01` y `cap_02` y los `15` de `cap_03`, los `23` de la bandeja.**

### 1.2. Que el arbol tiene mas de un escritor, medido y no supuesto

    $ git log --all --since="2026-09-16 20:00" --pretty=format:"%h %ad %d %s" --date=format:"%d %b %H:%M" | head -25
    9044af7 17 Sep 05:40  (HEAD -> extraccion-grove_high_output, ...) VUELTA 2 grove_high_output CERRADA: cap_03 entero minado, 15 candidatos ...
    95794c6 17 Sep 01:57  VUELTA 2 grove_high_output TAREA 2: los 15 candidatos de cap_03 por la aduana EN SECO uno a uno ...
    836e301 17 Sep 01:20  (origin/extraccion-gerber_emyth, extraccion-gerber_emyth) ACTA G1 del frente gerber_emyth, vuelta 1: PARADA ...
    4c4a616 17 Sep 00:47  Apertura ciega de la vuelta 1, sellada antes de exponer el reporte
    f6005e4 16 Sep 23:50  (origin/extraccion-marquet_turn_the_ship, ...) ACTA M2 del frente marquet_turn_the_ship, VUELTA 1: PARADA ...
    a84b84e 16 Sep 23:40  VUELTA 2 grove_high_output, TAREAS 3 y 4: los 121 pasos de cap_03 releidos uno a uno ...
    ...
    17d673f 16 Sep 22:28  (extraccion-mundo-11) DICTAMEN: cuatro sesiones, tres paradas, y una sola causa en los frentes

**LECTURA:** en las ultimas siete horas han escrito **cuatro ramas distintas**
(`grove_high_output`, `gerber_emyth`, `marquet_turn_the_ship`, `mundo-11`). **La
condicion de `HEREDADO 2` se cumple y por eso pongo hora en todo.**

### 1.3. El estado del arbol al abrir, medido a las `05:43`

    $ wc -l dataset/nodos.jsonl
    270 dataset/nodos.jsonl
    $ wc -l bitacora/VEREDICTOS.jsonl
    396 bitacora/VEREDICTOS.jsonl
    $ wc -l config/pares_mutuos.jsonl
    1 config/pares_mutuos.jsonl

**Y el gate, corrido por mi y no copiado, a las `05:45`:**

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 270
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

**LECTURA:** `270` nodos en el grafo y `0` de ellos de este libro, porque este
frente no inserta (`D.45`). **Las `396` lineas de veredicto son todas del serial**,
y la medida esta en `0.3`.

### 1.4. El censo de la bandeja, medido a las `05:44`

    $ python .v3g/censo_lote.py cuarentena/grove_high_output
    candidatos en cuarentena/grove_high_output : 23
    id                                                   pasos prev  sig  dominio
    revisar_tres_preguntas_valor_carrera                     7    0    0  carrera_profesional
    clasificar_trabajo_proceso_montaje_prueba                7    0    0  produccion
    rehacer_flujo_paso_limitante_capacidad                   6    0    0  produccion
    equilibrar_capacidad_personal_inventario_plazo           8    0    0  produccion
    preferir_inspeccion_proceso_prueba_destructiva           6    0    0  produccion
    dimensionar_inventario_materia_prima_reposicion          7    0    0  produccion
    detectar_arreglar_fallo_etapa_menor_valor                6    0    0  produccion
    construir_flujo_produccion_paso_limitante               10    0    0  produccion
    elegir_cinco_indicadores_diarios_fabrica                10    0    0  produccion
    emparejar_indicadores_efecto_contraefecto                7    0    0  produccion
    elegir_indicador_salida_trabajo_administrativo           7    0    0  produccion
    representar_actividad_caja_negra_ventanas                9    0    0  produccion
    construir_indicador_linealidad_alerta_temprana           9    0    0  produccion
    construir_indicador_tendencia_patron                     6    0    0  produccion
    construir_grafico_escalonado_pronosticos                 8    0    0  produccion
    archivar_indicadores_resolver_problemas                  4    0    0  produccion
    elegir_fabricar_pedido_pronostico                        9    0    0  produccion
    casar_flujo_fabricacion_flujo_ventas                    12    0    0  produccion
    dimensionar_plantilla_administrativa_pronostico          7    0    0  produccion
    decidir_aceptar_rechazar_material_defectuoso             8    0    0  produccion
    elegir_inspeccion_barrera_monitorizacion                12    0    0  produccion
    variar_frecuencia_inspeccion_nivel_calidad               6    0    0  produccion
    simplificar_trabajo_reducir_numero_pasos                 7    0    0  produccion
    TOTAL PASOS EN LA BANDEJA: 178

**LECTURA:** `23` candidatos, `178` pasos, **`0` aristas cableadas en toda la
bandeja** (las columnas `prev` y `sig` estan a cero de arriba abajo), que es lo que
`D.45` manda en un frente que no inserta. **Dos dominios y los dos nuevos en esta
casa:** `carrera_profesional` con `1` nodo y `produccion` con `22`.

### 1.5. Los pasos por capitulo, leidos del dato y no del reporte, a las `05:53`

    $ python .v3g/pasos_por_capitulo.py
    PASOS ESCRITOS POR CAPITULO (solo los de unidad unica):
      cap_01  nodos  1  pasos   7
      cap_02  nodos  7  pasos  50
      cap_03  nodos 15  pasos 121
      TOTAL           nodos 23  pasos 178
    candidatos que citan mas de un cap_NN o ninguno: 0

**LECTURA, y es la que importa para la seccion 8 del protocolo:** el capitulo de
cada candidato **no lo he copiado de ningun sitio**: el instrumento lo casa contra
la ruta `fuentes/grove_high_output/cap_NN.md` que el propio `resumen_teorico`
declara, y **los `23` declaran uno y solo uno**. `cap_03` escribio `121` pasos
sobre `15` nodos.

---

## 2. MI CLASE, CANDIDATO POR CANDIDATO

**ESTA ES LA LECTURA QUE DESPUES VOY A COMPARAR CON LA DEL EXTRACTOR.** He leido
enteros `fuentes/grove_high_output/cap_01.md`, `cap_02.md` y `cap_03.md`, y he
abierto los `23` ficheros de la bandeja. **Cada fila dice mi clase y las lineas del
libro que la sostienen.**

**LAS TRES CLASES QUE USO:**

| clase | que significa |
|---|---|
| **`SOSTENIDO`** | leo el tramo y **veo el procedimiento**: el inventario de etapas, medios u objetos de trabajo es del libro, y los pasos lo transcriben |
| **`SOSTENIDO CON RESERVA`** | lo sostengo, **pero digo por donde se rompe** si otro lector aprieta |
| **`NO SOSTENIDO`** | no lo veo procedimiento, o veo gemelo |

### 2.1. `cap_01`, la Introduction. Un nodo de `56` lineas de cuerpo con texto

| # | candidato | lineas que lo sostienen | MI CLASE |
|---|---|---|---|
| 1 | `revisar_tres_preguntas_valor_carrera` | `cap_01` `L101` a `L107`, `193` palabras | **SOSTENIDO CON RESERVA** |

**LO QUE LEO.** `L101` dice que el autor no ofrece formula segura y que deja unas
preguntas, **y el libro pone las tres, numeradas `1`, `2` y `3`**, cada una con su
contenido propio: `L103` la del valor anadido, con su como (*looking for ways to
make things truly better in your department*) y su vara (*every hour of your day
should be spent increasing the output or the value of the output of the people whom
you are responsible for*); `L105` la de estar enchufado, con sus dos caras (*a node
connected to a network of plugged-in people* contra *floating by yourself*); `L107`
la de probar lo nuevo en persona. **Los `7` pasos salen de esas tres lineas y
ninguna de las tres queda sin usar.**

**MI RESERVA, y la marco antes de ver nada:** de toda la bandeja **este es el que
mas cerca esta de POSTURA**, porque lo que se ejecuta es un examen de uno mismo y
no un trabajo con entregable material. **Lo sostengo** porque la vara de `6.1` no
pide entregable material, pide que el inventario sea del libro, y aqui lo es al
digito; y porque `L103` trae **una unidad de medida escrita** (*cada hora de tu
dia*), que es lo que separa una pregunta con procedimiento de una exhortacion.

**Y DIGO QUE LA INTRODUCTION DE `56` LINEAS CON TEXTO DIERA `1` SOLO NODO ME PARECE
LA LECTURA CORRECTA**, no un lote corto. `L13` a `L99` son diagnostico
(globalizacion, el correo electronico, quien es un mando intermedio, las tres ideas
del libro) **sin un solo inventario de acciones**: son las lineas que `6.1` llama
*una advertencia es linea*.

### 2.2. `cap_02`, The Basics of Production. Siete nodos, `50` pasos

| # | candidato | lineas que lo sostienen | MI CLASE |
|---|---|---|---|
| 2 | `construir_flujo_produccion_paso_limitante` | `L15` a `L27`, `602` palabras | **SOSTENIDO** |
| 3 | `clasificar_trabajo_proceso_montaje_prueba` | `L37` a `L47`, `582` palabras | **SOSTENIDO** |
| 4 | `rehacer_flujo_paso_limitante_capacidad` | `L49` a `L55`, `231` palabras | **SOSTENIDO** |
| 5 | `equilibrar_capacidad_personal_inventario_plazo` | `L57` a `L61`, `365` palabras | **SOSTENIDO** |
| 6 | `preferir_inspeccion_proceso_prueba_destructiva` | `L67`, `202` palabras | **SOSTENIDO** |
| 7 | `dimensionar_inventario_materia_prima_reposicion` | `L69`, `237` palabras | **SOSTENIDO** |
| 8 | `detectar_arreglar_fallo_etapa_menor_valor` | `L71` a `L75`, `263` palabras | **SOSTENIDO** |

**LO QUE LEO, tramo a tramo, y por que en los siete veo procedimiento:**

- **`L15` a `L27`.** El libro **numera el metodo en imperativo suyo**: *The first
  thing we must do is to pin down the step in the flow that will determine the
  overall shape of our operation*; *To work back from the time of delivery, you
  will need to calculate the time required*; *First you must allow time to assemble
  the items on a tray*; *Next you must get the toast*; *Using the egg time as your
  base, you must allow yourself time*. `L27` cierra con el criterio entero y con
  sus cuatro varas (*the longest (or most difficult, or most sensitive, or most
  expensive) step*), que es el paso `10`. **Inventario de ETAPAS del libro.**
- **`L37` a `L47`.** `L39` nombra **los tres tipos con su definicion pegada**
  (*process manufacturing*, *assembly*, *test*). `L45` trae la secuencia completa
  del compilador: prueba unitaria, vuelta a proceso para *rework*, montaje cuando
  todas pasan, y *system test* antes de enviar. **Los pasos `4` a `7` son esa
  secuencia y no un adorno del caso**, porque `L47` cierra diciendo que los cuatro
  trabajos distintos tienen un flujo basicamente similar.
- **`L49` a `L55`.** Es el mismo objeto que el nodo `2` **pero al reves**: alli se
  construye, aqui se rehace. `L51` lo escribe: *limited toaster capacity means you
  have to redo your flow around the new limiting step. The egg still determines the
  overall quality of the breakfast, but your time offsets must be altered*. **Esa
  frase es la frontera entera**, y la digo yo en `4.1`.
- **`L57` a `L61`.** **El tramo mas rico de la unidad.** Cuatro salidas nombradas
  una a una, **cada una con su coste escrito** (especializar personal y su
  *immense amount of overhead*; pedir ayuda al de al lado y su *less predictable*;
  otro tostador y su *expensive addition of capital equipment*; inventario continuo
  y su *waste*). `L61` pone la vara: *the best delivery time and product quality at
  the lowest possible cost*.
- **`L67`.** Una sola linea de `202` palabras que trae **dos medios con su
  mecanica** (*functional test* con su coste, tirar la unidad probada;
  *in-process inspection* con su termometro y su aviso al variar un grado o dos) y
  **cierra con el criterio en imperativo del libro**: *whenever possible, you should
  choose in-process tests over those that destroy product*.
- **`L69`.** Trae **la formula escrita**: *you should have enough to cover your
  consumption rate for the length of time it takes to replace your raw material*, y
  las tres preguntas de la oportunidad en riesgo. **No es un adjetivo de
  adecuacion**, es una regla de dimensionamiento.
- **`L71` a `L75`.** `L75` escribe la regla como regla (*A common rule we should
  always try to heed is to detect and fix any problem in a production process at the
  lowest-value stage possible*) y **la aplica tres veces nombrando en cada una las
  dos etapas que compara**.

### 2.3. `cap_03`, Managing the Breakfast Factory. Quince nodos, `121` pasos

| # | candidato | lineas que lo sostienen | MI CLASE |
|---|---|---|---|
| 9 | `elegir_cinco_indicadores_diarios_fabrica` | `L15` a `L29`, `560` palabras | **SOSTENIDO** |
| 10 | `emparejar_indicadores_efecto_contraefecto` | `L31` a `L33`, `208` palabras | **SOSTENIDO** |
| 11 | `elegir_indicador_salida_trabajo_administrativo` | `L35` a `L37` mas la tabla `L39` a `L67` | **SOSTENIDO** |
| 12 | `representar_actividad_caja_negra_ventanas` | `L71` a `L79`, `348` palabras | **SOSTENIDO CON RESERVA** |
| 13 | `construir_indicador_linealidad_alerta_temprana` | `L83` a `L87`, `352` palabras | **SOSTENIDO** |
| 14 | `construir_indicador_tendencia_patron` | `L89`, `94` palabras | **SOSTENIDO** |
| 15 | `construir_grafico_escalonado_pronosticos` | `L91` a `L97`, `306` palabras | **SOSTENIDO** |
| 16 | `archivar_indicadores_resolver_problemas` | `L99`, `88` palabras | **SOSTENIDO CON RESERVA** |
| 17 | `elegir_fabricar_pedido_pronostico` | `L101` a `L109`, `425` palabras | **SOSTENIDO** |
| 18 | `casar_flujo_fabricacion_flujo_ventas` | `L111` a `L121`, `453` palabras | **SOSTENIDO** |
| 19 | `dimensionar_plantilla_administrativa_pronostico` | `L123` a `L125`, `228` palabras | **SOSTENIDO** |
| 20 | `decidir_aceptar_rechazar_material_defectuoso` | `L135` a `L137`, `242` palabras | **SOSTENIDO** |
| 21 | `elegir_inspeccion_barrera_monitorizacion` | `L139` a `L141`, `356` palabras | **SOSTENIDO** |
| 22 | `variar_frecuencia_inspeccion_nivel_calidad` | `L143` a `L145`, `157` palabras | **SOSTENIDO** |
| 23 | `simplificar_trabajo_reducir_numero_pasos` | `L169` a `L173`, `382` palabras | **SOSTENIDO** |

**LO QUE LEO, y las lineas que lo sostienen:**

- **`9`, los cinco indicadores (`L15` a `L29`).** `L17` pregunta cuales serian los
  cinco datos que miraria cada dia al llegar al despacho, **y el libro pone los
  cinco, uno por linea**: pronostico y desviacion (`L19`), inventario de materia
  prima con sus dos salidas (`L21`), estado de los equipos (`L23`), gente
  disponible con sus dos salidas (`L25`), indicador de calidad con su registro de
  quejas *maintained by the cashier* (`L27`). `L29` cierra con el ritmo de la
  mirada y su para que. **Es un caso de fabrica de desayunos, si, pero los cinco
  son categorias y no productos**, y esa es la razon por la que lo sostengo.
- **`10`, el par efecto y contraefecto (`L31` a `L33`).** La advertencia ocupa una
  frase (*you should guard against overreacting*) **y el resto es el remedio con
  sus piezas nombradas**: *pairing indicators, so that together both effect and
  counter-effect are measured*, encarnado en *inventory levels* contra *the
  incidence of shortages*. Una advertencia es linea, **pero esto trae el medio**.
- **`11`, el indicador administrativo (`L35` a `L67`).** Dos varas con nombre del
  libro (*the first rule*, *the second criterion*), **seis funciones con su
  indicador leidas fila a fila de la tabla**, y **dos parejas de calidad
  desarrolladas**, una de ellas con evaluador nombrado. **El corte que junta la
  tabla con su parrafo me parece el correcto:** la tabla ES el inventario del
  parrafo, y sacarla aparte fabricaria el gemelo de su donante.
- **`12`, la caja negra (`L71` a `L79`).** **MI RESERVA, y es la mas gorda de la
  bandeja:** un lector estricto dira que esto es un CONCEPTO con ejemplos.
  **Lo sostengo** porque el libro manda hacer (*we can represent any activity that
  resembles a production process*; *we can draw a black box*; *cutting some windows
  in our box*), porque **repite el inventario entero sobre tres actividades que no
  son la fabrica**, nombrando en cada una cual es la entrada, cual la salida y cual
  el trabajo, y porque el entregable es material. **Si cae, es el primero de mi cola
  de relectura.**
- **`13`, la linealidad (`L83` a `L87`).** Instrumento con nombre propio, sus dos
  ejes, su recta ideal, su lectura a media carrera con su aritmetica, **y repetido
  entero sobre una segunda poblacion** (la unidad de fabricacion dentro del mes).
- **`14`, la tendencia (`L89`, `94` palabras).** El tramo mas delgado que da nodo
  junto con el `16`. **Lo sostengo** porque el libro nombra el instrumento, dice
  que se pone dentro con tres salidas distintas, nombra **las dos varas** (*against
  time* y *against some standard or expected level*) y las dos cosas que provoca.
- **`15`, el grafico escalonado (`L91` a `L97`).** Su periodo (*The chart is updated
  monthly*) **lo pone el libro con esas palabras**, y por eso no es puente. El pie
  de figura de `L95` da la marca del dato real.
- **`16`, el archivo de indicadores (`L99`, `88` palabras).** **MI RESERVA:** es el
  nodo mas delgado de la bandeja, y **sus pasos `1` y `2` nombran el mismo objeto
  dos veces** (mantener un archivo, y que ese archivo sea un banco de informacion);
  en una relectura apretada los fundiria en uno y el nodo se quedaria en tres pasos.
  **Lo sostengo como nodo aparte** porque su objeto y su disparador son distintos
  de los del `9`: alli se eligen los cinco que se miran cada dia, aqui se guarda la
  serie de todos ellos, y el disparador es *If something goes wrong*.
- **`17`, pedido contra pronostico (`L101` a `L109`).** El libro dice **cuantas
  vias hay** (*There are two ways to control the output of any factory*), las nombra
  las dos, pone la mecanica de cada una y el precio de la segunda.
- **`18`, casar los dos flujos (`L111` a `L121`).** `12` pasos, el tramo mas largo.
  **Lo sostengo como un solo nodo** porque el propio libro encadena la holgura a la
  falta de encaje con su *because neither the sales flow nor the manufacturing flow
  is completely predictable*.
- **`19`, la plantilla administrativa (`L123` a `L125`).** Cadena entera de medios
  nombrados: indicadores elegidos y vigilados, patrones de hecho deducidos de los
  datos de tendencia, pronostico de personas, reasignacion, y la plantilla casada
  con el crecimiento o el descenso previsto.
- **`20`, aceptar o rechazar material (`L135` a `L137`).** Dos salidas nombradas,
  la consecuencia medible de la segunda, el termino de comparacion, **quien decide
  y de que tres areas sale ese quien**, y la excepcion de fiabilidad con su nombre.
- **`21`, barrera contra monitorizacion (`L139` a `L141`).** La mecanica **completa
  de las dos tecnicas**, el intercambio por los dos lados y una regla de pulgar
  escrita por el libro.
- **`22`, la inspeccion variable (`L143` a `L145`).** La frecuencia se mueve **en
  los dos sentidos con su disparador en cada uno**, y la subida tiene condicion de
  parada. **Aqui esta mi unico PUENTE, y va en `3.2`.**
- **`23`, simplificar el trabajo (`L169` a `L173`).** **El tramo mas claro de las
  tres unidades:** el libro numera el procedimiento el mismo (*you first need to*,
  *Second*, *Third*).

### 2.4. El recuento de mi propia lectura, a las `05:57`

    $ python .v3g/cuentas_mi_clase.py
    candidatos en la bandeja                 : 23
    candidatos con clase escrita por mi      : 23
    en la bandeja y SIN mi clase             : 0
    con mi clase y NO en la bandeja          : 0

      SOSTENIDO                20
      SOSTENIDO_CON_RESERVA    3

**LECTURA:** **`0` candidatos `NO SOSTENIDO`.** Leo procedimiento en los `23`, y en
`3` de ellos digo por donde se rompen.

---

## 3. MI RELECTURA DE FIDELIDAD `D.30`, PASO A PASO

**HE RELEIDO LOS `178` PASOS CONTRA SU LINEA.** No he tomado por buena ninguna
derivacion declarada por el candidato: he abierto la linea del libro y he mirado si
el paso estaba dentro.

### 3.1. La cifra, con su instrumento al lado

    $ python .v3g/cuentas_mi_clase.py
    PASOS INVENTADOS POR CAPITULO, SEGUN MI PROPIA RELECTURA CIEGA
      cap       nodos    pasos   PUENTE por ciento
      cap_01        1        7        0      0.00
      cap_02        7       50        0      0.00
      cap_03       15      121        1      0.83
      TOTAL        23      178        1      0.56

**LECTURA:** por la seccion `8.1` del protocolo, **el peor capitulo de este lote
esta en `0,83` por ciento**, muy por debajo del tope de `10`. **La escalada se
decide sobre el peor capitulo y no sobre el promedio**, y el peor tampoco lo toca.

### 3.2. El unico paso que leo PUENTE, y donde

**`variar_frecuencia_inspeccion_nivel_calidad`, paso `6`.** El paso dice:

> *Desconfia de tu propia costumbre antes de descartarlo, porque este metodo casi
> no se usa ni siquiera en la fabricacion corriente, y la razon probable es que
> somos animales de costumbres y seguimos haciendo las cosas como las hemos hecho
> siempre, sea de una semana a otra o de un ano a otro.*

**La linea del libro, `cap_03` `L143`, reabierta y no citada de memoria:**

> *Yet this approach is not used very often, even in widget manufacturing. Why not?
> Probably because we are creatures of habit and keep doing things the way we always
> have, whether it be from week to week or year to year.*

**LO QUE VEO.** **Todo lo que va detras del `porque` es transcripcion literal.** Lo
que no esta en el libro es **la cabeza del paso**: *desconfia de tu propia costumbre
antes de descartarlo*. **El libro diagnostica por que el metodo se usa poco; no le
encarga al lector que desconfie de su costumbre.** Convertir una afirmacion del
libro en una comprobacion del lector **es la especie del acto**, la cuarta, la que
no esta en la tabla de las tres de `D.30`, **y es exactamente la misma que este
mismo lote corrigio en `construir_flujo_produccion_paso_limitante` paso `6`**.

**NO LO CARGO COMO CAIDA DE CLASE NI DE CIFRA, y digo por que:** `D.30` pone los
puentes en la metrica de volumen de la seccion `8`, **que no entra en la metrica de
credito** (`8.4`: *un puente encontrado y corregido es la regla funcionando*). **Lo
publico como lo que es: `1` de `178`, `0,56` por ciento**, y lo dejo escrito para
que la vuelta que inserte este nodo lo corrija antes de la aduana.

### 3.3. El paso que me hizo dudar y NO cargo como puente

**`construir_indicador_linealidad_alerta_temprana`, paso `9`.** Dice *trata al
mando de esa unidad como a alguien que probablemente no esta usando bien ni la
gente ni el equipo, y arregla la situacion*. **La linea, `cap_03` `L87`:** *the
manager of the unit is probably not using manpower and equipment efficiently. And
if the situation is not remedied, one minor breakdown toward month end could cause
the unit to miss its monthly output goal entirely.*

**Es la misma figura que `3.2` pero mas floja**, porque *if the situation is not
remedied* **presupone que remediarla es la accion**, y el *probably* lo trae el
libro. **Lo dejo como TRANSCRIPCION y lo marco aqui**, que es lo que hace falta
para que el siguiente lector lo pueda tumbar sin tener que encontrarlo.

---

## 4. MI LECTURA DE LA FRONTERA: QUE TRAMOS LEO CON CERO NODOS

**LA MEDIDA PRIMERO, Y DESPUES MI LECTURA**, que es lo que `D.38.3` ensanchada
manda separar. El instrumento **no sabe que dijo la frontera del reporte**: solo
sabe **que lineas de cuerpo no cita ningun candidato de la bandeja**.

    $ python .v3g/cobertura_frontera.py cap_03
    fuentes/grove_high_output/cap_03.md  cuerpo L8 a L179
    lineas de cuerpo                       : 172
    lineas de cuerpo CON texto             : 86
    lineas con texto que NINGUN candidato cita: 17
      L9    1 palabras | 2
      L11   4 palabras | Managing the Breakfast Factory
      L69   127 palabras | Such indicators have many uses. First, they spell out very clearly...
      L127  2 palabras | Assuring Quality
      L129  112 palabras | As we have said, manufacturing's charter is to deliver product...
      L131  79 palabras | In the language of production, the lowest-value-point inspection...
      L133  13 palabras | The key principle is to reject the defective "material" at its lowest-value stage.
      L155  106 palabras | Later, when we examine managerial productivity, we'll see that...
      L157  1 palabras | Productivity
      L159  118 palabras | The workings of our black box can furnish us with the simplest...
      L161  60 palabras | There is a second way to improve productivity. We can change the nature...
      L163  13 palabras | Productivity can be increased by performing the work activities at a higher rate
      L165  8 palabras | or by increasing the leverage of the activities.
      L167  195 palabras | Here I'd like to introduce the concept of leverage, which is the output...
      L175  1 palabras | II
      L177  1 palabras | Management
      L179  4 palabras | Is a Team Game

    $ python .v3g/cobertura_frontera.py cap_02
    lineas de cuerpo CON texto             : 36
    lineas con texto que NINGUN candidato cita: 6
      L9    1 palabras | 1
      L11   7 palabras | The Basics of Production: Delivering a Breakfast
      L13   11 palabras | (or a College Graduate, or a Compiler, or a Convicted Criminal)
      L29   7 palabras | Making the eggs is the limiting step.
      L63   159 palabras | Let's take our manufacturing example a step further and turn our business...
      L65   9 palabras | The continuous egg-boiler: a constant supply of three-minute eggs.

    $ python .v3g/cobertura_frontera.py cap_01
    lineas de cuerpo CON texto             : 56
    lineas con texto que NINGUN candidato cita: 52

**LO QUE EL INSTRUMENTO MIDIO:** cuantas lineas de cuerpo con texto **no aparecen
citadas en ningun `resumen_teorico` de la bandeja**. **NO MIDIO lo que la frontera
publicada dijo de ellas**, porque la frontera vive en el reporte y el reporte no
esta en el arbol. **Esa distincion es mia y la escribo aqui para no publicar de una
cifra una frase que la cifra no sostiene.**

### 4.1. `LECTURA`: los tramos gordos sin nodo, uno a uno, y si estoy de acuerdo

| tramo | palabras | mi lectura |
|---|---|---|
| `cap_03` `L69` | `127` | **CERO ES CORRECTO.** Es un inventario de **USOS** (*Such indicators have many uses. First... Second... Third...*), no de acciones. La vara `6.1` lo dice: **NOMBRAR NO ES PROCEDIMENTAR** |
| `cap_03` `L129` a `L133` | `204` | **CERO ES CORRECTO Y ES LA MEJOR SEÑAL DE TODA LA BANDEJA.** `L129` **repite** la regla del menor valor que `cap_02` `L75` ya dio como nodo `8`, **y el libro mismo lo dice** (*As we have said*, *as noted*). **El extractor NO mino aqui el gemelo de su propio nodo.** `L131` ademas solo **nombra** los tres puntos de inspeccion, y nombrar no es procedimentar |
| `cap_03` `L155` | `106` | **CERO ES CORRECTO.** Es un reenvio hacia delante (*Later, when we examine managerial productivity*) |
| `cap_03` `L159` a `L167` | `373` | **CERO ES CORRECTO, y es el que mas me costo.** `L161` dice *There is a second way to improve productivity*, que suena a inventario de MEDIOS. **Pero la mecanica de la primera via es una frase** (*reorganizing the work area or just by working harder*) **y la de la segunda no esta ahi: es el nodo `23`**, que sale de `L169`. **El material no se pierde, cambia de casa.** `L167` es la definicion de palanca, y una definicion no es procedimiento |
| `cap_02` `L63` | `159` | **DISCUTIBLE MIO, Y ES EL UNICO DE FRONTERA QUE LEVANTO.** Va entero en `4.2` |

### 4.2. **MI DISCUTIBLE DE FRONTERA: `cap_02` `L63`**, marcado a ciegas

**EL TRAMO.** `159` palabras que dicen *First, you buy a continuous egg-boiler...*
y *Second, you match the output of the continuous egg-boiler with the output of a
continuous toaster*, **numeradas por el libro**, con el precio escrito
(*at the expense of flexibility*, *we can no longer prepare each customer's order
exactly when and how he requests it*) y la ganancia escrita (*lower cost and more
predictable product quality*).

**POR QUE LO LEVANTO.** Es **un inventario de dos pasos numerado por el propio
libro, con su intercambio declarado**, que es la misma forma que sostiene al nodo
`23` (`simplificar_trabajo_reducir_numero_pasos`). **Y ademas hace falta:** el nodo
`6` (`preferir_inspeccion_proceso_prueba_destructiva`) se activa *cuando tu
operacion es continua*, y `L63` es **justo la linea que explica como llegaste
ahi**. `L67` empieza *But continuous operation does not automatically mean lower
cost and better quality*, o sea que continua a `L63` de forma expresa.

**POR QUE ME INCLINO IGUAL POR EL CERO, y por poco.** El *First* y el *Second* de
`L63` **son beats del relato del autor**, no instrucciones al lector: *Let's take
our manufacturing example a step further and turn our business into...*. Y el
entregable que saldria de ahi llevaria dentro **datos del caso** (la cocedora
continua, el tostador continuo), que es la **señal barata** que el manual `3.5` da
para saber que un caso se colo en el sitio del procedimiento.

> **MI POSICION: cero nodos, por poco margen, y pido ver la razon escrita.** Si la
> frontera publicada de la vuelta 1 **no dice nada de `L63`**, eso no es una caida
> de clase, pero **si es un tramo de `159` palabras numerado por el libro que salio
> sin motivo escrito**, y lo encargare.

### 4.3. `LECTURA` sobre `cap_01`: `52` lineas sin citar de `56`

**NO ES UN LOTE CORTO: ES UNA INTRODUCTION.** `L13` a `L99` son diagnostico y
postura sin inventario de acciones. **Las unicas lineas con inventario propio son
`L101` a `L107`**, y esas dieron el nodo `1`. **Estoy de acuerdo con la lectura.**

---

## 5. LOS PARES QUE VEO, Y MI VEREDICTO SI LA ADUANA LOS LEVANTA

**Los declaro ANTES de ver el informe completo del lote y ANTES del reporte**, que
es lo unico que los hace informativos. **Ninguno se cablea**: este frente no
inserta (`D.45`).

| # | par | mi veredicto | la linea que lo sostiene |
|---|---|---|---|
| **P1** | `construir_flujo_produccion_paso_limitante` con `rehacer_flujo_paso_limitante_capacidad` | **CONTINUA, no gemelo** | `cap_02` `L51`: *limited toaster capacity means you have to redo your flow around the new limiting step*. **REDO presupone el flujo ya construido.** Y trae lo que el otro no tiene: el paso que manda el plazo deja de ser el que manda la calidad |
| **P2** | `dimensionar_inventario_materia_prima_reposicion` (madre, `cap_02` `L69`) con `decidir_aceptar_rechazar_material_defectuoso` (hijo, `cap_03` `L135`) | **CONTINUA** | El paso `3` de la madre devuelve el material, de `cap_02` `L69`: *If the eggs are unacceptable in some way, you are going to have to send them back*. El hijo **abre exactamente ahi**: *When material is rejected at incoming inspection, a couple of choices present themselves*. **ES UN PAR QUE CRUZA CAPITULO Y NINGUNO DE LOS DOS FICHEROS LO DECLARA** |
| **P3** | `emparejar_indicadores_efecto_contraefecto` (madre) con `elegir_indicador_salida_trabajo_administrativo` (hijo) | **CONTINUA** | `L37` aplica el emparejar de `L31` a otro objeto: *their paired counterparts should stress the quality of work*. **El hijo anade las dos varas y la tabla de seis filas**, que es procedimiento propio |
| **P4** | `detectar_arreglar_fallo_etapa_menor_valor` (madre, `cap_02` `L75`) con `casar_flujo_fabricacion_flujo_ventas` paso `11` | **ARISTA, no par** | `cap_03` `L119` dice *Ideally, inventory should be kept at the lowest-value stage, as we've learned before*. **El libro se remite a si mismo**, asi que es cable y no fusion |
| **P5** | `elegir_indicador_salida_trabajo_administrativo` (madre) con `dimensionar_plantilla_administrativa_pronostico` paso `1` | **ARISTA, no par** | `L125` abre *if we have carefully chosen indicators that characterize an administrative unit*, que es el entregable del otro nodo puesto como condicion de entrada |
| **P6** | `preferir_inspeccion_proceso_prueba_destructiva` (`cap_02` `L67`) con `elegir_inspeccion_barrera_monitorizacion` (`cap_03` `L141`) | **CONTINUA, no gemelo** | El primero elige **el TIPO de prueba** (la que destruye producto contra la que no); el segundo elige **el REGIMEN** (retener todo contra muestrear y dejar correr). Comparten vocabulario, no objeto |
| **P7** | `elegir_inspeccion_barrera_monitorizacion` con `variar_frecuencia_inspeccion_nivel_calidad` | **CONTINUA, no gemelo** | `L143` abre *Another way to lower the cost of quality assurance*, o sea que **el propio libro los presenta como dos vias distintas**: aqui QUE tecnica, alli CADA CUANTO |
| **P8** | `construir_indicador_tendencia_patron` con `construir_grafico_escalonado_pronosticos` | **CONTINUA, no gemelo** | `L91` los **contrasta de forma expresa**: *better than if you used a simple trend chart*. **Una frontera que declara el propio texto** |
| **P9** | `clasificar_trabajo_proceso_montaje_prueba` paso `4` con `detectar_arreglar_fallo_etapa_menor_valor` paso `6` | **ARISTA, no par** | Los dos nombran la prueba unitaria; `L75` la usa como **ejemplo de la regla del menor valor**, no como su procedimiento |

**EL QUE MAS ME IMPORTA ES `P2`**, y por eso lo pongo aparte: **cruza de `cap_02` a
`cap_03`, o sea de la vuelta 1 a la vuelta 2**, y **ni el fichero de la madre ni el
del hijo lo nombran**. Es exactamente la figura que `D.38.5` vino a cubrir: **los
dos extremos viven en la bandeja**, ninguno en el grafo.

---

## 6. LOS DISCUTIBLES QUE MARCO A CIEGAS, NUMERADOS

**Marcados ANTES de ver el reporte.** Si alguno cae, cae **DENTRO** de mi marcado.

| # | discutible | donde |
|---|---|---|
| **D1** | **`representar_actividad_caja_negra_ventanas` es un CONCEPTO con ejemplos, no un procedimiento.** Lo sostengo, y es el primero de mi cola | `2.3`, nodo `12` |
| **D2** | **`archivar_indicadores_resolver_problemas` es una LINEA, y sus pasos `1` y `2` nombran el mismo objeto dos veces.** Lo sostengo como nodo aparte, con su reserva escrita | `2.3`, nodo `16` |
| **D3** | **`revisar_tres_preguntas_valor_carrera` es POSTURA: lo que se ejecuta es un examen de uno mismo.** Lo sostengo por la vara escrita de `L103` | `2.1` |
| **D4** | **El paso `6` de `variar_frecuencia_inspeccion_nivel_calidad` es un PUENTE del acto.** Lo cargo yo como puente, `1` de `178` | `3.2` |
| **D5** | **El paso `9` de `construir_indicador_linealidad_alerta_temprana` es la misma figura y NO lo cargo.** Lo dejo marcado para que se pueda tumbar | `3.3` |
| **D6** | **`cap_02` `L63`, `159` palabras numeradas por el libro, salieron sin nodo.** Me inclino por el cero **por poco margen** y pido la razon escrita | `4.2` |
| **D7** | **`P2` cruza capitulo y ningun fichero lo declara.** Si la aduana no lo levanta, es un par que solo se ve si alguien se acuerda de mirarlo | `5` |
| **D8** | **`dominio` nuevo por partida doble sin que ningun instrumento lo pare:** `produccion` y `carrera_profesional` no existian, y `1` solo candidato sostiene el segundo. **No es caida**, porque `config/umbrales.json` tiene `solo_dominio_y_nucleo` en `false` y por tanto no estrecha ningun barrido, **pero un dominio con un solo nodo es una frontera que hay que vigilar** | `1.4` |

---

## 7. LO QUE NO HE PODIDO CERRAR EN ESTA FASE, Y LO DIGO

**EL INFORME DE LA ADUANA SOBRE EL LOTE ENTERO LO LANCE Y NO HA CERRADO.**

    $ python forja.py informe --carpeta cuarentena/grove_high_output
    (lanzado a las 05:48:58, sin cerrar cuando firmo esta seccion; el testigo es
     .v3g/informe_lote.txt y esta a 1 linea, la del propio comando)

**LO QUE SI TENGO CERRADO ES EL INFORME DE UN CANDIDATO**, corrido entero a las
`05:46`, y lo pego con su cola de lectura porque es la unica medida de vecindad que
puedo firmar en esta fase:

    $ python forja.py informe cuarentena/grove_high_output/revisar_tres_preguntas_valor_carrera.json
    candidatos revisados        : 1
    poblacion del barrido       : 371   (270 del grafo mas 101 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60
    EL SALDO
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0
    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 2
      que señal levanta cada vecindad  : similitud_texto 2
    [BLOQUEARIA] revisar_tres_preguntas_valor_carrera
        vecino archivar_indicadores_resolver_problemas  [levantada por: similitud_texto]
          similitud_texto 0.357 | familia_id 0.000 | paso_contra_nodo 0.387
        vecino emparejar_indicadores_efecto_contraefecto  [levantada por: similitud_texto]
          similitud_texto 0.354 | familia_id 0.000 | paso_contra_nodo 0.376

**`LECTURA`, y va marcada porque es conclusion y no medida:** los dos vecinos que
la maquina levanta para el nodo `1` **son los dos de la bandeja y ninguno del
grafo**, y los dos rozan el umbral (`0,357` y `0,354` contra `0,35`). **Leidos los
pasos, ninguno de los dos es gemelo suyo:** el nodo `1` pregunta por la carrera de
uno mismo, el `16` guarda una serie de indicadores y el `10` empareja indicadores
de fabrica. **Mi veredicto para los dos, si llegan a pedirlo, seria SANO**, y esa
es la unica adjudicacion de vecindad que puedo firmar hoy.

**LO QUE ESTO CUESTA, Y NO LO ESCONDO:** sin el informe de lote cerrado **no puedo
publicar ni `ENTRARIAN` ni `BLOQUEARIAN` ni `CHOCAN` del lote de `23`**, y por
tanto **no publico ninguna de esas tres cifras**. Una cifra sin instrumento al lado
no se publica (`D.38.3`), y prefiero el hueco declarado a la cifra copiada. **Lo
recojo en mi turno normal y lo digo en el acta.**

---

## 8. EL RESUMEN DE MI APERTURA, EN UNA TABLA

**Todas las cifras de esta tabla salen de un instrumento pegado arriba, y llevan la
hora en la que se midio.**

| lo que mido | cifra | hora | donde esta su instrumento |
|---|---|---|---|
| nodos en `dataset/nodos.jsonl` | `270` | `05:43` | `1.3` |
| lineas en `bitacora/VEREDICTOS.jsonl` | `396` | `05:43` | `1.3` |
| lineas de veredicto de este libro | `0` | `05:52` | `0.3` |
| poblacion del barrido (grafo mas bandejas) | `371` | `05:43` y `05:46` | `0.1`, y cuadra con la maquina |
| candidatos en la bandeja de este libro | `23` | `05:44` | `1.4` |
| pasos escritos en la bandeja | `178` | `05:44` | `1.4` |
| pasos de `cap_03` | `121` | `05:53` | `1.5` |
| aristas cableadas en la bandeja | `0` | `05:44` | `1.4` |
| candidatos que leo SOSTENIDO | `20` de `23` | `05:57` | `2.4` |
| candidatos que leo SOSTENIDO CON RESERVA | `3` de `23` | `05:57` | `2.4` |
| candidatos que leo NO SOSTENIDO | `0` de `23` | `05:57` | `2.4` |
| pasos que leo PUENTE, peor capitulo | `1` de `121` en `cap_03`, `0,83` por ciento | `05:57` | `3.1` |
| pasos que leo PUENTE, lote entero | `1` de `178`, `0,56` por ciento | `05:57` | `3.1` |
| pares que declaro por lectura | `9` | `05:58` | `5` |
| discutibles que marco a ciegas | `8` | `05:58` | `6` |
| gate | `VERDE` sobre `270` nodos | `05:45` | `1.3` |
| barrido de guiones sobre mis instrumentos | `VERDE` | `05:52` | `0.4` |
| informe de aduana del lote de `23` | **SIN CERRAR, declarado** | `05:47` | `7` |

**Y LAS CUATRO DECLARACIONES OTRA VEZ, porque el arnes mira presencia:**

    ACTA ANTERIOR LEIDA: dea8d91127926fcadf2273a0af887e8b58249a86
    HEREDADO 1: CUMPLIDO
    HEREDADO 2: CUMPLIDO
    HEREDADO 3: CUMPLIDO
    HEREDADO 4: CUMPLIDO

### 8.1. **LAS RUTAS QUE ESTA APERTURA PUBLICA COMO PRUEBA, Y SU AVISO**

**Una ruta publicada como evidencia cuenta como `CIFRA PUBLICADA` en su sede**
(cosecha `7.B`), y una que apunte a un fichero inexistente o de cero bytes es
caida. **Asi que declaro el estado de las mias**, medido a las `06:03`:

    $ ls -la --time-style=+%H:%M .v3g/
    -rw-r--r-- 1 AlexDesk 197609  970 05:46 censo_lote.py
    -rw-r--r-- 1 AlexDesk 197609 1821 05:54 cobertura_frontera.py
    -rw-r--r-- 1 AlexDesk 197609 2708 05:56 cuentas_mi_clase.py
    -rw-r--r-- 1 AlexDesk 197609   65 05:48 informe_lote.txt
    -rw-r--r-- 1 AlexDesk 197609 1292 05:56 mi_clase.tsv
    -rw-r--r-- 1 AlexDesk 197609  491 05:54 palabras_tramo.py
    -rw-r--r-- 1 AlexDesk 197609 1633 05:53 pasos_por_capitulo.py
    -rw-r--r-- 1 AlexDesk 197609 1770 05:44 poblacion.py
    -rw-r--r-- 1 AlexDesk 197609 1116 05:53 sin_ids_tecleados.py
    -rw-r--r-- 1 AlexDesk 197609 1259 05:49 volcar.py

**Los diez existen y ninguno esta en cero bytes.** El mas pequeno,
`informe_lote.txt`, tiene `65` bytes y contiene **exactamente** la linea del comando
que declaro sin cerrar en `7`.

**Y AVISO DE LO QUE FALTA, porque no lo puedo arreglar yo en esta fase:**

    $ git ls-files .v3g | wc -l
    0

**`.v3g/` NO ESTA EN EL ARBOL DE GIT TODAVIA**, porque esta fase **no commitea** y
la sella el arnes sobre `docs/loop/`. **Quien haga checkout de ese commit no va a
encontrar mis instrumentos.** Lo declaro aqui y **los commiteo en mi turno normal**,
que es cuando `docs/loop/` entero se commitea (seccion `1.5` del protocolo). **Una
ruta que promete prueba y no viaja con ella es media prueba**, y prefiero decirlo yo
antes de que lo encuentre el siguiente.

**Cierro esta apertura a las `05:59` del 17 sep 2026, sin commitear: la sella el
arnes.**
