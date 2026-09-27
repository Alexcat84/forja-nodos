## 6. MI CLASE DE CADA PAR, POR LA VARA `6.1` Y SOLO ESA (`R7`), CON LOS PASOS DE LOS DOS DELANTE

*La senial dijo donde mirar y ahi acabo su trabajo (`D.19`). Los pasos los imprime `.v64aud/pasos.py`,
que busca cada id en el grafo y en las bandejas y dice de donde lo saca. Un par levantado desde los
dos lados va en una sola fila. **Las fichas de la tanda de la `63` las leo en su version de hoy**,
porque la `64` no las toca; **las seis de `d005`, en su version de `067c9df`** (seccion `2`).*

### 6.1. **LOS PARES DE LOS SEIS DE `d005`** (encargo `T2.b`; la lista de pares es la de `.v63aud/vecinos_d005.txt`, poblacion `462`, y el barrido de hoy de la seccion `5` dice si sigue en pie)

| par | mi clase | lo que la sostiene |
|---|---|---|
| `emparejar_indicadores_efecto_contraefecto` con `elegir_indicador_salida_trabajo_administrativo` | **CONTINUA, madre `emparejar...`, hijo `elegir_indicador...`** | L35 abre el tramo del hijo con *Nowhere can indicators, and paired indicators, be of more help than in administrative work*: el libro lleva el emparejamiento de L31 al trabajo administrativo. **El paso `5` del hijo** (*emparejalos con una pareja que insista en la calidad*) **es el paso `4` de la madre** (*empareja el indicador con un segundo que mida ese contraefecto*) **aplicado a indicadores de cantidad**, y los pasos `6` y `7` son sus dos ejemplos (L37). Lo que el hijo trae y la madre no: salida y no actividad, lo fisico y contable, la tabla de L39 a L67. **No REPITE: lo que queda fuera es procedimiento en los dos lados** |
| `construir_grafico_escalonado_pronosticos` con `construir_indicador_tendencia_patron` | **SANO, hermanos** | L91 abre el grafico con *Another sound way to anticipate the future*, y lo compara con *a simple trend chart*: **son dos ventanas distintas**. El grafico trabaja sobre pronosticos sucesivos; el indicador de tendencia, sobre la salida real contra el tiempo y un patron. Ninguno toma lo que el otro produce |
| `construir_grafico...` con `elegir_fabricar_pedido_pronostico` | **SANO** | los dos hablan de pronostico, pero el grafico lee como se mueve un pronostico y `elegir_fabricar` decide si se fabrica contra el. **El puente entre los dos lo pone `casar_flujo...` (L121), no ninguno de ellos** (seccion `7`) |
| `construir_grafico...` con `emparejar...` | **SANO** | vocabulario de indicador; procedimientos sin paso comun |
| `construir_indicador_tendencia_patron` con `archivar_indicadores_resolver_problemas` | **SANO** | el archivo guarda indicadores para cuando algo falla (L99); la tendencia mira la salida contra el tiempo (L89). Ningun paso de uno desarrolla uno del otro |
| `construir_indicador_tendencia_patron` con `emparejar...` | **SANO** | lo mismo |
| `elegir_fabricar...` con `emparejar...` | **SANO** | fabricar contra pronostico contra emparejar indicadores: nada que continuar |
| `archivar...` con `revisar_tres_preguntas_valor_carrera` (grafo) | **SANO** | un archivo de indicadores contra tres preguntas sobre tu carrera. La senial sale del vocabulario (*repasa*, *preguntate*) |
| `archivar...` con `vencer_sindrome_grupo_pares_autoconfianza` (bandeja) | **SANO** | nada en comun |
| `archivar...` con `cerrar_brecha_dos_preguntas_estrategia` (bandeja) | **SANO** | nada en comun |
| `emparejar...` con `revisar_tres_preguntas_valor_carrera` (grafo) | **SANO** | nada en comun |
| `elegir_indicador_salida_trabajo_administrativo` con `evaluar_directivo_resultados_fortaleza` (grafo, `zhuo_manager`) | **SANO, con frontera declarada** | **comparten un paso casi palabra por palabra**: el `2` del candidato y el `1` del vecino son la regla de Grove, *salida y no actividad, al vendedor por los pedidos y no por las visitas* (L35; Zhuo la toma de Grove). **Sin bascula** (`6.1`): lo que queda fuera es procedimiento en los dos lados, la tabla y la pareja de calidad en uno, las dos mitades del juicio y los dos casos que enganan en el otro. **No REPITE y no CONTINUA**: ninguno toma lo que el otro produce; los dos aplican la misma regla a objetos distintos, una unidad administrativa y un directivo |

### 6.2. **LOS PARES DE LOS NUEVE `BLOQUEARIA` DE `d140`** (encargo `T3`; la lista es la de `python .v63aud/vecinos.py`, poblacion `462`)

    $ python .v63aud/vecinos.py 2>&1 | grep -v '^ENTRARIA' | awk '/^ENTRARIA/{skip=1} /^BLOQUEARIA/{skip=0} !skip'
    BLOQUEARIA  clasificar_trabajo_proceso_montaje_prueba  poblacion 462  
        preferir_inspeccion_proceso_prueba_destructiva       similitud_texto              texto 0.372 familia 0.250 paso 0.461  paso 5 del candidato contra paso 6
    BLOQUEARIA  construir_flujo_produccion_paso_limitante  poblacion 462  
        retirar_barreras_politicas_metodo                    paso_contra_nodo             texto 0.108 familia 0.000 paso 0.614  paso 4 del candidato contra paso 1
        rehacer_flujo_paso_limitante_capacidad               similitud_texto, familia_id  texto 0.412 familia 0.429 paso 0.430  paso 9 del candidato contra paso 5
        preferir_inspeccion_proceso_prueba_destructiva       similitud_texto              texto 0.397 familia 0.000 paso 0.421  paso 8 del candidato contra paso 6
    BLOQUEARIA  detectar_arreglar_fallo_etapa_menor_valor  poblacion 462  
        supervisar_tarea_delegada_etapa_menor_valor          familia_id                   texto 0.242 familia 0.333 paso 0.459  paso 2 del candidato contra paso 1
    BLOQUEARIA  dimensionar_inventario_materia_prima_reposicion  poblacion 462  
        preferir_inspeccion_proceso_prueba_destructiva       similitud_texto              texto 0.391 familia 0.000 paso 0.403  paso 2 del candidato contra paso 2
        detectar_arreglar_fallo_etapa_menor_valor            similitud_texto              texto 0.357 familia 0.000 paso 0.401  paso 1 del candidato contra paso 2
    BLOQUEARIA  preferir_inspeccion_proceso_prueba_destructiva  poblacion 462  
        clasificar_trabajo_proceso_montaje_prueba            similitud_texto              texto 0.366 familia 0.250 paso 0.461  paso 6 del candidato contra paso 5
        rehacer_flujo_paso_limitante_capacidad               similitud_texto              texto 0.445 familia 0.000 paso 0.384  paso 1 del candidato contra paso 6
        construir_flujo_produccion_paso_limitante            similitud_texto              texto 0.410 familia 0.000 paso 0.442  paso 6 del candidato contra paso 8
        dimensionar_inventario_materia_prima_reposicion      similitud_texto              texto 0.384 familia 0.000 paso 0.417  paso 5 del candidato contra paso 6
    BLOQUEARIA  rehacer_flujo_paso_limitante_capacidad  poblacion 462  
        preferir_inspeccion_proceso_prueba_destructiva       similitud_texto              texto 0.460 familia 0.000 paso 0.378  paso 3 del candidato contra paso 2
        construir_flujo_produccion_paso_limitante            similitud_texto, familia_id  texto 0.419 familia 0.429 paso 0.430  paso 5 del candidato contra paso 9
        dimensionar_inventario_materia_prima_reposicion      similitud_texto              texto 0.357 familia 0.000 paso 0.387  paso 2 del candidato contra paso 3
    BLOQUEARIA  decidir_aceptar_rechazar_material_defectuoso  poblacion 462  
        dimensionar_plantilla_administrativa_pronostico      similitud_texto              texto 0.372 familia 0.000 paso 0.364  paso 4 del candidato contra paso 2
    BLOQUEARIA  dimensionar_plantilla_administrativa_pronostico  poblacion 462  
        elegir_cinco_indicadores_diarios_fabrica             similitud_texto              texto 0.351 familia 0.000 paso 0.434  paso 6 del candidato contra paso 3
        simplificar_trabajo_reducir_numero_pasos             similitud_texto              texto 0.351 familia 0.000 paso 0.388  paso 6 del candidato contra paso 6
        decidir_aceptar_rechazar_material_defectuoso         similitud_texto              texto 0.367 familia 0.000 paso 0.359  paso 2 del candidato contra paso 3
    BLOQUEARIA  simplificar_trabajo_reducir_numero_pasos  poblacion 462  
        dimensionar_plantilla_administrativa_pronostico      similitud_texto              texto 0.351 familia 0.000 paso 0.439  paso 4 del candidato contra paso 5

**Los pares distintos los cuenta un instrumento**, no mi ojo sobre el bloque: un par levantado desde
los dos lados cuenta una vez.

    $ python .v64aud/pares_d140.py
    candidatos BLOQUEARIA: 9 | pares distintos: 12
        clasificar_trabajo_proceso_montaje_prueba | preferir_inspeccion_proceso_prueba_destructiva
        construir_flujo_produccion_paso_limitante | preferir_inspeccion_proceso_prueba_destructiva
        construir_flujo_produccion_paso_limitante | rehacer_flujo_paso_limitante_capacidad
        construir_flujo_produccion_paso_limitante | retirar_barreras_politicas_metodo
        decidir_aceptar_rechazar_material_defectuoso | dimensionar_plantilla_administrativa_pronostico
        detectar_arreglar_fallo_etapa_menor_valor | dimensionar_inventario_materia_prima_reposicion
        detectar_arreglar_fallo_etapa_menor_valor | supervisar_tarea_delegada_etapa_menor_valor
        dimensionar_inventario_materia_prima_reposicion | preferir_inspeccion_proceso_prueba_destructiva
        dimensionar_inventario_materia_prima_reposicion | rehacer_flujo_paso_limitante_capacidad
        dimensionar_plantilla_administrativa_pronostico | elegir_cinco_indicadores_diarios_fabrica
        dimensionar_plantilla_administrativa_pronostico | simplificar_trabajo_reducir_numero_pasos
        preferir_inspeccion_proceso_prueba_destructiva | rehacer_flujo_paso_limitante_capacidad

**La tabla de abajo lleva una fila por cada uno de esos pares**, en otro orden.

| par | mi clase | lo que la sostiene |
|---|---|---|
| `construir_flujo_produccion_paso_limitante` con `rehacer_flujo_paso_limitante_capacidad` | **CONTINUA, madre `construir_flujo...`, hijo `rehacer_flujo...`** | la condicion del hijo es *cuando ya tienes un flujo construido*; su paso `4` rehace el flujo de la madre alrededor del paso limitante nuevo, **calculando otra vez hacia atras** (madre pasos `5`, `7` y `8`), y su paso `5` cambia solo los desfases (madre paso `9`). Lo que el hijo trae: la capacidad infinita supuesta, la cola, la espera dentro del flujo. L51 a L55 sobre L23 a L27 (`cap_02`) |
| `detectar_arreglar_fallo_etapa_menor_valor` con `supervisar_tarea_delegada_etapa_menor_valor` (bandeja) | **CONTINUA, madre `detectar...`, hijo `supervisar...`** | el paso `2` del hijo es la regla del paso `3` de la madre aplicada a la delegacion, y el hijo trae procedimiento propio (los borradores, la frecuencia por madurez, el detalle al azar). **Coincide con lo que la `ACTA 62` `62.5` sostuvo** y con los veredictos que el encargo manda reutilizar de `.v63ext/cmd_02_detectar.sh` |
| `construir_flujo...` con `retirar_barreras_politicas_metodo` (grafo, `smart_who`) | **SANO** | contratar sin barreras de politica contra construir un flujo. La senial (`paso_contra_nodo` `0.614`) sale de la muletilla *que es por donde el libro dice* contra *que es con quien el libro dice* |
| `construir_flujo...` con `preferir_inspeccion_proceso_prueba_destructiva` | **SANO** | la misma fabrica de desayunos; ningun paso de uno desarrolla uno del otro |
| `rehacer_flujo...` con `preferir_inspeccion...` | **SANO** | lo mismo |
| `clasificar_trabajo_proceso_montaje_prueba` con `preferir_inspeccion...` | **SANO** | las pruebas de `clasificar` (unitaria, del sistema, L45) no son la eleccion entre prueba funcional e inspeccion dentro del proceso de L67 |
| `dimensionar_inventario_materia_prima_reposicion` con `preferir_inspeccion...` | **SANO, hermanos** | los dos cuelgan de la maquina continua (L67 y L69, *What else could go wrong*): uno vigila el proceso, el otro la entrada y el inventario |
| `dimensionar_inventario...` con `detectar_arreglar_fallo...` | **SANO, y lo sigo marcando DISCUTIBLE** | lo comun es un ejemplo, el huevo podrido rechazado al recibirlo (paso `4` de `detectar` contra pasos `1` a `3` de `dimensionar`). Lo que `dimensionar` anade, el inventario por el tiempo de reposicion y la oportunidad en riesgo (L69), **no desarrolla la regla del menor valor**: desarrolla otra cosa. Lo que queda fuera es procedimiento en los dos lados |
| `rehacer_flujo...` con `dimensionar_inventario...` | **SANO** | vocabulario comun (parar, esperar), procedimientos distintos |
| `decidir_aceptar_rechazar_material_defectuoso` con `dimensionar_plantilla_administrativa_pronostico` | **SANO** | material que no llega a especificacion contra plantilla administrativa. La senial sale de *grupo equilibrado de mandos* contra *patrones de hecho* |
| `dimensionar_plantilla...` con `elegir_cinco_indicadores_diarios_fabrica` | **SANO** | los cinco datos del dia de la fabrica contra la plantilla por pronostico |
| `dimensionar_plantilla...` con `simplificar_trabajo_reducir_numero_pasos` | **SANO** | quitar pasos de un flujo contra ajustar la plantilla a la carga |

## 7. LOS PARES QUE LEO Y LA SENIAL NO LEVANTA (`D.29`, encargo `T4`, `d141`)

| madre | hijo | lo que lo sostiene | mi confianza |
|---|---|---|---|
| `elegir_indicador_salida_trabajo_administrativo` (`d005`) | `dimensionar_plantilla_administrativa_pronostico` | L125, *if we have carefully chosen indicators that characterize an administrative unit and watch them closely*: **el paso `1` del hijo presupone el producto de la madre**, y los pasos `3` a `7` siguen donde ella acaba | **alta: la sostengo** |
| `construir_indicador_tendencia_patron` (`d005`) | `dimensionar_plantilla...` | L125, *de facto standards, inferred from the trend data*: **el paso `2` del hijo sale de la serie y el patron que la madre mide** en sus pasos `3` y `4` | **alta: la sostengo**. **Hoy la senial si lo levanta** (seccion `5`, fila `NUEVO`); en la lista de poblacion `462` no |
| `elegir_fabricar_pedido_pronostico` (`d005`) | `casar_flujo_fabricacion_flujo_ventas` | L111, *Delivering a product that was built to forecast*: **la condicion del hijo** (*cuando fabricas contra pronostico*) **es la decision que la madre toma** en su paso `4` | **alta: la sostengo** |
| `construir_grafico_escalonado_pronosticos` (`d005`) | `casar_flujo...` | L121, *It is a good idea to use stagger charts in both the manufacturing and sales forecasts. As noted...*: el paso `12` del hijo usa el grafico de la madre en los dos pronosticos | **baja**: es un paso de doce, y lo que ese paso hace (mirar la variacion de un pronostico a otro) **es el paso `4` de la madre, no procedimiento nuevo**. Nombrar no es procedimentar. **No la sostengo como arista**; la dejo escrita para que conste que la mire |
| `dimensionar_inventario_materia_prima_reposicion` | `decidir_aceptar_rechazar_material_defectuoso` | el paso `1` del hijo (*cuando rechaces material en la inspeccion de recepcion*) abre la decision que la madre cierra con una sola salida en su paso `3` (*devuelve*); L135 anade la segunda (usar lo que no llega) y el grupo que decide | **alta: la sostengo**. No es de `d141`, pero es de la tanda y la senial tampoco lo levanta |
| `emparejar_indicadores_efecto_contraefecto` (`d005`) | `elegir_indicador_salida_trabajo_administrativo` (`d005`) | **este si lo levanta la senial** (seccion `6.1`): lo pongo aqui solo para que el orden lo tenga | **alta** |

**Y DOS QUE LEO COMO NO CONTINUA**, para que conste que las mire: `casar_flujo...` paso `11` nombra la
regla de `detectar_arreglar_fallo...` (L119, *as we've learned before*) y la aplica al inventario en una
sola linea: SANO, nombrar no es procedimentar. Y `elegir_cinco_indicadores_diarios_fabrica` con
`emparejar...`: el paso `8` de `elegir_cinco` (*no te quedes en contar cuantas unidades sirve cada
persona*) es un indicador de calidad junto a uno de cantidad (L27), **pero el libro no lo presenta como
par de efecto y contraefecto**; eso llega despues, en L31. SANO. **Hoy la senial lo levanta** (seccion `5`), y la clase no cambia.

## 8. LO QUE EL ORDEN TIENE QUE RESPETAR, LEIDO (encargo `T4`)

**No fijo el orden** (`D.36`: lo fija quien autoriza). **Lo que si leo son las madres que tienen que ir
delante**, con las aristas de `6` y `7`:

| hijo | madre que tiene que ir delante | capitulo de cada uno |
|---|---|---|
| `rehacer_flujo_paso_limitante_capacidad` | `construir_flujo_produccion_paso_limitante` | `cap_02` y `cap_02` |
| `decidir_aceptar_rechazar_material_defectuoso` | `dimensionar_inventario_materia_prima_reposicion` | `cap_03` y `cap_02` |
| `elegir_indicador_salida_trabajo_administrativo` | `emparejar_indicadores_efecto_contraefecto` | `cap_03` y `cap_03` |
| `dimensionar_plantilla_administrativa_pronostico` | `elegir_indicador_salida_trabajo_administrativo` **y** `construir_indicador_tendencia_patron` | `cap_03`, los tres |
| `casar_flujo_fabricacion_flujo_ventas` | `elegir_fabricar_pedido_pronostico` | `cap_03` y `cap_03` |

**LECTURA:** la cadena mas larga es de tres: `emparejar`, despues `elegir_indicador`, despues
`dimensionar_plantilla`. **Si la tanda de la `65` tiene tope, `dimensionar_plantilla` no puede entrar
sin sus dos madres de `d005` delante.** `supervisar_tarea_delegada...` es hijo de `detectar...` y vive en
`cap_04`: queda fuera de los `22`, pero su veredicto se escribe cuando entre el.

