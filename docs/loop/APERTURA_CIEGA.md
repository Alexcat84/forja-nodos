# APERTURA CIEGA DE LA VUELTA 50 (auditor de la linea serial, `claude-opus-5`)

> **QUE ES ESTA PAGINA.** La lectura que hago **antes** de que el arnes me exponga el reporte del
> extractor, para que despues se puedan contrastar dos lecturas independientes de la misma tanda.
> Manda `D.38.3`: aqui se publican **clases y lecturas**, y **toda cifra sale de un instrumento
> corrido en esta fase con su salida pegada al lado**. Manda `D.38.4` con su correccion del 16 sep:
> el barrido de vecinos se hace sobre **grafo mas bandejas**, entregando a la aduana la poblacion
> del grafo y dejando que ella ponga las bandejas.
>
> **Y MANDA EL `HEREDADO 2` DE LA `ACTA 47`, que sigue vivo:** la frase que acompana a un pegado
> dice lo que **ese** pegado mide, y la conclusion va aparte y marcada `LECTURA`.

---

## 1. LA DECLARACION QUE EL ARNES EXIGE (`D.40`)

    ACTA ANTERIOR LEIDA: 9c1eced05cb9f9b265e2f94e3a17e188af43b185

**COMPROBADA CONTRA EL ARBOL Y NO COPIADA DEL PROMPT:**

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    9c1eced05cb9f9b265e2f94e3a17e188af43b185

La salida mide la huella `git` del fichero `docs/loop/ACTA_AUDITOR.md` tal como vive en el arbol
ahora mismo.

`LECTURA`: la huella que el prompt me entrega y la del fichero que he abierto son la misma cadena,
asi que el acta que he leido es la que el arnes nombra y no otra version.

### 1.1. LOS HEREDADOS QUE EL ARNES ENTREGA SON `0`, Y ESO ES UN HALLAZGO Y NO UN TRAMITE

    $ python forja.py herencia
      acta anterior : ACTA 48. VUELTA 49, lote 7 (`grove_high_output`), ...
      su huella     : 9c1eced05cb9f9b265e2f94e3a17e188af43b185
      heredados     : 0

    AVISO: esta acta MENCIONA remedios en 1 encabezado(s) y no ESCRIBE ninguna tabla de
    remedios fuera de cita. No se entrega ninguno, y se dice en voz alta: un arnes que
    entrega cero sin avisar es el defecto que la TAREA 2 de la vuelta 31 vino a cerrar.

    El acta anterior no dejo ninguna tarea bloqueante ni ningun remedio escrito.

La salida mide lo que el extractor de herencia de `forja.py` saca hoy del acta `48`: cero piezas,
con su propio aviso de que hay **un** encabezado de remedio que no ha sabido leer.

**Y AHORA LO QUE HE ABIERTO YO, porque `AUDITOR_FORJA.md` me manda abrir mi propia acta en esta
fase, y esta es exactamente la razon por la que me lo manda:**

    $ grep -n "TAREA BLOQUEANTE DEL AUDITOR PARA LA VUELTA 50" docs/loop/ACTA_AUDITOR.md
    37045:### 48.9.d. **MI TAREA BLOQUEANTE DEL AUDITOR PARA LA VUELTA 50** (`5.5`, escalada al penultimo escalon)

La salida mide que la cadena `TAREA BLOQUEANTE DEL AUDITOR PARA LA VUELTA 50` aparece en la linea
`37045` de `docs/loop/ACTA_AUDITOR.md`, dentro de la seccion `48.9.d`.

Y esto es lo que esa seccion escribe, pegado de su sitio:

    | **TAREA BLOQUEANTE DEL AUDITOR, vuelta 50** | **El barrido del remedio se corre COMO
    ULTIMA OPERACION de mi fase ciega, sobre la pagina ya terminada, y su salida se pega
    DESPUES de todo lo demas.** Si al pegarla escribo una linea mas de prosa, **lo vuelvo
    a correr.** La cuenta de golpes que publique tiene que ser la del fichero que el arnes
    va a sellar, **no la de una version intermedia** |
    | **como se comprueba que esta roto** | se corre `.v49aud/17_superlativos.py` (o su
    sucesor) **sobre la apertura ya sellada** y se compara su cabecera con la cuenta que la
    pagina publica. **Si no coinciden, roto**, sin discusion y sin necesidad de leer una
    sola frase |

`LECTURA`: **la tarea bloqueante existe en el acta anterior y el instrumento de herencia la entrega
como `0`.** La `ACTA 48` la escribio bajo el encabezado `MI TAREA BLOQUEANTE DEL AUDITOR PARA LA
VUELTA 50`, y las actas `35` a `42` la habian escrito como `TAREA BLOQUEANTE DEL AUDITOR, para la
ACTA N`, que es la forma que el extractor de herencia sabe leer. **La pieza no se perdio por
memoria: se perdio por forma.** Y `D.40` nacio porque `ACTA 14`, `ACTA 15` y `ACTA 16` perdieron el
mismo remedio tres veces seguidas. La recupero por la via que el propio protocolo me deja abierta,
que es leer mi acta, y la cumplo en la seccion `12` como si el arnes me la hubiera puesto delante.
Lo registro con su medida y **no abro doctrina**, que es lo que `D.56` manda hacer con una pregunta
nueva mientras el mundo `11` no cierre.

### 1.2. LA TABLA DE LO QUE HEREDO, CON SU ESTADO

| # | de donde sale | que dice | estado |
|---|---|---|---|
| **HEREDADO 1** | `ACTA 48` `48.9.d`, **recuperado por mi, no entregado por el arnes** | el barrido del remedio se corre como operacion final de mi fase ciega, sobre la pagina ya terminada, y su salida se pega despues de todo lo demas; la cuenta de golpes que publique tiene que ser la del fichero que el arnes va a sellar | **CUMPLIDO**, seccion `12` |
| **HEREDADO 2** | `ACTA 47`, citado vivo en `48.9.d` | la frase que acompana a un pegado dice lo que **ese** pegado mide, y la conclusion va aparte y marcada `LECTURA` | **CUMPLIDO**, en cada seccion de esta pagina |
| **lo que `forja.py herencia` entrega** | el arnes | `0` | **declarado en `1.1` con su instrumento pegado** |

**NO ESCRIBO NINGUN `NO APLICA`** en esta tabla, asi que no hay motivo de `NO APLICA` que sostener
con una salida pegada. Las dos filas vivas salen `CUMPLIDO` y la tercera es la cuenta del arnes con
su instrumento delante.

---

## 2. LO QUE ESTA FASE NO VE, COMPROBADO EN `loop.log` Y NO SUPUESTO

    $ tail -n 4 docs/loop/loop.log
    [2026-09-19 13:29:49] extractor listo (USD 21.398844999999994), 3006s, intento 1 de 7
    [2026-09-19 13:29:50] VUELTA 6 : APERTURA CIEGA (claude-opus-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl
    [2026-09-19 13:29:50]   hereda 0 remedio(s) del acta anterior, entregados en el prompt (D.40)
    [2026-09-19 13:29:50]   y solo eso: remedios con su motivo, sin cifras ni conclusiones (D.52)

La salida mide las cuatro lineas finales de `docs/loop/loop.log`, que el arnes acaba de escribir
para este turno.

    $ git status --short docs/loop/
     D docs/loop/APERTURA_CIEGA.md
     D docs/loop/CREDITO_serial.jsonl
     D docs/loop/REPORTE.md
     M docs/loop/loop.log
     M docs/loop/ultimo_apertura.json
     D docs/loop/ultimo_auditor.json
     D docs/loop/ultimo_extractor.json

La salida mide que cinco ficheros de `docs/loop/` estan borrados del arbol de trabajo:
`APERTURA_CIEGA.md`, `CREDITO_serial.jsonl`, `REPORTE.md`, `ultimo_auditor.json` y
`ultimo_extractor.json`.

`LECTURA`: el log nombra cuatro retirados y el arbol ensena cinco borrados, porque
`APERTURA_CIEGA.md` es la pagina que estoy escribiendo y el arnes la rota en cada vuelta. En esta
corrida el cuarto retirado es `CREDITO_serial.jsonl` en lugar de `loop.log`, **asi que el log si lo
puedo abrir y lo he abierto**, y en cambio **el credito de mi linea no lo puedo leer en esta fase**,
que queda declarado en la seccion `9`.

### 2.1. LO QUE NO HE ABIERTO, DICHO POR SU NOMBRE

No he recuperado de `git` ni por ninguna otra via `REPORTE.md`, `ultimo_extractor.json`,
`ultimo_auditor.json` ni `CREDITO_serial.jsonl`. **Y tampoco he abierto `.v50/`**, la carpeta de
trabajo que el extractor commiteo en esta vuelta: sus ficheros no estan en la lista de `D.34.2`,
pero `.v50/informe_01.txt`, `.v50/vecinos_p41.txt` y sus vecinos **son la medida del extractor sobre
este mismo lote**, y abrirlos seria leer la lectura que vengo a contrastar a ciegas. De esa carpeta
he tomado los nombres de fichero, que salen del `git diff` de la seccion `4`, y nada de su interior.

**SI he abierto `.v46/frontera.py`**, el instrumento de la frontera de `cap_04`, escrito en la
vuelta `46` y citado dentro de las propias fichas: es un instrumento de la casa de cuatro vueltas
atras, no mide la tanda de hoy, y lo corro yo mismo en la seccion `6`.

---

## 3. EL ESTADO DEL ARBOL, CON SUS INSTRUMENTOS

    $ git rev-parse HEAD
    216b114449de15ae97360cf84e850b23a85afb16

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
       1086 total

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python forja.py resolutor
    nodos vivos: 346
    nodos deprecados (archivo): 0
    alias registrados: 0

    $ python forja.py rancios | grep -c RANCIO
    72

Las salidas miden, por ese orden: el `HEAD` del arbol; las lineas de `dataset/nodos.jsonl` y de
`bitacora/VEREDICTOS.jsonl`; el gate con sus trece guardas; el barrido de estilo; el resolutor de
ids; y la cuenta de lineas que el bloque de vigencia `D.15` imprime con la marca `RANCIO`.

`LECTURA`: el grafo trae `346` nodos y la bitacora `740` lineas. Los `72` rancios salen de la
familia `pedir_critica_primero_crear_seguridad_psicologica` y `dar_elogio_disciplina_igual_critica`,
que son nodos de `scott_radical_candor` y no de la tanda de hoy; `D.15` dice de forma expresa que
esto no pone el gate en rojo.

### 3.1. LA POBLACION DEL BARRIDO DE VECINOS (`D.38.4`, con su cuenta pegada)

    $ ls cuarentena/*/*.json | grep -v _insertados | grep -v _derivadas | grep -v ensayo_referencia_163 | wc -l
    47

    $ for d in cuarentena/*/; do printf "%6s  %s\n" "$(ls $d*.json 2>/dev/null | wc -l)" "$d"; done
         2  cuarentena/_derivadas/
         0  cuarentena/_insertados/
       163  cuarentena/ensayo_referencia_163/
        44  cuarentena/grove_high_output/
         3  cuarentena/marquet_turn_the_ship/
         0  cuarentena/onu_consumidor/
         0  cuarentena/scott_radical_candor/
         0  cuarentena/smart_who/
         0  cuarentena/zhuo_manager/

Las salidas miden los ficheros `json` de `cuarentena/` por carpeta, descartando `_insertados`,
`_derivadas` y `ensayo_referencia_163` como `D.38.5` manda.

`LECTURA`: la poblacion del barrido es `346` del grafo mas `47` de bandejas, o sea `393`, y `392`
por candidato, porque un nodo no es vecino de si mismo (`ACTA 18`). Los `163` de
`ensayo_referencia_163` quedan fuera por el criterio de fuentes de `D.38.5`, que no es una lista de
carpetas. **Esta cifra la cruzo contra la que la aduana imprime, en la seccion `8`.**

### 3.2. LAS PRUEBAS DE ACEPTACION SALEN CON CUATRO EN ROJO, Y LAS CUATRO SON DE ESTA FASE

    $ python tests/test_aceptacion.py
      total: 318 pruebas, 3 fallos, 1 errores

    ERROR: test_el_reporte_vivo_pasa_su_propia_guarda (__main__.PruebaTablaDeCierre)
      File "C:\Users\AlexDesk\Documents\forja-nodos\src\comun.py", line 80, in leer_texto
        with io.open(ruta, "r", encoding="utf-8") as f:
    FileNotFoundError: [Errno 2] No such file or directory:
      'C:\\Users\\AlexDesk\\Documents\\forja-nodos\\docs\\loop\\REPORTE.md'

    FAIL: test_la_linea_serial_del_repo_tiene_su_registro_escrito (PruebaHerenciaPorLinea)
    AssertionError: False is not true : docs/loop/CREDITO_serial.jsonl sin tandas: la
      migracion de D.48 no esta en el arbol

    FAIL: test_caso_positivo_un_frente_recien_nacido_hereda_cero (PruebaHerenciaPorLinea)
    FAIL: test_el_aviso_nombra_la_linea_y_su_registro (PruebaHerenciaPorLinea)
    AssertionError: 'libro_que_nunca_dicto_nada' not found in ''

    Ran 318 tests in 118.789s
    FAILED (failures=3, errors=1, skipped=1)

La salida mide `318` pruebas con `3` fallos, `1` error y `1` saltada, y sus trazas nombran dos
ficheros: `docs/loop/REPORTE.md` y `docs/loop/CREDITO_serial.jsonl`.

`LECTURA`: los dos ficheros que las trazas nombran son **dos de los cuatro que el arnes retiro para
esta fase**, segun la linea de `loop.log` pegada en la seccion `2`. **La suite de aceptacion no
puede salir verde dentro de una apertura ciega**, y por eso no cargo estos cuatro rojos contra la
vuelta `50`: el rojo lo produce la retirada, no el trabajo. Es la figura de `D.33`, artefacto de
maquina. Lo dejo escrito como observacion medida y **no encargo maquinaria** (`5.5`, moratoria
`7.F`, y `D.45` mientras corran frentes en paralelo).

---

## 4. QUE LOTE ES ESTE, MEDIDO EN EL ARBOL Y NO SUPUESTO

    $ git log --format='%h %ad %s' --date=format:'%H:%M:%S' -n 5
    216b114 13:27:55 VUELTA 50: cap_04 cerrado en 22 de 22 con P41, P42 y P44 por su aduana en el acto, d036 y d038 pagadas, y la frontera de cap_05 publicada
    55cd182 13:16:30 Vuelta 50, cap_04: candidato 3 de 3 (P44), capitulo cerrado en 22 de 22, y d036 y d038 pagadas con nueve correcciones declaradas
    adb5c9d 13:09:16 Vuelta 50, cap_04: candidato 2 de 3 (P42) escrito y pasado por su aduana en el acto, cero inserciones
    f717235 13:02:16 Vuelta 50, cap_04: candidato 1 de 3 (P41) escrito y pasado por su aduana en el acto, cero inserciones
    e740b2f 12:46:37 Apertura de la vuelta 50, con el esqueleto y la puerta de D.39 medida cerrada

    $ git diff --name-status 0ab7b6c..HEAD -- cuarentena/ dataset/ bitacora/ censos/
    A       cuarentena/grove_high_output/agrupar_interrupciones_subordinados_reuniones_regulares.json
    M       cuarentena/grove_high_output/buscar_actividad_alta_palanca_tres_vias.json
    A       cuarentena/grove_high_output/canalizar_interrupciones_cartel_hora_oficina.json
    M       cuarentena/grove_high_output/dimensionar_numero_subordinados_medio_dia_semanal.json
    M       cuarentena/grove_high_output/elegir_momento_actividad_palanca_maxima.json
    M       cuarentena/grove_high_output/empujar_persona_reunion_direccion_preferida.json
    M       cuarentena/grove_high_output/escalonar_fuentes_informacion_gerencial.json
    A       cuarentena/grove_high_output/preparar_respuestas_estandar_interrupciones_repetidas.json
    M       cuarentena/grove_high_output/programar_visita_area_observar_despachar.json
    M       cuarentena/grove_high_output/reunir_informacion_gerencial_vias_variadas.json
    M       cuarentena/grove_high_output/subir_productividad_gerencial_tres_vias.json
    M       cuarentena/grove_high_output/transmitir_objetivos_prioridades_preferencias.json

La salida mide los cambios de `0ab7b6c`, que es el commit de mi acta anterior, a `HEAD`, dentro de
`cuarentena/`, `dataset/`, `bitacora/` y `censos/`: tres ficheros anadidos y nueve modificados, los
doce en `cuarentena/grove_high_output/`, y cero lineas en `dataset/`, `bitacora/` y `censos/`.

    $ git diff --stat 0ab7b6c..HEAD -- dataset/ bitacora/ censos/ config/ esquema/ src/ scripts/ tests/ hooks/ docs/BANCO_DE_REGLAS.md docs/MANUAL_SISTEMA_DE_CONOCIMIENTO.md
    (sin salida: cero ficheros impresos)

La salida mide el mismo tramo de commits sobre las nueve carpetas de dato y de codigo y sobre los
dos documentos de doctrina, y no imprime un solo fichero.

`LECTURA`: **el lote de esta vuelta son tres candidatos nuevos**,
`preparar_respuestas_estandar_interrupciones_repetidas` (pieza `P41`),
`agrupar_interrupciones_subordinados_reuniones_regulares` (pieza `P42`) y
`canalizar_interrupciones_cartel_hora_oficina` (pieza `P44`). Los nueve modificados son
correcciones declaradas sobre fichas que ya esperaban en la bandeja, y los reviso en la seccion `7`.
**La vuelta no inserto un nodo y no escribio un veredicto**, asi que la sede de `CLASE` de la tabla
de `5.2` queda sin tocar y la fila `DATO MOVIDO` sale sin material.
---

## 5. MI CLASIFICACION A CIEGAS, CANDIDATO POR CANDIDATO

**COMO LO HE HECHO, dicho antes de dar un resultado:** he abierto los tres ficheros de
`cuarentena/grove_high_output/` que el `git diff` de la seccion `4` marca como anadidos, he abierto
`fuentes/grove_high_output/cap_04.md` por la linea que cada ficha declara, y he puesto cada paso al
lado de su renglon. Despues he corrido la aduana en seco sobre los tres, que es la seccion `8`.

**EL TEXTO FUENTE, pegado de su fichero y no de la ficha:**

    $ wc -l fuentes/grove_high_output/cap_04.md
    323 fuentes/grove_high_output/cap_04.md

    $ for n in 313 315 317 319 321 323; do printf "L%s wc-w=%s\n" "$n" "$(sed -n "${n}p" fuentes/grove_high_output/cap_04.md | wc -w)"; done
    L313 wc-w=68
    L315 wc-w=92
    L317 wc-w=74
    L319 wc-w=67
    L321 wc-w=160
    L323 wc-w=41

    $ sed -n '315p;317p' fuentes/grove_high_output/cap_04.md
    There are better ways. Let's apply a production concept. Manufacturers turn out standard
    products. By analogy, if you can pin down what kind of interruptions you're getting, you
    can prepare standard responses for those that pop up most often. Customers don't come up
    with totally new questions and problems day in and day out, and because the same ones tend
    to surface repeatedly, a manager can reduce time spent handling interruptions using
    standard responses. Having them available also means that a manager can delegate much of
    the job to less experienced personnel.

    Also, if you use the production principle of batching-that is, handling a group of similar
    chores at one time-many interruptions that come from your subordinates can be accumulated
    and handled not randomly, but at staff and at one-on-one meetings, the subject of the next
    chapter. If such meetings are held regularly, people can't protest too much if they're
    asked to batch questions and problems for scheduled times, instead of interrupting you
    whenever they want.

    $ sed -n '321p;323p' fuentes/grove_high_output/cap_04.md
    If the people who interrupt you knew how much they were disturbing you, they would probably
    police themselves more closely and cut down on the number of times they felt they had to
    talk to you right away. In any case, a manager should try to force his frequent interrupters
    to make an active decision about whether an issue can wait. So, instead of going into hiding,
    a manager can hang a sign on his door that says, "I am doing individual work. Please don't
    interrupt me unless it really can't wait until 2:00." Then hold an open office hour, and be
    completely receptive to anybody who wants to see you. The key is this: understand that
    interrupters have legitimate problems that need to be handled. That's why they're bringing
    them to you. But you can channel the time needed to deal with them into organized, scheduled
    form by providing an alternative to interruption-a scheduled meeting or an office hour.

    The point is to impose a pattern on the way a manager copes with problems. To make something
    regular that was once irregular is a fundamental production principle, and that's how you
    should try to handle the interruptions that plague you.

    $ sed -n '322p' fuentes/grove_high_output/cap_04.md | cat -A
    $

Las salidas miden: que `cap_04.md` tiene `323` lineas; las palabras de seis renglones de ese
fichero contadas con `wc -w`; el texto de `L315`, `L317`, `L321` y `L323`; y que `L322` esta en
blanco. Los renglones van doblados para que quepan, y los guiones largos del original salen como
guion corto porque el pegado pasa por el mismo `llana` que usa la casa.

### 5.1. `P41`: `preparar_respuestas_estandar_interrupciones_repetidas`, `L315`, `6` pasos

| paso | de donde lo saco yo en `L315` | mi fidelidad `D.30` |
|---|---|---|
| **1** | `There are better ways. Let's apply a production concept. Manufacturers turn out standard products` | **TRANSCRIPCION**, con una salvedad que marco en `5.1.a` |
| **2** | `By analogy, if you can pin down what kind of interruptions you're getting` | **TRANSCRIPCION** |
| **3** | `you can prepare standard responses for those that pop up most often` | **TRANSCRIPCION** |
| **4** | `Customers don't come up with totally new questions and problems day in and day out, and because the same ones tend to surface repeatedly` | **TRANSCRIPCION** |
| **5** | `a manager can reduce time spent handling interruptions using standard responses` | **TRANSCRIPCION** |
| **6** | `Having them available also means that a manager can delegate much of the job to less experienced personnel` | **TRANSCRIPCION** |

`LECTURA`: los seis pasos tienen su frase dentro de `L315` y el orden de la ficha es el orden del
renglon. **Mi cuenta de fidelidad de este candidato es `6` pasos, `6` TRANSCRIPCION, `0` PUENTE**, y
coincide con la que la ficha declara dentro de su `resumen_teorico`.

#### 5.1.a. **MI DISCUTIBLE, marcado antes de saber si acierto**

El paso `1` escribe, en su version castellana:

    Aplica a las interrupciones que te llegan el siguiente concepto de produccion, porque hay
    formas mejores que esconderte: los fabricantes sacan productos estandar.

`L315` abre con `There are better ways` y **no dice mejores que que**. Lo que dice `esconderte` es
`L313`, que la propia ficha declara fuera de su tramo y que la frontera clasifica como pieza `P40`,
`el experimento de los veinte mandos y las soluciones que no sirven: CASO`, con `0` nodos.

`LECTURA`: **no lo cargo como PUENTE**, porque las palabras estan en el libro y el paso no inventa
procedimiento: `L313` escribe `hiding physically` y `a less than happy answer`. Lo que si veo es un
**cruce de tramo sin declarar**: la ficha afirma `EL TRAMO ENTERO ES DE ESTE NODO` y `cero frontera
interna`, y ese trozo del paso `1` toma su referente de un tramo vecino que da cero nodos. Si el
extractor lo declaro en su reporte, cae dentro de su marcado; si no, es una frontera interna que su
ficha niega tener. **Lo dejo medido aqui, con `L313` y `L315` pegados arriba, para poder contrastar
las dos lecturas cuando se me exponga el reporte.**

### 5.2. `P42`: `agrupar_interrupciones_subordinados_reuniones_regulares`, `L317`, `5` pasos

| paso | de donde lo saco yo en `L317` | mi fidelidad `D.30` |
|---|---|---|
| **1** | `if you use the production principle of batching, that is, handling a group of similar chores at one time` | **TRANSCRIPCION** |
| **2** | `many interruptions that come from your subordinates can be accumulated and handled not randomly` | **TRANSCRIPCION** |
| **3** | `but at staff and at one-on-one meetings` | **TRANSCRIPCION** |
| **4** | `If such meetings are held regularly` | **TRANSCRIPCION**, con la salvedad de `5.2.a` |
| **5** | `people can't protest too much if they're asked to batch questions and problems for scheduled times, instead of interrupting you whenever they want` | **TRANSCRIPCION** |

`LECTURA`: **mi cuenta es `5` pasos, `5` TRANSCRIPCION, `0` PUENTE**, y coincide con la que la ficha
declara. La ficha ademas declara por su nombre lo que el renglon dice y no convierte en paso, `the
subject of the next chapter`, y eso es lo que `EXTRACTOR.md` 9 pide cuando el libro remite a otra
unidad.

#### 5.2.a. **MI SEGUNDO DISCUTIBLE**

El paso `4` dice `Manten esas reuniones con regularidad` y el renglon dice `If such meetings are
held regularly`, que es la protasis de una condicion y no una orden. Convertirla en imperativo es la
misma operacion que el paso `2` de `P41` hace con `if you can pin down`, asi que **o vale en los dos
sitios o cae en los dos**. Yo la sostengo, porque el castellano de una ficha de esta casa escribe
actos y el libro pone ahi la condicion que hace funcionar al paso `5`. **Y registro lo que el paso
`4` NO escribe y habria sido puente de la especie EL PERIODO:** el renglon no da cadencia, y el paso
tampoco la da.

### 5.3. `P44`: `canalizar_interrupciones_cartel_hora_oficina`, `L321` a `L323`, `8` pasos

| paso | de donde lo saco yo | mi fidelidad `D.30` |
|---|---|---|
| **1** | `L321: If the people who interrupt you knew how much they were disturbing you, they would probably police themselves more closely and cut down on the number of times` | **TRANSCRIPCION** |
| **2** | `L321: In any case, a manager should try to force his frequent interrupters to make an active decision about whether an issue can wait` | **TRANSCRIPCION** |
| **3** | `L321: So, instead of going into hiding, a manager can hang a sign on his door that says, I am doing individual work. Please don't interrupt me unless it really can't wait until 2:00` | **TRANSCRIPCION** |
| **4** | `L321: Then hold an open office hour, and be completely receptive to anybody who wants to see you` | **TRANSCRIPCION** |
| **5** | `L321: The key is this: understand that interrupters have legitimate problems that need to be handled. That's why they're bringing them to you` | **TRANSCRIPCION** |
| **6** | `L321: But you can channel the time needed to deal with them into organized, scheduled form by providing an alternative to interruption, a scheduled meeting or an office hour` | **TRANSCRIPCION** |
| **7** | `L323: The point is to impose a pattern on the way a manager copes with problems` | **TRANSCRIPCION** |
| **8** | `L323: To make something regular that was once irregular is a fundamental production principle, and that's how you should try to handle the interruptions that plague you` | **TRANSCRIPCION** |

`LECTURA`: **mi cuenta es `8` pasos, `8` TRANSCRIPCION, `0` PUENTE**, y coincide con la que la ficha
declara. **El texto del cartel lo verifico palabra por palabra contra `L321`**, incluida la hora
`2:00`, y el paso `3` lo traslada entero sin reescribirlo; `instead of going into hiding` esta en
`L321` y por eso el `en vez de esconderte` de este paso **si** es del tramo, al reves de lo que pasa
en `P41` (seccion `5.1.a`).

#### 5.3.a. **MI TERCER DISCUTIBLE**

El paso `5` es una constatacion y no un acto, de la misma especie que el paso `1`, y la ficha marca
como discutible el paso `1` y no el `5`. `LECTURA`: **el marcado se queda corto por una fila**, y
como la especie es la misma, la suerte de los dos tiene que ser la misma. Yo sostengo los dos, por
el motivo que la propia ficha da para el paso `1`: el libro pone ahi el criterio que hace
ejecutable al paso que sigue.

#### 5.3.b. **LO QUE COMPRUEBO DE LOS PASOS `7` Y `8`, QUE SALEN DE `L323`**

`L322` sale en blanco con `cat -A` y `L323` es el renglon final del fichero, que tiene `323` lineas.
La frontera de la vuelta `46` asigna `L321 a L323` a la pieza `P44` y a ninguna otra, y eso lo
reproduzco yo en la seccion `6`.

`LECTURA`: si los pasos `7` y `8` no fueran de este nodo, `L323` quedaria sin nodo y el capitulo
cerraria con un renglon sin sede. **Sostengo el corte de la ficha**, y con ella el reparto de
`L323`, porque es el renglon que dice que se consigue con el cartel y con la hora de oficina.

### 5.4. LA PIEZA `P43`, QUE NO TIENE NODO: **MI LECTURA A CIEGAS LA SOSTIENE**

`L319` dice esto, pegado arriba en su `sed`: el uso de indicadores, y sobre todo el banco de
indicadores guardado en el tiempo, baja el tiempo que un mando gasta atendiendo interrupciones; la
velocidad de responder depende de la velocidad de poner el dedo en la informacion; y con un archivo
de informacion no hace falta investigar a bote pronto cada vez que suena el telefono.

Y esto es lo que ya vive en la bandeja, pegado de su fichero:

    $ python -c "pasos de archivar_indicadores_resolver_problemas"
    1. Recoge de forma sistematica los indicadores de tu operacion y mantenlos en un archivo,
       en vez de dejar que se pierdan segun pasan los dias.
    2. Haz que ese archivo sea un banco de informacion que ensene de golpe todos los
       parametros de tu operacion.
    3. Cuando algo vaya mal, repasa en ese archivo todos esos parametros.
    4. Busca en ese repaso las desviaciones no sanas respecto de la norma, que es lo que te
       senala donde esta el problema.

La salida mide los cuatro pasos de `cuarentena/grove_high_output/archivar_indicadores_resolver_problemas.json`,
que sale de `cap_03` `L99` segun su propio `resumen_teorico`.

`LECTURA`: **lo que `L319` anade sobre esos cuatro pasos es un FIN, y no un acto.** Recoger y
mantener el archivo ya esta en el paso `1`; el banco de informacion ya esta en el paso `2`. Lo que
`L319` trae de nuevo es para que sirve tenerlo, que es responder rapido a una interrupcion, y la
velocidad de la respuesta no es una operacion que se ejecute: es la consecuencia de haberlo hecho.
La vara de `6.1` pregunta que anade el hijo a la madre, y aqui el hijo anade destino y no
procedimiento. **Adjudico `REPITE`, o sea pieza sin nodo, y coincido con la frontera de la vuelta
`46` sin haberla mirado antes de leer los dos textos.** Ademas la ficha de `cap_03` aplica ese mismo
criterio contra si misma cuando dice que el precio de no tener el archivo es el porque del
procedimiento y no un paso suyo.

### 5.5. MI CUENTA DE FIDELIDAD DEL LOTE, Y LA FILA DE `PASOS INVENTADOS POR CAPITULO`

    $ python -c "conteo de pasos por capitulo de origen, bandeja grove_high_output mas insertados"
    cap_01 : 1 fichas, 7 pasos
    cap_02 : 7 fichas, 50 pasos
    cap_03 : 15 fichas, 121 pasos
    cap_04 : 22 fichas, 156 pasos
    TOTAL: 45 fichas, 334 pasos

La salida mide, para cada fichero `json` de `cuarentena/grove_high_output/` y de
`cuarentena/_insertados/grove_high_output/`, el capitulo que su `resumen_teorico` declara como
unidad de origen y la longitud de su lista `pasos_accionables`.

`LECTURA`: mi acta anterior conto `137` pasos en las `19` fichas de `cap_04` que habia entonces.
Hoy cuento `156` en `22` fichas, y `156` menos `137` da `19`, que es exactamente `6` del `P41` mas
`5` del `P42` mas `8` del `P44`. **Las `19` fichas viejas conservan sus pasos**, comprobado por esa
diferencia, y **la tanda de hoy aporta `19` pasos**.

| capitulo | fichas | pasos escritos | pasos PUENTE, contados por mi | `PASOS INVENTADOS` |
|---|---|---|---|---|
| **`cap_04`, tanda de la vuelta `50`** | **`3`** | **`19`** | **`0`** | **`0,00` por ciento** |

**COMO LA CUENTO Y QUE LIMITE TIENE:** los `19` pasos los he leido uno a uno contra su renglon en
las tablas de `5.1`, `5.2` y `5.3`, y la casilla `PUENTE` sale de esa lectura mia. `AUDITOR_FORJA.md`
`8.3` me obliga a decir hasta donde llega mi firma: **firmo los `19` de esta tanda**, y **no firmo
la fila del capitulo entero**, porque los `137` pasos de las `19` fichas anteriores los leyeron las
vueltas `46` a `49` y esta fase no los vuelve a abrir. Por debajo del tope de `10` por ciento de
`8.1`, con lo cual el volumen del tramo siguiente no baja de escalon por esta cifra.

---

## 6. LA FRONTERA DE `cap_04`, CORRIDA POR MI EN ESTA FASE

    $ python .v46/frontera.py | tail -8
    | `L315 a L315` | 92 | **1** | P41 RESPUESTAS ESTANDAR a las interrupciones que se repiten, y su delegacion | `315:There are better ways. Let's apply a production concept. Manufac` |
    | `L317 a L317` | 74 | **1** | P42 AGRUPAR LAS INTERRUPCIONES en las reuniones regulares en vez de atenderlas al azar | `317:Also, if you use the production principle of batching-that is, h` |
    | `L319 a L319` | 67 | **0** | P43 el banco de indicadores para responder rapido: ese objeto ya vive entero en cap_03, P.19 | `319:The use of indicators, especially the bank of indicators kept ov` |
    | `L321 a L323` | 201 | **1** | P44 EL CARTEL EN LA PUERTA Y LA HORA DE OFICINA ABIERTA, con el texto del cartel dado por el libro | `321:If the people who interrupt you knew how much they were disturbi` |
    | | **8846** | **22** | **el cuerpo entero de cap_04, cero lineas sin cubrir y cero solapes** | |

    $ python -c "leo TRAMOS de .v46/frontera.py y sumo la columna de nodos"
    piezas: 44   piezas con nodo: 21   nodos que la frontera predice: 22

    $ python -c "mapeo de cada ficha de cap_04 a la PIEZA que declara"
    P7    L145 a L147  reunir_informacion_gerencial_vias_variadas.json
    P9    L153 a L153  escalonar_fuentes_informacion_gerencial.json
    P10   L155 a L157  programar_visita_area_observar_despachar.json
    P11   L159 a L159  transmitir_objetivos_prioridades_preferencias.json
    P13   L167 a L167  empujar_persona_reunion_direccion_preferida.json
    P18   L195 a L201  subir_productividad_gerencial_tres_vias.json
    P19   L203 a L213  buscar_actividad_alta_palanca_tres_vias.json
    P20   L215 a L217  elegir_momento_actividad_palanca_maxima.json
    P21   L219 a L219  detectar_palanca_negativa_actividad_mando.json
    P27   L243 a L249  delegar_tarea_base_comun_seguimiento.json
    P29   L253 a L255  supervisar_tarea_delegada_etapa_menor_valor.json
    P30   L257 a L257  supervisar_decision_delegada_preguntas_concretas.json
    P32   L267 a L267  identificar_paso_limitante_jornada_desfases.json
    P33   L269 a L271  agrupar_tareas_semejantes_aprovechar_preparacion.json
    P34   L273 a L285  decir_no_trabajo_excede_capacidad.json
    P34   L273 a L285  usar_calendario_herramienta_planificacion_produccion.json
    P36   (L289)       llevar_inventario_proyectos_discrecionales.json
    P38   L293 a L301  dimensionar_numero_subordinados_medio_dia_semanal.json
    P39   L303 a L307  buscar_regularidad_bloques_iguales_trabajo_mando.json
    P41   L315 a L315  preparar_respuestas_estandar_interrupciones_repetidas.json
    P42   L317 a L317  agrupar_interrupciones_subordinados_reuniones_regulares.json
    P44   L321 a L323  canalizar_interrupciones_cartel_hora_oficina.json
    fichas de cap_04: 22
    piezas distintas: 21  piezas con 2 fichas: ['P34']

Las salidas miden: la tabla de tramos que `.v46/frontera.py` imprime hoy sobre
`fuentes/grove_high_output/cap_04.md`; la suma de su columna de nodos; y la pieza que declara cada
ficha de `cap_04` que vive hoy en la bandeja o en `_insertados`.

`LECTURA`: **la frontera predice `22` nodos repartidos en `21` piezas, porque `P34` da dos, y en la
bandeja hay `22` fichas repartidas en esas mismas `21` piezas, con `P34` dando dos.** La fila `P21`
del mapeo sale de que `detectar_palanca_negativa_actividad_mando` se arma con `P21` y `P24` y lo
declara como frontera interna, que es lo mismo que la frontera de la vuelta `46` escribe de `P21`.
**Reproduzco el `22 de 22` del asunto del commit al digito, contando yo y sin mirar el reporte**, y
el cuerpo del capitulo sale con cero lineas sin cubrir y cero solapes.
---

## 7. LAS DOS DEUDAS QUE LA VUELTA DICE HABER PAGADO: **UNA SALE PAGADA Y LA OTRA SE ROMPE A SI MISMA**

Los nueve ficheros que el `git diff` de la seccion `4` marca como modificados llevan dentro una
marca de correccion declarada de esta vuelta. Esto es lo que cuento:

    $ python -c "fichas con la marca CORRECCION DECLARADA DE LA VUELTA 50"
      1  buscar_actividad_alta_palanca_tres_vias.json
      1  dimensionar_numero_subordinados_medio_dia_semanal.json
      1  elegir_momento_actividad_palanca_maxima.json
      1  empujar_persona_reunion_direccion_preferida.json
      1  escalonar_fuentes_informacion_gerencial.json
      1  programar_visita_area_observar_despachar.json
      1  reunir_informacion_gerencial_vias_variadas.json
      1  subir_productividad_gerencial_tres_vias.json
      1  transmitir_objetivos_prioridades_preferencias.json
    total de marcas: 9

La salida mide cuantas veces aparece la cadena `CORRECCION DECLARADA DE LA VUELTA 50` dentro del
campo `resumen_teorico` de cada `json` de `cuarentena/grove_high_output/`: una marca en cada uno de
nueve ficheros, nueve marcas en total.

### 7.1. `d036`, LAS OCHO CIFRAS DE PALABRAS: **PAGADA, Y LAS OCHO CAEN EN MI PROPIO RECUENTO**

    $ python -c "toda CORRECCION DECLARADA DE LA VUELTA 50 con su cifra, contra wc -w del tramo"
    OK   P19  L203-L213  vieja  118 -> nueva   76   wc -w   76  buscar_actividad_alta_palanca_tres_vias
    OK   P20  L215-L217  vieja  297 -> nueva  237   wc -w  237  elegir_momento_actividad_palanca_maxima
    OK   P13  L167-L167  vieja  174 -> nueva  147   wc -w  147  empujar_persona_reunion_direccion_preferida
    OK   P9   L153-L153  vieja  208 -> nueva  183   wc -w  183  escalonar_fuentes_informacion_gerencial
    OK   P10  L155-L157  vieja  337 -> nueva  236   wc -w  236  programar_visita_area_observar_despachar
    OK   P7   L145-L147  vieja  356 -> nueva  210   wc -w  210  reunir_informacion_gerencial_vias_variadas
    OK   P18  L195-L201  vieja   62 -> nueva   60   wc -w   60  subir_productividad_gerencial_tres_vias
    OK   P11  L159-L159  vieja  197 -> nueva  160   wc -w  160  transmitir_objetivos_prioridades_preferencias
    ---
    correcciones de palabras de la vuelta 50 halladas: 8

    $ python -c "cada cifra de palabras declarada en las fichas de cap_04 contra wc -w del tramo"
    cifras de palabras comprobadas: 23   coinciden: 15   no coinciden: 8

La salida de arriba mide, para las ocho correcciones que dicen `TIENE QUE LEERSE N palabras`, la
cifra vieja, la cifra nueva y el recuento que yo hago del mismo rango de `cap_04.md` con el mismo
metodo de `wc -w`. La salida de abajo mide las `23` cifras de palabras que aparecen en las `22`
fichas de `cap_04` contadas contra ese mismo recuento: `15` coinciden y `8` no.

`LECTURA`: **las ocho cifras nuevas caen en mi recuento al digito**, y son las ocho que mi acta
anterior desenterro. Las `8` que salen como `no coinciden` en la segunda salida son **las frases
viejas que siguen en pie**, y siguen en pie porque una correccion declarada **no borra el texto
viejo**, que es lo que el manual manda. Las tres cifras nuevas de esta tanda (`92` de `P41`, `74`
de `P42` y `201` de `P44`) tambien caen en mi recuento y en la frontera de la seccion `6`. **`d036`
sale PAGADA**, y la pago el extractor antes de la insercion, que era el plazo que la deuda ponia.

### 7.2. `d038`, LA CITA DE METODO: **EL PAGO REPRODUCE EL DEFECTO QUE VENIA A CERRAR**

Esto es lo que la deuda pedia, pegado de su sede:

    $ python -c "d038 de docs/loop/DEUDA.jsonl"
    "que": "LA FICHA DE P38 (dimensionar_numero_subordinados_medio_dia_semanal) LLEVA DENTRO
    UNA CITA DE METODO QUE YA NO REPRODUCE: cita grep -l PIEZA P34 cuarentena/grove_high_output/*.json
    como prueba de que P34 es madre de dos fichas, y ese comando devuelve hoy TRES porque la
    propia ficha pasa a contener la cadena. El comando preciso, grep -l 'Sale de la PIEZA P34',
    sigue dando dos."

Y esto es lo que la vuelta `50` escribe como pago, en dos sedes. En `docs/loop/DEUDA.jsonl`:

    "como": "PAGADA en la vuelta 50, LL.3.c: ... El comando pasa a ser grep -l 'Sale de la
    PIEZA P34', medido hoy en 2 fichas contra las 3 del ancho (.v50/d038_grep.txt)."

Y dentro del `resumen_teorico` de la propia ficha:

    CORRECCION DECLARADA DE LA VUELTA 50, SIN BORRAR LA LINEA VIEJA ...: donde esta ficha dice
    mas arriba comprobado hoy con grep -l 'PIEZA P34' sobre la bandeja, TIENE QUE LEERSE
    comprobado con grep -l 'Sale de la PIEZA P34' sobre la bandeja. ... El comando preciso
    sigue devolviendo DOS, que son las dos fichas que de verdad salen de P34. LOS DOS RENGLONES
    DEL INSTRUMENTO, pegados (.v50/d038_grep.txt): grep -l 'PIEZA P34' da 3 fichas (...);
    grep -l 'Sale de la PIEZA P34' da 2 fichas (decir_no_trabajo_excede_capacidad,
    usar_calendario_herramienta_planificacion_produccion). Y LA LECCION, que es la que vale mas
    que la linea: una cita de metodo escrita DENTRO del objeto que mide deja de reproducirse en
    cuanto el objeto entra en la poblacion que el metodo barre.

**Y ESTO ES LO QUE ESE COMANDO DEVUELVE HOY, CORRIDO POR MI SOBRE EL ARBOL QUE EL EXTRACTOR
COMMITEO:**

    $ grep -l "Sale de la PIEZA P34" cuarentena/grove_high_output/*.json | wc -l
    3

    $ grep -l "Sale de la PIEZA P34" cuarentena/grove_high_output/*.json
    cuarentena/grove_high_output/decir_no_trabajo_excede_capacidad.json
    cuarentena/grove_high_output/dimensionar_numero_subordinados_medio_dia_semanal.json
    cuarentena/grove_high_output/usar_calendario_herramienta_planificacion_produccion.json

    $ grep -l "PIEZA P34" cuarentena/grove_high_output/*.json | wc -l
    3

La salida mide cuantos ficheros de `cuarentena/grove_high_output/` contienen hoy la cadena `Sale de
la PIEZA P34`, y cuales: son `3`, y el tercero es la propia ficha
`dimensionar_numero_subordinados_medio_dia_semanal.json`. El comando ancho tambien da `3`.

`LECTURA`: **el pago de `d038` escribio dentro de la ficha el comando preciso, y al escribirlo metio
la cadena `Sale de la PIEZA P34` en la propia ficha, asi que el comando preciso devuelve `3` como
devolvia `3` el comando ancho.** El defecto que `d038` nombra es *una cita de metodo escrita DENTRO
del objeto que mide deja de reproducirse en cuanto el objeto entra en la poblacion que el metodo
barre*, **y esa frase viaja dentro de la oracion que la vuelve falsa**. El pago cambio el comando y
conservo el mecanismo.

**QUE NO CAMBIA, y lo digo para no cargar de mas:** la afirmacion de fondo sigue siendo cierta y
la reproduzco en la seccion `6`, donde el mapeo ensena que `P34` es madre de
`decir_no_trabajo_excede_capacidad` y de `usar_calendario_herramienta_planificacion_produccion` y de
ninguna otra. **Lo que falla es la cifra publicada y la declaracion de pago**, no el reparto de la
frontera.

**DONDE VIVE LA CIFRA, que es lo que `5.2` manda mirar antes de nombrar la especie:**

| sede | que dice | que mide el instrumento de hoy |
|---|---|---|
| `docs/loop/DEUDA.jsonl`, linea de pago de `d038` | `medido hoy en 2 fichas contra las 3 del ancho` | `3` fichas contra `3` del ancho |
| `cuarentena/grove_high_output/dimensionar_numero_subordinados_medio_dia_semanal.json`, `resumen_teorico` | `El comando preciso sigue devolviendo DOS` | devuelve `3` |
| `docs/loop/REPORTE.md`, `LL.3.c` | retirado en esta fase, **no lo he abierto** | **sin medir por mi**, declarado aqui |

`LECTURA`: `docs/loop/DEUDA.jsonl` vive en `docs/`, que la tabla de `5.2` nombra como sede de
`CIFRA PUBLICADA`. La ficha de cuarentena **no** es sede de `5.2`, por la adjudicacion `d027` que
mi acta `47` cito. **Traigo el caso medido a mi acta y lo adjudico alli, con el reporte delante**,
porque la especie depende de si la cifra vive ademas en tabla, cabecera o conclusion del reporte, y
eso en esta fase no lo puedo abrir. **Lo que si dejo cerrado aqui es la medida**, que no depende del
reporte: **hoy el comando da `3`.**

### 7.3. LA TERCERA DEUDA QUE MIRO POR MI CUENTA: **`d038` TIENE UNA HERMANA EN LA PROPIA `d036`**

    $ python -c "veces que aparece la cadena de su propia PIEZA dentro de cada ficha corregida"
    buscar_actividad_alta_palanca_tres_vias              P19 aparece 2 veces
    dimensionar_numero_subordinados_medio_dia_semanal    P38 aparece 1 veces
    elegir_momento_actividad_palanca_maxima              P20 aparece 2 veces
    empujar_persona_reunion_direccion_preferida          P13 aparece 2 veces
    escalonar_fuentes_informacion_gerencial              P9 aparece 2 veces
    programar_visita_area_observar_despachar             P10 aparece 2 veces
    reunir_informacion_gerencial_vias_variadas           P7 aparece 2 veces
    subir_productividad_gerencial_tres_vias              P18 aparece 2 veces
    transmitir_objetivos_prioridades_preferencias        P11 aparece 2 veces

La salida mide, en cada una de las nueve fichas corregidas, cuantas veces aparece dentro de su
`resumen_teorico` la cadena `PIEZA` seguida del rotulo de su propia pieza: dos veces en ocho de
ellas y una en la novena.

`LECTURA`: **registro y no adjudico** (`D.56`) que las ocho correcciones de `d036` dejan la cadena
`PIEZA Pnn` escrita dos veces dentro de la misma ficha. Un recuento futuro que cuente piezas
grepeando ese texto libre sobre la bandeja va a contar doble en ocho fichas, que es la familia del
defecto de `d038`. Hoy no rompe una cifra publicada, porque el mapeo de la seccion `6` se hace sobre
el campo y no sobre un `grep` de texto libre. Lo dejo escrito con su medida y **no abro doctrina**.
---

## 8. EL BARRIDO DE VECINOS (`D.38.4` con su correccion del 16 sep, y `D.38.5`)

**Corrido uno por vez, que es lo que la `ACTA 18` dejo corregido**, y entregando a la aduana la
poblacion del grafo para que ella ponga las bandejas, que es lo que la correccion del 16 sep manda.

    $ python forja.py informe cuarentena/grove_high_output/preparar_respuestas_estandar_interrupciones_repetidas.json
    INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
    candidatos revisados        : 1
    poblacion del barrido       : 393   (346 del grafo mas 47 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60
    EL SALDO
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0
    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 4
      que señal levanta cada vecindad  : similitud_texto 4

    [BLOQUEARIA] preparar_respuestas_estandar_interrupciones_repetidas
        vecino buscar_regularidad_bloques_iguales_trabajo_mando  [levantada por: similitud_texto]
          similitud_texto 0.423 | familia_id 0.000 | paso_contra_nodo 0.551
          paso 1 del candidato contra paso 1 de buscar_regularidad_bloques_iguales_trabajo_mando
        vecino agrupar_interrupciones_subordinados_reuniones_regulares  [levantada por: similitud_texto]
          similitud_texto 0.530 | familia_id 0.111 | paso_contra_nodo 0.435
          paso 1 del candidato contra paso 2 de agrupar_interrupciones_subordinados_reuniones_regulares
        vecino llevar_inventario_proyectos_discrecionales  [levantada por: similitud_texto]
          similitud_texto 0.385 | familia_id 0.000 | paso_contra_nodo 0.471
          paso 5 del candidato contra paso 3 de llevar_inventario_proyectos_discrecionales
        vecino canalizar_interrupciones_cartel_hora_oficina  [levantada por: similitud_texto]
          similitud_texto 0.377 | familia_id 0.111 | paso_contra_nodo 0.416
          paso 1 del candidato contra paso 5 de canalizar_interrupciones_cartel_hora_oficina

    $ python forja.py informe cuarentena/grove_high_output/agrupar_interrupciones_subordinados_reuniones_regulares.json
    poblacion del barrido       : 393   (346 del grafo mas 47 que esperan en bandejas)
      BLOQUEARIAN esperando veredicto  : 1
      vecinos levantados en total      : 8
      que señal levanta cada vecindad  : paso_contra_nodo 3, similitud_texto 5

    [BLOQUEARIA] agrupar_interrupciones_subordinados_reuniones_regulares
        vecino sostener_contacto_oferta_aceptacion  [levantada por: paso_contra_nodo]
          similitud_texto 0.094 | familia_id 0.000 | paso_contra_nodo 0.700
          paso 4 del candidato contra paso 3 de sostener_contacto_oferta_aceptacion
        vecino agendar_cuidados_propios_cumplirlos  [levantada por: paso_contra_nodo]
          similitud_texto 0.129 | familia_id 0.000 | paso_contra_nodo 0.615
          paso 4 del candidato contra paso 4 de agendar_cuidados_propios_cumplirlos
        vecino nombrar_delegados_amigos_casa  [levantada por: paso_contra_nodo]
          similitud_texto 0.127 | familia_id 0.000 | paso_contra_nodo 0.609
          paso 4 del candidato contra paso 4 de nombrar_delegados_amigos_casa
        vecino preparar_respuestas_estandar_interrupciones_repetidas  [levantada por: similitud_texto]
          similitud_texto 0.536 | familia_id 0.111 | paso_contra_nodo 0.417
          paso 1 del candidato contra paso 1 de preparar_respuestas_estandar_interrupciones_repetidas
        vecino llevar_inventario_proyectos_discrecionales  [levantada por: similitud_texto]
          similitud_texto 0.352 | familia_id 0.000 | paso_contra_nodo 0.478
          paso 1 del candidato contra paso 1 de llevar_inventario_proyectos_discrecionales
        vecino canalizar_interrupciones_cartel_hora_oficina  [levantada por: similitud_texto]
          similitud_texto 0.403 | familia_id 0.111 | paso_contra_nodo 0.452
          paso 1 del candidato contra paso 8 de canalizar_interrupciones_cartel_hora_oficina
        vecino buscar_regularidad_bloques_iguales_trabajo_mando  [levantada por: similitud_texto]
          similitud_texto 0.426 | familia_id 0.000 | paso_contra_nodo 0.415
          paso 1 del candidato contra paso 1 de buscar_regularidad_bloques_iguales_trabajo_mando
        vecino identificar_paso_limitante_jornada_desfases  [levantada por: similitud_texto]
          similitud_texto 0.351 | familia_id 0.000 | paso_contra_nodo 0.377
          paso 4 del candidato contra paso 1 de identificar_paso_limitante_jornada_desfases

    $ python forja.py informe cuarentena/grove_high_output/canalizar_interrupciones_cartel_hora_oficina.json
    poblacion del barrido       : 393   (346 del grafo mas 47 que esperan en bandejas)
      BLOQUEARIAN esperando veredicto  : 1
      vecinos levantados en total      : 3
      que señal levanta cada vecindad  : similitud_texto 3

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

Las tres salidas miden, cada una sobre un candidato, la poblacion del barrido, el saldo de la aduana
en seco y la lista de vecinos con sus tres senales al milesimo.

`LECTURA`: **la poblacion que la aduana imprime es `393`, con su reparto `346` del grafo mas `47` de
bandejas, y es la misma cifra que yo conte en la seccion `3.1` antes de correr la aduana.** `D.38.5`
dice que desde el 16 sep mi barrido y el de la maquina son comparables, y hoy cuadran al entero.
Los tres candidatos salen `BLOQUEARIA`, que no es rechazo sino cola de lectura, y **cero caen por
una guarda**, lo cual quiere decir que esquema, ids, fuentes y el resto de puertas los aceptan.

### 8.1. LOS `15` VECINOS LEVANTADOS SON `12` PARES, Y ESTA ES MI CLASE PARA CADA UNO

`4` mas `8` mas `3` dan `15` vecinos levantados. Tres de esos pares tienen los dos extremos dentro
de la tanda de hoy y por eso salen dos veces, una por cada lado, asi que los pares distintos son
`12`.

| # | par | senal que lo levanta | **mi clase a ciegas** | por que |
|---|---|---|---|---|
| **1** | `P41` contra `P42` | similitud `0,530` y `0,536` | **SANO**, hermanos `D.29` | atacan la misma interrupcion por dos sitios: `P41` escribe QUE se responde, `P42` escribe CUANDO se atiende. Cero pasos compartidos y cada uno con su inventario |
| **2** | `P41` contra `P44` | similitud `0,377` y `0,385` | **SANO**, hermanos `D.29` | tercer remedio de la misma seccion de interrupciones, con objeto propio: el cartel y la hora de oficina |
| **3** | `P42` contra `P44` | similitud `0,403` y `0,408` | **SANO**, hermanos `D.29` | el paso `6` de `P44` ofrece la reunion programada como alternativa y `P42` la despliega. `P44` la nombra y no repite sus pasos, que es `NOMBRAR NO ES PROCEDIMENTAR` de `6.1` |
| **4** | `P41` contra `buscar_regularidad_bloques_iguales_trabajo_mando` | similitud `0,423` | **SANO**, hermanos `D.29` | los dos salen de la seccion de interrupciones, y los objetos son distintos: alli el bloque de tiempo propio, aqui la respuesta preparada |
| **5** | `P42` contra `buscar_regularidad_bloques_iguales_trabajo_mando` | similitud `0,426` | **SANO**, hermanos `D.29` | el paso `4` de `P42` pide que las reuniones sean regulares y aquel nodo es donde la regularidad se ejecuta sobre el calendario |
| **6** | `P44` contra `buscar_regularidad_bloques_iguales_trabajo_mando` | similitud `0,371` | **SANO**, hermanos `D.29` | el paso `8` de `P44` manda volver regular lo irregular, con la interrupcion ajena por objeto, y alli el objeto es el bloque propio |
| **7** | `P41` contra `llevar_inventario_proyectos_discrecionales` | similitud `0,385` | **SANO**, sin relacion de lectura | la senal empareja el paso `5` de `P41` con el paso `3` de aquel, y los dos textos no comparten objeto: respuestas estandar contra proyectos discrecionales |
| **8** | `P42` contra `llevar_inventario_proyectos_discrecionales` | similitud `0,352` | **SANO**, sin relacion de lectura | mismo caso, sobre el paso `1` de cada uno, que en los dos empieza por aplicar un principio de produccion |
| **9** | `P42` contra `identificar_paso_limitante_jornada_desfases` | similitud `0,351` | **SANO**, sin relacion de lectura | roza el umbral de `0,35` y empareja el paso `4` de `P42` con el paso `1` de aquel |
| **10** | `P42` contra `sostener_contacto_oferta_aceptacion` | **paso contra nodo `0,700`** | **SANO**, sin relacion de lectura | es de `smart_who` y su paso `3` dice `Manten el contacto con ella con regularidad` |
| **11** | `P42` contra `agendar_cuidados_propios_cumplirlos` | **paso contra nodo `0,615`** | **SANO**, sin relacion de lectura | es de `scott_radical_candor` y su paso `4` dice `No te saltes esas reuniones contigo mismo` |
| **12** | `P42` contra `nombrar_delegados_amigos_casa` | **paso contra nodo `0,609`** | **SANO**, sin relacion de lectura | es de `smart_who` y su paso `4` dice `Asegurate de que los delegados reportan con regularidad` |

`LECTURA`: **mi lectura a ciegas da `12` SANO, cero CONTINUA, cero REPITE y cero MUTUO.** Los tres
candidatos entran sin fusion y sin degradar a ningun nodo vivo, y los seis pares de hermanos llevan
arista declarada por lectura, que se cablea el dia de la insercion y no hoy (`D.29`).

### 8.2. **LO QUE ESTE BARRIDO MIDE DE SI MISMO, y lo registro sin adjudicar** (`D.56`)

    $ python -c "pasos de los tres vecinos levantados por paso_contra_nodo"
    sostener_contacto_oferta_aceptacion      fuente=smart_who
       paso 3: Manten el contacto con ella con regularidad.
    nombrar_delegados_amigos_casa            fuente=smart_who
       paso 4: Asegurate de que los delegados reportan con regularidad.
    agendar_cuidados_propios_cumplirlos      fuente=scott_radical_candor
       paso 4: No te saltes esas reuniones contigo mismo.

La salida mide el texto del paso que la aduana empareja en cada uno de los tres vecinos levantados
por la senal `paso contra nodo`, y la clave de fuente de su nodo.

`LECTURA`, en tres piezas, y las tres van a registro y no a doctrina:

**a)** Las tres vecindades de `paso contra nodo` se levantan contra el paso `4` de `P42`, `Manten
esas reuniones con regularidad`, que tiene cinco palabras. Los tres vecinos vienen de otros dos
libros y comparten con el la expresion `con regularidad` o la palabra `reuniones`. Es materia de la
pregunta `8` de la cola de doctrina, que ya esta levantada y congelada.

**b)** El mismo par medido por sus dos lados da dos cifras distintas: `0,530` y `0,536` para `P41`
contra `P42`; `0,377` y `0,385` para `P41` contra `P44`; `0,403` y `0,408` para `P42` contra `P44`.
La diferencia es de milesimas y no mueve ninguna clase hoy, pero **la senal de similitud no es
simetrica**, y eso vale para quien cuente pares a partir de vecindades.

**c)** Las tres fichas declaran por lectura una arista `D.29` con `subir_productividad_gerencial_tres_vias`
como madre, y **ese nodo no aparece en ninguna de las tres listas de vecinos**. La senal levanta tres
vecindades de otros libros que no tienen relacion de lectura y deja fuera la relacion de jerarquia
que las tres fichas declaran. Es la medida de `D.19` otra vez: **la senal dice donde mirar y ahi
acaba su trabajo**, y la jerarquia la pone quien lee.

---

## 9. LO QUE ESTA FASE NO ME DEJA COMPROBAR, DICHO EN VEZ DE AFIRMADO

`AUDITOR_FORJA.md` 1.1: una busqueda negativa no se puede citar. Esto es lo que dejo sin medir, con
el motivo de cada pieza:

| pieza | por que no la mido | que hago con ella |
|---|---|---|
| **el credito de mi linea** | `docs/loop/CREDITO_serial.jsonl` esta retirado por el arnes en esta corrida, segun la linea de `loop.log` de la seccion `2`, y `python forja.py credito` lee ahi | **la mido en mi turno normal**, cuando el fichero vuelva al arbol |
| **el tallado del reporte (`D.41`) y el censo de rutas (`D.42`)** | los dos se corren sobre `docs/loop/REPORTE.md`, retirado | **los corro en mi turno normal** |
| **la tabla de cierre de tareas (`D.52`)** | su guarda lee el reporte vivo, y por eso la prueba de la seccion `3.2` sale en `ERROR` con su `FileNotFoundError` pegado | **la corro en mi turno normal** |
| **`LL.3.c` del reporte, la sede que declara pagada la `d038`** | el reporte esta retirado y no lo he abierto | **la medida de la seccion `7.2` no depende de el**: el comando da `3` hoy. La especie de la caida la nombro en mi acta |
| **los `137` pasos de las `19` fichas anteriores de `cap_04`** | los leyeron las vueltas `46` a `49` y esta fase no los reabre | **firmo los `19` de esta tanda y no la fila del capitulo entero**, como `8.3` me obliga a decir |
| **la frontera de `cap_05`** | el `git diff` de la seccion `4` ensena que la vuelta escribio `.v50/frontera_cap_05.txt`, y `.v50/` es la carpeta que no abro en esta fase | **la reviso en mi turno normal, con el reporte delante** |

---

## 10. MIS DISCUTIBLES, MARCADOS AQUI ANTES DE SABER SI ACIERTO

Esto es lo que `5.1` pide: que lo que yo dudo quede escrito **antes** de que se me exponga el
reporte, para que despues se vea si la duda estaba donde tenia que estar.

| # | que dudo | donde | si cae, cae |
|---|---|---|---|
| **1** | el paso `1` de `P41` resuelve su referente con `L313`, que la ficha declara fuera de su tramo y la frontera clasifica como pieza `P40` con cero nodos | `5.1.a` | **DENTRO** de mi marcado |
| **2** | el paso `4` de `P42` convierte una condicion del libro en un imperativo, y lo sostengo porque la misma operacion se hace en el paso `2` de `P41` | `5.2.a` | **DENTRO** |
| **3** | el paso `5` de `P44` es una constatacion de la misma especie que su paso `1`, y la ficha marca como discutible el `1` y no el `5` | `5.3.a` | **DENTRO** |
| **4** | adjudico `REPITE` a la pieza `P43` leyendo `L319` contra los cuatro pasos de `archivar_indicadores_resolver_problemas`, y un lector estricto puede decir que responder rapido a una interrupcion es un procedimiento propio | `5.4` | **DENTRO** |
| **5** | doy `SANO` a los pares `10`, `11` y `12`, que la senal `paso contra nodo` levanta por encima de `0,60`, y por tanto digo que la senal se equivoca tres veces sobre el mismo paso de cinco palabras | `8.1` y `8.2.a` | **DENTRO** |
| **6** | firmo `0` PUENTE en los `19` pasos de la tanda, leidos uno a uno contra su renglon | `5.5` | **DENTRO** |

---

## 11. LA TABLA DE CIERRE DE ESTA APERTURA

| lo que traigo | medida | instrumento, corrido en esta fase |
|---|---|---|
| **`ACTA ANTERIOR LEIDA: 9c1eced05cb9f9b265e2f94e3a17e188af43b185`** | huella identica a la del arbol | `git hash-object`, seccion `1` |
| **heredados entregados por el arnes** | `0`, y la tarea bloqueante de `48.9.d` **existe** y el instrumento no la ve | `python forja.py herencia` y `grep -n`, seccion `1.1` |
| **el lote de la vuelta** | `3` candidatos nuevos y `9` fichas corregidas, cero lineas en `dataset/`, `bitacora/` y `censos/` | `git diff --name-status`, seccion `4` |
| **fidelidad `D.30` de la tanda** | `19` pasos, `19` TRANSCRIPCION, `0` PUENTE, leidos por mi contra `L315`, `L317`, `L321` y `L323` | `sed` sobre el fuente, secciones `5.1` a `5.3` |
| **`PASOS INVENTADOS`, `cap_04`, tanda de la vuelta `50`** | `0,00` por ciento sobre `19` pasos, por debajo del tope de `10` de `8.1` | conteo de pasos por capitulo, seccion `5.5` |
| **la frontera de `cap_04`** | `22` nodos en `21` piezas, y `22` fichas en esas mismas `21` piezas | `.v46/frontera.py` y el mapeo, seccion `6` |
| **`d036`** | **PAGADA**: las `8` cifras nuevas caen en mi `wc -w` | recuento contra el fuente, seccion `7.1` |
| **`d038`** | **ROTA**: el comando que el pago declara en `2` da `3` hoy | `grep -l`, seccion `7.2` |
| **poblacion del barrido** | `393`, o sea `346` del grafo mas `47` de bandejas, contada por mi y por la aduana | `wc -l`, `ls` y `forja.py informe`, secciones `3.1` y `8` |
| **clases a ciegas** | `12` pares, `12` SANO, cero CONTINUA, cero REPITE, cero MUTUO | los tres informes, seccion `8.1` |
| **gate, guiones, resolutor** | verdes | `forja.py`, seccion `3` |
| **pruebas de aceptacion** | `318` pruebas, `3` fallos y `1` error, **y las cuatro trazas nombran ficheros retirados por esta misma fase** | `tests/test_aceptacion.py`, seccion `3.2` |
| **lo que dejo sin medir** | seis piezas, con su motivo | seccion `9` |
| **mis discutibles** | `6`, marcados antes de ver el reporte | seccion `10` |

**NO ESCRIBO `docs/loop/PARA_ALEXIS.md` desde esta fase**, que corresponde al acta y no a la
apertura. **No commiteo**: el arnes sella esta pagina.
---

## 12. EL BARRIDO DEL REMEDIO, CORRIDO COMO OPERACION FINAL SOBRE ESTA PAGINA

**HEREDADO 1, recuperado en la seccion `1.1`: CUMPLIDO.** Esta seccion se corre cuando el resto de
la pagina ya esta escrito, y su salida va pegada debajo sin que despues se anada una linea de prosa.
El remedio que comprueba es el `REMEDIO 1` de la `ACTA 46`: un superlativo mio lleva debajo la lista
ordenada entera que lo sostiene, y el camino que la `ACTA 48` eligio para que no se rompa es de
orden de operaciones y no de memoria.

**LA CUENTA QUE ESTA PAGINA PUBLICA ES LA CABECERA PEGADA DEBAJO**, que sale del fichero que el
arnes va a sellar. Lo que va despues de este parrafo son lineas sangradas, o sea salida de
instrumento, y el propio barrido las descarta de su cuenta de prosa.

    $ python .v49aud/17_superlativos.py
    SUPERLATIVOS, que es lo que el remedio obliga a contestar: 0 golpes en mi prosa, 1 lineas sangradas (salida de instrumento) descartadas
    
    AFIRMACIONES UNIVERSALES, que no las pide el remedio y las barro igual: 7 golpes en mi prosa, 12 lineas sangradas (salida de instrumento) descartadas
       linea 85   [negativa universal        ] NINGUN         ...**NO ESCRIBO NINGUN `NO APLICA`** en esta tabla...
       linea 123  [negativa universal        ] ninguna        ...recuperado de `git` ni por ninguna otra via `REPORTE.md`, `ult...
       linea 420  [negativa universal        ] ninguna        ...L323` a la pieza `P44` y a ninguna otra, y eso lo...
       linea 645  [negativa universal        ] ninguna        ...ninguna otra. **Lo que falla es la...
       linea 800  [negativa universal        ] ningun         ...sin fusion y sin degradar a ningun nodo vivo, y los seis pares...
       linea 825  [negativa universal        ] ninguna        ...es de milesimas y no mueve ninguna clase hoy, pero **la senal...
       linea 829  [negativa universal        ] ninguna        ...y **ese nodo no aparece en ninguna de las tres listas de vecin...
    
