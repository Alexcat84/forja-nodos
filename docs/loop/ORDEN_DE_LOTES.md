# EL ORDEN DE LOTES

**Fijado por `D.24` (10 sep 2026) y completado el mismo dia al llenar la bandeja
entera.** El orden es **por numero de capitulos, de menos a mas**, y el reservado
del mundo 10 va el ultimo.

**NO LO ELIGE EL BUCLE.** Un extractor que abre el libro que le apetece rompe la
comparabilidad entre lotes, que es lo unico que convierte una campaña en una
medida.

---

## La tabla

| lote | clave | caps | palabras | estado |
|---:|---|---:|---:|---|
| **1** | `onu_consumidor` | 4 | 1.534 | **CERRADO E INSERTADO** el 10 sep 2026 (`762e31d`). 6 nodos |
| **2** | `smart_who` | 7 | 44.133 | ~~**ABIERTO.** Dos capitulos por vuelta~~ **CORRECCION DECLARADA (vuelta 10): CERRADO EN EXTRACCION** (ACTA 8 seccion 10). ~~**Seis capitulos minados. 15 candidatos en `cuarentena/smart_who/`, SIN INSERTAR**~~ **CORRECCION DECLARADA (vuelta 16, TAREA 1.c del encargo, ACTA 15 seccion 3.6): esa cifra era cierta al escribirse y hoy es falsa por las dos mitades. LA BANDEJA ESTA VACIA Y EL LOTE 2 ESTA CERRADO E INSERTADO ENTERO. Remedido por mi el 12 sep 2026 antes de escribir esta fila:** `ls cuarentena/smart_who/*.json | wc -l` da **0**; `ls cuarentena/_insertados/smart_who/*.json | wc -l` da **59**; el cruce de los 59 archivados contra `dataset/nodos.jsonl` da **59 dentro del grafo y 0 fuera, 59 + 0 = 59**; y los nodos del grafo con fuente `smart_who` son **59**. **Los seis capitulos minados siguen siendo seis y eso no se toca** |
| 3 | `zhuo_manager` | 12 | 70.041 | ~~(vacio)~~ **CORRECCION DECLARADA (vuelta 10): ABIERTO** (ACTA 9). ~~**3 de 12 ficheros minados, 21 candidatos en `cuarentena/zhuo_manager/`, SIN INSERTAR. Esta vuelta corre a DOS unidades**~~ **CORRECCION DECLARADA (vuelta 11, ACTA 10 punto 1.d.1): aquella cifra era verdad al ESCRIBIRSE y falsa al cerrarse la misma vuelta 10. AL CIERRE DE LA VUELTA 10: 5 de 12 ficheros minados, 50 candidatos en `cuarentena/zhuo_manager/`, SIN INSERTAR.** ~~**Vuelta 11: corrio a UNA unidad (`cap_06.md`, Cap. 5). AL CIERRE DE LA VUELTA 11: 6 de 12 ficheros minados, 68 candidatos en `cuarentena/zhuo_manager/`, SIN INSERTAR.**~~ **CORRECCION DECLARADA (vuelta 13, TAREA 1.d del encargo, ACTA 12 seccion 12): aquella cifra quedo vieja cuando la vuelta 12 mino cuatro capitulos mas y cuando los 68 se archivaron. AL CIERRE DE LA VUELTA 12: 10 de 12 ficheros minados, 60 candidatos en `cuarentena/zhuo_manager/` y 68 archivados en `cuarentena/_insertados/zhuo_manager/`, SIN INSERTAR.** Las tres cifras las remedi yo al abrir la vuelta 13 y estan en `H.0` del reporte: `ls cuarentena/zhuo_manager/*.json | wc -l` da **60** y `ls cuarentena/_insertados/zhuo_manager/*.json | wc -l` da **68**. **CORRECCION DECLARADA (vuelta 14, TAREA 1.c del encargo, ACTA 13 seccion 9): la frase de arriba tiene DOS LECTURAS y por eso se rehace aqui, sin borrarla. Pegado al final de la enumeracion, ese *SIN INSERTAR* se lee como si alcanzase tambien a los 68 archivados, y NO los alcanza: LOS 68 ARCHIVADOS SI ESTAN INSERTADOS. Lo que sigue sin insertar es la BANDEJA.** **Y LA CIFRA DE LA BANDEJA YA NO ES 60: HOY ES 68**, porque la vuelta 13 mino `cap_11` y aniadio ocho candidatos. **EL ESTADO VIGENTE, MEDIDO EN LA VUELTA 14 CON TOTAL, FILTRADO Y RESIDUO (`EXTRACTOR.md` 5 y ACTA 13 seccion 5.5):** `ls cuarentena/zhuo_manager/*.json | wc -l` da **68**; `ls cuarentena/_insertados/zhuo_manager/*.json | wc -l` da **68**; y el cruce de los 68 archivados contra `dataset/nodos.jsonl` da **68 dentro del grafo y 0 fuera, 68 + 0 = 68**, mientras que el cruce de los 68 de la bandeja da **0 dentro y 68 pendientes, 0 + 68 = 68**. **12 de 12 ficheros minados: la EXTRACCION del lote 3 esta CERRADA** (ACTA 13 seccion 8.1). ~~**Su INSERCION no**, y `MODO_INSERCION=cuarentena` sigue vigente.~~ **CORRECCION DECLARADA (vuelta 16, TAREA 1.c del encargo, ACTA 15 secciones 3.6 y 8): las dos mitades de esa frase quedaron viejas la misma tarde del 11 sep 2026. EL LOTE 3 ESTA CERRADO EN EXTRACCION Y CERRADO EN INSERCION, y es el primer lote que `D.39` cierra entero. Remedido por mi el 12 sep 2026 antes de escribir esta fila:** `ls cuarentena/zhuo_manager/*.json | wc -l` da **0**; `ls cuarentena/_insertados/zhuo_manager/*.json | wc -l` da **136**; el cruce de los 136 archivados contra `dataset/nodos.jsonl` da **136 dentro del grafo y 0 fuera, 136 + 0 = 136**; los nodos del grafo con fuente `zhuo_manager` son **136**; y los 136 suman **1.107 pasos**. **Y `MODO_INSERCION=cuarentena` ya no es lo vigente: `D.39` (11 sep 2026) pone `MODO_INSERCION=insertar` por defecto**, y `docs/loop/loop.log` lo registra en sus dos ultimos arranques (`[2026-09-11 17:53:34]` y `[2026-09-11 21:40:37]`). |
| 4 | `scott_radical_candor` | 15 | 108.161 | **ABIERTO en la vuelta 14** (`D.32`, ACTA 13 seccion 8.2). **Las dos condiciones remedidas por el extractor al abrir**: `ls fuentes/scott_radical_candor/ | wc -l` da **15**, y `scott_radical_candor` esta en `FUENTES_CANONICAS.json`. ~~**AL CIERRE DE LA VUELTA 14: 4 de 15 ficheros minados** (`cap_00` a `cap_03`), **2 candidatos en `cuarentena/scott_radical_candor/`, SIN INSERTAR.**~~ **CORRECCION DECLARADA (vuelta 16, TAREA 1.c del encargo, ACTA 15 seccion 3.6): esa cifra era cierta al cierre de la vuelta 14 y la vuelta 15 la movio al minar `cap_04`. AL ABRIR LA VUELTA 16: 5 de 15 ficheros minados** (`cap_00` a `cap_04`) **y 8 candidatos en `cuarentena/scott_radical_candor/`, SIN INSERTAR. Remedido por mi el 12 sep 2026 antes de escribir esta fila:** `ls fuentes/scott_radical_candor/*.md | wc -l` da **15**; `ls cuarentena/scott_radical_candor/*.json | wc -l` da **8**, que suman **63 pasos**; y el cruce de los 8 contra `dataset/nodos.jsonl` da **0 dentro del grafo y 8 pendientes, 0 + 8 = 8**. **La cuenta de minados la leo del registro y no la invento**, porque un capitulo minado no deja marca en el repo: `docs/loop/REPORTE.md` L19036 (`**lote 4, scott_radical_candor** | **ABIERTO.** cap_00 a cap_04 minados, 8 candidatos en cuarentena, 63 pasos`) y `docs/loop/ACTA_AUDITOR.md` L14093. **EL LOTE 4 SIGUE ABIERTO, y por eso sus 8 candidatos no entran** (`D.39`). La frase va cortada a proposito ahi: **el SIN INSERTAR alcanza a la bandeja, que es lo unico que hay**, y esa es la leccion de la correccion de la vuelta 14 en la fila del lote 3. **Las cuatro unidades minadas son MATERIAL DE FRENTE y ninguna declara `Cap. N`**: `Copyright Page`, `Preface`, `Introduction` y `How to Use This Book`. **Los ocho capitulos numerados del libro son `cap_04` a `cap_11` (`Cap. 1` a `Cap. 8`) y suman 81.508 palabras de las 108.161.** **Este recorte NO trae `Notes`, `Index` ni `Acknowledgments`**, comprobado en la vuelta 14 |
| 5 | `marquet_turn_the_ship` | 17 | 33.702 | |
| 6 | `openstax_business_ethics` | 17 | 54.148 | CC BY 4.0 |
| 7 | `grove_high_output` | 18 | 64.372 | |
| 8 | `bernerslee_bananas` | 19 | 21.509 | **ficha PENDIENTE**, ver abajo |
| 9 | `gerber_emyth` | 22 | 62.648 | sin su cap. 17 |
| 10 | `openstax_org_behavior` | 32 | 93.408 | CC BY 4.0. El mayor |
| **11** | `gerber_emyth_cap17_reservado` | 1 | 3.845 | **RESERVADO. Entra el ultimo** |
| | **total** | **164** | **557.501** | |

> **CORRECCION DECLARADA, 10 sep 2026, vuelta 10 del bucle, TAREA 1.d del encargo.**
> **Se ha tocado SOLO la columna `estado` de los lotes 2 y 3**, y el texto viejo se deja a
> la vista tachado en vez de borrarse. **Ni el orden, ni las claves, ni la cuenta de
> capitulos, ni las palabras se han tocado:** eso lo fija `D.24` y no lo elige el bucle.

> **CORRECCION DECLARADA, 12 sep 2026, vuelta 16 del bucle, TAREA 1.c del encargo,
> ACTA 15 seccion 3.6.**
>
> **Se ha tocado SOLO la columna `estado` de los lotes 2, 3 y 4, y la seccion
> *Lo que este documento NO decide*.** El texto viejo se deja a la vista tachado en vez
> de borrarse. **Ni el orden, ni las claves, ni la cuenta de capitulos, ni las palabras
> se han tocado:** eso lo fija `D.24` y no lo elige el bucle.
>
> **LAS TRES FILAS ERAN CIERTAS EL DIA EN QUE SE ESCRIBIERON Y LA JURISPRUDENCIA DE ESA
> ESPECIE ESTA DENTRO DE ESTE MISMO FICHERO** (ACTA 10 punto 1.d.1: *aquella cifra era
> verdad al ESCRIBIRSE y falsa al cerrarse la misma vuelta*). **El remedio de la casa
> para eso es correccion declarada, no borrado.**
>
> **LAS CUATRO CIFRAS LAS REMEDI YO EL 12 SEP 2026 ANTES DE ESCRIBIRLAS**, y cada celda
> lleva su comando al lado: que la cifra viniera puesta en el encargo no me exime de
> comprobarla (`EXTRACTOR.md` 5, *el instrumento manda*).

**LOS EMPATES SE DESHACEN POR PALABRAS:** `marquet_turn_the_ship` y
`openstax_business_ethics` tienen 17 capitulos cada uno, y va primero el de menos
palabras.

## Por que de menos a mas

**El primer lote no se hace para meter nodos: se hace para medir el instrumento
con trabajo de verdad delante, barato** (`D.24`). Un lote de calibracion grande no
calibra, solo cuesta mas.

**Y el orden importa por una razon medida:** el primero que entra cambia lo que el
segundo mide (`EXTRACTOR.md` seccion 12). Con el grafo casi vacio la cola es
corta; crece con el grafo.

## Por que el reservado va el ultimo

`gerber_emyth_cap17_reservado` es **un solo capitulo apartado a proposito** por el
plan de recorte del mundo 11
(`docs/ESTRENO_DE_LA_ADUANA.md` seccion 1.1). **Entra cuando el grafo ya sepa con
quien compararlo**, y en particular cuando su propio libro ya este dentro: es el
unico caso de la campaña en que se sabe de antemano donde va a caer un candidato.

## El volumen por vuelta, que no es fijo

**Sale de la metrica `PASOS INVENTADOS POR CAPITULO`** que el auditor publica en
cada acta (`AUDITOR_FORJA.md` seccion 8, `CALIBRACION_D4.md` seccion 9.4):

| lo que mida un lote | el siguiente corre a |
|---|---|
| se mantiene o baja respecto al **36 por ciento** del lote 1 | **un capitulo mas por vuelta** |
| sube | **el techo vuelve a UNO** |

    lote 1   UN capitulo por vuelta      36,00 por ciento de puentes
    lote 2   DOS capitulos por vuelta    decision del fundador, 10 sep 2026
    lote 3   TRES capitulos por vuelta    3,31 por ciento, FIRMADA el 11 sep
             ~~TRES~~  la vuelta 12 corrio a CUATRO por encargo del fundador
    lote 4   ~~CUATRO~~ capitulos por vuelta decision del fundador, 11 sep 2026
    lote 4   TRES capitulos por vuelta   EL TRAMO BAJA, decision del fundador
                                         del 12 sep 2026, punto 2

> **CORRECCION DECLARADA, 11 sep 2026, vuelta 13 del bucle, TAREA 1.d del encargo.**
>
> **La columna de volumen decia `lote 3, TRES capitulos por vuelta` y la vuelta 12 corrio
> a CUATRO.** El extractor de la vuelta 12 declaro la discrepancia en vez de resolverla
> copiando, y **la ACTA 12 seccion 11 la adjudico: corrio bien.** El motivo escrito alli es
> que **un encargo asigna el trabajo de una vuelta y la tabla fija el techo de un lote**, y
> que `AUDITOR_FORJA.md` 8.1 ya lleva la redaccion nueva, asi que **la sede de doctrina
> estaba al dia y la que se quedo vieja era esta tabla.**
>
> **El texto viejo se tacha y no se borra**, y **no se ha tocado ni el orden, ni las claves,
> ni la cuenta de capitulos, ni las palabras:** eso lo fija `D.24` y no lo elige el bucle.

**LA CIFRA DEL LOTE 3 ESTA FIRMADA: 3,31 POR CIENTO** (decision del fundador del
11 sep 2026, punto 5.8). Bajo del 36 por ciento del lote 1 **en un factor de
once**, asi que el lote 4 y los siguientes corren a **CUATRO capitulos por
vuelta**.

> ### **CORRECCION DECLARADA, 12 sep 2026: EL LOTE 4 BAJA A TRES CAPITULOS POR VUELTA**
>
> *Decision del fundador del 12 sep 2026, punto 2, sobre la parada de la vuelta 17.*
>
> **LA CIFRA DE VOLUMEN NO SE HA MOVIDO y por eso el parrafo de arriba no se tacha:**
> el peor capitulo del lote 4 es `cap_04` con **6,25**, por debajo del tope de 10,
> **y por esa metrica el tramo seguiria en cuatro.** Lo que tumbo el cuatro es **el
> otro disparador**, el de `EXTRACTOR.md` 12.4, **cumplido por sus dos mitades** en
> la vuelta 17: por encima del techo de candidatos **y** sin cerrar su reporte.
>
> **Y VA CON LA REGLA DE PRECEDENCIA QUE FALTABA: EL TECHO DE CANDIDATOS POR VUELTA
> MANDA SOBRE EL DE CAPITULOS.** Si un solo capitulo pasa del techo, **la vuelta
> cierra en ese capitulo y lo declara**; los que quedaban del tramo pasan a la
> siguiente. **EJEMPLAR: `cap_07` dio 24 candidatos contra un techo de 15.**
>
> **EL FRENO DE `PASOS INVENTADOS` SIGUE APARTE**, con su tope de 10 y su salida
> escrita. Son dos techos distintos y ninguno sustituye al otro.
>
> **UNA DISCREPANCIA QUE DECLARO EN VEZ DE RESOLVERLA COPIANDO** (`D.38.3`): la
> `ACTA 17` dice **25 candidatos** en su seccion `5.2` y **24** en su `1.3`, y el
> fundador firma **24**. Lo que mido hoy, con el instrumento pegado:
>
>     $ git ls-files --others --exclude-standard cuarentena/scott_radical_candor/ | wc -l   ->  24
>     $ grep -l "cap_07" cuarentena/scott_radical_candor/*.json | wc -l                     ->  24
>     $ (los dos conjuntos comparados con diff)                                             ->  identicos
>
> **24, y son los mismos 24 por las dos medidas.** El `25` de la `5.2` queda sin
> reproducir: **no cambia nada** (las dos cifras pasan de 15), **pero es cifra
> publicada en acta y se sube al auditor de la vuelta 18 para que la adjudique.**

**Y EL FRENO VA ESCRITO CON SU NUMERO, que es lo que lo hace freno:** la cifra se
sigue publicando en cada acta, y **si sube por encima de 10 por ciento, se vuelve a
TRES.** No es una vigilancia general: es un umbral con su salida.

## Lo que hay que resolver ANTES de llegar a su lote

**`bernerslee_bananas` (lote 8) tiene la ficha incompleta**, y esta declarado en
`fuentes/FUENTES_CANONICAS.json`: el recorte no localizo pagina de copyright en el
PDF, asi que **no hay ISBN ni editorial verificados**, y el año va como
`PENDIENTE`. **La fuente es un campo sagrado** (manual principio 8): esa ficha se
cierra antes del primer nodo de ese libro, y **no la cierra el bucle.**

**Se dice ahora, con siete lotes de margen, y no el dia que toque.**

## Lo que este documento NO decide

**Cuando se inserta cada lote.** La extraccion y la insercion van por caminos
separados desde `D.26`: el bucle extrae a cuarentena, y ~~**cada insercion es una
autorizacion del fundador** que se pide con el informe del lote delante~~. **Un lote
cerrado y sin insertar no bloquea la extraccion del siguiente** (`D.32`).

> **CORRECCION DECLARADA, 12 sep 2026, vuelta 16 del bucle, TAREA 1.c del encargo,
> ACTA 15 seccion 3.6.**
>
> **La frase tachada era doctrina vigente cuando se escribio y hoy esta superada por
> `D.39` (11 sep 2026, decision 3 del fundador), que es correccion declarada de `D.26`
> y es la mas reciente de las dos.** `D.13` resuelve el choque sin contradiccion: entre
> dos reglas fechadas que chocan gana la mas reciente.
>
> **LO QUE DICE HOY, leido de `docs/BANCO_DE_REGLAS.md` L1492 a L1498 en esta vuelta:**
> *cuando un lote queda cerrado en extraccion y el acta del auditor certifica su
> informe (todos `ENTRARIAN`, o las caidas declaradas con su motivo), el extractor
> inserta ese lote en su vuelta siguiente, sin firma nueva del fundador. Los candidatos
> de un lote ABIERTO siguen en cuarentena hasta que su lote cierre.*
>
> **Y `MODO_INSERCION` pasa a `insertar` por defecto.** Lo que la regla NO abre es la
> barra libre: **meter candidatos de un lote abierto es una caida de dato**
> (`EXTRACTOR.md` 15.7), y por eso los 8 del lote 4 siguen hoy en la bandeja.
>
> **El texto viejo se tacha y no se borra**, y **no se ha tocado ni el orden, ni las
> claves, ni la cuenta de capitulos, ni las palabras:** eso lo fija `D.24` y no lo
> elige el bucle.
