# ENCARGO DE LA VUELTA 6 DEL FRENTE `gerber_emyth`: **VUELTA DE SANEAMIENTO** (`D.55`, `D.58`), la primera que esta linea corre

*Linea **`gerber_emyth`** (`extraccion-gerber_emyth`, worktree
`C:/Users/AlexDesk/Documents/forja-gerber_emyth`). **Escrito por el auditor del bucle** al
cerrar la `ACTA G5`, que audita tu vuelta `5`.*

> # **LIBRO DE ESTA VUELTA: gerber_emyth**
> # **CLASE DE ESTA VUELTA: SANEAMIENTO**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. COMO TE FUE, EN UNA TABLA, PARA QUE NO TENGAS QUE LEER EL ACTA ENTERA

| lo que mide la `ACTA G5` | resultado |
|---|---|
| las tres fronteras, **pieza por pieza** y con codigo que no es el tuyo | **las `17` piezas al digito**, residuo `0`, `0` solapes, `0` sin cubrir en los tres |
| tus `5` pasos, leidos **los `5`** contra `L169` a `L177` | **`0` PUENTE. Las tres filas de `PASOS INVENTADOS` te quedan FIRMADAS** |
| tu muestra con semilla `g5` | **identica byte a byte** |
| tu informe de aduana, vuelto a correr | **identico al milesimo**, y la poblacion `456` descompuesta en `346` mas `110` |
| tus **dos** discutibles marcados | **se sostienen los dos**, y con tu razon escrita firmada en el `4` |
| cinco superficies que **no** marcaste y que el auditor examino | **se sostienen las cinco** |
| `d107`, el paso nuevo que te encargue | **CUMPLIDO**, con la salida corrida en vez de darla por hecha |
| tus cinco rachas | `CIFRA PUBLICADA`, `CLASE` y `DATO MOVIDO` en `0`; **`REPORTE` sube a `1 de 3`** |

> ### **LO QUE SE CAE ES UNA CELDA, Y ESTA VEZ SI ACUMULA**
>
> La fila `R7` de la frontera de `cap_15` publica **`L185 a L280`** y el fichero tiene **`279`**
> lineas. **Vive en TABLA, y `5.2` dice que en tabla acumula.** No mueve ninguna cifra (las `2891`
> palabras salen iguales, porque la linea `280` no existe y no aporta ninguna), **pero es una celda
> falsa y no la perdono**: perdonarla seria elegir la lectura que me deja seguir.
>
> **NO ES CONVENCION DE TU INSTRUMENTO Y LO COMPROBE:** de las `22` fronteras que este frente lleva
> escritas, **`21` acaban en su ultima linea real y solo esta rebasa.** Y la guarda no la caza: de
> mis tres mutaciones, la de hueco y la de solape salen ROJAS y **la de rebasar el fichero sale
> MUDA** (`d109`, que **no** te encargo porque la moratoria de maquinaria sigue en pie).
>
> **Y CAEN DOS FRASES MAS, las dos en prosa y las dos SIN acumular**, y las dos son la misma figura:
> **un acierto con la razon equivocada a mano.** La primera dice que `R3` de `cap_15` va *sin
> imperativo explicito* y `L57` trae *the first question **you must always ask***; **tu decision se
> sostiene igual**, pero por el criterio del PUNTERO (*some of the standards* es abierto, *there are
> only specific questions* con cuatro vinetas detras es cerrado), que es el que la `ACTA G4` `3.3`
> ya dejo escrito. La segunda esta en `G5.6.a` y la pagas en la `TAREA 3`.

---

## 1. TAREA `1`: **LA CELDA `L280`, CORREGIDA REGENERANDO Y NUNCA TECLEANDO**

**Esa tabla es TALLADA**, asi que `D.41` manda **regenerar**: no toques la celda del reporte a mano
o el tallado aborta el commit. Es el caso contrario al de la `TAREA 1` de tu vuelta `5`, donde las
dos correcciones vivian en prosa y ahi si se tachaba.

Por este orden, y pega la salida de cada paso:

1. corrige el borde en el fichero de piezas que heredes (`"R7", 185, 280` pasa a `"R7", 185, 279`);
2. vuelve a correr `frontera.py` sobre `cap_15` y **pega la tabla nueva entera**;
3. sustituye la tabla de `G5.3.a` por la regenerada, **y deja escrito al lado que es una correccion
   declarada de la `ACTA G5` `4.1`**, con el motivo en una linea;
4. corre `python scripts/tallar_reporte.py` y **comprueba que sigue VERDE**.

> **YA MEDI QUE LA CORRECCION NO MUEVE NADA MAS, asi que si te mueve otra celda, para y traelo:**
>
>     $ sed 's/"R7", 185, 280/"R7", 185, 279/' .gerber_v5/piezas_cap15.txt > .g5aud/piezas_cap15_279.txt
>     $ python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_15.md .g5aud/piezas_cap15_279.txt > .g5aud/frontera_cap15_279.txt
>     $ diff .gerber_v5/frontera_cap15.txt .g5aud/frontera_cap15_279.txt
>     13c13
>     < | `R7` | L185 a L280 | **2891** | la historia de Sarah [...] | **CASO** |
>     ---
>     > | `R7` | L185 a L279 | **2891** | la historia de Sarah [...] | **CASO** |
>
> **Una sola celda. Las `2891`, el cuerpo `4685`, la suma, el residuo `0`, los `0` solapes y las `0`
> lineas sin cubrir salen identicos.**

**Y LO PRIMERO DE ESTA TAREA, ANTES QUE LA CELDA: DECLARA LA CLASE DE LA VUELTA.**

    python scripts/deuda.py --saneamiento --vuelta 6 --cita "PROMPT_SIGUIENTE.md, encargo de la vuelta 6, cabecera"

**No es papeleo.** La linea `gerber_emyth` **no ha saneado nunca** y va `4` de `5`. La vuelta `49`
de la serial corrio como saneamiento **y no lo anoto**, y desde entonces lo comprueba el codigo
(`D.58`). **Pega la salida.**

---

## 2. TAREA `2`: **EL BARRIDO DE DEUDA, QUE ES LA SUSTANCIA DE ESTA VUELTA**

    python scripts/deuda.py                     lo pendiente y que clase toca
    python scripts/deuda.py --clase 5           la cadencia

**Hoy son `42` pendientes y `33` pagadas.** No las vas a pagar todas: **la mayoria no son de esta
linea o piden tocar lo que `D.45` veda.** Lo que se te pide es **pasar por todas las de esta linea,
pagar las que se puedan pagar aqui, y declarar de las demas POR QUE no**, con su medida al lado.

Las de la linea `gerber_emyth`, tal como estan hoy, **y mi lectura de cual toca**:

| id | que es | en esta vuelta |
|---|---|---|
| `d094` | `cap_01` a `cap_03` sin minar | **NO SE PAGA**: es decision del fundador y no es bloqueante. Declaralo y sigue |
| `d098` | puntero `D.37` de `cap_05` `L29`, las tres fases | **NO SE PAGA AQUI**: es para la vuelta que INSERTE |
| `d102` | el tablero publicaba `candidatos_en_bandeja 10` con `11` en bandeja | **MIDELO**: hoy publica `16` y la bandeja tiene `16`. Si no reproduce, **pagala diciendo que no reproduce y con las dos salidas pegadas** |
| `d103` | el bloque de `gate` pegado a dos lineas en vez de tres | **MIDELO**: tu vuelta `5` lo pego a tres y mis dos actas tambien. Si el defecto ya no aparece en las tres ultimas vueltas, **pagala con las tres citas** |
| `d104` | puntero `D.37` de `cap_12` `L21`, la terna | **NO SE PAGA AQUI**: es para la vuelta que INSERTE |
| `d106` | el tablero publica `ult cap = cap_19` con `cap_17` minado | **NO SE PUEDE**: vive en `src/tablero.py`, que `D.45` veda desde un frente. **Mide que sigue viva y dejala** |
| `d107` | el primer candidato de una vuelta no ve a los que nacen despues | **SIGUE VIVA**: tu vuelta `5` la cumplio con un solo candidato, que es el caso trivial. Declaralo y dejala |
| `d108` | releer `cap_14` `L27` contra `L117` | **NO SE PAGA AQUI**: es para la vuelta que INSERTE |
| `d109` | la guarda de frontera no mira el borde de arriba | **NO SE PUEDE**: es maquinaria, y la moratoria (`7.F`, `D.47`) solo se levanta con una caida de DATO |
| `d110` | el discutible `5` se cierra en `cap_18`, no en `cap_17` | **NO SE PAGA AQUI**: `cap_18` no se mina en una vuelta de saneamiento |
| `d111` | la serie `D.37` de `cap_13` va por `0` de `7` con cuatro pasos leidos | **NO SE PAGA AQUI**: la decision es de la vuelta que INSERTE |
| `d112` | el orden de `tabla_de_cierre.py --escribir` | **SE PAGA EN LA `TAREA 3`** |

> **LO QUE CUENTA COMO PAGO, Y LO QUE NO.** Un pago es **una medida corrida en esta vuelta con su
> salida pegada**, no una frase. Y **una deuda que no reproduce se paga igual**, diciendo que no
> reproduce y con las dos salidas delante: la vieja citada y la nueva corrida. **Una busqueda
> negativa no se puede citar** sin haberla corrido.
>
> **Y SI AL MEDIR ALGUNA TE SALE PEOR DE LO QUE SU FICHA DICE, ESO NO SE PAGA: SE REESCRIBE** con su
> medida nueva, y se dice que la vieja se quedo corta.

---

## 3. TAREA `3`: **`d112`, Y SE PAGA CAMBIANDO EL ORDEN, NO EL CODIGO**

**LO QUE MIDIO LA `ACTA G5` `4.2` CAIDA `b`.** Tu `G5.6.a` dice que
`docs/loop/TABLA_DE_CIERRE.txt` guarda solo las dos filas de la `ACTA G4` *porque el instrumento
mide afirmaciones de la forma `N` de `M` del capitulo y esta vuelta no escribio ninguna*. **Eso es
falso, y lo dice su propio docstring:**

    $ sed -n '31,32p' scripts/tabla_de_cierre.py
    LO QUE NO INVENTA. Una fila sin cifra medible **se copia tal cual y se declara
    `SIN COMPROBAR`**. Un instrumento que rellena lo que no sabe no mide: dicta. Y el patron

    $ python scripts/tabla_de_cierre.py | sed -n '5,8p'
      filas             : 3
      SIN COMPROBAR  `1`  ninguna afirmacion de la forma 'N de M del capitulo' con su cap_NN
      SIN COMPROBAR  `2`  ninguna afirmacion de la forma 'N de M del capitulo' con su cap_NN
      SIN COMPROBAR  `3`  ninguna afirmacion de la forma 'N de M del capitulo' con su cap_NN

**LA CAUSA REAL ES EL ORDEN:** el instrumento lee **la ULTIMA** tabla de cabecera fija de
`REPORTE.md`, y tu corriste `--escribir` **antes** de pegar la tuya. **Te firmo que lo declaraste en
vez de esconderlo**, y por eso `CIFRA PUBLICADA` te sale limpia: lo que cae es la explicacion.

**EL PAGO, Y NO LLEVA NI UNA LINEA DE CODIGO NUEVO:**

1. escribe tu tabla de cierre de la vuelta `6` en el reporte **primero**;
2. corre `python scripts/tabla_de_cierre.py --escribir` **despues**;
3. pega la salida y **comprueba que el fichero trae TUS filas**, no las de otra vuelta;
4. paga `d112` con `scripts/deuda.py --pagar d112 --vuelta 6 --como "..."` y la salida al lado.

> **NO ES `d022` NI `d030`, y por eso tiene numero propio:** `d022` era la cabecera y `d030` el
> nombre del fichero de salida. **Esta es el orden**, y el remedio es gratis.

---

## 4. TAREA `4`: **EL CIERRE DE UNA VUELTA DE SANEAMIENTO**

Las guardas con su salida pegada entera (`gate` son **TRES** lineas, `d103`), las cifras
recomputadas y **no copiadas** de la apertura, la tabla de cierre (con el orden de la `TAREA 3`),
las condiciones de parada repasadas una a una con su medida, y `python forja.py credito` **medido y
no anotado**.

**LO QUE UNA VUELTA DE SANEAMIENTO PUBLICA ADEMAS, y es lo que la hace auditable:**

| pieza | por que |
|---|---|
| **deudas que pagas, una por una, con su salida** | un pago sin medida no es un pago |
| **deudas que NO pagas, con el motivo medido** | es la mitad que siempre se pierde, y sin ella no se sabe si quedaban o si no se miraron |
| **el saldo antes y despues** (`pendientes` y `pagadas`) | hoy sales de `42` y `33` |
| **la declaracion de saneamiento** (`TAREA 1`) | `D.58`, y lo comprueba el codigo |

---

## 5. LO QUE NO HACES, Y NO ES NEGOCIABLE

- **NO MINAS NINGUN CAPITULO NUEVO.** Esta vuelta es de saneamiento: `cap_18` espera, y con el
  espera `d110`.
- **NO INSERTAS.** `MODO_INSERCION=cuarentena`. Cero nodos al grafo (`D.39`).
- **NO TOCAS EL ARNES NI LA MAQUINARIA.** `D.45`, moratoria total: `orquestador_forja.sh`, `src/`,
  `scripts/`, `tests/`, `hooks/` y `esquema/`. **Mides y subes, no arreglas.** Eso cubre `d106` y
  `d109`, que son las dos de esta lista que mas pican.
- **NO ESCRIBES DOCTRINA.** La cola se queda en `11` (`D.55`). Si encuentras una pregunta nueva,
  **registrala con su medida y dejala ahi.** Si una lectura te pide mover la vara de `9.1`, **eso si
  es parada y se trae.**
- **NO TOCAS `cap_01`, `cap_02` NI `cap_03`.** Siguen en `d094` por decision del fundador.
- **NO TE ESCRIBES TU FILA DE CREDITO.** La mide `python forja.py credito`, que es de solo lectura;
  la anota el auditor. **Ya quedo dicho en el encargo anterior y no se vuelve a razonar.**

---

## 6. LOS PUNTEROS QUE NO SE PUEDEN PERDER

- **`d098`** (`D.37`, `cap_05` `L29`) y **`d104`** (`D.37`, `cap_12` `L21`): las dos ternas sin
  cabeza.
- **`d111`** (nuevo): la serie de `cap_13` va por **`0` de `7`** con los pasos `1`, `2`, `3` y `4` ya
  leidos, y **el `6` esta apartado y no se toca nunca**. Le quedan `cap_18` y `cap_19` para ganar
  una sola parte. **La decision es de la vuelta que inserte**, no tuya.
- **`d110`** (nuevo): `cap_18` abre recogiendo literalmente la pregunta con la que `cap_17` corta.
  **Cuando lo mines, lee esa apertura con `cap_17` `L189` a `L221` delante** y di si el autor saca
  el Operations Manual del caso o no.
- **`d108`**: releer `cap_14` `L27` contra `L117`. **Para la vuelta que INSERTE.**

**Y LA CADENCIA, PARA QUE NO TE PILLE:** al cerrar esta vuelta el contador de `D.55` vuelve a cero,
y la `7` sale `LIBRE`. **Si nada cambia, la `7` abre `cap_18`** (`Cap. 16`, *Your People Strategy*,
`5396` palabras, paso `5` de la serie).

---

## 7. AL CERRAR

- **Repasa `D.61` contra tu propio reporte antes de cerrarlo**: por cada discutible que publiques, o
  esta **ejecutado** o esta **cerrado con su motivo y la linea delante**. Ninguno abierto, tope `2`.
- **Mide `python forja.py credito`** y pega la salida. **No uses `--anotar`.**
- **Mide las condiciones de parada una a una y publica que las mediste.**
- **Commitea `docs/loop/` y tu carpeta de evidencia.**
- **Si nada te obliga a parar, NO escribas `PARA_ALEXIS.md`.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.**
