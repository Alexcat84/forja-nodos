
## LL.4. TAREA 4. **LA FRONTERA DE `cap_05`, PUBLICADA ANTES DE MINAR NADA** (`EXTRACTOR.md` 10)

**`cap_04` cierra hoy en `LL.2.k`, asi que la vuelta 51 mina `cap_05`, y una tanda no empieza sin su
frontera delante.** Es la unidad `Cap. 4` del libro, `Meetings, The Medium of Managerial Work`. El
instrumento es el mismo que la vuelta 46 corrio sobre `cap_04` (`.v46/frontera.py`), con **mi**
lectura de `cap_05` dentro y con la tercera cifra de control que el encargo pide: **cero constantes
tecleadas que el fichero pueda dar**, la cabecera se localiza por el segundo guion triple y la cita
de cada fila la imprime el instrumento de la linea.

### LL.4.a. **LA COMPROBACION DE `cap_05`, QUE VA ANTES DE LA TABLA, CON SUS TRES CIFRAS DE CONTROL**

<!-- TALLADO: parcial script=.v50/frontera.py salida=.v50/frontera_cap_05.txt -->

    ==============================================================================
    1. LA COMPROBACION DE cap_05, ANTES DE SU TABLA
    ==============================================================================
    fichero                                : fuentes/grove_high_output/cap_05.md
    la cabecera acaba en la linea          : 7   (segundo guion triple, no tecleado)
    tramos de mi lectura                   : 46
    lineas con contenido tras la cabecera  : 84
    lineas NO cubiertas                    : 0  []
    SOLAPES                                : 0  []
    suma de las filas                      : 4962 palabras
    cuerpo medido aparte                   : 4962 palabras
    CARACTERES DE CUERPO                   : 29820 caracteres
    fichero entero, para cruzar con wc -w  : 4990 palabras
    IGUALES                                : True
    NODOS QUE MI FRONTERA DA EN ESTA UNIDAD, cap_05 Y SOLO cap_05: 26

**LAS TRES CIFRAS DE CONTROL QUE EL ENCARGO PIDE, JUNTAS Y EN UNA LINEA: `29.820` caracteres de
cuerpo, `0` lineas sin cubrir y `0` solapes.** Y la cuarta que esta tabla lleva siempre: **`4962`
de suma de filas contra `4962` de cuerpo medido aparte.**

**CIERRA AL DIGITO Y SE CRUZA CON `wc -w`:** `4962` de cuerpo mas `28` de cabecera son los `4990`
que `wc -w` da del fichero entero.

<!-- TALLADO: parcial salida=.v50/cruce_wc.txt -->

    $ wc -w fuentes/grove_high_output/cap_05.md
    4990 fuentes/grove_high_output/cap_05.md
    $ sed -n "1,7p" fuentes/grove_high_output/cap_05.md | wc -w
    28

### LL.4.b. `cap_05`, `Meetings, The Medium of Managerial Work`: **CUARENTA Y SEIS TRAMOS Y VEINTISEIS NODOS**

<!-- TALLADO: script=.v50/frontera.py salida=.v50/frontera_cap_05.txt -->
| tramo de cap_05 | palabras | nodos | que es, y por que | la salida, pegada |
|---|---:|---:|---|---|
| `L9 a L11` | 6 | **0** | P1  rotulos: el numero 4 y el titulo textual Meetings, The Medium of Managerial Work | `9:4` |
| `L13 a L13` | 85 | **0** | P2  la mala fama de la reunion, con Drucker y Whyte citados: POSTURA con cifras de otros autores | `13:Meetings have a bad name. One school of management thought consi` |
| `L15 a L15` | 114 | **0** | P3  la reunion es el medio por el que se hace el trabajo de mando: DEFINICION, no hay nada que ejecutar | `15:But there is another way to regard meetings. Earlier we said tha` |
| `L17 a L17` | 76 | **0** | P4  las DOS clases de reunion, de proceso y de mision: DEFINICION, nombra sin poner inventario de medios | `17:The two basic managerial roles produce two basic kinds of meetin` |
| `L19 a L19` | 2 | **0** | P5  rotulo de seccion Process-Oriented Meetings, sin cuerpo que extraer | `19:Process-Oriented Meetings` |
| `L21 a L21` | 124 | **1** | P6  INFUNDIR REGULARIDAD A LA REUNION DE PROCESO: sus medios nombrados uno a uno y el control de produccion | `21:To make the most of this kind of meeting, we should aim to infus` |
| `L23 a L23` | 18 | **1** | P7  CABEZA DE SERIE: las TRES clases de reunion de proceso, contadas y nombradas una a una | `23:At Intel we use three kinds of process-oriented meetings: the on` |
| `L25 a L25` | 1 | **0** | P8  rotulo ONE-ON-ONES, sin cuerpo que extraer | `25:ONE-ON-ONES` |
| `L27 a L29` | 264 | **0** | P9  que es el uno a uno y para que sirve, mas las clases privadas del autor: DEFINICION mas CASO | `27:At Intel, a one-on-one is a meeting between a supervisor and a s` |
| `L31 a L31` | 46 | **0** | P10 con quien se tiene: el autor acota DE QUE va a hablar, y acotar el alcance no es procedimentar | `31:Who should have a one-on-one? In some situations a supervisor sh` |
| `L33 a L35` | 187 | **1** | P11 CADA CUANTO: la madurez relevante para la tarea y la velocidad de cambio del area, con sus dos frecuencias | `33:How often should you have one-on-ones? Or put another way, how d` |
| `L37 a L39` | 195 | **1** | P12 CUANTO DURA Y DONDE: la hora como minimo y el area de trabajo del subordinado, con lo que alli se aprende | `37:How long should a one-on-one meeting last? There really is no an` |
| `L41 a L41` | 145 | **1** | P13 LA REUNION ES DEL SUBORDINADO: el guion que el prepara y el paseo por el material | `41:A key point about a one-on-one: It should be regarded as the sub` |
| `L43 a L43` | 134 | **1** | P14 QUE SE TRATA: los indicadores, lo ocurrido desde la ultima, el problema potencial y la intuicion | `43:What should be covered in a one-on-one? We can start with perfor` |
| `L45 a L47` | 134 | **1** | P15 EL PAPEL DEL SUPERVISOR y el principio de una pregunta mas, con la frase de Drucker dentro | `45:What is the role of the supervisor in a one-on-one? He should fa` |
| `L49 a L49` | 157 | **1** | P16 LAS PISTAS MECANICAS: las dos copias del guion, las notas, y lo que escribirlo simboliza | `49:I'd like to suggest some mechanical hints for effective one-on-o` |
| `L51 a L51` | 64 | **1** | P17 EL FICHERO DE ESPERA donde los dos acumulan lo importante y no urgente: la tanda aplicada al uno a uno | `51:A real time-saver is using a "hold" file where both the supervis` |
| `L53 a L53` | 117 | **1** | P18 LOS ASUNTOS DE CORAZON A CORAZON y la guardia contra el que se suelta al final de la reunion | `53:The supervisor should also encourage the discussion of heart-to-` |
| `L55 a L55` | 85 | **1** | P19 EL UNO A UNO POR TELEFONO A DISTANCIA: la preparacion que exige y el intercambio de notas despues | `55:Long-distance telephone one-on-ones have become necessary becaus` |
| `L57 a L57` | 74 | **1** | P20 PROGRAMAR EN CADENA: fijar el siguiente al terminar el que se tiene, para evitar la cancelacion | `57:One-on-ones should be scheduled on a rolling basis-setting up th` |
| `L59 a L59` | 105 | **0** | P21 la palanca del uno a uno, noventa minutos por ochenta horas: DEFINICION con su cuenta | `59:What is the leverage of the one-on-one? Let's say you have a one` |
| `L61 a L63` | 210 | **0** | P22 el uno a uno con el responsable de ventas de Intel: CASO del autor, manual 3.5 | `61:At the same time, the subordinate teaches the supervisor, and wh` |
| `L65 a L65` | 103 | **0** | P23 el uno a uno en casa con sus hijas: CASO del autor, y el propio libro lo llama digresion | `65:To digress a bit, I also think that one-on-ones at home can help` |
| `L67 a L67` | 2 | **0** | P24 rotulo STAFF MEETINGS, sin cuerpo que extraer | `67:STAFF MEETINGS` |
| `L69 a L73` | 284 | **0** | P25 que es la reunion de personal y para que sirve, mas su primer grupo de ingenieros: DEFINICION mas CASO | `69:A staff meeting is one in which a supervisor and all of his subo` |
| `L75 a L75` | 63 | **1** | P26 QUE SE TRATA EN LA REUNION DE PERSONAL: el criterio de mas de dos, y que hacer si degenera en dos | `75:What should be discussed at a staff meeting? Anything that affec` |
| `L77 a L77` | 115 | **1** | P27 CUANTO SE ESTRUCTURA: la agenda con antelacion y la sesion abierta, con lo que cabe en cada una | `77:How structured should the meeting be? A free-for-all brainstormi` |
| `L79 a L83` | 216 | **1** | P28 EL PAPEL DEL SUPERVISOR en la reunion de personal: moderador y facilitador, y nunca conferenciante | `79:What is the role of the supervisor in the staff meeting-a leader` |
| `L85 a L85` | 2 | **0** | P29 rotulo OPERATION REVIEWS, sin cuerpo que extraer | `85:OPERATION REVIEWS` |
| `L87 a L87` | 153 | **0** | P30 que es la revision de operaciones y su proposito: DEFINICION con sus FINES, 9.1 restriccion 1 | `87:This is the medium of interaction for people who don't otherwise` |
| `L89 a L89` | 38 | **1** | P31 CABEZA DE SERIE: los CUATRO jugadores de la revision, contados y nombrados uno a uno | `89:Who are the players at an operation review? The organizing manag` |
| `L91 a L91` | 126 | **1** | P32 EL MANDO ORGANIZADOR: sus tareas nombradas una a una, incluida la de llevar el tiempo | `91:The supervisor of the presenting managers-an Intel divisional ma` |
| `L93 a L93` | 102 | **1** | P33 EL MANDO REVISOR: preguntar, comentar, dar el espiritu, y no leer el material por adelantado | `93:The reviewing manager is the senior supervisor at whom the revie` |
| `L95 a L95` | 168 | **1** | P34 LOS PRESENTADORES: los apoyos visuales, los cuatro minutos por apoyo, resaltar y vigilar al publico | `95:The people presenting the reviews-a group of marketing superviso` |
| `L97 a L97` | 174 | **1** | P35 EL PUBLICO: preguntar, anotar, hablar si no se esta de acuerdo, y dejar constancia del error de hecho | `97:The audience at an operation review also has a crucial part to p` |
| `L99 a L99` | 2 | **0** | P36 rotulo Mission-Oriented Meetings, sin cuerpo que extraer | `99:Mission-Oriented Meetings` |
| `L101 a L101` | 142 | **0** | P37 que es la reunion de mision y de quien es la culpa si falla: DEFINICION con POSTURA | `101:Unlike a process-oriented meeting, which is a regularly schedule` |
| `L103 a L103` | 71 | **1** | P38 ANTES DE CONVOCAR: el objetivo claro y las TRES preguntas que hay que contestar que si | `103:Thus the chairman must have a clear understanding of the meeting` |
| `L105 a L105` | 148 | **1** | P39 EL COSTE EN DINERO de la reunion y que hacer con el: CIFRA DEL AUTOR mas procedimiento propio | `105:An estimate of the dollar cost of a manager's time, including ov` |
| `L107 a L109` | 133 | **1** | P40 LA ASISTENCIA: identificar, conseguir el compromiso, el sustituto con poder, y el corte de ocho | `107:Assuming the meeting does need to be held, the chairman faces a ` |
| `L111 a L111` | 89 | **1** | P41 LA DISCIPLINA: no dejar pasar la tardanza y encarar al que llega tarde, con el coste por hora delante | `111:The chairman is also responsible for maintaining discipline. It ` |
| `L113 a L113` | 67 | **1** | P42 LA LOGISTICA: el equipo de la sala y la agenda que dice el proposito y el papel de cada uno | `113:The chairman should finally be responsible for logistical matter` |
| `L115 a L169` | 77 | **0** | P43 el ejemplar de agenda de la reunion de Filipinas: CASO del autor reproducido entero, manual 3.5 | `115:To:` |
| `L171 a L171` | 109 | **0** | P44 regimentacion contra disciplina, y el quirofano: POSTURA | `171:This may sound like too much regimentation for you, but whether ` |
| `L173 a L173` | 122 | **1** | P45 EL ACTA DESPUES DE LA REUNION: que resuma, que llegue rapido, y que diga que, quien y cuando | `173:Once the meeting is over, the chairman must nail down exactly wh` |
| `L175 a L175` | 113 | **0** | P46 el ochenta contra veinte y la senial de mala organizacion: POSTURA con cifra de Drucker | `175:Ideally, a manager should never have to call an ad hoc, mission-` |
| | **4962** | **26** | **el cuerpo entero de cap_05, cero lineas sin cubrir y cero solapes** | |

### LL.4.c. **EL TECHO, CONTRASTADO Y NO DECIDIDO AQUI**

<!-- TALLADO: parcial script=.v50/frontera.py salida=.v50/frontera_cap_05.txt -->

    ==============================================================================
    3. EL TECHO, CONTRASTADO Y NO DECIDIDO AQUI
    ==============================================================================
    NODOS QUE MI FRONTERA DA EN LA UNIDAD DE LA VUELTA SIGUIENTE (cap_05): 26
    TECHO DE CANDIDATOS POR VUELTA (EXTRACTOR.md 12.4): entre 5 y 15
    DENTRO DEL TECHO                                             : NO
    SI DA NO, MANDA LA REGLA DE PRECEDENCIA DE 12.4: la vuelta cierra en esta unidad,
    se mina hasta el techo y la linea del tramo dice en que candidato corto.

**VEINTISEIS CONTRA UN TECHO DE QUINCE, Y ES LA CIFRA MAS ALTA QUE HA DADO UN CAPITULO DE ESTE
LIBRO** (`cap_04` dio `22`). **La regla de precedencia de 12.4 se dispara de antemano: `cap_05` no
cabe en una vuelta**, y quien lo mine cerrara en esa unidad diciendo en que candidato corto. **Yo
no lo mino hoy: hoy solo publico su frontera**, que es lo que el encargo pide.

**Y UNA ADVERTENCIA DE COSTE QUE DEJO ESCRITA PORQUE LA MEDI HOY:** mis tres pasadas de aduana de
`LL.2` costaron `639,0`, `335,0` y `410,0` s con la bandeja en `44`. **Cada ficha que entra en la
bandeja sube la poblacion del barrido** (`391`, `392`, `393` en mis tres informes, leidos de
`LL.2.e`, `LL.2.g` y `LL.2.i`), **asi que un capitulo de `26` nodos se paga mas caro por nodo que
uno de `22`.** No propongo nada con esto: lo dejo medido para quien escriba el techo de la
vuelta 51.

### LL.4.d. **LOS VEINTE TRAMOS QUE DAN CERO, Y SON CASI LA MITAD**

<!-- TALLADO: parcial salida=.v50/cero_tramos_05.txt -->

    $ los tramos de la tabla que llevan **0** en la columna de nodos
    filas: 46 cero: 20
    P1 P2 P3 P4 P5 P8 P9 P10 P21 P22 P23 P24 P25 P29 P30 P36 P37 P43 P44 P46
    palabras que esos tramos suman: 1896 de 4962

**Un tramo que da cero es una decision, no un descuido**, y cada uno lleva su regla escrita en la
columna *que es, y por que* de la tabla de arriba, que es la que imprime el instrumento. **Los
cuatro motivos, agrupados:**

| motivo | tramos | la regla que lo tumba |
|---|---|---|
| **CASO del autor** | `P9` (las clases privadas de memorias), `P22` (el uno a uno con el responsable de ventas), `P23` (el uno a uno en casa, que el libro llama digresion), `P25` (su primer grupo de ingenieros), `P43` (la agenda de Filipinas, reproducida entera) | manual 3.5: el caso no es la casa, y entra **nombrado dentro** del nodo de su doctrina |
| **POSTURA o DEFINICION** | `P2`, `P3`, `P4`, `P21`, `P30`, `P37`, `P44`, `P46` | `EXTRACTOR.md` 9: una postura no ejecuta una busqueda, y una definicion no tiene nada que hacer |
| **rotulo o anuncio, sin cuerpo que extraer** | `P1`, `P5`, `P8`, `P24`, `P29`, `P36` | son el numero del capitulo, su titulo y los cuatro rotulos de seccion |
| **acota el alcance, y acotar no es procedimentar** | `P10` | *here I want to talk about one-on-ones between a supervisor and each of the professionals who report to him directly*: el autor dice DE QUE va a hablar, y **NOMBRAR NO ES PROCEDIMENTAR** |

**LOS DOS QUE MAS ME COSTARON, Y LOS DIGO PARA QUE SE PUEDAN TUMBAR:**

- **`P4`** enuncia las **DOS** clases de reunion y las nombra, asi que parece una cabeza de serie de
  `D.37`. **Le doy cero** porque lo que pone bajo cada nombre es **para que sirve cada una**, no un
  inventario de medios: *knowledge is shared and information is exchanged* son FINES, y `9.1`
  restriccion `1` los deja fuera. **La cabeza de serie de verdad es `P7`**, que dice *three kinds*
  y las nombra una a una, y esas tres si tienen procedimiento detras.
- **`P43`** son `28` lineas de agenda reproducida (`L115 a L169`, `77` palabras). **Le doy cero** y
  su material entra **nombrado dentro de `P42`**, que es el tramo donde el libro dice que el
  presidente mande una agenda y que anuncia el ejemplar. **Si alguien le diera nodo propio, su
  entregable llevaria un dato del caso** (la planta de Filipinas), que es la senial barata que
  manual 3.5 nombra.

| tarea | que pide | estado |
|---|---|---|
| `LL.4` | la frontera de `cap_05` publicada antes de minar nada, con el molde de `HH.2.c` y sus tres cifras de control | **CERRADA en `LL.4`**: `46` tramos, `4962` contra `4962`, `29.820` caracteres de cuerpo, `0` lineas sin cubrir, `0` solapes, cruce con `wc -w` al digito, `26` nodos contra un techo de `15` y los `20` tramos de cero con su regla |
