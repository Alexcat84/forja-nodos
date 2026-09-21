# PARA ALEXIS: **EL FRENTE `gerber_emyth` HA MINADO SU LIBRO HASTA DONDE SU PERMISO LLEGA, Y SE DETIENE**

*Escrito por el auditor del bucle al cerrar la `ACTA G8`, que audita la vuelta `8` del frente.
Rama `extraccion-gerber_emyth`, worktree `C:/Users/AlexDesk/Documents/forja-gerber_emyth`.
**`docs/loop/PROMPT_SIGUIENTE.md` queda VACIO**, que es lo que `AUDITOR_FORJA.md` `3` manda.*

> # **NO ES UNA PARADA POR CREDITO. LAS CINCO RACHAS ESTAN EN `0`.**
>
> **ES UNA PARADA POR ALCANCE:** lo que le queda a este libro esta reservado a ti, y lo que viene
> detras es un relevo, y **el relevo no lo hace el bucle** (`PARALELO.md` `5.0.b`, paso `(b)`).

---

## 1. EL MOTIVO, EN UNA TABLA

**Se cumplen DOS de las condiciones de `AUDITOR_FORJA.md` `3`**, y ninguna de las otras cuatro:

| condicion | por que se cumple |
|---|---|
| **DECISION DE ALEXIS** (*cambiar el alcance de la extraccion*) | lo unico que le queda por minar a este libro son `cap_01`, `cap_02` y `cap_03`, **apartados por tu decision** (`d094`), y el `cap17_reservado`, **que es otra clave del tablero con su condicion escrita sin cumplir**. Tomar cualquiera de las dos es cambiar el alcance |
| **CAMPANIA CONSUMADA** (la parada feliz) | el frente ha minado **`19` de las `22` unidades**, sin hueco entre `cap_04` y `cap_22`, y **no le queda ni una unidad permitida**. `PARALELO.md` `5.0.b` paso `(a)` pide **este fichero en el arbol** para que el relevo pueda empezar |

**Y NO HAY GUARDA EN ROJO:** `gate`, `guiones`, `tests`, tallado y censo **los cinco VERDES**, corridos
por mi en este turno.

---

## 2. EL ESTADO EXACTO, MEDIDO EN ESTE TURNO

| | |
|---|---|
| **hash auditado** | `7e823c9` (vuelta `8` del frente), sobre `extraccion-gerber_emyth` |
| **fase** | `MODO_INSERCION=cuarentena`, **regimen ligero** (`D.58`), clase `EXTRACCION`. **Cero inserciones en toda la vida del frente** |
| **nodos del grafo** | **`346`**, los mismos que al abrir. `python forja.py gate` VERDE |
| **nodos de este libro dentro del grafo** | **`0`** |
| **bandeja** | **`22`** candidatos en `cuarentena/gerber_emyth/`, pasados por la aduana en seco, **sin insertar** |
| **unidades del libro** | **`22`** en `fuentes/gerber_emyth/`. **`19` minadas** (`cap_04` a `cap_22`), **`3` sin minar** (`cap_01`, `cap_02`, `cap_03`, las tres en `d094`) |
| **guardas** | `gate` VERDE (`346`), `guiones` VERDE, `tests/test_aceptacion.py` **`350` pruebas `0` fallos**, tallado VERDE (`176` tablas), censo VERDE |
| **credito de la linea** | **las cinco especies en `0`**: `AUDITOR` `0 de 3`, `CIFRA PUBLICADA` `0 de 2`, `CLASE` `0 de 2`, `DATO MOVIDO` `0 de 2`, `REPORTE` `0 de 3` |
| **deuda** | **`49` pendientes, `39` pagadas** al cerrar esta acta (`44`/`39` heredadas, mas las `5` que anoto este turno) |
| **cadencia** | la vuelta `9` saldria `LIBRE`: `van 3 de 5 desde la ultima de saneamiento (la 6)` |

**LOS COMANDOS QUE LO SOSTIENEN, TODOS CORRIDOS HOY:**

    $ python forja.py gate | sed -n '2p'
      nodos verificados: 346
    $ python tests/test_aceptacion.py | tail -1
      total: 350 pruebas, 0 fallos, 0 errores
    $ ls cuarentena/gerber_emyth/*.json | wc -l
    22
    $ ls fuentes/gerber_emyth/*.md | wc -l
    22
    $ python scripts/deuda.py | sed -n '3p'
      pendientes: 49    pagadas: 39

---

## 3. LO QUE ESTE BUCLE COMPROBO ANTES DE PARAR, PARA QUE NO HAYA QUE REPETIRLO

**`D.32` manda que si un acta cierra un lote, mida las dos condiciones de apertura del siguiente y lo
abra en vez de parar. LAS MEDI, Y LAS PUBLICO** (`ACTA G8` `8.2`). Las dos salen verdes en las tres
claves posibles **y las tres estan bloqueadas por una tercera cosa**:

| clave | material en `fuentes/` | en la tabla canonica | `--puedo` | por que NO se abre |
|---|---:|---|---|---|
| `gerber_emyth_cap17_reservado` | `1` | SI | **`SI`** | `ORDEN_DE_LOTES.md` `L27`: lote `11`, **RESERVADO, entra el ultimo**, y su motivo escrito es que **entra cuando su propio libro ya este dentro del grafo**. Hoy hay **`0`** nodos de `gerber_emyth` en el grafo |
| `marquet_turn_the_ship` | `17` | SI | **`NO`** | *esta PAUSADO y NO COSECHADO, tiene `9` candidatos que todavia no han llegado a esta rama*. `D.50`: **se releva ENTERO y el relevo empieza por cosechar su rama** |
| `grove_high_output` | `18` | SI | **`SI`** | **no hay nada que continuar**: `18` de `18` capitulos minados, `ultimo_capitulo` `cap_18`, mineria cerrada en la vuelta `62` de la serial |

**EL BUCLE NO FUNDE RAMAS Y EL BUCLE NO CREA REMOTOS**, asi que lo unico que hago es pedirlo.

---

## 4. LO QUE SE NECESITA DE TI, Y SON CUATRO COSAS

### 4.1. **LA COSECHA DE ESTA RAMA, QUE ES EL PASO `(b)` Y ES TUYO**

**Lo pido, no lo hago** (`AUDITOR_FORJA.md` `3`: *`PARA_ALEXIS.md` PIDE el merge con el estado verde
delante; no lo hace*). El procedimiento entero esta escrito en `PARALELO.md` `5.1` a `5.3`:

    cd /c/Users/AlexDesk/Documents/forja-nodos
    git checkout extraccion-mundo-11
    git merge --no-ff extraccion-gerber_emyth
    python forja.py gate && python forja.py guiones && python tests/test_aceptacion.py && python scripts/cerrar_reporte.py

**CONFLICTOS QUE ESPERAR** (`PARALELO.md` `5.2`): seguros en `REPORTE.md`, `ACTA_AUDITOR.md`,
`loop.log` y `ultimo_*.json`, **y se resuelven conservando LOS DOS**. **En `dataset/`, `bitacora/`,
`censos/` y `config/pares_mutuos.jsonl` no deberia haber ninguno**, y lo tengo medido: este frente
**no toco una sola de esas sedes en toda su vida**, y la vuelta `8` lo vuelve a cumplir
(`git diff --name-only c888e54 7e823c9` fuera de `.gerber_v8/` da tres ficheros, los tres de registro).

### 4.2. **QUE PASA CON `cap_01`, `cap_02` Y `cap_03` (`d094`)**

Son tuyos desde la vuelta `2` del frente: mandaste empezar en `cap_05`. **El frente no los ha tocado
nunca y no los va a tocar sin tu palabra.** Si quieres el libro entero, **son una vuelta de extraccion
mas**; si no, `d094` se cierra declarando que el libro queda minado de `cap_04` en adelante **y eso se
escribe donde se pueda leer dentro de un anio**.

### 4.3. **SI ESTE LIBRO ENTRA O NO ENTRA AL MUNDO `11`, PORQUE LA PREMISA DEL CORTE HA CAMBIADO**

**No lo adjudico yo y no propongo nada.** Solo pongo la cifra nueva delante, que es lo que me toca:

> `PARALELO.md` `4.d` (**21 sep 2026, tu decision**) corto este libro de la campania con una premisa
> medida: que insertar sus candidatos *obligaria a minar los dos libros enteros, y eso es lo que esta
> campania decide no pagar*, **con el frente fotografiado en `10` candidatos y `4` de `22` capitulos.**

**HOY, MEDIDO POR MI:** **`22` candidatos y `19` de `22` capitulos.** **Ese coste ya esta pagado.** Lo
que la decision del `21` sep decidio no pagar **se pago entre la vuelta `4` y la `8`**. Es `d125`,
anotada en la vuelta `7` con cifras mas viejas, **y la vuelvo a medir aqui porque ha vuelto a cambiar.**

### 4.4. **LA FIRMA DE LOS CAPITULOS MINADOS EN CERO, QUE ES DE UN ACTA Y NO DE UNA MEDIDA** (`d096`)

`src/tablero.py` no puede deducir que un capitulo se leyo entero y dio cero: **se declara en
`config/frentes.json`, clave `minados_en_cero`, con la cita del acta que lo firma.** Hoy ese fichero
trae de `gerber_emyth` solo `cap_05`, `cap_06`, `cap_09` y `cap_10` (`ACTA G2` y `ACTA G3`), **y faltan
cinco**, con su acta firmante cada uno:

| capitulo | acta que lo firma |
|---|---|
| `cap_16` | `ACTA G5`, `SIN SUPERFICIE` con su razon leida |
| `cap_17` | `ACTA G5`, `SIN SUPERFICIE` con su razon leida |
| `cap_20` | **`ACTA G8` `3.2`**, la carta a Sarah mas los agradecimientos |
| `cap_21` | **`ACTA G8` `3.2`**, el `Epilogue` |
| `cap_22` | **`ACTA G8` `3.2`**, el `Afterword` mas el back matter |

**NO LOS ESCRIBO YO:** `config/` no es sede del auditor (`5.6`) y un frente no toca maquinaria
(`D.45`, `D.47`). **Y mientras falten, el tablero seguira diciendo `ult cap = cap_19` de un libro
minado hasta `cap_22`** (`d131`, corregida por `d132`), **y el `cap_17` que hoy si aparece lo pone
`d106` por el motivo equivocado**, no esta firma.

---

## 5. COMO SE RETOMA

**SI COSECHAS Y CIERRAS EL FRENTE** (lo que `PARALELO.md` `6` describe):

    cd /c/Users/AlexDesk/Documents/forja-nodos
    git worktree remove ../forja-gerber_emyth
    python forja.py tablero --escribir

**La rama NO se borra**: es el registro de como se extrajo este libro.

**SI QUIERES QUE ESTE FRENTE SIGA** (la unica via que no necesita cosecha), lo que puede hacer es
**una sola cosa y hay que decirsela**: **levantar `d094` y minar `cap_01`, `cap_02` y `cap_03`**. En
ese caso, el encargo lo escribe el auditor y el frente se relanza con su comando de siempre:

    cd /c/Users/AlexDesk/Documents/forja-gerber_emyth && \
      RAMA=extraccion-gerber_emyth MODO_INSERCION=cuarentena MAX_VUELTAS=20 \
      bash orquestador_forja.sh

**LO QUE NO SE PUEDE HACER SIN TI:** insertar (ningun frente inserta, `D.45`), tomar `marquet` (`D.50`,
el relevo empieza por su cosecha), abrir el `cap17_reservado` (su condicion escrita no se cumple) ni
tocar `src/`, el banco, el arnes o los protocolos (`D.45`, `D.47`).

---

## 6. LO QUE DEJA ESTE TURNO ESCRITO, PARA QUE NADA SE PIERDA

| donde | que |
|---|---|
| `docs/loop/ACTA_AUDITOR.md` | **`ACTA G8`**: las `16` piezas de las tres fronteras recompuestas con codigo mio y al digito, los tres `CERO CANDIDATOS` releidos por mi leyendo los tres capitulos enteros, el discutible sostenido, la caida de la cita verbatim y mis dos errores propios |
| `docs/loop/DEUDA.jsonl` | `d128` a `d132`, **`5` anotadas y `0` pagadas en mi turno** |
| `docs/loop/PROMPT_SIGUIENTE.md` | **VACIO**, por esta parada |
| **los punteros que la vuelta que INSERTE no puede perder** | `d098` y `d104` (`D.37`, las dos ternas sin cabeza, `cap_05` `L29` y `cap_12` `L21`), `d108` (releer `cap_14` `L27` contra `L117`) y **`d111`, la serie de `cap_13` medida en `0` de `7` y con su primera arista declarable ya identificada** (`REPORTE.md` `G8.5.c`) |

---

**Cero guiones largos y cero guiones medios. El bucle queda detenido en esta rama y no volvera a abrir
vuelta hasta que `docs/loop/PROMPT_SIGUIENTE.md` deje de estar vacio.**
