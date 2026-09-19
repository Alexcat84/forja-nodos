# APERTURA CIEGA DE LA VUELTA 7 DEL ARNES (vuelta 51 de la linea), lote 7 `grove_high_output`, `cap_05`: **clasifico por mi los seis candidatos, les cuento los pasos contra el libro, y mido la aduana que ellos declaran**

*Linea **serial** (`extraccion-mundo-11`), fase ciega del auditor. Escrita antes de que el arnes
me exponga el reporte. Modo austero (`D.47`): no repito lo que el registro ya dice.*

> **LAS CUATRO DECLARACIONES QUE EL ARNES EXIGE ANTES DE QUE YO ESCRIBA EL ACTA** (`D.40`), y
> cada una con su instrumento debajo en la seccion que la sostiene:

    ACTA ANTERIOR LEIDA: e508a1a9cbb136bb27e08cccf7ba2bcfac61ccce
    HEREDADO 1: CUMPLIDO
    HEREDADO 2: CUMPLIDO
    HEREDADO 3: CUMPLIDO

---

## AC.1. LA HUELLA DEL ACTA ANTERIOR, COMPROBADA Y NO COPIADA

La huella que el prompt me entrega es `e508a1a9cbb136bb27e08cccf7ba2bcfac61ccce`. La saco del
arbol con el instrumento de git y la comparo:

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    e508a1a9cbb136bb27e08cccf7ba2bcfac61ccce

    $ wc -l docs/loop/ACTA_AUDITOR.md
    37718 docs/loop/ACTA_AUDITOR.md

    $ grep -c '^# ACTA ' docs/loop/ACTA_AUDITOR.md
    49

Esa salida mide la huella del fichero `docs/loop/ACTA_AUDITOR.md` tal como esta en el arbol hoy,
sus lineas, y cuantas cabeceras de acta contiene.

`LECTURA`: la huella del arbol y la del prompt son la misma cadena de 40 caracteres, asi que el
acta que abri es la que el prompt nombra y no otra version. **El acta de cola es la `ACTA 49`, que
audita la vuelta 50**, y por tanto la que yo escriba al cerrar este turno es la `ACTA 50` y audita
la vuelta 51. La abri y la lei, que es lo que `D.40` me autoriza a hacer en esta fase.

## AC.2. LO QUE EL ARNES ME RETIRO, DICHO POR EL ARNES Y NO POR MI

`loop.log` no se retira, asi que la linea de mi propio turno se puede abrir y comprobar:

    $ grep -n 'VUELTA 7 : APERTURA CIEGA' docs/loop/loop.log
    3616:[2026-09-19 15:29:23] VUELTA 7 : APERTURA CIEGA (claude-opus-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl

    $ git status --porcelain docs/loop/
     M docs/loop/APERTURA_CIEGA.md
     D docs/loop/CREDITO_serial.jsonl
     D docs/loop/REPORTE.md
     M docs/loop/loop.log
     M docs/loop/ultimo_apertura.json
     D docs/loop/ultimo_auditor.json
     D docs/loop/ultimo_extractor.json

Esas dos salidas miden la linea que el arnes escribio para este turno y el estado del arbol de
`docs/loop/` frente al commit de cabeza.

`LECTURA`: **los cuatro que el arnes declara retirados estan los cuatro con la `D` de borrado**, y
la `M` de `APERTURA_CIEGA.md` es esta pagina, que el arnes retiro del arbol y que yo estoy
escribiendo ahora, asi que su marca de estado es la de mi propia escritura. **No recupero ninguno de git**, y esta pagina no cita ni una linea de ellos.

### AC.2.a. **LA CONSECUENCIA QUE TENGO QUE DECLARAR EN VEZ DE CALLARLA**: un instrumento de la casa no puede correr en esta fase

`docs/loop/CREDITO_serial.jsonl` es el registro que `forja.py credito` lee, y esta retirado. Asi
que el instrumento corre y contesta esto:

    $ python forja.py credito
    CREDITO DE LA LINEA 'serial' (D.48)
      registro: docs/loop/CREDITO_serial.jsonl

      LINEA SIN REGISTRO: no hay ningun suceso escrito.
      Una linea sin tandas NACE CON SU RACHA EN CERO y no hereda
      la de nadie (D.48). Lo que herede el arnes sera CERO remedios.

Esa salida mide lo que el instrumento imprime cuando su registro no esta en el arbol.

`LECTURA`: **esa salida NO es el estado de las rachas de esta linea: es el efecto de que el arnes
retirase el registro para mi fase ciega**, declarado por el arnes en la linea de mi turno que
acabo de pegar. **Por eso esta pagina no publica ni una cifra de racha**, y las rachas se leen en
mi turno normal, cuando el registro vuelva al arbol. Lo escribo porque el fallo simetrico ya me
costo una caida: la `ACTA 43` publico que el registro habia salido del arbol **y que nadie lo
habia declarado**, y el arnes lo declaraba.

## AC.3. EL ESTADO DEL ARBOL, MEDIDO POR MI HOY Y DESPUES DE QUE LA VUELTA 51 ESCRIBIERA

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1087 total

    $ ls cuarentena/grove_high_output/*.json | wc -l
    50

    $ ls cuarentena/*/*.json | wc -l
    218

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

Esas salidas miden las lineas de las tres sedes de estado, las fichas de la bandeja del libro, las
fichas de todas las bandejas, y las dos guardas de una linea corridas por mi sobre el arbol de hoy.

`LECTURA`: **de las cuatro guardas que `D.55` deja bloquear, las dos de una linea salen verdes**, y
las otras dos (las pruebas de aceptacion y la fidelidad `D.30` del capitulo) las corro en mi turno
normal porque piden minutos que esta fase gasta en el barrido de vecinos. **`dataset/nodos.jsonl`
se queda en `346` y `bitacora/VEREDICTOS.jsonl` en `740`**, que es lo que el encargo de la vuelta
51 puso como la caida que buscar: si una de las dos se hubiera movido, habria entrado un nodo con
la puerta de `D.39` cerrada.

## AC.4. LO QUE LA VUELTA 51 TOCO, LEIDO DEL ARBOL Y NO DE SU REPORTE

    $ git diff --name-status 3061fc2 b04ac62 -- cuarentena/
    M  cuarentena/grove_high_output/buscar_regularidad_bloques_iguales_trabajo_mando.json
    A  cuarentena/grove_high_output/cubrir_indicadores_problemas_reunion_individual.json
    M  cuarentena/grove_high_output/dimensionar_numero_subordinados_medio_dia_semanal.json
    A  cuarentena/grove_high_output/fijar_duracion_lugar_reunion_individual.json
    A  cuarentena/grove_high_output/fijar_frecuencia_reunion_individual_madurez_tarea.json
    A  cuarentena/grove_high_output/infundir_regularidad_reunion_proceso.json
    A  cuarentena/grove_high_output/preparar_guion_reunion_individual_subordinado.json
    M  cuarentena/grove_high_output/preparar_respuestas_estandar_interrupciones_repetidas.json
    A  cuarentena/grove_high_output/usar_tres_clases_reunion_proceso.json

    $ git diff --name-only 3061fc2 -- dataset/ bitacora/ censos/ config/ esquema/ src/ scripts/ tests/ hooks/ docs/BANCO_DE_REGLAS.md
    (vacio: ni un fichero)

Esa salida mide que ficheros de `cuarentena/` cambiaron entre el commit de apertura de la vuelta 51
y su commit de cierre, y que ficheros cambiaron en las sedes de dato entre esa apertura y el arbol
de hoy.

`LECTURA`: **seis fichas nuevas y tres corregidas, y cero ficheros movidos en las sedes de dato.**
Las seis nuevas son las seis piezas que mi encargo fijo (`P6`, `P7`, `P11`, `P12`, `P13`, `P14`), y
las tres corregidas son las tres que mi `TAREA 1.c` y mi `TAREA 3` nombraban. **La especie `DATO
MOVIDO` sale limpia por medida y no por confianza**, y lo mismo el *cero inserciones* del encargo.

### AC.4.a. Que dice el instrumento de poblacion, capitulo a capitulo

    $ python .v49aud/01_poblacion.py   (cola de la salida)
    cap_02 : 7 fichas en la bandeja
    cap_03 : 15 fichas en la bandeja
    cap_04 : 22 fichas en la bandeja
    cap_05 : 6 fichas en la bandeja

Esa salida mide, para cada ficha de la bandeja del libro, el capitulo que declara en su propio
`resumen_teorico`, y las agrupa.

`LECTURA`: **`cap_05` estrena con `6` fichas y `cap_04` se queda en `22`**, que es el reparto que
mi encargo fijo antes de empezar. `7` mas `15` mas `22` mas `6` dan las `50` de `AC.3`.

---

# AC.5. MI CLASIFICACION DE LOS SEIS CANDIDATOS, HECHA POR MI Y A CIEGAS

**COMO LA HICE, Y EN QUE ORDEN**, porque el orden es lo que la hace ciega: abri las seis fichas de
la bandeja, les saque los pasos con un instrumento, **lei los ocho renglones de `cap_05.md` que las
sostienen antes de leer una sola linea de lo que las fichas dicen de si mismas**, adjudique con la
vara de `AUDITOR_FORJA.md` 6.1, y **solo despues** abri los `resumen_teorico` para ver que decian.
**No abri `.v51/`**, que es el cuaderno de la vuelta, y lo declaro aqui como decision: sus informes
de aduana son la prueba del extractor y los cruzo en mi turno normal, no en esta fase.

## AC.5.a. Los pasos, contados por el instrumento y no por mi

    $ python .v51aud/03_pasos_cap05.py
    ficha                                                pieza   pasos
    infundir_regularidad_reunion_proceso                 P6          8
    usar_tres_clases_reunion_proceso                     P7          4
    fijar_frecuencia_reunion_individual_madurez_tarea    P11        10
    fijar_duracion_lugar_reunion_individual              P12        10
    preparar_guion_reunion_individual_subordinado        P13         7
    cubrir_indicadores_problemas_reunion_individual      P14        10
    TOTAL DE PASOS DE LAS SEIS FICHAS DE cap_05                     49

Esa salida mide cuantos elementos tiene `pasos_accionables` en cada una de las seis fichas, y su
suma.

## AC.5.b. Las palabras de cada tramo, recomputadas por mi hoy

    $ python .v51aud/05_palabras_tramos.py
    tramo            palabras
    L21 a L21             124
    L23 a L23              18
    L33 a L35             187
    L37 a L39             195
    L41 a L41             145
    L43 a L43             134
    suma de los seis      803

Esa salida mide las palabras de cada rango de lineas de `fuentes/grove_high_output/cap_05.md` con
`sed` mas `wc -w`, y su suma.

`LECTURA`: **las seis cifras coinciden al digito con las que mi propia frontera de la vuelta 50
publico** (`.v50/frontera_cap_05.txt`, filas `P6`, `P7`, `P11`, `P12`, `P13` y `P14`), y coinciden
tambien con las que las seis fichas declaran en su renglon de cabecera. **La frontera que mi
encargo mando usar se reproduce sin que yo la reabra.**

## AC.5.c. Los ocho renglones del libro que sostienen los seis nodos

    $ sed -n '21p;23p;33p;35p;37p;39p;41p;43p' fuentes/grove_high_output/cap_05.md | cut -c1-120
      (LA SALIDA VA CORTADA A 120 CARACTERES POR COLUMNA, Y LO DECLARO: son 8 renglones de 8)
    To make the most of this kind of meeting, we should aim to infuse it with regularity. In other words, the people attendi
    At Intel we use three kinds of process-oriented meetings: the one-on-one, the staff meeting, and the operation review.
    How often should you have one-on-ones? Or put another way, how do you decide how often somebody needs such a meeting? Th
    Another consideration here is how quickly things change in a job area. In marketing, for example, the pace may be so rap
    How long should a one-on-one meeting last? There really is no answer to this, but the subordinate must feel that there i
    Where should a one-on-one take place? In the supervisor’s office, in the subordinate’s office, or somewhere else? I 
    A key point about a one-on-one: It should be regarded as the subordinate’s meeting, with its agenda and tone set by hi
    What should be covered in a one-on-one? We can start with performance figures, indicators used by the subordinate, such 

    $ sed -n '21p;23p;33p;35p;37p;39p;41p;43p' fuentes/grove_high_output/cap_05.md | wc -l
    8

Esa salida mide los ocho renglones de origen de los seis nodos, cortados por columna, y su cuenta.

## AC.5.d. **MI LECTURA DE FIDELIDAD `D.30`, PASO A PASO Y CONTRA EL RENGLON**

Lei los `49` pasos contra su renglon. **Esto es una `LECTURA` mia y no una cifra de instrumento**:
lo que el instrumento cuenta son los `49`, y quien decide si un paso es transcripcion o puente soy
yo leyendo.

| ficha | pieza | pasos | mi lectura `D.30` | donde mire |
|---|---|---:|---|---|
| `infundir_regularidad_reunion_proceso` | `P6` | `8` | **8 TRANSCRIPCION, 0 PUENTE** | `L21` entero, frase a frase: la regularidad, las tres cosas que los asistentes tienen que saber, la tanda, el pronostico, el sistema de control y su efecto |
| `usar_tres_clases_reunion_proceso` | `P7` | `4` | **4 TRANSCRIPCION, 0 PUENTE** | `L23`, que cabe en un renglon: la cuenta `three kinds` y los tres nombres |
| `fijar_frecuencia_reunion_individual_madurez_tarea` | `P11` | `10` | **10 TRANSCRIPCION, 0 PUENTE** | `L33` para los pasos 1 a 7 y `L35` para los 8 a 10 |
| `fijar_duracion_lugar_reunion_individual` | `P12` | `10` | **10 TRANSCRIPCION, 0 PUENTE** | `L37` para los pasos 1 a 4 y `L39` para los 5 a 10 |
| `preparar_guion_reunion_individual_subordinado` | `P13` | `7` | **7 TRANSCRIPCION, 0 PUENTE** | `L41` entero, incluida la aritmetica de los ocho subordinados |
| `cubrir_indicadores_problemas_reunion_individual` | `P14` | `10` | **10 TRANSCRIPCION, 0 PUENTE** | `L43` entero, con sus tres ejemplos de indicador y sus cuatro clases |
| | | **`49`** | **`49` TRANSCRIPCION, `0` PUENTE** | |

`LECTURA`: **FIRMO el `0` PUENTE de los `49` pasos de esta tanda**, leidos por mi contra el renglon
antes de abrir lo que las fichas dicen de si mismas. `PASOS INVENTADOS POR CAPITULO` de `cap_05`
me sale `0` de `49`, o sea `0,00` por ciento, y la fila la cierro en mi acta con el reporte delante.

### AC.5.e. **LOS DOS SITIOS DONDE UN PASO DICE ALGO QUE SU RENGLON NO ESCRIBE**, y por que aun asi los firmo

Son dos marcos anadidos, no dos contenidos inventados, y los dejo escritos para que se puedan
discutir contra mi:

| # | donde | que anade el paso | por que lo firmo |
|---|---|---|---|
| `1` | `P7`, paso `1` | escribe *las reuniones de proceso que se usan son de tres clases*, y `L23` escribe `At Intel we use three kinds` | la cuenta y los tres nombres estan en el renglon; lo que el paso deja fuera es el sujeto `At Intel`, que es la casa del caso y no la regla (manual 3.5). **El titulo de la ficha si dice que es el libro quien las cuenta** |
| `2` | `P11`, paso `1` | escribe *en vez de poner la misma frecuencia para todas*, y `L33` no escribe esa contraposicion | el renglon la sostiene por sus dos extremos: `frequently (for example, once a week)` con el inexperto y `less frequently (perhaps once every few weeks)` con el veterano. **La frase anadida es el resumen de esos dos extremos**, no un dato nuevo |

`LECTURA`: **los dos son marco y no contenido**, asi que mi `0` PUENTE se sostiene; pero los marco
porque si un lector estricto los tumba, **caen dentro de lo que yo mismo marque** y no fuera.

---

# AC.6. **MI CLASE PARA CADA PAR, ADJUDICADA LEYENDO LOS PASOS Y NO LA SENIAL** (`D.19`, vara 6.1)

**EN QUE ORDEN LO HICE, Y LO DIGO PORQUE IMPORTA:** los seis candidatos hablan de la reunion
individual y de la reunion de proceso, y el grafo ya trae reuniones individuales de otro libro. Asi
que **abri los nodos del grafo y les lei los pasos enteros ANTES de que mi barrido terminase**. La
senial dijo despues donde mirar, y esta en `AC.7`. **La clase la pongo por la lectura.**

## AC.6.a. Los tres nodos del grafo que hablan de la misma reunion

    $ python .v51aud/10_vecinos_zhuo.py
    dirigir_reunion_individual_semanal         en el grafo: SI   libro: zhuo_manager   pasos: 10
    preguntar_conducir_reunion_individual      en el grafo: SI   libro: zhuo_manager   pasos: 7
    auditar_calendario_reuniones_semana        en el grafo: SI   libro: zhuo_manager   pasos: 10
    
    EL PAR QUE SE CONTRADICE, LOS DOS PASOS IMPRESOS DE SU FICHERO:
      paso 1 de cubrir_indicadores_problemas_reunion_individual (cuarentena, cap_05 L43):
        Empieza por las cifras de rendimiento, o sea los indicadores que usa el subordinado, como los ritmos de pedidos entrantes, la produccion o el estado de los proyectos.
      paso 4 de dirigir_reunion_individual_semanal (dataset/nodos.jsonl, zhuo_manager):
        Centrala en tu persona a cargo y en lo que la ayudaria a tener mas exito, no en ti y en lo que tu necesitas. Si lo que buscas es un parte de situacion, usa otro canal: el tiempo a solas es escaso y se aprovecha mejor en los temas que son mas dificiles de tratar en grupo o por correo.

Esa salida mide tres cosas: que los tres ids que las fichas de `cap_05` nombran como vecinos del
grafo estan en `dataset/nodos.jsonl`, el libro y los pasos de cada uno, y el texto literal de dos
pasos, uno de un candidato de hoy y otro del nodo del grafo, impresos de sus respectivos ficheros.

`LECTURA`: **los tres estan y los tres vienen de `zhuo_manager`**, asi que las tres aristas que las
fichas declaran hacia el grafo apuntan a nodos que existen. **Una busqueda negativa no se puede
citar** (`1.1`), y esta es positiva: los abri y los lei.

## AC.6.b. **LO QUE DECIDE, PAR POR PAR**, con la vara de `6.1` y su fila citada

| par | lo que el hijo trae que la madre no | mi clase | fila de la vara |
|---|---|---|---|
| `fijar_frecuencia_reunion_individual_madurez_tarea` contra `dirigir_reunion_individual_semanal` | **un CRITERIO y una frecuencia VARIABLE** (madurez relevante para la tarea, semanal con el inexperto, cada pocas semanas con el veterano) donde el del grafo pone **un suelo fijo** (*no menos de una por semana*) | **SANO, y FRONTERA DECLARADA** | *DOS DOCTRINAS LEGITIMAS NO SON DUPLICADO: son FRONTERA DECLARADA* |
| `fijar_duracion_lugar_reunion_individual` contra `dirigir_reunion_individual_semanal` | **una hora de suelo y el SITIO** (el area de trabajo del subordinado, con las cuatro cosas que ahi se ven) donde el del grafo pone **treinta minutos, y el sitio no aparece en sus diez pasos** (`AC.6.d`) | **SANO, y FRONTERA DECLARADA** | la misma, y ademas *NO TIENE BASCULA*: lo que queda fuera es procedimiento en los dos lados |
| `preparar_guion_reunion_individual_subordinado` contra `dirigir_reunion_individual_semanal` | **QUIEN prepara y con que artefacto** (el guion lo prepara el subordinado, con la razon aritmetica de los ocho) donde el del grafo **reparte la preparacion entre los dos** y da cuatro ideas de contenido | **SANO, y FRONTERA DECLARADA** | *TIENE DIRECCION*: pregunto que anade el hijo a la madre |
| `cubrir_indicadores_problemas_reunion_individual` contra `preguntar_conducir_reunion_individual` | **los ASUNTOS que se cubren** (indicadores, lo ocurrido desde la anterior, el problema potencial) donde el del grafo pone **las preguntas del que dirige**, en tres grupos | **SANO** | *NOMBRAR NO ES PROCEDIMENTAR*, y los dos traen procedimiento propio |
| `infundir_regularidad_reunion_proceso` contra `agrupar_interrupciones_subordinados_reuniones_regulares` (bandeja, `cap_04`) | **el DISENO de la reunion** para que la regularidad exista, donde el de la bandeja **agrupa las interrupciones** en una reunion que ya es regular | **SANO** | *LA ARISTA NO EXCULPA*: hay relacion y no hay paso comun |
| `usar_tres_clases_reunion_proceso` contra `subir_productividad_gerencial_tres_vias` (bandeja, `cap_04`) | **la cuenta y los nombres de las tres reuniones de proceso**, que no son las tres vias de la productividad | **SANO** | *DOS DOCTRINAS LEGITIMAS*, y ademas la senial los deja en `0.3061`, por debajo del umbral |
| los `15` pares internos de los seis entre si | cada uno trae su propia pregunta del libro: que infundir, cuales son las tres, cada cuanto, cuanto y donde, de quien es, y que se trata | **SANO los `15`: son HERMANOS** | *DOS DOCTRINAS LEGITIMAS NO SON DUPLICADO* |

`LECTURA`: **mi clase es `SANO` en los `21` pares que mire, y en ninguno leo un `REPITE`.** Lo que
hay entre los seis y los tres del grafo **no es duplicado: son dos libros que mandan cosas
distintas sobre la misma reunion**, y eso la vara manda escribirlo como frontera, no fundirlo.

### AC.6.c. **LA FRONTERA QUE ENCUENTRO Y QUE SU PROPIA FICHA NO NOMBRA**

**El par es `cubrir_indicadores_problemas_reunion_individual` contra `dirigir_reunion_individual_semanal`.** Lo mido antes de leerlo:

    $ python .v51aud/11_quien_nombra_a_quien.py
    infundir_regularidad_reunion_proceso               dirigir_reun:0  preguntar_co:0  auditar_cale:1
    usar_tres_clases_reunion_proceso                   dirigir_reun:1  preguntar_co:1  auditar_cale:0
    fijar_frecuencia_reunion_individual_madurez_tarea  dirigir_reun:1  preguntar_co:1  auditar_cale:0
    fijar_duracion_lugar_reunion_individual            dirigir_reun:1  preguntar_co:0  auditar_cale:0
    preparar_guion_reunion_individual_subordinado      dirigir_reun:1  preguntar_co:0  auditar_cale:0
    cubrir_indicadores_problemas_reunion_individual    dirigir_reun:0  preguntar_co:1  auditar_cale:0

Esa salida mide cuantas veces el fichero de cada candidato de `cap_05` escribe el id de cada uno de
los tres vecinos del grafo.

**LO QUE LOS DOS TEXTOS DICEN, uno al lado del otro y sin mi opinion en medio:**

    EL PAR QUE SE CONTRADICE, LOS DOS PASOS IMPRESOS DE SU FICHERO:
      paso 1 de cubrir_indicadores_problemas_reunion_individual (cuarentena, cap_05 L43):
        Empieza por las cifras de rendimiento, o sea los indicadores que usa el subordinado, como los ritmos de pedidos entrantes, la produccion o el estado de los proyectos.
      paso 4 de dirigir_reunion_individual_semanal (dataset/nodos.jsonl, zhuo_manager):
        Centrala en tu persona a cargo y en lo que la ayudaria a tener mas exito, no en ti y en lo que tu necesitas. Si lo que buscas es un parte de situacion, usa otro canal: el tiempo a solas es escaso y se aprovecha mejor en los temas que son mas dificiles de tratar en grupo o por correo.

`LECTURA`: **los dos nodos mandan cosas contrarias sobre con que se empieza la misma reunion**: uno
manda empezar por los indicadores y el estado de los proyectos, y el del grafo manda sacar el parte
de situacion de esa reunion y llevarlo a otro canal. **De las siete fronteras que mire, esta es la
que leo como contradiccion en el acto de apertura, y las otras seis son suelos distintos o repartos
distintos**, que es otra cosa. Las siete, enteras y sin recortar: (`1`) esta, indicadores contra
parte de situacion; (`2`) el suelo de duracion, `una hora` contra `treinta minutos`; (`3`) el suelo
de frecuencia, variable contra fijo; (`4`) quien prepara, el subordinado contra los dos; (`5`) las
preguntas del que dirige contra los asuntos que se cubren; (`6`) el diseno de la reunion contra la
tanda de interrupciones; (`7`) las tres clases de reunion contra las tres vias de la productividad.
**Y la ficha de `cap_05` que la protagoniza es la que NO nombra a ese vecino**, como acaba de medir
el instrumento de arriba: `dirigir_reun:0`.

### AC.6.d. La celda que dice que el nodo del grafo no pone sitio, medida

    $ python .v51aud/31_sitio_zhuo.py
    pasos del nodo: 10
      'oficina  ' aparece en sus pasos: 0
      'despacho ' aparece en sus pasos: 0
      'area     ' aparece en sus pasos: 0
      'sitio    ' aparece en sus pasos: 0
      'lugar    ' aparece en sus pasos: 0
      'sala     ' aparece en sus pasos: 0
      'mesa     ' aparece en sus pasos: 0
      'donde    ' aparece en sus pasos: 1

Esa salida mide cuantas veces aparece cada palabra de sitio en los diez pasos del nodo
`dirigir_reunion_individual_semanal` del grafo.

`LECTURA`: **de las ocho palabras de sitio, siete dan `0` y `donde` da `1`**, y ese `donde` esta en
su paso `3` (*temas que de otro modo no saldrian nunca*), que no es un sitio de reunion. Por eso la
celda de `AC.6.b` dice que el sitio no aparece en sus pasos, **y por eso lo que `P12` trae del lado
del sitio no lo repite nadie**.

**QUE NO HAGO CON ESTO, Y POR QUE**: no la llamo caida de nadie en esta pagina. `D.56` congela la
doctrina, la sede de un veredicto es `bitacora/VEREDICTOS.jsonl` y ahi hoy no puede llegar nada
porque la puerta de `D.39` esta cerrada, y mi propia adjudicacion de `d027` dice que **una ficha de
cuarentena no es sede de `5.2`**. **Lo que hago es dejarla medida aqui**, comparar con lo que el
reporte diga cuando el arnes me lo exponga, y anotarla en `DEUDA.jsonl` en mi turno normal para que
se lea el dia del cableado con los dos textos delante.

---

# AC.7. **EL BARRIDO DE VECINOS SOBRE GRAFO MAS BANDEJAS** (`D.38.4`), CORRIDO POR MI EN ESTA FASE

Lo corro con el instrumento de la casa, **una ficha por proceso**, y la senial la calcula
`src.aduana.senal_similitud_texto` sobre `comun.texto_comparable`, que es la misma funcion que corre
la aduana: **no reimplemento la senial y no la aproximo.** La poblacion es `dataset/nodos.jsonl` mas
lo que espera en las bandejas, descartando `_insertados` y `_derivadas`.

    $ python .v49aud/07_barrido.py <ficha>   (seis corridas, una por candidato)
    $ python .v51aud/29_tallado_barrido.py   (el tallado de las seis salidas)
    ficha                                               pobl  reloj s   sobre  el vecino mas proximo y su digito
    infundir_regularidad_reunion_proceso                 399    625.1       3  0.3699 preparar_guion_reunion_individual_subord
    usar_tres_clases_reunion_proceso                     399    676.3       0  0.3359 infundir_regularidad_reunion_proceso
    fijar_frecuencia_reunion_individual_madurez_tarea    399   1032.1       4  0.5492 fijar_duracion_lugar_reunion_individual
    fijar_duracion_lugar_reunion_individual              399    964.0       3  0.5501 fijar_frecuencia_reunion_individual_madu
    preparar_guion_reunion_individual_subordinado        399   1028.4       4  0.5222 cubrir_indicadores_problemas_reunion_ind
    cubrir_indicadores_problemas_reunion_individual      399   1144.9       3  0.5298 preparar_guion_reunion_individual_subord
    
    suma de los seis relojes: 5470.8 s  (91.2 min)
    ficheros de salida enteros: 6

Esa salida mide, para cada uno de los seis candidatos, la poblacion barrida, el reloj de su barrido,
cuantos vecinos quedan por encima del umbral de la casa, y el vecino de cabeza con su digito. Las
seis salidas enteras, con sus ocho vecinos cada una, estan en `.v51aud/04_barrido_*.out`.

`LECTURA`: **la poblacion que barri son `399` nodos en las seis corridas**, que es `346` del grafo
mas las bandejas con filtro canonico, y **los `17` levantamientos por encima del umbral son los
`17` pares de los seis candidatos entre si**: `3`, `0`, `4`, `3`, `4` y `3`. **Ni un nodo del grafo
aparece en las seis listas de cabeza.**

## AC.7.a. **LOS DIECIOCHO PARES CRUZADOS DE LIBRO, MEDIDOS UNO A UNO**, porque la lista de cabeza no los trae

La lectura de `AC.6` adjudica frontera contra tres nodos de `zhuo_manager`. Si el barrido no los
levanta, **eso hay que medirlo y no suponerlo**:

    $ python .v51aud/28_pares_cruzados.py
    candidato de cap_05                                nodo del grafo (zhuo_manager)            senial pasa el umbral 0.35
    fijar_frecuencia_reunion_individual_madurez_tarea  dirigir_reunion_individual_semanal       0.0808 no
    fijar_frecuencia_reunion_individual_madurez_tarea  preguntar_conducir_reunion_individual    0.1272 no
    fijar_frecuencia_reunion_individual_madurez_tarea  auditar_calendario_reuniones_semana      0.0996 no
    fijar_duracion_lugar_reunion_individual            dirigir_reunion_individual_semanal       0.0617 no
    fijar_duracion_lugar_reunion_individual            preguntar_conducir_reunion_individual    0.1619 no
    fijar_duracion_lugar_reunion_individual            auditar_calendario_reuniones_semana      0.1418 no
    preparar_guion_reunion_individual_subordinado      dirigir_reunion_individual_semanal       0.0661 no
    preparar_guion_reunion_individual_subordinado      preguntar_conducir_reunion_individual    0.0963 no
    preparar_guion_reunion_individual_subordinado      auditar_calendario_reuniones_semana      0.1314 no
    cubrir_indicadores_problemas_reunion_individual    dirigir_reunion_individual_semanal       0.1125 no
    cubrir_indicadores_problemas_reunion_individual    preguntar_conducir_reunion_individual    0.0881 no
    cubrir_indicadores_problemas_reunion_individual    auditar_calendario_reuniones_semana      0.1196 no
    infundir_regularidad_reunion_proceso               dirigir_reunion_individual_semanal       0.1424 no
    infundir_regularidad_reunion_proceso               preguntar_conducir_reunion_individual    0.1114 no
    infundir_regularidad_reunion_proceso               auditar_calendario_reuniones_semana      0.1715 no
    usar_tres_clases_reunion_proceso                   dirigir_reunion_individual_semanal       0.0770 no
    usar_tres_clases_reunion_proceso                   preguntar_conducir_reunion_individual    0.1212 no
    usar_tres_clases_reunion_proceso                   auditar_calendario_reuniones_semana      0.1083 no

Esa salida mide la senial de la casa entre cada uno de los seis candidatos de `cap_05` y cada uno de
los tres nodos del grafo que vienen de `zhuo_manager`, y si pasa el umbral.

`LECTURA`, y es la que me hace cambiar de opinion sobre esta tanda: **los `18` pares cruzados
de libro se quedan entre `0,0617` y `0,1715`, y el umbral esta en `0,35`: la maquina NO levanta ni
uno.** De ahi salen dos cosas que van en direcciones contrarias y las escribo las dos:

1. **A FAVOR DE LA VUELTA:** las cuatro fichas del uno a uno **declararon su arista de contraste
   contra `zhuo_manager` sin que ninguna senial se lo pidiera** (`AC.6.c` lo mide: `dirigir_reun:1`
   en `P11`, `P12` y `P13`, `preguntar_co:1` en `P14`). Eso es leer los vecinos en vez de obedecer a
   la maquina, que es lo que `D.19` y el principio `4` del manual mandan.
2. **CONTRA LA VUELTA, Y ES LA MISMA MEDIDA:** la frontera de `AC.6.c` mide **`0,1125`**, y dos
   pares de hermanos que dicen cosas distintas miden **`0,5501`** y **`0,5298`**. **La senial ordena
   por como esta escrito el texto, no por lo que el texto manda hacer**, asi que el par que se
   contradice en su acto de apertura es de los que la maquina deja abajo. **Por eso la omision de
   `P14` no la cazan los tres instrumentos que corri en esta pagina** (el barrido de vecinos de
   `AC.7`, la senial de los pares cruzados de `AC.7.a` y el bloque de vigencia de `AC.9.d`), **y por
   eso la dejo escrita aqui.**

---

# AC.8. LAS TRES FICHAS QUE LA VUELTA CORRIGIO, Y SI LA CORRECCION BORRO ALGO

Mi encargo pedia tres correcciones declaradas **sin borrar** (`d044`, `d045`, `d046`, manual
principio `6`). Eso se puede medir sin leer una linea de prosa: **si nada se borro, el texto viejo
tiene que seguir siendo un PREFIJO exacto del nuevo.**

    $ python .v51aud/20_sin_borrar.py
    dimensionar_numero_subordinados_medio_dia_semanal        viejo 11576 chars, nuevo 13648, crece  2072, el viejo es PREFIJO del nuevo: True
    buscar_regularidad_bloques_iguales_trabajo_mando         viejo  6169 chars, nuevo  7997, crece  1828, el viejo es PREFIJO del nuevo: True
    preparar_respuestas_estandar_interrupciones_repetidas    viejo  6267 chars, nuevo  8242, crece  1975, el viejo es PREFIJO del nuevo: True

    dimensionar_numero_subordinados_medio_dia_semanal        claves que cambian: ['resumen_teorico']
    buscar_regularidad_bloques_iguales_trabajo_mando         claves que cambian: ['resumen_teorico']
    preparar_respuestas_estandar_interrupciones_repetidas    claves que cambian: ['resumen_teorico']

Esa salida mide, para cada una de las tres fichas corregidas, el tamano de su `resumen_teorico` en
el commit de apertura de la vuelta 51 y hoy, si el viejo es prefijo literal del nuevo, y que claves
del fichero cambian entre las dos versiones.

`LECTURA`: **las tres correcciones anaden y no borran**, medido y no creido; y **la clave que cambia
es `resumen_teorico` y nada mas**, asi que ni un paso, ni una atribucion, ni un titulo se movieron.
Eso es exactamente lo que mi `TAREA 3` compro cuando adjudico que esas dos correcciones no pagaban
una pasada de aduana: **un cambio que no toca un paso no mueve un vecino**, y aqui se puede
comprobar que no toco ninguno.

## AC.8.a. **`d044`: EL PAGO QUE MI ACTA DIJO QUE ROMPIA SU PROPIO PAGO**

La vuelta 50 escribio dentro de la ficha el comando preciso, y con ello metio la cadena del comando
en la ficha que el comando barre. Corro el comando hoy, sobre el arbol ya corregido:

    $ grep -rl "Sale de la PIEZA P34" cuarentena/ docs/
    cuarentena/grove_high_output/decir_no_trabajo_excede_capacidad.json
    cuarentena/grove_high_output/dimensionar_numero_subordinados_medio_dia_semanal.json
    cuarentena/grove_high_output/usar_calendario_herramienta_planificacion_produccion.json
    docs/loop/ACTA_AUDITOR.md
    docs/loop/DEUDA.jsonl
    docs/loop/PROMPT_SIGUIENTE.md

Esa salida mide que ficheros de `cuarentena/` y de `docs/` contienen hoy la cadena que el pago de la
vuelta 50 uso como comando.

`LECTURA`: **el comando sigue devolviendo `3` fichas de la bandeja y no `2`**, o sea que el defecto
que mi `ACTA 49` midio **sigue midiendose igual**. Y eso **NO es un pago roto esta vez**, por lo que
la ficha hace con ello, que es lo contrario de afinar el comando:

    $ (cola del resumen_teorico de la ficha de P38, .v51aud/17_p38_cola.out, recortada por mi a sus dos frases de cierre)
    LA AFIRMACION, ESCRITA CON SUS DOS IDS Y SIN NINGUN COMANDO: la pieza P34 de la frontera de
    cap_04 publicada en la vuelta 46 (HH.2.c) es la madre de DOS fichas de la bandeja de
    grove_high_output, y son estas dos, nombradas una a una: decir_no_trabajo_excede_capacidad y
    usar_calendario_herramienta_planificacion_produccion.
    COMO SE COMPRUEBA SIN BARRER NADA: cada una de esas dos fichas declara su pieza de origen en la
    primera linea de su propio resumen_teorico.

Ese pegado es el texto que la ficha de `P38` tiene hoy en la cola de su `resumen_teorico`, cortado
por mi a las dos frases que dicen que hacer, y lo declaro cortado.

**ASI QUE CORRO LA COMPROBACION QUE LA PROPIA FICHA PROPONE**, que es la prueba de si el pago cierra:

    $ python .v51aud/18_comprobacion_d044.py
    decir_no_trabajo_excede_capacidad
       UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_04.md, unidad Cap. 3, titulo textual Managerial Leverage. Sale de la PIEZA P34 de la frontera publicada en la vuelta 46 (H

    usar_calendario_herramienta_planificacion_produccion
       UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_04.md, unidad Cap. 3, titulo textual Managerial Leverage. Sale de la PIEZA P34 de la frontera publicada en la vuelta 46 (H

    dimensionar_numero_subordinados_medio_dia_semanal
       UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_04.md, unidad Cap. 3, titulo textual Managerial Leverage. Sale de la PIEZA P38 de la frontera publicada en la vuelta 46 (H

    fichas cuya PRIMERA frase declara 'Sale de la PIEZA P34': 2
    fichas cuya PRIMERA frase declara 'Sale de la PIEZA P38': 1

Esa salida mide la cabecera del `resumen_teorico` de las tres fichas, y cuantas fichas de la bandeja
entera declaran cada una de esas dos piezas **en su frase de cabecera**.

`LECTURA`: **el metodo que la ficha propone da `2` y `1`, y da `2` y `1` sobre la bandeja de hoy, que
ya tiene `50` fichas**. La diferencia con el metodo viejo no es de afinado: **el viejo contaba
coincidencias en cualquier parte del fichero y por eso se contaba a si mismo; el nuevo ancla en la
frase de cabecera, que es la que declara el origen**, y una cita de metodo escrita en la cola de
otra ficha ya no lo ensucia. **Mi lectura es que `d044` SI cierra**, y lo que queda dentro de la
ficha son las dos lineas viejas en pie, que es lo que el principio `6` manda.

**LO QUE NO PUEDO COMPROBAR EN ESTA FASE, Y LO ESCRIBO EN VEZ DE AFIRMARLO**: la ficha dice que el
metodo vive a partir de hoy en `REPORTE.md MM.1.c`, **y `REPORTE.md` es uno de los cuatro que el
arnes retiro**. No se si esa seccion existe ni que pego. **Lo verifico en mi turno normal**, y si
esa seccion no esta o no trae la salida, entonces el pago se queda sin la mitad que se saco de la
bandeja.

---

# AC.9. **LAS NUEVE CIFRAS DE SENIAL QUE LAS FICHAS LLEVAN DENTRO, Y POR QUE HOY NO SE REPRODUCEN**

Las fichas de esta tanda escriben su veredicto dentro de si mismas, con el digito de la senial que
lo levanto. Cuento esos digitos con un instrumento antes de discutir ni uno:

    $ python .v51aud/25_salvedad.py
    infundir_regularidad_reunion_proceso               digitos declarados: 0   salvedad de version de texto: NINGUNA de las siete buscadas
    usar_tres_clases_reunion_proceso                   digitos declarados: 0   salvedad de version de texto: NINGUNA de las siete buscadas
    fijar_frecuencia_reunion_individual_madurez_tarea  digitos declarados: 1   salvedad de version de texto: NINGUNA de las siete buscadas
    fijar_duracion_lugar_reunion_individual            digitos declarados: 1   salvedad de version de texto: NINGUNA de las siete buscadas
    preparar_guion_reunion_individual_subordinado      digitos declarados: 3   salvedad de version de texto: NINGUNA de las siete buscadas
    cubrir_indicadores_problemas_reunion_individual    digitos declarados: 4   salvedad de version de texto: NINGUNA de las siete buscadas

    digitos declarados en la tanda: 9, repartidos en 4 de las 6 fichas

Esa salida mide, por ficha, cuantas veces aparece el patron `similitud de texto 0,ddd` y si el texto
trae alguna de las siete salvedades que busque sobre contra que version de texto se midio.

`LECTURA`: **hay `9` digitos declarados repartidos en `4` de las `6` fichas, y `0` de los `9` traen
salvedad de version.**

## AC.9.a. Lo que la senial come, leido del codigo de la casa

    $ grep -n -A 5 "def texto_comparable" src/comun.py
    190:def texto_comparable(nodo):
    191-    """Titulo mas resumen mas pasos: el texto que mira la señal 1."""
    192-    piezas = [nodo.get("titulo") or "", nodo.get("resumen_teorico") or ""]
    193-    piezas.extend(nodo.get("pasos_accionables") or [])
    194-    return normalizar_texto(" ".join(piezas))

Esa salida mide que campos del nodo entran en el texto que la senial compara.

`LECTURA`: **el `resumen_teorico` esta dentro del texto que la senial compara.** Y el veredicto con
su digito **se escribe en ese mismo `resumen_teorico`**, asi que el digito queda escrito dentro del
objeto del que se calcula.

## AC.9.b. Y esto es lo que da al medirlo

    $ python .v51aud/24_mecanismo_senial.py
    hijo (el que declara el digito)        vecino                                  ficha     hoy invertido recortado
    preparar_guion_reunion_individual_subo infundir_regularidad_reunion_proceso    0.416  0.3604    0.3699    0.3685
    fijar_frecuencia_reunion_individual_ma infundir_regularidad_reunion_proceso    0.385  0.3536    0.3617    0.3130
    cubrir_indicadores_problemas_reunion_i infundir_regularidad_reunion_proceso    0.391  0.3442    0.3507    0.3577
    cubrir_indicadores_problemas_reunion_i preparar_guion_reunion_individual_subo  0.432  0.5298    0.5222    0.3521
    fijar_duracion_lugar_reunion_individua fijar_frecuencia_reunion_individual_ma  0.445  0.5501    0.5492    0.3954
    
    umbral de la casa (config/umbrales.json): 0.35

Esa salida mide, para cinco pares que declaran digito: el digito que la ficha escribe, la senial de
hoy con el candidato como primer argumento, la senial de hoy con los argumentos invertidos, y la
senial de hoy con las colas de los dos resumenes recortadas en su marcador de bloque.

`LECTURA`, y va en tres piezas porque son tres cosas distintas:

1. **Ni uno de los cinco digitos declarados se reproduce hoy.** Dos se quedan cortos (`0,416` contra
   `0,3604`; `0,385` contra `0,3536`) y dos se pasan por mucho (`0,432` contra `0,5298`; `0,445`
   contra `0,5501`).
2. **La causa esta medida y es el crecimiento del propio resumen:** al recortar las colas, `0,5298`
   baja a `0,3521` y `0,5501` baja a `0,3954`, o sea **se acercan a lo que la ficha declara**. Cada
   ficha midio su digito **antes** de escribirse dentro los bloques de veredicto, arista y
   correccion, y esos bloques entran en el texto que la senial compara.
3. **La senial NO es simetrica, y eso tiene una consecuencia que se ve en esta tanda:** el par
   `infundir_regularidad_reunion_proceso` contra `cubrir_indicadores_problemas_reunion_individual`
   mide `0,3507` desde un lado y `0,3442` desde el otro, **con el umbral en `0,3500` en medio**. El
   mismo par queda levantado o no segun cual de los dos sea el candidato.

## AC.9.c. **ES LA TERCERA GENERACION DE `d038`, Y LA REGLA QUE LA CUBRE YA ESTA ESCRITA POR LA PROPIA VUELTA**

`d038` fue una cita de metodo escrita dentro del objeto que el metodo barre. `d044` fue su pago, que
afino el comando y conservo el mecanismo. **Y esto de aqui es la misma figura otra vez**: un
digito calculado del texto de la ficha, escrito dentro del texto de la ficha. **La frase que lo
cubre la escribio el pago de `d044` de esta misma vuelta**, y la cito entera porque es suya:

    LA LECCION, ya en su version entera: un comando escrito dentro de su propia poblacion no se
    arregla afinandolo, se arregla sacandolo.

Ese pegado es la frase de cierre del `resumen_teorico` de la ficha de `P38` en el arbol de hoy.

`LECTURA`: **el digito de la senial es el mismo caso que el comando**, y lo que cambia es que el
objeto barrido es el texto de la ficha en vez de la carpeta que la contiene. **No abro doctrina con esto** (`D.56` la congela): lo
dejo medido aqui, lo cruzo con el reporte en mi turno normal, y **lo anoto en `DEUDA.jsonl` con su
cita**, que es lo que `D.55` manda hacer con lo que no es averia.

### AC.9.d. **Y LA MAQUINA QUE EXISTE PARA ESTO NO LLEGA A LA BANDEJA**, medido

    $ python .v51aud/27_rancios.py
    rancios que el bloque de vigencia D.15 encuentra hoy: 71
    libro de los nodos que aparecen en ellos, contados: {'scott_radical_candor': 139, 'zhuo_manager': 2, 'smart_who': 1}
    alguno de grove_high_output: no
    
    infundir_regularidad_reunion_proceso               'huella': 0   'vigencia': 0   'D.15': 0
    usar_tres_clases_reunion_proceso                   'huella': 0   'vigencia': 0   'D.15': 0
    fijar_frecuencia_reunion_individual_madurez_tarea  'huella': 0   'vigencia': 0   'D.15': 0
    fijar_duracion_lugar_reunion_individual            'huella': 0   'vigencia': 0   'D.15': 0
    preparar_guion_reunion_individual_subordinado      'huella': 0   'vigencia': 0   'D.15': 0
    cubrir_indicadores_problemas_reunion_individual    'huella': 0   'vigencia': 0   'D.15': 0

Esa salida mide cuantos rancios encuentra hoy el bloque de vigencia `D.15` corriendo
`forja.py rancios`, de que libro son los nodos que aparecen en ellos, si alguno es de
`grove_high_output`, y cuantas veces las seis fichas de `cap_05` escriben las palabras `huella`,
`vigencia` y `D.15`.

`LECTURA`: **`D.15` es la maquina de este problema** (un veredicto emitido contra un texto que ya
cambio), **y mira `bitacora/VEREDICTOS.jsonl`**, que es donde los veredictos de esta tanda no estan
todavia porque la puerta de `D.39` esta cerrada. Las seis fichas escriben `0` huellas, asi que el dia
que lleguen a su sede **no habra huella vieja contra la que comparar el texto**. De los `71` rancios
de hoy **no hay uno de `grove_high_output`**, asi que esta vuelta no anade rancios.

**Y UNA CAIDA MIA QUE ME CACE A MI MISMO, ESCRITA AQUI PORQUE PASO EN ESTA PAGINA**: mi primer
borrador de esta seccion escribio *`8` hallazgos*, porque lei la salida de `forja.py rancios` con un
`tail -n 12` y conte las lineas que vi. **Son `71`**, contadas por el instrumento de arriba. La cifra
falsa no llego a esta pagina sellada porque la medi antes de cerrarla, **y la dejo escrita porque un
recorte de salida tomado por el total es exactamente la caida que mi `ACTA 40` ya se cargo una vez**
(cuatro lineas de un `grep` que daba ocho).

---

# AC.10. EL CORTE QUE MI ENCARGO FIJO, COMPROBADO CONTRA EL ARBOL

Mi encargo de la vuelta 51 fijo seis piezas y dejo `20` nodos fuera *aunque sobre turno*. Eso se
comprueba contando que piezas trajo la bandeja, y ya esta contado en `AC.5.a`: las piezas son `P6`,
`P7`, `P11`, `P12`, `P13` y `P14`, y son `6` de `6`. **Cero piezas de `P15` en adelante.**

Y la puerta que el encargo mando medir en vez de heredar, la mido yo:

    $ python -c "..." (las claves de cerrados_en_extraccion de config/frentes.json)
    libros CERRADOS EN EXTRACCION: ['scott_radical_candor', 'smart_who', 'zhuo_manager']
    'grove_high_output' entre ellos: no

Esa salida mide que libros declara `config/frentes.json` como cerrados en extraccion, y si
`grove_high_output` es uno de ellos.

`LECTURA`: **`grove_high_output` no esta entre los tres cerrados en extraccion**, asi que la puerta
sigue cerrada para este libro y las `50` fichas de su bandeja no pueden entrar al grafo todavia.
**El *cero inserciones* de esta vuelta es lo que la puerta obliga**, y `AC.3` mide que se cumplio:
`346` y `740` sin mover.

| lo que el encargo compro | como lo compruebo | sale |
|---|---|---|
| **seis candidatos, las seis piezas fijadas** | `AC.5.a`, instrumento sobre la bandeja | **`6` de `6`, y las piezas son las seis** |
| **cero inserciones** | `AC.3` y `AC.4`, `wc -l` y `git diff` | **`346`, `740`, `1` y cero ficheros movidos** |
| **las palabras recomputadas contra la frontera** | `AC.5.b`, `sed` mas `wc -w` | **las seis al digito** |
| **fidelidad `D.30` paso a paso** | `AC.5.d`, mi lectura contra el renglon | **`49` de `49` TRANSCRIPCION, `0` PUENTE** |
| **`d044` pagada sacando el comando del objeto** | `AC.8.a`, el metodo que la ficha propone | **da `2` y `1`, y aguanta en una bandeja de `50`** |
| **`d045` y `d046` por correccion declarada sin borrar** | `AC.8`, prueba de prefijo | **`True` en las tres, y solo `resumen_teorico` cambia** |
| **aduana en el mismo acto, con su reloj** | **NO LO PUEDO COMPROBAR AQUI**: los relojes viven en `.v51/` y en el reporte | **queda para mi turno normal** |

---

# AC.11. **LO QUE NO PUEDO COMPROBAR EN ESTA FASE, ESCRITO COMO LIMITACION Y NO COMO AFIRMACION**

`AUDITOR_FORJA.md` `1.1`: una busqueda negativa no se puede citar. Asi que esto es la lista de lo que
**no** mire, con el motivo de cada cosa:

| # | lo que no compruebo | por que | cuando |
|---|---|---|---|
| `1` | **las cifras del reporte de la vuelta 51** | `docs/loop/REPORTE.md` esta retirado por el arnes (`AC.2`) | mi turno normal |
| `2` | **los relojes de las seis pasadas de aduana, y sus informes** | viven en `.v51/`, el cuaderno de la vuelta, y **decido no abrirlo en esta fase** para que mi clase sea mia | mi turno normal |
| `3` | **las rachas de credito de la linea** | su registro esta retirado, y el instrumento contesta `LINEA SIN REGISTRO` (`AC.2.a`) | mi turno normal |
| `4` | **la seccion `MM.1.c` donde `d044` dice que vive ahora su comando** | esa seccion es del reporte retirado | mi turno normal |
| `5` | **las `318` pruebas de aceptacion y el tallado** | piden minutos, y esta fase los gasto en los seis barridos (`91,2` min de reloj, `AC.7`) | mi turno normal |
| `6` | **si el reporte declaro el cierre en `6` de `26` con su cifra** (`EXTRACTOR.md` 12.4) | del reporte retirado; lo que si mido es que la bandeja trae `6` | mi turno normal |

---

# AC.12. **LOS TRES HEREDADOS, UNO A UNO Y CON SU SALIDA PEGADA**

## HEREDADO 1: **CUMPLIDO**

El remedio dice que el barrido de la fase ciega se corre **como ultima operacion, sobre la pagina ya
terminada**, y que su salida se pega **despues de todo lo demas**. **Asi esta hecho**: la seccion
`AC.13` es la de cierre de esta pagina, su salida es la del barrido corrido sobre el texto ya
terminado, y **su cabecera es la cuenta que esta pagina publica**. La comprobacion del remedio es
esa comparacion, y esta a la vista en `AC.13`.

## HEREDADO 2: **CUMPLIDO**

El remedio dice que toda frase mia que acompane a un pegado dice lo que **ese** pegado mide, y que la
conclusion va aparte y marcada `LECTURA`. **Esta pagina esta escrita asi de punta a punta**, y la
presencia se puede contar:

    $ grep -c '^`LECTURA`' docs/loop/APERTURA_CIEGA.md
    27

    $ grep -c '^Esa salida mide' docs/loop/APERTURA_CIEGA.md
    23

Esas dos salidas miden cuantas lineas de esta pagina empiezan por la marca de conclusion y cuantas
empiezan por la frase que describe un pegado, contadas sobre la pagina terminada.

`LECTURA`: **`23` pegados descritos y `27` conclusiones marcadas.** La forma que el remedio pide es
la que esta pagina usa en cada seccion con cifra: debajo del pegado va una linea que empieza por
*Esa salida mide* y no concluye nada, y lo que concluyo va en su propia linea marcada. **Que haya
`27` y no `23` es porque cuatro secciones concluyen dos veces**, una por cada cosa que el pegado
mide.

## HEREDADO 3: **CUMPLIDO, Y CON EL CASO QUE ESTA PAGINA PRODUJO**

El remedio dice que toda cifra de **estado** que yo publique se mide **despues** de la operacion que
la cambia. **Esta pagina trae un caso propio, y lo produjo ella misma**: el `grep` de
`AC.8.a` barre `docs/`, y **esta pagina vive en `docs/` y escribe esa cadena cuatro veces**. Asi que
lo vuelvo a correr **despues** de escribirla:

    $ grep -c "Sale de la PIEZA P34" docs/loop/APERTURA_CIEGA.md
    4

    $ grep -rl "Sale de la PIEZA P34" cuarentena/ docs/
    cuarentena/grove_high_output/decir_no_trabajo_excede_capacidad.json
    cuarentena/grove_high_output/dimensionar_numero_subordinados_medio_dia_semanal.json
    cuarentena/grove_high_output/usar_calendario_herramienta_planificacion_produccion.json
    docs/loop/ACTA_AUDITOR.md
    docs/loop/APERTURA_CIEGA.md
    docs/loop/DEUDA.jsonl
    docs/loop/PROMPT_SIGUIENTE.md

Esa salida mide cuantas veces esta pagina escribe la cadena, y que ficheros de `cuarentena/` y
`docs/` la contienen **con esta pagina ya escrita dentro del arbol**.

`LECTURA`: **el pegado de `AC.8.a` daba `6` ficheros y ahora da `7`, y el septimo soy yo.** La cifra
de `AC.8.a` queda como lo que era, la medida de antes de escribir esta pagina, **y la de aqui es la
de despues**, que es la que el remedio manda publicar. **Y el mecanismo es el de `d038` por cuarta
vez**: escribi la cadena dentro de un fichero que el comando barre, en mi propia sede. **Por eso el
metodo bueno es el que `AC.8.a` verifica** (anclar en la frase de cabecera de la ficha), y no contar
coincidencias sobre una carpeta que crece.

---

# AC.13. **EL BARRIDO DE LA FASE CIEGA, CORRIDO COMO OPERACION DE CIERRE SOBRE LA PAGINA TERMINADA**

Es lo que `HEREDADO 1` obliga: se corre al final, sobre el texto ya terminado, **y su salida se pega
detras de todo lo demas**. Barre mi prosa, o sea las lineas que no van sangradas con cuatro
espacios; las sangradas son salidas de instrumento y van contadas aparte.

**LO QUE CONTESTO Y LO QUE NO, dicho antes de pegar la salida:** el remedio obliga a contestar los
**superlativos**, y esos los deje en `0` reescribiendo las cinco frases que los traian. Las
**afirmaciones universales** no las pide el remedio y el instrumento las barre igual, asi que las
contesto aqui una a una **por su numero de linea**, sin repetir la palabra, para que la cuenta de
este barrido no se mueva por contestarla:

| linea | clase | donde esta sostenida |
|---:|---|---|
| `59` | negativa universal | es una afirmacion sobre mi propia conducta en esta fase, y **el arnes la comprueba por su cuenta**: si yo hubiera recuperado uno de los cuatro retirados, lo escribe en `loop.log` |
| `106` | universal afirmativa | describe el pegado de `AC.3`, que es `ls cuarentena/*/*.json | wc -l` y da `218` |
| `246` | universal afirmativa | es una cita literal del paso `1` de la ficha de `P11`, y va en cursiva como cita |
| `293` | negativa universal | es mi lectura sobre los `21` pares que la tabla de `AC.6.b` lista fila a fila, y no sobre pares que no mire |
| `349` | universal afirmativa | es una cita literal del paso `3` del nodo del grafo, pegada de su fichero en `AC.6.d` |
| `425` | negativa universal | esta medida en `AC.7.a`: los `18` pares cruzados de libro dan entre `0,0617` y `0,1715` contra un umbral de `0,35` |
| `461` | negativa universal | esta medida en `AC.8`: la prueba de claves da `['resumen_teorico']` en las tres fichas corregidas |

**Y LA SALIDA, PEGADA DETRAS DE TODO LO DEMAS:**

    $ python .v49aud/17_superlativos.py
    SUPERLATIVOS, que es lo que el remedio obliga a contestar: 0 golpes en mi prosa, 3 lineas sangradas (salida de instrumento) descartadas

    AFIRMACIONES UNIVERSALES, que no las pide el remedio y las barro igual: 7 golpes en mi prosa, 8 lineas sangradas (salida de instrumento) descartadas
       linea 59   [negativa universal        ] ninguno        ...ia escritura. **No recupero ninguno de git**, y esta pagina no...
       linea 106  [universal afirmativa      ] todas          ...fichas de todas las bandejas, y las dos gua...
       linea 246  [universal afirmativa      ] todas          ...er la misma frecuencia para todas*, y `L33` no escribe esa co...
       linea 293  [negativa universal        ] ninguno        ...s `21` pares que mire, y en ninguno leo un `REPITE`.** Lo que...
       linea 349  [universal afirmativa      ] nunca          ...ue de otro modo no saldrian nunca*), que no es un sitio de re...
       linea 425  [negativa universal        ] ninguna        ...ntra `zhuo_manager` sin que ninguna senial se lo pidiera** (`AC...
       linea 461  [negativa universal        ] ninguno        ...comprobar que no toco ninguno....

Esa salida mide los superlativos y las afirmaciones universales de mi prosa en esta pagina, corrida
sobre el texto ya terminado, con las lineas sangradas de salida de instrumento contadas aparte.

### AC.13.a. **LA CUENTA QUE ESTA PAGINA PUBLICA ES LA DE LA RELECTURA, Y AQUI ESTA SU ARITMETICA**

Al pegar la salida de arriba, **sus siete lineas de detalle pasan a ser lineas sangradas**, y el
barrido de universales las cuenta entonces como salida de instrumento. Eso cambia una de las cuatro
cifras, asi que **lo mido despues de pegarla** (`HEREDADO 3`) y corro el instrumento otra vez sobre
la pagina con su salida ya dentro:

    $ python .v49aud/17_superlativos.py   (las dos cabeceras, tras pegar la salida de arriba)
    SUPERLATIVOS, que es lo que el remedio obliga a contestar: 0 golpes en mi prosa, 3 lineas sangradas (salida de instrumento) descartadas
    AFIRMACIONES UNIVERSALES, que no las pide el remedio y las barro igual: 7 golpes en mi prosa, 15 lineas sangradas (salida de instrumento) descartadas

Esa salida mide las dos cabeceras del mismo barrido corrido sobre esta pagina con la salida de
`AC.13` ya pegada dentro.

`LECTURA`: **la cabecera de superlativos sale identica, `0` golpes y `3` lineas sangradas, y es la
que el remedio ata.** La de universales conserva sus `7` golpes y sube de `8` a `15` lineas
sangradas, **y la diferencia son las `7` lineas de detalle que acabo de pegar**: `8` mas `7` dan
`15`. **De aqui en adelante la cuenta se queda quieta**, porque lo que se pega debajo son dos lineas
de cabecera y el barrido no encuentra en ellas una sola de las palabras que busca. **Asi que el que
corra este instrumento sobre la pagina sellada tiene que obtener estas dos cabeceras**, y esa es la
cuenta que esta pagina publica.

---

*Fin de la apertura ciega. No la commiteo: la sella el arnes. El reporte de la vuelta 51 lo leo
despues, en mi turno normal, y de ese cruce sale la `ACTA 50`.*
