# ENCARGO DE LA VUELTA 3 DEL FRENTE `marquet_turn_the_ship`: **PAGAR EL PUENTE DE `cap_06`, CERRAR SU ADUANA, Y MINAR `cap_07` Y `cap_08`**

*Linea **`marquet_turn_the_ship`** (`extraccion-marquet_turn_the_ship`, worktree
`C:/Users/AlexDesk/Documents/forja-marquet_turn_the_ship`). **Escrito por el auditor del bucle al
cerrar la `ACTA M3`**, que audita la vuelta `2` de este frente.*

> # **LIBRO DE ESTA VUELTA: marquet_turn_the_ship**
> # **CLASE DE ESTA VUELTA: EXTRACCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. LO QUE EL TABLERO DICE ANTES DE QUE ABRAS (`D.49`)

    $ python forja.py tablero --puedo marquet_turn_the_ship
    LINEA 'marquet_turn_the_ship', LIBRO 'marquet_turn_the_ship': SI
      'marquet_turn_the_ship' ya es de esta linea: continuarlo es lo que toca.
    $ python forja.py tablero | grep marquet
      3    5    marquet_turn_the_ship   EN CURSO   marquet_turn_the_ship   12   cap_06

**TU ESTADO, MEDIDO Y NO RECORDADO:**

    $ python forja.py gate | sed -n '2p'                        nodos verificados: 346
    $ ls cuarentena/marquet_turn_the_ship/*.json | wc -l         12
    $ ls fuentes/marquet_turn_the_ship/*.md | wc -l              17

**MINADOS: `cap_01` a `cap_06`. SEIS de `17`, con `12` candidatos en bandeja. NO INSERTAS NUNCA.**

---

## 1. LO QUE TU VUELTA ANTERIOR HIZO BIEN, Y NO SE REPITE

*`D.47`, austero: nada que el registro ya diga se vuelve a escribir. Esto va solo para que no lo
rehagas.*

- **Las tres fronteras de `cap_04`, `cap_05` y `cap_06` estan publicadas y verificadas al digito por
  el auditor**, `121` filas y `0` discrepancias (`ACTA M3` `M3.4`). **No las vuelvas a levantar.**
- **`cap_05` da CERO y esta firmado tras leerlo entero** (`M3.5`). **Cerrado.**
- **Tus tres discutibles se sostienen los tres** (`M3.6`). **No los reabras.**
- **Los tres candidatos llevan su `UNIDAD DE ORIGEN` y su cita de linea con `sed` pegado.**

---

## 2. TAREA 1. **LOS REGISTROS** (`ACTA M3` `M3.17` y `M3.18`)

1. **Anexa al reporte una `CORRECCION DECLARADA`, sin borrar el texto viejo**, con estas tres
   cifras que el auditor reconto:

   | donde | dice | es |
   |---|---|---|
   | `1.b` pegado y `1.g` tabla | `piezas: 24`, *unidades leidas `24`*, *residuo `23`* | **`25`, `25` y `24`** |
   | `3.b` pegado | `piezas: 49` | **`51`** |
   | `2.d` prosa | *los ocho mecanismos son capitulos por delante de este tramo* | **`cap_06` ES de este tramo**, y su primer mecanismo lo minaste tu en la `TAREA 3` |

2. **`PASOS INVENTADOS POR CAPITULO` se publica en el reporte, una fila por capitulo**, con la cifra
   que el acta firmo: `cap_04` **`0,00`** (`0` de `5`), `cap_05` **SIN SUPERFICIE**, `cap_06`
   **`11,11`** (`1` de `9`), el tramo **`7,14`** (`1` de `14`). **La fila de `cap_06` no es `0,00` y
   el motivo esta en `M3.7.2`.**

3. **Lee tu credito**, que el auditor abrio con la tanda `ACTA M3` al cerrar esta acta. **Tu racha
   de `REPORTE` esta en `1 de 3` y las otras cuatro en cero**, y las cinco viven en
   `docs/loop/CREDITO_marquet_turn_the_ship.jsonl`:

       python forja.py credito

4. **Lee `docs/loop/DEUDA.jsonl`** y mira las cinco filas que la `ACTA M3` anoto, **`d094` a
   `d098`**. **No las pagues
   esta vuelta**, y no es una opinion mia:

       $ python scripts/deuda.py --clase 3
       LIBRE
         van 2 de 5 desde la primera vuelta de la linea 'marquet_turn_the_ship' (la 1),
         que todavia no ha saneado nunca, con 27 deuda(s) esperando

---

## 3. TAREA 2. **BLOQUEANTE: EL PUENTE VIVO DE `cap_06`** (`D.30`, `D.55`)

> **Es la unica bloqueante de esta vuelta y cita su guarda de DATO en rojo:** la fidelidad `D.30`
> con puente, en `ACTA M3` `M3.15`.

**El paso `7` de `cuarentena/marquet_turn_the_ship/aplicar_ejercicio_codigo_genetico_control.json`
es PUENTE**, adjudicado por el auditor contra su linea:

    $ sed -n '113p' fuentes/marquet_turn_the_ship/cap_06.md
    When I've conducted this exercise, I usually find that the worries fall into two broad
    categories: issues of competence and issues of clarity. ... Both of these can be resolved.

    el paso escrito: "Lee las preocupaciones que salgan clasificandolas: casi siempre caen en
    dos categorias, competencia tecnica y claridad organizacional, y las dos se pueden resolver."

**EL LIBRO OBSERVA, EL PASO MANDA.** `L111` ya encarga ordenar y clasificar, y ese es tu paso `6`.

**LAS DOS SALIDAS LIMPIAS, y no hay una tercera:**

- **RETIRARLO** con `python scripts/retirar_paso.py`, o
- **REESCRIBIRLO sin imperativo**, como lo que el libro dice que pasa y no como algo que el lector
  deba hacer.

**NO INVENTES UN PASO NUEVO PARA TAPAR EL HUECO.** `D.30`: *un puente no se queda callado dentro de
un nodo.* **Y declara cual de las dos salidas tomaste, con el `sed` de la linea al lado.**

---

## 4. TAREA 3. **CIERRA LA ADUANA QUE LA VUELTA `2` DEJO ABIERTA, Y GUARDA SU SALIDA**

**Tu `3.f` dijo *PASADOS POR LA ADUANA EN SECO EN EL MISMO ACTO* sobre dos candidatos que no la
tuvieron.** El unico fichero que esa corrida abrio tiene `0` bytes:

    $ ls -la .m2/informe_aplicar_ejercicio.txt          0 bytes
    $ ls .m2/ | grep -c asignar                         0

**CORRE LAS DOS, DE UNA EN UNA, Y REDIRIGE CADA UNA A SU FICHERO ANTES DE SEGUIR:**

    python forja.py informe cuarentena/marquet_turn_the_ship/aplicar_ejercicio_codigo_genetico_control.json > .v3m/aduana/c1.txt
    python forja.py informe cuarentena/marquet_turn_the_ship/asignar_responsable_unico_evolucion_planificada.json > .v3m/aduana/c2.txt

**LA DE `aplicar_ejercicio` SE CORRE DESPUES DE PAGAR SU PUENTE**, no antes: la ficha va a cambiar.

> **CUENTA CON NUEVE MINUTOS POR INFORME.** El auditor lo midio hoy: `9` minutos y `19` segundos con
> la poblacion en `449`. **Son casi veinte minutos de reloj para los dos, y esa es la razon mecanica
> por la que tu vuelta anterior no llego.** Lanzalos temprano y escribe el reporte mientras corren,
> **pero no escribas que pasaron hasta que el fichero tenga bytes.**

**Y PEGA LAS TRES COLUMNAS, no una:** `ENTRARIAN`, `BLOQUEARIAN` y `CAERIAN`. Un `0 CAERIA` solo
cuenta media verdad.

---

## 5. TAREA 4. **`cap_06` SE RELEE ENTERO ANTES DE ABRIR `cap_07`** (`D.58`)

**Es la escalada escrita, no una recomendacion:** *si la muestra de un capitulo pasa del `10` por
ciento de pasos inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.* **`cap_06` dio `11,11`.**

**ES BARATO Y POR ESO VA ENTERO:** su frontera de `51` piezas ya esta publicada y verificada al
digito, asi que **lo que relees son sus `9` pasos contra sus `51` filas**, no el capitulo desde
cero. Lo que tienes que contestar, con su `sed` pegado:

1. **de las `49` filas `R`, ninguna era nodo**, y en particular las de `L83` a `L95` (el caso de
   Santa Fe del cambio de una palabra) y las de `L115` a `L125`;
2. **los `9` pasos que sobreviven** siguen siendo TRANSCRIPCION uno a uno tras pagar el puente.

**Y PUBLICA LA CIFRA DE `cap_06` OTRA VEZ tras la relectura.** Si baja a `0,00`, se dice; si no, se
dice igual.

---

## 6. TAREA 5. **`cap_07` Y `cap_08`, DOS CAPITULOS Y NO TRES**

> # **EL TRAMO DE ESTA LINEA BAJA A `DOS` CAPITULOS POR VUELTA.**

**Por `8.1`:** `cap_06` da `11,11`, por encima del tope de `10`, **se baja un escalon** desde los
tres con los que corrio la vuelta `2`. Y por el otro camino llega al mismo sitio: **la `ACTA M2`
`4.4` ya lo habia dejado en `DOS`** por el `15,09` de `cap_03`, y ese encargo nunca te llego.

| capitulo | unidad del libro | titulo textual | palabras | lineas |
|---|---|---|---:|---:|
| `cap_07` | Cap. 11 | *I Intend To . . .* | `2222` | `127` |
| `cap_08` | Cap. 12 | *Up Scope!* | `2253` | `131` |

**LA FRONTERA HEREDADA ES TU BORDE IZQUIERDO:** `cap_06` queda minado entero, cuerpo `L8` a `L139`,
`2905` palabras, `51` piezas, `0` residuo sin asignar (`ACTA M3` `M3.4`). **Citala como el borde del
que arrancas.** `cap_07` vive en otro fichero, asi que no hay linea que continuar entre los dos.

**POR CADA UNO ENTREGAS:**

1. **la frontera fila a fila** contra el fichero, con sus numeros de linea y sus palabras, **cero
   solapes y cero lineas sin cubrir.** Se comprueba al digito, asi que no la estimes. **Y la cuenta
   de piezas incluye las filas `P`**, que es lo que la vuelta `2` se dejo fuera;
2. **cada candidato con su `forja.py informe` guardado en fichero** y con su
   `UNIDAD DE ORIGEN: fuentes/marquet_turn_the_ship/cap_NN.md` en el `resumen_teorico`;
3. **`PASOS INVENTADOS`, una fila por capitulo. Si un capitulo da CERO, la fila se escribe igual** y
   dice `SIN SUPERFICIE`;
4. **la muestra de fidelidad con la semilla de esta vuelta:**

       python scripts/muestra_fidelidad.py --libro marquet_turn_the_ship --capitulos cap_07,cap_08 --semilla m3

**UN CAPITULO QUE DA CERO SE CIERRA IGUAL, Y SE FIRMA LEYENDOLO ENTERO Y DICIENDO CONTRA QUE.**
`cap_05` acaba de hacerlo y el auditor se lo firmo entero. **Cero no es un fallo: es un resultado.**

---

## 7. AL CERRAR, Y AQUI ES DONDE SE CAYO LA VUELTA `2`

**TU VUELTA ANTERIOR SE PARO EN LA `TAREA 3` Y LO QUE ESCRIBIO DESPUES NO LO DIJO.** El turno
termino solo (`stop_reason: end_turn`), y `REPORTE.md` se escribio por ultima vez **cuatro minutos
despues** de lanzar la aduana que no cerro. **Dos lineas declarando el cierre corto entraban ahi.**

> **SI TE QUEDAS SIN TURNO, PARAS Y LO DECLARAS**, con la cifra de lo que cerraste y el `wc -c` de
> tus ficheros al lado. **Un cierre corto declarado no cuesta nada; uno sin declarar es caida de
> `REPORTE`** (`EXTRACTOR.md` `12.4`). **Y no cierres el turno esperando un proceso de fondo**: o
> tiene bytes y lo pegas, o no los tiene y lo dices.

**LO QUE TIENE QUE ESTAR ESCRITO ANTES DE QUE ACABES:**

- **la tabla de discutibles de tu cabecera, LLENA.** La vuelta `2` la dejo vacia con tres
  discutibles escritos debajo;
- **`PASOS INVENTADOS` por capitulo**, en el reporte y no en un fichero de trabajo;
- **la muestra de fidelidad con su semilla y su salida pegada**;
- **el saldo de cada tarea y el cierre de la vuelta**;
- **`python forja.py credito --anotar`**, una linea por especie;
- **`python forja.py tablero --escribir`** y **`python scripts/cerrar_reporte.py`**. **El volcado
  de `docs/loop/TABLERO.jsonl` se quedo en `cap_03` y en `9` candidatos**, porque la vuelta `2` no
  cerro: la vista calculada ya dice `cap_06` y `12`, pero el fichero no (`ACTA M3` `M3.21.c`);
- **`docs/loop/` y tu carpeta de evidencia commiteados.** La vuelta `2` dejo el reporte modificado y
  las tres fichas **sin seguir por git**;
- **las condiciones de parada medidas una a una y publicadas.** Si ninguna se cumple, **no escribas
  `PARA_ALEXIS.md`.**

---

## 8. LO QUE NO HACES, Y NO ES NEGOCIABLE

- **NO INSERTAS.** `MODO_INSERCION=cuarentena`. Ningun frente inserta nunca.
- **NO TOCAS EL ARNES NI LA MAQUINARIA.** `D.45`, moratoria total: `orquestador_forja.sh`, `src/`,
  `scripts/`, `tests/`, `hooks/` y `esquema/`. **Si encuentras un defecto, lo MIDES y lo SUBES en tu
  `PARA_ALEXIS`, no lo arreglas.** La `ACTA M3` subio tres y no arreglo ninguno.
- **NO ESCRIBES DOCTRINA.** `D.56` congela la cola en `11`. Si encuentras una pregunta nueva,
  **registrala en tu reporte con su medida y dejala ahi.**
- **NO TOCAS EL LIBRO DE OTRO FRENTE.** Tu libro es `marquet_turn_the_ship`.
- **NO ABRAS UN TERCER CAPITULO.** El tramo es `DOS` y tiene su cifra detras.

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.**
