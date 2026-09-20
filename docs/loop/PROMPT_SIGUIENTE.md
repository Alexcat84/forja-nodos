# ENCARGO DE LA VUELTA 56: **LA MEDICION CON SONNET**

*Linea **serial** (`extraccion-mundo-11`). Escrito al aplicar la decision del fundador del
21 sep 2026, archivada en `docs/loop/paradas/2026-09-21-el-precio-del-extractor-DECISION.md`.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: EXTRACCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO PRIMERO: **ESTA VUELTA TE MIDE A TI, Y LO SABES DE ENTRADA**

**Corres con `claude-sonnet-5`.** Las cinco vueltas anteriores las mino Opus 5, y sus
cifras estan escritas: **dos turnos de extractor a `20,69` y `24,89` USD**. **Tu turno se
compara con esos dos.**

> **NO ES UNA TRAMPA Y NO HAY NADA QUE DISIMULAR.** Lo que se mide es si el trabajo sale
> igual de bien mas barato. **Si sale peor, la cifra lo dira y no pasa nada**: el fundador
> ya escribio que en ese caso Grove se termina con Opus y se acepta el precio. **Lo unico
> que arruinaria la medicion es que recortes calidad para bajar el coste.**

### EL UMBRAL, ESCRITO ANTES DE MEDIR

| | |
|---|---|
| **pasos inventados por muestra** | **bajo el `10` por ciento** |
| **coste del turno** | **la mitad o menos** que el de Opus (`20,69` y `24,89`) |

**Si se cumplen los dos, GROVE SE TERMINA CON SONNET.** Si no, **se termina con Opus**.

---

## LO QUE HA CAMBIADO, Y TE TOCA A TI

**La fase ciega, el sello y el testigo YA NO CORREN en `cuarentena`** (`D.58`, que estaba
escrita desde el 19 y **no habia llegado al codigo hasta hoy**). Tu vuelta va:
**extractor, auditor directo, acta corta.** Sin apertura ciega en medio.

---

## TAREA 1. **LA FRONTERA, ANTES DE CORTAR NADA**

    minados: cap_01 1, cap_02 7, cap_03 15, cap_04 22, cap_05 12,
             cap_06 8, cap_07 9, cap_10 1        (75 candidatos, 8 de 18)

**Mina `cap_08`, `cap_09` y cierra `cap_10`**, que quedo en `1`. Publica la frontera de
cada unidad y **cierrala contra el cuerpo**: la suma de las filas da el `wc -w`, **cero
lineas sin cubrir y cero solapes**. Si una no cierra, **esa unidad no se mina**.

**La tabla va pegada de su instrumento** (`D.41`).

## TAREA 2. **MINAR, CON EL TECHO POR DELANTE**

- **Techo: `30` candidatos.** Si los tres capitulos dan mas, **cierras donde llegues y lo
  declaras con su cifra**.
- **Un candidato por vez y en el orden del libro**, y cada uno por
  `python forja.py informe <candidato>` **en el acto de escribirlo**.
- **CERO INSERCIONES.** El lote 7 esta ABIERTO y `D.39` no deja entrar nada.
- **Las aristas que la señal no levanta se declaran por lectura** (`D.29`) con su razon
  escrita, **y se cablean el dia de la insercion**.

## TAREA 3. **LA FIDELIDAD, POR MUESTRA Y CON SU SEMILLA**

> # **LA SEMILLA DE ESTA VUELTA ES `v56`.**

    python scripts/muestra_fidelidad.py --libro grove_high_output \
           --capitulos cap_08,cap_09,cap_10 --semilla v56

**Reparte el instrumento, no tu.** Pega su salida: quien te audite vuelve a correrlo con
la misma semilla y **tiene que salirle la misma lista**.

> **EL DISPARADOR:** si la muestra de un capitulo **pasa del `10` por ciento de pasos
> inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.** Y esa misma cifra es **una
> de las tres que deciden si Grove sigue contigo.**

## TAREA 4. **LAS TRES CIFRAS DE LA MEDICION, EN SU PROPIA SECCION**

**Al lado de las de Opus, y cada una con su instrumento** (`D.59`: una media, un
porcentaje o una razon **las imprime un instrumento con su numerador y su denominador
nombrados**):

| # | la cifra | contra que se compara |
|---:|---|---|
| **1** | **coste de tu turno de extractor**, citado de `docs/loop/loop.log` | `20,69` y `24,89` de Opus |
| **2** | **pasos inventados por muestra**, por capitulo | el tope es `10` por ciento |
| **3** | **candidatos que la aduana en seco bloquearia** | el informe de cada candidato, contado |

**La `3` la tienes gratis:** cada `forja.py informe` te dice si ese candidato entraria o
bloquearia. **Cuentalos y publica la razon.**

---

## LO QUE NO ES TAREA TUYA

| | |
|---|---|
| **la deuda** | lo que quede pendiente. **La proxima de saneamiento la dira el arnes**, y no deja que el encargo diga otra cosa |
| **el alcance** | **decidido**: el mundo 11 cierra con cinco libros. `gerber_emyth` y `marquet_turn_the_ship` **se quedan en bandeja con sus `19`**, sin insertar. No los toques |
| **la doctrina** | congelada. Pregunta nueva: **registrala con su medida y dejala ahi** |

> **LO UNICO QUE TE BLOQUEA ES UNA GUARDA DE DATO EN ROJO**: `gate`, el cerrojo, el censo
> no decreciente, o la fidelidad `D.30` con puente. **Eso no es deuda: es averia.**

## AL CERRAR

    python forja.py gate
    python forja.py guiones
    python scripts/cerrar_reporte.py
    python forja.py tablero --escribir

**Acta corta** (`D.58`), **con la seccion de las tres cifras dentro**. Y **la linea del
tramo**, sea cual sea el numero, incluido `0`.

## EL COMANDO DE ESTA CORRIDA, PARA QUE CONSTE

    RAMA=extraccion-mundo-11 MODO_INSERCION=cuarentena \
    MODELO_EXTRACTOR=claude-sonnet-5 MAX_VUELTAS=20 bash orquestador_forja.sh

**El auditor sigue en Opus 5**, a proposito: **quien mide no puede ser el medido.**
