---

# TAREA 2. `cap_05`, LA FRONTERA PUBLICADA Y EL SALDO. CERRADA CON CERO CANDIDATOS

*`EXTRACTOR.md` 2.b: un capitulo que da cero se cierra igual, y se firma leyendo entero.*

## 2.a. La unidad que se mina

| | | de donde sale |
|---|---|---|
| fichero | `fuentes/marquet_turn_the_ship/cap_05.md` | encargo, seccion 2 |
| unidad que el fichero declara | Cap. 7 | `sed -n '4p' fuentes/marquet_turn_the_ship/cap_05.md` |
| titulo textual | *I Relieve You!* | `sed -n '5p' fuentes/marquet_turn_the_ship/cap_05.md` |
| lineas del fichero | 129 | `wc -l fuentes/marquet_turn_the_ship/cap_05.md` |
| palabras del fichero entero | 2223 | `wc -w fuentes/marquet_turn_the_ship/cap_05.md`, coincide con el encargo |
| cuerpo, desde `L8` | 2193 | `sed -n '8,$p' fuentes/marquet_turn_the_ship/cap_05.md \| wc -w` |

## 2.b. LA FRONTERA ENTERA, PIEZA A PIEZA

<!-- TALLADO: parcial salida=.m2/frontera_bruta.txt -->

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| R1 | L9 | 3 | rotulo del titulo | RESIDUO: rotulo |
| R2 | L11 | 15 | pregunta de apertura sobre evitar errores contra lograr la excelencia | POSTURA |
| R3 | L13 | 11 | fecha, sitio y cuenta atras al despliegue | RESIDUO: rotulo de fecha |
| R4 | L15 | 133 | asumir el mando, reflexion sobre la responsabilidad que empieza | CASO/POSTURA |
| R5 | L17 | 16 | introduccion a la cita del Reglamento de la Marina | CASO |
| R6 | L19 | 70 | cita literal de la Seccion 0802 sobre responsabilidad absoluta del comandante | CASO: norma externa citada, remite fuera del libro |
| R7 | L21 | 146 | reflexion sobre la delegacion como excepcion y el incentivo de un solo tour de mando | POSTURA |
| R8 | L23 | 23 | introduccion a la Seccion 0851 sobre comunicar el plan de batalla | CASO |
| R9 | L25 | 40 | cita literal de la orden de comunicar el plan antes de la accion | CASO: norma externa citada |
| R10 | L27 | 43 | reflexion sobre el "si es posible" de la orden | POSTURA |
| R11 | L29 | 44 | esas normas describen la estructura de lider a seguidores | POSTURA |
| R12 | L31 | 36 | transicion: sentado en el estrado, balance de lo que tenia a favor | CASO |
| R13 | L33 | 123 | "primero": la tripulacion queria el cambio | POSTURA, ver DISCUTIBLE 2 |
| R14 | L35 | 108 | "segundo": cadena de mando de apoyo | POSTURA, ver DISCUTIBLE 2 |
| R15 | L37 | 108 | "tercero": la dependencia de la tripulacion evito caer en viejos habitos | POSTURA, ver DISCUTIBLE 2 |
| R16 | L39 | 68 | "finalmente": la espiral descendente exigia romper el ciclo | POSTURA, ver DISCUTIBLE 2 |
| R17 | L41 | 7 | rotulo *Mechanism: Achieve Excellence, Don't Just Avoid Errors* | RESIDUO: rotulo de mecanismo |
| R18 | L43 | 71 | la cultura naval de enfocarse en errores | POSTURA |
| R19 | L45 | 77 | diagnostico: la tripulacion se volvio temerosa de errar | POSTURA |
| R20 | L47 | 99 | "estas destinado a fallar", reflexion sobre el error inevitable | POSTURA |
| R21 | L49 | 42 | evitar errores aleja de la excelencia | POSTURA |
| R22 | L51 | 29 | resolucion personal: la meta seria la excelencia | POSTURA |
| R23 | L53 | 87 | elaboracion de la meta de excelencia como forma de vida | POSTURA |
| R24 | L55 | 50 | transicion a la ceremonia de relevo | CASO |
| R25 | L57 | 18 | "I relieve you", toma del mando | CASO |
| R26 | L59 | 32 | introduccion al juramento personal | CASO |
| R27 | L61 | 21 | texto del juramento, primera parte | CASO |
| R28 | L63 | 26 | texto del juramento, segunda parte | CASO |
| R29 | L65 | 46 | texto del juramento, tercera parte | CASO |
| R30 | L67 | 12 | texto del juramento, cuarta parte | CASO |
| R31 | L69 | 2 | cierre del discurso a la tripulacion | CASO |
| R32 | L71 | 3 | "gracias" | CASO |
| R33 | L73 | 43 | se sento, reflexion sobre el despliegue en 172 dias | CASO |
| R34 | L75 | 3 | "estaba listo para trabajar" | CASO |
| R35 | L77 | 46 | ir al mar en submarino es trabajo duro y honorable | POSTURA |
| R36 | L79 | 54 | conectar las actividades diarias con algo mas grande | POSTURA |
| R37 | L81 | 81 | necesidad de que todos vieran el proposito ultimo del submarino | POSTURA |
| R38 | L83 | 21 | cierre *is a mechanism for CLARITY* y referencia a otro libro | RESIDUO: rotulo de cierre |
| R39 | L85 | 3 | rotulo QUESTIONS TO CONSIDER | RESIDUO: rotulo |
| R40 | L87 a L103 | 138 | las nueve preguntas de cierre del capitulo | PENDIENTE DE DOCTRINA, vuelta 25 |
| R41 | L105 a L107 | 3 | rotulo "PART II / CONTROL" | RESIDUO: rotulo de parte |
| R42 | L109 | 41 | el foco de Marquet: repartir el control y la autoridad de decision | POSTURA |
| R43 | L111 | 48 | el eslogan de mover la autoridad hacia la informacion, no la informacion hacia la autoridad | POSTURA |
| R44 | L113 | 48 | introduccion a los capitulos de la Parte II, agrupados en control, competencia y claridad | POSTURA |
| R45 | L115 a L129 | 55 | enumeracion de los ocho mecanismos de la Parte II (indice, sin desarrollo aqui) | RESIDUO: enumeracion, ver 2.d |
| **el cuerpo entero** | **L8 a L129** | **2193** | **suma de las piezas: 2193** | **residuo sin asignar: 0** |

    piezas: 45   lineas solapadas: 0   cuerpo 2193   suma 2193   residuo 0   lineas con palabras sin cubrir: 0

**LA FRONTERA CIERRA AL DIGITO: cuerpo `2193`, suma de piezas `2193`, residuo `0`, cero solapes y cero lineas
con palabras sin cubrir.** Cero piezas se minan.

## 2.c. POR QUE `Mechanism: Achieve Excellence, Don't Just Avoid Errors` NO DA NODO

El unico rotulo *Mechanism:* del capitulo (`R17`, `L41`) abre un tramo que corre hasta `R23` (`L53`) sin
un solo medio o etapa nombrado uno a uno: el mandato es cambiar el foco de evitar errores a lograr la
excelencia, y todo lo que sigue (`L43` a `L53`) es diagnostico y proposito, no un inventario de que hacer.
Por la vara madre (`EXTRACTOR.md` 9), **nombrar la meta no es procedentar el camino**: no hay adjetivo de
adecuacion que tumbe por `D.27` porque no hace falta, no hay ningun inventario que la restriccion 2 pudiera
tumbar. Es el mismo defecto que en `onu_consumidor` cap_03 parrafo 39 (*facilitar*, *mejorar* sin medios):
**una postura no ejecuta una busqueda.**

## 2.d. LOS DISCUTIBLES DE ESTE CAPITULO

**DISCUTIBLE 2**: `R13` a `R16` (*primero*, *segundo*, *tercero*, *finalmente*, `L33` a `L39`) forman una
serie ordinal explicita, pero se leen como condiciones favorables que Marquet encontro al asumir el mando
(la tripulacion queria cambiar, la cadena de mando apoyaba, su falta de conocimiento tecnico le impidio caer
en viejos habitos, la espiral descendente exigia romper el ciclo), **no como pasos que el lector ejecuta**.
No hay verbo en imperativo en ninguna de las cuatro, y las cuatro narran hechos pasados de la propia
experiencia del autor. **Se sostienen como POSTURA y no como SERIE NUMERADA** (manual 3.4): la serie
numerada exige que las partes sean medios o etapas de un trabajo, y aqui son condiciones observadas, no
etapas de un procedimiento. Lo marco porque el filo es real (la forma gramatical es la misma que una
serie de pasos) y quiero que se relea antes de sostenerlo como definitivo.

**Sobre `R45` (la enumeracion de los ocho mecanismos de la Parte II):** no cablea ninguna arista `D.37`
porque la regla exige que las partes **existan como nodos**, y hoy ninguno de los ocho existe: son
capitulos por delante de este tramo. Cuando alguno se mine, tocara revisar si esta lista los nombra con su
cuenta (ocho, uno a uno) para cablear entonces.

## 2.e. LOS TRES CASOS QUE EL MANUAL NOMBRA, contestados aunque salgan en negativo

| caso | veredicto | contra que se lee |
|---|---|---|
| SERIE NUMERADA (manual 3.4) | NO LA HAY, ver DISCUTIBLE 2 | `R13` a `R16` tienen la forma pero no el contenido de una serie de pasos; `R45` enumera mecanismos que aun no son nodos |
| CASO O ESTUDIO (manual 3.5) | NO LO HAY como doctrina propia | el capitulo entero es autobiografico (la ceremonia de relevo, el juramento) y no hay doctrina generica de la que el caso sea ejemplo |
| CIFRA DEL AUTOR (principios 5 y 8) | NO LA HAY | `172 dias al despliegue` y `$2.000 millones` (`L15`) son marcadores narrativos de fecha y presupuesto, no una tasa con banda; no se construye ningun nodo con ellos, asi que no entra ninguna atribucion |

## 2.f. LA MADRE POR LECTURA

Con cero candidatos no hay ninguna arista que declarar. Busque igual, por lectura, si algun paso de
`cap_03` o `cap_04` nombra el "Mechanism: Achieve Excellence" o el eslogan de mover la autoridad hacia la
informacion: ninguno lo hace. **Sin parentesco declarado.**

## 2.g. EL SALDO DE LA TAREA

| | |
|---|---:|
| unidades leidas (piezas) | **45** |
| procedimientos | **0** |
| postura/caso/residuo/pendiente | **45** |
| candidatos escritos en `cuarentena/marquet_turn_the_ship/` por esta tarea | **0** |
| discutibles marcados | **1** (seccion 2.d, sostenido) |

**CERO NODOS, CON SU RAZON ESCRITA ARRIBA, PIEZA A PIEZA.** El unico mecanismo formalmente rotulado del
capitulo no trae inventario, y la unica serie ordinal del capitulo narra condiciones, no pasos.
