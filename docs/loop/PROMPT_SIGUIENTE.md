# ENCARGO DE LA VUELTA 55: **VOLVER A MINAR, Y EMPEZAR POR EL CAPITULO QUE EL TABLERO TE VA A MANDAR SALTAR**

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor en la `ACTA 53`, que audito la
vuelta `54`. Modo austero (`D.47`): lo que el registro ya dice no se repite.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: EXTRACCION**
>
> *No la elijo yo, la imprime el instrumento:*
>
>     $ python scripts/deuda.py --clase 55
>     LIBRE
>       van 1 de 5 desde la ultima de saneamiento (la 54), con 19 deuda(s) esperando
>
> *Y el tablero confirma que esta linea puede tomar el libro:*
>
>     $ python forja.py tablero --puedo grove_high_output
>     LINEA 'serial', LIBRO 'grove_high_output': SI

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## TAREA 1. **LOS REGISTROS DE LA `ACTA 53`, RECOGIDOS SIN REABRIRLOS**

| # | lo adjudicado | donde vive | que haces con ello |
|---:|---|---|---|
| `1` | de tus `10` discutibles **se sostienen `9` y CAE el `1`** | `ACTA 53` `53.4` | **recoger.** Y volver a marcar antes de saber si aciertas (`EXTRACTOR.md` 8) |
| `2` | la pregunta `11`: **el ejemplar SI tiene casillero y es `DATO MOVIDO`**, que ya lo cobro en la `ACTA 38` `6` | `53.6` | **recoger y NO reabrir.** `D.56` sigue congelando la cola en `11` |
| `3` | `rehacer_flujo_paso_limitante_capacidad` **CONTINUA de** `construir_flujo_produccion_paso_limitante`, **no es duplicado** | `53.5` | **recoger.** Es una lectura menos de las `17` el dia de la insercion |
| `4` | tus dos caidas de prosa (`.v54/deuda_cierre.txt` con dos salidas, y `575` de `577`) **registran y NO acumulan** | `53.7` | **recoger.** No hay nada que pagar |
| `5` | `d033`, `d047`, `d024`, `d058`, `d007` y `d068`: **reproducidos al digito** | `53.1` | **recoger.** Tus pagos aguantan |
| `6` | **la caida propia del auditor**: `rancios 4` donde el instrumento imprime `RANCIO 71` | `53.11` | **recoger.** Es mia, no tuya, y va corregida sin borrar |

**Y DOS DEUDAS NUEVAS, ESCRITAS POR EL AUDITOR Y NO POR TI:** `d071` (el arnes hace fase ciega,
sello y testigo que `D.58` quita del ligero) y `d072` (el par que ninguna senial levanta por
ninguno de sus dos extremos). **Ninguna de las dos es trabajo tuyo hoy.**

---

## TAREA 2. **LA TRAMPA QUE TIENES QUE ESQUIVAR ANTES DE ESCRIBIR UN SOLO CANDIDATO**

> ## **`cap_07` ESTA EN `1` DE `9`, Y EL TABLERO TE VA A MANDAR SALTAR A `cap_08`.**

**No lo adivines: esta medido, y el que lo dice es el instrumento.**

    $ python forja.py tablero --puedo grove_high_output
    ... se continua desde el capitulo siguiente al ultimo minado (cap_07), citando su frontera

    $ ls cuarentena/grove_high_output/*.json | wc -l
    65
    (de esos, 1 solo es de cap_07: planificar_tres_pasos_demanda_estado_brecha)

**Y LA FRONTERA DE `cap_07` LA PUBLICO LA VUELTA `53`, CON SU CIFRA:**

    NODOS QUE MI FRONTERA DA EN ESTA UNIDAD, cap_07 Y SOLO cap_07: 9

**Saltar a `cap_08` dejaria `8` nodos atras.** Es `d028` al pie de la letra (*`src/tablero.py`
publica en `capitulos_minados` los que estan **parcialmente** minados*), que la `ACTA 45`
desentierra y que **sigue pendiente porque `D.45` veda `src/`**.

> **LO QUE HACES:** abres por **`cap_07`**, no por `cap_08`, **y lo declaras en tu reporte con
> la cifra de arriba delante.** Si tu propio recuento te da otra cosa, **declara la
> discrepancia y no la resuelvas copiando** (`EXTRACTOR.md` 5).

**Y `cap_08` YA ESTA CERRADO POR SU FRONTERA, no por olvido:** su frontera de la vuelta `53` le
da `0` nodos, y la `ACTA 52` `52.3.a` adjudico que ese `0` es correcto. **No lo reabras.**

---

## TAREA 3. **EL TRAMO: `cap_07` HASTA CERRARLO, Y LUEGO `cap_09` Y `cap_10` SI EL TECHO LLEGA**

**Tres capitulos por vuelta y techo de `30` candidatos**, que es lo que la decision del fundador
del 20 sep fijo para el regimen ligero. **`cap_07` cuenta como el primero de los tres.**

| | |
|---|---|
| **`cap_07`** | cerrar los **`8`** que le faltan de los `9` de su frontera |
| **`cap_09` y `cap_10`** | **frontera publicada ANTES de cortar nada** (`EXTRACTOR.md` 10), tramo a tramo contra el fichero, con `0` lineas sin cubrir y `0` solapes, y **cada fila con los nodos que preve** |
| **el techo** | `30` candidatos. **Si un solo capitulo lo pasa, la vuelta cierra ahi y lo DECLARA con su cifra** (`EXTRACTOR.md` 12.4). Una vuelta que cierra corto **y no lo dice** es caida de `REPORTE` |

**EL VOLUMEN NO SUBE NI BAJA, Y EL MOTIVO ESTA MEDIDO:** la `ACTA 53` `53.2` publica la fila por
capitulo de la vuelta `54` y sale **SIN SUPERFICIE** (`0` pasos escritos), asi que **la cifra que
dimensiona sigue siendo la de la `ACTA 52`**: `0,0` por ciento en `cap_06`, `cap_07` y `cap_08`,
**ninguna fila por encima del tope de `10`**.

---

## TAREA 4. **LA FIDELIDAD `D.30` Y LA MUESTRA CON SU SEMILLA ESCRITA**

**Esta vuelta SI escribe pasos, asi que `D.30` vuelve a tener superficie** y deja de declararse
sin objeto como en la `54`.

    python scripts/muestra_fidelidad.py --libro grove_high_output --capitulos cap_07,cap_09,cap_10 --semilla v55

- **La semilla se escribe en el reporte**, porque el auditor la vuelve a correr y **si le sale
  una lista distinta, es caida de cifra** (`D.58`).
- **Si la muestra de un capitulo pasa del `10` por ciento de pasos inventados, ese capitulo se
  relee ENTERO antes de seguir.** No es recomendacion: es la escalada.
- **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo y no una media de vuelta**, con su
  numerador y su denominador nombrados (`D.59`).

---

## TAREA 5. **EL CIERRE, Y EL COSTE DENTRO, PORQUE ESTA VEZ SI DECIDE**

> ## **EL DISPARADOR DE COSTE VA POR `1` DE `2`. LEELO ANTES DE EMPEZAR.**
>
> El encargo de la `54` lo escribio asi: ***si tras DOS vueltas el turno sigue por encima de `8`
> USD, el auditor lo declara con el desglose y el bucle se para para revisarlo.***
>
> **La `54` fue la primera y paso**: `20,6911` USD el turno de extractor, `6,8138` el de auditor
> ciego, medidos por `.v55aud/coste_corrida.py` sobre `docs/loop/loop.log`.
>
> **Si tu turno vuelve a pasar de `8`, la condicion escrita se cumple.** No te pido que gastes
> menos de lo que el trabajo cuesta: **te pido que sepas que esta contado**, y que si lo pasas,
> tu reporte diga **en que se fue**. El desglose de la `54` esta en `ACTA 53` `53.10` y el
> sumando que domina no es lo que el turno escribe: **son los `149` turnos internos y los
> `28.614.782` tokens de lectura de cache que arrastran.**

Al cerrar:

    python forja.py gate
    python forja.py guiones
    python scripts/cerrar_reporte.py
    python forja.py tablero --escribir

- **El estado recomputado al cierre, no copiado de la apertura** (`EXTRACTOR.md` 4).
- **La linea del tramo, sea cual sea el numero, incluido `0`.**
- **Tus discutibles marcados ANTES de saber si aciertas** (`EXTRACTOR.md` 8). La `54` marco
  `10` y `9` se sostuvieron: **el marcado esta funcionando, no lo encojas.**
- **La tabla de cierre de `D.52` con la cabecera que el instrumento busca**, y vuelta a correr
  despues de escribirla: `d022` dice que con otra cabecera el instrumento **regenera y da VERDE
  sobre la tabla de una vuelta anterior sin decirlo.**

---

## LO QUE NO ES TAREA TUYA

| | |
|---|---|
| **la deuda** | `19` pendientes. **La `59` es la de saneamiento**, no la `58`, y lo dice el instrumento (`d068` ya declaro la discrepancia). **El arnes no deja que el encargo diga otra cosa** |
| **`d071`** | el arnes es sede vedada por `D.45`. **Sube al fundador, no se toca** |
| **`d072` y los `17` vecindades de `cap_02`** | se cablean **el dia de la insercion**, no hoy |
| **los `6` de `d005`** | se reparan **antes de insertar**, y esta vuelta no inserta |
| **la doctrina** | congelada en `11` (`D.56`). Pregunta nueva: **registrala con su medida y dejala ahi** |
| **`config/frentes.json` y `config/umbrales.json`** | se leen, no se editan |

> **LO UNICO QUE TE BLOQUEA ES UNA GUARDA DE DATO EN ROJO** (`D.55`): `gate`, el cerrojo, el
> censo no decreciente, o la fidelidad `D.30` con puente. **Y solo esas cuatro.** La prueba de
> aceptacion **no** es una de ellas y hoy cierra con `2` fallos de `339`, anotados como `d067`
> y vedados por `D.45`: **declaralos y sigue.**

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.**
