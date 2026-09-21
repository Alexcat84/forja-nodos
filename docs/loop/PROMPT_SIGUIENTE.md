# ENCARGO DE LA VUELTA 8 DEL FRENTE `gerber_emyth`: **VUELTA DE EXTRACCION**, los TRES capitulos que le quedan al lote 9

*Linea **`gerber_emyth`** (`extraccion-gerber_emyth`, worktree
`C:/Users/AlexDesk/Documents/forja-gerber_emyth`). **Escrito por el auditor del bucle** al cerrar la
`ACTA G7`, que audita tu vuelta `7`.*

> # **LIBRO DE ESTA VUELTA: gerber_emyth**
> # **CLASE DE ESTA VUELTA: EXTRACCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

**LA CADENCIA LA DICE EL INSTRUMENTO Y EL COMANDO LLEVA EL NUMERO DE ESTA VUELTA**, corrido por mi
**despues** de anotar mis cinco deudas, que es la correccion de mi propio fallo de la vuelta pasada
(`ACTA G7` `5`, segundo parrafo):

    $ python scripts/deuda.py --clase 8
    LIBRE
      van 2 de 5 desde la ultima de saneamiento (la 6), con 45 deuda(s) esperando

**`LIBRE` no es una clase: es la ausencia de obligacion de sanear.** La cadencia se reinicio con tu
vuelta `6`, asi que la clase la elige este encargo segun el libro, y la elige **`EXTRACCION`**.

**Y EL TABLERO DA PERMISO** (`D.49`, `D.51`):

    $ python forja.py tablero --puedo gerber_emyth
    LINEA 'gerber_emyth', LIBRO 'gerber_emyth': SI
      'gerber_emyth' ya es de esta linea ('gerber_emyth'): continuarlo es lo que toca.

---

## 0. COMO TE FUE, EN UNA TABLA, PARA QUE NO TENGAS QUE LEER EL ACTA ENTERA

| lo que mide la `ACTA G7` | resultado |
|---|---|
| las `21` piezas de tus dos fronteras, recompuestas con codigo que no es el tuyo | **las `21` al digito**, `5396` y `4431`, residuo `0`, `0` solapes, `0` sin cubrir, **y las dos acaban en la ultima linea real** |
| tus `51` pasos, contados ficha a ficha y **leidos uno a uno** contra su parrafo, no por muestra | **`26` y `25` al digito, `0` PUENTE en los `51`** |
| `PASOS INVENTADOS POR CAPITULO` | **te FIRMO las dos filas en `0,00` por ciento**, y el total del lote |
| tus seis informes de aduana, re corridos por mi | **los seis `0 CAERIA`**, cuatro identicos al milesimo y dos con vecinos de mas **por el orden, no por discrepancia** |
| tu muestra de fidelidad con semilla `gerber_v7` | **identica byte a byte** (`diff` vacio) |
| tus dos discutibles marcados | **los dos se sostienen**, y al segundo le aniado la linea que lo separa de su gemelo aparente (`cap_19` `L45`) |
| `d110` y `d117` | **las dos pagadas de verdad**, la correccion de `d117` tachada sin borrar donde tocaba |
| ficheros de dato o de maquinaria movidos | **`0`**, medido con `git diff` entre tus dos commits |
| tus cinco rachas | **las cinco en `0`**. `REPORTE` **baja de `2 de 3` a `0 de 3`** |

> ### **LO QUE SE CAE ES UN ORDINAL, Y NO ACUMULA**
>
> Tu `G7.4.d` dice del par de `0.446`: *es el primer caso que este frente mide por encima de `0,4` sin
> ser gemelo*. **Este mismo fichero ya traia dos**, los dos de tu vuelta `4` y los dos adjudicados
> `SANO`: `0.489` y `0.430` (`REPORTE.md` `58285` y `58288`, tabla de lectura en `58293`). **Y mi re
> corrida levanta un cuarto**, `0.451`, que tu informe no pudo ver porque el vecino se escribio
> despues. **Tu lectura del par se sostiene entera y te la firmo: lo falso es el ordinal, no el
> veredicto.**
>
> **VIVE EN PROSA DE ACOMPANIAMIENTO**, no en tabla ni en cabecera ni en la conclusion, **asi que
> `5.2` dice que NO acumula**, y `5.4` dice que una tanda con caidas solo de las que no acumulan
> **reinicia la racha igual**. **`REPORTE` vuelve a `0 de 3`.** Queda anotada como `d122`.

> ### **Y LO QUE CORRIJO ES MIO, NO TUYO**
>
> Tu celda de `G7.4.e` dice del paso `6` de la serie *no se toca nunca (`D.45`)*. **`D.45` no dice
> eso** (es el paralelo que extrae contra el serial que inserta) **y la regla que si aparta ese
> material dice otra cosa**: `ORDEN_DE_LOTES.md` linea `27`, lote `11`, **`RESERVADO. Entra el
> ultimo`**. **Pero la palabra `nunca` sale de mi encargo**, asi que la declaro sin cargartela (`d123`)
> y **la corrijo aqui, que es donde nacio**: el material del paso `6` **entra el ultimo, y no lo toca
> este frente**. Las dos cosas, y en ese orden.

---

## 1. TAREA `1`: **LOS REGISTROS, Y UNA CORRECCION DECLARADA DE UNA LINEA**

1. **Registra en tu reporte** que la `ACTA G7` deja **las cinco rachas en `0`**. **Mide el credito y
   pega la salida**, no la copies de aqui:

        python forja.py credito

2. **Escribe la deuda de apertura con su salida**, que hoy sale de `45` pendientes y `38` pagadas:

        python scripts/deuda.py

3. **LA CORRECCION DECLARADA, Y ES DE UNA CELDA:** en la tabla de tu `G7.4.e`, la fila del paso `6`
   dice *no se toca nunca (`D.45` de esta vuelta, decision del fundador)*. **Tachala sin borrarla** y
   escribe al lado lo que la regla vigente dice, con su cita de linea:

        $ grep -n "cap17_reservado" docs/loop/ORDEN_DE_LOTES.md | head -1
        27:| **11** | `gerber_emyth_cap17_reservado` | 1 | 3.845 | **RESERVADO. Entra el ultimo** |

   **Es prosa dentro de una celda, no una tabla tallada desde un instrumento**, asi que **aqui se
   tacha y no se regenera**. **Y paga `d123`** con `python scripts/deuda.py --pagar d123 --vuelta 8
   --como "..."` y la salida pegada.

> **NO TE PIDO NINGUN REMEDIO MAS Y NO HAY NINGUNA TAREA BLOQUEANTE.** `D.55` deja **una** y solo con
> guarda de DATO en rojo; **no tengo ninguna en rojo**. Lo demas de lo que encontre esta en `d122`,
> `d124`, `d125` y `d126`, **agendado, no encargado**.

---

## 2. TAREA `2`: **`cap_20`, `A Letter to Sarah`**

**`cap_20`** (`Cap. 19`, *A Letter to Sarah*, **`1841`** palabras de cuerpo, **`79`** lineas, contadas
por mi con el cuerpo arrancando en `L8`).

1. **Publica la frontera pieza por pieza antes de extraer nada**, con el instrumento que vienes usando
   (`.gerber_v5/frontera.py` y su fichero de piezas), y **pega la tabla entera**. Residuo `0`, `0`
   solapes, `0` lineas sin cubrir.

   > **Y EL BORDE DE ARRIBA LO COMPARAS TU CONTRA `wc -l`**, porque la guarda no lo hace (`d109`, y la
   > moratoria sigue en pie). **Las dos fronteras de tu vuelta `7` lo cumplieron y te lo firme: no lo
   > pierdas en la que cierra el libro.**

2. **Cada candidato pasa por la aduana en el mismo acto en que se escribe** (`EXTRACTOR.md` `16`), con
   su informe pegado. **Cero inserciones al grafo** (`MODO_INSERCION=cuarentena`, `D.39`).

3. **Marca tus discutibles ANTES de saber si aciertas**, con su numero y su linea. **Tope `2` abiertos**
   (`D.61`), y cada uno **se ejecuta o se cierra con su motivo y la linea delante en esta misma vuelta**.

> **ES UNA CARTA, Y ESO NO DECIDE NADA POR TI.** Si la vara de `9.1` no encuentra inventario propio del
> libro, **el capitulo se registra MINADO CON CERO CANDIDATOS y se dice por que**, que es lo que
> `cap_16` y `cap_17` ya hicieron en este frente. **Cero candidatos con su razon es un resultado; cero
> candidatos sin razon escrita es un hueco.**

---

## 3. TAREA `3`: **`cap_21`, el `Epilogue`**

**`cap_21`** (*Epilogue: Bringing the Dream Back to American Small Business*, **`1851`** palabras de
cuerpo, **`149`** lineas, contadas por mi). **Mismo procedimiento que la `TAREA 2`**: frontera antes de
cortar con su borde comparado, aduana en el acto, discutibles marcados antes.

---

## 4. TAREA `4`: **`cap_22`, el `Afterword`, Y EL LOTE QUE CIERRA**

**`cap_22`** (*Afterword: Taking the First Step*, **`904`** palabras de cuerpo, **`129`** lineas,
contadas por mi). Mismo procedimiento.

**Y AL CERRARLO, DECLARA EL ESTADO DEL LOTE CON SU MEDIDA, sin decidir nada:**

- **cuantas unidades del lote `9` quedan sin minar**, contadas por ti contra `fuentes/gerber_emyth/`.
  Hoy son `6`: `cap_20` a `cap_22` (los de esta vuelta) y `cap_01` a `cap_03`, **que siguen en `d094`
  por decision del fundador y NO se tocan**;
- **si los tres caben, el lote `9` queda minado entero salvo `d094`**, y eso **lo declaras, no lo
  ejecutas**: la insercion es serial y de ningun frente (`D.45`), y **la cosecha es del fundador**;
- **si un solo capitulo pasa del techo de candidatos, la vuelta CIERRA AHI y lo dices con su cifra**
  (`EXTRACTOR.md` `12.4`). **Una vuelta que cierra corta y no lo declara es caida de `REPORTE`.**

**EL TECHO DE ESTA VUELTA: `30` candidatos, hasta TRES capitulos** (`EXTRACTOR.md` `15`, regimen
`EXTRACCION`). **Los tres caben en el tramo: son `4596` palabras entre los tres, menos que tu `cap_18`
solo.**

---

## 5. TAREA `5`: **EL CIERRE, Y EL INVENTARIO QUE HEREDA LA VUELTA QUE INSERTE**

Lo de siempre, con su salida pegada: **`gate` a TRES lineas** (`d103`), `guiones`,
`tests/test_aceptacion.py`, `tallar_reporte.py`, `censar_rutas.py`, las cifras de cierre
**recomputadas y no copiadas** de la apertura, las condiciones de parada una a una con su medida, y
`python forja.py credito` **medido y no anotado**.

| pieza | como |
|---|---|
| **`PASOS INVENTADOS POR CAPITULO`**, una fila por capitulo | `8.2`: la escalada se decide **sobre el peor capitulo**, no sobre el promedio |
| **el total del lote**, ademas de las filas | sirve para comparar lotes, **no decide el volumen** |
| **la muestra de fidelidad con su semilla escrita** | `python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_20,cap_21,cap_22 --semilla <la tuya>` |
| **si un capitulo pasa del `10` por ciento** | **ese capitulo se relee entero antes de seguir** (`D.58`). No es recomendacion |
| **LA TABLA DE CIERRE EN SU ORDEN** | tu tabla primero, `python scripts/tabla_de_cierre.py --escribir` despues, y `cat` para comprobar que trae **tus** filas. **Ese remedio de `d112` lleva dos vueltas funcionando** |

**Y UNA COSA MAS, QUE ES LA QUE LA INSERCION NO PUEDE PERDER** (`ACTA G7` `6`): **publica en una tabla
los punteros `D.37` que tu bandeja deja abiertos**, con la linea de la madre que nombra a cada hijo.
Hoy son tres, y el tercero ya tiene su par:

    d098   D.37, cap_05 L29, la terna sin cabeza
    d104   D.37, cap_12 L21, la terna sin cabeza
    d111   la serie de cap_13: el paso 8 de recorrer_siete_pasos_programa_desarrollo_negocio dice
           "Paso 5: Your People Strategy", que es el titulo de
           construir_estrategia_gente_cuatro_componentes. ARISTA DECLARABLE POR LECTURA.

**NO LA DECLARES TU.** `EXTRACTOR.md` `15.6` dice que esas aristas se declaran **en la misma vuelta en
que se INSERTAN las partes**, y esta no inserta. **Lo que te pido es la tabla, para que la vuelta que
inserte no tenga que volver a leer el libro para encontrarla.**

---

## 6. LO QUE NO HACES, Y NO ES NEGOCIABLE

- **NO INSERTAS.** `MODO_INSERCION=cuarentena`. Cero nodos al grafo (`D.39`).
- **NO TOCAS EL ARNES NI LA MAQUINARIA.** `D.45`, moratoria total: `orquestador_forja.sh`, `src/`,
  `scripts/`, `tests/`, `hooks/` y `esquema/`. **Mides y subes, no arreglas.** Eso cubre `d106`,
  `d109`, `d119` y `d124`, que son las cuatro que mas pican.
- **NO ESCRIBES DOCTRINA.** La cola se queda en `11` (`D.55`). Si encuentras una pregunta nueva,
  **registrala con su medida y dejala ahi.** Si una lectura te pide mover la vara de `9.1`, **eso si es
  parada y se trae.**
- **NO TOCAS `cap_01`, `cap_02` NI `cap_03`.** Siguen en `d094` por decision del fundador.
- **NO TOCAS `fuentes/gerber_emyth_cap17_reservado`.** Es el paso `6` de la serie y **entra el ultimo**
  (`ORDEN_DE_LOTES.md` lote `11`), **en otra clave del tablero y no en este frente.**
- **NO TE ESCRIBES TU FILA DE CREDITO.** La mide `python forja.py credito`, que es de solo lectura; la
  anota el auditor.
- **NO PUBLIQUES UNA CIFRA NI UN ORDINAL QUE NO HAYAS CORRIDO EN ESTA VUELTA.** Es la caida de la `7`,
  y la palabra que la produjo fue **`primer`**: **un `primero`, un `unico` o un `ninguno` es una
  busqueda, y una busqueda se corre antes de escribirla.**

---

## 7. LOS PUNTEROS QUE NO SE PUEDEN PERDER

- **`d098`** (`D.37`, `cap_05` `L29`) y **`d104`** (`D.37`, `cap_12` `L21`): las dos ternas sin cabeza.
  **Para la vuelta que INSERTE.**
- **`d108`**: releer `cap_14` `L27` contra `L117`. **Para la vuelta que INSERTE.**
- **`d111`**: la serie de `cap_13`, medida en `0` de `7` cabezas **y con su primera arista declarable
  ya identificada** (`TAREA 5`). **No decides nada: la publicas.**
- **`d122`** (nuevo, tuyo): el ordinal sin busqueda corrida. **Ya declarado, no hay que corregir nada
  en el reporte:** la lectura del par era buena.
- **`d123`** (nuevo, **y es mio**): el rotulo del reservado. **Se paga en la `TAREA 1`.**
- **`d124`** (nuevo): la copia de una cita verbatim deja de ser verbatim al pasar el barrido de
  guiones. **Medido: `3` lineas de `29`. No se arregla desde un frente.**
- **`d125`** (nuevo): `PARALELO.md` `4.d` fotografia este frente en `10` candidatos y `4 de 22`
  capitulos; hoy son `22` y `16 de 22`. **Sede del fundador: se mide y se sube.**
- **`d126`** (nuevo, **y es mio**): el segundo ejemplar de `d124` lo produje yo al medirlo. El fichero
  con el que compare la cita contra su fuente **puso el barrido de guiones en ROJO en mi propio
  turno**, y hubo que borrarlo. **Si escribes una copia de un parrafo de este libro fuera de
  `fuentes/`, te va a pasar igual: cuentalo con esta ficha delante en vez de descubrirlo.**

**Y LA CADENCIA, PARA QUE NO TE PILLE:** la `6` reinicio el contador. **La `9` y la `10` salen
`LIBRE`; la `11` es la siguiente de saneamiento** si nada cambia. Compruebalo tu con `--clase` y el
numero de la vuelta que mires, **no con el de la anterior**.

---

## 8. AL CERRAR

- **Repasa `D.61` contra tu propio reporte antes de cerrarlo**: por cada discutible que publiques, o
  esta **ejecutado** o esta **cerrado con su motivo y la linea delante**. Ninguno abierto, tope `2`.
- **Mide `python forja.py credito`** y pega la salida. **No uses `--anotar`.**
- **Mide las condiciones de parada una a una y publica que las mediste.**
- **Commitea `docs/loop/` y tu carpeta de evidencia.**
- **Si nada te obliga a parar, NO escribas `PARA_ALEXIS.md`.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente,
paras y lo traes. No adivines.**
