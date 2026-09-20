# APERTURA CIEGA DE LA VUELTA 52, lote 7 (`grove_high_output`), `cap_05`: **LOS SEIS CANDIDATOS DE LA SECCION DEL UNO A UNO, LEIDOS CONTRA EL LIBRO ANTES DE VER EL REPORTE**

*Fase ciega del auditor (`D.34`, `D.34.2`, `D.38.3`, `D.38.4`, `D.38.5`, `D.40`). Modo
austero (`D.47`): no repito lo que el registro ya dice. **Toda cifra de esta pagina sale de un
instrumento corrido en ESTA fase y va con su salida literal pegada.***

> **LO QUE NO TENGO DELANTE, DICHO POR EL REGISTRO Y NO POR MI.** La linea que el arnes
> escribio para este turno, leida por mi en `docs/loop/loop.log`, que **no** se retira:
>
>     $ tail -3 docs/loop/loop.log
>     [2026-09-19 18:44:37] VUELTA 8 : APERTURA CIEGA (claude-opus-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl
>     [2026-09-19 18:44:37]   hereda 3 remedio(s) del acta anterior, entregados en el prompt (D.40)
>     [2026-09-19 18:44:37]   y solo eso: remedios con su motivo, sin cifras ni conclusiones (D.52)
>
> **SON CUATRO Y LOS NOMBRA EL LOG: `REPORTE.md`, `ultimo_extractor.json`,
> `ultimo_auditor.json` y `CREDITO_serial.jsonl`.** No he recuperado ninguno, ni de `git` ni
> por ninguna otra via.
>
> **Y UNA DISCREPANCIA QUE DECLARO EN VEZ DE RESOLVER COPIANDO** (seccion `1`, *el instrumento
> manda*): **el aviso de mi prompt nombra `docs/loop/loop.log` entre los que no estan, y
> `loop.log` SI esta.** La linea del propio log no lo lista entre los retirados, y
> `AUDITOR_FORJA.md` seccion `1.5` sigue escribiendo que el arnes retira cuatro ficheros
> **incluyendo** `loop.log`, que ya no es lo que el arnes hace. **La cuenta sigue siendo
> cuatro; el cuarto ya no es `loop.log`, es `CREDITO_serial.jsonl`.** Lo dejo escrito para el
> turno normal, que es donde se arregla una pagina de protocolo.

---

## 0. LAS CUATRO DECLARACIONES QUE EL ARNES EXIGE, CON SU SALIDA PEGADA

    ACTA ANTERIOR LEIDA: 6835eb9a76f047e7384711f90879baf5918b45a8
    HEREDADO 1: CUMPLIDO
    HEREDADO 2: CUMPLIDO
    HEREDADO 3: CUMPLIDO

**Y NO LAS ESCRIBO DE MEMORIA.** La huella que el prompt me entrega es la del fichero que he
abierto, y lo compruebo con el instrumento de `git`:

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    6835eb9a76f047e7384711f90879baf5918b45a8

**Identica a la que el prompt entrega.** Abrir `ACTA_AUDITOR.md` en esta fase es lo que `D.40`
manda expresamente: es obra mia y no del extractor, y no es ninguno de los cuatro que `D.34.2`
retira.

### 0.1. `HEREDADO 1`: **CUMPLIDO**, y se comprueba con esta pagina ya dentro del arbol

> `1` **Toda cifra de ESTADO que yo publique se mide DESPUES de la operacion que la cambia**, y
> si mi propia escritura la mueve, se remide con la escritura ya dentro y se publica la de
> despues.

**APLICA**, y no lo declaro NO APLICA aunque la tentacion estaba: esta pagina publica cifras de
estado (`346` del grafo, `59` de bandejas, `405` de poblacion, `84` pasos de `cap_05`). **La
unica operacion que las podria mover en esta fase es la mia**, que es escribir este fichero.
Asi que las remido **con este fichero ya escrito en el arbol** y publico las de despues. La
salida de esa remedicion esta pegada en `9.1`.

### 0.2. `HEREDADO 2`: **CUMPLIDO**

> `2` **Toda division que yo publique lleva su numerador y su denominador escritos en la misma
> celda**, y se rehace antes de cerrar.

**APLICA.** Los cocientes de esta pagina son cuatro y los cuatro llevan sus dos numeros en su
celda: **`0` PUENTE de `35` pasos**, **`6` piezas de `6`**, **`35` de los `84` pasos de
`cap_05`** y **`405` que es `346` mas `59`**. Rehechos uno a uno en `9.2`.

### 0.3. `HEREDADO 3`: **CUMPLIDO**, y por construccion

> `3` **Ninguna cifra mia sale de un `grep -c` sobre la salida de un instrumento que publica su
> propio recuento**: se lee el recuento del instrumento.

**APLICA.** La cifra de poblacion de esta pagina **la escribe el propio instrumento de la casa**
en su frase hecha (`aduana.Poblacion`), y no la recuento yo por fuera:

    $ python -u barrido.py            (mi guion de barrido, fuera del arbol; ver 3)
    POBLACION DEL BARRIDO: 405   (346 del grafo mas 59 que esperan en bandejas)

**Y la de pasos de `cap_05` igual**, del contador de la casa, que publica su propio total:

    $ python scripts/muestra_fidelidad.py --libro grove_high_output --capitulos cap_05 --semilla apertura-v52
      --- cap_05: ENTERO, 84 paso(s), no hay muestra que elegir

**Donde use `ls | wc -l` para mirar una bandeja, la cifra que PUBLICO es la del instrumento**, y
las dos se cruzan en `9.2`: mis `346` mas `59` dan los `405` que el instrumento imprime solo.
**El unico `grep -c` que esta pagina escribe es el de la seccion `1`, y esta escrito para decir
que NO lo uso**, con el motivo al lado. **Lo digo asi, y no como una busqueda negativa** (seccion
`1.1`): no cito que no haya ninguno, senialo el que hay y para que esta.

---

## 1. EL HUECO DE ACTA, QUE VA ANTES QUE NADA (seccion `1.0`)

**NO HAY HUECO.** La ultima acta escrita es la `ACTA 50` y cubre la **vuelta 51**, que es la
inmediatamente anterior a la que vengo a auditar, la **52**:

    $ grep -n "^# ACTA " docs/loop/ACTA_AUDITOR.md | tail -2 | cut -c1-110
    37102:# ACTA 49. VUELTA 50, lote 7 (`grove_high_output`), `cap_04`: **LA TANDA ES BUENA Y SU CIER
    37722:# ACTA 50. VUELTA 51, lote 7 (`grove_high_output`), `cap_05`: **LA TANDA ES BUENA, SUS TRES

**Y AQUI ESTA LA MITAD DE `HEREDADO 3` EN ACTO:** lo natural para esto era `grep -c "^# ACTA "`
y **publicar el numero de actas**. No lo hago, porque para saber si hay hueco **no hace falta
contarlas**: hace falta leer la ultima y ver a que vuelta cubre. **Leida: `ACTA 50`, vuelta
`51`. Hueco: ninguno.**

## 2. EL REGIMEN DE ESTA VUELTA, Y POR QUE ESTA FASE EXISTE (`D.58`)

`D.58` se escribio **dentro de la vuelta que audito** (commit `9ec9b3c`, `18:15:47`, con su
decision archivada en `docs/loop/paradas/2026-09-19-dos-regimenes-DECISION.md`) y dice que en
una vuelta de extraccion **no hay fase ciega, ni sello, ni testigo**. **Y yo estoy en una fase
ciega.** No es una contradiccion, y lo mido antes de escribirlo:

    $ grep -n "arranque:" docs/loop/loop.log | tail -1
    2632:[2026-09-19 00:12:29] arranque: rama extraccion-mundo-11, MODO_INSERCION=insertar

**LECTURA:** la corrida abrio en `MODO_INSERCION=insertar`, que es el **regimen pesado**, y en
el pesado la fase ciega sigue viva. **Lo que decide el regimen es la bandera con la que la
corrida arranco, no lo que la vuelta acabase tocando.** Esta vuelta no toco el grafo aunque la
puerta estuviese abierta, y aun asi me toca sello. **Por eso escribo esta pagina.**

### 2.1. **UNA DISCREPANCIA DENTRO DE LA PROPIA DECISION QUE ABRIO EL REGIMEN, MEDIDA CON SU INSTRUMENTO**

La decision del fundador del 19 sep, en su punto `3`, ordena que **la cadencia de saneamiento la
haga cumplir el arnes** y cierra escribiendo **`La proxima es la 53`**. El encargo que se escribio
en el mismo commit declara la `53` de **EXTRACCION** y dice que **la `54` sera la de saneamiento**.
**Las dos no pueden ser ciertas, y el instrumento que esa misma decision mando construir contesta:**

    $ python scripts/deuda.py --clase 53
    LIBRE
      van 4 de 5 desde la ultima de saneamiento (la 49), con 17 deuda(s) esperando
    $ python scripts/deuda.py --clase 54
    SANEAMIENTO
      han pasado 5 vuelta(s) desde la ultima de saneamiento (la 49) y la cadencia es 5, con 17 deuda(s) pendientes

**EL CODIGO DICE `54`, Y EL ENCARGO ESCRITO LE HACE CASO.** Lo que queda descuadrado es **la frase
de la decision**, que dice `53`. **No lo resuelvo copiando y no lo adjudico aqui**: la decision es
del fundador y la sede de una decision del fundador no es mi apertura. **Lo declaro con las dos
salidas delante** para que el turno normal lo lleve donde corresponde. **Y anoto lo que NO
compruebo**: el `17` es lo que el instrumento dice hoy, y el encargo de la `53` escribe `19`
porque se escribio antes del ultimo commit de la vuelta. **Cual de los dos numeros corresponde a
que momento es cuenta del turno normal**, no de esta pagina.

## 3. LA POBLACION Y LOS UMBRALES DE MI BARRIDO (`D.38.4`, `D.38.5`)

**Grafo mas bandejas**, que es la poblacion que `D.38.4` me manda y la misma que la aduana mide
desde `D.38.5`, asi que **mi cifra y la del informe ya son comparables: si no cuadran es
discrepancia de verdad y no de metodo.**

    $ python -u barrido.py
    POBLACION DEL BARRIDO: 405   (346 del grafo mas 59 que esperan en bandejas)
    UMBRALES: similitud_texto 0.35  familia_id 0.30  paso_contra_nodo 0.60

> **QUE ES `barrido.py` Y POR QUE NO ES `forja.py informe`, QUE ES LO QUE HABRIA PREFERIDO.** Es
> un guion mio **que vive fuera del arbol** (en el scratchpad de la sesion, para no mover ni un
> byte del repo en esta fase) **y que no calcula nada por su cuenta**: carga la poblacion con
> `aduana.poblacion_de_bandejas`, los umbrales con `config.cargar` y mide cada par con
> `aduana.medir`, que son **las mismas funciones que corre la aduana**. Lo que hace de mas es
> **imprimir la cola entera y no solo lo que pasa umbral**, que es lo que me deja ver si un
> vecino se queda a las puertas. **Lo que no hace es escribir**: ni `dataset/`, ni `bitacora/`,
> ni `censos/`, ni `config/`. El motivo de no correr los seis informes enteros esta medido en
> `8.c`, y es el reloj.

**LOS `59` DE BANDEJA SON `56` DE `grove_high_output` MAS `3` DE `marquet_turn_the_ship`**, y
los `163` de `cuarentena/ensayo_referencia_163/` quedan fuera **con su motivo escrito en
`src/aduana.py`**: son un catalogo de referencia ajeno que la puerta rechazaria de todas formas,
asi que no abren cola de lectura. **El criterio no es una lista de nombres, es la tabla
canonica.**

    $ for d in cuarentena/*/; do printf ... "$d" "$(ls $d*.json | wc -l)"; done
    cuarentena/ensayo_referencia_163/         163
    cuarentena/grove_high_output/             56
    cuarentena/marquet_turn_the_ship/         3
    cuarentena/onu_consumidor/                0
    cuarentena/scott_radical_candor/          0
    cuarentena/smart_who/                     0
    cuarentena/zhuo_manager/                  0

## 4. QUE MATERIAL ES ESTE, SACADO DE `git` Y NO DE LAS FECHAS DE LOS FICHEROS

    $ git diff --name-status d8016d4 HEAD -- cuarentena/
    A  cuarentena/grove_high_output/acumular_asuntos_importantes_fichero_espera.json
    A  cuarentena/grove_high_output/alentar_asuntos_corazon_vigilar_final_reunion.json
    A  cuarentena/grove_high_output/conducir_reunion_individual_telefono_distancia.json
    M  cuarentena/grove_high_output/cubrir_indicadores_problemas_reunion_individual.json
    A  cuarentena/grove_high_output/facilitar_expresion_subordinado_pregunta_mas.json
    M  cuarentena/grove_high_output/fijar_duracion_lugar_reunion_individual.json
    M  cuarentena/grove_high_output/fijar_frecuencia_reunion_individual_madurez_tarea.json
    M  cuarentena/grove_high_output/infundir_regularidad_reunion_proceso.json
    M  cuarentena/grove_high_output/preparar_guion_reunion_individual_subordinado.json
    A  cuarentena/grove_high_output/programar_reunion_individual_cadena.json
    A  cuarentena/grove_high_output/tomar_notas_copia_guion_reunion_individual.json
    M  cuarentena/grove_high_output/usar_tres_clases_reunion_proceso.json

**SEIS NUEVOS Y SEIS TOCADOS**, y los seis tocados son los seis hermanos de la vuelta 51. Los
seis nuevos son los que clasifico; los seis tocados van en la seccion `8`.

**NINGUNO DE LOS SEIS VIVE YA EN EL GRAFO Y NINGUNO CHOCA CON OTRO DE SU BANDEJA:**

    $ python -c "... los seis ids contra los del grafo ..."
    ids en el grafo: 346
    acumular_asuntos_importantes_fichero_espera          ya en el grafo: False
    alentar_asuntos_corazon_vigilar_final_reunion        ya en el grafo: False
    conducir_reunion_individual_telefono_distancia       ya en el grafo: False
    facilitar_expresion_subordinado_pregunta_mas         ya en el grafo: False
    programar_reunion_individual_cadena                  ya en el grafo: False
    tomar_notas_copia_guion_reunion_individual           ya en el grafo: False

    $ python -c "... choque de ids dentro de la bandeja ..."
    ids distintos: 56 de 56 ficheros
    ids repetidos: ninguno

**Y LOS SEIS LLEGAN CON `nodos_previos` Y `nodos_siguientes` VACIOS**, que es lo que mi propio
encargo mando: las aristas se declaran por lectura hoy y **se cablean el dia de la insercion**.

    $ python -c "... prev y sig de los seis ..."
    PREV: [] SIG: []      (los seis, sin excepcion)

## 5. LA FRONTERA: LOS SEIS TRAMOS RECOMPUTADOS POR MI, UNO A UNO

**El corte de esta tanda no lo eligio el extractor: lo fijo mi propio encargo** de la `ACTA 50`,
que copio la tabla `LL.4.b` de la frontera de la vuelta 50. Asi que aqui no adjudico el corte:
**compruebo que cada candidato se pega al tramo que su encargo le dio**, y recomputo las seis
cifras de palabras con `wc -w` sobre el libro.

    $ for t in "P15 45,47" "P16 49,49" "P17 51,51" "P18 53,53" "P19 55,55" "P20 57,57"; do ... sed -n "$2p" fuentes/grove_high_output/cap_05.md | wc -w; done
    P15  L45,47  wc -w = 134
    P16  L49,49  wc -w = 157
    P17  L51,51  wc -w = 64
    P18  L53,53  wc -w = 117
    P19  L55,55  wc -w = 85
    P20  L57,57  wc -w = 74

| pieza | tramo | palabras que mi encargo publica | **palabras que mido hoy** | candidato que sale de ella | pasos |
|---|---|---:|---:|---|---:|
| `P15` | `L45` a `L47` | `134` | **`134`** | `facilitar_expresion_subordinado_pregunta_mas` | `6` |
| `P16` | `L49` | `157` | **`157`** | `tomar_notas_copia_guion_reunion_individual` | `7` |
| `P17` | `L51` | `64` | **`64`** | `acumular_asuntos_importantes_fichero_espera` | `4` |
| `P18` | `L53` | `117` | **`117`** | `alentar_asuntos_corazon_vigilar_final_reunion` | `8` |
| `P19` | `L55` | `85` | **`85`** | `conducir_reunion_individual_telefono_distancia` | `5` |
| `P20` | `L57` | `74` | **`74`** | `programar_reunion_individual_cadena` | `5` |
| | | | | **`6` candidatos de `6` piezas** | **`35`** |

**LAS SEIS SALEN AL DIGITO Y LA CORRESPONDENCIA ES UNO A UNO**: seis piezas, seis candidatos,
ninguna pieza con dos nodos y ningun nodo a caballo de dos piezas. **Y la cita que cada ficha
lleva dentro nombra su pieza y su tramo exactos**, que no es poco despues de `d038`:

    $ python -c "... UNIDAD DE ORIGEN de cada ficha ..."
    facilitar_expresion...   Sale de la PIEZA P15 de la frontera de cap_05 ... L45 a L47, 134 palabras.
    tomar_notas_copia...     Sale de la PIEZA P16 de la frontera de cap_05 ... L49 a L49, 157 palabras.
    acumular_asuntos...      Sale de la PIEZA P17 de la frontera de cap_05 ... L51 a L51, 64 palabras.
    alentar_asuntos...       Sale de la PIEZA P18 de la frontera de cap_05 ... L53 a L53, 117 palabras.
    conducir_reunion...      Sale de la PIEZA P19 de la frontera de cap_05 ... L55 a L55, 85 palabras.
    programar_reunion...     Sale de la PIEZA P20 de la frontera de cap_05 ... L57 a L57, 74 palabras.

**LOS `35` PASOS SON `35` DE LOS `84` QUE EL CONTADOR DE LA CASA DA PARA `cap_05`**, y los otros
`49` son los de la vuelta 51, que firme en la `ACTA 50`. **`49` mas `35` dan `84`**, y esa suma
la cierra el instrumento sin que yo la teclee:

    $ python scripts/muestra_fidelidad.py --libro grove_high_output --capitulos cap_05 --semilla apertura-v52
    MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO (D.58)
      libro    : grove_high_output
      semilla  : apertura-v52
      capitulos: cap_05

      RELEIDO ENTERO : cap_05
      POR MUESTRA    : ninguno, 15 pasos cada uno

      --- cap_05: ENTERO, 84 paso(s), no hay muestra que elegir

    $ python -c "... pasos por candidato nuevo ..."
    acumular_asuntos_importantes_fichero_espera           4 pasos
    alentar_asuntos_corazon_vigilar_final_reunion         8 pasos
    conducir_reunion_individual_telefono_distancia        5 pasos
    facilitar_expresion_subordinado_pregunta_mas          6 pasos
    programar_reunion_individual_cadena                   5 pasos
    tomar_notas_copia_guion_reunion_individual            7 pasos
    TOTAL DE LOS SEIS: 35 pasos

> **LO QUE EL CONTADOR DE LA CASA NO DICE, Y LO DIGO YO:** los `84` son los pasos de los
> candidatos de `cap_05` **que hay en la bandeja y en el archivo hoy**, y `35` de ellos son de
> esta tanda porque los otros `49` los conte y los firme yo en la vuelta anterior. **La resta
> `84` menos `35` igual a `49` es la que cierra el circulo**, y no la hace el instrumento: la
> hago yo, con los dos numeros delante.

## 6. FIDELIDAD `D.30`, PASO A PASO Y CONTRA SU RENGLON: **`0` PUENTE DE `35`**

**COMO LO HE LEIDO, Y ES LA MITAD DEL VALOR DE ESTA PAGINA:** abri el libro por las seis lineas,
lei los `35` pasos de las seis fichas, y **adjudique cada paso contra su renglon antes de abrir
el bloque de veredicto que la ficha lleva dentro**. Lo que juzgo aqui es el producto (titulo,
condiciones, entregable, pasos) contra el texto fuente, **no la razon que el extractor escribio
para si mismo**.

### 6.1. `P15`, `L45` y `L47`: `facilitar_expresion_subordinado_pregunta_mas`, `6` pasos

| paso | donde lo dice el libro | clase |
|---:|---|---|
| `1` facilita que exprese lo que pasa y lo que le molesta | `L45`: *He should facilitate the subordinate's expression of what's going on and what's bothering him* | **TRANSCRIPCION** |
| `2` ponte ahi para aprender y para orientar | `L45`: *The supervisor is there to learn and to coach* | **TRANSCRIPCION** |
| `3` como lo resume Drucker | `L45`: la cita de Drucker entera, *The good time users among managers do not talk to their subordinates about their problems but they know how to make the subordinates talk about theirs* | **TRANSCRIPCION** |
| `4` aplica el principio de direccion didactica, preguntar una vez mas | `L47`: *By applying Grove's Principle of Didactic Management, "Ask one more question!"* | **TRANSCRIPCION** |
| `5` cuando creas que ya lo dijo todo, hazle otra pregunta | `L47`: *When the supervisor thinks the subordinate has said all he wants to about a subject, he should ask another question* | **TRANSCRIPCION** |
| `6` manten el flujo pinchando con preguntas hasta llegar al fondo | `L47`: *keep the flow of thoughts coming by prompting the subordinate with queries until both feel satisfied that they have gotten to the bottom of a problem* | **TRANSCRIPCION** |

**`0` PUENTE de `6`.** Lo unico del tramo que no llega a paso son las dos preguntas con las que
el libro abre cada parrafo (*What is the role of the supervisor* y *How is this done*), que son
armazon y no procedimiento.

### 6.2. `P16`, `L49`: `tomar_notas_copia_guion_reunion_individual`, `7` pasos

| paso | donde lo dice el libro | clase |
|---:|---|---|
| `1` una copia del guion en cada lado | `L49`: *both the supervisor and subordinate should have a copy of the outline* | **TRANSCRIPCION** |
| `2` que los dos tomen notas sobre ella | `L49`: *and both should take notes on it* | **TRANSCRIPCION** |
| `3` sirve a varios propositos, el primero de cabeza, y casi nunca se vuelven a mirar | `L49`: *which serves a number of purposes*, mas *I take notes in just about all circumstances, and most often end up never looking at them again*, mas *to keep my mind from drifting and also to help me digest the information I hear and see* | **TRANSCRIPCION, con matiz de persona: ver `7.1`** |
| `4` toma las notas en forma de guion, que obliga a clasificar | `L49`: *Since I take notes in outline form, I am forced to categorize the information logically, which helps me to absorb it* | **TRANSCRIPCION, mismo matiz** |
| `5` lo que simboliza escribirlo es igual de importante, y muchos asuntos llevan a accion del subordinado | `L49`: *Equally important is what "writing it down" symbolizes. Many issues in a one-on-one lead to action required on the part of the subordinate* | **TRANSCRIPCION** |
| `6` la nota inmediata implica compromiso, como un apreton de manos | `L49`: *the act implies a commitment, like a handshake, that something will be done* | **TRANSCRIPCION** |
| `7` haz el seguimiento en la reunion siguiente | `L49`: *The supervisor, also having taken notes, can then follow up at the next one-on-one* | **TRANSCRIPCION** |

**`0` PUENTE de `7`**, y **dos pasos con un matiz que declaro en `7.1` y que NO cuento como
puente**, porque el contenido esta en el renglon.

### 6.3. `P17`, `L51`: `acumular_asuntos_importantes_fichero_espera`, `4` pasos

| paso | donde lo dice el libro | clase |
|---:|---|---|
| `1` usa un fichero de espera compartido por los dos | `L51`: *using a "hold" file where both the supervisor and subordinate* | **TRANSCRIPCION** |
| `2` acumula ahi lo importante pero no del todo urgente, para la reunion siguiente | `L51`: *accumulate important but not altogether urgent issues for discussion at the next meeting* | **TRANSCRIPCION** |
| `3` esa clase de fichero aplica el principio de produccion del agrupamiento | `L51`: *This kind of file applies the production principle of batching* | **TRANSCRIPCION** |
| `4` el ahorro sale de reducir al minimo el contacto improvisado, las llamadas y las visitas sin avisar, que son las interrupciones de antes | `L51`: *saves time for both involved by minimizing the need for ad hoc contact*, con *phone calls, drop-in visits*, y *which constitute the interruptions we considered earlier* | **TRANSCRIPCION** |

**`0` PUENTE de `4`.** El *real time-saver* con el que el libro abre el parrafo esta en el
entregable de la ficha, que es su sitio.

### 6.4. `P18`, `L53`: `alentar_asuntos_corazon_vigilar_final_reunion`, `8` pasos

| paso | donde lo dice el libro | clase |
|---:|---|---|
| `1` alienta los asuntos de corazon a corazon | `L53`: *should also encourage the discussion of heart-to-heart issues during one-on-ones* | **TRANSCRIPCION** |
| `2` es el foro perfecto para los problemas sutiles y profundos | `L53`: *this is the perfect forum for getting at subtle and deep work-related problems affecting his subordinate* | **TRANSCRIPCION** |
| `3` si esta satisfecho con su rendimiento | `L53`: *Is he satisfied with his own performance?* | **TRANSCRIPCION** |
| `4` si alguna frustracion o algun obstaculo le carcome | `L53`: *Does some frustration or obstacle gnaw at him?* | **TRANSCRIPCION** |
| `5` si tiene dudas sobre adonde va | `L53`: *Does he have doubts about where he is going?* | **TRANSCRIPCION** |
| `6` ponte en guardia contra el asunto sacado en momento inoportuno | `L53`: *wary of the "zinger," which is a heart-to-heart issue brought up at an awkward time* | **TRANSCRIPCION** |
| `7` la mayoria de las veces llegan cerca del final | `L53`: *More often than not, these come near the end of a meeting* | **TRANSCRIPCION** |
| `8` lo que pasa si lo dejas correr, y los cinco minutos | `L53`: *he's unhappy and has been looking outside for a job and give you only five minutes to deal with it* | **TRANSCRIPCION** |

**`0` PUENTE de `8`.** El paso `6` traduce `zinger` **por su definicion** en vez de por la
palabra, y la definicion es la que el propio renglon escribe dos palabras despues. **No es
invencion: es el libro definiendo su propio termino.**

### 6.5. `P19`, `L55`: `conducir_reunion_individual_telefono_distancia`, `5` pasos

| paso | donde lo dice el libro | clase |
|---:|---|---|
| `1` tenla por telefono cuando la organizacion este repartida | `L55`: *Long-distance telephone one-on-ones have become necessary because many organizations are now spread out geographically* | **TRANSCRIPCION** |
| `2` el supervisor con el guion antes de empezar | `L55`: *the supervisor must have the outline before the meeting begins* | **TRANSCRIPCION** |
| `3` las dos partes toman notas | `L55`: *both parties should take notes* | **TRANSCRIPCION** |
| `4` como no ves al otro, la toma de notas no funciona igual | `L55`: *Because you can't see the other participant in the meeting, note-taking can't work in the same way as in a face-to-face meeting* | **TRANSCRIPCION** |
| `5` intercambiad las notas despues, para saber a que se comprometio cada uno | `L55`: *Exchanging notes after the meeting is a way to make sure each knows what the other committed himself to do* | **TRANSCRIPCION** |

**`0` PUENTE de `5`**, con una **omision** que declaro en `7.2` y que no es puente: el renglon
dice ademas que estas reuniones *can work well enough with proper preparation and attention*, y
la ficha no lo recoge. **Omitir no es inventar**, y `D.30` cuenta lo segundo.

### 6.6. `P20`, `L57`: `programar_reunion_individual_cadena`, `5` pasos

| paso | donde lo dice el libro | clase |
|---:|---|---|
| `1` programalas en cadena | `L57`: *should be scheduled on a rolling basis* | **TRANSCRIPCION** |
| `2` fija la siguiente al terminar la que se esta teniendo | `L57`: *setting up the next one as the meeting taking place ends* | **TRANSCRIPCION** |
| `3` asi se tienen en cuenta los demas compromisos y se evitan cancelaciones | `L57`: *Other commitments can thereby be taken into account and cancellations avoided* | **TRANSCRIPCION** |
| `4` el caso contrario del horario fijo, el segundo miercoles y las vacaciones | `L57`: *such as every second Wednesday morning, and if the subordinate's vacation happens to fall on that date, the meeting is not going to occur* | **TRANSCRIPCION** |
| `5` en cadena eso se evita facilmente | `L57`: *By scheduling on a rolling basis, this can be easily avoided* | **TRANSCRIPCION** |

**`0` PUENTE de `5`.**

### 6.7. **LA CIFRA DE FIDELIDAD DE MI LECTURA CIEGA**

| capitulo | pasos escritos | **pasos inventados que yo cuento** | por ciento |
|---|---:|---:|---:|
| `cap_05`, piezas `P15` a `P20` | **`35`** | **`0`** | **`0` de `35`, que es `0,00`** |

**FIRMO `0` PUENTE DE `35` PASOS**, leidos por mi contra `L45`, `L47`, `L49`, `L51`, `L53`,
`L55` y `L57`, **antes de ver el reporte**. El disparador del `10` por ciento no se acerca:
`0` de `35` es `0,00`.

## 6.8. **MI CLASIFICACION DE LOS SEIS, UNO A UNO Y CON LA VARA DELANTE**

**Esto es lo que vengo a hacer en esta fase**, y lo escribo antes de ver una sola linea del
reporte. La pregunta es la de la vara madre (`6.1`), una y con direccion: **el candidato CONTINUA
el trabajo de lo que ya existe o lo REPITE.**

| # | candidato | **mi clase** | el vecino mas fuerte que yo veo, por LECTURA | que queda fuera, que es lo que decide |
|---:|---|---|---|---|
| `1` | `facilitar_expresion_subordinado_pregunta_mas` (`P15`) | **NODO LEGITIMO, SANO** | `dirigir_reunion_individual_semanal` (grafo, `zhuo_manager`) | del candidato: el principio de preguntar una vez mas y la cita de Drucker, que son procedimiento propio. Del vecino: las cuatro ideas de preparacion de Zhuo. **Procedimiento en los dos lados** |
| `2` | `tomar_notas_copia_guion_reunion_individual` (`P16`) | **NODO LEGITIMO, y CONTINUA de `P14`** | `preparar_guion_reunion_individual_subordinado` (bandeja, vuelta 51) | del candidato: las dos copias, la nota en forma de guion, lo que la nota simboliza y el seguimiento. Del vecino: quien prepara el guion y por que. **El guion se PREPARA en `P14` y se ANOTA en `P16`: dos actos, dos nodos** |
| `3` | `acumular_asuntos_importantes_fichero_espera` (`P17`) | **NODO LEGITIMO, y CONTINUA de la politica de agrupamiento** | `agrupar_interrupciones_subordinados_reuniones_regulares` (bandeja, `cap_04.md`, `P42`) | ver `7.3`: fuera del hijo queda la politica de mandar agrupar; fuera de la madre queda **el artefacto compartido y su criterio de admision**. **Es el par mas discutible de la tanda y lo marco yo** |
| `4` | `alentar_asuntos_corazon_vigilar_final_reunion` (`P18`) | **NODO LEGITIMO, SANO** | `cubrir_indicadores_problemas_reunion_individual` (bandeja, `P13`) | del candidato: las tres preguntas y **la guardia contra el asunto grave sacado al final**, que no esta en ningun otro sitio. Del vecino: los indicadores, lo ocurrido desde la anterior y el problema potencial |
| `5` | `conducir_reunion_individual_telefono_distancia` (`P19`) | **NODO LEGITIMO, variante por medio** | `tomar_notas_copia_guion_reunion_individual` (`P16`, esta misma tanda) | **es el unico par de la tanda donde dos fichas comparten dos pasos** (el guion por delante y las notas de las dos partes), y el libro los repite el mismo. Fuera del `P19` quedan la condicion de distancia, el no poder ver al otro y **el intercambio de notas al terminar**, que solo existe aqui. **Procedimiento en los dos lados: no es gemelo** |
| `6` | `programar_reunion_individual_cadena` (`P20`) | **NODO LEGITIMO, SANO** | `fijar_frecuencia_reunion_individual_madurez_tarea` (bandeja, vuelta 51) | del candidato: **cuando se fija la siguiente** (al terminar la que se tiene) y el contraejemplo del horario fijo. Del vecino: **cada cuanto** se tiene, por madurez de tarea. **Cada cuanto y cuando se agenda no son la misma decision** |

> ### **LO QUE ESTA TABLA NO DICE, Y SE DICE**
>
> **No firmo ningun veredicto de insercion aqui**, porque ninguno de los seis entra hoy: el lote
> `7` esta ABIERTO y `D.39` no los deja pasar. Lo que firmo es **la clase que yo leo hoy**, para
> que se pueda comparar con la que el extractor leyo sin que ninguno de los dos hubiese visto la
> del otro. **Las tres aristas que declaro por lectura** (`P14` a `P16`, `agrupar_interrupciones`
> a `P17`, y `P16` contra `P19` por contraste) **se cablean el dia de la insercion** y no hoy.
>
> **Y LA MITAD QUE ME FALTA LA DIGO:** esta tabla nombra al vecino mas fuerte **que yo veo
> leyendo**, y mi barrido de las tres seniales sobre los `405` estaba corriendo mientras la
> escribia. **Si el barrido levanta un vecino que esta tabla no nombra, el que se equivoco fui
> yo**, y queda escrito en `11` para que se vea.

## 7. MIS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Los marco yo y a ciegas, que es lo que los hace informativos** (seccion `5.1`). Son cuatro, y
ninguno de los cuatro es, en mi lectura, una caida.

### 7.1. **DISCUTIBLE `1`: dos pasos de `P16` convierten el testimonio de Grove en regla general**

El libro escribe en primera persona **su propia costumbre**: *I take notes in just about all
circumstances, and most often end up never looking at them again*, y *Since I take notes in
outline form, I am forced to categorize*. La ficha escribe *aunque la mayoria de las veces no se
vuelvan a mirar* y *toma las notas en forma de guion*. **Mi clase: TRANSCRIPCION, no puente.**

**POR QUE, Y ES LA REGLA DE LA CASA Y NO MI GUSTO:** el nodo es un procedimiento, y convertir
*yo hago X y me sirve para Y* en *haz X, que sirve para Y* **es exactamente lo que extraer un
procedimiento es**. Lo que `D.30` prohibe es **un paso que el libro no dice**, y los dos pasos
dicen lo que el renglon dice. **Lo marco porque la frontera esta cerca**: si un dia una ficha
generaliza un testimonio que el libro presenta como excepcion suya, eso si seria puente, y me
gustaria que la marca de hoy este escrita cuando llegue ese dia.

### 7.2. **DISCUTIBLE `2`: `P19` deja fuera la condicion con la que el libro salva la reunion por telefono**

El renglon dice que estas reuniones *can work well enough with proper preparation and
attention*, y la ficha no lo recoge en ningun paso. **Mi clase: omision, no puente**, y la ficha
**si** recoge las dos cosas concretas en que esa preparacion consiste (el guion por delante y
las notas de las dos partes), asi que lo omitido es el rotulo y no el contenido. **No la cuento
en la cifra de `6.7`.**

### 7.3. **DISCUTIBLE `3`: `P17` contra `agrupar_interrupciones_subordinados_reuniones_regulares`, que es el vecino mas fuerte de la tanda**

**Este es el par que yo habria levantado a mano si la maquina no lo levanta**, y lo leo con la
vara antes de mirar ninguna senial. **Y digo de donde viene cada uno, leido de su propia ficha y
no supuesto por su nombre:**

    $ python -c "... UNIDAD DE ORIGEN de los dos vecinos de agrupamiento ..."
    agrupar_interrupciones: UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_04.md, unidad Cap. 3, titulo textual Managerial Leverage. Sale de la PIEZA P42 de la frontera publicada en la vuelta 46 (HH.2.c), L317 a L317, 74 palabras.
    agrupar_tareas:        UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_04.md, unidad Cap. 3, titulo textual Managerial Leverage. Sale de la PIEZA P33 de la frontera publicada en la vuelta 46 (HH.2.c)

**Los dos son de `cap_04.md`, que es la unidad `Cap. 3` del libro**, y el candidato de hoy es de
`cap_05.md`, unidad `Cap. 4`. **El principio se enuncia en un capitulo y se instrumenta en el
siguiente**, que es justo la figura que una arista de continuidad existe para guardar. Los dos aplican el mismo principio (el agrupamiento) al
mismo fin (que el contacto improvisado baje), y el de la bandeja **ya nombra la reunion de uno a
uno como el sitio donde se atiende lo acumulado**.

| | |
|---|---|
| **la madre**, `agrupar_interrupciones_subordinados_reuniones_regulares` | la POLITICA: acumula las interrupciones de tus subordinados, atiendelas en las reuniones de personal y de uno a uno, manten esas reuniones con regularidad, y **pide a tu gente que agrupe sus preguntas** para esos momentos |
| **el hijo**, `P17` `acumular_asuntos_importantes_fichero_espera` (`cap_05`) | el INSTRUMENTO: **un fichero de espera compartido por las dos partes**, con un criterio de admision escrito (*importante pero no del todo urgente*) y un destino fijo (la reunion siguiente) |

**MI CLASE: CONTINUA, y no gemelo.** La vara no tiene bascula: lo que decide es **si lo que
queda fuera es procedimiento en los dos lados**, y lo es. Fuera del hijo queda la politica de
mandar agrupar y las reuniones de personal; fuera de la madre queda el artefacto compartido y su
criterio de admision. **Y tiene direccion**: el hijo anade a la madre un objeto que la madre no
nombra, no al reves. **Arista de continuidad que declaro por lectura** (`D.29`), de
`agrupar_interrupciones_subordinados_reuniones_regulares` a
`acumular_asuntos_importantes_fichero_espera`, **para cablear el dia de la insercion.**

### 7.4. **DISCUTIBLE `4`: `P15` y `P18` contra `dirigir_reunion_individual_semanal` del grafo, que es el vecino ajeno de la tanda**

El nodo `dirigir_reunion_individual_semanal` (de `zhuo_manager`, en el grafo) es el que en mi
`ACTA 50` quedo en **frontera declarada** contra `cubrir_indicadores_problemas_reunion_individual`
porque mandan cosas contrarias sobre con que se empieza la misma reunion. **La pregunta de hoy es
si los dos nuevos abren otra frontera igual, y mi respuesta es NO**, y por eso lo marco.

| par | que dice cada uno | **mi clase** |
|---|---|---|
| `P15` contra `dirigir_reunion_individual_semanal` | Grove: el supervisor facilita, aprende, orienta y pregunta una vez mas. Zhuo, paso `4`: centrala en tu persona a cargo y en lo que la ayudaria, no en ti | **NO es frontera: los dos mandan lo mismo.** Arista de contraste por concordancia, no por choque |
| `P18` contra `dirigir_reunion_individual_semanal` | Grove: alienta lo de corazon a corazon, con tres preguntas. Zhuo, paso `3`: usala para lo que de otro modo no saldria, que la motiva y cuales son sus aspiraciones | **NO es frontera: se solapan en el fin y difieren en el instrumento.** Las tres preguntas son de Grove y las cuatro ideas son de Zhuo |

**Y REGISTRO UNA PREGUNTA DE DOCTRINA SIN ABRIRLA, QUE ES LO QUE `D.55` MANDA** (la cola esta
congelada en `11` y una pregunta nueva **se registra con su medida y se deja ahi**): el par que
**si** parece mandar cosas contrarias no es de esta tanda, es
`preparar_guion_reunion_individual_subordinado` (vuelta 51, Grove: **el guion lo prepara el
subordinado**, porque el supervisor con ocho subordinados tendria que prepararlo ocho veces)
contra `dirigir_reunion_individual_semanal` paso `6` (Zhuo: **preparala tu**, con cuatro ideas
para empezar). **No lo adjudico, no abre parada y no va al banco: queda escrito con su medida
para el dia de la insercion.**

## 8. LAS SEIS FICHAS HERMANAS QUE ESTA VUELTA TOCO: **SOLO `resumen_teorico`, Y ANADE SIN BORRAR**

**Medido por diferencia contra el arbol de mi propia acta**, que es de donde tiene que salir la
base:

    $ python -c "... campos que cambian entre d8016d4 y HEAD ..."
    cubrir_indicadores_problemas_reunion_individual      campos que cambian: ['resumen_teorico']
    fijar_duracion_lugar_reunion_individual              campos que cambian: ['resumen_teorico']
    fijar_frecuencia_reunion_individual_madurez_tarea    campos que cambian: ['resumen_teorico']
    infundir_regularidad_reunion_proceso                 campos que cambian: ['resumen_teorico']
    preparar_guion_reunion_individual_subordinado        campos que cambian: ['resumen_teorico']
    usar_tres_clases_reunion_proceso                     campos que cambian: ['resumen_teorico']

    $ python -c "... longitudes y prefijo ..."
    ficha                                                   antes    ahora   delta  el viejo es prefijo del nuevo
    cubrir_indicadores_problemas_reunion_individual         10675    16335   +5660  True
    fijar_duracion_lugar_reunion_individual                  9123    11444   +2321  True
    fijar_frecuencia_reunion_individual_madurez_tarea        9623    11944   +2321  True
    infundir_regularidad_reunion_proceso                     6251     8590   +2339  True
    preparar_guion_reunion_individual_subordinado            9796    12131   +2335  True
    usar_tres_clases_reunion_proceso                         6728     9067   +2339  True

**LAS SEIS ANADEN Y NO BORRAN**, y lo digo con la prueba fuerte y no con la debil: **el texto
viejo es prefijo literal del nuevo en las seis**, asi que ni una palabra de lo que la vuelta 51
escribio se ha movido. **Y en las seis cambia un solo campo**: ni titulo, ni pasos, ni ids, ni
fuentes. **Cero pasos tocados en las seis.**

**LO QUE NO DIGO:** no digo que eso pague la deuda que dice pagar. **El contenido de lo anadido
es la razon escrita del extractor**, y leerla en esta fase seria leer lo que vengo a leer a
ciegas. **Queda para el turno normal.**

## 8.b. `cap_05` EN `12` DE `26`, COMPROBADO CON EL INSTRUMENTO Y NO CON LA MEMORIA

El criterio de que un candidato es de `cap_05` no lo pongo yo: **es el del contador de la casa**
(la ficha cita `grove_high_output/cap_05.md` dentro), y con ese criterio el capitulo tiene hoy
doce fichas escritas, **las seis de la vuelta 51 y las seis de esta**:

    $ python -c "from scripts import muestra_fidelidad as mf; ... candidatos_de('grove_high_output','cap_05')"
    cap_05 tiene 12 candidatos escritos
        acumular_asuntos_importantes_fichero_espera
        alentar_asuntos_corazon_vigilar_final_reunion
        conducir_reunion_individual_telefono_distancia
        cubrir_indicadores_problemas_reunion_individual
        facilitar_expresion_subordinado_pregunta_mas
        fijar_duracion_lugar_reunion_individual
        fijar_frecuencia_reunion_individual_madurez_tarea
        infundir_regularidad_reunion_proceso
        preparar_guion_reunion_individual_subordinado
        programar_reunion_individual_cadena
        tomar_notas_copia_guion_reunion_individual
        usar_tres_clases_reunion_proceso

**Y EL `26` LO REHAGO CON LOS DOS NUMEROS DE SU CELDA**, que es lo que `HEREDADO 2` me obliga:
los `14` que mi encargo deja fuera son `P26` a `P28` (`3`), `P31` a `P35` (`5`), `P38` a `P42`
(`5`) y `P45` (`1`), **y `3` mas `5` mas `5` mas `1` son `14`; `12` mas `14` son `26`**. La
seccion del uno a uno queda cerrada **si y solo si** `P21`, `P22` y `P23` dan cero nodos, que es
lo que mi propia frontera publica y **lo que el turno normal tiene que volver a mirar contra la
tabla**, no contra esta frase.

## 8.c. UNA MEDIDA QUE NO BUSCABA Y QUE ES LA MAS CARA DE ESTA PAGINA: **LO QUE CUESTA HOY UNA PASADA DE ADUANA, Y POR QUE SUBE**

**No la traigo de oidas: la traigo porque mi propio barrido tardaba y fui a medir por que.** Una
sola medicion par a par de la aduana cuesta esto, y el coste **va con el tamanio de la ficha
contra la que mide**:

    $ python -c "... aduana.medir(candidato, vecino) cronometrado, cuatro tamanios ..."
    TAMANIO DE LA FICHA EN LA POBLACION (caracteres de su json)
      la mayor      :  18808  cubrir_indicadores_problemas_reunion_individual
      la 10a mayor  :  14022  pedir_critica_primero_crear_seguridad_psicologica
      la mediana    :   4461  recorrer_rueda_hacer_cosas_equipo
      la menor      :   1531  registrar_fuente_canonica
      suma total    : 2065829 caracteres en 405 fichas

    COSTE DE UNA MEDICION, par a par (aduana.medir)
         7.823 s  contra cubrir_indicadores_problemas_reunion_individual    (18808 caracteres)
        13.134 s  contra pedir_critica_primero_crear_seguridad_psicologica  (14022 caracteres)
         2.812 s  contra recorrer_rueda_hacer_cosas_equipo                  (4461 caracteres)
         0.477 s  contra registrar_fuente_canonica                          (1531 caracteres)

**Y NO LO DEJO EN UNA EXTRAPOLACION: MIS SEIS BARRIDOS TRAEN SU RELOJ** y estan pegados en `11.1`.
**Suman `7649,3` s para `2424` pares**, que son **`3,155` s por par** y **`1274,9` s por candidato,
o sea `21,2` minutos de un nucleo por candidato**. Y la aduana entera cuesta mas que el barrido,
porque ademas corre sus validaciones: el `python forja.py informe` que lance al empezar **consumio
mas de `999` segundos de CPU sin llegar a terminar** (medido con `Get-Process`, con otro proceso
mio en paralelo, asi que esa cifra es de contencion y no de nucleo limpio).

**Y LO QUE ESO TIENE DE IMPORTANTE NO ES EL RELOJ, ES DE DONDE SALE EL TAMANIO:** la ficha mas
grande de las `405` es `cubrir_indicadores_problemas_reunion_individual` con `18808` caracteres,
y es una de las seis que **esta misma vuelta engordo**, `+5660` caracteres en su
`resumen_teorico` (seccion `8`). **El texto que engorda es el de la razon escrita, no el del
procedimiento**, y la senial se calcula sobre el texto entero. **Cada pago de deuda que se
escribe dentro de una ficha sube el coste de todas las pasadas de aduana que vengan despues.**

**NO LO ADJUDICO Y NO ABRO DOCTRINA** (`D.55`, la cola esta congelada en `11`): lo registro con
su medida, que es lo que esa regla manda hacer con una pregunta nueva. **Y no encargo ningun
instrumento nuevo**, que es lo que la moratoria de maquinaria me prohibe (`5.6`).

## 9. LAS DOS REMEDICIONES QUE MIS PROPIOS REMEDIOS ME OBLIGAN

### 9.1. `HEREDADO 1`: las cifras de estado, remedidas **con esta pagina ya dentro del arbol**

**Corrido DESPUES de escribir el fichero, y el propio instrumento lo dice midiendo la pagina
primero**, que es la unica manera de que se vea que el orden fue ese:

    $ python remedir.py
    LA PAGINA YA ESTA EN EL ARBOL:
      docs/loop/APERTURA_CIEGA.md   57589 bytes, 807 lineas

    CIFRAS DE ESTADO REMEDIDAS DESPUES DE ESCRIBIRLA:
      grafo dataset/nodos.jsonl        : 346
      bandejas que la aduana cuenta    : 59
      POBLACION DEL BARRIDO            : 405   (346 del grafo mas 59 que esperan en bandejas)
      pasos de cap_05 (contador de la casa): 84

**LAS CUATRO SALEN IDENTICAS A LAS QUE ESTA PAGINA PUBLICA**: `346`, `59`, `405` y `84`. **Y era
previsible y lo digo igual**: lo unico que mi turno escribe es este fichero de `docs/loop/`, que no
es sede de ninguna de las cuatro. **El remedio no me pide que la cifra cambie: me pide que la mida
despues**, y esta medida despues.

> **LO QUE ESTA REMEDICION NO CUBRE, Y SE DICE:** el tamanio y las lineas de esta pagina **son de
> antes de pegar este mismo bloque**, porque pegarlo la alarga. **No las publico como cifra de
> estado de la pagina**: estan aqui para fechar la remedicion, no para contarla.

### 9.2. `HEREDADO 2`: mis cuatro cocientes, rehechos con los dos numeros de su celda

| cociente que publico | sus dos numeros | rehecho |
|---|---|---|
| **`0` PUENTE de `35` pasos** | `0` y `35` | `0` dividido por `35` es `0,00` por ciento. **Sale** |
| **`6` candidatos de `6` piezas** | `6` y `6` | `6` dividido por `6` es `1`, uno a uno. **Sale** |
| **`35` de los `84` pasos de `cap_05`** | `35` y `84` | `84` menos `35` son `49`, que son los de la vuelta 51 que firme. **Sale** |
| **`405` de poblacion** | `346` y `59` | `346` mas `59` son `405`, y `59` son `56` mas `3`. **Sale** |

## 10. LO QUE NO HE PODIDO COMPROBAR, Y LO ESCRIBO EN VEZ DE AFIRMARLO

**Una busqueda negativa no se puede citar** (seccion `1.1`), y una comprobacion que no he
corrido tampoco:

| lo que falta | por que |
|---|---|
| **el barrido de vecinos par a par de los seis** | **YA NO FALTA: los seis terminaron y van pegados en `11`**, con sus seis relojes. Lo que sigue faltando es **la aduana entera** de los seis (las doce guardas, no solo las tres seniales), que cuesta mas que el barrido y **es del turno normal** |
| **el contenido de los diez ficheros de `.v52/`** | **existen los diez y ninguno esta en cero bytes**, comprobado en `11.2`. Su contenido es la medida del extractor y **no lo abro en esta fase a proposito** |
| **las cuatro guardas de dato (`gate`, cerrojo, censo, fidelidad con puente)** | son del turno normal. Aqui solo dejo escrito lo que vi de paso y hay que mirar: `procesos/` tiene **tres ficheros de cerrojo** de dias anteriores, y el codigo dice que un cerrojo huerfano **se declara, se rompe y se dice en voz alta**. No afirmo que sea averia: afirmo que hay que mirarlo |

    $ ls procesos/
    nodos.jsonl.218e43e4.cerrojo   (Sep 19 09:17)
    nodos.jsonl.679b2259.cerrojo   (Sep 18 19:49)
    nodos.jsonl.e52fd5d2.cerrojo   (Sep 18 21:18)

## 11. EL BARRIDO DE VECINOS, PEGADO TAL CUAL SALE

**LOS SEIS CORRIERON CONTRA LOS `405` DE LA POBLACION, UNO POR PROCESO Y EN PARALELO**, y cada
uno trae su reloj. **Antes de pegarlos declaro un fallo mio**, porque la primera corrida no vale y
el motivo es mio: **mi guion leia la clave `seniales` donde el codigo de la casa escribe
`senales`**, asi que imprimio las tres listas vacias y un `0 de 404` que **no era una medida, era
mi bug**. Lo arregle, volvi a correr los seis enteros, y **lo que va pegado abajo es la segunda
corrida**. La primera solo deja en pie su reloj, que no dependia de la clave.

### 11.1. LOS SEIS RELOJES

| candidato | reloj | pares |
|---|---:|---:|
| `acumular_asuntos_importantes_fichero_espera` | `1137,2` s | `404` |
| `alentar_asuntos_corazon_vigilar_final_reunion` | `1310,1` s | `404` |
| `conducir_reunion_individual_telefono_distancia` | `1294,6` s | `404` |
| `facilitar_expresion_subordinado_pregunta_mas` | `1238,9` s | `404` |
| `programar_reunion_individual_cadena` | `1423,1` s | `404` |
| `tomar_notas_copia_guion_reunion_individual` | `1245,4` s | `404` |
| **suma** | **`7649,3` s** | **`2424`** |

**`7649,3` entre `6` dan `1274,9` s por candidato**, y **`7649,3` entre `2424` pares dan `3,155` s
por par**. Los `2424` son `6` por `404`, y los `404` son los `405` de la poblacion menos el propio
candidato, **que no se mide contra si mismo** (`buscar_vecinos` lo excluye por su id, que es la
errata de metodo que la `ACTA 18` corrigio).

### 11.2. LO QUE LEVANTA CADA UNO, PEGADO

    $ cat vec_acumular_asuntos_importantes_fichero_espera.txt
      LOS CINCO MAS ALTOS DE similitud_texto (umbral 0.35, 0 NO APLICA):
        0.508  tomar_notas_copia_guion_reunion_individual
        0.498  alentar_asuntos_corazon_vigilar_final_reunion
        0.491  conducir_reunion_individual_telefono_distancia
        0.484  facilitar_expresion_subordinado_pregunta_mas
        0.432  programar_reunion_individual_cadena
      LOS CINCO MAS ALTOS DE familia_id (umbral 0.30, 0 NO APLICA):
        0.100  debatir_decidir_asuntos_cultura_evitar_delegar
        0.100  alentar_asuntos_corazon_vigilar_final_reunion
        0.000  vivir_valores_propios_evitar_listarlos
      LOS CINCO MAS ALTOS DE paso_contra_nodo (umbral 0.60, 0 NO APLICA):
        0.562  tomar_notas_copia_guion_reunion_individual
        0.536  rechazar_candidato_razones_relevantes
        0.521  cuidarse_agotamiento_centro_rueda
      LEVANTAN VECINO (levantada_por no vacio):
        alentar_asuntos_corazon_vigilar_final_reunion            similitud_texto 0.498
        conducir_reunion_individual_telefono_distancia           similitud_texto 0.491
        facilitar_expresion_subordinado_pregunta_mas             similitud_texto 0.484
        preparar_guion_reunion_individual_subordinado            similitud_texto 0.38
        programar_reunion_individual_cadena                      similitud_texto 0.432
        tomar_notas_copia_guion_reunion_individual               similitud_texto 0.508
      TOTAL QUE LEVANTAN: 6 de 404 pares

    $ cat vec_alentar_asuntos_corazon_vigilar_final_reunion.txt
      LOS CINCO MAS ALTOS DE paso_contra_nodo (umbral 0.60, 0 NO APLICA):
        0.612  fijar_duracion_lugar_reunion_individual
        0.574  despedir_persona_franqueza_radical
        0.571  resolver_dudas_frecuentes_pedir_critica
      LEVANTAN VECINO (levantada_por no vacio):
        acumular_asuntos_importantes_fichero_espera              similitud_texto 0.499
        conducir_reunion_individual_telefono_distancia           similitud_texto 0.466
        facilitar_expresion_subordinado_pregunta_mas             similitud_texto 0.432
        fijar_duracion_lugar_reunion_individual                  paso_contra_nodo 0.612
        preparar_guion_reunion_individual_subordinado            similitud_texto 0.38
        programar_reunion_individual_cadena                      similitud_texto 0.472
        tomar_notas_copia_guion_reunion_individual               similitud_texto 0.51
      TOTAL QUE LEVANTAN: 7 de 404 pares

    $ cat vec_conducir_reunion_individual_telefono_distancia.txt
      LOS CINCO MAS ALTOS DE familia_id (umbral 0.30, 0 NO APLICA):
        0.500  preguntar_conducir_reunion_individual
        0.286  programar_reunion_individual_cadena
        0.286  dirigir_reunion_individual_semanal
        0.250  preparar_guion_reunion_individual_subordinado
        0.250  fijar_duracion_lugar_reunion_individual
      LOS CINCO MAS ALTOS DE paso_contra_nodo (umbral 0.60, 0 NO APLICA):
        0.675  tomar_notas_copia_guion_reunion_individual
        0.526  definir_receta_propia_mantenerse_centrado
        0.521  clasificar_trabajo_proceso_montaje_prueba
      LEVANTAN VECINO (levantada_por no vacio):
        preguntar_conducir_reunion_individual                    familia_id 0.5
        acumular_asuntos_importantes_fichero_espera              similitud_texto 0.5
        alentar_asuntos_corazon_vigilar_final_reunion            similitud_texto 0.462
        facilitar_expresion_subordinado_pregunta_mas             similitud_texto 0.416
        programar_reunion_individual_cadena                      similitud_texto 0.476
        tomar_notas_copia_guion_reunion_individual               similitud_texto 0.474, paso_contra_nodo 0.675
      TOTAL QUE LEVANTAN: 6 de 404 pares

    $ cat vec_facilitar_expresion_subordinado_pregunta_mas.txt
      LOS CINCO MAS ALTOS DE paso_contra_nodo (umbral 0.60, 0 NO APLICA):
        0.562  fijar_resultado_excelente_reunion
        0.539  programar_visita_area_observar_despachar
        0.526  agrupar_tareas_semejantes_aprovechar_preparacion
        0.525  agrupar_interrupciones_subordinados_reuniones_regulares
      LEVANTAN VECINO (levantada_por no vacio):
        acumular_asuntos_importantes_fichero_espera              similitud_texto 0.475
        alentar_asuntos_corazon_vigilar_final_reunion            similitud_texto 0.414
        conducir_reunion_individual_telefono_distancia           similitud_texto 0.411
        cubrir_indicadores_problemas_reunion_individual          similitud_texto 0.362
        fijar_duracion_lugar_reunion_individual                  similitud_texto 0.361
        preparar_guion_reunion_individual_subordinado            similitud_texto 0.397
        programar_reunion_individual_cadena                      similitud_texto 0.445
        tomar_notas_copia_guion_reunion_individual               similitud_texto 0.434
      TOTAL QUE LEVANTAN: 8 de 404 pares

    $ cat vec_programar_reunion_individual_cadena.txt
      LOS CINCO MAS ALTOS DE familia_id (umbral 0.30, 0 NO APLICA):
        0.333  preguntar_conducir_reunion_individual
        0.333  dirigir_reunion_individual_semanal
        0.286  preparar_guion_reunion_individual_subordinado
      LEVANTAN VECINO (levantada_por no vacio):
        dirigir_reunion_individual_semanal                       familia_id 0.333
        preguntar_conducir_reunion_individual                    familia_id 0.333
        acumular_asuntos_importantes_fichero_espera              similitud_texto 0.431
        alentar_asuntos_corazon_vigilar_final_reunion            similitud_texto 0.474
        conducir_reunion_individual_telefono_distancia           similitud_texto 0.474
        facilitar_expresion_subordinado_pregunta_mas             similitud_texto 0.449
        tomar_notas_copia_guion_reunion_individual               similitud_texto 0.472
      TOTAL QUE LEVANTAN: 7 de 404 pares

    $ cat vec_tomar_notas_copia_guion_reunion_individual.txt
      LOS CINCO MAS ALTOS DE familia_id (umbral 0.30, 0 NO APLICA):
        0.375  preparar_guion_reunion_individual_subordinado
        0.250  programar_reunion_individual_cadena
        0.250  preguntar_conducir_reunion_individual
        0.250  dirigir_reunion_individual_semanal
      LOS CINCO MAS ALTOS DE paso_contra_nodo (umbral 0.60, 0 NO APLICA):
        0.675  conducir_reunion_individual_telefono_distancia
        0.553  alentar_asuntos_corazon_vigilar_final_reunion
        0.549  acumular_asuntos_importantes_fichero_espera
      LEVANTAN VECINO (levantada_por no vacio):
        acumular_asuntos_importantes_fichero_espera              similitud_texto 0.503
        alentar_asuntos_corazon_vigilar_final_reunion            similitud_texto 0.515
        conducir_reunion_individual_telefono_distancia           similitud_texto 0.472, paso_contra_nodo 0.675
        facilitar_expresion_subordinado_pregunta_mas             similitud_texto 0.432
        fijar_frecuencia_reunion_individual_madurez_tarea        similitud_texto 0.355
        preparar_guion_reunion_individual_subordinado            similitud_texto 0.4, familia_id 0.375
        programar_reunion_individual_cadena                      similitud_texto 0.468
      TOTAL QUE LEVANTAN: 7 de 404 pares

**LOS SEIS SUMAN `41` PARES QUE LEVANTAN VECINO**: `6` mas `7` mas `6` mas `8` mas `7` mas `7`, y
esa suma la hago yo con los seis numeros delante. **Ninguno de los seis entraria sin veredicto**,
y eso no es un rechazo: **es la cola de lectura del dia de la insercion.**

### 11.3. DONDE MI LECTURA Y LA MAQUINA NO COINCIDEN, Y QUIEN SE EQUIVOCO EN CADA CASO

**Dije en `6.8` que si el barrido levantaba un vecino que mi tabla no nombraba, el que se habia
equivocado era yo. Levanto uno, y lo era.**

| | |
|---|---|
| **LO QUE MI LECTURA ACERTO, Y ES LO MAS ALTO DE LA TANDA** | el par mas fuerte de las `2424` mediciones es `tomar_notas_copia_guion_reunion_individual` contra `conducir_reunion_individual_telefono_distancia`, **`paso_contra_nodo` `0,675` contra un umbral de `0,60`**, que es **el unico de la tanda que cruza ese umbral entre dos candidatos nuevos**. Es exactamente el par que marque en `6.8` fila `5` como *el unico par de la tanda donde dos fichas comparten dos pasos*, **escrito antes de correr el barrido** |
| **LO QUE SE ME ESCAPO** | **`preguntar_conducir_reunion_individual`** (grafo, `zhuo_manager`) **no esta en mi tabla y deberia estar.** Es *preguntar para conducir la reunion individual, con los tres grupos de preguntas del libro*, y su paso `4` dice que el trabajo del directivo **no es repartir consejo sino habilitar a la persona a que encuentre ella la respuesta**. **Ese es el vecino doctrinal de `P15`**, mas que el `dirigir_reunion_individual_semanal` que yo nombre |
| **Y AQUI ESTA LA IRONIA, QUE VALE MAS QUE MI FALLO** | la maquina **tampoco** lo levanto contra `P15`. Lo levanto contra `conducir_reunion_individual_telefono_distancia` con `familia_id` `0,500`, que es **coincidencia de nombre** (`conducir`, `reunion`, `individual`), y contra `P15` **no lo levanto por ninguna de las tres seniales**. **La senial mas alta de la tanda apunta al candidato equivocado del par correcto** |
| **la segunda que se me escapo** | `alentar_asuntos_corazon_vigilar_final_reunion` contra `fijar_duracion_lugar_reunion_individual` cruza `paso_contra_nodo` en `0,612`. Yo nombre a `cubrir_indicadores_problemas_reunion_individual` como su vecino mas fuerte. **El mio es por contenido y el de la maquina por paso**, y los dos hay que leerlos |

> **Y ESTO ES `D.19` OTRA VEZ, MEDIDO EN MI PROPIA TANDA:** *ninguna senial separa jerarquia de
> ruido, asi que una discrepancia NUNCA se adjudica citando una senial.* **La senial dijo donde
> mirar y ahi acabo su trabajo.** Mi clase de `P15` no cambia por que `familia_id` mire a otro
> lado: **cambia mi tabla, que nombraba un vecino peor que el que habia.** Lo dejo escrito con su
> medida y **la adjudicacion del par `P15` contra `preguntar_conducir_reunion_individual` es del
> dia de la insercion**, no de hoy.

**MI CLASE PARA ESE PAR, ESCRITA IGUAL QUE LAS OTRAS SEIS:** `P15` y
`preguntar_conducir_reunion_individual` **no son gemelos**. Los dos mandan preguntar en vez de
aconsejar, y eso es **concordancia de doctrina y no duplicado**; lo que queda fuera es
procedimiento en los dos lados: de Grove, **preguntar una vez mas** como principio unico y la cita
de Drucker; de Zhuo, **tres grupos de preguntas nombrados** con sus ejemplos. **Arista de
contraste, declarada por lectura, para cablear el dia de la insercion.**

## 12. LO QUE ESTA PAGINA FIRMA, PARA QUE SE PUEDA COMPARAR CON EL REPORTE

    ACTA ANTERIOR LEIDA: 6835eb9a76f047e7384711f90879baf5918b45a8
    HEREDADO 1: CUMPLIDO
    HEREDADO 2: CUMPLIDO
    HEREDADO 3: CUMPLIDO

| # | lo que firmo, antes de ver el reporte |
|---:|---|
| `1` | **`6` candidatos de `6` piezas**, `P15` a `P20`, uno a uno y sin pieza repartida |
| `2` | **las seis cifras de palabras de la frontera salen al digito**: `134`, `157`, `64`, `117`, `85`, `74` |
| `3` | **`0` PUENTE de `35` pasos**, leidos uno a uno contra `L45`, `L47`, `L49`, `L51`, `L53`, `L55` y `L57` |
| `4` | **los seis son nodos legitimos**: ninguno es gemelo de nada, y tres llevan arista declarada por lectura |
| `5` | **`41` pares levantan vecino** en los seis barridos, y ninguno de los seis entraria sin veredicto escrito |
| `6` | **las seis fichas hermanas anaden y no borran**, con el texto viejo como prefijo literal del nuevo |
| `7` | **cuatro discutibles mios marcados**, y **dos fallos mios declarados**: el vecino que no nombre y la clave que mi guion leia mal |

**LO QUE NO FIRMO:** ningun veredicto de insercion (no entra nada hoy), ninguna cifra del reporte
(no lo he visto), y ninguna adjudicacion de la discrepancia de `2.1`, que es del fundador.
