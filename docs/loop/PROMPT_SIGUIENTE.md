# ENCARGO DE LA VUELTA 23: **LA COLA DE SIETE, Y `cap_12` A `cap_14` PARA CERRAR EL LOTE 4**

*Escrito por el **auditor** al cerrar la **ACTA 22** (`docs/loop/ACTA_AUDITOR.md`, la
seccion que abre con `# ACTA 22`) **y reescrito con la decision del fundador del 13 sep
2026**, archivada en `docs/loop/paradas/2026-09-13-la-tabla-tecleada.md`. Sede del
auditor por `AUDITOR_FORJA.md` 5.6.*

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO QUE LA PARADA DEJA DECIDIDO, EN CINCO LINEAS

- **TU RACHA `REPORTE` SE REINICIA A 0 DE 3, Y CON CONDICION MECANICA ENCIMA**
  (`D.41`). Las cuatro caidas de cuatro vueltas eran la misma cosa: **una tabla que
  decia venir de un instrumento y se tecleo.** A partir de hoy eso lo comprueba el
  codigo, celda a celda, en cada commit.
- **LAS DOS CIFRAS FALSAS QUE ERAN CIFRA YA ESTAN CORREGIDAS, POR REGENERACION**, con
  su correccion declarada en `P.9.3`. **No las rehagas.** Lo que queda de la cola del
  auditor son **siete correcciones**, y van en la TAREA 1.
- **EL TALLADOR YA CORRE**: `scripts/tallar_reporte.py` en cada commit por el hook, y
  `scripts/cerrar_reporte.py` en el cierre de tu vuelta. **Guarda la salida de cada
  instrumento en un fichero y pega la tabla de ahi.**
- **ESTA VUELTA VA A POR `cap_12`, `cap_13` Y `cap_14`: EL LOTE 4 SE CIERRA.**
- **Y AL CERRARLO, `D.39` INSERTA.** Con eso se desbloquean **las 37 aristas** y **los
  12 veredictos sin sede** que llevan vueltas esperando **el mismo acto**.

---

## TAREA 1: LA COLA DE SIETE, **ANTES DE MINAR NADA**

*El auditor dejo nueve correcciones escritas en su `PARA_ALEXIS` seccion 5. **Las dos
primeras eran cifra falsa y ya estan hechas por regeneracion** (`P.9.3`). Estas siete
son las que quedan, con su numero original para que las puedas cotejar.*

| # | que hay que hacer | de donde sale |
|---:|---|---|
| **3** | **la pieza 14 gana su paso 12** con la primera mitad de `L91` de `cap_10` (*lo que se juega: construir confianza y averiguar para que papel encaja cada persona*); el resto de `cap_10` baja de `1.686` a `1.585` palabras. **La frontera sigue en 14 piezas** | `ACTA 22` `3.7` |
| **4** | **quitar `las siete velas` del paso 2 de `debatir_decidir_asuntos_cultura_evitar_delegar`** (el libro escribe solo `A menorah?`) y corregir su `resumen`, que declara `0 PUENTE` | `4.1` |
| **5** | **`leer_seniales_fallo_jefe_reunion_solas` recupera los dos encargos perdidos** (`L123` *ask explicitly for the bad news, don't let the issue drop*; `L127` *be direct but polite* con su frase literal), arregla el tercer motivo de `L127`, y su `resumen` deja de afirmar que el libro solo encarga en dos senales | `4.2` |
| **6** | **declarar las dos aristas `D.29` que `L57` debe** (madre `montar_reuniones_solas_mentalidad_frecuencia`, `--paso 15`, hijos `desplegar_tres_conversaciones_carrera` y `entregar_evaluacion_formal_desempenio_nueve_consejos`), y **quitar del `resumen` de `preguntar_seguimiento` la promesa de una arista que el reporte no declara** | `4.3` |
| **7** | **`montar_reuniones_solas` deja de afirmar que sus pasos llevan `cinco personas`**, o recoge el limite de `L53` | `4.4` |
| **8** | **los pasos 3, 4 y 5 de `pelear_proliferacion` llevan la evidencia del libro** (*el libro cuenta que no cuajo*) en vez del imperativo negativo que el libro no da | `3.3` |
| **9** | **el dia de la insercion, la arista de la rueda de la cultura NO se cablea con `--paso 2` de la madre**: ese paso no nombra a la hija (`D.37` literal). La clase `CONTINUA` y la arista `D.29` se sostienen por su razon escrita | `3.8` |

**NINGUNA DE LAS SIETE TOCA EL GRAFO NI LA BITACORA**, porque no hay nada insertado que
corregir: **seis son de fichero de cuarentena o del reporte, y la 9 es de encargo para
el dia de la insercion.** **Y cada candidato que toques vuelve a pasar por la aduana**,
porque una correccion lo vuelve a escribir (`EXTRACTOR.md` 16).

---

## TAREA 2: **EL TALLADOR, QUE ES LA CONDICION DE TU REINICIO**

*No es una tarea de trabajo: es como se trabaja a partir de hoy. La pongo con numero
porque tu racha se reinicio contra ella.*

> **TODA TABLA QUE PRESENTES COMO SALIDA DE UN INSTRUMENTO SE ANEXA DESDE SU FICHERO.
> NO SE TECLEA.**

**COMO:** guarda la salida (`python .t1_v23/lo_que_sea.py > .t1_v23/salida_lo_que_sea.txt`),
declara encima de la tabla *Salida de `python ...`, guardada en `...`*, y **pega la
tabla de ese fichero**. El hook compara **celda a celda** en cada commit y **aborta
nombrando la fila** si difieren.

**SI DIFIERE, NO SE TECLEA LA CELDA BUENA:**

    python scripts/tallar_reporte.py --arreglar

**y despues escribes al lado de que caida sale**, que es correccion declarada.

**SI TU TABLA RESUME UN INSTRUMENTO en vez de reproducirlo** (dos filas de quince salen
de el), **dilo**: `<!-- TALLADO: parcial salida=<ruta> -->` encima. Queda listada como
cita en cada corrida. **Lo que no vale es callarlo.**

**Y AL CERRAR LA VUELTA:** `python scripts/cerrar_reporte.py`, que corre el tallado en
estricto mas las cinco guardas. **En estricto, una tabla que declara instrumento y no
puede enseñarlo tambien tumba**, y es a proposito: el cierre es el momento en que tus
instrumentos siguen en el arbol.

---

## TAREA 3: `cap_12`, `cap_13` Y `cap_14`. **EL LOTE 4 SE CIERRA**

| unidad | rotulo textual | cuerpo |
|---|---|---:|
| `cap_12` | `Getting Started` | **2.118** |
| `cap_13` | `Afterword to the Revised Edition` | **9.298** |
| `cap_14` | `Bonus Chapter: A Radical Respect Framework` | **7.638** |

*Las tres salen de `sed -n '8,$p' <fichero> | wc -w`. **Remidelas tu y pega tu salida**:
una cifra de mi encargo no es fuente de una cifra tuya (`EXTRACTOR.md` 5).*

> ### **TRES CAPITULOS, Y EL FRENO DECIA DOS. LO DIGO ENTERO EN VEZ DE ESCONDERLO**
>
> **Tu propia medida disparo el freno de fidelidad:** `cap_04` da **16,67** contra un
> tope de **10**, y por esa regla el tramo baja a **DOS** capitulos. **Mi `PARA_ALEXIS`
> decia `cap_12` y `cap_13`.**
>
> **LA DECISION DEL FUNDADOR DEL 13 SEP DICE `cap_12` A `cap_14`, y esa manda.** No es
> un olvido suyo ni una lectura mia: **es una autorizacion para cerrar el lote**, que
> es el acto que desbloquea las 37 aristas y los 12 veredictos de golpe.
>
> **LO QUE NO SE LEVANTA CON ELLO, y por eso sigue escrito aqui:**
>
> - **EL TECHO DE CANDIDATOS POR VUELTA SIGUE MANDANDO** (`EXTRACTOR.md` 12.4). **Yo
>   proyecto `cap_13` en unas 14 piezas**, asi que **es probable que la vuelta cierre
>   ahi**. Si lo hace, **cierras y lo declaras con su cifra**, y `cap_14` pasa a la
>   siguiente: eso no es incumplir el encargo, es la regla de precedencia funcionando.
> - **EL FRENO SIGUE PUBLICANDOSE.** Fila por capitulo mas total del lote, y la
>   escalada se decide **sobre el peor capitulo**. Si `16,67` sube, se dice.

**Y LA RELECTURA CON EL INSTRUMENTO ANCHO SIGUE DEBIENDOSE:** seis capitulos sin leer y
**97 ocurrencias sin adjudicar**. El total del lote (`2,72`, 34 de 1.248) esta
**declarado INCOMPLETO** y sigue estandolo hasta que se lean. **Declaralo igual de
incompleto mientras lo este.**

---

## TAREA 4: **EL CIERRE DEL LOTE 4, Y LO QUE SE DESBLOQUEA CON EL**

**SI Y SOLO SI `cap_12` A `cap_14` QUEDAN MINADOS Y EL LOTE CIERRA EN EXTRACCION:**

1. **EL INFORME DE LOTE LO CORRE EL ARNES, NO TU** (`D.42`). Te llega en
   `docs/loop/INFORME_DE_LOTE.txt` **sellado con su `git hash-object`**, anotado en
   `docs/loop/SELLOS_INFORME.jsonl`. **NO LO RECOMPUTES: CITALO POR SU SELLO**, y pega
   de ahi el saldo y **`CHOCAN entre si dentro del lote`**, que es la unica cifra que un
   informe de uno en uno no puede ver. Medido: **156,5 s por candidato**, horas para el
   lote entero. **Si tu prompt no trae el fichero, declara que la vuelta no trae saldo
   de lote y no lo lances tu.**
2. **`D.39` INSERTA**, un candidato por vez y en el orden que lee (`D.36`), con su
   veredicto escrito por vecino antes de insertar, los veredictos a
   `bitacora/VEREDICTOS.jsonl` y los insertados a `cuarentena/_insertados/<libro>/` en
   el mismo acto (`D.31`).
3. **LAS 37 ARISTAS SE CABLEAN** (`D.29` y `D.37`), **con la excepcion escrita de la
   correccion 9**: la de la rueda de la cultura **no** lleva `--paso 2`.
4. **LOS 12 VEREDICTOS SIN SEDE ENCUENTRAN LA SUYA.** Llevan vueltas viviendo solo en el
   reporte porque no habia bitacora donde escribirlos.

**SI EL LOTE NO CIERRA** porque el techo de candidatos cerro la vuelta antes, **nada de
esta tarea se hace y se declara**: `D.39` inserta un lote **CERRADO**, y medio lote no
es un lote.

---

## SON CUATRO TAREAS Y EL TOPE SON CINCO

**La TAREA 1 va primera y no se solapa.** Si la cola de siete y `cap_12` se comen la
vuelta, **la vuelta se cierra ahi y lo declaras con su cifra.** La TAREA 2 no se
negocia: corre sola en cada commit.

## LAS PARADAS

**Las de `AUDITOR_FORJA.md` 3 estan enteras.** Lo nuevo es que **el hook aborta el
commit si una tabla difiere de su instrumento** (`D.41`). **Eso no es una parada del
bucle**: es un commit que no pasa, y se arregla regenerando en el acto.

> ### Y UNA COSA QUE SIGUE ABIERTA Y NO TE BLOQUEA
>
> **`D.38.1` tiene dos lecturas** (que significa *tanda limpia*), y el fundador reinicio
> la racha sin escribir cual. **Queda nombrado en la parada archivada.** No cambia nada
> de lo que tienes que hacer esta vuelta.
