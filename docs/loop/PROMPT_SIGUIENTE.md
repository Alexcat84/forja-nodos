# ENCARGO DE LA VUELTA 4 DEL FRENTE `gerber_emyth`: **CERRAR `cap_12` PRIMERO**, y solo despues abrir capitulo nuevo

*Linea **`gerber_emyth`** (`extraccion-gerber_emyth`, worktree
`C:/Users/AlexDesk/Documents/forja-gerber_emyth`). **Escrito por la sesion de chat del 22
sep 2026** al aplicar la decision del fundador sobre tu parada `G3`.*

> # **LIBRO DE ESTA VUELTA: `gerber_emyth`**
> # **CLASE DE ESTA VUELTA: EXTRACCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. TU RACHA SE REINICIO, Y VIENE CON UNA CONDICION QUE ES LA TAREA `1`

**Parabas por `REPORTE` a `3 de 3`.** El fundador la reinicio por escrito:

    $ python forja.py credito
      REPORTE            0 de 3     docs/loop/paradas/2026-09-22-gerber-g3-DECISION.md, punto 1
      CREDITO ENTERO: ninguna especie en su tope.

**LA CONDICION, LITERAL:** *la `TAREA 1` de la vuelta `4` ejecuta `d101` antes de abrir
`cap_13`.*

> **NO ES UN INDULTO Y NO LO LEAS COMO TAL.** De tus tres caidas, dos eran erratas de
> celda y **la tercera era trabajo anunciado y no hecho**. Tu propio auditor las separo
> antes de que nadie se lo pidiera. **El reinicio paga las dos primeras; la tercera se
> paga haciendola.**

### 0.a. **Y NACE UNA REGLA DE TU CAIDA. Leela antes de empezar: `D.61`**

> **UN DISCUTIBLE PUBLICADO SE EJECUTA O SE CIERRA EN LA MISMA VUELTA QUE LO ESCRIBE.**
>
> **Un *ahi nace otro candidato* publicado y no ejecutado es caida de `CIFRA PUBLICADA`,
> no de `REPORTE`.**

**Esto te cambia un precio, y hacia arriba:** `CIFRA PUBLICADA` tiene tope `2` y no `3`,
**asi que esta figura muerde antes**. Si esta vuelta publica un discutible y lo deja
abierto al cerrar, **no llega a la tercera**.

**Las dos maneras de cumplirla valen las dos:**

1. **SE HACE:** el candidato nace en esta vuelta, con su ficha y su informe.
2. **SE CIERRA:** el reporte escribe **por que no nace**, con la linea del libro delante.
   Un discutible cerrado con motivo **no cae**.

**Lo que no vale es dejarlo abierto**, porque es una promesa en una sede que la vuelta
siguiente no tiene por que leer.

---

## 1. TAREA `1`, Y VA ANTES QUE TODO LO DEMAS: **CERRAR `cap_12` (`d101`)**

`d101`, `ACTA G3` `3.1`, con las tres piezas ya nombradas:

| pieza | que es | que hace esta vuelta |
|---|---|---|
| `cap_12` **`L51`** | `THE INNOVATION`, el saludo nuevo, con las palabras exactas y sus dos ramas | **NACE CANDIDATO** |
| `cap_12` **`L63`** | el test de seis semanas del traje azul, con sus dos etapas y sus ocho prendas nombradas una a una | **NACE CANDIDATO** |
| `cap_12` **`L69`** | tocar el brazo | **SE DECLARA NO-NODO, CON SU MOTIVO.** No pasa la vara de `EXTRACTOR.md` `9.1`, y el acta ya lo dijo |

**LOS TRES SE ESCRIBEN. El tercero tambien**, y esa es la mitad que se suele perder: si
solo escribes los dos que nacen, **la vuelta siguiente vuelve a encontrarse el `L69`
abierto** y alguien lo vuelve a discutir desde cero.

**Cada candidato con su `python forja.py informe` corrido en el mismo acto en que lo
escribes.**

### 1.a. **Y LA CLASE DE `R3` SE CORRIGE DECLARANDO, SIN BORRAR**

`docs/loop/REPORTE.md` linea `57859`. **Se tacha y se escribe al lado**, como se
corrigieron las cuatro celdas de `d095`. **Correccion declarada, nunca borrado.**

---

## 2. TAREA `2`: **`cap_13` Y `cap_14`**

**Solo despues de que la `TAREA 1` este cerrada.** `cap_13` son `364` palabras, el mas
corto del libro; `cap_14` va detras.

Por cada capitulo:

1. **LA FRONTERA, fila a fila contra el fichero**, con sus numeros de linea y sus
   palabras, **cero solapes y cero lineas sin cubrir**. Se comprueba al digito.
2. **Los candidatos que de**, cada uno con su informe corrido en el acto.
3. **`PASOS INVENTADOS POR CAPITULO`, UNA FILA POR CAPITULO Y NO UNA MEDIA**
   (`AUDITOR_FORJA.md` `8`). **Si da CERO, la fila se escribe igual** y dice
   `SIN SUPERFICIE`.
4. **La muestra de fidelidad con la semilla de esta vuelta:**

       python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_13,cap_14 --semilla g4

**SON TRES CAPITULOS TOCADOS Y ESE ES EL TECHO DEL LIGERO** (`D.58`): `cap_12` que se
cierra, mas `cap_13` y `cap_14`. **No abras un cuarto.**

---

## 3. LO QUE CAMBIO EN TU MAQUINARIA MIENTRAS ESTABAS PARADO

**Los tres defectos que mediste y no podias tocar estan arreglados** (decision del `22`
sep, punto `3`). **Hiciste lo correcto las tres veces: los mediste, los anotaste con su
cita y los subiste.** `D.45` sigue vedandote tocarlos, y sigue siendo lo correcto.

| deuda | como queda |
|---|---|
| **`d097`** | la cadencia de saneamiento **cuenta por linea**. Antes decia *van `-56` de `5` desde la `59`* de la serial, y **este frente no podia recibir una vuelta de saneamiento nunca** |
| **`d096`** | tus `cap_05`, `cap_06`, `cap_09` y `cap_10` minados a cero **constan como minados**, con la firma de la `ACTA G2` y la `ACTA G3`. Tu fila pasa de `4` capitulos a `9`, y tu ultimo capitulo de `cap_11` a `cap_12` |
| **`d102`** | el arnes **pone al dia la fila del tablero al CERRAR el turno**, no solo al abrirlo |

> ### **Y `d097` TE TRAE UNA CONSECUENCIA QUE CONVIENE QUE SEPAS AHORA**
>
>     $ python scripts/deuda.py --clase 4
>     LIBRE
>       van 3 de 5 desde la primera vuelta de la linea 'gerber_emyth' (la 1), con 36 deuda(s) esperando
>
> **Tu vuelta `6` va a salir `SANEAMIENTO`**, y eso es la cadencia funcionando por primera
> vez en un frente. **Tienes `36` deudas esperando.** No es para esta vuelta, pero no te
> pille de sorpresa.

---

## 4. LOS PUNTEROS QUE NO SE PUEDEN PERDER

Estan los tres en `docs/loop/DEUDA.jsonl` y **ninguno se abre en esta vuelta**:

- **`d104`** (`D.37`, `cap_12` `L21`): nombra `Innovation`, `Quantification` y
  `Orchestration` una a una, y **ninguna existe como nodo cabeza**. Si nace la cabeza, la
  arista se declara **entonces y no antes**. **Ojo, que esta vuelta toca `cap_12`:** si
  los candidatos de la `TAREA 1` hicieran nacer esa cabeza, **es aqui donde se declara**.
- **`d098`** (`D.37`, `cap_05` `L29`): las tres fases del crecimiento. Su gemelo.
- **`d099`**: donde nace el nodo de la delegacion, **si nace**: `cap_18` `L345` a `L349`,
  no en `cap_06`. `cap_18` no esta minado.

---

## 5. LO QUE NO HACES, Y NO ES NEGOCIABLE

- **NO INSERTAS.** `MODO_INSERCION=cuarentena`. Cero nodos al grafo.
- **NO TOCAS EL ARNES NI LA MAQUINARIA.** `D.45`, moratoria total: `orquestador_forja.sh`,
  `src/`, `scripts/`, `tests/`, `hooks/` y `esquema/`. **Mides y subes, no arreglas.**
- **NO ESCRIBES DOCTRINA.** Si una pregunta necesita regla nueva, es parada.
- **NO TOCAS `cap_01`, `cap_02` NI `cap_03`.** Siguen en `d094` por decision del fundador,
  y **no son blocantes**.
- **NO ABRES `cap_13` ANTES DE CERRAR `cap_12`.** Es la condicion del reinicio de tu
  racha, literal.

---

## 6. AL CERRAR

- **Escribe tu tanda**: `python forja.py credito --anotar`.
- **Repasa `D.61` contra tu propio reporte antes de cerrarlo**: por cada discutible que
  hayas publicado, o esta ejecutado o esta cerrado con su motivo. **Ninguno abierto.**
- **Commitea `docs/loop/` y tu carpeta de evidencia.**
- **Si nada te obliga a parar, NO escribas `PARA_ALEXIS.md`**, y deja el encargo de la
  vuelta `5`. **Mide las condiciones de parada una a una y publica que las mediste.**
