# APERTURA CIEGA DE LA VUELTA 76, lote 9 (`gerber_emyth`), **CLASE INSERCION, VUELTA DE PREPARACION**

*Auditor `claude-opus-5-5`, fase ciega, 26 sep 2026. En la corrida que arranco el 26 a las `06:45`, el arnes la numera `VUELTA 1`.
Linea **serial**, rama `extraccion-mundo-11`. Modo austero (`D.47`). Todo lo de esta pagina sale de `.v76aud/`, escrito y
corrido en esta fase; cada bloque `$` lo pega `.v76aud/generar_apertura.py` corriendo el comando en el momento de escribirla.
**No hay ninguna tabla en esta pagina**, a proposito, como en la `73` y la `75`.*

**LO QUE ESTA VUELTA TENIA QUE HACER, Y LO QUE CLASIFICO A CIEGAS** (mi encargo, `docs/loop/PROMPT_SIGUIENTE.md`): **dejar listas sin
insertar ninguna las `22` fichas de la bandeja de Gerber**: su fidelidad leida entera, su barrido, sus veredictos, sus aristas por
lectura con `d111`, `d108` y `d098` delante, y su orden. **Yo hago lo mismo por mi cuenta**: leo los diez capitulos enteros y cada
paso contra su linea (seccion `3`), barro las `22` sobre grafo mas bandejas (seccion `4`), escribo mis clases y mis aristas (secciones
`5` y `6`) y las restricciones de orden que mi lectura pone (seccion `7`).

**UNA LIMITACION DE METODO, DICHA ANTES DE NADA: EN ESTA FASE NO HE CORRIDO `git` SOBRE EL REPOSITORIO**, ni una vez, como en la
`73` y la `75`: la carpeta de una linea viva es solo del arnes (`PARALELO.md` `7`). **Lo que se mide con `git` aqui no lo mido**: que
commit movio que y a que hora, y el contenido viejo de un fichero que cambio. Lo que si mido sin `git` es que ficheros son mas nuevos
que mi encargo y que fichas cambiaron contra mis propias huellas de la `73` (seccion `2`). El commit en que esta el arbol lo leo de
los ficheros de `.git/`:

@@RUN:0::cat .git/HEAD; cat .git/refs/heads/extraccion-mundo-11@@

## 0. **LA HERENCIA** (`D.40`)

ACTA ANTERIOR LEIDA: 259ed9a152ac06afded98d8ab7a57ada89b0d817

**Comprobada sin git**: es el blob de `docs/loop/ACTA_AUDITOR.md` tal como esta hoy en el arbol, calculado como lo calcula git. **La
`ACTA 74` la lei entera**, de su linea de cabecera a la ultima del fichero, y con ella el encargo que me deje:

@@RUN:0::python .v76aud/huella_acta.py@@

HEREDADO 1: NO APLICA en esta fase. **Motivo:** `R5` es un remedio **del extractor** y se mide **sobre su reporte de la `76`**
(`ACTA 74` `74.11`: *el reporte de la `76`, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera cambiada a
la `76`*), y el reporte **no esta en el arbol**: el arnes lo retiro para esta fase (`D.34.2`) y no lo he recuperado por ninguna via.
**Se mide en mi turno normal**, con los dos instrumentos sacados otra vez de los originales y no de las copias del extractor. Lo que
si esta en mi mano lo cumplo en mi pagina: cada bloque `$` lleva la salida del comando que abre, y nada mas.

@@RUN:0::ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl@@
@@RUN:0::grep -n "VUELTA 1 : APERTURA CIEGA" docs/loop/loop.log | tail -1@@

HEREDADO 2: CUMPLIDO. **`R6`, mio** (`ACTA 74` `74.11`): en esta fase los pasos de cualquier nodo los imprime
`.v67aud/normal/pasos_ciego.py`, que no ensenia `previos` ni `siguientes`: con el lei las `22` fichas (`.v76aud/pasos_22.txt`) y los
nodos de fuera que el barrido levanta (`.v76aud/pasos_fuera.txt`), y los bloques de pasos de esta pagina los corre el (seccion `5`).
Las lineas de esos ficheros que **empiezan** por una clave de relacion, y los instrumentos mios de esta fase que las **nombran**:

@@RUN:0::grep -c -E "^ *(previos|siguientes|nodos_previos|nodos_siguientes)" .v76aud/pasos_22.txt .v76aud/pasos_fuera.txt@@
@@RUN:0::grep -l -E "previos|siguientes" .v76aud/*.py | wc -l@@

**LO UNICO QUE SE ACERCA, para que se juzgue:** `pasos_22.txt` trae dos lineas con la palabra *siguientes* dentro de un paso
(*las siguientes actividades*, *las tres semanas siguientes*), que son texto del libro y no claves; y `.v76aud/correcciones.py`
(seccion `3`) imprime los tramos *CORRECCION DECLARADA* del `resumen_teorico`, prosa del extractor sobre pasos y citas. **No vi
ninguna clave de relacion con su valor de ningun nodo en esta fase.** La pagina entera la mide un `grep` sobre ella al cerrarla
(seccion `10`).

HEREDADO 3: CUMPLIDO. **`R7`, mio** (`ACTA 74` `74.11`): toda linea de esta pagina que reparte un total en clases la imprime un
instrumento que cuenta **todas** las clases con el mismo predicado y **dice su `suma`**: los de `.v76aud/` la traen, copiados de los
de la `73` o escritos en esta fase con ella, y los que reuso sin copiar (`.v70aud/poblacion.py`, `.v75aud/normal/bandeja_gerber.py` y
el de `R8`) ya la traian. **Medido sobre la pagina misma** en la seccion `10`, con la copia de `.v73aud/r7_pagina.py`.

HEREDADO 4: CUMPLIDO. **`R8`, mio** (`ACTA 74` `74.11`, *mi fase ciega de la `76`, sobre el encargo de la `76`*): **lo mido aqui con
el mismo instrumento de la `74.12`, sin copiarlo**, y su salida de hoy es identica a la que aquella acta guardo; la lectura, linea a
linea, en la seccion `8`. El encargo de la `77` lo escribo en mi turno normal y se mide alli.

HEREDADO 5: NO APLICA en esta fase. **Motivo:** `R9` es un remedio **del extractor** y se comprueba **en el reporte de la `76`, en
cada fila de fidelidad y en cada cuenta de PUENTE** (`ACTA 74` `74.11`), que el arnes retiro (bloque del HEREDADO `1`). **Lo que si
esta en mi mano**, y lo cumplo en mi lectura: **cada una de mis `176` filas trae su tramo literal del libro, y el instrumento
comprueba que ese tramo esta en la linea que cito** (seccion `3`); el cruce de su patron con el mio, en mi turno normal.

@@RUN:0::python .v76aud/contar_fidelidad.py | tail -1@@

HEREDADO 6: CUMPLIDO. **`R10`, mio, NUEVO en la `ACTA 74`** (`74.9` y `74.11`): toda salida pegada en `PROMPT_SIGUIENTE.md` se corre
despues de la ultima escritura del auditor en el registro que mide, o se vuelve a correr antes del commit y se compara. **Lo mido
sobre el encargo de la `76` por los dos caminos**: el registro que mide la clase, `DEUDA.jsonl`, es de antes que el encargo, y las
dos salidas pegadas (la clase y el tablero) **salen hoy identicas a lo pegado**, con la comparacion que la `74.13` guardo en
`.v75aud/normal/r10.txt` delante. El `TABLERO.jsonl` es de despues, y no es escritura mia: es la del arnes al arrancar esta corrida
(seccion `1`). **La otra mitad de su sitio, la `ACTA 75`, es de mi turno normal.**

@@RUN:0::ls -l --time-style=full-iso docs/loop/DEUDA.jsonl docs/loop/PROMPT_SIGUIENTE.md .v75aud/normal/r10.txt docs/loop/TABLERO.jsonl | awk '{print $6, substr($7,1,8), $9}'@@
@@RUN:0::python scripts/deuda.py --clase 76 | diff --strip-trailing-cr - <(sed -n "39,40p" docs/loop/PROMPT_SIGUIENTE.md | sed "s/^    //") && echo "clase: IDENTICA a la pegada en el encargo de la 76"@@
@@RUN:0::python forja.py tablero --puedo gerber_emyth | diff --strip-trailing-cr - <(sed -n "42,43p" docs/loop/PROMPT_SIGUIENTE.md | sed "s/^    //") && echo "tablero --puedo: IDENTICO al pegado en el encargo de la 76"@@

## 1. **LO QUE VI SIN BUSCARLO, Y LO DIGO ANTES DE MEDIR** (`d146`)

**La foto de `git status` que el entorno me pone delante trae los asuntos de los commits del extractor, y tres son cifras de su
vuelta**: `b0dda029` (*la fidelidad entera de las 22 fichas de Gerber (176 pasos, 9 PUENTE corregidos en la bandeja por correccion
declarada antes del barrido, cap_07 y cap_12 releidos enteros por D.58)*), `a0d42852` (*el barrido de las 22 de Gerber (22 de 22, 54
pares, recogido dentro del turno), sus 54 veredictos listos, 6 aristas por lectura con d111, d108 y d098 leidas, y el orden con D.36
en cero*) y `dfca777d` (*el cierre (censo igual al abrir y al cerrar, 22 fichas de Gerber preparadas y ninguna insertada, huellas,
D.61 sin discutible abierto, R5, gate, guiones, 382 pruebas y cierre estricto en verde)*). **Los lei antes de medir nada.** Es el
mismo hueco de `d146` que declararon las aperturas de la `65` a la `75`, y no lo arreglo yo (`D.45`).

**Y LO DEMAS DEL MISMO TIPO:** la cola de `docs/loop/loop.log`, que no se retira (el coste y la hora del turno del extractor, y la
parada de las `06:37` por la guarda del tablero con el relanzamiento de las `06:45`); mi `ACTA 74` entera y mi encargo; el texto de
`d098`, `d108` y `d111` en `docs/loop/DEUDA.jsonl`, que mi encargo manda leer; un `ls .v76ext`, que me enseño **los nombres** de su
carpeta (entre ellos `fidelidad.tsv`, `veredictos_listos.txt`, `aristas_lectura.txt`, `orden.txt` y un `vecinos_<id>.json` por
ficha), **no su contenido**; y **seis fichas de la bandeja llevan dentro, en su `resumen_teorico`, la lectura del propio extractor**
(la *CORRECCION DECLARADA DE LA VUELTA 76* con el texto viejo dentro). **Esas correcciones las lei DESPUES de escribir y contar mi
fidelidad paso a paso**: para leer las lineas que cada ficha cita sin leer su prosa, `.v76aud/citas_ficha.py` imprime solo los
`cap_NN` y los `LNN` que el resumen nombra antes de la primera correccion, y cuantas correcciones trae; lo que dicen, en la seccion
`3`, separado.

**LO QUE HAGO CON ELLO:** ninguna cifra de esta pagina sale de esos asuntos; todas salen de un instrumento corrido en esta fase, y
donde coinciden lo digo como coincidencia y no como fuente. **No he abierto nada de `.v76ext/` por dentro**, **ni
`bitacora/VEREDICTOS.jsonl` por dentro**: de ella solo cuento lineas. **Y ESTO SI PESA SOBRE MI LECTURA, Y LO DIGO:** el asunto de
`a0d42852` me dijo *54 pares* y *6 aristas por lectura* antes de barrer y de leer. Mis pares salen de mi barrido y mis aristas de la
seccion `6` con su linea del libro, y son las que son; **pero no puedo probar que no me empujaron**, y por eso lo escribo aqui.

## 2. **EL ALCANCE, Y EL CENSO QUE LO SOSTIENE**

Mi lista es la bandeja entera, leida del directorio, y su reparto por capitulo y por pasos lo da el instrumento de la `ACTA 74`
`74.10`, corrido hoy sin copiarlo:

@@RUN:0::wc -l < .v76aud/las22.txt; ls cuarentena/gerber_emyth | grep "\.json$" | sed 's/\.json$//' | diff - .v76aud/las22.txt && echo "las22.txt es la bandeja de Gerber entera, fichero a fichero"@@
@@RUN:0::python .v75aud/normal/bandeja_gerber.py | diff - .v75aud/normal/bandeja_gerber.txt && echo "bandeja_gerber.py de hoy: IDENTICO a su salida de la ACTA 74 74.10"; tail -2 .v75aud/normal/bandeja_gerber.txt@@

**El censo de hoy**, sin `git` (grafo, bitacora, pares mutuos; la bandeja de Gerber y sus insertados, la de Grove y sus insertados,
la de Marquet y `procesos/`), la poblacion de la aduana y el `gate`:

@@RUN:0::wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl@@
@@RUN:0::for d in cuarentena/gerber_emyth cuarentena/_insertados/gerber_emyth cuarentena/grove_high_output cuarentena/_insertados/grove_high_output cuarentena/marquet_turn_the_ship; do echo "$d $(find $d -maxdepth 1 -name '*.json' 2>/dev/null | wc -l)"; done; echo "procesos $(ls -A procesos/ | wc -l)"@@
@@RUN:0::python .v70aud/poblacion.py@@
@@RUN:0::python forja.py gate | head -2@@

**Lo que es mas nuevo que mi encargo** en las carpetas de dato, de codigo y de libro; la hora de cada cosa; y **las fichas de Gerber y
de Marquet contra mis huellas de la `73`**, tomadas antes de mi barrido de entonces:

@@RUN:0::find cuarentena dataset bitacora censos config fuentes esquema src scripts tests forja.py -type f -newer docs/loop/PROMPT_SIGUIENTE.md | sed 's|/[^/]*\.json$|/*.json|' | sort | uniq -c@@
@@RUN:0::ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md src/tablero.py tests/test_aceptacion.py | awk '{print $6, substr($7,1,8), $9}'; ls -l --time-style=full-iso cuarentena/gerber_emyth/*.json | awk '{print $6, substr($7,1,8)}' | sort | sed -n '$p'@@
@@RUN:0::grep -n -E "DETENIDO en la vuelta 5|^\[2026-09-26 06:45:19\] arranque|VUELTA 1 : EXTRACTOR" docs/loop/loop.log | tail -3@@
@@RUN:0::python .v76aud/huellas_contra_73.py@@

**LECTURA:**

1. `437`, `1111`, `1`, `92` en los insertados de Grove y `0` en su bandeja son los de mi `ACTA 74` `74.1` al cerrar la `75`; Gerber
   sigue en `22` y sin insertados, y Marquet en `20`: **la vuelta no inserto nada ni movio nada de sede**, que es lo que el encargo
   pedia, y `procesos/` esta vacio. La poblacion del barrido sigue en `479`.
2. **Lo unico de dato mas nuevo que mi encargo son `6` fichas de Gerber, y son las `6` cuyas huellas cambiaron contra las mias de la
   `73`**; las otras `16` de Gerber y las `20` de Marquet son byte a byte las de entonces. La ultima ficha se escribio a las `07:05:30`.
3. **Y DOS FICHEROS DE CODIGO, QUE MI ENCARGO PROHIBIA TOCAR**: `src/tablero.py` y `tests/test_aceptacion.py`, los dos a las
   `06:45:09`. **No los toco el extractor, por la hora**: el arnes paro a las `06:37:07` porque la guarda del tablero no dejaba abrir
   la vuelta con Gerber, se relanzo a las `06:45:19` y el extractor arranco a las `06:45:20`. **Lo que dicen ellos mismos**: el
   comentario nuevo de `src/tablero.py` (*UN COSECHADO QUE YA ENTRO ENTERO ES INSERTADO (26 sep 2026)*) y el test nuevo (*LA VUELTA 76
   NO ABRIO (26 sep 2026, 06:37)*) son el remedio de esa parada, que es lo que `d180` anoto en la `ACTA 73`. **Quien lo escribio no lo
   se sin `git`**: lo mido en mi turno normal, y si es del fundador no es de nadie de esta linea (`D.45`). **Lo que si mido**: el
   asunto de `dfca777d` dice *382 pruebas* y mi `ACTA 74` `74.1` conto `379`; la suite la corro en mi turno normal.
4. **Lo que no puedo decir sin `git`**: si alguna linea de la bitacora o algun byte del grafo cambio sin cambiar la cuenta ni la
   fecha. Eso lo mido en mi turno normal, con el hash del reporte delante.

## 3. **LA FIDELIDAD DE LAS `22`, LEIDA ENTERA** (`D.30`, `D.58`, `8`)

Lei **enteros** los diez capitulos que las `22` citan en su `UNIDAD DE ORIGEN` (`cap_04`, `cap_07`, `cap_08`, `cap_11`, `cap_12`,
`cap_13`, `cap_14`, `cap_15`, `cap_18` y `cap_19`), y cada paso contra su linea, con los pasos delante por `pasos_ciego.py`
(`.v76aud/pasos_22.txt`). Para `d098` lei ademas la apertura de `cap_05`. Las citas que cada ficha nombra, sin su prosa:

@@RUN:0::wc -l fuentes/gerber_emyth/cap_{04,07,08,11,12,13,14,15,18,19}.md | tail -1@@
@@RUN:0::python .v76aud/citas_ficha.py@@

Una fila por paso en `.v76aud/fidelidad.tsv`: `T` transcripcion, `P` puente (**la clausula reescrita cuenta como `P`**, `ACTA 62`
`62.5`), `D` mi duda, con su capitulo, su linea y **el tramo literal del libro**. El contador es copia de `.v73aud/contar_fidelidad.py`
con las rutas cambiadas, **una fila por capitulo** (`8.2`) y la suma de cada reparto (`R7`); cruza cada fila con los pasos de la
ficha de la bandeja de hoy, **y comprueba que el tramo que copio esta en la linea que cito**:

@@RUN:0::python .v76aud/contar_fidelidad.py@@

**LECTURA: los diez capitulos son de inventario rico donde hay fichas**: las seis reglas numeradas de `cap_11` (L45 a L55) y su
recorrido regla a regla, las listas numeradas de `cap_12` (L95), `cap_13` (L45 a L57), `cap_18` (L143 a L165 y L249 a L271) y
`cap_19` (L143 a L153 y L311 a L335), y las listas de preguntas de `cap_07` (L281), `cap_14` (L119 a L133) y `cap_15` (L171 a L177).
**Los pasos de hoy los transcriben casi frase a frase. No encuentro ningun PUENTE en el texto de hoy de las fichas.** Las figuras
que mire y dejo en `T`, para que se juzguen:

- `operar_modelo_gente_destreza_minima` paso `10`: *Comprueba que no estas prefiriendo gente muy cualificada...* donde L111 y L113
  **describen** el error del dueño tipico. Es **el aviso vuelto mandato** con el contenido del libro, la figura que la `ACTA 70`
  `70.4` adjudico `T`.
- `fingir_prototipo_cinco_mil_replicas` paso `4` (*que son seis*) y `recorrer_siete_pasos_programa_desarrollo_negocio` paso `3`
  (*en este orden*): la cuenta y el orden son los de la lista numerada del libro, no una clausula.
- `cambiar_saludo_cliente_dos_ramas` paso `4`: *sin el programa listo, ninguna de las dos respuestas tiene de que hablar* dice con
  otras palabras el *to talk about* de L57.

**MI UNICA DUDA, y me inclino a `T`:** `cuantificar_impacto_innovacion_6_pasos` paso `4`, *Cuenta cuantas personas compraron algo,
despues del cambio*: el `(4)` de L95 no dice *despues*; lo dice el `(3)`. **Es la figura de la serie leida de corrido.**

**`PASOS INVENTADOS` por mi instrumento, sobre el texto de hoy: `0` en los diez capitulos**; si mi duda cayese, `cap_12` `1` de `12`
(`8,33`). **Por debajo del `10` en las dos lecturas.** Es preparacion y no entrada.

**Y LO QUE LEI DESPUES, EN LAS FICHAS:** seis de las `22` traen en su `resumen_teorico` una *CORRECCION DECLARADA DE LA VUELTA 76*
con el texto viejo dentro, y son las `6` cuyas huellas cambiaron (seccion `2`). Cuantos PUENTE dice cada una sobre su texto viejo, y
que pasos o campos nombra, leido de su propia prosa:

@@RUN:0::python .v76aud/puentes_declarados.py@@

**Leo sus textos viejos y los clasifico yo, pasos citados por la propia correccion** (`.v76aud/correcciones.py`):

- `aplicar_ocho_reglas_juego_personas` paso `8` (*no la repitas mas de una vez cada seis meses*, contra el *maybe once every six
  months* de L163): **`P`**, vuelve tope firme lo que el libro da con un *maybe*. Paso `9` (*antes de jugarlo con tu gente*, L165):
  **`P`**, el libro da la razon y no el momento.
- `cambiar_saludo_cliente_dos_ramas` pasos `1`, `2` y `3` (*pregunta exactamente*, *dile exactamente*, contra el *try* de L51 y el
  *you can say* de L53 y L55): **`P` los tres**. La regla de decirlo cada vez es de la Orquestacion (L161), **despues** de probar y
  cuantificar, no de esta pieza.
- `cuantificar_impacto_innovacion_6_pasos` paso `6` (*comparando los numeros de antes con los de despues*): **lo habria leido `D`,
  inclinado a `T`**: comparar antes y despues es como la serie de L95 llega a *the improvement*. **Su lectura `P` es mas estricta que
  la mia y la correccion es mas fiel que el texto viejo**, asi que no hay nada que corregir en lo que queda. **PERO ME DEJA UNA
  PREGUNTA QUE LLEVO AL TURNO NORMAL:** su paso `4` conserva *despues del cambio*, que es **la misma figura** (la serie leida de
  corrido, seccion de arriba) y **es mi unica duda**. Si su vara retira el *comparando* del `6`, **por la misma vara el *despues del
  cambio* del `4` es `P`** y quedo en la bandeja.
- `dictar_ritmo_crecimiento_preguntas_escritas` paso `8` (*No te pares por no tener un plan bueno*, contra el *Remember, Sarah, any
  plan is better than no plan* de L287): **`P`**.
- `operar_modelo_gente_destreza_minima` paso `4` (*No contrates a los brillantes*, contra el *you don't need to hire* de L89):
  **`P`**, vuelve prohibicion lo que el libro da como innecesario.
- `interrogar_negocio_cinco_preguntas`: corrige el entregable y ningun paso; no cuenta en pasos.

**LECTURA:** sobre el texto viejo, **mi lectura da `7` `P` seguros y `1` `D`** en los ocho pasos que las correcciones nombran:
`cap_12` `3` o `4` de `12`, `cap_07` `1` de `8`, `cap_18` `2` de `26` y `cap_11` `1` de `57`. **`cap_12` y `cap_07` pasan del `10`
en las dos lecturas, y por eso se releen enteros antes de seguir** (`D.58`); **coincide con el *cap_07 y cap_12 releidos enteros*
del asunto de `b0dda029`**, y lo digo como coincidencia. **Lo que no coincide, y lo llevo a mi turno normal:** las fichas declaran
**`8`** PUENTE en pasos (bloque de arriba) y el asunto de `b0dda029` dice **`9`** PUENTE corregidos. Puede ser un campo que no es
paso contado como puente (hay dos entregables y una condicion corregidos), o un paso mas; **no lo decido sin su reporte**. **Los ocho
pasos corregidos los lei yo `T` en su texto de hoy**: las correcciones se sostienen. **Lo que no puedo decir** es si mi lectura ciega
habria cazado esos puentes, porque cuando lei ya no estaban.

## 4. **MI BARRIDO DE LAS `22`, SOBRE GRAFO MAS BANDEJAS** (`D.38.4`, `D.38.5`)

Copia de `.v73aud/barrido_uno.py` (la ficha normalizada como la aduana, contra `dataset/nodos.jsonl` mas
`aduana.poblacion_de_bandejas`, con `buscar_vecinos` de `src/aduana.py`) y de `.v73aud/barrer.sh` con la lista cambiada a
`.v76aud/las22.txt`, **cinco a la vez, recogido entero dentro de este turno**, lanzado **despues** de que las fichas cambiasen por
ultima vez (seccion `2`: la ultima es de las `07:05:30`). Antes de lanzarlo guarde la huella de cada ficha de las bandejas de Gerber
y de Marquet y del grafo, y al recogerlo las comprobe:

@@RUN:0::head -1 .v76aud/barrido.log; tail -1 .v76aud/barrido.log; grep -c "rc=0" .v76aud/barrido.log; grep -c "rc=" .v76aud/barrido.log@@
@@RUN:0::wc -l < .v76aud/huellas_al_barrer.txt; sha1sum -c --quiet .v76aud/huellas_al_barrer.txt && echo "las 42 fichas de las dos bandejas y el grafo: mismas huellas que al barrer"@@

**Poblacion y vecinos por candidato, cada fila de vecino con su senial, y los pares sin orden:**

@@RUN:0::python .v76aud/vecinos_tabla.py | tee .v76aud/vecinos_tabla.txt@@

**LECTURA:**

1. **Las `22` dan `54` filas de vecino en `34` pares sin orden**, `24` entre dos de la tanda y `10` con uno de fuera, todos del
   grafo. **Coincide con los *54 pares* del asunto de `a0d42852`**, que ahi llama *pares* a mis filas dirigidas, como en la `73`; y lo
   digo como coincidencia.
2. **Dos fichas no levantan a nadie**: `aplicar_ocho_reglas_juego_personas` (tampoco la levanta nadie) y
   `fingir_prototipo_cinco_mil_replicas` (solo la levanta la contratacion). **Por eso las cuatro partes de la serie de las seis reglas
   quedan sin par**, y su arista es por lectura (seccion `6`).
3. **Los de fuera son todos del grafo**: de Grove, `responder_primer_aviso_renuncia_subordinado` (levantada por cuatro de las `22`),
   `entregar_evaluacion_desempeno_tres_claves`, `pedir_critica_anonima_curso_entrenamiento_dictado` y
   `planificar_tres_pasos_demanda_estado_brecha`; de Scott, `recorrer_trece_elementos_proceso_evaluacion_formal` y
   `descubrir_motivacion_sentido_persona`. **Ninguno de la bandeja de Marquet.** El mas cercano por lectura es
   `planificar_tres_pasos_demanda_estado_brecha` con `dictar_ritmo_crecimiento_preguntas_escritas` (seccion `5`).
4. **`D.36`, lo que un solo lado levanta dentro de la tanda**: va a la seccion `7`, y no obliga.

**EL RELOJ, medido y no techo:** de punta a punta en el log de arriba, con fichas de estos segundos (la menor y la mayor):

@@RUN:0::grep "rc=" .v76aud/barrido.log | sed 's/.*segundos=//' | sort -n | sed -n '1p;$p'@@

## 5. **MI LECTURA CIEGA DE LOS PARES** (`1.2`, `6.1`, y solo la vara `6.1`)

**Leidos con los pasos de los dos delante**, todos con `pasos_ciego.py` (`R6`): `.v76aud/pasos_22.txt` para las `22` y
`.v76aud/pasos_fuera.txt` para los seis de fuera. **Una fila por par** en `.v76aud/mis_clases.tsv`, con su razon. **De donde sale cada
fila:** los `25` pares posibles dentro de un mismo capitulo los escribi **todos antes de que el barrido terminara** (con `4` de `22`
recogidas), en `.v76aud/clases_intra.txt`; los de entre capitulos y los de fuera, al recogerlo, en `.v76aud/clases_fuera.txt`.
**Cuando escribi cada fichero, contra cuando cerro cada ficha del barrido** (las seis primeras):

@@RUN:0::ls -l --time-style=full-iso .v76aud/clases_intra.txt .v76aud/aristas_lectura.tsv .v76aud/clases_fuera.txt | awk '{print $6, substr($7,1,8), $9}'; ls -l --time-style=full-iso .v76aud/vecinos_*.json | awk '{print substr($7,1,8)}' | sort | head -6@@

`armar_clases.py` los junta, y el cruce comprueba que cada par del barrido tiene su fila y cada fila su par:

@@RUN:0::python .v76aud/armar_clases.py@@
@@RUN:0::python .v76aud/cruce_clases.py@@

**El par de fuera mas cercano**, con los pasos de los dos delante:

@@RUN:0::python .v67aud/normal/pasos_ciego.py dictar_ritmo_crecimiento_preguntas_escritas planificar_tres_pasos_demanda_estado_brecha@@

**LECTURA, los cuatro `CONTINUA`**, y en los cuatro el hijo trae procedimiento propio y ningun paso del otro, asi que ninguno es
`REPITE`:

- `aplicar_seis_pasos_sistema_venta` madre de `medir_sistema_venta_trece_indicadores_benchmark`: la condicion del hijo es el sistema
  de venta operando, y L303 y L307 encadenan con palabras el Information System al Soft System *in our example*. **El mas firme.**
- `cambiar_saludo_cliente_dos_ramas` madre de `cuantificar_impacto_innovacion_6_pasos`: los pasos `2` y `3` del hijo cuentan antes y
  despues de *cambiar las palabras* del saludo, que es lo que L95 cuantifica.
- `construir_estrategia_gente_cuatro_componentes` madre de `aplicar_cinco_pasos_proceso_contratacion`: los pasos `10` y `11` del hijo
  entregan y repasan el Manual, el Objetivo Estrategico, la Organizational Strategy y el Position Contract que la madre compone (L119
  y L269), y L245 hace de la contratacion el primer medio de esa estrategia.
- `recorrer_siete_pasos_programa_desarrollo_negocio` madre de `construir_estrategia_gente_cuatro_componentes`: el hijo es el paso `5`
  que la madre nombra (su paso `8`, L53), y es la parte de `d111` (seccion `6`).

**MIS DUDAS, escritas antes de saber, y si alguna me cae, cae dentro de lo que marco aqui:**

- **Las tres ultimas `CONTINUA` pueden leerse `SANO`**: el saludo es el ejemplo del libro y la cuantificacion vale para cualquier
  innovacion; la estrategia de gente solo **nombra** en una linea lo que la contratacion repasa; y `recorrer` con la estrategia de
  gente es la pregunta de `d111`.
- **Dos `SANO` de dentro de un capitulo que el barrido no levanta pueden leerse `CONTINUA`**: `interrogar_negocio_cinco_preguntas`
  con madre `fingir_prototipo_cinco_mil_replicas` (su condicion es cerrar el trabajo del prototipo), y `aplicar_ocho_reglas_juego_personas`
  con madre `construir_estrategia_gente_cuatro_componentes` (su condicion nombra la People Strategy entre parentesis). **No los
  levanta el barrido, asi que no llevan linea**; si alguno fuese madre e hijo, seria arista por lectura, y **mi lectura no la
  sostiene**.
- **`responder_4_preguntas_estandares_objetivo_estrategico` con `responder_8_preguntas_construir_primary_aim`**, `SANO`: cap_15 L21
  encadena los dos capitulos, pero ningun paso del hijo usa las respuestas del Primary Aim.

**Los `30` `SANO`** comparten la forma pregunta, la palabra sistema, plan o crecimiento, o la imagen del negocio mirado desde fuera,
y ningun paso. **El mas cercano es `dictar_ritmo_crecimiento_preguntas_escritas` con `planificar_tres_pasos_demanda_estado_brecha`**
de Grove: los dos planifican, pero Grove compara demanda y estado presente y los concilia, y Gerber contesta sus preguntas de donde,
cuando, cuanto capital, gente, tecnologia y espacio, con contingencias y por escrito. **Hay procedimiento fuera del solape en los dos
lados** (`6.1`, sin bascula): dos doctrinas legitimas, no duplicado.

## 6. **LAS ARISTAS POR LECTURA** (`D.29`, `D.37`, `D.53`), **CON `d111`, `d108` Y `d098` DELANTE**

**Las que mi lectura sostiene o descarta**, una fila cada una en `.v76aud/aristas_lectura.tsv`, con su tramo de madre, de hijo y su
linea del libro, **escritas antes de que el barrido terminara** (con `5` de `22` recogidas), **mirando tambien madres que viven en el
grafo y en otras bandejas** (la busqueda por asunto, abajo). El cruce dice si el barrido levanto el par y donde vive hoy cada extremo:

@@RUN:0::python .v76aud/cruce_aristas.py@@

**La busqueda por asunto, y las partes de los titulos que dicen cuantas tienen**, por id y titulo sobre grafo mas bandejas:

@@RUN:0::python .v76aud/temas.py | grep -v "^    "@@

(La salida entera, un id por linea con su sede y su libro, en `.v76aud/temas.txt`.)

**LECTURA:**

- **MIS `11` `SOSTENGO` SON `4` LINEAS `CONTINUA` DE LA SECCION `5`, QUE EL BARRIDO LEVANTA, Y `7` ARISTAS POR LECTURA QUE NO**
  (`D.53`): las **`4` de `D.37`** de `fingir_prototipo_cinco_mil_replicas` a las reglas `1`, `2`, `4` y `6` (sus pasos `5`, `6`, `8` y
  `10`, cap_11 L45, L47, L51 y L55), que el barrido no levanta en ningun sentido; **`fingir_prototipo_cinco_mil_replicas` a
  `recorrer_siete_pasos_programa_desarrollo_negocio`** por `D.29` (cap_13 L21 y L41: el programa es el vehiculo del prototipo que la
  madre manda fingir); y **las dos de la pregunta de regla de abajo**, con su duda. **El asunto de `a0d42852` dice *6 aristas por
  lectura*: si es la misma cosa, difiere de mi cuenta en una, y mis dudas son justo donde puede estar.** Lo cruzo par a par en mi
  turno normal, sin decidir aqui cual.
- **`D.37` DISPARA EN UNA SERIE Y NO EN LAS DEMAS.** En `fingir_prototipo_cinco_mil_replicas` si: su titulo y su paso `4` dicen seis,
  sus pasos `5` a `10` las nombran, y **cuatro de las seis partes existen como nodo**; las reglas `3` y `5` no tienen ficha en ninguna
  sede (la busqueda de arriba da `0` en las dos). **En las demas no**: los cinco componentes de la contratacion, las ocho reglas del
  juego, los seis pasos de venta, los trece indicadores y las cinco preguntas **son los propios pasos de su ficha**, y ninguna parte
  existe como nodo aparte; en los tres tipos de sistemas, la venta y la medicion son **ejemplares** de un Soft System y de un
  Information System (L137 y L303), no las clases, y `D.37` pide que la parte sea *la que ese paso nombra*.
- **`d111`, LA SERIE DE `recorrer_siete_pasos_programa_desarrollo_negocio`**: **de las fichas de `cap_18`, la parte es
  `construir_estrategia_gente_cuatro_componentes`**, que es la People Strategy misma (L117 y L119 son su definicion), y el barrido la
  levanta desde los dos lados: **es linea `CONTINUA`, no arista por lectura**, citando el paso `8` de la cabeza (cap_13 L53). La
  contratacion y las reglas del juego son piezas dentro del paso, no el paso. **De `cap_19`, ninguna es el paso `7`**: cap_19 nunca
  define la Systems Strategy como procedimiento, y sus tres fichas son la tipologia y dos ejemplares. **Mi lectura: la cabeza entra
  con `1` de `7` y su unica arista a parte es esa.** Y lo dejo a la vista porque es el punto que `d111` pide decidir con la medida
  delante: **si la estrategia de gente se lee como METODO DENTRO del paso**, que es como la frontera de la vuelta `5` leyo los pasos
  `1` y `2`, **la cabeza entra con `0` de `7` y sin arista a parte**. `D.37` cubre las dos lecturas por su letra; lo que cambia es si
  esta ficha *es* la parte, y eso es lectura, no doctrina.
- **LA PREGUNTA DE REGLA, la de mas peso de esta pagina, y no la decido aqui:** `construir_estrategia_gente_cuatro_componentes` dice en
  su **titulo** *cuatro componentes* y los nombra (Primary Aim, Strategic Objective, Organizational Strategy, Operations Manuals), y dos
  de esas partes tienen ficha que las construye: `responder_8_preguntas_construir_primary_aim` y
  `responder_4_preguntas_estandares_objetivo_estrategico`. **Leido por la letra de `D.37`, la estrategia de gente seria CABEZA y esas
  dos, sus PARTES**; **mi lectura va en la direccion contraria, por `D.29`**: esas dos son **madres** de la estrategia de gente, cuya
  condicion es tenerlas escritas y cuyo paso `2` *arranca con* el Primary Aim. Mis razones: **la cuenta es del titulo de la ficha y
  no del libro** (L119 enumera sin contar, y la correccion del titular de `D.37` manda `D.29` cuando el texto solo enumera), y **esas
  dos fichas son metodos dentro de los pasos `1` y `2` del programa**, no el Primary Aim ni el Objetivo Estrategico (la misma lectura
  de `d111`). **Si la letra de `D.37` alcanza a una cuenta que solo pone la ficha, la direccion se invierte y eso es doctrina**: mi
  encargo dice que se para y se trae. **Lo llevo a mi turno normal con la lectura del extractor delante.**
- **`d108`, cap_14 L27 contra L117, con las dos delante:** L27 pregunta *What do I value most? What kind of life do I want? What do I
  want my life to look like, to feel like? Who do I wish to be?* y L117 abre *the following questions*, las ocho de L119 a L133 que
  `responder_8_preguntas_construir_primary_aim` transcribe enteras (seccion `3`). **Mi lectura firma la razon que escribe `d108`** (la `ACTA G4` no la he abierto; su razon la leo en la deuda): L27 es el
  mismo cuestionario del mismo Primary Aim en corto, su *look like* esta en L119, y separarlo haria el gemelo de su propio donante. **La
  ficha no le da nodo aparte y no hace falta.**
- **`d098`, el puntero de las tres fases de `cap_05` L29:** **ninguna ficha es su cabeza** (ninguna enumera Infancy, Adolescence y
  Maturity) **y ninguna es una de sus partes**: las dos de `cap_08`, el capitulo de Maturity, son piezas de ese capitulo (la plantilla
  de Watson y el modelo desde el cliente), no la fase; y `dictar_ritmo_crecimiento_preguntas_escritas`, de `cap_07`, es el remedio
  que el libro da al salir de la zona de confort, no la Adolescencia. En grafo mas bandejas **no hay cabeza ni nodo de fase** (la
  busqueda de arriba: lo que levanta *madurez* es la madurez relevante a la tarea de Grove, otra doctrina). **Sin arista**, y `d098`
  sigue esperando su cabeza.
- **Ninguna madre del grafo ni de otra bandeja para las `22`**, por mi lectura: lo que la busqueda levanta por contratacion,
  organizacion, sistema, manual, color o plan son otras doctrinas de otros libros (`6.1`), y ninguna es la condicion de una de las
  `22` ni la remite con palabras.

## 7. **EL ORDEN QUE MI LECTURA OBLIGA** (`D.36`)

**No es un orden: son las restricciones**, escritas antes de ver el del extractor. Madre antes que hijo por mis `CONTINUA` y mis
`SOSTENGO` con los dos extremos en la tanda, y cuantas cumple el orden de pieza del libro, **que saco de mi fidelidad** (capitulo y
primera linea), porque `.v76aud/las22.txt` va alfabetica:

@@RUN:0::python .v76aud/restricciones_orden.py@@

**LECTURA:** las `11` que obligan **las cumple ya el orden de pieza del libro**. De las `4` de `D.36` de un solo lado, **dos no las
cumple** (`medir_sistema_venta_trece_indicadores_benchmark` antes que `construir_estrategia_gente_cuatro_componentes`, y
`interrogar_negocio_cinco_preguntas` antes que `operar_modelo_gente_destreza_minima`); **son informativas y no obligan**, porque la
aduana de `insertar` mide grafo mas bandejas (`D.38.5`) y el par se levanta igual desde el lado que entre despues. **Su orden, contra
estas once, lo compruebo en mi turno normal.**

## 8. **`R8` MEDIDO SOBRE MI ENCARGO DE LA `76`, CON EL MISMO INSTRUMENTO** (`ACTA 74` `74.11` y `74.12`)

`R8` dice: *toda cifra de medida que escriba en `PROMPT_SIGUIENTE.md` (un reloj, una banda, una cuenta que solo se comprueba abriendo
un fichero, en digito o en letra) va DENTRO de un bloque `$` con su salida, o lleva EN SU MISMA LINEA la seccion del acta donde esta
pegada: ni la de la linea de al lado, ni una ruta de fichero*. El fichero es el encargo que escribi al cerrar la `ACTA 74`, y el
instrumento es el de la `74.12`, corrido sin copiarlo, con su salida de hoy contra la que guardo aquella acta:

@@RUN:0::head -1 docs/loop/PROMPT_SIGUIENTE.md | cut -c1-100; ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, $7, $9}'@@
@@RUN:0::python .v75aud/normal/r8_encargo76.py | diff - .v75aud/normal/r8_encargo76.txt && echo "IDENTICO a .v75aud/normal/r8_encargo76.txt, la salida de la ACTA 74 74.12"; python .v75aud/normal/r8_encargo76.py | tail -1@@

(Cada linea con numero, con sus digitos y sus palabras de numero, en `.v75aud/normal/r8_encargo76.txt`.) **LECTURA, grupo a grupo,
que es mia y no del instrumento; las volvi a leer una a una y no copio la de la `74.12`, aunque llego al mismo reparto:**

- **Numeros de vuelta, de acta, de rama o de carpeta de la casa**: `L3`, `L18`, `L21`, `L50`, `L64`, `L69`, `L70`,
  `L74`, `L77`, `L78`, `L79`, `L85`, `L86`, `L88`, `L93`, `L95`, `L96`, `L109`, `L121`, `L124`, `L125`, `L128`.
- **Secciones, reglas, deudas y numeros de tarea o de punto**: `L4`, `L14`, `L17`, `L19`, `L46`, `L52`, `L62`, `L66`, `L68`, `L72`,
  `L76`, `L80`, `L81`, `L83`, `L90`, `L92`, `L94`, `L96`, `L99`, `L105`, `L108`, `L109`, `L112`, `L115`, `L123`, `L138`, `L140`.
- **Identificadores de capitulo, de linea del libro o de fecha**: `cap_22` en `L45`; `cap_14`, `L27` y `L117` en `L103`; `cap_05` y
  `L29` en `L104`; `cap_13`, `cap_18` y `cap_19` en `L111`; el `23` sep en `L24`.
- **Umbrales de la casa**: el `10` por ciento de `L80`, que es regla y no medida.
- **Palabras de numero sin seccion**: *cinco a la vez* (`L23` y `L86`, un tope de la casa), *cinco fichas a la vez* (`L27`, el
  parametro del barrido de la `73`, cuyo reloj va dentro del bloque de `L30` a `L34`), *tres asientos* (`L24`, la frase fija del arnes,
  que el prompt de este turno trae igual), *los dos delante* y *las dos delante* (`L93` y `L103`, los dos nodos de un par y las dos
  lineas del libro), *las tres fases* (`L104`, lo que dice `cap_05` `L29`, citada en la misma linea), *en cero* (`L109`, la meta) y
  *cero guiones* (`L145`, la frase fija). **Ninguna es una cuenta de fichero.**
- **Las cifras de medida** van dentro de un bloque `$` (el reloj de la `73`, la clase, el tablero) o llevan su seccion de la `ACTA 74`
  en la misma linea: `L1`, `L5`, `L16`, `L56` a `L60`, `L65`, `L75`, `L87` y `L118`.

**`R8` CUMPLIDO EN EL ENCARGO DE LA `76`, medido otra vez aqui.**

## 9. **LO QUE DEJO PARA MI TURNO NORMAL, ESCRITO ANTES DE VER EL REPORTE**

1. **`R5`** en su reporte, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` sacados otra vez de los originales y con la
   cabecera cambiada a la `76`; **y `R9`** en cada fila de su fidelidad y en cada cuenta de PUENTE, con su patron ensanchado contra
   el mio.
2. **El censo con su hash**: que la vuelta no movio el grafo, la bitacora, los censos ni la bandeja de Marquet, y que en la de Gerber
   solo cambiaron las `6` fichas corregidas, **con `git diff`**; **y quien escribio `src/tablero.py` y `tests/test_aceptacion.py` a
   las `06:45:09`** (seccion `2`, punto `3`), con la suite corrida por mi.
3. **Mi fidelidad contra la suya, paso a paso**: mis `176` filas contra las suyas; sus correcciones contra mi lectura de sus textos
   viejos (seccion `3`); **los `8` PUENTE que declaran las fichas contra los `9` de su asunto de commit**; y **el *despues del cambio*
   del paso `4` de `cuantificar_impacto_innovacion_6_pasos`**, que es mi duda y su misma figura del paso `6`. **Si el marca PUENTE un
   paso de hoy que yo lei `T` sin duda, y gana, la caida de lectura es mia.**
4. **Mi barrido contra el suyo, fila dirigida a fila dirigida**, y **mis clases contra sus lineas de veredicto, par a par**; mis
   aristas por lectura contra las suyas, **por par y no por cuenta** (secciones `4` a `6`), con **`d111`, `d108` y `d098`** y **la
   pregunta de regla de la seccion `6`** delante.
5. **Su orden contra mis restricciones** (seccion `7`).
6. **La huella de las `22` fichas** que su cierre dice sellar, contra las mias de `.v76aud/huellas_al_barrer.txt`, tomadas antes de
   barrer y comprobadas al recogerlo.
7. **La muestra pineada de los SANO**: esta vuelta no escribe en la bitacora; los `SANO` de las `22` se muestrean cuando entren.
8. **`R8` sobre el encargo de la `77`**, medido antes de cerrarlo, y **`R10`**: toda salida que pegue en el encargo, corrida despues de
   mi ultima escritura en el registro que mide, o vuelta a correr antes del commit y comparada.

## 10. **ESTA PAGINA CONTRA `R6`, `R7` Y LOS GUIONES, MEDIDA SOBRE ELLA MISMA**

El generador corre dos veces, y estos bloques de la segunda pasada leen la pagina que escribio la primera, identica salvo estos
bloques. El primero cuenta las lineas de bloque `$` que empiezan por una clave de relacion; el segundo, con la copia de
`.v73aud/r7_pagina.py`, cuenta las lineas de bloque que reparten una cifra en clases y cuantas traen su `suma`; el tercero cuenta
guiones largos y medios:

@@RUN:0::grep -c -E "^    +(previos|siguientes|nodos_previos|nodos_siguientes)" docs/loop/APERTURA_CIEGA.md@@
@@RUN:0::python .v76aud/r7_pagina.py@@
@@RUN:0::grep -c -P "\x{2014}|\x{2013}" docs/loop/APERTURA_CIEGA.md@@
