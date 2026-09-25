# ENCARGO DE LA VUELTA 69: **SANEAMIENTO QUE DEJA `cap_05` Y `cap_06` LISTOS PARA ENTRAR EN LA `70` SIN UNA PREGUNTA ABIERTA: LA RELECTURA CONJUNTA DE LA CABEZA DE LAS TRES CLASES, `d053` Y `d056`. SIN INSERTAR NADA**

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 67`, que audito la vuelta `68`.
`AUDITOR_FORJA.md` seccion `1.4`.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: SANEAMIENTO**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **LA REGLA DEL TURNO**

**En esta vuelta no se corre `python forja.py insertar` ni una vez**, ni se escribe un veredicto en `bitacora/` ni una arista en
el dataset. Lo que cambies vive en `.v68ext/` (por correccion declarada) o en tu carpeta `.v69ext/`, y en las fichas de la
bandeja **solo si `d053` las parte** (TAREA 3).

> **NINGUN PROCESO TUYO VIVE CUANDO TU TURNO TERMINA.** Si lanzas algo en paralelo (un barrido, cinco a la vez como mucho), lo
> recoges dentro del turno, vigilandolo si tarda. **Si algo no cabe, NO lo lances: dilo en el reporte con lo que falta.** El
> `23` sep tres asientos cerraron diciendo que esperaban un trabajo de fondo, y ninguno volvio.

**EL RELOJ, MEDIDO Y NO TECHO:** el barrido de los `20` de la `68`, cinco a la vez, tardo `2` h `54` min (`68.3.2`).

## LA CLASE Y EL LIBRO, DICHOS POR EL INSTRUMENTO

    $ python scripts/deuda.py --clase 69
    SANEAMIENTO
      han pasado 5 vuelta(s) desde la ultima de saneamiento (la 64) y la cadencia es 5, con 58 deuda(s) pendientes

    $ python forja.py tablero --puedo grove_high_output
    LINEA 'serial', LIBRO 'grove_high_output': SI
      'grove_high_output' esta COSECHADO y sin dueño: su trabajo ya llego a esta rama, asi que se continua desde el capitulo siguiente al ultimo minado (cap_18), citando su frontera. D.50.

**Las `58` son las `57` de la apertura de la `68` mas `d170`, que anote yo** (la arista `EN ESPERA` de tu `D68.15`). Grove esta
minado entero: lo que le queda es insertar. **Esta vuelta se usa para pagar justo lo que frena la insercion de `cap_05` y
`cap_06`**, y la insercion vuelve en la `70` con todo decidido.

---

## TAREA 1: **REGISTROS DE LA `ACTA 67`**

En una tabla corta y sin reabrir el argumento (`D.47`):

| que | donde |
|---|---|
| **Las filas `21` y `22` dentro y firmadas**: `9` lineas iguales a las preparadas y a la lectura ciega del auditor, las `2` aristas las esperadas, sin solape; **`cap_04` entra entero en `0` de `156`** | `ACTA 67` `67.3`, `67.5` |
| **`cap_05` `0` de `84` y `cap_06` `0` de `62`, firmados**: tus `D68.3` a `D68.6` se sostienen y las cuatro dudas del auditor quedan `T` | `67.4.a` |
| **Barrido identico al del auditor, `118` de `118` pares, y `66` de `70` clases iguales**; tus `D68.8` a `D68.14` se sostienen y tu orden queda como esta | `67.4.b`, `67.4.c`, `67.4.e` |
| **`agrupar_tareas` a `infundir`, `SOSTENGO`: gana tu lectura** dentro de la duda del auditor | `67.4.d` |
| **Una caida de `REPORTE` que no acumula**: en `68.3.4` los `NO SOSTENGO` son `5` filas y `7` pares, no *seis* | `67.2` |
| **`R5` cumplido**, cuatro rachas en cero y la del auditor en `1 de 3` por una cifra suya | `67.0`, `67.7`, `67.9` |

## TAREA 2: **LA RELECTURA CONJUNTA** (`AUDITOR_FORJA.md` `1.3`), **ANTES DE TOCAR NADA MAS**

**Dos discrepancias, las dos dentro de tu marcado**, con el caso del auditor escrito en la `ACTA 67` `67.4.d`:

| | tu lectura | la del auditor |
|---|---|---|
| **`D68.7`** | `usar_tres_clases_reunion_proceso` madre de ocho piezas del uno a uno: las `8` lineas `CONTINUA` de `.v68ext/veredictos_listos.txt` (lineas `20` a `23`, `31`, `39`, `49` y `57`) y las cuatro filas `SOSTENGO` de la cabeza en `.v68ext/aristas_lectura.txt` | `SANO` y `NO SOSTENGO` en los ocho: la madre solo produce saber que hay tres clases y como se llaman; **ninguna de las ocho condiciones parte de eso**, cada una parte de su situacion con el uno a uno en marcha y contesta su propia pregunta del libro. Es la figura de `D67.3`, no la de `C1`. Y `D.37` ya dijo que ninguna parte es nodo |
| **`D68.15`** | `elegir_estilo_direccion_madurez_relevante_tarea` madre de `fijar_frecuencia_reunion_individual_madurez_tarea`, `EN ESPERA` | `NO`: el paso `5` del hijo es un *Cuenta con* que nombra el principio; ningun paso usa el estilo elegido que la madre produce |

1. **Lee los cinco puntos de su caso** (`67.4.d`, *MI CASO EN `D68.7`*) **con los pasos de los dos delante**, y **escribe en tu
   reporte, par por par, tu lectura contra su evidencia**, con la linea del libro de cada lado. **Decides tu con la vara `6.1` y lo
   declaras; no te pido que le des la razon.** Si mantienes tu lectura, di que punto de su caso no se sostiene y por que.
2. **Si cambias alguna linea o fila**, por correccion declarada y sin borrar: la vieja queda encima como comentario
   `# vuelta 69`, como hizo la `67` con las de la `66`, en `.v68ext/veredictos_listos.txt` y `.v68ext/aristas_lectura.txt`.
   **Las lineas de un mismo par, leido desde sus dos lados, cambian juntas.**
3. **Despues, con copias de `.v68ext/comprobar_veredictos.py` y `.v68ext/orden.py` en `.v69ext/`** (ruta de salida cambiada):
   cero vecinos sin linea, cero lineas sin vecino, **las tres comprobaciones del orden en cero** y **la cuenta de aristas
   esperadas en la `70`, por instrumento**. Si la conjunta no cambia nada, correlos igual y dilo.
4. **`D68.15` no toca a la `70`**: lo que decidas lo escribes en el comentario `EN ESPERA` de `.v68ext/aristas_lectura.txt`, con
   las dos lecturas, y `d170` lo guarda para la vuelta que inserte `cap_13`. **No pagues `d170`**: se paga cuando entre la madre.

## TAREA 3: **`d053`: SE PARTE O NO `fijar_duracion_lugar_reunion_individual`**

**La deuda, con su letra:** *su tramo contesta a DOS preguntas del libro: L37 a How long should a one-on-one meeting last y L39 a
Where should a one-on-one take place. El corte esta escrito de antemano entre el paso 4 y el paso 5 ... se decide el dia de la
insercion*. **La insercion es la `70`, asi que se decide aqui.**

1. **Lee `cap_05` L37 y L39 con la ficha delante y decide por la vara de `EXTRACTOR.md` `9.1`**, la misma con la que se
   recorto el resto de `cap_05`: si cada mitad es un nodo por si sola (su linea normativa y sus pasos) o si una de las dos no
   pasa la vara sin la otra. **Escribelo en tu reporte con la linea de cada lado, y marca discutible si dudas.**
2. **SI NO SE PARTE:** pagas `d053` con tu razon y nada mas cambia.
3. **SI SE PARTE:** las dos fichas nuevas en la bandeja, con la vieja dentro por correccion declarada y **los mismos pasos**, sin
   reescribir ninguno (su fidelidad ya esta firmada `T`, `ACTA 67` `67.4.a`); **y como una ficha nueva cambia la poblacion de
   todas**, el barrido de la tanda entera (`21` fichas) otra vez, con copias de `.v68ext/barrido_uno.py` y `.v68ext/barrer.sh` en
   `.v69ext/`, cinco a la vez y recogido dentro del turno; los veredictos de los pares nuevos, uno por vecino, leidos con los
   pasos de los dos delante; la comprobacion y el orden de la TAREA 2 corridos sobre ese barrido; y la huella de las `21`.
   **Si el barrido no te cabe, NO lo lances**: deja la ficha sin partir, no pagues `d053`, y lo dices con su fila vacia.

## TAREA 4: **`d056`: LA COLA DE LECTURA DE LA TANDA `52`**

**La deuda:** *los informes corren de uno en uno ... SE COBRA EL DIA DE LA INSERCION ... se recorre la cola sobre la poblacion de
ese dia y se veredicta lo que falte*. **La `68` hizo ese recorrido** sobre poblacion `479` con las `20` fichas dentro: `118` pares y
`118` lineas, cero vecinos sin linea (`68.3.3`, reproducido identico en la `ACTA 67` `67.1`). **Paga `d056` citandolo**, con la
salida de tu copia de `comprobar_veredictos.py` de la TAREA 2 pegada debajo, **y di en una linea que queda para la `70`**: la
aduana de `insertar` vuelve a medir sobre la poblacion de ese dia, y lo que levante sin linea se lee en el acto (`d031`).

## TAREA 5: **EL CIERRE**

- **Declara la vuelta de saneamiento en el registro** (`d085`):

      python scripts/deuda.py --saneamiento --vuelta 69

- **Paga solo lo que pagaste**, con `python scripts/deuda.py --pagar <id> --vuelta 69 --como "..."`: `d053` si esta decidida y,
  si se partio, con las `21` fichas barridas y veredictadas; `d056` si la TAREA 4 esta pegada. **Lo que quede a medias se queda
  pendiente y se dice.**
- **La cuenta de aristas esperadas en la `70` y la huella de las fichas preparadas**, las dos por instrumento, corridas despues
  del ultimo cambio: la huella con una copia de `.v68ext/pasos_y_huellas.py` en `.v69ext/`.
- **`PASOS INVENTADOS POR CAPITULO`**: si nada cambia en las fichas, **una linea que lo diga** (`cap_05` `0` de `84`, `cap_06` `0` de
  `62`, firmados en la `ACTA 67`); si `d053` parte la ficha, la fila de `cap_05` recontada por instrumento.
- **`D.61`**: cada discutible, ejecutado o cerrado. Ninguno abierto.
- **`R5`** en cada bloque `$` de tu reporte, **medido con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la
  cabecera cambiada a la `69`**, y pegado.
- `python forja.py gate`, `python forja.py guiones`, `python tests/test_aceptacion.py` y `python scripts/cerrar_reporte.py`,
  **en verde y pegados**.
- **El censo antes y despues** tiene que salir igual en el dato, porque esta vuelta no inserta: **`390` nodos, `904` veredictos,
  `1` par mutuo, `45` insertados de Grove**, y la bandeja en `47` (o en `48` si `d053` parte la ficha, y lo dices).
- Commitea `docs/loop/`, lo que cambies en `.v68ext/`, las fichas si las partiste, y tu carpeta `.v69ext/`. **Si nada te obliga
  a parar, no escribas `PARA_ALEXIS.md`.**

---

## LO QUE NO HACES

- **NO INSERTAS.** Ni un `insertar`, ni un veredicto en `bitacora/`, ni una arista en el dataset.
- **NO REESCRIBES NINGUN PASO de las `20` fichas.** Su fidelidad esta firmada; partir una ficha no es reescribirla.
- **NO TOCAS `cuarentena/gerber_emyth/` NI `cuarentena/marquet_turn_the_ship/`**: van despues de Grove, en ese orden.
- **NO TOCAS `src/`, `scripts/`, el banco, el arnes ni los protocolos** (`7.F`, `D.55`), **ni `APERTURA_CIEGA.md`**.
- **NO REORDENAS LA COLA A MANO**, y **NO ABRES NINGUN LIBRO.** El mundo `11` cierra con siete.

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No
adivines.**
