# ENCARGO DE LA VUELTA 33: **LA INSERCION CONTINUA, EN AUSTERO**

*Linea **serial** (`extraccion-mundo-11`), la unica que inserta (`D.45`). Escrito al
aplicar la decision del fundador del 17 sep 2026, archivada en
`docs/loop/paradas/2026-09-17-de-quien-es-la-racha-DECISION.md`.*

> # **LA PARADA ESTA LEVANTADA, Y CON QUE**
>
> **`REPORTE` vuelve a `0 de 3`** por decision escrita del fundador (`5.4`), **no por
> tanda limpia y no por ti.** El motivo que la decision da, y conviene que lo tengas
> delante porque cambia lo que se te pide: **las tres curas de esa especie ya corren en
> el hook** (`D.41` tallado, `D.42` censo de celdas, `D.46` el instante del sello), asi
> que **la proxima caida de esa especie la caza el codigo antes del commit.**
>
> **Lo que eso significa para ti:** no te la ahorras, **te la cazan antes.** Un rotulo
> que no dice lo que su instrumento midio ya no llega al acta: **tumba tu commit.**

---

## LO PRIMERO: **`D.48`, Y ESTO ES NUEVO DESDE AYER**

**LA RACHA ES DE SU LINEA, Y EL CREDITO VIVE EN UN FICHERO.**

    python forja.py credito

**Eso es lo que tu linea trae al abrir, y es la sede.** Lo que salga de ahi es lo que
vale; tu acta lo publica, no lo decide. Tu linea es **`serial`**, con `31` tandas
escritas y su historia entera migrada desde las `31` actas.

> ### **Y AL CERRAR TU ACTA ESCRIBES TU TANDA. No es opcional: es parte de cerrar.**
>
>     python forja.py credito --anotar --especie REPORTE --vuelta 33 \
>            --tanda "ACTA 32" --racha "0 de 3" --limpia --cita "ACTA 32, seccion 9.1"
>
> **`--cae` si la especie cayo en tu tanda, `--limpia` si no.** Una linea por especie.
> **El instrumento no reinicia nada por su cuenta:** un reinicio es un suceso aparte con
> su cita a un fichero de `docs/loop/paradas/`, igual que siempre.

**POR QUE EXISTE:** ayer tres frentes de libro nacieron de esta rama, **se llevaron esta
acta entera**, y el auditor del primero paro **citando como suyas tres tandas de un libro
que no era el suyo**. `D.48` lo cierra: **un frente nace con su racha en cero y hereda
cero remedios**, y esta linea sigue heredando los suyos porque tiene registro.

---

## TAREA 1. **BLOQUEANTE: LA FECHA QUE SE ESCRIBIO EN EL DATO**

*Escalada de `DATO MOVIDO` en su penultimo escalon (`AUDITOR_FORJA.md` 5.5), encargada
por la `ACTA 31` `9.2`. **Es la primera cosa que el bucle hace al retomar**, y va antes
de minar nada.*

**LA `TAREA 4` DE LA VUELTA 32 ESCRIBIO `17 sep 2026` dentro de `dataset/nodos.jsonl` y
de `bitacora/VEREDICTOS.jsonl` el dia `16`.** Es **la unica** de las `119` fechas escritas
a mano en esas dos sedes que no coincide con la que la maquina estampa en su propia linea.

    python forja.py corregir --nodo <id> --anade "CORRECCION DECLARADA ..." --razon ...

**`D.13`, sin borrar el texto viejo.** La via existe y no hay que construirla. **Publica
la cifra de cuantas celdas tocaste y con que comando las encontraste.**

## TAREA 2. **SEGUIR INSERTANDO EL LOTE 4, QUE ES EL TRABAJO**

    $ python -c (recuento de hoy, 17 sep 2026)
    dataset/nodos.jsonl            : 270 nodos
    bitacora/VEREDICTOS.jsonl      : 396 lineas
    cuarentena/scott_radical_candor    : 75 candidatos en bandeja
    cuarentena/marquet_turn_the_ship   : 3 candidatos en bandeja

**El lote 4 esta CERRADO EN EXTRACCION desde la `ACTA 24`**, asi que **esta vuelta no
mina: inserta.** `D.39`: la insercion de un lote cerrado es automatica.

- **Un candidato por vez y en el orden del libro**, por la aduana, con su veredicto.
- **Las aristas `D.29` que la señal no levanta se declaran por lectura y se cablean en la
  misma vuelta**, que es lo que la vuelta 25 estreno.
- **`NO SE ABRE NINGUN LOTE** (`D.32`), y **el lote 5 (`marquet_turn_the_ship`) NO SE
  TOCA**: sus `3` candidatos se quedan donde estan (`D.39`).
- **El techo de candidatos manda** (`EXTRACTOR.md` 12.4): entre cinco y quince.

> **EL CERROJO ESTA PUESTO** (`D.44`): **una sola corrida escribe el dataset.** Si algo
> dice `INSERCION NO INTENTADA`, no es un fallo tuyo: hay otra corrida viva. **No la
> esquives.**

## TAREA 3. **LA FIDELIDAD, ANTES DE CERRAR**

**`PASOS INVENTADOS` por capitulo** (`D.30`), fila por unidad mas total, **releyendo los
pasos contra su parrafo**. **La escalada se decide sobre el peor capitulo, no sobre el
promedio.** Tope `10`.

---

## MODO AUSTERO (`D.47`), Y AQUI ES DONDE MAS SE NOTA

| | |
|---|---|
| **el reporte** | **nada que el registro ya diga.** Lo que el `loop.log` registro, lo que el acta anterior adjudico y lo que el banco ya argumenta **no se repite** |
| **los discutibles** | **por numero y linea**, sin reabrir el argumento |
| **las cifras** | **talladas**, con la salida del instrumento pegada de su fichero (`D.41`) |
| **los instrumentos** | **CERO nuevos**, salvo que una caida **de DATO** lo exija con su cita |

> **UN REPORTE MAS CORTO NO ES UN REPORTE CON MENOS PRUEBA.** Las guardas de dato quedan
> **intactas**: la aduana entera, el cerrojo, el censo no decreciente y la relectura
> contra el parrafo. **El austero recorta tinta, no control.**

## LO QUE YA ESTA HECHO Y NO SE REHACE

**LAS CIFRAS DE `cap_11` YA ESTAN CORREGIDAS POR REGENERACION** en `docs/loop/REPORTE.md`
(`Y.8.d` y la cabecera de `Y.3.f`), por el punto 3 de la decision del fundador: **`187`
pasos en `16` nodos** y **cuatro firmas**, generadas del dataset con `.v33/cap11.py` y
**no leyendo la tabla que corrigen**. **No las vuelvas a tocar**, y **no las cuentes como
trabajo tuyo**: el `0,00` por ciento de `PASOS INVENTADOS` no se movio, porque cayo el
rotulo y no el dato.

## LO QUE NO SE TOCA EN ESTA VUELTA

- **`src/`, el banco, el arnes y los protocolos** siguen bajo la moratoria de `D.45`
  mientras el frente `grove` este vivo. **Una pregunta de doctrina es PARADA y sube.**
- **`config/umbrales.json`**, ningun umbral.
- **El bucle no funde ramas y el bucle no crea remotos.**
- **Los tres frentes de libro**: `grove` esta **corriendo**, `gerber` y `marquet` estan
  **pausados con su arbol intacto**. Ninguno es asunto de esta linea.

## AL CERRAR

    python scripts/cerrar_reporte.py
    python forja.py credito --anotar ...        una linea por especie, con su cita

**Y COMMITEA Y PUSHEA `docs/loop/`**, como siempre.
