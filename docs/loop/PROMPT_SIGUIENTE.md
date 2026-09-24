# ENCARGO DE LA VUELTA 68: **LAS FILAS `21` Y `22` DE `cap_04` DENTRO, UNA POR VEZ, Y `cap_05` Y `cap_06` ENTEROS DEJADOS LISTOS PARA INSERTAR: SU FIDELIDAD LEIDA ENTERA, SUS VECINOS BARRIDOS, SUS VEREDICTOS ESCRITOS Y SU ORDEN COMPROBADO**

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 66`, que audito la vuelta `67`.
`AUDITOR_FORJA.md` seccion `1.4`.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: INSERCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **LA REGLA DEL TURNO, Y EL METODO QUE LA `ACTA 66` TE SOSTUVO**

> **UN `insertar` POR VEZ, Y NINGUNO EN VUELO CUANDO TU TURNO TERMINE.** Cada candidato entra entero o no entra.
> **Al volver cada `insertar`: su fila en el reporte, commit y push.**

**El metodo de la `65`, la `66` y la `67` vale** (`ACTA 66` `66.3`: `20` `.fin` en `0`, `0` solapes): cada `insertar` lanzado
como un proceso por una copia de `.v67ext/insertar.py`, y tu bloqueado en primer plano con una copia de `.v67ext/esperar.py`
hasta su `.fin`, **sin lanzar el siguiente ni tocar el dataset ni la bandeja en medio**.

**Y LO MISMO PARA LO QUE CORRA EN PARALELO** (TAREA 3): puedes lanzar barridos de fondo, **cinco a la vez como mucho y
nunca mientras vuele un `insertar`**, pero **ninguno vivo al cerrar tu turno**: los recoges todos dentro, vigilandolos si
tardan. **Si no te caben, no los lances: lo dices en el reporte con los que faltan.** El `23` sep tres asientos cerraron
diciendo que esperaban un trabajo de fondo, y ninguno volvio.

**EL RELOJ, MEDIDO:** los `20` `insertar` de la `67` tardaron de `985,8` a `3988,1` s, mediana `1487,6`, contra poblacion `479`
(`.v67ext/relojes.txt`); el barrido de `22` fichas de la `66`, cinco a la vez, `2` h `7` min (`ACTA 65` `65.1`). **No son
techos: son lo que costo.**

## LA CLASE Y EL LIBRO, DICHOS POR EL INSTRUMENTO

    $ python scripts/deuda.py --clase 68
    LIBRE
      van 4 de 5 desde la ultima de saneamiento (la 64), con 57 deuda(s) esperando

    $ python forja.py tablero --puedo grove_high_output
    LINEA 'serial', LIBRO 'grove_high_output': SI
      'grove_high_output' esta COSECHADO y sin dueño: su trabajo ya llego a esta rama, asi que se continua desde el capitulo siguiente al ultimo minado (cap_18), citando su frontera. D.50.

**El orden de la campania es Grove, Gerber, Marquet** (`PARALELO.md` `8` punto `4`). **La frase de *continuar desde `cap_18`*
es de extraccion y no aplica: Grove esta minado entero**, y lo que se hace es insertar su bandeja por capitulo (`d028`).

---

## TAREA 1: **REGISTROS DE LA `ACTA 66`**

En una tabla corta y sin reabrir el argumento (`D.47`):

| que | donde |
|---|---|
| **Tus cinco discutibles se sostienen, `D67.1` a `D67.5`**, y **la relectura conjunta se cierra sin discrepancia**: `C1` y `C2` `CONTINUA`, `C3` sin arista (esta la gana tu razon, no la del auditor) | `ACTA 66` `66.4.a` |
| **Cero caidas que acumulen**: `90` lineas de veredicto iguales letra a letra a las preparadas, `11` aristas iguales par a par a la lista ciega del auditor, la muestra de los SANO `17` de `17`, y `d072` pagada | `66.3`, `66.4.b` |
| **Una caida de `REPORTE` que no acumula**: en `67.5.c` los `13` pasos que faltan son `5` de `agrupar_interrupciones` y `8` de `canalizar`, no `7` y `6` | `66.2` |
| **`R5` cumplido**, **`cap_04` entra en `0` de `143`**, y las cinco rachas de la serial en cero | `66.0`, `66.5`, `66.7` |

## TAREA 2: **LAS FILAS `21` Y `22` DE `cap_04`, UNA POR VEZ, ANTES DE TOCAR `cap_05`**

Las dos que la `67` dejo fuera por el tope, **en su orden de `.v67ext/orden.txt`**:

| fila | candidato | lineas listas | arista por lectura, con la madre ya en el grafo |
|---|---|---|---|
| `21` | `agrupar_interrupciones_subordinados_reuniones_regulares` | las `8` de su bloque en `.v66ext/veredictos_listos.txt` | `agrupar_tareas_semejantes_aprovechar_preparacion` a ella |
| `22` | `canalizar_interrupciones_cartel_hora_oficina` | la `1` de su bloque | `buscar_regularidad_bloques_iguales_trabajo_mando` a ella |

1. **Antes del primer `insertar`, lo que entra es lo que se leyo:** una copia de `.v67ext/pasos_y_huellas.py` con la lista
   cambiada a esas dos y el commit en `d8f4e2a`. **Las dos tienen que salir iguales.** Si una sale distinta, no entra, se
   relee entera contra `cap_04` y se dice.
2. **Las lineas `--veredicto` son las vivas de su bloque, tal cual**, sin las `#` (`D67.5`).
3. **La arista por lectura de cada una, con `python forja.py arista` en el acto de insertar el hijo**, `--veredicto CONTINUA`,
   su cita y su `--paso` el de la madre que su fila de `.v66ext/aristas_lectura.txt` cita, como en la `67`.
4. **La puerta es la aduana de `insertar`, no la lista** (`d031`). Si levanta un vecino sin linea, lo lees con los pasos de
   los dos delante, escribes su veredicto por la vara `6.1` y solo esa, **y lo marcas en el reporte como lectura tuya de esta
   vuelta**, discutible si dudas. Si levanta `CAERIA` o un error, no fuerces: no entra, y se declara.
5. **Al volver cada `insertar`, su fila en el reporte** como las de la `67`, y cada insertado a
   `cuarentena/_insertados/grove_high_output/` (`D.31`). **Con las dos dentro, `cap_04` queda entero en el grafo.**

## TAREA 3: **`cap_05` Y `cap_06` ENTEROS, DEJADOS LISTOS PARA SU INSERCION. AQUI NO SE INSERTA NINGUNO**

Son `20` candidatos, el tope de una tanda de insercion: `cap_05` `12` (`84` pasos, de `P6` a `P20`) y `cap_06` `8` (`62`
pasos, de `P7` a `P31`), las filas `25` a `44` de `.v65aud/normal/cola_grove.txt`, leidas de la `UNIDAD DE ORIGEN` de cada
`resumen_teorico`. **Es el camino de la `66`, que llevo a la `67` a entrar sin una sorpresa.** **Y SE INSERTAN EN LA `70`, NO EN
LA `69`**: el instrumento ya dice que la `69` es de saneamiento (`python scripts/deuda.py --clase 69`: `SANEAMIENTO`, han pasado
`5` desde la `64`), asi que lo que dejes listo tiene que aguantar una vuelta quieto, y por eso la TAREA 4 lo sella con su huella.
Todo en tu carpeta `.v68ext/`, **con copias de instrumentos que ya existen y la ruta cambiada**, no con instrumentos nuevos (`7.F`):

1. **La fidelidad ENTERA** (`D.30`, `D.58`): **cada paso de los `20` contra `fuentes/grove_high_output/cap_05.md` y
   `cap_06.md` leidos enteros**, marcado `T` o `P` con su linea, en un fichero con una fila por paso como
   `.v66ext/fidelidad.tsv` (la clausula reescrita CUENTA como `P`, `ACTA 62` `62.5`). **Todo PUENTE se corrige en la ficha de
   la bandeja por correccion declarada, con el texto viejo dentro, ANTES del barrido**: una ficha que cambia despues de su
   barrido tiene un barrido que ya no es suyo (`d031`). Publica `PASOS INVENTADOS` **una fila por capitulo**, por
   instrumento, y marca discutible todo paso en que dudes.
2. **El barrido de los `20`, sobre las fichas ya corregidas y con las filas `21` y `22` ya dentro**, contra **GRAFO MAS
   BANDEJAS** (`D.38.4`), con copias de `.v66ext/barrido_uno.py` y `.v66ext/barrer.sh` con la lista de `cap_05` y `cap_06`:
   **cinco a la vez como mucho, un log con su `INICIO` y su `TODOS TERMINADOS`, y los `20` recogidos dentro de tu turno.**
3. **Los veredictos listos, uno por vecino**, en el formato de `--veredicto` y con un bloque por candidato como
   `.v66ext/veredictos_listos.txt`: **leidos con los pasos de los dos delante** (`python .v64aud/pasos.py <a> <b>`) y por la
   vara `6.1`, y solo esa. **Y comprobado por instrumento que cada vecino del barrido tiene su linea y cada linea su
   vecino**, con una copia de `.v67ext/comprobar_veredictos.py`.
4. **Las aristas por lectura** (`D.29`, `D.53`), en un fichero como `.v66ext/aristas_lectura.txt`, con su tramo de madre y de
   hijo y su linea del libro, **mirando tambien madres que ya viven en el grafo** (la `67` cableo cuatro asi). **`D.37`**: los
   titulos que dicen cuantas partes tienen (*tres clases*, *seis preguntas*) se miran como en la `66`: si alguna parte es
   nodo, la arista cabeza a parte se declara.
5. **El orden de insercion de los `20`**, con una copia de `.v67ext/orden.py`: **madre antes que hijo, `D.36`, y las tres
   comprobaciones en cero.**

**Si la TAREA 3 no te cabe entera, parte por capitulo y por donde se pueda auditar**: `cap_05` entero antes que `cap_06`, y
dentro de cada uno la fidelidad antes que el barrido y el barrido antes que los veredictos. **Lo que no hagas lo dices con su
fila vacia**, y la siguiente vuelta de insercion empieza por ahi.

## TAREA 4: **EL CIERRE**

- **El censo antes y despues**: nodos, veredictos, pares mutuos, bandeja de Grove e insertados. Si entran las dos, el grafo
  queda en `390`, la bandeja en `47` y `_insertados` en `45`.
- **Las aristas de la tanda, contadas por instrumento**: las dos por lectura, vivas en el grafo.
- **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo**: la de lo que ENTRO (`cap_04`, las dos filas, contadas desde
  `.v66ext/fidelidad.tsv`, que la `ACTA 65` firmo) **y aparte las de `cap_05` y `cap_06`**, que son preparacion y no entrada.
- **`D.61`**: cada discutible ejecutado o cerrado. Ninguno abierto.
- **`R5`** en cada bloque `$` de tu tramo, **medido con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la
  cabecera cambiada a la `68`**, y pegado.
- `python forja.py gate`, `python forja.py guiones`, `python tests/test_aceptacion.py` y `python scripts/cerrar_reporte.py`,
  **pegados**. **El cierre estricto tiene que salir en verde: cualquier rojo es tuyo.**
- Commitea `docs/loop/`, `dataset/`, `bitacora/`, `censos/`, los movidos a `_insertados`, las fichas corregidas de la bandeja
  y tu carpeta `.v68ext/`. **Si nada te obliga a parar, no escribas `PARA_ALEXIS.md`.**
- **La huella de las `20` fichas preparadas**, con una copia de `.v67ext/pasos_y_huellas.py` con la lista de `cap_05` y
  `cap_06`, corrida despues del ultimo cambio de ficha y pegada: es contra lo que la `70` comprobara que entra lo que se leyo.

---

## LO QUE NO HACES

- **NO LANZAS NADA EN SEGUNDO PLANO QUE TOQUE EL DATASET**, y **NO TERMINAS TU TURNO CON NADA VIVO**, ni un `insertar` ni un
  barrido.
- **NO INSERTAS NINGUNO DE `cap_05` NI DE `cap_06`.** Su insercion es de la `70`, despues de que la `ACTA 67` adjudique su
  fidelidad y sus veredictos y de que pase la saneamiento de la `69`.
- **NO TOCAS `cuarentena/gerber_emyth/` NI `cuarentena/marquet_turn_the_ship/`**: van despues de Grove, en ese orden.
- **NO TOCAS `src/`, `scripts/`, el banco, el arnes ni los protocolos** (`7.F`, `D.55`), **ni `APERTURA_CIEGA.md`**.
- **NO REORDENAS LA COLA A MANO.**
- **NO ABRES NINGUN LIBRO.** El mundo `11` cierra con siete.

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No
adivines.**
