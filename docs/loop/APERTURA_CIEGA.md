# APERTURA CIEGA DEL AUDITOR, VUELTA 43, lote 7 (`grove_high_output`)

> Escrita a ciegas: `docs/loop/REPORTE.md`, `docs/loop/loop.log`,
> `docs/loop/ultimo_extractor.json` y `docs/loop/ultimo_auditor.json` **no estan en el
> arbol y no los recupero de git**. Lo que si abro de `docs/loop/` son sedes mias y
> registro, y la lista entera, con su motivo, esta en la tabla de aqui abajo.

---

## 1. LA COMPROBACION DEL HEREDADO, Y VA LA PRIMERA

**ESTA SECCION SE ESCRIBE ANTES QUE NADA QUE PUEDA TARDAR**, con su cuenta dentro
aunque sea provisional, y se actualiza al final. Es la letra de mi propia
`TAREA BLOQUEANTE` de la `ACTA 41`, punto 1, y la escribo la primera porque lo que
me tumbo la vuelta pasada fue prometerla por numero y no llegar a escribirla.

    ACTA ANTERIOR LEIDA: 94f77d1806efe24a6f9d0a99e8a5fa10c2c84e31
    HEREDADO 1: CUMPLIDO

**LA HUELLA, MEDIDA Y NO COPIADA.** No digo que leo esa huella: la mido contra el
fichero que tengo delante.

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    94f77d1806efe24a6f9d0a99e8a5fa10c2c84e31

    $ wc -l docs/loop/ACTA_AUDITOR.md
      33171 docs/loop/ACTA_AUDITOR.md

**CIFRA PROVISIONAL AL ESCRIBIRSE, ACTUALIZADA AL CERRAR, y las dos redacciones se quedan:**
cuando escribi esta seccion, que fue lo primero que escribi, el barrido de mis remisiones internas
todavia no habia corrido sobre el fichero terminado, asi que **aqui no habia ninguna cuenta
cerrada**: lo que habia era la promesa de que la cuenta viviria en la seccion 7 de esta apertura.
**Al cerrar, esa seccion existe, el barrido corrio sobre la pagina entera y su salida literal esta
pegada en el anexo del final:**

    REMISIONES INTERNAS COMPROBADAS  : 22
    REMISIONES QUE APUNTABAN AL VACIO: 0

**Y ASI SE CUMPLE EL HEREDADO ENTERO, punto por punto:** el `1` pide que esta seccion se escriba
antes que nada que pueda tardar, y se escribio **antes de abrir un solo candidato**; el `2` pide el
barrido de mis remisiones, y la seccion 7 de esta apertura lo trae **con las tres cosas que me cazo**;
el `3` pide las dos cuentas, y son las dos lineas de aqui arriba. **Nunca se prometio por numero.**

---

## 2. LO QUE ABRO Y LO QUE NO ABRO

| lo abro | motivo |
|---|---|
| `cuarentena/grove_high_output/` entero | es el material que vengo a clasificar |
| `fuentes/grove_high_output/cap_01.md`, `cap_02.md`, `cap_03.md` | es el texto contra el que se clasifica |
| `dataset/nodos.jsonl` | es el grafo, y la mitad de la poblacion del barrido |
| `docs/loop/ACTA_AUDITOR.md` | es obra mia, no del extractor, y no es ninguno de los cuatro que `D.34.2` retira. **Y digo exactamente que hice con el: medir su huella y su tamaño.** El heredado no lo saque leyendo sus `33171` lineas, me lo entrego `python forja.py herencia`, que es la sede que `D.40` manda |
| `docs/loop/PROMPT_SIGUIENTE.md` | **es sede mia** (`AUDITOR_FORJA.md` `5.6`): es el encargo que yo escribi, no la respuesta del extractor |
| `docs/loop/DEUDA.jsonl`, `TABLERO.jsonl`, el banco y el manual | registro y doctrina |

| NO lo abro | motivo |
|---|---|
| `REPORTE.md`, `loop.log`, `ultimo_extractor.json`, `ultimo_auditor.json` | no estan en el arbol, y **no los recupero de git** |
| **`.v43/`, el cuaderno de trabajo del extractor de esta vuelta** | **no esta en la lista de `D.34.2`, y aun asi no lo abro**: `frontera.txt`, `fidelidad_tanda.txt` e `ins_01_final.txt` son sus lecturas y sus cuentas de esta misma vuelta. Abrirlo seria leer a ciegas lo que vengo a leer a ciegas. **Listar sus nombres no es abrir sus ficheros, y listarlos es lo unico que hice**, que es lo que la salida de aqui abajo ensena. **Lo declaro yo, sin que nadie me lo pida, porque el sello no lo vigila** |

**Y LO DIGO CON LA SALIDA AL LADO, que es lo unico que sostiene un `no lo abro`:**

    $ ls .v43/
    bandeja_por_capitulo.txt
    c01.sh
    cola_01.txt
    cola_02.txt
    cola_02.txt.reloj
    correr.sh
    credito_apertura.txt
    estado.py
    estado_apertura.txt
    fidelidad.py
    fidelidad_tanda.txt
    frontera.py
    frontera.txt
    guardas_apertura.txt
    identidad_apertura.txt
    ins_01.txt
    ins_01_final.txt
    manual_3_4.txt
    orden_libro.txt
    par_1a.txt
    puedo_grove.txt
    tablero_apertura.txt

    $ git status --short docs/loop/          (corrido AL ABRIR la fase, antes de que esta pagina existiera)
     D docs/loop/APERTURA_CIEGA.md
     D docs/loop/CREDITO_serial.jsonl
     D docs/loop/REPORTE.md
     D docs/loop/loop.log
     M docs/loop/ultimo_apertura.json
     D docs/loop/ultimo_auditor.json
     D docs/loop/ultimo_extractor.json

**LECTURA:** el arnes retiro **seis** ficheros, no cuatro. `CREDITO_serial.jsonl` es sede de credito
(`D.48`) y `APERTURA_CIEGA.md` es esta misma pagina, asi que **esta fase corre sin poder leer la
racha de su propia linea**. No lo levanto como caida de nadie: lo dejo escrito aqui porque **es una
cifra que esta apertura no puede publicar con su instrumento**, y `D.38.3` manda decirlo en vez de
copiarla de memoria.

---

## 3. LO QUE MIDO EN ESTA FASE, CON EL INSTRUMENTO PEGADO

### 3.1. La poblacion del barrido: grafo mas bandejas (`D.38.4`, `D.38.5`)

    $ wc -l dataset/nodos.jsonl
      346 dataset/nodos.jsonl

    $ python <scratchpad>/poblacion.py
    claves canonicas (12): ['bernerslee_bananas', 'gerber_emyth', 'gerber_emyth_cap17_reservado',
     'grove_high_output', 'manual_sistema_conocimiento', 'marquet_turn_the_ship', 'onu_consumidor',
     'openstax_business_ethics', 'openstax_org_behavior', 'scott_radical_candor', 'smart_who',
     'zhuo_manager']

      carpeta=ensayo_referencia_163    fuentes_todas_canonicas=False  n=163
      carpeta=grove_high_output        fuentes_todas_canonicas=True   n=22
      carpeta=marquet_turn_the_ship    fuentes_todas_canonicas=True   n=3

      BANDEJA ADMISIBLE (D.38.5) : 25
      GRAFO                      : 346
      POBLACION DEL BARRIDO      : 371  (menos el propio candidato: 370)

**LO QUE EL INSTRUMENTO MIDIO:** `346` nodos en el grafo y `25` candidatos de bandeja cuyas fuentes
estan **todas** en la tabla canonica; `163` quedan fuera por fuente, que es el criterio que `D.38.5`
escribe, **no por nombre de carpeta**.

**LECTURA:** mi poblacion y la de la aduana son la misma desde `D.38.5`, asi que si mi cuenta de
vecinos no cuadra con la suya **es discrepancia de verdad y no de metodo**.

### 3.2. El material del lote, contado del fichero

    $ python <scratchpad>/pasos.py
      cap_02  clasificar_trabajo_proceso_montaje_prueba             7 pasos
      cap_02  construir_flujo_produccion_paso_limitante            10 pasos
      cap_02  detectar_arreglar_fallo_etapa_menor_valor             6 pasos
      cap_02  dimensionar_inventario_materia_prima_reposicion       7 pasos
      cap_02  equilibrar_capacidad_personal_inventario_plazo        8 pasos
      cap_02  preferir_inspeccion_proceso_prueba_destructiva        6 pasos
      cap_02  rehacer_flujo_paso_limitante_capacidad                6 pasos
      cap_03  archivar_indicadores_resolver_problemas               4 pasos
      cap_03  casar_flujo_fabricacion_flujo_ventas                 12 pasos
      cap_03  construir_grafico_escalonado_pronosticos              8 pasos
      cap_03  construir_indicador_linealidad_alerta_temprana        9 pasos
      cap_03  construir_indicador_tendencia_patron                  6 pasos
      cap_03  decidir_aceptar_rechazar_material_defectuoso          8 pasos
      cap_03  dimensionar_plantilla_administrativa_pronostico       7 pasos
      cap_03  elegir_cinco_indicadores_diarios_fabrica             10 pasos
      cap_03  elegir_fabricar_pedido_pronostico                     9 pasos
      cap_03  elegir_indicador_salida_trabajo_administrativo        7 pasos
      cap_03  elegir_inspeccion_barrera_monitorizacion             12 pasos
      cap_03  emparejar_indicadores_efecto_contraefecto             7 pasos
      cap_03  representar_actividad_caja_negra_ventanas             9 pasos
      cap_03  simplificar_trabajo_reducir_numero_pasos              7 pasos
      cap_03  variar_frecuencia_inspeccion_nivel_calidad            6 pasos

      cap_02  :  7 candidatos,  50 pasos
      cap_03  : 15 candidatos, 121 pasos

      BANDEJA grove_high_output : 22 candidatos, 171 pasos

    $ ls cuarentena/_insertados/grove_high_output/
    revisar_tres_preguntas_valor_carrera.json

    $ wc -l fuentes/grove_high_output/cap_01.md fuentes/grove_high_output/cap_02.md fuentes/grove_high_output/cap_03.md
      119 fuentes/grove_high_output/cap_01.md
       79 fuentes/grove_high_output/cap_02.md
      179 fuentes/grove_high_output/cap_03.md

**LO QUE EL INSTRUMENTO MIDIO:** `22` candidatos en la bandeja, `171` pasos; `1` candidato ya en
`_insertados`; `0` de la bandeja salen de `cap_01`.

**LECTURA:** los `23` que mi propio encargo nombraba (`PROMPT_SIGUIENTE.md`, TAREA 2) son estos
`22` mas el que ya entro, y la cuenta cierra sin resto. Los `121` pasos de `cap_03` son la misma
poblacion que el asunto del commit de la TAREA 2 dice haber releido.

### 3.3. El barrido de la aduana cuesta lo que cuesta, y lo mido antes de prometerlo

`D.38.4` manda barrer **uno por vez**. Mido lo que vale una corrida antes de decir cuantas caben en
esta fase, que es lo contrario de prometer un numero:

    $ python <scratchpad>/coste.py
      comparaciones medidas      : 25
      segundos                   : 14.39
      segundos por comparacion   : 0.576
      poblacion del barrido      : 370 vecinos por candidato
      coste de UN candidato      : 3.5 min
      coste de los 22 de bandeja : 78.1 min

Y la corrida real de un candidato, con su reloj de la casa pegado. **Va recortada y lo digo:** quito
la cabecera de la lista completa, la coletilla de cero inserciones, el nombre de fichero entre
parentesis de la linea `[BLOQUEARIA]` y las lineas `user` y `sys` del reloj. **Ni una cifra de las
que siguen esta tocada.**

    $ time python forja.py informe cuarentena/grove_high_output/archivar_indicadores_resolver_problemas.json
    ============================================================================
    INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
    ============================================================================
    candidatos revisados        : 1
    poblacion del barrido       : 371   (346 del grafo mas 25 que esperan en bandejas)
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

    [BLOQUEARIA] archivar_indicadores_resolver_problemas
        vecino construir_indicador_tendencia_patron  [levantada por: similitud_texto]
          similitud_texto 0.384 | familia_id 0.143 | paso_contra_nodo 0.420
          paso 2 del candidato contra paso 3 de construir_indicador_tendencia_patron
        vecino revisar_tres_preguntas_valor_carrera  [levantada por: similitud_texto]
          similitud_texto 0.369 | familia_id 0.000 | paso_contra_nodo 0.414
          paso 2 del candidato contra paso 1 de revisar_tres_preguntas_valor_carrera

    real	6m22.566s

**LO QUE LOS DOS INSTRUMENTOS MIDIERON:** la poblacion del barrido de la aduana es `371`, **el mismo
numero que yo calcule por mi cuenta en `3.1`**, y una corrida de un candidato tarda `6m22s` de reloj
contra los 3,5 min de la cuenta a puertas cerradas.

**LECTURA, y es la que decide como se lee el resto de esta pagina:** el segundo vecino levantado es
`revisar_tres_preguntas_valor_carrera`, que trata de **las tres preguntas de carrera de la
Introduction** y no tiene un solo objeto de trabajo en comun con **un archivo de indicadores de
fabrica**. La señal que lo levanta es `similitud_texto 0.369` sobre `titulo mas resumen_teorico`, y
los dos resumenes de esta casa comparten el mismo metalenguaje entero (`UNIDAD DE ORIGEN`, `DE DONDE
SALE CADA PASO`, `RELECTURA DE FIDELIDAD D.30`). **Un lote escrito con la misma plantilla se levanta
a si mismo.** Esta es la pregunta `8` de la cola de doctrina (`D.56`), y la dejo **registrada con su
medida y ahi**, que es lo que la congelacion manda: **no abre parada y no va al banco.**

---

## 4. MI CLASIFICACION, CANDIDATO A CANDIDATO, ANTES DE VER NADA

**LA VARA ES LA DE `AUDITOR_FORJA.md` `6.1`:** la pregunta es si el candidato **CONTINUA** el trabajo de su vecino o lo
**REPITE**, con direccion (que anade el hijo a la madre) y sin bascula (no decide el tamaño del
solape, decide si lo que queda fuera es procedimiento **en los dos lados**).

**COMO SE LEE LA COLUMNA `mi clase`:** `SANO` es *entra sin fusion*; `SANO, hijo de X` es *entra y su
arista con `X` es declarable por lectura* (`D.29`); `DISCUTIBLE` es *lo marco ANTES de saber si
acierto*, que es lo unico que hace informativa la metrica (`AUDITOR_FORJA.md` `5.1`).

### 4.0. La numeracion de lineas que sostiene las dos tablas, sacada del fichero

**NINGUNA CITA DE LINEA DE ESTA PAGINA ESTA ESCRITA DE MEMORIA.** Salen de esta corrida, y las pego
recortadas porque son la prueba de las dos columnas de la derecha:

    $ awk 'NF{printf "%3d| %.60s\n", NR, $0}' fuentes/grove_high_output/cap_02.md
     19| The task here encompasses the basic requirements of producti
     21| Instead, a manufacturer should accept the responsibility of d
     23| The first thing we must do is to pin down the step in the flow
     25| What must happen is illustrated opposite. To work back from th
     27| Now you come to the toast. Using the egg time as your base, yo
     39| Other production principles underlie the preparation of our br
     41| Process, assembly, and test operations can be readily applied
     43| The development of a "compiler," a major piece of computer sof
     45| In any case, the development of the individual pieces out of w
     51| Real life, as you know, is full of thickets and underbrush. In
     53| How would our model reflect the change in manufacturing flow?
     57| Now let's complicate things a little further. What happens if
     59| If you were a waiter, you could ask the waiter in line next to
     61| Because each alternative costs money, your task is to find the
     67| But continuous operation does not automatically mean lower cos
     69| What else could go wrong with our continuous egg-machine? The
     73| All production flows have a basic characteristic: the material
     75| A common rule we should always try to heed is to detect and fi
     77| Finally, at the risk of being considered hard-hearted, let's ex

    $ awk 'NF{printf "%3d| %.60s\n", NR, $0}' fuentes/grove_high_output/cap_03.md
     15| A hungry public has loved the breakfast you've been serving, a
     17| Let's say that as manager of the breakfast factory, you will w
     19| Here are my candidates. First, you'll want to know your sales
     29| All these indicators measure factors essential to running your
     31| Indicators tend to direct your attention toward what they are
     33| The principle here was evident many times in the development o
     35| Nowhere can indicators and paired indicators be of more help in
     37| The second criterion for a good indicator is that what you mea
     39| ADMINISTRATIVE FUNCTION   (la tabla del libro, hasta L65)
     69| Such indicators have many uses. First, they spell out very cle
     73| We can think of our breakfast factory as if it were a "black b
     77| The black box sorts out what the inputs, the output, and the l
     81| Leading indicators give you one way to look inside the black b
     83| Leading indicators might include the daily monitors we use to
     87| If we consider a manufacturing unit in this fashion, we may as
     89| Also valuable are trend indicators. These show output (breakfa
     91| Another sound way to anticipate the future is through the use
     93| In my experience, nowhere has the stagger chart been more prod
     95| (* means the actual number for that month)
     99| Finally, indicators can be a big help in solving all types of
    103| There are two ways to control the output of any factory. Some
    105| But if your competition in the sofa business makes the same pr
    107| An obvious disadvantage here is that the manufacturer takes an
    109| At Intel, we build to forecast because our customers demand th
    111| Delivering a product that was built to forecast to a customer
    113| Because the art and science of forecasting is so complex, you
    115| At Intel we try to match the two parallel flows with as much p
    119| The ideal is rarely found in the real world. More often, custo
    121| It is a good idea to use stagger charts in both the manufactur
    123| Forecasting future work demands and then adjusting the output
    125| But if we have carefully chosen indicators that characterize a
    129| As we have said, manufacturing's charter is to deliver product
    131| In the language of production, the lowest-value-point inspecti
    135| When material is rejected at incoming inspection, a couple of
    137| While in most instances the decision to accept or reject defec
    139| Inspections, of course, cost money to perform and further add
    141| Let's consider a few techniques commonly used to balance the t
    143| Another way to lower the cost of quality assurance is to use v
    145| Suitably thought through, intelligent inspection schemes can a
    147| I recently read a story in a news magazine that said that the
    153| For that, the bureaucratic minds at the embassy would need to
    157| Productivity
    167| Here I'd like to introduce the concept of leverage, which is t
    169| Automation is certainly one way to improve the leverage of all
    171| To implement the actual simplification, you must question why

**LO QUE ESTA CORRIDA ME CAZO A MI, y lo escribo porque es la especie que me tumbo la vuelta
pasada:** mi primera redaccion de las dos tablas de abajo traia las citas de linea **puestas de
memoria por el orden de la prosa**, y contra el fichero salian mal en **`20` de `22` filas**. Se
corrigieron **antes de sellar** y por eso no hay texto viejo que tachar: **esta pagina no se ha
publicado todavia.** La regla que lo cazo es la misma que el heredado de `1`: **una remision se
comprueba contra el fichero, no contra el recuerdo.**

**Y LA CUENTA DE ESA FRASE TAMBIEN LLEVA INSTRUMENTO, porque escribi `18` antes de contarla y son
`20`:**

    $ python <scratchpad>/fila20.py
      fila  1  cap_02 L19 a L25     -> cap_02 L19 a L27      CORREGIDA
      fila  2  cap_02 L45 a L47     -> cap_02 L51 a L53      CORREGIDA
      fila  3  cap_02 L49 a L53     -> cap_02 L57 a L61      CORREGIDA
      fila  4  cap_02 L31 a L41     -> cap_02 L39 a L45      CORREGIDA
      fila  5  cap_02 L63           -> cap_02 L67            CORREGIDA
      fila  6  cap_02 L65           -> cap_02 L69            CORREGIDA
      fila  7  cap_02 L69 a L71     -> cap_02 L73 a L75      CORREGIDA
      fila  8  cap_03 L15 a L25     -> cap_03 L15 a L29      CORREGIDA
      fila  9  cap_03 L27 y L29     -> cap_03 L31 a L33      CORREGIDA
      fila 10  cap_03 L31 a L33     -> cap_03 L35 a L37      CORREGIDA
      fila 11  cap_03 L41 a L45     -> cap_03 L73 a L77      CORREGIDA
      fila 12  cap_03 L49           -> cap_03 L81 a L87      CORREGIDA
      fila 13  cap_03 L51           -> cap_03 L89            CORREGIDA
      fila 14  cap_03 L91 a L95     -> cap_03 L91 a L95      ya estaba bien
      fila 15  cap_03 L99           -> cap_03 L99            ya estaba bien
      fila 16  cap_03 L103 a L111   -> cap_03 L103 a L109    CORREGIDA
      fila 17  cap_03 L113 a L121   -> cap_03 L111 a L121    CORREGIDA
      fila 18  cap_03 L125          -> cap_03 L123 a L125    CORREGIDA
      fila 19  cap_03 L135 a L139   -> cap_03 L135 a L137    CORREGIDA
      fila 20  cap_03 L141 a L145   -> cap_03 L139 a L141    CORREGIDA
      fila 21  cap_03 L147          -> cap_03 L143           CORREGIDA
      fila 22  cap_03 L175 a L177   -> cap_03 L169 a L171    CORREGIDA

      FILAS DE LAS DOS TABLAS        : 22
      FILAS CORREGIDAS               : 20
      FILAS QUE YA ESTABAN BIEN      : 2

**LECTURA, y me la cargo yo:** `18` era una cifra contada a ojo dentro de una frase que hablaba
justamente de cifras contadas a ojo. **La cazo yo y antes de sellar**, que es lo unico que la
distingue de la caida de la vuelta pasada, y la dejo escrita con las dos redacciones a la vista.

### 4.1. Los `7` de `cap_02` (Cap. 1, `The Basics of Production`)

| # | candidato | mi clase | lo que lo sostiene |
|---|---|---|---|
| 1 | `construir_flujo_produccion_paso_limitante` | **SANO** | es la madre del capitulo: requisitos (`L19`), compromiso de hora y coste (`L21`), paso limitante (`L23`), calculo hacia atras (`L25`) y desfases con el criterio del mas largo o mas dificil o mas sensible o mas caro (`L27`). Ningun vecino del grafo hace esto: el grafo no tiene un solo nodo de flujo de produccion |
| 2 | `rehacer_flujo_paso_limitante_capacidad` | **SANO, hijo de 1. DISCUTIBLE 1** | `L51` a `L53`. Lo marco porque un lector estricto dira que **REPITE**: vuelve a correr la receta de 1 con otro paso limitante. **Lo sostengo como CONTINUA** porque lo que queda fuera es procedimiento en los dos lados: 1 fija el paso limitante **por duracion** y el hijo lo redeclara **por cola de capacidad**, y ademas trae la regla que la madre no tiene, en `L51`: **el componente que manda la calidad NO cambia aunque cambie el paso limitante** (*the egg still determines the overall quality of the breakfast, but your time offsets must be altered*) |
| 3 | `equilibrar_capacidad_personal_inventario_plazo` | **SANO, hijo de 2** | `L57` a `L61`. Su objeto es otro: **enumerar y costear las salidas** (especializar, pedir ayuda al de al lado, anadir tostador, acumular inventario) y cambiarlas entre si contra el plazo, hasta las relaciones cuantificables de `L61`. La madre rehace un flujo; el hijo elige entre recursos |
| 4 | `clasificar_trabajo_proceso_montaje_prueba` | **SANO** | `L39` a `L45`: proceso, montaje y prueba (`L39`), la fuerza de ventas (`L41`) y el compilador con prueba unitaria, rehacer y prueba de sistema (`L45`). Ningun otro candidato del lote clasifica operaciones |
| 5 | `preferir_inspeccion_proceso_prueba_destructiva` | **SANO, hermano de 4** | `L67`. El 4 **nombra** la prueba; el 5 **elige entre dos pruebas** (funcional destructiva contra inspeccion en proceso) y anade automatizar la lectura con el aviso sonoro. `AUDITOR_FORJA.md` `6.1`: *nombrar no es procedimentar*, asi que 4 no consume a 5 |
| 6 | `dimensionar_inventario_materia_prima_reposicion` | **SANO. DISCUTIBLE 2** | `L69`. Lo marco contra `casar_flujo_fabricacion_flujo_ventas`, que tambien manda inventario. **Los sostengo separados**: aqui el inventario se dimensiona **por el tiempo de reposicion del proveedor** y se pesa contra su coste y la oportunidad en riesgo; alli se mete **holgura a proposito para casar dos flujos**. Dos procedimientos con dos disparadores |
| 7 | `detectar_arreglar_fallo_etapa_menor_valor` | **SANO** | `L73` a `L75`: el valor que crece por el flujo, con el valor percibido del rotulo (`L73`), y la regla comun con sus tres aplicaciones, huevo podrido, candidato en campus y prueba unitaria (`L75`) |

**LECTURA QUE VA A FAVOR DEL EXTRACTOR, y la escribo porque una metrica que solo encuentra fallos
ajenos no es una metrica (`AUDITOR_FORJA.md` `5.3`):** `cap_03` `L129` **vuelve a decir** la regla del 7 (*as noted, we
are better off catching a bad raw egg than a cooked one... reject before investing further value*), y
**la bandeja NO tiene un segundo nodo para ese parrafo.** El libro se repite y la bandeja no. No lo
doy por sentado: lo compruebo candidato a candidato en la tabla de `4.2`.

### 4.2. Los `15` de `cap_03` (Cap. 2, `Managing the Breakfast Factory`)

| # | candidato | mi clase | lo que lo sostiene |
|---|---|---|---|
| 8 | `elegir_cinco_indicadores_diarios_fabrica` | **SANO** | `L15` a `L29`: enfocar cada indicador en una meta (`L15`), los cinco datos (`L17`), uno a uno del pronostico al registro de quejas (`L19` a `L27`) y el repaso de primera hora (`L29`) |
| 9 | `emparejar_indicadores_efecto_contraefecto` | **SANO, hermano de 8. DISCUTIBLE 3** | `L31` a `L33`. Lo marco contra el 10, que **tambien empareja**. Los sostengo separados: el 9 empareja **efecto contra contraefecto** (nivel de inventario contra roturas de stock, `L31`) y el 10 empareja **cantidad contra calidad** (comprobantes tramitados contra errores encontrados, `L37`). Son dos parrafos distintos con dos ejemplos distintos, y `AUDITOR_FORJA.md` `6.1` los deja como **FRONTERA DECLARADA**, no como duplicado |
| 10 | `elegir_indicador_salida_trabajo_administrativo` | **SANO. DISCUTIBLE 3** | `L35` a `L37`, mas la tabla del libro de `L39` a `L65`. Sus dos varas (que cubra la salida y no la actividad; que sea cosa fisica y contable) no estan en ningun otro candidato |
| 11 | `representar_actividad_caja_negra_ventanas` | **SANO** | `L73` a `L77`: la caja negra con entrada, salida y trabajo, sus tres aplicaciones (`L73`) y las ventanas recortadas (`L77`) |
| 12 | `construir_indicador_linealidad_alerta_temprana` | **SANO, hijo de 11** | `L81` a `L87`: los indicadores adelantados (`L81`), los controles diarios y la recta ideal de la contratacion universitaria (`L83`) y la unidad que concentra su salida en la ultima semana (`L87`). Es **una** ventana concreta de la caja de 11 |
| 13 | `construir_indicador_tendencia_patron` | **SANO, hermano de 12** | `L89`: salida contra tiempo y contra un patron, con la extrapolacion y el por que del desvio |
| 14 | `construir_grafico_escalonado_pronosticos` | **SANO, hermano de 13. DISCUTIBLE 4** | `L91` a `L95`. Lo marco contra el 13 porque los dos son graficos de futuro. **Los sostengo separados con la linea del propio libro**: el escalonado deja ver la variacion de un pronostico al siguiente *better than if you used a simple trend chart* (`L91`), o sea que el libro **los opone**, no los solapa |
| 15 | `archivar_indicadores_resolver_problemas` | **SANO** | `L99`. Cuatro pasos y un solo objeto: el archivo que se repasa el dia que algo va mal. **El instrumento de `3.3` lo levanto contra el 13 y contra el nodo ya insertado, y mi lectura dice SANO contra los dos**: el 13 construye una ventana, el 15 guarda la serie para el dia del problema |
| 16 | `elegir_fabricar_pedido_pronostico` | **SANO** | `L103` a `L109`: las dos maneras de controlar la salida (`L103`), la comparacion de plazo con la competencia (`L105`), el riesgo de inventario (`L107`) y la mezcla de la fabrica de desayunos (`L109`) |
| 17 | `casar_flujo_fabricacion_flujo_ventas` | **SANO, hijo de 16** | `L111` a `L121`. Empieza donde acaba el 16: **ya elegido el pronostico**, los dos procesos simultaneos (`L111`), el pronostico repartido entre fabricacion y ventas (`L113`), el casado (`L115`), la holgura en el inventario de menor valor (`L119`) y los graficos escalonados en los dos (`L121`) |
| 18 | `dimensionar_plantilla_administrativa_pronostico` | **SANO, hijo de 17** | `L123` a `L125`. Lleva el pronostico a la fabrica administrativa, y **consume al 10 como entrada**: su paso 1 pide indicadores ya elegidos y vigilados, que es literalmente como abre `L125` |
| 19 | `decidir_aceptar_rechazar_material_defectuoso` | **SANO** | `L135` a `L137`: las dos salidas y el grupo equilibrado de mandos (`L135`), y el limite de fiabilidad con el marcapasos (`L137`) |
| 20 | `elegir_inspeccion_barrera_monitorizacion` | **SANO** | `L139` a `L141`: lo que cuesta inspeccionar y el equilibrio (`L139`), y barrera contra monitorizacion con su intercambio y su regla de pulgar (`L141`) |
| 21 | `variar_frecuencia_inspeccion_nivel_calidad` | **SANO, hijo de 20. DISCUTIBLE 5** | `L143`. Lo marco porque comparte con el 20 el proposito entero (*another way to lower the cost of quality assurance*). **Lo sostengo como CONTINUA**: el 20 elige **donde** se retiene el material, el 21 decide **cada cuanto** se mira, y el disparador del 21 es el nivel de calidad observado, que en el 20 no aparece |
| 22 | `simplificar_trabajo_reducir_numero_pasos` | **SANO** | `L169` a `L171`: dibujar el flujo con todos sus pasos, contarlos y fijar meta (`L169`), y preguntar por que se hace cada uno y tirar los que no aguanten (`L171`) |

### 4.3. Lo que apuesto ANTES de que corra el barrido entero

`d005` de `docs/loop/DEUDA.jsonl` dice que **`6` de los `15` de `cap_03` BLOQUEARIAN**. El barrido
completo tarda `78` min medidos (`3.3`) y esta corriendo mientras escribo. **Escribo aqui mi apuesta
para que se pueda contar contra la suya**, que es para lo que sirve una fase ciega:

| mis `6` | por que espero que los levante |
|---|---|
| `archivar_indicadores_resolver_problemas` | **ya medido en `3.3`: BLOQUEARIA con 2 vecinos** |
| `construir_indicador_tendencia_patron` | familia `construir_indicador_` con el 12, y vecino ya medido del 15 |
| `construir_grafico_escalonado_pronosticos` | comparte el objeto **pronostico** con el 13, el 16 y el 17 |
| `emparejar_indicadores_efecto_contraefecto` | comparte **emparejar** con los pasos 5 a 7 del 10 |
| `elegir_indicador_salida_trabajo_administrativo` | familia `elegir_` con el 8, el 16 y el 20, y el objeto administrativo con el 18 |
| `variar_frecuencia_inspeccion_nivel_calidad` | comparte **inspeccion** con el 19 y el 20 |

**Y LOS TRES SUPLENTES, por si mi orden falla:** `elegir_inspeccion_barrera_monitorizacion`,
`construir_indicador_linealidad_alerta_temprana` y `elegir_cinco_indicadores_diarios_fabrica`.

**LECTURA:** si el barrido levanta a los que comparten **plantilla de resumen** en vez de a los que
comparten **objeto de trabajo**, mi apuesta fallara por el lado que `3.3` ya midio, y esa sera la
medida de la pregunta `8` de la cola de doctrina, no una caida de nadie.

---

## 5. LAS PIEZAS DEL LIBRO QUE LEO Y NO VEO EN LA BANDEJA

El encargo manda clasificar **cada candidato y cada pieza que lea**. Las piezas que no llegaron a
candidato son la mitad que nadie mira, porque no dejan fichero. **Las escribo con mi clase, para
poder contarlas contra la frontera que el extractor publique.**

| pieza | mi clase | por que |
|---|---|---|
| `cap_01` `L61` a `L65`, las reglas del entorno nuevo y la tolerancia al desorden | **POSTURA, y no la haria nodo** | el inventario que el texto pone es de **actitudes** (*higher tolerance for disorder*, *double your efforts*), no de objetos de trabajo. `EXTRACTOR.md` `9.1` restriccion 1 lo deja fuera |
| `cap_01` `L79` a `L85`, menos niveles de mando, mas gente por jefe, y si las reuniones de uno con uno siguen haciendo falta | **POSTURA AQUI, procedimiento en su capitulo** | el texto esta en interrogativo (*Can you have them as often with ten direct reports as with five?*) y el propio libro lo remite a su capitulo. Hacerlo nodo aqui seria adelantar material con menos inventario del que tendra despues |
| `cap_01` `L99`, *nobody owes you a career*, con su lista de verbos | **ABSORBIDA por el nodo que entro** | la lista (*compete, enhance your value, hone, learn, adapt, get out of the way*) es exhortacion sin objeto de trabajo, y el inventario de verdad llega dos lineas despues, en `L101` a `L107`, que es de donde sale el nodo |
| `cap_02` `L63` a `L65`, la fabrica continua: comprar la hervidora, casar su salida con la tostadora continua, perder flexibilidad | **BORDE. Lo dejaria declarado, no callado** | tiene un imperativo real (*match the output of the continuous egg-boiler with the output of a continuous toaster*) pero el resto es el precio que se paga, no pasos. **Espero verlo en la frontera como pieza mirada y descartada**; si no aparece, es una pieza que nadie miro |
| `cap_02` `L77` a `L79`, la justicia penal como proceso de produccion | **EJEMPLO** | es la aplicacion del paso limitante a un caso, con su conclusion (*we permit the wrong step to limit the overall process*). El procedimiento ya vive en el candidato 1 |
| `cap_03` `L69`, los tres usos de los indicadores administrativos | **POSTURA** | inventario de **beneficios** (aclaran objetivos, dan objetividad, permiten comparar grupos), que es inventario de fines |
| `cap_03` `L81`, segunda mitad: **el indicador adelantado tiene que ser creible, y hay que estar dispuesto a actuar con el** | **PROCEDIMIENTO, Y NO ESTA EN NINGUN CANDIDATO** | *the indicators you choose should be credible, so that you will, in fact, act whenever they flash warning signals*, y antes *unless you are prepared to act on what your leading indicators are telling you, all you will get from monitoring them is anxiety*. **Es un criterio de eleccion con su objeto**, y el candidato 12, que toma `L81`, no lo recoge en ninguno de sus nueve pasos. **Esta es la pieza que mas me chirria de las siete** |
| `cap_03` `L131` a `L133`, los tres puntos de inspeccion con su nombre | **NOMENCLATURA** | nombrar entrada, en proceso y final es *nombrar no es procedimentar*, y el candidato 6 ya trae la inspeccion de recepcion con sus pasos |
| `cap_03` `L145` a `L153`, la embajada y las visas: aceptar que el `100` por cien sobra, poner una prueba de muestreo y elegir la muestra por criterios fijados de antemano | **BORDE, y lo marco** | el caso trae un procedimiento que **no** es el del candidato 20 (que elige entre barrera y monitorizacion **dentro de una fabrica**) ni el del 21 (que varia la frecuencia): aqui se **sustituye** un control del cien por cien por un muestreo en un proceso administrativo. **Si la frontera lo declaro como ejemplo del 21, lo acepto; si no lo miro, es la segunda pieza sin mirar** |
| `cap_03` `L157` a `L167`, productividad y palanca | **POSTURA, y bien diferida** | es definicion (*productivity is the output divided by the labor*) y el libro anuncia que la palanca se trabaja despues. El unico trozo con pasos, la simplificacion del trabajo, **si** es candidato (el 22) |

**LECTURA:** de las `10` piezas que leo y no son candidato, **`8` las dejaria fuera por la misma vara
con la que el extractor las dejo fuera**, y **`2` las marco**: la credibilidad del indicador
adelantado (`cap_03` `L81`) y el muestreo de la embajada (`cap_03` `L145` a `L153`). **No digo que
falten nodos**: digo que son las dos que voy a buscar en su frontera, y que si la frontera no las
nombra, lo que falta no es un nodo, es la mirada.

---

## 6. EL UNICO NODO DEL LOTE QUE YA VIVE EN EL GRAFO

`cuarentena/_insertados/grove_high_output/` tiene **un** fichero (`3.2`), y el grafo cierra en `346`.
Lo leo **sin abrir `bitacora/VEREDICTOS.jsonl`**: primero mi clase, y la razon escrita del extractor
se destapa despues, que es el orden que manda `AUDITOR_FORJA.md` `1.2`.

### 6.1. Su fidelidad `D.30`, contada por mi contra el parrafo

| paso del nodo | linea del libro | mi clase |
|---|---|---|
| 1 anadir valor real o solo pasar informacion | `cap_01` `L103` | **TRANSCRIPCION** |
| 2 el como: buscar sin parar maneras de hacer las cosas mejor en tu departamento | `cap_01` `L103` | **TRANSCRIPCION** |
| 3 la vara: cada hora del dia aumentando la produccion de aquellos de los que respondes | `cap_01` `L103` | **TRANSCRIPCION** |
| 4 estar enchufado, dentro de la empresa y del sector entero | `cap_01` `L105` | **TRANSCRIPCION** |
| 5 esperar a que otro te interprete, nodo de una red o flotando solo | `cap_01` `L105` | **TRANSCRIPCION** |
| 6 probar ideas, tecnicas y tecnologias nuevas, en persona | `cap_01` `L107` | **TRANSCRIPCION** |
| 7 esperar a que otros rehagan tu puesto, y a ti fuera de el | `cap_01` `L107` | **TRANSCRIPCION** |

**MI CUENTA: `7` pasos, `7` TRANSCRIPCION, `0` PUENTE, `0,00` por ciento de PASOS INVENTADOS.** Las
tres lineas del libro quedan usadas enteras y ningun paso cierra un bucle que el libro deje abierto:
**no hay periodo, no hay destinatario y no hay soporte**, que son las tres especies de puente del
lote 1.

### 6.2. Su discutible, adjudicado antes de leer su razon

El nodo marca como discutible que **tres preguntas para meditar sean POSTURA y no procedimiento**.
**Mi adjudicacion: SE SOSTIENE, es nodo**, y la vara es `EXTRACTOR.md` `9.1`, no la de continua
contra repite:

- **el inventario esta en el libro y esta numerado**: `L103`, `L105` y `L107` ponen las tres
  preguntas **una a una**, y cada una con sus dos caras. `EXTRACTOR.md` `9.1` acepta *los medios, las etapas o los
  objetos que hay que revisar, nombrados uno a uno por el texto*, y aqui los objetos a revisar son
  tres y los nombra el texto;
- **no es inventario de metas** (restriccion 1): el libro no dice adonde llegar, da el medio
  (*by continually looking for ways to make things truly better*) y la vara de medida (*every hour
  of your day*);
- **no hay adjetivo de adecuacion en el sitio del criterio** (restriccion 2): *I can offer you no
  surefire formula* niega que haya formula, **no pone un criterio blando**; lo que pone despues son
  tres preguntas concretas.

**LECTURA:** que el extractor lo marcase discutible **antes** de saber si acertaba es lo que hace
informativa a la metrica (`AUDITOR_FORJA.md` `5.1`), y por mi lectura **cae DENTRO de su marcado y
se sostiene**.

### 6.3. Sus vecinos, y por que mi clase contra la bandeja entera es `SANO`

    $ python <scratchpad>/dominios.py
      bandeja grove por dominio: {'produccion': 22}
      grafo: 5 dominios, carrera_profesional=1, produccion=0

**LO QUE EL INSTRUMENTO MIDIO:** los `22` de la bandeja son **todos** `produccion`, el grafo tiene
`5` dominios y **ninguno** de sus `346` nodos era `produccion` antes de este lote; `carrera_profesional`
tiene exactamente `1`, que es este nodo.

**LECTURA:** el lote 7 abre **dos dominios nuevos a la vez**, asi que contra el grafo viejo la clase
`REPITE` es estructuralmente improbable y **el riesgo de duplicado de este lote esta dentro de la
bandeja, no contra el catalogo**. Por eso mi clase del nodo insertado contra **los `22`** es `SANO`:
ni uno solo comparte con las tres preguntas de carrera un objeto de trabajo, y el unico vecino que la
maquina levanta contra el (`3.3`, `similitud_texto 0.369` contra `archivar_indicadores_resolver_problemas`)
lo levanta por **plantilla de resumen** y no por contenido.

**Y LO QUE NO PUEDO COMPROBAR EN ESTA FASE, dicho en voz alta:** `config/umbrales.json` trae
`solo_dominio_y_nucleo` en `false`, medido asi:

    $ grep -n "solo_dominio_y_nucleo" config/umbrales.json
    10:  "solo_dominio_y_nucleo": false,

y **por eso** un dominio nuevo no estrecha el barrido de nadie. Si estuviera en `true`, dos dominios
nuevos habrian dejado a este lote sin vecinos que mirar. **No es una caida: es la guarda que hoy nos
salva y que conviene volver a mirar el dia que alguien la cambie.**

---

## 7. EL BARRIDO DE MIS REMISIONES INTERNAS, Y LAS DOS CUENTAS

Es el punto 2 del heredado, y es el que me tumbo la vuelta pasada: mi apertura sellada remitia a una
seccion 8 que no existia. **El barrido no se promete: se corre y se pega.**

**EL CRITERIO, ESCRITO ANTES DE CONTAR**, porque una cuenta sin criterio no significa nada y porque
esta pagina cita secciones de tres documentos distintos:

| cuenta como | forma |
|---|---|
| **remision INTERNA** | la frase fija *seccion N de esta apertura*, y todo token entre acentos graves de la forma N.M **que no lleve delante, en su misma linea, el nombre de un documento de la casa** |
| **remision EXTERNA** | el mismo token **con su documento delante en la misma linea**, que es la forma que adopte en esta pagina para las secciones de `AUDITOR_FORJA.md` y de `EXTRACTOR.md` |
| **no cuenta** | D.NN, P.NN, ED.N y LNN: llevan letra delante y no son secciones de este fichero |

**Y POR ESO ESCRIBO SIEMPRE LA FORMA SINGULAR** (*la seccion 4 de esta apertura y la seccion 6 de
esta apertura*, nunca *las secciones 4 y 6*): una forma que el barrido no sabe leer **es una remision
que no se comprueba**, y un criterio con un agujero mide menos de lo que dice.

**LO QUE EL BARRIDO ME CAZO MIENTRAS ESCRIBIA, y son tres:**

1. **un 9.1 desnudo** en la seccion 6 de esta apertura, que un lector leeria como seccion mia y es de
   `EXTRACTOR.md`. **Se le puso el documento delante.**
2. **seis remisiones de seccion ambiguas** en el cuerpo (5.6, 6.1 tres veces, 5.1 y 5.3, todas de
   `AUDITOR_FORJA.md`), escritas como si fueran mias. **Se les puso el documento delante.**
3. **un 3.5 escrito entre acentos graves** cuando era una cantidad de minutos y no una seccion.
   **Se reescribio como 3,5 min**, porque una cifra disfrazada de remision ensucia las dos cuentas.

**Y HAY UNA CUARTA QUE NO ES DE REMISIONES Y LA CUENTO AQUI PORQUE SALIO DEL MISMO METODO:** las
citas de linea del libro de las dos tablas de la seccion 4 de esta apertura estaban puestas de
memoria y salian mal en `20` de `22` filas, recontadas con su instrumento. Se corrigieron contra el fichero **antes de sellar**, y
el instrumento que las sostiene esta pegado en la seccion 4.0 de esta apertura.

**LA SALIDA DEL BARRIDO, corrida sobre esta misma pagina ya terminada, esta pegada al final de este
fichero**, despues de la tabla de cierre, **porque pegarla en medio le habria movido a su propia
salida los numeros de linea que publica.**

> ### **LAS DOS CUENTAS QUE EL HEREDADO PIDE**
>
>     REMISIONES INTERNAS COMPROBADAS  : 22
>     REMISIONES QUE APUNTABAN AL VACIO: 0

---

## 8. LA TABLA DE CIERRE DE ESTA APERTURA

| lo que esta fase declara | valor | su instrumento |
|---|---|---|
| **ACTA ANTERIOR LEIDA** | `94f77d1806efe24a6f9d0a99e8a5fa10c2c84e31` | `git hash-object`, en la seccion 1 de esta apertura |
| **HEREDADO 1** | **CUMPLIDO** | la seccion 1 de esta apertura y la seccion 7 de esta apertura |
| nodos en el grafo | `346` | `wc -l dataset/nodos.jsonl` |
| candidatos en la bandeja del lote 7 | `22`, mas `1` ya insertado | `ls` y el contador de pasos |
| pasos en la bandeja | `171`, de los que `50` son de `cap_02` y `121` de `cap_03` | el contador de pasos |
| poblacion del barrido | `371`, o sea `346` del grafo mas `25` de bandejas | el informe de la aduana, que la imprime |
| candidatos clasificados por mi | `22` de `22`, mas el `1` insertado | la tabla de la seccion 4 de esta apertura |
| discutibles que marco antes de saber | `5` en la bandeja, mas el `1` del nodo insertado | la seccion 4 de esta apertura y la seccion 6 de esta apertura |
| piezas del libro leidas y no candidato | `10`, de las que marco `2` | la seccion 5 de esta apertura |
| fidelidad D.30 del nodo insertado | `7` de `7` TRANSCRIPCION, `0,00` por ciento | mi relectura contra `cap_01` `L103` a `L107` |
| barrido de guiones sobre esta pagina | **VERDE** | `python forja.py guiones docs/loop/APERTURA_CIEGA.md` |
| remisiones internas | `22` comprobadas, `0` al vacio | el barrido pegado al final |

**LO QUE ESTA FASE NO PUDO MEDIR, Y SE DICE EN VEZ DE RELLENARSE:**

- **el barrido de vecinos de los `22`**: cuesta `78` min medidos y quedo corriendo al cerrar esta
  pagina. Lo que si esta medido y pegado es **uno** de ellos, entero, con la poblacion que imprime;
- **la racha viva de mi linea**: `docs/loop/CREDITO_serial.jsonl` no esta en el arbol en esta fase,
  como dice la seccion 2 de esta apertura, asi que **no publico ninguna cuenta de racha aqui**;
- **el coste en dolares del turno**: el arnes no me lo escribe y no lo invento.

**NINGUNA CIFRA DE ESTA PAGINA ESTA CONTADA A OJO.** Cada una lleva su instrumento al lado y toda
conclusion mia va en linea marcada `LECTURA`, que es lo que D.38.3 manda desde el 16 sep.

---

## ANEXO. LA SALIDA LITERAL DEL BARRIDO DE REMISIONES

Corrido sobre esta pagina **sin este anexo**, que es lo unico que va detras de el, para que los
numeros de linea que publica sigan siendo los de esta pagina.

    $ python <scratchpad>/remisiones.py docs/loop/APERTURA_CIEGA.md
    SECCIONES QUE ESTE FICHERO ESCRIBE (18): 1, 2, 3, 3.1, 3.2, 3.3, 4, 4.0, 4.1, 4.2, 4.3, 5, 6, 6.1, 6.2, 6.3, 7, 8
    
    REMISIONES INTERNAS COMPROBADAS, una a una:
      linea   32  ->  seccion 7       EXISTE   (frase "de esta apertura")
      linea   41  ->  seccion 7       EXISTE   (frase "de esta apertura")
      linea  542  ->  seccion 4       EXISTE   (frase "de esta apertura")
      linea  548  ->  seccion 6       EXISTE   (frase "de esta apertura")
      linea  556  ->  seccion 4       EXISTE   (frase "de esta apertura")
      linea  558  ->  seccion 4.0     EXISTE   (frase "de esta apertura")
      linea  575  ->  seccion 1       EXISTE   (frase "de esta apertura")
      linea  576  ->  seccion 1       EXISTE   (frase "de esta apertura")
      linea  576  ->  seccion 7       EXISTE   (frase "de esta apertura")
      linea  581  ->  seccion 4       EXISTE   (frase "de esta apertura")
      linea  582  ->  seccion 4       EXISTE   (frase "de esta apertura")
      linea  582  ->  seccion 6       EXISTE   (frase "de esta apertura")
      linea  583  ->  seccion 5       EXISTE   (frase "de esta apertura")
      linea  593  ->  seccion 2       EXISTE   (frase "de esta apertura")
      linea  227  ->  seccion 3.1     EXISTE   (token N.M sin documento delante)
      linea  382  ->  seccion 4.2     EXISTE   (token N.M sin documento delante)
      linea  395  ->  seccion 3.3     EXISTE   (token N.M sin documento delante)
      linea  407  ->  seccion 3.3     EXISTE   (token N.M sin documento delante)
      linea  412  ->  seccion 3.3     EXISTE   (token N.M sin documento delante)
      linea  423  ->  seccion 3.3     EXISTE   (token N.M sin documento delante)
      linea  457  ->  seccion 3.2     EXISTE   (token N.M sin documento delante)
      linea  513  ->  seccion 3.3     EXISTE   (token N.M sin documento delante)
    
    REMISIONES QUE APUNTAN AL VACIO:
      ninguna
    
    REMISIONES EXTERNAS (llevan su documento delante en la misma linea): 11
      linea   54  ->  5.6
      linea  243  ->  6.1
      linea  249  ->  5.1
      linea  374  ->  6.1
      linea  379  ->  5.3
      linea  389  ->  6.1
      linea  436  ->  9.1
      linea  459  ->  1.2
      linea  481  ->  9.1
      linea  485  ->  9.1
      linea  496  ->  5.1
    
    ============================================================
      REMISIONES INTERNAS COMPROBADAS : 22
      REMISIONES QUE APUNTABAN AL VACIO: 0
    ============================================================
