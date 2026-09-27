
## 64.4. TAREA 3, LA RELECTURA CONJUNTA (`1.3`), EN SU ORDEN

**Mi lectura se escribio y se commiteo primero**: los `40` veredictos y los discutibles `D64.3` a `D64.5`
estan en `6e42f06`, empujado **antes** de abrir la apertura sellada de la `63`. **Solo despues** la abri:

    $ git log -1 --format='%h %cI %s' 6e42f06
    6e42f06 2026-09-23T10:20:47-04:00 Vuelta 64, T1 a T3: fidelidad entera de los seis de d005 (2 PUENTE en 41, reescritos) y 40 veredictos listos, antes de abrir la apertura sellada

y lei `git show 53e573e:docs/loop/APERTURA_CIEGA.md`, secciones `5.1`, `5.2` y `6`.

**LOS PARES DE `d140` QUE LEVANTA LA SENIAL (`5.1`)**: de las ocho filas de su tabla, **siete coinciden con
mis bloques en clase y en direccion** (`construir_flujo` madre de `rehacer`; `detectar` madre de
`supervisar`; `retirar_barreras` SANO; `preferir` SANO con `construir_flujo`, `rehacer` y `clasificar`;
`preferir` y `dimensionar_inventario` hermanos; `rehacer` y `dimensionar_inventario` SANO; `dimensionar_plantilla`
SANO con `decidir_aceptar`, `elegir_cinco` y `simplificar`). **Discrepamos en UNO**:

| par | la apertura sellada | mi lectura | la linea de cada lado | decido, con la vara `6.1` |
|---|---|---|---|---|
| `dimensionar_inventario_materia_prima_reposicion` con `detectar_arreglar_fallo_etapa_menor_valor` | **SANO**, marcado DISCUTIBLE: lo que anade `dimensionar` (el tamano del inventario, la oportunidad en riesgo) *no desarrolla la regla del menor valor* | **CONTINUA, madre `detectar`** (`D64.4`, marcado antes de abrir) | `detectar` paso `4`, de L75: `75:we should find and reject the rotten egg as it’s being delivered from our supplier`; `dimensionar` pasos `1` a `3`, de L69: `69:look at the eggs at the time of receipt, something called incoming or receiving inspection` | **MANTENGO CONTINUA.** La vara no tiene bascula: que `dimensionar` anada ademas el inventario no le quita que sus pasos `1` a `3` desplieguen, con procedimiento propio (que mirar, que devolver, que te deja), la linea que la madre pone en su paso `4`. Anadir procedimiento es lo que un hijo hace. **Queda como discrepancia declarada para el auditor**, con `D64.4` marcado antes |

Las dos citas de la tabla, pegadas y cortadas en el propio comando (`D.35`):

    $ grep -n -o "we should find and reject the rotten egg as it.s being delivered from our supplier" fuentes/grove_high_output/cap_02.md
    75:we should find and reject the rotten egg as it’s being delivered from our supplier
    $ grep -n -o "look at the eggs at the time of receipt, something called incoming or receiving inspection" fuentes/grove_high_output/cap_02.md
    69:look at the eggs at the time of receipt, something called incoming or receiving inspection

**LOS PARES QUE LA SENIAL NO LEVANTA (`5.2`) Y LOS QUE YO NO HABIA ESCRITO.** Son de `T4` y se deciden alli,
en `ARISTAS POR LECTURA (D.29)`. **Digo aqui cuales tenia escritos antes de abrir y cuales no**, porque una
coincidencia solo vale como ciega si mi lado estaba escrito:

| par de `5.2` | mi lado, antes de abrir | despues de abrir, con la vara |
|---|---|---|
| `elegir_indicador_salida...` madre de `dimensionar_plantilla...` | **escrito**: en `6e42f06`, la linea de `dimensionar_plantilla` contra `elegir_cinco` dice que el paso `1` pide *lo que despliega `elegir_indicador_salida_trabajo_administrativo`* | **coincide** |
| `construir_indicador_tendencia...` madre de `dimensionar_plantilla...` | **escrito**: `CONTINUA` en los dos bloques, porque hoy la senial lo levanta | **coincide** |
| `representar_actividad_caja_negra...` madre de `construir_indicador_linealidad...` | **no escrito** | **coincide**, pero **no cuenta como ciega** |
| `dimensionar_inventario...` madre de `decidir_aceptar...` | **no escrito** | **lo sostengo** (`64.5`) |
| `rehacer_flujo...` madre de `equilibrar_capacidad...` | **no escrito** | **lo sostengo** (`64.5`) |
| `elegir_fabricar...` madre de `casar_flujo...` | **no escrito** | **lo sostengo** |
| `construir_grafico_escalonado...` madre de `casar_flujo...` (*confianza baja*) | **no escrito** | **lo sostengo sin rebajarlo** (`64.5`) |
| `casar_flujo...` paso `11` con `detectar_arreglar...`: SANO | **no escrito** | **coincide en SANO, por otro motivo** (`64.5`) |
| `variar_frecuencia...` con `elegir_inspeccion...`: hermanos | **no escrito** | **coincide** |

**Y LAS SERIES (`6`)**: la apertura dice *ninguna en la tanda*, y **coincido**, con las mismas tres cuentas
(*las tres operaciones*, *los cinco datos*, *las dos tecnicas*) viviendo dentro de su propio nodo y L131 sin
nodo cabeza.
