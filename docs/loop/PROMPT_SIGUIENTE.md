# ENCARGO DE LA VUELTA 66: **LAS FILAS `21` Y `22` DE GROVE DENTRO, UNA POR VEZ, Y `cap_04` ENTERO DEJADO LISTO PARA INSERTAR: SU FIDELIDAD LEIDA ENTERA, SUS VECINOS BARRIDOS, SUS VEREDICTOS ESCRITOS Y SU ORDEN COMPROBADO**

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 64`, que audito
la vuelta `65`. `AUDITOR_FORJA.md` seccion `1.4`.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: INSERCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **LA REGLA DEL TURNO, Y EL METODO QUE LA `ACTA 64` TE SOSTUVO**

> **UN `insertar` POR VEZ, Y NINGUNO EN VUELO CUANDO TU TURNO TERMINE.** Cada candidato entra entero o no
> entra. **Al volver cada `insertar`: su fila en el reporte, commit y push.**

**El metodo de la `65` vale** (`ACTA 64` `64.4.a`, `D65.1` sostenido): cada `insertar` lanzado como un proceso
por una copia de `.v65ext/insertar.py`, y tu bloqueado en primer plano con una copia de `.v65ext/esperar.py`
hasta su `.fin`, **sin lanzar el siguiente ni tocar el dataset en medio**. Lo que lo sostuvo fue medido: cero
solapes, `20` `.fin` en `0`, el cerrojo suelto al cerrar. **Eso es lo que tu reporte tiene que poder
enseniar otra vez.**

**Y LO MISMO PARA LO QUE CORRA EN PARALELO** (TAREA 3): puedes lanzar barridos de fondo, **cinco a la vez como
mucho**, pero **ninguno vivo al cerrar tu turno**: los recoges todos dentro, vigilandolos si tardan. **Si no te
caben, no los lances: lo dices en el reporte con los que faltan.** El `23` sep tres asientos cerraron diciendo
que esperaban un trabajo de fondo, y ninguno volvio.

**EL RELOJ, MEDIDO:** una aduana de ficha contra poblacion `479` tardo de `816` a `2379` s en la `65`
(`.v65ext/relojes.txt`), y el barrido de `20` fichas cinco a la vez tardo `1` h `54` min en la fase ciega
(`.v65aud/barrido.log`). **No son techos: son lo que costo.**

## LA CLASE Y EL LIBRO, DICHOS POR EL INSTRUMENTO

    $ python scripts/deuda.py --clase 66
    LIBRE
      van 2 de 5 desde la ultima de saneamiento (la 64), con 57 deuda(s) esperando

    $ python forja.py tablero --puedo grove_high_output
    LINEA 'serial', LIBRO 'grove_high_output': SI
      'grove_high_output' esta COSECHADO y sin dueño: su trabajo ya llego a esta rama, asi que se continua desde el capitulo siguiente al ultimo minado (cap_18), citando su frontera. D.50.

**El orden de la campania es Grove, Gerber, Marquet** (`PARALELO.md` `8` punto `4`). **La frase de *continuar
desde `cap_18`* es de extraccion y no aplica: Grove esta minado entero**, y lo que se hace es insertar su
bandeja por capitulo (`d028`).

---

## TAREA 1: **REGISTROS DE LA `ACTA 64`**

En una tabla corta y sin reabrir el argumento (`D.47`):

| que | donde |
|---|---|
| **Tus cuatro discutibles se sostienen, `D65.1` a `D65.4`**, y **cero caidas tuyas**: los `48` veredictos de la bitacora son los adjudicados letra a letra, las siete aristas llevan la razon de su fila, y la muestra pineada de los SANO se sostiene `8` de `8` | `ACTA 64` `64.3` y `64.4` |
| **`R5` cumplido y `REPORTE` baja de `1 de 3` a `0 de 3`**: el bloque que `pegado65` marca es tu apertura, reproducida contra `90028c0`, y lo declaraste | `64.2` |
| **`PASOS INVENTADOS`: `cap_02` `4` de `50`, `8,00`; `cap_03` `2` de `108`, `1,85`**. Los dos bajo el `10` | `64.5` |
| **Las cinco rachas de la serial en cero** | `64.7` |
| **`d167`**: tu cierre estricto va a salir en ROJO por una tabla de la apertura del auditor, y solo por ella. Lee la TAREA 4 | `64.9` |

## TAREA 2: **LAS FILAS `21` Y `22`, UNA POR VEZ**

Las dos que la `65` dejo fuera por el tope, **en su orden de `.v65ext/orden.txt`**:

| fila | candidato | lineas listas |
|---|---|---|
| `21` | `variar_frecuencia_inspeccion_nivel_calidad` | ninguna: entraba sin vecinos contra `462` |
| `22` | `simplificar_trabajo_reducir_numero_pasos` | la de su bloque en `.v64ext/veredictos_listos.txt`, tal cual |

1. **Antes del primer `insertar`, lo que entra es lo que se leyo:** `python .v64aud/normal/pasos_y_huellas.py`,
   y las dos tienen que salir iguales al commit de su lectura entera (`b63405c`). Si una sale distinta, se
   relee entera contra `cap_03` antes de insertarla, y se dice.
2. **La puerta es la aduana de `insertar`, no la lista** (`d031`). Desde que la `64` midio, **la cosecha de
   Marquet trajo `17` candidatos nuevos a la bandeja** (`APERTURA_CIEGA.md` de la `65`, seccion `2`), y contra
   los `20` de la `65` no levanto ninguno; **contra estas dos no lo ha medido nadie**. Si la aduana levanta un
   vecino sin linea, lo lees con los pasos de los dos delante, escribes su veredicto por la vara `6.1` de
   `AUDITOR_FORJA.md` y solo esa, **y lo marcas en el reporte como lectura tuya de esta vuelta**, discutible si
   dudas. Si levanta `CAERIA` o un error, no fuerces: no entra, y se declara.
3. **Al volver cada `insertar`, su fila en el reporte** como las de la `65`: la aduana de hoy con sus vecinos,
   las lineas que pasaste, las aristas y su commit. Cada insertado a `cuarentena/_insertados/grove_high_output/`
   (`D.31`).

## TAREA 3: **`cap_04` ENTERO, DEJADO LISTO PARA LA INSERCION DE LA `67`. AQUI NO SE INSERTA NINGUNO**

Son `22` candidatos, de `P7` a `P44` (`.v65aud/normal/cola_grove.txt`, filas `3` a `24`, leidas de la
`UNIDAD DE ORIGEN` de cada `resumen_teorico`). **Por que preparar y no insertar:** es el camino que llevo a la
`65` a entrar sin una sorpresa, y **una fidelidad que se adjudica despues de insertar deja un PUENTE en el
grafo si cae** (`ACTA 64` `64.10`). Todo en tu carpeta `.v66ext/`, **con copias de instrumentos que ya
existen y la ruta cambiada**, no con instrumentos nuevos (`7.F`):

1. **La fidelidad ENTERA** (`D.30`, `D.58`): **cada paso de los `22` contra `fuentes/grove_high_output/cap_04.md`
   leido entero**, marcado `T` o `P` con su linea, **en un fichero con una fila por paso** como
   `.v64ext/fidelidad.tsv` (la clausula reescrita CUENTA como `P`, `ACTA 62` `62.5`). **Todo PUENTE se corrige
   en la ficha de la bandeja por correccion declarada, con el texto viejo dentro, ANTES del barrido**: una
   ficha que cambia despues de su barrido tiene un barrido que ya no es suyo (`d031`). Publica `PASOS
   INVENTADOS` de `cap_04` por instrumento, y marca discutible todo paso en que dudes.
2. **El barrido de los `22`, sobre las fichas ya corregidas**, contra **GRAFO MAS BANDEJAS** (`D.38.4`), con una
   copia de `.v65aud/barrido_uno.py` que lea la ficha de `cuarentena/grove_high_output/` en vez de
   `_insertados`, y una copia de `.v65aud/barrer.sh` con la lista de `cap_04`: **cinco a la vez como mucho, un
   log con su `INICIO` y su `TODOS TERMINADOS`, y los `22` recogidos dentro de tu turno.**
3. **Los veredictos listos, uno por vecino**, en el formato de `--veredicto` y con un bloque por candidato
   como `.v64ext/veredictos_listos.txt`: **leidos con los pasos de los dos delante** (`python .v64aud/pasos.py
   <a> <b>`) y por la vara `6.1`, y solo esa. **Y comprobado por instrumento que cada vecino del barrido
   tiene su linea y cada linea su vecino**, como `.v64ext/comprobar_veredictos.py`.
4. **Las aristas por lectura** (`D.29`, `D.53`), en un fichero como `.v64ext/aristas_lectura.txt`, con su
   tramo de madre y de hijo y su linea del libro. **Dos estan escritas desde hace vueltas y se cobran aqui:**
   - **`d072`**: `construir_flujo_produccion_paso_limitante` (ya en el grafo) es madre de
     `identificar_paso_limitante_jornada_desfases` por lectura, y **ninguna senial lo levanta por ninguno de
     sus dos lados**. Leela y sostenla o no con su razon.
   - **la arista EN COLA** de la `65`: `detectar_arreglar_fallo_etapa_menor_valor` a
     `supervisar_tarea_delegada_etapa_menor_valor` (`65.4.b`, `CONTINUA` desde el lado de la madre). **Si el
     barrido de `supervisar` levanta a `detectar`, su linea `CONTINUA` con `madre=` va en sus veredictos; si no
     lo levanta, va en las aristas por lectura.** Dilo con la salida del barrido delante.
   - **`D.37`**: los titulos de `cap_04` que dicen cuantas partes tienen (*tres vias*) se miran como en la
     `65`: si alguna parte es nodo, la arista cabeza a parte se declara.
5. **El orden de insercion de los `22`**, con una copia de `.v64ext/orden.py`: **madre antes que hijo, `D.36`,
   y las tres comprobaciones en cero**; con el tope en `20`, **las dos ultimas del orden pasan a la `68`**, y
   ningun hijo dentro del tope con su madre fuera.

**Si la TAREA 3 no te cabe entera, parte por donde se pueda auditar**: la fidelidad entera antes que nada,
luego el barrido, luego los veredictos. **Lo que no hagas lo dices con su fila vacia**, y la `67` empieza por
ahi.

## TAREA 4: **EL CIERRE**

- **El censo antes y despues**: nodos, veredictos, pares mutuos, bandeja de Grove e insertados. Si entran las
  dos, el grafo queda en `368` y la bandeja en `69`.
- **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo**: la de lo que ENTRO (`cap_03`, las dos filas,
  contadas desde su lectura entera adjudicada en la `ACTA 62` `62.6`, no a ojo) **y aparte la de `cap_04`**, que
  es preparacion y no entrada.
- **`D.61`**: cada discutible ejecutado o cerrado. Ninguno abierto.
- **`R5`** en cada bloque `$` de tu tramo, **medido con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py`
  con la cabecera cambiada a la `66`**, y pegado.
- `python forja.py gate`, `python forja.py guiones`, `python tests/test_aceptacion.py` y
  `python scripts/cerrar_reporte.py`, **pegados**. **EL CIERRE ESTRICTO VA A SALIR EN ROJO POR UNA SOLA LINEA
  QUE NO ES TUYA:** `SIN COMPROBAR  docs/loop/APERTURA_CIEGA.md linea 270`, una tabla de la apertura sellada
  del auditor de la `65` que el tallador no puede comprobar (`d167`). **Pegala, declarala, y NO TOQUES
  `APERTURA_CIEGA.md`**: su sello no es tuyo, y el auditor escribe la suya encima despues de tu turno.
  **Cualquier otro rojo si es tuyo.**
- Commitea `docs/loop/`, `dataset/`, `bitacora/`, `censos/`, los movidos a `_insertados`, las fichas corregidas
  de la bandeja y tu carpeta `.v66ext/`. **Si nada te obliga a parar, no escribas `PARA_ALEXIS.md`.**

---

## LO QUE NO HACES

- **NO LANZAS NADA EN SEGUNDO PLANO QUE TOQUE EL DATASET**, y **NO TERMINAS TU TURNO CON NADA VIVO**, ni un
  `insertar` ni un barrido.
- **NO INSERTAS NINGUNO DE `cap_04`.** Su insercion es de la `67`, despues de que la `ACTA 65` adjudique su
  fidelidad y sus veredictos.
- **NO TOCAS `cuarentena/gerber_emyth/` NI `cuarentena/marquet_turn_the_ship/`**: van despues de Grove, en ese
  orden.
- **NO TOCAS `src/`, `scripts/`, el banco, el arnes ni los protocolos** (`7.F`, `D.55`), **ni
  `APERTURA_CIEGA.md`**.
- **NO REORDENAS LA COLA A MANO.**
- **NO ABRES NINGUN LIBRO.** El mundo `11` cierra con siete.

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente,
paras y lo traes. No adivines.**
