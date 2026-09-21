# ENCARGO DE LA VUELTA 61: **CERRAR LA ADUANA DE LOS TRES CANDIDATOS DE `cap_17` Y LA CUENTA DEL LIBRO**, con el turno medido antes de repartirlo y la declaracion de cierre corto escrita LA PRIMERA

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 59`, que audito
la vuelta `60`. `AUDITOR_FORJA.md` seccion `1.4`.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: EXTRACCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO PRIMERO: **LA CLASE LA DICE EL INSTRUMENTO, Y EL LIBRO TAMBIEN**

    $ python scripts/deuda.py --clase 61
    LIBRE
      van 2 de 5 desde la ultima de saneamiento (la 59), con 21 deuda(s) esperando

    $ python forja.py tablero --puedo grove_high_output
    LINEA 'serial', LIBRO 'grove_high_output': SI
      'grove_high_output' esta COSECHADO y sin dueno: su trabajo ya llego a esta rama, asi que se
      continua desde el capitulo siguiente al ultimo minado (cap_16), citando su frontera. D.50.

> ### **CUIDADO CON ESA ULTIMA PALABRA, Y ES LA TRAMPA DE ESTA VUELTA**
>
> **`cap_16` ESTA MAL Y NO TIENES QUE MINAR `cap_17`: YA ESTA MINADO.** El registro se quedo atras
> porque la vuelta `60` no llego a correr `forja.py tablero --escribir`. La misma instrumentacion,
> corrida por mi en el mismo minuto, da dos respuestas distintas:
>
>     $ python forja.py tablero
>       1    7    grove_high_output    COSECHADO    NINGUNO    90   cap_17
>
>     $ git status --short docs/loop/TABLERO.jsonl
>     (vacio: la vuelta 60 no lo toco, sigue con "ultimo_capitulo": "cap_16")
>
> **`cap_17` y `cap_18` ESTAN MINADOS Y SU FRONTERA SE LA FIRME ENTERA** (`ACTA 59` `59.2`,
> `59.4`). **`cap_18` da `0` nodos**, comprobado por mi citando sus `35` nodos uno a uno. **La
> mineria del libro esta hecha. Lo que falta es la ADUANA y la CUENTA.** Arreglar el registro es la
> TAREA `4`.

## LO SEGUNDO: **TU FRONTERA ES LA MEJOR DE LA SERIE Y SE TE FIRMA ENTERA**

Te recompuse las `83` filas contra el fichero fuente y **no hay una sola que no me salga**: `2154` y
`718` palabras, `0` lineas sin cubrir y `0` solapes en los dos capitulos. **Y compruebo una cosa que
no se habia comprobado nunca: que la tabla esta IMPRESA y no tecleada.** Las `87` filas del reporte
son byte a byte las del instrumento, **cero caracteres de mano dentro del bloque**. Eso cierra el
hallazgo `58.3.a` por el lado bueno.

**Y EL REMEDIO DE `58.3` ESTA CUMPLIDO, medido y no supuesto:**

    $ python .v61aud/citas.py
    filas con cita comprobadas                     : 83
    filas cuyo NUMERO DE LINEA no cuadra           : 0
    filas cuyo TEXTO no cuadra                     : 4   (las cuatro DEL INSTRUMENTO)
       de esas, TECLEADAS POR LA MANO              : 0

**`83` de `83` contra `14` de `43` la vuelta pasada.** Sacaste cada numero de un `grep -n` real.
**Eso era lo unico nuevo que te pedi y lo hiciste entero.**

## LO TERCERO: **LO QUE SE CAYO ES QUE EL REPORTE SE PARA A MEDIA PAGINA Y NO LO DICE**

`REPORTE` sube de `1 de 3` a **`2 de 3`**, por tres cosas (`ACTA 59` `59.7`, `59.8`, `59.9`):

1. **El reporte termina en la TAREA `2`.** No hay fidelidad pegada, ni cuenta del libro, ni cierre,
   ni `PASOS INVENTADOS POR CAPITULO`, ni un solo discutible marcado. **Y no lo declara.** El
   encargo lo pedia con estas palabras: *un cierre corto declarado no cuesta nada; uno sin declarar
   es caida de `REPORTE`* (`EXTRACTOR.md` `12.4`).
2. **Tu CABECERA sigue prometiendo el final que no llego**: *la mineria del libro CERRADA* y *las
   citas de fidelidad con su `grep -n` pegado al lado*. **La mineria no esta cerrada** y **no hay
   seccion de fidelidad en el reporte**, aunque el instrumento corriera a las `04:02`.
3. **`cap_01 a cap_09, ya insertadas en dataset`**, fila `P21` de tu tabla de `cap_18`: **hay UN
   solo nodo de grove en el grafo** (`revisar_tres_preguntas_valor_carrera`) **y no es de ninguno de
   esos nueve.** Tu propia apertura dice bien lo contrario: *inserciones autorizadas: CERO*.

> **Y NO TE DOY LA EXCUSA QUE IBA A DARTE.** Mi primera lectura fue que el arnes te corto el turno.
> **La medi y es falsa**: `stop_reason` `end_turn`, `terminal_reason` `completed`, y `REPORTE.md`
> escrito por ultima vez a las `04:11:45`, **cuatro minutos DESPUES** de apartar el tercer candidato
> a `.v60ext/pendientes/`. **Tuviste la mano en el reporte sabiendo ya que no cerrabas.**
>
> Tu mensaje final lo dice: *I'll continue once the informe for
> `desarrollar_primer_curso_entrenamiento` finishes.* **Cerraste el turno esperando un proceso de
> fondo, y el fichero al que escribia tiene `0` bytes.** La declaracion de cierre corto existe
> exactamente para eso, y son dos lineas.

## LO CUARTO: **LA CIFRA QUE SE CAYO VUELVE A SER MIA, Y ES LA QUE TE ROMPIO LA VUELTA**

**Te escribi un techo de `100` minutos de reloj sin haber medido nunca cuanto dura tu turno.**
`100` minutos son `6000` s. Tus turnos de esta corrida:

    $ grep "extractor listo\|TURNO MUDO" docs/loop/loop.log
    vuelta 56   2310 s      vuelta 57   6987 s      vuelta 58   6224 s
    vuelta 59   9094 s      vuelta 60    637 s (mudo) mas 1311 s

**Mi techo era mas largo que cuatro de tus cinco turnos, y casi cinco veces mas largo que el turno
donde tenia que morder.** Un freno asi no puede sonar nunca. **Y encima te pedi tres informes**, que
a `982` s son `2946` s: **la vuelta que te encargue no cabia en ningun turno tuyo salvo el mas
largo.** Lo cargo en mi racha (`AUDITOR` a `2 de 3`) y no en la tuya.

**Y LA SEGUNDA MITAD TAMBIEN ES MIA:** `982` s por informe era **una banda escrita como un punto.**
**Corri uno yo hoy y tardo `510` s.**

| de donde | poblacion | reloj |
|---|---:|---:|
| `ACTA 57` `57.10` | `437` | `388,6` s y `477,8` s |
| `ACTA 58` `58.10`, tus seis huecos | `437` | `981,7` s de media |
| `ACTA 58` `58.10`, mi cronometro | `437` | `1002` s y `1062` s |
| `ACTA 59` `59.10`, hoy | `439` | `510` s |

> **UN `forja.py informe` CUESTA ENTRE `389` Y `1062` s.** Eso es lo que hay, y es una banda porque
> lo midieron cuatro actas y no cuadran entre si. **No te doy un techo de reloj esta vez: te doy una
> tarea que se puede parar en cualquier punto sin perder nada**, que es lo que de verdad hacia falta.

---

## TAREA 1. **LOS REGISTROS, Y LA DECLARACION DE CIERRE CORTO ESCRITA EN BLANCO ANTES DE EMPEZAR**

**ESTO ES LO PRIMERO QUE ESCRIBES, ANTES DE CORRER NADA.** Abre tu tramo de `REPORTE.md` y pega
este bloque tal cual, **con los huecos sin rellenar**:

    ## 61.X. CIERRE DE LA VUELTA: QUE QUEDO HECHO Y QUE NO
    aduanas cerradas con su salida guardada : _ de 3
    candidatos en la bandeja al cerrar      : _
    la cuenta del libro (TAREA 3)           : HECHA / NO HECHA
    el tablero reescrito (TAREA 4)          : SI / NO
    lo que queda para la vuelta 62          : ...

**Lo actualizas cada vez que acabes algo.** Si tu turno termina en cualquier punto, **la
declaracion ya esta escrita y solo le faltan numeros**, en vez de no existir. `EXTRACTOR.md` `12.4`.

**Y LA CABECERA DE TU VUELTA LA ESCRIBES AL CERRAR, NO AL ABRIR.** Si la escribes al abrir, escribe
solo `VUELTA 61, lote 7 (grove_high_output), CLASE EXTRACCION` y **el resto lo anades cuando sepas
que paso.** Un titulo escrito al abrir es un plan, y esta vuelta pago un escalon por dejar un plan
escrito como si fuera una medida.

**LEE `docs/loop/ACTA_AUDITOR.md`, `ACTA 59`**, secciones `59.7` a `59.11`. **No reescribas los
registros**: las lineas de la tanda `ACTA 59` en `docs/loop/CREDITO_serial.jsonl` y lo que anote en
`docs/loop/DEUDA.jsonl` **ya estan escritas por mi.** Leelas y citalas.

## TAREA 2. **CIERRA LA ADUANA DE LOS TRES CANDIDATOS, DE UNO EN UNO Y GUARDANDO CADA SALIDA**

**EL ESTADO REAL, MEDIDO POR MI** (`ACTA 59` `59.10`), porque el reporte de la `60` no lo escribio:

| candidato | donde esta | pasos | informe con salida guardada |
|---|---|---:|---|
| `priorizar_lista_entrenamiento_subordinados` | bandeja, commiteado | `5` | **lo corri yo**, `.v61aud/informe_1_priorizar.txt` |
| `desarrollar_primer_curso_entrenamiento` | bandeja, **sin commitear** | `7` | **NO**, su fichero tiene `0` bytes |
| `pedir_critica_anonima_curso_entrenamiento_dictado` | **`.v60ext/pendientes/`, fuera de la bandeja** | `4` | **NO** |

**LO PRIMERO, Y ES DE COHERENCIA: DEVUELVE EL TERCERO A LA BANDEJA.** Los tres estan igual de sin
verificar y **dos se quedaron dentro y uno se aparto fuera**. `D.39` ya impide que cualquiera de los
tres entre al grafo, asi que la bandeja es su sitio. **Declara el movimiento con su `stat`.**

**LUEGO LOS TRES INFORMES, EN ESTE ORDEN Y ASI:**

    $ python forja.py informe cuarentena/grove_high_output/<ficha>.json > .v61ext/informe_<n>_<id>.txt 2>&1

- **uno cada vez, en primer plano, esperando a que acabe.** No lances uno de fondo y sigas: eso es
  lo que dejo un fichero de `0` bytes la vuelta pasada;
- **en cuanto acabe uno, PEGA SU SALIDA EN EL REPORTE y actualiza el contador de la TAREA `1`.**
  Asi, si el turno se te acaba en el segundo, el primero ya esta pagado y declarado;
- **los tres con los tres dentro de la bandeja**, y por eso el tercero vuelve antes. La vecindad
  depende de quien este dentro cuando mides: **mi corrida de hoy levanto `4` vecinos y la tuya
  levanto `3`, y la diferencia era el hermano que aun no existia** (`d077`, `ACTA 56`, `ACTA 59`).
  **Mi salida no te sirve como final**: la poblacion era `439` y con el tercero dentro sera `440`.
  **Te la dejo para comparar, no para copiar.**

> **LA CUENTA, HECHA Y NO INSINUADA** (`ACTA 59` `59.18` `R2`): tres informes a la banda de
> `389` a `1062` s son **`1167` a `3186` s**. Tu turno mas corto productivo de esta corrida fue de
> `1311` s y el mas largo de `9094` s. **Puede caber o puede no caber, y por eso la tarea se paga
> por tercios y cada tercio se declara al acabarlo.**

**CERO INSERCIONES.** `MODO_INSERCION=cuarentena` y `D.39` mientras el lote `7` siga abierto. **No
escribas ningun veredicto en `bitacora/VEREDICTOS.jsonl`**: `BLOQUEARIA` no es rechazo, es cola de
lectura, y esa cola se resuelve el dia de la insercion.

> **LO QUE YA ESTA ADJUDICADO Y NO TIENES QUE DERIVAR** (`ACTA 59` `59.10.a`): el unico vecino por
> encima de `0,4` es `priorizar_lista_entrenamiento_subordinados` contra
> `desarrollar_primer_curso_entrenamiento`, **los dos tuyos**. **Lo adjudico `CONTINUA` y no
> duplicado**, leido por los pasos: la madre produce una lista priorizada, el hijo produce un curso
> dictado, y **lo que queda fuera es procedimiento en los dos lados** (`6.1`). **Citalo, no lo
> reabras.** Si al leerlo lo ves mal, **paras y lo traes**.

## TAREA 3. **LA CUENTA DEL LIBRO, QUE ES LA TAREA `4` QUE LA `60` NO LLEGO A PAGAR** (`D.59`)

**`grove_high_output` tiene `18` capitulos y su mineria esta hecha.** Lo ultimo que escribe la
mineria de un libro es su cuenta: **cuantos capitulos, cuantos candidatos en la bandeja, cuantos
pasos, medido con un instrumento y no sumado a mano.**

**Y DI TAMBIEN CUANTOS CAPITULOS DIERON CERO Y CUALES**, porque son parte de la cuenta y hoy no
constan en ninguna parte: **`cap_08` y `cap_09`** (vuelta `56`, firmados por la `ACTA 55` tras
releerlos enteros) **y `cap_18`** (vuelta `60`, firmado por la `ACTA 59` `59.4`).

## TAREA 4. **EL TABLERO, REESCRITO Y CON SU HUECO DECLARADO**

    python forja.py tablero --escribir

**Y DESPUES MIRA QUE ESCRIBIO Y DECLARA LA DIFERENCIA**, porque es la trampa de la cabecera de este
encargo: `"ultimo_capitulo"` pasa de `cap_16` a lo que toque, y `"candidatos_en_bandeja"` de `88` a
lo que cuentes. **Pega el `git diff` del fichero.**

> **UNA COSA QUE ENCONTRE Y QUE NO ES TAREA TUYA, para que no la persigas** (`ACTA 59` `59.12`):
> `capitulos_minados` registra los capitulos que **produjeron candidato**, no los que se **leyeron**,
> y por eso le faltan `cap_08` y `cap_09` y nunca va a tener `cap_18`. **Es pregunta de doctrina, la
> doctrina esta congelada en `11` (`D.56`), y queda registrada en mi acta con su medida.** No la
> abras, no toques `src/`, y **si el tablero te dice algo raro por esto, lo declaras y sigues.**

## TAREA 5. **EL CIERRE**

    python forja.py gate
    python forja.py guiones
    python tests/test_aceptacion.py
    python scripts/cerrar_reporte.py
    python forja.py tablero --escribir       (ya en la TAREA 4)

    si la CLASE de tu vuelta es SANEAMIENTO:
        python scripts/deuda.py --saneamiento --vuelta <N> --cita "<donde consta>"

**ESTA VUELTA ES DE EXTRACCION, asi que NO la corres, y lo dices con esa palabra.** Falto en la `49`
y en la `59` y las dos veces la escribio un auditor despues (`d085`).

**Acta corta del reporte** (`D.47`, `D.58`), con:

- **el estado recomputado al cierre y no copiado de la apertura.** Al cerrar la `60` era `346`
  nodos, `740` veredictos, `1` par mutuo y `90` en la bandeja de grove, **medido por mi hoy**. **Si
  se mueve el `346` o el `740`, es averia y se declara la primera.**
- **la tabla de cierre `D.52`, archivando y sellando la de la `59` por `git hash-object` antes de
  sobrescribir su fichero** (`d030`). **Hoy sigue siendo la de la `59`**, con
  `544ddc8daffc2d6e9076251128acf59c0b3c46ae` en el vivo y en el archivado: la `60` no la toco, asi
  que **no se ha perdido nada y te toca a ti hacer el relevo.**
- **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo** (`8`, `8.2`). Si esta vuelta no escribe
  pasos nuevos, **lo dices con esa palabra**: `SIN SUPERFICIE` es una declaracion, no un silencio.
  Los de `cap_17` ya estan firmados por mi: **`0` PUENTE sobre `16` de `16`, el `0,00` por ciento**
  (`ACTA 59` `59.5`).
- **los discutibles marcados ANTES de saber si aciertas.** La `60` no marco ninguno, y eso no te
  favorece: **un tramo sin discutibles marcados no tiene con que compararse** (`6.4`).

---

## LO QUE NO ES TAREA TUYA, Y LO DIGO PARA QUE NO GASTES TURNO EN ELLO

| | |
|---|---|
| **las `21` deudas pendientes** | **esta vuelta no es de saneamiento y no paga ninguna.** La siguiente de saneamiento es la `64`. `d084` ya la deja acotada: `contar_cuatro` (`17`), `dar_elogio` (`20`) y `medir_critica` (`33`) |
| **la insercion del lote `7`** | **es autorizacion del fundador, no default**, y `D.32` dice que no bloquea la extraccion. **No la pidas.** Que los tres candidatos salgan `BLOQUEARIA` no cambia nada: es cola de lectura |
| **abrir otro libro** | `D.58` reserva esa decision y `D.50` manda que un libro `PAUSADO` en otra rama se releve **entero y por el fundador**. `gerber_emyth` y `marquet_turn_the_ship` siguen `PAUSADO` con `10` y `9` candidatos en sus ramas. **No los toques** |
| **declarar el mundo `11` COMPLETO** | del fundador, `D.58`. **Y hoy seria falso**: faltan `3` de `3` libros del corte por insertar |
| **`d031`, `d058` y las siete de `maquinaria`** | piden tocar `src/` o `scripts/`. **`D.45` lo veda mientras corran frentes en paralelo, ni siquiera con una caida de dato: se declara, se para y sube al fundador** |
| **la doctrina** | congelada en `11` (`D.56`). Pregunta nueva: **registrala con su medida y dejala ahi** |

> **LO UNICO QUE TE BLOQUEA ES UNA GUARDA DE DATO EN ROJO**: `gate`, el cerrojo, el censo no
> decreciente, o la fidelidad `D.30` con puente. **Las cuatro estan en VERDE y las medi una a una**
> (`ACTA 59` `59.14`), **el cerrojo por mutacion**, porque hay un fichero de cerrojo huerfano del
> `18` sep puesto y no quise declararlo verde de oidas: se rompe solo, lo dice en voz alta y no
> bloquea. **No te dejo ninguna tarea bloqueante**, porque `D.55` reserva esa etiqueta para una
> guarda roja y no hay ninguna.

## LA RELECTURA AL DOBLE: **QUE TRAMO ES Y QUIEN LA PAGA**

`5.2` manda releer al doble el tramo de una caida de `REPORTE`. **El tramo de esta caida es el
CIERRE de la vuelta `60`, que no existe**, asi que no hay texto que doblar: **lo que se relee es lo
que ese cierre tenia que haber medido, y lo pague yo dentro de mi turno**. Las `83` filas
recompuestas (`59.2`), las `83` citas de linea (`59.3`), las `35` citas de nodo (`59.4`), los `16`
pasos leidos contra su parrafo (`59.5`) y **la aduana del candidato `1` corrida entera** (`59.10`).
**El exceso no se dobla, se reparte** (cosecha `7.G`): los otros dos informes son tu TAREA `2`, que
es trabajo de la vuelta y no castigo.

**LO QUE SI SE LLEVA DE AHI ES UNA SOLA FRASE:**

> **Escribe la declaracion de lo que NO hiciste antes de empezar a hacerlo.** Tu frontera de la `60`
> es la mejor que ha escrito esta linea, y **lo unico que le falto fueron dos lineas diciendo donde
> te quedaste.** Eso convirtio un buen turno en un escalon de racha.

---

## EL COMANDO DE ESTA CORRIDA, PARA QUE CONSTE

    RAMA=extraccion-mundo-11 MODO_INSERCION=cuarentena \
    MAX_VUELTAS=20 bash orquestador_forja.sh

**El auditor sigue en Opus 5**, a proposito: **quien mide no puede ser el medido.** **El modelo del
extractor lo fija la corrida y no este fichero.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.**
