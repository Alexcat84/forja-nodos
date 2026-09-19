# ENCARGO DE LA VUELTA 53: **REGIMEN LIGERO, TRES CAPITULOS DE UNA**

*Linea **serial** (`extraccion-mundo-11`). Escrito al aplicar la decision del fundador del
19 sep 2026, archivada en `docs/loop/paradas/2026-09-19-dos-regimenes-DECISION.md`.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: EXTRACCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## **ESTO ES NUEVO: HAY DOS REGIMENES, Y ESTAS EN EL LIGERO** (`D.58`)

**LA LINEA QUE LOS SEPARA ES UNA SOLA: si el dato existe ya.** En extraccion **nada toca el
grafo**: tus candidatos se quedan en su bandeja y `D.39` no los deja entrar hasta que el
lote cierre. **Un candidato mal leido aqui no ha hecho daño todavia.**

| | el ligero, que es el tuyo |
|---|---|
| **cuanto minas** | **TRES capitulos por vuelta**, techo de **`30` candidatos** |
| **las guardas** | **tallado y censo**, que son baratos. **Sin fase ciega, sin sello y sin testigo** |
| **la fidelidad** | **por MUESTRA**, y abajo tienes la tuya con su semilla |
| **el objetivo** | **turno por debajo de `5` USD** |

> **LO QUE NO SE AFLOJA, Y CONVIENE QUE SE LEA:** la relectura **no se quita, se mueve**.
> `D.58` la hace **ENTERA en la vuelta de insercion**, sobre los candidatos que entran, **y
> por eso ningun paso entra al grafo sin haber sido leido contra su libro una vez.**
> Releerlos dos veces cuesta el doble y protege lo mismo.

---

## TAREA 1. **LA FRONTERA DE LOS TRES, ANTES DE CORTAR NADA**

**`cap_06`, `cap_07` y `cap_08`.** Publica la frontera de cada uno y **cierrala contra el
cuerpo**: la suma de las filas da el `wc -w` del cuerpo, **cero lineas sin cubrir y cero
solapes**. **Si una no cierra, esa unidad no se mina.**

**LA TABLA VA PEGADA DE SU INSTRUMENTO** (`D.41`), y el tallado la compara celda a celda.

## TAREA 2. **MINAR, CON EL TECHO POR DELANTE**

- **Techo: `30` candidatos en la vuelta.** Si los tres capitulos dan mas, **cierras donde
  llegues y lo declaras con su cifra**.
- **Un candidato por vez y en el orden del libro.**
- **Cada uno pasa por `python forja.py informe <candidato>` en el acto de escribirlo.**
- **CERO INSERCIONES.** El lote 7 esta ABIERTO: `D.39` no deja entrar nada.
- **Las aristas que la señal no levanta se declaran por lectura** (`D.29`) **con su razon
  escrita**, y **se cablean el dia de la insercion**, no hoy.

## TAREA 3. **LA FIDELIDAD, POR MUESTRA Y CON SU SEMILLA**

> # **LA SEMILLA DE ESTA VUELTA ES `v53`, Y SE ESCRIBE EN EL REPORTE.**

**En cuanto los tres capitulos esten minados**, corre:

    python scripts/muestra_fidelidad.py --libro grove_high_output \
           --capitulos cap_06,cap_07,cap_08 --semilla v53

**El instrumento reparte, y no lo eliges tu:** uno de los tres **se relee ENTERO**, y los
otros dos llevan **una muestra de `15` pasos cada uno**. **Pega su salida** en el reporte:
quien te audite vuelve a correrlo con la misma semilla y **tiene que salirle la misma
lista**.

> **Una muestra que no se puede reproducir no es una muestra: es una eleccion**, y el que
> elige sus pasos elige su resultado.

**PUBLICA `PASOS INVENTADOS` POR CAPITULO**, los tres, diciendo cual es de muestra y cual
entero.

> ### **EL DISPARADOR, Y ES OBLIGATORIO**
>
> **Si la muestra de un capitulo pasa del `10` por ciento de pasos inventados, ESE
> CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.** El tope de `D.30` no se afloja: lo que
> cambia es que aqui se mide sobre `15` pasos, **y por eso escala a relectura entera en
> vez de a veredicto.**

---

## LO QUE NO ES TAREA TUYA

| | |
|---|---|
| **la deuda** | `19` pendientes. **No la pagues hoy.** **La vuelta 54 SERA de saneamiento**, y ya no depende de que nadie se acuerde: el arnes lo comprueba al abrir y **no deja que el encargo diga otra cosa** |
| **los `6` de `d005`** | son de `cap_03` y se reparan **antes de insertar**, no antes de minar |
| **la doctrina** | congelada en `11`. Pregunta nueva: **registrala con su medida y dejala ahi** |

> **LO UNICO QUE TE BLOQUEA ES UNA GUARDA DE DATO EN ROJO**: `gate`, el cerrojo, el censo
> no decreciente, o la fidelidad `D.30` con puente. **Eso no es deuda: es averia.**

## AL CERRAR

    python forja.py gate
    python forja.py guiones
    python scripts/cerrar_reporte.py
    python scripts/tabla_de_cierre.py --escribir      y se pega su salida
    python forja.py tablero --escribir

**Un acta corta** (`D.58`): la frontera al digito, el cotejo de la muestra, pasos
inventados por capitulo, y nada mas. **Lo que el registro ya dice no se repite** (`D.47`).

**Y ESCRIBE LA LINEA DEL TRAMO**, sea cual sea el numero, incluido `0`.

## LO QUE NO SE TOCA

- **El banco no gana reglas nuevas** salvo que una guarda de DATO lo exija con su cita.
- **`config/frentes.json` y `config/umbrales.json`** se leen, no se editan.
- **El bucle no funde ramas y el bucle no crea remotos.**
