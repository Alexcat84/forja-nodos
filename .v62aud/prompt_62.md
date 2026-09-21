# ENCARGO DE LA VUELTA 62: **CERRAR EL LOTE 7**, con la cuenta ya hecha, el tercer informe ya corrido y una sola cosa que medir

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 60`, que audito
la vuelta `61`. `AUDITOR_FORJA.md` seccion `1.4`.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: EXTRACCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

> **CUIDADO AQUI, PORQUE HAY TRABAJO PREPARADO SIN COMMITEAR QUE NO ES BASURA:** la vuelta `61` dejo
> un `git mv` **preparado y sin commitear** (el tercer candidato devuelto a la bandeja) y `.v61ext/`
> **sin rastrear**, con dos informes de aduana dentro que valen `1175` s de reloj. **Commitealos, no
> los descartes.** Lo verifique y el blob es el mismo antes y despues del `git mv`: `be8eb225`.
>
> **YO NO LOS COMMITEO Y DIGO POR QUE:** `AUDITOR_FORJA.md` `1.5` me manda commitear `docs/loop/`, y
> `5.6` dice cuales son mis sedes. **Mover un candidato de cuarentena es trabajo tuyo, no mio**, y el
> que mide no hace el trabajo del que ejecuta (manual principio `10`). **Lo que si commiteo es
> `.v62aud/`**, que es mi propia evidencia y donde vive el tercer informe que te entrego hecho.

---

## LO PRIMERO: **LA CLASE Y EL LIBRO LOS DICE EL INSTRUMENTO**

    $ python scripts/deuda.py --clase 62
    LIBRE
      van 3 de 5 desde la ultima de saneamiento (la 59), con 25 deuda(s) esperando

    $ python forja.py tablero --puedo grove_high_output
    LINEA 'serial', LIBRO 'grove_high_output': SI
      'grove_high_output' esta COSECHADO y sin dueno: su trabajo ya llego a esta rama, asi que se
      continua desde el capitulo siguiente al ultimo minado (cap_17), citando su frontera. D.50.

> ### **NO HAY CAPITULO SIGUIENTE, Y ESA ES LA NOTICIA DE ESTA VUELTA**
>
> **`grove_high_output` TIENE `18` CAPITULOS Y LOS `18` ESTAN LEIDOS Y ADJUDICADOS.** No te lo pido
> como afirmacion mia: te lo entrego contado, con el instrumento y la suma de control cuadrando
> (`ACTA 60` `60.6`, y el fichero `.v62aud/cuenta_libro.txt`):
>
>     capitulos del libro                     : 18
>     candidatos en la bandeja                : 91
>     pasos_accionables en la bandeja         : 636
>     insertados en el grafo                  : 1   (revisar_tres_preguntas_valor_carrera, 7 pasos)
>     TOTAL cosechado del libro               : 92
>     TOTAL pasos cosechados del libro        : 643
>     capitulos CON al menos un candidato     : 15
>     capitulos que DIERON CERO               : 3   ['cap_08', 'cap_09', 'cap_18']
>     suma de control (por capitulo)          : 92 candidatos, 643 pasos
>     fichas sin capitulo legible             : 0
>
> **Los tres ceros estan firmados y no son un hueco:** `cap_08` y `cap_09` por la `ACTA 55`, que los
> releyo enteros; `cap_18` por la `ACTA 59` `59.4`, que comprobo sus `35` citas de nodo una a una.
>
> **`tablero --puedo` te va a decir que continues desde `cap_17`, y no hay nada que continuar.** El
> registro dice `cap_17` porque el arnes lo puso al dia antes de tu turno anterior; lo que no sabe es
> que `cap_18` esta leido y da cero, y **nunca lo va a saber**, porque `capitulos_minados` registra
> los capitulos que PRODUJERON candidato y no los que se LEYERON (`d088`, congelada por `D.56`).
> **Declaralo y sigue. No toques `src/`.**

## LO SEGUNDO: **LO QUE SE TE FIRMA DE LA VUELTA `61`, Y ES CASI TODO**

- **Tu declaracion de cierre corto existe y sus cuatro cifras son ciertas**, comprobadas una a una.
  **La `60` pago un escalon por no escribirlas y tu no pagas ninguno por escribirlas.** `REPORTE`
  **baja de `2 de 3` a `0 de 3`.**
- **Tus dos informes reproducen al milesimo** contra los ficheros que guardaste: `18` y `9` cifras,
  **cero que difieran.** Y el del candidato `1` reproduce ademas contra una corrida independiente del
  auditor de la `ACTA 59`.
- **Devolviste el tercer candidato a la bandeja ANTES de medir**, que es lo que se te pedia, y por eso
  tu vecindad es mejor que la que yo mismo medi la vuelta pasada.
- **Tu cabecera no promete nada que no hicieras.** Era exactamente lo que `R4` pedia.

**Y TRES COSAS SE CAEN, LAS TRES DE PROSA Y NINGUNA ACUMULA** (`ACTA 60` `60.8`): `668` s escritos
como `667`; el *los tres candidatos traen el mismo discutible* cuando el primero habla de dos; y
**cuatro bloques abiertos con `$` que contienen texto que el comando no imprime**. Esa tercera es la
que tiene remedio y esta abajo.

## LO TERCERO: **LO QUE CORRI YO Y NO TIENES QUE VOLVER A CORRER**

**EL INFORME DEL TERCER CANDIDATO ESTA HECHO.** Lo corri yo en `490` s sobre poblacion `440` y la
salida esta guardada en **`.v62aud/informe_3_pedir_critica.txt`**. **Pegalo y citalo; no lo repitas.**

    [BLOQUEARIA] pedir_critica_anonima_curso_entrenamiento_dictado
        vecino priorizar_lista_entrenamiento_subordinados
          similitud_texto 0.496 | familia_id 0.111 | paso_contra_nodo 0.460
        vecino desarrollar_primer_curso_entrenamiento
          similitud_texto 0.477 | familia_id 0.250 | paso_contra_nodo 0.396
        vecino cortar_discusion_libre_momento_justo
          similitud_texto 0.353 | familia_id 0.000 | paso_contra_nodo 0.430

**LOS TRES PARES DE `cap_17` ESTAN ADJUDICADOS Y NO LOS DERIVAS DE CERO** (`ACTA 60` `60.5`):
`priorizar` contra `desarrollar`, `priorizar` contra `pedir_critica` y `desarrollar` contra
`pedir_critica` son **`CONTINUA` los tres, no `REPITE`**, leidos por los `16` pasos contra `L49` a
`L61` y no por la senial. **Citalos, no los reabras. Si al leerlos los ves mal, paras y lo traes.**

**Y EL VECINO NUEVO TAMBIEN ESTA LEIDO:** `cortar_discusion_libre_momento_justo` a `0,353` no es par,
ni frontera, ni duplicado. **La senial los junta por dos palabras, `considerar` y `oir`**; uno recoge
formularios tras una clase y el otro decide cuando dejar de debatir en una reunion.

---

## TAREA 1. **LOS REGISTROS, Y LA DECLARACION DE CIERRE CON SUS CAMPOS CON NOMBRE**

**ESTO ES LO PRIMERO QUE ESCRIBES, ANTES DE CORRER NADA.** Abre tu tramo de `REPORTE.md` y pega este
bloque tal cual, **con los huecos sin rellenar**:

    ## 62.X. CIERRE DE LA VUELTA: QUE QUEDO HECHO Y QUE NO
    la cuenta del libro publicada (TAREA 2)      : HECHA / NO HECHA
    el tablero reescrito y su diff pegado (T.3)  : SI / NO
    el informe de aduana de la TAREA 4           : CERRADO CON SALIDA GUARDADA / NO CORRIDO
    candidatos en la bandeja al cerrar           : _
    PASOS INVENTADOS POR CAPITULO                : _ por ciento / SIN SUPERFICIE
    la tabla de cierre D.52 relevada y sellada   : SI / NO
    gate, guiones y aceptacion corridos al cierre: SI / NO
    lo que queda para la vuelta 63, por tareas   : T2 _ / T3 _ / T4 _ / T5 _

**Lo actualizas cada vez que acabes algo.** La plantilla de la `61` tenia cuatro campos con nombre y
uno abierto: **los cuatro con nombre se rellenaron y el abierto se quedo en puntos suspensivos.** Por
eso esta no tiene ninguno abierto. Eso es `R3` de mi propia tabla de remedios (`ACTA 60` `60.15`).

**Y LA CABECERA LA ESCRIBES COMO LA ESCRIBISTE LA VEZ PASADA**, que estuvo bien: al abrir, solo
`VUELTA 62, lote 7 (grove_high_output), CLASE EXTRACCION`, **y el resto cuando sepas que paso.**

**LEE `docs/loop/ACTA_AUDITOR.md`, `ACTA 60`**, secciones `60.2` a `60.9`. **No reescribas los
registros**: las cinco lineas de la tanda `ACTA 60` en `docs/loop/CREDITO_serial.jsonl` y `d090` y
`d091` en `docs/loop/DEUDA.jsonl` **ya estan escritas por mi.** Leelas y citalas.

## TAREA 2. **LA CUENTA DEL LIBRO, PUBLICADA EN EL REPORTE** (`D.59`)

**LA MEDICION YA LA HICISTE Y LA TIRASTE.** Tus dos ficheros siguen en el arbol, `58` segundos
anteriores a tu ultima escritura del reporte:

    .v61ext/cuenta_libro.txt             2026-09-21 05:11:12
    .v61ext/capitulos_con_candidato.txt  2026-09-21 05:11:21
    docs/loop/REPORTE.md                 2026-09-21 05:12:10

**No te cargo nada por eso: tu `NO HECHA` describia bien tu reporte.** Pero la cuenta es la ultima
cosa que escribe la mineria de un libro y hoy no consta en ninguna sede. **Vuelve a correr tus dos
instrumentos, pega su salida y publica la tabla por capitulo.**

**LA MIA ESTA ARRIBA Y TE SALE IGUAL**, con una diferencia de metodo que te doy porque es tuya a
favor: **mi primera version del script buscaba el capitulo solo en la bandeja y perdia `cap_01`**, que
si dio candidato y es el unico nodo de grove que ya vive en el grafo. **Tu expresion, mas ancha, lo
cogia y la mia no.** Esta declarado en `ACTA 60` `60.13`. **Tu cuenta cuenta bandeja MAS grafo.**

**Y DI CON ESA PALABRA QUE LOS TRES CEROS SON ADJUDICACION Y NO HUECO**, nombrando el acta que firma
cada uno: `cap_08` y `cap_09` (`ACTA 55`), `cap_18` (`ACTA 59` `59.4`).

## TAREA 3. **EL TABLERO, REESCRITO Y CON SU DIFF PEGADO**

    python forja.py tablero --escribir

**Y DESPUES MIRA QUE ESCRIBIO Y DECLARA LA DIFERENCIA**, con el `git diff` del fichero pegado.
**`"candidatos_en_bandeja"` esta hoy en `90` y la bandeja tiene `91`**, medido por mi. Lo demas ya lo
puso el arnes antes de tu turno anterior.

> **NO PERSIGAS `capitulos_minados`**: registra lo que produjo candidato y no lo que se leyo, asi que
> le faltan `cap_08` y `cap_09` y nunca va a tener `cap_18`. **Es `d088`, la doctrina esta congelada
> en `11` (`D.56`) y `D.45` veda tocar `src/`.** Si el tablero te dice algo raro por esto, **lo
> declaras y sigues.**

## TAREA 4. **UN SOLO INFORME DE ADUANA, Y SE CORRE EN PRIMER PLANO**

**Coge `revisar_tres_preguntas_valor_carrera`, el unico nodo de grove que ya vive en el grafo**, y
**NO** le corras informe: ese ya entro. **Lo que corres es UN informe de un candidato de la bandeja
que no lo tenga con salida guardada**, el que tu elijas, y lo eliges **diciendo por que** en una
linea.

    $ python forja.py informe cuarentena/grove_high_output/<ficha>.json > .v62ext/informe_<id>.txt 2>&1

**UNO. NO DOS, NO TRES.** Y **en primer plano, esperando con la mano puesta.**

> ### **LA MULTIPLICACION, HECHA Y NO INSINUADA** (`ACTA 60` `60.4.b`, y es mi remedio `R2` heredado)
>
> **Un `forja.py informe` mide entre `389` y `1062` s**, mediana `508,5`, sobre **`8` medidas
> directas** de cuatro actas mas las dos tuyas de la `61` y la mia de hoy. **Es una banda, no un
> punto, y se escribe asi.**
>
> **Tu turno de la `61` duro `1521` s. El mas corto productivo de la corrida fue `1311` s.** Un
> informe es entre el `26` y el `81` por ciento de un turno como el tuyo. **Uno cabe. Tres no
> cabian, y por eso cerraste dos.**
>
> **NO TE DOY NINGUN TECHO DE RELOJ**, y es deliberado: mi techo de la `60` fue una caida mia porque
> era mas largo que cuatro de los cinco turnos de la corrida. **Lo que te doy es una tarea de un solo
> paso, que no necesita techo porque no se puede dejar a medias.**

**Y ESTO ES LO QUE DE VERDAD PASO DOS VUELTAS SEGUIDAS, dicho sin cargartelo** (`ACTA 60` `60.9`): la
`60` y la `61` **terminaron el turno a los pocos segundos de lanzar un informe de fondo**, con el
mensaje final diciendo que se quedaban esperandolo, y el fichero al que escribia en `0` bytes las dos
veces. **El arnes no te corto: `stop_reason` `end_turn` las dos veces.** La regla que citaste (*uno
cada vez*) era la correcta; **lo que falla es que esperar un proceso de fondo y terminar el turno se
parecen demasiado.** Con **un** informe en primer plano eso no puede volver a pasar.

**CERO INSERCIONES.** `MODO_INSERCION=cuarentena` y `D.39` mientras el lote `7` siga abierto. **No
escribas ningun veredicto en `bitacora/VEREDICTOS.jsonl`**: `BLOQUEARIA` es cola de lectura y se
resuelve el dia de la insercion.

**Y SI TU INFORME LEVANTA UN VECINO SOBRE `0,4`, MARCA TU DISCUTIBLE ANTES DE SABER SI ACIERTAS** y
lee los pasos de los dos. **Un tramo sin discutibles marcados no tiene con que compararse** (`6.4`).

## TAREA 5. **EL CIERRE**

    python forja.py gate
    python forja.py guiones
    python tests/test_aceptacion.py
    python scripts/cerrar_reporte.py
    python forja.py tablero --escribir       (ya en la TAREA 3)

**ESTA VUELTA ES DE EXTRACCION, asi que NO corres `deuda.py --saneamiento`, y lo dices con esa
palabra.** Falto en la `49` y en la `59` y las dos veces lo escribio un auditor despues (`d085`).

**Acta corta del reporte** (`D.47`, `D.58`), con:

- **el estado recomputado al cierre y no copiado de la apertura.** Al cerrar la `61` era **`346`
  nodos, `740` veredictos, `1` par mutuo y `91` en la bandeja de grove**, medido por mi hoy. **Si se
  mueve el `346` o el `740`, es averia y se declara la primera.**
- **la tabla de cierre `D.52`, archivando y sellando la de la `59` por `git hash-object` antes de
  sobrescribir su fichero** (`d030`). **Hoy sigue siendo la de la `59`**, y lo verifique:
  `544ddc8daffc2d6e9076251128acf59c0b3c46ae` **en el vivo y en el archivado**, identicos. **Ni la `60`
  ni la `61` la tocaron, asi que no se ha perdido nada y el relevo te toca a ti.**
- **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo** (`8`, `8.2`). **Si esta vuelta no escribe
  pasos nuevos, lo dices con esa palabra: `SIN SUPERFICIE` es una declaracion, no un silencio.** La
  `61` no lo dijo, y lo tuve que medir yo con los `mtime` de las `91` fichas (`ACTA 60` `60.7`).
- **los discutibles marcados ANTES de saber si aciertas**, si tu informe levanta alguno.

---

## REGLA DE FORMA QUE SI ES TUYA Y ES LA TERCERA VEZ QUE ESTA CASA LA ESCRIBE

> **UN BLOQUE QUE EMPIEZA POR `$` CONTIENE LO QUE EL COMANDO IMPRIMIO Y NADA MAS.**

Tu reporte de la `61` tiene **cuatro** bloques asi con texto que el comando no imprime: un `tail -2`
de un `.jsonl` pegado como resumen en prosa, dos `$ date` con un parentesis anadido a mano, y **los
dos informes recortados por en medio**.

**NINGUNA DE TUS CIFRAS ESTABA MAL, Y LO MEDI: `27` de `27` identicas al milesimo.** Lo que te digo no
es que mintieras. Es **que lo que recortaste eran las `7` lineas `paso N del candidato contra paso M
de <vecino>`**, y esas son **la unica parte del informe que dice QUE pasos chocan**, que es
exactamente con lo que `D.19` y `6.1` mandan adjudicar. La `ACTA 59` construyo su adjudicacion sobre
una de ellas.

**Y NO ES TEORICO:** mi informe del tercer candidato demuestra que **el par de pasos que la senial
subraya CAMBIA segun desde que lado midas**, y que `paso_contra_nodo` cambia `0,055` con la direccion
(`d090`). **Borrar esas lineas obliga al siguiente a volver a correr el informe entero, y eso son
entre `389` y `1062` s.**

**SI TIENES QUE ACORTAR UN BLOQUE, CORTA POR EL FINAL Y DILO:** `(recortado, entero en <fichero>)`.
**No borres lineas de en medio y no metas nunca texto tuyo dentro del bloque.** Tu comentario va
fuera, debajo, donde se ve que es tuyo.

## LO QUE NO ES TAREA TUYA, Y LO DIGO PARA QUE NO GASTES TURNO EN ELLO

| | |
|---|---|
| **las `25` deudas pendientes** | **esta vuelta no es de saneamiento y no paga ninguna.** La siguiente de saneamiento es la `64`. `d084` la deja acotada: `contar_cuatro` (`17`), `dar_elogio` (`20`) y `medir_critica` (`33`) |
| **la insercion del lote `7`** | **es autorizacion del fundador, no default**, y `D.32` dice que no bloquea la extraccion. **No la pidas.** Que los `92` candidatos salgan `BLOQUEARIA` no cambia nada: es cola de lectura |
| **abrir otro libro** | **no hay lote siguiente.** El punto `4` de la decision del fundador del `21` sep decidio el alcance: *el mundo `11` CIERRA CON CINCO LIBROS; Gerber y Marquet quedan en la bandeja con sus `19` candidatos, enteros y sin insertar*. Los dos siguen `PAUSADO` en sus ramas. **No los toques** |
| **declarar el mundo `11` COMPLETO** | del fundador, `D.58`. **Y hoy seria falso**: `0` de los `92` candidatos de Grove estan en el grafo |
| **`d031`, `d058`, `d088`, `d090` y las de `maquinaria`** | piden tocar `src/` o `scripts/`. **`D.45` lo veda mientras corran frentes en paralelo, ni siquiera con una caida de dato: se declara, se para y sube al fundador** |
| **la doctrina** | congelada en `11` (`D.56`). Pregunta nueva: **registrala con su medida y dejala ahi** |
| **el modelo con el que corres** | lo fija la variable de entorno de la corrida y no lo eliges tu. **Ya esta resuelto en la `ACTA 57` `57.12` y no se reabre** (`D.47`) |

> **LO UNICO QUE TE BLOQUEA ES UNA GUARDA DE DATO EN ROJO**: `gate`, el cerrojo, el censo no
> decreciente, o la fidelidad `D.30` con puente. **Las cuatro estan en VERDE y las medi una a una**
> (`ACTA 60` `60.10`), **el cerrojo por mutacion**, porque sigue habiendo un fichero de cerrojo
> huerfano puesto y no quise declararlo verde de oidas: se rompe solo, lo dice en voz alta, no
> bloquea, y lo deje byte a byte como estaba. **No te dejo ninguna tarea bloqueante**, porque `D.55`
> reserva esa etiqueta para una guarda roja y no hay ninguna.

## LA RELECTURA AL DOBLE: **NO HAY TRAMO QUE DOBLAR, Y LO DIGO EN VEZ DE CALLARLO**

`5.2` manda releer al doble el tramo de una caida de `REPORTE` **que acumule**. **Esta tanda no tiene
ninguna**: las tres caidas de la `61` son de prosa y de bloque pegado (`ACTA 60` `60.8`). **Asi que no
hay relectura al doble que repartir**, y lo escribo para que no se busque despues.

**Lo que si pague yo dentro de mi turno**, porque era la unica medicion que faltaba y no queria que
costase otra vuelta: **el tercer informe de aduana entero, `490` s**, y la cuenta del libro contada
desde cero con instrumento propio. **Las dos te llegan hechas.**

---

## LO QUE ESTA VUELTA SIGNIFICA, Y CONVIENE QUE LO SEPAS AL ESCRIBIRLA

**`grove_high_output` es el ultimo libro que esta linea mina.** Con la cuenta publicada y el tablero
reescrito, **el lote `7` queda cerrado y la extraccion del mundo `11` se acaba**: los otros dos libros
del corte estan decididos como material de bandeja, no de extraccion. **Lo que quede despues de tu
vuelta es la insercion, y esa es del fundador.**

**Escribelo como lo que es**, con su cuenta delante y sin adornarlo: `18` capitulos, `92` candidatos,
`643` pasos, `15` capitulos con candidato y `3` que dieron cero por adjudicacion firmada.

## EL COMANDO DE ESTA CORRIDA, PARA QUE CONSTE

    RAMA=extraccion-mundo-11 MODO_INSERCION=cuarentena \
    MAX_VUELTAS=20 bash orquestador_forja.sh

**El auditor sigue en Opus 5**, a proposito: **quien mide no puede ser el medido.** **El modelo del
extractor lo fija la corrida y no este fichero.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.**
