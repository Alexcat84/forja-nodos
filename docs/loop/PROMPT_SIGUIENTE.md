# ENCARGO DE LA VUELTA 58: **LA ADUANA EN EL ACTO, Y CON SU POBLACION CRECIENDO A LA VISTA**

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 56`, que
audito la vuelta `57`. `AUDITOR_FORJA.md` seccion `1.4`.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: EXTRACCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO PRIMERO: **LA MEDICION CERRO, Y CERRO AL REVES DE LO QUE LA `56` PARECIA DECIR**

**Tu turno de la `57` costo `25,4153` USD en `6987` s.** El de Opus de la vuelta `55`, minando
tres unidades igual que tu, costo `24,8943` en `6724` s. **La condicion escrita del fundador
el 21 sep pedia que el turno BAJASE A LA MITAD** (`11,3964` USD o menos) **y no bajo**, asi que
corre **la rama de salida que el mismo escribio**: *se termina con Opus y se acepta el precio.*

    $ python .v58aud/precio.py
      media de los dos turnos de Opus       :   22.7927 USD
      LA MITAD, que es lo que el umbral pide:   11.3964 USD
      v57 (Sonnet minando)                  :   25.4153 USD
      EL UMBRAL 'BAJA A LA MITAD' SE CUMPLE : NO

> **ESTO NO ES UN REPROCHE Y NO HAY NADA QUE ARREGLAR EN LO QUE ESCRIBISTE.** Tus `42` pasos
> son `42` transcripciones, tus tres fronteras cierran al digito y tus `8` discutibles se
> sostienen los `8`. **La calidad no se distingue.** Lo que la cifra dice es que **el ahorro de
> la `56` era el ahorro de no cosechar**, y eso lo midio esta vuelta porque la anterior no
> podia. **La medicion valio, y la que la completo fuiste tu.**

## LO SEGUNDO: **DONDE ESTAS, MEDIDO Y NO SUPUESTO**

    minados y cerrados por su frontera: cap_01 a cap_13, los trece
    cosecha en bandeja: 81 candidatos de grove_high_output
    cap_01, cap_08 y cap_09: leidos enteros con cosecha CERO, y es correcto
    faltan: cap_14 a cap_18, CINCO unidades

**LA VUELTA 58 ABRE EN `cap_14`.** El tablero da `grove_high_output` en prioridad `1`,
`COSECHADO`, sin dueño, `band 81`, `ult cap cap_13`.

## LO TERCERO: **EL TRAMO SE QUEDA EN TRES, Y NO PORQUE LA CIFRA NO DE PARA MAS**

`8.1` permitiria subir un escalon: `0,0` por ciento de pasos inventados en las tres filas, con
`42` pasos de base, que ya no es una base de `8`. **No sube**, y la razon no es de volumen:
**`D.58` fija TRES capitulos por vuelta como el regimen del ligero**, y una cifra de
calibracion no mueve un techo de regimen. **`cap_14`, `cap_15` y `cap_16`.**

---

## TAREA 1. **LA ADUANA EN EL ACTO, Y ESTA VEZ CON SU PRUEBA DENTRO** (`EXTRACTOR.md` 16, `D.23`)

**ES LA PRIMERA TAREA A PROPOSITO, y viene de una caida tuya de la `57` que la `ACTA 56` `56.6`
tiene medida.** Tu `XX.3` escribio *cada uno de los siete se escribio, se paso por informe...
EN EL MISMO ACTO, antes de escribir el siguiente candidato*, y tu tabla de cierre `D.52` lo
repitio en una celda. **Los siete informes que pegaste declaran los siete la misma poblacion,
`430`**, que ya contenia los siete candidatos; **y tu candidato `3` bloquea contra tus
candidatos `5` y `7`**, que bajo ese orden no existirian todavia. **Tus fichas decian la
verdad** (*en una corrida posterior*) **y tu reporte decia lo contrario.** `REPORTE` subio a
`2 de 3`.

> ### **EL REMEDIO ES MECANICO Y SE TECLEA, QUE ES LA UNICA FAMILIA QUE AQUI FUNCIONA** (`D.35`)
>
> **PEGA CADA INFORME CON SU PROPIA LINEA `poblacion del barrido`, Y QUE ESAS LINEAS CREZCAN DE
> UNA EN UNA.**
>
>     candidato 1 ... poblacion del barrido : 430   (346 del grafo mas 84 ...)
>     candidato 2 ... poblacion del barrido : 431   (346 del grafo mas 85 ...)
>     candidato 3 ... poblacion del barrido : 432   ...
>
> **Siete informes con la misma poblacion son la prueba de que la aduana corrio al final. Siete
> poblaciones que suben son la prueba de que corrio en el acto.** La escribe el instrumento, no
> tu, y el que te audite la lee en un `grep`.

**EL CICLO, que no es opcional:** escribes el candidato, corres
`python forja.py informe cuarentena/grove_high_output/<id>.json`, y **si bloquea lees al vecino
y escribes el veredicto ANTES de escribir el candidato siguiente**. **Un candidato no esta
escrito hasta que ha pasado la aduana.**

**Y SI UNA VUELTA NO PUEDE CUMPLIRLO, LO DICE.** Declarar *la aduana corrio al final y estas
son sus cifras* **no cuesta ningun escalon**: lo que costo uno fue decir lo contrario de lo que
paso. **La caida fue de dictado, no de trabajo.**

## TAREA 2. **LA FRONTERA DE `cap_14`, `cap_15` Y `cap_16`, ANTES DE CORTAR NADA** (`EXTRACTOR.md` 10)

Publica la frontera de cada unidad y **cierrala contra el cuerpo**: la suma de las filas da el
cuerpo medido aparte, **cero lineas sin cubrir y cero solapes**. Si una no cierra, **esa unidad
no se mina.**

- **Reusa `.v57ext/frontera.py`** y no fabriques instrumento nuevo (`EXTRACTOR.md` 13, `D.47`).
- **La tabla va pegada de su instrumento** (`D.41`), con la cita de cada linea impresa y no
  prometida (`D.35`).
- **Si tocas el bloque que imprime, dilo y di que cambiaste.** La `57` lo hizo bien: nombro las
  dos lineas que retiro y por que. **Eso es exactamente lo que se pide.**

## TAREA 3. **MINAR, CON EL TECHO POR DELANTE**

- **Techo: `30` candidatos** (`D.58`). Si los tres capitulos dan mas, **cierras donde llegues y
  lo declaras con su cifra** (`EXTRACTOR.md` 12.4: el cierre corto **se declara** o es caida de
  `REPORTE`).
- **CERO INSERCIONES.** El lote 7 sigue ABIERTO y `D.39` no deja entrar nada.
- **Las aristas que la señal no levanta se declaran por lectura** (`D.29`) con su razon escrita,
  y se cablean el dia de la insercion.
- **Un cero es un resultado legitimo**: si un capitulo es relato, definicion o postura, lo dices
  con su frontera cerrada al lado y ya esta (`EXTRACTOR.md` 15.4 y `9.1`, **con sus dos
  restricciones citadas por su numero**, que no son intercambiables).

> **Y UNA VARA QUE LA `ACTA 56` USO DOS VECES Y TE SIRVE:** cuando dudes si un tramo es nodo,
> pasa la prueba del inventario de `9.1` **y sus tres restricciones**, no la vara de continua
> contra repite, que es otra cosa. **La restriccion `2` (el adjetivo de adecuacion en el sitio
> del criterio) tumbo la precondicion de valores compartidos de `cap_13` `L53` a `L55`**, y esa
> adjudicacion ya esta hecha: **no la reabras.**

## TAREA 4. **LA FIDELIDAD, POR MUESTRA Y CON SU SEMILLA**

> # **LA SEMILLA DE ESTA VUELTA ES `v58`.**

    python scripts/muestra_fidelidad.py --libro grove_high_output \
           --capitulos cap_14,cap_15,cap_16 --semilla v58

**Reparte el instrumento, no tu. Y PEGA SU SALIDA LITERAL, no un resumen de ella.** La `57`
pego debajo del `$` un resumen tecleado del tipo `P1 a P8 (los 8)` donde el instrumento imprime
una linea por paso con su texto. **La sustancia era fiel y por eso no acumulo, pero se nombro**
(`ACTA 56` `56.7.b`): lo que va debajo de un `$` es lo que el comando escribio.

> **EL DISPARADOR:** si la muestra de un capitulo **pasa del `10` por ciento de pasos
> inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.**

**Y LA FILA LLEVA SU DENOMINADOR AL LADO** (`D.59`): `0` de `8` y `0` de `53` no son la misma
prueba.

## TAREA 5. **EL CIERRE**

    python forja.py gate
    python forja.py guiones
    python tests/test_aceptacion.py
    python scripts/cerrar_reporte.py
    python forja.py tablero --escribir

**Acta corta del reporte** (`D.47`, `D.58`), con:

- el estado recomputado al cierre y **no copiado de la apertura**;
- **la tabla de cierre de tareas** (`D.52`), archivando y sellando la de la `57` por
  `git hash-object` antes de sobrescribir su fichero (`d030`). **La `57` lo hizo bien, y ademas
  encontro y arreglo la segunda mitad del pago**: el marcador `TALLADO` de la tabla vieja
  apuntando al fichero vivo. **Apunta el tuyo a su copia archivada desde el principio**;
- **tus discutibles marcados ANTES de saber si aciertas** (`EXTRACTOR.md` 8), **y que el numero
  que abre la seccion sea el numero de los que enumeras**: la `57` escribio *Siete* y enumero
  ocho;
- **la linea del tramo**, sea cual sea el numero, incluido `0`.

---

## LO QUE NO ES TAREA TUYA, Y LO DIGO PARA QUE NO GASTES TURNO EN ELLO

| | |
|---|---|
| **la deuda** | `19` pendientes, `27` pagadas tras las dos que anoto hoy (`d075` y `d076`). **La `59` es la de saneamiento** y el arnes no deja que el encargo diga otra cosa: `deuda.py --clase 58` da **LIBRE** y `--clase 59` da **SANEAMIENTO** |
| **`d075` y `d076`** | son las dos que anoto yo sobre tu vuelta: que las cuatro vecindades de la `57` se midieron con la tanda entera dentro, y que no pude reproducir sus cifras de similitud. **Se cobran el dia de la insercion. No las toques ahora** |
| **el alcance** | **decidido**: el mundo 11 cierra con cinco libros. `gerber_emyth` y `marquet_turn_the_ship` se quedan en bandeja con sus candidatos, sin insertar. **No los toques** |
| **la insercion del lote 7** | autorizacion del fundador, no default. `81` candidatos esperan con `0 CAERIAN`. **No bloquea tu extraccion** (`D.32`) y no la pidas como tarea |
| **la doctrina** | congelada en `11` (`D.56`). Pregunta nueva: **registrala con su medida y dejala ahi.** No abre parada y no va al banco. **Y dos de las que la `57` dejo abiertas ya estan adjudicadas** (`ACTA 56` `56.4.6` y `56.4.7`): no vuelven |
| **la maquinaria** | `D.45` veda `src/`, el banco, el arnes y los protocolos mientras corran frentes en paralelo. **Ni con una caida de dato: se declara, se para y sube al fundador** |
| **el modelo** | ya esta decidido en el comando de abajo. **No es tuyo de cambiar y no hay nada que discutir**: es la rama de salida del umbral del 21 sep, con su medida delante |

> **LO UNICO QUE TE BLOQUEA ES UNA GUARDA DE DATO EN ROJO**: `gate`, el cerrojo, el censo no
> decreciente, o la fidelidad `D.30` con puente. **Eso no es deuda: es averia.** **Las cuatro
> estaban en VERDE al cerrar la `57`** (`ACTA 56` `56.8`), medidas por el auditor.

## LA RELECTURA AL DOBLE QUE LA CAIDA DE LA `57` OBLIGA, CON SU TECHO PUESTO

`5.2` manda releer al doble el tramo de una caida de `REPORTE`, y `5.5` le pone techo. **El
tramo de esa caida no son los tres capitulos**, que estan verificados al digito: **es lo que el
reporte afirma sobre su propio proceso.** Asi que:

> **Antes de escribir en tu reporte que hiciste algo en un orden, en un momento o en un acto,
> PEGA LA SALIDA QUE LO FECHA.** Una afirmacion sobre tu propio proceso **se prueba igual que
> una cifra**, y la tuya de la `57` la desmintieron tus propios ficheros. **Si no tienes con que
> probarla, no la escribas: describe lo que hiciste y ya esta.**

**No hay nada mas que doblar, y el exceso no se inventa** (`5.5`, `7.G` de la cosecha: la
relectura tiene techo y una regla de castigo sin techo se come el trabajo que vigila).

---

## EL COMANDO DE ESTA CORRIDA, PARA QUE CONSTE

    RAMA=extraccion-mundo-11 MODO_INSERCION=cuarentena \
    MODELO_EXTRACTOR=claude-opus-5 MAX_VUELTAS=20 bash orquestador_forja.sh

**El auditor sigue en Opus 5**, a proposito: **quien mide no puede ser el medido.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.**
