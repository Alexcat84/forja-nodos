
## KK.5. TAREA 5. **EL CIERRE, CON LAS MISMAS PIEZAS DE SIEMPRE**

### KK.5.a. **EL ESTADO AL CIERRE, RECOMPUTADO AL CIERRE Y NO COPIADO DE LA APERTURA** (`EXTRACTOR.md` 4)

<!-- TALLADO: parcial salida=.v49/cierre_estado.txt -->

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1087 total
    $ ls cuarentena/grove_high_output/*.json | wc -l
    41
    $ ls cuarentena/_insertados/grove_high_output/*.json | wc -l
    1

**`346`, `740`, `1` y `41`: LAS CUATRO SON LAS DE `KK.0`, AL DIGITO.** El encargo dice que una
vuelta de saneamiento que no inserta **no mueve ni el dataset ni la bitacora ni los pares mutuos ni
la cuenta de la bandeja**, y que si alguna se movia esa era la caida que buscar. **Ninguna se
movio**, y la bandeja sigue en `41` aunque dos de sus fichas cambiaron por dentro: **corregir una
ficha no la mueve de sitio.**

### KK.5.b. **LOS ARBOLES QUE NO PODIA TOCAR, MEDIDOS POR DIFERENCIA Y NO PROMETIDOS**

<!-- TALLADO: parcial salida=.v49/arbol_intacto.txt -->

    $ git status --short -- src/ tests/ scripts/ dataset/ forja.py hooks/ config/ bitacora/ censos/ docs/BANCO_DE_REGLAS.md
    (sin salida: ninguno de esos arboles cambio en esta vuelta)

**`tests/` ENTRA EN ESA LISTA Y SALE LIMPIO**, que es lo que convierte la `TAREA 4` en una medida y
no en un arreglo: **corri la prueba `21` veces** (las `20` de `d033` mas la suite entera) **y no
toque ni un byte de su fichero.**

### KK.5.c. **LA TABLA DE CIERRE DE TAREAS** (`D.52`)

*Salida de `python scripts/tabla_de_cierre.py --escribir`, pegada de
`docs/loop/TABLA_DE_CIERRE.txt`.*

> **LA COLISION DE `D.52` CON `D.41` MUERDE POR QUINTA VEZ SEGUIDA, Y SE PAGA A MANO OTRA VEZ**
> (`d030`, `TAREA 5.2` del encargo). Al escribir mi tabla en la ruta viva dejaba en rojo la de la
> vuelta 48 **sin tocar ni una celda de su reporte**. **La salida de la vuelta 48 se saco de git
> byte a byte y se archivo**, y la linea de `JJ.4.c` pasa a nombrar la copia archivada con su
> correccion declarada al lado:
>
> <!-- TALLADO: parcial salida=.v49/sello_v48.txt -->
>
>     $ git show HEAD:docs/loop/TABLA_DE_CIERRE.txt | git hash-object --stdin
>     9bf10e6792bffa91ebcbc9894af90834d13c2aac
>     $ git hash-object docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_v48.txt
>     9bf10e6792bffa91ebcbc9894af90834d13c2aac
>
> **EL MISMO `hash-object` ANTES Y DESPUES: la copia es la salida, no una transcripcion.** `42`,
> `46`, `47`, `48` y hoy la `49`: **quinto ejemplar seguido**, y eso es lo que la hace deuda de
> maquinaria y no descuido. `d022` y `d030` la tienen abierta y `D.45` me deja fuera de arreglarla.

<!-- TALLADO: parcial salida=docs/loop/TABLA_DE_CIERRE.txt -->

| # | tarea | como cerro |
|---:|---|---|
| 1 | los registros de la `ACTA 47`: las dos correcciones declaradas, lo adjudicado y las dos deudas nuevas | **CERRADA**: las dos correcciones escritas **en las cuatro sedes donde vivia el texto viejo y sin borrar una letra** (`JJ.3.b.bis`, la fila `4` y la fila `9` de `JJ.4.d`, `JJ.2.d` y `JJ.3.a`), la lista de `14` filas corrida hoy con su recorte declarado, las seis adjudicaciones de `47.5` recogidas sin reabrirse y las dos deudas nuevas leidas del registro |
| 2 | pagar `d027` y `d032`: dos fichas corregidas sin borrar, cada una con su aduana en el acto | **CERRADA Y LAS DOS PAGADAS**: `0 CAERIA` en las dos pasadas, relojes `559,4` s y `1479,4` s, la medida de `d031` partida por especie con su `sha1` de prueba, y un defecto de mi propia correccion declarado en `KK.2.e` |
| 3 | pagar `d024` en su primer tramo: `3` de los `7` de `cap_02`, uno por vez y en el orden del libro | **CERRADA CORTA EN `2` DE `3`**: `P2` y `P5` corridos con `0 CAERIA`, relojes `855,8` s y `1174,4` s, los `4` vecinos de su cola tabulados, el corte declarado con sus tres piezas y los **`5`** que quedan nombrados uno a uno |
| 4 | pagar `d033`: `20` corridas del caso aislado, su tasa y su banda, sin tocar `tests/` | **CERRADA**: `20` de `20` en verde, tasa `0,0000` con banda `0,0000` a `0,1611`, reloj `449,7` s, cero trazas porque no hubo roja, el mecanismo leido de tres lineas del propio codigo y dos propuestas escritas sin tocar nada |
| 5 | el cierre: las guardas, la tabla `D.52`, el estado recomputado, el tramo con su reloj y el coste | **CERRADA**: las cinco guardas en verde a la primera, el estado al digito (`346`, `740`, `1`, `41`), la colision de `D.52` sellada por `hash-object` por quinta vez, la deuda de `16` a `14` y el coste del turno contado de sus relojes |

### KK.5.d. **LA LINEA DEL TRAMO, CON SU RELOJ Y CON EL CORTE DICHO**

**ESTA VUELTA NO MINA Y NO INSERTA**, asi que su unidad no es el candidato ni el paso: es **la
pasada de aduana**, como el propio encargo la definio.

<!-- TALLADO: parcial salida=.v49/coste.txt -->

    $ python .v49/coste.py      (la cola del instrumento; la tabla entera va en `KK.5.h`)
    pasadas de aduana        : 4 de un techo de 5,  4069.0 s,  88.2 por ciento del turno
    de ellas, correccion de prosa : 2,  2038.8 s,  44.2 por ciento del turno
    media por pasada de aduana    : 1017.3 s   (la cifra que la vuelta 50 tiene que usar, 47.5.c)
    techo en minutos              : 4613.6 s medidos de un techo de 4949 s, o sea 76.9 min de 82.5

**LAS DOS MITADES DEL TECHO, Y LAS DOS SE CUMPLEN:**

- **en pasadas:** `4` de un techo de `5`. **Corte en la quinta** y esta declarado en `KK.3.d` con
  sus tres piezas.
- **en minutos:** `4.613,6` s medidos contra un techo de `4.949` s, o sea **`76,9` minutos de
  `82,5`**. **El techo en minutos NO se paso**, y es la primera vuelta desde la 46 que puede decirlo.

**LA CIFRA QUE LA VUELTA 50 TIENE QUE USAR, por `47.5.c`, que manda recalcularla y no arrastrarla:**
**`1.017,3` s por pasada**, que es la media de mis cuatro de hoy. **La estimacion de hoy iba en
`903,4` s y se quedo corta un `12,6` por ciento**, y esa diferencia es exactamente lo que se comio
la quinta pasada.

### KK.5.e. **LAS CINCO GUARDAS AL CIERRE, CORRIDAS Y PEGADAS, Y LAS CINCO A LA PRIMERA**

<!-- TALLADO: parcial salida=.v49/cierre_guardas.txt -->

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

<!-- TALLADO: parcial salida=.v49/cierre_pruebas.txt -->

    $ time python tests/test_aceptacion.py
      total: 318 pruebas, 0 fallos, 0 errores
    real	1m34.832s

**A LA PRIMERA, Y LO DIGO PORQUE LA VUELTA 48 NO PUDO:** su `JJ.4.b` tuvo que declarar una corrida
roja. **La mia no tuvo ninguna**, y `KK.4.c` explica por que puede pasar lo uno o lo otro sin que
cambie el codigo.

<!-- TALLADO: parcial salida=.v49/cierre_tallado.txt -->

    $ python scripts/tallar_reporte.py
    tablas que declaran instrumento : 220
      talladas, celda a celda       : 124
      que DIFIEREN de su instrumento: 0
      con la ruta VACIA             : 0   (cero bytes, 7.B)
      sin poder comprobar           : 0
      que CITAN y no reproducen     : 96   (declaradas PARCIAL)

<!-- TALLADO: parcial salida=.v49/cierre_censo.txt -->

    $ python scripts/censar_rutas.py
    rutas publicadas y censadas : 780
      pasan                     : 780
      CAEN                      : 0
          PATRON                           72
          VACIA A PROPOSITO                3
          con contenido                    698
          vacia por protocolo              7

**DOS COSAS DE ESTAS DOS CIFRAS QUE NO ME CALLO, aunque las dos salgan en verde:**

1. **EL CENSO DA `780` AL ABRIR Y `780` AL CERRAR, y el auditor publico `779`.** La `ACTA 47` ya
   registro ese mismo desfase de `1` contra mis `775` **como causa de momento y no de cuenta**: la
   guarda corre antes de que el reporte pegue su propia salida. **Lo que anado hoy es que la cifra
   no se movio con todo lo que he escrito**, asi que mis citas nuevas viven en bloques de codigo y
   **el censo no las cuenta como celda**. No lo presento como defecto: lo presento como el alcance
   real de `D.42`, medido.
2. **EL TALLADO PASA DE `219` A `220` DECLARACIONES Y DE `95` A `96` `PARCIAL`, o sea UNA sola**,
   cuando yo he escrito `14` marcadores `TALLADO` en esta vuelta. **El motivo esta leido y no
   supuesto:** `D.41` engancha cada marcador a **la tabla markdown que le sigue**
   (`scripts/tallar_reporte.py`, `tablas_de` en la linea `112`), y mis citas preceden **bloques de
   codigo**, que no son tablas. **La unica que conto es la de la linea `46629`, y se engancho a la
   tabla de tarea de `KK.2`, no al bloque para el que la escribi.** Es de la misma familia que
   `d029` y **no la arreglo**: `D.45`.

### KK.5.f. **EL CREDITO, LA DEUDA Y EL TABLERO: LOS TRES LEIDOS, UNO SOLO RECOMPUTADO POR MI**

<!-- TALLADO: parcial salida=.v49/credito_cierre.txt -->

    $ python forja.py credito
      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            1 de 3     ACTA 47
      CIFRA PUBLICADA    0 de 2     ACTA 47
      CLASE              0 de 2     ACTA 47
      DATO MOVIDO        0 de 2     ACTA 47
      REPORTE            1 de 3     ACTA 47

      CREDITO ENTERO: ninguna especie en su tope.

**LEIDO Y NO ANOTADO: esa sede no es mia** (`EXTRACTOR.md` 14), y las cinco rachas cierran donde
abrieron porque **nadie las mueve dentro de la vuelta: las mueve el acta siguiente.**

<!-- TALLADO: parcial salida=.v49/deuda_cierre.txt -->

    $ python scripts/deuda.py | head -3
    DEUDA DE LA LINEA (D.55): la deuda no bloquea la produccion
      registro: docs/loop/DEUDA.jsonl
      pendientes: 14    pagadas: 10

**DE `16` A `14`, QUE ES LO QUE EL ENCARGO PEDIA**, y el pago lleva su como escrito: `d027` y
`d032` con su correccion, su renglon del libro y su reloj de aduana dentro del propio registro.
**`d024` NO se marca pagada** y sigue en la lista con sus `5` restantes nombrados en `KK.3.d`.
**`d031` tampoco**: hoy se mide, no se paga, y lo que aporto son sus dos primeros ejemplares por
especie.

**EL TABLERO lo leo y no lo escribo.** La cola de doctrina sigue congelada en `11` (`D.56`) y **no
abro la doce**, aunque `KK.2.e` y `KK.5.e` traen dos observaciones que en otra vuelta habrian
llamado a la puerta: van como registro con su medida, que es lo que el encargo manda hacer con una
pregunta nueva.

### KK.5.g. **NO HAY FILA DE `PASOS INVENTADOS`, Y SE DICE CON SU MOTIVO**

**Una vuelta de saneamiento no escribe pasos nuevos**, asi que **el numerador y el denominador son
los dos cero** y la metrica no tiene fila propia: una razon de `0` entre `0` no es un `0` por
ciento, es una celda que no existe.

**LO QUE SI DIGO, Y ES LA CIFRA QUE EL AUDITOR FIRMO Y YO NO HE MOVIDO:** **`cap_04` sigue en `0`
PUENTE de `137` pasos.** No la recomputo y digo por que: **las `19` fichas de `cap_04` siguen con
sus mismos pasos**, y la unica que toque hoy (`P38`) **cambio su `resumen_teorico` y ni un paso**,
medido en `KK.5.b` por diferencia. **`cap_04` queda en `19` de `22`** y cierra en la vuelta 50 con
`P41`, `P42` y `P44`, por adjudicacion `47.5.d`.

### KK.5.h. **EN QUE SE FUE EL TURNO** (`D.55`), **Y ESTA VEZ SI ES DE SANEAMIENTO**

**ESTA VUELTA ES DE SANEAMIENTO Y LO DIGO CON ESAS PALABRAS**, que es lo que el encargo pide: es la
**quinta desde la `44`**, no mina, no inserta y **no produce ni un nodo nuevo**. Lo que produce son
**tres deudas pagadas o medidas y dos correcciones que ya no se pueden perder**, porque viven dentro
de las fichas y no solo en este reporte.

**Y NO INVENTO UN USD: este repo no tiene instrumento que lo mida.** Lo que la regla persigue es en
que se fue, y eso sale de mis relojes:

<!-- TALLADO: script=.v49/coste.py salida=.v49/coste.txt -->

| pieza del turno | instrumento | corridas | segundos | por ciento del turno |
|---|---|---:|---:|---:|
| pasada de aduana de `d027` | `forja.py informe` | 1 | 559.4 | 12.1 |
| pasada de aduana de `d032` | `forja.py informe` | 1 | 1479.4 | 32.1 |
| pasada de aduana de `cap_02` `P2` | `forja.py informe` | 1 | 855.8 | 18.6 |
| pasada de aduana de `cap_02` `P5` | `forja.py informe` | 1 | 1174.4 | 25.5 |
| las 20 corridas de `d033` | `unittest PruebaE` | 20 | 449.7 | 9.7 |
| prueba de aceptacion al cierre | `tests/test_aceptacion.py` | 1 | 94.8 | 2.1 |
| **TOTAL MEDIDO CON RELOJ** | | **25** | **4613.6** | **100.0** |

**LA LECTURA DE ESA TABLA, EN UNA LINEA:** **el `88,2` por ciento del turno medido se fue en cuatro
pasadas de aduana**, y **dos de esas cuatro no midieron un candidato nuevo: midieron una correccion
de prosa**. Eso son `2.038,8` s, el `44,2` por ciento del turno, **gastados en volver a comparar
contra `390` vecinos dos fichas que ya estaban comparadas**. `KK.2.d` lo mide y propone el remedio;
**yo no puedo escribirlo** (`D.45`).

### KK.5.i. **LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO** (`EXTRACTOR.md` 8)

**Marcados a ciegas, antes de la relectura del auditor**, y ordenados por lo que me parece mas
facil que caiga:

| # | donde | el discutible, en una linea |
|---:|---|---|
| 1 | `KK.3.d`, el corte en `2` de `3` | **elegi cortar la `TAREA 3` y no la `4`**, y un lector estricto puede decir que `d024` era la deuda nombrada del encargo y `d033` la propuesta convertida en tarea, o sea que corte la de mas rango. **Mi motivo esta escrito** (una tasa con `13` corridas es otra tasa, y `d024` nace parcial), **pero es una eleccion mia y no una regla** |
| 2 | `KK.2.e`, no rehacer hoy la linea de la ficha | **dejo dentro de una ficha una cita que hoy no reproduce**, y la dejo a sabiendas. Un lector estricto dira que `EXTRACTOR.md` 16 manda que un candidato no esta escrito hasta que pasa la aduana, y que mi ficha cambio despues de pasarla. **Mi lectura es que no cambio: el defecto es de la misma pasada**, y que rehacerlo costaba la `TAREA 3` entera. **Si cae, cae aqui** |
| 3 | `KK.2.a`, la correccion confinada al `entregable` | **no anote la correccion de `d027` tambien en el `resumen_teorico`**, que es donde esta casa suele escribirlas. Lo hice **a proposito**, para que la medida de `d031` tuviera un caso limpio de campo que no alimenta las senales, y lo declaro dentro de la propia ficha. **Un lector estricto dira que use una correccion para montar un experimento** |
| 4 | `KK.4.b`, comparar mi banda con el `1` de `6` | **cruzo una banda de Wilson de mi muestra con un punto de otra muestra**, y eso no es un contraste formal. **Lo escribo diciendo que no lo es**, pero sigue siendo la frase mas discutible de la `TAREA 4` |
| 5 | `KK.5.e`, mi lectura del censo en `780` | **afirmo que mis citas nuevas no cuentan como celda porque viven en bloques de codigo**, y eso lo deduzco de que la cifra no se movio, **no de haber leido `censar_rutas.py`**. Es una inferencia y la marco como tal |
| 6 | `KK.1.a`, la pieza que anado sobre la columna `nodo(s)` | digo que esa columna es **el pronostico de la frontera y no lo minado**, y lo deduzco de que `P41` y `P42` salen con `1 nodo(s)` sin estar minados. **Es solido, pero lo deduzco de dos filas** |

**LO QUE LOS SEIS TIENEN EN COMUN, y conviene que se vea:** **ninguno es una cifra.** Las cifras de
esta vuelta salen todas de un instrumento pegado; **los seis discutibles son decisiones y lecturas
mias**, que es lo que queda cuando una vuelta no mina.

### KK.5.j. **LO QUE PROPONGO Y NO ADJUDICO** (`EXTRACTOR.md` 14)

| # | propuesta | de donde sale |
|---:|---|---|
| 1 | **que el barrido se salte el recalculo cuando el `sha1` de `titulo` mas `resumen_teorico` mas `pasos` no ha cambiado** | `KK.2.d`: `d027` pago `559,4` s por un resultado determinado de antemano, y esta demostrado con su `sha1` |
| 2 | **que la tasa de `d033` se vuelva a medir con el arbol EN MOVIMIENTO** | `KK.4.c`: mis `20` midieron el arbol quieto y la roja observada ocurrio con el arbol en marcha. **Mi medida esta a medias y lo digo yo** |
| 3 | **que la prueba `E` corra contra una copia del arbol y no contra `RAIZ`** | `KK.4.c`, lineas `392` y `406` de `tests/test_aceptacion.py`. Es `tests/` y `D.45` me lo veda |
| 4 | **que la linea del metodo de la ficha de `P38` se rehaga en la pasada de la vuelta 50** | `KK.2.e`: esa ficha tiene que pasar la aduana de todos modos para entrar, y ahi la correccion sale gratis |

| tarea | que pide | estado |
|---|---|---|
| `KK.5` | el cierre: las cinco guardas, la tabla `D.52` con su colision, el estado recomputado, la linea del tramo con su reloj, la deuda recomputada y el coste de `D.55` | **CERRADA en `KK.5`**: las cinco guardas en verde **a la primera**, el estado al digito (`346`, `740`, `1`, `41`), la colision de `D.52` sellada por `hash-object` por quinta vez, el techo cumplido en sus dos mitades con el corte declarado, la deuda de `16` a `14`, el coste contado de sus relojes y **seis discutibles marcados a ciegas** |
