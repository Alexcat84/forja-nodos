
# VUELTA 67 DE LA LINEA SERIAL, lote 7 (`grove_high_output`), **CLASE INSERCION**: la relectura conjunta de dos pares y una arista de `cap_04`, y despues las `20` primeras filas de su orden, una por vez

*Encargo escrito por el auditor al cerrar la `ACTA 65`. Clase impresa por `python scripts/deuda.py --clase 67`
(`LIBRE`, van `3` de `5` desde la `64`). **Un `insertar` por vez, y ninguno vivo cuando el turno termine.***

**REPORTE ABIERTO AL EMPEZAR** (`EXTRACTOR.md` 3). Las filas se llenan al cerrarse cada tarea; cada insercion
anexa su fila al volver, con su commit. Si la vuelta se corta, lo que falte es exactamente lo que no tiene fila.

| tarea | que | estado |
|---|---|---|
| `T1` | los registros de la `ACTA 65` | **CERRADA** (`67.1`) |
| `T2` | la relectura conjunta de `C1`, `C2` y `C3`, antes del primer `insertar` | **CERRADA** (`67.2`) |
| `T3` | lo que entra es lo que se leyo: las `20` fichas contra `d8f4e2a` | **CERRADA** (`67.3`) |
| `T4` | las filas `1` a `20` del orden de `cap_04`, una por vez | abierta: cada fila se anexa al volver su `insertar` (`67.4`) |
| `T5` | el cierre: censo, aristas, `PASOS INVENTADOS`, `D.61`, `R5`, guardas, commit | abierta (`67.5`) |

## 67.0. LA APERTURA, MEDIDA ANTES DE LA PRIMERA OPERACION (`EXTRACTOR.md` 4)

**Lo pendiente, commiteado primero** (`EXTRACTOR.md` 1): `TABLERO.jsonl`, `loop.log`, `ultimo_auditor.json` y
`ultimo_extractor.json` del arnes, en `5e3664f`, gate verde, empujado.

<!-- TALLADO: parcial salida=.v67ext/apertura.txt -->

@@PEGA .v67ext/apertura.txt@@

**Coincide con el cierre de la `66`** (`368`, `796`, `1`, `69`, `23`: `ACTA 65` `65.1`), y **`procesos/` esta vacio:
ningun cerrojo que romper.** `.v67ext/censo.sh` es copia de `.v66ext/censo.sh` con el comentario cambiado, y se
vuelve a correr al cerrar. **`deuda.py` dice ya `58`**: la `d168` anotada por la `ACTA 65`, como su `65.10` anunciaba.

## 67.D. **LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO** (`EXTRACTOR.md` 8)

| | que | por que lo marco |
|---|---|---|
| `D67.1` | **`C2`, `elegir_momento` hijo de `buscar_actividad`: la paso a `CONTINUA`** y cambio mi linea (`67.2`) | el auditor la llama *la mas delgada*; el hijo usa el producto de la madre por su condicion escrita y por L215, pero sus pasos `2` y `3` son el ejemplo de la primera via y no una via entera |
| `D67.2` | **`C3`, la arista `buscar_actividad` a `detectar_palanca`: NO SOSTENGO**, contra el `SOSTENGO, DUDA` del auditor (`67.2`) | es una discrepancia viva: decido que el repaso de la condicion del hijo es el mandato de L193 y no el producto de la madre. Si el auditor lee lo contrario, la arista se cablea despues con `forja.py arista` sin mover dato |
| `D67.3` | **la fila `NO SOSTENGO` de `subir_productividad` a los cinco de L259 a L291 queda `NO SOSTENGO` con la razon reescrita** por `6.1` (`67.2`) | su razon vieja usaba la misma vara `9.1` restriccion `1` que cae en `C1`, y el encargo no la lista; la reescribo porque si no mi fichero diria dos cosas, y la clase la sostengo porque ninguna de las cinco condiciones es el producto del paso `2` de `subir` |
| `D67.4` | **`subir_productividad` con `elegir_momento` sigue `SANO`, con la razon reescrita en sus dos lineas** (`67.2`) | la razon vieja usaba `9.1` restriccion `1`; con `C1` y `C2` son abuelo y nieto por `buscar`, y no cableo la arista directa |
| `D67.5` | **`.v67ext/insertar.py` salta las lineas `#` del bloque de cada candidato** | la correccion declarada de la `TAREA 2` deja la linea vieja encima como comentario dentro del bloque, y la copia de la `66` la habria pasado como `--veredicto`. `comprobar_veredictos.py` y `orden.py` ya las saltaban |

## 67.1. TAREA 1: LOS REGISTROS DE LA `ACTA 65`, SIN REABRIR EL ARGUMENTO (`D.47`)

| que | donde |
|---|---|
| mis ocho discutibles de fidelidad y de metodo `D66.1` a `D66.7` se sostienen: `cap_04` queda en `0` de `156`, firmado. `D66.8`, `D66.10` y `D66.11` coinciden con la ciega del auditor y se sostienen | `ACTA 65` `65.4.a` y `65.4.b` |
| `decir_no` con `usar_calendario`: SANO, gana mi lectura, y el orden queda como esta | `65.4.b` |
| dos pares y una arista van a relectura conjunta: es mi `T2` | `65.4.b` |
| una caida de `REPORTE` que no acumula: en `66.2` la frase de la fila `22` es la linea `7` de su salida y no la `6` | `65.2` |
| `R5` cumplido, las cinco rachas de la serial en cero, y el cierre estricto vuelve a verde: **en la `67` un rojo del cierre estricto es mio** | `65.1`, `65.2`, `65.7` |

**`T1` CERRADA.**

## 67.2. TAREA 2: LA RELECTURA CONJUNTA (`AUDITOR_FORJA.md` `1.3`), ANTES DEL PRIMER `insertar`

**Los pasos de los cuatro, impresos primero** (salida entera en `.v67ext/pasos_conjunta.txt`), y el caso del auditor
leido en la `ACTA 65` `65.4.b`:

@@CORRE python .v64aud/pasos.py subir_productividad_gerencial_tres_vias buscar_actividad_alta_palanca_tres_vias elegir_momento_actividad_palanca_maxima detectar_palanca_negativa_actividad_mando | grep -E '^=====|cond:|P[0-9]\. ' | cut -c1-200@@

**Las lineas del libro que deciden, pegadas** (`D.35`):

@@CORRE awk 'NR==193||NR==195||NR==199||NR==201||NR==203||NR==207||NR==219 {print NR": "substr($0,1,170)}' fuentes/grove_high_output/cap_04.md | sed 's/\xe2\x80\x94/ /g'@@

| | par | decido, por `6.1` y solo esa | la razon, en una linea |
|---|---|---|---|
| `C1` | `subir_productividad` con `buscar_actividad` | **`CONTINUA`, madre `subir`. GANA LA LINEA DEL AUDITOR** | **la tension se resuelve del lado de los medios:** ritmo, palanca y mezcla son objetos de trabajo que L197 a L201 nombran uno a uno, asi que `subir` pasa `9.1` y entra en esta tanda. La condicion escrita de `buscar` es el producto de los pasos `3` y `4` de `subir`, y L203 abre su tramo. **Mi razon vieja usaba `9.1` restriccion `1` para decidir una arista, que es lo que la restriccion `3` prohibe** |
| `C2` | `buscar_actividad` con `elegir_momento` | **`CONTINUA`, madre `buscar`. GANA LA LINEA DEL AUDITOR** (`D67.1`) | la condicion escrita de `elegir` es *Cuando la actividad que tienes delante es de las de alta palanca*, el producto de `buscar`; L215 dice del ejemplo de la primera via *leverage that depends, however, on when it is performed*. Mi razon vieja contestaba si `elegir` despliega una via, que no es la pregunta |
| `C3` | arista `buscar_actividad` a `detectar_palanca` | **NO SOSTENGO. SANO** (`D67.2`) | el repaso de la condicion de `detectar` no es el producto de `buscar`: es el mandato de L193, que el paso `1` de `buscar` transcribe (`D66.3`, sostenido `T` por L193) y del que cuelgan los dos. El producto de `buscar` son las actividades reconocidas por sus tres vias, y ningun paso de `detectar` las usa ni nombra una via: el hijo busca en el mismo repaso las de signo contrario (L219) |

**Y DOS LINEAS QUE CAEN CON EL MISMO ARGUMENTO, AUNQUE EL ENCARGO NO LAS LISTE**: `subir` con `elegir` (`D67.4`) y la
fila `NO SOSTENGO` de `subir` a los cinco de L259 a L291 (`D67.3`) decian lo mismo que la razon vieja de `C1`. **Las dos
clases se sostienen por `6.1` y sus razones se reescriben**; ninguna cablea nada.

**Escrito por correccion declarada, sin borrar** (`.v67ext/corregir_t2.py`; las copias de antes en
`.v67ext/veredictos_listos_antes.txt` y `.v67ext/aristas_lectura_antes.txt`): cada linea vieja queda encima de la nueva
como comentario `# vuelta 67, <motivo>:`.

@@CORRE grep -c '^# vuelta 67' .v66ext/veredictos_listos.txt .v66ext/aristas_lectura.txt@@

@@CORRE git diff --stat .v66ext/@@

**Las dos comprobaciones, otra vez** (copias sin cambios en `.v67ext/`, salidas enteras en `.v67ext/comprobar_veredictos.txt`
y `.v67ext/orden.txt`):

@@CORRE python .v67ext/comprobar_veredictos.py | grep -E 'CONTINUA|^secciones|^ARISTAS|levantada hoy'@@

<!-- TALLADO: parcial salida=.v67ext/orden.txt -->

@@CORRE python .v67ext/orden.py@@

**Cero vecinos sin linea, cero lineas sin vecino, las tres comprobaciones del orden en cero.** **El orden no cambia**:
lo unico que se mueve es la columna de madres de las filas `7` y `8`, que ganan `subir` y `buscar`.

@@CORRE diff <(cut -c1-120 .v66ext/orden.txt) <(cut -c1-120 .v67ext/orden.txt)@@

**`T2` CERRADA.** Aristas de la tanda tras la conjunta: las siete por lectura del encargo, `C3` no; y las
`CONTINUA` con `madre=` que cablea la aduana pasan de dos (`reunir` a `escalonar`, `detectar_arreglar` a
`supervisar_tarea`) a cuatro, con `subir` a `buscar` en la fila `7` y `buscar` a `elegir` en la fila `8`.

## 67.3. TAREA 3: LO QUE ENTRA ES LO QUE SE LEYO

Copia de `.v66ext/pasos_y_huellas.py` con la lista cambiada a las filas `1` a `20` de `.v66ext/orden.txt` y el commit a
`d8f4e2a` (salida en `.v67ext/pasos_y_huellas.txt`):

@@CORRE python .v67ext/pasos_y_huellas.py@@

**`20` iguales y `0` distintas: ninguna ficha se relee.** **`T3` CERRADA.**

## 67.4. TAREA 4: LAS FILAS `1` A `20`, UNA POR VEZ

**Cada fila se anexa al volver su `insertar`**, con la salida entera en `.v67ext/insertar_<fila>_<id>.txt`. **Las
aristas por lectura que tocan**, con `python .v67ext/arista.py` y su salida en `.v67ext/arista_<madre>__<hijo>.txt`.
