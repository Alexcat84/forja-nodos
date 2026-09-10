# LOTE 1 `onu_consumidor`: SEIS CANDIDATOS INSERTADOS

**Archivados el 10 sep 2026.** Estos seis ficheros **ya no son candidatos**: sus
nodos viven en `dataset/nodos.jsonl`. Se guardan porque **el fichero de cuarentena
es el registro de COMO entro cada uno**, y ese registro vale mas cuanto mas viejo
es (`D.31`).

**NO SE BORRAN, NO SE EDITAN, Y EL INFORME NO LOS CUENTA.**

    python forja.py informe --carpeta cuarentena/_insertados/onu_consumidor
      6 ficheros ARCHIVADOS en cuarentena/_insertados: ya viven en el grafo,
      y el informe no los cuenta (D.31).

## Los seis, con su commit de insercion

**Todos entraron en `762e31d`**, el 10 sep 2026, con la autorizacion del fundador
y `MODO_INSERCION=insertar`. **El orden importaba y esta medido:** la madre
primero, porque si entra antes el hijo no hay madre en el grafo contra la que
declarar la arista.

| # | candidato | commit | veredicto |
|---|---|---|---|
| 1 | `formular_codigo_comercializacion_empresarial` | `762e31d` | sin vecinos. **MADRE** de la arista |
| 2 | `verificar_afirmaciones_ambientales_publicidad` | `762e31d` | **CONTINUA** sobre `formular_codigo...`, **declarado POR LECTURA** |
| 3 | `detectar_abusos_contractuales_consumo` | `762e31d` | sin vecinos |
| 4 | `examinar_normas_pesos_medidas` | `762e31d` | sin vecinos |
| 5 | `informar_efectos_ambientales_productos` | `762e31d` | sin vecinos |
| 6 | `vigilar_practicas_comerciales_perjudiciales` | `762e31d` | sin vecinos |

**La razon escrita del unico veredicto vive en `bitacora/VEREDICTOS.jsonl`**, con
las tres señales que NO lo levantaron: `similitud_texto` 0,224, `familia_id`
0,000, `paso_contra_nodo` 0,572 contra un umbral de 0,60.

## Que se puede hacer con estos ficheros

| se puede | no se puede |
|---|---|
| **comparar** el candidato archivado con el nodo vivo, para ver que le hizo la aduana al entrar (normalizacion, aristas cableadas) | **reinsertarlos**: la aduana los rechaza por `el id ya vive en el grafo`, y hace bien |
| **leer** como estaban escritos antes de la pasada de correccion de la vuelta 2, buscando la version anterior en git | **editarlos**: un registro que se retoca deja de ser un registro |

**El estado en que se archivan es el estado en que ENTRARON**, ya corregido: los
trece puentes de la vuelta 2 se repararon **antes** de la insercion
(`docs/CIERRE_LOTE_1.md` seccion 3.4). Para verlos como salieron de la vuelta 1,
`git log` sobre estos mismos ficheros.
