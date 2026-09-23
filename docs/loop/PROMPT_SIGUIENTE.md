# ENCARGO DE LA VUELTA 65: **LA INSERCION DE GROVE, POR FIN. LAS `20` PRIMERAS FILAS DEL ORDEN QUE LA `64` DEJO COMPROBADO, UNA POR VEZ, CON SUS VEREDICTOS YA ESCRITOS**

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 63`, que audito
la vuelta `64`. `AUDITOR_FORJA.md` seccion `1.4`.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: INSERCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **LA REGLA DEL TURNO, EN SU FORMA DE INSERCION**

**La `63` no inserto nada porque su extractor lanzo `insertar` en segundo plano y cerro el turno.** En
esta vuelta:

> **UN `insertar` POR VEZ, EN PRIMER PLANO, Y NINGUNO EN VUELO CUANDO TU TURNO TERMINE.** Cada candidato
> entra entero o no entra. **Al volver cada `insertar`: su fila en el reporte, commit y push.** Asi, si el
> turno se corta, lo insertado esta registrado y lo que falta es exactamente lo que no tiene fila.

**EL RELOJ, MEDIDO Y NO PROMETIDO:** la aduana de una ficha contra poblacion `462` tardo de `826` a `1979` s
con seis en paralelo (`.v64aud/barrido.log`) y paso de `590` s sola sin terminar (`REPORTE` `64.2.c`).
**Veinte son horas.** No es un techo: si decides parar antes de la fila `20`, paras **entre dos
inserciones**, lo dices con la fila donde paraste, y lo que queda pasa a la `66` en el mismo orden.

**LOS CERROJOS:** de los tres de `procesos/`, **solo `nodos.jsonl.679b2259.cerrojo` es del dataset de este
arbol** (`.v64aud/normal/cerrojos.txt`), huerfano desde la `63`: **lo rompe y lo declara tu primer
`insertar`** (`D.44`). Los otros dos no los toques.

## LA CLASE Y EL LIBRO, DICHOS POR EL INSTRUMENTO

    $ python scripts/deuda.py --clase 65
    LIBRE
      van 1 de 5 desde la ultima de saneamiento (la 64), con 52 deuda(s) esperando

    $ python forja.py tablero --puedo grove_high_output
    LINEA 'serial', LIBRO 'grove_high_output': SI
      'grove_high_output' esta COSECHADO y sin dueño: su trabajo ya llego a esta rama, asi que se continua desde el capitulo siguiente al ultimo minado (cap_18), citando su frontera. D.50.

---

## TAREA 1: **REGISTROS DE LA `ACTA 63`**

En una tabla corta y sin reabrir el argumento (`D.47`):

| que | donde |
|---|---|
| **Tus siete discutibles se sostienen, `D64.1` a `D64.7`**, y **las cinco discrepancias con la apertura sellada las ganas tu**: `emparejar` paso `1` es T, `construir_grafico` paso `5` y `elegir_fabricar` paso `8` son P, `dimensionar_inventario` es CONTINUA de `detectar`, y `construir_grafico` es madre de `casar_flujo`. **`cap_03`, los seis de `d005`: `2` de `41`, el `4,88` por ciento** | `ACTA 63` `63.3` y `63.5` |
| **El hueco que declaraste (vecinos nuevos fuera de los `22`) esta cerrado en verde**: el barrido completo de la fase ciega da tus seis bloques exactos y las mismas seniales en los `24` pares | `63.4` |
| **`REPORTE` sube a `1 de 3`**: el bloque `$` de `64.2.c` no trae ninguna linea de su salida ni la formula, y tu tabla de `64.1` decia que el unico corte era el de `64.0` | `63.2` |
| **`R5` sigue vivo, y se mide con DOS instrumentos**: `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py`, los dos con la cabecera del tramo cambiada a la vuelta `65` | `63.11` |

## TAREA 2: **ANTES DEL PRIMER `insertar`, TRES COMPROBACIONES PEGADAS**

1. **Que lo que entra es lo que se leyo.** La fidelidad de los `22` de `cap_02` y `cap_03` esta leida
   **entera**: los `16` de la `63` sobre `b63405c` (`ACTA 62` `62.5` y `62.6`) y los seis de `d005` sobre
   `997054d` (`ACTA 63` `63.3.a` y `63.5`). **`D.58` pide esa lectura entera sobre lo que entra, y ya esta
   hecha sobre esos mismos bytes**, asi que no se repite: se comprueba.

       python .v64aud/normal/pasos_y_huellas.py

   Tiene que decir `22` iguales y `0` distintas. **Si una ficha sale distinta, esa se relee entera contra su
   capitulo antes de insertarla**, y se dice.
2. **La tabla de la tanda, pegada de su instrumento** (`python .v64ext/orden.py`), con sus tres
   comprobaciones en cero. **Las `20` filas de la tanda son la `1` a la `20`**; `variar_frecuencia_inspeccion_nivel_calidad`
   y `simplificar_trabajo_reducir_numero_pasos` (filas `21` y `22`) **no entran en esta vuelta**.
3. **El censo al abrir**: `346` nodos, `740` veredictos, `1` par mutuo, `91` en la bandeja de Grove, y lo
   que haya en `cuarentena/_insertados/grove_high_output/`.

**POR QUE ESTE ORDEN Y NO OTRO:** no lo elijo yo ni tu (`D.36`). Aplica los criterios que fijo quien
autorizo la insercion (`DOS SEMANAS` punto `4`, y el encargo de la `63` punto `2.a.2`: **por capitulo, y la
madre antes que el hijo**) mas `D.36`, y `orden.py` los comprueba. **Si al insertar aparece una madre nueva
que el orden no tiene delante, paras esa rama de la cola y lo traes**: no reordenes a mano.

## TAREA 3: **LA TANDA, FILA A FILA**

**Por cada fila, en su orden:**

    python forja.py insertar cuarentena/grove_high_output/<id>.json --sin-preguntas --veredicto "<linea>" [--veredicto "<linea>" ...]

- **Las lineas `--veredicto` se copian de su bloque en `.v64ext/veredictos_listos.txt`**, tal cual: son `49`
  en `17` bloques, leidas con los pasos delante y adjudicadas en la `ACTA 63`. **No se reescriben.** Las de
  `detectar_arreglar_fallo_etapa_menor_valor` son las de `.v63ext/cmd_02_detectar.sh`.
- **LA PUERTA ES LA ADUANA DE `insertar`, NO LA LISTA** (`d031`): corre contra el grafo y las bandejas de ese
  momento. **Si levanta a un vecino que no tiene linea**, lo lees con los pasos de los dos delante, escribes
  su veredicto por la vara `6.1` de `AUDITOR_FORJA.md` y solo esa, **y lo marcas en el reporte como lectura
  tuya de esta vuelta**, discutible si dudas. **Si un vecino con linea ya no se levanta**, no pasas su linea y
  lo dices.
- **Si la aduana dice algo que no esperas** (`CAERIA`, un error, un gate rojo), **no fuerces**: ese candidato
  no entra, **sus hijos de la lista tampoco**, y sigues con el siguiente que no dependa de el. Se declara.
- **LAS ARISTAS POR LECTURA (`D.29`, `D.53`)**: las `8` filas `SOSTENGO` de `.v64ext/aristas_lectura.txt`
  tienen madre e hijo dentro de las `20`. **Se cablean en el acto de insertar el hijo, con la madre ya en el
  grafo**, con `python forja.py arista --madre --hijo --paso --razon` y la razon de su fila. **La de
  `construir_indicador_tendencia_patron` a `dimensionar_plantilla_administrativa_pronostico` ya va como
  `CONTINUA` en los veredictos**: no la cablees dos veces.
- **La de `detectar_arreglar_fallo_etapa_menor_valor` a `supervisar_tarea_delegada_etapa_menor_valor` queda EN
  COLA** (`D.29`): el hijo es de `cap_04` y sigue en la bandeja.
- **Cada insertado va a `cuarentena/_insertados/grove_high_output/` con su commit de insercion** (`D.31`).
- **Al volver cada `insertar`, su fila en el reporte**: id, lo que la aduana dijo hoy (veredicto y vecinos),
  las lineas de veredicto que escribio, las aristas que cableaste, **y su commit**.

## TAREA 4: **EL CIERRE**

- **El censo antes y despues**: nodos, veredictos, pares mutuos, bandeja de Grove e insertados. Si entran
  las `20`, el grafo queda en `366` y la bandeja en `71`.
- **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo sobre lo que ENTRO**, contada por un instrumento
  desde las lecturas enteras ya adjudicadas (`ACTA 62` `62.6` para `cap_02` y los nueve de `cap_03` de la
  `63`, `ACTA 63` `63.5` para los seis de `d005`), no desde cero y no a ojo.
- **`D.61`**: cada discutible ejecutado o cerrado. Ninguno abierto.
- **`R5`** en cada bloque `$` de tu tramo, **medido con los dos instrumentos de la TAREA 1** y pegado.
- `python forja.py gate`, `python forja.py guiones`, `python tests/test_aceptacion.py` y
  `python scripts/cerrar_reporte.py`, **en verde y pegados**.
- Commitea `docs/loop/`, `dataset/`, `bitacora/`, `censos/`, los movidos a `_insertados` y tu carpeta
  `.v65ext/`. **Si nada te obliga a parar, no escribas `PARA_ALEXIS.md`.**

---

## LO QUE NO HACES

- **NO LANZAS NADA EN SEGUNDO PLANO QUE TOQUE EL DATASET.** Ni un `insertar` fuera del primer plano.
- **NO TOCAS `cuarentena/gerber_emyth/`**, que va despues de Grove, ni el frente `marquet_turn_the_ship`,
  que tiene dueno (`D.49`).
- **NO TOCAS `src/`, el banco, el arnes ni los protocolos** mientras corra el frente de Marquet (`D.45`).
- **NO REORDENAS LA COLA A MANO** ni metes las filas `21` y `22`.
- **NO ABRES NINGUN LIBRO.** El mundo `11` cierra con siete.

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente,
paras y lo traes. No adivines.**
