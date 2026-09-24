
**`T4` CERRADA: las `20` filas dentro, una por vez**, cada una con su `.fin` en `0`, ninguna arrancada antes de que
volviera la anterior, y en todas los vecinos de hoy fueron exactamente los de su bloque: **cero vecinos sin linea, cero
lineas sin vecino, cero `CAERIA`, cero lecturas mias nuevas en esta vuelta.** `agrupar_interrupciones` y `canalizar` siguen
en la bandeja para la `68`, con sus dos aristas.

**Correccion declarada de la nota de la fila `11`**: dice que el `--paso 2` de `variar` es *el primero del tramo `2 a 4` que
su fila cita en la madre*. La columna de su fila dice `madre paso 2` a secas; el tramo `2 a 4` es de su razon. El paso
cableado es el que la fila cita, y no cambia nada.

## 67.5. TAREA 5: EL CIERRE

### 67.5.a. El censo antes y despues

<!-- TALLADO: parcial salida=.v67ext/censo_cierre.txt -->

@@CORRE bash .v67ext/censo.sh@@

| | al abrir (`67.0`) | al cerrar | delta |
|---|---:|---:|---:|
| nodos | `368` | `388` | `+20` |
| veredictos | `796` | `893` | `+97`: `90` lineas `--veredicto` de las `20` filas y `7` aristas por lectura |
| pares mutuos | `1` | `1` | `0` |
| bandeja de Grove | `69` | `49` | `-20` |
| insertados de Grove | `23` | `43` | `+20` |

**`388`, `49` y `43`, los del encargo.** **`procesos/` vacio al abrir y al cerrar.** Las `90` lineas son la suma de la
columna `lin` de las filas `1` a `20` de `.v67ext/orden.txt` (`67.2`).

El `$ bash .v67ext/censo.sh` de `67.0` es el estado de apertura y hoy imprime el de cierre; **se reproduce contra el
commit de apertura**, `5e3664f`:

@@CORRE for f in dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl; do echo "$f $(git show 5e3664f:$f | wc -l)"; done; for d in cuarentena/grove_high_output/ cuarentena/_insertados/grove_high_output/; do echo "$d $(git ls-tree --name-only 5e3664f $d | grep -c '\.json$')"; done@@

### 67.5.b. Las aristas de la tanda, contadas por instrumento

`.v67ext/aristas_vuelta.py`, copia de `.v65ext/aristas_vuelta.py` que lee la bitacora desde la linea `797` y cruza con
las esperadas de los dos ficheros de la `66` tras la `T2`:

@@CORRE python .v67ext/aristas_vuelta.py@@

**`11` esperadas, `11` en el grafo, `0` en cola, `0` sin registro y `0` registradas sin esperar.** Son las cuatro `CONTINUA`
con `madre=` que cablea la aduana (`reunir` a `escalonar`, `C1`, `C2` y la EN COLA de la `65`) y las siete por lectura del
encargo; `C3` no, porque es `NO SOSTENGO` (`D67.2`). **Ninguna sin adjudicar**: las cuatro `CONTINUA` y las siete
`SOSTENGO` estan adjudicadas en la `ACTA 65` `65.4.b` o decididas en la conjunta de `67.2`, y `d072` esta pagada (fila `13`).

### 67.5.c. `PASOS INVENTADOS POR CAPITULO`, de lo que ENTRO

**Contado desde `.v66ext/fidelidad.tsv`**, la lectura entera que la `ACTA 65` `65.5` firmo en `0` de `156`, con la copia
`.v67ext/pasos_inventados.py` cuya tanda son las filas `1` a `20`:

<!-- TALLADO: parcial salida=.v67ext/pasos_inventados.txt -->

@@CORRE python .v67ext/pasos_inventados.py@@

**`0` de `143`. Bajo el `10`.** Los `13` pasos que faltan hasta `156` son los de `agrupar_interrupciones` (`7`) y
`canalizar` (`6`), que no entraron.

### 67.5.d. `D.61`: los discutibles, cada uno ejecutado o cerrado

| | que | estado |
|---|---|---|
| `D67.1` | `C2`, `buscar` madre de `elegir` | **EJECUTADO**: sus dos lineas corregidas (`67.2`) y la arista cableada por la aduana en la fila `8` |
| `D67.2` | `C3`, `NO SOSTENGO` de `buscar` a `detectar` | **EJECUTADO**: su fila `NO SOSTENGO` en `.v66ext/aristas_lectura.txt`, y `detectar` entro sin arista en la fila `9`. Si la `ACTA` lo tumba, la arista se cablea con `forja.py arista` sin mover dato |
| `D67.3` | la razon reescrita del `NO SOSTENGO` de `subir` a los cinco | **EJECUTADO**: la fila vieja comentada encima, la nueva debajo; ninguna arista cableada |
| `D67.4` | `subir` con `elegir`, `SANO` con razon reescrita | **EJECUTADO** en sus dos lineas, pasadas en las filas `6` y `8` |
| `D67.5` | la copia de `insertar.py` que salta las lineas `#` | **EJECUTADO**: la cabecera de cada `.v67ext/insertar_*.txt` lista las lineas pasadas, y en las `20` coinciden con `vec` y `lin` de su fila del orden |

**Ninguno abierto.**

### 67.5.e. Las guardas

@@CORRE python forja.py gate@@

@@CORRE python forja.py guiones@@

@@CORRE tail -2 .v67ext/cierre_tests.txt@@

(`.v67ext/cierre_tests.txt` es la salida entera de `python tests/test_aceptacion.py`, corrida al cerrar con codigo `0`.)

### 67.5.f. El reloj

@@CORRE python .v67ext/relojes.py | tail -1@@

**No son techos: es lo que costo.** La fila `17` tardo `3988,1` s, el doble que la mediana, sin vecinos que leer; **no he
medido por que**, y no lo adivino. **Ningun proceso mio vive al cerrar el turno**: los `20` `.fin` en `0` (`.v67ext/relojes.txt`)
y `procesos/` vacio (`67.5.a`).
