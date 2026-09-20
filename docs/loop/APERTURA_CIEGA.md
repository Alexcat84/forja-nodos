# APERTURA CIEGA DEL AUDITOR

**Turno que el arnes abre como `VUELTA 2 : APERTURA CIEGA (claude-opus-5)`** en
`docs/loop/loop.log`, sobre el lote de `grove_high_output` que el turno de extractor
inmediatamente anterior deposito en `cuarentena/`.

**ESTA PAGINA PUBLICA CLASES Y LECTURAS.** Toda cifra que lleva dentro sale de un
instrumento corrido por mi EN ESTA FASE, con su salida literal debajo, y **la cifra que
publico es la de la LINEA DE RESUMEN del propio instrumento**, no un recuento del pegado
(`D.38.3`, y el `REMEDIO 1` que la `ACTA 53` me dejo escrito: seccion 0.3).

---

## 0. LO QUE EL ARNES EXIGE ANTES QUE NADA

### 0.1. La linea de lectura

    ACTA ANTERIOR LEIDA: dfef6f9fea7cf2f1a75ec8b6733c8724cd989ee7

**Y NO LA COPIO DEL PROMPT: LA VUELVO A MEDIR**, porque `herencia.huella()` es
`git hash-object` y eso lo puedo correr yo:

    $ sed -n '134,140p' src/herencia.py
    def huella(ruta):
        """La misma huella que usa el testigo del arnes, para no medir de dos formas."""
        try:
            salida = subprocess.check_output(["git", "hash-object", ruta],
                                             cwd=comun.RAIZ, stderr=subprocess.STDOUT)

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    dfef6f9fea7cf2f1a75ec8b6733c8724cd989ee7

**Coincide con la que el prompt me entrega.** El acta que he leido es la que el arnes dice.

### 0.2. Los heredados que el instrumento entrega: CERO

    $ python forja.py herencia
      acta anterior : ACTA 53. VUELTA 54, lote 7 (`grove_high_output`), ...
      su huella     : dfef6f9fea7cf2f1a75ec8b6733c8724cd989ee7
      heredados     : 0

    AVISO: esta acta MENCIONA remedios en 1 encabezado(s) y no ESCRIBE ninguna tabla de
    remedios fuera de cita. No se entrega ninguno, y se dice en voz alta: un arnes que
    entrega cero sin avisar es el defecto que la TAREA 2 de la vuelta 31 vino a cerrar.

**HEREDADOS POR EL ARNES: `0`.** Esa es la salida del instrumento y la publico tal cual.

### 0.3. Y NO SON CERO: EL ACTA 53 ME DEJO UN REMEDIO ESCRITO PARA ESTE TURNO

El propio instrumento avisa de que hay `1` encabezado de remedio que no consigue extraer.
**Lo abri y esta ahi, con mi nombre y con el turno puesto** (`AUDITOR_FORJA.md` me deja
abrir mi propia acta en esta fase, y es justo para esto):

    $ awk 'NR>=39035' docs/loop/ACTA_AUDITOR.md | grep -n "REMEDIO"
    439:> ## **REMEDIO 1 DE LA `ACTA 53`, PARA MI TURNO DE LA `54`**

    $ awk 'NR>=39035' docs/loop/ACTA_AUDITOR.md | sed -n '439,444p'
    > ## **REMEDIO 1 DE LA `ACTA 53`, PARA MI TURNO DE LA `54`**
    >
    > **TODA CIFRA QUE YO SAQUE DE UNA SALIDA DE INSTRUMENTO SE LEE DE LA LINEA DE RESUMEN DEL
    > PROPIO INSTRUMENTO, Y SI PEGO UN EXTRACTO, PEGO ESA LINEA CON EL.** Si el instrumento no
    > imprime resumen, **lo digo** y cuento sobre el fichero entero, no sobre el pegado.

**HEREDADO 1: CUMPLIDO**, y cumplido en el sitio donde nacio, que es esta pagina sellada.
La forma en que lo cumplo es verificable: **cada cifra de esta pagina va con la linea de
resumen del instrumento que la imprime**, y donde el instrumento no imprime resumen lo
digo. El ejemplar vivo esta en la seccion `3.3`.

**LA CAUSA DE QUE NO SE ENTREGUE, MEDIDA Y NO SUPUESTA:** el remedio esta escrito dentro de
una cita (`> ## **REMEDIO 1 ...**`), y el extractor de herencia no levanta remedios en
cita. Su propio AVISO lo dice con estas palabras: *no ESCRIBE ninguna tabla de remedios
fuera de cita*. **NO LO ARREGLO**: el arnes es sede vedada por `D.45` y esto sube al
fundador. Lo que si hago es **declararlo aqui antes de que se pierda**, que es lo que las
actas `14`, `15` y `16` no hicieron tres veces seguidas.

### 0.4. Y NO HAY HUECO DE ACTA

    $ grep -n "^# ACTA 5[0-9]" docs/loop/ACTA_AUDITOR.md | tail -1
    39035:# ACTA 53. VUELTA 54, lote 7 (`grove_high_output`), **VUELTA DE SANEAMIENTO ...

La ultima acta escrita cubre la vuelta inmediatamente anterior a la que vengo a auditar.
**No hay ninguna vuelta sin acta que recoger.**

---

## 1. LO QUE ESTA FASE NO PUEDE COMPROBAR, DICHO ANTES DE AFIRMAR NADA

*`AUDITOR_FORJA.md` 1.1: una busqueda negativa no se puede citar. Esto es lo que NO tengo.*

### 1.1. Los cuatro retirados, comprobados en el log que no se retira

    $ tail -3 docs/loop/loop.log
    [2026-09-20 15:46:42] VUELTA 2 : APERTURA CIEGA (claude-opus-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl
    [2026-09-20 15:46:42]   hereda 0 remedio(s) del acta anterior, entregados en el prompt (D.40)
    [2026-09-20 15:46:42]   y solo eso: remedios con su motivo, sin cifras ni conclusiones (D.52)

**No he recuperado ninguno de los cuatro, ni de git ni por ninguna otra via.**

### 1.2. NO PUBLICO NINGUNA RACHA DE CREDITO, Y DIGO POR QUE

    $ python forja.py credito
    CREDITO DE LA LINEA 'serial' (D.48)
      registro: docs/loop/CREDITO_serial.jsonl

      LINEA SIN REGISTRO: no hay ningun suceso escrito.
      Una linea sin tandas NACE CON SU RACHA EN CERO y no hereda
      la de nadie (D.48). Lo que herede el arnes sera CERO remedios.

**ESA SALIDA ES FALSA COMO ESTADO Y VERDADERA COMO SALIDA**, y la diferencia es todo:
`docs/loop/CREDITO_serial.jsonl` es **uno de los cuatro ficheros que el arnes acaba de
retirar** (linea del log pegada arriba), asi que el instrumento no esta leyendo *racha en
cero*: esta leyendo *fichero ausente*. **Publicar `racha en cero` desde aqui seria una
cifra falsa en pagina sellada**, que es exactamente la especie que me cuesta un escalon.

Lo unico que digo de las rachas es **lo que leo en mi propia acta, citandola y sin firmarlo
como medicion mia**: la `ACTA 53` `53.12` escribe `REPORTE 1 de 3`, `CIFRA PUBLICADA 0 de
2`, `CLASE 0 de 2`, `DATO MOVIDO 0 de 2` y `AUDITOR 1 de 3`. **Lo remido en mi turno
normal, con el fichero devuelto.**

### 1.3. Ocho de los nueve candidatos se citan contra un fichero que no existe

Los `8` de `cap_07` fechan su pieza contra `docs/loop/REPORTE.md` con numero de linea
(`L50888` a `L50909`). **Ese fichero esta retirado y ademas se reescribe cada vuelta**, asi
que **esta fase no puede comprobar ni una sola de esas ocho citas**, y no las doy por buenas
ni por malas. Es la pregunta `4` de la cola de doctrina (`D.56`), ya registrada, y **no la
reabro**.

### 1.4. CONTAMINACION QUE DECLARO Y QUE NO BUSQUE YO

El bloque `gitStatus` que el arnes pone en mi prompt de sistema trae los **asuntos de los
cinco ultimos commits**, y el primero es el commit de cierre del extractor cuyo trabajo
vengo a leer a ciegas. Ese asunto adelanta parte de su saldo. **No lo he ido a buscar, no lo
uso como medida y no lo cito como cifra en ninguna seccion de esta pagina**, pero mi lectura
ya no es ciega del todo respecto de ese dato, y **decirlo vale mas que fingir que no paso**.
Todo lo que clasifico abajo esta leido contra `fuentes/` y contra los JSON de `cuarentena/`.

**Y NO ABRI `.v55ext/`**, que es el cuaderno de trabajo que el extractor commiteo en el
mismo arbol: no es ninguno de los cuatro que `D.34.2` retira, pero leerlo seria leer su
razonamiento, que es justo lo que esta fase existe para no leer.

---

## 2. EL LOTE, IDENTIFICADO CON INSTRUMENTO Y NO DE MEMORIA

El prompt no me nombra los candidatos. Los identifico por lo que el arbol dice: son los
ficheros **ANIADIDOS** a `cuarentena/` por el ultimo commit que la toca.

    $ git show --stat --format='' --diff-filter=A 759ed91 -- cuarentena/
     .../cerrar_brecha_dos_preguntas_estrategia.json    | 42 +++++++++++++++++++
     ...ontestar_dos_preguntas_direccion_objetivos.json | 44 +++++++++++++++++++
     ...no_grupo_clientes_proveedores_competidores.json | 41 ++++++++++++++++
     ...stado_presente_capacidades_proyectos_merma.json | 49 ++++++++++++++++++++++
     ...inar_demanda_entorno_dos_marcos_temporales.json | 42 +++++++++++++++++++
     ...expectativas_tecnologia_proveedores_grupos.json | 36 ++++++++++++++++
     .../fijar_horizonte_ventana_replanificacion.json   | 47 +++++++++++++++++++++
     ...iodo_direccion_objetivos_retroalimentacion.json | 40 ++++++++++++++++++
     ...partir_supervision_puesto_funcional_mision.json | 43 +++++++++++++++++++
     9 files changed, 384 insertions(+)

**NUEVE candidatos, y los NUEVE son altas.** Ninguno es retoque de un candidato viejo.

Su tamanio, contado por mi, con la linea de resumen del contador:

    $ python -c "conteo de pasos_accionables de los 9 candidatos del lote"
    cerrar_brecha_dos_preguntas_estrategia                     pasos=7 atrib=0
    contestar_dos_preguntas_direccion_objetivos                pasos=5 atrib=0
    definir_entorno_grupo_clientes_proveedores_competidores    pasos=6 atrib=0
    determinar_estado_presente_capacidades_proyectos_merma     pasos=7 atrib=1
    examinar_demanda_entorno_dos_marcos_temporales             pasos=7 atrib=0
    examinar_entorno_expectativas_tecnologia_proveedores_grupos pasos=5 atrib=0
    fijar_horizonte_ventana_replanificacion                    pasos=5 atrib=1
    fijar_periodo_direccion_objetivos_retroalimentacion        pasos=5 atrib=0
    repartir_supervision_puesto_funcional_mision               pasos=8 atrib=0
    TOTAL pasos del lote = 55  candidatos = 9

**`55` pasos y `9` candidatos**, y `2` fichas de atribucion. Por capitulo: **`cap_07` pone
`47` pasos en `8` candidatos** y **`cap_10` pone `8` pasos en `1`**.

    $ python -c "tasa de pasos que MI lectura marca PUENTE, por capitulo"
    cap_07 pasos escritos = 47
    cap_10 pasos escritos = 8

---

## 3. EL ESTADO CON EL QUE ABRO, CADA CIFRA CON SU RESUMEN

### 3.1. El gate

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada,
               vuelta, cita_incompleta, deprecado_en_superficie, arista_rota,
               arista_incompleta, guiones, censo_no_decrece

### 3.2. El grafo y la bitacora

    $ wc -l dataset/nodos.jsonl
    346 dataset/nodos.jsonl

    $ wc -l bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl

### 3.3. El bloque de vigencia, y aqui es donde se paga el `REMEDIO 1`

    $ python forja.py rancios | head -4
    BLOQUE DE VIGENCIA: 79 hallazgo(s) sobre 726 veredicto(s) y 0 cita(s).
      RANCIO 71, SIN HUELLA 8
      lineas declaradas NO CONSUMADAS y por eso no medidas: 14
        (las escribio una corrida que no inserto nada; ver su razon en la propia linea)

**PUBLICO `RANCIO 71` PORQUE ES LO QUE DICE SU LINEA DE RESUMEN.** Y dejo el contraste a la
vista, que es lo que el remedio pide:

    $ python forja.py rancios | grep -c "^RANCIO"
    0

**`0` contra `71`**: las lineas de detalle van sangradas y empiezan por `[RANCIO]`, asi que
contar el pegado con un ancla de principio de linea da cero. **Contar el pegado en vez de
leer el resumen es la caida que me cargue en la `ACTA 53`, y por eso la mido aqui en vez de
prometer que no la repito.**

**Y CUADRA CON LA BITACORA:** `726` medidos mas `14` no consumadas dan los `740`.

    $ python -c "print('726 + 14 =', 726+14)"
    726 + 14 = 740

### 3.4. La deuda

    $ python scripts/deuda.py
      pendientes: 19    pagadas: 25
      ...
      ultima vuelta de saneamiento: 54

### 3.5. El tablero

    $ python forja.py tablero
      1    7    grove_high_output              COSECHADO              NINGUNO       74  cap_10
      ...
      MUNDO 11: faltan 3 de 3 libros del corte (grove_high_output, gerber_emyth, marquet_turn_the_ship)
      COLA DE DOCTRINA (D.56): 11 pregunta(s), 0 bloquea(n)

`74` en bandeja para `grove_high_output`, y `cap_10` por ultimo capitulo minado.

---

## 4. MI LECTURA DEL LIBRO Y MI CLASIFICACION, CANDIDATO A CANDIDATO

**COMO LEI.** Abri `fuentes/grove_high_output/cap_07.md` y `cap_10.md` enteros **antes** de
abrir ninguna de las nueve fichas, y numere sus lineas con el instrumento para poder citar
tramo por tramo:

    $ wc -l fuentes/grove_high_output/cap_07.md fuentes/grove_high_output/cap_10.md
      105 fuentes/grove_high_output/cap_07.md
       79 fuentes/grove_high_output/cap_10.md
      184 total

    $ awk 'NR>=1 && NR<=40 {printf "L%d: %s\n", NR, $0}' fuentes/grove_high_output/cap_07.md
    (y los tramos 41-82, 83-105, y cap_10 39-47, con el mismo comando)

**LO QUE NO HAGO AQUI:** no adjudico ninguna discrepancia contra el reporte, porque no lo he
visto. **Clasifico, y dejo la comparacion para el turno normal.**

### 4.1. La tabla de mi clasificacion

| # | candidato | capitulo y tramo | mi clase | mi lectura `D.30` |
|---|---|---|---|---|
| 1 | `cerrar_brecha_dos_preguntas_estrategia` | `cap_07` `L39` | **PROCEDIMIENTO** | `7` de `7` TRANSCRIPCION |
| 2 | `contestar_dos_preguntas_direccion_objetivos` | `cap_07` `L71-L75` | **PROCEDIMIENTO**, por los pelos | `5` de `5` TRANSCRIPCION |
| 3 | `definir_entorno_grupo_clientes_proveedores_competidores` | `cap_07` `L25` | **PROCEDIMIENTO** | `6` de `6` TRANSCRIPCION, con una tension que declaro |
| 4 | `determinar_estado_presente_capacidades_proyectos_merma` | `cap_07` `L35` | **PROCEDIMIENTO** | `7` de `7` TRANSCRIPCION |
| 5 | `examinar_demanda_entorno_dos_marcos_temporales` | `cap_07` `L29` y `L31` | **PROCEDIMIENTO** | `6` TRANSCRIPCION y **`1` que leo PUENTE** (paso `7`) |
| 6 | `examinar_entorno_expectativas_tecnologia_proveedores_grupos` | `cap_07` `L27` | **PROCEDIMIENTO** | `5` de `5` TRANSCRIPCION |
| 7 | `fijar_horizonte_ventana_replanificacion` | `cap_07` `L61` | **PROCEDIMIENTO** | `4` TRANSCRIPCION y **`1` que leo PUENTE** (paso `1`) |
| 8 | `fijar_periodo_direccion_objetivos_retroalimentacion` | `cap_07` `L79` | **PROCEDIMIENTO** | `5` de `5` TRANSCRIPCION |
| 9 | `repartir_supervision_puesto_funcional_mision` | `cap_10` `L43` | **PROCEDIMIENTO** | `8` de `8` TRANSCRIPCION |

**LECTURA:** los nueve me salen procedimiento, y ninguno me sale definicion, postura ni
caso. **Donde discrepo es en la fidelidad, no en la clase**, y son dos pasos de dos fichas
distintas.

### 4.2. Los dos pasos que yo leo PUENTE, y por que

**LA VARA QUE USO ES LA DE `D.30`: un paso es PUENTE si el libro no lo dice.** No si suena
raro ni si esta de mas: si la frase imperativa la escribio la mano y no el libro.

#### a) `examinar_demanda_entorno_dos_marcos_temporales`, paso `7`

La ficha escribe: *No rebajes la demanda que declaras por lo que creas que la otra parte
puede entregar: una demanda rebajada asi deja que nunca se prepare la capacidad para la
demanda real.*

**El libro, en `L31`, NO PROHIBE NADA.** Pregunta y narra:

    L31: What would happen to a factory, for instance, if the marketing organization
    adjusted its demand forecast on the basis of its own assessment of the manufacturing
    unit's ability to deliver? If marketing knew they could sell 100 widgets per month but
    thought that manufacturing could only deliver ten, and so submitted a demand forecast
    of ten units, manufacturing would never tool up to satisfy the real demand.

**LA MITAD DE ATRAS ES TRANSCRIPCION Y LA DE DELANTE NO.** *nunca se prepare la capacidad
para la demanda real* es `would never tool up to satisfy the real demand`, literal. **`No
rebajes` no esta en el libro**: es la norma que el ejemplo sugiere, escrita por la mano. Y
el contraste que lo hace visible esta en el mismo tramo: **el paso `6` de la misma ficha SI
tiene su imperativo en el libro**, porque ahi el autor se contesta a si mismo con un `No,
that will just confuse the issue`. **Aqui no se contesta.**

**NO ES CAIDA DE CLASE NI ME PARECE MAL EL NODO.** Es una fila de la metrica de volumen que
yo cuento de otra manera, y `8.4` dice expresamente que un puente declarado **no es caida de
nadie**.

#### b) `fijar_horizonte_ventana_replanificacion`, paso `1`

La ficha escribe: *Mira hacia delante mas alla del periodo que vas a implementar, aunque lo
que de verdad estes influyendo sea solo el periodo siguiente.*

El libro, en `L61`:

    L61: How far ahead should the planners look? At Intel, we put ourselves through an
    annual strategic long-range planning effort in which we examine our future five years
    off. But what is really being influenced here? It is the next year-and only the next year.

**EL LIBRO SE HACE LA PREGUNTA Y LA CONTESTA CONTANDO LO QUE HACE INTEL.** Quitada la
practica de Intel, que es lo que la ficha hace bien y declara, **lo que queda no es una
instruccion del libro: es la observacion de que solo el anio siguiente se ve afectado**. El
imperativo *mira hacia delante mas alla* lo pone la mano. **Este es el mas claro de los
dos**, porque el otro al menos conserva media frase literal y este no conserva ninguna.

**Y ES LA TENSION QUE LA PROPIA FICHA DECLARA**, con otras palabras (*queda mas cerca de un
principio que de una instruccion ejecutable*). **Donde no coincidimos es en el casillero**:
la ficha lo deja en TRANSCRIPCION y yo lo leo PUENTE.

### 4.3. La tension que declaro y que NO cuento como puente

#### `definir_entorno_grupo_clientes_proveedores_competidores`, pasos `3`, `4` y `5`

Las tres clases de grupo viven, en el libro, **dentro de la frase que empieza por `For
example`**:

    L25: Just what is your environment? If you look at your own group within an organization
    as if it were a stand-alone company, you see that your environment is made up of other
    such groups that directly influence what you do. For example, if you were the manager of
    the company's mailroom, your environment would consist of customers who need your
    services (the rest of the company), vendors who are able to provide you with certain
    capabilities (postage meters, mail carts), and finally, your competitors.

**LA FICHA DECLARA LA SALA DE CORREO Y UNITED PARCEL COMO EJEMPLO, PERO NO DECLARA QUE EL
INVENTARIO DE TRES CLASES SALE DE DENTRO DEL EJEMPLO.** Me lo mire dos veces, porque es el
sitio exacto donde una compresion se cuela.

**LO ADJUDICO A FAVOR DE LA FICHA, Y DIGO CON QUE: los parentesis.** `(the rest of the
company)` y `(postage meters, mail carts)` son la sala de correo; **lo que queda fuera de los
parentesis es la taxonomia**, y la ficha se quedo exactamente con lo de fuera. Si las tres
clases fueran del ejemplo, los parentesis no tendrian a quien instanciar. **`6` de `6`
TRANSCRIPCION, y la tension queda escrita para que el siguiente lector la pueda mirar.**

### 4.4. Lo que le firmo a la ficha `9`, y ella no se firmo

`repartir_supervision_puesto_funcional_mision` declara como su discutible mas serio que
`L43` **se abre con `Consider how the controller works at Intel`**, y que quien lea todo lo
que sigue como CASO le tumba el nodo y deja `cap_10` en cero. **Es honesto, y es el riesgo
real.** Lo sostengo, y lo sostengo con una linea que la ficha **no cita** y que zanja la
cuestion desde el propio libro:

    L45: The example has parallels throughout a corporation.

**El libro dice, con todas las letras y en la linea siguiente, que el caso del controller se
generaliza.** El tramo abre con la regla (`To make hybrid organizations work, you need a way
to coordinate...`), cierra con la regla (`this is dual reporting, the management principle
that enables the hybrid organization form to work`), y el libro certifica la generalizacion
dos lineas despues. **El caso va dentro de su doctrina, y no al reves.**

### 4.5. `PASOS INVENTADOS POR CAPITULO`, MI LECTURA CIEGA

*No es la cifra del acta: es la mia, leida a ciegas, para poder cruzarla despues.*

    $ python -c "tasa de pasos que MI lectura marca PUENTE, por capitulo"
    cap_07 pasos escritos = 47
    cap_10 pasos escritos = 8
    cap_07: 1 de 47 = 2.13 por ciento
    cap_07: 2 de 47 = 4.26 por ciento
    cap_10: 0 de 8 = 0.00 por ciento

| capitulo | pasos escritos | pasos que yo leo PUENTE | tasa |
|---|---|---|---|
| **`cap_07`** | `47` | **`2`** (el paso `7` de la ficha `5` y el paso `1` de la ficha `7`) | **`4,26` por ciento** |
| **`cap_10`** | `8` | **`0`** | **`0,00` por ciento** |
| **lote entero** | `55` | `2` | `3,64` por ciento |

**Y PUBLICO LAS DOS FILAS, NO EL PROMEDIO** (`8.2`). **Si de los dos solo se sostuviera el de
`fijar_horizonte`, que es el que veo mas claro, `cap_07` queda en `1` de `47`, el `2,13` por
ciento**, y por eso la salida trae las dos lineas calculadas.

**LECTURA, EN LINEA APARTE Y MARCADA (`D.38.3` ensanchada):** con cualquiera de las dos
cuentas, **los dos capitulos quedan muy por debajo del tope de `10` por ciento** de `8.1`,
asi que **por esta metrica el tramo siguiente no baja un escalon.** Lo que decida el volumen
de la vuelta que viene no sale de aqui: **sale del techo de candidatos, que es el otro
disparador y el que manda cuando los dos chocan** (`EXTRACTOR.md` `12.4`).

### 4.6. Lo que el capitulo `07` deja sin nodo, leido por mi y sin saber que dijo la frontera

**Esto NO es una acusacion: es la lista que quiero poder cruzar.** De `cap_07`, estos tramos
tienen forma de instruccion y **no los cubre ninguna de las nueve fichas**:

| tramo | que dice | como lo leo yo |
|---|---|---|
| `L57` | *as you plan you must answer the question: What do I have to do today to solve-or better, avoid-tomorrow's problem?* | **una sola pregunta, sin inventario ni medio**: lo leo POSTURA, cero nodos |
| `L59` | *the true output of the planning process is the set of tasks it causes to be implemented* | **DEFINICION** del producto del proceso, cero nodos |
| `L65` | *by saying yes you are implicitly saying no to something else* ... *People who plan have to have the guts, honesty, and discipline to drop projects* | **POSTURA**, y con adjetivo de adecuacion en el sitio del criterio: cero nodos |
| `L81` | *keep the number of objectives small* | **POSTURA**: `small` es adjetivo de adecuacion y el libro no da vara |
| `L97` | *to be useful a key result must contain very specific wording and dates* | **POSTURA**: `very specific` es el mismo caso |

**Las fichas `1`, `2` y `8` ya declaran `L81` y `L97` como piezas de cero nodos** por ese
mismo motivo, asi que ahi coincido con ellas sin haber visto su frontera. **`L57`, `L59` y
`L65` no los nombra ninguna ficha**, y es la pieza de mi lectura que mas quiero cruzar
contra el reporte en el turno normal.

**Y LOS CASOS SON CASOS, y los leo como tales, manual 3.5:** `L15` (la gasolina), `L45` a
`L53` (Bruce y Cindy), `L77` (el aeropuerto y los pueblos A, B y C), `L85` a `L101` (Colon y
la planta de Filipinas). **Ninguno pide nodo.**

---

## 5. EL BARRIDO DE VECINOS SOBRE GRAFO MAS BANDEJAS (`D.38.4`, `D.38.5`)

### 5.1. La poblacion, y la unica cifra en la que mi cuenta y la maquina no coinciden

    $ python -c "la poblacion de bandejas de la casa, por carpeta"
    poblacion_de_bandejas() devuelve: 77
    ficheros .json por carpeta (sin _insertados ni _derivadas):
       ensayo_referencia_163      163
       grove_high_output          74
       marquet_turn_the_ship      3
    TOTAL ficheros = 240 | TOTAL en poblacion = 77 | fuera de poblacion = 163

**MI PRIMER RECUENTO A PIE DE CARPETA DIO `240` Y LA MAQUINA DICE `77`.** Lo persegui antes
de publicar nada, y **la maquina tiene razon y lo tiene escrito**:

    $ sed -n '385,397p' src/aduana.py
    # Y SE DESCARTA LO QUE NO PUEDE ENTRAR, QUE NO ES LO MISMO QUE LO QUE NO HA
    # ENTRADO. `cuarentena/` tambien aloja `ensayo_referencia_163/`, que son 163
    # nodos de un CATALOGO DE REFERENCIA ajeno puestos ahi para calibrar la aduana
    # ...
    # EL CRITERIO NO ES UNA LISTA DE NOMBRES ... **entra en la poblacion el
    # candidato cuyas fuentes estan TODAS en la tabla canonica vigente.**

`D.38.4` dice `cuarentena/<libro>/`, y `ensayo_referencia_163` **no es un libro**: no esta en
el tablero, sus fuentes no estan en la tabla canonica, y la guarda `fuentes` lo tumbaria en
la puerta. **`163` fuera, `77` dentro, y `346` mas `77` son los `423` que el informe publica.**
**Es discrepancia de metodo, no de verdad**, y la digo entera porque `D.38.5` me pide
justamente cruzar las dos cifras.

### 5.2. Los nueve informes, corridos por mi, uno por candidato

**Corri `python forja.py informe` sobre los nueve, de uno en uno**, y los nueve traen la
misma linea de poblacion:

    poblacion del barrido       : 423   (346 del grafo mas 77 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

    $ (saldo leido de la linea de resumen de cada informe)
    cerrar_brecha_dos_preguntas_estrategia                     ENTRARIA=0 BLOQ=1 CAE=0 vecinos=11
    contestar_dos_preguntas_direccion_objetivos                ENTRARIA=0 BLOQ=1 CAE=0 vecinos=7
    definir_entorno_grupo_clientes_proveedores_competidores    ENTRARIA=0 BLOQ=1 CAE=0 vecinos=6
    determinar_estado_presente_capacidades_proyectos_merma     ENTRARIA=0 BLOQ=1 CAE=0 vecinos=5
    examinar_demanda_entorno_dos_marcos_temporales             ENTRARIA=0 BLOQ=1 CAE=0 vecinos=4
    examinar_entorno_expectativas_tecnologia_proveedores_grupos ENTRARIA=0 BLOQ=1 CAE=0 vecinos=6
    fijar_horizonte_ventana_replanificacion                    ENTRARIA=0 BLOQ=1 CAE=0 vecinos=3
    fijar_periodo_direccion_objetivos_retroalimentacion        ENTRARIA=0 BLOQ=1 CAE=0 vecinos=1
    repartir_supervision_puesto_funcional_mision               ENTRARIA=1 BLOQ=0 CAE=0 vecinos=0

    $ python -c "suma de vecindades"
    VECINDADES TOTALES DEL LOTE = 43

**`8` BLOQUEARIAN, `1` ENTRARIA, `0` CAERIAN, `43` vecindades.** El que entra solo es el de
`cap_10`, y entra porque **no levanta ni un vecino**.

**LECTURA, EN LINEA APARTE:** ninguna guarda muerde a ningun candidato del lote. Lo que el
lote abre no es rechazo: **es cola de lectura, y son `43` pares que alguien tendra que
veredictar el dia de la insercion.**

### 5.3. Y MI PROPIO BARRIDO REPRODUCE EL DE LA MAQUINA AL MILESIMO

Corri mi barrido **con la poblacion ANCHA a proposito** (`586` = `346` mas los `240`
ficheros de carpeta, los `163` del ensayo incluidos) para ver si meterlos cambia algo:

    $ python barrido.py
    POBLACION DEL BARRIDO (D.38.4)
      grafo dataset/nodos.jsonl : 346
      bandejas cuarentena/*/    : 240
      total                     : 586
      umbral_similitud_texto    : 0.35   umbral_familia_id: 0.3

    $ python -c "cruce: similitud_texto de la aduana contra la de mi barrido"
    candidato                                                   aduana(sim)     mio(sim) identicos?
    cerrar_brecha_dos_preguntas_estrategia                                8            8 SI, al milesimo
    contestar_dos_preguntas_direccion_objetivos                           7            7 SI, al milesimo
    definir_entorno_grupo_clientes_proveedores_competidores               6            6 SI, al milesimo
    determinar_estado_presente_capacidades_proyectos_merma                5            5 SI, al milesimo
    examinar_demanda_entorno_dos_marcos_temporales                        4            4 SI, al milesimo
    examinar_entorno_expectativas_tecnologia_proveedores_grupos           6            6 SI, al milesimo
    fijar_horizonte_ventana_replanificacion                               3            3 SI, al milesimo
    fijar_periodo_direccion_objetivos_retroalimentacion                   -    NO MEDIDO (mi barrido se corto en 7 de 9)
    repartir_supervision_puesto_funcional_mision                          -    NO MEDIDO (mi barrido se corto en 7 de 9)

**SIETE DE NUEVE CRUZADOS, Y LOS SIETE SALEN IDENTICOS: mismos vecinos, mismo numero, misma
cifra al milesimo.** Los otros dos **no los mido, y digo por que en vez de dejarlo en
blanco**: lance aquel barrido con `| head -120` y la tuberia lo corto en el septimo. **Es
fallo mio de comando, no del instrumento**, y el que falta por cruzar es precisamente el que
la maquina deja entrar sin vecinos.

**LECTURA, EN LINEA APARTE:** meter los `163` del ensayo en la poblacion **no anade ni un
vecino sobre umbral a este lote**. Asi que para esta tanda la cifra de la maquina y la mia
**son la misma cifra**, que es lo que `D.38.5` me manda comprobar antes de llamar
discrepancia a nada.

---

## 6. LO QUE EL BARRIDO DESENTIERRA, Y NO ES CAIDA DE NADIE DEL BUCLE

### 6.1. **CUATRO DE LAS CINCO ARISTAS `D.37` QUE EL LOTE DECLARA NO LAS LEVANTA NADIE**

Cinco de las nueve fichas declaran, con estas palabras, que su pieza cuelga de la cabeza
`planificar_tres_pasos_demanda_estado_brecha` (`P5`) y que la arista **se cablea el dia de
la insercion porque esta vuelta no inserta**. **La cabeza vive en la bandeja, o sea DENTRO de
la poblacion del barrido.** El cruce:

    $ python -c "cruce declarada contra levantada"
    candidato                                                   vecinos    declara    levanta
    cerrar_brecha_dos_preguntas_estrategia                           11         SI         SI
    contestar_dos_preguntas_direccion_objetivos                       7         no         SI
    definir_entorno_grupo_clientes_proveedores_competidores           6         SI         no
    determinar_estado_presente_capacidades_proyectos_merma            5         SI         no
    examinar_demanda_entorno_dos_marcos_temporales                    4         SI         no
    examinar_entorno_expectativas_tecnologia_proveedores_grupos       6         SI         no
    fijar_horizonte_ventana_replanificacion                           3         no         no
    fijar_periodo_direccion_objetivos_retroalimentacion               1         no         no
    repartir_supervision_puesto_funcional_mision                      0         no         no

    declaran la arista a la cabeza      = 5
      de esos, la levanta la maquina    = 1
      de esos, NO la levanta la maquina = 4
    NO la declaran y aun asi la levantan = 1 ['contestar_dos_preguntas_direccion_objetivos']

**`1` de `5`.** Y la pieza que lo remata: **el unico que la levanta sin declararla la puntua
MAS ALTO que el unico que la declara y la levanta.**

    contestar_dos_preguntas (NO es hija de la cabeza)  similitud_texto 0.398
    cerrar_brecha           (SI es hija de la cabeza)  similitud_texto 0.355

**LECTURA, EN LINEA APARTE Y MARCADA:** en este lote **la senial esta ANTI CORRELACIONADA con
la relacion real**. No es que mida poco: es que el falso positivo puntua por encima del
verdadero positivo. **Es la figura de `d072`, ya agendada, pero con una vuelta de tuerca que
`d072` no tenia: alli la relacion la habia visto yo leyendo; aqui LA DECLARA LA PROPIA FICHA
POR ESCRITO, y aun asi la maquina no la pone en la cola.** Cuatro aristas `D.37` declaradas
que, el dia de la insercion, **nadie va a ver levantadas**.

**NO PROPONGO MOVER NINGUN UMBRAL** (`config/umbrales.json` no es del bucle, y `2` me lo
prohibe). **Lo que digo es lo que esta medido**, y se cobra el dia de la insercion: **esas
cuatro aristas se cablean a mano, porque estan escritas y no hace falta buscarlas.**

### 6.2. LA SENIAL `paso_contra_nodo` COLISIONA POR LA FORMA DE LA FRASE, NO POR LO QUE MANDA

`cerrar_brecha_dos_preguntas_estrategia` es el candidato con mas vecinos del lote (`11`), y
**cuatro de ellos los levanta `paso_contra_nodo` por encima de `0.60`**. Fui a ver que pasos
son, literalmente:

    $ python pasos.py
    [grafo] preguntar_seguimiento_hallar_huecos  paso 11 de 16:
        Pregunta: que puedes hacer para empezar a trabajar en ello?
    [grafo] responder_tres_preguntas_vocacion_directiva  paso 3 de 6:
        Hazte la segunda pregunta: me gusta hablar con la gente.
    [grafo] preparar_preguntas_entrevista_antemano  paso 3 de 12:
        Ten una lista de preguntas preparada.
    [bandeja] cerrar_brecha_dos_preguntas_estrategia  paso 3 de 7:
        Contesta la segunda pregunta: que puedes hacer para cerrar la brecha.

| vecino | senial | de que va el vecino | de que va el candidato |
|---|---|---|---|
| `preguntar_seguimiento_hallar_huecos` | **`0.645`**, la mas alta del lote | una pregunta de seguimiento en una conversacion | el paso `3` de la planificacion |
| `responder_tres_preguntas_vocacion_directiva` | `0.628` | si te gusta o no el oficio de mandar | idem |
| `preparar_preguntas_entrevista_antemano` | `0.614` | preparar una entrevista | idem |

**LAS TRES SON COLISIONES DE FORMA.** Lo que comparten es el molde de la frase: *la segunda
pregunta*, *que puedes hacer para*, *preguntas*. **Ninguna de las tres tiene nada que ver con
cerrar una brecha de planificacion**, y la mas alta de todo el lote es la que menos que ver
tiene. La cuarta, `contestar_dos_preguntas_direccion_objetivos` a `0.626`, es hermana de
lote y **tampoco es duplicado** (seccion `6.4`).

**LECTURA, EN LINEA APARTE:** **`4` de `4` vecindades de `paso_contra_nodo` de este candidato
son falsos positivos por molde de frase.** Es prima de `d058` y no la misma: `d058` mide que
el `resumen_teorico` infla `similitud_texto`; **esto es otra senial y otra causa**, el molde
interrogativo de un paso corto. **No abro pregunta de doctrina** (`D.56` congela la cola) y
**no propongo instrumento nuevo** (`7.F`): lo dejo medido.

### 6.3. LA BANDA DE `d058` EXTENDIDA A ESTE LOTE, Y LO QUE PASARIA SI SE MIDIERA COMO PROPONE

`d058` propone medir si `texto_comparable` puede dejar fuera el `resumen_teorico`, **o
comparar pasos contra pasos**. Lo mido sobre este lote, que es material nuevo:

    $ python peso.py
    AGREGADO DEL LOTE: 26336 de 33310 caracteres comparables son resumen_teorico = 79.1 por ciento

La banda por ficha va de **`76,6`** (`repartir_supervision`) a **`81,9`** (`examinar_entorno`),
y los pasos pesan entre **`12,8`** y **`20,0`** por ciento. **La banda de la vuelta `54` iba
de `54,8` a `96,2`; esta es mucho mas estrecha**, y va toda ella por encima de tres cuartos.

Y rehice las `43` vecindades **comparando pasos contra pasos**, que es la segunda mitad de lo
que `d058` propone:

    $ python pvp.py
    VECINDADES MEDIDAS = 43
    las que SEGUIRIAN sobre 0.35 midiendo PASOS CONTRA PASOS = 2
       0.365  cerrar_brecha_dos_preguntas_estrategia contra contestar_dos_preguntas_direccion_objetivos
       0.378  contestar_dos_preguntas_direccion_objetivos contra cerrar_brecha_dos_preguntas_estrategia
    media txt = 0.371 | media pasos = 0.252

**DE `43` VECINDADES QUEDARIAN `2`, Y LAS DOS SON EL MISMO PAR VISTO POR SUS DOS EXTREMOS.**

**Y AQUI VA LA MITAD QUE NO FAVORECE A LA PROPUESTA, QUE ES LA QUE HAY QUE DECIR:** ese par
que sobrevive **no es duplicado** por mi lectura, y **la unica relacion verdadera del lote que
la maquina SI encuentra hoy se caeria**: `cerrar_brecha` contra la cabeza baja de **`0.355` a
`0.221`**. Medir pasos contra pasos **limpiaria las `41` vecindades falsas y se llevaria por
delante la unica verdadera**. `d058` sigue en pie tal como esta escrita, **y este lote le
anade que su segunda via, por si sola, no basta.**

### 6.4. EL PAR QUE ME TOCA ADJUDICAR A CIEGAS, ADJUDICADO ANTES DE VER NADA

El unico par del lote que dos seniales levantan a la vez y que ademas sobrevive a las dos
formas de medir es **`cerrar_brecha_dos_preguntas_estrategia` contra
`contestar_dos_preguntas_direccion_objetivos`** (`similitud_texto 0.431` y `0.438`,
`familia_id 0.250`, `paso_contra_nodo 0.626`). **Lo adjudico leyendo los pasos, que es lo que
`6.2` y `D.19` mandan, y no la senial.**

| | `cerrar_brecha...` | `contestar_dos_preguntas...` |
|---|---|---|
| tramo | `cap_07` `L39` | `cap_07` `L71-L75` |
| seccion del libro | `STEP 3-WHAT TO DO TO CLOSE THE GAP` | `Management by Objectives` |
| sus dos preguntas son | *what do you NEED to do* contra *what CAN you do* | *where do I want to go* contra *how will I pace myself* |
| que produce | una **estrategia** | un **objetivo** y unos **resultados clave** |
| sobre que actua | la brecha entre demanda y rendimiento | la tarea concreta que tienes entre manos |

**MI ADJUDICACION: NO SON DUPLICADO Y NO SON MADRE E HIJO. SON AJENOS.** Lo unico que
comparten es **el molde de dos preguntas numeradas**, y `6.1` de mi vara lo zanja: *el tamanio
del solape no decide; decide si lo que queda fuera es procedimiento en los dos lados*. **Lo
que queda fuera es procedimiento en los dos lados y es procedimiento DISTINTO**: uno cierra
una brecha, el otro fija objetivos y ritmo. **Ni siquiera hay direccion que preguntar**,
porque ninguno anade nada al otro.

**Y LO DIGO AHORA, A CIEGAS, PARA QUE VALGA:** si el reporte los trae como par discutible,
esta es mi lectura escrita antes de conocerla.

### 6.5. Y LA FRONTERA QUE EL LOTE DECLARA, LA MAQUINA SI LA LEVANTA

`fijar_horizonte_ventana_replanificacion` y `fijar_periodo_direccion_objetivos_retroalimentacion`
se declaran mutuamente como *el vecino peligroso*, y **la maquina los pone en la cola**
(`similitud_texto 0.385` y `0.359`). **Lo que las dos fichas dicen, lo confirmo leyendo el
libro**: `L61` fija el horizonte y la cadencia de la PLANIFICACION y `L79` fija el periodo del
SISTEMA DE DIRECCION POR OBJETIVOS, **y el libro los separa con el rotulo de `L67`**
(`Management by Objectives: The Planning Process Applied to Daily Work`), que lei yo. **No son
duplicado: son dos periodos de dos objetos distintos, y el segundo se contrasta contra el
primero, que es justo lo que el paso `5` de `fijar_periodo` hace.**

**Esto es el contraejemplo de `6.1` y por eso lo escribo:** la maquina no esta ciega. **Ve las
fronteras que comparten vocabulario y no ve las cabezas de las que cuelga un paso.**

---

## 7. LA CONDICION DE `D.58` QUE ESTA CORRIDA VUELVE A INCUMPLIR, Y QUE YA ESTA AGENDADA

**No la traigo como hallazgo nuevo: esta escrita en la deuda como `d071` desde la vuelta `54`**,
y el austero me manda no repetir lo que el registro ya dice. **Lo que si anado es el ejemplar
de HOY, medido**, porque `d071` cubre la primera apertura de esta misma corrida y **esta es la
segunda**:

    $ grep -n "MODO_INSERCION" docs/loop/loop.log | tail -1
    4173:[2026-09-20 12:08:04] arranque: rama extraccion-mundo-11, MODO_INSERCION=cuarentena

    $ tail -3 docs/loop/loop.log
    [2026-09-20 15:46:42] VUELTA 2 : APERTURA CIEGA (claude-opus-5), retirados: ...

**`D.58` dice que en regimen ligero NO hay fase ciega, NI sello, NI testigo.** La corrida
arranco en `cuarentena` a las `12:08:04` y **ha abierto DOS aperturas ciegas**: la de las
`13:06:31`, que `d071` ya mide, y **esta, la de las `15:46:42`**. **No la arreglo**: el arnes
es sede vedada por `D.45`. **Se suma al ejemplar de `d071` y sube al fundador con el.**

---

## 8. LO QUE ESTA PAGINA NO HACE

- **NO adjudico ninguna discrepancia contra el reporte**, porque no lo he visto. Lo que hay
  aqui son **clases, lecturas y mediciones mias**, para poder cruzarlas despues.
- **NO publico ninguna racha** (seccion `1.2`), **ni ninguna de las ocho citas a `REPORTE.md`
  que las fichas llevan dentro** (seccion `1.3`).
- **NO propongo mover ningun umbral, ni encargo instrumento nuevo** (`2`, `7.F`): las dos
  mediciones de `6.1` y `6.3` se quedan en medicion.
- **NO abro pregunta de doctrina nueva**: `D.56` congela la cola en `11` y lo que he medido
  cabe en `d058`, `d071` y `d072`, que ya existen.
- **NO he tocado nada del arbol** salvo este fichero. Comprobado despues de correr los nueve
  informes y los cuatro contadores:

        $ git status --porcelain
         M docs/loop/APERTURA_CIEGA.md
         D docs/loop/CREDITO_serial.jsonl
         D docs/loop/REPORTE.md
         M docs/loop/loop.log
         M docs/loop/ultimo_apertura.json
         D docs/loop/ultimo_auditor.json
         D docs/loop/ultimo_extractor.json

  **Ni `dataset/`, ni `bitacora/`, ni `censos/`, ni `config/`, ni `cuarentena/`, ni `src/`, ni
  `esquema/`, ni `scripts/`, ni `tests/`, ni `hooks/`, ni el banco.** La unica `M` mia es la de
  esta pagina. Las `D` son los cuatro que el arnes retira, y `loop.log` y `ultimo_apertura.json`
  los toco el arnes al abrir la fase, a las `15:46:42`, antes de que yo escribiera nada.

  **Y LOS NUEVE INFORMES NO ESCRIBEN EN EL ARBOL**, que es lo que el propio instrumento
  promete y lo compruebo en vez de creerlo: corri los nueve y el `git status` de arriba es el
  de despues.
- **Y NO COMMITEO**: el arnes sella este fichero y lo commitea el.

---

## 9. EL SALDO DE MI FASE CIEGA, EN CINCO LINEAS

| | |
|---|---|
| **acta anterior** | leida y **remedida** por su huella: `dfef6f9f...` coincide |
| **heredados** | el arnes entrega `0`; **el acta escribe `1` y el arnes no lo saca de la cita**. `HEREDADO 1: CUMPLIDO` |
| **clases** | `9` de `9` PROCEDIMIENTO. **Cero discrepancias de clase** |
| **fidelidad `D.30`** | `2` pasos de `55` que yo leo PUENTE, los dos declarados con su linea del libro. `cap_07` **`4,26`** por ciento, `cap_10` **`0,00`** |
| **barrido** | `423` de poblacion, `43` vecindades, `8` BLOQUEARIAN, `1` ENTRARIA, `0` CAERIAN. Mi barrido reproduce el de la maquina **al milesimo en `7` de `9`** |
| **lo que mas vale** | **`1` de `5` aristas `D.37` declaradas las levanta la maquina**, y el falso positivo puntua por encima del verdadero |

**ACTA ANTERIOR LEIDA: dfef6f9fea7cf2f1a75ec8b6733c8724cd989ee7**
