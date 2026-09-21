---

# TAREA 3. `cap_06`, LA FRONTERA PUBLICADA ANTES DE CORTAR Y LOS DOS CANDIDATOS CON SU ADUANA EN SECO

## 3.a. La unidad que se mina

| | | de donde sale |
|---|---|---|
| fichero | `fuentes/marquet_turn_the_ship/cap_06.md` | encargo, seccion 2 |
| unidad que el fichero declara | Cap. 8 | `sed -n '4p' fuentes/marquet_turn_the_ship/cap_06.md` |
| titulo textual | *Change, in a Word* | `sed -n '5p' fuentes/marquet_turn_the_ship/cap_06.md` |
| lineas del fichero | 139 | `wc -l fuentes/marquet_turn_the_ship/cap_06.md` |
| palabras del fichero entero | 2936 | `wc -w fuentes/marquet_turn_the_ship/cap_06.md`, coincide con el encargo |
| cuerpo, desde `L8` | 2905 | `sed -n '8,$p' fuentes/marquet_turn_the_ship/cap_06.md \| wc -w` |

## 3.b. LA FRONTERA ENTERA, PIEZA A PIEZA

<!-- TALLADO: parcial salida=.m2/frontera_bruta.txt -->

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| R1 | L9 | 4 | rotulo del titulo *Change, in a Word* | RESIDUO: rotulo |
| R2 | L11 | 21 | pregunta de apertura sobre cambiar la autoridad de decision | POSTURA |
| R3 | L13 | 14 | fecha, sitio y cuenta atras al despliegue | RESIDUO: rotulo de fecha |
| R4 | L15 | 134 | escena: la vieja instalacion de periscopios, reunion con los jefes | CASO |
| R5 | L17 | 115 | por que empezar con los jefes y no con oficiales o marineria | CASO/POSTURA: decision propia de Marquet, no procedimiento generalizable |
| R6 | L19 | 52 | historial de sermones vacios sobre "trabajar juntos" | CASO |
| R7 | L21 | 49 | resuelto a actuar diferente primero; nombra de paso otro mecanismo de otro capitulo, sin desarrollarlo aqui | POSTURA |
| R8 | L23 | 115 | confianza y dudas sobre jefes especificos de Santa Fe | CASO |
| R9 | L25 | 57 | un suboficial decide quedarse | CASO |
| R10 | L27 | 31 | pregunta inicial a los jefes: dirigen los jefes la marina | CASO |
| R11 | L29 | 7 | responden reflexivamente que si | CASO |
| R12 | L31 | 1 | "de verdad?" | CASO |
| R13 | L33 | 25 | segunda ronda de respuestas, mirando al piso | CASO |
| R14 | L35 | 140 | analisis institucional de la erosion de autoridad de los jefes | POSTURA |
| R15 | L37 | 44 | estas practicas reforzaron el modelo de lider a seguidores | POSTURA |
| R16 | L39 | 105 | el programa procedimental alternativo del reactor, bien definido | POSTURA |
| R17 | L41 | 33 | el enfasis en el procedimiento puede ser sofocante | POSTURA |
| R18 | L43 | 85 | el enfoque procedimental es limitante en operaciones tacticas | POSTURA |
| R19 | L45 | 59 | revertir la erosion exige que los jefes decidan deliberadamente | CASO/POSTURA |
| R20 | L47 | 38 | los jefes escepticos: Santa Fe no habia tenido incidentes graves | CASO |
| R21 | L49 | 31 | quince anios en la marina, siempre habia sido asi | CASO |
| R22 | L51 | 19 | la siguiente pregunta se basa en lo ya acordado | CASO |
| R23 | L53 | 6 | "quieren dirigirla?" | CASO |
| R24 | L55 | 7 | responden reflexivamente que si | CASO |
| R25 | L57 | 1 | "de verdad?" | CASO |
| R26 | L59 | 17 | ahi empezaron a hablar honestamente | CASO |
| R27 | L61 | 10 | rotulo *Mechanism: Find the Genetic Code for Control and Rewrite It* | RESIDUO: rotulo de mecanismo |
| R28 | L63 | 12 | introduccion: aqui hay una lista de los problemas principales | CASO |
| R29 | L65 a L75 | 102 | los seis problemas de los jefes, nombrados uno a uno | CASO: sintomas propios de Santa Fe, no medios de un procedimiento generalizable |
| R30 | L77 | 72 | hablamos de la realidad de ser responsables de sus divisiones | CASO |
| R31 | L79 | 83 | el entusiasmo de los jefes decayo | CASO |
| R32 | L81 | 65 | acordamos que el resultado serian mecanismos concretos; la pregunta clave a los jefes | CASO |
| R33 | L83 | 76 | primero y principal, los jefes querian estar a cargo de las licencias de sus hombres | CASO |
| R34 | L85 | 92 | la solucion que propusieron los jefes: el cambio de una palabra, de XO a COB | CASO: origen narrativo del ejercicio P1, no nodo propio |
| R35 | L87 | 98 | las dudas de Marquet para aceptar el cambio | CASO |
| R36 | L89 | 50 | acordado; el cambio se hizo esa misma tarde | CASO |
| R37 | L91 | 95 | el alcance del cambio: "Chiefs in Charge" sobre licencias, guardias y calificaciones | CASO |
| R38 | L93 | 70 | delegacion simetrica: Marquet delega las licencias de oficiales en el XO | CASO |
| R39 | L95 | 48 | la preocupacion no era la autoridad sino el comportamiento | CASO |
| R40 | L97 | 7 | subrotulo *Find Your Organization's Genetic Code for Control* | RESIDUO: rotulo |
| **P1** | **L99 a L113** | **208** | **NODO: el ejercicio de retiro para hallar y reescribir el codigo genetico del control, en seis etapas mas su lectura de cierre** | **NODO** |
| R41 | L115 | 3 | separador de seccion | RESIDUO: separador |
| R42 | L117 | 60 | cierre "is a mechanism for CONTROL" y explicacion general de delegar control | POSTURA |
| R43 | L119 | 77 | la claridad organizacional como barrera, no la dificultad tecnica | POSTURA |
| R44 | L121 | 82 | los programas de empoderamiento dirigido son contradictorios | POSTURA |
| R45 | L123 | 88 | sintesis: se buscaron practicas y procedimientos, no discursos | POSTURA |
| R46 | L125 | 3 | separador de seccion | RESIDUO: separador |
| **P2** | **L127** | **144** | **NODO: anadir la linea "jefe a cargo" a cada evento del documento de planificacion** | **NODO, ver DISCUTIBLE 3** |
| R47 | L129 | 74 | transicion: distribuir control no basta, exige mas competencia y claridad | POSTURA |
| R48 | L131 | 3 | rotulo QUESTIONS TO CONSIDER | RESIDUO: rotulo |
| R49 | L133 a L139 | 73 | las cuatro preguntas de cierre del capitulo | PENDIENTE DE DOCTRINA, vuelta 25 |
| **el cuerpo entero** | **L8 a L139** | **2905** | **suma de las piezas: 2905** | **residuo sin asignar: 0** |

    piezas: 49   lineas solapadas: 0   cuerpo 2905   suma 2905   residuo 0   lineas con palabras sin cubrir: 0

**LA FRONTERA CIERRA AL DIGITO: cuerpo `2905`, suma de piezas `2905`, residuo `0`, cero solapes y cero
lineas con palabras sin cubrir.** Dos piezas se minan, `P1` y `P2`; las otras 47 son residuo, postura o caso.

## 3.c. LA CITA DE LAS PIEZAS QUE SE MINAN, CON SU `sed` PEGADO (`D.35`)

<!-- TALLADO: parcial salida=.m2/citas_nodos.txt -->

| pieza | linea | la salida de `sed`, pegada | veredicto |
|---|---|---|---|
| P1 | L99 | `Here's an exercise you can do with your senior leadership at your next off-site.` | NODO, cabecera del ejercicio |
| P1 | L101 | `Identify in the organization's policy documents where decision-making authority is specified. (You can do this ahead of time if you want.)` | NODO, paso 1 |
| P1 | L103 | `Identify decisions that are candidates for being pushed to the next lower level in the organization.` | NODO, paso 2 |
| P1 | L105 | `For the easiest decisions, first draft language that changes the person who will have decision-making authority. In some cases, large decisions may need to ...` | NODO, paso 3 |
| P1 | L107 | `Next, ask each participant in the group to complete the following sentence on the five-by-eight card provided: "When I think about delegating this decisio...` | NODO, paso 4 |
| P1 | L109 | `Post those cards on the wall, go on a long break, and let the group mill around the comments posted on the wall.` | NODO, paso 5 |
| P1 | L111 | `Last, when the group reconvenes, sort and rank the worries and begin to attack them.` | NODO, paso 6 |
| P1 | L113 | `When I've conducted this exercise, I usually find that the worries fall into two broad categories: issues of competence and issues of clarity. People are w...` | NODO, paso 7 |
| P2 | L127 | `We expanded the power of the chiefs several times during the three years I was on Santa Fe. We started with giving them control over their men's leave. The...` | NODO |

## 3.d. POR QUE `P1` ES PROCEDIMIENTO: LA PRUEBA DEL INVENTARIO

El rotulo `L97` ("Find Your Organization's Genetic Code for Control") y `L99` ("Here's an exercise you
can do") llaman a esto un ejercicio por su nombre, y el propio texto pone **SEIS etapas nombradas una a
una y en orden** (identificar donde vive la autoridad, identificar las decisiones candidatas, redactar
el lenguaje, pedir la tarjeta de preocupaciones, pegarlas en la pared, ordenar y atacarlas), sin ningun
adjetivo de adecuacion en el sitio del criterio: cada etapa dice que hacer, no que tan bien hacerlo. Es
el caso limpio de `D.27`: inventario propio de etapas, restriccion 1 y 2 las dos a favor.

**EL CASO PREVIO (`R34`, `L85`, el cambio de una palabra de XO a COB) ENTRA COMO EJEMPLO DENTRO DE LA
DOCTRINA Y NO COMO NODO PROPIO** (manual 3.5): es de donde el autor generalizo el ejercicio, pero el
ejercicio mismo (`L97` a `L113`) no lleva el nombre de Santa Fe ni de ningun cargo de esa nave, y el
entregable del candidato tampoco.

## 3.e. EL DISCUTIBLE 3, MARCADO ANTES DE SABER SI ACIERTO

**`P2` (`L127`) tiene solo DOS pasos y ningun inventario nombrado uno a uno**: una accion (anadir la
linea "jefe a cargo") y su razon (senalar quien responde pesa mas que enumerar como podria fallar el
evento). A diferencia de `P1`, aqui no hay lista de etapas; hay una sola tecnica con su porque. La vara
madre (`EXTRACTOR.md` 9) no exige inventario para narrativa de negocio como exige `D.27` para material
normativo: solo pide que el paso sea ejecutable y que el libro lo diga, y las dos condiciones se cumplen
al pie de la letra. **Lo sostengo como nodo porque pasa la aduana y la relectura de fidelidad da 0
puentes, pero el margen es mas estrecho que el de `P1` y lo marco para que se relea primero.**

## 3.f. LOS DOS CANDIDATOS, ESCRITOS Y PASADOS POR LA ADUANA EN SECO EN EL MISMO ACTO

Los dos llevan `UNIDAD DE ORIGEN: fuentes/marquet_turn_the_ship/cap_06.md` en su `resumen_teorico`
(`D.58` 0.a).
