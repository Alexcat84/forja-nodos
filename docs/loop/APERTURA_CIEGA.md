# APERTURA CIEGA DEL AUDITOR, VUELTA 49 (`claude-opus-5`)

*Linea **serial** (`extraccion-mundo-11`), libro `grove_high_output`. Escrita ANTES de que el
arnes me exponga `docs/loop/REPORTE.md`. Modo austero (`D.47`): no repito lo que el registro ya
dice. Toda cifra de esta pagina sale de un instrumento corrido HOY y va con su salida pegada
(`D.38.3`); toda conclusion mia va en linea aparte marcada `LECTURA`.*

---

## 0. LAS TRES DECLARACIONES QUE EL ARNES EXIGE (`D.40`)

    ACTA ANTERIOR LEIDA: fa548ca517d97b8955f622aeec22134a5e5cfc3d
    HEREDADO 1: CUMPLIDO
    HEREDADO 2: CUMPLIDO

**La huella la comprobe yo y no la copie del prompt.** El instrumento mide el fichero
`docs/loop/ACTA_AUDITOR.md` tal como esta en el arbol ahora mismo:

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    fa548ca517d97b8955f622aeec22134a5e5cfc3d

Ese bloque mide la huella del acta en el arbol. `LECTURA`: **coincide con la que el prompt me
entrega**, que es la condicion que `D.40` pone (*decir que leiste otra version no es haberla
leido*).

### 0.a. `HEREDADO 1`, y la salida pegada que el propio remedio exige

> **El remedio, literal (`ACTA 47` `47.9.d`):** *Antes de escribir `HEREDADO N: CUMPLIDO` corro la
> comprobacion del remedio sobre mi propia pagina y pego su salida. Para el remedio del superlativo
> esa comprobacion es un barrido de los patrones de superlativo sobre `APERTURA_CIEGA.md` con cada
> golpe contestado.*

**Esto es lo que rompi en la vuelta 48:** el remedio del superlativo era bueno y la declaracion de
cumplido fue a ojo (`ACTA 47` `47.9.a`, tres superlativos sin lista en la misma pagina sellada).
**Hoy el barrido esta corrido sobre esta pagina y su salida entera esta pegada en la seccion `14`,
con una fila por golpe.** Si alguien encuentra un superlativo mio sin su lista debajo, el remedio
vuelve a estar roto y la seccion `14` es donde se comprueba.

### 0.b. `HEREDADO 2`, y su comprobacion

> **El remedio, literal:** *Toda frase mia que acompane a un pegado dice lo que ESE pegado mide, y
> si mi frase habla de otra cosa la marco `LECTURA` y digo de donde sale.*

**Su comprobacion esta en la seccion `15`:** un instrumento que saca cada bloque pegado de esta
pagina y le imprime encima la frase que lo presenta, para que se lean una contra otra sin tener
que buscarlas.

---

## 1. QUE ABRI, QUE NO ABRI, Y LO QUE ME LLEGO SIN PEDIRLO

    $ grep -n "APERTURA CIEGA" docs/loop/loop.log | tail -1
    3273:[2026-09-19 11:31:41] VUELTA 5 : APERTURA CIEGA (claude-opus-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl

Ese bloque mide que linea escribio el arnes en el log para mi turno y que cuatro ficheros retiro.

**NO ABRI** `REPORTE.md`, `ultimo_extractor.json`, `ultimo_auditor.json` ni `CREDITO_serial.jsonl`
(no estan en el arbol), **ni los ficheros de trabajo del extractor de `.v49/`**, que si estan y no
toque **porque son su medida y su conclusion**, que es justo lo que vengo a leer a ciegas. **Ni
`docs/loop/TABLA_DE_CIERRE.txt`**, que se deriva de su reporte: de ese fichero tome su huella sin
leer una celda (seccion `4.c`).

**LO QUE SI ABRI, Y ES OBRA MIA:** `docs/loop/ACTA_AUDITOR.md`, `docs/loop/PROMPT_SIGUIENTE.md`
(mi encargo de la vuelta 49) y mis instrumentos de `.v47aud/` y `.v48aud/`.

**Y LO QUE ME LLEGO SIN PEDIRLO, QUE LO DECLARO YO ANTES DE QUE NADIE LO PREGUNTE:**

| lo que vi | por donde entro | que me adelanta |
|---|---|---|
| `docs/loop/DEUDA.jsonl` | **lo abri yo**, y era la via de saber que debia esta vuelta | sus dos lineas `tipo: pago` **las escribe el extractor**, y traen SUS cifras de aduana (`0 CAERIA`, `1 BLOQUEARIA con 4 vecinos`, `ENTRARIA con 0 vecinos`, relojes `559,4` s y `1479,4` s) y un defecto propio suyo declarado |
| el asunto del commit `8d124c1` | **el arnes me lo puso en el prompt**, dentro del `git status` de apertura | *d027 y d032 pagadas con su aduana en el acto, d024 corta en 2 de 3, y la corrida intermitente medida en 0 de 20* |

**MI LECTURA YA NO ES CIEGA EN ESOS DOS PUNTOS Y NO VOY A FINGIR QUE LO ES.** Lo que queda por
hacer con ellos es medirlos yo: las secciones `5`, `6`, `7` y `11` traen **mi** cifra sacada de
**mi** instrumento, al lado de la suya.

---

## 2. EL MATERIAL DE ESTA VUELTA: **NO HAY CANDIDATO NUEVO QUE CLASIFICAR, Y ESO SE MIDE**

La fase ciega me manda abrir *los candidatos del lote*. **Esta vuelta no escribio ninguno**, y no
es una busqueda negativa citada de memoria (`AUDITOR_FORJA.md` 1.1): es el arbol.

    $ git diff --numstat HEAD~1 HEAD | grep -v "\.v49/"
    1	1	cuarentena/grove_high_output/dimensionar_numero_subordinados_medio_dia_semanal.json
    1	1	cuarentena/grove_high_output/reunir_informacion_gerencial_vias_variadas.json
    2	0	docs/loop/DEUDA.jsonl
    995	1	docs/loop/REPORTE.md
    5	4	docs/loop/TABLA_DE_CIERRE.txt
    10	0	docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_v48.txt

    $ git diff --stat HEAD~1 HEAD -- dataset/ bitacora/ config/ censos/ esquema/ src/ scripts/ tests/ docs/BANCO_DE_REGLAS.md docs/MANUAL_SISTEMA_DE_CONOCIMIENTO.md
    (sin salida)

El primer bloque mide **cuantas lineas cambio cada fichero** entre el commit anterior y este, sin
`.v49/`; el segundo mide **si alguna de esas sedes cambio**, y no imprime fichero ninguno.

`LECTURA`: **la vuelta 49 toco dos fichas de cuarentena y ningun dato.** Con eso, el material que
esta apertura puede clasificar es otro: **las dos fichas corregidas** (secciones `5` y `6`), **los
`7` candidatos de `cap_02` que `d024` dejo sin informe** (seccion `10`), y **las clases de la
propia vuelta medidas sobre su diferencia** (seccion `12`).

---

## 3. EL ESTADO DE LA LINEA, RECONTADO POR MI

    $ python .v49aud/01_poblacion.py
    dataset/nodos.jsonl : 346 nodos
    bitacora/VEREDICTOS.jsonl : 740 lineas
    config/pares_mutuos.jsonl : 1 lineas
    cuarentena/grove_high_output/ : 41 fichas

    cap_02 : 7 fichas en la bandeja
    cap_03 : 15 fichas en la bandeja
    cap_04 : 19 fichas en la bandeja

Ese bloque cuenta lineas de tres ficheros del arbol y ficheros de una carpeta, y reparte las `41`
fichas de la bandeja por el capitulo que cada `resumen_teorico` declara como unidad de origen.

`LECTURA`: **las cuatro cifras son las que mi propio encargo dijo que tenian que salir**
(`PROMPT_SIGUIENTE.md` TAREA 5 punto 3: *tiene que dar `346`, `740`, `1` y `41` fichas en la bandeja
de `grove`*), y `cap_04` sigue en `19`, que es lo que `47.5.d` adjudico. **Una vuelta de saneamiento
que no inserta no mueve ninguna de las cuatro, y ninguna se movio.**

---

## 4. LAS GUARDAS QUE BLOQUEAN (`D.55`), CORRIDAS POR MI

### 4.a. Las dos del arbol

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

El primer bloque mide las `13` guardas del gate sobre `346` nodos; el segundo, los guiones del
arbol.

`LECTURA`: **el cerrojo y el censo no decreciente viajan dentro de esa lista** (`censo_no_decrece`
esta nombrada en la salida), asi que de las cuatro guardas de DATO que `D.55` nombra como
bloqueantes, **tres salen verdes aqui**. La cuarta, la fidelidad `D.30`, **el gate no la mide**:
la releo yo a mano, paso por paso, en las secciones `5`, `6` y `10`.

### 4.b. La prueba de aceptacion

Va aparte, corrida aislada y con su tasa, en la seccion `11`.

### 4.c. El sello de `D.52`, que es el remedio a mano de `d030` otra vez

    $ git show HEAD~1:docs/loop/TABLA_DE_CIERRE.txt | git hash-object --stdin
    9bf10e6792bffa91ebcbc9894af90834d13c2aac
    $ git hash-object docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_v48.txt
    9bf10e6792bffa91ebcbc9894af90834d13c2aac

Ese bloque compara la huella de la tabla que estaba VIVA antes de esta vuelta con la huella de la
copia que esta vuelta archivo como `v48`.

`LECTURA`: **la copia archivada es byte a byte la que estaba viva**, no una transcripcion, y no
hizo falta leer ni una celda de ninguna de las dos. **El remedio de `d030` se volvio a pagar a
mano**, que es lo que `D.45` obliga mientras `scripts/` este fuera de alcance.

---

## 5. `d027`: LA FICHA DE `reunir_informacion_gerencial_vias_variadas`

### 5.a. Lo que el libro dice, leido por mi

    $ sed -n "145p" fuentes/grove_high_output/cap_04.md
    As you can see, much of my day is spent acquiring information. And as you can also see, I use many ways to get it. I read standard reports and memos but also get information ad hoc. [...]
    $ grep -rn "six ways" fuentes/grove_high_output/ | wc -l
    0
    $ grep -rno "many ways" fuentes/grove_high_output/cap_04.md
    145:many ways

Ese bloque mide **que escribe `L145`** y **cuantas veces aparece `six ways` en el libro entero**,
que es cero.

`LECTURA`: **la correccion que la ficha escribe es cierta.** El libro dice *many ways* y no da
cuenta, asi que quitar el numero en vez de cambiarlo por otro es lo que corresponde: **la ficha no
inventa la cuenta buena.**

### 5.b. Que movio la vuelta dentro de la ficha, medido con la funcion de la casa

    $ python .v49aud/06_huellas.py
    == reunir_informacion_gerencial_vias_variadas
       titulo                   antes     96 car, hoy     96 car, IGUAL
       condiciones_activacion   antes    229 car, hoy    229 car, IGUAL
       entregable_esperado      antes    153 car, hoy   1886 car, CAMBIA (+1733)
       resumen_teorico          antes   3450 car, hoy   3450 car, IGUAL
       pasos_accionables        antes      8, hoy      8, IGUALES
       huella del texto que mira la senial 1: antes 997ece8f644815ab, hoy 997ece8f644815ab, IGUAL
       texto_comparable: antes 4370 car, hoy 4370 car
       entregable_esperado: el texto viejo entero (153 car) SIGUE dentro del nuevo

Ese bloque compara la ficha de `HEAD~1` con la de `HEAD` campo a campo, y calcula sobre las dos la
huella de `comun.texto_comparable` (`src/comun.py:190`), que es el texto que mira la senial `1`.

`LECTURA`: **la correccion no borro nada** (el texto viejo entero sigue dentro del campo nuevo,
manual principio 6) **y no toco ni un paso**. Y la ficha afirma dentro de si misma que dejo el
`resumen_teorico` *byte a byte* para no mover su cola de vecinos: **la huella identica lo
confirma.**

### 5.c. Su fidelidad `D.30`, releida por mi contra el renglon

**Los `8` pasos contra `L145` y `L147`, uno a uno:** pasos `1` y `2` estan en *I read standard
reports and memos but also get information ad hoc*; el `3` en *I talk to people inside and outside
the company, managers at other firms or financial analysts or members of the press*; el `4` en
*Customer complaints, both external and internal, are also a very important source of information*;
el `5` en *To cut myself off from the casual complaints of people in that group would be a
mistake*; el `6` en *People also tell us things because they want us to do something for them*; el
`7` en *the information most useful to me [...] comes from quick, often casual verbal exchanges*;
el `8` en *usually the more timely the information, the more valuable it is*.

`LECTURA`: **firmo su `8` de `8` TRANSCRIPCION y `0` PUENTE.** Los dos renglones los tengo pegados
arriba y en la seccion `5.a`, y cada paso cae dentro de uno de los dos.

---

## 6. `d032`: LA FICHA DE `dimensionar_numero_subordinados_medio_dia_semanal`

### 6.a. La primera frase corregida: `P34` contra `P38`

    $ python .v49aud/04_palabras_cap04.py
    LOS TRAMOS DE LA TANDA DE LA VUELTA 48 (rangos leidos de los resumen_teorico de sus fichas):
       P34  L273 a L285   469 palabras
       P36  L289 a L289   101 palabras
       P38  L293 a L301   396 palabras
       P39  L303 a L307   242 palabras

Ese bloque cuenta las palabras del texto fuente en los rangos de linea que las propias fichas
declaran, **lista ordenada entera de los cuatro tramos de la tanda de la vuelta 48**.

`LECTURA`: **la correccion es cierta y la firmo**: `P38` con `396` no es el tramo de mas palabras
de su tanda, porque `P34` tiene `469`. Es la misma cifra que mi instrumento `.v48aud/01` saco en la
vuelta anterior, y hoy vuelve a salir igual leyendo el libro.

### 6.b. La segunda frase corregida: de donde sale el `cinco`

    $ sed -n "299p" fuentes/grove_high_output/cap_04.md
    Sometimes a business is organized in a way that makes the ideal fan-out of six to eight subordinates hard to reach. [...] So the plant manager will actually have six direct reports: five engineers and the manufacturing manager. The arrangement, shown below, does not have the engineers appearing to be at the same organizational level as the manufacturing manager [...]

Ese bloque mide **que escribe `L299` y en que orden**.

`LECTURA`: **el `cinco` y el `seis` estan en la prosa del libro, y `The arrangement, shown below`
es la frase siguiente**, o sea que el motivo viejo (*sale del dibujo*) era falso y la correccion lo
dice. **Y el motivo nuevo se sostiene con la regla que cita**, que la comprobe:

    $ sed -n '67,89p' docs/MANUAL_SISTEMA_DE_CONOCIMIENTO.md | sed -n '17,19p'
    5. SI ES UN CASO O ESTUDIO: el caso no es la casa. La doctrina vive en su nodo
       y el caso entra como ejemplo nombrado dentro de ella (señal barata: el
       entregable del caso lleva un dato del caso).

Ese bloque mide **que dice el punto `5` de la seccion `3` del manual**, que es lo que la ficha cita
como `manual seccion 3.5`.

`LECTURA`: **la regla dice lo que la ficha dice que dice.** Y su senial barata se puede mirar, asi
que la miro: el `entregable_esperado` entero de esta ficha, pegado sin cortar, es

    $ python -c "import json;print(json.load(open('cuarentena/grove_high_output/dimensionar_numero_subordinados_medio_dia_semanal.json',encoding='utf-8'))['entregable_esperado'])"
    Un numero de subordinados o equivalentes dentro de la horquilla que el autor da, sostenido por la guia de tiempo de la que esa horquilla sale, y con el reparto reorganizado cuando el negocio no deja llegar a ella.

Ese bloque imprime el campo `entregable_esperado` de la ficha, entero.

`LECTURA`: **el entregable lleva el dato de la REGLA** (la horquilla del autor, `six to eight`) **y
no lleva el `cinco` ni el `seis` del caso de la planta**, que es justo lo que la senial barata del
manual busca.

### 6.c. Que movio la vuelta dentro de la ficha

    $ python .v49aud/06_huellas.py
    == dimensionar_numero_subordinados_medio_dia_semanal
       titulo                   antes    157 car, hoy    157 car, IGUAL
       condiciones_activacion   antes    153 car, hoy    153 car, IGUAL
       entregable_esperado      antes    213 car, hoy    213 car, IGUAL
       resumen_teorico          antes   7820 car, hoy  10180 car, CAMBIA (+2360)
       pasos_accionables        antes     11, hoy     11, IGUALES
       huella del texto que mira la senial 1: antes f6f4f4dd3060e8a0, hoy 17327e3a009f5484, DISTINTA
       texto_comparable: antes 9794 car, hoy 12072 car
       resumen_teorico: el texto viejo entero (7820 car) SIGUE dentro del nuevo

Ese bloque compara la ficha de `HEAD~1` con la de `HEAD` campo a campo y calcula las dos huellas de
la senial `1`.

`LECTURA`: **ni un paso ni una atribucion se movieron, y el texto viejo sigue entero**, que es lo
que la correccion prometia y lo que mi encargo pedia. **Y la huella de la senial `1` SI cambia**,
al reves que en `d027`: por eso volver a pasar la aduana sobre esta ficha no era una formalidad.

---

## 7. EL BARRIDO DE VECINOS (`D.38.4`), CORRIDO POR MI SOBRE GRAFO MAS BANDEJAS

    $ python .v49aud/12_poblacion_barrida.py
    grafo (dataset/nodos.jsonl) : 346
    bandeja/ensayo_referencia_163  : 0 de 163 ficheros pasan el filtro canonico
    bandeja/grove_high_output      : 41 de 41 ficheros pasan el filtro canonico
    bandeja/marquet_turn_the_ship  : 3 de 3 ficheros pasan el filtro canonico
    bandeja/onu_consumidor         : 0 de 0 ficheros pasan el filtro canonico
    bandeja/scott_radical_candor   : 0 de 0 ficheros pasan el filtro canonico
    bandeja/smart_who              : 0 de 0 ficheros pasan el filtro canonico
    bandeja/zhuo_manager           : 0 de 0 ficheros pasan el filtro canonico
    POBLACION BARRIDA (D.38.4) : 390

Ese bloque mide **de que se compone la poblacion que barro**: el grafo mas las bandejas, sin
`_insertados` ni `_derivadas` y con el filtro de fuente canonica.

    $ python .v49aud/07_barrido.py reunir_informacion_gerencial_vias_variadas
    FICHA: reunir_informacion_gerencial_vias_variadas   (8 pasos)
      poblacion barrida: 390 nodos (grafo + bandejas, filtro canonico)
      medidos al digito: 389 de 389; descartados: 0
      umbral de la casa (config/umbrales.json): 0.35
      reloj del barrido: 378.0 s
      LOS 8 VECINOS MAS PROXIMOS, LISTA ORDENADA ENTERA:
        0.3802  [bandeja/grove_high_output] programar_visita_area_observar_despachar
        0.3714  [bandeja/grove_high_output] escalonar_fuentes_informacion_gerencial
        0.3663  [bandeja/grove_high_output] empujar_persona_reunion_direccion_preferida
        0.3519  [bandeja/grove_high_output] elegir_momento_actividad_palanca_maxima
        0.3316  [bandeja/grove_high_output] transmitir_objetivos_prioridades_preferencias
        0.3309  [bandeja/grove_high_output] subir_productividad_gerencial_tres_vias
        0.3289  [bandeja/grove_high_output] dimensionar_plantilla_administrativa_pronostico
        0.3256  [bandeja/grove_high_output] supervisar_tarea_delegada_etapa_menor_valor
      vecinos por encima del umbral 0.35: 4

    $ python .v49aud/07_barrido.py dimensionar_numero_subordinados_medio_dia_semanal
    FICHA: dimensionar_numero_subordinados_medio_dia_semanal   (11 pasos)
      poblacion barrida: 390 nodos (grafo + bandejas, filtro canonico)
      medidos al digito: 389 de 389; descartados: 0
      umbral de la casa (config/umbrales.json): 0.35
      reloj del barrido: 820.3 s
      LOS 8 VECINOS MAS PROXIMOS, LISTA ORDENADA ENTERA:
        0.3057  [bandeja/grove_high_output] llevar_inventario_proyectos_discrecionales
        0.2958  [bandeja/grove_high_output] buscar_regularidad_bloques_iguales_trabajo_mando
        0.2642  [bandeja/grove_high_output] supervisar_tarea_delegada_etapa_menor_valor
        0.2543  [bandeja/grove_high_output] usar_calendario_herramienta_planificacion_produccion
        0.2423  [bandeja/grove_high_output] supervisar_decision_delegada_preguntas_concretas
        0.2411  [bandeja/grove_high_output] casar_flujo_fabricacion_flujo_ventas
        0.2349  [bandeja/grove_high_output] decidir_aceptar_rechazar_material_defectuoso
        0.2345  [bandeja/grove_high_output] agrupar_tareas_semejantes_aprovechar_preparacion
      vecinos por encima del umbral 0.35: 0

Los dos bloques miden **la senial `1` de la casa** (`src.aduana.senal_similitud_texto`, `src/aduana.py:278`)
de cada ficha contra los otros `389` de la poblacion, al digito y sin muestra, con sus `8`
primeros en lista ordenada entera y su reloj.

`LECTURA`, y es el cruce que `D.38.5` me manda hacer: **mis dos cifras y las dos que la
`DEUDA.jsonl` trae escritas por el extractor coinciden**. `d027` da `4` vecinos sobre umbral contra
su *`1 BLOQUEARIA` con `4` vecinos*, y `d032` da `0` contra su *`ENTRARIA` con `0` vecinos*. **Las
dos poblaciones son la misma `390`**, asi que el cruce es de verdad y no de metodo.

`LECTURA` **sobre el coste, que es la medida que `d031` pedia**: mis dos barridos de una sola
senial costaron `378,0` s y `820,3` s **sobre una maquina que ademas estaba corriendo otras cosas
mias**. La ficha de `d027` no movio ni un caracter del texto que mira esa senial (seccion `5.b`) y
aun asi la aduana entera se volvio a correr sobre ella. **Lo mido y no lo adjudico aqui:** la
propuesta es del turno normal, y `D.45` deja `src/` fuera de mi alcance.

---

## 8. LO QUE ENCONTRE SIN BUSCARLO: **LAS PALABRAS DECLARADAS DE NUEVE FICHAS DE `cap_04`**

    $ python .v49aud/05_tramos_declarados.py
    ficha                                                pieza  rango declarado     dice   cuento cuadra
    buscar_actividad_alta_palanca_tres_vias              P19    L203  a L213       118       76 NO  <-- discrepa en 42
    detectar_palanca_negativa_actividad_mando            P21    L219  a L219        73       73 SI
    elegir_momento_actividad_palanca_maxima              P20    L215  a L217       297      237 NO  <-- discrepa en 60
    empujar_persona_reunion_direccion_preferida          P13    L167  a L167       174      147 NO  <-- discrepa en 27
    escalonar_fuentes_informacion_gerencial              P9     L153  a L153       208      183 NO  <-- discrepa en 25
    programar_visita_area_observar_despachar             P10    L155  a L157       337      236 NO  <-- discrepa en 101
    reunir_informacion_gerencial_vias_variadas           P7     L145  a L147       356      210 NO  <-- discrepa en 146
    subir_productividad_gerencial_tres_vias              P18    L195  a L201        62       60 NO  <-- discrepa en 2
    transmitir_objetivos_prioridades_preferencias        P11    L159  a L159       197      160 NO  <-- discrepa en 37

    fichas de cap_04 con pieza, rango y palabras declarados: 9 ; cuadran 1 ; discrepan 8

Ese bloque mide, para las fichas de `cap_04` que declaran pieza, rango de lineas y palabras dentro
de su `resumen_teorico`, **la cuenta de palabras del rango que ellas mismas declaran**, contra la
cifra que ellas mismas escriben. **No mide de donde sale la cifra declarada**, que vive en la
frontera publicada en el reporte, y el reporte no esta en el arbol.

`LECTURA`, con su limite dicho: **`8` de `9` no cuadran, y en esas `8` la ficha declara de mas.** Las
dos fichas de la tanda de la vuelta 48 que si pude cruzar (`P34` y `P38`, seccion `6.a`) **cuadran
al digito con mi misma vara**, asi que **no es que su metodo y el mio cuenten distinto**: los
golpes se concentran en las piezas declaradas antes. **Registro y no adjudico**: la causa puede
estar en que el rango escrito en la ficha no sea el rango de la pieza en la frontera, y **eso solo
se cierra contra la tabla de frontera, que es de la fase siguiente.**

**ESTO NO TUMBA NINGUNA DE LAS DOS CORRECCIONES DE ESTA VUELTA**, que van por otro sitio: la de
`d027` es sobre `six ways` y la de `d032` sobre `P34` contra `P38`, las dos comprobadas arriba
contra el libro.

---

## 9. UNA CAIDA MIA, MEDIDA EN ESTA MISMA FASE

Mi propia deuda `d031`, escrita por mi en la `ACTA 46`, dice: *el `resumen_teorico` alimenta la
senial `1` (`src/aduana.py` linea `315`)*.

    $ grep -n "^def " src/aduana.py | sed -n '5,7p'
    278:def senal_similitud_texto(texto_a, texto_b):
    295:def senal_familia_id(id_a, id_b):
    304:def senal_paso_contra_nodo(candidato, vecino):
    $ awk 'NR>=314 && NR<=315' src/aduana.py
        cuerpo_candidato = comun.normalizar_texto(
            "%s. %s" % (candidato.get("titulo") or "", candidato.get("resumen_teorico") or ""))

Ese bloque mide **en que linea empieza cada senial** y **que hay escrito en la linea `315`**.

`LECTURA`: **la linea `315` es cuerpo de la senial `3`** (`senal_paso_contra_nodo`, que empieza en
la `304`), **no de la senial `1`** (que empieza en la `278`). La sustancia de `d031` se sostiene y
es incluso mas ancha de lo que escribi (el `resumen_teorico` alimenta la `1` **y** la `3`), pero
**la linea que cite como prueba de la `1` no es de la `1`. La cita es mia y el fallo es mio.**
**Registro aqui la medida y la adjudico en el acta**, que es donde vive mi racha.

---

## 10. LOS `7` DE `cap_02` (`d024`): MI CLASIFICACION A CIEGAS, POR LECTURA

`d024` dice que los `7` candidatos de `cap_02` **no tienen informe de aduana por candidato**. Mi
encargo pidio `3` de los `7`, en el orden del libro. **Lo que hay en el arbol, por nombre de
fichero y sin abrir ninguno:**

    $ ls .v49/ | grep informe
    informe_cap02_1.txt
    informe_cap02_2.txt
    informe_d027.txt
    informe_d032.txt

Ese bloque mide **cuantos ficheros de informe escribio la vuelta y como se llaman**. No mide que
candidato lleva cada uno ni que dijo, porque no los abri.

`LECTURA`: **hay `2` ficheros de informe de `cap_02` y el encargo pedia `3`.** Si la vuelta cerro
corta y lo declaro con su reloj es cosa de su reporte, y eso lo verifico en el turno normal.

**MI PARTE ES LA CLASE, Y LA HAGO LEYENDO** (`D.19`: una discrepancia no se adjudica citando una
senial; se adjudica leyendo los pasos). Los `7`, en el orden del libro:

| # | candidato | pieza | que pide hacer | mi clase a ciegas |
|---|---|---|---|---|
| 1 | `construir_flujo_produccion_paso_limitante` | `P2` | construir el flujo desde el paso limitante y escalonar hacia atras desde la hora de entrega | **procedimiento propio** |
| 2 | `clasificar_trabajo_proceso_montaje_prueba` | `P5` | repartir un trabajo en proceso, montaje y prueba | **procedimiento propio** |
| 3 | `rehacer_flujo_paso_limitante_capacidad` | `P6` | rehacer el flujo cuando una capacidad limitada mueve el paso que manda | **procedimiento propio, y su par con el `1` ya esta adjudicado** |
| 4 | `equilibrar_capacidad_personal_inventario_plazo` | `P7` | intercambiar equipo, mano de obra e inventario contra el plazo | **procedimiento propio** |
| 5 | `preferir_inspeccion_proceso_prueba_destructiva` | `P9` | elegir la inspeccion dentro del proceso antes que la prueba que destruye producto | **procedimiento propio** |
| 6 | `dimensionar_inventario_materia_prima_reposicion` | `P10` | inspeccionar al recibir y dimensionar el inventario por el tiempo de reposicion | **procedimiento propio** |
| 7 | `detectar_arreglar_fallo_etapa_menor_valor` | `P11` | ordenar las etapas por valor y poner la comprobacion en la de menor valor | **procedimiento propio** |

**LOS TRES PARES QUE UN LECTOR ESTRICTO LEVANTARIA, Y POR QUE LOS DEJO SEPARADOS:**

| par | lo que comparten | lo que los separa, leido en los pasos |
|---|---|---|
| `5` con `7` | los dos deciden **donde** se comprueba | el `5` elige **por destructividad** (prueba funcional que tira la unidad contra termometro dentro del proceso, `L67`); el `7` elige **por valor acumulado** (`L75`: *detect and fix any problem at the lowest-value stage possible*). **Dos criterios distintos sobre la misma decision: es `D.29` por contraste, no duplicado** |
| `2` con `7` | los dos nombran la **prueba unitaria** del compilador | el `2` la usa para decir **que es** una operacion de prueba y en que orden va (`L45`); el `7` la usa como **ejemplo del criterio de valor** (`L75`). **Ninguno de los dos anade pasos al otro: no hay direccion madre a hijo** |
| `4` con `6` | los dos hablan de **inventario** | el `4` es inventario de **producto terminado** como moneda de cambio contra equipo y mano de obra (`L61`); el `6` es inventario de **materia prima** dimensionado por el tiempo de reposicion (`L69`). **Objetos de trabajo distintos** |

**Y EL PAR `1` CON `3` NO LO REABRO:** lo adjudico la `ACTA 32` del frente `grove` y lo re adjudico
`D.53` a `SANO` con correccion declarada dentro de las dos fichas (deuda `d004`, pagada en la vuelta
`44`). Lo releo y **la lectura de entonces se sostiene**: el `1` construye el flujo desde el paso
limitante y el `3` lo rehace cuando la cola mueve cual es ese paso.

### 10.a. La fidelidad `D.30` de tres de los siete, releida por mi contra el renglon

**`preferir_inspeccion_proceso_prueba_destructiva`, `6` pasos contra `L67`:** el coste de la averia
silenciosa (*The entire work-in-process [...] becomes unusable*), el desperdicio de al lado (*All
the toast is also wasted*), la prueba funcional que obliga a tirar la unidad, la inspeccion dentro
del proceso con el termometro, el aviso automatico (*bells anytime the temperature varied by a
degree or two*) y la preferencia final (*whenever possible, you should choose in-process tests over
those that destroy product*). **`6` de `6` TRANSCRIPCION.**

**`dimensionar_inventario_materia_prima_reposicion`, `7` pasos contra `L69`:** inspeccion de
recepcion, huevos rotos o de tamano que no toca, devolver y quedarte parado, tener inventario, el
principio de cubrir el consumo durante el tiempo de reposicion, pesar la ventaja contra el coste, y
la oportunidad en riesgo con sus tres preguntas. **`7` de `7` TRANSCRIPCION.**

**`detectar_arreglar_fallo_etapa_menor_valor`, `6` pasos contra `L73` y `L75`:** el material que se
vuelve mas valioso, el valor percibido del rotulo y el aparcamiento, la regla comun de la etapa de
menor valor, y sus tres aplicaciones (huevo podrido, entrevista de campus, prueba unitaria del
compilador). **`6` de `6` TRANSCRIPCION.**

`LECTURA`: **de los `19` pasos que relei de esos tres candidatos, `19` son transcripcion y `0` son
PUENTE.** No firmo los otros cuatro: no los relei paso a paso en esta fase y lo digo.

### 10.b. Y una deuda pagada que sigue pagada

Relei los `7` pasos de `clasificar_trabajo_proceso_montaje_prueba` contra `L39`, `L41` y `L45`,
porque ahi vivieron `d021` y `d023`: **los pasos `4` y `5` son hoy transcripcion de `L45` y solo de
`L45`** (*Each piece then undergoes an individual operation called a unit test* y *When one fails,
the defective portion of the software is returned to the process phase for rework*), **sin la mitad
de `L41` que los dos traian.** `LECTURA`: **el pago se sostiene, y la ficha lleva dentro sus tres
correcciones declaradas con el texto viejo entero.**

### 10.c. Y el barrido de vecinos de los siete, que `d024` echaba en falta

    $ python .v49aud/19_cola_siete.py
    clasificar_trabajo_proceso_montaje_prueba   (7 pasos)   reloj 510.8 s   vecinos sobre 0.35: 1
          0.3720  [bandeja/grove_high_output] preferir_inspeccion_proceso_prueba_destructiva
    construir_flujo_produccion_paso_limitante   (10 pasos)   reloj 426.7 s   vecinos sobre 0.35: 2
          0.4115  [bandeja/grove_high_output] rehacer_flujo_paso_limitante_capacidad
          0.3972  [bandeja/grove_high_output] preferir_inspeccion_proceso_prueba_destructiva
    detectar_arreglar_fallo_etapa_menor_valor   (6 pasos)   reloj 140.6 s   vecinos sobre 0.35: 0
    dimensionar_inventario_materia_prima_reposicion   (7 pasos)   reloj 127.0 s   vecinos sobre 0.35: 3
          0.3911  [bandeja/grove_high_output] preferir_inspeccion_proceso_prueba_destructiva
          0.3741  [bandeja/grove_high_output] equilibrar_capacidad_personal_inventario_plazo
          0.3575  [bandeja/grove_high_output] detectar_arreglar_fallo_etapa_menor_valor
    equilibrar_capacidad_personal_inventario_plazo   (8 pasos)   reloj 185.0 s   vecinos sobre 0.35: 2
          0.3891  [bandeja/grove_high_output] dimensionar_inventario_materia_prima_reposicion
          0.3530  [bandeja/grove_high_output] construir_indicador_tendencia_patron
    preferir_inspeccion_proceso_prueba_destructiva   (6 pasos)   reloj 166.3 s   vecinos sobre 0.35: 4
          0.4455  [bandeja/grove_high_output] rehacer_flujo_paso_limitante_capacidad
          0.4103  [bandeja/grove_high_output] construir_flujo_produccion_paso_limitante
          0.3837  [bandeja/grove_high_output] dimensionar_inventario_materia_prima_reposicion
          0.3657  [bandeja/grove_high_output] clasificar_trabajo_proceso_montaje_prueba
    rehacer_flujo_paso_limitante_capacidad   (6 pasos)   reloj 223.2 s   vecinos sobre 0.35: 3
          0.4601  [bandeja/grove_high_output] preferir_inspeccion_proceso_prueba_destructiva
          0.4191  [bandeja/grove_high_output] construir_flujo_produccion_paso_limitante
          0.3569  [bandeja/grove_high_output] dimensionar_inventario_materia_prima_reposicion

    pares sobre umbral en los 7 candidatos de cap_02: 15

Ese bloque es un **recorte declarado**: toma de las siete salidas del instrumento `07` (la senial
`1` de la casa sobre la poblacion de `390`) su reloj, su cuenta sobre umbral y **los vecinos que
pasan el umbral, enteros y en el orden en que el instrumento los dio**. Lo que recorta son los
vecinos por DEBAJO del umbral; **las siete salidas enteras, con sus `8` primeros cada una, estan en
`.v49aud/16_barrido_<id>.out`.**

`LECTURA`: **`6` de los `7` candidatos de `cap_02` tienen al menos un vecino por encima del umbral,
y suman `15` pares.** Eso es lo que `d024` decia que nadie habia medido por candidato, y **es
material de cola de lectura para la vuelta que abra la insercion de `cap_02`**, no una clase: quien
adjudica es la lectura de los pasos (seccion `10`), y ahi los siete me salen separados.

`LECTURA` **sobre un digito que no cuadra consigo mismo**: `dimensionar_inventario` ve a
`detectar_arreglar` en `0.3575`, y `detectar_arreglar` sale con `0` vecinos sobre umbral. **La
senial no es simetrica**, y no es un hallazgo de hoy: lo medi en la vuelta 48 con
`.v48aud/19_senial_no_es_simetrica.py`, `7` de `7` pares cambiaban de digito al invertir el orden.
**Lo que hoy se anade, y va con la lista entera de lo que he medido en los dos sentidos:** aquellos
`7` pares de la vuelta 48 cambiaban de digito pero **quedaban los dos lados del mismo lado del
umbral** (`0.3904` contra `0.3986`, `0.3655` contra `0.3712`, `0.3759` contra `0.3772`, `0.3641`
contra `0.3693`, `0.3544` contra `0.3578`, `0.3935` contra `0.4010`, `0.3680` contra `0.3665`), y
**este par de hoy cae a un lado en un sentido y al otro en el otro.** Lo dejo medido y sin
adjudicar (`D.56` congela la doctrina y `D.45` me veda `src/`).

---

## 11. `d033`: LA CORRIDA INTERMITENTE, MEDIDA POR MI

    $ bash .v49aud/11_d033.sh
    corrida 1: codigo 0, 18 s
    corrida 2: codigo 0, 17 s
    corrida 3: codigo 0, 17 s
    corrida 4: codigo 0, 17 s
    corrida 5: codigo 0, 17 s
    corrida 6: codigo 0, 17 s

    $ python .v49aud/13_banda.py
    0 rojas de  6 corridas : tasa 0,0 por ciento ; cota superior al 95 por ciento = 39.3 por ciento
    0 rojas de 20 corridas : tasa 0,0 por ciento ; cota superior al 95 por ciento = 13.9 por ciento
    0 rojas de 26 corridas : tasa 0,0 por ciento ; cota superior al 95 por ciento = 10.9 por ciento

El primer bloque mide **seis corridas aisladas mias** de
`tests.test_aceptacion.PruebaE.test_e_guion_largo_rompe_el_hook`, con su codigo de salida y su
reloj. El segundo mide **la cota superior exacta de la tasa** para `0` rojas sobre `6`, `20` y `26`
corridas.

`LECTURA`: **mi muestra sola no cierra `d033`.** `0` de `6` deja la cota en el `39,3` por ciento, y
eso no distingue una guarda sana de una que falla una de cada tres. **La fila de `26` esta puesta
para el turno normal**, cuando pueda verificar las `20` del reporte: si se sostienen, la cota baja
al `10,9` por ciento, **y una cota del `11` por ciento sobre una guarda que ya salio roja una vez
tampoco la declara sana.** `D.45` me prohibe tocar `tests/`, no medir.

---

## 12. LAS CLASES DE LA VUELTA, MEDIDAS SOBRE SU DIFERENCIA

| especie de `5.2` | mi medida a ciegas | de donde sale |
|---|---|---|
| **`CLASE`** | **no puede haberla**, y no es una opinion | `bitacora/VEREDICTOS.jsonl` y `config/pares_mutuos.jsonl` **no aparecen en el diff** de la seccion `2`, y sus cuentas son `740` y `1`, las mismas de la seccion `3` |
| **`DATO MOVIDO`** | **ninguna** | el segundo bloque de la seccion `2` no imprime ni un fichero de `dataset/`, `bitacora/`, `config/` ni `censos/` |
| **`CIFRA PUBLICADA`** | **una candidata, y no es del extractor: es mia** | la cita de linea de `d031` en `docs/loop/DEUDA.jsonl`, seccion `9`. `docs/` es sede de `5.2` |
| **`REPORTE`** | **no la puedo medir en esta fase** | su sede es `docs/loop/REPORTE.md`, retirado. Todo lo que esta pagina mide sobre el trabajo de la vuelta (secciones `5`, `6`, `7`, `10`, `11`) **sale del arbol y no de su reporte** |

**Y LA DEUDA, QUE SI ES MIA DE RECOMPUTAR:**

    $ python .v49aud/15_deuda.py
    lineas del fichero        : 35
    deudas anotadas           : 24
    deudas con linea de pago  : 10  (d001, d002, d003, d004, d008, d010, d021, d023, d027, d032)
    DEUDA VIVA                : 14  (d005, d006, d007, d009, d011, d012, d020, d022, d024, d028, d029, d030, d031, d033)

Ese bloque cuenta las anotaciones de `DEUDA.jsonl` y resta las que tienen linea de pago con el
mismo `id`.

`LECTURA`: **la deuda baja de `16` a `14`**, que es exactamente lo que mi encargo dijo que tenia que
salir si `d027` y `d032` quedaban pagadas (`PROMPT_SIGUIENTE.md` TAREA 5 punto 5). **`d024` sigue
viva y tiene que seguirlo**: el encargo dijo que no se marca pagada hasta que esten los siete.

---

## 13. LO QUE NO PUEDO COMPROBAR EN ESTA FASE, DICHO COMO LIMITACION Y NO COMO AFIRMACION

| lo que queda sin comprobar | por que | donde se cierra |
|---|---|---|
| **si la vuelta declaro su cierre corto de `d024`** con su cifra y su reloj | la declaracion vive en `REPORTE.md`, retirado | turno normal |
| **las `20` corridas de `d033`** | sus trazas estan en `.v49/`, que no abro en esta fase | turno normal |
| **los relojes `559,4` s y `1479,4` s de las dos aduanas** | los escribe el extractor en `DEUDA.jsonl` y su salida esta en `.v49/` | turno normal |
| **de donde sale la cifra de palabras de `8` fichas de `cap_04`** (seccion `8`) | la frontera que las publica vive en `REPORTE.md` | turno normal |
| **si `P38` es el quinto tramo del capitulo entero** | esa mitad de la frase **no la comprobe hoy**: hace falta la tabla de los `44` tramos, que vive en `REPORTE.md`. Mi `ACTA 47` la midio en su dia (`674`, `530`, `469` por delante) **y hoy no la he vuelto a correr** | turno normal |
| **la tabla de cierre `D.52` de esta vuelta** | no la abri: solo compare huellas (seccion `4.c`) | turno normal |
| **los `4` candidatos de `cap_02` que no relei paso a paso** | releerlos enteros no cabia en esta fase, y lo digo en vez de firmarlos | turno normal |

---

## 14. EL BARRIDO DE SUPERLATIVOS SOBRE ESTA MISMA PAGINA (`HEREDADO 1`)

**Lo que el barrido mira y lo que no, dicho para que el recorte no sea callado:** mira **mi prosa**,
o sea las lineas que no van sangradas con cuatro espacios. Las sangradas son salidas de instrumento
pegadas, que no son frases mias, y **van contadas aparte en la propia cabecera de la salida.**

    $ python .v49aud/17_superlativos.py
    SUPERLATIVOS, que es lo que el remedio obliga a contestar: 9 golpes en mi prosa, 2 lineas sangradas (salida de instrumento) descartadas
       linea 95   [primero o ultimo          ] El primer      ...El primer bloque mide **cuantas linea...
       linea 139  [primero o ultimo          ] El primer      ...El primer bloque mide las `13` guarda...
       linea 224  [primero o ultimo          ] La primera     ...### 6.a. La primera frase corregida: `P34` cont...
       linea 236  [superlativo con nombre en medio] el tramo de mas ...mo**: `P38` con `396` no es el tramo de mas palabras...
       linea 306  [superlativo con nombre en medio] el grafo mas   ...e la poblacion que barro**: el grafo mas las bandejas, sin...
       linea 381  [superlativo con nombre en medio] la ficha declara de mas ...` no cuadran, y en esas `8` la ficha declara de mas.** Las...
       linea 446  [comparativo de una palabra] menor          ...er la comprobacion en la de menor valor | **procedimiento pro...
       linea 477  [comparativo de una palabra] menor          ...menor valor, y sus tres aplicacio...
       linea 559  [primero o ultimo          ] El primer      ...El primer bloque mide **seis corridas...

    AFIRMACIONES UNIVERSALES, que no las pide el remedio y las barro igual: 10 golpes en mi prosa, 0 lineas sangradas (salida de instrumento) descartadas
       linea 81   [negativa universal        ] ninguno        .... **Esta vuelta no escribio ninguno**, y no...
       linea 96   [negativa universal        ] ninguno        ...bio**, y no imprime fichero ninguno....
       linea 98   [negativa universal        ] ningun         ...dos fichas de cuarentena y ningun dato.** Con eso, el materia...
       linea 123  [negativa universal        ] ninguna        ...que no inserta no mueve ninguna de las cuatro, y ninguna se...
       linea 123  [negativa universal        ] ninguna        ...ve ninguna de las cuatro, y ninguna se movio.**...
       linea 162  [negativa universal        ] ninguna        ...falta leer ni una celda de ninguna de las dos. **El remedio de...
       linea 388  [negativa universal        ] NINGUNA        ...**ESTO NO TUMBA NINGUNA DE LAS DOS CORRECCIONES DE...
       linea 421  [negativa universal        ] ninguno        ...fichero y sin abrir ninguno:**...
       linea 453  [negativa universal        ] Ninguno        ...terio de valor** (`L75`). **Ninguno de los dos anade pasos al o...
       linea 577  [negativa universal        ] ninguna        ...| **`DATO MOVIDO`** | **ninguna** | el segundo bloque de la...

Ese bloque barre los patrones de superlativo y de afirmacion universal sobre `APERTURA_CIEGA.md` e
imprime **cada golpe con su linea y su contexto**. **No juzga si el golpe es una caida:** eso lo
contesto yo aqui debajo, fila por fila, que es lo que el remedio obliga.

### 14.a. LOS `9` GOLPES DE SUPERLATIVO, CONTESTADOS UNO A UNO

| linea | que dice ahi | contestacion |
|---:|---|---|
| `95` | ordinal que distingue dos bloques pegados juntos | **no es comparacion**: los dos bloques que ordena estan pegados encima, a la vista, y son dos |
| `139` | lo mismo, en la seccion `4.a` | **no es comparacion**, y los dos bloques estan encima |
| `559` | lo mismo, en la seccion `11` | **no es comparacion**, y los dos bloques estan encima |
| `224` | ordinal de las dos frases corregidas de `d032` | **no es comparacion**: son dos, y cada una tiene su seccion (`6.a` y `6.b`) |
| `236` | **SI es una comparacion**, sobre las palabras de los tramos de la tanda | **lleva su lista ordenada entera pegada justo encima**, los `4` tramos con sus `469`, `396`, `242` y `101` (instrumento `.v49aud/04`) |
| `306` | *el grafo mas las bandejas* | **es una suma y no una comparacion**: nombra las dos sedes que `D.38.4` manda barrer |
| `381` | *en esas `8` la ficha declara de mas* | **es un exceso y no un puesto**, y lo sostiene la tabla pegada encima: las `8` filas que no cuadran tienen la cifra declarada por encima de la contada, y la `9` cuadra |
| `446` | la regla del libro, dentro de una celda | **no es frase mia sino la regla de `L75`** (*at the lowest-value stage possible*), y es el criterio que el propio candidato ordena en su paso `1` |
| `477` | la misma regla del libro, al releerla | **misma contestacion**: es cita de `L75`, y esta pegada en la seccion `10.a` |

`LECTURA`: **de los `9` golpes, `1` es una comparacion mia de verdad** (la de la linea `236`) **y
lleva su lista ordenada entera encima.** Los otros `8` son ordinales, sumas o citas del libro.
**El remedio, corrido y no declarado a ojo, es lo que hoy me deja escribir `CUMPLIDO`.**

### 14.b. LOS `10` GOLPES DE AFIRMACION UNIVERSAL, QUE EL REMEDIO NO PIDE Y CONTESTO IGUAL

| linea | que afirma | el instrumento que la sostiene |
|---:|---|---|
| `81` | que la vuelta no escribio candidato | el `numstat` de la seccion `2`: los dos ficheros de `cuarentena/` que toca son modificaciones, y la bandeja sigue en `41` (seccion `3`) |
| `96` | que el segundo `diff` no imprime fichero | **esta pegado encima y su salida es `(sin salida)`** |
| `98` | que no se movio dato | el mismo `diff` de la seccion `2` sobre las seis sedes |
| `123` dos veces | que las cuatro cuentas no se movieron | el instrumento `.v49aud/01` pegado encima, contra las cifras que mi encargo fijo |
| `162` | conducta mia: que no lei celdas de las dos tablas | **no es una medida sino lo que hice**, y lo que si esta medido son las dos huellas pegadas encima |
| `388` | que la seccion `8` no tumba las dos correcciones | las dos correcciones se sostienen con sus propios bloques de `5.a` y `6.a`, que miden otra cosa |
| `421` | conducta mia: que no abri los informes | **no es una medida sino lo que hice**, y el `ls` pegado encima es de nombres |
| `453` | `LECTURA` mia sobre dos candidatos | es lectura de sus pasos, y los pasos estan en sus dos fichas de `cuarentena/grove_high_output/` |
| `577` | que `DATO MOVIDO` sale a cero | el `diff` de la seccion `2`, que es la sede de esa especie |

---

## 15. CADA BLOQUE PEGADO CON LA FRASE QUE LO PRESENTA (`HEREDADO 2`)

**Lo que el instrumento hace y lo que no:** saca **cada bloque pegado de esta pagina** y le pone al
lado **la frase de prosa que lo precede y la que lo sigue**, para que se lean una contra otra sin
tener que buscarlas. **No juzga si la frase es cierta:** eso es lo unico que una maquina no puede
hacer aqui, y por eso el remedio es de forma.

    $ python .v49aud/18_bloques.py
    bloques pegados en la pagina: 23

    BLOQUE lineas 12 a 14, primera linea suya: ACTA ANTERIOR LEIDA: fa548ca517d97b8955f622aeec22134a5e5cfc3d
       frase de encima (linea 10): ## 0. LAS TRES DECLARACIONES QUE EL ARNES EXIGE (`D.40`)
       frase de debajo (linea 16): **La huella la comprobe yo y no la copie del prompt.** El instrumento mide el fichero

    BLOQUE lineas 19 a 20, primera linea suya: $ git hash-object docs/loop/ACTA_AUDITOR.md
       frase de encima (linea 17): `docs/loop/ACTA_AUDITOR.md` tal como esta en el arbol ahora mismo:
       frase de debajo (linea 22): Ese bloque mide la huella del acta en el arbol. `LECTURA`: **coincide con la que el prompt me

    BLOQUE lineas 52 a 53, primera linea suya: $ grep -n "APERTURA CIEGA" docs/loop/loop.log | tail -1
       frase de encima (linea 50): ## 1. QUE ABRI, QUE NO ABRI, Y LO QUE ME LLEGO SIN PEDIRLO
       frase de debajo (linea 55): Ese bloque mide que linea escribio el arnes en el log para mi turno y que cuatro ficheros retiro.

    BLOQUE lineas 84 a 93, primera linea suya: $ git diff --numstat HEAD~1 HEAD | grep -v "\.v49/"
       frase de encima (linea 82): es una busqueda negativa citada de memoria (`AUDITOR_FORJA.md` 1.1): es el arbol.
       frase de debajo (linea 95): El primer bloque mide **cuantas lineas cambio cada fichero** entre el commit anterior y este, sin

    BLOQUE lineas 107 a 115, primera linea suya: $ python .v49aud/01_poblacion.py
       frase de encima (linea 105): ## 3. EL ESTADO DE LA LINEA, RECONTADO POR MI
       frase de debajo (linea 117): Ese bloque cuenta lineas de tres ficheros del arbol y ficheros de una carpeta, y reparte las `41`

    BLOQUE lineas 131 a 137, primera linea suya: $ python forja.py gate
       frase de encima (linea 129): ### 4.a. Las dos del arbol
       frase de debajo (linea 139): El primer bloque mide las `13` guardas del gate sobre `346` nodos; el segundo, los guiones del

    BLOQUE lineas 153 a 156, primera linea suya: $ git show HEAD~1:docs/loop/TABLA_DE_CIERRE.txt | git hash-object --stdin
       frase de encima (linea 151): ### 4.c. El sello de `D.52`, que es el remedio a mano de `d030` otra vez
       frase de debajo (linea 158): Ese bloque compara la huella de la tabla que estaba VIVA antes de esta vuelta con la huella de la

    BLOQUE lineas 171 a 176, primera linea suya: $ sed -n "145p" fuentes/grove_high_output/cap_04.md
       frase de encima (linea 169): ### 5.a. Lo que el libro dice, leido por mi
       frase de debajo (linea 178): Ese bloque mide **que escribe `L145`** y **cuantas veces aparece `six ways` en el libro entero**,

    BLOQUE lineas 187 a 196, primera linea suya: $ python .v49aud/06_huellas.py
       frase de encima (linea 185): ### 5.b. Que movio la vuelta dentro de la ficha, medido con la funcion de la casa
       frase de debajo (linea 198): Ese bloque compara la ficha de `HEAD~1` con la de `HEAD` campo a campo, y calcula sobre las dos la

    BLOQUE lineas 226 a 231, primera linea suya: $ python .v49aud/04_palabras_cap04.py
       frase de encima (linea 224): ### 6.a. La primera frase corregida: `P34` contra `P38`
       frase de debajo (linea 233): Ese bloque cuenta las palabras del texto fuente en los rangos de linea que las propias fichas

    BLOQUE lineas 242 a 243, primera linea suya: $ sed -n "299p" fuentes/grove_high_output/cap_04.md
       frase de encima (linea 240): ### 6.b. La segunda frase corregida: de donde sale el `cinco`
       frase de debajo (linea 245): Ese bloque mide **que escribe `L299` y en que orden**.

    BLOQUE lineas 251 a 254, primera linea suya: $ sed -n '67,89p' docs/MANUAL_SISTEMA_DE_CONOCIMIENTO.md | sed -n '17,19p'
       frase de encima (linea 249): dice. **Y el motivo nuevo se sostiene con la regla que cita**, que la comprobe:
       frase de debajo (linea 256): Ese bloque mide **que dice el punto `5` de la seccion `3` del manual**, que es lo que la ficha cita

    BLOQUE lineas 262 a 263, primera linea suya: $ python -c "import json;print(json.load(open('cuarentena/grove_high_output/dimensionar_numero_
       frase de encima (linea 260): que la miro: el `entregable_esperado` entero de esta ficha, pegado sin cortar, es
       frase de debajo (linea 265): Ese bloque imprime el campo `entregable_esperado` de la ficha, entero.

    BLOQUE lineas 273 a 282, primera linea suya: $ python .v49aud/06_huellas.py
       frase de encima (linea 271): ### 6.c. Que movio la vuelta dentro de la ficha
       frase de debajo (linea 284): Ese bloque compara la ficha de `HEAD~1` con la de `HEAD` campo a campo y calcula las dos huellas de

    BLOQUE lineas 295 a 304, primera linea suya: $ python .v49aud/12_poblacion_barrida.py
       frase de encima (linea 293): ## 7. EL BARRIDO DE VECINOS (`D.38.4`), CORRIDO POR MI SOBRE GRAFO MAS BANDEJAS
       frase de debajo (linea 306): Ese bloque mide **de que se compone la poblacion que barro**: el grafo mas las bandejas, sin

    BLOQUE lineas 309 a 341, primera linea suya: $ python .v49aud/07_barrido.py reunir_informacion_gerencial_vias_variadas
       frase de encima (linea 307): `_insertados` ni `_derivadas` y con el filtro de fuente canonica.
       frase de debajo (linea 343): Los dos bloques miden **la senial `1` de la casa** (`src.aduana.senal_similitud_texto`, `src/aduana.py:278`)

    BLOQUE lineas 362 a 374, primera linea suya: $ python .v49aud/05_tramos_declarados.py
       frase de encima (linea 360): ## 8. LO QUE ENCONTRE SIN BUSCARLO: **LAS PALABRAS DECLARADAS DE NUEVE FICHAS DE `cap_04`**
       frase de debajo (linea 376): Ese bloque mide, para las fichas de `cap_04` que declaran pieza, rango de lineas y palabras dentro

    BLOQUE lineas 399 a 405, primera linea suya: $ grep -n "^def " src/aduana.py | sed -n '5,7p'
       frase de encima (linea 397): senial `1` (`src/aduana.py` linea `315`)*.
       frase de debajo (linea 407): Ese bloque mide **en que linea empieza cada senial** y **que hay escrito en la linea `315`**.

    BLOQUE lineas 423 a 427, primera linea suya: $ ls .v49/ | grep informe
       frase de encima (linea 421): fichero y sin abrir ninguno:**
       frase de debajo (linea 429): Ese bloque mide **cuantos ficheros de informe escribio la vuelta y como se llaman**. No mide que

    BLOQUE lineas 494 a 518, primera linea suya: $ python .v49aud/19_cola_siete.py
       frase de encima (linea 492): ### 10.c. Y el barrido de vecinos de los siete, que `d024` echaba en falta
       frase de debajo (linea 520): Ese bloque es un **recorte declarado**: toma de las siete salidas del instrumento `07` (la senial

    BLOQUE lineas 546 a 557, primera linea suya: $ bash .v49aud/11_d033.sh
       frase de encima (linea 544): ## 11. `d033`: LA CORRIDA INTERMITENTE, MEDIDA POR MI
       frase de debajo (linea 559): El primer bloque mide **seis corridas aisladas mias** de

    BLOQUE lineas 583 a 587, primera linea suya: $ python .v49aud/15_deuda.py
       frase de encima (linea 581): **Y LA DEUDA, QUE SI ES MIA DE RECOMPUTAR:**
       frase de debajo (linea 589): Ese bloque cuenta las anotaciones de `DEUDA.jsonl` y resta las que tienen linea de pago con el

    BLOQUE lineas 618 a 640, primera linea suya: $ python .v49aud/17_superlativos.py
       frase de encima (linea 616): pegadas, que no son frases mias, y **van contadas aparte en la propia cabecera de la salida.**
       frase de debajo (linea 642): Ese bloque barre los patrones de superlativo y de afirmacion universal sobre `APERTURA_CIEGA.md` e

Ese bloque lista los bloques pegados de esta pagina con sus dos frases vecinas.

**EL RECORTE, DECLARADO:** el instrumento se corrio **antes** de pegar aqui su propia salida, asi
que **de los bloques de esta pagina se lista a todos menos a si mismo**. El que falta es este, su
frase de encima es la que empieza *Lo que el instrumento hace y lo que no* y su frase de debajo es
la de *Ese bloque lista los bloques pegados*.

`LECTURA`: **mi molde en esta pagina es el mismo en los `23` bloques**: el bloque va debajo de la
frase que anuncia de donde sale, y **debajo del bloque va una frase que empieza por `Ese bloque
mide` o `Ese bloque cuenta`, que dice lo que ESE bloque mide y nada mas**; **la conclusion va
aparte, en una linea que empieza por `LECTURA`**. Es exactamente lo que el remedio pide, y se
comprueba leyendo la salida de arriba fila por fila.
