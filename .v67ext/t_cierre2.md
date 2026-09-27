
### 67.5.g. El cierre estricto, en verde

**Correccion declarada antes del verde:** la primera corrida (codigo `1`) marco `SIN COMPROBAR` una sola tabla, la de
decisiones de `C1` a `C3` en `67.2`: el tallador le atribuyo la frase *salida entera en `.v67ext/pasos_conjunta.txt`*,
que habla del bloque de pasos de encima. La tabla cita las condiciones que ese fichero imprime y no lo reproduce, asi
que lleva ahora encima `<!-- TALLADO: parcial salida=.v67ext/pasos_conjunta.txt -->`, anadido al cerrar, y se cuenta
como cita. **No se tecleo ninguna celda.** La segunda corrida, con la salida entera (y la de las pruebas que lanza, que va por stderr) en
`.v67ext/cierre_reporte.txt`:

@@CORRE python scripts/cerrar_reporte.py 2>/dev/null | grep -E '^(TALLADO|CENSO|TABLA DE CIERRE|CIERRE|GATE|BARRIDO)'@@

**Ningun rojo.**

**Tabla de tareas, al cerrar:**

| tarea | que | estado |
|---|---|---|
| `T1` | los registros de la `ACTA 65` | **CERRADA** (`67.1`) |
| `T2` | la relectura conjunta de `C1`, `C2` y `C3` | **CERRADA** (`67.2`): `C1` y `C2` `CONTINUA`, `C3` `NO SOSTENGO` |
| `T3` | las `20` fichas contra `d8f4e2a` | **CERRADA** (`67.3`): `20` iguales |
| `T4` | las filas `1` a `20`, una por vez | **CERRADA** (`67.4`): las `20` dentro, `11` aristas vivas |
| `T5` | el cierre | **CERRADA** (`67.5`) |

### 67.5.h. `R5`, medido con las dos copias de la cabecera cambiada a la `67`

`.v67ext/pegado67.py` es `.v64ext/pegado64.py` y `.v67ext/bloques_mudos67.py` es `.v64aud/normal/bloques_mudos.py`, las
dos con la cabecera del tramo en `# VUELTA 67 ` y el comentario de cabecera, nada mas cambiado. Corridas con todos los
bloques `$` de la vuelta ya escritos, menos este:

@@CORRE python .v67ext/pegado67.py; python .v67ext/bloques_mudos67.py@@

**Cero bloques que rompen `R1` y cero comandos sin salida.** Este bloque se cuenta a si mismo si se vuelve a correr: un
bloque y dos comandos mas.
