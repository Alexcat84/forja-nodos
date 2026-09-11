# APERTURA CIEGA DE LA VUELTA 10

**Lote 3, `zhuo_manager`. Tramo: Cap. 3 (`cap_04.md`) y Cap. 4 (`cap_05.md`), mas los dos
de la relectura conjunta 2.d que salen de `cap_03.md`.**

*Escrita por el auditor en la fase de apertura ciega de `D.34`, con `docs/loop/REPORTE.md`
retirado del arbol por el arnes. **No lo he recuperado de git ni por ninguna otra via.**
Esta es la lectura que despues se compara con la del extractor: mientras no se compare,
**no es una adjudicacion y no mueve credito de nadie.***

---

## 0. QUE VI Y QUE NO VI ANTES DE LEER, DICHO EXACTO

**La apertura ciega no es ciega a todo, y decir en que no lo es vale mas que la palabra
"ciega" repetida.** El orden real de mis actos fue este:

| lo que consulte, en orden | ciega? |
|---|---|
| `AUDITOR_FORJA.md` entero | protocolo mio |
| `ls` de `cuarentena/zhuo_manager/` y `fuentes/zhuo_manager/` | **NO: vi los 50 nombres de fichero, y un id dice de que va un nodo** |
| `ORDEN_DE_LOTES.md`, `cuarentena/LEEME.md`, `loop.log`, `git status` | estado, no lectura |
| `git log --diff-filter=A` sobre `cuarentena/` | **me dio el corte: 15 ficheros nuevos en un commit, 12 en otro, 2 en otro** |
| **`cuarentena/zhuo_manager/hacer_opinion_accionable.json` entero** | **NO, Y ES LA UNICA: la abri de muestra para aprender el esquema ANTES de leer los capitulos** |
| `dataset/nodos.jsonl`, los 52 ids | estado |
| `docs/loop/PROMPT_SIGUIENTE.md`, mi propio encargo de la vuelta 9 | sede mia |
| **`cap_04.md` entero y `cap_05.md` entero, de la primera a la ultima linea** | **aqui escribi mi inventario de secciones, seccion 3 y seccion 4 de este documento** |
| solo DESPUES, los 27 candidatos con sus pasos | |

**Por tanto:**

1. **NO soy ciego al numero de nodos ni a sus titulos.** El arnes me entrega la bandeja, y
   la bandeja tiene nombres. Lo que si es ciego es **el reparto pieza a pieza, la frontera,
   los discutibles, las aristas y la cuenta de puentes**, que es lo que se compara.
2. **`hacer_opinion_accionable` esta contaminado y no lo cuento como lectura independiente.**
   Lo digo aunque no me convenga: `L207` a `L231` habria dado nodo en mi inventario de todas
   formas, porque es una de las tres preguntas que el propio libro titula, pero **eso lo digo
   yo despues de haberlo visto, y una razon dada despues no vale lo que una dada antes.**
3. Todo lo demas de las secciones 3, 4 y 5 se escribio **con los capitulos delante y la
   bandeja cerrada.**

---

## 1. MI CRITERIO, ESCRITO ANTES DE CLASIFICAR Y NO DESPUES

**a. Para PIEZA CON NODO O SIN NODO.** Manual seccion 4 y la vara de `AUDITOR_FORJA.md` 6.1.
Una pieza saca nodo propio si trae **disparador propio, acto propio y entregable propio**.
`P.5.1`: **nombrar no es procedimentar.** Una cabeza de serie solo vale como nodo si trae
doctrina suya ademas de los nombres de sus hijos.

**b. Para CONTINUA O REPITE.** Con direccion y sin bascula: se pregunta **que aniade el hijo
a la madre**, y **decide si lo que queda fuera es procedimiento en los dos lados**, no el
tamanio del solape.

**c. Para TRANSCRIPCION O PUENTE (`D.30`), y aqui fijo la frontera ANTES de contar**, porque
esta cifra dimensiona el lote siguiente y la seccion 8.3 avisa de hacia donde se inclina sola:

> **ES PUENTE** un paso que manda algo que el libro **no manda en sentido**, y en particular
> el paso en imperativo levantado sobre **narracion en primera persona del pasado** o sobre
> **una cita de un tercero que cuenta y no ordena**. Es la especie de la 2.a de mi encargo
> anterior (`acordar_plan_conjunto_jefe` paso 8 contra `cap_03.md` `L47`).
>
> **ES TRANSCRIPCION** el cambio de modo verbal sobre un consejo que el libro ya dirige al
> lector en segunda persona, aunque venga en condicional o en enunciado. **Esta mitad es mia
> y la sostengo contra mi propio interes**: es la lectura que declare en la 2.a sobre
> `alinear_equipo_proposito_comun` paso 1 y `fijar_proceso_trabajo_equipo` paso 1, y **usar
> ahora una vara mas estrecha para contar mas puentes seria mover la vara a conveniencia.**

---

## 2. LO QUE MEDI YO, CON SU COMANDO AL LADO

    $ awk 'NR>7' fuentes/zhuo_manager/cap_04.md | wc -w        7237
    $ awk 'NR>7' fuentes/zhuo_manager/cap_05.md | wc -w        6318

**Coinciden al numero con las 7.237 y las 6.318 que yo mismo publique en el encargo.**
Suma del tramo: **13.555 palabras.**

**LOS TRES BORDES, comprobados por mi hoy y no copiados de mi nota vieja:**

| borde | lo que leo |
|---|---|
| `cap_04.md` cabecera | `unidad: Cap. 3`, `titulo_textual: Leading a Small Team`, `L9: Chapter Three` |
| `cap_04.md` ultima con texto | **`L321` de 321**, y cierra anunciando el capitulo siguiente: *the topic of our next chapter, giving effective feedback* |
| `cap_05.md` cabecera | `unidad: Cap. 4`, `titulo_textual: The Art of Feedback`, `L9: Chapter Four` |
| `cap_05.md` ultima con texto | **`L289` de 289**, y cierra con la frase de los posteres: *Feedback is a gift* |
| `cap_06.md` cabecera | `unidad: Cap. 5`, `titulo_textual: Managing Yourself`. **Abre unidad nueva: el borde por el otro lado esta limpio** |

**PASOS Y CANDIDATOS, contados por mi sobre los ficheros de cuarentena** (seccion 8.3.1: la
cifra la cuento yo, no la copio):

| unidad | fichero | palabras | candidatos | pasos escritos | candidatos por mil palabras |
|---|---|---:|---:|---:|---:|
| Cap. 3 | `cap_04.md` | 7.237 | **15** | **120** | **2,07** |
| Cap. 4 | `cap_05.md` | 6.318 | **12** | **111** | **1,90** |
| **tramo** | | **13.555** | **27** | **231** | **1,99** |
| (2.d) | `cap_03.md` | | 2 | 10 | no es de este tramo |

**Y LA COMPROBACION QUE SALE CERO SE ESCRIBE CERO:** ningun id de los 50 de la bandeja choca
con los 52 del dataset; ningun id duplicado; ningun candidato trae `nodos_previos` ni
`nodos_siguientes` escritos, que es lo correcto en `MODO_INSERCION=cuarentena` (`D.26`); el
campo `id` y el nombre de fichero dicen lo mismo en **50 de 50**.

---

## 3. MI INVENTARIO DEL Cap. 3, `cap_04.md`, PIEZA A PIEZA

**Escrito leyendo el fichero entero de un tiron, con la bandeja cerrada.**

| # | pieza | lineas | mi lectura a ciegas |
|---:|---|---|---|
| 1 | La reunion semanal de critica | `L17` a `L25` | **SIN NODO.** Esta contada en pasado y en primera persona del plural (*we would run*, *we'd pick an order*). Tiene forma de ritual y aun asi **no manda nada**: es la escena con la que el capitulo abre. **Y lo digo sabiendo que es la pieza con mas aspecto de procedimiento de las que dejo fuera** |
| 2 | El encuadre del capitulo | `L27` a `L29` | **SIN NODO.** *Managing a small team is about mastering a few basic fundamentals*: es indice de capitulo |
| 3 | La definicion de gestion, repetida | `L33` a `L35` | **SIN NODO PROPIO, Y ES IMPORTANTE QUE NO LO TENGA.** Ya vive en `revisar_proposito_personas_proceso`. Repetirla en nodo nuevo habria sido el gemelo del lote |
| 4 | Grove, y el diagnostico motivacion contra habilidad | `L37` a `L45` | **NODO.** Disparador (*trabajo flojo*), acto (*una serie de conversaciones*) y orden explicito en `L43`: *First... Then... If both of those don't resolve... then dive in to whether the issue is with skills* |
| 5 | Las tres afirmaciones de la confianza | `L61` a `L85` | **NODO.** `L61` declara el inventario (*the following three statements*), y cada afirmacion trae su prueba: la del tornasol en `L65`, la reunion incomoda de Rabkin en `L69`, la pregunta del jefe perfecto en `L85` |
| 6 | Mostrarse humano y la cabeza de las cuatro acciones | `L87` a `L101` | **NODO CABEZA, ARGUABLE Y LO DIGO.** `L101` declara el inventario (*requires the following few actions*). Pasa `P.5.1` **por poco**: su doctrina propia es el caso de `L89` a `L99`, donde lo unico que funciono fue admitir que a ella le pasaba igual. **Es la cabeza mas floja de las tres del tramo** |
| 7 | Respetar y cuidar | `L103` a `L119` | **NODO.** Primera de las cuatro acciones. `L113` da el contenido positivo y `L115` la condicion dura del respeto incondicional |
| 8 | La reunion individual semanal | `L121` a `L137` | **NODO.** Trae cifra (`L123`: *no less than a weekly 1:1... for thirty minutes*) y las cuatro ideas de preparacion de `L131` a `L137` |
| 9 | Las preguntas de la reunion individual | `L139` a `L173` | **NODO APARTE, Y NO PARTE DEL ANTERIOR.** Tres grupos titulados por el libro, *Identify*, *Understand*, *Support*, con once preguntas escritas. **Es el mismo caso que el DISCUTIBLE 4 de la vuelta 9, donde a ciegas me equivoque yo argumentando por forma.** Esta vez leo los pasos: `L143` trae encargo propio (*let her lead the 1:1 while you listen and probe*) |
| 10 | Ser honesto sobre el desempenio | `L175` a `L181` | **NODO, y es mi DISCUTIBLE 1** (seccion 7) |
| 11 | Admitir errores propios | `L183` a `L205` | **NODO.** Acto en `L185` (*apologize... take meaningful action*) y las cuatro frases de `L197` a `L203` |
| 12 | Jugar a las fortalezas | `L207` a `L231` | **NODO.** `L227` y `L229` dan el acto (*find opportunities for her to do more in that vein*) con sus dos ejemplos |
| 13 | La extension a equipos | `L233` a `L239` | **NODO APARTE.** `L233` declara la extension (*one step further... it also applies to teams*) y trae cuenta propia: la limonada de `L237`, con Toby al 10 por ciento contra Henry al 33 |
| 14 | El brillante que divide | `L241` a `L255` | **NODO, ARGUABLE.** Es sobre todo postura, y *una advertencia es linea*. Lo salvo porque el libro numera inventario propio: `L251` *What I later realized*, `L253` *The second thing I learned*, `L255` *The third lesson*. **Su entregable es el mas debil del capitulo** |
| 15 | El desencaje de valores | `L257` a `L279` | **NODO** |
| 16 | Mover rapido, cabeza | `L281` a `L303` | **NODO.** Trae la cifra del 80 por ciento (`L287`) y las cinco razones (`L289`) |
| 17 | Las dos opciones | `L305` a `L311` | **NODO APARTE.** `L305` *You have two options at this point*, y `L311` da la pregunta de contraste |
| 18 | El despido, el como | `L313` a `L317` | **NODO APARTE.** Disparador distinto: la decision **ya tomada**. `L313` manda *do it respectfully and directly* |
| 19 | Cierre y anuncio | `L319` a `L321` | **SIN NODO.** Remision entre capitulos |

**MI CUENTA A CIEGAS DEL Cap. 3: 15 nodos.** La bandeja trae 15.

---

## 4. MI INVENTARIO DEL Cap. 4, `cap_05.md`, PIEZA A PIEZA

| # | pieza | lineas | mi lectura a ciegas |
|---:|---|---|---|
| 1 | Drew y Robyn, la peor y la mejor opinion | `L17` a `L25` | **SIN NODO.** Narracion |
| 2 | Que es opinion, y la cabeza de las cuatro formas | `L27` a `L39` | **NODO CABEZA.** Pasa `P.5.1` **con holgura**: su doctrina propia es la definicion estrecha que el libro desmonta (`L35` a `L37`), sin la cual las cuatro formas no se entienden. `L39` declara el inventario |
| 3 | Fijar expectativas al comienzo | `L41` a `L59` | **NODO.** Tres cosas que tratar en `L51` a `L55` y dos ejemplos redactados |
| 4 | Opinion especifica de la tarea | `L61` a `L73` | **NODO** |
| 5 | Opinion sobre la conducta | `L75` a `L89` | **NODO** |
| 6 | Opinion de 360 grados | `L91` a `L101` | **NODO.** Cadencia propia (`L95`: *Every quarter*) y las dos preguntas del correo |
| 7 | Kate, Albert y las tres explicaciones | `L103` a `L125` | **NODO** |
| 8 | El ascenso que no va a llegar | `L127` a `L131` | **PARTE DEL ANTERIOR, Y ES MI DISCUTIBLE 2** (seccion 7) |
| 9 | El proyecto nuevo y exigente | `L133` a `L141` | **PARTE DEL ANTERIOR**, mismo discutible |
| 10 | La meta de octubre que no se llega | `L143` a `L151` | **PARTE DEL ANTERIOR**, mismo discutible |
| 11 | El cierre de la seccion | `L153` a `L155` | **PARTE DEL ANTERIOR.** `L155` es la pregunta con la que se cierra |
| 12 | George, y la cabeza de las tres preguntas | `L157` a `L169` | **NODO CABEZA.** Pasa `P.5.1`: su doctrina propia es la vara de resultado de `L167` (*The mark of a great coach is that others improve under your guidance*). `L169` declara el inventario |
| 13 | Doy opinion con bastante frecuencia? | `L171` a `L181` | **NODO** |
| 14 | Se esta oyendo mi opinion? | `L183` a `L205` | **NODO.** Tres tacticas de cierre en `L203` y `L205` |
| 15 | Lleva mi opinion a accion positiva? | `L207` a `L231` | **NODO.** *(pieza contaminada, seccion 0)* |
| 16 | La opinion critica y las cinco formulaciones | `L233` a `L269` | **NODO.** Las cinco de `L237` a `L245`, la plantilla de `L259`, y el sandwich de elogios de `L263` a `L269` |
| 17 | La mala noticia de una decision ya tomada | `L271` a `L281` | **NODO APARTE.** `L271` abre con disparador propio (*If you are delivering bad news about a decision*) y el acto es distinto: la decision **primero**, y no abrirla a discusion |
| 18 | El cierre del capitulo | `L283` a `L289` | **SIN NODO.** Reflexion de cierre sobre TODA la opinion. **Ojo a donde acaba: mi DISCUTIBLE 4** |

**MI CUENTA A CIEGAS DEL Cap. 4: 12 nodos**, y **15 si los tres escenarios de `L127`, `L133`
y `L143` salieran aparte.** La bandeja trae 12.

---

## 5. LOS DOS DE LA RELECTURA CONJUNTA 2.d, CONTRA `cap_03.md`

*Aqui yo no soy ciego: el caso lo escribi yo en el encargo. Lo que releo es si el corte
aguanta con el texto delante, y una de las dos la declare arguable antes de saber nada.*

| pieza | lineas | mi lectura |
|---|---|---|
| **El equilibrio del contribuidor individual** | `L87` a `L93` | **NODO, Y LA SOSTENGO SIN MATICES.** `L93` trae las tres cosas juntas: disparador numerico (*at the point in which your team becomes four or five people*), acto (*you should have a plan*) y entregable (el plan) |
| **La dinamica con los antiguos pares** | `L73` a `L85` | **NODO, ARGUABLE, Y LO DIJE ARGUABLE ANTES.** Es serie de tres con cabeza y **la tercera no manda nada**: `L85` cuenta en pasado que la autora acabo reconociendo que era normal. Pasa porque las otras dos **si** mandan: `L77` (*don't avoid those conversations... Seek to understand... Think of yourself as a coach*) y `L81` (*you need to address it swiftly and directly*) |

---

## 6. CLASIFICACION CANDIDATO A CANDIDATO

**`ENTRA`** significa: pieza con nodo propio en mi inventario, y el candidato la cubre.
**Ninguna de estas 29 es REPITE en mi lectura.** Las que van con asterisco se explican en la
seccion 7.

### Cap. 3, `cap_04.md`

| candidato | pasos | pieza que cubre | mi clase |
|---|---:|---|---|
| `diagnosticar_falta_motivacion_habilidad` | 9 | `L37` a `L45` | ENTRA |
| `comprobar_confianza_persona_cargo` | 10 | `L61` a `L85` | ENTRA |
| `ganar_confianza_personas_cargo` | 6 | `L87` a `L101` | ENTRA, cabeza floja |
| `respetar_cuidar_persona_cargo` | 8 | `L103` a `L119` | ENTRA |
| `dirigir_reunion_individual_semanal` | 10 | `L121` a `L137` | ENTRA |
| `preguntar_conducir_reunion_individual` | 7 | `L139` a `L173` | ENTRA |
| `ser_honesto_transparente_desempenio` | 7 | `L175` a `L181` | **ENTRA, asterisco** |
| `admitir_errores_areas_mejora_propias` | 9 | `L183` a `L205` | ENTRA |
| `ayudar_personas_jugar_fortalezas` | 8 | `L207` a `L231` | ENTRA |
| `repartir_tiempo_atencion_mejores_equipo` | 8 | `L233` a `L239` | ENTRA |
| `cortar_efecto_divisor_persona_brillante` | 8 | `L241` a `L255` | ENTRA, entregable debil |
| `resolver_desencaje_valores_persona_equipo` | 8 | `L257` a `L279` | **ENTRA, asterisco** |
| `mover_rapido_persona_papel_equivocado` | 9 | `L281` a `L303` | **ENTRA, con un puente en el paso 1** |
| `elegir_recolocar_despedir_persona` | 5 | `L305` a `L311` | **ENTRA, asterisco** |
| `despedir_persona_respeto_franqueza` | 8 | `L313` a `L317` | **ENTRA, asterisco** |

### Cap. 4, `cap_05.md`

| candidato | pasos | pieza que cubre | mi clase |
|---|---:|---|---|
| `elegir_forma_inspirar_cambio_conducta` | 7 | `L27` a `L39` | ENTRA |
| `fijar_expectativas_claras_comienzo` | 9 | `L41` a `L59` | ENTRA |
| `dar_opinion_especifica_tarea` | 8 | `L61` a `L73` | ENTRA |
| `compartir_opinion_conductual_regularidad` | 9 | `L75` a `L89` | ENTRA |
| `recoger_opinion_360_grados` | 10 | `L91` a `L101` | ENTRA |
| `avisar_pronto_incumplimiento_expectativas` | 12 | `L103` a `L155` | **ENTRA, asterisco**, y es el corte que mas discuto |
| `comprobar_opinion_produce_mejora` | 7 | `L157` a `L169` | ENTRA |
| `dar_opinion_frecuencia_suficiente` | 9 | `L171` a `L181` | ENTRA |
| `asegurar_opinion_llega_persona` | 11 | `L183` a `L205` | ENTRA |
| `hacer_opinion_accionable` | 10 | `L207` a `L231` | ENTRA, *contaminado* |
| `dar_opinion_critica_directa_desapasionada` | 11 | `L233` a `L269` | ENTRA |
| `dar_mala_noticia_decision_tomada` | 8 | `L271` a `L281` | **ENTRA, asterisco**, con reparo en el paso 8 |

### Los dos de la 2.d, `cap_03.md`

| candidato | pasos | pieza | mi clase |
|---|---:|---|---|
| `planificar_reduccion_trabajo_individual` | 3 | `L87` a `L93` | ENTRA |
| `establecer_dinamica_nueva_antiguos_pares` | 7 | `L73` a `L85` | ENTRA, arguable declarada |

---

## 7. MIS CUATRO DISCUTIBLES, MARCADOS AHORA Y NO DESPUES

*Los marco **antes** de ver el reporte, que es lo unico que hace informativa a la metrica
(`AUDITOR_FORJA.md` 5.1). Si el extractor marco otros, la diferencia es dato.*

### DISCUTIBLE 1. `ser_honesto_transparente_desempenio` contra `avisar_pronto_incumplimiento_expectativas`

**Es el par que mas cerca esta de REPITE en todo el tramo, y esta a caballo de dos capitulos.**
`cap_04.md` `L181` manda que tu persona a cargo sepa en todo momento donde esta, y acaba
diciendo **en el propio texto**: *For specifics on how to master the art of giving feedback,
see the next chapter.* El capitulo siguiente es exactamente el otro candidato.

**Mi adjudicacion: CONTINUA, no REPITE.** Con direccion: lo que el hijo aniade a la madre es
la regla de tiempo (`L113`: decirlo mucho antes de la revision), las tres explicaciones de
`L117` a `L121` y los tres escenarios. Lo que queda fuera en la madre **tambien es
procedimiento**: el desequilibrio de poder de `L177`, subir el nivel si la persona se lo
pregunta, no dar por hecho que lee entre lineas, y decirlo tambien cuando es estupendo.
**Procedimiento en los dos lados, luego no hay bascula que valga.**

**Lo que si sostengo: piden arista, y `L181` es el paso de la madre que nombra al hijo.**

### DISCUTIBLE 2. Los tres escenarios de `L127`, `L133` y `L143`: un nodo o cuatro

**Es el unico sitio del tramo donde mi corte pudo haber sido otro, y casi lo es.** Los tres
tienen cabecera propia en el libro, disparador propio y acto propio, que es justo el criterio
con el que la vuelta 9 saco las cuatro listas de preguntas a nodo aparte.

**Y aun asi los dejo dentro, por una razon textual y no de forma**, que es lo que `D.19` me
obliga a usar:

> `L39` dice *the four most common **ways** to inspire a change in behavior*.
> `L101` de `cap_04.md` dice *requires the following few **actions***.
> `L169` dice *consider how you're doing with each of the **following***.
> **`L125` dice otra cosa: *Following are some **examples** of how setting expectations early
> can preempt future disappointments*.**

**Tres inventarios declarados contra una lista de ejemplos declarada.** La palabra es del
libro, no mia. **Un lector que los partiera no estaria loco, y lo escribo para que conste que
lo pense**, pero el entregable de los tres es el mismo que el de la cabeza.

### DISCUTIBLE 3. El racimo del despido, que el libro dice dos veces en dos sitios

`resolver_desencaje_valores_persona_equipo` paso 6 manda probar primero un movimiento dentro
de la misma organizacion, de `L275`. `elegir_recolocar_despedir_persona` pasos 1 y 2 dicen lo
mismo, de `L305` a `L307`. **Es el libro el que se repite**, en dos secciones separadas por
veinticinco lineas.

Y el mismo racimo tiene un segundo cruce, este **entre capitulos**:
`despedir_persona_respeto_franqueza` paso 2 dice *no lo abras a discusion, porque no lo es*
(`cap_04.md` `L313`), y `dar_mala_noticia_decision_tomada` paso 2 dice *se firme y no la abras
a discusion* (`cap_05.md` `L275`). **Dos lineas de dos capitulos con la misma orden.**

**Mi adjudicacion: los cuatro CONTINUAN, y ninguno es REPITE.** En los dos cruces queda
procedimiento propio a ambos lados: en `elegir_recolocar`, el *tread carefully* de `L309`, la
prohibicion de ir barajando gente y la pregunta de contraste de `L311`; en `despedir_persona`,
la calle de dos sentidos de `L315` y el no alargar la ruptura de `L317`; en
`dar_mala_noticia`, la plantilla de `L273` y el contraejemplo del consenso fingido de `L275` a
`L277`.

**Pero cuatro nodos con la misma orden dentro y CERO aristas entre ellos es una lectura a
medias**, y esa es la mitad que reclamo.

### DISCUTIBLE 4. Donde acaba `L283`, que es cierre de capitulo y no de seccion

`dar_mala_noticia_decision_tomada` paso 8 se lleva `L283` (*people are not fragile flowers...
Telling it straight is a sign of respect*). **La frase es real y esta bien traducida: no es
puente.** Lo que discuto es la sede: `L283` abre con *what I've learned about giving
feedback, **even the most difficult feedback***, que es el capitulo entero, y acaba metida en
el nodo mas estrecho de los doce.

**Es la especie exacta de la 2.b de mi encargo anterior: el contenido bien, el sitio no.** Y
confirma lo que alli escribi, que **una pasada paso a paso no caza esto**, porque el paso por
separado es fiel.

---

## 8. MI CUENTA DE `PASOS INVENTADOS POR CAPITULO`, HECHA A CIEGAS

**Lei los 241 pasos contra su parrafo.** Con la vara de la seccion 1.c:

| capitulo | fichero | pasos escritos | puentes que veo | tasa | banda alta si cuento los fronterizos |
|---|---|---:|---:|---:|---:|
| **Cap. 3** | `cap_04.md` | 120 | **1** | **0,83 por ciento** | 3 de 120, **2,50** |
| **Cap. 4** | `cap_05.md` | 111 | **0** | **0,00 por ciento** | 1 de 111, **0,90** |
| **total del tramo** | | **231** | **1** | **0,43 por ciento** | 4 de 231, **1,73** |
| (2.d) | `cap_03.md` | 10 | 0 | 0,00 por ciento | 0 |

**EL UNICO PUENTE QUE VEO, con su cita:**

> **`mover_rapido_persona_papel_equivocado`, paso 1.** Ordena *Deja de considerar que tu papel
> es ante todo ser el campeon de tu equipo*. **`L283` no ordena eso: lo cuenta en primera
> persona del pasado** (*When I first started managing, I considered my role above all to be a
> champion for my team*), **y `L285` lo RATIFICA en vez de desmentirlo**: *Nobody. As their
> manager, this was my job. And everyone deserves a second chance.*
>
> **El propio paso se desdice dentro de si mismo**, porque su segunda mitad dice *Nadie lo
> hara, es cierto, y es tu trabajo*. Lo que el libro corrige no es ser campeon: es alargarlo,
> y eso llega en `L287` con el 80 por ciento y en `L299` con el 50 por ciento de la semana.
>
> **Es la especie de la 2.a, y es el sitio que yo mismo avise en el encargo:** donde el libro
> habla en primera persona del pasado.

**LOS TRES FRONTERIZOS QUE DEJO PASAR, y digo por que**, porque un fronterizo callado es una
cifra sin auditar:

| paso | linea | por que lo dejo pasar |
|---|---|---|
| `ayudar_personas_jugar_fortalezas` 3 | `L227` | *Recognition... can be hugely motivating if it feels genuine and specific* es enunciado, y el paso lo pasa a imperativo. **Modo verbal, no contenido** |
| `repartir_tiempo_atencion_mejores_equipo` 8 | `L239` | *if you help them to dream bigger... you'll be amazed* es condicional dirigido al lector. **Es consejo en segunda persona, no narracion** |
| `asegurar_opinion_llega_persona` 5 | `L199` | *This is why positive feedback is so effective* pasa a *Usa opinion positiva*. Mismo caso |

**Y AHORA LO QUE ME OBLIGA A DECIR LA SECCION 8.3, AUNQUE ME DEJE EN MAL LUGAR:**

> **Mi cifra a ciegas queda MUY por debajo de la serie reciente**, que va 3,09 / 5,00 / 5,56 /
> 3,80 / 5,26. **Un 0,43 por ciento es una caida de un orden de magnitud, y una cifra asi se
> sospecha antes de celebrarla.**
>
> Dos lecturas caben y **no se cual es, porque el reporte no lo he visto**: o el extractor
> transcribe ahora con un aparato de atribucion que antes no usaba, y de hecho lo veo en los
> 241 pasos (*Cuenta con que*, *El libro lo razona con*, y hasta un *el libro no manda nada*
> literal en `establecer_dinamica_nueva_antiguos_pares` paso 7); **o mi vara de hoy es mas
> ancha que la que produjo aquella serie**, y entonces el problema es mio.
>
> **La seccion 8.3 dice que el error que esta metrica invita a cometer es marcar un puente
> como transcripcion, porque baja la cifra y sube el volumen del lote siguiente. Esa es
> exactamente la direccion de mi propio numero, y por eso lo dejo escrito con su vara al lado
> ANTES de ver la suya.** Si la del extractor sale mas alta que la mia, **la reconciliacion no
> la resuelvo copiando la que me convenga**: se resuelve paso a paso y se declara.

**NO FIRMO TODAVIA ESTA CIFRA COMO LA DEL ACTA.** Es mi lectura a ciegas. La del acta sale de
compararla con la suya paso a paso, y si no puedo, **lo digo y no la publico como mia.**

---

## 9. LO QUE ESTA LECTURA ENCUENTRA Y NO ES UN DISCUTIBLE

**El lote de esta vuelta son los HIJOS de un nodo escrito hace dos vueltas, y nadie los ha
conectado.** `gestionar_personas_equipo`, que ya estaba en la bandeja, tiene estos pasos:

    paso 2  Desarrolla relaciones de confianza con ellos.
    paso 3  Entiende las fuerzas y las debilidades de cada uno, y tambien las tuyas.
    paso 4  Toma buenas decisiones sobre quien debe hacer que, y eso incluye contratar y despedir.
    paso 5  Entrena a cada persona para que de lo mejor de si.

**Los cuatro pasos son el indice del Cap. 3 y del Cap. 4.** El 2 apunta a
`ganar_confianza_personas_cargo`, el 3 a `ayudar_personas_jugar_fortalezas`, el 4 al racimo
del despido, y el 5 a los doce de la opinion. **Lo dejo escrito aqui como lectura, no como
encargo**, porque el test de `D.37` lo tengo que correr abriendo el paso de la madre y
comprobando que nombra al hijo, y **lo que esos pasos nombran son asuntos, no nodos.** Es
material de `D.29`, y de la vuelta que lo encargue.

---

## 10. LO QUE NO HE HECHO EN ESTA FASE, DICHO PARA QUE NO SE ME CUENTE COMO HECHO

- **No he corrido `forja.py informe`, ni el gate, ni las 72 pruebas.** Esta fase es lectura.
  Van en el turno normal, y **la cifra de `0 CAERIAN` no la cito hasta recomputarla.**
- **No he verificado las aristas del tramo**, porque los candidatos no las traen escritas y
  viven en el reporte, que no he visto.
- **No he abierto `docs/loop/REPORTE.md` ni lo he recuperado de git**, ni he leido
  `ultimo_extractor.json`.
- **No he tocado ningun candidato ni ningun fichero de `fuentes/`.**
- **No he contado los veredictos ni los sanos**, porque `MODO_INSERCION=cuarentena` y este
  lote no ha pasado por la aduana con veredicto escrito.

**Y ESTE FICHERO NO SE VUELVE A TOCAR.** Lo sella el arnes, y el sello se verifica al terminar
mi turno (`D.34`).
