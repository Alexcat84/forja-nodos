# APERTURA CIEGA, vuelta 1 de la corrida nueva (linea `serial`, rama `extraccion-mundo-11`)

*Escrita a ciegas el 19 sep 2026, ANTES de que el arnes me exponga el reporte del
extractor. Sella el arnes; yo no commiteo.*

---

## 1. LA DECLARACION QUE EL ARNES EXIGE (`D.40`)

    ACTA ANTERIOR LEIDA: 8fd9fc9094f880ab4f77775885baaf2c7eef815f

**Y NO ME LA CREO DE MEMORIA: LA MIDO.** La huella que el prompt me entrega es la del
fichero que tengo delante, y eso lo dice el instrumento y no yo:

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    8fd9fc9094f880ab4f77775885baaf2c7eef815f

    $ python forja.py herencia
      acta anterior : ACTA 43. VUELTA 44, lote 7 (grove_high_output) ...
      su huella     : 8fd9fc9094f880ab4f77775885baaf2c7eef815f
      heredados     : 0

**HEREDADOS: `0`.** No escribo ningun `HEREDADO n:` porque no hay ninguno que declarar, y
el propio instrumento lo dice en su ultima linea (*El acta anterior no dejo ninguna tarea
bloqueante ni ningun remedio escrito*). La `ACTA 43` cerro con parada por credito roto, no
con encargo.

---

## 2. LO QUE EL ARNES ME RETIRO, COMPROBADO EN SU PROPIO REGISTRO

`docs/loop/loop.log` **no se retira**, asi que la linea de mi turno la leo yo:

    [2026-09-19 00:12:33] VUELTA 1 : APERTURA CIEGA (claude-opus-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl
    [2026-09-19 00:12:33]   hereda 0 remedio(s) del acta anterior, entregados en el prompt (D.40)

| fichero | estado que mido | forma `D.42` |
|---|---|---|
| `docs/loop/REPORTE.md` | fuera del arbol | NO ES SEDE: retirado por el arnes para esta fase; lo nombro para decir que no lo he abierto |
| `docs/loop/ultimo_extractor.json` | fuera del arbol | NO ES SEDE: retirado por el arnes; es el resumen que `D.34.2` retira por ser peor que el reporte |
| `docs/loop/ultimo_auditor.json` | fuera del arbol | NO ES SEDE: retirado por el arnes |
| `docs/loop/CREDITO_serial.jsonl` | fuera del arbol, `40874` bytes en HEAD | NO ES SEDE: retirado por el arnes; mido su tamanio en el commit, NO su contenido |
| `docs/loop/ultimo_apertura.json` | en el arbol y con `0` bytes | NO ES SEDE: el arnes lo escribe al sellar, cuando mi turno ya termino |
| `docs/loop/PARA_ALEXIS.md` | no existe en el arbol | NO ES SEDE: lo nombro para decir que esta corrida no abre parada |

**UNA DISCREPANCIA ENTRE MI PROMPT Y EL ARNES, Y GANA EL ARNES.** Mi prompt avisa de que
`docs/loop/loop.log` esta retirado. **No lo esta**, y la linea del propio arnes no lo
nombra entre los cuatro: nombra `docs/loop/CREDITO_serial.jsonl`. Lo declaro porque el
prompt me manda comprobar ahi, y ahi no dice lo que el prompt dice.

    $ ls docs/loop/CREDITO_serial.jsonl
    ls: cannot access 'docs/loop/CREDITO_serial.jsonl': No such file or directory
    $ git cat-file -s HEAD:docs/loop/CREDITO_serial.jsonl     (bytes, NO su contenido)
    40874

**Y DE AHI SALE UNA TRAMPA QUE DEJO SENIALADA Y QUE NO ES DE NADIE DE HOY.** El
instrumento que `D.48` designa como registro del credito lee un fichero que el arnes
retira justo en esta fase, asi que **en la fase ciega publica un estado falso**:

    $ python forja.py credito
    CREDITO DE LA LINEA 'serial' (D.48)
      registro: docs/loop/CREDITO_serial.jsonl

      LINEA SIN REGISTRO: no hay ningun suceso escrito.
      Una linea sin tandas NACE CON SU RACHA EN CERO y no hereda
      la de nadie (D.48). Lo que herede el arnes sera CERO remedios.

> **LECTURA:** *LINEA SIN REGISTRO* **NO es cierto de la linea**: es cierto del arbol que
> yo tengo delante. El registro existe en HEAD con `40874` bytes. **NO PUBLICO NINGUNA
> RACHA PROPIA EN ESTA PAGINA**, porque la unica sede que la dice esta retirada y `D.57`
> me manda escribir la limitacion en vez de la afirmacion. Es la misma puerta por la que
> mi `ACTA 43` se cayo, y esta vez la nombro antes de cruzarla.

---

## 3. LAS GUARDAS, CORRIDAS POR MI EN ESTA FASE

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ wc -l dataset/nodos.jsonl
    346 dataset/nodos.jsonl

    $ wc -l bitacora/VEREDICTOS.jsonl
    740 bitacora/VEREDICTOS.jsonl

    $ python scripts/deuda.py
      pendientes: 9    pagadas: 6
      ultima vuelta de saneamiento: 44

| cifra | instrumento | valor |
|---|---|---|
| nodos del grafo | `forja.py gate` | **`346`** |
| lineas de la bitacora | `wc -l` sobre `bitacora/VEREDICTOS.jsonl` | **`740`** |
| deuda pendiente | `scripts/deuda.py` | **`9`** |
| guiones | `forja.py guiones` | **VERDE** |

**Ninguna de las cuatro guardas de DATO que `D.55` deja bloqueantes esta en rojo** por lo
que estas dos corridas miden: `gate` VERDE, y el censo no decreciente dentro de el.

> **Y SI: MIS INSTRUMENTOS ESCRIBEN EN EL ARBOL, asi que lo compruebo en vez de suponerlo.**
> Los mios de hoy dejan `21` ficheros en `.v47/`, y **DOS VECES me pusieron el barrido en
> ROJO**, las dos por el mismo motivo y ninguna por la pagina:
>
> 1. un volcado mio de las cabeceras de los capitulos arrastraba el guion largo de un
>    titulo verbatim del libro (`Meetings` seguido de `U+2014`). **Ese no sostenia ninguna
>    cifra de esta pagina, asi que lo retire.**
> 2. `.v47/verificar_renglones.py`, que **si** sostiene una cifra de aqui, llevaba los dos
>    guiones dentro de su propia tabla de normalizacion. **Ese no se puede retirar**, asi
>    que lo reescribi construyendo los caracteres por su codigo, **y lo volvi a correr para
>    comprobar que seguia dando lo mismo**: `44` de `44`.
>
> **El VERDE de arriba es de despues de las dos, y no de antes.** Los tres ficheros que
> esta pagina cita (`.v47/vecinos.py`, `.v47/atribuir.py` y `.v47/verificar_renglones.py`)
> siguen en el arbol.
>
> **Lo escribo porque es exactamente la caida que el arnes me entrega como aviso**: la
> vuelta 26 declaro que ninguno de sus instrumentos escribia en el arbol, seis escribian, y
> el barrido estaba en rojo con ocho hallazgos suyos.

---

## 4. LA POBLACION DEL BARRIDO (`D.38.4`) Y EL CRUCE CON LA ADUANA (`D.38.5`)

**EN CRUDO, MI CENSO DA `188`**, contando todo lo que espera en `cuarentena/` por libro y
descartando `_insertados` y `_derivadas`, que es la letra de `D.38.4`:

    $ python -    (cruce de TODAS las bandejas contra cerrados_en_extraccion, D.39)
    cerrados_en_extraccion: ['scott_radical_candor', 'smart_who', 'zhuo_manager']

    bandeja                    candidatos  cerrado?  insertables
    _derivadas                          2 (D.38.4: descartada)
    _insertados                         0 (D.38.4: descartada)
    ensayo_referencia_163             163     False            0
    grove_high_output                  22     False            0
    marquet_turn_the_ship               3     False            0
    onu_consumidor                      0     False            0
    scott_radical_candor                0      True            0
    smart_who                           0      True            0
    zhuo_manager                        0      True            0
    TOTAL BANDEJA                     188                      0

**Y LA ADUANA DA `25`, NO `188`.** La diferencia son los `163` de la bandeja
`ensayo_referencia_163`, que `src/aduana.py` linea `464` deja fuera **por su tabla de
fuentes y no por su nombre**: ninguna de sus `33` claves esta en
`fuentes/FUENTES_CANONICAS.json`.

    $ grep -n "CARPETAS_FUERA_DE_POBLACION" src/aduana.py
    405:CARPETAS_FUERA_DE_POBLACION = ("_insertados", "_derivadas")

    claves canonicas: ['_lea_esto', 'bernerslee_bananas', 'gerber_emyth',
     'gerber_emyth_cap17_reservado', 'grove_high_output', 'manual_sistema_conocimiento',
     'marquet_turn_the_ship', 'onu_consumidor', 'openstax_business_ethics',
     'openstax_org_behavior', 'scott_radical_candor', 'smart_who', 'zhuo_manager']

    bandeja                    clave declarada              canonica?  n
    ensayo_referencia_163      juran_s_quality_handbook     False      24
    ensayo_referencia_163      franchise_your_business_mark False      11
    ensayo_referencia_163      out_of_the_crisis            False      10
    ...                        (33 claves distintas, las 33 False, 163 ficheros)
    grove_high_output          grove_high_output            True       22
    marquet_turn_the_ship      marquet_turn_the_ship        True        3

> **LECTURA, Y NO LA TRAIGO COMO HALLAZGO PORQUE EL REGISTRO YA LA TIENE ADJUDICADA**
> (`D.47`, austero): `ensayo_referencia_163` es el catalogo de control que monta
> `calibracion/preparar_ensayo.py` en su linea `48`, y la `ACTA 31` ya retiro la lectura
> de que fuera vecino de nada de esta casa. **Asi que la poblacion buena de mi barrido es
> `371` y no `534`**, y con ella `D.38.5` se cumple: la aduana y yo medimos lo mismo.

    $ python .v47/vecinos.py
    poblacion del barrido (D.38.4)
      dataset/nodos.jsonl        : 346
      cuarentena (todas)         : 25
      POBLACION TOTAL            : 371
      umbrales: similitud 0.35  familia_id 0.3  paso_contra_nodo 0.6

**LA PUERTA DE `D.39`, MEDIDA POR MI:** `grove_high_output` **NO** esta en
`cerrados_en_extraccion` de `config/frentes.json`, y **el cruce de todas las bandejas del
arbol da `0` insertables**, como se lee en la tabla de arriba.

    $ python -    (estado de grove_high_output en config/frentes.json)
    cerrados_en_extraccion: {'smart_who': {...}, 'zhuo_manager': {...}, 'scott_radical_candor': {...}}
    grove_high_output en cerrados_en_extraccion: False

---

## 5. EL MATERIAL QUE CLASIFICO, Y SU CUENTA

    $ python -    (inventario real de los 22 candidatos de grove)
    candidato                                        dominio          pasos
    archivar_indicadores_resolver_problemas          produccion           4
    casar_flujo_fabricacion_flujo_ventas             produccion          12
    clasificar_trabajo_proceso_montaje_prueba        produccion           7
    construir_flujo_produccion_paso_limitante        produccion          10
    construir_grafico_escalonado_pronosticos         produccion           8
    construir_indicador_linealidad_alerta_temprana   produccion           9
    construir_indicador_tendencia_patron             produccion           6
    decidir_aceptar_rechazar_material_defectuoso     produccion           8
    detectar_arreglar_fallo_etapa_menor_valor        produccion           6
    dimensionar_inventario_materia_prima_reposicion  produccion           7
    dimensionar_plantilla_administrativa_pronostico  produccion           7
    elegir_cinco_indicadores_diarios_fabrica         produccion          10
    elegir_fabricar_pedido_pronostico                produccion           9
    elegir_indicador_salida_trabajo_administrativo   produccion           7
    elegir_inspeccion_barrera_monitorizacion         produccion          12
    emparejar_indicadores_efecto_contraefecto        produccion           7
    equilibrar_capacidad_personal_inventario_plazo   produccion           8
    preferir_inspeccion_proceso_prueba_destructiva   produccion           6
    rehacer_flujo_paso_limitante_capacidad           produccion           6
    representar_actividad_caja_negra_ventanas        produccion           9
    simplificar_trabajo_reducir_numero_pasos         produccion           7
    variar_frecuencia_inspeccion_nivel_calidad       produccion           6
    TOTAL                                                               171  candidatos: 22

| cifra | instrumento | valor |
|---|---|---|
| candidatos en la bandeja de grove | el inventario de arriba | **`22`** |
| pasos escritos, sumados | el inventario de arriba | **`171`** |
| candidatos cuyo `id` ya vive en el grafo | mi cruce contra `dataset/nodos.jsonl` | **`0`** |
| candidatos cuyo nombre de fichero no case con su `id` | el mismo cruce | **`0`** |

**NINGUNO DE LOS `22` DICE DE QUE CAPITULO SALE.** No hay campo de capitulo ni de vuelta
en la ficha: lo busque y no esta. Esa es la razon de la seccion siguiente.

---

## 6. MI CLASIFICACION A CIEGAS

**COMO LA HICE, porque el metodo decide lo que vale.** Lei `fuentes/grove_high_output/cap_02.md`
y `fuentes/grove_high_output/cap_03.md` **enteros**, y de los `22` candidatos lei **`10`
con todos sus pasos** y **`12` con su activacion, su entregable y su primer y ultimo
paso**. Lo digo porque la diferencia importa: lo segundo basta para adjudicar **de donde
sale** un nodo, y **no basta para firmar su fidelidad**.

**UN INSTRUMENTO QUE CORRI Y QUE NO SIRVE, Y LO DIGO EN VEZ DE CALLARLO.** Intente
atribuir capitulo por solapamiento lexico. **Es ruido**: los candidatos estan en castellano
y las fuentes son verbatim en ingles, asi que el maximo de las `22` filas fue `0.060` y
`9` de ellas empataron a tres decimales entre dos capitulos.

    $ python .v47/atribuir.py
    candidato                                        mejor    2o        reparto
    archivar_indicadores_resolver_problemas          cap_01   cap_02    0.000 / 0.000
    clasificar_trabajo_proceso_montaje_prueba        cap_02   cap_04    0.036 / 0.036
    decidir_aceptar_rechazar_material_defectuoso     cap_14   cap_03    0.028 / 0.019
    ...
    reparto por capitulo ganador: {'cap_01': 5, 'cap_02': 6, 'cap_03': 6, 'cap_04': 1, 'cap_05': 3, 'cap_14': 1}

> **LECTURA: ESA TABLA NO LA USO PARA NADA.** La atribucion que publico abajo sale de
> **leer los dos capitulos y reconocer cada pieza**, no de esa cifra. La pego porque corri
> el instrumento y `1.1` no me deja esconder una corrida que salio mal.

### 6.1. De que capitulo sale cada uno, leido contra el texto

> **LECTURA, y es mia:** de los `22`, **`7` salen de `fuentes/grove_high_output/cap_02.md`**
> (unidad *Cap. 1*, `The Basics of Production`) y **`15` de
> `fuentes/grove_high_output/cap_03.md`** (unidad *Cap. 2*, `Managing the Breakfast
> Factory`). **`7` mas `15` son los `22` que cuento en la seccion `5`**, y ninguno queda
> sin capitulo ni en dos capitulos a la vez.

**CADA NUMERO DE RENGLON DE ESTA TABLA ES UNA CIFRA, ASI QUE VA MEDIDO Y NO RECORDADO.**
Mi primer borrado los escribio de memoria y **la mayoria estaban mal**; los rehice contra
el fichero y despues los comprobe uno a uno, exigiendo que el renglon citado **contenga**
la frase que le cuelgo:

    $ python .v47/verificar_renglones.py

    renglones comprobados : 44
      CASAN               : 44
      NO CASAN            : 0

| # | candidato | de donde sale, con el renglon que lo sostiene | mi clase a ciegas |
|---|---|---|---|
| 1 | `construir_flujo_produccion_paso_limitante` | cap_02 L19 a L27, *the limiting step*, *total throughput time* | **SANO**, cabeza de la serie del flujo |
| 2 | `rehacer_flujo_paso_limitante_capacidad` | cap_02 L51 a L55, *limited toaster capacity* | **CONTINUA** de 1 |
| 3 | `equilibrar_capacidad_personal_inventario_plazo` | cap_02 L57 a L61, *equipment capacity, manpower, and inventory can be traded off* | **CONTINUA** de 2 |
| 4 | `clasificar_trabajo_proceso_montaje_prueba` | cap_02 L39 a L47, *process, assembly, and test* | **SANO**, cabeza de las tres operaciones |
| 5 | `preferir_inspeccion_proceso_prueba_destructiva` | cap_02 L67, *choose in-process tests over those that destroy product* | **CONTINUA** de 4 |
| 6 | `dimensionar_inventario_materia_prima_reposicion` | cap_02 L69, *receiving inspection*, *opportunity at risk* | **SANO** |
| 7 | `detectar_arreglar_fallo_etapa_menor_valor` | cap_02 L73 y L75, *detect and fix any problem at the lowest-value stage* | **SANO** |
| 8 | `elegir_cinco_indicadores_diarios_fabrica` | cap_03 L15 a L29, *which five would they be* | **SANO**, cabeza de los indicadores |
| 9 | `emparejar_indicadores_efecto_contraefecto` | cap_03 L31 y L33, *pairing indicators* | **CONTINUA** de 8 |
| 10 | `elegir_indicador_salida_trabajo_administrativo` | cap_03 L35 a L67, *the output of the work unit and not simply the activity* | **CONTINUA** de 9 |
| 11 | `representar_actividad_caja_negra_ventanas` | cap_03 L73 a L79, *black box*, *cutting some windows* | **SANO**, cabeza de la caja negra |
| 12 | `construir_indicador_linealidad_alerta_temprana` | cap_03 L81 a L87, *the linearity indicator* | **CONTINUA** de 11 |
| 13 | `construir_indicador_tendencia_patron` | cap_03 L89, *trend indicators* | **CONTINUA** de 11 |
| 14 | `construir_grafico_escalonado_pronosticos` | cap_03 L91 a L97, *the stagger chart* | **CONTINUA** de 13 |
| 15 | `archivar_indicadores_resolver_problemas` | cap_03 L99, *an archive of indicators* | **SANO** |
| 16 | `elegir_fabricar_pedido_pronostico` | cap_03 L103 a L109, *build to order* contra *build to forecast* | **SANO** |
| 17 | `casar_flujo_fabricacion_flujo_ventas` | cap_03 L111 a L121, *the order and the product should arrive at the shipping dock at the same time* | **CONTINUA** de 16 |
| 18 | `dimensionar_plantilla_administrativa_pronostico` | cap_03 L123 y L125, *forecast the number of people needed* | **CONTINUA** de 10 |
| 19 | `decidir_aceptar_rechazar_material_defectuoso` | cap_03 L135 y L137, *send it back to the vendor* o *waive our specifications* | **CONTINUA** de 6 |
| 20 | `elegir_inspeccion_barrera_monitorizacion` | cap_03 L139 y L141, *a gate-like inspection and a monitoring step* | **SANO** |
| 21 | `variar_frecuencia_inspeccion_nivel_calidad` | cap_03 L143, *variable inspections* | **CONTINUA** de 20 |
| 22 | `simplificar_trabajo_reducir_numero_pasos` | cap_03 L169 y L171, *work simplification* | **SANO** |

**EL REPARTO DE MIS CLASES:** `9` **SANO** y `13` **CONTINUA**. **Cero REPITE y cero
MUTUO**: no encontre en los `22` ni un par en el que lo que queda fuera del solape deje de
ser procedimiento en alguno de los dos lados, que es la vara de `6.1`.

**EL PAR QUE MAS CERCA ESTUVO DE CAER EN REPITE, y lo escribo porque casi lo adjudico
asi:** el `1` contra el `2`. Los dos construyen el mismo objeto, el flujo, y el segundo
repite el calculo hacia atras del primero. **Lo sostengo CONTINUA** porque lo que le queda
fuera al hijo **es procedimiento propio y no el nombre de la madre**: detectar la cola,
contar la espera **dentro** del flujo, y separar el paso que MANDA del paso que decide la
CALIDAD, que es una distincion que la madre no hace y que el paso `6` del hijo si escribe
(*no cambies de componente el que manda la calidad*). Sin bascula, como manda `6.1`.

---

## 7. MIS DISCUTIBLES, MARCADOS ANTES DE VER EL REPORTE

**Los marco ahora justamente para que se pueda medir si acerte.**

### DISCUTIBLE 1. `d021` se declara pagado, y yo leo el mismo puente un paso mas abajo

La deuda `d021`, leida en `docs/loop/DEUDA.jsonl`:

    d021 | fidelidad | vuelta 44
    QUE : PUENTE en clasificar_trabajo_proceso_montaje_prueba paso 4 ... El paso iguala la
    prueba unitaria del compilador (L45) con la presentacion en seco de la formacion de
    ventas (L41) y se lo atribuye al libro. El libro no las iguala en ningun renglon.

**El paso `4` se reparo**, y bien, con su correccion declarada entera dentro de la ficha.
**Pero el paso `5` no se toco, y dice esto:**

    5. Devuelve a la fase de proceso la pieza que falle su prueba, para rehacerla, y
       rehazla contra lo que la prueba dijo: las preocupaciones y las objeciones del
       publico que la probo.

Y los dos renglones del libro, medidos por mi en esta fase:

    $ grep -n "concerns and objections" fuentes/grove_high_output/cap_02.md
    41: ... If the dry run fails the test, the material must be "reworked" ... to meet the
        concerns and objections of the test audience.

    $ grep -n "returned to the process phase" fuentes/grove_high_output/cap_02.md
    45: ... Each piece then undergoes an individual operation called a "unit test." When one
        fails, the defective portion of the software is returned to the process phase for
        "rework."

    $ sed -n 47p fuentes/grove_high_output/cap_02.md
    Breakfast preparation, college recruiting, sales training, and compiler design are very
    much unlike one another, but all of them possess a basically similar flow of activity
    to produce a specific output.

> **LECTURA:** la primera mitad del paso `5` es `L45` y la segunda mitad es `L41`, que son
> **exactamente los dos renglones que `d021` nombra**, unidos en una sola instruccion y
> atribuidos al libro. **Y la propia correccion declarada de la ficha condena al paso `5`
> con su propio argumento**, cuando escribe que la presentacion en seco de `L41` prueba la
> presentacion **ya montada** y esta *del lado de la prueba de sistema y no del lado de la
> prueba unitaria*. El paso `5` es justamente la pieza que falla su prueba **unitaria**.
>
> **Y LA FICHA PUBLICA UNA CIFRA SOBRE ESO:** *la cifra buena es 7 pasos, 6 TRANSCRIPCION,
> 1 PUENTE en el acto de escribirla, y 7 TRANSCRIPCION, 0 PUENTE despues de esta
> correccion*. **Yo leo `1` PUENTE todavia en pie, en el paso `5`.**
>
> **LO QUE NO ADJUDICO AQUI, Y DIGO POR QUE:** si eso es `CIFRA PUBLICADA` o no depende de
> si la ficha de un candidato en bandeja es sede duradera de `5.2`, que lista `docs/`,
> `config/`, `esquema/` y el codigo de una guarda de `src/`, **y no lista la cuarentena**.
> Esa adjudicacion es del acta, no de la apertura ciega.

### DISCUTIBLE 2. Una generalizacion que NO llamo puente, y dejo escrita la lectura contraria

`detectar_arreglar_fallo_etapa_menor_valor` paso `6` dice *las piezas que componen el
producto* donde `cap_02` `L75` dice *the pieces that make up a compiler*. **No lo cuento
como PUENTE**, porque el renglon abre declarando una regla general (*A common rule we
should always try to heed*) y el compilador es su ejemplo. **Un lector estricto puede
decir que generalizar el ejemplo es poner algo que el libro no pone**, y si cae, cae
dentro de mi marcado. Los otros `5` pasos los firmo contra `L73` y `L75`, leidos uno a
uno: **`6` de `6` TRANSCRIPCION, `0` PUENTE**.

### DISCUTIBLE 3. El candidato mas delgado de los 22

`archivar_indicadores_resolver_problemas` tiene **`4`** pasos, el minimo de la tanda, y
sale de **un solo renglon** (`cap_03` `L99`). Lo adjudico **SANO** y con procedimiento
propio (mantener el archivo, repasarlo cuando algo falle, buscar las desviaciones no
sanas), **pero es el unico de los `22` del que un lector podria decir que es una
advertencia y no un nodo**.

### DISCUTIBLE 4. Un tramo del libro que no veo en ningun candidato

`cap_03` dedica cinco renglones (`L147` a `L155`) a la embajada americana en Londres y
cierra con un procedimiento: aceptar que la comprobacion del `100` por ciento es
innecesaria, instituir una prueba de muestreo, y **elegir la muestra segun criterios
predeterminados**, como hace la agencia tributaria. **Ninguno de los `22` titulos lo
recoge**, y `elegir_inspeccion_barrera_monitorizacion` no trae el paso de los criterios
predeterminados.

> **LECTURA, y la escribo con su limite:** puede ser una pieza que falta, o puede estar ya
> adjudicada como ilustracion de `variar_frecuencia_inspeccion_nivel_calidad`. **No puedo
> saber cual de las dos**, porque la frontera publicada de `cap_03` vive en el reporte y el
> reporte esta retirado de mi arbol.

---

## 8. LO QUE NO PUEDO COMPROBAR EN ESTA FASE, Y POR ESO NO LO AFIRMO (`D.57`)

1. **Que vuelta estoy auditando.** El arnes escribe que el rol es AUDITOR porque el
   reporte es mas nuevo que el acta. El nombre de la vuelta vive en el reporte, **que no
   puedo abrir**. Lo unico que mido es que la ultima acta escrita es la `ACTA 43` y que
   cubre la vuelta `44`, asi que **no hay hueco de acta** en el sentido de `1.0`: la vuelta
   que me toca es la inmediatamente siguiente a la ultima auditada.

2. **Mi propia racha.** Declarado en la seccion `2`: su unica sede esta retirada.

3. **La frontera publicada de `cap_02` y de `cap_03`**, sus cuentas de palabras y su cierre
   contra el cuerpo. Viven en el reporte del frente. **No publico ninguna cifra de
   frontera.**

4. **`PASOS INVENTADOS POR CAPITULO` de la vuelta auditada.** Cuento `171` pasos escritos
   en la bandeja, que es una cifra de fichero; **el numerador de `D.30` lo publica el
   reporte y no lo he visto.**

5. **El barrido de vecinos de los `22`, que NO termino dentro de mi turno.** Lo lance sobre
   la poblacion de `371` con la funcion de la casa. **Termino `1` de `22`**, en `384` s,
   que es el mismo orden que la corrida anterior de este instrumento (`387` s en el
   primero), y a ese ritmo los `22` pedian mas de dos horas.

   **Y LO PARE YO, A PROPOSITO, ANTES DE ESCRIBIR ESTA CIFRA.** Si lo dejo corriendo
   mientras el arnes sella, el `1 de 22` que publico aqui deja de ser cierto en el instante
   del sello, que es donde `D.38.3` manda que una cifra valga. **Prefiero una cifra baja y
   firme a una alta que caduca sola.** Lo que dio, pegado entero y sin recortar:

        $ python .v47/vecinos.py
         1/22  archivar_indicadores_resolver_problemas          vecinos=2   (384s)
                -> construir_indicador_tendencia_patron   {'similitud_texto': 0.384, 'familia_id': 0.143, 'paso_contra_nodo': 0.42}
                -> revisar_tres_preguntas_valor_carrera   {'similitud_texto': 0.369, 'familia_id': 0.0, 'paso_contra_nodo': 0.414}

   **De los otros `21` no digo nada**, ni que levanten vecinos ni que no los levanten: una
   busqueda negativa no se puede citar (`1.1`). **Y no extrapolo del primero**: `2` vecinos
   en un candidato no es una tasa.

---

## 9. EL RESUMEN DE LO QUE FIRMO

| lo que publico | valor | de donde sale |
|---|---|---|
| ACTA ANTERIOR LEIDA | `8fd9fc9094f880ab4f77775885baaf2c7eef815f` | `git hash-object` y `forja.py herencia` |
| heredados | **`0`** | `forja.py herencia` |
| nodos del grafo | **`346`** | `forja.py gate` |
| lineas de la bitacora | **`740`** | `wc -l` |
| deuda pendiente | **`9`** | `scripts/deuda.py` |
| poblacion del barrido `D.38.4` | **`371`** = `346` mas `25` | `.v47/vecinos.py` |
| candidatos en la bandeja de grove | **`22`** | el inventario de la seccion `5` |
| pasos escritos en esos `22` | **`171`** | el inventario de la seccion `5` |
| insertables en TODO el arbol (`D.39`) | **`0`** | el cruce de la seccion `4` |
| candidatos del barrido que terminaron | **`1` de `22`** | la seccion `8` punto `5` |
| mis clases a ciegas | **`9` SANO, `13` CONTINUA, `0` REPITE, `0` MUTUO** | LECTURA, la tabla `6.1` |
| mi reparto por capitulo | **`7` de cap_02, `15` de cap_03** | LECTURA, la tabla `6.1` |
| discutibles que marco antes de ver el reporte | **`4`** | la seccion `7` |

**Y LO QUE MAS ME IMPORTA DE ESTA PAGINA NO ES UNA CIFRA:** la unica que mi acta anterior
publico mal la publico **por creerse a un instrumento que leia un fichero retirado**. Hoy
ese mismo instrumento me ha dicho otra vez que mi linea no tiene registro. **Esta vez lo
he medido antes de escribirlo.**
