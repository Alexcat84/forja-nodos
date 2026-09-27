# APERTURA CIEGA DE LA VUELTA 79, lote 5 (`marquet_turn_the_ship`), **CLASE SANEAMIENTO**

*Auditor `claude-opus-5-5`, fase ciega, 26 sep 2026. En la corrida que arranco el 26 a las `09:27`, el arnes la numera `VUELTA 3`.
Linea **serial**, rama `extraccion-mundo-11`. Modo austero (`D.47`). Todo lo de esta pagina sale de `.v79aud/`, escrito y
corrido en esta fase; cada bloque `$` lo pega `.v79aud/generar_apertura.py` corriendo el comando en el momento de escribirla.
**No hay ninguna tabla en esta pagina**, a proposito, como en la `73` y de la `75` a la `78`.*

**LA VUELTA NO TRAE CANDIDATOS NUEVOS**: es de saneamiento, no inserta y su encargo le prohibe tocar `cuarentena/`. **Lo que clasifico
a ciegas es el material que la vuelta tenia que leer** (mi encargo, `docs/loop/PROMPT_SIGUIENTE.md`): la frontera de Zhuo que va a
relectura conjunta (seccion `3`); las dos posiciones de la frontera de Grove, escritas por mi para cruzarlas con el texto que la vuelta
deja preparado (seccion `4`); `d150` y `d180` (seccion `5`); y los cuatro punteros de Gerber, `d098`, `d104`, `d099` y `d135`, medidos
contra el grafo de hoy y leidos contra su linea del libro (seccion `6`). Las fichas de Marquet que esperan en la bandeja ya las
clasifique a ciegas en la `78`, y la seccion `7` dice por que esa lectura sigue en pie sin rehacerla.

**UNA LIMITACION DE METODO, DICHA ANTES DE NADA: EN ESTA FASE NO HE CORRIDO `git` SOBRE EL REPOSITORIO**, ni una vez, como de la `73`
a la `78`: la carpeta de una linea viva es solo del arnes (`PARALELO.md` `7`). **Lo que se mide con `git` aqui no lo mido**: que commit
movio que y a que hora, y en particular **el commit que cambio `src/tablero.py`**, que `d180` pide. El commit en que esta el arbol lo
leo de los ficheros de `.git/`:

@@RUN:0::cat .git/HEAD; cat .git/refs/heads/extraccion-mundo-11@@

## 0. **LA HERENCIA** (`D.40`)

ACTA ANTERIOR LEIDA: 34108a4eaed142687bc76148a037246f5d125ccb

**Comprobada sin git**: es el blob de `docs/loop/ACTA_AUDITOR.md` tal como esta hoy en el arbol, calculado como lo calcula git. **La
`ACTA 77` la lei entera**, de su linea de cabecera a la ultima del fichero, y con ella el encargo que me deje. **No hay hueco de acta**
(`1.0`): la `ACTA 77` cubre la vuelta `78`, y la que viene a auditarse es la `79`.

@@RUN:0::python .v79aud/huella_acta.py@@

HEREDADO 1: NO APLICA en esta fase. **Motivo:** `R5` es un remedio **del extractor** y se mide **sobre su reporte de la `79`**
(`ACTA 77` `77.11`: *el reporte de la `79`, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera cambiada a
la `79`*), y el reporte **no esta en el arbol**: el arnes lo retiro para esta fase (`D.34.2`) y no lo he recuperado por ninguna via.
**Se mide en mi turno normal**, con los dos instrumentos sacados otra vez de los originales y no de las copias del extractor. Lo que
si esta en mi mano lo cumplo en mi pagina: cada bloque `$` lleva la salida del comando que abre, y nada mas.

@@RUN:0::ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl@@
@@RUN:0::grep -n "VUELTA 3 : APERTURA CIEGA" docs/loop/loop.log | tail -1@@

HEREDADO 2: CUMPLIDO. **`R6`, mio** (`ACTA 77` `77.11`): en esta fase los pasos de cualquier nodo los imprime
`.v67aud/normal/pasos_ciego.py`, que no ensenia `previos` ni `siguientes`: con el lei los cuatro nodos de las dos fronteras
(`.v79aud/pasos_fronteras.txt`), los de `d098` y `d104` (`.v79aud/pasos_d098_d104.txt`) y los de `d099` (`.v79aud/pasos_d099.txt`), y
los bloques de pasos de esta pagina los corre el. De mis dos instrumentos nuevos, `grep_poblacion.py` **salta las claves de relacion
por codigo** y `origen_gerber.py` **solo lee `resumen_teorico`**, y los dos lo dicen en su cabecera. Las lineas de esos ficheros que
**empiezan** por una clave de relacion, y los instrumentos mios de esta fase que las **nombran**, con su lectura debajo:

@@RUN:0::grep -c -E "^ *(previos|siguientes|nodos_previos|nodos_siguientes)" .v79aud/pasos_fronteras.txt .v79aud/pasos_d098_d104.txt .v79aud/pasos_d099.txt@@
@@RUN:0::grep -l -E "previos|siguientes" .v79aud/*.py@@

**LECTURA:** el unico que las nombra es `grep_poblacion.py`, y **las nombra para excluirlas** (su conjunto `FUERA` y su cabecera).
**LO UNICO QUE SE ACERCA, para que se juzgue:** al abrir la fase imprimi la lista de
**nombres** de claves de un nodo de Gerber del grafo (entre ellos `nodos_previos` y `nodos_siguientes`), **sin sus valores**. **No vi
ninguna clave de relacion con su valor de ningun nodo en esta fase.** La pagina entera la mide un `grep` sobre ella al cerrarla
(seccion `10`).

HEREDADO 3: CUMPLIDO. **`R7`, mio** (`ACTA 77` `77.11`): toda linea de esta pagina que reparte un total en clases la imprime un
instrumento que cuenta **todas** las clases con el mismo predicado y **dice su `suma`**: los dos mios nuevos de `.v79aud/` la traen
(`grep_poblacion.py` por sede y `origen_gerber.py` por capitulo), y los que reuso sin copiar (`.v70aud/poblacion.py` y el de `R8`) ya la
traian. **Medido sobre la pagina misma** en la seccion `10`, con la copia de `.v78aud/r7_pagina.py`.

HEREDADO 4: CUMPLIDO. **`R8`, mio** (`ACTA 77` `77.11`, *mi fase ciega de la `79`, sobre el encargo de la `79`*): **lo mido aqui con
el mismo instrumento de la `77.12`, `.v78aud/normal/r8_encargo79.py`, sin copiarlo**, y su salida de hoy es identica a la que aquella
acta guardo; la lectura, linea a linea, en la seccion `8`. El encargo de la `80` lo escribo en mi turno normal y se mide alli.

HEREDADO 5: NO APLICA en esta fase. **Motivo:** `R9` es un remedio **del extractor** y se comprueba **en el reporte de la `79`, si
publica una cuenta de PUENTE** (`ACTA 77` `77.11`), y el reporte no esta en el arbol (bloque del HEREDADO `1`). **Y esta vuelta no marca
fidelidad**: es de saneamiento y su encargo no le pide ninguna fila de `D.30` (TAREA `2` a TAREA `5`); si su reporte trae aun asi una
cuenta de PUENTE, `R9` se mide alli en mi turno normal. Lo que el encargo le pide, por sus titulos:

@@RUN:0::grep -n "^## TAREA" docs/loop/PROMPT_SIGUIENTE.md@@
@@RUN:0::grep -n -i -E "puente|fidelidad" docs/loop/PROMPT_SIGUIENTE.md | cut -c1-90@@

**LECTURA del segundo bloque:** las lineas del encargo que dicen *puente* o *fidelidad* son una fila de la tabla de registros de la
TAREA `1` (lo que la `ACTA 77` ya cruzo) y la de `d150` (la fila de fidelidad de `cap_03` que la `78` ya dio y la `ACTA 77` `77.3`
firmo); **ninguna le manda marcar pasos**.

HEREDADO 6: CUMPLIDO. **`R10`, mio** (`ACTA 77` `77.11` y `77.13`): toda salida pegada en `PROMPT_SIGUIENTE.md` se corre despues de la
ultima escritura del auditor en el registro que mide, o se vuelve a correr antes del commit y se compara. **Se cumplio al cerrar la
`ACTA 77`**, con sus tres salidas comparadas despues de mis dos anotaciones (primera parte del bloque). **Lo que mido hoy**: que mi ultima
anotacion en `DEUDA.jsonl` (la de `d183`) es anterior al encargo, leida de su campo `anotada` y no de la hora del fichero, que despues
movio el extractor; y el bloque del tablero, vuelto a correr hoy e identico. **Una limitacion, dicha:** los otros dos bloques del
encargo miden `DEUDA.jsonl`, que el extractor escribio despues en esta vuelta, y hoy ya no son comparables; y `CREDITO_serial.jsonl`
esta retirado. **La otra mitad de su sitio, la `ACTA 78`, es de mi turno normal.**

@@RUN:0::bash .v79aud/r10.sh@@

## 1. **LO QUE VI SIN BUSCARLO, Y LO DIGO ANTES DE MEDIR** (`d146`)

**La foto de `git status` que el entorno me pone delante trae los asuntos de los ultimos commits de la rama, todos del extractor de
la `79`, y traen cifras y conclusiones de su vuelta**: `afe5ba49` (*los registros de la ACTA 77; la frontera de Zhuo la gana la lectura del auditor
(convergencia, fila corregida sin borrar) y el texto de la de Grove queda preparado en .v79ext/frontera_grove.txt, sin correr
corregir*), `b1b0b332` (*d150 y d180 pagadas por medida (.vm01 con 47 ficheros y la fila de cap_03 de 78.2.4 firmada en ACTA 77 77.3;
grove y gerber INSERTADO en el tablero, commit ccf9498f, sin tocar src)*), `891166bd` (*d098, d099 y d135 pagadas por medida contra el
grafo de hoy; d104 no pagada y traida (el paso 5 de distinguir_tres_tipos_sistemas_negocio nombra las tres actividades de cap_12 L21
sin cuenta, puerta de D.29)*), `318e4a74` (*el cierre (declarada de saneamiento; censo 459, 1172, 1, 20, 0 al abrir y al cerrar; huellas
de las 20 de Marquet identicas a las de la 78; cinco deudas pagadas y d104 traida; gate, guiones, suite y cierre estricto en verde; R5
en cero; ninguna insertada)*) y `da0b8787` (*la salida del hook del commit del cierre*). **Los lei antes de medir nada.** Es el mismo
hueco de `d146` que declararon las aperturas de la `65` a la `78`, y no lo arreglo yo (`D.45`).

**Y LO DEMAS DEL MISMO TIPO, QUE ES MIO:** la cola de `docs/loop/loop.log`, que no se retira (la hora y el coste del turno del
extractor); mi `ACTA 77` entera y mi encargo; **cuantos** ficheros tiene `.v79ext/` (un `ls | wc -l`, sin sus nombres; el unico nombre
que conozco es el que trae el asunto de `afe5ba49`); y al leer el texto de las deudas en `docs/loop/DEUDA.jsonl` imprimi **las claves**
de sus lineas, que dicen que hay **una linea de pago de la vuelta `79` para `d150`, `d180`, `d098`, `d099` y `d135`, ninguna para
`d104` ni `d183`**, y una linea de tipo `saneamiento` de la `79`. **De esas lineas no lei su `como`.**

**LO QUE HAGO CON ELLO:** ninguna cifra de esta pagina sale de esos asuntos; todas salen de un instrumento corrido en esta fase, y
donde coinciden lo digo como coincidencia y no como fuente. **No he abierto nada de `.v79ext/` por dentro**, **ni
`bitacora/VEREDICTOS.jsonl` por dentro**: de ella solo cuento lineas. **Y ESTO SI PESA SOBRE MI LECTURA, Y LO DIGO:** el asunto de
`afe5ba49` me dijo que la frontera de Zhuo la gana mi lectura, y la mia de la seccion `3` es la de la `ACTA 77` `77.5`, sellada antes;
**y el de `891166bd` me dijo que `d104` no se pago y por que**. Mi lectura de `d104` (seccion `6`) es otra en su consecuencia, y la
escribo con sus lineas; **pero no puedo probar que ese asunto no me hizo mirar el paso `5` antes que otra cosa.**

## 2. **EL ALCANCE, Y EL CENSO QUE LO SOSTIENE**

**El censo de hoy**, sin `git` (grafo, bitacora, pares mutuos; la bandeja de Marquet y sus insertados, la de Gerber y sus insertados,
y `procesos/`), la poblacion de la aduana y el `gate`:

@@RUN:0::wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl@@
@@RUN:0::for d in cuarentena/marquet_turn_the_ship cuarentena/_insertados/marquet_turn_the_ship cuarentena/gerber_emyth cuarentena/_insertados/gerber_emyth; do echo "$d $(find $d -maxdepth 1 -name '*.json' 2>/dev/null | wc -l)"; done; echo "procesos $(ls -A procesos/ | wc -l)"@@
@@RUN:0::python .v70aud/poblacion.py@@
@@RUN:0::python forja.py gate | head -2@@

**Lo que es mas nuevo que mi encargo** en las carpetas de dato, de codigo y de libro, y en `docs/`; y **las fichas de Marquet y el
grafo contra mis huellas de la `78`**, tomadas antes de mi barrido de entonces:

@@RUN:0::ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, substr($7,1,8), $9}'@@
@@RUN:0::find cuarentena dataset bitacora censos config fuentes esquema src scripts tests forja.py -type f -newer docs/loop/PROMPT_SIGUIENTE.md | wc -l@@
@@RUN:0::find docs -type f -newer docs/loop/PROMPT_SIGUIENTE.md | sort@@
@@RUN:0::wc -l < .v78aud/huellas_al_barrer.txt; sha1sum -c --quiet .v78aud/huellas_al_barrer.txt && echo "las fichas de la bandeja de Marquet y el grafo de hoy: mismas huellas que al barrer en mi fase ciega de la 78"@@

**LECTURA:**

1. El grafo, la bitacora y los pares mutuos, la bandeja de Marquet llena y sin insertados, y Gerber entero en `_insertados`, son los de
   mi `ACTA 77` `77.1`: **la vuelta no inserto nada ni movio nada de sede**, que es lo que el encargo pedia, y `procesos/` esta vacio. La
   poblacion del barrido sigue siendo la de la `77.1`.
2. **Ningun fichero de las carpetas de dato, de codigo o de libro es mas nuevo que mi encargo**, y **las fichas de Marquet y el grafo son
   byte a byte los de mi fase ciega de la `78`**: la vuelta no toco la bandeja (`d031`). En `docs/` lo mas nuevo es de `docs/loop/`: el
   registro de deudas (los pagos de la seccion `1`), el tablero y el log (el arnes), y mi `ACTA_AUDITOR.md`, **cuya hora es de antes de que
   arrancase el turno del extractor** (`loop.log`, abajo) y **cuyo blob es la huella que el prompt me da** (seccion `0`): no la toco nadie
   despues de mi.
3. **Lo que no puedo decir sin `git`**: si alguna linea de la bitacora cambio sin cambiar la cuenta ni la hora del fichero; la bitacora no
   tiene huella mia de la `78`. Eso lo mido en mi turno normal, con el hash del reporte delante.

@@RUN:0::grep -E "auditor listo|VUELTA 3 : EXTRACTOR|extractor listo" docs/loop/loop.log | tail -3; ls -l --time-style=full-iso docs/loop/ACTA_AUDITOR.md | awk '{print $6, substr($7,1,8), $9}'@@

## 3. **LA FRONTERA DE ZHUO: MI CLASE, CON LOS PASOS Y LAS LINEAS DELANTE** (`1.3`, `6.1`, `R7`)

**El par**: `comunicar_valores_diez_formas` (Zhuo, en el grafo) contra `repetir_mensaje_invariable_diario_reunion_evento` (Marquet, en
la bandeja). Los pasos que tocan el mensaje y su repeticion, y las lineas del libro:

@@RUN:0::python .v67aud/normal/pasos_ciego.py comunicar_valores_diez_formas repetir_mensaje_invariable_diario_reunion_evento | grep -E "^=====|  P[1-5]\. "@@
@@RUN:0::grep -n -o "Assume that for the message to stick, it should be heard ten different times and said in ten different ways\|The more you can enlist others to help spread your message" fuentes/zhuo_manager/cap_11.md@@
@@RUN:0::grep -n -o "What I realized, however, is the need for a relentless, consistent repetition of the message\|Repeat the same message day after day, meeting after meeting, event after event\|Changing the message? That results in confusion and a lack of direction" fuentes/marquet_turn_the_ship/cap_13.md@@

**MI CLASE: SIN CONTRADICCION. NO ES FRONTERA DECLARADA, Y EL PAR SIGUE `SANO` SIN ARISTA**, que es mi lectura sellada de la `78` y mi caso
de la `ACTA 77` `77.5`, **releida hoy y no copiada**, con la vara `6.1` y solo esa (`R7`):

- **Los dos mandan repetir el mismo mensaje.** Zhuo `L91`: el mensaje tiene que oirse muchas veces para calar, y cuantos mas lo
  extiendan, mejor. Marquet `L115` y `L119`: repeticion *relentless, consistent*, dia tras dia, reunion tras reunion, evento tras evento.
- **Lo que Zhuo varia es la FORMA** (*said in ten different ways*) y **la VIA** (su paso `5`, las vias que prueba). **Lo que Marquet
  prohibe cambiar es EL MENSAJE** (*Changing the message? That results in confusion and a lack of direction*), que es el contenido y
  la direccion. **Marquet no manda repetir las mismas palabras**, y su propio paso `1` varia la ocasion (la rutina, la reunion, el
  evento), que es la via de Zhuo. **Una doctrina dice como decir mas veces lo mismo; la otra, que no se cambie lo que se dice.** Se
  suman; no se contradicen.
- **La lectura contraria, escrita otra vez para que se pueda elegir**: *redundant, repetitive, and boring* de `L119` puede leerse como
  repetir la misma formulacion, y entonces *ten different ways* seria su contrario. **No la sostengo**: *boring* es lo que el lider teme
  que suene, no lo que manda hacer, y la alternativa que `L119` descarta es cambiar el mensaje, no reformularlo.
- **No es duplicado** (`6.1`, *no tiene bascula*): fuera de lo comun, Zhuo trae procedimiento propio (reclutar a otros, sus vias, meter
  los traspies, el metodo de Sandberg) y Marquet trae su linea propia, *no cambies el mensaje*, con su condicion propia (un cambio que la
  gente no logra imaginar). **Lo que ya adjudico la `ACTA 77` `77.4` (`SANO`) no se reabre** (`D.47`).

**CONSECUENCIA PARA LA TAREA `2`:** si mi lectura gana, **no hay texto de frontera de Zhuo que preparar**, y la fila de su fichero de
aristas se corrige por correccion declarada sin borrarla (mi encargo, TAREA `2` punto `1`). **Que la gano lo dice un asunto que vi**
(seccion `1`), y eso no es medirlo: **lo mido en mi turno normal**, leyendo su decision y su razon.

## 4. **LA FRONTERA DE GROVE: LAS DOS POSICIONES, ESCRITAS POR MI ANTES DE LEER LAS SUYAS** (`6.1`, `d183`)

**Sostenida en la `ACTA 77` `77.5`**, y hoy vuelta a leer con los pasos y las lineas delante:

@@RUN:0::python .v67aud/normal/pasos_ciego.py delegar_tarea_base_comun_seguimiento eliminar_seguimiento_descendente_responsabilizar_dueno | grep -E "^=====|  P[678]\. |  P[12]\. Di|  P[12]\. De"@@
@@RUN:0::grep -n -o "delegation without follow-through is abdication\|Even after you delegate it, you are still responsible for its accomplishment\|monitoring the delegated task is the only practical way for you to ensure a result" fuentes/grove_high_output/cap_04.md@@
@@RUN:0::grep -n -o "You are responsible, not me and not the XO, for getting it done\|we unburdened ourselves of the effort of maintaining the tickler\|simply report conditions without judgment\|What you want to avoid are the systems whereby senior personnel are determining what junior personnel should be doing" fuentes/marquet_turn_the_ship/cap_09.md@@

**MI CLASE: FRONTERA DECLARADA, SE SOSTIENE.** El choque esta en **quien responde de la tarea y quien la vigila**:

- **POSICION DE GROVE** (`delegar_tarea_base_comun_seguimiento`, pasos `6` a `8`; `cap_04` `L249`): **el que delega sigue respondiendo
  de la tarea y la vigila**. *delegation without follow-through is abdication*; *Even after you delegate it, you are still responsible
  for its accomplishment*, y vigilar la tarea delegada es la unica via practica de asegurar el resultado. Vigilar no es entrometerse.
- **POSICION DE MARQUET** (`eliminar_seguimiento_descendente_responsabilizar_dueno`, pasos `1` y `2`; `cap_09` `L71`, `L73` y `L85`):
  **responde el dueno y vigila el dueno, no el de arriba**. *You are responsible, not me and not the XO, for getting it done*; se
  suprime el sistema con el que el de arriba seguia los pendientes del de abajo (*we unburdened ourselves of the effort of maintaining
  the tickler*), y se conserva solo la medicion que informa sin juzgar (*simply report conditions without judgment*); lo que se evita son
  *the systems whereby senior personnel are determining what junior personnel should be doing*.
- **Por que es frontera y no convergencia**: los dos admiten medir, pero Grove pone la responsabilidad y el seguimiento **en el que
  delega** y Marquet **se los quita**. Son dos doctrinas legitimas con sus fuentes, y **ninguna es madre de la otra** (`6.1`, *dos
  doctrinas legitimas no son duplicado*). **La arista no se pone**: es frontera, no linaje.

**LO QUE ESPERO DEL TEXTO QUE LA VUELTA DEJA EN `.v79ext/`**, para cruzarlo en mi turno normal: las dos posiciones de arriba, **cada
una con el paso de su nodo y su linea del libro**, empezando por `CORRECCION DECLARADA`, para `forja.py corregir` sobre el nodo de
Marquet **despues de que entre** (mi encargo, TAREA `2` punto `2`), y **sin haber corrido `corregir`**. **Si su texto le atribuye a
Marquet que suprime toda medicion, o a Grove que manda entrometerse, lo corrijo**: `L85` conserva la medicion y `L249` separa vigilar
de entrometerse.

## 5. **`d150` Y `d180`: MIS DOS CLASES, POR MEDIDA**

**`d150`** pide la fila de fidelidad de `cap_03` de Marquet y los papeles de `.vm01/` intactos, contados en ficheros como su cita:

@@RUN:0::grep -o '"que": "[^"]*"' docs/loop/DEUDA.jsonl | grep -n "vuelta 1 del frente marquet"; find .vm01 -type f | wc -l@@

**MI CLASE: SE PAGA.** La cuenta de `.vm01/` es la que su propio texto pone, y la fila de `cap_03` es la de su `78.2.4`, que **mi `ACTA
77` `77.3` firmo** con mi lectura sellada al lado. Lo que queda de su letra (reescribir las tareas del reporte archivado del frente)
**no se escribe**: la relectura entera de la `78` lo sustituye (`77.3`). **Que `.vm01/` no cambio por dentro, fichero a fichero, necesita
`git`**: turno normal.

**`d180`** pide que el tablero llame `INSERTADO` a los libros cosechados que ya entraron enteros:

@@RUN:0::python forja.py tablero | grep -E "^ +[0-9]+ +[0-9]+ +(grove_high_output|gerber_emyth|marquet_turn_the_ship) |MUNDO 11"@@
@@RUN:0::grep -n -E "UN COSECHADO QUE YA ENTRO ENTERO|candidatos == 0 and en_grafo > 0 and unidades" src/tablero.py; ls -l --time-style=full-iso src/tablero.py | awk '{print $6, substr($7,1,8), $9}'@@

**MI CLASE: SE PAGA.** Grove y Gerber salen `INSERTADO`; Marquet sigue `COSECHADO` con su bandeja llena, que es lo cierto hasta que
entre. La rama que lo hace vive en `src/tablero.py` (segundo bloque), **y el fichero es de antes que mi encargo**: esta vuelta no lo toco,
que es lo que `7.F` y `D.55` piden. **El commit que lo cambio lo da `git log` y lo cruzo en mi turno normal** contra el que su reporte
pegue.

## 6. **LOS CUATRO PUNTEROS DE GERBER, CONTRA EL GRAFO DE HOY** (`D.37`, `D.29`, `6.1`, `D.38.4`)

**La medida de todo el apartado es sobre GRAFO MAS BANDEJAS** (`D.38.4`), con `.v79aud/grep_poblacion.py`, que salta `_insertados`,
`_derivadas` y la carpeta de ensayo, como `pasos_ciego.py`, y **nunca busca en claves de relacion** (`R6`).

### 6.1. **`d098`: la cabeza de las tres fases de crecimiento** (`cap_05` `L29`)

@@RUN:0::grep -n -o "the three phases of a business.s growth: Infancy, Adolescence, and Maturity" fuentes/gerber_emyth/cap_05.md@@
@@RUN:0::python .v79aud/grep_poblacion.py "infancy|adolescence|infancia|adolescencia|fases? de(l)? crecimiento|tres fases" | cut -c1-200@@
@@RUN:0::python .v79aud/grep_poblacion.py "infancy|adolescence|maturity|infancia|adolescencia|madurez|fases? de(l)? crecimiento|tres fases" gerber_emyth@@

**LECTURA:** en toda la poblacion, lo que casa con las fases o con *infancia* y *adolescencia* son nodos de otros libros donde son la
infancia y la adolescencia de una persona (primer bloque de busqueda: una tradicion de equipo, una historia de vida y un hijo). **En Gerber solo casan los dos
nodos de `cap_08`**, y casan por el titulo del capitulo (*Maturity and the Entrepreneurial Perspective*) en su frase de origen, **no por
su texto**: `construir_empresa_plantilla_vision_diaria` y `trazar_modelo_negocio_cliente_primero` procedimentan la perspectiva del
emprendedor (las tres razones de Watson; el modelo que arranca del cliente), no la fase.

**MI CLASE: NO NACIO NINGUNA CABEZA DE LAS TRES FASES. SE PAGA.** `D.37` pide **el texto de un nodo que diga cuantas partes hay y las
nombre**, y ningun nodo nombra *Infancy*, *Adolescence* y *Maturity* como partes. **Y aunque se leyera un nodo de `cap_08` como el nodo
de Maturity que `d098` preveia**, la arista cabeza a parte **no tiene cabeza**: no hay de donde colgarla. El libro ya no se extrae
(`PARALELO.md` `8` punto `3`), asi que la cabeza no va a nacer.

### 6.2. **`d104`: la cabeza de las tres actividades** (`cap_12` `L21`)

@@RUN:0::grep -n -o "Its foundation is three distinct yet thoroughly integrated activities\|They are Innovation, Quantification, and Orchestration" fuentes/gerber_emyth/cap_12.md@@
@@RUN:0::python .v79aud/grep_poblacion.py "innovation|quantification|orchestration|innovaci|cuantifica|orquesta" | tail -1@@
@@RUN:0::python .v79aud/grep_poblacion.py "innovation|quantification|orchestration|innovaci|cuantifica|orquesta" gerber_emyth | awk -F' [|] ' 'NF>3 {print $1}' | sort | uniq -c@@
@@RUN:0::python .v67aud/normal/pasos_ciego.py distinguir_tres_tipos_sistemas_negocio cuantificar_impacto_innovacion_6_pasos | grep -E "^=====|  titulo:|  cond:|  P[15]\. "@@
@@RUN:0::python .v79aud/grep_poblacion.py "metodo concreto dentro de Quantification|Innovacion de ejemplo" gerber_emyth | cut -c1-200@@

**LECTURA, nodo a nodo, de los cinco de Gerber que casan** (tercer bloque):

- **`distinguir_tres_tipos_sistemas_negocio`** (`cap_19`) es el unico cuyo texto **nombra las tres actividades juntas**, en su paso
  `5` y en su condicion: *la Innovacion, la Cuantificacion y la Orquestacion de estos tres tipos de sistemas*. **Las nombra sin decir
  cuantas son**: el *tres* de esa frase cuenta los tipos de sistemas (Hard, Soft, Information), que es lo que el nodo procedimenta, no las
  actividades. **Por la tabla de `D.37`, eso es *solo enumera sin decir cuantas*: `D.29` con razon escrita, no `D.37`.**
- **`cuantificar_impacto_innovacion_6_pasos`** (`cap_12`) es **un metodo dentro de Quantification** (su propio texto lo dice, ultimo
  bloque), y **`cambiar_saludo_cliente_dos_ramas` y `probar_traje_azul_seis_semanas`** (`cap_12`) son **ejemplos de Innovation** (sus
  denominaciones lo dicen). **Ninguno es la actividad entera**: son ejemplares de la parte, no la parte (la figura de `D68.7`, que la
  `76` leyo asi en Gerber). `aplicar_seis_pasos_sistema_venta` casa solo por *orquestada* en su nombre largo.

**MI LECTURA `D.29`, que es la puerta que queda**: ¿es `distinguir_tres_tipos_sistemas_negocio` madre de `cuantificar_impacto`, de
`cambiar_saludo` o de `probar_traje`? **NO LA SOSTENGO.** El producto de la madre es **saber de que tipo es cada sistema**, y ninguno de
los tres lo usa: uno cuenta puertas y compras antes y despues, otro cambia las palabras del saludo, otro prueba un traje. **El paso `5`
NOMBRA las actividades y no las procedimenta** (`6.1`, *nombrar no es procedimentar*). **DUDA, marcada y a la vista:** su condicion
dice *antes de poder innovarlo, cuantificarlo y orquestarlo*, que es un orden, y quien lo lea como madre de toda innovacion del negocio
leera la arista. **Me inclino a no**: un orden que el hijo no usa no es continuar su trabajo.

**MI CLASE: NO NACIO LA CABEZA QUE `D.37` NECESITA** (ningun nodo dice cuantas son las actividades y las nombra, y ninguna existe como
nodo entero), **Y MI LECTURA `D.29` NO DA ARISTA. `d104` SE PODRIA PAGAR con esta medida y esta lectura.** **Lo digo sabiendo que el
extractor no la pago y la trajo** (seccion `1`), con el paso `5` como puerta de `D.29`, que es justo lo que mi encargo le mandaba hacer si
leia que nacio algo (TAREA `4` punto `1`: *si nacio alguna, no la pagas y la traes*). **Traerla no es una caida suya**: es la lectura
prudente de mi letra. **La adjudicacion es mia y va a mi acta**, con esta lectura delante y la suya al lado.

### 6.3. **`d099`: donde nace el nodo de la delegacion** (`cap_18` `L345` a `L349`)

@@RUN:0::grep -n -o "Remember Delegation rather than Abdication\|You can.t delegate your accountabilities, Sarah\|Delegating your accountabilities is abdication\|And that means you must set the standard" fuentes/gerber_emyth/cap_18.md@@
@@RUN:0::python .v79aud/grep_poblacion.py "delega|abdica" gerber_emyth | cut -c1-200@@
@@RUN:0::python .v79aud/origen_gerber.py | sed -n 2p@@
@@RUN:0::python .v67aud/normal/pasos_ciego.py construir_estrategia_gente_cuatro_componentes aplicar_ocho_reglas_juego_personas aplicar_cinco_pasos_proceso_contratacion | grep -E "^=====|  titulo:"@@

**LECTURA:** **ningun nodo de Gerber que salga de `cap_18` habla de delegar.** Los de `cap_18` son la estrategia de la gente con sus
componentes, las reglas del juego y el proceso de contratacion (ultimo bloque), y **ninguno de sus pasos lleva `L345` a `L349`** (sus
pasos enteros, en `.v79aud/pasos_d099.txt`). El unico nodo de Gerber que nombra la delegacion es `operar_modelo_gente_destreza_minima`,
de `cap_11`, y la **nombra** como contraste en su ultimo paso (*Management by Abdication a la Management by Delegation*). El tramo de
`cap_18` es dialogo de Sarah que desemboca en *you must set the standard* y en el sistema de direccion: una advertencia dentro de otra
pieza.

**MI CLASE: NO NACIO. SE PAGA** diciendo que no nacio y que el libro ya no se extrae.

### 6.4. **`d135`: los tramos de `cap_03` (y de `cap_01`) que la insercion tendria que mirar**

@@RUN:0::python .v79aud/origen_gerber.py@@
@@RUN:0::for n in 169 201 225; do sed -n ${n}p fuentes/gerber_emyth/cap_03.md | cut -c1-90 | sed "s/^/L$n: /"; done@@

**LECTURA:** **ningun nodo de Gerber del grafo sale de `cap_03` ni de `cap_01`, y ninguno los nombra**: los tramos que `d135` lee y
descarta (los objetos de la jornada de Sarah, las etapas del proceso de la tia y los cuatro estados, en `cap_03`; y los de `cap_01`) **no
son origen de nada que haya entrado**, y la bandeja de Gerber esta vacia (seccion `2`). **MI CLASE: SE PAGA** con esa medida: quedan
leidos y descartados en la `ACTA G9`, y no hay nada que una insercion tuviera que mirar.

## 7. **LAS FICHAS DE MARQUET: MI LECTURA SELLADA DE LA `78` SIGUE EN PIE** (`D.38.4`, `D.38.5`, `d031`)

**No hay candidato nuevo ni ficha cambiada** (seccion `2`: las fichas de la bandeja y el grafo, byte a byte los de mis huellas de la `78`,
tomadas antes de mi barrido; la poblacion, la misma). **Mi fidelidad, mi barrido, mis clases, mi arista y mis restricciones de orden de
la `78`**, cruzados y adjudicados en la `ACTA 77`, **se leyeron sobre estos mismos bytes y esta misma poblacion**, asi que **no los
rehago**: rehacer un barrido sobre la misma entrada solo mediria el reloj. **Si la vuelta de insercion encuentra la bandeja o el grafo
movidos**, esa lectura deja de valer y se rehace entera (`d031`).

**`PASOS INVENTADOS POR CAPITULO`** (`8`): **esta vuelta no marca fidelidad** (HEREDADO `5`), asi que no hay fila que contar; la de las
fichas que entraran es la de la `ACTA 77` `77.3`. **La muestra pineada de los SANO** (`7`): esta vuelta no escribe en la bitacora
(seccion `2`); **no se inventa una muestra donde no hay poblacion**.

## 8. **`R8` MEDIDO SOBRE MI ENCARGO DE LA `79`, CON EL MISMO INSTRUMENTO** (`ACTA 77` `77.11` y `77.12`)

`R8` dice: *toda cifra de medida que escriba en `PROMPT_SIGUIENTE.md` (un reloj, una banda, una cuenta que solo se comprueba abriendo
un fichero, en digito o en letra) va DENTRO de un bloque `$` con su salida, o lleva EN SU MISMA LINEA la seccion del acta donde esta
pegada: ni la de la linea de al lado, ni una ruta de fichero*. El fichero es el encargo que escribi al cerrar la `ACTA 77`, y el
instrumento es el de la `77.12`, corrido sin copiarlo, con su salida de hoy contra la que guardo aquella acta:

@@RUN:0::head -1 docs/loop/PROMPT_SIGUIENTE.md | cut -c1-100; ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, $7, $9}'@@
@@RUN:0::python .v78aud/normal/r8_encargo79.py | diff - .v78aud/normal/r8_encargo79.txt && echo "IDENTICO a .v78aud/normal/r8_encargo79.txt, la salida de la ACTA 77 77.12"; python .v78aud/normal/r8_encargo79.py | tail -1@@

Las lineas de prosa con numero y **sin** seccion, cada una con los numeros que el instrumento le ve:

@@RUN:0::python .v78aud/normal/r8_encargo79.py | grep -E "^  L[0-9]+ - " | sed -E 's/\] \|.*$/]/'@@

**LECTURA, grupo a grupo, que es mia y no del instrumento; las volvi a leer una a una en el encargo y no copio la de la `77.12`:**

- **Numeros de vuelta, de acta, de mundo o de carpeta de la casa**: `L3`, `L28` y `L29` (el mundo), `L51`, `L66` y `L112` a `L115`
  (`.v78ext/`), `L71`, `L105`, `L110`, `L118` y `L122` (la `79`, la `80`, `.v79ext/`), `L81`, `L84` y `L99` (la `78`, `.vm01/`, la
  `ACTA 78`), `L83` (la vuelta del frente) y `L104` (la `ACTA G9`).
- **Secciones, reglas, deudas, remedios y numeros de tarea, de punto o de lista**: `L4`, `L14`, `L20` (`D.58`), `L22` (`d031`), `L46`,
  `L47`, `L53` (`D.47`), `L69` (`6.1`), `L77`, `L79`, `L86`, `L88` (`7.F`, `D.55`), `L91`, `L93`, `L96`, `L100`, `L102`, `L108`, `L110`
  (`d085`), `L116` (`D.61`), `L117` (`R5`), `L131`, `L133` y `L134` (`PARALELO.md` seccion `8`).
- **Identificadores de capitulo y de linea del libro**: `cap_17` en `L28`; `cap_13` `L119` en `L69`; `cap_03` en `L81`, `L102` y `L103`;
  `cap_05` `L29` y `cap_12` `L21` en `L97`; `cap_18` `L345` a `L349` en `L100` y `L101`.
- **Palabras de numero que no son cuenta de fichero**: *los dos delante* (`L69`, los dos nodos del par), *las dos posiciones* (`L71`, las
  de una frontera), *los dos nodos de Marquet* (`L76`, los dos que la misma TAREA nombra), *LAS DOS DEUDAS* (`L79`, `d150` y `d180`,
  nombradas en la misma linea), *la bandeja en cero* (`L86`, la condicion que `d180` describe, no una medida) y *cero guiones* (`L138`, la
  frase fija).
- **Las cifras de medida** van dentro de un bloque `$` (la clase, el tablero y las siete deudas) o llevan su seccion de la `ACTA 77` en
  la misma linea (las del instrumento con seccion).

**LAS CUENTAS EN LETRA**, que el instrumento ve por palabra, buscadas tambien con un `grep` mas ancho:

@@RUN:0::grep -n -i -w -E "uno|una|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|catorce|veinte|treinta|cero|mil|cien|ambas|ambos" docs/loop/PROMPT_SIGUIENTE.md | cut -c1-100@@

**LECTURA, linea a linea:** `L1` (*SEIS DEUDAS*) nombra las seis en la misma linea; `L41` esta **dentro de un bloque `$`** (el texto de
`d135` que imprime `deuda.py`); `L57`, `L59`, `L60` y `L62` son filas de la tabla de la TAREA `1` con **su seccion de la `ACTA 77` en la
misma fila** (*nueve instrumentos*, *catorce discutibles*, *mis dos dudas*, *dos fronteras*, *Cero caidas*); `L69`, `L71`, `L76`, `L79`,
`L86` y `L138` estan leidas arriba; las demas (`L22`, `L53`, `L72`, `L94`, `L99`, `L105`, `L112`) son **el articulo *una*** o *cada una*, no una cuenta.
**Ninguna linea de prosa trae una cifra de medida sin su bloque o su seccion en la misma linea: `R8` CUMPLIDO en el encargo de la `79`.**

## 9. **LO QUE DEJO PARA MI TURNO NORMAL, ESCRITO ANTES DE VER EL REPORTE**

1. **`R5`** en su reporte, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` sacados otra vez de los originales y con la
   cabecera cambiada a la `79`; **y `R9`**, si su reporte publica una cuenta de PUENTE.
2. **El censo con su hash**: que la vuelta no movio el grafo, la bitacora, los censos ni ninguna bandeja, **con `git diff`**, y quien
   escribio que y a que hora; y que `.vm01/` no cambio por dentro (`d150`).
3. **La conjunta de Zhuo**: su decision y su razon contra mi seccion `3`, y **su fila corregida sin borrar**.
4. **El texto de la frontera de Grove** que dejo en `.v79ext/`, contra mis dos posiciones de la seccion `4`: cada una con su paso y su
   linea, empezando por `CORRECCION DECLARADA`, y **sin `corregir` corrido**.
5. **Sus pagos, uno a uno, contra mis clases**: `d150` y `d180` (seccion `5`, con el commit de `src/tablero.py` por `git log`), `d098`,
   `d099` y `d135` (seccion `6`), leyendo su `como`; y que **`d183` no se pago**.
6. **`d104`**: su lectura del paso `5` contra la mia (seccion `6.2`), **adjudicada en mi acta con la vara**: si gana la mia, se paga en la
   vuelta que toque; si gana la suya, la arista que falte es de la `ACTA 78`, como dice mi encargo.
7. **La declaracion de saneamiento de la `79`** (`d085`), con `deuda.py --clase 80`, y **las huellas de las fichas de Marquet** que su
   cierre dice conservar, contra las mias de `.v78aud/huellas_al_barrer.txt` (seccion `2`).
8. **`R8` sobre el encargo de la `80`**, medido antes de cerrarlo, y **`R10`**. **La `80` inserta las fichas de Marquet y cierra la
   campania** (`ACTA 77` `77.10`), con el pago de `d183` despues de que entre `eliminar_seguimiento`.

## 10. **ESTA PAGINA CONTRA `R6`, `R7` Y LOS GUIONES, MEDIDA SOBRE ELLA MISMA**

El generador corre dos veces, y estos bloques de la segunda pasada leen la pagina que escribio la primera, identica salvo estos
bloques. El primero cuenta las lineas de bloque `$` que empiezan por una clave de relacion; el segundo, con la copia de
`.v78aud/r7_pagina.py`, cuenta las lineas de bloque que reparten una cifra en clases y cuantas traen su `suma`; el tercero cuenta
guiones largos y medios:

@@RUN:0::grep -c -E "^    +(previos|siguientes|nodos_previos|nodos_siguientes)" docs/loop/APERTURA_CIEGA.md@@
@@RUN:0::python .v79aud/r7_pagina.py@@
@@RUN:0::grep -c -P "\x{2014}|\x{2013}" docs/loop/APERTURA_CIEGA.md@@
