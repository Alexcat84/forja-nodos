# ENCARGO DE LA VUELTA 71: **LAS `20` FICHAS SIGUIENTES DE GROVE (`cap_07`, `cap_10`, `cap_11`, `cap_12`, `cap_13` Y `cap_14`) DEJADAS LISTAS PARA INSERTAR: SU FIDELIDAD LEIDA ENTERA, SUS VECINOS BARRIDOS, SUS VEREDICTOS ESCRITOS, SUS ARISTAS LEIDAS Y SU ORDEN COMPROBADO. AQUI NO SE INSERTA NINGUNA**

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 69`, que audito la vuelta `70`.
`AUDITOR_FORJA.md` seccion `1.4`.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: INSERCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **LA REGLA DEL TURNO, Y POR QUE ESTA VUELTA NO INSERTA**

**La tanda que estaba lista entro entera en la `70`** (`ACTA 69`): no queda nada adjudicado que insertar. Esta vuelta hace para
las `20` fichas siguientes lo que la `68` hizo para `cap_05` y `cap_06` (su TAREA 3), que llevo a la `70` a meter `20` de `20` sin
una sola sorpresa. **Es regimen de insercion (`D.58`): la relectura de fidelidad del lote se hace ENTERA, aqui, antes de que entre.**
Su insercion es de la vuelta siguiente, despues de que mi fase ciega barra y lea lo que dejes y la `ACTA 70` lo adjudique.

**PUEDES LANZAR BARRIDOS DE FONDO, CINCO A LA VEZ COMO MUCHO, PERO NINGUNO VIVO AL CERRAR TU TURNO**: los recoges todos dentro,
vigilandolos si tardan. **Si no te caben, no los lances: lo dices en el reporte con los que faltan.** El `23` sep tres asientos
cerraron diciendo que esperaban un trabajo de fondo, y ninguno volvio. **Y NINGUN `insertar`**, ni en primer plano ni de fondo.

**EL RELOJ, MEDIDO:** el barrido de las `20` fichas de `cap_05` y `cap_06` en la `68`, cinco a la vez, fue de `18:29:53` a
`21:23:47` (`.v68ext/barrido.log`), con fichas de `2400` a `4200` s. **No es un techo: es lo que costo.**

## LA CLASE Y EL LIBRO, DICHOS POR EL INSTRUMENTO

    $ python scripts/deuda.py --clase 71
    LIBRE
      van 2 de 5 desde la ultima de saneamiento (la 69), con 56 deuda(s) esperando

    $ python forja.py tablero --puedo grove_high_output
    LINEA 'serial', LIBRO 'grove_high_output': SI
      'grove_high_output' esta COSECHADO y sin dueño: su trabajo ya llego a esta rama, asi que se continua desde el capitulo siguiente al ultimo minado (cap_18), citando su frontera. D.50.

**El orden de la campania es Grove, Gerber, Marquet** (`PARALELO.md` `8` punto `4`). **La frase de *continuar desde `cap_18`*
es de extraccion y no aplica: Grove esta minado entero**, y lo que se hace es insertar su bandeja por capitulo (`d028`).

---

## TAREA 1: **REGISTROS DE LA `ACTA 69`**

En una tabla corta y sin reabrir el argumento (`D.47`):

| que | donde |
|---|---|
| **Las `20` filas dentro, una por vez, sin solape y en su orden**: `118` lineas iguales letra a letra a las vivas preparadas, sobre los `118` pares del barrido del auditor y con sus clases selladas; `7` aristas iguales par a par; `3` madres viejas que solo ganan su `nodos_siguientes` | `ACTA 69` `69.3`, `69.4` |
| **Tus cuatro discutibles se sostienen**, `D70.1` a `D70.4`, y la espera de fondo de la fila `10` queda declarada y sin cargo | `69.4`, `69.5` |
| **La muestra de los SANO, `20` de `20`**; `cap_05` y `cap_06` entran en `0` de `84` y `0` de `62`; la guarda `D.59` muerde por mutacion | `69.5`, `69.6`, `69.1` |
| **Cero caidas, ni de prosa**: las cinco rachas de la serial en cero y `R5` cumplido | `69.2`, `69.8`, `69.0` |

## TAREA 2: **LA FIDELIDAD ENTERA DE LAS `20`** (`D.30`, `D.58`)

Las `20` son las fichas de la bandeja de Grove cuya `UNIDAD DE ORIGEN` es `cap_07` (`9`), `cap_10` (`1`), `cap_11` (`2`), `cap_12`
(`3`), `cap_13` (`2`) y `cap_14` (`3`); **una por linea, con su capitulo y su cuenta de pasos, en `.v70aud/normal/bandeja_grove.txt`,
sus `20` primeras lineas**. Las `7` de `cap_15`, `cap_16` y `cap_17` **no son de esta vuelta**. Todo en tu carpeta `.v71ext/`, **con
copias de instrumentos que ya existen y la ruta cambiada**, no con instrumentos nuevos (`7.F`):

1. **Cada paso de las `20` contra su capitulo de `fuentes/grove_high_output/` leido entero**, marcado `T` o `P` con su linea, en un
   fichero con una fila por paso como `.v68ext/fidelidad.tsv` (la clausula reescrita CUENTA como `P`, `ACTA 62` `62.5`), y sus citas
   comprobadas con una copia de `.v68ext/citas.sh`.
2. **Todo PUENTE se corrige en la ficha de la bandeja por correccion declarada, con el texto viejo dentro, ANTES del barrido**: una
   ficha que cambia despues de su barrido tiene un barrido que ya no es suyo (`d031`).
3. **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo, seis filas**, por una copia de `.v68ext/contar_fidelidad.py`, **y el
   peor capitulo nombrado** (`8.2`). **Si uno pasa del `10` por ciento, ese capitulo se relee entero antes de seguir** (`D.58`).
4. **Marca discutible todo paso en que dudes, al escribirlo.**

## TAREA 3: **EL BARRIDO DE LAS `20`, SOBRE LAS FICHAS YA CORREGIDAS**

Contra **GRAFO MAS BANDEJAS** (`D.38.4`), con copias de `.v68ext/barrido_uno.py` y `.v68ext/barrer.sh` con la lista de las `20` y la
ruta `.v71ext/`: **cinco a la vez como mucho, un log con su `INICIO` y su `TODOS TERMINADOS`, y las `20` recogidas dentro de tu
turno.** La poblacion al abrir es `479`: `410` del grafo mas `69` de bandejas (`27` de Grove, `22` de Gerber y `20` de Marquet,
`ACTA 69` `69.1`). **Una tabla por candidato de sus vecinos**, como `.v68ext/` la dejo para la `70`.

## TAREA 4: **LOS VEREDICTOS, LAS ARISTAS Y EL ORDEN**

1. **Los veredictos listos, uno por vecino**, en el formato de `--veredicto` y con un bloque por candidato como
   `.v68ext/veredictos_listos.txt`: **leidos con los pasos de los dos delante** (`python .v64aud/pasos.py <a> <b>`) y por la vara
   `6.1`, y solo esa. **Y comprobado por instrumento que cada vecino del barrido tiene su linea y cada linea su vecino**, con una
   copia de `.v69ext/comprobar_veredictos.py`.
2. **Las aristas por lectura** (`D.29`, `D.53`), en un fichero como `.v68ext/aristas_lectura.txt`, con su tramo de madre y de hijo
   y su linea del libro, **mirando tambien madres que ya viven en el grafo** (la `70` cableo tres asi). **`D.37`**: los titulos que
   dicen cuantas partes tienen se miran como en la `68`, y aqui hay varios: `planificar_tres_pasos_demanda_estado_brecha` contra
   `examinar_demanda_entorno_dos_marcos_temporales`, `determinar_estado_presente_capacidades_proyectos_merma` y
   `cerrar_brecha_dos_preguntas_estrategia`; y las *dos preguntas* de `cerrar_brecha` y de
   `contestar_dos_preguntas_direccion_objetivos`. **Si alguna parte es nodo, la arista cabeza a parte se declara; si la cabeza solo
   cuenta y nombra, es la figura de `D68.7`, que la conjunta de la `69` cerro sin arista.** Marca discutible lo que dudes.
3. **`d170`, EN ESTA TANDA**: `elegir_estilo_direccion_madurez_relevante_tarea` (`cap_13`) y
   `fijar_frecuencia_reunion_individual_madurez_tarea` (en el grafo desde la `70`). **La conjunta de la `69` lo decidio: NO es
   arista** (`D69.3`, `ACTA 68` `68.5`). Si tu barrido levanta el par, su linea es `SANO` con esa cita; si no lo levanta, no hay
   linea ni arista. **Dilo en el reporte con la salida del barrido delante.** `d170` se paga en la vuelta que inserte la ficha.
4. **El orden de insercion de las `20`**, con una copia de `.v69ext/orden.py`: **madre antes que hijo, `D.36`, y las comprobaciones
   en cero.**

**Si no te cabe todo, parte por capitulo y por donde se pueda auditar**: `cap_07` entero antes que los demas, y dentro de cada uno
la fidelidad antes que el barrido y el barrido antes que los veredictos. **Lo que no hagas lo dices con su fila vacia**, y la
vuelta siguiente empieza por ahi.

## TAREA 5: **EL CIERRE**

- **El censo antes y despues**: nodos, veredictos, pares mutuos, bandeja de Grove e insertados. **No entra nada**: `410`, `1027`,
  `1`, `27` y `65` al abrir y al cerrar.
- **`PASOS INVENTADOS POR CAPITULO`, seis filas**, que son **preparacion y no entrada**.
- **La huella de las `20` fichas preparadas**, con una copia de `.v70ext/pasos_y_huellas.py` con la lista de las `20`, corrida
  despues del ultimo cambio de ficha y pegada: es contra lo que la vuelta de insercion comprobara que entra lo que se leyo.
- **`D.61`**: cada discutible ejecutado o cerrado. Ninguno abierto.
- **`R5`** en cada bloque `$` de tu tramo, **medido con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera
  cambiada a la `71`**, y pegado.
- `python forja.py gate`, `python forja.py guiones`, `python tests/test_aceptacion.py` y `python scripts/cerrar_reporte.py`,
  **pegados**. **El cierre estricto tiene que salir en verde: cualquier rojo es tuyo.**
- Commitea `docs/loop/`, las fichas corregidas de la bandeja y tu carpeta `.v71ext/`. **Si nada te obliga a parar, no escribas
  `PARA_ALEXIS.md`.**

---

## LO QUE NO HACES

- **NO INSERTAS NINGUNA FICHA**, y **NO TERMINAS TU TURNO CON NADA VIVO**, ni un barrido.
- **NO TOCAS LAS `7` FICHAS DE `cap_15`, `cap_16` Y `cap_17`**: van en la vuelta que inserte estas `20`.
- **NO TOCAS `cuarentena/gerber_emyth/` NI `cuarentena/marquet_turn_the_ship/`**: van despues de Grove, en ese orden.
- **NO TOCAS `src/`, `scripts/`, el banco, el arnes ni los protocolos** (`7.F`, `D.55`), **ni `APERTURA_CIEGA.md`**.
- **NO REORDENAS LA COLA A MANO.**
- **NO ABRES NINGUN LIBRO.** El mundo `11` cierra con siete.

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No
adivines.**
