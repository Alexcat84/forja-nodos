
---

## P.5. TAREA 4: **LA CIFRA DE FIDELIDAD QUE FALTABA, MEDIDA Y ACOTADA**. **CERRADA**, Y **EL FRENO SE DISPARA**

### P.5.a. **NO ES MAQUINARIA NUEVA, Y LO HAGO COMPROBABLE EN VEZ DE PROMETERLO** (moratoria, `EXTRACTOR.md` 13)

*El encargo dice: el instrumento ya existe y lo escribiste tu; lo que se encarga es CORRERLO.*

**`.t1_v22/correr_cuentas21.py` NO reescribe la lista de numerales ni la expresion regular:
EJECUTA `.t1_v21/cuentas21.py` y le saca su propia variable `CUENTAS` del espacio de nombres
resultante.** Si aquel fichero cambiara, este cambiaria con el.

    $ python .t1_v22/correr_cuentas21.py
    fichero corrido      : .t1_v21/cuentas21.py
    numerales que caza   : 20  dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez, once,
                               doce, quince, veinte, treinta, cuarenta, cincuenta, cien, ambas,
                               ambos, sendas
    su corrida de control sobre cap_10, HOY: ocurrencias de numeral que cuentan cosas,
                                             en los 194 pasos: 35

> **LA CORRECCION QUE ME HICE A MI MISMO ANTES DE PUBLICAR, y la dejo escrita porque casi publico
> una cifra falsa:** mi primera version de este guion imprimia *en la vuelta 21 esa misma linea dio
> 22*. **Es falso.** El `22` de la vuelta 21 era **el NUMERADOR que salio de leer las ocurrencias
> una a una**, no la cuenta de ocurrencias. **Una ocurrencia no es un puente hasta que alguien la
> lee contra la linea**, y esa es la distincion entera de esta tarea.

### P.5.b. **EL REPARTO, CONTRASTADO CONTRA LA `ACTA 21` `1.3`, Y AHI SE CAZO UN FALLO MIO**

    $ python .t1_v22/correr_cuentas21.py    (seccion 1)
      cap_01   candidatos=  1  pasos=   9        cap_07   candidatos= 25  pasos= 225
      cap_03   candidatos=  1  pasos=   7        cap_08   candidatos= 12  pasos= 102
      cap_04   candidatos=  6  pasos=  48        cap_09   candidatos= 20  pasos= 272
      cap_05   candidatos=  8  pasos=  76        cap_10   candidatos= 14  pasos= 205
      cap_06   candidatos= 10  pasos= 117        cap_11   candidatos= 16  pasos= 187
      TOTAL    candidatos=113  pasos=1248
      SIN MARCA DE CAPITULO: 0  []

**LAS OCHO FILAS DE `cap_01` A `cap_09` REPRODUCEN AL DIGITO LAS DE LA `ACTA 21` `1.3`.** Las dos
que no coinciden con ella son las dos que esta vuelta movio: `cap_10` de `13/194` a **`14/205`**
(la pieza 14) y `cap_11` de nada a **`16/187`**.

> ### **CAIDA MIA, CAZADA POR MI ANTES DE PUBLICAR, Y ES LA MISMA ESPECIE QUE ME CACE EN LA VUELTA 21.**
>
> Mi primer reparto daba **`cap_04` con 5 candidatos y 41 pasos**, contra los `6` y `48` que el
> auditor mide en su `1.3`. **La causa es un patron demasiado estrecho:** yo buscaba
> `cap_(\d\d)\.md`, y `invitar_desafio_reciproco_equipo` **nombra su `cap_04` sin el `.md`**, asi
> que perdia ese candidato y sus 7 pasos. **En la vuelta 21 me cace exactamente lo mismo** (*mi
> instrumento de reparto perdia 7 pasos de `cap_04` por un `.md` de mas en un patron*), y volvi a
> escribirlo.
>
> **LO QUE CAMBIA ES CUANDO SE CAZO:** esta vez la cifra **nunca llego a publicarse**, porque el
> encargo me daba una cifra externa contra la que contrastarla. **La leccion que saco es de
> metodo, no de expresion regular: un reparto que no se contrasta contra un conteo ajeno es un
> reparto que se cree a si mismo.**

### P.5.c. **LAS OCURRENCIAS POR CAPITULO, `cap_00` A `cap_09`. ES UNA MEDIDA DE OCURRENCIAS, NO UN NUMERADOR**

*Y lo digo con las palabras del encargo, porque es la distincion que sostiene toda la tarea.*

| unidad | candidatos | pasos | **ocurrencias** | ocurrencias por 100 pasos | **leido?** |
|---|---:|---:|---:|---:|---|
| `cap_00` | 0 | 0 | **0** | sin definir | no hay que leer |
| `cap_01` | 1 | 9 | **1** | 11,11 | **sin leer** |
| `cap_02` | 0 | 0 | **0** | sin definir | no hay que leer |
| `cap_03` | 1 | 7 | **6** | 85,71 | **sin leer** |
| `cap_04` | 6 | 48 | **9** | 18,75 | # **LEIDO, una a una** |
| `cap_05` | 8 | 76 | **20** | 26,32 | **sin leer** |
| `cap_06` | 10 | 117 | **33** | 28,21 | **sin leer** |
| `cap_07` | 25 | 225 | **20** | 8,89 | **sin leer** |
| `cap_08` | 12 | 102 | **17** | 16,67 | **sin leer** |
| `cap_09` | 20 | 272 | **54** | 19,85 | # **LEIDO, una a una** |
| | **83** | **856** | **160** | **18,69** | **2 capitulos de 8 con material** |

**LOS DOS QUE SE LEEN SON LOS QUE EL ENCARGO FIJA:** el de **mas ocurrencias** (`cap_09`, con 54) y
**`cap_04`** (la fila heredada mas alta). **De esos dos firmo el numerador. Los otros seis se
quedan en `sin leer` con su cuenta de ocurrencias publicada, y NO los corrijo esta vuelta.**

> **Y LA FILA QUE SALTA A LA VISTA LA DIGO YO EN VEZ DE ESPERAR A QUE LA VEA OTRO:** `cap_03` tiene
> **6 ocurrencias en 7 pasos**, la densidad mas alta con diferencia (`85,71` por 100 pasos).
> **No la leo, porque el encargo acota a dos capitulos y una relectura sin techo se come el trabajo
> que vigila.** La dejo nombrada aqui para que la vuelta que la lea sepa por donde empezar.

### P.5.d. **COMO SE SEPARA UNA OCURRENCIA DE UN PUENTE: EL CRITERIO SE LEE DE LO QUE LA VUELTA 21 RETIRO, NO SE INVENTA HOY**

*Es la parte que hace verificable el numerador, y por eso va antes que las cifras.*

**ABRI `.t1_v21/arreglo_cuentas.py`, que es donde viven las 22 retiradas, y la especie esta escrita
con sus ejemplares literales:**

    "El texto da sus dos ejemplares:"        ->  "El texto da sus ejemplares:"
    "y el texto nombra tres, tu jefe, ..."   ->  "y el texto los nombra: tu jefe, ..."
    "hazte las tres preguntas del texto:"    ->  "hazte las preguntas del texto:"

> ### **EL CRITERIO, ESCRITO COMO REGLA PARA QUE SE ME PUEDA CONTRADECIR: ES PUENTE CUANDO EL PASO ATRIBUYE UNA CUENTA AL LIBRO Y EL LIBRO NO ESCRIBE ESE NUMERO, AUNQUE LA ENUMERACION QUE SIGUE SEA COMPLETA Y CIERTA.**
>
> **Y DIGO QUE ESTUVE A PUNTO DE ABLANDARLO**, porque es el sesgo obvio de quien mide su propio
> trabajo: mi primer impulso fue decir que *el texto nombra tres* es una afirmacion **verdadera**
> sobre el texto y por tanto no es puente. **La vuelta 21 ya decidio que no**, y sus ejemplares
> retirados son literalmente de esa forma. **Me ato a su criterio en vez de estrenar el mio**, que
> es lo que `EXTRACTOR.md` 5 llama declarar la discrepancia en vez de resolverla copiando.

**LA CRIBA MECANICA QUE ORDENA LA LECTURA** (`.t1_v22/clasificar_cuentas.py`): separa las
ocurrencias en **grupo A** (el numeral va pegado a una marca de atribucion: *el texto*, *que
nombra*, *que pone*, *que da*) y **grupo B** (el numeral va dentro del contenido transcrito). **No
decide nada: ordena.**

| | `cap_09` | `cap_04` |
|---|---:|---:|
| grupo A, a leer contra la linea | **14** | **6** |
| grupo B, la cifra dentro del contenido | **40** | **3** |
| total | **54** | **9** |

**EL GRUPO B SE COMPROBO CON UNA SEGUNDA CRIBA MAS ESTRECHA** (`.t1_v22/cribar_cuentas.py`): el
numeral ingles equivalente tiene que aparecer **en una linea concreta del tramo**, no en el tramo
entero.

    $ python (comprobacion estrecha del grupo B de cap_09)
      GRUPO B de cap_09: 40 ocurrencias
        con su numeral ingles EN UNA LINEA del tramo : 40
        SIN el en ninguna linea del tramo            : 0

**LOS 40 PASAN. Y DIGO EXACTAMENTE QUE HICE Y QUE NO, sin adornarlo:** los **20 del grupo A** los
lei **uno a uno con el `sed` del libro delante**, y sus lineas van pegadas abajo. De los **43 del
grupo B** corri la criba estrecha sobre los 43 y **abri a mano 12 de ellos** (`L123` *2-3 minutes*,
`L125` *five direct reports / three times a week*, `L127` *one of two things / twenty-five- and
fifty-minute*, `L95` *three-year-old*, `L159` *slide six / 100 percent / 5 percent*, `L33` *sixty or
so people*, `L41` *count to six*, `L317` *four rules of thumb*, `L303` *Both genders*). **Los otros
31 los sostiene la criba y no mi lectura, y eso es lo que vale la fila.**

### P.5.e. **`cap_04` LEIDO ENTERO: LAS NUEVE OCURRENCIAS, UNA A UNA, CON SU `sed` PEGADO** (`D.35`)

| # | candidato, paso | lo que el paso dice | la linea del libro, pegada | **veredicto** |
|---:|---|---|---|---|
| 1 | `ajustar_franqueza_oido_oyente` P1 | *Mide **las dos dimensiones** en el oido del que escucha* | `157:BOTH DIMENSIONS OF Radical Candor are sensitive to context. They get measured at the listener's ear, not at the speaker's mouth.` y `81:I have identified two dimensions that, when paired, will help you move in a positive direction.` | **TRANSCRIPCION** |
| 2 | `ajustar_franqueza_oido_oyente` P2 | *ni como un juicio sobre una cultura: **el texto descarta los tres** por su nombre* | `157:Radical Candor is not a personality type or a talent or a cultural judgment.` **Descarta tres y NO escribe la cuenta** | # **PUENTE** |
| 3 | `cuidar_persona_completa_equipo` P9 | *ni con la charla forzada en actos sociales: **el texto descarta los tres** por su nombre* | `119:Caring personally is not about memorizing birthdays and names of family members. Nor is it about sharing the sordid details of one's personal life, or forced chitchat at social events you'd rather not attend.` **Descarta tres y NO escribe la cuenta** | # **PUENTE** |
| 4 | `delimitar_franqueza_radical_cinco_noes` P1 | *y **pone los dos ejemplares** de lo que la anula* | `145:If you follow that phrase with words like, "You are a liar and I don't trust you," or "You're a dipshit," you've just acted like a garden-variety jerk.` **Da dos y NO escribe la cuenta**. Es literalmente la forma que la vuelta 21 retiro (*El texto da sus dos ejemplares*) | # **PUENTE** |
| 5 | `delimitar_franqueza_radical_cinco_noes` P3 | *deja **tres cosas** sin importancia sin decir cada dia* | `147:A good rule of thumb for any relationship is to leave three unimportant things unsaid each day.` | **TRANSCRIPCION** |
| 6 | `delimitar_franqueza_radical_cinco_noes` P4 | *que son **las tres direcciones que el texto nombra*** | `149:To be Radically Candid, you need to practice it "up," "down," and "sideways."` **Nombra tres y NO escribe la cuenta** | # **PUENTE** |
| 7 | `invitar_desafio_reciproco_equipo` P3 | *sobre todo con quien acaba de llegar y con quien te tiene por jefe: **el texto lo dice de los dos*** | `139:Building enough trust between people to enable reciprocal challenge irrespective of reporting relationship takes time and attention.` mas `137:Elisse was new to the team and so was holding back her opinions.` **NO escribe cuenta**, pero **tampoco dice `el texto nombra dos`: dice que el texto lo afirma de los dos casos que el paso acaba de nombrar** | # **DISCUTIBLE, contado aparte** |
| 8 | `revisar_ciclo_responsabilidades_relaciones` P2 | *Cuenta con **los cinco estorbos que el texto nombra uno a uno*** | `69:Many things get in the way, though: power dynamics first and foremost, but also fear of conflict, worry about the boundaries of what's appropriate or "professional," fear of losing credibility, time pressure.` **Nombra cinco, dice `Many` y NO escribe la cuenta** | # **PUENTE** |
| 9 | `revisar_ciclo_responsabilidades_relaciones` P3 | *Repasa **las tres responsabilidades que el texto numera**, en su orden* | `71:They determine whether you can fulfill your three responsibilities as a manager: 1) ... 2) ... 3) ...` | **TRANSCRIPCION** |

> ### **`cap_04`: `5` PUENTES DE 9 OCURRENCIAS, MAS `1` DISCUTIBLE CONTADO APARTE. TRES SON TRANSCRIPCION.**

### P.5.f. **`cap_09` LEIDO: LAS CATORCE DEL GRUPO A, UNA A UNA, CON SU `sed` PEGADO**

| # | candidato, paso | la linea del libro, pegada | **veredicto** |
|---:|---|---|---|
| 1 | `abrazar_incomodidad_arrancar_critica_equipo` P5, *las dos ventajas que el texto pone* | `33:...Airing it in public has another benefit as well: it saves you from having to hear the same thing over and over.` **Marca un segundo beneficio y NO escribe la cuenta** | # **PUENTE, y es el mas suave de los seis: el libro escribe `another benefit as well`** |
| 2 | `dar_guia_acto_cinco_consejos` P5, *dos o tres minutos* | `123:Say it in 2-3 minutes between meetings. Just saying it right away in a minute or two, three at most...` | **TRANSCRIPCION** |
| 3 | `dar_guia_acto_cinco_consejos` P7, *con cinco personas... elogiar tres veces por semana* | `125:If you have five direct reports and you want to offer each praise three times a week and criticism once a week...` | **TRANSCRIPCION** |
| 4 | `dar_guia_acto_cinco_consejos` P8, *la primera de las dos salidas que el texto pone* | `127:...you must do one of two things. One, keep slack time in your calendar...` | **TRANSCRIPCION** |
| 5 | `dar_guia_humilde_tres_tecnicas` P14, *alguien de tres anios* | `95:This is funny in a three-year-old, but when adults confuse subjective tastes with objective reality, it's arrogant.` | **TRANSCRIPCION** |
| 6 | `elogiar_publico_criticar_privado_sus_tres_matices` P1, *los dos motivos que el texto da* | `157:Public criticism tends to trigger a defensive reaction... Public praise tends to lend more weight to the praise...` **Da los motivos y NO escribe la cuenta** | # **PUENTE** |
| 7 | `elogiar_publico_criticar_privado_sus_tres_matices` P2, *antes de poner las tres cosas que hay que pensar* | `157:However, this is a rule of thumb, not a hard and fast rule. Here are some things to think about.` **Dice `SOME things`, no tres** | # **PUENTE, Y EL PEOR DE LOS SEIS: LA CUENTA VIVE TAMBIEN EN EL `id` DEL FICHERO** (`..._sus_tres_matices`) |
| 8 | `evitar_personalizar_guia_aceptar_personal` P3, *los dos motivos por los que el texto dice* | `169:It's a problem because 1) it's generally inaccurate and 2) it renders an otherwise solvable problem really hard to fix...` **El libro los NUMERA** | **TRANSCRIPCION** |
| 9 | `exigir_critica_jefe_reticente` P2, *una de las tres frases que el texto da* | `299:Try saying, "What can I do or stop doing...?" or "I'm worried you're so concerned..." or "The thing that I most need from you..."` **Da tres y NO escribe la cuenta** | # **PUENTE** |
| 10 | `medir_guia_propia_pegatinas_marco` P7, *los cuatro casos que el texto nombra uno a uno* | `185:If somebody feels you were unnecessarily harsh... If they feel you pulled your punches... If they feel you dished out too many... If they feel you told them they did a good job but then...` **Nombra cuatro y NO escribe la cuenta** | # **PUENTE** |
| 11 | `medir_guia_propia_pegatinas_marco` P8, *las cuatro cosas... numeradas por el mismo* | `189:...Two, when you have a shared vocabulary... Three, the visual cue is a reminder... Four, if you ask them to do this but they don't...` **El libro las NUMERA hasta cuatro** | **TRANSCRIPCION** |
| 12 | `organizar_sistema_recoger_quejas_equipo` P1, *la diferencia que el texto marca entre las dos redacciones* | `59:JOHNSON & JOHNSON'S ORIGINAL credo had an interesting line... When it got rewritten, this intention got watered down into a much vaguer and less useful statement...` **Contrasta dos y NO escribe la cuenta** | # **PUENTE** |
| 13 | `responder_critica_abrasiva_cuatro_reglas` P1, *las cuatro reglas generales que el texto anuncia* | `317:Before you react to feedback that you're too aggressive/abrasive/etc., consider the following four rules of thumb:` | **TRANSCRIPCION** |
| 14 | `revisar_critica_mujer_agresiva_cuatro_tacticas` P2, *el texto dice que los dos generos* | `303:Both genders are equally guilty here I've found, unfortunately.` | **TRANSCRIPCION** |

> ### **`cap_09`: `6` PUENTES DE 54 OCURRENCIAS. OCHO DEL GRUPO A SON TRANSCRIPCION Y LOS 40 DEL GRUPO B PASAN LA CRIBA ESTRECHA.**

### P.5.g. **EL NUMERADOR FIRMADO DE LOS DOS CAPITULOS, Y LO QUE HACE CON EL FRENO**

**LOS PUENTES NUEVOS SON DISJUNTOS DE LOS HEREDADOS, Y LO COMPRUEBO EN VEZ DE SUPONERLO:** el `3`
heredado de `cap_04` sale entero de **`invitar_desafio_hacia_arriba`** (hoy
`invitar_desafio_reciproco_equipo`), segun mi propia tabla de la vuelta 15 (`REPORTE.md` `L18379`:
`| invitar_desafio_hacia_arriba | 7 | 4 | 3 | 0 |`). **Mis cinco de hoy estan en otros cuatro
ficheros.** El `1` heredado de `cap_09` es el puente que la vuelta 20 se cazo, y tampoco es ninguno
de mis seis.

| unidad | numerador heredado | **puentes nuevos del ancho** | **numerador firmado** | pasos | **tasa** | quien firma |
|---|---:|---:|---:|---:|---:|---|
| `cap_04` | 3 | # **5** | # **8** | 48 | # **16,67** | **numerador y criterio, MIOS** |
| `cap_09` | 1 | # **6** | # **7** | 272 | # **2,57** | **numerador y criterio, MIOS** |

**Y CON EL DISCUTIBLE DE `cap_04` DENTRO, que publico igual para no elegir la cifra que me
conviene:** `9 de 48 = 18,75`.

> # **EL FRENO SE DISPARA. `cap_04` PASA DEL TOPE DE 10 CON `16,67`, Y NO HAY LECTURA DE ESTA CIFRA EN QUE NO LO PASE: CON EL DISCUTIBLE FUERA DA `16,67` Y CON EL DENTRO DA `18,75`.**
>
> **LO QUE `EXTRACTOR.md` 12.4 Y LA `ACTA 21` `7.3` MANDAN ENTONCES:** *sube por encima del 10 por
> ciento? -> el tramo BAJA un escalon*. **El tramo pasa de TRES capitulos a DOS.**
>
> **Y DIGO CONTRA MI MISMO LO QUE ESTO SIGNIFICA, PORQUE ES INCOMODO:** el encargo de hoy decia
> *`PASOS INVENTADOS` da peor fila `cap_10` 8,76 contra tope 10 y no se dispara*. **Con la medida
> que el propio encargo me mando hacer, esa frase deja de ser cierta:** la peor fila ya no es
> `cap_10` con `8,76`, es **`cap_04` con `16,67`**. **No es que el trabajo haya empeorado. Es que
> `cap_04` nunca se habia medido con el instrumento ancho, y el total del lote era un suelo**,
> exactamente como el encargo escribio.
>
> **NO CORRIJO LOS CINCO PUENTES DE `cap_04` NI LOS SEIS DE `cap_09` EN ESTA VUELTA, Y DIGO POR
> QUE:** el encargo acota esta tarea a **medir y firmar**, no a reparar, y `ACTA 21` `4.8` deja
> dicho que **el numerador cuenta los puentes cazados se hayan corregido o no**, asi que corregirlos
> no bajaria ni una decima. **Cada uno lleva arriba su linea del libro y su correccion es de una
> frase**, asi que la vuelta que los repare los tiene listos. **No se empieza lo que no se cierra.**

### P.5.h. LA TABLA DE `PASOS INVENTADOS` ENTERA, FILA POR CAPITULO MAS TOTAL DEL LOTE, CON EL CRITERIO CORREGIDO DE `ACTA 21` `4.8`

| unidad | rotulo | cuerpo | candidatos | numerador | pasos | **tasa** | quien lo firma |
|---|---|---:|---:|---:|---:|---:|---|
| `cap_00` | `Copyright Page` | 218 | 0 | 0 | 0 | **sin definir** | |
| `cap_01` | `Preface` | 2.846 | 1 | 0 | 9 | **0,00** | **sin leer con el ancho**: 1 ocurrencia |
| `cap_02` | `Introduction` | 3.908 | 0 | 0 | 0 | **sin definir** | |
| `cap_03` | `How to Use This Book` | 627 | 1 | 0 | 7 | **0,00** | **sin leer con el ancho**: **6 ocurrencias en 7 pasos** |
| **`cap_04`** | **`Cap. 1`** | 6.263 | 6 | # **8** | **48** | # **16,67** | # **FIRMADO POR MI HOY** |
| `cap_05` | `Cap. 2` | 8.756 | 8 | 2 | 76 | **2,63** | **sin leer con el ancho**: 20 ocurrencias |
| `cap_06` | `Cap. 3` | 11.587 | 10 | 0 | 117 | **0,00** | **sin leer con el ancho**: 33 ocurrencias |
| `cap_07` | `Cap. 4` | 13.678 | 25 | 0 | 225 | **0,00** | **sin leer con el ancho**: 20 ocurrencias |
| `cap_08` | `Cap. 5` | 6.140 | 12 | 0 | 102 | **0,00** | **sin leer con el ancho**: 17 ocurrencias |
| **`cap_09`** | **`Cap. 6`** | 17.482 | 20 | # **7** | **272** | # **2,57** | # **FIRMADO POR MI HOY** |
| `cap_10` | `Cap. 7` | 8.976 | 14 | **17** | **205** | **8,29** | numerador del auditor (`ACTA 21` `7.2`); **denominador remedido hoy: 205 y no 194** |
| `cap_11` | `Cap. 8` | 8.626 | 16 | **0** | **187** | **0,00** | **MIO, leido en el acto de escribir los 16** |
| | **lote 4 hasta `cap_11`** | **89.107** | **113** | **34** | **1.248** | **2,72** | **INCOMPLETO, y lo digo: SEIS filas siguen sin medir con el instrumento ancho** |

> **DOS AVISOS SOBRE ESTA TABLA, Y LOS DOY YO:**
>
> **1. `cap_10` baja de `8,76` a `8,29` y NO es una mejora: es que le sume 11 pasos.** El numerador
> del auditor (`17`) no se toca; el denominador pasa de `194` a `205` porque la pieza 14 anadio sus
> once. **Una tasa que baja porque crece el denominador no dice nada bueno de nadie**, y la `ACTA
> 21` `12` ya avisaba de esta misma trampa. Con los dos pasos de transposicion de `P.3.b` contados
> como puente serian `19 de 205 = 9,27`.
>
> **2. El total del lote (`2,72`) SIGUE SIENDO UN SUELO, y la cifra la sume con la maquina despues
> de haberla tecleado mal.** Escribi `32` y `2,56` de cabeza; el sumatorio da **`34` y `2,72`**, y
> **publico el del sumatorio** (`EXTRACTOR.md` 5: la celda que no salga de un instrumento no se
> escribe). Lo dejo dicho porque es exactamente la especie de caida que esta casa cuenta. Seis filas sin leer con el ancho suman
> **97 ocurrencias** sin adjudicar. **La fila que decide no es el total: es la peor**, y la peor
> esta firmada.
