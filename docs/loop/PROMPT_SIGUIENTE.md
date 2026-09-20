# ENCARGO DE LA VUELTA 54: **SANEAMIENTO EN REGIMEN LIGERO**

*Linea **serial** (`extraccion-mundo-11`). Escrito al aplicar la decision del fundador del
20 sep 2026, archivada en
`docs/loop/paradas/2026-09-20-la-media-la-calcula-el-instrumento-DECISION.md`.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: SANEAMIENTO**
>
> *No la elegi yo: la impuso la cadencia. `python scripts/deuda.py --clase 54` dice
> `SANEAMIENTO`, con `5` vueltas desde la `49` y `19` deudas pendientes, y desde `D.58`
> **el arnes no deja que el encargo diga otra cosa.** Lo intente y me paro.*
>
> **REGIMEN Y CLASE SON COSAS DISTINTAS:** el regimen es `MODO_INSERCION=cuarentena` y
> empieza HOY; la clase es lo que la vuelta hace dentro de el. **Esta paga deuda, y la
> siguiente mina.**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO PRIMERO: **ESTA VUELTA ES UNA MEDICION, Y LA CIFRA ERES TU**

**El regimen ligero de `D.58` se escribio ayer y todavia no existe como cifra.** Las
vueltas `52` y `53` corrieron con `MODO_INSERCION=insertar`, asi que arrastraron **fase
ciega, sello y testigo** aunque `D.58` los quite. **Esta es la primera que corre de verdad
en ligero.**

| | |
|---|---|
| **objetivo escrito** | **turno por debajo de `5` USD** |
| **el contraste** | el turno del auditor de la `53` costo **`12,77`** |
| **si tras DOS vueltas el turno sigue por encima de `8`** | **el auditor lo declara con el desglose de en que se va, y el bucle se para para revisarlo** |

**El arnes publica el coste de cada turno en `docs/loop/loop.log`.** No hace falta que lo
midas tu: **hace falta que lo cites.**

---

## LO SEGUNDO, Y CAMBIA COMO ESCRIBES: **`D.59`**

> **TODA MEDIA, PORCENTAJE, RAZON O DIFERENCIA LA IMPRIME UN INSTRUMENTO, con su
> numerador y su denominador NOMBRADOS. Una cifra derivada a mano de dos celdas no se
> publica.**

**El tallador lo comprueba en cada commit**, sobre **la vuelta viva** y **por parrafo**:
una frase con cifra derivada **cuyo parrafo no nombre su instrumento** tumba el commit,
nombrando la frase.

**LA CAIDA QUE LA OBLIGO ES DE TU ANTECESOR Y ES FINA:** publico `media por pasada CON
reloj: 517,7 s` con **`11` pasadas en el numerador y `9` en el denominador**. `4659,0` es
cierto y `9` es cierto; **lo falso es que uno sea el numerador del otro**. La caida real
por pasada era **`42,1` por ciento**, no `29,2`.

> **NO ES MAS TRABAJO: ES OTRO SITIO.** Si vas a publicar una media, **escribe el
> instrumento que la calcula** y pega su salida. Si la cifra ya la imprime un instrumento
> tuyo, **nombralo en el mismo parrafo** y ya esta.

---

## LA TAREA: **PAGAR LA DEUDA, Y NO MINAR NADA**

    python scripts/deuda.py        las 19, con su cita y su vuelta de origen

**UNA VUELTA DE SANEAMIENTO NO INSERTA NI MINA** (`D.55`). Su trabajo es **saldar lo que
esta escrito**, y cada pago se anota:

    python scripts/deuda.py --pagar <id> --vuelta 54 --como "..."

### EL ORDEN QUE PROPONGO, Y PUEDES CAMBIARLO SI LO DICES

1. **Las cuatro de `grove`** (`d001` a `d004`): dos cifras mal derivadas, un rotulo y un
   paso que hay que reescribir antes de que pase la aduana. **Son las mas viejas** y
   vienen de otra mano.
2. **`d005`**, que no se paga hoy pero **se relee**: nombra los `6` candidatos de `cap_03`
   que la aduana en seco de grove bloquearia. **Esos `6` deciden que entra el dia de la
   insercion**, asi que conviene tenerlos nombrados y medidos.
3. **`d058`**, que el auditor levanto y **mide algo que se cobrara el dia de la
   insercion**: el `resumen_teorico` es del `70,3` al `83,1` por ciento del texto que la
   señal `1` compara.
4. **Lo demas, por orden de vuelta de origen.**

> **LO QUE NO SE PAGA SE DECLARA.** Si una deuda no se puede saldar en esta vuelta, **di
> por que y dejala abierta**: una deuda cerrada sin arreglar es peor que una abierta.

### Y LA PREGUNTA `11` DE LA COLA, QUE ESTA VUELTA TIENE ENCARGADA

**`config/frentes.json` la dejo encargada a la vuelta de saneamiento que tocara, y esta es
la que toca:**

> *Un defecto en `dataset/` que NO es una cifra falsa ni un veredicto mal puesto.
> **Clasificalo CON UN EJEMPLAR DELANTE:** si existe una tercera especie de defecto de
> dato, **las cuatro guardas de `deuda.py` tienen que saber su nombre.***

---

## TAREA 4. **EL ACTA CORTA, Y EL COSTE DENTRO**

**Lo pagado con su id, lo que queda abierto con su motivo, la clasificacion de la pregunta
`11`, y el coste del turno citado del log.** Nada mas. **Lo que el registro ya dice no se repite** (`D.47`).

---

## LO QUE NO ES TAREA TUYA

| | |
|---|---|
| **la deuda** | `19` pendientes. **La vuelta 58 sera de saneamiento** (cinco desde la `53`), y el arnes **no deja que el encargo diga otra cosa** |
| **los `6` de `d005`** | se reparan **antes de insertar**, no antes de minar |
| **la doctrina** | congelada en `11`. Pregunta nueva: **registrala con su medida y dejala ahi** |

> **LO UNICO QUE TE BLOQUEA ES UNA GUARDA DE DATO EN ROJO**: `gate`, el cerrojo, el censo
> no decreciente, o la fidelidad `D.30` con puente. **Eso no es deuda: es averia.**

## AL CERRAR

    python forja.py gate
    python forja.py guiones
    python scripts/cerrar_reporte.py
    python forja.py tablero --escribir

**Y ESCRIBE LA LINEA DEL TRAMO**, sea cual sea el numero, incluido `0`.

## LO QUE NO SE TOCA

- **El banco no gana reglas nuevas** salvo que una guarda de DATO lo exija con su cita.
- **`config/frentes.json` y `config/umbrales.json`** se leen, no se editan.
- **El bucle no funde ramas y el bucle no crea remotos.**
