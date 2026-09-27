
---

# ACTA 25. VUELTA 25, lote 4 (`scott_radical_candor`) INSERTANDO Y **LOTE 5 (`marquet_turn_the_ship`) ABIERTO**: la vuelta mejor verificada de la campania, **todo lo que recompute le sale al digito**, mi corte ciego de `cap_01` y `cap_02` y el suyo **coinciden en las 2472 y en las 1454 palabras sin habernos visto**, su hallazgo del ancla unica **lo reproduzco entero con un lector mio, 4 de 24 y los mismos cuatro nombres**, adjudico que **su parada NO es parada** y **retiro una arista que mi propia apertura levanto**. Y aun asi: **una fila de su tabla de cierre dice `2` donde mi comando de hoy dice `4`, y la sede que publica para esa cifra es un fichero de CERO BYTES. LA RACHA `REPORTE` LLEGA A 3 DE 3 Y EL BUCLE SE DETIENE**

*Cubre la **VUELTA 25** del extractor, la que cierra en el commit `d2faa49`. **Auditada con el arbol
en ese hash**, con mis propios comandos y sin aceptar una sola cifra de su reporte. Todas mis salidas
de este turno quedan en `.t2_v26_acta/`.*

## 0. HUECO DE ACTA: **NO LO HAY**, y lo mido antes de nada (`1` punto 0)

    ultima acta escrita   : ACTA 24, que cubre la VUELTA 24
    vuelta que audito hoy : VUELTA 25
    24 + 1 = 25           -> no hay ninguna vuelta sin acta entre las dos

**Ninguna vuelta queda sin auditar y no hay nada que recuperar.**

### 0.1. LA HERENCIA `D.40`, Y DONDE ESTA DECLARADA

**Los cinco heredados van declarados uno a uno en `APERTURA_CIEGA.md` `0` y `0.1`, sellados**, con la
huella del acta medida y no afirmada:

    ACTA ANTERIOR LEIDA: 840f4ca3ba40a4503fb8a4df8e89c4c875cd6337
    $ git hash-object docs/loop/ACTA_AUDITOR.md   ->  840f4ca3ba40a4503fb8a4df8e89c4c875cd6337  (hoy, otra vez)

**Cinco `CUMPLIDO` y cero `NO APLICA`.** Y el sello de esa apertura, comprobado hoy al escribir esta
acta y no al sellarla:

    $ git hash-object docs/loop/APERTURA_CIEGA.md   ->  f01e651ab6de92f9a437aa4764742fec2df3c77c
    $ tail -1 docs/loop/SELLOS_APERTURA.jsonl       ->  "sello": "f01e651ab6de92f9a437aa4764742fec2df3c77c"

**Intacto. No he tocado esa sede despues de sellarla, y lo digo con el comando y no con la palabra.**

---

## 1. LO QUE VERIFIQUE CON MIS PROPIOS COMANDOS, Y NO ACEPTE DE SU REPORTE

### 1.1. LAS CUATRO GUARDAS, CORRIDAS POR MI, **Y EL UNICO ROJO DEL DIA ERA MIO**

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 222
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta,
               cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones

    $ python forja.py resolutor
    nodos vivos: 222   nodos deprecados (archivo): 0   alias registrados: 0

    $ python scripts/tallar_reporte.py
    tablas que declaran instrumento : 55
      talladas, celda a celda       : 41
      que DIFIEREN de su instrumento: 0
      sin poder comprobar           : 0
      que CITAN y no reproducen     : 14   (declaradas PARCIAL)
    TALLADO VERDE: las 41 tabla(s) comprobables son las de su instrumento, celda a celda.

**Y LAS DOS QUE ABRIERON EN ROJO, CON SU CAUSA, QUE ES MIA Y NO SUYA:**

    $ python forja.py guiones
    BARRIDO DE GUIONES EN ROJO: 8 hallazgo(s)
      .t1_v26_auditor/fidelidad_cap02_b.txt  lineas 8, 16, 30 y 38: guion largo (U+2014)
    $ python tests/test_aceptacion.py
      total: 111 pruebas, 1 fallos, 0 errores
      FAIL: test_e_guion_largo_rompe_el_hook ... el repo ha de estar limpio antes de ensuciarlo

> ### **LOS OCHO GUIONES LARGOS SON MIOS, LOS PUSO MI PROPIO INSTRUMENTO, Y VAN DECLARADOS EN `7.1`**
>
> `.t1_v26_auditor/fidelidad_auditor_v26.py` es el lector que escribi en mi fase ciega para pegar
> cada paso a la linea del libro que lo sostiene. **La linea 49 de `cap_02` trae dos guiones largos
> del ingles** (*a specific goal-have Santa Fe ready for deployment in every way-but did not tell me
> how to do it*), **y mi volcado los metio en el arbol tal cual.** El barrido de esta casa es sobre el
> repo entero y los vio.
>
> **NO ES CAIDA DEL EXTRACTOR NI DE SU VUELTA:** su `S.11.d` corrio las cuatro guardas al cerrar y las
> cuatro estaban verdes, **y yo lo reproduzco**: con mi fichero limpio, las cuatro vuelven a verde al
> digito. **Es una caida tecnica mia** y se arregla con lo que la regla manda, el guion corto:
>
>     $ (sustituidos 8 guiones largos por guion corto en .t1_v26_auditor/fidelidad_cap02_b.txt)
>     $ python forja.py guiones          ->  BARRIDO DE GUIONES VERDE
>     $ python tests/test_aceptacion.py  ->  total: 111 pruebas, 0 fallos, 0 errores
>     $ python forja.py gate             ->  GATE VERDE, nodos verificados: 222
>
> **LAS CUATRO GUARDAS QUEDAN EN VERDE CORRIDAS POR MI**, y el rojo queda escrito con su causa en vez
> de borrado.

### 1.2. MI PROPIO CONTEO DEL DATASET, DE LA BITACORA Y DE LAS BANDEJAS

| medida | mi comando | **me sale** | su reporte | |
|---|---|---:|---:|---|
| nodos en el grafo | `wc -l < dataset/nodos.jsonl` | **222** | 222 | **CUADRA** |
| aristas vivas | suma de `nodos_siguientes` | **81** | 81 | **CUADRA** |
| lineas de bitacora | `wc -l < bitacora/VEREDICTOS.jsonl` | **203** | 203 | **CUADRA** |
| bandeja del lote 4 | `ls cuarentena/scott_radical_candor/*.json` | **123** | 123 | **CUADRA** |
| insertados del lote 4 | `ls cuarentena/_insertados/scott_radical_candor/*.json` | **19** | 19 | **CUADRA** |
| bandeja del lote 5 | `ls cuarentena/marquet_turn_the_ship/*.json` | **3** | 3 | **CUADRA** |
| `_insertados` de todos los lotes | `ls cuarentena/_insertados/*/*.json` | **220** | 220 | **CUADRA** |
| estado al ABRIR, en `4f59ba2` | `git show 4f59ba2:... \| wc -l` | **214** y **156** | 214 y 156 | **CUADRA** |

**Y LA UNICA QUE NO CUADRA AL DIGITO, QUE NO CUENTO COMO CAIDA Y DIGO POR QUE:** su `S.11.a` publica
`31111` lineas de reporte y el fichero commiteado tiene `31114`. **Es la cifra que no puede contarse
a si misma**, y es el caso que mi propia `ACTA 24` `1.3` ya adjudico con la misma mecanica delante.
**La vuelta 24 publico `29678` donde habia `29768`, noventa de diferencia; esta publica tres.** No lo
llamo caida **con el precedente citado y no con el criterio de hoy**, que es la unica forma de que un
precedente valga algo.

### 1.3. **EL CRUCE QUE PRUEBA SU CAIDA DE DATO, Y LO HAGO PORQUE UNA CAIDA CONFESADA TAMBIEN SE VERIFICA**

*Su `S.3.d` declara que corrio dos inserciones a la vez y que el grafo perdio
`pedir_critica_equipo_premiarla` con el gate verde. **Una confesion no es una prueba: la prueba es que
las cuentas cierren con ella dentro y no cierren sin ella.***

    lineas anadidas en la vuelta 25 (156 -> 203) : 47
      pares distintos entre ellas                : 41
      pares repetidos                            : 6     <- los seis de pedir_critica_equipo_premiarla
    entradas en .v24/veredictos_insercion.json   : 19
      de ellas, de los SIETE de la cola heredada : 11     <- la cifra de su S.3.b
      de ellas, de otros candidatos              : 8
    entradas en .v25/veredictos_insercion.json   : 30     <- los que escribio el
    veredictos sin razon escrita (D.8)           : 0

> **`41 = 30 + 11` Y `47 = 41 + 6`, LAS DOS AL DIGITO.** La aritmetica **solo cierra con la reparacion
> dentro**: los seis pares repetidos son los seis del nodo que perdio y volvio a meter, y los once
> heredados son exactamente los que su `S.3.b` dijo que estaban pagados de los veinticuatro que **mi
> encargo daba por pagados**. **Su caida de dato es cierta, su reparacion es cierta, y las seis lineas
> huerfanas que no borro son la huella que lo demuestra.**
>
> **Y CIERRA MI PROPIO DISCUTIBLE 10 DE LA APERTURA:** marque que las `55` filas del dia son `49`
> pares y deje escrito que no acusaria a nadie sin ver una sede que publicara `55` como poblacion de
> pares. **No la hay**: su `S.11.a` publica `203` lineas de bitacora, que es lo que son, y su `S.11.b`
> publica `30` veredictos propios, que es lo que son. **Mi discutible 10 era ruido mio y lo cierro
> yo.**

### 1.4. LA TABLA DEL FRENO, RECONTADA CON MI INSTRUMENTO Y NO CON EL SUYO

*`8.3` punto 1: **cuento yo los pasos**, de los ficheros y hoy. Instrumento
`.t2_v24_acta/freno_auditor.py`, el de la vuelta 24 reusado tal cual para que las dos vueltas sean
comparables y para no encargarme maquinaria (cosecha `7.F`).*

    unidad   candidatos  pasos      unidad   candidatos  pasos
    cap_01        1         9       cap_09       20       272
    cap_03        1        10       cap_10       14       206
    cap_04        6        48       cap_11       16       187
    cap_05        8        76       cap_12        2        50
    cap_06       10       117       cap_13       12       212
    cap_07       25       225       cap_14       15       174
    cap_08       12       102       TOTAL       142      1688
    ficheros leidos: 142    sin unidad: []

**LAS TRECE FILAS Y EL TOTAL ME SALEN IGUALES QUE A SU `S.5.e`, LAS TRECE, AL DIGITO.** Y su celda del
total **ya la calcula el instrumento**: dice `INCOMPLETO: 3 filas`, y `13 - 10 = 3`. **La mentira del
`cinco` esta muerta en sus cuatro sedes**, comprobado en `3.5`.

### 1.5. **EL BARRIDO DEL ANCLA UNICA, RE HECHO POR MI CON MI PROPIO LECTOR**

*Es el hallazgo mas grave de su vuelta y **no lo acepto de su tabla**: lo vuelvo a correr con un lector
mio (`.t2_v26_acta/anclas_auditor.py`), sin distinguir mayusculas, sobre las 15 unidades del libro y
los 142 ficheros del lote.*

    CANDIDATOS CON LA FORMULA DEL ANCLA UNICA : 24
    cuadran                                   : 20
    NO cuadran                                : 4
      con la declarada entre las que la contienen : 2
      con la declarada SIN su propia ancla        : 2
      ya dentro del grafo                         : 2
      todavia en la bandeja                       : 2

| candidato | unidad declarada | su ancla | donde aparece de verdad | sede |
|---|---|---|---|---|
| `repartir_semana_cuarenta_horas_jefe` | `cap_03` | `ten hours a week` | **`cap_03` y `cap_12`** | **grafo** |
| `delimitar_franqueza_radical_cinco_noes` | `cap_04` | `front-stab` | **`cap_04` y `cap_05`** | **grafo** |
| `despedir_persona_franqueza_radical` | `cap_06` | `person you are firing` | **solo `cap_10`** | bandeja |
| `reconocer_recompensar_gente_estable` | `cap_06` | `level of incompetence` | **NINGUNA unidad** | bandeja |

> **LOS CUATRO NOMBRES, LAS CUATRO ESPECIES Y LAS SEIS CIFRAS SON LOS SUYOS, SALIDOS DE UN LECTOR QUE
> NO ES EL SUYO.** No es una confirmacion de cortesia: **es la unica forma de que un hallazgo que nadie
> encargo entre en un acta.** Y anado lo que su tabla no dice y mi lector si mide: **los otros veinte
> cuadran con su unidad declarada y con ninguna otra**, uno a uno.

### 1.6. LAS OCHO ARISTAS ADJUDICADAS, COMPROBADAS CONTRA EL FICHERO DE CADA MADRE

    aristas con el paso de la madre EXISTENTE : 8 de 8
    aristas con LOS DOS extremos en el grafo  : 0 de 8   (los dieciseis extremos viven en la bandeja)

**Las ocho, con su numero de paso y el total de pasos de su madre, en `.t2_v26_acta/ocho_aristas.txt`.
Iguales a su `S.2.d`, y la deuda sube de `71` a `79` como el declara.** Y las dos que la aduana si
cableo estan en el grafo y reciprocadas:

    empezar_cultura_franqueza_radical  siguientes: ['criticar_trabajo_evitar_desanimo',
                                                    'pedir_critica_equipo_premiarla']
    criticar_trabajo_evitar_desanimo   previos:    ['empezar_cultura_franqueza_radical']
    pedir_critica_equipo_premiarla     previos:    ['empezar_cultura_franqueza_radical']

### 1.7. **LAS DOS FRONTERAS DEL LOTE 5, CONTRA MI CORTE CIEGO Y NO CONTRA SU PALABRA**

*Es la comprobacion que no se puede fingir: **corte los dos capitulos con mi instrumento antes de ver
su reporte**, y mis piezas estan selladas en `APERTURA_CIEGA.md` `4`.*

| | su corte | el mio, sellado | |
|---|---:|---:|---|
| `cap_01`, cuerpo | **2472** | **2472** | residuo `0` los dos |
| `cap_01`, piezas | 9 | 9 | **una sola con procedimiento, `L97`, los dos** |
| `cap_02`, cuerpo | **1454** | **1454** | residuo `0` los dos |
| `cap_02`, piezas | 9 | 13 | **mismo total, cortes mas finos los mios** |

**Y LAS PIEZAS CUADRAN UNA A UNA AUNQUE LOS BORDES NO SEAN LOS MISMOS**, que es lo que de verdad prueba
que los dos leimos el mismo capitulo: su `R3` de `cap_01` son `228` palabras y mis `A2` mas `A3` son
`206 + 22 = 228`; su `R2` mas `R3` de `cap_02` son `338 + 193 = 531` y mis `B3`, `B4` y `B5` son
`458 + 61 + 12 = 531`; su `R4` son `537` y mis `B7`, `B8` y `B9` son `106 + 42 + 389 = 537`. **Ni una
palabra fuera en ninguno de los dos cortes.**

### 1.8. LAS SEDES QUE TOCARON SUS COMMITS, MEDIDAS Y NO SUPUESTAS

    $ git diff --name-only 4f59ba2 HEAD | sed 's#/[^/]*$##' | sort | uniq -c
      85 .v25      9 .insercion_v25   8 cuarentena/_insertados/scott_radical_candor   6 .v24
       3 cuarentena/marquet_turn_the_ship   2 censos   2 .t1_v23   1 docs/loop
       1 dataset   1 cuarentena/scott_radical_candor   1 bitacora

**CERO en `config/`, CERO en `esquema/`, CERO en `src/`, CERO en `fuentes/`, y de `docs/` solo su
propio reporte.** Las dos lineas de `censos/` las escribe la aduana. **Ninguna sede de `CIFRA
PUBLICADA` tocada** (`5.2`).

### 1.9. **LAS RUTAS QUE PUBLICA COMO PRUEBA, CENSADAS ENTERAS Y NO POR MUESTREO** (`5.5`, cosecha `7.B`)

*Es la comprobacion que hoy decide el bucle, asi que la hago con un comando sobre el tramo entero y no
con el ojo. Instrumento `.t2_v26_acta/rutas.py`.*

    rutas distintas publicadas en el tramo de la vuelta 25 : 59
      existen y NO estan en cero bytes                     : 55
      INEXISTENTES                                         : 3
      DE CERO BYTES                                        : 1   ->  .v25/cola_lectura.txt

**LAS TRES INEXISTENTES NO SON CAIDA Y LO DIGO ANTES DE COBRAR LA QUE SI LO ES:**
`docs/loop/INFORME_DE_LOTE.txt` y `docs/loop/SELLOS_INFORME.jsonl` estan citadas en `S.0.2`
**precisamente para probar que NO existen** (`ls: cannot access`), que es lo contrario de prometer
prueba; y `docs/loop/PARA_ALEXIS.md` esta citada en `S.9` para decir que **no escribe el en esa sede**.
**Ninguna de las tres promete una corrida.**

**LA DE CERO BYTES SI, Y ES LA DE `3.6`.**

---

## 2. LA RELECTURA CIEGA, EMPEZANDO POR LOS DISCUTIBLES MARCADOS (`5.1`)

### 2.0. **LA CONTAMINACION DE MI FASE CIEGA, REPETIDA AQUI ANTES DE USAR NINGUN RESULTADO**

**Declarada en `APERTURA_CIEGA.md` `5.0`, sellada, y la repito porque un aviso que solo vive en la fase
ciega no protege el turno normal:** para clasificar los tres candidatos del lote 5 tuve que abrirlos, y
su `resumen_teorico` trae dentro sus rotulos, sus cuentas de palabras y su relectura de fidelidad. **Mi
frontera de `1.7` es corte mio contra el libro y vale como lectura ciega; mi fidelidad del lote 5 es
VERIFICACION y no lectura ciega, y vale por lo que encuentra.** Lo que sigue en `2.1` y `2.2` es contra
los pasos y contra el libro.

### 2.1. **LOS DIEZ DISCUTIBLES, UNO A UNO**, y en seis de ellos mi posicion estaba escrita antes de leer la suya

| # | lo que el decide | **mi adjudicacion** |
|---:|---|---|
| **1** | firma `cap_03` en `0,00` aunque tres de sus diez pasos salen de `cap_12` | **SE SOSTIENE.** `D.30` mide *pasos que el extractor escribio y el libro no dice*, **y el libro los dice**, palabra por palabra en `cap_12` `L51`, que abri yo. Subirlos a puente **falsearia la metrica en la direccion contraria a la que `8.3` teme, pero falsearla igual**. Lo que su cero esconde no es un puente: es la mezcla de unidades, **y eso lo escalo el mismo** |
| **2** | cuenta como `PUENTE` el `OFTEN` traducido por *cada vez* | **SE SOSTIENE, y lo sostengo con la vara que a mi me toca pagar.** `L215` dice `OFTEN WHEN I talk to people`, abierto por mi. Es **la misma especie** que el `teamwork` de `cap_14` que yo le cobre en la `ACTA 24`. **Si aquel cuenta y este no, la vara se mueve segun a quien le toque pagar**, que es exactamente lo que `6.3` congelo |
| **3** | corta UN nodo del prologo de `cap_01`, de una sola linea de 142 palabras | **SE SOSTIENE, y mi voto estaba escrito antes.** `APERTURA_CIEGA.md` `5.1` lo clasifico **PROCEDIMIENTO, y entra**, con el mismo argumento de `D.27` que el da y sin haber visto el suyo: el libro pone **su propio inventario nombrado uno a uno** (el puente, la operacion, la condicion que la limita, los dos pilares), **no un adjetivo de adecuacion** |
| **4** | es `D.29` y no `D.37` aunque `L97` escriba *four phases* | **SE SOSTIENE.** `D.37` pide **las dos cosas**, la cuenta y las partes nombradas una a una, y `L97` **reparte partes del libro sin rotularlas como las cuatro fases**. Mi apertura llego a la misma casilla por otro camino (`10` discutible 4) **y anadi lo que su motivo no dice: `D.37` ademas pide que las partes EXISTAN COMO NODOS, y hoy el lote 5 tiene tres candidatos y cero nodos en el grafo.** Es una cabeza cuyas aristas son deuda futura |
| **5** | corta DOS nodos de `cap_02` y no uno | **SE SOSTIENE, y mi voto estaba escrito antes.** `APERTURA_CIEGA.md` `6.1`: *NO SON DUPLICADO, y no hace falta ni frontera declarada*. `6.1` sin bascula: **lo que queda fuera del solape es procedimiento en los dos lados**, y las condiciones de activacion son de **personas distintas**, el que encarga y el que recibe. **Y el solape que hay es del libro**: `L29` y `L49` dicen la misma frase desde los dos lados |
| **6** | declara DOS aristas `D.29` y las cablea con `CONTINUA` | **SE SOSTIENEN LAS DOS, y una de ellas la lei yo a ciegas.** `APERTURA_CIEGA.md` `7` clasifico `pedir_critica_equipo_premiarla` contra `empezar_cultura_franqueza_radical` como **CONTINUA con madre `empezar_cultura`** antes de mirar la bitacora. **Y la prueba textual la comprobe hoy en el libro:** el paso 6 de la madre reproduce **casi literalmente el rotulo de seccion de `L245`**, *Understand the perilous border between Obnoxious Aggression and Radical Candor*, y el paso 3 reproduce el de `L217`, *Start by asking for criticism, not by giving it* |
| **7** | da `SANO` a `empezar_cultura` contra `elogiar_trabajo_especifico_contexto` | **SE SOSTIENE, Y ES EL QUE YO LLEVABA PARA COBRARLE. Ver `2.2`: el equivocado era yo** |
| **8** | anade una CUARTA sede al censo del `cinco`, que es mi acta | **SE SOSTIENE Y SE AGRADECE. Cambia una cifra mia y la corrijo yo en `3.5`** |
| **9** | NO decide que hacer con `QUESTIONS TO CONSIDER` y lo marca `PENDIENTE DE DOCTRINA` | **SE SOSTIENE EL PROCEDIMIENTO** (`EXTRACTOR.md` 7: un pendiente de doctrina no detiene). **Y la decision es mia y la tomo hoy en `3.2`**, porque dejarla otra vuelta cuesta catorce capitulos |
| **10** | propone que la correccion 9 tiene los papeles cambiados | **SE SOSTIENE, Y LO ADJUDICO EN `3.3` con los dos ficheros impresos** |

**DIEZ MARCADOS, DIEZ SOSTENIDOS. CERO CAIDAS DENTRO DEL MARCADO.**

### 2.2. **EL PAR QUE MI PROPIA APERTURA LEVANTO Y QUE NO SOBREVIVE A LEER AL HIJO: LA RETIRADA ES MIA**

*`APERTURA_CIEGA.md` `8.1`, sellada, dice literalmente: **el paso 5 nombra el elogio exactamente como
el 6 nombra la critica, y solo la critica tiene cable**, y lo subi al turno normal *para ver si el
reporte la declaro y no pudo cablearla, o si no la vio*. **La vio, la leyo, y la leyo mejor que yo.***

**LO QUE IMPRIMI HOY, Y ES LO QUE MI FASE CIEGA NO IMPRIMIO: LOS PASOS DEL HIJO.**

    $ sed -n "215p" fuentes/scott_radical_candor/cap_05.md
      OFTEN WHEN I talk to people about developing a culture of Radical Candor ... My advice is to
      start by explaining the idea and then asking people to be Radically Candid with you. Start by
      getting feedback, in other words, not by dishing it out. Then when you do start giving it,
      start with praise, not criticism. When you move on to criticism, make sure you understand
      where the perilous border between Radical Candor and Obnoxious Aggression is.

    $ sed -n "217p;231p;233p;245p" fuentes/scott_radical_candor/cap_05.md
      L217  Start by asking for criticism, not by giving it
      L231  Balance praise and criticism
      L233  Worry more about praise, less about criticism-but above all be sincere
      L245  Understand the perilous border between Obnoxious Aggression and Radical Candor

> ### **LA PRUEBA QUE SEPARA EL PASO 5 DE LOS PASOS 3 Y 6 ES TEXTUAL Y NO DE GUSTO, Y ES LA SUYA**
>
> **Los pasos 3 y 6 reproducen el ROTULO de la seccion que el libro abre a continuacion. El paso 5
> no.** *start with praise, not criticism* **no es** *Balance praise and criticism*, y menos todavia
> *Worry more about praise, less about criticism*: **uno dice por cual se EMPIEZA y el otro cuanto de
> cada uno.** Son dos instrucciones distintas.
>
> **Y LO QUE LO CIERRA SIN ARGUMENTO MIO: LOS NUEVE PASOS DEL HIJO.** `equilibrar_elogio_critica_equipo`
> manda *da mas elogio que critica*, *no apliques un ratio fijo*, *no uses el sandwich de opinion*, las
> dos formas de fallar y las dos preguntas de Karen Sipprell. **Ninguno de sus nueve pasos dice
> empieza por el elogio.** El hijo **no procedimenta lo que la madre nombra**, y `6.1` es explicita:
> *NOMBRAR NO ES PROCEDIMENTAR* corta hacia el hijo **solo cuando el hijo procedimenta eso mismo**.
>
> **Y EL OTRO CANDIDATO A HIJO QUE YO SI NOMBRE, `elogiar_trabajo_especifico_contexto`, ESTA PEOR
> COLOCADO TODAVIA:** sale de `L75` a `L83`, **cien lineas ANTES** de la que la madre recoge. La madre
> no remite hacia atras.

**Y HAY UN DETALLE QUE LE AGRADEZCO Y QUE HAY QUE ESCRIBIR: EL LEYO LOS DOS.** Su bitacora tiene el par
con `elogiar` en la linea `169` y el par con `equilibrar` en la `173`, **separados a proposito**, con
esta razon en el segundo: *lo separo a proposito del veredicto anterior, porque la tentacion era darle
el mismo trato*. **Mi apertura solo vio uno de los dos, y era el mas facil.**

| | |
|---|---|
| **que retiro** | **la arista `empezar_cultura --paso 5--> elogiar_trabajo_especifico_contexto`**, que mi apertura levanto como hueco |
| **por que es RETIRADA y no `CIFRA PUBLICADA PROPIA`** | mi apertura escribio, literal, *no la escribo yo en ninguna sede hoy ... la mido, la dejo aqui con su paso, y la subo al turno normal*. **Una lectura declarada provisional y retirada en el turno siguiente es el metodo funcionando**, y es la misma distincion que trace en `ACTA 24` `7.3`. **La trazo otra vez sobre una cifra mia y lo digo para que cualquiera pueda decir que me absolvi** |
| **que me llevo, que es lo que vale** | **mi fase ciega imprimio los pasos de la MADRE y no los del HIJO.** Una arista se decide con los dos lados impresos. **Va a mi remedio de `11`** |
