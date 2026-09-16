
---

# ACTA 29. VUELTA 30, lote 4 (`scott_radical_candor`), `cap_07` CERRADO EN INSERCION mas la cabeza `THINK TIME` de `cap_11`: la vuelta sale **limpia de `CLASE` y de `CIFRA PUBLICADA`**, sus **veintiuna cifras me salen al digito**, mis **dieciseis relecturas pineadas se sostienen las dieciseis** y sus **ocho discutibles se sostienen los ocho**. Y aun asi: **una cita que publica en celda de tabla apunta a la `ACTA 28` y la adjudicacion vive en la `ACTA 27`**, y **mi propia apertura sellada publica `4` puentes que son `0`, rompiendo el remedio que yo mismo escribi. `REPORTE` sube a `1 de 3` y MI RACHA a `1 de 3`. NO HAY PARADA**

| | |
|---|---|
| fecha del acta | **2026-09-16**, leida del instrumento (`date` da `Wed, Sep 16, 2026 4:39:35 PM`; `src.aduana._hoy()` da `2026-09-16`) |
| vueltas que cubre esta acta | **la vuelta 30, y solo ella.** Medido en la seccion 0, no supuesto. **No hay vuelta 29 y lo mido**, no lo supongo |
| rama | `extraccion-mundo-11` (`git rev-parse --abbrev-ref HEAD`) |
| hash auditado | **`b2edb7b`**, `HEAD` al abrir mi turno. El cierre tallado del extractor declara `37fe5c7` mas el commit que lo publica, y su apertura `b9f484a` |
| sello de mi apertura ciega | **`406ca90e54a2097d3f8371f01346b48a5d377d51`**, **intacto**: `git hash-object docs/loop/APERTURA_CIEGA.md` lo devuelve hoy y es el que `SELLOS_APERTURA.jsonl` anoto a las `16:16:54` |
| testigo de guardas al sellar (`D.45`) | **no desmiente ni una cifra mia**: `gate` VERDE, `guiones` VERDE, `censo_rutas` VERDE a las `16:16:52`. **Es la primera vez que la cura de `A.4` corre sobre mi, y paso** |
| arbol de trabajo | **ninguna sede de dato modificada por mi turno.** Mis mutaciones corrieron **sobre copia**, y la de `guiones` se retiro en el acto con el barrido verde detras |
| veredicto general | **REPORTE VERIFICADO AL DIGITO EN LAS VEINTIUNA CIFRAS QUE PUBLICA.** Cero `CLASE`, cero `CIFRA PUBLICADA`, **una `REPORTE`: la cita mal atribuida de la seccion 7.1** |
| paradas del extractor | **CERO declaradas**, y lo compruebo: es la segunda vuelta seguida sin ninguna |
| **parada mia** | **NO.** Mi racha va a `1 de 3` y ninguna de las seis condiciones se cumple. `PROMPT_SIGUIENTE.md` se escribe y `PARA_ALEXIS.md` **no** |

---

## 0. HUECO DE ACTA: MEDIDO, Y NO LO HAY, AUNQUE LOS NUMEROS NO SEAN CONSECUTIVOS

*Va antes que nada porque el protocolo lo pone antes que nada (`AUDITOR_FORJA.md` 1.0).*

    $ grep -n "^# ACTA " docs/loop/ACTA_AUDITOR.md | tail -1
      25208:# ACTA 28. VUELTA 28, lote 4 (scott_radical_candor) INSERTANDO cap_07 mas la cabeza de cap_11 ...
    $ grep -c "VUELTA 29" docs/loop/REPORTE.md
      0
    $ git log --all --oneline | grep -c "VUELTA 29"
      0
    $ git log --oneline 67c651c..b9f484a
      b9f484a ARNES: estado del arnes pendiente antes de abrir la vuelta 30
      585a609 D.44 el censo no decrece, el cerrojo de insercion, y D.45 una cifra vale en el instante del sello
      97584af ARNES: el tallado reventaba en la fase ciega y habria dejado al arnes sin poder sellar

**LECTURA: la ultima acta es la `ACTA 28` y cubre la vuelta 28; la vuelta que audito es la 30; y la
vuelta 29 NO EXISTE.** Entre el cierre de la `ACTA 28` y la apertura de la 30 hay tres commits y
ninguno es una vuelta del extractor: dos son del arnes y el tercero es la decision del fundador. **El
salto de numero lo pone la propia decision**, cuyo punto `4` dice literalmente *`PROMPT_SIGUIENTE` de
la vuelta 30*.

> **ASI QUE NO HAY HUECO, Y LO DIGO CON LA MEDIDA DELANTE EN VEZ DE CON EL NUMERO.** Un salto de
> numeracion se parece a un hueco y no lo es, **y la unica forma de distinguirlos es contar vueltas
> del extractor, no contar enteros.** Esta acta cubre **una sola vuelta** y lo dice.

**Numero de acta: la 29.** Las actas van por su orden y no por el numero de la vuelta que auditan;
**esta es la vigesimonovena y audita la vuelta 30**, y se dice aqui para que nadie lea el desfase como
un acta perdida.

### 0.1. LA HERENCIA, Y LA HUELLA CUADRA AL CARACTER

    $ git hash-object docs/loop/ACTA_AUDITOR.md      (hoy, antes de aniadir esta acta)
      148bbd78baae05817d71e200a32bb755a85ca152

**Es exactamente la huella que mi apertura sellada declara haber leido** (`APERTURA_CIEGA.md` `0.1`,
bloque `ACTA ANTERIOR LEIDA`). **`HEREDADO 1` y `HEREDADO 2`: los dos declarados `CUMPLIDO`, y los dos
lo estan contra lo que el arnes me entrego.**

> ### **PERO LO QUE EL ARNES ME ENTREGO NO ERAN LOS REMEDIOS DE LA `ACTA 28`, Y ESO TIENE CONSECUENCIA**
>
> Lo mido corriendo el mismo instrumento que corre el arnes:
>
>     $ python forja.py herencia
>       HEREDADO 1   [REMEDIO, linea 25541 del acta]  -> ACTA 28 seccion 3.2
>       HEREDADO 2   [REMEDIO, linea 25794 del acta]  -> ACTA 28 seccion 6.1
>
> **Las secciones `3.2` y `6.1` de la `ACTA 28` no ESCRIBEN remedios: CITAN los de la `ACTA 27` para
> decir que se cumplieron.** Los remedios que la `ACTA 28` escribe de nuevo estan en la tabla que
> precede a su seccion `9`, y son otros dos. **El de esa tabla que a mi me tocaba es el `1`**, y no me
> llego. **La seccion 8 dice lo que hice con el sin saberlo, y lo que eso me cuesta.**

---

## 1. LO QUE VERIFIQUE, CON MIS PROPIOS COMANDOS

**El estado de verdad es el repo.** Todo lo que sigue se corrio EN ESTA VUELTA y ninguna cifra se
copio del reporte. Salidas en `.v30c/`.

### 1.1. LOS CINCO INSTRUMENTOS Y LOS DOS CENSOS, CORRIDOS POR MI

| instrumento | mi salida de hoy | ruta |
|---|---|---|
| `python forja.py gate` | `GATE VERDE`, **256** nodos verificados, **13** guardas | `.v30c/gate.txt` |
| `python forja.py guiones` | `BARRIDO DE GUIONES VERDE` | `.v30c/guiones.txt` |
| `python forja.py resolutor` | **256** vivos, `0` deprecados, `0` alias | `.v30c/resolutor.txt` |
| `python tests/test_aceptacion.py` | **193** pruebas, **0** fallos, **0** errores | `.v30c/test.txt` |
| `python forja.py rancios` | `34` hallazgos sobre `361` veredictos, `RANCIO 26`, `SIN HUELLA 8`, `14` no consumadas | `.v30c/rancios.txt` |
| `python scripts/tallar_reporte.py` | `TALLADO VERDE`, **50** tablas comprobables celda a celda | `.v30c/tallado.txt` |
| `python scripts/censar_rutas.py` | `CENSO VERDE`, **455** rutas | `.v30c/censo.txt` |

> **LA UNICA DISCREPANCIA CONTRA EL REPORTE ES DE PRUEBAS, Y LA DECLARO EN VEZ DE RESOLVERLA
> COPIANDO** (`AUDITOR_FORJA.md` 1.1). El reporte publica **`192`** en apertura y en cierre; yo mido
> **`193`**. **No es una cifra falsa suya: es que el arbol se movio despues de su cierre.**
>
>     $ git show b9f484a:tests/test_aceptacion.py | grep -c "    def test_"   ->  192
>     $ git show faa0dd1:tests/test_aceptacion.py | grep -c "    def test_"   ->  192
>     $ git show 96274b3:tests/test_aceptacion.py | grep -c "    def test_"   ->  193
>     $ git diff --stat faa0dd1 96274b3 -- tests/test_aceptacion.py           ->  1 file changed, 21 insertions(+)
>
> **`LECTURA`, en linea aparte: la prueba numero `193` la aniade el arnes en `96274b3`, DESPUES de que
> la vuelta cerrase.** Las dos cifras son ciertas, cada una en su instante, **que es exactamente lo
> que `D.45` dice de una cifra.**

**Y LOS CUATRO FALLOS DE MI PROPIA APERTURA SELLADA SE EXPLICAN AQUI, porque los prometi para mi
turno** (`APERTURA_CIEGA.md` `7.5`, `POR ADJUDICAR 9`): mi fase ciega midio **`193` pruebas con `4`
fallos**, hoy mido **`193` con `0`**. **Los cuatro eran artefactos de la fase ciega**, tres por el
`REPORTE.md` retirado por `D.34.2` y el cuarto por la ruta que el arnes llena al terminar mi turno.
**Mi lectura ciega acerto, y no lo doy por bueno: lo mido.**

### 1.2. MI PROPIO CONTEO DEL DATASET, DE LA BITACORA Y DE LAS BANDEJAS

<!-- TALLADO: parcial salida=.v30c/cuentas.txt -->

    $ python .v30c/cuentas.py
      nodos: 256
      veredictos: 375
      nodos que mencionan scott_radical_candor: 53
      con no_consumada true: 14
      aristas por nodos_siguientes: 92   por nodos_previos: 92
    $ ls cuarentena/scott_radical_candor/*.json | wc -l              ->  89
    $ ls cuarentena/_insertados/scott_radical_candor/*.json | wc -l  ->  53
    $ ls cuarentena/marquet_turn_the_ship/*.json | wc -l             ->   3

| cifra del reporte | donde la publica | mi medida | |
|---|---|---:|---|
| nodos al cerrar | `W.8.b` | **256** | cuadra |
| veredictos al cerrar | `W.8.b` | **375** | cuadra |
| `no_consumada` al cerrar | `W.8.b` | **14** | cuadra |
| nodos con fuente `scott_radical_candor` | `W.8.b`, `W.2.i` | **53** | cuadra |
| bandeja del lote 4 | `W.8.b`, `W.2.i` | **89** | cuadra |
| archivados del lote 4 | `W.8.b`, `W.2.i` | **53** | cuadra |
| bandeja del lote 5 | `W.8.b` | **3** | cuadra |
| aristas por `nodos_siguientes` | `W.8.b` | **92** | cuadra, **y por los dos extremos**: `92` tambien por `nodos_previos` |
| lote 4 insertado sobre `142` | `W.8.b` | **37,3 por ciento** | cuadra con su `37` |

**LAS SEIS DE APERTURA, LEIDAS DE `git` Y NO DE SU PALABRA:**

    $ git show b9f484a:dataset/nodos.jsonl        | grep -c '"id"'                  ->  243
    $ git show b9f484a:bitacora/VEREDICTOS.jsonl  | grep -c '"veredicto"'           ->  289
    $ git show b9f484a:bitacora/VEREDICTOS.jsonl  | grep -c '"no_consumada": true'  ->   14
    $ git ls-tree -r --name-only b9f484a cuarentena/scott_radical_candor/ | grep -c '\.json$'              ->  102
    $ git ls-tree -r --name-only b9f484a cuarentena/_insertados/scott_radical_candor/ | grep -c '\.json$'  ->   40
    $ git ls-tree -r --name-only b9f484a cuarentena/marquet_turn_the_ship/ | grep -c '\.json$'             ->    3

**Las seis de `W.0.b` me salen al digito**, y las mido **contra el commit de apertura, no contra el
encargo**, que es lo que el extractor no podia hacer y yo si.

### 1.3. EL REPARTO DE LAS `86` LINEAS NUEVAS, RECONTADO Y NO ACEPTADO

<!-- TALLADO: parcial salida=.v30c/split.txt -->

    $ python .v30c/split.py
      lineas 'lectura declarada' : 4
      lineas de la aduana        : 82
      los 12 de cap_07 en orden del libro: [9, 4, 1, 7, 3, 3, 10, 10, 10, 8, 7, 5]
      SUMA de los 12 : 77
      bloquear_tiempo_pensar_calendario (aduana) : 5
      TOTAL aduana   : 82

**`82` mas `3` mas `1` igual a `86`, y las tres piezas las separo por el campo `levantada_por`, no por
su prosa.** De las cuatro lineas `lectura declarada`, **tres llevan arista** (las `D.37` de
`mantener_manos`, `reservar_calendario` y `cuidarse`) **y una no** (el par del calendario). **El cuadre
de `W.8.c` se sostiene entero.**

### 1.4. **LOS `77` PARES, QUE ES LA COMPROBACION QUE MAS VALE DE LA VUELTA**

**Los doce repartos que mi barrido ciego publico sin haber visto nada** (`APERTURA_CIEGA.md` `5`,
sellada a las `16:16:54`) **y los doce que la aduana escribio de verdad en la bitacora son los mismos
doce numeros, uno a uno y en el mismo orden del libro:**

    mi barrido ciego (grafo mas bandejas, 13 corridas)   9, 4, 1, 7, 3, 3, 10, 10, 10, 8, 7, 5
    la bitacora, contada por candidato                   9, 4, 1, 7, 3, 3, 10, 10, 10, 8, 7, 5
    suma                                                 77 contra 77, diferencia 0

> **`LECTURA`, en linea aparte: esto no es que dos cifras coincidan, es que dos poblaciones distintas
> dan el mismo reparto.** El extractor barrio contra un grafo que crecia nodo a nodo; **yo barri contra
> el grafo ya terminado, con los trece dentro.** Que salga el mismo reparto dice **que el orden de
> insercion no le escondio ni un par**, y eso es lo que yo podia comprobar y el no. **Es tambien la
> prueba de campo de `D.38.5`**: si la poblacion fuese solo el grafo, estas dos cifras no cuadrarian.

### 1.5. **LA CAIDA DE DATO: NO LA HAY, Y LO MIDO POR TRES CAMINOS QUE NO SE COPIAN**

**Es la especie que tumbo la vuelta 28, asi que no me basta con que el gate este verde.**

    $ (censo del dataset y de la bitacora en cada commit de la vuelta 30)
      b9f484a  nodos=243  veredictos=289    (apertura)
      8e626b6  nodos=243  veredictos=289
      23ceccd  nodos=246  veredictos=303
      7de53a9  nodos=249  veredictos=316
      e1f3f8e  nodos=252  veredictos=346
      56a3d11  nodos=255  veredictos=369
      5834c50  nodos=256  veredictos=375
      445a13e  nodos=256  veredictos=375
      37fe5c7  nodos=256  veredictos=375
      faa0dd1  nodos=256  veredictos=375    (cierre)

<!-- TALLADO: parcial salida=.v30c/diff_bitacora.txt -->

    $ python .v30c/diff_bit.py
      lineas al abrir la vuelta 30 (b9f484a): 289
      lineas hoy                           : 375
      lineas nuevas                        : 86
      de las 289 viejas, CAMBIADAS: 8 -> [252, 256, 258, 260, 261, 262, 263, 264]
      de las 289 viejas, INTACTAS : 281
      prefijo intacto: ninguna linea vieja se borro ni se reordeno: True
      linea 252: clase/huellas/senales intactas=True | la razon vieja sigue entera al principio=True | +498 caracteres
      (y lo mismo las otras siete, las ocho con +498 caracteres exactos)

    $ (censos, lineas que desaparecen)
      censos/atribuciones.md   :  82 ->  85 lineas,  lineas que DESAPARECEN: 0
      censos/denominaciones.md : 561 -> 593 lineas,  lineas que DESAPARECEN: 0

**LECTURA: el censo del dataset SOLO SUBE, `243` a `256`; ninguna de las `289` lineas viejas se borro
ni se reordeno; las `8` que cambian cambian SOLO por el final de su `razon`, con la clase, el
candidato, el vecino, las dos huellas y las tres seniales intactas; y los dos censos crecen sin perder
una linea.** **Ninguna caida de dato, y no lo digo por el verde del gate: lo digo por la diferencia.**

**Y DIGO EL LIMITE DE MI PROPIA MEDIDA, porque el reporte afirma algo mas fino de lo que yo puedo
comprobar:** `W.2.e` dice que el censo subio **de uno en uno, trece veces**. Yo mido la monotonia
**commit a commit**, que va en tandas de tres. **La afirmacion es compatible con lo que mido y no la
puedo verificar mas fina**, porque las corridas intermedias no dejaron commit. **No la firmo como mia
y no la cuento como caida: la declaro como no verificable con lo que hay en el arbol.**

### 1.6. LA GUARDA QUE NO MUERDE ES CIFRA (cosecha 7.C): MUTO TRES Y MUERDEN LAS TRES

<!-- TALLADO: parcial salida=.v30c/mutaciones.txt -->

| guarda | como la mute | que hizo |
|---|---|---|
| `arista_rota` | copia del dataset con `nodos_siguientes` apuntando a un id inexistente | **`GATE EN ROJO: 1 fallo`**, nombrando el nodo y el id |
| `guiones` | un fichero con un guion largo puesto en `docs/loop/` | **`BARRIDO EN ROJO: 2 hallazgos`**, con fichero, linea y columna |
| `censo_no_decrece` (`D.44`) | `gate.censo_no_decrece(nodos[1:])`, un nodo menos | **`1 fallo`**: *estaba en el dataset del commit HEAD y NO esta en el arbol* |

**LAS TRES MUERDEN Y EL ARBOL QUEDA COMO ESTABA.** Las dos primeras corrieron sobre copia; la de
`guiones` toco el arbol **un minuto**, la retire, y **el barrido volvio a verde en el mismo comando**.
**Lo digo porque la primera salida de mi propia fase ciega dejo el barrido en rojo con ficheros suyos,
y esa es la caida que no quiero repetir callado.**

---

## 2. LA RELECTURA CIEGA, EMPEZANDO POR LOS DISCUTIBLES MARCADOS (`AUDITOR_FORJA.md` 1.2, 5.1)

**Metodo, y es el `REMEDIO 2` que heredo de la `ACTA 27` por la `ACTA 28` `3.2`:** imprimi **primero**
los pasos de los dos nodos de cada par, escribi mi clase en `.v30c/mis_clases_pineada.txt` a las
**`16:32:33`**, y **solo despues** destape las razones, **una por comando** (`.v30c/una.py`, un numero
de linea por corrida). **Ni un comando saco dos razones.**

### 2.1. **`DISCUTIBLE 1`: la arista `D.29` `desplegar_plan_orden_operaciones_franqueza_radical` MADRE de `bloquear_tiempo_pensar_calendario`. SOSTENIDA**

**El extractor la marca el primero y dice que es la mas fragil de la vuelta.** Lo es, y aguanta.

| lado | lo que trae |
|---|---|
| **madre**, `cap_12`, paso `30` | *Pon algo de tiempo para pensar en tu calendario.* **Una sola frase, item de un inventario ordenado de 42 pasos** |
| **hija**, `cap_11` `L165-173`, `6` pasos | reconocer a que te enfrentas, la consecuencia de no hacer nada, agendarlo, mantenerlo sagrado, decir que nadie agende encima, enfadarse si lo intentan, animar al equipo |

**MI ADJUDICACION, con la vara y sin bascula:** lo que el hijo aniade a la madre es **el procedimiento
entero**; lo que la madre tiene es **el nombre**. `AUDITOR_FORJA.md` 6.1 y `P.5.1`: **NOMBRAR NO ES
PROCEDIMENTAR.** Eso es `D.29` literal.

> ### **Y LA OBJECION QUE EL PROPIO EXTRACTOR SE PONE, RESUELTA CON EL EJEMPLAR DE `D.29` DELANTE**
>
> La objecion es *una remision hacia atras no es una cabeza*, y **es cierta y es cita de esta casa**.
> Lo que la deja fuera aqui es el propio ejemplar con el que `D.29` nacio:
>
>     formular_codigo_comercializacion_empresarial   (parrafo 31, MADRE)
>         baja a
>     verificar_afirmaciones_ambientales_publicidad  (parrafo 30, HIJO)
>
> **La madre del ejemplar fundador de `D.29` es el parrafo 31 y el hijo el 30: la madre viene DESPUES
> en la fuente.** Asi que **el orden del libro no decide la maternidad**, y nunca la decidio.
>
> **Lo que la decide es la figura, y las dos figuras son distintas:** la que la `ACTA 27` `2.2` tumbo
> era *una remision de la autora a una tecnica que ella ya dio*, **condicional y dentro de una
> anecdota, veintiocho lineas despues del parrafo propio del hijo**. El paso `30` del plan **no es una
> remision: es un imperativo dirigido al lector, item de un inventario cuya funcion declarada es
> nombrar las etapas**. Y el manual seccion 3 punto 4 pone la forma: **una serie numerada es un nodo
> por paso MAS UNA CABEZA.** La cabeza existe, el hijo es su paso.

**LA RAZON ESCRITA, destapada despues** (linea `371`): dice exactamente eso, con la frase del paso 30
citada y con el `resumen_teorico` de la madre delante. **Coincide con mi lectura sin habernos visto.**

### 2.2. **`DISCUTIBLE 2` y `DISCUTIBLE 3`: el triangulo de la retorica, `SANO` los dos. SOSTENIDOS**

*Los adjudico juntos porque el propio extractor dice que si cae uno caen los tres, y tiene razon.*

`L321` anuncia los tres elementos de Aristoteles y luego el libro pone tres rotulos: `Emotion`
(`L323`), `Credibility` (`L349`), `Logic` (`L359`). Son tres nodos hermanos.

| lo que mire | lo que encontre |
|---|---|
| **si son duplicado** | **no.** `persuadir` deja fuera `8` pasos de emocion, `establecer` `8` de credibilidad, `compartir` `5` de logica. **Lo que queda fuera es procedimiento en los tres lados**, que es la vara sin bascula |
| **si hay madre** | **no la hay como nodo.** `L321` es cabeza de lista y **no trae procedimiento propio** (*the rest of this section will cover, briefly...*), y `EXTRACTOR.md` 9 dice que eso no es nodo |
| **si `persuadir` es la madre por haberse tragado el preambulo** | **no.** Mire sus once pasos uno a uno: **ninguno nombra la credibilidad ni la logica como partes de una cuenta**, y `D.37` en su lectura estrecha del 11 sep exige **que diga cuantas y las nombre**. Sin paso que citar no hay `--paso n`, y **una arista sin su linea es una afirmacion sin cita** |
| **el reparto de `L313`** | los dos citan esa linea, **y el reparto es correcto**: `persuadir` toma la clausula de la emocion y **suelta la de la credibilidad**, que `establecer` recoge en su paso `1`. **No se la quedan los dos** |

**ADJUDICO `SANO` SIN ARISTA EN LOS TRES PARES.** Y lo que el extractor levanta como consecuencia es
cierto y no es culpa suya: **quedan hermanos por un hueco.** Va a la seccion 5 como propuesta `2`.

### 2.3. **`DISCUTIBLE 4`: `calibrar_ascensos_evitar_politica` contra `bloquear_tiempo_pensar_calendario`, `paso_contra_nodo` `0,911`. `SANO` SOSTENIDO**

**Es la senial mas alta de toda la campania y es un falso positivo de manual.** Lo firmo despues de
leer los `19` pasos de uno y los `6` del otro.

    paso 14 de calibrar : Y anima a todo tu equipo a hacer lo mismo.
    paso  6 de bloquear : Y anima a todos los de tu equipo a hacer lo mismo.

**La frase es casi la misma y el `LO MISMO` es cosa distinta:** en uno es **dormir, hacer ejercicio y
desayunar bien el dia de la reunion de calibracion de ascensos**; en el otro es **bloquear tiempo de
pensar en el calendario**. `similitud_texto` mide `0,223`, muy por debajo de umbral, **y los dos
trabajos no se tocan en ningun otro paso.**

> **`LECTURA`: este par es la mejor noticia tecnica de la vuelta y conviene decirlo.** El vecino
> **esta en la bandeja, no en el grafo**, y la aduana lo levanto igual. **Eso es `D.38.5` funcionando
> en produccion**, que es la regla que la `ACTA 26` desenterro y que llevaba cuatro dias escrita sin
> llegar a `src/aduana.py`. **Hoy la veo morder sobre un candidato real.**

### 2.4. **`DISCUTIBLE 7`: `explicar_idea_facil_comprender_oyente` contra `fijar_fecha_cierre_debate_equipo`, `0,610`. `SANO` SOSTENIDO**

`CLARIFY` contra `DEBATE`. Uno carga con que la idea se entienda; el otro fija cuando acaba el debate
y quien decide. **El cruce es paso `6` contra paso `2` y lo unico que comparten es la forma de frase**
(*cuenta con lo que el texto dice*), que no es trabajo compartido. **Ningun paso de uno hace lo que
hace ninguno del otro**, y lo compruebo leyendo los `13` y los `11`.

**Y contesto la pregunta que el extractor deja abierta:** *si me equivoco, hay una arista `CLARIFY` a
`DEBATE` que no declare.* **No la hay, y no es por parecido: es por nivel.** La secuencia de la rueda
no cablea pieza con pieza; **la cablearia la cabeza de la rueda**, y sobre eso mido aparte en `6.3`.

### 2.5. LOS TRES DISCUTIBLES QUE NO SON DE CLASE, ADJUDICADOS

| # | el discutible | mi adjudicacion |
|---:|---|---|
| **5** | haber insertado un candidato `13` que no es de `cap_07` | **BIEN HECHO, y el encargo se lo pedia.** Su `TAREA 2` dice *la vuelta que inserte al primero lo lee contra el segundo*, y ese primero es `bloquear_tiempo_pensar_calendario`. **Y lo metio DESPUES de cerrar `cap_07` entero**, que es lo unico que el orden del libro (`D.36`) protege dentro de un capitulo. **No se adelanto nada** |
| **6** | cerrar las `8` lineas `SIN HUELLA` con `anotar` y no volviendolas a juzgar | **BIEN HECHO, y es la salida que `D.15` nombra.** `D.15` da dos y **no ordena cual**. Lo compruebo por diferencia en `1.5`: `anotar` **no toco ni una clase, ni un candidato, ni un vecino, ni una huella, ni una senial**. **Y la fila queda cerrada**: lo que sigue saliendo `8` es el instrumento, que no sabe leer el campo `anotaciones`, **y eso es la propuesta `1` y no una fila abierta** |
| **8** | dos vias para las tres aristas de la misma serie `D.37` | **BIEN HECHO, y la alternativa habria sido peor.** La aduana cablea cuando levanta a la madre; donde no llega, `forja.py arista`. **Correr las dos sobre el mismo par seria el duplicado que `D.29` evita.** El resultado en el dato es identico y lo compruebo por los dos extremos: `92` aristas por `nodos_siguientes` y `92` por `nodos_previos` |

**LOS OCHO DISCUTIBLES SE SOSTIENEN LOS OCHO. CERO CAIDAS DENTRO DEL MARCADO** (`5.1`).

---

## 3. LA MUESTRA PINEADA DE LOS SANOS (`AUDITOR_FORJA.md` 7)

### 3.1. LA POBLACION Y EL TAMANIO, CON LA CUENTA DELANTE

<!-- TALLADO: parcial salida=.v30c/pineada.txt -->

    $ python .v30c/pineada.py
      SANO de la tanda: 80
      el mayor entre 3 y el 20 por ciento: 16    techo 20
      SEMILLA: 300916    random.Random(SEM).sample(sanos,16)

**`16` relecturas: el `20` por ciento de `80`, por debajo del techo de `20`.** Elegidas **al azar con
semilla escrita**, no a ojo.

### 3.2. **LAS DIECISEIS, Y LAS DIECISEIS SE SOSTIENEN**

**Escribi mis clases a las `16:32:33` en `.v30c/mis_clases_pineada.txt`. Destape las razones despues,
una por comando.**

| linea | el par | mi clase ciega | la razon escrita |
|---:|---|---|---|
| 291 | `parar_debate` contra `abrir_debate_humor` | `SANO`, actos opuestos bajo `DEBATE` | coincide |
| 298 | `parar_debate` contra `centrar_debate_ideas` | `SANO`, disparadores distintos | coincide |
| 299 | `fijar_fecha` contra `explicar_idea_facil` | `SANO`, falso positivo de senial 3 | coincide |
| 300 | `fijar_fecha` contra `centrar_debate_ideas` | `SANO` sin arista, **cosa juzgada** | coincide, **y me cita** |
| 304 | `pedir_hechos` contra `parar_debate` | `SANO`, `DECIDE` contra `DEBATE` | coincide |
| 307 | `pedir_hechos` contra `compartir_logica` | `SANO` | coincide |
| 308 | `pedir_hechos` contra `crear_obligacion_disentir` | `SANO`, mismo fin y actos distintos | coincide |
| 310 | `pedir_hechos` contra `aprender_resultados` | `SANO` | coincide, **y aniade que el vecino es cabeza de serie y el candidato no es parte suya** |
| 317 | `compartir_logica` contra `centrar_debate_ideas` | `SANO` | coincide |
| 318 | `compartir_logica` contra `minimizar_impuesto` | `SANO` | coincide, **con las tres partes nombradas una a una** |
| 323 | `compartir_logica` contra `pedir_hechos` | `SANO`, el `307` al reves | coincide |
| 335 | `minimizar_impuesto` contra `parar_debate` | `SANO` | coincide |
| 341 | `proteger_tiempo` contra `reservar_calendario` | `SANO`, hermanos de la serie de `L373` | coincide |
| 349 | `mantener_manos` contra `abrir_debate_humor` | `SANO` | coincide |
| 364 | `cuidarse` contra `cambiar_posicion_hechos` | `SANO`, hermanos de la serie de `L401` | coincide |
| 372 | `bloquear_tiempo_pensar` contra `proteger_tiempo` | `SANO`, tu tiempo contra el de tu equipo | coincide |

**`16` de `16` SE SOSTIENEN. CERO caidas de `CLASE` en la muestra pineada.**

### 3.3. LA TASA CON SU BANDA, PORQUE UNA TASA SIN BANDA ES MEDIA CIFRA

<!-- TALLADO: parcial salida=.v30c/rachas.txt -->

    $ python .v30c/rachas.py
      muestra pineada: 16 relecturas, 0 caidas de CLASE
      tasa: 0,00 por ciento
      banda 95 por ciento, cota superior con k=0: 1-0.05**(1/16) = 17.07 por ciento

> **`LECTURA`, en linea aparte y dicha contra mi propio resultado: `0` de `16` NO significa que la
> tasa de dejar pasar sea cero.** Con `16` relecturas y cero caidas, **lo unico que puedo afirmar al
> `95` por ciento es que la tasa verdadera esta entre `0,00` y `17,07` por ciento.** La banda es ancha
> porque la muestra es pequenia, **y la muestra es pequenia porque la manda el protocolo**. **Una tanda
> con `80` SANO y `16` releidos no prueba que la aduana no deje pasar nada: prueba que si deja pasar
> algo, no es a manos llenas.**

### 3.4. `D.8`: UN SANO SIN RAZON ESCRITA ES UNA CAIDA, Y NO HAY NINGUNO

    $ python .v30c/nuevas.py
      por veredicto: SANO 80, CONTINUA 6
      candidatos distintos: 13
      SIN razon (D.8): 0
      razon mas corta: 125 caracteres

**Las `86` traen razon y la mas corta tiene `125` caracteres.** `D.8` se cumple en las `86` **sin
releer ninguna**, que es lo que la propia regla dice de si misma.

---

## 4. `PASOS INVENTADOS POR CAPITULO` (`AUDITOR_FORJA.md` 8), FIRMADA POR MI

### 4.1. EL DENOMINADOR, CONTADO POR MI (`8.3` punto 1)

    $ python .v30c/muestra_pasos.py
      pasos de los 13 de la tanda : 96
      pasos de los 12 de cap_07   : 90

**Cuadra con los `90` de `W.2.b` y con los `90` de mi propia apertura sellada.**

### 4.2. **EL NUMERADOR: MI LECTURA CIEGA DECIA `4` PUENTES Y HOY DIGO `0`. LA RETIRO POR CORRECCION DECLARADA**

**Mi apertura sellada `4.1` leyo como PUENTE los pasos `4` a `7` de
`cuidarse_agotamiento_centro_rueda`**, con el argumento de que el manual 3.5 dice que *el caso no
viaja al paso*. **Fui a leer el manual en el turno normal y el manual dice lo contrario de lo que le
atribui:**

    docs/MANUAL_SISTEMA_DE_CONOCIMIENTO.md, seccion 3, punto 5
      SI ES UN CASO O ESTUDIO: el caso no es la casa. La doctrina vive en su nodo y el caso entra
      como ejemplo nombrado dentro de ella (senial barata: el entregable del caso lleva un dato
      del caso).

**La regla no prohibe que el caso entre en el paso: MANDA que entre como ejemplo nombrado dentro de la
doctrina.** Y trae su propia senial barata, que aplico:

    entregable de cuidarse_agotamiento_centro_rueda:
      Tu mismo cuidado y centrado, con tiempo de pensar reservado en el calendario, y la rueda
      girando otra vez.

**No lleva ni un dato del caso: ni `Dick Costolo`, ni `Twitter`, ni las dos horas.** Por la senial del
propio manual, **este nodo es el nodo de la doctrina con el caso nombrado dentro, que es exactamente
lo que la regla pide.**

**Y `D.30` decide por su letra, no por la mia:** su prueba es **el libro pone el medio, la etapa o el
objeto**. `L415` pone declinar invitaciones y el humor a su costa; `L417` pone no fingir que no pasa
nada y bloquear tiempo de pensar **todos los dias**. **Los cuatro medios estan en el libro.** Lo que el
candidato aniade es el imperativo, **y ese giro ya lo adjudico la `ACTA 28` `4.3` como el estilo de
transcripcion de esta casa y no una invencion**, sobre este mismo nodo y sobre su paso `6`.

> **ADJUDICO: LOS CUATRO SON `TRANSCRIPCION`. MI LECTURA CIEGA SE RETIRA POR CORRECCION DECLARADA, sin
> borrar lo que escribi.** `APERTURA_CIEGA.md` `4` y `4.1` quedan en su sitio y esta seccion es la que
> manda. **Lo que esto me cuesta va a la seccion 8, y es lo que me cuesta.**

### 4.3. LA MUESTRA DE HOY, CON SEMILLA ESCRITA, SOBRE LO QUE MI FASE CIEGA NO LEYO

    $ python .v30c/muestra_pasos.py
      poblacion NO leida en mi fase ciega (cap_07): 48
      SEMILLA: 160926    random.Random(160926).sample(pob,16)

**Los `16`, leidos contra su linea del libro con `awk` sobre `fuentes/scott_radical_candor/cap_07.md`.
Los cuatro que mas cerca estuvieron de ser puente, con su linea pegada:**

| paso | la linea del libro | veredicto |
|---|---|---|
| `repartir_decision` paso `7`: *ve a su reunion y mira a la sala, no al que habla* | `L275`: *Looking around the room, I registered arms crossed, faces stony, and a silence so loud that it penetrated even Mark's well-prepared speech* | **TRANSCRIPCION**, y es el mismo giro descriptivo a imperativo de `4.2` |
| `fijar_fecha` paso `9`: *lo cierren durante una comida o un paseo* | `L257`: *I could have suggested the people whose differences he was having a hard time reconciling try to wrap it up over a meal or a walk* | **TRANSCRIPCION**, y el condicional del libro pasa a imperativo |
| `establecer_credibilidad` paso `9` | `L357`: *Don't forget to establish your credibility or to help the deciders on your team to establish theirs* | **TRANSCRIPCION** literal |
| `persuadir` paso `6`: *como estaban las emociones en el equipo de ingenieria* | `L333` y `L335`: *What were the emotions on the engineering team like?* / *They were just exhausted* | **TRANSCRIPCION**, dialogo del libro |

**`16` de `16` TRANSCRIPCION. `0` PUENTE.**

### 4.4. **MI FILA, FIRMADA, POR CAPITULO Y CON EL TOTAL** (`8.2`)

| capitulo | nodos | **pasos escritos** | **PUENTE** | **PASOS INVENTADOS** |
|---|---:|---:|---:|---:|
| **`cap_07`** (lote 4, `scott_radical_candor`) | 12 | **90** | **0** | **`0,00` por ciento** |
| **`cap_11`** (lote 4, `scott_radical_candor`) | 1 | **6** | **0** | **`0,00` por ciento** |
| **total del tramo** | 13 | **96** | **0** | **`0,00` por ciento** |

**LA FIRMO, y digo con que cobertura:** **`58` de los `90` de `cap_07`** leidos por mi (`42` enteros en
mi fase ciega mas `16` al azar con semilla escrita hoy), el **`64,4` por ciento**, **y los `6` de
`cap_11` enteros**. **`64` de `96`.** **No firmo lo que no lei:** los `32` restantes los cubro por
muestreo.

> **`LECTURA`, en linea aparte: el `0,00` de esta fila vale MAS que el de la `ACTA 28`, y no porque el
> capitulo sea mejor.** Vale mas **porque el unico candidato a puente que esta casa tenia sobre la mesa
> era el mio, lo trabaje en las dos direcciones, y cayo por el manual y no por comodidad.** Un `0,00`
> que nadie ataco es una cifra sin probar; **este lo atacaron y aguanto.**

### 4.5. LO QUE LA CIFRA DECIDE SOBRE EL VOLUMEN (`8.1`)

| lo que mido | lo que manda |
|---|---|
| el **peor capitulo** es `0,00`, muy por debajo del tope de `10` | **el freno de fidelidad NO se activa** |
| se **mantiene** contra el tramo anterior (`ACTA 28` firmo `0,00` sobre `135`) | **el tramo podria subir un escalon** |
| **pero el lote 4 esta CERRADO EN EXTRACCION desde la `ACTA 24`** | **no hay lote siguiente que dimensionar: lo que corre es insercion** |
| el freno que **SI** aprieta | **el coste de la aduana**, medido por el extractor en `26` corridas de entre `63` y `136` segundos, y por mi hoy: **una sola corrida en seco sobre UN candidato paso de `120` segundos** |

**Y DIGO LO QUE ESO SIGNIFICA PARA EL ENCARGO: el tramo no lo decide esta metrica.** Lo decide el
reloj, **y por eso el encargo no sube el numero de candidatos.**

---

## 5. **LAS TRES PROPUESTAS DEL EXTRACTOR, ADJUDICADAS UNA A UNA** (`EXTRACTOR.md` 14)

| # | propuesta | mi adjudicacion |
|---:|---|---|
| **1** | que `forja.py rancios` distinga un hallazgo DECLARADO de uno que nadie ha mirado | **ACEPTADA EN SU DIAGNOSTICO, RECHAZADA COMO ENCARGO DE HOY.** El diagnostico es cierto y lo reproduzco: `34` de `34` llevan `VIGENCIA DECLARADA` en `anotaciones` y el instrumento sigue imprimiendo `RANCIO 26, SIN HUELLA 8`. **Pero es un lector nuevo y la moratoria de `5.6` es literal: no encargo maquinaria salvo que una caida de DATO lo exija con su cita, y aqui no hay caida de dato.** Queda **registrado en esta acta**, que es sede que sobrevive, **y la fila de la cola se declara CERRADA igual**, porque lo que sigue sin distinguir es el instrumento y no el trabajo |
| **2** | que se adjudique que hacer con una entradilla que es cabeza de lista sin procedimiento propio | **ADJUDICADA AQUI, y no hace falta doctrina nueva.** `EXTRACTOR.md` 9 ya dice que **una cabeza de lista sin procedimiento propio no es un nodo**, y la consecuencia (piezas hermanas sin madre) **es la consecuencia de esa regla, no un defecto de esta vuelta.** **Es la lectura buena y se queda:** inventar un nodo para una entradilla que solo anuncia seria fabricar un nodo sin acto, que es lo que `D.27` prohibe por el otro lado. **Lo que si toca es que la cola lo diga por su nombre**, y lo dice: `3` de `7` rotulos de `cap_07` sin nodo, medidos hoy por mi en `.v30c/cierre_cap07.txt` |
| **3** | que el arnes entregue la cola de vecinos sellada, que `D.43` extendida manda desde el 16 sep | **ACEPTADA, y es del arnes y no del extractor.** `D.43` extendida esta escrita y **esta corrida no la trajo**: no existe fichero de cola en `docs/loop/`, y lo compruebo yo. **Va al encargo dentro de la `TAREA 2`, que es la tarea del arnes**, con su medida al lado: hoy costo `26` corridas de la aduana dentro del turno |

---

## 6. **LOS NUEVE `POR ADJUDICAR` DE MI APERTURA SELLADA, ADJUDICADOS UNO A UNO**

### 6.1. **`POR ADJUDICAR 1`: el par del calendario que ninguna senial cruza. ADJUDICO `CONTINUA`, Y EL AGUJERO ES REAL**

**El par:** `reservar_calendario_tiempo_ejecutar` (en el grafo, `cap_07` `L385-387`, rotulo *Block time
to execute*) contra `pelear_proliferacion_reuniones_bloquear_ejecucion` (**en la bandeja**, `cap_11`
`L225-233`, rotulo *Fight meeting proliferation*).

**MI ADJUDICACION, leyendo los `4` pasos de uno y los `8` del otro:** **no son duplicado, son
`CONTINUA`**, con la madre en `cap_07` y la hija en `cap_11`. Lo que la hija aniade **son los tres
remedios que el libro prueba y descarta** (quitar las sillas, el dia sin reuniones, el objetivo de
terminar antes la cuarta parte), **la solucion de combatir fuego con fuego, y el encargo al equipo**.
Lo que la madre aniade es **la causa de por que ese tiempo no aparece nunca en el calendario**. **Es
procedimiento en los dos lados y la vara no tiene bascula.**

**Y LA CONSECUENCIA, REPRODUCIDA CON MI INSTRUMENTO EN ESTA MISMA FASE:**

<!-- TALLADO: parcial salida=.v30c/informe_pelear.txt -->

    $ python forja.py informe --carpeta .v30c/uno_pelear
      poblacion del barrido       : 348   (256 del grafo mas 92 que esperan en bandejas)
      EL SALDO
        ENTRARIAN sin leer nada          : 1
        BLOQUEARIAN esperando veredicto  : 0
      [ENTRARIA] pelear_proliferacion_reuniones_bloquear_ejecucion

> **`LECTURA`: el dia que ese candidato llegue a la puerta, la aduana lo dejara pasar SIN MANDAR LEER
> NADA**, con el nodo que manda su mismo acto ya dentro. **Las tres seniales lo dan por desconocido en
> las dos direcciones, y la poblacion ya incluye las bandejas**, asi que no es el agujero que `D.38.4`
> cerro: **es que la poblacion correcta no basta cuando las tres seniales no se tocan.**
>
> **ADJUDICAR NO ES MEDIR, asi que no cableo yo.** Lo que hago es lo que `1.4` me obliga: **lo
> encargo**, con la clase ya decidida por mi, **para que la vuelta que inserte a `pelear` solo tenga
> que ejecutar la declaracion y no volver a decidirla.** Va al encargo como `TAREA 4`, con fecha de
> caducidad: **el dia que ese candidato pase la puerta, este par ya no se puede leer nunca.**

### 6.2. **`POR ADJUDICAR 2`: la arista `cuidarse` paso `7` contra `bloquear_tiempo_pensar_calendario`. EXISTE Y NADIE LA JUZGO**

**Primero la busqueda, que la corri y por eso la puedo citar** (`1.1`: *una busqueda negativa no se
puede citar*):

    $ python .v30c/razon.py   (el par, en los dos sentidos)
      cuidarse_agotamiento_centro_rueda  <->  bloquear_tiempo_pensar_calendario
        NO HAY LINEA EN LA BITACORA

    $ (los cinco vecinos que la aduana levanto para bloquear_tiempo_pensar_calendario)
      calibrar_ascensos_evitar_politica              paso_contra_nodo 0.911
      desplegar_plan_orden_operaciones_franqueza...  paso_contra_nodo 0.615
      proteger_tiempo_equipo_jefe                    paso_contra_nodo 0.604
      reservar_calendario_tiempo_ejecutar            familia_id 0.333
      exigir_critica_jefe_reticente                  similitud_texto 0.364

**`cuidarse` no esta entre ellos, y `cuidarse` ya vivia en el grafo: entro como candidato `12` y
`bloquear` como `13`.** Asi que **ninguna senial los cruzo y ningun veredicto era debido.**

**MI ADJUDICACION, con los pasos delante:**

    cuidarse paso 7    : Bloquea en tu calendario tiempo de pensar todos los dias.
    bloquear entregable: El tiempo para pensar bloqueado en tu calendario y mantenido, con tu equipo
                         avisado de que ahi no se agenda y animado a bloquear el suyo.

**Es `D.29` literal: la madre NOMBRA en un paso y la hija PROCEDIMENTA en seis.** Y es **la misma
figura que esta misma vuelta uso para cablear `desplegar_plan` paso `30` contra este mismo hijo**.

> **Y ME PONGO LA OBJECION MAS FUERTE CONTRA MI, QUE ES LA MIA DE LA `ACTA 27` `2.2`:** *una remision
> hacia atras no es una cabeza*. **No aplica, y la diferencia esta en el texto y no en mi
> preferencia:** lo que la `ACTA 27` tumbo era **una remision condicional de la autora, dentro de una
> anecdota, a una tecnica ya dada** (*I could have suggested...*). **El paso `7` de `cuidarse` no
> remite a nada: es un imperativo dirigido al lector**, escrito como tal en el nodo, y el nodo que lo
> despliega entero existe y vive en el grafo.
>
> **QUE CUESTA ESTO AL EXTRACTOR: lo digo, y digo tambien que no acumula, con la regla delante.** No es
> `CLASE`, porque `CLASE` es **un veredicto mal puesto** y aqui **no hay veredicto ninguno**: la aduana
> no levanto el par y no habia nada que juzgar. No es `CIFRA PUBLICADA` ni `REPORTE`, porque el reporte
> **no afirma en ningun sitio que no falten aristas**. **No encaja en ninguna de las cuatro especies de
> `5.2`, y no invento una quinta: eso seria doctrina nueva y seria parada.** **Se registra con su
> nombre, se encarga, y no acumula.** Es la misma tension que la fila `DATO MOVIDO` describe: *un danio
> real sin sitio donde anotarlo acaba anotandose donde no va.*
>
> **Y LO QUE SI VALE DECIR ES QUE LA CAZO LA FASE CIEGA.** Mi apertura sellada la levanto sin ver el
> reporte, **y hoy se sostiene.** Va al encargo como `TAREA 3`, cableable hoy mismo porque **los dos
> extremos viven en el grafo**.

### 6.3. **`POR ADJUDICAR 3`: mis cuatro puentes. RETIRADOS, y la seccion 4 dice por que**

**Adjudicado en `4.2`.** `0` puentes, `0,00` por ciento, firmado con `58` de `90` leidos.

**Y aprovecho para cerrar la pregunta que me deje abierta en `2.4`, porque la corri:**

    $ (aristas de la cabeza de la rueda, leidas de dataset/nodos.jsonl)
      recorrer_rueda_hacer_cosas_equipo   previos=['recorrer_rueda_conscientemente_cultura_equipo']
                                          siguientes=[]

**La cabeza de la rueda nombra las siete etapas en sus pasos `2` a `8` y no tiene ni una arista a las
piezas.** **ADJUDICO QUE ESTA BIEN ASI, y lo adjudico con `D.37` en su lectura estrecha del 11 sep:**
sus pasos **no dicen cuantas etapas son**, asi que `D.37` no la autoriza; **y lo que nombran son
ETAPAS, no nodos**: `DECIDE` tiene dos piezas en el grafo, `DEBATE` cinco. **Una cabeza que nombra un
nivel que no es nodo no tiene hija que cablear**, que es la misma figura de `2.2` un piso mas arriba.
**No falta ninguna arista ahi, y lo digo habiendolo mirado.**

### 6.4. **`POR ADJUDICAR 4`: mis discutibles ciegos `1` y `2`. LOS DOS SE RESUELVEN A FAVOR DEL EXTRACTOR**

| mi discutible ciego | mi adjudicacion de hoy |
|---|---|
| **`fijar_fecha_cierre_debate_equipo` se come DOS rotulos del libro** (`L245` *Be clear when the debate will end* y `L251` *Don't grab a decision...*) | **BIEN CORTADO.** Lei los dos tramos: `L253` a `L257` **no trae un acto propio**, trae la anecdota del plano de mesas **y su moraleja es el mismo acto del primer rotulo** (*the right thing to do would have been to set a "decide by" date*). **Dos rotulos con un solo acto son un nodo, no dos**, y partirlo habria dado una pieza sin procedimiento |
| **`persuadir_emocion_oyente_no_propia` se traga el preambulo de los TRES elementos** (`L309` a `L321`) | **BIEN, Y ERA LA UNICA SALIDA LIMPIA.** Adjudicado en `2.2`: la cabeza de `L321` **no es nodo** por `EXTRACTOR.md` 9, y el preambulo de `L313` **tiene procedimiento** que alguien tenia que recoger. **Lo recogio la primera pieza de la seccion y solto la clausula que le tocaba a la segunda.** La alternativa era perderlo |

### 6.5. **`POR ADJUDICAR 5`: la cola de aristas que se escribe y no se lee. REGISTRO, Y NO ENCARGO MAQUINARIA**

**El hallazgo es cierto y lo reproduzco:** `arista_en_cola` la escribe `src/aduana.py` y sus tres
unicos lectores del repo son pruebas que comprueban que se escribio. **Ninguna corrida vuelve a la
bitacora a buscar la arista que esperaba.**

**ADJUDICO: es REGISTRO, no correccion declarada de `D.29`.** `D.29` dice literalmente que **mientras
el candidato espera en cuarentena la arista vive en un bloque propio y titulado del reporte**, y eso es
lo que la vuelta hizo (`W.5`). **La regla no promete un mecanismo: promete una sede.** Lo que el
hallazgo prueba es que **la sede depende de una mano**, y eso es cierto y es el coste. **Hoy son `2`
aristas en cola y las dos estan nombradas.** **No encargo maquinaria** (`5.6`), **y encargo la mano**:
la cola entera va al encargo, fila a fila, como `TAREA 5`.

### 6.6. **`POR ADJUDICAR 6`: la receta de `D.38.4` corrida al pie de la letra hace danio. CORRECCION DECLARADA POR `D.13`**

**El hallazgo de mi fase ciega, medido:** construir la poblacion a mano como *grafo mas bandejas*
**cuenta las bandejas dos veces** (`440` en vez de `348`) **y ademas tumba al candidato por la guarda
`el id ya vive en el grafo`**, porque el candidato acaba dentro de su propia poblacion.

**ADJUDICO POR `D.13`, que es regla escrita y no lectura mia:** *entre dos reglas fechadas que chocan
gana la mas reciente, y la perdedora se corrige sin borrarse.* **`D.38.4` es del 11 sep, cuando la
aduana media solo el grafo. `D.38.5` llego a `src/aduana.py` el 16 sep y hace ese trabajo sola.**

> **LA CORRECCION DECLARADA QUE ENCARGO, y se escribe SIN BORRAR el texto viejo:** en `D.38.4` del
> banco, que la receta de construir la poblacion a mano **queda superada por `D.38.5`**, y que el
> barrido del auditor se hace **entregando a la aduana la poblacion del grafo y dejando que ella ponga
> las bandejas**. **No muevo la regla yo: `5.6` dice cuales son mis sedes y el banco no es una.** Va al
> encargo dentro de la `TAREA 1`.

### 6.7. **`POR ADJUDICAR 7`: las `8` lineas `SIN HUELLA` que no se pueden comprobar nunca. REGISTRO**

**El hallazgo:** las ocho se emitieron cuando su vecino esperaba en la bandeja, **asi que la huella que
guardaron es la de un nodo VACIO** y no hay texto contra el que releerlas.

**ADJUDICO: registro, y `D.15` ya lo cubre.** `D.15` da dos salidas y **declararlas es una de las dos**.
La vuelta uso esa, sin tocar clase ni huella, y lo compruebo por diferencia en `1.5`. **Lo que queda no
es una fila abierta: es que el instrumento no sabe leer el campo que la cierra**, que es la propuesta
`1`. **Y digo el precio con su numero, porque es el precio de `D.38.5` y no de esta vuelta: `8`
veredictos de una sola tanda que no se podran comprobar nunca contra el texto con el que se emitieron.**

### 6.8. **`POR ADJUDICAR 8`: `The rock tumbler` (`L212-224`). PROPUESTA SOSTENIDA, Y NO ES CAIDA**

**Mi fase ciega leyo que `L217` a `L223` trae tres encargos al jefe con su consecuencia y que ningun
nodo de `DEBATE` los recoge.** Lo mantengo **como propuesta** y **adjudico que no es caida de la
vuelta**, por la misma razon que `2.2`: **`L223` es cabeza de lista** (*Here are some ideas that can
help you...*) **y una cabeza de lista sin procedimiento propio no es nodo** (`EXTRACTOR.md` 9).

**Lo que no se resuelve solo es `L221`**, que no es cabeza de lista sino encargo (*Your job as a boss
is to turn on that "rock tumbler"*). **Va al encargo como fila de cola, no como tarea**, porque
`cap_07` esta cerrado en insercion y reabrirlo por una pieza pide una decision de alcance que no es
mia.

### 6.9. **`POR ADJUDICAR 9`: los cuatro fallos de la prueba de aceptacion. ARTEFACTOS DE LA FASE CIEGA, Y LO MIDO**

**Mi lectura ciega decia que eran artefactos y que se curarian solos. Hoy: `193` pruebas, `0` fallos.**
**Acerte, y lo que lo prueba no es mi lectura: es el instrumento corrido hoy** (`.v30c/test.txt`). **No
es caida de nadie y no toca ninguna racha.**

---

## 7. LAS CAIDAS DEL EXTRACTOR, CON SU ESPECIE Y SU SEDE

### 7.1. **`REPORTE`: la cita que sostiene su discutible mas fragil apunta al acta equivocada**

**LO QUE PUBLICA**, en `W.6`, **celda de la tabla de discutibles**, y otra vez en la prosa de `W.3.a`:

> la **`ACTA 28`** `2.2` adjudico que **una remision hacia atras no es una cabeza**

**LO QUE MIDO:**

    $ (seccion 2.2 de cada acta, buscada dentro de su propio rango)
      ACTA 28 seccion 2.2 (linea 25470): DISCUTIBLE 2: SIN HUELLA en vez de NODO IDO para la
                                         huella de un nodo vacio. SOSTENIDO
      ACTA 27 seccion 2.2 (linea 24666): DISCUTIBLE 3: centrar_debate_ideas_fuera_egos contra
                                         fijar_fecha_cierre_debate_equipo. SOSTENIDO, CONTAMINADA
    $ grep -n "remision hacia atras" docs/loop/ACTA_AUDITOR.md
      24700:  ... Una remision hacia atras no es una cabeza.                  (dentro de la ACTA 27)
      25075:  ... es una remision hacia atras veintiocho lineas despues ...   (dentro de la ACTA 27)

**La adjudicacion existe, esta bien citada en su contenido, y vive en la `ACTA 27`, no en la `28`.**

| | |
|---|---|
| **especie** | **`REPORTE`**: una afirmacion equivocada que no mueve ningun dato (`5.2`) |
| **sede** | `docs/loop/REPORTE.md`, **celda de tabla** en `W.6` mas prosa en `W.3.a` |
| **acumula** | **SI.** Vive en TABLA (`5.2`), y **una cita publicada como el fundamento de una adjudicacion es una ruta que promete prueba**: cosecha `7.B` dice que eso **es cifra en su sede**, y aqui la ruta apunta a una seccion que dice otra cosa. **Adjudico por extension natural de `7.B` y la cito**, que es lo que `AUDITOR_FORJA.md` 1.3 me autoriza a hacer |
| **la lectura que le salvaria, y no la tomo** | *el contenido es correcto y solo falla el numero*. **Es cierto, y es justo lo que hace la cita peligrosa**: quien vaya a comprobarla lee una adjudicacion distinta y la da por buena. **Es la misma figura que la ruta vacia, que le costo dos paradas a esta casa** |
| **el atenuante, que digo porque es verdad** | **el extractor se puso la objecion contra si mismo y la enuncio bien.** La caida no es de razonamiento: es de puntero |

**Y LA MISMA CITA VIAJA A UNA TERCERA SEDE, que registro y no cuento dos veces:** la razon de la **linea
`300` de `bitacora/VEREDICTOS.jsonl`** dice *la `ACTA 28` `2.2` lo adjudico `SANO` SIN ARISTA*. **El
veredicto de esa linea es correcto y lo releo en `3.2`**, asi que **no es `CLASE`**: `CLASE` es un
veredicto mal puesto y este esta bien puesto. **Es el mismo defecto en otra sede, y la tanda es la
unidad: un escalon, no dos.** **Se corrige con `forja.py anotar`, sin tocar la clase**, y va al encargo.

### 7.2. **LO QUE NO ES CAIDA Y LO DIGO PARA QUE NADIE LO CUENTE COMO TAL**

| | |
|---|---|
| la arista `cuidarse` paso `7` que falta (`6.2`) | **registro con nombre, NO acumula.** No hay veredicto mal puesto porque no hubo veredicto |
| `192` contra `193` pruebas (`1.1`) | **no es caida:** el arbol se movio despues del cierre, y lo pruebo con `git` |
| `censos/` movido | **no es `DATO MOVIDO`:** crece `+3` y `+32` lineas y **no pierde ninguna**, que es lo que el manual seccion 3 punto 6 manda al insertar |
| `W.2.e`, el censo de uno en uno trece veces | **no verificable con lo que hay en el arbol**, y compatible con lo que si mido. **No la firmo y no la cuento** |

---

## 8. **MIS PROPIAS CAIDAS, CON MI NOMBRE Y ANTES DE LAS RACHAS**

> *La metrica que solo encuentra fallos ajenos no es una metrica* (`5.3`).

### 8.1. **`REMEDIO ROTO`: el `REMEDIO 1` que escribi en la `ACTA 28` lo rompi en la apertura siguiente**

**LO QUE ESCRIBI** (`ACTA 28`, tabla de remedios, antes de su seccion `9`):

> **`REMEDIO 1`: NINGUNA CELDA DE MI APERTURA SELLADA PUBLICA EL RESULTADO DE UNA LECTURA DISCUTIBLE
> COMO CIFRA.** Una arista, una clase o una frontera que mi fase ciega levante y que el turno normal
> aun tiene que adjudicar se publica en la tabla como `POR ADJUDICAR`, **nunca como un numero cerrado.**

**LO QUE PUBLIQUE** (`APERTURA_CIEGA.md` `4`, **sellada**):

> | **`cuidarse_agotamiento_centro_rueda`** | **7** | **3** | **4** |
> | **mi muestra** | **48** | **44** | **4** |
>
> **Sobre los 42 pasos de `cap_07` que he leido, mi cuenta da 4 puentes: `9,52` por ciento.**

**Es exactamente el caso del remedio: una lectura que yo mismo marque como `MI DISCUTIBLE 3` y deje
como `POR ADJUDICAR 3`, publicada como `4` y como `9,52` en celdas de tabla.**

| | |
|---|---|
| **especie** | **`REMEDIO ROTO`** (`D.38.2`). **Es de sustancia de auditoria** (cifras y lecturas), no de formato de artefacto, asi que la acotacion del 12 sep no lo saca |
| **el atenuante, que mido y NO uso** | **el arnes no me lo entrego.** `python forja.py herencia` devuelve como `HEREDADO 1` y `2` las secciones `3.2` y `6.1` de la `ACTA 28`, que **citan** remedios viejos, **no la tabla que escribe los nuevos** (`0.1`). **El remedio nunca llego a mi prompt** |
| **por que no me absuelve** | **`D.40` lo dejo escrito para este caso exacto:** *el fallo era de arquitectura, y la arquitectura es del arnes. **El siguiente `REMEDIO ROTO` acumula como cualquier otro.*** Y `5.4` corregida el 16 sep dice que mis dos predecesores eligieron la lectura que les perjudicaba. **Elijo la misma** |
| **y por eso el remedio del arnes lo ENCARGO, no lo declaro** | `1.4`: *la escalada se encarga, no solo se declara*. Va como **`TAREA 2` bloqueante** |

### 8.2. **`CIFRA PUBLICADA PROPIA`: el `4` y el `9,52` de esa misma tabla son `0` y `0,00`**

**Adjudicado en `4.2` con el manual y con `D.30` delante.** La cifra buena de mi tabla sellada es **`0`
puentes** y **`0,00` por ciento**.

| | |
|---|---|
| **especie** | **`CIFRA PUBLICADA PROPIA`** (`D.38.2`): una cifra falsa en mi apertura sellada |
| **sede** | `docs/loop/APERTURA_CIEGA.md`, sellada como `406ca90e54a2097d3f8371f01346b48a5d377d51` |
| **no la corrijo en su sitio** | el sello lo prohibe. **La correccion declarada vive aqui**, y esta es la sede que manda |
| **la lectura que me salvaria, y no la tomo** | *iba marcada como `LECTURA` y como discutible, y `D.38.3` ensanchada manda publicar la conclusion marcada para que el siguiente la cace*. **Es cierto, y por eso la caida es de la celda y no de la costumbre: lo que `D.38.3` manda marcar es la conclusion, y lo que mi propio `REMEDIO 1` prohibia era ponerle un numero a una celda.** Hice lo uno y falle lo otro |

### 8.3. **LAS DOS SON UNA TANDA, Y LA TANDA ES LA UNIDAD**

**`8.1` y `8.2` son el mismo fallo visto por dos sitios**, que es lo que `D.38.2` dice de sus dos
especies: *un remedio roto es una promesa que no se cumplio, y una cifra propia falsa es una
comprobacion que no se hizo.* **Suben mi racha UN escalon, no dos.**

### 8.4. **LO QUE SI FUNCIONO, y lo digo sin usarlo de excusa**

**El testigo de guardas de `D.45` corrio sobre mi por primera vez y no me desmintio ni una cifra**, y
mi fase ciega **predijo por escrito** que el censo de rutas estaria en verde al sellar y por que. **Lo
estuvo.** Y mi barrido ciego de vecinos **dio los mismos doce numeros que la aduana** sin haberla
visto. **Ninguna de las dos cosas me quita el escalon de `8.1`.**

### 8.5. **MIS REMEDIOS PARA EL SIGUIENTE, numerados y con comprobacion mecanica**

*`D.40` dice que el arnes los entrega. Como hoy he medido que el arnes coge la seccion equivocada, los
escribo **en la seccion que la `TAREA 2` tiene que aprender a leer**, y los escribo cortos.*

| # | **REMEDIO** | como se comprueba que se cumplio |
|---:|---|---|
| **1** | **NINGUNA CELDA DE MI APERTURA SELLADA LLEVA UN NUMERO QUE SALGA DE UNA LECTURA MIA.** Si el numero lo produce un instrumento, va con su salida pegada; **si lo produzco yo leyendo, la celda dice `POR ADJUDICAR` y el numero va en la frase, marcado `LECTURA`** | que **ninguna celda de tabla** de `APERTURA_CIEGA.md` contenga una cifra cuya unica fuente sea una lectura mia, y que **cada `POR ADJUDICAR` tenga su seccion en el acta** |
| **2** | **LA RELECTURA CIEGA DESTAPA UNA RAZON POR VEZ, Y DESPUES DE ESCRIBIR MI CLASE A FICHERO.** Nunca un comando que saque varias razones de golpe | que el acta publique **la hora del fichero de mis clases** y que sea **anterior** a la primera consulta de la bitacora. Hoy: `.v30c/mis_clases_pineada.txt`, `16:32:33` |
| **3** | **TODA REGLA QUE CITE LA LEO EN SU SEDE EN LA MISMA FASE EN QUE LA CITO.** Mi caida de `4.2` fue citar el manual de memoria y atribuirle lo contrario de lo que dice | que cada cita de regla del acta o de la apertura **lleve su texto pegado o su numero de seccion comprobado**, no solo su nombre |

---

## 9. LAS RACHAS AL CERRAR, Y LAS SEIS CONDICIONES DE PARADA

### 9.1. Las cuatro rachas, con su motivo

| especie | de quien | venia en | **queda en** | por que |
|---|---|---|---|---|
| **`CLASE`** (y `DATO MOVIDO`) | extractor | 1 de 2 | **0 de 2** | **tanda limpia.** `16` de `16` pineadas sostenidas, `8` de `8` discutibles sostenidos, **cero veredictos mal puestos** y **cero dato movido**, medido por diferencia en `1.5`. La reinicia **una tanda limpia** (`D.38.1`, y la correccion de `5.4` del 16 sep: *limpia significa sin caidas de la especie que esa racha acumula*) |
| **`CIFRA PUBLICADA`** | extractor | 0 de 2 | **0 de 2** | **no toca ninguna de sus sedes.** Lo mido: `git diff --name-only b9f484a faa0dd1` **no trae ni un fichero de `docs/` fuera de `loop/`, ni de `config/`, ni de `esquema/`, ni de `src/`** |
| **`REPORTE`** | extractor | 0 de 3 | **1 de 3** | **la cita mal atribuida de `7.1`**, en celda de tabla |
| **la mia, una sola** | **auditor** | **0 de 3** | **1 de 3** | **`REMEDIO ROTO` mas `CIFRA PUBLICADA PROPIA`** (`8.1`, `8.2`), **una tanda, un escalon** |

**DIGO QUE REINICIO MI RACHA Y QUIEN LA REINICIO, porque `5.4` me obliga a citarla y porque *ninguna de
las dos eres tu*:** venia en `3 de 3` con parada, y la reinicio **una decision del fundador**, no una
tanda limpia:

> **decision del fundador del 16 sep 2026, punto 2**, archivada en
> `docs/loop/paradas/2026-09-16-el-cerrojo-y-el-testigo-DECISION.md`:
> *LA RACHA DEL AUDITOR SE REINICIA con la cura de `A.4`: el TESTIGO DE GUARDAS AL SELLAR.*

**Asi que mi contador entra en esta vuelta en `0` y sale en `1 de 3`.**

### 9.2. La consecutividad, medida contra las actas y no contra mi memoria

| tanda | `CLASE` extr. | `REPORTE` extr. | **la mia** | de donde |
|---|---|---|---|---|
| **vuelta 27** | 0 de 2 | 2 de 3 | 2 de 3 | `ACTA 27` |
| **vuelta 28** | 1 de 2 | 0 de 3 (tanda limpia) | 3 de 3, **parada** | `ACTA 28` |
| **reinicio** | | | **0 de 3**, decision del fundador del 16 sep, punto 2 | `paradas/2026-09-16-el-cerrojo-y-el-testigo-DECISION.md` |
| **vuelta 30** | **0 de 2** (tanda limpia) | **1 de 3** | **1 de 3** | esta acta |

**No hay vuelta 29**, medido en la seccion `0`, **asi que la 28 y la 30 son consecutivas y la palabra
*seguidas* de `5.2` se aplica entre ellas sin hueco.**

### 9.3. **LAS SEIS CONDICIONES DE PARADA, UNA A UNA** (`AUDITOR_FORJA.md` 3)

| condicion | mi medida |
|---|---|
| **doctrina NUEVA necesaria** | **NO.** Los `8` discutibles, las `3` propuestas y los `9` `POR ADJUDICAR` se adjudican **citando regla escrita**: `D.29` con su ejemplar, `D.30`, `D.13`, `D.15`, `D.37` en su lectura estrecha, `D.38.5`, manual seccion 3 puntos 4 y 5, `EXTRACTOR.md` 9, `P.5.1`, `6.1`, `ACTA 27` `2.2` y `ACTA 28` `4.3`. **La unica extension que hago es la de cosecha `7.B` a una cita**, y `1.3` autoriza adjudicar por extension natural **citando la regla**, que es lo que hago en `7.1` |
| **contradiccion con regla vigente o cifra publicada** | **HAY UNA Y SE RESUELVE CON REGLA ESCRITA**: `D.38.4` contra `D.38.5` (`6.6`). **La resuelve `D.13`**, y la correccion declarada va al encargo. **Ninguna cifra publicada queda contradicha sin resolver** |
| **decision de Alexis** | **NO hay nada reservado.** Nada que borrar, ningun umbral movido, ningun remoto, ningun gasto fuera del repo, ningun cambio de alcance. **La reparacion del arnes de la `TAREA 2` no es maquinaria nueva: es que un mecanismo que `D.40` ya ordena haga lo que su regla dice**, y la exige una caida de esta misma tanda con su cita (`8.1`) |
| **fallo tecnico repetido** | **NO.** `gate`, `guiones`, `resolutor`, `193` de `193` pruebas, `tallar_reporte` y `censar_rutas` **en verde hoy, los siete**. Y los `4` fallos de mi fase ciega **estan en verde**, asi que no hay dos vueltas seguidas de nada |
| **credito roto** | **NO.** `CLASE` `0 de 2`, `CIFRA PUBLICADA` `0 de 2`, `REPORTE` `1 de 3`, **la mia `1 de 3`.** Ninguna llega a su tope |
| **campania consumada** | **NO.** Lote 4 al **`53` de `142`** insertados (`37,3` por ciento), **`89` en bandeja**, lote 5 sin abrir con sus `3` |

> ### **NO HAY PARADA. `PROMPT_SIGUIENTE.md` se escribe y `PARA_ALEXIS.md` NO se escribe.**
>
> **Y lo digo con la palabra que le corresponde al extractor: esta vuelta cierra `cap_07` entero, con
> los doce candidatos dentro, las dos series `D.37` cerradas, las ocho lineas `SIN HUELLA` declaradas,
> el par del calendario leido y escrito en su sede, y el reparto de sus `77` pares cuadrando al digito
> contra un barrido ciego que no habia visto.** Su unica caida es un numero de acta.
>
> **La mia es haber roto mi propio remedio en la primera apertura despues de escribirlo.**

### 9.4. **LA ESCALADA SE ENCARGA, NO SOLO SE DECLARA** (`1.4`, `5.5`)

**`5.5` obliga a abrir con el remedio como tarea bloqueante cuando hay tres actas seguidas con la misma
caida propia. No es el caso hoy** (mi racha esta en `1 de 3`, reiniciada por el fundador). **Pero `1.4`
obliga siempre que exista un remedio autorizado, y existe:**

| lo que detecto | el remedio autorizado | donde lo encargo |
|---|---|---|
| el arnes entrega como remedios heredados secciones que **citan** remedios viejos, no las que **escriben** los nuevos (`0.1`, `8.1`) | **`D.40`, ya escrita y ratificada por el fundador**: *lo que un auditor le deja al siguiente lo entrega el arnes, no la memoria* | **`TAREA 2` BLOQUEANTE** del encargo, con caso positivo escrito |
| un par leido y adjudicado que **ninguna senial va a levantar nunca** (`6.1`) | **`D.29`**: la arista que la senial no levanta se declara por lectura | **`TAREA 4`**, con la clase ya adjudicada por mi |
| una arista `D.29` que existe y que nadie juzgo (`6.2`) | **`D.29`**, y los dos extremos ya viven | **`TAREA 3`**, cableable hoy |

---
