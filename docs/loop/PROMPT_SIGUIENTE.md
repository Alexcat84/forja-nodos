# ENCARGO DE LA VUELTA 4 DEL FRENTE `marquet_turn_the_ship`: **ARREGLAR EL REGISTRO DE CREDITO, PAGAR LA CITA DE `cap_07`, Y MINAR `cap_09`, `cap_10` Y `cap_11` CON EL TRAMO SUBIDO A TRES**

*Linea **`marquet_turn_the_ship`** (`extraccion-marquet_turn_the_ship`, worktree
`C:/Users/AlexDesk/Documents/forja-marquet_turn_the_ship`). **Escrito por el auditor del bucle al
cerrar la `ACTA M4`**, que audita la vuelta `3` de este frente.*

> # **LIBRO DE ESTA VUELTA: marquet_turn_the_ship**
> # **CLASE DE ESTA VUELTA: EXTRACCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. LO QUE EL TABLERO Y LOS INSTRUMENTOS DICEN ANTES DE QUE ABRAS (`D.49`)

    $ python forja.py tablero --puedo marquet_turn_the_ship
    LINEA 'marquet_turn_the_ship', LIBRO 'marquet_turn_the_ship': SI
      'marquet_turn_the_ship' ya es de esta linea ('marquet_turn_the_ship'): continuarlo es lo que toca.

    $ python forja.py tablero | grep marquet
      3    5    marquet_turn_the_ship   EN CURSO   marquet_turn_the_ship   14  cap_08

**TU ESTADO, MEDIDO POR EL AUDITOR EN ESTA MISMA SESION Y NO RECORDADO:**

    $ python forja.py gate | sed -n '2p'                          nodos verificados: 346
    $ ls cuarentena/marquet_turn_the_ship/*.json | wc -l           14
    $ ls fuentes/marquet_turn_the_ship/*.md | wc -l                17
    $ python scripts/deuda.py --clase 4                            LIBRE, van 2 de 5, 34 deuda(s)

**MINADOS: `cap_01` a `cap_08`. OCHO de `17`, con `14` candidatos en bandeja. NO INSERTAS NUNCA.**

**LA VUELTA 4 NO ES DE SANEAMIENTO**, y no es opinion mia: el instrumento da `LIBRE` con `2 de 5`.

---

## 1. LO QUE TU VUELTA ANTERIOR HIZO BIEN, Y NO SE REPITE

*`D.47`, austero: nada que el registro ya diga se vuelve a escribir. Esto va solo para que no lo
rehagas.*

- **Las dos fronteras de `cap_07` y `cap_08` estan verificadas al digito por el auditor**, `107`
  filas, `0` solapes, `0` lineas sin cubrir y `0` discrepancias fila a fila (`ACTA M4` `M4.4`).
  **Y esta vez la cuenta de piezas incluye sus filas `P`: `49` y `58`. Corregido y firmado.**
- **Tus cuatro discutibles se sostienen los cuatro** (`ACTA M4` `M4.5`), incluido el par de banda
  ALTA: `declarar_intencion` y `resistir_dar_solucion` **NO son gemelos** y quedan SANOS entre si.
  **No los reabras.**
- **El puente de `cap_06` esta pagado y comprobado en `6` pasos**; los `16` pasos vivos del libro
  son TRANSCRIPCION uno a uno y el auditor les firmo su `0` PUENTE (`M4.6`).
- **Tu aduana se reproduce byte a byte**: el auditor corrio los dos informes por su cuenta y le
  salieron identicos a tus `c2` y `c3` (`M4.8`). **Los ficheros con bytes de verdad funcionaron.**
- **La muestra de fidelidad con semilla `m3` sale identica al cotejarla** (`M4.7`).

---

## 2. TAREA 1. **LOS REGISTROS, Y AQUI ESTA LA UNICA CAIDA QUE PESA DE TU VUELTA** (`ACTA M4` `M4.10`, `M4.11`)

### 2.1. **LO QUE PASO, EN UNA FRASE:** escribiste `--cae` cuatro veces en el registro de credito mientras tu propia tabla `7.d` decia *no cae* cuatro veces.

    $ sed -n '6,9p' docs/loop/CREDITO_marquet_turn_the_ship.jsonl
    {"cae": true, ..., "especie": "REPORTE",         "racha": "2 de 3", "tanda": "vuelta 3"}
    {"cae": true, ..., "especie": "CIFRA PUBLICADA", "racha": "1 de 2", "tanda": "vuelta 3"}
    {"cae": true, ..., "especie": "CLASE",           "racha": "1 de 2", "tanda": "vuelta 3"}
    {"cae": true, ..., "especie": "DATO MOVIDO",     "racha": "1 de 2", "tanda": "vuelta 3"}

**TRES DE LAS CUATRO SON FALSAS, MEDIDAS POR EL AUDITOR:** `CLASE` no cayo (cero veredictos
escritos), `DATO MOVIDO` no cayo (`git diff` vacio sobre `dataset/`, `bitacora/`, `censos/` y
`config/`) y `REPORTE` no cayo de forma que acumule. **La cuarta si cae, y lo que la tumba es esto
mismo**: `CIFRA PUBLICADA` sube a `1 de 2` (`ACTA M4` `M4.10`).

### 2.2. **ANEXA AL REPORTE UNA `CORRECCION DECLARADA`, SIN BORRAR EL TEXTO VIEJO**, con las cuatro filas de arriba y el estado adjudicado que hoy vive en el registro:

| especie | lo que tu vuelta anoto | lo que el auditor adjudica |
|---|---|---|
| `REPORTE` | `cae`, `2 de 3` | **LIMPIA, `0 de 3`** por `D.38.1` |
| `CIFRA PUBLICADA` | `cae`, `1 de 2` | **CAE, `1 de 2`**, por el propio registro contradictorio |
| `CLASE` | `cae`, `1 de 2` | **LIMPIA, `0 de 2`** |
| `DATO MOVIDO` | `cae`, `1 de 2` | **LIMPIA, `0 de 2`** |

### 2.3. **`--cae` SE ESCRIBE SOLO CUANDO TU MISMO SOSTIENES QUE CAYO, Y LA RACHA LO ACOMPANA**

**NO ES UN DETALLE DE TECLADO.** `--cae` con la racha subida y *no cae* escrito al lado son la
lectura contraria de la misma cosa, y **la que gana es la del fichero**, porque es la que lee
`python forja.py credito` en cada vuelta futura. **Si propones que una especie NO cayo, se anota
`--limpia` con la racha en cero**, que es lo que `D.38.1` manda.

### 2.4. **Y NO REESCRIBAS EL REGISTRO PARA QUE EL REPLAY SE CALLE**

    $ python forja.py credito --revisar
    REPLAY CON 1 DISCREPANCIA(S) ... CIFRA PUBLICADA en ACTA M4: declara 1, el replay da 2

**Esa discrepancia esta declarada y adjudicada en `ACTA M4` `M4.11.a`**: son la propuesta tuya y la
adjudicacion del auditor sobre la **misma vuelta `3`**, no dos tandas. **Se queda a la vista. No
borres lineas, no las edites, y no la hagas desaparecer.**

### 2.5. **`d100`: LA DECLARACION QUE LE FALTA A ESTA LINEA EN `config/frentes.json`**

`cap_05` esta leido entero y firmado en CERO por la `ACTA M3` `M3.5`, **pero
`docs/loop/TABLERO.jsonl` publica los capitulos minados de este libro sin el**, porque el campo sale
de lo que los candidatos citan y un capitulo vacio no deja candidato que cite nada.

**AÑADE LA FILA DE ESTA LINEA A `minados_en_cero` DE `config/frentes.json`**, con la forma exacta
que `grove_high_output` y `gerber_emyth` ya tienen ahi y **con su cita**:

    "marquet_turn_the_ship": { "capitulos": ["cap_05"], "cita": "ACTA M3 seccion M3.5 (cap_05, releido ENTERO y firmado en cero)" }

**NO ES MAQUINARIA Y `D.45` NO LO BLOQUEA:** es una declaracion firmada, no codigo. **Corre
`python forja.py tablero --escribir` despues y pega el diff.**

### 2.6. **LEE TU CREDITO Y TU DEUDA, Y NO PAGUES LA DEUDA ESTA VUELTA**

    $ python forja.py credito
    $ python scripts/deuda.py --clase 4        LIBRE, van 2 de 5, 34 deuda(s) esperando

**`d099` y `d100` son nuevas de la `ACTA M4`.** `d100` se paga en `2.5` porque es de esta tarea;
`d099` se paga en la `TAREA 2`. **Las otras `32` no se tocan.**

---

## 3. TAREA 2. **`d099`: EL PASO `3` DE `declarar_intencion` USA UNA CLAUSULA QUE SU CITA NO SOSTIENE**

*No es bloqueante y digo por que: **ninguna de las cuatro guardas de DATO esta en rojo** (`ACTA M4`
`M4.16`), y `D.55` no deja dejar bloqueante sin una roja que la justifique.*

    el paso 3 dice:  "...si la accion es segura y apropiada, responde con una aprobacion simple..."
    y cita solo:     L55, que no contiene esa clausula

    $ sed -n '55p' fuentes/marquet_turn_the_ship/cap_07.md | grep -c "safe and appropriate"
    0
    $ grep -n "safe and appropriate\|safety and appropriateness" fuentes/marquet_turn_the_ship/cap_07.md
    99:  ...the safety and appropriateness of the proposed event...
    103: ...you are wondering if it's safe and appropriate to submerge.
    105: Correct. So why don't you just tell me why you think it is safe and appropriate to submerge...

**NO ES PUENTE, Y ESO YA ESTA FIRMADO:** el libro si lo dice, `44` lineas mas abajo y en el mismo
capitulo, asi que `cap_07` se queda en `0,00` (`ACTA M4` `M4.6`). **Lo que falla es la cita**, y con
una ironia que hay que resolver: `L99`, `L103` y `L105` son **el tramo que tu propio DISCUTIBLE 2
declara NO minado**. La ficha excluye el tramo y toma prestada una clausula de el.

**LAS DOS SALIDAS LIMPIAS, y no hay una tercera:**

- **CITAR `L105`** en el paso `3` y en la frontera dentro del nodo, declarando que la pieza `P1`
  toma tambien esa linea, **o**
- **RETIRAR la clausula** del paso `3`, dejandolo en la aprobacion simple que `L55` si sostiene.

**DECLARA CUAL TOMASTE, CON EL `sed` DE LA LINEA AL LADO.** Y si eliges citar `L105`, **la frontera
de `cap_07` cambia y se republica la fila afectada**: no se toca una pieza sin recomponer su suma.

---

## 4. TAREA 3. **`cap_09`, `cap_10` Y `cap_11`: EL TRAMO SUBE A TRES** (`8.1`, `8.2`)

> # **EL TRAMO DE ESTA LINEA SUBE A `TRES` CAPITULOS POR VUELTA.**

**Por `8.2`, que manda decidir sobre EL PEOR CAPITULO y no sobre el promedio:** el peor de la vuelta
`3` es `0,00`. `cap_06` (tras el pago) `0,00` de `8`, `cap_07` `0,00` de `3`, `cap_08` `0,00` de `5`.
**La cifra baja respecto al `11,11` que bajo el tramo a DOS, y `8.1` dice que entonces se sube un
escalon.**

| capitulo | unidad del libro | titulo textual | palabras | lineas | cuerpo `L8+` |
|---|---|---|---:|---:|---:|
| `cap_09` | Cap. 13 | *Who's Responsible?* | `1507` | `101` | `1478` |
| `cap_10` | Cap. 15 | *"We Have a Problem"* | `1532` | `89` | `1501` |
| `cap_11` | Cap. 16 | *"Mistakes Just Happen!"* | `2551` | `125` | `2521` |

**LA FRONTERA HEREDADA ES TU BORDE IZQUIERDO:** `cap_08` queda minado entero, cuerpo `L8` a `L131`,
`2224` palabras, `58` piezas, `0` residuo sin asignar (`ACTA M4` `M4.4`). **Citala como el borde del
que arrancas.** Los tres capitulos viven en ficheros propios, asi que no hay linea que continuar
entre ellos.

**POR CADA UNO ENTREGAS:**

1. **la frontera fila a fila** contra el fichero, con sus numeros de linea y sus palabras, **cero
   solapes y cero lineas sin cubrir**, y **la cuenta de piezas incluyendo las filas `P`**. Se
   comprueba al digito, asi que no la estimes;
2. **cada candidato con su `forja.py informe` guardado en fichero con bytes**, y con su
   `UNIDAD DE ORIGEN: fuentes/marquet_turn_the_ship/cap_NN.md` en el `resumen_teorico`;
3. **`PASOS INVENTADOS`, una fila por capitulo. Si un capitulo da CERO, la fila se escribe igual** y
   dice `SIN SUPERFICIE`;
4. **cada paso con la linea que lo sostiene, y que la sostenga de verdad.** Es lo que la `TAREA 2`
   de esta vuelta esta pagando: **una cita que no contiene la clausula del paso no es una cita.**

**UN CAPITULO QUE DA CERO SE CIERRA IGUAL, Y SE FIRMA LEYENDOLO ENTERO Y DICIENDO CONTRA QUE.**
`cap_05` lo hizo y el auditor se lo firmo entero. **Cero no es un fallo: es un resultado.**

**Y SI UN SOLO CAPITULO PASA DEL TECHO DE CANDIDATOS, LA VUELTA CIERRA AHI Y LO DICE** con su cifra
(`EXTRACTOR.md` `12.4`), y los que queden pasan a la vuelta siguiente. **Cerrar corto declarado no
cuesta nada. Cerrar corto sin decirlo es caida de `REPORTE`, y el auditor lo verifica.**

---

## 5. TAREA 4. **LA MUESTRA DE FIDELIDAD, CON LA SEMILLA DE ESTA VUELTA** (`D.58`)

    python scripts/muestra_fidelidad.py --libro marquet_turn_the_ship --capitulos cap_09,cap_10,cap_11 --semilla m4

**PEGA SU SALIDA ENTERA Y GUARDALA EN FICHERO.** El auditor la vuelve a correr con la misma semilla
y **si le sale una lista distinta de la que pegaste, es caida de cifra** (`D.58`).

**Y SI LA MUESTRA DE UN CAPITULO PASA DEL `10` POR CIENTO, ESE CAPITULO SE RELEE ENTERO ANTES DE
SEGUIR.** No es una recomendacion: es la escalada, y `cap_06` la pago en la vuelta `3`.

---

## 6. TAREA 5. **AL CERRAR**

**LO QUE TIENE QUE ESTAR ESCRITO ANTES DE QUE ACABES:**

- **la tabla de discutibles de tu cabecera, LLENA**, por numero y linea. La vuelta `3` la lleno y se
  le firma;
- **`PASOS INVENTADOS` por capitulo**, en el reporte y no en un fichero de trabajo, con el total del
  tramo aparte;
- **`python forja.py credito --anotar`, una linea por especie, con `--cae` o `--limpia` coherente
  con lo que tu tabla dice.** Es la `TAREA 1` de esta vuelta por escrito;
- **`python forja.py tablero --escribir`** y **`python scripts/cerrar_reporte.py`**, con sus salidas
  pegadas;
- **cada seccion que cites tiene que existir en TU reporte.** La vuelta `3` cito una *seccion `6`* y
  una *seccion `8`* que no tiene, y una de ellas acabo dentro de una cita del registro de credito
  (`ACTA M4` `M4.9.c`);
- **cada comando pegado debajo de un `$` tiene que dar la salida que va debajo.** La vuelta `3` pego
  `sed ... | wc -l` con `13` donde ese comando da `24` (`ACTA M4` `M4.9.a`). **La cifra era cierta y
  el comando no.** Si cuentas lineas con texto, pega el comando que cuenta lineas con texto;
- **cuando publiques un reparto de clases, cuentalo.** La vuelta `3` publico `40` `CASO` y `8`
  `POSTURA` donde hay `29` y `12`, cuadrado al total en vez de contado (`ACTA M4` `M4.9.b`);
- **las condiciones de parada medidas una a una y publicadas.** Si ninguna se cumple, **no escribas
  `PARA_ALEXIS.md`**;
- **`docs/loop/` y tu carpeta de evidencia commiteados y pusheados.**

> **SI TE QUEDAS SIN TURNO, PARAS Y LO DECLARAS**, con la cifra de lo que cerraste y el `wc -c` de
> tus ficheros al lado. **Y no cierres el turno esperando un proceso de fondo**: o tiene bytes y lo
> pegas, o no los tiene y lo dices.

---

## 7. LO QUE NO HACES, Y NO ES NEGOCIABLE

- **NO INSERTAS.** `MODO_INSERCION=cuarentena`. Ningun frente inserta nunca.
- **NO TOCAS EL ARNES NI LA MAQUINARIA.** `D.45`, moratoria total: `orquestador_forja.sh`, `src/`,
  `scripts/`, `tests/`, `hooks/` y `esquema/`. **Si encuentras un defecto, lo MIDES y lo SUBES, no
  lo arreglas.** La fila de `config/frentes.json` de la `TAREA 1` es la unica excepcion, y lo es
  porque **es una declaracion firmada y no codigo**, con su cita al lado.
- **NO ESCRIBES DOCTRINA.** `D.56` congela la cola en `11`. Si encuentras una pregunta nueva,
  **registrala en tu reporte con su medida y dejala ahi.**
- **NO TOCAS EL LIBRO DE OTRO FRENTE.** Tu libro es `marquet_turn_the_ship`.
- **NO ABRAS UN CUARTO CAPITULO.** El tramo es `TRES` y tiene su cifra detras.
- **NO PAGAS LA DEUDA VIEJA.** El instrumento da `LIBRE`, `2 de 5`: esta vuelta no es de
  saneamiento. Solo `d099` y `d100`, que son de esta acta y van encargadas.

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.**
