
## 64.5. TAREA 4: `d141`, LAS ARISTAS POR LECTURA Y EL ORDEN DE LOS `22`

### 64.5.a. LA MATRIZ DE LOS `22`, Y LO QUE `2.c` NO HABIA VISTO

**Para ordenar hace falta saber que par levanta y en que sentido**, y los informes de poblacion `462` son de
antes de mis correcciones. **Mido los `22` contra los `22` en los dos sentidos con `aduana.medir`**
(`.v64ext/matriz22.py`, las fichas de hoy, `462` pares ordenados). **Lo corri en cuatro trozos, uno en primer
plano y tres en paralelo en segundo plano, y recogi los tres dentro del turno**: sus avisos de fin llegaron
antes de seguir, y ningun proceso mio queda vivo.

<!-- TALLADO: parcial salida=.v64ext/matriz22_a.txt -->

    $ grep -h FIN .v64ext/matriz22_a.txt .v64ext/matriz22_b.txt .v64ext/matriz22_c.txt .v64ext/matriz22_d.txt
    FIN filas 0 a 6 de 22, 126 pares medidos, 486 s
    FIN filas 6 a 12 de 22, 126 pares medidos, 576 s
    FIN filas 12 a 17 de 22, 105 pares medidos, 498 s
    FIN filas 17 a 22 de 22, 105 pares medidos, 535 s
    $ cat .v64ext/matriz22_a.txt .v64ext/matriz22_b.txt .v64ext/matriz22_c.txt .v64ext/matriz22_d.txt | grep -c LEVANTA
    43

**Y AQUI ESTA LO QUE EL PAR A PAR DE `2.c` NO VEIA: nueve sentidos mas levantan hoy**, que ni los informes ni
el par a par listaban (`.v64ext/matriz_nuevos.txt`, que resta de la matriz lo que ya estaba en `pares_despues.txt`),
todos con una ficha corregida en un extremo, y **dos candidatos que salian `ENTRARIA` a poblacion `462` hoy
bloquean**: `equilibrar_capacidad...` contra `construir_indicador_tendencia...`, y `elegir_inspeccion_barrera...`
contra `emparejar...` y `construir_grafico...`. **La causa es la correccion misma**: la nota declarada que se
anade al `resumen_teorico` comparte vocabulario con sus vecinos de capitulo, y la senial `1` lee el resumen. Es
`d031` medida otra vez. **No lo arreglo encogiendo la nota**: la correccion declarada con el texto viejo dentro es
la regla, y la senial solo ordena.

**Sus veredictos, anadidos a la misma sede y comprobados con el mismo instrumento**, que ahora lee tambien la
matriz:

<!-- TALLADO: parcial salida=.v64ext/comprobar_veredictos.txt -->

    $ python .v64ext/comprobar_veredictos.py | grep -v '^  OK'
    archivar_indicadores_resolver_problemas            lineas 4 | levantados hoy 4 | FALTAN 0 | SOBRAN 0 | medidos y ya no levantan 0
    construir_grafico_escalonado_pronosticos           lineas 3 | levantados hoy 3 | FALTAN 0 | SOBRAN 0 | medidos y ya no levantan ['casar_flujo_fabricacion_flujo_ventas', 'representar_actividad_caja_negra_ventanas']
    construir_indicador_tendencia_patron               lineas 6 | levantados hoy 6 | FALTAN 0 | SOBRAN 0 | medidos y ya no levantan ['representar_actividad_caja_negra_ventanas']
    elegir_fabricar_pedido_pronostico                  lineas 2 | levantados hoy 2 | FALTAN 0 | SOBRAN 0 | medidos y ya no levantan ['casar_flujo_fabricacion_flujo_ventas', 'dimensionar_plantilla_administrativa_pronostico']
    elegir_indicador_salida_trabajo_administrativo     lineas 3 | levantados hoy 3 | FALTAN 0 | SOBRAN 0 | medidos y ya no levantan ['dimensionar_plantilla_administrativa_pronostico']
    emparejar_indicadores_efecto_contraefecto          lineas 6 | levantados hoy 6 | FALTAN 0 | SOBRAN 0 | medidos y ya no levantan ['revisar_tres_preguntas_valor_carrera']
    construir_flujo_produccion_paso_limitante          lineas 3 | levantados hoy 3 | FALTAN 0 | SOBRAN 0 | medidos y ya no levantan 0
    clasificar_trabajo_proceso_montaje_prueba          lineas 1 | levantados hoy 1 | FALTAN 0 | SOBRAN 0 | medidos y ya no levantan 0
    rehacer_flujo_paso_limitante_capacidad             lineas 3 | levantados hoy 3 | FALTAN 0 | SOBRAN 0 | medidos y ya no levantan 0
    preferir_inspeccion_proceso_prueba_destructiva     lineas 4 | levantados hoy 4 | FALTAN 0 | SOBRAN 0 | medidos y ya no levantan 0
    dimensionar_inventario_materia_prima_reposicion    lineas 2 | levantados hoy 2 | FALTAN 0 | SOBRAN 0 | medidos y ya no levantan ['rehacer_flujo_paso_limitante_capacidad']
    detectar_arreglar_fallo_etapa_menor_valor          lineas 1 | levantados hoy 1 | FALTAN 0 | SOBRAN 0 | medidos y ya no levantan ['casar_flujo_fabricacion_flujo_ventas', 'dimensionar_inventario_materia_prima_reposicion']
    decidir_aceptar_rechazar_material_defectuoso       lineas 1 | levantados hoy 1 | FALTAN 0 | SOBRAN 0 | medidos y ya no levantan 0
    dimensionar_plantilla_administrativa_pronostico    lineas 6 | levantados hoy 6 | FALTAN 0 | SOBRAN 0 | medidos y ya no levantan ['elegir_indicador_salida_trabajo_administrativo']
    simplificar_trabajo_reducir_numero_pasos           lineas 1 | levantados hoy 1 | FALTAN 0 | SOBRAN 0 | medidos y ya no levantan 0
    equilibrar_capacidad_personal_inventario_plazo     lineas 1 | levantados hoy 1 | FALTAN 0 | SOBRAN 0 | medidos y ya no levantan 0
    elegir_inspeccion_barrera_monitorizacion           lineas 2 | levantados hoy 2 | FALTAN 0 | SOBRAN 0 | medidos y ya no levantan 0
    secciones 17, lineas 49, ilegibles 0

**`17` bloques y `49` lineas, cero que falten y cero que sobren.** Los bloques de `64.3` siguen valiendo; lo que
se anade a cada uno, y los dos bloques nuevos, van aqui con el mismo titulo. **La sede completa, con las `49`,
es `.v64ext/veredictos_listos.txt`**, que es de donde la `65` copia cada `--veredicto`.

### VEREDICTOS LISTOS DE construir_indicador_tendencia_patron (lineas anadidas a `64.3`)

    equilibrar_capacidad_personal_inventario_plazo|SANO|Ajenos: el vecino intercambia equipo, personal e inventario contra el plazo de entrega (cap_02 L57 a L61); el candidato mide la salida contra el tiempo y contra un patron (cap_03 L89). La senial sale de palabras comunes como salida, coste y mes. VECINO NUEVO de la matriz de los 22, tras la correccion de esta ficha.
    elegir_indicador_salida_trabajo_administrativo|SANO|El mismo par que el indicador administrativo lee desde su lado: los comprobantes tramitados son aqui un ejemplo de salida y alli una fila de su tabla, y ninguno usa el procedimiento del otro. VECINO NUEVO de la matriz de los 22.

### VEREDICTOS LISTOS DE elegir_indicador_salida_trabajo_administrativo (lineas anadidas a `64.3`)

    construir_indicador_tendencia_patron|SANO|El paso 2 del vecino pone de ejemplo de salida los comprobantes tramitados, que es la primera fila de la tabla del paso 4 del candidato, pero el vecino no elige indicador: mide contra el tiempo y contra un patron la salida que ya tengas (L89), y el candidato elige cual medir en una unidad administrativa con sus dos varas y su pareja (L35 a L67). Ninguno usa el procedimiento del otro. VECINO NUEVO de la matriz de los 22, tras las correcciones de las dos fichas.

### VEREDICTOS LISTOS DE emparejar_indicadores_efecto_contraefecto (lineas anadidas a `64.3`)

    elegir_cinco_indicadores_diarios_fabrica|SANO|Parrafos seguidos, L29 y L31, y objetos distintos: el vecino elige los cinco datos que se miran cada manana y actua sobre ellos ese dia; el candidato empareja cada indicador con el de su contraefecto para no pasarse. El vecino no empareja nada ni el candidato elige los datos del dia. VECINO NUEVO: lo levanta la matriz de los 22 tras la correccion de esta ficha, y el informe archivado no lo traia.
    dimensionar_plantilla_administrativa_pronostico|SANO|Comparten indicadores como palabra: el candidato empareja efecto y contraefecto (L31 a L33); el vecino dimensiona la plantilla con el pronostico de su carga (L123 a L125). Ninguno despliega una linea del otro. VECINO NUEVO de la matriz de los 22, tras la correccion de esta ficha.

### VEREDICTOS LISTOS DE dimensionar_plantilla_administrativa_pronostico (lineas anadidas a `64.3`)

    emparejar_indicadores_efecto_contraefecto|SANO|El mismo par que emparejar lee desde su lado: dimensionar la plantilla con el pronostico contra emparejar efecto y contraefecto. Ningun paso compartido. VECINO NUEVO de la matriz de los 22, tras la correccion del vecino.

### VEREDICTOS LISTOS DE equilibrar_capacidad_personal_inventario_plazo (bloque nuevo)

    construir_indicador_tendencia_patron|SANO|Ajenos: el candidato intercambia equipo, personal e inventario contra el plazo de entrega y busca la forma mas rentable (cap_02 L57 a L61); el vecino mide la salida contra el tiempo y contra un patron (cap_03 L89). La senial sale de palabras comunes. ESTE CANDIDATO SALIA ENTRARIA a poblacion 462 y HOY BLOQUEA por la correccion del vecino, que es d031 otra vez: la ficha que se toca mueve la senial de sus vecinos.

### VEREDICTOS LISTOS DE elegir_inspeccion_barrera_monitorizacion (bloque nuevo)

    emparejar_indicadores_efecto_contraefecto|SANO|Los dos pesan dos cosas a la vez y ahi acaba el parecido: el candidato elige entre retener el material en una barrera y dejarlo correr con muestreo, y pesa calidad contra perturbacion del flujo (L139 a L141); el vecino empareja un indicador con el de su contraefecto (L31). Ninguno despliega una linea del otro. ESTE CANDIDATO SALIA ENTRARIA a poblacion 462 y HOY BLOQUEA por la correccion del vecino.
    construir_grafico_escalonado_pronosticos|SANO|Ajenos: inspeccion de barrera o monitorizacion (L141) contra un grafico que compara pronosticos sucesivos (L91 a L93). La senial sale de vocabulario comun. VECINO NUEVO por la correccion del vecino.

### 64.5.b. ARISTAS POR LECTURA (D.29)

**Madre, hijo, la linea del libro y la razon, las que sostengo y las que no.** Sede: `.v64ext/aristas_lectura.txt`.
**La senial no levanta ninguna de las `SOSTENGO` en ningun sentido** (matriz de los `22` y `.v64ext/pares_despues.txt`),
salvo la segunda, que hoy si levanta y por eso va ademas en los bloques de veredicto. **Se cablean al insertar el
hijo, con la madre ya en el grafo**, con `python forja.py arista --madre --hijo --paso --razon` (`D.29`, `D.53`).
**Ninguna es serie de `D.37`**: ningun texto de los `22` dice cuantas partes tiene con las partes viviendo como
nodo, y en eso coincido con la apertura sellada (`64.4`).

| | madre | hijo | pasos | linea | razon |
|---|---|---|---|---|---|
| **SOSTENGO** | `elegir_indicador_salida_trabajo_administrativo` | `dimensionar_plantilla_administrativa_pronostico` | madre pasos 1 a 7, hijo paso 1 | cap_03 L125 | El paso 1 del hijo, elige con cuidado los indicadores que caracterizan a la unidad administrativa, nombra en una linea el procedimiento que la madre despliega en siete pasos, y el hijo sigue donde ella acaba con los suyos (pasos 2 a 7). Dependencia de proceso, como el ejemplar de D.29. La senial no lo levanta en ningun sentido. |
| **SOSTENGO** | `construir_indicador_tendencia_patron` | `dimensionar_plantilla_administrativa_pronostico` | madre pasos 2 a 4, hijo paso 2 | cap_03 L125 | El paso 2 del hijo deduce patrones de hecho de los datos de tendencia, que son el producto de la madre. HOY LA SENIAL LO LEVANTA en los dos sentidos tras la correccion de la madre, asi que ademas de aqui va en los dos bloques de VEREDICTOS LISTOS como CONTINUA. |
| **SOSTENGO** | `elegir_fabricar_pedido_pronostico` | `casar_flujo_fabricacion_flujo_ventas` | madre pasos 4 a 7, hijo paso 1 | cap_03 L111 | El hijo empieza donde la madre decide fabricar contra pronostico: su paso 1 trata la entrega de un producto fabricado contra pronostico, que es la via que la madre elige y asume en sus pasos 4 a 7, y anade los dos flujos, los dos pronosticos, la holgura en inventario y el grafico escalonado (pasos 2 a 12). |
| **SOSTENGO** | `construir_grafico_escalonado_pronosticos` | `casar_flujo_fabricacion_flujo_ventas` | madre pasos 1 a 8, hijo paso 12 | cap_03 L121 | L121 dice As noted y remite al grafico de L91 a L97; el paso 12 del hijo usa el procedimiento de la madre en los dos pronosticos, el de fabricacion y el de ventas, con su proposito propio: acotar las causas de inexactitud. Nombrar no es procedimentar decide si una linea cuenta como despliegue, y aqui nadie la cuenta asi: la arista dice que el hijo usa a la madre, como verificar_afirmaciones usa a formular_codigo en el ejemplar de D.29 (DISCUTIBLE D64.6). |
| **SOSTENGO** | `representar_actividad_caja_negra_ventanas` | `construir_indicador_linealidad_alerta_temprana` | madre paso 8, hijo paso 2 | cap_03 L83 | El paso 2 del hijo, recorta en tu caja esta ventana concreta, el indicador de linealidad, es una de las ventanas que el paso 8 de la madre manda recortar; L83 dice a window cut into the black box is the linearity indicator. El hijo anade la recta ideal, el trazado, la lectura a media carrera y la accion correctora. |
| **SOSTENGO** | `representar_actividad_caja_negra_ventanas` | `construir_indicador_tendencia_patron` | madre paso 8, hijo paso 1 | cap_03 L89 | El paso 1 del hijo, monta el indicador de tendencia, que es otra ventana recortada en tu caja, es otra de las ventanas del paso 8 de la madre; L89 dice This extrapolation gives us another window in our black box. Mia y no de la apertura sellada (DISCUTIBLE D64.7). |
| **SOSTENGO** | `dimensionar_inventario_materia_prima_reposicion` | `decidir_aceptar_rechazar_material_defectuoso` | madre paso 3, hijo paso 1 | cap_03 L135 | La madre cierra el rechazo en la inspeccion de recepcion con una sola salida, devuelve el material (paso 3, cap_02 L69); el paso 1 del hijo abre ahi mismo la decision con dos salidas, devolver o usar lo que no llega, y anade el grupo equilibrado que la toma y la regla de fiabilidad (pasos 2 a 8). L135 empieza When material is rejected at incoming inspection. Leido despues de abrir la apertura sellada. |
| **SOSTENGO** | `rehacer_flujo_paso_limitante_capacidad` | `equilibrar_capacidad_personal_inventario_plazo` | madre pasos 2 a 4, hijo paso 1 | cap_02 L57 | El hijo sigue donde la madre acaba: con el flujo rehecho alrededor de la cola del tostador, L57 complica el mismo caso (stuck in line waiting for a toaster when it is time to start boiling your egg), y el paso 1 del hijo es ese choque; el hijo anade las cuatro salidas con su coste y el intercambio de equipo, personal e inventario contra el plazo (pasos 2 a 8). Leido despues de abrir la apertura sellada, que lo daba con confianza media. |
| **NO SOSTENGO** | `elegir_fabricar_pedido_pronostico` | `dimensionar_plantilla_administrativa_pronostico` | hijo paso 4 | cap_03 L123 | El paso 4 del hijo pronostica la carga y ajusta la salida, pero la madre no ensena a pronosticar: elige entre dos vias de fabricar. Es la idea comun de fabricar contra pronostico, no un procedimiento que el hijo use. Va SANO en el bloque de dimensionar_plantilla, porque ese sentido la senial si lo levanta. |
| **NO SOSTENGO** | `detectar_arreglar_fallo_etapa_menor_valor` | `casar_flujo_fabricacion_flujo_ventas` | hijo paso 11 | cap_03 L119 | El paso 11 del hijo guarda el inventario en la etapa de menor valor; la regla de la madre es detectar y arreglar fallos en esa etapa. Son dos consecuencias distintas del mismo principio del valor anadido (cap_02 L73), y ninguna usa a la otra. SANO, como la apertura sellada, aunque ella lo cierra por nombrar no es procedimentar. |
| **NO SOSTENGO** | `elegir_cinco_indicadores_diarios_fabrica` | `construir_indicador_linealidad_alerta_temprana` | hijo paso 1 | cap_03 L83 | El paso 1 del hijo cuenta como adelantados los controles diarios que ya usas, pero no ejecuta el procedimiento de elegir los cinco: los reclasifica. SANO. |
| **NO SOSTENGO** | `representar_actividad_caja_negra_ventanas` | `construir_grafico_escalonado_pronosticos` | ninguno | cap_03 L91 | L91 presenta el escalonado como otra manera de anticipar el futuro, no como ventana de la caja, y ningun paso del escalonado nombra la caja. SANO. |
| **NO SOSTENGO** | `elegir_inspeccion_barrera_monitorizacion` | `variar_frecuencia_inspeccion_nivel_calidad` | ninguno | cap_03 L143 | Hermanos: L143 dice Another way to lower the cost of quality assurance, y ninguno usa al otro. SANO, como la apertura sellada. |

**Las lineas de la tabla, pegadas** (`D.35`), cortadas en el propio `grep -o`:

<!-- TALLADO: parcial salida=.v64ext/citas_t4.txt -->

    $ grep -n -o "if we have carefully chosen indicators that characterize an administrative unit" fuentes/grove_high_output/cap_03.md
    125:if we have carefully chosen indicators that characterize an administrative unit
    $ grep -n -o "de facto standards, inferred from the trend data" fuentes/grove_high_output/cap_03.md
    125:de facto standards, inferred from the trend data
    $ grep -n -o "Delivering a product that was built to forecast to a customer consists of two simultaneous processes" fuentes/grove_high_output/cap_03.md
    111:Delivering a product that was built to forecast to a customer consists of two simultaneous processes
    $ grep -n -o "It is a good idea to use stagger charts in both the manufacturing and sales forecasts. As noted" fuentes/grove_high_output/cap_03.md
    121:It is a good idea to use stagger charts in both the manufacturing and sales forecasts. As noted
    $ grep -n -o "a .window. cut into the black box is the linearity indicator" fuentes/grove_high_output/cap_03.md
    83:a “window” cut into the black box is the linearity indicator
    $ grep -n -o "This extrapolation gives us another window in our black box" fuentes/grove_high_output/cap_03.md
    89:This extrapolation gives us another window in our black box
    $ grep -n -o "When material is rejected at incoming inspection, a couple of choices present themselves" fuentes/grove_high_output/cap_03.md
    135:When material is rejected at incoming inspection, a couple of choices present themselves
    $ grep -n -o "stuck in line waiting for a toaster when it.s time to start boiling your egg" fuentes/grove_high_output/cap_02.md
    57:stuck in line waiting for a toaster when it’s time to start boiling your egg
    $ grep -n -o "Forecasting future work demands and then adjusting the output" fuentes/grove_high_output/cap_03.md
    123:Forecasting future work demands and then adjusting the output
    $ grep -n -o "inventory should be kept at the lowest-value stage, as we.ve learned before" fuentes/grove_high_output/cap_03.md
    119:inventory should be kept at the lowest-value stage, as we’ve learned before
    $ grep -n -o "Leading indicators might include the daily monitors we use to run our breakfast factory" fuentes/grove_high_output/cap_03.md
    83:Leading indicators might include the daily monitors we use to run our breakfast factory
    $ grep -n -o "Another sound way to anticipate the future is through the use of the stagger chart" fuentes/grove_high_output/cap_03.md
    91:Another sound way to anticipate the future is through the use of the stagger chart
    $ grep -n -o "Another way to lower the cost of quality assurance is to use variable inspections" fuentes/grove_high_output/cap_03.md
    143:Another way to lower the cost of quality assurance is to use variable inspections

> **DISCUTIBLES DE ARISTA, MARCADOS AL ESCRIBIRLAS**
>
> - **`D64.6`**: `construir_grafico_escalonado...` madre de `casar_flujo...` la sostengo **sin rebajarla**, y la
>   apertura sellada la daba con confianza baja por *nombrar no es procedimentar*. Mi motivo: esa vara decide si
>   una linea cuenta como despliegue de otro nodo (continua o repite), no si un hijo usa a una madre; el ejemplar
>   de `D.29` es exactamente un hijo que nombra a su madre en un paso y la usa.
> - **`D64.7`**: `representar_actividad_caja_negra...` madre de `construir_indicador_tendencia...` (L89, *another
>   window in our black box*) es mia y no de la apertura sellada, que solo daba la de la linealidad.

### 64.5.c. EL ORDEN DE LOS `22`, MADRE ANTES QUE HIJO, Y LA TANDA QUE PROPONGO PARA LA `65`

**La tabla la imprime `.v64ext/orden.py`**: lo unico que escribo a mano es la lista del orden; las madres las lee
de los veredictos y de las aristas, el informe vigente y su poblacion de su fichero, los vecinos de la matriz y de
`pares_despues.txt`, y *listos* es que cada vecino que levanta tenga su linea. **Y comprueba las tres reglas**:
ningun hijo delante de su madre, `D.36` (un par que levanta en un solo sentido se inserta con el que lo levanta
despues), y ningun hijo dentro del tope con la madre fuera. La columna *dijo(462)* es lo que dijo su informe
archivado, no lo que diria hoy: `equilibrar` y `elegir_inspeccion` bloquearian (`64.5.a`).

<!-- TALLADO: parcial salida=.v64ext/orden.txt -->

    $ python .v64ext/orden.py
    #   candidato                                        cap    pza  madre(s)                                     informe         pob  dijo(462)  vec  lin   listos
    1   construir_flujo_produccion_paso_limitante        cap_02 P2   -                                            .v63aud         462  BLOQUEARIA 3    3     SI
    2   clasificar_trabajo_proceso_montaje_prueba        cap_02 P5   -                                            .v63aud         462  BLOQUEARIA 1    1     SI
    3   detectar_arreglar_fallo_etapa_menor_valor        cap_02 P11  -                                            .v63aud         462  BLOQUEARIA 1    1     SI
    4   dimensionar_inventario_materia_prima_reposicion  cap_02 P10  detectar_arreglar_fallo_etapa_menor_valor    .v63aud         462  BLOQUEARIA 2    2     SI
    5   rehacer_flujo_paso_limitante_capacidad           cap_02 P6   construir_flujo_produccion_paso_limitante    .v63aud         462  BLOQUEARIA 3    3     SI
    6   equilibrar_capacidad_personal_inventario_plazo   cap_02 P7   rehacer_flujo_paso_limitante_capacidad       .v63aud         462  ENTRARIA   1    1     SI
    7   preferir_inspeccion_proceso_prueba_destructiva   cap_02 P9   -                                            .v63aud         462  BLOQUEARIA 4    4     SI
    8   elegir_cinco_indicadores_diarios_fabrica         cap_03 P2   -                                            .v63aud         462  ENTRARIA   0    0     SI
    9   emparejar_indicadores_efecto_contraefecto        cap_03 P3   -                                            archivo fase 2  462  BLOQUEARIA 6    6     SI
    10  elegir_indicador_salida_trabajo_administrativo   cap_03 P4   emparejar_indicadores_efecto_contraefecto    archivo fase 2  462  BLOQUEARIA 3    3     SI
    11  representar_actividad_caja_negra_ventanas        cap_03 P7   -                                            .v63aud         462  ENTRARIA   0    0     SI
    12  construir_indicador_linealidad_alerta_temprana   cap_03 P9   representar_actividad_caja_negra_ventanas    .v63aud         462  ENTRARIA   0    0     SI
    13  construir_indicador_tendencia_patron             cap_03 P10  representar_actividad_caja_negra_ventanas    archivo fase 2  462  BLOQUEARIA 6    6     SI
    14  construir_grafico_escalonado_pronosticos         cap_03 P11  -                                            archivo fase 2  462  BLOQUEARIA 3    3     SI
    15  archivar_indicadores_resolver_problemas          cap_03 P12  -                                            archivo fase 2  462  BLOQUEARIA 4    4     SI
    16  elegir_fabricar_pedido_pronostico                cap_03 P13  -                                            archivo fase 2  462  BLOQUEARIA 2    2     SI
    17  casar_flujo_fabricacion_flujo_ventas             cap_03 P14  construir_grafico_escalonado_pronosticos, elegir_fabricar_pedido_pronostico .v63aud         462  ENTRARIA   0    0     SI
    18  dimensionar_plantilla_administrativa_pronostico  cap_03 P15  construir_indicador_tendencia_patron, elegir_indicador_salida_trabajo_administrativo .v63aud         462  BLOQUEARIA 6    6     SI
    19  decidir_aceptar_rechazar_material_defectuoso     cap_03 P17  dimensionar_inventario_materia_prima_reposicion .v63aud         462  BLOQUEARIA 1    1     SI
    20  elegir_inspeccion_barrera_monitorizacion         cap_03 P18  -                                            .v63aud         462  ENTRARIA   2    2     SI   <- corte del tope
    21  variar_frecuencia_inspeccion_nivel_calidad       cap_03 P19  -                                            .v63aud         462  ENTRARIA   0    0     SI
    22  simplificar_trabajo_reducir_numero_pasos         cap_03 P23  -                                            .v63aud         462  BLOQUEARIA 1    1     SI
    
    COMPROBACIONES
      hijo delante de su madre: 0 []
      D.36, par que levanta en un solo sentido con el que lo levanta entrando antes: 0 []
      hijo dentro del tope con su madre fuera: 0 []
      tanda propuesta: 20 de 22; fuera del tope: variar_frecuencia_inspeccion_nivel_calidad, simplificar_trabajo_reducir_numero_pasos

**LO QUE EL ORDEN CAMBIA RESPECTO AL DEL LIBRO, y por que**: en `cap_02`, `detectar` (`P11`) y
`dimensionar_inventario` (`P10`) suben delante de `rehacer` (`P6`). `detectar` es madre de `dimensionar_inventario`,
y `rehacer` levanta a `dimensionar_inventario` y no al reves (`0,357` contra `0,329`, `.v64ext/pares_despues.txt`),
asi que **`D.36` pide que `rehacer` entre despues para que su informe lea el par**. `cap_03` entra en el orden del
libro, que ya pone cada madre delante.

**LA TANDA QUE PROPONGO PARA LA `65`: LAS FILAS `1` A `20`**, `cap_02` entero y `13` de `cap_03`, con
`variar_frecuencia...` y `simplificar_trabajo...` para la siguiente. Ninguno de los dos es madre de nadie, y los
dos leen a sus vecinos desde el grafo cuando entren. **Proponer no es fijar**: el orden lo fija quien autoriza
(`D.36`), y lo recoge el encargo de la `65`.

**Y EL RELOJ, MEDIDO HOY Y NO PROMETIDO**: `aduana.medir` me costo unos `3,9` s por par con las fichas de Grove en
primer plano (`486` s para `126` pares) y `4,6` s con tres trozos en paralelo (`576` s para `126`), y el barrido de
una sola ficha contra `462` no cupo en `590` s. **Veinte `insertar` son varias horas de aduana**, en primer plano y
uno por vez. **Si no caben en el turno de la `65`, que la tanda sea mas corta, no que alguno quede en vuelo.**
