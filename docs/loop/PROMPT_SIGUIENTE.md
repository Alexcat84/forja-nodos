# ENCARGO DE LA VUELTA 70: **LAS `20` FILAS DE `cap_05` Y `cap_06` DENTRO, UNA POR VEZ, CON LAS `118` LINEAS Y LAS `7` ARISTAS QUE LAS DOS LECTURAS YA COMPARTEN**

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 68`, que audito la vuelta `69`.
`AUDITOR_FORJA.md` seccion `1.4`.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: INSERCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **LA REGLA DEL TURNO, Y EL METODO QUE YA FUNCIONO DOS VECES**

> **UN `insertar` POR VEZ, Y NINGUNO EN VUELO CUANDO TU TURNO TERMINE.** Cada candidato entra entero o no entra.
> **Al volver cada `insertar`: su fila en el reporte, commit y push.**

**El metodo de la `67` y la `68` vale**: cada `insertar` lanzado como un proceso por una copia de `.v68ext/insertar.py`, y tu
bloqueado en primer plano con una copia de `.v68ext/esperar.py` hasta su `.fin`, **sin lanzar el siguiente ni tocar el dataset ni
la bandeja en medio**. **NO LANZAS NADA EN SEGUNDO PLANO QUE SIGA VIVO AL CERRAR TU TURNO.** Si algo no te cabe, no lo lances:
lo dices en el reporte con las filas que faltan, y entran en la `71`.

**EL RELOJ, MEDIDO:** la `67` metio `20` filas en `36983` s de turno, con `insertar` de `985,8` a `3988,1` s y mediana `1487,6`
contra poblacion `479`; las dos de la `68` tardaron `1786,6` y `2153,7` s (`ACTA 67` `67.8`). **No son techos: son lo que costo.**

## LA CLASE Y EL LIBRO, DICHOS POR EL INSTRUMENTO

    $ python scripts/deuda.py --clase 70
    LIBRE
      van 1 de 5 desde la ultima de saneamiento (la 69), con 56 deuda(s) esperando

    $ python forja.py tablero --puedo grove_high_output
    LINEA 'serial', LIBRO 'grove_high_output': SI
      'grove_high_output' esta COSECHADO y sin dueño: su trabajo ya llego a esta rama, asi que se continua desde el capitulo siguiente al ultimo minado (cap_18), citando su frontera. D.50.

**El orden de la campania es Grove, Gerber, Marquet** (`PARALELO.md` `8` punto `4`). **La frase de *continuar desde `cap_18`*
es de extraccion y no aplica: Grove esta minado entero**, y lo que se hace es insertar su bandeja por capitulo (`d028`).

---

## TAREA 1: **REGISTROS DE LA `ACTA 68`**

En una tabla corta y sin reabrir el argumento (`D.47`):

| que | donde |
|---|---|
| **La relectura conjunta se cierra sin discrepancia**: tus `D69.1` a `D69.3` se sostienen; de tus `118` pares dirigidos cambian justo los `8` de la cabeza, tus `70` pares sin orden son los `70` de la lectura sellada del auditor, y **tus `7` aristas esperadas son las suyas, par a par** | `ACTA 68` `68.3`, `68.5` |
| **`d053`: no se parte, y tu `D69.4` se sostiene por la vara**: la mitad de L37 cae por la restriccion `2` de `9.1` y su cifra va en `atribuciones`; L57 nombra una ETAPA y L37 una cantidad | `68.5` |
| **Saneamiento declarado y `d053` y `d056` bien pagadas**; `d170` sigue esperando a la madre | `68.4` |
| **Cero caidas, ni de prosa**: las cinco rachas de la serial en cero y `R5` cumplido | `68.2`, `68.8`, `68.0` |

## TAREA 2: **LO QUE ENTRA ES LO QUE SE LEYO**

Antes del primer `insertar`, con una copia de `.v69ext/pasos_y_huellas.py` con el commit cambiado a `4ec8c16` (el cierre de la
`69`: ninguna ficha cambio en ella, `ACTA 68` `68.1`): **las `20` fichas de la bandeja iguales a su blob en `4ec8c16`**, y sus `20`
filas iguales a las de `.v69ext/pasos_y_huellas.txt`. Si una sale distinta, no entra, se relee entera contra su capitulo y se dice.

## TAREA 3: **LAS `20` FILAS DE `.v69ext/orden.txt`, UNA POR VEZ**

**En su orden, filas `1` a `20`**: los `12` de `cap_05` y los `8` de `cap_06`. Con las `20` dentro, **los dos capitulos quedan
enteros en el grafo.**

1. **Las lineas `--veredicto` son las vivas del bloque de cada candidato en `.v68ext/veredictos_listos.txt`, tal cual, sin las
   `#`**: las que la relectura conjunta corrigio en la `69` incluidas, y ninguna de las viejas que quedaron en comentario. Las
   `CONTINUA` con `madre=` cablean su arista en el acto: `preparar_guion_reunion_individual_subordinado` a
   `tomar_notas_copia_guion_reunion_individual` en la fila `8`, y `tomar_notas_copia_guion_reunion_individual` a
   `conducir_reunion_individual_telefono_distancia` en la fila `11`.
2. **Las cinco aristas por lectura, con `python forja.py arista` en el acto de insertar el hijo**, `--veredicto CONTINUA`, su cita y
   su `--paso` el de la madre que su fila `SOSTENGO` de `.v68ext/aristas_lectura.txt` cita, como en la `67` y la `68`:
   `agrupar_tareas_semejantes_aprovechar_preparacion` y `buscar_regularidad_bloques_iguales_trabajo_mando` a
   `infundir_regularidad_reunion_proceso` (fila `1`); `agrupar_interrupciones_subordinados_reuniones_regulares` a
   `acumular_asuntos_importantes_fichero_espera` (fila `9`); y `conducir_etapas_modelo_ideal_decision` a
   `ejercer_poder_posicion_etapa_decision_clara` (fila `14`) y a `cortar_discusion_libre_momento_justo` (fila `17`). **Ninguna
   con madre `usar_tres_clases_reunion_proceso`**, y la de `D68.15` no es de esta vuelta (`d170`).
3. **La puerta es la aduana de `insertar`, no la lista** (`d031`). Si levanta un vecino sin linea, lo lees con los pasos de los
   dos delante, escribes su veredicto por la vara `6.1` y solo esa, **y lo marcas en el reporte como lectura tuya de esta
   vuelta**, discutible si dudas. Si levanta `CAERIA` o un error, no fuerces: no entra, y se declara.
4. **Al volver cada `insertar`, su fila en el reporte** como las de la `67` y la `68`: la aduana de hoy con sus vecinos, las lineas
   que pasaste, las aristas que cableaste y su commit. Cada insertado a `cuarentena/_insertados/grove_high_output/` (`D.31`).

## TAREA 4: **LAS ARISTAS DE LA TANDA, POR INSTRUMENTO**

Al terminar la ultima fila que entre: **cuantas se esperaban (`7`), cuantas viven en el grafo, y ninguna sin adjudicar**; y que
ningun nodo viejo cambio fuera del `nodos_siguientes` de sus madres. Si alguna fila no entro, la cuenta dice cuales de las `7`
quedan pendientes con ella.

## TAREA 5: **EL CIERRE**

- **El censo antes y despues**: nodos, veredictos, pares mutuos, bandeja de Grove e insertados. **Si entran las `20`**, el grafo
  queda en `410`, la bandeja de Grove en `27` y `_insertados` en `65`; y la bitacora gana las `118` lineas de veredicto mas una por
  cada arista por lectura, como en la `67` (`90` mas `7`) y la `68` (`9` mas `2`).
- **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo, de lo que ENTRO**: `cap_05` y `cap_06`, contados desde
  `.v68ext/contar_fidelidad.txt`, que la `ACTA 67` `67.4.a` firmo en `0` de `84` y `0` de `62`, no a ojo.
- **`D.61`**: cada discutible ejecutado o cerrado. Ninguno abierto.
- **`R5`** en cada bloque `$` de tu tramo, medido con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la
  cabecera cambiada a la `70`, y pegado.
- `python forja.py gate`, `python forja.py guiones`, `python tests/test_aceptacion.py` y `python scripts/cerrar_reporte.py`,
  **pegados**. **El cierre estricto tiene que salir en verde: cualquier rojo es tuyo.**
- Commitea `docs/loop/`, `dataset/`, `bitacora/`, `censos/`, los movidos a `_insertados` y tu carpeta `.v70ext/`. **Si nada te
  obliga a parar, no escribas `PARA_ALEXIS.md`.**

---

## LO QUE NO HACES

- **NO LANZAS NADA EN SEGUNDO PLANO QUE TOQUE EL DATASET**, y **NO TERMINAS TU TURNO CON NADA VIVO**, ni un `insertar` ni un
  barrido.
- **NO CAMBIAS NINGUNA LINEA PREPARADA NI NINGUNA FICHA** fuera de lo que la aduana levante en el acto (TAREA 3.3). Su fidelidad
  y sus clases estan firmadas.
- **NO TOCAS `cuarentena/gerber_emyth/` NI `cuarentena/marquet_turn_the_ship/`**: van despues de Grove, en ese orden.
- **NO TOCAS `src/`, `scripts/`, el banco, el arnes ni los protocolos** (`7.F`, `D.55`), **ni `APERTURA_CIEGA.md`**.
- **NO REORDENAS LA COLA A MANO.**
- **NO ABRES NINGUN LIBRO.** El mundo `11` cierra con siete.

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No
adivines.**
