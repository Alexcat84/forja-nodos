# ENCARGO DE LA VUELTA 79: **SANEAMIENTO. LA RELECTURA CONJUNTA DE UNA FRONTERA DE MARQUET, EL TEXTO DE LA OTRA DEJADO LISTO, Y SEIS DEUDAS DE LOS LIBROS DE LA CAMPANIA PAGADAS O DICHAS: `d150`, `d180`, `d098`, `d104`, `d099` Y `d135`. NO SE INSERTA NADA Y NO SE TOCA NI UN BYTE DE LA BANDEJA DE MARQUET** (`ACTA 77` `77.5`, `77.10`)

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 77`, que audito la vuelta `78`.
`AUDITOR_FORJA.md` seccion `1.4`. **Toda cifra de medida de esta pagina va dentro de un bloque `$` con su salida, o lleva en
su misma linea la seccion de la `ACTA 77` donde esta pegada** (`R8`, `ACTA 77` `77.11`).*

> # **LIBRO DE ESTA VUELTA: `marquet_turn_the_ship`**
> # **CLASE DE ESTA VUELTA: SANEAMIENTO**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **POR QUE ESTA VUELTA NO INSERTA, Y LO DICE EL INSTRUMENTO**

@@RUN:0::python scripts/deuda.py --clase 79@@

**La cadencia la cuenta el registro, no el encargo** (`D.58`): esta vuelta **no inserta nada**. Las fichas de Marquet que dejo
listas la `78` entran en la vuelta siguiente, contra la huella que la `78` sello y la `ACTA 77` reprodujo (`77.4`). **Por eso esta
vuelta no toca `cuarentena/`**: una ficha que cambie ahora deja sin valor su barrido y su huella (`d031`).

@@RUN:0::python forja.py tablero --puedo marquet_turn_the_ship@@

**La frase de *continuar desde `cap_17`* es de extraccion y no aplica**: el frente de Marquet se cosecho y la extraccion del mundo
`11` esta cerrada (`PARALELO.md` seccion `8` punto `3`). Las deudas de Gerber leen nodos de `gerber_emyth`, que esta `INSERTADO`:
**leerlos no es tomar ese libro**, y no se escribe nada suyo.

**PUEDES LANZAR TRABAJOS DE FONDO, PERO NINGUNO VIVO AL CERRAR TU TURNO**: los recoges todos dentro, vigilandolos si tardan.
**Si no te caben, no los lances: lo dices en el reporte.** Y **NINGUN `insertar`**, ni en primer plano ni de fondo.

**Las deudas que paga esta vuelta**, tal como estan en el registro:

@@RUN:0::python scripts/deuda.py | grep -E "^  (d098|d099|d104|d135|d150|d180|d183) "@@

**Su texto entero esta en `docs/loop/DEUDA.jsonl`**, y lo lees entero antes de pagar ninguna. **`d183` NO se paga aqui**: es la
de la frontera de la TAREA `2`, y se paga en la vuelta que inserte.

---

## TAREA 1: **REGISTROS DE LA `ACTA 77`**

En una tabla corta y sin reabrir el argumento (`D.47`):

| que | donde |
|---|---|
| **Tu vuelta, reproducida**: movio las `2` fichas corregidas y nada mas de dato; tus nueve instrumentos dan lo que pegaste y el cierre estricto del auditor sale verde | `ACTA 77` `77.0`, `77.1` |
| **Tu fidelidad, tu barrido, tus lineas, tu arista y tu orden, cruzados enteros contra mi lectura sellada**: ninguna diferencia de clase, de fila ni de arista | `77.3`, `77.4` |
| **Tus catorce discutibles se sostienen**, `D78.1` a `D78.14`; mis dos dudas de `cap_03` se cierran `T` por la figura de `D76.8` | `77.5` |
| **Tus dos fronteras declaradas**: la de Grove se sostiene y se agenda como `d183`; la de Zhuo va a relectura conjunta (TAREA `2`) | `77.5` |
| **`d150` firmada en su sustancia**: tu fila de `cap_03` es la que pedia | `77.3` |
| **Cero caidas tuyas**; `R5` y `R9` cumplidos | `77.0`, `77.2`, `77.7` |

## TAREA 2: **LA RELECTURA CONJUNTA DE LA FRONTERA DE ZHUO, Y EL TEXTO DE LAS FRONTERAS DEJADO LISTO** (`1.3`, `6.1`, `77.5`)

1. **La de Zhuo, a relectura conjunta.** Tu fila de `.v78ext/aristas_lectura.txt` lee `comunicar_valores_diez_formas` (de
   `zhuo_manager`, en el grafo) contra `repetir_mensaje_invariable_diario_reunion_evento` (bandeja) como **FRONTERA DECLARADA**; mi
   lectura ciega la leyo **sin contradiccion**, y mi caso, con su evidencia, esta en la `ACTA 77` `77.5`. **Decides tu, con la vara
   `6.1` y solo esa**, con los pasos de los dos delante (`python .v64aud/pasos.py <a> <b>`) y `cap_13` `L119` pegado de un `grep -n
   -o`. Escribes tu decision con su razon; **si gana la mia, tu fila se corrige por correccion declarada en tu reporte, sin borrarla**.
2. **El texto de cada frontera que quede en pie, preparado y NO escrito**, en un fichero de `.v79ext/`: las dos posiciones con sus
   fuentes (el paso de cada nodo y la linea del libro, cada una con su `grep -n -o` pegado), empezando por `CORRECCION DECLARADA`,
   para que la vuelta que inserte lo pase tal cual a `python forja.py corregir --nodo <id> --anade "..." --razon "..."` **despues de
   que el nodo de Marquet entre**. **La de Grove** (`delegar_tarea_base_comun_seguimiento` contra
   `eliminar_seguimiento_descendente_responsabilizar_dueno`) **esta sostenida** (`77.5`) y va siempre; la de Zhuo, solo si tu
   decision la deja en pie. **No corres `corregir` en esta vuelta**: los dos nodos de Marquet no viven en el grafo.
3. **Marca discutible lo que dudes, al escribirlo.**

## TAREA 3: **`d150` Y `d180`, LAS DOS DEUDAS DE LA CAMPANIA QUE YA TIENEN SU PRUEBA**

1. **`d150`**: su sustancia era la fila de fidelidad de `cap_03` de Marquet que el frente nunca publico bien. **Tu fila de la `78`
   la da**, contada entera paso a paso, y la `ACTA 77` `77.3` la firma con mi lectura sellada al lado. **Lo que queda de su letra** (las
   tareas `2` y `3` del reporte de la vuelta `1` del frente, desde los papeles de `.vm01/`) **no se escribe**: es el reporte archivado de
   un frente cosechado, y la relectura entera de la `78` lo sustituye. **Lo mides antes de pagar**: que `.vm01/` sigue intacto, con
   `find .vm01 -type f | wc -l`, que la cita de `d150` cuenta en ficheros, y lo pegas. Paga citando `78.2.4` y la `ACTA 77` `77.3`.
2. **`d180`**: el tablero llamaba `COSECHADO` a un libro cosechado con la bandeja en cero y sus nodos en el grafo. **Se paga por
   medida, no por memoria**: `python forja.py tablero` pegado, con `grove_high_output` y `gerber_emyth` en `INSERTADO`; `git log
   --format="%h %cI %s" -1 -- src/tablero.py`, pegado, que da el commit que lo cambio; y **no tocas `src/`** (`7.F`, `D.55`). Si el
   tablero no los da `INSERTADO`, no la pagas y lo dices.

## TAREA 4: **`d098`, `d104`, `d099` Y `d135`: LOS PUNTEROS DE GERBER, CON EL LIBRO YA ENTERO EN EL GRAFO**

Gerber esta `INSERTADO` (bloque de la seccion `0`) y su extraccion esta cerrada para siempre (`PARALELO.md` seccion `8` punto `3`).
Cada una se lee entera en el registro y se contesta **contra el grafo de hoy, con instrumento**:

1. **`d098` y `d104`** son punteros de `D.37`: *si nace la cabeza, la arista se declara entonces*. **Mide** si algun nodo del grafo es
   cabeza de las fases de crecimiento que `cap_05` `L29` nombra o de las palabras que nombra `cap_12` `L21`, con un `grep` sobre `dataset/nodos.jsonl` pegado
   con su salida. **Si no nacio ninguna**, se pagan diciendo que no nacio y que el libro ya no se extrae; **si nacio alguna, no la
   pagas y la traes**: una arista que falta en el grafo es de la `ACTA 78`, no tuya.
2. **`d099`** pregunta donde nace el nodo de la delegacion de Gerber. **Mide** que nodo del grafo sale de `cap_18` y habla de delegar,
   con su `grep` pegado, y **lee sus pasos** contra `cap_18` `L345` a `L349`. Se paga nombrando el nodo, o diciendo que no nacio.
3. **`d135`** dice que los tramos de `cap_03` de Gerber que nombra estan leidos y descartados con su motivo, *para la vuelta que inserte*.
   **Mide** cuantos nodos de `gerber_emyth` del grafo citan `cap_03` como su origen, con su `grep` pegado, y se paga con esa medida:
   si ninguno, esos tramos quedan leidos y descartados en la `ACTA G9` y no hay nada que la insercion tuviera que mirar.
4. **Paga con `python scripts/deuda.py --pagar <id> --vuelta 79 --como "..."`**, con cada `como` en un fichero de `.v79ext/`. **Si una no
   se puede pagar con su medida, no la pagas: lo dices con su fila.**

## TAREA 5: **EL CIERRE**

- **Declara la vuelta**: `python scripts/deuda.py --saneamiento --vuelta 79`, pegado (`d085`). Sin eso, la `80` vuelve a salir
  `SANEAMIENTO`.
- **El censo antes y despues**, con una copia de `.v78ext/censo.sh`: **no se mueve nada de dato.** Grafo, bitacora, pares mutuos,
  bandeja de Marquet e insertados al abrir son los de la `ACTA 77` `77.1`, y al cerrar tienen que ser los mismos.
- **Las fichas de Marquet, byte a byte las que sello la `78`**: `python .v78ext/pasos_y_huellas.py` vuelto a correr, con su salida
  identica a `.v78ext/pasos_y_huellas.txt`, pegado, al abrir y al cerrar.
- **`D.61`**: cada discutible ejecutado o cerrado. Ninguno abierto.
- **`R5`** en cada bloque `$` de tu tramo, medido con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera
  cambiada a la `79`, y pegado.
- **La cabecera, las tablas de tareas y la tabla de cierre: cada cifra de sus celdas sale de un instrumento corrido en esta vuelta.**
- `python forja.py gate`, `python forja.py guiones`, `python tests/test_aceptacion.py` y `python scripts/cerrar_reporte.py`,
  **pegados**. **El cierre estricto tiene que salir en verde: cualquier rojo es tuyo.**
- Commitea `docs/loop/` y tu carpeta `.v79ext/`. **Si nada te obliga a parar, no escribas `PARA_ALEXIS.md`.**

---

## LO QUE NO HACES

- **NO INSERTAS NADA**, y **NO TERMINAS TU TURNO CON NADA VIVO**.
- **NO TOCAS `cuarentena/`**, ni la bandeja de Marquet ni `_insertados`.
- **NO TOCAS `dataset/`, `bitacora/` NI `censos/`**: esta vuelta lee y paga, no mueve dato. **Ni `forja.py corregir`, ni `arista`.**
- **NO TOCAS `src/`, `scripts/`, `config/`, el banco, el arnes, el tablero ni los protocolos** (`7.F`, `D.55`), **ni
  `APERTURA_CIEGA.md`**. Los procesos del fundador que veas vivos en otra copia no son tuyos: ni los tocas ni los esperas.
- **NO PAGAS NINGUNA DEUDA QUE ESTE ENCARGO NO NOMBRE**, **NO PAGAS `d183`**, **NO ABRES NINGUN LIBRO** y **NO CREAS EL TAG**: la
  vuelta que meta la ultima ficha de Marquet es la que cierra la campania (`PARALELO.md` seccion `8` puntos `4` y `5`).

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No
adivines.**
