# ENCARGO DE LA VUELTA 35: **EL PUENTE QUE ENTRO AL GRAFO, Y DESPUES CERRAR `cap_09`**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

*Linea **serial** (`extraccion-mundo-11`), la unica que inserta (`D.45`). Escrito al cerrar
la `ACTA 33`, que audita la vuelta 34.*

> # **LIBRO DE ESTA VUELTA: scott_radical_candor**

**El arnes lee esa linea y la comprueba contra el tablero ANTES de gastar un turno.**

    python forja.py tablero                el estado de los once libros
    python forja.py tablero --siguiente    que libro le toca a ESTA linea, y por que

**TU APERTURA CITA LAS DOS COSAS** (`D.49`): **el estado y el dueño de tu libro**, y **por
que te toca ese y no otro**. `scott_radical_candor` esta `CERRADO EN EXTRACCION`, es de tu
linea y **`D.50` releva AL CERRAR y no a mitad**: quedan `48` en bandeja.

**LA COLA DE DOCTRINA SIGUE EN SEIS Y NINGUNA BLOQUEA.** Si te topas con una, **di que es
la numero `N` y sigue**. La vuelta 34 se topo con cuatro y lo hizo bien: eso no se cambia.

---

## 1. **LO QUE LA `ACTA 33` ADJUDICO, Y QUE NO TIENES QUE IR A BUSCAR**

| # | que | como quedo |
|---:|---|---|
| **`DISCUTIBLE 1`** | `practicar_franqueza_radical_jefe_propio` `P13`, `L215` | **CAE. ES `PUENTE`**, y es tu `TAREA 1` |
| **`DISCUTIBLE 2`** | el par de `0,867` | **SE SOSTIENE. `SANO`, y la arista `D.29` NO se declara** |
| **`DISCUTIBLE 3`** | el par de `0,402` | **SE SOSTIENE. `SANO`**, y la banda de `0,4` sigue en la cola de doctrina |
| **tu `PARADA` de `AA.5.h`** | el cierre de `D.41` en rojo por una tabla ajena | **NO ERA PARADA, e hiciste bien en declararla y no tocarla.** El rojo se apago cuando la apertura ciega de la vuelta 34 sobrescribio a la de la 33. **El cierre esta VERDE hoy** |
| **`PASOS INVENTADOS` de `cap_09`** | tu `0` de `181` | **el auditor firma `1` de `181`, `0,55` por ciento.** Sigue muy por debajo del tope de `10`: **el tramo no cambia de escalon por esta cifra** |

**TU CREDITO AL ABRIR, Y NO TE LO ESCRIBES TU** (`ACTA 33` 9.1, remedio 4):

    python forja.py credito          CLASE 0 de 2, CIFRA PUBLICADA 0 de 2, DATO MOVIDO 0 de 2,
                                     REPORTE 2 de 3, AUDITOR 2 de 3

**`CLASE`, `CIFRA PUBLICADA` y `DATO MOVIDO` vuelven a `0` por tanda limpia** (`D.38.1`).
**`REPORTE` esta en `2 de 3`, que es el penultimo escalon: la proxima cae al tope.** Y por
eso las tres primeras tareas de este encargo son exactamente su remedio.

> **NO ESCRIBAS NINGUNA LINEA EN `docs/loop/CREDITO_serial.jsonl`.** `D.48` dice que eso es
> parte de **cerrar el acta**, y el acta no es tuya (`AUDITOR_FORJA.md` 5.6). **Lo que si
> haces, y en tu reporte**, es proponer la lectura de cada especie con su motivo: eso es lo
> que `EXTRACTOR.md` 14 llama proponer sin adjudicarse.

---

## 2. **TAREA 1, BLOQUEANTE: EL PUENTE QUE YA ESTA DENTRO DEL GRAFO** (`D.30`, `D.13`)

*`D.30`: **cada puente se retira o se reescribe, citando el parrafo que NO lo dice. Un
puente no se queda callado dentro de un nodo.** Va ANTES de insertar nada.*

**EL CASO, EN DOS LINEAS.** El libro, `cap_09.md` `L215`:

    If they don't, give up immediately or assume ill intent. Try again, carefully, ...

**El paso `13` que entro al grafo:**

    Si no, para inmediatamente, y no des por supuesta la mala intencion: vuelve a
    intentarlo con cuidado, ...

**`X or Y` comparte polaridad en las dos lecturas posibles** (`give up ... or assume ...`,
o `don't give up ... or assume ...`). **El paso escribe la primera mitad en positivo y la
segunda en negativo**, que no es ninguna de las dos, y **se contradice a si mismo**: *para
inmediatamente* seguido de *vuelve a intentarlo con cuidado*.

### 2.a. **CORRIGELO SIN RESOLVER LA ERRATA DEL LIBRO EN NINGUNA DIRECCION**

    python forja.py corregir --nodo practicar_franqueza_radical_jefe_propio --anade "CORRECCION DECLARADA ..." --razon ...

- **El paso se queda con lo que `L215` sostiene SIN ambiguedad**: si reacciona bien, sigue;
  si no, vuelve a intentarlo con cuidado; si la segunda vez la reaccion es la misma, puede
  que sea momento de irse.
- **La clausula contradictoria se DECLARA y no se elige**: el `resumen_teorico` dice que
  `L215` del recorte se contradice con su propia frase siguiente, **y que este nodo no
  decide cual de las dos lecturas es la buena**. `D.30` no te deja escribir lo que el libro
  no dice, **y tampoco te deja inventar cual queria decir**.
- **`D.13`, sin borrar un caracter del texto viejo**, y con la linea `215` pegada (`D.35`).
- **El `resumen_teorico` de ese nodo declara hoy `17 pasos, 17 TRANSCRIPCION, 0 PUENTE`.**
  Esa frase tambien queda corregida, por la misma via y sin borrarla.

### 2.b. **Y REPUBLICA LA CIFRA, QUE ES LA MITAD QUE IMPORTA**

**Tu reporte dice que `PASOS INVENTADOS` de `cap_09` fue `0,00` por ciento. El auditor lo
firma en `1` de `181`, `0,55` por ciento.** El reporte nuevo lo dice **sin borrar la cifra
vieja** y **citando la `ACTA 33` seccion 3.1**. No es una humillacion y no cambia el
volumen del lote: **es la cifra que la casa usa para decidir tamaños, y una cifra firmada
por dos manos distintas no puede tener dos valores publicados sin decirlo.**

---

## 3. **TAREA 2: LA FIDELIDAD, ANTES DE INSERTAR, Y CON UN OJO NUEVO** (`D.30`, remedio 3)

**`PASOS INVENTADOS` por capitulo, fila por unidad mas total, releyendo los pasos contra su
parrafo.** El orden no se discute: **va antes de que entre ni un nodo**, y se ve en el orden
de tus commits. La vuelta 34 lo cumplio y eso no se pierde.

> **LO QUE ANADE ESTA VUELTA, Y SALE DE LA CAIDA DE LA 34:** antes de publicar un
> `0 PUENTE`, **relee expresamente todo paso cuya linea del libro se contradiga consigo
> misma o cuya polaridad el paso parta por la mitad** (una mitad en positivo y la otra en
> negativo). **Declara cuales releiste por ese motivo, aunque sean cero.** Un barrido que
> solo se cuenta cuando encuentra algo no es un barrido.

**La escalada se decide sobre el peor capitulo, no sobre el promedio.** Tope `10`.

---

## 4. **TAREA 3: CERRAR `cap_09` EN INSERCION, Y AHI PARA EL TRAMO**

    $ python -c "cuenta cuarentena/scott_radical_candor por capitulo"
      cap_09   candidatos= 5  pasos=  91
      cap_10   candidatos=14  pasos= 206
      cap_12   candidatos= 2  pasos=  50
      cap_13   candidatos=12  pasos= 212
      cap_14   candidatos=15  pasos= 174
      TOTAL   candidatos=48  pasos=733

**EL TRAMO SON LOS `5` DE `cap_09`, Y CIERRAN EL CAPITULO**, en el orden del libro:
`entregar_evaluacion_formal_desempenio_nueve_consejos` (L331),
`impedir_punialadas_espalda_equipo` (L363), `fomentar_guia_reciproca_companieros` (L369),
`conducir_reuniones_salto_nivel_diez_reglas` (L383) y
`resolver_dudas_frecuentes_reuniones_salto_nivel` (L415).

> **POR QUE NO SE EMPIEZA `cap_10` EN LA MISMA VUELTA, con la cuenta delante:** `5` mas `14`
> son `19`, **por encima del techo de `15`** (`EXTRACTOR.md` 12.4), y `cap_10` **cabe entero
> en una vuelta**, asi que **no se reparte en dos**. `5` esta dentro del tramo permitido,
> que es *entre cinco y quince candidatos*. **Declara el tramo corto con su cifra**, que es
> lo que la vuelta 34 hizo bien y lo que la 17 no hizo.

- **Un candidato por vez y en el orden del libro**, por la aduana, con su veredicto.
- **Archiva en `_insertados` EN EL MISMO ACTO** (`D.31`). La vuelta 34 se cobro a si misma
  el precio de no hacerlo: un vecino listado dos veces.
- **Las aristas `D.29` que la señal no levanta se declaran por lectura y se cablean en la
  misma vuelta.** Queda **una** de las tres remisiones de `cap_08.md` `L95`, la del capitulo
  siete, y **espera a que entre `cap_10`**: no la fuerces ahora.
- **NO SE ABRE NINGUN LOTE** (`D.32`). El tablero lo impide y no una frase.

> **EL CERROJO VIVE EN `procesos/`, nunca dentro de `dataset/`** (`D.44`, `D.52`). Si algo
> dice `INSERCION NO INTENTADA`, hay otra corrida viva. **No la esquives.**

---

## MODO AUSTERO (`D.47`), QUE SIGUE VIGENTE HASTA QUE CIERRE EL MUNDO 11

| | |
|---|---|
| **el reporte** | **nada que el registro ya diga** |
| **los discutibles** | **por numero y linea**, sin reabrir el argumento |
| **las cifras** | **talladas**, con la salida del instrumento pegada de su fichero (`D.41`) |
| **los instrumentos** | **CERO nuevos**, salvo que una caida **de DATO** lo exija con su cita |

> **El austero recorta tinta, no control.** La aduana entera, el cerrojo, el censo no
> decreciente y la relectura contra el parrafo **quedan intactos**.

## LO QUE NO SE TOCA

- **`src/`, el banco, el arnes y los protocolos**: moratoria de `D.45`.
- **`config/umbrales.json`**, ningun umbral, y **`config/frentes.json`** se lee y no se edita.
- **`docs/loop/CREDITO_serial.jsonl`**: sede del acta, no tuya.
- **El bucle no funde ramas y el bucle no crea remotos.**
- **Los frentes**: `grove_high_output` es de su linea; `gerber_emyth` y
  `marquet_turn_the_ship` estan pausados. **Ninguno es asunto tuyo.**

## AL CERRAR

    python scripts/cerrar_reporte.py
    python forja.py tablero --escribir          el tablero se vuelve a medir (D.49)

**Y COMMITEA Y PUSHEA `docs/loop/`.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una
regla vigente, paras y lo traes. No adivines.**
