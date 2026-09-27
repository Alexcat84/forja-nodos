
## 48.6. LAS CAIDAS DEL EXTRACTOR, CON SU SEDE Y SU CUENTA

### 48.6.a. **UNA, Y ES LA QUE EL MISMO MARCO: EL MECANISMO DEL CENSO** (`KK.5.e`, punto `1`)

**Lo que publico:** *el censo solo suma `2` rutas, porque **la unidad de `D.42` es la CELDA** y la
mayoria de mis citas viven en bloques de codigo, no en celdas.*

    $ python .v49aud/26_discutibles.py
    marcador TALLADO tal cual                unidades 1  rutas extraidas ninguna
    marcador TALLADO con comillas            unidades 1  rutas extraidas [('.v49/coste.txt', 'linea', False)]
    linea de bloque con comando              unidades 1  rutas extraidas ninguna
    linea de bloque, ruta sola en comillas   unidades 1  rutas extraidas [('.v49/coste.txt', 'linea', True)]
    celda de tabla de donde sale             unidades 3  rutas extraidas [('.v49/coste.txt', 'celda 3', True)]

Ese bloque pasa cinco formas de cita por `unidades_de`, `parece_ruta` y `es_sede` de
`scripts/censar_rutas.py`, e imprime que ruta extrae cada una y si la toma como sede.

`LECTURA`: **una linea de bloque SI es una unidad del censo y SI puede ser sede**, como muestra la
cuarta fila. **Lo que impide contar sus treinta marcadores es otra cosa: el marcador `TALLADO` no
lleva comillas invertidas**, y `EN_COMILLAS` solo extrae lo que va entre ellas, **asi que su ruta
no llega a extraerse nunca.** La cifra `2` es cierta; **el porque es falso.**

**SEDE Y CUENTA:** vive en **prosa de acompanamiento** de `KK.5.e`, no en tabla ni en cabecera ni
en conclusion, **y el propio reporte la marco como inferencia** en su fila `5` de discutibles
(*lo deduzco de que la cifra no se movio, no de haber leido `censar_rutas.py`*). Por `5.2`,
**REGISTRA Y NO ACUMULA.**

**LO QUE SI HIZO BIEN, y no es un consuelo sino la diferencia entre esta caida y otra:** marco el
sitio antes de saber si acertaba y dijo con sus palabras que era una inferencia. **Una inferencia
declarada que resulta falsa cuesta una linea de acta; una inferencia escondida dentro de la frase
de una cifra viaja de acta en acta.**

### 48.6.b. **LO QUE COMPROBE ANTES DE DECIR QUE NO HAY MAS**

| especie | esta tanda | como lo comprobe |
|---|---|---|
| **`CLASE`** | **NINGUNA, y no es opinion** | `bitacora/VEREDICTOS.jsonl` sigue en `740` y `config/pares_mutuos.jsonl` en `1`: **la vuelta no escribio ni un veredicto**, asi que no hay veredicto que poder poner mal |
| **`DATO MOVIDO`** | **NINGUNA** | `git diff --stat 50a9d83..HEAD` sobre `dataset/`, `bitacora/`, `config/`, `censos/`, `esquema/`, `src/`, `scripts/`, `tests/`, `hooks/`, `forja.py` y el banco **no imprime un solo fichero** |
| **`CIFRA PUBLICADA`** | **NINGUNA** | las unicas sedes duraderas que la vuelta toco son dos fichas de `cuarentena/`, que `d027` adjudico que **no son sede de `5.2`**; y sus dos correcciones las verifique renglon a renglon contra el libro en mi fase ciega |
| **`REPORTE`** | **UNA, y NO acumula** | `48.6.a`. Recompute ademas las veinticuatro filas de `48.2.b` y **ninguna otra se movio** |

**LA TANDA ES LIMPIA PARA LA ESPECIE QUE `REPORTE` ACUMULA**, asi que por la correccion declarada
del 16 sep 2026 en `5.4` (*`LIMPIA` significa sin caidas de la especie que esa racha acumula, y
una tanda con caidas solo de las que no acumulan reinicia la racha igual*) **`REPORTE` baja de
`1 de 3` a `0`.** **No es un indulto mio: es la letra**, y la caida queda escrita arriba con su
nombre, que es lo que `5.4` dice que la hace util.

## 48.7. LA MUESTRA PINEADA DE LOS SANOS (`AUDITOR_FORJA.md` 7)

    $ git diff --stat 50a9d83..HEAD -- bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
    (sin salida)
    $ wc -l bitacora/VEREDICTOS.jsonl
    740 bitacora/VEREDICTOS.jsonl

Ese bloque mide si la vuelta escribio algun veredicto y cuantos hay en el registro.

`LECTURA`: **la tanda tiene `0` veredictos `SANO`, porque tiene `0` veredictos.** La seccion `7`
manda releerlos todos mientras sean menos de tres: **releo los cero y publico la cifra**, que es
lo que la regla pide. **No invento una muestra donde no hay poblacion**, y con `0` de `0` **no hay
tasa ni banda que publicar**: una tasa sobre cero casos no es un cero, es una celda que no existe.
**Semilla: no hace falta, porque no hay nada que sortear**, y decirlo es mas honesto que escribir
un numero al lado de una muestra vacia.

## 48.8. `PASOS INVENTADOS POR CAPITULO` (`AUDITOR_FORJA.md` 8). **UNA FILA POR CAPITULO**

    $ python .v49aud/24_pasos_por_capitulo.py
    cap_02    7 fichas    50 pasos
    cap_03   15 fichas   121 pasos
    cap_04   19 fichas   137 pasos
    contra HEAD~1  : 19 fichas con los MISMOS pasos, 0 distintas, 0 ausentes
    contra HEAD    : 19 fichas con los MISMOS pasos, 0 distintas, 0 ausentes

Ese bloque cuenta los pasos de cada ficha de la bandeja de `grove_high_output`, repartidos por el
`cap_NN.md` que la propia ficha declara, y compara paso a paso las `19` de `cap_04` contra el
commit anterior y contra el de la vuelta.

| capitulo | pasos escritos EN ESTA VUELTA | `PUENTE` | por ciento | el denominador vivo, contado hoy por mi |
|---|---:|---:|---|---|
| `cap_02` | **`0`** | **`0`** | **sin fila**: `0` entre `0` | `50` pasos en `7` fichas |
| `cap_03` | **`0`** | **`0`** | **sin fila**: `0` entre `0` | `121` pasos en `15` fichas |
| `cap_04` | **`0`** | **`0`** | **sin fila**: `0` entre `0` | `137` pasos en `19` fichas |
| **total del lote 7** | **`0`** | **`0`** | **sin fila** | `308` pasos en `41` fichas |

**POR QUE NO HAY PORCENTAJE, Y POR QUE NO ES UN CERO:** una vuelta de saneamiento **no escribe un
solo paso**, asi que el numerador y el denominador son los dos cero. **Mi propio encargo lo dijo
por adelantado** y la vuelta lo cumplio con su motivo escrito (`KK.5.g`), **que es justo lo que
`8.3` punto `3` pide que no falte.**

**Y LO QUE SI FIRMO, PORQUE LO MEDI Y NO LO COPIE:** **`cap_04` sigue en `0` `PUENTE` de `137`
pasos.** La razon por la que no hace falta releer los `137` contra su renglon es que **ninguno se
movio**: las `19` fichas conservan sus pasos identicos contra `HEAD~1` y contra `HEAD`, medido por
diferencia, y la unica que cambio por dentro cambio su `resumen_teorico` **y ni un paso**.

**EL VOLUMEN DEL LOTE SIGUIENTE NO SE MUEVE** (`8.1`): sin fila no hay comparacion que hacer, y la
ultima medida viva sigue siendo la de la vuelta 48. **La vuelta 50 corre al escalon que `47.5.d`
ya fijo**: cerrar `cap_04` con `P41`, `P42` y `P44`.

## 48.9. MIS CAIDAS PROPIAS, CON MI NOMBRE. **DOS, Y LAS DOS DE LA MISMA FAMILIA**

### 48.9.a. **Mi apertura sellada publica `9` donde su propio instrumento da `12`**

    $ python .v49aud/17_superlativos.py      (MI instrumento, corrido HOY sobre la pagina sellada)
    SUPERLATIVOS, que es lo que el remedio obliga a contestar: 12 golpes en mi prosa, 16 lineas sangradas descartadas
       ...
       linea 655  [superlativo con nombre en medio] el grafo mas
       linea 656  [superlativo con nombre en medio] la ficha declara de mas
       linea 684  [unicidad                  ] unico          ...rase es cierta:** eso es lo unico que una maquina no puede...

    AFIRMACIONES UNIVERSALES, que no las pide el remedio y las barro igual: 11 golpes en mi prosa
       ...
       linea 785  [universal afirmativa      ] todos          ...s de esta pagina se lista a todos menos a si mismo**...

Ese bloque corre **mi propio instrumento del remedio** sobre la apertura tal como quedo sellada, y
su cabecera imprime la cuenta de golpes.

`LECTURA`: **mi pagina publica `9` y `10`; el mismo instrumento sobre el mismo fichero da hoy `12`
y `11`.** La causa es mia y es de las de siempre: **lo corri antes de escribir mis secciones `14` y
`15`, y despues segui escribiendo.** De los tres golpes de mas, **dos son mi propia tabla de
contestaciones repitiendo frases ya contestadas** (lineas `655` y `656`), **pero el de la linea
`684` es un superlativo nuevo y sin contestar**: *eso es lo unico que una maquina no puede hacer
aqui*, **sin lista de lo que una maquina si puede hacer.** Y `unico` **es literalmente uno de los
cuatro patrones que el `REMEDIO 1` de la `ACTA 46` nombra por su nombre**.

**ES `CIFRA PUBLICADA PROPIA`** (`D.38.2`: *una cifra falsa en tu acta o en tu apertura sellada*):
el `9` no describe la pagina que sella. **Y es tambien la sustancia del `REMEDIO 1` rota**, que es
la otra especie de mi racha. **Las dos viven en la misma racha y la suben una sola vez**, porque
una racha cuenta tandas y no caidas.

**LO QUE NO ME ABSUELVE, Y LO DIGO YO:** la letra del `HEREDADO 1` pide pegar la salida, y la
pegue. **Pero el remedio existe para que ningun superlativo mio quede sin lista, y uno quedo.**
Cumplir la forma de un remedio y romperle la sustancia es exactamente lo que le acabo de cargar al
extractor en `48.6.a`, y no me lo puedo cobrar en un sitio y perdonar en el otro.

### 48.9.b. **Mi deuda `d031` cita una linea que no es de la senial que dice**

    $ grep '"d031"' docs/loop/DEUDA.jsonl      (el trozo que lo dice)
    ... el resumen_teorico alimenta la senial 1 (src/aduana.py linea 315) ...
    $ awk 'NR>=314 && NR<=315' src/aduana.py
        cuerpo_candidato = comun.normalizar_texto(
            "%s. %s" % (candidato.get("titulo") or "", candidato.get("resumen_teorico") or ""))

Ese bloque imprime lo que escribi en `d031` y lo que hay en la linea `315` de `src/aduana.py`.

`LECTURA`: **la linea `315` es cuerpo de `senal_paso_contra_nodo`, que es la senial `3` y empieza
en la `304`** (`48.2.c`). La senial `1` empieza en la `278`. **La sustancia de `d031` se sostiene y
es incluso mas ancha de lo que escribi** (el `resumen_teorico` alimenta la `1` **y** la `3`),
**pero la linea que publique como prueba de la `1` no es de la `1`.** Sede `docs/loop/DEUDA.jsonl`,
que es `docs/`, y por tanto sede de `5.2`. **La cita es mia y el fallo es mio.**

**Y LA AGRAVA que el extractor, en esta misma vuelta, cito la `278` CORRECTAMENTE dentro de la
ficha de `d027`.** El la tenia bien y yo la tenia mal.

**CORRECCION DECLARADA, SIN BORRAR**, anotada en el mismo registro con su linea nueva y su cita a
esta seccion.

### 48.9.c. **LO QUE COMPROBE ANTES DE DECIR QUE NO HAY MAS**

Volvi a medir hoy las cifras de mi pagina sellada, una a una: `346`, `740`, `1` y `41`; el reparto
`7`, `15` y `19` de la bandeja; las `469`, `396`, `242` y `101` palabras; los `390` de poblacion;
los `4` y los `0` vecinos sobre umbral y sus digitos; los `15` pares de `cap_02`; el `23` de
bloques pegados; las huellas `997ece8f`, `f6f4f4dd`, `17327e3a` y `9bf10e67`; y las `14` deudas
vivas con sus `10` pagadas. **Ninguna se movio.** Las dos unicas que no se sostienen son las de
`48.9.a` y `48.9.b`.

### 48.9.d. **MI TAREA BLOQUEANTE DEL AUDITOR PARA LA VUELTA 50** (`5.5`, escalada al penultimo escalon)

> **`AUDITOR` esta en `2 de 3`. La escalada se ENCARGA, no solo se declara**, y declararla sin
> encargarla seria una caida propia mas, escrita con mi nombre.

| | |
|---|---|
| **TAREA BLOQUEANTE DEL AUDITOR, vuelta 50** | **El barrido del remedio se corre COMO ULTIMA OPERACION de mi fase ciega, sobre la pagina ya terminada, y su salida se pega DESPUES de todo lo demas.** Si al pegarla escribo una linea mas de prosa, **lo vuelvo a correr.** La cuenta de golpes que publique tiene que ser la del fichero que el arnes va a sellar, **no la de una version intermedia** |
| **como se comprueba que esta roto** | se corre `.v49aud/17_superlativos.py` (o su sucesor) **sobre la apertura ya sellada** y se compara su cabecera con la cuenta que la pagina publica. **Si no coinciden, roto**, sin discusion y sin necesidad de leer una sola frase |
| **por que esta forma y no otra** | mis tres ultimas caidas propias son de la misma familia: **una cifra de la fase ciega que dejo de ser cierta porque la pagina siguio creciendo.** El remedio no puede ser *acuerdate*: tiene que ser **un orden de operaciones con una comprobacion mecanica al final** |
| **`REMEDIO` segundo, que sigue vivo y esta tanda CUMPLIO** | el `HEREDADO 2` de la `ACTA 47`: toda frase mia que acompane a un pegado dice lo que ESE pegado mide, y la conclusion va aparte y marcada `LECTURA` |

## 48.10. EL CREDITO DE ESTA TANDA

| especie | esta tanda | racha al cerrar | por que |
|---|---|---|---|
| **`CLASE`** | **LIMPIA** | **`0 de 2`** | cero veredictos escritos en la vuelta (`740` contra `740`, medido por diferencia) |
| **`CIFRA PUBLICADA`** | **LIMPIA** | **`0 de 2`** | las dos sedes duraderas que la vuelta toco son fichas de `cuarentena/`, que `d027` adjudico que no son sede de `5.2`, y sus correcciones las verifique contra el libro |
| **`DATO MOVIDO`** | **LIMPIA** | **`0 de 2`** | el `git diff` de la vuelta entera sobre `dataset/`, `bitacora/`, `config/` y `censos/` sale vacio |
| **`REPORTE`** | **`1` caida, de PROSA, NO acumula** | **de `1 de 3` a `0`** | `48.6.a`, y `5.4` corregida el 16 sep: una tanda con caidas solo de las que no acumulan **reinicia la racha igual** |
| **`AUDITOR`** | **`2` caidas, las dos de mis especies** | **de `1 de 3` a `2 de 3`** | `48.9.a` y `48.9.b`. **Lo subo yo**, y por eso `48.9.d` va encargada y no solo declarada |

## 48.11. LAS CONDICIONES DE PARADA (`AUDITOR_FORJA.md` 3): **NINGUNA SE CUMPLE**

| condicion | como sale | medido con |
|---|---|---|
| **doctrina NUEVA necesaria** | **NO.** Las adjudicaciones de `48.5` se apoyan en reglas escritas y citadas: `5.2`, `5.4`, `7.B`, `7.C`, `D.38.1`, `D.45`, `47.5.d` y la adjudicacion de sede de `d027`. **Y las dos preguntas nuevas que traigo** (la puerta de `D.39` sin caso rojo automatico, y las ocho cifras declaradas a mano) **se registran con su medida y se quedan ahi**, que es lo que `D.56` manda hacer con una pregunta nueva | `48.3`, `48.5.a` |
| **contradiccion con regla o cifra publicada** | **NO.** Las tres correcciones de esta vuelta, las dos del extractor y la mia de `d031`, se escriben por **correccion declarada sin borrar**, que es el mecanismo que ya existe | `48.5`, `48.9.b` |
| **decision de Alexis** | **NO.** No se borra contenido, no se mueve un umbral, no se cambia el alcance, no se crea un remoto, no se publica fuera del repo | `git diff` de `config/` vacio |
| **fallo tecnico repetido** | **NO.** `gate`, `guiones`, las `318` pruebas, el tallado y el censo: **los cinco verdes hoy y corridos por mi.** La corrida roja de `d033` **no se repitio**: las `20` del extractor mas mis `6` dan `0` de `26` | `48.2.a` |
| **credito roto** | **NO.** `AUDITOR` en `2 de 3` y el tope es `3`; las otras cuatro por debajo del suyo | `48.10` |
| **campania consumada** | **NO** | `python forja.py tablero`: *MUNDO 11: faltan 3 de 3 libros del corte* |

**NO ESCRIBO `docs/loop/PARA_ALEXIS.md`.** El encargo de la vuelta `50` sale de esta sede.

## 48.12. EL COSTE DEL TURNO (`D.55`)

    $ python -c "import json,io;print(json.loads(io.open('docs/loop/ultimo_apertura.json',encoding='utf-8').read())['total_cost_usd'])"
    12.353634999999997

Ese bloque lee el coste que **el arnes** escribio para mi fase ciega. El de este segundo turno no
lo puedo leer desde dentro, porque el arnes lo escribe cuando mi turno ya termino.

**`12,35` USD en la fase ciega sola, por encima de los `10` de `D.55`, y lo declaro aunque la
vuelta sea de saneamiento.** En que se fue, con su instrumento al lado: **los barridos `D.38.4`**,
que miden la senial `1` de cada ficha contra los otros `389` de la poblacion **uno a uno y sin
muestra**. Solo los nueve de la fase ciega (`d027`, `d032` y los `7` de `cap_02`) costaron
`378,0`, `820,3`, `510,8`, `426,7`, `140,6`, `127,0`, `185,0`, `166,3` y `223,2` s, que suman
**`2.977,9` s de reloj**. **No hay forma barata de cumplir `D.38.4`:** la alternativa es aproximar,
y aproximar es justo lo que la regla prohibe.

**LA PIEZA CARA DE ESTE SEGUNDO TURNO ES LA PRUEBA DE ACEPTACION** (`318` pruebas, `1m41.879s`) y
**el resto son guiones de segundos**: el tallado, el censo partido por documento, los `44` tramos,
el recuento de pasos, la mutacion de la puerta sobre una copia y la aritmetica. **En mis dos
turnos no corre ni una aduana**, que es la pieza que se lleva el `88,2` por ciento del turno del
extractor. **Su turno es caro en reloj de maquina y el mio en fichas leidas.**
