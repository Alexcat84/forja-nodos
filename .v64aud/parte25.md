## 5. EL BARRIDO DE VECINOS DE LOS SEIS DE `d005`, SOBRE GRAFO MAS BANDEJAS Y CORRIDO EN ESTA FASE (`D.38.4`)

**POBLACION DE ESTA MEDIDA, Y NO ES LA DE LA SECCION `3`:** los seis informes corren sobre las fichas
**tal como estan HOY en la bandeja**, cinco de ellas con commit de la `64`. **El informe no imprime
pasos, solo ids, seniales y numero de paso**, asi que correrlo no me ensenia que corrigio el extractor.
Lo corri porque `d031` dice que retocar una ficha mueve su senial, y la lista de pares del encargo es
de las fichas de `067c9df`.

    $ cat .v64aud/barrido.log
    INICIO 2026-09-23 10:42:57
    archivar_indicadores_resolver_problemas rc=0 segundos=826
    construir_indicador_tendencia_patron rc=0 segundos=1326
    emparejar_indicadores_efecto_contraefecto rc=0 segundos=1519
    elegir_indicador_salida_trabajo_administrativo rc=0 segundos=1656
    construir_grafico_escalonado_pronosticos rc=0 segundos=1789
    elegir_fabricar_pedido_pronostico rc=0 segundos=1979
    TODOS TERMINADOS 2026-09-23 11:15:56

    $ python .v64aud/vecinos_hoy.py
    BLOQUEARIA  archivar_indicadores_resolver_problemas  hoy poblacion 462 | archivo: BLOQUEARIA poblacion 462
        SIGUE             cerrar_brecha_dos_preguntas_estrategia           similitud_texto            texto 0.353 familia 0.000 paso 0.393  paso 4 del candidato contra paso 6
        SIGUE             construir_indicador_tendencia_patron             similitud_texto            texto 0.361 familia 0.143 paso 0.420  paso 2 del candidato contra paso 3
        SIGUE             revisar_tres_preguntas_valor_carrera             similitud_texto            texto 0.369 familia 0.000 paso 0.414  paso 2 del candidato contra paso 1
        SIGUE             vencer_sindrome_grupo_pares_autoconfianza        similitud_texto            texto 0.364 familia 0.000 paso 0.405  paso 1 del candidato contra paso 5
    BLOQUEARIA  construir_grafico_escalonado_pronosticos  hoy poblacion 462 | archivo: BLOQUEARIA poblacion 462
        SIGUE             construir_indicador_tendencia_patron             similitud_texto            texto 0.365 familia 0.143 paso 0.453  paso 4 del candidato contra paso 5
        SIGUE             elegir_fabricar_pedido_pronostico                similitud_texto            texto 0.393 familia 0.143 paso 0.453  paso 7 del candidato contra paso 4
        SIGUE             emparejar_indicadores_efecto_contraefecto        similitud_texto            texto 0.378 familia 0.000 paso 0.434  paso 1 del candidato contra paso 3
    BLOQUEARIA  construir_indicador_tendencia_patron  hoy poblacion 462 | archivo: BLOQUEARIA poblacion 462
        SIGUE             archivar_indicadores_resolver_problemas          similitud_texto            texto 0.365 familia 0.143 paso 0.427  paso 2 del candidato contra paso 1
        SIGUE             construir_grafico_escalonado_pronosticos         similitud_texto            texto 0.362 familia 0.143 paso 0.461  paso 5 del candidato contra paso 4
        NUEVO             dimensionar_plantilla_administrativa_pronostico  similitud_texto            texto 0.373 familia 0.000 paso 0.405  paso 5 del candidato contra paso 6
        NUEVO             elegir_indicador_salida_trabajo_administrativo   similitud_texto            texto 0.378 familia 0.125 paso 0.378  paso 5 del candidato contra paso 3
        NUEVO             emparejar_indicadores_efecto_contraefecto        similitud_texto            texto 0.393 familia 0.143 paso 0.427  paso 5 del candidato contra paso 2
        NUEVO             equilibrar_capacidad_personal_inventario_plazo   similitud_texto            texto 0.353 familia 0.000 paso 0.424  paso 1 del candidato contra paso 4
    BLOQUEARIA  elegir_fabricar_pedido_pronostico  hoy poblacion 462 | archivo: BLOQUEARIA poblacion 462
        SIGUE             construir_grafico_escalonado_pronosticos         similitud_texto            texto 0.387 familia 0.143 paso 0.440  paso 4 del candidato contra paso 7
        NUEVO             emparejar_indicadores_efecto_contraefecto        similitud_texto            texto 0.362 familia 0.000 paso 0.419  paso 2 del candidato contra paso 3
    BLOQUEARIA  elegir_indicador_salida_trabajo_administrativo  hoy poblacion 462 | archivo: BLOQUEARIA poblacion 462
        NUEVO             construir_indicador_tendencia_patron             similitud_texto            texto 0.374 familia 0.125 paso 0.403  paso 6 del candidato contra paso 3
        SIGUE             emparejar_indicadores_efecto_contraefecto        similitud_texto            texto 0.394 familia 0.125 paso 0.489  paso 3 del candidato contra paso 4
        SIGUE             evaluar_directivo_resultados_fortaleza           paso_contra_nodo           texto 0.170 familia 0.000 paso 0.766  paso 2 del candidato contra paso 1
    BLOQUEARIA  emparejar_indicadores_efecto_contraefecto  hoy poblacion 462 | archivo: BLOQUEARIA poblacion 462
        SIGUE             construir_grafico_escalonado_pronosticos         similitud_texto            texto 0.384 familia 0.000 paso 0.446  paso 3 del candidato contra paso 1
        SIGUE             construir_indicador_tendencia_patron             similitud_texto            texto 0.397 familia 0.143 paso 0.453  paso 3 del candidato contra paso 5
        NUEVO             dimensionar_plantilla_administrativa_pronostico  similitud_texto            texto 0.355 familia 0.000 paso 0.396  paso 4 del candidato contra paso 2
        NUEVO             elegir_cinco_indicadores_diarios_fabrica         similitud_texto            texto 0.359 familia 0.125 paso 0.445  paso 4 del candidato contra paso 8
        SIGUE             elegir_fabricar_pedido_pronostico                similitud_texto            texto 0.367 familia 0.000 paso 0.408  paso 4 del candidato contra paso 1
        NUEVO             elegir_indicador_salida_trabajo_administrativo   similitud_texto            texto 0.383 familia 0.125 paso 0.468  paso 4 del candidato contra paso 3
        DEJA DE LEVANTAR  revisar_tres_preguntas_valor_carrera             similitud_texto            texto 0.354 familia 0.000 paso 0.386  paso 2 del candidato contra paso 2
    pares que siguen: 15 | dejan de levantar: 1 | nuevos: 9

**Las cifras de esas filas son las de HOY**; la fila `DEJA DE LEVANTAR` lleva las del archivo, porque hoy
no hay. **El `15`, `1` y `9` cuentan filas candidato a vecino**, no pares: un par visto desde los dos
lados cuenta dos veces ahi. **Los pares distintos los cuenta otro instrumento:**

    $ python .v64aud/pares_d005.py
    pares distintos: archivo 12 | hoy 16 | en los dos 11 | solo archivo 1 | solo hoy 5
       SOLO ARCHIVO   emparejar_indicadores_efecto_contraefecto | revisar_tres_preguntas_valor_carrera
       SOLO HOY       construir_indicador_tendencia_patron | dimensionar_plantilla_administrativa_pronostico
       SOLO HOY       construir_indicador_tendencia_patron | elegir_indicador_salida_trabajo_administrativo
       SOLO HOY       construir_indicador_tendencia_patron | equilibrar_capacidad_personal_inventario_plazo
       SOLO HOY       dimensionar_plantilla_administrativa_pronostico | emparejar_indicadores_efecto_contraefecto
       SOLO HOY       elegir_cinco_indicadores_diarios_fabrica | emparejar_indicadores_efecto_contraefecto

**Los seis siguen en `BLOQUEARIA` y la poblacion sigue en `462`.** `archivar...` **no tiene commit de la
`64` y aun asi sus cifras se mueven** (`0.384` en el archivo, `0.361` hoy, contra `construir_indicador_tendencia`):
**LECTURA:** es `d031` desde el otro lado, porque el que cambio es el vecino.

**MI CLASE DE LOS SEIS PARES QUE CAMBIAN** (los once que siguen van en la seccion `6.1`):

| par | estado | mi clase | lo que la sostiene |
|---|---|---|---|
| `emparejar...` con `revisar_tres_preguntas_valor_carrera` | **deja de levantar** | **SANO** (sin cambios) | ya lo leia SANO en `6.1`. **Si hay un veredicto escrito sobre este par, esta escrito sobre un vecino que la senial ya no levanta**, y eso se tiene que decir (encargo `2.c`) |
| `construir_indicador_tendencia_patron` con `dimensionar_plantilla_administrativa_pronostico` | **nuevo** | **CONTINUA, madre `construir_indicador_tendencia...`, hijo `dimensionar_plantilla...`** | **es uno de los pares de `d141` que la seccion `7` lee sin senial**: L125, *de facto standards, inferred from the trend data*. **LECTURA:** la senial lo levanta hoy y no lo levantaba el `23` a primera hora; la arista que leia sin senial ahora tiene tambien senial |
| `construir_indicador_tendencia...` con `elegir_indicador_salida_trabajo_administrativo` | **nuevo** | **SANO** | los dos hablan de salida (*vouchers processed* sale en L37 a L45 y en L89), pero la condicion del indicador de tendencia es *cuando ya tienes nombrada la salida de tu caja*, que es la caja negra de L73 y no la tabla administrativa. Ninguno toma lo que el otro produce |
| `construir_indicador_tendencia...` con `equilibrar_capacidad_personal_inventario_plazo` | **nuevo** | **SANO** | la tendencia de la salida contra los cuatro costes del tostador (`cap_02` L57 a L61): nada en comun |
| `emparejar...` con `dimensionar_plantilla...` | **nuevo** | **SANO** | emparejar indicadores contra ajustar la plantilla a la carga pronosticada |
| `emparejar...` con `elegir_cinco_indicadores_diarios_fabrica` | **nuevo** | **SANO** | ya lo miraba en la seccion `7` sin senial: el quinto dato de `elegir_cinco` pone calidad junto a cantidad (L27), **pero el libro no lo presenta como par de efecto y contraefecto**; eso llega en L31 |

