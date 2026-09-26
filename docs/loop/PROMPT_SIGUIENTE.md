# ENCARGO DE LA VUELTA 78: **LAS FICHAS DE MARQUET DEJADAS LISTAS PARA INSERTAR: SU FIDELIDAD LEIDA ENTERA, SUS VECINOS BARRIDOS, SUS VEREDICTOS ESCRITOS, SUS ARISTAS LEIDAS Y SU ORDEN COMPROBADO. AQUI NO SE INSERTA NINGUNA** (`ACTA 76` `76.11`)

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 76`, que audito la vuelta `77`.
`AUDITOR_FORJA.md` seccion `1.4`. **Toda cifra de medida de esta pagina va dentro de un bloque `$` con su salida, o lleva en
su misma linea la seccion de la `ACTA 76` donde esta pegada** (`R8`, `ACTA 76` `76.12`).*

> # **LIBRO DE ESTA VUELTA: `marquet_turn_the_ship`**
> # **CLASE DE ESTA VUELTA: INSERCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **LA REGLA DEL TURNO, Y POR QUE ESTA VUELTA NO INSERTA**

**Gerber entro entero en la `77`**: su bandeja esta vacia y el libro vive en el grafo y en `_insertados` (`ACTA 76` `76.1`). **El
orden de la campania es Grove, Gerber, Marquet** (`PARALELO.md` seccion `8` punto `4`), y Marquet es el ultimo libro del corte (`76.11`). Esta
vuelta hace para la bandeja de Marquet lo que la `76` hizo para la de Gerber, que llevo a la `77` a meter las fichas sin una sola
sorpresa. **Es regimen de insercion (`D.58`): la relectura de fidelidad se hace ENTERA, aqui, antes de que entren**, porque las
fichas de Marquet se escribieron en un frente de regimen ligero, con muestra y no con lectura entera. Su insercion es de una vuelta
posterior, despues de que mi fase ciega barra y lea lo que dejes y la `ACTA 77` lo adjudique.

**PUEDES LANZAR BARRIDOS DE FONDO, CINCO A LA VEZ COMO MUCHO, PERO NINGUNO VIVO AL CERRAR TU TURNO**: los recoges todos dentro,
vigilandolos si tardan. **Si no te caben, no los lances: lo dices en el reporte con los que faltan.** El `23` sep hubo asientos que
cerraron diciendo que esperaban un trabajo de fondo, y ninguno volvio. **Y NINGUN `insertar`**, ni en primer plano ni de fondo. El
presupuesto de plazas de la maquina bajo el 26 sep (`docs/loop/paradas/2026-09-26-seis-plazas-NOTA.md`), y `src/presupuesto.py` lo
respeta.

**EL RELOJ, MEDIDO, Y NO ES UN TECHO: ES LO QUE COSTO.** El barrido de la `76`, por ficha (el menor y el mayor, en segundos) y
de punta a punta:

    $ grep "rc=" .v76ext/barrido.log | sed "s/.*segundos=//" | sort -n | sed -n "1p;\$p"; grep -E "^(INICIO|TODOS)" .v76ext/barrido.log
    269
    1209
    INICIO 2026-09-26 07:10:53
    TODOS TERMINADOS 2026-09-26 07:53:49

## LA CLASE Y EL LIBRO, DICHOS POR EL INSTRUMENTO

    $ python scripts/deuda.py --clase 78
    LIBRE
      van 4 de 5 desde la ultima de saneamiento (la 74), con 50 deuda(s) esperando
    $ python forja.py tablero --puedo marquet_turn_the_ship
    LINEA 'serial', LIBRO 'marquet_turn_the_ship': SI
      'marquet_turn_the_ship' esta COSECHADO y sin dueño: su trabajo ya llego a esta rama, asi que se continua desde el capitulo siguiente al ultimo minado (cap_17), citando su frontera. D.50.

**La frase de *continuar desde `cap_17`* es de extraccion y no aplica: el frente de Marquet se cosecho y el de extraccion esta
cerrado para siempre** (`PARALELO.md` seccion `8` punto `3`). Lo que se hace es preparar su bandeja para insertarla.

---

## TAREA 1: **REGISTROS DE LA `ACTA 76`**

En una tabla corta y sin reabrir el argumento (`D.47`):

| que | donde |
|---|---|
| **Tu vuelta, reproducida**: tus instrumentos dan lo que pegaste, y el cierre estricto del auditor sale verde | `ACTA 76` `76.1` |
| **Las `22` de Gerber dentro, una por vez, sin solape, en su orden y despues del commit de la TAREA 2**; sus lineas de veredicto iguales letra a letra a las preparadas, a las filas del barrido del auditor y a sus clases selladas; sus aristas iguales par a par y por los dos lados; ningun nodo viejo cambia | `76.4` |
| **La relectura conjunta se cierra**: las dos piezas las gana la lectura del auditor y tu las ejecutaste; la arista `fingir` a `recorrer` con `CONTINUA` y el paso `1` se sostiene | `76.3` |
| **Tus cuatro discutibles se sostienen**, y `D77.4` se adjudica sin especie | `76.3` |
| **`d111` y `d108` firmadas** | `76.3` |
| **Cero caidas tuyas**: `REPORTE` vuelve a cero, `R5` cumplido y `R9` sin objeto | `76.2`, `76.8`, `76.0` |

## TAREA 2: **LA FIDELIDAD ENTERA DE LAS FICHAS DE MARQUET** (`D.30`, `D.58`)

Son **todas las fichas de `cuarentena/marquet_turn_the_ship/`**; **cuantas por capitulo y cuantos pasos trae cada una estan en la
`ACTA 76` `76.11`, bloque de `.v77aud/normal/bandeja_marquet.py`**, y tu primera medida es volver a correrlo. Todo en tu carpeta
`.v78ext/`, **con copias de instrumentos que ya existen y la ruta cambiada**, no con instrumentos nuevos (`7.F`):

1. **Cada paso contra la linea del libro que lo sostiene, en `fuentes/marquet_turn_the_ship/`, con su capitulo leido entero**,
   marcado `T` o `P` con su linea, en un fichero con una fila por paso como `.v76ext/fidelidad.tsv` (la clausula reescrita CUENTA
   como `P`, `ACTA 62` `62.5`), y sus citas comprobadas con una copia de `.v76ext/citas.sh`. **El capitulo que se lee es el de la
   linea que cada paso cita**, no solo el de su `UNIDAD DE ORIGEN`.
2. **`R9`, del extractor y con su letra**: toda fila `T` cuyo paso compare, contraste o califique la prueba del libro cita en su
   nota el tramo literal que lo sostiene, o es `P`; **y antes de publicar la cuenta de PUENTE, el `grep` de esas clausulas sobre los
   pasos que marcas `T`**, con una copia de `.v76ext/r9.py`, pegado con lo que encuentre.
3. **Todo PUENTE se corrige en la ficha de la bandeja por correccion declarada, con el texto viejo dentro, ANTES del barrido**, con
   una copia de `.v76ext/corregir_t2.py`: una ficha que cambia despues de su barrido tiene un barrido que ya no es suyo (`d031`). Y
   despues de la ultima correccion, **cada ficha normalizada y pasada por `aduana.validar_candidato`**, como `.v76ext/validar.py`.
4. **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo**, por una copia de `.v76ext/contar_fidelidad.py`, **y el peor capitulo
   nombrado** (`8.2`). **Si uno pasa del `10` por ciento, ese capitulo se relee entero antes de seguir** (`D.58`).
5. **`d150` se prepara aqui.** Su texto:

       $ grep '"id": "d150"' docs/loop/DEUDA.jsonl | grep -o '"que": "[^"]*"'
       "que": "La TAREA 2 y la TAREA 3 del reporte de la vuelta 1 del frente marquet siguen sin escribirse desde los papeles de .vm01/, que estan intactos con 47 ficheros, y la fila de cap_03 sigue publicada en 0,00 donde la ACTA M2 la recontro."

   **Tu fila de `cap_03`, contada entera paso a paso, es la cifra que `d150` pedia**: la pegas con su texto delante, y **no la
   pagas** (se paga en la vuelta que inserte).
6. **Marca discutible todo paso en que dudes, al escribirlo.**

## TAREA 3: **EL BARRIDO, SOBRE LAS FICHAS YA CORREGIDAS**

Contra **GRAFO MAS BANDEJAS** (`D.38.4`), con copias de `.v76ext/barrido_uno.py` y `.v76ext/barrer.sh` con la lista de las fichas y
la ruta `.v78ext/`: **cinco a la vez como mucho, un log con su `INICIO` y su `TODOS TERMINADOS`, y todas recogidas dentro de tu
turno.** **La poblacion al abrir, con su reparto por sede, esta en la `ACTA 76` `76.1`, bloque de `.v70aud/poblacion.py`**: vuelve a
correrlo al abrir y pega su salida. **Una tabla por candidato de sus vecinos**, con una copia de `.v76ext/tabla_vecinos.py`.
**Marquet solapa en parte con Zhuo y con Scott, que ya viven en el grafo** (`PARALELO.md`, *Los tres del mundo 11, con el motivo literal de la decision*): sus
vecinos del grafo se leen con el mismo cuidado que los de la bandeja.

## TAREA 4: **LOS VEREDICTOS, LAS ARISTAS Y EL ORDEN**

1. **Los veredictos listos, uno por vecino**, en el formato de `--veredicto` y con un bloque por candidato como
   `.v76ext/veredictos_listos.txt`: **leidos con los pasos de los dos delante** (`python .v64aud/pasos.py <a> <b>`) y por la vara
   `6.1`, y solo esa. **Y comprobado por instrumento que cada vecino del barrido tiene su linea y cada linea su vecino**, con una
   copia de `.v76ext/comprobar_veredictos.py`.
2. **Las aristas por lectura** (`D.29`, `D.37`, `D.53`), en un fichero como `.v76ext/aristas_lectura.txt`, con su tramo de madre y
   de hijo y su linea del libro, **mirando tambien madres que ya viven en el grafo**, las de Zhuo y Scott las primeras. **`D.37`
   tambien para los titulos que dicen cuantas partes tienen**: si alguna parte es nodo, la arista cabeza a parte se declara; si la
   cabeza solo cuenta y nombra, no hay arista (`D68.7`). **Un par cabeza a parte que la senial levanta va `SANO` en su linea, con su
   arista aparte** (`D.53`, como la `ACTA 75` `75.4` adjudico en Gerber). Marca discutible lo que dudes.
3. **El orden de insercion**, con una copia de `.v76ext/orden.py`: **madre antes que hijo, `D.36`, y las comprobaciones en cero**, y
   **las aristas esperadas** que el orden imprime.

**Si no te cabe todo, parte por capitulo y por donde se pueda auditar**: primero `cap_03`, que es el que mas fichas tiene (`76.11`) y el
de `d150`, y dentro de cada uno la fidelidad antes que el barrido y el barrido antes que los veredictos. **Lo que no hagas lo dices con
su fila vacia**, y la vuelta siguiente empieza por ahi.

## TAREA 5: **EL CIERRE**

- **El censo antes y despues**: nodos, veredictos, pares mutuos, bandeja de Marquet e insertados de Marquet, con una copia de
  `.v77ext/censo.sh` con esas dos rutas. **No entra nada**: al abrir son los de la `ACTA 76` `76.1`, y al cerrar tienen que ser los
  mismos.
- **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo**, que son **preparacion y no entrada**.
- **La huella de las fichas preparadas**, con una copia de `.v76ext/pasos_y_huellas.py` con la lista de esta vuelta, corrida despues
  del ultimo cambio de ficha y pegada: es contra lo que la vuelta de insercion comprobara que entra lo que se leyo.
- **`D.61`**: cada discutible ejecutado o cerrado. Ninguno abierto.
- **`R5`** en cada bloque `$` de tu tramo, **medido con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera
  cambiada a la `78`**, y pegado. **Y `R9`** en toda cuenta de PUENTE que publiques.
- **LA CABECERA, LAS TABLAS DE TAREAS Y LA TABLA DE CIERRE: cada cifra de sus celdas sale de un instrumento corrido en esta vuelta**,
  y se reescriben al cerrar contra lo que se hizo, como hiciste en la `77`.
- `python forja.py gate`, `python forja.py guiones`, `python tests/test_aceptacion.py` y `python scripts/cerrar_reporte.py`,
  **pegados**. **El cierre estricto tiene que salir en verde: cualquier rojo es tuyo.**
- Commitea `docs/loop/`, las fichas corregidas de la bandeja y tu carpeta `.v78ext/`. **Si nada te obliga a parar, no escribas
  `PARA_ALEXIS.md`.**

---

## LO QUE NO HACES

- **NO INSERTAS NINGUNA FICHA**, y **NO TERMINAS TU TURNO CON NADA VIVO**, ni un barrido.
- **NO TOCAS NINGUN NODO DEL GRAFO.** Si una lectura de vecino te enseña un defecto en uno, lo traes al reporte y no lo corriges.
- **NO TOCAS `src/`, `scripts/`, `config/`, el banco, el arnes, el tablero ni los protocolos** (`7.F`, `D.55`), **ni
  `APERTURA_CIEGA.md`**. Los procesos del fundador que veas vivos en otra copia no son tuyos: ni los tocas ni los esperas.
- **NO REORDENAS LA COLA A MANO**, **NO PAGAS NINGUNA DEUDA** (`d150` se prepara aqui y se paga en la vuelta que inserte) y **NO
  ABRES NINGUN LIBRO.**
- **NO CREAS EL TAG NI PARAS LA CAMPANIA**: eso es de la vuelta que meta la ultima ficha de Marquet (`PARALELO.md` seccion `8`
  puntos `4` y `5`).

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No
adivines.**
