# ENCARGO DE LA VUELTA 76: **LAS FICHAS DE GERBER DEJADAS LISTAS PARA INSERTAR: SU FIDELIDAD LEIDA ENTERA, SUS VECINOS BARRIDOS, SUS VEREDICTOS ESCRITOS, SUS ARISTAS LEIDAS (CON `d111`, `d108` Y `d098` DELANTE) Y SU ORDEN COMPROBADO. AQUI NO SE INSERTA NINGUNA** (`ACTA 74` `74.10`)

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 74`, que audito la vuelta `75`.
`AUDITOR_FORJA.md` seccion `1.4`. **Toda cifra de medida de esta pagina va dentro de un bloque `$` con su salida, o lleva en
su misma linea la seccion de la `ACTA 74` donde esta pegada** (`R8`, `ACTA 74` `74.11`).*

> # **LIBRO DE ESTA VUELTA: `gerber_emyth`**
> # **CLASE DE ESTA VUELTA: INSERCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **LA REGLA DEL TURNO, Y POR QUE ESTA VUELTA NO INSERTA**

**Grove entro entero en la `75`**: su bandeja esta vacia y el libro vive en el grafo y en `_insertados` (`ACTA 74` `74.1`). **El
orden de la campania es Grove, Gerber, Marquet** (`PARALELO.md` seccion `8` punto `4`), asi que toca Gerber. Esta vuelta hace para
la bandeja de Gerber lo que la `71` y la `73` hicieron para Grove, que llevo a la `72` y a la `75` a meter todo sin una sola
sorpresa. **Es regimen de insercion (`D.58`): la relectura de fidelidad se hace ENTERA, aqui, antes de que entren**, y en Gerber
importa mas: sus fichas se escribieron en un frente de regimen ligero, con muestra y no con lectura entera. Su insercion es de la
vuelta siguiente, despues de que mi fase ciega barra y lea lo que dejes y la `ACTA 75` lo adjudique.

**PUEDES LANZAR BARRIDOS DE FONDO, CINCO A LA VEZ COMO MUCHO, PERO NINGUNO VIVO AL CERRAR TU TURNO**: los recoges todos dentro,
vigilandolos si tardan. **Si no te caben, no los lances: lo dices en el reporte con los que faltan.** El `23` sep tres asientos
cerraron diciendo que esperaban un trabajo de fondo, y ninguno volvio. **Y NINGUN `insertar`**, ni en primer plano ni de fondo.

**EL RELOJ, MEDIDO, Y NO ES UN TECHO: ES LO QUE COSTO.** El barrido de la `73`, cinco fichas a la vez, por ficha (el menor y el
mayor, en segundos) y de punta a punta:

    $ grep "rc=" .v73ext/barrido.log | sed "s/.*segundos=//" | sort -n | sed -n "1p;\$p"; grep -E "^(INICIO|TODOS)" .v73ext/barrido.log
    411
    998
    INICIO 2026-09-26 02:04:16
    TODOS TERMINADOS 2026-09-26 02:23:54

## LA CLASE Y EL LIBRO, DICHOS POR EL INSTRUMENTO

    $ python scripts/deuda.py --clase 76
    LIBRE
      van 2 de 5 desde la ultima de saneamiento (la 74), con 52 deuda(s) esperando
    $ python forja.py tablero --puedo gerber_emyth
    LINEA 'serial', LIBRO 'gerber_emyth': SI
      'gerber_emyth' esta COSECHADO y sin dueño: su trabajo ya llego a esta rama, asi que se continua desde el capitulo siguiente al ultimo minado (cap_22), citando su frontera. D.50.

**La frase de *continuar desde `cap_22`* es de extraccion y no aplica: el frente de Gerber se cosecho y el de extraccion esta
cerrado para siempre** (`PARALELO.md` seccion `8` punto `3`). Lo que se hace es preparar su bandeja para insertarla.

---

## TAREA 1: **REGISTROS DE LA `ACTA 74`**

En una tabla corta y sin reabrir el argumento (`D.47`):

| que | donde |
|---|---|
| **La bloqueante cumplida**: los pasos `8` y `17` de `dar_elogio_disciplina_igual_critica` fuera del campo, en su orden, con su correccion declarada; la guarda `D.30` en verde | `ACTA 74` `74.0`, `74.3` |
| **Las `7` de Grove dentro, una por vez, sin solape y en su orden**; sus lineas de veredicto iguales letra a letra a las preparadas, a los pares del barrido del auditor y a sus clases selladas; sus aristas iguales par a par y por los dos lados | `74.3` |
| **Tus cuatro discutibles se sostienen**, `D75.1` a `D75.4`, y la muestra de los SANO tambien | `74.5` |
| **Cero caidas tuyas**: `REPORTE` vuelve a cero, y `R5` y `R9` cumplidos | `74.2`, `74.7`, `74.0` |
| **Una caida del auditor**: la cifra de deudas de su encargo de la `75`, que tu mismo declaraste en tu `75.0`; `AUDITOR` sube | `74.9` |

## TAREA 2: **LA FIDELIDAD ENTERA DE LAS FICHAS DE GERBER** (`D.30`, `D.58`)

Son **todas las fichas de `cuarentena/gerber_emyth/`**; **cuantas por capitulo y cuantos pasos trae cada una estan en la `ACTA 74`
`74.10`, bloque de `.v75aud/normal/bandeja_gerber.py`**, y tu primera medida es volver a correrlo. Todo en tu carpeta `.v76ext/`,
**con copias de instrumentos que ya existen y la ruta cambiada**, no con instrumentos nuevos (`7.F`):

1. **Cada paso contra la linea del libro que lo sostiene, en `fuentes/gerber_emyth/`, con su capitulo leido entero**, marcado `T` o
   `P` con su linea, en un fichero con una fila por paso como `.v73ext/fidelidad.tsv` (la clausula reescrita CUENTA como `P`,
   `ACTA 62` `62.5`), y sus citas comprobadas con una copia de `.v73ext/citas.sh`. **Hay fichas que citan mas de un capitulo**: el
   capitulo que se lee es el de la linea que cada paso cita, no solo el de su `UNIDAD DE ORIGEN`.
2. **`R9`, del extractor y con su letra** (`ACTA 73` `73.11`): toda fila `T` cuyo paso compare, contraste o califique la prueba del
   libro cita en su nota el tramo literal que lo sostiene, o es `P`; **y antes de publicar la cuenta de PUENTE, el `grep` de esas
   clausulas sobre los pasos que marcas `T`, pegado con lo que encuentre.** Tu patron de la `75` (`.v75ext/r9.py`) no ve *demostrar*
   (`ACTA 74` `74.4`): ensanchalo en tu copia.
3. **Todo PUENTE se corrige en la ficha de la bandeja por correccion declarada, con el texto viejo dentro, ANTES del barrido**, con
   una copia de `.v73ext/corregir_t2.py`: una ficha que cambia despues de su barrido tiene un barrido que ya no es suyo (`d031`). Y
   despues de la ultima correccion, **cada ficha normalizada y pasada por `aduana.validar_candidato`**, como `.v73ext/validar_siete.txt`.
4. **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo**, por una copia de `.v73ext/contar_fidelidad.py`, **y el peor capitulo
   nombrado** (`8.2`). **Si uno pasa del `10` por ciento, ese capitulo se relee entero antes de seguir** (`D.58`).
5. **Marca discutible todo paso en que dudes, al escribirlo.**

## TAREA 3: **EL BARRIDO, SOBRE LAS FICHAS YA CORREGIDAS**

Contra **GRAFO MAS BANDEJAS** (`D.38.4`), con copias de `.v73ext/barrido_uno.py` y `.v73ext/barrer.sh` con la lista de las fichas y
la ruta `.v76ext/`: **cinco a la vez como mucho, un log con su `INICIO` y su `TODOS TERMINADOS`, y todas recogidas dentro de tu
turno.** **La poblacion al abrir, con su reparto por sede, esta en la `ACTA 74` `74.1`, bloque de `.v70aud/poblacion.py`**: vuelve a
correrlo al abrir y pega su salida. **Una tabla por candidato de sus vecinos**, con una copia de `.v73ext/tabla_vecinos.py`.

## TAREA 4: **LOS VEREDICTOS, LAS ARISTAS Y EL ORDEN**

1. **Los veredictos listos, uno por vecino**, en el formato de `--veredicto` y con un bloque por candidato como
   `.v73ext/veredictos_listos.txt`: **leidos con los pasos de los dos delante** (`python .v64aud/pasos.py <a> <b>`) y por la vara
   `6.1`, y solo esa. **Y comprobado por instrumento que cada vecino del barrido tiene su linea y cada linea su vecino**, con una
   copia de `.v73ext/comprobar_veredictos.py`.
2. **Las aristas por lectura** (`D.29`, `D.53`), en un fichero como `.v73ext/aristas_lectura.txt`, con su tramo de madre y de hijo
   y su linea del libro, **mirando tambien madres que ya viven en el grafo**. **Estas deudas de Gerber piden su lectura para la vuelta
   que inserte el lote**, y se preparan aqui con su texto de `docs/loop/DEUDA.jsonl` pegado (`python scripts/deuda.py`):
   - **`d111`**: `recorrer_siete_pasos_programa_desarrollo_negocio` es cabeza de serie numerada (`D.37`), y sus partes que quedaban por
     minar eran las de `cap_18` y `cap_19`. **Lee si alguna ficha de esos dos capitulos es una de sus partes**; si lo es, la arista
     cabeza a parte se declara citando la linea; si no, la cabeza entra sin arista a parte, y lo dices con la medida delante. **Si la
     lectura pidiera algo que `D.37` no cubre por su letra, paras y lo traes**: no lo decides al vuelo.
   - **`d108`**: `cap_14` `L27` contra `L117`, con las dos delante, por `responder_8_preguntas_construir_primary_aim`.
   - **`d098`**: el puntero de las tres fases de `cap_05` `L29`: **mira si alguna ficha es su cabeza o una de sus partes**.
   **`D.37`** tambien para los titulos que dicen cuantas partes tienen (`aplicar_cinco_pasos_proceso_contratacion`,
   `aplicar_seis_pasos_sistema_venta`, `aplicar_ocho_reglas_juego_personas`, `construir_estrategia_gente_cuatro_componentes`,
   `interrogar_negocio_cinco_preguntas`, `medir_sistema_venta_trece_indicadores_benchmark` y los demas): **si alguna parte es nodo,
   la arista cabeza a parte se declara; si la cabeza solo cuenta y nombra, no hay arista** (`D68.7`). Marca discutible lo que dudes.
3. **El orden de insercion**, con una copia de `.v73ext/orden.py`: **madre antes que hijo, `D.36`, y las comprobaciones en cero.**

**Si no te cabe todo, parte por capitulo y por donde se pueda auditar**: primero `cap_13`, `cap_18` y `cap_19` juntos, porque son los
de `d111`, y dentro de cada uno la fidelidad antes que el barrido y el barrido antes que los veredictos. **Lo que no hagas lo dices
con su fila vacia**, y la vuelta siguiente empieza por ahi.

## TAREA 5: **EL CIERRE**

- **El censo antes y despues**: nodos, veredictos, pares mutuos, bandeja de Gerber e insertados de Gerber, con una copia de
  `.v75ext/censo.sh` con esas dos rutas. **No entra nada**: al abrir son los de la `ACTA 74` `74.1`, y al cerrar tienen que ser los
  mismos.
- **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo**, que son **preparacion y no entrada**.
- **La huella de las fichas preparadas**, con una copia de `.v73ext/pasos_y_huellas.py` con la lista de esta vuelta, corrida despues
  del ultimo cambio de ficha y pegada: es contra lo que la vuelta de insercion comprobara que entra lo que se leyo.
- **`D.61`**: cada discutible ejecutado o cerrado. Ninguno abierto.
- **`R5`** en cada bloque `$` de tu tramo, **medido con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera
  cambiada a la `76`**, y pegado. **Y `R9`** en toda cuenta de PUENTE que publiques.
- `python forja.py gate`, `python forja.py guiones`, `python tests/test_aceptacion.py` y `python scripts/cerrar_reporte.py`,
  **pegados**. **El cierre estricto tiene que salir en verde: cualquier rojo es tuyo.**
- Commitea `docs/loop/`, las fichas corregidas de la bandeja y tu carpeta `.v76ext/`. **Si nada te obliga a parar, no escribas
  `PARA_ALEXIS.md`.**

---

## LO QUE NO HACES

- **NO INSERTAS NINGUNA FICHA**, y **NO TERMINAS TU TURNO CON NADA VIVO**, ni un barrido.
- **NO TOCAS `cuarentena/marquet_turn_the_ship/`**: va despues de Gerber.
- **NO TOCAS NINGUN NODO DEL GRAFO.** Si una lectura de vecino te enseña un defecto en uno, lo traes al reporte y no lo corriges.
- **NO TOCAS `src/`, `scripts/`, el banco, el arnes, el tablero ni los protocolos** (`7.F`, `D.55`), **ni `APERTURA_CIEGA.md`**. Los
  procesos del fundador que veas vivos en otra copia no son tuyos: ni los tocas ni los esperas.
- **NO REORDENAS LA COLA A MANO**, **NO PAGAS NINGUNA DEUDA** (las de la TAREA `4.2` se leen aqui y se pagan en la vuelta que
  inserte) y **NO ABRES NINGUN LIBRO.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No
adivines.**
