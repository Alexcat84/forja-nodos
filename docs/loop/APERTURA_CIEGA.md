# APERTURA CIEGA DE LA VUELTA 73, lote 7 (`grove_high_output`), **CLASE INSERCION, VUELTA DE PREPARACION**

*Auditor `claude-opus-5-5`, fase ciega, 26 sep 2026. En la corrida que arranco el 25 a las `21:43`, el arnes la numera `VUELTA 2`.
Linea **serial**, rama `extraccion-mundo-11`. Modo austero (`D.47`). Todo lo de esta pagina sale de `.v73aud/`, escrito y
corrido en esta fase; cada bloque `$` lo pega `.v73aud/generar_apertura.py` corriendo el comando en el momento de escribirla.
**No hay ninguna tabla en esta pagina**, a proposito, como en la `71`.*

**UNA LIMITACION DE METODO, DICHA ANTES DE NADA: EN ESTA FASE NO HE CORRIDO `git` EN LA CARPETA**, ni una vez. La carpeta de una
linea viva es solo del arnes (`PARALELO.md` `7`), y lo aplico tambien a mi asiento, como pidio la `ACTA 71` `71.9`. **Lo que
se mide con `git diff` aqui no lo mido**: que cambio la vuelta linea a linea y contra que commit. Lo que si mido sin `git` es
que ficheros son mas nuevos que mi encargo y que fichas cambiaron contra mis propias huellas de la `71` (seccion `2`). El commit
en que esta el arbol lo leo de los ficheros de `.git/`:

    $ cat .git/HEAD; cat .git/refs/heads/extraccion-mundo-11
    ref: refs/heads/extraccion-mundo-11
    5a868688592cccf9af89a1367f7da39b01e52d5e

## 0. **LA HERENCIA** (`D.40`)

ACTA ANTERIOR LEIDA: b58e01d4feff0064cd14042387d9d11124b9f001

**Comprobada sin git**: es el blob de `docs/loop/ACTA_AUDITOR.md` tal como esta hoy en el arbol, calculado a mano como lo
calcula git. La `ACTA 71` la lei entera, de su linea de cabecera a la ultima del fichero:

    $ python .v73aud/huella_acta.py
    sha1 del blob tal cual: b58e01d4feff0064cd14042387d9d11124b9f001
    lineas con CRLF en el arbol: 0 | sha1 del blob normalizado a LF: b58e01d4feff0064cd14042387d9d11124b9f001
    lineas del fichero: 48899 | la ACTA 71 empieza en la linea: [48492]

HEREDADO 1: NO APLICA en esta fase. **Motivo:** `R5` es un remedio **del extractor** y se mide **sobre su reporte de la
`73`** (`ACTA 71` `71.11`: *el reporte de la `73`, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py`, los dos con
la cabecera del tramo cambiada a la `73`*), y el reporte **no esta en el arbol**: el arnes lo retiro para esta fase (`D.34.2`)
y no lo he recuperado por ninguna via. **Se mide en mi turno normal**, con los dos instrumentos sacados otra vez de los
originales y no de las copias del extractor. Lo que si esta en mi mano lo cumplo en mi pagina: cada bloque `$` lleva la salida
del comando que abre, y nada mas.

    $ ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl
    ls: cannot access 'docs/loop/REPORTE.md': No such file or directory
    ls: cannot access 'docs/loop/ultimo_extractor.json': No such file or directory
    ls: cannot access 'docs/loop/ultimo_auditor.json': No such file or directory
    ls: cannot access 'docs/loop/CREDITO_serial.jsonl': No such file or directory
    $ grep -n "VUELTA 2 : APERTURA CIEGA" docs/loop/loop.log | tail -1
    7424:[2026-09-26 02:42:16] VUELTA 2 : APERTURA CIEGA (claude-opus-5-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl

HEREDADO 2: CUMPLIDO. **`R6`, mio** (`ACTA 71` `71.11`): en esta fase los pasos de cualquier nodo los imprime
`.v67aud/normal/pasos_ciego.py`, que no enseña `previos` ni `siguientes`: con el lei las `7` fichas
(`.v73aud/pasos_siete.txt`) y los nodos de fuera (`.v73aud/pasos_fuera_*.txt`), y el unico bloque de pasos de esta pagina lo
corre el (seccion `5`). Los ficheros de pasos que lei, cuantas lineas con esas claves traen, y cuantos instrumentos mios las
nombran:

    $ grep -c -E "previos|siguientes" .v73aud/pasos_*.txt
    .v73aud/pasos_fuera_a.txt:0
    .v73aud/pasos_fuera_b.txt:0
    .v73aud/pasos_siete.txt:0
    $ grep -l -E "previos|siguientes" .v73aud/*.py .v73aud/*.sh | wc -l
    0

**LO UNICO QUE SE ACERCA, para que se juzgue:** `.v73aud/correcciones.py` (seccion `3`) imprime tramos del `resumen_teorico` de
las fichas que empiezan por *CORRECCION DECLARADA*; es prosa del extractor sobre pasos y citas, y el bloque de esta pagina que
lo resume solo cuenta y nombra fichas. **No vi ninguna clave de relacion con su valor de un nodo tocado en esta fase.** El
cumplimiento de la pagina entera lo mide un `grep` sobre ella al cerrarla (seccion `10`).

HEREDADO 3: CUMPLIDO. **`R7`, mio** (`ACTA 71` `71.11`): toda linea de esta pagina que reparte un total en clases la imprime un
instrumento que cuenta **todas** las clases con el mismo predicado y **dice su `suma`**: `contar_fidelidad`, `huellas_contra_71`,
`cobertura`, `temas`, `vecinos_tabla`, `armar_clases`, `cruce_clases`, `cruce_aristas` y la copia de `.v70aud/poblacion.py`, y
el de `R8`, que es el de la `ACTA 71` sin tocar. **Medido sobre la pagina misma** en la seccion `10`, con la copia de
`.v70aud/r7_pagina.py`.

HEREDADO 4: CUMPLIDO. **`R8`, mio, ESCALADO** (`ACTA 71` `71.11`): se comprueba **aqui**, en mi fase ciega, sobre el encargo
de la `73`, **con el mismo instrumento y leyendo sus lineas**. Lo corri sin copiarlo (`.v72aud/normal/r8_encargo73.py`), su
salida es identica a la que la `ACTA 71` `71.12` guardo, y la lectura linea a linea, con **una lectura mia discutible que dejo a
la vista y no escondo** (dos lineas con una cuenta en letra que el instrumento no ve), esta en la seccion `8`. El encargo de la
`74` lo escribo en mi turno normal y se mide alli.

## 1. **LO QUE VI SIN BUSCARLO, Y LO DIGO ANTES DE MEDIR** (`d146`)

**La foto de `git status` que el entorno me pone delante trae los asuntos de los commits del extractor, y tres son cifras
de su vuelta**: `c98d891b` (*la fidelidad entera de las 7 (42 pasos, 6 PUENTE corregidos en la bandeja antes del barrido,
cap_15 releido entero)*), `4ab7ff52` (*el barrido de las 7 (29 pares, recogido dentro del turno), sus 29 lineas de veredicto,
las aristas por lectura y el orden (D.36 en cero, 3 aristas esperadas)*) y `70916d6b` (*censo 430/1081/1/7/85 al abrir y al
cerrar, PASOS INVENTADOS 22,7/0,0/6,2 con 0 que entrara, huellas de las 7, D.61 sin abiertos, R5, guardas y cierre estricto en
verde; ninguna insertada*). **Los lei antes de medir nada.** Es el mismo hueco de `d146` que declararon las aperturas de la `65`
a la `72`, y no lo arreglo yo (`D.45`). Tambien lei la cola de `docs/loop/loop.log`, que no se retira, mi `ACTA 71` entera, la
`ACTA 60` `60.5` (que mi encargo cita) y mi encargo, `docs/loop/PROMPT_SIGUIENTE.md`.

**Y DOS COSAS MAS, DEL MISMO TIPO:** un `ls .v73ext` me enseño **los nombres** de los ficheros de su carpeta (entre ellos
`fidelidad.tsv`, `veredictos_listos.txt`, `aristas_lectura.txt`, `orden.txt` y un `vecinos_<id>.json` por ficha), **no su
contenido**; y **cuatro fichas de la bandeja llevan dentro, en su `resumen_teorico`, la lectura del propio extractor** (la
*CORRECCION DECLARADA DE LA VUELTA 73* con el texto viejo dentro). **Esas correcciones las lei DESPUES de escribir y contar mi
fidelidad paso a paso** (`.v73aud/fidelidad_fuente.txt` y su contador, antes de `.v73aud/correcciones.py`), y lo que dicen va
en la seccion `3`, separado.

**LO QUE HAGO CON ELLO:** ninguna cifra de esta pagina sale de esos asuntos; todas salen de un instrumento corrido en esta
fase, y donde coinciden lo digo como coincidencia y no como fuente. **No he abierto nada de `.v73ext/` por dentro**, **ni
`bitacora/VEREDICTOS.jsonl` por dentro**: de ella solo cuento lineas. **Y ESTO SI PESA SOBRE MI LECTURA, Y LO DIGO:** el asunto
de `4ab7ff52` me dijo *3 aristas esperadas* antes de leer. Mis aristas salen de la seccion `6` con su linea del libro, y son las
que son; pero no puedo probar que no me empujo, y por eso lo escribo aqui.

## 2. **EL ALCANCE, Y EL CENSO QUE LO SOSTIENE**

El encargo de la `73` es **dejar listas sin insertar ninguna** las fichas que quedan en la bandeja de Grove, las de `cap_15`,
`cap_16` y `cap_17`: fidelidad entera, barrido, veredictos, aristas por lectura, orden y la huella. Mi lista es la bandeja
entera, leida del directorio, y su reparto por capitulo lo da el instrumento de la `ACTA 71` `71.1`, corrido hoy:

    $ wc -l < .v73aud/los7.txt; ls cuarentena/grove_high_output | sed 's/\.json$//' | diff - .v73aud/los7.txt && echo "los7.txt es la bandeja de Grove entera, fichero a fichero"
    7
    los7.txt es la bandeja de Grove entera, fichero a fichero
    $ python .v72aud/normal/siete.py | diff - .v72aud/normal/siete.txt && echo "siete.py de hoy: IDENTICO a su salida de la ACTA 71 71.1"; tail -2 .v72aud/normal/siete.txt
    siete.py de hoy: IDENTICO a su salida de la ACTA 71 71.1
    fichas por capitulo: {'cap_15': 3, 'cap_16': 1, 'cap_17': 3} | suma: 7
    pasos por capitulo: {'cap_15': 22, 'cap_16': 4, 'cap_17': 16} | suma: 42

**El censo de hoy**, sin `git` (grafo, bitacora, pares mutuos; las bandejas de Grove, Gerber y Marquet, los insertados de
Grove y `procesos/`), y la poblacion de la aduana:

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        430 dataset/nodos.jsonl
       1081 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1512 total
    $ for d in cuarentena/grove_high_output cuarentena/_insertados/grove_high_output cuarentena/gerber_emyth cuarentena/marquet_turn_the_ship; do echo "$d $(ls $d/*.json | wc -l)"; done; echo "procesos $(ls -A procesos/ | wc -l)"
    cuarentena/grove_high_output 7
    cuarentena/_insertados/grove_high_output 85
    cuarentena/gerber_emyth 22
    cuarentena/marquet_turn_the_ship 20
    procesos 0
    $ python .v70aud/poblacion.py
    poblacion: 479 | por sede: {'grafo': 430, 'bandeja': 49} | suma: 479
    $ python forja.py gate | head -2
    GATE VERDE.
      nodos verificados: 430

**Lo que es mas nuevo que mi encargo**, que escribi al cerrar la `ACTA 71`, en las carpetas de dato, de codigo y de libro; y
**las fichas de las tres bandejas contra mis huellas de la `71`**, tomadas antes de mi barrido de entonces:

    $ ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, $7, $9}'
    2026-09-26 01:47:33.720687500 docs/loop/PROMPT_SIGUIENTE.md
    $ find cuarentena dataset bitacora censos config fuentes esquema src scripts tests forja.py -type f -newer docs/loop/PROMPT_SIGUIENTE.md | sed 's|/[^/]*\.json$|/*.json|' | sort | uniq -c
          4 cuarentena/grove_high_output/*.json
    $ python .v73aud/huellas_contra_71.py
    fichas de hoy contra .v71aud/huellas_al_barrer.txt: {('gerber_emyth', 'igual'): 22, ('grove_high_output', 'CAMBIO'): 4, ('grove_high_output', 'igual'): 3, ('marquet_turn_the_ship', 'igual'): 20} | suma: 49
      CAMBIO cuarentena/grove_high_output/gestionar_retencion_subordinado_valioso_renuncia.json
      CAMBIO cuarentena/grove_high_output/pedir_critica_anonima_curso_entrenamiento_dictado.json
      CAMBIO cuarentena/grove_high_output/responder_primer_aviso_renuncia_subordinado.json
      CAMBIO cuarentena/grove_high_output/usar_banco_nueve_preguntas_entrevista.json

**LECTURA:** `430`, `1081`, `1`, `7` y `85` son los de mi `ACTA 71` `71.1` al cerrar la `72`, y Gerber y Marquet siguen en
`22` y `20`: **la vuelta no inserto nada ni movio nada de sede**, que es lo que el encargo pedia, y `procesos/` esta vacio. La
poblacion del barrido sigue en `479`. **Lo unico mas nuevo que mi encargo fuera de `docs/loop/` y de `.v73ext/` son `4` fichas
de la bandeja de Grove, y son las `4` cuyas huellas cambiaron contra las mias de la `71`**; las otras `3` de Grove y las `42` de
Gerber y Marquet son byte a byte las de entonces. **Lo que no puedo decir sin `git`**: si alguna linea de la bitacora o algun
byte del grafo cambio sin cambiar la cuenta ni la fecha. Eso lo mido en mi turno normal, con el hash del reporte delante.

**Y LAS `7` SON TODO LO QUE GROVE TIENE DE ESOS TRES CAPITULOS**, en cualquier sede, por la `UNIDAD DE ORIGEN` de su
`resumen_teorico`:

    $ python .v73aud/cobertura.py
    por sede y capitulo: {('bandeja', 'cap_15'): 3, ('bandeja', 'cap_16'): 1, ('bandeja', 'cap_17'): 3} | suma: 7
    de esos tres capitulos y fuera de los 7: 0

**LECTURA, sin medirla mas:** hay piezas de esos capitulos sin candidato en ninguna sede. En `cap_15`, casi toda la mitad de la
entrevista: el proposito de L17 a L25, el control de la entrevista y cortar al que se enrolla (L33), llevarla a terreno comun
(L35), las cuatro categorias de L57 a L87, las preguntas directas y la situacion hipotetica (L91 y L93), dejar que pregunte el
candidato (L95), las referencias y la segunda entrevista (L97 y L99) y no usar trucos (L101). En `cap_16`, la paga como
retroalimentacion: la prima por desempeño y sus tres factores (L19 a L23), las dos formas de administrar el salario y su
compromiso (L25 a L35) y los ascensos por desempeño (L37 a L47). En `cap_17`, el porque del entrenamiento (L19 a L47) y lo que
descubres la primera vez (L63 a L69). **Es la frontera de las vueltas que minaron Grove, que no reabro (`D.47`)**; solo digo
que la vi, y que en `cap_15` es ancha.

## 3. **LA FIDELIDAD DE LAS `7`, LEIDA ENTERA** (`D.30`, `D.58`, `8`)

Lei **enteros** los tres capitulos, `cap_15` (Cap. 14, *Two Difficult Tasks*), `cap_16` (Cap. 15, *Compensation as
Task-Relevant Feedback*) y `cap_17` (Cap. 16, *Why Training Is the Boss's Job*), y cada paso de las `7` contra su linea, con los
pasos delante por `pasos_ciego.py` (`.v73aud/pasos_siete.txt`):

    $ wc -l fuentes/grove_high_output/cap_1[5-7].md
      123 fuentes/grove_high_output/cap_15.md
       51 fuentes/grove_high_output/cap_16.md
       69 fuentes/grove_high_output/cap_17.md
      243 total

Una fila por paso en `.v73aud/fidelidad.tsv`: `T` transcripcion, `P` puente (**la clausula reescrita cuenta como `P`**, `ACTA
62` `62.5`), `D` mi duda, con su capitulo, su linea y la frase del libro. El contador es copia de `.v71aud/contar_fidelidad.py`
con las rutas cambiadas, **una fila por capitulo** (`8.2`) y la suma de cada reparto (`R7`), y cruza cada fila con los pasos de
la ficha de la bandeja de hoy:

    $ python .v73aud/contar_fidelidad.py
    candidato                                                    ficha filas   T   P  DUDA  suma
    desarrollar_primer_curso_entrenamiento                           7     7   7   0     0     7
    gestionar_retencion_subordinado_valioso_renuncia                 6     6   5   0     1     6
    pedir_critica_anonima_curso_entrenamiento_dictado                4     4   4   0     0     4
    priorizar_lista_entrenamiento_subordinados                       5     5   5   0     0     5
    reciclar_empleado_ascendido_mas_alla_capacidad                   4     4   4   0     0     4
    responder_primer_aviso_renuncia_subordinado                      7     7   7   0     0     7
    usar_banco_nueve_preguntas_entrevista                            9     9   9   0     0     9
    cap_17: candidatos 3 | pasos en ficha 16 | filas 16 | T 16 | P 0 | DUDA 0 | suma: 16 | PUENTE 0 de 16 = 0.00 por ciento | si las DUDA cayesen: 0 de 16 = 0.00 por ciento
    cap_15: candidatos 3 | pasos en ficha 22 | filas 22 | T 21 | P 0 | DUDA 1 | suma: 22 | PUENTE 0 de 22 = 0.00 por ciento | si las DUDA cayesen: 1 de 22 = 4.55 por ciento
    cap_16: candidatos 1 | pasos en ficha 4 | filas 4 | T 4 | P 0 | DUDA 0 | suma: 4 | PUENTE 0 de 4 = 0.00 por ciento | si las DUDA cayesen: 0 de 4 = 0.00 por ciento
    los tres: candidatos 7 | pasos en ficha 42 | filas 42 | T 41 | P 0 | DUDA 1 | suma: 42

**LECTURA: los tres capitulos son de inventario rico donde hay fichas** (la lista de preguntas de L39 a L55, la cadena de
imperativos de L111, la de L113 a L121, la de L49 y la de L49 a L61 de `cap_17`), y los pasos de hoy los transcriben casi frase a
frase. **No encuentro ningun PUENTE en el texto de hoy de las fichas.** Mi unica duda es **una figura**, y me inclino a `T`:

- **dos frases del libro leidas de corrido**: `gestionar_retencion_subordinado_valioso_renuncia` paso `6` junta en *el segundo*
  compromiso a ti y a la gente con la que trabaja a diario, y dice que *el segundo pesa mas*, donde L121 pone el compromiso
  contigo en una frase y en la siguiente compara los compromisos con la gente de cada dia contra el del conocido nuevo.

**`d078`, CON LA LINEA DELANTE:** el *no discutas* del paso `3` y el del paso `5` de `responder_primer_aviso_renuncia_subordinado`
**los dice el libro dos veces en la misma linea**, L111: *Let him talk, don't argue about anything with him* y, cuatro frases
despues, *Don't argue, don't lecture, and don't panic*. **Lo leo igual que `d078`: es repeticion del libro, no del extractor**, y
los dos pasos son `T`.

**UNA COSA DE FORMA QUE NO ES PUENTE:** `priorizar_lista_entrenamiento_subordinados` paso `4` dice *los mando maestros* por
*manager-teachers* de L51: es la transcripcion mal concordada, no una clausula que el libro no ponga. Esa ficha es byte a byte
la de mi fase ciega de la `71` (seccion `2`), asi que no es de esta vuelta.

**`PASOS INVENTADOS` por mi instrumento, sobre el texto de hoy: `0` en los tres capitulos**; si mi duda cayese, `cap_15` `1` de
`22` (`4,55`). **Por debajo del `10` en las dos lecturas.** Es preparacion y no entrada.

**Y LO QUE LEI DESPUES, EN LAS FICHAS:** cuatro de las `7` traen en su `resumen_teorico` una *CORRECCION DECLARADA DE LA
VUELTA 73* con el texto viejo dentro, y son las `4` cuyas huellas cambiaron (seccion `2`):

    $ python .v73aud/correcciones.py | grep -c "^====="; python .v73aud/correcciones.py | grep "^=====" | sed 's/^===== //'
    4
    gestionar_retencion_subordinado_valioso_renuncia
    pedir_critica_anonima_curso_entrenamiento_dictado
    responder_primer_aviso_renuncia_subordinado
    usar_banco_nueve_preguntas_entrevista

**Leo sus textos viejos y los clasifico yo, pasos citados por la propia correccion:**

- `usar_banco_nueve_preguntas_entrevista` paso `3` (*Preguntale que te convenceria de que tu empresa deberia contratarlo*,
  contra *Convince me why my company should hire you*, L43): **`P`**, es otra pregunta. Paso `8` (*Si el puesto lo justifica,
  ...*, contra *(Vary this one according to the situation.)*, L53): **`P`**, una condicion que el libro no pone. Y su condicion
  de activacion (*la hora u hora y media* contra *an hour or two*, L27), que no es paso y no cuenta en la cifra.
- `responder_primer_aviso_renuncia_subordinado` paso `6` (*..., en vez de intentar resolverlo todo en el momento*, contra
  *Don't try to change his mind at this point, but buy time*, L111): **`P`**.
- `gestionar_retencion_subordinado_valioso_renuncia` paso `1` (*..., en vez de cargar con todo tu solo*, L113): **`P`**. Paso
  `5` (*dejando claro que no se trata de una concesion arrancada por chantaje, sino de corregir algo que ya se deberia haber
  hecho*, contra el *You might say something like* de L119): **lo habria leido `D`, inclinado a `T`**: es la figura del
  **ejemplo convertido en mandato**, la misma que en la `71` lei `D` y la `ACTA 70` `70.4` adjudico `T`; el contenido es el del
  ejemplo del libro. **Su lectura `P` es mas estricta que la mia y la correccion es mas fiel que el texto viejo**, asi que no hay
  nada que corregir en lo que queda.
- `pedir_critica_anonima_curso_entrenamiento_dictado` paso `3` (*... complacer a todos los miembros de tu clase por igual*, L61):
  **`P`**, flojo: el *in about equal balance* de L61 es del reparto de las opiniones, no de complacer a todos por igual.

**LECTURA:** sobre el texto viejo, **mi lectura da `5` `P` seguros y `1` `D`** en esos seis pasos: `cap_15` `4` o `5` de `22` y
`cap_17` `1` de `16`. **Las dos lecturas pasan del `10` en `cap_15`, y por eso `cap_15` se relee entero antes de seguir**
(`D.58`); **coincide con el *6 PUENTE corregidos* y el *cap_15 releido entero* del asunto de `c98d891b`, y con el *22,7/0,0/6,2*
de `70916d6b` si se lee `5` de `22`, `0` de `4` y `1` de `16`**, y lo digo como coincidencia. **Los seis pasos corregidos los lei
yo `T` en su texto de hoy**: las correcciones se sostienen. **Lo que no puedo decir** es si mi lectura ciega habria cazado esos
puentes, porque cuando lei ya no estaban. Fila a fila lo cruzo en mi turno normal.

## 4. **MI BARRIDO DE LAS `7`, SOBRE GRAFO MAS BANDEJAS** (`D.38.4`, `D.38.5`)

Copia de `.v71aud/barrido_uno.py` (la ficha normalizada como la aduana, contra `dataset/nodos.jsonl` mas
`aduana.poblacion_de_bandejas`, con `buscar_vecinos` de `src/aduana.py`, que desde el `25` reparte el calculo por el presupuesto
unico de plazas) y de `.v71aud/barrer.sh` con la lista cambiada a `.v73aud/los7.txt`, **cinco a la vez, recogido entero dentro
de este turno**, lanzado **despues** de que las fichas cambiasen por ultima vez (seccion `2`). Antes de lanzarlo guarde la
huella de cada ficha de las tres bandejas y del grafo, y al recogerlo las comprobe:

    $ head -1 .v73aud/barrido.log; tail -1 .v73aud/barrido.log; grep -c "rc=0" .v73aud/barrido.log; grep -c "rc=" .v73aud/barrido.log
    INICIO 2026-09-26 02:44:03
    TODOS TERMINADOS 2026-09-26 03:07:01
    7
    7
    $ wc -l < .v73aud/huellas_al_barrer.txt; sha1sum -c --quiet .v73aud/huellas_al_barrer.txt && echo "las 49 fichas de las tres bandejas y el grafo: mismas huellas que al barrer"
    50
    las 49 fichas de las tres bandejas y el grafo: mismas huellas que al barrer

**Poblacion y vecinos por candidato, cada fila de vecino con su senial, y los pares sin orden:**

    $ python .v73aud/vecinos_tabla.py | tee .v73aud/vecinos_tabla.txt
    (1) candidato | poblacion | vecinos | en grafo | en bandeja
        desarrollar_primer_curso_entrenamiento                   479   2   0   2
        gestionar_retencion_subordinado_valioso_renuncia         479   3   1   2
        pedir_critica_anonima_curso_entrenamiento_dictado        479   7   2   5
        priorizar_lista_entrenamiento_subordinados               479   3   0   3
        reciclar_empleado_ascendido_mas_alla_capacidad           479   1   0   1
        responder_primer_aviso_renuncia_subordinado              479   7   4   3
        usar_banco_nueve_preguntas_entrevista                    479   6   3   3
    sin fichero de vecinos: 0 []
    (2) vecino levantado | senial | texto familia paso
        desarrollar_primer_curso_entrenamiento                 > pedir_critica_anonima_curso_entrenamiento_dictado      bandeja similitud_texto  0.450 0.250 0.451
        desarrollar_primer_curso_entrenamiento                 > priorizar_lista_entrenamiento_subordinados             bandeja similitud_texto  0.409 0.143 0.394
        gestionar_retencion_subordinado_valioso_renuncia       > responder_primer_aviso_renuncia_subordinado            bandeja similitud_texto  0.376 0.250 0.421
        gestionar_retencion_subordinado_valioso_renuncia       > entregar_evaluacion_desempeno_tres_claves              grafo   similitud_texto  0.403 0.000 0.390
        gestionar_retencion_subordinado_valioso_renuncia       > usar_banco_nueve_preguntas_entrevista                  bandeja similitud_texto  0.388 0.000 0.398
        pedir_critica_anonima_curso_entrenamiento_dictado      > gestionar_retencion_subordinado_valioso_renuncia       bandeja similitud_texto  0.369 0.000 0.516
        pedir_critica_anonima_curso_entrenamiento_dictado      > priorizar_lista_entrenamiento_subordinados             bandeja similitud_texto  0.472 0.111 0.447
        pedir_critica_anonima_curso_entrenamiento_dictado      > desarrollar_primer_curso_entrenamiento                 bandeja similitud_texto  0.447 0.250 0.396
        pedir_critica_anonima_curso_entrenamiento_dictado      > usar_banco_nueve_preguntas_entrevista                  bandeja similitud_texto  0.388 0.000 0.431
        pedir_critica_anonima_curso_entrenamiento_dictado      > repartir_supervision_puesto_funcional_mision           grafo   similitud_texto  0.351 0.000 0.425
        pedir_critica_anonima_curso_entrenamiento_dictado      > responder_primer_aviso_renuncia_subordinado            bandeja similitud_texto  0.410 0.000 0.389
        pedir_critica_anonima_curso_entrenamiento_dictado      > entregar_evaluacion_desempeno_tres_claves              grafo   similitud_texto  0.385 0.000 0.400
        priorizar_lista_entrenamiento_subordinados             > pedir_critica_anonima_curso_entrenamiento_dictado      bandeja similitud_texto  0.466 0.111 0.439
        priorizar_lista_entrenamiento_subordinados             > desarrollar_primer_curso_entrenamiento                 bandeja similitud_texto  0.411 0.143 0.401
        priorizar_lista_entrenamiento_subordinados             > reciclar_empleado_ascendido_mas_alla_capacidad         bandeja similitud_texto  0.355 0.000 0.384
        reciclar_empleado_ascendido_mas_alla_capacidad         > priorizar_lista_entrenamiento_subordinados             bandeja similitud_texto  0.355 0.000 0.416
        responder_primer_aviso_renuncia_subordinado            > preguntar_seguimiento_hallar_huecos                    grafo   paso_contra_nodo 0.190 0.000 0.627
        responder_primer_aviso_renuncia_subordinado            > usar_banco_nueve_preguntas_entrevista                  bandeja similitud_texto  0.386 0.000 0.458
        responder_primer_aviso_renuncia_subordinado            > gestionar_retencion_subordinado_valioso_renuncia       bandeja similitud_texto  0.378 0.250 0.450
        responder_primer_aviso_renuncia_subordinado            > entregar_evaluacion_desempeno_tres_claves              grafo   similitud_texto  0.418 0.000 0.408
        responder_primer_aviso_renuncia_subordinado            > construir_indicador_tendencia_patron                   grafo   similitud_texto  0.351 0.000 0.417
        responder_primer_aviso_renuncia_subordinado            > planificar_tres_pasos_demanda_estado_brecha            grafo   similitud_texto  0.363 0.000 0.409
        responder_primer_aviso_renuncia_subordinado            > pedir_critica_anonima_curso_entrenamiento_dictado      bandeja similitud_texto  0.395 0.000 0.389
        usar_banco_nueve_preguntas_entrevista                  > identificar_disparadores_propios_reaccion              grafo   paso_contra_nodo 0.175 0.000 0.607
        usar_banco_nueve_preguntas_entrevista                  > responder_primer_aviso_renuncia_subordinado            bandeja similitud_texto  0.394 0.000 0.458
        usar_banco_nueve_preguntas_entrevista                  > gestionar_retencion_subordinado_valioso_renuncia       bandeja similitud_texto  0.412 0.000 0.426
        usar_banco_nueve_preguntas_entrevista                  > entregar_evaluacion_desempeno_tres_claves              grafo   similitud_texto  0.369 0.000 0.422
        usar_banco_nueve_preguntas_entrevista                  > pedir_critica_anonima_curso_entrenamiento_dictado      bandeja similitud_texto  0.383 0.000 0.419
        usar_banco_nueve_preguntas_entrevista                  > planificar_tres_pasos_demanda_estado_brecha            grafo   similitud_texto  0.355 0.000 0.402
    filas de vecino: 29
    (3) pares sin orden | levantado desde
        desarrollar_primer_curso_entrenamiento                 ~ pedir_critica_anonima_curso_entrenamiento_dictado      tanda-tanda los dos
        desarrollar_primer_curso_entrenamiento                 ~ priorizar_lista_entrenamiento_subordinados             tanda-tanda los dos
        gestionar_retencion_subordinado_valioso_renuncia       ~ responder_primer_aviso_renuncia_subordinado            tanda-tanda los dos
        entregar_evaluacion_desempeno_tres_claves              ~ gestionar_retencion_subordinado_valioso_renuncia       con fuera   solo gestionar_retencion_subordinado_valioso_renuncia
        gestionar_retencion_subordinado_valioso_renuncia       ~ usar_banco_nueve_preguntas_entrevista                  tanda-tanda los dos
        gestionar_retencion_subordinado_valioso_renuncia       ~ pedir_critica_anonima_curso_entrenamiento_dictado      tanda-tanda solo pedir_critica_anonima_curso_entrenamiento_dictado
        pedir_critica_anonima_curso_entrenamiento_dictado      ~ priorizar_lista_entrenamiento_subordinados             tanda-tanda los dos
        pedir_critica_anonima_curso_entrenamiento_dictado      ~ usar_banco_nueve_preguntas_entrevista                  tanda-tanda los dos
        pedir_critica_anonima_curso_entrenamiento_dictado      ~ repartir_supervision_puesto_funcional_mision           con fuera   solo pedir_critica_anonima_curso_entrenamiento_dictado
        pedir_critica_anonima_curso_entrenamiento_dictado      ~ responder_primer_aviso_renuncia_subordinado            tanda-tanda los dos
        entregar_evaluacion_desempeno_tres_claves              ~ pedir_critica_anonima_curso_entrenamiento_dictado      con fuera   solo pedir_critica_anonima_curso_entrenamiento_dictado
        priorizar_lista_entrenamiento_subordinados             ~ reciclar_empleado_ascendido_mas_alla_capacidad         tanda-tanda los dos
        preguntar_seguimiento_hallar_huecos                    ~ responder_primer_aviso_renuncia_subordinado            con fuera   solo responder_primer_aviso_renuncia_subordinado
        responder_primer_aviso_renuncia_subordinado            ~ usar_banco_nueve_preguntas_entrevista                  tanda-tanda los dos
        entregar_evaluacion_desempeno_tres_claves              ~ responder_primer_aviso_renuncia_subordinado            con fuera   solo responder_primer_aviso_renuncia_subordinado
        construir_indicador_tendencia_patron                   ~ responder_primer_aviso_renuncia_subordinado            con fuera   solo responder_primer_aviso_renuncia_subordinado
        planificar_tres_pasos_demanda_estado_brecha            ~ responder_primer_aviso_renuncia_subordinado            con fuera   solo responder_primer_aviso_renuncia_subordinado
        identificar_disparadores_propios_reaccion              ~ usar_banco_nueve_preguntas_entrevista                  con fuera   solo usar_banco_nueve_preguntas_entrevista
        entregar_evaluacion_desempeno_tres_claves              ~ usar_banco_nueve_preguntas_entrevista                  con fuera   solo usar_banco_nueve_preguntas_entrevista
        planificar_tres_pasos_demanda_estado_brecha            ~ usar_banco_nueve_preguntas_entrevista                  con fuera   solo usar_banco_nueve_preguntas_entrevista
    pares sin orden: 20 | {'tanda-tanda': 10, 'con fuera': 10} | suma: 20

**LECTURA:**

1. **Las `7` dan `29` filas de vecino en `20` pares sin orden**, `10` entre dos de la tanda y `10` con uno de fuera, todos del
   grafo. **Coincide con los *29 pares* y las *29 lineas de veredicto* del asunto de `4ab7ff52`**, que ahi llama *pares* a mis
   filas, como en la `68` y la `71`; y lo digo como coincidencia.
2. **Todas levantan a alguien**, y **todo lo levanta `similitud_texto`** entre `0,351` y `0,472`, salvo dos por
   `paso_contra_nodo` (`0,627` y `0,607`) sobre la forma *pregunta*: `preguntar_seguimiento_hallar_huecos` de Scott y
   `identificar_disparadores_propios_reaccion` de Zhuo.
3. **Los seis pares dentro de un capitulo los levanta todos, y desde los dos lados**: los tres de la cadena de `cap_17` y los
   tres de `cap_15`. **Ninguna pieza del libro queda sin su par por falta de senial.**
4. **Los de fuera son todos del grafo y por prosa**: de Grove, `entregar_evaluacion_desempeno_tres_claves` (`cap_14`, levantada
   por cuatro de las `7`), `repartir_supervision_puesto_funcional_mision`, `construir_indicador_tendencia_patron` y
   `planificar_tres_pasos_demanda_estado_brecha`; y los dos de otros libros del punto `2`. **Ninguno de las bandejas de Gerber o
   Marquet.**
5. **`D.36`, lo que un solo lado levanta dentro de la tanda:** `pedir_critica` levanta a `gestionar_retencion` y no al reves. Va
   a la seccion `7`, y no obliga.

**EL RELOJ, medido y no techo:** de las `02:44:03` a las `03:07:01` del 26, con fichas de estos segundos (la menor y la mayor):

    $ grep "rc=" .v73aud/barrido.log | sed 's/.*segundos=//' | sort -n | sed -n '1p;$p'
    596
    1090

## 5. **MI LECTURA CIEGA DE LOS PARES** (`1.2`, `6.1`, y solo la vara `6.1`)

**Leidos con los pasos de los dos delante**, todos con `pasos_ciego.py` (`R6`): `.v73aud/pasos_siete.txt` para las `7`, y
`.v73aud/pasos_fuera_a.txt` y `.v73aud/pasos_fuera_b.txt` para los de fuera. **Una fila por par** en `.v73aud/mis_clases.tsv`,
con su razon. **De donde sale cada fila:** los pares de dentro de un mismo capitulo (`6`, los tres de `cap_15` y los tres de
`cap_17`) los escribi **todos antes de que el barrido terminara**, en `.v73aud/clases_intra.txt`; los de entre capitulos y los
de fuera, al recogerlo, en `.v73aud/clases_fuera.txt`. `armar_clases.py` los junta, y el cruce comprueba que cada par del
barrido tiene su fila y cada fila su par:

    $ python .v73aud/armar_clases.py
    pares del barrido: 20 | filas escritas: 20 | sin clase: 0 []
    de donde sale cada fila: {'intra': 6, 'fuera': 14} | suma: 20
    filas de clases_intra.txt: 6 | por el barrido: {'levantada': 6} | suma: 6
    $ python .v73aud/cruce_clases.py
    pares del barrido: 20 | filas de clase: 20
    pares sin fila: []
    filas sin par: []
    clases: {'CONTINUA': 4, 'SANO': 16} | suma: 20
    con DUDA escrita: 2
      CONTINUA  desarrollar_primer_curso_entrenamiento ~ pedir_critica_anonima_curso_entrenamiento_dictado | madre desarrollar_primer_curso_entrenamiento
      CONTINUA  priorizar_lista_entrenamiento_subordinados ~ desarrollar_primer_curso_entrenamiento | madre priorizar_lista_entrenamiento_subordinados
      CONTINUA  responder_primer_aviso_renuncia_subordinado ~ gestionar_retencion_subordinado_valioso_renuncia | madre responder_primer_aviso_renuncia_subordinado
      CONTINUA  priorizar_lista_entrenamiento_subordinados ~ pedir_critica_anonima_curso_entrenamiento_dictado | madre priorizar_lista_entrenamiento_subordinados

**El par de `cap_15` que el encargo manda mirar con direccion**, con los pasos de los dos delante:

    $ python .v67aud/normal/pasos_ciego.py responder_primer_aviso_renuncia_subordinado gestionar_retencion_subordinado_valioso_renuncia
    ===== responder_primer_aviso_renuncia_subordinado | cuarentena\grove_high_output\responder_primer_aviso_renuncia_subordinado.json
      titulo: Responder al primer momento en que un subordinado valioso avisa que quiere renunciar: dejar lo que haces, escucharlo sin discutir y comprarte tiempo antes de actuar
      fuente: ['grove_high_output']
      cond: Cuando un subordinado valioso y estimado se acerca al mando y anuncia, de pasada, que ha decidido dejar la empresa.
      P1. Deja lo que estas haciendo en cuanto el subordinado te avisa de que quiere renunciar, en vez de posponer la conversacion para mas tarde.
      P2. Sientalo y preguntale por que se va.
      P3. Dejalo hablar sin discutir nada de lo que diga, aunque sus razones no te parezcan buenas.
      P4. Cuando haya terminado de exponer sus razones, hazle mas preguntas para que los asuntos de fondo puedan salir a la luz.
      P5. No discutas, no sermonees y no entres en panico durante esta primera conversacion.
      P6. No intentes cambiarle la idea en este momento, sino compra tiempo: cuando haya dicho todo lo que tiene que decir, pide el tiempo que necesites para prepararte para el siguiente encuentro.
      P7. Cumple despues con lo que te hayas comprometido a hacer en esta primera conversacion.
    ===== gestionar_retencion_subordinado_valioso_renuncia | cuarentena\grove_high_output\gestionar_retencion_subordinado_valioso_renuncia.json
      titulo: Gestionar la retencion de un subordinado valioso tras su primer aviso de renuncia: escalar al propio jefe, perseguir cada via para conservarlo y volver con una solucion a sus razones reales
      fuente: ['grove_high_output']
      cond: Cuando, tras la primera conversacion en la que un subordinado valioso anuncio que queria renunciar, el mando tiene que buscarle una salida que lo retenga en la empresa.
      P1. Lleva el problema a tu propio jefe en busca de ayuda y consejo y, aunque el tambien intente posponerlo, haz que sea problema suyo y que participe de la solucion.
      P2. Persigue con energia cada via disponible para retener al subordinado en la empresa, incluida la de transferirlo a otro departamento.
      P3. Si la transferencia parece la salida mas probable, asume tu mismo el papel de gestor de ese proyecto hasta que quede resuelto del todo.
      P4. Vuelve al subordinado con una solucion que atienda sus razones reales para querer irse y que ademas beneficie a la empresa.
      P5. Haz que se sienta comodo con el nuevo arreglo; puedes decirle algo como que no les arranco por chantaje nada que no debieran haber hecho igual, que al estar a punto de irse les hizo ver su error, y que solo hacen lo que debieron hacer sin que pasara nada de esto.
      P6. Si el subordinado dice que ya acepto un puesto en otra empresa, hazle ver que tiene dos compromisos distintos, uno con un futuro empleador que apenas conoce y otro contigo y con la gente con la que trabaja a diario, y que el segundo pesa mas.

**LECTURA, los cuatro `CONTINUA`**, y en los cuatro el hijo trae procedimiento propio y ningun paso del otro, asi que ninguno es
`REPITE`:

- `responder_primer_aviso_renuncia_subordinado` madre de `gestionar_retencion_subordinado_valioso_renuncia`: la condicion del
  hijo es la madre hecha (*tras la primera conversacion*), L113 encadena con palabras (*What's your next move?*), y la madre
  compra el tiempo (paso `6`) y promete cumplir (paso `7`) para lo que el hijo ejecuta.
- `priorizar_lista_entrenamiento_subordinados` madre de `desarrollar_primer_curso_entrenamiento`: el hijo arranca del tema mas
  urgente de la lista priorizada (L51 y L53).
- `desarrollar_primer_curso_entrenamiento` madre de `pedir_critica_anonima_curso_entrenamiento_dictado`: la condicion del hijo
  es el curso dictado (L61); la critica de la madre (paso `6`, los mas informados durante la vuelta desechable) y el formulario
  anonimo del hijo son otro publico, otro instrumento y otro momento.
- `priorizar_lista_entrenamiento_subordinados` madre de `pedir_critica_anonima_curso_entrenamiento_dictado`, por la cadena.

**Los tres de `cap_17` son los tres de la `ACTA 60` `60.5`, con la misma madre en cada uno: mi lectura de hoy no difiere.**

**MIS DOS DUDAS, escritas antes de saber, y si alguna me cae, cae dentro de lo que marco aqui:**

- **`responder` con `gestionar` puede leerse `SANO` de dos fases hermanas** de una misma pieza (*I Quit!*, L105 a L123), que
  ninguna cabeza enumera. Lo leo `CONTINUA` por la condicion del hijo y por el *next move* de L113.
- **`priorizar` con `pedir_critica` puede leerse `SANO`**: la condicion del hijo es el producto de `desarrollar`, no el de
  `priorizar`, que par a par es su abuela; es la figura que en mi fase ciega de la `71` deje `SANO` (`definir_entorno` con
  `cerrar_brecha`). Lo dejo `CONTINUA` porque la `60.5` lo adjudico asi con la vara y mi lectura no lo contradice, solo lo afina.

**Los `16` `SANO`** comparten la forma *pregunta*, la conversacion con un subordinado o palabras sueltas (*curso*, *formado*,
*debilidad*), y ningun paso. **El mas cercano es `entregar_evaluacion_desempeno_tres_claves` con `responder_primer_aviso`**:
las dos piden escuchar al subordinado, pero una es franqueza y comprobar que el mensaje llego, y la otra es callar, preguntar y
comprar tiempo; hay procedimiento en los dos lados fuera del solape (`6.1`, sin bascula).

## 6. **LAS ARISTAS POR LECTURA** (`D.29`, `D.37`, `D.53`)

**Las que mi lectura sostiene o descarta**, una fila cada una en `.v73aud/aristas_lectura.tsv`, con su tramo de madre, de hijo
y su linea del libro, **escritas antes de que el barrido terminara**, **mirando tambien madres que viven en el grafo y en otras
bandejas** (la busqueda por asunto, abajo). El cruce dice si el barrido levanto el par y donde vive hoy cada extremo:

    $ python .v73aud/cruce_aristas.py
    SOSTENGO D.29, DUDA responder_primer_aviso_renuncia_subordinado        (bandeja) > gestionar_retencion_subordinado_valioso_renuncia       (bandeja) | levantado por el barrido: SI
    SOSTENGO D.29  priorizar_lista_entrenamiento_subordinados         (bandeja) > desarrollar_primer_curso_entrenamiento                 (bandeja) | levantado por el barrido: SI
    SOSTENGO D.29  desarrollar_primer_curso_entrenamiento             (bandeja) > pedir_critica_anonima_curso_entrenamiento_dictado      (bandeja) | levantado por el barrido: SI
    SOSTENGO D.29, DUDA priorizar_lista_entrenamiento_subordinados         (bandeja) > pedir_critica_anonima_curso_entrenamiento_dictado      (bandeja) | levantado por el barrido: SI
    NO             usar_banco_nueve_preguntas_entrevista              (bandeja) > preparar_preguntas_entrevista_antemano                 (grafo) | levantado por el barrido: no
    NO             gestionar_retencion_subordinado_valioso_renuncia   (bandeja) > practicar_franqueza_radical_jefe_propio                (grafo) | levantado por el barrido: no
    NO             priorizar_lista_entrenamiento_subordinados         (bandeja) > identificar_temas_formacion_tarjetas_decision          (NINGUNA) | levantado por el barrido: no
    NO             desarrollar_primer_curso_entrenamiento             (bandeja) > aprovechar_formacion_reglada                           (grafo) | levantado por el barrido: no
    NO             reciclar_empleado_ascendido_mas_alla_capacidad     (bandeja) > calibrar_ascensos_evitar_politica                      (grafo) | levantado por el barrido: no
    filas: 9 | por lo que queda: {'SOSTENGO': 4, 'NO': 5} | suma: 9
    filas con DUDA escrita: 2 de 9
    por el barrido: {'levantada': 4, 'no levantada': 5} | suma: 9

(**El hueco del cruce, dicho:** solo conoce el grafo y la bandeja de Grove, y por eso pone `NINGUNA` a
`identificar_temas_formacion_tarjetas_decision`, que vive en la de Marquet; lo dice la busqueda de abajo.)

**La busqueda por asunto, y las partes de los dos titulos de la tanda que dicen cuantas tienen** (*el primer curso en siete
pasos*, *el banco de nueve preguntas*), por id y titulo sobre grafo mas bandejas:

    $ python .v73aud/temas.py | tee .v73aud/temas.txt | grep -v "^    "
    poblacion: 479 | por sede: grafo 430, bandeja 49 | suma: 479
    la entrevista a un candidato: 49
    la renuncia y la retencion: 5
    el ascenso y el reciclaje: 6
    el entrenamiento: 25
    la critica y la retroalimentacion del curso: 3
    el jefe del mando como ayuda: 2
    curso en siete pasos: el calendario: 6
    curso en siete pasos: el esquema: 0
    curso en siete pasos: los instructores: 1
    nueve preguntas: debilidades, logros, fracasos: 4

(La salida entera, un id por linea con su sede y su libro, en `.v73aud/temas.txt`.)

**LECTURA:**

- **MIS CUATRO `SOSTENGO` LOS LEVANTA EL BARRIDO, ASI QUE NO SON ARISTAS POR LECTURA: SON LAS CUATRO LINEAS `CONTINUA` DE LA
  SECCION `5`** (`D.53`), y **la tanda deja, por mi lectura, `4` aristas, todas con los dos extremos en la tanda y ninguna por
  lectura.** **El asunto de `4ab7ff52` dice *3 aristas esperadas*: si es la misma cosa, difiere de mi cuenta en una, y mis dos
  dudas de la seccion `5` son justo donde puede estar.** Lo cruzo par a par en mi turno normal, sin decidir aqui cual.
- **`D.37` NO DISPARA en ninguna**: los dos titulos que dicen cuantas partes tienen las enumeran **como sus propios pasos**
  (las siete etapas del curso, L53 a L59; las nueve preguntas, L39 a L55), y **ninguna parte existe como nodo**: lo que la
  busqueda levanta por *calendario*, *instructor*, *debilidad*, *logro* o *fracaso* es la propia ficha u otras doctrinas de
  otros libros. `pedir_critica` no es la octava etapa: L61 empieza *After you've given the course*, fuera de la serie.
- **Ninguna madre del grafo ni de otra bandeja para las `7`**, por mi lectura: los bancos de preguntas de Zhuo y de Smart, la
  franqueza con el propio jefe de Scott, la formacion reglada y el jefe entrenador de Zhuo, las tarjetas de formacion de Marquet
  y los ascensos de Scott y Smart **son otras doctrinas** (`6.1`, dos doctrinas legitimas no son madre e hija), y ninguna es la
  condicion de una de las `7` ni la remite con palabras. Los cinco `NO` de la tabla son los que lei con los pasos delante
  (`.v73aud/pasos_fuera_a.txt`); el resto de lo que la busqueda levanta comparte solo la palabra.
- **`cap_16` no tiene ni par ni arista**: `reciclar_empleado_ascendido_mas_alla_capacidad` solo levanta a `priorizar`, `SANO`.

## 7. **EL ORDEN QUE MI LECTURA OBLIGA** (`D.36`)

**No es un orden: son las restricciones**, escritas antes de ver el del extractor. Madre antes que hijo por mis `CONTINUA` y mis
`SOSTENGO` con los dos extremos en la tanda, y cuantas cumple el orden de pieza del libro, **que saco de mi fidelidad**
(capitulo y primera linea), porque `.v73aud/los7.txt` va alfabetica:

    $ python .v73aud/restricciones_orden.py
    orden de pieza del libro (capitulo y primera linea de mi fidelidad): 7
       1 cap_15 L39 usar_banco_nueve_preguntas_entrevista
       2 cap_15 L111 responder_primer_aviso_renuncia_subordinado
       3 cap_15 L113 gestionar_retencion_subordinado_valioso_renuncia
       4 cap_16 L49 reciclar_empleado_ascendido_mas_alla_capacidad
       5 cap_17 L49 priorizar_lista_entrenamiento_subordinados
       6 cap_17 L53 desarrollar_primer_curso_entrenamiento
       7 cap_17 L61 pedir_critica_anonima_curso_entrenamiento_dictado
    restricciones: 5
      desarrollar_primer_curso_entrenamiento                     antes que pedir_critica_anonima_curso_entrenamiento_dictado            CONTINUA               el orden del libro la cumple
      priorizar_lista_entrenamiento_subordinados                 antes que desarrollar_primer_curso_entrenamiento                       CONTINUA               el orden del libro la cumple
      responder_primer_aviso_renuncia_subordinado                antes que gestionar_retencion_subordinado_valioso_renuncia             CONTINUA               el orden del libro la cumple
      priorizar_lista_entrenamiento_subordinados                 antes que pedir_critica_anonima_curso_entrenamiento_dictado            CONTINUA               el orden del libro la cumple
      gestionar_retencion_subordinado_valioso_renuncia           antes que pedir_critica_anonima_curso_entrenamiento_dictado            D.36, solo lo levanta pedir_critica_anonima_curso_entrenamiento_dictado el orden del libro la cumple
    que obligan (madre antes que hijo): 4 | violadas por el orden del libro: 0
    D.36 de un solo lado, informativas: 1

**LECTURA:** las cuatro que obligan (`responder` antes que `gestionar`, `priorizar` antes que sus dos hijas y `desarrollar` antes
que `pedir_critica`) **las cumple ya el orden de pieza del libro**. La `D.36` de un solo lado es informativa y **no obliga**,
porque la aduana de `insertar` mide grafo mas bandejas (`D.38.5`); y tambien la cumple. **Su orden, contra estas cuatro, lo
compruebo en mi turno normal.**

## 8. **`R8` MEDIDO SOBRE MI ENCARGO DE LA `73`, CON EL MISMO INSTRUMENTO** (`ACTA 71` `71.11`)

`R8` dice: *toda cifra de medida que escriba en `PROMPT_SIGUIENTE.md` (un reloj, una banda, una cuenta sacada de un fichero)
va DENTRO de un bloque `$` con su salida, o lleva EN SU MISMA LINEA la seccion del acta donde esta pegada: ni la seccion de la
linea de al lado, ni una ruta de fichero*. Que el fichero es el encargo que escribi al cerrar la `ACTA 71`, y el instrumento
de la `71.12` corrido sin copiarlo, con su salida de hoy contra la que guardo aquella acta:

    $ head -1 docs/loop/PROMPT_SIGUIENTE.md | cut -c1-100; ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, $7, $9}'
    # ENCARGO DE LA VUELTA 73: **LAS ULTIMAS FICHAS DE GROVE (`cap_15`, `cap_16` Y `cap_17`) DEJADAS LIS
    2026-09-26 01:47:33.720687500 docs/loop/PROMPT_SIGUIENTE.md
    $ python .v72aud/normal/r8_encargo73.py | diff - .v72aud/normal/r8_encargo73.txt && echo "IDENTICO a .v72aud/normal/r8_encargo73.txt, la salida de la ACTA 71 71.12"; python .v72aud/normal/r8_encargo73.py | tail -1
    IDENTICO a .v72aud/normal/r8_encargo73.txt, la salida de la ACTA 71 71.12
    lineas del encargo: {'linea de bloque sangrado': 9, 'prosa con digito, con seccion de la ACTA 71': 11, 'prosa con digito, sin seccion de la ACTA 71': 48, 'prosa sin digito': 62} | suma: 130

(Las `48` lineas sin seccion, cada una con sus numeros, en `.v73aud/r8_encargo73.txt`.) **LECTURA, grupo a grupo, que es mia y
no del instrumento; las volvi a leer una a una y no copio la de la `71.12`, aunque llego al mismo reparto:**

- **Numeros de vuelta, de acta, de rama o de carpeta de la casa**: `L1`, `L3`, `L17`, `L19`, `L25`, `L47`, `L63`, `L66`, `L71`,
  `L77`, `L78`, `L80`, `L85`, `L87`, `L88`, `L95`, `L103`, `L106`, `L109`, `L110`, `L113`.
- **Secciones, reglas, deudas y numeros de tarea o de punto**: `L4`, `L14`, `L18`, `L42`, `L43`, `L49`, `L59`, `L65`, `L69`,
  `L70`, `L72`, `L73`, `L75`, `L82`, `L84`, `L86`, `L94`, `L101`, `L108`, `L122`.
- **Identificadores de capitulo o de paso** (`cap_15` a `cap_18`, los pasos `3` y `5` de `d078`): `L61`, `L67`, `L89`, `L93`,
  `L97`, y los `15`, `16` y `17` de `L1`.
- **Una fecha**: `L22` (el `23` sep). **Un umbral de regla**: el `10` por ciento de `D.58` en `L72`.
- **Las cifras de medida** estan dentro de un bloque `$` (el reloj del barrido de la `71`, en `L28` a `L30`; la clase y el
  tablero, en `L34` a `L40`), o llevan su seccion en la misma linea: `L16`, `L53` a `L57`, `L62`, `L79`, `L104`, `L125`
  (secciones `71.x`) y `L90` (`60.5`, de la `ACTA 60`).

**EL INSTRUMENTO NO VE LAS CUENTAS EN LETRA**, y la `71.12` dijo que tambien le tocan (*donde el encargo dice una cuenta en letra
..., la seccion que la sostiene va en la misma linea*). Las busco con un `grep` sobre las palabras de numero:

    $ grep -n -i -w -E "dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|veinte|cero" docs/loop/PROMPT_SIGUIENTE.md | cut -c1-150
    21:**PUEDES LANZAR BARRIDOS DE FONDO, CINCO A LA VEZ COMO MUCHO, PERO NINGUNO VIVO AL CERRAR TU TURNO**: los recoges todos dentro,
    22:vigilandolos si tardan. **Si no te caben, no los lances: lo dices en el reporte con los que faltan.** El `23` sep tres asientos
    25:**EL RELOJ, MEDIDO, Y NO ES UN TECHO: ES LO QUE COSTO.** El barrido de la `71`, cinco fichas a la vez, por ficha y ordenado por
    54:| **Tus seis discutibles se sostienen**, `D72.1` a `D72.6` | `71.5` |
    55:| **La muestra de los SANO se sostiene entera**; lo que entro lleva cero PUENTE en los seis capitulos | `71.5`, `71.4` |
    56:| **Cero caidas tuyas, ni de prosa**, y `R5` cumplido | `71.2`, `71.0` |
    62:pasos trae cada una estan en la `ACTA 71` `71.1`, bloque de `.v72aud/normal/siete.py`**, y tu primera medida es volver a correrlo.
    71:3. **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo, tres filas**, por una copia de `.v71ext/contar_fidelidad.py`, **y el
    78:la ruta `.v73ext/`: **cinco a la vez como mucho, un log con su `INICIO` y su `TODOS TERMINADOS`, y todas recogidas dentro de tu
    85:   `.v71ext/veredictos_listos.txt`: **leidos con los pasos de los dos delante** (`python .v64aud/pasos.py <a> <b>`) y por la vara
    90:   citas**: la `ACTA 60` `60.5` adjudico **`CONTINUA`** los tres pares de su cadena (`priorizar_lista_entrenamiento_subordinados`
    95:3. **El orden de insercion**, con una copia de `.v71ext/orden.py`: **madre antes que hijo, `D.36`, y las comprobaciones en cero.**
    105:- **`PASOS INVENTADOS POR CAPITULO`, tres filas**, que son **preparacion y no entrada**.
    129:**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No

**LECTURA, linea a linea:** `L21` y `L78` (*cinco a la vez como mucho*) y `L25` (*cinco fichas a la vez*, el parametro de
`barrer.sh`) son **la regla del turno y el metodo**, no medida; `L95` y `L129` (*en cero*) son **la meta que se pide**; `L85`
(*los dos*) son **los dos nodos del par**; `L62` la levanta la palabra *siete* de `siete.py`, **un nombre de fichero**, y
lleva `71.1` en la misma linea; `L54`, `L55`, `L56` y `L90` llevan su seccion en la misma linea. `L22` (*el `23` sep
tres asientos cerraron ...*) es **la advertencia del arnes copiada**: la misma frase esta en el prompt que el arnes me da en este
turno, y no es una cuenta mia sacada de un fichero.

**LA QUE DEJO A LA VISTA:** `L71` y `L105` dicen *`PASOS INVENTADOS POR CAPITULO`, (una fila por capitulo,) tres filas*, sin
seccion en su linea; la mas cercana, `71.1`, esta en `L62` y en `L104`, **las lineas de al lado**. **Mi lectura: no es una cifra
de medida, es aritmetica de la propia pagina**: el tamaño de la tabla que se pide, una fila por cada uno de los tres
capitulos que el mismo encargo nombra por su identificador en `L1` y en `L61`, y se comprueba leyendo la pagina, no abriendo un
fichero. **La lectura contraria, escrita para que se juzgue:** el numero de capitulos que quedan en la bandeja es una cuenta de la
bandeja, de la misma familia que *las `7` fichas* que mi fase ciega de la `72` cargo como rotura; **si esa lectura gana, `R8` se
rompe por tercera vez y `AUDITOR` pasa de `2 de 3` a `3 de 3`, que es parada** (`5.4`). **La cifra es cierta** (el bloque de
`siete.py` de la seccion `2` trae tres capitulos), y **no la adjudico yo a mi favor en esta fase**: la llevo a mi turno normal y
la escribo en el acta con esta lectura y su contraria delante (seccion `9`, punto `8`).

## 9. **LO QUE DEJO PARA MI TURNO NORMAL, ESCRITO ANTES DE VER EL REPORTE**

1. **`R5`** en su reporte, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` sacados otra vez de los originales y
   con la cabecera cambiada a la `73`.
2. **El censo con su hash**: que la vuelta no movio el grafo, la bitacora, los censos ni las bandejas de Gerber y Marquet, y
   que en la de Grove solo cambiaron las `4` fichas corregidas, **con `git diff`**, que es lo que en esta fase no he medido.
3. **Mi fidelidad contra la suya, paso a paso**: `42` filas mias contra las suyas, y sus `6` correcciones contra mi lectura de
   sus textos viejos (seccion `3`): cinco `P` y el paso `5` de `gestionar_retencion`, que yo habria leido `D`. **Si el marca
   PUENTE un paso de hoy que yo lei `T` sin duda, y gana, la caida de lectura es mia.**
4. **Mis clases contra sus lineas de veredicto, par a par**, y mis aristas por lectura contra las suyas, por par y no por cuenta
   (secciones `5` y `6`).
5. **Su orden contra mis restricciones** (seccion `7`).
6. **La huella de las `7` fichas** que su cierre dice sellar, contra las mias de `.v73aud/huellas_al_barrer.txt`, tomadas antes de
   barrer y comprobadas al recoger.
7. **La muestra pineada de los SANO**: esta vuelta no escribe en la bitacora; los `SANO` de las `7` se muestrean cuando entren.
8. **`R8`, la lectura de `L71` y `L105`** (seccion `8`), adjudicada en el acta con su contraria delante; **y `R8` sobre el
   encargo de la `74`**, medido antes de cerrarlo, con las cuentas en letra incluidas esta vez.

## 10. **ESTA PAGINA CONTRA `R6`, `R7` Y LOS GUIONES, MEDIDA SOBRE ELLA MISMA**

El generador corre dos veces, y estos bloques de la segunda pasada leen la pagina que escribio la primera, identica salvo
estos bloques. El primero cuenta las lineas de bloque `$` que empiezan por una clave de relacion; el segundo, con la copia de
`.v70aud/r7_pagina.py`, cuenta las lineas de bloque que reparten una cifra en clases y cuantas traen su `suma`; el tercero
cuenta guiones largos y medios:

    $ grep -c -E "^    +(previos|siguientes|nodos_previos|nodos_siguientes)" docs/loop/APERTURA_CIEGA.md
    0
    $ python .v73aud/r7_pagina.py
    lineas de bloque que reparten en clases: 11 | por estado: {'con suma': 11} | suma: 11
    $ grep -c -P "\x{2014}|\x{2013}" docs/loop/APERTURA_CIEGA.md
    0
