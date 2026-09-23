**EL METODO VIGENTE de `D.38.4`** (su correccion del 16 sep): se barre **uno por vez**, entregando a
la aduana el candidato y dejando que ella ponga las bandejas. Lance los `16` en paralelo con
`.v63aud/barrer.sh`, **los recogi todos dentro del turno**, y ninguno quedo en cero bytes. El registro
del lanzador, con el codigo de salida y los segundos de cada uno:

{{$ cat .v63aud/barrido.log}}

**LA POBLACION**, leida de los `16` informes y no de memoria:

{{$ grep -h "poblacion del barrido" .v63aud/informe_*.txt | sort | uniq -c}}

**LO QUE LEVANTO CADA UNO**, resumido por `.v63aud/vecinos.py` desde los informes de la carpeta
`.v63aud/`, uno por candidato:

{{$ python .v63aud/vecinos.py}}

### 5.1. **MI CLASE DE CADA PAR LEVANTADO, POR LA VARA `6.1` Y LEYENDO LOS PASOS**

*La senial dijo donde mirar y ahi acabo su trabajo (`D.19`). Cada par lo he leido con los pasos de los
dos delante. Un par que la aduana levanta desde los dos lados va en una sola fila.*

| par | mi clase | lo que la sostiene |
|---|---|---|
| `construir_flujo_produccion_paso_limitante` con `rehacer_flujo_paso_limitante_capacidad` | **CONTINUA, madre `construir_flujo...`, hijo `rehacer_flujo...`** | el hijo rehace el flujo de la madre cuando la capacidad es finita: su paso `4` vuelve a calcular hacia atras desde la entrega (madre pasos `7` a `9`), y su paso `5` mantiene los ciclos y cambia solo los desfases (madre paso `9`). Lo que anade (la cola, la espera dentro del flujo) es procedimiento que la madre no trae. L51 a L53 sobre L23 a L27 |
| `detectar_arreglar_fallo_etapa_menor_valor` con `supervisar_tarea_delegada_etapa_menor_valor` (bandeja, `cap_04`) | **CONTINUA, madre `detectar_arreglar...`, hijo `supervisar_tarea...`** | el paso `2` del hijo es la regla de la madre (paso `3`) aplicada a la delegacion, y el hijo trae procedimiento propio que la madre no tiene: los borradores en sucio, la frecuencia variable por madurez en la tarea, el detalle al azar. **El hijo espera en la bandeja**: la arista se declara cuando entre el |
| `construir_flujo_produccion_paso_limitante` con `retirar_barreras_politicas_metodo` (grafo, `smart_who`) | **SANO** | nada en comun: contratar sin barreras de politica contra construir un flujo. La senial sale de la muletilla del paso `4` del candidato (*que es por donde el libro dice que se empieza*) contra la del vecino (*que es con quien el libro dice*) |
| `preferir_inspeccion_proceso_prueba_destructiva` con `construir_flujo...`, con `rehacer_flujo...` y con `clasificar_trabajo_proceso_montaje_prueba` | **SANO** los tres | la misma fabrica de desayunos y el mismo vocabulario (el huevo, el tostador, rehacer); procedimientos distintos a los dos lados, y ninguno desarrolla un paso del otro |
| `preferir_inspeccion_proceso_prueba_destructiva` con `dimensionar_inventario_materia_prima_reposicion` | **SANO**, hermanos | los dos cuelgan de la maquina continua de L63 (L67 y L69, *what else could go wrong*): uno elige como vigilar el proceso, el otro inspecciona la entrada y dimensiona el inventario. Ninguno continua al otro |
| `dimensionar_inventario_materia_prima_reposicion` con `detectar_arreglar_fallo_etapa_menor_valor` | **SANO, y lo marco DISCUTIBLE** | lo comun es un ejemplo, el huevo podrido rechazado al recibirlo (paso `4` de `detectar...` contra pasos `1` a `3` de `dimensionar...`). Lo que queda fuera es procedimiento en los dos lados, asi que no REPITE. **La duda es si `dimensionar...` CONTINUA a `detectar...` desarrollando su paso `4`**; lo leo SANO porque lo que anade `dimensionar...` (el tamano del inventario por el tiempo de reposicion y la oportunidad en riesgo) no desarrolla la regla del menor valor, desarrolla otra cosa |
| `rehacer_flujo_paso_limitante_capacidad` con `dimensionar_inventario...` | **SANO** | vocabulario comun (parar, esperar), procedimientos distintos |
| `dimensionar_plantilla_administrativa_pronostico` con `decidir_aceptar_rechazar_material_defectuoso`, con `elegir_cinco_indicadores_diarios_fabrica` y con `simplificar_trabajo_reducir_numero_pasos` | **SANO** los tres | la plantilla administrativa contra material defectuoso, contra los cinco datos del dia y contra quitar pasos de un flujo: ningun paso de uno desarrolla un paso del otro |

### 5.2. **LOS PARES QUE LEO Y LA SENIAL NO LEVANTA**

**La aduana deja entrar sin vecino a candidatos que yo leo como hijos.** No es un fallo de la aduana
(`D.19`: ninguna senial separa jerarquia de ruido). **Es exactamente el caso de `D.29`**: el par se
declara por lectura, con su razon, o no se declara nunca.

| madre | hijo | lo que lo sostiene | la aduana |
|---|---|---|---|
| `representar_actividad_caja_negra_ventanas` | `construir_indicador_linealidad_alerta_temprana` | el paso `2` del hijo (*recorta en tu caja esta ventana concreta*) desarrolla el paso `8` de la madre (*recorta ventanas en la caja*); L83: *a window cut into the black box* | el hijo sale `ENTRARIA` |
| `dimensionar_inventario_materia_prima_reposicion` | `decidir_aceptar_rechazar_material_defectuoso` | el paso `1` del hijo (*cuando rechaces material en la inspeccion de recepcion*) abre la decision que la madre cierra en su paso `3` con una sola salida (*devuelve*); L135 anade la segunda (usar lo que no llega) y el grupo que decide | no levanta el par |
| `rehacer_flujo_paso_limitante_capacidad` | `equilibrar_capacidad_personal_inventario_plazo` | L57 (*let us complicate things a little further*, en el libro con contraccion) es la misma cola del tostador de L51, ahora chocando con el huevo; el hijo trae las salidas que la madre no tiene (especializar, pedir ayuda, otro tostador, inventario). **Confianza media**: tambien se puede leer como hermano | el hijo sale `ENTRARIA` |
| `elegir_indicador_salida_trabajo_administrativo` (**`d005`**) | `dimensionar_plantilla_administrativa_pronostico` | L125: *if we have carefully chosen indicators that characterize an administrative unit*; el paso `1` del hijo nombra el trabajo de la madre y los pasos `3` a `7` siguen donde ella acaba | no levanta el par |
| `construir_indicador_tendencia_patron` (**`d005`**) | `dimensionar_plantilla_administrativa_pronostico` | L125: *de facto standards, inferred from the trend data*; el paso `2` del hijo sale del patron que la madre mide en su paso `4` | no levanta el par |
| `elegir_fabricar_pedido_pronostico` (**`d005`**) | `casar_flujo_fabricacion_flujo_ventas` | L111: *delivering a product that was built to forecast*; el hijo empieza donde la madre decide fabricar contra pronostico | el hijo sale `ENTRARIA` |
| `construir_grafico_escalonado_pronosticos` (**`d005`**) | `casar_flujo_fabricacion_flujo_ventas` | L121 (*as noted*) remite al grafico de L91 a L97; el paso `12` del hijo lo usa en los dos pronosticos. **Confianza baja**: es un paso de doce, y nombrar no es procedimentar | el hijo sale `ENTRARIA` |

**Y DOS QUE LEO COMO NO CONTINUA**, para que conste que las mire: `casar_flujo...` paso `11` nombra la
regla de `detectar_arreglar_fallo...` (L119, *as we have learned before*, en el libro con
contraccion) y la aplica al inventario en una sola linea, y **nombrar no es procedimentar**: SANO. Y
`variar_frecuencia_inspeccion_nivel_calidad` con `elegir_inspeccion_barrera_monitorizacion` son
**hermanos** (L143: *another way to lower the cost*): SANO.
