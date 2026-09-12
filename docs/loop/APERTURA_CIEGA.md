# APERTURA CIEGA DEL AUDITOR, vuelta 16 (lote 4, `scott_radical_candor`)

**Fecha de la fase:** 12 sep 2026. **Rama:** `extraccion-mundo-11`. **HEAD al abrir:**
`da62e73`.

Esta es la lectura que hago **antes de ver `docs/loop/REPORTE.md`**, para poder
compararla despues con la del extractor. Manda `D.34` (el arnes retira los cuatro
ficheros y sella esto), `D.38.3` (**clases y lecturas, no cifras contadas a mano**:
toda cifra lleva su instrumento y su salida literal al lado) y `D.38.4` (**el
barrido es sobre GRAFO MAS BANDEJAS**).

---

## 0. LO QUE HE MIRADO Y LO QUE NO. CONTAMINACION DECLARADA

**No he recuperado ninguno de los cuatro ficheros retirados.** No he abierto
`REPORTE.md`, ni `loop.log`, ni `ultimo_extractor.json`, ni `ultimo_auditor.json`,
ni por `git show`, ni por `git checkout`, ni por ninguna otra via.

**PERO ME HE CONTAMINADO POR UN SITIO Y LO DIGO YO.** El protocolo seccion 1.1 me
manda correr `git log`, y lo corri. Los **cuerpos de los tres commits de la vuelta
16 resumen el reporte con sus cifras**:

    $ git log --oneline -3
    da62e73 EL CIERRE DE LA VUELTA 16: dos capitulos enteros, 17 candidatos, 185 pasos, una arista y cero inserciones porque el lote esta abierto
    7c3e224 cap_06 del lote 4 (Cap. 3, Understand What Motivates Each Person on Your Team): 10 candidatos, 117 pasos, cero puentes
    e65991d cap_05 del lote 4 (Cap. 2, Get, Give, and Encourage Guidance): 7 candidatos, 68 pasos, 2 puentes retirados en el acto

Y el cuerpo de `da62e73` traia ademas cuatro porcentajes de pasos inventados y dos
cifras de palabras. **Asi que mi lectura de esas cifras NO es ciega**, y lo escribo
aqui antes de que nadie me lo pregunte. Lo que si es ciego, y es lo que esta
apertura vale: **la clasificacion candidato a candidato y paso a paso contra el
libro, que ningun commit resume.** Toda cifra que publico abajo la he **remedido
con mi instrumento**, y **donde mi medida discrepa de la del commit, lo digo.**

**`D.34` dice que el arnes retira cuatro ficheros. No dice que retire el `git log`,
y el `git log` de esta casa lleva el reporte dentro.** Eso es un agujero del
mecanismo, no una caida de nadie, y lo traigo como encargo a mi turno normal.

---

## 1. LOS INSTRUMENTOS DE ESTA FASE, CON SU SALIDA LITERAL

### 1.1. Tamanio de lo leido (`wc -l`, `wc -w`)

    $ wc -l fuentes/scott_radical_candor/cap_05.md fuentes/scott_radical_candor/cap_06.md
       311 fuentes/scott_radical_candor/cap_05.md
       359 fuentes/scott_radical_candor/cap_06.md
       670 total

    $ wc -w fuentes/scott_radical_candor/cap_05.md fuentes/scott_radical_candor/cap_06.md
      8786 fuentes/scott_radical_candor/cap_05.md
     11620 fuentes/scott_radical_candor/cap_06.md
     20406 total

**He leido los dos capitulos enteros, las 670 lineas, no una muestra.**

### 1.2. Estado del grafo y de la bandeja (`wc -l`, `ls | wc -l`)

    $ wc -l dataset/nodos.jsonl
    203 dataset/nodos.jsonl

    $ ls cuarentena/scott_radical_candor/*.json | wc -l
    25

    $ ls cuarentena/_insertados/
    onu_consumidor
    smart_who
    zhuo_manager

**El lote 4 no ha insertado ni un nodo: `_insertados/` no tiene su carpeta.**

### 1.3. Contador de pasos, candidato a candidato

    $ python -c "... len(d['pasos_accionables']) ... for cuarentena/scott_radical_candor/*.json"
    acompaniar_mejores_equipo_socio.json                 pasos 11
    ajustar_franqueza_oido_oyente.json                   pasos  8
    cambiar_potencial_trayectoria_crecimiento.json       pasos 14
    criticar_trabajo_evitar_desanimo.json                pasos 14
    cuidar_persona_completa_equipo.json                  pasos 10
    dar_critica_inmediata_ayuda_tangible.json            pasos 10
    decidir_momento_despedir_persona.json                pasos 12
    delimitar_franqueza_radical_cinco_noes.json          pasos  9
    descubrir_motivacion_sentido_persona.json            pasos 13
    despedir_persona_franqueza_radical.json              pasos 11
    desplegar_marco_franqueza_radical.json               pasos  9
    elogiar_trabajo_especifico_contexto.json             pasos  7
    empezar_cultura_franqueza_radical.json               pasos  6
    equilibrar_elogio_critica_equipo.json                pasos  9
    imaginar_caso_simple_bragueta_abierta.json           pasos 11
    invitar_desafio_reciproco_equipo.json                pasos  7
    manejar_enfado_persona_desafiada.json                pasos  7
    pedir_critica_equipo_premiarla.json                  pasos 11
    reconocer_recompensar_gente_estable.json             pasos 12
    repartir_semana_cuarenta_horas_jefe.json             pasos  7
    retar_superestrellas_equipo_constantemente.json      pasos 13
    retirar_etiquetas_permanentes_equipo.json            pasos 10
    revisar_ciclo_responsabilidades_relaciones.json      pasos  7
    revisar_cinco_causas_mal_desempenio.json             pasos 11
    subir_vara_calidad_equipo.json                       pasos 10
    TOTAL pasos_accionables en la bandeja: 249

**De ahi salen, sumados por el mismo instrumento, los 17 candidatos de esta vuelta:**
`cap_05` (los 7 de `e65991d`) = 14+10+7+6+9+11+11 = **68 pasos**; `cap_06` (los 10 de
`7c3e224`) = 11+14+12+13+11+12+13+10+11+10 = **117 pasos**; **total 185**. Coincide
con lo que dice el asunto del commit, y lo digo habiendolo contado yo.

### 1.4. Aristas declaradas (contador propio, corrido en esta fase)

    GRAFO: 203 nodos | nodos_previos 79 | nodos_siguientes 79
    BANDEJA scott_radical_candor: 25 candidatos | previos 0 | siguientes 0 | SIN NINGUNA ARISTA: 25

**Esto NO es una caida y lo digo antes de que parezca una.** `D.37` dice que la
arista cabeza a parte *"se declara por lectura **en el acto de insertar**"*, y el
lote 4 esta abierto y no ha insertado nada. **Cero aristas en la bandeja es el
estado correcto.** Lo que si queda anotado es **la deuda de aristas que la
insercion va a tener que pagar**, y la nombro en la seccion 4.

### 1.5. Barrido de vecinos sobre GRAFO MAS BANDEJAS (`D.38.4`)

**La poblacion, construida con el metodo literal del banco y medida:**

    $ python -c "... dataset/nodos.jsonl + glob('cuarentena/*/*.json') sin _insertados ni _derivadas ..."
    $ wc -l .poblacion_auditor_v16.jsonl
    391 .poblacion_auditor_v16.jsonl

    $ wc -l .poblacion_auditor_v16_sin_ensayo.jsonl
    228 .poblacion_auditor_v16_sin_ensayo.jsonl

**391 = 203 del grafo + 188 de bandejas** (163 de `ensayo_referencia_163` + 25 del
lote 4). **228 es la misma poblacion sin el catalogo de control.** Publico las dos
porque la diferencia decide el barrido y el banco no la resuelve: `D.38.4` globea
`cuarentena/*/*.json` sin excepcion, y `ensayo_referencia_163` **es el catalogo de
referencia** (`cuarentena/_derivadas/FUENTES_DEL_CONTROL.json`), no un lote
esperando entrar. **No lo resuelvo yo aqui: lo declaro y lo traigo.**

**LO QUE EL BARRIDO DE LAS TRES SENIALES DIO, Y LO QUE NO.** Corri
`src.aduana.buscar_vecinos` (el instrumento de la casa) en modo *leave one out*
contra los 390 restantes. **Termino 2 de los 17 dentro de esta fase y los publico
enteros; los otros 15 seguian corriendo al cerrar.** Salida literal de los dos que
cerraron:

    POBLACION DEL BARRIDO (D.38.4)
      grafo dataset/nodos.jsonl : 203
      bandejas cuarentena/*/    : 188
      TOTAL                     : 391
      umbrales: sim 0.35 | fam 0.3 | paso 0.6

    ### acompaniar_mejores_equipo_socio.json   (contra 390)
        SIN VECINOS: ninguna senial levanta nada

    ### cambiar_potencial_trayectoria_crecimiento.json   (contra 390)
        vecino cambiar_mentalidad_fija_crecimiento  [levantada por: familia_id]
          similitud_texto 0.228 | familia_id 0.333 | paso_contra_nodo 0.439
          paso 12 del candidato contra paso 3 de cambiar_mentalidad_fija_crecimiento

**LA PRIMERA DE ESAS DOS LINEAS ES EL HALLAZGO DE ESTA APERTURA**, y la desarrollo
en 3.B: `acompaniar_mejores_equipo_socio` **no levanta ni un vecino con las tres
seniales sobre los 391**, y sin embargo tiene en el grafo un nodo que dice lo mismo
en tres de sus pasos. **El barrido entero, con la poblacion que `D.38.4` manda, es
ciego a ese par.**

**Por que no termino el resto**, medido en vez de estimado:

    COSTE DEL BARRIDO DE TRES SENIALES (src.aduana.medir)
      candidato medido : acompaniar_mejores_equipo_socio
      pares medidos    : 40
      segundos         : 26.15
      segundos por par : 0.654
      poblacion D.38.4 : 391
      pares del lote 16: 17 x 390 = 6630

**`src.aduana._ratio` es `difflib.SequenceMatcher(autojunk=False)` a nivel de
caracter**, y los nodos de este libro son largos. **El extractor choco con el mismo
muro en esta misma vuelta**, y su testigo lo prueba:

    $ ls -la .barrido_C_con_ensayo_v16.txt .barrido_D_grafo_solo_v16.txt
    -rw-r--r-- 1 AlexDesk 197609       0 Sep 11 23:25 .barrido_C_con_ensayo_v16.txt
    -rw-r--r-- 1 AlexDesk 197609    2584 Sep 11 23:23 .barrido_D_grafo_solo_v16.txt

**`.barrido_C_con_ensayo_v16.txt` esta en CERO BYTES.** El barrido sobre grafo mas
bandejas no completo, y el que si completo (`.barrido_D`) es **solo contra el
grafo**, que es justo la poblacion que `D.38.4` prohibe usar sola. **Si el reporte
cita ese fichero de cero bytes como prueba de una corrida, es CIFRA PUBLICADA por
la clausula 7.B de la cosecha** (*"la ruta que promete prueba es cifra"*, y un
testigo en cero bytes cuenta como turno mudo). **Lo dejo anotado aqui, sellado,
antes de leer el reporte.**

### 1.6. Barrido que SI completo: senial `familia_id` sobre los 391

Corrido con `src.aduana.senal_familia_id` sobre la poblacion entera de `D.38.4`.
**Salida literal, completa, los 17 candidatos:**

    POBLACION DEL BARRIDO (D.38.4): grafo 203 + bandejas 188 = 391
    senial barrida: familia_id | umbral 0.3

    ### acompaniar_mejores_equipo_socio   (contra 390)
        SIN VECINOS por familia_id
    ### cambiar_potencial_trayectoria_crecimiento   (contra 390)
        familia_id 0.333  [GRAFO] cambiar_mentalidad_fija_crecimiento
    ### criticar_trabajo_evitar_desanimo   (contra 390)
        SIN VECINOS por familia_id
    ### dar_critica_inmediata_ayuda_tangible   (contra 390)
        SIN VECINOS por familia_id
    ### decidir_momento_despedir_persona   (contra 390)
        familia_id 0.333  [GRAFO] elegir_recolocar_despedir_persona
        familia_id 0.333  [GRAFO] despedir_persona_respeto_franqueza
        familia_id 0.333  [BANDEJA] despedir_persona_franqueza_radical
    ### descubrir_motivacion_sentido_persona   (contra 390)
        SIN VECINOS por familia_id
    ### despedir_persona_franqueza_radical   (contra 390)
        familia_id 0.600  [GRAFO] despedir_persona_respeto_franqueza
        familia_id 0.333  [GRAFO] elegir_recolocar_despedir_persona
        familia_id 0.333  [BANDEJA] empezar_cultura_franqueza_radical
        familia_id 0.333  [BANDEJA] desplegar_marco_franqueza_radical
        familia_id 0.333  [BANDEJA] decidir_momento_despedir_persona
    ### elogiar_trabajo_especifico_contexto   (contra 390)
        SIN VECINOS por familia_id
    ### empezar_cultura_franqueza_radical   (contra 390)
        familia_id 0.333  [BANDEJA] desplegar_marco_franqueza_radical
        familia_id 0.333  [BANDEJA] despedir_persona_franqueza_radical
    ### equilibrar_elogio_critica_equipo   (contra 390)
        familia_id 0.333  [BANDEJA] pedir_critica_equipo_premiarla
    ### imaginar_caso_simple_bragueta_abierta   (contra 390)
        SIN VECINOS por familia_id
    ### pedir_critica_equipo_premiarla   (contra 390)
        familia_id 0.333  [BANDEJA] equilibrar_elogio_critica_equipo
    ### reconocer_recompensar_gente_estable   (contra 390)
        familia_id 0.333  [GRAFO] reconocer_recompensar_uso_metodo
    ### retar_superestrellas_equipo_constantemente   (contra 390)
        SIN VECINOS por familia_id
    ### retirar_etiquetas_permanentes_equipo   (contra 390)
        SIN VECINOS por familia_id
    ### revisar_cinco_causas_mal_desempenio   (contra 390)
        SIN VECINOS por familia_id
    ### subir_vara_calidad_equipo   (contra 390)
        SIN VECINOS por familia_id

**La cifra mas alta del lote es `0.600`, el doble del umbral**, y es
`despedir_persona_franqueza_radical` contra `despedir_persona_respeto_franqueza`,
que ya vive en el grafo.

### 1.7. Barrido de adyacencia por lectura, sobre la poblacion entera

Como el barrido de tres seniales no completo, **no me quedo sin poblacion barrida:
la barro por termino**, con el instrumento corrido en esta fase y su salida
contada.

    poblacion total revisada: 366   (203 del grafo + 163 de las otras bandejas, excluida la bandeja del propio lote)
    con termino de la familia del lote: 97

De esos 97 **abri y lei los pasos completos de los cinco vecinos mas cercanos por
lectura**, que son los que adjudico en la seccion 3:
`despedir_persona_respeto_franqueza`, `elegir_recolocar_despedir_persona`,
`repartir_tiempo_atencion_mejores_equipo`, `dar_opinion_critica_directa_desapasionada`
y `diagnosticar_falta_motivacion_habilidad`, los cinco de `zhuo_manager`.

---

## 2. MI CLASIFICACION, CANDIDATO A CANDIDATO

**Cada fila dice: si lo leo como PROCEDIMIENTO o como POSTURA, cuantos pasos leo
como TRANSCRIPCION y cuantos como PUENTE, y las lineas del libro que lo
sostienen.** He leido los 185 pasos uno a uno contra su parrafo.

### 2.A. Los siete de `cap_05` (Cap. 2, *Get, Give, and Encourage Guidance*)

| candidato | clase | pasos | transcripcion / puente | lineas que lo sostienen |
|---|---|---|---|---|
| `dar_critica_inmediata_ayuda_tangible` | **PROCEDIMIENTO** | 10 | **10 / 0** | `cap_05.md` L11-39 (la historia del *um*) y L43 (el parrafo que desmonta los medios uno a uno) |
| `elogiar_trabajo_especifico_contexto` | **PROCEDIMIENTO** | 7 | **7 / 0** | L75-83 (*I admire that about you*), L205-211 (*Just trying to say something nice*), L131-165 (el correo de los bonos) |
| `criticar_trabajo_evitar_desanimo` | **PROCEDIMIENTO** | 14 | **14 / 0** | L245-279 (la frontera peligrosa, con L261 el error de atribucion y L271 la lista) y L119-127 (el analisis del correo propio) |
| `equilibrar_elogio_critica_equipo` | **PROCEDIMIENTO** | 9 | **9 / 0** | L231-243, con L237 (los ratios y el sandwich) y L243 (Karen Sipprell) |
| `pedir_critica_equipo_premiarla` | **PROCEDIMIENTO** | 11 | **11 / 0** | L217-229, con L221 (las cuatro razones numeradas) y L229 (Toyota y el te de Tokio) |
| `imaginar_caso_simple_bragueta_abierta` | **PROCEDIMIENTO** | 11 | **11 / 0** | L281-309, con L283-285 (el escenario) y L297 (Kim Vorrath) |
| `empezar_cultura_franqueza_radical` | **DISCUTIBLE, ver 3.E** | 6 | **6 / 0** | L213-215, un solo parrafo |

**cap_05: 68 pasos leidos, 68 los leo como transcripcion, 0 como puente.**

**Lo que esto NO dice:** los dos puentes que el asunto del commit `e65991d` declara
retirados **no los puedo ver**, porque lo que hay en la bandeja es el fichero ya
corregido. **Mi 0 de 68 es sobre el texto final, no sobre el borrador**, y lo digo
para que nadie lea mi cifra como un desmentido de la suya. Si el reporte declara 2
de 68 sobre el borrador, **las dos cifras son compatibles y miden cosas
distintas**, y eso es lo que habra que cuadrar.

### 2.B. Los diez de `cap_06` (Cap. 3, *Understand What Motivates Each Person on Your Team*)

| candidato | clase | pasos | transcripcion / puente | lineas que lo sostienen |
|---|---|---|---|---|
| `cambiar_potencial_trayectoria_crecimiento` | **PROCEDIMIENTO** | 14 | **14 / 0** | L11-67, con L27-43 (las dos columnas, transcritas exactas) y L55-65 (las nueve casillas y las tres preguntas) |
| `descubrir_motivacion_sentido_persona` | **PROCEDIMIENTO** | 13 | **13 / 0** | L87 (las tres cosas que averiguar) y L99-111 (el problema de la pasion, con L101 Spinoza, L103 Kellaway y L107-111 Wren) |
| `acompaniar_mejores_equipo_socio` | **PROCEDIMIENTO** | 11 | **11 / 0** | L113-129, con L123 (Costolo), L125 (la cuenta del minuto) y L127 (arremangarse) |
| `reconocer_recompensar_gente_estable` | **PROCEDIMIENTO** | 12 | **12 / 0** | L153 (las vias), L155-159 (*Fair performance ratings*), L161-175 (*Recognition*), L177-183 (*Respect*), L185-193 (la obsesion por la promocion) |
| `retar_superestrellas_equipo_constantemente` | **PROCEDIMIENTO** | 13 | **13 / 0** | L199-217 (los seis medios), L219-227 (las dos salvaguardas), L229-241 (crecer no es dirigir) |
| `subir_vara_calidad_equipo` | **PROCEDIMIENTO** | 10 | **10 / 0** | L243-259, con L253-257 (la politica de los dos anios) |
| `decidir_momento_despedir_persona` | **PROCEDIMIENTO** | 12 | **12 / 0** | L271-291 (las tres preguntas y las cuatro mentiras, numeradas por el libro) |
| `despedir_persona_franqueza_radical` | **PROCEDIMIENTO, ver 3.A** | 11 | **11 / 0** | L293-303, con L269 (los sudores frios) y L297-299 (el verano de cajera) |
| `revisar_cinco_causas_mal_desempenio` | **PROCEDIMIENTO** | 11 | **11 / 0** | L305-341: L307 dice **cinco** razones y el libro las despliega bajo **cuatro** rotulos (L311, L323, L331, L337) |
| `retirar_etiquetas_permanentes_equipo` | **PROCEDIMIENTO** | 10 | **10 / 0** | L343-357, con L349 (los tres nombres de trimestre de Jared Smith) |

**cap_06: 117 pasos leidos, 117 los leo como transcripcion, 0 como puente.**

**LA LECTURA QUE MAS ME COSTO Y QUE SOSTENGO:** `revisar_cinco_causas_mal_desempenio`
dice **cinco** causas y el capitulo solo pone **cuatro rotulos**. Fui a comprobar si
la quinta era invento, y **no lo es**: `cap_06.md` L307 dice literalmente *"five
different reasons that are worth parsing"*, y el rotulo de L323
(*"New to role; too much too fast"*) **lleva dos causas dentro con dos mecanismos
distintos**. La cuenta es del libro, no del lector. **`D.37` se aplica bien aqui.**

### 2.C. Los dos arreglos en frio de la vuelta (`3847c9d`)

| fichero | que cambio | mi clase |
|---|---|---|
| `delimitar_franqueza_radical_cinco_noes` | de 8 a 9 pasos: entra el peldanio que faltaba del tercer no | **ARREGLO CORRECTO.** El imperativo existe y lo verifique: `cap_04.md` **L147**, *"leave three unimportant things unsaid each day"* |
| `cuidar_persona_completa_equipo` | entra el campo `atribuciones` (maxima de Kofman) y se reindenta; los 10 pasos no se tocan | **ARREGLO CORRECTO.** `atribuciones` esta en `esquema/nodo.schema.json` `properties`, comprobado, asi que no rompe la aduana |

> **DISCREPANCIA DECLARADA, y el instrumento manda.** El cuerpo del commit `3847c9d`
> situa ese imperativo en **`cap_04.md` L149**. Mi `grep -n` lo situa en **L147**;
> L149 es el no siguiente, el de *"not a hierarchical thing"*. **El asunto de un
> commit no es sede de cifra** (5.6), asi que esto no acumula por si solo. **Pero si
> ese mismo L149 esta escrito en `REPORTE.md`, ahi si es sede**, y entonces es
> especie REPORTE. Queda apuntado para cuadrarlo.

### 2.D. Los ocho candidatos viejos de la bandeja

Los lei tambien, porque son vecinos de los 17 por `D.38.4` y porque sin ellos no
puedo juzgar el solape dentro del lote: `desplegar_marco_franqueza_radical`,
`ajustar_franqueza_oido_oyente`, `invitar_desafio_reciproco_equipo`,
`manejar_enfado_persona_desafiada`, `revisar_ciclo_responsabilidades_relaciones`,
`repartir_semana_cuarenta_horas_jefe`, mas los dos de 2.C. **Ninguno de los 17 de
esta vuelta lo leo como gemelo de ninguno de esos ocho.**

---

## 3. LOS PARES QUE YO MARCARIA COMO DISCUTIBLES, ADJUDICADOS CON LA VARA

Marco **cinco**. Los adjudico **leyendo los pasos**, no citando una senial, que es
lo que manda `D.19`. Publico mi clase **antes** de saber cual marco el extractor.

### 3.A. `despedir_persona_franqueza_radical` (bandeja) contra `despedir_persona_respeto_franqueza` (grafo, `zhuo_manager`)

**Es el par mas cercano del lote por los dos caminos: por senial (`familia_id 0.600`,
el doble del umbral) y por lectura.** Las dos activaciones son la misma: *"ya has
decidido y toca la conversacion"*.

**Lo que el HIJO aniade a la MADRE** (y la pregunta va en esa direccion, nunca al
reves): los dos recordatorios numerados por el libro con su mecanica, **imaginar
antes de la reunion cual seria concretamente el trabajo bueno para esa persona**,
**ofrecer una presentacion**, y la reformulacion *"no es la persona la que es mala,
es el puesto el que es malo para esa persona"*. Nada de eso esta en el nodo de
`zhuo_manager`, que se queda en *"ayudala a ponerse en el mejor camino"* sin decir
como.

**Lo que la MADRE deja fuera:** no abrirlo a discusion, no alargar la ruptura, la
calle de dos sentidos, y usar la experiencia para mejorar como jefe. Tampoco esta
en el hijo.

> **MI CLASE: CONTINUA. Queda fuera procedimiento en los dos lados**, que es lo que
> `6.1` manda mirar, y el solape es el marco compartido, no el procedimiento.
> **La arista no exculpa y aqui ademas no existe: la deuda de arista queda anotada.**

### 3.B. `acompaniar_mejores_equipo_socio` contra `repartir_tiempo_atencion_mejores_equipo` (grafo, `zhuo_manager`)

**EL CASO QUE MAS ME IMPORTA DE ESTA APERTURA, y no por su veredicto sino por lo
que demuestra.** Es **uno de los dos candidatos cuyo barrido de las TRES seniales
completo** sobre los 391 de `D.38.4`, y su salida literal es esta:

    ### acompaniar_mejores_equipo_socio.json   (contra 390)
        SIN VECINOS: ninguna senial levanta nada

**Cero vecinos con las tres seniales sobre grafo mas bandejas.** La lectura dice que
es el segundo par mas cercano del lote.

El solape es real y es de paso contra paso: el paso 5 del candidato (*"cada minuto
que pasas con alguien que hace un gran trabajo rinde mucho mas"*) y su paso 10 (*"no
dediques mas tiempo a quien va mal que a quien va bien"*) **dicen lo mismo** que los
pasos 2, 4 y 6 del nodo que ya vive.

**Lo que el hijo aniade:** el marco socio / jefe ausente / microgestor, las **cuatro
consecuencias** de ignorar a los mejores, y los **cuatro actos** del socio (saber el
detalle, ayudar con los obstaculos, arremangarse a hacer el trabajo, preguntar y
desafiar). **Lo que la madre deja fuera:** la cuenta del puesto de limonada, la
comparacion con los consejeros delegados y los inversores, y el *diagnostica y
resuelve rapido lo del que se atasca*.

> **MI CLASE: CONTINUA, con dos pasos gemelos declarados.** No fusion: el solape es
> la premisa, y el procedimiento es distinto en los dos lados.
>
> **Y ESTE PAR ES EL EJEMPLAR DE `D.19` DE ESTA CASA, medido y no supuesto.**
> *"Ninguna senial separa jerarquia de ruido."* Aqui **las tres seniales juntas, con
> la poblacion entera de `D.38.4`, devuelven CERO** para el par que la lectura
> encuentra; mientras tanto la senial que si grita en el lote
> (`reconocer_recompensar_gente_estable` contra `reconocer_recompensar_uso_metodo`,
> `familia_id 0.333`) es **ruido puro**: premiar a quien usa un metodo de
> contratacion no tiene nada que ver con premiar a la gente estable. **La senial
> callo donde habia que leer y grito donde no habia nada.** El barrido dijo donde
> mirar y ahi acabo su trabajo.
>
> **Y de aqui sale el encargo que llevo a mi turno normal:** si la aduana no levanta
> este par, **el par no entra en ninguna cola de lectura al insertar**, y el gemelo
> de dos pasos entra al grafo sin que nadie lo mire. **Eso no lo arregla un umbral
> mas bajo**, que es justo lo que `config/umbrales.json` prohibe que decida solo;
> lo arregla que la lectura del lote lo traiga escrito, y por eso lo escribo aqui.

### 3.C. `revisar_cinco_causas_mal_desempenio` contra `diagnosticar_falta_motivacion_habilidad` (grafo, `zhuo_manager`)

Mismo objeto declarado: **por que alguien bueno esta rindiendo mal**. Pero las dos
taxonomias son distintas y las dos son del libro que las trae: Zhuo parte en dos por
Grove (**no sabe** o **no quiere**) y abre tres submotivos de desmotivacion; Scott
parte en **cinco** (papel equivocado, recien llegado, demasiado de golpe, problema
personal, mal encaje) y **asigna la culpa al jefe en la primera**.

> **MI CLASE: FRONTERA DECLARADA, no duplicado.** `6.1` lo dice con todas las
> letras: *"dos doctrinas legitimas no son duplicado"*, y **una frontera se pierde
> por poda, no por fusion.** Las dos viven, con sus dos posiciones escritas y su
> arista. Si alguien propone fundirlas, mi voto es que no.

### 3.D. `criticar_trabajo_evitar_desanimo` contra `dar_opinion_critica_directa_desapasionada` (grafo, `zhuo_manager`)

Solape real en **no personalizar**, y con ejemplar casi calcado: Zhuo pone *"eres un
descuidado"* contra *"tu accion fue descuidada"*; Scott pone *"eres descuidado"*
contra *"has estado trabajando noches y fines de semana"*. **Es el mismo par de
frases en dos libros.** Y hay un segundo cruce: el sandwich, rechazado en el paso 10
de Zhuo y en el paso 4 de `equilibrar_elogio_critica_equipo`.

**Lo que queda fuera es procedimiento en los dos lados:** Zhuo compara **cinco
formulaciones** y da plantilla; Scott da articular el porque, devolver a la via,
averiguar antes, ser humilde, en persona e inmediatamente, elogiar en publico y
criticar en privado, y contar historias propias.

> **MI CLASE: CONTINUA, con un paso gemelo y una arista debida.** Y anoto lo que
> vigilaria: **si un dia alguien poda uno de los dos, se lleva por delante el
> ejemplar de la otra casa.**

### 3.E. `empezar_cultura_franqueza_radical`, contra sus propias tres partes

**Es el unico de los 17 que no doy por bueno de entrada, y es un candidato mio, no
un par.** Sus seis pasos son: cuenta con el nervio, explica la idea, pide que te
critiquen, empieza recibiendo, empieza por el elogio, entiende la frontera. **Los
pasos 3, 5 y 6 son los titulos de las tres secciones que vienen detras**, y esas
tres secciones ya son tres nodos de este mismo lote
(`pedir_critica_equipo_premiarla`, `elogiar_trabajo_especifico_contexto`,
`criticar_trabajo_evitar_desanimo`).

**La vara dice: NOMBRAR NO ES PROCEDIMENTAR** (`P.5.1`, congelada). Una segunda
linea solo cuenta como expansion si trae **procedimiento propio**, no solo el nombre
de otro.

> **MI CLASE: DISCUTIBLE, y me inclino por que SOBREVIVE, por poco.** Lo que trae
> propio es **el ORDEN y su razon**: *empieza recibiendo, no repartiendo*, que el
> libro argumenta y que no esta en ninguna de las tres partes. Un orden con su
> porque **si es procedimiento**. Pero es el candidato del lote con menos suelo
> propio, y **si alguien lo tumba citando `P.5.1`, no voy a poder decir que la cita
> este mal traida.**
>
> Su propio `resumen_teorico` dice que sus aristas van por **`D.29` con razon
> escrita y no por `D.37`**, porque el texto **no dice cuantas piezas son**. **Lo
> comprobe en la fuente y es exacto:** `cap_05.md` L215 enumera sin contar. **La
> doctrina esta bien aplicada, y esa parte no la discuto.**

---

## 4. LA DEUDA DE ARISTAS QUE ESTE LOTE VA A TENER QUE PAGAR AL INSERTAR

Cero aristas es correcto hoy (seccion 1.4). **Estas son las que mi lectura dice que
la insercion va a deber**, y las dejo escritas ahora para poder comprobarlas
despues:

| madre | hijo | por que |
|---|---|---|
| `empezar_cultura_franqueza_radical` | `pedir_critica_equipo_premiarla` | `D.29`, cabeza a parte, con razon escrita |
| `empezar_cultura_franqueza_radical` | `elogiar_trabajo_especifico_contexto` | `D.29` |
| `empezar_cultura_franqueza_radical` | `criticar_trabajo_evitar_desanimo` | `D.29` |
| `decidir_momento_despedir_persona` | `despedir_persona_franqueza_radical` | secuencia: decidir y despues hacer, dos rotulos distintos del libro |
| `cambiar_potencial_trayectoria_crecimiento` | `retirar_etiquetas_permanentes_equipo` | el marco y el uso del marco en el tiempo |
| `revisar_cinco_causas_mal_desempenio` | `decidir_momento_despedir_persona` | diagnosticar antes de decidir |

---

## 5. LO QUE EL CAPITULO TIENE Y NINGUN CANDIDATO SE LLEVO

**Esto es lo que una apertura ciega puede aportar y un reporte no: lo que falta.**
No lo afirmo de memoria, **lo busque sobre la poblacion entera** y publico la salida:

    poblacion buscada: 391
      [resultados esperados fijados por el empleado / medibles] -> 2  GRAFO:definir_resultados_tarjeta_puntuacion, BANDEJA:metas_vs_proposito
      [intangibles / trabajo en equipo como parte de la evaluacion] -> 1  BANDEJA:crecimiento_ingresos_verdes
      [los cuatro usos del marco (contratar, despedir, empujar, espejo)] -> 0
      [definicion de crecimiento empinado / gradual] -> 3  BANDEJA:cambiar_potencial..., retar_superestrellas..., retirar_etiquetas...
      [no poner a un empinado en un puesto gradual] -> 1  BANDEJA:reconocer_recompensar_gente_estable

**LA SECCION `GROWTH MANAGEMENT` DE `cap_06` (L69-L83) NO PRODUJO NINGUN
CANDIDATO**, y dentro de ella hay dos piezas que leo como procedimiento y que **no
estan en ninguno de los 391**:

1. **`cap_06.md` L77, los cuatro usos del marco**: *"figure out whom to hire, whom to
   fire, ... and when a person's poor performance might just be the boss's (your)
   fault"*, mas empujar a todo el equipo hacia el desempenio excelente. **Cero
   apariciones en la poblacion.**
2. **`cap_06.md` L83, como se evalua el desempenio pasado**: resultados **mas**
   intangibles como el trabajo en equipo; *"the expected results ... are ideally set
   by the employee; they should be as objective and as measurable as possible"*; y
   los intangibles, imposibles de medir pero no dificiles de describir, con sus
   expectativas igual de claras. **Es un procedimiento con su entregable, y no
   esta.** Los dos aciertos del barrido son de otro libro (una tarjeta de puntuacion
   de contratacion) y de un nodo de ingresos verdes: **ruido, no cobertura.**

Menor, y lo digo con menos conviccion: **`cap_05.md` L179-187 (*The false apology*)**
tiene una leccion procedimentable (*mejor callar que moverse en la direccion
equivocada del eje; mejor aun subir por el eje de cuidar y entender al otro antes de
responder*) que tampoco veo recogida. **Los cuatro cuadrantes de `cap_05` L59-L212
en bloque no dieron candidato propio**, y eso lo leo como decision razonable
(*"una advertencia es linea"*), **salvo por ese parrafo.**

---

## 6. DOS COSAS QUE MI INSTRUMENTO CONTRADICE, Y UNA ES MIA

**`D.38.3` no me deja resolver una discrepancia copiando: me obliga a declararla.**

### 6.1. Contra una cifra de MI PROPIA SEDE, `docs/loop/ORDEN_DE_LOTES.md` L20

    $ wc -w fuentes/scott_radical_candor/*.md | tail -1
     108587 total

    $ wc -w fuentes/scott_radical_candor/cap_0[4-9].md fuentes/scott_radical_candor/cap_1[01].md | tail -1
     81732 total

**`ORDEN_DE_LOTES.md` L20 dice `108.161` palabras del libro y `81.508` de los ocho
capitulos numerados. Mi `wc -w` de hoy dice `108.587` y `81.732`.** Diferencia de
**426** y de **224**.

> **ESTO ES UNA CIFRA EN UNA SEDE DURADERA (`docs/`), Y LA SEDE ES MIA.** `5.2`
> dice que una cifra falsa ahi es **CIFRA PUBLICADA**, y `D.38.2` dice que una cifra
> propia falsa acumula en **mi** racha, no en la del extractor. **No me absuelvo y
> tampoco me condeno a ciegas:** la fila no dice con que instrumento se midio el
> `108.161`, y **esa ausencia es exactamente el defecto que `D.38.3` persigue**. Si
> se midio con otro contador, la discrepancia es de metodo; si se conto a ojo, es
> caida mia. **Lo declaro aqui, sellado, y lo resuelvo en mi turno normal
> midiendolo con instrumento y corrigiendo la fila por correccion declarada sin
> borrar el texto viejo.** El numero de ficheros de la fila si lo confirmo:
> `ls fuentes/scott_radical_candor/ | wc -l` da **15**.

### 6.2. Contra dos cifras del cuerpo del commit `da62e73`

| lo que dice el commit | lo que dice mi `wc -w` | diferencia |
|---|---|---|
| `cap_07` tiene **13.678** palabras | **13706** | 28 |
| la vuelta mino **20.343** palabras | **20406** (8786 + 11620) | 63 |

**El asunto y el cuerpo de un commit no son sede de cifra** (5.6), asi que esto no
acumula. **Si esas mismas cifras estan en `REPORTE.md`, ahi si hay sede**, y habra
que decidir si es una diferencia de contador o una cifra mal puesta. **Lo dejo
medido ahora para que la comparacion no dependa de la memoria de nadie.**

---

## 7. EL VOLUMEN DE LA VUELTA, MEDIDO Y SIN ADJUDICAR

**El lote 4 corre a CUATRO capitulos por vuelta** (`ORDEN_DE_LOTES.md` L88 y L104,
decision del fundador del 11 sep 2026). **Esta vuelta cerro DOS**, `cap_05` y
`cap_06`.

    $ wc -w fuentes/scott_radical_candor/cap_05.md fuentes/scott_radical_candor/cap_06.md
      8786   11620   ->  20406 palabras minadas

    $ wc -w fuentes/scott_radical_candor/cap_07.md
     13706

**No adjudico esto aqui**, porque adjudicar el volumen exige la fila de pasos
inventados por capitulo y esa la firmo en el acta, no en la apertura. **Lo dejo
medido:** la vuelta entrego **la mitad de los capitulos del escalon vigente**, y el
capitulo que no abrio es **el mayor de los cuatro que le tocaban**. Si la razon es
buena se vera en el reporte; **lo que no puede pasar es que nadie lo haya medido**,
y ya esta medido.

**Y digo lo que NO he hecho: no he leido ni una linea de `cap_07`, `cap_08` ni
ninguno posterior**, y no hago ninguna afirmacion sobre su contenido. Lo unico que
he corrido sobre ellos es `wc -w`.

---

## 8. RESUMEN DE MI LECTURA CIEGA, EN UNA PAGINA

| | |
|---|---|
| capitulos leidos enteros | **2**, las **670** lineas (`wc -l`) |
| candidatos de la vuelta clasificados | **17**, uno a uno, con sus pasos abiertos |
| candidatos viejos de la bandeja leidos ademas | **8** |
| pasos leidos contra su parrafo | **185** (contador de pasos, seccion 1.3) |
| pasos que leo como **PUENTE** en el texto final | **0 de 185** |
| candidatos que leo como **PROCEDIMIENTO** | **16 de 17** |
| candidatos que leo como **DISCUTIBLE** | **1**, `empezar_cultura_franqueza_radical` (3.E) |
| pares que yo marcaria discutibles | **5** (3.A a 3.E) |
| de esos, **FRONTERA DECLARADA** y no duplicado | **1**, `revisar_cinco_causas` contra `diagnosticar_falta_motivacion_habilidad` |
| gemelos que pediria fusionar | **NINGUNO** |
| aristas debidas al insertar, anotadas | **6** (seccion 4) |
| piezas del capitulo sin candidato, buscadas sobre los 391 | **2 seguras** (`cap_06` L77 y L83) y **1 dudosa** (`cap_05` L179-187) |
| discrepancias de cifra declaradas | **3**: una **en mi propia sede** (6.1) y dos en cuerpo de commit (6.2), mas la del `L147`/`L149` (2.C) |
| barrido `D.38.4` de tres seniales | **2 de 17 completos**, publicados enteros, con el coste de los otros 15 medido (1.5); el del extractor tampoco completo, y su testigo esta en **cero bytes** |
| de esos 2, los que levantan vecino | **1**; el otro, `acompaniar_mejores_equipo_socio`, da **cero vecinos** teniendo un par de lectura en el grafo |
| barrido `D.38.4` por `familia_id` sobre los **391** | **COMPLETO**, salida integra en 1.6 |

**LO QUE MAS DEFENDERE CUANDO LEA EL REPORTE:** que los 185 pasos son transcripcion
del libro, que `revisar_cinco_causas` cuenta cinco porque el libro cuenta cinco, y
que **`acompaniar_mejores_equipo_socio` y `repartir_tiempo_atencion_mejores_equipo`
son un par de lectura que ninguna senial levanta** (3.B).

**LO QUE MAS DISPUESTO ESTOY A PERDER:** `empezar_cultura_franqueza_radical` (3.E).

**LO QUE TRAIGO CONTRA MI MISMO:** la cifra de palabras de `ORDEN_DE_LOTES.md` L20
(6.1), y el haberme contaminado por el `git log` (seccion 0).

---

*Escrito antes de abrir `docs/loop/REPORTE.md`. No commiteo: el arnes sella este
fichero. No lo toco despues del sello.*
