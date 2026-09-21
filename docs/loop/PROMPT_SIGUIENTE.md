# ENCARGO DE LA VUELTA 2 DEL FRENTE `marquet_turn_the_ship`: **REABRIR**, desde `cap_04` con la frontera heredada

*Linea **`marquet_turn_the_ship`** (`extraccion-marquet_turn_the_ship`, worktree
`C:/Users/AlexDesk/Documents/forja-marquet_turn_the_ship`). **Escrito por la sesion de chat
del 22 sep 2026** al aplicar el punto `3` de la decision del fundador `GERBER ENTRA,
MARQUET SIGUE`.*

> # **LIBRO DE ESTA VUELTA: `marquet_turn_the_ship`**
> # **CLASE DE ESTA VUELTA: EXTRACCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. ESTE FRENTE LLEVA CINCO DIAS PARADO Y ACABA DE RECIBIR CINCO DIAS DE MAQUINARIA

**Tu vuelta `1` fue el `16` sep y paro con CINCO motivos.** Ninguno era culpa del trabajo de
la vuelta, y **los cinco estan resueltos**. Tu parada entera esta archivada en
`docs/loop/archivo/marquet_turn_the_ship/PARA_ALEXIS_2026-09-17.md`. Esto es donde quedo
cada uno:

| tu motivo | como queda |
|---|---|
| **`1`. mi sello esta roto y no lo rompi yo** | **MUERTO DE RAIZ.** `D.58` apaga la fase ciega en `cuarentena`, y **el sello vive dentro de ella**: `apertura_ciega()` sale en su linea `20` y no llega a la `49`. **No hay sello que romper** |
| **`2`. la restauracion del arnes borro `171` lineas publicadas** | **MUERTO DE RAIZ, y por lo mismo.** El `retirar=` y todo el refugio viven dentro de `apertura_ciega()`, detras del mismo `return`. **En cuarentena no se retira ni un fichero** |
| **`3`. que registro y que racha hereda un frente** | **`D.48`**: cada linea lleva la suya, y la tuya vive en `docs/loop/CREDITO_marquet_turn_the_ship.jsonl` |
| **`4`. un candidato que se cita a si mismo la fase ciega** | el mecanismo que lo produjo **ya no existe en este regimen**. El candidato sigue en tu bandeja y **lo leera la vuelta de insercion** |
| **`5`. `REPORTE` a `3 de 3`, credito roto** | **era la racha de la serial, no la tuya**, que es exactamente el defecto que `D.48` cerro |

    $ python forja.py credito
      LINEA SIN REGISTRO: no hay ningun suceso escrito.
      Una linea sin tandas NACE CON SU RACHA EN CERO y no hereda la de nadie (D.48).

> **NACES CON LAS CINCO RACHAS EN CERO. No arrastras nada de nadie.**

### 0.a. **Lo que cambio en la maquinaria mientras estabas parado, y te toca**

- **`D.58`, regimen ligero: la fase ciega esta APAGADA.** Turno del auditor directo y
  corto. **Techo de TRES capitulos por vuelta.**
- **`D.59`: toda media, porcentaje o razon la imprime un instrumento**, con numerador y
  denominador nombrados. Hay una guarda que corre en cada commit.
- **`D.60`: un mundo se cierra cuando sus libros estan INSERTADOS, no extraidos.** Te toca
  directo: **entras al mundo `11` como SEPTIMO libro si cierras tu extraccion antes de que
  la cuota de la semana se agote.** Si no, tu bandeja queda entera y **no bloquea nada**.
- **`D.61`: un discutible publicado se ejecuta o se cierra EN LA MISMA VUELTA.** Un *ahi
  nace otro candidato* publicado y no ejecutado es caida de `CIFRA PUBLICADA`, cuyo tope
  es `2` y no `3`. **Muerde antes que `REPORTE`.**
- **El capitulo de un candidato sale de su `UNIDAD DE ORIGEN`**, no de mencionarlo. Escribe
  `UNIDAD DE ORIGEN: fuentes/marquet_turn_the_ship/cap_NN.md` en cada `resumen_teorico`.

---

## 1. TU ESTADO, MEDIDO Y NO RECORDADO

    $ ls cuarentena/marquet_turn_the_ship/*.json | wc -l
    9
    $ ls fuentes/marquet_turn_the_ship/*.md | wc -l
    17
    $ python forja.py gate | sed -n '2p'
      nodos verificados: 346

**MINADOS: `cap_01`, `cap_02`, `cap_03`, con `9` candidatos. Tres de `17`.**

---

## 2. LA TAREA: **`cap_04`, `cap_05` Y `cap_06`**

**El fundador escribio *desde `cap_04` con su frontera heredada*, y eso es lo que haces.**

| capitulo | palabras |
|---|---:|
| `cap_04` | `1271` |
| `cap_05` | `2223` |
| `cap_06` | `2936` |
| **total** | **`6430`** |

**SON TRES Y ES EL TECHO DEL LIGERO** (`D.58`). No abras un cuarto.

**LA FRONTERA HEREDADA ES TU BORDE IZQUIERDO:** `cap_03` ya esta minado y su frontera
publicada en tu propio reporte archivado. **Citala como el borde del que arrancas**, para
que no quede hueco entre `cap_03` y `cap_04`.

### 2.a. Lo que entregas por cada capitulo

1. **LA FRONTERA, fila a fila contra el fichero**, con sus numeros de linea y sus palabras,
   **cero solapes y cero lineas sin cubrir**. Se comprueba al digito, asi que no la
   estimes.
2. **Los candidatos que de**, cada uno con su `python forja.py informe` corrido en el mismo
   acto en que lo escribes, **y cada uno con su `UNIDAD DE ORIGEN`**.
3. **`PASOS INVENTADOS POR CAPITULO`, UNA FILA POR CAPITULO Y NO UNA MEDIA**
   (`AUDITOR_FORJA.md` `8`). **Si un capitulo da CERO, la fila se escribe igual** y dice
   `SIN SUPERFICIE`.
4. **La muestra de fidelidad con la semilla de esta vuelta:**

       python scripts/muestra_fidelidad.py --libro marquet_turn_the_ship --capitulos cap_04,cap_05,cap_06 --semilla m2

### 2.b. **UN CAPITULO QUE DA CERO SE CIERRA IGUAL, Y SE FIRMA LEYENDO**

Lo acaban de demostrar dos libros seguidos: Grove cerro con `3` de `18` en cero y Gerber
con `9` de `22`, **y todos estan firmados**.

> **Un capitulo vacio no se puede comprobar por muestra: no hay pasos que muestrear.** La
> unica verificacion posible es **leerlo ENTERO y decir contra que se leyo.** Si alguno de
> los tres no da nodo, **eso no es un fallo tuyo: es un resultado.**

---

## 3. LO QUE DECIDE SI ESTE LIBRO ENTRA AL MUNDO `11`, Y CONVIENE QUE LO SEPAS

**`17` capitulos, `3` minados, `14` por delante.** A tres por vuelta son **cinco vueltas
mas**. La decision del fundador dice: *si la cuota de la semana lo cierra, se cosecha e
inserta como septimo; si no, queda en bandeja entero*.

**NO CORRAS POR ESO.** Una vuelta que sale limpia vale mas que dos que hay que repetir, y
**una bandeja a medias no bloquea nada** (`D.60`). Lo que cuesta caro es un capitulo mal
firmado, porque **eso si viaja al grafo**.

---

## 4. LO QUE NO HACES, Y NO ES NEGOCIABLE

- **NO INSERTAS.** `MODO_INSERCION=cuarentena`. Ningun frente inserta nunca, y si alguien
  escribe `insertar` en este arbol **el arnes se detiene antes de gastar un turno**.
- **NO TOCAS EL ARNES NI LA MAQUINARIA.** `D.45`, moratoria total: `orquestador_forja.sh`,
  `src/`, `scripts/`, `tests/`, `hooks/` y `esquema/`. **Si encuentras un defecto, lo MIDES
  y lo SUBES en tu `PARA_ALEXIS`, no lo arreglas.** Tu vuelta `1` hizo exactamente eso con
  cinco cosas y **tenia razon en las cinco**.
- **NO ESCRIBES DOCTRINA.** Si una pregunta necesita regla nueva, es parada.
- **NO TOCAS EL LIBRO DE OTRO FRENTE.** `gerber_emyth` esta corriendo su ultima vuelta en
  su propio arbol y **tiene dueno** (`D.49`). Tu libro es `marquet_turn_the_ship`.

---

## 5. AL CERRAR

- **Escribe tu tanda**: `python forja.py credito --anotar`. **Tu racha es tuya y empieza en
  cero** (`D.48`). Una linea que no escribe su credito **nace de nuevo cada vuelta**, y eso
  no es una racha en cero: es una racha que no existe.
- **Repasa `D.61` contra tu propio reporte**: cada discutible, ejecutado o cerrado con su
  motivo. **Ninguno abierto.**
- **Commitea `docs/loop/` y tu carpeta de evidencia.**
- **Si nada te obliga a parar, NO escribas `PARA_ALEXIS.md`**, y deja el encargo de la
  vuelta `3`. **Mide las condiciones de parada una a una y publica que las mediste**, en
  vez de suponer que no se cumplen.
