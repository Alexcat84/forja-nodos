# APERTURA CIEGA DE LA VUELTA 39, lote 4 (`scott_radical_candor`), `cap_13`

*Fase ciega del auditor de la `ACTA 38`. `docs/loop/REPORTE.md`, `loop.log`,
`ultimo_extractor.json` y `ultimo_auditor.json` no estan en el arbol y no los he
recuperado. Modo austero (`D.47`): cifra con instrumento, sin parrafo de acompaniamiento.*

---

## 0. LA DECLARACION QUE EL ARNES PIDE, Y VA LA PRIMERA

    ACTA ANTERIOR LEIDA: 017d96c016a2300875cee5129d038d9f4417603b
    HEREDADO 1: NO APLICA A ESTA FASE, porque esta apertura no sube ninguna pregunta a la cola

    $ python forja.py tablero | grep 'COLA DE DOCTRINA'
      COLA DE DOCTRINA (D.53): 10 pregunta(s), 0 bloquea(n)

    $ python -c "import json; d=json.load(open('config/frentes.json',encoding='utf-8')); print(len(d['cola_de_doctrina']['preguntas']))"
      10

    $ python -c "... for p in preguntas: print('n=%s medida_en=%s' % (p['n'], p['medida_en']))"
      n=9   medida_en=ACTA 37 seccion 8
      n=10  medida_en=ACTA 37 seccion 9

**EL MOTIVO, ESCRITO Y NO INSINUADO.** El heredado dice: *toda pregunta que yo diga en un
acta que SUBE a la cola de doctrina la escribo en `config/frentes.json` en la misma tanda, y
pego la salida de `python forja.py tablero | grep 'COLA DE DOCTRINA'` con la cuenta nueva al
lado.* **Esta apertura no sube ninguna pregunta a la cola**, y el acta donde la obligacion
muerde todavia no esta escrita. **Declarar `CUMPLIDO` aqui seria afirmar el cumplimiento de
un acta que no existe**, que es exactamente la especie `CIFRA PUBLICADA PROPIA` de `5.5`.

**SIGUE VIVO PARA LA `ACTA 38`, Y LO DIGO AQUI PARA QUE SE ME PUEDA COBRAR:** lo que esta
apertura deja anotado en su seccion `8` son **leads, no preguntas subidas**. Si alguno sube
en el acta, sube a `config/frentes.json` **en la misma tanda** y con esta misma salida al lado.

**Y LA SALIDA PEGADA PRUEBA ALGO MAS QUE EL MOTIVO, que es para lo que `D.40` la manda
correr: la promesa de la tanda ANTERIOR si se puede comprobar hoy, y se sostiene.** La
`ACTA 37` dijo que subia dos preguntas, la `9` y la `10`. **Estan las dos en la sede, con su
`medida_en` apuntando a su propia acta**, que son las dos ultimas lineas de arriba. **La
cuenta de la cola es `10` por las dos medidas: la del tablero y la de su propio fichero.**

---

## 1. LO QUE NO ES CIEGO EN ESTA APERTURA, Y LO DECLARO YO ANTES DE PUBLICAR NADA

**`D.38.3` manda separar la medida de la conclusion. Esto es anterior: es declarar por donde
entro luz en una fase que se llama ciega.**

| que vi | como | que contamina |
|---|---|---|
| **los asuntos de los commits de la vuelta 39** | corri `git log --oneline -3` al abrir, antes de leer nada | **el asunto del extractor trae SUS CIFRAS DE CIERRE** (`324` nodos, `506` veredictos, `134` aristas, cola en `0`, `0` de `56` en su tramo). **Mi coincidencia con ellas vale menos por eso, y donde coincida lo digo con esta linea delante** |
| **la clase de los `20` veredictos** | los liste con su columna `veredicto` antes de adjudicar | el manual `1.2` manda imprimir los pasos, adjudicar, **y solo despues destapar la razon**. **La razon NO la destape antes; la etiqueta si.** Donde yo coincida, la coincidencia esta anclada; **donde discrepe, la discrepancia es fuerte** |

**NO ES UNA CONFESION DE ADORNO.** Mi racha propia vive de cifras de esta fase, y la unica
manera de que un lector siguiente pese mis coincidencias es sabiendo que las mire con la
etiqueta puesta. **Lo que NO esta anclado es lo que sigue: los `56` pasos contra el libro, el
barrido de vecinos, y la cola de aristas, que los corri contra la fuente y contra el arbol.**

---

## 2. LOS INSTRUMENTOS, CORRIDOS EN ESTA FASE, CON SU SALIDA

    $ python forja.py gate
      GATE VERDE.
        nodos verificados: 324

    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl
          324 dataset/nodos.jsonl
          506 bitacora/VEREDICTOS.jsonl

    $ python forja.py resolutor
      nodos vivos: 324
      nodos deprecados (archivo): 0
      alias registrados: 0

    $ python forja.py rancios | grep -c "RANCIO"
      51
    $ python forja.py rancios | grep -c "2026-09-18"
      4

    $ ls cuarentena/scott_radical_candor/*.json | wc -l
      21
    $ ls cuarentena/_insertados/scott_radical_candor/ | wc -l
      121

**LECTURA (`D.38.3`, la frase es del instrumento y la conclusion va aparte):** el gate, el
barrido de guiones y el resolutor salen en verde sobre `324` nodos, y `dataset/nodos.jsonl`
tiene las mismas `324` lineas que el gate verifica. **De los `51` veredictos `RANCIO` del
bloque de vigencia, `4` llevan la fecha de hoy**, que es `D.15` cola de trabajo y no gate en
rojo, y el propio instrumento lo dice en su ultima linea.

**Y LA BANDEJA, DESGLOSADA POR CAPITULO CON SU INSTRUMENTO:**

    $ (primera aparicion de cap_NN en cada fichero de la bandeja, contada por capitulo)
      cap_13   6
      cap_14  15
      TOTAL   21

### 2.1. **LA SUITE DE ACEPTACION SALE EN ROJO EN MI FASE, Y LA CAUSA ES MI PROPIA FASE**

    $ python tests/test_aceptacion.py
      total: 294 pruebas, 3 fallos, 1 errores

    ERROR: test_el_reporte_vivo_pasa_su_propia_guarda
      FileNotFoundError: ...\docs\loop\REPORTE.md
    FAIL: test_la_linea_serial_del_repo_tiene_su_registro_escrito
      AssertionError: docs/loop/CREDITO_serial.jsonl sin tandas: la migracion de D.48 no esta en el arbol
    FAIL: test_caso_positivo_un_frente_recien_nacido_hereda_cero
    FAIL: test_el_aviso_nombra_la_linea_y_su_registro

**NO PUBLICO ESTE ROJO COMO ESTADO DE LA VUELTA 39, Y DIGO POR QUE CON EL CODIGO DELANTE.**
Las cuatro leen ficheros que el arnes retira para mi fase. El error lee `REPORTE.md`. Las
otras tres cuelgan de que `docs/loop/CREDITO_serial.jsonl` no este:

    $ grep -n "lineas_con_registro" src/herencia.py
      259:    if not credito.lineas_con_registro():
      260:        pass

**Sin registro de ninguna linea, `herencia.extraer` toma la rama `pass`**, y entonces una
linea inventada hereda los remedios de la serial en vez de cero, que es justo lo que esas dos
pruebas vigilan.

    $ python forja.py credito
      LINEA SIN REGISTRO: no hay ningun suceso escrito.

    $ git log --oneline -1 -- docs/loop/CREDITO_serial.jsonl
      a41fc11 ACTA 37: ...

**LA CONDICION DE CIERRE DE LA `TAREA 1.A` NO LA PUEDO VERIFICAR EN ESTA FASE, Y NO LA
FIRMO.** Queda medida en mi turno normal, con el arbol entero. **Lo que si dejo escrito es
que el rojo de hoy es reproducible desde la ausencia, y no desde el trabajo de la vuelta.**

### 2.2. **EL ARNES RETIRA CINCO FICHEROS, NO CUATRO, Y EL QUINTO ES UNO QUE `D.48` ME MANDA LEER**

    $ git status --short
      D docs/loop/APERTURA_CIEGA.md
      D docs/loop/CREDITO_serial.jsonl
      D docs/loop/REPORTE.md
      D docs/loop/loop.log
      D docs/loop/ultimo_auditor.json
      D docs/loop/ultimo_extractor.json

`D.34.2` retira **cuatro** y el prompt de esta fase nombra esos cuatro. `APERTURA_CIEGA.md`
es el fichero que yo escribo y su ausencia es correcta. **El que sobra es
`CREDITO_serial.jsonl`**, y `AUDITOR_FORJA.md` `5` escribe `python forja.py credito` como
*lo que tu linea trae al abrir*. **Hoy mi linea abre sin credito y el instrumento dice que no
hay ninguno, cuando `git` dice que lo hay desde la `ACTA 37`.** No lo recupero. **Lo declaro,
y es lead de mi turno normal, no cifra de nadie.**

---

## 3. LA POBLACION Y EL BARRIDO DE VECINOS (`D.38.4`, metodo vigente del 16 sep)

**LA POBLACION SE RECONSTRUYE INCREMENTAL, que es la que cada candidato tuvo delante**, y no
en una sola foto: el candidato `2` lo barrio el extractor contra un grafo que ya tenia dentro
al `1`. Se le entrega a la aduana la poblacion del **grafo** y **ella pone las bandejas**, que
es el metodo vigente desde la correccion del 16 sep a `D.38.4`.

    $ wc -l pob_p1.jsonl pob_p2.jsonl pob_p3.jsonl
          321 pob_p1.jsonl        (el grafo de hoy menos los tres de la vuelta)
          322 pob_p2.jsonl        (menos los candidatos 2 y 3)
          323 pob_p3.jsonl        (menos el candidato 3)

### 3.1. Las tres salidas, pegadas

    $ FORJA_DATASET=pob_p1.jsonl python forja.py informe pedir_critica_primero_crear_seguridad_psicologica.json
      poblacion del barrido       : 345   (321 del grafo mas 24 que esperan en bandejas)
      vecinos levantados en total : 1
      [BLOQUEARIA] pedir_critica_primero_crear_seguridad_psicologica
          vecino integrar_peticion_critica_rutina_existente  [levantada por: paso_contra_nodo]
            similitud_texto 0.215 | familia_id 0.100 | paso_contra_nodo 0.733
            paso 17 del candidato contra paso 6 de integrar_peticion_critica_rutina_existente

    $ FORJA_DATASET=pob_p2.jsonl python forja.py informe elegir_pregunta_recurrente_pedir_critica.json
      poblacion del barrido       : 346   (322 del grafo mas 24 que esperan en bandejas)
      ENTRARIAN sin leer nada          : 1
      BLOQUEARIAN esperando veredicto  : 0
      [ENTRARIA] elegir_pregunta_recurrente_pedir_critica

    $ FORJA_DATASET=pob_p3.jsonl python forja.py informe resolver_dudas_frecuentes_pedir_critica.json
      poblacion del barrido       : 347   (323 del grafo mas 24 que esperan en bandejas)
      vecinos levantados en total : 2
      [BLOQUEARIA] resolver_dudas_frecuentes_pedir_critica
          vecino despedir_persona_franqueza_radical  [levantada por: paso_contra_nodo]
            similitud_texto 0.173 | familia_id 0.000 | paso_contra_nodo 0.621
          vecino resolver_dudas_frecuentes_reuniones_salto_nivel  [levantada por: familia_id]
            similitud_texto 0.238 | familia_id 0.375 | paso_contra_nodo 0.467

**LA POBLACION SALE `345`, `346` Y `347`, y son `24` de bandeja en las tres.** Los `24` los
cuadro yo con su instrumento, y cuadran:

    $ for d in cuarentena/*/; do echo "$d $(ls $d | wc -l)"; done
      cuarentena/scott_radical_candor/     21
      cuarentena/marquet_turn_the_ship/     3
      cuarentena/onu_consumidor/            0
      cuarentena/smart_who/                 0
      cuarentena/zhuo_manager/              0
      (ensayo_referencia_163 con 164 queda fuera: son el catalogo ajeno de calibracion,
       y D.38.5 lo descarta por no tener sus fuentes en la tabla canonica)

`21` mas `3` son `24`. **`D.38.5` esta cumplida por la maquina: la aduana ya pone las bandejas ella sola**, y
mi barrido y el suyo miden la misma poblacion. **Lo cruzo y no hay discrepancia de metodo.**

### 3.2. **LA CIFRA QUE ESTE BARRIDO PUBLICA, Y ES LA MAS DURA DE LA VUELTA**

| | |
|---|---:|
| **vecinos que la senial levanta en los tres candidatos** | **`3`** |
| **pares con veredicto escrito en la vuelta** | **`19`** |
| **pares que existen SOLO porque alguien leyo** | **`16`** |

**LECTURA (`D.38.3`, conclusion aparte y marcada):** `16` de los `19` pares de esta vuelta
**no los levanta ninguna senial**, y los `16` los adjudico yo tambien por lectura en `5`.
**Esto no es una caida de nadie: es `D.19` medida otra vez** (*ninguna senial separa jerarquia
de ruido*), y es el argumento que sostiene por que `5.1` de esta apertura es la seccion mas
larga.

### 3.3. **EL CANDIDATO `2` NO LEVANTA NI UN VECINO, Y ES EL PRIMERO DE LOS CUATRO ELEMENTOS**

    ENTRARIAN sin leer nada          : 1
    BLOQUEARIAN esperando veredicto  : 0

`elegir_pregunta_recurrente_pedir_critica` **es el elemento `1` de `L237` y la aduana lo dejaria
entrar sin leer nada.** Sus `5` veredictos son los `5` declarados por lectura, y su arista a la
cabeza tambien. **LECTURA: si esta casa esperase a que una senial levantara a la primera de las
cuatro partes de una serie `D.37`, la primera parte entraria huerfana.** Lo reproduzco con mi
propia corrida y lo firmo.

**Y HAY UN SEGUNDO EJEMPLAR EN LA MISMA VUELTA, que es de donde sale mi `DISCUTIBLE 1`:**
el candidato `3` se barrio contra una poblacion que **ya tenia dentro al candidato `2`**
(`323` del grafo), y **la senial no levanto el par `resolver_dudas` contra `elegir_pregunta`**,
que es el par de dos nodos que salen **de la misma seccion del libro**, `L167` a `L185` dentro
de `L115` a `L186`. **Lo levanto yo leyendo, y solo leyendo.**

---

## 4. MI RELECTURA DE FIDELIDAD `D.30`, PASO A PASO CONTRA SU LINEA

**LA CORRI ENTERA Y SOBRE LOS TRES, no sobre una muestra.** El denominador va dicho: son los
**tres candidatos de la vuelta**, que son **media parte de `cap_13`** y no el capitulo.

    $ python -c "... len(d['pasos_accionables']) ..."
      pedir_critica_primero_crear_seguridad_psicologica   17
      elegir_pregunta_recurrente_pedir_critica            24
      resolver_dudas_frecuentes_pedir_critica             15
      TOTAL                                               56

| candidato | pasos | mi `TRANSCRIPCION` | mi `PUENTE` | de que lineas |
|---|---:|---:|---:|---|
| `pedir_critica_primero_crear_seguridad_psicologica` | `17` | `17` | `0` | `L075` a `L089`, `L105`, `L107`, `L109`, `L113` y `L237` |
| `elegir_pregunta_recurrente_pedir_critica` | `24` | `24` | `0` | `L119` a `L165` |
| `resolver_dudas_frecuentes_pedir_critica` | `15` | `15` | `0` | `L171` a `L185` |
| **TOTAL DE MI TRAMO** | **`56`** | **`56`** | **`0`** | |

**`PASOS INVENTADOS` DE MI LECTURA: `0` de `56`, `0,00` por ciento, sobre los tres candidatos
de la vuelta 39 y NO sobre `cap_13` entero.** El capitulo tiene hoy `12` piezas conocidas
(`6` en el grafo y `6` en bandeja) y **yo no he releido las otras nueve**, asi que **la fila
del capitulo no la firmo.**

### 4.1. La clase que el encargo manda releer entera, y que salio de ella

**Persona, cuenta, escalon o adjetivo de sentimiento.** Los relei **contra su linea completa**,
y son estos, uno a uno:

| paso | lo que nombra | su linea | veredicto mio |
|---|---|---|---|
| `P08` cand. `1` | **Amy Edmondson**, Harvard Business School | `L105` | `TRANSCRIPCION`, la definicion es literal |
| `P11` cand. `1` | **dos anios**, **200** entrevistas, **250** atributos, **180** equipos | `L107` | `TRANSCRIPCION`, los cuatro numeros estan en la linea |
| `P13` cand. `1` | **cinco** dinamicas, cimiento de **las otras cuatro** | `L107` | `TRANSCRIPCION` |
| `P15` cand. `1` | **consejero delegado** (`CEO`), jefes intermedios | `L109` | `TRANSCRIPCION`, y el escalon se conserva |
| `P12` cand. `2` | **seis meses**, **una semana**, **tres meses** | `L137` | `TRANSCRIPCION` |
| `P14` cand. `3` | **Carol Dweck**, un instituto de **Chicago**, la nota *todavia no* | `L183` | `TRANSCRIPCION` |

**Y UNO QUE ESTUVO A PUNTO DE SALIRME `PUENTE` Y NO LO ES, porque lei la linea entera.**
El `P06` del candidato `1` abre con un imperativo (*empieza por el primero y no por otro*)
que `L087` y `L089`, que son las lineas que cita, **no escriben**. **Pero `L105` escribe
`why soliciting feedback is FIRST in the order of operations` y `L113` escribe `prove you can
take it BEFORE you dish out`.** El imperativo lo sostiene el propio capitulo, dos parrafos mas
abajo de donde el paso cita. **`TRANSCRIPCION`.**

### 4.2. **UNA CITA QUE FUI A CAZAR Y QUE YA ESTABA CAZADA**

El `P17` del candidato `1` **nombra los cuatro elementos uno a uno**. `L113` dice **cuantos**
(*each of the four tips*) **y no los nombra**. Los nombres estan en `L237`:

    $ sed -n '237p' fuentes/scott_radical_candor/cap_13.md
      Now that you've practiced the four elements of soliciting criticism [...] coming up with
      a go-to question, embracing the discomfort, listening with the intent to understand, and
      making listening tangible by rewarding the candor [...]

**Abri el `resumen_teorico` esperando encontrar `L113` sola, y encontre la correccion ya
escrita**, fechada el 18 sep en la vuelta 39, diciendo literalmente *el paso 17 sale de la
linea 113 Y de la 237*. **Lo digo porque el hallazgo es suyo y no mio**, y porque un auditor
que se calla las que ya estaban cerradas publica una tasa de aciertos que no es la real.

---

## 5. MIS CLASES, ANTES DE DESTAPAR NINGUNA RAZON

**Los `20` veredictos de la vuelta son las lineas `487` a `506`.** La `487` es la correccion
declarada de la `TAREA 1.B` sobre `practicar_triangulo_critica_tres_papeles` y no es un par.

### 5.1. **LA SERIE `D.37` DE LOS CUATRO ELEMENTOS: LA LEI YO EN EL LIBRO Y SALE ENTERA**

`L237` nombra los cuatro. **Fui a ver que nodo es cada uno por las lineas de su
`resumen_teorico`, y no por su nombre:**

| elemento de `L237` | nodo | sus lineas |
|---|---|---|
| *coming up with a go-to question* | `elegir_pregunta_recurrente_pedir_critica` | `L115` a `L165` |
| *embracing the discomfort* | `abrazar_incomodidad_silencio_contar_seis` | `L187` a `L198` |
| *listening with the intent to understand* | `escuchar_entender_critica_dominar_defensa` | `L199` a `L214` |
| *making listening tangible by rewarding the candor* | `premiar_franqueza_hacer_escucha_tangible` | `L215` a `L234` |

**LOS CUATRO EXISTEN Y LOS CUATRO TIENEN SU VEREDICTO DESDE LA CABEZA.** La serie no se rompe.

### 5.2. **EL `SANO` QUE MI PROPIO ENCARGO PRE ADJUDICO: SE SOSTIENE, PERO POR OTRA LINEA**

Mi `TAREA 3.B` dijo `SANO` para `pedir_critica_primero` contra
`integrar_peticion_critica_rutina_existente` **citando `L113`**, y `L113` **no nombra a
ninguno de los cuatro**. Mi cita estaba corta, igual que la del extractor.

**LO QUE LO SOSTIENE ES `L237`, Y LO SOSTIENE MEJOR:** `L237` nombra los cuatro e
`integrar_peticion` **no es ninguno**. Su `resumen_teorico` dice que sale de `L111` a `L112`
y de `L235` a `L246`, o sea del rotulo `BUILD IT INTO YOUR EXISTING SCHEDULE`, **que en el
libro va DESPUES de los cuatro y es la frase que los cierra**. `D.37`, *Lo que NO autoriza*:
un nodo del mismo dominio que no es ninguna de las partes **es hermano, y su veredicto es
`SANO`**. **Mi adjudicacion: `SANO`, con la cita corregida de `L113` a `L237`.**

### 5.3. **LOS CINCO PASOS DEL ORDEN DE OPERACIONES: LOS CINCO TIENEN DESTINO**

| paso del libro | linea | nodo que lo recoge | como esta hoy |
|---|---|---|---|
| `1` *solicit criticism* | `L077` | el propio `pedir_critica_primero` | es la cabeza |
| `2` *give praise* | `L079` | `dar_elogio_disciplina_igual_critica` | `CONTINUA`, en bandeja, a cola |
| `3` *give criticism* | `L081` | `criticar_trabajo_evitar_desanimo` | `CONTINUA`, en el grafo |
| `4` *gauge the criticism and adjust* | `L083` | `medir_critica_respuesta_oyente_brujula` | `CONTINUA`, en bandeja, a cola |
| `5` *encourage praise and criticism between others* | `L085` | `fomentar_guia_reciproca_companieros` | `CONTINUA`, en el grafo |

**MI CLASE PARA LOS CINCO: `CONTINUA` CON ARISTA, NINGUNO `REPITE`.** Son las cinco etapas de
un inventario que el propio texto numera, y cada una trae procedimiento propio.

**Y COINCIDO EN QUE ESTO ES `D.29` Y NO `D.37`:** `L075` a `L085` **numera** los cinco pero
**no escribe la palabra cinco**, y `D.37` pide que el texto diga **cuantas** partes hay.
`L113` si la dice para los cuatro elementos. **Las dos series salen del mismo nodo y caen de
lados distintos de la vara, y esa lectura la sostengo yo tambien.**

### 5.4. **`empezar_cultura_franqueza_radical`: EL PAR MAS CERCA DE UN `REPITE` DE TODO EL TRAMO**

Imprimi los pasos de los dos antes de decidir.

| | `empezar_cultura_franqueza_radical` (`cap_05`) | `pedir_critica_primero` (`cap_13`) |
|---|---|---|
| pasos | `6` | `17` |
| el orden | en prosa: pide antes de dar, elogia antes de criticar | **numerado**, `L077` a `L085` |
| los pasos `4` y `5` | **no los tiene** | los tiene |
| razon medida | **ninguna** | Edmondson `L105`, Google `L107`, circulo virtuoso `L109` |
| lo que tiene el viejo y el nuevo no | *explica la idea primero* (`P02`), *la frontera peligrosa con la agresion odiosa* (`P06`) | |

**MI VEREDICTO: `CONTINUA` CON ARISTA, NO `REPITE`.** La vara `6.1` dice que **no hay
bascula**: el tamanio del solape no decide, decide **si lo que queda fuera es procedimiento en
los dos lados**, y aqui lo es en los dos. **Coincido con el extractor, y coincido tambien en
que es el par donde mas cerca se esta de un `REPITE` en el capitulo.**

### 5.5. La tabla entera de mis clases

| lineas | par | mi clase |
|---|---|---|
| `488` | `pedir_critica_primero` contra `integrar_peticion_critica_rutina_existente` | **`SANO`** (`5.2`) |
| `489` `492` `495` | contra los tres elementos restantes de `L237` | **`CONTINUA`** (`5.1`) |
| `490` `493` `494` | contra `dar_elogio`, `fomentar_guia`, `medir_critica` | **`CONTINUA`** (`5.3`) |
| `491` | contra `empezar_cultura_franqueza_radical` | **`CONTINUA`** (`5.4`) |
| `496` | contra `desplegar_plan_orden_operaciones_franqueza_radical` | **`CONTINUA`**: el plan despliega el orden que este nodo escribe |
| `497` | `criticar_trabajo_evitar_desanimo` contra `pedir_critica_primero` | **`CONTINUA`**: es el paso `3` del orden |
| `498` a `501` | `elegir_pregunta` contra `abrazar_incomodidad_arrancar_critica_equipo`, `exigir_critica_jefe_reticente`, `integrar_peticion`, `pedir_critica_equipo_premiarla` | **`SANO` los cuatro**: ninguno es *la pregunta recurrente*, son hermanos del mismo dominio |
| `502` | `elegir_pregunta` contra `pedir_critica_primero` | **`CONTINUA`**: elemento `1` de `L237` |
| `503` `504` `506` | `resolver_dudas` contra `despedir_persona`, `resolver_dudas_reuniones_salto_nivel`, `pedir_critica_primero` | **`SANO` los tres** |
| `505` | `resolver_dudas` contra `elegir_pregunta` | **`SANO`, y va marcado DISCUTIBLE** (`7`) |

**`20` de `20` adjudicados. Cero `REPITE` y cero fusiones en mi lectura.**

---

## 6. LA COLA DE ARISTAS, RECONTADA ENTERA CON INSTRUMENTO MIO

El cierre de mi encargo pedia que esta cifra saliera `0`.

    $ python -c "... aristas del grafo, veredictos CONTINUA, y los que no tienen cable ..."
      aristas dirigidas en el grafo: 134
      veredictos CONTINUA: 154
      CONTINUA con LOS DOS EXTREMOS EN EL GRAFO y SIN CABLE: 0

**LECTURA:** la cifra que el encargo pedia en `0` sale `0` contra mi propio recuento, sobre
`154` veredictos `CONTINUA` y `134` aristas dirigidas. **Lo que queda esperando espera porque
su otro extremo sigue en bandeja, que es `D.29` funcionando y no una arista rota.**

---

## 7. MIS DISCUTIBLES, MARCADOS ANTES DE VER EL REPORTE

**`DISCUTIBLE 1`. `L505`, `resolver_dudas_frecuentes_pedir_critica` contra
`elegir_pregunta_recurrente_pedir_critica`: `SANO`, y creo que falta una arista.**
El nodo `FAQ` sale de `L167` a `L185`, **que esta DENTRO de la seccion `A GO-TO QUESTION`, que
va de `L115` a `L186`**. Su `Q1` (`L169`) es literalmente *do I have to use the same go-to
question each week*, y los pasos `P01` a `P03` del hijo la contestan. **Mi adjudicacion:
`SANO` se sostiene** (no hay `REPITE`: tres de las cuatro dudas no van de la pregunta
recurrente), **pero una arista declarada por lectura desde `elegir_pregunta` estaria bien
fundada por el `Q1`.** Propuesta, no caida.

**`DISCUTIBLE 2`. Los ordinales de los cuatro atributos del candidato `2`.**
`L129` escribe *here are some attributes of good go-to questions* y **no dice cuantos**. Los
pasos `P05`, `P06`, `P09` y `P12` los llaman *el primer atributo*, *el segundo*, *el tercero*
y *el cuarto*, y el titulo del nodo dice *los cuatro atributos que el texto da*. **El
contenido es del libro; la numeracion la pone la mano.** **Mi adjudicacion: no es `PUENTE` de
`D.30`**, porque `D.30` cuenta pasos que el libro no dice y estos los dice. **Lo marco porque
el mismo nodo cabeza distingue con todo cuidado `D.29` de `D.37` por exactamente esta
diferencia** (*el texto NUMERA pero NO escribe la palabra cinco*), **y aqui el texto ni numera
ni cuenta.**

**`DISCUTIBLE 3`. La celda `medida_en` de la pregunta `7` de la cola, ya reparada.**
La `TAREA 1.C` la dejo en `REPORTE.md AC.7 (vuelta 37)`. **`REPORTE.md` se reescribe cada
vuelta**, asi que la reparacion cambia una seccion que no existia por **una seccion de un
reporte que hoy ya no esta en ese fichero**. Lo mismo, y de antes, con las preguntas `2` y `4`,
que citan `APERTURA_CIEGA.md 9.2` y `APERTURA_CIEGA.md 5.4` **sin numero de vuelta**, y **esas
las escribi yo**. **NO LO ADJUDICO EN ESTA FASE y no cargo nada: `REPORTE.md` no esta en el
arbol, y verificarlo aqui seria afirmar una busqueda que no he corrido.** Queda medido en mi
turno normal.

**`DISCUTIBLE 4`. La frontera de `cap_13` no me cierra, y no es trabajo de esta vuelta.**
El libro esta `CERRADO EN EXTRACCION` en el tablero. `cap_13` tiene `12` piezas conocidas y
**el rotulo `DIVERSITY AND INCLUSION` de `L323` a `L332` no aparece en ninguna**. Lei la
seccion entera: es anecdota y anuncio de taller, y una lectura razonable la deja fuera por
`D.27`. **El unico grano procedimental es la cena de ensayo de `L329`**, y esa figura la
adjudicamos el extractor y yo por separado en la vuelta 37. **Lo dejo anotado como lead y no
como caida de nadie: la extraccion de `cap_13` no es la vuelta que audito.**

---

## 8. LO QUE ME DEJO ANOTADO A MI MISMO PARA EL TURNO NORMAL

1. **La `TAREA 1.A`**: correr la suite con el arbol entero y firmar su verde o su rojo (`2.1`).
2. **`CREDITO_serial.jsonl` fuera del arbol** en una fase donde `D.48` me manda leerlo (`2.2`).
3. **Las rutas de `config/frentes.json` que prometen prueba** (`DISCUTIBLE 3`), con
   `REPORTE.md` delante.
4. **La cifra `0` de `ceo` del `resumen_teorico` del candidato `1`.** Se midio sobre `321`
   nodos del arbol `e3950c6` y **lo dice con su hash**, que es lo que `D.38.3` pide. Hoy mide
   otra cosa, y la diferencia la pone el propio nodo al entrar:

        $ grep -o -iE "\bceo\b" dataset/nodos.jsonl | wc -l              4
        $ grep -o -i "consejero delegado" dataset/nodos.jsonl | wc -l   43

   **Los `4` de `ceo` viven los `4` dentro de `pedir_critica_primero_crear_seguridad_psicologica`**,
   que es el nodo que publica la cifra. **LECTURA: no lo llamo caida**, porque la medida va
   fechada y con su arbol delante; **lo llamo la figura de la pregunta `4` de la cola con un
   ejemplar nuevo**, y con ese ejemplar se puede por fin decidir.

---

**Escrito en la fase ciega, sin recuperar ninguno de los cuatro ficheros retirados, y sin
commitear: el sello lo pone el arnes.**
