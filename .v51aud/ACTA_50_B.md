
## 50.4. LAS CAIDAS DEL EXTRACTOR, CON SU SEDE Y SU CUENTA

### 50.4.a. **`29,5` MINUTOS DONDE SU PROPIA CELDA ESCRIBE `1728,2` SEGUNDOS. ACUMULA**

**La celda entera, copiada de la tabla del techo de `MM.4.f`:**

    | minutos | 57 | 29,5 min medidos como SUELO | 1635,2 s de aduana medida mas 93 de la
    prueba de aceptacion dan 1728,2 s. Es un suelo y no un total, porque la sexta
    pasada no tiene reloj |

    $ python .v51aud/... (la aritmetica de los cinco relojes, rehecha por mi)
    suma de los cinco relojes               : 1635.2 s
    media sobre 5                           : 327.0 s
    suma mas la prueba de 93 s              : 1728.2 s
    eso en minutos                          : 28.80 min
    lo que el reporte publica               : 29,5 min
    segundos que harian falta para 29,5 min : 1770.0 s

Esa salida mide la suma de los cinco relojes leidos de `.v51/reloj_c*.txt`, su media, su suma con los `93` s de la prueba de aceptacion, esa suma en minutos, y los segundos que harian falta para dar `29,5`.

`LECTURA`: **`1728,2` s son `28,80` min, y para dar `29,5` harian falta `1770,0`, o sea `41,8` s que no aparecen en ninguna otra cifra del reporte.** La celda **se contradice a si misma**: escribe el numerador y publica otro cociente. **No es una cifra de instrumento mal leida: es una division hecha a mano**, y por eso ni el tallado ni el censo pueden verla.

**LA SEDE ES `docs/loop/REPORTE.md`, asi que la especie es `REPORTE`** (`5.2`, que separa expresamente ese fichero de las demas sedes de `docs/`). **Y VIVE EN TABLA**, que es una de las tres formas que `5.2` dice que acumulan. **`REPORTE` sube de `0 de 3` a `1 de 3`.**

**LO QUE NO HAGO CON ELLA, y lo digo porque me lo pregunte:** no la rebajo a prosa por ser pequena. La cifra que dice si una vuelta cupo en su techo **es la que mide si el techo sirve**, y un techo calibrado con un `2,4` por ciento de error se lo come la vuelta siguiente sin que nadie lo vea. **Y no toco su otra mitad**: el `6` de `6` de pasadas es correcto y lo verifique de los seis informes.

**RELECTURA AL DOBLE DEL TRAMO** (`5.2`): remedi **las diecinueve** cifras de `MM.4.f` una a una. `NO MEDIDO`, `253,2`, `374,4`, `339,8`, `317,1`, `350,7`, los vecinos `0`, `0`, `1`, `1`, `3`, `4`, las poblaciones `394` a `399`, `6` pasadas, `5` con reloj, `1635,2`, `327,0`, `461,3`, `-29,1`, `menor 0 mayor 4 suma 9`, `374,4` contra `461,3`, el techo `6` de `6` y el `1728,2`. **Todas salen menos el `29,5`.**

### 50.4.b. **`72` RANCIOS DONDE EL INSTRUMENTO ESCRIBE `RANCIO 71`. PROSA, NO ACUMULA**

    $ grep -c "RANCIO" .v51/cerrar_reporte_raw.txt
    72
    $ grep -n "RANCIO" .v51/cerrar_reporte_raw.txt | head -1
    697:  RANCIO 71, SIN HUELLA 8
    $ python forja.py rancios | grep -c "^  \[RANCIO\]"
    71

Esas salidas miden lo que el `grep -c` del reporte cuenta, cual es la primera de las lineas que cuenta, y cuantos hallazgos `[RANCIO]` imprime hoy el instrumento de la casa.

`LECTURA`: **el `grep -c` cuenta `72` lineas porque la primera de ellas es la linea de resumen del propio instrumento**, que escribe `RANCIO 71`. **La cifra `72` es cierta como recuento de lineas y falsa como recuento de rancios**, y el reporte la publica con la segunda frase: *`72` rancios*. **Es el ejemplar que `D.38.3` ensanchada nombra**: el instrumento esta pegado, la cifra que devuelve es cierta, y **lo falso es la frase**. Vive en **prosa de acompanamiento** de `MM.4.o`, no en tabla ni en cabecera ni en la conclusion de la vuelta, **asi que registra y NO acumula** (`5.2`).

**Y LO QUE LA FRASE AFIRMABA DE VERDAD SIGUE EN PIE, y lo mido para no cobrarle de mas:** `0` de los rancios de hoy nombra a ninguna de sus `9` fichas, comprobado ficha a ficha con sus nueve ids. **La conclusion es correcta; el denominador con el que se publica, no.**

**NO ES SUYA SOLA, Y LA OTRA MITAD ES MIA:** la vuelta 50 escribio el mismo `grep -c` y publico *la cola de vigencia sigue en `72`*, y **mi `ACTA 49` lo dio por bueno en su tabla de verificacion**. Lo declaro aqui: **aquel `72` tambien era `71`**, y quien no lo miro fui yo.

### 50.4.c. **`OCHO` FICHAS DONDE SU PROPIO PARENTESIS ENUMERA NUEVE. PROSA, NO ACUMULA**

`MM.4.a` escribe: *Las **ocho** fichas que toque por correccion declarada (`P38` en `MM.1`, `P6` y `P7` en `MM.2.h`, las cuatro con veredicto en `MM.2.e` y `P39` y `P41` en `MM.3`) siguen en la bandeja.*

    $ git diff --name-status 3061fc2 b04ac62 -- cuarentena/
    M  buscar_regularidad_bloques_iguales_trabajo_mando.json
    A  cubrir_indicadores_problemas_reunion_individual.json
    M  dimensionar_numero_subordinados_medio_dia_semanal.json
    A  fijar_duracion_lugar_reunion_individual.json
    A  fijar_frecuencia_reunion_individual_madurez_tarea.json
    A  infundir_regularidad_reunion_proceso.json
    A  preparar_guion_reunion_individual_subordinado.json
    M  preparar_respuestas_estandar_interrupciones_repetidas.json
    A  usar_tres_clases_reunion_proceso.json
    (9 ficheros: 6 nuevos y 3 modificados)

Esa salida mide que ficheros de `cuarentena/` cambian entre el commit de apertura de la vuelta 51 y el commit de cierre, y de que clase es cada cambio.

`LECTURA`: **`1` mas `2` mas `4` mas `2` dan `9`, no `8`**; `git` da `9`; y **el propio `MM.4.o` escribe `9` dos veces**. El reporte se contradice consigo mismo dentro de su misma seccion de cierre. Es **prosa de acompanamiento**, asi que **registra y NO acumula**, y es **la misma figura que la `ACTA 49` ya le cobro** (*`LL.0.a` dice tres minados y `LL.2.k` dice cuatro*): **una cifra tecleada dos veces en el mismo documento que sale distinta.**

### 50.4.d. **LO QUE COMPROBE ANTES DE DECIR QUE NO HAY MAS**

**No afirmo que no haya mas: afirmo lo que recorri.** Recompute las cifras de `MM.0`, `MM.1`, `MM.2`, `MM.3` y `MM.4` que tienen instrumento o aritmetica, que son las de `50.1.a` mas las diecinueve de `MM.4.f`; corri sus seis informes de aduana, sus dos instrumentos de tanda (`cola_lectura.py` y `por_que_0445.py`), su `pasos_inventados.py`, su `d028.py` y su `puerta.py`; reconstrui sus dos bases de tallado y de censo commit a commit; y compare su tabla de `PASOS INVENTADOS` con un conteo mio hecho por otro camino. **Lo que no hice: releer los `156` pasos de `cap_04` otra vez**, porque los firme en la `ACTA 49` y `MM.4.e` los publica como cierre y no como merito de hoy.

## 50.5. LAS ADJUDICACIONES

### 50.5.a. **LOS NUEVE DIGITOS DE SENIAL ESCRITOS DENTRO DEL TEXTO DEL QUE LA SENIAL SE CALCULA: NO ES CAIDA, Y ES LA TERCERA GENERACION DE `d038`**

**Lo medi en mi fase ciega, antes de leer el reporte**, y lo cierro hoy con el mecanismo a la vista:

    $ python .v51aud/44_crecimiento_ficha.py
    fijar_duracion_lugar_reunion_individual
       caracteres de resumen_teorico hoy       : 9123
       texto ANTES del primer bloque VEREDICTO : 6705    texto DESPUES : 2418
    fijar_frecuencia_reunion_individual_madurez_tarea
       caracteres de resumen_teorico hoy       : 9623
       texto ANTES del primer bloque VEREDICTO : 7217    texto DESPUES : 2406

    $ python .v51/por_que_0445.py      (SU instrumento, corrido por mi hoy)
    senial 1 TAL COMO LA ADUANA LA MIDE  : 0.550
    caracteres de resumen_teorico        : 9123 y 9623
    el resumen es el  90 y el 89 por ciento del texto que la senial 1 compara

La primera salida mide, en las dos fichas del par mas alto, cuantos caracteres tiene hoy su `resumen_teorico` y por donde lo parte su primer bloque `VEREDICTO`. La segunda es el instrumento del propio reporte corrido sobre el arbol de hoy.

`LECTURA`: **su instrumento publico `0.445`, `6704 y 7216` y `87 y 85 por ciento`, y hoy da `0.550`, `9123 y 9623` y `90 y 89`.** Y el corte lo explica entero: **`6705` y `7217` son exactamente donde empieza el bloque `VEREDICTO`**, o sea que **todo el crecimiento es el veredicto que la propia vuelta escribio despues de medir**. Lo mismo pasa con los nueve digitos de `MM.2.e`: **ninguno se reproduce**.

**ADJUDICO QUE NO ES CAIDA DE NINGUNA ESPECIE, y con las reglas escritas:**

| | |
|---|---|
| **no es `CLASE`** | las sedes de `CLASE` son `bitacora/VEREDICTOS.jsonl`, `config/pares_mutuos.jsonl` y el dataset (`5.2`), y **ninguna se movio**. Ademas los nueve veredictos se sostienen releidos, `50.7` |
| **no es `CIFRA PUBLICADA`** | la sede del digito es la ficha de cuarentena, y **mi propia adjudicacion de `d027` dice que una ficha de cuarentena no es sede de `5.2`** |
| **no es `REPORTE`** | lo que el reporte pega es la salida literal de su instrumento en el momento en que lo corrio, y el tallado lo confirma. **La cifra era cierta cuando se midio, y lo que explica es una medida de ese mismo momento** |

**PERO SE COBRA EL DIA DE LA INSERCION, y por eso va ENCARGADA y no solo agendada:** el dia que estas seis fichas entren, su veredicto se escribira en `bitacora/VEREDICTOS.jsonl` **con un digito que ya no es el de ningun texto vivo**, y `D.15` no podra avisar, porque compara huellas de la bitacora y ahi todavia no hay nada que comparar. **La frase que lo resuelve la escribio el propio extractor al pagar `d044`**, y se la devuelvo literal: *un comando escrito dentro de su propia poblacion no se arregla afinandolo, se arregla sacandolo.* **El digito es el mismo caso que el comando.** Es la `TAREA 3` del encargo y queda anotada en `DEUDA.jsonl`.

### 50.5.b. **LA FRONTERA QUE NINGUNA MAQUINA DE ESTA CASA VA A LEVANTAR, Y QUE SU FICHA NO NOMBRA**

**La encontre en mi fase ciega leyendo los pasos, no siguiendo una senial** (`D.19`), y la cierro hoy con la medida al lado:

    $ python .v51aud/10_vecinos_zhuo.py      (los dos pasos, impresos de sus ficheros)
      paso 1 de cubrir_indicadores_problemas_reunion_individual (cuarentena, cap_05 L43):
        Empieza por las cifras de rendimiento, o sea los indicadores que usa el subordinado,
        como los ritmos de pedidos entrantes, la produccion o el estado de los proyectos.
      paso 4 de dirigir_reunion_individual_semanal (dataset/nodos.jsonl, zhuo_manager):
        Centrala en tu persona a cargo y en lo que la ayudaria a tener mas exito, no en ti y
        en lo que tu necesitas. Si lo que buscas es un parte de situacion, usa otro canal.

    $ python .v51aud/28_pares_cruzados.py    (la senial de la casa, 18 pares cruzados de libro)
    cubrir_indicadores_problemas_reunion_individual  dirigir_reunion_individual_semanal  0.1125 no
    ... los 18 entre 0.0617 y 0.1715, umbral 0.35, NINGUNO pasa

    $ python .v51aud/11_quien_nombra_a_quien.py
    cubrir_indicadores_problemas_reunion_individual    dirigir_reun:0  preguntar_co:1  auditar_cale:0

Esas salidas miden los dos pasos literales de sus respectivos ficheros, la senial de la casa entre cada candidato de `cap_05` y cada uno de los tres nodos de `zhuo_manager` del grafo, y cuantas veces cada candidato escribe el id de cada uno de esos tres.

`LECTURA`: **los dos nodos mandan cosas contrarias sobre con que se empieza la misma reunion**: uno manda empezar por los indicadores y el estado de los proyectos, y el otro manda sacar el parte de situacion de esa reunion y llevarlo a otro canal. **La senial los deja en `0,1125` con el umbral en `0,35`, y en la misma tanda dos pares de hermanos miden `0,5501` y `0,5298`**: la maquina ordena por como esta escrito el texto, no por lo que el texto manda hacer. **Y la ficha que protagoniza la contradiccion es la unica de las cuatro del uno a uno que NO nombra a ese vecino.**

**ADJUDICO, con la vara de `6.1`:** esto **no es duplicado y no es caida de nadie**. Es la fila *DOS DOCTRINAS LEGITIMAS NO SON DUPLICADO: son FRONTERA DECLARADA*, y la vara manda **escribir las dos posiciones con sus fuentes**, no fundirlas. **Y adjudico a favor de la vuelta lo que va a su favor**: sus otras cuatro fichas declararon arista de contraste contra `zhuo_manager` **sin que ninguna senial se lo pidiera**, que es leer los vecinos en vez de obedecer a la maquina (`D.19`, manual principio `4`).

**LO QUE FALTA ES UNA SOLA FICHA Y ES PROSA**, asi que va encargada como `TAREA 4` y anotada en `DEUDA.jsonl`. **Y no abro doctrina con ello** (`D.56`): la regla que lo cubre ya esta escrita en `6.1`.

### 50.5.c. **LOS TRES PAGOS DE DEUDA CIERRAN LOS TRES, Y LO FIRMO**

    $ python .v51aud/50_pagos.py
    d044  el viejo es PREFIJO del nuevo                     : True
    d044  veces que aparece 'grep' EN ELLA                  : 0
    d044  veces que aparece 'Sale de la PIEZA P34' EN ELLA  : 0
    d044  la LINEA DE PAGO de DEUDA.jsonl contiene esa cadena: False
    metodo nuevo sobre los 50 ficheros de la bandeja de HOY:
      declaran 'P34' en su CABECERA: 2   declaran 'P38' en su CABECERA: 1
    d045  claves que cambian ['resumen_teorico']  pasos: True  titulo: True  atribuciones: True
    d046  claves que cambian ['resumen_teorico']  pasos: True  titulo: True  atribuciones: True

Esa salida mide, sobre el arbol de hoy: si la correccion de `P38` anade sin borrar y si contiene el comando que la rompio, si la linea de pago de `DEUDA.jsonl` contiene esa cadena, que da el metodo nuevo sobre la bandeja entera, y que claves y campos cambian en las dos fichas de `d045` y `d046`.

`LECTURA`: **`d044` cierra, y cierra por donde tenia que cerrar.** El comando viejo sigue dando `3` y **eso no lo puede evitar nadie**, porque el principio `6` prohibe borrar las lineas viejas; lo que cambio es que **la afirmacion ya no cuelga de ese numero**: se lee sola, con sus dos ids escritos, y **el metodo que la comprueba ancla en la frase de cabecera y da `2` y `1` sobre una bandeja de `50`**. **Y la linea de pago de `DEUDA.jsonl`, que es la sede que se rompio la vez anterior, ya no lleva la cadena dentro.** `d045` y `d046` cierran igual: **anaden y no borran, y no mueven ni un paso, ni un titulo, ni una atribucion**, comprobado por diferencia y no por promesa. **Las tres PAGADAS, y lo firmo.**

### 50.5.d. **LA CUARTA LINEA DEL SELLO DE `D.52` YA NO REPRODUCE, Y ESO LE DA LA RAZON**

    $ git log -1 --format="%h" -- docs/loop/TABLA_DE_CIERRE.txt
    b04ac62                                        (el reporte publica 216b114)
    $ git show 216b114:docs/loop/TABLA_DE_CIERRE.txt | git hash-object --stdin
    3b39a3fd477a02d14ec5cdefb97255e689ae713c
    $ git hash-object docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_v50.txt
    3b39a3fd477a02d14ec5cdefb97255e689ae713c
    $ git show HEAD:docs/loop/TABLA_DE_CIERRE.txt | git hash-object --stdin
    984dab3b09068c22d1a93459fbb54f7f2ce8517a       (el reporte publica 3b39a3fd)

Esas salidas miden el commit que escribio hoy la tabla de cierre, el sello de la version de la vuelta 50 sacada de `216b114`, el de la copia archivada, y el de la version que `HEAD` tiene ahora.

`LECTURA`: **las dos lineas que sostienen el sello reproducen identicas**, asi que la copia archivada **es** la salida y no una transcripcion. **Las otras dos ya no**, y eso **no es caida sino el ejemplar que `d047` pedia**: el reporte publico la cuarta linea avisando de que manana no coincidiria, **y no coincide**. **Adjudico `d047` DEMOSTRADA con su ejemplar**; sigue sin pagarse porque `D.45` nos deja fuera a los dos, y **la cita buena es la del commit**, que es lo que el propio reporte hizo.

### 50.5.e. **`0` CHOQUES EN SEIS PASADAS DE UN CANDIDATO CADA UNA: ES CIERTO Y NO PUEDE SER OTRA COSA**

El campo `CHOCAN entre si dentro del lote` mide choques **dentro de la misma pasada**, y las seis pasadas llevaron **un** candidato cada una. **Asi que ese `0` no puede salir distinto y no mide nada de esta tanda.** Lo que si midio los cruces entre los seis fue **la poblacion creciente**: cada candidato barrio contra los anteriores, y de ahi salieron los `9` pares de cola. **No es caida**, porque el reporte pega el campo del informe tal cual; **lo dejo registrado para que nadie lo lea como una medida de ausencia de choques.**

### 50.5.f. **`P12` COMO UN NODO ES CIFRA MIA, Y LO DECLARO EN VEZ DE CARGARSELO A EL**

Mi encargo de la vuelta 51 escribe `P12 | L37 a L39 | 1 | cuanto dura y donde`. **El extractor siguio mi tabla**, y su discutible `7` dice que lo haria en dos con el corte entre el paso `4` y el `5`. **`L37` contesta a `How long` y `L39` a `Where`, que son dos preguntas distintas del libro**, y el titulo del nodo lleva una `y` que las junta.

**NO LO PARTO HOY y digo por que:** la ficha esta escrita, pasada por su aduana y con su veredicto dentro, y partirla ahora costaria dos pasadas nuevas y reabriria la frontera que mi propio encargo prohibio reabrir. **Lo dejo medido aqui y anotado en `DEUDA.jsonl`**, para que se decida **el dia de la insercion**, que es cuando el corte vuelve a ser barato. **La cifra es mia y la carga es mia**, no suya.

### 50.5.g. **LO QUE REGISTRO Y NO ADJUDICO** (`D.56`, la cola de doctrina sigue congelada en `11`)

    $ python .v51aud/54_matriz_senial.py
    pares DIRIGIDOS de los seis entre si, en total          : 30
    los que la ADUANA levanto en el acto                    : 9
    los que estan por encima del umbral HOY                 : 17
    los que mi barrido de la fase ciega conto (AC.7)        : 17
    cubrir contra infundir : 0.3442 desde un lado y 0.3507 desde el otro (umbral 0.3500)

Esa salida mide la matriz dirigida de la senial `1` de la casa entre los seis candidatos sobre las fichas de hoy, cuantos de esos `30` pares dirigidos estan por encima del umbral, y cuantos levanto la aduana en el acto.

| # | lo que medi | su cifra | por que lo dejo ahi |
|---:|---|---|---|
| `1` | **mi barrido de la fase ciega y la aduana miden lo mismo, y la diferencia es de DIRECCION y no de pares** | los `9` de la aduana y los `17` mios son **los mismos `9` pares sin orden**, contados en las dos direcciones menos una que hoy cae por debajo. `30` dirigidos posibles, `9` levantados en el acto, `17` por encima hoy | **es el cruce que `D.38.5` me manda hacer, y sale sin discrepancia de sustancia.** No abre nada |
| `2` | **la senial de esta casa no es simetrica, y un par de esta tanda cae a los dos lados del umbral** | `cubrir` contra `infundir` da `0,3442` desde un lado y `0,3507` desde el otro, con el umbral en `0,3500` en medio | mover un umbral me esta vedado y la doctrina esta congelada. **Queda con su cifra** |

## 50.6. `PASOS INVENTADOS POR CAPITULO` (`AUDITOR_FORJA.md` 8). **UNA FILA POR CAPITULO, Y CONTADA POR MI**

**`8.3` me obliga a contar yo el denominador y a no copiarlo. Lo cuento por otro camino que el suyo**: el mio recorre bandeja mas `_insertados` mas el grafo y saca el capitulo **del fichero fuente que la ficha cita**; el suyo recorre las dos carpetas y saca la unidad **de la frase de cabecera del `resumen_teorico`**.

    $ python .v51aud/43_pasos_sin_doble.py
    ids del libro en dataset/nodos.jsonl        : 1 ['revisar_tres_preguntas_valor_carrera']
    capitulo         fichas    pasos
    cap_01                1        7
    cap_02                7       50
    cap_03               15      121
    cap_04               22      156
    cap_05                6       49
    TOTAL                51      383

Esa salida mide, por capitulo de `grove_high_output`, cuantas fichas hay en la poblacion entera del libro y cuantos elementos suman sus `pasos_accionables`, contando una sola vez el unico id que vive a la vez en `_insertados` y en el grafo.

| capitulo | fichas | pasos escritos | PUENTE | `PASOS INVENTADOS` |
|---|---:|---:|---:|---:|
| `cap_01`, que su instrumento llama `Introduction` | `1` | `7` | `0` | **`0` de `7`, `0,00` por ciento** |
| `cap_02` | `7` | `50` | `0` | **`0` de `50`, `0,00` por ciento** |
| `cap_03` | `15` | `121` | `0` | **`0` de `121`, `0,00` por ciento** |
| `cap_04` | `22` | `156` | `0` | **`0` de `156`, `0,00` por ciento**, cerrado |
| `cap_05` | `6` | `49` | `0` | **`0` de `49`, `0,00` por ciento**, parcial: `6` de `26` nodos |
| **TODO el lote 7** | **`51`** | **`383`** | **`0`** | **`0` de `383`, `0,00` por ciento** |

`LECTURA`: **las seis filas me salen identicas a las suyas**, y la unica diferencia es el nombre de la primera: su instrumento la llama `Introduction` porque lee la unidad que la ficha declara, y el mio la llama `cap_01` porque lee el fichero que la ficha cita. **Es la misma ficha y los mismos `7` pasos.** `8.3.2` me manda releer una muestra de los marcados TRANSCRIPCION contra su parrafo, **y en `cap_05` no hay muestra: relei los `49`**, uno a uno contra sus ocho renglones, en mi fase ciega y antes de ver su tabla. **FIRMO el `0` de `49`.**

**LO QUE ESTA CIFRA DICE DEL VOLUMEN** (`8.1`): `cap_05` estrena en `0,00` por ciento, **muy por debajo del tope de `10`**, y el peor capitulo del lote es tambien `0,00`. **Por la tabla de `8.1` eso autoriza subir un escalon.** Digo en `50.11` por que no lo aplico tal cual: **el techo de candidatos manda cuando los dos chocan** (`EXTRACTOR.md` 12.4), y `cap_05` va por `6` de `26`.

**Y DIGO QUE CAPITULO ERA**, que es lo que `8.4` pide: `cap_05` es el capitulo de las reuniones, y **el autor lo escribe en preguntas y respuestas** (`How often`, `How long`, `Where`, `What should be covered`), o sea **en procedimiento ya ordenado**. Un `0,00` por ciento aqui mide menos merito que el mismo `0,00` en un capitulo de prosa corrida, y esa es la mitad de `8.4` que nadie puede medir con una cifra.

## 50.7. LA MUESTRA PINEADA DE LOS SANOS (`AUDITOR_FORJA.md` 7)

**LA POBLACION DE ESTA TANDA ES CERO EN LA BITACORA Y NUEVE EN LAS FICHAS, y lo digo antes de elegir muestra:** `bitacora/VEREDICTOS.jsonl` no se movio (`740` contra `740`), asi que **la tanda no escribio ni un `SANO` en la sede que esta seccion nombra.** Los nueve estan dentro de las fichas que viajan, que es su discutible `13`.

    $ python .v51aud/52_sanos.py
    veredictos escritos dentro de las seis fichas : 9
    SANO                                          : 9
    con RAZON escrita detras                      : 9

    $ python .v51aud/53_banda.py
     0 de  9 caen  ->  tasa 0.0000   banda de Wilson 95%: [0.0000, 0.2992]
     0 de 21 caen  ->  tasa 0.0000   banda de Wilson 95%: [0.0000, 0.1546]

La primera salida mide cuantos bloques `VEREDICTO <clase> sobre el vecino <id>` llevan dentro las seis fichas de `cap_05`, cuantos son `SANO`, y cuantos traen texto de razon detras de la clase. La segunda mide la banda de Wilson al `95` por ciento de `0` caidas sobre `9` y sobre `21`.

| | |
|---|---|
| **cuantos habia** | `9` |
| **cuantos releo** | **los `9`**, o sea la poblacion entera. La muestra que `7` pide seria `3` (el mayor entre `3` y el `20` por ciento de `9`), y **la supero porque ya los habia leido enteros en mi fase ciega**, con los dos extremos de cada par delante |
| **como los eligo** | **no elijo: releo todos**, asi que no hay semilla que escribir y lo digo en vez de inventar una |
| **cuantos se sostienen** | **`9`**. Los seis candidatos contestan a seis preguntas distintas del libro sobre la misma reunion, y **`0` pasos literalmente comunes y `0` lineas del libro compartidas** lo sostienen por el otro lado |
| **cuantos caen** | **`0`** |
| **la tasa con su banda** | **`0,0000`**, banda de Wilson al `95` por ciento **`[0,0000, 0,2992]`** sobre `9`. Y sobre los `21` pares que mire en la fase ciega, **`0,0000`** con banda **`[0,0000, 0,1546]`** |
| **`D.8`, un `SANO` sin razon escrita** | **`0` de `9`.** Los nueve llevan `RAZON:` con su par emparejado y su medida |

`LECTURA`: **la banda es ancha y lo digo en vez de venderla como un cero**: con `9` relecturas y ninguna caida, lo que queda medido es que **la tasa de dejar pasar de esta tanda no llega al `30` por ciento**, que no es una garantia. **Una tasa sin banda es media cifra, y una banda de `0,30` es una cifra que pide mas poblacion**, no una que cierre el asunto.
