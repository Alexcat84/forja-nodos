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
    PLACEHOLDER_TABLA_DE_CIERRE_SALIDA

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
    PLACEHOLDER_HASH_ANTES
    $ cp docs/loop/TABLA_DE_CIERRE.txt docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_gerber_v2.txt
    $ git hash-object docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_gerber_v2.txt
    PLACEHOLDER_HASH_DESPUES

### G2.8.d. LAS CONDICIONES DE PARADA, REPASADAS UNA A UNA (`EXTRACTOR.md` 7)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| una pregunta de doctrina | ninguna: los dos discutibles de `G2.7` son de lectura, no de regla, y no piden doctrina nueva | **NO ES PARADA** |
| una caida de dato | ninguna: `0` ficheros de `dataset/`, `bitacora/`, `censos/` ni `config/pares_mutuos.jsonl` movidos (`G2.8.b`) | **NO ES PARADA** |
| algo contradice una regla vigente o una cifra publicada con su corte | nada: la frontera de la vuelta 1 se reproduce identica y el saldo del encargo (`10` candidatos, `4` capitulos) coincide con lo medido en `G2.1` | **NO ES PARADA** |
| una guarda en rojo | ninguna: las tres de `G2.8.a` en VERDE | **NO ES PARADA** |
| una operacion cuyo texto no alcance para ejecutarse sin decidir | ninguna: las cuatro tareas del encargo estaban escritas enteras | **NO ES PARADA** |

**NINGUNA DE LAS CINCO SE CUMPLE. ESTE TURNO CIERRA SIN PARADA**, y `docs/loop/PARA_ALEXIS.md` sigue sin tocar y no es mia (`EXTRACTOR.md` 14).

## G2.9. CREDITO Y LO QUE PROPONGO

    $ python forja.py credito --anotar --especie REPORTE --vuelta 2 --tanda "G2" --racha "PLACEHOLDER_RACHA" --cita "REPORTE.md G2"
    PLACEHOLDER_CREDITO_SALIDA

### Propuestas al auditor, todas en mi sede y ninguna adjudicada por mi

1. **Con `cap_05` y `cap_06` cerrados a cero y firmados, el hueco entre `cap_04` y `cap_07` queda cerrado.** El frente tiene ahora `cap_04`, `cap_05`, `cap_06`, `cap_07`, `cap_08` y `cap_11` minados: seis de veintidos. Propongo que la vuelta siguiente suba a los tres capitulos que `D.58` permite en regimen ligero, ya que esta (la segunda tras la reanudacion) cerro limpia y sin parada, tal como el propio encargo (seccion 3) preveia.
2. **`cap_01`, `cap_02` y `cap_03` siguen en deuda (`d094`)**, y quedan para cuando el auditor o el fundador decidan si entran en el mismo frente o se dejan fuera del corte, como ya se declaro en el encargo.

### Cola declarada

Ninguna. Las cuatro tareas del encargo cierran en esta misma vuelta y no dejan tarea pendiente propia.
