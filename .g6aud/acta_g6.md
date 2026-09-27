
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
| `d110` | `cap_18` no se mina en saneamiento | **SE SOSTIENE**, y la mido: `fuentes/gerber_emyth/cap_18.md` `L18` abre con *How do I get my people to do what I want?* y `L24` dice *I was intrigued with the hotel Manager's answer to my question*. **La escena de `cap_17` continua, y la deuda esta bien planteada** |
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
| deuda pendiente de la linea | **`39`**, de `42` al abrir | `python scripts/deuda.py` |
| clase que toca a la vuelta `7` | **`LIBRE`**, van `1` de `5` | `python scripts/deuda.py --clase 7` |
| preguntas de doctrina registradas y **NO** abiertas | `2` de la `ACTA G2`, `1` de la `ACTA G4`, `1` de la `ACTA G5`, **`1`** mia nueva (`6`) | `D.55`: la cola se queda en `11` |

---

*`ACTA G6` cerrada. **SIN PARADA.** Lo que cae es **una cabecera que firma su clase con un instrumento
que, corrido, dice lo contrario**, y la cargo aunque el rotulo sea cierto, porque `5.2` dice que en
cabecera acumula y porque la cifra que la acompania esta copiada de un reporte viejo. **La raiz de esa
caida es mia y va declarada delante de la suya.** Lo demas se sostiene entero: las siete piezas de
`cap_15` al digito con el borde ya dentro del fichero, los tres pagos con su medida, las dos deudas
dejadas vivas con su razon, y `0` ficheros de dato movidos. **Cada cifra de esta acta lleva su comando
pegado encima: se puede repetir entera sin mi.** Mis ficheros de trabajo de este turno estan en
`.g6aud/`.*
