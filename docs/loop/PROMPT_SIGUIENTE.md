# ENCARGO DE LA VUELTA 7 DEL FRENTE `gerber_emyth`: **VUELTA DE EXTRACCION**, `cap_18` y `cap_19`, y la mitad de `d111` que se juega ahi

*Linea **`gerber_emyth`** (`extraccion-gerber_emyth`, worktree
`C:/Users/AlexDesk/Documents/forja-gerber_emyth`). **Escrito por el auditor del bucle** al cerrar la
`ACTA G6`, que audita tu vuelta `6`.*

> # **LIBRO DE ESTA VUELTA: gerber_emyth**
> # **CLASE DE ESTA VUELTA: EXTRACCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

**LA CADENCIA LA DICE EL INSTRUMENTO Y EL COMANDO LLEVA EL NUMERO DE ESTA VUELTA**, que es justo lo
que el encargo anterior hizo mal (`ACTA G6` `5.1`):

    $ python scripts/deuda.py --clase 7
    LIBRE
      van 1 de 5 desde la ultima de saneamiento (la 6), con 39 deuda(s) esperando

**`LIBRE` no es una clase: es la ausencia de obligacion.** La cadencia se reinicio con tu vuelta `6`,
asi que la clase la elige este encargo segun el libro, y la elige **`EXTRACCION`**.

---

## 0. COMO TE FUE, EN UNA TABLA, PARA QUE NO TENGAS QUE LEER EL ACTA ENTERA

| lo que mide la `ACTA G6` | resultado |
|---|---|
| las `7` piezas de `cap_15` con la celda ya corregida, recompuestas con codigo que no es el tuyo | **las `7` al digito**, residuo `0`, `0` solapes, `0` sin cubrir, **y `R7` acaba ya en la ultima linea real** |
| que la correccion fuese quirurgica | **`4` lineas borradas del reporte y ninguna mas**, `D.41` cumplida por donde pica |
| tus tres pagos (`d102`, `d103`, `d112`) | **los tres reproducen y los tres se firman** |
| tus dos deudas dejadas vivas (`d106`, `d107`) | **las dos se sostienen con su razon**, y `d107` por el motivo cierto: `1` candidato en la vuelta `5` |
| las ocho que no pagas | **los ocho motivos se sostienen**, repasados uno a uno |
| el duplicado de `DEUDA.jsonl` que declaraste tu mismo | **NO es `DATO MOVIDO`**, y se te firma la declaracion: `1` linea en el registro, `4` en el commit |
| `PASOS INVENTADOS POR CAPITULO` | **cero poblacion**, `0` capitulos minados y `0` pasos escritos, publicado con su medida |
| tus cinco rachas | `CIFRA PUBLICADA`, `CLASE`, `DATO MOVIDO` y `AUDITOR` en `0`; **`REPORTE` sube a `2 de 3`** |

> ### **LO QUE SE CAE ES LA CABECERA, Y LA RAIZ ES MIA**
>
> Tu bloque abre diciendo que la clase te la dicto `python scripts/deuda.py --clase 5` citando `G6.1`, y
> que la linea *va `4` de `5`*. **El rotulo `SANEAMIENTO` es cierto**, pero **ese comando imprime
> `LIBRE`**, `G6.1` **no trae ninguna salida de `--clase`** (`ls .gerber_v6/ | grep -c clase` da `0`), y
> en la vuelta `6` la cuenta es **`5` de `5`**, no `4` de `5`. **Una cuenta de `4` de `5` no alcanza una
> cadencia de `5`: la frase justifica el rotulo con el numero que lo desmiente.** Y ese `4` de `5` esta
> **copiado de `REPORTE.md` `59300`**, que es el reporte de tu vuelta anterior, y `EXTRACTOR.md` `5` dice
> que una nota vieja **nunca** es fuente de una cifra nueva. **Vive en CABECERA, y `5.2` dice que en
> cabecera acumula.**
>
> **LA RAIZ ES MIA Y VA DECLARADA ANTES QUE LA TUYA** (`ACTA G6` `5.1`): yo te puse ese comando delante
> en dos sedes. **Queda anotado como `d117` y corregido en este encargo**, que escribe `--clase 7`.
>
> **Y CAE UNA SEGUNDA, QUE NO SUMA OTRO ESCALON PORQUE LA RACHA CUENTA TANDAS:** tu `G6.6` dice *las
> nueve filas de la tabla de deuda* y la tabla del encargo tenia **`12`**. La declaro sin cargarla
> aparte, porque existe una lectura en la que `nueve` es cierto (las nueve que no se pagan).

> ### **LO QUE ESTO SIGNIFICA PARA TI, EN UNA LINEA**
>
> **`REPORTE` va `2 de 3`. Un escalon mas y el bucle para.** Y las dos caidas de esta tanda son la
> misma especie: **una frase de cabecera o de tabla que nombra un instrumento sin haberlo corrido en
> esta vuelta.** No es un problema de lectura del libro: es de escritura del reporte.

---

## 1. TAREA `1`: **LOS REGISTROS, Y UNA SOLA FRASE DE REMEDIO QUE TE VAS A ESCRIBIR TU**

1. **Registra en tu reporte** que la `ACTA G6` deja `REPORTE` en `2 de 3` y las otras cuatro rachas en
   `0`. **Mide el credito y pega la salida**, no la copies de aqui:

        python forja.py credito

2. **Escribe la deuda de apertura y su salida**, que hoy sale de `39`, y con mis tres anotadas sube:

        python scripts/deuda.py

3. **LA CORRECCION DECLARADA QUE TE PIDO, Y ES DE UNA LINEA:** en el bloque de tu vuelta `6`, junto a la
   cabecera, **tacha sin borrar** la frase *dictada por el instrumento y no por mi lectura (`python
   scripts/deuda.py --clase 5`, `G6.1`)* y escribe al lado el comando que si la dicta (`--clase 6`) con
   su salida, y la nota de que la cifra `4` de `5` era de la vuelta anterior. **Esa frase vive en prosa
   dentro de una cita de bloque, no en tabla tallada**, asi que aqui **si se tacha y no se regenera**:
   es el caso contrario al de tu `TAREA 1` de la vuelta `6`.

   **La salida que necesitas ya esta corrida y reproducible**, y esta en mi carpeta:

        python .g6aud/clase_de_vuelta.py

   **Si tocas la tabla tallada de al lado, el tallado aborta el commit. No la toques.**

> **NO TE PIDO NINGUN REMEDIO MAS.** `D.55` deja **una** tarea bloqueante y solo con guarda de DATO en
> rojo; **no tengo ninguna en rojo, asi que esta no es bloqueante**: es el primer punto de la `TAREA 1`
> y se cierra en diez minutos. **Lo demas de lo que encontre esta en `d117`, `d118` y `d119`, agendado,
> no encargado.**

---

## 2. TAREA `2`: **`cap_18`, LA FRONTERA PUBLICADA ANTES DE CORTAR**

**`cap_18`** (`Cap. 16`, *Your People Strategy*, **`5396`** palabras de cuerpo, **`413`** lineas,
contadas por mi). Es el **paso `5`** de la serie de siete de `cap_13`.

1. **Publica la frontera pieza por pieza antes de extraer nada**, con el mismo instrumento que vienes
   usando (`.gerber_v5/frontera.py` y su fichero de piezas), y **pega la tabla entera**. Que la suma de
   piezas cuadre con el cuerpo, con **residuo `0`**, **`0` solapes** y **`0` lineas sin cubrir**.

   > **Y EL BORDE DE ARRIBA LO COMPARAS TU CONTRA `wc -l`**, porque la guarda no lo hace (`d109`, y la
   > moratoria sigue en pie). **Es la caida que la `ACTA G5` te cargo y que la `6` corrigio: no la
   > repitas en un capitulo nuevo.**

2. **Cada candidato pasa por la aduana en el mismo acto en que se escribe** (`EXTRACTOR.md` `16`), con
   su informe pegado. **Cero inserciones al grafo** (`MODO_INSERCION=cuarentena`, `D.39`).

3. **Marca tus discutibles ANTES de saber si aciertas**, con su numero y su linea. **Tope `2` abiertos**
   (`D.61`), y **cada uno se ejecuta o se cierra con su motivo y la linea delante en esta misma vuelta**.

---

## 3. TAREA `3`: **`d110`, QUE SE PAGA MINANDO `cap_18` Y NO DESPUES**

**Es la deuda que esta vuelta existe para pagar**, y la medi yo antes de encargartela:

    $ sed -n '21p;27p' fuentes/gerber_emyth/cap_18.md | cut -c1-108
    H ow do I get my people to do what I want?” This is the one question I hear most often from small business
    Since that is the question most often asked of me, I was intrigued with the hotel Manager’s answer to my q

**`cap_18` recoge literalmente la escena con la que `cap_17` corta.** Asi que:

1. **lee la apertura de `cap_18` con `cap_17` `L189` a `L221` delante**, las dos a la vez;
2. **di si el autor saca el Operations Manual del caso del hotel Venetia o lo deja dentro del dialogo**,
   y dilo **con las lineas citadas de los dos ficheros**;
3. **paga `d110`** con `python scripts/deuda.py --pagar d110 --vuelta 7 --como "..."` y la salida pegada.

> **ESTO REABRE EL DISCUTIBLE `5` DE TU VUELTA `5`, QUE LA `ACTA G5` CERRO CON LA RESERVA ESCRITA DE QUE
> EL TEXTO SEGUIA.** Si al leer las dos mitades juntas te sale que **si** hay metodo, eso **no es una
> caida de nadie**: es la deuda funcionando. **Y entonces el candidato nace en `cap_18`, no en `cap_17`.**

---

## 4. TAREA `4`: **`cap_19` SI EL TECHO LO PERMITE, Y SI NO, SE DECLARA EL CIERRE CORTO**

**`cap_19`** (**`4431`** palabras de cuerpo, **`441`** lineas, contadas por mi) es el **paso `7`** de la
serie, y **el `6` esta apartado en `fuentes/gerber_emyth_cap17_reservado` y no se toca nunca**.

- **Si `cap_18` solo pasa del techo de candidatos, la vuelta CIERRA AHI y lo declaras con su cifra**
  (`EXTRACTOR.md` `12.4`). **Una vuelta que cierra corta y no lo dice es caida de `REPORTE`**, y con
  `2 de 3` encima eso es el tercer escalon.
- **Si los dos capitulos caben, cierras `cap_19` igual que el `18`:** frontera publicada antes de
  cortar, aduana en el acto, discutibles marcados antes.
- **Y midas lo que midas, `d111` se queda para la vuelta que INSERTE.** Al cerrar `cap_18` y `cap_19`,
  la cabeza `recorrer_siete_pasos_programa_desarrollo_negocio` habra visto sus dos ultimas partes
  disponibles: **escribe en el reporte en cuanto queda la serie (`N` de `7`) con tu medida delante**, y
  **no decidas que se hace con ella**. Esa decision no es de una vuelta que no inserta.

---

## 5. TAREA `5`: **EL CIERRE, Y `PASOS INVENTADOS POR CAPITULO` CON POBLACION DE VERDAD**

Esta vuelta **si** mina, asi que la metrica vuelve a tener divisor y **es la cifra que dimensiona el
lote siguiente** (`AUDITOR_FORJA.md` `8`):

| pieza | como |
|---|---|
| **una fila por capitulo**, no una media | `8.2`: la escalada se decide **sobre el peor capitulo** |
| **el total del lote**, ademas de las filas | sirve para comparar lotes, pero **no decide el volumen** |
| **la muestra de fidelidad con su semilla escrita** | `python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_18,cap_19 --semilla <la tuya>` |
| **si un capitulo pasa del `10` por ciento** | **ese capitulo se relee entero antes de seguir** (`D.58`). No es recomendacion |

Y lo de siempre, con su salida pegada: **`gate` a TRES lineas** (`d103`), `guiones`,
`tests/test_aceptacion.py`, `tallar_reporte.py`, `censar_rutas.py`, las cifras de cierre
**recomputadas y no copiadas** de la apertura, las condiciones de parada una a una con su medida, y
`python forja.py credito` **medido y no anotado**.

**Y LA TABLA DE CIERRE, EN EL ORDEN QUE `d112` DEJO PAGADO:** tu tabla primero, `python
scripts/tabla_de_cierre.py --escribir` despues, y comprueba con `cat` que el fichero trae **tus** filas.
**Ese remedio funciono en la vuelta `6` y se te firmo: no lo pierdas.**

---

## 6. LO QUE NO HACES, Y NO ES NEGOCIABLE

- **NO INSERTAS.** `MODO_INSERCION=cuarentena`. Cero nodos al grafo (`D.39`).
- **NO TOCAS EL ARNES NI LA MAQUINARIA.** `D.45`, moratoria total: `orquestador_forja.sh`, `src/`,
  `scripts/`, `tests/`, `hooks/` y `esquema/`. **Mides y subes, no arreglas.** Eso cubre `d106`, `d109`
  y `d119`, que son las tres que mas pican.
- **NO ESCRIBES DOCTRINA.** La cola se queda en `11` (`D.55`). Si encuentras una pregunta nueva,
  **registrala con su medida y dejala ahi.** Si una lectura te pide mover la vara de `9.1`, **eso si es
  parada y se trae.**
- **NO TOCAS `cap_01`, `cap_02` NI `cap_03`.** Siguen en `d094` por decision del fundador.
- **NO TOCAS `fuentes/gerber_emyth_cap17_reservado`.** Es el paso `6` de la serie y esta apartado.
- **NO TE ESCRIBES TU FILA DE CREDITO.** La mide `python forja.py credito`, que es de solo lectura; la
  anota el auditor.
- **NO PUBLIQUES UNA CIFRA QUE NO HAYAS CORRIDO EN ESTA VUELTA.** Es la caida de la `6` y la unica que
  te queda antes del tope.

---

## 7. LOS PUNTEROS QUE NO SE PUEDEN PERDER

- **`d098`** (`D.37`, `cap_05` `L29`) y **`d104`** (`D.37`, `cap_12` `L21`): las dos ternas sin cabeza.
  **Para la vuelta que INSERTE.**
- **`d108`**: releer `cap_14` `L27` contra `L117`. **Para la vuelta que INSERTE.**
- **`d111`**: la serie de `cap_13`. **Mides en cuanto queda al cerrar `cap_19`, y no decides.**
- **`d117`** (nuevo, y es mio): el comando de la cadencia con el numero de su propia vuelta. **Ya
  corregido en la cabecera de este encargo**; si lo vuelves a ver mal escrito en un encargo, **parate y
  traelo**.
- **`d118`** (nuevo): la ficha de `d106` dice `cap_17` donde el ultimo capitulo que dejo nodo es
  `cap_15`. **No cambia el defecto de `d106`, solo su rotulo.**
- **`d119`** (nuevo, **pregunta de doctrina registrada y NO abierta**): la cadencia de un frente que
  nunca saneo cuenta desde `primera_vuelta`, que sale del registro de CREDITO, **que lo escribe el
  auditor**. Hoy no hace dano. **No se abre y no se toca.**

**Y LA CADENCIA, PARA QUE NO TE PILLE:** la `6` reinicio el contador. **La `8`, la `9` y la `10` salen
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
