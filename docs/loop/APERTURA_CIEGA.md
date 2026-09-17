# APERTURA CIEGA. FRENTE `grove_high_output`, VUELTA 1

*Fase ciega del auditor (`D.34`). **Rama `extraccion-grove_high_output`, worktree
`../forja-grove_high_output`.** Modo austero (`D.47`): cifras talladas y cero parrafo que
repita lo que ya dice el registro.*

> **ESTA APERTURA ES MAS CIEGA QUE LAS ANTERIORES, y hay que decirlo porque cambia lo que
> vale.** Las otras se escribian con el extractor ya corrido y su reporte retirado. Esta se
> escribe **antes de que el extractor de este frente haya escrito nada**: la bandeja del
> libro **no existe todavia**. **Mi corte no puede parecerse al suyo por contagio, porque el
> suyo aun no esta.**

---

## 0. LA DECLARACION QUE EL ARNES EXIGE (`D.40`)

    ACTA ANTERIOR LEIDA: f6c76f63bd9b6aeea7b1d5a9d485977d2d61f593
    HEREDADO 1: CUMPLIDO
    HEREDADO 2: NO APLICA
    HEREDADO 3: CUMPLIDO
    HEREDADO 4: CUMPLIDO

**La huella es la que el prompt me entrega, y la cruzo con el arbol en esta misma fase:**

    $ git ls-tree HEAD docs/loop/ACTA_AUDITOR.md
    100644 blob f6c76f63bd9b6aeea7b1d5a9d485977d2d61f593	docs/loop/ACTA_AUDITOR.md

    $ git rev-parse HEAD
    be2b6782f3728e3cfe28a7e2e7d05fba4013063e

**Ese `HEAD` es el de CUANDO MIDO, y se movio debajo de mi antes de cerrar.** Lo cuento en
`3.1`, con su commit y su `--stat`, porque una huella que envejece dentro de la propia fase
**se declara y no se corrige por lo bajo**.

---

## 1. LOS CUATRO HEREDADOS, UNO A UNO, CON SU SALIDA PEGADA

### 1.1. `HEREDADO 1`: **CUMPLIDO**

> *Ninguna celda de mi apertura sellada lleva un numero que salga de una lectura mia.*

**Como lo cumplo:** toda cifra en celda de tabla de este fichero sale de un instrumento que
corri en esta fase, y su fichero de salida esta nombrado en la propia tabla. **Las cifras que
salen de MI LECTURA no van en celda**: van en frase marcada `LECTURA`, y su celda dice
`POR ADJUDICAR`.

**Y LO COMPRUEBO CON UN INSTRUMENTO, no con mi palabra:** `celdas.py` saca **toda** celda de
tabla de este mismo fichero que lleve una cifra, sin saber cual espera.

    $ python .vg01c/celdas.py docs/loop/APERTURA_CIEGA.md
    CELDAS DE TABLA CON CIFRA: 64

**De esas `64`, las unicas que son una CUENTA son las ocho de la tabla de `2.`, y las ocho
llevan su instrumento en la celda de al lado.** Las otras `56` son rotulos de pieza (`P1`,
`Q7`), citas de linea (`L57`, `L81`), nombres de regla (`D.38.4`, `D.30`), rutas de fichero e
ids de nodo. **Ni una cuenta mia sin instrumento.**

**Y LOS DOS `POR ADJUDICAR` QUE ABRO AQUI SON ESTOS**, para que el acta les deba seccion:
**cuantos candidatos saco yo de `cap_01`** y **cuantos de `cap_02`** (secciones `5.1` y
`5.2`). Sus numeros viven en la frase, marcados `LECTURA`, porque salen de leer y no de medir.

    $ ls .vg01c/
    celdas.py             cierre.txt            cierre_frontera.py    cuatro_repuestos.txt
    frontera.py           frontera_cap_01.txt   frontera_cap_02.txt   frontera_cap_03.txt
    guardas.txt           heredado1.txt         heredado2.txt         heredado3.txt
    heredado4.txt         mis_clases.txt        piezas.py             piezas_cap_01.txt
    piezas_cap_02.txt     poblacion.py          poblacion.txt

### 1.2. `HEREDADO 2`: **NO APLICA**, y el motivo es que **no hay razon que destapar**

> *La relectura ciega destapa una razon por vez, y despues de escribir mi clase a fichero.*

**MOTIVO:** el remedio rige sobre la relectura de **veredictos ajenos**, y este frente no
tiene ninguno: **la bandeja del libro no existe y la bitacora no trae ni una linea suya.** No
hay razon escrita que yo pueda destapar, ni antes ni despues de nada.

    $ ls -la --time-style=full-iso .vg01c/mis_clases.txt
    -rw-r--r-- 1 AlexDesk 197609 3348 2026-09-16 21:06:58.161277700 -0400 .vg01c/mis_clases.txt

    $ date
    2026-09-16 21:07:10 -0400

    $ wc -l bitacora/VEREDICTOS.jsonl
    396 bitacora/VEREDICTOS.jsonl

    $ grep -c grove_high_output bitacora/VEREDICTOS.jsonl
    0

    $ ls cuarentena/grove_high_output/
    ls: cannot access 'cuarentena/grove_high_output/': No such file or directory

**Y AUN ASI LE CUMPLO LA FORMA**, porque cumplirla aqui es gratis y romperla despues es
caro: **mis clases estan escritas a fichero a las `21:06:58`, y mi primera consulta de la
bitacora es de las `21:07:10`.** Doce segundos, pero en el orden que el remedio pide.

### 1.3. `HEREDADO 3`: **CUMPLIDO**

> *Toda cifra que firmo como mia la corro yo en esta vuelta, aunque el reporte la traiga
> medida.*

**Las dos cifras que el encargo publica del libro, remedidas por mi:**

    $ ls fuentes/grove_high_output/ | wc -l
    18

    $ wc -w fuentes/grove_high_output/*.md | tail -1
     64862 total

**Las dos me salen al digito contra el encargo** (`18` unidades, `64.862` palabras). Y el
instrumento de la herencia lo corro yo, no lo copio del prompt:

    $ python forja.py herencia
      su huella     : f6c76f63bd9b6aeea7b1d5a9d485977d2d61f593
      heredados     : 4

### 1.4. `HEREDADO 4`: **CUMPLIDO**

> *Una tabla que publico como de instrumento no lleva una constante tecleada dentro.*

    $ grep -nE "\"[a-z_]{8,}\"|'[a-z_]{8,}'" .vg01c/*.py
    .vg01c/poblacion.py:12:raiz = 'cuarentena'

**La unica constante larga de texto en mis cuatro instrumentos es el nombre del directorio
`cuarentena`.** Ni una lista de ids, ni un rotulo, ni un titulo. Y el unico instrumento que
SI teclea algo suyo **lo dice en su primera linea de salida**, que es justo lo que el remedio
pide:

    $ head -1 .vg01c/piezas_cap_02.txt
    INSTRUMENTO piezas.py  CONSTANTE TECLEADA DENTRO: SI, los RANGOS de linea, que son MI LECTURA. Las palabras y la cobertura las mide el fichero.

    $ head -1 .vg01c/poblacion.txt
    INSTRUMENTO poblacion.py  SIN IDS TECLEADOS: lee dataset/nodos.jsonl y cuarentena/*/ (descarta los que empiezan por _)

---

## 2. LO QUE MIDO DEL ESTADO, ANTES DE LEER NADA

| que | cifra | instrumento que la saca |
|---|---:|---|
| nodos del grafo | **270** | `.vg01c/guardas.txt`, `forja.py gate` |
| lineas de la bitacora | **396** | `.vg01c/heredado2.txt`, `wc -l` |
| lineas de la bitacora de este libro | **0** | `.vg01c/heredado2.txt`, `grep -c` |
| candidatos en bandeja de este libro | **0** | `.vg01c/heredado2.txt`, `ls`, la carpeta no existe |
| poblacion de vecinos, `D.38.4` | **511** | `.vg01c/poblacion.txt`, `poblacion.py` |
| unidades del libro | **18** | `.vg01c/heredado3.txt`, `ls` mas `wc -l` |
| palabras del libro | **64.862** | `.vg01c/heredado3.txt`, `wc -w` |
| pruebas de aceptacion | **201** | `.vg01c/guardas.txt`, `tests/test_aceptacion.py` |

**Las tres guardas de la casa, corridas por mi en esta fase:**

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 270

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python tests/test_aceptacion.py
      total: 201 pruebas, 0 fallos, 0 errores

**La poblacion de `D.38.4`, desglosada por su instrumento:**

    $ python .vg01c/poblacion.py
    BANDEJA:ensayo_referencia_163     163
    BANDEJA:marquet_turn_the_ship       3
    BANDEJA:scott_radical_candor       75
    GRAFO                             270
    POBLACION TOTAL                   511

---

## 3. UNA AVERIA DE LA FASE QUE DECLARO ANTES QUE MI TRABAJO

**Los cuatro ficheros que `D.34.2` retira ESTABAN retirados cuando el arnes me invoco, y a
mitad de mi fase volvieron al arbol.** No los he abierto, y digo como se que no hacia falta
abrirlos para saber de donde salieron.

    $ git log --oneline -2
    be2b678 loop.log: registro pendiente antes de abrir la vuelta 1 del frente grove_high_output
    6c93aa2 FRENTE grove_high_output: encargo de su vuelta 1 en austero, y este frente NO inserta (D.45)

    $ git show --stat be2b678 | tail -3
     docs/loop/loop.log | 4 ++++
     1 file changed, 4 insertions(+)

    $ ls -la --time-style=full-iso docs/loop/REPORTE.md docs/loop/loop.log docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json
    -rw-r--r-- 1 AlexDesk 197609   61554 2026-09-16 20:55:13.807706600 -0400 docs/loop/loop.log
    -rw-r--r-- 1 AlexDesk 197609 2499868 2026-09-16 20:55:06.491572500 -0400 docs/loop/REPORTE.md
    -rw-r--r-- 1 AlexDesk 197609    4619 2026-09-16 20:55:06.494579800 -0400 docs/loop/ultimo_auditor.json
    -rw-r--r-- 1 AlexDesk 197609       0 2026-09-16 20:55:13.916224400 -0400 docs/loop/ultimo_extractor.json

    $ git status --short docs/loop/
    (vacio, sin una sola diferencia contra HEAD)

**LECTURA:** el commit `be2b678` toca **solo `loop.log`**, y sin embargo los cuatro aparecen
en el arbol con hora `20:55` y **sin una sola diferencia contra `HEAD`**. Eso es un
`checkout` reponiendo ficheros seguidos, no un extractor escribiendolos. **El reporte que hay
en el arbol es el del mundo 11 y no el de este frente**, asi que su reposicion no me
contamina de lo que vengo a leer a ciegas. **Aun asi no lo he abierto, porque la regla no
dice no te contamines: dice no lo abras.**

**Y UNA CIFRA QUE NO VOY A MALINTERPRETAR.** `ultimo_extractor.json` esta a **cero bytes**, y
la cosecha `7.B` dice que un testigo en cero bytes cuenta como turno mudo. **Aqui no lo es:**

    $ git ls-tree HEAD docs/loop/ultimo_extractor.json
    100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391	docs/loop/ultimo_extractor.json

    $ git hash-object -t blob /dev/null
    e69de29bb2d1d6434b8b29ae775ad8c2e48c5391

**`e69de29` es el blob vacio de git**, asi que el fichero ya estaba a cero **en `HEAD`, antes
de mi fase y antes de este frente**. Lo digo porque la lectura facil era cargarlo como turno
mudo del extractor de grove, y **habria sido una cifra propia falsa con el instrumento pegado
al lado**, que es exactamente la especie que me tumbo en la vuelta 26.

### 3.1. Y LA SEGUNDA MITAD DE LA AVERIA: **el extractor corre A LA VEZ que mi fase ciega**

**Mientras yo escribia esto, el turno del extractor abrio su reporte y commiteo.** No lo he
abierto. Lo se sin abrirlo porque el commit **se llevo por delante mi propio directorio de
trabajo**, que estaba a medio escribir:

    $ git log --oneline -3
    862390c VUELTA 1 grove_high_output: el reporte se abre con la apertura medida y las tres tareas con su fila vacia
    be2b678 loop.log: registro pendiente antes de abrir la vuelta 1 del frente grove_high_output
    6c93aa2 FRENTE grove_high_output: encargo de su vuelta 1 en austero, y este frente NO inserta (D.45)

    $ git show --stat 862390c | tail -4
     .vg01c/poblacion.py         |  39 ++++++++++++++
     .vg01c/poblacion.txt        |   6 +++
     docs/loop/REPORTE.md        |  70 +++++++++++++++++++++++++
     22 files changed, 722 insertions(+)

**QUE SIGNIFICA Y QUE NO.** `D.34` pone mi fase ciega **antes** de que se me exponga el
reporte, no antes de que el reporte exista; que el extractor escriba mientras yo leo el libro
**no me contamina**, porque lo que no he hecho es abrirlo. **Lo que si rompe es la prueba de
orden:** hasta hoy mi apertura se sellaba con el turno del extractor ya cerrado, y **la
huella que firmo en `0.` envejece dentro de mi propia fase**.

**Y TIENE UN LADO BUENO QUE ME CONVIENE DECIR, porque me favorece y por eso hay que medirlo
en vez de celebrarlo:** `862390c` **commitea `.vg01c/mis_clases.txt`**, asi que mis clases de
`cap_01` y `cap_02` quedan **en el arbol, fechadas, en el mismo commit que abre su reporte y
antes de que exista un solo candidato suyo**. Mi corte no puede ya ser reescrito despues de
ver el suyo, y eso no es merito mio: **es que el arnes lo sello sin querer.**

**LO QUE RECOMPRUEBO DESPUES DEL COMMIT, porque una cifra mia no puede envejecer callando:**

    $ python forja.py gate | head -2
    GATE VERDE.
      nodos verificados: 270

    $ wc -l bitacora/VEREDICTOS.jsonl
    396 bitacora/VEREDICTOS.jsonl

    $ ls cuarentena/grove_high_output/
    ls: cannot access 'cuarentena/grove_high_output/': No such file or directory

    $ python .vg01c/poblacion.py | tail -1
    POBLACION TOTAL                   511

**Las cuatro cifras de la tabla de `2.` que el commit podia haber movido no se han movido, y
la bandeja del libro SIGUE SIN EXISTIR.** Asi que todo lo de `4.` a `7.` sigue escrito contra
un libro que nadie ha cortado todavia.

**ESTO NO ES PARADA Y NO LO ENCARGO AQUI:** las dos mitades son del arnes, y `D.45` le prohibe
a este frente tocar el arnes. **Se declaran y suben al fundador con el acta.**

---

## 4. MI FRONTERA CIEGA, Y CIERRA CONTRA EL CUERPO

**Ningun corte se publica si la suma de las piezas no da el cuerpo entero, con cero lineas
sin cubrir y cero solapes.**

    $ python .vg01c/cierre_frontera.py fuentes/grove_high_output/cap_01.md fuentes/grove_high_output/cap_02.md fuentes/grove_high_output/cap_03.md
    fuentes/grove_high_output/cap_01.md    cabecera=   23 cuerpo= 3841 suma=  3864 fichero=  3864  CIERRA=SI
    fuentes/grove_high_output/cap_02.md    cabecera=   41 cuerpo= 3386 suma=  3427 fichero=  3427  CIERRA=SI
    fuentes/grove_high_output/cap_03.md    cabecera=   27 cuerpo= 5828 suma=  5855 fichero=  5855  CIERRA=SI

    $ wc -w fuentes/grove_high_output/cap_01.md fuentes/grove_high_output/cap_02.md fuentes/grove_high_output/cap_03.md
     3864 fuentes/grove_high_output/cap_01.md
     3427 fuentes/grove_high_output/cap_02.md
     5855 fuentes/grove_high_output/cap_03.md

### 4.1. `cap_01`, unidad `Introduction`

    $ python .vg01c/piezas.py fuentes/grove_high_output/cap_01.md ROTULO=9:9 Q1=11:49 Q2=51:59 Q3=61:67 Q4=69:77 Q5=79:85 Q6=87:101 Q7=103:107 Q8=109:119
    ROTULO L9    a L9     lineas= 1  palabras=    1
    Q1     L11   a L49    lineas=20  palabras= 1218
    Q2     L51   a L59    lineas= 5  palabras=  497
    Q3     L61   a L67    lineas= 4  palabras=  369
    Q4     L69   a L77    lineas= 5  palabras=  540
    Q5     L79   a L85    lineas= 4  palabras=  403
    Q6     L87   a L101   lineas= 8  palabras=  439
    Q7     L103  a L107   lineas= 3  palabras=  178
    Q8     L109  a L119   lineas= 6  palabras=  196
    SUMA DE LAS PIEZAS: 3841 palabras
    CUERPO ENTERO:      3841 palabras
    LINEAS DE CUERPO SIN PIEZA: 0  ->  []
    SOLAPES: NO

### 4.2. `cap_02`, unidad `Cap. 1`, *The Basics of Production*

    $ python .vg01c/piezas.py fuentes/grove_high_output/cap_02.md ROTULO=9:13 P0=15:21 P1=23:29 P2=31:35 P3=37:47 P4=49:61 P5=63:67 P6=69:69 P7=71:75 P8=77:79
    ROTULO L9    a L13    lineas= 3  palabras=   19
    P0     L15   a L21    lineas= 4  palabras=  273
    P1     L23   a L29    lineas= 4  palabras=  336
    P2     L31   a L35    lineas= 3  palabras=  259
    P3     L37   a L47    lineas= 6  palabras=  582
    P4     L49   a L61    lineas= 7  palabras=  596
    P5     L63   a L67    lineas= 3  palabras=  370
    P6     L69   a L69    lineas= 1  palabras=  237
    P7     L71   a L75    lineas= 3  palabras=  263
    P8     L77   a L79    lineas= 2  palabras=  451
    SUMA DE LAS PIEZAS: 3386 palabras
    CUERPO ENTERO:      3386 palabras
    LINEAS DE CUERPO SIN PIEZA: 0  ->  []
    SOLAPES: NO

> **LOS RANGOS SON MI LECTURA Y EL INSTRUMENTO LO DICE EN SU PRIMERA LINEA.** Lo que mide el
> fichero son las palabras, la cobertura y el solape. **Donde corto lo decido yo, y por eso
> es comparable con donde corte el.**

---

## 5. MIS CLASES A CIEGAS, PIEZA POR PIEZA

**La vara es la de `AUDITOR_FORJA.md` 6.1, y la pregunta es una: el texto da PROCEDIMIENTO, o
da POSTURA, RELATO o DEFINICION.** *Nombrar no es procedimentar; una advertencia es linea.*

### 5.1. `cap_01`, unidad `Introduction`

| pieza | lineas | **MI CLASE** | lo que la sostiene |
|---|---|---|---|
| `Q1` | `L11` a `L49` | **NO CANDIDATO** | relato y diagnostico: el ataque japones de las memorias, la globalizacion, el correo. Cero imperativos al lector |
| `Q2` | `L51` a `L59` | **NO CANDIDATO** | definicion de a quien va dirigido el libro. `L57` define al know-how manager, y definir no es procedimentar |
| `Q3` | `L61` a `L67` | **NO CANDIDATO** | **POSTURA.** `L65`: *let chaos reign, then rein in chaos*. Una postura no ejecuta una busqueda (vara `6.1`) |
| `Q4` | `L69` a `L77` | **NO CANDIDATO** | las tres ideas del libro y el simil del cuerpo de bomberos. Tesis, no pasos |
| `Q5` | `L79` a `L85` | **NO CANDIDATO EN ESTA UNIDAD** | `L81` a `L85` comentan la reunion a solas y le cambian frecuencia y duracion, pero **no la montan**. Su procedimiento es de `cap_05` |
| `Q6` | `L87` a `L101` | **NO CANDIDATO** | diagnostico de carrera. `L101` dice literalmente *I can offer you no surefire formula* |
| `Q7` | `L103` a `L107` | **CANDIDATO** | las **tres preguntas** numeradas por el propio texto: anadir valor, estar enchufado, probar tu mismo lo nuevo. Enumeradas, ejecutables, y la primera trae su como |
| `Q8` | `L109` a `L119` | **NO CANDIDATO** | cierre y firma |

**CANDIDATOS QUE YO SACO DE `cap_01`: `POR ADJUDICAR`.**
**LECTURA: uno, y es `Q7`.** Es cifra de lectura mia, y por eso no va en celda
(`HEREDADO 1`).

### 5.2. `cap_02`, unidad `Cap. 1`

| pieza | lineas | **MI CLASE** | lo que la sostiene |
|---|---|---|---|
| `P0` | `L15` a `L21` | **NO CANDIDATO** | la carta de la produccion: entregar a la hora comprometida, a calidad aceptable y al menor coste. Definicion |
| `P1` | `L23` a `L29` | **CANDIDATO** | `L23` nombra el **paso limitante** y manda fijarlo primero; `L25` y `L27` mandan trabajar **hacia atras** desde la hora de entrega y **desfasar** cada componente por su propio tiempo de paso |
| `P2` | `L31` a `L35` | **NO CANDIDATO**, marcado **DISCUTIBLE** | es `P1` aplicado al reclutamiento. Lo unico propio es el cribado telefonico de `L33`. **Lo que le daria la vuelta:** leer el cribado como paso con entregable propio, la razon de ofertas por visita |
| `P3` | `L37` a `L47` | **DISCUTIBLE**, me inclino a **CANDIDATO** | `L39` da los tres tipos de operacion; `L41` y `L45` dan el retrabajo y el **test de unidad antes del test de sistema**, que si es procedimiento |
| `P4` | `L49` a `L61` | **CANDIDATO** | `L51` dice que la capacidad limitada **MUEVE** el paso limitante; `L59` da las alternativas y `L61` manda reducir el canje entre mano de obra, capacidad e inventario a **relaciones cuantificables** |
| `P5` | `L63` a `L67` | **CANDIDATO** | `L67` cierra con la regla en imperativo: **preferir la prueba en proceso a la que destruye producto**, con el termometro y el aviso como ejemplar |
| `P6` | `L69` | **CANDIDATO** | inspeccion de recepcion, y la **regla de dimensionado**: inventario igual al consumo durante el plazo de reposicion, pesado contra su coste y contra la **oportunidad en riesgo** |
| `P7` | `L71` a `L75` | **CANDIDATO** | `L75`: *detect and fix any problem in a production process at the lowest-value stage possible*. Una regla, tres instancias trabajadas |
| `P8` | `L77` a `L79` | **NO CANDIDATO** | la justicia penal es **ILUSTRACION** de `P1` y `P7`. El texto no le da ni un paso al lector. **Si el reporte trae nodo de aqui, mi clase es PUENTE** (`D.30`) |

**CANDIDATOS QUE YO SACO DE `cap_02`: `POR ADJUDICAR`.**
**LECTURA: cinco firmes (`P1`, `P4`, `P5`, `P6`, `P7`) mas uno discutible (`P3`), o sea cinco
o seis.**

---

## 6. EL BARRIDO DE VECINOS, SOBRE GRAFO MAS BANDEJAS (`D.38.4`)

**Y AQUI HAY UN HALLAZGO QUE NO ES DE FORMA.** El grafo de esta casa **no tiene ni un nodo de
produccion ni de calidad**: es gestion de personas y contratacion.

    $ python (censo de fuentes y dominios sobre dataset/nodos.jsonl)
    FUENTES EN EL GRAFO:
     zhuo_manager                       136
     scott_radical_candor                67
     smart_who                           59
     onu_consumidor                       6
     manual_sistema_conocimiento          2
    DOMINIOS EN EL GRAFO:
     gestion_equipos                    203
     contratacion                        59
     proteccion_consumidor                6
     forja                                2

**LECTURA, y es la que pre registro:** los vecinos de `cap_02` de Grove **no estan en el
grafo. Estan enteros en la bandeja `ensayo_referencia_163`**, que trae `163` candidatos de
dominio de calidad y que **`D.38.4` obliga a barrer y el grafo solo no ve**. **Un barrido que
cargue solo `dataset/nodos.jsonl` le va a devolver CERO vecinos a todo `cap_02` y va a
declarar SANOS los siete.** Es el caso exacto que `D.38.4` y `D.38.5` vinieron a cerrar, y es
la primera vez que un frente lo puede disparar entero.

    $ python .vg01c/poblacion.py cuello botella restric limitante throughput capacidad
    BANDEJA:ensayo_referencia_163 constraint_management       Gestion de Restricciones (Teoria de las Restricciones)
    BANDEJA:ensayo_referencia_163 restricciones_extremas_como_innovacion
    BANDEJA:ensayo_referencia_163 comprension_capacidades_limitaciones_ia
    CASAN: 3

### 6.1. Las cinco clases que dejo pre registradas, con su vecino y su razon

| mi pieza | vecino mas cercano | sede del vecino | **MI CLASE, A CIEGAS** | la razon, con la vara |
|---|---|---|---|---|
| `P1` | `constraint_management` | bandeja `ensayo_referencia_163` | **CONTINUA** | el vecino da identificar, explotar, subordinar, elevar y repetir. **Grove no da ninguno de esos cinco: da la programacion hacia atras con desfases.** Queda procedimiento propio de los dos lados, y la vara dice que eso no es duplicado |
| `P4` | `constraint_management` | bandeja `ensayo_referencia_163` | **CONTINUA** de `P1`, no del vecino | `P4` anade lo que `P1` no dice: que el limitante **se mueve** cuando la capacidad aprieta, y el canje cuantificado. Si el reporte funde `P1` y `P4` en un nodo, **mi clase es que pierde el desplazamiento del limitante** |
| `P6` | `just_in_time_manufacturing` | bandeja `ensayo_referencia_163` | **CONTINUA** | el vecino manda **bajar** el inventario progresivamente. Grove da **cuanto**: el consumo durante el plazo de reposicion, contra la oportunidad en riesgo. Lo que queda fuera es procedimiento en los dos lados |
| `P7` | `proceso_como_cadena_de_etapas` | bandeja `ensayo_referencia_163` | **CONTINUA** | el vecino **mapea** la cadena y busca donde nacen los defectos. Grove dice **donde cortar**: la etapa de menor valor. Mapear no es decidir |
| `Q5` si se escribe | `montar_reuniones_solas_mentalidad_frecuencia` | **GRAFO** | **REPITE** | el nodo del grafo ya monta la reunion a solas con su mentalidad, su frecuencia y su agenda. `L81` a `L85` de Grove **solo le cambia el mando de la frecuencia**, y eso es una linea, no una expansion |

### 6.2. Y un choque **dentro del propio libro** que dejo apuntado antes de que ocurra

`cap_03` repite la regla del menor valor en `L131` a `L133`, con estas palabras:
*the key principle is to reject the defective material at its lowest-value stage*.

**MI CLASE PRE REGISTRADA:** un nodo de `cap_02` `P7` **y** un nodo de `cap_03` `L131` a
`L133` son **REPITE entre ellos**. Lo que **si** es `CONTINUA` de `P7` es `cap_03` `L135` a
`L143`, que es otra cosa: **que hacer cuando el material se rechaza**, y como abaratar el
esquema de inspeccion. **La frontera limpia esta en `L135`, no en `L131`.**

---

## 7. LO QUE PREVEO DE LA VUELTA, ESCRITO PARA QUE SE PUEDA FALSAR

**El techo de este frente es de cinco a quince candidatos**, y `cap_01` mas `cap_02` me dan,
por mi lectura, **seis o siete**. **LECTURA: preveo que la vuelta NO cierre en `cap_02` y
entre en `cap_03`**, que es donde estan los indicadores, el grafico escalonado, el fabricar
contra pedido o contra pronostico, el esquema de inspeccion y la palanca.

**Las tres formas en que esto puede salir, escritas antes de verlo:**

1. **Coincidimos pieza a pieza en `cap_02`.** Entonces la fuerza del corte no es de ninguno
   de los dos: es del texto, y lo digo asi en el acta en vez de apuntarmelo.
2. **El saca nodo de `P2` o de `P8`.** Son sus dos sitios de puente: el reclutamiento y la
   justicia penal son ilustraciones, y **el texto no le da pasos al lector en ninguna de las
   dos**. Ahi mi clase ya esta escrita y no la muevo despues.
3. **El declara SANOS los siete de `cap_02`.** Entonces lo que fallo no son sus clases: es
   que **barrio solo el grafo**, donde no hay ni un nodo de calidad, y `D.38.4` le pedia
   grafo mas bandejas. **Esa es la caida que mas me espero**, y la dejo nombrada con su
   cifra: la bandeja `ensayo_referencia_163` tiene **163** candidatos y el grafo **270**
   nodos, y **los tres vecinos que le encuentro a este libro estan los tres en la primera.**

---

## 8. MIS RUTAS, QUE VIAJAN CON EL COMMIT

**Cosecha `7.B`: una ruta que prueba una corrida y no viaja deja de probar nada en cuanto
otro clona.** Mis ficheros de esta fase viven en `.vg01c/` y van al repo con el sello.

| fichero | que prueba |
|---|---|
| `.vg01c/frontera.py` y sus tres `.txt` | el corte en lineas y palabras de `cap_01`, `cap_02` y `cap_03` |
| `.vg01c/cierre_frontera.py`, `.vg01c/cierre.txt` | que las tres fronteras cierran contra el cuerpo |
| `.vg01c/piezas.py`, `.vg01c/piezas_cap_01.txt`, `.vg01c/piezas_cap_02.txt` | mis piezas, su cobertura y su cero solapes |
| `.vg01c/poblacion.py`, `.vg01c/poblacion.txt` | la poblacion de `D.38.4`, grafo mas bandejas |
| `.vg01c/mis_clases.txt` | mis clases, con su hora, escritas antes de tocar la bitacora |
| `.vg01c/guardas.txt` | gate, guiones y las 201 pruebas, corridas por mi |
| `.vg01c/celdas.py`, `.vg01c/heredado1.txt` | que ninguna celda de tabla de esta apertura lleva una cuenta sin instrumento |
| `.vg01c/heredado2.txt`, `.vg01c/heredado3.txt`, `.vg01c/heredado4.txt` | la salida pegada de cada heredado |
| `.vg01c/cuatro_repuestos.txt` | la averia de la seccion `3`, con su commit y sus horas |

---

## 9. LO QUE NO HE HECHO EN ESTA FASE, DICHO POR MI

- **No he abierto `REPORTE.md`, `loop.log`, `ultimo_extractor.json` ni `ultimo_auditor.json`**,
  aunque los cuatro estaban en el arbol desde las `20:55`.
- **No he recuperado ninguno de git**, ni por `git show` de su contenido, ni por `checkout`,
  ni por diff. Lo unico que he corrido sobre ellos es `ls`, `git ls-tree`, `git status
  --short` y `git show --stat`, que dan tamanio, huella y nombre de fichero, y **no dan ni una
  linea de su texto**.
- **No he abierto `cap_04` en adelante.** Mi prevision de la seccion `7` sobre `cap_03` se
  apoya solo en el corte de lineas de `cap_03`, que es lo que hay pegado en `4.`, y en las
  dos lineas suyas que cito en `6.2`.
- **No he tocado `src/`, ni el banco, ni el arnes, ni los protocolos** (`D.45`).

*Apertura ciega del frente `grove_high_output`, vuelta 1, cerrada para que el arnes la selle.
**No la vuelvo a tocar**: el sello se verifica al terminar el turno.*
