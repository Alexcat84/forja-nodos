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
| **2** | `smart_who` | 7 | 44.133 | ~~**ABIERTO.** Dos capitulos por vuelta~~ **CORRECCION DECLARADA (vuelta 10): CERRADO EN EXTRACCION** (ACTA 8 seccion 10). **Seis capitulos minados. 15 candidatos en `cuarentena/smart_who/`, SIN INSERTAR** |
| 3 | `zhuo_manager` | 12 | 70.041 | ~~(vacio)~~ **CORRECCION DECLARADA (vuelta 10): ABIERTO** (ACTA 9). ~~**3 de 12 ficheros minados, 21 candidatos en `cuarentena/zhuo_manager/`, SIN INSERTAR. Esta vuelta corre a DOS unidades**~~ **CORRECCION DECLARADA (vuelta 11, ACTA 10 punto 1.d.1): aquella cifra era verdad al ESCRIBIRSE y falsa al cerrarse la misma vuelta 10. AL CIERRE DE LA VUELTA 10: 5 de 12 ficheros minados, 50 candidatos en `cuarentena/zhuo_manager/`, SIN INSERTAR.** **Vuelta 11: corrio a UNA unidad (`cap_06.md`, Cap. 5). AL CIERRE DE LA VUELTA 11: 6 de 12 ficheros minados, 68 candidatos en `cuarentena/zhuo_manager/`, SIN INSERTAR.** |
| 4 | `scott_radical_candor` | 15 | 108.161 | |
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
    lote 4   CUATRO capitulos por vuelta decision del fundador, 11 sep 2026

**LA CIFRA DEL LOTE 3 ESTA FIRMADA: 3,31 POR CIENTO** (decision del fundador del
11 sep 2026, punto 5.8). Bajo del 36 por ciento del lote 1 **en un factor de
once**, asi que el lote 4 y los siguientes corren a **CUATRO capitulos por
vuelta**.

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
separados desde `D.26`: el bucle extrae a cuarentena, y **cada insercion es una
autorizacion del fundador** que se pide con el informe del lote delante. **Un lote
cerrado y sin insertar no bloquea la extraccion del siguiente** (`D.32`).
