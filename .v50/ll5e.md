
### LL.5.e. **LAS CINCO GUARDAS AL CIERRE, CORRIDAS Y PEGADAS, Y LAS CINCO A LA PRIMERA**

<!-- TALLADO: parcial salida=.v50/cierre_guardas.txt -->

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

<!-- TALLADO: parcial salida=.v50/cierre_pruebas.txt -->

    $ python tests/test_aceptacion.py
    OK (skipped=1)
      total: 318 pruebas, 0 fallos, 0 errores
    real	1m37.000s

**A LA PRIMERA Y SIN NINGUNA ROJA**, que es lo que `d033` vigila desde la vuelta 48: **la corrida
intermitente no ha vuelto a aparecer**, y con esta van `21` corridas seguidas en verde contando las
`20` de `KK.4`. **No la marco pagada ni la doy por muerta**: `d033` sigue abierta porque la
condicion que la produjo, el arbol en movimiento, **sigue sin reproducirse**, no sin existir.

<!-- TALLADO: parcial salida=.v50/cierre_tallado.txt -->

    $ python scripts/tallar_reporte.py
    tablas que declaran instrumento : 232
      talladas, celda a celda       : 128
      que DIFIEREN de su instrumento: 0
      con la ruta VACIA             : 0   (cero bytes, 7.B)
      sin poder comprobar           : 0
      que CITAN y no reproducen     : 104   (declaradas PARCIAL)

<!-- TALLADO: parcial salida=.v50/cierre_censo.txt -->

    $ python scripts/censar_rutas.py
    rutas publicadas y censadas : 798
      pasan                     : 798
      CAEN                      : 0
          PATRON                           72
          VACIA A PROPOSITO                3
          con contenido                    715

**EL TALLADO VA DE `223 / 125 / 98` A `232 / 128 / 104`, Y LAS TRES SUBIDAS TIENEN NOMBRE:** las
`3` talladas nuevas son **la tabla de frontera de `cap_05`** (`LL.4.b`), **la tabla de citas de
`LL.2.c`** y **la tabla `D.52` de `LL.5.d`**. **Y esa tercera la ancle a mano, y lo digo:** al
pegarla quedo enganchada al marcador de `.v50/sello_v49.txt`, que no era suyo, y **paso de
`PARCIAL` a `tallada celda a celda` en cuanto le puse su propio marcador**. Es el mismo enganche
que `KK.5.e` registro en la vuelta 49, de la familia de `d029`: **una tabla puede quedar declarada
por un marcador que no era suyo**, y la unica defensa es ponerle el suyo.

**EL CENSO VA DE `782` A `798`, `16` RUTAS NUEVAS**, todas `con contenido` (de `700` a `715`, mas
una de `vacia por protocolo`). **Cero caen.** Y lo que la vuelta 49 no supo decir, hoy lo digo con
su mecanismo medido por el auditor y no por mi: **los marcadores `TALLADO` no cuentan como ruta
porque no llevan comillas invertidas** (`48.6.a`), no porque vivan en bloques de codigo.

### LL.5.f. **`PASOS INVENTADOS POR CAPITULO`, Y ESTA VUELTA SI TIENE FILA** (`AUDITOR_FORJA.md` 8)

<!-- TALLADO: parcial salida=.v50/pasos_inventados.txt -->

    LOS DE ESTA VUELTA, cap_04, tanda de P41, P42 y P44
      preparar_respuestas_estandar_interrupciones_repetidas     6 pasos
      agrupar_interrupciones_subordinados_reuniones_regulares   5 pasos
      canalizar_interrupciones_cartel_hora_oficina              8 pasos
      numerador PUENTE                                          0
      denominador, pasos escritos hoy                          19
      porcentaje de cap_04 SOBRE LOS PASOS DE HOY            0.00 por ciento

    EL CAPITULO ENTERO, las 22 fichas de cap_04 en la bandeja
      fichas de cap_04                                         22
      pasos del capitulo entero                               156
      de ellos, escritos en esta vuelta                        19
      de ellos, escritos en las vueltas 46, 47 y 48           137
      numerador PUENTE del capitulo entero                       0
      porcentaje de cap_04 SOBRE EL CAPITULO ENTERO          0.00 por ciento

**DESGLOSADA POR CAPITULO Y NO COMO MEDIA, con su numerador y su denominador delante:**

| capitulo | pasos escritos HOY | PUENTE de hoy | por ciento de hoy | pasos del capitulo entero | PUENTE del capitulo | por ciento del capitulo |
|---|---:|---:|---:|---:|---:|---:|
| `cap_04` | `19` | `0` | **`0,00`** | `156` | `0` | **`0,00`** |
| `cap_01` a `cap_03` | `0` | `0` | sin fila: esta vuelta no los toca | | | |

**LOS `137` DEL CAPITULO ANTES DE HOY SON LOS QUE EL AUDITOR FIRMO EN LA `ACTA 48`**, contados por
el de las `19` fichas. **`137` mas mis `19` dan `156`, y `156` es lo que cuento yo hoy de las `22`
fichas:** la cifra del auditor y la mia cierran por suma, que es el unico contraste que puedo
ofrecer sin recontar su trabajo.

**Y LA FIDELIDAD DE MIS `19` NO LA CERTIFICA LA ADUANA Y LO DIGO** (`D.30`): los tres informes
salieron `0 CAERIA` **antes y despues de mi relectura**, exactamente como el lote 1. Lo que sostiene
el `0` PUENTE es **la tabla paso a paso contra su renglon** de `LL.2.e`, `LL.2.g` y `LL.2.i`, con
los `4` renglones del libro pegados en `LL.2.c`, **y los `6` puentes que declaro haber estado a
punto de escribir y no escribi.**

### LL.5.g. **LA LINEA DEL TRAMO, CON SU RELOJ, Y NO HUBO CORTE**

**LA UNIDAD DE ESTA VUELTA ES LA PASADA DE ADUANA**, como el encargo la definio en su techo.

<!-- TALLADO: script=.v50/coste.py salida=.v50/coste.txt -->

| pieza del turno | instrumento | corridas | segundos | por ciento del turno |
|---|---|---:|---:|---:|
| pasada de aduana de `P41` | `forja.py informe` | 1 | 639.0 | 43.0 |
| pasada de aduana de `P42` | `forja.py informe` | 1 | 335.0 | 22.5 |
| pasada de aduana de `P44` | `forja.py informe` | 1 | 410.0 | 27.6 |
| prueba de aceptacion al cierre | `tests/test_aceptacion.py` | 1 | 97.0 | 6.5 |
| las cuatro guardas restantes del cierre | `gate`, `guiones`, `tallado`, `censo` | 4 | 6.0 | 0.4 |
| **TOTAL MEDIDO CON RELOJ** | | **8** | **1487.0** | **100.0** |

<!-- TALLADO: parcial script=.v50/coste.py salida=.v50/coste.txt -->

    pasadas de aduana        : 3 de un techo de 3,  1384.0 s,  93.1 por ciento del turno
    media por pasada de aduana    : 461.3 s   (la cifra que la vuelta 51 tiene que usar, 47.5.c)
    estimada por el encargo       : 1017.3 s por pasada, o sea 3051.9 s las tres
    desvio de la estimacion       : -1667.9 s  (-54.7 por ciento)
    techo en minutos              : 1487.0 s medidos de un techo de 3420 s, o sea 24.8 min de 57.0

**LAS DOS MITADES DEL TECHO SE CUMPLEN Y NO HUBO CORTE:** `3` pasadas de `3`, y `24,8` minutos
medidos de `57`. **No cerre corto en ningun candidato**, asi que la linea del tramo no tiene corte
que declarar: **`cap_04` sale entero, `22` de `22`.**

**Y LA CIFRA QUE LA VUELTA 51 TIENE QUE USAR, por `47.5.c`, que manda recalcularla y no
arrastrarla: `461,3` s por pasada.** Es **menos de la mitad** de los `1.017,3` con los que el
encargo la estimo, y **el desvio es a mi favor y aun asi lo escribo, porque un techo que sobra el
`54,7` por ciento es un techo mal calculado igual que uno que se queda corto.** El motivo que puedo
medir: **las cuatro pasadas de la vuelta 49 tocaban fichas con vecindad grande** (`d032` sola costo
`1.479,4` s), y mis tres de hoy son candidatos nuevos con `2`, `7` y `3` vecinos. **Lo que la media
de una vuelta mide no es el coste del instrumento: es el coste de las fichas de esa vuelta.**

### LL.5.h. **EL CREDITO, LA DEUDA Y EL TABLERO: LOS TRES LEIDOS, UNO SOLO RECOMPUTADO POR MI**

<!-- TALLADO: parcial salida=.v50/credito_cierre.txt -->

    $ python forja.py credito
      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            2 de 3     ACTA 48
      CIFRA PUBLICADA    0 de 2     ACTA 48
      CLASE              0 de 2     ACTA 48
      DATO MOVIDO        0 de 2     ACTA 48
      REPORTE            0 de 3     ACTA 48

      CREDITO ENTERO: ninguna especie en su tope.

**LEIDO Y NO ANOTADO: esa sede no es mia** (`EXTRACTOR.md` 14), y las cinco rachas cierran donde
abrieron porque **nadie las mueve dentro de la vuelta: las mueve el acta siguiente.**

<!-- TALLADO: parcial salida=.v50/deuda_cierre.txt -->

    $ python scripts/deuda.py | head -3
    DEUDA DE LA LINEA (D.55): la deuda no bloquea la produccion
      registro: docs/loop/DEUDA.jsonl
      pendientes: 15    pagadas: 13

**DE `17` A `15`, QUE ES LO QUE EL ENCARGO PEDIA**, y las dos pagadas llevan su como escrito dentro
del propio registro, con sus ficheros de instrumento citados.

**LAS `15` QUE QUEDAN ABIERTAS, IMPRESAS DEL INSTRUMENTO Y NO TECLEADAS POR MI**, que es el remedio
mecanico que me llevo de la fila `h` de `48.5.b`:

<!-- TALLADO: parcial salida=.v50/deuda_pendientes.txt -->

    id     vuelta  especie            que
    --------------------------------------------------------------------------------------------
    d005   grove v2 relevo de grove    De los 15 candidatos de cap_03 de grove, su aduana e
    d006   41      relectura          cap_13 entero esta en 4 de 212, el 1,89 por ciento,
    d007   41      doctrina           La cola de doctrina queda congelada en 11 preguntas
    d009   42      deuda              scripts/tabla_de_cierre.py mide la tabla de cierre c
    d011   43      deuda              TODO TECHO QUE EL AUDITOR ESCRIBA LLEVA SU MITAD EN
    d012   43      deuda              SEGUNDO EJEMPLAR MEDIDO de la pregunta 9 de la cola
    d020   44      maquinaria         src/arista.py linea 182 teclea veredicto CONTINUA en
    d022   44      maquinaria         scripts/tabla_de_cierre.py localiza la tabla por la
    d024   45      aduana             LOS 7 CANDIDATOS DE cap_02 DE grove NO TIENEN INFORM
    d028   46      maquinaria         src/tablero.py:214 publica en capitulos_minados los
    d029   46      maquinaria         El tallado de D.41 casa las filas por su primera cel
    d030   47      maquinaria         scripts/tabla_de_cierre.py --escribir escribe SIEMPR
    d031   47      aduana             RETOCAR UNA LINEA DE UN resumen_teorico EN CUARENTEN
    d033   48      maquinaria         test_e_guion_largo_rompe_el_hook salio ROJO una vez
    d037   49      maquinaria         LA PUERTA DE D.39 NO TIENE CASO ROJO AUTOMATICO: gre

**QUINCE, IMPRESAS, Y NINGUNA SE ME QUEDA FUERA DE LA LISTA PORQUE LA LISTA NO LA ESCRIBO YO.** Y
su reparto tampoco lo cuento a ojo:

<!-- TALLADO: parcial salida=.v50/deuda_reparto.txt -->

    $ reparto por especie de las 15 pendientes, contado de .v50/deuda_pendientes.txt
      maquinaria        7   d020 d022 d028 d029 d030 d033 d037
      deuda             3   d009 d011 d012
      aduana            2   d024 d031
      relevo de grove   1   d005
      relectura         1   d006
      doctrina          1   d007
      TOTAL            15

**`10` DE LAS `15` ESTAN FUERA DE MI ALCANCE POR `D.45` Y LA MORATORIA**, que son las `7` de
`maquinaria` mas las `3` de `deuda` de instrumento; **`2` son doctrina congelada** (`d006` y
`d007`, por `D.56`); y **`3` tienen su tramo escrito y no vence hoy** (`d005`, `d024` y `d031`).
**Que queden abiertas no es descuido: `D.55` las agenda, no las perdona.**

**EL TABLERO lo leo y no lo escribo**, y su frase de `LL.2.a` sigue siendo la que no obedezco. **La
cola de doctrina sigue congelada en `11`** y **no abro la doce**, aunque `LL.2.h` traiga una
observacion medida que en otra vuelta habria llamado a la puerta.

### LL.5.i. **EN QUE SE FUE EL TURNO** (`D.55`)

**ESTA VUELTA ES DE PRODUCCION Y LO DIGO CON ESAS PALABRAS:** `scripts/deuda.py --clase 50` la
llama `INSERCION` (`LL.0.c`) y **esta vuelta no inserta**, porque quien decide eso es `D.39` y
`LL.0.a` la mide cerrada. **Lo que esta vuelta produce son los tres ultimos nodos de `cap_04`**,
mas dos deudas pagadas y la frontera del capitulo siguiente.

**NO INVENTO UN USD: este repo no tiene instrumento que lo mida**, y el turno no llega a `25`
minutos de reloj medido, muy por debajo del umbral de `10` USD que `D.55` pone para exigir el
desglose. **Lo doy igual, medido de mis relojes, en la tabla de `LL.5.g`:** **el `93,1` por ciento
del turno medido se fue en tres pasadas de aduana**, y las tres midieron **candidatos nuevos**, que
es donde `KK.2.d` decia que la medida si cuenta. **Cero segundos gastados en volver a comparar una
correccion de prosa**, que es exactamente lo que la adjudicacion `3.c` del encargo compro.

### LL.5.j. **LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO** (`EXTRACTOR.md` 8)

**Marcados a ciegas, antes de la relectura del auditor**, y ordenados por lo que me parece mas
facil que caiga:

| # | donde | el discutible, en una linea |
|---:|---|---|
| 1 | `LL.2.i`, el paso `3` de `P44` con la hora del cartel dentro | **traslado el `2:00` del cartel dentro de un paso**, y un lector estricto dira que es un dato de un ejemplo metido en un paso, la senial barata de manual 3.5. **Mi motivo: el libro no presenta ese cartel como caso de nadie**, lo escribe entre comillas y en presente, asi que reescribirlo seria puente. Y dejo el entregable sin ningun dato del cartel |
| 2 | las tres fichas, la arista `1` declarada `D.29` y no `D.37` | **etiqueto como `D.29` la misma relacion que la ficha de `P39` etiqueto `D.37`**, con la misma cabeza. Un lector estricto dira que dos fichas del mismo capitulo no pueden etiquetar distinto la misma arista. **Mi motivo esta escrito dentro de las tres fichas**, y **no toco la de `P39`** porque no es mi encargo y `D.56` congela la doctrina |
| 3 | `LL.2.f`, mi lectura contra la banda alta | **`0,423` de senial `1` esta en la banda donde el catalogo tiene `325` gemelos y CERO ajenos**, y yo digo que no es gemelo. **Es la lectura contra la cifra**, y `EXTRACTOR.md` 11 dice que las seniales ordenan y no deciden, pero **quien lea solo la banda tiene aqui su caso** |
| 4 | `LL.2.i`, los pasos `7` y `8` de `P44` desde L323 | **me llevo el parrafo de cierre del capitulo entero a un nodo**, y un lector estricto dira que un cierre de capitulo es POSTURA. **Mi motivo: la frontera de `HH.2.c` asigna L321 a L323 a esta pieza y a ninguna otra**, asi que si no fueran de aqui L323 quedaria huerfana |
| 5 | `LL.2.g`, el paso `4` de `P42`, de cinco palabras | **lo dejo tal cual sabiendo que levanta las tres vecindades de senial `3` de la tanda.** Un lector estricto dira que un paso de cinco palabras no es un paso. **Mi motivo: el libro escribe `If such meetings are held regularly` y engordarlo para complacer a un umbral seria escribir yo lo que el libro no escribe** |
| 6 | `LL.4.b`, el cero de `P4` de `cap_05` | **doy cero nodos a un tramo que dice DOS clases y las nombra**, que es la forma de una cabeza de serie. **Mi motivo: lo que pone bajo cada nombre son FINES** y `9.1` restriccion `1` los deja fuera, **y la cabeza de verdad es `P7`**. Es un pronostico, no una extraccion, asi que si cae cuesta poco |
| 7 | `LL.2.h`, mi lectura de por que sube la senial `1` | **afirmo que lo que levanta las vecindades es mi forma de redactar el paso de encuadre**, y lo deduzco de que `4` de `6` levantamientos son `paso 1 contra paso 1`. **Es una inferencia sobre `6` casos, y la marco como tal**: no he leido el codigo de la senial |

**LO QUE LOS SIETE TIENEN EN COMUN:** **ninguno es una cifra.** Las cifras de esta vuelta salen
todas de un instrumento pegado; **los siete son decisiones de lectura mias.** Y **el `2` y el `7`
son los dos que mas me costaria defender**, por motivos opuestos: el `2` porque me separa de una
ficha ya escrita, y el `7` porque es la clase de frase que me tumbo en la vuelta 49, **un mecanismo
inferido detras de una cifra cierta**.

### LL.5.k. **LO QUE PROPONGO Y NO ADJUDICO** (`EXTRACTOR.md` 14)

| # | propuesta | de donde sale |
|---:|---|---|
| 1 | **que la media por pasada de aduana se publique con el numero de vecinos al lado**, y no sola | `LL.5.g`: `461,3` contra `1.017,3` en dos vueltas seguidas. **La media mide las fichas de la vuelta, no el instrumento**, y un techo construido sobre ella se equivoca en las dos direcciones |
| 2 | **que la etiqueta de arista entre una cabeza de `D.37` y un nodo que solo es MEDIO de una de sus vias se escriba en el banco** | el discutible `2`: hoy hay dos fichas del mismo capitulo que la etiquetan distinto, **y las dos tienen su motivo escrito**. Es doctrina y `D.56` la congela: **la registro, no la abro** |
| 3 | **que `cap_05` se mine en DOS vueltas desde el encargo**, y no que se corte sobre la marcha | `LL.4.c`: `26` nodos contra un techo de `15` esta medido **antes** de empezar, cosa que `cap_04` no tuvo. **Cortar declarandolo es correcto; planificar el corte es mas barato** |
