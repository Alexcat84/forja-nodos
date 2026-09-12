# APERTURA CIEGA DE LA VUELTA 21, lote 4 (`scott_radical_candor`)

*Escrita por el **auditor** antes de ver `docs/loop/REPORTE.md`, que no esta en el arbol.
`AUDITOR_FORJA.md` 1.5 (`D.34`), `D.38.3`, `D.38.4` y `D.40`.*

**LO QUE ESTA FASE PUBLICA SON CLASES Y LECTURAS. Toda cifra que aparece abajo lleva pegado el
instrumento que la saco y su salida literal**, y toda cifra lleva su denominador en la misma
frase. **Ninguna sale de contar a ojo.**

---

## 0. LA HERENCIA, QUE ES LO PRIMERO (`D.40`)

    ACTA ANTERIOR LEIDA: 2d794fc9231cf3f28b519f720e4d10cc48a1c4e3
    HEREDADO 1: CUMPLIDO

### 0.1. La huella, remedida por mi en esta fase y no copiada del prompt

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    2d794fc9231cf3f28b519f720e4d10cc48a1c4e3
    $ wc -l docs/loop/ACTA_AUDITOR.md
    18132 docs/loop/ACTA_AUDITOR.md

**Coincide con la que el prompt me entrega.** La lei, y lei ademas `docs/loop/PROMPT_SIGUIENTE.md`
entero, que es sede mia por `AUDITOR_FORJA.md` 5.6 y donde vive el encargo de esta vuelta.

### 0.2. `HEREDADO 1`, que es la `ACTA 19` `7.5` (linea 17998), **CUMPLIDO**

El heredado no es un remedio suelto: es **la obligacion de declarar mis remedios tambien cuando
aguantan**, porque `REMEDIO ROTO` solo informa si se declara en los dos sentidos. **Su cumplimiento
es la seccion 6 de este fichero**, con una fila por remedio y su comprobacion de hoy al lado.

### 0.3. Y DECLARO ADEMAS LO QUE EL ARNES NO ME ENTREGO, porque tambien es mio

El arnes me entrego **un** heredado. **Mi `ACTA 19` `7.4` dejo ademas dos ordenes escritas bajo el
titulo `TAREA BLOQUEANTE DEL AUDITOR DE LA VUELTA 20`**, y no declararlas por no venir numeradas
en el prompt seria exactamente la perdida que `D.40` vino a impedir. **Las dos, y las dos
CUMPLIDAS en este fichero:**

| orden mia de la `ACTA 19` `7.4` | donde se cumple aqui | resultado |
|---|---|---|
| **ORDEN A**, toda tabla de reparto lleva su fila de residuo, y la fila de residuo es **cero o trae nombres** | seccion `1.2`: la fila `SIN` da **0** sobre `83`, y los `39` del nivel 2 salen **impresos con su nombre uno a uno** | **CUMPLIDA** |
| **ORDEN B**, el rotulo de una tabla se escribe **despues** del instrumento y con el codigo delante | seccion `1.1`: mi primer censo **reprodujo la caida de la `ACTA 19` `7.1`** (`cap_04: 5`, `SIN: 1`), la cace **antes de publicar** y reescribi el instrumento; la fila buena es `cap_04: 6, 48 pasos` y `SIN: 0` | **CUMPLIDA, y es la que evito la caida** |

---

## 0.bis. CONTAMINACION DE ESTA FASE, DECLARADA ENTERA Y ANTES DE NADA

**El prompt que me invoca trae, en su bloque de contexto de git, los asuntos de commit del
extractor de esta vuelta**, y uno de ellos resume el resultado de la vuelta con sus cifras. **No
lo busque yo: venia puesto.** Lo digo entero porque es la **tercera vuelta seguida** que la puerta
de `git log` me ensucia la fase ciega, y las dos anteriores la falta si fue mia.

**QUE HAGO CON ELLO:** todo lo que este fichero publica esta **remedido por mi desde el arbol**
con el instrumento pegado al lado, y **ninguna cifra de aqui sale de esa cabecera**. Donde mi
medida coincide con lo que aquel asunto decia, lo digo (`2.1`), porque callarlo seria peor que
declararlo.

**LO QUE NO HICE:** no corri `git log`, `git show` ni `git checkout` sobre `REPORTE.md`,
`loop.log`, `ultimo_extractor.json` ni `ultimo_auditor.json`. **Y no abri los directorios de
trabajo del extractor de esta vuelta** (`.aduana_v20/`, `.barrido_v20/`, `.t1_v20/`): no son
ninguno de los cuatro que `D.34.2` retira, pero **son su lectura**, y esta fase existe para que yo
escriba la mia antes. Su existencia la vi en un `ls` del raiz y ahi la deje.

---

## 1. LA POBLACION, MEDIDA ANTES DE CLASIFICAR NADA

### 1.1. Mi instrumento fallo primero, y lo cuento porque es la ORDEN B funcionando

Mi primera version del censo buscaba `cap_NN.md` **solo dentro de `resumen_teorico`** y publico:

    cap_04	candidatos=5	pasos=41
    SIN	candidatos=1	pasos=7

**Es la misma fila falsa que me costo la caida de la `ACTA 19` `7.1`.** La cace leyendo el rotulo
contra el codigo **antes de publicar**, que es lo que la ORDEN B manda. El fichero en disputa
vuelve a ser `invitar_desafio_reciproco_equipo`, que nombra `cap_04` en su prosa y no lleva la
cabecera `UNIDAD DE ORIGEN:`.

**Y probe tambien el extremo contrario** (buscar `cap_NN` en el fichero entero, sin niveles): da
`CHOQUE:cap_05+cap_06+cap_07+cap_08+cap_09` y otras trece filas de choque, **porque un candidato
que cita a un vecino de otro capitulo nombra dos**. Los dos extremos mienten; por eso el
instrumento bueno declara **por que nivel responde cada fila**.

**EL INSTRUMENTO QUE PUBLICO ES `.censo_apertura_v21.py`:** nivel 1, la cabecera textual
`UNIDAD DE ORIGEN: .../cap_NN.md`; nivel 2, si no la hay, el primer `cap_NN` del fichero entero,
**marcado como deducido y no declarado**.

### 1.2. El censo de la bandeja del lote 4, con su residuo en cero

    $ python .censo_apertura_v21.py
    --- POR CAPITULO (bandeja entera del lote 4) ---
    cap_01	candidatos=1	pasos=9
    cap_03	candidatos=1	pasos=7
    cap_04	candidatos=6	pasos=48
    cap_05	candidatos=8	pasos=76
    cap_06	candidatos=10	pasos=117
    cap_07	candidatos=25	pasos=225
    cap_08	candidatos=12	pasos=102
    cap_09	candidatos=20	pasos=272
    TOTAL	candidatos=83	pasos=856

    --- NIVEL QUE RESPONDIO ---
    nivel 1	44
    nivel 2	39

**NO HAY FILA `SIN`: el residuo es `0` sobre `83`, y los `39` del nivel 2 salen impresos con su
nombre uno a uno en la salida del instrumento**, que es lo que la ORDEN A exige. **83 candidatos y
856 pasos en la bandeja del lote 4**, contra los **78 candidatos y 761 pasos** que mi `ACTA 19`
`6.2` firmo: **cinco candidatos y 95 pasos mas.**

    $ ls cuarentena/scott_radical_candor/*.json | wc -l
    83

### 1.3. La poblacion del barrido, que es grafo mas bandejas (`D.38.4`)

    $ python .barrido_auditor_v21.py cuarentena/scott_radical_candor
    POBLACION DEL BARRIDO (D.38.4)
      grafo dataset/nodos.jsonl : 203
      bandejas cuarentena/*/    : 246
      TOTAL                     : 449
      umbrales: sim 0.35 | fam 0.3 | paso 0.6

    $ wc -l dataset/nodos.jsonl
    203 dataset/nodos.jsonl

**449 sobre 449 = 203 del grafo mas 246 de las bandejas**, descartando `_insertados` y
`_derivadas`. Mi `ACTA 19` barrio **444 = 203 + 241**; **los cinco de diferencia son los cinco
candidatos nuevos, y el grafo no se ha movido: 203 antes y 203 hoy.**

---

## 2. LO QUE ESTA VUELTA HIZO, MEDIDO POR MI ANTES DE LEER SU REPORTE

### 2.1. `cap_09` esta cerrado en 20 de 20, y las cinco son exactamente las cinco que debia

    $ python .cierre_cap09_v21.py
    piezas de cap_09 con nodo en la bandeja : 20
      de la vuelta anterior                 : 15  ['P10','P11','P12','P13','P14','P15','P20','P21','P25','P26','P4','P5','P6','P8','P9']
      escritas en esta vuelta               : 5  ['P22','P23','P24','P27','P28']

    LAS CINCO, CON SUS PASOS:
      P22  revisar_critica_mujer_agresiva_cuatro_tacticas       pasos=12
      P23  responder_critica_abrasiva_cuatro_reglas             pasos=14
      P24  entregar_evaluacion_formal_desempenio_nueve_consejos pasos=22
      P27  conducir_reuniones_salto_nivel_diez_reglas           pasos=31
      P28  resolver_dudas_frecuentes_reuniones_salto_nivel      pasos=16
      pasos de las cinco: 95
      pasos de las veinte: 272

    numeros de pieza de la frontera de 30 que NO dan nodo: 10  [1, 2, 3, 7, 16, 17, 18, 19, 29, 30]

    candidatos de la bandeja que nombran cap_10 en cualquier campo: 0 []

**LAS CINCO SON `P22`, `P23`, `P24`, `P27` y `P28`: exactamente las cinco que mi encargo nombro, ni
una mas ni una menos.** Las `20` piezas con nodo mas las `10` sin nodo dan las `30` de la frontera
adjudicada, **que no reabro**. **`cap_09` queda cerrado en 20 de 20 y 272 pasos**, y el reparto
`15 mas 5` cuadra con las 15 que la vuelta anterior escribio.

**Y `cap_10` NO SE ESCRIBIO: `0` candidatos de `83` lo nombran en ningun campo.** La vuelta se
queda, por tanto, **en el limite de capitulo y no dentro de uno**, que es la unica forma legitima
que mi TAREA 3 punto 4 dejaba abierta. **Si su reporte lo declara, cumple; si no lo declara, es
caida de especie `REPORTE`** por `AUDITOR_FORJA.md` 8.1, **y eso lo veo en mi turno normal, no
aqui.**

### 2.2. Mi lectura de fidelidad `D.30` de los 95 pasos, uno a uno contra su linea

**Abri los cinco candidatos y lei su tramo en `fuentes/scott_radical_candor/cap_09.md`** con
`sed -n` y con las lineas numeradas por `awk 'NR>=331 && NF>0'`. Clasifico cada pieza y digo lo
que sostiene la clase.

| pieza | tramo | mi clase | lo que la sostiene |
|---|---|---|---|
| **`P22`** `revisar_critica_mujer_agresiva_cuatro_tacticas` | `L301` a `L313` | **PROCEDIMIENTO, da nodo** | `L303` encuadra y **`L305`, `L309`, `L311` y `L313` son CUATRO tacticas rotuladas** con actos nombrados: cambiar el genero, describir ejemplos concretos, fijarse en las palabras, dar sugerencias concretas |
| **`P23`** `responder_critica_abrasiva_cuatro_reglas` | `L315` a `L329` | **PROCEDIMIENTO, da nodo** | `L317` dice literalmente *the following four rules of thumb* y detras hay **CINCO** rotulos. **La serie es de cuatro (`L319`, `L321`, `L323`, `L325`) y `L327` es coda**: adjudicado en mi `ACTA 19`, y **mi relectura de hoy lo sostiene**, porque `L319` a `L325` mandan sobre la conducta propia de quien recibe la critica y `L327` manda sobre como tratar a quien la dio |
| **`P24`** `entregar_evaluacion_formal_desempenio_nueve_consejos` | `L331` a `L361` | **PROCEDIMIENTO, da nodo** | `L339` anuncia *here is my advice for delivering a performance review well*, y detras hay **NUEVE** rotulos contados sobre la pagina: `L341`, `L343`, `L345`, `L347`, `L353`, `L355`, `L357`, `L359`, `L361`. **`L349` y `L351` son cuerpo de `L347`, no rotulo nuevo** |
| **`P27`** `conducir_reuniones_salto_nivel_diez_reglas` | `L383` a `L413` | **PROCEDIMIENTO, da nodo. La pieza mas procedimental del capitulo** | `L391` anuncia *a few rules of thumb I learned for conducting them*, y detras hay **DIEZ** rotulos: `L393`, `L395`, `L397`, `L401`, `L403`, `L405`, `L407`, `L409`, `L411`, `L413`. **`L399` empieza por *More importantly* y es cuerpo de `L397`, no rotulo** |
| **`P28`** `resolver_dudas_frecuentes_reuniones_salto_nivel` | `L415` a `L425` | **PROCEDIMIENTO, da nodo, y CUELGA de `P27`** | **CUATRO** preguntas con su respuesta en `L419`, `L421`, `L423` y `L425`, y las respuestas traen actos, no adjetivos de adecuacion. **`L417` dice *some of the questions* sin dar cuenta**, asi que el `cuatro` que publico **cuenta rotulos de la pagina y no una cifra del libro**, y lo digo porque la diferencia es justo lo que `D.37` vigila |

**MI CUENTA DE PUENTES, cotejando los 95 pasos contra sus lineas: `0` de `95`.** Ninguno de los
95 añade un acto que su parrafo no diga. **Tasa de puente de las cinco piezas: `0,00` sobre un
denominador de `95` pasos**, y **`95` es la suma de `12 + 14 + 22 + 31 + 16`** que el instrumento
de `2.1` imprime.

**LOS DOS SITIOS DONDE ESTUVE A PUNTO DE MARCAR PUENTE Y NO LO MARQUE**, dichos porque un `0` sin
sus casos limite no es una lectura:

- **`P22` paso 10** convierte en mandato al lector (*cuestiona en voz alta el uso de palabras como
  abrasiva*) lo que `L311` cuenta **de un tercero**: *One of the things I appreciated about working
  with Dick Costolo was that he challenged the use of words like "abrasive."* **El acto SI esta en
  el libro; lo que cambia es el sujeto.** `D.30` caza el paso que el libro no dice, no el paso que
  el libro dice de otro. **TRANSCRIPCION, con la redireccion de sujeto declarada.** Lo mismo pasa,
  y por eso no lo cuento tres veces, en **`P24` paso 5** (el jefe del visto mas y visto menos) y en
  **`P28` pasos 1 y 2** (*ponte a excavar*, que el libro cuenta en pasado y en primera persona).
- **`P28` paso 16** es el unico donde el candidato **declara su propia correccion dentro del acto
  de escribir**: decia *las dos maneras* y el libro dice *a world of difference between saying X
  and saying Y* **sin dar cuenta**. **La comprobe contra `L425` y la correccion es cierta**: el
  paso final no lleva cuenta.

### 2.3. LO QUE MI LECTURA SI ECHA EN FALTA, y es mi discutible numero 1

**`P22` tiene `atribuciones: 0`**, y su tramo contiene un experimento con resultado:

    $ sed -n '307p' fuentes/scott_radical_candor/cap_09.md
    Two improv actors I know who do role plays to help people practice giving good guidance at some
    major Silicon Valley companies did the following experiment: they both used the word "fucking"
    when talking to their "boss" in the role play. Participants, male and female, reacted with
    extreme offense when the female actor used the word, but didn't blink when the male actor did.

**`L307` no esta ni en un paso ni en una atribucion: se cae entero del candidato.** No es puente
(nadie invento nada) ni error de clase (ningun veredicto se movio), **pero es la unica evidencia
empirica que el libro da de la tactica `cambia el genero`, y el nodo se queda sin ella.**

Las otras cuatro piezas si llevan la suya, y las abri una a una: **`P23`** el caso Heidi/Howard
Roizen, **`P24`** la abolicion en General Electric, **`P27`** dos (Roxane Wales, y las siete u ocho
horas al anio con cinco personas a cargo), **`P28`** las tres veces en anios de reuniones.
**`4` de `5` con atribucion y `1` sin ella.**

**LO DEJO PLANTEADO Y NO LO ADJUDICO AQUI**, porque adjudicar es del turno normal y con su reporte
delante.

### 2.4. Una omision menor, dicha para que no la encuentre nadie despues

**`P24` no recoge la ultima frase de `L361`**: *Many companies separate "development conversations"
from "rating conversations" by a quarter or more. This is fine, as long as the "development
conversations" don't substitute for regular impromptu guidance, which should be happening on a
weekly cadence.* Es una condicion con cadencia nombrada. **Una omision no es puente y no entra en
`PASOS INVENTADOS`**, que mide lo inventado y no lo dejado fuera. La digo y no la convierto en
caida.

---

## 3. MI FRONTERA CIEGA DE `cap_10`, CORTADA POR MI ANTES DE VER LA SUYA

*Mi TAREA 3 le mandaba cortar y publicar la frontera de `cap_10` **antes** de extraer. La corto yo
tambien, a ciegas, para que las dos lecturas se puedan cruzar linea a linea en mi turno normal.*

### 3.1. El cuerpo, medido aparte y antes de la tabla

    $ sed -n '4,5p' fuentes/scott_radical_candor/cap_10.md
    unidad: Cap. 7
    titulo_textual: Team
    $ wc -l fuentes/scott_radical_candor/cap_10.md
    263 fuentes/scott_radical_candor/cap_10.md
    $ sed -n '8,$p' fuentes/scott_radical_candor/cap_10.md | wc -w
    8976

### 3.2. La tabla, y se cierra contra el cuerpo o no se publica (`ACTA 18` `7.5` orden 1)

    $ python .frontera_auditor_v21.py
    cl  tramo         palabras  rotulo leido en la linea de cabecera
    NO  L9    a L13       187  subtitulo del capitulo y apertura, remite al Cap. 3
    NO  L15   a L21       200  CAREER CONVERSATIONS: rotulo, subtitulo y encuadre
    NO  L23   a L45      1254  el caso de Russ Laraway: Todd, Sarah, el off site y la encuesta
    SI  L47   a L59       780  Conversation one: life story
    SI  L61   a L75       737  The second conversation: dreams
    SI  L77   a L87       345  Conversation three: eighteen-month plan
    NO  L89   a L91       101  cierre de seccion tras el asterisco
    SI  L93   a L125     1095  GROWTH MANAGEMENT: el plan anual y sus CUATRO pasos rotulados
    NO  L127  a L135      191  HIRING: rotulo, mentalidad rock star/superstar y encuadre
    SI  L137  a L163     1310  el proceso de contratacion: CINCO piezas rotuladas
    NO  L165  a L171      196  FIRING: rotulo, subtitulo y encuadre de las dos empresas
    SI  L173  a L201     1176  despedir: las TRES cosas que el texto anuncia, mas Follow up de coda
    NO  L203  a L213      318  PROMOTIONS: rotulo, subtitulo y el caso de los comites de Google
    SI  L215  a L223      320  la reunion de calibracion de ascensos: CUATRO consejos rotulados
    SI  L225  a L251      568  REWARD YOUR ROCK STARS: CUATRO vias de recompensa sin ascenso
    NO  L253  a L255       63  AVOID ABSENTEE MANAGEMENT: remite a una tabla, sin procedimiento propio
    NO  L257  a L259      133  SUMMARY
    NO  L261  a L263        2  marcador del capitulo siguiente (8. RESULTS)

    PIEZAS QUE MI LECTURA CIEGA CUENTA EN cap_10: 18
      SI (yo escribiria nodo): 8
      NO (yo no extraeria)   : 10

    lineas con contenido de L8 en adelante NO cubiertas : 0 []
    lineas cubiertas por DOS piezas o mas (solapes)     : 0 []

    suma de palabras de mis 18 filas : 8976
    cuerpo de cap_10 medido aparte   : 8976
    CUADRA

**MI FRONTERA CIEGA DE `cap_10`: 18 piezas, 8 dan nodo y 10 no, con `0` lineas sin cubrir de las
`263` del fichero, `0` solapes, y `8976` palabras de suma contra `8976` de cuerpo medido aparte.**

**Mi encargo proyectaba `10,3` candidatos** a la densidad de `cap_09` (`17.482` palabras entre sus
`20` piezas con nodo dan `874` por candidato; `8976 / 874 = 10,3`). **Mi lectura de hoy corta mas
grueso: `8` candidatos, o `1.122` palabras por candidato sobre `8976`.** La diferencia no corrige
aquella proyeccion: **es que `cap_10` gasta mas pagina en casos.** El caso de Russ Laraway solo son
`1.254` de las `8.976` palabras del cuerpo, el **`14,0` por ciento**, y yo no lo extraigo.

### 3.3. Las tres decisiones de mi corte que mas se pueden discutir, dichas antes y no despues

1. **`L93` a `L125` como UN nodo y no como cuatro.** `L99` declara un entregable unico (*Once a
   year, you need to put together a growth-management plan for each person*) y los cuatro rotulos
   (`L101`, `L107`, `L115`, `L121`) son **sus pasos**, no cuatro procedimientos. Si el extractor lo
   parte en cuatro, la discrepancia es de granularidad y **la decide el entregable, no el tamaño**.
2. **`L173` a `L201` en un solo nodo, y con la trampa de la cuenta dentro.** **`L173` anuncia
   *three things* y detras hay CUATRO rotulos**: `L175` *Don't wait too long*, `L181` *Don't make
   the decision unilaterally*, `L189` *Give a damn*, `L197` *Follow up*. **Es la misma trampa que
   `L317` de `cap_09`**, donde el libro decia cuatro y habia cinco. **Mi lectura: las tres son
   `L175`, `L181` y `L189`, porque son lo que se hace para que despedir sea mas facil, y `L197` es
   coda porque ocurre despues del despido.** Es **extension natural** de la adjudicacion que mi
   `ACTA 19` ya hizo sobre `L317`, y la cito en vez de abrir doctrina nueva (`AUDITOR_FORJA.md`
   1.3).
3. **`L23` a `L45` fuera.** El caso de Russ Laraway con Todd y Sarah **lleva metodo narrado dentro**
   (`L35` a `L41`), y aun asi lo dejo fuera porque ese metodo **vuelve proceduralizado** en las tres
   conversaciones de `L47`, `L61` y `L77`. **Si el extractor lo extrae, no le llamo puente: le
   llamo solape**, y lo mido contra las tres.

### 3.4. **EL RIESGO DE FRONTERA DE `cap_10`, Y ES EL HALLAZGO DE ESTA APERTURA**

`cap_10` es `Cap. 7`, `Team`. **El propio libro declara la continuidad en su primera linea de
cuerpo**, y por eso esto no se adjudica citando una señal (`D.19`) sino leyendo:

    $ sed -n '11p' fuentes/scott_radical_candor/cap_10.md
    CHAPTER THREE ("UNDERSTAND WHAT MOTIVATES Each Person on Your Team") discussed the importance
    of getting to know each person who reports to you well enough that you can put the right
    people in the right roles, avoiding both boredom and burn-out.

    $ sed -n '4,5p' fuentes/scott_radical_candor/cap_06.md
    unidad: Cap. 3
    titulo_textual: Understand What Motivates Each Person on Your Team

**`Cap. 3` es `cap_06`, y `cap_06` ya tiene `10` candidatos y `117` pasos en la bandeja** (censo
`1.2`). **Cinco de mis ocho piezas de `cap_10` caen encima de uno suyo.** Los empareje **leyendo
titulos y pasos**, no seniales:

| mi pieza de `cap_10` | el candidato de `cap_06` que ya esta en la bandeja | mi lectura con la vara de `6.1` |
|---|---|---|
| `L47` a `L87`, las tres conversaciones de carrera | `descubrir_motivacion_sentido_persona` | **CONTINUA.** La madre dice **de donde** sale el sentido; la hija da **el guion de las tres conversaciones** con su duracion y sus preguntas. Procedimiento propio en los dos lados |
| `L93` a `L125`, el plan de crecimiento anual | `retirar_etiquetas_permanentes_equipo` y `cambiar_potencial_trayectoria_crecimiento` | **CONTINUA.** `L101` dice *Put names in boxes (**temporarily!**)*, y ese *temporarily* **es la doctrina de la madre citada por la hija**; lo que la hija añade es la cadencia anual, el contraste externo y el plan de tres a cinco puntos |
| `L173` a `L201`, despedir | `decidir_momento_despedir_persona` y `despedir_persona_franqueza_radical` | **CONTINUA.** La madre resuelve **cuando** y **con que trato**; la hija resuelve **el procedimiento**: no esperar, no decidir solo, documentar con quien sepa, y el seguimiento al mes |
| **`L225` a `L251`, recompensar a las estrellas de rock** | **`reconocer_recompensar_gente_estable`** | **EL PAR MAS CERRADO DEL CAPITULO, Y AUN ASI `CONTINUA`.** Ver el bloque de abajo |
| `L137` a `L163` contratar, y `L215` a `L223` la calibracion de ascensos | **ninguno** | **Sin madre en la bandeja.** Son lo genuinamente nuevo de `cap_10` |

> #### **EL PAR QUE HAY QUE MIRAR CON LUPA, Y LO DIGO ANTES DE QUE SE ESCRIBA**
>
> `reconocer_recompensar_gente_estable` (`cap_06`, **12 pasos**, leidos hoy uno a uno) se titula
> literalmente *por vias que no sean la promocion*, **que es el asunto entero de mi pieza `L225` a
> `L251`.** Y el solape no es de tema, es de acto:
>
> | acto | donde esta en la madre | donde esta en la hija |
> |---|---|---|
> | nombrar experto de referencia y ponerlo a enseñar | pasos `7` a `10` | `L247`, *Gurus* |
> | tratar ese papel como honor y no obligacion, y buscar otra via si odia enseñar | paso `9` | `L247` |
> | dar tribuna publica a quien hace trabajo poco visible | paso `2` | `L251`, *Public presentations* |
> | dar las gracias en privado a los timidos | paso `2` | `L243`, *Say thank-you* |
>
> **CON LA VARA, Y CON DIRECCION: que añade la HIJA a la MADRE.** Queda fuera del solape, y es
> procedimiento: **darle al guru un par de meses para preparar una clase** (`L247`); **no mandar el
> correo de anuncio de ascensos** (`L231`); **anunciar el cambio de papel pero no el ascenso**
> (`L235`); **elogiar en publico la cosa que quieres que se repita, y no el ascenso** (`L237`); **y
> dar las gracias por escrito ademas de en persona, y a menudo las dos** (`L243`). Y queda fuera
> por el lado de la madre, tambien procedimiento: **el racionamiento de puntuaciones altas** (pasos
> `5` y `6`), **los premios de antiguedad** (paso `3`) y **las dos formas de promocion mala** (paso
> `12`).
>
> **`NOMBRAR NO ES PROCEDIMENTAR` no la salva ni la hunde: hay procedimiento propio en los dos
> lados, y por eso mi lectura ciega es `CONTINUA` con arista declarada, no `REPITE`.** Pero es
> **el par mas cerrado que he visto en el lote 4**, y **la aduana no lo va a levantar sola**,
> porque los dos extremos viven en la bandeja y `paso_contra_nodo` compara contra el grafo. Es
> exactamente la averia que costo el par de la vuelta 19.
>
> **`EXTRACTOR.md` 12 lo cubre por su letra**: *un capitulo entero en la misma familia no es
> duplicado, es un libro que trata un tema*. **No pido doctrina nueva y esto no es parada.**

---

## 4. EL BARRIDO DE VECINOS `D.38.4`, SOBRE GRAFO MAS BANDEJAS

*Uno por vez, con el resto de la poblacion como contrario (`leave one out`), usando
`src.aduana.buscar_vecinos`, que es el instrumento de la casa. **Cero escrituras.***

    $ python -u .barrido_auditor_v21.py cuarentena/scott_radical_candor
    POBLACION DEL BARRIDO (D.38.4)
      grafo dataset/nodos.jsonl : 203
      bandejas cuarentena/*/    : 246
      TOTAL                     : 449
      umbrales: sim 0.35 | fam 0.3 | paso 0.6

    candidatos de la vuelta 21 (las cinco de cap_09) a barrer: 5
    ### conducir_reuniones_salto_nivel_diez_reglas.json   (contra 448)
        vecino resolver_dudas_frecuentes_reuniones_salto_nivel  [levantada por: familia_id]
          similitud_texto 0.207 | familia_id 0.333 | paso_contra_nodo 0.471
          paso 19 del candidato contra paso 12 de resolver_dudas_frecuentes_reuniones_salto_nivel

    ### entregar_evaluacion_formal_desempenio_nueve_consejos.json   (contra 448)
        SIN VECINOS: ninguna senial levanta nada

    ### resolver_dudas_frecuentes_reuniones_salto_nivel.json   (contra 448)
        vecino conducir_reuniones_salto_nivel_diez_reglas  [levantada por: familia_id]
          similitud_texto 0.221 | familia_id 0.333 | paso_contra_nodo 0.479
          paso 12 del candidato contra paso 19 de conducir_reuniones_salto_nivel_diez_reglas

    ### responder_critica_abrasiva_cuatro_reglas.json   (contra 448)
        SIN VECINOS: ninguna senial levanta nada

    ### revisar_critica_mujer_agresiva_cuatro_tacticas.json   (contra 448)
        vecino comprobar_criticas_hombre_mujeres_equipo  [levantada por: similitud_texto]
          similitud_texto 0.381 | familia_id 0.222 | paso_contra_nodo 0.43
          paso 2 del candidato contra paso 6 de comprobar_criticas_hombre_mujeres_equipo

### 4.1. La cuenta, con su denominador

**`5` candidatos barridos, cada uno contra `448`. `3` de los `5` levantan vecino y `2` no levantan
ninguno. Se levantan `3` vecindades en total, que son `2` pares distintos.**

> ### **Y LA CIFRA QUE JUSTIFICA `D.38.4` ENTERA: `3` DE `3` VECINOS ESTAN EN LA BANDEJA Y `0` EN EL GRAFO.**
>
> No es casualidad ni suerte del muestreo: **el grafo tiene `0` nodos de `scott_radical_candor`
> sobre `203`** (`7.3`), asi que **ningun vecino de un candidato de este lote puede estar en el
> grafo hoy.** Un barrido contra el grafo solo habria devuelto **cero de cero**, y habria parecido
> limpio. **Es la segunda vuelta seguida que el barrido de bandeja es el unico que encuentra algo.**

### 4.2. Par 1, `P27` contra `P28`: la arista que el propio candidato ya declara

**Reciproco y por `familia_id 0.333`**, no por los pasos (`paso_contra_nodo 0.471` y `0.479`, los
dos por debajo del umbral `0.6`). **`P28` cuelga de `P27`**, mi encargo lo exigia en la misma
vuelta y el `resumen_teorico` de `P28` lo declara como cola `D.29`. **El barrido confirma lo que el
candidato ya decia: no hay hallazgo nuevo aqui, y eso tambien se publica.**

### 4.3. Par 2, `P22` contra `P20`: **mi lectura ciega es `SANO`, y digo por que**

`comprobar_criticas_hombre_mujeres_equipo` es la pieza `P20`, `L291` a `L293`, `6` pasos. Los abri
los dos y los lei antes de decidir. **Solo lo levanta `similitud_texto 0.381`; `paso_contra_nodo`
da `0.43` y no llega al `0.6`.** Y `D.19` manda no adjudicar citando una señal, asi que leo:

| | `P20`, `L291` a `L293` | `P22`, `L301` a `L313` |
|---|---|---|
| **disparador** | eres un hombre y **te preocupa contenerte** al criticar a una mujer | estas a punto de decirle a una mujer que **es demasiado agresiva** |
| **entregable** | saber, **dicho por ella**, como esta cayendo tu guia | la critica dada **sin haber caido en la trampa de competencia contra simpatia**, o retirada |
| **actos** | preguntarselo, explicarle el marco, decir la frase, pedirle que te mida | cambiar el genero, describir ejemplos concretos, vigilar las palabras, dar sugerencias concretas |

**El error que `P20` caza es dar de MENOS; el que `P22` caza es dar lo EQUIVOCADO.** No comparten
ni un acto. **Lo que comparten es vocabulario** (mujer, critica, genero, equipo), que es justo lo
que `similitud_texto` mide. **Son hermanas bajo el mismo encuadre de `L289`** (*I have a few
thoughts on how individuals can take action to cool things down*), **no madre e hija**, asi que
tampoco pido arista: `D.29` y `D.37` piden la arista cuando una cuelga de otra, y aqui ninguna
cuelga.

**MI VEREDICTO CIEGO: `SANO`. Vecindad de vocabulario, no de acto.** Si su reporte lo marco como
discutible, coincidimos en donde mirar; si lo marco como par, ahi hay discrepancia y va a
relectura conjunta con esta tabla delante.

---

## 5. MIS DISCUTIBLES DE ESTA APERTURA, NUMERADOS Y SIN ADJUDICAR

*Los marco YO y ANTES de ver su reporte, que es lo unico que hace informativa la comparacion
(`AUDITOR_FORJA.md` 5.1). **Marcar no es adjudicar**: adjudicar es del turno normal.*

| # | discutible | mi lectura de hoy |
|---:|---|---|
| **1** | **`P22` sale con `atribuciones: 0` y `L307` se cae entero**: el experimento de los dos actores de improvisacion no esta ni en paso ni en atribucion | **Perdida de evidencia, no puente.** Es la unica prueba empirica que el libro da de *cambia el genero* |
| **2** | **La redireccion de sujeto**: `P22` paso 10, `P24` paso 5 y `P28` pasos 1 y 2 convierten en mandato al lector un acto que el libro cuenta **de un tercero o en pasado** | **TRANSCRIPCION**, porque el acto esta en el libro. **Pero la especie merece nombre**, y la traigo al turno normal para que se nombre una vez y no se discuta cinco |
| **3** | **`P24` deja fuera la ultima frase de `L361`**, la cadencia semanal de la guia improvisada | **Omision, no puente.** No entra en `PASOS INVENTADOS` |
| **4** | **`P28` se titula *las cuatro dudas mas frecuentes* y `L417` dice *some of the questions*** | **Se sostiene**, porque el `cuatro` cuenta rotulos impresos y no repite una cuenta del libro. **Pero el propio candidato argumenta en su `resumen_teorico` que la cuenta *no esta escrita***, y luego la usa en el titulo |
| **5** | **`cap_10` `L173` anuncia *three things* y trae CUATRO rotulos** | **Las tres son `L175`, `L181` y `L189`; `L197` es coda.** Extension natural de la adjudicacion de `L317`, citada y no inventada |
| **6** | **`L225` a `L251` de `cap_10` contra `reconocer_recompensar_gente_estable` de `cap_06`** | **`CONTINUA` con arista, no `REPITE`**, y es **el par mas cerrado del lote 4**. Bloque de `3.4` |
| **7** | **Granularidad de `L93` a `L125`**: un nodo o cuatro | **Uno**, porque `L99` declara un entregable unico |
| **8** | **`P22` contra `P20`**, que **mi barrido si levanto** por `similitud_texto 0.381` | **`SANO`, y ya adjudicado por mi en `4.3` con los dos leidos delante.** Lo dejo en esta lista para que se vea que **lo mire**, no para reabrirlo |

---

## 6. `HEREDADO 1` CUMPLIDO: MIS REMEDIOS, UNO A UNO, TAMBIEN LOS QUE AGUANTAN

*Esto **es** el heredado. `ACTA 19` `7.5`: `REMEDIO ROTO` solo informa si el remedio tambien se
declara cuando aguanta. **Ninguna fila queda en blanco, y el `NO APLICA` lleva su motivo detras.***

| remedio mio | comprobacion EN ESTA FASE | resultado |
|---|---|---|
| **`D.40`**, leer `ACTA_AUDITOR.md` en la fase ciega antes de escribir | seccion `0.1`: huella `2d794fc9...` **remedida por mi con `git hash-object`**, igual a la que el prompt entrega, y `18132` lineas con `wc -l`. Lei ademas `PROMPT_SIGUIENTE.md` entero | **CUMPLIDO** |
| **`D.38.4`**, barrido sobre grafo **mas** bandejas | secciones `1.3` y `4`: **`449 = 203 + 246`**, uno por vez contra `448`, con su `wc -l` pegado | **CUMPLIDO** |
| **`D.38.3`**, toda cifra de la fase ciega con su instrumento al lado | **todas las de este fichero**, y las derivadas (`874`, `10,27`, `1.122`, `14,0`) con su division escrita | **CUMPLIDO** |
| **`ACTA 19` `7.4` ORDEN A**, la fila de residuo es cero o trae nombres | `1.2`: **`SIN` no existe, residuo `0` sobre `83`**, y los `39` deducidos salen con nombre | **CUMPLIDO** |
| **`ACTA 19` `7.4` ORDEN B**, el rotulo se escribe despues del instrumento | `1.1`: **cace la fila falsa antes de publicarla**, y probe ademas el extremo contrario para saber que los dos mienten | **CUMPLIDO, Y ES EL QUE EVITO LA CAIDA DE HOY** |
| **`ACTA 18` `7.5` orden 1**, la frontera se cierra contra el cuerpo o no se publica | `3.2`: **`0` lineas sin cubrir, `0` solapes, `8976` igual a `8976`** | **CUMPLIDO** |
| **`ACTA 18` `7.5` orden 2**, el denominador en la misma frase | toda cifra de este fichero lleva el suyo | **CUMPLIDO** |
| **`ACTA 18` `7.5` orden 3**, el barrido de guiones dos veces | **primera AQUI y antes del sello**, pegada en `7.1`; la segunda al cerrar el turno | **PRIMERA CUMPLIDA. La segunda no la declaro cumplida por adelantado** |
| **`D.34`**, no recuperar de git los cuatro ficheros retirados | **no corri `git log`, `git show` ni `git checkout` sobre ninguno.** La contaminacion que si hubo **la trajo el prompt** y la declaro entera en `0.bis` | **CUMPLIDO, con la contaminacion ajena declarada al lado** |
| **`D.34`**, no tocar `APERTURA_CIEGA.md` tras el sello | **el sello todavia no existe cuando escribo esto** | **NO SE PUEDE DECLARAR AQUI, Y NO LO DECLARO.** Se comprueba al cerrar mi turno contra `SELLOS_APERTURA.jsonl`, y ahi va |
| **`5.5`**, re correr por mutacion toda guarda declarada mordiendo | **NO APLICA EN ESTA FASE, y este es el motivo:** la guarda que se re corre es **la que el reporte declara mordiendo**, y `docs/loop/REPORTE.md` **no esta en el arbol** por `D.34.2`. Sin reporte no hay guarda declarada, y mutar una guarda al azar no comprueba nada | **NO APLICA, con motivo. Se cumple en mi turno normal** |

---

## 7. LO QUE CIERRA ESTA FASE

### 7.1. El barrido de guiones, primera de las dos (`ACTA 18` `7.5` orden 3)

    $ python forja.py guiones docs/loop/APERTURA_CIEGA.md
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

### 7.2. Donde esta el lote 4, medido y no recordado

    $ for c in 00 .. 14; do sed -n '8,$p' fuentes/scott_radical_candor/cap_$c.md | wc -w; done
      (salida entera en .cuerpos_lote4_v21.txt)
    $ awk '{s+=$2} END {print s}' .cuerpos_lote4_v21.txt
    108161
    $ awk '$1<="cap_09" {s+=$2} END {print s}' .cuerpos_lote4_v21.txt
    71505
    $ awk '$1>="cap_10" {s+=$2} END {print s}' .cuerpos_lote4_v21.txt
    36656

**`cap_00` a `cap_09` cerrados suman `71.505` palabras de las `108.161` del libro entero, el
`66,1` por ciento; quedan `36.656`, el `33,9` por ciento, repartidas en `cap_10` a `cap_14`.**
**El `71.505` reproduce al digito el denominador que mi `ACTA 19` `6.2` firmo**, medido hoy otra
vez y desde el arbol.

### 7.3. Y una cosa que mide el codigo y no yo, porque sostiene el hallazgo de `3.4`

    $ grep -n "nodos = comun.leer_jsonl" src/informe.py
    113:    nodos = comun.leer_jsonl(ruta_dataset)

**`revisar()` carga la poblacion UNA vez desde `dataset/nodos.jsonl` y no la extiende con los
candidatos del lote**: `ids_del_lote` solo vigila choques de id, no vecindad. **Y el grafo tiene
`0` nodos de `scott_radical_candor` sobre `203`** (los `203` son `136` de `zhuo_manager`, `59` de
`smart_who`, `6` de `onu_consumidor` y `2` del manual). **Por eso ningun par de la bandeja contra
la bandeja lo levanta su aduana**, y por eso `D.38.4` manda que el mio barra las dos poblaciones.

### 7.4. Lo que NO he mirado, dicho para que se pueda comprobar

`docs/loop/REPORTE.md`, `loop.log`, `ultimo_extractor.json` y `ultimo_auditor.json` **no estan en
el arbol y no los busque**. `.aduana_v20/`, `.barrido_v20/` y `.t1_v20/` **si estan y no los abri**:
son la lectura del extractor de esta misma vuelta, y esta fase existe para que yo escriba la mia
antes de verla.

**Esta apertura queda cerrada. No la vuelvo a tocar: el arnes la sella y el sello se verifica al
terminar mi turno.**
