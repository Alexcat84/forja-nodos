# APERTURA CIEGA DE LA VUELTA 28, **antes de ver el reporte del extractor**

*Escrita por el **auditor** en su fase ciega (`AUDITOR_FORJA.md` `1` punto 5, `D.34`,
`D.34.2`). El arnes ha retirado del arbol `REPORTE.md`, `loop.log`,
`ultimo_extractor.json` y `ultimo_auditor.json`, y **no he recuperado ninguno de los
cuatro, ni de git ni por ninguna otra via.** Lo que si he abierto, porque es obra mia y
`D.40` lo manda, es `docs/loop/ACTA_AUDITOR.md` y mi propio `PROMPT_SIGUIENTE.md`.*

> **LAS DOS REGLAS QUE MANDAN EN ESTE FICHERO, Y LAS APLICO A TODO LO QUE SIGUE**
>
> **`D.38.3`:** toda cifra sale de un instrumento corrido en ESTA fase, con su salida
> literal pegada al lado, **y la frase que la acompania dice lo que el instrumento
> MIDIO.** Toda conclusion sobre contenido va en linea aparte marcada `LECTURA`.
>
> **`D.38.4` y `D.38.5`:** el barrido de vecinos se hace sobre **grafo mas bandejas**,
> uno por vez, con el propio candidato excluido.

---

## 0. LA HERENCIA, DECLARADA ANTES DE NADA (`D.40`)

### **ACTA ANTERIOR LEIDA: `aebb5219006cb8ac6804e37a450c0f7f17498c32`**

### **HEREDADOS: `0`**

**No declaro ningun `NO APLICA`, porque no hay ningun heredado al que aplicarselo.** Aun
asi corro el instrumento y pego su salida:

    $ python forja.py herencia
      acta anterior : ACTA 26. VUELTA 26, lote 4 (scott_radical_candor) INSERTANDO, cap_06 CERRADO ENTERO: ...
      su huella     : aebb5219006cb8ac6804e37a450c0f7f17498c32
      heredados     : 0

      El acta anterior no dejo ninguna tarea bloqueante ni ningun remedio escrito.
      Aun asi tienes que declarar la linea de lectura.

*(salida entera en `.v28/herencia_instrumento_v28.txt`)*

**Y COMPRUEBO LA HUELLA CONTRA EL FICHERO QUE TENGO DELANTE, en vez de copiarla del
prompt** (`AUDITOR_FORJA.md` `1.1`, *el instrumento manda*):

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    aebb5219006cb8ac6804e37a450c0f7f17498c32

    $ git cat-file -s aebb5219006cb8ac6804e37a450c0f7f17498c32   ->  1535094
    $ wc -c docs/loop/ACTA_AUDITOR.md                            ->  1535094

**Coinciden.** La huella que el prompt me entrega es la del acta que he leido, byte a byte.

### 0.1. **Y COMPRUEBO POR QUE SON CERO, en vez de darlo por bueno**

*`0` heredados puede significar dos cosas muy distintas: que el acta anterior no dejo
nada, o que dejo algo donde el instrumento no mira. **Lo mido antes de firmarlo.***

    $ sed -n '23616,24409p' docs/loop/ACTA_AUDITOR.md \
        | grep -nicE "TAREA BLOQUEANTE DEL AUDITOR|^#+ *REMEDIO|REMEDIO PENDIENTE|REMEDIO QUE DEJO"
    0

    $ sed -n '23616,24409p' docs/loop/ACTA_AUDITOR.md | grep -niE "remedio"
    767:> **No encargo el remedio de mi propia caida como tarea bloqueante.** `5.5` manda abrir con el
    768:> remedio el acta siguiente **cuando la racha aun corre**; **cuando la racha se rompe, `3` manda otra
    771:> remedio va escrito en `PARA_ALEXIS.md`, en la seccion de como retomar.

*(salida entera en `.v28/herencia_v28.txt`)*

> **`LECTURA`: los `0` heredados son ciertos y ademas son DELIBERADOS.** La `ACTA 26` `10`
> decidio a proposito **no** dejar tarea bloqueante, porque cerraba en parada y
> `AUDITOR_FORJA.md` `3` manda `PROMPT_SIGUIENTE.md` vacio: *escribir un encargo y una
> parada a la vez seria dejar el bucle corriendo por encima de una parada que nadie ve.*
> **El remedio se escribio en `PARA_ALEXIS.md`**, que es la sede correcta para una parada,
> **y ese fichero ya no existe en el arbol** porque el fundador resolvio lo que pedia:
>
>     $ ls docs/loop/PARA_ALEXIS.md
>     ls: cannot access 'docs/loop/PARA_ALEXIS.md': No such file or directory
>
>     $ git log --oneline -1 -- docs/loop/PARA_ALEXIS.md
>     0cff634 TANDA LIMPIA resuelta para siempre: la parada de la vuelta 26 se disuelve
>             por letra, y la cura se instala igual
>
> **La herencia no se ha perdido: se ha consumido.** El fichero entero esta archivado en
> `docs/loop/paradas/2026-09-16-la-frase-y-el-instrumento-DECISION.md`, con la decision
> del fundador puesta encima y sin tocar una palabra de su cuerpo.

### 0.2. **LAS DOS COSAS QUE PEDI COMO `OBLIGATORIA`, COMPROBADAS UNA POR UNA**

*No son heredados en el sentido de `D.40` (no viajan por el instrumento), pero son mias y
estan escritas, asi que las compruebo aqui en vez de darlas por hechas.*

| lo que pedi | donde | mi comprobacion de hoy |
|---|---|---|
| **`4.1` mi racha**: la reinicia una tanda limpia o una decision escrita, **y ninguna de las dos soy yo** | `PARA_ALEXIS.md` `4.1` | **RESUELTA.** Decision 1 del fundador del 16 sep: `LIMPIA` es *sin caidas de la especie que esa racha acumula*; la `ACTA 25` era limpia; **mi racha recomputa a `1 de 3`** |
| **`4.2` `D.38.5` contra `src/aduana.py`** | `PARA_ALEXIS.md` `4.2` | **CABLEADA.** Ya no es contradiccion. La salida va debajo |

    $ grep -n "poblacion_de_bandejas" src/aduana.py src/informe.py
    src/aduana.py:438:def poblacion_de_bandejas(raiz=None, fecha=None, tabla_fuentes=None):
    src/aduana.py:923:    bandejas = poblacion_de_bandejas(fecha=fecha)
    src/informe.py:98:poblacion_de_bandejas = aduana.poblacion_de_bandejas
    src/informe.py:123:        bandejas = poblacion_de_bandejas(fecha=fecha, tabla_fuentes=tabla_fuentes)

    $ sed -n '923,926p' src/aduana.py
        bandejas = poblacion_de_bandejas(fecha=fecha)
        poblacion = list(nodos) + list(bandejas)
        censo = Poblacion(len(nodos), len(bandejas))
        vecinos = buscar_vecinos(candidato, poblacion, umbrales)

*(salida entera en `.v28/d385_v28.txt`)*

> **`LECTURA`: la linea `923` esta DENTRO del camino de insercion y no del informe en
> seco**, que es exactamente donde mi `ACTA 26` `5` dijo que faltaba (*se cableo en
> `informe.py`, que corre EN SECO, y no aqui, que es donde se decide*). **La contradiccion
> que yo traje como segundo motivo de parada esta cerrada, y no la vuelvo a cobrar.**

### 0.3. **LA CONDICION MECANICA QUE ME PUSE YO, Y QUE CUMPLO EN ESTE FICHERO**

`PARA_ALEXIS.md` `4.1` recomendaba, contra mis dos caidas de la vuelta 26:

> *toda afirmacion universal sobre el dato (`ningun`, `todos`, `cero`) que publique en mi
> apertura o en mi acta se corre como comando sobre el **CONTENIDO** y no sobre los campos,
> con su salida pegada.*

**El fundador la instalo en su forma de `D.38.3` ensanchada** (decision del 16 sep, punto
2.b). **La cumplo en todo lo que sigue**, y la primera que corro es justamente la frase que
me costo la caida:

    $ censo de CONTENIDO sobre dataset/nodos.jsonl: resumen_teorico que nombra un cap_NN
      nodos cuyo resumen_teorico nombra un cap_NN : 38 de 239

    $ los CINCO nodos nuevos de esta vuelta, leidos del GRAFO
      escuchar_callado_equipo_tranquilizar_incomodo      cap_NN=True  punteros_de_linea=True
      escuchar_ruidoso_opinion_fuerte_pedir_agujeros     cap_NN=True  punteros_de_linea=True
      crear_cultura_escucha_equipo                       cap_NN=True  punteros_de_linea=True
      explicar_idea_facil_comprender_oyente              cap_NN=True  punteros_de_linea=True
      centrar_debate_ideas_fuera_egos                    cap_NN=True  punteros_de_linea=True
      dicen de que capitulo salen : 5 de 5
      traen punteros de linea     : 5 de 5

*(salida entera en `.v28/censo_capitulo_v28.txt`)*

> **`LECTURA`: la costumbre de nombrar el capitulo y sus punteros de linea esta puesta en
> los cinco de esta vuelta**, y el censo del grafo entero sube de `33 de 234` (mi cifra de
> la vuelta 26) a `38 de 239`, que son exactamente los cinco nuevos. **La frase falsa que
> publique entonces (*ningun nodo dice de que capitulo sale*) era falsa entonces y lo es
> con mas margen hoy**, y esta vez la digo midiendo el contenido y no los campos.

### 0.4. **UNA CAIDA PROPIA QUE ME CAZO MI PROPIO REMEDIO, Y LA DECLARO AQUI PORQUE PASO AQUI**

*`ACTA 26` `7.1`: *el barrido de guiones estaba en ROJO al empezar mi turno normal y los
ocho hallazgos eran mios.* **Lo corri ANTES de escribir, que es lo que aquella caida
enseñaba, y estaba en rojo otra vez, con trece hallazgos y los trece mios.***

    $ python forja.py guiones        (primera corrida, a mitad de esta fase)
    BARRIDO DE GUIONES EN ROJO: 13 hallazgo(s)
      .v28/pre27/cuarentena/ensayo_referencia_163/...  (9, guion largo U+2014)
      .v28/rotulos_cap07.txt linea 8 columna 8: guion largo (U+2014)
      .v28/rotulos_cap07.txt linea 15 columna 8: guion largo (U+2014)
      .v28/rotulos_cap07.txt linea 36 columna 8: guion largo (U+2014)
      .v28/rotulos_cap07.txt linea 53 columna 8: guion largo (U+2014)

**LOS TRECE ERAN MIOS Y DE ESTA FASE**, y son de dos especies:

- **nueve** venian de `.v28/pre27/`, una extraccion de `git archive` que hice para
  reconstruir la bandeja de la vuelta 27. **Borrada**: era material de usar y tirar, el
  barrido ya esta corrido y su salida guardada, y el comando que la recrea esta pegado
  en `4`.
- **cuatro** venian de `.v28/rotulos_cap07.txt`, que es **salida de instrumento con el
  texto del libro dentro**, y el libro escribe guiones largos. **Regenerado con los
  guiones normalizados y con la normalizacion escrita en su cabecera**, que es lo que
  permite que siga siendo la salida y no una tabla tecleada.

    $ python forja.py guiones        (tras limpiar)
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 239
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada,
               vuelta, cita_incompleta, deprecado_en_superficie, arista_rota,
               arista_incompleta, guiones

*(salida en `.v28/guardas_apertura_v28.txt`)*

> **`LECTURA`: la declaro con mi nombre y la dejo arreglada, no solo dicha.** Es la misma
> especie de la `ACTA 26` `7.1` y la diferencia es el momento: **aquella vez el rojo
> sobrevivio a mi fase ciega y llego a mi turno normal; esta vez lo corri dentro de la
> fase y lo arregle dentro de la fase.** El turno normal decide como se clasifica; lo que
> no puede es encontrarselo.

---

## 1. EL ESTADO, MEDIDO ANTES DE CLASIFICAR NADA

*Todo sale de `.v28/cuentas_v28.txt` y `.v28/aristas_v28.txt`, corridos en esta fase.*

    $ wc -l dataset/nodos.jsonl                                      ->  239
    $ git show 360f941:dataset/nodos.jsonl | wc -l                   ->  234
    $ wc -l bitacora/VEREDICTOS.jsonl                                ->  264
    $ git show 360f941:bitacora/VEREDICTOS.jsonl | wc -l             ->  240
    $ ls cuarentena/scott_radical_candor/*.json | wc -l              ->  106
    $ git ls-tree -r --name-only 360f941 cuarentena/scott_radical_candor/ | grep -c ".json$"   ->  111
    $ ls cuarentena/marquet_turn_the_ship/*.json | wc -l             ->  3
    $ ls cuarentena/_insertados/scott_radical_candor/*.json | wc -l  ->  36
    $ ls cuarentena/_insertados/*/*.json | wc -l                     ->  237
    $ wc -l config/pares_mutuos.jsonl                                ->  1

| medida | al abrir la vuelta 27 (`360f941`) | hoy | movimiento |
|---|---:|---:|---:|
| nodos en el grafo | 234 | **239** | **+5** |
| veredictos en bitacora | 240 | **264** | **+24** |
| bandeja del lote 4 | 111 | **106** | **-5** |
| insertados del lote 4 | 31 | **36** | **+5** |
| ficheros en `_insertados` | 232 | **237** | **+5** |
| bandeja del lote 5 | 3 | **3** | **0** |
| pares mutuos | 1 (solo cabecera) | **1** | **0** |

**La aritmetica cierra sola:** `234 + 5 = 239`; `111 - 5 = 106`; `31 + 5 = 36`;
`232 + 5 = 237`.

### 1.1. Las aristas y los nodos nuevos, por su NOMBRE y no por su numero

    $ python .v28/aristas_v28.py            (salida en .v28/aristas_v28.txt)
    nodos al abrir la v27 : 234
    nodos hoy             : 239
    aristas al abrir v27  : 84
    aristas hoy           : 87
    NUEVAS                : 3
       + aprender_resultados_vencer_dos_presiones > cambiar_posicion_hechos_explicar_cambio
       + decidir_momento_despedir_persona > despedir_persona_franqueza_radical
       + despedir_persona_respeto_franqueza > despedir_persona_franqueza_radical
    RETIRADAS             : 0

    NODOS NUEVOS          : 5
       * escuchar_callado_equipo_tranquilizar_incomodo    (11 pasos)
       * escuchar_ruidoso_opinion_fuerte_pedir_agujeros   (13 pasos)
       * crear_cultura_escucha_equipo                     (17 pasos)
       * explicar_idea_facil_comprender_oyente            (13 pasos)
       * centrar_debate_ideas_fuera_egos                  (10 pasos)

> **`LECTURA`: las TRES aristas nuevas son exactamente las tres que yo encargue** en
> `PROMPT_SIGUIENTE.md` `TAREA 2` (`2.a`, `2.b` y `2.c`), **y la primera de la lista es la
> PRIMERA ARISTA ENTRE DOS LIBROS de esta casa**. **Cero retiradas.** Las tres las
> adjudique en la `ACTA 26` `2.3` y en mi apertura anterior: **no las releo aqui, porque
> releer lo que ya adjudique no es lectura ciega, es repetirme.**

---

## 2. MI CORTE CIEGO DE `cap_07`: QUE PIEZAS DA EL CAPITULO

*Esta es la mitad que no depende de nadie: **abro el libro, lo corto yo, y despues comparo
con lo que el arbol tiene escrito.***

    $ wc -l -w fuentes/scott_radical_candor/cap_07.md
      433 13706 fuentes/scott_radical_candor/cap_07.md

**El fichero se llama `cap_07` y su cabecera dice `unidad: Cap. 4`,
`titulo_textual: Drive Results Collaboratively`.** Es el capitulo de la **rueda de hacer
cosas** (`GSD wheel`), y su esqueleto son siete trabajos: `LISTEN`, `CLARIFY`, `DEBATE`,
`DECIDE`, `PERSUADE`, `EXECUTE` y `LEARN`.

### 2.1. Los rotulos que el libro imprime, sacados con un instrumento

    $ awk 'NR>7 && length($0)>0 && length($0)<75 {printf "L%-4s| %s\n", NR, $0}' \
          fuentes/scott_radical_candor/cap_07.md
      (58 lineas; salida entera en .v28/rotulos_cap07.txt)

**Los siete pasos de la rueda estan en `L79`, `L165`, `L213`, `L259`, `L303`, `L367` y
`L389`**, y debajo de cada uno cuelgan sus sub rotulos.

### 2.2. **MI CORTE, Y DESPUES EL DEL ARBOL**

**Mi lectura da `25` piezas procedimentables en `cap_07`:**

| paso de la rueda | piezas que yo corto | de donde |
|---|---:|---|
| **la cabeza de la rueda** | **1** | `L65`, *The art of getting stuff done without telling people what to do* |
| **`LISTEN`** | **4** | *Quiet listening*, *Loud listening*, *Create a culture of listening*, *Adapt to a culture of listening* |
| **`CLARIFY`** | **2** | *Be clear in your own mind* mas *Create a safe space...*; y *Be clear to others* mas *Make thoughts...* |
| **`DEBATE`** | **5** | seis sub rotulos, **y *Be clear when the debate will end* mas *Don't grab a decision...* van juntos** |
| **`DECIDE`** | **3** | *You're not the decider*, *The decider should get facts*, *Go spelunking* |
| **`PERSUADE`** | **3** | *Emotion*, *Credibility*, *Logic* |
| **`EXECUTE`** | **4** | *Minimize the collaboration tax*, *Don't waste your team's time*, *Keep the dirt under your fingernails*, *Block time to execute* |
| **`LEARN`** | **3** | la cabeza de `LEARN`, *Pressure to be consistent*, *Burnout* |
| | **`25`** | |

**Y esto es lo que el arbol tiene escrito, medido y no leido de su palabra:**

    $ censo de resumen_teorico que cita fuentes/scott_radical_candor/cap_07.md
      (bandeja mas _insertados del lote 4; salida entera en .v28/cap07_piezas.txt)
      total: 25

    $ prueba de solape y de hueco sobre esos 25 tramos
      (salida entera en .v28/cobertura_cap07.txt)
      TRAMOS DECLARADOS : 25
      SOLAPES entre tramos declarados : 0
      LINEAS CON TEXTO FUERA DE TODO TRAMO : 53, en 5 bloques
         L9   a L63   (28 lineas)  | Telling people what to do doesn't work
         L79  a L89   (6 lineas)   | LISTEN
         L165 a L175  (6 lineas)   | CLARIFY
         L213 a L223  (6 lineas)   | DEBATE
         L421 a L433  (7 lineas)   | PART II

> ### **`LECTURA`: MI CORTE Y EL DEL ARBOL COINCIDEN EN LAS `25`, Y LOS CINCO HUECOS ESTAN BIEN DEJADOS**
>
> **Las `25` piezas coinciden una a una, y la particion no se solapa en ni una linea.** Las
> dos decisiones finas que yo tomaria tambien estan tomadas igual: ***Be clear in your own
> mind* y *Create a safe space* van en el mismo nodo** (entre `L181` y `L183` no hay una
> sola linea de texto), y ***Be clear when the debate will end* y *Don't grab a decision*
> van juntos** (`L245` a `L257`), porque la anecdota del plano de mesas es el caso de esa
> misma regla y no de otra.
>
> **Y los `5` bloques que quedan fuera NO son nodos, uno por uno:**
>
> - **`L9` a `L63`**: las dos historias de *telling people what to do didn't work*, en
>   Google y en Apple. **Es relato y argumento, no procedimiento**: no hay ni un acto que
>   nadie ejecute.
> - **`L79` a `L89`, `L165` a `L175`, `L213` a `L223`**: los preambulos de `LISTEN`,
>   `CLARIFY` y `DEBATE`, con sus epigrafes. **Son postura y metafora** (*your job as a
>   boss is to turn on that rock tumbler*), y **su procedimiento esta entero en los sub
>   rotulos de debajo.** `6.1`: *una postura no ejecuta una busqueda; una advertencia es
>   linea.*
> - **`L421` a `L433`**: la portadilla de `PART II` y el titulo del capitulo `5`. **No es
>   material de este capitulo.**
>
> **NO TENGO NADA QUE RECLAMARLE AL CORTE DE `cap_07`.**

---

## 3. LOS CINCO CANDIDATOS DE ESTA VUELTA, CLASIFICADOS POR MI A CIEGAS

*Los cinco que entraron son los `5` que el instrumento de `1.1` nombra. Los he leido
enteros, con su tramo del libro delante, **antes de abrir una sola linea nueva de
`bitacora/VEREDICTOS.jsonl`**.*

| # | candidato | tramo | pasos | **mi clase** | con que la adjudico |
|---:|---|---|---:|---|---|
| **1** | `escuchar_callado_equipo_tranquilizar_incomodo` | `L91`-`L111` | 11 | **SANO** | `6.1`, *dos doctrinas legitimas no son duplicado: son FRONTERA DECLARADA* |
| **2** | `escuchar_ruidoso_opinion_fuerte_pedir_agujeros` | `L113`-`L129` | 13 | **SANO** | la misma frontera, por el otro lado |
| **3** | `crear_cultura_escucha_equipo` | `L131`-`L153` | 17 | **SANO** | `6.1`, *no tiene bascula*: lo que queda fuera es procedimiento en los dos lados |
| **4** | `explicar_idea_facil_comprender_oyente` | `L197`-`L211` | 13 | **SANO** | `6.1`, direccion y procedimiento propio |
| **5** | `centrar_debate_ideas_fuera_egos` | `L225`-`L229` | 10 | **SANO** | `6.1`, tecnica con sus disparadores escritos |

**LOS CINCO SANOS. Cero fusiones, cero deprecaciones, cero mutuos.** Debajo van los que
cuestan explicacion, porque adjudicar sin escribir el razonamiento no es adjudicar.

### 3.1. `1` contra `2`: **la frontera que el libro declara el mismo**

**No son duplicados y el propio libro lo dice por escrito.** `L115` abre la segunda
definiendola por contraste con la primera: *If quiet listening involves being silent to
give people room to talk, loud listening is about saying things intended to get a reaction
out of them.* Y `L129` cierra la seccion entera con la regla que las separa: *Perhaps most
important is to stick to the style that feels most natural to you.*

**Lo que queda fuera es procedimiento en los dos lados**, que es lo que `6.1` manda mirar:

| | callado | ruidoso |
|---|---|---|
| **el acto** | diez minutos de silencio con cara y cuerpo neutros en cada `1:1` | poner un punto de vista fuerte encima de la mesa y pedir agujeros |
| **su coste declarado** | **tres**, inventariados uno a uno en `L107` | **uno**: el que no se atreve a devolver el golpe |
| **la compensacion** | decir lo que piensas de vez en cuando; no ser inescrutable sin motivo | construir la confianza del que no se atreve; nombrar tu mismo el defecto de tu idea |

**Son `FRONTERA DECLARADA` y no duplicado.** `6.1`: *una frontera se pierde por poda, no
por fusion.*

**Y NO LES PONGO ARISTA ENTRE ELLOS, y digo por que:** `D.29` pide que la madre **NOMBRE**
una parte y el hijo la **PROCEDIMENTE**. `L115` nombra la escucha callada **para
contrastarla**, no para delegar en ella. **Son hermanos de la misma cabeza, no madre e
hijo.**

### 3.2. `3` contra `crear_espacio_seguro_madurar_ideas_nuevas`, **que sigue en la bandeja**

**Es el par que mas cerca esta de ser un gemelo en esta vuelta, y por eso lo leo entero.**
Los dos hablan de ideas nuevas del equipo; **los dos tienen procedimiento propio y ninguno
se come al otro:**

| | `crear_cultura_escucha_equipo` (`L131`) | `crear_espacio_seguro...` (`L177`) |
|---|---|---|
| **paso de la rueda** | `LISTEN` | `CLARIFY` |
| **a quien mira** | a que el equipo **se escuche entre si** | a que **una idea** madure antes del debate |
| **el acto** | un sistema de ideas y quejas con sus tres claves, un equipo de ideas con sus tres compromisos, la vuelta a la mesa en reunion | la reunion previa de Susan Wojcicki, el *plussing* de Pixar, el `1:1` como sitio seguro |
| **lo que queda fuera del otro** | el *plussing*, la reunion previa, el no juzgar en el `1:1` | el sistema, el equipo de ideas, el caso de los teclados de Sarah Teng |

**SANO los dos.** El solape de tema es grande y el de procedimiento es **cero**, que es lo
que `6.1` manda mirar: *el tamaño del solape no decide.*

### 3.3. `4` contra `compartir_logica_mostrar_razonamiento`, **que tambien sigue en la bandeja**

Los dos van de que tu razonamiento llegue, **y otra vez el acto es distinto:**
`explicar_idea` (`L197`, paso `CLARIFY`) manda **conocer al oyente** y elegir que
seleccionas, que eliminas y que subrayas **en funcion del publico**; `compartir_logica`
(`L359`, paso `PERSUADE`) manda **enseñar tus operaciones**, compartir **como llegaste** a
la idea y no solo la idea. **Uno ajusta al oyente, el otro destapa la derivacion.** SANO
los dos.

### 3.4. `5` contra los otros cuatro de `DEBATE`

`centrar_debate_ideas_fuera_egos` (`L225`) convive con `crear_obligacion_disentir_equipo`
(`L231`, bandeja), `parar_debate_emocion_agotamiento` (`L235`, bandeja),
`abrir_debate_humor_explicar_proposito` (`L239`, **ya en el grafo**) y
`fijar_fecha_cierre_debate_equipo` (`L245`, bandeja). **Son cinco tecnicas del mismo paso
de la rueda, con cinco disparadores distintos y cinco actos distintos**, y el libro imprime
su propio rotulo para cada una. **SANO.**

**Lo que hace que esto sea procedimiento y no postura, y lo digo porque es la prueba que
`6.1` pide:** `L227` **nombra los disparadores con sus palabras exactas** (*I'm going to
win this argument*, *my idea versus your idea*, *my recommendation versus your
recommendation*, *my team feels...*). **Hay un acto que ejecutar y una señal escrita para
ejecutarlo.**

---

## 4. EL BARRIDO DE VECINOS (`D.38.4`), SOBRE GRAFO MAS BANDEJAS Y UNO POR VEZ

*La poblacion es la que el extractor tuvo delante: el grafo y las bandejas **tal como
estaban al abrir la vuelta 27** (`360f941`), **menos el propio candidato** (correccion de
la `ACTA 18`: un nodo no es vecino de si mismo). El instrumento es
`src.aduana.buscar_vecinos`, con `config/umbrales.json` sin tocar.*

**Los dos comandos que reconstruyen la poblacion, para que esto se pueda repetir:**

    $ git show 360f941:dataset/nodos.jsonl > .v28/grafo_pre27.jsonl     ->  234 lineas
    $ mkdir -p .v28/pre27 && git archive 360f941 cuarentena | tar -x -C .v28/pre27

> **`.v28/grafo_pre27.jsonl` SI ESTA en el arbol y `.v28/pre27/` NO, y lo digo aqui para no
> publicar una ruta que no sostiene nada** (`D.42`, cosecha `7.B`). La segunda la borre a
> mitad de esta fase porque metia nueve guiones largos en el barrido (`0.4`); **el comando
> de arriba la recrea entera y el barrido ya esta corrido con ella dentro.**

**Y el barrido** (`python .v28/barrido_v28.py <los cinco candidatos>`, salida entera en
`.v28/barrido_v28.txt`):

    poblacion del barrido       : 348   (234 del grafo mas 114 que esperan en bandejas)

    ==============================================================================
    CANDIDATO : crear_cultura_escucha_equipo
    pasos     : 17
    barrido contra 347 (la poblacion menos el propio candidato)
    VECINOS QUE SUPERAN UMBRAL : 4
       - crear_obligacion_disentir_equipo                         [familia_id=0.333]
       - adaptar_escucha_cultura_ajena                            [familia_id=0.333]
       - juzgar_cultura_renuncias_equipo                          [familia_id=0.333]
       - crear_plan_creible_equipo                                [familia_id=0.333]
    ==============================================================================
    CANDIDATO : escuchar_callado_equipo_tranquilizar_incomodo
    pasos     : 11
    VECINOS QUE SUPERAN UMBRAL : 0
       (ninguno)
    ==============================================================================
    CANDIDATO : escuchar_ruidoso_opinion_fuerte_pedir_agujeros
    pasos     : 13
    VECINOS QUE SUPERAN UMBRAL : 0
       (ninguno)
    ==============================================================================
    CANDIDATO : centrar_debate_ideas_fuera_egos
    pasos     : 10
    VECINOS QUE SUPERAN UMBRAL : 8
       - rechazar_candidato_razones_relevantes                    [paso_contra_nodo=0.607]
       - fijar_fecha_cierre_debate_equipo                         [similitud_texto=0.372]
       - bajar_detalle_organizacion_fuente_hechos                 [similitud_texto=0.356]
       - mantener_manos_trabajo_real_equipo                       [similitud_texto=0.354]
       - compartir_logica_mostrar_razonamiento                    [similitud_texto=0.369]
       - parar_debate_emocion_agotamiento                         [similitud_texto=0.36]
       - proteger_tiempo_equipo_jefe                              [similitud_texto=0.357]
       - minimizar_impuesto_colaboracion_equipo                   [similitud_texto=0.369]
    ==============================================================================
    CANDIDATO : explicar_idea_facil_comprender_oyente
    pasos     : 13
    VECINOS QUE SUPERAN UMBRAL : 1
       - compartir_logica_mostrar_razonamiento                    [similitud_texto=0.37]
    ==============================================================================

**MI CIFRA DE PARES: `4 + 0 + 0 + 8 + 1 = 13`.** Y la poblacion va con su reparto, como
`D.38.3` pide: **`348`, que son `234` del grafo mas `114` que esperaban en bandejas.**

### 4.1. Los trece pares, adjudicados uno a uno

| # | par | señal que lo levanto | **mi clase** | por que |
|---:|---|---|---|---|
| 1 | `crear_cultura` vs `crear_obligacion_disentir_equipo` | `familia_id` 0.333 | **SANO** | dos tecnicas de dos pasos distintos de la rueda; comparten `crear` y `equipo` en el id y nada mas |
| 2 | `crear_cultura` vs `adaptar_escucha_cultura_ajena` | `familia_id` 0.333 | **SANO** | hermanos de `LISTEN`: uno monta un sistema en tu casa, el otro se adapta a una casa ajena |
| 3 | `crear_cultura` vs `juzgar_cultura_renuncias_equipo` | `familia_id` 0.333 | **SANO** | el de `zhuo_manager` **juzga** una cultura por lo que cede; este **monta** un sistema de escucha |
| 4 | `crear_cultura` vs `crear_plan_creible_equipo` | `familia_id` 0.333 | **SANO** | estrategia contra escucha. No se tocan en ni un paso |
| 5 | `centrar_debate` vs `rechazar_candidato_razones_relevantes` | `paso_contra_nodo` **0.607** | **SANO** | ver `4.2` |
| 6 | `centrar_debate` vs `fijar_fecha_cierre_debate_equipo` | `similitud_texto` 0.372 | **SANO, Y CON ARISTA `D.29` PENDIENTE** | ver `4.3` |
| 7 | `centrar_debate` vs `bajar_detalle_organizacion_fuente_hechos` | 0.356 | **SANO** | `DECIDE` contra `DEBATE`: ir a la fuente del hecho no es sacar el ego del debate |
| 8 | `centrar_debate` vs `mantener_manos_trabajo_real_equipo` | 0.354 | **SANO** | `EXECUTE`. Ningun acto en comun |
| 9 | `centrar_debate` vs `compartir_logica_mostrar_razonamiento` | 0.369 | **SANO** | `PERSUADE`. Ningun acto en comun |
| 10 | `centrar_debate` vs `parar_debate_emocion_agotamiento` | 0.36 | **SANO** | hermanos de `DEBATE` con disparador distinto: **ego** contra **agotamiento** |
| 11 | `centrar_debate` vs `proteger_tiempo_equipo_jefe` | 0.357 | **SANO** | `EXECUTE`. Ningun acto en comun |
| 12 | `centrar_debate` vs `minimizar_impuesto_colaboracion_equipo` | 0.369 | **SANO** | `EXECUTE`. Ningun acto en comun |
| 13 | `explicar_idea` vs `compartir_logica_mostrar_razonamiento` | 0.37 | **SANO** | razonado en `3.3` |

> **`LECTURA`: los siete pares de `similitud_texto` entre `0,354` y `0,372` son el mismo
> fenomeno, y tiene nombre.** Son **todos hermanos del mismo capitulo**, escritos por la
> misma mano, con el mismo vocabulario (*el texto dice que*, *cuenta con que*, *tu equipo*)
> y la misma forma de paso. **La señal no esta midiendo parentesco: esta midiendo estilo de
> redaccion de un capitulo.** No pido mover el umbral (`2`: los umbrales son de Alexis), y
> lo dejo escrito como dato: **el umbral de `0,35` produce cola falsa dentro de un mismo
> capitulo largo**, y `D.19` ya tiene escrito que ninguna señal separa jerarquia de ruido.

### 4.2. **El unico par que paso el umbral fuerte, y es ruido: `0,607` de `paso_contra_nodo`**

**Es el vecino mas fuerte de los trece y viene de otro libro** (`smart_who`,
`rechazar_candidato_razones_relevantes`). **Imprimi los pasos de los dos antes de decidir:**

| | `centrar_debate_ideas_fuera_egos` | `rechazar_candidato_razones_relevantes` |
|---|---|---|
| **cuando se activa** | notas *voy a ganar esta discusion* en un debate de tu equipo | vas a descartar a un candidato y tienes que decir por que |
| **que entrega** | un debate de vuelta sobre los hechos, sin propietarios de ideas | un rechazo sostenido sobre hechos de la tarjeta de puntuacion |
| **lo que la señal vio** | `P2` *redirigelos a centrarse en los hechos*, `P4` *no dejes que lo secuestre como puedan sentirse* | `P4` *atente a los hechos*, `P5` *excluye los asuntos y los sentimientos irrelevantes* |

**SANO.** La señal se levanto sobre **dos pasos que dicen *hechos si, sentimientos
irrelevantes no***, que es una frase que aparece en las dos partes por motivos
completamente distintos. **`D.19` manda: una discrepancia NUNCA se adjudica citando una
señal; la señal dijo donde mirar y ahi acabo su trabajo.** Mire, y el resto del par no se
toca en nada: ni la condicion de activacion, ni el entregable, ni el dominio, ni un solo
acto.

### 4.3. **LA ARISTA QUE MI LECTURA LEVANTA Y QUE NINGUNA SEÑAL DECLARA COMO TAL**

**`fijar_fecha_cierre_debate_equipo` (`L245`-`L257`, EN BANDEJA) es MADRE de
`centrar_debate_ideas_fuera_egos` (`L225`-`L229`, YA EN EL GRAFO), por `D.29`.**

**La madre NOMBRA el acto y no lo procedimenta.** Su `P10`:

> *O sugiere que cambien de papel y defienda cada uno la posicion del otro.*

y el libro lo escribe en `L257`, **dentro de una lista de sugerencias abierta con *For
example***: *...or that they switch roles and argue for each other's positions.*

**El hijo lo PROCEDIMENTA, y trae procedimiento propio que la madre no tiene** (`P.5.1`,
*nombrar no es procedimentar*). Sus `P9` y `P10`:

> *Si alguien lleva rato defendiendo A, pidele que empiece a defender B.*
> *Si el debate va a durar un rato, avisales de antemano de que les vas a pedir que cambien
> de papel*, con la razon escrita en `L229`: cuando la gente sabe que va a tener que
> defender el punto de vista de otro, **escucha con mas atencion de forma natural**.

**El aviso previo y su motivo son del hijo y solo del hijo.** Eso es exactamente la figura
de `D.29`: la madre nombra la parte, el hijo la ejecuta y añade.

**ES `D.29` Y NO `D.37`, y lo digo con el instrumento delante**, porque `D.37` exige que la
cabeza diga **cuantas** partes hay:

    $ sed -n '245,257p' fuentes/scott_radical_candor/cap_07.md \
        | grep -ciE "two ways|three ways|four|both ways|these two"
    0

    $ grep -n "switch roles" fuentes/scott_radical_candor/cap_07.md
    229:Another way to help people search for the best answer instead of seeking ego validation
        is to make them switch roles. If a person has been arguing for A, ask them to start
        arguing for B. ...
    257:The right thing to do would have been to set a "decide by" date ... For example, I could
        have suggested the people whose differences he was having a hard time reconciling try
        to wrap it up over a meal or a walk, or that they switch roles and argue for each
        other's positions. ...

*(salida en `.v28/madre_sin_cuenta_v28.txt`)*

**La madre no publica ninguna cuenta de sus sugerencias: las abre con *For example* y las
encadena con *or*.** Sin cuenta no hay `D.37`.

**NO SE PUEDE CABLEAR HOY**, y esa es la mitad que importa: **la madre esta en la bandeja y
el hijo ya vive en el grafo**, asi que la arista va al reves del orden que `D.29` manda
(*la madre entra primero*). **Queda declarada aqui para que no se pierda**, que es
literalmente lo que `D.29` dice que pasa con una arista que solo vive en prosa.

---

## 5. **LO QUE LEVANTO Y NO ES UN PAR: LA CABEZA DE LA RUEDA SE QUEDO FUERA Y SUS PARTES SIGUEN ENTRANDO**

*Esto no sale del barrido de vecinos: sale de mirar el capitulo entero. **Y es lo unico de
esta apertura que traigo como hallazgo y no como confirmacion.***

    $ python .v28/rueda_v28.py         (salida en .v28/rueda_v28.txt)
    CABEZA DE LA RUEDA : recorrer_rueda_hacer_cosas_equipo
      vive en el grafo : False
      piezas de cap_07 que NO son la cabeza : 24
      de ellas, YA EN EL GRAFO             : 10
      de ellas, aun en bandeja             : 14

    ARISTAS EN EL GRAFO QUE TOCAN A LA CABEZA : 0

    LAS PIEZAS DE cap_07 YA EN EL GRAFO, CON SUS ARISTAS:
       L91   escuchar_callado_equipo_tranquilizar_incomodo    previos=[] siguientes=[]
       L113  escuchar_ruidoso_opinion_fuerte_pedir_agujeros   previos=[] siguientes=[]
       L131  crear_cultura_escucha_equipo                     previos=[] siguientes=[]
       L155  adaptar_escucha_cultura_ajena                    previos=[] siguientes=[]
       L197  explicar_idea_facil_comprender_oyente            previos=[] siguientes=[]
       L225  centrar_debate_ideas_fuera_egos                  previos=[] siguientes=[]
       L239  abrir_debate_humor_explicar_proposito            previos=[] siguientes=[]
       L295  bajar_detalle_organizacion_fuente_hechos         previos=[] siguientes=[]
       L389  aprender_resultados_vencer_dos_presiones         previos=[] siguientes=['cambiar_posicion_hechos_explicar_cambio']
       L403  cambiar_posicion_hechos_explicar_cambio          previos=['aprender_resultados_vencer_dos_presiones'] siguientes=[]

### 5.1. Lo que yo encargue, escrito en mi sede y citable

`PROMPT_SIGUIENTE.md` `TAREA 3`, en su propio recuadro:

> **`recorrer_rueda_hacer_cosas_equipo` se inserta ANTES que sus partes** (propuesta `2`
> del extractor en `T.6`, adjudicada): sus tres partes estan en la bandeja, y **si entran
> antes que la cabeza, sus aristas `D.37` no las va a poder cablear la aduana.**

> ### **`LECTURA`: LA CABEZA SIGUE FUERA, `10` DE SUS `24` PARTES ESTAN DENTRO, Y `5` DE ESAS `10` ENTRARON EN ESTA MISMA VUELTA**
>
> `recorrer_rueda_hacer_cosas_equipo` **no vive en el grafo**, **cero aristas lo tocan**, y
> **ocho de las diez partes suyas que ya viven no tienen ni una arista.** Las dos que si la
> tienen se apuntan la una a la otra y no a la cabeza.
>
> **Las `10` partes reparten asi entre los pasos que la cabeza nombra:** `P2` escuchar
> (`4`), `P3` clarificar (`1`), `P4` debatir (`2`), `P5` decidir (`1`), `P8` aprender (`2`).
> **`P6` persuadir y `P7` ejecutar no tienen todavia ninguna parte dentro.**
>
> **Son `10` aristas `D.29` pendientes, y `5` se volvieron pendientes en esta vuelta.**

### 5.2. **Y UNA CAIDA PROPIA MIA DENTRO DEL MISMO ASUNTO: CITE `D.37` DONDE EL BANCO DICE `D.29`**

**Mi encargo dice *sus aristas `D.37`*. No son `D.37`. Son `D.29`**, y el propio fichero
del candidato ya lo habia argumentado antes de que yo escribiera, en su `resumen_teorico`:

> *ESTO NO ES UNA SERIE `D.37` Y LO DIGO ANTES DE QUE SE CUENTE MAL: el texto enumera los
> siete trabajos pero NO dice cuantos son, y la linea 75 escribe literalmente `that is a
> lot of steps`.*

**Lo compruebo contra el libro en vez de creerle:**

    $ sed -n '65,77p' fuentes/scott_radical_candor/cap_07.md | grep -oiE "seven|a lot of steps"
    a lot of steps

    $ sed -n '75p' fuentes/scott_radical_candor/cap_07.md | cut -c1-40
    That's a lot of steps. Remember, they a

**Y `D.37` corregida el 11 sep no deja margen:** *dice **cuantas** partes hay **y las
nombra*** va a `D.37`; ***solo enumera** sin decir cuantas* va a **`D.29`, con razon
escrita**. `L73` nombra los siete trabajos; `L75` se niega a contarlos.

> **`LECTURA`: la sustancia de mi encargo era correcta y la regla que la sostiene la cite
> mal.** *La madre entra primero* **es letra literal de `D.29`**, no de `D.37`, asi que el
> encargo pedia lo que hay que pedir apoyandose en la regla equivocada. **La cita venia de
> la propuesta `2` del extractor, que adjudique sin contrastarla contra el
> `resumen_teorico` del propio candidato, que la traia ya resuelta y en contra.** La misma
> cita esta repetida en `PARA_ALEXIS.md` `4.3.6`, hoy archivado. **Las dos son sede mia**
> (`5.6`), **y las dos las declaro yo aqui antes de ver el reporte.**

---

## 6. LA FIDELIDAD `D.30`, RELEIDA PASO A PASO CONTRA SU PARRAFO

*`8.3`: la cifra de `PASOS INVENTADOS` es una cifra que yo firmo, asi que cuento yo los
pasos y releo yo los marcados `TRANSCRIPCION` contra su linea.*

    $ punteros de linea citados en el resumen_teorico de los CINCO, extraidos con regex
      y comprobados contra el fichero fuente
      pasos escritos en los cinco        : 64
      punteros de linea distintos citados: 29
      L91, L101, L105, L107, L109, L113, L115, L117, L119, L125, L129, L131, L133, L135,
      L137, L139, L145, L147, L153, L197, L199, L203, L205, L207, L209, L211, L225, L227, L229
      punteros que caen en linea VACIA o fuera del fichero: 0

*(salida en `.v28/punteros_v28.txt`)*

**El instrumento mide `64` pasos escritos y `29` punteros de linea distintos, y ninguno de
los `29` cae en linea vacia ni fuera del fichero.** Los tramos declarados (`L91`-`L111`,
`L113`-`L129`, `L131`-`L153`, `L197`-`L211`, `L225`-`L229`) los comprobe ademas uno a uno
con `sed` contra su rotulo, y **los cinco abren donde dicen abrir.**

> ### **`LECTURA`: `64` pasos, `64` `TRANSCRIPCION`, `0` `PUENTE`. `cap_07` da `0,00` por ciento de pasos inventados en esta tanda**
>
> **Los cuatro que mas mire, porque son los que invitan a inventar:**
>
> - **`crear_cultura` `P7`, *define unos limites claros de cuanto tiempo puedes dedicarle***:
>   es la especie del **PERIODO**, que esta casa paga cara. **No es puente:** `L133` escribe
>   *Define clear boundaries of how much time you can spend*, **y no escribe cuanto**, que
>   es justo lo que habria habido que inventar y no se invento.
> - **`escuchar_callado` `P1`, *reserva al menos diez minutos***: el libro lo cuenta como lo
>   que **hizo un alumno** (`L101`), no como una orden. **Convertir un acto relatado en un
>   acto ejecutable es lo que hace la extraccion entera**, y el nodo lo declara en su
>   `resumen_teorico` en vez de disimularlo. **`TRANSCRIPCION`**: los diez minutos y la cara
>   neutra estan escritos, no puestos.
> - **`escuchar_ruidoso` `P9`**, la peticion de agujeros, es **cita literal** de `L125`
>   (*Please poke holes in this idea, I know it may be terrible...*).
> - **`centrar_debate` `P1`**, los cuatro disparadores, es **cita literal** de `L227`.
>
> **Y UNA OMISION QUE NO ES PUENTE PERO QUE DEJO ESCRITA:** `L153` inventaria **tres**
> maneras de repartir la palabra en una reunion, y `crear_cultura` recoge **dos** (`P16` la
> vuelta a la mesa, `P17` la conversacion previa). **La tercera, *ponerse de pie y pasear
> bloqueando fisicamente al que habla de mas*, no esta en ningun paso.** No es puente (no
> se invento nada) y no es caida de clase (el nodo sigue siendo el mismo nodo): **es una
> linea del libro que no llego, y la traigo al turno normal.**

---

## 7. LO QUE TRAIGO AL TURNO NORMAL, SIN HABER DESTAPADO NADA

| # | lo que traigo | de donde sale |
|---:|---|---|
| **1** | **la cabeza de la rueda sigue fuera y `5` partes mas entraron sin ella**, con `10` aristas `D.29` pendientes y `0` aristas tocandola | `5`, medido |
| **2** | **`fijar_fecha_cierre_debate_equipo` es MADRE de `centrar_debate_ideas_fuera_egos` por `D.29`**, y la madre esta en la bandeja mientras el hijo ya vive | `4.3`, leido |
| **3** | **cite `D.37` donde el banco dice `D.29`**, en mi propio encargo y en mi propio `PARA_ALEXIS.md` | `5.2`, caida propia |
| **4** | **el barrido de guiones estaba en ROJO a mitad de mi fase ciega con `13` hallazgos mios**, corrido y arreglado dentro de la fase | `0.4`, caida propia |
| **5** | **mis `13` pares**, para cruzarlos contra los que el reporte diga | `4`, medido |
| **6** | **la tercera manera de `L153` no llego a ningun paso** | `6`, leido |
| **7** | **el umbral de `0,35` produce cola falsa entre hermanos del mismo capitulo**: `7` de mis `13` pares son eso. **No pido moverlo** (`2`) | `4.1`, dato |
| **8** | **`P6` persuadir y `P7` ejecutar de la rueda no tienen todavia ninguna parte dentro** | `5.1`, medido |

**Y UNA COSA QUE ME ENCARGO A MI MISMO PARA EL TURNO NORMAL, porque `PARA_ALEXIS.md` `5`
punto 3 la pide y el instrumento de `D.40` no la entrega:** *el acta que retome cita ese
fichero por su nombre y dice en que queda cada racha y por que*. **El fichero es
`docs/loop/paradas/2026-09-16-la-frase-y-el-instrumento-DECISION.md`.**

---

## 8. ESTA APERTURA, EN UNA TABLA

| | |
|---|---|
| **acta anterior leida** | **`aebb5219006cb8ac6804e37a450c0f7f17498c32`**, huella reproducida con `git hash-object` y confirmada por tamaño |
| **heredados** | **`0`**, con el instrumento pegado **y comprobado el motivo** (`0.1`) |
| **`NO APLICA` declarados** | **`0`.** No hay ninguno al que aplicarselo |
| **piezas de `cap_07` en mi corte ciego** | **`25`**, y el arbol declara **`25`**, con **`0` solapes** y `5` bloques fuera que no son nodos |
| **candidatos clasificados por mi** | **`5`**, los cinco que entraron. **`5` SANO, `0` fusiones, `0` mutuos** |
| **poblacion de mi barrido** | **`348`**, que son **`234` del grafo mas `114` en bandejas** (`D.38.4`, uno por vez) |
| **pares que levanto mi barrido** | **`13`**, adjudicados los trece (`4.1`) |
| **pares con señal fuerte** | **`1`** (`paso_contra_nodo` `0,607`), **adjudicado SANO leyendo los pasos y no la señal** (`D.19`) |
| **aristas que mi lectura levanta y la señal no** | **`1`**: `fijar_fecha_cierre_debate_equipo > centrar_debate_ideas_fuera_egos`, `D.29`, **no cableable hoy** |
| **aristas nuevas en el grafo** | **`3`**, las tres que yo encargue, **`0` retiradas** |
| **pasos releidos contra su parrafo** | **`64` de `64`**, con **`29` punteros de linea comprobados y `0` caidos en vacio**. **`0` PUENTE** en mi lectura |
| **caidas propias que declaro en esta fase** | **`2`**: `D.37` por `D.29` en mi sede (`5.2`), y el barrido de guiones en rojo con `13` hallazgos mios (`0.4`, arreglado dentro de la fase) |
| **guardas al cerrar la fase** | `gate` **VERDE** (239 nodos, 12 guardas), `guiones` **VERDE** |
| **lo que NO he hecho** | no he abierto `REPORTE.md`, `loop.log`, `ultimo_extractor.json` ni `ultimo_auditor.json`, **ni los he recuperado de git**; no he leido ninguna linea nueva de `bitacora/VEREDICTOS.jsonl` antes de clasificar; **y no he commiteado nada** |

    ACTA ANTERIOR LEIDA: aebb5219006cb8ac6804e37a450c0f7f17498c32
    HEREDADOS: 0
