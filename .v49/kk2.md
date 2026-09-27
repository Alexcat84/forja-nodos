
## KK.2. TAREA 2. **`d027` Y `d032` PAGADAS: DOS FICHAS CORREGIDAS SIN BORRAR, CON SU ADUANA EN EL ACTO**

**Las dos correcciones estan DENTRO de la ficha, que es donde sobreviven al reporte**, y las dos
pasaron la aduana **en el mismo acto en que se escribieron** (`EXTRACTOR.md` 16). **Cero
inserciones**: la puerta de `D.39` mide cerrada (`KK.0.a`) y corregir una ficha no la mueve de la
bandeja.

### KK.2.a. **`d027`: EL ENTREGABLE QUE PUBLICABA UNA CUENTA QUE EL LIBRO NO DA**

**LOS DOS RENGLONES QUE LO DECIDEN, LEIDOS POR MI HOY Y PEGADOS CON SU `sed` AL LADO** (`D.35`):

    $ sed -n '145p' fuentes/grove_high_output/cap_04.md     (el tramo que decide, de la linea entera)
    145:...And as you can also see, I use many ways to get it. I read standard reports and memos
        but also get information ad hoc...
    $ grep -rn "six ways" fuentes/grove_high_output/
    (cero lineas: el libro ENTERO no escribe la cuenta, y no solo este capitulo)

**LA CORRECCION, ESCRITA AL LADO DEL TEXTO VIEJO Y SIN BORRARLO** (manual principio 6): donde el
`entregable_esperado` dice *las seis en uso* tiene que leerse *todas las que el libro nombra, en
uso*, **SIN CUENTA**.

**Y LA TENSION QUE LA PROPIA DEUDA NOMBRA, DECLARADA Y NO TAPADA:** `denominaciones.nombre_largo`
enumera **seis** vias y los **ocho** pasos las reparten de otra manera, porque los pasos `4`, `5` y
`6` parten la queja del cliente en tres mandatos que el libro escribe en tres frases distintas, y el
paso `8` no es una via sino la regla de preferencia que ordena a las otras siete. **La ficha tenia
DOS cuentas internas incompatibles y ninguna de las dos era del libro.** Por eso la correccion
**quita el numero en vez de cambiarlo por otro**: no invento la cuenta buena.

### KK.2.b. **`d032`: LAS DOS FRASES DE LA FICHA DE `P38`, UNA A UNA**

| # | la frase vieja, que se queda en pie | lo que tiene que leerse, medido hoy |
|---:|---|---|
| 1 | *Es el tramo mas rico de esta tanda* | **NO lo es.** `P38` tiene `396` palabras y `P34` tiene `469`, **de esta misma tanda**, y `P34` es madre de dos de los cinco candidatos de la vuelta 48. **La otra mitad de la frase, *el quinto del capitulo entero*, SI es cierta**: `P38` es el puesto `5` de `44` |
| 2 | *ese cinco sale del dibujo que el libro pone debajo* | **`L299` lo escribe en su propia prosa**, una frase antes de nombrar el esquema. **La decision de no escribir el `cinco` se sostiene y no la cambio**; lo que se corrige es el motivo, y el bueno es que el `cinco` es del **CASO** de la planta con dos secciones, y manual 3.5 dice que **el caso no es la casa** |

**LO QUE SOSTIENE LA MITAD 1, corrido por mi hoy y pegado entero en `JJ.3.b.bis`:** `P5 674`,
`P2 530`, **`P34 469`**, `P3 411`, **`P38 396`**. Y quien es la madre de `P34` no lo teclee:

<!-- TALLADO: parcial salida=.v49/madre_p34.txt -->

    $ grep -l "Sale de la PIEZA P34" cuarentena/grove_high_output/*.json
    cuarentena/grove_high_output/decir_no_trabajo_excede_capacidad.json
    cuarentena/grove_high_output/usar_calendario_herramienta_planificacion_produccion.json

**NI UN PASO NI UNA ATRIBUCION CAMBIAN.** El paso `10` sigue escribiendo la relacion y no el total,
y las atribuciones siguen llevando las cifras de la REGLA (*six to eight*, *three or four too few*,
*ten too many*, *half a day a week*, *two days a week*, *an hour a week*) **y ninguna del caso**.

### KK.2.c. **LAS DOS PASADAS DE ADUANA, CON SU RELOJ, QUE ES LO QUE EL ENCARGO VIENE A MEDIR**

<!-- TALLADO: parcial salida=.v49/informe_d027.txt -->

    $ time python forja.py informe cuarentena/grove_high_output/reunir_informacion_gerencial_vias_variadas.json
    poblacion del barrido       : 390   (346 del grafo mas 44 que esperan en bandejas)
    EL SALDO
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0
    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 4
      por candidato bloqueado          : menor 4, mediana 4, mayor 4
      que señal levanta cada vecindad  : similitud_texto 4
    real	9m19.396s

<!-- TALLADO: parcial salida=.v49/informe_d032.txt -->

    $ time python forja.py informe cuarentena/grove_high_output/dimensionar_numero_subordinados_medio_dia_semanal.json
    poblacion del barrido       : 390   (346 del grafo mas 44 que esperan en bandejas)
    EL SALDO
      ENTRARIAN sin leer nada          : 1
      BLOQUEARIAN esperando veredicto  : 0   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0
    real	24m39.398s

**CERO `CAERIA` EN LAS DOS. Ninguna correccion rompio su ficha**, que es lo unico que la aduana
puede certificar de una correccion de prosa. **Y las dos siguen en la bandeja**: un informe no
inserta.

### KK.2.d. **LO QUE ESTAS DOS CIFRAS MIDEN DE `d031`, Y NO LO DECIDO YO: LO MIDO Y LO PROPONGO**

| | `d027` | `d032` |
|---|---:|---:|
| **campo tocado** | `entregable_esperado` | `resumen_teorico` |
| **alimenta las senales** | **NO** | **SI** |
| **reloj de la pasada de hoy** | **`559,4` s** | **`1479,4` s** |
| **la misma ficha, medida antes** | no hay medida: es de la vuelta 46 y `d024` es la deuda hermana | **`1188` s** en la vuelta 48 (`JJ.2.d`, fila `4`) |
| **saldo hoy** | `BLOQUEARIA`, `4` vecinos, `0 CAERIA` | `ENTRARIA`, `0` vecinos, `0 CAERIA` |
| **se movio el saldo por la correccion** | **no se puede saber**: no habia medida previa | **NO: identico al de la vuelta 48** |

**LA PRIMERA MEDIDA, Y ES LA QUE MAS DICE:** la correccion de `d027` **no toco ni un caracter del
texto que las senales leen**, y aun asi costo la aduana entera. **No lo supongo: lo comparo.**

<!-- TALLADO: parcial salida=.v49/senial1_intacta.txt -->

    $ python .v49/senial1_intacta.py
    HEAD (antes de la correccion)     4505 caracteres  sha1 b3bc37aa10a219cb5b0e4f580fa865990499dfc5
    arbol (despues)                   4505 caracteres  sha1 b3bc37aa10a219cb5b0e4f580fa865990499dfc5

    texto que alimenta senal 1 y senal 3 IDENTICO : True
    entregable_esperado cambiado                  : True
    campos con diferencia                         : ['entregable_esperado']

**La senal 1 lee `titulo` mas `resumen_teorico` mas `pasos`** (`src/aduana.py` linea `278`) **y la
senal 3 lee los pasos contra el cuerpo `titulo` mas `resumen_teorico`** (linea `304`). **El
`entregable_esperado` no entra en ninguna de las dos**, asi que las cuatro vecindades de `d027` y
sus doce cifras habrian salido identicas sin mi correccion. **Pague `559,4` s por un recalculo cuyo
resultado estaba determinado antes de empezar.**

**LA SEGUNDA MEDIDA, Y VA EN CONTRA DE LO QUE YO ESPERABA:** `d032` **si** toco el texto de las
senales, y **el saldo no se movio ni un vecino**: `ENTRARIA` con `0` vecinos antes y despues. Lo
que si se movio es el precio: **`1479,4` s hoy contra `1188` s en la vuelta 48, `291` s mas sobre la
misma poblacion de `390`**. La correccion alarga el `resumen_teorico` de `7.820` a `10.180`
caracteres, y ese campo es justo el que las dos senales comparan contra los `390` vecinos.
**Una correccion declarada no solo cuesta una pasada: encarece todas las siguientes.**

**LO QUE PROPONGO, Y NO ADJUDICO** (`EXTRACTOR.md` 14): que el barrido pueda **saltarse el recalculo
cuando el texto que alimenta las senales no ha cambiado**, comprobandolo con el mismo `sha1` que
este reporte acaba de pegar. Con `d027` delante es una comparacion de tres lineas que habria
ahorrado la pasada entera. **No lo escribo yo:** vive en `src/`, y `D.45` me lo veda.

**Y LO QUE ESTAS DOS CIFRAS TODAVIA NO PERMITEN DECIDIR, dicho para que nadie las lea de mas:** son
**dos** ejemplares, uno por especie, y `d031` pidio **mas** ejemplares antes de decidir. Lo que hoy
si se puede decir, y antes no, es que **las dos especies no son la misma**: la que no toca las
senales es **inutil de recalcular y cara de correr**, y es la unica de las dos con remedio barato.

### KK.2.e. **UN DEFECTO DE MI PROPIA CORRECCION, DICHO POR MI ANTES DE QUE LO ENCUENTRE NADIE**

**La correccion de `d032` cita dentro de la ficha el comando con el que comprobe la madre de `P34`,
y ese comando, corrido hoy, ya no devuelve dos ficheros sino tres**, porque **la propia ficha pasa a
contener la cadena que el comando busca**. Es una cita que no reproduce, que es la especie que
`D.35` y `D.42` persiguen, y **la escribi yo hoy**:

<!-- TALLADO: parcial salida=.v49/autocita_d032.txt -->

    $ grep -l "PIEZA P34" cuarentena/grove_high_output/*.json      (el comando tal como quedo citado DENTRO de la ficha)
    cuarentena/grove_high_output/decir_no_trabajo_excede_capacidad.json
    cuarentena/grove_high_output/dimensionar_numero_subordinados_medio_dia_semanal.json
    cuarentena/grove_high_output/usar_calendario_herramienta_planificacion_produccion.json
    $ grep -l "Sale de la PIEZA P34" cuarentena/grove_high_output/*.json   (el preciso, el que si reproduce)
    cuarentena/grove_high_output/decir_no_trabajo_excede_capacidad.json
    cuarentena/grove_high_output/usar_calendario_herramienta_planificacion_produccion.json

**TRES CONTRA DOS, Y EL DE EN MEDIO ES LA FICHA MISMA.**

**LO QUE NO ES, Y LO DIGO PARA NO INFLARLO:** la **afirmacion** es cierta y sigue siendo
verificable. `P34` es la pieza de origen de `decir_no_trabajo_excede_capacidad` y de
`usar_calendario_herramienta_planificacion_produccion`, y el comando preciso que lo reproduce
(`grep -l "Sale de la PIEZA P34"`) es el que esta pegado en `KK.2.b` y da **dos**. Lo defectuoso es
**la linea del metodo dentro de la ficha**, no el dato.

**LO QUE NO HAGO HOY, Y POR QUE, CON LA CUENTA DELANTE:** arreglarlo son bytes de un
`resumen_teorico`, o sea **otra pasada de aduana entera**, y `d032` acaba de medirla en `1479,4` s.
Con `2.894,6` s ya gastados de un techo de `4.949` s (`KK.5.d`), esa pasada **se come la `TAREA 3`
entera**, que es una deuda nombrada del encargo. **El encargo pone el liston del corte en AVERIA**
(*y si alguno sale `CAERIA`, eso si es averia*), **y esto no lo es**: `0 CAERIA` en las dos pasadas.

**LO QUE SI HAGO:** lo dejo escrito aqui, y **propongo** que la linea se rehaga en la pasada que esa
ficha tiene que pasar de todos modos para entrar en el grafo, **la de la vuelta 50**, que es donde
sale gratis. **No lo adjudico yo** (`EXTRACTOR.md` 14).

| tarea | que pide | estado |
|---|---|---|
| `KK.2` | pagar `d027` y `d032`: las dos fichas corregidas sin borrar, cada una con su pasada de aduana en el acto y su reloj | **CERRADA en `KK.2`**: las dos correcciones escritas dentro de su ficha con el renglon del libro pegado, **`0 CAERIA` en las dos**, relojes `559,4` s y `1479,4` s, la medida de `d031` **partida por especie** con su propuesta escrita y no adjudicada, y **un defecto de mi propia correccion declarado en `KK.2.e` con su cuenta** |
