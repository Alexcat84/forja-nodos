# APERTURA CIEGA DE LA VUELTA 18, lote 4 (`scott_radical_candor`), `cap_08`

*Escrita por el auditor ANTES de ver `docs/loop/REPORTE.md`. `AUDITOR_FORJA.md` 1.5,
`D.34.2`, `D.38.3`, `D.38.4` y `D.40`.*

---

## 0. LA HERENCIA QUE `D.40` ME ENTREGA, DECLARADA ANTES DE NADA

    ACTA ANTERIOR LEIDA: a09c9ad9d4011419b5ec0c951e9628817c474f1f
    HEREDADO 1: CUMPLIDO
    HEREDADO 2: CUMPLIDO
    HEREDADO 3: CUMPLIDO EN CUATRO FILAS, NO APLICA EN UNA

*Las tres van con su motivo y su comprobacion debajo, una por una. El `NO APLICA`
de la quinta fila del heredado 3 lleva su motivo escrito en la tabla, que es lo que
`D.40` exige para que no cuente como que falta.*

**Y LA LEI DE VERDAD, QUE ES LO QUE LAS TRES VUELTAS ANTERIORES NO HICIERON.** La huella
que declaro no la copio del prompt: **la remido contra el arbol antes de escribirla**, que
es lo que `D.40` pide cuando dice que decir que leiste otra version no es haberla leido.

    $ git hash-object docs/loop/ACTA_AUDITOR.md
      a09c9ad9d4011419b5ec0c951e9628817c474f1f      <- identica a la del prompt
    $ wc -l docs/loop/ACTA_AUDITOR.md
      16577 docs/loop/ACTA_AUDITOR.md

**LO QUE ABRI DE ELLA, con su linea:** la seccion `7` entera (`L16445` a `L16503`, mis
caidas y mis remedios), la `8` (las rachas al cerrar, `L16507` a `L16520`), la `9` (`D.32`,
`L16524` a `L16538`), la `10` (las paradas repasadas) y la `11` (la tabla de cierre,
`L16562` a `L16577`). **Mas las lineas que necesite para adjudicar el `24` contra `25`**
(`L15782`, `L15788`, `L16154`, `L16423`, `L16568`), que estan en la seccion `8` de esta
apertura.

### HEREDADO 1: **CUMPLIDO**

*El remedio pedia dos comprobaciones y pedia correrlas sin releerme. Las corro sobre el
fichero que estoy escribiendo, que es donde el remedio manda que salgan.*

    $ grep -c "ACTA ANTERIOR LEIDA" docs/loop/APERTURA_CIEGA.md            ->  2   (mi remedio pide 1)
    $ grep -c "DISCREPANCIA: mi instrumento" docs/loop/APERTURA_CIEGA.md   ->  3   (mi remedio pide al menos 1)
    $ grep -c "ACTA_AUDITOR\|ACTA 17" docs/loop/APERTURA_CIEGA.md          -> 28   (mi remedio pide mayor que 0)

**LAS TRES CIFRAS SON LA SALIDA REAL DEL `grep` SOBRE ESTE FICHERO YA ESCRITO, Y NO LAS QUE
YO HABIA PUESTO.** Escribi `1`, `2` y *mayor que 0* de cabeza antes de correrlo; **al
correrlo dio `2`, `3` y `28`**, porque la propia linea de comprobacion contiene la cadena
que busca y se cuenta a si misma. **Las corrijo aqui en vez de dejar la cifra bonita**, que
es lo unico que `D.38.3` viene a impedir: **una cifra de esta fase sale del instrumento o no
se publica.** El remedio pedia *al menos uno* en las dos primeras y **las dos lo pasan**.

**Las dos discrepancias estan en las secciones `6.2` y `8`**, y las dos llevan la salida
del instrumento pegada. **No son de adorno para que el `grep` de uno:** una de ellas tumba
el metodo literal que `D.38.4` escribe.

### HEREDADO 2: **CUMPLIDO**, y digo por donde fallaba

**EL FALLO ERA DE FONDO Y NO DE ROTULO**, con mis palabras de la `ACTA 17` `7.1`: la
seccion 0 de aquella apertura listaba todo lo que habia leido y `docs/loop/ACTA_AUDITOR.md`
no estaba en la lista. **Hoy esta, y es lo primero de la lista**, con su huella remedida
arriba y con las lineas concretas que abri.

**LO QUE LO HIZO POSIBLE NO FUI YO ACORDANDOME**, y lo digo porque `D.35` dice que un
remedio que se cumple acordandose no es un remedio: **el arnes me entrego los tres
heredados en el prompt** (`D.40`), y el prompt me dijo con todas las letras que
`ACTA_AUDITOR.md` **no** es ninguno de los cuatro ficheros que `D.34.2` retira. **Las tres
vueltas anteriores me comporte como si estuviera prohibido abrirlo.**

### HEREDADO 3: **CUMPLIDO en cuatro filas, NO APLICA en una, y el motivo va escrito**

*`REMEDIO ROTO` solo informa si tambien se declara cuando aguanta. Esa era la mitad del
heredado 3, y por eso la tabla se repite entera en vez de darse por sabida.*

| remedio mio | comprobacion EN ESTA FASE | resultado |
|---|---|---|
| `D.38.4`, barrido sobre grafo mas bandejas | seccion `6`: **429 = 203 + 226** y **266** sin el catalogo de control, las dos con su `wc -l` | **CUMPLIDO**, y ademas **con una discrepancia contra el metodo literal de la regla** |
| `D.38.3`, toda cifra de esta fase con su instrumento al lado | toda cifra de este fichero lleva su comando pegado, incluida la frontera de `cap_08`, que la corta un guion y no mi ojo (seccion `3`) | **CUMPLIDO** |
| `D.34`, no recuperar de git los cuatro ficheros retirados | no corri `git show` ni `git checkout` sobre `REPORTE.md`, `loop.log`, `ultimo_extractor.json` ni `ultimo_auditor.json`. **Pero hay una contaminacion mia por otra via y la declaro entera en la seccion `1.2`** | **CUMPLIDO EN LA LETRA, con una falta propia declarada al lado** |
| `D.34`, no tocar `APERTURA_CIEGA.md` tras el sello | **NO APLICA TODAVIA, y este es el motivo: el sello no existe mientras escribo.** Lo pone el arnes al cerrar esta fase. La comprobacion es del cierre de mi turno normal y alli se publica con su `git hash-object` contra `SELLOS_APERTURA.jsonl` | **NO APLICA EN ESTA FASE** |
| `5.5`, re correr por mutacion toda guarda que el reporte declare mordiendo | **NO APLICA EN ESTA FASE, y este es el motivo: no he visto el reporte.** La regla muerde sobre *toda guarda que el reporte declare mordiendo*, y sin reporte no hay declaracion que re correr. Se cumple en mi turno normal | **NO APLICA EN ESTA FASE** |

---

## 1. LO QUE LEI, LO QUE NO, Y UNA CONTAMINACION MIA QUE DECLARO YO

### 1.1. Lo leido, con su ruta

| que | para que |
|---|---|
| `docs/loop/AUDITOR_FORJA.md`, **las 574 lineas** | mi protocolo. `$ wc -l` da `574` |
| `docs/loop/ACTA_AUDITOR.md` | **la herencia** (seccion `0`). Autorizado expresamente: no es de los cuatro de `D.34.2` |
| `docs/loop/PROMPT_SIGUIENTE.md`, **219 lineas** | el encargo bajo el que corrio la vuelta 18. Sede mia (`5.6`) |
| `docs/loop/ORDEN_DE_LOTES.md` | el lote, el tramo y la cifra que el fundador me sube para adjudicar |
| `docs/BANCO_DE_REGLAS.md` `L1426` a `L1498` | `D.38.4` y `D.39` literales |
| `fuentes/scott_radical_candor/cap_08.md`, **189 lineas** | **el texto fuente, entero** |
| `fuentes/scott_radical_candor/cap_07.md` `L150` a `L165` | el tramo del nodo que la TAREA 2 debia |
| los **63** candidatos de `cuarentena/scott_radical_candor/` | la bandeja entera, y los **13** de esta vuelta uno por uno con sus pasos |

**LO QUE NO ABRI, Y NO ESTABA:** `docs/loop/REPORTE.md`, `docs/loop/loop.log`,
`docs/loop/ultimo_extractor.json` y `docs/loop/ultimo_auditor.json`. **No los recupere de
git ni por ninguna otra via**, y `docs/loop/ultimo_apertura.json` **si** esta en el arbol
pero **esta vacio**, asi que tampoco dice nada:

    $ wc -c docs/loop/ultimo_apertura.json
      0 docs/loop/ultimo_apertura.json

### 1.2. **MI CONTAMINACION, Y LA DECLARO YO PORQUE NADIE MAS LA VE**

**PARA SABER QUE CANDIDATOS ERAN DE ESTA VUELTA CORRI ESTO:**

    $ git show --stat --name-only feaa14d

**Y ESE COMANDO NO TRAE SOLO LOS NOMBRES: TRAE EL CUERPO DEL MENSAJE DE COMMIT**, que en
esta casa es un resumen del reporte. **Lo lei antes de poder evitarlo.** Lo que vi, dicho
entero para que la comparacion posterior se pueda descontar:

- el saldo de la aduana que el extractor declara para los 12 de `cap_08`,
- que levanto **un** vecino y por que señal,
- el par concreto que leyo y su clase,
- su cifra de `PASOS INVENTADOS` de `cap_08` y del lote,
- y que la vuelta cierra en `cap_08` por el techo de candidatos.

**LO QUE HICE DESPUES, y es lo unico que puedo hacer:** todos los comandos siguientes
llevan `--format=""` y el mensaje no vuelve a salir. **Y mi clasificacion de la seccion `4`
la escribo contra el libro**, no contra ese saldo: cuando mi clase coincide con lo que vi,
**lo digo en la fila**, para que nadie cuente como acuerdo independiente lo que puede ser
eco.

> **Y HAY UNA SEGUNDA VIA QUE NO ES MIA Y TAMBIEN LA DIGO:** el propio prompt del arnes me
> entrega, en su bloque `gitStatus`, **los asuntos de los cinco ultimos commits**, y tres de
> ellos llevan cifras de la vuelta que vengo a auditar a ciegas (`12 candidatos, 102 pasos,
> cero puentes`, y `20 piezas, 12 nodos, 7 no extraidas`). **No es una falta mia y no la
> apunto como tal**, pero **es una fuga de la fase ciega** y el sitio de decirlo es este.
> **Mi frontera de la seccion `3` la corto con un guion sobre el fichero**, y da **18**
> piezas, no 20: **si hubiera querido copiar, habria copiado.**

---

## 2. EL ESTADO DEL ARBOL AL ABRIR, CIFRA A CIFRA Y CON SU COMANDO

    $ git rev-parse HEAD
      8da5e5e01a08d27e010c4deddafe58f8d7e2c21e
    $ wc -l dataset/nodos.jsonl
      203 dataset/nodos.jsonl
    $ wc -l bitacora/VEREDICTOS.jsonl
      148 bitacora/VEREDICTOS.jsonl
    $ ls cuarentena/scott_radical_candor/*.json | wc -l
      63
    $ ls fuentes/scott_radical_candor/*.md | wc -l
      15
    $ python (nodos del grafo cuya ficha de fuentes nombra scott_radical_candor)
      0

| | |
|---|---|
| **grafo** | **203 nodos**, los mismos con los que la `ACTA 17` cerro |
| **veredictos** | **148**, los mismos con los que la `ACTA 17` abrio y cerro. **La vuelta 18 no emitio ni uno** |
| **bandeja del lote 4** | **63 candidatos**, contra los **50** que la `ACTA 17` `9` dejo medidos. **La vuelta escribio 13** |
| **nodos del lote 4 en el grafo** | **0.** El lote sigue ABIERTO y `D.39` solo inserta lo CERRADO |

**LOS 13 DE LA VUELTA, Y COMO SE QUE SON ESOS 13:**

    $ git show --stat --name-only --format="" feaa14d | grep -c json   ->  12   (cap_08)
    $ git show --stat --name-only --format="" 22b6bb9 | grep -c json   ->   1   (el nodo que cap_07 debia)
    $ 12 + 1 = 13,  y  50 + 13 = 63, que cuadra con el ls de arriba

**LAS TRES MEDIDAS DE CUERPO DEL TRAMO, REMEDIDAS POR MI** porque el encargo dice que una
cifra suya no es fuente de una cifra mia (`EXTRACTOR.md` 5):

    $ sed -n '8,$p' fuentes/scott_radical_candor/cap_08.md | wc -w   ->   6140
    $ sed -n '8,$p' fuentes/scott_radical_candor/cap_09.md | wc -w   ->  17482
    $ sed -n '8,$p' fuentes/scott_radical_candor/cap_10.md | wc -w   ->   8976

**LAS TRES COINCIDEN AL DIGITO CON LA TABLA DE LA TAREA 3 DEL ENCARGO.** Y sostienen la
lectura que el encargo dejo escrita: **`cap_09` pesa mas que `cap_07`**, que dio 24
candidatos.

---

## 3. LA FRONTERA DE `cap_08` QUE YO CORTO, Y LA CORTA UN GUION

**`D.38.3` PROHIBE CONTAR A OJO, ASI QUE NO CUENTO LAS PIEZAS: LAS SACO CON UN FILTRO** y
despues declaro uno por uno los descartes, que es donde un guion se equivoca.

    $ python (linea no vacia, menos de 70 caracteres, sin punto final, desde L9)
      20 rotulos candidatos

| linea | rotulo | |
|---|---|---|
| `L9` | *An approach to establishing trust with your direct reports* | subtitulo del capitulo |
| `L15` | **STAY CENTERED** | seccion |
| `L25` | Work-life integration | |
| `L29` | Figure out your "recipe" to stay centered and stick to it | |
| `L37` | Calendar | |
| `L41` | Show up for yourself | |
| `L45` | **FREE AT WORK** | seccion |
| `L67` | **MASTER THE ART OF SOCIALIZING AT WORK** | seccion |
| `L77` | Even non-mandatory events can feel mandatory | |
| `L83` | Booze | |
| `L89` | **RESPECT BOUNDARIES** | seccion |
| `L93` | Building trust | |
| `L97` | Sharing values | |
| `L105` | Demonstrating openness | |
| `L123` | Physical space | |
| `L133` | *"Were you weirded out that a strange man hugged and kissed you?"* | **DESCARTADO: es dialogo dentro de `Physical space`**, no rotulo |
| `L151` | Recognizing your own emotions | |
| `L161` | Master your reactions to others' emotions | |
| `L183` | `* * *` | **DESCARTADO como rotulo: es el separador que abre el cierre** |
| `L189` | GUIDANCE | **DESCARTADO: es el titulo del capitulo SIGUIENTE**, ya fuera de `cap_08` |

**20 menos 3 descartes da 17 rotulos. Y las piezas son 18**, porque el cierre (`L185`) tiene
cuerpo y no tiene rotulo propio: lo abre el separador de `L183`.

### 3.1. Las 18 piezas, y cual se hizo nodo

| # | pieza | lineas de cuerpo | mi lectura |
|---:|---|---|---|
| 1 | cabeza del capitulo | `L11` a `L13` | **NO SE EXTRAE.** Es el mapa del capitulo (*this chapter will focus on inside out*). Un mapa sin sentidos no es medio mapa (`6.1`) |
| 2 | **STAY CENTERED**, cabeza sin rotulo propio | `L19` a `L23` | **NO SE EXTRAE.** Es la postura (*you can't give a damn about others if you don't take care of yourself*). **Una advertencia es linea, no nodo** |
| 3 | Work-life integration | `L27` | **NODO** |
| 4 | Figure out your "recipe" | `L31` a `L35` | **NODO** |
| 5 | Calendar | `L39` | **NODO, fundido con la 6** |
| 6 | Show up for yourself | `L43` | **fundida en la 5** |
| 7 | **FREE AT WORK** | `L47` a `L65` | **NODO.** La pieza mas grande del capitulo |
| 8 | **MASTER THE ART OF SOCIALIZING** | `L69` a `L75` | **NODO.** Cabecera de seccion que **si** trae procedimiento propio |
| 9 | Even non-mandatory events | `L79` a `L81` | **NODO** |
| 10 | Booze | `L85` a `L87` | **NO SE EXTRAE.** Es una lista de desastres en pasado, **sin un solo acto**: `D.27` no la deja pasar |
| 11 | **RESPECT BOUNDARIES**, cabeza sin rotulo propio | `L91` | **NO SE EXTRAE.** Declara que hay una linea fina y que no hay un sitio correcto para ella. **Postura, no procedimiento** |
| 12 | Building trust | `L95` | **NODO** |
| 13 | Sharing values | `L99` a `L103` | **NODO** |
| 14 | Demonstrating openness | `L107` a `L121` | **NODO** |
| 15 | Physical space | `L125` a `L149` | **NODO** |
| 16 | Recognizing your own emotions | `L153` a `L159` | **NODO** |
| 17 | Master your reactions to others' emotions | `L163` a `L181` | **NODO** |
| 18 | cierre | `L185` | **NO SE EXTRAE.** *Building relationships takes time and real energy.* Postura |

**MI CUENTA: 18 PIEZAS, 13 EXTRAIDAS, 12 NODOS (una fusion), 5 NO EXTRAIDAS CON SU MOTIVO.**
**13 mas 5 da 18, y 13 piezas menos 1 fusion da 12 nodos**, que es exactamente lo que la
bandeja tiene de `cap_08`.

---

## 4. MI CLASIFICACION, CANDIDATO POR CANDIDATO, ESCRITA CONTRA EL LIBRO

**LA VARA ES LA DE `6.1`:** el candidato **CONTINUA** el trabajo del existente o lo
**REPITE**; se pregunta que aniade el hijo a la madre y **nunca al reves**; **no hay
bascula**, y lo que decide es **si lo que queda fuera es procedimiento en los dos lados**.

    $ python (len(pasos_accionables) de los 12 de cap_08)   ->  102 pasos
    $ python (len(pasos_accionables) del nodo de cap_07)    ->    9 pasos
    $ 102 + 9 = 111 pasos escritos por la vuelta 18

| # | candidato | pieza | pasos | **mi clase** |
|---:|---|---|---:|---|
| 1 | `integrar_trabajo_vida_mejor_version` | 3, `L25` a `L27` | 5 | **ENTRARIA** |
| 2 | `definir_receta_propia_mantenerse_centrado` | 4, `L29` a `L35` | 9 | **ENTRARIA CON FRONTERA** contra 1 y 3 |
| 3 | `agendar_cuidados_propios_cumplirlos` | 5 mas 6, `L37` a `L43` | 5 | **DISCUTIBLE MIO.** Es la unica fusion del capitulo |
| 4 | `ceder_autoridad_unilateral_equipo` | 7, `L45` a `L65` | 15 | **DISCUTIBLE MIO.** Quince pasos en un solo nodo |
| 5 | `dominar_arte_socializar_trabajo` | 8, `L67` a `L75` | 9 | **ENTRARIA** |
| 6 | `evitar_presion_social_actos_equipo` | 9, `L77` a `L81` | 6 | **ENTRARIA** |
| 7 | `construir_confianza_equipo_tiempo_solas` | 12, `L93` a `L95` | 7 | **ENTRARIA** |
| 8 | `vivir_valores_propios_evitar_listarlos` | 13, `L97` a `L103` | 9 | **ENTRARIA** |
| 9 | `demostrar_apertura_visiones_distintas` | 14, `L105` a `L121` | 10 | **ENTRARIA** |
| 10 | `manejar_contacto_fisico_regla_platino` | 15, `L123` a `L149` | 9 | **ENTRARIA** |
| 11 | `reconocer_emociones_propias_avisar_equipo` | 16, `L151` a `L159` | 7 | **ENTRARIA** |
| 12 | `dominar_reacciones_emociones_ajenas` | 17, `L161` a `L181` | 11 | **ENTRARIA CON FRONTERA** contra 11 |
| 13 | `adaptar_escucha_cultura_ajena` | `cap_07` `L155` a `L163` | 9 | **ENTRARIA.** Es el nodo que la TAREA 2 debia |

### 4.1. El racimo de cuatro que este capitulo crea, y por que digo que no es duplicado

**`integrar_trabajo_vida`, `definir_receta_propia` y `agendar_cuidados_propios` salen de la
misma seccion `STAY CENTERED`, y en la bandeja ya vivia `cuidarse_agotamiento_centro_rueda`
de `cap_07`.** Cuatro nodos sobre cuidarse uno mismo es exactamente la forma que tiene una
duplicacion, **asi que lo leo despacio y con la vara, no con la bascula:**

| nodo | su entregable, que es lo que decide | procedimiento propio que los otros no traen |
|---|---|---|
| `integrar_trabajo_vida_mejor_version` | **el marco**: dejar de tratarlo como suma cero | *no lo pienses como equilibrio, pienselo como integracion*, y el doble impulso |
| `definir_receta_propia_mantenerse_centrado` | **la receta**: que cosas concretas, y con que cadencia | *haz lo que te funcione a ti*, prioriza cuando aprieta, y la señal de si funciona |
| `agendar_cuidados_propios_cumplirlos` | **la agenda**: donde vive la receta y como se defiende | ponerlo en el calendario, el tiempo de desplazamiento, y no dejar que te la pisen |
| `cuidarse_agotamiento_centro_rueda` (`cap_07`) | **el caso de Costolo**, ya en la bandeja | lo que hizo el, nombrado dentro de sus pasos |

**LOS TRES DE `cap_08` SON UNA CADENA, NO TRES COPIAS: marco, receta, agenda.** Lo que
queda fuera de cada uno **es procedimiento en los tres lados**, que es literalmente la
prueba de `6.1`. **ENTRARIAN los tres, y la frontera queda declarada aqui.**

### 4.2. **DISCUTIBLE MIO 1**: la fusion de `Calendar` con `Show up for yourself`

**ES LA UNICA FUSION DEL CAPITULO Y ROMPE EL CRITERIO DE CORTE QUE EL RESTO USA.** En las
otras diecisiete piezas el rotulo del libro es el corte; aqui dos rotulos dan un nodo.

**MI LECTURA, Y VA A FAVOR DE LA FUSION:** `L43` no tiene objeto propio. *Don't blow off
those meetings with yourself or let others schedule over them* **habla de unas reuniones
que no existen hasta que `L39` las crea.** Separada, `L43` seria un nodo de dos pasos **sin
entregable**: no se puede entregar "no saltarse" algo que otro nodo tiene que haber puesto
antes. **Es una restriccion sobre el objeto de la pieza 5, no una pieza con objeto.**

**LO SOSTENGO, Y DIGO QUE ME INCOMODA:** un criterio de corte que se rompe una vez de
dieciocho es un criterio que hay que poder defender esa vez. **Lo defiendo por el
entregable, que es la prueba de la casa, y no por el tamanio de las piezas.**

### 4.3. **DISCUTIBLE MIO 2**: quince pasos en `ceder_autoridad_unilateral_equipo`

**ES EL NODO MAS GRANDE DE LA VUELTA Y EL QUE MAS SE PARECE A DOS NODOS.** Dentro de sus
quince pasos hay un bloque que se sostiene solo:

| pasos | que son |
|---|---|
| `P1` a `P8`, `P13` a `P15` | soltar la autoridad unilateral: la orden, sus limites, y que no es abdicar |
| **`P9` a `P12`** | **los tres procesos de Google** (seleccion, ascenso, evaluacion), uno por uno, con su mecanica |

**`P9` A `P12` TIENEN PROCEDIMIENTO PROPIO Y ENTREGABLE PROPIO**, y por la vara de `6.1`
eso es justo lo que separa dos nodos. **Y AUN ASI NO PIDO PARTIRLO**, por una razon que
tambien es de la vara: **el libro los pone como el ejemplar de la orden, no como una receta
para ti.** `P13` lo dice con sus palabras: *valga o no el metodo extremo de Google para tu
empresa*. **Un caso que el propio texto marca como ajeno no es un procedimiento que el
lector ejecute**, y esta casa ya admite `TRANSCRIPCION DE CASO` con el caso dentro del paso.

**LO MARCO DISCUTIBLE ANTES DE SABER NADA, Y DIGO DE QUE LADO CAIGO: NO SE PARTE.**

### 4.4. La frontera entre las dos piezas de emociones, que es la mas fina del capitulo

`reconocer_emociones_propias_avisar_equipo` (`L151`) y `dominar_reacciones_emociones_ajenas`
(`L161`) son **vecinas de rotulo y vecinas de tema**, y el libro las separa por **de quien
son las emociones**:

| | de quien | el acto central |
|---|---|---|
| pieza 16 | **tuyas** | decirlo en voz alta para que no crean que es culpa suya |
| pieza 17 | **de los demas** | no intentar controlarlas, y dominar **tu reaccion** a ellas |

**LA DIRECCION LAS SEPARA Y NO HAY SOLAPE DE ACTOS: ENTRARIAN LAS DOS, con la frontera
escrita.**

---

## 5. LA FIDELIDAD `D.30`: LOS **111** PASOS CONTRA SU PARRAFO

**ES LA CIFRA QUE DESPUES FIRMO COMO `PASOS INVENTADOS`, Y `8.3` DICE QUE NO SE COPIA.**
Lei el capitulo entero antes de abrir un solo candidato, y despues cada paso contra la
linea que su cabecera cita.

**LAS CABECERAS DE PUNTERO, PRIMERO, PORQUE UN PASO FIEL A LA LINEA EQUIVOCADA NO ES FIEL:**

| candidato | declara | lo que hay en esas lineas | |
|---|---|---|---|
| `integrar_trabajo_vida` | `L25` a `L27` | rotulo `Work-life integration` y su cuerpo | **CUADRA** |
| `definir_receta_propia` | `L29` a `L35` | rotulo `Figure out your "recipe"` y sus tres parrafos | **CUADRA** |
| `agendar_cuidados_propios` | `L37` a `L43` | `Calendar` mas `Show up for yourself`, los dos con cuerpo | **CUADRA** |
| `ceder_autoridad_unilateral` | `L45` a `L65` | `FREE AT WORK` entero | **CUADRA** |
| `adaptar_escucha_cultura_ajena` | `cap_07` `L155` a `L163` | rotulo `Adapt to a culture of listening` y sus cuatro parrafos | **CUADRA** |

**LAS CINCO COMPROBADAS CONTRA EL FICHERO, no contra lo que la cabecera dice de si misma.**
Y las dos que el encargo mandaba arreglar en su TAREA `0.c` **estan arregladas**:

    crear_espacio_seguro_madurar_ideas_nuevas  -> ahora declara "lineas 177 a 195"      (declaraba 181 a 195)
    establecer_credibilidad_pericia_humildad   -> ahora declara "349 a 357 mas la 313"  (declaraba 349 a 357)

### 5.1. El resultado: **111 de 111 leidos, CERO PUENTES**

**LOS QUE FUI A BUSCAR PRIMERO son los que un puente suele usar de escondite:** el paso que
trae un nombre propio, la cifra, y la frase que suena a consejo de quien extrae.

| paso | de donde salia el riesgo | lo que dice el libro | |
|---|---|---|---|
| `manejar_contacto_fisico` `P3`, *aguanta el abrazo seis segundos* | una cifra | `L141`: *hold a hug for at least six seconds* | **TRANSCRIPCION** |
| `manejar_contacto_fisico` `P7`, la regla de platino | una regla con nombre | `L145`: las dos reglas, con su definicion | **TRANSCRIPCION** |
| `agendar_cuidados_propios` `P3`, *haz como si tuvieras que coger un tren* | suena a imagen del extractor | `L39`: *Pretend you have a train to catch* | **TRANSCRIPCION** |
| `ceder_autoridad_unilateral` `P8`, la anarquia peor que la tirania | una comparacion fuerte | `L55`: *the only thing worse than tyranny is anarchy* | **TRANSCRIPCION**, y con la direccion bien puesta |
| `ceder_autoridad_unilateral` `P10` a `P12`, los tres procesos de Google | tres mecanicas muy concretas | `L59`: expedientes hasta Larry Page, comite de iguales, 360 grados y calibrado | **TRANSCRIPCION** |
| `demostrar_apertura` `P10`, Dick Costolo y *you all* | un caso largo | `L115` a `L121` | **TRANSCRIPCION** |
| `evitar_presion_social` `P3`, Marissa Mayer y el barco | un caso con nombre | `L79` | **TRANSCRIPCION** |
| `dominar_reacciones` `P9` y `P10`, paniuelos y botellas de agua | dos trucos muy operativos | `L177` y `L179` | **TRANSCRIPCION** |
| `adaptar_escucha` `P1` a `P9`, Astrid Tuminez | el nodo que se debia, nueve pasos | `cap_07` `L157` a `L163`, los cinco medios uno a uno | **TRANSCRIPCION** |

**NO ENCONTRE NI UN PASO QUE EL LIBRO NO DIGA. `cap_08`: 0 de 102. El nodo de `cap_07`: 0 de
9.** Esa es la cifra que llevare a mi acta, **y la firmo con la misma limitacion que ya
firme en la `ACTA 17`**, porque sin ella el cero se lee como lo que no es:

> **`D.30` mide si el paso ESTA EN EL LIBRO. No mide si es un paso.** Este capitulo tiene
> muchos *cuenta con que...* que son transcripcion perfecta y que nadie ejecuta. **Eso lo
> mide `D.27`, que es otra vara y no entra en esta cifra.** No propongo tocar ninguna.

### 5.2. **LO UNICO QUE ENCONTRE, y es un desvio de atribucion, no un puente**

`integrar_trabajo_vida_mejor_version` `P4` dice *el texto pone de ejemplo las ocho horas de
suenio que **su autora** necesita*. **Su cabecera cita `L25` a `L27`, y `L27` no se lo
atribuye a la autora: se lo dice al lector** (*If **you** need to get eight hours of sleep
to stay centered*). **Quien duerme ocho horas como receta propia es la autora en `L35`**,
que es cuerpo de **otra** pieza, la 4.

    $ sed -n '27p' cap_08.md   ->  "If you need to get eight hours of sleep to stay centered..."
    $ sed -n '35p' cap_08.md   ->  "Here's what I need to do to stay centered: sleep eight hours..."

**POR QUE NO ES PUENTE:** el hecho **esta en el capitulo**, en `L35`, y `D.30` mide si el
paso esta en el libro. **POR QUE LO DECLARO IGUAL:** la misma cifra aparece en `P6` de
`definir_receta_propia`, **que es el nodo al que `L35` pertenece**, asi que el dato vive en
dos nodos y **en uno de los dos esta mal atribuido**. Es de la familia de las dos cabeceras
de puntero que la TAREA `0.c` mando arreglar. **Lo subo a mi turno normal para adjudicar su
sede: un `resumen_teorico` de cuarentena no es sede de `CIFRA PUBLICADA` (`5.2`).**

---

## 6. EL BARRIDO DE VECINOS SOBRE **GRAFO MAS BANDEJAS** (`D.38.4`)

### 6.1. Las dos poblaciones, con su `wc -l`

    $ wc -l dataset/nodos.jsonl
      203
    $ ls cuarentena/*/*.json | grep -v _insertados | grep -v _derivadas | wc -l
      226        (163 del catalogo de control ensayo_referencia_163  +  63 del lote 4)
    $ wc -l pob_todo.jsonl
      429        <- 203 + 226, LA POBLACION DE LA REGLA, con el catalogo de control dentro
    $ wc -l pob_sin_control.jsonl
      266        <- 203 + 63, la misma sin el catalogo de control

**BARRI CONTRA LA DE 429, QUE ES LA LITERAL DE `D.38.4`** (todo lo que espera en
`cuarentena/<libro>/` descartando `_insertados` y `_derivadas`), **y publico las dos**
porque `ensayo_referencia_163` es el catalogo con el que se estreno la aduana
(`docs/ESTRENO_DE_LA_ADUANA.md`), de dominio `quality` y de otro libro: **no es material de
esta campania y quien lea la cifra tiene derecho a saber cual es cual.** Barrer con el
dentro es la lectura **conservadora**: mas vecinos posibles, no menos.

### 6.2. **DISCREPANCIA: mi instrumento contra el metodo literal de `D.38.4`**

**LA RECETA DE `D.38.4`, CORRIDA TAL COMO ESTA ESCRITA, NO DEVUELVE NI UN VECINO.** La
corri primero asi, y esta es su salida:

    $ FORJA_DATASET=<grafo mas bandejas> python forja.py informe --carpeta cuarentena/scott_radical_candor
      candidatos revisados        : 63
      nodos en el grafo de destino: 429
      ENTRARIAN  0  |  BLOQUEARIAN  0  |  CAERIAN  63  |  CHOCAN  0
      POR QUE GUARDA CAEN
          63  el id ya vive en el grafo

**LOS 63 CAEN CONTRA SI MISMOS.** La receta mete la bandeja en la poblacion **y despues
barre esa misma bandeja**, asi que cada candidato se encuentra a si mismo, la guarda de id
muerde primero y **corta antes de llegar a buscar vecinos.** Con la receta literal, un
auditor que la cumpla al pie de la letra publica **cero vecinos** y cree que ha barrido.

**LO QUE CORRI EN SU LUGAR, Y ES LA MISMA REGLA SIN SU ERRATA:** la poblacion entera
**menos el propio candidato**, uno por uno, trece veces.

    $ por cada candidato: poblacion = 429 - 1 = 428, y forja.py informe sobre ese candidato
      13 corridas, "poblacion: 428" en las 13

**UN NODO NO ES VECINO DE SI MISMO.** No ensancho la regla ni la estrecho: **quito de la
poblacion lo unico que la regla no podia querer dentro.** `D.38.4` dice que la poblacion es
*la que el extractor tuvo delante*, y el extractor no tenia el candidato dentro del grafo
cuando lo midio.

> **NO LO ARREGLO EN EL BANCO Y DIGO POR QUE:** tocar `D.38.4` es doctrina y **no es mio**
> (`6.3`: ninguna vuelta mueve la vara sin correccion declarada de Alexis). **Lo declaro
> aqui con su salida, que es lo que `AUDITOR_FORJA.md` 1.1 manda hacer con una discrepancia,
> y lo subo a mi turno normal.** Y digo lo que veo sin ir mas alla de lo que mido: **la
> `ACTA 17` publico `416 = 203 + 213` y su testigo dice `contra 415 titulos`**, que es
> `416 - 1`. **La resta estaba bien hecha alli**, asi que aquella vuelta ya barrio con la
> exclusion puesta **y no dejo escrito que la receta del banco no la trae.**

### 6.3. El saldo del barrido: **8 ENTRARIA, 5 BLOQUEARIA, 10 vecinos levantados**

| candidato | saldo | vecinos | señal |
|---|---|---:|---|
| `agendar_cuidados_propios_cumplirlos` | **ENTRARIA** | 0 | |
| `ceder_autoridad_unilateral_equipo` | **ENTRARIA** | 0 | |
| `definir_receta_propia_mantenerse_centrado` | **ENTRARIA** | 0 | |
| `demostrar_apertura_visiones_distintas` | **ENTRARIA** | 0 | |
| `dominar_arte_socializar_trabajo` | **ENTRARIA** | 0 | |
| `dominar_reacciones_emociones_ajenas` | **ENTRARIA** | 0 | |
| `integrar_trabajo_vida_mejor_version` | **ENTRARIA** | 0 | |
| `manejar_contacto_fisico_regla_platino` | **ENTRARIA** | 0 | |
| `construir_confianza_equipo_tiempo_solas` | **BLOQUEARIA** | 2 | `similitud_texto` |
| `evitar_presion_social_actos_equipo` | **BLOQUEARIA** | 2 | `similitud_texto` |
| `reconocer_emociones_propias_avisar_equipo` | **BLOQUEARIA** | 4 | `similitud_texto` |
| `vivir_valores_propios_evitar_listarlos` | **BLOQUEARIA** | 1 | **`paso_contra_nodo`** |
| `adaptar_escucha_cultura_ajena` | **BLOQUEARIA** | 1 | **`familia_id`** |

**QUE SEÑAL PAGA LA COLA: `similitud_texto` 8, `paso_contra_nodo` 1, `familia_id` 1.** Las
tres pagan algo, y la mas alta de todo el barrido es un `paso_contra_nodo` de **0,606**.

**Y LOS 10 SON 9 PARES**, porque `construir_confianza` y `reconocer_emociones` se levantan
**el uno al otro**: la pareja sale dos veces, una desde cada lado.

### 6.4. Los 9 pares, leidos por los pasos y **no por la señal** (`D.19`)

*`D.19`: ninguna señal separa jerarquia de ruido, asi que una discrepancia NUNCA se adjudica
citando una señal. **La señal dijo donde mirar y ahi acabo su trabajo.***

| # | par | lo que comparten | lo que los separa | **mi clase** |
|---:|---|---|---|---|
| 1 | `adaptar_escucha_cultura_ajena` contra `crear_cultura_escucha_equipo` | la palabra *escucha*, y el mismo capitulo | **la direccion**: uno monta un sistema de ideas y quejas **en TU equipo**; el otro te cambia a TI cuando **el extranjero eres tu**. Los cinco medios (citas sueltas, actos publicos, no encadenar, comida de verdad) **no estan en ninguno de los 17 pasos del otro** | **SANO** |
| 2 | `vivir_valores_propios` contra `sostener_contacto_oferta_aceptacion` | el verbo *mantener* y el sustantivo *contacto* | uno mantiene el contacto **con tus propios valores**; el otro, **con un candidato al que ya le hiciste la oferta**. Dominios distintos y libros distintos | **SANO** |
| 3 | `evitar_presion_social` contra `proteger_tiempo_equipo_jefe` | proteger el tiempo del equipo, y *dejarles irse a casa* | uno habla de **actos sociales** organizados para hacer equipo; el otro de **reuniones, analisis y mandatos de arriba**. Ni un acto se repite | **SANO**, frontera declarada |
| 4 | `evitar_presion_social` contra `crear_obligacion_disentir_equipo` | la palabra *presion*, y *todos de acuerdo* | uno es higiene del **debate**; el otro, de la **fiesta**. Ningun paso se toca | **SANO** |
| 5 | `reconocer_emociones_propias` contra `cuidarse_agotamiento_centro_rueda` | el estado de animo **del jefe** | uno **se cuida** (declinar invitaciones, bloquear tiempo de pensar); el otro **lo dice en voz alta** para que el equipo no crea que es culpa suya. **Cuidarse no es avisar** | **SANO**, y es el quinto del racimo de `4.1` |
| 6 | `reconocer_emociones_propias` contra `construir_confianza_equipo_tiempo_solas` | los dos construyen confianza | uno la construye con **tiempo a solas y regular**; el otro, con **una frase el dia que llegas de mal humor** | **SANO** |
| 7 | `reconocer_emociones_propias` contra `centrar_debate_ideas_fuera_egos` | la palabra *emocion* cerca de *reunion* | uno saca **los egos** del debate; el otro pone **tu animo** encima de la mesa | **SANO** |
| 8 | `reconocer_emociones_propias` contra `minimizar_impuesto_colaboracion_equipo` | *lo que el jefe se echa encima* | uno se echa encima **el impuesto de colaboracion**; el otro, **el aviso de su mal dia** | **SANO** |
| 9 | `construir_confianza` contra `minimizar_impuesto_colaboracion_equipo` | el tiempo del jefe repartido | uno **pasa tiempo a solas** con cada uno; el otro **se come la carga de coordinar** para que el equipo no la tenga | **SANO** |

**NUEVE PARES LEIDOS, NUEVE SANOS, CERO DUPLICADOS. MI SALDO DE LECTURA: LOS 13 ENTRARIAN.**

### 6.5. La frontera que el instrumento **NO** levanto, y la escribo igual

**`agendar_cuidados_propios_cumplirlos` salio con CERO vecinos**, y en la misma bandeja hay
**dos nodos mas que mandan bloquear tiempo en el calendario**:

| nodo | que bloquea en el calendario |
|---|---|
| `agendar_cuidados_propios_cumplirlos` (nuevo) | **lo que necesitas para ti**: la receta, el tiempo de desplazamiento |
| `reservar_calendario_tiempo_ejecutar` (bandeja) | **el tiempo de ejecutar**, que es solitario y por eso nunca se apunta |
| `cuidarse_agotamiento_centro_rueda` `P7` (bandeja) | **dos horas de tiempo de pensar al dia** |

**TRES OBJETOS DISTINTOS EN EL MISMO VERBO.** Por `6.1` no hay bascula y lo que decide es si
lo que queda fuera es procedimiento en los tres lados: **lo es** (el tren y la cena en uno,
el sesgo del calendario colaborativo en otro, declinar invitaciones en el tercero).
**ENTRARIAN los tres, y la frontera queda escrita aqui porque ninguna señal la vio.**

> **ES EL AVISO DE `D.19` AL REVES Y POR ESO LO DEJO ANOTADO:** la señal no solo levanta
> ruido (los nueve pares de `6.4`), **tambien se calla donde hay tema.** Ninguna de las dos
> cosas adjudica: adjudica la lectura.

---

## 7. MIS DISCUTIBLES, MARCADOS AQUI Y NO DESPUES

**LOS MARCO EN ESTE FICHERO, QUE ES EL QUE EL ARNES SELLA**, porque un discutible que
aparece despues de ver el reporte no es un discutible: es una respuesta.

| # | discutible mio | donde | de que lado caigo |
|---:|---|---|---|
| 1 | la fusion de `Calendar` con `Show up for yourself`, unico corte del capitulo que no sigue al rotulo | `4.2` | **A FAVOR de la fusion**, por el entregable |
| 2 | los quince pasos de `ceder_autoridad_unilateral_equipo`, con `P9` a `P12` sosteniendose solos | `4.3` | **NO SE PARTE**, porque el libro marca el caso como ajeno |
| 3 | el racimo de cuatro nodos sobre cuidarse uno mismo | `4.1` | **LOS CUATRO ENTRAN**, y la frontera queda escrita |
| 4 | la frontera entre las dos piezas de emociones, la mas fina del capitulo | `4.4` | **LAS DOS ENTRAN**, las separa la direccion |
| 5 | las ocho horas de suenio atribuidas a la autora donde `L27` se las dice al lector | `5.2` | **NO ES PUENTE**, pero el dato vive en dos nodos y en uno esta mal atribuido |
| 6 | `Booze` (`L85` a `L87`) fuera, siendo pieza con rotulo propio | `3.1` | **BIEN FUERA**: lista de desastres en pasado, cero actos |
| 7 | **la vuelta cierra en `cap_08` con 13 candidatos y el techo son 15**: ningun capitulo paso del techo | `7.1` | **BIEN CERRADA, pero por EXTENSION de `12.4` y no por su letra** |

---

### 7.1. **DISCUTIBLE 7: el cierre corto que ningun capitulo disparo**

**`EXTRACTOR.md` 12.4 dispara cuando UN SOLO CAPITULO PASA DEL TECHO.** Esta vuelta escribio
**13** candidatos y el techo son **15**, y `cap_08` dio **12**. **Por la letra de la regla,
el disparador NO se cumplio: ningun capitulo paso de nada.**

**LO QUE SI MIDO, Y ES LO QUE SOSTIENE EL CIERRE:**

    $ python (candidatos por unidad contra palabras de cuerpo, sobre la bandeja)
      cap_07   25 candidatos | 13678 palabras |  547 palabras por candidato
      cap_08   12 candidatos |  6140 palabras |  512 palabras por candidato

    $ proyeccion de cap_09 (17482 palabras) con esas dos densidades
      con 512 -> 34 candidatos     con 547 -> 32 candidatos
    $ proyeccion de cap_10 (8976 palabras)
      con 512 -> 18 candidatos     con 547 -> 16 candidatos

**`cap_09` SOLO DA ENTRE 32 Y 34, QUE ES MAS DEL DOBLE DEL TECHO.** Y la regla dice tambien
que **un capitulo no se parte en dos vueltas**. Las dos frases juntas dejan una sola salida
que no rompa ninguna: **no abrir `cap_09` en esta vuelta.** Abrirlo habria dado una vuelta
de **47** candidatos, que es exactamente el danio que el techo existe para impedir.

> **POR ESO LO LLAMO EXTENSION Y NO LETRA, y lo marco antes de ver el reporte:** la regla
> escrita **reacciona** a un capitulo que ya paso del techo; esta vuelta **se adelanto** a
> uno que iba a pasarlo. **Es la misma finalidad y no es la misma orden.** `AUDITOR_FORJA.md`
> 1.3 dice que si una regla escrita cubre el caso **por extension natural, se adjudica
> citandola**, y que solo es PARADA si hace falta doctrina NUEVA. **Mi lectura es que esta la
> cubre por extension natural, y lo adjudico asi en mi turno normal.**
>
> **LO QUE ME QUEDA POR VERIFICAR Y NO PUEDO EN ESTA FASE** (`8.1`, *lo que te toca
> verificar*): **que la vuelta lo DECLARO con su cifra.** Una vuelta que cierra corto y no lo
> dice es caida de especie `REPORTE`. **El reporte es de los cuatro retirados y no lo he
> visto**, asi que esto queda apuntado aqui y se comprueba en mi turno normal.

**UNA LIMITACION DEL INSTRUMENTO, DICHA:** la cuenta por unidad sale de buscar `cap_NN` en
el `resumen_teorico`, y **24 de los 63 candidatos de la bandeja no lo nombran** (los de
vueltas anteriores). **Por eso la tabla solo publica `cap_07` y `cap_08`, que son las dos
unidades cuyos candidatos si lo declaran**, y no una densidad del lote entero que el
instrumento no puede sostener.

**Y UN CRUCE QUE SALE GRATIS Y CONFIRMA LA SECCION `8`:** ese mismo instrumento cuenta
**25** candidatos de `cap_07`, no 24, **porque incluye el nodo de la TAREA 2 de esta
vuelta**. Es la tercera medida independiente de que 24 y 25 cuentan cosas distintas.

---

## 8. LA CIFRA QUE EL ENCARGO ME SUBE PARA ADJUDICAR: **`24` CONTRA `25`**

*`PROMPT_SIGUIENTE.md` TAREA `0.b`, y `ORDEN_DE_LOTES.md` en su correccion del 12 sep 2026:
mi propia `ACTA 17` dice `25 candidatos` en su `5.2` y `24` en su `1.3`. El encargo me pide
que remida con mi instrumento y que publique **cual de las dos es la falsa**.*

**LA ADJUDICO, Y LA RESPUESTA ES QUE NINGUNA DE LAS DOS ES FALSA: CUENTAN COSAS DISTINTAS.**

    $ git show --stat --name-only --format="" 28651cf | grep -c "cuarentena/scott_radical_candor/.*json"
      24      <- los candidatos de cap_07
    $ git show --stat --name-only --format="" ab06569 | grep "cuarentena/scott_radical_candor/.*json"
      cuarentena/scott_radical_candor/reparar_mal_comportamiento_evitar_disculpa_falsa.json
      1       <- el nodo de la pieza 12 de cap_05, TAREA 3 de aquella vuelta
    $ 24 + 1 = 25 candidatos escritos por la vuelta 17

**Y CUADRA POR EL OTRO LADO, con la bandeja:** la `ACTA 16` midio **25** candidatos en la
bandeja (`L15782`, con 7 de 15 unidades minadas) y la `ACTA 17` midio **50** (`L16528`, con
8 de 15). **25 mas 25 da 50.**

| cifra | donde | que cuenta | |
|---|---|---|---|
| **24** | `ACTA 17` `1.3` (`L16154`) y su tabla de cierre (`L16568`) | **los candidatos de `cap_07`** | **CIERTA** |
| **25** | `ACTA 17` `5.2` (`L16423`) | **los candidatos que la vuelta 17 escribio**, `cap_07` mas el nodo de `cap_05` | **CIERTA** |

**LAS DOS MEDIDAS QUE EL FUNDADOR FIRMO MIDEN `cap_07`**, y por eso dan 24: el
`grep -l "cap_07"` **no puede ver** un nodo que sale de `cap_05`. **Firmar el 24 fue
correcto para lo que se estaba midiendo, y no refuta el 25.**

> **`CIFRA PUBLICADA PROPIA`: NO ACUMULA, Y NO POR BENEVOLENCIA CONMIGO MISMO.** `D.38.2`
> define la especie como **una cifra FALSA** en mi acta, y aqui no hay ninguna falsa: hay
> **dos denominadores sin nombrar**. **LO QUE SI ES CAIDA, Y LA DECLARO, ES DE REDACCION:**
> la `5.2` escribio *LA VUELTA 17 ESCRIBIO 25 CANDIDATOS* sin decir que uno era de `cap_05`,
> **y por eso costo una tarea del encargo siguiente y una correccion declarada en
> `ORDEN_DE_LOTES.md`.** Una cifra cierta que obliga a tres documentos a perseguirla **es
> una cifra mal escrita**, aunque no sea una cifra falsa.

**DISCREPANCIA: mi instrumento contra una nota vieja.** La correccion declarada de
`ORDEN_DE_LOTES.md` dice *el `25` de la `5.2` queda sin reproducir*. **Lo reproduzco arriba
con dos comandos**, asi que esa frase queda superada por medida, y **no la resuelvo
copiando: la declaro** (`AUDITOR_FORJA.md` 1.1).

---

## 9. **MI CAIDA DE ESTA FASE, PILLADA EN EL ACTO Y POR MI: CUARTA VUELTA SEGUIDA**

**LA `ACTA 17` `7.3` DECLARO ESTO MISMO POR TERCERA VEZ SEGUIDA.** Lo vuelvo a hacer hoy,
y lo mido antes de que lo mida nadie:

    $ python forja.py guiones
      BARRIDO DE GUIONES EN ROJO: 18 hallazgo(s)
        .barrido_aud18/pob_todo.jsonl linea 275 columna 1687: guion largo (U+2014)
        .barrido_aud18/pob_uno.jsonl  linea 275 columna 1687: guion largo (U+2014)
        ... (18 en total, TODOS de esos dos ficheros mios)

**DIECIOCHO HALLAZGOS, DOS FICHEROS MIOS DE USAR Y TIRAR, ESCRITOS DENTRO DEL ARBOL.** Es
**el mismo numero y la misma forma** que la `ACTA 17` `7.3`. Los guiones no son mios ni del
extractor: **son del libro**, y entran en mi fichero de poblacion porque el barrido de
`D.38.4` copia los nodos tal cual.

**Y LA REGLA QUE ME LO DECIA ESTA DENTRO DE `D.38.4`, QUE ES LA QUE YO ESTABA CUMPLIENDO:**
su ejemplo escribe la poblacion en **`/tmp/poblacion.jsonl`**. **Yo la escribi en
`.barrido_aud18/`, dentro del repo.** Cumpli el fondo de la regla y rompi su ejemplo.

**LO REMEDIADO EN ESTA MISMA FASE**, con la salida de despues pegada en la seccion `10`:
todo mi material de usar y tirar se movio a `/tmp/aud18/`, **fuera del arbol**, y el barrido
se remidio en verde.

> ### **Y AQUI VA LO QUE `5.5` ME OBLIGA A ESCRIBIR, PORQUE SON CUATRO SEGUIDAS**
>
> *La caida del auditor gana dientes: **tres actas seguidas con la misma caida propia obligan
> a que el acta siguiente ABRA con su remedio como tarea bloqueante del propio auditor.***
>
> **YA VAN CUATRO, Y LAS CUATRO LAS ARREGLE A MANO Y A TIEMPO.** Ese es el problema, no la
> disculpa: `D.35` dice que **un remedio que se cumple acordandose no es un remedio**, y
> acordarse es exactamente lo unico que ha impedido el rojo las cuatro veces.
>
> **TAREA BLOQUEANTE DEL AUDITOR DE LA VUELTA 19, ESCRITA POR EL AUDITOR DE LA 18.** Y no es
> una orden de acordarse: **es una de no poder olvidarse.**
>
> > **TODO FICHERO DE USAR Y TIRAR DE LA FASE CIEGA SE ESCRIBE EN `/tmp/`, Y LA APERTURA LO
> > DEMUESTRA CON UNA SALIDA, NO CON UNA PROMESA.** La comprobacion es **una orden y se corre
> > sin leerme**:
> >
> >     $ git status --porcelain | grep -v "^ M docs/loop/APERTURA_CIEGA.md"
> >       (tiene que salir VACIO antes del sello)
> >     $ python forja.py guiones
> >       (tiene que salir en VERDE, y su salida va pegada en la apertura)
>
> **NO PIDO MAQUINARIA NUEVA Y DIGO POR QUE:** la moratoria de `5.5` (cosecha `7.F`) me
> prohibe encargar arneses, y ademas **no hace falta ninguno**: `forja.py guiones` ya existe,
> ya muerde, y es el que me ha pillado las cuatro veces. **Lo que faltaba no era el
> instrumento: era correrlo antes del sello en vez de despues.**

### 9.1. **Y AL IR A LIMPIAR ENCONTRE QUE LA VEZ ANTERIOR NO SE LIMPIO: SE COMMITEO**

**ESTO NO LO FUI A BUSCAR: SALIO DE MIRAR QUE HABIA EN EL ARBOL ANTES DE ENSUCIARLO YO.**

    $ git status --porcelain
      ?? .barrido_v18/pob.jsonl          <- 765 KB, sin seguir, ya estaba al abrir mi turno
    $ git ls-files .barrido_v18/ | wc -l
      6                                  <- SEIS ficheros mios DENTRO del repo, seguidos
    $ ls .frontera_auditor_v18.py
      .frontera_auditor_v18.py           <- el SEPTIMO, tambien seguido
    $ git log --oneline --diff-filter=A -- .barrido_v18/ .frontera_auditor_v18.py
      329c080 ACTA 17: la vuelta 17 verificada entera y limpia, y LA PARADA POR MI PROPIA RACHA

**LOS SIETE ENTRARON EN EL COMMIT DE LA `ACTA 17`, QUE ES MIO**, el 12 sep 2026 a las
06:39. `barrer.py`, `barrer2.py`, `nuevos.txt`, `faltan.txt`, `BARRIDO_NUEVOS.txt`,
`BARRIDO_RESTO.txt` y `.frontera_auditor_v18.py`: **mi maquinaria de usar y tirar de aquella
fase ciega, ahora permanente en el repo.**

**Y NINGUNO ESTA CITADO EN LA `ACTA 17`:**

    $ grep -c "barrido_v18" docs/loop/ACTA_AUDITOR.md        ->  0
    $ grep -c "frontera_auditor" docs/loop/ACTA_AUDITOR.md   ->  0

**ESO ES LO QUE LOS DEJA SIN DEFENSA.** `5.5` (*la ruta que promete prueba es cifra*) haria
obligatorio meter un testigo **que el acta cite**: un informe que dice *de estos 163, 49
caerian* solo se comprueba si el material viaja, y por eso `.gitignore` deja viajar
`cuarentena/`. **Pero un fichero que ninguna sede nombra no prueba nada: solo pesa.**

> **LO QUE ESTO LE HACE A MI `ACTA 17` `7.3`.** Alli escribi *limpiado y remedido, con las
> dos salidas pegadas*. **Era cierto de lo que decia y corto de lo que callaba:** limpie los
> **dos** ficheros que `forja.py guiones` me senialo, **y los otros siete se fueron dentro
> del commit.** El barrido de guiones no los vio porque **no tienen guiones**: el grafo no
> los tiene, y los guiones de mi poblacion de hoy venian de los candidatos de Scott.
>
> **LA LECCION, Y ES LA QUE HACE FALTA PARA QUE EL REMEDIO SIRVA: `forja.py guiones` NO ES
> UN DETECTOR DE SUCIEDAD, ES UN DETECTOR DE GUIONES.** Mi remedio de arriba se apoyaba en
> el, y solo con el habria vuelto a dejar pasar estos siete. **Por eso la tarea bloqueante
> lleva `git status --porcelain` DELANTE del barrido y no detras: el que caza esta familia es
> el primero.**

**QUE PIDO QUE SE HAGA CON ELLOS: NADA, TODAVIA.** Borrar contenido que ninguna regla manda
borrar **esta reservado a Alexis** (`AUDITOR_FORJA.md` 3), y `D.33` protege los artefactos
del arnes. **Estos no son del arnes** (ningun `.sh` de la casa los escribe; los escribi yo),
**pero la retirada de siete ficheros ya commiteados es una decision suya y no mia.** Va a mi
turno normal con esta medida delante, **y el untracked de 765 KB con ella.**

**NO LO APUNTO COMO CAIDA NUEVA:** es **la misma** caida de la `7.3`, vista entera. Lo que
cambia no es la cuenta, **es el remedio**, que ahora sabe que instrumento le faltaba.

**NO ACUMULA EN MI RACHA, Y LO DIGO CON LA LETRA DELANTE**, que es lo mismo que dije las
tres veces anteriores y por eso mismo lo vuelvo a subir: `D.38.2` me da **dos** especies,
`REMEDIO ROTO` y `CIFRA PUBLICADA PROPIA`, **y ensuciar el arbol no es ninguna de las dos.**
**Es la cuarta vuelta seguida que este hueco me beneficia.** Por eso el remedio de arriba lo
escribo como tarea bloqueante **y no como una nota**: es lo unico que `5.5` me deja hacer
sin absolverme ni legislar.

---

## 10. EL ARBOL AL CERRAR ESTA FASE, Y LA PRUEBA DE QUE LO DEJE LIMPIO

*Es la mitad que las cuatro vueltas anteriores se saltaron: **el remedio no vale como
promesa, vale como salida.***

    $ mv .barrido_aud18 /tmp/aud18/barrido_aud18     (todo mi material de usar y tirar, FUERA del arbol)

    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ git status --porcelain
       M docs/loop/APERTURA_CIEGA.md      <- este fichero, que es lo que vengo a escribir
       D docs/loop/REPORTE.md             \
       D docs/loop/loop.log                |  los CUATRO que el arnes retira (D.34.2),
       D docs/loop/ultimo_auditor.json     |  y que yo no he tocado
       D docs/loop/ultimo_extractor.json  /
       M docs/loop/ultimo_apertura.json   <- del arnes, y hoy en CERO bytes
      ?? .barrido_v18/pob.jsonl           <- NO ES DE ESTA VUELTA: es el resto de la ACTA 17, seccion 9.1

**NADA MIO DE HOY QUEDA EN EL ARBOL.** El unico `??` que sale es el que la seccion `9.1`
denuncia, **y lo dejo a proposito: borrarlo seria borrar la prueba de lo que estoy
declarando**, y ademas retirar ficheros que ninguna regla manda retirar **es de Alexis**
(`AUDITOR_FORJA.md` 3).

### 10.1. Las cinco guardas, corridas por mi en esta fase

    $ python forja.py gate
      GATE VERDE.  nodos verificados: 203
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada,
               vuelta, cita_incompleta, deprecado_en_superficie, arista_rota,
               arista_incompleta, guiones

    $ python forja.py resolutor
      nodos vivos: 203 | nodos deprecados (archivo): 0 | alias registrados: 0

    $ python forja.py rancios
      BLOQUE DE VIGENCIA VERDE.  veredictos comprobados: 148
      todos siguen emitidos contra el texto que leyeron

    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE.

    $ python tests/test_aceptacion.py
      total: 84 pruebas, 0 fallos, 0 errores

**LAS CINCO EN VERDE.** Y una cifra que cruza sola: **84 pruebas, contra las 77 que mi
`ACTA 17` publico.** Las **siete** de diferencia son las que el encargo anuncio en su
TAREA `1.c`, y el propio banco de pruebas las nombra: *`D.40`, lo que un auditor le deja al
siguiente lo entrega el arnes: 7 pruebas mas*. **La herencia que me llego en el prompt tiene
su instrumento en verde detras, y lo compruebo yo.**

**LO QUE NO CORRO EN ESTA FASE, CON SU MOTIVO ESCRITO:** las **mutaciones** de `5.5`. La
regla dice que se re corre por mutacion *toda guarda que el REPORTE declare mordiendo*, y
**el reporte es uno de los cuatro retirados.** Sin declaracion no hay nada que mutar.
**Van en mi turno normal**, y esa es la fila `NO APLICA` de mi tabla del heredado 3.

---

## 11. LO QUE ESTA APERTURA DEJA DICHO, EN UNA TABLA

| | |
|---|---|
| **vuelta que audito** | 18, lote 4 (`scott_radical_candor`), `cap_08` (`Cap. 5`, *Relationships*) |
| **hash al abrir mi turno** | `8da5e5e01a08d27e010c4deddafe58f8d7e2c21e` |
| **acta anterior leida** | `a09c9ad9d4011419b5ec0c951e9628817c474f1f`, **remedida contra el arbol con `git hash-object`** |
| **herencia `D.40`** | **HEREDADO 1 CUMPLIDO. HEREDADO 2 CUMPLIDO. HEREDADO 3: cuatro filas CUMPLIDAS y una NO APLICA con su motivo** |
| **piezas del capitulo** | **18**, cortadas por un filtro y con los **3** descartes nombrados uno a uno |
| **candidatos clasificados a ciegas** | **13** (12 de `cap_08` mas el nodo que `cap_07` debia) |
| **mi saldo de lectura** | **13 ENTRARIAN.** Ninguno repite a nadie |
| **barrido de vecinos** | poblacion **429 = 203 + 226** (y **266** sin el catalogo de control); cada candidato contra **428**; **10 vecinos, 9 pares, 9 SANO, 0 duplicados** |
| **pasos releidos contra su parrafo** | **111 de 111**, mas las **5** cabeceras de puntero comprobadas contra el fichero |
| **`PASOS INVENTADOS` que voy a firmar** | **`cap_08`: 0 de 102, `0,00`.** El nodo de `cap_07`: **0 de 9** |
| **mis discutibles, marcados AQUI** | **7**, en `7` y `7.1` |
| **la cifra que el encargo me subio** | **`24` y `25` son las DOS ciertas**, con denominadores distintos, y lo mido por tres vias (`8`) |
| **caidas propias de esta fase** | **1**: suciedad mia en el arbol, **cuarta seguida**, remediada en el acto y con **tarea bloqueante escrita** (`9`). **Su alcance entero en `9.1`: siete ficheros mios commiteados en la `ACTA 17`, ninguno citado por ella** |
| **una fuga de la fase ciega que NO es mia** | el `gitStatus` del prompt me entrega asuntos de commit con cifras de la vuelta que vengo a auditar (`1.2`) |
| **las cinco guardas** | **las cinco en verde**, corridas por mi, con el arbol ya limpio (`10.1`) |
| **lo que queda para mi turno normal** | que la vuelta **declarase** su cierre corto (`7.1`); la sede del desvio de atribucion (`5.2`); la errata de metodo de `D.38.4` (`6.2`); los siete ficheros de `9.1`; y las mutaciones de `5.5` |

---

**NO COMMITEO. EL ARNES SELLA ESTE FICHERO Y LO COMMITEA EL** (`D.34.2`). **Y NO LO VUELVO
A TOCAR DESPUES DEL SELLO:** esa comprobacion cierra mi turno, con su `git hash-object`
contra `SELLOS_APERTURA.jsonl`.
