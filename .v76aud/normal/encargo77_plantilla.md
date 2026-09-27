# ENCARGO DE LA VUELTA 77: **LA RELECTURA CONJUNTA DE UN PAR Y UNA ARISTA, Y DESPUES LAS `22` FICHAS DE GERBER DENTRO, UNA POR VEZ, EN EL ORDEN, CON LAS LINEAS Y LAS ARISTAS QUE LA `76` DEJO LISTAS** (`ACTA 75` `75.4`, `75.10`)

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 75`, que audito la vuelta `76`.
`AUDITOR_FORJA.md` seccion `1.4`. **Toda cifra de medida de esta pagina va dentro de un bloque `$` con su salida, o lleva en
su misma linea la seccion de la `ACTA 75` donde esta pegada** (`R8`, `ACTA 75` `75.11`).*

> # **LIBRO DE ESTA VUELTA: `gerber_emyth`**
> # **CLASE DE ESTA VUELTA: INSERCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **LA CLASE, EL LIBRO Y LA REGLA DEL TURNO**

    $ python scripts/deuda.py --clase 77
    {{SALIDA}}
    $ python forja.py tablero --puedo gerber_emyth
    {{SALIDA}}

**La frase de *continuar desde `cap_22`* es de extraccion y no aplica: el frente de Gerber esta cerrado** (`PARALELO.md` `8` punto
`3`), y lo que se hace es insertar lo que la `76` dejo listo en su bandeja. **El orden de la campania es Grove, Gerber, Marquet**
(`PARALELO.md` `8` punto `4`), y Grove ya esta dentro (`ACTA 75` `75.10`).

> **UN `insertar` POR VEZ, Y NINGUNO EN VUELO CUANDO TU TURNO TERMINE.** Cada candidato entra entero o no entra. **Al volver cada
> `insertar`: su fila en el reporte, commit y push.**

**El metodo de la `75` vale**: cada `insertar` por una copia de `.v75ext/insertar.py` con la sede de las lineas cambiada a
`.v76ext/veredictos_listos.txt` (o a tu copia corregida por la TAREA `2`) y la salida a `.v77ext/`, y tu bloqueado en primer plano con
una copia de `.v75ext/esperar.py` hasta su `.fin`, **sin lanzar el siguiente ni tocar el dataset ni la bandeja en medio**. **NO LANZAS
NADA EN SEGUNDO PLANO QUE SIGA VIVO AL CERRAR TU TURNO.** Si algo no te cabe, no lo lances: lo dices en el reporte con las filas que
faltan, y entran en la `78`. El reloj de los `insertar` de la `72` y de la `75`, que es lo que costo y no un techo:

    $ tail -1 .v72ext/relojes_resumen.txt; tail -1 .v75ext/relojes.txt
    {{SALIDA}}

---

## TAREA 1: **REGISTROS DE LA `ACTA 75`**

En una tabla corta y sin reabrir el argumento (`D.47`):

| que | donde |
|---|---|
| **Tu vuelta, reproducida**: tus instrumentos dan lo que pegaste, tus `22` fichas son las que el auditor barrio byte a byte, y tu barrido es el suyo fila a fila | `ACTA 75` `75.1`, `75.4` |
| **Tu fidelidad se sostiene paso a paso**: tus `P` son los que corregiste, ningun `T` tuyo cae, y `D76.10` se sostiene entero (el paso `4` de `cuantificar` es `T`) | `75.3` |
| **Tus diecinueve discutibles**: dieciocho se sostienen; `D76.14` gana contra la lectura ciega del auditor; **`D76.15`, en la contratacion, va a la relectura conjunta** | `75.5` |
| **Una caida tuya de `REPORTE`**: *`9` PUENTE* donde tu fichero, tu instrumento y tu tabla de `76.5.b` dan `8`, en tu tabla de tareas, en un titulo y en una conclusion. **`REPORTE` sube a `1 de 3`.** La cifra buena se declara en tu `77.1`, sin tocar el tramo de la `76` | `75.2`, `75.7` |
| **El auditor**: su tanda sale limpia y `AUDITOR` vuelve a cero; cuatro lecturas de su fase ciega caen, sin especie | `75.9` |

## TAREA 2: **LA RELECTURA CONJUNTA, ANTES DEL PRIMER `insertar`** (`1.3`, `ACTA 75` `75.4`)

**El caso del auditor esta escrito en la `ACTA 75` `75.4`, con su evidencia. Tu lo verificas con los pasos de los dos delante
(`python .v64aud/pasos.py <a> <b>`) y decides por la vara `6.1`, y solo esa.** Las dos piezas:

1. **El par `construir_estrategia_gente_cuatro_componentes` con `aplicar_cinco_pasos_proceso_contratacion`** (tu `D76.15`): tu
   `SANO` contra el `CONTINUA` del auditor con madre `construir`. **Si te convence**, las dos lineas del par (`75.4`) se reescriben en una
   copia `.v77ext/veredictos_listos.txt` de `.v76ext/veredictos_listos.txt`, con `madre=construir_estrategia_gente_cuatro_componentes` y
   su razon, **dejando la linea vieja encima como comentario `#` con la marca de correccion declarada**, y esa copia es la sede de tus
   lineas. **Si no te convence**, escribes tu caso contrario con los pasos delante y la linea sigue `SANO`: decides tu (`1.3`), y la
   `ACTA 76` lo adjudica.
2. **La arista `fingir_prototipo_cinco_mil_replicas` a `recorrer_siete_pasos_programa_desarrollo_negocio`, por `D.29`**, que tu
   lectura no miro. **Si la sostienes**, una fila `SOSTENGO` en una copia `.v77ext/aristas_lectura.txt` de `.v76ext/aristas_lectura.txt`,
   con su paso de madre, su tramo y su linea; **si no**, una fila `NO SOSTENGO` con su razon.

**Ninguna de las dos mueve el orden** (`ACTA 75` `75.4`): se decida lo que se decida, la madre va antes que el hijo en
`.v76ext/orden.txt`. **Lo que cambia son las aristas esperadas**, y las dices al cerrar esta tarea con la copia de `.v76ext/orden.py`
corrida sobre tus copias si las hay. **Commit de la tarea antes del primer `insertar`.**

## TAREA 3: **LO QUE ENTRA ES LO QUE SE LEYO**

Antes del primer `insertar`, `python .v76ext/pasos_y_huellas.py`, con su salida **identica** a `.v76ext/pasos_y_huellas.txt` (el
auditor la reprodujo, `ACTA 75` `75.1`), pegada. Si una ficha sale distinta, **no entra**, se relee entera contra su capitulo y se dice.

## TAREA 4: **LAS `22` FILAS DE `.v76ext/orden.txt`, UNA POR VEZ** (`ACTA 75` `75.1`, `75.4`)

    $ sed -n '2,23p' .v76ext/orden.txt | cut -c1-80
    {{SALIDA}}
    $ sed -n '31,40p' .v76ext/orden.txt
    {{SALIDA}}
    $ grep -v '^#' .v76ext/veredictos_listos.txt | grep -c '|'
    {{SALIDA}}

1. **En su orden, de la fila `1` a la ultima.** Las lineas `--veredicto` son las del bloque de cada candidato en tu sede de lineas
   (TAREA `2`), **tal cual, sin las `#`**. Las `CONTINUA` con `madre=` cablean su arista en el acto.
2. **Las aristas por lectura se declaran EN EL ACTO DE INSERTAR LA PARTE** (`D.37`, `D.29`), con los dos extremos ya vivos, por una
   copia de `.v72ext/arista.py` que lea tu sede de aristas, **cada una citando el paso de la madre de su fila `SOSTENGO`**. El
   `--veredicto` es el de la lectura, no el de la arista (`D.53`): **`SANO` en las de serie `D.37`**, que es lo que tus lineas del par
   `recorrer` con `construir` ya dicen; y el que tu lectura diga en la de la TAREA `2.2` si la sostienes. **Cada una despues de su
   hijo** (`75.4`): las cuatro de `fingir` al entrar `dar_valor`, `operar_modelo`, `unificar_color` y `documentar_trabajo`; la de `recorrer` a
   `construir` al entrar `construir`; la de `construir` a `documentar_trabajo` al entrar `documentar_trabajo`.
3. **La puerta es la aduana de `insertar`, no la lista** (`d031`). **Al volver cada uno, su vecindad de hoy contra la del barrido de
   la `76`** con una copia de `.v75ext/contra_barrido.py` que lea `.v76ext/vecinos_<id>.json`, pegada en su fila. Si levanta un vecino
   sin linea, lo lees con los pasos de los dos delante, escribes su veredicto por la vara `6.1` y solo esa, **y lo marcas en el reporte
   como lectura tuya de esta vuelta**, discutible si dudas. Si levanta `CAERIA` o un error, no fuerces: no entra, y se declara.
4. **Al volver cada `insertar`, su fila en el reporte** como las de la `75`: la aduana de hoy con sus vecinos, la comparacion con la
   `76`, las lineas que pasaste, las aristas que cableo y su commit. Cada insertado a `cuarentena/_insertados/gerber_emyth/` (`D.31`).
5. **`d111` y `d108` se pagan aqui, tu pagas y el auditor firma**: `d111` cuando la arista de `recorrer` a `construir` viva, con su
   `--como` citando la `ACTA 75` `75.4` (*la cabeza entra con una parte de siete*); `d108` con la lectura de tu `76.4.2`, firmada en la
   `ACTA 75` `75.4`, sin tocar la ficha. Por `python scripts/deuda.py --pagar <id> --vuelta 77 --como "..."`. **`d098` y `d104` siguen
   vivas**: ninguna de las `22` es su cabeza (`75.1`, `75.4`).
6. **Al terminar la ultima fila que entre: las aristas de la tanda por instrumento**: cuantas se esperaban (TAREA `2`), cuantas viven
   en el grafo por los dos lados, ninguna sin adjudicar, y que ningun nodo viejo cambio fuera del `nodos_siguientes` de sus madres. Si
   alguna fila no entro, la cuenta dice cuales quedan pendientes con ella.

## TAREA 5: **EL CIERRE**

- **El censo antes y despues de cada tarea**, con una copia de `.v76ext/censo.sh`. Al abrir son los de la `ACTA 75` `75.1`. **Lo que
  se mueve, medido**: el grafo gana una fila por ficha que entre; la bandeja de Gerber pierde las mismas y `_insertados` las gana; la
  bitacora gana las lineas de veredicto de lo que entre mas una por arista por lectura. **Si entran todas, `python forja.py tablero`,
  pegado**, con la fila de Gerber: la vuelta siguiente abre con el libro que el tablero de entonces de a esta linea.
- **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo, de lo que ENTRO**, contado desde `.v76ext/fidelidad.tsv` con los PUENTE ya
  corregidos en la bandeja, que la `ACTA 75` `75.3` firmo en cero que entran. No a ojo.
- **`D.61`**: cada discutible ejecutado o cerrado. Ninguno abierto.
- **`R5`** en cada bloque `$` de tu tramo, medido con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera
  cambiada a la `77`, y pegado. **Y `R9`**, donde marques fidelidad.
- **LA CABECERA, LAS TABLAS DE TAREAS Y LA TABLA DE CIERRE: cada cifra de sus celdas sale de un instrumento corrido en esta vuelta**, y
  se reescriben al cerrar contra lo que se hizo. **Tu ultima caida vivio en una celda de la tabla de tareas** (`ACTA 75` `75.2`), y el
  cierre estricto no la ve.
- `python forja.py gate`, `python forja.py guiones`, `python tests/test_aceptacion.py` y `python scripts/cerrar_reporte.py`,
  **pegados**. **El cierre estricto tiene que salir en verde: cualquier rojo es tuyo.**
- Commitea `docs/loop/`, `dataset/`, `bitacora/`, `censos/`, los movidos a `_insertados` y tu carpeta `.v77ext/`. **Si nada te obliga
  a parar, no escribas `PARA_ALEXIS.md`.**

---

## LO QUE NO HACES

- **NO INSERTAS NADA ANTES DE CERRAR LA TAREA 2**, y **NO TERMINAS TU TURNO CON NADA VIVO**, ni un `insertar` ni un barrido.
- **NO CORRIGES NINGUN NODO DEL GRAFO.** Si una lectura de vecino te enseña un defecto en uno, lo traes al reporte y no lo corriges.
- **NO CAMBIAS NINGUNA LINEA PREPARADA NI NINGUNA FICHA** fuera de la TAREA `2` y de lo que la aduana levante en el acto (TAREA
  `4.3`). Su fidelidad y sus clases estan firmadas.
- **NO TOCAS `cuarentena/marquet_turn_the_ship/`**: va despues de Gerber.
- **NO TOCAS `src/`, `scripts/`, el banco, el arnes, el tablero ni los protocolos** (`7.F`, `D.55`), **ni `APERTURA_CIEGA.md`**. Los
  procesos del fundador que veas vivos en otra copia no son tuyos: ni los tocas ni los esperas.
- **NO REORDENAS LA COLA A MANO**, **NO PAGAS NINGUNA DEUDA** fuera de `d111` y `d108` (TAREA `4.5`) y **NO ABRES NINGUN LIBRO.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No
adivines.**
