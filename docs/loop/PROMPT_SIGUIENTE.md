# ENCARGO DE LA VUELTA 3 DEL FRENTE `gerber_emyth`: **`cap_09` Y `cap_10`, EL SEGUNDO HUECO, MAS `cap_12` PARA SEGUIR HACIA ADELANTE**

*Linea `gerber_emyth` (`extraccion-gerber_emyth`, worktree
`C:/Users/AlexDesk/Documents/forja-gerber_emyth`). Escrito por la sesion de chat del 21 sep 2026 al
cerrar la vuelta 2, con la misma autorizacion del punto 3 de la decision del fundador de ese dia que
autorizo escribir este fichero directamente (no hay auditor en este bucle manual). **Se declara la
misma nota que la vuelta 2 trajo**: `EXTRACTOR.md` seccion 14 dice que este fichero es sede del
auditor y no del extractor; se escribe igual porque la vuelta anterior lo pidio con todas las letras
en su seccion 5, y sin ese permiso explicito no se tocaria.*

> # **LIBRO DE ESTA VUELTA: `gerber_emyth`**
> # **CLASE DE ESTA VUELTA: EXTRACCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. EL ESTADO, MEDIDO AL CERRAR LA VUELTA 2 Y NO RECORDADO

    $ git rev-parse --short HEAD
    072b49f... (mas el commit de la vuelta 2, que este mismo cierre añade)
    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl
    346 dataset/nodos.jsonl
    740 bitacora/VEREDICTOS.jsonl
    $ ls cuarentena/gerber_emyth/*.json | wc -l
    10

**La vuelta 2 cerro limpia y sin parada** (`REPORTE.md` seccion `G2`, cierre en `G2.8.d`: las cinco
condiciones de parada repasadas, ninguna se cumple). `cap_05` y `cap_06` quedaron minados a **cero
candidatos cada uno**, firmados por frontera completa (residuo `0`, cero solapes, cero huecos) mas
lectura entera de los dos ficheros y la muestra de fidelidad de `D.58` con semilla `g2` (tambien en
cero, porque no habia paso que muestrear).

**Capitulos ya minados del libro, los seis:** `cap_04`, `cap_05`, `cap_06`, `cap_07`, `cap_08`,
`cap_11`. **Candidatos en bandeja: siguen en `10`**, porque `cap_05` y `cap_06` no aportaron ninguno.

**`cap_01`, `cap_02` y `cap_03` siguen en deuda** (`d094`, anotada en la vuelta 2): no es blocante y
no se tocan en esta vuelta tampoco.

---

## 1. POR QUE ESTOS TRES: `cap_09`, `cap_10` Y `cap_12`

**`cap_09` y `cap_10` son el segundo hueco que queda entre capitulos ya minados**: viven entre `cap_08`
(minado en la vuelta 1) y `cap_11` (minado en la vuelta 1), exactamente el mismo patron que la vuelta 2
cerro entre `cap_04` y `cap_07`. Es la situacion mas barata de auditar que quedaba: frontera conocida a
los dos lados.

**`cap_12` es el primero SIN minar que sigue en orden hacia adelante** una vez cerrado ese segundo
hueco, y `D.58` (regimen ligero) permite hasta **tres capitulos por vuelta con techo de `30`
candidatos**. La vuelta 2 propuso subir de dos a tres capitulos precisamente porque cerro limpia
(`REPORTE.md` `G2.9`), y este encargo aplica esa subida.

**Si un solo capitulo del tramo pasa del techo de `30` candidatos, la vuelta cierra en ese capitulo y
declara el resto para la siguiente** (`EXTRACTOR.md` 12.4, precedencia del techo de candidatos sobre el
de capitulos).

---

## 2. LO QUE ENTREGAS POR CADA CAPITULO

Lo mismo de siempre (`EXTRACTOR.md` 9 a 16), sin novedad de doctrina:

1. **La frontera**, fila a fila contra el fichero, cero solapes y cero lineas sin cubrir.
2. **Los candidatos que el capitulo de**, en `cuarentena/gerber_emyth/<id>.json`, cada uno con su
   `python forja.py informe` corrido en el mismo acto en que se escribe.
3. **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo y no una media.** Si un capitulo da cero,
   la fila se escribe igual como `SIN SUPERFICIE`, y ese capitulo se lee ENTERO (no hay paso que
   muestrear).
4. **La muestra de fidelidad con la semilla de esta vuelta:**

       python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_09,cap_10,cap_12 --semilla g3

---

## 3. LO QUE NO HACES EN ESTA VUELTA

- **NO INSERTAS.** Ni un nodo. `MODO_INSERCION=cuarentena`.
- **NO TOCAS EL ARNES NI LA MAQUINARIA** (`D.45`): `orquestador_forja.sh`, `src/`, `scripts/`,
  `tests/`, `hooks/` y `esquema/` estan vedados. Un defecto se mide y se sube en `PARA_ALEXIS.md` (que
  escribe el auditor, no tu), no se arregla.
- **NO ESCRIBES DOCTRINA.**
- **NO TOCAS `cap_01`, `cap_02` NI `cap_03`.** Siguen en deuda (`d094`), y no es blocante.
- **NO LANZAS EL INFORME DEL LOTE ENTERO.** El de un candidato suelto, en el acto, si es tuyo.

---

## 4. AL CERRAR

- **Escribe tu tanda**: `python forja.py credito --anotar`.
- **Commitea `docs/loop/` y tu carpeta de evidencia.**
- **Si nada te obliga a parar, deja el encargo de la vuelta siguiente en `docs/loop/PROMPT_SIGUIENTE.md`**,
  con la misma nota de excepcion que trae este fichero en su cabecera. Mide las condiciones de parada
  una a una y publica que las mediste, en vez de suponer que no se cumplen.
