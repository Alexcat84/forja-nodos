LIBRO DE ESTA VUELTA: marquet_turn_the_ship

# ENCARGO DE LA VUELTA 6 DEL FRENTE `marquet_turn_the_ship`: **`cap_16` Y `cap_17`, EL BARRIDO DE `d104` Y EL CIERRE DEL LIBRO**

*Linea **`marquet_turn_the_ship`** (`extraccion-marquet_turn_the_ship`, worktree
`C:/Users/AlexDesk/Documents/forja-marquet_turn_the_ship`). Escrito por el auditor al cerrar la
**`ACTA M6`**, que audita tu vuelta `5`. `MODO_INSERCION=cuarentena`, regimen ligero.*

> # **LIBRO DE ESTA VUELTA: `marquet_turn_the_ship`**
> # **CLASE DE ESTA VUELTA: EXTRACCION** (`python scripts/deuda.py --clase 6` da `LIBRE`, `van 4 de 5`)

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **TU TURNO ACABA CUANDO TU TRABAJO ACABA**

Puedes lanzar trabajos de fondo o en paralelo, **pero NUNCA termines tu turno con uno vivo**:
recogelos todos dentro del turno, vigilandolos si tardan. Un proceso que sobrevive a tu turno lo
mata el cierre del turno y nadie lo recoge. **Si algo no cabe en tu turno, NO lo lances: dilo en tu
reporte.** Esta vuelta tiene la tarea mas larga del libro (la `TAREA 3`), y por eso va con su reloj
medido delante.

---

## TAREA 1. **REGISTROS: EL ACTA M6, Y EL REMEDIO DE TU RACHA `REPORTE`, QUE ESTA EN `2 de 3`**

**Lee la `ACTA M6`** (`docs/loop/ACTA_AUDITOR.md`, al final). Lo que te toca de ella:

**TU `REPORTE` SUBIO DE `1 de 3` A `2 de 3`. UNA CAIDA MAS DE LA QUE ACUMULA Y LA LINEA PARA.** La
caida (`M6.3`, `M6.8.a`): **las cuatro tablas de frontera que pegaste en tu `1.a` no eran las brutas
de `.v5m/frontera/`, sino un resumen agrupado de ellas tecleado encima**, marcado `TALLADO: parcial`.
**`12` de sus filas agrupadas llevan una cifra de palabras que no es la suma de sus piezas**
(`cap_13` `R1 a R48`: `2680` donde hay `1982`), `cap_12` pisa `L107` dos veces, y **ninguna de las
cuatro columnas suma el cuerpo que su ultima fila declara con `residuo sin asignar: 0`**. Y el
parrafo de encima decia *Coinciden al digito: cero solapes*. **Las brutas si coincidian al digito: la
frontera era cierta y la tabla que publicaste no.**

**EL REMEDIO, Y ES REGLA ESCRITA (`D.41`, *la tabla pegada de su fichero*), NO DOCTRINA NUEVA:**

1. **LA FRONTERA DE CADA CAPITULO SE PEGA ENTERA, FILA POR PIEZA, TAL COMO LA ESCRIBE TU FICHERO
   BRUTO.** Sin filas agrupadas (`R15 a R23`), sin la marca `parcial`, y con su `<!-- TALLADO:
   salida=... -->` apuntando al fichero, para que `scripts/tallar_reporte.py` **la reproduzca en vez
   de citarla** (una tabla `parcial` se despacha como `CITA` sin comprobar, linea `461`: por eso la
   tuya paso el cierre).
2. **Si quieres un resumen, va APARTE y marcado `LECTURA`**, nunca en el sitio de la tabla.
3. **La frase *coincide al digito* solo va debajo de una tabla que el tallado haya reproducido**, y
   con la linea del cierre que lo dice pegada al lado.

**No es bloqueante** (ninguna guarda de dato esta en rojo, `D.55`; ejemplar `M4.16.a`): **es tu
primera tarea, y la cumples en cada frontera de esta vuelta.**

**LO DEMAS DE LA `M6` NO ACUMULA Y SE CORRIGE SIN CEREMONIA:** bajo un `$` va **solo lo que el
comando imprime** (tus tres `informe` iban resumidos y con un *(cero vecinos levantados)* que el
instrumento no escribe); **quien se relee entero en la muestra lo decide la semilla**, no el numero de
pasos (`scripts/muestra_fidelidad.py` linea `15`); y **no cites una `TAREA 4` que tu reporte no
tiene**.

**LO QUE LA `M6` TE FIRMA:** los `12` pasos, `12` TRANSCRIPCION; la muestra `m5` identica; tus tres
discutibles, sostenidos los tres; tus tres aduanas, reproducidas; y `d103` cumplida al minuto.

---

## TAREA 2. **`cap_16` Y `cap_17`: LOS DOS ULTIMOS CAPITULOS**

| capitulo | palabras |
|---|---:|
| `cap_16` | `830` |
| `cap_17` | `2673` |

**Tu borde izquierdo es `cap_15`**, leido entero en cero en tu vuelta `5` (`2.a`) y firmado por la
`ACTA M6` `M6.4`; su firma en `config/frentes.json` la escribe la sesion, no tu.

**Por cada capitulo:**

1. **LA FRONTERA, fila por pieza contra el fichero, ENTERA** (`TAREA 1`): numeros de linea y
   palabras, cero solapes y cero lineas sin cubrir, tallada contra su fichero bruto.
2. **Los candidatos que de**, cada uno con su `python forja.py informe` **corrido despues de escribir
   la ficha y con su salida GUARDADA en un fichero antes de seguir**; **no toques una ficha despues de
   su aduana sin volver a correrla** (`d103`). Cada uno con su `UNIDAD DE ORIGEN`.
3. **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo**; si da cero, `SIN SUPERFICIE`, y **un
   capitulo que no da nodo se firma LEYENDOLO ENTERO**.
4. **La muestra de fidelidad con la semilla de esta vuelta:**

       python scripts/muestra_fidelidad.py --libro marquet_turn_the_ship --capitulos cap_16,cap_17 --semilla m6

> **Si un capitulo pasa del `10` por ciento, se relee entero antes de seguir.**

---

## TAREA 3. **`d104`: EL BARRIDO DE LA BANDEJA ENTERA, AL CERRAR EL LOTE**

**Cuando la `TAREA 2` haya escrito sus fichas, y no antes**, la aduana se vuelve a correr sobre **cada
ficha de la bandeja de este libro** contra su texto de hoy, uno a uno:

    python forja.py informe cuarentena/marquet_turn_the_ship/<ficha>.json > .v6m/aduana/<ficha>.txt

**SU RELOJ, MEDIDO Y NO SUPUESTO (`ACTA M6` `M6.7`):** **un solo candidato contra la poblacion de `479` tarda entre `690` y `1198` s**, tres corridos en
paralelo por tu auditor (el de `8` pasos, el mas lento). **LECTURA de tu auditor, no medida:** si el
coste crece con los candidatos, una sola corrida sobre `20` o mas **no cabe en un turno**. **Una corrida con los `20`
candidatos de hoy mas los de tu `TAREA 2` NO esta medida por nadie.** Asi que:

- **PRIMERO las aduanas de tus candidatos nuevos** (`TAREA 2`), que son las que no puedes dejar;
- **DESPUES, el barrido por tandas de tres informes individuales en paralelo**, cada uno a su
  fichero en `.v6m/aduana/`, **cronometrado, y cada tanda RECOGIDA ENTERA antes de lanzar la
  siguiente**. Una tanda que no te da tiempo a recoger **no se lanza**;
- **lo que no quepa lo declaras con la lista exacta de fichas sin barrer**, y `d104` queda sin
  pagar. **Un barrido a medias no paga `d104`, pero si avanza, y la lista dice cuanto.**

**Lo que publicas del barrido:** el saldo (`ENTRARIAN`, `BLOQUEARIAN`, `CAERIAN`, `CHOCAN`), y **por
cada vecindad que cambie respecto a la cifra que su ficha llevaba**, cual era y cual es. **Cada par en
banda alta (`0,4` en adelante) lo lees por sus pasos** (`EXTRACTOR.md` `11`). Si lo pagas:
`python scripts/deuda.py --pagar d104 --vuelta 6 --como "..."`.

---

## TAREA 4. **LA CUENTA DEL LIBRO, Y EL CIERRE DE LA EXTRACCION**

**Si `cap_16` y `cap_17` quedan minados**, el libro esta leido entero. Publica **la cuenta del libro,
contada con un instrumento y con su salida pegada**, una fila por capitulo: `cap_01` a `cap_17`,
candidatos en bandeja por `UNIDAD DE ORIGEN`, pasos, y los capitulos en cero con la sede que los
firma. **Y di con la cifra delante si la extraccion de `marquet_turn_the_ship` esta CERRADA.**

**Si lo esta, NO cosechas, NO fundes y NO insertas**: eso es de la sesion y del fundador (`D.39`,
`D.50`, decision del `22` sep punto `4`: *al cerrar Marquet, se cosecha e inserta como septimo libro*).
**Lo dejas medido para que tu auditor pueda escribir la parada de campaña consumada.**

---

## LO QUE NO HACES

- **NO INSERTAS.** `MODO_INSERCION=cuarentena`.
- **NO TOCAS LA MAQUINARIA** (`D.45`): `orquestador_forja.sh`, `src/`, `scripts/`, `tests/`, `hooks/`,
  `esquema/`, **ni `config/`**. Si hace falta una firma, la pides en el reporte.
- **NO ESCRIBES DOCTRINA.** Si hace falta regla nueva, es parada.
- **NO TOCAS `cuarentena/grove_high_output/` NI `cuarentena/gerber_emyth/`**: son poblacion de tu
  aduana, no tuya.

## AL CERRAR

- **Tu tanda**: `python forja.py credito --anotar`, **con `--cae` o `--limpia` en cada especie,
  coherente con tu tabla.**
- **`D.61`**: cada discutible ejecutado o cerrado con su motivo.
- **Commitea `docs/loop/`, `cuarentena/marquet_turn_the_ship/` y `.v6m/`.**
- **Mide las condiciones de parada una a una** y publica que las mediste. **No escribas
  `PARA_ALEXIS.md`**: la parada, si la hay, la escribe tu auditor.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No adivines.
