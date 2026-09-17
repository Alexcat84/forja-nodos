# APERTURA CIEGA DE LA VUELTA 35, linea `serial`, libro `scott_radical_candor`

Escrita ANTES de ver `docs/loop/REPORTE.md`, que el arnes retira a proposito (`D.34.2`).
Es la lectura que despues se compara con la del extractor. Mi acta de esta vuelta sera la
**`ACTA 34`**.

**MODO AUSTERO (`D.47`) VIGENTE:** lo que el registro ya dice no se repite. Lo que queda
intacto es **la cifra con su instrumento al lado**, y por eso toda cifra de aqui abajo
lleva su salida literal pegada.

---

## 0. LA DECLARACION QUE EL ARNES EXIGE (`D.40`)

```
ACTA ANTERIOR LEIDA: d2fa59ef5128507f86f8b1ce095665e9750176bf
HEREDADO 1: CUMPLIDO
HEREDADO 2: CUMPLIDO
HEREDADO 3: CUMPLIDO
HEREDADO 4: CUMPLIDO
HEREDADO 5: CUMPLIDO
```

**LA HUELLA NO ME LA CREO PORQUE EL PROMPT ME LA DE: LA COMPRUEBO.** La que el arnes me
entrega es la del **blob** del acta, y el acta que tengo delante en el arbol es esa misma:

```
$ git hash-object docs/loop/ACTA_AUDITOR.md
d2fa59ef5128507f86f8b1ce095665e9750176bf
$ git rev-parse HEAD:docs/loop/ACTA_AUDITOR.md
d2fa59ef5128507f86f8b1ce095665e9750176bf
```

Las dos coinciden con la heredada: **la `ACTA 33` que leo es la que el prompt nombra**, y
no otra version.

### 0.1. `HEREDADO 1: CUMPLIDO`. Es mi tarea bloqueante, y la unica que me toca a mi

El remedio dice: **toda cifra de recuento de un fichero de texto se comprueba con un
segundo instrumento de la casa que no sea el mio, y la salida de los dos va pegada.** Se
comprueba mirando que junto a cada recuento haya **dos** lineas que empiecen por `$`.

**LO CUMPLO POR CONSTRUCCION Y DE UNA VEZ PARA LOS CINCO FICHEROS QUE ESTE DOCUMENTO
CUENTA**, con `wc -l` y con `grep -c ""`, que son dos programas distintos:

```
$ wc -l docs/loop/ACTA_AUDITOR.md docs/loop/AUDITOR_FORJA.md fuentes/scott_radical_candor/cap_09.md dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl
  29594 docs/loop/ACTA_AUDITOR.md
    740 docs/loop/AUDITOR_FORJA.md
    433 fuentes/scott_radical_candor/cap_09.md
    302 dataset/nodos.jsonl
    427 bitacora/VEREDICTOS.jsonl
  31496 total
$ grep -c "" docs/loop/ACTA_AUDITOR.md docs/loop/AUDITOR_FORJA.md fuentes/scott_radical_candor/cap_09.md dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl
docs/loop/ACTA_AUDITOR.md:29594
docs/loop/AUDITOR_FORJA.md:740
fuentes/scott_radical_candor/cap_09.md:433
dataset/nodos.jsonl:302
bitacora/VEREDICTOS.jsonl:427
```

**LOS DOS DAN LO MISMO EN LOS CINCO**, asi que se publican. Y el que me costo el escalon,
`cap_09.md`, lleva **un tercero** y la comprobacion de su ultimo byte, porque un fichero
que no acaba en salto de linea es exactamente como se fabrica un `434` de un `433`:

```
$ python -c "print('lineas fuentes/scott_radical_candor/cap_09.md:', sum(1 for _ in open('fuentes/scott_radical_candor/cap_09.md',encoding='utf-8')))"
lineas fuentes/scott_radical_candor/cap_09.md: 433
$ tail -c 1 fuentes/scott_radical_candor/cap_09.md | xxd | tail -1
00000000: 0a                                       .
```

**`433` por tres programas distintos, y el fichero SI acaba en salto de linea.** La cifra
de mi apertura anterior decia `434`.

### 0.2. `HEREDADO 2: CUMPLIDO`. El `P13` corregido por `D.13` sin borrar

Lo pedia asi: *el `P13` de `practicar_franqueza_radical_jefe_propio` se corrige por `D.13`
sin borrar el texto viejo, y la errata del libro no se resuelve en ninguna de las dos
direcciones*. Se comprueba con **`forja.py corregir` corrido sobre ese nodo, la linea
`215` pegada y el gate en verde**. Las tres cosas estan:

```
$ git show --stat --format="%h %s" 3fc81ff
3fc81ff V.35 TAREA 1: el puente P13 que ya estaba en el grafo, retirado por declaracion sin elegir cual de las dos lecturas de L215 queria el libro, y la cifra de cap_09 republicada en 1 de 181

 .v35/L215_fragmento.txt   |  1 +
 .v35/correccion_p13.txt   | 11 ++++++
 bitacora/VEREDICTOS.jsonl |  1 +
 dataset/nodos.jsonl       |  2 +-
 docs/loop/REPORTE.md      | 86 +++++++++++++++++++++++++++++++++++++++++++++++
 5 files changed, 100 insertions(+), 1 deletion(-)
$ awk 'NR==215' fuentes/scott_radical_candor/cap_09.md | grep -o "If they react well.*better boss\."
If they react well and reward the candor, keep going. If they don’t, give up immediately or assume ill intent. Try again, carefully, but if you get the same reaction the next time, it may be time to move on. You deserve a better boss.
$ python forja.py gate
GATE VERDE.
  nodos verificados: 302
  guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece
```

**LA LINEA `215` LA PEGO DE SU INSTRUMENTO Y RECORTADA A PROPOSITO**, desde *If they react
well*: el principio de la linea trae un guion largo del libro y este documento vive bajo
el barrido de guiones de la casa. La parte que la adjudicacion necesitaba es la pegada.

El bloque de correccion que `src/correccion.py` escribio lo leo entero en la **seccion
`9`**, y de ahi sale un **`POR ADJUDICAR`**, no una caida.

### 0.3. `HEREDADO 3: CUMPLIDO` en lo que esta fase puede medir, y digo que mitad no veo

Lo pedia asi: *`PASOS INVENTADOS` de `cap_09` se vuelve a publicar con el numerador
corregido*. Se comprueba con **la fila de `cap_09` del reporte nuevo diciendo `1 de 181` y
citando la `ACTA 33`**.

**LA SEDE DE ESA COMPROBACION ES `docs/loop/REPORTE.md`, Y EL ARNES LO TIENE RETIRADO
AHORA MISMO. NO LO RECUPERO.** Lo que si sostengo con instrumento es que la vuelta toco el
reporte en el mismo commit en que corrigio el dato, y que **el numerador corregido esta
escrito dentro del propio `dataset/`**, que es sede duradera y no se reescribe cada vuelta:

```
$ ls docs/loop/REPORTE.md
ls: cannot access 'docs/loop/REPORTE.md': No such file or directory
$ git log 0d92254..be5baba --name-only --format="" | sort -u | grep "docs/loop/"
docs/loop/REPORTE.md
docs/loop/TABLERO.jsonl
```

Y la cifra corregida, leida del dataset y no del reporte (la cita literal completa esta en
la seccion `9`):

```
la cuenta buena es 17 pasos, 16 TRANSCRIPCION, 1 PUENTE, y el puente es P13
```

**LO CUENTO COMO CUMPLIDO PORQUE EL NUMERADOR CORREGIDO ESTA PUBLICADO EN LA MAS DURADERA
DE LAS DOS SEDES.** La fila del reporte la verifico en mi turno normal, en cuanto el arnes
me lo exponga: es el **`POR ADJUDICAR 1`** de la seccion `12`, y si esa fila no dice el
numerador corregido citando la `ACTA 33`, lo cargo entonces. **Lo escribo por adelantado
para que no pueda quedarse en el olvido.**

### 0.4. `HEREDADO 4: CUMPLIDO`, y lo cumplo ADEMAS por mi cuenta

Lo pedia asi: *antes de publicar un `0 PUENTE`, se relee el paso cuya linea de libro sea
internamente contradictoria o cuya polaridad el paso parta por la mitad, y se declara cual
se releyo*. Se comprueba con **el reporte nombrando los pasos releidos por ese motivo,
aunque sean cero**.

La sede vuelve a ser el reporte retirado. Pero este remedio **dejo rastro propio en el
arbol** y ademas **lo he corrido yo entero**:

```
$ git log 0d92254..be5baba --name-only --format="" | sort -u | grep "^.v35/"
.v35/aceptacion_apertura.txt
.v35/aceptacion_cierre.txt
.v35/apertura.py
.v35/apertura_tabla.txt
.v35/arista_cableada.txt
.v35/cerrojo.txt
.v35/cierre.py
.v35/cierre_tabla.txt
.v35/correccion_p13.txt
.v35/credito_apertura.txt
.v35/credito_cierre.txt
.v35/cuenta_cuarentena.txt
.v35/entrega_arnes.txt
.v35/fidelidad.py
.v35/fidelidad_tabla.txt
.v35/insercion_tabla.py
.v35/insercion_tabla.txt
.v35/L215_fragmento.txt
.v35/ojo_nuevo_citas.txt
.v35/polaridad.py
.v35/polaridad.txt
.v35/rancios_cierre.txt
.v35/tablero_apertura.txt
.v35/tablero_cierre.txt
.v35/tablero_siguiente.txt
```

Hay un `polaridad.py` y un `ojo_nuevo_citas.txt` commiteados en la vuelta, **y no los
abro**: son la lectura del extractor, y la seccion `1.3` dice por que en esta fase no la
leo. **Mi propio barrido de polaridad, con su metodo, su falso positivo cazado por mi y
los seis pasos releidos uno a uno con su linea de libro al lado, es la seccion `6`.** El
remedio pedia que los pasos releidos se nombren: **los nombro yo.**

### 0.5. `HEREDADO 5: CUMPLIDO`. El extractor no escribio en el registro de credito

Lo pedia asi: *el extractor NO escribe su tanda en `docs/loop/CREDITO_serial.jsonl`*, y se
comprueba con **`git log -1 --name-only` del cierre de la vuelta**. Esa comprobacion la
corro literal:

```
$ git log -1 --name-only --format="%h %s"
be5baba V.35 CIERRE: las tres tareas cerradas, cap_09 entero en el grafo con 15 de 15, el cierre de D.41 en verde y el rancio que fabrico mi propia correccion declarado en vez de callado

.v35/aceptacion_cierre.txt
.v35/cierre.py
.v35/cierre_tabla.txt
.v35/credito_cierre.txt
.v35/rancios_cierre.txt
.v35/tablero_cierre.txt
docs/loop/REPORTE.md
docs/loop/TABLERO.jsonl
$ git log -1 --name-only --format="" | grep -c "CREDITO"
0
$ git log 0d92254..be5baba --name-only --format="" | sort -u | grep -c "CREDITO"
0
```

**Ni el commit de cierre ni ninguno de los cinco commits de trabajo de la vuelta tocan
`docs/loop/CREDITO_*.jsonl`.** El remedio mordio: escribir esas lineas sigue siendo
trabajo mio al cerrar el acta, que es lo que `D.48` manda.

---

## 1. QUE TENGO DELANTE, QUE LEI, Y UNA COSA QUE DECLARO EN VEZ DE CALLARLA

### 1.1. Los ficheros que no estan, medidos y no supuestos

```
$ ls docs/loop/
ACTA_AUDITOR.md
AUDITOR.md
AUDITOR_FORJA.md
EJECUTOR.md
EXTRACTOR.md
ORDEN_DE_LOTES.md
paradas
PARALELO.md
PROMPT_SIGUIENTE.md
SELLOS_APERTURA.jsonl
TABLERO.jsonl
TESTIGO_GUARDAS.json
ultimo_apertura.json
$ git status --short docs/loop/
 M docs/loop/APERTURA_CIEGA.md
 D docs/loop/CREDITO_serial.jsonl
 D docs/loop/REPORTE.md
 D docs/loop/loop.log
 M docs/loop/ultimo_apertura.json
 D docs/loop/ultimo_auditor.json
 D docs/loop/ultimo_extractor.json
```

**ESA PRIMERA LINEA DICE `M` Y NO `D` PORQUE LA ESCRIBI YO**, en esta misma fase y unos
minutos antes de correr ese comando: el arnes me dejo `APERTURA_CIEGA.md` **borrado** del
arbol, igual que los otros, y lo que la `M` registra es este documento. **Lo digo porque
pegar la salida de antes debajo del comando de ahora seria fabricar la prueba**, que es
justo la especie que me tumbo la vuelta pasada.

**SON SEIS AUSENCIAS Y NO CUATRO, Y CADA UNA TIENE SU MOTIVO ESCRITO:** los cuatro de
`D.34.2` (`REPORTE.md`, `loop.log`, `ultimo_extractor.json`, `ultimo_auditor.json`),
`CREDITO_serial.jsonl` por `D.52`, y `APERTURA_CIEGA.md` porque es el fichero que estoy
escribiendo. **Ninguno lo recupero de git.** Git los sigue teniendo, y eso lo compruebo
por su nombre y sin abrir ni uno:

```
$ git ls-files docs/loop/ | grep -E "REPORTE|CREDITO|loop.log|ultimo_"
docs/loop/CREDITO_serial.jsonl
docs/loop/REPORTE.md
docs/loop/loop.log
docs/loop/ultimo_apertura.json
docs/loop/ultimo_auditor.json
docs/loop/ultimo_extractor.json
```

### 1.2. LO QUE SI LEI, Y UNA LECTURA QUE NADIE ME VA A CAZAR SI NO LA DIGO YO

Lei `docs/loop/AUDITOR_FORJA.md` entero (`740` lineas, medidas arriba con dos
instrumentos) y `docs/loop/ACTA_AUDITOR.md`, que es obra mia y no del extractor.

**Y AHORA LO QUE ME TOCA DECLARAR.** `docs/loop/ultimo_apertura.json` esta en el arbol con
**cero bytes**, y para saber por que corri esto:

```
$ wc -c docs/loop/ultimo_apertura.json
0 docs/loop/ultimo_apertura.json
$ git diff HEAD -- docs/loop/ultimo_apertura.json | head -4
diff --git a/docs/loop/ultimo_apertura.json b/docs/loop/ultimo_apertura.json
index 4145e70..e69de29 100644
--- a/docs/loop/ultimo_apertura.json
+++ b/docs/loop/ultimo_apertura.json
```

**ESE `git diff` ME DEVOLVIO EL MENSAJE FINAL DE MI PROPIA APERTURA ANTERIOR, Y LO LEI.**
Lo declaro, y digo las tres cosas que importan:

| | |
|---|---|
| **que es** | el volcado del mensaje final de **mi** turno ciego de la vuelta anterior. Es obra mia, de la misma especie que `ACTA_AUDITOR.md`, **y no es ninguno de los cuatro ficheros que `D.34.2` retira** |
| **que NO es** | no es el reporte, no es el `loop.log`, no es `ultimo_extractor.json`. **No contiene ni una linea escrita por el extractor de esta vuelta** |
| **por que lo digo** | porque el fichero estaba vaciado, porque el prompt me manda no recuperar y **la unica forma honesta de haber mirado es decir que mire**. Una salida pegada no prueba que un motivo sea cierto, pero **obliga a correr algo antes de escribirlo**, y esta es la misma letra de `D.40` aplicada contra mi |

**Y LO QUE ESA LECTURA ME DIO, QUE ES POCO Y CONVIENE QUE SE SEPA:** mis propias cifras de
la vuelta 34 y la confesion de mi propia caida. **No me dio ni una clase de esta tanda.**

### 1.3. LO QUE NO ABRI, Y ESO SI ES DISCIPLINA DE LA FASE

**Los `25` ficheros de `.v35/` estan en el arbol y no abri ni uno.** Son la lectura del
extractor: `fidelidad_tabla.txt`, `polaridad.txt`, `ojo_nuevo_citas.txt` e
`insercion_tabla.txt` contienen **exactamente** lo que vengo a leer a ciegas. Abrirlos no
lo prohibe `D.34.2`, que nombra cuatro ficheros, **pero convertiria esta apertura en una
copia**. Mis cuentas de las secciones `5`, `6`, `7` y `8` salen del libro y del dataset.

**Y DIGO LA CONTAMINACION QUE SI TUVE, PORQUE VINO EN EL PROMPT Y NO LA ELEGI:** el arnes
me entrega los asuntos de commit de la vuelta, y uno de ellos publica cifras de la lectura
del extractor:

```
$ git log 0d92254..be5baba --format="%h %s" | tac
ee2b6bf V.35 APERTURA DEL REPORTE: el esqueleto de la vuelta 35 con sus tres tareas vacias, abierto antes de la primera tarea
3fc81ff V.35 TAREA 1: el puente P13 que ya estaba en el grafo, retirado por declaracion sin elegir cual de las dos lecturas de L215 queria el libro, y la cifra de cap_09 republicada en 1 de 181
d9818a6 V.35 TAREA 2: la fidelidad del tramo de cap_09 ANTES de insertar, 0 PUENTE de 91, y el ojo nuevo barrido a maquina: 25 X or Y, 6 bajo negacion, 5 sanas y 1 marcada como discutible
eaaf78f V.35 TAREA 3: cap_09 cerrado en insercion con 5 de 5, 15 de 15 del capitulo, 297 a 302 nodos, tres veredictos leidos y la arista D.29 cableada en la misma vuelta
be5baba V.35 CIERRE: las tres tareas cerradas, cap_09 entero en el grafo con 15 de 15, el cierre de D.41 en verde y el rancio que fabrico mi propia correccion declarado en vez de callado
```

**ASI QUE SE, ANTES DE MEDIR, QUE EL DECLARA `0 PUENTE de 91`, `25 X or Y`, `6 bajo
negacion`, `5 sanas y 1 discutible`.** Lo que **no** se, y es lo que salva el valor de la
comparacion, es **cual** de las seis marco como discutible. `AUDITOR_FORJA.md 1.1` me deja
correr `git log`: es el primer paso de mi ciclo. **Lo que no puedo hacer es llamar ciega a
una lectura contaminada sin decir por donde entro la luz.**

### 1.4. HUECO DE ACTA: CERO

```
$ grep -c "^# ACTA " docs/loop/ACTA_AUDITOR.md
33
$ grep "^# ACTA " docs/loop/ACTA_AUDITOR.md | tail -1 | cut -c1-70
# ACTA 33. VUELTA 34, lote 4 (`scott_radical_candor`), **`cap_09` inse
```

**`33` encabezados y el ultimo es la `ACTA 33`, que cubre la `VUELTA 34`.** La vuelta que
audito es la **35**, la inmediatamente siguiente. **No hay ninguna vuelta sin acta, asi que
no audito mas de una.** El desfase entre el numero de acta y el de vuelta es registro
viejo (viene de la vuelta 29) y no lo repito.

---

## 2. LAS GUARDAS, RE CORRIDAS POR MI EN ESTA FASE

| guarda | salida | |
|---|---|---|
| `gate` | `GATE VERDE`, `302` nodos, `13` guardas | **VERDE** |
| `guiones` | cero largos y cero medios | **VERDE** |
| `resolutor` | `302` vivos, `0` deprecados, `0` alias | **VERDE** |
| `rancios` (`D.15`) | `49` hallazgos sobre `413` veredictos | **COLA DE TRABAJO, no rojo** |
| `tests/test_aceptacion.py` | `274` pruebas, **`4` fallos antes de escribir esto, `3` despues** | **los tres, de sede retirada** |
| `cerrar_reporte.py` (`D.41`, `D.42`) | **`1` ruta en rojo antes de escribir esto, `0` despues** | **la ruta era este fichero** |

```
$ python forja.py guiones
BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
$ python forja.py resolutor
nodos vivos: 302
nodos deprecados (archivo): 0
alias registrados: 0
$ python forja.py rancios | head -4
BLOQUE DE VIGENCIA: 49 hallazgo(s) sobre 413 veredicto(s) y 0 cita(s).
  RANCIO 41, SIN HUELLA 8
  lineas declaradas NO CONSUMADAS y por eso no medidas: 14
    (las escribio una corrida que no inserto nada; ver su razon en la propia linea)
$ python forja.py rancios | grep -c "^  \[RANCIO\]"
41
$ python forja.py rancios | grep -c "^  \[SIN HUELLA\]"
8
```

**`413` medidos mas `14` no consumadas son los `427` que cuenta la bitacora**, y eso cuadra
con la seccion `3`. `D.15` dice literalmente que esto **no** pone nada en rojo.

### 2.1. LOS FALLOS DE LA SUITE, MEDIDOS DOS VECES: ANTES Y DESPUES DE ESCRIBIR ESTO

**ANTES DE ESCRIBIR ESTE FICHERO, LA SUITE DABA CUATRO:**

```
  total: 274 pruebas, 4 fallos, 0 errores
FAIL: test_e_guion_largo_rompe_el_hook (__main__.PruebaE.test_e_guion_largo_rompe_el_hook)
FAIL: test_caso_positivo_un_frente_recien_nacido_hereda_cero (__main__.PruebaHerenciaPorLinea.test_caso_positivo_un_frente_recien_nacido_hereda_cero)
FAIL: test_el_aviso_nombra_la_linea_y_su_registro (__main__.PruebaHerenciaPorLinea.test_el_aviso_nombra_la_linea_y_su_registro)
FAIL: test_la_linea_serial_del_repo_tiene_su_registro_escrito (__main__.PruebaHerenciaPorLinea.test_la_linea_serial_del_repo_tiene_su_registro_escrito)
```

Y el cuarto, `PruebaE`, exige el repo limpio antes de ensuciarlo y por eso corre el hook
entero, donde caia el censo de rutas de `D.42` con **una sola ruta**:

```
CAE  docs\loop\ACTA_AUDITOR.md linea 29446, celda 3
     ruta : docs/loop/APERTURA_CIEGA.md
     NO esta en el arbol, y la celda no lleva la marca 'VACIA A PROPOSITO: <motivo>'. Una ruta publicada como sede de una cifra que no prueba nada es caida de cifra (cosecha 7.B)
     celda: `docs/loop/APERTURA_CIEGA.md`, apertura **sellada**

CENSO EN ROJO: 1 ruta(s) publicadas como sede de una cifra no sostienen nada.
```

**LA RUTA QUE CAIA ERA ESTE FICHERO, CITADO EN MI PROPIA `ACTA 33`, LINEA `29446`.** Y la
prediccion que se puede comprobar: **se cura en cuanto lo escriba.** Lo comprobe, y se
curo. Estas dos corridas son **posteriores** a guardar el documento:

```
$ python scripts/cerrar_reporte.py --hook | head -22
============================================================================
TALLADO DEL REPORTE (D.41): la tabla que dice ser de instrumento
============================================================================
tablas que declaran instrumento : 0
  talladas, celda a celda       : 0
  que DIFIEREN de su instrumento: 0
  con la ruta VACIA             : 0   (cero bytes, 7.B)
  sin poder comprobar           : 0
  que CITAN y no reproducen     : 0   (declaradas PARCIAL)

TALLADO VERDE: las 0 tabla(s) comprobables son las de su instrumento, celda a celda.
============================================================================
CENSO DE RUTAS (D.42): la unidad de la ruta es la celda
============================================================================
rutas publicadas y censadas : 134
  pasan                     : 134
  CAEN                      : 0
      PATRON                           10
      VACIA A PROPOSITO                3
      con contenido                    111
      vacia por protocolo              10
$ python tests/test_aceptacion.py | grep "^  total:"
  total: 274 pruebas, 3 fallos, 0 errores
$ python tests/test_aceptacion.py 2>&1 | grep "^FAIL:"
FAIL: test_caso_positivo_un_frente_recien_nacido_hereda_cero (__main__.PruebaHerenciaPorLinea.test_caso_positivo_un_frente_recien_nacido_hereda_cero)
FAIL: test_el_aviso_nombra_la_linea_y_su_registro (__main__.PruebaHerenciaPorLinea.test_el_aviso_nombra_la_linea_y_su_registro)
FAIL: test_la_linea_serial_del_repo_tiene_su_registro_escrito (__main__.PruebaHerenciaPorLinea.test_la_linea_serial_del_repo_tiene_su_registro_escrito)
```

**CENSO DE `133` A `134` RUTAS Y DE `1` CAIDA A `0`, Y LA SUITE DE `4` FALLOS A `3`.** La
ruta que faltaba era la de este documento, y la cuarta prueba colgaba de ella.

**LOS TRES QUE QUEDAN CUELGAN DE UN FICHERO QUE EL ARNES RETIRA EN ESTA FASE**, y la propia
prueba lo dice con su nombre por delante:

```
AssertionError: False is not true : docs/loop/CREDITO_serial.jsonl sin tandas: la migracion de D.48 no esta en el arbol
```

**NO CARGO NINGUNO DE LOS CUATRO A NADIE**, y digo por que con la regla en la mano: `7.B` de
la cosecha castiga *una ruta publicada como evidencia que apunta a un fichero
inexistente*, y esa ruta apuntaba a un fichero que **existe en git y que el protocolo
retira a proposito**. Lo que la medicion destapa no es una cifra falsa: es **una exencion
que le falta al censo**, que si tiene las diez del reporte (`vacia por protocolo: 10`) y no
tiene la de la apertura. Eso es maquinaria del arnes y no sustancia de auditoria (`D.33`),
asi que **va de propuesta al encargo y no de caida a ninguna racha.** La suite entera se
firma en mi turno normal.

---

## 3. EL DATO, MEDIDO CONTRA EL ARCHIVO Y CON MIS PROPIOS COMANDOS

```
$ python -c "
import json,collections
tot=0; nod=0; porlibro=collections.Counter(); pasos_libro=collections.Counter()
for l in open('dataset/nodos.jsonl',encoding='utf-8'):
    l=l.strip()
    if not l: continue
    d=json.loads(l); nod+=1
    np=len(d.get('pasos_accionables',[])); tot+=np
    for f in d.get('fuentes',[]):
        porlibro[f['clave']]+=1; pasos_libro[f['clave']]+=np
print('nodos:',nod,' pasos_accionables totales:',tot)
for k,v in porlibro.most_common(): print(' ',k,v,'nodos,',pasos_libro[k],'pasos')
"
nodos: 302  pasos_accionables totales: 2555
  zhuo_manager 136 nodos, 1107 pasos
  scott_radical_candor 99 nodos, 1046 pasos
  smart_who 59 nodos, 359 pasos
  onu_consumidor 6 nodos, 32 pasos
  manual_sistema_conocimiento 2 nodos, 11 pasos
```

| medida | hoy | como la mido |
|---|---|---|
| nodos en el grafo | **`302`** | `wc -l`, `grep -c`, `gate`, `resolutor` y el contador de objetos json: **cinco** de acuerdo |
| pasos accionables en el grafo | **`2555`** | el contador de arriba |
| veredictos en la bitacora | **`427`** | `wc -l` y `grep -c` de la seccion `0.1` |
| lo que la vuelta anadio | **`+5` nodos, `+4` veredictos** | el `numstat` de abajo |
| nodos desaparecidos | **`0`** | la comparacion de ids de abajo |

```
$ git diff --numstat 0d92254..be5baba -- bitacora/VEREDICTOS.jsonl dataset/nodos.jsonl
4	0	bitacora/VEREDICTOS.jsonl
6	1	dataset/nodos.jsonl
```

**`6` lineas anadidas y `1` quitada en el dataset son `5` nodos nuevos mas UN nodo
reescrito**, que es la correccion declarada del `P13`. Cuadra con `297` a `302`.

```
$ COPIA=<fuera del repo>/nodos_pre_v35.jsonl python -c "
import json,os
hoy={json.loads(l)['id'] for l in open('dataset/nodos.jsonl',encoding='utf-8') if l.strip()}
antes={json.loads(l)['id'] for l in open(os.environ['COPIA'],encoding='utf-8') if l.strip()}
print('ids hoy:',len(hoy),' ids de la copia pre insercion:',len(antes))
print('desaparecidos (antes y no hoy):', sorted(antes-hoy) or 'NINGUNO')
print('nuevos (hoy y no antes)       :', len(hoy-antes))
for i in sorted(hoy-antes): print('   ',i)
"
ids hoy: 302  ids de la copia pre insercion: 297
desaparecidos (antes y no hoy): NINGUNO
nuevos (hoy y no antes)       : 5
    conducir_reuniones_salto_nivel_diez_reglas
    entregar_evaluacion_formal_desempenio_nueve_consejos
    fomentar_guia_reciproca_companieros
    impedir_punialadas_espalda_equipo
    resolver_dudas_frecuentes_reuniones_salto_nivel
```

`COPIA` es el dataset de hoy menos esos cinco ids, escrito por mi **fuera del repo**, y es
la misma copia contra la que corro el barrido de vecinos de la seccion `7`. **Cero nodos
desaparecidos: el cerrojo y `D.44` no tienen nada que decir en esta vuelta.**

---

## 4. EL MATERIAL: `cap_09` DE `scott_radical_candor`

`433` lineas, medidas con tres instrumentos en la seccion `0.1`. Lo que el capitulo tiene
dentro, contado por mi contra el dataset y contra la bandeja:

```
$ python -c "
import json,glob
nuevos={'conducir_reuniones_salto_nivel_diez_reglas','entregar_evaluacion_formal_desempenio_nueve_consejos','fomentar_guia_reciproca_companieros','impedir_punialadas_espalda_equipo','resolver_dudas_frecuentes_reuniones_salto_nivel'}
n_v=p_v=0; n_a=p_a=0
for l in open('dataset/nodos.jsonl',encoding='utf-8'):
    d=json.loads(l)
    if 'scott_radical_candor/cap_09.md' not in d.get('resumen_teorico',''): continue
    np=len(d['pasos_accionables'])
    if d['id'] in nuevos: n_v+=1; p_v+=np
    else: n_a+=1; p_a+=np
print('cap_09 ANTES de la vuelta 35 : %d nodos, %d pasos' % (n_a,p_a))
print('cap_09 EN la vuelta 35       : %d nodos, %d pasos' % (n_v,p_v))
print('cap_09 HOY en el grafo       : %d nodos, %d pasos' % (n_a+n_v,p_a+p_v))
print('cap_09 en bandeja            : %d nodos' % sum(1 for x in glob.glob('cuarentena/scott_radical_candor/*.json') if 'cap_09.md' in open(x,encoding='utf-8').read()))
"
cap_09 ANTES de la vuelta 35 : 15 nodos, 181 pasos
cap_09 EN la vuelta 35       : 5 nodos, 91 pasos
cap_09 HOY en el grafo       : 20 nodos, 272 pasos
cap_09 en bandeja            : 0 nodos
```

**LECTURA, y la marco porque es una conclusion sobre contenido y no lo que el instrumento
midio (`D.38.3` ensanchada):** `cap_09` esta **cerrado en insercion**. Las `20` piezas del
capitulo que tenian nodo propio viven las `20` en el grafo, y en la bandeja de
`scott_radical_candor` **no queda ni una** de este capitulo. El `181` de la `ACTA 33` es
exactamente el denominador de las `15` de entonces, y `181` mas `91` son los `272` de hoy.

### 4.1. UNA CIFRA DE LA VUELTA QUE NO ME CUADRA, Y LA DEJO PLANTEADA SIN ADJUDICARLA

Los asuntos de commit de la vuelta dicen **`15 de 15 del capitulo`** y **`cap_09 entero en
el grafo con 15 de 15`**. **Mi medicion dice `20` de `20`.** Lo unico que mide `15` en este
capitulo es **el tramo de la vuelta 34**, y el asunto de la vuelta 34 lo decia asi:

```
$ git log --format="%h %s" | grep -E "^3dbc901|^1a356dd"
3dbc901 V.34 CIERRE: cap_09 entra 15 de 15 del tramo, las tres tareas cerradas, y una PARADA en el cierre de D.41 que no es de mi sede
1a356dd V.34 TAREA 2 (3 de 3): cierra el tramo de cap_09 con 15 de 15 insertados, 282 a 297 nodos
```

**LA VUELTA 34 ESCRIBIO `15 de 15 DEL TRAMO`. LA VUELTA 35 ESCRIBE `15 de 15 DEL
CAPITULO`.** Son dos poblaciones distintas con la misma cifra.

**NO LO CARGO Y NO LO ADJUDICO AQUI, POR DOS RAZONES ESCRITAS:** `5.6` dice que **el asunto
de un commit NO es sede de cifra**, asi que por si solo no es caida de nada; y la sede que
si lo seria, `docs/loop/REPORTE.md`, esta retirada. **Es el `POR ADJUDICAR 2`**, y es el
primero que mirare cuando el arnes me exponga el reporte, porque `REPORTE` viene en `2 de
3` y una cifra mal escalada en TABLA, CABECERA o CONCLUSION seria el tercer escalon.

### 4.2. Lo que queda en la bandeja del libro, por capitulo

```
$ python -c "
import json,glob,re,collections
cap=collections.Counter()
for p in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
    rt=json.load(open(p,encoding='utf-8')).get('resumen_teorico','')
    m=re.search(r'scott_radical_candor/(cap_\d+)\.md', rt)
    cap[m.group(1) if m else 'SIN_UNIDAD']+=1
for k,v in sorted(cap.items()): print(' ',k,v)
print(' total ficheros:', sum(cap.values()))
"
  cap_10 14
  cap_12 2
  cap_13 12
  cap_14 15
 total ficheros: 43
$ ls cuarentena/scott_radical_candor/*.json | wc -l
43
$ ls cuarentena/_insertados/scott_radical_candor/*.json | wc -l
99
```

`99` archivados mas `43` en bandeja son los `142` candidatos escritos del libro, y los `99`
del archivo son exactamente los `99` nodos de `scott_radical_candor` que cuenta el dataset
en la seccion `3`. **Los dos numeros salen de sitios distintos y coinciden.**

---

## 5. MI RELECTURA DE FIDELIDAD `D.30`: LOS `91` PASOS DEL TRAMO, UNO A UNO

**QUE HICE, CON PALABRAS DEL INSTRUMENTO Y NO DE LA CONCLUSION:** abri
`fuentes/scott_radical_candor/cap_09.md` por las lineas `331` a `425`, imprimi los `91`
pasos de los cinco nodos que la vuelta inserto, y **compare cada paso con la linea del
libro de la que su propio nodo dice que sale**. La asignacion paso a linea la saco del
`resumen_teorico` de cada nodo, que es dataset y no reporte:

```
$ python <mi lector del mapa, sobre dataset/nodos.jsonl>
entregar_evaluacion_formal_desempenio_nueve_consejos   pasos=22
   22 pasos, 22 TRANSCRIPCION, 0 PUENTE. P1 de la linea 335; P2 de la 337; P3 de la 341; P4, P5 y P6 de la 343; P7 de la 345; P8 de la 347; P9 de la 349; P10 de la 351; P11, P12, P13 y P14 de la 353; P15 y P16 de la 355; P17, P18 y P19 de la 357; P20 de la 359; P21 y P22 de la 361.

impedir_punialadas_espalda_equipo   pasos=9
   9 pasos, 9 TRANSCRIPCION, 0 PUENTE. Los nueve salen de la linea 367.

fomentar_guia_reciproca_companieros   pasos=13
   13 pasos, 13 TRANSCRIPCION, 0 PUENTE. P1, P2 y P3 salen de la linea 371; P4 a P10 de la 373; P11 de las lineas 375 y 377; P12 y P13 de la 381.

conducir_reuniones_salto_nivel_diez_reglas   pasos=31
   31 pasos, 31 TRANSCRIPCION, 0 PUENTE. P1 de la linea 385; P2 de la 389; P3, P4 y P5 de la 391; P6 de la 393; P7 de la 395; P8, P9 y P10 de la 397; P11 y P12 de la 399; P13 de la 401; P14, P15 y P16 de la 403; P17, P18, P19 y P20 de la 405; P21 y P22 de la 407; P23 y P24 de la 409; P25, P26, P27, P28 y P29 de la 411; P30 y P31 de la 413.

resolver_dudas_frecuentes_reuniones_salto_nivel   pasos=16
   16 pasos, 16 TRANSCRIPCION, 0 PUENTE. P1 y P2 de la linea 419; P3, P4, P5 y P6 de la 421; P7, P8, P9 y P10 de la 423; P11, P12, P13, P14, P15 y P16 de la 425.
```

**LO PRIMERO QUE COMPROBE FUE EL MAPA MISMO, PORQUE UN MAPA MAL ASIGNADO HACE FIEL A
CUALQUIER COSA.** Los rotulos que ese mapa nombra estan donde dice: `331` es `FORMAL
PERFORMANCE REVIEWS`, `363` es `PREVENT BACKSTABBING`, `369` es `PEER GUIDANCE`, `383` es
el rotulo de las reuniones de salto de nivel y `415` es el de sus dudas frecuentes. Las
cinco piezas empiezan en su rotulo y ninguna se mete en el tramo de la siguiente.

### 5.1. MI VEREDICTO, PIEZA POR PIEZA

| pieza | nodo | pasos | mi lectura |
|---|---|---:|---|
| `P24` | `entregar_evaluacion_formal_desempenio_nueve_consejos` | `22` | **`22` TRANSCRIPCION, `0` PUENTE** |
| `P25` | `impedir_punialadas_espalda_equipo` | `9` | **`9` TRANSCRIPCION, `0` PUENTE** |
| `P26` | `fomentar_guia_reciproca_companieros` | `13` | **`13` TRANSCRIPCION, `0` PUENTE** |
| `P27` | `conducir_reuniones_salto_nivel_diez_reglas` | `31` | **`31` TRANSCRIPCION, `0` PUENTE** |
| `P28` | `resolver_dudas_frecuentes_reuniones_salto_nivel` | `16` | **`16` TRANSCRIPCION, `0` PUENTE** |
| | **el tramo** | **`91`** | **`91` TRANSCRIPCION, `0` PUENTE** |

**MI CUENTA Y LA DE LA VUELTA COINCIDEN EN LAS CINCO PIEZAS Y EN EL TOTAL.** Y lo digo
sabiendo lo que me ensenio la `ACTA 33`: **ese mismo `0` fue `1` la vuelta pasada**, asi que
esta vez no lo firmo por parecido, sino con los sitios donde el paso pudo irse del libro y
no se fue, que son los de `5.2` y `5.3`.

### 5.2. LOS SEIS PASOS DONDE LA TRADUCCION TOMO UNA DECISION, Y POR QUE LOS SOSTENGO

**ESTOS SON LOS QUE UN RELECTOR TIENE QUE VOLVER A MIRAR**, y los pongo yo porque el resto
es copia literal y no necesita defensa:

| paso | lo que el paso hace | linea | mi lectura |
|---|---|---|---|
| `P26` `P11` | convierte en acto (*comprueba antes si esa practica encaja donde estas*) lo que el libro dice como limite (*that approach will not work everywhere*) | `375` y `377` | **TRANSCRIPCION.** El limite es del libro en sus dos mitades, Apple y aviacion. El imperativo es la forma del limite y no un anadido: **una mecanica copiada sin su limite queda mas ancha que el libro** |
| `P24` `P10` | *dale el escrito a la persona* donde el libro dice *a written review offers people a useful way of clarifying points* | `351` | **TRANSCRIPCION.** El acto es el que la frase supone, y el motivo va pegado tal cual |
| `P24` `P16` | *diez minutos de descanso no bastan* donde el libro dice *I always needed more than a ten-minute break* | `355` | **TRANSCRIPCION.** Es la misma afirmacion dicha por el otro lado, y la cifra de los diez minutos es del libro |
| `P27` `P3` | parte en dos ramas la clausula *you are not automatically presuming that the boss is guilty, or that you are unwilling to hear any criticism* | `391` | **TRANSCRIPCION, y es la que mas mire.** Seccion `6.2` |
| `P28` `P1` | *ponte a excavar en los problemas* donde el libro lo cuenta en pasado (*I started digging into the problems*) | `419` | **TRANSCRIPCION.** Lo que entra es el acto. La cifra del caso (*only happened to me three times*) **no** esta en el paso, y lo comprobe: no aparece |
| `P28` `P16` | dice *el mundo de diferencia* y **no** dice cuantas maneras son | `425` | **TRANSCRIPCION, con una correccion del extractor dentro del acto.** El libro dice *a world of difference between saying X and saying Y* sin dar cuenta, y el paso no la da. **Una cuenta que el libro no escribe habria sido puente, y no esta** |

### 5.3. LO QUE EL TRAMO DEJO FUERA, Y LO COMPROBE UNO A UNO

**EL PUENTE SE MIDE TAMBIEN POR LO QUE NO SE ESCRIBIO.** Estas cuatro son las piezas del
tramo que mas invitaban a inventar:

| lo que el libro trae | donde | esta en algun paso |
|---|---|---|
| el Sistema de Notificacion de Seguridad de la Aviacion, con la FAA y la NASA | `377` | **NO.** De esa linea solo entra el limite de la aviacion. Correcto: es el ejemplar, no el acto |
| el sistema medico imaginado, en condicional (*What if...*) | `379` | **NO.** Una hipotesis no es un acto. Habria sido el puente mas grande del tramo |
| la organizacion plana como mito y la jerarquia como hecho inescapable | `387` | **NO.** Es la razon de la seccion y no un acto. Escribirla como paso habria convertido una postura en procedimiento |
| que hacer si la conversacion a tres tampoco resuelve el conflicto | `367` | **NO**, y el libro tampoco lo dice: cierra con *Hopefully, they will work it out*. **El bucle queda abierto, que es lo que `D.30` manda** |

### 5.4. `PASOS INVENTADOS POR CAPITULO` (seccion `8`), CON MI DENOMINADOR

| capitulo | pasos escritos | puentes | por ciento | de donde sale |
|---|---:|---:|---:|---|
| `cap_09` **hasta la vuelta 34** | `181` | `1` | **`0,55`** | el `P13` que la `ACTA 33` adjudico |
| `cap_09` **el tramo de la vuelta 35** | `91` | `0` | **`0,00`** | mi relectura de `5.1` |
| `cap_09` **entero, hoy** | `272` | `1` | **`0,37`** | la suma de los dos, medida en la seccion `4` |

**MUY POR DEBAJO DEL TOPE DEL `10` POR CIENTO DE `8.1`**, asi que por esta metrica el
volumen del lote siguiente no baja ningun escalon. **Y digo lo que esta cifra NO es**
(`8.4`): no entra en la metrica de credito, y el `1` del numerador es un puente
**encontrado y corregido**, que es la regla funcionando.

---

## 6. EL BARRIDO DE POLARIDAD: EL REMEDIO QUE YO ESCRIBI, CORRIDO POR MI

El remedio heredado `4` pide releer **el paso cuya linea de libro sea internamente
contradictoria o cuya polaridad el paso parta por la mitad**, y declarar cual se releyo. La
figura tiene nombre y fecha: **`L215`**, donde *give up immediately or assume ill intent*
comparte polaridad en las dos lecturas posibles y el `P13` escribio una mitad en positivo y
la otra en negativo.

### 6.1. EL METODO, Y UN FALSO POSITIVO MIO CAZADO ANTES DE PUBLICAR

Corri un barrido de `or` frase a frase sobre las lineas `331` a `425`, marcando las que
llevan negacion a su izquierda dentro de la misma frase. **La primera version del barrido
daba cero, y era mentira:** el libro escribe el apostrofo tipografico y mi patron buscaba
el de teclado, asi que `aren`+`t`, `don`+`t` y `hadn`+`t` no entraban. **Lo cace con un
control: le pase la linea `215`, que SE que tiene la figura, y me dio cero.** Con el
apostrofo corregido, la `215` aparece y el tramo tambien:

```
$ python <mi barrido de polaridad, con L215 de control>
== CONTROL, el paso que tumbo la vuelta 34 (L215 a L215) ==
   L215  no, or
   L215  n’t, give up immediately or
   coincidencias: 2

== EL TRAMO DE ESTA VUELTA, las cinco piezas (L331 a L425) ==
   L367  not over email or
   L377  n’t been careless or
   L385  without your direct reports in the room, and ask what they could do or
   L391  n’t automatically presuming that the boss, your direct report, is guilty, or
   L411  no changes were made, or
   L425  not to judge or
   L425  n’t defend or
   coincidencias: 7

== EL CAPITULO ENTERO (L1 a L433) ==
   coincidencias: 35
```

Y la poblacion de la que salen, que es la cifra que hace legible al `7`:

```
$ python <mi barrido de disyunciones, L331 a L425>
disyunciones 'or' en L331-425        : 25
  de ellas, con negacion a su izquierda en la misma frase: 7
```

**`25` DISYUNCIONES EN EL TRAMO, `7` MARCADAS A MAQUINA. Y DE ESAS `7`, UNA ES UN FALSO
POSITIVO MIO:** en `L385` la marca es un `without` que vive en otra clausula (*without your
direct reports in the room*) y **no alcanza a la disyuncion** (*what they could do or stop
doing*). **Releidas una a una, la poblacion de verdad es `6`**, y lo digo asi en vez de
publicar el `7` de la maquina: el instrumento dice donde mirar, y ahi acaba su trabajo
(`D.19`).

### 6.2. LAS SEIS, RELEIDAS Y NOMBRADAS, QUE ES LO QUE EL REMEDIO PIDE

| linea | la clausula del libro | donde cae | mi lectura |
|---|---|---|---|
| `367` | *This must be a live conversation (i.e., not over email or text)* | `P25` `P5` | **SANA.** *no por correo ni por mensaje*: la negacion alcanza a las dos mitades |
| `377` | *As long as the pilots had not been careless or reckless, they were granted immunity* | **ningun paso** | **SANA POR AUSENCIA.** De esa linea solo entra el limite de la aviacion. La clausula de la inmunidad **no** esta en ningun paso, y lo comprobe |
| `391` | *you are not automatically presuming that the boss, your direct report, is guilty, or that you are unwilling to hear any criticism* | `P27` `P3` | **SANA, Y ES LA GEMELA EXACTA DE `L215`.** Ver abajo |
| `411` | *If people feel that no changes were made, or that the meeting did not make a difference* | `P27` `P29` | **SANA.** *no se hizo ningun cambio, o que la reunion no sirvio de nada*: cada mitad conserva su negacion |
| `425` | *Make it clear that your role is not to judge but to pass along the feedback* | `P28` `P13` | **SANA.** *tu papel no es juzgar sino transmitir lo que te digan* |
| `425` | *Do not defend or malign the boss you are hearing about* | `P28` `P15` | **SANA.** *No defiendas ni denigres al jefe*: negacion sobre las dos mitades |

**`6` DE `6` SANAS EN MI LECTURA.**

**Y LA `391` MERECE SU PARRAFO, PORQUE ES LA MISMA TRAMPA QUE LA `215` Y ESTA VEZ NO CAYO.**
El libro pone una negacion que alcanza a dos clausulas unidas por `or`, asi que las dos
tienen que salir negadas. El paso escribe: *tiene que quedar claro que **no** das por
supuesto que el jefe sea culpable, **ni que no** estes dispuesto a oir ninguna critica
suya*. **Las dos mitades salen negadas, que es lo que la linea sostiene.** Es de lectura
pesada, tres negaciones en una frase, y si algo de este tramo se marcase como discutible
apostaria por esta; **pero la polaridad esta bien puesta, y eso es lo que `D.30` mide.**

### 6.3. LA OTRA MITAD DEL REMEDIO: LINEAS INTERNAMENTE CONTRADICTORIAS

`L215` no era solo una disyuncion bajo negacion: **se contradecia con su propia frase
siguiente** (*give up immediately* seguido de *Try again, carefully*). Busque esa figura en
el tramo leyendo las seis clausulas de arriba y sus frases vecinas. **No encontre ninguna
linea del tramo `331` a `425` que se contradiga consigo misma**, y digo el limite de esa
busqueda: **es una lectura mia y no hay instrumento de la casa que la mida**, asi que vale
lo que valga mi lectura de esas noventa y cinco lineas. **Lo declaro como lectura y no como
cifra.**

---

## 7. EL BARRIDO DE VECINOS `D.38.4`: GRAFO MAS BANDEJAS, CON EL INSTRUMENTO DE LA CASA

**COMO LO CORRO, PORQUE EL METODO ES LA MITAD DE LA CIFRA.** Los cinco candidatos ya viven
en el grafo, y `D.31` hace que el informe los salte por estar archivados en `_insertados`.
Asi que reconstrui **fuera del repo** el estado exacto que la aduana tuvo delante: el
dataset de hoy menos esos cinco ids (`297`), y la bandeja con los cinco devueltos a ella
(`48` de `scott_radical_candor` mas `3` de `marquet_turn_the_ship`). **No toque ni un
fichero del repo: el informe es de solo lectura y las copias viven fuera.**

```
$ FORJA_DATASET=<copia 297> FORJA_CUARENTENA=<copia bandejas> python forja.py informe <los 5 candidatos>
============================================================================
INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
============================================================================
candidatos revisados        : 5
poblacion del barrido       : 348   (297 del grafo mas 51 que esperan en bandejas)
umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

EL SALDO
  ENTRARIAN sin leer nada          : 3
  BLOQUEARIAN esperando veredicto  : 2   (no es rechazo: es cola de lectura)
  CAERIAN por una guarda           : 0
  CHOCAN entre si dentro del lote  : 0

LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
  vecinos levantados en total      : 3
  por candidato bloqueado          : menor 1, mediana 2, mayor 2
  que señal levanta cada vecindad  : familia_id 3

============================================================================
LA LISTA COMPLETA, candidato por candidato
============================================================================

[ENTRARIA] impedir_punialadas_espalda_equipo   (impedir_punialadas_espalda_equipo.json)

[ENTRARIA] fomentar_guia_reciproca_companieros   (fomentar_guia_reciproca_companieros.json)

[ENTRARIA] entregar_evaluacion_formal_desempenio_nueve_consejos   (entregar_evaluacion_formal_desempenio_nueve_consejos.json)

[BLOQUEARIA] conducir_reuniones_salto_nivel_diez_reglas   (conducir_reuniones_salto_nivel_diez_reglas.json)
    vecino resolver_dudas_frecuentes_reuniones_salto_nivel  [levantada por: familia_id]
      similitud_texto 0.207 | familia_id 0.333 | paso_contra_nodo 0.471
      paso 19 del candidato contra paso 12 de resolver_dudas_frecuentes_reuniones_salto_nivel

[BLOQUEARIA] resolver_dudas_frecuentes_reuniones_salto_nivel   (resolver_dudas_frecuentes_reuniones_salto_nivel.json)
    vecino conducir_reuniones_salto_nivel_diez_reglas  [levantada por: familia_id]
      similitud_texto 0.221 | familia_id 0.333 | paso_contra_nodo 0.479
      paso 12 del candidato contra paso 19 de conducir_reuniones_salto_nivel_diez_reglas
    vecino resolver_dudas_frecuentes_pedir_critica  [levantada por: familia_id]
      similitud_texto 0.229 | familia_id 0.375 | paso_contra_nodo 0.457
      paso 15 del candidato contra paso 13 de resolver_dudas_frecuentes_pedir_critica

NADA SE INSERTO. Este informe es de SOLO LECTURA: para que un nodo
entre hace falta python forja.py insertar, uno por vez, con su
veredicto escrito por vecino.
```

| lo que mide | cifra |
|---|---:|
| poblacion del barrido | **`348`** (`297` del grafo mas `51` de bandejas) |
| candidatos que entrarian sin leer nada | **`3`** |
| candidatos que abren cola de lectura | **`2`** |
| vecindades levantadas | **`3`** |
| candidatos que caerian por una guarda | **`0`** |

**LECTURA, marcada porque es conclusion y no medida:** la poblacion de la aduana y la mia
**son ya la misma** (`D.38.5`), y por eso el cruce de esta cifra contra la bitacora es una
comparacion de verdad y no de metodo. **Los `3` vecinos levantados son exactamente los `3`
veredictos de lectura que la vuelta escribio**, ni uno mas ni uno menos, y las tres
vecindades las levanta **la misma senial**, `familia_id`. **Ninguna la levanta la
similitud de texto**: las tres estan en `0,20` a `0,23`, muy por debajo del umbral `0,35`.

**Y UNO DE LOS TRES VECINOS VIVE EN LA BANDEJA Y NO EN EL GRAFO:**
`resolver_dudas_frecuentes_pedir_critica` es un candidato de `cap_13` que sigue esperando
juicio. **Es justo el caso que `D.38.4` y `D.38.5` vinieron a arreglar**, y hoy lo levanta
la maquina sola.

---

## 8. MIS ADJUDICACIONES CIEGAS DE LA TANDA

La vuelta escribio **cuatro** lineas de bitacora, y solo **tres** son lecturas de clase:

```
$ git diff 0d92254..be5baba -- bitacora/VEREDICTOS.jsonl | grep "^+" | grep -v "^+++" | <mi lector, sin el campo razon>
CORREGIDO practicar_franqueza_radical_jefe_propio    practicar_franqueza_radical_jefe_propio    arista=None
CONTINUA  conducir_reuniones_salto_nivel_diez_reglas resolver_dudas_frecuentes_reuniones_salto_nivel  arista=conducir_reuniones_salto_nivel_diez_reglas > resolver_dudas_frecuentes_reuniones_salto_nivel
CONTINUA  resolver_dudas_frecuentes_reuniones_salto_nivel conducir_reuniones_salto_nivel_diez_reglas  arista=conducir_reuniones_salto_nivel_diez_reglas > resolver_dudas_frecuentes_reuniones_salto_nivel
SANO      resolver_dudas_frecuentes_reuniones_salto_nivel resolver_dudas_frecuentes_pedir_critica     arista=
```

### 8.1. HASTA DONDE LLEGA MI CEGUERA, Y LO DIGO ANTES DE DAR LAS CLASES

**LA CLASE ESCRITA LA VI ANTES DE ADJUDICAR, Y NO PODIA NO VERLA:** `bitacora/VEREDICTOS.jsonl`
es fuente de verdad numero `3` de mi protocolo, y el barrido de la seccion `7` salia de
ahi. **Lo que NO he abierto es el campo `razon` de ninguna de las cuatro lineas.** Solo
comprobe que existe, que es lo que `D.8` manda mirar:

```
$ python -c "<lector que imprime solo si el campo razon esta y cuanto mide>"
L424 CORREGIDO: razon presente=True, longitud=857, levantada_por=['correccion declarada']
L425 CONTINUA: razon presente=True, longitud=1968, levantada_por=['familia_id']
L426 CONTINUA: razon presente=True, longitud=1342, levantada_por=['familia_id']
L427 SANO: razon presente=True, longitud=1607, levantada_por=['familia_id']
```

**LAS CUATRO TIENEN RAZON ESCRITA. `0` SANO sin razon, que es caida de `D.8` aunque
acierte.** Y por eso adjudico **diciendo de que depende cada clase**, para que se pueda
comprobar que no estoy firmando lo que ya estaba escrito.

### 8.2. EL PAR `P27` CONTRA `P28`, EN LAS DOS DIRECCIONES

**Lei los `31` pasos de la madre y los `16` de la hija antes de decidir**, que es lo que
`1.2` manda.

| | |
|---|---|
| **la pregunta de la vara** | la hija **CONTINUA** el trabajo de la madre o lo **REPITE** |
| **que hace la madre** | `P27` conduce la reunion: consentimiento previo, explicacion al equipo, notas proyectadas, arranque, priorizacion, reparto de notas, cambios y seguimiento, y la cadencia anual |
| **que anade la hija** | `P28` responde a **cuatro averias** que la madre no toca: el equipo entero que ha perdido la fe, la sala que no habla, la persona que no se calla, y el equilibrio entre apoyar al jefe y oir al equipo |
| **lo que queda fuera del solape** | **procedimiento en los dos lados**, que es lo que `6.1` pide mirar: la hija trae leer caras, ofrecer asuntos oidos de antemano, dar la vuelta a la sala, prometer mirar a fondo sin juzgar en el acto. La madre trae el consentimiento y la mecanica de las notas |
| **la bascula NO decide** | fui a mirar **que dos pasos cruza la maquina**, y son los dos que nombran la *sesion de quejas*: el `19` de la madre (*intenta que la gente piense en soluciones, para que no degenere en una sesion de quejas*) contra el `12` de la hija (*si parece que estas pescando razones para castigar a ese jefe: o la gente se cierra en banda, o se desata una sesion de quejas*). **Es la misma averia vista desde dos sitios: la madre la previene conduciendo, la hija la diagnostica cuando ya paso.** Y aun asi el solape no manda: lo que decide es que fuera de el hay procedimiento propio en las dos |

**MI CLASE: `CONTINUA`, con la madre `conducir_reuniones_salto_nivel_diez_reglas` y la hija
`resolver_dudas_frecuentes_reuniones_salto_nivel`.** La direccion la sostiene el libro:
`L417` presenta las dudas como *questions people have asked me most often* **sobre** las
reuniones que `L383` a `L413` acaban de explicar. **Una FAQ no existe sin su procedimiento.**

**Y LA ARISTA: SI, EN ESA DIRECCION.** `6.1` avisa de que *la arista no exculpa*, asi que la
declaro por lo que los pasos hacen y no por el cable. Esta puesta en los dos extremos:

```
$ python -c "<lector de nodos_previos y nodos_siguientes de los dos extremos>"
conducir_reuniones_salto_nivel_diez_reglas         previos=[]  siguientes=['resolver_dudas_frecuentes_reuniones_salto_nivel']
resolver_dudas_frecuentes_reuniones_salto_nivel    previos=['conducir_reuniones_salto_nivel_diez_reglas']  siguientes=[]
```

### 8.3. `P28` CONTRA `resolver_dudas_frecuentes_pedir_critica`, QUE ESPERA EN LA BANDEJA

| | |
|---|---|
| **que son** | dos colecciones de dudas frecuentes: una sobre **reuniones de salto de nivel** (`cap_09`), otra sobre **pedir critica sobre uno mismo** (`cap_13`) |
| **por que la maquina los cruza** | `familia_id` `0,375`: comparten el arranque `resolver_dudas_frecuentes_`. **Es la senial diciendo donde mirar, y ahi acaba su trabajo** (`D.19`) |
| **que hace cada uno** | el de `cap_09` responde que hacer **cuando conduces** una reunion ajena: leer caras, no juzgar, transmitir sin atribuir. El de `cap_13` responde que hacer **cuando la critica es sobre ti**: variar la pregunta recurrente, reconocer lo que no sabes arreglar, el *todavia no* de Dweck |
| **ni madre ni hija** | ninguno continua el trabajo del otro: **son dos hermanos de capitulos distintos**, y ninguno es condicion ni despliegue del otro |
| **tampoco gemelos** | el solape es el rotulo, no el procedimiento. **Fusionarlos perderia las dos mecanicas** |

**MI CLASE: `SANO`, sin arista.** Y digo lo que me haria cambiar de idea, que es lo que
deja comprobar una adjudicacion: si alguno de los dos tuviera un paso que remitiera al
otro, seria `D.29` por lectura. **Los lei y no lo tienen.**

### 8.4. EL RESUMEN DE MIS TRES

| # | par | mi clase |
|---:|---|---|
| `1` | `conducir_reuniones` contra `resolver_dudas_frecuentes_reuniones` | **`CONTINUA`**, arista madre a hija |
| `2` | `resolver_dudas_frecuentes_reuniones` contra `conducir_reuniones` | **`CONTINUA`**, la misma arista por el otro extremo |
| `3` | `resolver_dudas_frecuentes_reuniones` contra `resolver_dudas_frecuentes_pedir_critica` | **`SANO`** |

**LAS TRES COINCIDEN CON LA CLASE ESCRITA EN LA BITACORA.** La comparacion que de verdad
mide algo, la de **mi razon contra la suya**, la hago en mi turno normal, cuando destape
los cuatro campos `razon`. **Aqui dejo escrito de que depende cada una de las mias para que
esa comparacion no la pueda ganar yo a posteriori.**

### 8.5. LA MUESTRA PINEADA DE LOS SANO (seccion `7` del protocolo)

**LA TANDA TIENE UN SOLO `SANO`.** El protocolo dice: *mientras la forja tenga menos de
tres `SANO` por tanda, esta seccion se cumple releyendo todos, y el acta lo dice con su
cifra*. **Releidos `1` de `1`, y se sostiene.** No invento una muestra donde no hay
poblacion, y no hay semilla que escribir porque no hay sorteo.

---

## 9. LA CORRECCION DEL `P13`, LEIDA ENTERA POR MI

Es el remedio heredado `2`, y lo leo en su sede, que es el `resumen_teorico` del nodo en
`dataset/nodos.jsonl`. Lo que la vuelta escribio, en corto y con sus palabras:

| lo que la correccion hace | lo comprobe |
|---|---|
| declara que el `P13` lleva un puente y lo **retira por declaracion** | si |
| **no borra** el texto viejo del paso, y lo cita entero dentro del bloque | si |
| **pega la linea `215`** desde su instrumento, con `grep -n -o` | si, y la volvi a sacar yo en `0.2` |
| **no elige** ninguna de las dos lecturas de la errata | si: dice literal *QUEDA FUERA DEL PROCEDIMIENTO Y SE DECLARA SIN ELEGIR* |
| declara la contradiccion de la linea con su frase siguiente | si |
| **corrige la cuenta de fidelidad del propio resumen sin borrarla**: donde decia `17` TRANSCRIPCION y `0` PUENTE, la cuenta buena es `16` y `1` | si |
| explica **por que esta via y no otra**: `src/correccion.py` solo toca el `resumen_teorico`, e `insertar` rechaza un id que ya vive | si, y lo comprobe en la ayuda de `forja.py` |

**LAS SIETE CONDICIONES DEL REMEDIO ESTAN. LO DOY POR CUMPLIDO.**

### 9.1. Y LA PREGUNTA QUE ESTA CORRECCION DEJA ABIERTA, QUE NO ES UNA CAIDA

**EL TEXTO DEL PASO `P13` SIGUE SIENDO EL MISMO EN `pasos_accionables`**, y lo compruebo:

```
$ python -c "<lector del P13 de practicar_franqueza_radical_jefe_propio en el dataset>"
 P13 Si reacciona bien y premia la franqueza, sigue. Si no, para inmediatamente, y no des por supuesta la mala intencion: vuelve a intentarlo con cuidado, y si la segunda vez la reaccion es la misma, puede que sea momento de irse.
```

Asi que hoy el grafo tiene **un paso cuyo propio nodo declara, mas abajo, que ese paso es
un puente retirado**. Quien lea `pasos_accionables`, que es para lo que existe un nodo, se
lleva el puente; quien lea el `resumen_teorico` se entera de que esta retirado.

**NO LO CARGO COMO CAIDA, Y DIGO POR QUE:** el remedio que yo escribi pedia `corregir` por
`D.13` **sin borrar**, y eso es exactamente lo que la casa sabe hacer hoy. **Pedir mas
habria sido pedir un instrumento que no existe**, y `7.F` de la cosecha me prohibe encargar
maquinaria nueva salvo que una caida de dato lo exija.

**LO QUE SI HAGO ES LEVANTARLA COMO PREGUNTA DE DOCTRINA**, porque no tiene casillero: el
gate tiene una guarda llamada `deprecado_en_superficie`, pero es sobre **aristas** que
apuntan a nodos deprecados, no sobre **un paso retirado que sigue en la superficie**. **Es
la septima de la cola de doctrina del tablero, y como las seis de ahora, NO bloquea**: el
nodo esta dentro, el gate esta verde, la correccion esta declarada y la cifra corregida.
**Por `D.45` no la resuelvo yo mientras corran frentes en paralelo.**

---

## 10. LAS RACHAS, TAL COMO ME LLEGAN, Y EL INSTRUMENTO QUE HOY NO LAS PUEDE LEER

```
$ python forja.py credito
CREDITO DE LA LINEA 'serial' (D.48)
  registro: docs/loop/CREDITO_serial.jsonl

  LINEA SIN REGISTRO: no hay ningun suceso escrito.
  Una linea sin tandas NACE CON SU RACHA EN CERO y no hereda
  la de nadie (D.48). Lo que herede el arnes sera CERO remedios.
```

**ESA SALIDA NO DICE QUE MI RACHA SEA CERO: DICE QUE EL FICHERO NO ESTA EN EL ARBOL**, y no
esta porque el arnes lo retira en esta fase (seccion `1.1`). **No lo recupero.** La racha
viva me llega por el unico camino legitimo que tengo abierto ahora, que es el encabezado de
la `ACTA 33` que si puedo leer:

| especie | racha que heredo | de donde |
|---|---|---|
| `REPORTE` (extractor) | **`2 de 3`**, penultimo escalon | encabezado de la `ACTA 33` |
| `CLASE` | **`0 de 2`** | idem |
| `CIFRA PUBLICADA` | **`0 de 2`** | idem |
| `DATO MOVIDO` | **`0 de 2`** | idem |
| **la mia** (`REMEDIO ROTO` mas `CIFRA PUBLICADA PROPIA`) | **`2 de 3`**, penultimo escalon | idem |

**LO QUE ESTO SIGNIFICA PARA ESTA VUELTA, Y POR ESO LO ESCRIBO AQUI Y NO AL FINAL:** una
caida de `REPORTE` que viva en TABLA, CABECERA o CONCLUSION seria **la tercera seguida** y
**detiene el bucle**. Y una cifra falsa mia en este mismo documento seria **mi tercera** y
lo detiene igual. **Por eso este fichero no publica ni una cifra sin su comando al lado, y
por eso he corrido dos veces las que cambiaban mientras lo escribia.**

**Y NO ME REINICIO NADA:** la racha la pone a cero una tanda limpia o una decision escrita
de Alexis en `docs/loop/paradas/`, y **ninguna de las dos soy yo** (`5.4`).

---

## 11. EL TABLERO, LEIDO Y CITADO (`D.49`)

```
$ python forja.py tablero
TABLERO DE FRENTES (D.49, D.50): sede unica del estado de la campania
  registro: docs/loop/TABLERO.jsonl

  prio lote clave                          estado                 dueno                 band ult cap
  --------------------------------------------------------------------------------------------------------
  .    1    onu_consumidor                 INSERTADO              NINGUNO                  0  cap_02
  .    2    smart_who                      INSERTADO              NINGUNO                  0  cap_05
  .    3    zhuo_manager                   INSERTADO              NINGUNO                  0       .
  .    4    scott_radical_candor           CERRADO EN EXTRACCION  serial                  43  cap_14
  .    11   gerber_emyth_cap17_reservado   SIN EMPEZAR            NINGUNO                  0       .
  1    7    grove_high_output              EN CURSO               grove_high_output       23  cap_03
  2    9    gerber_emyth                   PAUSADO                NINGUNO                 10  cap_11
  3    5    marquet_turn_the_ship          PAUSADO                NINGUNO                  9  cap_03
  4*   8    bernerslee_bananas             SIN EMPEZAR            NINGUNO                  0       .
  5*   6    openstax_business_ethics       SIN EMPEZAR            NINGUNO                  0       .
  6*   10   openstax_org_behavior          SIN EMPEZAR            NINGUNO                  0       .

  libros CON DUEÑO ahora mismo: 2
    scott_radical_candor           lo trabaja 'serial' (CERRADO EN EXTRACCION)
    grove_high_output              lo trabaja 'grove_high_output' (EN CURSO)

  MUNDO 11: faltan 3 de 3 libros del corte (grove_high_output, gerber_emyth, marquet_turn_the_ship)

  COLA DE DOCTRINA (D.52): 6 pregunta(s), 0 bloquea(n)
```

| lo que el tablero me dice | |
|---|---|
| **el libro de esta vuelta** | `scott_radical_candor`, lote `4`, dueno `serial`, que es mi linea |
| **su estado** | `CERRADO EN EXTRACCION`. Lo que queda del libro es **insercion**, no extraccion |
| **lo que le queda en bandeja** | `43`, que son los `cap_10`, `cap_12`, `cap_13` y `cap_14` de la seccion `4.2` |
| **lo que NO toco** | los tres frentes en paralelo, sus ramas y sus bandejas (`D.45`) |
| **la cola de doctrina** | `6` preguntas, **ninguna bloquea**. La seccion `9.1` propone la septima |

**LECTURA:** el libro **no cierra** con esta vuelta y por lo tanto **no toca abrir el
siguiente por `D.32` ni relevar por `D.50`**: quedan `43` candidatos por insertar en la
misma clave, con el mismo dueno y en la misma rama. **El encargo de mi turno normal seguira
diciendo `LIBRO DE ESTA VUELTA: scott_radical_candor`.**

---

## 12. LOS `POR ADJUDICAR` QUE DEJO PARA MI TURNO NORMAL

Son las preguntas que **no** puedo cerrar sin el reporte delante. Las escribo numeradas
para poder cerrarlas una a una en el acta, como manda `5.3`.

| # | que es | por que no la cierro hoy |
|---:|---|---|
| **1** | la fila de `cap_09` del reporte: dice el numerador corregido (`1`) citando la `ACTA 33`? | es el remedio heredado `3`, y su sede esta retirada |
| **2** | **la cifra `15 de 15 del capitulo`**: que poblacion nombra ese `15`, si el capitulo tiene `20` nodos y `0` en bandeja? | seccion `4.1`. **Si esa cifra vive en TABLA, CABECERA o CONCLUSION del reporte, es el tercer escalon de `REPORTE`** |
| **3** | el reporte nombra los pasos releidos por polaridad (remedio `4`)? y cual de las `6` marco como discutible? | mi barrido da `6 de 6` SANAS. **Si el suyo marca una, o la sostengo o cae una de las dos lecturas** |
| **4** | el reporte declara `0 PUENTE de 91` con el mismo reparto por pieza que mi seccion `5.1`? | mi cuenta esta escrita antes de verlo |
| **5** | mis cuatro `razon` sin destapar, contra mis tres clases de la seccion `8` | la comparacion que mide algo es esa, y la hago con el acta |
| **6** | el `diff` de dato de los commits de la vuelta, mirado linea a linea | hoy compruebo el saldo (`+5`, `+4`, cero desaparecidos); el contenido de cada linea va en el acta |
| **7** | la suite de aceptacion, firmada con el arbol completo | hoy son `3` fallos y los tres cuelgan de un fichero retirado (`2.1`) |
| **8** | la exencion que le falta al censo de rutas para `APERTURA_CIEGA.md` | es maquinaria del arnes (`D.33`), y va **de propuesta** al encargo |
| **9** | la pregunta de doctrina de la seccion `9.1`, para la cola del tablero | `D.45`: no la resuelvo yo mientras corran frentes en paralelo |

**NINGUNA DE LAS NUEVE ES PARADA HOY**, y lo digo con `3` delante: no hace falta doctrina
nueva para seguir, no hay contradiccion con regla vigente sin via de correccion, y ninguna
de las tres guardas de dato (cerrojo, `D.44`, aduana) tiene nada que decir en esta vuelta.

---

## 13. LO QUE ESTA APERTURA SOSTIENE, EN UNA TABLA

| | lo que medi | con que |
|---|---|---|
| **guardas** | `gate`, `guiones`, `resolutor` **VERDES** sobre `302` nodos | los tres instrumentos, corridos hoy |
| **vigencia** | `49` hallazgos sobre `413` veredictos: **cola de trabajo, no rojo** (`D.15`) | `forja.py rancios` |
| **suite** | `274` pruebas, `4` fallos antes de escribir esto y **`3` despues**, los tres de sede retirada | dos corridas, las dos pegadas |
| **censo de rutas** | `1` ruta en rojo antes, **`0` despues**: era este fichero | `scripts/cerrar_reporte.py --hook`, dos corridas |
| **dato** | `297` a `302` nodos, `+4` veredictos, **cero nodos desaparecidos** | `numstat` y comparacion de ids |
| **material** | `cap_09` = `433` lineas, `20` nodos, `272` pasos, **`0` en bandeja** | tres instrumentos para las lineas, el dataset para lo demas |
| **fidelidad `D.30`** | los `91` pasos del tramo releidos uno a uno: **`91` TRANSCRIPCION, `0` PUENTE** | el libro contra el dataset |
| **`PASOS INVENTADOS`** | `cap_09` entero: **`1` de `272`**, que es `0,37` por ciento | la suma de los dos tramos |
| **polaridad** | `25` disyunciones, `7` a maquina, **`6` tras releer, `6` SANAS** | mi barrido, con `L215` de control |
| **vecinos `D.38.4`** | poblacion `348` (`297` mas `51`), **`3` vecindades**, las tres por `familia_id` | `forja.py informe` sobre copias fuera del repo |
| **clases** | **`3` adjudicadas por mi, las `3` coinciden** con la clase escrita. `0` SANO sin razon | los pasos de los dos nodos de cada par |
| **herencia** | `5` de `5` declarados **CUMPLIDO**, con su salida pegada | la seccion `0` entera |

**Y LO QUE ESTA APERTURA NO SOSTIENE, QUE TAMBIEN ES SUYO:** no he visto el reporte, asi que
**no digo nada de lo que el reporte dice**. Las nueve preguntas de la seccion `12` son
exactamente eso, y ninguna la resuelvo adivinando.
