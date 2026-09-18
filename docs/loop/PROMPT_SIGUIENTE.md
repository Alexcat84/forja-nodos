# ENCARGO DE LA VUELTA 37: **`cap_12` Y `cap_13`, Y EL PUENTE SE ARREGLA ANTES DE QUE ENTRE**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

*Linea **serial** (`extraccion-mundo-11`), la unica que inserta (`D.45`). Escrito al cerrar la
`ACTA 35`, que audita la vuelta 36 y no abre ninguna parada.*

> # **LIBRO DE ESTA VUELTA: `scott_radical_candor`**

> ## **EL TRAMO SUBE A DOS CAPITULOS, Y LO SUBEN LOS DOS TECHOS A LA VEZ**
>
> | techo | lo medido | que sale |
> |---|---|---:|
> | `PASOS INVENTADOS` (`AUDITOR_FORJA.md` 8.1) | `cap_10` dio **`0` PUENTE de `206`**, `0,00` por ciento contra un tope de `10` | de `1` capitulo a **`2`** |
> | candidatos (`EXTRACTOR.md` 12.4) | `cap_12` trae `2` y `cap_13` trae `12` | **`14`**, contra un techo de `15` |
>
> **`cap_14` NO ENTRA EN ESTA VUELTA:** trae `15` el solo, justo en el techo, y `12.4` prohibe
> partir un capitulo para completar un tramo. **Va entero en la vuelta siguiente.**

---

## 1. LA APERTURA: **EL TABLERO Y SU PRIORIDAD** (`D.49`, `D.51`)

    python forja.py tablero                el estado de los once libros
    python forja.py tablero --siguiente    que libro le toca a ESTA linea, y por que

**Tu apertura cita las dos cosas**: el estado y el dueno de tu libro, **y por que te toca ese y
no otro**. `scott_radical_candor` sigue `CERRADO EN EXTRACCION` con `29` en bandeja: **`D.50`
releva AL CERRAR y no a mitad**, asi que te toca el mismo.

**La cola de doctrina sigue en `6` preguntas y ninguna bloquea.** La `ACTA 35` **retiro** la que
mi apertura ciega iba a aniadir (la asimetria de `difflib`), porque **`D.29` ya la tenia escrita
desde el 10 sep**: es caida mia, esta en la `ACTA 35` seccion 5, y **la cola no crece**.

---

## 2. TAREA 1, **BLOQUEANTE: EL PUENTE DE `cap_12` SE ARREGLA ANTES DE QUE EL CANDIDATO ENTRE** (`D.30`)

**`ACTA 35` seccion 6.** El paso `P33` de `desplegar_plan_orden_operaciones_franqueza_radical`,
que **espera en la bandeja**, dice:

    Asegurate de que no estas creando una cultura obsesionada con el ascenso, y dedica un
    pensamiento extra a como estas recompensando a tus superestrellas.

**Y `cap_12` `L41` dice `rock stars`**, que en este libro **no es sinonimo de `superstar`: son
las dos mitades opuestas de su marco**, y `cap_10` `L19` las escribe en la misma frase para
oponerlas (*a mistake to push everyone to be either a "superstar" or a "rock star"*). El
destino de la remision es la seccion `REWARD YOUR ROCK STARS` de `cap_10` `L225`.

- **Reescribe el paso contra su linea, o retiralo**, que es lo que `D.30` manda para un puente.
- **Corre tu conteo de las dos palabras sobre `cap_12` y `cap_10` y pegalo**, con la linea del
  libro al lado.
- **Y esto va ANTES de la primera insercion de `cap_12`**, no despues: `D.30` dice que la
  correccion vale mas barata en el minuto en que se escribe.

> **NO ES CAIDA DE NADIE TODAVIA, Y POR ESO ES BLOQUEANTE:** el paso **no ha entrado al grafo**,
> asi que no toca el `0` de `206` de `cap_10` que la `ACTA 35` firma. **Si entra sin arreglar,
> entonces si es un `PUENTE` dentro del grafo.**

## 3. TAREA 2. **`cap_12` Y `cap_13` ENTEROS: `14` CANDIDATOS**

- **Un candidato por vez y en el orden del libro**, por la aduana, con su veredicto.
- **`D.31` EN EL MISMO ACTO:** el insertado se archiva en `cuarentena/_insertados/<libro>/`
  **dentro de la misma funcion que inserta**, no despues. La vuelta 36 lo perdio dos veces y lo
  pago con un veredicto duplicado (`DATO MOVIDO`, `1 de 2`). **El remedio ya esta escrito en
  `.v36/cadena3.sh`: usalo o escribe el tuyo, pero que no dependa de acordarse.**
- **LAS TRES ARISTAS EN COLA SE CIERRAN SOLAS AL ENTRAR `cap_12`**, porque su madre es
  `desplegar_plan_orden_operaciones_franqueza_radical`. **Comprueba que se cablearon y publica
  la cuenta**: si alguna queda en cola con sus dos extremos vivos, eso es un cableado perdido.
- **Y UNA ARISTA MAS QUE LA `ACTA 35` TE DEJA MEDIDA:** `cap_12` `L41` lleva **DOS** remisiones
  *(see chapter seven)* en la misma frase. La vuelta 36 cablo la primera (a
  `evitar_obsesion_ascenso_estatus`) **y no la segunda**, que apunta a
  `reconocer_excelencia_trayectoria_gradual`, hoy huerfano. **Cablea la segunda por lectura
  (`D.29`) o di por que no.**
- **`NO SE ABRE NINGUN LOTE`** (`D.32`): el lote 4 no cierra con esta vuelta.

> **EL CERROJO VIVE EN `procesos/`** (`D.53`), nunca dentro de `dataset/`. Si algo dice
> `INSERCION NO INTENTADA`, hay otra corrida viva. **No la esquives.**

## 4. TAREA 3. **LA FIDELIDAD, ANTES DE QUE LOS NODOS ENTREN** (`D.30`, `EXTRACTOR.md` 15.4)

**`PASOS INVENTADOS` por capitulo**, **fila por `cap_12` y fila por `cap_13`, mas el total**,
releyendo los pasos contra su parrafo. Son `50` mas `212` pasos, **y la fila decide el volumen
mientras el total solo compara lotes** (`AUDITOR_FORJA.md` 8.2).

> **LA RELECTURA VA ANTES DE LA PRIMERA INSERCION.** **La escalada se decide sobre el PEOR
> capitulo, no sobre el promedio.** Tope `10`.

**Y UNA PIEZA DE `cap_13` QUE LA `ACTA 35` TE DEJA ESCRITA ANTES DE QUE LA DECIDAS**
(`POR ADJUDICAR 7`): `L323` `DIVERSITY AND INCLUSION` **no tiene candidato**, y dentro del
relato de una participante hay una practica con periodo y metodo (*spaghetti dinners once a
month*, donde se comparten las historias y se ensaya lo que se podria haber dicho). **La lectura
ciega del auditor fue que NO es nodo** (la practica se la atribuye el libro a una asistente a un
taller, y lo que el texto hace despues es anunciar su propio taller, manual 3.5). **Decidelo tu
con el tramo delante y publica tu razon en las dos direcciones.** `L333` `WHAT'S NEXT?` es
promocion y esta bien fuera.

## 5. TAREA 4. **LA FRONTERA DE `cap_10` QUE NADIE DECLARO, COMPROBADA Y NO REABIERTA**

**`ACTA 35` `POR ADJUDICAR 2`.** `cap_10` tiene **ocho secciones en mayusculas** y **`L253`
`AVOID ABSENTEE MANAGEMENT AND MICROMANAGEMENT` es la unica sin nodo**, ni en el grafo ni en la
bandeja. **No es caida tuya:** la frontera se publica en la vuelta que **mina**, no en la que
inserta, y la 36 no mino nada.

**LO QUE SE PIDE ES UNA COMPROBACION DE UNA LINEA, y nada mas:** busca en el reporte la vuelta
que mino `cap_10` y **di si su frontera declaro `L253` con su razon**. Si la declaro, pega la
cita y cierra el punto. **Si no la declaro, dilo y deja `L253` leida con tu veredicto**
(`D.27`: una postura no es un procedimiento; `L255` dice *I've developed a simple chart* y **el
cuadro no esta en el texto**).

**NO SE REABRE `cap_10` NI SE MINA NADA NUEVO POR ESTO.** Es una comprobacion de registro.

---

## 6. **LO QUE YA ESTA HECHO Y NO SE REHACE**

| | |
|---|---|
| **las `37` clases de la vuelta 36** | adjudicadas y coincidentes las `37` (`ACTA 35` 2.2). **No se releen** |
| **los `206` pasos de `cap_10`** | `0` PUENTE, firmado por el auditor con su propio conteo (`ACTA 35` 3) |
| **el duplicado de la linea `431`** | anotado sin borrar, especie `DATO MOVIDO`, racha `1 de 2`. **Cerrado** |
| **las cuatro lineas de credito de la tanda `ACTA 35`** | ya escritas por la vuelta 36 y adjudicadas tal cual. **La quinta, `AUDITOR`, la escribio el auditor.** No se vuelven a anotar |

**No las vuelvas a tocar y no las cuentes como trabajo tuyo.**

## 7. LO QUE NO SE TOCA

- **El banco, los protocolos, `scripts/` y `orquestador_forja.sh`**: la excepcion acotada a
  `D.45` ya se gasto. **Las tres propuestas que la `ACTA 35` deja abiertas son de Alexis**, no
  tuyas: el asunto del commit del arnes, la retirada de cinco ficheros donde `D.34.2` escribe
  cuatro, y la sede unica de `docs/loop/TABLA_DE_CIERRE.txt` que el propio reporte propuso.
- **`config/umbrales.json`**, ningun umbral. **`config/frentes.json`** se lee, no se edita.
- **El bucle no funde ramas y el bucle no crea remotos.**
- **Los frentes**: `grove_high_output` es de su linea; `gerber_emyth` y `marquet_turn_the_ship`
  estan pausados. **Ninguno es asunto tuyo.**

## 8. AL CERRAR

    python scripts/cerrar_reporte.py
    python scripts/tabla_de_cierre.py --escribir   y se pega su salida
    python forja.py tablero --escribir             el tablero se vuelve a medir (D.49)
    python forja.py credito --anotar ...           una linea por especie, con su cita

**La `cita` es REFERENCIA, nunca un resultado** (`D.53`). **Y tu tabla de cierre publica `N de M`
del CAPITULO y no del tramo**: el instrumento lo comprueba contra el grafo y **muerde**, y el
auditor lo verifico por mutacion (`ACTA 35` 1.2).

**Y COMMITEA Y PUSHEA `docs/loop/`.**

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.**
