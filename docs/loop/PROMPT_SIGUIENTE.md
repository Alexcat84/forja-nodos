# ENCARGO DE LA VUELTA 3 DEL FRENTE `gerber_emyth`: **EL REMEDIO HEREDADO PRIMERO, Y DESPUES `cap_09`, `cap_10` Y `cap_12`**

*Linea `gerber_emyth` (`extraccion-gerber_emyth`, worktree
`C:/Users/AlexDesk/Documents/forja-gerber_emyth`). **Escrito por el auditor del bucle al cerrar la
`ACTA G2`**, que es la sede que `AUDITOR_FORJA.md` `5.6` le asigna. **La nota de excepcion que
traian los dos encargos anteriores se retira**: aquel fichero lo escribio una sesion de chat porque
no habia auditor en el bucle; hoy lo hay, y este encargo sale de una auditoria hecha.*

> # **LIBRO DE ESTA VUELTA: gerber_emyth**
> # **CLASE DE ESTA VUELTA: EXTRACCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. TU VUELTA 2, AUDITADA: **LA COSECHA CERO ERA CIERTA Y ESTA FIRMADA**

**`ACTA G2` de `docs/loop/ACTA_AUDITOR.md`.** Antes del encargo, lo que salio bien, porque es la
mayor parte y no se dice sola:

- **las `9` filas de tus dos fronteras me salen al digito** contra mi propio codigo, y con ellas
  los dos cuerpos (`2400` y `1980`), los dos residuos en `0`, los dos solapes en `0` y los dos
  huecos en `0`;
- **las `32` celdas de tu tabla de apertura me salen las `32`**, incluidas las `22` palabras de
  cuerpo del libro y su total de `62648`;
- **tu muestra de fidelidad con semilla `g2` me sale identica byte a byte**, y tus cuatro
  `git hash-object` me salen los cuatro;
- **tus `3` discutibles se sostienen los `3`.** Lei `cap_05` y `cap_06` enteros y mire ademas
  **tres superficies que tu no marcaste**: ninguna pasa la vara. **El cero de los dos capitulos
  es mio tambien.**

**Y DOS CAIDAS, las dos en `ACTA G2` `3`:**

| que | donde | especie |
|---|---|---|
| tu tabla de parada dice `los dos discutibles` donde `G2.7` tiene **`3`**, y tu propio `G2.8.c` dice `3` | `REPORTE.md` linea `57681`, y es una TABLA | **`REPORTE`**, ahora en **`2 de 3`** |
| escribiste `--racha "1 de 3"` en `docs/loop/CREDITO_gerber_emyth.jsonl` **para una tanda que declaras limpia**, y sin `--limpia` ni `--cae` | el registro de credito, sede duradera bajo `docs/` | **`CIFRA PUBLICADA`**, ahora en **`1 de 2`** |

**La segunda es mitad del encargo que recibiste y mitad tuya**, y asi esta escrita en el acta: el
encargo te mando escribir tu tanda, **y adjudicar tu propia racha no es tuyo** (manual principio
`10`: el que mide no adjudica). **Tu levantaste el caso gemelo** (que `PROMPT_SIGUIENTE.md` era
sede del auditor) **y no levantaste este.** Lo corregi anadiendo, sin borrar tu linea.

**MI PROPIA RACHA TAMBIEN SUBIO, a `2 de 3`**, por el remedio de la `ACTA G1` que sigue sin
cumplir. **Por eso es la `TAREA 1`.**

---

## 1. TU ESTADO, MEDIDO POR MI EN LA AUDITORIA Y NO RECORDADO

    $ git rev-parse --short HEAD
    0fd8e1d   (mas el commit de mi acta, que este cierre anade)
    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl
    346 dataset/nodos.jsonl
    740 bitacora/VEREDICTOS.jsonl
    $ ls cuarentena/gerber_emyth/*.json | wc -l
    10
    $ python forja.py tablero --puedo gerber_emyth
    LINEA 'gerber_emyth', LIBRO 'gerber_emyth': SI
      'gerber_emyth' ya es de esta linea ('gerber_emyth'): continuarlo es lo que toca.

**Minados y adjudicados, los seis:** `cap_04`, `cap_05`, `cap_06`, `cap_07`, `cap_08`, `cap_11`.
**Quedan `16` de `22`.** La bandeja sigue en `10` candidatos con `89` pasos, contados por mi.

**Y UN AVISO QUE TE AHORRA UNA DUDA:** `docs/loop/TABLERO.jsonl` sigue diciendo
`capitulos_minados: ['cap_04', 'cap_07', 'cap_08', 'cap_11']`. **No es un error tuyo ni una
contradiccion con lo de arriba:** ese campo registra los capitulos que PRODUJERON candidato, no
los que se leyeron, asi que un capitulo adjudicado en cero no puede aparecer nunca. Esta medido
como `d088` en grove y lo anote como `d096` aqui. **No lo toques** (`D.45`).

---

## 2. TAREA 1: **EL REMEDIO HEREDADO DE LA `ACTA G1`, QUE LLEVA DOS VUELTAS SIN CUMPLIR**

*Es `d095` en `docs/loop/DEUDA.jsonl`, y su origen es
`docs/loop/paradas/2026-09-17-gerber-la-racha-y-la-linea-vieja-RESUELTA.md` seccion `5`.*
**NO ES BLOCANTE** (`D.55`: ninguna de las cuatro guardas de dato esta en rojo). **Es lo primero
que haces, no una puerta que te impida hacer lo demas.**

### 2.1. Las correcciones declaradas, **con tachado en su sitio y sin borrar**

**Tres celdas del bloque `G1`, que hoy vive en
`docs/loop/archivo/gerber_emyth/REPORTE_frente_hasta_v1.md`:**

1. **la de `G1.10.d` que cita `G1.10.e`**, seccion que no existe. Verificado por mi hoy:

       $ grep -n "G1.10.e" docs/loop/archivo/gerber_emyth/REPORTE_frente_hasta_v1.md
       36809:| una guarda en rojo | **ninguna en este turno.** Las cuatro de `G1.10.e` en verde al sellar | **NO ES PARADA** |

2. **la fila `CERRADO` del esqueleto `G1.0`**, que prometia un cierre en secciones que el bloque
   no llego a tener;
3. **la apertura de `G1.9`**, que promete un saldo que no llego. **El saldo que faltaba ya esta
   medido y publicado en la `ACTA G1` seccion `2`: se cita de ahi y NO se vuelve a correr.**

**Y una cuarta, que es de esta vuelta y es tuya:** la celda de `G2.8.d` que dice `los dos
discutibles` donde hay `3`. **Misma forma: tachado en su sitio, la cifra buena al lado, y el
motivo.**

### 2.2. El instrumento del punto `2`, que **hoy revienta y por que**

    $ python .v1g_auditor/secciones.py
    ValueError: max() iterable argument is empty

**No esta roto: esta apuntando a donde el bloque `G1` ya no vive.** Busca su encabezado dentro de
`docs/loop/REPORTE.md` y ese bloque se archivo el `21` sep.

> **QUE HACES CON ESO, y es una sola frase:** **corres la comprobacion sobre el bloque de ESTA
> vuelta**, que es el que estas escribiendo, contra `docs/loop/REPORTE.md`. Es la misma
> comprobacion de catorce lineas con `G3` en lugar de `G1`: **toda seccion que tu bloque cita
> contra las que tu bloque tiene. Tiene que dar `0` antes de que cierres el reporte.**
>
> **NO ES MAQUINARIA NUEVA** y no rompe la moratoria: es el instrumento que ya existe, corrido
> sobre otro bloque. **Y NO TOQUES `.v1g_auditor/secciones.py`**, que es sede mia: si necesitas
> una copia adaptada, la escribes en tu propia carpeta de evidencia de esta vuelta.

---

## 3. TAREA 2: **LA FRONTERA DE `cap_09`, `cap_10` Y `cap_12`**

**POR QUE ESTOS TRES.** `cap_09` y `cap_10` son **el segundo hueco entre capitulos ya minados**,
entre `cap_08` y `cap_11`: frontera conocida y verificable a los dos lados, que es el mismo patron
barato que la vuelta `2` cerro entre `cap_04` y `cap_07`. **`cap_12` es el primero sin minar que
sigue en orden** una vez cerrado ese hueco.

**POR QUE TRES Y NO DOS**, y la cifra que lo autoriza **no es la de pasos inventados**:

> `D.58`, tabla del regimen de extraccion: **el extractor mina TRES capitulos por vuelta, con
> techo de `30` candidatos.** `docs/BANCO_DE_REGLAS.md` linea `3201`.

**Lo digo asi a proposito.** `PASOS INVENTADOS` de la vuelta `2` salio `SIN SUPERFICIE` en los dos
capitulos, y **una metrica sin denominador no autoriza una subida de volumen**: la subida la
autoriza el techo escrito, no una cifra que no se pudo medir.

**Entregas, fila a fila contra el fichero:** numeros de linea, palabras, **cero solapes y cero
lineas sin cubrir**, y el residuo cerrando en `0`. **Se comprueba al digito, asi que no la
estimes:** yo la recompuse entera la vuelta pasada y la voy a recomponer otra vez.

---

## 4. TAREA 3: **LOS CANDIDATOS QUE CADA CAPITULO DE**

En `cuarentena/gerber_emyth/<id>.json`, **cada uno con su `python forja.py informe` corrido en el
mismo acto en que escribes la ficha.** El del lote entero **no lo lanzas** (`D.43`): lo corre el
arnes.

**SI UN SOLO CAPITULO PASA DE `30` CANDIDATOS, la vuelta cierra en ese capitulo y lo declara**, y
los que quedaban del tramo pasan a la vuelta siguiente (`EXTRACTOR.md` `12.4`, precedencia del
techo de candidatos). **Lo que verifico yo es que lo DECLARES**: una vuelta que cierra corta y no
lo dice es caida de `REPORTE`, y una que cierra corta y lo dice no es nada.

**Y UN CAPITULO QUE DE CERO SE CIERRA IGUAL**, leyendolo entero y diciendo contra que se leyo.
**Tu vuelta `2` lo hizo bien dos veces y se lo firme las dos.** Un cero es un resultado.

---

## 5. TAREA 4: **`PASOS INVENTADOS POR CAPITULO`**

**Una fila por capitulo y no una media** (`AUDITOR_FORJA.md` `8`), y **el total del lote aparte**.
Si un capitulo da cero, **la fila se escribe igual como `SIN SUPERFICIE`**: `D.59` prohibe
publicar una razon sin numerador y sin denominador, y cero sobre cero no es una razon.

**Es la cifra que yo firmo despues de contarla yo mismo contra la cuarentena**, asi que dame con
que: **el capitulo de origen de cada candidato tiene que poder leerse de su ficha.**

---

## 6. TAREA 5: **LA MUESTRA DE FIDELIDAD, SEMILLA `g3`**

    python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_09,cap_10,cap_12 --semilla g3

**La semilla va escrita en el reporte y la salida se pega literal.** Yo vuelvo a correrla con esa
misma semilla: **si me sale una lista distinta de la que pegaste, es caida de cifra** (`D.58`).

**Y EL DISPARADOR NO ES UNA RECOMENDACION:** si la muestra de un capitulo pasa del `10` por
ciento de pasos inventados, **ese capitulo se relee ENTERO antes de seguir**.

---

## 7. LO QUE NO HACES EN ESTA VUELTA

- **NO INSERTAS.** Ni un nodo. `MODO_INSERCION=cuarentena`.
- **NO ADJUDICAS TU PROPIA RACHA.** Esta es la novedad respecto al encargo anterior y sale de la
  caida de `3.2` del acta: **la tanda del credito la escribe el AUDITOR**, con el nombre del acta
  en el campo `tanda`, que es lo que hacen las `12` lineas de `docs/loop/CREDITO_serial.jsonl`.
  **Tu mides y declaras tus caidas en el reporte; el numero de la racha lo pongo yo.**
- **NO TOCAS EL ARNES NI LA MAQUINARIA** (`D.45`): `orquestador_forja.sh`, `src/`, `scripts/`,
  `tests/`, `hooks/` y `esquema/`. Un defecto **se mide y se anota en `docs/loop/DEUDA.jsonl`**,
  no se arregla.
- **NO ESCRIBES DOCTRINA.** La cola esta congelada en `11` (`D.56`). Una pregunta nueva se anota
  con su medida y se deja ahi.
- **NO TOCAS `cap_01`, `cap_02` NI `cap_03`.** Siguen en deuda (`d094`), no es blocante.
- **NO LANZAS EL INFORME DEL LOTE ENTERO** (`D.43`). El de un candidato suelto, en el acto, si es
  tuyo.
- **NO TOCAS `docs/loop/PARA_ALEXIS.md` NI `docs/loop/ACTA_AUDITOR.md`**, que son sede mia
  (`5.6`). Hoy el primero no existe, y eso es correcto: **no hay parada.**

---

## 8. DOS PUNTEROS QUE TE DEJO MEDIDOS, PARA QUE NO LOS BUSQUES DOS VECES

**No son tareas.** Salen de mi relectura de `cap_05` y `cap_06` y viven en `docs/loop/DEUDA.jsonl`:

- **`d099`, la delegacion.** `cap_06` solo NOMBRA el contraste *Abdication* contra *Delegation*,
  por eso su cero se sostiene. **El libro lo desarrolla en `cap_18`** (`Cap. 16`, *Your People
  Strategy*, `5396` palabras, sin minar), lineas `345`, `347` y `349`. **Si hay nodo, nace ahi.**
  Cuando `cap_18` entre en un tramo, esa es la linea que hay que leer con lupa.
- **`d098`, las tres fases.** `cap_05` `L29` dice cuantas partes hay y las nombra (*Infancy,
  Adolescence, and Maturity*), que es el supuesto de `D.37`. **Hoy `D.37` no aplica** porque no
  hay nodo cabeza ni partes que existan como nodo. **Si alguna vuelta futura hace nacer una de
  las tres, la arista se declara entonces citando `cap_05` `L29`, y no antes.**

---

## 9. AL CERRAR

- **Repasa las condiciones de parada una a una y publica que las mediste**, como hiciste en
  `G2.8.d`. **Con la cuenta bien**, que es lo unico que fallo de esa tabla.
- **Corre la comprobacion de secciones de `2.2` sobre tu propio bloque. Tiene que dar `0`.**
- **Commitea `docs/loop/` y tu carpeta de evidencia.** Una ruta que prueba una corrida y no viaja
  al repo deja de probar nada en cuanto otro clone.
- **Deja el reporte cerrado en tu turno.** Si no cierra, el tramo de la siguiente baja un escalon
  por `EXTRACTOR.md` `12.4`, y eso ya le costo una vuelta a esta casa.

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.**
