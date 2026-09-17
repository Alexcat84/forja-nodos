# PARADA DEL BUCLE DEL EXTRACTOR: **CREDITO ROTO, `REPORTE` A `3 de 3`**

*Escrita por el auditor al cerrar la `ACTA 31`, que audita la vuelta 32. Sede del auditor por
`AUDITOR_FORJA.md` 5.6. **El bucle no funde ramas y el bucle no crea remotos.***

**`docs/loop/PROMPT_SIGUIENTE.md` queda VACIO**, que es lo que `AUDITOR_FORJA.md` 3 manda en una
parada, y lo que `config/sedes_vacias.json` reconoce como vacio por protocolo.

---

## 1. EL MOTIVO, EN UNA LINEA Y CON SU REGLA

> **`AUDITOR_FORJA.md` 3, credito roto:** *`REPORTE` tres seguidas de la especie que acumula.*

| tanda | acta | caida de `REPORTE` | racha |
|---|---|---|---:|
| **vuelta 30** | `ACTA 29` | una cita en celda de tabla apunta a la `ACTA 28` y la adjudicacion vive en la `ACTA 27` | **1 de 3** |
| **vuelta 31** | `ACTA 30` | la fila `10` de la tabla de la cabeza de `cap_11` pone un nodo que no es | **2 de 3** |
| **vuelta 32** | **`ACTA 31`** | **el cierre publica `167` pasos de `cap_11` EN EL GRAFO, y el grafo tiene `187` en `16` nodos** | **`3 de 3`. TOPE** |

**Tres tandas CONSECUTIVAS, sin ninguna limpia en medio**, que es lo que `5.2` y la correccion
declarada `D.38.1` exigen para que la racha cuente.

### 1.1. La caida de esta vuelta, con su medida y no con su adjetivo

**Lo que `docs/loop/REPORTE.md` publica en la tabla de su `Y.8.d` y en la cabecera de su `Y.3.f`:**

    | cap_11 en el grafo                          | 14 de 14 candidatos                            |
    | pasos de cap_11 en el grafo                 | 167, los 142 de la vuelta 31 mas los 25 de hoy |
    | PASOS INVENTADOS de cap_11, capitulo entero | 0,00 por ciento sobre 167 pasos, en dos firmas |

**Lo que el dato dice, contado por el auditor en esta vuelta:**

    $ python .v33aud/cap11.py
    nodos del GRAFO con unidad de origen cap_11 : 16
    sus pasos                                   : 187

    los que .v31/orden_cap11.txt NO cuenta en sus 14:
       bloquear_tiempo_pensar_calendario                   6 pasos
       recorrer_rueda_conscientemente_cultura_equipo      14 pasos

**EL `167` ES DE UN INSTRUMENTO QUE MIDE OTRA POBLACION, Y EL INSTRUMENTO LO DICE EN SU PRIMERA
LINEA:**

    ORDEN DEL LIBRO, cap_11, LO QUE QUEDA EN BANDEJA
    poblacion: cuarentena/scott_radical_candor, filtrada por resumen_teorico que cita cap_11.md
    candidatos: 14   pasos: 167

**Y la contradiccion vive dentro del propio reporte:** su tabla de `Y.2.c` nombra
`bloquear_tiempo_pensar_calendario` y `recorrer_rueda_conscientemente_cultura_equipo` como **en el
grafo**, y ninguno de los dos esta entre los `14`.

**LO QUE NO CAE, para que la parada no se lea mas grande de lo que es:** `PASOS INVENTADOS` de
`cap_11` **sigue siendo `0,00` por ciento** (las cuatro firmas dan cero puentes), y **el capitulo SI
cierra en insercion**: la bandeja tiene `0` candidatos de `cap_11`, medido. **Lo que cae es el
denominador, el numero de candidatos y el numero de firmas.**

---

## 2. EL ESTADO EXACTO, MEDIDO HOY

| pieza | valor |
|---|---|
| rama | `extraccion-mundo-11` |
| hash auditado (cierre de la vuelta 32) | `4ca7c58` |
| hash al escribir esta parada | `1861e25` mas los commits de esta acta |
| fase | **lote 4 INSERTANDO.** `cap_11` cerrado; el lote 4 sigue abierto en insercion |
| nodos en `dataset/nodos.jsonl` | **270** |
| pasos del grafo | **2.181** |
| aristas por los dos extremos | **105** y **105**, cero sin reciproco |
| veredictos en `bitacora/VEREDICTOS.jsonl` | **396**, de ellos **14** no consumados |
| bandeja lote 4 (`scott_radical_candor`) | **75** sobre **142**, un **47,2** por ciento insertado |
| bandeja lote 5 (`marquet_turn_the_ship`) | **3**, sin tocar (`D.39`) |
| `python forja.py gate` | **VERDE**, `270` nodos verificados |
| `python forja.py guiones` | **VERDE** |
| `python tests/test_aceptacion.py` | **201 pruebas, 0 fallos** hoy; **200, 0** en el hash auditado |
| `python scripts/tallar_reporte.py --estricto` | **VERDE**, `69` tablas |
| `python scripts/censar_rutas.py` | **VERDE**, `519` rutas |

**NINGUNA GUARDA ESTA EN ROJO. EL DATO ESTA SANO.** Esta parada **no es un fallo tecnico**: es la
regla de credito haciendo lo que se escribio que hiciera.

### 2.1. Las cuatro rachas al parar

| especie | de quien | queda en |
|---|---|---|
| `CLASE` y `DATO MOVIDO` | extractor | **`1 de 2`**, penultimo escalon (`ACTA 31` `4.2`) |
| `CIFRA PUBLICADA` | extractor | **`0 de 2`** |
| **`REPORTE`** | extractor | **`3 de 3`. TOPE, y es el motivo de esta parada** |
| la del auditor, una sola | auditor | **`0 de 3`** al cerrar, **tras pasar por `2 de 3`** (`ACTA 31` `9.1`) |

---

## 3. LO QUE SE NECESITA DE ALEXIS

*Nada de esto lo toca el bucle. Cinco cosas, y las cuatro primeras las pide `D.45` por estar en sedes
unicas mientras corren frentes en paralelo.*

### 3.1. **LA DECISION QUE DESBLOQUEA: reiniciar la racha `REPORTE`, o no**

**`5.4` es explicito: la racha NO se reinicia sola, y no la reinicia el auditor.** *Un auditor que
pone su propia racha a cero se esta absolviendo.* **La reinicia una decision de Alexis escrita en
`docs/loop/paradas/`**, y el acta que retome la citara.

**Lo que el auditor pone delante para que la decision se tome con la medida y no con el adjetivo:**
las tres caidas de la racha son **la misma familia** y ninguna movio un dato. Son **una cita a un acta
equivocada**, **un id equivocado en una celda** y **una poblacion equivocada en una etiqueta**. Las
tres son *dictado suelto*, que es exactamente lo que `5.2` dice que esta racha mide. **La racha esta
haciendo su trabajo; la pregunta es si el remedio ya existe.**

### 3.2. **LA PROPUESTA `1` DEL EXTRACTOR, QUE EL AUDITOR SOSTIENE: `D.41` y el `AVISO`**

> **Que `D.41` diga, en una linea, que un instrumento con una constante tecleada dentro tiene que
> imprimirla en su `AVISO`.**

**La medida que la sostiene, reproducida por el auditor:** la caida de la vuelta 31 salio **VERDE en
el tallado** y estuvo una vuelta entera en pie, porque `D.41` compara la tabla contra el instrumento
**y nada compara el instrumento contra el libro**. Y la version 2 del mismo instrumento, al generar
del dato, **cazo una segunda celda mala que nadie habia pedido**.

**Es una linea en `docs/BANCO_DE_REGLAS.md`, y el banco es sede unica: `D.45` prohibe que la toque
una sesion del bucle.**

### 3.3. **EL `LEEME.md` QUE `D.31` MANDA Y QUE EL LOTE 4 NO TIENE**

    $ for d in cuarentena/_insertados/*/ ; do echo "$d $(ls $d | grep -ci '.md$') md, $(ls $d/*.json | wc -l) json" ; done
      cuarentena/_insertados/onu_consumidor/        1 md,   6 json
      cuarentena/_insertados/scott_radical_candor/  0 md,  67 json
      cuarentena/_insertados/smart_who/             2 md,  59 json
      cuarentena/_insertados/zhuo_manager/          1 md, 136 json

**`D.31` lo manda con estas palabras:** *Un `LEEME.md` en la carpeta del lote archivado nombra cada
candidato con **el commit que lo metio** y su veredicto.* **Los otros tres lotes lo tienen. El lote 4
lleva `67` archivados y ninguno**, y ninguna acta lo habia levantado. **No es de esta vuelta y no es
maquinaria: es el registro que la regla pide, con tres modelos ya escritos en el arbol.**

### 3.4. **LAS DOS PROPUESTAS QUE PIDEN `src/`, registradas y no encargadas**

| # | propuesta | por que sube |
|---:|---|---|
| **3** | que el archivado a `cuarentena/_insertados/` lo haga la aduana y no la mano | toca `src/`, y `D.45` lo prohibe mientras haya paralelo |
| **4** | `censos/series_y_cabezas.md` sigue con **`0`** filas y el grafo tiene **`270`** nodos | `EXTRACTOR.md` 9 dice que **lo escribe la aduana**. Es `src/` |

**Y una que NO sube y queda solo registrada:** medir si el molde de redaccion `lo que el texto dice
que` fabrica cola de lectura. **`66` pasos de `50` nodos sobre una poblacion de `348` lo llevan**,
medido por el auditor a ciegas. **Es un lector nuevo y la moratoria de maquinaria lo cubre.**

---

## 4. COMO SE RETOMA

**Si Alexis reinicia la racha**, el acta que retome escribe el encargo siguiente **abriendo por estas
dos**, que son remedio y no trabajo nuevo:

1. **BLOQUEANTE, y es la escalada de `DATO MOVIDO` en su penultimo escalon** (`AUDITOR_FORJA.md` 5.5):
   corregir la fecha **`17 sep 2026`** que la `TAREA 4` de la vuelta 32 escribio dentro de
   `dataset/nodos.jsonl` y de `bitacora/VEREDICTOS.jsonl` el dia **`16`**. **La via existe y no hay
   que construirla:** `python forja.py corregir`, `D.13`, **sin borrar el texto viejo**. Es la unica
   de las `119` fechas escritas a mano en esas dos sedes que no coincide con la que la maquina estampa
   en su propia linea.

2. **Corregir en `docs/loop/REPORTE.md`, por correccion declarada y sin borrar**, las tres celdas de
   `Y.8.d` y la cabecera de `Y.3.f`: **`16` candidatos y no `14`**, **`187` pasos y no `167`**,
   **cuatro firmas y no dos** (`14` en la `ACTA 28`, `6` en la `ACTA 29`, `142` en la `ACTA 30` y
   `25` en la `ACTA 31`). **El `0,00` por ciento no se toca: es cierto sobre `187`.**

**Lo que NO se retoma sin decision:** nada de `src/`, del banco, del arnes ni de los protocolos
(`D.45`), y ningun umbral de `config/umbrales.json`.

**Y lo que el bucle NO hace en ningun caso:** fundir ramas y crear remotos.

---

## 5. UNA COSA MAS, QUE EL AUDITOR DICE CONTRA SI MISMO

**La `ACTA 30` declaro su tanda limpia y se puso la racha propia a `0 de 3`. No lo estaba.** Publico
**`7`** rotulos con nodo en el grafo donde eran **`8`**, y **lo cazo el extractor** en su
`DISCUTIBLE 1`, marcado a ciegas antes de saber si acertaba. **La `ACTA 31` deshace ese reinicio** y
escribe la racha como `2 de 3` al abrir su tanda.

**Y la `ACTA 31` deja escrito como se rompe ella misma** (`7.4`): el encabezado de una columna de su
apertura sellada dice *en `4ca7c58`* junto a `4` fallos de prueba, y un clon limpio de ese hash da
`0`, porque los cuatro eran de su propia fase ciega. **Eligio la lectura de que no es caida de cifra
y la cito**, pero **si Alexis lee que el encabezado de una columna es la afirmacion, la racha del
auditor tambien esta en `3 de 3` y esta parada tiene un motivo mas.**

**Se dice aqui para que no haya que buscarlo.**
