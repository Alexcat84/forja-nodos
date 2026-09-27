# APERTURA CIEGA DE LA VUELTA 74, lote 7 (`grove_high_output`), **CLASE SANEAMIENTO**

*Auditor `claude-opus-5-5`, fase ciega, 26 sep 2026. En la corrida que arranco el 25 a las `21:43`, el arnes la numera `VUELTA 3`.
Linea **serial**, rama `extraccion-mundo-11`. Modo austero (`D.47`). Todo lo de esta pagina sale de `.v74aud/`, escrito y
corrido en esta fase; cada bloque `$` lo pega `.v74aud/generar_apertura.py` corriendo el comando en el momento de escribirla.
**No hay ninguna tabla en esta pagina**, a proposito, como en la `72` y la `73`.*

**LA VUELTA NO TRAE CANDIDATOS NUEVOS**: es de saneamiento, no inserta y su encargo le prohibe tocar `cuarentena/`. **Lo que clasifico
a ciegas es el material que la vuelta tenia que leer**: los pasos de los tres nodos de `cap_13` de Scott que nombra `d084`, contra
el capitulo entero (seccion `3`); las fichas de la tanda `58` que nombra `d077` (seccion `4`); y los dos pasos de `d078` (seccion
`5`). Las fichas de Grove que esperan en la bandeja ya las clasifique a ciegas en la `73`, y la seccion `6` dice por que esa
lectura sigue en pie sin releerlas.

**UNA LIMITACION DE METODO, DICHA ANTES DE NADA: EN ESTA FASE NO HE CORRIDO `git` EN LA CARPETA**, ni una vez, como en la `73`: la
carpeta de una linea viva es solo del arnes (`PARALELO.md` `7`). **Lo que se mide con `git diff` aqui no lo mido**: que cambio la
vuelta linea a linea y contra que commit. El commit en que esta el arbol lo leo de los ficheros de `.git/`:

@@RUN:0::cat .git/HEAD; cat .git/refs/heads/extraccion-mundo-11@@

## 0. **LA HERENCIA** (`D.40`)

ACTA ANTERIOR LEIDA: a9550bfe65dfdc0769d8bac00412c9bbbaa362a3

**Comprobada sin git**: es el blob de `docs/loop/ACTA_AUDITOR.md` tal como esta hoy en el arbol, calculado como lo calcula git. **La
`ACTA 72` la lei entera**, de su linea de cabecera a la ultima del fichero:

@@RUN:0::python .v74aud/huella_acta.py@@

HEREDADO 1: NO APLICA en esta fase. **Motivo:** `R5` es un remedio **del extractor** y se mide **sobre su reporte de la `74`**
(`ACTA 72` `72.11`: *el reporte de la `74`, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py`, los dos con la cabecera
del tramo cambiada a la `74`*), y el reporte **no esta en el arbol**: el arnes lo retiro para esta fase (`D.34.2`) y no lo he
recuperado por ninguna via. **Se mide en mi turno normal**, con los dos instrumentos sacados otra vez de los originales y no de las
copias del extractor. Lo que si esta en mi mano lo cumplo en mi pagina: cada bloque `$` lleva la salida del comando que abre, y
nada mas.

@@RUN:0::ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl@@
@@RUN:0::grep -n "VUELTA 3 : APERTURA CIEGA" docs/loop/loop.log | tail -1@@

HEREDADO 2: CUMPLIDO. **`R6`, mio** (`ACTA 72` `72.11`): en esta fase los pasos de cualquier nodo los imprime
`.v67aud/normal/pasos_ciego.py`, que no enseña `previos` ni `siguientes`: con el lei los tres nodos de `d084`
(`.v74aud/pasos_tres.txt`) y los dos pasos de `d078` (seccion `5`, el unico bloque de pasos de esta pagina). Los ficheros de pasos
que lei, cuantas lineas con esas claves traen, y cuantos instrumentos mios las nombran:

@@RUN:0::grep -c -E "previos|siguientes" .v74aud/pasos_tres.txt@@
@@RUN:0::grep -l -E "previos|siguientes" .v74aud/*.py | wc -l@@

**LO UNICO QUE SE ACERCA, para que se juzgue:** `.v74aud/d077_ciego.py` (seccion `4`) imprime **los nombres** de los ficheros
`barrido_<id>.txt` y `vecinos_<id>.json` de las carpetas de vuelta, con su fecha, y **no su contenido**. **No vi ninguna clave de
relacion con su valor de ningun nodo en esta fase.** El cumplimiento de la pagina entera lo mide un `grep` sobre ella al cerrarla
(seccion `9`).

HEREDADO 3: CUMPLIDO. **`R7`, mio** (`ACTA 72` `72.11`): toda linea de esta pagina que reparte un total en clases la imprime un
instrumento que cuenta **todas** las clases con el mismo predicado y **dice su `suma`**: `contar_fidelidad`, `firma_cap13` (que
reparte en dos clases lo que el libro mayor de la `ACTA 58` imprime por nodo), `huellas_contra_73`, `d077_ciego`, la copia de
`.v70aud/poblacion.py`, y el de `R8`, que es el de la `ACTA 72` sin tocar. **Medido sobre la pagina misma** en la seccion `9`, con la
copia de `.v73aud/r7_pagina.py`.

HEREDADO 4: CUMPLIDO. **`R8`, mio** (`ACTA 72` `72.11`): se comprueba **aqui**, en mi fase ciega, sobre el encargo de la `74`, **con
el mismo instrumento y leyendo sus lineas**. Lo corri sin copiarlo (`.v73aud/normal/r8_encargo74.py`), su salida es identica a la
que la `ACTA 72` `72.12` guardo, y la lectura linea a linea, con las cuentas en letra buscadas aparte, esta en la seccion `7`. El
encargo de la `75` lo escribo en mi turno normal y se mide alli.

## 1. **LO QUE VI SIN BUSCARLO, Y LO DIGO ANTES DE MEDIR** (`d146`)

**La foto de `git status` que el entorno me pone delante trae los asuntos de los commits del extractor de la `74`, y traen cifras y
conclusiones de su vuelta**: `5459afe3` (*d078 pagada citando D73.5 y ACTA 72 72.5, d077 pagada ficha por ficha (las 7 de la tanda
58 barridas antes de entrar o de quedar lista, ninguna cambiada por lectura de vecino) y la vuelta declarada de saneamiento*),
`186484d2` (*la fidelidad de los tres nodos de cap_13 de Scott sin firma (70 filas, 70 citas en su linea, 1 PUENTE traido sin tocar
el grafo) y d084 y d006 pagadas a falta de la firma de la ACTA 73*) y `6312424b` (*censo 430/1081/1/7/85 al abrir y al cerrar, nada
movido; las 7 fichas de Grove con la huella de la 73; D.61 sin abiertos; R5, guardas y cierre estricto en verde; d078, d077, d084 y
d006 pagadas, ninguna insertada*). **Los lei antes de medir nada.** Es el mismo hueco de `d146` que declararon las aperturas de la
`65` a la `73`, y no lo arreglo yo (`D.45`).

**Y TRES COSAS MAS, DEL MISMO TIPO, QUE SON MIAS:** un `ls .v74ext` me enseño **los nombres** de los ficheros de su carpeta (entre
ellos `fidelidad.tsv`, `citas_fidelidad.txt`, `contar_fidelidad.txt`, `d077.txt`, `libro_mayor.txt` y un `como_<id>.txt` por cada
deuda del encargo, `d006`, `d077`, `d078` y `d084`), **no su contenido**; al buscar el texto de esas deudas en `docs/loop/DEUDA.jsonl` vi que **cada una
tiene ya una linea de pago de la vuelta `74`**, y de esas lineas imprimi solo sus claves, **no su `como`**; y la cola de
`docs/loop/loop.log`, que no se retira, con el coste y la hora del turno del extractor. Tambien lei mi `ACTA 72` entera y mi
encargo, `docs/loop/PROMPT_SIGUIENTE.md`.

**LO QUE HAGO CON ELLO:** ninguna cifra de esta pagina sale de esos asuntos; todas salen de un instrumento corrido en esta fase, y
donde coinciden lo digo como coincidencia y no como fuente. **No he abierto nada de `.v74ext/` por dentro**, **ni
`bitacora/VEREDICTOS.jsonl` por dentro**. **Y ESTO SI PESA SOBRE MI LECTURA, Y LO DIGO:** el asunto de `186484d2` me dijo *1
PUENTE* antes de leer, y mi lectura de la seccion `3` encuentra uno. Sale de su linea del libro y es el que es; **pero no puedo
probar que el asunto no me empujo a buscarlo, ni si su puente es el mio**. Eso se sabe en mi turno normal, fila a fila.

## 2. **EL ALCANCE, Y EL CENSO QUE LO SOSTIENE**

**El censo de hoy**, sin `git` (grafo, bitacora, pares mutuos; las bandejas de Grove, Gerber y Marquet, los insertados de Grove y
`procesos/`), la poblacion de la aduana y el gate:

@@RUN:0::wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl@@
@@RUN:0::for d in cuarentena/grove_high_output cuarentena/_insertados/grove_high_output cuarentena/gerber_emyth cuarentena/marquet_turn_the_ship; do echo "$d $(ls $d/*.json | wc -l)"; done; echo "procesos $(ls -A procesos/ | wc -l)"@@
@@RUN:0::python .v70aud/poblacion.py@@
@@RUN:0::python forja.py gate | head -2@@

**Lo que es mas nuevo que mi encargo**, que escribi al cerrar la `ACTA 72`, en las carpetas de dato, de codigo y de libro; y **el grafo
y las fichas de las tres bandejas contra mis huellas de la `73`**, tomadas antes de mi barrido de entonces:

@@RUN:0::ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, $7, $9}'@@
@@RUN:0::find cuarentena dataset bitacora censos config fuentes esquema src scripts tests forja.py -type f -newer docs/loop/PROMPT_SIGUIENTE.md | wc -l@@
@@RUN:0::python .v74aud/huellas_contra_73.py@@

**LECTURA:** el censo es el de mi `ACTA 72` `72.1`, y la poblacion del barrido sigue donde estaba. **Ningun fichero de las carpetas
de dato, de codigo o de libro es mas nuevo que mi encargo**, y **el grafo y todas las fichas de las tres bandejas son byte a byte los
de mi fase ciega de la `73`**: la vuelta no inserto nada y no toco la bandeja, que es lo que el encargo pedia. **Lo que no puedo
decir sin `git`**: si alguna linea de la bitacora cambio sin cambiar la cuenta ni la fecha; la bitacora no tiene huella mia de la
`73`. Eso lo mido en mi turno normal, con el hash del reporte delante.

## 3. **LA FIDELIDAD DE LOS TRES NODOS DE `cap_13` QUE NADIE HA FIRMADO** (`d084`, `d006`, `D.30`, `8`)

**Cuales son, por instrumento y no por la letra de `d084`**: el libro mayor de la `ACTA 58` `58.2.d` (`.v60aud/libro_mayor_cap13.py`)
corrido hoy, primero su linea final y despues su reparto en dos clases con su suma, contra mis filas:

@@RUN:0::python .v60aud/libro_mayor_cap13.py | tail -1@@
@@RUN:0::python .v74aud/firma_cap13.py@@

Lei **entero** `fuentes/scott_radical_candor/cap_13.md` (*Afterword to the Revised Edition: Rolling Out Radical Candor*), y cada
paso de los tres contra su linea, con los pasos delante por `pasos_ciego.py` (`.v74aud/pasos_tres.txt`):

@@RUN:0::wc -l fuentes/scott_radical_candor/cap_13.md; head -6 fuentes/scott_radical_candor/cap_13.md | tail -2@@

Una fila por paso en `.v74aud/fidelidad.tsv`: `T` transcripcion, `P` puente (**la clausula reescrita cuenta como `P`**, `ACTA 62`
`62.5`, y **la posibilidad convertida en orden tambien**, `D71.9` y `D73.3`), `D` mi duda, con su linea y la frase del libro. El
contador es copia de `.v73aud/contar_fidelidad.py` que lee los pasos **del grafo**, una fila por nodo y el total, con la suma de cada
reparto (`R7`), y **comprueba cada cita**: los tramos de la frase que copie tienen que estar en su linea del capitulo.

@@RUN:0::python .v74aud/contar_fidelidad.py@@

**Y LA COMPROBACION DE CITAS MUERDE** (`5.5`, *la guarda que no muerde es cifra*): la misma, sobre una copia de mis filas con una
palabra cambiada en una cita:

@@RUN:0::sed 's/Praise first/Praise last/' .v74aud/fidelidad_fuente.txt > .v74aud/fidelidad_mutada.txt; python .v74aud/contar_fidelidad.py .v74aud/fidelidad_mutada.txt | tail -2@@

**LECTURA: es un capitulo de inventario rico** (las secciones del epilogo *Practice: What's your story?*, *Praise* y *Gauge
criticism*), y los pasos lo transcriben casi frase a frase, muchos con su *cuenta con lo que el texto dice* delante, que es verbo de
marco y no medio nuevo. **Mi unico PUENTE:**

- **`dar_elogio_disciplina_igual_critica` paso `8`**: *Cuenta ademas con lo que el elogio consigue **y la critica no**: ayuda a la
  gente a centrarse en sus fuerzas...*, contra `L273`, *Also, praise helps people focus on their strengths and on doing more work that
  they enjoy and less of what they hate*. **El libro no compara ahi con la critica**: dice *Also*. La clausula *y la critica no* es
  del paso, la figura de la clausula anadida. **Correccion que propongo, sin tocar nada**: *Cuenta ademas con lo que el elogio
  consigue: ayuda a la gente a centrarse en sus fuerzas y a hacer mas del trabajo que disfruta y menos del que odia.* **ESTE NODO VIVE
  EN EL GRAFO: un PUENTE ahi es la guarda de fidelidad `D.30`**, y lo adjudica mi `ACTA 73` antes de que nadie mueva un dato
  (encargo de la `74`, TAREA `3`, punto `2`).

**Mis dudas, las cuatro inclinadas a `T`**, y las dejo a la vista:

- **`contar_cuatro_historias` pasos `3` y `15`**: el condicional del libro puesto de orden (*If you tell your team your story...*
  de `L45`, *When people unpack their own stories, and share them...* de `L55`). **Me inclino a `T`** porque es el condicional del
  ejercicio que `L43` abre (*Here is an exercise we do in our workshops*), no un modal de posibilidad (*perhaps*, *might*) como los de
  `D71.9` y `D73.3`, y los dos pasos conservan el *porque el texto dice*.
- **`contar_cuatro_historias` paso `8`**: *Cuenta la tuya y no la del libro*, para la historia de agresion odiosa, donde `L49` solo
  dice que la tuya es *por definicion mejor* que la del correo de los *clutter sites*; la prohibicion literal (*Don't tell Kim's Bob
  story*) es de `L51` y de la otra historia. **Me inclino a `T`**: la comparacion y la orden dicen lo mismo.
- **`medir_critica` paso `8`**: *no lo hagas desde el telefono ni desde el ordenador*, contra *You cannot do this if you are on your
  phone or on your computer* de `L297`. El *desde* puede leerse como el canal de la conversacion, y *on your phone* es estar mirando el
  telefono. **Me inclino a `T`**: es una traduccion floja, no una clausula que el libro no ponga.

**`PASOS INVENTADOS`, por el bloque de arriba**: una fila por nodo y el total de los tres, con mi `P` sola y con mis dudas caidas.
**LECTURA:** el total queda **por debajo del `10` en las dos lecturas**; **por nodo**, `contar_cuatro_historias` pasaria del `10` solo
si cayesen sus tres dudas. **Esta cifra no dimensiona ningun lote** (`8.1`): son nodos que ya viven en el grafo, y lo que mide es si
la firma que les falta se puede dar.

**LO QUE NO LEI COMO FIDELIDAD, Y LO DIGO:** las `condiciones_activacion` de los tres (no son pasos y no cuentan en la cifra), y **las
piezas del capitulo que ningun paso lleva** (por ejemplo, *Telling these stories can help you avoid repeating similar offenses* de
`L53`): son frontera y no puente, y no las reabro (`D.47`).

## 4. **`d077`: LAS FICHAS DE LA TANDA `58`, POR INSTRUMENTO** (`D.38.4`)

**Cuales son**: los nombres de `.v58ext/informe_<n>_<id>.txt`, que es lo que la cita de `d077` nombra; **donde vive cada una hoy**; su
huella contra la mia de la `73` si sigue en la bandeja; y **que carpetas de vuelta traen un barrido suyo por nombre**, con su fecha,
sin mirar dentro de `.v74ext/`:

@@RUN:0::python .v74aud/d077_ciego.py@@

**Las que ya entraron, en la lista de entrada de la `72`**, que la `ACTA 71` firmo entera, y lo que las `ACTA 70` y `71` dicen de su
barrido y de sus bytes:

@@RUN:0::grep -n -E "entregar_evaluacion_desempeno_tres_claves|preparar_resena_mixta_hoja_trabajo|guiar_subordinado_etapas_resistencia_desempeno" .v71ext/orden.txt | cut -c1-80@@
@@RUN:0::grep -n -E "^# ACTA 7[01]\. " docs/loop/ACTA_AUDITOR.md | cut -c1-420@@

**LECTURA, ficha por ficha, en dos grupos:**

- **Las tres de `cap_14` que ya viven en el grafo** (`entregar_evaluacion`, `preparar_resena` y `guiar_subordinado`) **se barrieron
  sobre grafo mas bandejas en la vuelta `71`**, por el extractor y por mi fase ciega, que la `ACTA 70` firmo (*su barrido es el mio
  fila a fila*), y **entraron en la `72` desde `.v71ext/orden.txt`** *con los bytes que se leyeron* (`ACTA 71`). **Es la relectura
  contra la cola de su dia que `d077` pedia**, hecha antes de entrar.
- **Las cuatro que siguen en la bandeja** (`usar_banco`, `responder_primer_aviso`, `gestionar_retencion` y `reciclar_empleado`) **se
  barrieron en la `73`**, por el extractor y por mi fase ciega, que la `ACTA 72` `72.3` firmo (*identica fila a fila*), y **hoy son
  byte a byte las que yo barri** (bloque de arriba y seccion `2`). **Es la relectura de su dia para la vuelta que las inserte**,
  siempre que la bandeja siga sin moverse hasta entonces.

**MI CLASE PARA `d077`: SE PUEDE PAGAR**, con una condicion que ya es la de `d031`: que las cuatro de la bandeja entren con la huella
de la `73`. **LO QUE NO PUEDO DECIR EN ESTA FASE, Y ES LO QUE `d077` PREGUNTA AL FINAL:** *si alguna lectura de vecino le cambio el
texto* a alguna de las siete entre la tanda `58` y su barrido de entrada. Lo unico que se sin `git` es que **las cuatro correcciones
de la `73`** (`ACTA 72` `72.1`: `usar_banco`, `responder_primer_aviso`, `gestionar_retencion` y `pedir_critica_anonima`) **fueron de
fidelidad, no de vecino**, y que `pedir_critica_anonima` no es de la tanda `58`. **Lo que cambio cada ficha y por que, commit a
commit, lo mido en mi turno normal**, y ahi cruzo su fila por ficha contra la mia.

## 5. **`d078`: LOS DOS PASOS, CON LA LINEA DELANTE**

@@RUN:0::python .v67aud/normal/pasos_ciego.py responder_primer_aviso_renuncia_subordinado | grep -E "^=====|  P(3|5)\. "@@
@@RUN:0::sed -n 111p fuentes/grove_high_output/cap_15.md | grep -o -E "don.t argue about anything with him|Don.t argue, don.t lecture, and don.t panic"@@

**LECTURA:** los dos pasos siguen en la ficha, y `L111` dice el *no discutas* dos veces. **`d078` ya esta decidido**: el `D73.5` del
extractor los dejo los dos, y mi `ACTA 72` `72.5` lo sostuvo porque el `5` trae *no sermonees* y *no entres en panico*, que el `3` no
trae. **Mi clase: SE PAGA citando esas dos secciones, y la ficha no se toca**, que es lo que la huella de la seccion `2` dice que
paso.

## 6. **LAS FICHAS DE GROVE: MI LECTURA SELLADA DE LA `73` SIGUE EN PIE** (`D.38.4`, `D.38.5`)

**No hay candidato nuevo ni ficha cambiada** (seccion `2`: el grafo y las tres bandejas byte a byte los de mis huellas de la `73`,
tomadas antes de mi barrido; la poblacion, la misma). **Mi fidelidad, mi barrido, mis clases, mis aristas y mi orden de la `73`**,
cruzados y adjudicados en la `ACTA 72`, **se leyeron sobre estos mismos bytes y esta misma poblacion**, asi que **no los rehago**:
rehacer un barrido sobre la misma entrada solo mediria el reloj. **Si la vuelta de insercion encuentra la bandeja o el grafo movidos**,
esa lectura deja de valer y se rehace entera (`d031`).

## 7. **`R8` MEDIDO SOBRE MI ENCARGO DE LA `74`, CON EL MISMO INSTRUMENTO** (`ACTA 72` `72.11`)

`R8` dice: *toda cifra de medida que escriba en `PROMPT_SIGUIENTE.md` (un reloj, una banda, una cuenta que solo se comprueba abriendo un
fichero, en digito o en letra) va DENTRO de un bloque `$` con su salida, o lleva EN SU MISMA LINEA la seccion del acta donde esta
pegada*. Que el fichero es el encargo que escribi al cerrar la `ACTA 72`, y el instrumento de la `72.12` corrido sin copiarlo, con su
salida de hoy contra la que guardo aquella acta:

@@RUN:0::head -1 docs/loop/PROMPT_SIGUIENTE.md | cut -c1-100; ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, $7, $9}'@@
@@RUN:0::python .v73aud/normal/r8_encargo74.py | diff - .v73aud/normal/r8_encargo74.txt && echo "IDENTICO a .v73aud/normal/r8_encargo74.txt, la salida de la ACTA 72 72.12"; python .v73aud/normal/r8_encargo74.py | tail -1@@

Las lineas de prosa con numero y **sin** seccion, cada una con los numeros que el instrumento le ve:

@@RUN:0::python .v73aud/normal/r8_encargo74.py | grep -E "^  L[0-9]+ - " | sed -E 's/\] \|.*$/]/'@@

**LECTURA, grupo a grupo, que es mia y no del instrumento; las volvi a leer una a una y no copio la de la `72.12`:**

- **Numeros de vuelta, de acta, de rama o de carpeta de la casa**: `L1`, `L3`, `L47`, `L69`, `L70`, `L75`, `L76`, `L88`, `L89`,
  `L92`, `L99`, `L101`, `L102`, `L104`, `L105`, `L108`.
- **Secciones, reglas, deudas y numeros de tarea o de punto**: `L4`, `L14`, `L20`, `L22`, `L28`, `L49`, `L59`, `L64`, `L65`, `L72`,
  `L74`, `L83`, `L86`, `L90`, `L94`, `L97`, `L103`, `L117`, y los de tarea y punto de `L61` y `L69`.
- **Identificadores de capitulo, de paso o de tanda**: `cap_13` en `L1`, `L72`, `L74` y `L90`; `cap_18` en `L28`; los pasos `3` y `5`
  de `d078` en `L61`; la tanda `58` en `L64`.
- **Las cifras de medida** estan dentro de un bloque `$` (la clase, el tablero, las deudas, los pasos de los nodos de `d084`), o
  llevan su seccion de la `ACTA 72` en la misma linea (las lineas con `S` del instrumento).

**LAS CUENTAS EN LETRA**, que el instrumento ve por palabra y que busco tambien con un `grep` mas ancho:

@@RUN:0::grep -n -i -w -E "uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|veinte|treinta|cero|mil|cien|ambas|ambos" docs/loop/PROMPT_SIGUIENTE.md | cut -c1-120@@

**LECTURA, linea a linea:** `L39` esta **dentro de un bloque `$`** (es el texto de `d077` que imprime `deuda.py`); `L55` (*diez
discutibles*) y `L62` (*los dos*, los dos pasos que la misma linea nombra) llevan `72.5` **en la misma linea**; `L91` (*uno por uno*)
es **una manera**, no una cuenta; `L123` (*cero guiones*) es **la meta de la frase fija de cierre**. **Ninguna linea de prosa trae una
cifra de medida sin su bloque o su seccion en la misma linea: `R8` CUMPLIDO en el encargo de la `74`.**

## 8. **LO QUE DEJO PARA MI TURNO NORMAL, ESCRITO ANTES DE VER EL REPORTE**

1. **`R5`** en su reporte, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` sacados otra vez de los originales y con la
   cabecera cambiada a la `74`.
2. **El censo con su hash**: que la vuelta no movio el grafo, la bitacora, los censos ni ninguna bandeja, **con `git diff`**, que es
   lo que en esta fase no he medido (la bitacora sobre todo, que no tiene huella mia).
3. **Mi fidelidad de los tres nodos de `d084` contra la suya, fila a fila**: mis filas (seccion `3`) contra las suyas. **Si su
   PUENTE es otro que el mio, o si marca `P` un paso que yo lei `T` sin duda y gana, la caida de lectura es mia.** Y **el PUENTE que
   quede se adjudica en el acta como guarda `D.30`**, con su correccion encargada, **sin que nadie toque el grafo antes**.
4. **La firma de `d084` y `d006`**: si su fichero cubre, uno por uno, los pasos sin firma del libro mayor (seccion `3`), **firmo**; si
   no, el pago se corrige por correccion declarada.
5. **`d077` fila a fila**: su tabla por ficha contra la mia (seccion `4`), y **con `git log` sobre cada ficha, si alguna lectura de
   vecino le cambio el texto** entre la tanda `58` y su barrido de entrada.
6. **`d078`**: que lo pago citando `D73.5` y la `72.5`, y que la ficha no cambio (seccion `5`).
7. **La huella de las fichas de Grove** que su cierre dice conservar, contra las mias de `.v73aud/huellas_al_barrer.txt` (seccion
   `2`).
8. **La muestra pineada de los SANO**: esta vuelta no escribe en la bitacora; no hay poblacion.
9. **`R8` sobre el encargo de la `75`**, medido antes de cerrarlo, con las cuentas en letra incluidas.

## 9. **ESTA PAGINA CONTRA `R6`, `R7` Y LOS GUIONES, MEDIDA SOBRE ELLA MISMA**

El generador corre dos veces, y estos bloques de la segunda pasada leen la pagina que escribio la primera, identica salvo estos
bloques. El primero cuenta las lineas de bloque `$` que empiezan por una clave de relacion; el segundo, con la copia de
`.v73aud/r7_pagina.py`, cuenta las lineas de bloque que reparten una cifra en clases y cuantas traen su `suma`; el tercero cuenta
guiones largos y medios:

@@RUN:0::grep -c -E "^    +(previos|siguientes|nodos_previos|nodos_siguientes)" docs/loop/APERTURA_CIEGA.md@@
@@RUN:0::python .v74aud/r7_pagina.py@@
@@RUN:0::grep -c -P "\x{2014}|\x{2013}" docs/loop/APERTURA_CIEGA.md@@
