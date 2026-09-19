# APERTURA CIEGA DE LA VUELTA 45, lote 7 (`grove_high_output`), bandeja de `cap_02` y `cap_03`

**Auditor de la linea `serial`, rama `extraccion-mundo-11`.** Escrita ANTES de ver
`docs/loop/REPORTE.md`, que no esta en el arbol. **La vuelta que vengo a auditar es la
`44`, la primera de saneamiento de esta linea.**

---

## 0. LAS DOS DECLARACIONES QUE EL ARNES EXIGE

    ACTA ANTERIOR LEIDA: 1d393837d9ead4208bcf20c36afa395e812b4818
    HEREDADO 1: CUMPLIDO

**`HEREDADO 1` es mi propia `TAREA BLOQUEANTE` de la `ACTA 42`, y tiene tres puntos. Los
tres se cumplen en esta pagina:**

- **`1`. Ninguna frase de esta pagina dice que algo `esta corriendo` ni que `quedo
  corriendo`.** Lo que corri va con su salida pegada; lo que no corri lleva la palabra
  **`NO LO CORRI`** o **`NO TERMINO`** y el motivo detras. **La seccion `9` es exactamente
  eso**, y la seccion `10` pega el barrido que lo comprueba.
- **`2`. Toda cifra de coste o de duracion de esta pagina lleva `MEDIDO` o `PROYECTADO`.**
  Estan en la seccion `9.1`, y la proyeccion **no** lleva `medidos` al lado.
- **`3`. El barrido de mis propias afirmaciones de corrida esta CORRIDO sobre esta misma
  pagina y su salida va pegada en la seccion `10`, sea cero o no sea cero.**

---

## 1. LO QUE NO HE ABIERTO, Y POR QUE

`docs/loop/REPORTE.md`, `docs/loop/loop.log`, `docs/loop/ultimo_extractor.json` y
`docs/loop/ultimo_auditor.json` **no estan en el arbol y no los he recuperado de git.**

**Y hay un quinto que tampoco he abierto, y ese SI esta en el arbol:**
`docs/loop/archivo/grove_high_output/REPORTE.md`. Es el reporte del frente `grove` ya
cosechado, **y su material es exactamente el que vengo a clasificar a ciegas**: los `22`
candidatos de esta bandeja los escribio ese frente. **Leerlo seria leer la lectura que
vengo a comparar con la mia**, asi que **NO LO LEI**. Mido su tamanio, que no es leerlo:

    $ wc -c docs/loop/archivo/grove_high_output/*
     73865 docs/loop/archivo/grove_high_output/ACTA_AUDITOR.md
      4847 docs/loop/archivo/grove_high_output/loop.log
    118685 docs/loop/archivo/grove_high_output/REPORTE.md
    197397 total

**Lo que SI he abierto, y el manual lo dice en voz alta** (`AUDITOR_FORJA.md` 1, recuadro
*"Y SI, PUEDES ABRIR `docs/loop/ACTA_AUDITOR.md` EN LA FASE CIEGA"*): mi propia
`ACTA_AUDITOR.md` de esta linea, para saber que me encargue a mi mismo.

    $ wc -l docs/loop/ACTA_AUDITOR.md
    33679 docs/loop/ACTA_AUDITOR.md

---

## 2. LOS INSTRUMENTOS QUE CORRI, CON SU SALIDA PEGADA (`D.38.3`)

### 2.1. El gate y las dos guardas de estilo e identidad

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python forja.py resolutor
    nodos vivos: 346
    nodos deprecados (archivo): 0
    alias registrados: 0

### 2.2. El estado del arbol

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1087 total

    $ git log --format="%h %ad %s" --date=format:"%Y-%m-%d %H:%M:%S" -3
    98911d1 2026-09-18 21:21:51 La cifra de turno de FF.5.f corregida sin borrar la intermedia: 1663 s r
    de12cdb 2026-09-18 21:20:30 VUELTA 44, LA PRIMERA DE SANEAMIENTO DE ESTA LINEA: seis deudas pagadas
    ebc5c89 2026-09-18 20:53:51 Pendiente de la vuelta 43 recogido antes de abrir la 44: tablero, log, s

### 2.3. El tablero y la deuda

    $ python forja.py tablero --puedo grove_high_output
    LINEA 'serial', LIBRO 'grove_high_output': SI
      'grove_high_output' esta COSECHADO y sin dueño: su trabajo ya llego a esta rama, asi que se continua desde el capitulo siguiente al ultimo minado (cap_03), citando su frontera. D.50.

    $ python scripts/deuda.py
    DEUDA DE LA LINEA (D.55): la deuda no bloquea la produccion
      registro: docs/loop/DEUDA.jsonl
      pendientes: 6    pagadas: 6

      id     vuelta  especie            que
      --------------------------------------------------------------------------------------------
      d005   grove v2 relevo de grove    De los 15 candidatos de cap_03 de grove, su aduana e
      d006   41      relectura          cap_13 entero esta en 4 de 212, el 1,89 por ciento,
      d007   41      doctrina           La cola de doctrina queda congelada en 11 preguntas
      d009   42      deuda              scripts/tabla_de_cierre.py mide la tabla de cierre c
      d011   43      deuda              TODO TECHO QUE EL AUDITOR ESCRIBA LLEVA SU MITAD EN
      d012   43      deuda              SEGUNDO EJEMPLAR MEDIDO de la pregunta 9 de la cola

      ultima vuelta de saneamiento: 44

**`LECTURA` (`D.38.3`, la frase es la del instrumento):** el instrumento midio **`6`
pendientes y `6` pagadas**. Mi conclusion sobre contenido, que va aparte y marcada: **las
`6` pagadas son `d001`, `d002`, `d003`, `d004`, `d008` y `d010`**, y **`d003` la verifico
yo en la seccion `8.1` contra el libro, porque es la unica de las seis que toca el texto de
un candidato de esta bandeja.**

### 2.4. LA CIFRA QUE EL INSTRUMENTO DA Y QUE NO ME CREO: EL CREDITO

    $ python forja.py credito
    CREDITO DE LA LINEA 'serial' (D.48)
      registro: docs/loop/CREDITO_serial.jsonl

      LINEA SIN REGISTRO: no hay ningun suceso escrito.
      Una linea sin tandas NACE CON SU RACHA EN CERO y no hereda
      la de nadie (D.48). Lo que herede el arnes sera CERO remedios.

**`LECTURA`, y esta la levanto yo:** el instrumento dice `LINEA SIN REGISTRO`. **No es que
la linea no tenga registro: es que el fichero no esta en el arbol.**

    $ git status --porcelain docs/loop/
     D docs/loop/APERTURA_CIEGA.md
     D docs/loop/CREDITO_serial.jsonl
     D docs/loop/REPORTE.md
     D docs/loop/loop.log
     M docs/loop/ultimo_apertura.json
     D docs/loop/ultimo_auditor.json
     D docs/loop/ultimo_extractor.json

    $ git ls-tree --name-only -r HEAD -- docs/loop/ | grep CREDITO
    docs/loop/CREDITO_serial.jsonl

**`docs/loop/CREDITO_serial.jsonl` esta en `HEAD` y NO esta en el arbol.** `D.34.2` retira
**cuatro** ficheros y el aviso del arnes nombra **esos cuatro**. **Este es un quinto, y
nadie lo declaro.** No lo recupero, porque recuperar nada en esta fase invalida mi
apertura.

**Lo que esto cuesta, dicho ahora:** mi `ACTA 42` dejo `AUDITOR` en **`2 de 3`** y
`REPORTE` en **`1 de 3`**, y el instrumento que sirve para no tener que fiarse de mi
memoria **contesta `CERO` a las dos.** **Si la vuelta 45 se fia del instrumento en vez del
acta, mi racha se reinicia sola**, y `5.4` dice que una racha no se reinicia sola y que
**un auditor que pone su propia racha a cero se esta absolviendo.** Queda escrito antes de
ver el reporte, para que no parezca hallado despues.

---

## 3. EL MATERIAL: CENSO DE LA BANDEJA, CONTADO CON INSTRUMENTO

    $ ls cuarentena/grove_high_output/*.json | wc -l
    22

    $ python -c "censo de bandeja: capitulo de origen, pasos y aristas, candidato a candidato"
    cap_02  clasificar_trabajo_proceso_montaje_prueba        pasos= 7 aristas=0
    cap_02  construir_flujo_produccion_paso_limitante        pasos=10 aristas=0
    cap_02  detectar_arreglar_fallo_etapa_menor_valor        pasos= 6 aristas=0
    cap_02  dimensionar_inventario_materia_prima_reposicion  pasos= 7 aristas=0
    cap_02  equilibrar_capacidad_personal_inventario_plazo   pasos= 8 aristas=0
    cap_02  preferir_inspeccion_proceso_prueba_destructiva   pasos= 6 aristas=0
    cap_02  rehacer_flujo_paso_limitante_capacidad           pasos= 6 aristas=0
    cap_03  archivar_indicadores_resolver_problemas          pasos= 4 aristas=0
    cap_03  casar_flujo_fabricacion_flujo_ventas             pasos=12 aristas=0
    cap_03  construir_grafico_escalonado_pronosticos         pasos= 8 aristas=0
    cap_03  construir_indicador_linealidad_alerta_temprana   pasos= 9 aristas=0
    cap_03  construir_indicador_tendencia_patron             pasos= 6 aristas=0
    cap_03  decidir_aceptar_rechazar_material_defectuoso     pasos= 8 aristas=0
    cap_03  dimensionar_plantilla_administrativa_pronostico  pasos= 7 aristas=0
    cap_03  elegir_cinco_indicadores_diarios_fabrica         pasos=10 aristas=0
    cap_03  elegir_fabricar_pedido_pronostico                pasos= 9 aristas=0
    cap_03  elegir_indicador_salida_trabajo_administrativo   pasos= 7 aristas=0
    cap_03  elegir_inspeccion_barrera_monitorizacion         pasos=12 aristas=0
    cap_03  emparejar_indicadores_efecto_contraefecto        pasos= 7 aristas=0
    cap_03  representar_actividad_caja_negra_ventanas        pasos= 9 aristas=0
    cap_03  simplificar_trabajo_reducir_numero_pasos         pasos= 7 aristas=0
    cap_03  variar_frecuencia_inspeccion_nivel_calidad       pasos= 6 aristas=0
    candidatos=22  pasos_totales=171
    por capitulo: {'cap_02': 7, 'cap_03': 15}

    $ python -c "nodos de grove en el grafo"
      revisar_tres_preguntas_valor_carrera | cap_01 | pasos 7
    nodos grove en grafo: 1  nodos totales: 346

    $ wc -l fuentes/grove_high_output/cap_02.md fuentes/grove_high_output/cap_03.md
    119 fuentes/grove_high_output/cap_02.md
    179 fuentes/grove_high_output/cap_03.md

    $ wc -w fuentes/grove_high_output/cap_02.md fuentes/grove_high_output/cap_03.md
     3427 fuentes/grove_high_output/cap_02.md
     5855 fuentes/grove_high_output/cap_03.md
     9282 total

**`LECTURA`:** la bandeja es **`7` de `cap_02` mas `15` de `cap_03`**, y en el grafo vive
**`1`** nodo de este libro, el de `cap_01`. **Los `15` de `cap_03` son los mismos `15` que
la deuda `d005` nombra**, y los `7` de `cap_02` **no estan en ninguna deuda**.

---

## 4. MI CLASIFICACION, CANDIDATO A CANDIDATO Y A CIEGAS

**Lei los dos capitulos enteros antes de abrir un solo candidato**, y despues cada
candidato contra su tramo. La columna **`tramo que yo leo`** la escribi **antes** de
extraer la que cada ficha declara, y la comparacion de las dos esta en la seccion `4.2`.

**`cap_02` es el capitulo `1` del libro** (*The Basics of Production*) y **`cap_03` es el
capitulo `2`** (*Managing the Breakfast Factory*). Los dos van en `fidelidad: verbatim`.

### 4.1. Las veintidos filas

| # | candidato | cap | tramo que yo leo | es procedimiento | mi clase |
|---|---|---|---|---|---|
| 1 | `construir_flujo_produccion_paso_limitante` | 02 | L17 a L27 | **SI**: fija el paso limitante y escalona hacia atras | **SANO**, cabeza de la serie de flujo |
| 2 | `rehacer_flujo_paso_limitante_capacidad` | 02 | L51 a L55 | **SI**: busca la cola, declara paso limitante nuevo, rehace | **SANO con ARISTA** (ver `5.1`) |
| 3 | `equilibrar_capacidad_personal_inventario_plazo` | 02 | L57 a L61 | **SI**: nombra las cuatro salidas, apunta su coste, intercambia | **SANO** |
| 4 | `clasificar_trabajo_proceso_montaje_prueba` | 02 | L37 a L45 | **SI**: senala proceso, montaje y prueba en tu propio trabajo | **SANO**, cabeza de la serie de prueba |
| 5 | `preferir_inspeccion_proceso_prueba_destructiva` | 02 | L67 | **SI**: elige inspeccion en proceso sobre prueba destructiva | **SANO con ARISTA** (ver `5.1`) |
| 6 | `dimensionar_inventario_materia_prima_reposicion` | 02 | L69 | **SI**: inspeccion de recepcion y dimensionado por tiempo de reposicion | **SANO** |
| 7 | `detectar_arreglar_fallo_etapa_menor_valor` | 02 | L73 a L75 | **SI**: ordena etapas por valor y corrige en la de menor valor | **SANO**, principio que otros tres citan |
| 8 | `elegir_cinco_indicadores_diarios_fabrica` | 03 | L15 a L29 | **SI**: los cinco datos, uno a uno, y el repaso de primera hora | **SANO** |
| 9 | `emparejar_indicadores_efecto_contraefecto` | 03 | L31 a L33 | **SI**: nombra efecto y contraefecto y los mide juntos | **SANO**, con un discutible de fidelidad (`8.3`) |
| 10 | `elegir_indicador_salida_trabajo_administrativo` | 03 | L35 a L67 | **SI**: las dos varas mas la tabla de seis funciones | **SANO con ARISTA** hacia el `9` |
| 11 | `representar_actividad_caja_negra_ventanas` | 03 | L73 a L79 | **SI**: nombra entrada, salida y trabajo, y recorta ventanas | **SANO**, cabeza de la serie de ventanas |
| 12 | `construir_indicador_linealidad_alerta_temprana` | 03 | L83 a L87 | **SI**: recta ideal, lo conseguido, lectura a media carrera | **SANO con ARISTA** hacia el `11` |
| 13 | `construir_indicador_tendencia_patron` | 03 | L89 | **SI**: salida contra tiempo y contra patron | **SANO con ARISTA** hacia el `11` |
| 14 | `construir_grafico_escalonado_pronosticos` | 03 | L91 a L97 | **SI**: monta, actualiza cada mes, lee la variacion | **SANO con ARISTA** hacia el `13` |
| 15 | `archivar_indicadores_resolver_problemas` | 03 | L99 | **SI**: recoge, archiva, repasa cuando algo falle | **SANO**, el mas corto de la bandeja con `4` pasos |
| 16 | `elegir_fabricar_pedido_pronostico` | 03 | L103 a L109 | **SI**: la eleccion entre las dos vias y el riesgo de inventario | **SANO**, cabeza de la serie de pronostico |
| 17 | `casar_flujo_fabricacion_flujo_ventas` | 03 | L111 a L121 | **SI**: los dos flujos, los dos pronosticos, la holgura | **SANO con ARISTA** hacia el `16` |
| 18 | `dimensionar_plantilla_administrativa_pronostico` | 03 | L123 a L125 | **SI**: patrones de hecho y plantilla contra pronostico | **SANO con ARISTA** hacia el `10` |
| 19 | `decidir_aceptar_rechazar_material_defectuoso` | 03 | L135 a L137 | **SI**: las dos salidas, el grupo equilibrado, el limite de fiabilidad | **SANO con ARISTA** hacia el `6` |
| 20 | `elegir_inspeccion_barrera_monitorizacion` | 03 | L139 a L141 | **SI**: barrera contra monitorizacion, con su intercambio | **SANO**, cabeza de la serie de inspeccion de `cap_03` |
| 21 | `variar_frecuencia_inspeccion_nivel_calidad` | 03 | L143 | **SI**: sube y baja la frecuencia segun vaya la calidad | **SANO**, hermana del `20` (ver `5.2`) |
| 22 | `simplificar_trabajo_reducir_numero_pasos` | 03 | L169 a L171 | **SI**: dibuja, cuenta, fija meta, pregunta y tira | **SANO** |

**`LECTURA`: los veintidos traen procedimiento propio y ninguno es gemelo de otro.** No leo
ni un `REPITE` en la bandeja. Lo que si leo son **nueve relaciones madre a hijo**, y van en
la seccion `5`.

### 4.2. MI TRAMO CONTRA EL QUE CADA FICHA DECLARA: COINCIDEN LOS VEINTIDOS

    $ python -c "la PIEZA y el tramo L que cada ficha declara en su resumen_teorico"
    archivar_indicadores_resolver_problemas          cap_03  P12 L99 a L99
    casar_flujo_fabricacion_flujo_ventas             cap_03  P14 L111 a L121
    clasificar_trabajo_proceso_montaje_prueba        cap_02  P5 L37 a L47
    construir_flujo_produccion_paso_limitante        cap_02  P2 L15 a L27
    construir_grafico_escalonado_pronosticos         cap_03  P11 L91 a L97
    construir_indicador_linealidad_alerta_temprana   cap_03  P9 L83 a L87
    construir_indicador_tendencia_patron             cap_03  P10 L89 a L89
    decidir_aceptar_rechazar_material_defectuoso     cap_03  P17 L135 a L137
    detectar_arreglar_fallo_etapa_menor_valor        cap_02  P11 L71 a L75
    dimensionar_inventario_materia_prima_reposicion  cap_02  P10 L69
    dimensionar_plantilla_administrativa_pronostico  cap_03  P15 L123 a L125
    elegir_cinco_indicadores_diarios_fabrica         cap_03  P2 L15 a L29
    elegir_fabricar_pedido_pronostico                cap_03  P13 L101 a L109
    elegir_inspeccion_barrera_monitorizacion         cap_03  P18 L139 a L141
    emparejar_indicadores_efecto_contraefecto        cap_03  P3 L31 a L33
    equilibrar_capacidad_personal_inventario_plazo   cap_02  P7 L57 a L61
    preferir_inspeccion_proceso_prueba_destructiva   cap_02  P9 L67
    rehacer_flujo_paso_limitante_capacidad           cap_02  P6 L49 a L55
    representar_actividad_caja_negra_ventanas        cap_03  P7 L71 a L79
    simplificar_trabajo_reducir_numero_pasos         cap_03  P23 L169 a L173
    variar_frecuencia_inspeccion_nivel_calidad       cap_03  P19 L143 a L145

*(`elegir_indicador_salida_trabajo_administrativo` no sale en esa lista por una errata mia
de expresion de busqueda, y esta corregida al final de esta seccion: declara `PIEZAS P4 y
P5, L35 a L37 y la tabla de L39 a L67`, que es exactamente mi tramo.)*

**`LECTURA`: mi tramo y el suyo coinciden en los veintidos, y las unicas diferencias son
los renglones de rotulo y de cierre de los bordes**, que yo no cuento porque lei prosa:

| candidato | lo que yo dejo fuera y ellos meten | que es ese renglon |
|---|---|---|
| `construir_flujo_produccion_paso_limitante` | `L15` | `The Three-Minute Egg`, rotulo |
| `rehacer_flujo_paso_limitante_capacidad` | `L49` | `A Few Complications`, rotulo |
| `clasificar_trabajo_proceso_montaje_prueba` | `L47` | el renglon que resume las cuatro aplicaciones |
| `detectar_arreglar_fallo_etapa_menor_valor` | `L71` | `Adding Value`, rotulo |
| `representar_actividad_caja_negra_ventanas` | `L71` | `The Black Box`, rotulo |
| `elegir_fabricar_pedido_pronostico` | `L101` | `Controlling Future Output`, rotulo |
| `variar_frecuencia_inspeccion_nivel_calidad` | `L145` | el renglon que cierra el apartado |
| `simplificar_trabajo_reducir_numero_pasos` | `L173` | el renglon del *hardly new* y las profesiones blandas |
| `construir_indicador_linealidad_alerta_temprana` | **al reves: yo meti `L81` y ellos no** | los indicadores adelantados y su credibilidad |

**Y UNA CIFRA MIA QUE CORREGI ANTES DE PUBLICARLA, porque casi la publico falsa.** Mi
primer barrido dijo que **`1` de `22` fichas no declaraba pieza ni tramo**
(`elegir_indicador_salida_trabajo_administrativo`). **Era falso: mi propia expresion de
busqueda solo casaba `PIEZA` en singular, y esa ficha declara `PIEZAS P4 y P5`.** Corrijo
sin borrar y pego el instrumento corregido:

    $ python -c "PIEZA/PIEZAS y tramo L declarados, expresion corregida"
    fichas que declaran PIEZA y tramo L: 22 de 22   (sin declarar: 0)

**Lo digo porque es exactamente mi especie**: una cifra propia falsa sacada de un
instrumento bien corrido con la pregunta mal escrita. **La cazo yo y la escribo yo.**

---

## 5. LAS NUEVE RELACIONES MADRE A HIJO QUE LEO, Y LA CLASE QUE LES PONGO

### 5.1. DOS DE ELLAS YA ESTAN ADJUDICADAS DENTRO DE LA FICHA, Y MI PRIMERA LECTURA FUE LA CONTRARIA

**Lo escribo en el orden en que paso, que es lo unico que lo hace comprobable.**

**Lei los pasos primero y adjudique `CONTINUA`** para los dos pares siguientes, con este
razonamiento mio: el hijo toma el procedimiento de la madre y lo sigue.

    par 1   madre construir_flujo_produccion_paso_limitante  ->  hijo rehacer_flujo_paso_limitante_capacidad
    par 2   madre clasificar_trabajo_proceso_montaje_prueba  ->  hijo preferir_inspeccion_proceso_prueba_destructiva

**Despues abri el `resumen_teorico` de las cuatro fichas**, que es material que esta fase
me manda abrir, **y encontre dentro una correccion declarada de la vuelta `44`**:

    $ git show --word-diff=plain de12cdb -- cuarentena/grove_high_output/construir_flujo_produccion_paso_limitante.json
    {+... CORRECCION DECLARADA de la vuelta 44 de la linea serial (deuda d004, cita grove
    PARA_ALEXIS 5.3.4, resuelta por D.53 del 17 sep 2026) ... LA ACTA 32 seccion 3.3 del
    frente grove adjudico CONTINUA este par por la lectura vieja de que un par con arista
    declarada no puede ser SANO. D.53 decide lo contrario con su prueba por reduccion: UN
    SANO PUEDE LLEVAR ARISTA DECLARADA, Y DECLARARLA NO LO CONVIERTE EN CONTINUA, porque si
    lo hiciera D.37 seria imposible y toda cabeza de serie devoraria sus partes. ... LA
    ARISTA SIGUE EN PIE Y SE CABLEA AL INSERTAR: madre construir_flujo_produccion_paso_limitante
    paso 9, hijo rehacer_flujo_paso_limitante_capacidad. No se borra nada: la clase CONTINUA
    de la ACTA 32 queda escrita donde esta.+}

**Fui entonces al banco y lei `D.53` entera** (`docs/BANCO_DE_REGLAS.md` linea `2982`):

> **UN `SANO` PUEDE LLEVAR ARISTA DECLARADA, Y DECLARARLA NO LO CONVIERTE EN `CONTINUA`.**
> **El veredicto dice si un par REPITE, CONTINUA o esta SANO en su procedimiento.** **La
> arista dice si hay RELACION DECLARABLE entre los dos.** Son dos preguntas distintas y se
> contestan por separado.

**ADJUDICO: los dos pares son `SANO` con arista declarada, y mi primera lectura estaba
equivocada.** El hijo no sigue el procedimiento de la madre: **trae uno propio**.
`rehacer_flujo` comprueba si el flujo supone capacidad infinita, busca donde hay cola,
cuenta el tiempo de espera dentro del flujo y declara un paso limitante nuevo, **que son
cuatro cosas que `construir_flujo` no hace**; `preferir_inspeccion` elige entre prueba
destructiva e inspeccion en proceso, **que es una eleccion que `clasificar_trabajo` nombra
pero no resuelve**. **Sin `D.53` yo habria fundido cuatro procedimientos en dos.**

**No me absuelve y lo digo: mi lectura ciega de estos dos pares fue la vieja**, y lo que la
corrigio fue una regla escrita el `17 sep` que yo tenia disponible y no consulte antes de
clasificar. **Queda escrito antes de ver el reporte.**

### 5.2. LAS OTRAS SIETE LAS LEVANTO YO, Y NINGUNA FICHA LAS DECLARA

    $ python -c "aristas: campos frente a prosa"
    aristas en los campos nodos_previos/nodos_siguientes de los 22: 0
    candidatos cuyo resumen_teorico contiene la palabra ARISTA      : 6
       - casar_flujo_fabricacion_flujo_ventas
       - clasificar_trabajo_proceso_montaje_prueba
       - construir_flujo_produccion_paso_limitante
       - dimensionar_plantilla_administrativa_pronostico
       - preferir_inspeccion_proceso_prueba_destructiva
       - rehacer_flujo_paso_limitante_capacidad

**`LECTURA`:** de los `22`, **`0` traen arista en el campo** y **`6` la nombran en prosa**.
De esos `6`, **`4` son los del par `1` y el par `2`** de arriba, y **`2` mas
(`casar_flujo_fabricacion_flujo_ventas` y `dimensionar_plantilla_administrativa_pronostico`)
prometen la arista "en el reporte de esta vuelta"**, y **esa vuelta es la del frente `grove`
ya cosechado**, cuyo reporte esta archivado y yo no he abierto. **Nadie de esta linea las ha
cableado, y la promesa apunta a una sede que esta vuelta no lee.**

**Las siete que leo yo, con la madre, el paso de la madre que nombra al hijo, y la linea del
libro que lo sostiene:**

| # | madre | paso | hijo | linea del libro |
|---|---|---|---|---|
| 3 | `representar_actividad_caja_negra_ventanas` | 8 | `construir_indicador_linealidad_alerta_temprana` | `cap_03` L83: el indicador de linealidad es *"a generally applicable example of a 'window' cut into the black box"* |
| 4 | `representar_actividad_caja_negra_ventanas` | 8 | `construir_indicador_tendencia_patron` | `cap_03` L89: *"This extrapolation gives us another window in our black box"* |
| 5 | `construir_indicador_tendencia_patron` | 5 | `construir_grafico_escalonado_pronosticos` | `cap_03` L91: el grafico escalonado anticipa *"better than if you used a simple trend chart"* |
| 6 | `elegir_fabricar_pedido_pronostico` | 4 | `casar_flujo_fabricacion_flujo_ventas` | `cap_03` L111: *"Delivering a product that was built to forecast to a customer consists of two simultaneous processes"* |
| 7 | `elegir_indicador_salida_trabajo_administrativo` | 5 | `emparejar_indicadores_efecto_contraefecto` | `cap_03` L37: los de la tabla son de cantidad, *"their paired counterparts should stress the quality of work"* |
| 8 | `elegir_indicador_salida_trabajo_administrativo` | 2 | `dimensionar_plantilla_administrativa_pronostico` | `cap_03` L125: *"if we have carefully chosen indicators ... we are ready to apply the methods of factory control to administrative work"* |
| 9 | `dimensionar_inventario_materia_prima_reposicion` | 1 | `decidir_aceptar_rechazar_material_defectuoso` | `cap_03` L135: *"When material is rejected at incoming inspection, a couple of choices present themselves"* |

**Y una decima que leo y NO declaro como arista, con su motivo:**
`elegir_inspeccion_barrera_monitorizacion` **a** `variar_frecuencia_inspeccion_nivel_calidad`.
`cap_03` L143 abre con *"Another way to lower the cost of quality assurance"*, **que remite
al apartado y no a un paso nombrado de la madre**, y `D.37` pide que el texto **diga cuantas
partes tiene y las nombre**. **No las nombra: son hermanas bajo un mismo rotulo, y eso es
frontera declarada, no arista.** Lo dejo escrito para que el turno normal lo adjudique con
el reporte delante.

**Las nueve son `SANO` con arista, ninguna es `CONTINUA` y ninguna es `REPITE`** (`D.53`).

---

## 6. LO QUE LOS DOS CAPITULOS TIENEN Y NINGUN CANDIDATO RECOGE

**Esta es la mitad que un barrido de vecinos no encuentra nunca**, porque el barrido busca
lo que sobra y esto es lo que falta. Recorri los dos capitulos renglon a renglon contra la
tabla de tramos de `4.2`.

| tramo sin candidato | que dice el libro ahi | por que pesa |
|---|---|---|
| `cap_03` **L159 a L167** | la definicion de **productividad** (salida dividida por el trabajo), **las dos maneras de subirla** (mas rapido, o cambiando que se hace) y el concepto de **`leverage`** con sus cuatro ejemplares | **es el concepto que da nombre al libro** y el antecedente directo de `simplificar_trabajo`, cuyo `L169` abre diciendo *"Automation is certainly one way to improve the leverage of all types of work"* |
| `cap_03` **L145 a L155** | el ejemplar de la embajada, el muestreo contra el `100` por cien, la comparacion con el `IRS` y **la inspeccion variable aplicada al trabajo del mando** | `L155` dice que eso *"gives us an important tool for improving managerial productivity"*, y ningun paso lo recoge |
| `cap_03` **L129 a L131** | los **tres puntos de inspeccion con su nombre**: `incoming`, `in process` y `final`, y *"reject before investing further value"* | es el inventario que ordena los cuatro candidatos de inspeccion de la bandeja, y **no hay nodo que lo tenga** |
| `cap_03` **L69** | los **tres usos** de los indicadores administrativos: fijan objetivos, dan objetividad y **permiten comparar grupos que hacen lo mismo en sitios distintos** | el libro lo remata anunciando la analogia deportiva de mas adelante |
| `cap_03` **L81** | los indicadores adelantados y **la condicion de creerselos**: *"unless you are prepared to act on what your leading indicators are telling you, all you will get from monitoring them is anxiety"* | es la unica linea del tramo `L81` a `L87` que **ningun paso** de `construir_indicador_linealidad` toca, y es la que pone la condicion de uso |
| `cap_02` **L31 a L35** | la contratacion universitaria como paso limitante caro, y **la entrevista telefonica de criba** para subir la razon de ofertas por visita | es procedimiento con su efecto medido, y solo sobrevive como ejemplo dentro de otro nodo |
| `cap_02` **L63 a L65** | la **operacion continua**: cocedor continuo, casar su salida con la del tostador, y **la flexibilidad que se pierde a cambio** | `L67`, que es el candidato `5`, **empieza preguntando que pasa si esa maquina se descalibra**, asi que el nodo existe y su antecedente no |
| `cap_02` **L77 a L79** | el sistema penal como proceso de produccion, con **el millon de dolares por condena contra los `80.000` de la celda** | es el cierre del capitulo y su ejemplar mas fuerte del principio *"dejar que el paso equivocado limite el proceso"* |

**La comprobacion de la primera fila, con instrumento y no a ojo:**

    $ grep -ril "apalanca\|leverage\|productividad" cuarentena/grove_high_output/
    cuarentena/grove_high_output/simplificar_trabajo_reducir_numero_pasos.json

    $ python -c "donde aparece esa palabra dentro de esa unica ficha"
    titulo no
    condiciones_activacion SI
    entregable_esperado no
    resumen_teorico SI
    denominaciones: {... "otros_idiomas": [... {"idioma": "ingles", "termino": "leverage"}]}
    (ningun paso_accionable la contiene)

    $ grep -o "apalancamiento\|leverage" dataset/nodos.jsonl | sort | uniq -c
    (cero lineas: no aparece en ninguno de los 346 nodos del grafo)

**`LECTURA`:** el instrumento midio que **`leverage` aparece en `1` de `22` fichas y en `0`
de `346` nodos del grafo**, y que **dentro de esa unica ficha no esta en ningun paso**: esta
en `otros_idiomas`, en `condiciones_activacion` y en el resumen. **Mi conclusion, que va
aparte: la bandeja NOMBRA el apalancamiento y no lo PROCEDIMENTA**, que es justo lo que
`P.5.1` no acepta como expansion, **y aqui no hay siquiera un nodo del que expandir.**

---

## 7. EL CAPITULO SIGUIENTE, MEDIDO ANTES DE QUE NADIE PONGA UN TECHO

    $ ls fuentes/grove_high_output/ | wc -l
    18
    $ wc -l fuentes/grove_high_output/cap_04.md
    323 fuentes/grove_high_output/cap_04.md

**`LECTURA`: el material del capitulo siguiente esta en `fuentes/` y la clave esta en la
tabla canonica**, que son las dos condiciones que `D.32` manda medir. `cap_04` tiene `323`
renglones, **casi el doble que `cap_03` y casi el triple que `cap_02`**, y es el mas largo
de los dieciocho. **Lo dejo medido aqui porque la deuda `d011` dice que todo techo que yo
escriba lleva su mitad en minutos**, y un capitulo de `323` renglones no cuesta lo que uno
de `119`.

---

## 8. FIDELIDAD `D.30`: LO QUE RELEI CONTRA EL LIBRO

### 8.1. LA DEUDA `d003`, QUE TOCA EL TEXTO DE UN CANDIDATO: PAGADA Y VERIFICADA

`d003` mandaba *"quitarle la cabeza que el libro no encarga y dejar la transcripcion"* al
paso `6` de `variar_frecuencia_inspeccion_nivel_calidad`. **Esto es lo que la vuelta `44`
cambio:**

    $ git show de12cdb -- cuarentena/grove_high_output/variar_frecuencia_inspeccion_nivel_calidad.json
    -  "Desconfia de tu propia costumbre antes de descartarlo, porque este metodo casi no se usa ni siquiera en la fabricacion corriente, y la razon probable es que somos animales de costumbres y seguimos haciendo las cosas como las hemos hecho siempre, sea de una semana a otra o de un ano a otro."
    +  "Cuenta con que este metodo casi no se usa ni siquiera en la fabricacion corriente, y con que la razon probable es que somos animales de costumbres y seguimos haciendo las cosas como las hemos hecho siempre, sea de una semana a otra o de un ano a otro."

Y esto es lo que el libro dice, `cap_03` `L143`:

> *"Yet this approach is not used very often, even in widget manufacturing. Why not?
> Probably because we are creatures of habit and keep doing things the way we always have,
> whether it be from week to week or year to year."*

**ADJUDICO: `d003` esta bien pagada.** Lo que se quito (*"Desconfia de tu propia costumbre
antes de descartarlo"*) **es una orden que el libro no da**; lo que queda es la
transcripcion. **`TRANSCRIPCION`, no `PUENTE`.**

### 8.2. MUESTRA AL AZAR DE `30` PASOS SOBRE `171`, CON SEMILLA ESCRITA

**No los elegi a ojo** (`AUDITOR_FORJA.md` 7: *elegir a ojo mide lo que el auditor ya
sospecha*). **Semilla `44`, la vuelta que audito.**

    $ python -c "muestra de pasos al azar con semilla 44"
    universo de pasos: 171
    cap_03 | archivar_indicadores_resolver_problemas | paso 3
    cap_03 | casar_flujo_fabricacion_flujo_ventas | paso 4
    cap_02 | clasificar_trabajo_proceso_montaje_prueba | paso 2
    cap_02 | clasificar_trabajo_proceso_montaje_prueba | paso 3
    cap_02 | construir_flujo_produccion_paso_limitante | paso 2
    cap_02 | construir_flujo_produccion_paso_limitante | paso 3
    cap_02 | construir_flujo_produccion_paso_limitante | paso 6
    cap_02 | construir_flujo_produccion_paso_limitante | paso 7
    cap_03 | construir_grafico_escalonado_pronosticos | paso 8
    cap_03 | construir_indicador_linealidad_alerta_temprana | paso 5
    cap_03 | decidir_aceptar_rechazar_material_defectuoso | paso 2
    cap_02 | dimensionar_inventario_materia_prima_reposicion | paso 3
    cap_02 | dimensionar_inventario_materia_prima_reposicion | paso 5
    cap_03 | dimensionar_plantilla_administrativa_pronostico | paso 1
    cap_03 | dimensionar_plantilla_administrativa_pronostico | paso 7
    cap_03 | elegir_cinco_indicadores_diarios_fabrica | paso 3
    cap_03 | elegir_cinco_indicadores_diarios_fabrica | paso 8
    cap_03 | elegir_fabricar_pedido_pronostico | paso 3
    cap_03 | elegir_fabricar_pedido_pronostico | paso 4
    cap_03 | elegir_indicador_salida_trabajo_administrativo | paso 1
    cap_03 | elegir_indicador_salida_trabajo_administrativo | paso 2
    cap_02 | equilibrar_capacidad_personal_inventario_plazo | paso 2
    cap_02 | equilibrar_capacidad_personal_inventario_plazo | paso 3
    cap_02 | equilibrar_capacidad_personal_inventario_plazo | paso 5
    cap_02 | preferir_inspeccion_proceso_prueba_destructiva | paso 2
    cap_02 | rehacer_flujo_paso_limitante_capacidad | paso 3
    cap_03 | representar_actividad_caja_negra_ventanas | paso 3
    cap_03 | representar_actividad_caja_negra_ventanas | paso 8
    cap_03 | simplificar_trabajo_reducir_numero_pasos | paso 7
    cap_03 | variar_frecuencia_inspeccion_nivel_calidad | paso 3

**Los `30` los lei uno a uno contra su renglon del libro. Los `30` salen `TRANSCRIPCION`:
`0` `PUENTE` en la muestra.** Cuatro ejemplares, por si el siguiente lector quiere
rehacerlos:

| paso sorteado | renglon del libro | que dice el libro |
|---|---|---|
| `construir_flujo` p7 | `cap_02` L25 | *"First you must allow time to assemble the items on a tray. Next you must get the toast from the toaster and the coffee from the pot, as well as the egg out of the boiling water."* |
| `dimensionar_inventario` p5 | `cap_02` L69 | *"you should have enough to cover your consumption rate for the length of time it takes to replace your raw material ... if your egg man comes by and delivers once a day, you want to keep a day's worth of inventory on hand"* |
| `dimensionar_plantilla` p7 | `cap_03` L125 | *"the staffing of administrative units would always be left at its highest level and, given Parkinson's famous law, people would find ways to let whatever they're doing fill the time available for its completion"* |
| `linealidad` p5 | `cap_03` L83 | *"the only way we can hit our target is by getting acceptance at a much higher rate in the remaining two months than we had gotten in the preceding four"* |

### 8.3. LOS DOS DISCUTIBLES DE FIDELIDAD QUE LEVANTO YO, FUERA DE LA MUESTRA

**Van aparte de la muestra a proposito**: estos SI los elegi a ojo, releyendo los `171`
pasos buscando la especie *"el nodo afirma algo que el libro no afirma"*. **Meterlos dentro
de la muestra al azar falsearia su tasa.**

**`DISCUTIBLE DE FIDELIDAD 1`, y es el que mas me pesa.**
`clasificar_trabajo_proceso_montaje_prueba` paso `4`:

> *"Prueba cada pieza por separado antes de montarla, **que es lo que el libro llama prueba
> unitaria**, y en un trabajo de personas toma la forma de una presentacion en seco ante un
> grupo escogido."*

El libro llama **`unit test`** a la prueba de las piezas **del compilador** (`cap_02` L45) y
llama **`dry run` presentation** a la prueba **de la formacion de ventas** (`cap_02` L41).
**NO las iguala en ningun renglon.** El paso las iguala y **se lo atribuye al libro**. **Mi
lectura: el contenido es transcripcion y la atribucion no lo es.** No lo firmo como `PUENTE`
sin ver como lo marco el extractor en su propia tabla de fidelidad, **y por eso lo dejo
escrito aqui antes de verla.**

**`DISCUTIBLE DE FIDELIDAD 2`.** `emparejar_indicadores_efecto_contraefecto` pasos `2` y `3`
(*"Nombra el efecto..."*, *"Nombra el contraefecto..."*). `cap_03` L31 dice *"you should
guard against overreacting. This you can do by pairing indicators, so that together both
effect and counter-effect are measured"*. **El libro nombra las dos cosas; no ordena
nombrarlas como dos pasos.** **ADJUDICO `TRANSCRIPCION` por extension natural**, porque
medir las dos juntas exige identificarlas primero, **y dejo escrita la lectura contraria
para que se pueda discutir.**

**Y una tercera cosa que NO es caida y registro igual:** `elegir_cinco_indicadores` paso `9`
convierte el *"Perhaps you should set up a 'customer complaint log'"* de `L27` en un
**`Monta`** sin matiz. **Es modalidad, no contenido**: no lo cargo, lo anoto.

---

## 9. LO QUE NO CORRI Y LO QUE NO TERMINO, CON EL MOTIVO DETRAS

### 9.1. EL BARRIDO DE VECINOS DE `D.38.4` SOBRE LOS `22`: **NO TERMINO**

**Lo lance y no termino dentro de mi turno.** Su mandato vigente
(`docs/BANCO_DE_REGLAS.md` `D.38.4`, correccion declarada del 16 sep) es entregar a la
aduana la poblacion del grafo y dejar que ella ponga las bandejas:

    $ python -u forja.py informe --carpeta cuarentena/grove_high_output
    (lanzado 21:31:00, detenido por mi 21:43:47 sin terminar: 767 s MEDIDOS)
    $ wc -c <fichero de salida del barrido>
    0

**Lo detuve yo antes de cerrar la pagina, y lo digo:** dejarlo para que acabase despues
habria puesto una corrida mia terminando **dentro de mi propia fase sellada**, que es la
figura que mis `ACTA 39` y `ACTA 40` le cobraron al extractor dos vueltas seguidas. **`767
s` MEDIDOS y `0` bytes de salida: el informe imprime al terminar y no termino.**

**Por que tarda, MEDIDO con la propia funcion de la casa:**

    $ python -c "coste de una comparacion de la aduana"
    MEDIDO: 1.197 s por comparacion (media de 20 llamadas a aduana.medir)
    MEDIDO: poblacion del barrido = 346 del grafo + 22 de bandejas
    PROYECTADO: 1 candidato contra 367 = 7.3 min
    PROYECTADO: los 22 candidatos = 161.0 min

**La cifra `1.197` es MEDIDA y las dos de abajo son PROYECTADAS**, y la proyeccion no lleva
la palabra medida al lado. **Aviso sobre la medida: se tomo con el barrido de los `22`
ocupando la maquina, asi que es un techo y no un suelo.**

**LO QUE ESTO SIGNIFICA, Y NO LO ADORNO:** esta apertura **no publica ni una cifra de
vecinos**, ni de pares levantados, ni de `ENTRARIAN` contra `BLOQUEARIAN`. **La
clasificacion de la seccion `4` y las nueve relaciones de la `5` salen de leer los dos
capitulos y los `22` candidatos, no de un barrido**, y van escritas como lecturas con su
renglon al lado. **La deuda `d005` dice que el frente `grove` midio `9 ENTRARIAN` y `6
BLOQUEARIAN` sobre los `15` de `cap_03`: NO reproduje esa cifra y NO la cito como propia.**

**Esto es el remedio de mi `ACTA 42` funcionando.** Aquella apertura **afirmo dos veces un
barrido de los `22` que nunca corrio**, y le colgo una duracion inventada. Esta dice que lo
lanzo, que no termino, cuanto cuesta y que no publica su cifra. **Prefiero una pagina sin
esa cifra a una pagina con esa cifra inventada.**

### 9.2. `tests/test_aceptacion.py`: **NO LO CORRI**

**Motivo:** el barrido de la `9.1` tenia la maquina ocupada y la suite toma el cerrojo del
dataset, que es justo lo que la `9.3` esta midiendo; correrla habria mezclado las dos
medidas. **Queda encargado para mi turno normal.**

### 9.3. EL CERROJO: EXISTE, ES HUERFANO, Y **NO** ESTA EN ROJO

    $ ls -la procesos/
    -rw-r--r-- 1 AlexDesk 197609 43 Sep 18 19:49 nodos.jsonl.679b2259.cerrojo
    -rw-r--r-- 1 AlexDesk 197609 42 Sep 18 21:18 nodos.jsonl.e52fd5d2.cerrojo

    $ python -c "el cerrojo de este arbol, con el instrumento de la casa"
    ruta      : procesos\nodos.jsonl.679b2259.cerrojo
    pid       : 30764
    desde     : 1789775347.2028258 -> 2026-09-18 19:49:07
    ahora     : 2026-09-18 21:30:55
    antiguedad: 6108 s
    cerrojo._vive(pid): None

    $ python -c "edad contra tope"
    edad 6125 s   TOPE_DE_HUERFANO 900 s   edad>tope: True
    vivo: None (None = no se puede comprobar en este sistema)
    se rompe y se declara: True

**`LECTURA`, y va aparte de la cifra porque es una conclusion:** el cerrojo de este arbol
**existe**, su proceso `30764` **no aparece en `ps`**, y `cerrojo._vive` devuelve `None`,
que **en este sistema significa duda y no un no** (`src/cerrojo.py` linea `85`). **La edad
de `6125 s` pasa el `TOPE_DE_HUERFANO` de `900 s`, asi que la proxima insercion lo rompe y
lo declara en vez de esperar.** **NO es una guarda de dato en rojo, y no abre bloqueante.**

**Y por que lo mido igual:** mi `ACTA 42` nombro **un cerrojo huerfano** como la causa
medida de que la vuelta `43` metiera `1` de `15`. **Aquel vivia dentro de `dataset/` y un
`checkout` lo repartia; `D.56` lo saco a `procesos/`.** Compruebo que la mudanza aguanta:

    $ git check-ignore -v procesos/nodos.jsonl.679b2259.cerrojo
    .gitignore:39:procesos/	procesos/nodos.jsonl.679b2259.cerrojo
    $ git status --porcelain procesos/
    (vacio: git no ve nada ahi)

**El segundo cerrojo, `e52fd5d2`, es de otra ruta de dataset y no de esta**: el instrumento
de la casa calcula para este arbol la huella `679b2259` y no la otra.

---

## 10. EL BARRIDO DE MIS PROPIAS AFIRMACIONES DE CORRIDA (`HEREDADO 1` punto `3`)

**Corrido sobre esta misma pagina, antes del sello. Su salida va pegada, sea cero o no sea
cero.**

    $ grep -n -i "esta corriendo\|quedo corriendo\|quedara corriendo\|corriendo mientras" docs/loop/APERTURA_CIEGA.md
    17:- **`1`. Ninguna frase de esta pagina dice que algo `esta corriendo` ni que `quedo
    CODIGO=0

    $ grep -n -i "corriendo" docs/loop/APERTURA_CIEGA.md
    17:- **`1`. Ninguna frase de esta pagina dice que algo `esta corriendo` ni que `quedo
    18:  corriendo`.** Lo que corri va con su salida pegada; lo que no corri lleva la palabra

**PRIMERA CORRIDA: `1` hallazgo, y es la linea `17`**, o sea **la cita de la forma
prohibida dentro de la propia declaracion que la prohibe**. **Ninguna afirmacion de corrida
en futuro.**

**SEGUNDA CORRIDA, SOBRE LA PAGINA YA CON LA PRIMERA PEGADA DENTRO.** Pegar la salida de
un barrido dentro de la pagina que el barrido mira **cambia lo que el barrido mide**, asi
que lo vuelvo a correr sobre el fichero final y pego tambien esta:

    $ grep -n -i "esta corriendo\|quedo corriendo\|quedara corriendo\|corriendo mientras" docs/loop/APERTURA_CIEGA.md
    17:- **`1`. Ninguna frase de esta pagina dice que algo `esta corriendo` ni que `quedo
    636:    $ grep -n -i "esta corriendo\|quedo corriendo\|quedara corriendo\|corriendo mientras" docs/loop/APERTURA_CIEGA.md
    637:    17:- **`1`. Ninguna frase de esta pagina dice que algo `esta corriendo` ni que `quedo
    641:    17:- **`1`. Ninguna frase de esta pagina dice que algo `esta corriendo` ni que `quedo

**`4` hallazgos, y los cuatro son la misma linea `17` vista cuatro veces**: la linea `17`
en si, la linea `636` que es el comando pegado, y las lineas `637` y `641` que son la linea
`17` citada dentro de las dos salidas pegadas. **Ninguna de las cuatro afirma que nada
corra.** Ese es el punto fijo: a partir de aqui, pegar el barrido otra vez solo anadiria
mas copias de la misma linea.

**TERCERA Y ULTIMA CORRIDA, SOBRE EL FICHERO YA SELLADO, Y ESTA SOLO CUENTA.** Cada vez
que pego un listado con sus renglones, **el listado siguiente cuenta tambien lo que acabo
de pegar**, asi que el ultimo instrumento de esta seccion es el contador, cuya salida es un
numero y **no anade ni una linea que casar**:

    $ grep -c -i -e "esta corr""iendo" -e "quedo corr""iendo" -e "quedara corr""iendo" -e "corr""iendo mientras" docs/loop/APERTURA_CIEGA.md
    9

**`9` lineas casan en el fichero sellado, y estan todas en dos sitios: la linea `17`, que
es la declaracion del `HEREDADO 1`, y las lineas `642` a `662`, que son las dos salidas
pegadas de esta misma seccion `10`.** Los renglones exactos son `17`, `642`, `643`, `647`,
`658`, `659`, `660`, `661` y `662`, sobre `720` del fichero. **Fuera de la declaracion y de
las salidas pegadas no casa ni una.**

**Los renglones de esta frase se miden sobre el fichero tal como lo entrego**, y el
contador `9` **no se mueve** cuando cambia lo que hay antes de la seccion `10`: lo unico
que se movio entre una edicion y otra fue la numeracion, no la cuenta. **Si el arnes anade
algo al sellar, la cifra que manda es el `9` del contador.**

**NINGUNA DE LAS TRES CORRIDAS SALE EN CERO, Y POR ESO VAN LAS TRES PEGADAS**, que
es lo que `HEREDADO 1` punto `3` manda: *sea cero o no sea cero*. **Y las tres apuntan al
mismo sitio: a la linea que cita la forma, nunca a una frase que la use.**

Lo que esta pagina dice de sus propias corridas son dos formas y solo dos: **`CORRIO`, con
su salida pegada** (secciones `2`, `3`, `4.2`, `5.2`, `6`, `7`, `8` y `9.3`), y **`NO LO
CORRI` o `NO TERMINO`, con el motivo detras** (secciones `9.1` y `9.2`).

---

## 11. LO QUE LLEVO A MI TURNO NORMAL, ESCRITO ANTES DE VER EL REPORTE

**Para que se pueda comprobar que no lo pense despues de leerlo.**

| # | lo que traigo | contra que lo comparo cuando se abra el reporte |
|---|---|---|
| 1 | **`22` candidatos, `171` pasos, `7` de `cap_02` y `15` de `cap_03`** | su censo de bandeja |
| 2 | **Los `22` son `SANO` en su procedimiento y ninguno `REPITE`** | sus veredictos y sus discutibles marcados |
| 3 | **`9` relaciones madre a hijo**, de las que **`2` ya estan declaradas en ficha y `7` las levanto yo** | sus aristas declaradas, y si alguna de mis siete no esta |
| 4 | **Mi tramo `L` coincide con el declarado en los `22`**, con `9` diferencias de rotulo | su tabla de frontera |
| 5 | **`0` `PUENTE` en `30` pasos sorteados con semilla `44`** | su fila de `PASOS INVENTADOS POR CAPITULO` |
| 6 | **`2` discutibles de fidelidad que levanto yo**, uno de ellos sin firmar | como marco esos dos pasos en su tabla de fidelidad |
| 7 | **`8` tramos de los dos capitulos sin ningun candidato**, con `L159` a `L167` (`leverage`) a la cabeza | si su frontera los declara o si pasan en silencio |
| 8 | **`d003` pagada y verificada contra `L143`** | su declaracion de la vuelta de saneamiento |
| 9 | **`CREDITO_serial.jsonl` fuera del arbol sin que nadie lo declare**, y el instrumento contestando `CERO` donde mi acta dice `2 de 3` y `1 de 3` | de donde saca la vuelta 45 la racha que publique |
| 10 | **El cerrojo huerfano de `6125 s` que NO esta en rojo** | si alguien lo nombra como bloqueante |
| 11 | **El barrido de vecinos, que no termino**, con su coste `MEDIDO` y su proyeccion | su propio informe de aduana sobre los `22` |

**Ninguna de estas once es un veredicto: son las lecturas con las que entro.** El veredicto
va en el acta, y el acta se escribe con el reporte delante.

**NO COMMITEO. El arnes sella esta pagina y la commitea el** (`D.34`).
