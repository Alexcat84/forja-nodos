# ENCARGO DE LA VUELTA 36: **`cap_10` ENTERO, Y SIN PARTIRLO**

*Linea **serial** (`extraccion-mundo-11`), la unica que inserta (`D.45`). Escrito al
aplicar la decision del fundador del 17 sep 2026, archivada en
`docs/loop/paradas/2026-09-17-la-tabla-de-cierre-DECISION.md`.*

> # **LA PARADA ESTA LEVANTADA, Y CON UN REMEDIO DELANTE, NO CON UN PERDON**
>
> `REPORTE` vuelve a `0 de 3` **con una condicion que ya esta cumplida**: el remedio
> corre. Las tres caidas de esa racha vivian en **la misma tabla**, la de cierre de
> tareas, **que era la unica del reporte sin instrumento declarado**. `D.41` no la miraba
> por diseño: compara tablas contra su fichero de salida, y esa no tenia ninguno.
>
> **Ahora lo tiene.** `scripts/tabla_de_cierre.py`, corriendo en cada commit.
>
> **LO QUE ESO SIGNIFICA PARA TI:** si tu tabla de cierre publica `N de M del capitulo` y
> el grafo no da ese `M`, **tu commit no pasa**. No se corrige tecleando la celda buena:
> **se regenera y se pega.**

---

## 1. LA APERTURA: **EL TABLERO Y SU PRIORIDAD** (`D.49`, `D.51`)

> # **LIBRO DE ESTA VUELTA: `scott_radical_candor`**

    python forja.py tablero                el estado de los once libros
    python forja.py tablero --siguiente    que libro le toca a ESTA linea, y por que

**Tu apertura cita las dos cosas**: el estado y el dueño de tu libro, **y por que te toca
ese y no otro**. Mientras `scott_radical_candor` no cierre, te toca el mismo: `D.50`
releva **al cerrar** y no a mitad.

**La cola de doctrina del tablero tiene ahora `6` preguntas**, y **una menos que ayer**:
la `7` quedo decidida y es `D.54`. Si te topas con alguna de las seis, **no la adjudiques:
di que es la numero `N` de la cola y sigue.**

---

## 2. TAREA 1. **`cap_10` ENTERO, SUS `14`, Y NO SE PARTE**

    $ python .v36/estado.py
    poblacion: el arbol entero, sin filtrar
    dataset/nodos.jsonl                        : 302 nodos
    bitacora/VEREDICTOS.jsonl                  : 427 lineas
    cuarentena/scott_radical_candor            : 43
    cuarentena/_insertados/scott_radical_candor: 99
    la bandeja por capitulo                    : cap_10 14, cap_12 2, cap_13 12, cap_14 15

**`99` de `142` insertados, el `69,7` por ciento.** El capitulo que toca es **`cap_10`, con
sus `14` candidatos**, y el encargo anterior ya dejo declarado que **caben en una vuelta y
por eso NO SE PARTEN**. Son `14` contra un techo de `15` (`EXTRACTOR.md` 12.4): **cabe
justo, y por eso entra entero.**

- **Un candidato por vez y en el orden del libro**, por la aduana, con su veredicto.
- **Las aristas `D.29` que la señal no levanta se declaran por lectura y se cablean en la
  misma vuelta.**
- **Y ESPERA UNA REMISION QUE YA ESTA MEDIDA:** `cap_08.md` `L95` remite al capitulo
  siete, y **esperaba a que `cap_10` entrara**. Cablea esa arista en esta vuelta, o di por
  que no.
- **`NO SE ABRE NINGUN LOTE** (`D.32`). El lote 5 no se toca: lo impide el tablero.

> **EL CERROJO VIVE EN `procesos/`** (`D.53`), nunca dentro de `dataset/`. Si algo dice
> `INSERCION NO INTENTADA`, hay otra corrida viva. **No la esquives.**

## 3. TAREA 2. **LA FIDELIDAD, ANTES DE QUE LOS NODOS ENTREN**

**`PASOS INVENTADOS` por capitulo** (`D.30`), fila por unidad mas total, **releyendo los
pasos contra su parrafo**.

> **LA RELECTURA VA ANTES DE LA PRIMERA INSERCION**, que es la letra que la vuelta 33
> rompio y la 35 ya cumplio. **La escalada se decide sobre el peor capitulo**, no sobre el
> promedio. Tope `10`.

## 4. TAREA 3. **CERRAR CON LA TABLA REGENERADA, NO TECLEADA**

    python scripts/tabla_de_cierre.py --escribir

**Y PEGAS SU SALIDA**, con su marca de tallado encima, igual que las demas tablas del
reporte. La salida vive en `docs/loop/TABLA_DE_CIERRE.txt`.

**Lo que el instrumento sabe medir, y solo eso:** una afirmacion **`N` de `M` del
capitulo** con su `cap_NN` en la misma fila, donde `M` es **cuantos nodos del grafo salen
de ese capitulo**, medido por la ruta completa. **Una fila sin cifra medible se declara
`SIN COMPROBAR` y se copia tal cual**: el instrumento no rellena lo que no sabe.

---

## 5. **LO QUE YA ESTA HECHO Y NO SE REHACE**

| | |
|---|---|
| **la fila `3` de la tabla de cierre de la vuelta 35** | corregida por regeneracion: decia `15 de 15 del capitulo` y `cap_09` son **`20`**, con `272` pasos. **El `15` de la izquierda era cierto; lo falso era el denominador**, que era el del TRAMO |
| **el paso `13` de `practicar_franqueza_radical_jefe_propio`** | **retirado del campo** (`D.54`), no solo de la prosa. Sus pasos pasan de `17` a `16` y **su texto literal queda escrito dentro del nodo** |
| **el barrido de esa especie** | corrido sobre los `302` nodos: **era uno, y era ese**. Despues: `0` |

**No las vuelvas a tocar y no las cuentes como trabajo tuyo.**

## 6. LO QUE NO SE TOCA

- **El banco, los protocolos y `orquestador_forja.sh`**: la excepcion a `D.45` que
  permitio el remedio de hoy **era acotada a `scripts/`**, y ya se gasto.
- **`config/umbrales.json`**, ningun umbral. **`config/frentes.json`** se lee, no se edita.
- **El bucle no funde ramas y el bucle no crea remotos.**
- **Los frentes**: `grove_high_output` es de su linea; `gerber_emyth` y
  `marquet_turn_the_ship` estan pausados. **Ninguno es asunto tuyo.**

## 7. AL CERRAR

    python scripts/cerrar_reporte.py
    python scripts/tabla_de_cierre.py --escribir   y se pega su salida
    python forja.py tablero --escribir             el tablero se vuelve a medir (D.49)
    python forja.py credito --anotar ...           una linea por especie, con su cita

**La `cita` es REFERENCIA, nunca un resultado** (`D.53`): `"ACTA 35, seccion 9.1"`, jamas
`"11 SANO releidos"`. **Una cita con conclusion dentro no pasa el sello.**

**Y COMMITEA Y PUSHEA `docs/loop/`.**
