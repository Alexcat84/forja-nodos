# LA CALIBRACION D.4: los umbrales contra la distribucion

**TANDA B de la v0.3, 9 sep 2026.** Este documento recalibra los tres umbrales de
`config/umbrales.json` contra el catalogo limpio de My-idea, y cumple lo que
`docs/COSECHA_2026-09.md` seccion 4 escribio que la fase 2 necesitaba.

**Ninguna cifra de aqui esta tecleada.** Todas salen de
`calibracion/SALIDA_D4.txt` y de `calibracion/SALIDA_ADUANA_MUESTRA.txt`, y las
medidas crudas par a par estan volcadas en `calibracion/MEDIDAS_CRUDAS.jsonl`,
para que cualquier umbral se pueda re evaluar sin volver a medir.

| | |
|---|---|
| corpus | `docs/GRAFO_DE_REFERENCIA.md`, tag `catalogo-limpio-v1`, commit `1b128323` |
| vivos | 3.169 |
| semilla de muestreo | 20260909 |
| instrumentos | `calibracion/medir_d4.py`, `calibracion/volcar_medidas.py`, `calibracion/aduana_sobre_muestra.py` |

---

> **AMPLIADA EL 10 sep 2026 con la SECCION 9, `LOTE 1`**, que calibra algo que
> las ocho primeras no podian: **el trabajo de extraer**, medido sobre el primer
> lote real. Las secciones 1 a 8 calibraron las señales contra un catalogo ya
> hecho; la 9 calibra la mano que escribe.

## 1. LO QUE D.4 EXIGIA, Y DONDE ESTA CADA COSA

| lo que pedia la cosecha seccion 4 | donde esta |
|---|---|
| la distribucion de las tres señales (p50, p90, p99) | seccion 2 |
| la banda por tramo de cada una | seccion 3 |
| la tasa de acierto por tramo separando gemelo de jerarquia (9.19) | seccion 3 |
| la averia del cero silencioso | seccion 5.A |
| la averia del umbral por debajo de la mediana | seccion 5.B |
| la prueba de que la aduana acepta el catalogo auditado | seccion 6 |

## 2. LA DISTRIBUCION, POR CLASE DE VERDAD CONOCIDA

Las tres clases y por que son verdad conocida estan en
`docs/GRAFO_DE_REFERENCIA.md` seccion 3: **671 gemelos adjudicados REPITE por una
persona**, 800 pares de jerarquia declarada (de 7.282) y 4.000 ajenos al azar.

| señal | clase | p50 | p90 | p99 | max |
|---|---|---:|---:|---:|---:|
| **similitud_texto** | GEMELO | 0,394 | 0,593 | 0,728 | 0,811 |
| | JERARQUIA | 0,213 | 0,288 | 0,365 | 0,439 |
| | AJENO | 0,198 | 0,261 | 0,306 | **0,344** |
| **familia_id** | GEMELO | 0,333 | 0,800 | 1,000 | 1,000 |
| | JERARQUIA | 0,000 | 0,200 | 0,500 | 0,667 |
| | AJENO | 0,000 | 0,000 | 0,143 | **0,250** |
| **paso_contra_nodo** | GEMELO | 0,946 | 1,000 | 1,000 | 1,000 |
| | JERARQUIA | 0,439 | 0,522 | 0,644 | 0,918 |
| | AJENO | 0,412 | 0,464 | **0,524** | **0,652** |

**TRES LECTURAS, Y LA TERCERA ES LA QUE MANDA EN ESTA CALIBRACION:**

1. **Las señales 1 y 2 separan limpiamente.** El maximo de los AJENOS (0,344 y
   0,250) esta por debajo de la mediana de los GEMELOS (0,394 y 0,333): hay
   sitio para poner el umbral entre las dos poblaciones **sin tocarse**.
2. **La señal 3 no separa igual.** Su maximo ajeno es 0,652 y su p99 es 0,524:
   **la cola ajena de la señal 3 llega alto**, y ahi es donde vive la averia (b).
3. **NINGUNA de las tres separa la JERARQUIA de los AJENOS.** Miralo en la
   señal 3: jerarquia p50 0,439 contra ajeno p50 0,412. Y en la señal 1:
   0,213 contra 0,198. **Son la misma poblacion para una señal de superficie.**
   Esto no es un fallo de la calibracion: es el principio 4 del manual con
   numeros propios, y su consecuencia esta escrita en la seccion 7.

**UNA HONESTIDAD SOBRE LA CLASE GEMELO, y hay que decirla antes de usar sus
numeros.** Los 671 pares son (superviviente, absorbido) DESPUES de que la fusion
se ejecutara, asi que **el superviviente contiene el texto del absorbido**. Eso
sesga las dos señales, y en direcciones contrarias:

- la **señal 1** queda SUBESTIMADA (el superviviente trae ademas su propio
  material, que diluye el parecido);
- la **señal 3** queda SOBREESTIMADA (los pasos del absorbido estan literalmente
  dentro del superviviente, por eso su p50 es 0,946).

**Lo que esta clase mide de verdad, dicho con precision: si la aduana cazaria un
candidato cuyo material YA VIVE en el grafo.** Ese es el duplicado mas comun de
todos (volver a extraer un procedimiento que ya entro) y es el que la aduana
existe para cazar. **Lo que NO mide es el gemelo parafraseado**, y para ese la
unica evidencia de esta casa sigue siendo su propio fixture plantado.

## 3. LA BANDA POR TRAMO (9.19)

> **La similitud alta caza duplicados, la media caza jerarquias** (banco de
> textos 9.19 de My-idea, 13 ago 2026).

Medido sobre el catalogo, la banda de la **señal 1** dice esto:

| tramo | GEMELO | JERARQ | AJENO |
|---|---:|---:|---:|
| 0,0 a 0,2 | 22 | 342 | 2.061 |
| 0,2 a 0,3 | 123 | 745 | 1.878 |
| **0,3 a 0,4** | **201** | 99 | 61 |
| **0,4 en adelante** | **325** | 4 | **0** |

**El 9.19 se confirma a medias, y la mitad que falla importa.** Se confirma que
**arriba solo hay gemelos**: de 0,4 para arriba hay 325 gemelos y CERO ajenos.
**No se confirma que la banda media sea de jerarquias**: en 0,2 a 0,3 hay 745
pares de jerarquia y 1.878 ajenos, o sea que **la banda media es sobre todo
ruido**. En aquella casa la cola venia ordenada por similitud y por eso la banda
media concentraba jerarquia; aqui, medido contra pares al azar, no.

**Lo que esto cambia para la forja:** la banda ALTA se puede leer como señal de
duplicado. **La banda MEDIA no se puede leer como señal de jerarquia**, y quien
la lea asi va a leer ruido tres de cada cuatro veces.

## 4. LOS UMBRALES NUEVOS, CON SU MEDICION AL LADO

La vara: **un umbral tiene que cazar GEMELOS y no abrir cola falsa.** La ultima
columna es la que decide, y es la traduccion operativa de *disparar deja de ser
noticia*: **cuantos vecinos falsos levantaria cada candidato contra los 3.169
vivos**.

### similitud_texto: de 0,45 a **0,35**

| umbral | GEMELO caza | JERARQ caza | cola falsa por candidato |
|---:|---:|---:|---:|
| 0,30 | 78,4 por ciento | 7,0 | **48,3** |
| **0,35** | **63,0 por ciento** | 1,4 | **0,0** |
| 0,40 | 48,4 por ciento | 0,4 | 0,0 |
| 0,45 (vigente) | 34,6 por ciento | 0,0 | 0,0 |

**Se baja a 0,35.** El vigente 0,45 dejaba escapar **28 puntos de deteccion de
gemelos a cambio de nada**: a 0,35 la cola falsa sigue siendo CERO, porque el
maximo ajeno medido es 0,344. Por debajo de 0,35 la cola explota a 48 vecinos.
**0,35 es el borde exacto de la poblacion ajena, y esta medido, no elegido.**

### familia_id: de 0,50 a **0,30**

| umbral | GEMELO caza | JERARQ caza | cola falsa por candidato |
|---:|---:|---:|---:|
| **0,30** | **51,1 por ciento** | 4,6 | **0,0** |
| 0,40 | 44,9 por ciento | 2,5 | 0,0 |
| 0,50 (vigente) | 37,4 por ciento | 1,6 | 0,0 |

**Se baja a 0,30.** Gana 14 puntos de deteccion con cola falsa CERO. El maximo
ajeno es 0,250, asi que 0,30 deja un margen de 0,05 sobre la poblacion que no
debe disparar.

### paso_contra_nodo: de 0,55 a **0,60**, y es la averia (b)

| umbral | GEMELO caza | JERARQ caza | cola falsa por candidato |
|---:|---:|---:|---:|
| 0,45 | 97,3 por ciento | 40,1 | **522,9** |
| 0,50 | 94,0 por ciento | 16,1 | **79,2** |
| 0,55 (vigente) | 91,2 por ciento | 5,6 | **14,3** |
| **0,60** | **87,2 por ciento** | 3,0 | **2,4** |
| 0,65 | 82,1 por ciento | 1,0 | 1,6 |
| 0,70 | 76,8 por ciento | 0,5 | 0,0 |

**Se sube a 0,60**, y esta es la unica de las tres que se mueve hacia arriba.

**EL DATO:** el umbral vigente 0,55 abre una cola falsa de **14,3 vecinos por
candidato**. Sobre un lote de 167 candidatos son **unas 2.400 lecturas de ruido**.
Subir a 0,60 la deja en **2,4** (seis veces menos) **a cambio de 4 puntos de
deteccion de gemelos**, y esos cuatro puntos los recupera la señal 1, que con su
umbral nuevo pasa de 34,6 a 63,0 por ciento. **Las señales se solapan poco: por
eso se corren las tres.**

**Por que NO se sube a 0,70 aunque la cola falsa sea cero ahi:** el fixture del
HIJO de esta casa (el que despliega en siete pasos el paso 2 de su madre) mide
**0,658**. A 0,70 ese hijo entraria SIN que nadie declarara su arista, y
*la jerarquia se cablea, no se copia* es el principio 2 del manual. **0,60 deja
al hijo cazado con margen y corta la cola seis veces.**

> ### CORRECCION DECLARADA, 9 sep 2026, misma tarde
>
> **La cifra de 2,4 de la tabla de arriba NO SE BORRA, y era un SUELO, no un
> centro.** El estreno de la aduana la midio directamente sobre un lote real
> contra 3.157 vivos (`docs/ESTRENO_DE_LA_ADUANA.md` seccion 5) y salio **4,6
> vecinos por candidato**, casi el doble.
>
> **EL MOTIVO, y es doctrina:** la estimacion analitica sale de la tasa de
> disparo sobre pares AL AZAR, y **un lote real no es al azar**. Trae capitulos
> enteros del mismo tema, que es exactamente el caso que `EXTRACTOR.md` seccion
> 12 avisa. Una poblacion de referencia mal elegida no da una cifra imprecisa:
> da una cifra sesgada hacia abajo.
>
> **MANDA LA MEDIDA DIRECTA. Cuando una estimacion y un control chocan, no se
> promedian: gana el que conto.** El umbral 0,60 no se mueve por esto: 4,6 sigue
> siendo tres veces menos que los 14,3 del vigente anterior, y la decision se
> tomo por la comparacion entre umbrales, que la correccion no altera.

### El control directo, que confirma la estimacion

La cola por candidato se midio de dos maneras, y las dos van publicadas porque
una estimacion sin control es una proyeccion. **Conteo directo de 10 candidatos
contra los 3.169 vivos, con los umbrales VIGENTES de la v0.2 (0,45 / 0,50 /
0,55)**, corrida de 2.831 segundos:

| | |
|---|---|
| cola por candidato | min 4, **p50 7**, p90 17, max 18 |
| uno a uno | 18, 17, 16, 15, 9, 7, 6, 6, 5, 4 |
| candidatos con cola VACIA | **0 de 10** |

**Las dos mediciones coinciden en lo que importa:** la estimacion daba 14,3
falsos por candidato para la señal 3 sola, el conteo directo da una mediana de 7
con cola larga hasta 18, **y NINGUN candidato entraba sin leer nada**. Sobre un
catalogo auditado par a par, donde por construccion no queda un solo duplicado,
**cada nodo abria una cola de siete lecturas de ruido.** Eso es exactamente
*disparar deja de ser noticia*, medido en casa propia.

### Lo que cambia en el fixture propio, y es el diseño multi señal funcionando

Con los umbrales nuevos, el **gemelo plantado** de esta casa (mismos pasos,
otras palabras) pasa a estar levantado **solo por la señal 1** (mide 0,515, muy
por encima de 0,35), porque su `paso_contra_nodo` de 0,584 queda ahora bajo el
0,60. **Sigue cazado, y por una sola señal.** Es lo que el manual dice de las
tres: se solapan poco, y por eso se corren juntas. La prueba de aceptacion lo
declara en su salida.

## 5. LAS DOS AVERIAS DE `costuras_internas.py`, MEDIDAS AQUI

### 5.A. EL CERO SILENCIOSO: cubierto, y comprobado sobre el catalogo

La regla ya vive en **D.16** desde la tanda A: fuera de su dominio una señal
devuelve `NO APLICA` explicito, que revienta si se compara con un umbral.

**Lo que esta calibracion añade es la medicion:** sobre los 5.471 pares medidos,
**NO_APLICA salio 0 veces en las tres señales**. Ninguna quedo fuera de su
dominio en este corpus. Eso no debilita la regla: **dice que el corpus no la
ejercita, no que sobre.** El caso que la disparo en aquella casa (un nodo con
menos pasos que el minimo de la ventana) no existe aqui porque las tres señales
de la forja no usan ventana.

### 5.B. EL UMBRAL POR DEBAJO DE LA MEDIANA

> *El p50 de la señal nueva es 45,8, o sea que el umbral quedo POR DEBAJO DE LA
> MEDIANA. Disparar deja de ser noticia.*

Contra la mediana de los AJENOS, los tres umbrales vigentes salian **SANOS**
(0,45 contra 0,198; 0,50 contra 0,000; 0,55 contra 0,412). **Y aun asi la señal
3 estaba mal puesta.**

**LA LECCION QUE ESTA CALIBRACION AÑADE A LA REGLA MADRE, y se escribe porque la
vara de la mediana no la habria cazado:** la mediana no basta cuando la
distribucion tiene **cola gorda**. La señal 3 tiene su p50 ajeno en 0,412 y su
maximo en 0,652: el umbral 0,55 estaba muy por encima de la mediana **y aun asi
dentro del 1 por ciento superior de la poblacion ajena**, que sobre 3.169 vivos
son 14 vecinos falsos por candidato.

> **LA VARA CORREGIDA: un umbral no se juzga contra la mediana de lo que no debe
> disparar, sino contra su COLA.** La cifra que decide es cuantos vecinos falsos
> abre por candidato, y esa se calcula multiplicando la tasa de disparo ajena
> por el tamaño del catalogo. **La mediana dice si el umbral es absurdo; la cola
> dice si es usable.**

Queda escrita como **D.18** en `docs/BANCO_DE_REGLAS.md`.

## 6. LA PRUEBA DE ACEPTACION: la aduana contra el catalogo auditado

> **Un catalogo auditado que la aduana rechazara en masa es la aduana mal
> calibrada, no el catalogo.**

Medido con `calibracion/aduana_sobre_muestra.py` sobre **50 nodos vivos** al azar
(semilla 20260909), corridos por el MODO INFORME de la aduana de verdad:

| | |
|---|---:|
| ENTRARIAN sin leer nada | 35 |
| BLOQUEARIAN (cola de lectura, **no es rechazo**) | 0 |
| CAERIAN (rechazo) | 15 |
| **ACEPTADOS** | **35 de 50 (70,0 por ciento)** |

**Y EL BARRIDO ENTERO, contado sobre los 3.169 vivos y no estimado sobre 50:**

| guarda | cuantos | por ciento |
|---|---:|---:|
| ids que rompen `docs/REGLAS_DE_ID.md` | **917** | 28,9 |
| de ellos, por preposicion o articulo | 768 | |
| de ellos, por palabra fuera del castellano | 93 | |
| de ellos, por sufijo numerico | 48 | |
| de ellos, por una sola pieza | 8 | |
| nodos con guion largo o medio en su texto | **48** | 1,5 |
| **VIVOS QUE PASARIAN LAS DOS GUARDAS** | **2.222** | **70,1** |

La muestra de 50 estimo 70,0 y el barrido entero cuenta 70,1: **la muestra era
buena.**

**LA CONCLUSION, Y ES LA QUE LA PRUEBA VENIA A BUSCAR: CERO de las 15 caidas es
por calibracion de señales.** Ninguna señal rechaza nada: las señales bloquean,
y bloquear no es tumbar. **Las 15 caen por dos reglas de ESTA casa**, que son
mas estrictas que las que aquella campaña aplico:

1. **`docs/REGLAS_DE_ID.md`** (13 de las 15, y 917 en el catalogo entero).
2. **D.12, cero guiones largos** (2 de las 15, y 48 en el catalogo).

**Eso NO se arregla moviendo un umbral, y no se arregla sin el fundador.** Va a
la seccion 8 como decision abierta.

## 7. LO QUE ESTA CALIBRACION DEJA DICHO SOBRE LA JERARQUIA

**Ninguna de las tres señales separa un par de jerarquia declarada de un par al
azar.** Con los umbrales nuevos, la jerarquia declarada se levanta asi: señal 1
el 1,4 por ciento, señal 2 el 4,6, señal 3 el 3,0.

**Esto no se arregla bajando umbrales**, y la medicion lo prueba: para levantar
el 40 por ciento de la jerarquia haria falta la señal 3 en 0,45, y ahi la cola
falsa es de **523 vecinos por candidato**. **Se leeria ruido, no jerarquia.**

**Dos precisiones para que esta conclusion no se lea mas ancha de lo que es:**

- La clase medida es **arista declarada**, que es mucho mas ancha que la figura
  del hijo (la madre que nombra en una linea lo que el hijo despliega en siete).
  La mayoria de las aristas del catalogo son secuencia de proceso, no expansion
  de linea. **La figura estrecha SI la caza la señal 3**: el fixture del hijo
  mide 0,658, muy por encima del p99 de la jerarquia general (0,644).
- El manual ya lo sabia y lo escribio en su principio 4 con sus propias cifras
  (vocabulario compartido, 3 por ciento de precision). **Esta calibracion no
  descubre la debilidad: la mide en esta casa.**

> **CONSECUENCIA ESCRITA: la aduana caza duplicados, y la jerarquia la caza la
> LECTURA.** Un candidato que entra con la cola vacia no esta certificado como
> sin madre: esta certificado como sin gemelo. Por eso
> `docs/loop/EXTRACTOR.md` manda buscar la madre POR LECTURA cuando el candidato
> despliega algo que el libro ya nombro.

## 8. LO QUE QUEDA PARA EL FUNDADOR

**1. LOS 917 IDS DEL CATALOGO QUE ROMPEN LAS REGLAS DE ID DE ESTA CASA (28,9 por
ciento).** El grueso son preposiciones y articulos (768), del estilo
`buen_lugar_para_trabajar` o `pensar_en_grande_empezar_pequeno`. Tres caminos:

- **(a) LAS REGLAS SE QUEDAN Y EL ID SE REESCRIBE AL ENTRAR**, con el id viejo en
  `ids_alias`. **Es la que recomiendo, y no pide regla nueva ninguna:** para eso
  existe `ids_alias`, el resolutor camina la cadena y no se pierde ninguna
  busqueda. Cuesta renombrar, y ese trabajo es del extractor.
- **(b) LAS REGLAS SE AFLOJAN PARA LO IMPORTADO.** No la recomiendo: es inventar
  una regla en caliente para que quepa un lote, que es justo lo que el manual
  prohibe.
- **(c) LAS REGLAS SE AFLOJAN EN GENERAL.** Es legitimo y es tuyo, pero pide su
  propia medicion: la regla 3 nacio porque la variante por preposicion es la
  forma mas barata de fabricar un gemelo invisible.

**2. LOS 48 NODOS CON GUION LARGO (1,5 por ciento).** Hoy la aduana los RECHAZA.
Como un guion es FORMA y no doctrina, **la aduana podria normalizarlos en la
puerta** igual que ya normaliza el id (D.7). Es una linea de codigo. **No la
escribo sin ti** porque cambia el texto de un candidato, y reescribir contenido
ajeno en silencio no es normalizar forma: es editar.

**3. SI LOS LOTES DE CUARENTENA VIAJAN EN EL REPO.** Hoy `cuarentena/*/` esta
ignorada. Detalle y motivo en `cuarentena/LEEME.md`.

---

## 9. LOTE 1: LA CALIBRACION CONTRA TRABAJO DE VERDAD (10 sep 2026)

**Las secciones 1 a 8 calibraron las señales contra un catalogo YA HECHO.** Esta
calibra otra cosa: **el trabajo de extraer**, medido sobre el primer lote real de
esta casa, `onu_consumidor` (`D.24`, lote de calibracion).

> **Cuenta entera en `docs/CIERRE_LOTE_1.md`.** Aqui van las cifras, que es donde
> las busca quien vuelva a calibrar.

### 9.1. Las cuatro medidas

| medida | cifra del lote 1 | como se conto |
|---|---|---|
| **candidatos por mil palabras** | **4,97** sobre palabra minada; **3,42** sobre libro entero | 6 candidatos / 1.208 palabras de `cap_02` mas `cap_03`; 6 / 1.755 del libro con sus cuatro ficheros |
| **pasos inventados por lote** | **13 de 36, el 36 por ciento** | relectura parrafo a parrafo en la vuelta 2. Cuatro de los seis candidatos llevaban al menos uno. El lote quedo en 32 pasos |
| **veredictos escritos** | **1** en seis inserciones, y **1 de 1 fue invisible para las tres señales** | `bitacora/VEREDICTOS.jsonl`, 10 sep 2026 |
| **coste por capitulo** | **9,73 USD** por capitulo tocado (3), **16,64 USD** por mil palabras | 29,20 USD y 86,5 minutos en dos vueltas de dos asientos, leidos de los testigos del arnes |

**El desglose del coste:**

    vuelta 1   extractor  7,01 USD  1178 s      vuelta 2   extractor  7,41 USD  1305 s
               auditor    6,63 USD  1317 s                 auditor    8,15 USD  1393 s

### 9.2. Cual de las cuatro se puede proyectar, y cual no

**LA UNICA QUE SE TRANSFIERE ES EL 36 POR CIENTO DE PASOS INVENTADOS**, porque
**no es una propiedad del libro sino de la mano que escribe.** Es la que `D.30`
convierte en regla y la que el lote 2 va a comprobar.

**LAS OTRAS TRES NO, y el motivo esta medido:** los capitulos del lote 1
promedian **439 palabras**; los 160 que quedan promedian **3.517**, **ocho veces
mas**. El lote 1 es el **0,3 por ciento** del corpus restante (1.755 palabras
contra 562.648).

| proyeccion del coste sobre lo que queda | cifra |
|---|---:|
| por capitulo tocado (9,73 x 160) | ~1.560 USD |
| por mil palabras (16,64 x 562,6) | ~9.360 USD |

**SEIS VECES DE DIFERENCIA. La cifra por palabra es la menos mala y aun asi esta
inflada**, porque las dos vueltas gastaron mucho en doctrina que no se repite.

**Y LA TASA DE CANDIDATOS NO SE PROYECTA EN ABSOLUTO:** a 4,97 por mil saldrian
2.796 candidatos, cifra no creible. El texto normativo es denso y terso; un libro
de gestion gasta muchas mas palabras por procedimiento.

### 9.3. El reparto de los puentes, que dice donde mirar

| parrafo | inventario propio | puentes |
|---|---|---:|
| 29, cinco medios nombrados | rico | **0 por ciento** |
| 32, una frase | pobre | **83 por ciento** |

> **UN PARRAFO POBRE NO PRODUCE UN NODO POBRE: PRODUCE UN NODO INVENTADO.**

### 9.4. La metrica de volumen del lote 2, y su regla de escalada

*Decision del fundador del 10 sep 2026.* El lote 2 corre a **DOS capitulos por
vuelta**, y **cada acta del auditor publica `PASOS INVENTADOS POR CAPITULO`**:

| lote | volumen por vuelta | puentes medidos |
|---|---|---:|
| 1 | UNO | **36,00 por ciento** |
| 2 | DOS | |
| 3 | TRES | **3,31 por ciento**, firmada el 11 sep 2026 |
| **4 y siguientes** | **CUATRO** | el freno: **por encima del 10 por ciento se baja un escalon** |

**LA LINEA BASE DEJA DE SER EL 36 POR CIENTO** (decision del fundador del 11 sep
2026, punto 5.8). Era la cifra de una casa que empezaba, y el lote 3 la bajo
**once veces**. Comparar contra ella ya no dice nada: **el freno es ahora un numero
fijo, 10 por ciento, con su salida escrita.**

**LA CIFRA ES POR CAPITULO Y NO POR VUELTA, y eso no es un detalle:** con dos
capitulos por vuelta, una media de vuelta esconderia un capitulo limpio detras de
uno malo. **La escalada se decide sobre el peor capitulo, no sobre el promedio.**

### 9.5. Lo que este lote NO pudo medir

**EL ERROR DE DEJAR PASAR SIGUE SIN MEDIR.** Las dos vueltas del bucle corrieron
con cero inserciones, asi que no hubo veredictos, sin veredictos no hubo `SANO`, y
sin `SANO` no hubo muestra pineada: **dos tandas con poblacion cero**. Con los
seis nodos ya dentro, **la vuelta siguiente es la primera que puede medirlo**.
