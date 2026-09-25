# APERTURA CIEGA DE LA VUELTA 68, lote 7 (`grove_high_output`), **CLASE INSERCION**

*Auditor `claude-opus-5-5`, fase ciega, del 24 al 25 sep 2026, la que el arnes numera `VUELTA 4` en la corrida que
arranco el 23 a las `21:50`. Linea **serial**, rama `extraccion-mundo-11`, arbol en `3d28595` (el ultimo commit
del extractor). Modo austero (`D.47`). Todo lo de esta pagina sale de `.v68aud/`, escrito y corrido en esta
fase; cada bloque `$` lo pega `.v68aud/generar_apertura.py` corriendo el comando en el momento de escribirla.
**No hay ninguna tabla en esta pagina**, a proposito, como en la `66` (`d167`).*

## 0. **LA HERENCIA** (`D.40`)

ACTA ANTERIOR LEIDA: c95ca6a4145846707fd40ea2c8442b59f19b7266

HEREDADO 1: NO APLICA en esta fase. **Motivo:** `R5` es un remedio **del extractor** y se mide **sobre su
reporte de la `68`** (`ACTA 66` `66.11`: *el reporte de la `68`, con `.v64ext/pegado64.py` y
`.v64aud/normal/bloques_mudos.py`, los dos con la cabecera del tramo cambiada a la `68`*), y el reporte **no
esta en el arbol**: el arnes lo retiro para esta fase (`D.34.2`) y no lo he recuperado por ninguna via. **Se mide
en mi turno normal**, con los dos instrumentos sacados otra vez de los originales y no de las copias del
extractor. Lo que si esta en mi mano lo cumplo en mi pagina: cada bloque `$` lleva la salida del comando que
abre, y nada mas.

    $ ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl
    ls: cannot access 'docs/loop/REPORTE.md': No such file or directory
    ls: cannot access 'docs/loop/ultimo_extractor.json': No such file or directory
    ls: cannot access 'docs/loop/ultimo_auditor.json': No such file or directory
    ls: cannot access 'docs/loop/CREDITO_serial.jsonl': No such file or directory
    $ grep -n "VUELTA 4 : APERTURA CIEGA" docs/loop/loop.log | tail -1
    5989:[2026-09-24 21:56:28] VUELTA 4 : APERTURA CIEGA (claude-opus-5-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl

HEREDADO 2: CUMPLIDO. **`R6`, mio** (`ACTA 66` `66.11`): en esta fase los pasos de cualquier nodo los imprime
`.v67aud/normal/pasos_ciego.py`, que no enseña `previos` ni `siguientes`, y ningun instrumento de esta fase
imprime claves de relacion de un nodo que la vuelta haya tocado. Los ficheros de pasos que lei, y cuantas
lineas con esas claves traen:

    $ grep -c -E "previos|siguientes" .v68aud/pasos_cap05.txt .v68aud/pasos_cap06.txt .v68aud/pasos_fuera_a.txt .v68aud/pasos_fuera_b.txt .v68aud/pasos_pares.txt
    .v68aud/pasos_cap05.txt:0
    .v68aud/pasos_cap06.txt:0
    .v68aud/pasos_fuera_a.txt:0
    .v68aud/pasos_fuera_b.txt:0
    .v68aud/pasos_pares.txt:0
    $ grep -l -E "nodos_previos|nodos_siguientes|previos|siguientes" .v68aud/*.py | wc -l
    0

**LECTURA:** ningun instrumento mio de esta fase nombra esas claves, y ninguna salida de pasos las trae.
`entra_lo_leido.py` compara solo titulo, condiciones, pasos y entregable (seccion `3`), asi que **las dos aristas
de las filas `21` y `22` NO las miro aqui**: las espero por mi lectura sellada de la `66` y las compruebo en mi
turno normal. **No vi ninguna clave de relacion de un nodo tocado en esta fase.** Y el cumplimiento de la pagina
entera lo mide un `grep` sobre ella antes de cerrarla (seccion `9`).

**LA HUELLA** es la que el prompt me entrega, comprobada solo contra el propio prompt: **no la recomputo**,
porque `forja.py herencia` lee en esta fase un fichero retirado (`d146`).

## 1. **LO QUE VI SIN BUSCARLO, Y LO DIGO ANTES DE MEDIR** (`d146`)

**La foto de `git status` que el entorno me pone delante trae los asuntos de los commits del extractor, y dos
son cifras de su cierre**: `6be63c5` *Vuelta 68, T4: el cierre (390 nodos, bandeja de Grove en 47 e insertados
en 45, cap_04 entero en el grafo con 0 de 156, las 2 aristas de la tanda vivas, cap_05 y cap_06 listos para la 70
con sus 20 huellas iguales, R5 en cero, ...)* y `9de244e` *Vuelta 68, T3: cap_05 y cap_06 listos para la 70
(fidelidad 0 de 84 y 0 de 62, barrido de los 20 con 118 pares y sus 118 lineas, 9 aristas por lectura, orden con
las tres comprobaciones en cero), ninguno insertado*. **Y un `git log` que corri para saber desde que commit medir
me los volvio a enseñar.** Los lei antes de medir nada. Es el mismo hueco de `d146` que ya declararon las
aperturas de la `65`, la `66` y la `67`, y no lo arreglo yo (`D.45`). Tambien lei la cola de `docs/loop/loop.log`,
que no se retira.

**LO QUE HAGO CON ELLO:** ninguna cifra de esta pagina sale de esos asuntos; todas salen de un instrumento
corrido en esta fase, y donde coinciden lo digo como coincidencia y no como fuente. **Las clases no las tocan**:
los asuntos no nombran ni un veredicto ni un par ni una arista. **No he abierto nada de `.v68ext/`** (ni su
fidelidad, ni su barrido, ni sus veredictos, ni sus aristas, ni su orden), **ni `bitacora/VEREDICTOS.jsonl` por
dentro**: de ella solo cuento lineas.

## 2. **EL ALCANCE, Y EL CENSO QUE LO SOSTIENE**

La vuelta tenia dos trabajos (encargo de la `68`): **insertar las filas `21` y `22`** de `cap_04`
(`agrupar_interrupciones_subordinados_reuniones_regulares` y `canalizar_interrupciones_cartel_hora_oficina`), y
**dejar `cap_05` y `cap_06` listos sin insertar ninguno**: fidelidad entera, barrido, veredictos, aristas por
lectura, orden y la huella de las `20` fichas. El commit de mi `ACTA 66` con su hook es `587f1d8`.

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        390 dataset/nodos.jsonl
        904 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1295 total
    $ ls cuarentena/grove_high_output/*.json | wc -l
    47
    $ ls cuarentena/_insertados/grove_high_output/*.json | wc -l
    45
    $ git diff --stat 587f1d8 3d28595 -- dataset/ bitacora/ censos/ config/pares_mutuos.jsonl
     bitacora/VEREDICTOS.jsonl | 11 +++++++++++
     censos/denominaciones.md  |  7 +++++++
     dataset/nodos.jsonl       |  6 ++++--
     3 files changed, 22 insertions(+), 2 deletions(-)
    $ git diff --name-status 587f1d8 3d28595 -- cuarentena/
    R100	cuarentena/grove_high_output/agrupar_interrupciones_subordinados_reuniones_regulares.json	cuarentena/_insertados/grove_high_output/agrupar_interrupciones_subordinados_reuniones_regulares.json
    R100	cuarentena/grove_high_output/canalizar_interrupciones_cartel_hora_oficina.json	cuarentena/_insertados/grove_high_output/canalizar_interrupciones_cartel_hora_oficina.json
    $ ls -A procesos/ | wc -l
    0
    $ git status --short -- dataset bitacora censos cuarentena config | wc -l
    0

**LECTURA:** contra el censo de la `ACTA 66` `66.1` (`388`, `893`, `1`, `49`, `43`), el grafo sube `2`, la bandeja
baja `2` y `_insertados` sube `2`, que es lo que el encargo esperaba si entraban las dos. **La bitacora gana `11`
lineas**: si son las `8` y la `1` del bloque de cada fila mas las `2` de sus aristas por lectura, cuadra, **pero eso
no lo miro aqui porque seria abrirla**. **Lo unico que se movio en `cuarentena/` son los dos `git mv` de las filas
`21` y `22`, al cien por cien: ninguna ficha de `cap_05` ni de `cap_06` cambio en la bandeja desde mi acta**, asi que
la vuelta no corrigio ningun paso de los `20`, y **cualquier PUENTE que mi lectura encuentre sigue en la ficha**.
`procesos/` esta vacio: ningun cerrojo quedo cogido.

**Y LOS `20` DE LA TANDA SON TODO LO QUE GROVE TIENE DE ESOS DOS CAPITULOS**, en cualquier sede, por la `UNIDAD DE
ORIGEN` de su `resumen_teorico`:

    $ python .v68aud/cobertura.py
    por sede y capitulo: {('bandeja', 'cap_05'): 12, ('bandeja', 'cap_06'): 8}
    de cap_05 o cap_06 y fuera de los 20: 0

**LECTURA, sin medirla mas:** las piezas de *staff meetings* (L67 a L83), *operation reviews* (L85 a L97) y
*mission-oriented meetings* (L99 a L175) de `cap_05` no tienen candidato con esa unidad en ninguna sede. Es la
frontera de la vuelta `50`, que no reabro (`D.47`); solo digo que la vi.

## 3. **LAS FILAS `21` Y `22`: LO QUE ENTRO ES LO QUE SE LEYO** (`D.58`)

Copia de `.v67aud/entra_lo_leido.py` con la tanda cambiada a las dos filas: compara titulo, condiciones, pasos y
entregable del nodo del grafo con la ficha en `d8f4e2a` (el cierre de la `66`, sobre el que lei `cap_04` entero), y el
blob de `_insertados` con ese mismo commit; y cuenta sus pasos contra **mi** fidelidad sellada de la `66`
(`.v66aud/fidelidad.tsv`). **No imprime claves de relacion** (`R6`).

    $ python .v68aud/entra_lo_leido.py
    agrupar_interrupciones_subordinados_reuniones_regulares pasos  5 filas mias  5 P 0 D 0
    canalizar_interrupciones_cartel_hora_oficina           pasos  8 filas mias  8 P 0 D 0
    nodos de la tanda en el grafo iguales a su lectura entera: 2 | distintos: 0
    fichas de _insertados con el mismo blob que en d8f4e2a: 2 | distintas: 0
    cap_04 lo que entro: candidatos 2 | pasos 13 | filas de mi lectura 13 | P 0 | D 0
    PUENTE sobre pasos que entraron: 0 de 13 = 0.00 por ciento
    si mis D cayesen a PUENTE: 0 de 13 = 0.00 por ciento
    $ python .v68aud/entra_lo_leido.py 22 | tail -5
    nodos de la tanda en el grafo iguales a su lectura entera: 22 | distintos: 0
    fichas de _insertados con el mismo blob que en d8f4e2a: 22 | distintas: 0
    cap_04 lo que entro: candidatos 22 | pasos 156 | filas de mi lectura 156 | P 0 | D 4
    PUENTE sobre pasos que entraron: 0 de 156 = 0.00 por ciento
    si mis D cayesen a PUENTE: 4 de 156 = 2.56 por ciento

**LECTURA:** las dos viven en el grafo con los bytes que se leyeron, y **`cap_04` queda entero en el grafo con las
`22` iguales a su lectura**. **`PASOS INVENTADOS` de lo que entro en esta vuelta: `0` de `13`**, y de `cap_04`
entero `0` de `156`, con mis cuatro `D` que la `ACTA 65` `65.4.a` adjudico `T`.

**LO QUE ESPERO DE ELLAS EN MI TURNO NORMAL, sellado desde la `66`** (`APERTURA_CIEGA.md` de la `66`, secciones
`6` y `7`, y `.v66aud/mis_clases.tsv`): sus lineas de veredicto, las de sus bloques de
`.v66ext/veredictos_listos.txt` letra a letra, y **sus dos aristas por lectura**:
`agrupar_tareas_semejantes_aprovechar_preparacion` madre de `agrupar_interrupciones_subordinados_reuniones_regulares`,
y `buscar_regularidad_bloques_iguales_trabajo_mando` madre de `canalizar_interrupciones_cartel_hora_oficina`.

    $ grep -E "agrupar_interrupciones|canalizar_interrupciones" .v66aud/aristas_lectura.tsv .v66aud/mis_clases.tsv | cut -f1-4
    .v66aud/aristas_lectura.tsv:agrupar_tareas_semejantes_aprovechar_preparacion	agrupar_interrupciones_subordinados_reuniones_regulares	SOSTENGO	pasos 1 y 3
    .v66aud/aristas_lectura.tsv:buscar_regularidad_bloques_iguales_trabajo_mando	canalizar_interrupciones_cartel_hora_oficina	SOSTENGO	paso 1
    .v66aud/mis_clases.tsv:agrupar_interrupciones_subordinados_reuniones_regulares	identificar_paso_limitante_jornada_desfases	SANO
    .v66aud/mis_clases.tsv:agrupar_interrupciones_subordinados_reuniones_regulares	llevar_inventario_proyectos_discrecionales	SANO
    .v66aud/mis_clases.tsv:agrupar_interrupciones_subordinados_reuniones_regulares	buscar_regularidad_bloques_iguales_trabajo_mando	SANO
    .v66aud/mis_clases.tsv:agrupar_interrupciones_subordinados_reuniones_regulares	preparar_respuestas_estandar_interrupciones_repetidas	SANO
    .v66aud/mis_clases.tsv:agrupar_interrupciones_subordinados_reuniones_regulares	sostener_contacto_oferta_aceptacion	SANO
    .v66aud/mis_clases.tsv:agendar_cuidados_propios_cumplirlos	agrupar_interrupciones_subordinados_reuniones_regulares	SANO
    .v66aud/mis_clases.tsv:agrupar_interrupciones_subordinados_reuniones_regulares	nombrar_delegados_amigos_casa	SANO
    .v66aud/mis_clases.tsv:agrupar_interrupciones_subordinados_reuniones_regulares	canalizar_interrupciones_cartel_hora_oficina	SANO

## 4. **LA FIDELIDAD DE `cap_05` Y `cap_06`, LEIDA ENTERA** (`D.30`, `D.58`, `8`)

Lei `fuentes/grove_high_output/cap_05.md` (Cap. 4, *Meetings, The Medium of Managerial Work*) y `cap_06.md`
(Cap. 5, *Decisions, Decisions*) enteros, y cada paso de los `20` contra su linea, con los pasos delante por
`pasos_ciego.py` (`.v68aud/pasos_cap05.txt`, `.v68aud/pasos_cap06.txt`).

    $ wc -l fuentes/grove_high_output/cap_05.md fuentes/grove_high_output/cap_06.md
      175 fuentes/grove_high_output/cap_05.md
       95 fuentes/grove_high_output/cap_06.md
      270 total

Una fila por paso en `.v68aud/fidelidad.tsv`: `T` transcripcion, `P` puente (**la clausula reescrita cuenta como
`P`**, `ACTA 62` `62.5`), `D` mi duda, con su capitulo y su linea. El contador es copia de
`.v66aud/contar_fidelidad.py` con las rutas cambiadas y **una fila por capitulo** (`8.2`), y cruza cada fila con los
pasos de la ficha de la bandeja de hoy:

    $ python .v68aud/contar_fidelidad.py
    candidato                                          ficha filas   T   P  DUDA
    infundir_regularidad_reunion_proceso                   8     8   8   0     0
    usar_tres_clases_reunion_proceso                       4     4   4   0     0
    fijar_frecuencia_reunion_individual_madurez_tarea     10    10  10   0     0
    fijar_duracion_lugar_reunion_individual               10    10  10   0     0
    preparar_guion_reunion_individual_subordinado          7     7   7   0     0
    cubrir_indicadores_problemas_reunion_individual       10    10  10   0     0
    facilitar_expresion_subordinado_pregunta_mas           6     6   6   0     0
    tomar_notas_copia_guion_reunion_individual             7     7   7   0     0
    acumular_asuntos_importantes_fichero_espera            4     4   4   0     0
    alentar_asuntos_corazon_vigilar_final_reunion          8     8   5   0     3
    conducir_reunion_individual_telefono_distancia         5     5   5   0     0
    programar_reunion_individual_cadena                    5     5   5   0     0
    conducir_etapas_modelo_ideal_decision                 12    12  12   0     0
    decidir_nivel_competente_inferior                      8     8   8   0     0
    vencer_sindrome_grupo_pares_autoconfianza              5     5   4   0     1
    tomar_mando_reunion_pares_presidente_ausente           6     6   6   0     0
    ejercer_poder_posicion_etapa_decision_clara            7     7   7   0     0
    cortar_discusion_libre_momento_justo                   7     7   7   0     0
    zanjar_seis_preguntas_decision_adelantado              9     9   9   0     0
    anunciar_decision_inesperada_reconvocar_reunion        8     8   8   0     0
    cap_05: candidatos 12 | pasos en ficha 84 | filas 84 | T 81 | P 0 | DUDA 3 | PUENTE 0 de 84 = 0.00 por ciento | si las DUDA cayesen: 3 de 84 = 3.57 por ciento
    cap_06: candidatos 8 | pasos en ficha 62 | filas 62 | T 61 | P 0 | DUDA 1 | PUENTE 0 de 62 = 0.00 por ciento | si las DUDA cayesen: 1 de 62 = 1.61 por ciento

**LECTURA: los dos capitulos son de inventario rico**, casi todo frases con mandato (*should*, *must*) o con el medio
nombrado, y los pasos lo transcriben pieza a pieza, a menudo frase a frase. **No encuentro ningun PUENTE.** Mis cuatro
dudas son **dos figuras**:

- `alentar_asuntos_corazon_vigilar_final_reunion` pasos `3`, `4` y `5`, *Preguntale si esta satisfecho / si alguna
  frustracion le carcome / si tiene dudas sobre adonde va*: L53 da las tres preguntas **como ejemplos del asunto de
  corazon a corazon**, en tercera persona, y no manda hacerselas; el verbo *Preguntale* es del extractor. Me inclino a
  `T`, porque *encourage the discussion of heart-to-heart issues* es sacarlos, y un lector estricto lo leeria clausula
  reescrita.
- `vencer_sindrome_grupo_pares_autoconfianza` paso `1`, *trabaja sobre la autoconfianza de cada uno*: L49 da una
  condicion (*You can overcome ... if each of the members has self-confidence*), no un acto. Me inclino a `T` porque los
  pasos `2` a `5` son el como que el libro da, y el `5` (*everyone in your operation should be made to understand
  this*) si es mandato.

**Y lo que NO marco duda, para que se vea el criterio:** `tomar_notas_copia_guion_reunion_individual` paso `4`
(*Toma las notas en forma de guion*) convierte en mandato una practica en primera persona (*Since I take notes in
outline form*), que es la figura de `reunir_informacion` paso `1` que la `66` leyo `T`; y
`fijar_frecuencia_reunion_individual_madurez_tarea` paso `1` (*en vez de poner la misma frecuencia para todas*) es glosa
de *each of your subordinates*.

**`PASOS INVENTADOS` por mi instrumento: `cap_05` `0` de `84` y `cap_06` `0` de `62`; si mis dudas cayesen, `3` de `84`
y `1` de `62`.** Por debajo del `10` en las dos lecturas. Es preparacion y no entrada. **Coincide con el `0 de 84 y 0 de
62` del asunto de `9de244e`, y lo digo como coincidencia**; paso a paso lo cruzo en mi turno normal.

## 5. **MI BARRIDO DE LOS `22`, SOBRE GRAFO MAS BANDEJAS** (`D.38.4`, `D.38.5`)

Copia de `.v66aud/barrido_uno.py` (la ficha normalizada como la aduana, contra `dataset/nodos.jsonl` mas
`aduana.poblacion_de_bandejas`, con `buscar_vecinos` de `src/aduana.py`) y de `.v66aud/barrer.sh` con la lista
cambiada: las dos filas desde `_insertados` y los `20` desde la bandeja, **cinco a la vez, recogido entero dentro de
este turno**. Antes de lanzarlo guarde la huella de cada ficha y del grafo, y al recogerlo las comprobe:

    $ head -1 .v68aud/barrido.log; tail -1 .v68aud/barrido.log; grep -c "rc=0" .v68aud/barrido.log; grep -c "rc=" .v68aud/barrido.log
    INICIO 2026-09-24 21:59:17
    TODOS TERMINADOS 2026-09-25 01:32:24
    22
    22
    $ sha1sum -c --quiet .v68aud/huellas_al_barrer.txt && echo "bandeja de grove, las dos filas y el grafo: mismas huellas que al barrer"
    bandeja de grove, las dos filas y el grafo: mismas huellas que al barrer
    $ cat .v68aud/head_al_barrer.txt; git rev-parse HEAD
    3d285956ff2896d3cdebea7257b3273f4644f3dc
    3d285956ff2896d3cdebea7257b3273f4644f3dc

**UN ARRANQUE FALLIDO, DICHO:** el primer lanzamiento llevaba mal la lista (tome las lineas `25` a `44` de
`.v66aud/cola_grove.txt` sin descontar su cabecera, lo que dejaba fuera `infundir_regularidad_reunion_proceso` y metia
`planificar_tres_pasos_demanda_estado_brecha` de `cap_07`). Lo pare a los pocos segundos, mate el arbol entero de
procesos, borre sus salidas y relance con las filas `23` a `42`. Su log queda en `.v68aud/barrido_abortado.log`, y
ninguna cifra de esta pagina sale de el:

    $ cat .v68aud/barrido_abortado.log
    INICIO 2026-09-24 21:58:06
    fijar_frecuencia_reunion_individual_madurez_tarea rc=127 segundos=33
    agrupar_interrupciones_subordinados_reuniones_regulares rc=127 segundos=33
    canalizar_interrupciones_cartel_hora_oficina rc=127 segundos=33
    usar_tres_clases_reunion_proceso rc=127 segundos=33
    fijar_duracion_lugar_reunion_individual rc=127 segundos=33
    preparar_guion_reunion_individual_subordinado rc=1 segundos=7
    cubrir_indicadores_problemas_reunion_individual rc=1 segundos=8
    facilitar_expresion_subordinado_pregunta_mas rc=1 segundos=8
    tomar_notas_copia_guion_reunion_individual rc=1 segundos=8
    acumular_asuntos_importantes_fichero_espera rc=1 segundos=8
    $ sed -n '24p;43p' .v66aud/cola_grove.txt; head -1 .v68aud/los20.txt; tail -1 .v68aud/los20.txt
     23  cap_05 P6   infundir_regularidad_reunion_proceso                    pasos 8
     42  cap_06 P31  anunciar_decision_inesperada_reconvocar_reunion         pasos 8
    infundir_regularidad_reunion_proceso
    anunciar_decision_inesperada_reconvocar_reunion

**Poblacion y vecinos por candidato:**

    $ python .v68aud/vecinos_tabla.py | tee .v68aud/vecinos_tabla.txt | sed -n '1,/^sin fichero/p'
    (1) candidato | poblacion | vecinos | en grafo | en bandeja
        agrupar_interrupciones_subordinados_reuniones_regulares  479   8   8   0
        canalizar_interrupciones_cartel_hora_oficina             479   1   1   0
        infundir_regularidad_reunion_proceso                     479   5   0   5
        usar_tres_clases_reunion_proceso                         479   5   0   5
        fijar_frecuencia_reunion_individual_madurez_tarea        479   6   0   6
        fijar_duracion_lugar_reunion_individual                  479   7   0   7
        preparar_guion_reunion_individual_subordinado            479   9   0   9
        cubrir_indicadores_problemas_reunion_individual          479   6   0   6
        facilitar_expresion_subordinado_pregunta_mas             479   8   0   8
        tomar_notas_copia_guion_reunion_individual               479   7   0   7
        acumular_asuntos_importantes_fichero_espera              479   6   0   6
        alentar_asuntos_corazon_vigilar_final_reunion            479   7   0   7
        conducir_reunion_individual_telefono_distancia           479   6   1   5
        programar_reunion_individual_cadena                      479   7   2   5
        conducir_etapas_modelo_ideal_decision                    479   0   0   0
        decidir_nivel_competente_inferior                        479   3   0   3
        vencer_sindrome_grupo_pares_autoconfianza                479  13   3  10
        tomar_mando_reunion_pares_presidente_ausente             479   4   0   4
        ejercer_poder_posicion_etapa_decision_clara              479   2   0   2
        cortar_discusion_libre_momento_justo                     479   6   1   5
        zanjar_seis_preguntas_decision_adelantado                479   2   0   2
        anunciar_decision_inesperada_reconvocar_reunion          479   9   1   8
    sin fichero de vecinos: 0 []
    $ grep -c ">" .v68aud/vecinos_tabla.txt
    127
    $ grep ">" .v68aud/vecinos_tabla.txt | grep -c " grafo "
    17
    $ tail -1 .v68aud/vecinos_tabla.txt
    pares sin orden: 78 | {'con fuera': 28, 'tanda-tanda': 50}

**Las filas de vecino de los `20`, sin las dos filas de `cap_04`, y los pares sin orden que tocan a los `20`:**

    $ grep ">" .v68aud/vecinos_tabla.txt | grep -Ev "^    (agrupar_interrupciones|canalizar_interrupciones)" | wc -l
    118
    $ grep "~" .v68aud/vecinos_tabla.txt | grep -Ev "agrupar_interrupciones_subordinados|canalizar_interrupciones_cartel" | awk '{print $4}' | sort | uniq -c
         20 con
         50 tanda-tanda
    $ grep ">" .v68aud/vecinos_tabla.txt | grep -Ev "^    (agrupar_interrupciones|canalizar_interrupciones)" | grep " grafo "
        conducir_reunion_individual_telefono_distancia         > preguntar_conducir_reunion_individual                  grafo   familia_id       0.077 0.500 0.395
        programar_reunion_individual_cadena                    > preguntar_conducir_reunion_individual                  grafo   familia_id       0.080 0.333 0.418
        programar_reunion_individual_cadena                    > dirigir_reunion_individual_semanal                     grafo   familia_id       0.049 0.333 0.350
        vencer_sindrome_grupo_pares_autoconfianza              > aprender_resultados_vencer_dos_presiones               grafo   paso_contra_nodo 0.217 0.111 0.712
        vencer_sindrome_grupo_pares_autoconfianza              > archivar_indicadores_resolver_problemas                grafo   similitud_texto  0.363 0.000 0.396
        vencer_sindrome_grupo_pares_autoconfianza              > supervisar_decision_delegada_preguntas_concretas       grafo   similitud_texto  0.364 0.000 0.379
        cortar_discusion_libre_momento_justo                   > construir_indicador_tendencia_patron                   grafo   similitud_texto  0.353 0.000 0.401
        anunciar_decision_inesperada_reconvocar_reunion        > dirigir_reunion_decision                               grafo   familia_id       0.171 0.333 0.420

**Y las dos filas de `cap_04` contra mi barrido sellado de la `66`:**

    $ python .v68aud/filas_66_68.py
    agrupar_interrupciones_subordinados_reuniones_regulares | 66: 8 | hoy: 8 | solo 66: [] | solo hoy: [] | de hoy con su fila en .v66aud/mis_clases.tsv: 8
    canalizar_interrupciones_cartel_hora_oficina | 66: 1 | hoy: 1 | solo 66: [] | solo hoy: [] | de hoy con su fila en .v66aud/mis_clases.tsv: 1

**LECTURA:**

1. **Las filas `21` y `22` levantan hoy exactamente los vecinos que levantaron en mi barrido de la `66`**, `8` y `1`,
   todos del grafo; **esas nueve filas son ocho pares, porque las dos se levantan entre si, y los ocho tienen su clase en mi
   `.v66aud/mis_clases.tsv` sellada**. Si su aduana midio lo
   que yo mido, no pudo levantar un vecino sin linea preparada; eso lo cruzo contra su bitacora en mi turno normal.
2. **Los `20` dan `118` filas de vecino.** Coincide con el `118` del asunto de `9de244e`, que ahi se llama *pares*, y lo
   digo como coincidencia. En pares sin orden son `50` entre dos de la tanda y `20` con uno de fuera (el `con` de la salida es `con fuera`, que
   `awk` parte en dos).
3. **`conducir_etapas_modelo_ideal_decision` no levanta a nadie**, contra `479`; lo levantan otros. **`vencer_sindrome`
   levanta `13`**: cinco hermanos de `cap_06` y ocho de lejos (`cap_07` y otros capitulos de Grove, Scott), por
   `similitud_texto` entre `0,35` y `0,43`, y uno por `paso_contra_nodo` `0,712` que es el mismo verbo (*apoya en la experiencia* contra *aprende de la experiencia*).
4. **Los `8` vecinos del grafo** son tres de Zhuo (`preguntar_conducir_reunion_individual` y
   `dirigir_reunion_individual_semanal`, levantados por `familia_id` desde el telefono y el calendario en cadena, y
   `dirigir_reunion_decision` desde `anunciar`), `aprender_resultados_vencer_dos_presiones` de Scott, y tres de Grove ya
   insertados (`archivar_indicadores`, `supervisar_decision_delegada`, `construir_indicador_tendencia`).
5. **LO QUE EL BARRIDO NO LEVANTA Y SE LEE:** `agrupar_interrupciones` no levanta `acumular_asuntos_importantes_fichero_espera`,
   e `infundir_regularidad` no levanta `buscar_regularidad`: las dos relaciones van por lectura (seccion `7`). **Y NO
   LEVANTA EL CHOQUE DE DOCTRINA DE LOS DOS LIBROS SOBRE EL UNO A UNO**: Zhuo pone la reunion *no menos de una por semana y
   de treinta minutos* (`dirigir_reunion_individual_semanal` paso `2`), y Grove pone la frecuencia por la madurez de tarea
   (`fijar_frecuencia` pasos `6` y `7`, *una vez cada pocas semanas* con el veterano) y *una hora como minimo*
   (`fijar_duracion` paso `3`). **Dos doctrinas legitimas no son duplicado** (`6.1`): es frontera, y ningun par del
   barrido la lleva. No abro linea por mi cuenta; lo dejo para mi turno normal, **como pregunta y no como caida de
   nadie**, y la doctrina esta congelada (`D.55`).

**EL RELOJ, medido y no techo:** de `857` a `5488` s por ficha, de las `21:59:17` del 24 a las `01:32:24` del 25.

    $ grep "rc=" .v68aud/barrido.log | sed 's/.*segundos=//' | sort -n | sed -n '1p;$p'
    857
    5488

## 6. **MI LECTURA CIEGA DE LOS PARES** (`1.2`, `6.1`, y solo la vara `6.1`)

**Leidos con los pasos de los dos delante**, todos con `pasos_ciego.py` (`R6`): `.v68aud/pasos_cap05.txt`,
`.v68aud/pasos_cap06.txt` para los `20`, y `.v68aud/pasos_fuera_a.txt`, `.v68aud/pasos_fuera_b.txt` y
`.v68aud/pasos_pares.txt` para los de fuera. **Una fila por par** en `.v68aud/mis_clases.tsv`, con su razon. El cruce
comprueba que cada par del barrido tiene su fila y cada fila su par:

    $ python .v68aud/cruce_clases.py
    pares del barrido: 78 | filas de clase: 78
    pares sin fila: []
    filas sin par: []
    clases: {'SANO': 76, 'CONTINUA': 2}
    con DUDA escrita: 3
      CONTINUA  tomar_notas_copia_guion_reunion_individual ~ conducir_reunion_individual_telefono_distancia | madre tomar_notas_copia_guion_reunion_individual
      CONTINUA  preparar_guion_reunion_individual_subordinado ~ tomar_notas_copia_guion_reunion_individual | madre preparar_guion_reunion_individual_subordinado

**De donde sale cada fila:** los pares de dentro de `cap_05` y de dentro de `cap_06` los escribi **todos** (`94`) antes de
que el barrido terminara, en `.v68aud/clases_intra.txt`; los de fuera, al recogerlo, en `.v68aud/clases_fuera.txt`; y los
ocho pares de las filas `21` y `22` son los de mi lectura sellada de la `66`, sin tocar. `armar_clases.py` los junta:

    $ python .v68aud/armar_clases.py
    pares del barrido: 78 | filas escritas: 78 | sin clase: 0 []
    de donde sale cada fila: {'intra': 50, 'la 66': 8, 'fuera': 20}
    $ grep -v "^[#@]" .v68aud/clases_intra.txt | wc -l
    94

**LECTURA, los dos `CONTINUA`**, y en los dos el hijo trae procedimiento propio, asi que ninguno es `REPITE`:

- `preparar_guion_reunion_individual_subordinado` madre de `tomar_notas_copia_guion_reunion_individual`: la condicion del
  hijo (*la reunion individual ya tiene su guion preparado*) es el producto de la madre, y el hijo anade la copia a cada
  parte, las notas, lo que simbolizan y el seguimiento (L41, L49).
- `tomar_notas_copia_guion_reunion_individual` madre de `conducir_reunion_individual_telefono_distancia`: el hijo adapta
  la toma de notas a la distancia (*note-taking can't work in the same way*, L55) y anade el intercambio al terminar.

**MIS TRES DUDAS EN PARES QUE EL BARRIDO LEVANTA, escritas antes de saber:** el `CONTINUA` de telefono **puede leerse
SANO de variantes hermanas**, porque su condicion es geografica y no el producto de las notas; el `SANO` de
`ejercer_poder` con `cortar_discusion` **puede leerse `CONTINUA` con madre `cortar`**, porque la condicion de `ejercer`
(*el momento de decidir ha llegado claramente*) es lo que `cortar` decide; y el `SANO` de `preparar_guion` con
`cubrir_indicadores` **puede leerse `CONTINUA` con madre `preparar`**, porque la condicion de `cubrir` dice *o
preparando su guion*. Si alguna me cae, cae dentro de lo que marco aqui.

**Y LOS PARES CON OTRO LIBRO:** los cuatro con Zhuo los leo `SANO`: dos libros sobre la misma reunion, **ningun paso
compartido** en el par que el barrido levanta. El unico que se acerca es `anunciar` con `dirigir_reunion_decision`: los
dos vuelven a reunir a la gente, Zhuo para **rehacer** una decision de proceso malo y Grove para que la gente **digiera y
opine** una palabra final inesperada. El mismo gesto con dos fines.

## 7. **LAS ARISTAS POR LECTURA** (`D.29`, `D.37`, `D.53`)

**Las que mi lectura sostiene o descarta**, una fila cada una en `.v68aud/aristas_lectura.tsv` con su tramo de madre,
de hijo y su linea del libro. El cruce dice si el barrido levanto el par (entonces no es arista por lectura sino
linea de veredicto) y donde vive hoy cada extremo:

    $ python .v68aud/cruce_aristas.py
    SOSTENGO, DUDA buscar_regularidad_bloques_iguales_trabajo_mando   (grafo) > infundir_regularidad_reunion_proceso                   (bandeja) | levantado por el barrido: no
    NO, DUDA       agrupar_tareas_semejantes_aprovechar_preparacion   (grafo) > infundir_regularidad_reunion_proceso                   (bandeja) | levantado por el barrido: no
    SOSTENGO       agrupar_interrupciones_subordinados_reuniones_regulares (grafo) > acumular_asuntos_importantes_fichero_espera            (bandeja) | levantado por el barrido: no
    EN VEREDICTO   preparar_guion_reunion_individual_subordinado      (bandeja) > tomar_notas_copia_guion_reunion_individual             (bandeja) | levantado por el barrido: SI
    EN VEREDICTO, DUDA tomar_notas_copia_guion_reunion_individual         (bandeja) > conducir_reunion_individual_telefono_distancia         (bandeja) | levantado por el barrido: SI
    NO             preparar_guion_reunion_individual_subordinado      (bandeja) > conducir_reunion_individual_telefono_distancia         (bandeja) | levantado por el barrido: no
    NO, DUDA       preparar_guion_reunion_individual_subordinado      (bandeja) > cubrir_indicadores_problemas_reunion_individual        (bandeja) | levantado por el barrido: SI
    NO, DUDA       elegir_estilo_direccion_madurez_relevante_tarea    (bandeja) > fijar_frecuencia_reunion_individual_madurez_tarea      (bandeja) | levantado por el barrido: no
    NO             supervisar_tarea_delegada_etapa_menor_valor        (grafo) > fijar_frecuencia_reunion_individual_madurez_tarea      (bandeja) | levantado por el barrido: no
    SOSTENGO       conducir_etapas_modelo_ideal_decision              (bandeja) > ejercer_poder_posicion_etapa_decision_clara            (bandeja) | levantado por el barrido: no
    SOSTENGO       conducir_etapas_modelo_ideal_decision              (bandeja) > cortar_discusion_libre_momento_justo                   (bandeja) | levantado por el barrido: no
    NO, DUDA       conducir_etapas_modelo_ideal_decision              (bandeja) > decidir_nivel_competente_inferior                      (bandeja) | levantado por el barrido: no
    NO, DUDA       cortar_discusion_libre_momento_justo               (bandeja) > ejercer_poder_posicion_etapa_decision_clara            (bandeja) | levantado por el barrido: SI
    NO             vencer_sindrome_grupo_pares_autoconfianza          (bandeja) > tomar_mando_reunion_pares_presidente_ausente           (bandeja) | levantado por el barrido: SI
    NO             tomar_mando_reunion_pares_presidente_ausente       (bandeja) > ejercer_poder_posicion_etapa_decision_clara            (bandeja) | levantado por el barrido: no
    NO             zanjar_seis_preguntas_decision_adelantado          (bandeja) > anunciar_decision_inesperada_reconvocar_reunion        (bandeja) | levantado por el barrido: SI
    NO, DUDA       usar_tres_clases_reunion_proceso                   (bandeja) > fijar_frecuencia_reunion_individual_madurez_tarea      (bandeja) | levantado por el barrido: SI
    filas: 17 | SOSTENGO: 4 | NO: 5 | levantadas por el barrido: 7

**LECTURA:**

- **Cuatro `SOSTENGO` por lectura, ninguno levantado por el barrido.** Dos con la madre **ya en el grafo**:
  `buscar_regularidad_bloques_iguales_trabajo_mando` madre de `infundir_regularidad_reunion_proceso` (**con DUDA**: la
  condicion del hijo, una reunion en calendario fijo, es el producto de los pasos `8` y `9` de la madre, pero se puede
  leer como el mismo principio aplicado a dos objetos), y `agrupar_interrupciones_subordinados_reuniones_regulares`, **la
  fila `21` que acaba de entrar**, madre de `acumular_asuntos_importantes_fichero_espera` (L51 remite con palabras: *the
  interruptions we considered earlier*). Y dos con los dos extremos en la tanda: `conducir_etapas_modelo_ideal_decision`
  madre de `ejercer_poder_posicion_etapa_decision_clara` (L61) y de `cortar_discusion_libre_momento_justo` (L63).
- **Dos `EN VEREDICTO`**: las dos relaciones de las notas las levanta el barrido, asi que no son aristas por lectura sino
  las dos lineas `CONTINUA` con `madre=` de la seccion `6`, como la de `detectar_arreglar` en la `66`.
- **Los `NO`, para que se vea el criterio**, y los que llevan DUDA la llevan escrita en su fila: `agrupar_tareas` no es
  madre directa de `infundir` ni de `acumular` (queda de abuela, como `D67.4`); `decidir_nivel` es un rasgo del modelo y
  no su continuacion (L33, *another feature of the model*); `vencer_sindrome` y `tomar_mando` son dos remedios del mismo
  sindrome; y **`fijar_frecuencia` no cuelga de `elegir_estilo_direccion_madurez_relevante_tarea`** (cap_13, en la
  bandeja): su paso `5` nombra el estilo por madurez con un *Cuenta con* y su paso `3` mide la madurez por su cuenta.
  **Es la que la `66` dejo escrita para cuando entrara su hijo** (`supervisar_tarea` paso `6`), y la leo igual: nombrar no
  es procedimentar.

**`D.37`, LOS TITULOS QUE DICEN CUANTAS PARTES TIENEN:** dos, y los dos dicen cuantas **y** las nombran:
`usar_tres_clases_reunion_proceso` (el uno a uno, la reunion de personal y la revision de operaciones) y
`zanjar_seis_preguntas_decision_adelantado` (que, cuando, quien decide, a quien se consulta, quien ratifica o veta, a
quien se informa). La busqueda de cada parte por id y titulo sobre grafo mas bandejas:

    $ python .v68aud/d37_partes.py
    poblacion: 479
    tres clases: uno a uno: 16
        dirigir_reunion_individual_semanal                           ['zhuo_manager']
        preguntar_conducir_reunion_individual                        ['zhuo_manager']
        abrazar_incomodidad_arrancar_critica_equipo                  ['scott_radical_candor']
        montar_equipo_gestion_desempenio_revisar_sistema             ['scott_radical_candor']
        agrupar_interrupciones_subordinados_reuniones_regulares      ['grove_high_output']
        construir_estrategia_gente_cuatro_componentes                ['gerber_emyth']
        alentar_asuntos_corazon_vigilar_final_reunion                ['grove_high_output']
        conducir_reunion_individual_telefono_distancia               ['grove_high_output']
        cubrir_indicadores_problemas_reunion_individual              ['grove_high_output']
        facilitar_expresion_subordinado_pregunta_mas                 ['grove_high_output']
        fijar_duracion_lugar_reunion_individual                      ['grove_high_output']
        fijar_frecuencia_reunion_individual_madurez_tarea            ['grove_high_output']
        preparar_guion_reunion_individual_subordinado                ['grove_high_output']
        programar_reunion_individual_cadena                          ['grove_high_output']
        tomar_notas_copia_guion_reunion_individual                   ['grove_high_output']
        usar_tres_clases_reunion_proceso                             ['grove_high_output']
    tres clases: reunion de personal: 3
        organizar_jornada_entrevistas_candidato                      ['smart_who']
        conducir_reunion_equipo_agenda_tres_bloques                  ['scott_radical_candor']
        usar_tres_clases_reunion_proceso                             ['grove_high_output']
    tres clases: revision de operaciones: 1
        usar_tres_clases_reunion_proceso                             ['grove_high_output']
    seis preguntas: que decision: 0
    seis preguntas: cuando: 0
    seis preguntas: quien decide: 2
        montar_reunion_gran_decision                                 ['scott_radical_candor']
        zanjar_seis_preguntas_decision_adelantado                    ['grove_high_output']
    seis preguntas: a quien consultar: 1
        zanjar_seis_preguntas_decision_adelantado                    ['grove_high_output']
    seis preguntas: quien ratifica o veta: 2
        montar_reunion_gran_decision                                 ['scott_radical_candor']
        zanjar_seis_preguntas_decision_adelantado                    ['grove_high_output']
    seis preguntas: a quien informar: 0

**LECTURA: ninguna parte existe como nodo.** Lo que la busqueda levanta para *uno a uno* son los diez de la tanda,
cada uno **un aspecto** del uno a uno (frecuencia, duracion y lugar, guion, contenido, papel, notas, fichero, corazon a
corazon, telefono, calendario) y ninguno **el** uno a uno; la propia cabeza; dos de Zhuo que son la reunion individual
de **otro libro**; `agrupar_interrupciones`, que usa las reuniones; y dos de Scott y uno de Gerber que la nombran de
pasada; *reunion de personal* levanta la reunion de equipo de Scott
y una jornada de entrevistas de Smart, que no son la parte de Grove; y las seis preguntas solo se encuentran a si
mismas y a `montar_reunion_gran_decision` de Scott, que es una reunion entera y no una pregunta. **`D.37` no dispara
en ninguno de los dos**, con el criterio que la `66` uso con `subir_productividad`. **La duda de la cabeza de serie la
dejo escrita en la ultima fila de `aristas_lectura.tsv`.**

## 8. **EL ORDEN QUE MI LECTURA OBLIGA** (`D.36`)

**No es un orden: son las restricciones**, escritas antes de ver el del extractor. Madre antes que hijo por mis
`CONTINUA` y mis `SOSTENGO` con los dos extremos en la tanda, y cuantas cumple el orden de pieza del libro:

    $ python .v68aud/restricciones_orden.py
    restricciones: 6
      tomar_notas_copia_guion_reunion_individual           antes que conducir_reunion_individual_telefono_distancia           CONTINUA               el orden del libro la cumple
      preparar_guion_reunion_individual_subordinado        antes que tomar_notas_copia_guion_reunion_individual               CONTINUA               el orden del libro la cumple
      conducir_etapas_modelo_ideal_decision                antes que ejercer_poder_posicion_etapa_decision_clara              arista por lectura     el orden del libro la cumple
      conducir_etapas_modelo_ideal_decision                antes que cortar_discusion_libre_momento_justo                     arista por lectura     el orden del libro la cumple
      anunciar_decision_inesperada_reconvocar_reunion      antes que decidir_nivel_competente_inferior                        D.36, solo lo levanta decidir_nivel_competente_inferior EL ORDEN DEL LIBRO LA VIOLA
      ejercer_poder_posicion_etapa_decision_clara          antes que vencer_sindrome_grupo_pares_autoconfianza                D.36, solo lo levanta vencer_sindrome_grupo_pares_autoconfianza EL ORDEN DEL LIBRO LA VIOLA
    que obligan (madre antes que hijo): 4 | violadas por el orden del libro: 0
    D.36 de un solo lado, informativas: 2
    ultimas dos del orden del libro: ['zanjar_seis_preguntas_decision_adelantado', 'anunciar_decision_inesperada_reconvocar_reunion']

**LECTURA:** las cuatro que obligan (`preparar_guion` antes que `tomar_notas`, `tomar_notas` antes que el telefono, y
`conducir_etapas` antes que `ejercer_poder` y que `cortar_discusion`) **las cumple ya el orden de pieza del libro**. Las
dos `D.36` de un solo lado son informativas y **no obligan**, porque la aduana de `insertar` mide grafo mas bandejas
(`D.38.5`). Las dos madres de la seccion `7` que viven en el grafo no ponen orden. **Su orden, contra estas cuatro, lo
compruebo en mi turno normal.**

## 9. **LO QUE DEJO PARA MI TURNO NORMAL, ESCRITO ANTES DE VER EL REPORTE**

1. **`R5`** en su reporte, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` sacados otra vez de los
   originales y con la cabecera cambiada a la `68`.
2. **Las filas `21` y `22`**: sus `11` lineas nuevas de bitacora contra sus bloques de `.v66ext/veredictos_listos.txt`
   letra a letra y sus dos aristas contra las dos de la seccion `3`, **par a par**; y los relojes sin solape.
3. **Mi fidelidad contra la suya, paso a paso**: `146` filas mias contra las suyas. Si mis cuatro `D` se quedan en `T`,
   las dos cifras siguen en `0`; si alguna cae a PUENTE, cae dentro de lo que marque aqui; **y si el marca PUENTE un
   paso que yo lei `T` sin duda, y gana, la caida de lectura es mia.**
4. **Mis clases contra sus lineas de veredicto, par a par**, y mis `SOSTENGO` contra sus aristas por lectura, por par y
   no por cuenta (**el asunto de `9de244e` dice `118` pares y `9` aristas**).
5. **Su orden contra mis restricciones.**
6. **La huella de las `20` fichas** que su cierre dice sellar, contra las mias de `.v68aud/huellas_al_barrer.txt`.
7. **La muestra pineada de los SANO**: esta vuelta solo escribe en la bitacora los de las filas `21` y `22`; los de
   `cap_05` y `cap_06` se muestrean cuando entren, en la `70`.

**Y ESTA PAGINA CONTRA `R6`, medido sobre ella misma:** el generador corre dos veces, y este bloque de la segunda
pasada lee la pagina que escribio la primera, identica salvo este bloque. Cuenta las lineas de bloque `$` que
empiezan por una clave de relacion; las que la nombran en mis frases y comandos no cuentan, porque la nombran para
decir que no la imprimo:

    $ grep -c -E "^    +(previos|siguientes|nodos_previos|nodos_siguientes)" docs/loop/APERTURA_CIEGA.md
    0
