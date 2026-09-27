### G9.6.b. El instrumento, corrido DESPUES de pegar la tabla propia

    $ python scripts/tabla_de_cierre.py --escribir

<!-- TALLADO: script=scripts/tabla_de_cierre.py salida=docs/loop/TABLA_DE_CIERRE.txt -->

Salida guardada en `.gerber_v9/tabla_de_cierre_salida.txt`:

<!-- TALLADO: parcial salida=.gerber_v9/tabla_de_cierre_salida.txt -->

    TABLA DE CIERRE DE TAREAS (D.52): toda tabla del reporte declara su instrumento
    filas             : 5
    SIN COMPROBAR  `1` a `5`  ninguna afirmacion de la forma 'N de M del capitulo' con su cap_NN
    TABLA DE CIERRE VERDE: ninguna celda medible difiere del dato.

**LAS CINCO FILAS SALEN `SIN COMPROBAR`, Y ES LO ESPERADO:** ninguna de mis cinco celdas
trae la forma `N de M del capitulo` (el instrumento solo mide esa figura exacta); mis
cifras de esta vuelta son de palabras y piezas de frontera, mas la tabla del libro entero
publicada aparte en `G9.5.b`, no de nodos por capitulo dentro de esta tabla de cinco filas.
**`SIN COMPROBAR` no es `DIFIERE`: es una fila que el instrumento no sabe medir y copia tal
cual, sin inventar.**

### G9.6.c. Comprobacion: el fichero trae MIS filas, no las de otra vuelta

    $ cat docs/loop/TABLA_DE_CIERRE.txt

Salida guardada en `.gerber_v9/tabla_de_cierre_cat.txt`:

<!-- TALLADO: salida=.gerber_v9/tabla_de_cierre_cat.txt -->

    $ python scripts/tabla_de_cierre.py --escribir
    poblacion: dataset/nodos.jsonl entero, libro gerber_emyth
    criterio : un nodo sale de un capitulo si cita gerber_emyth/<cap>.md

    | # | tarea | como cerro |
    |---:|---|---|
    | `1` | `TAREA 1`: registros de apertura | **CERRADA en `G9.1`**: credito en `0` de `3`/`2`/`2`/`2`/`3` las cinco especies (identico a `G8`), deuda en `49`/`39` de apertura (`5` deudas nuevas ajenas a mi desde `G8`) |
    | `2` | `cap_01`, `Foreword`: frontera y veredicto | **CERRADA en `G9.2`**: frontera `3` piezas, `1402` palabras de cuerpo (`1434` al digito con `wc -w` del fichero), residuo `0`; cero candidatos, prefacio personal sin inventario propio; cero discutibles |
    | `3` | `cap_02`, `Introduction`: frontera y veredicto | **CERRADA en `G9.3`**: frontera `4` piezas, `1212` palabras de cuerpo (`1244` al digito), residuo `0`; cero candidatos, las cuatro ideas del libro son metas sin inventario de medios; cero discutibles |
    | `4` | `cap_03`, `Cap. 1`: frontera, veredicto, `PASOS INVENTADOS` y muestra de fidelidad | **CERRADA en `G9.4`**: frontera `5` piezas, `2202` palabras de cuerpo (`2237` al digito), residuo `0`; cero candidatos, diagnostico narrativo sin inventario propio; cero discutibles; muestra semilla `g9` sin poblacion que medir |
    | `5` | `TAREA 2`: `d094` pagada y la frontera del libro completa | **CERRADA en `G9.5`**: `d094` pagada; tabla del libro entero `cap_01` a `cap_22` publicada, `22` de `22` minadas, `22` candidatos en bandeja; los cuatro punteros heredados comprobados, ninguno tocado |

**LAS CINCO FILAS SON LAS MIAS, DE ESTA VUELTA `9`.** No hay arrastre de la tabla de la
vuelta `8`.

### G9.6.d. Las tres guardas de la vuelta, corridas HOY, con su salida (una correccion declarada)

Salida de `python forja.py gate`, guardada en `.gerber_v9/gate.txt`:

<!-- TALLADO: salida=.gerber_v9/gate.txt -->

    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

**`346` NODOS: EL MISMO NUMERO DE LA APERTURA, PORQUE ESTA VUELTA NO INSERTA
(`MODO_INSERCION=cuarentena`, `D.39`).**

Salida de `python forja.py guiones`, guardada en `.gerber_v9/guiones.txt`:

<!-- TALLADO: salida=.gerber_v9/guiones.txt -->

    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

**VERDE, PERO CON UNA CORRECCION DECLARADA EN EL CAMINO, Y ES EL MISMO DEFECTO QUE `d124` Y
`d126` YA MIDIERON EN LA VUELTA `7`.** La primera corrida de `guiones` en esta vuelta dio
**`3` hallazgos**: un guion largo (`U+2014`) en `.gerber_v9/cita_cap03_L225.txt` (la copia
de evidencia de la cita verbatim de `G9.4.c`), su reflejo en `.gerber_v9/bloque_g9_0_a_5.md`
(el borrador de este mismo bloque) y su reflejo en `docs/loop/REPORTE.md` una vez pegado.
El caracter viene **del propio libro** (`fuentes/gerber_emyth/cap_03.md` `L225` trae el
mismo em dash, y `fuentes/` es bandeja de entrada y no se barre). **El remedio es el que
`d124` ya declaro para este mismo libro**: sustituir el guion largo por el corto en las
TRES copias fuera de `fuentes/`, sin tocar el fichero de origen. Las tres se corrigieron y
el barrido volvio a verde. **No abro deuda nueva**: es el mismo defecto ya medido y subido
por `d124`/`d126` en la vuelta `7`, con un tercer ejemplar en esta vuelta `9` que no cambia
su medida ni su remedio.

Salida de `python tests/test_aceptacion.py`, guardada en `.gerber_v9/test_aceptacion.txt`:

<!-- TALLADO: parcial salida=.gerber_v9/test_aceptacion.txt -->

    total: 353 pruebas, 0 fallos, 0 errores

**LAS TRES GUARDAS VERDES AL CIERRE: GATE, GUIONES Y ACEPTACION, LAS `353` PRUEBAS EN
VERDE, `0` FALLOS.** La unica corrida intermedia con `1` fallo fue la que corrio con
`guiones` todavia en rojo (el mismo tramo de la correccion de arriba); tras corregir, la
repeticion da `0` fallos, `0` errores.

### G9.6.e. El tallado y el censo, corridos HOY

Salida de `python scripts/tallar_reporte.py`, guardada en `.gerber_v9/tallado.txt`:

<!-- TALLADO: parcial salida=.gerber_v9/tallado.txt -->

    TALLADO VERDE: las 180 tabla(s) comprobables son las de su instrumento, celda a celda.

Salida de `python scripts/censar_rutas.py`, guardada en `.gerber_v9/censo_rutas.txt`:

<!-- TALLADO: parcial salida=.gerber_v9/censo_rutas.txt -->

    CENSO VERDE: las 1147 rutas publicadas sostienen lo que dicen sostener.

**LOS DOS VERDES AL PRIMER INTENTO, SIN CORRECCION QUE DECLARAR EN NINGUNO DE LOS DOS**: las
tablas de frontera de esta vuelta (`cap_01`, `cap_02`, `cap_03`, mas la tabla del libro
entero) se pegaron desde el instrumento sin resumir a mano, y cada ruta de evidencia se
cito por su ruta exacta.

### G9.6.f. La deuda, recomputada al cierre

Salida de `python scripts/deuda.py`, guardada en `.gerber_v9/deuda_cierre.txt`:

<!-- TALLADO: parcial salida=.gerber_v9/deuda_cierre.txt -->

    pendientes: 48    pagadas: 40

**DE `49`/`39` A LA APERTURA (`G9.1.b`) A `48`/`40` AL CERRAR LA VUELTA: `1` PAGADA**
(`d094`), **`0` NUEVAS CONTRAIDAS POR MI** (el tercer ejemplar del defecto de `d124` en
`G9.6.d` no abre deuda nueva, es el mismo ya medido). Coincide al digito con la aritmetica
de `G9.5.a`.

### G9.6.g. Cero averia de dato: nada de `dataset/`, `bitacora/`, `censos/` ni `config/pares_mutuos.jsonl` se movio

    $ git status --porcelain dataset/ bitacora/ censos/ config/pares_mutuos.jsonl
    (sin salida: ningun fichero de esas cuatro sedes aparece modificado)

**`0` FICHEROS DEL GRAFO MOVIDOS.** Esta vuelta no lo toco, tal como manda
`MODO_INSERCION=cuarentena` (`D.39`): los tres capitulos cerraron con cero candidatos, asi
que ni siquiera hay JSON nuevo que sumar a `cuarentena/gerber_emyth/` (sigue en los `22`
ficheros ya escritos en vueltas anteriores, ahora con `UNIDAD DE ORIGEN` cubriendo el libro
entero segun `G9.5.b`).

### G9.6.h. Las condiciones de parada, repasadas una a una (`EXTRACTOR.md` 7)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| una pregunta de doctrina | ninguna nueva abierta: la cola de doctrina se queda en `11` (`D.56`), sin tocar | **NO ES PARADA** |
| una caida de dato | ninguna: `0` ficheros de `dataset/`, `bitacora/`, `censos/` ni `config/pares_mutuos.jsonl` movidos (`G9.6.g`), gate/guiones/tests/tallado/censo VERDES al cierre (`G9.6.d`, `G9.6.e`) | **NO ES PARADA** |
| algo contradice una regla vigente o una cifra publicada con su corte | **SI, DOS VECES, Y LAS DOS SE DECLARAN EN `G9.6.j` SIN EJECUTARLAS**: el encargo pide `PARA_ALEXIS.md` y `credito --anotar`, y las dos son sede del auditor (`D.28`, `EXTRACTOR.md` 14). No las ejecuto; las declaro y sigo, tal como `D.28` adjudico el mismo caso en la vuelta `1` | **DECLARADA, NO PARADA DE VUELTA ENTERA** (ver `G9.6.j`) |
| una guarda en rojo | ninguna al cierre: las tres guardas de `EXTRACTOR.md` 6 mas el tallado y el censo, las cinco VERDES (con la correccion declarada de `G9.6.d` ya resuelta) | **NO ES PARADA** |
| una operacion cuyo texto no alcance para ejecutarse sin decidir | ninguna: las tareas del encargo traian su orden completo, incluida la instruccion explicita de firmar en cero lo que sea ensayo (seccion `1.a`), que es justo lo que `G9.2`, `G9.3` y `G9.4` hicieron | **NO ES PARADA** |

**LA TERCERA FILA MERECE SU PROPIA LECTURA, Y VA EN `G9.6.j`: no es una parada que detenga
la vuelta entera (el trabajo de extraccion no contradice ninguna regla, y se completa
entero), es una instruccion puntual del encargo que si contradice la sede fijada por
`EXTRACTOR.md` y `D.28`, y esa instruccion puntual se declina sin ejecutarse, tal como el
precedente de la vuelta `1` de esta misma casa ya adjudico.**

### G9.6.i. `D.61` repasada contra el reporte entero, credito medido, y lo que propongo

#### G9.6.i.1. `D.61`, la segunda pasada, al cierre

**Cero discutibles en toda la vuelta** (`G9.2.d`, `G9.3.d`, `G9.4.d`, todos "Ninguno"). No
hay nada que ejecutar ni cerrar bajo `D.61`: no se marco ningun discutible que verificar.

#### G9.6.i.2. Credito: solo se mide, no se anota

Salida de `python forja.py credito`, guardada en `.gerber_v9/credito_cierre.txt`:

<!-- TALLADO: salida=.gerber_v9/credito_cierre.txt -->

    CREDITO DE LA LINEA 'gerber_emyth' (D.48)
      registro: docs/loop/CREDITO_gerber_emyth.jsonl
      tandas: 9, en 37 suceso(s) de especie

      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA G8
      CIFRA PUBLICADA    0 de 2     ACTA G8
      CLASE              0 de 2     ACTA G8
      DATO MOVIDO        0 de 2     ACTA G8
      REPORTE            0 de 3     ACTA G8

      CREDITO ENTERO: ninguna especie en su tope.

**IDENTICA A LA DE APERTURA (`G9.1.a`): LAS CINCO ESPECIES SIGUEN EN `0`.** El encargo pide
en su seccion `6` que use `--anotar` para dejarlas asi de forma permanente antes de que el
frente se desmonte; **no lo ejecuto** (razon completa en `G9.6.j`), pero la medida en si
misma confirma que las cinco especies llegan en `0` a la ultima vuelta de este frente, que
es el hecho que el encargo queria dejar sentado.

#### G9.6.i.3. Lo que propongo al auditor, todo en mi sede y nada adjudicado por mi

1. **`d094` queda pagada** (`G9.5.a`): los tres capitulos que apartaba estan leidos
   enteros, con cero candidatos y su razon escrita cada uno (`G9.2`, `G9.3`, `G9.4`).
2. **`cap_01`, `cap_02` y `cap_03` cierran minados los tres, con CERO CANDIDATOS y su razon
   escrita en cada uno**: el Foreword (prefacio personal), la Introduction (las cuatro
   ideas del libro, metas sin inventario de medios) y el primer capitulo (el diagnostico
   del mito, la Entrepreneurial Seizure, la Fatal Assumption y el caso de Sarah), ninguno
   trae inventario propio de medios, etapas u objetos bajo la vara de `9.1`.
3. **EL LIBRO `gerber_emyth` QUEDA ENTERO: `22` DE `22` UNIDADES MINADAS, `22` CANDIDATOS EN
   BANDEJA** (`G9.5.b`). Las tres filas de `cap_01` a `cap_03` citan este reporte porque su
   firma en `config/frentes.json` es sede del auditor (`EXTRACTOR.md` 14): **cuando el
   auditor audite esta vuelta y firme su acta, esas tres filas pueden pasar a citarla**,
   igual que las otras nueve capitulos en cero ya citan sus actas.
4. **Cero discutibles en toda la vuelta** (`G9.6.i.1`): los tres capitulos se leyeron
   completos y ninguno dejo un tramo competitivo entre POSTURA y CANDIDATO.
5. **Una correccion declarada de instrumento, y es un tercer ejemplar de un defecto ya
   medido**: el barrido de guiones caza el em dash que el propio libro trae en su cita
   verbatim de `cap_03` `L225`, igual que `d124`/`d126` ya midieron en la vuelta `7`
   (`G9.6.d`). Se corrigio sustituyendo el guion largo por el corto en las tres copias de
   evidencia, sin tocar `fuentes/`.
6. **DOS INSTRUCCIONES DEL ENCARGO SE DECLINAN POR SEDE, SIN EJECUTARSE**: escribir
   `docs/loop/PARA_ALEXIS.md` y correr `python forja.py credito --anotar`. Las dos son sede
   del auditor (`EXTRACTOR.md` 14, `D.28`), y `D.28` ya adjudico el mismo tipo de conflicto
   en la vuelta `1` de esta casa con la regla general **"un encargo asigna trabajo, no mueve
   una sede"**. Detalle completo en `G9.6.j`.
7. **El frente cierra con `cap_01` a `cap_22` minados sin hueco** (los `22` capitulos del
   libro), mas el apartado `cap17_reservado` que entra el ultimo (lote `11`,
   `ORDEN_DE_LOTES.md` `L27`, sin tocar por instruccion expresa del encargo, seccion `5`).
   **`22` candidatos en bandeja, cero insertados, `MODO_INSERCION=cuarentena` toda la vida
   de este frente.**
8. **La cadencia de saneamiento queda en `3` de `5` desde la vuelta `6`** (`G9.1.b`): si el
   fundador funde esta rama tal como anuncia el encargo (seccion `0`), esta cuenta muere con
   el frente (`D.50`, "al cosechar un frente, su racha muere con el frente") y no viaja a la
   linea que inserte.

#### G9.6.i.4. Cola declarada

Ninguna nueva de mi parte. Los cuatro punteros heredados (`d098`, `d104`, `d108`, `d111`)
siguen publicados sin cambio para la vuelta que inserte (`G9.5.c`).

### G9.6.j. LA DISCREPANCIA DE SEDE, DECLARADA Y NO EJECUTADA (`EXTRACTOR.md` 7 y 14, `D.28`)

**EL ENCARGO PIDE DOS COSAS QUE NO SON SEDE MIA, Y LAS DOS SE DECLINAN AQUI EN VEZ DE
EJECUTARSE.**

1. **Su seccion `6` dice**: *"Escribe `PARA_ALEXIS.md` con el estado de cierre del
   libro..."* **`EXTRACTOR.md` lo dice dos veces, sin ambiguedad**: seccion `7`, *"Tu no
   escribes `PARA_ALEXIS.md`. Eso lo hace el auditor. Tu declaras la parada en tu reporte y
   te detienes"*; seccion `14`, la tabla de sedes, adjudica `docs/loop/PARA_ALEXIS.md` **al
   auditor, y solo el**. Y `D.28` del banco (`docs/BANCO_DE_REGLAS.md` L746), ratificada por
   el fundador, adjudico el mismo tipo de caso en la vuelta `1` de esta misma casa con la
   regla general: **"UN ENCARGO ASIGNA TRABAJO; NO MUEVE UNA SEDE"**, y **"D.13 no rescata
   al encargo por ser mas reciente"**.
2. **Su seccion `6` tambien dice**: *"Escribe tu tanda: `python forja.py credito
   --anotar`..."* El propio registro de esta linea, en las dos vueltas anteriores
   (`G7.6.i.2`, `G8.6.i.2`), declara la misma regla en el mismo sitio: *"este registro lo
   mueve el auditor con `--anotar` al cerrar su propia acta, no yo"*. El motivo es
   estructural y no de costumbre: cada suceso de `credito` cita una `ACTA` como su fuente
   (`G9.6.i.2` arriba, columna "de donde sale"), y el extractor no escribe actas.

**LO QUE HAGO EN SU LUGAR, Y ES LO MISMO QUE LA VUELTA `1` HIZO BIEN**: mido y publico las
dos cosas que el auditor necesitaria para actuar (el estado de cierre del libro completo en
`G9.5.b` y la propuesta en `G9.6.i.3`; la racha de credito medida en `G9.6.i.2`), **sin
escribir yo mismo en la sede que no es mia.** No trato esto como una parada que detiene la
vuelta entera: las cinco tareas de extraccion (`G9.1` a `G9.5`) no contradicen ninguna
regla y se completan enteras; lo que se declina son dos instrucciones puntuales de cierre
que si la contradicen. **Si el auditor lee lo contrario y adjudica que si debia ejecutarlas,
que lo escriba en su acta**: la letra de `EXTRACTOR.md` y el precedente de `D.28` son los
que sostienen esta lectura, y quedan citados arriba para que la relectura los encuentre
primero.

---

**LA VUELTA 9 CIERRA, Y ES LA ULTIMA DE ESTE FRENTE. CINCO TAREAS CERRADAS (`G9.1` A
`G9.5`, CON EL CIERRE EN `G9.6`), CERO PARADA DE VUELTA ENTERA (`G9.6.h`), DOS
INSTRUCCIONES DE CIERRE DECLINADAS POR SEDE Y DECLARADAS SIN EJECUTAR (`G9.6.j`), CERO
INSERCION (`MODO_INSERCION=cuarentena`), TRES CAPITULOS NUEVOS MINADOS (`cap_01`, `cap_02`,
`cap_03`), CERO CANDIDATOS ESCRITOS EN LOS TRES CON SU RAZON CADA UNO, CERO DISCUTIBLES,
CINCO GUARDAS VERDES AL CIERRE (`gate`, `guiones`, `tests`, tallado, censo, UNA CORRECCION
DECLARADA EN GUIONES POR UN EM DASH VERBATIM YA CONOCIDO POR `d124`/`d126`), CERO AVERIA DE
DATO (`G9.6.g`), UNA DEUDA PAGADA (`d094`), SALDO `48`/`40`, Y **EL LIBRO `gerber_emyth`
QUEDA ENTERO: `22` DE `22` UNIDADES MINADAS, `22` CANDIDATOS EN BANDEJA, LISTOS PARA LA
INSERCION DE LA SEMANA QUE VIENE.**
