
---

# ACTA 31. **HUECO DE ACTA: cubro DOS vueltas**, la `32` del serial (`scott_radical_candor`, `cap_11` cerrado en insercion) y la **vuelta 1 del frente `grove_high_output`, que NO ESTA CERRADA Y SIGUE ESCRIBIENDO MIENTRAS FIRMO**. La `32` sale limpia de `CLASE` y de `CIFRA PUBLICADA`, su par unico y sus nueve discutibles se sostienen, y sus cifras de cierre me salen al digito. Y aun asi: **su tabla `Y.8.d` publica `167` pasos de `cap_11` *en el grafo* y *capitulo entero*, y en el grafo hay `187` sobre `16` nodos. `REPORTE` LLEGA A `3 de 3` Y EL BUCLE SE DETIENE.** Y mi propia apertura sellada publica una poblacion de vecinos de `511` que la doctrina vigente pone en `348`, con la exclusion escrita en la regla que yo cite: **MI RACHA SUBE A `1 de 3`**

*Escrita por el auditor del bucle. Protocolo: `docs/loop/AUDITOR_FORJA.md`. Mi fase ciega esta en
`docs/loop/APERTURA_CIEGA.md` y **el arnes la sello antes de exponerme el reporte**. Modo austero
(`D.47`).*

    $ git hash-object docs/loop/APERTURA_CIEGA.md
    b02c03844aaf54dc029fa9f946e4a9c60d9b16ba
    $ tail -1 docs/loop/SELLOS_APERTURA.jsonl
    {"vuelta": 1, "fecha": "2026-09-16 21:16:39", "sello": "b02c03844aaf54dc029fa9f946e4a9c60d9b16ba"}

**EL SELLO CUADRA AL DIGITO: no he tocado mi apertura despues de sellarla.**

## 0. HUECO DE ACTA, Y LO MIDO ANTES DE NADA (`AUDITOR_FORJA.md` 1.0)

    $ grep -o "^# ACTA [0-9]*\. VUELTA [0-9]*" docs/loop/ACTA_AUDITOR.md | tail -3
      # ACTA 28. VUELTA 28
      # ACTA 29. VUELTA 30
      # ACTA 30. VUELTA 31

**HAY HUECO, y no lo digo yo primero: lo midio el arnes antes de invocarme.**

    $ sed -n '919,922p' docs/loop/loop.log
      [2026-09-16 20:53:52] ROL INICIAL POR MEDICION: AUDITOR. El REPORTE es mas nuevo que el ACTA,
        asi que la vuelta anterior quedo SIN AUDITAR.
        ultimo commit de REPORTE.md      : 2026-09-16 20:23:56
        ultimo commit de ACTA_AUDITOR.md : 2026-09-16 19:33:58

**LAS DOS VUELTAS QUE CUBRO, NOMBRADAS UNA A UNA:**

| vuelta | rama que la escribio | estado | que audito de ella |
|---|---|---|---|
| **VUELTA 32** (lote 4, `scott_radical_candor`, `cap_11` en insercion) | `extraccion-mundo-11` | **CERRADA** en `4ca7c58` | **todo**: cifras, par, nueve discutibles, fidelidad |
| **VUELTA 1 del frente `grove_high_output`** | `extraccion-grove_high_output`, **la mia** | **ABIERTA**: `TAREA 1` cerrada, `TAREA 2` y `TAREA 3` sin escribir | **lo que esta publicado**, y digo fila por fila lo que no puedo auditar y por que |

### 0.1. LA HERENCIA QUE DECLARE EN LA FASE CIEGA, CERRADA AQUI (`D.40`)

| # | lo que declare al abrir | **como queda al cerrar** |
|---:|---|---|
| **1** | `CUMPLIDO`: ninguna celda de mi apertura lleva un numero de una lectura mia | **CUMPLIDO EN LA FORMA Y ROTO EN EL FONDO.** `celdas.py` conto `64` celdas con cifra y las `8` cuentas llevaban su instrumento, **y una de las ocho mide la poblacion equivocada** (`7.1`). El remedio pedia *instrumento al lado*, no *rotulo cierto*, asi que **no lo cargo como `REMEDIO ROTO`**: lo cargo como `CIFRA PUBLICADA PROPIA`, que es su especie |
| **2** | `NO APLICA`, con su motivo y su salida pegada | **SOSTENIDO**, y hoy lo cumplo con caso: mis clases del par de la vuelta 32 estan en `.vg01a/mis_clases_32.txt` a las `21:36:12` y mi primera corrida que imprime una razon es de las `21:36:27` (`2.1`) |
| **3** | `CUMPLIDO`: toda cifra que firmo la corro yo | **CUMPLIDO.** Las `10` filas de `1.` y las `4` de `5.` llevan mi comando y mi salida, ninguna copiada del reporte |
| **4** | `CUMPLIDO`: ninguna tabla mia con constante tecleada dentro | **CUMPLIDO CON UNA EXCEPCION DECLARADA EN SU PRIMERA LINEA**, que es lo que el remedio pide: `.vg01a/frontera_32.py` teclea los **dos hashes** de apertura y cierre de la vuelta 32, que salen del propio reporte, **y lo imprime** |

## 1. LA VERIFICACION, CON MIS COMANDOS Y EN ESTA VUELTA (`AUDITOR_FORJA.md` 1.1)

    $ python forja.py gate
      GATE VERDE.
        nodos verificados: 270
    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python forja.py resolutor
      nodos vivos: 270 | nodos deprecados (archivo): 0 | alias registrados: 0
    $ python tests/test_aceptacion.py
      total: 201 pruebas, 0 fallos, 0 errores
    $ python scripts/tallar_reporte.py --estricto
      TALLADO VERDE: las 71 tabla(s) comprobables son las de su instrumento, celda a celda.
    $ python scripts/censar_rutas.py
      CENSO VERDE: las 524 rutas publicadas sostienen lo que dicen sostener.

**LAS SEIS EN VERDE, CORRIDAS POR MI A LAS `21:30` DEL 16 sep.** Y mi propio recuento del dataset y de
las bandejas, con su instrumento:

<!-- TALLADO: script=.vg01a/cuentas.py salida=.vg01a/cuentas.txt -->

| pieza | **lo que mide mi instrumento hoy** | lo que la vuelta 32 publica al cerrar | cuadra |
|---|---:|---:|---|
| nodos en `dataset/nodos.jsonl` | **270** | 270 | **SI** |
| aristas por `nodos_siguientes` | **105** | 105 | **SI** |
| aristas por `nodos_previos` | **105** | 105 | **SI** |
| veredictos en `bitacora/VEREDICTOS.jsonl` | **396** | 396 | **SI** |
| de ellos, con `no_consumada: true` | **14** | 14 | **SI** |
| bandeja del lote 4, `scott_radical_candor` | **75** | 75 | **SI** |
| archivados del lote 4 | **67** | 67 | **SI** |
| bandeja del lote 5, `marquet_turn_the_ship` | **3** | 3 | **SI** |
| lote 4 insertado sobre `142`, por ciento | **47,18** | 47,2 | **SI**, redondeo |
| veredictos por clase | **`SANO` 279, `CONTINUA` 112, `CORREGIDO` 5** | no la publica | la anado yo |

**Y LA FRONTERA DE LA VUELTA 32, MEDIDA POR LOS DOS EXTREMOS EN GIT Y NO EN SU PROSA:**

<!-- TALLADO: script=.vg01a/frontera_32.py salida=.vg01a/frontera_32.txt -->

    $ python .vg01a/frontera_32.py
      56a0df6  apertura vuelta 32   nodos=267 veredictos=391
      4ca7c58  cierre vuelta 32     nodos=270 veredictos=396
      HEAD     hoy                  nodos=270 veredictos=396

**`267` a `270` y `391` a `396`, al digito contra su tabla `Y.8.b`.** Y los `5` veredictos nuevos los
desgloso yo y me salen los suyos: `1` de vecino (el `SANO` del kanban), `3` declaraciones de arista (la
de `TAREA 2.d` y las dos de caducidad) y `1` correccion declarada. **`1` mas `3` mas `1` son `5`.**

### 1.1. LA UNICA DISCREPANCIA DE INSTRUMENTO, Y ES DE METODO Y NO DE DATO

**Su reporte publica `200` pruebas y yo cuento `201`.** No es una cifra falsa suya:

    $ git show 4ca7c58:tests/test_aceptacion.py > .vg01a/test_4ca7c58.py
    $ python .vg01a/test_4ca7c58.py
      total: 200 pruebas, 0 fallos, 0 errores

**`200` era cierto en su commit de cierre.** La prueba que falta la metio `269c068`, el commit del
fundador que escribe `D.45` y `D.47`, **posterior a su cierre**. `EXTRACTOR.md` 5 manda declarar la
discrepancia en vez de copiar, y aqui la declaro al reves: **la suya era buena y la mia tambien, y las
separa un commit que no es de ninguno de los dos.**

## 2. LA RELECTURA CIEGA (`AUDITOR_FORJA.md` 1.2 y 5.1)

### 2.1. EL PAR UNICO DE VECINO DE LA TANDA, CON MI CLASE ESCRITA ANTES DE DESTAPAR SU RAZON

*El remedio `2` que herede manda que mi clase este en fichero antes de la primera corrida que imprima
una razon. Las horas, pegadas:*

    $ ls -la --time-style=full-iso .vg01a/mis_clases_32.txt
      1751 2026-09-16 21:36:12.923510900 -0400 .vg01a/mis_clases_32.txt
    $ date            (justo antes de abrir la bitacora)
      Wed, Sep 16, 2026  9:36:27 PM

| | |
|---|---|
| **el par** | hijo `montar_tablero_kanban_medir_actividades` (`10` pasos), madre `repartir_notas_publicar_reparto_esperado` (`9` pasos, en bandeja) |
| **su señal** | `paso_contra_nodo` `0,607`, la unica que la aduana levanto en toda la tanda |
| **MI CLASE, escrita a ciegas** | **`SANO`. Ni `CONTINUA` ni `REPITE`, y tampoco arista** |
| **su clase** | **`SANO`, sin arista** |
| **veredicto** | **COINCIDIMOS, y su razon es mejor que mi sospecha** |

**LA VARA, con direccion y sin bascula:** el objeto del hijo es **el trabajo en curso** (tres columnas,
notas por persona, quien es el cuello de botella); el de la madre es **la nota de la persona** (que
reparto esperas y si lo publicas). **Lo que queda fuera del solape es procedimiento en los dos lados**,
y ninguno es subconjunto del otro. Y `NOMBRAR NO ES PROCEDIMENTAR`: el paso `10` del hijo **nombra** la
evaluacion como consecuencia y no la ejecuta, asi que tampoco sostiene arista.

**DONDE ME GANA SU LECTURA, y lo digo porque mide la calidad de la mia:** yo supuse que el solape estaba
en su paso `10` contra el paso `9` de ella. **Su razon nombra el par verdadero**, su paso `4` contra el
paso `3` de ella, *y lo que comparten es el andamio de mi propia formula de redaccion, lo que el texto
dice que, no el objeto*. **Misma clase, mejor diagnostico, y el suyo estaba escrito en la bitacora antes
de que yo lo leyera.**

### 2.2. LOS NUEVE DISCUTIBLES MARCADOS, ADJUDICADOS UNO A UNO (`D.47`: por numero y linea)

| # | lo que marco | **mi adjudicacion** | la regla o la lectura que la sostiene |
|---:|---|---|---|
| **1** | `8` rotulos con nodo en el grafo contra los `7` del encargo | **SE SOSTIENE, y el `7` del encargo era del auditor y queda corregido sin borrarse** | mi `.vg01a/cabeza.py` lee el indice del fichero y el dataset: **`10` rotulos, `10` nodos, `9` cableados y reciprocos**. Antes de insertar kanban y pasear eran `8` en el grafo. **Su instrumento midio bien y mi predecesor conto sobre la tabla rota de la vuelta 31** |
| **2** | no cablear la arista del rotulo `7` a `pelear_proliferacion` | **SE SOSTIENE COMO `D.37`, Y LA ARISTA ES DECLARABLE POR `D.29`** | `EXTRACTOR.md` 15.6 pide que la parte sea *la que ese paso nombra* y el paso `6` nombra *las zonas libres de reuniones*: por `D.37` tiene razon en no cablearla. **Pero 15.6 escribe la otra puerta:** *si el texto enumera sin la cita literal, esto NO es `D.37`: es `D.29`, y la arista se declara con razon escrita*. **Mi lectura de `L223` a `L233`**: la seccion trata el dia sin reuniones (paso `4` del nodo) y cierra bloqueando tiempo de ejecutar, **y ocupa el septimo hueco de la lista del autor**. Queda en la cola con mi razon, **para la rama que si puede cablear** |
| **3** | llamar *dos vias independientes* a `10` rotulos y `10` titulares | **SE SOSTIENE LA COLUMNA Y SE CORRIGE LA PALABRA** | los valores de la celda son ciertos, y la fila `7` (`SOLO LA POSICION`) es lo que hace visible el caso. **No son dos vias: son dos CAMPOS del mismo fichero.** Correccion de palabra, no de cifra, **y la levanto porque la levanto el primero** |
| **4** | `SANO` para el kanban con `0,607` | **SE SOSTIENE**, coincidimos a ciegas (`2.1`) | la vara `6.1`, procedimiento en los dos lados |
| **5** | paso `10` del kanban es `TRANSCRIPCION` | **SE SOSTIENE** | lei `L249`: *Measuring activities and displaying them publicly also tends to lead to ratings and promotions that more consistently reward the top performers and are less prone to the biases that bedevil us all* es **general y del libro**, y su porque (*bias was less likely to creep into hiring, rating, and promotion decisions when activities got measured*) **tambien esta escrito en general**, aunque viva dentro del caso de Rivkin. **No es puente** |
| **6** | paso `8` del kanban se para en la primera frase de `L245` | **SE SOSTIENE** | la frase es literal del libro, y dejar fuera el caso de AdSense **no convierte el nodo en postura**: sus pasos `1` a `4` montan el tablero. *Una advertencia es linea* (vara `6.1`) |
| **7** | declarar vigentes los `4` `RANCIO` propios en vez de releerlos | **SE SOSTIENE** | `D.15` deja las dos salidas y la declaracion trae su razon y su ruta. **La objecion de independencia es buena y no es una regla**: va a la cola como relectura, no como caida |
| **8** | archivar con `git mv` y no con una operacion de la aduana | **SE SOSTIENE, Y NO ES `DATO MOVIDO`** | la definicion del 16 sep acota `DATO MOVIDO` a `dataset/`, `bitacora/` y `censos/`. **`cuarentena/` no esta**, y `D.31` manda archivar sin decir con que mano. Su propuesta `3` sube al fundador |
| **9** | no cablear `debatir_decidir` a su madre por contenido | **SE SOSTIENE** | lo comprobo en vez de aceptarlo: `0` de `14` pasos de la madre lo nombran. **`D.37` pide un paso que citar y no hay ninguno.** Que quede huerfano en un capitulo cableado es registro, no deuda |

**NUEVE MARCADOS, NUEVE SOSTENIDOS EN SU VEREDICTO. CERO CAIDAS DENTRO DEL MARCADO.** Los dos que
llevan matiz (`2` y `3`) **lo llevan a favor de su lectura y no en contra**: el `2` abre una puerta que
el propio `15.6` escribe, y el `3` corrige una palabra suya que el mismo puso en duda.

## 3. LA MUESTRA PINEADA DE LOS SANOS (`AUDITOR_FORJA.md` 7)

| | |
|---|---:|
| veredictos `SANO` de la tanda | **1** |
| menos de tres, asi que **releo TODOS** y lo digo con su cifra | **1 de 1** |
| se sostienen | **1** |
| caen | **0** |
| tasa de caida de `CLASE` | **`0,00` por ciento** |
| banda exacta al 95 por ciento, una cola | **`0,00` a `95,00` por ciento** |

**LA BANDA ES CASI TODO EL RANGO Y ESO ES LA CIFRA, no un defecto del metodo:** con **una** relectura no
hay prueba de tasa. Lo digo porque la `ACTA 30` ya avisaba de lo mismo con seis, y **quien lea las dos
actas seguidas puede leer dos `0,00` por ciento como si midieran lo mismo. No lo miden.**

**Y UN `SANO` SIN RAZON ESCRITA ES CAIDA AUNQUE ACIERTE** (`D.8`): el unico `SANO` de la tanda **tiene
razon escrita, larga, y con el par de pasos nombrado**. No hay caida por este lado.

## 4. LA CAIDA DE LA VUELTA 32, FUERA DEL MARCADO: **`167` PASOS QUE EN EL GRAFO SON `187`**

*`AUDITOR_FORJA.md` 8.3 me obliga a contar yo los pasos del capitulo y comparar con lo que el reporte
dice. Lo conte. No cuadra.*

<!-- TALLADO: script=.vg01a/pasos_cap.py salida=.vg01a/pasos_cap.txt -->

    $ python .vg01a/pasos_cap.py scott_radical_candor cap_11
      nodos que declaran su unidad de origen : 40 de 270
      scott_radical_candor   cap_11      16 nodos     187 pasos

<!-- TALLADO: script=.vg01a/cap11_entrada.py salida=.vg01a/cap11_entrada.txt -->

    $ python .vg01a/cap11_entrada.py        (el commit de entrada de cada uno, por git log -S)
      recorrer_rueda_conscientemente_cultura_equipo   14 pasos   487767c  VUELTA 28
      bloquear_tiempo_pensar_calendario                6 pasos   5834c50  VUELTA 30
      once nodos                                     142 pasos   cf43222  VUELTA 31
      tres nodos                                      25 pasos   94cae85  VUELTA 32

**LO QUE SU TABLA `Y.8.d` DICE, en dos filas, y las dos en celda de tabla:**

| lo que su fila publica | **lo que mi instrumento mide** |
|---|---|
| *pasos de `cap_11` **en el grafo**: `167`, los `142` de la vuelta 31 mas los `25` de hoy* | **en el grafo hay `187`, sobre `16` nodos** |
| *`PASOS INVENTADOS` de `cap_11`, **capitulo entero**: `0,00` por ciento sobre `167` pasos* | el capitulo entero son **`187`**; `167` son **los `14` candidatos de los tramos de las vueltas `31` y `32`** |

**LA CIFRA ES CIERTA Y EL ROTULO ES FALSO, y esa es una especie con nombre en esta casa.**
`AUDITOR_FORJA.md` 1, ensanche de `D.38.3` del 16 sep: *la linea que acompania a una cifra dice lo que el
instrumento MIDIO*, y su ejemplar es **mio**, de la vuelta 26: *el instrumento estaba pegado y la cifra
era cierta: lo falso era la frase.* **`142` mas `25` son `167` y nadie discute la suma. Lo que no es
cierto es que eso sea el grafo ni el capitulo entero:** faltan `recorrer_rueda` (`14` pasos, vuelta 28) y
`bloquear_tiempo` (`6`, vuelta 30), **`20` pasos que se escribieron para `cap_11` y que la palabra
*entero* promete y no trae.**

**LO QUE NO ES, y lo digo porque acota el dano:** el numerador no se mueve (`0` puentes por mi relectura
de `5.`), asi que **`0` sobre `167` y `0` sobre `187` dan el mismo `0,00` por ciento y la decision de
volumen no cambia.** Y mi predecesor **no comparte esta caida**: su `ACTA 30` `8.1` escribio la fila como
*`cap_11` (los once del tramo)*, que es exacto. **El rotulo se ensancho en esta vuelta.**

**POR QUE ACUMULA, con la regla delante:** sede `docs/loop/REPORTE.md`, asi que la especie es **`REPORTE`**
(`5.2`, la sede decide la especie y no el dano). Y `5.2` dice que `REPORTE` *acumula solo si la cifra vive
en TABLA, CABECERA o CONCLUSION*: **vive en tabla, en dos filas de `Y.8.d`.** La cargo como **UNA** caida
y no como dos, porque **es el mismo rotulo ensanchado en dos filas de la misma tabla**.

**Y ESTA FUERA DEL MARCADO**, que es lo que la hace informativa (`5.1`): ninguno de sus nueve discutibles
la nombra. Su discutible `5` **usa** la frase *los `167` del capitulo entero* para medir otra cosa, **asi
que la frase viajo dentro de un discutible sin ser lo discutido.**

## 5. `PASOS INVENTADOS POR CAPITULO`, FIRMADA POR MI (`AUDITOR_FORJA.md` 8)

**LOS `25` PASOS DEL TRAMO DE LA VUELTA 32, RELEIDOS UNO A UNO CONTRA SU PARRAFO** (`8.3.2`), que es la
mitad de la regla que invita al error de marcar un puente como transcripcion:

| capitulo | nodos | pasos escritos | **puentes que encuentro** | **`PASOS INVENTADOS`** |
|---|---:|---:|---:|---:|
| **`cap_11`, el tramo de la vuelta 32** | 3 | **25** | **0** | **`0,00` por ciento** |
| **total del lote 4 en esta vuelta** | 3 | **25** | **0** | **`0,00` por ciento** |

**LAS TRES FUENTES QUE ABRI, y no la palabra del reporte:** `L235` a `L249` (`KANBAN BOARDS`, `10` pasos),
`L251` a `L269` (`WALK AROUND`, `9`) y `L301` a `L305` (`Debate and decide explicitly`, `6`). **Los `25`
estan en el libro**, incluida la lista entera de asuntos de cultura del paso `2` de `debatir_decidir` y
los tres *primero, segundo, tercero* de `pasear`. **Y los casos que el libro cuenta y el nodo deja fuera**
(Costolo, Lincoln, Hewlett Packard, los platos sucios, AdSense, Rivkin) **estan fuera con razon: son
relato, y meterlos habria sido el puente.**

### 5.1. LA FILA DEL CAPITULO ENTERO, QUE ES LA QUE SU `Y.8.d` PROMETE, Y LO QUE FIRMO DE ELLA

| capitulo entero en el grafo | nodos | pasos | quien firmo cada tramo |
|---|---:|---:|---|
| **`cap_11`** | **16** | **187** | `167` firmados: `142` en la `ACTA 30` y `25` en esta acta. **`20` de las vueltas 28 y 30**, firmados en sus propias actas |

**NO PUBLICO UN PORCENTAJE DEL CAPITULO ENTERO COMO MIO** (`8.3`: *si no puedes verificarla, lo dices y no
la publicas como tuya*): **hoy he releido `25` de esos `187` pasos.** Lo que firmo es la fila del tramo.
**Lo que declaro es la poblacion, `187` sobre `16` nodos, que es lo que la palabra *entero* tiene que
significar la proxima vez que se escriba.**

### 5.2. LO QUE LA CIFRA DECIDE SOBRE EL VOLUMEN

| lo que mido | lo que dice `8.1` |
|---|---|
| `0,00` se mantiene respecto a la vuelta 31 (`0,00`) | **permitiria un capitulo mas por vuelta** |
| `0,00` esta por debajo del tope de `10` | **el freno de fidelidad NO se activa** |

**Y NO DIMENSIONO NINGUN LOTE, porque el bucle para** (`9.`). La decision de volumen del frente
`grove_high_output` **la tomara el acta que lo cierre con su vuelta cerrada delante**, y hoy no hay vuelta
cerrada que medir (`6.`).

### 5.3. **EL CIERRE CORTO, VERIFICADO** (`EXTRACTOR.md` 12.4)

**No hay cierre corto que declarar en la vuelta 32:** cerro `cap_11` con los `3` que quedaban, `14` de
`14` del tramo, y **ninguna unidad sola paso el techo de candidatos.** No hay caida por este lado.

## 6. LA VUELTA 1 DEL FRENTE `grove_high_output`: LO QUE SI PUEDO AUDITAR, Y LO QUE NO

### 6.1. LO QUE PUEDO Y LO VERIFICO AL DIGITO: SU `TAREA 1`, LA FRONTERA

<!-- TALLADO: parcial salida=.vg01a/frontera_recontrol.txt -->

    $ python .vg01c/cierre_frontera.py fuentes/grove_high_output/cap_01.md fuentes/grove_high_output/cap_02.md
      cap_01.md   cabecera=   23 cuerpo= 3841 suma=  3864 fichero=  3864  CIERRA=SI
      cap_02.md   cabecera=   41 cuerpo= 3386 suma=  3427 fichero=  3427  CIERRA=SI
    $ wc -w fuentes/grove_high_output/cap_01.md fuentes/grove_high_output/cap_02.md
      3864 cap_01.md   3427 cap_02.md

**SUS DOS FRONTERAS CIERRAN CONTRA MI INSTRUMENTO Y NO CONTRA SU PALABRA**, y son las mismas cifras que yo
publique en mi apertura sellada **antes de ver su reporte**: `3841` y `3386` de cuerpo, `3864` y `3427` de
fichero, cero lineas sin cubrir y cero solapes. **Su `TAREA 1` se sostiene entera.**

### 6.2. Y EL CRUCE DE LOS DOS CORTES CIEGOS, QUE ES LA UNICA PRUEBA QUE VALE AQUI

*Mi corte esta sellado en `APERTURA_CIEGA.md` `4.` y `5.`, escrito **antes de que existiera un solo
candidato suyo**. Lo cruzo contra el estado del arbol, no contra su reporte, porque su reporte no los
trae.*

<!-- TALLADO: parcial salida=.vg01a/grove_candidatos.txt -->

    $ (lector de cuarentena/grove_high_output/*.json, corrido a las 21:51)
      revisar_tres_preguntas_valor_carrera             cap_01  L101 a L107    7 pasos
      construir_flujo_produccion_paso_limitante        cap_02  L15  a L27    10 pasos
      clasificar_trabajo_proceso_montaje_prueba        cap_02  L37  a L47     7 pasos
      rehacer_flujo_paso_limitante_capacidad           cap_02  L49  a L55     6 pasos
      equilibrar_capacidad_personal_inventario_plazo   cap_02  L57  a L61     8 pasos
      preferir_inspeccion_proceso_prueba_destructiva   cap_02  L63  a L67     6 pasos
      dimensionar_inventario_materia_prima_reposicion  cap_02  L69           7 pasos
      detectar_arreglar_fallo_etapa_menor_valor        cap_02  L71  a L75     6 pasos
      candidatos: 8   pasos escritos: 57

| mi pieza ciega | mi clase sellada | lo que el arbol trae a las `21:51` | coincide |
|---|---|---|---|
| `cap_01` `Q7` `L103` a `L107` | **CANDIDATO** | `revisar_tres_preguntas_valor_carrera`, `L101` a `L107` | **SI** |
| `cap_01` `Q1`, `Q2`, `Q3`, `Q4`, `Q6`, `Q8` | **NO CANDIDATO** | ninguno | **SI** |
| `cap_01` `Q5` `L79` a `L85` | **NO CANDIDATO EN ESTA UNIDAD**, y `REPITE` si se escribia | ninguno | **SI** |
| `cap_02` `P0` mas `P1` `L15` a `L29` | **un candidato** | `construir_flujo_produccion_paso_limitante` | **SI** |
| `cap_02` `P2` `L31` a `L35` (reclutamiento) | **NO CANDIDATO**, marcado discutible | ninguno | **SI** |
| `cap_02` `P3` `L37` a `L47` | **DISCUTIBLE, me inclino a CANDIDATO** | `clasificar_trabajo_proceso_montaje_prueba` | **SI**, y mi duda se resuelve del lado que dije |
| `cap_02` `P4` `L49` a `L61` | **UN candidato** | **DOS**: `L49` a `L55` y `L57` a `L61` | **NO. La unica diferencia de los dos cortes** |
| `cap_02` `P5`, `P6`, `P7` | **CANDIDATO** los tres | los tres, en sus mismos rangos | **SI** |
| `cap_02` `P8` `L77` a `L79` (justicia penal) | **NO CANDIDATO**, y **PUENTE si aparecia nodo** | ninguno | **SI** |

**MI PREVISION `2` NO SE CUMPLIO Y ESO ES LO MEJOR DE ESTE CRUCE.** Escribi sellado que sus dos sitios de
puente eran el reclutamiento y la justicia penal, **y no hay nodo en ninguno de los dos.** `710` palabras
de ilustracion que el corte deja fuera con razon.

**Y LA UNICA DIFERENCIA LA RESUELVO CONTRA MI, y la escribo ahora y no despues:** mi pieza `L49` a `L61`
era **una** y el arbol trae **dos**. Lei los dos rangos. `L49` a `L55` da que **la capacidad limitada
MUEVE el paso limitante** y manda rehacer el flujo; `L57` a `L61` da el **canje entre equipo, personal e
inventario contra el plazo**, y manda reducirlo a relaciones cuantificables. **Queda procedimiento propio
de los dos lados, y la vara `6.1` dice que eso no es duplicado: es la particion mas fina.** **Mi corte de
una sola pieza era el mas grueso de los dos**, y en mi propia apertura `6.1` ya habia nombrado las dos
aportaciones por separado **sin sacar la consecuencia**. **Retiro mi pieza unica.**

> **LO QUE ESTE CRUCE NO ES: una adjudicacion de sus veredictos.** No hay veredictos que adjudicar, y los
> ocho ficheros **no estan en su reporte ni en la bitacora**. Es un cruce de dos cortes, **fechado a las
> `21:51`**, y lo que mide es la frontera, no su tanda.

### 6.3. LO QUE NO PUEDO AUDITAR, FILA POR FILA Y CON SU MOTIVO

| lo que el protocolo me pide | por que no puedo | la medida |
|---|---|---|
| **el hash del reporte, para clonar y recomputar** (`1.1`) | **su reporte no publica hash de cierre**: su apertura `Z.0`, que lo traia, **la borro su propio commit siguiente** (`6.4`) | `git show caaf15c -- docs/loop/REPORTE.md` |
| **sus veredictos** | **no hay ninguno** | `grep -c grove_high_output bitacora/VEREDICTOS.jsonl` da **`0`** de `396` |
| **sus discutibles marcados** (`1.2` y `5.1`) | **no hay seccion de discutibles**: el reporte acaba en `Z.1.c` | `sed -n '36039,$p' docs/loop/REPORTE.md` |
| **su `PASOS INVENTADOS`** (`8`) | **su `TAREA 3` no esta escrita.** Los `57` pasos de `6.2` existen en el arbol **y el reporte no dice cuales marca `TRANSCRIPCION`**, que es lo que yo verifico | `8.3`: no la publico como mia |
| **su informe de aduana por candidato** (`EXTRACTOR.md` 16) | **`.v1g/informe_01.txt` estaba a CERO BYTES a las `21:18:50`**, y a las `21:54` habia ocho informes en el indice **sin una linea de reporte que los cite** | `ls -la --time-style=full-iso .v1g/` |
| **su cierre** | **no hay cierre.** Ni tabla de cierre, ni guardas al cerrar, ni las seis condiciones de parada | `Z.1.c` es su ultima seccion |

**NO CARGO NINGUNA DE ESTAS SEIS COMO CAIDA SUYA, y digo por que:** **una vuelta abierta no ha incumplido
nada todavia.** Lo que cargo es lo que ya esta commiteado y publicado, que es `6.4`.

### 6.4. LO QUE SI ESTA PUBLICADO Y NO TIENE CASILLERO: **su commit se llevo su propia apertura**

    $ git show 862390c --stat -- docs/loop/REPORTE.md
      docs/loop/REPORTE.md | 70 +++++++++++++++++++++++++
    $ git show caaf15c --stat -- docs/loop/REPORTE.md
      docs/loop/REPORTE.md | 141 +++++++++++++++++------------------
    $ grep -c "grove_high_output" docs/loop/REPORTE.md
      0

**A las `21:12:04` el commit `862390c` abrio la vuelta con `70` lineas: el titulo del frente, la tabla
`Z.0` de apertura medida (`EXTRACTOR.md` 4), `Z.0.a` y el esqueleto `Z.SKEL` de las tres tareas
(`EXTRACTOR.md` 3). A las `21:16:49` el commit `caaf15c` las sustituyo por `Z.1`.** El resultado es el que
cualquiera puede medir hoy: **`Z.1` cuelga directamente de `Y.8.g` de la vuelta 32, la vuelta 1 no tiene
titulo, no tiene apertura, no tiene esqueleto, y la palabra `grove_high_output` no aparece ni una vez en
`36126` lineas de reporte.**

**LO QUE SE PERDIO ERA BUENO, y es lo que mas me cuesta escribir:** aquella `Z.0` publicaba que la aduana
admite **`78`** de los `241` ficheros de bandeja y que la poblacion del informe es **`348`**, con el filtro
`_fuentes_canonicas` nombrado y la frase *la que manda es la de la aduana*. **Eso es exactamente lo que yo
publique mal** (`7.1`). **La unica lectura de esta casa que tenia razon sobre la poblacion la borro su
propio autor cuatro minutos despues de escribirla**, y yo no la lei porque el arnes me la retiraba con
razon.

**Y NO TIENE CASILLERO, LO DIGO EN VEZ DE METERLO DONDE NO VA** (la figura del 16 sep, punto 3):

| especie | por que no encaja |
|---|---|
| `REPORTE` | es *una afirmacion equivocada* (`5.2`). **Un borrado no afirma nada** |
| `CIFRA PUBLICADA` | su sede es `docs/`, `config/`, `esquema/` y el codigo de una guarda. **`docs/loop/REPORTE.md` tiene especie propia, y es la otra** |
| `DATO MOVIDO` | su definicion del 16 sep acota a `dataset/`, `bitacora/` y `censos/`. **El reporte no esta** |

**ASI QUE NO LO CARGO EN NINGUNA RACHA Y LO SUBO.** Y no lo arreglo yo: `5.6` dice que mis sedes son el
acta, el encargo y `PARA_ALEXIS.md`, **y el reporte es sede del extractor.**

## 7. MIS PROPIAS CAIDAS, CON MI NOMBRE (`AUDITOR_FORJA.md` 5.3 y 2)

### 7.1. **`CIFRA PUBLICADA PROPIA`: mi apertura sellada publica `511` de poblacion de vecinos, y la doctrina vigente la pone en `348`**

**Lo que publique**, en celda de tabla de mi apertura sellada, seccion `2.`:

    | poblacion de vecinos, D.38.4 | 511 | .vg01c/poblacion.txt, poblacion.py |

**Lo que dice la regla que yo mismo cite, en su propia seccion:** `D.38.5` del banco, **`Lo que entra en
la poblacion, y el criterio NO es una lista de carpetas`**:

    cuarentena/ tambien aloja ensayo_referencia_163/, que son 163 nodos de un catalogo de
    referencia ajeno puestos ahi para calibrar la aduana. Esos no esperan juicio: no van a
    entrar nunca en este grafo.
    ENTRA EN LA POBLACION EL CANDIDATO CUYAS FUENTES ESTAN TODAS EN LA TABLA CANONICA VIGENTE.

<!-- TALLADO: parcial salida=.vg01a/aduana_poblacion.txt -->

    $ python (llamada a src.aduana.poblacion_de_bandejas, sin reimplementarla)
      poblacion_de_bandejas() total: 86
         scott_radical_candor            75
         grove_high_output                8
         marquet_turn_the_ship            3
    $ python (las claves de fuentes/FUENTES_CANONICAS.json)
      quality_is_free_the NO esta entre las 13 claves

**LA CUENTA ERA CIERTA Y EL ROTULO ERA FALSO: es la misma especie que le cobro a el en `4.`, y me la
cobro igual.** `270` mas `241` son `511` y el instrumento estaba pegado. **Pero la poblacion del barrido
de vecinos no es ese conjunto:** los `163` de `ensayo_referencia_163` estan excluidos **por la regla que
yo cite por su numero**, y la poblacion de aquel instante era `270` mas `78`, o sea **`348`**.

**Y ARRASTRA MAS QUE LA CELDA, y por eso lo pongo entero:**

| lo que mi apertura publica | **como queda** |
|---|---|
| la celda `poblacion de vecinos, D.38.4: 511` | **FALSA.** Eran `348` |
| `6.`, *los vecinos de `cap_02` estan enteros en la bandeja `ensayo_referencia_163`* | **RETIRADA.** Ese material no es vecino de nada de esta casa |
| `6.1`, tres de mis cinco clases pre registradas (`P1`, `P6`, `P7` contra vecinos de esa bandeja) | **RETIRADAS: no eran pares.** Sus vecinos no pueden entrar nunca al grafo |
| `6.1`, la quinta (`Q5` contra `montar_reuniones_solas_mentalidad_frecuencia`, **en el GRAFO**) | **EN PIE**, y el arbol la confirma: no hay candidato de `Q5` |
| `7.` prevision `3`, *esa es la caida que mas me espero: que declare SANOS los siete por barrer solo el grafo* | **RETIRADA, y era al reves:** la aduana hace lo que la regla manda, **y el que barrio la poblacion equivocada fui yo** |

**QUE ESPECIE ES Y POR QUE ACUMULA:** `CIFRA PUBLICADA PROPIA`, *una cifra falsa en tu acta o en tu
apertura sellada*. Vive en celda de tabla de una sede sellada. **Sube mi racha a `1 de 3`.**

**Y QUE NO ES:** no es `REMEDIO ROTO`. Mi remedio `1` pedia **instrumento al lado de toda cifra**, y lo
cumpli: la cifra llevaba su instrumento y su fichero. **Lo que el remedio no pedia es que el rotulo fuera
cierto, y eso es lo que fallo.** No me lo cobro dos veces por el mismo hecho, **y digo que esa lectura no
me favorece:** cargarlo como `REMEDIO ROTO` habria dejado mi racha en `1 de 3` igual.

**LO QUE ME HABRIA SALVADO ERA LEER LA REGLA HASTA EL FINAL.** Cite `D.38.4` y `D.38.5` por su numero en
tres sitios de mi apertura. **La seccion que me desmiente esta dentro de `D.38.5`**, y lleva ahi desde el
12 sep.

### 7.2. LO QUE NO ME CARGO, Y LO DIGO PARA QUE SE PUEDA DISCUTIR

- **La averia del arnes de mi seccion `3.`** la declare en la fase ciega, sin abrir ninguno de los cuatro
  ficheros retirados, y el arnes la registro por su cuenta (`8.`). **Declararla era lo que me tocaba.**
- **Mi `HEREDADO 2` con `NO APLICA`** llevaba motivo y salida pegada, que es lo que `D.40` ensanchada y la
  regla del 16 sep piden. **No cuenta como que falta.**

## 8. LA AVERIA DEL ARNES, MEDIDA, Y **NO LA ARREGLO PORQUE `D.45` ME LO PROHIBE**

*No es una queja de fase: es la razon por la que la vuelta 1 de este frente no se puede auditar, y va con
sus horas.*

### 8.1. LAS TRES MITADES, Y LAS TRES ESTAN EN EL REGISTRO

    $ sed -n '924,932p' docs/loop/loop.log
      [20:53:52] VUELTA 1 : APERTURA CIEGA, retirados: REPORTE.md loop.log ultimo_extractor.json
                 ultimo_auditor.json
      [21:16:34] auditor ciego listo, 1361s
      [21:16:35] APERTURA CIEGA ROTA en la vuelta 1: REAPARECIERON REPORTE.md loop.log
                 ultimo_extractor.json ultimo_auditor.json
      [21:16:35]   durante la fase ciega. Solo se recuperan a mano, asi que fue deliberado.
      [21:16:45] VUELTA 1 : AUDITOR

| # | la mitad | la prueba |
|---|---|---|
| **1** | **el arnes se salto el turno del extractor** y abrio por el auditor, con razon medida | `loop.log` lineas `919` a `923` |
| **2** | **y el turno del extractor corrio de todas formas, DENTRO de mi fase ciega**: `be2b678` (`20:57:03`), `862390c` (`21:12:04`) y `caaf15c` (`21:16:49`), los tres con mensaje de extractor | `git log --date=iso` |
| **3** | **y sigue corriendo DENTRO de mi turno de acta**: la bandeja del libro tenia `1` fichero a las `21:18:39`, `2` a las `21:30` y **`8` a las `21:51`**, y el indice de git lo escribio otro proceso a las `21:54:11`, con **`20` ficheros dentro que no son mios** | `ls --time-style=full-iso`, `git status --short`, el `mtime` del indice del worktree |

**EL *fue deliberado* DE LA LINEA `929` ES LA UNICA PARTE QUE NO ES CIERTA, y la corrijo porque me acusa a
mi:** los cuatro ficheros no los recupere yo. Mi apertura sellada lo dice en su seccion `9.` antes de que
hubiera discusion, y lo que los repuso esta medido en su seccion `3.`: aparecieron los cuatro a la vez,
con hora `20:55`, **sin una sola diferencia contra `HEAD`**. **Eso es el checkout de otro proceso, no una
lectura mia.**

### 8.2. LO QUE ESTO LE HACE A LA AUDITORIA, Y NO ES UNA MOLESTIA

**`AUDITOR_FORJA.md` abre diciendo `EL ESTADO DE VERDAD ES EL REPO`.** Con dos roles escribiendo el mismo
arbol, **el repo deja de ser un estado y pasa a ser una corriente**: cada cifra que publico lleva la hora
a la que la mire y **ninguna se puede recomputar despues**. Lo he medido tres veces en este turno: la
poblacion de bandejas de la aduana me dio **`78`**, **`80`** y **`86`** en treinta y cinco minutos.

**Y ES LA MISMA FIGURA DE LA CAIDA DE LA VUELTA 28, escrita en `D.45`:** *dos `insertar` a la vez, y un
nodo entro y desaparecio con el gate en VERDE encima.* `D.45` separo extraer de insertar para que eso no
pasara. **Lo que nadie escribio es que el AUDITOR y el EXTRACTOR del MISMO frente no pueden correr a la
vez sobre el mismo arbol**, y hoy han corrido.

### 8.3. **Y NO LO TOCO**

**`D.45`, la letra:** *durante el paralelo rige moratoria de maquinaria y doctrina: ninguna sesion toca
`src/`, el banco, el arnes ni los protocolos. Una pregunta de doctrina es PARADA y sube al fundador.* Y el
encargo de este frente lo repite: *ni siquiera con una caida de dato.*

**El remedio vive en `orquestador_forja.sh`, que es el arnes.** Asi que **lo declaro con sus horas, lo
subo, y no escribo ni una linea de codigo.**

## 9. LAS RACHAS Y LAS SEIS CONDICIONES DE PARADA (`AUDITOR_FORJA.md` 3, 5.4 y 5.5)

### 9.1. Las cuatro rachas, con su motivo

| especie | de quien | venia en | **queda en** | por que |
|---|---|---|---|---|
| **`CLASE`** (y `DATO MOVIDO`) | extractor | 0 de 2 | **0 de 2** | **tanda limpia.** `1` de `1` pineada sostenida, `9` de `9` discutibles sostenidos en su veredicto, **cero veredictos mal puestos**, y los `5` veredictos nuevos cuadran con el movimiento del grafo por los dos extremos (`1.`). El `git mv` de `D.31` **no es `DATO MOVIDO`** (`2.2`, discutible `8`) |
| **`CIFRA PUBLICADA`** | extractor | 0 de 2 | **0 de 2** | toco `docs/BANCO_DE_REGLAS.md` en su cierre, **y lo que escribio ahi es la renumeracion de `D.45` a `D.46` del fundador, sin colision**: hoy el banco tiene `D.43` a `D.47` una vez cada una, y lo comprobe. **Cero cifras falsas en sede duradera** |
| **`REPORTE`** | extractor | **2 de 3** | **`3 de 3`. TOPE** | **la tabla `Y.8.d`** (`4.`): `167` pasos publicados como *en el grafo* y *capitulo entero* donde el grafo tiene `187` sobre `16` nodos. **Celda de tabla, y fuera del marcado** |
| **la mia, una sola** | **auditor** | 0 de 3 | **`1 de 3`** | **`CIFRA PUBLICADA PROPIA`** (`7.1`): la celda `511` de mi apertura sellada, que la doctrina vigente pone en `348` |

**LA CONSECUTIVIDAD, MEDIDA Y NO SUPUESTA** (`D.38.1`, con la precision de `5.4` del 16 sep: *`LIMPIA`
significa sin caidas de la especie que esa racha acumula*):

| tanda | `REPORTE` acumula en ella | quien lo dice |
|---|---|---|
| **vuelta 30** | **SI**, `1 de 3` | `ACTA 29` |
| **vuelta 31** | **SI**, `2 de 3` | `ACTA 30` `9.1` |
| **vuelta 32** | **SI**, `3 de 3` | esta acta, `4.` |

**TRES TANDAS CONSECUTIVAS Y NINGUNA LIMPIA EN MEDIO. `5.4` dice tres, y son tres.**

### 9.2. Las seis condiciones, repasadas una a una

| condicion | lo que mido | veredicto |
|---|---|---|
| **doctrina NUEVA necesaria** | **HAY UNA**: el borrado de su propia apertura del reporte (`6.4`) **no encaja en ninguna de las tres especies**, y lo demuestro con la letra de las tres. Lo demas se adjudica con regla escrita: el discutible `2` con `D.29` por la puerta que `15.6` escribe, el `8` con la definicion de `DATO MOVIDO`, **y mi propia caida con la seccion de `D.38.5` que ya estaba escrita** | **ES PARADA** |
| **contradiccion** con regla vigente o cifra publicada | **HAY DOS QUE NO SE RESUELVEN AQUI.** Una: `D.34` manda que mi fase ciega corra con el reporte retirado, y **el extractor escribio el reporte dentro de ella** (`8.1`). Dos: `AUDITOR_FORJA.md` 1.1 manda clonar el hash del reporte y **su reporte ya no publica hash, porque su commit borro la seccion que lo traia**. El remedio de las dos vive en el arnes, **y `D.45` me prohibe tocarlo** | **ES PARADA** |
| **decision de Alexis** | **HAY TRES.** La arquitectura del arnes (`8.`), la reparacion del reporte, **que es sede del extractor y no mia** (`5.6`), y las cuatro propuestas de maquinaria de la vuelta 32, que registro y **no encargo** | **ES PARADA** |
| **fallo tecnico repetido** | **NO.** `gate`, `guiones`, `resolutor`, `201` pruebas, tallado con `71` tablas y censo con `524` rutas: **las seis en verde, corridas por mi** (`1.`). La rotura de la fase ciega es la **primera**, no la segunda | **NO ES PARADA** |
| **credito roto** | **`REPORTE` `3 de 3`**, tres tandas consecutivas (`9.1`). `CLASE` `0 de 2`, `CIFRA PUBLICADA` `0 de 2`, la mia `1 de 3` | **ES PARADA** |
| **campania consumada** | **NO.** Lote 4 al `47,18` por ciento de `142` con `75` en bandeja; lote 5 con `3` sin tocar; el frente `grove_high_output` con `8` candidatos en bandeja y `0` en el grafo | **NO ES PARADA** |

**CUATRO DE LAS SEIS SE CUMPLEN, Y LA QUE MANDA ES LA DEL CREDITO, porque es la que la metrica nombra con
su cuenta: `REPORTE 3 de 3`.**

> **ESCRIBO `docs/loop/PARA_ALEXIS.md` Y DEJO `docs/loop/PROMPT_SIGUIENTE.md` VACIO** (`AUDITOR_FORJA.md` 3).

### 9.3. **LA ESCALADA, ENCARGADA Y NO SOLO DECLARADA** (`1.4` y `5.5`), Y DONDE VA CON EL BUCLE PARADO

**`5.5` me obliga a encargar el remedio de una racha en su penultimo escalon, y `REPORTE` paso del
penultimo al tope en la misma tanda.** Con el bucle detenido **no hay encargo siguiente donde ponerlo**,
asi que va donde el protocolo deja que vaya: **a `PARA_ALEXIS.md`, como la primera cosa que la retomada
tiene que hacer, con su remedio escrito y autorizado.**

**EL REMEDIO ES `D.38.3` ENSANCHADA, la del 16 sep, por extension de su propio motivo:** *la linea que
acompania a una cifra dice lo que el instrumento MIDIO, y toda conclusion sobre contenido va en linea
aparte marcada `LECTURA`.* **La cifra `167` no necesita instrumento nuevo: necesita que su rotulo diga
`los 14 candidatos de los tramos 31 y 32` en vez de `en el grafo` y `capitulo entero`.** No es maquinaria
y no pide decision nueva.

**Y EL MISMO REMEDIO ME CAZA A MI EN `7.1`, QUE ES LA PARTE QUE LO HACE CREIBLE:** las dos caidas de esta
acta, la suya y la mia, **son la misma**: una cuenta cierta bajo un rotulo que promete otra poblacion.
**Un remedio que solo se le encarga a uno de los dos no es un remedio, es un reproche.**

### 9.4. **MIS REMEDIOS PARA EL SIGUIENTE AUDITOR**, numerados y con comprobacion mecanica

| # | **REMEDIO** | como se comprueba que se cumplio |
|---:|---|---|
| **1** | **UNA CIFRA DE POBLACION NO SE PUBLICA SIN LEER HASTA EL FINAL LA REGLA QUE LA DEFINE.** Si cito una regla por su numero para justificar una poblacion, **pego en la apertura la linea de esa regla que dice que entra y que no** | que cada cifra de poblacion de mi apertura lleve **la cita literal del criterio**, no solo el numero de la regla. Hoy: `7.1` es la caida de no hacerlo |
| **2** | **TODA CIFRA DE ESTADO QUE PUBLIQUE LLEVA LA HORA A LA QUE LA MEDI**, mientras corran frentes en paralelo | que ninguna celda de estado de mi apertura ni de mi acta este sin hora cuando el arbol tenga mas de un escritor |
| **3** | **LA RELECTURA CIEGA DESTAPA UNA RAZON POR VEZ, Y DESPUES DE ESCRIBIR MI CLASE A FICHERO.** Heredado y cumplido hoy (`2.1`), lo paso entero | que el acta publique la hora del fichero de clases y que sea anterior a la primera corrida que imprima una razon |
| **4** | **UNA TABLA QUE PUBLICO COMO DE INSTRUMENTO NO LLEVA UNA CONSTANTE TECLEADA DENTRO, Y SI LA LLEVA LO DICE EN SU PRIMERA LINEA.** Heredado y cumplido hoy (`0.1`), lo paso entero | que los instrumentos de mi `.vNN/` no tengan listas de ids a mano cuando el dato las pueda casar |

### 9.5. `D.32`: NO HAY LOTE QUE ABRIR, Y LO DIGO CON LA MEDIDA

**Esta acta no cierra ningun lote.** El lote 4 esta cerrado en extraccion desde la `ACTA 24` y lo que
corria es insercion, con `75` en bandeja. **El lote 7, `grove_high_output`, esta ABIERTO y su vuelta 1 no
ha cerrado.** No hay condicion de apertura que medir porque no hay lote que cerrar.

### 9.6. LA COLA, COMO QUEDA AL CERRAR ESTA ACTA

| lo que queda | cifra que mido hoy | de quien es y que la cierra |
|---|---:|---|
| **la arista del rotulo `7` de la cabeza de `cap_11`**, adjudicada hoy como declarable por `D.29` (`2.2`) | **1** | **del serial.** `forja.py arista` con mi razon, en la rama de insercion. **Este frente no puede** |
| los `4` `RANCIO` de `D.15` declarados vigentes por quien los causo (discutible `7`) | **4** | del serial, relectura independiente. **Registro, no caida** |
| `debatir_decidir` huerfano en un capitulo cableado (discutible `9`) | **1** | del serial. Registro |
| **las cuatro propuestas de la vuelta 32** (`Y.7`) | **4** | **del fundador.** Registradas y **NO encargadas**: moratoria de maquinaria y `D.45` |
| **la apertura y el titulo borrados del reporte de la vuelta 1** (`6.4`) | **70** lineas | **del fundador**, y de la sesion que las borro. **No es mi sede** |
| **el reporte de la vuelta 1, sin `TAREA 2`, sin `TAREA 3` y sin cierre** | **2** tareas de **3** | su extractor, **cuando su turno se le devuelva sin un auditor encima** |
| **los `8` candidatos de `grove_high_output` en bandeja, con `57` pasos y sin una linea de reporte** | **8** | **su propia vuelta, al cerrarse.** `0` lineas en la bitacora |
| bandeja del lote 4 | **75** | la insercion serial |
| lote 5, `marquet_turn_the_ship` | **3** | su propio frente en paralelo |
| `censos/series_y_cabezas.md` con `0` filas y `270` nodos en el grafo | **0** | propuesta `4` de la vuelta 32. Moratoria |

---

*`ACTA 31` cerrada. **Cubre la vuelta 32 del serial y lo publicado de la vuelta 1 del frente
`grove_high_output`.** Mis ficheros de trabajo viven en `.vg01a/` y los de mi fase ciega en `.vg01c/`, y
**viajan al repo con este commit** (cosecha `7.B`). **El bucle se detiene: `PARA_ALEXIS.md` escrito y
`PROMPT_SIGUIENTE.md` vacio.***

---
