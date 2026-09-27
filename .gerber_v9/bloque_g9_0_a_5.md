# FRENTE `gerber_emyth`, VUELTA 9: **LA ULTIMA. `cap_01`, `cap_02` Y `cap_03`, Y EL LIBRO QUEDA ENTERO** (`D.58`, frente en paralelo: **NO INSERTA**)

## G9.0. EL ESQUELETO DE LA VUELTA (`EXTRACTOR.md` 3)

| # | tarea del encargo | como cierra | donde |
|---:|---|---|---|
| 1 | `TAREA 1`: registros de apertura | **CERRADA**: credito y deuda medidos, deuda subida a `49`/`39` desde la `44`/`39` del cierre de `G8` (`5` deudas nuevas de `ACTA G8`, ajenas a mi) | `G9.1` |
| 2 | `cap_01`, `Foreword`: frontera y veredicto | **CERRADA**: frontera `3` piezas, `1402` palabras de cuerpo (`1434` con la cabecera yaml, al digito con `wc -w`), residuo `0`; cero candidatos, prefacio personal sin inventario propio; cero discutibles | `G9.2` |
| 3 | `cap_02`, `Introduction`: frontera y veredicto | **CERRADA**: frontera `4` piezas, `1212` palabras de cuerpo (`1244` con la cabecera yaml), residuo `0`; cero candidatos, las cuatro ideas del libro nombradas como metas sin inventario de medios; cero discutibles | `G9.3` |
| 4 | `cap_03`, `Cap. 1, The Entrepreneurial Myth`: frontera y veredicto, `PASOS INVENTADOS` y muestra de fidelidad | **CERRADA**: frontera `5` piezas, `2202` palabras de cuerpo (`2237` con la cabecera yaml), residuo `0`; cero candidatos, diagnostico narrativo del mito y del caso de Sarah sin inventario propio; cero discutibles; muestra de fidelidad con semilla `g9` sin poblacion que medir | `G9.4` |
| 5 | `TAREA 2`: cerrar `d094` y publicar la frontera del libro entero, `cap_01` a `cap_22` | **CERRADA**: `d094` pagada citando esta vuelta; tabla del libro entero publicada, `22` de `22` unidades minadas, `22` candidatos en bandeja; los cuatro punteros heredados (`d098`, `d104`, `d108`, `d111`) comprobados, ninguno tocado por estos tres capitulos | `G9.5` |

**CINCO TAREAS ENCARGADAS, EN EL TOPE DE CINCO** (`EXTRACTOR.md` 1.3): las tres del punto `1` del encargo mas la `TAREA 2` de su punto `2`, mas el registro de apertura que abre el reporte antes de la primera (`EXTRACTOR.md` 3).

## G9.1. TAREA 1: LOS REGISTROS DE APERTURA

### G9.1.a. Credito medido al abrir

Salida de `python forja.py credito`, guardada en `.gerber_v9/credito_apertura.txt`:

<!-- TALLADO: salida=.gerber_v9/credito_apertura.txt -->

    CREDITO DE LA LINEA 'gerber_emyth' (D.48)
      registro: docs/loop/CREDITO_gerber_emyth.jsonl
      tandas: 9, en 37 suceso(s) de especie

      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA G8
      CIFRA PUBLICADA    0 de 2     ACTA G8
      CLASE              0 de 2     ACTA G8
      DATO MOVIDO        0 de 2     ACTA G8
      REPORTE            0 de 3     ACTA G8

      CREDITO ENTERO: ninguna especie en su tope.

**LAS CINCO ESPECIES SIGUEN EN `0`, TAL COMO `ACTA G8` LAS DEJO.** Esta es, tal como el
encargo lo dice en su seccion `6`, la ultima oportunidad de esta linea de dejarlas asi: no
las toco yo (`G9.6.i` mide el cierre), pero las cinco parten en `0`.

### G9.1.b. Deuda medida al abrir

Salida de `python scripts/deuda.py`, guardada en `.gerber_v9/deuda_apertura.txt`:

<!-- TALLADO: salida=.gerber_v9/deuda_apertura.txt -->

    DEUDA DE LA LINEA (D.55): la deuda no bloquea la produccion
      registro: docs/loop/DEUDA.jsonl
      pendientes: 49    pagadas: 39

Salida de `python scripts/deuda.py --clase 9`, guardada en `.gerber_v9/clase9.txt`:

<!-- TALLADO: salida=.gerber_v9/clase9.txt -->

    LIBRE
      van 3 de 5 desde la ultima de saneamiento (la 6), con 49 deuda(s) esperando

**`49` PENDIENTES, NO LAS `44` CON LAS QUE CERRO `G8`.** La diferencia es `5` deuda(s)
nuevas: `d128` a `d132`, las cinco anotadas en la vuelta `8` con cita `ACTA G8` (visibles en
la propia salida de `deuda.py` de esta vuelta), ajenas a este reporte. **Sin discrepancia
que declarar**: el instrumento manda y la cifra de hoy no es la de `G8.6.f` porque algo se
movio entre medias, no porque yo la mida distinto.

## G9.2. `cap_01`, `Foreword`

### G9.2.a. El borde de arriba, comparado contra `wc -l` y `wc -w` (`d109`, la guarda que no lo cubre)

    $ wc -l fuentes/gerber_emyth/cap_01.md
    71 fuentes/gerber_emyth/cap_01.md
    $ wc -w fuentes/gerber_emyth/cap_01.md
    1434 fuentes/gerber_emyth/cap_01.md

**`71` LINEAS, AL DIGITO CON EL BORDE DE LA ULTIMA PIEZA DE LA FRONTERA (abajo). `1434`
PALABRAS DEL FICHERO ENTERO, AL DIGITO CON LAS `1434` QUE EL ENCARGO CUENTA EN SU CABECERA.**

### G9.2.b. La frontera, publicada antes de cortar

Salida de `python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_01.md .gerber_v9/piezas_cap01.txt`,
guardada en `.gerber_v9/frontera_cap01.txt`:

<!-- TALLADO: salida=.gerber_v9/frontera_cap01.txt -->

    AVISO: cero celdas tecleadas en este instrumento. El arranque del cuerpo NO
    es una constante mia: sale de fuentes/gerber_emyth/cap_01.md, linea 8, que es la siguiente al segundo
    --- de la cabecera yaml (cierres en L1 y L7). El cuerpo va de L8 a L71.

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L10 | **1** | el rotulo FOREWORD | **RESIDUO: rotulo** |
| `R2` | L11 a L66 | **1393** | el prefacio del autor a la edicion revisada: quince anios desde The E-Myth original, su vida personal (familia, matrimonio, nietos), la pregunta de que saben los duenos de negocios extraordinarios, la insistencia en la atencion a los detalles pequenos hechos exactamente bien, y la presentacion de Sarah como interlocutora del libro; cero pasos, cero medio nombrado, cero inventario de etapas u objetos | **POSTURA: prefacio personal, sin inventario propio** |
| `R3` | L67 a L71 | **8** | la firma: Michael E. Gerber, Santa Rosa California, junio 2001 | **RESIDUO: firma** |
| **el cuerpo entero** | **L8 a L71** | **1402** | **suma de las piezas: 1402** | **residuo sin asignar: 0** |

    piezas: 3   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 1402   suma 1402   residuo 0

**`1402` PALABRAS DE CUERPO (sin la cabecera yaml, que trae `32` palabras propias: `1402` +
`32` = `1434`, al digito con `wc -w` del fichero entero). `3` PIEZAS, `0` SOLAPES, `0`
LINEAS SIN CUBRIR, RESIDUO `0`.** Fichero completo en `.gerber_v9/piezas_cap01.txt` (D.42).

### G9.2.c. La vara de `9.1`, pasada sobre las tres piezas, y el veredicto: cero candidatos

`R1` es rotulo, `R3` es firma: ninguna trae procedimiento. `R2`, el prefacio entero, es la
pieza que la vara tiene que leer con cuidado: quince anios de vida personal del autor (su
familia, sus nietos, sus viajes), la pregunta retorica de que saben los duenos de negocios
extraordinarios, y la tesis de que las cosas pequenas hechas exactamente bien son lo que
distingue un negocio grande. Leida contra la vara madre (seccion `9`: **NOMBRAR NO ES
PROCEDIMENTAR**) y su prueba del inventario (`9.1`, `D.27`): **el prefacio no pone un solo
inventario propio de medios, etapas u objetos de trabajo.** No hay una lista de que
atender, no hay una secuencia de pasos, no hay un conjunto de cosas por revisar: es memoria
y reflexion, cerrando con la presentacion de Sarah como la interlocutora del libro que
vendra despues.

**VEREDICTO: `cap_01` SE REGISTRA MINADO CON CERO CANDIDATOS.** Es el Foreword de la
edicion revisada: prefacio personal del autor, sin inventario propio que la vara de `9.1`
pueda transcribir. **Cero candidatos con su razon escrita es un resultado, no un hueco**
(tal como el encargo lo anticipa en su seccion `1.a`).

### G9.2.d. Discutibles

**Ninguno.** Leida la unica pieza con forma de cuerpo (`R2`) contra la vara madre y su
prueba del inventario, no hay una sola lista o secuencia nombrada en todo el capitulo: es
memoria en primera persona sin un solo verbo en imperativo dirigido al lector. No abro
discutible sobre `cap_01`.

## G9.3. `cap_02`, `Introduction`

### G9.3.a. El borde de arriba, comparado contra `wc -l` y `wc -w`

    $ wc -l fuentes/gerber_emyth/cap_02.md
    99 fuentes/gerber_emyth/cap_02.md
    $ wc -w fuentes/gerber_emyth/cap_02.md
    1244 fuentes/gerber_emyth/cap_02.md

**`99` LINEAS, AL DIGITO CON EL BORDE DE LA ULTIMA PIEZA DE LA FRONTERA. `1244` PALABRAS DEL
FICHERO ENTERO, AL DIGITO CON LAS `1244` QUE EL ENCARGO CUENTA EN SU CABECERA.**

### G9.3.b. La frontera, publicada antes de cortar

Salida de `python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_02.md .gerber_v9/piezas_cap02.txt`,
guardada en `.gerber_v9/frontera_cap02.txt`:

<!-- TALLADO: salida=.gerber_v9/frontera_cap02.txt -->

    AVISO: cero celdas tecleadas en este instrumento. El arranque del cuerpo NO
    es una constante mia: sale de fuentes/gerber_emyth/cap_02.md, linea 8, que es la siguiente al segundo
    --- de la cabecera yaml (cierres en L1 y L7). El cuerpo va de L8 a L99.

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L10 | **1** | el rotulo INTRODUCTION | **RESIDUO: rotulo** |
| `R2` | L11 a L16 | **17** | el epigrafe de Joseph Heller (Something Happened), sobre alguien enloqueciendo despacio dentro de todo negocio | **RESIDUO: epigrafe** |
| `R3` | L17 a L94 | **1183** | la introduccion del libro: la estadistica de fracaso de los pequenos negocios en Estados Unidos, el anuncio de las cuatro ideas del libro (Idea 1 el E-Myth, Idea 2 la Turn-Key Revolution, Idea 3 el Business Development Process, Idea 4 su aplicacion sistematica), y la tesis de que el negocio es un reflejo de quien es su dueno; las cuatro ideas se nombran como el CONTENIDO del libro entero, no como pasos que el lector ejecute aqui, y no traen inventario propio de medios, etapas u objetos de trabajo en este tramo | **POSTURA: anuncio tematico del libro, metas nombradas sin inventario de medios** |
| `R4` | L95 a L99 | **11** | el separador PART I, The E-Myth and American Small Business | **RESIDUO: separador de parte** |
| **el cuerpo entero** | **L8 a L99** | **1212** | **suma de las piezas: 1212** | **residuo sin asignar: 0** |

    piezas: 4   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 1212   suma 1212   residuo 0

**`1212` PALABRAS DE CUERPO (mas `32` de la cabecera yaml: `1212` + `32` = `1244`, al digito
con `wc -w` del fichero entero). `4` PIEZAS, `0` SOLAPES, `0` LINEAS SIN CUBRIR, RESIDUO
`0`.** Fichero completo en `.gerber_v9/piezas_cap02.txt` (D.42).

### G9.3.c. La vara de `9.1`, pasada sobre las cuatro piezas, y el veredicto: cero candidatos

`R1` es rotulo, `R2` es epigrafe, `R4` es separador de parte: ninguna trae procedimiento.

`R3` es el tramo que compite: anuncia las **cuatro ideas** del libro, cada una con su
propio parrafo (`IDEA #1` a `IDEA #4`). Comprobado contra `D.37` (la serie que el titulo
enumera se cablea en la misma vuelta en que nace su cabeza): **las cuatro ideas no son un
inventario de medios, etapas u objetos de trabajo, son las CUATRO TESIS del libro entero**
(que existe el mito del emprendedor, que hay una revolucion Turn-Key en marcha, que el
Business Development Process es su motor, y que ese proceso se aplica de forma
sistematica). Es la restriccion `1` de `9.1` al digito: **un inventario de METAS o de FINES
no cuenta, nombrar adonde hay que llegar sigue siendo nombrar.** Las cuatro ideas anuncian
DE QUE va el libro, no COMO se ejecuta nada aqui; su despliegue en procedimiento (Primary
Aim, Strategic Objective, Organizational Strategy, People Strategy, Systems Strategy, y los
capitulos de Innovacion, Cuantificacion y Orquestacion) ya vive, capitulo a capitulo, en los
candidatos minados de `cap_04` en adelante. Declarar aqui una cabeza de serie con estas
cuatro ideas fabricaria una cabeza que el propio libro no usa como tal: no hay una unica
lectura donde una IDEA se corresponda uno a uno con una PARTE nombrada por su numero (a
diferencia de `d098` y `d104`, donde el libro nombra tres o tres fases EXACTAS que luego
son un capitulo cada una). **No abre puntero `D.37` nuevo.**

**VEREDICTO: `cap_02` SE REGISTRA MINADO CON CERO CANDIDATOS.** Es la Introduction del
libro: la estadistica de fracaso, el anuncio de las cuatro ideas rectoras y la tesis del
negocio como reflejo del dueno, ninguna con inventario propio bajo `9.1`. **Cero candidatos
con su razon escrita.**

### G9.3.d. Discutibles

**Ninguno.** El unico tramo que podria competir (las cuatro ideas de `R3`) se resuelve sin
ambiguedad contra la restriccion `1` de `9.1`: son metas y fines del libro entero, no un
inventario de medios que el lector ejecute en este tramo. No abro discutible sobre `cap_02`.

## G9.4. `cap_03`, `Cap. 1`, `The Entrepreneurial Myth`

### G9.4.a. El borde de arriba, comparado contra `wc -l` y `wc -w`

    $ wc -l fuentes/gerber_emyth/cap_03.md
    233 fuentes/gerber_emyth/cap_03.md
    $ wc -w fuentes/gerber_emyth/cap_03.md
    2237 fuentes/gerber_emyth/cap_03.md

**`233` LINEAS, AL DIGITO CON EL BORDE DE LA ULTIMA PIEZA DE LA FRONTERA. `2237` PALABRAS
DEL FICHERO ENTERO, AL DIGITO CON LAS `2237` QUE EL ENCARGO CUENTA EN SU CABECERA.**

### G9.4.b. La frontera, publicada antes de cortar

Salida de `python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_03.md .gerber_v9/piezas_cap03.txt`,
guardada en `.gerber_v9/frontera_cap03.txt`:

<!-- TALLADO: salida=.gerber_v9/frontera_cap03.txt -->

    AVISO: cero celdas tecleadas en este instrumento. El arranque del cuerpo NO
    es una constante mia: sale de fuentes/gerber_emyth/cap_03.md, linea 8, que es la siguiente al segundo
    --- de la cabecera yaml (cierres en L1 y L7). El cuerpo va de L8 a L233.

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L18 | **22** | el numero del capitulo, el separador, el titulo THE ENTREPRENEURIAL MYTH y el epigrafe de Aldous Huxley sobre embriagarse de trabajo para no verse como se es | **RESIDUO: rotulo y epigrafe** |
| `R2` | L19 a L60 | **332** | el mito del emprendedor: la imagen heroica del emprendedor, y como en la experiencia del autor esa persona real casi nunca se sostiene, sino que el emprendedor solo existio un instante fugaz y luego desaparecio, dejando una mala interpretacion de quien empieza negocios y por que; cero pasos, cero inventario propio | **POSTURA: diagnostico del mito, sin inventario propio** |
| `R3` | L61 a L102 | **400** | The Entrepreneurial Seizure: describe, en segunda persona, el momento en que un tecnico que trabaja para otro sufre un ataque de fiebre emprendedora y decide independizarse; es narracion de un proceso psicologico que le ocurre al lector, no una lista de pasos que el lector ejecute ni un inventario de medios, etapas u objetos de trabajo | **POSTURA: narracion del ataque emprendedor, sin inventario propio** |
| `R4` | L103 a L150 | **387** | The Fatal Assumption: expone la Fatal Assumption (creer que saber el trabajo tecnico de un negocio es saber dirigir un negocio que hace ese trabajo) y enumera oficios (carpintero, barbero, redactor tecnico, peluquera, ingeniero, musico) que se convierten en negocios bajo esa falacia; los oficios listados son EJEMPLOS del diagnostico, no un inventario de medios o etapas de un procedimiento que el lector ejecute | **POSTURA: diagnostico de la Fatal Assumption, ejemplos sin procedimiento** |
| `R5` | L151 a L233 | **1061** | la historia de Sarah y su negocio All About Pies: el relato de su jornada de tres de la manana a las nueve o diez de la noche, su llanto, el origen de su amor por hornear con su tia, y el cierre en que el autor le dice que es hora de aprender todo sobre pies otra vez; en L225 nombra cuatro etapas (exhilaration, terror, exhaustion, despair) que todo tecnico con Entrepreneurial Seizure experimenta, pero son etapas de una experiencia psicologica narrada en tercera persona, no medios, etapas u objetos de trabajo que el lector deba revisar o ejecutar; cero inventario propio procedimental | **POSTURA: caso narrado de Sarah, con etapas de experiencia y no de procedimiento** |
| **el cuerpo entero** | **L8 a L233** | **2202** | **suma de las piezas: 2202** | **residuo sin asignar: 0** |

    piezas: 5   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 2202   suma 2202   residuo 0

**`2202` PALABRAS DE CUERPO (mas `35` de la cabecera yaml: `2202` + `35` = `2237`, al digito
con `wc -w` del fichero entero). `5` PIEZAS, `0` SOLAPES, `0` LINEAS SIN CUBRIR, RESIDUO
`0`.** Fichero completo en `.gerber_v9/piezas_cap03.txt` (D.42).

### G9.4.c. La vara de `9.1`, pasada sobre las cinco piezas, y el veredicto: cero candidatos

`R1` es rotulo y epigrafe. `R2` (el mito), `R3` (la Entrepreneurial Seizure) y `R4` (la
Fatal Assumption) son diagnostico en segunda y tercera persona: describen algo que le
OCURRE al lector o a los tecnicos en general (un ataque, una asuncion fatal), no una lista
de medios, etapas u objetos de trabajo que el lector deba revisar o ejecutar. Los seis
oficios de `R4` (carpintero, barbero, redactor tecnico, peluquera, ingeniero, musico) son
EJEMPLOS del diagnostico ilustrando la misma falacia, no un inventario de pasos.

`R5`, la historia de Sarah, es el tramo que merece la lectura mas cuidadosa: es narrativa
de caso (manual seccion `3.5`, "el caso no es la casa"), y trae en `L225` la frase **"First,
exhilaration; second, terror; third, exhaustion; and, finally, despair"**. Cita, con su
`sed` pegado (`D.35`), guardada en `.gerber_v9/cita_cap03_L225.txt`:

<!-- TALLADO: salida=.gerber_v9/cita_cap03_L225.txt -->

    225:First, exhilaration; second, terror; third, exhaustion; and, finally, despair. A terrible sense of loss-not only the loss of what was closest to them, their special relationship with their work, but the loss of purpose, the loss of self.

Leida contra la vara madre (seccion `9`) y la prueba del inventario (`9.1`, `D.27`): estas
cuatro palabras nombran **etapas de una experiencia psicologica que el tecnico sufre**
("every technician suffering from an Entrepreneurial Seizure experiences exactly the same
thing"), narradas en tercera persona sin un solo verbo en imperativo dirigido al lector. No
son medios, etapas u objetos de trabajo que alguien revise: son un diagnostico clinico de
lo que le pasa a quien atraviesa el Entrepreneurial Seizure, la misma figura que `R2`, `R3`
y `R4` ya establecieron para todo el capitulo. El cierre del capitulo, "You take this one
step at a time" (`L231`), es una unica advertencia (manual seccion `4`, `P.11`: una
advertencia es linea, no procedimiento) que remite al capitulo siguiente sin desplegar ella
misma ningun paso. **No abre candidato ni puntero nuevo.**

**VEREDICTO: `cap_03` SE REGISTRA MINADO CON CERO CANDIDATOS.** Es el primer capitulo del
libro (`The Entrepreneurial Myth`): el diagnostico del mito del emprendedor, la
Entrepreneurial Seizure, la Fatal Assumption y el caso de Sarah, sin un solo tramo con
inventario propio de medios, etapas u objetos de trabajo bajo `9.1`. **Cero candidatos con
su razon escrita.**

### G9.4.d. Discutibles

**Ninguno.** El unico tramo que se acerco a competir (las cuatro etapas de `L225`) se
resuelve sin ambiguedad: son un diagnostico narrado en tercera persona, sin un solo verbo en
imperativo, mas debil incluso que el discutible de `cap_22` `Rb` de la vuelta `8`
(`G8.4.c`), que si traia cuatro imperativos explicitos ("you must") y aun asi se cerro
`SANO`. No abro discutible sobre `cap_03`.

### G9.4.e. `PASOS INVENTADOS POR CAPITULO`, los tres capitulos de esta vuelta (`AUDITOR_FORJA.md` 8)

Los tres capitulos de esta vuelta cerraron con **cero candidatos** (`G9.2`, `G9.3`, `G9.4`),
asi que no hay pasos escritos que medir: no es que la fidelidad haya fallado, es que no hay
ficha de la que medirla.

<!-- TALLADO: parcial salida=.gerber_v9/muestra_fidelidad.txt -->

| capitulo | candidatos nuevos (esta vuelta) | pasos escritos | PUENTE | pasos inventados |
|---|---:|---:|---:|---:|
| `cap_01` | `0` | `0` | `0` | **sin poblacion que medir** |
| `cap_02` | `0` | `0` | `0` | **sin poblacion que medir** |
| `cap_03` | `0` | `0` | `0` | **sin poblacion que medir** |
| **el lote entero** | **`0`** | **`0`** | **`0`** | **sin poblacion que medir** |

**`8.2` de `AUDITOR_FORJA.md`: la escalada se decide sobre el peor capitulo, y aqui no hay
ninguno que escale: los tres estan en la misma poblacion vacia.**

### G9.4.f. La muestra de fidelidad con su semilla escrita (`D.58`, regimen ligero)

Salida de
`python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_01,cap_02,cap_03 --semilla g9`,
guardada en `.gerber_v9/muestra_fidelidad.txt`:

<!-- TALLADO: salida=.gerber_v9/muestra_fidelidad.txt -->

    MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO (D.58)
      libro    : gerber_emyth
      semilla  : g9
      capitulos: cap_01, cap_02, cap_03

      RELEIDO ENTERO : cap_02
      POR MUESTRA    : cap_01, cap_03, 15 pasos cada uno

      EL DISPARADOR: si la muestra de un capitulo pasa del 10 por ciento de
      pasos inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.

      --- cap_01: 0 paso(s) en la muestra

      --- cap_03: 0 paso(s) en la muestra

      --- cap_02: ENTERO, 0 paso(s), no hay muestra que elegir

**LA SEMILLA `g9` REPARTE `cap_02` ENTERO Y `cap_01`/`cap_03` POR MUESTRA, PERO LOS TRES DAN
`0` PASOS: NO HAY CANDIDATOS DE LOS QUE MUESTREAR.** El disparador del `10` por ciento no
tiene sobre que dispararse (`0` de `0` no es una fraccion). **NO SE DISPARA NADA, PORQUE NO
HAY NADA QUE DISPARAR.**

## G9.5. TAREA 2: CERRAR `d094` Y LA FRONTERA DEL LIBRO COMPLETA

### G9.5.a. `d094` pagada

Salida de
`python scripts/deuda.py --pagar d094 --vuelta 9 --como "vuelta 9 lee cap_01, cap_02 y cap_03 enteros de gerber_emyth (leyendo cero candidatos con razon escrita en cada uno) y cierra el hueco declarado en d094"`,
guardada en `.gerber_v9/pago_d094.txt`:

<!-- TALLADO: salida=.gerber_v9/pago_d094.txt -->

    PAGADA d094 en la vuelta 9

**`d094` QUEDA PAGADA.** Nacio en la vuelta `2` para anotar que `cap_01` a `cap_03` seguian
sin minar por decision del fundador (`docs/loop/DEUDA.jsonl` linea `94`); esta vuelta los
lee enteros y cierra el hueco que anotaba.

### G9.5.b. La tabla del libro entero, `cap_01` a `cap_22`, con su estado y su firma

**ES LO QUE SE LLEVA LA COSECHA** (encargo, seccion `2`): fundida de tres fuentes medidas
hoy, `docs/loop/TABLERO.jsonl` (grafo mas bandejas), `config/frentes.json` (los capitulos
ya firmados en cero por un acta del auditor) y `cuarentena/gerber_emyth/*.json` (los
candidatos por su `UNIDAD DE ORIGEN`). Salida de `python .gerber_v9/tabla_libro.py`,
guardada en `.gerber_v9/tabla_libro.txt`:

<!-- TALLADO: salida=.gerber_v9/tabla_libro.txt -->

    | capitulo | estado | candidatos | firma |
    |---|---|---:|---|
    | `cap_01` | MINADO EN CERO | 0 | vuelta 9, este reporte (G9.2/G9.3/G9.4), sin acta todavia |
    | `cap_02` | MINADO EN CERO | 0 | vuelta 9, este reporte (G9.2/G9.3/G9.4), sin acta todavia |
    | `cap_03` | MINADO EN CERO | 0 | vuelta 9, este reporte (G9.2/G9.3/G9.4), sin acta todavia |
    | `cap_04` | MINADO CON CANDIDATOS | 1 | TABLERO.jsonl, grafo+bandejas |
    | `cap_05` | MINADO EN CERO | 0 | ACTA G2 (cap_05 y cap_06), ACTA G3 3.5 (cap_09 y cap_10), ACTA G5 (cap_16 y cap_17, SIN SUPERFICIE con su razon leida) y ACTA G8 3.2 (cap_20 la carta a Sarah mas los agradecimientos, cap_21 el Epilogue, cap_22 el Afterword mas el back matter). Frente gerber_emyth, rama extraccion-gerber_emyth |
    | `cap_06` | MINADO EN CERO | 0 | ACTA G2 (cap_05 y cap_06), ACTA G3 3.5 (cap_09 y cap_10), ACTA G5 (cap_16 y cap_17, SIN SUPERFICIE con su razon leida) y ACTA G8 3.2 (cap_20 la carta a Sarah mas los agradecimientos, cap_21 el Epilogue, cap_22 el Afterword mas el back matter). Frente gerber_emyth, rama extraccion-gerber_emyth |
    | `cap_07` | MINADO CON CANDIDATOS | 1 | TABLERO.jsonl, grafo+bandejas |
    | `cap_08` | MINADO CON CANDIDATOS | 2 | TABLERO.jsonl, grafo+bandejas |
    | `cap_09` | MINADO EN CERO | 0 | ACTA G2 (cap_05 y cap_06), ACTA G3 3.5 (cap_09 y cap_10), ACTA G5 (cap_16 y cap_17, SIN SUPERFICIE con su razon leida) y ACTA G8 3.2 (cap_20 la carta a Sarah mas los agradecimientos, cap_21 el Epilogue, cap_22 el Afterword mas el back matter). Frente gerber_emyth, rama extraccion-gerber_emyth |
    | `cap_10` | MINADO EN CERO | 0 | ACTA G2 (cap_05 y cap_06), ACTA G3 3.5 (cap_09 y cap_10), ACTA G5 (cap_16 y cap_17, SIN SUPERFICIE con su razon leida) y ACTA G8 3.2 (cap_20 la carta a Sarah mas los agradecimientos, cap_21 el Epilogue, cap_22 el Afterword mas el back matter). Frente gerber_emyth, rama extraccion-gerber_emyth |
    | `cap_11` | MINADO CON CANDIDATOS | 6 | TABLERO.jsonl, grafo+bandejas |
    | `cap_12` | MINADO CON CANDIDATOS | 3 | TABLERO.jsonl, grafo+bandejas |
    | `cap_13` | MINADO CON CANDIDATOS | 1 | TABLERO.jsonl, grafo+bandejas |
    | `cap_14` | MINADO CON CANDIDATOS | 1 | TABLERO.jsonl, grafo+bandejas |
    | `cap_15` | MINADO CON CANDIDATOS | 1 | TABLERO.jsonl, grafo+bandejas |
    | `cap_16` | MINADO EN CERO | 0 | ACTA G2 (cap_05 y cap_06), ACTA G3 3.5 (cap_09 y cap_10), ACTA G5 (cap_16 y cap_17, SIN SUPERFICIE con su razon leida) y ACTA G8 3.2 (cap_20 la carta a Sarah mas los agradecimientos, cap_21 el Epilogue, cap_22 el Afterword mas el back matter). Frente gerber_emyth, rama extraccion-gerber_emyth |
    | `cap_17` | MINADO EN CERO | 0 | ACTA G2 (cap_05 y cap_06), ACTA G3 3.5 (cap_09 y cap_10), ACTA G5 (cap_16 y cap_17, SIN SUPERFICIE con su razon leida) y ACTA G8 3.2 (cap_20 la carta a Sarah mas los agradecimientos, cap_21 el Epilogue, cap_22 el Afterword mas el back matter). Frente gerber_emyth, rama extraccion-gerber_emyth |
    | `cap_18` | MINADO CON CANDIDATOS | 3 | TABLERO.jsonl, grafo+bandejas |
    | `cap_19` | MINADO CON CANDIDATOS | 3 | TABLERO.jsonl, grafo+bandejas |
    | `cap_20` | MINADO EN CERO | 0 | ACTA G2 (cap_05 y cap_06), ACTA G3 3.5 (cap_09 y cap_10), ACTA G5 (cap_16 y cap_17, SIN SUPERFICIE con su razon leida) y ACTA G8 3.2 (cap_20 la carta a Sarah mas los agradecimientos, cap_21 el Epilogue, cap_22 el Afterword mas el back matter). Frente gerber_emyth, rama extraccion-gerber_emyth |
    | `cap_21` | MINADO EN CERO | 0 | ACTA G2 (cap_05 y cap_06), ACTA G3 3.5 (cap_09 y cap_10), ACTA G5 (cap_16 y cap_17, SIN SUPERFICIE con su razon leida) y ACTA G8 3.2 (cap_20 la carta a Sarah mas los agradecimientos, cap_21 el Epilogue, cap_22 el Afterword mas el back matter). Frente gerber_emyth, rama extraccion-gerber_emyth |
    | `cap_22` | MINADO EN CERO | 0 | ACTA G2 (cap_05 y cap_06), ACTA G3 3.5 (cap_09 y cap_10), ACTA G5 (cap_16 y cap_17, SIN SUPERFICIE con su razon leida) y ACTA G8 3.2 (cap_20 la carta a Sarah mas los agradecimientos, cap_21 el Epilogue, cap_22 el Afterword mas el back matter). Frente gerber_emyth, rama extraccion-gerber_emyth |

    total capitulos: 22   minados: 22   candidatos en bandeja: 22

**`22` DE `22` UNIDADES MINADAS. `22` CANDIDATOS EN BANDEJA, AL DIGITO CON EL TABLERO Y CON
LA SECCION `3` DEL ENCARGO. EL LIBRO QUEDA ENTERO.** Las filas de `cap_01` a `cap_03` citan
`este reporte, sin acta todavia`: son mi veredicto de esta vuelta (`G9.2`, `G9.3`, `G9.4`),
no una firma de `config/frentes.json`, porque esa sede es del auditor (`EXTRACTOR.md` 14,
"la firma de un acta" segun la propia cabecera de `minados_en_cero`): **no la edito yo.**
Cuando el auditor audite esta vuelta y firme su acta, esas tres filas pasan a citar su
propia acta igual que las otras nueve.

### G9.5.c. Los cuatro punteros heredados, comprobados contra los tres capitulos de esta vuelta

**NO LOS DECLARO YO SI NO NACEN** (`EXTRACTOR.md` `15.6`: las aristas `D.37` se declaran en
la vuelta que INSERTA las partes, y esta vuelta no inserta). Lo que el encargo pide en su
seccion `4` es comprobarlos, y eso hago:

    d098   D.37, cap_05 L29, la terna sin cabeza (Infancy, Adolescence, Maturity)
    d104   D.37, cap_12 L21, la terna sin cabeza (Innovation, Quantification, Orchestration)
    d108   releer cap_14 L27 contra L117
    d111   la serie de cap_13, en 0 de 7, con su primera arista declarable ya identificada

**NINGUNO DE LOS CUATRO SE TOCA POR `cap_01`, `cap_02` NI `cap_03`.** Los tres capitulos de
esta vuelta son Foreword, Introduction y el primer capitulo del libro (el diagnostico del
mito del emprendedor): ninguno nombra las tres fases de crecimiento de `d098`, ninguno
nombra Innovation/Quantification/Orchestration de `d104`, ninguno toca `cap_14` ni `cap_17`
(`d108`, `d111`), y ninguno de los tres produjo un candidato nuevo que pudiera emparejarse
con alguna de las cuatro cabezas (`G9.2`, `G9.3`, `G9.4` cierran los tres en cero). **LOS
CUATRO PUNTEROS SIGUEN PUBLICADOS, SIN CAMBIO, PARA LA VUELTA QUE INSERTE.**
