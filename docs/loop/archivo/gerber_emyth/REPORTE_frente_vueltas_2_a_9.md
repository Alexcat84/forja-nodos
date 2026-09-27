<!-- ARCHIVO DEL FRENTE gerber_emyth: SOLO LO SUYO. Lo anterior es la sede de la serial que su arbol heredo, y vive en docs/loop/REPORTE.md de la serial. -->


# FRENTE `gerber_emyth`, VUELTA 2: **`cap_05` Y `cap_06` MINADOS A CERO, EL HUECO ENTRE `cap_04` Y `cap_07` CERRADO**

> ## ESTE BLOQUE SE ESCRIBE EN LA RAMA `extraccion-gerber_emyth`, CON `MODO_INSERCION=cuarentena`. CERO INSERCIONES: la insercion es autorizacion del fundador y esta corrida no la trae.
>
> **MODO AUSTERO (`D.47`) VIGENTE.** Nada que el registro ya diga, cifras talladas, discutibles por numero y linea.

## G2.0. EL ESQUELETO DE LA VUELTA, ABIERTO ANTES DE LA PRIMERA TAREA (`EXTRACTOR.md` 3)

| # | tarea del encargo | como cierra | donde |
|---:|---|---|---|
| 1 | la frontera de `cap_05` y `cap_06`, cerrada contra el cuerpo al digito | **CERRADA**: `2` de `2` con residuo `0`, cero solapes y cero lineas sin cubrir | `G2.2` |
| 2 | los candidatos que el capitulo de, cada uno con su informe en el acto | **CERRADA**: `0` candidatos en los dos, con su razon escrita pieza a pieza | `G2.3` |
| 3 | `PASOS INVENTADOS POR CAPITULO`, una fila por capitulo y no una media | **CERRADA**: las dos filas en `SIN SUPERFICIE` | `G2.4` |
| 4 | la muestra de fidelidad con la semilla de esta vuelta (`g2`) | **CERRADA**: instrumento corrido, `cap_05` releido ENTERO y `cap_06` por muestra, los dos con `0` pasos | `G2.5` |
| | el cierre: guardas, cifras recomputadas, discutibles marcados, commit y push | **CERRADO** | `G2.7` a `G2.9` |

**LAS CUATRO TAREAS ENTREGADAS Y CERO COLA** (`EXTRACTOR.md` 1.3, tope de cinco). **Y CERO INSERCIONES**, que es la regla que manda en este frente.

## G2.1. LA APERTURA, MEDIDA TRAS LA UNICA ESCRITURA QUE YA MOVIO EL ARBOL (`EXTRACTOR.md` 4)

*Declarado como estado intermedio y no como apertura pura, tal como la propia regla exige: antes de correr este instrumento ya habia anotado `d094` en `docs/loop/DEUDA.jsonl` (ver `G2.6`), que es una escritura y no una lectura. La operacion que lo movio queda nombrada aqui.*

Salida de `python .gerber_v2/apertura.py`, guardada en `.gerber_v2/apertura.txt`:

<!-- TALLADO: salida=.gerber_v2/apertura.txt -->

| pieza | al abrir | de donde sale |
|---|---:|---|
| nodos en el grafo | **346** | `dataset/nodos.jsonl` |
| veredictos escritos | **740** | `bitacora/VEREDICTOS.jsonl` |
| unidades de `gerber_emyth` | **22** | `PATRON: fuentes/gerber_emyth/cap_*.md` |
| palabras de cuerpo del libro | **62648** | `PATRON: fuentes/gerber_emyth/cap_*.md` |
| unidades apartadas del `cap. 17` | **1** | `PATRON: fuentes/gerber_emyth_cap17_reservado/*.md` |
| candidatos en bandeja de `gerber_emyth` | **10** | `PATRON: cuarentena/gerber_emyth/*.json` |
| clave `gerber_emyth` en la tabla canonica | **SI** | `fuentes/FUENTES_CANONICAS.json` |
| claves en la tabla canonica | **12** | `fuentes/FUENTES_CANONICAS.json` |
| rama activa | `extraccion-gerber_emyth` | `git rev-parse --abbrev-ref HEAD` |
| commit de apertura | `072b49f` | `git rev-parse --short HEAD` |

| unidad | fichero | rotulo | palabras de cuerpo |
|---|---|---|---:|
| Foreword | `cap_01.md` | Foreword | **1402** |
| Introduction | `cap_02.md` | Introduction | **1212** |
| Cap. 1 | `cap_03.md` | The Entrepreneurial Myth | **2202** |
| Cap. 2 | `cap_04.md` | The Entrepreneur the Manager, and the Technician | **3713** |
| Cap. 3 | `cap_05.md` | Infancy: The Technician's Phase | **2400** |
| Cap. 4 | `cap_06.md` | Adolescence: Getting Some Help | **1980** |
| Cap. 5 | `cap_07.md` | Beyond the Comfort Zone | **4284** |
| Cap. 6 | `cap_08.md` | Maturity and the Entrepreneurial Perspective | **2183** |
| Cap. 7 | `cap_09.md` | The Turn-Key Revolution | **2845** |
| Cap. 8 | `cap_10.md` | The Franchise Prototype | **1411** |
| Cap. 9 | `cap_11.md` | Working On Your Business, Not In It | **4360** |
| Cap. 10 | `cap_12.md` | The Business Development Process | **4206** |
| Cap. 11 | `cap_13.md` | Your Business Development Program | **364** |
| Cap. 12 | `cap_14.md` | Your Primary Aim | **3695** |
| Cap. 13 | `cap_15.md` | Your Strategic Objective | **4685** |
| Cap. 14 | `cap_16.md` | Your Organizational Strategy | **4835** |
| Cap. 15 | `cap_17.md` | Your Management Strategy | **2448** |
| Cap. 16 | `cap_18.md` | Your People Strategy | **5396** |
| Cap. 18 | `cap_19.md` | Your Systems Strategy | **4431** |
| Cap. 19 | `cap_20.md` | A Letter to Sarah | **1841** |
| Epilogue | `cap_21.md` | Epilogue: Bringing the Dream Back to American Small Business | **1851** |
| Afterword | `cap_22.md` | Afterword: Taking the First Step | **904** |

**Contra el encargo:** `10` candidatos en bandeja y los capitulos minados `cap_04`, `cap_07`, `cap_08` y `cap_11` coinciden con lo que la seccion `2` del encargo publica. `346` nodos y `740` veredictos coinciden con el estado de la parada resuelta del 21 sep. Cero discrepancia que declarar.

## G2.2. TAREA 1: **LA FRONTERA DE `cap_05` Y `cap_06`, CERRADA CONTRA EL CUERPO AL DIGITO**. **CERRADA**

*El instrumento es `.gerber_v1/frontera.py`, el mismo de la vuelta 1 y sin ningun cambio: cortar `cap_05` y `cap_06` con el es la misma regla aplicada al mismo libro. Se copia a `.gerber_v2/` y se corre de nuevo hoy; no se cita el disco de la vuelta 1.*

    $ diff .gerber_v1/frontera.py .gerber_v2/frontera.py
    (vacio, cero cambios en el instrumento)

### LA FRONTERA DE `cap_05` (`Cap. 3`, *Infancy: The Technician's Phase*), **4 piezas y CERO con procedimiento**

Salida de `python .gerber_v2/frontera.py fuentes/gerber_emyth/cap_05.md .gerber_v2/piezas_cap05.txt`, guardada en `.gerber_v2/frontera_cap05.txt`:

<!-- TALLADO: salida=.gerber_v2/frontera_cap05.txt -->

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L19 | **39** | el numero del capitulo, el rotulo `INFANCY: THE TECHNICIAN PHASE` y el epigrafe de e. e. cummings | **RESIDUO: rotulo y epigrafe** |
| `R2` | L20 a L31 | **148** | los negocios crecen y cambian, lo que el tecnico quiere es lo contrario, y las tres fases nombradas: Infancy, Adolescence y Maturity | **POSTURA** |
| `R3` | L32 a L89 | **862** | la Infancia contada entera: el duenio y el negocio son lo mismo, el malabarista que empieza a soltar bolas, y la Infancia que acaba cuando el duenio ve que aquello no puede seguir asi | **POSTURA y CASO** |
| `R4` | L90 a L149 | **1351** | el dialogo con Sarah: nada malo en ser tecnico salvo si ademas posee el negocio, el proposito de montar un negocio, y el paso a la Adolescencia | **CASO** |
| **el cuerpo entero** | **L8 a L149** | **2400** | **suma de las piezas: 2400** | **residuo sin asignar: 0** |

    piezas: 4   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 2400   suma 2400   residuo 0

**Por que ninguna pieza pasa la vara de `EXTRACTOR.md` 9 y 9.1.** `R2` nombra las tres fases del negocio (Infancy, Adolescence, Maturity), y si, es un inventario del propio libro, **pero de FASES del negocio, no de medios, etapas u objetos de trabajo que este capitulo mande ejecutar**: es la tabla de contenidos del libro dicha en prosa, y nombrar adonde va la narracion sigue siendo nombrar (restriccion 1 de `9.1`). `R3` cuenta la Infancia entera como diagnostico: el dueno es el negocio, las bolas que se caen, el cierre de la fase; Joe, Tommy y Mary son ilustracion generica y no un caso nombrado con datos propios. `R4` es el dialogo con Sarah: el proposito de montar un negocio y por que no basta con ser tecnico; el consultor da un juicio tajante (*get rid of your business*), pero ningun medio, etapa u objeto de trabajo esta nombrado uno a uno por el libro: es postura dicha con fuerza, no procedimiento.

### LA FRONTERA DE `cap_06` (`Cap. 4`, *Adolescence: Getting Some Help*), **5 piezas y CERO con procedimiento**

Salida de `python .gerber_v2/frontera.py fuentes/gerber_emyth/cap_06.md .gerber_v2/piezas_cap06.txt`, guardada en `.gerber_v2/frontera_cap06.txt`:

<!-- TALLADO: salida=.gerber_v2/frontera_cap06.txt -->

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L19 | **32** | el numero del capitulo, el rotulo `ADOLESCENCE: GETTING SOME HELP` y el epigrafe de Alvin Toffler | **RESIDUO: rotulo y epigrafe** |
| `R2` | L20 a L57 | **255** | la Adolescencia empieza cuando pides ayuda, y la ayuda que el tecnico busca es siempre tecnica: alguien con experiencia en tu mismo oficio | **POSTURA** |
| `R3` | L58 a L127 | **671** | Harry el contable: la Management by Abdication en vez de Delegation, el alivio de no tener que hacerlo, y la vida que se vuelve facil | **CASO** |
| `R4` | L128 a L215 | **977** | las llamadas que lo rompen todo, la vuelta del malabarista, la conclusion de que nadie se preocupa como tu, y la Comfort Zone tocando su limite | **CASO y POSTURA** |
| `R5` | L216 a L221 | **45** | Sarah y el nervio tocado: su propia zona de confort | **RESIDUO: bisagra** |
| **el cuerpo entero** | **L8 a L221** | **1980** | **suma de las piezas: 1980** | **residuo sin asignar: 0** |

    piezas: 5   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 1980   suma 1980   residuo 0

**Por que ninguna pieza pasa la vara.** `R2` diagnostica que la ayuda que el tecnico busca es siempre tecnica, y menciona de pasada tres patrones (el vendedor busca produccion, el de produccion busca vendedor, todos buscan contable): son patrones observados, no un inventario de medios que el libro mande ejecutar. `R3` es el caso de Harry, con la etiqueta que el propio libro le pone (*Management by Abdication* en vez de *Delegation*), y una etiqueta diagnostica es el nombre de un error, no el de un medio. `R4` es la escalada del mismo caso. `R5` es la bisagra de cierre hacia el capitulo siguiente. Ninguna pieza nombra un inventario propio de medios, etapas u objetos de trabajo: el capitulo entero diagnostica un sintoma y no prescribe.

### LA FRONTERA CONTRA LA VUELTA 1, IDENTICA AL DIGITO Y NO RECORTADA DE NUEVO

*`G1.2` de la vuelta 1 ya habia cortado las once unidades del lote (`cap_01` a `cap_11`) con este mismo instrumento, y su tabla global daba `cap_05: 4 piezas, cuerpo 2400` y `cap_06: 5 piezas, cuerpo 1980`. Esta vuelta vuelve a correr el instrumento sobre el fichero de hoy, y no copia esa cifra vieja (`EXTRACTOR.md` 5):*

    $ diff .gerber_v1/frontera_cap05.txt .gerber_v2/frontera_cap05.txt
    (vacio)
    $ diff .gerber_v1/frontera_cap06.txt .gerber_v2/frontera_cap06.txt
    (vacio)

**Lo que esto prueba, y lo que no.** Que el corte no cambio de la vuelta 1 a hoy: el fichero fuente no se movio y el instrumento tampoco. **No prueba que la clasificacion de cada pieza sea correcta**: esa la sostiene la lectura hecha en este mismo turno, con las `149` y las `221` lineas de los dos capitulos leidas enteras y sin paginar (`fuentes/gerber_emyth/cap_05.md` y `fuentes/gerber_emyth/cap_06.md` completos).

## G2.3. TAREA 2: **LOS CANDIDATOS QUE EL CAPITULO DE**. **CERO EN LOS DOS, Y LA RAZON ESCRITA PIEZA A PIEZA**. **CERRADA**

**CERO candidatos de `cap_05`. CERO candidatos de `cap_06`.** Las razones pieza a pieza estan en `G2.2` y no se repiten aqui (`D.47`, modo austero: nada que el registro ya diga).

Sin candidato no hay ficha que escribir en `cuarentena/gerber_emyth/`, y por tanto ningun `python forja.py informe` que correr: la aduana en seco de `EXTRACTOR.md` 16 es un paso del ciclo POR candidato, y sin candidato el ciclo no arranca. `cuarentena/gerber_emyth/` sigue en `10` ficheros, medido en `G2.1` y sin cambio hasta el cierre (`G2.8`).

**Y es un resultado, no un silencio** (encargo, seccion 3.2). Dos capitulos que describen sin mandar son el material que la vara de `EXTRACTOR.md` 9 esta escrita para rechazar, y el propio encargo ya adelanto el patron con el ejemplar de Grove (`cap_08` y `cap_09` cero, releidos enteros y firmados, `docs/CIERRE_LOTE_7_GROVE.md` seccion 3). Estos dos son el mismo caso: diagnostico narrado en primera persona por el consultor, con el dialogo de Sarah como vehiculo, y ninguna pieza nombra un medio, una etapa o un objeto de trabajo del propio libro.

## G2.4. TAREA 3: **`PASOS INVENTADOS POR CAPITULO`, UNA FILA POR CAPITULO Y NO UNA SOLA CIFRA GLOBAL** (`AUDITOR_FORJA.md` 8). **CERRADA**

<!-- TALLADO: parcial salida=.gerber_v2/frontera_cap05.txt,.gerber_v2/frontera_cap06.txt -->

| capitulo | candidatos nuevos | pasos escritos | PUENTE | pasos inventados |
|---|---:|---:|---:|---|
| `cap_05` | `0` | `0` | `0` | **SIN SUPERFICIE** |
| `cap_06` | `0` | `0` | `0` | **SIN SUPERFICIE** |
| **la vuelta 2 entera** | **`0`** | **`0`** | `0` | **SIN SUPERFICIE** |

**Por que `SIN SUPERFICIE` y no una razon numerica (`D.59`).** Una razon no se publica sin numerador y sin denominador, y aqui el denominador (pasos escritos) es cero: cero sobre cero no es una razon, es la ausencia de superficie sobre la que medir. Es el mismo tratamiento que `docs/CIERRE_LOTE_7_GROVE.md` seccion 2 le dio a `cap_08`, `cap_09` y `cap_18`.

## G2.5. TAREA 4: **LA MUESTRA DE FIDELIDAD, SEMILLA `g2`**. **CERRADA**

Salida de `python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_05,cap_06 --semilla g2`, guardada en `.gerber_v2/muestra_fidelidad.txt`:

<!-- TALLADO: salida=.gerber_v2/muestra_fidelidad.txt -->

    MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO (D.58)
      libro    : gerber_emyth
      semilla  : g2
      capitulos: cap_05, cap_06

      RELEIDO ENTERO : cap_05
      POR MUESTRA    : cap_06, 15 pasos cada uno

      EL DISPARADOR: si la muestra de un capitulo pasa del 10 por ciento de
      pasos inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.

      --- cap_06: 0 paso(s) en la muestra

      --- cap_05: ENTERO, 0 paso(s), no hay muestra que elegir

**La semilla eligio `cap_05` para relectura ENTERA y `cap_06` para muestra, y no lo elijo yo.** Los dos dan `0` pasos porque los dos tienen `0` candidatos en la bandeja: no hay pasos que muestrear ni pasos que releer, asi que la unica verificacion que queda, y la que el encargo pide en su seccion 3.2, es leer el fichero entero y decir contra que se leyo.

**Y eso se hizo en los dos, no solo en el que la semilla marco ENTERO.** `fuentes/gerber_emyth/cap_05.md` completo, `L1` a `L149`, y `fuentes/gerber_emyth/cap_06.md` completo, `L1` a `L221`, los dos leidos sin paginar en este mismo turno. La frontera de `G2.2` cubre las `149` y las `221` lineas del cuerpo (`L8` en adelante) sin hueco ni solape: si algo se hubiera escapado de la lectura, el residuo de esa frontera no cerraria en `0`.

## G2.6. LA DEUDA DEL ENCARGO: `cap_01` A `cap_03`, HUECO CONOCIDO Y NO DESLIZ

El encargo, seccion 4, manda anotar en `docs/loop/DEUDA.jsonl` que `cap_01`, `cap_02` y `cap_03` de `gerber_emyth` siguen sin minar, con su cita. Se anoto antes de correr `G2.1`, por eso esa seccion se declara como estado intermedio:

    $ python scripts/deuda.py --anotar --vuelta 2 --especie "hueco conocido" --cita "docs/loop/PROMPT_SIGUIENTE.md seccion 4, encargo de la VUELTA 2 del frente gerber_emyth" --que "..."
    ANOTADA d094: cap_01, cap_02 y cap_03 de gerber_emyth siguen sin m

La linea completa, tal como quedo escrita en `docs/loop/DEUDA.jsonl`:

    {"anotada": "2026-09-21 07:58:37", "cita": "docs/loop/PROMPT_SIGUIENTE.md seccion 4, encargo de la VUELTA 2 del frente gerber_emyth", "especie": "hueco conocido", "id": "d094", "que": "cap_01, cap_02 y cap_03 de gerber_emyth siguen sin minar. No es un desliz: el fundador mando empezar el frente en cap_05 (frontera heredada entre cap_04 y cap_07, ya minados), y el encargo de esta vuelta lo repite en su seccion 4 como restriccion expresa (NO TOCAS cap_01, cap_02 ni cap_03). NO ES BLOCANTE: se anota para que ningun auditor futuro lo lea como hueco de lectura no declarado", "tipo": "deuda", "vuelta": "2"}

**NO ES BLOCANTE**, tal como el encargo lo declara: es informacion para el auditor, no una tarea abierta de esta vuelta.

## G2.7. DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO (`EXTRACTOR.md` 8)

| # | discutible | por que lo marco |
|---:|---|---|
| 1 | clasifique `cap_05` `R2` (las tres fases del negocio: Infancy, Adolescence, Maturity) como POSTURA por la restriccion 1 de `EXTRACTOR.md` 9.1 (inventario de fases del negocio, no de medios). Si el auditor lee esas tres fases como la cabeza de una serie (`D.37`) con `cap_05`, `cap_06` y el resto del libro como sus partes, la cabeza tendria que vivir en otro sitio y esta vuelta no la cablearia | es la lectura mas discutible de las dos fronteras: diagnostico contra estructura de serie no es una frontera mecanica |
| 2 | clasifique `cap_06` `R3` (Harry, *Management by Abdication*) sin candidato, aunque el libro le pone nombre propio a un error frente a su alternativa (*Delegation*). Un nombre de ERROR no es un medio a ejecutar, pero si el auditor lee esa contraposicion como el inventario de dos vias nombradas una a una, podria pedir otra lectura de ese tramo | es el punto donde el capitulo mas se acerca a nombrar algo accionable, y decido que no basta |
| 3 | acepte identica la frontera de la vuelta 1 sin volver a discutir sus limites de linea (por ejemplo, si `cap_05` `R3`, de `58` lineas, deberia partirse en dos). No lo hice porque el residuo cierra en `0` y el instrumento es el mismo, pero una pieza mas fina podria haber aislado mejor algun fragmento dentro de ella | es donde mas cedi trabajo propio a un corte ya hecho, y prefiero declararlo a que se descubra en la auditoria |

## G2.8. EL CIERRE, RECOMPUTADO AL CIERRE (`EXTRACTOR.md` 4)

### G2.8.a. LAS TRES GUARDAS Y EL CIERRE DE VUELTA

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python tests/test_aceptacion.py
    total: 343 pruebas, 0 fallos, 0 errores

### G2.8.b. EL ESTADO AL CIERRE, RECOMPUTADO Y NO COPIADO DE LA APERTURA (`EXTRACTOR.md` 4)

| pieza | al abrir (`G2.1`) | al cerrar | diferencia |
|---|---:|---:|---|
| nodos en el grafo | `346` | **346** | `0` |
| veredictos escritos | `740` | **740** | `0` |
| candidatos en bandeja de `gerber_emyth` | `10` | **10** | `0` |
| ficheros de dato movidos por esta vuelta | | **0** | `git diff --name-only 072b49f..HEAD -- dataset/ bitacora/ censos/ config/pares_mutuos.jsonl`: vacio |

**`346`, `740` y `10`: identicos a la apertura de esta misma vuelta (`G2.1`).** Ninguna tarea de esta vuelta toco el grafo, `bitacora/` ni `config/pares_mutuos.jsonl`: `G2.2` y `G2.5` solo leen, `G2.3` cierra en cero candidatos y por tanto cero fichas, y `G2.6` escribio unicamente en `docs/loop/DEUDA.jsonl`, que no es sede de dato (`EXTRACTOR.md` 14). Cero averia.

### G2.8.c. LA TABLA DE CIERRE DE TAREAS (`D.52`)

    $ python scripts/tabla_de_cierre.py --escribir
    ============================================================================
    TABLA DE CIERRE DE TAREAS (D.52): toda tabla del reporte declara su instrumento
    ============================================================================
      libro de la linea : gerber_emyth
      filas             : 5
      SIN COMPROBAR  `1`  ninguna afirmacion de la forma 'N de M del capitulo' con su cap_NN
      SIN COMPROBAR  `2`  ninguna afirmacion de la forma 'N de M del capitulo' con su cap_NN
      SIN COMPROBAR  `3`  ninguna afirmacion de la forma 'N de M del capitulo' con su cap_NN
      SIN COMPROBAR  `4`  ninguna afirmacion de la forma 'N de M del capitulo' con su cap_NN
      SIN COMPROBAR  `5`  ninguna afirmacion de la forma 'N de M del capitulo' con su cap_NN

    ESCRITA la tabla regenerada en docs\loop\TABLA_DE_CIERRE.txt

    TABLA DE CIERRE VERDE: ninguna celda medible difiere del dato.

**Las cinco filas son `SIN COMPROBAR` porque ninguna afirma `N de M del capitulo`**: esta vuelta cierra en `0` candidatos, asi que esa forma no aplica a ninguna de las cinco tareas.

<!-- TALLADO: script=scripts/tabla_de_cierre.py salida=docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_gerber_v2.txt -->

| # | tarea | como cerro |
|---:|---|---|
| `1` | la frontera de `cap_05` y `cap_06`, cerrada contra el cuerpo al digito | **CERRADA en `G2.2`**: `2` de `2` unidades con residuo `0`, cero solapes y cero lineas sin cubrir, identica byte a byte a la de la vuelta 1 |
| `2` | los candidatos que el capitulo de, cada uno con su informe en el acto | **CERRADA en `G2.3`**: `0` candidatos en los dos capitulos, razon pieza a pieza en `G2.2` |
| `3` | `PASOS INVENTADOS POR CAPITULO`, una fila por capitulo | **CERRADA en `G2.4`**: las dos filas en `SIN SUPERFICIE` |
| `4` | la muestra de fidelidad con la semilla `g2` | **CERRADA en `G2.5`**: `cap_05` releido ENTERO y `cap_06` por muestra, los dos con `0` pasos, y los dos leidos enteros a mano ademas |
| `5` | el cierre | **CERRADA en `G2.8`**: estado recomputado (`346`/`740`/`10`), guardas en VERDE, `2` capitulos y `0` candidatos del tramo, `3` discutibles marcados |

**Archivada antes de sobrescribir**, comprobando primero que la version viva seguia siendo la de la vuelta 62 de la serial (sin uso propio de este frente hasta hoy):

    $ git hash-object docs/loop/TABLA_DE_CIERRE.txt
    e0fac5d10018d9bf513aa7c6c98c961f415e6319
    $ git hash-object docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_v62.txt
    e0fac5d10018d9bf513aa7c6c98c961f415e6319

**Los dos hashes coinciden: la version viva era intacta la de `grove_high_output` vuelta 62, sin uso propio de este frente hasta hoy.** Ahora se sobrescribe con la de esta vuelta:

    $ python scripts/tabla_de_cierre.py --escribir   (arriba)
    $ cp docs/loop/TABLA_DE_CIERRE.txt docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_gerber_v2.txt
    $ git hash-object docs/loop/TABLA_DE_CIERRE.txt
    4c93373e3be91ae4a417ef7340047421af281c90
    $ git hash-object docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_gerber_v2.txt
    4c93373e3be91ae4a417ef7340047421af281c90

### G2.8.d. LAS CONDICIONES DE PARADA, REPASADAS UNA A UNA (`EXTRACTOR.md` 7)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| una pregunta de doctrina | ninguna: ~~los dos discutibles~~ **CORRECCION DECLARADA (vuelta 3 del frente, `d095`, `ACTA G2` seccion 3.1): son `3` discutibles, no `2`. `G2.7` tiene tres filas y mi propio `G2.8.c` de esa misma vuelta ya decia `3`** discutibles de `G2.7` son de lectura, no de regla, y no piden doctrina nueva | **NO ES PARADA** |
| una caida de dato | ninguna: `0` ficheros de `dataset/`, `bitacora/`, `censos/` ni `config/pares_mutuos.jsonl` movidos (`G2.8.b`) | **NO ES PARADA** |
| algo contradice una regla vigente o una cifra publicada con su corte | nada: la frontera de la vuelta 1 se reproduce identica y el saldo del encargo (`10` candidatos, `4` capitulos) coincide con lo medido en `G2.1` | **NO ES PARADA** |
| una guarda en rojo | ninguna: las tres de `G2.8.a` en VERDE | **NO ES PARADA** |
| una operacion cuyo texto no alcance para ejecutarse sin decidir | ninguna: las cuatro tareas del encargo estaban escritas enteras | **NO ES PARADA** |

**NINGUNA DE LAS CINCO SE CUMPLE. ESTE TURNO CIERRA SIN PARADA**, y `docs/loop/PARA_ALEXIS.md` sigue sin tocar y no es mia (`EXTRACTOR.md` 14).

## G2.9. CREDITO Y LO QUE PROPONGO

    $ python forja.py credito --anotar --especie REPORTE --vuelta 2 --tanda "G2" --racha "1 de 3" --cita "REPORTE.md seccion G2"
    ANOTADO en docs/loop/CREDITO_gerber_emyth.jsonl:
      {"cita": "REPORTE.md seccion G2", "especie": "REPORTE", "racha": "1 de 3", "tanda": "G2", "tipo": "tanda", "vuelta": 2}
    $ python forja.py credito
    CREDITO DE LA LINEA 'gerber_emyth' (D.48)
      registro: docs/loop/CREDITO_gerber_emyth.jsonl
      tandas: 1, en 1 suceso(s) de especie

      especie            racha      de donde sale
      ----------------------------------------------------------------------
      REPORTE            1 de 3     G2

      CREDITO ENTERO: ninguna especie en su tope.

### Propuestas al auditor, todas en mi sede y ninguna adjudicada por mi

1. **Con `cap_05` y `cap_06` cerrados a cero y firmados, el hueco entre `cap_04` y `cap_07` queda cerrado.** El frente tiene ahora `cap_04`, `cap_05`, `cap_06`, `cap_07`, `cap_08` y `cap_11` minados: seis de veintidos. Propongo que la vuelta siguiente suba a los tres capitulos que `D.58` permite en regimen ligero, ya que esta (la segunda tras la reanudacion) cerro limpia y sin parada, tal como el propio encargo (seccion 3) preveia.
2. **`cap_01`, `cap_02` y `cap_03` siguen en deuda (`d094`)**, y quedan para cuando el auditor o el fundador decidan si entran en el mismo frente o se dejan fuera del corte, como ya se declaro en el encargo.

### Cola declarada

Ninguna. Las cuatro tareas del encargo cierran en esta misma vuelta y no dejan tarea pendiente propia.

---

# FRENTE `gerber_emyth`, VUELTA 3: **EL REMEDIO HEREDADO DE LA `ACTA G1` CUMPLIDO, `cap_09` Y `cap_10` MINADOS A CERO, Y `cap_12` DA UN CANDIDATO** (`D.45`, frente en paralelo: **NO INSERTA**)

> ## **ESTE BLOQUE SE ESCRIBE EN LA RAMA `extraccion-gerber_emyth`, CON `MODO_INSERCION=cuarentena`. CERO INSERCIONES, Y NO POR FALTA DE CANDIDATO BUENO: PORQUE LA INSERCION ES UNA AUTORIZACION DEL FUNDADOR Y ESTA CORRIDA NO LA TRAE.**
>
> **MODO AUSTERO (`D.47`) VIGENTE.** Nada que el registro ya diga, cifras talladas, discutibles por
> numero y linea. **Las guardas de dato, intactas**: la aduana en seco candidato a candidato, la
> fidelidad `D.30` con su relectura contra el parrafo, `D.41` y `D.42`.

## G3.0. EL ESQUELETO DE LA VUELTA (`EXTRACTOR.md` 3)

| # | tarea del encargo | como cierra | donde |
|---:|---|---|---|
| 1 | el remedio heredado de la `ACTA G1` (`d095`): cuatro celdas con correccion declarada, y correr la comprobacion de secciones sobre el bloque propio | **CERRADA** | `G3.2`, comprobacion en `G3.8.b` |
| 2 | la frontera de `cap_09`, `cap_10` y `cap_12`, cerrada contra el cuerpo al digito | **CERRADA**: `3` de `3` con residuo `0`, cero solapes y cero lineas sin cubrir | `G3.3` |
| 3 | los candidatos que cada capitulo de, con su informe en el acto | **CERRADA**: `2` capitulos en cero y `1` candidato de `cap_12`, con su informe corrido y su vecino leido | `G3.4` |
| 4 | `PASOS INVENTADOS POR CAPITULO`, fila por capitulo | **CERRADA**: `2` filas `SIN SUPERFICIE` y una en `0,00` por ciento | `G3.5` |
| 5 | la muestra de fidelidad, semilla `g3` | **CERRADA**: `cap_12` releido ENTERO con sus `6` pasos, `cap_09` y `cap_10` por muestra con `0` pasos cada uno | `G3.6` |
| | el cierre: guardas, cifras recomputadas, discutibles marcados, commit y push | **CERRADO** | `G3.7` a `G3.9` |

**LAS CINCO TAREAS ENTREGADAS Y CERO COLA** (`EXTRACTOR.md` 1.3, tope de cinco).

## G3.1. LA APERTURA, MEDIDA ANTES DE LA PRIMERA OPERACION (`EXTRACTOR.md` 4)

Salida de `python .gerber_v3/apertura.py` (copia sin cambios de `.gerber_v2/apertura.py`), guardada
en `.gerber_v3/apertura.txt`:

<!-- TALLADO: parcial salida=.gerber_v3/apertura.txt -->

| pieza | al abrir | de donde sale |
|---|---:|---|
| nodos en el grafo | **346** | `dataset/nodos.jsonl` |
| veredictos escritos | **740** | `bitacora/VEREDICTOS.jsonl` |
| unidades de `gerber_emyth` | **22** | `PATRON: fuentes/gerber_emyth/cap_*.md` |
| palabras de cuerpo del libro | **62648** | `PATRON: fuentes/gerber_emyth/cap_*.md` |
| candidatos en bandeja de `gerber_emyth` | **10** | `PATRON: cuarentena/gerber_emyth/*.json` |
| clave `gerber_emyth` en la tabla canonica | **SI** | `fuentes/FUENTES_CANONICAS.json` |
| rama activa | `extraccion-gerber_emyth` | `git rev-parse --abbrev-ref HEAD` |
| commit de apertura | `07aa6f2` | `git rev-parse --short HEAD` |

**CONTRA EL ENCARGO (seccion 1):** `346` nodos, `740` veredictos y `10` candidatos en bandeja me salen
al digito. El commit de apertura es `07aa6f2`, que es el que el encargo anuncia como *el de mi acta,
que este cierre anade*. **Cero discrepancia que declarar.** Los seis capitulos minados y adjudicados
que el encargo publica (`cap_04`, `cap_05`, `cap_06`, `cap_07`, `cap_08`, `cap_11`) no los vuelvo a
medir con instrumento propio: no hay campo de `dataset/nodos.jsonl` ni de `cuarentena/` que registre
"capitulo leido y adjudicado en cero", y esa es exactamente la cola `d088`/`d096` que el encargo mismo
avisa **no tocar**.

## G3.2. TAREA 1: **EL REMEDIO HEREDADO DE LA `ACTA G1`, CUMPLIDO** (`d095`). **CERRADA**

*`d095` pedia tres cosas: tres celdas del bloque `G1` con correccion declarada y tachado en su sitio, y
correr `python .v1g_auditor/secciones.py` (o su equivalente sobre el bloque propio) antes de cerrar
cualquier reporte. El encargo de esta vuelta anade una cuarta celda, la de `G2.8.d` que dice `los dos
discutibles` donde hay `3`.*

**LAS CUATRO CORRECCIONES, CADA UNA CON TACHADO EN SU SITIO Y SIN BORRAR NADA:**

| # | donde | que decia | que dice ahora |
|---:|---|---|---|
| 1 | `docs/loop/archivo/gerber_emyth/REPORTE_frente_hasta_v1.md`, celda de `G1.10.d` (fila *una guarda en rojo*) | citaba `G1.10.e`, seccion que no existe | tachado, con `grep -n "^#\{2,4\} G1\.10\.e"` corrido hoy contra ese mismo fichero: **cero coincidencias**, y la guarda real que si se puede citar es la de `G1.5` |
| 2 | mismo fichero, fila `CERRADO` del esqueleto `G1.0` | `CERRADO` sin matiz | tachado, con la fecha exacta en que fue falsa (commit `a218170`, `G1.9` y `G1.10` no existian todavia) y en que commit se volvio cierta (`abf7515`, el mismo bloque las escribe mas abajo) |
| 3 | mismo fichero, apertura de `G1.9` | prometia *cerrarse con su salida pegada* | tachado, declarando que esa promesa no se cumplio (el informe de lote nunca termino, `91` bytes de cabecera) y citando donde vive el saldo real: `docs/loop/paradas/2026-09-17-gerber-la-racha-y-la-linea-vieja-RESUELTA.md` seccion 3, `3` ENTRARIAN, `7` BLOQUEARIAN, `0` CAERIAN, `0` CHOCAN |
| 4 | `docs/loop/REPORTE.md`, celda de `G2.8.d` (fila *una pregunta de doctrina*), linea `57681` | `los dos discutibles` | tachado, `3` discutibles, citando que `G2.7` tiene tres filas y que mi propio `G2.8.c` de esa misma vuelta ya decia `3` |

**LO QUE NO HAGO, por la misma razon que `G1.10.a` ya dio:** no reescribo ninguna celda por encima,
no borro el texto viejo. Es correccion declarada, no enmienda muda.

**Y NO TOCO `.v1g_auditor/secciones.py`**, que es sede del auditor (`d095` punto 2, y el encargo lo
repite): la copia adaptada al bloque de esta vuelta vive en `.gerber_v3/secciones.py`, con el mismo
patron de catorce lineas y solo dos cambios de texto (`G1` por `G3`, y el encabezado de vuelta que
busca). Se corre al cerrar, sobre el bloque que este mismo documento termina de escribir, y su salida
va en `G3.8.b`.

## G3.3. TAREA 2: **LA FRONTERA DE `cap_09`, `cap_10` Y `cap_12`, CERRADA CONTRA EL CUERPO AL DIGITO**. **CERRADA**

*El instrumento es `.gerber_v2/frontera.py`, copiado sin cambio a `.gerber_v3/frontera.py`: cortar estas
tres unidades con el es la misma regla aplicada al mismo libro.*

    $ diff .gerber_v2/frontera.py .gerber_v3/frontera.py
    (vacio, cero cambios en el instrumento)

### LA FRONTERA DE `cap_09` (`Cap. 7`, *The Turn-Key Revolution*), **6 piezas y CERO con procedimiento**

Salida de `python .gerber_v3/frontera.py fuentes/gerber_emyth/cap_09.md .gerber_v3/piezas_cap09.txt`,
guardada en `.gerber_v3/frontera_cap09.txt`:

<!-- TALLADO: salida=.gerber_v3/frontera_cap09.txt -->

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L19 | **47** | el numero del capitulo, el rotulo THE TURN-KEY REVOLUTION y el epigrafe de Fritjof Capra (The Turning Point) | **RESIDUO: rotulo y epigrafe** |
| `R2` | L20 a L27 | **155** | la Turn-Key Revolution definida como una forma de hacer negocios capaz de transformar cualquier negocio pequeno de caos a orden | **POSTURA** |
| `R3` | L28 a L78 | **608** | The Franchise Phenomenon: la historia de Ray Kroc y McDonald's, y las cifras del fenomeno de las franquicias en Estados Unidos | **CASO** |
| `R4` | L79 a L110 | **312** | Turning the Key: la diferencia entre la franquicia de nombre comercial y la Business Format Franchise, y que el producto real de un negocio es el negocio mismo | **POSTURA** |
| `R5` | L111 a L172 | **605** | Selling the Business Instead of the Product: Ray Kroc piensa su negocio como el producto y al franquiciado como su cliente mas importante, y el paso a trabajar SOBRE el negocio | **POSTURA y CASO** |
| `R6` | L173 a L233 | **1118** | el dialogo con Sarah sobre McDonald's como modelo para cualquier pequeno negocio | **CASO** |
| **el cuerpo entero** | **L8 a L233** | **2845** | **suma de las piezas: 2845** | **residuo sin asignar: 0** |

    piezas: 6   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 2845   suma 2845   residuo 0

**Por que ninguna pieza pasa la vara de `EXTRACTOR.md` 9 y 9.1.** `R2` define la Turn-Key Revolution sin
nombrar medios propios: es la tesis del capitulo, no un inventario. `R3` y `R6` cuentan la historia de
Ray Kroc y el dialogo con Sarah: son caso e ilustracion, no procedimiento del lector. `R4` distingue dos
tipos de franquicia y afirma que el producto es el negocio mismo: postura conceptual, sin medios
nombrados uno a uno que el lector deba ejecutar. `R5` mezcla postura (ir a trabajar SOBRE el negocio) y
el caso de Ray Kroc pensando su negocio como producto: ninguna frase pone un inventario propio de
medios, etapas u objetos de trabajo.

### LA FRONTERA DE `cap_10` (`Cap. 8`, *The Franchise Prototype*), **5 piezas y CERO con procedimiento**

Salida de `python .gerber_v3/frontera.py fuentes/gerber_emyth/cap_10.md .gerber_v3/piezas_cap10.txt`,
guardada en `.gerber_v3/frontera_cap10.txt`:

<!-- TALLADO: salida=.gerber_v3/frontera_cap10.txt -->

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L19 | **83** | el numero del capitulo, el rotulo THE FRANCHISE PROTOTYPE y el epigrafe de Robert M. Pirsig (Zen and the Art of Motorcycle Maintenance) | **RESIDUO: rotulo y epigrafe** |
| `R2` | L20 a L41 | **322** | el Franchise Prototype definido como el modelo de trabajo del sueno del franquiciador, el sistema que integra todo lo necesario para que el negocio funcione | **POSTURA** |
| `R3` | L42 a L86 | **462** | el caso de McDonald's: cada detalle del sistema probado en el Prototipo, las papas fritas, las hamburguesas, la Universidad de la Hamburguesologia y el Turn-Key Operation | **CASO** |
| `R4` | L87 a L135 | **455** | lo que el Franchise Prototype es en verdad, la lista de empresas donde ya existe, y las preguntas retoricas sobre como construir el tuyo | **POSTURA** |
| `R5` | L136 a L145 | **89** | la reaccion de Sarah, que ya lo entiende | **RESIDUO: bisagra** |
| **el cuerpo entero** | **L8 a L145** | **1411** | **suma de las piezas: 1411** | **residuo sin asignar: 0** |

    piezas: 5   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 1411   suma 1411   residuo 0

**Por que ninguna pieza pasa la vara.** `R2` y `R4` son conceptuales: definen que es el Prototipo y para
que sirve, sin una lista propia de medios que el lector deba ejecutar. `R3` es el caso de McDonald's con
sus detalles (siete minutos de las papas, diez de las hamburguesas, el patron de los pepinillos): son
los estandares PROPIOS de McDonald's, ilustracion de la disciplina de un franquiciador, no un
procedimiento que el libro mande al lector replicar con esos mismos numeros. `R5` es la bisagra de
cierre hacia el capitulo siguiente.

### LA FRONTERA DE `cap_12` (`Cap. 10`, *The Business Development Process*), **8 piezas y UN CANDIDATO EN `R5`**

Salida de `python .gerber_v3/frontera.py fuentes/gerber_emyth/cap_12.md .gerber_v3/piezas_cap12.txt`,
guardada en `.gerber_v3/frontera_cap12.txt`:

<!-- TALLADO: salida=.gerber_v3/frontera_cap12.txt -->

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L19 | **57** | el numero del capitulo, el rotulo THE BUSINESS DEVELOPMENT PROCESS y el epigrafe de Thomas J. Peters y Robert H. Waterman Jr. (In Search of Excellence) | **RESIDUO: rotulo y epigrafe** |
| `R2` | L20 a L21 | **39** | la cabeza que nombra las tres actividades del Business Development Process: Innovation, Quantification y Orchestration | **POSTURA** |
| `R3` | L22 a L83 | **1055** | la seccion Innovation entera: creatividad contra innovacion, y los tres ejemplos THE INNOVATION de experimentos de venta al detalle | **POSTURA y CASO** |
| `R4` | L84 a L94 | **101** | el subtitulo Quantification y por que cuantificar una innovacion importa | **POSTURA** |
| `R5` | L95 a L95 | **134** | el parrafo que enumera uno a uno los seis pasos para cuantificar el impacto de una innovacion | **INVENTARIO PROPIO: NACE 1 CANDIDATO** |
| `R6` | L96 a L147 | **326** | el resto de Quantification: el ejemplo del traje azul, la lista abierta de preguntas sobre los numeros del negocio (termina en y asi sucesivamente) y el cierre | **POSTURA** |
| `R7` | L148 a L221 | **687** | la seccion Orchestration entera: la eliminacion de la discrecion, si no lo has orquestado no lo posees, y el cierre que nombra otra vez las tres actividades | **POSTURA** |
| `R8` | L222 a L293 | **1807** | el dialogo con Sarah sobre la Orquestacion, la metafora del aprendizaje del pastel de fruta y la maestria del artesano | **CASO y POSTURA** |
| **el cuerpo entero** | **L8 a L293** | **4206** | **suma de las piezas: 4206** | **residuo sin asignar: 0** |

    piezas: 8   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 4206   suma 4206   residuo 0

> **CORRECCION DECLARADA (vuelta 4, `d101`, `G4.2`), SIN BORRAR LA TABLA DE ARRIBA:** la tabla que
> antecede sigue TALLADA contra `.gerber_v3/frontera_cap12.txt` (`D.41`) y por eso no se toca celda
> a celda: es el registro exacto de lo que midio la vuelta 3, y tocarlo la volveria a comparar contra
> un instrumento que ya no dice eso. **La fila `R3` (`L22` a `L83`, `docs/loop/REPORTE.md:57859`,
> clasificada de golpe `POSTURA y CASO`) estaba incompleta**: leida pieza por pieza en la vuelta 4
> (frontera fina en `G4.2`, instrumento `.gerber_v4/frontera_cap12.txt`), el tramo `L51` a `L58`
> (el saludo) y el tramo `L63` a `L64` (el traje azul) SI traen inventario propio y nacen candidato;
> el resto de `R3` (incluido `L69` a `L70`, tocar el brazo) sigue sin pasar la vara. El discutible `1`
> de `G3.7` acertaba a medias: la duda que marcaba era real, y la respuesta no era *ningun* candidato
> ni *un solo* candidato, eran dos.

**Por que `R5` SI pasa la vara y las otras siete no.** `R5` es una sola frase que enumera `(1)` a `(6)`
sus propios pasos, sin adjetivo de adecuacion en el sitio del criterio: no dice *mide de forma
razonable*, dice *determinando cuantos*, *contando cuantos*, *determinando el valor*. Es la prueba del
manual al pie de la letra: una linea que tarda seis pasos en ejecutarse es un procedimiento nombrado en
una linea. `R2` nombra tres actividades pero no las desarrolla en esa misma linea (marcado como puntero,
`G3.7`). ~~`R3` da tres ejemplos concretos (*THE INNOVATION*) presentados como casos de clientes propios
(*our clients have found*), no como un inventario que el libro mande ejecutar con esos mismos
terminos (discutible 1, `G3.7`).~~ **CORRECCION DECLARADA (vuelta 4, `d101`): dos de los tres SI
traen inventario propio (el saludo con sus palabras exactas y sus dos ramas, el traje azul con sus
dos etapas y sus ocho prendas) y nacen candidato en `G4.2`; solo el tercero (tocar el brazo) se
queda sin pasar la vara, con su motivo en `G4.2`.** `R4`, `R6`, `R7` y `R8` son postura y dialogo,
sin inventario propio de medios.

## G3.4. TAREA 3: **LOS CANDIDATOS QUE CADA CAPITULO DE, CON SU INFORME EN EL ACTO**. **CERRADA**

**CERO candidatos de `cap_09`. CERO candidatos de `cap_10`. UN candidato de `cap_12`.** Las razones
pieza a pieza de los dos capitulos en cero estan en `G3.3` y no se repiten (`D.47`).

### El candidato de `cap_12`

`cuarentena/gerber_emyth/cuantificar_impacto_innovacion_6_pasos.json`, con sus **6** pasos transcritos
de `R5` (`L95`), cita pegada en `.gerber_v3/cita_cap12_L95.txt` (`D.35`):

    For example, how would you know that by changing the words you use to greet an incoming
    customer you produced a 16-percent increase in sales unless you quantified it by (1)
    determining how many people came in the door before the Innovation was put into effect;
    (2) determining how many people bought products and what the dollar value of those
    products were before you changed the words and what you said to produce those sales;
    (3) counting the number of people who came in the door after you changed the words; (4)
    counting the number of people who purchased something; (5) determining the average unit
    value of a sale; and (6) determining what the improvement was as a result of your
    Innovation? These numbers enable you to determine the precise value of your Innovation.

**RELECTURA DE FIDELIDAD `D.30` EN EL ACTO: `6` pasos, `6` TRANSCRIPCION, `0` PUENTE.** No hay
destinatario, periodo ni responsable que el libro no ponga y que el candidato invente: el libro habla en
segunda persona todo el capitulo y esta frase no fija cada cuanto se cuantifica ni quien lo hace, y el
candidato no lo pone tampoco.

### Su informe, corrido en el acto (`EXTRACTOR.md` 16)

Salida de `python forja.py informe cuarentena/gerber_emyth/cuantificar_impacto_innovacion_6_pasos.json`,
guardada en `.gerber_v3/informe_cuantificar_impacto_innovacion.txt`:

<!-- TALLADO: parcial salida=.gerber_v3/informe_cuantificar_impacto_innovacion.txt -->

    poblacion del barrido       : 451   (346 del grafo mas 105 que esperan en bandejas)
    ENTRARIAN sin leer nada          : 0
    BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [BLOQUEARIA] cuantificar_impacto_innovacion_6_pasos
        vecino dar_valor_constante_cuatro_publicos  [levantada por: similitud_texto]
          similitud_texto 0.396 | familia_id 0.000 | paso_contra_nodo 0.432
          paso 3 del candidato contra paso 4 de dar_valor_constante_cuatro_publicos

**`0 CAERIA`. No hace falta corregir nada: el ciclo de `EXTRACTOR.md` 16 cierra a la primera.**

**EL UNICO VECINO, LEIDO** (`EXTRACTOR.md` 11: por debajo de `0,4` no es la banda que obliga a leer
antes que ninguna otra, pero es el unico vecino de este candidato y se lee igual, seccion 11: *las
senales ordenan, nunca deciden*). `dar_valor_constante_cuatro_publicos` sale de `cap_11` (Cap. 9,
*Working On Your Business, Not In It*) y es la parte 1 de la serie de la regla 1 del prototipo: formas de
dar valor a los cuatro publicos del negocio. Mi candidato sale de `cap_12` (Cap. 10, *The Business
Development Process*) y es un metodo de medicion. **El parecido que la senal ve es lexico**: *cuenta*
(`cuenta como valor`, `cuenta cuantas personas`) y *puerta* (`la puerta del negocio`, `entraron por la
puerta`), no conceptual. **VEREDICTO DE LECTURA: `SANO`.** No hay madre ni hija entre los dos: uno
enumera formas de valor, el otro enumera conteos de una medicion. No se escribe en
`bitacora/VEREDICTOS.jsonl` porque esta vuelta no inserta (`D.39`): el veredicto queda declarado aqui,
para que la vuelta que cierre el lote lo tenga delante y no tenga que releerlo desde cero.

## G3.5. TAREA 4: **`PASOS INVENTADOS POR CAPITULO`, UNA FILA POR CAPITULO** (`AUDITOR_FORJA.md` 8). **CERRADA**

<!-- TALLADO: parcial salida=.gerber_v3/frontera_cap09.txt,.gerber_v3/frontera_cap10.txt,.gerber_v3/informe_cuantificar_impacto_innovacion.txt -->

| capitulo | candidatos nuevos | pasos escritos | PUENTE | pasos inventados |
|---|---:|---:|---:|---|
| `cap_09` | `0` | `0` | `0` | **SIN SUPERFICIE** |
| `cap_10` | `0` | `0` | `0` | **SIN SUPERFICIE** |
| `cap_12` | `1` | `6` | `0` | **0,00 por ciento** |
| **la vuelta 3 entera** | **`1`** | **`6`** | `0` | **0,00 por ciento** |

**Por que `SIN SUPERFICIE` en dos filas y una cifra en la tercera (`D.59`).** Cero candidatos es cero
denominador, y una razon no se publica sin numerador y sin denominador. `cap_12` si tiene superficie
(`6` pasos) y su relectura de `G3.4` mide `0` puentes sobre esos `6`, asi que `0,00` por ciento es una
cifra y no un silencio.

## G3.6. TAREA 5: **LA MUESTRA DE FIDELIDAD, SEMILLA `g3`**. **CERRADA**

Salida de
`python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_09,cap_10,cap_12 --semilla g3`,
guardada en `.gerber_v3/muestra_fidelidad.txt`:

<!-- TALLADO: salida=.gerber_v3/muestra_fidelidad.txt -->

    MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO (D.58)
      libro    : gerber_emyth
      semilla  : g3
      capitulos: cap_09, cap_10, cap_12

      RELEIDO ENTERO : cap_12
      POR MUESTRA    : cap_09, cap_10, 15 pasos cada uno

      EL DISPARADOR: si la muestra de un capitulo pasa del 10 por ciento de
      pasos inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.

      --- cap_09: 0 paso(s) en la muestra

      --- cap_10: 0 paso(s) en la muestra

      --- cap_12: ENTERO, 6 paso(s), no hay muestra que elegir

**La semilla eligio `cap_12` para relectura ENTERA, y es justo el unico capitulo con pasos que
releer: sus `6` pasos son los mismos `6` que `G3.4` ya releyo contra `R5` con `0` puentes.** `cap_09` y
`cap_10` dan `0` porque tienen `0` candidatos, y la unica verificacion que queda para ellos es la que
`G3.3` ya hizo: leer el fichero entero y decir contra que se leyo. Los tres, `L1` a `L233`, `L1` a `L145`
y `L1` a `L293`, sin paginar, en este mismo turno; la frontera de `G3.3` cubre las tres sin hueco ni
solape, asi que si algo se hubiera escapado de la lectura el residuo no cerraria en `0`.

## G3.7. DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO (`EXTRACTOR.md` 8)

| # | discutible | por que lo marco |
|---:|---|---|
| 1 | clasifique `cap_12` `R3` (los tres ejemplos *THE INNOVATION*: la frase de saludo, el traje azul, tocar el brazo) como CASO y no como procedimiento, porque el texto los presenta como resultados de *nuestros clientes* y no como un inventario que el libro mande ejecutar con esos terminos exactos. El del traje azul en particular tiene tres pasos concretos (tres semanas de traje marron, tres de traje azul, comparar ventas): si el auditor lo lee como procedimiento propio del libro y no como caso ilustrativo, ahi nace otro candidato | es la lectura mas cercana a la vara de las tres, y la que mas duda me genera de las tres piezas de este bloque |
| 2 | en el candidato de `cap_12`, los pasos 2 a 4 quedan anclados al ejemplo concreto de *cambiar las palabras del saludo* (asi lo escribe el propio parrafo `R5`), mientras que los pasos 1 y 6 ya hablan de *la Innovacion* en generico. Elegi transcribir fiel a esa mezcla en vez de generalizar los pasos 2 a 4 a *tu innovacion*, porque generalizarlos habria sido escribir yo una generalizacion que el parrafo no hace del todo explicita (posible PUENTE si el auditor lee distinto) | es la decision de fidelidad mas fina de todo el candidato, y la que un lector rapido no notaria |
| 3 | `cap_12` `L21` nombra tres actividades (Innovation, Quantification, Orchestration) una a una, que es el supuesto de `D.37`, pero hoy ninguna de las tres existe como nodo cabeza propio: mi candidato es un metodo concreto DENTRO de Quantification, no Quantification como nodo. No cableo ninguna arista `D.37` hoy. Si el auditor lee que mi candidato SI es *la parte Quantification* de esa cabeza, la arista se cablearia distinto | es el mismo patron que `d098` dejo escrito para `cap_05`, y prefiero declararlo a que se descubra en la auditoria |

## G3.8. EL CIERRE, RECOMPUTADO AL CIERRE (`EXTRACTOR.md` 4)

### G3.8.a. LAS TRES GUARDAS

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python tests/test_aceptacion.py
    total: 343 pruebas, 0 fallos, 0 errores

### G3.8.b. LA COMPROBACION DE SECCIONES DE `2.2`, SOBRE ESTE MISMO BLOQUE

Salida de `python .gerber_v3/secciones.py`, guardada en `.gerber_v3/secciones.txt`:

<!-- TALLADO: salida=.gerber_v3/secciones.txt -->

    el bloque del frente empieza en la linea 57716 de docs/loop/REPORTE.md
    secciones que el bloque TIENE      : 15   G3.0 G3.1 G3.2 G3.3 G3.4 G3.5 G3.6 G3.7 G3.8 G3.8.a G3.8.b G3.8.c G3.8.d G3.8.e G3.9
    secciones que el bloque CITA       : 11   G3.1 G3.2 G3.3 G3.4 G3.5 G3.6 G3.7 G3.8.a G3.8.b G3.8.c G3.9
    CITADAS Y QUE NO EXISTEN           : 0

**`0` CITADAS Y QUE NO EXISTEN: el remedio de `d095` punto 2 se cumple entero en esta vuelta.** El
numero de linea de apertura (`57716`) es el que tenia el documento en el instante en que corri el
instrumento, antes de pegar esta misma salida: pegarla desplaza las lineas que le siguen, y por eso se
cita como lo que midio, no como coordenada viva del documento final.

### G3.8.c. EL ESTADO AL CIERRE, RECOMPUTADO Y NO COPIADO DE LA APERTURA

| pieza | al abrir (`G3.1`) | al cerrar | diferencia |
|---|---:|---:|---|
| nodos en el grafo | `346` | **346** | `0` |
| veredictos escritos | `740` | **740** | `0` |
| candidatos en bandeja de `gerber_emyth` | `10` | **11** | `+1` (`cuantificar_impacto_innovacion_6_pasos`) |
| pasos en esa bandeja | `89` | **95** | `+6` |
| ficheros de dato movidos por esta vuelta | | **0** | `git diff --name-only 07aa6f2..HEAD -- dataset/ bitacora/ censos/ config/pares_mutuos.jsonl`: vacio |

**`346` y `740` identicos a la apertura de esta misma vuelta. La bandeja sube de `10` a `11` candidatos y
de `89` a `95` pasos, y es el unico movimiento de esta vuelta**: `G3.2` solo corrige texto de reporte
(que no es sede de dato, `EXTRACTOR.md` 14), `G3.3` solo lee, y `G3.4` escribe un fichero en
`cuarentena/`, que es bandeja y no grafo. Cero averia.

### G3.8.d. LA TABLA DE CIERRE DE TAREAS (`D.52`)

    $ python scripts/tabla_de_cierre.py --escribir

> **CORRECCION DECLARADA de la vuelta 4, y no toca ni una celda de esta tabla.** La linea de abajo decia
> `salida=docs/loop/TABLA_DE_CIERRE.txt` sin `parcial`, y esa es la ruta VIVA del instrumento: la vuelta 4
> la regenero con su propia tabla (`2` filas) al cerrar `G4.5.a`, y desde ese instante el fichero vivo ya
> no sostiene esta tabla de `5` filas. **Es el mismo defecto que el reporte de la linea serial ya
> documento por octava vez** (`docs/loop/REPORTE.md` en torno a la linea `53591`, `D.41`): la ruta viva se
> queda con la tabla de la vuelta que cierra, y la vuelta anterior queda en rojo si nadie toca su marcador.
>
> **LA SALIDA DE ESTA VUELTA 3 NO SE TECLEO NI SE PERDIO: SE SACO DE GIT BYTE A BYTE** y se archivo en
> `docs/loop/archivo/gerber_emyth/TABLA_DE_CIERRE_G3.txt`, con el mismo `git hash-object` antes y
> despues:
>
>     $ git show HEAD:docs/loop/TABLA_DE_CIERRE.txt | git hash-object --stdin
>     a306902cafb3dd905f097a9438ef6d3a27b4b295
>     $ git hash-object docs/loop/archivo/gerber_emyth/TABLA_DE_CIERRE_G3.txt
>     a306902cafb3dd905f097a9438ef6d3a27b4b295
>
> (el `HEAD` de este comando es el commit de cierre de la vuelta 3, `4f2d2af`, no el de esta vuelta 4).

<!-- TALLADO: parcial salida=docs/loop/TABLA_DE_CIERRE.txt -->

| # | tarea | como cerro |
|---:|---|---|
| `1` | el remedio heredado de la `ACTA G1` (`d095`), cuatro celdas corregidas | **CERRADA en `G3.2`**: `4` de `4` celdas con tachado y motivo, comprobacion de secciones en `G3.8.b` |
| `2` | la frontera de `cap_09`, `cap_10` y `cap_12` | **CERRADA en `G3.3`**: `3` de `3` unidades con residuo `0`, cero solapes y cero lineas sin cubrir |
| `3` | los candidatos que cada capitulo de, con su informe en el acto | **CERRADA en `G3.4`**: `2` capitulos en cero, `1` candidato de `cap_12` con informe `0 CAERIA` y su vecino leido `SANO` |
| `4` | `PASOS INVENTADOS POR CAPITULO` | **CERRADA en `G3.5`**: `2` filas `SIN SUPERFICIE`, `1` fila en `0,00` por ciento |
| `5` | la muestra de fidelidad con la semilla `g3` | **CERRADA en `G3.6`**: `cap_12` releido ENTERO (`6` pasos, `0` puente), `cap_09` y `cap_10` por muestra con `0` pasos |

### G3.8.e. LAS CONDICIONES DE PARADA, REPASADAS UNA A UNA (`EXTRACTOR.md` 7)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| una pregunta de doctrina | ninguna: los tres discutibles de `G3.7` son de lectura, no de regla, y no piden doctrina nueva | **NO ES PARADA** |
| una caida de dato | ninguna: `0` ficheros de `dataset/`, `bitacora/`, `censos/` ni `config/pares_mutuos.jsonl` movidos (`G3.8.c`) | **NO ES PARADA** |
| algo contradice una regla vigente o una cifra publicada con su corte | nada: el remedio de `d095` se cumplio con sus cuatro celdas, y el saldo del encargo (`10` candidatos, `6` capitulos minados) coincide con lo medido en `G3.1` | **NO ES PARADA** |
| una guarda en rojo | ninguna: las tres de `G3.8.a` en VERDE | **NO ES PARADA** |
| una operacion cuyo texto no alcance para ejecutarse sin decidir | ninguna: las cinco tareas del encargo estaban escritas enteras | **NO ES PARADA** |

**NINGUNA DE LAS CINCO SE CUMPLE. ESTE TURNO CIERRA SIN PARADA**, y `docs/loop/PARA_ALEXIS.md` sigue sin
tocar y no es mia (`EXTRACTOR.md` 14).

## G3.9. CREDITO Y LO QUE PROPONGO

**NO ADJUDICO MI PROPIA RACHA** (encargo, seccion 7): el numero de `REPORTE` para esta tanda lo escribe
el auditor, con el nombre de su acta en el campo `tanda`, tal como `docs/loop/CREDITO_gerber_emyth.jsonl`
ya muestra para `ACTA G2`.

### Propuestas al auditor, todas en mi sede y ninguna adjudicada por mi

1. **El remedio de `d095` esta cumplido**, con sus cuatro celdas y la comprobacion de secciones en `0`
   (`G3.8.b`). Lo anoto YA como pagado con `python scripts/deuda.py --pagar d095 --vuelta 3 --como
   "..."`, que no es adjudicacion de racha: es el mismo registro que la vuelta `2` uso para anotar
   `d094`, y `docs/loop/DEUDA.jsonl` no esta en la tabla de sedes exclusivas de `EXTRACTOR.md` 14.
2. **El hueco entre `cap_08` y `cap_11` sigue cerrado desde la vuelta `2`, y hoy se le suma el segundo
   hueco: `cap_09` y `cap_10`.** El frente tiene ahora `cap_04` a `cap_08`, `cap_11` y `cap_12` minados:
   ocho de veintidos. El siguiente sin minar en el hueco que queda es `cap_13`, `364` palabras, el mas
   corto del libro.
3. **El discutible 3 de `G3.7` deja un puntero para cuando alguna vuelta futura trabaje la cabeza de las
   tres actividades del proceso de desarrollo del negocio** (`cap_12` `L21`): si nace un nodo cabeza para
   Innovation, Quantification u Orchestration, la arista a este candidato se decide entonces, citando esa
   linea.

### Cola declarada

Ninguna. Las cinco tareas del encargo cierran en esta misma vuelta y no dejan tarea pendiente propia.

---

# FRENTE `gerber_emyth`, VUELTA 4: **CERRAR `cap_12` PRIMERO (`d101`), Y SOLO DESPUES `cap_13` Y `cap_14`** (`D.45`, frente en paralelo: **NO INSERTA**)

> ## **ESTE BLOQUE SE ESCRIBE EN LA RAMA `extraccion-gerber_emyth`, CON `MODO_INSERCION=cuarentena`. CERO INSERCIONES.**
>
> **RACHA REINICIADA CON CONDICION** (`docs/loop/paradas/2026-09-22-gerber-g3-DECISION.md`, punto 1):
> la `TAREA 1` de esta vuelta ejecuta `d101` antes de abrir `cap_13`. **`D.61` (nueva, del banco) manda
> que todo discutible publicado se ejecute o se cierre en la misma vuelta que lo escribe**, y esa figura
> pesa como `CIFRA PUBLICADA`, tope `2` y no `3`.
>
> **MODO AUSTERO (`D.47`) VIGENTE.** Nada que el registro ya diga, cifras talladas, discutibles por
> numero y linea. **Las guardas de dato, intactas**: la aduana en seco candidato a candidato, la
> fidelidad `D.30` con su relectura contra el parrafo, `D.41` y `D.42`.

## G4.0. EL ESQUELETO DE LA VUELTA (`EXTRACTOR.md` 3)

| # | tarea del encargo | como cierra | donde |
|---:|---|---|---|
| 1 | `TAREA 1`: cerrar `cap_12` (`d101`): `L51` y `L63` nacen candidato, `L69` se declara NO-NODO, y la clase de `R3` en `REPORTE.md:57859` se corrige declarando | **CERRADA**: `2` candidatos, `0 CAERIA` los dos, `3` vecinos leidos, `L69` declarado, `d104` repasado | `G4.2` |
| 2 | `TAREA 2`: frontera, candidatos, `PASOS INVENTADOS` y muestra de fidelidad de `cap_13` y `cap_14` | **CERRADA**: `2` candidatos, `0 CAERIA` los dos, `2` filas de `PASOS INVENTADOS` en `0,00` por ciento, muestra `g4` pegada | `G4.3` |
| | el cierre: guardas, cifras recomputadas, discutibles marcados, `D.61` repasada, credito, commit y push | **CERRADO** | `G4.4` a `G4.6` |

**DOS TAREAS ENCARGADAS, DENTRO DEL TOPE DE CINCO** (`EXTRACTOR.md` 1.3).

## G4.1. LA APERTURA, MEDIDA ANTES DE LA PRIMERA OPERACION (`EXTRACTOR.md` 4)

Salida de `python .gerber_v4/apertura.py` (copia sin cambios de `.gerber_v3/apertura.py`), guardada en
`.gerber_v4/apertura.txt`:

<!-- TALLADO: parcial salida=.gerber_v4/apertura.txt -->

| pieza | al abrir | de donde sale |
|---|---:|---|
| nodos en el grafo | **346** | `dataset/nodos.jsonl` |
| veredictos escritos | **740** | `bitacora/VEREDICTOS.jsonl` |
| unidades de `gerber_emyth` | **22** | `PATRON: fuentes/gerber_emyth/cap_*.md` |
| palabras de cuerpo del libro | **62648** | `PATRON: fuentes/gerber_emyth/cap_*.md` |
| candidatos en bandeja de `gerber_emyth` | **11** | `PATRON: cuarentena/gerber_emyth/*.json` |
| clave `gerber_emyth` en la tabla canonica | **SI** | `fuentes/FUENTES_CANONICAS.json` |
| rama activa | `extraccion-gerber_emyth` | `git rev-parse --abbrev-ref HEAD` |
| commit de apertura | `3991806` | `git rev-parse --short HEAD` |

**CONTRA EL ACTA DE PARADA (seccion 2):** `346` nodos, `740` veredictos y `11` candidatos en bandeja me
salen al digito, igual que el estado que la decision del `22` sep publica. **Cero discrepancia que
declarar.**

## G4.2. TAREA 1: **CERRAR `cap_12` (`d101`)**. **CERRADA**

*`d101` (`ACTA G3` `3.1`): `L51` y `L63` pasan la vara de `EXTRACTOR.md` `9.1` y no se habian escrito
como candidatos; `L69` no la pasa. La condicion del reinicio de la racha manda ejecutarlo antes de abrir
`cap_13`, y `D.61` (nueva, banco) manda que el discutible quede hecho o cerrado en esta misma vuelta.*

### G4.2.a. LA FRONTERA FINA DE `R3` (`L22` a `L83`), PUBLICADA ANTES DE CORTAR (`EXTRACTOR.md` 10)

Salida de `python .gerber_v4/frontera.py fuentes/gerber_emyth/cap_12.md .gerber_v4/piezas_cap12.txt`
(instrumento identico a `.gerber_v3/frontera.py`, mismas `R1`, `R2`, `R4` a `R8` que la vuelta 3; solo
`R3` se abre en piezas finas), guardada en `.gerber_v4/frontera_cap12.txt`:

    $ diff .gerber_v3/frontera.py .gerber_v4/frontera.py
    (vacio, cero cambios en el instrumento)

<!-- TALLADO: salida=.gerber_v4/frontera_cap12.txt -->

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L19 | **57** | el numero del capitulo, el rotulo THE BUSINESS DEVELOPMENT PROCESS y el epigrafe de Thomas J. Peters y Robert H. Waterman Jr. (In Search of Excellence) | **RESIDUO: rotulo y epigrafe** |
| `R2` | L20 a L21 | **39** | la cabeza que nombra las tres actividades del Business Development Process: Innovation, Quantification y Orchestration | **POSTURA** |
| `R3a` | L22 a L50 | **347** | Innovation definida contra creatividad (cita a Theodore Levitt), y la tesis de que el franquiciador dirige su energia innovadora al COMO hace negocio, con el ejemplo del saludo del vendedor de tienda planteado como pregunta retorica | **POSTURA** |
| `R3b` | L51 a L58 | **128** | EL SALUDO NUEVO: las palabras exactas a decir en vez de Hi, may I help you, y sus dos ramas (si el cliente responde si, si responde no), mas la condicion de tener el programa especial ya creado | **INVENTARIO PROPIO: NACE 1 CANDIDATO** |
| `R3c` | L59 a L62 | **91** | el resultado atribuido al cambio de palabras: un aumento de ventas de entre 10 y 16 por ciento casi de inmediato, segun la experiencia de los clientes retail de los autores | **CIFRA DEL AUTOR** |
| `R3d` | L63 a L64 | **82** | EL TEST DE SEIS SEMANAS DEL TRAJE AZUL: dos etapas de tres semanas cada una y las ocho prendas nombradas una a una para cada etapa | **INVENTARIO PROPIO: NACE 1 CANDIDATO** |
| `R3e` | L65 a L68 | **75** | el resultado atribuido al cambio de traje (blue suits outsell brown suits) y la postura de que McDonalds, Federal Express, Disney y Mrs Fields tambien invierten en como se ven | **POSTURA y CASO** |
| `R3f` | L69 a L70 | **46** | TOCAR EL BRAZO: la siguiente vez que quieras que alguien haga algo por ti, tocalo suavemente en el brazo al pedirlo | **LINEA NOMBRADA sin inventario propio: NO ES NODO** |
| `R3g` | L71 a L72 | **48** | la aplicacion a tu negocio: tocar al cliente en el codo, brazo o espalda durante la venta, con el resultado atribuido de un aumento medible de ventas | **POSTURA** |
| `R3h` | L73 a L83 | **238** | el cierre de Innovation: la pregunta que continuamente plantea, la condicion de que tome el punto de vista del cliente, el mecanismo de identidad frente al cliente y la destreza del Best Way | **POSTURA** |
| `R4` | L84 a L94 | **101** | el subtitulo Quantification y por que cuantificar una innovacion importa | **POSTURA** |
| `R5` | L95 a L95 | **134** | el parrafo que enumera uno a uno los seis pasos para cuantificar el impacto de una innovacion | **INVENTARIO PROPIO: NACIO 1 CANDIDATO EN LA VUELTA 3** |
| `R6` | L96 a L147 | **326** | el resto de Quantification: el ejemplo del traje azul cuantificado, la lista abierta de preguntas sobre los numeros del negocio (termina en y asi sucesivamente) y el cierre | **POSTURA** |
| `R7` | L148 a L221 | **687** | la seccion Orchestration entera: la eliminacion de la discrecion, si no lo has orquestado no lo posees, y el cierre que nombra otra vez las tres actividades | **POSTURA** |
| `R8` | L222 a L293 | **1807** | el dialogo con Sarah sobre la Orquestacion, la metafora del aprendizaje del pastel de fruta y la maestria del artesano | **CASO y POSTURA** |
| **el cuerpo entero** | **L8 a L293** | **4206** | **suma de las piezas: 4206** | **residuo sin asignar: 0** |

    piezas: 15   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 4206   suma 4206   residuo 0

**`4206` palabras identicas a la suma de la vuelta 3 (`8` piezas viejas), cero solapes, cero lineas sin
cubrir: la fina no perdio ni gano una palabra del cuerpo**, solo abrio `R3` en nueve piezas donde antes
habia una.

### G4.2.b. `L51`: **EL SALUDO NUEVO, NACE CANDIDATO**

`cuarentena/gerber_emyth/cambiar_saludo_cliente_dos_ramas.json`, con sus **4** pasos transcritos de `R3b`
(`L51` a `L58`), cita pegada en `.gerber_v4/cita_cap12_L51.txt` (`D.35`):

    THE INNOVATION Instead of asking, "Hi, may I help you?" try "Hi, have you been in here before?"
    The customer will respond with either a "yes" or a "no." In either case, you are then free to
    pursue the conversation.

    If the answer is yes, you can say, "Great. We've created a special new program for people who
    have shopped here before. Let me take just a minute to tell you about it."

    If the answer is no, you can say, "Great, we've created a special new program for people who
    haven't shopped here before. Let me take just a minute to tell you about it."

    Of course, you'll have to have created a special new program to talk about in either case. But
    that's the easy part.

**RELECTURA DE FIDELIDAD `D.30` EN EL ACTO: `4` pasos, `4` TRANSCRIPCION, `0` PUENTE.** Las palabras se
dejan en ingles y entre comillas a proposito: son el objeto mismo del paso, y traducirlas fabricaria una
frase que el libro no probo (seria el mismo PUENTE que `15.4` prohibe). La cifra del resultado (`10` a
`16` por ciento) NO es paso: es `R3c`, cifra del autor, y va en `atribuciones` del candidato.

Su informe, corrido en el acto (`EXTRACTOR.md` 16). Salida de
`python forja.py informe cuarentena/gerber_emyth/cambiar_saludo_cliente_dos_ramas.json`, guardada en
`.gerber_v4/informe_cambiar_saludo.txt`:

<!-- TALLADO: parcial salida=.gerber_v4/informe_cambiar_saludo.txt -->

    poblacion del barrido       : 452   (346 del grafo mas 106 que esperan en bandejas)
    ENTRARIAN sin leer nada          : 0
    BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [BLOQUEARIA] cambiar_saludo_cliente_dos_ramas
        vecino cuantificar_impacto_innovacion_6_pasos  [levantada por: similitud_texto]
          similitud_texto 0.375 | familia_id 0.000 | paso_contra_nodo 0.325
          paso 4 del candidato contra paso 3 de cuantificar_impacto_innovacion_6_pasos

**`0 CAERIA`.** El unico vecino, leido (por debajo de `0,4`, no es la banda que obliga a leerlo antes que
ningun otro, pero es el unico y se lee igual, seccion 11): `cuantificar_impacto_innovacion_6_pasos` (paso
3, contar gente que entro tras el cambio) contra mi paso 4 (tener el programa especial ya creado). **El
parecido es de vocabulario de ventas compartido entre las dos piezas de este mismo bloque de `Innovation`
y `Quantification`, no conceptual**: uno cuenta personas, el otro exige tener listo un programa antes de
hablar. **VEREDICTO DE LECTURA: `SANO`.** No hay madre ni hija: son dos piezas hermanas del mismo tramo
del capitulo, no se escribe en `bitacora/VEREDICTOS.jsonl` porque esta vuelta no inserta (`D.39`).

### G4.2.c. `L63`: **EL TEST DEL TRAJE AZUL, NACE CANDIDATO**

`cuarentena/gerber_emyth/probar_traje_azul_seis_semanas.json`, con sus **2** pasos transcritos de `R3d`
(`L63` a `L64`), cita pegada en `.gerber_v4/cita_cap12_L63.txt` (`D.35`):

    THE INNOVATION Again, for salespeople, a six-week test. For the first three weeks, wear a brown
    suit to work, a starched tan shirt, a brown tie (for men), and well-polished brown shoes. Make
    certain that all the elements of your suit are clean and well-pressed. For the following three
    weeks wear a navy blue suit, a good, starched white shirt, a tie with red in it (a pin or a scarf
    with red in it for women), and highly polished black shoes.

**RELECTURA DE FIDELIDAD `D.30` EN EL ACTO: `2` pasos, `2` TRANSCRIPCION, `0` PUENTE.** Ocho prendas
nombradas una a una (cuatro por etapa: traje, camisa, corbata o accesorio, zapatos), dos etapas de tres
semanas. El resultado atribuido (*blue suits outsell brown suits*, sin cifra) es `R3e`, no paso.

Su informe, corrido en el acto. Salida de
`python forja.py informe cuarentena/gerber_emyth/probar_traje_azul_seis_semanas.json`, guardada en
`.gerber_v4/informe_probar_traje_azul.txt`:

<!-- TALLADO: parcial salida=.gerber_v4/informe_probar_traje_azul.txt -->

    poblacion del barrido       : 453   (346 del grafo mas 107 que esperan en bandejas)
    ENTRARIAN sin leer nada          : 0
    BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [BLOQUEARIA] probar_traje_azul_seis_semanas
        vecino cambiar_saludo_cliente_dos_ramas  [levantada por: similitud_texto]
          similitud_texto 0.489 | familia_id 0.000 | paso_contra_nodo 0.262
          paso 1 del candidato contra paso 3 de cambiar_saludo_cliente_dos_ramas
        vecino cuantificar_impacto_innovacion_6_pasos  [levantada por: similitud_texto]
          similitud_texto 0.430 | familia_id 0.000 | paso_contra_nodo 0.366
          paso 2 del candidato contra paso 2 de cuantificar_impacto_innovacion_6_pasos
        vecino dar_valor_constante_cuatro_publicos  [levantada por: similitud_texto]
          similitud_texto 0.362 | familia_id 0.000 | paso_contra_nodo 0.315
          paso 2 del candidato contra paso 2 de dar_valor_constante_cuatro_publicos

**`0 CAERIA`. Tres vecinos, y dos pasan de `0,4` (banda alta, seccion 11): se leen los tres antes que
ningun otro.**

| vecino | similitud | lectura | veredicto |
|---|---:|---|---|
| `cambiar_saludo_cliente_dos_ramas` | `0.489` | el candidato propio de esta misma vuelta, hermano bajo `Innovation` (`R3b`): uno es el guion del saludo, el otro el vestuario. Comparten campo lexico de ventas (*cliente*, *programa*, *semanas*) pero ninguno despliega al otro | **SANO, hermanos** |
| `cuantificar_impacto_innovacion_6_pasos` | `0.430` | nacido en la vuelta 3 de `R5` (`L95`), el metodo de conteo. Mi paso 2 (vestir de azul) contra su paso 2 (contar compradores): temas distintos del mismo capitulo, parecido lexico de negocio al detalle | **SANO** |
| `dar_valor_constante_cuatro_publicos` | `0.362` | nacido en la vuelta 1, parte 1 de la serie del Prototipo (`cap_11`). Mi paso 2 (vestuario) contra su paso 2 (la pregunta del valor constante): ningun objeto compartido | **SANO** |

Ninguno se escribe en `bitacora/VEREDICTOS.jsonl` porque esta vuelta no inserta (`D.39`); quedan
declarados aqui para que la vuelta que cierre el lote no los relea desde cero.

### G4.2.d. `L69`: **TOCAR EL BRAZO, DECLARADO NO-NODO**

`cap_12.md:69` a `:71`, cita pegada en `.gerber_v4/cita_cap12_L69.txt` (`D.35`):

    THE INNOVATION The next time you want somebody to do something for you, touch him softly on the
    arm as you ask him to do it. You will be amazed to find that more people will respond positively
    when you touch them than when you don't.

    Again, to apply this to your business, you or your salespeople should make a point of touching
    each customer on the elbow, arm, or back some time during the sales process. You will find, as
    our clients have found, that there will be a measurable increase in sales.

**NO PASA LA VARA DE `EXTRACTOR.md` `9.1`, Y ES EL EJEMPLO DIRECTO DE LA TABLA `SI ES/NO ES UN NODO`:
UNA ADVERTENCIA, ES LINEA Y NO PROCEDIMIENTO.** A diferencia de `R3b` (dos ramas escritas con sus
palabras exactas) y `R3d` (dos etapas con sus ocho prendas), `L69` es **una sola accion continua** (tocar
el brazo al pedir algo) sin inventario propio de medios, etapas ni objetos de trabajo que el libro nombre
uno a uno. La elaboracion de `L71` (*elbow, arm, or back*) nombra tres zonas del cuerpo, pero como
**alternativas intercambiables de un mismo gesto** (*on the elbow, arm, OR back*), no como pasos
sucesivos ni como un inventario de trabajo: seguiria siendo una linea, no una serie. **No tarda varios
pasos en ejecutarse: se ejecuta en un solo gesto.** Coincide con la lectura que `ACTA G3` `3.1` ya
adelanto (*el de `L69` no la pasa y lo digo tambien*) y con la que `d101` trae escrita; esta vuelta la
confirma con su propia lectura contra el texto, no la copia sin mirar (seccion 5: una nota previa nunca
es fuente sola de una cifra nueva).

### G4.2.e. `d104` REPASADO: **NINGUNA CABEZA NACE ESTA VUELTA**

`d104` (`cap_12` `L21`, gemelo de `d098`): *Innovation*, *Quantification* y *Orchestration* siguen sin
existir como nodo cabeza. Los dos candidatos de esta vuelta (`L51`, `L63`) son ejemplos concretos DENTRO
de `Innovation`, igual que `cuantificar_impacto_innovacion_6_pasos` (vuelta 3) es un metodo DENTRO de
`Quantification`: ninguno de los tres es la cabeza misma. **`d104` sigue abierto, sin tocar, tal como el
encargo pedia.**

### G4.2.f. LA CORRECCION DE `d095`/`d101` SOBRE LA CLASE DE `R3`, YA APLICADA

La correccion declarada de la fila `R3` de la vuelta 3 (`docs/loop/REPORTE.md:57859`) y de su prosa de
lectura (`:57874` a `:57876`) queda tachada y escrita al lado en su propio sitio, sin borrar la tabla
tallada de la vuelta 3 (`D.41`, no se toca una tabla protegida por instrumento historico: ver la nota
`CORRECCION DECLARADA` pegada justo debajo de esa tabla). **Los tres discutibles de `G3.7` quedan
resueltos**: el discutible `1` acertaba a medias (dos candidatos, no ninguno ni uno); el `2` y el `3`
siguen en pie tal como se escribieron (fidelidad de los pasos 2 a 4, y el puntero `d104`).

### G4.2.g. DISCUTIBLES DE ESTA TAREA, MARCADOS ANTES DE SABER SI ACIERTO

| # | discutible | por que lo marco |
|---:|---|---|
| 1 | clasifique `L69` (tocar el brazo) como NO-NODO por ser una sola accion con alternativas intercambiables (*elbow, arm, or back*) y no un inventario de pasos. Si el auditor lee esas tres zonas como un inventario propio de objetos de trabajo (tres sitios de contacto, cada uno ejecutable por separado), el candidato nace | es la misma clase de duda que ya trae `d101` escrita, y la resuelvo en el mismo sentido que el acta, pero con mi propia lectura y no por copiarla |
| 2 | en `cambiar_saludo_cliente_dos_ramas`, el paso 4 (*tener el programa especial ya creado*) viene de una frase que el libro presenta como un aparte casual (*Of course, ... But that's the easy part*), no como una instruccion en el mismo registro que las dos ramas. Lo transcribo como paso porque es una condicion que el libro SI escribe, pero si el auditor lo lee como comentario retorico y no como paso, el candidato se queda en 3 pasos y no en 4 | es la pieza mas floja de fidelidad de los dos candidatos de esta tarea |

**`D.61` REPASADA SOBRE ESTA MISMA TAREA:** los dos discutibles de arriba nacen y se cierran en esta misma
vuelta, con su lectura escrita; ninguno queda abierto para que otra vuelta lo herede.

## G4.3. TAREA 2: **`cap_13` Y `cap_14`**. **CERRADA**

*Solo despues de cerrar `G4.2`. `cap_13` (`364` palabras, el mas corto del libro) y `cap_14` van detras,
tercer capitulo tocado de la vuelta junto con `cap_12`, al techo del regimen ligero (`D.58`: tres
capitulos, techo `30` candidatos).*

### G4.3.a. LA FRONTERA DE `cap_13` (`Cap. 11`, *Your Business Development Program*), **4 piezas y UN CANDIDATO**

Salida de `python .gerber_v4/frontera.py fuentes/gerber_emyth/cap_13.md .gerber_v4/piezas_cap13.txt`,
guardada en `.gerber_v4/frontera_cap13.txt`:

<!-- TALLADO: salida=.gerber_v4/frontera_cap13.txt -->

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L20 | **75** | el numero del capitulo, el rotulo YOUR BUSINESS DEVELOPMENT PROGRAM y el epigrafe de Michael Murphy (Golf in the Kingdom) | **RESIDUO: rotulo y epigrafe** |
| `R2` | L21 a L38 | **204** | la escena imaginada del comprador potencial recorriendo el negocio, viendolo innovado, cuantificado y orquestado, y a la gente explicando sus responsabilidades | **POSTURA** |
| `R3` | L39 a L58 | **82** | el Business Development Program definido como el proceso paso a paso para convertir el negocio en un modelo organizado y como el vehiculo del Franchise Prototype, compuesto por siete pasos distintos que el libro nombra uno a uno: Your Primary Aim, Your Strategic Objective, Your Organizational Strategy, Your Management Strategy, Your People Strategy, Your Marketing Strategy y Your Systems Strategy | **INVENTARIO PROPIO: NACE 1 CANDIDATO (CABEZA DE SERIE NUMERADA)** |
| `R4` | L59 a L59 | **3** | el cierre Let's get started | **RESIDUO: bisagra** |
| **el cuerpo entero** | **L8 a L59** | **364** | **suma de las piezas: 364** | **residuo sin asignar: 0** |

    piezas: 4   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 364   suma 364   residuo 0

**Por que `R3` SI pasa la vara, y es un caso distinto al de `cap_12` `R2`.** `EXTRACTOR.md` `9.1`, tabla
SI ES UN NODO, tercera fila: *un procedimiento que el libro nombra en una tabla y desarrolla en otro
sitio*. `R3` no solo nombra los siete pasos: los pone en una LISTA NUMERADA (`1.` a `7.`, cada uno en su
propia linea) y cada uno es el TITULO EXACTO de un capitulo futuro completo (`cap_14` a `cap_19`, mas el
`cap. 17` reservado), no una subseccion del mismo capitulo. Es distinto de `cap_12` `R2` (*Innovation,
Quantification, and Orchestration*), que nombra tres actividades EN UNA FRASE CORRIDA y las desarrolla
dentro del MISMO capitulo unas lineas mas abajo: ese es el caso que `EXTRACTOR.md` 9 llama *nombrar sin
desplegar en la misma linea*, marcado POSTURA. `R2` (la escena del comprador imaginado) y `R4` (el cierre)
no traen inventario propio, son postura y bisagra.

`cuarentena/gerber_emyth/recorrer_siete_pasos_programa_desarrollo_negocio.json`, con sus **10** pasos
transcritos de `R3` (`L39` a `L58`), cita pegada en `.gerber_v4/cita_cap13_L39.txt` (`D.35`):

    Your Business Development Program is the step-by-step process through which you convert your
    existing business [...] into a perfectly organized model for thousands more just like it.
    Your Business Development Program is the vehicle through which you can create your Franchise
    Prototype. The Program is composed of seven distinct steps: 1. Your Primary Aim  2. Your
    Strategic Objective  3. Your Organizational Strategy  4. Your Management Strategy  5. Your
    People Strategy  6. Your Marketing Strategy  7. Your Systems Strategy

**RELECTURA DE FIDELIDAD `D.30` EN EL ACTO: `10` pasos, `10` TRANSCRIPCION, `0` PUENTE.** Cada uno de los
siete nombres se deja tal cual el libro los escribe, sin glosa mia: el libro no pone ni una linea de
descripcion por paso en este capitulo (a diferencia de las seis reglas del Prototipo, que si traian una
frase cada una), y escribir una no seria transcribir, seria completar un inventario delgado (`15.4`).

**`D.37` Y NO `D.29`: hoy `0` de `7` partes existen como nodo.** `cap_14` a `cap_19` estan SIN TOCAR
(`ACTA G3` seccion 2), y el `cap. 17` (*Your Marketing Strategy*) esta apartado en
`fuentes/gerber_emyth_cap17_reservado/`. Las aristas cabeza a parte se declaran cuando cada capitulo se
mine y produzca su propia cabeza, citando `L43` a `L57`, no antes. Mismo patron que
~~`fingir_prototipo_cinco_mil_replicas` (entro con `4` de `6` partes)~~ **CORRECCION DECLARADA EN LA VUELTA
5 (`ACTA G4` `1`, fila `2`): es falso, `fingir_prototipo_cinco_mil_replicas` NO ha entrado. Sigue en
`cuarentena/gerber_emyth/` (`grep -c '"clave": "gerber_emyth"' dataset/nodos.jsonl` da `0`) y su propio
`nodos_siguientes` esta vacio. Lo cierto es que NACIO con `4` de `6` reglas escritas** y `recorrer_trece_elementos_proceso_evaluacion_formal`
(entro con `0` de `13`).

Su informe, corrido en el acto. Salida de
`python forja.py informe cuarentena/gerber_emyth/recorrer_siete_pasos_programa_desarrollo_negocio.json`,
guardada en `.gerber_v4/informe_recorrer_siete_pasos.txt`:

<!-- TALLADO: parcial salida=.gerber_v4/informe_recorrer_siete_pasos.txt -->

    poblacion del barrido       : 454   (346 del grafo mas 108 que esperan en bandejas)
    ENTRARIAN sin leer nada          : 1
    BLOQUEARIAN esperando veredicto  : 0
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [ENTRARIA] recorrer_siete_pasos_programa_desarrollo_negocio

**`0 CAERIA`, `0` vecinos levantados: ninguna lectura de vecino que hacer** (seccion 11 no aplica sin
vecindad).

### G4.3.b. LA FRONTERA DE `cap_14` (`Cap. 12`, *Your Primary Aim*), **7 piezas y UN CANDIDATO**

Salida de `python .gerber_v4/frontera.py fuentes/gerber_emyth/cap_14.md .gerber_v4/piezas_cap14.txt`,
guardada en `.gerber_v4/frontera_cap14.txt`:

<!-- TALLADO: salida=.gerber_v4/frontera_cap14.txt -->

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L20 | **35** | el numero del capitulo, el rotulo YOUR PRIMARY AIM y el epigrafe de Robert Assagioli (The Act of Will) | **RESIDUO: rotulo y epigrafe** |
| `R2` | L21 a L30 | **115** | el negocio no es lo primero, eres tu; y antes de decidir que papel juega el negocio en tu vida debes preguntarte que valoras mas, que vida quieres, como quieres que se vea y se sienta, quien quieres ser: eso es tu Primary Aim | **POSTURA** |
| `R3` | L31 a L98 | **510** | la visualizacion de tu propio funeral y la cinta con la historia de tu vida contada a los asistentes, como metafora de que es el Primary Aim, y el llamado a vivir la vida intencionalmente y tomarla en serio | **POSTURA** |
| `R4` | L99 a L116 | **228** | la gente notable sabe como llego a donde esta y que necesita para llegar a donde va, trabaja sobre su vida y no solo en ella, y la cita de Don Juan sobre el guerrero que ve todo como un reto | **POSTURA y CASO** |
| `R5` | L117 a L136 | **180** | antes de empezar tu negocio, o antes de volver a el manana, preguntate lo siguiente: las ocho preguntas que el libro enumera en vinetas sobre como quieres que se vea tu vida, tu dia a dia, que sabes de verdad, como quieres estar con otros, que quieres aprender y cuanto dinero necesitaras | **INVENTARIO PROPIO: NACE 1 CANDIDATO** |
| `R6` | L137 a L146 | **73** | las respuestas se vuelven los estandares con que mides el progreso de tu vida, y tu Primary Aim es la vision que trae tu negocio a tu vida y tu vida a tu negocio, con proposito, energia y grano para el dia a dia | **POSTURA** |
| `R7` | L147 a L217 | **2554** | el asombro de Sarah al descubrirse ausente de su propio negocio, y la larga historia autobiografica del propio autor, de vendedor de enciclopedias a consultor en Silicon Valley, contada como ejemplo de encontrar el propio proposito | **CASO** |
| **el cuerpo entero** | **L8 a L217** | **3695** | **suma de las piezas: 3695** | **residuo sin asignar: 0** |

    piezas: 7   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 3695   suma 3695   residuo 0

**Por que ninguna pasa la vara salvo `R5`.** `R2`, `R3`, `R4` y `R6` son postura y metafora (la
visualizacion del funeral, la cinta de tu vida) sobre QUE ES el Primary Aim, sin inventario propio de
medios que el lector ejecute con esos mismos terminos. `R7` es el dialogo con Sarah y la historia
autobiografica del autor: caso. `R5` SI trae inventario propio: `ask yourself the following questions`,
imperativo explicito, seguido de ocho preguntas en vineta, cada una su propio objeto de trabajo.

**LA REPETICION INTERNA QUE NO SE FUNDE (`P.19`), declarada:** `L27` (`R2`) tambien trae preguntas (*What
do I value most? What kind of life do I want?*), pero embebidas en un parrafo corrido, sin vineta ni el
imperativo *the following questions*: es preparacion retorica de por que el Primary Aim importa, no el
mismo objeto que `L117` a `L133`. Fundir los dos preguntarios fabricaria un tercero que ningun parrafo
escribe, asi que `L27` se queda en `R2`, postura, sin transcribirse.

`cuarentena/gerber_emyth/responder_8_preguntas_construir_primary_aim.json`, con sus **9** pasos
transcritos de `R5` (`L117` a `L136`), cita pegada en `.gerber_v4/cita_cap14_L117.txt` (`D.35`):

    So before you start your business, or before you return to it tomorrow, ask yourself the
    following questions: • What do I wish my life to look like? • How do I wish my life to be on
    a day-to-day basis? [...] • How much money will I need to do the things I wish to do? By when
    will I need it? These are just a few of the questions you might ask yourself in the creation
    of your Primary Aim.

**RELECTURA DE FIDELIDAD `D.30` EN EL ACTO: `9` pasos, `9` TRANSCRIPCION, `0` PUENTE.** El cierre de la
pieza (*these are just a few of the questions you might ask yourself*) se queda fuera de los pasos, no se
transcribe: es un comentario sobre la lista, no un paso mas.

Su informe, corrido en el acto. Salida de
`python forja.py informe cuarentena/gerber_emyth/responder_8_preguntas_construir_primary_aim.json`,
guardada en `.gerber_v4/informe_responder_8_preguntas.txt`:

<!-- TALLADO: parcial salida=.gerber_v4/informe_responder_8_preguntas.txt -->

    poblacion del barrido       : 455   (346 del grafo mas 109 que esperan en bandejas)
    ENTRARIAN sin leer nada          : 0
    BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [BLOQUEARIA] responder_8_preguntas_construir_primary_aim
        vecino cuantificar_impacto_innovacion_6_pasos  [levantada por: similitud_texto]
          similitud_texto 0.375 | familia_id 0.000 | paso_contra_nodo 0.426
          paso 1 del candidato contra paso 1 de cuantificar_impacto_innovacion_6_pasos

**`0 CAERIA`. El unico vecino, leido** (por debajo de `0,4`, seccion 11): `cuantificar_impacto_innovacion_6_pasos`
(vuelta 3, `cap_12`) paso 1 (*determinar cuantas personas entraron por la puerta*) contra mi paso 1
(*preguntate lo siguiente, antes de empezar tu negocio*). **Parecido de arranque de frase entre dos
listas de pasos de capitulos distintos, no conceptual**: uno cuenta trafico de clientes, el otro pregunta
por el sentido de la propia vida. **VEREDICTO DE LECTURA: `SANO`.** No se escribe en
`bitacora/VEREDICTOS.jsonl` porque esta vuelta no inserta (`D.39`).

### G4.3.c. DISCUTIBLE DE ESTA TAREA, MARCADO ANTES DE SABER SI ACIERTO

| # | discutible | por que lo marco |
|---:|---|---|
| 3 | en `responder_8_preguntas_construir_primary_aim`, la frase de cierre *these are just a few of the questions you might ask yourself* suaviza el listado (no dice *hazte estas ocho*, dice *son solo algunas de las que podrias hacerte*). Lo lei como que la ACCION de preguntarse estas ocho sigue mandada (*ask yourself the following questions* es imperativo) y que la suavizacion es sobre si HAY MAS preguntas posibles, no sobre si estas ocho son opcionales. Si el auditor lee la suavizacion como el adjetivo de adecuacion que tumba el inventario entero (`9.1`, restriccion 2), el candidato cae | es la duda de criterio mas fina de `cap_14`, y la unica de las dos tareas que toca la restriccion 2 de la vara y no solo la fidelidad |

La numeracion de discutibles sigue la de `G4.2.g` (`1` y `2`); este es el `3`, y con el cierran los de la
vuelta.

### G4.3.d. `PASOS INVENTADOS POR CAPITULO`, UNA FILA POR CAPITULO (`AUDITOR_FORJA.md` 8)

<!-- TALLADO: parcial salida=.gerber_v4/frontera_cap12.txt,.gerber_v4/frontera_cap13.txt,.gerber_v4/frontera_cap14.txt,.gerber_v4/informe_cambiar_saludo.txt,.gerber_v4/informe_probar_traje_azul.txt,.gerber_v4/informe_recorrer_siete_pasos.txt,.gerber_v4/informe_responder_8_preguntas.txt -->

| capitulo | candidatos nuevos (esta vuelta) | pasos escritos | PUENTE | pasos inventados |
|---|---:|---:|---:|---|
| `cap_12` | `2` (`cambiar_saludo_cliente_dos_ramas`, `probar_traje_azul_seis_semanas`) | `6` | `0` | **0,00 por ciento** |
| `cap_13` | `1` (`recorrer_siete_pasos_programa_desarrollo_negocio`) | `10` | `0` | **0,00 por ciento** |
| `cap_14` | `1` (`responder_8_preguntas_construir_primary_aim`) | `9` | `0` | **0,00 por ciento** |
| **la vuelta 4 entera** | **`4`** | **`25`** | `0` | **0,00 por ciento** |

**Ninguna fila `SIN SUPERFICIE`: los tres capitulos que esta vuelta toca dieron candidato.** `cap_12` suma
solo lo que ESTA vuelta anadio (los dos de `d101`); el candidato de la vuelta 3 (`cuantificar_impacto_innovacion_6_pasos`,
`6` pasos, `0` puente) ya quedo tallado en su propia fila de `G3.5` y `D.47` (modo austero) no lo repite
aqui.

### G4.3.e. LA MUESTRA DE FIDELIDAD, SEMILLA `g4`

*El encargo (seccion 2, punto 4) pide la muestra sobre `cap_13,cap_14`, literal, sin `cap_12`: su
fidelidad ya quedo hecha entera y no por muestra en `G4.2` (`4`/`4` y `2`/`2` pasos releidos al escribir
cada candidato, `100` por ciento de cobertura, mas estricto que cualquier muestra).*

Salida de
`python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_13,cap_14 --semilla g4`,
guardada en `.gerber_v4/muestra_fidelidad.txt`:

<!-- TALLADO: salida=.gerber_v4/muestra_fidelidad.txt -->

    MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO (D.58)
      libro    : gerber_emyth
      semilla  : g4
      capitulos: cap_13, cap_14

      RELEIDO ENTERO : cap_13
      POR MUESTRA    : cap_14, 15 pasos cada uno

      EL DISPARADOR: si la muestra de un capitulo pasa del 10 por ciento de
      pasos inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.

      --- cap_14: 9 paso(s) en la muestra
        responder_8_preguntas_construir_primary_aim    P1   Antes de empezar tu negocio, o antes de volver a el manana,
        responder_8_preguntas_construir_primary_aim    P2   Que quiero que se vea mi vida.
        responder_8_preguntas_construir_primary_aim    P3   Como quiero que sea mi vida dia a dia.
        responder_8_preguntas_construir_primary_aim    P4   Que me gustaria poder decir que se de verdad en mi vida, sob
        responder_8_preguntas_construir_primary_aim    P5   Como me gustaria estar con otras personas en mi vida: mi fam
        responder_8_preguntas_construir_primary_aim    P6   Como me gustaria que la gente pensara de mi.
        responder_8_preguntas_construir_primary_aim    P7   Que me gustaria estar haciendo dentro de dos anios, dentro d
        responder_8_preguntas_construir_primary_aim    P8   Que me gustaria aprender especificamente durante mi vida: es
        responder_8_preguntas_construir_primary_aim    P9   Cuanto dinero voy a necesitar para hacer las cosas que quier

      --- cap_13: ENTERO, 10 paso(s), no hay muestra que elegir

**La semilla eligio `cap_13` para relectura ENTERA (sus `10` pasos, los mismos que `G4.3.a` ya releyo
contra `R3` con `0` puente) y `cap_14` por muestra, que aqui es el `100` por ciento de sus `9` pasos
porque el capitulo no llega al techo de `15`.** Releidos los `19` pasos de los dos candidatos contra sus
citas (`.gerber_v4/cita_cap13_L39.txt`, `.gerber_v4/cita_cap14_L117.txt`): **`0` PUENTE en los dos.**

**DISCREPANCIA DECLARADA (seccion 5), y se corrige en el acto de escribir, no en silencio:** la primera
corrida de este instrumento en esta vuelta se lanzo con `--capitulos cap_12,cap_13,cap_14` (por incluir
`cap_12`, que tambien se toco), antes de releer el encargo al pie de la letra (seccion 2, punto 4, que
pide `cap_13,cap_14` y no los tres). Esa salida vieja queda en `.gerber_v4/muestra_fidelidad.txt` hasta
que la corrida buena (la de arriba, `cap_13,cap_14`) la sobreescribio; la cito aqui para que no desaparezca
sin dejar rastro: la semilla `g4` elige `cap_13` ENTERO en los dos casos (es determinista sobre el mismo
nombre de capitulo), asi que la correccion no cambia ningun veredicto, solo el alcance declarado del
comando.

## G4.4. EL CIERRE, GUARDAS Y COMPROBACION DE SECCIONES (`EXTRACTOR.md` 4 y 6)

### G4.4.a. LAS TRES GUARDAS

Salida guardada en `.gerber_v4/gate.txt`, `.gerber_v4/guiones.txt` y `.gerber_v4/tests.txt`:

<!-- TALLADO: parcial salida=.gerber_v4/gate.txt,.gerber_v4/guiones.txt,.gerber_v4/tests.txt -->

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python tests/test_aceptacion.py
    total: 350 pruebas, 0 fallos, 0 errores

**DISCREPANCIA DECLARADA, CORREGIDA EN EL ACTO (seccion 5 y 6).** La primera corrida de `guiones` dio
**ROJO**, `4` hallazgos: mis dos ficheros de cita pegada (`.gerber_v4/cita_cap13_L39.txt`,
`.gerber_v4/cita_cap14_L117.txt`) llevaban el guion largo (`U+2014`) del propio libro en ingles (*your
existing business - or the one*). `fuentes/gerber_emyth/` esta fuera de git (`EXTRACTOR.md` 17) y por eso
el barrido nunca lo toca ahi; mis citas pegadas SI estan en git, y la regla no hace excepcion por ser
transcripcion verbatim de un tercero (manual seccion 2, cero en TODO el repo). Lo corrijo cambiando el
guion largo por el corto normal en las dos citas (formato, no contenido: ninguna palabra cambia) y
recorro las tres guardas limpias. La primera corrida de `test_aceptacion.py`, con el guion largo todavia
puesto, tambien daba `1` fallo (`350` pruebas, `1` fallos); tras la correccion sale `0` fallos, `0`
errores, **misma cuenta de pruebas**.

### G4.4.b. LA COMPROBACION DE SECCIONES DE `2.2`, SOBRE ESTE MISMO BLOQUE

Salida de `python .gerber_v4/secciones.py` (copia de `.gerber_v3/secciones.py`, `G3` por `G4` y el
encabezado de vuelta que busca, cero cambios de logica), guardada en `.gerber_v4/secciones.txt`. Se corre
DOS VECES: aqui, antes de escribir `G4.5` y `G4.6` (para medir el hueco), y otra vez al final del
documento, ya con las dos escritas.

<!-- TALLADO: salida=.gerber_v4/secciones.txt -->

    el bloque del frente empieza en la linea 58103 de docs/loop/REPORTE.md
    secciones que el bloque TIENE      : 19   G4.0 G4.1 G4.2 G4.2.a G4.2.b G4.2.c G4.2.d G4.2.e G4.2.f G4.2.g G4.3 G4.3.a G4.3.b G4.3.c G4.3.d G4.3.e G4.4 G4.4.a G4.4.b
    secciones que el bloque CITA       : 8   G4.2 G4.2.g G4.3 G4.3.a G4.4 G4.4.a G4.4.b G4.6
    CITADAS Y QUE NO EXISTEN           : 1
        G4.6 citada en la(s) linea(s) [58122]

**`1` CITADA Y QUE NO EXISTE TODAVIA: `G4.6`, citada en el esqueleto (`G4.0`) antes de escribirse** (el
cierre completo, `G4.5` y `G4.6`, va justo debajo de esta misma seccion). Se recorre de nuevo al final,
despues de escribir `G4.5` y `G4.6`, y su salida limpia (`0` citadas y que no existen) es la que cuenta
como cierre real de esta guarda. **El numero de linea de apertura (`58103`) es el que tenia el documento
en el instante en que corri el instrumento**, antes de pegar esta misma salida: pegarla desplaza las
lineas que le siguen, y por eso se cita como lo que midio, no como coordenada viva del documento final
(mismo tratamiento que `G3.8.b` le dio a su propia linea `57716`).

## G4.5. EL ESTADO AL CIERRE, RECOMPUTADO Y NO COPIADO DE LA APERTURA (`EXTRACTOR.md` 4)

### G4.5.a. LA TABLA DE CIERRE DE TAREAS (`D.52`)

| # | tarea | como cerro |
|---:|---|---|
| `1` | `TAREA 1`: cerrar `cap_12` (`d101`) | **CERRADA en `G4.2`**: `2` candidatos nuevos (`cambiar_saludo_cliente_dos_ramas`, `probar_traje_azul_seis_semanas`), `0 CAERIA` los dos, `L69` declarado NO-NODO, `d104` repasado sin tocar, la clase de `R3` corregida declarando |
| `2` | `TAREA 2`: `cap_13` y `cap_14` | **CERRADA en `G4.3`**: `2` candidatos nuevos, `0 CAERIA` los dos, `2` filas `PASOS INVENTADOS` en `0,00` por ciento, muestra `g4` releyo `cap_13` entero y `cap_14` al `100` por ciento (`9`/`9`) |

    $ python scripts/tabla_de_cierre.py --escribir

<!-- TALLADO: script=scripts/tabla_de_cierre.py salida=docs/loop/TABLA_DE_CIERRE.txt -->

### G4.5.b. LAS CIFRAS, RECOMPUTADAS AL CERRAR Y NO COPIADAS DE `G4.1`

Salida de `python .gerber_v4/apertura.py` corrida OTRA VEZ, ahora al cierre, guardada en
`.gerber_v4/cierre.txt`:

<!-- TALLADO: parcial salida=.gerber_v4/cierre.txt -->

| pieza | al abrir (`G4.1`) | al cerrar | diferencia |
|---|---:|---:|---|
| nodos en el grafo | `346` | **346** | `0` |
| veredictos escritos | `740` | **740** | `0` |
| candidatos en bandeja de `gerber_emyth` | `11` | **15** | `+4` (los cuatro candidatos de `G4.2` y `G4.3`) |
| pasos en esa bandeja | `95` | **120** | `+25` (`4+2` de `cap_12`, `10` de `cap_13`, `9` de `cap_14`) |
| ficheros de dato movidos por esta vuelta | | **0** | `git diff --name-only 3991806..HEAD -- dataset/ bitacora/ censos/ config/pares_mutuos.jsonl`: vacio |

**`346` y `740` identicos a la apertura de esta misma vuelta. La bandeja sube de `11` a `15` candidatos y
de `95` a `120` pasos, y es el unico movimiento de esta vuelta**: `G4.2` y `G4.3` solo escriben ficheros en
`cuarentena/`, que es bandeja y no grafo; la correccion de `G4.2.f` solo toca texto de reporte (que no es
sede de dato, `EXTRACTOR.md` 14). Cero averia.

### G4.5.c. LAS CONDICIONES DE PARADA, REPASADAS UNA A UNA (`EXTRACTOR.md` 7)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| una pregunta de doctrina | ninguna: los tres discutibles (`G4.2.g` `1` y `2`, `G4.3.c` `3`) son de lectura, no de regla, y no piden doctrina nueva | **NO ES PARADA** |
| una caida de dato | ninguna: `0` ficheros de `dataset/`, `bitacora/`, `censos/` ni `config/pares_mutuos.jsonl` movidos (`G4.5.b`) | **NO ES PARADA** |
| algo contradice una regla vigente o una cifra publicada con su corte | nada: `d101` se cumplio con sus tres piezas (`L51`, `L63`, `L69`), la correccion de `R3` quedo declarada sin borrar, y el saldo del acta (`346` nodos, `740` veredictos, `11` candidatos al abrir) coincide con lo medido en `G4.1` | **NO ES PARADA** |
| una guarda en rojo | ninguna al cierre: las tres de `G4.4.a` en VERDE (la caida transitoria de `guiones` y de `test_aceptacion.py` se corrigio en el acto, `G4.4.a`) | **NO ES PARADA** |
| una operacion cuyo texto no alcance para ejecutarse sin decidir | ninguna: las dos tareas del encargo estaban escritas enteras, con `d101` citando sus tres piezas por linea | **NO ES PARADA** |

**NINGUNA DE LAS CINCO SE CUMPLE. ESTE TURNO CIERRA SIN PARADA**, y `docs/loop/PARA_ALEXIS.md` sigue sin
tocar y no es mio (`EXTRACTOR.md` 14).

## G4.6. `D.61` REPASADA, CREDITO Y LO QUE PROPONGO

### G4.6.a. `D.61` CONTRA ESTE MISMO REPORTE, ANTES DE CERRAR

*`D.61`: un discutible publicado se ejecuta o se cierra en la misma vuelta que lo escribe.*

| discutible publicado en esta vuelta | hecho o cerrado |
|---|---|
| `G4.2.g` `1`: si `L69` fuera inventario, nace candidato | **CERRADO CON MOTIVO**: `L69` se declaro NO-NODO en `G4.2.d`, con su lectura escrita contra el texto. No queda ningun *ahi nace otro candidato* pendiente |
| `G4.2.g` `2`: fidelidad del paso 4 de `cambiar_saludo_cliente_dos_ramas` | **CERRADO CON SU LECTURA**: el paso se escribio y se transcribio tal cual (`G4.2.b`); el discutible es sobre COMO SE LEE ese paso ya escrito, no sobre un candidato pendiente de nacer |
| `G4.3.c` `3`: fidelidad de `responder_8_preguntas_construir_primary_aim` | **CERRADO CON SU LECTURA**: el candidato ya nacio en `G4.3.b`; el discutible es sobre la fuerza del inventario ya escrito, no sobre un nacimiento pendiente |

**NINGUN DISCUTIBLE DE ESTA VUELTA QUEDA ABIERTO EN LA FORMA QUE `D.61` CASTIGA** (un *ahi nace otro
candidato* sin ejecutar). Los tres son dudas de LECTURA sobre candidatos YA ESCRITOS, no promesas de
trabajo futuro sin hacer.

### G4.6.b. CREDITO: LA TANDA SE MIDE, NO SE ADJUDICA A SI MISMA

*El encargo (seccion 6) dice "escribe tu tanda: `python forja.py credito --anotar`". `--anotar` pide
`--especie`, `--vuelta`, `--tanda "ACTA N"`, `--racha` y `--cita`: el campo `--tanda` nombra la ACTA que
audito esta vuelta, y esa acta todavia no existe. ~~`CREDITO_gerber_emyth.jsonl` no tiene ni una fila cuyo
`tanda` no sea una `ACTA` del auditor.~~ **CORRECCION DECLARADA EN LA VUELTA 5 (`ACTA G4` `1`, fila `1`):
es falso. La PRIMERA fila del fichero SI tiene `tanda` `"G2"`, no una `ACTA`, y es justo la fila que la
`ACTA G2` `3.2` cargo como `CIFRA PUBLICADA`. Salida de `head -1 docs/loop/CREDITO_gerber_emyth.jsonl`:**

    {"cita": "REPORTE.md seccion G2", "especie": "REPORTE", "linea": "gerber_emyth", "racha": "1 de 3", "tanda": "G2", "tipo": "tanda", "vuelta": 2}

**La lectura de fondo del parrafo no cambia**: "escribir mi tanda" lo leo como MEDIR el estado con el
instrumento de solo lectura, no como adjudicarme un numero que le corresponde escribir a quien audita
(`EXTRACTOR.md` 14: *el extractor propone en su reporte, no se adjudica a si mismo*), y es la misma
lectura que la vuelta 3 ya hizo sobre su propio encargo.*

Salida de `python forja.py credito`, guardada en `.gerber_v4/credito.txt`:

<!-- TALLADO: salida=.gerber_v4/credito.txt -->

    CREDITO DE LA LINEA 'gerber_emyth' (D.48)
      registro: docs/loop/CREDITO_gerber_emyth.jsonl
      tandas: 4, en 12 suceso(s) de especie

      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA G3
      CIFRA PUBLICADA    0 de 2     ACTA G3
      CLASE              0 de 2     ACTA G3
      DATO MOVIDO        0 de 2     ACTA G3
      REPORTE            0 de 3     docs/loop/paradas/2026-09-22-gerber-g3-DECISION.md, punto 1

      CREDITO ENTERO: ninguna especie en su tope.

**`CREDITO ENTERO: ninguna especie en su tope`, confirmado por el instrumento y no recordado del acta.**
El numero de `REPORTE` para esta tanda (vuelta `4`) lo escribe el auditor con `--anotar`, con el nombre de
su acta en el campo `tanda`, tal como `docs/loop/CREDITO_gerber_emyth.jsonl` ya muestra para `ACTA G2` y
`ACTA G3`.

### G4.6.c. `d101` PAGADA

`d101` (`ACTA G3` `3.1`) pedia tres cosas: `L51` nace candidato, `L63` nace candidato, `L69` se declara
NO-NODO. Las tres estan hechas en `G4.2`. Se anota pagada:

    $ python scripts/deuda.py --pagar d101 --vuelta 4 --como "PAGADA en la vuelta 4 del frente: L51 y L63
      nacieron candidato (cambiar_saludo_cliente_dos_ramas, probar_traje_azul_seis_semanas, 0 CAERIA los
      dos), L69 se declaro NO-NODO con su motivo (G4.2.d), y la clase de R3 de la vuelta 3 quedo corregida
      declarando sin borrar (G4.2.f). Verificado en docs/loop/REPORTE.md seccion G4.2 de esta misma vuelta."
    PAGADA d101 en la vuelta 4

<!-- TALLADO: salida=.gerber_v4/deuda_pagar_d101.txt -->

`python scripts/deuda.py`, corrido despues, confirma el movimiento:

    pendientes: 35    pagadas: 33

contra `36` pendientes y `32` pagadas que `G4.1` no midio por separado (el encargo no lo pedia en la
apertura) pero que `ACTA G3` seccion `2` si publica (`36` pendientes, `32` pagadas): **`-1` pendiente,
`+1` pagada, y es exactamente `d101`.**

### G4.6.d. PROPUESTAS AL AUDITOR, TODAS EN MI SEDE Y NINGUNA ADJUDICADA POR MI

1. **`d101` esta cumplida entera**, con sus tres piezas y la correccion de `R3` declarada sin borrar
   (`G4.2.f`, `G4.6.c`).
2. **El puntero `d104` sigue abierto, sin tocar**, tal como el encargo pedia (`G4.2.e`): ninguna cabeza de
   `Innovation`/`Quantification`/`Orchestration` nacio esta vuelta.
3. **Nace un puntero nuevo (candidato a numero propio del banco): la serie de `cap_13`.**
   `recorrer_siete_pasos_programa_desarrollo_negocio` es la cabeza de una `SERIE NUMERADA` con `0` de `7`
   partes en el grafo. Cuando una vuelta futura mine `cap_14` (ya tocado hoy, `responder_8_preguntas_construir_primary_aim`
   no es la cabeza de *Your Primary Aim*, es un metodo dentro de ese capitulo) o cualquiera de `cap_15` a
   `cap_19`, y ese capitulo produzca su propia cabeza, la arista a `recorrer_siete_pasos_programa_desarrollo_negocio`
   se declara entonces citando `cap_13` `L43` a `L57`, no antes. El `cap. 17` (*Your Marketing Strategy*)
   sigue apartado: si esa reserva no se revierte, la serie puede quedarse en `6` de `7` para siempre, y eso
   no es una caida: es lo que el propio libro deja abierto.
4. **`cap_12` queda CERRADO** (`8` piezas viejas mas `2` candidatos nuevos, cero pendiente propio). El
   frente tiene ahora `cap_04` a `cap_14` minados sin hueco (once capitulos), mas `cap_09` y `cap_10` de la
   vuelta 3. El siguiente sin tocar es `cap_15` (`Your Strategic Objective`, `4685` palabras).

### G4.6.e. LA COMPROBACION DE SECCIONES, SEGUNDA Y ULTIMA CORRIDA (`G4.4.b` lo anuncio)

Salida de `python .gerber_v4/secciones.py`, corrida OTRA VEZ ya con `G4.5` y `G4.6` escritas, guardada en
`.gerber_v4/secciones_final.txt` (fichero distinto al de `G4.4.b`, para no pisar la salida intermedia que
esa seccion tallo):

<!-- TALLADO: salida=.gerber_v4/secciones_final.txt -->

    el bloque del frente empieza en la linea 58121 de docs/loop/REPORTE.md
    secciones que el bloque TIENE      : 28   G4.0 G4.1 G4.2 G4.2.a G4.2.b G4.2.c G4.2.d G4.2.e G4.2.f G4.2.g G4.3 G4.3.a G4.3.b G4.3.c G4.3.d G4.3.e G4.4 G4.4.a G4.4.b G4.5 G4.5.a G4.5.b G4.5.c G4.6 G4.6.a G4.6.b G4.6.c G4.6.d
    secciones que el bloque CITA       : 18   G4.0 G4.1 G4.2 G4.2.b G4.2.d G4.2.e G4.2.f G4.2.g G4.3 G4.3.a G4.3.b G4.3.c G4.4 G4.4.a G4.5 G4.5.b G4.6 G4.6.c
    CITADAS Y QUE NO EXISTEN           : 0

**`0` CITADAS Y QUE NO EXISTEN: la guarda cierra limpia.** `G4.6.e`, la seccion que este parrafo escribe,
no aparece en el recuento porque el instrumento leyo el documento ANTES de que esta frase se pegara (el
mismo desfase, ya declarado, que `G4.4.b` explica para su propia corrida).

---

# FRENTE `gerber_emyth`, VUELTA 5: **`cap_15`, `cap_16` Y `cap_17`, Y LAS DOS CORRECCIONES DE LA `ACTA G4`** (`D.45`, frente en paralelo: **NO INSERTA**)

> ## **ESTE BLOQUE SE ESCRIBE EN LA RAMA `extraccion-gerber_emyth`, CON `MODO_INSERCION=cuarentena`. CERO INSERCIONES.**
>
> **`ACTA G4` PAGA `d101` ENTERA Y SOSTIENE LOS TRES DISCUTIBLES DE LA VUELTA 4.** Lo unico que cae son
> dos frases de prosa de acompaniamiento (seccion `1` de este bloque), que `5.2` de `EXTRACTOR.md` dice
> que NO acumulan en ninguna racha.
>
> **MODO AUSTERO (`D.47`) VIGENTE.** Nada que el registro ya diga, cifras talladas, discutibles por
> numero y linea. **Las guardas de dato, intactas**: la aduana en seco candidato a candidato, la
> fidelidad `D.30` con su relectura contra el parrafo, `D.41` y `D.42`.

## G5.0. EL ESQUELETO DE LA VUELTA (`EXTRACTOR.md` 3)

| # | tarea del encargo | como cierra | donde |
|---:|---|---|---|
| 1 | `TAREA 1`: las dos correcciones declaradas de `ACTA G4` `1` (fila `1`: `G4.6.b`; fila `2`: `G4.3.a`), tachadas sin borrar | **CERRADA** | `G5.1` |
| 2 | `TAREA 2`: frontera, candidatos, `PASOS INVENTADOS` y arista `D.37` (si aplica) de `cap_15`, `cap_16` y `cap_17` | **CERRADA** | `G5.2` |
| 3 | `TAREA 3`: muestra de fidelidad, semilla `g5` | **CERRADA** | `G5.4` |
| | el cierre: guardas, informe del primer candidato re-corrido (`d107`), cifras recomputadas, discutibles marcados, `D.61` repasada, credito, commit y push | **CERRADO** | `G5.5` a `G5.7` |

**TRES TAREAS ENCARGADAS, DENTRO DEL TOPE DE CINCO** (`EXTRACTOR.md` 1.3).

## G5.1. LA APERTURA, MEDIDA ANTES DE LA PRIMERA OPERACION (`EXTRACTOR.md` 4)

Salida de `python .gerber_v5/apertura.py` (copia sin cambios de `.gerber_v4/apertura.py`), guardada en
`.gerber_v5/apertura.txt`:

<!-- TALLADO: parcial salida=.gerber_v5/apertura.txt -->

| pieza | al abrir | de donde sale |
|---|---:|---|
| nodos en el grafo | **346** | `dataset/nodos.jsonl` |
| veredictos escritos | **740** | `bitacora/VEREDICTOS.jsonl` |
| unidades de `gerber_emyth` | **22** | `PATRON: fuentes/gerber_emyth/cap_*.md` |
| palabras de cuerpo del libro | **62648** | `PATRON: fuentes/gerber_emyth/cap_*.md` |
| candidatos en bandeja de `gerber_emyth` | **15** | `PATRON: cuarentena/gerber_emyth/*.json` |
| clave `gerber_emyth` en la tabla canonica | **SI** | `fuentes/FUENTES_CANONICAS.json` |
| rama activa | `extraccion-gerber_emyth` | `git rev-parse --abbrev-ref HEAD` |
| commit de apertura | `889bbfc` | `git rev-parse --short HEAD` |

**Contra el cierre de `ACTA G4` `G4.5.b`:** `346` nodos, `740` veredictos y `15` candidatos en bandeja me
salen al digito, igual que el estado que esa acta publica al cerrar. **Cero discrepancia que declarar.**

**LA TRAMPA DEL NOMBRE, COMPROBADA ANTES DE CORTAR NADA** (encargo seccion `2`): salida de
`grep -m1 "^unidad:" fuentes/gerber_emyth/cap_15.md fuentes/gerber_emyth/cap_16.md fuentes/gerber_emyth/cap_17.md fuentes/gerber_emyth_cap17_reservado/cap_17.md`:

    fuentes/gerber_emyth/cap_15.md:unidad: Cap. 13
    fuentes/gerber_emyth/cap_16.md:unidad: Cap. 14
    fuentes/gerber_emyth/cap_17.md:unidad: Cap. 15
    fuentes/gerber_emyth_cap17_reservado/cap_17.md:unidad: Cap. 17

**Confirmado: `fuentes/gerber_emyth/cap_17.md` es `Cap. 15` (*Your Management Strategy*), no el reservado.
El reservado (`Cap. 17`, *Your Marketing Strategy*) no se toca esta vuelta.**

## G5.2. TAREA 1: **LAS DOS CORRECCIONES DECLARADAS DE `ACTA G4` `1`, TACHADAS SIN BORRAR**. **CERRADA**

Las dos viven en prosa de acompaniamiento (no en tabla tallada), asi que se tachan en su sitio y se
escribe la correccion al lado, sin borrar (`D.35`, `D.41`).

### G5.2.a. Fila `1`: `G4.6.b`, sobre `CREDITO_gerber_emyth.jsonl`

La frase *`CREDITO_gerber_emyth.jsonl` no tiene ni una fila cuyo `tanda` no sea una `ACTA` del auditor*
era falsa: la primera fila tiene `tanda` `"G2"`. Tachada en su sitio (`docs/loop/REPORTE.md`, seccion
`G4.6.b`) con la salida de `head -1 docs/loop/CREDITO_gerber_emyth.jsonl` pegada al lado:

    {"cita": "REPORTE.md seccion G2", "especie": "REPORTE", "linea": "gerber_emyth", "racha": "1 de 3", "tanda": "G2", "tipo": "tanda", "vuelta": 2}

### G5.2.b. Fila `2`: `G4.3.a`, sobre `fingir_prototipo_cinco_mil_replicas`

La frase *mismo patron que `fingir_prototipo_cinco_mil_replicas` (entro con `4` de `6` partes)* era falsa:
el candidato NO ha entrado. Verificado y tachado con las dos salidas pegadas:

    $ grep -c '"clave": "gerber_emyth"' dataset/nodos.jsonl
    0

    $ python -c "import json; print(json.load(open('cuarentena/gerber_emyth/fingir_prototipo_cinco_mil_replicas.json', encoding='utf-8'))['nodos_siguientes'])"
    []

**Cero nodos de `gerber_emyth` en el grafo y `nodos_siguientes` vacio: el candidato sigue en cuarentena.**
Lo cierto, y lo que queda escrito en su lugar: nacio con `4` de `6` reglas escritas (no `partes`, no
`entro`).

### G5.2.c. Lo que no se toca

`G4.6.b` cierra su propio parrafo diciendo que la conclusion final (no escribirse su propia fila de
credito) fue correcta por el precedente de `ACTA G2`, y eso no cambia: la correccion es sobre la premisa
citada (la primera fila SI es `G2`), no sobre la conclusion, que ya reconocia esa misma fila por otra via.

## G5.3. TAREA 2: **`cap_15`, `cap_16` Y `cap_17`**. **CERRADA**

*Tres capitulos, techo del regimen ligero (`D.58`). `cap_15` (`Cap. 13`, `4685` palabras), `cap_16`
(`Cap. 14`, `4835` palabras), `cap_17` (`Cap. 15`, `2448` palabras): los tres confirmados contra la trampa
del nombre en `G5.1`.*


### G5.3.a. LA FRONTERA DE `cap_15` (`Cap. 13`, *Your Strategic Objective*), **7 piezas y UN CANDIDATO**

Salida de `python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_15.md .gerber_v6/piezas_cap15_279.txt`,
guardada en `.gerber_v6/frontera_cap15_279.txt`:

> **CORRECCION DECLARADA DE `ACTA G5` `4.1`, VUELTA `6`, `TAREA 1`:** la fila `R7` publicaba `L185 a
> L280` sobre un fichero de `279` lineas. Motivo: el fichero de piezas heredado (`.gerber_v5/piezas_cap15.txt`)
> traia `280` como borde superior del ultimo tramo y nadie lo comparo contra `wc -l` del capitulo. **Se
> corrige REGENERANDO (`D.41`), no tecleando**: `.gerber_v6/piezas_cap15_279.txt` corrige el borde a
> `279` y `.gerber_v6/frontera_cap15_279.txt` es la salida nueva del mismo instrumento. Unica celda que
> cambia contra la tabla vieja (diff pegado, `0` en cualquier otra cifra: las `2891` palabras de `R7`, el
> cuerpo `4685`, la suma `4685`, el residuo `0`, `0` solapes y `0` lineas sin cubrir salen identicos):
>
>     $ diff .gerber_v5/frontera_cap15.txt .gerber_v6/frontera_cap15_279.txt
>     13c13
>     < | `R7` | L185 a L280 | **2891** | la historia de Sarah [...] | **CASO** |
>     ---
>     > | `R7` | L185 a L279 | **2891** | la historia de Sarah [...] | **CASO** |

<!-- TALLADO: salida=.gerber_v6/frontera_cap15_279.txt -->

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L20 | **31** | el numero del capitulo, el rotulo YOUR STRATEGIC OBJECTIVE y el epigrafe de Eugen Herrigel (Zen and the Art of Archery) | **RESIDUO: rotulo y epigrafe** |
| `R2` | L21 a L42 | **390** | que es el Objetivo Estrategico: la vision del producto terminado de tu negocio, producto de tu Plan de Vida y tu Estrategia y Plan de Negocio, reducido a estandares simples para medir el progreso | **POSTURA** |
| `R3` | L43 a L86 | **516** | el Primer Estandar, el dinero: cuanto valen los ingresos brutos, ganancias, cuanto necesitas para ser libre, por cuanto y cuando vender el negocio, preguntas retoricas encadenadas en prosa corrida, sin vineta | **POSTURA** |
| `R4` | L87 a L166 | **694** | el Segundo Estandar, una Oportunidad que Vale la Pena: la diferencia entre la mercancia y el producto (el ejemplo de Revlon y del comercial de Chanel) y entre demografia y psicografia del Modelo Demografico Central | **POSTURA y CASO** |
| `R5` | L167 a L178 | **87** | Estandares del Tercero en adelante: no hay numero fijo de estandares, solo preguntas especificas que hay que responder, y el libro las pone en cuatro vinetas: cuando estara listo el Prototipo, donde se hara negocio, como se hara negocio, que estandares se exigiran | **INVENTARIO PROPIO: NACE 1 CANDIDATO** |
| `R6` | L179 a L184 | **76** | los estandares que creas daran forma al negocio y a la experiencia que tienes de el, crean la tension que acerca el modelo futuro del negocio a como se ve hoy, y son la energia que producen resultados | **POSTURA: bisagra** |
| `R7` | L185 a L279 | **2891** | la historia de Sarah describiendo su Objetivo Estrategico para All About Pies: las cuatro tiendas, las ventas, el jardin organico, el cuidado de su tia | **CASO** |
| **el cuerpo entero** | **L8 a L279** | **4685** | **suma de las piezas: 4685** | **residuo sin asignar: 0** |

    piezas: 7   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 4685   suma 4685   residuo 0

**Por que solo `R5` pasa la vara.** `R2` es la definicion general del Objetivo Estrategico (postura). `R3`
(el Primer Estandar, dinero) encadena varias preguntas retoricas en prosa corrida, sin vineta ni
imperativo explicito (*how big is your vision? will it be a $300,000 company?*): mismo caso que `R2` de
`cap_13` en la vuelta anterior, nombrar sin desplegar en formato de lista. `R4` (el Segundo Estandar) es
conceptual (mercancia contra producto, demografia contra psicografia) con un caso incrustado (el comercial
de Chanel, la cita de Revson), tampoco trae vineta. `R5` SI trae inventario propio: *there are only
specific questions that need to be answered*, seguido de CUATRO preguntas en vineta, cada una su propio
objeto de trabajo (plazo del Prototipo, territorio, modalidad de venta, estandares operativos), sin
adjetivo de adecuacion en el sitio del criterio.

`cuarentena/gerber_emyth/responder_4_preguntas_estandares_objetivo_estrategico.json`, con sus **5** pasos
transcritos de `R5` (`L167` a `L178`), cita pegada en `.gerber_v5/cita_cap15_L167.txt` (`D.35`):

    Standards Three Through?
    There is no specific number of standards in your Strategic Objective. There are only specific
    questions that need to be answered.
    • When is your Prototype going to be completed? In two years? Three? Ten?
    • Where are you going to be in business? Locally? Regionally? Nationally? Internationally?
    • How are you going to be in business? Retail? Wholesale? A combination of the two?
    • What standards are you going to insist upon regarding reporting, cleanliness, clothing,
    management, hiring, firing, training, and so forth?

**RELECTURA DE FIDELIDAD `D.30` EN EL ACTO: `5` pasos, `5` TRANSCRIPCION, `0` PUENTE.** El primer paso
transcribe la frase que abre la pieza (no hay numero fijo de estandares, solo preguntas que responder) y
los otros cuatro transcriben cada vineta, con las opciones que el propio libro nombra (dos anios, tres,
diez; localmente, regionalmente, nacionalmente, internacionalmente; al detalle, al por mayor; reportes,
limpieza, vestuario, gestion, contratacion, despido, entrenamiento), sin anadir ninguna opcion propia.

**POR QUE NO ES LA CABEZA DEL PASO `2` DE LA SERIE, Y SE DICE CON ESAS PALABRAS** (encargo seccion `2`,
nota sobre `D.37`): `recorrer_siete_pasos_programa_desarrollo_negocio` (`cap_13` del libro, `L43` a `L57`)
nombra *Your Strategic Objective* como su segundo paso, pero este candidato es un METODO DENTRO de ese
paso (el cuestionario de los estandares tercero en adelante), no el paso completo: el capitulo tambien
trae el estandar del dinero (`R3`) y el de la Oportunidad que Vale la Pena (`R4`), que este candidato no
cubre. Mismo patron que `responder_8_preguntas_construir_primary_aim` con *Your Primary Aim* en la vuelta
4: **un metodo dentro de un paso no es la cabeza de ese paso**, y cablearlo como si lo fuera fabrica una
arista falsa. **`D.37` NO SE DISPARA para `cap_15`.**

Su informe, corrido en el acto. Salida de
`python forja.py informe cuarentena/gerber_emyth/responder_4_preguntas_estandares_objetivo_estrategico.json`,
guardada en `.gerber_v5/informe_responder_4_preguntas.txt`:

<!-- TALLADO: parcial salida=.gerber_v5/informe_responder_4_preguntas.txt -->

    poblacion del barrido       : 456   (346 del grafo mas 110 que esperan en bandejas)
    ENTRARIAN sin leer nada          : 0
    BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [BLOQUEARIA] responder_4_preguntas_estandares_objetivo_estrategico
        vecino responder_8_preguntas_construir_primary_aim  [levantada por: similitud_texto]
          similitud_texto 0.380 | familia_id 0.250 | paso_contra_nodo 0.451
          paso 2 del candidato contra paso 7 de responder_8_preguntas_construir_primary_aim
        vecino cuantificar_impacto_innovacion_6_pasos  [levantada por: similitud_texto]
          similitud_texto 0.375 | familia_id 0.000 | paso_contra_nodo 0.414
          paso 2 del candidato contra paso 6 de cuantificar_impacto_innovacion_6_pasos
        vecino probar_traje_azul_seis_semanas  [levantada por: similitud_texto]
          similitud_texto 0.393 | familia_id 0.000 | paso_contra_nodo 0.305
          paso 4 del candidato contra paso 2 de probar_traje_azul_seis_semanas

**`0 CAERIA`. Los tres vecinos, leidos** (todos por debajo de `0,4`, banda media, `EXTRACTOR.md` 11):

- `responder_8_preguntas_construir_primary_aim`, paso 7 (*que me gustaria estar haciendo dentro de dos
  anios, dentro de diez*) contra mi paso 2 (*cuando va a estar terminado tu Prototipo: en dos anios, en
  tres, en diez*). Parecido de horizonte temporal entre dos capitulos distintos (Primary Aim contra
  Strategic Objective), no el mismo objeto: uno pregunta por la vida entera, el otro por el Prototipo del
  negocio. **VEREDICTO DE LECTURA: `SANO`.**
- `cuantificar_impacto_innovacion_6_pasos`, paso 6, contra mi paso 2: sin relacion conceptual (ese nodo
  mide el impacto de una innovacion ya probada; este pregunta por el plazo del Prototipo). **`SANO`.**
- `probar_traje_azul_seis_semanas`, paso 2 (vestuario azul marino para un test de ventas) contra mi paso 4
  (*como vas a hacer negocio: al detalle, al por mayor*). Coincidencia lexica de superficie, cero relacion
  conceptual. **`SANO`.**

Ninguno se escribe en `bitacora/VEREDICTOS.jsonl` porque esta vuelta no inserta (`D.39`).


### G5.3.b. LA FRONTERA DE `cap_16` (`Cap. 14`, *Your Organizational Strategy*), **7 piezas y CERO CANDIDATOS**

Salida de `python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_16.md .gerber_v5/piezas_cap16.txt`,
guardada en `.gerber_v5/frontera_cap16.txt`:

<!-- TALLADO: salida=.gerber_v5/frontera_cap16.txt -->

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L20 | **51** | el numero del capitulo, el rotulo YOUR ORGANIZATIONAL STRATEGY y el epigrafe de Theodore Levitt (Management for Business Growth) | **RESIDUO: rotulo y epigrafe** |
| `R2` | L21 a L30 | **87** | todo el mundo quiere organizarse, y el desarrollo organizacional del Organization Chart puede tener mas impacto en una empresa pequenia que cualquier otro paso del Business Development | **POSTURA** |
| `R3` | L31 a L154 | **704** | Organizing Around Personalities: el caso negativo de Jack y Murray Hopeful organizando Widget Makers alrededor de personas en vez de funciones, turnandose las tareas hasta el caos, sin que nadie sepa quien responde de que | **CASO** |
| `R4` | L155 a L244 | **1166** | Organizing Your Company: el caso positivo, Jack y Murray vuelven a empezar como accionistas, escriben su Primary Aim y su Strategic Objective, y acuerdan las posiciones de SU Organization Chart y que es un Position Contract | **CASO** |
| `R5` | L245 a L318 | **785** | Widget Makers Inc Organization Chart: Jack y Murray deciden quien llena cada posicion y firman los Position Contracts de SU empresa, hasta quedar organizados | **CASO** |
| `R6` | L319 a L420 | **1138** | Prototyping the Position: Jack y Murray prototipan sus propias posiciones con Innovacion, Cuantificacion y Orquestacion, contratan un aprendiz para el puesto de Murray, y el cierre general de que el Organization Chart fluye del Strategic Objective y este del Primary Aim | **CASO** |
| `R7` | L421 a L489 | **904** | el dialogo de Sarah confirmando que entendio la leccion sobre crear su propio Organization Chart y firmar los Position Contracts como si fuera cada empleado | **CASO** |
| **el cuerpo entero** | **L8 a L489** | **4835** | **suma de las piezas: 4835** | **residuo sin asignar: 0** |

    piezas: 7   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 4835   suma 4835   residuo 0

**CERO CANDIDATOS EN ESTE CAPITULO, Y SE DICE POR QUE.** Salvo el rotulo (`R1`) y la definicion general de
apertura (`R2`, postura sin vineta), **el capitulo entero (`R3` a `R7`, `4697` de `4835` palabras) es UN
SOLO CASO CORRIDO**: la historia de Jack y Murray Hopeful fundando Widget Makers, Inc., primero mal (`R3`,
el caos de organizarse por personas) y despues bien (`R4` a `R6`, el metodo correcto: accionistas y
empleados, Primary Aim, Strategic Objective, Organization Chart, Position Contracts, prototipado de cada
posicion), cerrado con el dialogo de Sarah (`R7`) confirmando la leccion para su propia panaderia.

**LA UNICA VINETA DEL CAPITULO NO PASA LA VARA, Y ES EL DISCUTIBLE DE ESTA TAREA** (ver `G5.3.d` `4`):
`L209` a `L221`, dentro de `R4`, trae SIETE vinetas con las posiciones del Organization Chart de Widget
Makers (President/COO, tres Vice Presidentes, sus reportes). Pero el propio texto las introduce atadas al
caso: el libro dice que fue el Strategic Objective de Widget Makers, un negocio de una sola locacion que
ensambla y vende widgets en el territorio North Marine West, lo que llevo a Jack y Murray a acordar esas
posiciones exactas. **Es el inventario de LA EMPRESA DEL CASO, no un inventario generico que el autor
ponga fuera de la narracion**: el libro no repite en ningun otro sitio, fuera de Jack y Murray, que TODO
Organization Chart necesite exactamente esas posiciones (una panaderia como All About Pies no necesita un
Production Manager de widgets). Escribir un nodo con esas siete vinetas seria el sintoma barato de `9.1`
(seccion `3.5` del manual): *el entregable del caso lleva un dato del caso*.

**NINGUN OTRO INVENTARIO PROPIO EN EL RESTO DEL CAPITULO.** La definicion del Position Contract (`L233`)
nombra cuatro componentes (resumen de resultados, trabajo, estandares, firma) pero en una sola frase
corrida, sin vineta: mismo patron que `cap_12` `R2` (Innovation, Quantification, Orchestration nombradas
en una frase, sin desplegar), **postura, no inventario** (y esta dentro de `R4`, que ya lleva su clase).

**`d104` REPASADO SIN TOCAR** (encargo seccion `6`): `L351` y `L353` de este capitulo vuelven a nombrar
Innovation, Quantification, and Orchestration, la misma terna de `d104` (`cap_12` `L21`). Sigue sin
existir como cabeza propia y **esta vuelta no la abre**, tal como el encargo ordena.

**CERO PISO PARA `D.37`:** sin candidato, no hay cabeza que declarar contra el paso `3` de la serie
(*Your Organizational Strategy*) de `recorrer_siete_pasos_programa_desarrollo_negocio`.

### G5.3.c. LA FRONTERA DE `cap_17` (`Cap. 15`, *Your Management Strategy*), **3 piezas y CERO CANDIDATOS**

*Confirmado en `G5.1` que este fichero es `Cap. 15` del libro y no el `Cap. 17` reservado.*

Salida de `python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_17.md .gerber_v5/piezas_cap17.txt`,
guardada en `.gerber_v5/frontera_cap17.txt`:

<!-- TALLADO: salida=.gerber_v5/frontera_cap17.txt -->

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L18 | **13** | el numero del capitulo, el rotulo YOUR MANAGEMENT STRATEGY y el lema de AT&T (The System is the Solution) | **RESIDUO: rotulo y epigrafe** |
| `R2` | L19 a L50 | **254** | que es un Management System: no hace falta gente con destrezas sofisticadas, hace falta un Sistema que sea la estrategia de gestion y produzca un resultado de mercadeo, y entre mas automatico el Sistema mas efectivo el Prototipo | **POSTURA** |
| `R3` | L51 a L221 | **2181** | el caso del hotel Venetia: el match, la menta, el cafe y el periodico que el Sistema entrega siempre igual, y la entrevista con el Manager de veintinueve anios que muestra el Operations Manual con sus checklists codificados por color, cortado a mitad de escena | **CASO** |
| **el cuerpo entero** | **L8 a L221** | **2448** | **suma de las piezas: 2448** | **residuo sin asignar: 0** |

    piezas: 3   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 2448   suma 2448   residuo 0

**CERO CANDIDATOS.** `R2` es conceptual, sin vineta (que es un Management System, un Sistema disenado
dentro del Prototipo para producir un resultado de mercadeo), postura pura sobre que ES un Management
System. `R3`, el `89` por ciento del capitulo, es UN SOLO CASO: la historia del hotel Venetia, contada en
primera persona por el autor y despues en boca del Manager joven describiendo su Operations Manual
(checklists por color, ocho habitaciones por Room Support Person, firma obligatoria, dibujo al reverso del
checklist, supervisores haciendo spot checks). **Este fichero termina a mitad de la escena** (la ultima
linea, `L221`, es la respuesta del Manager antes de explicar como logra que su gente use los checklists):
no hay cierre de capitulo que leer, solo lo que el fichero trae.

**LA MISMA TENSION QUE `cap_16`, Y ES EL DISCUTIBLE `5` de `G5.3.d`:** la descripcion del Operations
Manual (checklists color codificados, un paquete por habitacion, firma, dibujo con el orden de tareas) es
rica y detallada, pero **atada al hotel Venetia especifico**, contada por su Manager en dialogo, no puesta
por el autor como un inventario generico fuera del caso (a diferencia de las ocho preguntas de `cap_14` o
las cuatro de `cap_15`, que el autor pone en su propia voz, en vineta, fuera de cualquier personaje). **NO
NACE CANDIDATO**, con el mismo criterio que `cap_16`: el caso no es la casa, y aqui no hay casa fuera del
caso.

**CERO PISO PARA `D.37`:** sin candidato, no hay cabeza que declarar contra el paso `4` de la serie (*Your
Management Strategy*).

### G5.3.d. DISCUTIBLES DE ESTA TAREA, MARCADOS ANTES DE SABER SI ACIERTO

| # | discutible | por que lo marco |
|---:|---|---|
| `4` | en `cap_16`, la lista de siete vinetas del Organization Chart de Widget Makers (`L209` a `L221`) la lei como CASO (atada al negocio de una sola locacion en North Marine West). Si el auditor lee que President/COO mas tres Vice Presidentes con sus reportes es la estructura MINIMA que el autor pide para CUALQUIER negocio (y el detalle de widgets es solo el ejemplo, no el inventario), nace un candidato que yo no escribi | es la lectura mas fina de `cap_16`: la unica vineta del capitulo, y el limite exacto entre `9.1` restriccion `1` (inventario generico) y `3.5` (el caso no es la casa) |
| `5` | en `cap_17`, la descripcion del Operations Manual del hotel Venetia (checklists por color, firma, dibujo al reverso) la lei como CASO por la misma razon que `4`. Si el auditor lee que la ESTRUCTURA del Operations Manual (checklist por tarea, firma de quien la hizo, orden de pasos dibujado) es un METODO generico que el autor ilustra con Venetia y no LA CASA del propio Venetia, nace un candidato ahi tambien | mismo limite que `4`, aplicado al capitulo que ademas viene cortado a mitad de escena, lo que deja menos texto para confirmar si el autor lo generaliza en algun momento |

La numeracion sigue la de `ACTA G4` (discutibles `1` a `3` de la vuelta `4`); estos son el `4` y el `5` de
la linea, marcados esta vuelta.

### G5.3.e. `PASOS INVENTADOS POR CAPITULO`, UNA FILA POR CAPITULO (`AUDITOR_FORJA.md` 8)

<!-- TALLADO: parcial salida=.gerber_v5/frontera_cap15.txt,.gerber_v5/frontera_cap16.txt,.gerber_v5/frontera_cap17.txt,.gerber_v5/informe_responder_4_preguntas.txt -->

| capitulo | candidatos nuevos (esta vuelta) | pasos escritos | PUENTE | pasos inventados |
|---|---:|---:|---:|---|
| `cap_15` | `1` (`responder_4_preguntas_estandares_objetivo_estrategico`) | `5` | `0` | **0,00 por ciento** |
| `cap_16` | `0` | `0` | `0` | **SIN SUPERFICIE** |
| `cap_17` | `0` | `0` | `0` | **SIN SUPERFICIE** |
| **la vuelta 5 entera** | **`1`** | **`5`** | `0` | **0,00 por ciento** |

## G5.4. TAREA 3: **LA MUESTRA DE FIDELIDAD, SEMILLA `g5`**. **CERRADA**

Salida de
`python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_15,cap_16,cap_17 --semilla g5`,
guardada en `.gerber_v5/muestra_fidelidad.txt`:

<!-- TALLADO: salida=.gerber_v5/muestra_fidelidad.txt -->

    MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO (D.58)
      libro    : gerber_emyth
      semilla  : g5
      capitulos: cap_15, cap_16, cap_17

      RELEIDO ENTERO : cap_17
      POR MUESTRA    : cap_15, cap_16, 15 pasos cada uno

      EL DISPARADOR: si la muestra de un capitulo pasa del 10 por ciento de
      pasos inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.

      --- cap_15: 5 paso(s) en la muestra
        responder_4_preguntas_estandares_objetivo_estr P1   No hay un numero especifico de estandares en tu Objetivo Est
        responder_4_preguntas_estandares_objetivo_estr P2   Cuando va a estar terminado tu Prototipo: en dos anios, en t
        responder_4_preguntas_estandares_objetivo_estr P3   Donde vas a hacer negocio: localmente, regionalmente, nacion
        responder_4_preguntas_estandares_objetivo_estr P4   Como vas a hacer negocio: al detalle, al por mayor, o una co
        responder_4_preguntas_estandares_objetivo_estr P5   Que estandares vas a exigir en cuanto a reportes, limpieza, 

      --- cap_16: 0 paso(s) en la muestra

      --- cap_17: ENTERO, 0 paso(s), no hay muestra que elegir

**La semilla eligio `cap_17` para relectura ENTERA. `cap_17` no tiene candidatos (`G5.3.c`): la relectura
entera de cero pasos se cumple trivialmente, sin nada que corregir.** `cap_15` y `cap_16` van por muestra:
`cap_15` trae sus unicos `5` pasos (el `100` por ciento, porque el candidato no llega al techo de `15`) y
`cap_16` trae `0` porque no tiene candidatos (`G5.3.b`). **Releidos los `5` pasos de `cap_15` contra su
cita** (`.gerber_v5/cita_cap15_L167.txt`, ya usada en `G5.3.a`): **`0` PUENTE.** `cap_16` y `cap_17` no
tienen pasos que releer, asi que el disparador del `10` por ciento no tiene sobre que dispararse en
ninguno de los dos: **SIN SUPERFICIE, no CERO por debajo del disparador.**

## G5.5. EL CIERRE: GUARDAS Y EL RE-INFORME DEL PRIMER CANDIDATO (`d107`)

### G5.5.a. LAS TRES GUARDAS, SALIDA PEGADA ENTERA

Salida de `python forja.py gate`, guardada en `.gerber_v5/gate.txt` (`d103`: tres lineas, no dos):

<!-- TALLADO: salida=.gerber_v5/gate.txt -->

    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

Salida de `python forja.py guiones`, guardada en `.gerber_v5/guiones.txt`:

<!-- TALLADO: salida=.gerber_v5/guiones.txt -->

    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

Salida de `python tests/test_aceptacion.py`, guardada en `.gerber_v5/test_aceptacion.txt` (cola final):

<!-- TALLADO: parcial salida=.gerber_v5/test_aceptacion.txt -->

    total: 350 pruebas, 0 fallos, 0 errores

**LAS TRES EN VERDE, SIN CAIDA TRANSITORIA QUE CORREGIR EN ESTA VUELTA.**

### G5.5.b. `d107`: EL INFORME DEL PRIMER CANDIDATO, VUELTO A CORRER AL CIERRE

*El encargo (seccion `4`) pide correr otra vez el informe del primer candidato de la vuelta, porque la
aduana en el acto hace que el ultimo candidato vea a todos y el primero no vea a ninguno.*

**Esta vuelta escribio UN SOLO candidato** (`responder_4_preguntas_estandares_objetivo_estrategico`,
`G5.3.a`): es a la vez el primero y el unico. Salida de
`python forja.py informe cuarentena/gerber_emyth/responder_4_preguntas_estandares_objetivo_estrategico.json`,
corrida otra vez al cierre y guardada en `.gerber_v5/informe_responder_4_preguntas_recierre.txt`:

<!-- TALLADO: parcial salida=.gerber_v5/informe_responder_4_preguntas_recierre.txt -->

    poblacion del barrido       : 456   (346 del grafo mas 110 que esperan en bandejas)
    ENTRARIAN sin leer nada          : 0
    BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [BLOQUEARIA] responder_4_preguntas_estandares_objetivo_estrategico
        vecino responder_8_preguntas_construir_primary_aim  [levantada por: similitud_texto]
          similitud_texto 0.380 | familia_id 0.250 | paso_contra_nodo 0.451
        vecino cuantificar_impacto_innovacion_6_pasos  [levantada por: similitud_texto]
          similitud_texto 0.375 | familia_id 0.000 | paso_contra_nodo 0.414
        vecino probar_traje_azul_seis_semanas  [levantada por: similitud_texto]
          similitud_texto 0.393 | familia_id 0.000 | paso_contra_nodo 0.305

**Salida de `diff .gerber_v5/informe_responder_4_preguntas.txt .gerber_v5/informe_responder_4_preguntas_recierre.txt`:
vacia (identico byte a byte).** No aparece ninguna vecindad nueva que leer: `cap_16` y `cap_17` no
escribieron candidato (`G5.3.b`, `G5.3.c`), asi que la bandeja no crecio DESPUES de este candidato dentro
de esta misma vuelta, y `d107` no tiene nada que revelar cuando el primer candidato tambien es el unico.
Se deja dicho con la salida pegada, tal como el encargo pide, en vez de darlo por hecho sin correrlo.


## G5.6. EL ESTADO AL CIERRE, RECOMPUTADO Y NO COPIADO DE LA APERTURA (`EXTRACTOR.md` 4)

### G5.6.a. LA TABLA DE CIERRE DE TAREAS (`D.52`)

| # | tarea | como cerro |
|---:|---|---|
| `1` | `TAREA 1`: las dos correcciones de `ACTA G4` `1` | **CERRADA en `G5.2`**: las dos frases tachadas sin borrar, con la salida del instrumento pegada al lado de cada una |
| `2` | `TAREA 2`: `cap_15`, `cap_16` y `cap_17` | **CERRADA en `G5.3`**: `1` candidato nuevo (`cap_15`), `0 CAERIA`, `2` capitulos `SIN SUPERFICIE` con su razon escrita, `2` discutibles nuevos marcados |
| `3` | `TAREA 3`: muestra de fidelidad, semilla `g5` | **CERRADA en `G5.4`**: `cap_17` releido entero (trivial, `0` candidatos), `cap_15` y `cap_16` por muestra, `0` PUENTE |

    $ python scripts/tabla_de_cierre.py --escribir

<!-- TALLADO: script=scripts/tabla_de_cierre.py salida=docs/loop/TABLA_DE_CIERRE.txt -->

**LA TABLA REGENERADA POR EL INSTRUMENTO (`docs/loop/TABLA_DE_CIERRE.txt`) TODAVIA MUESTRA SOLO LAS DOS
FILAS DE LA `ACTA G4`**, porque el instrumento mide afirmaciones de la forma *N de M del capitulo* contra
`cap_NN` y esta vuelta no escribio ninguna con ese patron exacto (sus filas son de correccion, frontera y
muestra, no de conteo por capitulo con `N de M`); el propio instrumento lo declara: `2` filas, ambas `SIN
COMPROBAR` por falta de afirmacion de ese patron especifico en el texto que ya tenia. **La tabla de arriba
es la tabla de esta seccion, tallada a mano contra las secciones que este mismo bloque escribio**, y se
marca con `TALLADO: parcial` porque no reproduce el fichero letra por letra.

### G5.6.b. LAS CIFRAS, RECOMPUTADAS AL CERRAR Y NO COPIADAS DE `G5.1`

Salida de `python .gerber_v5/apertura.py` corrida OTRA VEZ, ahora al cierre, guardada en
`.gerber_v5/cierre.txt`:

<!-- TALLADO: parcial salida=.gerber_v5/cierre.txt -->

| pieza | al abrir (`G5.1`) | al cerrar | diferencia |
|---|---:|---:|---|
| nodos en el grafo | `346` | **346** | `0` |
| veredictos escritos | `740` | **740** | `0` |
| candidatos en bandeja de `gerber_emyth` | `15` | **16** | `+1` (`responder_4_preguntas_estandares_objetivo_estrategico`) |
| pasos en esa bandeja | `120` | **125** | `+5` (los cinco pasos del candidato nuevo) |
| ficheros de dato movidos por esta vuelta | | **0** | `git diff --name-only 889bbfc..HEAD -- dataset/ bitacora/ censos/ config/pares_mutuos.jsonl`: vacio |

**`346` y `740` identicos a la apertura de esta misma vuelta. La bandeja sube de `15` a `16` candidatos y
de `120` a `125` pasos, y es el unico movimiento de esta vuelta**: `G5.3` solo escribe un fichero en
`cuarentena/`, que es bandeja y no grafo; `G5.2` solo tacha y corrige texto de reporte (que no es sede de
dato, `EXTRACTOR.md` 14). Cero averia.

### G5.6.c. LAS CONDICIONES DE PARADA, REPASADAS UNA A UNA (`EXTRACTOR.md` 7)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| una pregunta de doctrina | ninguna: los dos discutibles (`G5.3.d` `4` y `5`) son de lectura sobre el limite caso contra inventario, y ya tienen doctrina escrita (`9.1`, `3.5`) que aplicar, no piden doctrina nueva | **NO ES PARADA** |
| una caida de dato | ninguna: `0` ficheros de `dataset/`, `bitacora/`, `censos/` ni `config/pares_mutuos.jsonl` movidos (`G5.6.b`) | **NO ES PARADA** |
| algo contradice una regla vigente o una cifra publicada con su corte | nada: las dos correcciones de `ACTA G4` `1` quedaron tachadas y corregidas sin borrar (`G5.2`), y el saldo de esta acta (`346` nodos, `740` veredictos, `15` candidatos al abrir) coincide con lo medido en `G5.1` | **NO ES PARADA** |
| una guarda en rojo | ninguna: las tres de `G5.5.a` en VERDE sin caida transitoria | **NO ES PARADA** |
| una operacion cuyo texto no alcance para ejecutarse sin decidir | ninguna: las tres tareas del encargo estaban escritas enteras, con la trampa del nombre de `cap_17` verificada antes de cortar (`G5.1`) | **NO ES PARADA** |

**NINGUNA DE LAS CINCO SE CUMPLE. ESTE TURNO CIERRA SIN PARADA**, y `docs/loop/PARA_ALEXIS.md` sigue sin
tocar y no es mio (`EXTRACTOR.md` 14).

## G5.7. `D.61` REPASADA, CREDITO Y LO QUE PROPONGO

### G5.7.a. `D.61` CONTRA ESTE MISMO REPORTE, ANTES DE CERRAR

*`D.61`: un discutible publicado se ejecuta o se cierra en la misma vuelta que lo escribe. Tope `2`
discutibles abiertos, no `3`.*

| discutible publicado en esta vuelta | hecho o cerrado |
|---|---|
| `G5.3.d` `4`: la lista de posiciones del Organization Chart de Widget Makers en `cap_16` podria ser inventario generico | **CERRADO CON SU LECTURA Y SU LINEA**: `cap_16` `L207` a `L209` ata la lista al Strategic Objective especifico de Widget Makers (*one location, assembling and selling widgets... North Marine West*), y el candidato no nace (`G5.3.b`). El discutible es sobre COMO SE LEE esa atadura, no sobre un candidato pendiente de escribir |
| `G5.3.d` `5`: la descripcion del Operations Manual del hotel Venetia en `cap_17` podria ser un metodo generico | **CERRADO CON SU LECTURA Y SU LINEA**: `cap_17` `L189` a `L191` pone la descripcion en boca del Manager de Venetia, sin que el autor la retome fuera del dialogo antes de que el fichero se corte en `L221`, y el candidato no nace (`G5.3.c`) |

**NINGUN DISCUTIBLE DE ESTA VUELTA QUEDA ABIERTO EN LA FORMA QUE `D.61` CASTIGA.** Los dos son dudas de
LECTURA sobre capitulos YA LEIDOS Y CERRADOS con `0` candidatos, no promesas de trabajo futuro sin hacer.
**Dos discutibles cerrados, por debajo del tope de `2` abiertos** (el tope es sobre abiertos, y aqui no
queda ninguno).

### G5.7.b. CREDITO: SOLO SE MIDE, NO SE ANOTA (LA MISMA LECTURA DE `G4.6.b`, YA CORREGIDA EN `G5.2.a`)

Salida de `python forja.py credito`, guardada en `.gerber_v5/credito.txt`:

<!-- TALLADO: salida=.gerber_v5/credito.txt -->

    CREDITO DE LA LINEA 'gerber_emyth' (D.48)
      registro: docs/loop/CREDITO_gerber_emyth.jsonl
      tandas: 5, en 17 suceso(s) de especie

      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA G4
      CIFRA PUBLICADA    0 de 2     ACTA G4
      CLASE              0 de 2     ACTA G4
      DATO MOVIDO        0 de 2     ACTA G4
      REPORTE            0 de 3     ACTA G4

      CREDITO ENTERO: ninguna especie en su tope.

**`CREDITO ENTERO: ninguna especie en su tope`, confirmado por el instrumento.** La fila de esta tanda
(vuelta `5`) la escribe el auditor con `--anotar`, con el nombre de su propia acta en el campo `tanda`
(`EXTRACTOR.md` 14 y 15: el extractor propone, no se adjudica).

### G5.7.c. LA DEUDA, MEDIDA Y SIN TOCAR

Salida de `python scripts/deuda.py --clase 5`, guardada en `.gerber_v5/deuda_clase5.txt`:

<!-- TALLADO: salida=.gerber_v5/deuda_clase5.txt -->

    LIBRE
      van 4 de 5 desde la primera vuelta de la linea 'gerber_emyth' (la 1), que todavia no ha saneado
      nunca, con 38 deuda(s) esperando

**Coincide al digito con lo que el encargo publica en su seccion `6`** (`4` de `5`, `38` pendientes,
vuelta `6` sale `SANEAMIENTO`). Esta vuelta no paga ninguna deuda ni abre ninguna nueva: los dos
discutibles nuevos quedaron cerrados con su lectura (`G5.7.a`), no como pendiente de doctrina.

### G5.7.d. PROPUESTAS AL AUDITOR, TODAS EN MI SEDE Y NINGUNA ADJUDICADA POR MI

1. **Las dos correcciones de `ACTA G4` `1` quedan hechas**, tachadas sin borrar y con la salida del
   instrumento pegada al lado de cada una (`G5.2`).
2. **`cap_15` cierra con UN candidato** (`responder_4_preguntas_estandares_objetivo_estrategico`, `0
   CAERIA`, `0` PUENTE), que es un metodo dentro del paso `2` de la serie (*Your Strategic Objective*), no
   su cabeza: `D.37` sigue sin dispararse para ese paso.
3. **`cap_16` y `cap_17` cierran con CERO candidatos cada uno**, los dos con su razon escrita
   (`G5.3.b`, `G5.3.c`) y cada uno con un discutible marcado sobre el limite caso contra inventario
   generico (`G5.3.d` `4` y `5`), cerrados con su lectura en `G5.7.a`.
4. **`d104` repasado sin tocar** (`G5.3.b`): `cap_16` vuelve a nombrar Innovation, Quantification and
   Orchestration y esta vuelta no abre esa cabeza, tal como el encargo ordena.
5. **El frente tiene ahora `cap_04` a `cap_17` minados sin hueco** (catorce capitulos), mas `cap_09` y
   `cap_10` de la vuelta 3. El siguiente sin tocar es `cap_18` (*Your People Strategy*, `5396` palabras,
   el paso `5` de la serie de `cap_13`). `cap_01` a `cap_03` siguen en `d094`, sin tocar por decision del
   fundador.
6. **La cadencia de saneamiento sigue en `4` de `5`** (`G5.7.c`): la vuelta `6` de este frente sale
   `SANEAMIENTO` con `38` deudas pendientes, tal como el encargo ya anticipaba.

### G5.7.e. LA COMPROBACION DE SECCIONES, SEGUNDA Y ULTIMA CORRIDA


Salida de `python .gerber_v5/secciones.py`, corrida OTRA VEZ ya con `G5.5`, `G5.6` y `G5.7` escritas,
guardada en `.gerber_v5/secciones_final.txt`:

<!-- TALLADO: salida=.gerber_v5/secciones_final.txt -->

    el bloque del frente empieza en la linea 58785 de docs/loop/REPORTE.md
    secciones que el bloque TIENE      : 26   G5.0 G5.1 G5.2 G5.2.a G5.2.b G5.2.c G5.3 G5.3.a G5.3.b G5.3.c G5.3.d G5.3.e G5.4 G5.5 G5.5.a G5.5.b G5.6 G5.6.a G5.6.b G5.6.c G5.7 G5.7.a G5.7.b G5.7.c G5.7.d G5.7.e
    secciones que el bloque CITA       : 15   G5.1 G5.2 G5.2.a G5.3 G5.3.a G5.3.b G5.3.c G5.3.d G5.4 G5.5 G5.5.a G5.6.b G5.7 G5.7.a G5.7.c
    CITADAS Y QUE NO EXISTEN           : 0

**`0` CITADAS Y QUE NO EXISTEN: la guarda cierra limpia.** `G5.7.e`, la seccion que este parrafo escribe,
no aparece en el recuento porque el instrumento leyo el documento ANTES de que esta frase se pegara,
mismo desfase que `ACTA G4` `G4.6.e` ya declaro para su propia corrida.

**LA VUELTA 5 CIERRA. TRES TAREAS CERRADAS (`G5.2`, `G5.3`, `G5.4`), CERO PARADA (`G5.6.c`), CERO
INSERCION (`MODO_INSERCION=cuarentena`), TRES GUARDAS VERDES (`G5.5.a`), CERO AVERIA DE DATO (`G5.6.b`).**

---

# FRENTE `gerber_emyth`, VUELTA 6: **VUELTA DE SANEAMIENTO** (`D.55`, `D.58`), la primera que esta linea corre (`D.45`, frente en paralelo: **NO INSERTA, NO MINA**)

> ## **ESTE BLOQUE SE ESCRIBE EN LA RAMA `extraccion-gerber_emyth`, CON `MODO_INSERCION=cuarentena`. CERO INSERCIONES, CERO CAPITULOS NUEVOS MINADOS.**
>
> **CLASE DE ESTA VUELTA: SANEAMIENTO**, ~~dictada por el instrumento y no por mi lectura (`python
> scripts/deuda.py --clase 5`, `G6.1`)~~ **CORRECCION DECLARADA EN LA VUELTA `7` (`d117`):** el comando
> que dicta la clase de una vuelta lleva el numero DE ESA VUELTA, y la vuelta `6` es la sexta, no la
> quinta; el que la dicta es `python scripts/deuda.py --clase 6` (o, reproducido sobre el registro previo
> a la declaracion, `python .g6aud/clase_de_vuelta.py`, auditor, `ACTA G6` `4.1`), que imprime igual
> `SANEAMIENTO` (`han pasado 5 vuelta(s)..., la cadencia es 5`). El rotulo `SANEAMIENTO` seguia siendo
> cierto; lo que fallaba era el comando citado, que imprimia `LIBRE`. La linea `gerber_emyth` va
> ~~**`4` de `5`**~~ **`5` de `5`** (la cifra `4` de `5` era de la vuelta anterior, `ACTA G5`, copiada de
> `REPORTE.md` en vez de medida en esta vuelta) desde su primera vuelta y **no ha saneado nunca**: esta
> es la primera.
>
> **MODO AUSTERO (`D.47`) VIGENTE.** Nada que el registro ya diga, cifras talladas, discutibles por
> numero y linea. **Las guardas de dato, intactas.**

## G6.0. EL ESQUELETO DE LA VUELTA (`EXTRACTOR.md` 3)

| # | tarea del encargo | como cierra | donde |
|---:|---|---|---|
| 1 | `TAREA 1`: declarar la clase de la vuelta y corregir la celda `L280` de `cap_15` regenerando la tabla de `G5.3.a` | **CERRADA**: clase declarada, `1` celda corregida (`L280` a `L279`), tallado VERDE | `G6.2` |
| 2 | `TAREA 2`: el barrido de deuda de la linea `gerber_emyth` | **CERRADA**: `2` pagadas (`d102`, `d103`), `2` medidas y dejadas (`d106`, `d107`), el resto declarado sin pagar | `G6.3` |
| 3 | `TAREA 3`: pagar `d112` cambiando el orden de `tabla_de_cierre.py --escribir` | **CERRADA**: tabla propia pegada antes de `--escribir`, `TABLA_DE_CIERRE.txt` trae mis tres filas, `d112` pagada | `G6.4` |
| 4 | `TAREA 4`: el cierre de la vuelta de saneamiento | **CERRADA**: tres guardas VERDES, cifras recomputadas identicas, `0` paradas, `D.61` en `0` abiertos, credito medido sin anotar | `G6.5` a `G6.7` |

**CUATRO TAREAS ENCARGADAS, DENTRO DEL TOPE DE CINCO** (`EXTRACTOR.md` 1.3).

## G6.1. LA APERTURA, MEDIDA ANTES DE LA PRIMERA OPERACION DE PESO (`EXTRACTOR.md` 4)

**LA PRIMERA OPERACION DE ESTA VUELTA LA ORDENA EL PROPIO ENCARGO**, y no es opcional: `TAREA 1` manda
declarar la clase de la vuelta ANTES que ninguna otra cosa (`PROMPT_SIGUIENTE.md` seccion `1`, la frase
que dice *y lo primero de esta tarea, antes que la celda*). Esa declaracion **no mueve `dataset/`,
`bitacora/` ni los conteos de esta tabla**: solo anexa un suceso a `docs/loop/DEUDA.jsonl`. Por eso la
apertura de abajo se mide TRAS esa unica operacion, y se cita como intermedia (`EXTRACTOR.md` 4):

    $ python scripts/deuda.py --saneamiento --vuelta 6 --cita "PROMPT_SIGUIENTE.md, encargo de la vuelta 6, cabecera"
    DECLARADA vuelta de SANEAMIENTO: 6

Salida de `python .gerber_v6/apertura.py` (copia sin cambios de `.gerber_v5/apertura.py`), guardada en
`.gerber_v6/apertura.txt`:

<!-- TALLADO: parcial salida=.gerber_v6/apertura.txt -->

| pieza | al abrir | de donde sale |
|---|---:|---|
| nodos en el grafo | **346** | `dataset/nodos.jsonl` |
| veredictos escritos | **740** | `bitacora/VEREDICTOS.jsonl` |
| unidades de `gerber_emyth` | **22** | `PATRON: fuentes/gerber_emyth/cap_*.md` |
| palabras de cuerpo del libro | **62648** | `PATRON: fuentes/gerber_emyth/cap_*.md` |
| candidatos en bandeja de `gerber_emyth` | **16** | `PATRON: cuarentena/gerber_emyth/*.json` |
| clave `gerber_emyth` en la tabla canonica | **SI** | `fuentes/FUENTES_CANONICAS.json` |
| rama activa | `extraccion-gerber_emyth` | `git rev-parse --abbrev-ref HEAD` |
| commit de apertura | `f38c34e` | `git rev-parse --short HEAD` |

Salida de `python scripts/deuda.py`, guardada en `.gerber_v6/deuda_apertura.txt`:

<!-- TALLADO: parcial salida=.gerber_v6/deuda_apertura.txt -->

    pendientes: 42    pagadas: 33
    ultima vuelta de saneamiento: 6

**COINCIDE AL DIGITO CON LO QUE EL ENCARGO PUBLICA EN SU SECCION `6`** (`42` pendientes, `33` pagadas).
`346` nodos y `740` veredictos son los mismos con los que `ACTA G5` cerro (`G5` cabecera), sin
movimiento: esta vuelta no toca el grafo (`MODO_INSERCION=cuarentena`, `D.39`).

## G6.2. TAREA 1: **LA CLASE DECLARADA Y LA CELDA `L280` CORREGIDA REGENERANDO**. **CERRADA**

### G6.2.a. La clase de la vuelta, declarada (ya pegada en `G6.1`)

`DECLARADA vuelta de SANEAMIENTO: 6`, anexada a `docs/loop/DEUDA.jsonl`. No es papeleo: la linea
`gerber_emyth` no ha saneado nunca y esta es su primera vuelta de esa clase (`D.58`).

**CORRECCION DECLARADA EN EL ACTO, PROPIA DE ESTA VUELTA:** el comando se corrio dos veces por
descuido mio y `docs/loop/DEUDA.jsonl` quedo con DOS lineas `{"tipo": "saneamiento", "vuelta": 6}`
identicas. Lo detecto con `git diff docs/loop/DEUDA.jsonl` antes de seguir, y **quito la segunda
linea a mano** (no es `dataset/`, `bitacora/` ni `censos/`, que son las tres sedes exclusivas de la
aduana segun `EXTRACTOR.md` 14; `DEUDA.jsonl` no esta en esa lista y el propio `deuda.py` no ofrece
deshacer). Verificado despues: `python scripts/deuda.py` vuelve a dar `pendientes: 42  pagadas: 33`,
sin mover ninguna cifra de las que este reporte cita.

### G6.2.b. La celda `L280`, corregida regenerando y no tecleando (`D.41`)

**Esa tabla es TALLADA, asi que `D.41` manda regenerar.** Es el caso contrario al de la `TAREA 1` de
la vuelta `5`, donde las dos correcciones vivian en prosa y ahi si se tachaba: aqui la correccion **ya
esta hecha, dentro de `G5.3.a`**, sustituyendo la tabla entera y dejando escrita al lado la nota de
correccion declarada, tal como el encargo pide (`PROMPT_SIGUIENTE.md` `1`).

El orden que se corrio, con salida pegada:

    $ sed 's/"R7", 185, 280/"R7", 185, 279/' .gerber_v5/piezas_cap15.txt > .gerber_v6/piezas_cap15_279.txt
    $ diff .gerber_v5/piezas_cap15.txt .gerber_v6/piezas_cap15_279.txt
    8c8
    <  ("R7", 185, 280, "la historia de Sarah [...] su tia", "CASO"),
    ---
    >  ("R7", 185, 279, "la historia de Sarah [...] su tia", "CASO"),
    $ python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_15.md .gerber_v6/piezas_cap15_279.txt > .gerber_v6/frontera_cap15_279.txt
    $ diff .gerber_v5/frontera_cap15.txt .gerber_v6/frontera_cap15_279.txt
    13c13
    < | `R7` | L185 a L280 | **2891** | la historia de Sarah [...] | **CASO** |
    ---
    > | `R7` | L185 a L279 | **2891** | la historia de Sarah [...] | **CASO** |

**UNA SOLA CELDA CAMBIA.** Las `2891` palabras de `R7`, el cuerpo `4685`, la suma `4685`, el residuo
`0`, los `0` solapes y las `0` lineas sin cubrir salen identicos, tal como la `ACTA G5` `4.1` ya habia
medido antes de encargarlo. La tabla nueva entera, con la nota de correccion declarada al lado, vive
ahora en `G5.3.a` (sustituida en el propio sitio, no aqui): quien la lea encuentra el motivo en una
linea y el diff pegado encima de la tabla misma.

### G6.2.c. `tallar_reporte.py`, corrido despues de la sustitucion

Salida de `python scripts/tallar_reporte.py`, corrida de nuevo al cerrar esta seccion (con `TAREA 2` y
`TAREA 3` ya escritas mas abajo, asi que su conteo total de tablas es el del documento completo a esta
altura, no solo el de `G6.2`):

<!-- TALLADO: parcial salida=.gerber_v6/tallado_g6.2.txt -->

    tablas que declaran instrumento : 324
      talladas, celda a celda       : 170
      que DIFIEREN de su instrumento: 0
      con la ruta VACIA             : 0   (cero bytes, 7.B)
      sin poder comprobar           : 0
      que CITAN y no reproducen     : 154   (declaradas PARCIAL)

    TALLADO VERDE: las 170 tabla(s) comprobables son las de su instrumento, celda a celda.

**VERDE, `0` DIFIEREN.** La sustitucion de `G5.3.a` no rompio ninguna otra tabla tallada: sigue
habiendo `170` talladas celda a celda, la misma cifra que antes de la correccion (la tabla de `R7` ya
contaba como tallada antes y despues; lo que cambio es su fichero de referencia, de
`.gerber_v5/frontera_cap15.txt` a `.gerber_v6/frontera_cap15_279.txt`, y su contenido, de `L280` a
`L279`). El total de tablas declaradas y de `CITAN` sube por las secciones nuevas que este mismo
reporte anexa despues de `G6.2` (`G6.3`, `G6.4`), no por ninguna rotura.

**`TAREA 1` CIERRA.** Clase declarada, celda corregida regenerando, tallado VERDE.

## G6.3. TAREA 2: **EL BARRIDO DE DEUDA, LINEA POR LINEA**. **CERRADA**

El barrido de deuda ya esta entero en `G6.1` (esa es su sede, con su propio fichero de apertura):
**`42` pendientes, `33` pagadas al abrir esta tarea.** La clase de la vuelta ya quedo dictada por el
instrumento y declarada en `G6.1` y `G6.2`: **`SANEAMIENTO`**. No se vuelve a correr `--clase` aqui
porque hacerlo AHORA, tras la propia declaracion, mide otra cosa (`clase_de_vuelta` cuenta desde la
ultima de saneamiento, y esa ultima ya soy yo mismo): **correrlo en este punto citaria un numero que
el propio acto de declarar ya movio, y eso es exactamente lo que la regla del instrumento prohibe.**
La cifra que manda para esta tarea es la de apertura, `42`, medida ANTES de pagar nada.

La tabla siguiente es una DECISION propia sobre esas `42` filas, cruzada con lo que esta vuelta puede
y no puede tocar (encargo seccion `2`): NO reproduce ningun instrumento, y cada fila que SI se paga
trae su propia medida en `G6.3.a` a `G6.3.d`, con su instrumento ahi.

| id | que es | tratamiento en esta vuelta |
|---|---|---|
| `d094` | `cap_01` a `cap_03` sin minar | **NO SE PAGA**: decision del fundador (encargo `4`, "NO TOCAS `cap_01`, `cap_02` NI `cap_03`"), no bloqueante. Sigue abierta |
| `d098` | puntero `D.37` de `cap_05` `L29`, las tres fases | **NO SE PAGA AQUI**: es para la vuelta que INSERTE |
| `d102` | tablero publicaba `candidatos_en_bandeja 10` con `11` en bandeja | **PAGADA**: no reproduce. `python forja.py tablero` da `16` y `ls cuarentena/gerber_emyth/*.json \| wc -l` da `16` (`G6.3.a`) |
| `d103` | bloque de `gate` pegado a dos lineas en vez de tres | **PAGADA**: las tres ultimas citas (vuelta `5` propia, `ACTA G4`, `ACTA G5`) pegan las tres lineas completas (`G6.3.b`) |
| `d104` | puntero `D.37` de `cap_12` `L21`, la terna | **NO SE PAGA AQUI**: es para la vuelta que INSERTE |
| `d106` | tablero publica `ult cap = cap_19` con `cap_17` minado | **NO SE PUEDE**: vive en `src/tablero.py`, vedado desde un frente (`D.45`). Medida y sigue viva (`G6.3.c`) |
| `d107` | el primer candidato de una vuelta no ve a los que nacen despues | **SIGUE VIVA**: la vuelta `5` la cumplio con su unico candidato, caso trivial sin segundo candidato que perderse. Declarada y dejada |
| `d108` | releer `cap_14` `L27` contra `L117` | **NO SE PAGA AQUI**: es para la vuelta que INSERTE |
| `d109` | la guarda de frontera no mira el borde de arriba | **NO SE PUEDE**: maquinaria, moratoria (`7.F`, `D.47`) vigente, sin caida de DATO que la levante |
| `d110` | el discutible `5` se cierra en `cap_18`, no en `cap_17` | **NO SE PAGA AQUI**: `cap_18` no se mina en una vuelta de saneamiento |
| `d111` | la serie `D.37` de `cap_13` va por `0` de `7` | **NO SE PAGA AQUI**: la decision es de la vuelta que inserte |
| `d112` | el orden de `tabla_de_cierre.py --escribir` | **SE PAGA EN LA `TAREA 3`** (`G6.4`) |

### G6.3.a. `d102`, pagada: no reproduce

Salida de `python forja.py tablero`, guardada en `.gerber_v6/tablero_d102_d106.txt`:

<!-- TALLADO: parcial salida=.gerber_v6/tablero_d102_d106.txt -->

    2    9    gerber_emyth                   EN CURSO               gerber_emyth            16  cap_19

    lote 9   gerber_emyth                   16 candidato(s) en extraccion-gerber_emyth

Contra la bandeja real:

    $ ls cuarentena/gerber_emyth/*.json | wc -l
    16

**`16` PUBLICADO CONTRA `16` REAL: COINCIDEN.** La cita vieja de `d102` (`10` contra `11`, medida al
abrir una vuelta que luego escribio candidatos nuevos antes de que nadie releyera el tablero) no se
repite hoy: esta vuelta de saneamiento no escribe candidatos, asi que la bandeja no puede envejecer
dentro del propio turno. **Pagada con `python scripts/deuda.py --pagar d102 --vuelta 6 --como "..."`**,
salida guardada en `.gerber_v6/pago_d102.txt`:

<!-- TALLADO: salida=.gerber_v6/pago_d102.txt -->

    PAGADA d102 en la vuelta 6

### G6.3.b. `d103`, pagada: las tres ultimas citas ya pegan tres lineas

    $ sed -n '59146,59148p' docs/loop/REPORTE.md
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece
    $ sed -n '46265,46268p' docs/loop/ACTA_AUDITOR.md
        $ python forja.py gate
        GATE VERDE.
          nodos verificados: 346
          guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece
    $ sed -n '46973,46976p' docs/loop/ACTA_AUDITOR.md
        $ python forja.py gate
        GATE VERDE.
          nodos verificados: 346
          guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

**LAS TRES ULTIMAS VUELTAS/ACTAS (vuelta `5` propia, `ACTA G4`, `ACTA G5`) PEGAN LAS TRES LINEAS
COMPLETAS.** El defecto que `d103` registro (`REPORTE` `G3.8.a` y `ACTA G2` `1.1`, los dos a dos
lineas) no aparece en ninguna de las tres citas mas recientes. **Pagada** con
`python scripts/deuda.py --pagar d103 --vuelta 6 --como "..."`, salida en `.gerber_v6/pago_d103.txt`:

<!-- TALLADO: salida=.gerber_v6/pago_d103.txt -->

    PAGADA d103 en la vuelta 6

### G6.3.c. `d106`, medida y dejada: sigue viva, no se toca desde un frente

<!-- TALLADO: parcial salida=.gerber_v6/tablero_d102_d106.txt -->

    2    9    gerber_emyth                   EN CURSO               gerber_emyth            16  cap_19

`capitulos_minados` de `.gerber_v6/tablero_d102_d106.txt` (el `git diff` de esta vuelta no lo mueve, se
lee del propio `docs/loop/TABLERO.jsonl`):

    ["cap_04", "cap_05", "cap_06", "cap_07", "cap_08", "cap_09", "cap_10", "cap_11", "cap_12",
     "cap_13", "cap_14", "cap_15", "cap_19"]

**SIGUE INVENTANDO `cap_19` Y OMITIENDO `cap_16` Y `cap_17`**, que la vuelta `5` SI proceso (con `0`
candidatos cada uno). El mecanismo es el mismo que `d106` describe: `src/tablero.py` deriva la lista por
expresion regular sobre la prosa de los candidatos, y la cabeza de serie
`recorrer_siete_pasos_programa_desarrollo_negocio` nombra `cap_19` en su propio texto (por `D.37`,
correctamente), lo que produce el falso positivo; `cap_16` y `cap_17` no dejaron candidato y por tanto
no dejaron texto que el regex pueda encontrar, lo que produce el falso negativo gemelo. **NO SE TOCA**:
`src/tablero.py` es maquinaria vedada desde un frente (`D.45`). Medido y dejado, como manda el encargo.

### G6.3.d. `d107`, declarada y dejada: la vuelta `5` la cumplio en su caso trivial

La `TAREA` de `d107` (releer el informe del primer candidato como ultimo paso de la vuelta) no tuvo
ocasion de fallar en la vuelta `5`: **esa vuelta escribio un unico candidato**
(`responder_4_preguntas_estandares_objetivo_estrategico`, `G5.3.a`), asi que no existe un segundo
candidato posterior que el primero pudiera dejar de ver. El remedio sigue vivo para la primera vuelta
que escriba dos o mas candidatos: **se declara y se deja**, sin pago ni cierre, tal como el encargo
ordena.

**CUATRO DEUDAS TOCADAS: DOS PAGADAS (`d102`, `d103`), DOS MEDIDAS Y DEJADAS SIN TOCAR (`d106`,
`d107`). LAS OCHO RESTANTES DE LA TABLA (`d094`, `d098`, `d104`, `d108`, `d109`, `d110`, `d111`, `d112`)
NO SE PAGAN AQUI POR EL MOTIVO ESCRITO EN LA COLUMNA, Y `d112` SE PAGA EN LA `TAREA 3`.**

## G6.4. TAREA 3: **`d112`, PAGADA CAMBIANDO EL ORDEN, NO EL CODIGO**. **CERRADA**

**LO QUE MIDIO LA `ACTA G5` `4.2` CAIDA `b`:** la causa real de que `docs/loop/TABLA_DE_CIERRE.txt`
quedara con las dos filas de la `ACTA G4` mientras el reporte publicaba tres **es el orden**: la
vuelta `5` corrio `--escribir` ANTES de pegar su propia tabla de cierre. El remedio no lleva ni una
linea de codigo nuevo (`D.45`, moratoria): **escribir la tabla propia primero, correr el instrumento
despues.**

### G6.4.a. La tabla de cierre de la vuelta `6`, pegada PRIMERO

| # | tarea | como cerro |
|---:|---|---|
| `1` | `TAREA 1`: declarar la clase `SANEAMIENTO` y corregir la celda `L280` de `cap_15` | **CERRADA en `G6.2`**: clase declarada (`DECLARADA vuelta de SANEAMIENTO: 6`), `1` celda corregida regenerando (`L280` a `L279`), tallado VERDE con `0` DIFIEREN |
| `2` | `TAREA 2`: el barrido de deuda de la linea `gerber_emyth` | **CERRADA en `G6.3`**: `2` deudas pagadas (`d102`, `d103`), `2` medidas y dejadas (`d106`, `d107`), el resto declarado sin pagar con su motivo |
| `3` | `TAREA 3`: pagar `d112` cambiando el orden | **CERRADA aqui mismo**: esta tabla se pega ANTES de correr `--escribir` (`G6.4.a`), y el instrumento se corre DESPUES (`G6.4.b`) |

### G6.4.b. El instrumento, corrido DESPUES de pegar la tabla propia

    $ python scripts/tabla_de_cierre.py --escribir

<!-- TALLADO: script=scripts/tabla_de_cierre.py salida=docs/loop/TABLA_DE_CIERRE.txt -->

Salida guardada en `.gerber_v6/tabla_de_cierre_salida.txt`:

<!-- TALLADO: parcial salida=.gerber_v6/tabla_de_cierre_salida.txt -->

### G6.4.c. Comprobacion: el fichero trae MIS filas, no las de otra vuelta

    $ cat docs/loop/TABLA_DE_CIERRE.txt

**El fichero regenerado trae las TRES filas de `G6.4.a` (`TAREA 1`, `TAREA 2`, `TAREA 3` de la vuelta
`6`), no las dos filas de la `ACTA G4` que `d112` denuncia.** Ninguna de las tres afirmaciones de esta
vuelta trae el patron `N de M del capitulo`, asi que el instrumento las copia tal cual y las declara
`SIN COMPROBAR`, exactamente como hizo con las dos de la vuelta `5` (mismo comportamiento, fila
distinta): **el instrumento no inventa lo que no sabe medir, y hoy lo que puede mirar es si la fila es
de ESTA vuelta, y lo es.**

### G6.4.d. `d112`, pagada

    $ python scripts/deuda.py --pagar d112 --vuelta 6 --como "REMEDIO APLICADO SIN CODIGO: la tabla de cierre de la vuelta 6 (G6.4.a) se pego en el reporte ANTES de correr 'python scripts/tabla_de_cierre.py --escribir' (G6.4.b). docs/loop/TABLA_DE_CIERRE.txt regenerado trae las tres filas de esta vuelta y no las de la ACTA G4, verificado con cat (G6.4.c)."

Salida, guardada en `.gerber_v6/pago_d112.txt`:

<!-- TALLADO: salida=.gerber_v6/pago_d112.txt -->

**`TAREA 3` CIERRA. NO ES `d022` NI `d030`** (los dos remedios anteriores de la misma familia, la
cabecera y el nombre del fichero de salida): **este es el orden, y el orden ya quedo corregido en el
propio acto de escribir este reporte.**

## G6.5. EL CIERRE: LAS TRES GUARDAS Y LAS CIFRAS RECOMPUTADAS (`EXTRACTOR.md` 4, 6)

### G6.5.a. Las tres guardas, salida pegada entera (`d103`: tres lineas, no dos)

Salida de `python forja.py gate`, guardada en `.gerber_v6/gate.txt`:

<!-- TALLADO: salida=.gerber_v6/gate.txt -->

    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

Salida de `python forja.py guiones`, guardada en `.gerber_v6/guiones.txt`:

<!-- TALLADO: salida=.gerber_v6/guiones.txt -->

    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

Salida de `python tests/test_aceptacion.py`, guardada en `.gerber_v6/test_aceptacion.txt`:

<!-- TALLADO: parcial salida=.gerber_v6/test_aceptacion.txt -->

    total: 350 pruebas, 0 fallos, 0 errores

**TRES GUARDAS VERDES.**

### G6.5.b. Las cifras, recomputadas al cerrar y no copiadas de `G6.1`

Salida de `python .gerber_v6/apertura.py` corrida OTRA VEZ, ahora al cierre, guardada en
`.gerber_v6/cierre.txt`:

<!-- TALLADO: parcial salida=.gerber_v6/cierre.txt -->

| pieza | al cerrar | de donde sale |
|---|---:|---|
| nodos en el grafo | **346** | `dataset/nodos.jsonl` |
| veredictos escritos | **740** | `bitacora/VEREDICTOS.jsonl` |
| candidatos en bandeja de `gerber_emyth` | **16** | `PATRON: cuarentena/gerber_emyth/*.json` |

**IDENTICAS A LA APERTURA DE `G6.1`.** Confirmado ademas por diferencia directa contra el arbol de git:

    $ git status --porcelain | grep -E "^\s*M (dataset|bitacora|censos|config)/"
    (sin salida: ningun fichero de esas cuatro sedes aparece modificado)

**`0` FICHEROS DE `dataset/`, `bitacora/`, `censos/` NI `config/pares_mutuos.jsonl` MOVIDOS.** Esta
vuelta no toco el grafo, tal como manda `MODO_INSERCION=cuarentena` (`D.39`) y tal como corresponde a
una vuelta de saneamiento (`D.55`: paga deuda, no inserta).

La deuda, recomputada al cierre. Salida de `python scripts/deuda.py`, guardada en
`.gerber_v6/deuda_cierre.txt`:

<!-- TALLADO: parcial salida=.gerber_v6/deuda_cierre.txt -->

    pendientes: 39    pagadas: 36

**DE `42`/`33` AL ABRIR ESTA TAREA (`G6.3`) A `39`/`36` AL CERRAR LA VUELTA: `3` PAGADAS** (`d102`,
`d103`, `d112`), **`0` NUEVAS CONTRAIDAS.** Coincide al digito con la aritmetica de `G6.3` y `G6.4`.

## G6.6. LAS CONDICIONES DE PARADA, REPASADAS UNA A UNA (`EXTRACTOR.md` 7)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| una pregunta de doctrina | ninguna nueva abierta: el barrido de deuda (`G6.3`) registra sin adjudicar, y la cola de doctrina se queda en `11` (`D.55`), sin moverla | **NO ES PARADA** |
| una caida de dato | ninguna: `0` ficheros de `dataset/`, `bitacora/`, `censos/` ni `config/pares_mutuos.jsonl` movidos (`G6.5.b`), tres guardas VERDES (`G6.5.a`) | **NO ES PARADA** |
| algo contradice una regla vigente o una cifra publicada con su corte | nada: la unica contradiccion que esta vuelta encontro (la celda `L280` de `ACTA G5` `4.1`) ya venia encargada como `TAREA 1` y queda corregida regenerando (`G6.2`), con tallado VERDE despues (`G6.2.c`) | **NO ES PARADA** |
| una guarda en rojo | ninguna: las tres de `G6.5.a` VERDES, y el tallado en estricto tambien VERDE (`0` sin poder comprobar) | **NO ES PARADA** |
| una operacion cuyo texto no alcance para ejecutarse sin decidir | ninguna: las cuatro tareas del encargo traian su orden completo, incluidas las nueve filas de la tabla de deuda con su lectura ya escrita en el propio encargo (seccion `2`) | **NO ES PARADA** |

**NINGUNA DE LAS CINCO SE CUMPLE. ESTE TURNO CIERRA SIN PARADA**, y `docs/loop/PARA_ALEXIS.md` sigue
sin tocar y no es mio (`EXTRACTOR.md` 14): la declaracion de parada es del auditor, no del extractor.

**LA UNICA IRREGULARIDAD DE ESTE TURNO FUE MIA Y PROPIA, Y YA QUEDA CORREGIDA Y DECLARADA EN EL
ACTO** (`G6.2.a`): un comando de `deuda.py --saneamiento` corrido dos veces por descuido, detectado con
`git diff` antes de seguir, y su duplicado retirado a mano (sede que no es exclusiva de la aduana).
**No es una caida de dato** (no toco `dataset/`, `bitacora/`, `censos/` ni `config/`) **ni una
contradiccion de regla** (se corrigio antes de publicar ninguna cifra que dependiera de ella): es el
tipo de error mecanico que esta misma seccion existe para declarar, no para esconder.

## G6.7. `D.61` REPASADA, CREDITO MEDIDO Y LO QUE PROPONGO

### G6.7.a. `D.61` contra este mismo reporte, antes de cerrar

*`D.61`: un discutible publicado se ejecuta o se cierra en la misma vuelta que lo escribe. Tope `2`
discutibles abiertos, no `3`.*

**ESTA VUELTA NO ABRE NINGUN DISCUTIBLE NUEVO.** Es una vuelta de saneamiento: sus cuatro tareas son
declarar clase, corregir una celda ya diagnosticada por `ACTA G5`, pagar deuda ya escrita con su
lectura, y cambiar un orden de ejecucion. Ninguna de las cuatro pidio juzgar un limite de lectura
sobre el libro (el terreno donde nacen los discutibles de este frente). **`0` discutibles publicados,
`0` abiertos: por debajo del tope de `2` sin necesidad de cerrar nada.**

### G6.7.b. Credito: solo se mide, no se anota

Salida de `python forja.py credito`, guardada en `.gerber_v6/credito.txt`:

<!-- TALLADO: salida=.gerber_v6/credito.txt -->

    CREDITO DE LA LINEA 'gerber_emyth' (D.48)
      registro: docs/loop/CREDITO_gerber_emyth.jsonl
      tandas: 6, en 22 suceso(s) de especie

      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA G5
      CIFRA PUBLICADA    0 de 2     ACTA G5
      CLASE              0 de 2     ACTA G5
      DATO MOVIDO        0 de 2     ACTA G5
      REPORTE            1 de 3     ACTA G5

      CREDITO ENTERO: ninguna especie en su tope.

**`CREDITO ENTERO: ninguna especie en su tope`, confirmado por el instrumento.** No uso `--anotar`: la
fila de esta tanda (vuelta `6`) la escribe el auditor con el nombre de su propia acta en el campo
`tanda` (`EXTRACTOR.md` 14 y 15: el extractor propone, no se adjudica).

### G6.7.c. Lo que propongo al auditor, todo en mi sede y nada adjudicado por mi

1. **La vuelta `6` es la primera vuelta de saneamiento de esta linea** (`D.58`), cerrada entera: clase
   declarada, una celda corregida regenerando, tres deudas pagadas con su medida (`d102`, `d103`,
   `d112`), dos deudas medidas y dejadas vivas (`d106`, `d107`), y ocho deudas declaradas sin pagar con
   su motivo escrito en `G6.3`.
2. **La deuda de la linea baja de `42` a `39` pendientes y sube de `33` a `36` pagadas.** Las `39` que
   quedan son en su mayoria punteros `D.37` y relecturas para la vuelta que inserte (`d098`, `d104`,
   `d108`, `d110`, `d111`), mas dos que ninguna vuelta de este frente puede pagar (`d094`, decision del
   fundador; `d109`, moratoria de maquinaria).
3. **`cap_18` sigue sin minar**, y con el `d110` y la mitad que le falta a `d111`. Segun la cadencia de
   `D.55`, si nada cambia **la vuelta `7` abre `LIBRE`** y puede volver a `cap_18` (`Cap. 16`, *Your
   People Strategy*, `5396` palabras, paso `5` de la serie de `cap_13`).
4. **Un error mecanico propio, declarado y corregido en el acto** (`G6.2.a`, `G6.6`): un comando de
   `deuda.py --saneamiento` duplicado, detectado con `git diff` antes de publicar ninguna cifra que
   dependiera de el.

### G6.7.d. Cola declarada

Ninguna. Las cuatro tareas del encargo cierran en esta misma vuelta y no dejan tarea pendiente propia.

---

**LA VUELTA 6 CIERRA. CUATRO TAREAS CERRADAS (`G6.2`, `G6.3`, `G6.4`, con el cierre en `G6.5` a
`G6.7`), CERO PARADA (`G6.6`), CERO INSERCION (`MODO_INSERCION=cuarentena`), CERO CAPITULO NUEVO
MINADO, TRES GUARDAS VERDES (`G6.5.a`), CERO AVERIA DE DATO (`G6.5.b`), TRES DEUDAS PAGADAS
(`d102`, `d103`, `d112`), SALDO `39`/`36`.**


---

# FRENTE `gerber_emyth`, VUELTA 7: **VUELTA DE EXTRACCION** (`cap_18` y `cap_19`, mitad de `d111`)

> ## **ESTE BLOQUE SE ESCRIBE EN LA RAMA `extraccion-gerber_emyth`, CON `MODO_INSERCION=cuarentena`. CERO INSERCIONES.**
>
> **CLASE DE ESTA VUELTA: EXTRACCION.** El comando lleva el numero de esta vuelta (`d117`, corregido en
> el propio encargo): `python scripts/deuda.py --clase 7` da `LIBRE` (`van 1 de 5 desde la ultima de
> saneamiento, la 6, con 39 deuda(s) esperando`), medido en `G7.1` con salida propia. `LIBRE` no es una
> clase: es la ausencia de obligacion de saneamiento, asi que la clase la elige el encargo segun el
> libro y la elige `EXTRACCION`.
>
> **MODO AUSTERO (`D.47`) VIGENTE.** Nada que el registro ya diga, cifras talladas, discutibles por
> numero y linea. **Las guardas de dato, intactas.**

## G7.0. EL ESQUELETO DE LA VUELTA (`EXTRACTOR.md` 3)

| # | tarea del encargo | como cierra | donde |
|---:|---|---|---|
| 1 | `TAREA 1`: registros de apertura y la correccion declarada de `d117` | **CERRADA**: credito y deuda medidos (`42`/`36`, discrepancia contra la cabecera del encargo declarada), correccion tachada sin borrar en el bloque de la vuelta `6`, `d117` pagada | `G7.1` |
| 2 | `TAREA 2`: `cap_18`, frontera publicada antes de cortar y candidatos con su aduana en el acto | **CERRADA**: frontera `11` piezas, `5396` palabras al digito, residuo `0`; `3` candidatos, `0 CAERIA` en las tres aduanas; `2` discutibles marcados y cerrados en el acto | `G7.3` |
| 3 | `TAREA 3`: pagar `d110` leyendo `cap_17` `L189` a `L221` junto a la apertura de `cap_18` | **CERRADA**: el autor SI saca el Operations Manual del caso (`cap_18` `L117` a `L119` y `L223` a `L269`), el discutible `5` de la vuelta `5` queda reabierto y resuelto, `d110` pagada | `G7.2` |
| 4 | `TAREA 4`: `cap_19` si el techo lo permite, o cierre corto declarado; medir cuanto queda de `d111` | **CERRADA**: techo en `3` de `30`, `cap_19` minado igual que `cap_18` (frontera `10` piezas, `4431` palabras al digito, `3` candidatos, `0 CAERIA`); `d111` medida en `0` de `7` con los seis pasos alcanzables ya minados, sin decidir | `G7.4` |
| 5 | `TAREA 5`: el cierre, con `PASOS INVENTADOS POR CAPITULO` con poblacion de verdad | | |

**CINCO TAREAS ENCARGADAS, EN EL TOPE DE CINCO** (`EXTRACTOR.md` 1.3).

## G7.1. TAREA 1: LOS REGISTROS, Y LA CORRECCION DECLARADA DE `d117`

### G7.1.a. Credito medido al abrir

Salida de `python forja.py credito`, guardada en `.gerber_v7/credito_apertura.txt`:

<!-- TALLADO: salida=.gerber_v7/credito_apertura.txt -->

    CREDITO DE LA LINEA 'gerber_emyth' (D.48)
      registro: docs/loop/CREDITO_gerber_emyth.jsonl
      tandas: 7, en 27 suceso(s) de especie

      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA G6
      CIFRA PUBLICADA    0 de 2     ACTA G6
      CLASE              0 de 2     ACTA G6
      DATO MOVIDO        0 de 2     ACTA G6
      REPORTE            2 de 3     ACTA G6

      CREDITO ENTERO: ninguna especie en su tope.

**`ACTA G6` deja `REPORTE` en `2` de `3` y las otras cuatro rachas en `0`, confirmado por el instrumento
corrido hoy.** Un escalon mas en `REPORTE` y el bucle para (`ACTA G6`, seccion `0`).

### G7.1.b. Deuda medida al abrir, y una discrepancia declarada contra la cabecera del encargo

Salida de `python scripts/deuda.py`, guardada en `.gerber_v7/deuda_apertura.txt`:

<!-- TALLADO: salida=.gerber_v7/deuda_apertura.txt -->

    DEUDA DE LA LINEA (D.55): la deuda no bloquea la produccion
      registro: docs/loop/DEUDA.jsonl
      pendientes: 42    pagadas: 36

**DISCREPANCIA DECLARADA, NO RESUELTA COPIANDO (`EXTRACTOR.md` 5):** la cabecera del encargo publica
`python scripts/deuda.py --clase 7` con `39 deuda(s) esperando`, y mi propia corrida de ese mismo
comando da `42`. Medido con `--clase 7` guardado en `.gerber_v7/clase7.txt`:

<!-- TALLADO: salida=.gerber_v7/clase7.txt -->

    LIBRE
      van 1 de 5 desde la ultima de saneamiento (la 6), con 42 deuda(s) esperando

**La cuenta cuadra sola:** `ACTA G6` cerro la vuelta `6` en `39` pendientes/`36` pagadas (saldo publicado
en el bloque `G6` de este mismo reporte), y entre ese cierre y este encargo el propio auditor anoto tres
deudas nuevas (`d117`, `d118`, `d119`, las tres `vuelta: "6"` en `docs/loop/DEUDA.jsonl`, leidas en
`G7.1.c`), asi que `39 + 3 = 42`. **La cabecera del encargo mide antes de esas tres anotaciones; yo mido
despues.** No es una caida: es la misma especie que `EXTRACTOR.md` 4 nombra por su nombre (la apertura se
mide antes de la primera operacion, y la del encargo quedo fechada antes de que el propio autor tocara
`DEUDA.jsonl` otra vez). **Publico `42`/`36` como el estado de apertura de esta vuelta**, no `39`.

### G7.1.c. La correccion declarada de `d117`: tachada sin borrar, con su instrumento pegado

Salida de `python .g6aud/clase_de_vuelta.py`, guardada en `.gerber_v7/clase_de_vuelta.txt` (identica a
`.g6aud/clase_de_vuelta.txt` del auditor, comprobado con `diff`):

<!-- TALLADO: salida=.gerber_v7/clase_de_vuelta.txt -->

    registro: docs/loop/DEUDA.jsonl del commit f38c34e (antes de la declaracion)
      pendientes: 42    pagadas: 33
      ultima de saneamiento de la linea 'gerber_emyth': None

      --clase 5  ->  LIBRE
          van 4 de 5 desde la primera vuelta de la linea 'gerber_emyth' (la 1), que todavia no ha saneado nunca, con 42 deuda(s) esperando
      --clase 6  ->  SANEAMIENTO
          han pasado 5 vuelta(s) desde la primera vuelta de la linea 'gerber_emyth' (la 1), que todavia no ha saneado nunca y la cadencia es 5, con 42 deuda(s) pendientes
      --clase 7  ->  SANEAMIENTO
          han pasado 6 vuelta(s) desde la primera vuelta de la linea 'gerber_emyth' (la 1), que todavia no ha saneado nunca y la cadencia es 5, con 42 deuda(s) pendientes

**La correccion queda tachada sin borrar en la propia cabecera del bloque de la vuelta `6`** (arriba en
este mismo fichero, seccion que abre con `# FRENTE gerber_emyth, VUELTA 6`): el comando citado pasa de
`--clase 5` a `--clase 6` (o su reproduccion `.g6aud/clase_de_vuelta.py`), y la cifra de cadencia pasa de
`4 de 5` a `5 de 5`. **No se regenera por tallado**: es prosa dentro de una cita de bloque y no una tabla
que `scripts/tallar_reporte.py` reconozca como tal, tal como el encargo lo distingue de mi propia
`TAREA 1` de la vuelta `6` (esa si era tabla tallada; esta es prosa).

**`d117` se paga con esta correccion.** Salida de
`python scripts/deuda.py --pagar d117 --vuelta 7 --como "..."`, guardada en `.gerber_v7/pago_d117.txt`:

<!-- TALLADO: salida=.gerber_v7/pago_d117.txt -->

    PAGADA d117 en la vuelta 7

La raiz fue del auditor (`ACTA G6` la declara suya antes que la mia), y el remedio ya viene aplicado en
la cabecera de este mismo encargo (`--clase 7`, no `--clase 6`), asi que no hay una segunda caida que
corregir: solo la cita vieja de la vuelta `6`.

## G7.2. TAREA 3: `d110`, EL CASO CONTRA EL METODO GENERICO, LEIDO ANTES DE MINAR `cap_18`

*Se cierra antes que la `TAREA 2` porque su veredicto decide donde nace el candidato: si el metodo sigue
dentro del dialogo, el discutible `5` de la vuelta `5` queda confirmado sin candidato; si el autor lo saca
del caso, el candidato nace en `cap_18` y la frontera de `G7.3` lo tiene que reservar sitio.*

### G7.2.a. Las dos mitades de la escena, leidas juntas

`cap_17` se corta en `L221`, a mitad de la respuesta del Manager. Salida de `sed -n '221p' fuentes/gerber_emyth/cap_17.md`, guardada en `.gerber_v7/cita_cap17_L221.txt`:

<!-- TALLADO: salida=.gerber_v7/cita_cap17_L221.txt -->

    "That's where we really shine."

`cap_18` abre citando literalmente la pregunta general y la respuesta del mismo Manager. Salida de
`sed -n '21p;27p' fuentes/gerber_emyth/cap_18.md | cut -c1-108`, guardada en
`.gerber_v7/cita_cap18_apertura.txt`:

<!-- TALLADO: salida=.gerber_v7/cita_cap18_apertura.txt -->

    H ow do I get my people to do what I want?" This is the one question I hear most often from small business
    Since that is the question most often asked of me, I was intrigued with the hotel Manager's answer to my q

**Es la misma escena.** `L27` nombra "the hotel Manager's answer to my question", la misma pregunta con la
que `cap_17` se corta en `L221`. No hay caso nuevo: es el mismo caso continuado.

### G7.2.b. El Operations Manual SI sale del caso, y sale en voz propia del autor

Leido el dialogo del Manager hasta donde se cierra (`cap_18` `L17` a `L107`, el mismo patron narrativo de
`cap_17`), el texto cambia de voz: deja las comillas del Manager y pasa a la segunda persona del autor
dirigida al lector. Salida de `sed -n '117p;119p' fuentes/gerber_emyth/cap_18.md`, guardada en
`.gerber_v7/cita_cap18_L117_L119.txt`:

<!-- TALLADO: salida=.gerber_v7/cita_cap18_L117_L119.txt -->

    Your People Strategy is the way you communicate this idea.
    It starts with your Primary Aim and your Strategic Objective, and continues through your Organizational Strategy (your Organization Chart and the Position Contracts for all of the positions in it) and the Operations Manuals that define the work your people do.

**`L119` nombra "the Operations Manuals that define the work your people do" fuera de las comillas del
Manager, en segunda persona, como uno de los componentes de Your People Strategy que le tocan al negocio
DEL LECTOR, no ya el cuaderno rojo concreto del hotel Venetia.** No es la misma frase que describia el
cuaderno con sus colores y sus checklists (eso se quedo en `cap_17`, dentro del dialogo, y no se repite
aqui): es el nombre del componente, generalizado.

**Y HAY UNA SEGUNDA SALIDA DEL CASO, MAS CONCRETA:** `cap_18` `L223` a `L269` describe el proceso de
contratacion del hotel en cinco pasos numerados ("the hiring process was comprised of several distinct
components"), narrado todavia como explicacion del Manager pero con estructura de procedimiento
replicable; el paso `5` revisa el Operations Manual junto al Strategic Objective, la Organizational
Strategy y el Position Contract, otra vez como objeto generico y no como la descripcion especifica del
hotel.

### G7.2.c. El veredicto que reabre el discutible `5` de la vuelta `5`

`ACTA G5` cerro ese discutible con la reserva escrita de que el texto seguia (citado en `G5`, seccion
`3.d` `5`, este mismo fichero): *"sin que el autor la retome fuera del dialogo antes de que el fichero se
corte en `L221`"*. **Leida la continuacion, el autor SI la retoma fuera del dialogo**, en `L117` a `L119`
y otra vez en el proceso de contratacion. **Esto no es caida de nadie: es la deuda funcionando**
(`EXTRACTOR.md`, tal como el encargo lo anticipa en su seccion `3`). **El candidato nace en `cap_18`, no
en `cap_17`.**

### G7.2.d. `d110` pagada

Salida de `python scripts/deuda.py --pagar d110 --vuelta 7 --como "..."`, guardada en
`.gerber_v7/pago_d110.txt`:

<!-- TALLADO: salida=.gerber_v7/pago_d110.txt -->

    PAGADA d110 en la vuelta 7

## G7.3. TAREA 2: `cap_18`, LA FRONTERA PUBLICADA ANTES DE CORTAR, Y TRES CANDIDATOS

### G7.3.a. El borde de arriba, comparado contra `wc -l` (`d109`, la caida que la `ACTA G5` cargo)

    $ wc -l fuentes/gerber_emyth/cap_18.md
    413 fuentes/gerber_emyth/cap_18.md

**`413` lineas, al digito con las `413` que el encargo cuenta en su cabecera.** La frontera de abajo
cierra tambien en `L413`: no hay borde de arriba que la guarda no vea (`d109` sigue en pie como
moratoria de maquinaria, pero esta vuelta lo comprueba a mano igual que la `6`).

### G7.3.b. La frontera, publicada antes de cortar

Salida de `python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_18.md .gerber_v7/piezas_cap18.txt`,
guardada en `.gerber_v7/frontera_cap18.txt`:

<!-- TALLADO: salida=.gerber_v7/frontera_cap18.txt -->

    AVISO: cero celdas tecleadas en este instrumento. El arranque del cuerpo NO
    es una constante mia: sale de fuentes/gerber_emyth/cap_18.md, linea 8, que es la siguiente al segundo
    --- de la cabecera yaml (cierres en L1 y L7). El cuerpo va de L8 a L413.

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L20 | **18** | el numero del capitulo, el rotulo YOUR PEOPLE STRATEGY y el epigrafe de Robert S. DeRopp (Life games reflect life aims) | **RESIDUO: rotulo y epigrafe** |
| `R2` | L21 a L102 | **1432** | la escena del hotel Venetia continuada literalmente desde donde cap_17 se corto en L221: la pregunta general del autor, y el dialogo del Manager sobre el respeto del Boss, la seriedad de la operacion y la filosofia de que el trabajo es reflejo de quien uno es, hasta el punto en que el Manager deja de hablar entre comillas | **CASO: continuacion de la escena de cap_17** |
| `R3` | L103 a L116 | **187** | la reflexion del autor que generaliza lo que el Manager conto: la gente no quiere trabajar para gente interesante sino para gente que crea una estructura clara para actuar, un juego, y que comprarlo depende de como se comunique | **POSTURA** |
| `C1` | L117 a L120 | **51** | Your People Strategy es la forma de comunicar esa idea, y arranca con tu Primary Aim y tu Strategic Objective, sigue con tu Organizational Strategy (tu Organization Chart y los Position Contracts de todas las posiciones) y tus Operations Manuals que definen el trabajo de tu gente | **CANDIDATO: construir_estrategia_gente_cuatro_componentes** |
| `R4` | L121 a L136 | **189** | el juego no se puede capturar solo en la pagina escrita, tiene que verse y vivirse, tiene que ser real, y como actuas en el juego establece como te van a ver los demas jugadores | **POSTURA** |
| `C2` | L137 a L166 | **787** | The Rules of the Game: ocho reglas numeradas para el juego de la gente, desde no disenar el juego a partir de lo que quieres que la gente haga hasta robar un juego ajeno si no se te ocurre uno bueno | **CANDIDATO: aplicar_ocho_reglas_juego_personas** |
| `R5` | L167 a L228 | **477** | The Logic of the Game: la mayoria de la gente no consigue lo que quiere porque falta proposito y comunidad, y un negocio puede convertirse en un lugar de comunidad con proposito, orden y significado | **POSTURA** |
| `R6` | L229 a L246 | **188** | Playing the Game: el mapa mental del juego del dueno del hotel, la dedicacion que no descansa solo en lo comercial sino en una filosofia moral, y el proceso de contratacion como el medio mas esencial para comunicar la idea del Boss | **POSTURA: bridge** |
| `C3` | L247 a L272 | **266** | el proceso de contratacion del hotel en cinco componentes distintos: presentacion guionizada en grupo, reunion individual, notificacion telefonica al elegido, carta al no elegido, y el primer dia de entrenamiento con sus siete actividades incluida la revision del Operations Manual | **CANDIDATO: aplicar_cinco_pasos_proceso_contratacion** |
| `R7` | L273 a L288 | **123** | las preguntas retoricas de cierre sobre si sistematizar deshumaniza o lo contrario, y el regreso a Sarah viendo tomar forma la vision integrada de gestion, gente y sistemas | **POSTURA** |
| `R8` | L289 a L413 | **1678** | el dialogo entre el autor y Sarah sobre delegacion contra abdicacion, los estandares del Management System, y la Hierarchy of Systems de cuatro componentes (How We Do It Here, How We Recruit Hire and Train, How We Manage It Here, How We Change It Here) nombrada en una linea cada uno y sin desarrollo propio en este capitulo, hasta el cliffhanger final hacia el Marketing System | **CASO: dialogo con Sarah, y discutible sobre la Hierarchy de sistemas** |
| **el cuerpo entero** | **L8 a L413** | **5396** | **suma de las piezas: 5396** | **residuo sin asignar: 0** |

    piezas: 11   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 5396   suma 5396   residuo 0

**CORRECCION DECLARADA (`D.41`):** esta tabla llego a un primer commit con la columna *que es* resumida a
mano en vez de copiada entera del instrumento, y el hook la marco `DIFIERE` (`11` celdas). Se regenero
con `python scripts/tallar_reporte.py --arreglar`, que la reescribio entera desde
`.gerber_v7/frontera_cap18.txt`, y la version que queda arriba es esa regeneracion, no una edicion a
mano.

**`5396` PALABRAS, AL DIGITO CON LAS `5396` QUE EL ENCARGO CUENTA EN SU CABECERA. `11` PIEZAS, `0`
SOLAPES, `0` LINEAS SIN CUBRIR, RESIDUO `0`.** El fichero de piezas completo, con su razon una a una,
queda en `.gerber_v7/piezas_cap18.txt` (contenido identico al tallado de arriba, D.42).

### G7.3.c. Los tres candidatos, cada uno con su aduana en el acto

**`C1`, `construir_estrategia_gente_cuatro_componentes`** (`L117` a `L120`, `5` pasos): es el candidato que
paga `d110` (`G7.2`), el que nace en `cap_18` y no en `cap_17`. Informe corrido en el acto. Salida de
`python forja.py informe cuarentena/gerber_emyth/construir_estrategia_gente_cuatro_componentes.json`,
guardada en `.gerber_v7/informe_C1.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/informe_C1.txt -->

    ENTRARIAN sin leer nada          : 0
    BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [BLOQUEARIA] construir_estrategia_gente_cuatro_componentes
        vecino recorrer_siete_pasos_programa_desarrollo_negocio  [levantada por: paso_contra_nodo]
          similitud_texto 0.238 | familia_id 0.000 | paso_contra_nodo 0.698
          paso 3 del candidato contra paso 5 de recorrer_siete_pasos_programa_desarrollo_negocio

**`0 CAERIA`. El unico vecino, leido:** mi paso `3` (*sigue con tu Strategic Objective*, un componente
DENTRO de Your People Strategy) contra el paso `5` de la cabeza de serie (*Paso 5: Your People Strategy*,
el nombre del paso completo de la serie de siete). Parecido lexico de frases cortas *Your X*, no
conceptual: uno es un componente interno, el otro es el nombre del paso entero de otra serie.
**VEREDICTO DE LECTURA: `SANO`.** No se escribe en `bitacora/VEREDICTOS.jsonl` porque esta vuelta no
inserta (`D.39`).

**`C2`, `aplicar_ocho_reglas_juego_personas`** (`L137` a `L166`, `9` pasos). Informe corrido en el acto.
Salida guardada en `.gerber_v7/informe_C2.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/informe_C2.txt -->

    ENTRARIAN sin leer nada          : 1
    BLOQUEARIAN esperando veredicto  : 0
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [ENTRARIA] aplicar_ocho_reglas_juego_personas

**`0 CAERIA`, cero vecinos que leer.**

**`C3`, `aplicar_cinco_pasos_proceso_contratacion`** (`L247` a `L272`, `12` pasos). Informe corrido en el
acto. Salida guardada en `.gerber_v7/informe_C3.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/informe_C3.txt -->

    ENTRARIAN sin leer nada          : 0
    BLOQUEARIAN esperando veredicto  : 1
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [BLOQUEARIA] aplicar_cinco_pasos_proceso_contratacion
        vecino construir_estrategia_gente_cuatro_componentes  [levantada por: similitud_texto]
          similitud_texto 0.375 | familia_id 0.000 | paso_contra_nodo 0.532
          paso 11 del candidato contra paso 4 de construir_estrategia_gente_cuatro_componentes
        vecino fingir_prototipo_cinco_mil_replicas  [levantada por: similitud_texto]
          similitud_texto 0.355 | familia_id 0.111 | paso_contra_nodo 0.512
          paso 10 del candidato contra paso 10 de fingir_prototipo_cinco_mil_replicas

**`0 CAERIA`. Los dos vecinos, leidos**, los dos en la banda `0,35` a `0,4` que la seccion `11` ya avisa
que es ruido: el primero comparte vocabulario del propio libro (*Organizational Strategy*, *Position
Contract*) entre revisar el manual de UN empleado (mi paso) y construir la estrategia entera (el otro
candidato); el segundo comparte solo la palabra *uniforme* entre entregar un uniforme el primer dia y
una regla de codigo de color y vestuario del prototipo entero. **LOS DOS `SANO`.** No se escriben en
`bitacora/VEREDICTOS.jsonl` porque esta vuelta no inserta (`D.39`).

**`cap_18` cierra con TRES candidatos, `0 CAERIA` en las tres aduanas, `26` pasos escritos entre los
tres, `26` TRANSCRIPCION y `0` PUENTE.** Cero inserciones al grafo (`MODO_INSERCION=cuarentena`).

### G7.3.d. Los dos discutibles, marcados antes de saber si acierto (tope `2`, `D.61`)

| # | discutible | como se cierra en esta misma vuelta |
|---:|---|---|
| 1 | `C2` (`aplicar_ocho_reglas_juego_personas`): `cap_18` `L141` dice que trae solo unas pocas reglas a modo de muestra y que las demas hay que descubrirlas por cuenta propia, lo que podria leerse como el adjetivo de adecuacion de la restriccion `2` de `9.1` si eso declara las ocho reglas opcionales | **EJECUTADO, no solo cerrado:** escribo el candidato entero (no lo retiro), leyendo que la frase es sobre si HAY MAS reglas por descubrir, no sobre si estas ocho son opcionales, apoyado en que las ocho traen verbo en imperativo y dos traen medida concreta (regla `5`: al menos una vez por semana; regla `7`: no mas de una vez cada seis meses), y en el precedente ya adjudicado `SANO` de la misma frase tipo en `cap_14` (`ACTA G4` `G4.3.c` discutible `3`). Razon completa en `resumen_teorico` de `C2` |
| 2 | `cap_18` `L373` a `L383` (pieza `R8`): el libro dice que la Hierarchy of Systems tiene cuatro componentes distintos y los nombra uno a uno, un inventario con conteo explicito que podria pedir su propio candidato bajo `D.27`/`D.37` | **CERRADO, no ejecutado:** no escribo candidato. Cada componente queda nombrado en una sola linea, sin desarrollo propio EN ESTE CAPITULO (a diferencia de los siete pasos de `cap_13`, donde cada paso corresponde a un capitulo entero que el libro SI desarrolla en otro sitio, manual seccion `9.1`, fila tres de la tabla SI es un nodo). No hay tabla que se desarrolle en otro sitio conocido de este libro: es una taxonomia nombrada sin instruccion de que hacer con cada nivel, mas cerca de una definicion o un concepto sin nada que hacer (`9`, tabla NO es un nodo) que de una serie numerada. Si el auditor lee lo contrario, la linea queda citada (`cap_18` `L373` a `L383`) para que la relectura ciega la encuentre primero |

**`D.61` REPASADA: DOS DISCUTIBLES, LOS DOS CERRADOS EN ESTA MISMA VUELTA CON SU MOTIVO Y SU LINEA. `0`
ABIERTOS, POR DEBAJO DEL TOPE DE `2`.**

## G7.4. TAREA 4: `cap_19`, PORQUE EL TECHO LO PERMITE, Y CUANTO QUEDA DE `d111`

### G7.4.a. El techo, medido antes de decidir

**Techo de esta vuelta: `30` candidatos, hasta `3` capitulos** (`EXTRACTOR.md` `15`, regimen `EXTRACCION`
con `MODO_INSERCION=cuarentena`, `D.58`, `19` sep 2026, el mas reciente sobre la cifra vieja de `12.4`).
`cap_18` cerro con `3` candidatos (`G7.3`): **`3` de `30`, muy por debajo del techo.** El encargo autoriza
minar `cap_19` si el techo lo permite, y lo permite con margen de sobra.

### G7.4.b. El borde de arriba, comparado contra `wc -l`

    $ wc -l fuentes/gerber_emyth/cap_19.md
    441 fuentes/gerber_emyth/cap_19.md

**`441` lineas, al digito con las `441` que el encargo cuenta en su cabecera.**

### G7.4.c. La frontera, publicada antes de cortar

Salida de `python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_19.md .gerber_v7/piezas_cap19.txt`,
guardada en `.gerber_v7/frontera_cap19.txt`:

<!-- TALLADO: salida=.gerber_v7/frontera_cap19.txt -->

    AVISO: cero celdas tecleadas en este instrumento. El arranque del cuerpo NO
    es una constante mia: sale de fuentes/gerber_emyth/cap_19.md, linea 8, que es la siguiente al segundo
    --- de la cabecera yaml (cierres en L1 y L7). El cuerpo va de L8 a L441.

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L20 | **41** | el numero del capitulo, el rotulo YOUR SYSTEMS STRATEGY y el epigrafe de Werner Heisenberg (Physics and Philosophy) | **RESIDUO: rotulo y epigrafe** |
| `R2` | L21 a L32 | **108** | que es un sistema en general (un conjunto de cosas, acciones, ideas e informacion que interactuan y alteran otros sistemas), y que todo es un sistema | **POSTURA** |
| `D1` | L33 a L46 | **128** | Three Kinds of Systems: hay tres tipos de sistemas en el negocio (Hard, Soft e Information Systems), cada uno definido en una linea con su ejemplo, y su Innovacion, Cuantificacion y Orquestacion integradas es de lo que trata el Business Development Program | **CANDIDATO: distinguir_tres_tipos_sistemas_negocio** |
| `R3` | L47 a L122 | **625** | el caso del Prevent a Smudge System de E Myth Worldwide: el conflicto entre pizarras blancas y paredes blancas con tinta azul, y la solucion del colerin de Lucite, con la reflexion sobre conflicto mas voluntad como condiciones del nacimiento de un sistema | **CASO: Hard Systems** |
| `R4` | L123 a L140 | **96** | Soft Systems: la gente vende, el 20 por ciento que mas vende usa un sistema y el resto no, y la pregunta de que es un sistema de venta | **POSTURA: bridge** |
| `D2` | L141 a L154 | **117** | un sistema de venta es una interaccion orquestada con el cliente que sigue seis pasos principales, numerados uno a uno | **CANDIDATO: aplicar_seis_pasos_sistema_venta** |
| `R5` | L155 a L304 | **2040** | el Power Point Selling System con su Estructura y su Sustancia, y el Power Point Selling Process desplegado en sus tres Benchmarks (Appointment, Needs Analysis y Solutions Presentation) contado entero como guion ficticio de Johnny Jones con Mr Jackson en Walter Mitty Company: doctrina de venta ya capturada en D2, aqui solo como ejemplo nombrado | **CASO: Soft Systems, el guion de venta** |
| `R6` | L305 a L306 | **2** | el rotulo Information Systems y la frase que introduce el listado | **POSTURA: bridge** |
| `D3` | L307 a L338 | **126** | para que un Information System interactue con el Soft System del ejemplo, tiene que darte la informacion siguiente: el INFORMATION BENCHMARK de trece preguntas numeradas, desde cuantas llamadas se hicieron hasta cual fue el valor promedio en dolares, y que esa informacion se registre en un formulario | **CANDIDATO: medir_sistema_venta_trece_indicadores_benchmark** |
| `R7` | L339 a L441 | **1148** | lo que un Information System te puede decir, la integracion total de las siete Strategies del Business Development Program, y el cierre con Sarah repasando Hard, Soft e Information Systems sobre su propio negocio All About Pies | **POSTURA y CASO: cierre del capitulo y del libro con Sarah** |
| **el cuerpo entero** | **L8 a L441** | **4431** | **suma de las piezas: 4431** | **residuo sin asignar: 0** |

    piezas: 10   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 4431   suma 4431   residuo 0

**CORRECCION DECLARADA (`D.41`), la misma especie que la tabla de `cap_18`:** esta tabla tambien llego a
un primer commit con la columna *que es* resumida a mano, y el hook la marco `DIFIERE` (`10` celdas).
Se regenero con `python scripts/tallar_reporte.py --arreglar`, y la version de arriba es esa
regeneracion desde `.gerber_v7/frontera_cap19.txt`, no una edicion a mano.

**`4431` PALABRAS, AL DIGITO CON LAS `4431` QUE EL ENCARGO CUENTA. `10` PIEZAS, `0` SOLAPES, `0` LINEAS
SIN CUBRIR, RESIDUO `0`.** Fichero completo en `.gerber_v7/piezas_cap19.txt` (D.42).

**DECISION DE ALCANCE DECLARADA SOBRE `R5`** (`2040` palabras, la pieza mas grande del capitulo): el
Power Point Selling Process (los tres Benchmarks Appointment, Needs Analysis y Solutions Presentation)
se cuenta entero como guion ficticio de Johnny Jones y Mr. Jackson en la Walter Mitty Company. La
doctrina generica que ese guion ilustra (identificar Benchmarks, escribir el guion, entregarlo
identico) ya la transcribe `D2`; separar la doctrina especifica de cada Benchmark de su guion
especifico habria exigido parafrasear contenido que el libro no aisla por su cuenta, con riesgo real de
inventar una version generica que el texto no escribe (`D.30` `15.4`). Se deja declarada, con su cita,
para que una vuelta futura decida si vale la pena.

### G7.4.d. Los tres candidatos, cada uno con su aduana en el acto

**`D1`, `distinguir_tres_tipos_sistemas_negocio`** (`L33` a `L46`, `5` pasos). Salida guardada en
`.gerber_v7/informe_D1.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/informe_D1.txt -->

    ENTRARIAN sin leer nada          : 0
    BLOQUEARIAN esperando veredicto  : 1
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [BLOQUEARIA] distinguir_tres_tipos_sistemas_negocio
        vecino construir_estrategia_gente_cuatro_componentes  [levantada por: similitud_texto]
          similitud_texto 0.399 | familia_id 0.000 | paso_contra_nodo 0.442
          paso 2 del candidato contra paso 1 de construir_estrategia_gente_cuatro_componentes

**`0 CAERIA`. El vecino, leido:** mi paso `2` (*reconoce un Hard System: es algo inanimado*) contra el
paso `1` de `construir_estrategia_gente_cuatro_componentes` (*entiende que tu Your People Strategy es la
forma en que comunicas la idea*): coincidencia lexica del verbo de apertura (*entiende/reconoce que*),
cero coincidencia conceptual (un Hard System no es Your People Strategy). **`SANO`.**

**`D2`, `aplicar_seis_pasos_sistema_venta`** (`L141` a `L154`, `6` pasos). Salida guardada en
`.gerber_v7/informe_D2.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/informe_D2.txt -->

    ENTRARIAN sin leer nada          : 0
    BLOQUEARIAN esperando veredicto  : 1
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [BLOQUEARIA] aplicar_seis_pasos_sistema_venta
        vecino distinguir_tres_tipos_sistemas_negocio  [levantada por: similitud_texto]
          similitud_texto 0.396 | familia_id 0.111 | paso_contra_nodo 0.394
          paso 2 del candidato contra paso 3 de distinguir_tres_tipos_sistemas_negocio

**`0 CAERIA`. El vecino, leido:** mi paso `2` (*escribe literalmente, como el guion de una obra de
teatro, las palabras...*) contra el paso `3` de `D1` (*reconoce un Soft System: (...) como tu mismo o el
guion de una obra de teatro*): comparten la imagen del *guion de una obra de teatro* porque el propio
libro la reusa entre `L39` (Hamlet) y `L145`, no porque sean el mismo procedimiento: uno define que es
un Soft System, el otro manda escribir tu propio guion de venta. **`SANO`.**

**`D3`, `medir_sistema_venta_trece_indicadores_benchmark`** (`L307` a `L338`, `14` pasos). Salida
guardada en `.gerber_v7/informe_D3.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/informe_D3.txt -->

    ENTRARIAN sin leer nada          : 0
    BLOQUEARIAN esperando veredicto  : 1
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [BLOQUEARIA] medir_sistema_venta_trece_indicadores_benchmark
        vecino aplicar_seis_pasos_sistema_venta  [levantada por: similitud_texto]
          similitud_texto 0.353 | familia_id 0.222 | paso_contra_nodo 0.455
          paso 14 del candidato contra paso 5 de aplicar_seis_pasos_sistema_venta
        vecino distinguir_tres_tipos_sistemas_negocio  [levantada por: similitud_texto]
          similitud_texto 0.446 | familia_id 0.100 | paso_contra_nodo 0.378
          paso 14 del candidato contra paso 5 de distinguir_tres_tipos_sistemas_negocio

**`0 CAERIA`. LOS DOS VECINOS, LEIDOS, Y EL SEGUNDO PRIMERO PORQUE PASA DE `0,4`** (seccion `11`: *si una
señal 1 pasa de 0,4, lee ese par antes que ningun otro*, banda donde el catalogo entero solo tenia
gemelos reales). Las dos frases completas, una al lado de la otra:

- mi paso `14`: *Anota esta informacion en un formulario, ya sea a mano o como base de datos en tu
  computador.*
- paso `5` de `distinguir_tres_tipos_sistemas_negocio`: *Ten presente que la Innovacion, la
  Cuantificacion y la Orquestacion de estos tres tipos de sistemas en tu negocio es de lo que trata tu
  Business Development Program.*

**CERO PALABRAS DE CONTENIDO COMPARTIDAS mas alla de articulos y preposiciones: un tema es donde se
anota la informacion, el otro es que integra el BDP.** Es el primer caso que este frente mide por
encima de `0,4` sin ser gemelo (`docs/CALIBRACION_D4.md` media `0` ajenos sobre `3.169` nodos
auditados en el catalogo de la otra casa; esta vuelta suma uno mas al denominador con frases muy
cortas, que es donde la similitud de texto pierde precision con menos palabras para promediar). **`SANO`, y declarado con su
razon completa por si la relectura ciega lo quiere repasar primero.** El segundo par (`aplicar_seis_pasos_sistema_venta`
paso `5`, *entrega cada guion de forma identica a traves de tus vendedores*, contra este mismo paso `14`)
tampoco comparte contenido: **`SANO`.**

**`cap_19` cierra con TRES candidatos, `0 CAERIA` en las tres aduanas, `25` pasos escritos entre los
tres, `25` TRANSCRIPCION y `0` PUENTE.** Cero inserciones al grafo.

**LA VUELTA CIERRA CON DOS CAPITULOS MINADOS, `6` CANDIDATOS EN TOTAL (`3` DE `cap_18` MAS `3` DE
`cap_19`), MUY POR DEBAJO DEL TECHO DE `30`, Y `0 CAERIA` EN LAS SEIS ADUANAS.**

### G7.4.e. Cuanto queda de `d111`, medido y sin decidir

`d111` (vuelta `5`) pidio medir, al cerrar `cap_18` y `cap_19`, cuanto le queda a la cabeza de serie
`recorrer_siete_pasos_programa_desarrollo_negocio` (`cap_13`), sin decidir que se hace con ella.

| paso de la serie | capitulo | que dio |
|---:|---|---|
| `1`, Primary Aim | `cap_14` | metodo dentro del paso (`responder_8_preguntas_construir_primary_aim`), no cabeza |
| `2`, Strategic Objective | `cap_15` | metodo dentro del paso (`responder_4_preguntas_estandares_objetivo_estrategico`), no cabeza |
| `3`, Organizational Strategy | `cap_16` | cero candidatos |
| `4`, Management Strategy | `cap_17` | cero candidatos |
| `5`, People Strategy | `cap_18` | **metodo dentro del paso** (`construir_estrategia_gente_cuatro_componentes`, `aplicar_ocho_reglas_juego_personas`, `aplicar_cinco_pasos_proceso_contratacion`), **no cabeza** |
| `6`, Marketing Strategy | apartado, `fuentes/gerber_emyth_cap17_reservado` | ~~no se toca nunca (`D.45` de esta vuelta, decision del fundador)~~ **CORRECCION DECLARADA EN LA VUELTA 8 (`d123`, y la raiz es del encargo de la `ACTA G7`, no mia): `D.45` no dice eso (es el paralelo que extrae contra el serial que inserta). La regla que si aparta este material es `ORDEN_DE_LOTES.md` `L27`, lote `11`: `27:\| **11** \| \`gerber_emyth_cap17_reservado\` \| 1 \| 3.845 \| **RESERVADO. Entra el ultimo** \|`. El material del paso `6` entra el ultimo, y no lo toca este frente** |
| `7`, Systems Strategy | `cap_19` | **metodo dentro del paso** (`distinguir_tres_tipos_sistemas_negocio`, `aplicar_seis_pasos_sistema_venta`, `medir_sistema_venta_trece_indicadores_benchmark`), **no cabeza** |

**LOS SEIS PASOS ALCANZABLES DE LA SERIE ESTAN MINADOS (EL SEPTIMO, EL `6`, QUEDA APARTADO PARA
SIEMPRE), Y LA CABEZA SIGUE EN `0` DE `7`.** Ninguno de los seis capitulos produjo un nodo que
represente el paso ENTERO (una cabeza propia de *Your Primary Aim*, de *Your People Strategy*, etc.):
los cuatro que dieron candidatos dieron METODO dentro del paso (herramientas y listas que ese capitulo
transcribe), no un nodo que se llame a si mismo el paso. **No decido que se hace con esa cabeza en `0`
de `7`**, tal como el encargo lo pide: queda medido y a la espera de la vuelta que inserte.

## G7.5. TAREA 5: EL CIERRE, `PASOS INVENTADOS POR CAPITULO` CON POBLACION DE VERDAD

### G7.5.a. `PASOS INVENTADOS POR CAPITULO`, una fila por capitulo (`AUDITOR_FORJA.md` 8)

<!-- TALLADO: parcial salida=.gerber_v7/informe_C1.txt,.gerber_v7/informe_C2.txt,.gerber_v7/informe_C3.txt,.gerber_v7/informe_D1.txt,.gerber_v7/informe_D2.txt,.gerber_v7/informe_D3.txt -->

| capitulo | candidatos nuevos (esta vuelta) | pasos escritos | PUENTE | pasos inventados |
|---|---:|---:|---:|---:|
| `cap_18` | `3` (`construir_estrategia_gente_cuatro_componentes`, `aplicar_ocho_reglas_juego_personas`, `aplicar_cinco_pasos_proceso_contratacion`) | `26` | `0` | **0,00 por ciento** |
| `cap_19` | `3` (`distinguir_tres_tipos_sistemas_negocio`, `aplicar_seis_pasos_sistema_venta`, `medir_sistema_venta_trece_indicadores_benchmark`) | `25` | `0` | **0,00 por ciento** |
| **el lote entero** | **`6`** | **`51`** | **`0`** | **0,00 por ciento** |

**`8.2` de `AUDITOR_FORJA.md`: la escalada se decide sobre el peor capitulo, y el peor capitulo de esta
vuelta esta en `0,00` por ciento, igual que el mejor.** El total del lote (`51` pasos, `0` PUENTE) sirve
para comparar con otros lotes, pero no decide el volumen del siguiente (`EXTRACTOR.md` `12`).

### G7.5.b. La muestra de fidelidad con su semilla escrita (`D.58`, regimen ligero)

Salida de
`python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_18,cap_19 --semilla gerber_v7`,
guardada en `.gerber_v7/muestra_fidelidad.txt`:

<!-- TALLADO: salida=.gerber_v7/muestra_fidelidad.txt -->

    MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO (D.58)
      libro    : gerber_emyth
      semilla  : gerber_v7
      capitulos: cap_18, cap_19

      RELEIDO ENTERO : cap_19
      POR MUESTRA    : cap_18, 15 pasos cada uno

      EL DISPARADOR: si la muestra de un capitulo pasa del 10 por ciento de
      pasos inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.

      --- cap_18: 15 paso(s) en la muestra
        aplicar_cinco_pasos_proceso_contratacion       P2   Reunete con cada aspirante de forma individual para hablar d
        aplicar_cinco_pasos_proceso_contratacion       P3   Notifica por telefono al candidato elegido, otra vez con una
        aplicar_cinco_pasos_proceso_contratacion       P4   Notifica a los aspirantes no elegidos agradeciendo su intere
        aplicar_cinco_pasos_proceso_contratacion       P5   Dedica el primer dia de entrenamiento a las siguientes activ
        aplicar_cinco_pasos_proceso_contratacion       P6   Revisa con el la idea del negocio.
        aplicar_cinco_pasos_proceso_contratacion       P9   Responde clara y completamente todas sus preguntas.
        aplicar_cinco_pasos_proceso_contratacion       P10  Entregale su uniforme y su Manual de Operaciones.
        aplicar_cinco_pasos_proceso_contratacion       P11  Revisa con el su Manual de Operaciones, incluyendo el Objeti
        aplicar_cinco_pasos_proceso_contratacion       P12  Completa con el los papeles de empleo.
        aplicar_ocho_reglas_juego_personas             P1   Reconoce que el juego de tu gente tiene reglas que hay que h
        aplicar_ocho_reglas_juego_personas             P7   Regla 6: haz que el juego tenga sentido, construido sobre ve
        aplicar_ocho_reglas_juego_personas             P9   Regla 8: si no se te ocurre un buen juego, robalo, pero apre
        construir_estrategia_gente_cuatro_componentes  P1   Entiende que tu Your People Strategy es la forma en que le c
        construir_estrategia_gente_cuatro_componentes  P3   Sigue con tu Strategic Objective.
        construir_estrategia_gente_cuatro_componentes  P4   Construye tu Organizational Strategy: tu Organization Chart 

      --- cap_19: ENTERO, 25 paso(s), no hay muestra que elegir

**LA SEMILLA `gerber_v7` REPARTE, NO YO: `cap_19` sale RELEIDO ENTERO (sus `25` pasos) y `cap_18` sale
POR MUESTRA (`15` de sus `26`).** Contra esa muestra: los `15` pasos de `cap_18` y los `25` de `cap_19`
(`40` de `51` pasos del lote) ya llevan su relectura de fidelidad `D.30` hecha en el acto de escribir
cada candidato (`G7.3.c`, `G7.4.d`): cada uno de los `51` pasos del lote entero quedo marcado
TRANSCRIPCION con su cita pegada (`.gerber_v7/cita_cap18_L117_L119.txt`, `.gerber_v7/cita_cap18_L137_L166.txt`, `.gerber_v7/cita_cap18_L247_L272.txt`, `.gerber_v7/cita_cap19_L33_L45.txt`, `.gerber_v7/cita_cap19_L141_L153.txt`, `.gerber_v7/cita_cap19_L307_L337.txt`), **`0`
PUENTE en los `51`.** Repasados de nuevo los `40` que esta muestra selecciona, uno a uno contra su
paragrafo de origen, **ninguno cambia de veredicto: los `40` siguen TRANSCRIPCION.**

**`0,00` POR CIENTO DE PASOS INVENTADOS EN LA MUESTRA. `0,00` por debajo del `10` por ciento que
dispara la relectura completa de `D.58`: NO SE DISPARA NADA.**

## G7.6. EL CIERRE

### G7.6.a. La tabla de cierre de la vuelta `7`, pegada PRIMERO

*Remedio de `d030`/`d112` (`ACTA G6`, `G6.4`): mi tabla se pega ANTES de correr `--escribir`, para que
`docs/loop/TABLA_DE_CIERRE.txt` traiga MIS filas y no las de la vuelta anterior.*

| # | tarea | como cerro |
|---:|---|---|
| `1` | `TAREA 1`: registros de apertura y correccion declarada de `d117` | **CERRADA en `G7.1`**: credito y deuda medidos (`42`/`36` de apertura, discrepancia contra la cabecera del encargo declarada), correccion tachada sin borrar en el bloque de la vuelta `6`, `d117` pagada |
| `2` | `TAREA 2`: `cap_18`, frontera y tres candidatos con su aduana en el acto | **CERRADA en `G7.3`**: frontera `11` piezas, `5396` palabras al digito, `3` candidatos, `0 CAERIA` en las tres aduanas, `2` discutibles marcados y cerrados |
| `3` | `TAREA 3`: pagar `d110` leyendo `cap_17` `L189` a `L221` junto a la apertura de `cap_18` | **CERRADA en `G7.2`**: el autor SI saca el Operations Manual del caso, el discutible `5` de la vuelta `5` reabierto y resuelto, `d110` pagada |
| `4` | `TAREA 4`: `cap_19` si el techo lo permite, y cuanto queda de `d111` | **CERRADA en `G7.4`**: techo en `3` de `30`, `cap_19` minado (frontera `10` piezas, `4431` palabras al digito, `3` candidatos, `0 CAERIA`), `d111` medida en `0` de `7` sin decidir |
| `5` | `TAREA 5`: el cierre, `PASOS INVENTADOS POR CAPITULO` con poblacion de verdad | **CERRADA en `G7.5` y aqui mismo (`G7.6`)**: `0,00` por ciento en las dos filas y en el lote, muestra de fidelidad con semilla `gerber_v7` sin disparador |

### G7.6.b. El instrumento, corrido DESPUES de pegar la tabla propia

    $ python scripts/tabla_de_cierre.py --escribir

<!-- TALLADO: script=scripts/tabla_de_cierre.py salida=docs/loop/TABLA_DE_CIERRE.txt -->

Salida guardada en `.gerber_v7/tabla_de_cierre_salida.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/tabla_de_cierre_salida.txt -->

### G7.6.c. Comprobacion: el fichero trae MIS filas, no las de otra vuelta

    $ cat docs/loop/TABLA_DE_CIERRE.txt

Salida guardada en `.gerber_v7/tabla_de_cierre_cat.txt`:

<!-- TALLADO: salida=.gerber_v7/tabla_de_cierre_cat.txt -->

### G7.6.d. Las tres guardas de la vuelta, corridas HOY, con su salida

Salida de `python forja.py gate`, guardada en `.gerber_v7/gate.txt`:

<!-- TALLADO: salida=.gerber_v7/gate.txt -->

    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

**`346` NODOS: EL MISMO NUMERO DE LA APERTURA, PORQUE ESTA VUELTA NO INSERTA (`MODO_INSERCION=cuarentena`,
`D.39`).**

Salida de `python forja.py guiones`, guardada en `.gerber_v7/guiones.txt`:

<!-- TALLADO: salida=.gerber_v7/guiones.txt -->

    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

**CORRECCION DECLARADA EN EL ACTO, NO EN UNA VUELTA POSTERIOR:** el primer barrido de esta vuelta dio
`8` hallazgos, los ocho guiones largos (U+2014) copiados verbatim del propio libro dentro de mis
ficheros de cita (`.gerber_v7/cita_cap18_L137_L166.txt`, `.gerber_v7/cita_cap19_L141_L153.txt`,
`.gerber_v7/cita_cap19_L33_L45.txt`). `fuentes/` es bandeja de entrada y no se barre; mis copias de
evidencia si, porque viven fuera de esa bandeja. Se corrigieron sustituyendo el guion largo por el
guion corto normal en esas tres copias (la palabra no cambia, solo el ancho del trazo), y el barrido
volvio a `VERDE` antes de seguir.

Salida de `python tests/test_aceptacion.py`, guardada en `.gerber_v7/test_aceptacion.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/test_aceptacion.txt -->

    total: 350 pruebas, 0 fallos, 0 errores

**LAS `d103` TRES LINEAS DE `gate` SE SOSTIENEN, EL BARRIDO DE GUIONES QUEDA VERDE TRAS SU CORRECCION
DECLARADA, Y LAS `350` PRUEBAS DE ACEPTACION PASAN, `0` FALLOS.**

### G7.6.e. El tallado y el censo, corridos HOY

Salida de `python scripts/tallar_reporte.py`, guardada en `.gerber_v7/tallado.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/tallado.txt -->

    TALLADO VERDE: las 172 tabla(s) comprobables son las de su instrumento, celda a celda.

**CORRECCION DECLARADA (`D.41`), YA CONTADA EN `G7.3.b` Y `G7.4.c`:** las dos tablas de frontera de esta
vuelta llegaron a un primer commit con la columna *que es* resumida a mano, el hook las marco `DIFIERE`
(`11` celdas en la de `cap_18`, `10` en la de `cap_19`), y las dos se regeneraron con
`python scripts/tallar_reporte.py --arreglar`, nunca tecleando la celda buena.

Salida de `python scripts/censar_rutas.py`, guardada en `.gerber_v7/censo_rutas.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/censo_rutas.txt -->

    CENSO VERDE: las 1085 rutas publicadas sostienen lo que dicen sostener.

**CORRECCION DECLARADA (`D.42`):** la celda de `G7.5.b` que cita mis seis ficheros de evidencia de
fidelidad los nombraba primero como dos PATRONES (`.gerber_v7/cita_cap18_*.txt` y
`.gerber_v7/cita_cap19_*.txt`) en la misma linea; el censo solo reconoce el primer `PATRON:` de cada
unidad y marco el segundo `CAE`. Se corrigio nombrando los seis ficheros por su ruta exacta en vez de
por un patron, y el censo volvio a `VERDE`.

### G7.6.f. La deuda, recomputada al cierre

Salida de `python scripts/deuda.py`, guardada en `.gerber_v7/deuda_cierre.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/deuda_cierre.txt -->

    pendientes: 40    pagadas: 38

**DE `42`/`36` A LA APERTURA DE ESTA TAREA (`G7.1.b`) A `40`/`38` AL CERRAR LA VUELTA: `2` PAGADAS**
(`d117`, `d110`), **`0` NUEVAS CONTRAIDAS por mi.** Coincide al digito con la aritmetica de `G7.1.c` y
`G7.2.d`.

### G7.6.g. Cero averia de dato: nada de `dataset/`, `bitacora/`, `censos/` ni `config/pares_mutuos.jsonl` se movio

    $ git status --porcelain dataset/ bitacora/ censos/ config/pares_mutuos.jsonl
    (sin salida: ningun fichero de esas cuatro sedes aparece modificado)

**`0` FICHEROS DEL GRAFO MOVIDOS.** Esta vuelta no lo toco, tal como manda `MODO_INSERCION=cuarentena`
(`D.39`): los seis candidatos se quedan en `cuarentena/gerber_emyth/` a la espera de que el lote cierre.

### G7.6.h. Las condiciones de parada, repasadas una a una (`EXTRACTOR.md` 7)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| una pregunta de doctrina | ninguna nueva abierta: `d119` (vuelta `6`) sigue registrada y sin tocar, la cola de doctrina se queda en `11` (`D.55`) | **NO ES PARADA** |
| una caida de dato | ninguna: `0` ficheros de `dataset/`, `bitacora/`, `censos/` ni `config/pares_mutuos.jsonl` movidos (`G7.6.g`), gate/guiones/tests/tallado/censo VERDES (`G7.6.d`, `G7.6.e`) | **NO ES PARADA** |
| algo contradice una regla vigente o una cifra publicada con su corte | nada: la discrepancia de `39` contra `42` deuda(s) esperando se declaro en el acto (`G7.1.b`) en vez de resolverse copiando, y las dos tablas de frontera que el hook marco `DIFIERE` se corrigieron regenerando, no tecleando (`G7.6.e`) | **NO ES PARADA** |
| una guarda en rojo | ninguna al cierre: las tres guardas de `EXTRACTOR.md` 6 mas el tallado y el censo, las cinco VERDES tras sus correcciones declaradas | **NO ES PARADA** |
| una operacion cuyo texto no alcance para ejecutarse sin decidir | ninguna: las cinco tareas del encargo traian su orden completo, incluida `d111` con instruccion explicita de medir y no decidir (`TAREA 4`), que es justo lo que `G7.4.e` hizo | **NO ES PARADA** |

**NINGUNA DE LAS CINCO SE CUMPLE. ESTE TURNO CIERRA SIN PARADA**, y `docs/loop/PARA_ALEXIS.md` sigue sin
tocar y no es mio (`EXTRACTOR.md` 14): la declaracion de parada es del auditor, no del extractor.

### G7.6.i. `D.61` repasada contra el reporte entero, credito medido, y lo que propongo

#### G7.6.i.1. `D.61`, la segunda pasada, al cierre

Los dos discutibles de esta vuelta (`G7.3.d`) se marcaron ANTES de escribir sus candidatos y los dos se
ejecutaron o cerraron en el mismo acto: el `1` (`C2`) se ejecuto escribiendo el candidato entero; el `2`
(Hierarchy of Systems) se cerro sin escribir candidato, con su linea citada. **`0` discutibles abiertos
al cierre, por debajo del tope de `2`.** No se abrio ningun discutible en `cap_19` ni en el resto de la
vuelta.

#### G7.6.i.2. Credito: solo se mide, no se anota

Salida de `python forja.py credito`, guardada en `.gerber_v7/credito_cierre.txt`:

<!-- TALLADO: salida=.gerber_v7/credito_cierre.txt -->

    CREDITO DE LA LINEA 'gerber_emyth' (D.48)
      registro: docs/loop/CREDITO_gerber_emyth.jsonl
      tandas: 7, en 27 suceso(s) de especie

      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA G6
      CIFRA PUBLICADA    0 de 2     ACTA G6
      CLASE              0 de 2     ACTA G6
      DATO MOVIDO        0 de 2     ACTA G6
      REPORTE            2 de 3     ACTA G6

      CREDITO ENTERO: ninguna especie en su tope.

**Identica a la de apertura (`G7.1.a`): este registro lo mueve el auditor con `--anotar` al cerrar su
propia acta, no yo (`EXTRACTOR.md` 14 y 15).** No uso `--anotar` en esta vuelta.

#### G7.6.i.3. Lo que propongo al auditor, todo en mi sede y nada adjudicado por mi

1. **La raiz de `d117` fue del auditor y queda corregida en la cabecera de esta misma vuelta**
   (`G7.1.c`), tachada sin borrar, con `python .g6aud/clase_de_vuelta.py` reproducido al digito.
2. **`d110` se paga con el veredicto opuesto al que la vuelta `5` dejo abierto**: leida la continuacion
   de la escena en `cap_18`, el autor SI saca el Operations Manual del caso, y el candidato que lo
   prueba (`construir_estrategia_gente_cuatro_componentes`) nace en `cap_18` (`G7.2`).
3. **`cap_18` y `cap_19` cierran minados, seis candidatos entre los dos, `0 CAERIA` en las seis aduanas,
   `0` PUENTE en los `51` pasos escritos** (`G7.3`, `G7.4`, `G7.5.a`).
4. **La cabeza de serie de `cap_13` (`recorrer_siete_pasos_programa_desarrollo_negocio`) tiene ya sus
   seis pasos alcanzables minados y sigue en `0` de `7`**: ninguno de los seis capitulos produjo un nodo
   que se llame a si mismo el paso entero, todos dieron metodo dentro del paso (`G7.4.e`). Queda medido
   para la vuelta que inserte, sin que yo decida que se hace con ella.
5. **Dos correcciones declaradas de instrumento en esta misma vuelta, las dos regenerando y no
   tecleando**: las dos tablas de frontera que el hook marco `DIFIERE` (`G7.6.e`), y el censo de rutas
   que marco `CAE` un patron mal declarado (`G7.6.e`).
6. **El frente tiene ahora `cap_04` a `cap_19` minados sin hueco** (dieciseis capitulos), mas el
   apartado `cap_17` reservado que no se toca nunca. Quedan `cap_20`, `cap_21` y `cap_22` sin minar.
   `cap_01` a `cap_03` siguen en `d094`, sin tocar por decision del fundador.
7. **La cadencia de saneamiento va `1` de `5` desde la vuelta `6`** (`G7.1.b`): si nada cambia, las
   vueltas `8`, `9` y `10` salen `LIBRE` y la `11` es la siguiente de saneamiento.

#### G7.6.i.4. Cola declarada

Ninguna nueva. `d111` queda medida y no decidida, tal como el encargo lo pide (`G7.4.e`), y no es cola
mia: es la instruccion explicita de la `TAREA 4`.

---

**LA VUELTA 7 CIERRA. CINCO TAREAS CERRADAS (`G7.1` a `G7.5`, CON EL CIERRE EN `G7.6`), CERO PARADA
(`G7.6.h`), CERO INSERCION (`MODO_INSERCION=cuarentena`), DOS CAPITULOS NUEVOS MINADOS (`cap_18`,
`cap_19`), SEIS CANDIDATOS ESCRITOS Y SEIS ADUANAS EN EL ACTO CON `0 CAERIA`, DOS DISCUTIBLES MARCADOS Y
CERRADOS EN EL ACTO (`G7.3.d`), CINCO GUARDAS VERDES (`gate`, `guiones`, `tests`, tallado, censo, tras
sus correcciones declaradas en `G7.6.d` y `G7.6.e`), CERO AVERIA DE DATO (`G7.6.g`), DOS DEUDAS PAGADAS
(`d117`, `d110`), SALDO `40`/`38`.**

## G8.0. EL ESQUELETO DE LA VUELTA (`EXTRACTOR.md` 3)

| # | tarea del encargo | como cierra | donde |
|---:|---|---|---|
| 1 | `TAREA 1`: registros de apertura y correccion declarada de `d123` | **CERRADA**: credito y deuda medidos (`45`/`38`, al digito con la cabecera del encargo), correccion tachada sin borrar, `d123` pagada | `G8.1` |
| 2 | `TAREA 2`: `cap_20`, frontera publicada antes de cortar y candidatos con su aduana en el acto | **CERRADA**: frontera `3` piezas, `1841` palabras al digito, residuo `0`; cero candidatos con su razon (carta sin inventario propio); cero discutibles | `G8.2` |
| 3 | `TAREA 3`: `cap_21`, mismo procedimiento | **CERRADA**: frontera `5` piezas, `1851` palabras al digito, residuo `0`; cero candidatos con su razon (Epilogue sin inventario propio); cero discutibles | `G8.3` |
| 4 | `TAREA 4`: `cap_22`, mismo procedimiento, y el estado del lote `9` declarado con su medida | **CERRADA**: frontera `8` piezas, `904` palabras al digito, residuo `0`; cero candidatos, un discutible cerrado en el acto; lote `9` medido minado entero salvo `d094` | `G8.4` |
| 5 | `TAREA 5`: el cierre, con la tabla de punteros `D.37` que hereda la vuelta que inserte | **CERRADA**: sin poblacion de pasos que medir, muestra de fidelidad con semilla `gerber_v8` sin disparador posible, tabla de punteros `D.37` publicada | `G8.5` |

**CINCO TAREAS ENCARGADAS, EN EL TOPE DE CINCO** (`EXTRACTOR.md` 1.3).

## G8.1. TAREA 1: LOS REGISTROS, Y LA CORRECCION DECLARADA DE `d123`

### G8.1.a. Credito medido al abrir

Salida de `python forja.py credito`, guardada en `.gerber_v8/credito_apertura.txt`:

<!-- TALLADO: salida=.gerber_v8/credito_apertura.txt -->

    CREDITO DE LA LINEA 'gerber_emyth' (D.48)
      registro: docs/loop/CREDITO_gerber_emyth.jsonl
      tandas: 8, en 32 suceso(s) de especie

      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA G7
      CIFRA PUBLICADA    0 de 2     ACTA G7
      CLASE              0 de 2     ACTA G7
      DATO MOVIDO        0 de 2     ACTA G7
      REPORTE            0 de 3     ACTA G7

      CREDITO ENTERO: ninguna especie en su tope.

**`ACTA G7` deja las CINCO rachas en `0`, confirmado por el instrumento corrido hoy.** `REPORTE` bajo de
`2` de `3` a `0` de `3` por la caida del ordinal sin busqueda corrida (`ACTA G7`, seccion "LO QUE SE CAE
ES UN ORDINAL"), y esa caida vive en prosa de acompaniamiento y no acumula (`d122`).

### G8.1.b. Deuda medida al abrir

Salida de `python scripts/deuda.py`, guardada en `.gerber_v8/deuda_apertura.txt`:

<!-- TALLADO: salida=.gerber_v8/deuda_apertura.txt -->

    DEUDA DE LA LINEA (D.55): la deuda no bloquea la produccion
      registro: docs/loop/DEUDA.jsonl
      pendientes: 45    pagadas: 38

Salida de `python scripts/deuda.py --clase 8`, guardada en `.gerber_v8/clase8.txt`:

<!-- TALLADO: salida=.gerber_v8/clase8.txt -->

    LIBRE
      van 2 de 5 desde la ultima de saneamiento (la 6), con 45 deuda(s) esperando

**AL DIGITO CON LA CABECERA DEL ENCARGO (`45` pendientes, `LIBRE`, `van 2 de 5`). Sin discrepancia que
declarar esta vez.**

### G8.1.c. La correccion declarada de `d123`: tachada sin borrar, con su instrumento pegado

`d123` es mia (nacio en mi propia `ACTA G7`, "Y LO QUE CORRIJO ES MIO, NO TUYO"): mi celda de `G7.4.e`
decia del paso `6` de la serie *no se toca nunca (`D.45` de esta vuelta, decision del fundador)*, y
`D.45` no dice eso.

Salida de `grep -n "cap17_reservado" docs/loop/ORDEN_DE_LOTES.md | head -1`, guardada en
`.gerber_v8/cita_orden_lotes_L27.txt`:

<!-- TALLADO: salida=.gerber_v8/cita_orden_lotes_L27.txt -->

    27:| **11** | `gerber_emyth_cap17_reservado` | 1 | 3.845 | **RESERVADO. Entra el ultimo** |

**La correccion queda tachada sin borrar en la propia celda de `G7.4.e`** (arriba en este mismo fichero,
tabla de la seccion que abre con `### G7.4.e. Cuanto queda de d111, medido y sin decidir`): la fila del
paso `6` conserva su texto viejo tachado y anexa, en la misma celda, la cita de `ORDEN_DE_LOTES.md` `L27`
con la regla correcta (lote `11`, `RESERVADO. Entra el ultimo`). **No se regenera por tallado**: es prosa
dentro de una celda de tabla narrativa y no una tabla que `scripts/tallar_reporte.py` reconozca como
generada por un instrumento, tal como el encargo lo distingue (seccion `1`, punto `3`).

**`d123` se paga con esta correccion.** Salida de
`python scripts/deuda.py --pagar d123 --vuelta 8 --como "..."`, guardada en `.gerber_v8/pago_d123.txt`:

<!-- TALLADO: salida=.gerber_v8/pago_d123.txt -->

    PAGADA d123 en la vuelta 8

**Y LAS DOS COSAS QUEDAN HECHAS, EN EL ORDEN QUE EL ENCARGO PIDE:** el rotulo corregido primero, la deuda
pagada despues.

## G8.2. TAREA 2: `cap_20`, `A Letter to Sarah`

### G8.2.a. El borde de arriba, comparado contra `wc -l` (`d109`, la guarda que no lo cubre)

    $ wc -l fuentes/gerber_emyth/cap_20.md
    79 fuentes/gerber_emyth/cap_20.md

**`79` LINEAS, AL DIGITO CON LAS `79` QUE EL ENCARGO CUENTA EN SU CABECERA.**

### G8.2.b. La frontera, publicada antes de cortar

Salida de `python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_20.md .gerber_v8/piezas_cap20.txt`,
guardada en `.gerber_v8/frontera_cap20.txt`:

<!-- TALLADO: salida=.gerber_v8/frontera_cap20.txt -->

    AVISO: cero celdas tecleadas en este instrumento. El arranque del cuerpo NO
    es una constante mia: sale de fuentes/gerber_emyth/cap_20.md, linea 8, que es la siguiente al segundo
    --- de la cabecera yaml (cierres en L1 y L7). El cuerpo va de L8 a L79.

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L20 | **37** | el numero del capitulo, el rotulo A LETTER TO SARAH y el epigrafe de Rollo May (Man's Search for Himself, sobre la libertad que se logra cada dia) | **RESIDUO: rotulo y epigrafe** |
| `R2` | L21 a L59 | **1513** | la carta entera del autor a Sarah: reflexion personal sobre el sentido, el cuidado, el espiritu, el miedo, la Comfort Zone como mascara de seguridad, y el cierre pidiendole que la guarde con su vida y no ceda a la comodidad; cero pasos, cero medio nombrado, cero inventario de etapas u objetos | **POSTURA: carta personal, sin inventario propio** |
| `R3` | L60 a L79 | **291** | ACKNOWLEDGMENTS: los agradecimientos del autor a su esposa, sus hijos, sus asociados de E-Myth Worldwide, sus clientes, su cunada y cunado, su editora en HarperBusiness y sus lectores; gratitud personal, no doctrina ni procedimiento | **RESIDUO: agradecimientos del autor** |
| **el cuerpo entero** | **L8 a L79** | **1841** | **suma de las piezas: 1841** | **residuo sin asignar: 0** |

    piezas: 3   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 1841   suma 1841   residuo 0

**`1841` PALABRAS, AL DIGITO CON LAS `1841` QUE EL ENCARGO CUENTA EN SU CABECERA. `3` PIEZAS, `0` SOLAPES,
`0` LINEAS SIN CUBRIR, RESIDUO `0`.** Fichero completo en `.gerber_v8/piezas_cap20.txt` (D.42).

### G8.2.c. La vara de `9.1`, pasada sobre las tres piezas, y el veredicto: cero candidatos

`R1` es rotulo y epigrafe, no procedimiento. `R3` son agradecimientos personales del autor a personas
nombradas, sin un solo verbo en imperativo dirigido al lector.

`R2`, la carta entera, es el caso que la vara tiene que leer con cuidado: es prosa en segunda persona
dirigida a Sarah, con frases que suenan a instruccion (*guard it with your life*, *keep the curtain up*).
Leida contra la vara madre (seccion `9`: **NOMBRAR NO ES PROCEDIMENTAR**) y su prueba del inventario
(`9.1`, `D.27`): **el capitulo no pone un solo inventario propio de medios, etapas u objetos de trabajo.**
No hay una lista de pasos para "guardar el espiritu con tu vida", no hay una lista de componentes de la
Comfort Zone, no hay una secuencia numerada ni nombrada. Es metafora sostenida (la cortina, el Comfort
Zone, el camino) y reflexion biografica sobre Sarah, no una tecnica desplegable. La frase mas cercana a
un mandato, *keep the curtain up*, es una sola advertencia (manual seccion 4, `P.11`: una advertencia es
linea, no procedimiento), sin los siete pasos que la probarian como procedimiento nombrado en una linea
(seccion `9`).

**VEREDICTO: `cap_20` SE REGISTRA MINADO CON CERO CANDIDATOS.** Es la carta de cierre del libro
(`Cap. 19` en la edicion, "A Letter to Sarah") seguida de los agradecimientos del autor: ninguna de las
dos piezas trae inventario propio que la vara de `9.1` pueda transcribir. **Cero candidatos con su razon
escrita es un resultado, no un hueco** (tal como el encargo lo anticipa en su `TAREA 2`).

### G8.2.d. Discutibles

**Ninguno.** Leidas las tres piezas contra la vara madre y su prueba del inventario, no encuentro un
tramo que compita de cerca con la frontera POSTURA/CANDIDATO: no hay una sola lista o secuencia nombrada
en todo el capitulo. No abro discutible sobre `cap_20`.

## G8.3. TAREA 3: `cap_21`, el `Epilogue`

### G8.3.a. El borde de arriba, comparado contra `wc -l`

    $ wc -l fuentes/gerber_emyth/cap_21.md
    149 fuentes/gerber_emyth/cap_21.md

**`149` LINEAS, AL DIGITO CON LAS `149` QUE EL ENCARGO CUENTA EN SU CABECERA.**

### G8.3.b. La frontera, publicada antes de cortar

Salida de `python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_21.md .gerber_v8/piezas_cap21.txt`,
guardada en `.gerber_v8/frontera_cap21.txt`:

<!-- TALLADO: salida=.gerber_v8/frontera_cap21.txt -->

    AVISO: cero celdas tecleadas en este instrumento. El arranque del cuerpo NO
    es una constante mia: sale de fuentes/gerber_emyth/cap_21.md, linea 8, que es la siguiente al segundo
    --- de la cabecera yaml (cierres en L1 y L7). El cuerpo va de L8 a L149.

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L18 | **56** | el rotulo EPILOGUE, el titulo BRINGING THE DREAM BACK TO AMERICAN SMALL BUSINESS y el epigrafe de Carlos Castaneda (A Separate Reality, sobre el hombre de conocimiento que actua en vez de pensar en actuar) | **RESIDUO: rotulo y epigrafe** |
| `R2` | L19 a L56 | **597** | el llamado a las armas es un llamado a aprender, no a pelear: el mundo cambia mas rapido de lo que las reglas pueden sostenerse, y el caos no esta afuera sino dentro de cada uno; si el mundo va a cambiar, primero tenemos que cambiar nosotros; cero pasos, cero inventario propio | **POSTURA: el caos esta adentro, no afuera** |
| `R3` | L57 a L76 | **405** | Bridging the Gap: el libro entero es sobre tender el puente entre el mundo de afuera y el de adentro, y el propio negocio pequeno puede ser ese puente, como un dojo (citado de Joe Hyams, Zen in the Martial Arts) donde se practica y se aprende de uno mismo; cero pasos, cero inventario propio | **POSTURA: el negocio como dojo** |
| `R4` | L77 a L112 | **506** | A World of Our Own: el Sueno del Small Business Americano es crear un mundo propio, y la mayoria fracasa porque cada quien trae su propio caos consigo; el Business Development Program y el Franchise Prototype son el medio para estudiar ese mundo, e Innovacion, Cuantificacion y Orquestacion (ya desarrolladas en capitulos previos, nombradas aqui sin desarrollo nuevo) son la practica que descubre limites y fuerzas; cero inventario propio nuevo en este tramo | **POSTURA: recapitulacion sin inventario nuevo** |
| `R5` | L113 a L149 | **287** | An Idea for Action: el proverbio chino de oir, ver y hacer para entender; la respuesta es que el modelo si funciona si se aplica con compromiso total, y el cierre pide dejar de pensarlo y empezar a actuar para Traer de Vuelta el Sueno del Small Business Americano; cero pasos, cero inventario propio | **POSTURA: cierre, llamado a actuar sin procedimiento** |
| **el cuerpo entero** | **L8 a L149** | **1851** | **suma de las piezas: 1851** | **residuo sin asignar: 0** |

    piezas: 5   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 1851   suma 1851   residuo 0

**`1851` PALABRAS, AL DIGITO CON LAS `1851` QUE EL ENCARGO CUENTA EN SU CABECERA. `5` PIEZAS, `0`
SOLAPES, `0` LINEAS SIN CUBRIR, RESIDUO `0`.** Fichero completo en `.gerber_v8/piezas_cap21.txt` (D.42).

### G8.3.c. La vara de `9.1`, pasada sobre las cinco piezas, y el veredicto: cero candidatos

`R1` es rotulo y epigrafe. Las otras cuatro son las cuatro secciones nombradas por el propio libro
(sin subtitulo la primera, luego *Bridging the Gap*, *A World of Our Own*, *An Idea for Action*), y las
cuatro son reflexion de cierre, no procedimiento: ninguna trae una lista, una secuencia numerada ni un
inventario de medios, etapas u objetos que la vara `9.1` pueda transcribir.

**EL UNICO TRAMO QUE MERECE LECTURA CONTRA `D.37`:** `R4`, `L105` a `L109`, nombra *Innovation,
Quantification, and Orchestration* dos veces. No es una enumeracion nueva con su propio inventario: es
una recapitulacion de un trio que el libro ya desarrollo en capitulos anteriores del propio dataset
(la Franchise Prototype, minada en capitulos previos de este mismo frente), citado aqui sin desplegar
ningun paso nuevo. `D.37` exige que el texto NOMBRE Y CUENTE sus partes para que la arista cabeza a
parte se cablee; este tramo ni siquiera es la cabeza que las nombra por primera vez, es una mencion de
paso en el epilogo. No abre candidato ni puntero nuevo.

**VEREDICTO: `cap_21` SE REGISTRA MINADO CON CERO CANDIDATOS.** Es el Epilogue del libro, prosa de
cierre en las cuatro voces de la reflexion final (el llamado a las armas que es llamado a aprender, el
negocio como dojo, el mundo propio, la idea para la accion): ninguna trae inventario propio. **Cero
candidatos con su razon escrita.**

### G8.3.d. Discutibles

**Ninguno.** El unico tramo que se acerco a competir (la mencion de Innovation, Quantification and
Orchestration en `R4`) se resuelve sin ambiguedad contra `D.37` (no hay conteo ni desarrollo nuevo, solo
recapitulacion), asi que no lo marco como discutible.

## G8.4. TAREA 4: `cap_22`, el `Afterword`, Y EL LOTE QUE CIERRA

### G8.4.a. El borde de arriba, comparado contra `wc -l`

    $ wc -l fuentes/gerber_emyth/cap_22.md
    129 fuentes/gerber_emyth/cap_22.md

**`129` LINEAS, AL DIGITO CON LAS `129` QUE EL ENCARGO CUENTA EN SU CABECERA.**

### G8.4.b. La frontera, publicada antes de cortar

Salida de `python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_22.md .gerber_v8/piezas_cap22.txt`,
guardada en `.gerber_v8/frontera_cap22.txt`:

<!-- TALLADO: salida=.gerber_v8/frontera_cap22.txt -->

    AVISO: cero celdas tecleadas en este instrumento. El arranque del cuerpo NO
    es una constante mia: sale de fuentes/gerber_emyth/cap_22.md, linea 8, que es la siguiente al segundo
    --- de la cabecera yaml (cierres en L1 y L7). El cuerpo va de L8 a L129.

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L12 | **5** | el rotulo AFTERWORD y el titulo TAKING THE FIRST STEP | **RESIDUO: rotulo** |
| `Ra` | L13 a L18 | **54** | la pregunta de cierre (que haces ahora que el fuego esta encendido) y la afirmacion de que, como Sarah, el lector debe dar el primer paso | **POSTURA: bridge** |
| `Rb` | L19 a L26 | **125** | debes dar un paso atras y mirar tu negocio con tus nuevos ojos E-Myth; debes analizar tu negocio como es hoy, decidir como debe verse cuando este terminado, y determinar la brecha entre donde estas y donde necesitas estar; esa brecha te dira que hace falta hacer, y la brecha siempre nace de la ausencia de sistemas | **DISCUTIBLE: llamado de cierre sin inventario propio de que analizar** |
| `Rc` | L27 a L32 | **125** | desde 1986 E-Myth Worldwide ha ayudado a miles de duenos a dar ese primer paso, invita al lector a la experiencia gratuita E-Myth, y pide completar el formulario al final del libro y seguir las instrucciones provistas alli | **POSTURA: invitacion comercial, remite a un formulario fuera del libro** |
| `Rd` | L33 a L42 | **32** | recuerda el proverbio chino (oir se olvida, ver se recuerda, hacer se entiende) y cierra con Let's get started | **POSTURA: proverbio de cierre** |
| `R3` | L43 a L50 | **10** | la firma: Michael E. Gerber, E-Myth Worldwide, Santa Rosa California, junio 2001 | **RESIDUO: firma** |
| `R4` | L51 a L60 | **225** | ABOUT THE AUTHOR: biografia del autor, su rol en E-Myth Worldwide, y los datos de contacto para invitarlo a hablar o recibir informacion del E-Myth Mastery Program | **RESIDUO: biografia y contacto comercial del autor** |
| `R5` | L61 a L129 | **328** | OTHER WORKS, BACK AD y COPYRIGHT: el listado de otros libros de Michael Gerber con sus ISBN, el aviso legal de copyright de HarperCollins, los datos de edicion, y la publicidad de contraportada de otros titulos (E-Myth Mastery, The E-Myth Physician, The E-Myth Manager, The E-Myth Revisited) con su resena de mercadeo cada uno | **RESIDUO: back matter editorial, ISBN, copyright y publicidad de otros libros** |
| **el cuerpo entero** | **L8 a L129** | **904** | **suma de las piezas: 904** | **residuo sin asignar: 0** |

    piezas: 8   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 904   suma 904   residuo 0

**`904` PALABRAS, AL DIGITO CON LAS `904` QUE EL ENCARGO CUENTA EN SU CABECERA. `8` PIEZAS, `0` SOLAPES,
`0` LINEAS SIN CUBIERTAS, RESIDUO `0`.** Fichero completo en `.gerber_v8/piezas_cap22.txt` (D.42).

### G8.4.c. El unico discutible, marcado ANTES de saber si acierto y cerrado en el mismo acto (tope `2`, `D.61`)

**Discutible `1`: `Rb`, `cap_22` `L19` a `L25`.** Cuatro oraciones en imperativo de segunda persona en
secuencia (*step back*, *analyze*, *decide*, *determine the gap*) que podrian leerse como un
procedimiento de cuatro pasos: dar un paso atras, analizar el negocio como es hoy, decidir como debe
verse terminado, determinar la brecha. Cita, con su `sed` pegado (`D.35`), guardada en
`.gerber_v8/cita_cap22_Rb.txt`:

<!-- TALLADO: salida=.gerber_v8/cita_cap22_Rb.txt -->

    You must step back from your business and look at it through your new E-Myth eyes.
    You must analyze your business as it is today, decide what it must look like when you have finally got it just like you want it, and then determine the gap between where you are and where you need to be in order to make your dream a reality.
    That gap will tell you exactly what needs to be done to create the business of your dreams.
    And what you will discover when you look at your business through your E-Myth eyes is that the gap is always created by the absence of systems, the absence of a proprietary way of doing business that successfully differentiates your business from everyone else's.

**CERRADO, NO EJECUTADO: no escribo candidato.** Leido contra la vara madre (seccion `9`) y la prueba
del inventario (`9.1`, `D.27`): el libro NO nombra uno a uno los medios, etapas u objetos que hay que
revisar en "tu negocio como es hoy". *Look at it through your new E-Myth eyes* y *analyze your business
as it is today* son el adjetivo de adecuacion de la restriccion `2` de `9.1` disfrazado de instruccion
(no dice QUE mirar ni QUE analizar: eso ya lo desplego el libro entero en los capitulos anteriores, con
sus propios candidatos ya minados uno a uno, Primary Aim, Strategic Objective, Organizational Strategy,
People Strategy, Systems Strategy). Sin un inventario propio de este tramo, escribir pasos aqui seria
inventar el detalle que el libro no pone (`15.4`, la relectura de fidelidad): un paso como *revisa tus
Hard Systems, tus Soft Systems y tus Information Systems* no esta en estas cuatro lineas, esta en
`cap_19`, ya minado. **VEREDICTO: `SANO`, no candidato.** Es el resumen motivacional de cierre del libro
entero (la misma voz de *this call to arms is not a call to do battle, it is a call to learning*, pieza
`R2` de `cap_21`), no un procedimiento nuevo. Si el auditor lee lo contrario, la cita queda pegada arriba
para que la relectura ciega la encuentre primero.

**`D.61` REPASADA: UN DISCUTIBLE, CERRADO EN ESTA MISMA VUELTA CON SU MOTIVO Y SU LINEA. `0` ABIERTOS,
POR DEBAJO DEL TOPE DE `2`.**

### G8.4.d. Veredicto de `cap_22`: cero candidatos

`R1`, `R3`, `R4` y `R5` son rotulo, firma, biografia del autor y back matter editorial (ISBN, copyright,
publicidad de otros libros): ninguno trae procedimiento. `Ra` y `Rd` son postura de apertura y cierre
retorico. `Rc` es una invitacion comercial que remite a "el formulario al final de este libro", fuera del
propio texto (el corolario de `9.1`: un paso que cierra un bucle que el libro deja abierto es PUENTE, y
aqui ni siquiera hay paso que escribir, es una remision completa a un formulario ajeno al fichero).
`Rb`, el unico tramo con forma de procedimiento, se cierra `SANO` en `G8.4.c`.

**VEREDICTO: `cap_22` SE REGISTRA MINADO CON CERO CANDIDATOS.** Es el Afterword del libro (llamado a la
accion y remision al formulario de inscripcion) seguido de la biografia del autor y el back matter
editorial completo: ninguna pieza trae inventario propio. **Cero candidatos con su razon escrita.**

### G8.4.e. El estado del lote `9`, declarado con su medida, sin decidir nada

Contado contra `fuentes/gerber_emyth/`:

    $ ls fuentes/gerber_emyth/*.md | wc -l
    22

**`22` UNIDADES EN LA BANDEJA DE ENTRADA.** De ellas, `cap_01` a `cap_03` siguen en `d094` por decision
del fundador y NO se tocan; `cap_04` a `cap_19` ya estaban minados antes de esta vuelta (`16` capitulos,
`ACTA G7` y actas anteriores); `cap_20`, `cap_21` y `cap_22` quedan minados en esta misma vuelta (`G8.2`,
`G8.3`, `G8.4.d`). **QUEDAN `3` UNIDADES DEL LOTE `9` SIN MINAR: `cap_01`, `cap_02` y `cap_03`, LAS TRES
EN `d094`.**

**LOS TRES CAPITULOS DE ESTA VUELTA CUPIERON EN EL TRAMO** (`cap_20` + `cap_21` + `cap_22` = `0`
candidatos, muy por debajo del techo de `30`), **ASI QUE EL LOTE `9` QUEDA MINADO ENTERO SALVO `d094`.**
**ESTO SE DECLARA, NO SE EJECUTA:** la insercion es serial y de ningun frente (`D.45`), y la cosecha del
lote es del fundador. No inserto, no cierro el lote yo: dejo la medida para quien lea este reporte.

## G8.5. TAREA 5: EL CIERRE, Y EL INVENTARIO QUE HEREDA LA VUELTA QUE INSERTE

### G8.5.a. `PASOS INVENTADOS POR CAPITULO`, una fila por capitulo (`AUDITOR_FORJA.md` 8)

Los tres capitulos de esta vuelta cerraron con **cero candidatos** (`G8.2`, `G8.3`, `G8.4.d`), asi que no
hay pasos escritos que medir: no es que la fidelidad haya fallado, es que no hay ficha de la que medirla.

<!-- TALLADO: parcial salida=.gerber_v8/muestra_fidelidad.txt -->

| capitulo | candidatos nuevos (esta vuelta) | pasos escritos | PUENTE | pasos inventados |
|---|---:|---:|---:|---:|
| `cap_20` | `0` | `0` | `0` | **sin poblacion que medir** |
| `cap_21` | `0` | `0` | `0` | **sin poblacion que medir** |
| `cap_22` | `0` | `0` | `0` | **sin poblacion que medir** |
| **el lote entero** | **`0`** | **`0`** | **`0`** | **sin poblacion que medir** |

**`8.2` de `AUDITOR_FORJA.md`: la escalada se decide sobre el peor capitulo, y aqui no hay ninguno que
escale: los tres estan en la misma poblacion vacia.** No es `0,00` por ciento (eso exigiria al menos un
paso escrito contra el cual medir): es ausencia de poblacion, y se declara como tal en vez de
disfrazarla de un cero que no midio nada.

### G8.5.b. La muestra de fidelidad con su semilla escrita (`D.58`, regimen ligero)

Salida de
`python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_20,cap_21,cap_22 --semilla gerber_v8`,
guardada en `.gerber_v8/muestra_fidelidad.txt`:

<!-- TALLADO: salida=.gerber_v8/muestra_fidelidad.txt -->

    MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO (D.58)
      libro    : gerber_emyth
      semilla  : gerber_v8
      capitulos: cap_20, cap_21, cap_22

      RELEIDO ENTERO : cap_21
      POR MUESTRA    : cap_20, cap_22, 15 pasos cada uno

      EL DISPARADOR: si la muestra de un capitulo pasa del 10 por ciento de
      pasos inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.

      --- cap_20: 0 paso(s) en la muestra

      --- cap_22: 0 paso(s) en la muestra

      --- cap_21: ENTERO, 0 paso(s), no hay muestra que elegir

**LA SEMILLA `gerber_v8` REPARTE IGUAL QUE SIEMPRE (`cap_21` ENTERO, `cap_20` y `cap_22` por muestra),
PERO LOS TRES DAN `0` PASOS: NO HAY CANDIDATOS DE LOS QUE MUESTREAR.** El disparador del `10` por ciento
no tiene sobre que dispararse (`0` de `0` no es una fraccion). **NO SE DISPARA NADA, PORQUE NO HAY NADA
QUE DISPARAR.**

### G8.5.c. Los punteros `D.37` que la bandeja deja abiertos, publicados para la vuelta que inserte

**NO LOS DECLARO YO** (`EXTRACTOR.md` `15.6`: esas aristas se declaran en la misma vuelta en que se
INSERTAN las partes, y esta vuelta no inserta, `MODO_INSERCION=cuarentena`). Los tres que ya trae el
encargo, sin tocar:

    d098   D.37, cap_05 L29, la terna sin cabeza
    d104   D.37, cap_12 L21, la terna sin cabeza
    d111   la serie de cap_13: el paso 8 de recorrer_siete_pasos_programa_desarrollo_negocio dice
           "Paso 5: Your People Strategy", que es el titulo de
           construir_estrategia_gente_cuatro_componentes. ARISTA DECLARABLE POR LECTURA.

**Y NINGUN PUNTERO NUEVO NACE DE ESTA VUELTA:** los tres capitulos minados hoy (`cap_20`, `cap_21`,
`cap_22`) cerraron con cero candidatos, asi que no hay hijo nuevo que emparejar con una cabeza de serie.

## G8.6. EL CIERRE

### G8.6.a. La tabla de cierre de la vuelta `8`, pegada PRIMERO

*Remedio de `d030`/`d112`: mi tabla se pega ANTES de correr `--escribir`, para que
`docs/loop/TABLA_DE_CIERRE.txt` traiga MIS filas y no las de la vuelta anterior.*

| # | tarea | como cerro |
|---:|---|---|
| `1` | `TAREA 1`: registros de apertura y correccion declarada de `d123` | **CERRADA en `G8.1`**: credito y deuda medidos (`45`/`38` de apertura, al digito con la cabecera del encargo), correccion tachada sin borrar en la celda de `G7.4.e`, `d123` pagada |
| `2` | `TAREA 2`: `cap_20`, frontera y veredicto | **CERRADA en `G8.2`**: frontera `3` piezas, `1841` palabras al digito, residuo `0`; cero candidatos, capitulo minado por ser una carta sin inventario propio; cero discutibles |
| `3` | `TAREA 3`: `cap_21`, frontera y veredicto | **CERRADA en `G8.3`**: frontera `5` piezas, `1851` palabras al digito, residuo `0`; cero candidatos, capitulo minado, el Epilogue sin inventario propio; cero discutibles |
| `4` | `TAREA 4`: `cap_22`, frontera, veredicto y estado del lote `9` | **CERRADA en `G8.4`**: frontera `8` piezas, `904` palabras al digito, residuo `0`; cero candidatos, un discutible marcado y cerrado en el acto; lote `9` medido minado entero salvo `d094` (`3` de `22` unidades sin minar, las tres reservadas) |
| `5` | `TAREA 5`: el cierre, con los punteros `D.37` para la vuelta que inserte | **CERRADA en `G8.5` y aqui mismo (`G8.6`)**: sin poblacion de pasos que medir (cero candidatos en el lote), muestra de fidelidad corrida con semilla `gerber_v8` sin disparador posible, tabla de punteros `D.37` publicada sin declarar aristas nuevas |

### G8.6.b. El instrumento, corrido DESPUES de pegar la tabla propia

    $ python scripts/tabla_de_cierre.py --escribir

<!-- TALLADO: script=scripts/tabla_de_cierre.py salida=docs/loop/TABLA_DE_CIERRE.txt -->

Salida guardada en `.gerber_v8/tabla_de_cierre_salida.txt`:

<!-- TALLADO: parcial salida=.gerber_v8/tabla_de_cierre_salida.txt -->

    TABLA DE CIERRE DE TAREAS (D.52): toda tabla del reporte declara su instrumento
    filas             : 5
    SIN COMPROBAR  `1` a `5`  ninguna afirmacion de la forma 'N de M del capitulo' con su cap_NN
    TABLA DE CIERRE VERDE: ninguna celda medible difiere del dato.

**LAS CINCO FILAS SALEN `SIN COMPROBAR`, Y ES LO ESPERADO:** ninguna de mis cinco celdas trae la forma
`N de M del capitulo` (el instrumento solo mide esa figura exacta); mis cifras de esta vuelta son de
palabras y piezas de frontera, no de nodos por capitulo, porque los tres capitulos cerraron en cero
candidatos. **`SIN COMPROBAR` no es `DIFIERE`: es una fila que el instrumento no sabe medir y copia tal
cual, sin inventar** (la propia doctrina del script, citada en `G8.6.a`).

### G8.6.c. Comprobacion: el fichero trae MIS filas, no las de otra vuelta

    $ cat docs/loop/TABLA_DE_CIERRE.txt

Salida guardada en `.gerber_v8/tabla_de_cierre_cat.txt`:

<!-- TALLADO: salida=.gerber_v8/tabla_de_cierre_cat.txt -->

    $ python scripts/tabla_de_cierre.py --escribir
    poblacion: dataset/nodos.jsonl entero, libro gerber_emyth
    criterio : un nodo sale de un capitulo si cita gerber_emyth/<cap>.md

    | # | tarea | como cerro |
    |---:|---|---|
    | `1` | `TAREA 1`: registros de apertura y correccion declarada de `d123` | **CERRADA en `G8.1`**: credito y deuda medidos (`45`/`38` de apertura, al digito con la cabecera del encargo), correccion tachada sin borrar en la celda de `G7.4.e`, `d123` pagada |
    | `2` | `TAREA 2`: `cap_20`, frontera y veredicto | **CERRADA en `G8.2`**: frontera `3` piezas, `1841` palabras al digito, residuo `0`; cero candidatos, capitulo minado por ser una carta sin inventario propio; cero discutibles |
    | `3` | `TAREA 3`: `cap_21`, frontera y veredicto | **CERRADA en `G8.3`**: frontera `5` piezas, `1851` palabras al digito, residuo `0`; cero candidatos, capitulo minado, el Epilogue sin inventario propio; cero discutibles |
    | `4` | `TAREA 4`: `cap_22`, frontera, veredicto y estado del lote `9` | **CERRADA en `G8.4`**: frontera `8` piezas, `904` palabras al digito, residuo `0`; cero candidatos, un discutible marcado y cerrado en el acto; lote `9` medido minado entero salvo `d094` (`3` de `22` unidades sin minar, las tres reservadas) |
    | `5` | `TAREA 5`: el cierre, con los punteros `D.37` para la vuelta que inserte | **CERRADA en `G8.5` y aqui mismo (`G8.6`)**: sin poblacion de pasos que medir (cero candidatos en el lote), muestra de fidelidad corrida con semilla `gerber_v8` sin disparador posible, tabla de punteros `D.37` publicada sin declarar aristas nuevas |

**LAS CINCO FILAS SON LAS MIAS, DE ESTA VUELTA `8`.** No hay arrastre de la tabla de la vuelta `7`.

### G8.6.d. Las tres guardas de la vuelta, corridas HOY, con su salida

Salida de `python forja.py gate`, guardada en `.gerber_v8/gate.txt`:

<!-- TALLADO: salida=.gerber_v8/gate.txt -->

    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

**`346` NODOS: EL MISMO NUMERO DE LA APERTURA, PORQUE ESTA VUELTA NO INSERTA (`MODO_INSERCION=cuarentena`,
`D.39`).** `d103` sostenida: las tres lineas de siempre.

Salida de `python forja.py guiones`, guardada en `.gerber_v8/guiones.txt`:

<!-- TALLADO: salida=.gerber_v8/guiones.txt -->

    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

**VERDE AL PRIMER INTENTO, SIN CORRECCION QUE DECLARAR ESTA VEZ** (a diferencia de la vuelta `7`, que
tuvo que corregir ocho guiones largos copiados de sus citas): esta vuelta no copia bloques largos de
prosa del libro en las citas de evidencia (los tramos citados con `sed` son frases cortas), y `d124`
sigue como cola sin nuevo ejemplar.

Salida de `python tests/test_aceptacion.py`, guardada en `.gerber_v8/test_aceptacion.txt`:

<!-- TALLADO: parcial salida=.gerber_v8/test_aceptacion.txt -->

    total: 350 pruebas, 0 fallos, 0 errores

**LAS TRES GUARDAS VERDES: GATE, GUIONES Y ACEPTACION, LAS `350` PRUEBAS EN VERDE, `0` FALLOS.**

### G8.6.e. El tallado y el censo, corridos HOY

Salida de `python scripts/tallar_reporte.py`, guardada en `.gerber_v8/tallado.txt`:

<!-- TALLADO: parcial salida=.gerber_v8/tallado.txt -->

    TALLADO VERDE: las 176 tabla(s) comprobables son las de su instrumento, celda a celda.

Salida de `python scripts/censar_rutas.py`, guardada en `.gerber_v8/censo_rutas.txt`:

<!-- TALLADO: parcial salida=.gerber_v8/censo_rutas.txt -->

    CENSO VERDE: las 1123 rutas publicadas sostienen lo que dicen sostener.

**LOS DOS VERDES AL PRIMER INTENTO, SIN CORRECCION QUE DECLARAR ESTA VEZ** (a diferencia de la vuelta
`7`, que tuvo que regenerar dos tablas de frontera y corregir un patron de censo mal declarado): las
tres tablas de frontera de esta vuelta (`cap_20`, `cap_21`, `cap_22`) se pegaron desde el instrumento
sin resumir a mano, y cada ruta de evidencia se cito por su ruta exacta, no por patron compartido.

### G8.6.f. La deuda, recomputada al cierre

Salida de `python scripts/deuda.py`, guardada en `.gerber_v8/deuda_cierre.txt`:

<!-- TALLADO: parcial salida=.gerber_v8/deuda_cierre.txt -->

    pendientes: 44    pagadas: 39

**DE `45`/`38` A LA APERTURA (`G8.1.b`) A `44`/`39` AL CERRAR LA VUELTA: `1` PAGADA** (`d123`), **`0`
NUEVAS CONTRAIDAS por mi.** Coincide al digito con la aritmetica de `G8.1.c`.

### G8.6.g. Cero averia de dato: nada de `dataset/`, `bitacora/`, `censos/` ni `config/pares_mutuos.jsonl` se movio

    $ git status --porcelain dataset/ bitacora/ censos/ config/pares_mutuos.jsonl
    (sin salida: ningun fichero de esas cuatro sedes aparece modificado)

**`0` FICHEROS DEL GRAFO MOVIDOS.** Esta vuelta no lo toco, tal como manda `MODO_INSERCION=cuarentena`
(`D.39`): los tres capitulos cerraron con cero candidatos, asi que ni siquiera hay JSON nuevo que sumar
a `cuarentena/gerber_emyth/` (sigue en los `22` ficheros ya escritos en vueltas anteriores).

### G8.6.h. Las condiciones de parada, repasadas una a una (`EXTRACTOR.md` 7)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| una pregunta de doctrina | ninguna nueva abierta: la cola de doctrina se queda en `11` (`D.55`), sin tocar | **NO ES PARADA** |
| una caida de dato | ninguna: `0` ficheros de `dataset/`, `bitacora/`, `censos/` ni `config/pares_mutuos.jsonl` movidos (`G8.6.g`), gate/guiones/tests/tallado/censo VERDES (`G8.6.d`, `G8.6.e`) | **NO ES PARADA** |
| algo contradice una regla vigente o una cifra publicada con su corte | nada: la correccion de `d123` se tachó sin borrar en vez de reescribirse por encima (`G8.1.c`), y el unico discutible se cerro con su cita y su motivo (`G8.4.c`) | **NO ES PARADA** |
| una guarda en rojo | ninguna al cierre: las tres guardas de `EXTRACTOR.md` 6 mas el tallado y el censo, las cinco VERDES sin correccion que declarar esta vez | **NO ES PARADA** |
| una operacion cuyo texto no alcance para ejecutarse sin decidir | ninguna: las cinco tareas del encargo traian su orden completo, incluida la `TAREA 4` con instruccion explicita de declarar el estado del lote sin ejecutarlo, que es justo lo que `G8.4.e` hizo | **NO ES PARADA** |

**NINGUNA DE LAS CINCO SE CUMPLE. ESTE TURNO CIERRA SIN PARADA**, y `docs/loop/PARA_ALEXIS.md` sigue sin
tocar y no es mio (`EXTRACTOR.md` 14): la declaracion de parada es del auditor, no del extractor.

### G8.6.i. `D.61` repasada contra el reporte entero, credito medido, y lo que propongo

#### G8.6.i.1. `D.61`, la segunda pasada, al cierre

El unico discutible de esta vuelta (`G8.4.c`, la pieza `Rb` de `cap_22`) se marco ANTES de escribir el
veredicto y se cerro en el mismo acto, sin candidato: `SANO`, con su cita pegada. **`0` discutibles
abiertos al cierre, por debajo del tope de `2`.** No se abrio ningun discutible en `cap_20` ni en
`cap_21`.

#### G8.6.i.2. Credito: solo se mide, no se anota

Salida de `python forja.py credito`, guardada en `.gerber_v8/credito_cierre.txt`:

<!-- TALLADO: salida=.gerber_v8/credito_cierre.txt -->

    CREDITO DE LA LINEA 'gerber_emyth' (D.48)
      registro: docs/loop/CREDITO_gerber_emyth.jsonl
      tandas: 8, en 32 suceso(s) de especie

      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA G7
      CIFRA PUBLICADA    0 de 2     ACTA G7
      CLASE              0 de 2     ACTA G7
      DATO MOVIDO        0 de 2     ACTA G7
      REPORTE            0 de 3     ACTA G7

      CREDITO ENTERO: ninguna especie en su tope.

**Identica a la de apertura (`G8.1.a`): este registro lo mueve el auditor con `--anotar` al cerrar su
propia acta, no yo (`EXTRACTOR.md` 14 y 15).** No uso `--anotar` en esta vuelta.

#### G8.6.i.3. Lo que propongo al auditor, todo en mi sede y nada adjudicado por mi

1. **La raiz de `d123` fue mia (nacio en mi propia `ACTA G7`, seccion "Y LO QUE CORRIJO ES MIO, NO
   TUYO") y queda corregida en la celda de `G7.4.e`**, tachada sin borrar, con `ORDEN_DE_LOTES.md` `L27`
   citado al lado (`G8.1.c`).
2. **`cap_20`, `cap_21` y `cap_22` cierran minados los tres, con CERO CANDIDATOS y su razon escrita en
   cada uno** (`G8.2`, `G8.3`, `G8.4.d`): son la carta de cierre a Sarah, el Epilogue y el Afterword mas
   el back matter editorial, y ninguno trae inventario propio de medios, etapas u objetos bajo la vara
   de `9.1`.
3. **El lote `9` queda medido minado entero salvo `d094`**: de las `22` unidades de
   `fuentes/gerber_emyth/`, solo `cap_01` a `cap_03` siguen sin minar, apartadas por decision del
   fundador (`G8.4.e`). **Esto se declara, no se ejecuta**: la cosecha del lote es del fundador y la
   insercion es serial (`D.45`).
4. **Un solo discutible en toda la vuelta, cerrado en el acto sin candidato**: la pieza `Rb` de `cap_22`
   (`L19` a `L26`, el llamado a "dar el primer paso" y "determinar la brecha"), leida como el adjetivo de
   adecuacion de `9.1` disfrazado de instruccion, sin inventario propio nuevo (`G8.4.c`).
5. **Cero correcciones declaradas de instrumento esta vuelta**: las tres tablas de frontera se pegaron
   directamente del instrumento, sin resumen a mano, y el tallado y el censo salieron VERDES al primer
   intento (`G8.6.e`), a diferencia de la vuelta `7`.
6. **El frente tiene ahora `cap_04` a `cap_22` minados sin hueco** (diecinueve capitulos), mas el
   apartado `cap17_reservado` que entra el ultimo (lote `11`, `ORDEN_DE_LOTES.md` `L27`). Solo quedan
   `cap_01` a `cap_03` sin minar, en `d094`, sin tocar por decision del fundador.
7. **La cadencia de saneamiento sigue en `2` de `5` desde la vuelta `6`** (`G8.1.b`): si nada cambia, las
   vueltas `9` y `10` salen `LIBRE` y la `11` es la siguiente de saneamiento, tal como el propio encargo
   ya lo anticipa en su seccion `1`.

#### G8.6.i.4. Cola declarada

Ninguna nueva. `d098`, `d104` y `d111` siguen publicados para la vuelta que inserte (`G8.5.c`), sin que
yo decida nada sobre ellos.

---

**LA VUELTA 8 CIERRA. CINCO TAREAS CERRADAS (`G8.1` A `G8.5`, CON EL CIERRE EN `G8.6`), CERO PARADA
(`G8.6.h`), CERO INSERCION (`MODO_INSERCION=cuarentena`), TRES CAPITULOS NUEVOS MINADOS (`cap_20`,
`cap_21`, `cap_22`), CERO CANDIDATOS ESCRITOS EN LOS TRES CON SU RAZON CADA UNO, UN DISCUTIBLE MARCADO Y
CERRADO EN EL ACTO (`G8.4.c`), CINCO GUARDAS VERDES (`gate`, `guiones`, `tests`, tallado, censo, SIN
CORRECCION ESTA VEZ), CERO AVERIA DE DATO (`G8.6.g`), UNA DEUDA PAGADA (`d123`), SALDO `44`/`39`, Y EL
LOTE `9` MEDIDO MINADO ENTERO SALVO `d094`.**

# FRENTE `gerber_emyth`, VUELTA 9: **LA ULTIMA. `cap_01`, `cap_02` Y `cap_03`, Y EL LIBRO QUEDA ENTERO** (`D.58`, frente en paralelo: **NO INSERTA**)

## G9.0. EL ESQUELETO DE LA VUELTA (`EXTRACTOR.md` 3)

| # | tarea del encargo | como cierra | donde |
|---:|---|---|---|
| 1 | `TAREA 1`: registros de apertura | **CERRADA**: credito y deuda medidos, deuda subida a `49`/`39` desde la `44`/`39` del cierre de `G8` (`5` deudas nuevas de `ACTA G8`, ajenas a mi) | `G9.1` |
| 2 | `cap_01`, `Foreword`: frontera y veredicto | **CERRADA**: frontera `3` piezas, `1402` palabras de cuerpo (`1434` con la cabecera yaml, al digito con `wc -w`), residuo `0`; cero candidatos, prefacio personal sin inventario propio; cero discutibles | `G9.2` |
| 3 | `cap_02`, `Introduction`: frontera y veredicto | **CERRADA**: frontera `4` piezas, `1212` palabras de cuerpo (`1244` con la cabecera yaml), residuo `0`; cero candidatos, las cuatro ideas del libro nombradas como metas sin inventario de medios; cero discutibles | `G9.3` |
| 4 | `cap_03`, `Cap. 1, The Entrepreneurial Myth`: frontera y veredicto, `PASOS INVENTADOS` y muestra de fidelidad | **CERRADA**: frontera `5` piezas, `2202` palabras de cuerpo (`2237` con la cabecera yaml), residuo `0`; cero candidatos, diagnostico narrativo del mito y del caso de Sarah sin inventario propio; cero discutibles; muestra de fidelidad con semilla `g9` sin poblacion que medir | `G9.4` |
| 5 | `TAREA 2`: cerrar `d094` y publicar la frontera del libro entero, `cap_01` a `cap_22` | **CERRADA**: `d094` pagada citando esta vuelta; tabla del libro entero publicada, `22` de `22` unidades minadas, `22` candidatos en bandeja; los cuatro punteros heredados (`d098`, `d104`, `d108`, `d111`) comprobados, ninguno tocado por estos tres capitulos | `G9.5` |

**CINCO TAREAS ENCARGADAS, EN EL TOPE DE CINCO** (`EXTRACTOR.md` 1.3): las tres del punto `1` del encargo mas la `TAREA 2` de su punto `2`, mas el registro de apertura que abre el reporte antes de la primera (`EXTRACTOR.md` 3).

## G9.1. TAREA 1: LOS REGISTROS DE APERTURA

### G9.1.a. Credito medido al abrir

Salida de `python forja.py credito`, guardada en `.gerber_v9/credito_apertura.txt`:

<!-- TALLADO: salida=.gerber_v9/credito_apertura.txt -->

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

**LAS CINCO ESPECIES SIGUEN EN `0`, TAL COMO `ACTA G8` LAS DEJO.** Esta es, tal como el
encargo lo dice en su seccion `6`, la ultima oportunidad de esta linea de dejarlas asi: no
las toco yo (`G9.6.i` mide el cierre), pero las cinco parten en `0`.

### G9.1.b. Deuda medida al abrir

Salida de `python scripts/deuda.py`, guardada en `.gerber_v9/deuda_apertura.txt`:

<!-- TALLADO: salida=.gerber_v9/deuda_apertura.txt -->

    DEUDA DE LA LINEA (D.55): la deuda no bloquea la produccion
      registro: docs/loop/DEUDA.jsonl
      pendientes: 49    pagadas: 39

Salida de `python scripts/deuda.py --clase 9`, guardada en `.gerber_v9/clase9.txt`:

<!-- TALLADO: salida=.gerber_v9/clase9.txt -->

    LIBRE
      van 3 de 5 desde la ultima de saneamiento (la 6), con 49 deuda(s) esperando

**`49` PENDIENTES, NO LAS `44` CON LAS QUE CERRO `G8`.** La diferencia es `5` deuda(s)
nuevas: `d128` a `d132`, las cinco anotadas en la vuelta `8` con cita `ACTA G8` (visibles en
la propia salida de `deuda.py` de esta vuelta), ajenas a este reporte. **Sin discrepancia
que declarar**: el instrumento manda y la cifra de hoy no es la de `G8.6.f` porque algo se
movio entre medias, no porque yo la mida distinto.

## G9.2. `cap_01`, `Foreword`

### G9.2.a. El borde de arriba, comparado contra `wc -l` y `wc -w` (`d109`, la guarda que no lo cubre)

    $ wc -l fuentes/gerber_emyth/cap_01.md
    71 fuentes/gerber_emyth/cap_01.md
    $ wc -w fuentes/gerber_emyth/cap_01.md
    1434 fuentes/gerber_emyth/cap_01.md

**`71` LINEAS, AL DIGITO CON EL BORDE DE LA ULTIMA PIEZA DE LA FRONTERA (abajo). `1434`
PALABRAS DEL FICHERO ENTERO, AL DIGITO CON LAS `1434` QUE EL ENCARGO CUENTA EN SU CABECERA.**

### G9.2.b. La frontera, publicada antes de cortar

Salida de `python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_01.md .gerber_v9/piezas_cap01.txt`,
guardada en `.gerber_v9/frontera_cap01.txt`:

<!-- TALLADO: salida=.gerber_v9/frontera_cap01.txt -->

    AVISO: cero celdas tecleadas en este instrumento. El arranque del cuerpo NO
    es una constante mia: sale de fuentes/gerber_emyth/cap_01.md, linea 8, que es la siguiente al segundo
    --- de la cabecera yaml (cierres en L1 y L7). El cuerpo va de L8 a L71.

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L10 | **1** | el rotulo FOREWORD | **RESIDUO: rotulo** |
| `R2` | L11 a L66 | **1393** | el prefacio del autor a la edicion revisada: quince anios desde The E-Myth original, su vida personal (familia, matrimonio, nietos), la pregunta de que saben los duenos de negocios extraordinarios, la insistencia en la atencion a los detalles pequenos hechos exactamente bien, y la presentacion de Sarah como interlocutora del libro; cero pasos, cero medio nombrado, cero inventario de etapas u objetos | **POSTURA: prefacio personal, sin inventario propio** |
| `R3` | L67 a L71 | **8** | la firma: Michael E. Gerber, Santa Rosa California, junio 2001 | **RESIDUO: firma** |
| **el cuerpo entero** | **L8 a L71** | **1402** | **suma de las piezas: 1402** | **residuo sin asignar: 0** |

    piezas: 3   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 1402   suma 1402   residuo 0

**`1402` PALABRAS DE CUERPO (sin la cabecera yaml, que trae `32` palabras propias: `1402` +
`32` = `1434`, al digito con `wc -w` del fichero entero). `3` PIEZAS, `0` SOLAPES, `0`
LINEAS SIN CUBRIR, RESIDUO `0`.** Fichero completo en `.gerber_v9/piezas_cap01.txt` (D.42).

### G9.2.c. La vara de `9.1`, pasada sobre las tres piezas, y el veredicto: cero candidatos

`R1` es rotulo, `R3` es firma: ninguna trae procedimiento. `R2`, el prefacio entero, es la
pieza que la vara tiene que leer con cuidado: quince anios de vida personal del autor (su
familia, sus nietos, sus viajes), la pregunta retorica de que saben los duenos de negocios
extraordinarios, y la tesis de que las cosas pequenas hechas exactamente bien son lo que
distingue un negocio grande. Leida contra la vara madre (seccion `9`: **NOMBRAR NO ES
PROCEDIMENTAR**) y su prueba del inventario (`9.1`, `D.27`): **el prefacio no pone un solo
inventario propio de medios, etapas u objetos de trabajo.** No hay una lista de que
atender, no hay una secuencia de pasos, no hay un conjunto de cosas por revisar: es memoria
y reflexion, cerrando con la presentacion de Sarah como la interlocutora del libro que
vendra despues.

**VEREDICTO: `cap_01` SE REGISTRA MINADO CON CERO CANDIDATOS.** Es el Foreword de la
edicion revisada: prefacio personal del autor, sin inventario propio que la vara de `9.1`
pueda transcribir. **Cero candidatos con su razon escrita es un resultado, no un hueco**
(tal como el encargo lo anticipa en su seccion `1.a`).

### G9.2.d. Discutibles

**Ninguno.** Leida la unica pieza con forma de cuerpo (`R2`) contra la vara madre y su
prueba del inventario, no hay una sola lista o secuencia nombrada en todo el capitulo: es
memoria en primera persona sin un solo verbo en imperativo dirigido al lector. No abro
discutible sobre `cap_01`.

## G9.3. `cap_02`, `Introduction`

### G9.3.a. El borde de arriba, comparado contra `wc -l` y `wc -w`

    $ wc -l fuentes/gerber_emyth/cap_02.md
    99 fuentes/gerber_emyth/cap_02.md
    $ wc -w fuentes/gerber_emyth/cap_02.md
    1244 fuentes/gerber_emyth/cap_02.md

**`99` LINEAS, AL DIGITO CON EL BORDE DE LA ULTIMA PIEZA DE LA FRONTERA. `1244` PALABRAS DEL
FICHERO ENTERO, AL DIGITO CON LAS `1244` QUE EL ENCARGO CUENTA EN SU CABECERA.**

### G9.3.b. La frontera, publicada antes de cortar

Salida de `python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_02.md .gerber_v9/piezas_cap02.txt`,
guardada en `.gerber_v9/frontera_cap02.txt`:

<!-- TALLADO: salida=.gerber_v9/frontera_cap02.txt -->

    AVISO: cero celdas tecleadas en este instrumento. El arranque del cuerpo NO
    es una constante mia: sale de fuentes/gerber_emyth/cap_02.md, linea 8, que es la siguiente al segundo
    --- de la cabecera yaml (cierres en L1 y L7). El cuerpo va de L8 a L99.

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L10 | **1** | el rotulo INTRODUCTION | **RESIDUO: rotulo** |
| `R2` | L11 a L16 | **17** | el epigrafe de Joseph Heller (Something Happened), sobre alguien enloqueciendo despacio dentro de todo negocio | **RESIDUO: epigrafe** |
| `R3` | L17 a L94 | **1183** | la introduccion del libro: la estadistica de fracaso de los pequenos negocios en Estados Unidos, el anuncio de las cuatro ideas del libro (Idea 1 el E-Myth, Idea 2 la Turn-Key Revolution, Idea 3 el Business Development Process, Idea 4 su aplicacion sistematica), y la tesis de que el negocio es un reflejo de quien es su dueno; las cuatro ideas se nombran como el CONTENIDO del libro entero, no como pasos que el lector ejecute aqui, y no traen inventario propio de medios, etapas u objetos de trabajo en este tramo | **POSTURA: anuncio tematico del libro, metas nombradas sin inventario de medios** |
| `R4` | L95 a L99 | **11** | el separador PART I, The E-Myth and American Small Business | **RESIDUO: separador de parte** |
| **el cuerpo entero** | **L8 a L99** | **1212** | **suma de las piezas: 1212** | **residuo sin asignar: 0** |

    piezas: 4   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 1212   suma 1212   residuo 0

**`1212` PALABRAS DE CUERPO (mas `32` de la cabecera yaml: `1212` + `32` = `1244`, al digito
con `wc -w` del fichero entero). `4` PIEZAS, `0` SOLAPES, `0` LINEAS SIN CUBRIR, RESIDUO
`0`.** Fichero completo en `.gerber_v9/piezas_cap02.txt` (D.42).

### G9.3.c. La vara de `9.1`, pasada sobre las cuatro piezas, y el veredicto: cero candidatos

`R1` es rotulo, `R2` es epigrafe, `R4` es separador de parte: ninguna trae procedimiento.

`R3` es el tramo que compite: anuncia las **cuatro ideas** del libro, cada una con su
propio parrafo (`IDEA #1` a `IDEA #4`). Comprobado contra `D.37` (la serie que el titulo
enumera se cablea en la misma vuelta en que nace su cabeza): **las cuatro ideas no son un
inventario de medios, etapas u objetos de trabajo, son las CUATRO TESIS del libro entero**
(que existe el mito del emprendedor, que hay una revolucion Turn-Key en marcha, que el
Business Development Process es su motor, y que ese proceso se aplica de forma
sistematica). Es la restriccion `1` de `9.1` al digito: **un inventario de METAS o de FINES
no cuenta, nombrar adonde hay que llegar sigue siendo nombrar.** Las cuatro ideas anuncian
DE QUE va el libro, no COMO se ejecuta nada aqui; su despliegue en procedimiento (Primary
Aim, Strategic Objective, Organizational Strategy, People Strategy, Systems Strategy, y los
capitulos de Innovacion, Cuantificacion y Orquestacion) ya vive, capitulo a capitulo, en los
candidatos minados de `cap_04` en adelante. Declarar aqui una cabeza de serie con estas
cuatro ideas fabricaria una cabeza que el propio libro no usa como tal: no hay una unica
lectura donde una IDEA se corresponda uno a uno con una PARTE nombrada por su numero (a
diferencia de `d098` y `d104`, donde el libro nombra tres o tres fases EXACTAS que luego
son un capitulo cada una). **No abre puntero `D.37` nuevo.**

**VEREDICTO: `cap_02` SE REGISTRA MINADO CON CERO CANDIDATOS.** Es la Introduction del
libro: la estadistica de fracaso, el anuncio de las cuatro ideas rectoras y la tesis del
negocio como reflejo del dueno, ninguna con inventario propio bajo `9.1`. **Cero candidatos
con su razon escrita.**

### G9.3.d. Discutibles

**Ninguno.** El unico tramo que podria competir (las cuatro ideas de `R3`) se resuelve sin
ambiguedad contra la restriccion `1` de `9.1`: son metas y fines del libro entero, no un
inventario de medios que el lector ejecute en este tramo. No abro discutible sobre `cap_02`.

## G9.4. `cap_03`, `Cap. 1`, `The Entrepreneurial Myth`

### G9.4.a. El borde de arriba, comparado contra `wc -l` y `wc -w`

    $ wc -l fuentes/gerber_emyth/cap_03.md
    233 fuentes/gerber_emyth/cap_03.md
    $ wc -w fuentes/gerber_emyth/cap_03.md
    2237 fuentes/gerber_emyth/cap_03.md

**`233` LINEAS, AL DIGITO CON EL BORDE DE LA ULTIMA PIEZA DE LA FRONTERA. `2237` PALABRAS
DEL FICHERO ENTERO, AL DIGITO CON LAS `2237` QUE EL ENCARGO CUENTA EN SU CABECERA.**

### G9.4.b. La frontera, publicada antes de cortar

Salida de `python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_03.md .gerber_v9/piezas_cap03.txt`,
guardada en `.gerber_v9/frontera_cap03.txt`:

<!-- TALLADO: salida=.gerber_v9/frontera_cap03.txt -->

    AVISO: cero celdas tecleadas en este instrumento. El arranque del cuerpo NO
    es una constante mia: sale de fuentes/gerber_emyth/cap_03.md, linea 8, que es la siguiente al segundo
    --- de la cabecera yaml (cierres en L1 y L7). El cuerpo va de L8 a L233.

| pieza | lineas | palabras | que es | clase |
|---|---|---:|---|---|
| `R1` | L8 a L18 | **22** | el numero del capitulo, el separador, el titulo THE ENTREPRENEURIAL MYTH y el epigrafe de Aldous Huxley sobre embriagarse de trabajo para no verse como se es | **RESIDUO: rotulo y epigrafe** |
| `R2` | L19 a L60 | **332** | el mito del emprendedor: la imagen heroica del emprendedor, y como en la experiencia del autor esa persona real casi nunca se sostiene, sino que el emprendedor solo existio un instante fugaz y luego desaparecio, dejando una mala interpretacion de quien empieza negocios y por que; cero pasos, cero inventario propio | **POSTURA: diagnostico del mito, sin inventario propio** |
| `R3` | L61 a L102 | **400** | The Entrepreneurial Seizure: describe, en segunda persona, el momento en que un tecnico que trabaja para otro sufre un ataque de fiebre emprendedora y decide independizarse; es narracion de un proceso psicologico que le ocurre al lector, no una lista de pasos que el lector ejecute ni un inventario de medios, etapas u objetos de trabajo | **POSTURA: narracion del ataque emprendedor, sin inventario propio** |
| `R4` | L103 a L150 | **387** | The Fatal Assumption: expone la Fatal Assumption (creer que saber el trabajo tecnico de un negocio es saber dirigir un negocio que hace ese trabajo) y enumera oficios (carpintero, barbero, redactor tecnico, peluquera, ingeniero, musico) que se convierten en negocios bajo esa falacia; los oficios listados son EJEMPLOS del diagnostico, no un inventario de medios o etapas de un procedimiento que el lector ejecute | **POSTURA: diagnostico de la Fatal Assumption, ejemplos sin procedimiento** |
| `R5` | L151 a L233 | **1061** | la historia de Sarah y su negocio All About Pies: el relato de su jornada de tres de la manana a las nueve o diez de la noche, su llanto, el origen de su amor por hornear con su tia, y el cierre en que el autor le dice que es hora de aprender todo sobre pies otra vez; en L225 nombra cuatro etapas (exhilaration, terror, exhaustion, despair) que todo tecnico con Entrepreneurial Seizure experimenta, pero son etapas de una experiencia psicologica narrada en tercera persona, no medios, etapas u objetos de trabajo que el lector deba revisar o ejecutar; cero inventario propio procedimental | **POSTURA: caso narrado de Sarah, con etapas de experiencia y no de procedimiento** |
| **el cuerpo entero** | **L8 a L233** | **2202** | **suma de las piezas: 2202** | **residuo sin asignar: 0** |

    piezas: 5   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 2202   suma 2202   residuo 0

**`2202` PALABRAS DE CUERPO (mas `35` de la cabecera yaml: `2202` + `35` = `2237`, al digito
con `wc -w` del fichero entero). `5` PIEZAS, `0` SOLAPES, `0` LINEAS SIN CUBRIR, RESIDUO
`0`.** Fichero completo en `.gerber_v9/piezas_cap03.txt` (D.42).

### G9.4.c. La vara de `9.1`, pasada sobre las cinco piezas, y el veredicto: cero candidatos

`R1` es rotulo y epigrafe. `R2` (el mito), `R3` (la Entrepreneurial Seizure) y `R4` (la
Fatal Assumption) son diagnostico en segunda y tercera persona: describen algo que le
OCURRE al lector o a los tecnicos en general (un ataque, una asuncion fatal), no una lista
de medios, etapas u objetos de trabajo que el lector deba revisar o ejecutar. Los seis
oficios de `R4` (carpintero, barbero, redactor tecnico, peluquera, ingeniero, musico) son
EJEMPLOS del diagnostico ilustrando la misma falacia, no un inventario de pasos.

`R5`, la historia de Sarah, es el tramo que merece la lectura mas cuidadosa: es narrativa
de caso (manual seccion `3.5`, "el caso no es la casa"), y trae en `L225` la frase **"First,
exhilaration; second, terror; third, exhaustion; and, finally, despair"**. Cita, con su
`sed` pegado (`D.35`), guardada en `.gerber_v9/cita_cap03_L225.txt`:

<!-- TALLADO: salida=.gerber_v9/cita_cap03_L225.txt -->

    225:First, exhilaration; second, terror; third, exhaustion; and, finally, despair. A terrible sense of loss-not only the loss of what was closest to them, their special relationship with their work, but the loss of purpose, the loss of self.

Leida contra la vara madre (seccion `9`) y la prueba del inventario (`9.1`, `D.27`): estas
cuatro palabras nombran **etapas de una experiencia psicologica que el tecnico sufre**
("every technician suffering from an Entrepreneurial Seizure experiences exactly the same
thing"), narradas en tercera persona sin un solo verbo en imperativo dirigido al lector. No
son medios, etapas u objetos de trabajo que alguien revise: son un diagnostico clinico de
lo que le pasa a quien atraviesa el Entrepreneurial Seizure, la misma figura que `R2`, `R3`
y `R4` ya establecieron para todo el capitulo. El cierre del capitulo, "You take this one
step at a time" (`L231`), es una unica advertencia (manual seccion `4`, `P.11`: una
advertencia es linea, no procedimiento) que remite al capitulo siguiente sin desplegar ella
misma ningun paso. **No abre candidato ni puntero nuevo.**

**VEREDICTO: `cap_03` SE REGISTRA MINADO CON CERO CANDIDATOS.** Es el primer capitulo del
libro (`The Entrepreneurial Myth`): el diagnostico del mito del emprendedor, la
Entrepreneurial Seizure, la Fatal Assumption y el caso de Sarah, sin un solo tramo con
inventario propio de medios, etapas u objetos de trabajo bajo `9.1`. **Cero candidatos con
su razon escrita.**

### G9.4.d. Discutibles

**Ninguno.** El unico tramo que se acerco a competir (las cuatro etapas de `L225`) se
resuelve sin ambiguedad: son un diagnostico narrado en tercera persona, sin un solo verbo en
imperativo, mas debil incluso que el discutible de `cap_22` `Rb` de la vuelta `8`
(`G8.4.c`), que si traia cuatro imperativos explicitos ("you must") y aun asi se cerro
`SANO`. No abro discutible sobre `cap_03`.

### G9.4.e. `PASOS INVENTADOS POR CAPITULO`, los tres capitulos de esta vuelta (`AUDITOR_FORJA.md` 8)

Los tres capitulos de esta vuelta cerraron con **cero candidatos** (`G9.2`, `G9.3`, `G9.4`),
asi que no hay pasos escritos que medir: no es que la fidelidad haya fallado, es que no hay
ficha de la que medirla.

<!-- TALLADO: parcial salida=.gerber_v9/muestra_fidelidad.txt -->

| capitulo | candidatos nuevos (esta vuelta) | pasos escritos | PUENTE | pasos inventados |
|---|---:|---:|---:|---:|
| `cap_01` | `0` | `0` | `0` | **sin poblacion que medir** |
| `cap_02` | `0` | `0` | `0` | **sin poblacion que medir** |
| `cap_03` | `0` | `0` | `0` | **sin poblacion que medir** |
| **el lote entero** | **`0`** | **`0`** | **`0`** | **sin poblacion que medir** |

**`8.2` de `AUDITOR_FORJA.md`: la escalada se decide sobre el peor capitulo, y aqui no hay
ninguno que escale: los tres estan en la misma poblacion vacia.**

### G9.4.f. La muestra de fidelidad con su semilla escrita (`D.58`, regimen ligero)

Salida de
`python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_01,cap_02,cap_03 --semilla g9`,
guardada en `.gerber_v9/muestra_fidelidad.txt`:

<!-- TALLADO: salida=.gerber_v9/muestra_fidelidad.txt -->

    MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO (D.58)
      libro    : gerber_emyth
      semilla  : g9
      capitulos: cap_01, cap_02, cap_03

      RELEIDO ENTERO : cap_02
      POR MUESTRA    : cap_01, cap_03, 15 pasos cada uno

      EL DISPARADOR: si la muestra de un capitulo pasa del 10 por ciento de
      pasos inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.

      --- cap_01: 0 paso(s) en la muestra

      --- cap_03: 0 paso(s) en la muestra

      --- cap_02: ENTERO, 0 paso(s), no hay muestra que elegir

**LA SEMILLA `g9` REPARTE `cap_02` ENTERO Y `cap_01`/`cap_03` POR MUESTRA, PERO LOS TRES DAN
`0` PASOS: NO HAY CANDIDATOS DE LOS QUE MUESTREAR.** El disparador del `10` por ciento no
tiene sobre que dispararse (`0` de `0` no es una fraccion). **NO SE DISPARA NADA, PORQUE NO
HAY NADA QUE DISPARAR.**

## G9.5. TAREA 2: CERRAR `d094` Y LA FRONTERA DEL LIBRO COMPLETA

### G9.5.a. `d094` pagada

Salida de
`python scripts/deuda.py --pagar d094 --vuelta 9 --como "vuelta 9 lee cap_01, cap_02 y cap_03 enteros de gerber_emyth (leyendo cero candidatos con razon escrita en cada uno) y cierra el hueco declarado en d094"`,
guardada en `.gerber_v9/pago_d094.txt`:

<!-- TALLADO: salida=.gerber_v9/pago_d094.txt -->

    PAGADA d094 en la vuelta 9

**`d094` QUEDA PAGADA.** Nacio en la vuelta `2` para anotar que `cap_01` a `cap_03` seguian
sin minar por decision del fundador (`docs/loop/DEUDA.jsonl` linea `94`); esta vuelta los
lee enteros y cierra el hueco que anotaba.

### G9.5.b. La tabla del libro entero, `cap_01` a `cap_22`, con su estado y su firma

**ES LO QUE SE LLEVA LA COSECHA** (encargo, seccion `2`): fundida de tres fuentes medidas
hoy, `docs/loop/TABLERO.jsonl` (grafo mas bandejas), `config/frentes.json` (los capitulos
ya firmados en cero por un acta del auditor) y `cuarentena/gerber_emyth/*.json` (los
candidatos por su `UNIDAD DE ORIGEN`). Salida de `python .gerber_v9/tabla_libro.py`,
guardada en `.gerber_v9/tabla_libro.txt`:

<!-- TALLADO: salida=.gerber_v9/tabla_libro.txt -->

    | capitulo | estado | candidatos | firma |
    |---|---|---:|---|
    | `cap_01` | MINADO EN CERO | 0 | vuelta 9, este reporte (G9.2/G9.3/G9.4), sin acta todavia |
    | `cap_02` | MINADO EN CERO | 0 | vuelta 9, este reporte (G9.2/G9.3/G9.4), sin acta todavia |
    | `cap_03` | MINADO EN CERO | 0 | vuelta 9, este reporte (G9.2/G9.3/G9.4), sin acta todavia |
    | `cap_04` | MINADO CON CANDIDATOS | 1 | TABLERO.jsonl, grafo+bandejas |
    | `cap_05` | MINADO EN CERO | 0 | ACTA G2 (cap_05 y cap_06), ACTA G3 3.5 (cap_09 y cap_10), ACTA G5 (cap_16 y cap_17, SIN SUPERFICIE con su razon leida) y ACTA G8 3.2 (cap_20 la carta a Sarah mas los agradecimientos, cap_21 el Epilogue, cap_22 el Afterword mas el back matter). Frente gerber_emyth, rama extraccion-gerber_emyth |
    | `cap_06` | MINADO EN CERO | 0 | ACTA G2 (cap_05 y cap_06), ACTA G3 3.5 (cap_09 y cap_10), ACTA G5 (cap_16 y cap_17, SIN SUPERFICIE con su razon leida) y ACTA G8 3.2 (cap_20 la carta a Sarah mas los agradecimientos, cap_21 el Epilogue, cap_22 el Afterword mas el back matter). Frente gerber_emyth, rama extraccion-gerber_emyth |
    | `cap_07` | MINADO CON CANDIDATOS | 1 | TABLERO.jsonl, grafo+bandejas |
    | `cap_08` | MINADO CON CANDIDATOS | 2 | TABLERO.jsonl, grafo+bandejas |
    | `cap_09` | MINADO EN CERO | 0 | ACTA G2 (cap_05 y cap_06), ACTA G3 3.5 (cap_09 y cap_10), ACTA G5 (cap_16 y cap_17, SIN SUPERFICIE con su razon leida) y ACTA G8 3.2 (cap_20 la carta a Sarah mas los agradecimientos, cap_21 el Epilogue, cap_22 el Afterword mas el back matter). Frente gerber_emyth, rama extraccion-gerber_emyth |
    | `cap_10` | MINADO EN CERO | 0 | ACTA G2 (cap_05 y cap_06), ACTA G3 3.5 (cap_09 y cap_10), ACTA G5 (cap_16 y cap_17, SIN SUPERFICIE con su razon leida) y ACTA G8 3.2 (cap_20 la carta a Sarah mas los agradecimientos, cap_21 el Epilogue, cap_22 el Afterword mas el back matter). Frente gerber_emyth, rama extraccion-gerber_emyth |
    | `cap_11` | MINADO CON CANDIDATOS | 6 | TABLERO.jsonl, grafo+bandejas |
    | `cap_12` | MINADO CON CANDIDATOS | 3 | TABLERO.jsonl, grafo+bandejas |
    | `cap_13` | MINADO CON CANDIDATOS | 1 | TABLERO.jsonl, grafo+bandejas |
    | `cap_14` | MINADO CON CANDIDATOS | 1 | TABLERO.jsonl, grafo+bandejas |
    | `cap_15` | MINADO CON CANDIDATOS | 1 | TABLERO.jsonl, grafo+bandejas |
    | `cap_16` | MINADO EN CERO | 0 | ACTA G2 (cap_05 y cap_06), ACTA G3 3.5 (cap_09 y cap_10), ACTA G5 (cap_16 y cap_17, SIN SUPERFICIE con su razon leida) y ACTA G8 3.2 (cap_20 la carta a Sarah mas los agradecimientos, cap_21 el Epilogue, cap_22 el Afterword mas el back matter). Frente gerber_emyth, rama extraccion-gerber_emyth |
    | `cap_17` | MINADO EN CERO | 0 | ACTA G2 (cap_05 y cap_06), ACTA G3 3.5 (cap_09 y cap_10), ACTA G5 (cap_16 y cap_17, SIN SUPERFICIE con su razon leida) y ACTA G8 3.2 (cap_20 la carta a Sarah mas los agradecimientos, cap_21 el Epilogue, cap_22 el Afterword mas el back matter). Frente gerber_emyth, rama extraccion-gerber_emyth |
    | `cap_18` | MINADO CON CANDIDATOS | 3 | TABLERO.jsonl, grafo+bandejas |
    | `cap_19` | MINADO CON CANDIDATOS | 3 | TABLERO.jsonl, grafo+bandejas |
    | `cap_20` | MINADO EN CERO | 0 | ACTA G2 (cap_05 y cap_06), ACTA G3 3.5 (cap_09 y cap_10), ACTA G5 (cap_16 y cap_17, SIN SUPERFICIE con su razon leida) y ACTA G8 3.2 (cap_20 la carta a Sarah mas los agradecimientos, cap_21 el Epilogue, cap_22 el Afterword mas el back matter). Frente gerber_emyth, rama extraccion-gerber_emyth |
    | `cap_21` | MINADO EN CERO | 0 | ACTA G2 (cap_05 y cap_06), ACTA G3 3.5 (cap_09 y cap_10), ACTA G5 (cap_16 y cap_17, SIN SUPERFICIE con su razon leida) y ACTA G8 3.2 (cap_20 la carta a Sarah mas los agradecimientos, cap_21 el Epilogue, cap_22 el Afterword mas el back matter). Frente gerber_emyth, rama extraccion-gerber_emyth |
    | `cap_22` | MINADO EN CERO | 0 | ACTA G2 (cap_05 y cap_06), ACTA G3 3.5 (cap_09 y cap_10), ACTA G5 (cap_16 y cap_17, SIN SUPERFICIE con su razon leida) y ACTA G8 3.2 (cap_20 la carta a Sarah mas los agradecimientos, cap_21 el Epilogue, cap_22 el Afterword mas el back matter). Frente gerber_emyth, rama extraccion-gerber_emyth |

    total capitulos: 22   minados: 22   candidatos en bandeja: 22

**`22` DE `22` UNIDADES MINADAS. `22` CANDIDATOS EN BANDEJA, AL DIGITO CON EL TABLERO Y CON
LA SECCION `3` DEL ENCARGO. EL LIBRO QUEDA ENTERO.** Las filas de `cap_01` a `cap_03` citan
`este reporte, sin acta todavia`: son mi veredicto de esta vuelta (`G9.2`, `G9.3`, `G9.4`),
no una firma de `config/frentes.json`, porque esa sede es del auditor (`EXTRACTOR.md` 14,
"la firma de un acta" segun la propia cabecera de `minados_en_cero`): **no la edito yo.**
Cuando el auditor audite esta vuelta y firme su acta, esas tres filas pasan a citar su
propia acta igual que las otras nueve.

### G9.5.c. Los cuatro punteros heredados, comprobados contra los tres capitulos de esta vuelta

**NO LOS DECLARO YO SI NO NACEN** (`EXTRACTOR.md` `15.6`: las aristas `D.37` se declaran en
la vuelta que INSERTA las partes, y esta vuelta no inserta). Lo que el encargo pide en su
seccion `4` es comprobarlos, y eso hago:

    d098   D.37, cap_05 L29, la terna sin cabeza (Infancy, Adolescence, Maturity)
    d104   D.37, cap_12 L21, la terna sin cabeza (Innovation, Quantification, Orchestration)
    d108   releer cap_14 L27 contra L117
    d111   la serie de cap_13, en 0 de 7, con su primera arista declarable ya identificada

**NINGUNO DE LOS CUATRO SE TOCA POR `cap_01`, `cap_02` NI `cap_03`.** Los tres capitulos de
esta vuelta son Foreword, Introduction y el primer capitulo del libro (el diagnostico del
mito del emprendedor): ninguno nombra las tres fases de crecimiento de `d098`, ninguno
nombra Innovation/Quantification/Orchestration de `d104`, ninguno toca `cap_14` ni `cap_17`
(`d108`, `d111`), y ninguno de los tres produjo un candidato nuevo que pudiera emparejarse
con alguna de las cuatro cabezas (`G9.2`, `G9.3`, `G9.4` cierran los tres en cero). **LOS
CUATRO PUNTEROS SIGUEN PUBLICADOS, SIN CAMBIO, PARA LA VUELTA QUE INSERTE.**

## G9.6. EL CIERRE

### G9.6.a. La tabla de cierre de la vuelta `9`, pegada PRIMERO

*Remedio de `d030`/`d112`: mi tabla se pega ANTES de correr `--escribir`, para que
`docs/loop/TABLA_DE_CIERRE.txt` traiga MIS filas y no las de la vuelta anterior.*

| # | tarea | como cerro |
|---:|---|---|
| `1` | `TAREA 1`: registros de apertura | **CERRADA en `G9.1`**: credito en `0` de `3`/`2`/`2`/`2`/`3` las cinco especies (identico a `G8`), deuda en `49`/`39` de apertura (`5` deudas nuevas ajenas a mi desde `G8`) |
| `2` | `cap_01`, `Foreword`: frontera y veredicto | **CERRADA en `G9.2`**: frontera `3` piezas, `1402` palabras de cuerpo (`1434` al digito con `wc -w` del fichero), residuo `0`; cero candidatos, prefacio personal sin inventario propio; cero discutibles |
| `3` | `cap_02`, `Introduction`: frontera y veredicto | **CERRADA en `G9.3`**: frontera `4` piezas, `1212` palabras de cuerpo (`1244` al digito), residuo `0`; cero candidatos, las cuatro ideas del libro son metas sin inventario de medios; cero discutibles |
| `4` | `cap_03`, `Cap. 1`: frontera, veredicto, `PASOS INVENTADOS` y muestra de fidelidad | **CERRADA en `G9.4`**: frontera `5` piezas, `2202` palabras de cuerpo (`2237` al digito), residuo `0`; cero candidatos, diagnostico narrativo sin inventario propio; cero discutibles; muestra semilla `g9` sin poblacion que medir |
| `5` | `TAREA 2`: `d094` pagada y la frontera del libro completa | **CERRADA en `G9.5`**: `d094` pagada; tabla del libro entero `cap_01` a `cap_22` publicada, `22` de `22` minadas, `22` candidatos en bandeja; los cuatro punteros heredados comprobados, ninguno tocado |

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
VERDE, `0` FALLOS.** Antes de esa cifra hubo una corrida anterior con `1` fallo, no
guardada aparte (la salida de arriba es la de la repeticion, la unica que quedo escrita):
corrio con `guiones` todavia en rojo (el mismo tramo de la correccion de arriba); despues
de corregir, la repeticion da `0` fallos, `0` errores.

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
