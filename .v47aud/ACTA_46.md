
---

# ACTA 46. VUELTA 47, lote 7 (`grove_high_output`), `cap_04`: **LA VUELTA VUELVE A CERRAR ENTERA Y SU CIERRE CORTO ES CORRECTO**, con el techo en minutos mordiendo en el sexto candidato y declarado con su reloj, que es justo lo que `EXTRACTOR.md` 12.4 me manda verificar. **Recompongo hoy el `22` de la frontera de `cap_04` que mi apertura dejo a deber** (`44` filas, `8846` contra `8846`, `0` lineas sin cubrir, `0` solapes) y me sale entero; **sus seis relojes y sus seis informes los reproduzco uno a uno** (`4090` s, `9` vecinos, `2` `ENTRARIA`, `4` `BLOQUEARIA`, `0` `CAERIA`) y **sus nueve pares de cola me salen los nueve al milesimo**; **la guarda que declara mordiendo la muerdo por mutacion y muerde**; su instrumento de tanda **reproduce su salida byte a byte**; y **FIRMO su `0` PUENTE de `95` pasos de `cap_04`**, con el denominador contado por mi de las catorce fichas. **Sus dos caidas son de PROSA y NO acumulan**: un superlativo que su propia tabla de frontera desmiente (`P27` con `347` palabras publicado como *el tramo mas rico de la tanda* cuando `P24` tiene `356`) y un *el mas proximo* adjudicado por una senial cuando el instrumento de la casa da lo contrario en dos de las tres. **`REPORTE` sigue en `0 de 3`** por `D.38.1`, y `CLASE`, `CIFRA PUBLICADA` y `DATO MOVIDO` salen **LIMPIAS** con su motivo medido: **esta vuelta no movio ni una linea de `dataset/`, `bitacora/` ni `config/`**, comprobado por diferencia. **Y MI PROPIA TANDA SALE LIMPIA**: ni una cifra falsa en mi pagina sellada y mi remedio de la `ACTA 45` **CUMPLIDO**, asi que `AUDITOR` baja de `2 de 3` a `0` por la tanda limpia de `5.4`, **no por indulto mio**. **REGISTRO Y NO ADJUDICO UNA MEDIDA DE FORMA** (`D.56` congela la doctrina): `13` de los `45` pasos de esta tanda y `12` de los `50` de la anterior **abren declarando y no ejecutando**, y de los `13` el extractor marco `5`. Ninguna condicion de parada se cumple: **no escribo `PARA_ALEXIS.md`**, y el encargo de la vuelta `48` sale de esta sede.

## 46.0. HUECO DE ACTA: **NO LO HAY**, y va antes que nada

La ultima acta escrita es la `ACTA 45` y cubre la vuelta `46`, que es la inmediatamente
anterior a la `47`. **Cubro una sola vuelta y no hay guardas que re correr por hueco.**

    $ python forja.py herencia | head -3
      acta anterior : ACTA 45. VUELTA 46, lote 7 (`grove_high_output`), `cap_04`: ...

## 46.1. LA HERENCIA DE `D.40`, DECLARADA Y COMPROBADA

    ACTA ANTERIOR LEIDA: d0255b4e685a777102c0c116f69dab7d23af2db2
    HEREDADO 1: CUMPLIDO

**Y LA DECLARACION SE COMPRUEBA EN VEZ DE COPIARSE DEL PROMPT**, hoy y en mi fase ciega:

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    d0255b4e685a777102c0c116f69dab7d23af2db2

El remedio heredado es el mio de `45.9.b`: **todo barrido de mi fase ciega escribe su guion
y su salida en el arbol, y ningun superlativo mio se publica sin la lista ordenada que lo
sostiene.** Lo cumpli: los guiones y sus salidas estan en `.v47aud/`, y el unico superlativo
de mi pagina sellada (*el par mas alto es `0,3333`*) lleva **la lista ordenada entera de los
doce pares** pegada encima.

**EL ARNES ME ENTREGO `heredados: 0` Y TENIA RAZON LA MAQUINA**, no yo: escribi el remedio
como parrafo dentro de un bloque de cita y `src/herencia.py` entrega filas de tabla fuera de
cita. **Lo salvo la otra red**, la de leer mi propia acta en la fase ciega. Va a `46.10` con
mi nombre y con su arreglo puesto en esta misma acta.

## 46.2. LO QUE RECOMPUTE CON MIS PROPIOS COMANDOS, Y NO COPIE DE SU REPORTE

**Las guardas que `AUDITOR_FORJA.md` 1.1 nombra, corridas por mi hoy:**

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python tests/test_aceptacion.py
      total: 318 pruebas, 0 fallos, 0 errores
    $ python scripts/tallar_reporte.py
    TALLADO VERDE: las 119 tabla(s) comprobables son las de su instrumento, celda a celda.
    $ python scripts/censar_rutas.py
    CENSO VERDE: las 767 rutas publicadas sostienen lo que dicen sostener.
    $ python scripts/tabla_de_cierre.py
    TABLA DE CIERRE VERDE: ninguna celda medible difiere del dato.

**Y LAS `318` CON `0` Y `0` SON LA OTRA MITAD DE MI PROPIA APERTURA**, que las midio con `3`
fallos y `1` error por la retirada de `D.34.2`. **La causa que diagnostique a ciegas queda
confirmada al reponerse los ficheros**: los cuatro rojos eran artefactos del arnes y ninguno
era un defecto del arbol.

**El estado, contado por mi y cruzado por diferencia contra el commit de apertura `327d969`:**

| cifra | el reporte dice | yo mido | como |
|---|---:|---:|---|
| `dataset/nodos.jsonl` al abrir y al cerrar | `346` y `346` | `346` y `346` | `wc -l`, y `git diff --stat 327d969 HEAD` vacio |
| `bitacora/VEREDICTOS.jsonl` al abrir y al cerrar | `740` y `740` | `740` y `740` | idem |
| `config/pares_mutuos.jsonl` | `1` y `1` | `1` y `1` | idem |
| bandeja `grove_high_output` al cerrar | `36` | `36` | `ls cuarentena/grove_high_output/*.json` |
| bandeja `marquet_turn_the_ship` | `3` | `3` | idem |
| `_insertados/grove_high_output` | `1` | `1` | idem |
| poblacion del barrido al cerrar | `385` | `385` | `346` de grafo mas `39` de bandejas, con la de `ensayo_referencia_163` fuera de la tabla canonica |
| deuda al abrir y al cerrar | `12` pendientes, `8` pagadas | `12` y `8` | `python scripts/deuda.py` |

**LA MORATORIA SE CUMPLIO Y LO MIDO POR DIFERENCIA, no por lectura:**

    $ git diff --stat 327d969 HEAD -- tests/ src/ scripts/ forja.py hooks/ docs/BANCO_DE_REGLAS.md docs/loop/EXTRACTOR.md docs/loop/AUDITOR_FORJA.md
    (vacio)

    $ git diff --name-status 327d969 HEAD -- cuarentena/
    6 A   (los seis candidatos de cap_04)
    1 M   (transmitir_objetivos_prioridades_preferencias, la arista de P27)

**Y LA CORRECCION DE LA MADRE NO BORRA NADA, que es lo que manual principio 6 manda y lo
unico que un `M` no dice por si solo:**

    $ python .v47aud/40_madre_sin_borrar.py
    campo que cambia: resumen_teorico
    el texto viejo esta entero dentro del nuevo: True
    largo viejo: 3362  largo nuevo: 4170  anadido: 808

### 46.2.a. **EL `22` DE LA FRONTERA DE `cap_04`, RECOMPUESTO HOY**, que es lo que mi apertura sellada se dejo a deber en su seccion `12`

Mi pagina ciega dijo con todas las letras que el `22` lo citaba de mi `ACTA 45` y que **no lo
habia recompuesto hoy**. Lo recompongo ahora, antes de usarlo para nada que decida volumen:

    $ python .v47aud/30_frontera.py
    filas de la tabla                      : 44
    suma de la columna de palabras         : 8846
    suma de la columna de nodos            : 22
    filas que dan cero nodos               : 23
    filas cuya cuenta de palabras DIFIERE  : 0 []
    lineas con contenido tras la cabecera  : 158
    lineas con contenido NO cubiertas      : 0 []
    SOLAPES                                : 0 []
    cuerpo medido aparte (L9 al final)     : 8846
    cabecera (L1 a L7)                     : 25
    fichero entero                         : 8871

**LAS `44` FILAS SE CRUZAN CONTRA EL FICHERO UNA A UNA Y NINGUNA DIFIERE**, y el `8846` mas
el `25` da el `8871`. **El `22` es de hoy y ya no es una cifra citada.**

**Y CUANTOS DE ESOS `22` ESTAN MINADOS**, contado de las propias fichas por su campo
`UNIDAD DE ORIGEN`:

    $ python .v47aud/16_cap04.py
    cap_02           7
    cap_03          15
    cap_04          14
    total bandeja grove_high_output: 36

`LECTURA`: **`14` de `22`, y quedan `8`**, que son los mismos `8` que el reporte nombra por su
tramo en `II.2.h`. **La trampa de `d028` sigue viva y hoy se cobraria `8` nodos**, no `14`.

### 46.2.b. **LOS SEIS RELOJES Y LOS SEIS INFORMES, ABIERTOS UNO A UNO**

Los doce ficheros existen y **ninguno tiene cero bytes** (cosecha 7.B). Recalculo cada
intervalo de sus dos marcas:

| candidato | el reporte dice | el intervalo que dan sus marcas |
|---|---:|---|
| `detectar_palanca_negativa_actividad_mando` | 857 | `real 14m16.566s` es `856,6`, redondeado a `857` |
| `delegar_tarea_base_comun_seguimiento` | 861 | `04:16:02` a `04:30:23` da 861 |
| `supervisar_tarea_delegada_etapa_menor_valor` | 732 | `04:31:12` a `04:43:24` da 732 |
| `supervisar_decision_delegada_preguntas_concretas` | 471 | `04:43:47` a `04:51:38` da 471 |
| `identificar_paso_limitante_jornada_desfases` | 555 | `04:51:47` a `05:01:02` da 555 |
| `agrupar_tareas_semejantes_aprovechar_preparacion` | 614 | `05:01:13` a `05:11:27` da 614 |
| **total de la tanda** | **4090** | **4090** |
| la ficha corregida de `P27`, aparte | 578 | `05:12:33` a `05:22:11` da 578 |

**Y LAS CUENTAS QUE CUELGAN DE ESE TOTAL ME SALEN TODAS:** `4090 / 6 = 681,7`;
`4090 / 45 = 90,9` s por paso; `4044 / 50 = 80,9` de la vuelta `46`; `90,9` contra `80,9` da el
`12,4` por ciento de subida por paso y `681,7` contra `505,5` el `34,8` por candidato;
`4090 + 578 + 232 = 4900` s, con los `232` de las dos pruebas de aceptacion leidos de sus dos
lineas `real`; y `4668 / 4900 = 95,3` por ciento. **Las trece cifras de `II.2.h` y `II.4.f` son
suyas al digito, y el `NO` de su techo tambien: `4090` contra `4020`.**

**LOS SEIS INFORMES DICEN LO QUE SU TABLA DICE:** `2` `ENTRARIA` (los dos con `0` vecinos),
`4` `BLOQUEARIA`, `0` `CAERIA`, y la suma de vecinos `0+0+2+2+3+2` da `9`. La poblacion sube de
`380` a `385` informe a informe, **un candidato por informe**.

**Y SUS NUEVE PARES DE COLA ME SALEN LOS NUEVE AL MILESIMO**, con sus tres seniales cada uno,
leidos de los propios informes y no de su tabla: la banda va de `0,226` a `0,409`, hay **un
solo par por encima de `0,40`**, y el reparto de seniales es `familia_id 1` y
`similitud_texto 8`.

## 46.3. LA GUARDA QUE DECLARA MORDIENDO, VUELTA A MORDER POR MUTACION

*Cosecha 7.C: una guarda publicada como mordiendo que no muerde es cifra falsa.*

`II.3` declara que su instrumento de tanda **se para sin publicar la tabla** si una ficha
declara mas pasos de los que tiene. **Le cambio el valor esperado y compruebo que CAE:**

    $ python .v47aud/36_tanda_mutada.py
    LA TABLA NO SE PUBLICA: detectar_palanca_negativa_actividad_mando declara 9 pasos y tiene 9

**Y COMPRUEBO ADEMAS QUE NO ESTA SIEMPRE ROJA**, que es la otra mitad de la prueba: corro el
instrumento sin mutar y comparo su salida con la que el reporte pego.

    $ python .v47/tanda.py > .v47aud/37_tanda_original.out
    $ diff .v47/tanda_cap_04.txt .v47aud/37_tanda_original.out
    IDENTICA a la salida que el reporte pego

**LA GUARDA MUERDE Y EL INSTRUMENTO REPRODUCE SU SALIDA BYTE A BYTE.**

**LA COLISION DE `D.52` LA SELLO YO TAMBIEN**, porque la prueba que el reporte ofrece es un
`hash-object` y eso se comprueba en dos comandos:

    $ git show d209b33:docs/loop/TABLA_DE_CIERRE.txt | git hash-object --stdin
    ed84ec8edfb1e4dadf1edc3110d8ca1ab988f64a
    $ git hash-object docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_v46.txt
    ed84ec8edfb1e4dadf1edc3110d8ca1ab988f64a

**La copia archivada ES la salida de la vuelta `46`, no una transcripcion suya.** Y la averia
que la obliga va anotada hoy como `d030`, porque es el tercer ejemplar seguido.

## 46.4. LA RELECTURA CIEGA: **LOS SEIS DISCUTIBLES MARCADOS, Y LOS SEIS SE SOSTIENEN**

**Empiezo por los discutibles marcados, que es lo que `5.1` manda**, y los seis estaban
escritos dentro de su ficha **antes de que ninguna senial hablara**. Imprimi primero los
pasos de cada nodo (`.v47aud/41_pasos.py`) y los renglones del libro
(`.v47aud/42_renglones.out`), y solo despues destape la razon que la ficha escribe.

**NO HAY VEREDICTO QUE DESTAPAR EN `bitacora/VEREDICTOS.jsonl` Y LO DIGO EN VEZ DE
CALLARLO:** esta vuelta escribio **cero veredictos** (`740` contra `740`), porque no inserto.
Lo que releo son **los discutibles de las fichas y las nueve lecturas de cola** que el
reporte publica por adelantado.

| # | el discutible que la ficha se marca | mi adjudicacion | lo que la sostiene, leido del renglon |
|---:|---|---|---|
| 1 | `detectar_palanca_negativa...`, pasos `6` y `9`: consecuencias y no actos | **SE SOSTIENE** | son consecuencias, si, y son **las dos que el libro usa como criterio de deteccion**: `L233` contrapone la palanca ilimitada del desanimo y las largas contra un mal curso de ventas que se arregla reformando, y `L235` da la vision restringida del subordinado. **Sin el `9`, la prueba del paso `8` no tiene salida que detectar.** Si caen, el nodo queda en `7` |
| 2 | `delegar_tarea_base_comun...`, paso `1`: una razon y no un acto | **SE SOSTIENE** | es la premisa con que `L245` abre (*Because managerial time has a hierarchy of values*) y **es el unico sitio del nodo donde esa jerarquia se nombra**. Es el mas debil de los diez y lo digo: si cae, el nodo conserva `9` actos y no se mueve |
| 3 | `supervisar_tarea_delegada...`, paso `9`: una comparacion y no un acto | **SE SOSTIENE** | `L255` la escribe en el mismo renglon que el paso `8` (*would be like quality assurance testing 100 percent*) y **es el techo del al azar del paso `8`**: sin ella, *entra en los detalles solo al azar, lo justo* no tiene cota superior ninguna |
| 4 | `supervisar_decision_delegada...`, pasos `3`, `4` y `5`: salen del caso de Intel, y si caen cae el nodo entero | **SE SOSTIENE, Y ES EL QUE MEJOR MARCO** | manual 3.5 dice que el caso no es la casa. **Los tres pasos no llevan ni un dato del caso**: ni Intel, ni la compra de equipo de capital, ni el *we*. Y **el propio libro los generaliza en su ultima frase**: *This technique allows us to find out how good the thinking is*, o sea que el autor los llama tecnica y no anecdota |
| 5 | `identificar_paso_limitante...`, paso `5`: el resumen que el propio libro hace | **SE SOSTIENE COMO TRANSCRIPCION, con un reparo medido** | `L267` cierra con *In short, if we determine what is immovable and manipulate the more yielding activities around it*. Es del libro, asi que **no es `PUENTE`**. El reparo va a `46.7` y no es caida: **es el unico de los `45` que solo re dice otros pasos del mismo nodo**, y aun asi suma `1` al denominador de la metrica de volumen |
| 6 | `agrupar_tareas_semejantes...`, pasos `4` y `5`: los dos ejemplos del libro | **SE SOSTIENE** | el `5` **no es un ejemplo**: `L271` lo escribe en forma normativa (*he should set aside a block of time and do a batch of them together*). El `4` si sale del ejemplar de las ilustraciones, y entra **con el caso nombrado dentro del acto**, que es exactamente lo que manual 3.5 manda, y no como paso propio del caso |

**LOS SEIS SE SOSTIENEN. DENTRO DEL MARCADO: `6` de `6`. FUERA DEL MARCADO: `0` caidas de
clase.** Y digo lo que esa cifra significa y lo que no: **significa que el extractor sabia
donde estaba su duda**, no que los `45` pasos esten bien, que es otra prueba y la firme
releyendolos uno a uno en mi fase ciega.

**Y EL `4` MERECE SU MEDIDA, porque yo mismo lo llame el mas caro en mi pagina sellada y un
superlativo sin medida es justo lo que le estoy cobrando al extractor en `46.6`:** de los seis,
el `4` es el unico cuyo marcado se lleva **la mitad del nodo** (`3` de `6` pasos), y los tres
que quedarian (`1`, `2` y `6`) abren los tres declarando, o sea que **no quedaria ni un acto
ejecutable**. El siguiente en proporcion es el `6`, con `2` de `6`, y el nodo conserva actos.

**LAS NUEVE LECTURAS DE COLA, RELEIDAS TAMBIEN**, empezando por la unica por encima de `0,40`
como la propia regla manda: `agrupar_tareas_semejantes` contra `identificar_paso_limitante`,
`0,409`. **Sostengo su `SANO`**: `L267` abre con *First, we must identify our limiting step* y
`L269` con *A second production principle we can apply*, o sea que **el libro los numera como
primero y segundo de la misma serie**, y mi propio barrido de pasos de la fase ciega midio
**cero pasos identicos entre los catorce candidatos de `cap_04`**. Las otras ocho las sostengo
igual y no reabro el argumento (modo austero).

## 46.5. LAS ADJUDICACIONES

### 46.5.a. **ADJUDICO QUE EL CIERRE CORTO ES CORRECTO Y ESTA DECLARADO**, que es lo que `EXTRACTOR.md` 12.4 me manda verificar

La regla dice que una vuelta que cierra en un capitulo **y no lo dice** es caida de especie
`REPORTE`. **Esta lo dice, y con las tres piezas:** el numero (`6` de `8`), el reloj (`4090` s
contra un techo de `4020`) y **los que quedan nombrados por su tramo** (`P34` con dos nodos,
`P36`, `P38`, `P39`, `P41`, `P42` y `P44`, que son `8` y cuadran con mi `22` menos `14`).
**No hay caida y lo digo con la medida delante.**

### 46.5.b. **ADJUDICO QUE LA ARISTA HACIA UN ID QUE NO EXISTE NO ES CAIDA HOY, Y DIGO QUE LA HACE FRAGIL**

Mi fase ciega encontro que `identificar_paso_limitante_jornada_desfases` declara una arista
hacia `usar_calendario_herramienta_planificacion_produccion`, **y hoy ese id no vive en
ninguna sede**, comprobado sobre las `894` fichas y no por una busqueda negativa citada:

    $ python .v47aud/(barrido de grafo y de todas las bandejas, sin filtro)
    sedes donde vive 'usar_calendario_herramienta_planificacion_produccion': NINGUNA
    nodos del grafo barridos: 346     fichas de cuarentena barridas: 548

**NO ES CAIDA**, y lo adjudico citando la regla por extension natural: esta casa ya declara
aristas hacia nodos futuros, y `buscar_actividad_alta_palanca_tres_vias` se declaro madre *del
que sale de `L231` a `L235`* cuando ese nodo no existia. **La diferencia que si marco** es que
aquella se declaro **por su tramo** y esta **por un id inventado de antemano**: un id que nadie
ha escrito puede no coincidir con el que se escriba, y entonces la arista queda colgada **sin
que ninguna guarda lo cante**, porque el gate solo mira el grafo. **Adjudico que la vuelta 48
escriba ese nodo o corrija la arista a su tramo**, y va como fila del encargo: el tramo que le
toca es `P34`, que es justo el primero de los que la vuelta 48 mina, **asi que se paga sin
coste propio**.

### 46.5.c. **ADJUDICO QUE LA MITAD EN MINUTOS DE `d011` SE ESTIME SOBRE PASOS, Y NO ES DOCTRINA NUEVA**

El extractor lo propone en `II.4.g` y **la propuesta es suya, la sede del techo es mia**
(`5.6`). `d011` obliga a que **todo techo que yo escriba lleve su mitad en minutos**; **no dice
de que se estiman esos minutos.** Estimarlos de `90,9` s por paso en vez de `681,7` s por
candidato **no mueve la regla: mejora la estimacion de la misma cantidad**, y la medida que lo
sostiene es suya: entre las dos tandas del mismo capitulo, el coste por candidato sube un
`34,8` por ciento y el coste por paso solo un `12,4`. **Lo aplico en el encargo de la vuelta 48
y no lo llevo al banco**, que `D.56` esta congelada.

### 46.5.d. **ADJUDICO QUE EL VOLUMEN NO SUBE, AUNQUE LA METRICA DE `8.1` LO PERMITIRIA**

`PASOS INVENTADOS` se mantiene en `0,00` por ciento dos tandas seguidas, y `8.1` diria *un
capitulo mas por vuelta*. **No sube, y la regla que manda es la otra:** `EXTRACTOR.md` 12.4
dice que **cuando los dos techos chocan manda el de candidatos**, y `cap_04` sigue con `8` de
sus `22` sin minar. **Una vuelta no avanza de capitulo con el suyo abierto.** El volumen se
queda donde esta y la vuelta 48 termina `cap_04`.

### 46.5.e. **LO QUE ANOTO EN LA DEUDA, PORQUE `D.55` DICE QUE LO QUE NO BLOQUEA SE AGENDA**

| id | que es | de donde sale |
|---|---|---|
| **`d030`** | `scripts/tabla_de_cierre.py --escribir` escribe **siempre en la misma ruta viva**, asi que toda vuelta que cierra deja en rojo la tabla de la anterior. **Tercer ejemplar seguido** (`42` lo sufrio, `46` lo reparo y lo volvio a causar, `47` igual). Es distinto de `d009` y de `d022` | `REPORTE.md` `II.4.c`, sellado en `46.3` |
| **`d031`** | **retocar una linea de un `resumen_teorico` en cuarentena cuesta la aduana entera**: `578` s medidos, lo mismo que un candidato nuevo, y por eso la vuelta dejo sin cablear una arista que la senial levanto (`732` s) | `REPORTE.md` `II.2.f` y `II.4.g`, con `.v47/reloj_madre_p27.txt` |

**LA TERCERA PROPUESTA DEL EXTRACTOR NO VA A LA DEUDA PORQUE LA ADJUDICO HOY**, y es la de
`46.5.c`.

## 46.6. LAS CAIDAS DEL EXTRACTOR, CON SU SEDE Y SU CUENTA

**DOS, LAS DOS DE ESPECIE `REPORTE` Y LAS DOS EN PROSA DE ACOMPANIAMIENTO**, asi que
**registran con su nombre y NO acumulan** (`5.2`).

### 46.6.a. **UN SUPERLATIVO QUE SU PROPIA TABLA DE FRONTERA DESMIENTE** (`II.3.b`, linea `44950`)

> *el tramo mas rico de la tanda (`P27`, `347` palabras con cinco objetos nombrados) dio `10`
> pasos y `0` puentes*

**LA CIFRA ES CIERTA Y EL SUPERLATIVO ES FALSO.** `P27` tiene `347` palabras, si. **Pero el
tramo mas rico de la tanda es `P24`, con `356`**, y el tramo entero del candidato `1` es `P21`
mas `P24`, o sea `429`. Publico la lista ordenada entera, que es lo que un superlativo
necesita:

    $ python .v47aud/44_tramos.py
    LOS TRAMOS DE LA TANDA DE LA VUELTA 47, ORDENADOS, LISTA ENTERA:
       P24     356 palabras   1 nodo(s)
       P27     347 palabras   1 nodo(s)
       P29     227 palabras   1 nodo(s)
       P33     212 palabras   1 nodo(s)
       P32     122 palabras   1 nodo(s)
       P30     106 palabras   1 nodo(s)
       P21      73 palabras   0 nodo(s)

**Y LA FRASE QUE ESE SUPERLATIVO VENIA A SOSTENER NO SE SOSTIENE CON ESA VARA TAMPOCO.** Dos
renglones antes el parrafo dice *los `23` tramos que la frontera dejo en cero son justamente
los pobres*, y a continuacion ofrece las palabras como medida de riqueza:

    tramos con CERO nodos : 23   palabras: media 199.7  minimo 8  maximo 674 (P5)
    tramos CON nodo       : 21   palabras: media 202.6  minimo 60  maximo 469 (P34)

`LECTURA`: **las dos poblaciones son indistinguibles en palabras**, y **los dos tramos mas
ricos del capitulo entero, `P5` con `674` y `P2` con `530`, dan cero nodos.** La tesis de
fondo, que los tramos en cero son pobres **de inventario**, **si la sostiene su tabla de
frontera**, donde cada uno de los `23` lleva su regla escrita (`CASO`, `POSTURA`,
`DEFINICION`, rotulo). Lo que no la sostiene es la medida que el parrafo eligio: **conto
palabras y publico una frase sobre inventario.** Es la especie que `D.38.3` nombra y la que a
mi me costo la caida de la vuelta `26`.

### 46.6.b. **UN EL MAS PROXIMO ADJUDICADO POR UNA SENIAL, CONTRA `D.19`** (`II.2.f`)

> *Los dos son de `cap_02` y los dos valen; el que no escribi es el mas proximo.*

**LO MIDO CON EL INSTRUMENTO DE LA CASA, `src/aduana.medir`, Y DA LO CONTRARIO EN DOS DE LAS
TRES SENIALES:**

    $ python .v47aud/45_proximidad.py
    candidato: supervisar_tarea_delegada_etapa_menor_valor
    LISTA ORDENADA ENTERA, por similitud_texto:
       elegir_inspeccion_barrera_monitorizacion     similitud_texto 0.2660 | familia_id 0.0000 | paso_contra_nodo 0.4910
       detectar_arreglar_fallo_etapa_menor_valor    similitud_texto 0.2260 | familia_id 0.3330 | paso_contra_nodo 0.4350

`LECTURA`: **el pariente que la ficha SI escribio gana en similitud de texto y en paso contra
nodo.** El otro gana solo en `familia_id`, **que compara la cadena del id**, y el propio
reporte lo dice sin sacar la consecuencia: *la familia la comparten porque comparten el objeto
`etapa_menor_valor`*. `AUDITOR_FORJA.md` 6.2, con `D.19` detras, dice que **una discrepancia
nunca se adjudica citando una senial**: la senial dice donde mirar y ahi acaba su trabajo.

**LO QUE NO ES, Y CONVIENE DECIRLO:** no es caida de `CLASE` ni de `DATO MOVIDO`. **La arista
no se cableo**, ninguna ficha cambio por esto, y el hallazgo de fondo sigue siendo bueno: la
senial `2` levanto un pariente legitimo que la lectura no habia visto. **Lo falso es el
ranking, no el hallazgo.**

## 46.7. LA FORMA DE LOS PASOS: **UNA MEDIDA QUE REGISTRO Y NO ADJUDICO** (`D.56`)

El discutible `5` me llevo a mirar una cosa que se mide y no se opina: **con que abre cada
paso.** Un paso que abre *Cuenta con que...* manda sostener una creencia, no ejecutar.

    $ python .v47aud/43_forma_pasos.py
    == tanda de la vuelta 47 : 45 pasos
       Cuenta        12   (26.7 por ciento)
       Revisa         5   (11.1 por ciento)
       Aplica         3   (6.7 por ciento)
       ...
       pasos que ABREN declarando y no ejecutando: 13 de 45 = 28.9 por ciento
    == tanda de la vuelta 46 : 50 pasos
       Cuenta        11   (22.0 por ciento)
       ...
       pasos que ABREN declarando y no ejecutando: 12 de 50 = 24.0 por ciento

`LECTURA`: **`13` de `45` y `12` de `50`, el mismo capitulo y la misma mano.** Y la cifra que
de verdad interesa, que es la de `5.1`: **de esos `13`, el extractor marco `5` como discutibles
y no marco `8`.** La lista entera de los trece esta en `.v47aud/43_forma_pasos.out`.

**POR QUE IMPORTA, Y ES UNA SOLA FRASE:** `pasos escritos` es el **denominador** de
`PASOS INVENTADOS`, y un paso declarativo **nunca puede ser `PUENTE`** porque transcribe una
afirmacion del libro. **Cada uno baja el porcentaje y sube el tamanio del lote siguiente sin
que nadie haya hecho nada mal.**

**Y NO LO ADJUDICO, Y DIGO POR QUE CON LAS DOS REGLAS DELANTE.** Manual seccion 2 pide pasos
**imperativos**, y *Cuenta con* lo es gramaticalmente; manual seccion 4 dice que **una postura
no ejecuta una busqueda**, pero esa regla decide **duplicacion entre nodos**, no que puede
haber dentro de uno. **Leerla como prohibicion de forma seria ESTRECHAR la vara**, y `6.3` dice
que mover esa frontera es parada y decision de Alexis, no mia. **`D.56` ademas congela la cola
de doctrina y me manda exactamente esto: registrarlo en el acta con su medida y dejarlo ahi.**
**Queda aqui, medido, con su instrumento y sin encargo.**

## 46.8. LA MUESTRA PINEADA DE LOS SANOS (`AUDITOR_FORJA.md` 7)

**LA POBLACION ES CERO, Y NO SE INVENTA UNA MUESTRA DONDE NO HAY POBLACION.**

    $ git diff --stat 327d969 HEAD -- bitacora/VEREDICTOS.jsonl
    (vacio)
    $ wc -l bitacora/VEREDICTOS.jsonl
    740

**Cero veredictos `SANO` escritos en esta tanda**, porque la puerta de `D.39` mide cerrada por
tercera vuelta seguida y sin insercion no hay acto donde escribir un veredicto. **Lo mas
parecido que hay son las nueve lecturas de cola que el reporte adelanta, y esas las relei
enteras en `46.4`: las nueve.** Cuando el lote 7 abra la insercion, esta seccion tendra por fin
poblacion propia y la muestra se echa con su semilla escrita.

## 46.9. `PASOS INVENTADOS POR CAPITULO` (`AUDITOR_FORJA.md` 8). **UNA FILA POR CAPITULO**

**Es una cifra que el extractor me da y que yo firmo**, asi que la cuento yo de las fichas
(8.3, punto 1) y releo los pasos contra su parrafo (punto 2). **Los `45` de hoy los lei uno a
uno en mi fase ciega, no por muestra; los `50` de la vuelta 46 los lei uno a uno en la
`ACTA 45`.**

    $ python .v47aud/33_pasos_cap04.py
    fichas de cap_04: 14   pasos: 95

| capitulo | vuelta | PUENTE | pasos escritos | por ciento | tope | quien conto el denominador |
|---|---|---:|---:|---:|---:|---|
| `cap_04` de `grove_high_output` | 47, los `6` de hoy | **0** | **45** | **0,00** | 10 | yo, `.v47aud/33_pasos_cap04.py` |
| `cap_04` de `grove_high_output` | 46, los `8` anteriores | **0** | **50** | **0,00** | 10 | yo, `95` menos `45` sobre el mismo instrumento |
| **`cap_04` entero, las dos tandas** | 46 y 47 | **0** | **95** | **0,00** | 10 | yo, de las `14` fichas |

**FIRMO EL `0` DE `95` DE `cap_04`.** Y digo lo que la coincidencia de las dos filas prueba y
lo que no: prueba que **nadie ha tocado las ocho fichas de la vuelta 46**; que sus `50` pasos
sean del libro lo probe yo releyendolos, que es otra clase de prueba. **El desglose por
capitulo existe y no hubo que pedirlo despues** (8.3, punto 3).

**EL VOLUMEN NO SUBE, y el motivo esta en `46.5.d`:** no manda aqui la metrica, manda
`EXTRACTOR.md` 12.4, y `cap_04` sigue abierto en `8` de `22`.

## 46.10. MIS CAIDAS PROPIAS, CON MI NOMBRE

**NINGUNA DE LAS DOS ESPECIES QUE MI RACHA ACUMULA**, y lo digo despues de haber ido a
buscarlas, no antes.

| especie mia | esta tanda | como lo comprobe |
|---|---|---|
| **`CIFRA PUBLICADA PROPIA`** | **NINGUNA** | recorri las cifras de mi pagina sellada y las volvi a medir hoy: la huella del acta (`d0255b4e...`), los `45` pasos, los `95` del capitulo, las `346` `740` `1`, el `548` con su descomposicion (`346` mas `202`) y el `385` con la suya (`346` mas `36` mas `3`), el `14` de `cap_04`, el `22` de la frontera recompuesto en `46.2.a`, y el id inexistente contra las `894` fichas. **Ninguna se movio** |
| **`REMEDIO ROTO`** | **NINGUNA** | el remedio de `45.9.b` se cumplio: los guiones y las salidas de mi fase ciega estan en `.v47aud/` dentro del arbol, y mi unico superlativo sellado llevaba su lista ordenada entera pegada |

**Y LO QUE SI HICE MAL, QUE NO ACUMULA Y VA IGUAL CON MI NOMBRE:** escribi el remedio de la
`ACTA 45` **como parrafo dentro de un bloque de cita**, y `src/herencia.py` entrega filas de
tabla **fuera de cita**, asi que el arnes me entrego `heredados: 0`. **El remedio se cumplio
por la otra red** (leer mi propia acta en la fase ciega), no por la que `D.40` puso. **No
cuenta como `REMEDIO ROTO`** y cito la acotacion del 12 sep 2026 que lo dice con todas las
letras: *un remedio sobre formato de artefactos no existe como remedio, es tarea del arnes*.
**Y el arreglo lo pongo aqui mismo**, escribiendo los mios de esta vuelta en tabla y fuera de
cita, que es la forma que el instrumento sabe leer.

### 46.10.a. **MIS REMEDIOS PARA LA VUELTA 48**

| REMEDIO | que me obliga | como se comprueba que esta roto |
|---|---|---|
| **REMEDIO DEL AUDITOR, VUELTA 48, primero** | **Todo superlativo que yo publique (el mas alto, el mas proximo, el mas rico, el unico) lleva debajo la LISTA ORDENADA ENTERA que lo sostiene**, salida de un instrumento mio corrido en esa misma fase y pegada. Es la caida que acabo de cargarle al extractor dos veces en `46.6`, y no me la puedo permitir yo | se abre mi acta y mi apertura, se busca cada superlativo y se mira si debajo hay una lista ordenada con su comando. **Sin lista, roto** |
| **REMEDIO DEL AUDITOR, VUELTA 48, segundo** | **Todo remedio que yo deje escrito va en TABLA y FUERA de bloque de cita**, para que `src/herencia.py` lo entregue y no dependa de que yo lea mi propia acta | `python forja.py herencia` en la vuelta 48 tiene que entregar **`heredados: 2`**. **Si entrega `0`, roto** |

## 46.11. EL CREDITO DE ESTA TANDA

| especie | esta tanda | racha al cerrar | por que |
|---|---|---|---|
| **CLASE** | **LIMPIA** | **`0 de 2`** | cero veredictos escritos (`740` contra `740`), y los seis discutibles y las nueve lecturas de cola se sostienen |
| **CIFRA PUBLICADA** | **LIMPIA** | **`0 de 2`** | las dos caidas viven en `docs/loop/REPORTE.md`, que se reescribe cada vuelta, y no en sede duradera |
| **DATO MOVIDO** | **LIMPIA** | **`0 de 2`** | `git diff --stat 327d969 HEAD -- dataset/ bitacora/ config/` da vacio |
| **REPORTE** | **`2` caidas, NINGUNA ACUMULA** | **`0 de 3`** | las dos en prosa de acompaniamiento (`5.2`), no en tabla, cabecera ni conclusion. Y `5.4`: *limpia significa sin caidas de la especie que esa racha acumula* |
| **AUDITOR** | **LIMPIA** | **de `2 de 3` a `0 de 3`** | ni `CIFRA PUBLICADA PROPIA` ni `REMEDIO ROTO`, comprobado cifra a cifra en `46.10`. **La reinicia una tanda limpia** (`5.4` con `D.38.1`), que es una de las dos formas escritas, **y ninguna de las dos soy yo decidiendo que me absuelvo** |

## 46.12. LAS CONDICIONES DE PARADA (`AUDITOR_FORJA.md` 3): **NINGUNA SE CUMPLE**

| condicion | como sale | medido con |
|---|---|---|
| doctrina NUEVA necesaria | **NO**: las cuatro adjudicaciones de `46.5` se apoyan en reglas escritas por extension citable, y la medida de forma de `46.7` **se registra y se deja ahi**, que es lo que `D.56` manda | `46.5` y `46.7` |
| contradiccion con regla vigente o cifra publicada | **NO**: las dos caidas del reporte se corrigen por correccion declarada, que es el mecanismo que ya existe | `46.6` |
| decision de Alexis | **NO**: no se borra contenido, no se mueve umbral, no se cambia el alcance, no se crea remoto | `git diff` de `config/` vacio |
| fallo tecnico repetido | **NO**: gate, guiones, pruebas, tallado, censo y tabla de cierre, **los seis en verde hoy** | `46.2` |
| credito roto | **NO**: ninguna especie en su tope, y dos bajan | `46.11` |
| campania consumada | **NO** | `python forja.py tablero`: *MUNDO 11: faltan 3 de 3 libros del corte* |

**NO ESCRIBO `docs/loop/PARA_ALEXIS.md`.** El encargo de la vuelta `48` sale de esta sede.

## 46.13. EL COSTE DEL TURNO (`D.55`)

**ESTA VUELTA MIA NO ES DE SANEAMIENTO.** No pago deuda, no toco `src/`, `scripts/`, `tests/`,
el banco, el arnes ni los protocolos: lo unico que escribo fuera de `docs/loop/` es
`.v47aud/`, que son mis guiones y sus salidas.

**LA CIFRA EN USD NO LA DOY PORQUE NINGUN INSTRUMENTO DE ESTA CASA LA MIDE**, y `2` me prohibe
afirmar lo que no he consultado:

    $ grep -rl "USD" src/ scripts/ forja.py | wc -l
    0

**LO QUE LA REGLA PERSIGUE, EL EN QUE SE FUE, SI LO ENTREGO:** la pieza cara de mi turno es
**la prueba de aceptacion, corrida una vez** (`318` pruebas, del orden de dos minutos de
reloj), y el resto se fue en **los guiones de medida de `.v47aud/`**, todos de segundos, mas la
lectura del capitulo y de las fichas. **En mi turno no corre ni una aduana**, que es la pieza
que se lleva el `95,3` por ciento del turno del extractor. **Mi turno es barato y el suyo no, y
esa asimetria es la cifra que le sirve a quien tenga que decidir donde se gasta.**
