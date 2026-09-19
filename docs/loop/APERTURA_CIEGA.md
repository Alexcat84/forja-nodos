# APERTURA CIEGA DE LA VUELTA 46, lote 7 (`grove_high_output`), bandeja de `cap_02` y `cap_03`

**Auditor de la linea `serial`, rama `extraccion-mundo-11`.** Escrita ANTES de ver
`docs/loop/REPORTE.md`, que no esta en el arbol. **La vuelta que vengo a auditar es la
`45`, la primera de insercion despues de la parada por credito roto.**

---

## 0. LAS DOS DECLARACIONES QUE EL ARNES EXIGE

    ACTA ANTERIOR LEIDA: 8fd9fc9094f880ab4f77775885baaf2c7eef815f
    HEREDADOS: NINGUNO

**`NINGUNO` no es un silencio mio: es lo que el instrumento de la herencia mide**, y va con
su salida pegada como `D.40` manda.

    $ python forja.py herencia
      acta anterior : ACTA 43. VUELTA 44, lote 7 (`grove_high_output`), **LA PRIMERA VUELTA DE SANEAMIENTO DE ESTA LINEA**: [...]
      su huella     : 8fd9fc9094f880ab4f77775885baaf2c7eef815f
      heredados     : 0

      El acta anterior no dejo ninguna tarea bloqueante ni ningun remedio escrito. Aun asi
      tienes que declarar la linea de lectura.

**Y la huella la comprueba mi propio instrumento contra el fichero que abri**, porque
`D.40` dice que decir que leiste otra version no es haberla leido:

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    8fd9fc9094f880ab4f77775885baaf2c7eef815f

    $ git cat-file -s 8fd9fc9094f880ab4f77775885baaf2c7eef815f
    2241205

**La huella que el prompt me entrega es la del fichero que hay en el arbol ahora mismo**, y
es el que lei. **No hay ningun heredado que declarar `CUMPLIDO` ni `NO APLICA`**, porque no
hay ninguno: la `ACTA 43` cerro con parada y dejo `PROMPT_SIGUIENTE.md` vacio, y el encargo
de la vuelta `45` lo escribio el fundador al levantar la parada.

---

## 1. LO QUE NO HE ABIERTO, Y LO QUE SI

**El arnes escribio en `docs/loop/loop.log` la linea de mi propio turno, y `loop.log` YA NO
SE RETIRA (`D.57`).** Asi que lo que se me retiro no lo supongo: lo leo.

    $ tail -3 docs/loop/loop.log
    [2026-09-18 23:40:30] VUELTA 1 : APERTURA CIEGA (claude-opus-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl
    [2026-09-18 23:40:30]   hereda 0 remedio(s) del acta anterior, entregados en el prompt (D.40)
    [2026-09-18 23:40:30]   y solo eso: remedios con su motivo, sin cifras ni conclusiones (D.52)

    $ git status --porcelain docs/loop/
     M docs/loop/APERTURA_CIEGA.md
     D docs/loop/CREDITO_serial.jsonl
     D docs/loop/REPORTE.md
     M docs/loop/loop.log
     M docs/loop/ultimo_apertura.json
     D docs/loop/ultimo_auditor.json
     D docs/loop/ultimo_extractor.json

**Esta salida es la de despues de escribir esta pagina, y lo digo porque su primera linea lo
delata:** `APERTURA_CIEGA.md` sale ` M` y no ` D` **porque la acabo de escribir yo.** Cuando
la corri al abrir el turno, esa linea era ` D` y las otras seis eran identicas. **Pego la
vigente y digo lo que cambio, en vez de pegar la vieja como si fuera la de ahora.**

**`LECTURA` (`D.38.3`, la frase es la del instrumento):** el instrumento midio **cuatro
ficheros nombrados en la linea de `retirados:` y siete rutas movidas en `docs/loop/`**. Mi
conclusion sobre contenido, aparte y marcada: **los cuatro nombrados salieron del arbol y
`loop.log` NO salio**, que es exactamente la mitad de `D.57` que la decision del `18 sep`
puso; **y `CREDITO_serial.jsonl`, que la `ACTA 43` encontro retirado SIN DECLARAR, hoy va
declarado en la linea.** La averia que rompio mi racha esta cerrada y lo compruebo desde
dentro de la fase ciega, que era el caso positivo que la decision pedia.

**No los he recuperado de git.** Ninguno de los cuatro.

**Y hay un quinto que tampoco he abierto y que SI esta en el arbol:**
`docs/loop/archivo/grove_high_output/REPORTE.md`, el reporte del frente `grove` ya
cosechado, **que es quien escribio los `22` candidatos que vengo a clasificar a ciegas.**
Leerlo seria leer la lectura que vengo a comparar con la mia. Mido su tamanio, que no es
leerlo:

    $ wc -c docs/loop/archivo/grove_high_output/REPORTE.md
    118685 docs/loop/archivo/grove_high_output/REPORTE.md

**Lo que SI he abierto**, y `AUDITOR_FORJA.md` 1 lo dice en voz alta: mi propia
`ACTA_AUDITOR.md`, `AUDITOR_FORJA.md` entero, `docs/BANCO_DE_REGLAS.md` en sus reglas
`D.53` y `D.55`, `docs/loop/PROMPT_SIGUIENTE.md`, `docs/loop/DEUDA.jsonl`,
`docs/loop/paradas/2026-09-18-arista-py-y-la-ciega-sin-registro-DECISION.md`, los dos
capitulos fuente y los `22` candidatos.

**Y he abierto tambien mi propia `APERTURA_CIEGA.md` de la vuelta anterior**
(`git show e3abd05`), que es sede mia y no del extractor. **Lo digo porque cambia como hay
que leer esta pagina:** la bandeja que clasifico hoy es **la misma** que clasifique
entonces, asi que mi seccion `6` no es una lectura virgen. **Lo que hice fue releer los dos
capitulos enteros y los `22` candidatos contra su tramo otra vez**, y la seccion `6.2` dice
donde mi lectura de hoy se separa de la de entonces.

---

## 2. LOS INSTRUMENTOS QUE CORRI, CON SU SALIDA PEGADA (`D.38.3`)

### 2.1. Las guardas de la casa

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python forja.py guiones cuarentena/grove_high_output/
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python forja.py resolutor
    nodos vivos: 346
    nodos deprecados (archivo): 0
    alias registrados: 0

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1087 total

### 2.2. El tablero y la deuda

    $ python forja.py tablero
      prio lote clave                          estado                 dueno                 band ult cap
      1    7    grove_high_output              COSECHADO              NINGUNO                 22  cap_03
      2    9    gerber_emyth                   PAUSADO                NINGUNO                 10  cap_11
      3    5    marquet_turn_the_ship          PAUSADO                NINGUNO                  9  cap_03
      libros CON DUEÑO ahora mismo: 0
      MUNDO 11: faltan 3 de 3 libros del corte (grove_high_output, gerber_emyth, marquet_turn_the_ship)
      COLA DE DOCTRINA (D.56): 11 pregunta(s), 0 bloquea(n)

**ESE BLOQUE ES UN RECORTE Y LO DIGO CON LO QUE CORTE**: el instrumento imprime **once
filas** y yo pego **las tres del corte del mundo 11**. Las ocho que no pego son
`onu_consumidor`, `smart_who`, `zhuo_manager` y `scott_radical_candor` (las cuatro
`INSERTADO`, bandeja `0`), `gerber_emyth_cap17_reservado` `SIN EMPEZAR`, y
`bernerslee_bananas`, `openstax_business_ethics` y `openstax_org_behavior`, las tres
`SIN EMPEZAR` y marcadas **fuera de campania**. **Ninguna de las ocho tiene candidato en
bandeja**, y por eso ninguna entra en lo que clasifico hoy.

    $ python scripts/deuda.py
      pendientes: 9    pagadas: 6
      d005   grove v2 relevo de grove    De los 15 candidatos de cap_03 de grove, su aduana e
      d006   41      relectura          cap_13 entero esta en 4 de 212, el 1,89 por ciento,
      d007   41      doctrina           La cola de doctrina queda congelada en 11 preguntas
      d009   42      deuda              scripts/tabla_de_cierre.py mide la tabla de cierre c
      d011   43      deuda              TODO TECHO QUE EL AUDITOR ESCRIBA LLEVA SU MITAD EN
      d012   43      deuda              SEGUNDO EJEMPLAR MEDIDO de la pregunta 9 de la cola
      d020   44      maquinaria         src/arista.py linea 182 teclea veredicto CONTINUA en
      d021   44      fidelidad          PUENTE en clasificar_trabajo_proceso_montaje_prueba
      d022   44      maquinaria         scripts/tabla_de_cierre.py localiza la tabla por la
      ultima vuelta de saneamiento: 44

**`LECTURA`:** el instrumento midio **`9` pendientes y `6` pagadas**. Mi conclusion sobre
contenido, aparte: **las `9` pendientes son `3` mas que las `6` que este mismo instrumento
midio al abrir la vuelta `45`**, y las tres nuevas (`d020`, `d021`, `d022`) son de la
vuelta `44`. **`d021` es la unica de las nueve que toca el texto de un candidato de esta
bandeja**, y la verifico yo contra el libro en la seccion `8`.

**Y la columna `band` del tablero NO mide esta bandeja para los otros dos libros**, y lo
digo para no publicar una discrepancia que no existe: el propio instrumento escribe
`bandeja_medida_en` y para `marquet_turn_the_ship` apunta a
`extraccion-marquet_turn_the_ship`. En ESTE arbol `cuarentena/marquet_turn_the_ship/` tiene
`3`, no `9`. **Son dos poblaciones distintas medidas a proposito, no una cifra mal puesta.**

---

## 3. LA CIFRA QUE EL INSTRUMENTO DA Y QUE NO PUBLICO COMO SUYA: EL CREDITO

    $ python forja.py credito
    CREDITO DE LA LINEA 'serial' (D.48)
      registro: docs/loop/CREDITO_serial.jsonl

      LINEA SIN REGISTRO: no hay ningun suceso escrito.
      Una linea sin tandas NACE CON SU RACHA EN CERO y no hereda
      la de nadie (D.48). Lo que herede el arnes sera CERO remedios.

**ESTA ES LA LIMITACION, ESCRITA EN VEZ DE LA AFIRMACION (`D.57`).** El instrumento lee
`docs/loop/CREDITO_serial.jsonl`, **y ese fichero es uno de los cuatro que el arnes retiro
para mi turno**, nombrado en la linea de `retirados:` de la seccion `1`. Asi que su
`LINEA SIN REGISTRO` **no mide que la linea no tenga registro: mide que el fichero no esta
en el arbol durante mi fase ciega.**

    $ git ls-tree --name-only -r HEAD -- docs/loop/ | grep CREDITO
    docs/loop/CREDITO_serial.jsonl

**Esta en `HEAD` y no esta en el arbol. NO LO RECUPERO.** Y por tanto **NO PUBLICO NINGUNA
CIFRA DE RACHA EN ESTA PAGINA**: ni la mia ni la del extractor. La racha se lee en el
registro, el registro no esta, y una racha contada de memoria es exactamente la especie de
caida que me ha tumbado tres actas.

**Lo unico que si puedo comprobar, porque su sede SI esta en el arbol**, es que el reinicio
de mi racha existe y quien lo firmo:

    $ sed -n '31,36p' docs/loop/paradas/2026-09-18-arista-py-y-la-ciega-sin-registro-DECISION.md
    > 3. LA RACHA DEL AUDITOR SE REINICIA con la condicion mecanica que el
    >    mismo propuso: el arnes NO retira loop.log durante la fase ciega (es
    >    registro del arnes, no del extractor, y sin el la ciega no puede
    >    comprobar que se le retiro) y, ademas, pega la linea literal de
    >    retirados: en el prompt de la fase ciega. Regla al banco, sin numero,
    >    tu lo asignas: LA FASE CIEGA SABE QUE NO VE. Caso positivo con

**`AUDITOR_FORJA.md` 5.4 dice que la racha la reinicia una decision de Alexis escrita en
`docs/loop/paradas/` y que el acta lo dice citandola. La cito. NO me la reinicio yo**, y
**la cuenta exacta la dejo para cuando el registro vuelva al arbol.**

---

## 4. LO QUE LA VUELTA 45 MOVIO EN EL DATO: MEDIDO, NO SUPUESTO

La vuelta `45` se encargo como **vuelta de insercion** (`docs/loop/PROMPT_SIGUIENTE.md`,
que si esta en el arbol). Lo que movio lo mido commit a commit:

    $ for h in 3b8c607 4dc991d 2aae716 26ad453 3274336; do printf "%s dataset=%s veredictos=%s\n" ... done
    3b8c607 dataset=346 veredictos=740
    4dc991d dataset=346 veredictos=740
    2aae716 dataset=346 veredictos=740
    26ad453 dataset=346 veredictos=740
    3274336 dataset=346 veredictos=740
    ARBOL    dataset=346 veredictos=740

**Los cinco hashes, con su asunto, y esta columna la pongo YO y no el instrumento:**
`3b8c607` cierre de la vuelta `44`; `4dc991d` `D.53` al codigo y `D.57` al arnes; `2aae716`
apertura de la vuelta `45`; `26ad453` esqueleto de la vuelta `45`; `3274336` `TAREA 1` de la
vuelta `45`.

    $ ls cuarentena/_insertados/grove_high_output/ | wc -l
    1

    $ ls cuarentena/grove_high_output/*.json | wc -l
    22

**`LECTURA`:** el instrumento midio **`346` nodos y `740` veredictos en los cinco commits y
en el arbol**, y **`1` fichero en `_insertados` de grove contra `22` en la bandeja**. Mi
conclusion sobre contenido, aparte y marcada: **en la vuelta `45` no entro ni un nodo al
grafo, y la bandeja de grove sigue entera en `22`.** El asunto del commit `3274336` dice
`la insercion de grove queda declarada como PARADA DE TAREA`; **el asunto de un commit no es
sede de cifra (`5.6`), asi que lo que firmo es la medida, no el asunto**, y las dos dicen lo
mismo.

**Lo que NO puedo comprobar desde aqui, y lo escribo en vez de afirmarlo:** **por que** no
entro ninguno. El motivo estara en `REPORTE.md`, que no esta en el arbol. **No lo supongo.**
Lo unico medible es el rastro que la corrida dejo sin commitear:

    $ ls -la .v45/informe_d021.txt .v45/informe_d021.reloj
    -rw-r--r-- 1 AlexDesk 197609 11 Sep 18 23:29 .v45/informe_d021.reloj
    -rw-r--r-- 1 AlexDesk 197609  0 Sep 18 23:29 .v45/informe_d021.txt

**`LECTURA`:** el instrumento midio **un fichero de `0` bytes con su reloj al lado**. Mi
conclusion, aparte: **una corrida de `forja.py informe` se lanzo y su salida quedo en cero**,
que es la firma de una corrida que no termino. **`7.B` de la cosecha dice que una ruta
publicada como prueba y que apunta a un fichero de cero bytes es caida de cifra**; si el
reporte la publica como prueba, es caida; **si no la publica, no hay caida y yo no la
invento.** No puedo saber cual de las dos es sin el reporte, **y por eso lo dejo escrito
aqui como lo que hay que mirar en cuanto lo tenga delante**, no como una caida.

---

## 5. EL MATERIAL: CENSO DE LA BANDEJA, CONTADO CON INSTRUMENTO

    $ python .v46/censo_bandeja.py
    cap_02 clasificar_trabajo_proceso_montaje_prueba        pasos= 7 aristas=0  PIEZA P5 L37 a L47
    cap_02 construir_flujo_produccion_paso_limitante        pasos=10 aristas=0  PIEZA P2 L15 a L27
    cap_02 detectar_arreglar_fallo_etapa_menor_valor        pasos= 6 aristas=0  PIEZA P11 L71 a L75
    cap_02 dimensionar_inventario_materia_prima_reposicion  pasos= 7 aristas=0  PIEZA P10 L69
    cap_02 equilibrar_capacidad_personal_inventario_plazo   pasos= 8 aristas=0  PIEZA P7 L57 a L61
    cap_02 preferir_inspeccion_proceso_prueba_destructiva   pasos= 6 aristas=0  PIEZA P9 L67
    cap_02 rehacer_flujo_paso_limitante_capacidad           pasos= 6 aristas=0  PIEZA P6 L49 a L55
    cap_03 archivar_indicadores_resolver_problemas          pasos= 4 aristas=0  PIEZA P12 L99 a L99
    cap_03 casar_flujo_fabricacion_flujo_ventas             pasos=12 aristas=0  PIEZA P14 L111 a L121
    cap_03 construir_grafico_escalonado_pronosticos         pasos= 8 aristas=0  PIEZA P11 L91 a L97
    cap_03 construir_indicador_linealidad_alerta_temprana   pasos= 9 aristas=0  PIEZA P9 L83 a L87
    cap_03 construir_indicador_tendencia_patron             pasos= 6 aristas=0  PIEZA P10 L89 a L89
    cap_03 decidir_aceptar_rechazar_material_defectuoso     pasos= 8 aristas=0  PIEZA P17 L135 a L137
    cap_03 dimensionar_plantilla_administrativa_pronostico  pasos= 7 aristas=0  PIEZA P15 L123 a L125
    cap_03 elegir_cinco_indicadores_diarios_fabrica         pasos=10 aristas=0  PIEZA P2 L15 a L29
    cap_03 elegir_fabricar_pedido_pronostico                pasos= 9 aristas=0  PIEZA P13 L101 a L109
    cap_03 elegir_indicador_salida_trabajo_administrativo   pasos= 7 aristas=0  ?
    cap_03 elegir_inspeccion_barrera_monitorizacion         pasos=12 aristas=0  PIEZA P18 L139 a L141
    cap_03 emparejar_indicadores_efecto_contraefecto        pasos= 7 aristas=0  PIEZA P3 L31 a L33
    cap_03 representar_actividad_caja_negra_ventanas        pasos= 9 aristas=0  PIEZA P7 L71 a L79
    cap_03 simplificar_trabajo_reducir_numero_pasos         pasos= 7 aristas=0  PIEZA P23 L169 a L173
    cap_03 variar_frecuencia_inspeccion_nivel_calidad       pasos= 6 aristas=0  PIEZA P19 L143 a L145
    candidatos=22  pasos_totales=171

    $ wc -l fuentes/grove_high_output/cap_02.md fuentes/grove_high_output/cap_03.md
    119 fuentes/grove_high_output/cap_02.md
    179 fuentes/grove_high_output/cap_03.md

**`LECTURA`:** el instrumento midio **`22` candidatos, `171` pasos, `7` de `cap_02` y `15`
de `cap_03`, y `0` aristas escritas en ficha.** Mi conclusion, aparte: **la columna del
tramo es la que la propia ficha declara en su `resumen_teorico`**, y **la unica celda `?` es
`elegir_indicador_salida_trabajo_administrativo`**, cuyo `resumen_teorico` no deja el tramo
en el patron `PIEZA Pn Lx a Ly` que mi instrumento busca. **No es una ficha sin tramo: es mi
patron el que no la pilla**, y su tramo lo leo yo a mano en la seccion `6` y lo digo ahi.

---

## 6. MI CLASIFICACION, CANDIDATO A CANDIDATO Y A CIEGAS

**Relei los dos capitulos enteros antes de volver a abrir un candidato**, y despues cada
candidato contra su tramo del libro. `cap_02` es el capitulo `1` (*The Basics of
Production*) y `cap_03` es el capitulo `2` (*Managing the Breakfast Factory*); los dos van
en `fidelidad: verbatim`.

### 6.1. Las veintidos filas

| # | candidato | cap | tramo que yo leo | mi clase | mi lectura del par |
|---|---|---|---|---|---|
| 1 | `construir_flujo_produccion_paso_limitante` | 02 | `L15` a `L27` | **SANO** | cabeza de la serie de flujo; procedimiento propio: fija el paso limitante y escalona hacia atras |
| 2 | `rehacer_flujo_paso_limitante_capacidad` | 02 | `L49` a `L55` | **SANO con arista** | hijo del `1`: busca la cola, cuenta la espera, declara paso limitante NUEVO. No repite al `1`: lo rehace |
| 3 | `equilibrar_capacidad_personal_inventario_plazo` | 02 | `L57` a `L61` | **SANO con arista** | hijo del `1`: nombra las cuatro salidas con su coste e intercambia capacidad, mano de obra e inventario |
| 4 | `clasificar_trabajo_proceso_montaje_prueba` | 02 | `L37` a `L47` | **SANO** | cabeza de la serie de prueba; las tres operaciones senaladas en tu propio trabajo |
| 5 | `preferir_inspeccion_proceso_prueba_destructiva` | 02 | `L67` | **SANO con arista** | hijo del `4` por su paso `3`: abre la prueba en las dos vias y elige. **Es el par que `D.53` re adjudico, y lo leo `SANO` igual** |
| 6 | `dimensionar_inventario_materia_prima_reposicion` | 02 | `L69` | **SANO con arista** | hijo del `5`: inspeccion de recepcion y dimensionado por tiempo de reposicion |
| 7 | `detectar_arreglar_fallo_etapa_menor_valor` | 02 | `L71` a `L75` | **SANO** | el principio de valor creciente; procedimiento propio de ordenar etapas y poner la comprobacion |
| 8 | `elegir_cinco_indicadores_diarios_fabrica` | 03 | `L15` a `L29` | **SANO** | cabeza de la serie de indicadores; los cinco datos uno a uno y el repaso de primera hora |
| 9 | `emparejar_indicadores_efecto_contraefecto` | 03 | `L31` a `L33` | **SANO con arista** | hijo del `8`: nombra efecto y contraefecto y los mide juntos |
| 10 | `elegir_indicador_salida_trabajo_administrativo` | 03 | `L35` a `L67` | **SANO con arista** | hijo del `9`: las dos varas mas la tabla de seis funciones. **Tramo leido a mano: la tabla va de `L39` a `L65` y su pie esta en `L67`** |
| 11 | `representar_actividad_caja_negra_ventanas` | 03 | `L71` a `L79` | **SANO** | cabeza de la serie de ventanas: entrada, salida, trabajo, y las ventanas recortadas |
| 12 | `construir_indicador_linealidad_alerta_temprana` | 03 | `L83` a `L87` | **SANO con arista** | hijo del `11`: la recta ideal, lo conseguido y la lectura a media carrera |
| 13 | `construir_indicador_tendencia_patron` | 03 | `L89` | **SANO con arista** | hijo del `11`: salida contra tiempo y contra patron |
| 14 | `construir_grafico_escalonado_pronosticos` | 03 | `L91` a `L97` | **SANO con arista** | hijo del `13`: el propio libro lo compara con el grafico de tendencia simple |
| 15 | `archivar_indicadores_resolver_problemas` | 03 | `L99` | **SANO** | el mas corto de la bandeja con `4` pasos: recoge, archiva, repasa cuando algo falle |
| 16 | `elegir_fabricar_pedido_pronostico` | 03 | `L103` a `L109` | **SANO** | cabeza de la serie de pronostico: las dos vias y el riesgo de inventario |
| 17 | `casar_flujo_fabricacion_flujo_ventas` | 03 | `L111` a `L121` | **SANO con arista** | hijo del `16`: los dos flujos, los dos pronosticos y la holgura |
| 18 | `dimensionar_plantilla_administrativa_pronostico` | 03 | `L123` a `L125` | **SANO con arista** | hijo del `10`: patrones de hecho y plantilla contra pronostico |
| 19 | `decidir_aceptar_rechazar_material_defectuoso` | 03 | `L135` a `L137` | **SANO con arista** | hijo del `6`: que hacer cuando la inspeccion de recepcion rechaza, y donde deja de ser economico |
| 20 | `elegir_inspeccion_barrera_monitorizacion` | 03 | `L139` a `L141` | **SANO** | cabeza de la serie de inspeccion de `cap_03`: barrera contra monitorizacion con su intercambio |
| 21 | `variar_frecuencia_inspeccion_nivel_calidad` | 03 | `L143` | **SANO** | hermano del `20`, no hijo: el libro lo abre con *otra manera de bajar el coste* |
| 22 | `simplificar_trabajo_reducir_numero_pasos` | 03 | `L169` a `L171` | **SANO** | dibuja, cuenta, fija meta, pregunta y tira |

**`LECTURA`, y es mia, no de ningun instrumento: los veintidos traen procedimiento propio y
NO leo ni un `REPITE` ni un `CONTINUA` en la bandeja.** Lo que leo son **trece relaciones
declarables**, y `D.53` dice que declararlas no convierte el par en `CONTINUA`: **el
veredicto y la arista son puertas distintas.**

### 6.2. DONDE MI LECTURA DE HOY SE SEPARA DE MI PROPIA APERTURA SELLADA DE LA VUELTA 45

Lo digo porque abri esa pagina y seria deshonesto presentar esto como una lectura virgen.
**Las veintidos clases coinciden. Se separan en dos sitios, los dos de tramo:**

- **`11`, `representar_actividad_caja_negra_ventanas`:** entonces escribi `L73 a L79`; **hoy
  leo `L71 a L79`**, porque `L71` es el encabezado *The Black Box* y la ficha lo declara
  asi. **Mi cifra vieja estaba corta por una linea, y la corrijo aqui sin borrarla.**
- **`22`, `simplificar_trabajo_reducir_numero_pasos`:** entonces escribi `L169 a L171`; **hoy
  leo lo mismo**, pero **la ficha declara `L169 a L173`** y `L173` no pone ni un paso. **El
  tramo declarado es mas ancho que el usado**, que no es caida de nadie, y lo dejo medido.

---

## 7. LA RELECTURA DE FIDELIDAD `D.30`: LOS `171` PASOS, LEIDOS UNO A UNO CONTRA EL LIBRO

**No es una muestra: son los `171`.** Lei cada paso contra su parrafo del capitulo.

| capitulo | pasos | `TRANSCRIPCION` que leo | `PUENTE` que leo |
|---|---|---|---|
| `cap_02` | `50` | `50` | `0` |
| `cap_03` | `121` | `121` | `0` |
| **total** | **`171`** | **`171`** | **`0`** |

**El denominador sale del instrumento** (`pasos_totales=171`, seccion `5`); **la particion
entre `TRANSCRIPCION` y `PUENTE` es LECTURA MIA y la firmo como tal**, no como cifra de
maquina.

**Y LLEVA UNA CONDICION QUE NO SE PUEDE OMITIR: ese `0` es sobre el arbol de HOY, con la
correccion de `d021` YA APLICADA.** Sobre el texto anterior a esa correccion **son `170` y
`1`**, y ese `1` es el paso `4` de `clasificar_trabajo_proceso_montaje_prueba`. La seccion
`8` lo verifica.

---

## 8. `d021`: LO VERIFICO CONTRA EL LIBRO, Y MARCO UN DISCUTIBLE QUE LA CORRECCION NO TOCA

    $ git diff --stat cuarentena/
     .../grove_high_output/clasificar_trabajo_proceso_montaje_prueba.json | 4 ++--
     1 file changed, 2 insertions(+), 2 deletions(-)

**El texto viejo del paso `4`:** *Prueba cada pieza por separado antes de montarla, que es
lo que el libro llama prueba unitaria, **y en un trabajo de personas toma la forma de una
presentacion en seco ante un grupo escogido**.*

**El texto nuevo:** *Prueba cada pieza por separado antes de montarla, que es lo que el
libro llama prueba unitaria.*

**LO VERIFICO YO CONTRA `cap_02`, y la correccion se sostiene.** `L45` dice *Each piece then
undergoes an individual operation called a "unit test"*, que es pieza a pieza y **ANTES** del
montaje. `L41` dice *The test operation comes in the form of a "dry run" presentation with a
selected group of field sales personnel*, y en ese mismo parrafo la presentacion ya esta
**MONTADA** (*are made to flow into one presentation*). **El libro no iguala las dos
operaciones en ningun renglon de `L41`, `L45` ni `L47`**, y `L47` solo dice *a basically
similar flow of activity*. **La mitad retirada atribuia al libro una equivalencia que el
libro no escribe: era `PUENTE`, y retirarla es correcto.**

> ### **EL DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO: EL PASO `5` LLEVA LA MISMA FIGURA Y NADIE LO TOCO**
>
> El paso `5` dice: *Devuelve a la fase de proceso la pieza que falle su prueba, para
> rehacerla, **y rehazla contra lo que la prueba dijo: las preocupaciones y las objeciones
> del publico que la probo**.*
>
> **La primera mitad es `L45`** (*the defective portion of the software is returned to the
> process phase for "rework"*). **La segunda es `L41`** (*the material must be "reworked" to
> meet the concerns and objections of the test audience*). **Es la MISMA costura entre los
> dos casos que `d021` condeno en el paso `4`**, en la misma ficha y sin corregir.
>
> **YO LO LEO `TRANSCRIPCION`, y digo por que:** a diferencia del paso `4`, aqui **el libro
> usa la palabra `rework` en los DOS casos**, asi que la costura no inventa una equivalencia
> de operaciones: junta dos redacciones de una operacion que el libro si nombra dos veces.
> **Esa es la lectura que deja la ficha en pie, o sea la que me conviene**, y por eso dejo
> escrita la contraria: **un lector estricto dira que `d021` no se pago entera y que aqui
> queda un `PUENTE` de la misma especie.** Si cae, **cae DENTRO de mi marcado.**

**Y UNA MEDIDA QUE DEJO SIN ADJUDICAR PORQUE ME FALTA EL REPORTE:** la correccion **esta sin
commitear**.

    $ git status --porcelain cuarentena/
     M cuarentena/grove_high_output/clasificar_trabajo_proceso_montaje_prueba.json

**`LECTURA`:** el instrumento midio **una ruta de `cuarentena/` modificada y no commiteada**
al terminar la vuelta `45`. Mi conclusion, aparte: **el texto corregido existe en el arbol y
no existe en ningun commit**, y `d021` sigue figurando `pendiente` en `scripts/deuda.py`.
**No digo si eso es caida**: si el reporte declara la correccion como entregada, la sede y la
especie se discuten con el reporte delante; **si la declara como trabajo en curso, no hay
nada que discutir.** No tengo el reporte. **Escribo la medida y no la conclusion.**

---

## 9. LAS `93` LINEAS RE ADJUDICADAS: LAS CUENTO YO Y SALEN AL DIGITO

La decision del `18 sep` publica un censo. **Lo recomputo con mi propio comando sobre la
bitacora de hoy**, porque `AUDITOR_FORJA.md` 1.1 dice que una cifra se lee del instrumento
corrido en esta vuelta.

    $ python -c "el cohorte de las 93: lineas de arista declarada por lectura, contadas hoy"
    lineas de arista declarada por lectura, HOY : 93
       SIN LECTURA PROPIA     79
       SANO                   13
       CONTINUA                1
    de ese cohorte, con veredicto_original      : 92
    de ese cohorte, con cita_del_veredicto      : 93

**Lo que la decision publica:** `CONTINUA 1`, `SANO 13`, `SIN LECTURA PROPIA 79`,
`con cita 93`.

**`LECTURA`: las cuatro cifras me salen al digito.** Y la quinta, que la decision no publica,
**tambien cuadra**: `92` lineas llevan `veredicto_original` y no `93`, porque **la unica que
ya estaba bien leida no cambio de valor y no tiene valor viejo que guardar**. `92 + 1 = 93`.
**No es una cifra que falte: es la que sobra si se cuenta mal.**

    $ sed -n '175,185p' src/arista.py
        if veredicto is None or str(veredicto).upper() not in VEREDICTOS:
            resultado.codigo = CODIGO_RECHAZO
            resultado.decir("")
            resultado.decir("ARISTA NO ESCRITA: falta --veredicto, y no se supone (D.53).")
            resultado.decir("  El veredicto de un par y su arista son puertas distintas: el")
            resultado.decir("  veredicto lo emite LA LECTURA (%s) y viaja con la arista."
                            % ", ".join(VEREDICTOS))
            resultado.decir("  Hasta el 18 sep 2026 aqui se tecleaba CONTINUA siempre, y eso")
            resultado.decir("  escribio 93 lineas de la sede de CLASE contra una regla que")
            resultado.decir("  la casa ya tenia escrita.")
            return resultado

**`LECTURA`:** el instrumento midio **el rechazo escrito en `src/arista.py` cuando falta
`--veredicto`**. Mi conclusion, aparte: **el hallazgo que la `ACTA 43` desentierro esta
cerrado en el codigo**, y la cifra `93` que el propio codigo cita en su rechazo **es la que
yo acabo de recontar**, asi que no es una cifra huerfana dentro de una guarda.

---

## 10. EL BARRIDO DE VECINOS `D.38.4`: LO QUE TERMINO, LO QUE NO, Y SU COSTE MEDIDO

### 10.1. La poblacion, y una brecha que mido y no adjudico

    $ python .v46/familia.py
    poblacion D.38.4: grafo 346 + bandejas 25 = 371

    $ for d in cuarentena/*/; do printf "%-44s %s\n" "$d" "$(ls "$d" | grep -c '\.json$')"; done
    cuarentena/_derivadas/                       2
    cuarentena/_insertados/                      0
    cuarentena/ensayo_referencia_163/            163
    cuarentena/grove_high_output/                22
    cuarentena/marquet_turn_the_ship/            3
    cuarentena/onu_consumidor/                   0
    cuarentena/scott_radical_candor/             0
    cuarentena/smart_who/                        0
    cuarentena/zhuo_manager/                     0

**`LECTURA`, y es una brecha de metodo que dejo medida:** `D.38.4` define mi poblacion como
*`dataset/nodos.jsonl` mas todo lo que espera en `cuarentena/<libro>/`, descartando
`_insertados` y `_derivadas`*. **Contada asi, la poblacion es `346 + 163 + 22 + 3 = 534`.**
La que la aduana mide es **`371`**. La diferencia son **las `163` de
`cuarentena/ensayo_referencia_163/`**, y **mido por que se caen**:

    $ python -c "por que las 163 de ensayo_referencia_163 no entran en la poblacion de la aduana"
    claves canonicas en fuentes/FUENTES_CANONICAS.json: 13
    cuarentena/ensayo_referencia_163: {'NO canonica': 163}
      de esas, sin ninguna clave de fuente: 0

**Las `163` se caen por el filtro `_fuentes_canonicas` de `src/aduana.py`**, que exige que
TODAS las fuentes de un candidato esten en la tabla vigente, **y las `163` tienen clave de
fuente pero ninguna es canonica.** **`D.38.5` me dice que mi barrido y el de la aduana ya
miden la misma poblacion y que si no cuadran es discrepancia de verdad; cuadran, porque uso
el instrumento de la aduana.** Lo que no cuadra es **la aduana contra la letra de `D.38.4`**,
y son `163` candidatos de diferencia.

**NO ABRO PARADA Y NO LA LLEVO A LA COLA.** `D.56` congela la doctrina hasta que cierre el
mundo 11 y manda *registrala en tu acta con su medida y DEJALA AHI*. **Queda registrada con
su medida.** Y digo la mitad que la atenua, para no dejarla sesgada a mi favor: **un
candidato de fuente no canonica no puede entrar por la aduana**, asi que la brecha es de
vecinos que nunca seran nodos.

### 10.2. La senal que SI termino: `familia_id` sobre los `371`

    $ python .v46/familia.py
    umbral_familia_id: 0.3
    construir_flujo_produccion_paso_limitante        levanta 1
          0.429  rehacer_flujo_paso_limitante_capacidad
    rehacer_flujo_paso_limitante_capacidad           levanta 1
          0.429  construir_flujo_produccion_paso_limitante

    familia_id levanta 2 pares sobre 22 candidatos, poblacion 371, en 0.3 s

**TAMBIEN ES UN RECORTE, y digo que corte:** el instrumento imprime **una fila por cada uno
de los `22`**, y yo pego **las dos que levantan algo**. **Las otras veinte dicen
`levanta 0`** y su salida entera esta en `.v46/familia.txt`. **El total `2` de la ultima
linea es del instrumento y cuadra con las dos filas que pego**, que es lo que hace
comprobable el recorte.

**`LECTURA`:** el instrumento midio **`2` levantamientos, que son el mismo par visto por sus
dos extremos**, sobre poblacion `371` y en `0,3` segundos **MEDIDOS**. Mi conclusion, aparte:
**ese par es el `1` con el `2` de mi tabla, que yo ya habia leido madre e hijo sin mirar
ninguna senal.** `D.19`: **la senal dijo donde mirar y ahi acabo su trabajo.**

### 10.3. LAS OTRAS DOS SENALES: EL BARRIDO **NO TERMINO**, Y NO PUBLICO SU CIFRA

**`similitud_texto` y `paso_contra_nodo` sobre los `371` siguen corriendo cuando cierro esta
pagina.** Lo digo con la palabra que mi propia `ACTA 42` me dejo encargada: **`NO TERMINO`.**

**El coste, con su etiqueta:**

    $ python -u -c "las dos senales caras, cronometradas sobre 40 vecinos"
    sobre 40 vecinos: similitud_texto 14.16s   paso_contra_nodo 9.20s
    proyeccion a 371 x 22 candidatos: similitud 48 min, paso 31 min

    $ head -9 .v46/vecinos.txt
    poblacion del barrido (D.38.4)
      dataset/nodos.jsonl        : 346
      cuarentena (todas)         : 25
      POBLACION TOTAL            : 371
      umbrales: similitud 0.35  familia_id 0.3  paso_contra_nodo 0.6

     1/22  archivar_indicadores_resolver_problemas          vecinos=2   (387s)
            -> construir_indicador_tendencia_patron   {'similitud_texto': 0.384, 'familia_id': 0.143, 'paso_contra_nodo': 0.42}
            -> revisar_tres_preguntas_valor_carrera   {'similitud_texto': 0.369, 'familia_id': 0.0, 'paso_contra_nodo': 0.414}

**`387` s para el candidato `1` de `22` es MEDIDO. `142` min para los veintidos es
PROYECTADO** sobre ese ritmo, y no lleva la palabra `medidos` al lado.

**Y LA PROYECCION ES UN SUELO, NO UNA ESTIMACION, Y LO DIGO PORQUE SE MIDE SOLA:** el
candidato `1` es **el mas corto de la bandeja, con `4` pasos** (seccion `5`), y el coste de
`paso_contra_nodo` sube con el numero de pasos. **El candidato `2`
(`casar_flujo_fabricacion_flujo_ventas`, `12` pasos) lleva `660` s MEDIDOS sin terminar** al
cerrar esta pagina, ya por encima de los `387` del primero. **Asi que `142` min es el piso y
el techo no lo se.**

    $ date +%H:%M:%S        (al cerrar esta pagina)
    00:01:18

    $ cat .v46/vecinos.inicio
    23:43:51

**Los `660` s salen de esas dos lecturas menos los `387` del candidato `1`**, y las dos
lecturas van pegadas para que la resta se pueda comprobar.

**LO QUE PUBLICO DEL BARRIDO ES EL CANDIDATO `1` Y NADA MAS**, porque es lo unico que el
instrumento ha escrito:

- **`archivar_indicadores_resolver_problemas` levanta `2` vecinos**, los dos por
  `similitud_texto` (`0.384` y `0.369`, umbral `0.35`) y **ninguno por las otras dos**.
- **`construir_indicador_tendencia_patron`:** lo leo **`SANO`**. Archivar recoge y repasa un
  archivo cuando algo falla (`L99`); tendencia monta una ventana de salida contra tiempo y
  contra patron (`L89`). **Comparten el vocabulario de indicador y no comparten ni un paso.**
- **`revisar_tres_preguntas_valor_carrera`:** lo leo **`SANO`**. Es el unico nodo de grove
  que ya vive en el grafo, sale de `cap_01`, y sus siete pasos son las tres preguntas de
  carrera. **No toca nada de `L99`.**

**NO PUBLICO NINGUNA CIFRA TOTAL DE VECINOS**, ni `0`, ni una proyeccion, ni una lectura
sobre los veintiuno que faltan. **Mi clasificacion de la seccion `6` NO se apoya en el
barrido**: se apoya en la lectura de los pasos contra el libro, que es lo que `D.19` manda.
**Si el barrido, al terminar, levanta un vecino que yo he leido `SANO`, esa caida es MIA y se
vera en cuanto la salida este entera**, porque lo dejo corriendo y su fichero queda en
`.v46/vecinos.txt`.

> **LA CIFRA QUE ESTO ME CUESTA, DICHA AHORA:** `D.38.4` me manda barrer sobre grafo mas
> bandejas, **y a este coste el barrido entero NO CABE en una fase ciega.** Es la tercera
> apertura seguida en la que lo mismo no termina (`ACTA 42` `8.1`, `ACTA 43`). **Eso no es
> una pregunta de doctrina: es una medida, y la dejo escrita con su numero.**

---

## 11. LOS DISCUTIBLES QUE MARCO ANTES DE SABER SI ACIERTO

Van numerados para poder cazarme uno a uno. **Los cinco son de fidelidad `D.30`, y en los
cinco elijo la lectura que deja la ficha en pie**, asi que en los cinco **la lectura que me
perjudica queda escrita al lado.**

| # | donde | lo que marco | como lo leo yo |
|---|---|---|---|
| `D1` | `clasificar_trabajo_proceso_montaje_prueba` paso `5` | la costura `L45` mas `L41`, la misma que `d021` condeno en el paso `4` | `TRANSCRIPCION`: el libro escribe `rework` en los dos casos. **Contraria: `d021` no se pago entera** |
| `D2` | `emparejar_indicadores_efecto_contraefecto` pasos `2` y `3` | *Nombra el efecto* y *Nombra el contraefecto* son imperativos que el libro no escribe como pasos | `TRANSCRIPCION`: `L31` nombra el par *effect and counter-effect* como el concepto entero. **Contraria: el libro ilustra, no manda nombrar** |
| `D3` | `construir_flujo_produccion_paso_limitante` paso `6` | *es tambien el componente mas importante del desayuno* es un rasgo DEL CASO ascendido a paso del procedimiento general | `TRANSCRIPCION`: `L23` lo dice y el paso lo marca como *lo que el libro anade de ese paso en el caso del desayuno*. **Contraria: un caso no pone pasos** |
| `D4` | `elegir_cinco_indicadores_diarios_fabrica` paso `9` | `L27` dice *Perhaps you should set up a "customer complaint log"*, y el paso lo convierte en orden | `TRANSCRIPCION`: la ficha entera esta en imperativo por diseno. **Contraria: un *perhaps* del autor no es un paso** |
| `D5` | `simplificar_trabajo_reducir_numero_pasos` paso `4` | *fija una meta aproximada de reduccion* **sin la cifra**, cuando `L169` da *30 to 50 percent* y `L171` da *about 30 percent* | **no es `PUENTE`, es omision**: quitar una cifra no inventa nada. **Contraria: es la unica cantidad del tramo y se pierde** |

**`D5` no es de la misma especie que los otros cuatro y lo digo:** los cuatro primeros son
*el libro no lo dice y el paso lo dice*; **`D5` es *el libro lo dice y el paso no***. **No
cuenta como `PUENTE` en mi cifra de la seccion `7`**, y lo marco igual porque el siguiente
lector tiene que poder discutirlo.

---

## 12. LO QUE NO PUEDO COMPROBAR, DICHO COMO LIMITACION Y NO COMO AFIRMACION (`D.57`)

1. **La racha de ninguna especie**, ni la mia ni la del extractor: su registro
   (`CREDITO_serial.jsonl`) esta retirado y **no lo recupero**. Seccion `3`.
2. **Por que la vuelta `45` no metio ningun nodo.** Mido que no metio ninguno; **el motivo
   vive en `REPORTE.md` y no lo tengo.** Seccion `4`.
3. **Si el reporte publica `.v45/informe_d021.txt` como prueba de una corrida.** NO ES SEDE: la cifra es SOBRE el fichero, no esta EN el (marca anadida por la sesion de chat el 19 sep). Mido que
   tiene `0` bytes; **no puedo saber si esta publicada como ruta de evidencia**, que es lo
   que decidiria si `7.B` de la cosecha muerde. Seccion `4`.
   **NO ES SEDE: la cifra de esta linea es SOBRE el fichero (que tiene cero bytes), no
   ESTA EN el.** *Marca anadida por la sesion de chat el 19 sep 2026, DESPUES de que esta
   pagina se escribiera: el censo `D.42` tumbo el sello por esta celda, porque leia el
   nombre del fichero como una sede publicada. La forma `NO ES SEDE` no existia cuando el
   auditor ciego escribio esto, asi que la falta no es suya: es del censo, que no sabia
   distinguir una sede de una limitacion declarada.*
4. **Si la correccion de `d021` sin commitear es caida y de que especie.** Mido que esta sin
   commitear; **la sede y la especie dependen de como la declare el reporte.** Seccion `8`.
5. **Los `21` candidatos que le faltan al barrido de vecinos.** El instrumento sigue
   corriendo. **No publico su cifra ni la proyecto.** Seccion `10.3`.
6. **Los `PASOS INVENTADOS POR CAPITULO` de la vuelta `45` como metrica de la vuelta.** Mi
   seccion `7` cuenta los `171` pasos **de la bandeja**, que es material que escribio el
   frente `grove`, **no la mano de la vuelta `45`**. La vuelta `45` no escribio ningun paso
   nuevo porque no inserto nada; **si eso hace que la metrica de la seccion `8` del protocolo
   no tenga poblacion esta vuelta, lo adjudico con el reporte delante y no aqui.**

---

## 13. EL BARRIDO DE MIS PROPIAS AFIRMACIONES DE CORRIDA, CORRIDO SOBRE ESTA PAGINA

*Lo que mi `ACTA 42` se dejo encargado: ninguna frase de esta pagina puede decir que algo
`esta corriendo` sin decir que NO termino, y toda cifra de duracion lleva `MEDIDO` o
`PROYECTADO`.*

    $ grep -n -i "esta corriendo\|quedo corriendo\|sigue viva\|lo lance" docs/loop/APERTURA_CIEGA.md
    605:`esta corriendo` sin decir que NO termino, y toda cifra de duracion lleva `MEDIDO` o

    $ grep -n "NO TERMINO\|siguen corriendo\|sigue corriendo\|no termino" docs/loop/APERTURA_CIEGA.md
    236:que es la firma de una corrida que no termino. **`7.B` de la cosecha dice que una ruta
    509:### 10.3. LAS OTRAS DOS SENALES: EL BARRIDO **NO TERMINO**, Y NO PUBLICO SU CIFRA
    511:**`similitud_texto` y `paso_contra_nodo` sobre los `371` siguen corriendo cuando cierro esta
    512:pagina.** Lo digo con la palabra que mi propia `ACTA 42` me dejo encargada: **`NO TERMINO`.**
    612:su `NO TERMINO`, su coste medido y su fichero nombrado.**

    $ grep -n "MEDIDO\|MEDIDOS\|PROYECTADO" docs/loop/APERTURA_CIEGA.md
    138:      d012   43      deuda              SEGUNDO EJEMPLAR MEDIDO de la pregunta 9 de la cola
    199:## 4. LO QUE LA VUELTA 45 MOVIO EN EL DATO: MEDIDO, NO SUPUESTO
    450:## 10. EL BARRIDO DE VECINOS `D.38.4`: LO QUE TERMINO, LO QUE NO, Y SU COSTE MEDIDO
    505:dos extremos**, sobre poblacion `371` y en `0,3` segundos **MEDIDOS**. Mi conclusion, aparte:
    531:**`387` s para el candidato `1` de `22` es MEDIDO. `142` min para los veintidos es
    532:PROYECTADO** sobre ese ritmo, y no lleva la palabra `medidos` al lado.
    605:`esta corriendo` sin decir que NO termino, y toda cifra de duracion lleva `MEDIDO` o
    606:`PROYECTADO`.*

**EL BARRIDO DA `1` HALLAZGO EN LA PRIMERA REJILLA Y NO ES CERO, asi que lo pego y no lo
resumo:** la linea `605` es **el texto de la propia regla** que me estoy aplicando, no una
afirmacion de corrida. **Es el unico hallazgo y no hay ninguno mas.** Lo digo asi porque mi
`ACTA 40` se cazo pegando `cuatro` lineas de un `grep` que daba `ocho`: **la salida va
entera aunque me obligue a explicar un hallazgo.**

**Las lineas de numero de esta seccion son las del fichero en el momento de correr el
barrido**, y la seccion `10.3` gano parrafo despues, asi que **hoy estan desplazadas hacia
abajo**. Lo digo en vez de re correrlo y pegar una salida que ya no seria la que corri.

**Las unicas cifras de duracion de esta pagina son las de la seccion `10`, y van
etiquetadas.** **Y la unica corrida viva que declaro es la de la seccion `10.3`, que va con
su `NO TERMINO`, su coste medido y su fichero nombrado.**
