# APERTURA CIEGA DE LA `ACTA 37`, sobre la VUELTA 38

`scott_radical_candor`, lote 4, **`cap_13`**. Escrita antes de ver
`docs/loop/REPORTE.md`, que no esta en el arbol.

---

## 0. LO QUE EL ARNES EXIGE QUE TRAIGA

    ACTA ANTERIOR LEIDA: 4acc6005ac6193741024ffc422d56f90a6c201c2
    HEREDADO 1: CUMPLIDO

**La huella la comprobe, no la copie:**

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    4acc6005ac6193741024ffc422d56f90a6c201c2

    $ python forja.py herencia
      acta anterior : ACTA 36. VUELTA 37, lote 4 (`scott_radical_candor`) ...
      su huella     : 4acc6005ac6193741024ffc422d56f90a6c201c2
      heredados     : 1

**`HEREDADO 1` es `CUMPLIDO` y no `NO APLICA`**, y se ve en la seccion 5: la casilla
`PUENTE` de este capitulo la escribo contra **lo que el extractor ESCRIBIO**, el
`grep -n PUENTE` va corrido sobre la ultima acta **y sobre esta pagina**, con las dos
salidas pegadas, y **la casilla no sale `0`.**

---

## 1. LA CABECERA, Y VA PRIMERO PORQUE AFECTA A TODA CIFRA DE ESTA PAGINA

> ### **EL ARBOL SE MOVIO DEBAJO DE MI FASE CIEGA, Y LO MIDO CON EL MISMO INSTRUMENTO DOS VECES**

El `gitStatus` que **el propio arnes** me entrego al abrir la conversacion no tenia
ninguna entrada de `cuarentena/`. La tiene ahora, y es una **renombrada ya puesta en
el indice**:

    $ git status --porcelain            (al abrir, entregado por el arnes)
     M dataset/nodos.jsonl
     M bitacora/VEREDICTOS.jsonl
     M censos/denominaciones.md
     ?? .v38/informes/i03_triangulo.txt
                                        (ninguna linea de cuarentena/)

    $ git status --porcelain            (corrido por mi, mas tarde, misma fase)
    R  cuarentena/scott_radical_candor/practicar_triangulo_critica_tres_papeles.json
    -> cuarentena/_insertados/scott_radical_candor/practicar_triangulo_critica_tres_papeles.json

**Y EL MISMO INSTRUMENTO DE LA CASA DA DOS CIFRAS DENTRO DE MI PROPIO TURNO:**

    $ python forja.py gate              (primera corrida, sin sello de hora)
    GATE VERDE.
      nodos verificados: 320

    $ python forja.py gate              (segunda corrida, 2026-09-18 02:41:02)
    GATE VERDE.
      nodos verificados: 321

**LA HORA LO CIERRA:**

    $ ls -la --time-style=+%F_%T dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl .git/index .v38/informes/
    2026-09-18_02:34:42  dataset/nodos.jsonl
    2026-09-18_02:34:42  bitacora/VEREDICTOS.jsonl
    2026-09-18_02:34:42  .git/index
    2026-09-18_02:10:17  .v38/informes/i01_mejorar_consciencia.txt
    2026-09-18_02:25:12  .v38/informes/i02_contar_cuatro.txt
    2026-09-18_02:34:42  .v38/informes/i03_triangulo.txt

    $ date
    Fri, Sep 18, 2026  2:40:11 AM

**LECTURA:** mi fase ciega arranco con `cuarentena/_insertados` sellado a las `02:25:12`
(la hora de `i02`), y **a las `02:34:42` entro al grafo un tercer nodo**,
`practicar_triangulo_critica_tres_papeles`, con su informe de aduana, su linea de
bitacora, sus censos y **la renombrada ya en el indice de git**. **Yo no corri
`forja.py insertar` ni una sola vez**: mis corridas son `gate`, `guiones`, `resolutor`,
`credito`, `herencia`, `tablero`, `informe` y lectores de solo lectura.

**POR QUE LO PONGO EL PRIMERO Y NO EN UN ANEXO:** `D.38.3` me obliga a pegar el
instrumento al lado de la cifra. **Si la poblacion cambia mientras el instrumento
corre, el instrumento pegado no basta: hace falta la hora.** Toda cifra de grafo de
esta pagina lleva de aqui en adelante **su sello de hora**, y la que no lo lleve no
vale. Es lo unico que me separa de publicar `320` y `321` en la misma pagina como si
fueran la misma medida.

**LO QUE NO DIGO:** no digo de quien es. Digo **que paso**, **cuando**, y **que yo no
fui**. La sede de esa adjudicacion es el acta, con el reporte delante.

---

## 2. LA POBLACION, MEDIDA

    == SELLO DE HORA: 2026-09-18 02:41:02 ==

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 321
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada,
               vuelta, cita_incompleta, deprecado_en_superficie, arista_rota,
               arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python forja.py resolutor
    nodos vivos: 321
    nodos deprecados (archivo): 0
    alias registrados: 0

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl
        321 dataset/nodos.jsonl
        486 bitacora/VEREDICTOS.jsonl

**CONTRA `git`, que es lo que dice cuanto puso ESTA vuelta:**

    $ git show HEAD:dataset/nodos.jsonl | wc -l          319
    $ git show HEAD:bitacora/VEREDICTOS.jsonl | wc -l    479

| medida | `HEAD` (`b9c2255`) | arbol, `02:41:02` | delta sin commitear |
|---|---|---|---|
| nodos | `319` | `321` | **`+2`** |
| lineas de bitacora | `479` | `486` | **`+7`** |

**LOS TRES NODOS QUE ESTA VUELTA PUSO EN EL GRAFO**, contados commit a commit con el
instrumento y no a ojo:

    $ (por cada commit de la vuelta, ids de dataset/nodos.jsonl contra el anterior)
    03e9ee8   nodos=318  (base, apertura de la vuelta 38)
    faddf01   nodos=318  nuevos=[]
    3f3a949   nodos=318  nuevos=[]
    442aa56   nodos=318  nuevos=[]
    b9c2255   nodos=319  nuevos=['mejorar_consciencia_propia_relacional_dos_practicas']
    worktree  nodos=321  nuevos=['contar_cuatro_historias_propias_ver_hueco_intencion',
                                 'practicar_triangulo_critica_tres_papeles']

**UNA COSA MAS QUE SALE DE AHI Y LA DIGO AUNQUE SEA MENOR:** en `b9c2255`,
`contar_cuatro_historias_propias_ver_hueco_intencion` **ya estaba archivado como
insertado** (`R100` a `_insertados/`) **y su nodo no estaba en el `dataset` de ese
commit**. La bandeja decia insertado y el catalogo decia que no. **Hoy cuadran**: el
nodo esta en el arbol. Lo dejo medido, no adjudicado.

---

## 3. EL TABLERO, QUE `D.49` MANDA LEER Y CITAR

    $ python -c "from src import tablero; print(len(tablero.cola_de_doctrina()))"
    cola_de_doctrina() = 8 entradas

| libro | estado | rama | bandeja | en grafo |
|---|---|---|---|---|
| `scott_radical_candor` | `CERRADO EN EXTRACCION` | serial | `27` en el dump, **`24` medido** | `115` en el dump |
| `grove_high_output` | `EN CURSO` | `extraccion-grove_high_output` | `23` | `0` |
| `gerber_emyth` | `PAUSADO` | `extraccion-gerber_emyth` | `10` | `0` |
| `marquet_turn_the_ship` | `PAUSADO` | `extraccion-marquet_turn_the_ship` | `9` | `0` |

    $ ls cuarentena/scott_radical_candor/*.json | wc -l              24
    $ ls cuarentena/_insertados/scott_radical_candor/*.json | wc -l  118

**EL LIBRO DE ESTA VUELTA ES `scott_radical_candor`**, y es el de mi linea.

**Y EL DUMP DEL TABLERO ESTA RANCIO, medido:**

    $ grep -c '"tipo": "doctrina"' docs/loop/TABLERO.jsonl
    6
    $ python -c "from src import tablero; print(len(tablero.cola_de_doctrina()))"
    8

**LECTURA:** `config/frentes.json` es la sede viva y trae `8`;
`docs/loop/TABLERO.jsonl`, que es el volcado por el que la casa lo lee, trae `6`. **La
vuelta subio la cola a `8` y no volvio a volcar el tablero.** `2` preguntas de doctrina
estan en la sede y **no estan en el fichero por el que se leen**.

---

## 4. LA GUARDA QUE ESTA EN ROJO, Y NO ES ARTEFACTO DE MI FASE

    $ python tests/test_aceptacion.py
      total: 294 pruebas, 4 fallos, 1 errores
    FAILED (failures=4, errors=1, skipped=1)

**LAS CINCO, SEPARADAS UNA A UNA. CUATRO SON ARTEFACTO DE MI PROPIA FASE Y UNA NO:**

| prueba | causa medida | artefacto mio? |
|---|---|---|
| `test_el_reporte_vivo_pasa_su_propia_guarda` | `FileNotFoundError: docs/loop/REPORTE.md` | **SI**, `D.34.2` lo retira |
| `test_la_linea_serial_del_repo_tiene_su_registro_escrito` | `CREDITO_serial.jsonl sin tandas` | **SI**, la fase ciega no lo ve |
| `test_caso_positivo_un_frente_recien_nacido_hereda_cero` | el mismo, via `src/herencia.py:259` | **SI** |
| `test_el_aviso_nombra_la_linea_y_su_registro` | el mismo, via `src/herencia.py:259` | **SI** |
| **`test_la_cola_del_repo_trae_las_seis_con_su_medida`** | **`AssertionError: 8 != 6`** | **NO** |

**LAS CUATRO MIAS TIENEN SU CAUSA LEIDA EN EL CODIGO, no supuesta**, y lo digo porque
declarar *es artefacto de mi fase* sin abrir nada es exactamente el `NO APLICA` sin
salida que `D.40` prohibe:

    $ grep -n "RECIEN NACIDA" -B4 src/herencia.py
    258-    linea = credito.linea_actual()
    259-    if not credito.lineas_con_registro():
    260-        pass
    261-    elif not credito.nacida(linea):
    264:                    "LINEA RECIEN NACIDA: '%s' no tiene ninguna tanda cerrada ..."

Con `CREDITO_serial.jsonl` fuera del arbol **ninguna linea tiene registro**, se entra
por el `pass` de la `260` y la deteccion de linea recien nacida no llega a correrse.

**EFECTO COLATERAL QUE DECLARO SOBRE MI MISMO:** en esta fase
`python forja.py herencia` me entrega los remedios **por esa rama de reserva**, no por
la normal. En mi caso entrego lo correcto, y lo se porque **lo que me entrego coincide
palabra por palabra con lo que el arnes escribio en mi prompt**, asi que pude cotejar
las dos copias. **Si no coincidieran, la fase ciega no tendria como saber cual vale.**

**LA QUINTA ES REAL Y TIENE FECHA:**

    $ git log --oneline -1 -- config/frentes.json
    b9c2255 V.38 TAREA 4: las dos preguntas suben a la cola de doctrina y la dejan en 8 ...
    $ git log --oneline -1 -- tests/test_aceptacion.py
    d2d71cd D.52, TODA TABLA DEL REPORTE DECLARA SU INSTRUMENTO ...   (vuelta anterior)

    $ sed -n '3821,3824p' tests/test_aceptacion.py
    def test_la_cola_del_repo_trae_las_seis_con_su_medida(self):
        cola = tablero.cola_de_doctrina()
        self.assertEqual(len(cola), 6)

**LECTURA:** la vuelta subio la cola de `6` a `8` en su TAREA 4 y **dejo clavada en
`6`** la prueba que la vigila. **La suite de aceptacion quedo en ROJO al cerrar la
vuelta.**

**Y EL MECANISMO POR EL QUE NO LO CAZO NADIE ESTA MEDIDO:**

    $ grep -n "test_aceptacion" .git/hooks/pre-commit
    (el hook NO corre tests/test_aceptacion.py)

El hook corre `gate`, `guiones` y `scripts/cerrar_reporte.py --hook`, **y los tres
estan verdes**. La suite de aceptacion **no esta en el hook**, asi que el commit paso.
**No encargo aqui ninguna maquinaria nueva** (`7.F` de la cosecha, la moratoria): lo
dejo medido.

---

## 5. `PASOS INVENTADOS POR CAPITULO`, QUE ES LA CASILLA DEL `HEREDADO 1`

### 5.1. La frontera de `cap_13`, cerrada por mi

    $ (por cada candidato de scott que cita cap_13.md en su resumen: su pieza y sus pasos)
    pieza  1  mejorar_consciencia_propia_relacional_dos_practicas   13  INSERTADO  L17-22, L35-40
    pieza  2  contar_cuatro_historias_propias_ver_hueco_intencion   17  INSERTADO  L41-58
    pieza  3  practicar_triangulo_critica_tres_papeles              15  INSERTADO  L59-72
    pieza  4  pedir_critica_primero_crear_seguridad_psicologica     17  bandeja    L73-86, L105-110, L113-114
    pieza  5  elegir_pregunta_recurrente_pedir_critica              24  bandeja    L115-120, L129-166
    pieza  6  resolver_dudas_frecuentes_pedir_critica               15  bandeja    L167-186
    pieza  7  abrazar_incomodidad_silencio_contar_seis              12  bandeja    L187-198
    pieza  8  escuchar_entender_critica_dominar_defensa             13  bandeja    L199-214
    pieza  9  premiar_franqueza_hacer_escucha_tangible              20  bandeja    L215-234
    pieza 10  integrar_peticion_critica_rutina_existente            13  bandeja    L111-112, L235-246
    pieza 11  dar_elogio_disciplina_igual_critica                   20  bandeja    L247-252, L267-288
    pieza 12  medir_critica_respuesta_oyente_brujula                33  bandeja    L289-322
    TOTAL cap_13 = 12 candidatos, 212 pasos escritos

    $ wc -l fuentes/scott_radical_candor/cap_13.md
    347 fuentes/scott_radical_candor/cap_13.md

    $ grep -n -E '^(YOU|SOLICIT|A GO-TO|EMBRACE|LISTEN|MAKE LISTENING|BUILD IT|PRAISE:|APPLY|GAUGE|DIVERSITY|WHAT|Practice|Praise Practice|FAQ|Improve|Kim|Jason|BONUS)' fuentes/scott_radical_candor/cap_13.md
     17:YOU                                     193:Practice: Count to six in your head
     19:Improve using role plays and storytell  199:LISTEN WITH THE INTENT TO UNDERSTAND
     41:Practice: What's your story?            207:Practice: Listening
     59:Practice: The Feedback Triangle         215:MAKE LISTENING TANGIBLE: REWARD THE CANDOR
     73:SOLICIT CRITICISM FIRST                 223:Practice: Make Listening Tangible
     91:Kim's Soliciting Feedback Story         231:Practice: Reward criticism you disagree with
    115:A GO-TO QUESTION YOU CAN ACTUALLY ASK   235:BUILD IT INTO YOUR EXISTING SCHEDULE
    121:Jason's Story                           243:Practice: add soliciting feedback to the 1:1
    159:Practice: Ask for a critique of your    247:PRAISE: FOCUS ON THE GOOD STUFF. REALLY.
    167:FAQ                                     255:Jason's Story
    187:EMBRACE THE DISCOMFORT                  275:APPLY THE SAME DISCIPLINE TO PRAISE
                                                281:Praise Practice
                                                289:GAUGE CRITICISM
                                                323:DIVERSITY AND INCLUSION
                                                333:WHAT'S NEXT?
                                                347:BONUS CHAPTER

**LECTURA, Y LA FIRMO:** cruce los `347` renglones contra las `12` piezas y **la
frontera cierra**. Lo que ninguna pieza toma es: `L1-16` (cabecera), `L23-34` (el caso
del inversor y su asociado), `L87-104` (la historia de Kim y su hija), `L121-128` y
`L253-266` (las dos historias de Jason), y `L323-346` (`DIVERSITY AND INCLUSION` y
`WHAT'S NEXT?`). **Los cinco primeros son manual `3.5`, el caso y no la casa.** El
ultimo lo adjudique **NO ES NODO** en mi apertura de la vuelta anterior y lo vuelvo a
adjudicar igual sin releer aquella: la cena de ensayo de `L325` es **lo que otra
persona cuenta que hace**, no una instruccion al lector, y el taller de `L329` es **un
producto de los autores**, no un procedimiento.

### 5.2. El tramo de ESTA vuelta son las piezas `1` a `6`, y suman `101` pasos

    13 + 17 + 15 + 17 + 24 + 15 = 101

**Es la baja de tramo que la `ACTA 36` encargo por `EXTRACTOR.md` 12.4, y cuadra al
digito con lo que la vuelta trabajo.**

### 5.3. LA RELECTURA `D.30` DE LOS `101`, PASO A PASO CONTRA SU LINEA

Lei los `101` pasos del tramo **contra `fuentes/scott_radical_candor/cap_13.md`
entero, que abri antes de abrir ningun candidato.**

| pieza | pasos | `PUENTE` que yo firmo | contra que linea |
|---|---|---|---|
| 1 `mejorar_consciencia` | `13` | `0` | `L19`, `L35`, `L37`, `L39` |
| 2 `contar_cuatro` | `17` | **`1`** (`P8`) | `L49`, *her boss's boss's boss* |
| 3 `practicar_triangulo` | `15` | `0` | `L63`, `L65`, `L67`, `L69`, `L71` |
| 4 `pedir_critica_primero` | `17` | **`2`** (`P6`, `P15`) | `L87`, `L89`, `L109` |
| 5 `elegir_pregunta` | `24` | `0` | `L117`, `L129` a `L145`, `L147` a `L163`, `L165` |
| 6 `resolver_dudas` | `15` | `0` | `L169` a `L185` |
| **TOTAL TRAMO** | **`101`** | **`3`** | **`2,97` por ciento** |

**LOS TRES, CON NOMBRE Y CON LA LINEA QUE LOS TUMBA:**

**`PUENTE 1`, pieza 2 `P8`.** Escribia *al jefe de su jefe* donde `L49` escribe
*her boss's boss's boss*, **tres escalones y no dos**. **NO ES UN HALLAZGO MIO DE
HOY**: lo adjudico mi propia `ACTA 36` `3.1`, y **por eso mismo cuenta aqui**, porque
el `HEREDADO 1` manda contar contra lo escrito y no contra lo que hoy vive en el
grafo. Lo entrego el `grep` que ese mismo heredado me obliga a correr:

    $ grep -n PUENTE docs/loop/ACTA_AUDITOR.md | sed -n 's/^30741://p'
    **LOS TRES `PUENTE`, CON NOMBRE:** `desplegar_plan_orden_operaciones_franqueza_radical`
    `P33` (superestrellas por rock stars, levantado por la ACTA 35 6); y los dos del
    `3.1`, `contar_cuatro_historias_propias_ver_hueco_intencion` `P8` y
    `dar_elogio_disciplina_igual_critica` `P13`.

**`PUENTE 2`, pieza 4 `P6`.** Lo que estaba escrito, sacado de `git` y no del arbol de
hoy:

    $ git show 3f3a949^:cuarentena/scott_radical_candor/pedir_critica_primero_crear_seguridad_psicologica.json
    "Empieza por el primero y no por otro ...: como las dos historias mas repetidas del
     libro eran las de una jefa dando critica, muchos lectores se quedaron con la
     impresion de que la franqueza radical va sobre todo de jefes criticando a empleados"

`L87` parte el contraste por la mitad: *One was about a boss giving feedback
successfully. The other was about what happens when a boss fails to give feedback.*
**La segunda es de una jefa que NO la da**, y el paso las hacia las dos de dar. Y `L89`
pone la causa al reves: la impresion de los lectores viene de que **al libro le
FALTABA** una historia de pedir (*the book didn't have a similarly memorable story
about a boss soliciting feedback ... As a result*), no de que sobraran las de dar.
**Una relacion de causa que el libro no escribe la escribio el extractor: `PUENTE`.**

**`PUENTE 3`, pieza 4 `P15`.** Escribia *cuando quien manda pide critica* donde `L109`
escribe *When the CEO solicits criticism*. **Es el mas discutible de los tres y lo
digo:** no inventa un objeto, ensancha el sujeto. **Lo cargo igual**, porque la frase
entera de `L109` es un descenso de escalones (del CEO a los jefes intermedios, y de
ahi a todos los niveles de la organizacion), **y *quien manda* borra el escalon de
arriba**, que es lo unico que la frase afirma. Enunciado asi, el paso afirma **de
cualquier jefe** lo que el libro afirma **del CEO**: es una proposicion que el libro no
hace.

### 5.4. LO QUE TENGO QUE DECLARAR SOBRE MI PROPIA CEGUERA EN DOS DE LOS TRES

**`PUENTE 2` y `PUENTE 3` NO LOS ENCONTRE A CIEGAS, Y SERIA FALSO DECIR QUE SI.** El
bloque `Recent commits` que **el arnes me pone en el prompt** trae el asunto de
`3f3a949` entero, y ese asunto **nombra los dos pasos y los llama `PUENTE`**. Lo lei
antes de abrir un solo candidato. **No lo pedi y no podia no verlo, pero eso no lo
hace ciego.**

**LO QUE SI ES CIEGO Y MIO, y es la mitad que vale:** los **`99` pasos restantes** del
tramo los lei uno a uno contra su linea **sin que nada me dijera donde mirar**, y dan
**`0` `PUENTE` mas**. Y el `PUENTE 1` **no estaba en ningun commit**: salio del `grep`
sobre mi propia acta que el `HEREDADO 1` me manda correr, que es justo para lo que
sirve.

**POR QUE LO ESCRIBO EN VEZ DE CALLARLO:** una apertura ciega que no declara por donde
se le colo la informacion **publica como coincidencia de dos lecturas algo que no eran
dos lecturas.** Y la `ACTA 36` gasto una caida mia justo por publicar un `0` sin haber
elegido bien la fuente antes de contarla. **Declarar la contaminacion cuesta menos que
fingir que no la hubo.**

### 5.5. LA FILA, Y LA CASILLA NO SALE `0`

| capitulo | pasos escritos | `TRANSCRIPCION` | `PUENTE` | **`PASOS INVENTADOS`** | contra el techo de `10` |
|---|---|---|---|---|---|
| **`cap_13`, tramo de la vuelta 38 (piezas `1` a `6`)** | **`101`** | `98` | **`3`** | **`2,97` por ciento** | **DEBAJO** |

**Y LA DEL CAPITULO ENTERO LA DECLARO PARCIAL, QUE ES LO QUE ES:**

| capitulo | pasos escritos | `PUENTE` adjudicados hasta hoy | leidos por mi en esta fase | **sin leer** |
|---|---|---|---|---|
| `cap_13` completo | `212` | **`4`** (los tres de arriba mas `dar_elogio` `P13`, `ACTA 36` `3.1`) | `101` | **`91`** |

**NO PUBLICO UN POR CIENTO DE CAPITULO ENTERO**, porque `91` de sus `212` pasos no los
ha leido nadie en esta fase, y una fraccion con el numerador a medias **no es una
medida, es una apuesta.** Lo que publico es el tramo, que lei entero.

**Y ESTO NO ES UN REPROCHE POR TENER LOS DEFECTOS** (`8.4`): los tres se cazaron y se
corrigieron **antes de insertar**, con su correccion declarada escrita y sin borrar el
texto viejo. **Lo que cambia es la fila.**

---

## 6. MIS CLASES, ADJUDICADAS ANTES DE DESTAPAR NADA

**No he abierto `bitacora/VEREDICTOS.jsonl` por el campo de clase ni por el de razon**
de ninguno de los tres nodos de esta vuelta. De ese fichero solo he contado lineas
(`486`). Lo que sigue sale de **los pasos y de `cap_13.md`**.

| # | pieza | mi clase | mi razon, en una linea |
|---|---|---|---|
| 1 | `mejorar_consciencia` (entro) | **SANO, cabeza de serie `D.37`**, con **`DISCUTIBLE 1` encima** | `L39` escribe *two practices* y **las nombra**: dice cuantas, que es la condicion literal de `D.37` |
| 2 | `contar_cuatro` (entro) | **SANO, parte de la serie** | `L41` a `L58` pone su propio inventario: cuatro historias nombradas una a una con su pregunta de arranque escrita |
| 3 | `practicar_triangulo` (entro a las `02:34:42`) | **SANO, parte de la serie** | `L63` escribe *Here's how it works*, y `L63`, `L65` y `L69` nombran los tres papeles uno a uno |
| 4 | `pedir_critica_primero` (bandeja) | **CONTINUA con arista**, madre `empezar_cultura_franqueza_radical`, hijo este | ver `6.2` |
| 5 | `elegir_pregunta` (bandeja) | **SANO** | `L131` a `L141` pone los cuatro atributos y `L147` a `L163` las nueve preguntas literales; nada de eso vive en el grafo |
| 6 | `resolver_dudas` (bandeja) | **SANO** | `L167` a `L186`, cuatro preguntas con su respuesta desplegada en pasos; la de Dweck (`L183`) no esta en ningun nodo |

### 6.1. La cuenta de la serie `D.37`, comprobada en el libro y no en el nodo

    $ sed -n '39p' fuentes/scott_radical_candor/cap_13.md
    You can improve both your self-awareness and your relational awareness. We have
    developed two practices, storytelling and role plays, that will help you improve both.

`D.37` pide que el texto diga **cuantas** partes tiene. `L39` dice `two` **y las
nombra**. Las dos existen como pieza (`2` y `3`) y **las dos entraron en esta vuelta**.
La serie esta completa: `1` cabeza, `2` partes, `0` huerfanas.

### 6.2. El par de la pieza `4`, leido con los dos lados delante

**LA MADRE, que lleva en el grafo desde `cap_05`:**

    $ (dataset/nodos.jsonl) empezar_cultura_franqueza_radical, 6 pasos
    P02 Empieza explicando la idea.
    P03 Y despues pide a tu gente que sea radicalmente franca contigo.
    P04 ... empieza recibiendo guia, no repartiendola.
    P05 Cuando empieces a darla, empieza por el elogio y no por la critica.
    P06 Cuando pases a la critica, asegurate de entender donde esta la frontera peligrosa
        entre la franqueza radical y la agresion odiosa.

**EL HIJO** trae la lista **numerada por el propio libro** en `L75` a `L83`, y sus
etapas `4` (*gauge the criticism and adjust*) y `5` (*encourage praise and criticism
between others*) **no estan en la madre ni en prosa ni en ningun sitio.**

**MI VEREDICTO: `CONTINUA` con arista, y la direccion es madre `empezar_cultura` a
hijo `pedir_critica_primero`.** La vara no tiene bascula: no decide el tamanio del
solape, decide **si lo que queda fuera es procedimiento en los dos lados**. Fuera del
solape, el hijo pone **dos etapas nuevas del plan**; la madre pone **la frontera
peligrosa**, que el hijo no toca. **Procedimiento en los dos lados: no es `REPITE`.**

**Y ME PONGO EL REPARO YO MISMO:** `10` de los `17` pasos del hijo (`P07` a `P16`) son
razon y medicion, no etapa. **No lo cargo**, porque *cuenta con* es la forma de toda la
casa y estrechar la vara por eso seria moverla, **y mover la vara es parada** (`6.3`).
Lo dejo escrito para que se vea que lo mire y por que no lo use.

---

## 7. LOS DOS DISCUTIBLES QUE LEVANTO YO, A CIEGAS

### 7.1. **DISCUTIBLE 1: la cabeza de la serie, `mejorar_consciencia`, solo NOMBRA a sus dos partes**

**Y PESA, porque este nodo ENTRO AL GRAFO en esta vuelta** (`b9c2255`).

De sus `13` pasos, **`9` son definicion** (`P01` a `P09`: distingue las dos
consciencias, cuenta con lo que no significa, usa esa consciencia para bien) y **los
tres unicos imperativos que dejan algo hecho son estos:**

    P10 ... usa para ello las DOS practicas que el texto dice haber desarrollado:
        contar historias y los juegos de papeles.
    P11 Haz la primera, contar historias, que el texto despliega bajo el rotulo
        cual es tu historia.
    P12 Haz la segunda, el juego de papeles, que el texto despliega bajo el rotulo
        el triangulo de la critica.

**`P11` y `P12` son, palabra por palabra, los rotulos de las piezas `2` y `3`.**

La vara de `6.1` de mi protocolo tiene una fila escrita para esta figura: **`NOMBRAR NO
ES PROCEDIMENTAR`**, *una segunda linea solo cuenta como expansion si trae
procedimiento propio, no solo el nombre de otro* (`P.5.1`, congelada el 3 sep 2026).
Quitale a este nodo `P11` y `P12` y **lo que queda no deja fichero**: queda la
distincion entre las dos consciencias, que es una definicion.

**NO LO ADJUDICO YO AQUI, Y DIGO POR QUE.** Si esto cae, cae por `D.27`
(procedimiento contra definicion) sobre un nodo **ya insertado**, y esa es sede de
`CLASE`. **Lo dejo levantado con los tres pasos citados** y lo adjudico en el acta con
su reporte delante. Lo que no voy a hacer es dejarlo sin escribir: **una cabeza de
serie cuyos unicos imperativos son los nombres de sus partes es exactamente la figura
que `P.5.1` congelo.**

### 7.2. **DISCUTIBLE 2: el `0 PUENTE` que un resumen sigue afirmando debajo de su propia correccion**

    $ (cuarentena/.../pedir_critica_primero...json, resumen_teorico, arbol de hoy)
    "... RELECTURA DE FIDELIDAD D.30 EN EL ACTO, paso a paso contra su linea: 17 pasos,
     17 TRANSCRIPCION, 0 PUENTE. ... CORRECCION DECLARADA 18 sep 2026, vuelta 38,
     relectura de fidelidad D.30 antes de insertar, DOS defectos ..."

**El mismo campo afirma `0 PUENTE` y, unas frases despues, `DOS defectos`.** La
correccion declarada esta bien hecha y no borra nada, que es lo que la casa manda; **lo
que no se toco es la cifra vieja, que sigue leyendose como vigente.**

**POR QUE IMPORTA Y NO ES UNA QUISQUILLA:** `resumen_teorico` **viaja al
`dataset/nodos.jsonl` cuando el candidato entra**, y ahi es sede de `CIFRA PUBLICADA`
(`5.2`). Hoy esta pieza esta en la bandeja y **todavia no lo es. Entra asi y lo es.**

**LO QUE NO CARGO, Y LO SEPARO:** `practicar_triangulo` **ya entro** a las `02:34:42` y
su resumen tambien dice `15 TRANSCRIPCION, 0 PUENTE` con su correccion detras, **pero
ahi la cifra es cierta**: su defecto era de grafia (*groseria* con tilde) y no de
`D.30`, y el propio texto lo dice. **Ese no lo cargo.**

---

## 8. LAS DOS CIFRAS DE LAS CORRECCIONES, COMPROBADAS CON EL INSTRUMENTO

Las dos viven en `resumen_teorico`, o sea que van camino de una sede duradera.

**PRIMERA: *el unico caracter acentuado de los seis candidatos*, y *uno de los dos
unicos de todo `dataset/nodos.jsonl`, que tiene `318` nodos*.**

    $ (censo de vocales acentuadas sobre el arbol de 3f3a949, que es donde el lo midio)
    3f3a949   nodos=318   vocales acentuadas=2
          i con tilde     ...contandole como creia que se medIa su exito en ese papel...
          u con dieresis  ...Eso avergUenza al candidato, da a entender...

    $ (mismo censo sobre bandeja + insertados de scott, hoy)
    total = 0

**LA MITAD QUE SE SOSTIENE AL DIGITO:** vocales acentuadas, son `2` y son esas dos,
en el arbol de entonces y en el de ahora.

**LA OTRA MITAD YA NO, Y CAMBIO DE SEDE MIENTRAS YO ESCRIBIA ESTA PAGINA.** El
`318` era cierto en `3f3a949`. Pero `practicar_triangulo` **entro al grafo a las
`02:34:42`** (seccion 1), asi que esa frase **ya no esta en la bandeja: esta dentro de
`dataset/nodos.jsonl`**, que es sede de `CIFRA PUBLICADA` por `5.2`:

    $ (dataset/nodos.jsonl, resumen_teorico de practicar_triangulo_critica_tres_papeles)
    "... uno de los dos unicos de todo dataset/nodos.jsonl, que tiene 318 nodos."

    $ wc -l dataset/nodos.jsonl
    321 dataset/nodos.jsonl

**LECTURA:** una cuenta de nodos escrita **sobre** un fichero acabo publicada **dentro
de** ese fichero, y **la propia insercion que la publico la dejo corta**: dice `318`
donde el fichero que la contiene tiene `321` lineas. **Lo que falla es solo la cuenta
de nodos**; el `2` de vocales acentuadas, que es lo que la correccion de grafia
necesitaba, **sigue siendo cierto hoy**. Lo mido y no lo adjudico: si una cifra cierta
al escribirse cuenta al mudarse de sede es adjudicacion de acta.


**SEGUNDA: *consejero delegado, `36` apariciones en `dataset/nodos.jsonl` contra `1`
de ceo*.**

    $ grep -o -i 'consejero delegado' dataset/nodos.jsonl | wc -l     39
    $ grep -o -iE '\bceo\b' dataset/nodos.jsonl | wc -l                0
    $ (mismo censo corrido sobre 3f3a949, el arbol en que el lo midio)
      "consejero delegado" = 39   |   "ceo" = 0

**NO SE SOSTIENE, y en el segundo no es por poco:** son **`39` y `0`**, no `36` y `1`,
y **en el mismo arbol en que el lo midio**, asi que no es que se moviera el arbol
debajo.

**LECTURA, Y SEPARO LAS DOS COSAS:** **la eleccion de grafia que la cifra sostiene es
la correcta** (`consejero delegado` es la grafia de la casa por goleada, y `ceo` no
aparece ni una vez), **y la correccion del `P15` esta bien hecha**. Lo que esta mal es
**la cifra que se cito para justificarla**. La sede es `resumen_teorico` de un
candidato que **aun esta en la bandeja**, asi que hoy no es `CIFRA PUBLICADA`; **lo es
en cuanto entre.**

---

## 9. EL BARRIDO DE VECINOS (`D.38.4` y `D.38.5`), SOBRE GRAFO MAS BANDEJAS

**LA POBLACION DEL BARRIDO, MEDIDA ANTES DE CORRERLO:**

    $ python forja.py resolutor                                      nodos vivos: 321
    $ ls cuarentena/scott_radical_candor/*.json | wc -l               24
    grafo 321 + bandeja de scott 24 = 345 titulos vivos, sello 02:41:02

Corrido con el instrumento de la casa, que desde `D.38.5` carga **la misma poblacion
que yo**, sobre la primera pieza del tramo que aun no ha entrado:

    $ python forja.py informe cuarentena/scott_radical_candor/pedir_critica_primero_crear_seguridad_psicologica.json
    (arrancado a las 02:40:58. La aduana en seco cuesta minutos por candidato: la
     ACTA 36 la midio en 367 s. Su salida queda en .a37/ar_pieza04.txt y se cruza en
     el acta.)

**EL VECINO QUE DECIDE YA LO LEI A MANO Y ESTA EN `6.2`**, porque es el unico par del
tramo donde la vara puede dar `REPITE`: `empezar_cultura_franqueza_radical`, de
`cap_05`. **No espero a la maquina para eso**: `D.19` dice que una discrepancia **no se
adjudica citando una senial**, se adjudica leyendo los pasos, **y los pasos ya estan
leidos y pegados.** La senial dice donde mirar y ahi acaba su trabajo.

---

## 10. LO QUE DEJO SIN HACER, DICHO POR SU NOMBRE

| que | por que |
|---|---|
| **`91` de los `212` pasos de `cap_13`** (piezas `7` a `12`, menos `dar_elogio` `P13`) | fuera del tramo de esta vuelta; por eso **no publico por ciento de capitulo entero** |
| **el campo de clase y el de razon de `bitacora/VEREDICTOS.jsonl`** | `1.2` manda adjudicar antes de destapar; solo conte lineas |
| **`.v38/informes/` y `.v38/guardas.sh`** | son el rastro de trabajo del extractor en esta vuelta. **Los mire por su hora, no por su contenido**, que es lo que la seccion 1 necesita |
| **el cruce del informe de aduana de la pieza `4`** | arranco a las `02:40:58` y cuesta minutos; **su fichero esta nombrado y su salida se cruza en el acta** |
| **de quien es la caida de la seccion 1** | esa adjudicacion es del acta, con el reporte delante |
| **la racha viva de mi linea** | `CREDITO_serial.jsonl` no esta en el arbol en esta fase y `forja.py credito` contesta `LINEA SIN REGISTRO`. **Eso NO significa racha en cero**, y no lo publico como si lo significara |

---

## 11. RESUMEN DE LA APERTURA

1. **El arbol se movio dentro de mi fase ciega**: el mismo `gate` dio `320` y luego
   `321`, y `dataset`, `bitacora`, `censos` y `.git/index` llevan todos la hora
   `02:34:42`. **Toda cifra de grafo de esta pagina lleva sello de hora por eso.**
2. **`tests/test_aceptacion.py` esta en ROJO** con `8 != 6`: la vuelta subio la cola de
   doctrina y dejo clavada la prueba que la vigila. Las otras cuatro caidas **si** son
   artefacto de mi fase, con su causa leida en `src/herencia.py:259` y no supuesta.
3. **El volcado `docs/loop/TABLERO.jsonl` trae `6` donde la sede viva trae `8`.**
4. **La fila de `PASOS INVENTADOS` de mi tramo es `3` de `101`, `2,97` por ciento**, no
   `0`, **debajo del techo de `10`**, y **declaro que dos de los tres me llegaron por el
   prompt del arnes** y no por mi lectura.
5. **`DISCUTIBLE 1`**: la cabeza de serie que entro al grafo **solo nombra a sus dos
   partes**, y `P.5.1` tiene una fila escrita para esa figura.
6. **`DISCUTIBLE 2` y seccion 8**: dos cifras camino de sede duradera, una que se
   contradice con su propia correccion y otra que no se sostiene (`39` y `0`, no `36` y
   `1`).

---

## 12. EL `grep` SOBRE MI PROPIA PAGINA, QUE CIERRA EL `HEREDADO 1`

*La casilla `PUENTE` de mi fila es `3` y no `0`, asi que la condicion del heredado
(`un 0 en esa casilla con la palabra PUENTE escrita en mi propia pagina no se publica`)
**no llega a activarse**. Aun asi lo corro y lo pego, porque el remedio pide el barrido
y no solo su conclusion.*

> **Y UNA ADVERTENCIA SOBRE ESTA CIFRA, porque es la trampa del propio remedio:** el
> `grep` sobre la pagina **se cuenta a si mismo**. En cuanto pego su salida, la palabra
> `PUENTE` aparece una vez mas por cada linea pegada, y volver a correrlo da un numero
> mayor. **Asi que la cifra que publico es la del CUERPO de la pagina**, o sea todo lo
> anterior a esta seccion 12, **y doy el comando que la reproduce al digito.** Una cifra
> que solo es cierta en el instante en que se escribio no es una cifra: es una foto.

    $ sed -n '1,/^## 12\./p' docs/loop/APERTURA_CIEGA.md | grep -c PUENTE
    18

    $ sed -n '1,/^## 12\./p' docs/loop/APERTURA_CIEGA.md | grep -n PUENTE
    24:`PUENTE` de este capitulo la escribo contra **lo que el extractor ESCRIBIO**, el
    25:`grep -n PUENTE` va corrido sobre la ultima acta **y sobre esta pagina**, con las dos
    301:| pieza | pasos | `PUENTE` que yo firmo | contra que linea |
    313:**`PUENTE 1`, pieza 2 `P8`.** Escribia *al jefe de su jefe* donde `L49` escribe
    319:    $ grep -n PUENTE docs/loop/ACTA_AUDITOR.md | sed -n 's/^30741://p'
    320:    **LOS TRES `PUENTE`, CON NOMBRE:** `desplegar_plan_orden_operaciones_franqueza_radical`
    325:**`PUENTE 2`, pieza 4 `P6`.** Lo que estaba escrito, sacado de `git` y no del arbol de
    339:**Una relacion de causa que el libro no escribe la escribio el extractor: `PUENTE`.**
    341:**`PUENTE 3`, pieza 4 `P15`.** Escribia *cuando quien manda pide critica* donde `L109`
    352:**`PUENTE 2` y `PUENTE 3` NO LOS ENCONTRE A CIEGAS, Y SERIA FALSO DECIR QUE SI.** El
    354:`3f3a949` entero, y ese asunto **nombra los dos pasos y los llama `PUENTE`**. Lo lei
    360:**`0` `PUENTE` mas**. Y el `PUENTE 1` **no estaba en ningun commit**: salio del `grep`
    372:| capitulo | pasos escritos | `TRANSCRIPCION` | `PUENTE` | **`PASOS INVENTADOS`** | contra el techo de `
    378:| capitulo | pasos escritos | `PUENTE` adjudicados hasta hoy | leidos por mi en esta fase | **sin leer**
    478:### 7.2. **DISCUTIBLE 2: el `0 PUENTE` que un resumen sigue afirmando debajo de su propia correccion**
    482:     17 TRANSCRIPCION, 0 PUENTE. ... CORRECCION DECLARADA 18 sep 2026, vuelta 38,
    485:**El mismo campo afirma `0 PUENTE` y, unas frases despues, `DOS defectos`.** La
    494:su resumen tambien dice `15 TRANSCRIPCION, 0 PUENTE` con su correccion detras, **pero
