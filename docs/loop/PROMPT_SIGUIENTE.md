# ENCARGO DE LA VUELTA 34: **LA INSERCION DEL LOTE 4 CONTINUA, EN AUSTERO**

*Linea **serial** (`extraccion-mundo-11`), la unica que inserta (`D.45`).*

> # **ESTE ENCARGO NO ABRE NADA TODAVIA**
>
> **`docs/loop/PARA_ALEXIS.md` esta en el arbol**: el auditor cerro la `ACTA 32` con
> **`DATO MOVIDO` en `2 de 2`, credito roto**, y `AUDITOR_FORJA.md` `5.4` dice que esa
> racha **la reinicia una decision del fundador escrita en `docs/loop/paradas/`, y no la
> reinicia nadie mas.** **El arnes se detiene en ese fichero antes de llegar aqui.**
>
> Queda escrito **para que el relanzamiento sea de un solo paso cuando la decision
> llegue**, no para saltarse la parada.

---

## 1. LA APERTURA: **EL TABLERO Y SU PRIORIDAD, ANTES DE NADA** (`D.49`, `D.51`)

> # **LIBRO DE ESTA VUELTA: `scott_radical_candor`**

**Esa linea no es adorno: el arnes la lee y la comprueba contra el tablero antes de gastar
un turno.** Si el libro que declara tiene otro dueño, o no es el que el orden le da a esta
linea, **la vuelta no abre.**

    python forja.py tablero                el estado de los once libros
    python forja.py tablero --siguiente    que libro le toca a ESTA linea, y por que

**TU APERTURA CITA LAS DOS COSAS**, y esto es `D.49` con sus palabras (*toda linea lee el
tablero en su apertura y lo cita*):

| | que citas |
|---|---|
| **el tablero** | el estado y el dueño de tu libro, y **los dos libros que tienen dueño hoy** |
| **la prioridad** | **por que te toca este y no otro** (`D.51`), y que numero del orden es |

**EL ORDEN DEL MUNDO 11, QUE NO ELIGES TU** (`D.51`): `1` `grove_high_output`,
`2` `gerber_emyth`, `3` `marquet_turn_the_ship`, **y ahi esta el corte**. Los tres de
debajo (`bernerslee_bananas`, `openstax_business_ethics`, `openstax_org_behavior`) **no se
extraen en esta campania**: quedan en bandeja, con su ficha, para entrar por la aduana de
a uno cuando el fundador lo decida.

**MIENTRAS `scott_radical_candor` NO CIERRE, TE TOCA `scott_radical_candor`**, porque
`D.50` releva **al cerrar** un libro y no a mitad. **Y cuando cierre, NO abras el siguiente
por tu cuenta:** `--siguiente` te dira que le falta al que toca, y si lo que falta es una
cosecha, **se pide y se para**. El bucle no funde ramas.

---

## 2. **LO PRIMERO DEL TURNO: TU CREDITO** (`D.48`)

    python forja.py credito

**Es la sede de tu racha, y tu acta la publica, no la decide.** Al cerrar escribes tu
tanda, **una linea por especie, y es parte de cerrar**:

    python forja.py credito --anotar --especie "DATO MOVIDO" --vuelta 34 \
           --tanda "ACTA 33" --racha "0 de 2" --limpia --cita "ACTA 33, seccion 9.1"

**`--cae` si la especie cayo en tu tanda, `--limpia` si no.**

> ### **Y UNA COSA QUE TU ANTECESOR LEVANTO CONTRA EL INSTRUMENTO, Y TIENES QUE SABER**
>
> **El campo `cita` del registro de credito puede traer conclusiones del reporte dentro**,
> y la apertura ciega lee ese registro. **Si estas en fase ciega, el `cita` de una tanda
> ajena es contaminacion**: `D.34.2` retira cuatro ficheros por una puerta y esto abre
> otra. **Esta subido al fundador y no se resuelve aqui.** Mientras tanto: **escribe tus
> `cita` como REFERENCIA** (`"ACTA 33, seccion 9.1"`), **nunca como resultado**
> (`"11 SANO releidos"`).

---

## 3. TAREA 1. **SEGUIR INSERTANDO EL LOTE 4**

    $ python .v34/estado.py
    poblacion: el arbol entero, sin filtrar
    dataset/nodos.jsonl                     : 282 nodos
    bitacora/VEREDICTOS.jsonl               : 410 lineas
    cuarentena/scott_radical_candor         : 63
    cuarentena/_insertados/scott_radical_candor: 79

**`cap_08` cerro en insercion, `12` de `12`. El siguiente es `cap_09`, con `20` candidatos
en bandeja contra un techo de `15`** (`EXTRACTOR.md` 12.4). **El techo manda:** si el
capitulo entero no cabe, **la vuelta cierra donde cabe y lo declara con su cifra.**

- **Un candidato por vez y en el orden del libro**, por la aduana, con su veredicto.
- **Las aristas `D.29` que la señal no levanta se declaran por lectura y se cablean en la
  misma vuelta.**
- **`NO SE ABRE NINGUN LOTE** (`D.32`), y **el lote 5 NO SE TOCA**: ahora ademas lo impide
  el tablero, no solo esta frase.

> **EL CERROJO ESTA PUESTO** (`D.44`): una sola corrida escribe el dataset. Si algo dice
> `INSERCION NO INTENTADA`, hay otra corrida viva. **No la esquives.**

## 4. TAREA 2. **BLOQUEANTE: LA AFIRMACION DEL GRAFO QUE HOY ES FALSA**

*Es el segundo ejemplar de `DATO MOVIDO` que el auditor midio, y **es contenido puro del
dataset**, no un fichero de proceso.*

**Un nodo que entro en la vuelta 33 dice dentro de `dataset/nodos.jsonl` que tres capitulos
NO estan minados todavia, y uno de los tres tiene `16` nodos y `187` pasos en el grafo**,
metidos por la vuelta 32. **La misma vuelta 33 lo probo**, porque cablo una arista a ese
capitulo.

    python forja.py corregir --nodo <id> --anade "CORRECCION DECLARADA ..." --razon ...

**`D.13`, sin borrar el texto viejo.** Y **publica el comando con el que lo encontraste**,
no solo el que lo arregla.

## 5. TAREA 3. **LA FIDELIDAD, ANTES DE CERRAR**

**`PASOS INVENTADOS` por capitulo** (`D.30`), fila por unidad mas total, **releyendo los
pasos contra su parrafo**, y **la relectura va ANTES de que los nodos entren**, que es la
letra que la vuelta 33 rompio. **La escalada se decide sobre el peor capitulo.** Tope `10`.

---

## MODO AUSTERO (`D.47`)

| | |
|---|---|
| **el reporte** | **nada que el registro ya diga** |
| **los discutibles** | **por numero y linea**, sin reabrir el argumento |
| **las cifras** | **talladas**, con la salida del instrumento pegada de su fichero (`D.41`) |
| **los instrumentos** | **CERO nuevos**, salvo que una caida **de DATO** lo exija con su cita |

> **El austero recorta tinta, no control.** La aduana entera, el cerrojo, el censo no
> decreciente y la relectura contra el parrafo **quedan intactos**.

## LO QUE NO SE TOCA

- **`src/`, el banco, el arnes y los protocolos**: moratoria de `D.45`.
- **`config/umbrales.json`**, ningun umbral.
- **`config/frentes.json`**: lo que hay ahi son **decisiones del fundador con su cita**, no
  configuracion.
- **El bucle no funde ramas y el bucle no crea remotos.**
- **Los frentes**: `grove_high_output` es de su linea; `gerber_emyth` y
  `marquet_turn_the_ship` estan pausados. **Ninguno es asunto tuyo, y ahora el tablero lo
  impide de verdad.**

## AL CERRAR

    python scripts/cerrar_reporte.py
    python forja.py tablero --escribir          el tablero se vuelve a medir (D.49)
    python forja.py credito --anotar ...        una linea por especie, con su cita

**Y COMMITEA Y PUSHEA `docs/loop/`.**
