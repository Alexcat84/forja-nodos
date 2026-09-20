# ENCARGO DE LA VUELTA 57: **GROVE SIGUE CON SONNET, Y AHORA SE MIDE MINANDO**

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 55`, que
audito la vuelta `56`. `AUDITOR_FORJA.md` seccion `1.4`.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: EXTRACCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO PRIMERO: **LA MEDICION SALIO A TU FAVOR, Y ESO CAMBIA UNA COSA Y SOLO UNA**

**El umbral escrito se cumplio en sus dos condiciones** (`ACTA 55` `55.5`): tu turno de la `56`
costo **`8,2132` USD** contra `20,6911` y `24,8943` de Opus, o sea **`0,40` y `0,33`** de su
precio, y los pasos inventados por muestra dieron **`0,0` por ciento**. Asi que se aplica lo que
el fundador ya habia escrito el 21 sep: **GROVE SE TERMINA CON SONNET.**

> **LO QUE ESO NO SIGNIFICA, y va aqui porque es la unica trampa de esta vuelta:** la `56` cerro
> con **cero candidatos nuevos**, porque `cap_08` y `cap_09` no tenian nada que extraer. **Tu
> coste barato todavia no se ha medido en una vuelta que COSECHA.** Esta vuelta es esa medida.
>
> **NO ES UNA AMENAZA Y NO HAY NADA QUE DISIMULAR.** Si minar `cap_11` y `cap_12` te cuesta el
> doble que leer `cap_08`, eso es lo normal y la cifra lo dira. **Lo unico que arruinaria la
> medicion es que recortes lectura para que el numero salga bonito.** La `ACTA 55` verifico al
> digito que la `56` no lo hizo: leyo `6718` palabras, publico `75` filas de frontera que cuadran
> y se nego a fabricar un nodo de una pregunta retorica. **Ese es el listón.**

## LO SEGUNDO: **DONDE ESTAS, MEDIDO Y NO SUPUESTO**

    minados y cerrados por su frontera: cap_01 a cap_10, los diez
    cosecha en bandeja: cap_02 7, cap_03 15, cap_04 22, cap_05 12,
                        cap_06 8, cap_07 9, cap_10 1   (74 candidatos)
    cap_01, cap_08 y cap_09: leidos enteros con cosecha CERO, y es correcto
    faltan: cap_11 a cap_18, ocho unidades

**`LA VUELTA 57 ABRE EN `cap_11`.** El tablero solo puede ver `cap_10` como *ult cap* porque lee
el capitulo mas alto CITADO por un candidato, y `cap_08` y `cap_09` no tienen ninguno que cite.
**Eso no significa que esten sin minar: estan minados, cerrados y auditados** (`ACTA 55` `55.3.b`
y `55.3.c`). **No los vuelvas a abrir.**

## LO TERCERO: **EL TRAMO SE QUEDA EN TRES CAPITULOS, Y DIGO POR QUE NO SUBE**

`8.1` permitiria subir un escalon porque la cifra bajo. **No sube**, y la razon esta escrita en
`ACTA 55` `55.2`: el `0,0` por ciento de la `56` sale de **`8` pasos de `1` candidato**. Una cifra
buena sobre una base de `8` no es permiso para mover volumen. **Tres capitulos: `cap_11`,
`cap_12` y `cap_13`.**

---

## TAREA 1. **LA FRONTERA, ANTES DE CORTAR NADA** (`EXTRACTOR.md` 10)

**Mina `cap_11`, `cap_12` y `cap_13`.** Publica la frontera de cada unidad y **cierrala contra el
cuerpo**: la suma de las filas da el cuerpo medido aparte, **cero lineas sin cubrir y cero
solapes**. Si una no cierra, **esa unidad no se mina.**

- **Reusa `.v56ext/frontera.py`** y no fabriques instrumento nuevo (`EXTRACTOR.md` 13, `D.47`).
- **La tabla va pegada de su instrumento** (`D.41`), con la cita de cada linea impresa y no
  prometida (`D.35`).
- **Y NO ESCRIBAS *ni una linea de maquinaria tocada* SI TOCAS EL BLOQUE QUE IMPRIME.** La `56`
  lo escribio y cambio `4` lineas por `7` en el bloque del techo (`ACTA 55` `55.6.a`). **El
  cambio estaba bien; la frase no.** Di lo que cambiaste y por que: **lo que la moratoria protege
  es lo que MIDE, no lo que IMPRIME.**

## TAREA 2. **MINAR, CON EL TECHO POR DELANTE**

- **Techo: `30` candidatos.** Si los tres capitulos dan mas, **cierras donde llegues y lo
  declaras con su cifra** (`EXTRACTOR.md` 12.4: cuando los dos techos chocan manda el de
  candidatos, y el cierre corto **se declara** o es caida de `REPORTE`).
- **Un candidato por vez y en el orden del libro**, y cada uno por
  `python forja.py informe <candidato>` **en el acto de escribirlo**.
- **CERO INSERCIONES.** El lote 7 esta ABIERTO y `D.39` no deja entrar nada.
- **Las aristas que la señal no levanta se declaran por lectura** (`D.29`) con su razon escrita, y
  se cablean el dia de la insercion.
- **Un cero es un resultado legitimo y no hace falta defenderlo de mas** (la `56` lo hizo bien):
  si un capitulo es relato, definicion o postura, **lo dices con su frontera cerrada al lado y ya
  esta.** `EXTRACTOR.md` 15.4 y `9.1` son las reglas que te cubren, **y las dos restricciones se
  citan por su numero**: la `1` tumba inventarios de FINES, la `2` tumba el adjetivo de
  adecuacion en el sitio del criterio. **No son intercambiables** (`ACTA 55` `55.3.b`).

## TAREA 3. **LA FIDELIDAD, POR MUESTRA Y CON SU SEMILLA**

> # **LA SEMILLA DE ESTA VUELTA ES `v57`.**

    python scripts/muestra_fidelidad.py --libro grove_high_output \
           --capitulos cap_11,cap_12,cap_13 --semilla v57

**Reparte el instrumento, no tu.** Pega su salida: quien te audite vuelve a correrlo con la misma
semilla y **tiene que salirle la misma lista** o es caida de cifra (`D.58`).

> **EL DISPARADOR:** si la muestra de un capitulo **pasa del `10` por ciento de pasos inventados,
> ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.**

**Y LA FILA LLEVA SU DENOMINADOR AL LADO** (`D.59`): `0` de `8` y `0` de `53` no son la misma
prueba, y la cifra sin su base no deja decidir volumen.

## TAREA 4. **EL PRECIO DE SONNET MINANDO, QUE ES LA CIFRA QUE ESTA VUELTA AÑADE**

**Es la mitad que faltaba de la medicion del 21 sep.** Publica en su propia seccion, cada una con
su instrumento:

| # | la cifra | contra que se compara |
|---:|---|---|
| **1** | **candidatos escritos** y **capitulos cerrados** | `0` y `3` de la vuelta `56` |
| **2** | **pasos inventados por muestra, por capitulo, con su denominador** | el tope es `10` por ciento |
| **3** | **candidatos que la aduana en seco bloquearia**, contados de cada `informe` | `0` de `1` en la `56`, `0` de `9` en la `55` |
| **4** | **tu coste**, y **NO lo inventes**: el arnes lo escribe en `docs/loop/loop.log` cuando tu turno cierre | `8,2132` de la `56` (sin cosecha) y `24,8943` de Opus en la `55` (con `9` candidatos) |

**LA `4` NO LA PUEDES MEDIR Y NO TIENES QUE INTENTARLO.** La `56` lo declaro bien: *no existe
todavia y no lo invento*. **Lo que SI te toca es dejar el desglose de en que se fue**, que es lo
que `D.56` pide.

## TAREA 5. **EL CIERRE**

    python forja.py gate
    python forja.py guiones
    python tests/test_aceptacion.py
    python scripts/cerrar_reporte.py
    python forja.py tablero --escribir

**Acta corta del reporte** (`D.47`, `D.58`), con:

- el estado recomputado al cierre y **no copiado de la apertura**;
- **la tabla de cierre de tareas** (`D.52`), archivando y sellando la de la `56` por
  `git hash-object` antes de sobrescribir su fichero (`d030`, el remedio a mano que ya funciona
  cuatro veces);
- **tus discutibles marcados ANTES de saber si aciertas** (`EXTRACTOR.md` 8), que es lo unico que
  hace informativa la metrica de credito;
- **la linea del tramo**, sea cual sea el numero, incluido `0`.

---

## LO QUE NO ES TAREA TUYA, Y LO DIGO PARA QUE NO GASTES TURNO EN ELLO

| | |
|---|---|
| **la deuda** | `17` pendientes, `27` pagadas. **`d067` y `d071` las pague yo en la `ACTA 55` `55.7`** con su evidencia: las pago el fundador en el commit `e5b7b9d`, yo solo lo comprobe. **La proxima de saneamiento es la `59`** y el arnes no deja que el encargo diga otra cosa |
| **d067** | **NO la vuelvas a declarar PENDIENTE.** Esta pagada, y afirmar lo contrario es lo que le costo a la `56` su escalon de `REPORTE` (`ACTA 55` `55.6`). Si `tests/test_aceptacion.py` sale verde, sale verde **porque las dos pruebas estan reparadas**, no porque no se dispare nada |
| **el alcance** | **decidido**: el mundo 11 cierra con cinco libros. `gerber_emyth` y `marquet_turn_the_ship` se quedan en bandeja con sus candidatos, sin insertar. **No los toques** |
| **la insercion del lote 7** | autorizacion del fundador, no default. `74` candidatos esperan con `0 CAERIAN`. **No bloquea tu extraccion** (`D.32`) y no la pidas como tarea |
| **la doctrina** | congelada en `11` (`D.56`). Pregunta nueva: **registrala con su medida y dejala ahi.** No abre parada y no va al banco |
| **la maquinaria** | `D.45` veda `src/`, el banco, el arnes y los protocolos mientras corran frentes en paralelo. **Ni con una caida de dato: se declara, se para y sube al fundador** |

> **LO UNICO QUE TE BLOQUEA ES UNA GUARDA DE DATO EN ROJO**: `gate`, el cerrojo, el censo no
> decreciente, o la fidelidad `D.30` con puente. **Eso no es deuda: es averia**, y una averia se
> arregla antes de seguir. **Las cuatro estaban en verde al cerrar la `56`** (`ACTA 55` `55.13`).

## LA RELECTURA AL DOBLE QUE LA CAIDA DE LA `56` OBLIGA, CON SU TECHO PUESTO

`5.2` manda releer al doble el tramo de una caida de `REPORTE`, y `5.5` le pone techo. **El tramo
de esa caida NO son los tres capitulos**, que estan verificados al digito: **es lo que el reporte
dice sobre el estado de los registros.** Asi que:

> **Antes de escribir una sola linea sobre `DEUDA.jsonl`, `CREDITO_serial.jsonl` o el estado de una
> guarda, CORRE el instrumento que lo dice y pega su salida.** Y si tu frase explica **por que**
> una cifra sale como sale, **esa frase tambien se comprueba**: la cifra puede ser cierta y la
> explicacion falsa, que es exactamente lo que paso.

**No hay nada mas que doblar, y el exceso no se inventa** (`5.5`, 7.G de la cosecha: la relectura
tiene techo y una regla de castigo sin techo se come el trabajo que vigila).

---

## EL COMANDO DE ESTA CORRIDA, PARA QUE CONSTE

    RAMA=extraccion-mundo-11 MODO_INSERCION=cuarentena \
    MODELO_EXTRACTOR=claude-sonnet-5 MAX_VUELTAS=20 bash orquestador_forja.sh

**El auditor sigue en Opus 5**, a proposito: **quien mide no puede ser el medido.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.**
