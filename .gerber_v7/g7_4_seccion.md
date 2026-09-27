
## G7.4. TAREA 4: `cap_19`, PORQUE EL TECHO LO PERMITE, Y CUANTO QUEDA DE `d111`

### G7.4.a. El techo, medido antes de decidir

**Techo de esta vuelta: `30` candidatos, hasta `3` capitulos** (`EXTRACTOR.md` `15`, regimen `EXTRACCION`
con `MODO_INSERCION=cuarentena`, `D.58`, `19` sep 2026, el mas reciente sobre la cifra vieja de `12.4`).
`cap_18` cerro con `3` candidatos (`G7.3`): **`3` de `30`, muy por debajo del techo.** El encargo autoriza
minar `cap_19` si el techo lo permite, y lo permite con margen de sobra.

### G7.4.b. El borde de arriba, comparado contra `wc -l`

    $ wc -l fuentes/gerber_emyth/cap_19.md
    441 fuentes/gerber_emyth/cap_19.md

**`441` lineas, al digito con las `441` que el encargo cuenta en su cabecera.**

### G7.4.c. La frontera, publicada antes de cortar

Salida de `python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_19.md .gerber_v7/piezas_cap19.txt`,
guardada en `.gerber_v7/frontera_cap19.txt`:

<!-- TALLADO: salida=.gerber_v7/frontera_cap19.txt -->

    AVISO: cero celdas tecleadas en este instrumento. El arranque del cuerpo NO
    es una constante mia: sale de fuentes/gerber_emyth/cap_19.md, linea 8, que es la siguiente al segundo
    --- de la cabecera yaml (cierres en L1 y L7). El cuerpo va de L8 a L441.

    | pieza | lineas | palabras | que es | clase |
    |---|---|---:|---|---|
    | `R1` | L8 a L20 | **41** | numero de capitulo, rotulo YOUR SYSTEMS STRATEGY, epigrafe de Heisenberg | **RESIDUO** |
    | `R2` | L21 a L32 | **108** | que es un sistema en general | **POSTURA** |
    | `D1` | L33 a L46 | **128** | Three Kinds of Systems: Hard, Soft e Information Systems, cada uno definido | **CANDIDATO: distinguir_tres_tipos_sistemas_negocio** |
    | `R3` | L47 a L122 | **625** | el caso del Prevent a Smudge System de E Myth Worldwide | **CASO: Hard Systems** |
    | `R4` | L123 a L140 | **96** | Soft Systems: la gente vende, el 20 por ciento que usa sistema | **POSTURA: bridge** |
    | `D2` | L141 a L154 | **117** | un sistema de venta en seis pasos principales, numerados | **CANDIDATO: aplicar_seis_pasos_sistema_venta** |
    | `R5` | L155 a L304 | **2040** | Power Point Selling System y Process con sus tres Benchmarks, guion ficticio de Johnny Jones | **CASO: Soft Systems, el guion de venta** |
    | `R6` | L305 a L306 | **2** | rotulo Information Systems | **POSTURA: bridge** |
    | `D3` | L307 a L338 | **126** | INFORMATION BENCHMARK: trece preguntas numeradas | **CANDIDATO: medir_sistema_venta_trece_indicadores_benchmark** |
    | `R7` | L339 a L441 | **1148** | integracion de las siete Strategies, cierre con Sarah | **POSTURA y CASO: cierre del capitulo y del libro** |
    | **el cuerpo entero** | **L8 a L441** | **4431** | **suma de las piezas: 4431** | **residuo sin asignar: 0** |

    piezas: 10   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 4431   suma 4431   residuo 0

**`4431` PALABRAS, AL DIGITO CON LAS `4431` QUE EL ENCARGO CUENTA. `10` PIEZAS, `0` SOLAPES, `0` LINEAS
SIN CUBRIR, RESIDUO `0`.** Fichero completo en `.gerber_v7/piezas_cap19.txt` (D.42).

**DECISION DE ALCANCE DECLARADA SOBRE `R5`** (`2040` palabras, la pieza mas grande del capitulo): el
Power Point Selling Process (los tres Benchmarks Appointment, Needs Analysis y Solutions Presentation)
se cuenta entero como guion ficticio de Johnny Jones y Mr. Jackson en la Walter Mitty Company. La
doctrina generica que ese guion ilustra (identificar Benchmarks, escribir el guion, entregarlo
identico) ya la transcribe `D2`; separar la doctrina especifica de cada Benchmark de su guion
especifico habria exigido parafrasear contenido que el libro no aisla por su cuenta, con riesgo real de
inventar una version generica que el texto no escribe (`D.30` `15.4`). Se deja declarada, con su cita,
para que una vuelta futura decida si vale la pena.

### G7.4.d. Los tres candidatos, cada uno con su aduana en el acto

**`D1`, `distinguir_tres_tipos_sistemas_negocio`** (`L33` a `L46`, `5` pasos). Salida guardada en
`.gerber_v7/informe_D1.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/informe_D1.txt -->

    ENTRARIAN sin leer nada          : 0
    BLOQUEARIAN esperando veredicto  : 1
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [BLOQUEARIA] distinguir_tres_tipos_sistemas_negocio
        vecino construir_estrategia_gente_cuatro_componentes  [levantada por: similitud_texto]
          similitud_texto 0.399 | familia_id 0.000 | paso_contra_nodo 0.442
          paso 2 del candidato contra paso 1 de construir_estrategia_gente_cuatro_componentes

**`0 CAERIA`. El vecino, leido:** mi paso `2` (*reconoce un Hard System: es algo inanimado*) contra el
paso `1` de `construir_estrategia_gente_cuatro_componentes` (*entiende que tu Your People Strategy es la
forma en que comunicas la idea*): coincidencia lexica del verbo de apertura (*entiende/reconoce que*),
cero coincidencia conceptual (un Hard System no es Your People Strategy). **`SANO`.**

**`D2`, `aplicar_seis_pasos_sistema_venta`** (`L141` a `L154`, `6` pasos). Salida guardada en
`.gerber_v7/informe_D2.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/informe_D2.txt -->

    ENTRARIAN sin leer nada          : 0
    BLOQUEARIAN esperando veredicto  : 1
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [BLOQUEARIA] aplicar_seis_pasos_sistema_venta
        vecino distinguir_tres_tipos_sistemas_negocio  [levantada por: similitud_texto]
          similitud_texto 0.396 | familia_id 0.111 | paso_contra_nodo 0.394
          paso 2 del candidato contra paso 3 de distinguir_tres_tipos_sistemas_negocio

**`0 CAERIA`. El vecino, leido:** mi paso `2` (*escribe literalmente, como el guion de una obra de
teatro, las palabras...*) contra el paso `3` de `D1` (*reconoce un Soft System: (...) como tu mismo o el
guion de una obra de teatro*): comparten la imagen del *guion de una obra de teatro* porque el propio
libro la reusa entre `L39` (Hamlet) y `L145`, no porque sean el mismo procedimiento: uno define que es
un Soft System, el otro manda escribir tu propio guion de venta. **`SANO`.**

**`D3`, `medir_sistema_venta_trece_indicadores_benchmark`** (`L307` a `L338`, `14` pasos). Salida
guardada en `.gerber_v7/informe_D3.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/informe_D3.txt -->

    ENTRARIAN sin leer nada          : 0
    BLOQUEARIAN esperando veredicto  : 1
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [BLOQUEARIA] medir_sistema_venta_trece_indicadores_benchmark
        vecino aplicar_seis_pasos_sistema_venta  [levantada por: similitud_texto]
          similitud_texto 0.353 | familia_id 0.222 | paso_contra_nodo 0.455
          paso 14 del candidato contra paso 5 de aplicar_seis_pasos_sistema_venta
        vecino distinguir_tres_tipos_sistemas_negocio  [levantada por: similitud_texto]
          similitud_texto 0.446 | familia_id 0.100 | paso_contra_nodo 0.378
          paso 14 del candidato contra paso 5 de distinguir_tres_tipos_sistemas_negocio

**`0 CAERIA`. LOS DOS VECINOS, LEIDOS, Y EL SEGUNDO PRIMERO PORQUE PASA DE `0,4`** (seccion `11`: *si una
señal 1 pasa de 0,4, lee ese par antes que ningun otro*, banda donde el catalogo entero solo tenia
gemelos reales). Las dos frases completas, una al lado de la otra:

- mi paso `14`: *Anota esta informacion en un formulario, ya sea a mano o como base de datos en tu
  computador.*
- paso `5` de `distinguir_tres_tipos_sistemas_negocio`: *Ten presente que la Innovacion, la
  Cuantificacion y la Orquestacion de estos tres tipos de sistemas en tu negocio es de lo que trata tu
  Business Development Program.*

**CERO PALABRAS DE CONTENIDO COMPARTIDAS mas alla de articulos y preposiciones: un tema es donde se
anota la informacion, el otro es que integra el BDP.** Es el primer caso que este frente mide por
encima de `0,4` sin ser gemelo (`docs/CALIBRACION_D4.md` media `0` ajenos sobre `3.169` nodos
auditados en el catalogo de la otra casa; esta vuelta suma uno mas al denominador con frases muy
cortas, que es donde la similitud de texto pierde precision con menos palabras para promediar). **`SANO`, y declarado con su
razon completa por si la relectura ciega lo quiere repasar primero.** El segundo par (`aplicar_seis_pasos_sistema_venta`
paso `5`, *entrega cada guion de forma identica a traves de tus vendedores*, contra este mismo paso `14`)
tampoco comparte contenido: **`SANO`.**

**`cap_19` cierra con TRES candidatos, `0 CAERIA` en las tres aduanas, `25` pasos escritos entre los
tres, `25` TRANSCRIPCION y `0` PUENTE.** Cero inserciones al grafo.

**LA VUELTA CIERRA CON DOS CAPITULOS MINADOS, `6` CANDIDATOS EN TOTAL (`3` DE `cap_18` MAS `3` DE
`cap_19`), MUY POR DEBAJO DEL TECHO DE `30`, Y `0 CAERIA` EN LAS SEIS ADUANAS.**

### G7.4.e. Cuanto queda de `d111`, medido y sin decidir

`d111` (vuelta `5`) pidio medir, al cerrar `cap_18` y `cap_19`, cuanto le queda a la cabeza de serie
`recorrer_siete_pasos_programa_desarrollo_negocio` (`cap_13`), sin decidir que se hace con ella.

| paso de la serie | capitulo | que dio |
|---:|---|---|
| `1`, Primary Aim | `cap_14` | metodo dentro del paso (`responder_8_preguntas_construir_primary_aim`), no cabeza |
| `2`, Strategic Objective | `cap_15` | metodo dentro del paso (`responder_4_preguntas_estandares_objetivo_estrategico`), no cabeza |
| `3`, Organizational Strategy | `cap_16` | cero candidatos |
| `4`, Management Strategy | `cap_17` | cero candidatos |
| `5`, People Strategy | `cap_18` | **metodo dentro del paso** (`construir_estrategia_gente_cuatro_componentes`, `aplicar_ocho_reglas_juego_personas`, `aplicar_cinco_pasos_proceso_contratacion`), **no cabeza** |
| `6`, Marketing Strategy | apartado, `fuentes/gerber_emyth_cap17_reservado` | no se toca nunca (`D.45` de esta vuelta, decision del fundador) |
| `7`, Systems Strategy | `cap_19` | **metodo dentro del paso** (`distinguir_tres_tipos_sistemas_negocio`, `aplicar_seis_pasos_sistema_venta`, `medir_sistema_venta_trece_indicadores_benchmark`), **no cabeza** |

**LOS SEIS PASOS ALCANZABLES DE LA SERIE ESTAN MINADOS (EL SEPTIMO, EL `6`, QUEDA APARTADO PARA
SIEMPRE), Y LA CABEZA SIGUE EN `0` DE `7`.** Ninguno de los seis capitulos produjo un nodo que
represente el paso ENTERO (una cabeza propia de *Your Primary Aim*, de *Your People Strategy*, etc.):
los cuatro que dieron candidatos dieron METODO dentro del paso (herramientas y listas que ese capitulo
transcribe), no un nodo que se llame a si mismo el paso. **No decido que se hace con esa cabeza en `0`
de `7`**, tal como el encargo lo pide: queda medido y a la espera de la vuelta que inserte.
