# ENCARGO DE LA VUELTA 72: **LAS `20` FILAS DE `.v71ext/orden.txt` DENTRO, UNA POR VEZ, CON LAS `50` LINEAS Y LAS `6` ARISTAS QUE LAS DOS LECTURAS YA COMPARTEN. CON ELLAS, `cap_07`, `cap_10`, `cap_11`, `cap_12`, `cap_13` Y `cap_14` QUEDAN ENTEROS EN EL GRAFO**

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 70`, que audito la vuelta `71`.
`AUDITOR_FORJA.md` seccion `1.4`. **Toda cifra de medida de esta pagina lleva su bloque `$` o la seccion del acta donde esta
pegada** (`R8`, `ACTA 70` `70.12`).*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: INSERCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **LA REGLA DEL TURNO, Y EL METODO QUE YA FUNCIONO TRES VECES**

> **UN `insertar` POR VEZ, Y NINGUNO EN VUELO CUANDO TU TURNO TERMINE.** Cada candidato entra entero o no entra.
> **Al volver cada `insertar`: su fila en el reporte, commit y push.**

**El metodo de la `67`, la `68` y la `70` vale**: cada `insertar` lanzado como un proceso por una copia de `.v68ext/insertar.py`, y tu
bloqueado en primer plano con una copia de `.v68ext/esperar.py` hasta su `.fin`, **sin lanzar el siguiente ni tocar el dataset ni
la bandeja en medio**. **NO LANZAS NADA EN SEGUNDO PLANO QUE SIGA VIVO AL CERRAR TU TURNO.** Si algo no te cabe, no lo lances: lo
dices en el reporte con las filas que faltan, y entran en la `73`. El `23` sep tres asientos cerraron diciendo que esperaban un
trabajo de fondo, y ninguno volvio.

**EL RELOJ, MEDIDO, Y NO SON TECHOS: SON LO QUE COSTO.** Los `20` `insertar` de la `70`, con la aduana de antes del reparto del
fundador:

    $ tail -1 .v70ext/relojes_resumen.txt
    insertar: 20 | minimo 747.0 s | mediana 2493.4 s | maximo 4236.0 s | suma 45201.6 s (12.56 h)

y el barrido de la `71`, ya con la senial `1` repartida (`68d6946`), cinco fichas a la vez, por ficha y ordenado por valor:

    $ grep "rc=" .v71ext/barrido.log | sed 's/.*segundos=//' | sort -n | sed -n '1p;$p'
    578
    1640

## LA CLASE Y EL LIBRO, DICHOS POR EL INSTRUMENTO

    $ python scripts/deuda.py --clase 72
    LIBRE
      van 3 de 5 desde la ultima de saneamiento (la 69), con 56 deuda(s) esperando

    $ python forja.py tablero --puedo grove_high_output
    LINEA 'serial', LIBRO 'grove_high_output': SI
      'grove_high_output' esta COSECHADO y sin dueño: su trabajo ya llego a esta rama, asi que se continua desde el capitulo siguiente al ultimo minado (cap_18), citando su frontera. D.50.

**El orden de la campania es Grove, Gerber, Marquet** (`PARALELO.md` `8` punto `4`). **La frase de *continuar desde `cap_18`* es de
extraccion y no aplica: Grove esta minado entero**, y lo que se hace es insertar su bandeja por capitulo (`d028`).

---

## TAREA 1: **REGISTROS DE LA `ACTA 70`**

En una tabla corta y sin reabrir el argumento (`D.47`):

| que | donde |
|---|---|
| **Tus `13` discutibles se sostienen**; en `D71.12` cae la lectura ciega del auditor en `2` pares y **tus `50` lineas quedan como estan** | `ACTA 70` `70.5` |
| **Tu barrido es el del auditor fila a fila, `50` de `50` con sus seniales**, y tus instrumentos se reproducen identicos; tus `4` PUENTE y sus correcciones se sostienen, y las `6` dudas del auditor caen a tu `T` | `70.1`, `70.4` |
| **Tus `4` aristas por lectura son las del auditor** y tu orden cumple sus `12` restricciones | `70.3` |
| **Una cifra tuya falsa en prosa**: *`13` de las `20` levantan vecinos*, donde son `15`. Registrada, no acumula | `70.2` |
| **Una cifra falsa del auditor en el encargo de la `71`** (*fichas de `2400` a `4200` s* en la `68`, que son `865` a `4566`): su racha `AUDITOR` en `1 de 3`, y su remedio `R8` | `70.10`, `70.12` |

## TAREA 2: **LO QUE ENTRA ES LO QUE SE LEYO**

Antes del primer `insertar`, con una copia de `.v71ext/pasos_y_huellas.py` con el commit de comparacion cambiado a `682a39c` (el
cierre del reintento de la `71`; ninguna ficha cambio despues de `3e90afc`, `ACTA 70` `70.1`): **las `20` fichas de la bandeja
iguales a su blob en `682a39c`**, y sus `20` huellas iguales a las de `.v71ext/pasos_y_huellas.txt`. Si una sale distinta, no entra,
se relee entera contra su capitulo y se dice.

## TAREA 3: **LAS `20` FILAS DE `.v71ext/orden.txt`, UNA POR VEZ**

**En su orden, filas `1` a `20`**: las `9` de `cap_07`, `1` de `cap_10`, `2` de `cap_11`, `3` de `cap_12`, `2` de `cap_13` y `3` de
`cap_14` (`APERTURA_CIEGA.md` `2`, y la `ACTA 70` `70.6`).

1. **Las lineas `--veredicto` son las del bloque de cada candidato en `.v71ext/veredictos_listos.txt`, tal cual, sin las `#`.** Las
   `CONTINUA` con `madre=` cablean su arista en el acto: `definir_entorno_grupo_clientes_proveedores_competidores` a
   `examinar_entorno_expectativas_tecnologia_proveedores_grupos` en la fila `5`, y a
   `examinar_demanda_entorno_dos_marcos_temporales` en la fila `6`.
2. **Las cuatro aristas por lectura, con `python forja.py arista` en el acto de insertar el hijo**, como en la `67`, la `68` y la
   `70`, con su cita y su `--paso` el de la madre que su fila `SOSTENGO` de `.v71ext/aristas_lectura.txt` cita:
   `planificar_tres_pasos_demanda_estado_brecha` a `examinar_demanda_entorno_dos_marcos_temporales` (fila `6`), a
   `determinar_estado_presente_capacidades_proyectos_merma` (fila `7`) y a `cerrar_brecha_dos_preguntas_estrategia` (fila `8`),
   las tres por `D.37`; y `elegir_modo_control_motivacion_factor_cua` a `escalonar_complejidad_puesto_empleado_nuevo` (fila `12`),
   por `D.29`. **Ninguna de las partes entre si** (`ACTA 70` `70.5`, `D71.12`).
3. **`d170`, EN LA FILA `16`**: `elegir_estilo_direccion_madurez_relevante_tarea` entra **sin linea ni arista** con
   `fijar_frecuencia_reunion_individual_madurez_tarea`, como decidio la conjunta de la `69` (`D69.3`, `ACTA 68` `68.5`). **Si la
   aduana de hoy levanta el par**, su linea es `SANO` con esa cita, y lo dices. Pagala con `python scripts/deuda.py --pagar d170
   --vuelta 72 --como "..."` al volver ese `insertar`.
4. **La puerta es la aduana de `insertar`, no la lista** (`d031`). Si levanta un vecino sin linea, lo lees con los pasos de los dos
   delante, escribes su veredicto por la vara `6.1` y solo esa, **y lo marcas en el reporte como lectura tuya de esta vuelta**,
   discutible si dudas. Si levanta `CAERIA` o un error, no fuerces: no entra, y se declara.
5. **Al volver cada `insertar`, su fila en el reporte** como las de la `70`: la aduana de hoy con sus vecinos, las lineas que
   pasaste, las aristas que cableaste y su commit. Cada insertado a `cuarentena/_insertados/grove_high_output/` (`D.31`).

## TAREA 4: **LAS ARISTAS DE LA TANDA, POR INSTRUMENTO**

Al terminar la ultima fila que entre: **cuantas se esperaban (`6`, la ultima linea de `.v71ext/orden.txt`), cuantas viven en el
grafo, y ninguna sin adjudicar**; y que ningun nodo viejo cambio fuera del `nodos_siguientes` de sus madres. Si alguna fila no
entro, la cuenta dice cuales de las `6` quedan pendientes con ella.

## TAREA 5: **EL CIERRE**

- **El censo antes y despues**: nodos, veredictos, pares mutuos, bandeja de Grove e insertados. Al abrir son `410`, `1027`, `1`, `27`
  y `65` (`ACTA 70` `70.1`). **Si entran las `20`**, el grafo gana `20`, la bandeja de Grove pierde `20` y `_insertados` los gana; y
  la bitacora gana las `50` lineas de veredicto (`70.3`) mas una por cada arista por lectura, como en la `70` (`118` mas `5`).
- **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo, de lo que ENTRO**: los seis, contados desde `.v71ext/fidelidad.tsv` con
  los `4` PUENTE ya corregidos en la bandeja, que la `ACTA 70` `70.6` firmo en `0` que entran. No a ojo.
- **`D.61`**: cada discutible ejecutado o cerrado. Ninguno abierto.
- **`R5`** en cada bloque `$` de tu tramo, medido con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera
  cambiada a la `72`, y pegado.
- `python forja.py gate`, `python forja.py guiones`, `python tests/test_aceptacion.py` y `python scripts/cerrar_reporte.py`,
  **pegados**. **El cierre estricto tiene que salir en verde: cualquier rojo es tuyo.**
- Commitea `docs/loop/`, `dataset/`, `bitacora/`, `censos/`, los movidos a `_insertados` y tu carpeta `.v72ext/`. **Si nada te obliga
  a parar, no escribas `PARA_ALEXIS.md`.**

---

## LO QUE NO HACES

- **NO LANZAS NADA EN SEGUNDO PLANO QUE TOQUE EL DATASET**, y **NO TERMINAS TU TURNO CON NADA VIVO**, ni un `insertar` ni un
  barrido.
- **NO CAMBIAS NINGUNA LINEA PREPARADA NI NINGUNA FICHA** fuera de lo que la aduana levante en el acto (TAREA 3.4). Su fidelidad y
  sus clases estan firmadas.
- **NO TOCAS LAS `7` FICHAS DE `cap_15`, `cap_16` Y `cap_17`**: se preparan en la vuelta siguiente.
- **NO TOCAS `cuarentena/gerber_emyth/` NI `cuarentena/marquet_turn_the_ship/`**: van despues de Grove, en ese orden.
- **NO TOCAS `src/`, `scripts/`, el banco, el arnes ni los protocolos** (`7.F`, `D.55`), **ni `APERTURA_CIEGA.md`**. Los procesos
  del fundador que veas vivos en otra copia no son tuyos: ni los tocas ni los esperas.
- **NO REORDENAS LA COLA A MANO.**
- **NO ABRES NINGUN LIBRO.** El mundo `11` cierra con siete.

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No
adivines.**
