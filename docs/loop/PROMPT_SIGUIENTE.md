# ENCARGO DE LA VUELTA 5 DEL FRENTE `marquet_turn_the_ship`: **`cap_12` A `cap_15`, CUATRO CAPITULOS**, y el libro queda a una vuelta de cerrarse

*Linea **`marquet_turn_the_ship`** (`extraccion-marquet_turn_the_ship`, worktree
`C:/Users/AlexDesk/Documents/forja-marquet_turn_the_ship`). **Escrito por la sesion de chat
del 22 sep 2026** al aplicar la decision del fundador `DOS SEMANAS`, archivada en la serial
en `docs/loop/paradas/2026-09-22-dos-semanas-DECISION.md`. Tu vuelta `4` paro y su acta no
escribe encargo.*

> # **LIBRO DE ESTA VUELTA: `marquet_turn_the_ship`**
> # **CLASE DE ESTA VUELTA: EXTRACCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. TU RACHA SE REINICIO, Y LA AVERIA QUE LA ROMPIO YA NO SE PUEDE REPETIR

**Parabas por `CIFRA PUBLICADA` a `2 de 2`.** El fundador la reinicio por escrito:

    $ python forja.py credito
      CIFRA PUBLICADA    0 de 2     docs/loop/paradas/2026-09-22-dos-semanas-DECISION.md, punto 2
      REPORTE            1 de 3     ACTA M5
      CREDITO ENTERO: ninguna especie en su tope.

**Su motivo, y conviene que lo entiendas porque te afecta desde ya:** tus dos caidas eran **la
misma averia del instrumento**. `forja.py credito --anotar` aceptaba una fila que sube la racha
**sin decir si cae**, y tu vuelta `4` escribio cuatro. **Desde el `21` sep el instrumento se
niega**:

    una tanda que no dice si cae. Una racha solo sube cuando algo cae, y sin esa bandera el
    registro publica una cifra que nadie puede releer (ACTA M5 M5.11). Escribe cae true o cae false.

**Y tus cuatro filas de la vuelta `4` estan corregidas por correccion declarada**: `cae` alineado
con la racha que ya declaraban, el valor viejo al lado en `cae_original`, y **ninguna racha
movida**. Tu auditor de la `M5` las nombro con precision; **tenia razon en las dos cosas que
midio y no podia tocar** (`D.45`).

**AL ANOTAR TU TANDA: `--cae` o `--limpia` en cada especie, coherente con lo que tu tabla
dice.** Es la unica forma que el instrumento acepta ya.

---

## 1. LO QUE CAMBIO ALREDEDOR DE TI

| | |
|---|---|
| **gerber_emyth** | **COSECHADO el `22` sep.** Sus `22` candidatos estan en la bandeja de la serial, y su frente se desmonto |
| **la serial** | **INSERTANDO**: Grove primero, despues Gerber. **Tu libro va DESPUES de los dos**, como SEPTIMO del mundo `11` |
| **el mundo `11`** | **cierra con SIETE libros**, y el tuyo es el septimo. **Entra cuando cierres tu extraccion**: la sesion cosecha tu rama y la serial te inserta al acabar Gerber |
| **modelos** | tu extractor **`claude-sonnet-5`** y tu auditor **`claude-opus-5-5`**, los dos con su esfuerzo por defecto |
| **tu arbol** | acaba de recibir la maquinaria de la serial. **Tu `DEUDA.jsonl` y tu sede viva son las tuyas**, sin tocar |

> **UNA COSA DE SEDE, y no es una caida tuya: `config/` es de la sesion de chat.** Tu vuelta `4`
> escribio alli la firma en cero de tu `cap_05`, pagando `d100`, que tu propio auditor te
> encargo. **El contenido era correcto y la serial lo adopto con la misma cita.** A partir de
> ahora, **si hace falta una firma en `config/`, pidela en el acta y la escribe la sesion**, que
> es como lo hizo el frente de Gerber tres veces.

---

## 2. LA TAREA: **`cap_12`, `cap_13`, `cap_14` Y `cap_15`**

**CUATRO, y el numero no es un capricho:** tu `ACTA M5` `M5.18` lo midio y lo firmo. **El peor
capitulo de tu ultimo tramo dio `0,00`**, y `8.1` da un capitulo mas: **de tres a cuatro.** El
fundador lo confirmo en su decision.

| capitulo | palabras |
|---|---:|
| `cap_12` | `2087` |
| `cap_13` | `2998` |
| `cap_14` | `1324` |
| `cap_15` | `1819` |
| **total** | **`8228`** |

**Y DESPUES SOLO QUEDAN `cap_16` (`830` palabras) Y `cap_17` (`2673`)**: la vuelta `6` cierra el
libro.

**LA FRONTERA HEREDADA ES TU BORDE IZQUIERDO:** `cap_11` esta minado y su frontera publicada en
tu reporte. **Citala como el borde del que arrancas.**

### 2.a. Lo que entregas por cada capitulo

1. **LA FRONTERA, fila a fila contra el fichero**, con numeros de linea y palabras, **cero solapes
   y cero lineas sin cubrir**.
2. **Los candidatos que de**, cada uno con su `python forja.py informe` **corrido en el mismo acto
   en que lo escribes, y con su salida GUARDADA en un fichero antes de seguir**: tu vuelta `2`
   escribio *pasados por la aduana* sobre dos que no la tuvieron, y un fichero de `0` bytes no es
   una aduana. **Y cada uno con su `UNIDAD DE ORIGEN`.**
3. **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo.** Si da cero, la fila dice
   `SIN SUPERFICIE`, y **un capitulo que no da nodo se firma LEYENDOLO ENTERO**.
4. **La muestra de fidelidad con la semilla de esta vuelta:**

       python scripts/muestra_fidelidad.py --libro marquet_turn_the_ship --capitulos cap_12,cap_13,cap_14,cap_15 --semilla m5

> **Y SI UN CAPITULO PASA DEL `10` POR CIENTO, SE RELEE ENTERO ANTES DE SEGUIR, y el tramo baja
> un escalon.** Lo viviste en tu `cap_06` con `11,11`, y funciono exactamente como esta escrito.

---

## 3. LAS DOS DEUDAS DE TU `M5` QUE VIAJAN, Y CUANDO SE PAGAN

- **`d103`**: las aduanas de un lote se corren mientras sus fichas todavia cambian, y la salida
  deja de reproducir sobre el arbol commiteado. **Lo evitas con el punto `2.a.2`**: fichero
  guardado antes de seguir, y **no toques una ficha despues de correr su aduana** sin volver a
  correrla.
- **`d104`**: cuando una ficha cambia, cambian sus vecindades, y **`13` fichas quedan con la cifra
  de antes**. **Se paga con un barrido completo al cerrar el lote**, que es tu vuelta `6`, no esta.

---

## 4. LO QUE NO HACES

- **NO INSERTAS.** `MODO_INSERCION=cuarentena`. Ningun frente inserta nunca.
- **NO TOCAS LA MAQUINARIA** (`D.45`): `orquestador_forja.sh`, `src/`, `scripts/`, `tests/`,
  `hooks/`, `esquema/`, **ni `config/`**. Mides y subes.
- **NO ESCRIBES DOCTRINA.** Si hace falta regla nueva, es parada.
- **NO TOCAS `cuarentena/grove_high_output/` NI `cuarentena/gerber_emyth/`**, que acaban de llegar
  a tu arbol con la maquinaria: **son la bandeja de la serial**, y la serial los esta insertando.
  Estan ahi para que tu aduana los vea como vecinos, que es justo lo que tiene que pasar.

---

## 5. AL CERRAR

- **Tu tanda**: `python forja.py credito --anotar`, **con `cae` en cada especie**.
- **`D.61`**: cada discutible ejecutado o cerrado con su motivo. **Ninguno abierto.**
- **Commitea `docs/loop/` y tu carpeta de evidencia.**
- **Si nada te obliga a parar, NO escribas `PARA_ALEXIS.md`**, y deja el encargo de la vuelta
  `6`: **`cap_16`, `cap_17`, el barrido de `d104`, y el cierre del libro.** Mide las condiciones
  de parada una a una y publica que las mediste.
