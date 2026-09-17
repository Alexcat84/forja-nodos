
---

# ACTA DEL FRENTE `marquet_turn_the_ship`, VUELTA 1: la frontera de `cap_03` **me cierra al digito contra mi propio instrumento**, sus **tres discutibles se sostienen los tres**, sus **8 puentes retirados en el acto los verifico uno a uno** y `PASOS INVENTADOS` sale **0,00 en las tres filas**. Y aun asi: **el reporte se quedo en la TAREA 1 con las otras dos declaradas ABIERTA en su propia tabla**, y **mientras yo auditaba, el arnes corrio una SEGUNDA fase ciega sobre este mismo arbol, sello una apertura distinta encima de la mia y lanzo un SEGUNDO turno de auditor**. **MI SELLO ESTA ROTO Y NO LO ROMPI YO: EL BUCLE SE DETIENE**

*Escrita el 16 sep 2026. Frente en paralelo (`D.45`), **MODO AUSTERO** (`D.47`): nada que el
registro ya diga, cifras talladas, discutibles por numero y linea.*

> **NO LLEVA NUMERO DE ACTA, Y ES DELIBERADO.** La ultima acta de este arbol es la `ACTA 30`
> (vuelta 31). La `ACTA 31` existe, **pero en la otra rama** (`8e453d3` de
> `extraccion-mundo-11`), y numerarme `31` o `32` desde aqui **seria contestar la pregunta de
> herencia de registro que el fundador acaba de subirse a si mismo** (seccion 8, motivo 3). Me
> nombro por frente y por vuelta, que es lo unico que no decide nada.

## 0. HUECO DE ACTA, y va antes que nada (`AUDITOR_FORJA.md` 1.0)

**HAY HUECO EN ESTA RAMA Y NO LO CUBRO, Y ESO TAMBIEN LO DECLARO.** La ultima acta de este
arbol cubre la **vuelta 31**; la **vuelta 32** corrio en esta rama por herencia de commits
(`6dee045` a `4ca7c58`) y **aqui no tiene acta**. La tiene en la linea de insercion: `8e453d3`,
`ACTA 31, VUELTA 32: PARADA POR CREDITO ROTO`.

**No la re audito, y el motivo es de doctrina y no de pereza:** la vuelta 32 es de
`scott_radical_candor` y de la linea que inserta, **no de este frente ni de este libro**, y
auditarla desde aqui es exactamente el cruce que el `DICTAMEN` del fundador de las `22:28`
nombra como el defecto que paro a los otros tres frentes. **Va en la parada, seccion 8.**

## 1. LO QUE VERIFIQUE, CORRIDO POR MI EN ESTA VUELTA

| instrumento | salida |
|---|---|
| `python forja.py gate` | `.marquet_a1/guardas_auditor.txt` |
| `python forja.py guiones` | `.marquet_a1/guardas_auditor.txt` |
| `python tests/test_aceptacion.py` | `.marquet_a1/guardas_auditor.txt` |
| mi tallado celda a celda de la frontera de `cap_03` | `.marquet_a1/frontera_verificada.txt` |
| mi censo de pasos de los nueve | `.marquet_a1/censo_auditor.txt` |
| mi poblacion de barrido | `.marquet_a1/poblacion_auditor.txt` |
| mi mutacion de las tres guardas de puerta | `.marquet_a1/mutacion_guardas.txt` |
| mi poblacion de la muestra pineada | `.marquet_a1/pineada_poblacion.txt` |
| el estado del arnes al cerrar mi turno | `.marquet_a1/arnes_concurrente.txt` |

    GATE VERDE.
      nodos verificados: 270
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
      total: 201 pruebas, 0 fallos, 0 errores

| | | mi comando |
|---|---:|---|
| nodos en `dataset/nodos.jsonl` | **270** | `wc -l` sobre el fichero |
| lineas en `bitacora/VEREDICTOS.jsonl` | **396** | `wc -l` sobre el fichero |
| candidatos en la bandeja del lote | **9** | cuenta de `.json` de la carpeta |
| **inserciones de esta vuelta** | **CERO** | `270` al abrir (`dbff694`) y `270` al cerrar |

**LAS CINCO CIFRAS DE APERTURA DEL REPORTE ME SALEN AL DIGITO CONTRA GIT**, y no contra su
palabra: `270` nodos, `3` candidatos en bandeja y `dbff694` los leo de
`git show dbff694:dataset/nodos.jsonl` y de `git ls-tree dbff694`. Las `17` unidades no estan en
git, porque `.gitignore` linea 13 ignora las carpetas de corpus, y las cuento del arbol.

### 1.1. LA FRONTERA DE `cap_03`, TALLADA CELDA A CELDA POR MI INSTRUMENTO

**Las 16 filas (nombre, rango, palabras) las leo de la tabla `1.b` del reporte; las palabras las
cuento del fichero.**

    piezas                                   : 16
    suma declarada                           : 1978
    wc -w del cuerpo (L8 en adelante)        : 1978
    celdas que DIFIEREN                      : NINGUNA
    lineas de cuerpo con palabras sin cubrir : []

**LAS DIECISEIS CELDAS DE CUENTA SON LAS DEL FICHERO, UNA A UNA.** Y las `30` palabras que
separan el `wc -w` del fichero (`2008`) del cuerpo (`1978`) son el encabezado `YAML` de `L1` a
`L7`: las cuento y son `30`.

**Y COINCIDE CON MI CORTE CIEGO, que es la mitad que importa:** mi frontera sellada corto `18`
piezas `P` y `19` piezas `R` por linea; sus `7` piezas `P` agrupadas contienen exactamente mis
`18`, ningun candidato declara una linea que yo no tenga, y las dos lineas de residuo que sus
candidatos declaran (`L17`, `L29`) las declaran **a la cara y con su motivo**.

### 1.2. LAS TRES GUARDAS DE PUERTA, RE CORRIDAS POR MUTACION (cosecha `7.C`)

**El reporte no declara ninguna guarda mordiendo**, asi que no hay caso rojo automatico que
sacar de el; **las dos caidas `CAERIA` que si hubo viven en los papeles del extractor y no en
ninguna sede**. Las muerdo yo, sobre copia en memoria y sin tocar la bandeja:

      el candidato TAL COMO ESTA en la bandeja      PASA las cuatro guardas
      MUTACION 1: sin el campo 'fuentes'            CAE: no cumple esquema/nodo.schema.json
      MUTACION 2: preposicion prohibida en el id    CAE: rompe docs/REGLAS_DE_ID.md (regla 3)
      MUTACION 3: clave fuera de la tabla canonica  CAE: LA FUENTE ES UN CAMPO SAGRADO

**LAS TRES MUERDEN**, y la primera reproduce literalmente el mensaje que el intento 1 de la
vuelta registro (*falta el campo obligatorio fuentes*).

## 2. RELECTURA CIEGA: LOS TRES DISCUTIBLES MARCADOS, POR SU NUMERO

*Empiezo por ellos porque es lo que `5.1` manda. **Mi clase estaba escrita y sellada antes de
abrir el reporte.***

| # | pieza | lo que decidio la vuelta | **lo que adjudico** |
|---:|---|---|---|
| 1 | `R5`, `L35` | fuera: nombra sintoma y techo, sin medio de deteccion | **SE SOSTIENE** |
| 2 | `R7`, `L61` | fuera con inventario de seis, por la restriccion 1 de `D.27` | **SE SOSTIENE** |
| 3 | una unidad y no dos, por el coste de la aduana | cierre corto declarado con su cifra | **SE SOSTIENE** |

**`1`.** `L35` describe un estado (*hunker-down mode*, *satisfying the minimum requirements*) y
**no pone ni un medio**: quien escribiera el paso lo escribiria de su cabeza. Es la cara
negativa de `D.27` sin necesidad de su restriccion. **Mi frontera ciega tambien la corto `R`.**

**`2`.** Es el caso dificil y la vuelta lo dijo asi. `L61` enumera seis: *drunken driving
citations, liberty incidents, physical fitness failures, tagout errors, rework, a reactor
problem*, **todas precedidas de `avoid`**. `D.27` restriccion 1 es literal: *un inventario de
METAS o de FINES no cuenta: nombrar adonde hay que llegar sigue siendo nombrar*, y su ejemplar
`19 de cap_01` (*cuatro desenlaces*) **es la misma figura**. Adjudico **citando la regla y su
ejemplar, sin ensanchar ni estrechar la vara** (`6.3`). **Mi frontera ciega tambien la corto `R`.**

**`3`.** El encargo de este frente pone el techo **en candidatos, no en capitulos**: *entre
cinco y quince*, y *si una unidad sola lo pasa, la vuelta cierra en esa unidad*. `cap_03` dio
**6**, que esta dentro, asi que **el cierre corto no lo obliga el techo**: lo obliga el coste, y
la vuelta lo midio antes de escribir el primer candidato (`4m2.801s` por candidato, con su
`time` pegado). **`EXTRACTOR.md` 17 escribe el ritmo en una linea:** *un capitulo por vuelta, no
el libro*. **Y lo que a mi me tocaba verificar es que lo declarase con su cifra**
(`AUDITOR_FORJA.md` 8.1): lo declara en `1.a` y lo mide en `1.c`. **No es caida.**

### 2.1. LA POBLACION `348` DEL REPORTE CONTRA MI `354`: NO ES DISCREPANCIA

La cronometro de `1.c` dice `348 = 270 + 78`; mi barrido de hoy dice `354 = 270 + 84`. **Es el
mismo instrumento en dos momentos**: `78` era `75` de `scott` mas los `3` de `marquet` antes de
escribir los seis; `84` es `75` mas los `9` de ahora. **Lo digo en vez de apuntarlo como
choque**, que es lo que costaria la cifra.

## 3. `PASOS INVENTADOS POR CAPITULO` (`AUDITOR_FORJA.md` 8). **NO ES OPCIONAL, Y LA FIRMO YO**

**El denominador es de mi censo, corrido hoy. El numerador es mi lectura**, la de mi fase
sellada sobre los setenta pasos, mas cinco relecturas de esta fase contra su parrafo.

| unidad | nodos | pasos escritos | **PUENTE** | **PASOS INVENTADOS** |
|---|---:|---:|---:|---:|
| `cap_01` | 1 | **7** | **0** | **0,00 por ciento** |
| `cap_02` | 2 | **10** | **0** | **0,00 por ciento** |
| `cap_03` | 6 | **53** | **0** | **0,00 por ciento** |
| **el lote `marquet_turn_the_ship` entero** | **9** | **70** | **0** | **0,00 por ciento** |

| | |
|---|---:|
| **la fila que decide, que es la peor** | `cap_03` con **0,00** |
| tope | **10,00** |
| **el freno** | **NO SE ACTIVA** |

**LO QUE UN `0,00` ESCONDE, Y POR ESO VA PEGADO:** la vuelta **escribio y retiro 8 puentes en el
acto**, siete de la especie *el medio* y uno de *destinatario invertido*. **Los verifico los
ocho uno a uno contra el JSON de la bandeja y los ocho estan corregidos.** `8.4` es explicita:
**eso es la regla funcionando, no una caida**, y un extractor que declara sus puentes trabaja
mejor que uno que declara cero.

**LAS CINCO RELECTURAS DE ESTA FASE, contra su linea y no de memoria:** `contar_firmas` paso 5
(la cadena de siete de `L39`, *Seven people!*, siete puestos en el orden del texto),
`auditar_formacion` paso 9 (`L55`, *there was no photographer, so we lost the chance to promote
these accomplishments*), `inspeccionar_reparto` pasos 7 y 8 (`L53`, las dos mitades literales) y
`observar_reunion` paso 1 (`L17`, *a routine review of maintenance issues*). **Las cinco se
sostienen como TRANSCRIPCION.**

**Y LA QUE EL REPORTE NO PUBLICA ES ESTA MISMA TABLA:** de eso trata la seccion 5.

### 3.1. LAS DOS FRONTERAS INCOMPLETAS, ADJUDICADAS

Mi fase sellada caza dos pasos apoyados en una linea que su resumen no declaraba
(`encargar_meta` paso 2 contra `L51`, `cambiar_forma` paso 4 contra `L27`). **Adjudico que NO
son puente y que la especie es otra: FRONTERA INCOMPLETA.** La linea existe, es del libro y es
de la misma unidad, y `D.30` mide *pasos que el extractor puso y el libro no dice*. **El
numerador de `cap_02` se queda en `0`.** Las dos estan declaradas y corregidas dentro de su
candidato, sin borrar el texto viejo.

## 4. LA MUESTRA PINEADA DE LOS SANOS (`AUDITOR_FORJA.md` 7)

    LINEAS QUE NOMBRAN UN ID DE LA BANDEJA marquet : 0
    VEREDICTOS *SANO* ESCRITOS POR ESTA VUELTA     : 0
    POBLACION DE LA MUESTRA PINEADA                : 0

**POBLACION CERO, Y NO SE INVENTA UNA MUESTRA DONDE NO HAY POBLACION** (7, ultimo parrafo).
Este frente no inserta (`D.45`), asi que no escribe veredicto ninguno. **Lo que ocupa su sitio
es el barrido de mi fase sellada**, que midio los nueve contra `GRAFO MAS BANDEJAS` y levanto
`21` vecinos, **ninguno de ellos un nodo del grafo**.

## 5. LAS CAIDAS, POR ESPECIE Y CON NOMBRE

### 5.1. **CAIDA 1, especie `REPORTE`, del extractor: la vuelta cerro sin cerrar su reporte**

**EL HECHO, medido:** el reporte abre la vuelta en su linea `36041` y **se acaba dentro de la
TAREA 1**. Su propia tabla de tareas publica **`TAREA 2` ABIERTA** y **`TAREA 3` ABIERTA**, y
**`PASOS INVENTADOS POR CAPITULO` no aparece en ninguna parte del reporte**.

**LA REGLA QUE LO NOMBRA ES LITERAL** (`AUDITOR_FORJA.md` 8.3, punto 3): *si el reporte no
desglosa por capitulo, eso es una caida de especie REPORTE y la nombras: la cifra agregada no se
puede desglosar despues.* **Aqui no desglosa ni agrega: no publica.**

**ACUMULA**, porque la celda vive en **TABLA de CABECERA** y no en prosa de acompaniamiento
(`5.2`).

**Y VA CON LO QUE LA ATENUA, porque el acta no es un expediente:** el trabajo **se hizo y lo he
verificado entero**. Los seis candidatos estan escritos y con su aduana por candidato (`0
CAERIA`), los 8 puentes estan retirados, la fidelidad esta releida fila por fila en los papeles
del extractor, y el turno acabo **esperando dos corridas de aduana que no llegaron**, declarado
asi en el `loop.log`. **El danio es a la sede, no al dato:** el reporte de esta vuelta no publica
lo que la vuelta midio, y `8.3` dice por que eso no se recupera pidiendolo la vuelta siguiente.

**LO QUE NO LE CARGO:** que el candidato `cambiar_forma_trabajar_conservar_plantilla` cite la
apertura ciega por dentro de su resumen. La sede es un `resumen_teorico` de la cuarentena, que
no es ninguna de las de `5.2`, y **el extractor declaro el credito en vez de quedarselo**. Eso
no es suyo: es del arnes, y va en la parada.

### 5.2. **LA RACHA: la abro en `1 de 3` PARA ESTE FRENTE, y digo que eso mismo es la pregunta**

| especie | esta tanda | **racha del frente `marquet_turn_the_ship`** |
|---|---|---|
| `CLASE` | **0** | **0 de 2** |
| `CIFRA PUBLICADA` | **0** | **0 de 2** |
| `REPORTE` | **1** | **1 de 3** |

**NO ARRASTRO EL `2 de 3` DE LA LINEA DE INSERCION, Y NO ES QUE ME LO PERDONE: ES QUE NO SE SI
ES MIO.** `5.2` dice que la racha del extractor y la del auditor **se cuentan aparte** con este
motivo escrito: *una racha mezclada no dice de quien es el problema*. Las tres tandas que la
racha heredada cita son de `cap_11` de `scott_radical_candor`, **que no es el libro de este
frente ni lo corrio esta mano**. **Pero no me adjudico la lectura:** el fundador se subio esta
pregunta a si mismo hoy a las `22:28` y dijo que es doctrina. **Va entera a la parada, y si
Alexis lee que si se hereda, esta tanda cierra la racha en `3 de 3`.**

**NO LA REINICIO NI PUEDO** (`5.4`): la reinicia una decision de Alexis escrita en la carpeta de
paradas, **y ninguna de las dos es el auditor**. Lo que digo es que **este frente no habia
corrido ninguna tanda antes de hoy**, no que la otra racha se borre.

### 5.3. **MI PROPIA CAIDA, con mi nombre, y la unica que encontre**

**Mi apertura sellada dice en `0.3` que los ocho instrumentos de su seccion 1 estan corridos EN
ESA FASE. Uno no lo estaba.** La salida que publico para su seccion 6 **lleva hora `21:15:27`** y
mi fase no se abrio hasta las `21:44:27`.

**LO CORRI HOY Y SALE IDENTICO AL BYTE** (`.marquet_a1/poblacion_auditor.txt`, comparado sin una
sola diferencia): `515`, `84`, `270`, `354`. **Asi que la cifra no es falsa, y `CIFRA PUBLICADA
PROPIA` pide que lo sea.** Y `REMEDIO ROTO` pide sustancia de auditoria: el remedio dice *la
corro yo en esta vuelta*, y esa corrida **cae dentro de la vuelta** aunque no dentro de mi fase
ni de mi mano.

**NO ME LA CARGO, Y DIGO EXACTAMENTE POR QUE, PARA QUE SE ME PUEDA CONTRADECIR:** lo falso es la
frase de procedencia, no la cifra, **y una frase de procedencia falsa en mi apertura no tiene
casillero en `5.2`**, que me da dos especies y ninguna encaja. **Inventarme una es doctrina, y
eso es parada.** Lo subo con lo demas. **Y no cambia ningun desenlace:** si Alexis la lee como
`CIFRA PUBLICADA PROPIA`, mi racha de este frente va de `0` a `1 de 3` y no para nada.

**LAS OTRAS CIFRAS DE MI APERTURA LAS RECOMPUTE HOY Y SALEN AL DIGITO:** `4644 = 9 x 516`,
`517 = 270 + 247`, y la muletilla `19 de 2181` en el grafo contra `58 de 1887` en bandejas.

## 6. LAS SEIS CONDICIONES DE PARADA, REPASADAS UNA A UNA

| condicion (`AUDITOR_FORJA.md` 3) | |
|---|---|
| doctrina nueva necesaria | **SE CUMPLE**, y por dos sitios (parada, motivos 3 y 4) |
| contradiccion con regla o cifra vigente | **SE CUMPLE**: mi sello (parada, motivo 1) |
| decision de Alexis reservada | **SE CUMPLE**: el registro que hereda un frente |
| fallo tecnico repetido dos vueltas | no se cumple: es la vuelta 1 de este frente |
| credito roto | **NO PUEDO DECIDIRLO**, y ese es el motivo 3 |
| campania consumada | no se cumple: `cap_03` de `17` |

## 7. LO QUE QUEDA MEDIDO Y EN VERDE AL CERRAR MI TURNO

`gate` VERDE con `270` nodos, `guiones` VERDE, `201` pruebas con `0` fallos, `396` lineas de
bitacora sin una sola de este frente, `9` candidatos en bandeja y **cero inserciones**. **El
trabajo de la vuelta esta entero en el arbol**: lo que falta es su reporte.

## 8. LA PARADA

**Escrita en `docs/loop/PARA_ALEXIS.md`** con los cuatro motivos, el estado exacto y como
retomar. **`docs/loop/PROMPT_SIGUIENTE.md` queda VACIO**, que es lo que la seccion 3 manda.
