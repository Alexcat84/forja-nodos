
## 5. **LAS ARISTAS QUE TOCAN LA TANDA, CONTRA LAS QUE MI LECTURA ADJUDICADA ESPERA** (`D.29`, `D.53`)

**Lo que espero** sale de dos sedes ya adjudicadas en la `ACTA 63` (`63.3`): las `8` filas `SOSTENGO` de
`.v64ext/aristas_lectura.txt` y los `CONTINUA` con madre de `.v64ext/veredictos_listos.txt` cuyos dos
extremos estan entre las `20`. **Lo que hay** lo lee el instrumento del dataset, por los dos extremos.

    $ python .v65aud/aristas.py
    FUERA DE LA TANDA (no se espera en el grafo): detectar_arreglar_fallo_etapa_menor_valor > supervisar_tarea_delegada_etapa_menor_valor
    ESTA        construir_flujo_produccion_paso_limitante        > rehacer_flujo_paso_limitante_capacidad           veredicto CONTINUA | en los dos extremos
    ESTA        construir_grafico_escalonado_pronosticos         > casar_flujo_fabricacion_flujo_ventas             lectura SOSTENGO | en los dos extremos
    ESTA        construir_indicador_tendencia_patron             > dimensionar_plantilla_administrativa_pronostico  lectura SOSTENGO | en los dos extremos
    ESTA        detectar_arreglar_fallo_etapa_menor_valor        > dimensionar_inventario_materia_prima_reposicion  veredicto CONTINUA | en los dos extremos
    ESTA        dimensionar_inventario_materia_prima_reposicion  > decidir_aceptar_rechazar_material_defectuoso     lectura SOSTENGO | en los dos extremos
    ESTA        elegir_fabricar_pedido_pronostico                > casar_flujo_fabricacion_flujo_ventas             lectura SOSTENGO | en los dos extremos
    ESTA        elegir_indicador_salida_trabajo_administrativo   > dimensionar_plantilla_administrativa_pronostico  lectura SOSTENGO | en los dos extremos
    ESTA        emparejar_indicadores_efecto_contraefecto        > elegir_indicador_salida_trabajo_administrativo   veredicto CONTINUA | en los dos extremos
    ESTA        rehacer_flujo_paso_limitante_capacidad           > equilibrar_capacidad_personal_inventario_plazo   lectura SOSTENGO | en los dos extremos
    ESTA        representar_actividad_caja_negra_ventanas        > construir_indicador_linealidad_alerta_temprana   lectura SOSTENGO | en los dos extremos
    ESTA        representar_actividad_caja_negra_ventanas        > construir_indicador_tendencia_patron             lectura SOSTENGO | en los dos extremos
    aristas que tocan la tanda: 11 | esperadas por mi lectura: 11 | esperadas y presentes: 11 | esperadas y ausentes: 0 | presentes sin lectura mia: 0

**LECTURA:** **el grafo tiene exactamente las aristas que mi lectura adjudicada pide, ni una mas ni una
menos, todas con la direccion adjudicada y escritas en los dos extremos.** La de
`construir_indicador_tendencia_patron` a `dimensionar_plantilla_administrativa_pronostico` sale una sola
vez aunque viva en las dos sedes (`SOSTENGO` y `CONTINUA`): no se cableo dos veces. **La de `detectar` a
`supervisar_tarea_delegada_etapa_menor_valor` no esta en el grafo, y es lo correcto**: el hijo es de
`cap_04` y sigue en la bandeja (`D.29`, en cola). **Ninguna arista toca a un nodo que ya viviera en el
grafo antes de la `65`.**

## 6. **LOS PARES DE LA BITACORA, SOLO POR SUS IDS** (`1.2`: primero mi clase, despues su razon)

    $ python .v65aud/pares_bitacora.py
    lineas de la bitacora en 997054d: 740 | hoy: 795 | nuevas: 55
    fechas de las nuevas: ['2026-09-23']
    candidatos de las nuevas fuera de la tanda: []
    pares repetidos en las nuevas: 0 []
    pares listos de las filas 1 a 20: 48
      EN LA BITACORA Y NO EN LOS LISTOS  casar_flujo_fabricacion_flujo_ventas | construir_grafico_escalonado_pronosticos
      EN LA BITACORA Y NO EN LOS LISTOS  casar_flujo_fabricacion_flujo_ventas | elegir_fabricar_pedido_pronostico
      EN LA BITACORA Y NO EN LOS LISTOS  construir_indicador_linealidad_alerta_temprana | representar_actividad_caja_negra_ventanas
      EN LA BITACORA Y NO EN LOS LISTOS  construir_indicador_tendencia_patron | representar_actividad_caja_negra_ventanas
      EN LA BITACORA Y NO EN LOS LISTOS  decidir_aceptar_rechazar_material_defectuoso | dimensionar_inventario_materia_prima_reposicion
      EN LA BITACORA Y NO EN LOS LISTOS  dimensionar_plantilla_administrativa_pronostico | elegir_indicador_salida_trabajo_administrativo
      EN LA BITACORA Y NO EN LOS LISTOS  equilibrar_capacidad_personal_inventario_plazo | rehacer_flujo_paso_limitante_capacidad
    en los dos: 48 | solo bitacora: 7 | solo listos: 0

**LECTURA:** **los `48` pares de los veredictos listos de las filas `1` a `20` estan todos en la bitacora**,
y los `7` que estan de mas son, uno a uno, **las siete aristas `SOSTENGO` que no iban ya como `CONTINUA`**
(seccion `5`), escritas hijo primero: **son el registro de la arista por lectura, no un vecino nuevo de la
aduana.** Si la aduana hubiera levantado en el acto un vecino sin linea, apareceria aqui como par de la
bitacora fuera de las dos listas, **y no aparece ninguno.** Lo confirma por el otro lado mi barrido (seccion
`8`). **Que cada linea de la bitacora sea literalmente la de su bloque de listos es comprobacion de mi turno
normal**: aqui no leo ni una clase ni una razon del extractor.

## 7. **LA MUESTRA PINEADA DE LOS SANO, LEIDA CON LOS PASOS DELANTE** (`7`)

**Poblacion:** los SANO de `.v64ext/veredictos_listos.txt` de las filas `1` a `20`, que son las lineas que
el encargo mando copiar tal cual (`PROMPT_SIGUIENTE.md` `T3`), contados como par y no como linea. **La
tomo aqui y no en el turno normal a proposito**: elegirla sin ver la bitacora del extractor es lo unico que
la hace ciega a lo que escribio.

    $ python .v65aud/muestra_sano.py
    pares SANO distintos en las filas 1 a 20: 26 | muestra: 6 | semilla 65023
      archivar_indicadores_resolver_problemas | vencer_sindrome_grupo_pares_autoconfianza
      construir_indicador_tendencia_patron | emparejar_indicadores_efecto_contraefecto
      dimensionar_plantilla_administrativa_pronostico | simplificar_trabajo_reducir_numero_pasos
      decidir_aceptar_rechazar_material_defectuoso | dimensionar_plantilla_administrativa_pronostico
      construir_grafico_escalonado_pronosticos | construir_indicador_tendencia_patron
      dimensionar_inventario_materia_prima_reposicion | rehacer_flujo_paso_limitante_capacidad

**LO QUE ESTA RELECTURA NO ES, Y LO DIGO ANTES:** no es ciega a la clase de la `64`. En esta fase imprimi
`.v64ext/veredictos_listos.txt` entero para sacar los pares, y la `ACTA 63` ya habia leido los `26`. **Es
ciega a lo que el extractor de la `65` escribio**, y la leo con los pasos de los dos nodos delante
(`python .v64aud/pasos.py <a> <b>`) y el libro abierto.

    $ grep -n -o "simple trend chart" fuentes/grove_high_output/cap_03.md
    91:simple trend chart
    $ grep -n -o "archive of indicators" fuentes/grove_high_output/cap_03.md
    99:archive of indicators
    $ grep -n -o "flow chart of the production process as it exists" fuentes/grove_high_output/cap_03.md
    169:flow chart of the production process as it exists
    $ grep -n -o "balanced group of managers" fuentes/grove_high_output/cap_03.md
    135:balanced group of managers
    $ grep -n -o "peer-group syndrome if each of the members has self-confidence" fuentes/grove_high_output/cap_06.md
    49:peer-group syndrome if each of the members has self-confidence
    $ grep -n -o "incoming or receiving inspection" fuentes/grove_high_output/cap_02.md
    69:incoming or receiving inspection

| par | mi clase, por la vara `6.1` y solo esa | lo que la sostiene |
|---|---|---|
| `archivar_indicadores_resolver_problemas` con `vencer_sindrome_grupo_pares_autoconfianza` | **SANO** | Ajenos: guardar y repasar un archivo de indicadores cuando algo falla (`cap_03` L99) contra apoyar la autoconfianza de un grupo de iguales en familiaridad, experiencia y la constatacion de que nadie se muere por decidir mal (`cap_06` L49). Ningun paso de uno hace lo que hace un paso del otro |
| `construir_indicador_tendencia_patron` con `emparejar_indicadores_efecto_contraefecto` | **SANO** | Comparten la palabra indicador. El primero mide una salida contra el tiempo y contra un patron y extrapola (pasos `3` a `6`); el segundo nombra efecto y contraefecto y los vigila juntos (pasos `2` a `6`, L31). Ninguno usa el producto del otro ni despliega una linea suya |
| `dimensionar_plantilla_administrativa_pronostico` con `simplificar_trabajo_reducir_numero_pasos` | **SANO** | La meta comun, la productividad administrativa, no es un paso. Uno dimensiona la gente con patrones de tendencia y el pronostico (L125); el otro dibuja el flujo, cuenta pasos y tira los que no aguantan el por que (L169). Procedimiento propio en los dos lados y sin linea compartida |
| `decidir_aceptar_rechazar_material_defectuoso` con `dimensionar_plantilla_administrativa_pronostico` | **SANO** | Ajenos dentro de `cap_03`: devolver o usar material fuera de especificacion, con el grupo equilibrado y la regla de fiabilidad (L135 a L137), contra la plantilla de una unidad administrativa (L123 a L125) |
| `construir_grafico_escalonado_pronosticos` con `construir_indicador_tendencia_patron` | **SANO** | Dos ventanas que el libro contrasta (L91, *better than if you used a simple trend chart*). El paso `4` del escalonado nombra el grafico de tendencia **solo como termino de comparacion**, y nombrar no es procedimentar (`P.5.1`): no toma su procedimiento ni lo continua. El de tendencia no nombra el escalonado |
| `dimensionar_inventario_materia_prima_reposicion` con `rehacer_flujo_paso_limitante_capacidad` | **SANO** | Comparten el desayuno de `cap_02`. Uno inspecciona la entrada y dimensiona el inventario por el tiempo de reposicion (L69); el otro rehace el flujo alrededor de la cola de un recurso (L51). Ningun paso compartido |

    $ python .v65aud/banda_muestra.py
    caen 0 de 6 | tasa 0.000 | banda Wilson 95%: 0.000 a 0.390

**MI LECTURA DE LA MUESTRA:** `6` de `6` los leo SANO, **que es la clase que la `64` dejo escrita para los
seis**. Si la bitacora dice lo mismo, la muestra se sostiene; **el cruce con la bitacora es de mi turno
normal.**
