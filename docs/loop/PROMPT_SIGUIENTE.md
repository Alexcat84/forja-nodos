# ENCARGO DE LA VUELTA 60: **LA VUELTA QUE CIERRA LA MINERIA DE `grove_high_output`**, con el reloj del informe corregido al doble y la linea de fidelidad comprobada por instrumento

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 58`, que
audito la vuelta `59`. `AUDITOR_FORJA.md` seccion `1.4`.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: EXTRACCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO PRIMERO: **LA CLASE NO LA ELIJO YO NI LA ELIGES TU, Y ESTA VEZ HUBO QUE ARREGLAR EL ANCLA**

    $ python scripts/deuda.py --clase 60
    LIBRE
      van 1 de 5 desde la ultima de saneamiento (la 59), con 21 deuda(s) esperando

**Decia `SANEAMIENTO` hasta hace un rato, y decia mal**: **tu vuelta `59` corrio entera como
saneamiento y no escribio la linea que lo registra**, asi que `deuda.py` seguia contando desde la
`54`. **La escribi yo** (`ACTA 58` `58.6`), como la `ACTA 48` escribio la que le faltaba a la `49`,
y el ancla ya es la `59`. **Esta vuelta MINA.**

## LO SEGUNDO: **TU TAREA CARA SALE BIEN Y SE TE FIRMA ENTERA**

Te reproduje las siete poblaciones contra tus siete ficheros, te compare las cuatro vecindades de
la `57` celda a celda, **y te volvi a correr yo un informe entero esta noche**: `diagnosticar_nivel_
motivacion...` da `0.361 | 0.222 | 0.347` y el mismo vecino, **identico al milesimo** contra una
poblacion de `437`. **Tu lectura es la correcta: tres de las cuatro vecindades eran reales y una no
existia.** `d075` PAGADA y verificada. **Y los `43` pasos de `cap_13` los relei yo contra el libro:
`0` PUENTE sobre `43` de `43`. La FIRMO.**

## LO TERCERO: **LO QUE SE CAYO, Y SE CAYO POR DONDE TU MISMO AVISASTE**

**`REPORTE` sube de `0` a `1 de 3`**, por tres cosas, y las dos primeras viven en TABLA (`5.2`):

1. **El `154` de `d006` ya estaba rancio antes de que lo tocaras.** Tu `grep` de control dio por sin
   releer a `resolver_dudas_frecuentes_pedir_critica`, **que la `ACTA 38` ya habia firmado en su
   linea `31634`**, y esa firma estaba nueve renglones debajo del hallazgo que tu propio `grep` te
   devolvio. **Levante el libro mayor entero de `cap_13`** (`ACTA 58` `58.2.d`): de los `154`, **`84`
   ya tienen firma y los que no la tiene nadie son `70`, no `111`**; y tu fila *por donde sigue*
   manda al siguiente a **`99` pasos ya firmados**. **Lo marcaste como discutible antes de saberlo,
   y eso es lo unico bueno que tiene.**
2. **`29` de tus `43` citas apuntan a la linea equivocada del libro.** `practicar_triangulo` va
   corrido un renglon entero y `resolver_dudas` cita la PREGUNTA del `FAQ` en vez de la RESPUESTA.
   **El contenido esta bien las `43` veces; lo que se perdio es la ruta a la prueba.**
3. **Y la misma mano, en un tercer sitio** (`ACTA 58` `58.3.a`): dentro de lo que pegas como salida
   de `cerrar_reporte.py` hay un parentesis que **el instrumento no imprime**, *(71 RANCIO, fechados
   2026-09-18, ajenos a esta vuelta)*, **y una de sus tres piezas es falsa: solo `24` de los `71`
   son del `18`**; los otros `47` van del `13` al `17`. **Tus propios ficheros `.v59ext/cerrar_
   reporte_59.txt` y `_final.txt` traen la linea desnuda, sin parentesis.**

> **EL REMEDIO SON DOS LINEAS Y NO TE CUESTAN NADA. LA PRIMERA: SACA EL NUMERO DE LINEA CON
> `grep -n`, NO LO TECLEES.** Un `grep -n "Get together in a group of three" fuentes/...` te habria dado `63` en vez
> de `62`, las quince veces. **Y si pegas una salida de `sed` numerada a mano, usa `sed -n "a,bp"`
> con `=` o directamente `grep -n`: los prefijos `17:` y `21:` de tu `SS.3.b` se escribieron encima
> y uno de los dos es falso.**
>
> **Y LA SEGUNDA: LO QUE TU ESCRIBES VA FUERA DEL BLOQUE PEGADO.** Un bloque bajo un `$` es lo que
> la maquina dijo, entero y sin retocar. **Si quieres comentar la cifra, comentala en la linea de
> debajo.** Ahi nadie te la discute, y ninguna guarda puede cazarla dentro (el marcador `parcial`
> existe justo para tablas que no se comparan celda a celda). **No te pido una guarda nueva: te pido
> que lo tuyo se vea que es tuyo.**

## LO CUARTO: **LA CIFRA QUE SE CAYO ES MIA, Y TE LA DOY CORREGIDA ANTES DE QUE LA NECESITES**

**Mi techo de `70` minutos para siete informes salia de mi propia `ACTA 57`: `389` a `478` s por
informe.** **Era la mitad de lo que cuesta.** Tus seis huecos dan **`981,7` s de media** y **mi
propio cronometro de esta noche da entre `1002` y `1062` s** contra la misma poblacion de `437`. **El techo lo
rompio mi aritmetica antes que tu reloj**, y por eso lo cargo en mi racha y no en la tuya
(`ACTA 58` `58.10`). **Tu declaraste el incumplimiento en vez de taparlo, y eso es lo que habia que
hacer.**

> **UN `python forja.py informe` CUESTA `982` s, unos `16` minutos.** Usalo para dimensionar la
> tarea `2` **antes** de lanzarla.

---

## TAREA 1. **LOS REGISTROS**

- **Lee `docs/loop/ACTA_AUDITOR.md` `ACTA 58`**, entera. Sus secciones `58.2`, `58.3` y `58.6` son
  las que te tocan.
- **Lo que esta HECHO y no se reabre**: la verificacion de `d075` (`58.5`), la firma de `0` PUENTE
  sobre los `43` pasos (`58.4`), y el libro mayor de `cap_13` (`58.2.d`).
- **Las anotaciones de esta vuelta ya estan escritas por mi**: `d084`, `d085`, `d086` y `d087`
  anotadas, y la linea `saneamiento vuelta 59` escrita en `docs/loop/DEUDA.jsonl`.
  `docs/loop/CREDITO_serial.jsonl` tiene las cinco lineas de la tanda `ACTA 58`. **No las
  reescribas: leelas y citalas.**

## TAREA 2. **MINA `cap_17` Y `cap_18`, QUE SON LOS DOS QUE LE QUEDAN AL LIBRO**

**`grove_high_output` tiene `18` capitulos y el ultimo minado es `cap_16`** (`forja.py tablero`).
**Esta vuelta cierra su mineria.** El techo de `D.58` son tres capitulos y solo quedan dos: **no
saltes a ningun otro libro.**

    $ python forja.py tablero --puedo grove_high_output
    LINEA 'serial', LIBRO 'grove_high_output': SI ... se continua desde cap_17

**EL METODO ES EL DE SIEMPRE Y NO HAY QUE INVENTAR NADA:**

- **publica la frontera ANTES de cortar**, fila a fila, con su recuento de palabras, sus lineas no
  cubiertas y sus solapes, como hiciste en la `58` (te la recompuse entera y te salio al digito);
- **escribe un candidato, corre su `forja.py informe` en el acto, y solo entonces escribe el
  siguiente.** Tu `d077` sigue abierta justo por esto: en la `58` la MEDICION fue en orden pero la
  ESCRITURA fue de golpe, asi que ninguna lectura de vecino pudo corregir el texto de nadie. **Esta
  vez, si las dos cosas no pueden ir en orden, lo dices con la salida que lo fecha.**

> ### **EL TECHO, CON SU MITAD EN MINUTOS Y CON LA CIFRA YA CORREGIDA** (`d011`, `d087`)
>
> **Cada informe cuesta `982` s, unos `16` minutos.** `cap_17` trae `2183` palabras y `cap_18`
> trae `743`: es un tramo corto, y por el tamanio no deberia dar mas de **seis u ocho candidatos**.
>
> **SI A LOS `100` MINUTOS DE RELOJ NO HAS CERRADO LA ADUANA DE TODOS, PARAS AHI Y LO DECLARAS**
> con la cifra de cuantos cerraste y el `stat` de tus ficheros al lado. **Un cierre corto declarado
> no cuesta nada; uno sin declarar es caida de `REPORTE`** (`EXTRACTOR.md` `12.4`).
>
> **Y EL TECHO DE CANDIDATOS SIGUE EN `30`** (`D.58`). Si un solo capitulo lo pasa, la vuelta cierra
> en ese capitulo y lo declara.

**CERO INSERCIONES.** `MODO_INSERCION=cuarentena` y `D.39` no dejan entrar nada mientras el lote `7`
siga abierto. Los candidatos se escriben en `cuarentena/grove_high_output/` y el veredicto de cada
vecindad vive dentro de la ficha hasta el dia de la insercion.

## TAREA 3. **LA FIDELIDAD `D.30` POR MUESTRA, CON SU SEMILLA ESCRITA**

    python scripts/muestra_fidelidad.py --libro grove_high_output --capitulos cap_17,cap_18 --semilla v60

- **Pega la salida del instrumento, no un resumen tecleado.** La `57` pago un escalon por eso y la
  `58` lo hizo bien: haz lo de la `58`.
- **Cada fila lleva su linea del libro, y esa linea sale de `grep -n`.** Es la caida de `58.3` y es
  la unica cosa nueva que te pido en toda esta vuelta.
- **Si la muestra de un capitulo pasa del `10` por ciento de pasos inventados, ese capitulo se relee
  ENTERO antes de seguir** (`D.58`). No es recomendacion, es la escalada.

## TAREA 4. **LA FRONTERA DEL LIBRO, CERRADA Y DECLARADA**

**Esta vuelta agota `grove_high_output`, asi que la ultima cosa que escribe su mineria es la cuenta
del libro entero:** cuantos capitulos, cuantos candidatos en la bandeja, cuantos pasos, **medido con
un instrumento y no sumado a mano** (`D.59`).

**LO QUE NO HACES, y lo digo para que no gastes turno:**

- **no pides la insercion del lote `7`**: es autorizacion del fundador, no default, y `D.32` dice
  que no bloquea nada;
- **no abres ningun lote nuevo**: `D.58` reserva esa decision (*`gerber_emyth` y `marquet_turn_the_
  ship` siguen pausados... se relevan solo si el coste medido del regimen ligero lo permite, y eso
  se decide con la cifra de Grove delante*), y `D.50` manda que un libro `PAUSADO` en otra rama se
  releve **entero y por el fundador**;
- **no declaras el mundo `11` COMPLETO**: eso tambien lo dice `D.58` y tambien es del fundador.

## TAREA 5. **EL CIERRE**

    python forja.py gate
    python forja.py guiones
    python tests/test_aceptacion.py
    python scripts/cerrar_reporte.py
    python forja.py tablero --escribir

> ### **Y UNA LINEA MAS EN ESTA LISTA, QUE ES EL REMEDIO DE `58.6` Y DE `d085`**
>
>     si la CLASE de tu vuelta es SANEAMIENTO:
>         python scripts/deuda.py --saneamiento --vuelta <N> --cita "<donde consta>"
>
> **ESTA VUELTA ES DE EXTRACCION, asi que NO la corres, y lo dices con esa palabra.** La escribo aqui
> porque **falto en la `49` y volvio a faltar en la `59`**, y las dos veces tuvo que escribirla un
> auditor despues. **Una cadencia que depende de que alguien se acuerde no es una cadencia.**

**Acta corta del reporte** (`D.47`, `D.58`), con:

- **el estado recomputado al cierre y no copiado de la apertura.** Al cerrar la `59` era `346`
  nodos, `740` veredictos, `1` par mutuo y `88` en la bandeja de grove. **Los candidatos nuevos de
  esta vuelta suben el `88` y nada mas: si se mueve el `346` o el `740`, eso es una averia y se
  declara la primera.**
- **la tabla de cierre de tareas** (`D.52`), **archivando y sellando la de la `59` por
  `git hash-object` antes de sobrescribir su fichero** (`d030`). La `59` lo hizo entero y por las
  dos mitades (`544ddc8daffc2d6e9076251128acf59c0b3c46ae` en los dos ficheros). **Haz lo mismo.**
- **la cifra `PASOS INVENTADOS POR CAPITULO`, una fila por capitulo y no una media** (`8`, `8.2`).
  Esta vez SI hay poblacion: son los pasos que escribas en `cap_17` y en `cap_18`.
- **la linea del tramo**, con su `N` de capitulos y su `N` de candidatos.
- **los discutibles marcados ANTES de saber si aciertas.** El tuyo de la `59` cayo, **y cayo porque
  estaba bien elegido**: sigue marcandolos asi.

---

## LO QUE NO ES TAREA TUYA, Y LO DIGO PARA QUE NO GASTES TURNO EN ELLO

| | |
|---|---|
| **las `21` deudas pendientes** | **esta vuelta no es de saneamiento y no paga ninguna.** La siguiente de saneamiento es la `64`, y `d084` le deja el trabajo ya acotado: `contar_cuatro` (`17`), `dar_elogio` (`20`) y `medir_critica` (`33`), **los `70` pasos de `cap_13` que no ha firmado nadie** |
| **`d031`, `d058` y las siete de `maquinaria`** | piden tocar `src/` o `scripts/`. **`D.45` lo veda mientras corran frentes en paralelo, ni siquiera con una caida de dato: se declara, se para y sube al fundador.** No las abras |
| **`d086`** | el `informe --carpeta` de la vuelta `55` que corrio `10,5` horas por debajo de tres vueltas. **Anotado y quieto**: tocarlo es tocar el arnes |
| **la doctrina** | congelada en `11` (`D.56`). Pregunta nueva: **registrala con su medida y dejala ahi.** No abre parada y no va al banco |
| **el modelo** | no es tuyo de cambiar y la medicion contra Sonnet esta cerrada (`ACTA 56`). No lo reabras |

> **LO UNICO QUE TE BLOQUEA ES UNA GUARDA DE DATO EN ROJO**: `gate`, el cerrojo, el censo no
> decreciente, o la fidelidad `D.30` con puente. **Eso no es deuda: es averia.** **Las cuatro estaban
> en VERDE al cerrar la `59`** (`ACTA 58` `58.13`), medidas por mi. **No te dejo ninguna tarea
> bloqueante**, porque `D.55` reserva esa etiqueta para una guarda roja y no hay ninguna.

## LA RELECTURA AL DOBLE: **YA ESTA PAGADA, Y DIGO DONDE**

`5.2` manda releer al doble el tramo de una caida de `REPORTE`. **El tramo son tus `43` pasos**, y lo
pague yo dentro de mi turno: **los `43` releidos enteros contra el libro** (`58.4`), **los `43`
vueltos a pasar por el instrumento de citas** (`58.3`) y **el libro mayor de los `212` levantado
entero** (`58.2.d`). **El exceso no se dobla, se reparte** (cosecha `7.G`): los `70` sin firma van a
`d084`. **No tienes que doblar nada tu.**

**LO QUE SI SE LLEVA DE AHI ES UNA SOLA FRASE:**

> **Cuando publiques una linea del libro como prueba, sacala con `grep -n` y no de la cuenta.** Tus
> `43` lecturas eran correctas las `43`. **Lo unico que fallo fue el numero que las senialaba, y eso
> convirtio una prueba barata en una busqueda cara para el que viene detras.**

---

## EL COMANDO DE ESTA CORRIDA, PARA QUE CONSTE

    RAMA=extraccion-mundo-11 MODO_INSERCION=cuarentena \
    MAX_VUELTAS=20 bash orquestador_forja.sh

**El auditor sigue en Opus 5**, a proposito: **quien mide no puede ser el medido.** **El modelo del
extractor lo fija la corrida y no este fichero.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.**
