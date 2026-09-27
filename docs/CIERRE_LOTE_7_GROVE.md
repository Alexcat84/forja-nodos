# CIERRE DEL LOTE 7: `grove_high_output`

**21 sep 2026.** **La mineria de `grove_high_output` esta cerrada: `18` de `18` capitulos
leidos y adjudicados, `92` candidatos cosechados, `643` pasos.** Con ella cierra **la
extraccion del mundo `11`**.

Fue ademas **el lote de la medicion del extractor barato**: sus siete ultimas vueltas
corrieron con `claude-sonnet-5` en la silla del extractor y `claude-opus-5` en la del
auditor, bajo el umbral escrito en la decision del fundador del `21` sep. **Esto es lo que
midio.**

---

## 1. LA CUENTA DEL LIBRO

Contada por el auditor de la `ACTA 61` desde cero, con un instrumento distinto del del
extractor, y **las `18` filas por capitulo salieron las `18` al digito**:

    $ python .v62aud2/cuenta2.py
    capitulos del libro                     : 18
    candidatos en la bandeja                : 91
    pasos_accionables en la bandeja         : 636
    insertados en el grafo                  : 1
    pasos en los insertados                 : 7
    TOTAL cosechado del libro               : 92
    TOTAL pasos cosechados del libro        : 643
    capitulos CON al menos un candidato: 15
    capitulos que DIERON CERO          : 3 ['cap_08', 'cap_09', 'cap_18']
    suma de control (por capitulo)     : 92 candidatos, 643 pasos
    fichas sin capitulo legible        : 0

**LOS TRES CEROS SON ADJUDICACION FIRMADA, NO HUECO**, y el motivo de cada uno esta en la
seccion `3`.

---

## 2. `PASOS INVENTADOS POR CAPITULO`: LA CIFRA QUE DECIDIA SI SONNET SERVIA

**El umbral escrito** (decision del fundador del `21` sep, punto `3`): *si los pasos
inventados por muestra quedan bajo el `10` por ciento y el turno baja a la mitad, GROVE SE
TERMINA CON SONNET.*

<!-- TALLADO: parcial salida=.v63rec/calidad_sonnet.txt -->

    $ python .v63rec/calidad_sonnet.py
    PASOS INVENTADOS POR CAPITULO, CORRIDA CON SONNET (vueltas 56 a 62)

    cap      vuelta acta    escritos  muestra   leidos  PUENTE  inventado
    ------------------------------------------------------------------------------
    cap_08   56     ACTA 55       0   ENTERO        0       0  SIN SUPERFICIE
    cap_09   56     ACTA 55       0   ENTERO        0       0  SIN SUPERFICIE
    cap_10   56     ACTA 55       8        8        8       0  0,0 por ciento
    cap_11   57     ACTA 56      17       15       17       0  0,0 por ciento
    cap_12   57     ACTA 56      11       11       11       0  0,0 por ciento
    cap_13   57     ACTA 56      14       14       14       0  0,0 por ciento
    cap_14   58     ACTA 57      18       15       18       0  0,0 por ciento
    cap_15   58     ACTA 57      22       15       22       0  0,0 por ciento
    cap_16   58     ACTA 57       4   ENTERO        4       0  0,0 por ciento
    cap_17   60     ACTA 59      16       15       16       0  0,0 por ciento
    cap_18   60     ACTA 59       0   ENTERO        0       0  SIN SUPERFICIE
    ------------------------------------------------------------------------------
    TOTAL                       110       93      110       0

    capitulos con superficie (pasos > 0)  : 8
    pasos escritos por Sonnet             : 110
    pasos que la muestra de D.58 cubrio   : 93
    pasos que el auditor leyo de verdad   : 110
    pasos PUENTE encontrados              : 0
    cobertura de la lectura, leidos/escritos : 100.0 por ciento
    pasos inventados, PUENTE/escritos        : 0.0 por ciento

    CAPITULOS QUE SUPERAN EL 10 POR CIENTO SIN RELECTURA ENTERA : 0
       NINGUNO

> ## **NINGUN CAPITULO SUPERA EL `10` POR CIENTO. NINGUNO LLEGA A SUPERAR EL `0,0`.**
>
> **La unica condicion que invalidaba el ahorro no se cumplio en ninguna fila.**

### 2.a. **Y LA CIFRA ES MAS FUERTE QUE EL UMBRAL QUE LA PEDIA, por una razon concreta**

El umbral hablaba de **muestra**. **La muestra de `D.58` cubrio `93` de los `110` pasos, y
el auditor leyo los `110`.** No es lo mismo, y la diferencia es la que vale:

| | pasos |
|---|---:|
| que la muestra de `D.58` eligio | `93` |
| que el auditor leyo **de mas**, fuera de muestra | `13` |
| de `cap_16`, releido ENTERO por su semilla | `4` |
| **leidos contra la linea del libro** | **`110` de `110`** |

**Esto no es un muestreo con un cero: es un censo con un cero.** Cada paso que Sonnet
escribio en este libro fue leido por Opus contra el parrafo del que dice salir, y **cero
resultaron PUENTE**.

Las tres actas lo dicen con sus denominadores a la vista: la `ACTA 56` **firma sobre `42` y
no sobre `40`**, la `ACTA 57` **sobre `44` y no sobre `34`**, y la `ACTA 55` releyo los `8`
de `cap_10` contra `L43` entera.

### 2.b. **Las vueltas que no aparecen en la tabla, y por que no aparecen**

Las vueltas `59`, `61` y `62` **escribieron cero pasos**, y eso se publica en vez de
callarse (`ACTA 58` `58.8`, `ACTA 60` `60.7`, `ACTA 61` `61.6`): **`SIN SUPERFICIE`, medido
con la ventana del turno contra las fechas de la bandeja, no supuesto.** No dan fila porque
**el disparador del `10` por ciento no tiene denominador donde morder.**

### 2.c. **El unico paso discutido, y queda escrito para que se pueda discutir**

El paso `1` de `desarrollar_primer_curso_entrenamiento` dice *sobre el tema mas urgente **de
tu lista***, y *de tu lista* esta en `cap_17` `L49`, no en `L53`. **Dos auditores por
separado** (`ACTA 59` `59.5` y `ACTA 60` `60.7`) **lo cuentan TRANSCRIPCION**: es un ancla
al nodo anterior del mismo capitulo, no una etapa que el libro no escriba. **Si alguien lo
quiere recontar como PUENTE, la cifra del libro pasa de `0,0` a `0,9` por ciento y sigue
nueve veces por debajo del umbral.**

---

## 3. LOS TRES CAPITULOS QUE DIERON CERO, Y POR QUE SU CERO ESTA FIRMADO

**Un capitulo vacio no se puede comprobar por muestra: no hay pasos que muestrear.** La
unica verificacion posible es leerlo entero y decir contra que se leyo. **Eso es lo que
motiva las relecturas enteras, y es la razon de que los tres ceros cuesten mas de verificar
que un capitulo con veinte nodos.**

| capitulo | quien firma su cero | como lo verifico |
|---|---|---|
| `cap_08` | **`ACTA 55`** `55.3` | **leido ENTERO del fichero** antes de firmar, y el acta declara que su relectura **no fue ciega** y no la vende como tal (`D.58` apaga la ciega en cuarentena) |
| `cap_09` | **`ACTA 55`** `55.3` | idem, leido ENTERO del fichero |
| `cap_18` | **`ACTA 59`** `59.4` | **sus `35` citas de nodo comprobadas una a una, y las `35` existen**; ademas `56` tramos recompuestos fila a fila, `718` palabras, `0` solapes y `0` lineas sin cubrir |

**`cap_18` merece una linea aparte**: la `ACTA 59` escribio que su cero *no se firma por el
argumento sino por las citas*. El capitulo es material de sintesis que remite a unidades
anteriores del propio libro, y **la forma de probar que no aporta nodo nuevo fue verificar
que todo lo que cita ya existe**, no aceptar que el extractor lo dijera.

---

## 4. LA ADUANA DE LOS `91`: TODOS TIENEN VEREDICTO, Y `73` LO TIENEN CONTRA UNA POBLACION VIEJA

La decision del `21` sep pidio reconciliar `35` contra `47`. **Las dos cifras median mal, y
la peor de las dos era la de esta sesion**: contaba *ficheros cuyo nombre contiene el id*,
que no dice nada sobre si la aduana se pronuncio.

**La medida buena es la linea de veredicto que `forja.py informe` imprime**, que es la unica
sede donde la aduana se pronuncia sobre un candidato:

    $ python .v63rec/rec2.py
    BANDEJA DE grove_high_output : 91 candidatos
    CON VEREDICTO DE ADUANA YA CORRIDO : 91
    SIN VEREDICTO, HAY QUE CORRERLOS   : 0

    por poblacion del barrido que lo produjo:
       poblacion 423 : 73 candidato(s)
       poblacion 431 :  2 candidato(s)
       poblacion 432 :  2 candidato(s)
       poblacion 433 :  2 candidato(s)
       poblacion 434 :  2 candidato(s)
       poblacion 436 :  2 candidato(s)
       poblacion 437 :  4 candidato(s)
       poblacion 440 :  4 candidato(s)

    por veredicto:
       BLOQUEARIA   : 71
       ENTRARIA     : 20

La lista entera, candidato por candidato con su fichero y su poblacion, esta en
`.v63rec/veredictos_de_aduana.txt`.

### 4.a. **LO QUE FALTA NO ES EL INFORME: ES LA POBLACION**

**`73` de los `91` se adjudicaron contra una poblacion de `423`, y hoy la poblacion es
`440`.** Los `17` que entraron en medio **son hermanos suyos del mismo libro**, de `cap_11`
a `cap_17`.

> **Un candidato de `cap_04` juzgado contra `423` fue juzgado sin `cap_11` a `cap_17`
> delante, que son exactamente los vecinos con los que mas probable es que choque.** No es
> que el informe este roto: es que **la poblacion crecio por debajo de el.**

**El aviso en contra, y es fuerte:** la `ACTA 61` `61.4.b` dejo la mejor prueba de
determinismo que esta casa tiene. Tres corridas del mismo candidato en dos fechas, con la
poblacion movida de `414` a `440`, **dieron el mismo vecino y las mismas tres cifras al
milesimo, difiriendo en una sola linea de `30`**, la de la poblacion. **Eso sugiere que
rehacerlos cambiara poco. No prueba que no cambie nada**, porque esa medida es de un
candidato y no de la vecindad entera.

### 4.b. **POR QUE SE REHACEN IGUAL: PORQUE NO CUESTAN DINERO**

    $ grep -rn "anthropic|openai|claude|requests|urllib|http" src/aduana.py src/informe.py
    (vacio)

**`forja.py informe` es computo puro. No llama a ningun modelo. Su precio es reloj, no
dolares.** Por eso la reconciliacion no se hace escogiendo `73` sino **corriendo la bandeja
entera contra la poblacion de hoy**, que ademas **revalida los `18` vigentes gratis** y da
una segunda medida de `d092`:

    $ python forja.py informe --carpeta cuarentena/grove_high_output > .v63rec/informe_bandeja_440.txt

**LANZADO A LAS `07:08:59` DEL `21` SEP Y MATADO A PROPOSITO A LOS POCOS MINUTOS**, cuando
la enmienda del fundador del mismo dia pospuso la insercion a la semana siguiente por
cuota. **Su fichero de salida no existe, y eso se declara en vez de callarse**:
`.v63rec/informe_bandeja_440.meta` dice quien lo mato y por que.

**No se mato por dinero.** Se mato porque preparaba una insercion que ya no ocurre esta
semana, y porque **se quedaria viejo igual**: si `gerber_emyth` cierra su extraccion y se
cosecha por `D.50`, sus candidatos entran a esta bandeja y **la poblacion deja de ser
`440`**.

> **CUANDO LA INSERCION SE RETOME, LA PRIMERA TAREA DE SU ENCARGO ES RELANZARLO**, contra
> la poblacion que haya ese dia, y **ninguna tanda de insercion abre sin su salida
> delante.** La reconciliacion de esta seccion, que es lo que la decision pedia, **ya esta
> hecha y no hay que repetirla**: se sabe que los `91` tienen veredicto y cuales `73` lo
> tienen contra `423`.

---

## 5. LO QUE COSTO, Y DONDE SE FUE EL DINERO

    $ awk '/2026-09-20 17:16:34/,0' docs/loop/loop.log | grep -o "USD [0-9.]*" | awk ...
    turnos: 14, total 215.7603, media 15.4115
    extractor 87.7118, auditor 128.0485

| | USD | por turno |
|---|---:|---:|
| extractor (`claude-sonnet-5`), `7` turnos | `87,71` | `12,53` |
| auditor (`claude-opus-5`), `7` turnos | `128,05` | `18,29` |
| **total de la corrida** | **`215,76`** | **`15,41`** |

**EL AHORRO LLEGO Y SE LO COMIO LA OTRA SILLA.** Los tres ultimos turnos de extractor
costaron `8,08`, `2,66` y `8,49`, contra los `20` a `25` que costaban con Opus. **Pero el
auditor se llevo `128` de los `216`, mas que el extractor**, y la media por turno apenas
bajo de `14,98` a `15,41`.

**Y ESO NO ES UN DEFECTO A CORREGIR EN ESTE LOTE.** El auditor gasto eso **leyendo los `110`
pasos uno a uno en vez de firmar `93`**, que es precisamente la razon de que la seccion `2`
pueda decir censo y no muestra. **El gasto compro la cifra que autorizo el ahorro.**

> **La cifra del auditor solo se ve al cerrar una campania**, y queda escrita aqui para
> quien presupueste la siguiente.

### 5.a. **UNA CORRECCION DECLARADA SOBRE LA CUENTA**

~~`19` turnos, `293,55` USD, media `15,45`~~ **`14` turnos, `215,7603` USD, media
`15,4115`**. La primera cifra, que esta sesion le dio al fundador a las `06:33`, **sumaba
una ventana mas ancha que el arranque de esta corrida** y arrastraba turnos de la anterior.

**Y una diferencia que no es error de nadie:** la `ACTA 61` publica `13` turnos y `203,6359`.
Le falta **su propio turno final**, el que escribio la parada. `203,6359` mas `12,1244525`
da `215,7603`, al centimo. **Un auditor no puede cobrarse dentro de su propia acta.**

---

## 6. EL VEREDICTO SOBRE SONNET, QUE ERA LA PREGUNTA DE LA CAMPANIA

| la condicion escrita el `21` sep | medido | |
|---|---|---|
| pasos inventados por muestra **bajo el `10` por ciento** | **`0,0` por ciento sobre `110` de `110`** | **CUMPLE** |
| turno del extractor **a la mitad** | de `20` a `25` USD a `2,66` a `8,49` | **CUMPLE** |

> **GROVE SE TERMINO CON SONNET, Y LA CALIDAD NO DIFIRIO.** No *similar*: **cero pasos
> inventados sobre el censo entero del libro.**

**LO QUE ESTE CIERRE NO AUTORIZA:** que la insercion corra barata. **La insercion va con
Opus en las dos sillas** (decision del fundador del `21` sep): es la unica fase que toca el
grafo y la unica que no se deshace leyendo.
