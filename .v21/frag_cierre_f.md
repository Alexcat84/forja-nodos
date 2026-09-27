
## O.8. LAS CONDICIONES DE PARADA, REPASADAS UNA A UNA (`EXTRACTOR.md` 7)

| condicion | |
|---|---|
| **Algo contradice una regla vigente** | **NO, Y LO RAZONO PORQUE ES LA QUE MAS CERCA ESTUVO.** La negrita de la TAREA 3 (*cableadas en la misma vuelta en que se escriban sus partes*) no cabe con `D.39`, pero **no hay dos reglas en conflicto**: `D.37` dice `INSERTAS`, el instrumento dice *en el acto de insertarla*, `D.39` no deja insertar un lote abierto, y la decision 4 del fundador dice *sin insercion porque el lote sigue abierto*. **Cuatro piezas escritas coinciden y la negrita esta sola.** Va como PROPUESTA 2 y no como parada (`O.4.b`, `O.6.8`) |
| **Algo contradice una cifra publicada con su corte** | **NO, y las discrepancias que encontre las declaro en vez de resolverlas copiando** (`EXTRACTOR.md` 5): el coste del informe (**453 s** contra los **156,5** de `D.41`, `O.6.2`), y la promesa de `D.38.5` de que la aduana levantaria el par (**no lo levanta**, `O.5.b`). **Las ocho filas heredadas de `PASOS INVENTADOS` reproducen al digito** (`O.6.3`) |
| **Doctrina NUEVA necesaria** | **NO.** Los tres cortes que lo parecian se resuelven **por regla ya escrita**: las tres conversaciones sin cabeza con manual 3.4 y la vara de `4.1` (`O.6.6` discutible 1); el par de despedir con la vara de `CONTINUA` contra `REPITE` (discutible 7); y el par de la lupa **venia adjudicado** por la decision 3 del fundador |
| **Una operacion cuyo texto no alcanza para ejecutarse sin decidir** | **NO.** La unica que lo roza es la TAREA 3, y **no tuve que decidir nada**: corri el instrumento, pegue su rechazo, y **la regla que manda estaba escrita en mi propio manual** (`EXTRACTOR.md` 15.6) |
| **Un pendiente de doctrina** | **NO DETIENE, y no hay ninguno abierto.** Las cuatro cosas que traigo van como propuestas con su cifra (`O.6.8`) |
| **Yo no escribo `PARA_ALEXIS.md`** | **No lo escribo.** `EXTRACTOR.md` 7 y 14: eso lo hace el auditor |

> # **NO HAY PARADA. LA VUELTA 21 CIERRA LAS CUATRO TAREAS Y CIERRA SU REPORTE.**

## O.9. `D.32`: ESTA VUELTA **NO CIERRA NINGUN LOTE**, y mido el estado igual

    $ ls fuentes/scott_radical_candor/*.md | wc -l                   ->  15 unidades
    $ grep -c "scott_radical_candor" fuentes/FUENTES_CANONICAS.json  ->   2 (la clave esta)
    $ ls cuarentena/scott_radical_candor/*.json | wc -l              ->  96 candidatos, 1050 pasos
    $ python (nodos del grafo con fuente scott_radical_candor)        ->   0 de 203

| | |
|---|---|
| **lote 4** | **ABIERTO**, y **sin ningun capitulo partido**: `cap_00` a `cap_10` **enteros**, `cap_11` a `cap_14` sin minar (**27.680 palabras**) |
| **condicion 1 de `D.32`** (material en `fuentes/<clave>/`) | **VERDE**: los 15 ficheros estan |
| **condicion 2 de `D.32`** (clave en la tabla canonica) | **VERDE**, y lo prueba que los trece informes de hoy no dieron ni un rechazo de fuente |
| **cola de extraccion** | `cap_11` a `cap_14`, **cuatro unidades** |
| **insercion** | **NO se abre**: `D.39` solo inserta un lote **CERRADO**. **Cero inserciones en la vuelta 21 es la regla funcionando, por cuarta vez** |

### O.9.1. EL VOLUMEN QUE LA VUELTA SIGUIENTE TENDRIA, MEDIDO

*Las tres puertas de `EXTRACTOR.md` 12.4, cada una con su cifra de hoy.*

| puerta | cifra de hoy | se dispara? |
|---|---|---|
| **`PASOS INVENTADOS`** | peor unidad **`cap_04` 6,25 contra tope 10** | **NO.** El tramo NO baja: sigue en **tres capitulos** |
| **cerrar el reporte** | **la vuelta 21 SI cerro el suyo, entero** | **NO** |
| **techo de candidatos** | **`cap_10` dio 13 y cabia bajo 15**, y esta vuelta corrio a un capitulo por eso y no por el freno | **no aplica ya a `cap_10`** |

**LOS CUATRO QUE QUEDAN, CON SU CUERPO MEDIDO POR MI HOY:**

    $ python (cuerpo de cap_11 a cap_14, sed -n '8,$p' | wc -w cada uno)

| unidad | rotulo | cuerpo | proyeccion por la densidad de `cap_10` (`690` palabras por nodo) |
|---|---|---:|---:|
| `cap_11` | `Cap. 8` | **8.626** | **~12,5** |
| `cap_12` | `Getting Started` | **2.118** | **~3** |
| `cap_13` | `Afterword` | **9.298** | **~13,5** |
| `cap_14` | `Bonus Chapter` | **7.638** | **~11** |
| | **los cuatro juntos** | **27.680** | **~40** |

**LA DENSIDAD DE `cap_10` MEDIDA POR MI: `8.976 / 13 = 690` palabras por candidato**, contra las
`874` de `cap_09`. **Y digo lo que eso vale y lo que no:** la proyeccion por densidad fallo en
`cap_10` (predijo `10,3` y fueron `13`), asi que **la doy como orden de magnitud y no como cuenta**.
Lo que si se sostiene es la direccion: **con `~690` palabras por nodo, `cap_11` solo ya pasaria
del techo de 15 si midiera mas de `10.350` palabras**, y eso **se mide en su vuelta y no en esta**.
