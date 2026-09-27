<!-- ARCHIVO DEL FRENTE gerber_emyth: SOLO LO SUYO. Lo anterior es la sede de la serial que su arbol heredo, y vive en docs/loop/ACTA_AUDITOR.md de la serial. -->


---

# ACTA `G2` DEL FRENTE `gerber_emyth`. VUELTA 2, lote 9, `cap_05` y `cap_06` **EN CUARENTENA**, **CLASE EXTRACCION EN REGIMEN LIGERO**: **LA COSECHA CERO ES CIERTA Y SE LA FIRMO ENTERA TRAS LEER LOS DOS CAPITULOS LINEA A LINEA; LO QUE SE CAE ES UNA CELDA DE SU TABLA DE PARADA Y, LA MAS CARA, EL NUMERO QUE SE ESCRIBIO A SI MISMO EN EL REGISTRO DE CREDITO**. Le recompongo **las `9` filas de las dos fronteras** contra el fichero y me salen **al digito** (`2400` y `1980` palabras, residuo `0`, `0` solapes, `0` lineas sin cubrir), le reproduzco **las `32` celdas de su tabla de apertura** una a una, su muestra de fidelidad con semilla `g2` me sale **identica byte a byte**, sus cuatro `git hash-object` me salen **los cuatro**, y **los tres discutibles que marco se sostienen los tres**, con **tres superficies mas que el NO marco y que examino yo**. Y aun asi: **su tabla de parada dice `los dos discutibles` donde hay `3`**, y **el registro de credito de esta linea publica `1 de 3` para una tanda que el mismo declara limpia**, cuando su encargo le dijo por escrito que su racha empieza en cero. **`REPORTE` sube a `2 de 3` y `CIFRA PUBLICADA` abre en `1 de 2`.** **Y MI PROPIA RACHA SUBE A `2 de 3`**, porque el remedio que la `ACTA G1` dejo escrito no se cumplio. **NO HAY PARADA, Y LAS DOS ESCALADAS VAN ENCARGADAS**

*Escrita el 21 sep 2026 por el auditor del bucle, sobre el commit `0fd8e1d` de la rama
`extraccion-gerber_emyth`, worktree `C:/Users/AlexDesk/Documents/forja-gerber_emyth`.
**Clase de la vuelta auditada: EXTRACCION en regimen ligero** (`D.58`), asi que **no hubo fase
ciega, ni sello, ni testigo**, y esta acta es corta por mandato de esa misma regla y de `D.47`.*

---

## 0. **NO HAY HUECO DE ACTA**, y la herencia se declara antes que nada

**La `ACTA G1` cubre la vuelta `1` de este frente y yo cubro la `2`.** No hay vuelta sin auditar
entre las dos. La `ACTA G1` no vive en este fichero porque el commit `c01e8aa` archivo la sede
propia del frente al reanudarlo:

    $ grep -c "^# ACTA .G1. DEL FRENTE" docs/loop/archivo/gerber_emyth/ACTA_AUDITOR_frente_hasta_G1.md
    1
    $ git log --oneline -1 c01e8aa
    c01e8aa Reanuda el frente gerber_emyth: trae la maquinaria, la doctrina y el grafo de la serial, y archiva su propia sede

**ACTA ANTERIOR LEIDA:** `docs/loop/archivo/gerber_emyth/ACTA_AUDITOR_frente_hasta_G1.md`,
seccion `7`, y su parada archivada en
`docs/loop/paradas/2026-09-17-gerber-la-racha-y-la-linea-vieja-RESUELTA.md`.

**EL ARNES NO ME ENTREGO NINGUN `REMEDIOS PENDIENTES QUE HEREDAS`** (`D.40`), y no es un
descuido suyo: **entre la `G1` y la `G2` el arnes no corrio.** El frente se reanudo a mano y el
encargo de la vuelta `2` lo escribio una sesion de chat, que lo declara en su propia cabecera.
**Los fui a buscar yo, y por eso los numero aqui.**

| | heredado de la `ACTA G1`, seccion `5` de su parada | como queda hoy, medido |
|---|---|---|
| **HEREDADO 1** | correccion declarada CON TACHADO de tres celdas del bloque `G1`: la de `G1.10.d` que cita `G1.10.e` (seccion que no existe), la fila `CERRADO` del esqueleto `G1.0`, y la apertura de `G1.9` que promete un saldo que no llego | **NO CUMPLIDO** |
| **HEREDADO 2** | correr `python .v1g_auditor/secciones.py` antes de cerrar cualquier reporte, y que de `0` | **NO CUMPLIDO, y hoy el instrumento REVIENTA** |
| **HEREDADO 3** | tramo de `5` candidatos arrancando en `cap_12` | **CADUCADO por `D.13`**, y el motivo esta debajo |

**HEREDADO 1, medido y no recordado.** La celda sigue sin tachar:

    $ grep -n "G1.10.e" docs/loop/archivo/gerber_emyth/REPORTE_frente_hasta_v1.md
    36809:| una guarda en rojo | **ninguna en este turno.** Las cuatro de `G1.10.e` en verde al sellar | **NO ES PARADA** |

**HEREDADO 2, con su salida pegada** (`D.40` ensanchada: un incumplimiento tambien lleva el
comando que lo sostiene):

    $ python .v1g_auditor/secciones.py
    Traceback (most recent call last):
      File "C:\Users\AlexDesk\Documents\forja-gerber_emyth\.v1g_auditor\secciones.py", line 6, in <module>
        ini = max(i for i, l in enumerate(texto) if l.startswith('# FRENTE `gerber_emyth`, VUELTA 1'))
    ValueError: max() iterable argument is empty
    $ grep -c "^# FRENTE .gerber_emyth., VUELTA 1" docs/loop/REPORTE.md
    0
    $ grep -c "^# FRENTE .gerber_emyth., VUELTA 1" docs/loop/archivo/gerber_emyth/REPORTE_frente_hasta_v1.md
    1

> **LECTURA:** el instrumento busca el bloque `G1` dentro de `docs/loop/REPORTE.md`, y **ese
> bloque se archivo**. No esta roto por su codigo: esta apuntando a donde el bloque ya no vive.
> **Sigue siendo cumplible** apuntandolo al fichero archivado, y asi va encargado.

**HEREDADO 3: CADUCADO, y lo adjudico citando regla y no comodidad.** Mandaba arrancar en
`cap_12` con tramo de `5`. La decision del fundador del `21` sep `2026`, punto `3`, es
**posterior** y manda continuar desde `cap_05` con la frontera heredada. **`D.13`: entre dos
reglas fechadas que chocan gana la mas reciente**, y la perdedora se corrige sin borrarse. Su
disparador, ademas, era `EXTRACTOR.md` `12.4` por un reporte que no cerro en su turno, **y la
vuelta `2` si cerro el suyo**.

---

## 1. LO QUE VERIFIQUE CON MIS PROPIOS COMANDOS

### 1.1. Las guardas, corridas por mi en este turno

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python tests/test_aceptacion.py
      total: 343 pruebas, 0 fallos, 0 errores
    $ python forja.py resolutor
    nodos vivos: 346
    nodos deprecados (archivo): 0
    alias registrados: 0
    $ python scripts/tallar_reporte.py
    TALLADO VERDE: las 161 tabla(s) comprobables son las de su instrumento, celda a celda.
    $ python scripts/censar_rutas.py
    CENSO VERDE: las 922 rutas publicadas sostienen lo que dicen sostener.

**Las cuatro guardas que bloquean** (`D.55`: `gate`, el cerrojo, el censo no decreciente y la
fidelidad `D.30` con puente) **estan en VERDE.** Ninguna averia que reparar antes de seguir.

### 1.2. Mi propio conteo del dataset y de la bitacora

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
    $ ls cuarentena/gerber_emyth/*.json | wc -l
    10
    $ git diff --name-only 072b49f..HEAD -- dataset/ bitacora/ censos/ config/pares_mutuos.jsonl
    (vacio)

**`346`, `740` y `10` coinciden con su apertura (`G2.1`) y con su cierre (`G2.8.b`), y `0`
ficheros de dato movidos.** La vuelta no toco el grafo, y eso lo mido yo, no lo copio.

### 1.3. Las dos fronteras, recompuestas por mi contra el fichero y no contra su salida

**No corri su instrumento: escribi el mio.** Deriva el arranque del cuerpo del propio fichero
(la linea siguiente al segundo cierre de la cabecera yaml), suma palabras por tramo, y cuenta
huecos y solapes:

    $ python -c "<mi recuento, fila a fila, sobre los dos ficheros>"
    fuentes/gerber_emyth/cap_05.md | cierres [1, 7] | cuerpo L8-L149 | palabras cuerpo 2400
        R1 L8-L19 39
        R2 L20-L31 148
        R3 L32-L89 862
        R4 L90-L149 1351
        SUMA 2400 RESIDUO 0 HUECOS 0 SOLAPES 0
    fuentes/gerber_emyth/cap_06.md | cierres [1, 7] | cuerpo L8-L221 | palabras cuerpo 1980
        R1 L8-L19 32
        R2 L20-L57 255
        R3 L58-L127 671
        R4 L128-L215 977
        R5 L216-L221 45
        SUMA 1980 RESIDUO 0 HUECOS 0 SOLAPES 0

> **LAS `9` FILAS DE LAS DOS FRONTERAS ME SALEN AL DIGITO**, y con ellas los dos totales, los
> dos residuos, los dos recuentos de solape y los dos de hueco. **`13` cifras.**

Y **los tres `diff` que el reporte pega tambien los corri yo**, porque una comparacion citada y
no corrida no prueba nada: `.gerber_v1/frontera.py` contra `.gerber_v2/frontera.py`, y las dos
salidas de `cap_05` y `cap_06` de una vuelta contra la otra. **Los tres vacios.**

### 1.4. Su tabla de apertura, celda a celda, contra mi propio conteo del libro

Conte yo las `22` unidades del libro con mi codigo, sin tocar el suyo:

    $ python -c "<mi recuento del cuerpo de las 22 unidades>"
    cap_01.md 1402 | cap_02.md 1212 | cap_03.md 2202 | cap_04.md 3713 | cap_05.md 2400
    cap_06.md 1980 | cap_07.md 4284 | cap_08.md 2183 | cap_09.md 2845 | cap_10.md 1411
    cap_11.md 4360 | cap_12.md 4206 | cap_13.md  364 | cap_14.md 3695 | cap_15.md 4685
    cap_16.md 4835 | cap_17.md 2448 | cap_18.md 5396 | cap_19.md 4431 | cap_20.md 1841
    cap_21.md 1851 | cap_22.md  904
    TOTAL CUERPO 62648 | ficheros 22

**Las `22` palabras de cuerpo me salen las `22`, y el total `62648` tambien.** Los `22` rotulos
de `unidad` y los `22` de `titulo_textual` los lei de las cabeceras yaml y **coinciden los
`44`**, incluido el salto de `Cap. 16` a `Cap. 18` en la tabla, que es correcto: el `Cap. 17`
esta apartado y **su fichero existe y es uno**.

**La celda `claves en la tabla canonica: 12` la comprobe por dentro antes de firmarla**, porque
el fichero tiene `13` claves de primer nivel: la que sobra es `_lea_esto`, y el instrumento
cuenta las que no empiezan por guion bajo. **La celda es de su instrumento y la cifra es
cierta.**

### 1.5. La muestra de fidelidad, recorrida con su semilla (`D.58`)

    $ python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_05,cap_06 --semilla g2 > /tmp/mf.txt
    $ diff /tmp/mf.txt .gerber_v2/muestra_fidelidad.txt
    (vacio)

**La lista que me sale es la que el reporte pego, byte a byte.** `cap_05` ENTERO, `cap_06` por
muestra, **`0` pasos en los dos**. `D.58` dice que una lista distinta es caida de cifra: **no lo
es.** Y el disparador del `10` por ciento **no tiene sobre que dispararse**: no hay paso.

### 1.6. Los cuatro `git hash-object` de la tabla de cierre

    $ git hash-object docs/loop/TABLA_DE_CIERRE.txt
    4c93373e3be91ae4a417ef7340047421af281c90
    $ git hash-object docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_gerber_v2.txt
    4c93373e3be91ae4a417ef7340047421af281c90
    $ git hash-object docs/loop/archivo/tablas_de_cierre/TABLA_DE_CIERRE_v62.txt
    e0fac5d10018d9bf513aa7c6c98c961f415e6319
    $ git rev-parse 072b49f:docs/loop/TABLA_DE_CIERRE.txt
    e0fac5d10018d9bf513aa7c6c98c961f415e6319

**Los cuatro me salen los cuatro.** Su afirmacion de que archivo la version viva antes de
sobrescribirla, y de que esa version era intacta la de la vuelta `62` de la serial, **se
sostiene contra git y no solo contra su prosa.**

---

## 2. `PASOS INVENTADOS POR CAPITULO`, QUE ES CIFRA MIA Y LA FIRMO (seccion `8`)

**No la copio: la conte yo contra la cuarentena**, que es lo que mi `8.3` punto `1` manda:

    $ python -c "<mi recuento de pasos y capitulo de origen, candidato a candidato>"
    construir_empresa_plantilla_vision_diaria    pasos  8 | ['cap_08']
    dar_valor_constante_cuatro_publicos          pasos  8 | ['cap_11']
    dictar_ritmo_crecimiento_preguntas_escritas  pasos  8 | ['cap_07']
    documentar_trabajo_manual_operaciones        pasos 10 | ['cap_11']
    fingir_prototipo_cinco_mil_replicas          pasos 11 | ['cap_11']
    hacer_trabajo_futuro_imaginar_negocio        pasos  7 | ['cap_04']
    interrogar_negocio_cinco_preguntas           pasos 10 | ['cap_11']
    operar_modelo_gente_destreza_minima          pasos 10 | ['cap_11']
    trazar_modelo_negocio_cliente_primero        pasos  9 | ['cap_08']
    unificar_color_forma_vestuario_modelo        pasos  8 | ['cap_11']
    TOTAL pasos en bandeja: 89

| capitulo | candidatos nuevos que yo cuento | pasos escritos que yo cuento | PUENTE | pasos inventados |
|---|---:|---:|---:|---|
| `cap_05` | `0` | `0` | `0` | **SIN SUPERFICIE** |
| `cap_06` | `0` | `0` | `0` | **SIN SUPERFICIE** |
| **la vuelta `2` entera** | **`0`** | **`0`** | **`0`** | **SIN SUPERFICIE** |

> **LECTURA:** `SIN SUPERFICIE` es lo correcto y no una evasiva. `D.59` prohibe publicar una
> razon sin numerador y sin denominador, y el denominador aqui es `0`. **Ninguno de los `89`
> pasos de la bandeja sale de `cap_05` ni de `cap_06`**, asi que el capitulo no aporto
> superficie sobre la que medir. **Su fila es la mia.**

**Mi `8.3` punto `2` (releer una muestra de los pasos marcados TRANSCRIPCION contra su parrafo)
se cumple con su cifra y no con una muestra inventada:** la poblacion de esta tanda es `0`
pasos. **No se inventa una muestra donde no hay poblacion** (seccion `7`).

**Y LO QUE ESTO LE DEJA AL VOLUMEN:** nada subio, porque nada se midio. La subida de `2` a `3`
capitulos del encargo siguiente **NO la sostiene esta metrica**: la sostiene el techo escrito de
`D.58`, y asi va dicho en el encargo.

---

## 3. LO QUE SE CAE, POR ESPECIE

### 3.1. `REPORTE`, **`1` caida que ACUMULA**: su tabla de parada cuenta `2` discutibles donde hay `3`

**La celda, y esta en una TABLA**, que es una de las tres sedes que hacen acumular a esta
especie (`5.2`):

    $ sed -n '57681p' docs/loop/REPORTE.md
    | una pregunta de doctrina | ninguna: los dos discutibles de `G2.7` son de lectura, no de regla, y no piden doctrina nueva | **NO ES PARADA** |

**Y el propio reporte se desmiente a si mismo dos secciones antes**, lo que quita toda duda
sobre cual de las dos cifras es la falsa:

    $ sed -n '57659p' docs/loop/REPORTE.md
    | `5` | el cierre | **CERRADA en `G2.8`**: estado recomputado (`346`/`740`/`10`), guardas en VERDE, `2` capitulos y `0` candidatos del tramo, `3` discutibles marcados |
    $ sed -n '57600,57607p' docs/loop/REPORTE.md | grep -c "^| [0-9]"
    3

**`G2.7` tiene `3` filas. `G2.8.c` dice `3`. `G2.8.d` dice `los dos`.**

> **POR QUE ACUMULA Y NO SE PERDONA.** No es prosa de acompanamiento: es **la columna de la
> medida** de la tabla que decide si el bucle sigue, y la fila que recorre es justamente la de
> `doctrina NUEVA necesaria`. **Una tabla de parada que no sabe cuantas dudas repaso no esta
> repasandolas.** Y lo digo tambien por el otro lado, que es lo que la hace justa: **el
> veredicto de esa fila es correcto**. Los tres discutibles son de lectura, los tres, y ninguno
> pide doctrina nueva. **Lo falso es la cifra, no la conclusion.**

**DENTRO CONTRA FUERA DEL MARCADO** (`5.3`): **FUERA.** El extractor marco `3` discutibles y
acerto en los `3` sitios donde tenia duda; **lo que no vio fue la cuenta de sus propias dudas.**

**`REPORTE` pasa de `1 de 3` (tanda `G1`) a `2 de 3`.** Es el penultimo escalon, y la escalada
va encargada en `8`.

### 3.2. `CIFRA PUBLICADA`, **`1` caida que ACUMULA**: la racha que se escribio a si mismo

**La linea, tal como quedo escrita en el registro:**

    $ head -1 docs/loop/CREDITO_gerber_emyth.jsonl
    {"cita": "REPORTE.md seccion G2", "especie": "REPORTE", "linea": "gerber_emyth", "racha": "1 de 3", "tanda": "G2", "tipo": "tanda", "vuelta": 2}

**LO QUE LA HACE FALSA, y son dos cosas distintas que se suman:**

1. **El numero contradice su propia declaracion.** La tanda `G2` **se declara limpia de punta a
   punta**: `G2.8.d` repasa las cinco condiciones de parada y ninguna se cumple, y el bloque no
   declara ni una caida propia. **`D.38.1` es explicita: una tanda limpia pone el contador a
   CERO, no lo congela.** Bajo su propia declaracion la celda tenia que decir `0 de 3`.
2. **Y su encargo se lo habia dicho con todas las letras**, asi que no hay lectura ancha que lo
   salve:

       $ git show 072b49f:docs/loop/PROMPT_SIGUIENTE.md | grep -n "empieza en"
       Escribe tu tanda: python forja.py credito --anotar. Tu racha es tuya y empieza en
       cero (D.48). Una linea que no escribe su credito nace de nuevo cada vuelta [...]

**Y ES FALSA BAJO LAS DOS LECTURAS POSIBLES, que es lo que me deja adjudicarla sin doctrina
nueva.** Si la tanda `G2` es limpia, el numero es `0 de 3`. Si la tanda `G2` cae (y cae, por
`3.1`), entonces con la tanda `G1` en `1` el numero es `2 de 3`. **`1 de 3` no es ninguno de los
dos.**

**POR QUE `CIFRA PUBLICADA` Y NO `REPORTE`, que es la pregunta que decide el escalon.** `5.2`
dice que **la sede decide la especie, no el dano**. La sede de `REPORTE` es
`docs/loop/REPORTE.md`, **que se reescribe cada vuelta**. Esta cifra no vive ahi: vive en
`docs/loop/CREDITO_gerber_emyth.jsonl`, que esta bajo `docs/`, **se anade y no se reescribe**, y
que la decision del fundador del `17` sep `2026` creo **precisamente para que el credito dejase
de vivir solo en un acta que nadie relee**. Es la sede mas duradera que esta cifra podia tener,
y **es el numero del que depende que el bucle pare o siga.**

**Y HAY UN SEGUNDO DEFECTO EN LA MISMA LINEA, que no cuenta aparte pero explica el primero:**
se escribio **sin `--limpia` y sin `--cae`**, y sin ese campo el instrumento **no puede
replayarla**:

    $ grep -n "cae" src/credito.py
    295:        if "cae" not in suceso or suceso.get("migrado"):
    300:        contador[especie] = contador.get(especie, 0) + 1 if suceso["cae"] else 0

Con el campo puesto, `revisar()` habria cazado el `1` contra el replay en el acto. **Sin el, el
instrumento toma el numero declarado como punto de partida y no acusa a nadie.** La guarda
estaba ahi y la linea paso por debajo.

**LO QUE DIGO A SU FAVOR, y lo digo porque es cierto y porque una metrica que solo acusa no es
una metrica:**

- **El encargo le mando escribir la tanda** (`seccion 5`), y en las `12` lineas del registro de
  la serial **la tanda la escribe siempre el AUDITOR**, con el nombre del acta en el campo
  `tanda` (`ACTA 59`, `ACTA 60`, `ACTA 61`). Aqui el campo dice `G2`, que es una seccion de su
  reporte. **El encargo le pidio adjudicar, y adjudicar no es suyo** (regla madre, manual
  principio `10`: **el que mide no adjudica**). **La primera responsabilidad de esta caida es
  del encargo**, que lo escribio una sesion de chat y no un auditor.
- **El error va CONTRA el, no a su favor.** Se cargo un escalon que no le tocaba. Queda
  descartada de plano la lectura de que la cifra se eligio por conveniencia.
- **Y supo hacerlo bien en el caso gemelo.** Su mensaje de cierre levanta, por su cuenta, que el
  encargo le mandaba escribir `docs/loop/PROMPT_SIGUIENTE.md` siendo sede del auditor, y lo
  declara como desviacion. **Es exactamente la misma figura**, y la otra mitad no la levanto.

**`CIFRA PUBLICADA` abre en `1 de 2`.** El tope es `2`. **No para**, y la escalada va encargada.

### 3.3. `CLASE` y `DATO MOVIDO`: **CERO las dos**

| especie | lo que mido | de donde |
|---|---|---|
| **`CLASE`** | **CERO.** El frente no inserta: `0` veredictos puestos, `bitacora/` intacta, `config/pares_mutuos.jsonl` en su unica linea | `1.2` |
| **`DATO MOVIDO`** | **CERO.** `0` ficheros de `dataset/`, `bitacora/`, `censos/` o `config/pares_mutuos.jsonl` movidos entre `072b49f` y `HEAD` | `1.2` |

### 3.4. La correccion del registro, hecha **anadiendo y sin borrar**

**La linea del extractor se queda donde esta.** Encima escribo mi tanda, que es lo que el `17`
sep mando que fuese parte de cerrar un acta, con la tanda `G1` entrando como `migrado` porque su
historia es anterior a este registro (el fichero nacio hoy) y su adjudicacion vive en
`docs/loop/paradas/`, que es donde `5.4` siempre mando que viviera:

    $ python forja.py credito
    CREDITO DE LA LINEA 'gerber_emyth' (D.48)
      registro: docs/loop/CREDITO_gerber_emyth.jsonl
      tandas: 3, en 7 suceso(s) de especie

      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            2 de 3     ACTA G2
      CIFRA PUBLICADA    1 de 2     ACTA G2
      CLASE              0 de 2     ACTA G2
      DATO MOVIDO        0 de 2     ACTA G2
      REPORTE            2 de 3     ACTA G2

      CREDITO ENTERO: ninguna especie en su tope.
    $ python forja.py credito --revisar
    REPLAY VERDE en la linea 'gerber_emyth': las 5 tanda(s) vigilables suman lo que declaran.
      1 suceso(s) migrado(s) quedan FUERA del replay: sus reinicios viven en docs/loop/paradas/, no en el registro.
    $ python forja.py credito --citas
    CITAS VERDES en la linea 'gerber_emyth': todas son referencia, ninguna trae una conclusion dentro (D.56).

---

## 4. LA RELECTURA CIEGA: **LOS TRES DISCUTIBLES SE SOSTIENEN LOS TRES**

**Declaro el limite de mi propia ceguera antes de adjudicar, porque de lo contrario la cifra no
vale.** En regimen ligero **no hay veredicto que destapar**: `bitacora/VEREDICTOS.jsonl` no se
toco y la razon escrita que `1.2` de mi protocolo manda destapar al final **no existe en esta
vuelta**. Lo que si hice, y es lo unico que aqui significa algo: **lei
`fuentes/gerber_emyth/cap_05.md` y `fuentes/gerber_emyth/cap_06.md` enteros, linea a linea, las
`149` y las `221`**, y adjudique con `EXTRACTOR.md` `9` y `9.1` delante. **Su prosa la habia
leido antes**, y por eso **anado en `4.4` tres superficies que el NO marco**: es ahi, y no en
sus tres, donde se ve si lei yo.

### 4.1. Discutible `1`: `cap_05` `R2`, las tres fases. **SE SOSTIENE.** Y `D.37` no aplica, y lo cito

**La linea que lo levanta**, y la marca el bien:

    $ sed -n '29p' fuentes/gerber_emyth/cap_05.md
    To understand why, let's take a look at the three phases of a business's growth: Infancy, Adolescence, and Maturity.

**Dice CUANTAS partes hay y las NOMBRA.** Ese es literalmente el supuesto de `D.37`, asi que su
duda estaba bien puesta. **Y aun asi `D.37` no aplica, por su propia letra y por tres sitios:**

| lo que `D.37` exige | lo que hay aqui |
|---|---|
| *cuando el titulo o el texto de **UN NODO** enumera sus partes* | **no hay nodo.** La enumeracion vive en una pieza clasificada POSTURA, y una frase de un libro no es una cabeza |
| *y esas partes **EXISTEN COMO NODOS*** | **no existe ninguna.** `cap_05` (Infancy) y `cap_06` (Adolescence) dan `0` candidatos, verificado en `2` |
| *la arista se declara **EN EL ACTO DE INSERTAR LA PARTE*** | **no se inserta nada.** `MODO_INSERCION=cuarentena` y `D.39` no deja entrar a la bandeja |

**Y por la vara de `9.1`, que es la que decide si `R2` es nodo:** las tres fases son un
inventario, si, **pero de FASES por las que un negocio pasa**, no de medios, etapas u objetos de
trabajo que el libro mande ejecutar. **Nadie ejecuta la Infancia.** Es la restriccion `1` en su
forma mas limpia: **nombrar adonde va la narracion sigue siendo nombrar.** Y `9.1` arranca por
*una linea NORMATIVA se vuelve procedimentable*: **`R2` no tiene mandato ninguno**, asi que la
prueba del inventario ni siquiera llega a abrirse.

> **LECTURA, y va marcada porque es conclusion mia y no medida:** la clasificacion es correcta
> **y ademas no cuesta nada**, que es la parte que su duda temia. `D.37` es una regla sobre el
> CABLE, no sobre el NACIMIENTO, y opera en el acto de insertar. Si una vuelta futura hace nacer
> una cabeza de las tres fases, **la arista se declarara entonces citando `cap_05` L29**, y esa
> linea no se va a ninguna parte. **Queda anotado en `docs/loop/DEUDA.jsonl` como `d098` para
> que no dependa de que alguien lo recuerde.**

### 4.2. Discutible `2`: `cap_06` `R3`, *Management by Abdication*. **SE SOSTIENE**, y traigo la medida que lo cierra

    $ sed -n '103p' fuentes/gerber_emyth/cap_06.md
    It's called Management by Abdication rather than by Delegation .

**Su lectura es la correcta y la vara madre la sostiene palabra por palabra:** *una linea solo
cuenta como procedimiento propio si trae procedimiento propio, **y no solo el nombre de otro***.
Aqui `Delegation` es **exactamente el nombre de otro**: el capitulo no dice ni una vez en que
consiste delegar, ni con que se hace, ni por que etapas pasa. Un nombre de error frente a un
nombre de alternativa **no es un inventario de dos vias: son dos etiquetas.**

**Y NO SE PIERDE NADA, que es lo que su duda queria saber. Lo mido:**

    $ grep -rn -i "delegat" fuentes/gerber_emyth/*.md fuentes/gerber_emyth_cap17_reservado/*.md
    fuentes/gerber_emyth/cap_06.md:103:It's called Management by Abdication rather than by Delegation .
    fuentes/gerber_emyth/cap_11.md:113:That is, the typical small business owner prefers Management by Abdication to Management by Delegation .
    fuentes/gerber_emyth/cap_18.md:345:"Remember Delegation rather than Abdication?
    fuentes/gerber_emyth/cap_18.md:347:"You can't delegate your accountabilities, Sarah.
    fuentes/gerber_emyth/cap_18.md:349:"Delegating your accountabilities is abdication.

> **LECTURA:** el libro **nombra** el contraste en `cap_06` y en `cap_11`, y **vuelve sobre el
> con contenido propio en `cap_18`** (`Cap. 16`, *Your People Strategy*, `5396` palabras,
> **SIN MINAR**). `EXTRACTOR.md` `9` admite como nodo *un procedimiento que el libro nombra en
> una tabla y desarrolla en otro sitio*: **el sitio donde se desarrolla es `cap_18`, no
> `cap_06`.** El cero de `cap_06` no pierde el nodo: **lo deja donde nace.** Anotado como
> `d099`, y `cap_18` entra por este motivo en la cola del encargo.

### 4.3. Discutible `3`: haber aceptado la frontera de la vuelta `1` sin repartir `R3`. **SE SOSTIENE**, y lo probe donde el dijo

**La pieza que el senala es `cap_05` `R3`, `58` lineas, `862` palabras.** La lei entera buscando
lo unico que un corte mas fino podria haber aislado: un tramo con forma de procedimiento dentro
de una narracion. **El unico candidato a ese corte son las `L67` a `L73`**, que es donde el
texto cambia a verbos sueltos:

    $ sed -n '67,73p' fuentes/gerber_emyth/cap_05.md | tr -s '\n' ' '
    What do you do? You stretch. You work harder. You put in more time, more energy.  If you put in twelve hours before, you now put in fourteen.  If you put in fourteen hours before, you now put in sixteen.  If you put in sixteen hours before, you now put in twenty. But the balls keep dropping!

> **LECTURA:** es **descripcion de lo que el duenio hace**, en segunda persona narrativa, y el
> propio parrafo la cierra diciendo que no funciona (*but the balls keep dropping*). **Un
> procedimiento que el libro presenta para decir que fracasa no es un procedimiento que el libro
> mande ejecutar.** Un corte mas fino habria aislado el tramo y habria dado el mismo cero.
> **Ceder al corte de la vuelta `1` no le costo nada, y lo compruebo en vez de concederselo.**

### 4.4. **LAS TRES SUPERFICIES QUE EL NO MARCO Y QUE MIRE YO**, que es donde se ve si lei

**Mi seccion `7` dice que la relectura de los marcados mide un error y que el otro error, el de
dejar pasar, hay que medirlo aparte.** Aqui no hay `SANO` que pinear, asi que lo que hago es lo
equivalente: **ir a las piezas donde el NO dudo y buscar inventario.** Fui a tres, y son las
tres que mas se acercan en los dos capitulos.

| # | pieza y linea | por que la mire | mi veredicto |
|---:|---|---|---|
| **a** | `cap_05` `R4`, **`L131`** | es **la unica enumeracion cerrada de los dos capitulos**, y el no la marco | **NO ES NODO** |
| **b** | `cap_05` `R4`, **`L141`** | trae **tres verbos en fila** sobre que hacer con el Entrepreneur | **NO ES NODO** |
| **c** | `cap_06` `R2`, **`L37` a `L41`** | trae **tres patrones nombrados uno a uno** | **NO ES NODO** |

**(a), y es la mas seria de las tres:**

    $ sed -n '131p' fuentes/gerber_emyth/cap_05.md
    [...] "get rid of your business! And get rid of it as quickly as you can. [...] You can't
    ignore the financial accountabilities, the marketing accountabilities, the sales and
    administrative accountabilities. [...] cash flow, growth, customer sensitivity,
    competitive sensitivity, and so forth.

> **LECTURA:** tiene imperativo (*get rid of your business*) y tiene lista nombrada, que son las
> dos senales que `9.1` busca. **Y aun asi no es nodo, por tres sitios a la vez.** Primero, la
> forma es **una advertencia** (*you can't ignore*), y `9` la nombra por su nombre: *una
> advertencia es linea, no procedimiento*. Segundo, **la lista se cierra en `and so forth`**: el
> libro la deja ABIERTA, y una lista abierta no es el inventario propio del libro. Cualquier
> paso que la cerrase **lo escribiria el extractor**, que es la definicion literal de PUENTE en
> el corolario de `9.1`. Y tercero, lo que enumera son **areas de responsabilidad**, o sea
> fines, no medios ni etapas ni objetos de trabajo: **restriccion `1`.**
>
> **LO DIGO PORQUE ES LA QUE YO HABRIA MARCADO EN SU LUGAR**, y que no la marcase es lo unico de
> su lectura que le reprocho. **No cambia su cero**, y por eso no es caida de nada: es una duda
> que faltaba en su lista de dudas.

**(b):** *your Entrepreneur needs to be coaxed out, nourished, and given **the room she needs**
to expand* (`L141`). Tres verbos, si, **pero el criterio es un adjetivo de adecuacion**: *the
room she needs*. **Restriccion `2` de `9.1`: el adjetivo de adecuacion en el sitio del criterio
TUMBA, aunque haya inventario.** No es nodo.

**(c):** *The sales-oriented owner goes out to find a production person* y las dos que le siguen
(`L37` a `L41`). Son **tres patrones que el libro OBSERVA**, en tercera persona y en indicativo,
y el parrafo entero existe para decir que esa busqueda es el error. **Describir lo que la gente
hace mal no es mandar hacerlo.** No es nodo.

> # **FIRMO EL CERO DE LOS DOS CAPITULOS.** `3` de `3` discutibles suyos en pie, `3` superficies
> mas miradas por mi, y **ninguna pasa la vara de `EXTRACTOR.md` `9`**. Los dos capitulos son
> diagnostico narrado, y `cap_06` se cierra con la bisagra hacia el `cap_07`, que es donde la
> Comfort Zone se vuelve materia. **La cosecha cero es el resultado correcto, no un turno flojo.**

---

## 5. MIS PROPIOS ERRORES, CON MI NOMBRE (`5.3`)

### 5.1. `REMEDIO ROTO`: **el remedio de la `ACTA G1` no se cumplio, y la racha es de la LINEA**

**Lo declaro contra mi.** `D.48` dice que la racha es **de la linea**, no de la sesion, y la
racha del auditor de `gerber_emyth` venia en `1 de 3` por el `REMEDIO ROTO` que la propia
`ACTA G1` se cargo. **El remedio que esa acta dejo escrito sigue sin cumplirse** (`0`, los dos
puntos vivos), y `5.5` es explicita: **romper un remedio escrito acumula, sea de quien sea.**

**Y ES REMEDIO DE SUSTANCIA DE AUDITORIA, no de formato de artefacto**, que es la acotacion del
`12` sep: el punto `1` es una **correccion declarada de celdas publicadas** y el punto `2` es
**una comprobacion de cierre**. Ninguno de los dos es un volcado que escriba la tuberia del
arnes.

**LO QUE PODRIA ALEGAR Y NO ALEGO:** que el remedio nunca llego, porque el arnes no corrio entre
las dos vueltas y el encargo lo escribio una sesion de chat que no lo arrastro. **Es cierto y
esta medido en `0`. No me absuelve.** `D.40` nacio justamente porque *lo que un auditor le deja
al siguiente lo entrega el arnes, no la memoria*, y su propia historia son tres actas seguidas
escribiendo el mismo remedio y rompiendolo las tres. **Un auditor que elige la lectura que lo
deja seguir se esta absolviendo** (`5.4`), y esa es la unica regla de esta seccion que no tiene
matices.

**`AUDITOR` pasa de `1 de 3` a `2 de 3`.** Penultimo escalon. **Va encargado en `8`, como
`TAREA 1`.**

### 5.2. Lo que NO me cargo, y digo por que para que se pueda discutir

- **La relectura ciega sin veredicto que destapar** (`4`). No es caida: en regimen ligero no hay
  veredicto, y lo declaro en vez de escribir *relectura ciega* sobre una fase que no existio.
- **El coste del turno** (`D.55`, sobre `10` USD con desglose). **El del extractor lo mido:
  `7,161081899999999` USD**, leido de `docs/loop/ultimo_extractor.json`, **por debajo del tope**.
  **El mio no lo puedo medir**: el volcado lo escribe la tuberia del arnes en
  `docs/loop/ultimo_auditor.json` **cuando mi turno ya ha terminado**, que es la misma figura por
  la que la correccion del `12` sep saco de mi racha lo que no controlo. **Queda como medida
  pendiente del arnes, no como cifra mia sin medir.**

---

## 6. LO QUE REGISTRO Y NO ABRE PARADA (`D.55`, `D.56`)

**La cola de doctrina se queda en `11`.** Lo que sigue son preguntas con su medida, y `D.55` es
tajante: *registralas en tu acta con su medida y DEJALAS AHI.*

### 6.1. Las cinco anotaciones de deuda de esta acta

    $ python scripts/deuda.py --anotar --vuelta 3 [...]   (cinco veces)
    ANOTADA d095: EL REMEDIO QUE LA ACTA G1 DEJO ESCRITO NO LLEGO A LA VUELTA 2 Y SIGUE
    ANOTADA d096: SEGUNDO EJEMPLAR DE d088, EN UN LIBRO DISTINTO: capitulos_minados de d
    ANOTADA d097: LA CADENCIA DE SANEAMIENTO DE D.58 NO TIENE ARITMETICA EN UN FRENTE: s
    ANOTADA d098: EL PUNTERO D.37 DE gerber_emyth, ESCRITO PARA QUE NO SE PIERDA: fuente
    ANOTADA d099: DONDE NACE EL NODO DE LA DELEGACION DE gerber_emyth, SI NACE: cap_06 L

### 6.2. `d096`: el tablero no puede ver un capitulo minado a cero

    $ python -c "<lectura de la fila gerber_emyth de docs/loop/TABLERO.jsonl>"
    capitulos_minados: ['cap_04', 'cap_07', 'cap_08', 'cap_11']

> **LECTURA:** la vuelta `2` mino `cap_05` y `cap_06`, yo lo firmo en `4`, **y el tablero sigue
> diciendo cuatro.** El campo registra los capitulos que PRODUJERON candidato, no los que se
> LEYERON. **Es `d088`, medido en grove con `cap_08`, `cap_09` y `cap_18`**, y este es su
> segundo ejemplar en un libro distinto. **No lo toco:** `D.45` veda `src/` desde un frente y
> `D.56` congela la cola.

### 6.3. `d097`: la cadencia de saneamiento no tiene aritmetica en un frente

    $ python -c "import sys; sys.path.insert(0,'scripts'); import deuda; print(deuda.clase_de_vuelta(3))"
    ('LIBRE', 'van -56 de 5 desde la ultima de saneamiento (la 59), con 28 deuda(s) esperando')

> **LECTURA:** el veredicto `LIBRE` es el correcto, **y la cuenta que lo produce no lo es**:
> `docs/loop/DEUDA.jsonl` es un registro UNICO para todas las lineas y su ultima de saneamiento
> es la `59` **de la serial**, mientras que este frente numera sus vueltas `1`, `2`, `3`. Un
> numero negativo nunca alcanza la cadencia de `5`, asi que **un frente no puede recibir una
> vuelta de saneamiento por este camino, nunca.** Lo digo porque `D.58` dice que *la cadencia ya
> no es tuya* y que *ahora lo comprueba el codigo*: **en un frente, hoy, no lo comprueba.**
> **Anotado y no tocado**, por `D.45`.

### 6.4. `D.32`: no hay lote que abrir, y lo mido

    $ ls fuentes/gerber_emyth/cap_*.md | wc -l
    22
    $ ls .gerber_v1/piezas_cap*.txt .gerber_v2/piezas_cap*.txt | wc -l
    13

**El lote `9` esta ABIERTO, no cerrado**: `6` de `22` unidades minadas y adjudicadas
(`cap_04`, `cap_05`, `cap_06`, `cap_07`, `cap_08`, `cap_11`). `D.32` manda medir las dos
condiciones de apertura **si el acta cierra un lote**, y **esta no cierra ninguno.**

---

## 7. LAS CONDICIONES DE PARADA, REPASADAS UNA A UNA (`AUDITOR_FORJA.md` `3`)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| **doctrina NUEVA necesaria** | **ninguna.** Los `3` discutibles los adjudique citando `D.37`, `EXTRACTOR.md` `9` y `9.1`; las dos caidas, con `D.38.1`, `5.2` y `D.48`; el `HEREDADO 3`, con `D.13`; y el choque entre `5.5` y `D.55`, con `D.13` otra vez. **Las preguntas nuevas de `6.2` y `6.3` NO abren cola: `D.55` manda dejarlas anotadas** | **NO ES PARADA** |
| **contradiccion** con regla vigente o cifra publicada | **dos, y las dos se resuelven con las reglas de correccion existentes**: la celda de `G2.8.d` contra `G2.8.c`, que se corrige declarando sin borrar, y la linea del credito, corregida anadiendo en `3.4` | **NO ES PARADA** |
| **decision de Alexis** | **ninguna que este turno necesite**. No borro contenido, no muevo umbrales, no cambio el alcance, no creo remotos, no fundo ramas | **NO ES PARADA** |
| **fallo tecnico repetido** (dos vueltas por la misma causa) | **ninguno.** `gate`, `guiones`, `343` pruebas, tallado y censo, **los cinco en VERDE hoy** y ninguno en rojo en la vuelta anterior | **NO ES PARADA** |
| **credito roto** | **NO.** `REPORTE` `2 de 3` (tope `3`), `CIFRA PUBLICADA` `1 de 2` (tope `2`), `AUDITOR` `2 de 3` (tope `3`), `CLASE` y `DATO MOVIDO` en `0`. **Ninguna en su tope**, y el instrumento lo dice en `3.4` | **NO ES PARADA** |
| **campana consumada** | **no.** `6` de `22` unidades minadas, `10` candidatos en bandeja, `0` insertados | **NO ES PARADA** |

> # **NINGUNA DE LAS SEIS SE CUMPLE. NO ESCRIBO `PARA_ALEXIS.md`**, y el encargo de la vuelta
> `3` queda escrito en `docs/loop/PROMPT_SIGUIENTE.md`.

---

## 8. **LAS DOS ESCALADAS, ENCARGADAS Y NO SOLO DECLARADAS** (`5.5`, `1` punto `4`)

**`REPORTE` esta en `2 de 3` y `AUDITOR` esta en `2 de 3`: los dos en el penultimo escalon, y
los dos obligan.** `5.5` dice que se encargan **como tarea bloqueante en el mismo acta**.

**Y AQUI DOS REGLAS CHOCAN, ASI QUE LO RESUELVO CITANDO Y NO ELIGIENDO.** `D.55`, del `18` sep
`2026`, dice: *tu acta puede dejar como maximo UNA tarea bloqueante, y solo si cita la guarda de
DATO en rojo que la justifica*, y nombra las cuatro que bloquean. **Las cuatro estan en VERDE**
(`1.1`). `5.5` es del `9` sep. **`D.13`: entre dos reglas fechadas que chocan gana la mas
reciente.** Gana `D.55`.

> **ASI QUE LAS DOS ESCALADAS VAN COMO `TAREA 1` DEL ENCARGO, QUE ES LO PRIMERO QUE LA VUELTA
> HACE, Y NINGUNA VA COMO BLOQUEANTE.** La escalada **se encarga**, que es lo que `5.5` protege;
> lo que `D.55` quita no es el encargo, es el bloqueo. **Cero bloqueantes en esta acta.**

**Y el resto de lo pendiente va a `docs/loop/DEUDA.jsonl` con su cita**, que es exactamente lo
que `D.55` manda hacer con lo que no es averia: `d095` a `d099`, en `6.1`.

---

## 9. LA COLA, COMO QUEDA AL CERRAR ESTA ACTA

| lo que queda | cifra que mido hoy | que la cierra |
|---|---:|---|
| **el remedio de la `ACTA G1`, puntos `1` y `2`** | **`2`** vivos de `3` | **`TAREA 1` de la vuelta `3`** (`d095`) |
| unidades del lote `9` sin minar | **`16`** de `22` | las vueltas siguientes, a `3` capitulos (`D.58`) |
| candidatos en bandeja del lote `9` | **`10`**, con **`89`** pasos, **`0`** insertados | `D.39` y la cosecha, que es del fundador |
| `cap_01`, `cap_02` y `cap_03` sin minar | **`3`** | `d094`. **No es blocante y no se toca** |
| el nodo de la delegacion, si lo hay | **`1`** puntero, a `cap_18` `L345` a `L349` | `d099`. `cap_18` entra en la cola de capitulos |
| el puntero `D.37` de las tres fases | **`1`**, a `cap_05` `L29` | `d098`. **Solo en el acto de insertar una parte** |
| deuda pendiente de la linea | **`33`** pendientes, `31` pagadas | una vuelta de saneamiento, **que hoy no toca** (`6.3`) |
| preguntas de doctrina registradas y NO abiertas | **`2`** (`6.2` y `6.3`) | el cierre del mundo `11`. **`D.55` y `D.56`** |

---

*`ACTA G2` cerrada. **SIN PARADA.** Mis ficheros de trabajo de este turno son comandos sueltos y
no un directorio: cada cifra de esta acta lleva su comando pegado encima, que es lo que `D.38.3`
pide y lo que hace que se pueda repetir sin mi.*

---

# ACTA `G3` DEL FRENTE `gerber_emyth`. VUELTA 3, lote 9, `cap_09`, `cap_10` y `cap_12` **EN CUARENTENA**, **CLASE EXTRACCION EN REGIMEN LIGERO**: **TODO LO QUE MIDIO ME REPRODUCE, EL REMEDIO HEREDADO ESTA CUMPLIDO ENTERO, Y LO QUE SE CAE ES LA COSECHA DE `cap_12`: SU PROPIO DISCUTIBLE `1` TENIA RAZON Y EL CAPITULO DA AL MENOS TRES CANDIDATOS, NO UNO**. Le recompongo **las `19` filas de las tres fronteras** contra el fichero con codigo mio y me salen **al digito** (`2845`, `1411` y `4206` palabras, residuo `0`, `0` solapes y `0` lineas sin cubrir en las tres), **le vuelvo a correr yo el informe entero y sale IDENTICO BYTE A BYTE** (`160,8` s sobre poblacion `451`), su muestra con semilla `g3` me sale **identica byte a byte**, las `4` celdas del remedio `d095` estan **las `4`** con tachado y motivo, y su vecino `SANO` lo leo paso contra paso y **se lo firmo**. **PERO EL `R3` DE `cap_12` NO ESTA CERRADO**: los bloques `THE INNOVATION` de `L51` y `L63` son inventario propio del libro en imperativo, con sus etapas y sus objetos nombrados uno a uno, **y pasan `EXTRACTOR.md` `9.1` igual que lo paso `unificar_color_forma_vestuario_modelo` en la vuelta `1` de este mismo libro**. La cifra vive en la **CABECERA** y en **cuatro TABLAS**: **`REPORTE` sube de `2 de 3` a `3 de 3` y llega a su TOPE.** `CIFRA PUBLICADA` baja a `0 de 2`, `CLASE` y `DATO MOVIDO` siguen en `0`, y **mi propia racha baja de `2 de 3` a `0 de 3` porque el remedio que deje escrito SI se cumplio**. **PARADA POR CREDITO ROTO** (`3`, `5.4`): escribo `docs/loop/PARA_ALEXIS.md` y **dejo `docs/loop/PROMPT_SIGUIENTE.md` VACIO**.

*Escrita el 21 sep 2026 por el auditor del bucle, sobre el commit `4f2d2af` de la rama
`extraccion-gerber_emyth`, worktree `C:/Users/AlexDesk/Documents/forja-gerber_emyth`.
**Clase de la vuelta auditada: EXTRACCION en regimen ligero** (`D.58`), asi que **no hubo fase
ciega, ni sello, ni testigo**, y el propio arnes lo registro:
`[2026-09-21 08:40:28] sin sello que verificar: esta vuelta no tuvo fase ciega (D.58)`.
Acta corta por `D.58` y por `D.47`.*

---

## 0. **NO HAY HUECO DE ACTA**, y la herencia se declara antes que nada

**La `ACTA G2` cubre la vuelta `2` de este frente y yo cubro la `3`.** No hay vuelta sin auditar
entre las dos, y esta vez lo dice el arnes con su medida:

    $ grep -n "ROL INICIAL POR MEDICION" docs/loop/loop.log | tail -1
    [2026-09-21 07:53:20] ROL INICIAL POR MEDICION: EXTRACTOR. El ACTA no es mas vieja que el REPORTE: no hay vuelta sin auditar delante.

**ACTA ANTERIOR LEIDA:** `docs/loop/ACTA_AUDITOR.md`, `ACTA G2`, lineas `45107` a `45733`.

| | heredado de la `ACTA G2` seccion `8` | como queda hoy, medido |
|---|---|---|
| **HEREDADO 1** | la escalada de `REPORTE` (`2 de 3`), encargada como `TAREA 1` de la vuelta `3` y **no** como bloqueante (`D.55`, con las cuatro guardas de dato en verde) | **CUMPLIDO como encargo**, y su sustancia verificada en `1.6` |
| **HEREDADO 2** | la escalada propia de `AUDITOR` (`2 de 3`): que el remedio de la `ACTA G1` dejara de estar vivo | **CUMPLIDO Y MEDIDO**: `4` de `4` celdas y la comprobacion en `0` (`1.6`) |

**LA HERENCIA NO ME LA ENTREGO EL ARNES** (`D.40`), como tampoco a mi predecesor: el frente corre
con el orquestador pero el bloque `REMEDIOS PENDIENTES QUE HEREDAS` no llego en el prompt. **La fui
a buscar yo a mi propia acta**, que es lo que `AUDITOR_FORJA.md` dice expresamente que puedo hacer
en cualquier fase. **Lo declaro en vez de callarlo.**

---

## 1. LO QUE VERIFIQUE CON MIS PROPIOS COMANDOS

### 1.1. Las guardas, corridas por mi en este turno

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python tests/test_aceptacion.py
      total: 343 pruebas, 0 fallos, 0 errores
    $ python forja.py resolutor
    nodos vivos: 346
    nodos deprecados (archivo): 0
    alias registrados: 0
    $ python scripts/tallar_reporte.py
    TALLADO VERDE: las 165 tabla(s) comprobables son las de su instrumento, celda a celda.
    $ python scripts/censar_rutas.py
    CENSO VERDE: las 943 rutas publicadas sostienen lo que dicen sostener.

**Las cuatro guardas que bloquean** (`D.55`) **estan en VERDE. Ninguna averia que reparar**, y por
eso la parada de esta acta **no es tecnica**: es de credito.

### 1.2. Mi propio conteo del dataset, de la bitacora y de la bandeja

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
    $ ls cuarentena/gerber_emyth/*.json | wc -l
    11
    $ git diff --name-only 07aa6f2..HEAD -- dataset/ bitacora/ censos/ config/pares_mutuos.jsonl
    (vacio)

**`346` y `740` identicos a su apertura y a su cierre; la bandeja en `11`, que es `10` mas el
candidato de esta vuelta. Y `0` ficheros de dato movidos.** Los `95` pasos de la bandeja los conte
yo, ficha a ficha (`8+6+8+8+10+11+7+10+10+9+8`), y **son los `89` de la vuelta `2` mas los `6` de
esta**: su tabla `G3.8.c` me sale entera.

### 1.3. Las tres fronteras, recompuestas por mi contra el fichero y no contra su salida

**No corri su instrumento: escribi el mio.** Deriva el arranque del cuerpo del propio fichero (la
linea siguiente al segundo cierre de la cabecera yaml), cierra el cuerpo en la ultima linea no
vacia, suma palabras por tramo y cuenta huecos y solapes:

    $ python <mi recuento, fila a fila, sobre los tres ficheros>
    cap_09 | cierres [1, 7] | cuerpo L8-L233 | palabras 2845 (esperado 2845) OK
        R1  L8   -L19      47 OK      R2  L20  -L27     155 OK
        R3  L28  -L78     608 OK      R4  L79  -L110    312 OK
        R5  L111 -L172    605 OK      R6  L173 -L233   1118 OK
        SUMA 2845  RESIDUO 0  SOLAPES 0  SIN CUBRIR 0  FUERA DE CUERPO 0  piezas 6
    cap_10 | cierres [1, 7] | cuerpo L8-L145 | palabras 1411 (esperado 1411) OK
        R1  L8   -L19      83 OK      R2  L20  -L41     322 OK
        R3  L42  -L86     462 OK      R4  L87  -L135    455 OK
        R5  L136 -L145     89 OK
        SUMA 1411  RESIDUO 0  SOLAPES 0  SIN CUBRIR 0  FUERA DE CUERPO 0  piezas 5
    cap_12 | cierres [1, 7] | cuerpo L8-L293 | palabras 4206 (esperado 4206) OK
        R1  L8   -L19      57 OK      R2  L20  -L21      39 OK
        R3  L22  -L83    1055 OK      R4  L84  -L94     101 OK
        R5  L95  -L95     134 OK      R6  L96  -L147    326 OK
        R7  L148 -L221    687 OK      R8  L222 -L293   1807 OK
        SUMA 4206  RESIDUO 0  SOLAPES 0  SIN CUBRIR 0  FUERA DE CUERPO 0  piezas 8

> **LAS `19` FILAS DE LAS TRES FRONTERAS ME SALEN AL DIGITO**, y con ellas los tres cuerpos, los
> tres residuos, los tres recuentos de solape y los tres de hueco. **`31` cifras, cero que
> difieran.** La frontera de esta vuelta esta cerrada al digito y **eso es cierto sin matiz**: lo
> que se cae en `4.1` no es el corte, **es la clase que puso en una de las piezas.**

### 1.4. El informe de la aduana, corrido entero por mi, **identico byte a byte**

    $ python forja.py informe cuarentena/gerber_emyth/cuantificar_impacto_innovacion_6_pasos.json > .g3aud/informe_auditor.txt
    real 2m40.809s
    $ diff .g3aud/informe_auditor.txt .gerber_v3/informe_cuantificar_impacto_innovacion.txt
    (vacio)

**Poblacion `451`, `0` ENTRARIAN, `1` BLOQUEARIA, `0` CAERIAN, `0` CHOCAN**, y las tres cifras del
vecino identicas al milesimo (`0.396`, `0.000`, `0.432`). **Su `0 CAERIA` es cierto y se lo firmo.**
`160,8` s, por debajo de la banda que la `ACTA 60` publico (`389` a `1062` s sobre poblacion `440`),
y lo digo para que no se lea como contradicha: **este lote es de UN candidato, no de siete.**

### 1.5. La muestra de fidelidad, recorrida con su semilla (`D.58`)

    $ python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_09,cap_10,cap_12 --semilla g3 > .g3aud/muestra_g3.txt
    $ diff .g3aud/muestra_g3.txt .gerber_v3/muestra_fidelidad.txt
    (vacio)

**La lista que me sale es la que el reporte pego, byte a byte.** `cap_12` ENTERO, `cap_09` y
`cap_10` por muestra con `0` pasos. `D.58` dice que una lista distinta es caida de cifra: **no lo
es.**

### 1.6. El remedio `d095`, celda a celda, que es el `HEREDADO 2`

| # | celda | como esta hoy | donde lo verifico |
|---:|---|---|---|
| 1 | `G1.10.d`, la cita a `G1.10.e` | **TACHADA**, con la cifra de su `grep` y la guarda que si se puede citar (`G1.5`) | linea `36816` del fichero archivado |
| 2 | fila `CERRADO` del esqueleto `G1.0` | **TACHADA**, con el commit en que fue falsa (`a218170`) y aquel en que se volvio cierta (`abf7515`) | linea `36056`, y la tabla de `G1.10.a` lo sostiene commit a commit |
| 3 | apertura de `G1.9` | **TACHADA**, declarando la promesa incumplida (`91` bytes de cabecera) y citando donde vive el saldo | linea `36622` |
| 4 | `G2.8.d`, *los dos discutibles* | **TACHADA**, `3` y no `2`, citando `G2.7` y su propio `G2.8.c` | linea `57681` de `docs/loop/REPORTE.md` |

**Y la comprobacion de secciones, corrida POR MI sobre su bloque:**

    $ python .gerber_v3/secciones.py
    el bloque del frente empieza en la linea 57716 de docs/loop/REPORTE.md
    secciones que el bloque TIENE      : 15   G3.0 G3.1 G3.2 G3.3 G3.4 G3.5 G3.6 G3.7 G3.8 G3.8.a G3.8.b G3.8.c G3.8.d G3.8.e G3.9
    secciones que el bloque CITA       : 11   G3.1 G3.2 G3.3 G3.4 G3.5 G3.6 G3.7 G3.8.a G3.8.b G3.8.c G3.9
    CITADAS Y QUE NO EXISTEN           : 0

    $ python scripts/deuda.py | grep -c "^  d095"
    0

> **`d095` ESTA PAGADA Y NO SOLO DECLARADA.** Es el remedio que la `ACTA G1` escribio, que la
> `ACTA G2` se cargo a si misma por no cumplirlo, y que esta vuelta cumplio entero. **Lo pongo
> primero y con su medida delante porque es la mejor parte de esta vuelta y porque, en esta casa,
> tres actas seguidas escribieron el mismo remedio sin que llegase ninguna.**

---

## 2. `PASOS INVENTADOS POR CAPITULO`, QUE ES CIFRA MIA Y LA FIRMO CON UNA SALVEDAD (seccion `8`)

**No la copio: la conte yo contra la cuarentena** (`8.3` punto `1`), y **relei los `6` pasos contra
su parrafo** (`8.3` punto `2`), que es el paso que esta metrica invita a saltarse:

| capitulo | candidatos que yo cuento | pasos que yo cuento | PUENTE que yo leo | pasos inventados |
|---|---:|---:|---:|---|
| `cap_09` | `0` | `0` | `0` | **SIN SUPERFICIE** |
| `cap_10` | `0` | `0` | `0` | **SIN SUPERFICIE** |
| `cap_12` | `1` escrito (**`3` que el capitulo da**, `4.1`) | `6` | `0` | **`0,00` por ciento** |
| **la vuelta `3` entera** | **`1` escrito** | **`6`** | **`0`** | **`0,00` por ciento** |

**LOS `6` PASOS, RELEIDOS UNO A UNO CONTRA `L95`, DAN `6` TRANSCRIPCION Y `0` PUENTE**, y firmo el
`0,00`. **Las dos glosas que si mire y que NO cuento como puente, y las dejo a la vista para que el
siguiente lector pueda discutirmelas:**

- el paso `4` anade *despues del cambio* donde el texto dice solo *counting the number of people
  who purchased something*;
- el paso `6` anade *comparando los numeros de antes con los de despues* donde el texto dice
  *determining what the improvement was as a result of your Innovation*.

> **LECTURA, y es conclusion mia y no medida:** ninguna de las dos escribe un MEDIO, una ETAPA ni un
> OBJETO que el libro no ponga, que es lo que `D.30` llama PUENTE, y ninguna es de las tres especies
> que `15.4` nombra (destinatario, periodo, responsable). **Las dos hacen explicito el orden que la
> propia enumeracion impone**: el paso `3` ya dice *after you changed the words*, y la frase que
> cierra el parrafo dice *these numbers enable you to determine the precise value*. **Lo declaro en
> vez de contarlas en silencio: su discutible `2` iba justo aqui.**

**LO QUE ESTA CIFRA NO AUTORIZA.** `8.1` dimensiona el lote siguiente con ella, y `0,00` por ciento
mandaria subir un capitulo. **No lo encargo, y no por la cifra: porque no hay encargo que escribir**
(seccion `7`). Y `8.4` es explicita: **esta metrica no entra en la metrica de credito**, asi que el
`0,00` **no compensa nada** de lo que cae en `4.1`.

---

## 3. LA RELECTURA DE SUS DISCUTIBLES: **EL `1` CAE, EL `2` Y EL `3` SE SOSTIENEN**

**Declaro el limite de mi propia ceguera antes de adjudicar, porque si no la cifra no vale.** En
regimen ligero **no hay veredicto que destapar**: `bitacora/VEREDICTOS.jsonl` no se toco, y la razon
escrita que `1.2` de mi protocolo manda destapar al final **no existe en esta vuelta**. Su prosa la
habia leido antes de leer el libro. Lo que hice, y es lo unico que aqui significa algo: **lei
`cap_09`, `cap_10` y `cap_12` enteros, linea a linea, las `233`, las `145` y las `293`**, y adjudique
con `EXTRACTOR.md` `9` y `9.1` delante.

### 3.1. Discutible `1`: los tres `THE INNOVATION` de `cap_12` `R3`. **CAE**, y el lo marco bien

**Su marca, que es exacta y por eso va primero:**

    $ sed -n '57987p' docs/loop/REPORTE.md
    | 1 | clasifique `cap_12` `R3` [...] como CASO y no como procedimiento [...] El del traje azul en particular tiene tres pasos concretos [...]: si el auditor lo lee como procedimiento propio del libro y no como caso ilustrativo, ahi nace otro candidato |

**LOS TRES BLOQUES, CON SU `sed` PEGADO** (`D.35`):

    $ sed -n '51p;63p;69p' fuentes/gerber_emyth/cap_12.md
    THE INNOVATION Instead of asking, "Hi, may I help you?" try "Hi, have you been in here before?" The customer will respond with either a "yes" or a "no." In either case, you are then free to pursue the conversation.
    THE INNOVATION Again, for salespeople, a six-week test. For the first three weeks, wear a brown suit to work, a starched tan shirt, a brown tie (for men), and well-polished brown shoes. Make certain that all the elements of your suit are clean and well-pressed. For the following three weeks wear a navy blue suit, a good, starched white shirt, a tie with red in it (a pin or a scarf with red in it for women), and highly polished black shoes.
    THE INNOVATION The next time you want somebody to do something for you, touch him softly on the arm as you ask him to do it. You will be amazed to find that more people will respond positively when you touch them than when you do not.

| bloque | mi veredicto | por que |
|---|---|---|
| `L51` a `L57`, el saludo | **ES NODO** | el libro pone **las palabras exactas** (la pregunta nueva, la respuesta al `yes`, la respuesta al `no`) y **el requisito previo** (*you will have to have created a special new program*). Inventario de MEDIOS nombrados uno a uno, en imperativo al lector, **sin adjetivo de adecuacion en el sitio del criterio** |
| `L63` a `L65`, el traje azul | **ES NODO** | inventario de ETAPAS (*first three weeks*, *for the following three weeks*) **y** de OBJETOS DE TRABAJO (traje, camisa, corbata, zapatos, los ocho nombrados uno a uno), en imperativo (*wear*, *Make certain*), con entregable en el propio texto (*sales will go up during the second three-week period*) |
| `L69` a `L71`, tocar el brazo | **NO ES NODO** | es **un solo gesto**. `9` pide *una linea que al desplegarse pide siete pasos, y esos siete pasos se escriben*; esta se despliega en uno. **Nombrar codo, brazo o espalda no convierte un gesto en procedimiento**, y lo digo por el lado que no me conviene: es la que yo tampoco habria escrito |

**POR QUE SU RAZON NO SOSTIENE, y es una sola frase.** Escribio que los tres estan *presentados como
casos de clientes propios* (*our clients have found*). **Esa frase atestigua el RESULTADO, no la
instruccion.** La instruccion esta en segunda persona y en imperativo, dirigida al lector. **`P.17`
manda que gane la lectura de los pasos y no el argumento por formato o familia**, y `D.19` dice lo
mismo por el otro lado: **una senial dice donde mirar y ahi acaba su trabajo.**

**Y LA PRUEBA DE QUE NO ESTOY MOVIENDO LA VARA ES DE ESTA MISMA CASA Y DE ESTE MISMO LIBRO:**

    $ python -c "<lectura de cuarentena/gerber_emyth/unificar_color_forma_vestuario_modelo.json>"
    id    : unificar_color_forma_vestuario_modelo
    pasos : 8
    paso 6: "Cuenta con lo que midio Louis Cheskin, fundador del Color Research Institute, en el
             ensayo que el texto cita: un triangulo produjo bastante menos ventas que un circulo
             [...]"

**Ese nodo nacio en la vuelta `1` de este frente, de `cap_11`, de un pasaje que mezcla igual la
prescripcion con el ensayo de un tercero, y lo firmo la `ACTA G1`.** Si aquel es nodo, **el test de
seis semanas del traje azul lo es con mas margen**, porque no tiene ni el adjetivo de adecuacion que
aquel tuvo que salvar. **Aplico la vara escrita, no una mas ancha** (`9.1`, ultima clausula).

**LO QUE ESTO LE CUESTA AL CAPITULO:** `cap_12` **no esta minado**. Da **al menos `3`** candidatos y
se escribio `1`. Anotado como `d101`.

> **LO QUE DIGO A SU FAVOR, y lo digo porque es cierto:** **lo marco antes de saberlo**, nombro la
> pieza, nombro el bloque concreto (*el del traje azul en particular*) y **escribio la consecuencia
> exacta que yo acabo de sacar** (*ahi nace otro candidato*). `5.1`: una caida DENTRO del marcado
> dice que el extractor sabia donde estaba su duda. **Es la caida mejor senializada que he leido en
> este frente, y aun asi es una caida**, porque marcar la duda no es resolverla y la cifra que se
> publico es la otra.

### 3.2. Discutible `2`: los pasos `2` a `4` anclados al ejemplo. **SE SOSTIENE**

**Generalizar *cambiar las palabras del saludo* a *tu innovacion* habria sido escribir una
generalizacion que el parrafo no hace.** Eso es exactamente el corolario de `9.1` y la definicion de
PUENTE de `D.30`: **un paso que cierra un bucle que el libro deja abierto.** Eligio la fidelidad
contra su propia comodidad. **Su lectura es la correcta, y mi medida esta en `2`.**

### 3.3. Discutible `3`: `cap_12` `L21` y `D.37`. **SE SOSTIENE**, y lo adjudico citando

    $ sed -n '21p' fuentes/gerber_emyth/cap_12.md
    B uilding the Prototype of your business is a continuous process, a Business Development Process. Its foundation is three distinct yet thoroughly integrated activities through which your business can pursue its natural evolution. They are Innovation, Quantification, and Orchestration.

**Dice cuantas partes hay y las nombra, que es el supuesto de `D.37`. Y aun asi `D.37` no aplica, por
su propia letra:** ninguna de las tres existe como nodo, **la arista se declara EN EL ACTO DE
INSERTAR LA PARTE**, y esta vuelta no inserta (`MODO_INSERCION=cuarentena`, `D.39`). **Es la misma
figura que adjudique en la `ACTA G2` `4.1` para `cap_05` `L29`**, y no la vuelvo a razonar (`D.47`).
**Puntero anotado como `d104`**, gemelo de `d098`.

### 3.4. El vecino que levanto la aduana: **`SANO`, y lo leo paso contra paso**

    paso 3 del candidato : "Cuenta cuantas personas entraron por la puerta despues de cambiar las palabras."
    paso 4 del vecino    : "Cuenta como valor una palabra dicha en la puerta del negocio cuando un cliente se va."

**Uno cuenta personas para medir; el otro cuenta un gesto como valor.** El parecido que la senial ve
es lexico (*cuenta*, *puerta*, *palabra*) y no conceptual. **Ni CONTINUA ni REPITE: no hay madre ni
hija entre los dos** (`6.1`, y `D.19` delante: adjudico leyendo los pasos). **`SANO` confirmado.**

### 3.5. `cap_09` y `cap_10`: **FIRMO EL CERO DE LOS DOS**, y digo donde mire

**Los lei enteros.** Las superficies que mas se acercan, y que el no marco:

| pieza | por que la mire | mi veredicto |
|---|---|---|
| `cap_09` `R5`, `L145` a `L150` | las preguntas de ingeniero de Ray Kroc (*How could the components be constructed so that...*) | **NO ES NODO**: son preguntas retoricas en tercera persona sobre lo que **el** se pregunto |
| `cap_10` `R3`, `L42` a `L60` | los estandares de McDonald's nombrados uno a uno (siete minutos, diez minutos, el patron de los pepinillos, sesenta segundos) | **NO ES NODO**: estan en tercera persona y en pasado (*were left*, *were removed*, *were placed*). **Son los estandares de McDonald's, no una orden al lector** |
| `cap_12` `R6`, `L107` a `L129` | *Begin by quantifying everything*, seguido de once preguntas sobre los numeros del negocio | **NO ES NODO**: la lista **se cierra en `And so forth`**. Es la misma figura del `and so forth` que adjudique en la `ACTA G2` `4.4` (a): **una lista que el libro deja abierta no es su inventario propio**, y el paso que la cerrase lo escribiria el extractor |

> **Y ESA ES JUSTO LA PRUEBA DE QUE `3.1` NO ES UNA VARA MAS ANCHA APLICADA A CAPRICHO:** el mismo
> criterio que deja `cap_10` `R3` fuera (tercera persona, pasado, estandares de otro) y `cap_12` `R6`
> fuera (lista abierta) **mete `cap_12` `L51` y `L63` dentro** (segunda persona, imperativo,
> inventario cerrado). **El extractor trazo esa raya bien dos veces y la trazo mal una.**

---

## 4. LO QUE SE CAE, POR ESPECIE

### 4.1. `REPORTE`, **`1` caida que ACUMULA**: `cap_12` da al menos `3` candidatos y se publico `1`

**La cifra vive en la CABECERA y en cuatro TABLAS**, que son las sedes que hacen acumular (`5.2`):

    $ sed -n '57716p;57730p;57848p;57943p;58044p' docs/loop/REPORTE.md
    # FRENTE `gerber_emyth`, VUELTA 3: [...] `cap_09` Y `cap_10` MINADOS A CERO, Y `cap_12` DA UN CANDIDATO [...]
    | 3 | los candidatos que cada capitulo de [...] | **CERRADA**: `2` capitulos en cero y `1` candidato de `cap_12` [...] | `G3.4` |
    ### LA FRONTERA DE `cap_12` [...], **8 piezas y UN CANDIDATO EN `R5`**
    | `cap_12` | `1` | `6` | `0` | **0,00 por ciento** |
    | `3` | los candidatos que cada capitulo de [...] | **CERRADA en `G3.4`**: `2` capitulos en cero, `1` candidato de `cap_12` [...] |

**Y la celda que la sostiene, la clase de `R3`:**

    $ sed -n '57859p' docs/loop/REPORTE.md
    | `R3` | L22 a L83 | **1055** | la seccion Innovation entera [...] | **POSTURA y CASO** |

> **POR QUE ACUMULA Y NO SE PERDONA.** No es prosa de acompaniamiento: es **la cifra de la cosecha**,
> la que dice cuanto dio el capitulo, y viaja de la cabecera a la tabla de cierre pasando por la
> tabla que dimensiona el lote siguiente. **Un capitulo que se declara minado y no lo esta es el
> unico error de este bucle que no se descubre solo**, porque el capitulo ya no vuelve a mirarse. Y
> lo digo tambien por el otro lado, que es lo que la hace justa: **el candidato que SI escribio es
> bueno**, sus `6` pasos son transcripcion pura, su informe da `0 CAERIA` y su vecino es `SANO`.
> **Lo que falta no es calidad: es cantidad, y la cantidad era el trabajo de la vuelta.**

**DENTRO CONTRA FUERA DEL MARCADO** (`5.3`): **DENTRO.** Marco la pieza, marco el bloque y escribio
la consecuencia. **Es la unica de las tres caidas de este frente que estaba senializada.**

**`REPORTE` pasa de `2 de 3` a `3 de 3`. TOPE.**

### 4.2. `CIFRA PUBLICADA`, `CLASE` y `DATO MOVIDO`: **LAS TRES LIMPIAS**

| especie | lo que mido | de donde |
|---|---|---|
| **`CIFRA PUBLICADA`** | **CERO.** Esta vuelta **no escribio su propia racha**, que es justo lo que su encargo le prohibio tras la caida de la `ACTA G2` `3.2`; las cuatro correcciones declaradas de `1.6` son ciertas una a una; `d095` esta pagada de verdad | `1.6` |
| **`CLASE`** | **CERO.** `0` veredictos puestos, `bitacora/` intacta, `config/pares_mutuos.jsonl` en su unica linea | `1.2` |
| **`DATO MOVIDO`** | **CERO.** `0` ficheros de `dataset/`, `bitacora/`, `censos/` o `config/pares_mutuos.jsonl` movidos entre `07aa6f2` y `HEAD` | `1.2` |

**`CIFRA PUBLICADA` baja de `1 de 2` a `0 de 2` por tanda limpia** (`D.38.1`, y la correccion del
`16` sep: *limpia significa sin caidas de la especie que esa racha acumula*), **no por indulto mio.**

### 4.3. El registro de credito, escrito con su instrumento

    $ python forja.py credito --anotar --especie REPORTE --vuelta 3 --tanda "ACTA G3" --racha "3 de 3" --cae --cita "..."   (y cuatro mas)
    $ python forja.py credito
    CREDITO DE LA LINEA 'gerber_emyth' (D.48)
      registro: docs/loop/CREDITO_gerber_emyth.jsonl
      tandas: 4, en 12 suceso(s) de especie

      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA G3
      CIFRA PUBLICADA    0 de 2     ACTA G3
      CLASE              0 de 2     ACTA G3
      DATO MOVIDO        0 de 2     ACTA G3
      REPORTE            3 de 3     ACTA G3  TOPE

      CREDITO ROTO: REPORTE en su tope.
    $ python forja.py credito --revisar
    REPLAY VERDE en la linea 'gerber_emyth': las 10 tanda(s) vigilables suman lo que declaran.
    $ python forja.py credito --citas
    CITAS VERDES en la linea 'gerber_emyth': todas son referencia, ninguna trae una conclusion dentro (D.56).

**LAS TRES TANDAS QUE HACEN LA RACHA, Y SON SEGUIDAS SIN UNA LIMPIA EN MEDIO** (`D.38.1`):

| tanda | la caida de `REPORTE` | donde vivia |
|---|---|---|
| **`G1`** | cito una seccion `G1.10.e` que no existe | celda de tabla (`ACTA G1` `4.1`, y la parada del `17` sep seccion `1`) |
| **`G2`** | *los dos discutibles* donde `G2.7` tiene `3` | celda de tabla (`ACTA G2` `3.1`) |
| **`G3`** | `cap_12` da `1` candidato donde da al menos `3` | **CABECERA y cuatro TABLAS** (`4.1`) |

**La racha no la reinicia nadie mas que una tanda limpia o una decision escrita de Alexis, y ninguna
de las dos soy yo** (`5.4`).

### 4.4. Y una segunda de `REPORTE` que **registro y NO acumula**, porque vive en PROSA

    $ sed -n '58074,58075p' docs/loop/REPORTE.md
       El frente tiene ahora `cap_04` a `cap_08`, `cap_11` y `cap_12` minados:
       ocho de veintidos. El siguiente sin minar [...]

**La enumeracion son `7` capitulos, no `8`, y omite los dos que esa misma vuelta acababa de minar**
(`cap_09` y `cap_10`). **Lo tocado son `9`**, y lo cuento yo:

    $ python -c "<mi recuento sobre las 22 unidades>"
    total 22   cerradas 8   abiertas 1 (cap_12)   sin tocar 13

**Vive en la lista de propuestas de `G3.9`, que es prosa de acompaniamiento: registra y NO acumula**
(`5.2`). **Lo digo porque una caida que no acumula se sigue registrando con mi nombre encima**
(correccion del `16` sep a `5.4`), y porque **la cifra corregida es la que uso yo en `7` y en `8`**:
esa es la unica razon por la que importa.

---

## 5. MI PROPIA TANDA, Y SOY EL BENEFICIADO DE MI PROPIO JUICIO

**`AUDITOR` baja de `2 de 3` a `0 de 3`**, y digo con todas las letras que **el que se absuelve es el
mismo que juzga**, para que se pueda discutir:

| especie mia | lo que mido |
|---|---|
| **`REMEDIO ROTO`** | **NO.** El remedio que la `ACTA G2` dejo escrito era que `d095` dejase de estar vivo, y **esta pagado y medido en `1.6`**, con `4` de `4` celdas y la comprobacion en `0`. Es **sustancia de auditoria** (correccion declarada y comprobacion de cierre), no formato de artefacto |
| **`CIFRA PUBLICADA PROPIA`** | **NO.** Toda cifra de esta acta lleva su comando pegado encima, y las que no pude medir van dichas como tales |

**LO QUE NO ME CARGO, Y DIGO POR QUE:**

- **La relectura ciega sin veredicto que destapar** (`3`). En regimen ligero no hay veredicto, y lo
  declaro en vez de escribir *relectura ciega* sobre una fase que no existio.
- **El coste de mi turno.** El del extractor lo mido: **`8,9883078` USD**, leido de
  `docs/loop/ultimo_extractor.json`, **por debajo del tope de `10`** de `D.55`, asi que no hay
  desglose que publicar. **El mio no lo puedo medir**: lo escribe la tuberia del arnes en
  `docs/loop/ultimo_auditor.json` cuando mi turno ya termino. **Medida pendiente del arnes, no cifra
  mia sin medir.**

**LO QUE SI ME CARGO SIN QUE ACUMULE, porque no es de ninguna de mis dos especies pero es mio:** la
`ACTA G2`, que es de esta linea y es mia, pego el bloque de `gate` cortado en la segunda linea, igual
que este reporte. **Lo levanto contra mi tambien**, y lo anoto como `d103` en vez de cargarselo a
nadie.

---

## 6. LO QUE REGISTRO Y NO ABRE COLA (`D.55`, `D.56`)

**La cola de doctrina se queda en `11`.** Lo que sigue son medidas, anotadas y dejadas ahi.

### 6.1. Las cuatro anotaciones de deuda de esta acta

    $ python scripts/deuda.py --anotar --vuelta 3 [...]   (cuatro veces)
    ANOTADA d101: cap_12 R3 NO ESTA CERRADO: los bloques THE INNOVATION de L51 (el salud
    ANOTADA d102: TERCER EJEMPLAR DE LA FAMILIA d088/d096: la fila de gerber_emyth de do
    ANOTADA d103: EL BLOQUE PEGADO DE python forja.py gate SE CORTA EN LA SEGUNDA LINEA
    ANOTADA d104: PUNTERO D.37 DE cap_12: L21 nombra Innovation, Quantification y Orches

### 6.2. `d102`: la fila del tablero envejece dentro del propio turno

    $ git show HEAD -- docs/loop/TABLERO.jsonl | grep -c "candidatos_en_bandeja.: 10"
    2
    $ ls cuarentena/gerber_emyth/*.json | wc -l
    11

> **LECTURA:** la fila dice `10` y la bandeja tiene `11`. **No es cifra del extractor**: la escribe
> la guarda del tablero del arnes **al ABRIR la vuelta**
> (`[2026-09-21 08:40:29] tablero comprobado: la vuelta puede abrir`), cuando todavia eran `10`, y el
> unico campo que cambio en el commit es `commits_propios_de_su_rama`, de `23` a `25`. **Es la
> tercera vez que este registro publica un estado que ya no es el suyo** (`d088` en grove, `d096`
> aqui). **No lo toco**: `D.45` veda `src/` desde un frente.

### 6.3. `d103`: el bloque de `gate`, cortado en toda la casa

**El instrumento imprime tres lineas y los reportes y actas pegan dos**, sin marca de parcial. Lo
hace `G3.8.a` **y lo hace mi propia `ACTA G2` `1.1`**. **Convencion de la casa, no caida de nadie**, y
por eso va anotada y no cargada. La salida entera esta en `1.1` de esta acta.

---

## 7. LAS CONDICIONES DE PARADA, REPASADAS UNA A UNA (`AUDITOR_FORJA.md` `3`)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| **doctrina NUEVA necesaria** | **ninguna.** El discutible `1` lo adjudico con `EXTRACTOR.md` `9` y `9.1` **tal como estan escritos**, con un ejemplar de esta misma casa y este mismo libro delante (`3.1`); el `3`, con la letra de `D.37`; las glosas de fidelidad, con `D.30` y `15.4`. **No estrecho ni ensancho la vara** | **NO ES PARADA** |
| **contradiccion** con regla vigente o cifra publicada | **una, y se resuelve con las reglas de correccion existentes**: la clase de `cap_12` `R3`, que se corrige declarando sin borrar en la vuelta que retome el capitulo (`d101`) | **NO ES PARADA** |
| **decision de Alexis** | **ninguna que este turno necesite por si sola.** No borro contenido, no muevo umbrales, no cambio el alcance, no creo remotos, no fundo ramas | **NO ES PARADA** |
| **fallo tecnico repetido** | **ninguno.** Las seis guardas de `1.1` en VERDE hoy, y ninguna en rojo en la vuelta anterior | **NO ES PARADA** |
| **credito roto** | **SI, Y LO DICE EL INSTRUMENTO ANTES QUE YO** (`4.3`): `REPORTE` en **`3 de 3`**, su tope, **tres tandas seguidas sin una limpia en medio** (`5.4`, `D.38.1`) | **ES PARADA** |
| **campania consumada** | **no.** `9` de `22` unidades tocadas y solo `8` CERRADAS, porque `cap_12` queda abierto (`4.1`); `11` candidatos en bandeja, `0` insertados | **NO ES PARADA** |

> # **SE CUMPLE UNA: CREDITO ROTO. ESCRIBO `docs/loop/PARA_ALEXIS.md` Y DEJO `docs/loop/PROMPT_SIGUIENTE.md` VACIO.**

**Y NO ESCRIBO ESCALADA NI TAREA BLOQUEANTE** (`5.5`, `D.55`): la escalada se encarga **en el encargo
siguiente**, y no hay encargo siguiente que escribir. Lo que la vuelta que reanude tenga que hacer
esta en `docs/loop/DEUDA.jsonl` con su cita, que es donde `D.55` manda que viva.

---

## 8. LA COLA, COMO QUEDA AL CERRAR ESTA ACTA

| lo que queda | cifra que mido hoy | donde vive |
|---|---:|---|
| `cap_12` **sin cerrar**: candidatos que el capitulo da y no se escribieron | **`2`** como minimo (`L51` y `L63`) | `d101` |
| unidades del lote `9` sin tocar | **`13`** de `22` (`cap_01` a `cap_03`, y `cap_13` a `cap_22`), contadas por mi | `d094` y el orden del libro |
| candidatos en bandeja del lote `9` | **`11`**, con **`95`** pasos, **`0`** insertados | `D.39`, y la cosecha es del fundador |
| punteros `D.37` abiertos | **`2`** (`cap_05` `L29`, `cap_12` `L21`) | `d098` y `d104` |
| el nodo de la delegacion, si lo hay | **`1`** puntero, a `cap_18` `L345` a `L349` | `d099` |
| deuda pendiente de la linea | **`36`** pendientes, `32` pagadas | una vuelta de saneamiento, que en un frente hoy **no puede llegar** (`d097`) |
| preguntas de doctrina registradas y NO abiertas | **`2`** de la `ACTA G2`, **`0`** mias nuevas | `D.55` y `D.56` |

---

*`ACTA G3` cerrada. **CON PARADA**, y es la primera de este frente que no es por doctrina sino por la
metrica que el propio frente lleva. Mis ficheros de trabajo de este turno estan en `.g3aud/`, y cada
cifra de esta acta lleva su comando pegado encima: **se puede repetir entera sin mi.***

---

# ACTA `G4` DEL FRENTE `gerber_emyth`. VUELTA 4, lote 9, `cap_12` cerrado y `cap_13` y `cap_14` minados **EN CUARENTENA**, **CLASE EXTRACCION EN REGIMEN LIGERO**: **`d101` ESTA PAGADA ENTERA Y SE LA FIRMO PIEZA POR PIEZA; SUS TRES DISCUTIBLES SE SOSTIENEN LOS TRES; Y LO QUE SE CAE NO ES NINGUNA DE SUS CIFRAS, SINO DOS FRASES DE PROSA QUE NO MUEVEN LA RACHA**. Le recompongo **las tres fronteras al digito con codigo mio y sin su instrumento** (`4206`, `364`, `3695` palabras, residuo `0`, `0` solapes y `0` lineas sin cubrir en las tres), le cuento **los `25` pasos ficha a ficha** y **los leo los `25` contra su parrafo** (no por muestra): **`0` PUENTE, y le FIRMO las tres filas de `PASOS INVENTADOS` en `0,00` por ciento**. Su muestra con semilla `g4` me sale **identica byte a byte** (`diff` vacio), **le vuelvo a correr yo los cuatro informes de aduana** y **tres salen identicos al milesimo** y el cuarto gana dos vecinos **por el orden en que se corrieron, no por discrepancia**. Cinco guardas en VERDE, `TALLADO VERDE` sobre `167` tablas, y **`0` ficheros de dato movidos**. **Los tres discutibles marcados se sostienen los tres**, y examino **cuatro superficies mas que el NO marco**: las cuatro se sostienen y dos dejan deuda. **Caen dos afirmaciones, las dos en prosa de acompaniamiento y por tanto de las que NO acumulan** (`5.2`): que el registro de credito *no tiene ni una fila cuyo `tanda` no sea una `ACTA`* (la primera fila la tiene, y es justo la que la `ACTA G2` `3.2` cargo), y que `fingir_prototipo_cinco_mil_replicas` *entro con `4` de `6` partes* (no ha entrado: **`0` nodos de `gerber_emyth` en el grafo**). **La tanda es LIMPIA para las cinco rachas** (`D.38.1`): `REPORTE` `0 de 3`, `CIFRA PUBLICADA` `0 de 2`, `CLASE` `0 de 2`, `DATO MOVIDO` `0 de 2`, y **la mia `0 de 3`**. **Y publico dos cifras mias que nadie me pidio y que `D.55` me obliga a decir:** el turno del extractor costo **`16,8261033` USD** con el objetivo del ligero en `5`, y **el `98,69` por ciento de sus tokens fue relectura de contexto**; y **el tablero publica hoy `ultimo_capitulo = cap_19` para un libro cuyo ultimo capitulo minado es `cap_14`**, que es el **cuarto** ejemplar de la familia `d088`/`d096`/`d102` y **el primero que inventa un capitulo en vez de perderlo**. **NO HAY PARADA:** escribo `docs/loop/PROMPT_SIGUIENTE.md` y **no escribo `docs/loop/PARA_ALEXIS.md`**.

*Escrita el 21 sep 2026 por el auditor del bucle, sobre el commit `c710ee4` de la rama
`extraccion-gerber_emyth`, worktree `C:/Users/AlexDesk/Documents/forja-gerber_emyth`.
**Clase de la vuelta auditada: EXTRACCION en regimen ligero** (`D.58`), asi que **no hubo fase
ciega, ni sello, ni testigo**, y el arnes lo registro el mismo:*

    $ grep -n "SIN FASE CIEGA" docs/loop/loop.log | tail -1
    1100:[2026-09-21 11:37:12] VUELTA 1 : SIN FASE CIEGA (D.58: en cuarentena no hay cifra sobre el grafo que proteger)

*Acta corta por `D.58` y por `D.47`. Mis ficheros de trabajo estan en `.g4aud/`.*

---

## 0. **NO HAY HUECO DE ACTA**, y la herencia se declara antes que nada

**La `ACTA G3` cubre la vuelta `3` de este frente y yo cubro la `4`.** No hay vuelta sin auditar
entre las dos:

    $ grep -n "^# ACTA .G[0-9]" docs/loop/ACTA_AUDITOR.md | tail -2 | cut -c1-58
    45107:# ACTA `G2` DEL FRENTE `gerber_emyth`. VUELTA 2, lote 9
    45737:# ACTA `G3` DEL FRENTE `gerber_emyth`. VUELTA 3, lote 9

**ACTA ANTERIOR LEIDA:** `docs/loop/ACTA_AUDITOR.md`, `ACTA G3`, lineas `45737` a `46255`.

| | heredado | como queda hoy, medido |
|---|---|---|
| **HEREDADO 1** | **NO APLICA, y el motivo va escrito** (`D.40`): la `ACTA G3` cerro **con parada** y por eso **no dejo escrita ninguna tarea bloqueante ni ningun remedio**. No es que no me llegara: es que no existe | **NO APLICA** |

**LA SALIDA QUE LO SOSTIENE** (`D.40` ensanchada, 16 sep: un `NO APLICA` lleva su comando pegado):

    $ sed -n '45737,46260p' docs/loop/ACTA_AUDITOR.md | grep -n "TAREA BLOQUEANTE"
    458:**Y NO ESCRIBO ESCALADA NI TAREA BLOQUEANTE** (`5.5`, `D.55`): la escalada se encarga

**Y LO QUE SI HEREDE NO ES DE UN AUDITOR: ES DEL FUNDADOR.** El reinicio de la racha `REPORTE`
vino con una condicion mecanica (*la `TAREA 1` de la vuelta `4` ejecuta `d101` antes de abrir
`cap_13`*), y **la vuelta la cumplio en el orden literal**: `G4.2` es `cap_12`, `G4.3` es `cap_13` y
`cap_14`, y el reporte lo declara en su propio esqueleto. **Verificado en `1.5`.**

---

## 1. LO QUE VERIFIQUE CON MIS PROPIOS COMANDOS

### 1.1. Las cinco guardas, corridas por mi en esta vuelta

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python tests/test_aceptacion.py
      total: 350 pruebas, 0 fallos, 0 errores
    $ python scripts/tallar_reporte.py
    TALLADO VERDE: las 167 tabla(s) comprobables son las de su instrumento, celda a celda.

**LAS TRES LINEAS DE `gate`, NO DOS.** `d103` (`ACTA G3` `6.3`) dice que toda la casa pega ese
bloque cortado en la segunda linea. **Lo pego entero para no ser el cuarto**, y la tercera linea es
la que nombra las trece guardas que corrieron.

**EL BLOQUE DE `guiones` DEL REPORTE (`G4.4.a`) SE SOSTIENE, Y SU CAIDA TRANSITORIA TAMBIEN.** La
vuelta declaro que la primera corrida dio ROJO con `4` hallazgos (el guion largo del libro en ingles,
dentro de sus dos ficheros de cita pegada) y que la corrigio en el acto. **Lo verifico por el unico
sitio donde queda rastro, que es el fichero mismo:**

    $ python -c "import io,glob; print([f for f in glob.glob('.gerber_v4/cita_*.txt') if any(c in io.open(f,encoding='utf-8').read() for c in (chr(8212),chr(8211)))])"
    []

> **LECTURA:** ni uno de los cinco ficheros de cita lleva hoy guion largo ni medio, y el barrido de
> la casa sale verde sobre el arbol entero. **La correccion esta hecha; que la primera corrida fuese
> roja solo lo dice el reporte, y eso lo acepto como declaracion suya, no como medida mia.**

### 1.2. El estado, contado por mi y no copiado

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
    $ ls cuarentena/gerber_emyth/*.json | wc -l
    15

| pieza | lo que publica `G4.1` y `G4.5.b` | lo que mido yo | |
|---|---:|---:|---|
| nodos en el grafo | `346` | **346** | **al digito** |
| veredictos escritos | `740` | **740** | **al digito** |
| candidatos en bandeja al cerrar | `15` | **15** | **al digito** |
| pasos en esa bandeja al cerrar | `120` | **120** | **al digito** |
| unidades de `gerber_emyth` | `22` | **22** | **al digito** |
| palabras de cuerpo del libro | `62648` | **62648** | **al digito** |
| ficheros de dato movidos | `0` | **0** | **al digito** |

Los `120` pasos los cuento ficha a ficha, no de su tabla:

    $ python -c "import json,glob; print(sum(len(json.load(open(f,encoding='utf-8'))['pasos_accionables']) for f in glob.glob('cuarentena/gerber_emyth/*.json')))"
    120

Y las `62648` palabras salen de mi propio recorrido de los `22` ficheros, derivando el arranque del
cuerpo de la segunda linea de cierre de cada cabecera, **sin tocar su instrumento**.

**`DATO MOVIDO` medido por mi, y sale en cero:**

    $ git diff --name-only 3991806..HEAD -- dataset/ bitacora/ censos/ config/pares_mutuos.jsonl
    (vacio)

Lo unico que la vuelta movio es `cuarentena/gerber_emyth/` (cuatro ficheros nuevos), `docs/loop/`
(reporte, deuda, tabla de cierre y el archivo de la tabla anterior) y su carpeta de evidencia
`.gerber_v4/`. **Es bandeja, no grafo.**

### 1.3. Las tres fronteras, recompuestas por mi SIN su instrumento

**No me basta con volver a correr su `frontera.py`: eso comprueba que el fichero de piezas no
cambio, no que la frontera cierre.** Cuento el cuerpo con `sed` y `wc`, que es codigo que no es
suyo:

    $ sed -n '8,293p' fuentes/gerber_emyth/cap_12.md | wc -w
    4206
    $ sed -n '8,59p'  fuentes/gerber_emyth/cap_13.md | wc -w
    364
    $ sed -n '8,217p' fuentes/gerber_emyth/cap_14.md | wc -w
    3695

| capitulo | piezas | cuerpo | suma de piezas | residuo | solapes | sin cubrir |
|---|---:|---:|---:|---:|---:|---:|
| `cap_12` (fina, `R3` abierto en nueve) | `15` | **4206** | **4206** | **0** | **0** | **0** |
| `cap_13` | `4` | **364** | **364** | **0** | **0** | **0** |
| `cap_14` | `7` | **3695** | **3695** | **0** | **0** | **0** |

**Y SU PROPIO INSTRUMENTO ME REPRODUCE FILA A FILA** al volver a correrlo sobre sus ficheros de
piezas: las tres tablas salen iguales, y `TALLADO VERDE` (`1.1`) dice ademas que las tablas pegadas
en el reporte son celda a celda las de esa salida.

**LA FRONTERA FINA NO PERDIO NI GANO UNA PALABRA:** `4206` en la vuelta `3` con `8` piezas y `4206`
en la vuelta `4` con `15`. **Abrir `R3` en nueve piezas no movio el cuerpo, que es exactamente lo
que `d101` pedia comprobar.**

### 1.4. La muestra de fidelidad con semilla `g4`: **identica byte a byte**

    $ python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_13,cap_14 --semilla g4 > .g4aud/mf.txt
    $ diff .g4aud/mf.txt .gerber_v4/muestra_fidelidad.txt
    (vacio)

**La semilla reparte `cap_13` a relectura ENTERA y `cap_14` por muestra**, y la muestra de `cap_14`
son sus `9` pasos porque el capitulo no llega al techo de `15`. **Me sale la misma lista, en el
mismo orden, con los mismos cortes de columna.** Una muestra que se reproduce es una muestra.

**Y LA DISCREPANCIA QUE EL PROPIO REPORTE DECLARA (`G4.3.e`) SE SOSTIENE:** que la primera corrida
llevase `cap_12,cap_13,cap_14` y la buena `cap_13,cap_14` **no cambia el reparto**, porque el
instrumento es determinista sobre el nombre del capitulo. **Lo compruebo corriendo yo las dos:**

    $ python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_12,cap_13,cap_14 --semilla g4 | grep "RELEIDO ENTERO"
      RELEIDO ENTERO : cap_13

> **LECTURA:** declaro una corrida mia, no su palabra. **El alcance del comando cambio y el reparto
> no**, asi que la correccion que declaro es exacta y no absuelve nada que hubiera que absolver.

### 1.5. La condicion del reinicio, verificada en el orden en que se le pidio

**`d101` antes de `cap_13`, y por sus tres piezas.** Lo compruebo por lo que quedo escrito:

    $ python scripts/deuda.py | tail -2
      pendientes: 35    pagadas: 33
    $ grep -o '"id": "d101", "linea": "gerber_emyth", "tipo": "pago", "vuelta": "4"' docs/loop/DEUDA.jsonl
    "id": "d101", "linea": "gerber_emyth", "tipo": "pago", "vuelta": "4"

**`36` pendientes y `32` pagadas publicaba la `ACTA G3` `8`; hoy son `35` y `33`.** Una menos
pendiente, una mas pagada, y la fila de pago nombra `d101` y la vuelta `4`. **Al digito.**

Las tres piezas, una a una:

| pieza de `d101` | lo que pedia | lo que mido |
|---|---|---|
| `cap_12` `L51` | nace candidato | **`cuarentena/gerber_emyth/cambiar_saludo_cliente_dos_ramas.json`, `4` pasos** |
| `cap_12` `L63` | nace candidato | **`cuarentena/gerber_emyth/probar_traje_azul_seis_semanas.json`, `2` pasos** |
| `cap_12` `L69` | se declara NO-NODO con su motivo | **declarado en `G4.2.d` con su lectura contra el texto, no copiada del acta** |

**Y LA CORRECCION DE LA CLASE DE `R3` (`G4.2.f`) SE SOSTIENE, Y SU FORMA TAMBIEN.** El encargo pedia
*tachar y escribir al lado*; la vuelta **no tacho la celda** y escribio la correccion declarada
debajo, citando `D.41`. **Le doy la razon, y no es un favor:** la letra de `D.41` dice **"SE CORRIGE
REGENERANDO, NUNCA TECLEANDO LA CELDA BUENA"**, y esa tabla es TALLADA contra
`.gerber_v3/frontera_cap12.txt`. Tachar dentro de ella habria hecho que la tabla dejase de ser la de
su instrumento, **y el tallado aborta el commit** (`D.41`, y `1.1` mide que hoy esta verde sobre
`167` tablas). Las cuatro celdas de `d095` que el encargo pone de ejemplo **no estaban en tablas
talladas**: eran celdas de tablas de parada y de esqueleto. **Es otro caso, y la vuelta eligio bien
y lo dijo.**

### 1.6. Los cuatro informes de aduana, vueltos a correr por mi

    $ for n in <los cuatro candidatos>; do python forja.py informe cuarentena/gerber_emyth/$n.json; done > .g4aud/informes.txt

| candidato | lo que pego el reporte | lo que me sale hoy | |
|---|---|---|---|
| `cambiar_saludo_cliente_dos_ramas` | poblacion `452`, `1` vecino, `0 CAERIA` | poblacion `455`, **`3`** vecinos, **`0 CAERIA`** | **el vecino que pego, al milesimo** |
| `probar_traje_azul_seis_semanas` | poblacion `453`, `3` vecinos, `0 CAERIA` | poblacion `455`, `3` vecinos, `0 CAERIA` | **IDENTICO al milesimo** |
| `recorrer_siete_pasos_programa_desarrollo_negocio` | poblacion `454`, `0` vecinos, `1 ENTRARIA` | poblacion `455`, `0` vecinos, `1 ENTRARIA` | **IDENTICO** |
| `responder_8_preguntas_construir_primary_aim` | poblacion `455`, `1` vecino, `0 CAERIA` | poblacion `455`, `1` vecino, `0 CAERIA` | **IDENTICO al milesimo** |

**`0 CAERIA` y `0 CHOCAN` en los cuatro, que es lo que la vuelta afirma.** Las cinco cifras de
similitud que el reporte pego me salen las cinco al milesimo (`0.375`, `0.489`, `0.430`, `0.362` y
`0.375`), con sus `familia_id` en `0.000` y sus `paso_contra_nodo` en `0.325`, `0.262`, `0.366`,
`0.315` y `0.426`, **y con el mismo par de pasos nombrado en cada una.**

**LA POBLACION ME CUADRA CON LA SUYA, Y LA MIDO** (`D.38.5`, la aduana mide la misma poblacion que
yo):

    $ python -c "import os,glob; print(sum(len(glob.glob('cuarentena/%s/*.json'%d)) for d in os.listdir('cuarentena') if not d.startswith('_')))"
    272

> **LECTURA:** `272` menos los `163` de `cuarentena/ensayo_referencia_163/`, que es banco de pruebas
> y no bandeja de campania, da **`109`**, que es exactamente lo que el informe dice que espera en
> bandejas, y `346` mas `109` son `455`, su poblacion. **Cuadra, y cuadra por la via de `D.38.5`:
> ya medimos lo mismo.**

### 1.7. La diferencia de `cambiar_saludo` NO es discrepancia: es el orden, y tiene consecuencia

**Su informe se corrio en el acto** (`EXTRACTOR.md` 16), es decir **el primero de los cuatro**,
cuando los otros tres todavia no existian. Por eso su bloque publica un vecino y hoy salen tres.
**Las dos vecindades nuevas son candidatos escritos DESPUES que el.**

| vecindad que su informe no pudo ver | similitud | quien la leyo |
|---|---:|---|
| `probar_traje_azul_seis_semanas` | `0.487` | **SI, desde el otro lado**: `G4.2.c` la lee a `0.489` y la adjudica `SANO, hermanos` |
| `responder_8_preguntas_construir_primary_aim` | `0.350` | **NADIE. La leo yo en `3.5`** |

> **LECTURA, y es la util de este apartado:** correr la aduana en el acto **garantiza que el ultimo
> candidato de una vuelta ve a todos y que el primero no ve a ninguno.** No es una caida de nadie y
> no la cargo: **el reporte pego lo que su instrumento dijo en ese instante, que es justo lo que
> `D.38.3` manda.** Pero deja un hueco real, y esta vuelta lo tuvo: **un par por leer.** Va anotado
> en `6.2` y encargado como el ultimo paso de la vuelta `5`.

---

## 2. `PASOS INVENTADOS POR CAPITULO`, QUE ES CIFRA MIA Y LA FIRMO ENTERA (seccion `8`)

**No la copio: cuento yo los pasos y leo yo los parrafos** (`8.3`).

    $ python -c "import json;[print(n, len(json.load(open('cuarentena/gerber_emyth/%s.json'%n,encoding='utf-8'))['pasos_accionables'])) for n in NOMBRES]"
    cambiar_saludo_cliente_dos_ramas                   4
    probar_traje_azul_seis_semanas                     2
    recorrer_siete_pasos_programa_desarrollo_negocio  10
    responder_8_preguntas_construir_primary_aim        9

| capitulo | candidatos nuevos | pasos escritos, contados por mi | PUENTE que yo encuentro | pasos inventados |
|---|---:|---:|---:|---|
| `cap_12` | `2` | **6** | **0** | **0,00 por ciento** |
| `cap_13` | `1` | **10** | **0** | **0,00 por ciento** |
| `cap_14` | `1` | **9** | **0** | **0,00 por ciento** |
| **la vuelta 4 entera** | **4** | **25** | **0** | **0,00 por ciento** |

**LA FIRMO SOBRE `25` PASOS Y NO SOBRE `9`**, porque no me quede en la muestra: **lei los `25`
contra su parrafo del libro**, que es el `100` por ciento y no el reparto que la semilla pedia.
`8.3` punto `2` avisa de que *el error que esta metrica invita a cometer es marcar un puente como
transcripcion*, y el unico modo de cazarlo es leer.

**Y LA FILA DECIDE EL VOLUMEN** (`8.2`): el peor capitulo es `0,00`, asi que **el volumen no baja**,
y lo que lo limita es el techo del ligero (tres capitulos, `D.58`), no la metrica.

### 2.1. Las dos salvedades que declaro, y ninguna es PUENTE

> **LECTURA 1, `probar_traje_azul_seis_semanas`:** sus dos pasos empiezan por *haz que el vendedor
> vista*, y el libro escribe *wear a brown suit to work* en segunda persona al propio vendedor. **El
> destinatario cambia de registro**, del vendedor al duenio del negocio. **No es PUENTE** (`D.30`:
> puente es lo que el extractor pone y el libro no dice) porque el libro nombra al destinatario en
> la misma frase (*Again, for salespeople*) y el capitulo entero habla al duenio. **Las ocho prendas
> y las dos etapas de tres semanas estan las diez en el texto, una a una.**

> **LECTURA 2, `recorrer_siete_pasos_programa_desarrollo_negocio`:** sus pasos `1` y `2` son
> **definicionales** (*Entiende tu Business Development Program como...*, *Usalo tambien como el
> vehiculo...*), no ejecutables. **Tampoco es PUENTE**: las dos frases estan en `L39` y `L41` con
> ese contenido. Es lo que una **cabeza de serie numerada** hace (`9.1`, `SERIE NUMERADA`), y los
> siete pasos que si son la serie (`P4` a `P10`) son los siete titulos exactos. **Lo declaro porque
> la proporcion importa: `3` de sus `10` pasos son marco y `7` son la serie.**

---

## 3. LA RELECTURA: **SUS TRES DISCUTIBLES SE SOSTIENEN LOS TRES**

**No hubo fase ciega ni veredicto que destapar** (`D.58`, medido en la cabecera de esta acta), asi
que **no escribo `relectura ciega` sobre una fase que no existio**, igual que la `ACTA G3`. Lo que
si hago, y es lo que `5.1` protege: **empiezo por los que el marco antes de saber si acertaba, y en
cada uno leo primero el texto del libro y despues su razon.**

### 3.1. Discutible `1`: `cap_12` `L69`, tocar el brazo, NO-NODO. **SE SOSTIENE**

    $ sed -n '69p;71p' fuentes/gerber_emyth/cap_12.md
    THE INNOVATION The next time you want somebody to do something for you, touch him softly on the arm as you ask him to do it. [...]
    Again, to apply this to your business, you or your salespeople should make a point of touching each customer on the elbow, arm, or back some time during the sales process. [...]

**MI LECTURA CON `9.1` DELANTE, antes de mirar la suya.** La restriccion `1` pide inventario de
**MEDIOS, ETAPAS u OBJETOS DE TRABAJO nombrados uno a uno**. Aqui hay **un solo gesto continuo**
(tocar al pedir algo) y **una sola aplicacion** del mismo gesto. Las tres zonas de `L71` van unidas
por **`or`**: *elbow, arm, **or** back*. **Una disyuncion de tres sitios para el mismo gesto es un
medio escrito de tres maneras, no tres medios.** Y la columna `NO es un nodo` nombra este caso con
su nombre: **una advertencia es linea, no procedimiento**.

**EL CONTRASTE ESTA DENTRO DEL MISMO `R3`, y es lo que lo cierra:** `L51` da **las palabras exactas
mas dos ramas escritas mas una condicion previa**; `L63` da **dos etapas de tres semanas con cuatro
prendas cada una**. `L69` no tiene ni etapas ni objetos: **se ejecuta en un gesto.**

**Y ADEMAS LA VUELTA HIZO LO CORRECTO CON LA FORMA**, que es la mitad que se pierde siempre: **lo
escribio**. `d101` pedia declarar el NO-NODO, y si solo se escriben los dos que nacen, la vuelta
siguiente vuelve a discutir `L69` desde cero.

### 3.2. Discutible `2`: el paso `4` de `cambiar_saludo`. **SE SOSTIENE, y son `4` pasos**

    $ sed -n '57p' fuentes/gerber_emyth/cap_12.md
    Of course, you will have to have created a special new program to talk about in either case. But that is the easy part.
      (el fichero lo trae con apostrofo tipografico: "you'll" y "that's")

**MI LECTURA.** El libro escribe una **obligacion modal explicita** (*you'll have to have created*)
sobre un **objeto de trabajo nombrado** (*a special new program*) del que **dependen las dos ramas**
(*in either case*). Transcribirla como paso de condicion previa **no anade nada**: el corolario de
`9.1` prohibe escribir el destinatario, el responsable o el periodo que el libro deja abiertos, **y
ninguno de los tres aparece en ese paso**.

**SU ARGUMENTO EN CONTRA MIDE EL REGISTRO, NO EL INVENTARIO.** Que la frase venga como aparte
(*Of course... But that's the easy part*) dice **como suena**, no **que manda**. `9.1` decide por
inventario, no por tono. **Y lo que si era tono se quedo fuera**: *But that's the easy part* no se
transcribio, y hace bien, porque es valoracion y no paso.

### 3.3. Discutible `3`: la suavizacion de `responder_8_preguntas`. **SE SOSTIENE**

    $ sed -n '117p;135p' fuentes/gerber_emyth/cap_14.md
    So before you start your business, or before you return to it tomorrow, ask yourself the following questions:
    These are just a few of the questions you might ask yourself in the creation of your Primary Aim.

**MI LECTURA CON LA RESTRICCION `2` DELANTE.** La restriccion `2` tumba cuando **el adjetivo de
adecuacion esta EN EL SITIO DEL CRITERIO**, y sus ejemplares lo dicen: *medidas apropiadas*,
*politicas adecuadas*, *requisitos razonables*. **En los tres, el libro pone el mandato y NO nombra
los objetos**, asi que quien los nombre es el extractor. **Aqui pasa lo contrario:** el mandato es
*ask yourself **the following** questions*, un puntero cerrado, y detras vienen **ocho vinetas, cada
una con su objeto propio**. La frase de cierre dice **cuantas preguntas existen en el mundo**, no
**cual es el criterio de adecuacion de estas ocho**. **No es un adjetivo de adecuacion: es un aviso
de no exhaustividad sobre un conjunto que ya esta escrito.**

**Y LA VUELTA SE FRENO DONDE DEBIA:** *these are just a few* **no se transcribio como paso noveno**,
y eso es exactamente lo que habria sido PUENTE.

> ### **LECTURA MIA, MARCADA, SOBRE LA TENSION QUE ESTE DISCUTIBLE ABRE Y QUE EL REPORTE NO CRUZO**
>
> `cap_12` `R6` (`L96` a `L147`) hace **el mismo movimiento** y esta clasificada **POSTURA**:
>
>     $ sed -n '107p;111,113p;131p' fuentes/gerber_emyth/cap_12.md
>     Begin by quantifying everything related to how you do business.
>     How many customers do you see in person each day?
>     How many in the morning?
>     In the afternoon?
>     And so forth.
>
> **Diez preguntas de conteo nombradas una a una, bajo un imperativo, con un aviso de no
> exhaustividad detras: la misma figura que `cap_14` `R5`.**
>
> **LAS DOS CLASIFICACIONES SOLO SON COMPATIBLES SI LA LINEA QUE SEPARA ES EL PUNTERO, NO LA
> SUAVIZACION.** *the following questions* apunta a **un conjunto cerrado y escrito**; *quantifying
> **everything** ... and so forth* es **un universal abierto del que las preguntas son ejemplos**, y
> el propio libro lo remata dos lineas despues: *You cannot ask too many questions about the
> numbers*. **Sostengo las dos con ese criterio, que es texto del libro y no seniial** (`D.19`: una
> discrepancia nunca se adjudica citando una seniial).
>
> **LO DEJO ESCRITO Y MARCADO PARA QUE EL SIGUIENTE LECTOR PUEDA TUMBARME:** si la linea fuera la
> suavizacion, caeria `responder_8_preguntas`; si fuera la mera enumeracion, `cap_12` `R6` tendria
> que dar candidato. **No estrecho ni ensancho la vara** (`9.1`, y `6.3` de mi protocolo): leo el
> puntero, que ya estaba en los dos textos.
>
> **Y AYUDA QUE `R6` NO SE QUEDA SIN NODO:** `R5` (`L95`) ya dio
> `cuantificar_impacto_innovacion_6_pasos` en la vuelta `3`, que es el procedimiento cerrado de
> Quantification con sus seis pasos numerados. **Lo que `R6` aniade es ilustracion de ese mismo
> metodo, no un metodo nuevo.**

### 3.4. **FUERA DEL MARCADO: cuatro superficies que el NO marco y que examino yo**

*Es la cifra que `5.1` pide de verdad: una caida DENTRO del marcado dice que sabia donde estaba su
duda; una FUERA dice que no la vio venir.*

| # | superficie | mi lectura | |
|---:|---|---|---|
| `a` | **`cap_14` `R2`, `L27`**: *you must ask yourself **these** questions* mas cuatro preguntas | **SE SOSTIENE la decision, y matizo la razon**: ver abajo | **sin caida, deja deuda** |
| `b` | **`cap_12` `R6`**, `L96` a `L147` | **SE SOSTIENE** por el criterio del puntero (`3.3`) | **sin caida, deja deuda** |
| `c` | **`cap_13` `R2`**, `L21` a `L38`: la cadena de *Imagine yourself...* | **SE SOSTIENE**: son escenas del resultado, fines y no medios (restriccion `1`), y su objeto **ya esta en casa dos veces** | **sin caida** |
| `d` | **`cap_14` `R4` y `R6`**, `L99` a `L116` y `L137` a `L146` | **SE SOSTIENEN**: lei las dos enteras y no hay inventario, ni vinetas, ni imperativo con objetos | **sin caida** |

**SOBRE `a`, y es el unico donde no firmo la razon escrita aunque firme la decision.**

    $ sed -n '27p' fuentes/gerber_emyth/cap_14.md
    But before you can determine what that role will be, you must ask yourself these questions: What do I value most? What kind of life do I want? What do I want my life to look like, to feel like? Who do I wish to be?

El reporte deja `L27` dentro de `R2` como **POSTURA**, citando `P.19`. **Bajo mi propio criterio del
puntero (`3.3`), *these questions* tambien es un puntero cerrado**, asi que la razon por la que `L27`
no es nodo **no puede ser que sea postura**: es que **su objeto ya esta en casa en `L117`**, que es
el mismo cuestionario del mismo Primary Aim desplegado a ocho, y separarlo fabricaria el gemelo de
su propio donante.

**NO LO CARGO COMO CAIDA, y digo por que para que se pueda discutir:** la fila de la tabla
**describe las cuatro preguntas con su contenido** y no las esconde; la decision **esta declarada en
parrafo aparte con su regla**; el resultado (un solo nodo del cuestionario) **es el correcto**; y la
pieza `R2` entera son `115` palabras cuyo registro dominante **si** es el argumento de apertura.
**Clasificar una pieza por su registro dominante, declarando lo que lleva dentro, no es una celda
falsa.** Va a deuda para que la vuelta que inserte relea `L27` contra `L117` con las dos delante.

**SOBRE `c`, la confirmacion que el reporte no nombro y que refuerza su propia decision:** el objeto
de `cap_13` `R2` (imaginar tu negocio como prototipo que alguien compra) **ya vive en la bandeja dos
veces**, en `hacer_trabajo_futuro_imaginar_negocio` (`cap_04`) y en
`fingir_prototipo_cinco_mil_replicas` (`cap_11`). **Llego al sitio correcto; el gemelo que evito no
lo nombro.**

### 3.5. **El par que nadie leyo, y lo leo yo** (`1.7`)

`cambiar_saludo_cliente_dos_ramas` contra `responder_8_preguntas_construir_primary_aim`,
`similitud_texto 0.350`, paso `3` contra paso `8`:

| lado | el paso |
|---|---|
| **paso 3 de `cambiar_saludo`** | *Si el cliente responde que no, dile exactamente: Great, we have created a special new program for people who have not shopped here before...* |
| **paso 8 de `responder_8_preguntas`** | *Que me gustaria aprender especificamente durante mi vida: espiritual, fisica, financiera, tecnica e intelectualmente, y tambien sobre las relaciones.* |

**Ni un objeto compartido.** Uno es una rama de guion de venta al detalle; el otro es una pregunta
sobre el aprendizaje de la propia vida. El parecido es de **longitud y de enumeracion**, que es lo
que la seniial mide. **VEREDICTO DE LECTURA: `SANO`**, y no se escribe en `bitacora/VEREDICTOS.jsonl`
porque esta vuelta no inserta (`D.39`).

---

## 4. LO QUE SE CAE, POR ESPECIE

### 4.1. `CLASE`: **LIMPIA, y por sede**

**Cero veredictos escritos y cero ficheros de dato movidos** (`1.2`). `5.2` dice que **la sede decide
la especie**, y la sede de `CLASE` es `bitacora/VEREDICTOS.jsonl`, `config/pares_mutuos.jsonl` y el
dataset. **Esta vuelta no escribio en ninguna de las tres.** `0 de 2`.

### 4.2. `DATO MOVIDO`: **LIMPIA**

`git diff --name-only 3991806..HEAD -- dataset/ bitacora/ censos/ config/pares_mutuos.jsonl` sale
vacio (`1.2`). `0 de 2`.

### 4.3. `CIFRA PUBLICADA`: **LIMPIA**, y `D.61` repasada por mi

`D.61` (nueva, del banco): **un discutible publicado se ejecuta o se cierra en la misma vuelta**, y
un *ahi nace otro candidato* publicado y no ejecutado **es `CIFRA PUBLICADA`, tope `2`**.

| discutible de la vuelta `4` | ejecutado o cerrado |
|---|---|
| `1` (`L69` NO-NODO) | **CERRADO con su lectura contra el texto** (`G4.2.d`), y verificado por mi en `3.1` |
| `2` (paso `4` de `cambiar_saludo`) | **el paso esta escrito**; la duda es sobre como se lee un paso ya escrito, no sobre un candidato por nacer |
| `3` (la suavizacion de `cap_14`) | **el candidato ya nacio**; la duda es sobre la fuerza de un inventario ya transcrito |

**NINGUNO QUEDA ABIERTO EN LA FORMA QUE `D.61` CASTIGA.** Y lo verifico contra la definicion, no
contra su tabla: **la figura que `D.61` persigue es una promesa de trabajo futuro**, y los tres son
dudas de lectura sobre material que ya existe en la bandeja. **`0 de 2`.**

**Y LAS OTRAS SEDES DURADERAS QUE LA VUELTA SI TOCO, MEDIDAS:** `docs/loop/DEUDA.jsonl` (la fila de
pago de `d101`, verificada al digito en `1.5`) y `docs/loop/TABLA_DE_CIERRE.txt` (regenerada por su
instrumento, y `TALLADO VERDE` la cubre). **Ninguna cifra falsa en ninguna de las dos.**

### 4.4. `REPORTE`: **DOS CAIDAS, y las dos de las que NO acumulan**

*`5.2`: la especie `REPORTE` **acumula solo si la cifra vive en TABLA, CABECERA o CONCLUSION; en
lista de rutas o prosa de acompaniamiento, NO acumula**.*

**CAIDA `1`. `G4.6.b`, parrafo en cursiva:** *`CREDITO_gerber_emyth.jsonl` no tiene ni una fila cuyo
`tanda` no sea una `ACTA` del auditor.*

    $ head -1 docs/loop/CREDITO_gerber_emyth.jsonl
    {"cita": "REPORTE.md seccion G2", "especie": "REPORTE", "linea": "gerber_emyth", "racha": "1 de 3", "tanda": "G2", "tipo": "tanda", "vuelta": 2}

> **LECTURA:** la primera fila del fichero tiene `tanda` `"G2"`, que **no es una `ACTA`**, y su
> `cita` apunta a `REPORTE.md`. **Es exactamente la fila que la `ACTA G2` `3.2` cargo como
> `CIFRA PUBLICADA`**, y sigue ahi porque el registro **se aniade y no se reescribe**. La frase es
> falsa, y ademas la fila que la desmiente **es la unica prueba escrita de que un extractor de esta
> linea si se escribio su propia tanda alguna vez.**

**PERO LA CONCLUSION DE LA SECCION ES CORRECTA Y SE LA FIRMO**, y por eso esto es una caida de
premisa y no de decision: **no escribir su propia fila de credito es lo que la casa manda**, y lo
manda **por el precedente de esa misma fila**. La vuelta hizo lo correcto **con el argumento
equivocado a mano**, que es la forma de acierto que conviene decir en voz alta.

**CAIDA `2`. `G4.3.a`, parrafo de acompaniamiento:** *Mismo patron que
`fingir_prototipo_cinco_mil_replicas` (**entro** con `4` de `6` partes)*.

    $ grep -c '"id": "fingir_prototipo_cinco_mil_replicas"' dataset/nodos.jsonl
    0
    $ python -c "import json; print(sum(1 for l in open('dataset/nodos.jsonl',encoding='utf-8') for f in json.loads(l).get('fuentes',[]) if f.get('clave')=='gerber_emyth'))"
    0

> **LECTURA:** `fingir_prototipo_cinco_mil_replicas` **no ha entrado**: esta en
> `cuarentena/gerber_emyth/`, y **`0` nodos de `gerber_emyth` viven en el grafo**. Su
> `nodos_siguientes` esta **vacio**, asi que tampoco lleva `4` aristas de nada. Lo que el candidato
> si dice de si mismo, y es cierto, es que **nacio con cuatro de las seis reglas escritas** y que las
> aristas *se cablean el dia de la insercion*. **La sustancia del precedente que invoca es buena; el
> verbo `entro` es falso.**

**Y LA PRIMERA MITAD DE ESE MISMO PARRAFO ES CIERTA Y LA COMPRUEBO:** *hoy `0` de `7` partes existen
como nodo* sale al digito del mismo comando.

**LO QUE VERIFIQUE Y LE SALE BIEN EN ESE MISMO SITIO**, porque una caida al lado de un acierto no
tinie el acierto: la correspondencia de los siete pasos con sus capitulos, que era la afirmacion
cara de `G4.3.a`, **me sale exacta**:

    $ for c in 14 15 16 17 18 19; do grep -m1 "^titulo_textual:" fuentes/gerber_emyth/cap_$c.md; done
    titulo_textual: Your Primary Aim
    titulo_textual: Your Strategic Objective
    titulo_textual: Your Organizational Strategy
    titulo_textual: Your Management Strategy
    titulo_textual: Your People Strategy
    titulo_textual: Your Systems Strategy
    $ grep -m1 "^titulo_textual:" fuentes/gerber_emyth_cap17_reservado/cap_17.md
    titulo_textual: Your Marketing Strategy

> **LECTURA:** los siete titulos de `L43` a `L57` son **los titulos exactos de siete capitulos
> completos**, seis en `fuentes/gerber_emyth/` y el septimo (*Your Marketing Strategy*) apartado en
> `fuentes/gerber_emyth_cap17_reservado/`. **`R3` de `cap_13` es cabeza de `SERIE NUMERADA` con todas
> las letras**, y `D.37` y no `D.29` es la lectura correcta. **Se lo firmo entero.**

### 4.5. **Y POR TANTO: LA TANDA ES LIMPIA PARA LAS CINCO RACHAS**

**`D.38.1` y la correccion del 16 sep son explicitas:** *`LIMPIA` significa **sin caidas de la
especie que esa racha acumula**. Una tanda con caidas solo de las que **no** acumulan reinicia la
racha igual.* Las dos caidas de `4.4` viven en **prosa de acompaniamiento**, no en tabla, ni en
cabecera, ni en conclusion.

| especie | racha al abrir | caidas que acumulan en mi tanda | racha al cerrar |
|---|---|---:|---|
| `REPORTE` | `0 de 3` | **0** (dos caidas, ninguna acumula) | **`0 de 3`** |
| `CIFRA PUBLICADA` | `0 de 2` | **0** | **`0 de 2`** |
| `CLASE` | `0 de 2` | **0** | **`0 de 2`** |
| `DATO MOVIDO` | `0 de 2` | **0** | **`0 de 2`** |
| `AUDITOR` (mia) | `0 de 3` | **0** (ver `5`) | **`0 de 3`** |

**LAS DOS CAIDAS SE REGISTRAN CON SU NOMBRE IGUAL**, que es lo que las hace utiles: lo unico que
dejan de hacer es mover el contador.

---

## 5. MI PROPIA TANDA, Y SOY EL BENEFICIADO DE MI PROPIO JUICIO

**`AUDITOR` se queda en `0 de 3`**, y lo digo con todas las letras: **el que se absuelve es el mismo
que juzga.**

| especie mia | lo que mido |
|---|---|
| **`REMEDIO ROTO`** | **NO, y no por merito mio:** la `ACTA G3` cerro con parada y **no dejo remedio escrito** (`0`, con su comando pegado en `0`). **No hay promesa que romper.** Lo declaro asi y no como si hubiera cumplido algo |
| **`CIFRA PUBLICADA PROPIA`** | **NO.** Toda cifra de esta acta lleva su comando encima, y las tres que no pude medir van dichas como tales en `5.1` |

### 5.1. **LO QUE NO PUDE MEDIR, Y LO DIGO EN VEZ DE PUBLICARLO**

1. **Que la primera corrida de `guiones` diese ROJO con `4` hallazgos** (`G4.4.a`). Hoy los ficheros
   estan limpios (`1.1`) y el barrido verde. **Acepto su declaracion como declaracion, no la publico
   como medida mia.**
2. **Que `recorrer_trece_elementos_proceso_evaluacion_formal` entrase con `0` de `13` partes.** El
   nodo **existe** en el grafo y **hoy tiene `13` `nodos_siguientes`**, eso lo mido; **el estado que
   tenia el dia de su insercion no lo medi.**
3. **El coste de mi propio turno.** Lo escribe la tuberia del arnes en `docs/loop/ultimo_auditor.json`
   cuando mi turno ya termino. **Medida pendiente del arnes, no cifra mia sin medir.**

---

## 6. LO QUE REGISTRO Y NO ABRE COLA (`D.55`, `D.56`)

**La cola de doctrina se queda en `11`.** Lo que sigue son medidas, anotadas y dejadas ahi.

> ### **CORRECCION DECLARADA DENTRO DE MI PROPIO TURNO, SIN BORRAR: LOS TRES NUMEROS DE DEUDA**
>
> **Escribi `d105`, `d106` y `d107` ANTES de correr `scripts/deuda.py --anotar`**, deduciendolos de
> que la ultima deuda del listado era `d104`. **El instrumento asigno `d106`, `d107` y `d108`**, y
> `d105` **no existe**:
>
>     $ grep -o '"id": "d10[0-9]"' docs/loop/DEUDA.jsonl | sort -u
>     "id": "d101"
>     "id": "d102"
>     "id": "d103"
>     "id": "d104"
>     "id": "d106"
>     "id": "d107"
>     "id": "d108"
>
> **ES EXACTAMENTE LA FAMILIA QUE `D.38.3` NOMBRA**: un nombre propio publicado sin leerlo de la
> salida del instrumento corrido en esta misma fase. **Lo cazo yo, en mi turno, antes del commit**,
> y por eso el texto que se commitea es verdadero. Los tres numeros viejos quedan tachados en su
> sitio con el bueno al lado, y esta nota explica por que.
>
> **NO ME LA CARGO COMO `CIFRA PUBLICADA PROPIA`, y digo bajo que lectura para que se pueda
> discutir:** la sede de esa especie es **el acta publicada**, y ninguna version con los numeros
> malos llego a existir fuera de mi turno. **Es el mismo baremo que le aplique al extractor en `1.1`
> con su `guiones` rojo transitorio**, y aplicarme uno mas duro a mi que a el seria tan malo como
> aplicarme uno mas blando. **Lo que si hago es dejarlo escrito**, porque un auditor que corrige en
> silencio dentro de su turno es indistinguible de uno que no se equivoco nunca.

### 6.1. **~~`d105`~~ `d106`: EL TABLERO INVENTA UN CAPITULO MINADO, Y ES EL PRIMERO QUE INVENTA EN VEZ DE PERDER**

*Cuarto ejemplar de la familia `d088` / `d096` / `d102`, y **el que cambia de signo**.*

    $ python forja.py tablero | grep "  gerber_emyth "
      2    9    gerber_emyth                   EN CURSO               gerber_emyth            15  cap_19
    $ python -c "import sys;sys.path.insert(0,'.');from src import tablero;print([f['capitulos_minados'] for f in tablero.libros(tablero.medir()) if f['clave']=='gerber_emyth'])"
    [['cap_04','cap_05','cap_06','cap_07','cap_08','cap_09','cap_10','cap_11','cap_12','cap_13','cap_14','cap_19']]

> **LECTURA, y es la cifra que importa de este apartado:** el ultimo capitulo minado de
> `gerber_emyth` es **`cap_14`**, y el tablero publica **`cap_19`**. `cap_15`, `cap_16`, `cap_17`,
> `cap_18` y `cap_19` **estan SIN TOCAR**, con **`21795`** palabras entre los cinco.
>
> **LA CAUSA, MEDIDA:** `src/tablero.py:133` deriva los capitulos minados **por expresion regular
> sobre el texto entero de cada candidato**, no sobre sus `fuentes`. El candidato nuevo
> `recorrer_siete_pasos_programa_desarrollo_negocio` **cita `cap_19` en su prosa** (es la cabeza de
> la serie y nombra donde vivira cada parte), y el instrumento lo lee como si fuese su origen:
>
>     $ python -c "import re;print(sorted(set(re.findall(r'cap_(\d+)',open('cuarentena/gerber_emyth/recorrer_siete_pasos_programa_desarrollo_negocio.json',encoding='utf-8').read()))))"
>     ['09', '10', '11', '13', '14', '19']
>
> **POR QUE ES PEOR QUE SUS TRES HERMANAS.** `d088`, `d096` y `d102` **perdian** capitulos: el
> tablero decia menos de lo que habia, y quien lo leyera trabajaba de mas. **Esta aniade uno**: el
> tablero dice **mas** de lo que hay, y la columna `ult cap` es la que `D.50` usa para saber por
> donde va un libro al relevarlo. **Un falso negativo hace repetir trabajo; un falso positivo
> esconde cinco capitulos sin minar.**
>
> **NO ES CAIDA DE LA VUELTA.** El candidato tiene que nombrar donde vive cada parte de su serie:
> eso es `D.37` funcionando. **Lo que falla es de quien deriva la cifra**, y esa cifra la escribe el
> instrumento, no el reporte.
>
> **NO LO TOCO** (`D.45` veda `src/` desde un frente, y no es ninguna de las cuatro guardas de DATO
> que bloquean). **Lo mido, lo anoto y lo subo**, que es lo que las tres veces anteriores resulto
> ser lo correcto.

### 6.2. ~~`d106`~~ `d107`: **LA VUELTA CIERRA CON UN PAR SIN LEER, POR EL ORDEN DE LA ADUANA**

La medida esta en `1.7` y la lectura en `3.5`. **No es caida de nadie**: correr la aduana en el acto
(`EXTRACTOR.md` 16) hace que el primer candidato de una vuelta **no pueda ver a ninguno** de los que
se escriben despues. **Remedio barato y sin maquinaria nueva:** volver a correr el informe del
**primer** candidato como ultimo paso de la vuelta. **Va encargado en la vuelta `5`.**

### 6.3. ~~`d107`~~ `d108`: **RELEER `cap_14` `L27` CONTRA `L117` CON LAS DOS DELANTE**

La medida y la lectura estan en `3.4`, punto `a`. **Para la vuelta que inserte este lote**, no para
ahora.

### 6.4. **EL COSTE DEL TURNO, QUE `D.55` ME OBLIGA A DECLARAR CON SU DESGLOSE**

*`D.55`: si un turno pasa de `10` USD y la vuelta no es de saneamiento, el acta lo declara con el
desglose de en que se fue. `D.58` pone el objetivo del regimen ligero en `5`.*

    $ python -c "import json;d=json.load(open('docs/loop/ultimo_extractor.json',encoding='utf-8'));u=d['usage'];print(d['total_cost_usd'],d['duration_ms'],d['num_turns'],u['input_tokens'],u['cache_creation_input_tokens'],u['cache_read_input_tokens'],u['output_tokens'])"
    16.8261033 3110148 166 310 388137 40686221 152699

| pieza | medida | |
|---|---:|---|
| coste del turno del extractor | **16,8261033 USD** | `claude-sonnet-5`, `166` turnos, `51,8` minutos |
| tope de declaracion de `D.55` | `10` | **lo pasa** |
| objetivo del regimen ligero (`D.58`) | `5` | **lo triplica** |
| tokens de **relectura de contexto** (`cache_read`) | **40 686 221** | **98,69 por ciento de todos los tokens del turno** |
| tokens **escritos** (`output`, pensamiento incluido) | `152 699` | `0,37` por ciento |
| relectura de contexto **por turno** | **245 098** | `40 686 221` entre `166` |
| tamanio de `docs/loop/REPORTE.md` | **4 087 721 bytes**, `58 772` lineas | `os.path.getsize` y `wc -l` |

> **LECTURA:** **en que se fue no es en escribir: es en releer.** El turno escribio `152 699` tokens
> y releyo `40 686 221`. La sede que domina esa relectura es `docs/loop/REPORTE.md`, que pesa
> **`4,09` MB** y crece cada vuelta por anexion (`EXTRACTOR.md` 3). **El propio `D.47` ya midio esta
> enfermedad con otras palabras:** *un registro de treinta mil lineas no es un registro mejor, es uno
> que nadie relee*. Hoy son **`58 772`**.
>
> **NO LO ENCARGO, Y DIGO POR QUE.** Rotar `REPORTE.md` a `docs/loop/archivo/` es un mecanismo que
> esta casa **ya tiene y ya uso en este mismo frente**
> (`docs/loop/archivo/gerber_emyth/REPORTE_frente_hasta_v1.md`), pero **es una sede compartida con la
> linea serial y con los frentes en paralelo**, y moverla desde una rama es justo lo que `D.45` dice
> que la cosecha no sabria fundir. **Es decision del fundador, la declaro con su medida y la dejo
> aqui.** Lo unico que si esta en mi mano lo hago: **el encargo de la vuelta `5` abre recordando
> `D.47` con esta cifra delante.**

---

## 7. LAS CONDICIONES DE PARADA, REPASADAS UNA A UNA (`AUDITOR_FORJA.md` `3`)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| **doctrina NUEVA necesaria** | **ninguna.** Los tres discutibles los adjudico con `EXTRACTOR.md` `9.1` **tal como esta escrita** (restricciones `1` y `2`, y la columna `NO es un nodo`); la forma de la correccion de `R3`, con la letra de `D.41`; la fidelidad, con `D.30`; la cabeza de serie, con `D.37` y `9.1`. **No estrecho ni ensancho la vara**, y la tension que encuentro (`3.3`) la registro **sin abrirla**, como `D.55` manda | **NO ES PARADA** |
| **contradiccion** con regla vigente o cifra publicada | **una, `d106`** (`6.1`): el tablero publica `cap_19` donde hay `cap_14`. **Se resuelve con las reglas de correccion existentes**, que es lo que las tres veces anteriores de esta misma familia hicieron: medir, anotar con cita y subir. **No es ninguna de las cuatro guardas de DATO que bloquean** (`D.55`) | **NO ES PARADA** |
| **decision de Alexis** | **ninguna que este turno necesite para cerrar.** Lo que si es suyo y se lo dejo medido: **el tamanio de `REPORTE.md`** (`6.4`) y **`d106`** (`6.1`). No borro contenido, no muevo umbrales, no cambio el alcance, no creo remotos, no fundo ramas | **NO ES PARADA** |
| **fallo tecnico repetido** | **ninguno.** Las cinco guardas de `1.1` en VERDE hoy; la vuelta `3` no tuvo ninguna en rojo. La caida transitoria de `guiones` **no es repetida y quedo corregida dentro del mismo turno** | **NO ES PARADA** |
| **credito roto** | **NO, y lo dice el instrumento antes que yo** (`4.5`): las cinco especies en `0`, ninguna en su tope | **NO ES PARADA** |
| **campania consumada** | **no.** `11` de `22` unidades minadas (`cap_04` a `cap_14`), `15` candidatos en bandeja con `120` pasos, **`0` insertados**, y `cap_15` a `cap_22` sin tocar | **NO ES PARADA** |

> # **NINGUNA SE CUMPLE. NO ESCRIBO `docs/loop/PARA_ALEXIS.md` Y DEJO EL ENCARGO DE LA VUELTA `5` EN `docs/loop/PROMPT_SIGUIENTE.md`.**

**Y NO ESCRIBO NINGUNA TAREA BLOQUEANTE** (`D.55`): **el tope es una, y solo si cita una guarda de
DATO en rojo.** No tengo ninguna en rojo, asi que **cero bloqueantes**, y lo que queda por hacer va a
`docs/loop/DEUDA.jsonl` con su cita, que es donde `D.55` manda que viva.

---

## 8. LA COLA, COMO QUEDA AL CERRAR ESTA ACTA

| lo que queda | cifra que mido hoy | donde vive |
|---|---:|---|
| unidades del lote `9` **minadas** | **`11`** de `22` (`cap_04` a `cap_14`, sin hueco) | contadas por mi contra `fuentes/gerber_emyth/` |
| unidades **sin tocar** | **`11`**: `cap_01` a `cap_03` y `cap_15` a `cap_22` | `d094` para las tres primeras |
| palabras sin minar de los cinco siguientes | **`21795`** (`cap_15` `4685`, `cap_16` `4835`, `cap_17` `2448`, `cap_18` `5396`, `cap_19` `4431`) | mi propio conteo |
| candidatos en bandeja del lote `9` | **`15`**, con **`120`** pasos, **`0`** insertados | `D.39`, y la cosecha es del fundador |
| punteros `D.37` abiertos | **`2`** (`cap_05` `L29`, `cap_12` `L21`), **mas `1` nuevo**: la serie de `cap_13`, `0` de `7` partes | `d098`, `d104`, y `G4.6.d` punto `3` |
| deuda pendiente de la linea | **`35`** pendientes, `33` pagadas, mas las **`3`** que abro aqui | la vuelta `6` sale `SANEAMIENTO` |
| clase que toca a la vuelta `5` | **`LIBRE`**, van `4` de `5` | `python scripts/deuda.py --clase 5` |
| preguntas de doctrina registradas y **NO** abiertas | **`2`** de la `ACTA G2`, **`1`** mia nueva (`3.3`, la linea del puntero) | `D.55`: la cola se queda en `11` |

---

*`ACTA G4` cerrada. **SIN PARADA**, y es la primera de este frente en la que **no se cae ni una
cifra**: las dos caidas son frases, y las dos viven donde `5.2` dice que no acumulan. **Cada cifra de
esta acta lleva su comando pegado encima: se puede repetir entera sin mi.** Mis ficheros de trabajo
de este turno estan en `.g4aud/`.*

# ACTA `G5` DEL FRENTE `gerber_emyth`. VUELTA 5, lote 9, `cap_15`, `cap_16` y `cap_17` minados **EN CUARENTENA**, **CLASE EXTRACCION EN REGIMEN LIGERO**: **LAS DIECISIETE PIEZAS ME SALEN AL DIGITO CON CODIGO MIO, LOS DOS CERO SON CIERTOS Y SE LOS FIRMO, Y LO QUE SE CAE ES UNA CELDA DE TABLA QUE NOMBRA UNA LINEA QUE NO EXISTE**. Recompongo **las diecisiete piezas de los tres capitulos sin su instrumento** y **las diecisiete me dan su palabra exacta**, con residuo `0`, `0` solapes y `0` lineas sin cubrir en los tres. Le cuento **los `5` pasos del unico candidato** y **los leo los `5` contra su parrafo** (`L169` a `L177`), no por muestra: **`0` PUENTE, y le FIRMO las tres filas de `PASOS INVENTADOS`**. Su muestra con semilla `g5` me sale **identica byte a byte** y su informe de aduana **identico al milesimo**, con la poblacion `456` que yo descompongo en `346` mas `110`. **Los dos discutibles marcados se sostienen los dos**, y examino **cinco superficies mas que el NO marco**: las cinco se sostienen. **Y corro el instrumento que decide los dos discutibles antes de leerlos**: en los tres capitulos hay **`11`** lineas con vineta y ni una mas, `4` en la pieza que dio candidato, `7` en la lista del caso de Widget Makers, `0` en `cap_17`. **LO QUE CAE ES UNA CIFRA, Y VIVE EN TABLA**: la fila `R7` de la frontera de `cap_15` publica `L185 a L280` sobre un fichero de **`279`** lineas. **`REPORTE` sube de `0 de 3` a `1 de 3`.** Compruebo que **no es convencion del instrumento** (**`21`** de las **`22`** fronteras que este frente ha escrito acaban en su ultima linea real, y esta es la unica que rebasa) y que **la guarda no la caza**: mis dos mutaciones de hueco y de solape salen ROJAS y la de rebasar el fichero sale MUDA. Caen ademas **dos frases de prosa que NO acumulan, y las dos son la misma figura: un acierto con la razon equivocada a mano**. La primera, *`R3` sin vineta ni imperativo explicito*, cuando `L57` trae *you must always ask*; **la decision sobre `R3` se sostiene igual**, pero por el criterio del PUNTERO de la `ACTA G4` `3.3`. La segunda, que `TABLA_DE_CIERRE.txt` guarda las dos filas de la `ACTA G4` *porque el instrumento solo mide afirmaciones `N` de `M` del capitulo*: **el docstring dice que una fila sin cifra medible SE COPIA TAL CUAL**, y corrido por mi con el reporte completo da **`3`** filas. **La causa real es el ORDEN**, y va a `d112` como cuarto ejemplar de la familia `d022` con causa distinta. **Cinco guardas en VERDE**, `TALLADO VERDE` sobre `170` tablas, **`0` ficheros de dato movidos**. **Y pago la medida que la `ACTA G4` `5.1` dejo pendiente del arnes**: aquel turno de auditor costo **`15,9045775`** USD con el `98,04` por ciento de sus tokens en relectura de contexto. **NO HAY PARADA:** escribo `docs/loop/PROMPT_SIGUIENTE.md` y **no escribo `docs/loop/PARA_ALEXIS.md`**.

*Escrita el 21 sep 2026 por el auditor del bucle, sobre el commit `0ea25eb` de la rama
`extraccion-gerber_emyth`, worktree `C:/Users/AlexDesk/Documents/forja-gerber_emyth`.
**Clase de la vuelta auditada: EXTRACCION en regimen ligero** (`D.58`), asi que **no hubo fase
ciega, ni sello, ni testigo**, y el arnes lo registro el mismo:*

    $ grep -n "SIN FASE CIEGA" docs/loop/loop.log | tail -1
    1117:[2026-09-21 12:39:03] VUELTA 2 : SIN FASE CIEGA (D.58: en cuarentena no hay cifra sobre el grafo que proteger)

*Acta corta por `D.58` y por `D.47`. Mis ficheros de trabajo estan en `.g5aud/`.*

---

## 0. **NO HAY HUECO DE ACTA**, y la herencia se declara antes que nada

**La `ACTA G4` cubre la vuelta `4` de este frente y yo cubro la `5`.** No hay vuelta sin auditar
entre las dos:

    $ grep -n "^# ACTA .G[0-9]" docs/loop/ACTA_AUDITOR.md | tail -2 | cut -c1-58
    45737:# ACTA `G3` DEL FRENTE `gerber_emyth`. VUELTA 3, lote 9
    46220:# ACTA `G4` DEL FRENTE `gerber_emyth`. VUELTA 4, lote 9

**ACTA ANTERIOR LEIDA:** `docs/loop/ACTA_AUDITOR.md`, `ACTA G4`, lineas `46220` a `46924`.

| | heredado | como queda hoy, medido |
|---|---|---|
| **HEREDADO 1** | **NO APLICA, y el motivo va escrito** (`D.40`): la `ACTA G4` cerro **sin tarea bloqueante y sin remedio**, porque `D.55` solo deja dejar una si cita una guarda de DATO en rojo, y no habia ninguna | **NO APLICA** |

**LA SALIDA QUE LO SOSTIENE** (`D.40` ensanchada, 16 sep: un `NO APLICA` lleva su comando pegado):

    $ sed -n '46220,46924p' docs/loop/ACTA_AUDITOR.md | grep -c "TAREA BLOQUEANTE DEL AUDITOR"
    0
    $ sed -n '46220,46924p' docs/loop/ACTA_AUDITOR.md | grep -n "NINGUNA TAREA BLOQUEANTE" | cut -c1-70
    681:**Y NO ESCRIBO NINGUNA TAREA BLOQUEANTE** (`D.55`): **el tope es u

**LO QUE SI HEREDE, Y NO ES UN REMEDIO SINO UNA MEDIDA A MEDIAS.** La `ACTA G4` `5.1` punto `3`
declaro que **no podia medir el coste de su propio turno**, porque lo escribe la tuberia del arnes
cuando el turno ya termino. **Hoy si se puede, y lo mido en `6.3`**: es lo que aquella acta pedia
sin poder pedirlo.

---

## 1. LO QUE VERIFIQUE CON MIS PROPIOS COMANDOS

### 1.1. Las cinco guardas, corridas por mi en esta vuelta

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python tests/test_aceptacion.py
      total: 350 pruebas, 0 fallos, 0 errores
    $ python scripts/tallar_reporte.py
    TALLADO VERDE: las 170 tabla(s) comprobables son las de su instrumento, celda a celda.

**LAS TRES LINEAS DE `gate`, NO DOS** (`d103`). **Y `TALLADO` sube de `167` a `170` tablas**, que
son exactamente las tres fronteras que esta vuelta escribio.

**ESTA VUELTA NO DECLARA NINGUNA GUARDA MORDIENDO**, asi que la mutacion de `7.C` de la cosecha no
tiene sobre que correr en estas cinco. **Donde si la corro es sobre la guarda de frontera, y ahi
esta el hallazgo de `4.1`.**

### 1.2. El estado, contado por mi y no copiado

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
    $ ls cuarentena/gerber_emyth/*.json | wc -l
    16
    $ python -c "import json,glob; print(sum(len(json.load(open(f,encoding='utf-8'))['pasos_accionables']) for f in glob.glob('cuarentena/gerber_emyth/*.json')))"
    125

| pieza | lo que publica `G5.6.b` al cerrar | lo que mido yo | |
|---|---:|---:|---|
| nodos en el grafo | `346` | **346** | **al digito** |
| veredictos escritos | `740` | **740** | **al digito** |
| candidatos en bandeja al cerrar | `16` | **16** | **al digito** |
| pasos en esa bandeja al cerrar | `125` | **125** | **al digito** |
| unidades de `gerber_emyth` | `22` | **22** | **al digito** |
| palabras de cuerpo del libro | `62648` | **62648** | **al digito** |
| ficheros de dato movidos | `0` | **0** | **al digito** |

Las `62648` salen de mi propio recorrido de los `22` ficheros, derivando el arranque del cuerpo de
la segunda linea de cierre de cada cabecera, **sin tocar su instrumento**:

    $ python -c "import glob,io; t=0
    for f in sorted(glob.glob('fuentes/gerber_emyth/cap_*.md')):
        L=io.open(f,encoding='utf-8').read().splitlines()
        d=[i for i,l in enumerate(L) if l.strip()=='---'][1]+1
        t+=len(' '.join(L[d:]).split())
    print(t)"
    62648

**`DATO MOVIDO` medido por mi, y sale en cero:**

    $ git diff --name-only 889bbfc..HEAD -- dataset/ bitacora/ censos/ config/pares_mutuos.jsonl
    (vacio)

**La bandeja sube de `15` a `16` y los pasos de `120` a `125`**, que es el unico movimiento de la
vuelta. **Es bandeja, no grafo.**

### 1.3. Las tres fronteras, recompuestas por mi SIN su instrumento, **pieza por pieza**

**No me basta con volver a correr su `frontera.py`**: eso comprueba que el fichero de piezas no
cambio, no que la frontera cierre. Escribo el mio, que ademas comprueba **el borde de arriba** que
el suyo no mira:

    $ python .g5aud/refrontera.py
    === cap_15, 279 lineas en el fichero
      R1 L8 a L20   reporte 31   mio 31   OK
      R2 L21 a L42   reporte 390   mio 390   OK
      R3 L43 a L86   reporte 516   mio 516   OK
      R4 L87 a L166   reporte 694   mio 694   OK
      R5 L167 a L178   reporte 87   mio 87   OK
      R6 L179 a L184   reporte 76   mio 76   OK
      R7 L185 a L280   reporte 2891   mio 2891   OK
      cuerpo 4685   suma 4685   residuo 0   solapes 0   sin cubrir 0   celdas que discrepan 0
      PIEZAS QUE REBASAN EL FICHERO: R7 acaba en L280
    === cap_16, 489 lineas en el fichero
      R1 L8 a L20   reporte 51   mio 51   OK
      R2 L21 a L30   reporte 87   mio 87   OK
      R3 L31 a L154   reporte 704   mio 704   OK
      R4 L155 a L244   reporte 1166   mio 1166   OK
      R5 L245 a L318   reporte 785   mio 785   OK
      R6 L319 a L420   reporte 1138   mio 1138   OK
      R7 L421 a L489   reporte 904   mio 904   OK
      cuerpo 4835   suma 4835   residuo 0   solapes 0   sin cubrir 0   celdas que discrepan 0
    === cap_17, 221 lineas en el fichero
      R1 L8 a L18   reporte 13   mio 13   OK
      R2 L19 a L50   reporte 254   mio 254   OK
      R3 L51 a L221   reporte 2181   mio 2181   OK
      cuerpo 2448   suma 2448   residuo 0   solapes 0   sin cubrir 0   celdas que discrepan 0

**LAS DIECISIETE PIEZAS ME DAN SU PALABRA EXACTA.** Y el cuerpo de cada uno, contado ademas con
`sed` y `wc`, que es codigo que no es ni suyo ni mio:

    $ sed -n '8,279p' fuentes/gerber_emyth/cap_15.md | wc -w
    4685
    $ sed -n '8,489p' fuentes/gerber_emyth/cap_16.md | wc -w
    4835
    $ sed -n '8,221p' fuentes/gerber_emyth/cap_17.md | wc -w
    2448

**LO UNICO QUE NO ME SALE ES UNA CELDA, Y ES LA CAIDA DE `4.1`:** la fila `R7` de `cap_15` dice
`L185 a L280` y el fichero tiene `279` lineas.

### 1.4. La muestra de fidelidad con semilla `g5`: **identica byte a byte**

    $ python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_15,cap_16,cap_17 --semilla g5 > .g5aud/mf.txt
    $ diff .g5aud/mf.txt .gerber_v5/muestra_fidelidad.txt
    (vacio)

**La semilla reparte `cap_17` a relectura ENTERA y `cap_15` y `cap_16` por muestra**, y me sale la
misma lista, en el mismo orden, con los mismos cortes de columna. **Una muestra que se reproduce es
una muestra.**

**Y LA LECTURA DE `G5.4` SOBRE ESA MUESTRA SE SOSTIENE, QUE ES LA MITAD QUE IMPORTA:** `cap_17`
salio a relectura entera y **tiene cero pasos**, asi que se cumple sin nada que releer, y `cap_16`
tambien tiene cero. **El disparador del `10` por ciento no tiene sobre que dispararse en ninguno de
los dos, y el reporte lo dice con esas palabras** (`SIN SUPERFICIE`, no *cero por debajo del
disparador*). **Le firmo la distincion: es exactamente la que `D.38.3` ensanchada pide, separar la
medida de la conclusion.**

### 1.5. El informe de aduana, vuelto a correr por mi: **identico al milesimo**

    $ python forja.py informe cuarentena/gerber_emyth/responder_4_preguntas_estandares_objetivo_estrategico.json

| pieza | lo que pega `G5.3.a` y `G5.5.b` | lo que me sale hoy | |
|---|---:|---:|---|
| poblacion del barrido | `456` | **456** | **al digito** |
| `ENTRARIAN sin leer nada` | `0` | **0** | |
| `BLOQUEARIAN esperando veredicto` | `1` | **1** | |
| `CAERIAN por una guarda` | `0` | **0** | |
| `CHOCAN entre si dentro del lote` | `0` | **0** | |
| `responder_8_preguntas_construir_primary_aim` | `0.380` / `0.250` / `0.451` | **iguales** | **al milesimo** |
| `cuantificar_impacto_innovacion_6_pasos` | `0.375` / `0.000` / `0.414` | **iguales** | **al milesimo** |
| `probar_traje_azul_seis_semanas` | `0.393` / `0.000` / `0.305` | **iguales** | **al milesimo** |

**Y LOS TRES PARES DE PASOS NOMBRADOS ME SALEN LOS MISMOS** (`2` contra `7`, `2` contra `6`, `4`
contra `2`).

**LA POBLACION ME CUADRA, Y LA DESCOMPONGO YO** (`D.38.5`):

    $ python -c "import os,glob; print(sum(len(glob.glob('cuarentena/%s/*.json'%d)) for d in os.listdir('cuarentena') if not d.startswith('_')))"
    273

> **LECTURA:** `273` menos los `163` de `cuarentena/ensayo_referencia_163/`, que es banco de pruebas
> y no bandeja de campania, da **`110`**, que es lo que el informe dice que espera en bandejas, y
> `346` mas `110` son **`456`**. **Cuadra por la via de `D.38.5`: ya medimos la misma poblacion.**

### 1.6. `d107`, el paso nuevo del encargo: **la salida esta pegada y el `diff` vacio es cierto**

    $ diff .gerber_v5/informe_responder_4_preguntas.txt .gerber_v5/informe_responder_4_preguntas_recierre.txt
    (vacio)

**Y LA RAZON QUE DA ES LA CORRECTA, Y LA COMPRUEBO:** esta vuelta escribio **un solo** candidato,
asi que el primero y el ultimo son el mismo y la bandeja no crecio detras de el. **`d107` no tiene
nada que revelar aqui, y la vuelta lo dijo corriendo el instrumento en vez de darlo por hecho**, que
es lo que el encargo pedia con esas palabras. **Pago cumplido, y la deuda sigue viva para la vuelta
que escriba dos candidatos o mas.**

---

## 2. `PASOS INVENTADOS POR CAPITULO`, QUE ES CIFRA MIA Y LA FIRMO ENTERA (seccion `8`)

**No la copio: cuento yo los pasos y leo yo los parrafos** (`8.3`).

    $ python -c "import json,io; print(len(json.load(io.open('cuarentena/gerber_emyth/responder_4_preguntas_estandares_objetivo_estrategico.json',encoding='utf-8'))['pasos_accionables']))"
    5

| capitulo | candidatos nuevos | pasos escritos, contados por mi | PUENTE que yo encuentro | pasos inventados |
|---|---:|---:|---:|---|
| `cap_15` | `1` | **5** | **0** | **0,00 por ciento** |
| `cap_16` | `0` | **0** | **0** | **SIN SUPERFICIE** |
| `cap_17` | `0` | **0** | **0** | **SIN SUPERFICIE** |
| **la vuelta 5 entera** | **`1`** | **5** | **0** | **0,00 por ciento** |

**LA FIRMO SOBRE LOS `5`, QUE ES EL `100` POR CIENTO**, y no sobre el reparto de la semilla. Los
cinco pasos contra su parrafo:

    $ sed -n '169p;171p;173p;175p;177p' fuentes/gerber_emyth/cap_15.md
    There is no specific number of standards in your Strategic Objective. There are only specific questions that need to be answered.
    • When is your Prototype going to be completed? In two years? Three? Ten?
    • Where are you going to be in business? Locally? Regionally? Nationally? Internationally?
    • How are you going to be in business? Retail? Wholesale? A combination of the two?
    • What standards are you going to insist upon regarding reporting, cleanliness, clothing, management, hiring, firing, training, and so forth?

| paso | de donde sale | opcion propia anadida |
|---|---|---|
| `P1` | `L169`, entero | **ninguna** |
| `P2` | `L171`: dos anios, tres, diez | **ninguna** |
| `P3` | `L173`: localmente, regionalmente, nacionalmente, internacionalmente | **ninguna** |
| `P4` | `L175`: al detalle, al por mayor, la combinacion de las dos | **ninguna** |
| `P5` | `L177`: reportes, limpieza, vestuario, gestion, contratacion, despido, entrenamiento | **ninguna** |

**`0` PUENTE, y la fila decide el volumen** (`8.2`): el peor capitulo con superficie sale `0,00`,
asi que **el volumen no baja**, y lo que lo limita es el techo del ligero (tres capitulos, `D.58`),
no la metrica.

### 2.1. La salvedad que declaro, y no es PUENTE

> **LECTURA:** `P1` **no es ejecutable**: es la frase de marco (*no hay un numero especifico de
> estandares, solo preguntas que responder*). **No es PUENTE** porque esta transcrita de `L169`
> palabra por palabra, y es la misma figura que la `ACTA G4` `2.1` `LECTURA 2` ya declaro para
> `recorrer_siete_pasos`. **Lo digo porque la proporcion importa: `1` de sus `5` pasos es marco y
> `4` son el inventario.**

---

## 3. LA RELECTURA: **SUS DOS DISCUTIBLES SE SOSTIENEN LOS DOS**

**No hubo fase ciega ni veredicto que destapar** (`D.58`, medido en la cabecera), asi que no escribo
`relectura ciega` sobre una fase que no existio. Lo que si hago, y es lo que `5.1` protege:
**empiezo por los que el marco antes de saber si acertaba, y en cada uno leo primero el texto del
libro y despues su razon.**

**Y ANTES DE LEER NINGUNO, CORRO EL INSTRUMENTO QUE DECIDE LOS DOS** (`D.38.3`: la cifra sale de un
instrumento corrido en esta misma fase):

    $ for c in 15 16 17; do echo "cap_$c: $(grep -c '^•' fuentes/gerber_emyth/cap_$c.md)"; done
    cap_15: 4
    cap_16: 7
    cap_17: 0

> **LECTURA:** en los tres capitulos hay **`11`** lineas con vineta y ni una mas. Las `4` de
> `cap_15` son `L171` a `L177`, **la pieza que dio el candidato**; las `7` de `cap_16` son `L209` a
> `L221`, **la lista del discutible `4`**; `cap_17` no tiene ninguna. **Las dos unicas superficies
> con inventario en formato de lista de toda la vuelta son las dos que el marco.** Eso no decide
> quien tiene razon, pero dice que **miro donde habia que mirar.**

### 3.1. Discutible `4`: las siete vinetas del Organization Chart de `cap_16`. **SE SOSTIENE**

    $ sed -n '207p;209p;217p' fuentes/gerber_emyth/cap_16.md
    Since their Strategic Objective has indicated how they will be doing business (one location, assembling and selling widgets and widget-related accessories to a specific consumer within the territory described as North Marine West), Jack and Murray agree that their Organization Chart will require the following positions:
    • President and Chief Operating Officer (COO), accountable for the overall achievement of the Strategic Objective and reporting to the SHAREHOLDERS who include, on an equal basis, Jack and Murray.
    • Reporting to the Vice-President/Marketing are two positions: Sales Manager and Advertising/Research Manager.

**MI LECTURA CON `9.1` DELANTE, antes de mirar la suya.** La restriccion `1` pide inventario de
objetos de trabajo nombrados uno a uno, **y aqui lo hay**: siete posiciones, cada una con su
rendicion de cuentas y su linea de reporte. **La lista existe. Lo que decide no es si existe, sino
de quien es.**

**Y DE QUIEN ES LO DICE LA GRAMATICA DEL PROPIO LIBRO, no una seniial** (`D.19`):

| la lista de `cap_15` `R5`, que SI dio candidato | la lista de `cap_16` `R4`, que NO |
|---|---|
| *There are only specific questions that need to be answered* | *Jack and Murray agree that **their** Organization Chart will require the following positions* |
| **segunda persona generica**: *your Prototype*, *are you going to be in business* | **tercera persona del caso**: sujeto nombrado y posesivo del caso |
| **sin premisa**: el autor habla al lector | **con premisa del caso**: *Since **their** Strategic Objective has indicated... one location... North Marine West* |

**LA PREMISA ES LA PRUEBA.** `L207` no introduce la lista: **la DERIVA** de un Objetivo Estrategico
concreto (una sola locacion, ensamblar y vender widgets en North Marine West). **Un negocio con otro
Objetivo Estrategico no saca esas posiciones**, y el libro lo remata el mismo:

    $ sed -n '224p;411p' fuentes/gerber_emyth/cap_16.md
    Jack and Murray sit back and look at the completed Organization Chart of Widget Makers, Inc., and smile. It sure looks like a big company. The only problem is that Jack and Murray’s names will have to fill all the boxes! They’re the only two employees.
    In this example, Widget Makers, Inc., became an orderly system for creating and re-creating Jack and Murray’s lives.

**ESCRIBIR UN NODO CON `Production Manager` Y `Advertising/Research Manager` SERIA EL SINTOMA BARATO
DE `9.1`** (manual `3.5`): *el entregable del caso lleva un dato del caso*. **Una panaderia como All
About Pies no tiene Production Manager de widgets.**

**Y LO QUE EL CAPITULO SI GENERALIZA NO TRAE INVENTARIO**, que es la otra mitad y la compruebo:

    $ sed -n '409p' fuentes/gerber_emyth/cap_16.md
    That your Organization Chart flows down from your Strategic Objective, which in turn flows down from your Primary Aim.

**Segunda persona, generico, y sin una sola vineta detras** (`3`, `cap_16: 7`, y las siete son las
del caso). Es postura, y es exactamente donde el libro sale del caso. **SU LECTURA SE SOSTIENE, y
su razon escrita tambien.**

### 3.2. Discutible `5`: el Operations Manual del hotel Venetia en `cap_17`. **SE SOSTIENE**

    $ sed -n '191p;195p;203p' fuentes/gerber_emyth/cap_17.md
    “This is our Operations Manual . As you can see, it’s nothing but a series of checklists. This one is a checklist for setting up a room.” He opened the book to a yellow page.
    “Each checklist itemizes the specific steps each Room Support Person must take to do his or her job. There are eight packages of checklists for each Room Support Person waiting in their mailbox when they come in every day. Each package of checklists is used for one of the eight rooms the Room Support Person is accountable for.
    “On the back of each checklist is a drawing of the specific room that identifies each task to be completed, and the order in which it has to be done. The drawing takes the RSP through the routine, and, as they complete each task, they check off the corresponding part of the drawing to show that it was done.

**MI LECTURA.** Hay objetos nombrados uno a uno (checklist por tarea, codigo de color, firma, dibujo
al reverso, control por sorpresa), **pero no hay una sola vineta en todo el capitulo** (`3`,
`cap_17: 0`) y **todo esta en boca del Manager**, en primera persona del plural y con los datos del
hotel pegados: *our Operations Manual*, *eight rooms*, *yellow... Room Setup*, *Room Support Person*.

**LA TENAZA QUE CIERRA EL CASO, Y ES LA QUE HACE BUENA LA DECISION:**

| si el nodo se escribe con los datos del texto | si el nodo se escribe sin ellos |
|---|---|
| lleva `8` habitaciones por persona, amarillo y azul, `Room Support Person` | lleva una generalizacion que el libro **no** escribe |
| **cae por `9.1` y por el manual `3.5`**: el entregable del caso lleva un dato del caso | **cae por `D.30`**: puente es lo que el extractor pone y el libro no dice |

**No hay tercera salida en este texto, asi que no nace candidato. SE SOSTIENE.**

> ### **PERO SU RAZON TIENE UNA MITAD QUE NO LE FIRMO, Y VA A DEUDA (`d110`)**
>
> El discutible dice que `cap_17` *viene cortado a mitad de escena, lo que deja menos texto para
> confirmar si el autor lo generaliza en algun momento*. **La escena no se pierde: continua en el
> fichero siguiente, y el fichero siguiente esta en `fuentes/`.**
>
>     $ sed -n '221p' fuentes/gerber_emyth/cap_17.md
>     I could understand and believe all he had said, but still I asked, “How do you get your RSPs to use the checklists? How do you get them to use the system? Don’t they get tired of the routine? Doesn’t it get boring for them?”
>     $ sed -n '29p' fuentes/gerber_emyth/cap_18.md
>     Since that is the question most often asked of me, I was intrigued with the hotel Manager’s answer to my question, “How do you get your people to do what you want?”
>
> **LECTURA:** `cap_18` (`Cap. 16`, *Your People Strategy*) **abre recogiendo literalmente la
> pregunta con la que `cap_17` corta**. El texto que hacia falta para saber si el autor saca el
> metodo del caso **existe, y se mina en la vuelta siguiente.**
>
> **NO LO CARGO COMO CAIDA, y digo bajo que lectura para que se pueda discutir:** la frase es cierta
> **sobre `cap_17`**, que si se corta ahi, y la decision que sostiene es correcta por la tenaza de
> arriba, **que no depende de la continuacion**. **Lo que hago es cerrar el discutible de verdad**:
> va a `d110` y el encargo de la vuelta `6` lo nombra.

### 3.3. **FUERA DEL MARCADO: cinco superficies que el NO marco y que examino yo**

*Es la cifra que `5.1` pide de verdad: una caida DENTRO del marcado dice que sabia donde estaba su
duda; una FUERA dice que no la vio venir.*

| # | superficie | mi lectura | |
|---:|---|---|---|
| `a` | **`cap_15` `R3`**, `L43` a `L86`: el Primer Estandar, el dinero | **SE SOSTIENE LA DECISION, y NO le firmo la razon**: ver abajo | **sin caida de clase; cae su frase, en prosa** |
| `b` | **`cap_15` `R4`**, `L87` a `L166`: el Segundo Estandar | **SE SOSTIENE**: conceptual mas caso incrustado, `0` vinetas y sin puntero cerrado | **sin caida** |
| `c` | **`cap_16` `L233`**: los cuatro componentes del Position Contract | **SE SOSTIENE**: es una DEFINICION (*a Position Contract... is a summary of*), no un mandato. Mismo patron que `cap_12` `R2` | **sin caida** |
| `d` | **`cap_16` `R6`**, `L319` a `L420`: Prototyping the Position | **SE SOSTIENE**: narrativa en tercera persona de punta a punta, `0` vinetas, sin inventario fuera del caso | **sin caida** |
| `e` | **`cap_17` `R2`**, `L19` a `L50`: que es un Management System | **SE SOSTIENE**: postura pura, sin objeto de trabajo enumerado | **sin caida** |

**SOBRE `a`, Y ES EL UNICO DONDE FIRMO LA DECISION PERO NO LA RAZON.**

El reporte escribe, en `G5.3.a`: *`R3` (el Primer Estandar, dinero) encadena varias preguntas
retoricas en prosa corrida, **sin vineta ni imperativo explicito***.

    $ sed -n '57p;59p' fuentes/gerber_emyth/cap_15.md
    Indeed, the first question you must always ask when creating standards for your Strategic Objective is: What will serve my Primary Aim?
    The first question about money then becomes: How much money do I need to live the way I wish? Not in income but in assets. In other words, how much money do you need in order to be independent of work, to be free ?

> **LECTURA:** *the first question **you must always ask*** es un imperativo modal explicito sobre
> un objeto nombrado, y `L51` enumera cuatro objetos uno a uno (ingresos brutos, *gross profits,
> pretax profits, after-tax profits*). **La mitad de su razon que dice *sin imperativo explicito* es
> falsa.**

**Y AUN ASI LA DECISION ES LA CORRECTA, por el criterio que la `ACTA G4` `3.3` dejo escrito:** lo
que separa no es la suavizacion ni la vineta, **es el PUNTERO.**

    $ sed -n '43p' fuentes/gerber_emyth/cap_15.md
    Let’s take a closer look at some of the standards that need to be included in your Strategic Objective .

> **LECTURA:** `R3` abre con ***some** of the standards*, un conjunto **abierto** del que el
> capitulo da ejemplos sueltos; `R5` abre con *There are only specific questions that need to be
> answered* y detras vienen **cuatro vinetas y nada mas**, un conjunto **cerrado y escrito**. **Es
> la misma linea que sostuvo `cap_14` `R5` contra `cap_12` `R6` en la vuelta `4`**, y se aplica sola
> aqui. **No estrecho ni ensancho la vara** (`6.3`): uso la que ya estaba escrita.

**LO CARGO COMO CAIDA DE FRASE Y NO DE CLASE**, y va en `4.2`.

---

## 4. LO QUE SE CAE, POR ESPECIE

### 4.1. `REPORTE`: **UNA CAIDA QUE ACUMULA, y vive en TABLA**

*`5.2`: la especie `REPORTE` **acumula si la cifra vive en TABLA, CABECERA o CONCLUSION**.*

**LA CELDA:** en `G5.3.a`, la fila `R7` de la frontera de `cap_15` publica **`L185 a L280`**.

    $ wc -l fuentes/gerber_emyth/cap_15.md
    279 fuentes/gerber_emyth/cap_15.md

> **LECTURA:** el fichero tiene **`279`** lineas y la celda nombra una pieza que acaba en la
> **`280`**. **La linea `280` no existe.** La pieza va de `L185` a `L279`.

**COMPRUEBO QUE NO ES UNA CONVENCION DEL INSTRUMENTO, porque si lo fuera no seria una celda falsa.**
Recorro las `22` fronteras que este frente ha escrito desde la vuelta `1` y comparo el borde de
arriba de cada una contra su fichero:

    $ python .g5aud/bordes.py
    .gerber_v1\piezas_cap01.txt      ultima pieza L71    fichero 71    exacta
    .gerber_v1\piezas_cap02.txt      ultima pieza L99    fichero 99    exacta
    .gerber_v1\piezas_cap03.txt      ultima pieza L233   fichero 233   exacta
    .gerber_v1\piezas_cap04.txt      ultima pieza L297   fichero 297   exacta
    .gerber_v1\piezas_cap05.txt      ultima pieza L149   fichero 149   exacta
    .gerber_v1\piezas_cap06.txt      ultima pieza L221   fichero 221   exacta
    .gerber_v1\piezas_cap07.txt      ultima pieza L329   fichero 329   exacta
    .gerber_v1\piezas_cap08.txt      ultima pieza L179   fichero 179   exacta
    .gerber_v1\piezas_cap09.txt      ultima pieza L233   fichero 233   exacta
    .gerber_v1\piezas_cap10.txt      ultima pieza L145   fichero 145   exacta
    .gerber_v1\piezas_cap11.txt      ultima pieza L329   fichero 329   exacta
    .gerber_v2\piezas_cap05.txt      ultima pieza L149   fichero 149   exacta
    .gerber_v2\piezas_cap06.txt      ultima pieza L221   fichero 221   exacta
    .gerber_v3\piezas_cap09.txt      ultima pieza L233   fichero 233   exacta
    .gerber_v3\piezas_cap10.txt      ultima pieza L145   fichero 145   exacta
    .gerber_v3\piezas_cap12.txt      ultima pieza L293   fichero 293   exacta
    .gerber_v4\piezas_cap12.txt      ultima pieza L293   fichero 293   exacta
    .gerber_v4\piezas_cap13.txt      ultima pieza L59    fichero 59    exacta
    .gerber_v4\piezas_cap14.txt      ultima pieza L217   fichero 217   exacta
    .gerber_v5\piezas_cap15.txt      ultima pieza L280   fichero 279   REBASA
    .gerber_v5\piezas_cap16.txt      ultima pieza L489   fichero 489   exacta
    .gerber_v5\piezas_cap17.txt      ultima pieza L221   fichero 221   exacta

> **LECTURA:** **`21` de `22` acaban en su ultima linea real y UNA la rebasa. No es convencion: es
> una celda.**

**Y LA GUARDA NO LA CAZA, Y LO MIDO POR MUTACION** (`7.C` de la cosecha, aplicada a la guarda que el
reporte usa para decir `0` solapes y `0` huecos):

    $ grep -v '"R6", 179, 184' .gerber_v5/piezas_cap15.txt > .g5aud/piezas_mutada.txt
    $ python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_15.md .g5aud/piezas_mutada.txt | tail -2
    piezas: 6   lineas solapadas: 0   lineas sin cubrir: 6   cuerpo 4685   suma 4609   residuo 76
    HUECOS: L179, L180, L181, L182, L183, L184
    $ sed 's/"R6", 179, 184/"R6", 175, 184/' .gerber_v5/piezas_cap15.txt > .g5aud/piezas_mutada2.txt
    $ python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_15.md .g5aud/piezas_mutada2.txt | tail -1
    piezas: 7   lineas solapadas: 1   lineas sin cubrir: 0   cuerpo 4685   suma 4721   residuo -36

> **LECTURA:** **las dos mutaciones que la guarda cubre salen ROJAS** (el hueco con su lista, el
> solape con su residuo negativo). **La tercera, rebasar el fichero, sale MUDA**, porque
> `frontera.py` calcula los huecos como *cuerpo menos cubiertas* y no mira nunca el borde de arriba:
> la linea inventada no aporta palabras, asi que el residuo sigue en `0` y el instrumento no tiene
> de que quejarse. **Va a `d109`, y NO la encargo**: la moratoria de maquinaria (`7.F`) y `D.47`
> solo se levantan con una caida de DATO, **y esta no lo es.**

**POR QUE ACUMULA Y NO LA PERDONO.** `5.2` es explicita: en TABLA, acumula. Y esta ademas en **tres**
sitios (la tabla de `G5.3.a`, la de `.gerber_v5/frontera_cap15.txt` y la fila del fichero de
piezas). **No mueve ningun dato** (el recuento de palabras es identico, porque la linea `280` no
existe y no aporta ninguna), **y por eso es `REPORTE` y no `CIFRA PUBLICADA`: la sede manda** (`5.2`).

**LA CORRECCION ES BARATA Y LA MIDO ANTES DE ENCARGARLA**, porque una correccion que mueva una cifra
buena no es una correccion:

    $ sed 's/"R7", 185, 280/"R7", 185, 279/' .gerber_v5/piezas_cap15.txt > .g5aud/piezas_cap15_279.txt
    $ python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_15.md .g5aud/piezas_cap15_279.txt > .g5aud/frontera_cap15_279.txt
    $ diff .gerber_v5/frontera_cap15.txt .g5aud/frontera_cap15_279.txt
    13c13
    < | `R7` | L185 a L280 | **2891** | la historia de Sarah [...] | **CASO** |
    ---
    > | `R7` | L185 a L279 | **2891** | la historia de Sarah [...] | **CASO** |

> **LECTURA:** **la unica celda que cambia es la del rango.** Las `2891` palabras, el cuerpo de
> `4685`, la suma, el residuo `0`, los `0` solapes y las `0` lineas sin cubrir salen **identicos**.
> **La tabla es TALLADA, asi que se corrige REGENERANDO y nunca tecleando la celda** (`D.41`), y va
> encargada asi en la `TAREA 1` de la vuelta `6`.

**`REPORTE` SUBE DE `0 de 3` A `1 de 3`.**

### 4.2. `REPORTE`, las otras dos: **dos frases en PROSA que NO acumulan, y las dos son la misma figura**

*`5.2`: en **lista de rutas o prosa de acompaniamiento**, la especie `REPORTE` **NO acumula**. Se
registra con su nombre y lo unico que deja de hacer es mover el contador (`D.38.1`).*

**LAS DOS SON UN ACIERTO CON LA RAZON EQUIVOCADA A MANO, que es la forma de fallo que conviene decir
en voz alta porque viaja sola de vuelta en vuelta.**

**CAIDA `a`. `G5.3.a`:** *`R3` ... sin vineta ni **imperativo explicito***. La medida y la lectura
estan en `3.3` punto `a`: `L57` trae *the first question **you must always ask***. **La decision de
`R3` se sostiene**, y la sostengo yo con el criterio del PUNTERO. **Caida de premisa, no de clase.**

**CAIDA `b`. `G5.6.a`:** *la tabla regenerada muestra solo las dos filas de la `ACTA G4` **porque el
instrumento mide afirmaciones de la forma `N` de `M` del capitulo** y esta vuelta no escribio
ninguna con ese patron*.

    $ sed -n '31,33p' scripts/tabla_de_cierre.py
    LO QUE NO INVENTA. Una fila sin cifra medible **se copia tal cual y se declara
    `SIN COMPROBAR`**. Un instrumento que rellena lo que no sabe no mide: dicta. Y el patron
    es **estrecho a proposito**: `de 5 de 5` de un TRAMO no se toca, porque un tramo no es un

    $ python scripts/tabla_de_cierre.py | head -7
    ============================================================================
    TABLA DE CIERRE DE TAREAS (D.52): toda tabla del reporte declara su instrumento
    ============================================================================
      libro de la linea : gerber_emyth
      filas             : 3
      SIN COMPROBAR  `1`  ninguna afirmacion de la forma 'N de M del capitulo' con su cap_NN
      SIN COMPROBAR  `2`  ninguna afirmacion de la forma 'N de M del capitulo' con su cap_NN

> **LECTURA:** **una fila sin cifra medible NO se descarta: se copia tal cual.** Corrido por mi con
> el reporte ya completo, el instrumento encuentra **`3`** filas (las de `G5.6.a`) y las declara las
> tres `SIN COMPROBAR`. **La razon por la que su fichero guarda las dos filas de la `ACTA G4` no es
> el patron: es el ORDEN.** El instrumento lee **la ULTIMA** tabla de cabecera fija de
> `REPORTE.md`, y `--escribir` se corrio **antes** de pegar la de `G5.6.a`.
>
> **LO QUE SI LE FIRMO, Y NO ES POCO:** que el fichero muestra las dos filas de la `ACTA G4`
> **es cierto**, la vuelta **lo declaro en vez de esconderlo**, y marco su propia tabla como
> `TALLADO: parcial`. **Un fichero viejo declarado no es una cifra falsa**, y por eso `CIFRA
> PUBLICADA` sale limpia en `4.3`. Lo que cae es la explicacion.
>
> **CUARTO EJEMPLAR DE LA FAMILIA `d022`, CON CAUSA DISTINTA**, y por eso lo anoto aparte en `d112`:
> `d022` era la cabecera, `d030` era el nombre del fichero de salida, **y esta es el orden.**
> **EL REMEDIO NO ES MAQUINARIA**: correr `--escribir` **despues** de pegar la tabla, y va encargado
> asi en la vuelta `6`.

**NINGUNA DE LAS DOS MUEVE EL CONTADOR.** La que lo mueve es la de `4.1`, que vive en TABLA.

### 4.3. `CIFRA PUBLICADA`: **LIMPIA**, y `D.61` repasada por mi

| discutible de la vuelta `5` | ejecutado o cerrado |
|---|---|
| `4` (las siete vinetas de `cap_16`) | **CERRADO con su lectura y su linea** (`G5.7.a`, `L207` a `L209`), verificado por mi en `3.1` |
| `5` (el Operations Manual de `cap_17`) | **CERRADO con su lectura y su linea** (`G5.7.a`, `L189` a `L191`), verificado por mi en `3.2`. **Su mitad floja va a `d110`, que es deuda y no discutible abierto** |

**NINGUNO QUEDA ABIERTO EN LA FORMA QUE `D.61` CASTIGA**: los dos son dudas de lectura sobre
capitulos ya leidos y cerrados con `0` candidatos, **no promesas de trabajo futuro**. `0 de 2`.

**Y LAS OTRAS SEDES DURADERAS QUE LA VUELTA TOCO, MEDIDAS:** `docs/loop/TABLA_DE_CIERRE.txt`
(regenerada por su instrumento, y `TALLADO VERDE` la cubre) y `docs/loop/DEUDA.jsonl` (esta vuelta
no abrio ni pago ninguna, y lo mido: `38` pendientes y `33` pagadas antes de las tres mias, que son
los mismos que la `ACTA G4` `8` dejo al cerrar contando las suyas).

**Y `docs/loop/TABLA_DE_CIERRE.txt` LA MIRO APARTE, PORQUE ES SEDE DURADERA Y HOY GUARDA LA TABLA
DE OTRA VUELTA.** Lo que dice el reporte es cierto, lo que dice de por que no: va en `4.2`, caida
`b`.

### 4.4. `CLASE`: **LIMPIA, y por sede**

**Cero veredictos escritos y cero ficheros de dato movidos** (`1.2`). La sede de `CLASE` es
`bitacora/VEREDICTOS.jsonl`, `config/pares_mutuos.jsonl` y el dataset, **y esta vuelta no escribio
en ninguna de las tres**. `0 de 2`.

**Y LOS TRES VEREDICTOS DE LECTURA QUE SI ESCRIBIO EN SU REPORTE** (`SANO` para los tres vecinos del
candidato) **se los verifico y se los firmo**: `responder_8_preguntas` pregunta por el horizonte de
una vida entera y el candidato por el plazo de un Prototipo; `cuantificar_impacto_innovacion` mide
una innovacion ya probada; `probar_traje_azul` es vestuario de un test de ventas contra la modalidad
de venta al detalle o al por mayor. **Coincidencia lexica de superficie en los tres, cero objeto
compartido.** No se escriben en `bitacora/` porque `D.39` no lo permite en cuarentena, **y eso es
correcto.**

### 4.5. `DATO MOVIDO`: **LIMPIA**

`git diff --name-only 889bbfc..HEAD -- dataset/ bitacora/ censos/ config/pares_mutuos.jsonl` sale
vacio (`1.2`). `0 de 2`.

### 4.6. **LA TANDA, ESPECIE POR ESPECIE**

| especie | racha al abrir | caidas que acumulan en mi tanda | racha al cerrar |
|---|---|---:|---|
| `REPORTE` | `0 de 3` | **1** (`4.1`, celda en tabla) | **`1 de 3`** |
| `CIFRA PUBLICADA` | `0 de 2` | **0** | **`0 de 2`** |
| `CLASE` | `0 de 2` | **0** | **`0 de 2`** |
| `DATO MOVIDO` | `0 de 2` | **0** | **`0 de 2`** |
| `AUDITOR` (mia) | `0 de 3` | **0** (ver `5`) | **`0 de 3`** |

**NINGUNA EN SU TOPE. `REPORTE` NECESITA TRES SEGUIDAS PARA PARAR** (`5.4`), **y una tanda limpia en
medio la pone a cero** (`D.38.1`).

---

## 5. MI PROPIA TANDA, Y SOY EL BENEFICIADO DE MI PROPIO JUICIO

**`AUDITOR` se queda en `0 de 3`**, y lo digo con todas las letras: **el que se absuelve es el mismo
que juzga.**

| especie mia | lo que mido |
|---|---|
| **`REMEDIO ROTO`** | **NO, y no por merito mio:** la `ACTA G4` no dejo remedio ni bloqueante (`0`, con su comando pegado en `0`). **No hay promesa que romper** |
| **`CIFRA PUBLICADA PROPIA`** | **NO.** Toda cifra de esta acta lleva su comando encima, y lo que no pude medir va dicho como tal en `5.1` |

### 5.1. **LO QUE NO PUDE MEDIR, Y LO DIGO EN VEZ DE PUBLICARLO**

1. **Que las tres guardas diesen verde en el turno del extractor, y no solo hoy.** Yo las corro hoy
   y me salen verdes; **que su primera corrida tambien lo fuera lo acepto como declaracion suya**,
   no como medida mia.
2. **El coste de mi propio turno.** Lo escribe la tuberia del arnes en `docs/loop/ultimo_auditor.json`
   cuando mi turno ya termino, y ahora mismo el fichero esta en **`0` bytes** porque `D.34.2` lo
   retira. **Medida pendiente del arnes, y el auditor de la vuelta `6` la puede pagar como yo pago
   la de la `ACTA G4` en `6.3`.**

---

## 6. LO QUE REGISTRO Y NO ABRE COLA (`D.55`)

**La cola de doctrina se queda en `11`.** Lo que sigue son medidas, anotadas y dejadas ahi. **Las
cuatro tienen su fila en `docs/loop/DEUDA.jsonl`**, escrita por el instrumento y no tecleada por mi:

    $ python scripts/deuda.py | tail -6 | cut -c1-84
      d109   5       maquinaria         LA GUARDA DE FRONTERA NO CAZA UNA PIEZA QUE REBA
      d110   5       relectura          EL DISCUTIBLE 5 SE CIERRA EN cap_18, NO EN cap_1
      d111   5       relectura          LA SERIE D.37 DE cap_13 VA POR 0 DE 7 CON CUATRO
      d112   5       maquinaria         CUARTO EJEMPLAR DE LA FAMILIA d022, CON CAUSA DI

      ultima vuelta de saneamiento: ninguna todavia

### 6.1. `d109`: **LA GUARDA DE FRONTERA TIENE DOS BORDES Y VIGILA UNO**

La medida y las tres mutaciones estan en `4.1`. **Dos rojas, una muda.** **No la encargo**
(`7.F`, `D.47`): la moratoria de maquinaria solo se levanta con una caida de DATO.

### 6.2. `d111`: **LA SERIE `D.37` DE `cap_13` VA POR `0` DE `7` CON CUATRO PASOS YA LEIDOS**

*Medida nueva sobre un puntero que la `ACTA G4` `8` ya tenia abierto.*

    $ sed -n '43,57p' fuentes/gerber_emyth/cap_13.md | grep "^[0-9]\."
    1. Your Primary Aim
    2. Your Strategic Objective
    3. Your Organizational Strategy
    4. Your Management Strategy
    5. Your People Strategy
    6. Your Marketing Strategy
    7. Your Systems Strategy

| paso de la serie | fichero | como cerro | parte cableada |
|---:|---|---|---|
| `1` | `cap_14` | metodo dentro del paso (`responder_8_preguntas`), no cabeza | **no** |
| `2` | `cap_15` | metodo dentro del paso (`responder_4_preguntas`), no cabeza | **no** |
| `3` | `cap_16` | **cero candidatos** | **no** |
| `4` | `cap_17` | **cero candidatos** | **no** |
| `5` | `cap_18` | sin minar | pendiente |
| `6` | `gerber_emyth_cap17_reservado` | **apartado, no se toca** | **nunca** |
| `7` | `cap_19` | sin minar | pendiente |

> **LECTURA:** la cabeza de serie va camino de entrar al grafo con **`0` de `7`** partes, y le
> quedan **dos** capitulos para ganar alguna. **No es caida de nadie**: las cuatro decisiones de
> arriba son correctas una a una y se las he firmado las cuatro. **Lo que digo es que la vuelta que
> INSERTE tiene que decidir que se hace con una cabeza de serie en esa situacion, con la medida
> delante y no al vuelo.** `d111`, y **no abre doctrina** (`D.55`).

### 6.3. **EL COSTE, Y AQUI PAGO LA MEDIDA QUE LA `ACTA G4` DEJO PENDIENTE**

*`D.55`: si un turno pasa de `10` USD y la vuelta no es de saneamiento, el acta lo declara con el
desglose. `D.58` pone el objetivo del regimen ligero en `5`.*

    $ python -c "import json,io;d=json.load(io.open('docs/loop/ultimo_extractor.json',encoding='utf-8'));u=d['usage'];print(d['total_cost_usd'],d['num_turns'],d['duration_ms'],u['cache_read_input_tokens'],u['output_tokens'],u['cache_creation_input_tokens'])"
    8.971043100000001 107 1574222 19772887 95513 267647
    $ git show HEAD:docs/loop/ultimo_auditor.json | python -c "import json,sys;d=json.load(sys.stdin);u=d['usage'];print(d['total_cost_usd'],d['num_turns'],d['duration_ms'],u['cache_read_input_tokens'],u['output_tokens'],u['cache_creation_input_tokens'])"
    15.904577500000002 121 2130043 20106385 121835 280436

| turno | coste USD | turnos | minutos | relectura de contexto | escrito | relectura sobre el total |
|---|---:|---:|---:|---:|---:|---:|
| **extractor de la vuelta `5`** | **8,9710431** | `107` | `26,2` | `19 772 887` | `95 513` | **98,20 por ciento** |
| **auditor de la `ACTA G4`** | **15,9045775** | `121` | `35,5` | `20 106 385` | `121 835` | **98,04 por ciento** |

> **LECTURA 1, la del extractor:** **no pasa el tope de `10` de `D.55`**, asi que no me debe
> desglose, y aun asi lo pego porque la comparacion es la cifra util: **`16,8261033` en la vuelta
> `4` contra `8,9710431` en la `5`**, casi la mitad, con `D.47` delante y un capitulo mas de tramo.
> **Sigue por encima del objetivo de `5` del ligero, y sigue con el `98` por ciento de sus tokens en
> releer.**
>
> **LECTURA 2, la del auditor, y es la que la `ACTA G4` `5.1` declaro que no podia medir:** aquel
> turno **paso el tope de `10`** y **nadie lo declaro**, porque el dato no existia mientras el turno
> corria. **Ya existe, y lo declaro yo.** Su desglose es el mismo del extractor: **escribio
> `121 835` tokens y releyo `20 106 385`.**

**LAS DOS SEDES QUE SE RELEEN, MEDIDAS HOY**, y la segunda no la habia medido nadie:

    $ python -c "import os;print([(f, os.path.getsize('docs/loop/'+f)) for f in ('REPORTE.md','ACTA_AUDITOR.md')])"
    [('REPORTE.md', 4126938), ('ACTA_AUDITOR.md', 3145437)]

> **LECTURA:** `REPORTE.md` pesa **`4 126 938`** bytes y `ACTA_AUDITOR.md` **`3 145 437`**. La
> `ACTA G4` `6.4` midio la primera y dejo la segunda sin medir: **juntas son `7 272 375` bytes**, y
> las dos crecen por anexion cada vuelta. **Es la misma enfermedad que `D.47` nombro con otras
> palabras**, y rotarlas **sigue siendo decision del fundador**, porque son sede compartida con la
> serial y con los frentes en paralelo (`D.45`). **Lo declaro con su medida y lo dejo aqui.**

---

## 7. LAS CONDICIONES DE PARADA, REPASADAS UNA A UNA (`AUDITOR_FORJA.md` `3`)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| **doctrina NUEVA necesaria** | **ninguna.** Los dos discutibles los adjudico con `9.1` y el manual `3.5` tal como estan escritos, mas el criterio del PUNTERO de la `ACTA G4` `3.3`; la fidelidad, con `D.30`; la forma de la correccion, con `D.41`. **No estrecho ni ensancho la vara** (`6.3`), y lo que encuentro nuevo (`6.1`, `6.2`) lo registro **sin abrirlo** | **NO ES PARADA** |
| **contradiccion** con regla vigente o cifra publicada | **una, y se resuelve con las reglas de correccion existentes**: la celda `L280` de `4.1`, que se corrige REGENERANDO (`D.41`) y va encargada en la `TAREA 1` de la vuelta `6`. **`d106` sigue viva** (el tablero publica `ult cap = cap_19` para un libro cuyo ultimo minado es `cap_17`) y sigue sin ser de este frente: es de `src/`, que `D.45` veda | **NO ES PARADA** |
| **decision de Alexis** | **ninguna que este turno necesite para cerrar.** Lo que si es suyo y le dejo medido: **las dos sedes que se releen** (`6.3`) y **`d106`**. No borro contenido, no muevo umbrales, no cambio el alcance, no creo remotos, no fundo ramas | **NO ES PARADA** |
| **fallo tecnico repetido** | **ninguno.** Las cinco guardas de `1.1` en VERDE hoy, y la vuelta `4` tampoco tuvo ninguna en rojo al cerrar | **NO ES PARADA** |
| **credito roto** | **NO.** `REPORTE` sube a `1 de 3`, que **no es su tope**; las otras cuatro en `0`. **Hacen falta TRES seguidas** (`5.4`) | **NO ES PARADA** |
| **campania consumada** | **no.** `14` de `22` unidades minadas (`cap_04` a `cap_17`, sin hueco), `16` candidatos en bandeja con `125` pasos, **`0` insertados**, y `cap_18` a `cap_22` sin tocar | **NO ES PARADA** |

> # **NINGUNA SE CUMPLE. NO ESCRIBO `docs/loop/PARA_ALEXIS.md` Y DEJO EL ENCARGO DE LA VUELTA `6` EN `docs/loop/PROMPT_SIGUIENTE.md`.**

**Y NO ESCRIBO NINGUNA TAREA BLOQUEANTE** (`D.55`): **el tope es una, y solo si cita una guarda de
DATO en rojo.** No tengo ninguna en rojo, **asi que cero bloqueantes**, y lo que queda por hacer va
a `docs/loop/DEUDA.jsonl` con su cita, que es donde `D.55` manda que viva.

**LA CLASE DE LA VUELTA `6` NO LA DECIDO YO**, la dice el instrumento:

    $ python scripts/deuda.py --clase 5
    LIBRE
      van 4 de 5 desde la primera vuelta de la linea 'gerber_emyth' (la 1), que todavia no ha saneado nunca, con 38 deuda(s) esperando

> **LECTURA:** la vuelta `5` corrio `LIBRE` con `4` de `5`. **La `6` es la quinta, asi que sale
> `SANEAMIENTO`**, y el arnes no deja que el encargo diga otra cosa (`D.58`). **Mi encargo la
> escribe como saneamiento**, y por eso su `TAREA 2` paga deuda en vez de abrir `cap_18`.

---

## 8. LA COLA, COMO QUEDA AL CERRAR ESTA ACTA

| lo que queda | cifra que mido hoy | donde vive |
|---|---:|---|
| unidades del lote `9` **minadas** | **`14`** de `22` (`cap_04` a `cap_17`, sin hueco) | contadas por mi contra `fuentes/gerber_emyth/` |
| unidades **sin tocar** | **`8`**: `cap_01` a `cap_03` y `cap_18` a `cap_22` | `d094` para las tres primeras |
| palabras sin minar de los dos siguientes | **`9827`** (`cap_18` `5396`, `cap_19` `4431`) | `.gerber_v5/cierre.txt` |
| candidatos en bandeja del lote `9` | **`16`**, con **`125`** pasos, **`0`** insertados | `D.39`, y la cosecha es del fundador |
| punteros `D.37` abiertos | **`3`**: `cap_05` `L29`, `cap_12` `L21`, y la serie de `cap_13` en `0` de `7` | `d098`, `d104`, `d111` |
| deuda pendiente de la linea | **`38`** antes de las mias, **`42`** despues | `d109`, `d110`, `d111`, `d112` |
| clase que toca a la vuelta `6` | **`SANEAMIENTO`**, la quinta desde la `1` | `python scripts/deuda.py --clase 5` |
| preguntas de doctrina registradas y **NO** abiertas | **`2`** de la `ACTA G2`, `1` de la `ACTA G4`, **`1`** mia nueva (`6.2`) | `D.55`: la cola se queda en `11` |

---

*`ACTA G5` cerrada. **SIN PARADA.** Lo que cae es **una celda de tabla que nombra una linea que no
existe**, y la cargo aunque no mueva ni una palabra de ninguna cifra, porque `5.2` dice que en TABLA
acumula y **perdonarla seria elegir la lectura que me deja seguir**. Lo demas se sostiene entero:
las diecisiete piezas al digito, los cinco pasos sin puente, los dos cero con su razon leida, y los
dos discutibles en pie. **Cada cifra de esta acta lleva su comando pegado encima: se puede repetir
entera sin mi.** Mis ficheros de trabajo de este turno estan en `.g5aud/`.*

---

# ACTA `G6` DEL FRENTE `gerber_emyth`. VUELTA 6, lote 9, **CLASE SANEAMIENTO**, la primera que esta linea corre (`D.55`, `D.58`): **LA CELDA `L280` ESTA CORREGIDA REGENERANDO Y SE LA FIRMO AL DIGITO CON CODIGO MIO, LOS TRES PAGOS SE SOSTIENEN LOS TRES, Y LO QUE SE CAE ES LA CABECERA: FIRMA SU CLASE CON UN INSTRUMENTO QUE, CORRIDO, DICE `LIBRE`**

Recompongo **las `7` piezas de `cap_15` sin su instrumento** y me salen al digito (`2891` palabras en
`R7`, cuerpo `4685`, suma `4685`, residuo `0`, `0` solapes, `0` lineas sin cubrir), **y `R7` acaba
ahora en la ultima linea real del fichero**: la correccion de la `ACTA G5` `4.1` esta hecha
**regenerando y no tecleando**, con su diff pegado encima de la tabla y su motivo en una linea.
**Los tres pagos me reproducen los tres**: `d102` no reproduce (`16` publicados contra `16` reales,
contados por mi), `d103` no reproduce (las tres citas pegan **tres** lineas, las tres verificadas por
mi con `sed`), y `d112` esta pagada de verdad, **porque `docs/loop/TABLA_DE_CIERRE.txt` trae hoy las
tres filas de la vuelta `6` y no las dos de la `ACTA G4`**. `d106` sigue viva y la mido yo: el tablero
publica `cap_19` como ultimo capitulo minado de un libro cuyo ultimo minado es `cap_15`, y **omite
`cap_16` y `cap_17`**. **Siete instrumentos en VERDE** (`gate`, `guiones`, `350` pruebas, tallado,
censo de rutas, resolutor, tabla de cierre) y **`0` ficheros de `dataset/`, `bitacora/`, `censos/` ni
`config/` movidos**, medido por `git diff` entre los dos commits de la vuelta.

**LO QUE CAE VIVE EN LA CABECERA DEL BLOQUE.** Dice: *`CLASE DE ESTA VUELTA: SANEAMIENTO`, dictada por
el instrumento y no por mi lectura (`python scripts/deuda.py --clase 5`, `G6.1`). La linea
`gerber_emyth` va `4` de `5`*. **Las tres piezas de esa frase fallan y el rotulo acierta:** el comando
citado, corrido por mi sobre el registro con el que la vuelta abrio, imprime **`LIBRE`**; `G6.1` **no
trae ninguna salida de `--clase`** y no existe fichero suyo que la guarde; y **la linea no va `4` de
`5` en la vuelta `6`, va `5` de `5`**, que es justamente por lo que le toca sanear. **Una cuenta de
`4` de `5` no alcanza una cadencia de `5`: la frase justifica el rotulo con el numero que lo
desmiente.** Y esa cifra **esta copiada del reporte de la vuelta anterior** (`REPORTE.md` `59300`),
que es lo que `EXTRACTOR.md` `5` prohibe con todas las letras. **Vive en CABECERA, asi que `5.2` dice
que acumula: `REPORTE` sube de `1 de 3` a `2 de 3`.**

**Y LA RAIZ DE ESA CAIDA ES MIA, Y LA DECLARO ANTES QUE LA SUYA** (`5.3`): la `ACTA G5` `8` y el
encargo de la vuelta `6` le pusieron delante `python scripts/deuda.py --clase 5` **como el instrumento
de la clase de la vuelta `6`**, cuando el que la dicta es `--clase 6`. **El rotulo que yo publique era
cierto y el comando con el que lo firme no lo produce.** No acumula en mi racha porque la cifra de mi
celda (*la quinta desde la `1`*) **es verdadera**, y `CIFRA PUBLICADA PROPIA` pide una cifra falsa; **se
registra con mi nombre igual** (`5.4`) y va a la deuda con su medida.

**Cae ademas una cifra de tabla que NO suma un escalon aparte**, porque la racha cuenta tandas y no
caidas: `G6.6` dice *las nueve filas de la tabla de deuda* del encargo, **y la tabla tiene `12`**,
contadas por mi. Existe una lectura en la que `nueve` es cierto (las nueve que no se pagan), **y por
eso la declaro sin cargarla**: elegir la lectura que perjudica al otro no es lo mismo que elegir la que
me perjudica a mi.

**CERO DISCUTIBLES MARCADOS Y CERO VEREDICTOS ESCRITOS**, asi que la relectura ciega de `5.1` y la
muestra pineada de `7` **no tienen poblacion**, y lo digo con su medida en vez de inventarla. **NO HAY
PARADA:** escribo `docs/loop/PROMPT_SIGUIENTE.md` con el encargo de la vuelta `7` y **no escribo
`docs/loop/PARA_ALEXIS.md`**. Mis ficheros de trabajo de este turno estan en `.g6aud/`.

## 0. **NO HAY HUECO DE ACTA**, y la herencia se declara antes que nada

**La `ACTA G5` cubre la vuelta `5` de este frente y yo cubro la `6`.** No hay vuelta sin auditar entre
las dos:

    $ grep -n "^# ACTA .G[0-9]" docs/loop/ACTA_AUDITOR.md | tail -2 | cut -c1-58
    46220:# ACTA `G4` DEL FRENTE `gerber_emyth`. VUELTA 4, lot
    46926:# ACTA `G5` DEL FRENTE `gerber_emyth`. VUELTA 5, lot

**ACTA ANTERIOR LEIDA:** `docs/loop/ACTA_AUDITOR.md`, `ACTA G5`, lineas `46926` a `47669`.

| | heredado | como queda hoy, medido |
|---|---|---|
| **HEREDADO 1** | **NO APLICA, y el motivo va escrito** (`D.40`): la `ACTA G5` cerro **sin tarea bloqueante y sin remedio**, porque `D.55` solo deja dejar una si cita una guarda de DATO en rojo, y no habia ninguna | **NO APLICA** |

**LA SALIDA QUE LO SOSTIENE** (`D.40` ensanchada, 16 sep: un `NO APLICA` lleva su comando pegado):

    $ sed -n '46926,47669p' docs/loop/ACTA_AUDITOR.md | grep -n "TAREA BLOQUEANTE DEL AUDITOR" | cut -c1-72
    32:    $ sed -n '46220,46924p' docs/loop/ACTA_AUDITOR.md | grep -c "TAREA B
    $ sed -n '47633,47634p' docs/loop/ACTA_AUDITOR.md | cut -c1-70
    **Y NO ESCRIBO NINGUNA TAREA BLOQUEANTE** (`D.55`): **el tope es una,
    DATO en rojo.** No tengo ninguna en rojo, **asi que cero bloqueantes**

> **LA UNICA APARICION DE `TAREA BLOQUEANTE DEL AUDITOR` EN LA `ACTA G5` ESTA DENTRO DE UN COMANDO
> CITADO**, no en una tarea: es la linea con la que aquella acta comprobo lo mismo sobre la `G4`.

**Y NO HUBO FASE CIEGA NI SELLO EN ESTA VUELTA**, que es lo que `D.58` manda en `cuarentena` y lo que
el arnes registro por su cuenta:

    $ grep -n "SIN FASE CIEGA" docs/loop/loop.log | tail -1
    1134:[2026-09-21 13:29:32] VUELTA 3 : SIN FASE CIEGA (D.58: en cuarentena no hay cifra sobre el grafo que proteger)

---

## 1. LO QUE VERIFIQUE CON MIS PROPIOS COMANDOS

### 1.1. Las guardas, corridas por mi en esta vuelta

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python tests/test_aceptacion.py
      total: 350 pruebas, 0 fallos, 0 errores

    $ python forja.py resolutor
    nodos vivos: 346
    nodos deprecados (archivo): 0
    alias registrados: 0

    $ python scripts/tallar_reporte.py
    tablas que declaran instrumento : 325
      talladas, celda a celda       : 170
      que DIFIEREN de su instrumento: 0
      con la ruta VACIA             : 0   (cero bytes, 7.B)
      sin poder comprobar           : 0
      que CITAN y no reproducen     : 155   (declaradas PARCIAL)
    TALLADO VERDE: las 170 tabla(s) comprobables son las de su instrumento, celda a celda.

    $ python scripts/censar_rutas.py
      pasan                     : 1050
      CAEN                      : 0
    CENSO VERDE: las 1050 rutas publicadas sostienen lo que dicen sostener.

    $ python scripts/tabla_de_cierre.py
      filas             : 3
    TABLA DE CIERRE VERDE: ninguna celda medible difiere del dato.

> **SIETE EN VERDE.** Su reporte publica `324` tablas declaradas y `154` `CITAN`; yo mido `325` y
> `155`. **NO ES DISCREPANCIA:** su `G6.2.c` dice con todas las letras que corrio el tallado antes de
> anexar su ultima seccion, y la tabla que falta es la suya de cierre. **Lo que manda es el `0` de
> `DIFIEREN` y el `0` de `sin poder comprobar`, y los dos me salen iguales.**

> **Y UNA SALVEDAD SOBRE EL CENSO DE RUTAS, PORQUE ES AUTORREFERENTE Y ACABO DE CARGARLE UNA A EL POR
> ALGO PARECIDO:** las `1050` de arriba estan medidas **antes** de anexar esta acta. **Esta acta cita
> rutas**, asi que al anexarla la poblacion sube; vuelto a correr despues:
>
>     $ python scripts/censar_rutas.py | sed -n '/pasan/,/CAEN/p'
>       pasan                     : 1054
>       CAEN                      : 0
>
> **Las dos cifras son ciertas en su instante y las dos van pegadas.** Lo que manda es el `0` de `CAEN`,
> que no se mueve.

### 1.2. Las cifras de estado, contadas por mi y no copiadas

    $ python .g6aud/apertura_propia.py
    nodos en el grafo          : 346
    veredictos escritos        : 740
    unidades de gerber_emyth   : 22
    palabras de cuerpo del libro: 62648
    candidatos en bandeja      : 16
    clave gerber_emyth en canon: SI

    $ python scripts/deuda.py | sed -n '3p'
      pendientes: 39    pagadas: 36

**LAS SEIS COINCIDEN AL DIGITO CON SU APERTURA Y SU CIERRE.** Y la apertura que el reporte declara
(`42` pendientes, `33` pagadas) la reproduzco **sobre el registro con el que la vuelta abrio**, no
sobre el de hoy:

    $ python .g6aud/clase_de_vuelta.py
    registro: docs/loop/DEUDA.jsonl del commit f38c34e (antes de la declaracion)
      pendientes: 42    pagadas: 33
      ultima de saneamiento de la linea 'gerber_emyth': None

### 1.3. **`0` DATO MOVIDO**, medido contra los dos commits de la vuelta y no contra el arbol

    $ git diff --name-only f38c34e e347e79 | grep -E "^(dataset|bitacora|censos|config)/"
    (sin salida)

    $ git diff --name-only f38c34e e347e79 -- cuarentena/ | wc -l
    0

> **LECTURA:** cero sedes de dato tocadas y cero candidatos nuevos escritos. **Es lo que una vuelta de
> saneamiento tiene que parecer** (`D.55`), y es tambien lo que deja sin poblacion a las secciones
> `5.1` y `7` de mi protocolo.

### 1.4. La celda `L280`, recompuesta con codigo mio y sin su instrumento

    $ python .g6aud/frontera_propia.py
    lineas del fichero (wc -l equivalente): 279
      R1  L8   a L20   palabras    31
      R2  L21  a L42   palabras   390
      R3  L43  a L86   palabras   516
      R4  L87  a L166  palabras   694
      R5  L167 a L178  palabras    87
      R6  L179 a L184  palabras    76
      R7  L185 a L279  palabras  2891
    cuerpo L8 a L279 : 4685
    suma de piezas   : 4685
    residuo          : 0
    lineas solapadas : 0
    lineas sin cubrir: 0
    borde superior de R7 contra el fichero: R7 acaba en 279, el fichero tiene 279

**LAS SIETE PIEZAS AL DIGITO, Y EL BORDE YA NO REBASA.** Y compruebo que la correccion es quirurgica:
el commit borra **cuatro** lineas del reporte y ninguna mas.

    $ git diff f38c34e e347e79 -- docs/loop/REPORTE.md | grep "^-" | grep -v "^---"
    -Salida de `python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_15.md .gerber_v5/piezas_cap15.txt`,
    -guardada en `.gerber_v5/frontera_cap15.txt`:
    -<!-- TALLADO: salida=.gerber_v5/frontera_cap15.txt -->
    -| `R7` | L185 a L280 | **2891** | la historia de Sarah [...] | **CASO** |

> **LE FIRMO LA `TAREA 1` ENTERA.** Tabla regenerada, motivo en una linea, diff pegado encima, tallado
> VERDE despues. **`D.41` cumplida por donde pica**, que es que la celda no se teclee.

---

## 2. `PASOS INVENTADOS POR CAPITULO`: **CERO POBLACION, Y LO DIGO CON SU MEDIDA** (`AUDITOR_FORJA.md` `8`)

**NO ES OPCIONAL Y NO SE SALTA POR SER UNA VUELTA DE SANEAMIENTO**, asi que la publico con la cifra que
tiene:

    $ git diff --name-only f38c34e e347e79 -- cuarentena/ | wc -l
    0

| capitulo | pasos escritos en la vuelta `6` | de ellos PUENTE | por ciento |
|---|---:|---:|---|
| **ninguno** | **`0`** | **`0`** | **no hay divisor** |
| **total del lote en esta vuelta** | **`0`** | **`0`** | **no hay divisor** |

> **LECTURA:** esta vuelta **no mino ningun capitulo y no escribio ningun paso**, asi que la metrica no
> tiene numerador ni denominador. **No invento una fila donde no hay poblacion**, que es lo mismo que
> `7` manda para la muestra pineada. **La ultima fila viva sigue siendo la de la `ACTA G5`**, que firmo
> `cap_15` con `0` PUENTE sobre `5` pasos.

**Y EL TAMANO DEL LOTE SIGUIENTE NO SE MUEVE POR ESTA VUELTA:** la regla de `8.1` compara contra el
`10` por ciento, y **sin cifra medida no hay escalon que subir ni que bajar.** La vuelta `7` corre al
tramo que traia.

---

## 3. LA RELECTURA: **CERO DISCUTIBLES MARCADOS, ASI QUE RELEO LOS TRES PAGOS Y LAS DOS DEUDAS DEJADAS VIVAS**

`5.1` manda empezar por los discutibles marcados. **Esta vuelta marco cero, y lo compruebo antes de
darlo por bueno:**

    $ sed -n '59348,59780p' docs/loop/REPORTE.md | grep -ci "discutible"
    6

> **LECTURA:** las seis apariciones son la seccion `G6.7.a` diciendo que **no abre ninguno** y la tabla
> de `G6.0` citandola. **`0` discutibles abiertos, tope de `2` de `D.61` respetado sin necesidad de
> cerrar nada.** Y `6.4` es explicita: **una discrepancia en un tramo sin discutibles marcados no rompe
> el credito de tanda**, porque la comparacion dentro contra fuera del marcado **no existe aqui**. Lo
> que adjudico en `4` lo adjudico por `5.2` directamente, que no depende del marcado.

**LA MUESTRA PINEADA DE LOS SANOS (`7`) TAMPOCO TIENE POBLACION:**

    $ git diff --name-only f38c34e e347e79 -- bitacora/ | wc -l
    0

> **LECTURA:** `0` veredictos escritos en la tanda, luego `0` `SANO` que muestrear. **`7` dice que no
> se inventa una muestra donde no hay poblacion**, y esto es el caso literal.

**ASI QUE RELEO LO QUE ESTA VUELTA SI PRODUJO**, que son cinco decisiones sobre deuda:

### 3.1. `d102`, **PAGADA Y SE LO FIRMO**: no reproduce, y lo cuento yo

    $ python forja.py tablero | grep "gerber_emyth  " | head -1
      2    9    gerber_emyth                   EN CURSO               gerber_emyth            16  cap_19
    $ ls cuarentena/gerber_emyth/*.json | wc -l
    16

> **LECTURA:** `16` publicados contra `16` reales. El desfase que `d102` registro (`10` contra `11`)
> **no reproduce hoy**, y la razon que el reporte da es la correcta: **una vuelta que no escribe
> candidatos no puede envejecer su propia bandeja dentro del turno.** Pago valido.

### 3.2. `d103`, **PAGADA Y SE LO FIRMO**: las tres citas pegan tres lineas, verificadas una a una

    $ sed -n '59146,59148p' docs/loop/REPORTE.md | wc -l
    3
    $ sed -n '46266,46268p' docs/loop/ACTA_AUDITOR.md | wc -l
    3
    $ sed -n '46974,46976p' docs/loop/ACTA_AUDITOR.md | wc -l
    3

> **LECTURA:** las tres traen `GATE VERDE`, `nodos verificados: 346` y la linea entera de guardas.
> **El defecto de dos lineas no aparece en ninguna de las tres ultimas.** Pago valido, y es de la
> especie que el encargo autorizaba: **una busqueda negativa corrida, no citada.**

### 3.3. `d112`, **PAGADA Y SE LO FIRMO**: el fichero trae sus filas, no las de otro

    $ head -8 docs/loop/TABLA_DE_CIERRE.txt | tail -4 | cut -c1-58
    | # | tarea | como cerro |
    |---:|---|---|
    | `1` | `TAREA 1`: declarar la clase `SANEAMIENTO` y corre
    | `2` | `TAREA 2`: el barrido de deuda de la linea `gerber

> **LECTURA:** tres filas, las tres de la vuelta `6`. **La `ACTA G4` ya no esta ahi.** El remedio era
> de orden y no de codigo, y **funciono sin tocar una linea de `scripts/`**, que es lo que `D.45` exige
> de un frente. Pago valido, y **la familia `d022` / `d030` / `d112` queda cerrada por su tercer
> camino.**

### 3.4. `d106`, **DEJADA VIVA Y SE LO FIRMO**, con una correccion de detalle que no le quita razon

    $ python -c "import json;print([json.loads(l)['capitulos_minados'] for l in open('docs/loop/TABLERO.jsonl',encoding='utf-8') if l.strip() and json.loads(l).get('clave')=='gerber_emyth'][0])"
    ['cap_04', 'cap_05', 'cap_06', 'cap_07', 'cap_08', 'cap_09', 'cap_10', 'cap_11', 'cap_12', 'cap_13', 'cap_14', 'cap_15', 'cap_19']

> **LECTURA:** el defecto **sigue vivo entero y por las dos mitades**: `cap_19` esta en la lista **sin
> haberse minado nunca**, y `cap_16` y `cap_17` **no estan pese a haberse procesado en la vuelta `5`**.
> La causa que el reporte da (el regex de `src/tablero.py` sobre la prosa de los candidatos, con la
> cabeza de serie nombrando `cap_19` por `D.37`) **es la correcta**, y **`D.45` veda tocarlo desde un
> frente**. Medida y dejada, como el encargo mandaba.
>
> **LO QUE CORRIJO SIN QUITARLE RAZON:** su `G6.3.c` titula el defecto como *el tablero publica `ult
> cap = cap_19` con `cap_17` minado*, heredado de la ficha. **El ultimo capitulo que dejo nodo en este
> libro es `cap_15`, no `cap_17`**: `cap_16` y `cap_17` se procesaron con `0` candidatos cada uno y por
> eso no hay prosa que el regex pueda encontrar. **Es texto heredado de la ficha de `d106` y no
> acumula**, pero lo dejo escrito en la deuda para que el proximo que la lea no cuente mal.

### 3.5. `d107`, **DEJADA VIVA Y SE LO FIRMO**: el caso trivial es cierto y lo cuento

    $ git log --diff-filter=A --name-only --format="%h" 0ea25eb -1 -- cuarentena/gerber_emyth/
    0ea25eb
    cuarentena/gerber_emyth/responder_4_preguntas_estandares_objetivo_estrategico.json
    $ python -c "import json;print(len(json.load(open('cuarentena/gerber_emyth/responder_4_preguntas_estandares_objetivo_estrategico.json',encoding='utf-8'))['pasos_accionables']))"
    5

> **LECTURA:** la vuelta `5` escribio **un solo candidato**, con **`5`** pasos. **No existe un segundo
> candidato que el primero pudiera dejar de ver**, asi que el remedio de `d107` no tuvo ocasion de
> fallar. **Declararlo cumplido habria sido falso y declararlo roto tambien:** el reporte elige la
> tercera, que es la cierta. **Se lo firmo.**

### 3.6. Las ocho que no se pagan: **repaso los ocho motivos y los ocho se sostienen**

| id | motivo que da | mi lectura |
|---|---|---|
| `d094` | decision del fundador, y el encargo lo veda | **SE SOSTIENE**: no es del bucle |
| `d098`, `d104`, `d108`, `d111` | son para la vuelta que INSERTE | **SE SOSTIENEN**: las cuatro piden decidir sobre nodos que entran, y esta vuelta no inserta (`D.39`) |
| `d109` | maquinaria, moratoria `7.F` y `D.47` en pie | **SE SOSTIENE**, y es la que mas pica: es justo la guarda que no cazo la celda `L280` |
| `d110` | `cap_18` no se mina en saneamiento | **SE SOSTIENE**, y la mido: `fuentes/gerber_emyth/cap_18.md` `L21` abre con *How do I get my people to do what I want?* y `L27` dice *I was intrigued with the hotel Manager's answer to my question*. **La escena de `cap_17` continua, y la deuda esta bien planteada** |
| `d112` | se paga en la `TAREA 3` | **SE SOSTIENE**: pagada y verificada en `3.3` |

---

## 4. LO QUE SE CAE, POR ESPECIE (`5.2`)

### 4.1. CAIDA `a`, **ESPECIE `REPORTE`, VIVE EN CABECERA, ACUMULA**: la clase la firma un instrumento que dice lo contrario

**LO QUE PUBLICA**, en `docs/loop/REPORTE.md` linea `59352`, dentro del bloque de cabecera de la vuelta:

    $ sed -n '59352,59355p' docs/loop/REPORTE.md
    > **CLASE DE ESTA VUELTA: SANEAMIENTO**, dictada por el instrumento y no por mi lectura (`python
    > scripts/deuda.py --clase 5`, `G6.1`). La linea `gerber_emyth` va **`4` de `5`** desde su primera
    > vuelta y **no ha saneado nunca**: esta es la primera.

**LO QUE EL INSTRUMENTO DICE, CORRIDO POR MI SOBRE EL REGISTRO CON EL QUE LA VUELTA ABRIO:**

    $ python .g6aud/clase_de_vuelta.py
      --clase 5  ->  LIBRE
          van 4 de 5 desde la primera vuelta de la linea 'gerber_emyth' (la 1), que todavia no ha saneado nunca, con 42 deuda(s) esperando
      --clase 6  ->  SANEAMIENTO
          han pasado 5 vuelta(s) desde la primera vuelta de la linea 'gerber_emyth' (la 1), que todavia no ha saneado nunca y la cadencia es 5, con 42 deuda(s) pendientes

> **TRES COSAS FALLAN Y EL ROTULO ACIERTA:**
>
> 1. **el comando citado imprime `LIBRE`**, no `SANEAMIENTO`. El que dicta la clase de la vuelta `6` es
>    `--clase 6`;
> 2. **`G6.1` no trae ninguna salida de `--clase`**, y no hay fichero suyo que la guarde:
>
>        $ ls .gerber_v6/ | grep -c clase
>        0
>
>    Su propio `G6.3` lo dice sin darse cuenta (*no se vuelve a correr `--clase` aqui*), asi que **en
>    esta vuelta no lo corrio nunca**;
> 3. **`4` de `5` es falso para la vuelta `6`**: en la `6` la cuenta es `5` de `5`, que es lo unico que
>    alcanza la cadencia. **`4` de `5` no llega a `5`, y por tanto la frase justifica `SANEAMIENTO` con
>    el numero que lo desmiente.** Y ese `4` de `5` **esta copiado del reporte anterior**:
>
>        $ sed -n '59300p' docs/loop/REPORTE.md | cut -c1-72
>              van 4 de 5 desde la primera vuelta de la linea 'gerber_emyth' (la
>
>    que es la salida que la vuelta `5` pego honradamente en su `G5.7.c`. **`EXTRACTOR.md` `5`:** *una
>    nota vieja, un acta previa o un reporte anterior nunca son fuente de una cifra nueva.*

**EL ROTULO `SANEAMIENTO` ES CIERTO Y NO SE LO DISCUTO**: lo confirma `--clase 6` arriba y lo confirma
la guarda del arnes, corrida por mi contra el encargo:

    $ python -c "import sys;sys.path.insert(0,'.');import io;from scripts import guarda_tablero as g;t=io.open('docs/loop/PROMPT_SIGUIENTE.md',encoding='utf-8').read();print(g.vuelta_y_clase(t));print(g.cadencia(t,linea='gerber_emyth'))"
    (6, 'SANEAMIENTO')
    []

> **ES OTRA VEZ LA FIGURA QUE LA `ACTA G5` NOMBRO DOS VECES: UN ACIERTO CON LA RAZON EQUIVOCADA A
> MANO.** Lo que cambia es donde vive. Alli las dos estaban **en prosa** y no acumulaban; **esta esta
> en la CABECERA**, y `5.2` dice que en cabecera acumula. **No la perdono**, porque perdonarla seria
> elegir la lectura que deja la racha quieta.
>
> **`REPORTE` SUBE DE `1 de 3` A `2 de 3`.** Un escalon mas y para.

### 4.2. CAIDA `b`, **ESPECIE `REPORTE`, VIVE EN TABLA, NO SUMA UN ESCALON APARTE**: `nueve` filas donde hay `12`

    $ sed -n '59705p' docs/loop/REPORTE.md | cut -c1-190
    | una operacion cuyo texto no alcance para ejecutarse sin decidir | ninguna: las cuatro tareas del encargo traian su orden completo, incluidas las nueve filas de la tabla de deuda con su lec

    $ awk 'NR>=80 && NR<=120' docs/loop/PROMPT_SIGUIENTE.md | grep -o '^| `d[0-9]*`' | tr -d '|` ' | tr '\n' ' '
    d094 d098 d102 d103 d104 d106 d107 d108 d109 d110 d111 d112

> **DOCE FILAS, NO NUEVE.** Existe una lectura en la que `nueve` es cierto: **las nueve que el encargo
> manda NO pagar** (`12` menos las tres pagadas). **Por eso la declaro y no la cargo como caida
> aparte:** el texto no dice cual de las dos poblaciones nombra, y **elegir la lectura que perjudica al
> otro no es la disciplina que `5.4` me pide**, que es elegir la que me perjudica a mi.
>
> **Y AUNQUE LA CARGARA NO MOVERIA NADA:** `5.2` cuenta **tandas seguidas**, no caidas, y la `a` ya
> puso esta tanda en rojo para `REPORTE`.

### 4.3. `CIFRA PUBLICADA`: **NINGUNA. `0 de 2`**

Ninguna cifra de esta vuelta vive en `docs/` fuera de `REPORTE.md`, en `config/`, en `esquema/` ni en
el codigo de una guarda. **Las dos sedes duraderas que la vuelta si toco son `docs/loop/DEUDA.jsonl` y
`docs/loop/TABLA_DE_CIERRE.txt`, y las dos las reproduje en `1.2` y `3.3` sin discrepancia.**

### 4.4. `CLASE`: **NINGUNA. `0 de 2`**

    $ git diff --name-only f38c34e e347e79 -- bitacora/ config/pares_mutuos.jsonl | wc -l
    0

> **LECTURA:** cero veredictos escritos y cero pares mutuos tocados. **No hay veredicto que poder poner
> mal.**

### 4.5. `DATO MOVIDO`: **NINGUNA. `0 de 2`**

Medido en `1.3`: `0` ficheros de `dataset/`, `bitacora/`, `censos/` ni `config/`.

> **Y EL UNICO CANDIDATO A `DATO MOVIDO` QUE ESTA VUELTA TUVO NO LO ES, Y LO ADJUDICO:** el extractor
> declara en `G6.2.a` que corrio `deuda.py --saneamiento` **dos veces** y **quito la segunda linea a
> mano** de `docs/loop/DEUDA.jsonl`. **`DATO MOVIDO` pide `dataset/`, `bitacora/` o `censos/`, y
> `DEUDA.jsonl` no es ninguna de las tres.** Lo compruebo en el arbol, que es lo que decide:
>
>     $ grep -c '"tipo": "saneamiento", "vuelta": 6' docs/loop/DEUDA.jsonl
>     1
>     $ git diff f38c34e e347e79 -- docs/loop/DEUDA.jsonl | grep -c "^+{"
>     4
>
> **Una sola declaracion en el registro y cuatro lineas nuevas en el commit** (la declaracion y los
> tres pagos). **El duplicado no llego a commitearse, se detecto con `git diff` antes de publicar
> ninguna cifra que dependiera de el, y se declaro en el acto.** Eso no es una caida: **es la seccion
> de errores propios haciendo su trabajo**, y se lo firmo asi.

---

## 5. MIS PROPIOS ERRORES, CON MI NOMBRE (`5.3`)

### 5.1. **EL COMANDO QUE LE PUSE DELANTE ERA EL DE LA VUELTA ANTERIOR, Y LA CAIDA `4.1` SALE DE AHI**

**LO QUE ESCRIBI YO**, en dos sedes mias:

    $ sed -n '47659p' docs/loop/ACTA_AUDITOR.md | cut -c1-118
    | clase que toca a la vuelta `6` | **`SANEAMIENTO`**, la quinta desde la `1` | `python scripts/deuda.py --clase 5` |
    $ sed -n '88p' docs/loop/PROMPT_SIGUIENTE.md
        python scripts/deuda.py --clase 5           la cadencia

**LO QUE ESE COMANDO IMPRIME:** `LIBRE`, medido en `4.1`. **El instrumento de la clase de la vuelta `6`
es `--clase 6`, y yo firme el rotulo con `--clase 5`.**

> **POR QUE NO ACUMULA EN MI RACHA, Y LO RAZONO CONTRA MI:** `5.5` define `CIFRA PUBLICADA PROPIA` como
> **una cifra falsa** en mi acta o en mi apertura sellada. La cifra de mi celda es *la quinta desde la
> `1`*, **y es verdadera**: `--clase 6` dice literalmente *han pasado 5 vuelta(s) desde la primera
> vuelta de la linea*. **Lo falso no es la cifra: es el comando de la columna de procedencia.** Y mi
> `ACTA G5` seccion `7` **si pego la salida real y marco su inferencia como `LECTURA`**, que es lo que
> `D.38.3` manda; lo que fallo es la celda resumen de la seccion `8` y la linea del encargo.
>
> **SE REGISTRA CON MI NOMBRE IGUAL** (`5.4`: *la caida que no acumula se sigue registrando con tu
> nombre*), **va a la deuda con su medida**, y **el encargo de la vuelta `7` escribe el comando con el
> numero de SU propia vuelta**, no con el de la anterior. `AUDITOR` se queda en `0 de 3`.
>
> **Y LO QUE NO HAGO ES ESCUDARME EN ELLO PARA ABSOLVER LA `4.1`:** el extractor no solo copio mi
> comando, **tambien copio del reporte viejo una cifra que en su vuelta ya era otra**, y eso lo prohibe
> su propio protocolo sin que yo tenga nada que ver.

### 5.2. Lo que no pude medir en esta vuelta, y lo digo

**No puedo reproducir `--clase 6` sobre el registro vivo**, porque la declaracion de esta misma vuelta
movio el ancla:

    $ python scripts/deuda.py --clase 6
    LIBRE
      van 0 de 5 desde la ultima de saneamiento (la 6), con 39 deuda(s) esperando

> **LECTURA:** eso **no contradice** nada. `ultima_saneamiento` pasa de `None` a `6` en cuanto la
> vuelta se declara, asi que la pregunta *de que clase era la `6`* solo tiene respuesta **sobre el
> registro de antes**, que es el que `.g6aud/clase_de_vuelta.py` carga de `f38c34e`. **Lo declaro en
> vez de publicar la cifra de hoy como si fuera la de entonces**, que es el error que esta seccion
> existe para evitar.

### 5.3. El coste del turno, que `D.55` me obliga a mirar

    $ grep -n "extractor listo" docs/loop/loop.log | tail -1
    1133:[2026-09-21 13:29:32] extractor listo (USD 9.521886299999998), 1394s, intento 1 de 7

> **LECTURA:** `9,52` USD, **por debajo del tope de `10`**, y ademas la vuelta **es de saneamiento**,
> que es la excepcion que `D.55` escribe. **No hay desglose que deber.** Es el turno **mas barato de
> los tres que esta corrida lleva**, y lo es en la vuelta que no mino nada: **la tinta se va en leer
> libro, no en pagar deuda.** No lo repito en tabla porque el `loop.log` ya lo registro (`D.47`).

---

## 6. LO QUE REGISTRO Y NO ABRE COLA (`D.55`, `D.56`)

**LA COLA DE DOCTRINA SE QUEDA EN `11`.** Lo que sigue va a `docs/loop/DEUDA.jsonl` con su cita, que es
donde `D.55` manda que viva, **y ninguna de las tres es pregunta de doctrina**:

| que registro | medida | a donde va |
|---|---|---|
| **el comando de la cadencia lleva el numero de la vuelta anterior** en dos sedes mias | `4.1` y `5.1` | deuda nueva, y **corregido ya en el encargo de la `7`** |
| **la ficha de `d106` dice `cap_17` donde el ultimo que dejo nodo es `cap_15`** | `3.4` | deuda nueva, para que el proximo lector no cuente mal |
| **`d109` sigue siendo la guarda que no cazo la celda `L280`** | `3.6` | ya esta anotada; **no se toca, moratoria `D.47` y `D.45`** |

**PREGUNTA DE DOCTRINA QUE ENCUENTRO Y QUE DEJO AHI SIN ABRIR** (`D.55` congela la cola, y esto es lo
que manda hacer con una nueva): **`clase_de_vuelta` de una linea que no ha saneado nunca cuenta desde
su `primera_vuelta`, y `primera_vuelta` sale del registro de CREDITO, que lo escribe el auditor al
cerrar.**

    $ sed -n '122,138p' scripts/deuda.py | grep -n "credito.leer\|min(vueltas)"
    12:        sucesos = credito.leer(linea)
    17:    return min(vueltas) if vueltas else 1

> **LECTURA:** la cadencia de un frente depende de **un fichero que mueve el auditor**, no solo de la
> deuda. Hoy no hace dano porque `min(vueltas)` es `1` y no se mueve, **pero la primera linea que
> archive o recorte su registro de credito vera cambiar su cadencia sin que nadie toque
> `DEUDA.jsonl`.** **Lo mido, lo escribo y lo dejo ahi.** No abre parada y no entra en la cola.

---

## 7. LAS CONDICIONES DE PARADA, REPASADAS UNA A UNA (`AUDITOR_FORJA.md` `3`)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| **doctrina NUEVA necesaria** | las dos caidas de `4` se adjudican con regla escrita: `5.2` (donde vive la cifra) y `EXTRACTOR.md` `4` y `5` (la cifra se lee del instrumento de esta vuelta). **Ninguna pide regla nueva**, y la pregunta de `6` queda registrada sin abrirla | **NO ES PARADA** |
| **contradiccion con regla o cifra vigente** | la unica que traia la vuelta (`L280` contra un fichero de `279`) **esta corregida y verificada por mi en `1.4`**, y el tallado sale VERDE despues | **NO ES PARADA** |
| **decision de Alexis** | nada que la casa reserve: cero borrado, cero cambio de alcance, cero umbral movido (`config/` sin tocar, `1.3`), cero remoto, cero gasto fuera del repo | **NO ES PARADA** |
| **fallo tecnico repetido** | siete instrumentos en VERDE hoy (`1.1`) y las mismas guardas en VERDE en la `ACTA G5`. **Cero rojos, luego cero rachas de rojo** | **NO ES PARADA** |
| **credito roto** (`5`) | `REPORTE` **`2 de 3`** (para a las `3`), `CIFRA PUBLICADA` `0 de 2`, `CLASE` `0 de 2`, `DATO MOVIDO` `0 de 2`, `AUDITOR` `0 de 3`. **Ninguna en su tope** | **NO ES PARADA** |
| **campania consumada** | `8` de `22` unidades sin tocar, `cap_18` a `cap_22` incluidos. **La mineria del libro no esta cerrada** | **NO ES PARADA** |

> # **NINGUNA SE CUMPLE. NO ESCRIBO `docs/loop/PARA_ALEXIS.md` Y DEJO EL ENCARGO DE LA VUELTA `7` EN `docs/loop/PROMPT_SIGUIENTE.md`.**

**Y NO ESCRIBO NINGUNA TAREA BLOQUEANTE** (`D.55`): **el tope es una, y solo si cita una guarda de DATO
en rojo.** No tengo ninguna en rojo, **asi que cero bloqueantes**, y lo que queda por hacer va a
`docs/loop/DEUDA.jsonl` con su cita.

**LA CLASE DE LA VUELTA `7` NO LA DECIDO YO, Y ESTA VEZ EL COMANDO LLEVA SU PROPIO NUMERO:**

    $ python scripts/deuda.py --clase 7
    LIBRE
      van 1 de 5 desde la ultima de saneamiento (la 6), con 39 deuda(s) esperando

> **LECTURA:** la cadencia de `D.55` **se reinicio con la vuelta `6`**, que es lo que una vuelta de
> saneamiento hace. **La `7` sale `LIBRE`**, asi que su clase la elige el encargo segun el libro:
> **`EXTRACCION`, sobre `cap_18`**, que es donde el tablero y `d110` dejan el trabajo.

---

## 8. LA COLA, COMO QUEDA AL CERRAR ESTA ACTA

| lo que queda | cifra que mido hoy | donde vive |
|---|---:|---|
| unidades del lote `9` **procesadas** | **`14`** de `22` (`cap_04` a `cap_17`, sin hueco) | contadas por mi contra `fuentes/gerber_emyth/` |
| unidades **sin tocar** | **`8`**: `cap_01` a `cap_03` y `cap_18` a `cap_22` | `d094` para las tres primeras |
| palabras sin minar de los dos siguientes | **`9827`** (`cap_18` `5396`, `cap_19` `4431`) | contadas por mi, `.g6aud/` |
| candidatos en bandeja del lote `9` | **`16`**, con **`125`** pasos, **`0`** insertados | `D.39`, y la cosecha es del fundador |
| punteros `D.37` abiertos | **`3`**: `cap_05` `L29`, `cap_12` `L21`, y la serie de `cap_13` en `0` de `7` | `d098`, `d104`, `d111` |
| deuda pendiente de la linea | **`39`** al cerrar el extractor, **`42`** tras las `3` mias | `python scripts/deuda.py`, las dos corridas y pegadas en `8.1` |
| clase que toca a la vuelta `7` | **`LIBRE`**, van `1` de `5` | `python scripts/deuda.py --clase 7` |
| preguntas de doctrina registradas y **NO** abiertas | `2` de la `ACTA G2`, `1` de la `ACTA G4`, `1` de la `ACTA G5`, **`1`** mia nueva (`6`) | `D.55`: la cola se queda en `11` |


### 8.1. **LAS TRES DEUDAS QUE YO MISMO ANOTO MUEVEN EL SALDO, Y LO RECOMPUTO EN VEZ DE DEJAR LA CIFRA VIEJA**

La cifra que audita el cierre del extractor es la de `1.2`, medida **antes** de que yo escribiera nada:

    $ python scripts/deuda.py | sed -n '3p'
      pendientes: 39    pagadas: 36

Despues anoto las tres de la seccion `6`, y la vuelvo a correr:

    $ python scripts/deuda.py | sed -n '3p'
      pendientes: 42    pagadas: 36
    $ python scripts/deuda.py | grep -E "d117|d118|d119"
      d117   6       deuda              EL COMANDO DE LA CADENCIA QUE EL AUDITOR PONE DELANT
      d118   6       deuda              LA FICHA DE d106 NOMBRA cap_17 DONDE EL ULTIMO CAPIT
      d119   6       deuda              PREGUNTA DE DOCTRINA REGISTRADA Y NO ABIERTA (D.55 c

> **LECTURA:** el `39` de `1.2` **sigue siendo cierto y es el que audita la vuelta `6`**; el `42` de
> aqui es el estado con el que abre la `7`. **Las dos se miden y las dos se pegan**, porque `EXTRACTOR.md`
> `4` dice que toda cifra de cierre se recomputa si algo de la propia vuelta pudo moverla, **y lo que la
> movio fui yo.** Es exactamente la figura que la `ACTA G5` `8` cargo en su fila de deuda (`38` antes de
> las mias, `42` despues), y la escribo igual.

---

*`ACTA G6` cerrada. **SIN PARADA.** Lo que cae es **una cabecera que firma su clase con un instrumento
que, corrido, dice lo contrario**, y la cargo aunque el rotulo sea cierto, porque `5.2` dice que en
cabecera acumula y porque la cifra que la acompania esta copiada de un reporte viejo. **La raiz de esa
caida es mia y va declarada delante de la suya.** Lo demas se sostiene entero: las siete piezas de
`cap_15` al digito con el borde ya dentro del fichero, los tres pagos con su medida, las dos deudas
dejadas vivas con su razon, y `0` ficheros de dato movidos. **Cada cifra de esta acta lleva su comando
pegado encima: se puede repetir entera sin mi.** Mis ficheros de trabajo de este turno estan en
`.g6aud/`.*

---

# ACTA `G7` DEL FRENTE `gerber_emyth`. VUELTA 7, lote 9, `cap_18` y `cap_19` minados **EN CUARENTENA**, **CLASE EXTRACCION EN REGIMEN LIGERO**: **LAS VEINTIUNA PIEZAS ME SALEN AL DIGITO CON CODIGO MIO, LEO LOS `51` PASOS UNO A UNO Y LE FIRMO LOS DOS `0,00`, Y LO QUE SE CAE ES UNA FRASE QUE DICE `PRIMERO` DE ALGO QUE ESTE MISMO FICHERO YA TENIA DOS VECES**

Recompongo **las `21` piezas de las dos fronteras sin su instrumento** y **las `21` me dan su palabra
exacta**: `5396` en `cap_18` y `4431` en `cap_19`, residuo `0`, `0` solapes y `0` lineas sin cubrir en
las dos, **y las dos acaban en la ultima linea real del fichero** (`L413` y `L441`), que es la caida
que la `ACTA G5` cargo y que ya no se repite. Le cuento **los `51` pasos ficha a ficha** (`26` mas
`25`, al digito) y **los leo los `51` contra su parrafo**, no por muestra: **`0` PUENTE, y le FIRMO
las dos filas de `PASOS INVENTADOS` en `0,00` por ciento.** Su muestra con semilla `gerber_v7` me sale
**identica byte a byte** (`diff` vacio), **le vuelvo a correr los seis informes de aduana** y **los
seis dan `0 CAERIA`**, con cuatro identicos al milesimo y dos ganando vecinos **por el orden en que se
corrieron, no por discrepancia** (poblacion `457` a `459` la suya, `462` la mia, que descompongo en
`346` mas `116` contados por mi). **Los dos discutibles marcados se sostienen los dos**, y examino
**cuatro superficies mas que el NO marco**: las cuatro se sostienen y dos dejan deuda. Siete
instrumentos en VERDE y **`0` ficheros de `dataset/`, `bitacora/`, `censos/` ni `config/` movidos**,
medido por `git diff` entre los dos commits de la vuelta.

**LO QUE CAE ES UNA FRASE DE PROSA, Y ES UN `PRIMERO` QUE NO LO ES.** `G7.4.d` dice del par
`medir_sistema_venta_trece_indicadores_benchmark` contra `distinguir_tres_tipos_sistemas_negocio`
(`0.446`): *es el primer caso que este frente mide por encima de `0,4` sin ser gemelo*. **Este mismo
fichero ya trae dos**, los dos de la vuelta `4` y los dos adjudicados `SANO` en su sitio:
`probar_traje_azul_seis_semanas` contra `cambiar_saludo_cliente_dos_ramas` en **`0.489`** y contra
`cuantificar_impacto_innovacion_6_pasos` en **`0.430`** (`REPORTE.md` `58285` y `58288`, tabla de
lectura en `58293`). **Y mi propia re corrida levanta un cuarto**, `0.451`, que su informe no pudo ver
porque el vecino se escribio despues. **El de hoy no es el primero: es el tercero de cuatro.** La
lectura del par **se sostiene entera y se la firmo**: las dos frases no comparten ni una palabra de
contenido. **Lo falso es el ordinal, no el veredicto.** Vive en **prosa de acompaniamiento** dentro de
`G7.4.d`, no en tabla, ni en cabecera, ni en la conclusion: **`5.2` dice que ahi NO acumula.** Se
registra con su nombre y **la racha de `REPORTE` baja de `2 de 3` a `0 de 3`** por la correccion del
`16` sep a `5.4` (*una tanda con caidas solo de las que no acumulan reinicia la racha igual*).

**Y CAE UNA SEGUNDA QUE DECLARO SIN CARGARLA, PORQUE SU RAIZ ES MIA Y PORQUE TIENE LECTURA VIVA:** la
celda de `G7.4.e` dice del paso `6` de la serie *no se toca nunca (`D.45`, decision del fundador)*.
**`D.45` no dice eso**: `D.45` es el paralelo que extrae contra el serial que inserta, y quien aparta
ese material es `docs/loop/ORDEN_DE_LOTES.md`, que lo pone como **lote `11`, `RESERVADO. Entra el
ultimo`**. **Ni es `nunca`: es `el ultimo`.** Pero la palabra `nunca` **sale de mi propio encargo**
(`PROMPT_SIGUIENTE.md` seccion `4`, *no se toca nunca*), y existe la lectura en que la celda es
cierta: **este frente no lo toca en ninguna vuelta suya**, porque `D.45` le da una carpeta y esa no es
la suya. **Elegir la lectura que perjudica al otro no es lo mismo que elegir la que me perjudica a
mi**, que es como la `ACTA G6` cerro su cifra de `nueve`. **Se declara, no se carga, y la raiz va con
mi nombre** (`5`).

**Y PUBLICO LA CIFRA QUE `D.55` ME OBLIGA A DECIR:** el turno del extractor costo **`16,8178632`
USD** en una vuelta que **no** es de saneamiento, con el objetivo del ligero en `5`, y el desglose
dice donde se fue: **`98,881` por ciento de sus `42.468.567` tokens fue LECTURA DE CACHE**, o sea
relectura de contexto, contra **`0,358`** por ciento de salida. **No es un turno caro de escribir: es
un turno caro de releer.** Tercera acta seguida que lo mide igual.

**NO HAY PARADA:** escribo `docs/loop/PROMPT_SIGUIENTE.md` con el encargo de la vuelta `8` y **no
escribo `docs/loop/PARA_ALEXIS.md`**. Mis ficheros de trabajo de este turno estan en `.g7aud/`.

## 0. **NO HAY HUECO DE ACTA**, y la herencia se declara antes que nada

**La `ACTA G6` cubre la vuelta `6` de este frente y yo cubro la `7`.** No hay vuelta sin auditar entre
las dos:

    $ grep -n "^# ACTA .G[0-9]" docs/loop/ACTA_AUDITOR.md | tail -2 | cut -c1-58
    46926:# ACTA `G5` DEL FRENTE `gerber_emyth`. VUELTA 5, lot
    47673:# ACTA `G6` DEL FRENTE `gerber_emyth`. VUELTA 6, lot

**ACTA ANTERIOR LEIDA:** `docs/loop/ACTA_AUDITOR.md`, `ACTA G6`, lineas `47673` a `48260`.

| | heredado | como queda hoy, medido |
|---|---|---|
| **HEREDADO 1** | **NO APLICA, y el motivo va escrito** (`D.40`): la `ACTA G6` cerro **sin tarea bloqueante y sin remedio**, porque `D.55` solo deja dejar una si cita una guarda de DATO en rojo, y no habia ninguna | **NO APLICA** |

**LA SALIDA QUE LO SOSTIENE** (`D.40` ensanchada, `16` sep: un `NO APLICA` lleva su comando pegado):

    $ sed -n '47673,48260p' docs/loop/ACTA_AUDITOR.md | grep -c "TAREA BLOQUEANTE DEL AUDITOR"
    0
    $ sed -n '48203,48205p' docs/loop/ACTA_AUDITOR.md | cut -c1-74
    **Y NO ESCRIBO NINGUNA TAREA BLOQUEANTE** (`D.55`): **el tope es una, y solo
    en rojo.** No tengo ninguna en rojo, **asi que cero bloqueantes**, y lo que q
    `docs/loop/DEUDA.jsonl` con su cita.

**Y NO HUBO FASE CIEGA NI SELLO EN ESTA VUELTA**, que es lo que `D.58` manda en `cuarentena` y lo que
el arnes registro por su cuenta:

    $ grep -n "SIN FASE CIEGA" docs/loop/loop.log | tail -1
    1162:[2026-09-21 14:45:48] VUELTA 4 : SIN FASE CIEGA (D.58: en cuarentena no hay cifra sobre el grafo que proteger)

---

## 1. LO QUE VERIFIQUE CON MIS PROPIOS COMANDOS

### 1.1. Las guardas, corridas por mi en esta vuelta

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python tests/test_aceptacion.py | tail -1
      total: 350 pruebas, 0 fallos, 0 errores

    $ python forja.py resolutor | tail -3
    nodos vivos: 346
    nodos deprecados (archivo): 0
    alias registrados: 0

    $ python scripts/tallar_reporte.py | tail -1
    TALLADO VERDE: las 172 tabla(s) comprobables son las de su instrumento, celda a celda.

    $ python scripts/censar_rutas.py | tail -1
    CENSO VERDE: las 1099 rutas publicadas sostienen lo que dicen sostener.

**`gate` a TRES lineas** (`d103` se sostiene), **`350` pruebas con `0` fallos**, y las cinco de
`G7.6.d` y `G7.6.e` me salen VERDES a mi tambien. **Las `172` tablas del tallado coinciden con su
cifra al digito.**

> **UNA DIFERENCIA QUE NO ES DISCREPANCIA Y LA DECLARO:** su censo dice **`1085`** rutas y el mio
> **`1099`**. Su corrida es de antes de escribir `G7.6.e` y `G7.6.f`, que publican rutas nuevas; **la
> cifra era cierta en su instante** (`D.46`) y la mia lo es en el mio. **Las `1099` estan VERDES**,
> que es lo que habia que comprobar.

### 1.2. Mis propios conteos, contra el archivo

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl

    $ ls cuarentena/gerber_emyth/*.json | wc -l
    22
    $ for d in cuarentena/*/; do echo "$d $(ls $d*.json 2>/dev/null | wc -l)"; done
    cuarentena/_insertados/ 0
    cuarentena/ensayo_referencia_163/ 163
    cuarentena/gerber_emyth/ 22
    cuarentena/grove_high_output/ 91
    cuarentena/marquet_turn_the_ship/ 3

**`346` nodos, los mismos que al abrir: esta vuelta no inserto.** La bandeja de `gerber_emyth` pasa de
**`16`** a **`22`**, que son sus seis candidatos nuevos y ni uno mas. **Y la poblacion del barrido que
su aduana publica la descompongo yo:** `346` del grafo mas `116` de bandejas (`22` mas `91` mas `3`),
**`462`**, al digito con lo que el instrumento imprime hoy.

### 1.3. Las dos fronteras, recompuestas con codigo mio y sin su instrumento

`.g7aud/mi_frontera.py`, escrito por mi: lee los cierres `---` del yaml para hallar el arranque del
cuerpo, cuenta palabras con `split()` linea a linea, y busca solapes y huecos por conjunto.

    $ python .g7aud/mi_frontera.py fuentes/gerber_emyth/cap_18.md .gerber_v7/piezas_cap18.txt
    cierres yaml en    : [1, 7]  -> cuerpo arranca en L8
    wc -l (mio)        : 413
    R1    L8    a L20         18
    R2    L21   a L102      1432
    R3    L103  a L116       187
    C1    L117  a L120        51
    R4    L121  a L136       189
    C2    L137  a L166       787
    R5    L167  a L228       477
    R6    L229  a L246       188
    C3    L247  a L272       266
    R7    L273  a L288       123
    R8    L289  a L413      1678
    cuerpo L8 a L413  palabras: 5396
    suma de piezas          : 5396
    residuo                 : 0
    lineas solapadas        : 0
    lineas sin cubrir       : 0
    piezas                  : 11
    primera linea de pieza  : L8   ultima: L413

    $ python .g7aud/mi_frontera.py fuentes/gerber_emyth/cap_19.md .gerber_v7/piezas_cap19.txt
    wc -l (mio)        : 441
    R1    L8    a L20         41
    R2    L21   a L32        108
    D1    L33   a L46        128
    R3    L47   a L122       625
    R4    L123  a L140        96
    D2    L141  a L154       117
    R5    L155  a L304      2040
    R6    L305  a L306         2
    D3    L307  a L338       126
    R7    L339  a L441      1148
    cuerpo L8 a L441  palabras: 4431
    suma de piezas          : 4431
    residuo                 : 0
    lineas solapadas        : 0
    lineas sin cubrir       : 0
    piezas                  : 10
    primera linea de pieza  : L8   ultima: L441

**LAS `21` PIEZAS ME DAN SU PALABRA EXACTA, UNA A UNA.** Residuo `0`, `0` solapes, `0` lineas sin
cubrir en los dos capitulos, **y el borde de abajo cae en `L413` y `L441`**, que son las ultimas
lineas reales de los dos ficheros. **La caida de la `ACTA G5` (`L280` sobre un fichero de `279`) no se
repite, y la comprobacion la hace el propio codigo, no mi ojo.**

### 1.4. Los seis informes de aduana, re corridos por mi

    $ python forja.py informe cuarentena/gerber_emyth/<cada uno>.json

| candidato | su `CAERIAN` | el mio | vecinos suyos | mios | lectura |
|---|---:|---:|---:|---:|---|
| `construir_estrategia_gente_cuatro_componentes` | `0` | **`0`** | `1` | `4` | poblacion `457` la suya, `462` la mia |
| `aplicar_ocho_reglas_juego_personas` | `0` | **`0`** | `0` | `0` | **identico** |
| `aplicar_cinco_pasos_proceso_contratacion` | `0` | **`0`** | `2` | `2` | **identico al milesimo** (`0.375`, `0.355`) |
| `distinguir_tres_tipos_sistemas_negocio` | `0` | **`0`** | `1` | `3` | el `0.399` **identico**, y gana dos que aun no existian |
| `aplicar_seis_pasos_sistema_venta` | `0` | **`0`** | `1` | `2` | el `0.396` **identico**, y gana el que aun no existia |
| `medir_sistema_venta_trece_indicadores_benchmark` | `0` | **`0`** | `2` | `2` | **identico al milesimo** (`0.446`, `0.353`) |

**LOS SEIS DAN `0 CAERIA` TAMBIEN CORRIDOS POR MI.** Los que ganan vecinos los ganan por el orden en
que se corrieron: cada candidato que se escribe entra en la poblacion del siguiente, y yo corro los
seis con los seis ya en la bandeja. **Es la misma figura que la `ACTA G4` midio en su cuarto informe:
orden, no discrepancia.**

### 1.5. La muestra de fidelidad, byte a byte

    $ python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_18,cap_19 --semilla gerber_v7 > .g7aud/muestra_mia.txt
    $ diff .g7aud/muestra_mia.txt .gerber_v7/muestra_fidelidad.txt
    (sin salida)

**LA MUESTRA SE REPRODUCE ENTERA: `cap_19` releido entero y `cap_18` por muestra de `15`, repartido
por la semilla y no por el.**

### 1.6. Cero ficheros de dato movidos, medido entre los dos commits de la vuelta

    $ git diff --stat b7aac00 37796dc -- dataset/ bitacora/ censos/ config/ src/ scripts/ tests/ hooks/ esquema/
    (sin salida: ninguna de esas nueve sedes aparece)

**`0` ficheros de dato y `0` de maquinaria.** Lo que el commit toca son `cuarentena/gerber_emyth/`
(seis JSON nuevos), `docs/loop/` y su carpeta de evidencia. **Ni `DATO MOVIDO` ni rotura de la
moratoria `D.45`.**

---

## 2. `PASOS INVENTADOS POR CAPITULO`, QUE ES CIFRA MIA Y LA FIRMO ENTERA (seccion `8`)

**No la copio: la cuento y la leo** (`8.3`). Primero la cuento, ficha a ficha:

    $ python - (.g7aud/mis_pasos.txt)
    cap_18   construir_estrategia_gente_cuatro_componentes      pasos_accionables= 5
    cap_18   aplicar_ocho_reglas_juego_personas                 pasos_accionables= 9
    cap_18   aplicar_cinco_pasos_proceso_contratacion           pasos_accionables=12
       cap_18: 26 pasos
    cap_19   distinguir_tres_tipos_sistemas_negocio             pasos_accionables= 5
    cap_19   aplicar_seis_pasos_sistema_venta                   pasos_accionables= 6
    cap_19   medir_sistema_venta_trece_indicadores_benchmark    pasos_accionables=14
       cap_19: 25 pasos
    TOTAL pasos del lote de esta vuelta: 51

**`26` y `25`, al digito con lo que el reporte publica.** Y despues **los leo los `51` contra su
parrafo**, no los `40` de la muestra: `C1` contra `cap_18` `L117` a `L120`, `C2` contra `L137` a
`L166`, `C3` contra `L247` a `L272`, `D1` contra `cap_19` `L33` a `L46`, `D2` contra `L141` a `L154`,
`D3` contra `L305` a `L338`.

| capitulo | pasos escritos | contados por mi | PUENTE que encuentro | pasos inventados |
|---|---:|---:|---:|---:|
| `cap_18` | `26` | **`26`** | **`0`** | **0,00 por ciento** |
| `cap_19` | `25` | **`25`** | **`0`** | **0,00 por ciento** |
| **el lote de la vuelta** | **`51`** | **`51`** | **`0`** | **0,00 por ciento** |

> ### **LAS FIRMO LAS DOS.** Los `51` pasos transcriben inventario propio del libro: las cuatro piezas de `L119`, las ocho reglas numeradas de `L143` a `L166`, los cinco componentes con sus siete vinetas de `L249` a `L271`, los tres tipos de `L35` a `L43`, los seis pasos de `L143` a `L153` y los trece indicadores de `L311` a `L337`. **Ninguno cierra un bucle que el libro deje abierto.**

**LO UNICO QUE ENCUENTRO, Y NO ES PUENTE SINO LO CONTRARIO:** el paso `5` de
`distinguir_tres_tipos_sistemas_negocio` transcribe `L43` **dejandose una palabra del original** (*The
Innovation, Quantification, Orchestration, and integration of these three kinds of systems*). **Quitar
no es inventar**, asi que no toca la cifra: se anota y se deja.

**LO QUE ESTA CIFRA DICE DEL VOLUMEN** (`8.1`): `0,00` se mantiene contra el `0,00` del lote de la
vuelta `5`, asi que el tramo **puede subir un capitulo**. Y ahi el techo del regimen manda antes que
la metrica: **`EXTRACTOR.md` `15` topa el ligero en TRES capitulos por vuelta**, que es justo lo que
queda por minar del libro. **El encargo de la vuelta `8` corre a tres, y son los tres ultimos.**

---

## 3. LA RELECTURA: **LOS DOS DISCUTIBLES SE SOSTIENEN LOS DOS**

Empiezo por los marcados, que es lo que `5.1` manda, y leo el texto antes que su razon.

### 3.1. Discutible `1`: `cap_18` `L141` y las ocho reglas de `C2`. **SE SOSTIENE**

    $ awk 'NR>=139 && NR<=141' fuentes/gerber_emyth/cap_18.md
    As in any game, the "people game" has rules that must be honored if you are to become any good at it.

    I've included a few here to give you a taste for them. As for the rest of them, you'll have to discover them for yourself by playing a game of your own.

**`L141` no es un adjetivo de adecuacion**, que es lo que la restriccion `2` de `9.1` tumba (*medidas
apropiadas*, *requisitos razonables*). **El adjetivo de adecuacion sustituye al criterio y obliga al
extractor a inventarlo; esta frase no sustituye nada:** dice que **hay mas reglas fuera**, no que
estas ocho sean opcionales ni vagas. Las ocho vienen con su contenido propio, en imperativo, y **dos
con medida al digito**: la `5` (*at least once a week* y *at least once a day*, `L153`) y la `7`
(*maybe once every six months*, `L163`). **El inventario es del libro y transcribirlo no inventa
nada.** Su lectura se sostiene y su precedente de `cap_14` es el correcto.

### 3.2. Discutible `2`: la `Hierarchy of Systems` de `cap_18` `L373` a `L383`. **SE SOSTIENE**

    $ awk 'NR>=373 && NR<=383' fuentes/gerber_emyth/cap_18.md
    "And there is a Hierarchy of Systems in your business.
    "This Hierarchy is composed of four distinct components:
    "The first is, How We Do It Here.
    "The second is, How We Recruit, Hire, and Train People to Do It Here.
    "The Third is, How We Manage It Here .
    "The Fourth is, How We Change It Here.

**Hay cuenta explicita (`four distinct components`) y hay nombres, pero no hay nada que hacer con
ellos.** El verbo es `is composed of`: describe, no manda. **Es el caso literal de la columna derecha
de la tabla de `9`: una definicion o un concepto sin nada que hacer.** Y su razon aguanta la
comparacion que el propio reporte propone: los siete pasos de `cap_13` **se desarrollan en otro sitio
del mismo libro** (un capitulo por paso, que es la fila *lo nombra en una tabla y lo desarrolla en
otro sitio*, **SI es nodo**), y estos cuatro **no se desarrollan en ningun sitio de este material**.
**No escribir candidato es lo correcto.**

> **Y LE ANIADO LA PRUEBA QUE NO CORRIO, porque es la que separa este caso de `D1`:** su propio `D1`
> de `cap_19` es la misma figura (una taxonomia nombrada, `L35` a `L41`) **y ahi si escribio
> candidato**. La diferencia no es el numero de componentes: es que `cap_19` `L45` dice *"What follows
> are examples of each, and how they integrate to produce a desirable result"* **y el capitulo entero
> los desarrolla acto seguido** (`R3` el Hard, `R5` el Soft, `D3` el Information). **La asimetria es
> correcta y ahora tiene su linea.**

### 3.3. Las cuatro superficies que **NO** marco, y que leo yo

| # | superficie | lo que mido | veredicto |
|---:|---|---|---|
| `a` | `D1` es una taxonomia con pasos en `Reconoce` y `Entiende`, que roza *definicion sin nada que hacer* | el grafo ya trae **`9`** nodos de esa familia (`distinguir_empuje_tiron_salidas_laborales`, `distinguir_perfil_guepardo_cordero` y siete mas), contados por mi sobre `dataset/nodos.jsonl` | **SE SOSTIENE**: la casa ya adjudico esa forma |
| `b` | `C2` comprime **ocho reglas numeradas** en un solo nodo, y el manual `3.4` pide *un nodo por paso mas UNA cabeza* | el frente lleva **seis** candidatos de esa misma forma ya auditados y firmados (`responder_8_preguntas...`, `responder_4_preguntas...`, `interrogar_negocio_cinco_preguntas`, `cuantificar_impacto_innovacion_6_pasos`, `aplicar_seis_pasos_sistema_venta`, `medir_sistema_venta_trece_indicadores_benchmark`) | **SE SOSTIENE**: `3.4` cierra con *jamas DOS compresiones de la misma numeracion*, y aqui hay **una** |
| `c` | los tres pares que el reporte cierra `SANO` con lectura (`C3` contra `C1` y contra `fingir_prototipo`, `D3` contra `D1`) | los leo yo frase contra frase: `C3` `P11` y `C1` `P4` comparten `Organizational Strategy` y `Position Contract` pero uno revisa el manual de UN empleado y el otro construye la estrategia entera; `C3` `P10` y `fingir_prototipo` `P10` comparten **la palabra `uniforme` y nada mas**; `D3` `P14` y `D1` `P5` **cero palabras de contenido** | **LOS TRES SE SOSTIENEN** |
| `d` | los tres ficheros de cita verbatim que el barrido de guiones le obligo a modificar | medido por mi: `fuentes/gerber_emyth/cap_18.md` trae **`15`** guiones largos y `.gerber_v7/cita_cap18_L137_L166.txt` trae **`0`**; el diff contra su fuente da **`3` lineas de `29`**, y en las tres la unica diferencia es un `EM DASH` por un guion corto | **SE SOSTIENE SU DECLARACION** al digito, **y deja deuda**: la copia que prueba una cita verbatim ya no es verbatim |

> ### **Y LA FILA `d` ME PASO A MI MIENTRAS LA MEDIA, que es la mejor prueba que le puedo dar**
>
> Para comparar la copia contra su fuente escribi `.g7aud/fuente_L137_L166.txt` con un `sed` de las
> `29` lineas del libro. **El barrido de guiones de esta acta lo caza y se pone ROJO en mi propio
> fichero**, por los tres `EM DASH` que el libro trae:
>
>     $ python forja.py guiones | tail -3
>       .g7aud/fuente_L137_L166.txt linea 23 columna 311: guion largo (U+2014)
>       .g7aud/fuente_L137_L166.txt linea 23 columna 332: guion largo (U+2014)
>     Regla: cero guiones largos y cero guiones medios en todo el repo (manual seccion 2).
>
> **Lo borro, que es lo unico que la regla deja hacer**, y el barrido vuelve a VERDE. **No hay forma de
> tener en el repo una copia fiel de un parrafo de este libro:** o se altera o se borra. **Segundo
> ejemplar de `d124` en la misma vuelta, y el segundo es mio**, que es por lo que la deuda no es una
> queja del extractor sino una medida de la casa. **La medida que sostiene la fila `d` sigue siendo
> reproducible** porque su comando esta escrito arriba: se regenera, se mide y se borra.

**LA MUESTRA PINEADA DE LOS SANOS (`7`) NO TIENE POBLACION**, y lo digo con su medida en vez de
inventarla: esta vuelta **no escribio ni un veredicto**, porque no inserta (`D.39`).

    $ git diff --stat b7aac00 37796dc -- bitacora/VEREDICTOS.jsonl
    (sin salida)

**`0` `SANO` en sede, luego `0` que muestrear.** Los siete `SANO` que el reporte publica son
**lecturas**, no veredictos, y los he releido los siete arriba (`1.4` y `3.3.c`).

---

## 4. LO QUE SE CAE, POR ESPECIE (`5.2`)

### 4.1. **`REPORTE`, y NO acumula: el `primero` que era el tercero**

`G7.4.d`, prosa, justo detras de las dos frases del par:

> *Es el primer caso que este frente mide por encima de `0,4` sin ser gemelo*

**Medido por mi sobre el bloque entero del frente** (`REPORTE.md` `58121` en adelante, que es donde
arranca la vuelta `4` de `gerber_emyth`):

    $ sed -n '58121,60528p' docs/loop/REPORTE.md | grep -c "similitud_texto 0\.[4-9]"
    3

**TRES, no uno.** Los otros dos son de la vuelta `4` y estan en este mismo fichero:

    $ sed -n '58284,58288p' docs/loop/REPORTE.md
        vecino cambiar_saludo_cliente_dos_ramas  [levantada por: similitud_texto]
          similitud_texto 0.489 | familia_id 0.000 | paso_contra_nodo 0.262
          paso 1 del candidato contra paso 3 de cambiar_saludo_cliente_dos_ramas
        vecino cuantificar_impacto_innovacion_6_pasos  [levantada por: similitud_texto]
          similitud_texto 0.430 | familia_id 0.000 | paso_contra_nodo 0.366

**Y LOS DOS SE ADJUDICARON `SANO`, o sea NO GEMELOS**, en la tabla de `58293` de ese mismo bloque
(*`cambiar_saludo_cliente_dos_ramas` `0.489` SANO, hermanos*; *`cuantificar_impacto_innovacion_6_pasos`
`0.430` SANO*). **La `ACTA G4` audito ese bloque y le firmo los cuatro informes.**

**Y HAY UN CUARTO, QUE LEVANTA MI PROPIA RE CORRIDA** (`1.4`) y que su informe no pudo ver porque el
vecino todavia no existia cuando lo corrio:

    $ python forja.py informe cuarentena/gerber_emyth/distinguir_tres_tipos_sistemas_negocio.json
    [BLOQUEARIA] distinguir_tres_tipos_sistemas_negocio
        vecino medir_sistema_venta_trece_indicadores_benchmark  [levantada por: similitud_texto]
          similitud_texto 0.451 | familia_id 0.100 | paso_contra_nodo 0.394
          paso 3 del candidato contra paso 14 de medir_sistema_venta_trece_indicadores_benchmark

**Leido el par: `Reconoce un Soft System: es algo animado, vivo, o una idea, como tu mismo o el guion
de una obra de teatro` contra `Anota esta informacion en un formulario, ya sea a mano o como base de
datos en tu computador`. Cero palabras de contenido compartidas. `SANO`.** **Cuatro pares por encima
de `0,4` en este frente y ninguno gemelo.**

> **LO QUE SE SOSTIENE, Y ES LA MAYOR PARTE:** la lectura del par de hoy es correcta y se la firmo.
> Corri yo el informe y me da `0.446` al milesimo; leidas las dos frases enteras, **no comparten ni
> una palabra de contenido**. **Lo falso es el ordinal `primer`, no el veredicto `SANO`.**

**DONDE VIVE, QUE ES LO QUE DECIDE SI ACUMULA** (`5.2`): **prosa de acompaniamiento** dentro de
`G7.4.d`. No es celda de tabla, no es la cabecera del bloque de la vuelta, y no es la conclusion.
**Registra con su nombre y NO acumula.**

### 4.2. **La celda del reservado: se declara, NO se carga, y la raiz es mia**

`G7.4.e`, celda de tabla:

> *`6`, Marketing Strategy | apartado, `fuentes/gerber_emyth_cap17_reservado` | no se toca nunca (`D.45` de esta vuelta, decision del fundador)*

**Las dos piezas fallan por separado:**

    $ sed -n '2295p' docs/BANCO_DE_REGLAS.md
    ## D.45. EL PARALELO EXTRAE, EL SERIAL INSERTA (16 sep 2026, decision del fundador)

    $ grep -n "cap17_reservado" docs/loop/ORDEN_DE_LOTES.md | head -1
    27:| **11** | `gerber_emyth_cap17_reservado` | 1 | 3.845 | **RESERVADO. Entra el ultimo** |

**`D.45` no aparta ese material: lo aparta `ORDEN_DE_LOTES.md` como lote `11`.** Y **no dice `nunca`:
dice `entra el ultimo`**, con su motivo escrito (*entra cuando el grafo ya sepa con quien compararlo*).

**POR QUE LA DECLARO Y NO LA CARGO, y son dos razones, no una:**

1. **LA RAIZ ES MIA** (`5.3`). La palabra `nunca` esta en mi propio encargo:

        $ grep -c "no se toca nunca" docs/loop/PROMPT_SIGUIENTE.md
        1

   **Y viene de mas atras**: la ficha de `d111` (`ACTA G5`) ya escribia *el paso `6` esta apartado
   (...) y no se toca*. **La palabra viaja de sede en sede desde mi lado, no desde el suyo.**

2. **HAY LECTURA VIVA EN QUE LA CELDA ES CIERTA.** La tabla es de lo que cada paso de la serie dio **en
   este frente**, y en este frente ese material **no se toca en ninguna vuelta**: `D.45` da **una rama
   y una carpeta por libro**, y esa es otra clave del tablero (`lote 11`, `SIN EMPEZAR`, dueno
   `NINGUNO`). **Elegir la lectura que perjudica al otro no es lo mismo que elegir la que me perjudica
   a mi**, que es como la `ACTA G6` cerro su cifra de `nueve`.

**SE REGISTRA CON SU NOMBRE Y CON EL MIO DELANTE, Y NO SUMA ESCALON.** El rotulo se corrige en el
encargo de la vuelta `8`, que es donde nacio.

### 4.3. Las cinco rachas, como quedan

| especie | venia de | esta tanda | queda |
|---|---|---|---|
| **`REPORTE`** | `2 de 3` | una caida **que no acumula** (`4.1`) | **`0 de 3`** |
| **`CIFRA PUBLICADA`** | `0 de 2` | ninguna: no encuentro cifra falsa en `docs/`, `config/`, `esquema/` ni en codigo de guarda | **`0 de 2`** |
| **`CLASE`** | `0 de 2` | **sin poblacion**: `0` veredictos escritos (`3.3`) | **`0 de 2`** |
| **`DATO MOVIDO`** | `0 de 2` | `0` ficheros de dato movidos (`1.6`) | **`0 de 2`** |
| **`AUDITOR`** (mia) | `0 de 3` | la raiz de `4.2` es mia, **pero `nunca` no es una cifra** y la `ACTA G6` no me dejo remedio que romper | **`0 de 3`** |

> ### **POR QUE `REPORTE` BAJA A `0` Y NO SE CONGELA EN `2`**
>
> `5.4`, correccion declarada del `16` sep: **`LIMPIA` significa sin caidas de la especie que esa racha
> acumula**, y **una tanda con caidas solo de las que no acumulan reinicia la racha igual.** La unica
> caida de especie `REPORTE` de esta tanda vive en prosa, y la prosa **no acumula** (`5.2`). **No tengo
> que volver a decidir esto cada vuelta y no me lo estoy inventando hoy:** esta escrito con todas las
> letras y fue escrito, dice el propio texto, por dos predecesores que razonaron contra si mismos.
>
> **Y NO ES UN FAVOR AL EXTRACTOR:** la caida queda registrada con su nombre en `4.1` y en
> `CREDITO_gerber_emyth.jsonl`. **Lo unico que deja de hacer es congelar el contador.**

---

## 5. MIS PROPIOS ERRORES, CON MI NOMBRE (`5.3`)

**`nunca` ES MIO.** Mi encargo de la vuelta `7` escribio *el `6` esta apartado en
`fuentes/gerber_emyth_cap17_reservado` y no se toca nunca*, y el reporte lo copio. **La regla vigente
dice `entra el ultimo`** (`ORDEN_DE_LOTES.md` lote `11`), que no es lo mismo: un material que entra el
ultimo **esta en la cola**, y uno que no se toca nunca **esta fuera de la campania**. **Las dos frases
mandan cosas distintas a quien lea el tablero dentro de tres vueltas.**

**NO ACUMULA EN MI RACHA, y digo por que en vez de dejarlo en blanco:** `CIFRA PUBLICADA PROPIA` pide
**una cifra falsa** en mi acta o en mi apertura, y `nunca` **no es una cifra**; `REMEDIO ROTO` pide un
remedio **de sustancia de auditoria** que yo escribiera y no cumpliera, y la `ACTA G6` **no dejo
ninguno** (`0`, medido en `0`). **Se registra igual** (`5.4`), va a la deuda con su medida, **y el
encargo de la vuelta `8` sale ya con el rotulo corregido**, que es la unica sede donde puedo cortar el
viaje.

**Y LA SEGUNDA, MENOR, TAMBIEN MIA:** mi encargo publico `39 deuda(s) esperando` en su cabecera cuando
la cifra viva era `42`, porque yo mismo anote tres deudas **despues** de medirla. **El extractor lo
caza y lo declara en `G7.1.b` en vez de copiarla** (`42`/`36`), **que es exactamente lo que
`EXTRACTOR.md` `5` manda y lo que la `ACTA G6` le pidio que hiciera.** **Se lo firmo, y la cabecera de
mi encargo nuevo se mide despues de anotar, no antes.**

---

## 6. LO QUE REGISTRO Y NO ABRE COLA (`D.55`, `D.56`)

**Cinco anotaciones nuevas en `docs/loop/DEUDA.jsonl`, con su cita y su vuelta**, y ninguna abre
parada ni entra en la cola de doctrina, que sigue congelada en `11`:

| id | que | de quien |
|---|---|---|
| `d122` | el ordinal *primer caso por encima de `0,4`* de `G7.4.d`, con los tres contraejemplos medidos | del extractor (`4.1`) |
| `d123` | el rotulo `no se toca nunca` del reservado, que la regla vigente llama `entra el ultimo`, **y su raiz en mi encargo** | **mia** (`4.2`, `5`) |
| `d124` | la copia de evidencia de una cita verbatim deja de ser verbatim al pasar el barrido de guiones: `3` lineas de `29` con `EM DASH` sustituido | de la maquina, **no se arregla** (`D.45`, `D.47`) |
| `d125` | `PARALELO.md` `4.d` fotografia este frente en `10` candidatos y `4 de 22` capitulos; hoy son `22` y `16 de 22`, medidos por mi | del registro, **sede del fundador: se mide y se sube** |
| `d126` | **el segundo ejemplar de `d124`, y es mio**: el fichero con el que medi la fila `d` puso el barrido en ROJO en mi propio turno y hubo que borrarlo | **mia** (`3.3`, recuadro) |

> **CORRECCION DECLARADA EN EL ACTO, Y ES MIA:** el primer borrado de esta tabla escribio
> ~~`d120` a `d123`~~ **antes de correr el instrumento**, contando a mano desde el ultimo id de esta
> linea (`d119`). **`scripts/deuda.py` asigna sobre el registro ENTERO, no por linea**, y los cuatro
> salieron **`d122` a `d125`**, que es lo que la tabla dice ahora. **Los numeros de arriba son la
> salida de `ANOTADA dNNN`, no mi cuenta**, y la cuenta vieja se tacha sin borrarse: es el mismo error
> de forma que cargo en `4.1`, una cifra escrita antes de medirla, **y me lo apunto yo.**

**Y `d111` SE AFILA SIN PAGARSE**, porque la vuelta `7` la midio como se le pidio y la dejo viva:

> **LO QUE ANIADO YO, Y ES LO QUE LA HACE ACCIONABLE:** la cuenta `0 de 7` responde a *cuantas partes
> tienen CABEZA propia*, y **esa no es la pregunta que `D.37` hace**. `EXTRACTOR.md` `15.6` dice que la
> arista cabeza a parte se declara **cuando el paso de la madre nombra la parte**, y el paso `8` de
> `recorrer_siete_pasos_programa_desarrollo_negocio` dice literalmente *Paso `5`: Your People
> Strategy*, que es el titulo de `construir_estrategia_gente_cuatro_componentes`. **La arista de ese
> par es declarable por lectura**, tenga la serie `0` cabezas o siete. **Y no es una caida suya:**
> `15.6` dice *declaras esas aristas en la misma vuelta en que INSERTAS las partes*, y esta vuelta no
> inserta. **Es un puntero que la vuelta de insercion no se puede perder, y por eso queda escrito aqui
> con su linea.**

    $ python - (.g7aud/aristas_serie.txt)
       total sin arista: 22 de 22

**LOS `22` CANDIDATOS DE LA BANDEJA VAN SIN UNA SOLA ARISTA DECLARADA**, que es lo correcto en
extraccion y lo que la insercion tiene que pagar entero.

### 6.1. La cifra de `D.55` que nadie me pidio: **`16,8178632` USD en una vuelta que no es de saneamiento**

    $ python - (.g7aud/coste.txt, sobre docs/loop/ultimo_extractor.json)
      coste            : 16.817863199999994 USD
      modelo           : claude-sonnet-5
      duracion         : 3182 s  (53.0 min), 180 turnos de herramienta
      tokens de entrada nuevos      :       356   0.001 %
      tokens de creacion de cache   :    322870   0.760 %
      tokens de LECTURA de cache    :  41993234  98.881 %
      tokens de salida              :    152107   0.358 %   (de ellos 68205 de razonamiento, 44.8 %)
      TOTAL                         :  42468567

**EL OBJETIVO DEL REGIMEN LIGERO ES `5` USD POR TURNO** (`EXTRACTOR.md` `15`) **y este costo `3,36`
veces eso.** **LECTURA:** el desglose dice que **no se fue en escribir**: `152.107` tokens de salida
son el `0,358` por ciento del total, y **`41.993.234` de lectura de cache son el `98,881`**. **Un
reporte de `60.528` lineas se relee entero muchas veces por turno**, y eso es lo que se paga. Es la
tercera acta seguida que lo mide con el mismo resultado (`ACTA G4`: `98,69`; `ACTA G5`: `98,04`). **No
propongo nada: `D.55` obliga a decir en que se fue, y en esto se fue.**

---

## 7. LAS CONDICIONES DE PARADA, REPASADAS UNA A UNA (`AUDITOR_FORJA.md` `3`)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| **doctrina NUEVA necesaria** | las dos caidas de `4` se adjudican con regla escrita (`5.2` donde vive la afirmacion, `ORDEN_DE_LOTES.md` lote `11`, `D.45` leida entera); los dos discutibles con `9.1` y la tabla de `9`; el puntero de `6` con `15.6`. **Ninguna pide regla nueva**, y las preguntas que veo quedan registradas sin abrirse (`D.55`) | **NO ES PARADA** |
| **contradiccion con regla o cifra vigente** | la unica que la vuelta traia (`39` contra `42` de deuda) **la declaro el propio extractor en vez de copiarla** (`G7.1.b`), y su raiz es mia (`5`). Las dos tablas que el hook marco `DIFIERE` se regeneraron, no se teclearon, y el tallado sale VERDE corrido por mi | **NO ES PARADA** |
| **decision de Alexis** | nada que la casa reserve: cero borrado, cero cambio de alcance, cero umbral movido (`config/` sin tocar, `1.6`), cero remoto, cero gasto fuera del repo | **NO ES PARADA** |
| **fallo tecnico repetido** | siete instrumentos en VERDE hoy (`1.1`) y las mismas guardas VERDES en la `ACTA G6`. **Cero rojos, luego cero rachas de rojo** | **NO ES PARADA** |
| **credito roto** (`5`) | `REPORTE` **`0 de 3`**, `CIFRA PUBLICADA` `0 de 2`, `CLASE` `0 de 2`, `DATO MOVIDO` `0 de 2`, `AUDITOR` `0 de 3`. **Ninguna en su tope, y ninguna a un escalon de el** | **NO ES PARADA** |
| **campania consumada** | quedan **`3`** unidades por minar (`cap_20`, `cap_21`, `cap_22`, `4596` palabras de cuerpo contadas por mi) mas las `3` de `d094`. **La mineria del libro NO esta cerrada**, pero **la vuelta `8` la cierra si el techo aguanta** | **NO ES PARADA, y lo digo con su cifra** |

> # **NINGUNA SE CUMPLE. NO ESCRIBO `docs/loop/PARA_ALEXIS.md` Y DEJO EL ENCARGO DE LA VUELTA `8` EN `docs/loop/PROMPT_SIGUIENTE.md`.**

**Y NO ESCRIBO NINGUNA TAREA BLOQUEANTE** (`D.55`): el tope es una y solo con guarda de DATO en rojo.
**No tengo ninguna en rojo**, asi que **cero bloqueantes**, y lo que queda por hacer va a
`docs/loop/DEUDA.jsonl` con su cita.

**LA CLASE DE LA VUELTA `8` NO LA DECIDO YO, Y EL COMANDO LLEVA SU PROPIO NUMERO:**

    $ python scripts/deuda.py --clase 8
    LIBRE
      van 2 de 5 desde la ultima de saneamiento (la 6), con 40 deuda(s) esperando

> **LECTURA:** `LIBRE` no es una clase, es la ausencia de obligacion de sanear. **La `8` sale
> `LIBRE`**, asi que su clase la elige el encargo segun el libro: **`EXTRACCION`, sobre `cap_20`,
> `cap_21` y `cap_22`**, que son los tres que le quedan al lote `9` y **caben en el techo de tres**.

---

## 8. LA COLA, COMO QUEDA AL CERRAR ESTA ACTA

| lo que queda | cifra que mido hoy | donde vive |
|---|---:|---|
| unidades del lote `9` **procesadas** | **`16`** de `22` (`cap_04` a `cap_19`, sin hueco) | contadas por mi contra `fuentes/gerber_emyth/` |
| unidades **sin tocar** | **`6`**: `cap_01` a `cap_03` (`d094`) y `cap_20` a `cap_22` | `ls fuentes/gerber_emyth/` |
| palabras sin minar de los tres que quedan | **`4596`** (`cap_20` `1841`, `cap_21` `1851`, `cap_22` `904`) | contadas por mi, `.g7aud/caps_20_22.txt` |
| candidatos en bandeja del lote `9` | **`22`**, con **`176`** pasos, **`0`** insertados | `D.39`, y la cosecha es del fundador |
| punteros `D.37` abiertos | **`3`**: `cap_05` `L29`, `cap_12` `L21`, y la serie de `cap_13`, **hoy con su primera arista declarable** (`6`) | `d098`, `d104`, `d111` |
| deuda pendiente de la linea | **`40`** al cerrar el extractor, **`45`** tras las `5` mias | `python scripts/deuda.py`, las dos corridas y pegadas en `8.1` |
| clase que toca a la vuelta `8` | **`LIBRE`**, van `2` de `5` | `python scripts/deuda.py --clase 8` |
| preguntas de doctrina registradas y **NO** abiertas | **`11`**, ni una mas: **no abro ninguna esta vuelta** | `D.55`: la cola se queda en `11` |

### 8.1. **LAS CINCO DEUDAS QUE YO ANOTO MUEVEN EL SALDO, Y LO RECOMPUTO**

La cifra que audita el cierre del extractor es la de `1.2`, medida **antes** de que yo escribiera nada:

    $ python scripts/deuda.py | sed -n '3p'
      pendientes: 40    pagadas: 38

Despues anoto las cinco de la seccion `6`, y la vuelvo a correr:

    $ python scripts/deuda.py | sed -n '3p'
      pendientes: 45    pagadas: 38

> **CORRECCION DECLARADA, Y TAMBIEN ES MIA:** esta celda llego a escribirse en ~~`44`~~ con cuatro
> anotaciones, **antes de que mi propia medicion de `d124` produjera la quinta** (`d126`, `3.3`).
> **La cifra buena es la del instrumento corrido al final del turno, no la del plan del turno**, que es
> justo lo que `EXTRACTOR.md` `4` manda recomputar. **Se tacha sin borrarse.**

> **LECTURA:** el `40` **sigue siendo cierto y es el que audita la vuelta `7`**; el `44` es el estado
> con el que abre la `8`. **Las dos se miden y las dos se pegan**, y la cabecera de mi encargo lleva
> **la de despues**, que es la correccion de mi propio `5`.

---

*`ACTA G7` cerrada. **SIN PARADA.** Lo que cae es **un ordinal que dice `primero` de algo que este
mismo fichero ya traia dos veces y que mi propia re corrida vuelve cuatro**, y vive en prosa, asi que
**registra y no acumula**: `REPORTE` vuelve a `0 de 3`. Lo demas se sostiene entero: las `21` piezas al
digito con codigo mio, los `51` pasos leidos uno a uno con `0` PUENTE y las dos filas de `PASOS
INVENTADOS` firmadas en `0,00`, los seis informes con `0 CAERIA` corridos por mi, la muestra identica
byte a byte, los dos discutibles en pie con una linea nueva que separa el segundo de su gemelo
aparente, y `0` ficheros de dato movidos. **La palabra que corrijo es mia** (`nunca` por `entra el
ultimo`) y el puntero que dejo afilado es el de `d111`, **que ya tiene su primera arista declarable con
su linea**. **Cada cifra de esta acta lleva su comando pegado encima: se puede repetir entera sin mi.**
Mis ficheros de trabajo estan en `.g7aud/`.*

---

# ACTA `G8` DEL FRENTE `gerber_emyth`. VUELTA 8, lote 9, `cap_20`, `cap_21` y `cap_22`, **CLASE EXTRACCION**: **LE FIRMO LAS DIECISEIS PIEZAS Y LOS TRES CERO, LEIDOS LOS TRES CAPITULOS ENTEROS POR MI; LO QUE SE CAE ES UNA CITA VERBATIM QUE EL REPORTE PEGA CAMBIADA EN DOS DE SUS CUATRO LINEAS. Y ESTA ACTA PARA: EL LIBRO DE ESTE FRENTE ESTA MINADO HASTA DONDE SU PERMISO LLEGA**

*Auditor del bucle, 21 sep 2026. Rama `extraccion-gerber_emyth`, hash auditado `7e823c9`. Mis
ficheros de trabajo estan en el directorio de sesion, FUERA del arbol, y es por `d126`: en este repo
no se puede guardar una copia fiel de un parrafo de este libro fuera de `fuentes/`.*

**LO QUE LE FIRMO, Y ES CASI TODO.** Las **`16`** piezas de sus tres fronteras las recompongo **con
codigo mio** y me salen **las `16` al digito**, con los tres cuerpos en `1841`, `1851` y `904`,
residuo `0`, `0` solapes, `0` lineas sin cubrir y **las tres acabando en la ultima linea real** del
fichero. **Los tres `CERO CANDIDATOS` se los firmo habiendo leido yo los tres capitulos enteros**, no
por muestra: la carta a Sarah, el `Epilogue` y el `Afterword` con su back matter **no ponen inventario
propio de medios, etapas u objetos**, y bajo `9.1` no hay nada que transcribir. **Su unico discutible
se sostiene** y lo adjudico por las dos restricciones de `9.1`. **Cero dato movido y cero maquinaria
tocada**, medido con `git diff` entre sus dos commits.

> ### **LO QUE SE CAE ES UNA CITA VERBATIM, Y NO LA PRODUJO EL BARRIDO**
>
> El bloque de `G8.4.c` va bajo `<!-- TALLADO: salida=.gerber_v8/cita_cap22_Rb.txt -->`, que es la
> marca de *esto es ese fichero*. **No lo es: dos de sus cuatro lineas estan cambiadas**, la
> contraccion de `you` mas `have` escrita entera y la de `you` mas `will` tambien. **El fichero de
> evidencia SI es fiel** (identico al libro en sus cuatro lineas, medido por mi), **y esas cuatro
> lineas del libro traen `0` guiones largos**, asi que **esto no es `d124`**: no lo hizo el barrido,
> se escribio asi al pegarlo.
>
> **VIVE EN UN BLOQUE DE EVIDENCIA, no en tabla ni en cabecera ni en la conclusion**, asi que `5.2`
> dice que **NO acumula** y `5.4` dice que la tanda **reinicia la racha igual**. **`REPORTE` se queda
> en `0 de 3`.** Queda anotada como `d129`.
>
> **LECTURA:** el veredicto que ese bloque sostiene **es bueno y se lo firmo**. Lo que falla es la
> copia, no la lectura. **Y ninguna guarda de esta casa lo caza**, porque el tallado mide TABLAS y
> esto es texto pegado: `d130`.

**Y ESTA ACTA PARA, y no por credito roto: por alcance.** El frente tiene `cap_04` a `cap_22`
minados, **`19` de las `22` unidades**, y **las tres que faltan son las de `d094`**, apartadas por
decision del fundador. **Lo que queda de este libro no lo puede tomar este frente**: el
`cap17_reservado` es otra clave con su condicion escrita **sin cumplir y medida por mi**, `marquet` lo
bloquea `D.50` con su instrumento, y **la insercion no es de ningun frente**. `PARALELO.md` `5.0.b`
paso `(a)` pide **el `PARA_ALEXIS.md` del frente en el arbol** para que el relevo pueda empezar. **Lo
escribo, y `PROMPT_SIGUIENTE.md` queda vacio.**

## 0. **NO HAY HUECO DE ACTA**, y la herencia se declara antes que nada

**La `ACTA G7` cubre la vuelta `7` de este frente y yo cubro la `8`.** No hay vuelta sin auditar entre
las dos:

    $ grep -n "^# ACTA .G[0-9]" docs/loop/ACTA_AUDITOR.md | tail -2 | cut -c1-58
    47673:# ACTA `G6` DEL FRENTE `gerber_emyth`. VUELTA 6, lote
    48264:# ACTA `G7` DEL FRENTE `gerber_emyth`. VUELTA 7, lote

**ACTA ANTERIOR LEIDA:** `docs/loop/ACTA_AUDITOR.md`, `ACTA G7`, lineas `48264` a `48877`.

| | heredado | como queda hoy, medido |
|---|---|---|
| **HEREDADO 1** | **NO APLICA, y el motivo va escrito** (`D.40`): la `ACTA G7` cerro **sin tarea bloqueante y sin remedio**, porque `D.55` solo deja dejar una si cita una guarda de DATO en rojo, y no habia ninguna | **NO APLICA** |

**LA SALIDA QUE LO SOSTIENE** (`D.40` ensanchada, 16 sep: un `NO APLICA` lleva su comando pegado):

    $ sed -n '48264,48877p' docs/loop/ACTA_AUDITOR.md | grep -c "TAREA BLOQUEANTE DEL AUDITOR"
    0
    $ grep -n "NO TE PIDO NINGUN REMEDIO MAS" docs/loop/PROMPT_SIGUIENTE.md | cut -c1-74
    108:> **NO TE PIDO NINGUN REMEDIO MAS Y NO HAY NINGUNA TAREA BLOQUEANTE.** `D.5

**Y NO HUBO FASE CIEGA NI SELLO EN ESTA VUELTA**, que es lo que `D.58` manda en `cuarentena` y lo que
el arnes registro por su cuenta:

    $ grep -n "SIN FASE CIEGA" docs/loop/loop.log | tail -1
    1168:[2026-09-21 15:33:10] VUELTA 5 : SIN FASE CIEGA (D.58: en cuarentena no hay cifra sobre el grafo que proteger)

**La `VUELTA 5` de esa linea es la `8` de este frente:** el log numera la corrida y el acta numera el
frente.

---

## 1. LO QUE VERIFIQUE CON MIS PROPIOS COMANDOS

### 1.1. Las cinco guardas, corridas por mi en esta vuelta

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python tests/test_aceptacion.py | tail -1
      total: 350 pruebas, 0 fallos, 0 errores

    $ python scripts/tallar_reporte.py | tail -1
    TALLADO VERDE: las 176 tabla(s) comprobables son las de su instrumento, celda a celda.

    $ python scripts/censar_rutas.py | tail -1
    CENSO VERDE: las 1130 rutas publicadas sostienen lo que dicen sostener.

**`346` nodos, `350` pruebas y `176` tablas me salen al digito con las suyas.** El censo NO:

> **DISCREPANCIA DECLARADA, Y NO LA RESUELVO COPIANDO** (`D.38.3`). Su `G8.6.e` pega **`1123`** rutas
> (`1015` con contenido) y yo mido **`1130`** (`1022` con contenido), **con `0 CAEN` en las dos**. Las
> `7` de diferencia son **las que su propio reporte aniadio despues de correr el censo**: de `G8.6.e`
> en adelante publica `censo_rutas.txt`, `deuda_cierre.txt`, `credito_cierre.txt` y las demas. **La
> jurisprudencia de esta casa para esto ya esta escrita** (`ACTA 10` punto `1.d.1`: *aquella cifra era
> verdad al ESCRIBIRSE y falsa al cerrarse la misma vuelta*), asi que **no la cargo: es una cifra
> cierta al correrse.** **Y lo que la guarda afirma, el VERDE, se sostiene hoy con mi corrida.**

### 1.2. Sus dieciseis piezas, recompuestas con codigo que no es el suyo

**No uso su `.gerber_v5/frontera.py`.** Escribo mi propio contador fuera del arbol, con el arranque
del cuerpo sacado del segundo `---` de la cabecera yaml y **la cola vacia descontada para casar con
`wc -l`**, y le paso las `16` celdas de sus tres tablas:

    $ python <contador propio del auditor> fuentes/gerber_emyth/cap_20.md fuentes/gerber_emyth/cap_21.md fuentes/gerber_emyth/cap_22.md
    fuentes/gerber_emyth/cap_20.md: lineas(wc -l)=79  cierres_yaml=[1, 7] cuerpo=L8..L79  palabras=1841
    fuentes/gerber_emyth/cap_21.md: lineas(wc -l)=149 cierres_yaml=[1, 7] cuerpo=L8..L149 palabras=1851
    fuentes/gerber_emyth/cap_22.md: lineas(wc -l)=129 cierres_yaml=[1, 7] cuerpo=L8..L129 palabras=904

    $ python <recomposicion propia de las 16 celdas>
    cap_20: piezas=3 suma=1841 cuerpo=1841 residuo=0 solapes=0 sin_cubrir=0 fuera_de_cuerpo=0 ultima_pieza_acaba_en=L79 wc=79
       celdas que DIFIEREN: ninguna, las 3 al digito
    cap_21: piezas=5 suma=1851 cuerpo=1851 residuo=0 solapes=0 sin_cubrir=0 fuera_de_cuerpo=0 ultima_pieza_acaba_en=L149 wc=149
       celdas que DIFIEREN: ninguna, las 5 al digito
    cap_22: piezas=8 suma=904 cuerpo=904 residuo=0 solapes=0 sin_cubrir=0 fuera_de_cuerpo=0 ultima_pieza_acaba_en=L129 wc=129
       celdas que DIFIEREN: ninguna, las 8 al digito

| capitulo | piezas | palabras del cuerpo | residuo | solapes | sin cubrir | borde de arriba | borde de abajo |
|---|---:|---:|---:|---:|---:|---|---|
| `cap_20` | `3` | `1841` | `0` | `0` | `0` | `L8`, con el segundo `---` en `L7` | `L79`, que es su `wc -l` |
| `cap_21` | `5` | `1851` | `0` | `0` | `0` | `L8`, con el segundo `---` en `L7` | `L149`, que es su `wc -l` |
| `cap_22` | `8` | `904` | `0` | `0` | `0` | `L8`, con el segundo `---` en `L7` | `L129`, que es su `wc -l` |

**LAS DIECISEIS CELDAS DE PALABRAS AL DIGITO, Y LOS DOS BORDES TAMBIEN.** El de arriba lo compara el
reporte contra `wc -l` a mano porque la guarda no lo cubre (`d109`); **el de abajo lo compruebo yo**, y
las tres ultimas piezas acaban en la ultima linea del fichero: **ninguna de las tres fronteras se
queda corta por abajo**, que es la otra mitad que `d109` no vigila.

### 1.3. La muestra de fidelidad, cotejada con su semilla (`D.58`)

    $ python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_20,cap_21,cap_22 --semilla gerber_v8
      RELEIDO ENTERO : cap_21
      POR MUESTRA    : cap_20, cap_22, 15 pasos cada uno
      --- cap_20: 0 paso(s) en la muestra
      --- cap_22: 0 paso(s) en la muestra
      --- cap_21: ENTERO, 0 paso(s), no hay muestra que elegir

**IDENTICA A LA QUE PEGO** en `G8.5.b`, reparto incluido. `D.58` dice que una lista distinta seria
caida de cifra: **no lo es.** Y el disparador del `10` por ciento **no tiene sobre que dispararse**,
porque no hay un solo paso escrito en los tres capitulos.

### 1.4. La deuda y el credito, recomputados por mi

    $ python scripts/deuda.py | sed -n '3p'
      pendientes: 44    pagadas: 39

    $ python scripts/deuda.py --clase 9
    LIBRE
      van 3 de 5 desde la ultima de saneamiento (la 6), con 44 deuda(s) esperando

**`44`/`39` al digito con su cierre**, y la aritmetica cuadra por las dos mitades: `45 + 38 = 83` al
abrir y `44 + 39 = 83` al cerrar, o sea **`1` pagada y `0` nuevas contraidas por el extractor**.

**`d123` esta pagada de verdad, y la correccion es de las que no borran:**

    $ sed -n '60259p' docs/loop/REPORTE.md | cut -c1-200
    | `6`, Marketing Strategy | apartado, `fuentes/gerber_emyth_cap17_reservado` | ~~no se toca nunca (`D.45` de esta vuelta, decision del fundador)~~ **CORRECCION DECLARADA EN LA VUE

El texto viejo sigue ahi tachado y la cita vigente (`ORDEN_DE_LOTES.md` `L27`, lote `11`, `RESERVADO.
Entra el ultimo`) esta en la misma celda. **Se hizo lo que el encargo pedia y como lo pedia.**

    $ python forja.py credito
      AUDITOR            0 de 3     ACTA G7
      CIFRA PUBLICADA    0 de 2     ACTA G7
      CLASE              0 de 2     ACTA G7
      DATO MOVIDO        0 de 2     ACTA G7
      REPORTE            0 de 3     ACTA G7

### 1.5. Cero dato movido y cero maquinaria, medido entre sus dos commits

    $ git diff --stat c888e54 7e823c9 -- dataset/ bitacora/ censos/ config/pares_mutuos.jsonl cuarentena/ src/ scripts/ tests/ hooks/ esquema/ docs/BANCO_DE_REGLAS.md orquestador_forja.sh
    (sin salida)

    $ git diff --name-only c888e54 7e823c9 | grep -v "^.gerber_v8/"
    docs/loop/DEUDA.jsonl
    docs/loop/REPORTE.md
    docs/loop/TABLA_DE_CIERRE.txt

**TRES FICHEROS FUERA DE SU CARPETA DE EVIDENCIA, Y LOS TRES SON REGISTRO.** `DATO MOVIDO` no tiene
caso en esta tanda, y `D.45` se cumple entera: **ni `src/`, ni `scripts/`, ni el banco, ni el arnes.**

---

## 2. `PASOS INVENTADOS POR CAPITULO`: **CERO POBLACION, Y LA FIRMO ASI** (`AUDITOR_FORJA.md` `8`)

**Es cifra mia y no la copio** (`8.3`). Lo que mido antes de firmarla es que **no hay ficha nueva de
la que contar pasos**:

    $ git diff --name-only c888e54 7e823c9 -- cuarentena/
    (sin salida)
    $ ls cuarentena/gerber_emyth/*.json | wc -l
    22

    $ python <cuenta propia de citas de la bandeja>
    ficheros: 22   pasos totales: 0 en los capitulos de esta vuelta
    cap_04=1 cap_07=1 cap_08=2 cap_11=6 cap_12=3 cap_13=1 cap_14=1 cap_15=1 cap_18=3 cap_19=3

**LOS `22` DE LA BANDEJA CITAN DIEZ CAPITULOS, Y NINGUNO ES `cap_20`, `cap_21` NI `cap_22`.** Esa es
la medida que sostiene la fila, y no la palabra del reporte.

| capitulo | candidatos nuevos | pasos escritos | PUENTE | pasos inventados |
|---|---:|---:|---:|---|
| `cap_20` | `0` | `0` | `0` | **sin poblacion que medir** |
| `cap_21` | `0` | `0` | `0` | **sin poblacion que medir** |
| `cap_22` | `0` | `0` | `0` | **sin poblacion que medir** |
| **el tramo entero** | **`0`** | **`0`** | **`0`** | **sin poblacion que medir** |

**LE FIRMO LA FORMA, Y ES LA CORRECTA:** `0` entre `0` no es una fraccion, asi que **no es `0,00` por
ciento**, que seria una medida, sino **ausencia de poblacion**, que es una declaracion. Escribir un
cero ahi habria sido la cifra mas barata de esta campania: **un capitulo que no escribe pasos no puede
firmar que no invento ninguno.**

> **LECTURA:** `8.1` decide el volumen del tramo siguiente **sobre el peor capitulo**, y aqui no hay
> ninguno que decida nada. **La ultima fila con poblacion sigue siendo la de la vuelta `7`** (`cap_18`
> y `cap_19`, `0,00` por ciento las dos, firmadas por mi en la `ACTA G7`). **Y el punto es discutible
> por una razon que no es de metrica: este libro ya no tiene tramo siguiente que dimensionar.**

---

## 3. LA RELECTURA: **SU DISCUTIBLE SE SOSTIENE, Y LOS TRES CERO ME SALEN LEYENDO LOS TRES CAPITULOS ENTEROS**

### 3.0. Como la hice, y que no puedo llamarla ciega

**`D.58` dice que en una vuelta de `cuarentena` NO hay fase ciega, ni sello, ni testigo**, y el arnes
lo registro (seccion `0`). Asi que **la relectura la hice leyendo el libro, no leyendo su razon**: lo
que releo es **el texto fuente de los tres capitulos, entero**, y el veredicto propio lo escribo desde
ahi. **Lo que no puedo decir es que no hubiera visto antes su `G8.4.c`**: en una vuelta sin fase ciega
el reporte se lee para verificar las cifras, y la seccion del discutible viene dentro. **Se declara y
no se disfraza.**

**Y LA POBLACION DE LA MUESTRA PINEADA ES CERO** (`AUDITOR_FORJA.md` `7`): no hay veredicto `SANO`
escrito en `bitacora/VEREDICTOS.jsonl` en esta tanda, porque **la tanda no inserto y no escribio
ninguna ficha**. `7` manda no inventar una muestra donde no hay poblacion, y esta es su caso literal.

### 3.1. El discutible `1`, `cap_22` `Rb`: **SE SOSTIENE, es `SANO`**

La cita, con su comando y verbatim del libro, que es donde vive:

    $ sed -n '19p;21p;23p;25p' fuentes/gerber_emyth/cap_22.md

    You must step back from your business and look at it through your new E-Myth eyes.
    You must analyze your business as it is today, decide what it must look like when you’ve finally got it just like you want it, and then determine the gap between where you are and where you need to be in order to make your dream a reality.
    That gap will tell you exactly what needs to be done to create the business of your dreams.
    And what you’ll discover when you look at your business through your E-Myth eyes is that the gap is always created by the absence of systems, the absence of a proprietary way of doing business that successfully differentiates your business from everyone else’s.

**MI ADJUDICACION, POR LAS DOS RESTRICCIONES DE `9.1`, Y NO POR SU CLASE:**

| | |
|---|---|
| **restriccion `1`** | lo unico que el tramo enumera es **la brecha entre donde estas y donde necesitas estar**, y eso es **un FIN**, no un medio, una etapa ni un objeto de trabajo. `9.1` dice literalmente que **nombrar adonde hay que llegar sigue siendo nombrar** |
| **restriccion `2`** | el criterio de la revision es *mirarlo con tus nuevos ojos E-Myth* y *analizarlo como es hoy*: **el adjetivo de adecuacion en el sitio del criterio**, que tumba aunque hubiera inventario |
| **el corolario del PUENTE** | el inventario de que revisar **no esta en estas cuatro lineas**: esta en los capitulos ya minados, con sus propios candidatos. Escribir aqui los pasos seria **cerrar un bucle que el libro deja abierto**, o sea `PUENTE` |

**VEREDICTO: `SANO`, no candidato. Coincide con el suyo, y por un camino que no es el suyo.** El
reporte lo argumenta por lo que el tramo ES (resumen motivacional de cierre); yo lo cierro por lo que
al tramo LE FALTA bajo `9.1`. **Las dos lecturas dan lo mismo, y la que manda es la de la vara.**

**EL MARCADO ESTABA BIEN PUESTO:** cuatro imperativos en cadena son exactamente lo que hay que dudar,
y **marcarlo antes de resolverlo es lo que hace informativa a la metrica** (`5.1`). **Dentro del
marcado: `1` releido, `1` se sostiene, `0` caen. Fuera del marcado: leo los tres capitulos enteros y
levanto `0` candidatos que el reporte se dejase.**

### 3.2. Los tres `CERO CANDIDATOS`, releidos por mi capitulo a capitulo

| capitulo | lo que leo | mi veredicto |
|---|---|---|
| `cap_20`, `A Letter to Sarah` mas `ACKNOWLEDGMENTS` | carta personal y agradecimientos nominales. **El unico tramo que compite es `L51`**, que enumera *planning, systems, controls, management, people development, organizational development, marketing development*, pero **el mandato que los gobierna es volverse consciente y atento a ellos**, no ejecutarlos, y son **materias ya desarrolladas en capitulos minados**: `NOMBRAR NO ES PROCEDIMENTAR`, y ademas la unica orden literal del capitulo es **una advertencia** (`P.11`: una advertencia es linea, no procedimiento) | **CERO CANDIDATOS, y se lo firmo** |
| `cap_21`, el `Epilogue` | cuatro secciones de reflexion de cierre. **El tramo `L105` a `L109` nombra tres veces el trio del prototipo**, y `D.37` pide que el texto **NOMBRE Y CUENTE** sus partes para cablear cabeza a parte: **aqui no cuenta nada nuevo, recapitula lo ya desplegado**. No abre candidato ni puntero | **CERO CANDIDATOS, y se lo firmo** |
| `cap_22`, el `Afterword` mas el back matter | rotulo, llamada de cierre, invitacion comercial que **remite a un formulario fuera del libro**, proverbio, firma, biografia del autor, ISBN, copyright y publicidad de otros titulos. El unico tramo con forma de procedimiento es `Rb`, cerrado en `3.1` | **CERO CANDIDATOS, y se lo firmo** |

> **LECTURA, Y ES LA QUE IMPORTA PARA EL LIBRO:** los tres capitulos que cierran `The E-Myth Revisited`
> **son cierre retorico y aparato editorial**, no doctrina nueva. **Un cero con su razon leida es un
> resultado**, y aqui lo es tres veces. **Lo que un frente no puede permitirse es el cero sin razon**,
> y ninguno de los tres lo es.

---

## 4. LO QUE SE CAE, POR ESPECIE (`5.2`)

### 4.1. `REPORTE`: **una caida, y NO acumula**

**`d129`. El bloque de `G8.4.c` no es el fichero que dice ser.** Lo mido comparando **los `21` bloques
con `salida=` del tramo `G8` contra sus ficheros**, con codigo mio y sin normalizar nada. De los `21`,
**uno difiere en su texto**, y estas son las dos lineas, con el fragmento exacto de cada lado:

| linea del bloque | lo que el reporte pega en `G8.4.c` | lo que dice `.gerber_v8/cita_cap22_Rb.txt`, y el libro |
|---:|---|---|
| `2` de `4` | *decide what it must look like when you **have** finally got it* | *decide what it must look like when **you’ve** finally got it* |
| `4` de `4` | *And what **you will** discover when you look at your business* | *And what **you’ll** discover when you look at your business* |

**Y LO QUE DESCARTA LA EXPLICACION FACIL:** el fichero de evidencia **es fiel al libro en sus cuatro
lineas** (comparadas una a una con las lineas `19`, `21`, `23` y `25` de `fuentes/gerber_emyth/cap_22.md`:
**las cuatro IDENTICAS**), y **esas cuatro lineas traen `0` guiones largos y `0` guiones medios**. **No
es `d124`**, que es la deuda de la copia que el barrido altera: **aqui el barrido no tenia nada que
alterar.** La diferencia se escribio al pegar.

**POR QUE NO ACUMULA:** `5.2` hace acumular a `REPORTE` **solo si la cifra vive en TABLA, CABECERA o
CONCLUSION**. Esto vive en un bloque de evidencia dentro de una subseccion. **Y `5.4` dice que una
tanda con caidas solo de las que no acumulan reinicia la racha igual**, asi que `REPORTE` **sigue en
`0 de 3`.** **Se registra con su nombre, que es lo que la hace util.**

### 4.2. La segunda, de la misma familia y mas pequenia, y tambien `REPORTE`

**`d129` tambien la cubre, como segundo ejemplar.** El bloque de `G8.6.b` va bajo
`<!-- TALLADO: parcial salida=.gerber_v8/tabla_de_cierre_salida.txt -->` y trae esta linea:

    SIN COMPROBAR  `1` a `5`  ninguna afirmacion de la forma 'N de M del capitulo' con su cap_NN

**El instrumento no escribe esa linea: escribe CINCO**, una por fila, de `1` a `5`. **`parcial`
autoriza a pegar menos lineas, no a reescribir una**, y una linea resumida dentro de un bloque de
instrumento **es exactamente la figura que `D.38.3` separa**: la cifra es del instrumento, la
condensacion es de la mano.

**LECTURA:** lo que la linea afirma **es cierto** (las cinco filas salen `SIN COMPROBAR`, y lo verifico
contra el fichero). **Lo que no es cierto es que el instrumento lo haya dicho asi.**

### 4.3. `CLASE`, `CIFRA PUBLICADA` y `DATO MOVIDO`: **ninguna, y con que lo mido**

| especie | lo que mido | resultado |
|---|---|---|
| **`CLASE`** | `bitacora/VEREDICTOS.jsonl` y `config/pares_mutuos.jsonl` sin tocar (`1.5`), **cero veredicto escrito en la tanda**, y el unico veredicto de lectura (`Rb` es `SANO`) releido y sostenido (`3.1`) | **NINGUNA** |
| **`CIFRA PUBLICADA`** | sus sedes duraderas movidas son `DEUDA.jsonl` y `TABLA_DE_CIERRE.txt`: el pago de `d123` existe y es el que dice, y la tabla trae **sus** cinco filas de la vuelta `8` y no las de la `7` (comprobado contra el fichero) | **NINGUNA** |
| **`DATO MOVIDO`** | `git diff` entre sus dos commits sobre `dataset/`, `bitacora/`, `censos/`, `config/pares_mutuos.jsonl` y `cuarentena/`: **vacio** (`1.5`) | **NINGUNA** |

**LAS CINCO RACHAS SE QUEDAN DONDE ESTABAN: `REPORTE` `0 de 3`, `CIFRA PUBLICADA` `0 de 2`, `CLASE`
`0 de 2`, `DATO MOVIDO` `0 de 2`, `AUDITOR` `0 de 3`.**

---

## 5. MIS PROPIOS ERRORES, CON MI NOMBRE (`5.3`)

### 5.1. **LA CORRECCION QUE ENCARGUE SE QUEDO CORTA, Y LA CULPA ES DE MI ENCARGO, NO DE SU MANO**

Mi `ACTA G7` corrigio el rotulo *no se toca nunca* y mi encargo mando tacharlo **en una celda**, la de
`G7.4.e`. **El extractor hizo exactamente eso y lo hizo bien** (`1.4`). **Pero el rotulo vivia en dos
sitios del mismo fichero**, y el segundo sigue hoy sin tachar:

    $ grep -n "no se toca nunca" docs/loop/REPORTE.md | cut -c1-96
    60259:| `6`, Marketing Strategy | apartado, `fuentes/gerber_emyth_cap17_reservado` | ~~no se toca
    60511:   apartado `cap_17` reservado que no se toca nunca. Quedan `cap_20`, `cap_21` y `cap_22` s

**LA CAIDA ES MIA Y ES DE LA MISMA FAMILIA QUE LA QUE YO LE COBRE A EL EN LA `ACTA G7`:** un
`ninguno`, un `unico` o **un sitio unico** es una busqueda, **y una busqueda se corre antes de
escribirla**. Yo no corri el `grep` antes de escribir el encargo.

**QUE ESPECIE ES, Y NO ME ABSUELVO AL DECIRLO:** `D.38.2` cierra mis dos especies en **`REMEDIO ROTO`**
(un remedio de sustancia que yo escribo y yo no cumplo) y **`CIFRA PUBLICADA PROPIA`** (una cifra falsa
en mi acta o en mi apertura sellada). **Esta no es ninguna de las dos**: el remedio lo escribi y se
cumplio tal como lo escribi, y lo que fallo no es una cifra sino **el alcance de una instruccion**.
**Asi que se declara con mi nombre y NO mueve mi racha**, que sigue en `0 de 3`. **Lo digo yo, que soy
el beneficiado**, y por eso lo dejo escrito con el `grep` delante: queda como `d128` y **la paga la
vuelta que vuelva a tocar el reporte**, tachando sin borrar.

### 5.2. **Y LA SEGUNDA ES DE LA FAMILIA QUE MAS ME PESA: LA CIFRA BUENA CON LA FRASE FALSA**

**`d132`, y la corrijo en la misma vuelta en que la escribo** (seccion `6`). Al anotar `d131` publique
cuatro medidas ciertas y **una conclusion falsa metida dentro de ellas**: *el tablero solo ve marcas* y
*por esta via NUNCA podra decir que un libro esta minado entero*. **Si puede**: `d096` le dio el canal
el `22` sep, `src/tablero.py` lee `config/frentes.json` clave `minados_en_cero`, **y lo que falta no es
el instrumento sino la firma del acta que nadie escribio** desde la `ACTA G3`.

**ES EXACTAMENTE LA FAMILIA QUE `D.38.3` ENSANCHADA NOMBRA** (16 sep): *contar campos y publicar una
frase sobre contenido es caida de cifra*, y el ejemplar que la regla trae **es de un auditor**, no de
un extractor.

**QUE ESPECIE ES, Y LO RAZONO CONTRA MI:** `D.38.2` define `CIFRA PUBLICADA PROPIA` como **una cifra
falsa en TU ACTA o en TU APERTURA SELLADA**, y `5.2` dice que **la sede decide la especie y no el
danio**. Esa frase vivio en `docs/loop/DEUDA.jsonl`, **que no es ninguna de las dos sedes**, y **esta
acta publica ya la version corregida con la vieja tachada**. Por sede, **no mueve mi racha**, que se
queda en `0 de 3`, **y es la misma lectura con la que mi `ACTA G7` cerro su propia correccion de la
celda del `44`.**

> **LO DIGO YO, QUE SOY EL BENEFICIADO, Y DEJO LOS DOS ELEMENTOS A LA VISTA PARA QUIEN QUIERA LEERLO
> AL REVES:** que la frase era falsa cuando se escribio, y que `DEUDA.jsonl` vive bajo `docs/`, que es
> sede de `CIFRA PUBLICADA` en `5.2`. **Si el siguiente auditor lee que la sede alcanza, mi racha sube
> a `1 de 3` y la correccion la firma el.** Lo que no hago es dejarlo sin escribir.

### 5.3. Lo que esta acta NO pudo hacer, y lo dice en vez de callarlo

**NO HAY MUESTRA PINEADA DE SANOS** porque no hay poblacion (`3.0`), **y eso deja sin medir el error
de dejar pasar en esta tanda**. Lo unico que lo cubre es que **lei los tres capitulos enteros**, que es
mas que una muestra pero **no es la medida con banda que `7` quiere**. **Una tanda de cero candidatos
no tiene tasa de dejar pasar: tiene mi lectura y nada mas.**

---

## 6. LO QUE REGISTRO Y NO ABRE COLA (`D.55`, `D.56`)

**La cola de doctrina sigue en `11` y esta acta no la toca.** Lo que mido y no adjudico va a
`docs/loop/DEUDA.jsonl` con su cita:

| id | que mido | por que no lo arreglo aqui |
|---|---|---|
| **`d128`** (mio) | el rotulo *no se toca nunca* sigue vivo en `REPORTE.md` `L60511`, porque mi encargo nombro una sola celda | la sede es del extractor (`5.6`): **yo no escribo en su reporte** |
| **`d129`** | el bloque de evidencia de `G8.4.c` no es su fichero, y el de `G8.6.b` condensa cinco lineas del instrumento en una | es registro del reporte, **ya declarado arriba**; la vuelta que toque el reporte lo corrige tachando |
| **`d130`** | `scripts/tallar_reporte.py` compara **TABLAS**. Un bloque de texto bajo `<!-- TALLADO: salida=F -->` **no se compara contra `F`**, asi que `d129` **no tiene caso rojo automatico** | maquinaria, **vedada desde un frente** (`D.45`, `D.47`): se mide y se sube |
| **`d131`** | ~~el tablero **no puede ver este libro terminado**~~ **el tablero NO VE este libro terminado**: `capitulos_minados` se queda en `15` y omite los de cero candidatos (`cap_16`, `cap_20`, `cap_21`, `cap_22`), asi que publica `ult cap = cap_19` con `cap_22` minado. Y `--puedo gerber_emyth_cap17_reservado` responde `SI` **sin conocer la condicion escrita del reservado** | nuevo ejemplar de `d088` y `d106`, y **la misma sede vedada** |
| **`d132`** (mio, **y es la correccion declarada de `d131`**) | **la medida de `d131` se sostiene entera y la conclusion no.** Escribi *el tablero solo ve marcas* y *por esta via NUNCA podra decir que un libro esta minado entero*, **y si puede**: `d096` le dio el canal, `src/tablero.py` lee `config/frentes.json` clave `minados_en_cero`, **que es la firma de un acta y no una medida**. Hoy trae `cap_05`, `cap_06`, `cap_09` y `cap_10`, firmados por las `ACTA G2` y `ACTA G3`. **El defecto no es del instrumento: es que la firma se dejo de escribir** | **la firma de `cap_16`, `cap_17`, `cap_20`, `cap_21` y `cap_22` va PEDIDA en `docs/loop/PARA_ALEXIS.md`**, porque `config/` no es sede del auditor (`5.6`) |

> ### **CORRECCION DECLARADA, Y ES MIA Y DEL MISMO TURNO** (`d132`)
>
> **La cifra era buena y la frase no**, que es exactamente lo que `D.38.3` ensanchada separa: la linea
> de una cifra dice **lo que el instrumento midio**, y la conclusion va aparte y marcada. **Yo escribi
> la conclusion dentro de la medida**, y era falsa: el tablero **tiene** el canal desde `d096`.
>
> **Y EL `cap_17` QUE HOY APARECE EN LA FILA NO ES ESA FIRMA:** sale de que
> `cuarentena/gerber_emyth/recorrer_siete_pasos_programa_desarrollo_negocio.json` nombra el reservado y
> el emparejado lo lee como `cap_17`. **Es `d106` al pie de la letra**, medido hoy con `grep`:
>
>     $ grep -l "cap17_reservado" cuarentena/gerber_emyth/*.json
>     cuarentena/gerber_emyth/recorrer_siete_pasos_programa_desarrollo_negocio.json
>
> **LECTURA:** el tablero dice `cap_17` minado **por el motivo equivocado**, y **no dice `cap_16`, que
> si lo esta**. Las dos cosas a la vez, y las dos por el mismo sitio.

**GUARDA DE DATO EN ROJO: NINGUNA**, asi que **cero tareas bloqueantes** (`D.55` deja una, y solo con
guarda de DATO en rojo). **Y no habria donde ponerla: esta acta no escribe encargo.**

**EL COSTE, QUE `D.55` ME MANDA DECIR SI PASA DE `10`:** el turno del extractor costo **`5,5610475`
USD** en `818` segundos (`loop.log`, cierre de la `VUELTA 5` de la corrida). **Por debajo de `10`, asi
que no hay desglose que dar**, y es el turno mas barato de este frente.

---

## 7. LAS CONDICIONES DE PARADA, REPASADAS UNA A UNA (`AUDITOR_FORJA.md` `3`)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| **doctrina NUEVA necesaria** | ninguna: el discutible se adjudica **citando `9.1` y sus dos restricciones**, que es extension natural de regla escrita, no doctrina nueva. La cola sigue en `11` | **NO** |
| **contradiccion con regla o cifra vigente** | la unica discrepancia de cifra es la del censo (`1.1`), **resuelta con la jurisprudencia de la casa sin doctrina nueva** | **NO** |
| **fallo tecnico repetido** | `gate`, `guiones`, `tests`, tallado y censo **VERDES hoy, corridos por mi** | **NO** |
| **credito roto** | las cinco rachas en `0` (`1.4`), y la unica caida de la tanda **no acumula** (`4.1`) | **NO** |
| **DECISION DE ALEXIS** | **SI, Y ES ESTA.** Lo que le queda por minar a este libro son `cap_01`, `cap_02` y `cap_03`, **apartados por decision del fundador** (`d094`), y el `cap17_reservado`, **otra clave con su condicion escrita sin cumplir**. Tomar cualquiera de las dos cosas es **cambiar el alcance de la extraccion**, que la casa reserva | **SI, PARA** |
| **campania consumada** | **el frente ha minado `19` de las `22` unidades y no tiene una sola unidad mas que le este permitida**. `PARALELO.md` `5.0.b` paso `(a)` pide **su `PARA_ALEXIS.md` en el arbol** para que el relevo empiece, y **el paso `(b)`, la cosecha, no es del bucle** | **SI, PARA** |

**SE CUMPLEN DOS, Y NINGUNA ES DE CREDITO.** Escribo `docs/loop/PARA_ALEXIS.md` y **dejo
`docs/loop/PROMPT_SIGUIENTE.md` VACIO**.

---

## 8. EL LOTE `9`, LAS DOS CONDICIONES DE `D.32` MEDIDAS, Y POR QUE AUN ASI NO ABRO NADA

### 8.1. El estado del lote, contado por mi

    $ ls fuentes/gerber_emyth/*.md | wc -l
    22

| | unidades | cuales |
|---|---:|---|
| **minadas por este frente** | **`19`** | `cap_04` a `cap_22`, sin hueco, leido del registro (un capitulo minado no deja marca en el repo) |
| **sin minar** | **`3`** | `cap_01`, `cap_02`, `cap_03`, **las tres en `d094`**, apartadas por el fundador |
| **en la bandeja, sin insertar** | **`22` candidatos** | `cuarentena/gerber_emyth/`, `0` en el grafo |

    $ python <cuenta propia de nodos del grafo por fuente>
    nodos de dataset/nodos.jsonl con fuente gerber_emyth: 0

**EL LOTE `9` QUEDA MINADO ENTERO SALVO `d094`, y se lo firmo.** La insercion no es de ningun frente
(`D.45`) y la cosecha no la hace el bucle.

### 8.2. Las dos condiciones de `D.32`, medidas y publicadas, para los tres candidatos posibles

| clave | material en `fuentes/<clave>/` | clave en la tabla canonica | lo que dice el instrumento | **se puede abrir** |
|---|---:|---|---|---|
| `gerber_emyth_cap17_reservado` | **`1`** | **SI** | `--puedo` da **`SI`** | **NO.** `ORDEN_DE_LOTES.md` `L27` lo pone en el lote `11`, **RESERVADO, entra el ultimo**, y el motivo escrito en ese mismo fichero es que **entra cuando su propio libro ya este dentro del grafo**: hoy hay **`0`** nodos de `gerber_emyth` en el grafo. **La condicion esta medida y NO se cumple** |
| `marquet_turn_the_ship` | **`17`** | **SI** | `--puedo` da **`NO`**: *esta PAUSADO y NO COSECHADO, tiene 9 candidatos que todavia no han llegado a esta rama* | **NO.** `D.50` manda **relevarlo entero**, y el relevo **empieza por cosechar su rama**, que es paso del fundador |
| `grove_high_output` | **`18`** | **SI** | `--puedo` da **`SI`**, *continua desde el capitulo siguiente al ultimo minado (`cap_18`)* | **NO HAY NADA QUE CONTINUAR:** el tablero lo da con **`18` de `18` capitulos minados y `ultimo_capitulo` `cap_18`**, y su mineria cerro en la vuelta `62` de la serial. **El `SI` esta vacio** |

**LAS DOS CONDICIONES DE `D.32` SALEN VERDES EN LAS TRES CLAVES, Y AUN ASI NINGUNA SE ABRE.** Es
exactamente lo que `D.50` vino a impedir: **`D.32` abriria el siguiente sin parada entre medias**, y
por eso la regla mas reciente manda mirar el tablero antes. **Publico las dos medidas, como `D.32`
pide, y declaro el tercer bloqueo de cada una, que es el que manda.**

### 8.3. Y una cosa que subo sin adjudicarla, porque no es mia

**`PARALELO.md` `4.d` (21 sep 2026) corto este libro de la campania con una premisa medida:** que
insertar sus candidatos *obligaria a minar los dos libros enteros, y eso es lo que esta campania decide
no pagar*, con el frente fotografiado en **`10` candidatos y `4` de `22` capitulos**. **Hoy el frente
esta en `22` candidatos y `19` de `22` capitulos:** ese coste **ya esta pagado**. Es `d125`, anotada en
la vuelta `7` con cifras mas viejas, **y la vuelvo a medir aqui porque ha cambiado otra vez**. **No
adjudico nada con esto:** si el libro entra o no entra al mundo `11` es decision del fundador
(`PARALELO.md` `4.c` y `4.d`), y lo unico que me toca es **ponerle la cifra nueva delante.**

---

### 8.4. Lo que este turno deja escrito, recomputado DESPUES de escribirlo

**Las cifras de `1.1` y `1.4` son las de la VERIFICACION, medidas antes de que yo escribiera nada.
Estas son las de DESPUES, y se publican las dos** (`D.38.3`: la discrepancia se declara, no se
resuelve copiando):

    $ python scripts/deuda.py | sed -n '3p'
      pendientes: 49    pagadas: 39
    $ python scripts/censar_rutas.py | tail -1
    CENSO VERDE: las 1132 rutas publicadas sostienen lo que dicen sostener.
    $ python scripts/tallar_reporte.py | tail -1
    TALLADO VERDE: las 176 tabla(s) comprobables son las de su instrumento, celda a celda.
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python forja.py credito | sed -n '6,11p'
      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA G8
      CIFRA PUBLICADA    0 de 2     ACTA G8
      CLASE              0 de 2     ACTA G8
      DATO MOVIDO        0 de 2     ACTA G8
      REPORTE            0 de 3     ACTA G8

**`44` mas las `5` que anoto en este turno dan `49`**, y ninguna la pago yo: `d128` y `d129` las paga
la vuelta que vuelva a tocar el reporte, y `d130`, `d131` y `d132` **no se pagan desde un frente**. El
censo pasa de `1130` a `1132` **porque esta acta publica dos rutas mas que antes no existian**, que es
la misma figura que le declaro a el en `1.1` **y por eso la mido yo tambien al final.**

**Y MI TANDA ESTA ESCRITA** (`D.48`): cinco lineas en `docs/loop/CREDITO_gerber_emyth.jsonl`, una por
especie, **las cinco `--limpia`**, con su cita a la seccion de esta acta que la sostiene.

---

*`ACTA G8` cerrada. **CON PARADA, y la parada no es por credito: es por alcance.** Lo que le firmo es
lo sustancial de la vuelta: **las `16` piezas de sus tres fronteras al digito con codigo mio**, los tres
bordes de abajo comprobados uno a uno, **los tres `CERO CANDIDATOS` con los tres capitulos leidos
enteros por mi**, su discutible sostenido por las dos restricciones de `9.1`, la muestra identica a su
semilla, `0` ficheros de dato movidos y `0` de maquinaria. **Lo que se cae es una cita verbatim que el
reporte pega cambiada en dos de sus cuatro lineas**, con el fichero de evidencia fiel al libro y `0`
guiones largos que culpar: **no es `d124`, es la mano**, vive en bloque de evidencia y **no acumula**.
**Y la caida propia la declaro yo:** mi encargo mando tachar un rotulo en una celda y el rotulo vivia
en dos, **porque no corri el `grep` antes de escribirlo**, que es la misma falta que yo le cobre a el
en la `ACTA G7`. **Cada cifra de esta acta lleva su comando pegado encima: se puede repetir entera sin
mi.***

---

# ACTA `G9` DEL FRENTE `gerber_emyth`. VUELTA 9, lote 9, `cap_01`, `cap_02` y `cap_03`, **CLASE EXTRACCION**: **LE FIRMO LAS DOCE PIEZAS AL DIGITO CON CODIGO MIO Y LOS TRES CERO LEYENDO YO LOS TRES CAPITULOS ENTEROS, Y LE ADJUDICO A SU FAVOR LAS DOS INSTRUCCIONES QUE DECLINO; LO QUE SE CAE ES UNA RAZON QUE SE QUEDA CORTA, NO UN VEREDICTO. Y ESTA ACTA PARA: EL LIBRO ESTA ENTERO Y LO QUE SIGUE ES DEL FUNDADOR**

*Auditor del bucle, 21 sep 2026. Rama `extraccion-gerber_emyth`, hash auditado `9ca4073`.
Mis ficheros de trabajo estan en el directorio de sesion, FUERA del arbol, y es por `d126`:
en este repo no se puede guardar una copia fiel de un parrafo de este libro fuera de
`fuentes/`.*

**LO QUE LE FIRMO, Y ES TODO LO SUSTANCIAL.** Las **`12`** piezas de sus tres fronteras las
recompongo **con codigo mio** y me salen **las `12` al digito**, con los tres cuerpos en
`1402`, `1212` y `2202`, residuo `0`, `0` solapes, `0` lineas sin cubrir y **las tres
acabando en la ultima linea real** del fichero. **Los tres `CERO CANDIDATOS` se los firmo
habiendo leido yo los tres capitulos enteros**, no por muestra. **La muestra de fidelidad
con su semilla `g9` me sale IDENTICA a la que pego**, linea a linea. **Y le adjudico a su
favor las dos instrucciones del encargo que declino**: `D.28` es literal y ratificada por el
fundador. **Cero dato movido y cero maquinaria tocada**, medido con `git diff` entre sus dos
commits.

> ### **LO QUE SE CAE ES UNA RAZON, NO UN VEREDICTO, Y LA LEVANTO LEYENDO EL LIBRO**
>
> `G9.4.d` dice que *el unico tramo que se acerco a competir* en `cap_03` son las cuatro
> etapas de `L225`, que son **estados psicologicos**. Dentro de esa misma pieza `R5` hay
> **dos inventarios literales que compiten mas fuerte bajo `9.1`**: `L169` enumera **diez
> objetos de trabajo** de la jornada de Sarah uno a uno, y `L201` enumera **siete etapas de
> un proceso que el propio libro llama** *the magic of the process*. **Su veredicto sigue
> siendo el mio** (`4.1` dice por que caen los dos), **pero no por el motivo que escribio.**
>
> **VIVE EN PROSA DE SUBSECCION, no en tabla ni en cabecera ni en la conclusion**, asi que
> `5.2` dice que **NO acumula** y `5.4` dice que la tanda **reinicia la racha igual**.
> **`REPORTE` se queda en `0 de 3`.** Queda anotada como `d135`.

**Y ESTA ACTA PARA, y es la parada feliz.** El libro esta minado **`22` de `22`** y **no le
queda una sola unidad que este frente pueda tomar**. Lo que sigue (fundir la rama, cosechar,
firmar los tres capitulos en `config/`) **es del fundador y el bucle no lo hace**. Escribo
`docs/loop/PARA_ALEXIS.md` y **dejo `docs/loop/PROMPT_SIGUIENTE.md` VACIO**, que es
literalmente lo que el encargo pide en su seccion `6` y lo que `PARALELO.md` `5.0.b` paso
`(a)` necesita delante.

## 0. **NO HAY HUECO DE ACTA**, y la herencia se declara antes que nada

**La `ACTA G8` cubre la vuelta `8` de este frente y yo cubro la `9`.** No hay vuelta sin
auditar entre las dos:

    $ grep -n "^# ACTA .G[0-9]" docs/loop/ACTA_AUDITOR.md | tail -3 | cut -c1-58
    48264:# ACTA `G7` DEL FRENTE `gerber_emyth`. VUELTA 7, lot
    48881:# ACTA `G8` DEL FRENTE `gerber_emyth`. VUELTA 8, lot
    49418:# ACTA `G9` DEL FRENTE `gerber_emyth`. VUELTA 9, lot

**ACTA ANTERIOR LEIDA:** `docs/loop/ACTA_AUDITOR.md`, `ACTA G8`, lineas `48881` a `49415`.

| | heredado | como queda hoy, medido |
|---|---|---|
| **HEREDADO 1** | **NO APLICA, y el motivo va escrito** (`D.40`): la `ACTA G8` cerro **sin tarea bloqueante**, porque `D.55` solo deja dejar una si cita una guarda de DATO en rojo, y no habia ninguna | **NO APLICA** |

**LA SALIDA QUE LO SOSTIENE** (`D.40` ensanchada, 16 sep: un `NO APLICA` lleva su comando
pegado):

    $ sed -n '48881,49415p' docs/loop/ACTA_AUDITOR.md | grep -c "^\*\*TAREA BLOQUEANTE"
    0
    $ sed -n '48881,49415p' docs/loop/ACTA_AUDITOR.md | grep -n "GUARDA DE DATO EN ROJO" | cut -c1-70
    422:**GUARDA DE DATO EN ROJO: NINGUNA**, asi que **cero tareas bloquea

**EL `grep -c` VA ANCLADO A PRINCIPIO DE LINEA A PROPOSITO, y lo digo porque el primero que
escribi no lo estaba y daba `1`:** la `ACTA G8` **cita** la cadena `TAREA BLOQUEANTE DEL
AUDITOR` dentro del comando con el que ella misma declaro su herencia, asi que un `grep`
suelto se caza a si mismo. **Lo corri antes de pegarlo y por eso lo se.**

**Y NO HUBO FASE CIEGA NI SELLO EN ESTA VUELTA**, que es lo que `D.58` manda en `cuarentena`
y lo que el arnes registro por su cuenta:

    $ grep -n "SIN FASE CIEGA" docs/loop/loop.log | tail -1
    1191:[2026-09-21 18:22:23] VUELTA 1 : SIN FASE CIEGA (D.58: en cuarentena no hay cifra sobre el grafo que proteger)

**La `VUELTA 1` de esa corrida es la `9` de este frente:** el log numera la corrida, que el
arnes reinicio al arrancar a las `17:46`, y el acta numera el frente.

---

## 1. LO QUE VERIFIQUE CON MIS PROPIOS COMANDOS

### 1.1. Las cinco guardas, corridas por mi en esta vuelta

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python tests/test_aceptacion.py | tail -1
      total: 353 pruebas, 0 fallos, 0 errores

    $ python scripts/tallar_reporte.py | tail -1
    TALLADO VERDE: las 181 tabla(s) comprobables son las de su instrumento, celda a celda.

    $ python scripts/censar_rutas.py | tail -1
    CENSO VERDE: las 1161 rutas publicadas sostienen lo que dicen sostener.

**`346` NODOS Y `353` PRUEBAS ME SALEN AL DIGITO CON LAS SUYAS.** Y mi conteo propio del
estado, que es el que `AUDITOR_FORJA.md` `1` me manda hacer aparte del instrumento:

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
    $ ls cuarentena/gerber_emyth/*.json | wc -l
    22

**EL TALLADO Y EL CENSO NO, Y NO LO RESUELVO COPIANDO** (`D.38.3`): su `G9.6.e` pega **`180`**
tablas y **`1147`** rutas, y yo mido **`181`** y **`1161`**. **Las dos diferencias las
explico midiendo, no suponiendo:**

    $ python <cuenta propia de la cola del reporte tras G9.6.e>
    G9.6.e arranca en la linea 61623 ; lineas despues de ella: 177
    filas de tabla markdown en la cola (|...|): 7
    rutas distintas citadas en la cola: 14

**UNA TABLA MAS Y CATORCE RUTAS MAS, QUE ES EXACTAMENTE LA DIFERENCIA DE LAS DOS CIFRAS**
(`180 + 1 = 181`, `1147 + 14 = 1161`). Son las que el propio reporte escribio **despues** de
correr los dos instrumentos: la tabla de condiciones de parada de `G9.6.h` y las rutas de
`G9.6.f` a `G9.6.j`. **La jurisprudencia de esta casa para esto ya esta escrita** (`ACTA 10`
punto `1.d.1`: *aquella cifra era verdad al ESCRIBIRSE y falsa al cerrarse la misma
vuelta*), asi que **no la cargo: es una cifra cierta al correrse.** **Y lo que la guarda
afirma, el VERDE, se sostiene hoy con mi corrida.**

### 1.2. Sus doce piezas, recompuestas con codigo que no es el suyo

**No uso su `.gerber_v5/frontera.py`.** Escribo mi propio contador fuera del arbol, con el
arranque del cuerpo sacado del segundo `---` de la cabecera yaml y **la cola vacia
descontada para casar con `wc -l`**, y le paso las `12` celdas de sus tres tablas:

    $ python <contador propio del auditor> cap_01 cap_02 cap_03
    fuentes/gerber_emyth/cap_01.md: wc-l=71  cierres_yaml=[1, 7] cuerpo=L8..L71  palabras_cuerpo=1402 palabras_cabecera=32 total=1434
       piezas=3 suma=1402 cuerpo=1402 residuo=0 solapes=0 sin_cubrir=0 fuera_de_cuerpo=0 ultima_acaba_en=L71 wc=71
       celdas que DIFIEREN: ninguna, las 3 al digito
    fuentes/gerber_emyth/cap_02.md: wc-l=99  cierres_yaml=[1, 7] cuerpo=L8..L99  palabras_cuerpo=1212 palabras_cabecera=32 total=1244
       piezas=4 suma=1212 cuerpo=1212 residuo=0 solapes=0 sin_cubrir=0 fuera_de_cuerpo=0 ultima_acaba_en=L99 wc=99
       celdas que DIFIEREN: ninguna, las 4 al digito
    fuentes/gerber_emyth/cap_03.md: wc-l=233 cierres_yaml=[1, 7] cuerpo=L8..L233 palabras_cuerpo=2202 palabras_cabecera=35 total=2237
       piezas=5 suma=2202 cuerpo=2202 residuo=0 solapes=0 sin_cubrir=0 fuera_de_cuerpo=0 ultima_acaba_en=L233 wc=233
       celdas que DIFIEREN: ninguna, las 5 al digito

| capitulo | piezas | palabras del cuerpo | cabecera yaml | residuo | solapes | sin cubrir | borde de abajo |
|---|---:|---:|---:|---:|---:|---:|---|
| `cap_01` | `3` | `1402` | `32` | `0` | `0` | `0` | `L71`, que es su `wc -l` |
| `cap_02` | `4` | `1212` | `32` | `0` | `0` | `0` | `L99`, que es su `wc -l` |
| `cap_03` | `5` | `2202` | `35` | `0` | `0` | `0` | `L233`, que es su `wc -l` |

**LAS DOCE CELDAS DE PALABRAS AL DIGITO, Y LOS DOS BORDES TAMBIEN.** El de arriba lo compara
el reporte contra `wc -w` a mano porque la guarda no lo cubre (`d109`), **y las tres sumas
del cuerpo mas la cabecera me dan sus tres totales** (`1402+32=1434`, `1212+32=1244`,
`2202+35=2237`); **el de abajo lo compruebo yo**, y las tres ultimas piezas acaban en la
ultima linea del fichero: **ninguna de las tres fronteras se queda corta por abajo**, que es
la otra mitad que `d109` no vigila.

### 1.3. La muestra de fidelidad, cotejada con su semilla (`D.58`)

    $ python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_01,cap_02,cap_03 --semilla g9
      RELEIDO ENTERO : cap_02
      POR MUESTRA    : cap_01, cap_03, 15 pasos cada uno
      --- cap_01: 0 paso(s) en la muestra
      --- cap_03: 0 paso(s) en la muestra
      --- cap_02: ENTERO, 0 paso(s), no hay muestra que elegir

**IDENTICA A LA QUE PEGO** en `G9.4.f`, reparto incluido. `D.58` dice que una lista distinta
seria caida de cifra: **no lo es.** Y el disparador del `10` por ciento **no tiene sobre que
dispararse**, porque no hay un solo paso escrito en los tres capitulos.

### 1.4. La cita verbatim: **su copia SI es su fichero, y la unica diferencia con el libro es la declarada**

**ES LA MISMA FAMILIA QUE LE COBRE EN LA `ACTA G8`** (`d129`: el bloque no era el fichero que
decia ser), **y esta vez no cae.** Lo mido caracter a caracter con codigo mio, sin normalizar
nada:

    $ python <comparador propio: libro vs fichero de evidencia vs bloque del reporte>
    evidencia (sin el '225:') == libro ? False
       primera diferencia en el caracter 103 : '-' vs (em dash U+2014)
       longitudes: 237 237
    em dashes (U+2014) en la linea del libro: 1
    em dashes en el fichero de evidencia    : 0
    em dashes en el bloque del reporte      : 0

**EL BLOQUE DEL REPORTE Y EL FICHERO DE EVIDENCIA SON EL MISMO TEXTO**, y la unica diferencia
con el libro es **UN caracter de `237`**, el em dash de `L225` sustituido por el guion corto.
**Eso es exactamente el remedio que `d124` dejo escrito para este mismo libro** y que su
`G9.6.d` declara: se sustituye en las copias de fuera de `fuentes/` y no se toca el origen.
**Le firmo la fidelidad de la cita.**

### 1.5. La deuda y el credito, recomputados por mi

    $ python scripts/deuda.py | sed -n '3p'
      pendientes: 48    pagadas: 40

    $ python scripts/deuda.py --clase 9
    LIBRE
      van 3 de 5 desde la ultima de saneamiento (la 6), con 48 deuda(s) esperando

**`48`/`40` AL DIGITO CON SU CIERRE**, y la aritmetica cuadra por las dos mitades:
`49 + 39 = 88` al abrir y `48 + 40 = 88` al cerrar, o sea **`1` pagada y `0` nuevas
contraidas por el extractor**. **`d094` esta pagada de verdad**, y con su vuelta escrita:

    $ grep -o '"id": "d094"[^}]*' docs/loop/DEUDA.jsonl | tail -1
    "id": "d094", "linea": "gerber_emyth", "tipo": "pago", "vuelta": "9"

    $ python forja.py credito | sed -n '5,11p'
      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA G8
      CIFRA PUBLICADA    0 de 2     ACTA G8
      CLASE              0 de 2     ACTA G8
      DATO MOVIDO        0 de 2     ACTA G8
      REPORTE            0 de 3     ACTA G8

### 1.6. Cero dato movido y cero maquinaria, medido entre sus dos commits

    $ git diff --stat 2f9b1a3 9ca4073 -- dataset/ bitacora/ censos/ config/ cuarentena/ src/ scripts/ tests/ hooks/ esquema/ fuentes/ docs/BANCO_DE_REGLAS.md orquestador_forja.sh
    (sin salida)

    $ git diff --name-only 2f9b1a3 9ca4073 | grep -v "^.gerber_v9/"
    docs/loop/DEUDA.jsonl
    docs/loop/REPORTE.md
    docs/loop/TABLA_DE_CIERRE.txt

**TRES FICHEROS FUERA DE SU CARPETA DE EVIDENCIA, Y LOS TRES SON REGISTRO.** `DATO MOVIDO` no
tiene caso en esta tanda, y `D.45` se cumple entera: **ni `src/`, ni `scripts/`, ni el banco,
ni el arnes, ni `fuentes/`.** **Y la vuelta entera es UN solo commit**, lo que hace la
comparacion mas facil de repetir sin mi.

---

## 2. `PASOS INVENTADOS POR CAPITULO`: **CERO POBLACION, Y LA FIRMO ASI** (`AUDITOR_FORJA.md` `8`)

**Es cifra mia y no la copio** (`8.3`). La cuento **por la `UNIDAD DE ORIGEN` que cada ficha
declara**, que es el criterio que el encargo fijo en su punto `1.b.2` y no el `grep` suelto
de `cap_NN` que `d106` ya midio como defectuoso:

    $ python <cuenta propia de la bandeja por UNIDAD DE ORIGEN declarada>
    fichas de la bandeja: 22   pasos_accionables totales: 176
       cap_04 f=1 p=7 | cap_07 f=1 p=8 | cap_08 f=2 p=17 | cap_11 f=6 p=57 | cap_12 f=3 p=12
       cap_13 f=1 p=10 | cap_14 f=1 p=9 | cap_15 f=1 p=5 | cap_18 f=3 p=26 | cap_19 f=3 p=25
    fichas SIN 'UNIDAD DE ORIGEN' declarada: 0
    cap_01: fichas=0 pasos=0
    cap_02: fichas=0 pasos=0
    cap_03: fichas=0 pasos=0

| capitulo | candidatos nuevos | pasos escritos | PUENTE | pasos inventados |
|---|---:|---:|---:|---|
| `cap_01` | `0` | `0` | `0` | **sin poblacion que medir** |
| `cap_02` | `0` | `0` | `0` | **sin poblacion que medir** |
| `cap_03` | `0` | `0` | `0` | **sin poblacion que medir** |
| **el tramo entero** | **`0`** | **`0`** | **`0`** | **sin poblacion que medir** |

**LE FIRMO LA FORMA, Y ES LA CORRECTA:** `0` entre `0` no es una fraccion, asi que **no es
`0,00` por ciento**, que seria una medida, sino **ausencia de poblacion**, que es una
declaracion. **Un capitulo que no escribe pasos no puede firmar que no invento ninguno.**

> **LECTURA, Y ES DE LA BANDEJA ENTERA, no de esta vuelta:** las `22` fichas declaran las
> `22` su `UNIDAD DE ORIGEN`, **cero sin declarar**. El encargo puso esa exigencia en su
> punto `1.b.2` para los candidatos nuevos de esta vuelta, que fueron `0`; **lo que mido es
> que el libro entero la cumple ya**, y eso es lo que la vuelta de insercion va a leer.
>
> **Y `8.1` NO TIENE TRAMO SIGUIENTE QUE DIMENSIONAR:** este libro ya no lo tiene. **La
> ultima fila con poblacion sigue siendo la de la vuelta `7`** (`cap_18` y `cap_19`, `0,00`
> por ciento las dos, firmadas por mi en la `ACTA G7`).

---

## 3. LA RELECTURA: **LOS TRES CERO ME SALEN LEYENDO LOS TRES CAPITULOS ENTEROS**

### 3.0. Como la hice, y que no puedo llamarla ciega

**`D.58` dice que en una vuelta de `cuarentena` NO hay fase ciega, ni sello, ni testigo**, y
el arnes lo registro (seccion `0`). **Y ESTA VUELTA NO MARCO NI UN DISCUTIBLE**, asi que
`5.1` se queda sin su punto de partida: no hay nada dentro del marcado que releer.

    $ sed -n '61117,61799p' docs/loop/REPORTE.md | grep -c "^\*\*Ninguno\.\*\*"
    3

**LO QUE HICE EN SU LUGAR, Y ES MAS QUE UNA MUESTRA: lei los tres capitulos ENTEROS**, las
`403` lineas de fichero, y escribi mi veredicto desde el texto. **`6.4` y `7.G` de la cosecha
dicen que una discrepancia en un tramo SIN DISCUTIBLES MARCADOS no rompe el credito de
tanda**: la comparacion que la regla supone no existe aqui. **Se registra, se adjudica, y no
acumula.**

**Y LA POBLACION DE LA MUESTRA PINEADA ES CERO** (`AUDITOR_FORJA.md` `7`): no hay veredicto
`SANO` escrito en `bitacora/VEREDICTOS.jsonl` en esta tanda, porque la tanda **no inserto y
no escribio ninguna ficha** (`1.6`: `bitacora/` sin tocar). `7` manda no inventar una muestra
donde no hay poblacion. **Una tanda de cero candidatos no tiene tasa de dejar pasar: tiene mi
lectura y nada mas**, y eso lo digo yo en vez de callarlo.

### 3.1. Los tres `CERO CANDIDATOS`, releidos por mi capitulo a capitulo

| capitulo | lo que leo | mi veredicto |
|---|---|---|
| `cap_01`, `Foreword` | prefacio personal del autor a la edicion revisada: quince anios, familia, viajes, y la tesis de que las cosas pequenias hechas exactamente bien distinguen a un negocio. **Los dos tramos que compiten son `L29`**, que enumera *finance, marketing, management, and operations*, **y `L39`**, que enumera *on the telephone, between the customer and a salesperson, on the shipping dock, at the cash register*. **Los dos caen por lo mismo: no hay mandato al que sirvan**, son ilustraciones de un diagnostico, y `9.1` procedimentaliza **una linea normativa** con su inventario, no un inventario suelto. El cierre `L63` es una cita ajena, y **una advertencia es linea** (`P.11`) | **CERO CANDIDATOS, y se lo firmo** |
| `cap_02`, `Introduction` | la estadistica de fracaso y las **cuatro `IDEA #`** del libro. Son la restriccion `1` de `9.1` al digito: **METAS y FINES**, no medios. `IDEA #4` dice *in a step-by-step method* **sin enumerar un solo paso**: es el caso literal de *solo el nombre de otro*. **Y compruebo su razon contra `D.37` con el fichero delante**, porque es la unica de las tres que hacia falta medir: el libro tiene **TRES** partes (`PART I` en `cap_02` `L95`, `PART II` en `cap_08` `L175`, `PART III` en `cap_11` `L325`) contra **cuatro** ideas, **asi que no hay correspondencia uno a uno con una parte numerada** y no nace cabeza de serie. **Su argumento se sostiene y ademas se puede reproducir** | **CERO CANDIDATOS, y se lo firmo** |
| `cap_03`, `Cap. 1` | el mito, la `Entrepreneurial Seizure`, la `Fatal Assumption` y el caso de Sarah. **Los dos tramos que mas compiten estan en `R5` y no son el que el reporte defiende** (`4.1`): `L169` y `L201`. **Caen los dos**, y por dos motivos que no son *no hay inventario*: **no hay linea normativa** a la que el inventario sirva, y **son del CASO y no de la casa** (manual `3.5`: el entregable llevaria el dato del caso, hornos y rhubarb). `L231` (*you take this one step at a time*) es **una advertencia** que remite al capitulo siguiente | **CERO CANDIDATOS, y se lo firmo** |

> **LECTURA, Y ES LA QUE IMPORTA PARA EL LIBRO:** las tres unidades que abren
> `The E-Myth Revisited` **son tesis y diagnostico**, no doctrina ejecutable. El libro pone
> su procedimiento **a partir de `cap_04`**, y ahi es donde estan los `22` candidatos. **Un
> cero con su razon leida es un resultado**, y aqui lo es tres veces.

### 3.2. **LA FIRMA DE LOS TRES CERO, QUE ES LO QUE `config/frentes.json` NECESITA Y YO NO PUEDO ESCRIBIR**

**ESTA ES LA FIRMA, Y SE CITA DESDE AQUI:** `cap_01`, `cap_02` y `cap_03` de `gerber_emyth`
quedan **LEIDOS ENTEROS Y ADJUDICADOS EN CERO NODOS** por el auditor de la vuelta `9`,
`ACTA G9` seccion `3.1`. **El campo `minados_en_cero` de `config/frentes.json` es quien lo
recoge** (`d096`), **y `config/` no es sede del auditor** (`5.6`), asi que **va PEDIDO en
`docs/loop/PARA_ALEXIS.md`** y anotado como `d136`. Hoy el campo trae `9` capitulos y el
tablero `19`:

    $ python -c "import json;print(json.load(open('config/frentes.json'))['minados_en_cero']['gerber_emyth']['capitulos'])"
    ['cap_05', 'cap_06', 'cap_09', 'cap_10', 'cap_16', 'cap_17', 'cap_20', 'cap_21', 'cap_22']
    $ python -c "import json;[print(len(json.loads(l)['capitulos_minados'])) for l in open('docs/loop/TABLERO.jsonl') if json.loads(l).get('clave')=='gerber_emyth']"
    19

**LECTURA:** con esos tres escritos el tablero pasa a `22` de `22` **por el canal que `d096`
le dio**, y el libro deja de necesitar que nadie lo cuente a mano. **Es la misma peticion que
la `ACTA G8` hizo por los cinco anteriores, y que se cumplio**: el encargo de esta vuelta lo
dice en su seccion `3`.

---

## 4. LO QUE SE CAE, POR ESPECIE (`5.2`)

### 4.1. `REPORTE`: **una caida con dos ejemplares, y NO acumula**

**`d135`. Una razon absoluta mas ancha que el capitulo, con el veredicto intacto.**

| donde | lo que el reporte afirma | lo que leo yo en el fichero |
|---|---|---|
| `G9.4.d`, `cap_03` | *el unico tramo que se acerco a competir* son las cuatro etapas de `L225` | `L169` enumera **diez objetos de trabajo** de la jornada de Sarah uno a uno, y `L201` **siete etapas de un proceso que el libro llama** *the magic of the process*. **Los dos compiten mas fuerte que `L225`**, que son estados psicologicos |
| `G9.2.c`, `cap_01` | *no hay una lista de que atender* | `L29` enumera cuatro materias y `L39` cuatro sitios |

**POR QUE EL VEREDICTO NO SE MUEVE, Y LO ESCRIBO YO:** los tres tramos caen igual, **pero
por un motivo que el reporte no da**. `9.1` vuelve procedimentable **una linea normativa**
cuando el libro pone su inventario; en los tres casos **no hay linea normativa**: son
narracion e ilustracion, sin un solo imperativo dirigido al lector. Y `L169` y `L201` son
ademas **del caso**, no de la casa (manual `3.5`), con la senial barata a la vista: **un nodo
sacado de ahi llevaria hornos y rhubarb en su entregable.**

**POR QUE NO ACUMULA:** `5.2` hace acumular a `REPORTE` **solo si la cifra vive en TABLA,
CABECERA o CONCLUSION**. Las dos frases viven en **prosa de subseccion**. **Y la celda de
tabla que si podria acumular NO es falsa**: la fila `R5` de la frontera de `cap_03` dice
*cero inventario propio procedimental* **precedido de** *no medios, etapas u objetos de
trabajo **que el lector deba revisar o ejecutar***, **y con ese calificativo la celda es
cierta**. La leo a su favor porque la leo entera. **Y `5.4` dice que una tanda con caidas
solo de las que no acumulan reinicia la racha igual**, asi que `REPORTE` **sigue en
`0 de 3`.**

> **DEJO LOS DOS ELEMENTOS A LA VISTA PARA QUIEN QUIERA LEERLO AL REVES:** que la celda de
> `R5` contiene la palabra `cero` y vive en una tabla, y que la salva un calificativo escrito
> tres lineas antes en la misma celda. **Si el siguiente lector adjudica que la tabla manda
> sobre el calificativo, `REPORTE` sube a `1 de 3` y la correccion la firma el.** Lo que no
> hago es dejarlo sin escribir.

### 4.2. **LO QUE MIDO Y NO ES DE NADIE: LA GUARDA `D.59` NO VE ESTE FRENTE**

**`d134`, y no la cargo contra nadie porque nadie publico una cifra sobre ella.** El asunto
del commit de la vuelta declara *una correccion del guardia `D.59` por un falso positivo de
"intermedia" contra "media"*. **Fui a mirar de donde salia**, y sale de que la guarda mide la
poblacion equivocada en este frente:

    $ python <medida propia sobre scripts/tallar_reporte.py y docs/loop/REPORTE.md>
    cabezas que el regex de D.59 reconoce: 61
    ULTIMA que reconoce: # VUELTA 62, lote 7 (`grove_high_output`), CLASE EXTRACCION
    linea de esa cabeza: 57016  / total lineas: 61799
    lineas que quedan DENTRO de la 'vuelta viva': 4783
    cabezas de FRENTE que el regex NO reconoce: 7

**`CABEZA_DE_VUELTA` es `^#{1,2}\s+VUELTA\s+\d+`, y las `7` cabeceras de este frente son
`# FRENTE (clave), VUELTA N:`.** Ninguna casa. Asi que su *vuelta viva* son **`4783`
lineas**, las vueltas `2` a `9` enteras del frente, **en vez de las `683` de la vuelta `9`**.

> **LECTURA, Y LA SEPARO DE LA CIFRA A PROPOSITO** (`D.38.3` ensanchada): **su propio
> docstring dice que la ventana ancha es justo lo que vino a evitar** (*sobre el reporte
> entero caerian `591` lineas de `53` vueltas de historia; sobre la vuelta viva cayeron `2`,
> y las dos eran de verdad*). **En este frente la ventana nunca se estrecho.** Es maquinaria,
> **vedada desde un frente** (`D.45`, `D.47`): **se mide y se sube.** Va en `PARA_ALEXIS.md`.

**Y UNA COSA MAS, QUE ES DEL REPORTE Y LA DIGO SIN CARGARLA:** esa correccion **esta en el
asunto del commit y no esta en el reporte**. `5.6` dice que **el asunto de un commit NO es
sede de cifra**, asi que no hay cifra publicada que caiga; pero una correccion declarada solo
en el asunto **no la encuentra quien relee el reporte**. Queda dicho aqui, que es donde se
relee.

### 4.3. `CLASE`, `CIFRA PUBLICADA` y `DATO MOVIDO`: **ninguna, y con que lo mido**

| especie | lo que mido | resultado |
|---|---|---|
| **`CLASE`** | `bitacora/VEREDICTOS.jsonl` y `config/pares_mutuos.jsonl` sin tocar (`1.6`), **cero veredicto escrito en la tanda**, y los tres veredictos de lectura releidos por mi capitulo entero y sostenidos (`3.1`) | **NINGUNA** |
| **`CIFRA PUBLICADA`** | su unica sede duradera movida es `docs/loop/DEUDA.jsonl` (el pago de `d094`, comprobado en `1.5`) y `TABLA_DE_CIERRE.txt`, que trae **sus** cinco filas de la vuelta `9` y no las de la `8` (comprobado contra el fichero). Las `12` celdas de frontera **me salen al digito** (`1.2`) | **NINGUNA** |
| **`DATO MOVIDO`** | `git diff` entre sus dos commits sobre `dataset/`, `bitacora/`, `censos/`, `config/`, `cuarentena/` y `fuentes/`: **vacio** (`1.6`) | **NINGUNA** |

**LAS CINCO RACHAS SE QUEDAN DONDE ESTABAN: `REPORTE` `0 de 3`, `CIFRA PUBLICADA` `0 de 2`,
`CLASE` `0 de 2`, `DATO MOVIDO` `0 de 2`, `AUDITOR` `0 de 3`.** **Este frente cierra con las
cinco en cero**, que es lo que el encargo queria dejar sentado.

---

## 5. LA ADJUDICACION QUE EL REPORTE ME PIDE: **LAS DOS INSTRUCCIONES DECLINADAS, Y LE DOY LA RAZON EN LAS DOS**

**`G9.6.j` me lo pone delante con sus citas y me pide que lo escriba en mi acta.** Lo escribo:
**el extractor acerto, y no por costumbre sino por regla literal.**

| instruccion del encargo | lo que dice la regla, leida por mi hoy | mi adjudicacion |
|---|---|---|
| seccion `6`, *escribe `PARA_ALEXIS.md`* | `D.28` (`docs/BANCO_DE_REGLAS.md`), **RATIFICADA POR EL FUNDADOR**: *`docs/loop/PARA_ALEXIS.md` LO ESCRIBE EL AUDITOR, Y SOLO EL. El extractor que quiera parar lo declara en SU REPORTE.* Y `EXTRACTOR.md` `7` (*Tu no escribes `PARA_ALEXIS.md`*) y su tabla de sedes de `14` | **BIEN DECLINADA** |
| seccion `6`, *corre `forja.py credito --anotar`* | `D.48`: *escribir ahi tu tanda es parte de cerrar el acta*, y cada suceso **cita un `ACTA` como su fuente**. **El extractor no escribe actas.** `5.6`: `ACTA_AUDITOR.md` es sede del auditor | **BIEN DECLINADA** |

**Y LA RAZON DE FONDO ES LA QUE `D.28` DEJO ESCRITA PARA TODOS LOS CASOS, no solo para el
suyo:**

> **UN ENCARGO ASIGNA TRABAJO; NO MUEVE UNA SEDE.**

**LO QUE CIERRA LA DISCUSION, Y ES DEL PROPIO `D.28`:** *`D.13` no rescata al encargo por ser
mas reciente... **una formula arrastrada en una plantilla no es una regla fechada.*** La
seccion `6` de este encargo **es exactamente una formula de cierre arrastrada**: pide las dos
cosas juntas, en el bloque de cierre, sin decir en ningun sitio que mueva una sede. **Si el
fundador quisiera moverla lo escribiria como regla**, y entonces `D.13` si arbitraria.

**LO QUE ESO ME DEJA A MI, Y LO HAGO EN ESTE MISMO TURNO:** escribir `PARA_ALEXIS.md`
(seccion `7`) y anotar la tanda con `--anotar` (seccion `8.3`). **No es una queja al encargo:
es que las dos cosas eran mias desde el principio.**

> **Y LE FIRMO TAMBIEN LA FORMA EN QUE LO DECLINO**, porque es la mitad que se suele hacer
> mal: **no trato la vuelta entera como parada** (las cinco tareas de extraccion se
> completaron), **midio y publico las dos cosas que yo necesitaba** para actuar (el estado de
> cierre en `G9.5.b`, la racha en `G9.6.i.2`), **y dejo las citas delante para que la
> relectura las encontrase primero.** Es literalmente lo que `D.28` elogia de la vuelta `1`.

---

### 5.1. MIS PROPIOS ERRORES, CON MI NOMBRE (`5.3`)

**TRES, Y LAS TRES LAS CACE YO ANTES DE COMMITEAR, QUE ES LO UNICO QUE LAS HACE UTILES.**
La metrica que solo encuentra fallos ajenos no es una metrica.

#### 5.1.a. **LA QUE SI LLEGA AL COMMIT: escribi `de 3` donde el tope es `2`, en el registro de credito**

**Al anotar mi tanda con `--anotar` le pase `--racha "0 de 3"` a las cinco especies.** Y el
tope de tres de ellas **es `2`, no `3`**: lo dicen `5.2` y `5.4` de este protocolo, y lo dice
el propio instrumento, que trae la tabla dentro:

    $ sed -n '/^TOPES = {/,/^}/p' src/credito.py
    TOPES = {
        "CLASE": 2,
        "DATO MOVIDO": 2,
        "CIFRA PUBLICADA": 2,
        "REPORTE": 3,
        "AUDITOR": 3,
    }

**Y LA RACHA ESCRITA GANA A LA TABLA**, que es lo que lo convierte en una cifra y no en un
descuido de forma: `src/credito.py` usa `TOPES` **solo cuando la linea no declara el suyo**,
asi que mi `de 3` **reemplazo el `2` de la doctrina en la sede**. El instrumento lo publicaba
asi:

    CIFRA PUBLICADA    0 de 3     ACTA G9
    CLASE              0 de 3     ACTA G9
    DATO MOVIDO        0 de 3     ACTA G9

**CORREGIDO EN EL MISMO TURNO, Y SIN BORRAR:** el registro es de solo anadir, asi que **las
tres lineas malas se quedan en `docs/loop/CREDITO_gerber_emyth.jsonl` y encima van las tres
buenas**, con cita a esta seccion. Hoy el instrumento publica lo que debe:

    $ python forja.py credito | sed -n '5,11p'
      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA G9
      CIFRA PUBLICADA    0 de 2     ACTA G9
      CLASE              0 de 2     ACTA G9
      DATO MOVIDO        0 de 2     ACTA G9
      REPORTE            0 de 3     ACTA G9

**QUE ESPECIE ES, Y LO RAZONO CONTRA MI.** `D.38.2` cierra mis dos especies en **`REMEDIO
ROTO`** y **`CIFRA PUBLICADA PROPIA`**, y define la segunda como **una cifra falsa en TU ACTA
o en TU APERTURA SELLADA**. Esta vivio en `docs/loop/CREDITO_gerber_emyth.jsonl`, **que no es
ninguna de las dos**, y **mi acta publica el `de 2` correcto en `4.3` y en `PARA_ALEXIS.md`
`2.b`**: fue justamente esa discrepancia entre mi acta y el registro la que me la hizo ver.
**Por sede, no mueve mi racha**, que se queda en `0 de 3`, **y es la misma lectura con la que
la `ACTA G8` `5.2` cerro su `d132`.**

> **DEJO LOS DOS ELEMENTOS A LA VISTA PARA QUIEN QUIERA LEERLO AL REVES, porque soy el
> beneficiado:** que la cifra era falsa cuando se escribio, y que
> `docs/loop/CREDITO_gerber_emyth.jsonl` **vive bajo `docs/`, que `5.2` nombra como sede de
> `CIFRA PUBLICADA`**. **Si el siguiente lector adjudica que la sede alcanza, mi racha sube a
> `1 de 3` y la correccion la firma el.** Lo que no hago es dejarlo sin escribir.
>
> **Y LO QUE NO ME ABSUELVE NI UN POCO:** con las cinco en `0`, un tope mal escrito no cambia
> nada hoy. **Cambiaria el dia que una especie llegue a `2`**, que es exactamente el dia en
> que el bucle tendria que pararse y no lo haria.

#### 5.1.b. **La que no llego al commit: una cifra de coste copiada de la `ACTA G8` en vez de corrida**

Esta en la seccion `6`, escrita en su sitio y sin borrarla: pegue **`4` turnos y `37,8592`
total** porque los copie de mi acta anterior, y **los de hoy son `10` y `127,0533`**.
**`AUDITOR_FORJA.md` `1` lo dice con todas sus letras**: *toda cifra o nombre propio que
publiques se lee de la salida del instrumento corrido EN ESTA VUELTA.*

#### 5.1.c. **La tercera: un `grep -c` que se cazaba a si mismo**

Esta en la seccion `0`, tambien en su sitio. Mi primera version de la evidencia de herencia
pegaba **`0`** donde el comando da **`1`**, porque la `ACTA G8` **cita** la cadena que yo
buscaba. **Lo corri antes de pegarlo**, cambie el `grep` a anclado y **deje la nota escrita**
en vez de quedarme con el numero bonito.

> **LO QUE LAS TRES TIENEN EN COMUN, Y ES MI PATRON:** las tres son **cifras de forma**, no de
> lectura. Mi lectura del libro y mi recomposicion de las fronteras aguantaron; **lo que se me
> escapa son los argumentos de los instrumentos que yo mismo corro.** Lo dejo medido aqui para
> que el siguiente auditor de este bucle lo lea antes de escribir sus propias cinco lineas de
> `--anotar`.

---

## 6. LO QUE REGISTRO Y NO ABRE COLA (`D.55`, `D.56`)

**La cola de doctrina sigue en `11` y esta acta no la toca.** Lo que mido y no adjudico va a
`docs/loop/DEUDA.jsonl` con su cita:

    $ python scripts/deuda.py | sed -n '3p'
      pendientes: 51    pagadas: 40

| id | que mido | por que no lo arreglo aqui |
|---|---|---|
| **`d134`** | `scripts/tallar_reporte.py` no reconoce ninguna de las `7` cabeceras de este frente, asi que la guarda `D.59` barre `4783` lineas de historia en vez de las `683` de la vuelta viva (`4.2`) | **maquinaria, vedada desde un frente** (`D.45`, `D.47`): se mide y se sube |
| **`d135`** | los dos tramos que mas compiten en `cap_03` (`L169`, `L201`) no son el que `G9.4.d` defiende, y el mismo ejemplar en `cap_01` `L29`/`L39` (`4.1`) | la sede es del extractor (`5.6`): **yo no escribo en su reporte**, y **el veredicto no cambia** |
| **`d136`** (la firma) | `minados_en_cero` de `config/frentes.json` trae `9` capitulos y le faltan `cap_01`, `cap_02` y `cap_03`; sin ellos el tablero se queda en `19` de `22` (`3.2`) | **`config/` no es sede del auditor** (`5.6`): **la firma esta escrita en `3.2` y la peticion va en `PARA_ALEXIS.md`** |

**GUARDA DE DATO EN ROJO: NINGUNA** (`1.1`: las cinco verdes, corridas por mi), asi que **cero
tareas bloqueantes** (`D.55` deja una, y solo con guarda de DATO en rojo). **Y no habria donde
ponerla: esta acta no escribe encargo.**

**EL COSTE, QUE `D.55` ME MANDA DECIR SI PASA DE `10`:** el turno del extractor costo
**`9,287955`** USD en `2153` segundos, **por debajo de `10`, asi que no hay desglose que dar**:

    $ grep -n "extractor listo" docs/loop/loop.log | tail -1
    1190:[2026-09-21 18:22:23] extractor listo (USD 9.287955299999997), 2153s, intento 1 de 7

**Mi propio turno lo escribe el arnes en `docs/loop/ultimo_auditor.json` cuando yo ya he
terminado**, asi que no puedo publicarlo aqui sin inventarlo (`D.38.2`: lo que la tuberia
escribe despues de mi turno no lo controlo). **Lo que si mido es la media que el instrumento
ya lleva**, y la pego en vez de estimarla:

    $ python forja.py tablero | grep -A2 "vueltas 4 a 8"
        gerber_emyth, vueltas 4 a 8 del frente            12.7053 USD/turno
          10 turnos, 127.0533 total     extractor  57.6979  |  auditor  69.3553
          extractor claude-sonnet-5, auditor claude-opus-5

> **Y AQUI ME CAZO A MI MISMO ANTES DE COMMITEAR, QUE ES LA MITAD QUE IMPORTA.** La primera
> version de este bloque pegaba **`4` turnos y `37,8592` total**, que son las cifras que la
> `ACTA G8` publico. **No las corri: las copie.** `AUDITOR_FORJA.md` `1` lo dice con todas sus
> letras (*toda cifra que publiques se lee de la salida del instrumento corrido EN ESTA
> VUELTA*), y las de hoy son **`10` turnos y `127,0533`**. **No llego a ser `CIFRA PUBLICADA
> PROPIA` porque no se commiteo**, pero **la dejo escrita** en vez de borrarla: lo que esta
> regla vigila es si me verifico, y la prueba de que me verifico es esta nota.

---

## 7. LAS CONDICIONES DE PARADA, REPASADAS UNA A UNA (`AUDITOR_FORJA.md` `3`)

| condicion | lo que mido en este turno | veredicto |
|---|---|---|
| **doctrina NUEVA necesaria** | ninguna: los tres cero se adjudican **citando `9.1` y el manual `3.5`**, que es extension natural de regla escrita; las dos instrucciones declinadas se adjudican **citando `D.28` literal**. La cola sigue en `11` | **NO** |
| **contradiccion con regla o cifra vigente** | las dos discrepancias de cifra (tallado y censo, `1.1`) **se resuelven con la jurisprudencia de la casa sin doctrina nueva**, y las mido en vez de suponerlas | **NO** |
| **fallo tecnico repetido** | `gate`, `guiones`, `tests`, tallado y censo **VERDES hoy, corridos por mi** (`1.1`) | **NO** |
| **credito roto** | las cinco rachas en `0` (`1.5`), y la unica caida de la tanda **no acumula** (`4.1`) | **NO** |
| **DECISION DE ALEXIS** | **SI, Y SON TRES.** `(a)` fundir esta rama a `extraccion-mundo-11`, que el propio encargo anuncia en su seccion `0` y que `D.50` paso `(b)` reserva al fundador: **el bucle no funde ramas**; `(b)` firmar `cap_01` a `cap_03` en `config/frentes.json`, sede que `5.6` no me da (`3.2`); `(c)` `d134`, maquinaria vedada por `D.45` | **SI, PARA** |
| **campania consumada** | **el libro esta minado `22` de `22` y no le queda una sola unidad que este frente pueda tomar** (`8`). `PARALELO.md` `5.0.b` paso `(a)` pide **su `PARA_ALEXIS.md` en el arbol** para que el relevo empiece | **SI, PARA** |

**SE CUMPLEN DOS, Y NINGUNA ES DE CREDITO. ES LA PARADA FELIZ.** Escribo
`docs/loop/PARA_ALEXIS.md` y **dejo `docs/loop/PROMPT_SIGUIENTE.md` VACIO**, que es
exactamente lo que el encargo pide en su seccion `6`.

---

## 8. EL LOTE `9` CERRADO, Y LAS DOS CONDICIONES DE `D.32` MEDIDAS PARA CADA CANDIDATO

### 8.1. El estado del lote, contado por mi

    $ ls fuentes/gerber_emyth/*.md | wc -l
    22
    $ python <cuenta propia de nodos del grafo por libro>
    nodos de dataset/nodos.jsonl : 346   de ellos que nombren 'gerber_emyth': 0

| | unidades | cuales |
|---|---:|---|
| **minadas por este frente** | **`22`** | `cap_01` a `cap_22`, **sin un solo hueco**: `19` hasta la `ACTA G8` mas las `3` de esta vuelta |
| **sin minar** | **`0`** | ninguna. `d094`, que apartaba las tres, **esta pagada** (`1.5`) |
| **en la bandeja, sin insertar** | **`22` candidatos, `176` pasos** | `cuarentena/gerber_emyth/`, `0` en el grafo, **las `22` con su `UNIDAD DE ORIGEN` declarada** (`2`) |

**`D.32` MANDA ABRIR EL LOTE SIGUIENTE SI SUS DOS CONDICIONES ESTAN VERDES, Y AQUI NO SE ABRE
NINGUNO. Publico las dos medidas de cada candidato, que es lo que la regla pide, y el tercer
bloqueo de cada uno, que es el que manda:**

| clave | material en `fuentes/<clave>/` | en la tabla canonica | `--puedo` corrido hoy | **se puede abrir** |
|---|---:|---|---|---|
| `gerber_emyth_cap17_reservado` | **`1`** | **SI** | **`SI`**, *SIN EMPEZAR y sin dueno* | **NO.** `ORDEN_DE_LOTES.md` `L27`: lote `11`, **RESERVADO, entra el ultimo**, y su condicion escrita es entrar **cuando su propio libro ya este en el grafo**: hoy hay **`0`** nodos de `gerber_emyth` en el grafo (`8.1`). **Medida, y NO se cumple** |
| `marquet_turn_the_ship` | **`17`** | **SI** | **`NO`**: *esta PAUSADO y NO COSECHADO, tiene `9` candidatos que todavia no han llegado a esta rama* | **NO.** `D.50` manda **relevarlo ENTERO**, y el relevo empieza por el paso `(b)`, **cosechar su rama, que es del fundador** |
| `grove_high_output` | **`18`** | **SI** | **`SI`**, *COSECHADO, continua desde el siguiente al ultimo minado (`cap_18`)* | **NO HAY NADA QUE CONTINUAR:** el tablero lo da con **`18` de `18` minados y `ultimo_capitulo` `cap_18`**. **El `SI` esta vacio** |
| `bernerslee_bananas`, `openstax_business_ethics`, `openstax_org_behavior` | `19`, `17`, `32` | **SI** las tres | **`SI`** las tres, *SIN EMPEZAR y sin dueno* | **NO.** El tablero las marca con **asterisco**, y su propia leyenda dice que eso es **`FUERA DE CAMPANIA: no se extrae, queda en bandeja para la aduana de a uno`**. Tomarlas es **cambiar el alcance**, que la casa reserva a Alexis |

**LAS DOS CONDICIONES DE `D.32` SALEN VERDES EN LAS SEIS CLAVES, Y AUN ASI NINGUNA SE ABRE.**
Es exactamente lo que `D.50` vino a impedir: **`D.32` abriria el siguiente sin parada entre
medias**, y por eso la regla mas reciente manda mirar el tablero antes.

### 8.2. Y una cosa que subo sin adjudicarla, porque no es mia

**`d125` se vuelve a mover, y la vuelvo a medir porque ha cambiado otra vez.**
`PARALELO.md` `4.d` corto este libro de la campania con el frente fotografiado en `10`
candidatos y `4` de `22` capitulos, sobre la premisa de que insertarlo *obligaria a minar los
dos libros enteros*. **Hoy el frente esta en `22` candidatos y `22` de `22` capitulos: ese
coste esta pagado ENTERO**, no en parte. **No adjudico nada con esto**, y el encargo de esta
vuelta dice que el fundador ya lo decidio en su seccion `0`: **lo unico que me toca es
ponerle la cifra final delante.**

### 8.3. Lo que este turno deja escrito, recomputado DESPUES de escribirlo

**Las cifras de `1.1` y `1.5` son las de la VERIFICACION, medidas antes de que yo escribiera
nada. Estas son las de DESPUES, y se publican las dos** (`D.38.3`: la discrepancia se
declara, no se resuelve copiando):

    $ python scripts/deuda.py | sed -n '3p'
      pendientes: 51    pagadas: 40
    $ python forja.py gate | head -2
    GATE VERDE.
      nodos verificados: 346
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python scripts/tallar_reporte.py | tail -1
    TALLADO VERDE: las 181 tabla(s) comprobables son las de su instrumento, celda a celda.
    $ python scripts/censar_rutas.py | tail -1
    CENSO VERDE: las 1162 rutas publicadas sostienen lo que dicen sostener.
    $ python forja.py credito | sed -n '5,11p'
      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA G9
      CIFRA PUBLICADA    0 de 2     ACTA G9
      CLASE              0 de 2     ACTA G9
      DATO MOVIDO        0 de 2     ACTA G9
      REPORTE            0 de 3     ACTA G9

**EL TALLADO NO SE MUEVE Y EL CENSO SUBE UNA, DE `1161` A `1162`**, porque esta acta y el
`PARA_ALEXIS.md` publican una ruta que antes no existia. **Es la misma figura que le declaro
a el en `1.1`, y por eso la mido yo tambien al final en vez de dejar la de arriba como si
fuese la ultima palabra.** `gate`, `guiones`, tallado y censo **siguen los cuatro en VERDE
con el acta ya escrita**.

**`48` mas las `3` que anoto en este turno dan `51`**, y ninguna la pago yo: `d135` la paga la
vuelta que vuelva a tocar el reporte, y `d134` y `d136` **no se pagan desde un frente**. El
censo sube **porque esta acta publica rutas que antes no existian**, que es la misma figura
que le declaro a el en `1.1` **y por eso la mido yo tambien al final.**

**Y MI TANDA ESTA ESCRITA** (`D.48`): cinco lineas en `docs/loop/CREDITO_gerber_emyth.jsonl`,
una por especie, **las cinco `--limpia`**, con su cita a la seccion de esta acta que la
sostiene. **Y esta vez la escribo yo de verdad**, que es la mitad practica de la adjudicacion
de la seccion `5`.

---

*`ACTA G9` cerrada. **CON PARADA, y es la feliz: el libro esta entero.** Lo que le firmo es
todo lo sustancial: **las `12` piezas de sus tres fronteras al digito con codigo mio**, los
tres bordes de abajo comprobados uno a uno, **los tres `CERO CANDIDATOS` con los tres
capitulos leidos enteros por mi**, la muestra identica a su semilla, **la cita verbatim fiel
a su fichero con la unica diferencia que `d124` autoriza**, `0` ficheros de dato movidos y `0`
de maquinaria. **Y le doy la razon en las dos instrucciones que declino**, citando el `D.28`
que el fundador ratifico. **Lo que se cae es una razon que se queda corta**, con el veredicto
intacto en los tres capitulos, **y la levanto leyendo el libro y no su argumento**: vive en
prosa y **no acumula**. **Lo que subo y no arreglo es una guarda que no ve este frente**, con
su medida pegada. **Este frente cierra con las cinco rachas en cero y `22` de `22` unidades
minadas. Cada cifra de esta acta lleva su comando pegado encima: se puede repetir entera sin
mi.***
