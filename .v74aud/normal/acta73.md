
# ACTA 73. VUELTA 74, lote 7 (`grove_high_output`), **CLASE SANEAMIENTO**: **LA VUELTA PAGA LO QUE SE LE PIDIO SIN MOVER UN BYTE Y SUS INSTRUMENTOS SE REPRODUCEN IDENTICOS; `d077` Y `d078` SE SOSTIENEN FICHA A FICHA. EN `cap_13` DE SCOTT LOS DOS LEIMOS UN PUENTE Y NO ERA EL MISMO: EL SUYO (`dar_elogio` PASO `17`, *HA MEDIDO*) LO GANA SU LECTURA, EL MIO (`dar_elogio` PASO `8`, *Y LA CRITICA NO*) SE LE ESCAPO FUERA DE SU MARCADO. SON `2` DE `70`, NO `1`. FIRMO LOS `70` PASOS Y `d084` CON `d006` QUEDAN PAGADAS CON LA CIFRA CORREGIDA; `REPORTE` SUBE A `2 de 3`. DOS PUENTES VIVEN EN EL GRAFO: LA GUARDA `D.30` ESTA EN ROJO Y SU CORRECCION POR `D.54` ES LA UNICA BLOQUEANTE DE LA `75`, QUE DESPUES INSERTA LAS `7` DE GROVE**

*Auditor `claude-opus-5-5`, 26 sep 2026, turno normal de la vuelta que el arnes numera `3` en la corrida que arranco el 25 a
las `21:43`. Linea **serial**, rama `extraccion-mundo-11`, hash auditado `6312424` (cierre del extractor, mas `7f6bf64` con la
salida del hook, sin trabajo nuevo), arbol en `05e588b` con mi apertura sellada. Modo austero (`D.47`). Toda mi evidencia de
este turno esta en `.v74aud/normal/`, y la de mi fase ciega en `.v74aud/`.*

## 73.0. **HUECO DE ACTA Y HERENCIA** (`1.0`, `D.40`)

**NO HAY HUECO.** La `ACTA 72` cubre la vuelta `73`; esta cubre la `74` entera: el turno del extractor (de `e76746f` a `7f6bf64`,
`03:26` a `03:59` del 26) y mi fase ciega, sellada en `05e588b`, que solo toca sus dos ficheros:

    $ sed -n '2,3p;9,10p' .v74aud/normal/censo.txt
    docs/loop/DEUDA.jsonl
    docs/loop/REPORTE.md
    docs/loop/APERTURA_CIEGA.md
    docs/loop/SELLOS_APERTURA.jsonl

(La primera pareja es lo que la vuelta movio fuera de `.v74ext/` entre `e76746f2` y `7f6bf647`; la segunda, lo que movio mi fase
ciega entre `7f6bf647` y `05e588bf`. Los comandos, enteros, en ese fichero.)

**HEREDADO 1, `R5` del extractor: CUMPLIDO.** Con mis copias sacadas con `sed` de los originales `.v64ext/pegado64.py` y
`.v64aud/normal/bloques_mudos.py`, no de las suyas, con la cabecera cambiada a la `74` (`3` y `2` lineas nuevas contra el original
con `diff --strip-trailing-cr`):

    $ cat .v74aud/normal/r5.txt
    bloques abiertos con `$` en el tramo de la vuelta 74 : 42
    bloques que ROMPEN R1 (ACTA 60 60.15)                : 0
    bloques abiertos con `$`: 15 | comandos `$`: 41 | comandos sin ninguna linea de salida en su bloque: 0

**Es lo que su `74.4.f` publica**, y la diferencia de uno entre los dos instrumentos la explica bien alli (una linea con `$` dentro
de la salida de un `sed` sobre mi acta). **HEREDADO 2, `R6`, y HEREDADO 3, `R7`, mios: CUMPLIDOS** en la fase ciega
(`APERTURA_CIEGA.md` `0` y `9`) **y `R7` en esta acta**: toda linea mia que reparte un total en clases la imprime un instrumento que
trae su `suma`. **HEREDADO 4, `R8`, mio: CUMPLIDO en el encargo de la `74`** (`APERTURA_CIEGA.md` `7`) y **medido sobre el de la
`75`** en `73.12`.

## 73.1. **LO QUE VERIFICO, CON MIS PROPIOS COMANDOS** (`1.1`)

    $ cat .v74aud/normal/gate.txt .v74aud/normal/guiones.txt .v74aud/normal/resolutor.txt
    GATE VERDE.
      nodos verificados: 430
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece
    rc=0
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    rc=0
    nodos vivos: 430
    nodos deprecados (archivo): 0
    alias registrados: 0
    rc=0
    $ grep 'total:' .v74aud/normal/suite.txt; tail -1 .v74aud/normal/suite.txt
      total: 379 pruebas, 0 fallos, 0 errores
    rc=0
    $ sed -n '11,$p' .v74aud/normal/censo.txt
    $ git diff --name-only eb9d0c04 HEAD -- dataset bitacora censos config esquema fuentes src scripts tests cuarentena forja.py | wc -l
    0
    $ git status --short -- dataset bitacora censos config esquema fuentes src scripts tests cuarentena | wc -l
    0
    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        430 dataset/nodos.jsonl
       1081 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1512 total
    cuarentena/grove_high_output 7
    cuarentena/_insertados/grove_high_output 85
    cuarentena/gerber_emyth 22
    cuarentena/marquet_turn_the_ship 20
    procesos 0
    $ python .v70aud/poblacion.py
    poblacion: 479 | por sede: {'grafo': 430, 'bandeja': 49} | suma: 479

**Es el censo de su `74.0` y su `74.4.a` al digito, el de mi `ACTA 72` `72.1` y el de mi apertura sellada**, y **ahora con `git`**,
que es lo que mi fase ciega no pudo medir (`APERTURA_CIEGA.md` `2`): **ni un fichero de dato, de codigo, de libro ni de bandeja
cambiado desde mi encargo de la `74` (`eb9d0c04`)**, ni commiteado ni en el arbol. **La bitacora tampoco**, que era lo unico que
mi fase ciega dejo sin huella.

**EL CIERRE ESTRICTO, CORRIDO POR MI:**

    $ grep -nE '^(CIERRE|CENSO|TALLADO|TABLA DE CIERRE)|DIFIEREN|CAEN  ' .v74aud/normal/cerrar_reporte.txt; tail -1 .v74aud/normal/cerrar_reporte.txt
    2:TALLADO DEL REPORTE (D.41): la tabla que dice ser de instrumento
    6:  que DIFIEREN de su instrumento: 0
    252:TALLADO VERDE: las 157 tabla(s) comprobables son las de su instrumento, celda a celda.
    254:CENSO DE RUTAS (D.42): la unidad de la ruta es la celda
    258:  CAEN                      : 0
    264:CENSO VERDE: las 1037 rutas publicadas sostienen lo que dicen sostener.
    266:TABLA DE CIERRE DE TAREAS (D.52): toda tabla del reporte declara su instrumento
    276:TABLA DE CIERRE VERDE: ninguna celda medible difiere del dato.
    1061:CIERRE VERDE: las cuatro guardas que muerden, el tallado y el censo. La vigencia corrio y publico su cuenta arriba: es cola, no guarda (D.15).
    rc=0

**VERDE, `rc=0`**, y `procesos/` vacio despues de mi suite y de mi cierre. **Cuenta `1037` rutas**, contra `1034` de su segunda
corrida y `1035` de su hook; **no descompongo la diferencia**: el arbol no es el mismo (despues entro mi apertura sellada), y lo que se
mide es que ninguna cae.

**LO QUE REPRODUZCO DE SU TRAMO**, corriendo sus instrumentos contra sus salidas guardadas, y mis huellas de la `73`:

    $ cat .v74aud/normal/reproduce.txt
    contar_fidelidad.py: IDENTICO a .v74ext/contar_fidelidad.txt
    citas.sh: IDENTICO a .v74ext/citas_fidelidad.txt
    d077.py: IDENTICO a .v74ext/d077.txt
    pasos_y_huellas.py: IDENTICO a .v73ext/pasos_y_huellas.txt
    libro_mayor_cap13.py: IDENTICO a .v74ext/libro_mayor.txt
    hoy contra .v73aud/huellas_al_barrer.txt: {('gerber_emyth', 'igual'): 22, ('grafo', 'igual'): 1, ('grove_high_output', 'igual'): 7, ('marquet_turn_the_ship', 'igual'): 20} | suma: 50 | en aquel fichero y hoy no: 0
    $ cat .v74aud/normal/deuda_como.txt
    pagos de la vuelta 74 en DEUDA.jsonl: 4 | como contra su fichero: {'d006': 'igual', 'd077': 'igual', 'd078': 'igual', 'd084': 'igual'}

**LECTURA:** las `7` fichas de Grove son byte a byte las que yo barri en la `73`, y la huella que su `74.4.b` dice conservar es la
de hoy. **Sus cuatro pagos estan en el registro letra a letra como sus ficheros.**

## 73.2. **EL REPORTE, AFIRMACION POR AFIRMACION** (`5.2`)

| afirmacion del reporte | sale | sede | especie |
|---|---|---|---|
| `74.0`: el censo de apertura, `procesos/` vacio, `SANEAMIENTO`, poblacion `479`, huellas identicas a las de la `73` | **cierta** (`73.1`) | bloque | |
| `74.D`, `74.D bis`, `74.D ter`: ocho discutibles marcados | **cierta**: `D74.1` a `D74.8`; los de fidelidad estan dentro de `.v74ext/fidelidad.tsv` con su numero, siete filas (`73.3`) | tablas | |
| `74.1`: los registros de la `ACTA 72` | **cierta** | tabla | |
| `74.2.1`: `d078`, los dos pasos, `L111` y `D73.5` en la linea `49131` de mi acta | **cierta** (mi `APERTURA_CIEGA.md` `5`, el mismo bloque) | bloque | |
| `74.2.2`: las `7` de la tanda `58` por dos vias, su sede, su barrido, sus lineas y **ninguna cambiada por lectura de vecino** | **cierta**: `d077.py` reproducido (`73.1`) y **cada ficha por `git log --numstat`** (`73.3`) | bloque y tabla | |
| `74.2.3`: la vuelta declarada de saneamiento, `d078` y `d077` pagadas | **cierta** (`73.1`, `deuda_como.txt`) | bloque | |
| `74.3.1`: `70` filas, `70` citas en su linea | **cierta** (`citas.sh` reproducido, `73.1`) | bloque | |
| `74.3.2`: ***`dar_elogio` `20` `19` `1`; los tres, `1` de `70`, el `1,4` por ciento*** | **FALSA: son `18` `T` y `2` `P`, y `2` de `70`, el `2,86`** (`73.4`, `73.5`) | **TABLA y CONCLUSION** | **`REPORTE`** |
| cabecera `T3` y tabla de cierre: ***`1` PUENTE traido sin tocar el grafo*** | **FALSA en la cuenta: son dos** (`73.5`); lo de *sin tocar el grafo* es cierto | **CABECERA y TABLA** | la misma caida |
| `74.3.3`: el puente de `dar_elogio` paso `17`, con su correccion propuesta | **cierta, y se sostiene** (`73.5`) | tabla | |
| `74.3.4`: el libro mayor, `70` de `212` sin firma, su fichero los cubre uno por uno | **cierta** (`73.1`; `0` sin fila y `0` de mas contra el grafo) | bloque | |
| `74.3.5`: `d084` y `d006` pagadas, la `75` `LIBRE` con `51` esperando | **cierta** (`73.10`, `clase75.txt`) | bloque | |
| `74.4.a` a `74.4.f`: censo, huellas, `D.61`, guardas, cierre estricto en su segunda corrida, `R5` | **cierta** (`73.0`, `73.1`); **la primera corrida en rojo la declara el mismo**, con su causa y sus dos salidas guardadas | bloques | |

**Una sola caida, y es de lectura: un paso que marco `T` y es `PUENTE`** (`73.5`). **Su especie y si acumula, en `73.7`.**

## 73.3. **SU FIDELIDAD CONTRA MI LECTURA SELLADA, FILA A FILA; Y `d077` COMMIT A COMMIT** (`APERTURA_CIEGA.md` `8`, puntos `3` a `6`)

    $ python .v74aud/normal/cruce_fidelidad.py
    filas mias: 70 | suyas: 70 | solo mias: 0 | solo suyas: 0
    pares (mia, suya): {('D', 'T'): 4, ('P', 'T'): 1, ('T', 'P'): 1, ('T', 'T'): 64} | suma: 70
    filas con linea del libro distinta: 0
    filas suyas marcadas DISCUTIBLE: 7
      contar_cuatro_historias_propias_ver_hueco_intencion  paso  3 | mia D L45 | suya T L45 DISCUTIBLE
      contar_cuatro_historias_propias_ver_hueco_intencion  paso  8 | mia D L49 | suya T L49 DISCUTIBLE
      contar_cuatro_historias_propias_ver_hueco_intencion  paso 15 | mia D L55 | suya T L55
      dar_elogio_disciplina_igual_critica                  paso  8 | mia P L273 | suya T L273
      dar_elogio_disciplina_igual_critica                  paso 17 | mia T L283 | suya P L283 DISCUTIBLE
      medir_critica_respuesta_oyente_brujula               paso  4 | mia T L295 | suya T L295 DISCUTIBLE
      medir_critica_respuesta_oyente_brujula               paso  8 | mia D L297 | suya T L297
      medir_critica_respuesta_oyente_brujula               paso 11 | mia T L301 | suya T L301 DISCUTIBLE
      medir_critica_respuesta_oyente_brujula               paso 14 | mia T L305 | suya T L305 DISCUTIBLE
      medir_critica_respuesta_oyente_brujula               paso 32 | mia T L321 | suya T L321 DISCUTIBLE

**`64` filas iguales, ninguna linea del libro distinta.** Mis cuatro `D` caen a su `T` y las dos `P` no coinciden: **cada uno leyo
un puente en `dar_elogio`, y no el mismo**. Se adjudican en `73.5`, **las dos**.

**`d077`, lo que mi fase ciega dejo para aqui** (*si alguna lectura de vecino le cambio el texto*, `APERTURA_CIEGA.md` `4`): cada
ficha por sus dos rutas, bandeja e insertados, con `git log --numstat`. Salida entera en `.v74aud/normal/d077_git.txt`; los commits
que cambian contenido despues de la `58`:

    $ grep -B1 -E "numstat [1-9][0-9]? [1-9]" .v74aud/normal/d077_git.txt | grep -v -E "^--|db70fe94" | cut -c1-110
      3e90afcc 2026-09-25T16:54:54-04:00 Vuelta 71, T1 y T2: los registros de la ACTA 69 y la fidelidad entera de 
        numstat 2 2
      c98d891b 2026-09-26T02:05:45-04:00 Vuelta 73, T2: la fidelidad entera de las 7 (42 pasos, 6 PUENTE corregido
        numstat 4 4
      c98d891b 2026-09-26T02:05:45-04:00 Vuelta 73, T2: la fidelidad entera de las 7 (42 pasos, 6 PUENTE corregido
        numstat 2 2
      c98d891b 2026-09-26T02:05:45-04:00 Vuelta 73, T2: la fidelidad entera de las 7 (42 pasos, 6 PUENTE corregido
        numstat 3 3

**LECTURA:** **cuatro commits de contenido en las siete fichas despues de su alta, y los cuatro son de fidelidad `D.30`** (el de la
`71` sobre `entregar_evaluacion`, los tres de la `73` sobre las tres de `cap_15`), escritos antes de su barrido, que la `ACTA 70` y
la `ACTA 72` firmaron con sus horas. **Ninguno es de vecino**; los de insercion mueven la ficha `0 0`. **Es su tabla de `74.2.2`,
fila a fila.** Y `d078`: la ficha con sus `7` pasos y su blob de la `73` (`73.1`), **como lei a ciegas** (`APERTURA_CIEGA.md` `5`).

## 73.4. **`PASOS INVENTADOS POR CAPITULO`** (`8`, `8.2`, `8.3`)

**Contados por los dos lados**: sus `70` filas son los `70` pasos del grafo (su `contar_fidelidad.py` reproducido, `73.1`, y mi
`contar_fidelidad.py` sellado, `APERTURA_CIEGA.md` `3`). Con las dos adjudicaciones de `73.5` aplicadas sobre sus marcas, por una
copia mia que lee su `.v74ext/fidelidad.tsv` y dice lo que cambia:

    $ cat .v74aud/normal/pasos_inventados.txt
    adjudicada por la ACTA 73: dar_elogio_disciplina_igual_critica paso 8, T de su marca pasa a P
    contar_cuatro_historias_propias_ver_hueco_intencion  pasos en el grafo 17 | por marca: {'T': 17} | suma: 17 | PUENTE 0 de 17 = 0.00 por ciento
    dar_elogio_disciplina_igual_critica                  pasos en el grafo 20 | por marca: {'P': 2, 'T': 18} | suma: 20 | PUENTE 2 de 20 = 10.00 por ciento
    medir_critica_respuesta_oyente_brujula               pasos en el grafo 33 | por marca: {'T': 33} | suma: 33 | PUENTE 0 de 33 = 0.00 por ciento
    cap_13, los tres: pasos en el grafo 70 | por marca: {'P': 2, 'T': 68} | suma: 70 | PUENTE 2 de 70 = 2.86 por ciento

| capitulo | que es | nodos | pasos | PUENTE | por ciento | PUENTE que siguen en el grafo |
|---|---|---:|---:|---:|---:|---:|
| `cap_13` de `scott_radical_candor`, los tres de `d084` | *Afterword: Rolling Out Radical Candor* | `3` | `70` | `2` | `2,86` | `2`, hasta la `75` |

**Ningun nodo por encima del `10`**: `dar_elogio` queda **en** el `10` justo, que no es *por encima*. **LECTURA:** los dos puentes
son clausulas, no medios: el paso transcribe el libro y le pega una comparacion (*y la critica no*) o una calidad de la prueba
(*ha medido*) que el libro no pone. **Es un capitulo de inventario rico**, y la cifra no dimensiona ningun lote (`8.1`): son nodos
que viven en el grafo desde la vuelta `37`, y lo que mide es la firma que les faltaba.

**`cap_13` ENTERO, `212` pasos, QUEDA FIRMADO**: `142` por las actas que su libro mayor cita (`38`, `39`, `40` y `58`) y **estos `70`
por esta acta**. El instrumento `.v60aud/libro_mayor_cap13.py` seguira diciendo `NADIE` para estos tres porque sus firmas estan
escritas a mano en su codigo, y **no lo toco**: la firma es esta seccion y `73.5`. **No compongo la cifra del capitulo entero**: el
`4` de `212` de `d006` es de la `ACTA 40` y no lo he medido hoy.

## 73.5. **LA RELECTURA** (`1.2`, `5.1`, `6.1`, `D.30`)

**PRIMERO LOS PASOS Y EL LIBRO, DESPUES SU RAZON.** Los pasos en disputa de `dar_elogio_disciplina_igual_critica`, del grafo, y sus
lineas:

    $ cat .v74aud/normal/lineas_puente.txt
    $ sed -n 273p fuentes/scott_radical_candor/cap_13.md | grep -o -E "Also, praise helps people focus on their strengths[^.]*"
    Also, praise helps people focus on their strengths and on doing more work that they enjoy and less of what they hate
    $ sed -n 273p fuentes/scott_radical_candor/cap_13.md | grep -o -i -E "critic[a-z]*" | wc -l
    0
    $ sed -n 283p fuentes/scott_radical_candor/cap_13.md | grep -o -E "We.ve (found|heard)|measur[a-z]*"
    We’ve found
    We’ve heard

- **Paso `8`**: *Cuenta ademas con lo que el elogio consigue **y la critica no**: ayuda a la gente a centrarse en sus fuerzas y a
  hacer mas del trabajo que disfruta y menos del que odia.* **`L273` no nombra la critica** (bloque de arriba): dice *Also*, y anade
  una razon mas para elogiar primero. **ADJUDICO `PUENTE` de clausula**, por `D.30` y el criterio de la `ACTA 62` `62.5`: el paso
  afirma de la critica algo que el libro no dice, y es la figura de `D71.9`, segundo caso (sostenido en la `ACTA 70` `70.5`): una
  palabra que cambia lo que el libro sostiene. **La lectura contraria, escrita**: el mismo parrafo contrapone fuerzas a debilidades
  (*focusing on strengths than weaknesses*), y un lector puede oir ahi la critica. **No la elijo**: el libro contrapone dos focos, no
  dos actos, y la critica de este libro no es *centrarse en las debilidades*. **Coincide con mi lectura ciega**, y lo digo porque me
  favorece.
- **Paso `17`, su `D74.6`**: *Cuenta con lo que el texto **ha medido** de ese ejercicio*, donde `L283` dice *We've found* y *We've
  heard*. **ADJUDICO `PUENTE` de clausula: GANA SU LECTURA, dentro de su marcado.** No es el verbo de marco de `D73.6` (la practica
  que el libro recomienda puesta de mandato): **es una afirmacion sobre la prueba del libro que el libro no hace**; lo que ellos
  cuentan es lo que vieron y oyeron en sus talleres. Quien lea el nodo cree que hay una medida detras. **Cae mi lectura ciega**, que
  lo leyo `T` sin duda.

**LOS DOS SE CORRIGEN, Y LA VIA ES LA QUE LA CASA YA TIENE**: `D.30` (*cada puente se retira o se reescribe; un puente no se queda
callado dentro de un nodo*) y **`D.54`** con `scripts/retirar_paso.py`, que es la unica via para un paso de un nodo ya insertado
(*ningun instrumento de la casa reescribe un paso de un nodo ya insertado*, `D.54`). **Es el camino exacto del `P13` de
`practicar_franqueza_radical_jefe_propio`** (vuelta `35` por `D.13` y `forja.py corregir`, aplicado despues por `D.54`): el paso sale
del campo, **su literal queda escrito en el nodo**, y la correccion dice que parte del paso es del libro. **No es doctrina nueva: es
`D.30` y `D.54` en su letra**, y la encargo como la unica bloqueante (`73.6`).

**Y CAE UNA CIFRA VIEJA DEL PROPIO NODO**, que no es de esta vuelta:

    $ python -c "import json,re; [print(d['id'], len(d['pasos_accionables']), 'pasos |', re.search(r'RELECTURA DE FIDELIDAD D.30 EN EL ACTO[^:]*: [^.]*', d['resumen_teorico']).group(0)) for d in map(json.loads, open('dataset/nodos.jsonl', encoding='utf-8')) if d['id']=='dar_elogio_disciplina_igual_critica']"
    dar_elogio_disciplina_igual_critica 20 pasos | RELECTURA DE FIDELIDAD D.30 EN EL ACTO, paso a paso contra su linea: 20 pasos, 20 TRANSCRIPCION, 0 PUENTE
    $ grep -n dar_elogio_disciplina_igual_critica bitacora/VEREDICTOS.jsonl | cut -d: -f1 | tr '\n' ' '
    490 531 532 533 534 535 732 

**LECTURA:** el `resumen_teorico` de `dar_elogio` dice *`20` pasos, `20` TRANSCRIPCION, `0` PUENTE*; **la cuenta buena es `18` y `2`**.
Es de la vuelta `37`, sin retroactividad para ninguna racha, y **se corrige en el mismo acto** por `forja.py corregir` (`D.13`, sin
borrar). La bitacora lo nombra en siete lineas; **las que citen un numero de paso suyo a partir del `8` quedaran con la numeracion
vieja**, y la correccion lo declara con la tabla de numeros (encargo de la `75`, TAREA `2`).

**SUS OCHO DISCUTIBLES, POR NUMERO** (`D.47`):

| | su marca | adjudico |
|---|---|---|
| `D74.1` | `d078` pagada citando `D73.5` y `72.5`, sin tocar la ficha | **SE SOSTIENE**: lo que `d078` pedia decidir ya estaba decidido y adjudicado; lo que queda el dia de la insercion es que la ficha entre con su huella, y eso lo mide la `75` (`APERTURA_CIEGA.md` `5`) |
| `D74.2` | `d077` entera, las cuatro de la bandeja con el barrido de la `73` | **SE SOSTIENE**: el texto de `d077` pide la cola *de ese dia*, y la de hoy es la del barrido (`0` ficheros movidos, `73.1`); **la aduana de cada `insertar` de la `75` la vuelve a medir**, como en la `72` |
| `D74.3` | las horas de los barridos contra la ultima escritura de ficha | **SE SOSTIENE**: sus citas a mi acta (`L48156`, `L49030`, `L49032`) son las horas que yo publique |
| `D74.4` | `contar_cuatro_historias` paso `3`, `T` | **SE SOSTIENE, y cae mi duda**: *If you tell your team* es la premisa del ejercicio que `L43` abre, no un modal de posibilidad |
| `D74.5` | el mismo nodo, paso `8`, `T` | **SE SOSTIENE, y cae mi duda**: la orden la escribe el libro para el mismo ejercicio en `L51` (*tell yours*) |
| `D74.6` | `dar_elogio` paso `17`, `P` | **SE SOSTIENE** (arriba) |
| `D74.7` | `medir_critica` pasos `4`, `11` y `32`, `T` | **SE SOSTIENE**: los lei `T` sin duda; los tres *can* son el metodo que el libro da, no una posibilidad lateral, y el `32` conserva el *ayuda* |
| `D74.8` | `medir_critica` paso `14`, `T` | **SE SOSTIENE**: lo lei `T` sin duda; *la via que el texto da* es cierta (el texto da esa) y el paso no excluye otra |

**Y mis otras dos dudas, que el no marco**: `contar_cuatro_historias` paso `15` (*When people unpack... and share them*, `L55`) y
`medir_critica` paso `8` (*You cannot do this if you are on your phone*, `L297`): **`T` los dos, cae mi duda**; la primera es el
mismo ejercicio, la segunda una traduccion floja sin clausula nueva.

**DENTRO CONTRA FUERA DEL MARCADO:** ocho marcados, **ocho se sostienen**. **Fuera del marcado, UNA caida: `dar_elogio` paso `8`**,
un `PUENTE` leido `T` sin duda. **Es la cifra que mueve el credito, y dice que no lo vio venir** (`5.1`). El tramo tiene marcados,
asi que la comparacion existe (`7.G`, `6.4`).

**LA RELECTURA AL DOBLE DEL TRAMO** (`5.2`): **hecha y pasada del doble**; el tramo es la fidelidad de los tres nodos, y la he
cruzado entera, `70` filas de `70`, no solo las marcadas (`73.3`).

**LA FIRMA DE `d084` Y `d006`** (encargo de la `74`, TAREA `3.3`): **su fichero cubre, uno por uno, los `70` pasos que la linea *SIN
FIRMA DE NADIE* cuenta, y los FIRMO** con la cuenta de esta seccion. **Los dos pagos se sostienen**, porque la condicion era la
cobertura. **Lo que cae es la cifra de sus `como`** (*`1` de `70`, el `1,4` por ciento; EL UNICO PUENTE*, y *con `1` PUENTE*):

> **CORRECCION DECLARADA DE LOS `como` DE `d084` Y `d006` EN `docs/loop/DEUDA.jsonl`, VUELTA `74`, SIN BORRARLOS:** donde dicen
> *`1` de `70`* y *el unico puente, `dar_elogio` paso `17`*, **vale `2` de `70`, el `2,86` por ciento: `dar_elogio` pasos `8` y
> `17`**, por esta seccion. El registro no tiene via para corregir un `como`, y esta acta es su sede.

**LA MUESTRA PINEADA DE LOS SANO** (`7`): **esta vuelta no escribe en la bitacora**, asi que no hay poblacion. Se tira cuando entren
las `29` lineas de la `75`, con semilla escrita.

## 73.6. **LAS CUATRO GUARDAS DE DATO** (`D.55`)

| guarda | estado | medida |
|---|---|---|
| `gate` | **VERDE** | `73.1` |
| el cerrojo (`D.44`) | **VERDE**: ningun `insertar` en la vuelta; `procesos/` vacio | `73.1` |
| censo no decreciente | **VERDE**: nada movido | `73.1` |
| fidelidad `D.30` con puente | **ROJO: DOS PUENTES VIVEN EN EL GRAFO**, `dar_elogio_disciplina_igual_critica` pasos `8` y `17` | `73.5` |

> **TAREA BLOQUEANTE DEL AUDITOR PARA LA VUELTA `75`, UNA Y SOLO UNA** (`D.55`, **citando la guarda `D.30` en rojo**): **los dos
> puentes de `dar_elogio_disciplina_igual_critica` salen del campo por `D.54`**, antes de ningun `insertar`: primero
> `python forja.py corregir` con la correccion declarada (las dos lineas del libro, que parte de cada paso es del libro, la cuenta
> `18` y `2` en lugar de `20` y `0`, y la tabla de numeros de paso vieja contra nueva), y despues `python scripts/retirar_paso.py`
> **sobre el paso `17` y luego sobre el `8`**, en ese orden para que el numero del segundo no se mueva. Gate en verde despues de cada
> una. **Encargo de la `75`, TAREA `2`.**

**Esta averia no es de la vuelta `74`**: el puente vive en el grafo desde la vuelta `37`; la `74` lo trajo como mandaba su encargo, y
esta acta lo adjudica **antes de que nadie mueva un dato**, que es lo que el encargo pedia.

## 73.7. **EL CREDITO DE LA LINEA `serial`** (`5.3`, `D.48`)

    $ sed -n '5,12p' .v74aud/normal/credito_abrir.txt
      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA 72
      CIFRA PUBLICADA    0 de 2     ACTA 72
      CLASE              0 de 2     ACTA 72
      DATO MOVIDO        0 de 2     ACTA 72
      REPORTE            1 de 3     ACTA 72

| especie | tanda `ACTA 73` | racha | el motivo, medido |
|---|---|---|---|
| **`CLASE`** | **LIMPIA** | `0 de 2` | no escribio ningun veredicto: la bitacora tiene `1081` lineas al abrir y al cerrar, sin diff (`73.1`) |
| **`CIFRA PUBLICADA`** | **LIMPIA** | `0 de 2` | no escribio en `docs/` fuera de `docs/loop/`, ni en `config/`, `esquema/` ni `src/` (`73.1`) |
| **`DATO MOVIDO`** | **LIMPIA** | `0 de 2` | no toco grafo, bitacora, censos ni bandejas (`73.1`) |
| **`REPORTE`** | **CAE** | **`2 de 3`** | `73.2`: *`1` PUENTE*, *`19` `1`* y *`1` de `70`*, falsos, en TABLA, CABECERA y CONCLUSION |
| **`AUDITOR`** | **LIMPIA** | `0 de 3` | `73.9`: ningun remedio mio roto y ninguna cifra mia falsa; lo que cae de mi es de clase |

**`REPORTE`, POR QUE ESTA ESPECIE Y POR QUE ACUMULA.** Una marca de fidelidad del extractor que cae **no es `CLASE`**, que es un
veredicto mal puesto en la bitacora, los pares o el dataset, y la vuelta no escribio en ninguno. **Es el precedente de la `ACTA 62`**
(`62.3`, su `D1`): la marca cayo y se cargo como `REPORTE`, **que alli no acumulo porque ninguna celda de tabla lo contradecia**.
**Aqui si**: la fila `dar_elogio` de su tabla de `74.3.2` dice `19` y `1`, y la cabecera y la tabla de cierre dicen *`1` PUENTE*.
**La lectura contraria, escrita**: la cifra es la cuenta exacta de sus marcas, hecha por instrumento, y lo que cae es una marca, que
es lo que la `ACTA 63` `63.9` uso para no cargarme a mi el mismo tipo de error. **No la elijo para el**, y esa asimetria no la
invento hoy: la `63.9` la declaro con el beneficiado escribiendola, y sigue ahi para que el fundador la tumbe.

**`REPORTE` QUEDA EN SU PENULTIMO ESCALON: LA SIGUIENTE CAIDA QUE ACUMULE PARA LA LINEA** (`5.4`). **La escalada se encarga**
(`1.4`, `5.5`): con la guarda `D.30` en rojo, la unica bloqueante que `D.55` me deja es la de `73.6`, y **el remedio de la especie va
en la tabla de `73.11`, `R9`**, como hizo la `ACTA 59` `59.18` en el mismo escalon. **No etiqueto una segunda bloqueante**: `D.55`,
del `18` sep, gana a `5.5` por `D.13`, y lo declaro en vez de resolverlo en silencio.

(Una linea por especie en `docs/loop/CREDITO_serial.jsonl`, al cerrar esta acta.)

## 73.8. **EL COSTE** (`D.55`)

    $ sed -n '7732p;7736p' docs/loop/loop.log
    [2026-09-26 03:59:43] extractor listo (USD 6.595389600000001), 2016s, intento 1 de 7
    [2026-09-26 04:12:17] auditor ciego listo (USD 4.5987241999999995), 753s, intento 1 de 7

**Por debajo de `10` USD los dos turnos, y la vuelta es de saneamiento**: no hay desglose que declarar.

## 73.9. **MI PROPIA TANDA** (`D.38.2`)

**LAS CIFRAS DE MI APERTURA SELLADA, CONTRA LO MEDIDO HOY:** el censo, la poblacion y las huellas (`73.1`); los `70` pasos y mis `70`
filas (`73.3`); las siete fichas de `d077` por sede (`73.3`); `R8` sobre el encargo de la `74` (`APERTURA_CIEGA.md` `7`). **Todas
cuadran.**

**LO QUE CAE DE MI, CON MI NOMBRE, Y NINGUNO ACUMULA:**

- **una clase de fidelidad**: `dar_elogio` paso `17`, que lei `T` sin duda y es `PUENTE`, **dentro de lo que el marco** (`D74.6`);
- **cuatro dudas**, las cuatro inclinadas a `T` y las cuatro caen a `T`, que es donde me inclinaba.

> **Y MI CUENTA SELLADA *`PUENTE 1 de 70 = 1.43 por ciento`* SALE FALSA EN SU CIFRA, COMO LA SUYA.** **No la cuento como `CIFRA
> PUBLICADA PROPIA`**, por el precedente de la `ACTA 63` `63.9` (*lo que cae son clases, y una clase no es una cifra*; `ACTA 16`
> `7.4`): es la cuenta exacta de mis marcas, por instrumento, rotulada como mi lectura. **Soy el beneficiado, y lo escribo al lado de
> `73.7`, donde la misma figura le cuesta un escalon al extractor**: si el fundador decide que la asimetria no vale, **las dos
> lecturas se corrigen juntas**, y mi racha pasa a `1 de 3`.

**LO QUE MI APERTURA DIJO QUE HARIA EN EL TURNO NORMAL** (su seccion `8`, nueve puntos) **esta todo aqui**: `R5` en `73.0`; el censo con
`git diff` en `73.1`; la fidelidad fila a fila y el puente en `73.3` y `73.5`; la firma en `73.5`; `d077` con `git log` en `73.3`;
`d078` en `73.3`; las huellas en `73.1`; la muestra en `73.5`; `R8` en `73.12`.

## 73.10. **LAS CONDICIONES DE PARADA, UNA A UNA** (`3`)

| condicion | se cumple | como lo mido |
|---|---|---|
| doctrina nueva | **NO** | los dos puentes los decide `D.30` con `62.5` y `D71.9`; su correccion, `D.54` y el precedente del `P13` (`73.5`) |
| contradiccion | **NO** | la de `5.5` contra `D.55` la resuelve `D.13` (`73.7`) |
| decision de Alexis | **NO** | retirar un paso de un nodo insertado ya es de `D.54`, decision del fundador del `17` sep; la insercion de Grove esta autorizada (`ACTA 64` `64.10`) |
| fallo tecnico repetido | **NO** | gate, guiones, la suite y el cierre estricto en verde (`73.1`) |
| credito roto | **NO** | `REPORTE` en `2 de 3`, las demas en cero (`73.7`) |
| campania consumada | **NO**: el tablero, abajo | |

    $ sed -n '11,13p;24p' .v74aud/normal/tablero.txt
      1    7    grove_high_output              COSECHADO              NINGUNO                  7  cap_18
      2    9    gerber_emyth                   COSECHADO              NINGUNO                 22  cap_22
      3    5    marquet_turn_the_ship          COSECHADO              NINGUNO                 20  cap_17
      MUNDO 11: faltan 3 de 7 libros del corte (grove_high_output, gerber_emyth, marquet_turn_the_ship)
    $ cat .v74aud/normal/clase75.txt
    LIBRE
      van 1 de 5 desde la ultima de saneamiento (la 74), con 51 deuda(s) esperando

**NO ESCRIBO `PARA_ALEXIS.md`.** **La `75` es LIBRE**: abre con la bloqueante de `73.6` y **despues inserta las `7` fichas de Grove**
que la `73` dejo listas y la `74` conservo byte a byte, con sus `29` lineas y sus `3` aristas (`.v73ext/orden.txt`, ultima linea).

**UNA COSA QUE VEO PARA DESPUES, Y LA ANOTO COMO DEUDA** (`D.55`): cuando la bandeja de Grove quede en `0`, **el tablero lo seguira
llamando `COSECHADO`**, porque el codigo mira *cosechado* antes que *bandeja vacia con nodos en el grafo*:

    $ grep -n -E 'elif clave in cosechados|elif candidatos == 0 and en_grafo > 0' src/tablero.py
    302:        elif clave in cosechados:
    316:        elif candidatos == 0 and en_grafo > 0:

**LECTURA:** la linea `MUNDO 11` pide `INSERTADO` a los siete, asi que **el tablero no dira nunca *completo* por si solo**. No es de
esta vuelta ni de la `75`, y no se toca (`D.45`, `7.F`): va al registro con esa medida.

## 73.11. **LOS REMEDIOS**

| # | de quien | remedio | donde se comprueba |
|---|---|---|---|
| `R5` | del extractor | **Sigue vivo con su letra**, cumplido de la `65` a la `74` | el reporte de la `75`, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera cambiada a la `75` |
| `R6` | del auditor | **Sigue vivo con su letra**: en la fase ciega, los pasos de cualquier nodo se imprimen con `.v67aud/normal/pasos_ciego.py`, y ningun instrumento de esa fase imprime claves de relacion de un nodo que la vuelta haya tocado | la apertura ciega de la `75` |
| `R7` | del auditor | **Sigue vivo con su letra**: toda linea de conteo por clases que publique cuenta todas las clases con el mismo predicado y trae su `suma` | la apertura ciega de la `75` y la `ACTA 74` |
| `R8` | del auditor | **Sigue vivo con su letra y su criterio** (`ACTA 72` `72.9`, `72.11`); instrumento de esta vuelta, `.v74aud/normal/r8_encargo75.py` | mi fase ciega de la `75`, sobre el encargo de la `75` (`73.12`); y el encargo de la `76` |
| **`R9`** | **del extractor, NUEVO** (`73.7`, la escalada de `REPORTE`) | **Toda fila de fidelidad que marque `T` y cuyo paso traiga una clausula que COMPARA o CONTRASTA** (*y X no*, *mas que*, *a diferencia de*) **o que CALIFICA LA PRUEBA del libro** (*ha medido*, *demuestra*, *esta probado*) **cita en su nota el tramo literal del libro que sostiene esa clausula; si no lo hay, la fila es `P`.** Y **antes de publicar una cuenta de PUENTE**, el reporte pega un `grep` de esas clausulas sobre los pasos que marca `T`, con lo que encuentra | el reporte de la `75` y siguientes que marquen fidelidad; en la `75`, sobre la correccion de `dar_elogio` |

**`D.55` se cumple**: la vuelta `75` recibe **una** tarea bloqueante, la de `73.6`, con la guarda `D.30` en rojo citada.

## 73.12. **`R8` MEDIDO SOBRE MI ENCARGO DE LA `75`, ANTES DE CERRARLO** (`73.11`)

    $ python .v74aud/normal/r8_encargo75.py | tail -1
    lineas del encargo: {'linea de bloque sangrado': 22, 'prosa con numero, con seccion de la ACTA 73': 18, 'prosa con numero, sin seccion de la ACTA 73': 53, 'prosa sin digito ni palabra de numero': 60} | suma: 153

(Las lineas con numero, cada una con sus digitos y sus palabras de numero, en `.v74aud/normal/r8_encargo75.txt`.) **LECTURA, grupo a
grupo, de las que no traen seccion, leidas una a una y no copiadas de la `72.12`:**

- **Numeros de vuelta, de acta, de rama, de mundo o de carpeta de la casa** (`75`, `76`, `74`, `73`, `72`, `59`, `11`, y `.v72ext/`,
  `.v73ext/`, `.v74ext/`, `.v75ext/`, `.v64ext/`).
- **Secciones, reglas, deudas y numeros de tarea, de punto o de lista** (`1.4`, `0`, `D.13`, `D.30`, `D.31`, `D.47`, `D.54`, `D.55`,
  `D.61`, `7.F`, `6.1`, `4.2`, `d031`, `R4`, `R5`, `R9`, y los `1` a `5` de tareas y puntos).
- **Identificadores de capitulo, de fila o de paso**: `cap_13`, `cap_15` a `cap_17`, `cap_18`; las filas `1`, `3`, `6` y `7` de
  `.v73ext/orden.txt`; los pasos `8` y `17` de `dar_elogio`, y **la tabla de numeros de paso de la TAREA `2.1`**, que es aritmetica de
  esos dos identificadores sobre los `20` pasos que la misma TAREA cita con su seccion en su linea.
- **Las dos lineas que citan una seccion de la `ACTA 72`** (`L108`, `72.5`; `L125`, `72.4`): llevan en su misma linea la seccion del
  acta donde su cifra esta pegada, que es la letra de `R8`; el instrumento solo reconoce las `73.N`.
- **Palabras de numero sin seccion**: `L73` (*las tres operaciones*, las que la misma TAREA enumera), `L111` (*los dos*, los dos
  nodos de un par) y `L152` (*cero guiones*, la meta de la frase fija). **Ninguna es una cuenta de fichero.**
- **Las cifras de medida** van dentro de un bloque `$` (la clase, el tablero, el reloj, las filas y las aristas de la tanda, las
  lineas preparadas) o llevan su seccion de la `ACTA 73` en la misma linea (los dos puentes, la cuenta del resumen, los `18` pasos, el
  censo de apertura, la huella).

**`R8` CUMPLIDO EN EL ENCARGO DE LA `75`, medido.** Lo vuelve a medir mi fase ciega (`73.11`).

## 73.13. **LO QUE ANOTO AL CERRAR**

- **`docs/loop/CREDITO_serial.jsonl`**: las lineas de la tanda `ACTA 73`: `CLASE`, `CIFRA PUBLICADA`, `DATO MOVIDO` y `AUDITOR` con
  `--limpia`, y `REPORTE` con `--cae`.
- **`docs/loop/DEUDA.jsonl`**: una deuda nueva, la del tablero de `73.10`, con su medida.
- **`docs/loop/PROMPT_SIGUIENTE.md`**: el encargo de la vuelta `75`, **LIBRE**: la bloqueante de `D.30` y las `7` de Grove.
- **`.v74aud/`**: mi evidencia de las dos fases, commiteada con `docs/loop/`.
