# APERTURA CIEGA DE LA VUELTA 70, lote 7 (`grove_high_output`), **CLASE INSERCION**

*Auditor `claude-opus-5-5`, fase ciega, 25 sep 2026, la que el arnes numera `VUELTA 6` en la corrida que arranco el
23 a las `21:50`. Linea **serial**, rama `extraccion-mundo-11`. Modo austero (`D.47`). Todo lo de esta pagina sale de
`.v70aud/`, escrito y corrido en esta fase; cada bloque `$` lo pega `.v70aud/generar_apertura.py` corriendo el
comando en el momento de escribirla. **No hay ninguna tabla en esta pagina**, a proposito, como en la `66`, la `68` y la
`69`. **En esta fase no corro `git`** (ni `log`, ni `diff`, ni `status`, ni `hash-object`): mido el arbol por sus
ficheros, sus huellas y sus fechas, y donde eso no alcanza lo digo como limitacion.*

## 0. **LA HERENCIA** (`D.40`)

ACTA ANTERIOR LEIDA: a2ad919527f64c4aefe1fee58278246df8191c74

**Y esta vez la compruebo sin git**: es el blob de `docs/loop/ACTA_AUDITOR.md` tal como esta hoy en el arbol,
calculado a mano como lo calcula git, con los finales de linea pasados a LF como manda `.gitattributes`. Tal cual no
cuadra y normalizado si, y lo pego las dos cosas para que se vea por que. La `ACTA 68` la lei entera, de su linea de
cabecera a la ultima del fichero:

    $ python .v70aud/huella_acta.py
    sha1 del blob tal cual: 4ea9ba4e6b7808fb8e078d5a6f4955dbf18fae4f
    lineas con CRLF en el arbol: 395 | sha1 del blob normalizado a LF: a2ad919527f64c4aefe1fee58278246df8191c74
    lineas del fichero: 47722 | la ACTA 68 empieza en la linea: [47401]

HEREDADO 1: NO APLICA en esta fase. **Motivo:** `R5` es un remedio **del extractor** y se mide **sobre su
reporte de la `70`** (`ACTA 68` `68.12`: *el reporte de la `70`, con `.v64ext/pegado64.py` y
`.v64aud/normal/bloques_mudos.py`, los dos con la cabecera del tramo cambiada a la `70`*), y el reporte **no esta
en el arbol**: el arnes lo retiro para esta fase (`D.34.2`) y no lo he recuperado por ninguna via. **Se mide en mi
turno normal**, con los dos instrumentos sacados otra vez de los originales y no de sus copias. Lo que si esta en mi
mano lo cumplo en mi pagina: cada bloque `$` lleva la salida del comando que abre, y nada mas.

    $ ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl
    ls: cannot access 'docs/loop/REPORTE.md': No such file or directory
    ls: cannot access 'docs/loop/ultimo_extractor.json': No such file or directory
    ls: cannot access 'docs/loop/ultimo_auditor.json': No such file or directory
    ls: cannot access 'docs/loop/CREDITO_serial.jsonl': No such file or directory
    $ grep -n "VUELTA 6 : APERTURA CIEGA" docs/loop/loop.log | tail -1
    6523:[2026-09-25 16:05:36] VUELTA 6 : APERTURA CIEGA (claude-opus-5-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl

HEREDADO 2: CUMPLIDO. **`R6`, mio** (`ACTA 68` `68.12`): en esta fase los pasos de cualquier nodo los imprime
`.v67aud/normal/pasos_ciego.py`, que no enseña `previos` ni `siguientes`, y **el unico bloque de pasos de esta pagina lo
corre** (seccion `5`). Ningun instrumento mio de esta fase nombra esas claves:

    $ grep -l -E "previos|siguientes" .v70aud/*.py | wc -l
    0

**Y DIGO LO UNICO QUE SE ACERCA, para que se juzgue:** `.v70aud/grafo_sin_tanda.py` (seccion `2`) quita los ids de las
`20` de **cualquier lista** de los nodos viejos, sin nombrar ninguna clave, para reconstruir el grafo que barri en la
`68`, y **cuenta** cuantos nodos viejos tenian alguno. **No imprime ninguna clave ni ningun id de relacion**: una cuenta y
un `SI` o un `NO`. Es la misma cuenta que la `67` publico sacandola de `git` (*reescritos solo en claves de relacion*), y
como alli es **cuenta y no identidad**: que nodos son lo miro en el turno normal. El cumplimiento de la pagina entera lo
mide un `grep` sobre ella al cerrarla (seccion `7`).

HEREDADO 3: CUMPLIDO. **`R7`, mio** (`ACTA 68` `68.12`): toda linea de esta pagina que reparte un total en clases la
imprime un instrumento que cuenta **todas** las clases con el mismo predicado y **dice su `suma`**: los nuevos de
`.v70aud/` la traen desde que nacen (`huellas_hoy.py`, `entra_lo_leido.py`, `esperado_70.py`, `clasificacion_20.py`), y
los que reuso de la `69` ya la traian (`poblacion.py`, `aristas_70.py`). **Medido sobre la pagina misma** en la
seccion `7`, con `.v70aud/r7_pagina.py`.

## 1. **LO QUE VI SIN BUSCARLO, Y LO DIGO ANTES DE MEDIR** (`d146`)

**La foto de `git status` que el entorno me pone delante trae los asuntos de los cinco ultimos commits del extractor,
y tres traen sus conclusiones de esta vuelta**, que lei antes de leer nada:

- `6c40696` *Vuelta 70, T3 a T5: las 20 filas de cap_05 y cap_06 dentro, 7 de 7 aristas en el grafo, censo
  410/1027/1/27/65, 0 de 84 y 0 de 62, guardas en verde*;
- `4a10a65` *Vuelta 70: el cierre estricto en verde y la tabla de tareas al cerrar*;
- `d58cd8c` *Vuelta 70, fila 20: decidir_nivel_competente_inferior insertado por la aduana, movido a _insertados*;
- y `a34a1f7` y `cfcbbb6`, sin cifras (*fila 20: su fila en el reporte* y *la salida del hook del cierre*).

**Tambien lei la cola de `docs/loop/loop.log`**, que no se retira (el turno del extractor, su coste y su duracion), **mi
propio encargo** (`docs/loop/PROMPT_SIGUIENTE.md`, que es mio) y, para calcular la huella, `.gitattributes`; y busque con
`grep` una clave de fin de linea en el fichero `.git/config` **leyendolo como texto**, sin correr git, y no salio nada. Es
el mismo hueco de `d146` que declararon las aperturas de la `65` a la `69`, y no lo arreglo yo (`D.45`).

**LO QUE ESO LE HACE A ESTA PAGINA, SIN REBAJARLO:**

1. **Mis clases de la tanda no las decido hoy**: son las de mis ficheros sellados de la `68` (`.v68aud/mis_clases.tsv` y
   `.v68aud/aristas_lectura.tsv`), que la conjunta de la `69` dejo iguales en los `70` pares (`ACTA 68` `68.3`), mas la
   unica correccion que yo mismo adjudique en la `ACTA 67` `67.4.d`, declarada dentro de `.v69aud/aristas_70.py`.
2. **Ninguna cifra de esta pagina sale de esos asuntos**; todas salen de un instrumento corrido en esta fase, y **donde
   coinciden lo digo como coincidencia y no como fuente**.
3. **No he abierto nada de `.v70ext/`, `.v69ext/` ni `.v68ext/`**, ni `bitacora/VEREDICTOS.jsonl` por dentro: de ella solo
   cuento lineas.
4. **Lo que `d58cd8c` quiere decir con *insertado por la aduana* no lo se**, y no lo adivino: lo leo en el reporte.

## 2. **EL CENSO, Y QUE LA POBLACION DE LA ADUANA ES LA DE MI BARRIDO DE LA `68`** (`D.38.4`, `D.38.5`)

La vuelta es **de insercion** (mi encargo, seccion `0`): las `20` filas de `cap_05` y `cap_06`, una por vez.

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        410 dataset/nodos.jsonl
       1027 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1438 total
    $ ls cuarentena/grove_high_output/*.json | wc -l
    27
    $ ls cuarentena/_insertados/grove_high_output/*.json | wc -l
    65
    $ ls cuarentena/gerber_emyth/*.json cuarentena/marquet_turn_the_ship/*.json | wc -l
    42
    $ ls -A procesos/ | wc -l
    0
    $ python forja.py gate | head -2
    GATE VERDE.
      nodos verificados: 410

**Sin `git`, lo que cambio desde mi barrido de la `68`, por tres instrumentos.** Primero, **cualquier fichero** del dato,
de las bandejas, del codigo o de la configuracion con fecha de escritura posterior a las huellas que tome al lanzarlo,
uno por linea:

    $ ls -l --time-style=full-iso .v68aud/huellas_al_barrer.txt | awk '{print $6, $7, $9}'
    2026-09-24 21:59:13.578070900 .v68aud/huellas_al_barrer.txt
    $ find cuarentena dataset bitacora censos config fuentes esquema src scripts -type f -newer .v68aud/huellas_al_barrer.txt | sort
    bitacora/VEREDICTOS.jsonl
    censos/atribuciones.md
    censos/denominaciones.md
    dataset/nodos.jsonl

Segundo, **las `50` huellas de entonces** (las `47` fichas de Grove, las dos filas de `cap_04` y el grafo) contra los
ficheros de hoy, buscando en `_insertados` la ficha que ya no esta en la bandeja:

    $ python .v70aud/huellas_hoy.py
    huellas: 50 | por estado: {'movida a _insertados, misma huella': 20, 'en su sitio, misma huella': 29, 'grafo, aparte': 1} | suma: 50
    movidas a _insertados: 20 | son las 20 de .v68aud/los20.txt: SI | fuera de ellas: []
    ficheros que no cuadran: []

Tercero, **el grafo**: si al de hoy le quito las `20` filas de la tanda, y ademas los ids de las `20` de las listas de los
nodos viejos, sale el fichero que barri, byte a byte:

    $ python .v70aud/grafo_sin_tanda.py
    filas del grafo hoy: 410 | la reconstruccion reproduce el fichero de hoy: SI
    de las 20 de la tanda en el grafo: 20 | filas que quedan sin ellas: 390
    las 20 son las ultimas filas del fichero: SI
    (a) sin las 20 filas, sha1 igual a la huella de mi barrido de la 68: NO
    (b) nodos viejos con algun id de las 20 en alguna lista: 3 | sin esos ids, sha1 igual a la huella: SI
    $ python .v70aud/poblacion.py
    poblacion: 479 | por sede: {'grafo': 410, 'bandeja': 69} | suma: 479

**LECTURA:**

- **El grafo tiene `410` filas, la bandeja de Grove `27`, sus insertados `65`, los pares mutuos `1` y `procesos/` esta
  vacio.** Coincide con el `410/1027/1/27/65` del asunto de `6c40696`, y lo digo como coincidencia.
- **Las `20` fichas movidas a `_insertados` son las `20` de mi lista, con la huella que tenian cuando las barri**, y las
  `27` que quedan en la bandeja y las dos filas de `cap_04`, tambien.
- **Los `390` nodos viejos son byte a byte los que barri, salvo `3` que ganaron algun id de la tanda en alguna lista**: sin
  esos ids, el fichero reconstruido tiene la huella de mi barrido. Quitando solo las filas no la tiene, y eso es lo que
  se espera si la tanda cableo madres viejas. **La cuenta `3` coincide con las `3` madres viejas que mi lectura espera**
  (seccion `4`), y es **cuenta y no identidad**. Las `20` son las ultimas filas del fichero.
- **Ningun fichero de `src/`, `scripts/`, `config/`, `esquema/`, `fuentes/` ni de ninguna bandeja se escribio despues
  de mis huellas**; lo que se escribio es el grafo, la bitacora y dos censos, que es lo que escribe una insercion. **Lo que
  no veo:** Gerber y Marquet no estan en mis huellas, asi que de ellas **mido la fecha y no el contenido**.
- **La poblacion de hoy es `479`**, la de mi barrido, con `20` en otra sede. Con el codigo, los umbrales y los textos
  iguales, **la aduana de cada `insertar` tuvo delante lo que tuvo mi barrido**, porque mover una ficha de la bandeja al
  grafo no la saca de la poblacion, y `buscar_vecinos` y `medir` miden titulo, resumen, pasos, id y dominio, **no las claves
  de relacion** (`src/aduana.py` y `texto_comparable` de `src/comun.py`, que lei).

## 3. **LAS `20`: LO QUE ENTRO ES LO QUE SE LEYO** (`D.58`), **Y SUS PASOS INVENTADOS** (`8`, `8.2`)

Cada nodo del grafo contra su ficha de `_insertados` (cuya huella es la leida, seccion `2`) en titulo, condiciones,
pasos, entregable y resumen; y sus pasos contra **mi** lectura entera sellada en la `68`, `.v68aud/fidelidad_fuente.txt`,
una fila por paso:

    $ python .v70aud/entra_lo_leido.py
    las 20 por sede hoy: {'grafo y _insertados': 20} | suma: 20
    nodos del grafo contra su ficha, cinco campos: {'igual': 20} | suma: 20
    nodos con descuadre entre sus pasos en el grafo y mis filas selladas: 0 []
    cap_05 lo que ENTRO: candidatos 12 | pasos 84 | mis marcas: {'T': 81, 'P': 0, 'D': 3} | suma: 84 | PUENTE 0 de 84 = 0.00 por ciento | con las D adjudicadas T: T 84, P 0, suma 84
    cap_06 lo que ENTRO: candidatos 8 | pasos 62 | mis marcas: {'T': 61, 'P': 0, 'D': 1} | suma: 62 | PUENTE 0 de 62 = 0.00 por ciento | con las D adjudicadas T: T 62, P 0, suma 62

**LECTURA:** las `20` viven en el grafo **con los textos que se leyeron**, y cada una con tantos pasos como filas tiene mi
lectura. **`PASOS INVENTADOS` de lo que ENTRO: `cap_05` `0` de `84` y `cap_06` `0` de `62`**, las cifras firmadas en la
`ACTA 67` `67.5` y la `ACTA 68` `68.6`; mis `D` las adjudico `T` la `ACTA 67` `67.4.a`, y no lo reabro (`D.47`). **Por debajo
del `10`: no se baja escalon** (`8.1`). Coincide con el *0 de 84 y 0 de 62* de `6c40696`, y lo digo como coincidencia.

## 4. **LO QUE MI LECTURA ESPERA QUE LA TANDA DEJE**

Sacado **solo** de mis ficheros sellados de la `68` y de `.v69aud/aristas_70.py`; la bitacora, solo contada:

    $ python .v70aud/esperado_70.py
    filas dirigidas de mi barrido con candidato de las 20: 118 | por vecino: {'vecino en la tanda': 98, 'vecino fuera de la tanda': 20} | suma: 118
    aristas esperadas: 7 | por origen: {'CONTINUA': 2, 'SOSTENGO': 5} | suma: 7
    madres esperadas que no son de las 20 (viven en el grafo desde antes): 3 ['agrupar_interrupciones_subordinados_reuniones_regulares', 'agrupar_tareas_semejantes_aprovechar_preparacion', 'buscar_regularidad_bloques_iguales_trabajo_mando']
    hijos esperados que no son de las 20: 0 []
    bitacora esperada: 904 + 118 + 5 = 1027 | hoy (lineas): 1027 | IGUAL
    filas dirigidas por la clase sellada de su par: {'SANO': 114, 'CONTINUA': 4} | suma: 118
    $ python .v69aud/aristas_70.py
    filas de aristas_lectura.tsv: 17 | por clase (sin la marca DUDA, con ACTA 67 67.4.d aplicada): {'SOSTENGO': 5, 'EN VEREDICTO': 2, 'NO': 10} | suma: 17
    aristas esperadas en la 70: 7 | por origen: {'CONTINUA de veredicto': 2, 'SOSTENGO por lectura': 5} | suma: 7
      CONTINUA   tomar_notas_copia_guion_reunion_individual           > conducir_reunion_individual_telefono_distancia
      CONTINUA   preparar_guion_reunion_individual_subordinado        > tomar_notas_copia_guion_reunion_individual
      SOSTENGO   buscar_regularidad_bloques_iguales_trabajo_mando     > infundir_regularidad_reunion_proceso
      SOSTENGO   agrupar_tareas_semejantes_aprovechar_preparacion     > infundir_regularidad_reunion_proceso   (ACTA 67 67.4.d)
      SOSTENGO   agrupar_interrupciones_subordinados_reuniones_regulares > acumular_asuntos_importantes_fichero_espera
      SOSTENGO   conducir_etapas_modelo_ideal_decision                > ejercer_poder_posicion_etapa_decision_clara
      SOSTENGO   conducir_etapas_modelo_ideal_decision                > cortar_discusion_libre_momento_justo
    de ellas con madre usar_tres_clases_reunion_proceso: 0

**LECTURA, y lo que se compara en el turno normal, no aqui:**

- **Lineas de bitacora.** Si cada `insertar` escribio una linea por vecino que su aduana levanto, y la aduana levanto lo
  que mi barrido (seccion `2`), son `118`: `4` `CONTINUA` y `114` `SANO` por la clase sellada de su par; y `python forja.py
  arista` escribe su propia linea, asi que con mis `5` por lectura son `904` mas `118` mas `5`. **La bitacora tiene `1027`.** **Es
  coincidencia de cuenta y no de contenido**: no he abierto ni una linea. **Mi lectura no espera ningun vecino sin linea
  preparada**, porque la poblacion es la del barrido; uno que apareciera seria un hallazgo.
- **Aristas: `7`**, las `2` `CONTINUA` de las notas y `5` por lectura, **ninguna con madre
  `usar_tres_clases_reunion_proceso`**, y `3` de ellas con madre vieja (`buscar_regularidad` y `agrupar_tareas` a
  `infundir`, y `agrupar_interrupciones` a `acumular`). Coincide con el *7 de 7* de `6c40696`, y con la cuenta `3` de la
  seccion `2`: **par a par lo cruzo en el turno normal**, que es donde un `7` igual con pares distintos se veria.

## 5. **MI CLASIFICACION DE CADA CANDIDATO, Y LAS CINCO ARISTAS POR LECTURA RELEIDAS** (`6.1`, y solo la vara `6.1`)

**Las `20`, una por una**, de mis ficheros sellados: las lineas del libro que sus pasos transcriben, las filas dirigidas
de mi barrido en las que es candidata, sus pares sin orden por clase (cuenta los pares en los que esta de cualquiera de
los dos lados, y por eso puede pasar de sus filas) y las aristas que mi lectura le espera como hija:

    $ python .v70aud/clasificacion_20.py
     1 cap_05 infundir_regularidad_reunion_proceso               NODO | L21 a L21 | filas 5 | pares {'SANO': 5} suma 5 | hija: SOSTENGO de buscar_regularidad_bloques_iguales_trabajo_mando; SOSTENGO de agrupar_tareas_semejantes_aprovechar_preparacion
     2 cap_05 usar_tres_clases_reunion_proceso                   NODO | L23 a L23 | filas 5 | pares {'SANO': 5} suma 5 | hija: ninguna
     3 cap_05 fijar_frecuencia_reunion_individual_madurez_tarea  NODO | L33 a L35 | filas 6 | pares {'SANO': 6} suma 6 | hija: ninguna
     4 cap_05 fijar_duracion_lugar_reunion_individual            NODO | L37 a L39 | filas 7 | pares {'SANO': 7} suma 7 | hija: ninguna
     5 cap_05 preparar_guion_reunion_individual_subordinado      NODO | L41 a L41 | filas 9 | pares {'SANO': 8, 'CONTINUA': 1} suma 9 | hija: ninguna
     6 cap_05 cubrir_indicadores_problemas_reunion_individual    NODO | L43 a L43 | filas 6 | pares {'SANO': 6} suma 6 | hija: ninguna
     7 cap_05 facilitar_expresion_subordinado_pregunta_mas       NODO | L45 a L47 | filas 8 | pares {'SANO': 8} suma 8 | hija: ninguna
     8 cap_05 tomar_notas_copia_guion_reunion_individual         NODO | L49 a L49 | filas 7 | pares {'SANO': 5, 'CONTINUA': 2} suma 7 | hija: CONTINUA de preparar_guion_reunion_individual_subordinado
     9 cap_05 acumular_asuntos_importantes_fichero_espera        NODO | L51 a L51 | filas 6 | pares {'SANO': 6} suma 6 | hija: SOSTENGO de agrupar_interrupciones_subordinados_reuniones_regulares
    10 cap_05 alentar_asuntos_corazon_vigilar_final_reunion      NODO | L53 a L53 | filas 7 | pares {'SANO': 7} suma 7 | hija: ninguna
    11 cap_05 conducir_reunion_individual_telefono_distancia     NODO | L55 a L55 | filas 6 | pares {'SANO': 5, 'CONTINUA': 1} suma 6 | hija: CONTINUA de tomar_notas_copia_guion_reunion_individual
    12 cap_05 programar_reunion_individual_cadena                NODO | L57 a L57 | filas 7 | pares {'SANO': 7} suma 7 | hija: ninguna
    13 cap_06 conducir_etapas_modelo_ideal_decision              NODO | L23 a L29 | filas 0 | pares {} suma 0 | hija: ninguna
    14 cap_06 decidir_nivel_competente_inferior                  NODO | L33 a L33 | filas 3 | pares {'SANO': 3} suma 3 | hija: ninguna
    15 cap_06 vencer_sindrome_grupo_pares_autoconfianza          NODO | L49 a L49 | filas 13 | pares {'SANO': 13} suma 13 | hija: ninguna
    16 cap_06 tomar_mando_reunion_pares_presidente_ausente       NODO | L51 a L51 | filas 4 | pares {'SANO': 4} suma 4 | hija: ninguna
    17 cap_06 ejercer_poder_posicion_etapa_decision_clara        NODO | L61 a L61 | filas 2 | pares {'SANO': 3} suma 3 | hija: SOSTENGO de conducir_etapas_modelo_ideal_decision
    18 cap_06 cortar_discusion_libre_momento_justo               NODO | L63 a L63 | filas 6 | pares {'SANO': 6} suma 6 | hija: SOSTENGO de conducir_etapas_modelo_ideal_decision
    19 cap_06 zanjar_seis_preguntas_decision_adelantado          NODO | L65 a L77 | filas 2 | pares {'SANO': 2} suma 2 | hija: ninguna
    20 cap_06 anunciar_decision_inesperada_reconvocar_reunion    NODO | L93 a L93 | filas 9 | pares {'SANO': 10} suma 10 | hija: ninguna

**LECTURA: LAS `20` SON NODO**, con la clase de cada par que selle en la `68`. De la `68` a hoy no he cambiado ninguna: la
conjunta de la `69` las dejo como estaban (`ACTA 68` `68.3`).

**Las cinco aristas por lectura son las que el extractor cablea a mano con `python forja.py arista`**, y por eso las releo
hoy con el libro y los pasos delante. Las lineas del libro que las sostienen (tambien las de las dos `CONTINUA`):

    $ python .v70aud/lineas_fuente.py
    cap_05 L21 (723 caracteres): To make the most of this kind of meeting, we should aim to infuse it with regularity. In other words, the people attending should know how the meeting is run, what kinds of substantive matters are discussed, and what is to be accomplished. It should be designed to allow a manager to “batch” transactions, to use the same “production” set-up time and effort to [...]
    cap_05 L41 (852 caracteres): A key point about a one-on-one: It should be regarded as the subordinate’s meeting, with its agenda and tone set by him. There’s good reason for this. Somebody needs to prepare for the meeting. The supervisor with eight subordinates would have to prepare eight times; the subordinate only once. So the latter should be asked to prepare an outline, which is ver [...]
    cap_05 L49 (907 caracteres): I’d like to suggest some mechanical hints for effective one-on-one meetings. First, both the supervisor and subordinate should have a copy of the outline and both should take notes on it, which serves a number of purposes. I take notes in just about all circumstances, and most often end up never looking at them again. I do it to keep my mind from drifting an [...]
    cap_05 L51 (412 caracteres): A real time-saver is using a “hold” file where both the supervisor and subordinate accumulate important but not altogether urgent issues for discussion at the next meeting. This kind of file applies the production principle of batching and saves time for both involved by minimizing the need for ad hoc contact (raya) like phone calls, drop-in visits, and so on (raya) which [...]
    cap_05 L55 (533 caracteres): Long-distance telephone one-on-ones have become necessary because many organizations are now spread out geographically. But these can work well enough with proper preparation and attention: the supervisor must have the outline before the meeting begins, both parties should take notes, and so on. Because you can’t see the other participant in the meeting, not [...]
    cap_06 L61 (1176 caracteres): Sometimes no amount of discussion will produce a consensus, yet the time for a decision has clearly arrived. When this happens, the senior person (or “peer-plus-one”) who until now has guided, coached, and prodded the group along has no choice but to make a decision himself. If the decision-making process has proceeded correctly up to this point, the senior  [...]
    cap_06 L63 (825 caracteres): If you either enter the decision-making stage too early or wait too long, you won’t derive the full benefit of open discussion. The criterion to follow is this: don’t push for a decision prematurely. Make sure you have heard and considered the real issues rather than the superficial comments that often dominate the early part of a meeting. But if you feel th [...]

Y los pasos de sus ocho nodos, por `pasos_ciego.py` (`R6`):

    $ python .v67aud/normal/pasos_ciego.py conducir_etapas_modelo_ideal_decision ejercer_poder_posicion_etapa_decision_clara cortar_discusion_libre_momento_justo agrupar_interrupciones_subordinados_reuniones_regulares acumular_asuntos_importantes_fichero_espera buscar_regularidad_bloques_iguales_trabajo_mando agrupar_tareas_semejantes_aprovechar_preparacion infundir_regularidad_reunion_proceso
    ===== conducir_etapas_modelo_ideal_decision | grafo
      titulo: Conducir una decision por las etapas del modelo ideal: discusion libre, decision clara y apoyo pleno
      fuente: ['grove_high_output']
      cond: Cuando un grupo tiene que tomar una decision en un negocio que depende de lo que sabe, y quieres que el conocimiento de los que saben llegue a la decision en vez de quedarse callado.
      P1. Abre la primera etapa con discusion libre, en la que todos los puntos de vista y todos los aspectos del asunto se acogen abiertamente y se debaten.
      P2. Cuanto mayores sean el desacuerdo y la controversia, mas importante se vuelve la palabra libre.
      P3. Vigila la practica contraria, que es la corriente: cuando la reunion se calienta, los participantes se echan atras, tantean hacia donde van las cosas y no dicen nada hasta ver que postura va a imponerse, para apoyarla despues y no quedar asociados a la que pierde.
      P4. Cuenta con que, si los que saben se guardan su opinion, lo que se decida se apoyara en informacion y criterio mas incompletos de lo que podrian haber sido.
      P5. Pasa despues a la etapa siguiente, que es alcanzar una decision clara, y cuanto mayor sea el desacuerdo sobre el asunto, mas importante se vuelve la palabra clara.
      P6. Pon cuidado especial en enmarcar los terminos de la decision con claridad absoluta.
      P7. No oscurezcas el asunto para ahorrarte la discusion cuando sepas que la decision es polemica: hablando con medias palabras no evitas la discusion, solo la aplazas.
      P8. Cuenta con que a quien no le guste la decision se enfadara bastante mas si no recibe una version pronta y directa de lo que se decidio.
      P9. Exige por ultimo que todos los implicados den pleno apoyo a la decision alcanzada por el grupo.
      P10. No confundas ese apoyo con el acuerdo: basta con que los participantes se comprometan a respaldar la decision, y ese es un resultado satisfactorio.
      P11. Cuenta con que ni el mismo tiempo ni los mismos hechos van a producir acuerdo en muchos asuntos, porque las diferencias de opinion honestas y sentidas existen, y una organizacion no vive de que sus miembros esten de acuerdo en todo.
      P12. Pide a todos, y no solo a algunos, que ese compromiso de apoyo este honestamente presente: es lo unico que un mando puede esperar y lo que tiene que conseguir de cada uno.
    ===== ejercer_poder_posicion_etapa_decision_clara | grafo
      titulo: Ejercer el poder de posicion solo al llegar a la etapa de decision clara sin consenso, y nunca antes
      fuente: ['grove_high_output']
      cond: Cuando ninguna cantidad de discusion va a producir consenso y el momento de decidir ha llegado claramente, y el que dirige el grupo tiene que decidir si usa ya su autoridad de rango.
      P1. Reconoce la situacion por sus dos mitades: ninguna cantidad de discusion va a producir consenso, y aun asi el momento de decidir ha llegado claramente.
      P2. Cuando eso pase, acepta que la persona de mayor rango, la del par mas uno, que hasta ahora ha guiado, entrenado y espoleado al grupo, no tiene mas remedio que tomar ella misma la decision.
      P3. Comprueba que el proceso vino bien hasta ese punto: que quien decide lo hace con el beneficio completo de la discusion libre, en la que todos los puntos de vista, hechos, opiniones y juicios se expusieron sin el prejuicio del poder de posicion.
      P4. Ejerce entonces la autoridad del poder de posicion, que ahi es legitima y a veces inevitable, porque se alcanzo la etapa de decision clara y no aparecio ningun consenso.
      P5. No la ejerzas ni un momento antes: ejercerla antes no es legitimo, y es destructivo.
      P6. Cuenta con que esto no suele ser facil, porque existe reticencia a ejercer el poder de posicion de forma deliberada y explicita, ya que dar ordenes parece poco amable.
      P7. Vigila la consecuencia de esa reticencia: alarga la primera fase del proceso, que es el tiempo de discusion libre, mas alla del punto optimo, y la decision se aplaza.
    ===== cortar_discusion_libre_momento_justo | grafo
      titulo: Cortar la discusion libre en el momento justo: ni antes de oir los asuntos de verdad, ni cuando ya se ha oido todo
      fuente: ['grove_high_output']
      cond: Cuando diriges una discusion libre y tienes que decidir si ya es momento de pasar a la decision, o si todavia falta por oir lo que de verdad importa.
      P1. Cuenta con que entrar en la etapa de decision demasiado pronto o esperar demasiado te deja sin el beneficio completo de la discusion abierta.
      P2. Sigue el criterio que el libro escribe: no empujes hacia una decision prematuramente.
      P3. Asegurate de haber oido y considerado los asuntos de verdad, y no los comentarios superficiales que suelen dominar la primera parte de una reunion.
      P4. Pero en cuanto sientas que ya lo has oido todo y que todos los lados del asunto se han planteado, empuja hacia un consenso.
      P5. Si el consenso no sale, entra tu y toma la decision.
      P6. Vigila la discusion libre que sigue en una busqueda interminable de consenso: cuando eso pasa, la gente se aleja del consenso cercano justo cuando esta cerca de acertar, y eso rebaja las posibilidades de llegar a la decision correcta.
      P7. Pasa a tomar la decision en el momento justo, que es lo decisivo.
    ===== agrupar_interrupciones_subordinados_reuniones_regulares | grafo
      titulo: Agrupar en tanda las interrupciones que llegan de los subordinados y atenderlas en las reuniones regulares de personal y de uno a uno, en vez de atenderlas al azar
      fuente: ['grove_high_output']
      cond: Cuando las interrupciones de tus subordinados te caen al azar a lo largo del dia y las atiendes segun llegan.
      P1. Usa ademas el principio de produccion de la tanda, que es atender de una vez un grupo de tareas semejantes.
      P2. Acumula con ese principio muchas de las interrupciones que te vienen de tus subordinados, en vez de atenderlas al azar.
      P3. Atiende esas interrupciones acumuladas en las reuniones de personal y en las reuniones de uno a uno.
      P4. Manten esas reuniones con regularidad.
      P5. Pide entonces a tu gente que agrupe sus preguntas y problemas para esos momentos programados en vez de interrumpirte cuando quiera, porque con las reuniones celebradas con regularidad no pueden protestar mucho.
    ===== acumular_asuntos_importantes_fichero_espera | grafo
      titulo: Abrir un fichero de espera compartido donde las dos partes acumulan lo importante que no es del todo urgente, para tratarlo en la reunion siguiente
      fuente: ['grove_high_output']
      cond: Cuando entre una reunion individual y la siguiente aparecen asuntos importantes que no son del todo urgentes y hay que decidir si se interrumpe al otro o se esperan.
      P1. Usa un fichero de espera compartido por el supervisor y el subordinado.
      P2. Acumula ahi los asuntos importantes pero no del todo urgentes, para tratarlos en la reunion siguiente.
      P3. Cuenta con que esa clase de fichero aplica el principio de produccion del agrupamiento.
      P4. Cuenta con que el ahorro de tiempo para los dos implicados sale de reducir al minimo la necesidad de contacto improvisado, como las llamadas de telefono o las visitas sin avisar, que son las interrupciones que el libro considero antes.
    ===== buscar_regularidad_bloques_iguales_trabajo_mando | grafo
      titulo: Buscar la regularidad en el trabajo de mando alisando la carga, abriendo ventanas en la caja negra, y usando los mismos bloques de tiempo para las actividades iguales
      fuente: ['grove_high_output']
      cond: Cuando tu jornada de mando se te llena de parones y arranques y las actividades iguales te caen en momentos distintos cada semana.
      P1. Aplica a tu trabajo de mando el siguiente concepto de produccion: ve hacia la regularidad.
      P2. Alisa tu carga de trabajo todo lo que puedas, aunque no puedas controlar los habitos de los que te llegan, igual que una fabrica de desayunos iria mas eficiente si los clientes llegaran en un flujo estable y predecible en vez de entrar de uno en uno y de dos en dos.
      P3. Haz que tu trabajo de mando tome las caracteristicas de una fabrica y no las de un taller a pedido.
      P4. Impide en consecuencia, con todo lo que puedas, los pequenos parones y arranques de tu jornada, y tambien las interrupciones que traen las emergencias grandes.
      P5. Busca siempre las fuentes de problemas futuros de prioridad alta abriendo ventanas en la caja negra de tu organizacion, aunque algunas de esas emergencias sean inevitables.
      P6. Cuenta con lo que ganas al reconocer que tienes una bomba de relojeria entre manos: puedes atender el problema cuando tu quieras y no despues de que la bomba haya estallado.
      P7. Coordina tu trabajo con el de los demas mandos, porque solo puedes ir hacia la regularidad si los otros van tambien.
      P8. Usa, dicho de otro modo, los mismos bloques de tiempo para las actividades iguales.
      P9. Toma el ejemplo que el libro da de Intel: las mananas de los lunes se apartaron en toda la empresa como el momento en que se reunen los grupos de planificacion, asi que quien pertenece a uno puede contar con el lunes para eso y queda libre de choques de agenda.
    ===== agrupar_tareas_semejantes_aprovechar_preparacion | grafo
      titulo: Agrupar las tareas semejantes en una tanda para aprovechar un solo esfuerzo de preparacion
      fuente: ['grove_high_output']
      cond: Cuando tienes por delante varias actividades de mando del mismo tipo y las estas atendiendo una a una segun llegan, pagando su preparacion cada vez.
      P1. Aplica a tu trabajo de mando el segundo principio de produccion: agrupar las tareas semejantes.
      P2. Cuenta con que toda operacion de fabricacion exige una cierta cantidad de tiempo de preparacion, y con que ese tiempo tiene muchos paralelos en el trabajo de mando.
      P3. Para que el trabajo de mando avance con eficiencia, usa un mismo esfuerzo de preparacion y aplicalo a todo un grupo de actividades semejantes.
      P4. Reutiliza lo que ya preparaste: una vez preparado un juego de ilustraciones para una clase de formacion, tu productividad sube si puedes usar ese mismo juego una y otra vez con otras clases o grupos.
      P5. Cuando tengas varios informes que leer o varias evaluaciones de desempeno que aprobar, reserva un bloque de tiempo y hazlos en tanda, uno tras otro.
      P6. Hazlo asi para aprovechar al maximo el tiempo de preparacion mental que esa tarea necesita.
    ===== infundir_regularidad_reunion_proceso | grafo
      titulo: Infundir regularidad a la reunion de proceso, para poder agrupar en tanda las tareas de mando semejantes y pronosticar el tiempo que piden
      fuente: ['grove_high_output']
      cond: Cuando llevas una reunion de las que se repiten en un calendario fijo y quieres sacarle el maximo, en vez de dejar que cada convocatoria se organice sola.
      P1. Apunta a infundir regularidad a esta clase de reunion, que es la manera de sacarle el maximo.
      P2. Consigue que los que asisten sepan como se lleva la reunion.
      P3. Consigue que sepan que clases de asuntos de fondo se tratan en ella.
      P4. Consigue que sepan que es lo que hay que conseguir en ella.
      P5. Disenala de forma que te deje agrupar transacciones en tanda, o sea usar el mismo tiempo y esfuerzo de preparacion de produccion para atender muchas tareas de mando semejantes.
      P6. Aprovecha que, dada esa regularidad, tu y los demas asistentes podeis empezar a pronosticar el tiempo que piden las clases de trabajo que hay que hacer.
      P7. Deja que de ahi tome forma un sistema de control de produccion, registrado en los distintos calendarios.
      P8. Cuenta con lo que ese sistema consigue: que una reunion programada tenga el minimo impacto en las otras cosas que la gente esta haciendo.

**LECTURA, UNA POR UNA, Y LAS CINCO LAS SOSTENGO:**

- **`conducir_etapas` a `ejercer_poder`: SOSTENGO.** La condicion de la hija (*ninguna cantidad de discusion va a producir
  consenso y el momento de decidir ha llegado claramente*) es el producto del paso `5` de la madre, **pasar a la etapa de
  decision clara**; y la hija anade lo que la madre no dice, **quien decide y con que autoridad** (sus pasos `2` a `5`, L61:
  *legitimate ... if the clear decision stage is reached and no consensus has developed*). No repite: la madre no nombra
  el poder de posicion.
- **`conducir_etapas` a `cortar_discusion`: SOSTENGO.** La condicion de la hija (*diriges una discusion libre y tienes que
  decidir si ya es momento de pasar a la decision*) es el paso `1` de la madre ya en marcha, que desemboca en su paso `5`; y
  la hija anade **el criterio del momento** (L63, *don't push for a decision prematurely* y *if you feel that you have
  already heard everything*), que la madre no trae. **Las dos hijas son hermanas entre si** (mi `NO, DUDA` de
  `cortar_discusion` a `ejercer_poder`, sellado): las dos parten de la frontera entre la etapa `1` y la `2`, una por el
  cuando y otra por el quien.
- **`agrupar_interrupciones` a `acumular`: SOSTENGO.** L51 remite con palabras a la pieza de la madre (*which constitute
  the interruptions we considered earlier*); la condicion de la hija (*entre una reunion individual y la siguiente
  aparecen asuntos*) parte del producto de la madre, las interrupciones acumuladas para las reuniones regulares (sus pasos
  `2` y `3`), y la hija anade **el fichero compartido por las dos partes** y el filtro de lo importante y no urgente.
- **`buscar_regularidad` a `infundir`: SOSTENGO, con la `DUDA` sellada.** La condicion de la hija (*una reunion de las que
  se repiten en un calendario fijo*) es el producto de los pasos `8` y `9` de la madre, **los mismos bloques de tiempo para
  las actividades iguales**, con el lunes de los grupos de planificacion; y la hija anade la regularidad **dentro** de la
  reunion (sus pasos `2` a `4`) y el pronostico (`6` y `7`). La duda sigue escrita: se pueden leer como el mismo principio
  aplicado a la jornada y a la reunion.
- **`agrupar_tareas` a `infundir`: SOSTENGO, por la adjudicacion de la `ACTA 67` `67.4.d`**, que dio la razon al extractor
  dentro de mi `DUDA`. El paso `5` de la hija **procedimenta** la tanda (*usar el mismo tiempo y esfuerzo de preparacion ...
  para atender muchas tareas de mando semejantes*, L21), no solo la nombra, y eso es usar el producto de `agrupar_tareas`
  (su paso `3`, el mismo esfuerzo de preparacion aplicado a un grupo). **No la reabro** (`D.47`): la escribo para que se vea
  que la releo y que se sostiene.

## 6. **LO QUE DEJO PARA MI TURNO NORMAL, ESCRITO ANTES DE VER EL REPORTE**

1. **`R5`** en su reporte, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` sacados otra vez de los
   originales y con la cabecera cambiada a la `70`.
2. **Las lineas nuevas de la bitacora**, una a una: las `118` contra las vivas de `.v68ext/veredictos_listos.txt`
   (con las corregidas por la conjunta de la `69` y sin ninguna de las que quedaron en comentario) y contra mis clases
   selladas, y las `5` de `forja.py arista` contra mis cinco `SOSTENGO` de la seccion `5`, con su paso.
3. **Las `7` aristas, par a par**, contra `.v69aud/aristas_70.py`; que los `3` nodos viejos reescritos son las `3` madres
   viejas y que **solo** cambiaron sus claves de relacion; y **ninguna con madre `usar_tres_clases_reunion_proceso`**.
4. **Que cada `insertar` volvio con su `.fin` en `0`, en el orden de `.v69aud/restricciones_orden.py`, uno por vez y sin
   solaparse**, y que **ninguna aduana levanto un vecino fuera de mi barrido**; y que quiere decir `d58cd8c` con *insertado
   por la aduana* en la fila `20` (seccion `1`, punto `4`).
5. **La muestra pineada de los SANO** que la `70` escribio en la bitacora, **con semilla `70`**, el tamaño de la seccion
   `7` y su banda, releida contra mis clases selladas.
6. **El censo, las guardas y el cierre estricto**, que tallara esta pagina: no tiene tablas, asi que un rojo en el suyo
   sera suyo. Y el coste de su turno, del `loop.log`, contra su clase (`D.55`).

## 7. **ESTA PAGINA CONTRA `R6` Y `R7`, MEDIDA SOBRE ELLA MISMA**

El generador corre dos veces, y estos bloques de la segunda pasada leen la pagina que escribio la primera, identica
salvo ellos. El primero cuenta las lineas de bloque `$` que empiezan por una clave de relacion (las que la nombran en
mis frases y comandos no cuentan, porque la nombran para decir que no la imprimo); el segundo, las lineas de bloque que
reparten en clases, y cuantas traen su `suma`; el tercero, las rayas y guiones medios de la pagina:

    $ grep -c -E "^    +(previos|siguientes|nodos_previos|nodos_siguientes)" docs/loop/APERTURA_CIEGA.md
    0
    $ python .v70aud/r7_pagina.py
    lineas de bloque que reparten en clases: 31 | por estado: {'con suma': 31} | suma: 31
    $ grep -c -P "\x{2014}|\x{2013}" docs/loop/APERTURA_CIEGA.md
    0
