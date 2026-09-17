# APERTURA CIEGA DEL AUDITOR. FRENTE `gerber_emyth`, VUELTA 1

*Fase ciega de `D.34`, ampliada por `D.34.2`. Escrita ANTES de que el arnes me exponga
el reporte. Rige `D.38.3` (toda cifra con su instrumento pegado, y la conclusion sobre
contenido en linea aparte marcada `LECTURA`), `D.38.4` (el barrido sobre grafo mas
bandejas), `D.40` (la herencia entregada y declarada), `D.45` (moratoria de maquinaria y
de doctrina) y `D.47` (austero).*

> **ESTE FRENTE NO INSERTA.** Nada de lo que escribo aqui toca `dataset/`, `bitacora/`,
> `censos/` ni `config/`. Lo unico que escribo en el arbol es este fichero y
> `docs/loop/.v01_gerber/clases_ciegas.md`.

---

## 0. LA DECLARACION QUE EL ARNES EXIGE

    ACTA ANTERIOR LEIDA: f6c76f63bd9b6aeea7b1d5a9d485977d2d61f593
    HEREDADO 1: CUMPLIDO
    HEREDADO 2: CUMPLIDO
    HEREDADO 3: CUMPLIDO
    HEREDADO 4: CUMPLIDO

**LA HUELLA LA CORRO YO Y NO LA COPIO DEL PROMPT** (`HEREDADO 3`):

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    f6c76f63bd9b6aeea7b1d5a9d485977d2d61f593

**Y LA ULTIMA ACTA ES LA 30, QUE CUBRE LA VUELTA 31:**

    $ grep -n "^# ACTA" docs/loop/ACTA_AUDITOR.md | tail -2 | cut -c1-90
    26226:# ACTA 29. VUELTA 30, lote 4 (`scott_radical_candor`), `cap_07` CERRADO EN INSERCION
    27082:# ACTA 30. VUELTA 31, lote 4 (`scott_radical_candor`), **`cap_11` insertado de once

---

## 1. CADA HEREDADO, CON LO QUE LO SOSTIENE

### HEREDADO 1: CUMPLIDO

> *"NINGUNA CELDA DE MI APERTURA SELLADA LLEVA UN NUMERO QUE SALGA DE UNA LECTURA MIA."*

**Como lo cumplo, y es lo unico que cuenta:** toda celda de tabla de este fichero lleva
o bien una cifra de instrumento **con su salida pegada en el mismo apartado**, o bien
las palabras `POR ADJUDICAR`. **Mis conteos de lectura no entran en ninguna celda: van
en parrafo, marcados `LECTURA`.**

**Y EL REMEDIO ME CAZO ALGO HOY, que es para lo que estaba.** Escribi mis clases a
fichero con tres citas de linea leidas a ojo, volvi a correr el instrumento antes de
sellar, y **las tres eran imposibles**: en este recorte toda linea con contenido lleva
numero **par**, y yo habia escrito `L257`, `L97` y `L33`.

    $ for f in fuentes/gerber_emyth/*.md; do awk '/^---$/{n++;next} n>=2' $f \
        | grep -n . | cut -d: -f1 \
        | awk -v F=$(basename $f .md) '{if($1%2)i++} END{print F " impares: " i+0}'; done
    cap_01 impares: 0
    cap_02 impares: 0
    cap_03 impares: 0
    cap_04 impares: 0
    cap_05 impares: 0
    cap_06 impares: 0
    cap_07 impares: 0
    cap_08 impares: 0
    cap_09 impares: 0
    cap_10 impares: 0
    cap_11 impares: 0
    cap_12 impares: 0
    cap_13 impares: 0
    cap_14 impares: 0
    cap_15 impares: 0
    cap_16 impares: 0
    cap_17 impares: 0
    cap_18 impares: 0
    cap_19 impares: 0
    cap_20 impares: 0
    cap_21 impares: 0
    cap_22 impares: 0

**Las tres quedan corregidas por correccion declarada y sin borrarse** en
`docs/loop/.v01_gerber/clases_ciegas.md`, y **a este fichero sellado llegan ya con su
`grep` al lado** (apartado 6.1). **Lo declaro como caida propia cazada antes de sellar:
un numero cuya unica fuente era mi ojo es exactamente la especie que el remedio
prohibe.**

### HEREDADO 2: CUMPLIDO

> *"LA RELECTURA CIEGA DESTAPA UNA RAZON POR VEZ, Y DESPUES DE ESCRIBIR MI CLASE A
> FICHERO. [...] que el acta publique la hora del fichero de clases y que sea anterior a
> la primera corrida que IMPRIMA UNA RAZON."*

**LA HORA DEL FICHERO DE MIS CLASES:**

    $ ls --full-time docs/loop/.v01_gerber/clases_ciegas.md
    -rw-r--r-- 1 AlexDesk 197609 4462 2026-09-16 21:08:48.133353300 -0400 docs/loop/.v01_gerber/clases_ciegas.md

**LA PRIMERA CORRIDA MIA QUE PODIA IMPRIMIR UNA RAZON, Y ES POSTERIOR:**

    $ date "+%Y-%m-%d %H:%M:%S"
    2026-09-16 21:09:01
    $ grep -o '"razon": "[^"]\{0,60\}' bitacora/VEREDICTOS.jsonl | grep -i gerber
    $ echo "RAZONES DE gerber_emyth IMPRESAS: $(grep -c gerber bitacora/VEREDICTOS.jsonl)"
    RAZONES DE gerber_emyth IMPRESAS: 0

`21:08:48` es anterior a `21:09:01`. **Y ADEMAS no habia ninguna razon que destapar:
este libro no tiene ni una linea en la bitacora.** El fichero se escribio primero de
todas formas, que es lo que el remedio manda y no lo que las circunstancias permiten.

### HEREDADO 3: CUMPLIDO

> *"TODA CIFRA QUE FIRMO COMO MIA LA CORRO YO EN ESTA VUELTA, aunque el reporte la traiga
> medida."*

**No hay reporte del que copiar: no lo he abierto** (apartado 7). Cada cifra de este
fichero lleva debajo **mi** comando y **mi** salida, corridos en esta fase. Las guardas
del apartado 3, la poblacion del apartado 4 y la frontera del apartado 5 son todas
corridas mias, incluida la huella del acta del apartado 0, que el prompt me daba hecha
y que he vuelto a correr.

### HEREDADO 4: CUMPLIDO

> *"UNA TABLA QUE PUBLICO COMO DE INSTRUMENTO NO LLEVA UNA CONSTANTE TECLEADA DENTRO."*

**Mis instrumentos de esta fase son ordenes de una linea, y van enteros pegados.** El
unico que produce una tabla es el de la frontera (apartado 5), y **no tiene ni una
constante tecleada dentro**: el nombre de la unidad lo saca del frontmatter del propio
fichero, la lista de ficheros la saca del glob, y las palabras y las lineas las cuenta
`wc`. **Cero listas de ids a mano, cero cifras tecleadas.** Se ve en su codigo, que esta
pegado entero.

**Y NO ESCRIBO NINGUN INSTRUMENTO NUEVO EN `src/` NI EN `scripts/`** (`D.45`, `D.47`).

---

## 2. LO QUE EL ARBOL TIENE Y LO QUE NO, AL EMPEZAR

    $ git log --oneline -3
    6d2d56a FRENTE gerber_emyth vuelta 1: el esqueleto del reporte abierto antes de la primera tarea (EXTRACTOR.md 3), y la apertura medida antes de la primera operacion
    272e8ce arnes: loop.log de la apertura del frente gerber_emyth
    b4012fb FRENTE gerber_emyth: encargo de su vuelta 1 en austero, y este frente NO inserta (D.45)

**LA BANDEJA DE ESTE LIBRO ESTA VACIA.** Medida dos veces, con veinticuatro minutos de
diferencia, y **el resultado cambio de forma pero no de fondo**:

    $ ls -1 cuarentena/gerber_emyth/ 2>&1; echo "codigo de salida: $?"     # 20:47
    ls: cannot access 'cuarentena/gerber_emyth/': No such file or directory
    codigo de salida: 2

    $ date "+%H:%M:%S"; ls -1 cuarentena/gerber_emyth/ 2>&1 | head          # 21:11
    21:11:13

**`LECTURA`: a las 20:47 la carpeta no existia; a las 21:11 existe y esta vacia.** Es
decir, **el extractor esta corriendo mientras yo escribo esta fase** y ya creo su
bandeja. Lo digo aqui y no lo resuelvo: ver el apartado 7.

**CERO CANDIDATOS QUE CLASIFICAR.** Mi clasificacion de esta fase es, por tanto,
**sobre el TEXTO FUENTE y no sobre candidatos**, que es lo que queda cuando la bandeja
esta vacia y es lo que el encargo de la vuelta 1 describe (*"ABRE EL LIBRO. La bandeja
esta vacia"*).

    $ ls -1 cuarentena/
    _insertados/
    ensayo_referencia_163/
    LEEME.md
    marquet_turn_the_ship/
    scott_radical_candor/

---

## 3. LAS GUARDAS, CORRIDAS POR MI EN ESTA FASE

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 270
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python scripts/censar_rutas.py
      pasan                     : 519
      CAEN                      : 0
    CENSO VERDE: las 519 rutas publicadas sostienen lo que dicen sostener.

    $ python tests/test_aceptacion.py
      total: 201 pruebas, 0 fallos, 0 errores

    $ python forja.py resolutor
    nodos vivos: 270
    nodos deprecados (archivo): 0
    alias registrados: 0

| guarda | estado | de donde sale |
|---|---|---|
| `gate` | **VERDE**, 270 nodos | salida pegada arriba |
| `guiones` | **VERDE** | salida pegada arriba |
| censo de rutas `D.42` | **VERDE**, 519 rutas | salida pegada arriba |
| aceptacion | **VERDE**, 201 pruebas, 0 fallos | salida pegada arriba |
| resolutor | 270 vivos, 0 deprecados, 0 alias | salida pegada arriba |

**Las cinco en verde. Ninguna de las seis condiciones de parada de `AUDITOR_FORJA.md` 3
se cumple por estado del arbol.**

### 3.1. CORRECCION DECLARADA, ANTES DEL SELLO: `guiones` YA NO ESTA EN VERDE

*La tabla de arriba **no se borra**: era cierta a las `21:05` y la pego entera. **Volvi a
correr la guarda a las `21:18`, antes de entregar este fichero, y habia cambiado.***

    $ date "+%H:%M:%S"; python forja.py guiones
    21:18:06
    BARRIDO DE GUIONES EN ROJO: 4 hallazgo(s)
      .gerber_v1/citas.py linea 24 columna 25: guion largo (U+2014)
      .gerber_v1/citas.py linea 25 columna 25: guion medio (U+2013)
      .gerber_v1/citas.py linea 26 columna 21: guion largo (U+2014)
      .gerber_v1/citas.py linea 26 columna 42: guion medio (U+2013)
    Regla: cero guiones largos y cero guiones medios en todo el repo (manual seccion 2). Usa el guion corto normal.

**LOS CUATRO HALLAZGOS SON DEL MISMO FICHERO, Y ESE FICHERO NO ES MIO:**
`.gerber_v1/citas.py` es del extractor, y a las `21:05`, cuando corri la guarda la
primera vez, **no existia** (`git status` de las `21:11` lo lista como `??`, apartado 7).

**LO QUE SI ES MIO SALE VERDE, y lo mido aparte para no esconderme detras del reparto:**

    $ python forja.py guiones docs/loop/APERTURA_CIEGA.md docs/loop/.v01_gerber/clases_ciegas.md
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

**POR QUE LO ESCRIBO EN VEZ DE DEJAR LA TABLA COMO ESTABA.** La `ACTA 26` declaro `NO
APLICA` un heredado de guiones mientras el barrido estaba en rojo con ocho hallazgos
suyos, y esa es la caida que puso `D.40` en su forma de hoy. **Publicar `guiones: VERDE`
en un fichero sellado cuando la guarda esta en rojo es una cifra falsa en sede
duradera**, tenga la culpa quien la tenga. **La corrijo aqui, antes del sello, sin borrar
la medida vieja y con su hora al lado.**

**NO LO ARREGLO, y digo por que:** el fichero es del extractor y esta en su turno; `D.45`
me prohibe tocar lo que otra sesion esta escribiendo. **Lo dejo medido y nombrado para mi
turno normal.**

---

## 4. LA POBLACION DEL BARRIDO (`D.38.4`)

    $ wc -l dataset/nodos.jsonl
    270 dataset/nodos.jsonl

    $ ls -1 cuarentena/*/*.json | grep -v _insertados | grep -v _derivadas \
        | grep -v ensayo_referencia_163 | wc -l
    78

    $ ls -1 cuarentena/*/*.json | grep -v _insertados | grep -v _derivadas \
        | grep -v ensayo_referencia_163 | sed 's#/[^/]*$##' | sort | uniq -c
          3 cuarentena/marquet_turn_the_ship
         75 cuarentena/scott_radical_candor

| pieza | cuanto |
|---|---:|
| grafo, `dataset/nodos.jsonl` | **270** |
| bandejas que esperan juicio, sin `_insertados`, sin `_derivadas` y sin `ensayo_referencia_163` | **78** |
| **poblacion del barrido** | **348** |
| de ellos, de `gerber_emyth` | **0** |

**`LECTURA`: no hay ni un barrido de vecinos que correr en esta fase.** El metodo
vigente de `D.38.4` (correccion declarada del 16 sep) es
`python forja.py informe cuarentena/<lote>/<id>.json`, **uno por vez**, y no hay ni un
`<id>.json` de este libro contra el que correrlo. **No publico ni un vecino, y digo por
que, en vez de publicar cero y llamarlo barrido**, que es la errata de metodo que la
`ACTA 18` corrigio en esta misma regla.

---

## 5. LA FRONTERA DEL LIBRO, DE INSTRUMENTO

**EL INSTRUMENTO, entero y sin ninguna constante dentro** (`HEREDADO 4`):

    $ for f in fuentes/gerber_emyth/*.md; do
        u=$(awk '/^---$/{n++;next} n==1 && /^unidad:/{sub(/^unidad: */,"");print;exit}' "$f")
        w=$(awk '/^---$/{n++;next} n>=2' "$f" | wc -w)
        l=$(awk '/^---$/{n++;next} n>=2' "$f" | wc -l)
        printf "%-14s %-42s %7s %6s\n" "$(basename $f)" "$u" "$w" "$l"
      done

**SU SALIDA, pegada de ahi:**

    FICHERO        UNIDAD                                     PALABRAS LINEAS
    cap_01.md      Foreword                                      1402     64
    cap_02.md      Introduction                                  1212     92
    cap_03.md      Cap. 1                                        2202    226
    cap_04.md      Cap. 2                                        3713    290
    cap_05.md      Cap. 3                                        2400    142
    cap_06.md      Cap. 4                                        1980    214
    cap_07.md      Cap. 5                                        4284    322
    cap_08.md      Cap. 6                                        2183    172
    cap_09.md      Cap. 7                                        2845    226
    cap_10.md      Cap. 8                                        1411    138
    cap_11.md      Cap. 9                                        4360    322
    cap_12.md      Cap. 10                                       4206    286
    cap_13.md      Cap. 11                                         364     52
    cap_14.md      Cap. 12                                       3695    210
    cap_15.md      Cap. 13                                       4685    272
    cap_16.md      Cap. 14                                       4835    482
    cap_17.md      Cap. 15                                       2448    214
    cap_18.md      Cap. 16                                       5396    406
    cap_19.md      Cap. 18                                       4431    434
    cap_20.md      Cap. 19                                       1841     72
    cap_21.md      Epilogue                                      1851    142
    cap_22.md      Afterword                                      904    122

    $ for f in fuentes/gerber_emyth/*.md; do awk '/^---$/{n++;next} n>=2' "$f" | wc -w; done \
        | awk '{s+=$1} END{print "SUMA DE PALABRAS DE CUERPO: " s}'
    SUMA DE PALABRAS DE CUERPO: 62648

    $ ls -1 fuentes/gerber_emyth/*.md | wc -l
    22

### 5.1. UNA DIFERENCIA DE 786 PALABRAS ENTRE DOS CIFRAS PUBLICADAS, Y NO ES UNA CIFRA FALSA

**El encargo de esta vuelta y `docs/loop/PARALELO.md` publican `63.434` palabras. Mi
instrumento dice `62.648`, que es lo que dicen `ORDEN_DE_LOTES.md` y
`FUENTES_CANONICAS.json`.**

    $ grep -n "gerber" docs/loop/ORDEN_DE_LOTES.md | head -1
    25:| 9 | `gerber_emyth` | 22 | 62.648 | sin su cap. 17 |

    $ cat fuentes/gerber_emyth/*.md | wc -w
    63434

**`LECTURA`, y cierra al digito: las dos son ciertas y miden poblaciones distintas.**
`63.434` es el `wc -w` de los ficheros **enteros, con su frontmatter dentro**; `62.648`
es el **cuerpo**, que es lo que se mina. La diferencia, `786`, es el frontmatter de las
veintidos unidades. **No la cargo como cifra falsa a nadie**, y la dejo escrita porque
**la cifra que dimensiona un frente conviene que sea la del cuerpo**: el frontmatter no
produce nodos.

### 5.2. EL `cap. 17` APARTADO, COMPROBADO Y NO CREIDO

    $ awk '/^---$/{n++;next} n==1' fuentes/gerber_emyth_cap17_reservado/cap_17.md
    libro: Gerber, The E-Myth Revisited
    edicion: Copyright 2007 by Michael E. Gerber, HarperCollins e-books, EPub Edition May 2007, ISBN 9780061741654 (ebook) / 0-06-072318-1 (hardcover)
    unidad: Cap. 17
    titulo_textual: Your Marketing Strategy
    fidelidad: verbatim

    $ awk '/^---$/{n++;next} n>=2' fuentes/gerber_emyth_cap17_reservado/cap_17.md | wc -w
    3845

**`LECTURA`: el salto es real y esta donde el encargo dice.** En la tabla de arriba
`cap_19.md` lleva `unidad: Cap. 18`, asi que **la serie salta de `Cap. 16` a `Cap. 18`**
dentro de `fuentes/gerber_emyth/`, y el `Cap. 17` vive aparte con sus `3.845` palabras.
**Las dos cifras me salen al digito contra `FUENTES_CANONICAS.json`.**

---

## 6. MI CLASIFICACION CIEGA DEL TEXTO FUENTE

**Esto es lo que despues comparo con la lectura del extractor.** He leido entero el
cuerpo de las ONCE primeras unidades, `cap_01` a `cap_11`, que cubren el Foreword, la
Introduction y los capitulos `1` a `9` del libro. **Son mas unidades que las que cabe
minar en una vuelta al techo de candidatos, asi que la comparacion no se me queda
corta.**

**LAS TRES CLASES QUE USO, y las digo antes de usarlas:**

| clase | que significa |
|---|---|
| **PROCEDIMIENTO** | la unidad dicta pasos que el lector ejecuta. **Es nodo** |
| **DIAGNOSTICO** | la unidad describe, nombra o advierte. **NO es nodo**: los pasos habria que ponerlos yo, y eso es `PUENTE` (`D.30`) |
| **DISCUTIBLE** | hay accion nombrada y no hay pasos propios. **Lo marco a ciegas y no lo resuelvo** |

| unidad | fichero | MI CLASE | candidatos que le leo |
|---|---|---|---|
| Foreword | `cap_01` | **DIAGNOSTICO** | `POR ADJUDICAR` |
| Introduction | `cap_02` | **DIAGNOSTICO** | `POR ADJUDICAR` |
| Cap. 1 | `cap_03` | **DIAGNOSTICO** | `POR ADJUDICAR` |
| Cap. 2 | `cap_04` | **DISCUTIBLE** | `POR ADJUDICAR` |
| Cap. 3 | `cap_05` | **DISCUTIBLE** | `POR ADJUDICAR` |
| Cap. 4 | `cap_06` | **DIAGNOSTICO** | `POR ADJUDICAR` |
| Cap. 5 | `cap_07` | **PROCEDIMIENTO** | `POR ADJUDICAR` |
| Cap. 6 | `cap_08` | **PROCEDIMIENTO** | `POR ADJUDICAR` |
| Cap. 7 | `cap_09` | **DIAGNOSTICO** | `POR ADJUDICAR` |
| Cap. 8 | `cap_10` | **DIAGNOSTICO** | `POR ADJUDICAR` |
| Cap. 9 | `cap_11` | **PROCEDIMIENTO** | `POR ADJUDICAR` |

**LAS CELDAS DICEN `POR ADJUDICAR` A PROPOSITO** (`HEREDADO 1`): el numero de candidatos
que le leo a una unidad **sale de mi lectura y de ningun instrumento**, asi que no entra
en celda. Va en el parrafo de 6.2, marcado `LECTURA`.

### 6.1. LO QUE SOSTIENE CADA CLASE, con su `grep` pegado

**EL INSTRUMENTO que produce todas las lineas que cito:**

    $ cita () { awk '/^---$/{n++;next} n>=2' fuentes/gerber_emyth/$1.md \
                  | grep -n . | grep -E "$2" | cut -c1-96; }

**SU SALIDA.** *Las comillas tipograficas y los guiones largos del recorte van aqui
sustituidos por sus equivalentes ASCII, que es lo que la guarda `guiones` obliga: el
numero de linea y las palabras son los del instrumento, el signo no.*

    --- cap_04 ---
    256:"If it's true that within each businessperson there are three personalities, rather than
    284:"So the work of an Entrepreneur is to wonder," I continued. "To imagine and to dream.
    --- cap_05 ---
    114:"Don't you see? If your business depends on you, you don't own a business [...] you have a
    --- cap_06 ---
    96:It's called Management by Abdication rather than by Delegation .
    --- cap_07 ---
    266:"Simply put, your job is to prepare yourself and your business for growth.
    274:"By asking the right questions, such as: Where do I wish to be? When do I wish to be there
    280:"Remember, Sarah, any plan is better than no plan.
    --- cap_08 ---
    32:IBM is what it is today for three special reasons. The first reason is that, at the very begi
    34:The second reason was that once I had that picture, I then asked myself how a company which l
    36:The third reason IBM has been so successful was that once I had a picture of how IBM would lo
    40:From the very outset, IBM was fashioned after the template of my vision. And each and every d
    108:When The Entrepreneur creates the model, he surveys the world and asks: "Where is the oppo
    --- cap_11 ---
    34:In other words, pretend that you are going to franchise your business. (Note: I said pretend
    38:1. The model will provide consistent value to your customers, employees, suppliers, and lende
    40:2. The model will be operated by people with the lowest possible level of skill.
    42:3. The model will stand out as a place of impeccable order .
    44:4. All work in the model will be documented in Operations Manuals.
    46:5. The model will provide a uniformly predictable service to the customer.
    48:6. The model will utilize a uniform color, dress, and facilities code.
    246:Go to work on your business rather than in it, and ask yourself the following questions:

**Y LO QUE LEO EN CADA UNA:**

| unidad | linea del instrumento | `LECTURA` |
|---|---|---|
| `cap_01` | ninguna | autobiografia y dedicatoria. **Cero imperativos dirigidos al lector** |
| `cap_02` | ninguna | anuncia cuatro `IDEAS` y publica tasas de quiebra. **Material de `atribuciones`, no de `pasos_accionables`** |
| `cap_03` | ninguna | define el `Entrepreneurial Seizure` y la `Fatal Assumption`. **Son nombres, y nombrar no es procedimentar** |
| `cap_04` | `256`, `284` | `256` manda observarse a si mismo durante el dia; `284` es el `Future Work`, el `I wonder`. **Las dos dentro de un dialogo y sin secuencia propia** |
| `cap_05` | `114` | prueba de dependencia enunciada. **Acierta como criterio y no trae ni un paso** |
| `cap_06` | `96` | nombra `Management by Abdication rather than by Delegation`. **No dice como delegar** |
| `cap_07` | `266`, `274`, `280` | **dicta las preguntas del plan de crecimiento** (donde, cuando, cuanto capital, cuanta gente, que tecnologia, cuanto espacio en `Benchmark` Uno, Dos y Tres), **manda escribirlo** y **manda plan de contingencia de mejor y peor caso** |
| `cap_08` | `32`, `34`, `36`, `40`, `108` | los tres pasos de Watson mas el cierre diario, **dichos como pasos por la propia fuente**; y en `108` la construccion del modelo **empezando por el cliente** |
| `cap_09` | ninguna | historia de Ray Kroc y del `Business Format Franchise`. **Cifras, no pasos** |
| `cap_10` | ninguna | describe **que ES** el `Franchise Prototype` y cierra con las preguntas que responde `cap_11` |
| `cap_11` | `34`, `38` a `48`, `246` | **fingir 5.000 replicas, las SEIS REGLAS y el resumen ejecutable.** Las reglas `2` y `4` traen procedimiento propio; las `1`, `3`, `5` y `6` son criterios |

### 6.2. LO QUE MI LECTURA PREDICE, y es falsable

> **`LECTURA`, y va aqui y no en celda porque el numero es mio:** las once primeras
> unidades me dan **entre CINCO y OCHO candidatos reales**, y **seis de ellas me dan
> CERO**: `cap_01`, `cap_02`, `cap_03`, `cap_06`, `cap_09` y `cap_10`.

**LAS TRES COSAS QUE SE PUEDEN COMPROBAR CONTRA EL REPORTE CUANDO ME LO EXPONGAN:**

1. **Un nodo firmado sobre cualquiera de esas seis unidades** es, en mi lectura, un nodo
   con los pasos puestos por la mano que escribe y no por el libro. **Eso se mide con la
   relectura de fidelidad `D.30` contra el parrafo**, que es la guarda que el austero
   deja intacta.
2. **El techo de candidatos de la vuelta, entre cinco y quince, NO se alcanza por orden
   de libro dentro de `cap_01` a `cap_11`.** Una vuelta que lo alcance ahi habra bajado
   la vara, no encontrado mas material.
3. **El grueso procedimental esta de `cap_13` en adelante**, y esto **no** es lectura mia
   sino cuenta de maquina:

    $ for f in fuentes/gerber_emyth/*.md; do printf "%-11s listas=%s\n" "$(basename $f .md)" \
        "$(grep -cE '^[0-9]+\.|^[[:space:]]*[-*] ' $f)"; done
    cap_01      listas=0
    cap_02      listas=1
    cap_03      listas=1
    cap_04      listas=1
    cap_05      listas=1
    cap_06      listas=1
    cap_07      listas=1
    cap_08      listas=2
    cap_09      listas=1
    cap_10      listas=1
    cap_11      listas=14
    cap_12      listas=1
    cap_13      listas=8
    cap_14      listas=1
    cap_15      listas=1
    cap_16      listas=1
    cap_17      listas=1
    cap_18      listas=14
    cap_19      listas=10
    cap_20      listas=1
    cap_21      listas=0
    cap_22      listas=2

**`LECTURA` sobre esa cuenta, y va marcada porque es una conclusion sobre contenido y no
la medida:** las cuatro unidades por encima de siete son `cap_11`, `cap_13`, `cap_18` y
`cap_19`, y **tres de las cuatro caen fuera del tramo que una vuelta 1 por orden de libro
puede alcanzar.**

### 6.3. LOS TRES DISCUTIBLES QUE MARCO A CIEGAS, por numero y linea

*En austero van por numero y linea, sin reabrir el argumento (`D.47`).*

| # | unidad y linea | por que dudo |
|---|---|---|
| **1** | `cap_04` `L256` | la observacion de si mismo esta dicha en **una** frase larga dentro de un dialogo. **Si se parte en pasos, los pasos los pongo yo** |
| **2** | `cap_04` `L284` | `I wonder` es una pregunta, y **una pregunta repetida tres veces no es una secuencia**. La casa ya tiene doctrina: **nombrar no es procedimentar** (`P.5.1`) |
| **3** | `cap_05` `L114` | la prueba de dependencia **no trae ni un paso**. Puede vivir como `condiciones_activacion` de otro nodo en vez de como nodo propio |

**Y UNA CUARTA DUDA QUE NO ES DISCUTIBLE SINO DE CORTE:** `cap_11` puede salir como
**un** nodo (las seis reglas como pasos de una comprobacion) o como **tres** (la
comprobacion, mas el manual de operaciones de la regla `4`, mas la dependencia de
sistema y no de personas de la regla `2`). **No lo resuelvo aqui**, y lo dejo escrito
para poder decir despues si el extractor y yo cortamos en el mismo sitio.

---

## 7. LO QUE NO HE ABIERTO, Y LO QUE EL ARBOL HIZO MIENTRAS ESCRIBIA

**NO HE ABIERTO NINGUNO DE LOS CUATRO QUE `D.34.2` RETIRA:** `docs/loop/REPORTE.md`,
`docs/loop/loop.log`, `docs/loop/ultimo_extractor.json` ni `docs/loop/ultimo_auditor.json`.
**Y NO LOS HE RECUPERADO DE GIT.** Si he abierto `docs/loop/ACTA_AUDITOR.md`, que es obra
mia, no es ninguno de los cuatro, y `D.40` y el docstring de `src/herencia.py` dicen en
voz alta que puedo.

**PERO EL ARBOL SE MOVIO DEBAJO DE MI, Y LO DEJO ESCRITO CON SU HORA:**

| hora | que vi | con que instrumento |
|---|---|---|
| **20:47** | los cuatro ficheros **ausentes** del arbol y `cuarentena/gerber_emyth/` **inexistente** | `ls -la docs/loop/`, `ls -1 cuarentena/gerber_emyth/` |
| **20:55** | los cuatro **de vuelta** y `git status` **limpio**, tras el commit `272e8ce` del arnes | `ls -la docs/loop/`, `git status --short` |
| **21:11** | HEAD en `6d2d56a`, del **extractor**, y `cuarentena/gerber_emyth/` **creada y vacia** | `git log --oneline -1`, `ls -1 cuarentena/gerber_emyth/` |

    $ git show --stat --oneline 6d2d56a | head -10
    6d2d56a FRENTE gerber_emyth vuelta 1: el esqueleto del reporte abierto antes de la primera tarea (EXTRACTOR.md 3), y la apertura medida antes de la primera operacion
     .gerber_v1/apertura.py  | 47 +++++++++++++++++++++++++++++++++++++++++++
     .gerber_v1/apertura.txt | 41 ++++++++++++++++++++++++++++++++++++++
     .gerber_v1/frontera.py  | 53 +++++++++++++++++++++++++++++++++++++++++++++++++
     docs/loop/REPORTE.md    | 20 +++++++++++++++++++
     4 files changed, 161 insertions(+)

    $ git status --short --untracked-files=all | head -6
    ?? .gerber_v1/citas.py
    ?? .gerber_v1/frontera_cap01.txt
    ?? .gerber_v1/frontera_cap02.txt
    ?? .gerber_v1/frontera_cap03.txt
    ?? .gerber_v1/frontera_cap04.txt
    ?? .gerber_v1/frontera_cap05.txt

**`git show --stat` y `git status --short` ensenian NOMBRES Y RECUENTOS, no contenido.**
Los corri para saber que se habia movido, y **pare ahi**.

> ### LO QUE ESTO ABRE, Y NO LO DECIDO YO
>
> **`.gerber_v1/apertura.txt` es la apertura medida del extractor, y no es ninguno de los
> cuatro ficheros que `D.34.2` retira.** Abrirlo seria leer sus medidas antes de publicar
> las mias, **que es exactamente la puerta que `D.34.2` cerro cuando anadio el cuarto
> fichero** (*el mensaje final del extractor es un resumen de su propio reporte*). **NO LO
> HE ABIERTO, ni el ni ninguno de los `frontera_capNN.txt` ni `piezas_capNN.txt`.**
>
> **Y ES UNA PREGUNTA DE DOCTRINA: si la retirada de `D.34.2` es de CUATRO NOMBRES o de
> TODO LO QUE EL EXTRACTOR MIDE.** `D.45` dice que **una pregunta de doctrina en paralelo
> es PARADA y sube al fundador**, y que ninguna sesion toca el banco ni los protocolos
> mientras corran los frentes. **Asi que la declaro y no la resuelvo**, ni aqui ni en mi
> turno normal.
>
> **NO ES UNA CAIDA DE NADIE HOY:** ninguna regla escrita le prohibe al extractor escribir
> sus instrumentos en el arbol, y `D.41` le manda pegar sus tablas de fichero. **Lo que
> falta es la frase que diga que hacer con esos ficheros durante mi fase ciega.**

---

## 8. EL HUECO DE ACTA (`AUDITOR_FORJA.md` 1.0), DECLARADO

**La ultima acta es la `ACTA 30` y cubre la `VUELTA 31`** (apartado 0). **La `VUELTA 32`
corrio entera, cerro, y no tiene acta:**

    $ git log --oneline -30 | grep -ciE "VUELTA 32"
    6

**`LECTURA`: hay hueco de una vuelta, y NO es de este frente.** La `VUELTA 32` es del
frente serial de insercion (`extraccion-mundo-11`), que sigue vivo en su propio worktree
y tiene su propio auditor; este frente es la **vuelta 1** de `gerber_emyth` y su encargo
dice *"cada frente mide su libro y nada mas"*.

**LO DECLARO Y NO LO AUDITO AQUI, y digo por que:** auditar la `VUELTA 32` desde esta rama
significaria adjudicar sobre `dataset/` y `bitacora/`, que son **sedes unicas** y que este
frente **no toca** (`D.45`, `PARALELO.md` 5.2). **Quien la audite tiene que ser quien tenga
el grafo entero delante.** Lo dejo escrito para que el hueco no se pierda por haber abierto
tres frentes: **una vuelta sin auditar es una vuelta sin verificar, por mucho que las
siguientes salgan verdes.**

---

## 9. LO QUE CIERRO CON ESTA APERTURA

| | |
|---|---|
| **candidatos clasificados** | **0**, porque la bandeja esta vacia (apartado 2, con su `ls`) |
| **unidades fuente leidas enteras** | **11** de **22** (`cap_01` a `cap_11`), con sus citas grepeadas en 6.1 |
| **discutibles marcados a ciegas** | **3**, por numero y linea, en 6.3 |
| **guardas corridas por mi** | **5**, verdes a las `21:05`; **`guiones` en ROJO a las `21:18`** con `4` hallazgos, ninguno mio (apartado 3.1) |
| **poblacion del barrido `D.38.4`** | **348**, que es **270** de grafo mas **78** de bandejas |
| **vecinos publicados** | **0**, y se dice por que: no hay candidato contra el que barrer |
| **cifras sin instrumento al lado** | **ninguna** |
| **caidas propias cazadas antes de sellar** | **3** citas de linea imposibles, corregidas sin borrarse (apartado 1, `HEREDADO 1`) |
| **preguntas de doctrina** | **1**, declarada y NO resuelta (apartado 7) |
| **huecos de acta** | **1**, la `VUELTA 32`, declarada y no auditada aqui (apartado 8) |

### Y LA DECLARACION, REPETIDA COMO PERMITE `D.40`

    ACTA ANTERIOR LEIDA: f6c76f63bd9b6aeea7b1d5a9d485977d2d61f593
    HEREDADO 1: CUMPLIDO
    HEREDADO 2: CUMPLIDO
    HEREDADO 3: CUMPLIDO
    HEREDADO 4: CUMPLIDO

**NO COMMITEO. El arnes sella este fichero y lo commitea el.**
