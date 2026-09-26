# ENCARGO DE LA VUELTA 73: **LAS ULTIMAS FICHAS DE GROVE (`cap_15`, `cap_16` Y `cap_17`) DEJADAS LISTAS PARA INSERTAR: SU FIDELIDAD LEIDA ENTERA, SUS VECINOS BARRIDOS, SUS VEREDICTOS ESCRITOS, SUS ARISTAS LEIDAS Y SU ORDEN COMPROBADO. AQUI NO SE INSERTA NINGUNA**

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 71`, que audito la vuelta `72`.
`AUDITOR_FORJA.md` seccion `1.4`. **Toda cifra de medida de esta pagina va dentro de un bloque `$` con su salida, o lleva en
su misma linea la seccion de la `ACTA 71` donde esta pegada** (`R8`, escalado en la `ACTA 71` `71.11`).*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: INSERCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **LA REGLA DEL TURNO, Y POR QUE ESTA VUELTA NO INSERTA**

**La tanda que estaba lista entro entera en la `72`** (`ACTA 71` `71.3`): no queda nada adjudicado que insertar. Esta vuelta hace
para las fichas que quedan en la bandeja de Grove lo que la `71` hizo para las de `cap_07` a `cap_14`, que llevo a la `72` a meter
todas sin una sola sorpresa. **Es regimen de insercion (`D.58`): la relectura de fidelidad se hace ENTERA, aqui, antes de que
entren.** Su insercion es de la vuelta siguiente, despues de que mi fase ciega barra y lea lo que dejes y la `ACTA 72` lo adjudique.

**PUEDES LANZAR BARRIDOS DE FONDO, CINCO A LA VEZ COMO MUCHO, PERO NINGUNO VIVO AL CERRAR TU TURNO**: los recoges todos dentro,
vigilandolos si tardan. **Si no te caben, no los lances: lo dices en el reporte con los que faltan.** El `23` sep tres asientos
cerraron diciendo que esperaban un trabajo de fondo, y ninguno volvio. **Y NINGUN `insertar`**, ni en primer plano ni de fondo.

**EL RELOJ, MEDIDO, Y NO ES UN TECHO: ES LO QUE COSTO.** El barrido de la `71`, cinco fichas a la vez, por ficha y ordenado por
valor:

    $ grep "rc=" .v71ext/barrido.log | sed 's/.*segundos=//' | sort -n | sed -n '1p;$p'
    578
    1640

## LA CLASE Y EL LIBRO, DICHOS POR EL INSTRUMENTO

    $ python scripts/deuda.py --clase 73
    LIBRE
      van 4 de 5 desde la ultima de saneamiento (la 69), con 55 deuda(s) esperando

    $ python forja.py tablero --puedo grove_high_output
    LINEA 'serial', LIBRO 'grove_high_output': SI
      'grove_high_output' esta COSECHADO y sin dueño: su trabajo ya llego a esta rama, asi que se continua desde el capitulo siguiente al ultimo minado (cap_18), citando su frontera. D.50.

**El orden de la campania es Grove, Gerber, Marquet** (`PARALELO.md` seccion `8` punto `4`). **La frase de *continuar desde
`cap_18`* es de extraccion y no aplica: Grove esta minado entero**, y lo que se hace es insertar su bandeja por capitulo (`d028`).

---

## TAREA 1: **REGISTROS DE LA `ACTA 71`**

En una tabla corta y sin reabrir el argumento (`D.47`):

| que | donde |
|---|---|
| **Las filas de `.v71ext/orden.txt` dentro, una por vez, sin solape y en su orden**; sus lineas de veredicto iguales letra a letra a las preparadas, sobre los pares del barrido del auditor, con sus seniales y sus clases selladas; sus aristas iguales par a par; ningun nodo viejo cambia | `ACTA 71` `71.3` |
| **Tus seis discutibles se sostienen**, `D72.1` a `D72.6` | `71.5` |
| **La muestra de los SANO se sostiene entera**; lo que entro lleva cero PUENTE en los seis capitulos | `71.5`, `71.4` |
| **Cero caidas tuyas, ni de prosa**, y `R5` cumplido | `71.2`, `71.0` |
| **Una caida del auditor**: `R8` roto en su encargo de la `72`, su racha `AUDITOR` sube, y su remedio se escala | `71.9`, `71.11` |

## TAREA 2: **LA FIDELIDAD ENTERA DE LAS FICHAS QUE QUEDAN** (`D.30`, `D.58`)

Son **todas las fichas de `cuarentena/grove_high_output/`**, las de `cap_15`, `cap_16` y `cap_17`; **cuantas por capitulo y cuantos
pasos trae cada una estan en la `ACTA 71` `71.1`, bloque de `.v72aud/normal/siete.py`**, y tu primera medida es volver a correrlo.
Todo en tu carpeta `.v73ext/`, **con copias de instrumentos que ya existen y la ruta cambiada**, no con instrumentos nuevos (`7.F`):

1. **Cada paso contra su capitulo de `fuentes/grove_high_output/` leido entero**, marcado `T` o `P` con su linea, en un fichero con
   una fila por paso como `.v71ext/fidelidad.tsv` (la clausula reescrita CUENTA como `P`, `ACTA 62` `62.5`), y sus citas comprobadas
   con una copia de `.v71ext/citas.sh`. **`d078`**: el solape de los pasos `3` y `5` de `responder_primer_aviso_renuncia_subordinado`
   es una repeticion del propio libro en una misma linea; si lo lees igual, dilo con la linea delante.
2. **Todo PUENTE se corrige en la ficha de la bandeja por correccion declarada, con el texto viejo dentro, ANTES del barrido**: una
   ficha que cambia despues de su barrido tiene un barrido que ya no es suyo (`d031`).
3. **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo, tres filas**, por una copia de `.v71ext/contar_fidelidad.py`, **y el
   peor capitulo nombrado** (`8.2`). **Si uno pasa del `10` por ciento, ese capitulo se relee entero antes de seguir** (`D.58`).
4. **Marca discutible todo paso en que dudes, al escribirlo.**

## TAREA 3: **EL BARRIDO, SOBRE LAS FICHAS YA CORREGIDAS**

Contra **GRAFO MAS BANDEJAS** (`D.38.4`), con copias de `.v71ext/barrido_uno.py` y `.v71ext/barrer.sh` con la lista de las fichas y
la ruta `.v73ext/`: **cinco a la vez como mucho, un log con su `INICIO` y su `TODOS TERMINADOS`, y todas recogidas dentro de tu
turno.** **La poblacion al abrir, con su reparto por sede, esta en la `ACTA 71` `71.1`, bloque de `.v70aud/poblacion.py`**: vuelve a
correrlo al abrir y pega su salida. **Una tabla por candidato de sus vecinos**, con una copia de `.v71ext/tabla_vecinos.py`.

## TAREA 4: **LOS VEREDICTOS, LAS ARISTAS Y EL ORDEN**

1. **Los veredictos listos, uno por vecino**, en el formato de `--veredicto` y con un bloque por candidato como
   `.v71ext/veredictos_listos.txt`: **leidos con los pasos de los dos delante** (`python .v64aud/pasos.py <a> <b>`) y por la vara
   `6.1`, y solo esa. **Y comprobado por instrumento que cada vecino del barrido tiene su linea y cada linea su vecino**, con una
   copia de `.v71ext/comprobar_veredictos.py`.
2. **Las aristas por lectura** (`D.29`, `D.53`), en un fichero como `.v71ext/aristas_lectura.txt`, con su tramo de madre y de hijo
   y su linea del libro, **mirando tambien madres que ya viven en el grafo**. **Hay lectura previa de la casa sobre `cap_17` y la
   citas**: la `ACTA 60` `60.5` adjudico **`CONTINUA`** los tres pares de su cadena (`priorizar_lista_entrenamiento_subordinados`
   madre de `desarrollar_primer_curso_entrenamiento` y de `pedir_critica_anonima_curso_entrenamiento_dictado`, y
   `desarrollar_primer_curso_entrenamiento` madre de `pedir_critica_anonima_curso_entrenamiento_dictado`). **Si tu lectura de hoy
   difiere, no la fuerces: la marcas discutible y la dices con los pasos delante.** Y en `cap_15`, mira el par
   `responder_primer_aviso_renuncia_subordinado` y `gestionar_retencion_subordinado_valioso_renuncia` por la vara `6.1`, con direccion.
3. **El orden de insercion**, con una copia de `.v71ext/orden.py`: **madre antes que hijo, `D.36`, y las comprobaciones en cero.**

**Si no te cabe todo, parte por capitulo y por donde se pueda auditar**: `cap_17` entero antes que los demas, porque es el que trae
aristas adjudicadas, y dentro de cada uno la fidelidad antes que el barrido y el barrido antes que los veredictos. **Lo que no
hagas lo dices con su fila vacia**, y la vuelta siguiente empieza por ahi.

## TAREA 5: **EL CIERRE**

- **El censo antes y despues**: nodos, veredictos, pares mutuos, bandeja de Grove e insertados, con una copia de `.v72ext/censo.sh`.
  **No entra nada**: al abrir son los de la `ACTA 71` `71.1`, y al cerrar tienen que ser los mismos.
- **`PASOS INVENTADOS POR CAPITULO`, tres filas**, que son **preparacion y no entrada**.
- **La huella de las fichas preparadas**, con una copia de `.v71ext/pasos_y_huellas.py` con la lista de esta vuelta, corrida
  despues del ultimo cambio de ficha y pegada: es contra lo que la vuelta de insercion comprobara que entra lo que se leyo.
- **`D.61`**: cada discutible ejecutado o cerrado. Ninguno abierto.
- **`R5`** en cada bloque `$` de tu tramo, **medido con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera
  cambiada a la `73`**, y pegado.
- `python forja.py gate`, `python forja.py guiones`, `python tests/test_aceptacion.py` y `python scripts/cerrar_reporte.py`,
  **pegados**. **El cierre estricto tiene que salir en verde: cualquier rojo es tuyo.**
- Commitea `docs/loop/`, las fichas corregidas de la bandeja y tu carpeta `.v73ext/`. **Si nada te obliga a parar, no escribas
  `PARA_ALEXIS.md`.**

---

## LO QUE NO HACES

- **NO INSERTAS NINGUNA FICHA**, y **NO TERMINAS TU TURNO CON NADA VIVO**, ni un barrido.
- **NO TOCAS `cuarentena/gerber_emyth/` NI `cuarentena/marquet_turn_the_ship/`**: van despues de Grove, en ese orden.
- **NO TOCAS `src/`, `scripts/`, el banco, el arnes ni los protocolos** (`7.F`, `D.55`), **ni `APERTURA_CIEGA.md`**. Los procesos
  del fundador que veas vivos en otra copia no son tuyos: ni los tocas ni los esperas.
- **NO REORDENAS LA COLA A MANO.**
- **NO ABRES NINGUN LIBRO.** Lo que le falta al mundo `11` lo dice el tablero, pegado en la `ACTA 71` `71.10`.

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No
adivines.**
