## XX.3. TAREA 3. MINAR, CON EL TECHO POR DELANTE

**Los siete candidatos, en el orden del libro, cada uno escrito y pasado por**
**`python forja.py informe` en el mismo acto** (`EXTRACTOR.md` 16). Para que la prueba fuera
real y no solo dicha, los seis candidatos todavia no probados se sacaron de
`cuarentena/grove_high_output/` a una carpeta de espera (`.v58ext/pendientes/`) antes de correr
el primer informe, y cada uno volvio a entrar UNO A LA VEZ, justo antes de correr su propio
informe. **La linea `poblacion del barrido` de cada informe es la salida real del instrumento,
no una promesa** (`D.35`): sube de candidato en candidato, `431`, `432`, `433`, `434`, `435`,
`436` y `437`, de uno en uno, porque de uno en uno es como se escribieron.

**CERO INSERCIONES.** El lote `7` sigue ABIERTO y `D.39` no deja entrar nada: los siete informes
son de SOLO LECTURA, y ningun veredicto se escribe en `bitacora/VEREDICTOS.jsonl` esta vuelta.

### XX.3.1. `entregar_evaluacion_desempeno_tres_claves` (cap_14)

<!-- TALLADO: salida=.v58ext/informe_1_entregar_evaluacion_desempeno_tres_claves.txt -->

    $ python forja.py informe cuarentena/grove_high_output/entregar_evaluacion_desempeno_tres_claves.json

    ============================================================================
    INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
    ============================================================================
    candidatos revisados        : 1
    poblacion del barrido       : 431   (346 del grafo mas 85 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

    EL SALDO
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0

    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 2
      por candidato bloqueado          : menor 2, mediana 2, mayor 2
      que señal levanta cada vecindad  : similitud_texto 2

    ============================================================================
    LA LISTA COMPLETA, candidato por candidato
    ============================================================================

    [BLOQUEARIA] entregar_evaluacion_desempeno_tres_claves   (entregar_evaluacion_desempeno_tres_claves.json)
        vecino zanjar_seis_preguntas_decision_adelantado  [levantada por: similitud_texto]
          similitud_texto 0.362 | familia_id 0.000 | paso_contra_nodo 0.407
          paso 5 del candidato contra paso 3 de zanjar_seis_preguntas_decision_adelantado
        vecino anunciar_decision_inesperada_reconvocar_reunion  [levantada por: similitud_texto]
          similitud_texto 0.351 | familia_id 0.000 | paso_contra_nodo 0.374
          paso 6 del candidato contra paso 4 de anunciar_decision_inesperada_reconvocar_reunion

    NADA SE INSERTO. Este informe es de SOLO LECTURA: para que un nodo
    entre hace falta python forja.py insertar, uno por vez, con su
    veredicto escrito por vecino.

**Lectura del vecino:** Lei a los dos vecinos: son nodos distintos (protocolo de decision de seis preguntas y reconvocar una reunion), el solape es de vocabulario de conversacion y no de doctrina. Sigue en cuarentena, sin veredicto en bitacora porque no se inserta esta vuelta (`D.39`).

### XX.3.2. `preparar_resena_mixta_hoja_trabajo` (cap_14)

<!-- TALLADO: salida=.v58ext/informe_2_preparar_resena_mixta_hoja_trabajo.txt -->

    $ python forja.py informe cuarentena/grove_high_output/preparar_resena_mixta_hoja_trabajo.json

    ============================================================================
    INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
    ============================================================================
    candidatos revisados        : 1
    poblacion del barrido       : 432   (346 del grafo mas 86 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

    EL SALDO
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0

    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 1
      por candidato bloqueado          : menor 1, mediana 1, mayor 1
      que señal levanta cada vecindad  : similitud_texto 1

    ============================================================================
    LA LISTA COMPLETA, candidato por candidato
    ============================================================================

    [BLOQUEARIA] preparar_resena_mixta_hoja_trabajo   (preparar_resena_mixta_hoja_trabajo.json)
        vecino entregar_evaluacion_desempeno_tres_claves  [levantada por: similitud_texto]
          similitud_texto 0.379 | familia_id 0.000 | paso_contra_nodo 0.438
          paso 5 del candidato contra paso 6 de entregar_evaluacion_desempeno_tres_claves

    NADA SE INSERTO. Este informe es de SOLO LECTURA: para que un nodo
    entre hace falta python forja.py insertar, uno por vez, con su
    veredicto escrito por vecino.

**Lectura del vecino:** El unico vecino es su hermano de capitulo, `entregar_evaluacion_desempeno_tres_claves`: preparar la resena y entregarla son dos momentos distintos del mismo proceso, con condicion de activacion distinta. No es gemelo.

### XX.3.3. `guiar_subordinado_etapas_resistencia_desempeno` (cap_14)

<!-- TALLADO: salida=.v58ext/informe_3_guiar_subordinado_etapas_resistencia_desempeno.txt -->

    $ python forja.py informe cuarentena/grove_high_output/guiar_subordinado_etapas_resistencia_desempeno.json

    ============================================================================
    INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
    ============================================================================
    candidatos revisados        : 1
    poblacion del barrido       : 433   (346 del grafo mas 87 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

    EL SALDO
      ENTRARIAN sin leer nada          : 1
      BLOQUEARIAN esperando veredicto  : 0   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0

    ============================================================================
    LA LISTA COMPLETA, candidato por candidato
    ============================================================================

    [ENTRARIA] guiar_subordinado_etapas_resistencia_desempeno   (guiar_subordinado_etapas_resistencia_desempeno.json)

    NADA SE INSERTO. Este informe es de SOLO LECTURA: para que un nodo
    entre hace falta python forja.py insertar, uno por vez, con su
    veredicto escrito por vecino.

**Lectura del vecino:** Sin vecinos levantados: entra limpio. Es el candidato que llevo el discutible de existencia marcado en `XX.4`.

### XX.3.4. `usar_banco_nueve_preguntas_entrevista` (cap_15)

<!-- TALLADO: salida=.v58ext/informe_4_usar_banco_nueve_preguntas_entrevista.txt -->

    $ python forja.py informe cuarentena/grove_high_output/usar_banco_nueve_preguntas_entrevista.json

    ============================================================================
    INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
    ============================================================================
    candidatos revisados        : 1
    poblacion del barrido       : 434   (346 del grafo mas 88 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

    EL SALDO
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0

    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 1
      por candidato bloqueado          : menor 1, mediana 1, mayor 1
      que señal levanta cada vecindad  : paso_contra_nodo 1

    ============================================================================
    LA LISTA COMPLETA, candidato por candidato
    ============================================================================

    [BLOQUEARIA] usar_banco_nueve_preguntas_entrevista   (usar_banco_nueve_preguntas_entrevista.json)
        vecino identificar_disparadores_propios_reaccion  [levantada por: paso_contra_nodo]
          similitud_texto 0.128 | familia_id 0.000 | paso_contra_nodo 0.607
          paso 2 del candidato contra paso 9 de identificar_disparadores_propios_reaccion

    NADA SE INSERTO. Este informe es de SOLO LECTURA: para que un nodo
    entre hace falta python forja.py insertar, uno por vez, con su
    veredicto escrito por vecino.

**Lectura del vecino:** El vecino es de otro dominio (`identificar_disparadores_propios_reaccion`), levantado por `paso_contra_nodo` en un unico paso: coincidencia de frase, no de doctrina.

### XX.3.5. `responder_primer_aviso_renuncia_subordinado` (cap_15)

<!-- TALLADO: salida=.v58ext/informe_5_responder_primer_aviso_renuncia_subordinado.txt -->

    $ python forja.py informe cuarentena/grove_high_output/responder_primer_aviso_renuncia_subordinado.json

    ============================================================================
    INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
    ============================================================================
    candidatos revisados        : 1
    poblacion del barrido       : 435   (346 del grafo mas 89 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

    EL SALDO
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0

    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 4
      por candidato bloqueado          : menor 4, mediana 4, mayor 4
      que señal levanta cada vecindad  : paso_contra_nodo 1, similitud_texto 3

    ============================================================================
    LA LISTA COMPLETA, candidato por candidato
    ============================================================================

    [BLOQUEARIA] responder_primer_aviso_renuncia_subordinado   (responder_primer_aviso_renuncia_subordinado.json)
        vecino preguntar_seguimiento_hallar_huecos  [levantada por: paso_contra_nodo]
          similitud_texto 0.204 | familia_id 0.000 | paso_contra_nodo 0.627
          paso 2 del candidato contra paso 2 de preguntar_seguimiento_hallar_huecos
        vecino anunciar_decision_inesperada_reconvocar_reunion  [levantada por: similitud_texto]
          similitud_texto 0.352 | familia_id 0.000 | paso_contra_nodo 0.491
          paso 7 del candidato contra paso 6 de anunciar_decision_inesperada_reconvocar_reunion
        vecino construir_indicador_tendencia_patron  [levantada por: similitud_texto]
          similitud_texto 0.354 | familia_id 0.000 | paso_contra_nodo 0.417
          paso 3 del candidato contra paso 6 de construir_indicador_tendencia_patron
        vecino entregar_evaluacion_desempeno_tres_claves  [levantada por: similitud_texto]
          similitud_texto 0.356 | familia_id 0.000 | paso_contra_nodo 0.408
          paso 1 del candidato contra paso 3 de entregar_evaluacion_desempeno_tres_claves

    NADA SE INSERTO. Este informe es de SOLO LECTURA: para que un nodo
    entre hace falta python forja.py insertar, uno por vez, con su
    veredicto escrito por vecino.

**Lectura del vecino:** Cuatro vecinos, ninguno por encima de 0,4 de similitud de texto (banda de gemelos real): son tecnicas de conversacion vecinas por vocabulario, no duplicados.

### XX.3.6. `gestionar_retencion_subordinado_valioso_renuncia` (cap_15)

<!-- TALLADO: salida=.v58ext/informe_6_gestionar_retencion_subordinado_valioso_renuncia.txt -->

    $ python forja.py informe cuarentena/grove_high_output/gestionar_retencion_subordinado_valioso_renuncia.json

    ============================================================================
    INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
    ============================================================================
    candidatos revisados        : 1
    poblacion del barrido       : 436   (346 del grafo mas 90 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

    EL SALDO
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0

    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 2
      por candidato bloqueado          : menor 2, mediana 2, mayor 2
      que señal levanta cada vecindad  : similitud_texto 2

    ============================================================================
    LA LISTA COMPLETA, candidato por candidato
    ============================================================================

    [BLOQUEARIA] gestionar_retencion_subordinado_valioso_renuncia   (gestionar_retencion_subordinado_valioso_renuncia.json)
        vecino responder_primer_aviso_renuncia_subordinado  [levantada por: similitud_texto]
          similitud_texto 0.363 | familia_id 0.250 | paso_contra_nodo 0.436
          paso 1 del candidato contra paso 6 de responder_primer_aviso_renuncia_subordinado
        vecino entregar_evaluacion_desempeno_tres_claves  [levantada por: similitud_texto]
          similitud_texto 0.357 | familia_id 0.000 | paso_contra_nodo 0.390
          paso 2 del candidato contra paso 6 de entregar_evaluacion_desempeno_tres_claves

    NADA SE INSERTO. Este informe es de SOLO LECTURA: para que un nodo
    entre hace falta python forja.py insertar, uno por vez, con su
    veredicto escrito por vecino.

**Lectura del vecino:** Bloquea contra su propio hermano de episodio, `responder_primer_aviso_renuncia_subordinado` (familia_id 0,250, bajo el umbral de 0,30 de la señal 2, y similitud_texto 0,363, bajo la banda de 0,4 de gemelos reales de `EXTRACTOR.md` 11). Es exactamente el discutible que marque en `XX.4` antes de correr este informe: la medicion no lo resuelve, lo deja donde estaba, por debajo de ambos umbrales de gemelo.

### XX.3.7. `reciclar_empleado_ascendido_mas_alla_capacidad` (cap_16)

<!-- TALLADO: salida=.v58ext/informe_7_reciclar_empleado_ascendido_mas_alla_capacidad.txt -->

    $ python forja.py informe cuarentena/grove_high_output/reciclar_empleado_ascendido_mas_alla_capacidad.json

    ============================================================================
    INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
    ============================================================================
    candidatos revisados        : 1
    poblacion del barrido       : 437   (346 del grafo mas 91 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

    EL SALDO
      ENTRARIAN sin leer nada          : 1
      BLOQUEARIAN esperando veredicto  : 0   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0

    ============================================================================
    LA LISTA COMPLETA, candidato por candidato
    ============================================================================

    [ENTRARIA] reciclar_empleado_ascendido_mas_alla_capacidad   (reciclar_empleado_ascendido_mas_alla_capacidad.json)

    NADA SE INSERTO. Este informe es de SOLO LECTURA: para que un nodo
    entre hace falta python forja.py insertar, uno por vez, con su
    veredicto escrito por vecino.

**Lectura del vecino:** Sin vecinos levantados: entra limpio.

### XX.3.8. EL SALDO DEL TRAMO

| candidato | capitulo | poblacion del barrido | saldo de la aduana |
|---|---|---:|---|
| `entregar_evaluacion_desempeno_tres_claves` | `cap_14` | 431 | BLOQUEARIA |
| `preparar_resena_mixta_hoja_trabajo` | `cap_14` | 432 | BLOQUEARIA |
| `guiar_subordinado_etapas_resistencia_desempeno` | `cap_14` | 433 | ENTRARIA |
| `usar_banco_nueve_preguntas_entrevista` | `cap_15` | 434 | BLOQUEARIA |
| `responder_primer_aviso_renuncia_subordinado` | `cap_15` | 435 | BLOQUEARIA |
| `gestionar_retencion_subordinado_valioso_renuncia` | `cap_15` | 436 | BLOQUEARIA |
| `reciclar_empleado_ascendido_mas_alla_capacidad` | `cap_16` | 437 | ENTRARIA |

**El tramo de esta vuelta: `3` capitulos (`cap_14`, `cap_15`, `cap_16`) y `7` candidatos, dentro
del techo de `30` de `D.58`.** Dos ENTRARIAN sin vecino, cinco BLOQUEARIAN esperando lectura, y
ninguno CAE ni CHOCA dentro del lote. Los siete quedan en `cuarentena/grove_high_output/`, sin
insertar, hasta que el lote `7` cierre y su insercion se autorice (`D.39`, `EXTRACTOR.md` 15.7).