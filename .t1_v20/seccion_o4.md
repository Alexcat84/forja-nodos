
---

## O.4. TAREA 3: `cap_10` **SI CABE**. LA FRONTERA CORTADA Y PUBLICADA, Y LA VUELTA CIERRA EN `cap_09`. **CERRADA**

*El encargo pone cuatro puntos y los cuatro se ejecutan en orden. **El primero es obligatorio
pase lo que pase, y es el caro**: cortar la frontera y publicarla ANTES de extraer.*

### O.4.a. LA DENSIDAD Y LA PROYECCION, REMEDIDAS POR MI (`EXTRACTOR.md` 5)

    $ sed -n '8,$p' fuentes/scott_radical_candor/cap_10.md | wc -w
      8976
    $ sed -n '1,6p' fuentes/scott_radical_candor/cap_10.md
      libro: Scott, Radical Candor
      unidad: Cap. 7
      titulo_textual: Team
    $ python (17482 / 20 y 8976 / eso)
      874.1 palabras por candidato   ->   8976 / 874.1 = 10,3 candidatos

**LAS TRES CIFRAS DEL ENCARGO REPRODUCEN: `8.976` de cuerpo, `874` por candidato, `10,3` de
proyeccion.** Y el rotulo textual tambien: **`Team`, unidad `Cap. 7`.**

### O.4.b. **LA FRONTERA DE `cap_10`: LA COMPROBACION VA ANTES DE LA TABLA, Y CIERRA AL DIGITO**

*`EXTRACTOR.md` 10 y punto 1 del encargo: **si los dos totales no son el mismo, la cuenta de
piezas NO se publica, se publica la diferencia.** Asi que la comprobacion se corre primero.*

    $ python .t1_v20/frontera10.py    (la comprobacion va ANTES de la tabla)
    piezas                                 : 39
    lineas con contenido de L8 en adelante : 128
    lineas NO cubiertas                    : 0  []
    SOLAPES                                : 0  []
    cubiertas que no son contenido         : 0
    suma de las filas                      : 8976 palabras
    cuerpo medido aparte (sed 8,$ | wc -w) : 8976 palabras
    IGUALES                                : True

> ### **CIERRA AL DIGITO: `8.976` CONTRA `8.976`, CERO LINEAS SIN CUBRIR Y CERO SOLAPES. LA CUENTA DE PIEZAS SE PUEDE PUBLICAR.**

**LA TABLA NO ESTA TECLEADA: LA IMPRIME EL MISMO GUION QUE CORRE LA COMPROBACION** (`5`), con
la salida literal de la primera linea de cada pieza pegada en su ultima columna (`D.35`). Las
comillas tipograficas del original van normalizadas a grafia llana, porque la guarda `guiones`
muerde lo que yo escribo.

| pieza | tramo | palabras | da nodo? | **la salida, pegada** |
|---|---|---:|---|---|
| **P1** | `L9` a `L9` | 6 | **NO** | `9:Techniques for avoiding boredom and burnout` |
| **P2** | `L11` a `L13` | 181 | **NO** | `11:CHAPTER THREE ("UNDERSTAND WHAT MOTIVATES Each Person on Your Team") discussed the imp` |
| **P3** | `L15` a `L15` | 2 | **NO** | `15:CAREER CONVERSATIONS` |
| **P4** | `L17` a `L17` | 17 | **NO** | `17:Understand people's motivations and ambitions to help them take a step in the directio` |
| **P5** | `L19` a `L21` | 181 | **NO** | `19:AS DESCRIBED IN Chapter Three, all people have their own growth trajectories, and it's` |
| **P6** | `L23` a `L45` | 1254 | **NO** | `23:Russ Laraway, the cofounder of our company, Candor, Inc., is the very best manager I'v` |
| **P7** | `L47` a `L59` | 780 | **SI** | `47:Conversation one: life story` |
| **P8** | `L61` a `L75` | 737 | **SI** | `61:The second conversation: dreams` |
| **P9** | `L77` a `L87` | 345 | **SI** | `77:Conversation three: eighteen-month plan` |
| **P10** | `L89` a `L91` | 101 | **NO** | `89:* * *` |
| **P11** | `L93` a `L93` | 2 | **NO** | `93:GROWTH MANAGEMENT` |
| **P12** | `L95` a `L95` | 15 | **NO** | `95:Figure out who needs what types of opportunities, and how you're going to provide them` |
| **P13** | `L97` a `L99` | 120 | **SI** | `97:YOU'VE HAD YOUR three conversations and begun the process of lining up opportunities o` |
| **P14** | `L101` a `L105` | 174 | **SI** | `101:Put names in boxes (temporarily!)` |
| **P15** | `L107` a `L113` | 299 | **SI** | `107:Write growth plans` |
| **P16** | `L115` a `L119` | 243 | **SI** | `115:Don't be an "easy grader" or a "hard grader"` |
| **P17** | `L121` a `L125` | 242 | **SI** | `121:Ensure fairness by level` |
| **P18** | `L127` a `L127` | 6 | **NO** | `127:HIRING: YOUR MENTALITY AND YOUR PROCESS` |
| **P19** | `L129` a `L129` | 66 | **SI** | `129:WHEN HIRING, YOU'RE obviously looking for people who will be great at the job. But sho` |
| **P20** | `L131` a `L131` | 1 | **NO** | `131:Process` |
| **P21** | `L133` a `L163` | 1428 | **SI** | `133:Your hiring process is important; it's a vital part of building a great team. When you` |
| **P22** | `L165` a `L165` | 1 | **NO** | `165:FIRING` |
| **P23** | `L167` a `L167` | 3 | **NO** | `167:A necessary evil` |
| **P24** | `L169` a `L173` | 228 | **SI** | `169:SOME COMPANIES DON'T invest much time in the hiring process, on the theory that it's e` |
| **P25** | `L175` a `L179` | 361 | **SI** | `175:Don't wait too long` |
| **P26** | `L181` a `L187` | 315 | **SI** | `181:Don't make the decision unilaterally` |
| **P27** | `L189` a `L195` | 288 | **SI** | `189:Give a damn` |
| **P28** | `L197` a `L201` | 176 | **SI** | `197:Follow up` |
| **P29** | `L203` a `L203` | 1 | **NO** | `203:PROMOTIONS` |
| **P30** | `L205` a `L223` | 637 | **SI** | `205:Be fair` |
| **P31** | `L225` a `L225` | 4 | **NO** | `225:REWARD YOUR ROCK STARS` |
| **P32** | `L227` a `L227` | 8 | **NO** | `227:Don't give all the glory to the superstars` |
| **P33** | `L229` a `L237` | 249 | **SI** | `229:Avoid promotion/status obsession` |
| **P34** | `L239` a `L243` | 138 | **SI** | `239:Say "thank-you"` |
| **P35** | `L245` a `L247` | 109 | **SI** | `245:Gurus` |
| **P36** | `L249` a `L251` | 60 | **SI** | `249:Public presentations` |
| **P37** | `L253` a `L255` | 63 | **NO** | `253:AVOID ABSENTEE MANAGEMENT AND MICROMANAGEMENT` |
| **P38** | `L257` a `L259` | 133 | **NO** | `257:SUMMARY` |
| **P39** | `L261` a `L263` | 2 | **NO** | `261:8.` |

### O.4.c. QUE PIEZA DA NODO Y CUAL NO, **CON SU MOTIVO ESCRITO UNA A UNA** (`D.27`)

*Las **19** que no dan nodo llevan su motivo, que es lo que deja releerlas. La tabla la
imprime el mismo guion.*

| pieza | **da nodo?** | motivo |
|---|---|---|
| **P1** `L9` | **NO** | subtitulo del capitulo, 6 palabras. Nada que hacer |
| **P2** `L11` a `L13` | **NO** | entrada del capitulo: remite al capitulo tres y describe el problema. Nombrar no es procedimentar |
| **P3** `L15` | **NO** | rotulo de seccion, 2 palabras, sin cuerpo propio |
| **P4** `L17` | **NO** | subtitulo de la seccion, 17 palabras, sin cuerpo propio |
| **P5** `L19` a `L21` | **NO** | por que hacen falta las conversaciones de carrera y que ganan. Es la razon de la seccion, no un acto: su unico mandato, tenlas con cada persona, lo ejecutan enteras `P7`, `P8` y `P9` |
| **P6** `L23` a `L45` | **NO** | **EL CASO DE RUSS LARAWAY, 1.254 palabras**: como llego al metodo, con sus dos personas de ejemplo. Manual 3.5, **el caso no es la casa**: la doctrina vive en `P7`, `P8` y `P9` y el caso entra ahi como ejemplo nombrado |
| **P7** `L47` a `L59` | **SI** | la linea 49 pone la primera conversacion con su pregunta de arranque, sus temas y su duracion. Inventario de MEDIOS del propio libro |
| **P8** `L61` a `L75` | **SI** | la linea 69 dice *Russ recommends* que empieces asi y la 71 manda crear un documento con de tres a cinco columnas. Etapas y objetos nombrados |
| **P9** `L77` a `L87` | **SI** | la linea 79 pone las preguntas y la 81 dice *Here is what to do* con su lista. Inventario de MEDIOS |
| **P10** `L89` a `L91` | **NO** | cierre de la seccion: dice que esto es una vista de alto nivel y **remite a una web y a un libro que Russ esta escribiendo**. Remite al procedimiento de otro, que es el caso literal de la vara madre |
| **P11** `L93` | **NO** | rotulo de seccion, 2 palabras |
| **P12** `L95` | **NO** | subtitulo de la seccion, 15 palabras, sin cuerpo propio |
| **P13** `L97` a `L99` | **SI** | la linea 99 manda armar un plan de gestion del crecimiento para cada persona **una vez al anio** y mirar el equipo entero para cruzar aspiraciones con necesidades. Acto con su periodo escrito por el libro |
| **P14** `L101` a `L105` | **SI** | actos nombrados: escribir los nombres en sus casillas, identificar a los que estan fuera, y buscar una mirada de fuera que conozca el trabajo |
| **P15** `L107` a `L113` | **SI** | manda un plan de crecimiento de tres a cinco puntos por persona, con proyectos que lo sostengan, y dice que hacer con quien hace mal trabajo y no mejora |
| **P16** `L115` a `L119` | **SI** | actos nombrados: comparar notas con los iguales, y si diriges jefes, montar una via para que todos vean lo mismo |
| **P17** `L121` a `L125` | **SI** | actos nombrados: comprobar la equidad entre niveles y no solo dentro del equipo propio |
| **P18** `L127` | **NO** | rotulo de seccion, 6 palabras |
| **P19** `L129` | **SI, Y ES MI DISCUTIBLE 3** | la linea 129 pone el acto y su criterio: mirar la proporcion del equipo y, si tienes demasiados superestrellas, **contratar una estrella de roca a continuacion**. Son 66 palabras: la pieza mas pobre de las que doy por buenas |
| **P20** `L131` | **NO** | rotulo, 1 palabra |
| **P21** `L133` a `L163` | **SI, Y ES MI DISCUTIBLE 1** | la linea 135 cierra con *here are some simple things you can do* y detras van **SEIS practicas rotuladas**. Inventario de MEDIOS del propio libro, y **el mismo corte que `P24` y `P27` de `cap_09`**. Pero son **1.428 palabras**, la pieza mas grande del capitulo |
| **P22** `L165` | **NO** | rotulo de seccion, 1 palabra |
| **P23** `L167` | **NO** | subtitulo de la seccion, 3 palabras |
| **P24** `L169` a `L173` | **SI, Y TRAE LA UNICA `D.37` VIVA DEL CAPITULO** | la linea 173 dice *if you do three things, you can make it far, far easier* y las nombra debajo. **LA CUENTA ESTA ESCRITA**: es la cabeza de una serie `D.37` de **TRES**. Ver `O.4.d` |
| **P25** `L175` a `L179` | **SI** | la linea 179 pone **CUATRO razones numeradas por el texto** (*One, ... Two, ... Three, ... Four*) para identificar pronto el bajo desempenio. Serie numerada del propio libro |
| **P26** `L181` a `L187` | **SI** | actos nombrados: pedir consejo al jefe, calibrar con los iguales, documentar con quien sepa, y escribir tu los correos y el plan de mejora |
| **P27** `L189` a `L195` | **SI** | actos nombrados: respirar y dar un paso atras, no quedarse atrapado en el consejo legal, y despedir con humildad |
| **P28** `L197` a `L201` | **SI** | actos nombrados con su periodo escrito: escribir **al mes**, mantener la oreja en el suelo, y seguir siendo franco con quien se fue |
| **P29** `L203` | **NO** | rotulo de seccion, 1 palabra |
| **P30** `L205` a `L223` | **SI** | la linea 213 cierra con *here are some tips for preventing the politics* y detras van **CINCO rotuladas**. Inventario de MEDIOS |
| **P31** `L225` | **NO** | rotulo de seccion, 4 palabras |
| **P32** `L227` | **NO** | subtitulo de la seccion, 8 palabras, sin cuerpo propio |
| **P33** `L229` a `L237` | **SI** | actos nombrados: no obsesionarse con el ascenso, anunciar el cambio de papel, y pensar que se elogia en publico |
| **P34** `L239` a `L243` | **SI** | el acto y su distincion escrita: dar las gracias, y en que se diferencia de elogiar |
| **P35** `L245` a `L247` | **SI** | actos nombrados: reconocer a alguien como referente de su area y darle el papel que eso lleva |
| **P36** `L249` a `L251` | **SI, Y ES MI DISCUTIBLE 4** | el acto: dar a esa persona presentaciones publicas como manera de reconocer lo que hace. **60 palabras, la pieza mas pobre que doy por buena**, y `15.4` dice que el parrafo pobre produce el nodo inventado |
| **P37** `L253` a `L255` | **NO, Y ES MI DISCUTIBLE 2** | la linea 255 dice *I have developed a simple chart* **y el grafico NO esta en el recorte**. Mapa sin sentidos: no es medio mapa, no es nada |
| **P38** `L257` a `L259` | **NO** | resumen del capitulo: nombra los seis trabajos y no trae procedimiento propio de ninguno. Nombrar no es procedimentar |
| **P39** `L261` a `L263` | **NO** | cabecera del capitulo siguiente, `8.` `RESULTS`, 2 palabras |

> ### **EL RECUENTO, Y LA CIFRA QUE DECIDE LA VUELTA**
>
>     $ python .t1_v20/frontera10.py | tail -4
>     piezas de la frontera        : 39
>     piezas que DAN NODO          : 20   P7 P8 P9 P13 P14 P15 P16 P17 P19 P21 P24 P25 P26 P27 P28 P30 P33 P34 P35 P36
>     piezas que NO dan nodo       : 19
>     palabras de las que dan nodo : 6995 de 8976
>
> | | |
> |---|---:|
> | piezas de la frontera | **39** |
> | piezas que **dan nodo** | **20** |
> | piezas que **no** dan nodo, con su motivo escrito arriba | **19** |
> | palabras cubiertas, suma de filas contra cuerpo | **8.976 contra 8.976** |
> | **proyeccion por densidad** | **10,3** |
> | **frontera real** | **20** |
>
> ### **LA PROYECCION SE QUEDA EN LA MITAD, EXACTAMENTE COMO EN `cap_09`, Y ESO YA NO ES UNA SORPRESA: ES UN PATRON CON DOS CASOS MEDIDOS.**
>
> `cap_09` proyectaba 34, 32 y 15 por tres densidades distintas **y dio 20**. `cap_10`
> proyecta **10,3** por la densidad real de `cap_09` **y da 20**. **La densidad de palabras
> por candidato no predice la frontera de este libro**, y lo digo con los dos casos al lado en
> vez de volver a proyectar. El motivo se ve en la tabla: `cap_09` tiene **17.482** palabras
> con **10** piezas que no dan nodo, y `cap_10` tiene **8.976** con **19**. **`cap_10` es la
> mitad de largo y tiene el doble de rotulos**, asi que sus piezas son mucho mas pequenias:
> **350 palabras por pieza que da nodo contra 874 en `cap_09`.**
>
> **LO PROPONGO EN MI SEDE Y NO ME LO ADJUDICO** (`EXTRACTOR.md` 14): **el denominador que
> predice esta frontera no es la palabra, es el rotulo.** Cortar la frontera cuesta unos
> minutos y acierta; proyectar por densidad ha fallado en los dos capitulos en que se ha
> medido, **y las dos veces por debajo**. No pido maquinaria: pido que el encargo siguiente
> **corte la frontera antes de decidir el volumen**, que es lo que este ya me hizo hacer.

### O.4.d. LA `D.37` VIVA DE `cap_10`, LEVANTADA HOY Y DEJADA CON SU MEDIDA PARA QUIEN LA EXTRAIGA

*No extraigo `cap_10` (`O.4.e`), asi que **no la resuelvo**: la traigo con su cita pegada,
que es lo que `EXTRACTOR.md` 5 y 7 piden de un hecho que no me toca cerrar.*

    $ sed -n '173p' fuentes/scott_radical_candor/cap_10.md
      Firing people is hard, and it ought to be hard. But if you do three things, you can
      make it far, far easier on the person you are firing as well as on yourself and your team.
    $ grep -n "^Don't wait too long$\|^Don't make the decision unilaterally$\|^Give a damn$\|^Follow up$" fuentes/scott_radical_candor/cap_10.md
      189:Give a damn
      197:Follow up
                 <- DOS de cuatro, y el barrido esta mal, no el libro: L175 y L181 llevan
                    APOSTROFO TIPOGRAFICO y mi patron tecleaba el recto. Lo digo en vez de
                    publicar el dos, que es el mismo remedio de O.2.d desde el otro lado.
    $ grep -nE "^(Don.t wait too long|Don.t make the decision unilaterally|Give a damn|Follow up)$" fuentes/scott_radical_candor/cap_10.md
      175:Don't wait too long
      181:Don't make the decision unilaterally
      189:Give a damn
      197:Follow up
    $ grep -cE "^(Don.t wait too long|Don.t make the decision unilaterally|Give a damn|Follow up)$" fuentes/scott_radical_candor/cap_10.md
      4
    $ sed -n '179p' fuentes/scott_radical_candor/cap_10.md
      There are four very good reasons to push yourself to identify underperformance early.
      One, to be fair to the person who's failing. ...

> ### **`L173` DICE `three things` Y DEBAJO HAY CUATRO ROTULOS. ES LA MISMA FORMA EXACTA QUE EL `four rules of thumb` DE `L317` DE `cap_09`, QUE COSTO UNA ADJUDICACION ENTERA.**
>
> **Y ESTA VEZ LA CASA YA TIENE LA DOCTRINA ESCRITA, asi que la aplico en vez de volver a
> subir la tension:** la `ACTA 19` `4.1` adjudico que **la serie es la que el libro cuenta, no
> la que el maquetador rotulo**, y que el rotulo de mas **es una coda fuera de la serie
> anunciada** cuando no cabe en el marco que la cabeza pone.
>
> **EL MARCO QUE `L173` PONE:** *tres cosas que hacen el despido mas facil **para la persona a
> la que despides, para ti y para tu equipo***. **`Follow up` (`L197`) no es eso:** es lo que
> se hace **al mes de haber despedido**, cuando el despido ya ocurrio. **Las tres son `L175`,
> `L181` y `L189`, y `L197` es coda.**
>
> **LO DIGO COMO HIPOTESIS MEDIDA Y NO COMO ADJUDICACION, porque adjudicar no es mio**
> (`EXTRACTOR.md` 14) **y porque no he escrito los nodos**: quien extraiga `cap_10` tiene la
> cita y el marco, y **si la lectura de los pasos lo contradice, gana la lectura** (`P.17`).
>
> **Y LO QUE SI CAMBIA RESPECTO A `cap_09`, que es lo que la hace mas cara que aquella:** las
> tres partes de `L317` eran **pasos de un solo nodo**, asi que no habia arista que cablear.
> **Las tres de `L173` son `P25`, `P26` y `P27` de mi frontera, y las tres DAN NODO.** Asi que
> **aqui `D.37` si cablea tres aristas de verdad**, de `P24` a cada una, **y hay que
> declararlas en la misma vuelta en que se inserten las partes.** Van a mi cola como las
> numeros **13, 14 y 15** (`O.6.4`).

### O.4.e. **DONDE CIERRA LA VUELTA, Y CON QUE PUNTO DEL ENCARGO**

*Los cuatro puntos del encargo, recorridos en su orden y con su cifra delante. **No elijo: la
cifra elige.***

| punto | lo que dice | como sale |
|---:|---|---|
| **1** | corta la frontera y publicala ANTES de extraer, con la suma cruzada | **CUMPLIDO.** `39` piezas, `8.976` contra `8.976`, `0` sin cubrir, `0` solapes (`O.4.b`) |
| **2** | si `5` mas las piezas de `cap_10` cabe en quince, escribes `cap_10` entero | **NO APLICA.** `5 + 20 = 25`, y **25 no cabe en quince** |
| **3** | si `cap_10` SOLO ya pasa del techo, lo escribes ENTERO igual y no abres `cap_11` | **APLICARIA**, porque `cap_10` solo da **20 contra 15**. **Pero cede al punto 4, que es el que lo condiciona** |
| **4** | si escribir `cap_10` entero pone en riesgo el bloque de cierre, **NO escribes `cap_10`**: cierras en `cap_09` completo y lo declaras | **ES EL QUE SE APLICA.** Y va abajo con su cuenta, no con un adjetivo |

> # **LA VUELTA CIERRA EN `cap_09` COMPLETO, CON 5 CANDIDATOS ESCRITOS HOY Y `cap_09` EN 20 DE 20. `cap_10` NO SE EXTRAE, Y SU FRONTERA QUEDA CORTADA Y PUBLICADA PARA LA VUELTA SIGUIENTE. `cap_11` A `cap_14` SIGUEN SIN TOCAR.**

**Y AHORA LA CUENTA QUE ME LLEVA AL PUNTO 4 Y NO AL 3, porque el punto 4 dice *pone en riesgo*
y eso hay que medirlo y no sentirlo:**

| | |
|---|---:|
| candidatos que `cap_10` pide, frontera real | **20** |
| lo que tarda un informe de aduana en esta maquina, medido hoy | **`real 3m4.557s`** |
| **solo la aduana de esos 20, sin escribir ni una linea** | **mas de una hora** |
| candidatos ya escritos hoy, con sus informes | **5, mas el re informe de `P28`: 6 informes** |
| **la vuelta seria de 25 candidatos** | **y 25 es el numero exacto de la vuelta 17** |

> ### **LA VUELTA 17 ESCRIBIO 25 CANDIDATOS Y NO CERRO SU REPORTE. COSTO UNA PARADA Y UNA VUELTA ENTERA DE RECOGIDA. ES EL EJEMPLAR QUE `12.4` TIENE ESCRITO, Y ES LA MISMA CIFRA QUE ME SALDRIA HOY.**
>
> **Y NO LO DIGO YO SOLO, LO DICE EL ENCARGO EN SU PROPIA LETRA**, dos veces y en mayusculas:
> *y repito lo que mas importa, porque es el disparador de verdad: **cierra tu reporte***; y
> *un capitulo con su cierre escrito se audita; sin el, no*.
>
> **POR QUE ESTA ES LA FORMA LEGITIMA DE QUEDARSE CORTO Y NO UNA EXCUSA, con la letra del
> punto 4 delante:** *esa es la unica forma legitima de quedarte corto, **y es en el limite de
> capitulo, no dentro de uno***. **Me quedo corto en el limite de capitulo exacto:** `cap_09`
> entero y `cap_10` sin empezar. **Cero piezas de `cap_10` escritas, cero a medias, cero
> deuda dentro de un capitulo.** Lo que la vuelta 19 dejo fue un capitulo partido; **lo que
> esta vuelta deja es un capitulo sin abrir con su frontera ya cortada.**
>
> **Y LO QUE NO HAGO, DICHO POR SU NOMBRE PARA QUE SE PUEDA COBRAR SI ES UN ERROR: no escribo
> ni uno de los 20 de `cap_10`.** Escribir tres o cinco seria **exactamente** partir un
> capitulo, que es lo que la adjudicacion de la `ACTA 19` `4.3` acaba de prohibir y lo que
> esta vuelta vino a arreglar. **Entre quedarme en el limite de capitulo y volver a partir
> uno, la regla adjudicada no me deja elegir.**

**LO QUE LA VUELTA SIGUIENTE SE ENCUENTRA HECHO, y es la mitad caro del trabajo de `cap_10`:**

- **la frontera entera cortada, cerrada contra el cuerpo y publicada**, con las 39 filas y su
  cita pegada, y las 19 que no dan nodo con su motivo escrito;
- **la cuenta de candidatos que pide: 20**, medida y no proyectada;
- **la `D.37` de `L173` levantada con su cita y su marco**, con las tres aristas que cablea
  nombradas (`O.4.d`);
- **cuatro discutibles marcados sobre piezas que yo no voy a escribir** (`O.5`), que es lo
  mas incomodo que puedo dejar y lo mas util.

**LA TAREA 3 QUEDA CERRADA**, con su punto 1 cumplido entero y su decision tomada por el
punto 4.
