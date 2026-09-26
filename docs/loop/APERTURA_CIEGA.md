# APERTURA CIEGA DE LA VUELTA 78, lote 5 (`marquet_turn_the_ship`), **CLASE INSERCION, VUELTA DE PREPARACION**

*Auditor `claude-opus-5-5`, fase ciega, 26 sep 2026. En la corrida que arranco el 26 a las `09:27`, el arnes la numera `VUELTA 2`.
Linea **serial**, rama `extraccion-mundo-11`. Modo austero (`D.47`). Todo lo de esta pagina sale de `.v78aud/`, escrito y
corrido en esta fase; cada bloque `$` lo pega `.v78aud/generar_apertura.py` corriendo el comando en el momento de escribirla.
**No hay ninguna tabla en esta pagina**, a proposito, como en la `73`, la `75`, la `76` y la `77`.*

**LO QUE ESTA VUELTA TENIA QUE HACER, Y LO QUE CLASIFICO A CIEGAS** (mi encargo, `docs/loop/PROMPT_SIGUIENTE.md`): **dejar listas sin
insertar ninguna las fichas de la bandeja de Marquet**: su fidelidad leida entera (con `d150` preparada), su barrido, sus veredictos,
sus aristas por lectura y su orden. **Yo hago lo mismo por mi cuenta**: leo enteros los trece capitulos que las fichas citan y cada
paso contra su linea (seccion `3`), barro las fichas sobre grafo mas bandejas (seccion `4`), escribo mis clases y mis aristas
(secciones `5` y `6`) y las restricciones de orden que mi lectura pone (seccion `7`).

**UNA LIMITACION DE METODO, DICHA ANTES DE NADA: EN ESTA FASE NO HE CORRIDO `git` SOBRE EL REPOSITORIO**, ni una vez, como en la
`73`, la `75`, la `76` y la `77`: la carpeta de una linea viva es solo del arnes (`PARALELO.md` `7`). **Lo que se mide con `git` aqui
no lo mido**: que commit movio que y a que hora, y el contenido viejo de las fichas que cambiaron. Lo que si mido sin `git` es que
ficheros son mas nuevos que mi encargo y que fichas cambiaron contra mis propias huellas de la `76` (seccion `2`). El commit en que
esta el arbol lo leo de los ficheros de `.git/`:

    $ cat .git/HEAD; cat .git/refs/heads/extraccion-mundo-11
    ref: refs/heads/extraccion-mundo-11
    463248f5cbb605331345f3b6eadea40ee22a2453

## 0. **LA HERENCIA** (`D.40`)

ACTA ANTERIOR LEIDA: f790389111f662ce8d8133e3ddd7256d4b8cd98d

**Comprobada sin git**: es el blob de `docs/loop/ACTA_AUDITOR.md` tal como esta hoy en el arbol, calculado como lo calcula git. **La
`ACTA 76` la lei entera**, de su linea de cabecera a la ultima del fichero, y con ella el encargo que me deje. **No hay hueco de acta**
(`1.0`): la `ACTA 76` cubre la vuelta `77`, y la que viene a auditarse es la `78`.

    $ python .v78aud/huella_acta.py
    sha1 del blob tal cual: 7689ab047fe1db1717d7b7ff7415c4f310f1f600
    lineas con CRLF en el arbol: 466 | sha1 del blob normalizado a LF: f790389111f662ce8d8133e3ddd7256d4b8cd98d
    lineas del fichero: 51327 | la ACTA 76 empieza en la linea: [50764]

HEREDADO 1: NO APLICA en esta fase. **Motivo:** `R5` es un remedio **del extractor** y se mide **sobre su reporte de la `78`**
(`ACTA 76` `76.12`: *el reporte de la `78`, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera cambiada a
la `78`*), y el reporte **no esta en el arbol**: el arnes lo retiro para esta fase (`D.34.2`) y no lo he recuperado por ninguna via.
**Se mide en mi turno normal**, con los dos instrumentos sacados otra vez de los originales y no de las copias del extractor. Lo que
si esta en mi mano lo cumplo en mi pagina: cada bloque `$` lleva la salida del comando que abre, y nada mas.

    $ ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl
    ls: cannot access 'docs/loop/REPORTE.md': No such file or directory
    ls: cannot access 'docs/loop/ultimo_extractor.json': No such file or directory
    ls: cannot access 'docs/loop/ultimo_auditor.json': No such file or directory
    ls: cannot access 'docs/loop/CREDITO_serial.jsonl': No such file or directory
    $ grep -n "VUELTA 2 : APERTURA CIEGA" docs/loop/loop.log | tail -1
    9063:[2026-09-26 15:03:22] VUELTA 2 : APERTURA CIEGA (claude-opus-5-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl

HEREDADO 2: CUMPLIDO. **`R6`, mio** (`ACTA 76` `76.12`): en esta fase los pasos de cualquier nodo los imprime
`.v67aud/normal/pasos_ciego.py`, que no ensenia `previos` ni `siguientes`: con el lei las fichas (`.v78aud/pasos_20.txt`) y los nodos
de fuera que el barrido levanta (`.v78aud/pasos_fuera.txt`), y los bloques de pasos de esta pagina los corre el. Las lineas de esos
ficheros que **empiezan** por una clave de relacion, y los instrumentos mios de esta fase que las **nombran**:

    $ grep -c -E "^ *(previos|siguientes|nodos_previos|nodos_siguientes)" .v78aud/pasos_20.txt .v78aud/pasos_fuera.txt
    .v78aud/pasos_20.txt:0
    .v78aud/pasos_fuera.txt:0
    $ grep -l -E "previos|siguientes" .v78aud/*.py | wc -l
    0

**LO UNICO QUE SE ACERCA, para que se juzgue:** al abrir la fase imprimi las claves de UNA ficha de la bandeja
(`contar_firmas_cadena_tramite_parado`) con la longitud de cada valor, para saber su forma, y ahi salieron `nodos_previos` y
`nodos_siguientes` **con su valor, que es la lista vacia**, como manda `D.29` para toda ficha en cuarentena. **No vi ninguna clave de
relacion con valor de ningun nodo del grafo en esta fase.** La pagina entera la mide un `grep` sobre ella al cerrarla (seccion `10`).

HEREDADO 3: CUMPLIDO. **`R7`, mio** (`ACTA 76` `76.12`): toda linea de esta pagina que reparte un total en clases la imprime un
instrumento que cuenta **todas** las clases con el mismo predicado y **dice su `suma`**: los de `.v78aud/` la traen, copiados de los
de la `76` o escritos en esta fase con ella, y los que reuso sin copiar (`.v70aud/poblacion.py`, `.v77aud/normal/bandeja_marquet.py` y
el de `R8`) ya la traian. **Medido sobre la pagina misma** en la seccion `10`, con la copia de `.v76aud/r7_pagina.py`.

HEREDADO 4: CUMPLIDO. **`R8`, mio** (`ACTA 76` `76.12`, *mi fase ciega de la `78`, sobre el encargo de la `78`*): **lo mido aqui con
el mismo instrumento de la `76.13`, sin copiarlo**, y su salida de hoy es identica a la que aquella acta guardo; la lectura, en la
seccion `8`. El encargo de la `79` lo escribo en mi turno normal y se mide alli.

HEREDADO 5: NO APLICA en esta fase. **Motivo:** `R9` es un remedio **del extractor** y se comprueba **en el reporte de la `78`, en su
cuenta de PUENTE** (`ACTA 76` `76.12`), que el arnes retiro (bloque del HEREDADO `1`). **Lo que si esta en mi mano**, y lo cumplo en mi
lectura: **cada una de mis filas de fidelidad trae su tramo literal del libro, y el instrumento comprueba que ese tramo esta en la
linea que cito** (seccion `3`); el cruce de su patron con el mio, en mi turno normal:

    $ python .v78aud/contar_fidelidad.py | tail -1
    citas: filas 110 | el tramo esta en su linea: 110 | no esta: 0 | suma: 110

HEREDADO 6: CUMPLIDO. **`R10`, mio** (`ACTA 76` `76.12` y `76.14`): toda salida pegada en `PROMPT_SIGUIENTE.md` se corre despues de la
ultima escritura del auditor en el registro que mide, o se vuelve a correr antes del commit y se compara. **Lo mido sobre el encargo
de la `78`**: las cuatro salidas pegadas (el reloj del barrido de la `76`, la clase, el tablero y el texto de `d150`) **salen hoy
identicas a lo pegado**, con la copia de `.v77aud/normal/r10.sh`. **Una limitacion, dicha:** la copia no lee la hora de
`CREDITO_serial.jsonl`, porque el arnes lo retiro en esta fase; la que la `76.14` guardo, con esa hora delante, es la primera linea
de abajo. `DEUDA.jsonl` es de antes que el encargo y no la ha vuelto a escribir nadie. **La otra mitad de su sitio, la `ACTA 77`, es
de mi turno normal.**

    $ cat .v77aud/normal/r10.txt | sed -n '5p'
    2026-09-26 13:18:26 docs/loop/CREDITO_serial.jsonl
    $ bash .v78aud/r10.sh
    reloj del barrido de la 76: IDENTICO al pegado
    clase 78: IDENTICA a la pegada
    tablero --puedo: IDENTICO al pegado
    texto de d150: IDENTICO al pegado
    2026-09-26 12:37:57 docs/loop/DEUDA.jsonl
    2026-09-26 13:19:12 docs/loop/PROMPT_SIGUIENTE.md
    ahora: 2026-09-26 16:11:01

## 1. **LO QUE VI SIN BUSCARLO, Y LO DIGO ANTES DE MEDIR** (`d146`)

**La foto de `git status` que el entorno me pone delante trae los asuntos de los commits del extractor, y tres son cifras de su
vuelta**: `d19671a1` (*la fidelidad entera de las 20 de Marquet (110 pasos, 3 PUENTE corregidos en la bandeja antes del barrido,
cap_04 releido entero, R9 sin P nuevo; d150 preparada)*), `cc46a0da` (*el barrido de las 20 de Marquet (20 de 20, poblacion 479, 52
pares, recogido dentro del turno), 52 veredictos SANO listos, 1 arista por lectura y el orden con D.36 en cero; ninguna insertada*) y
`91bf4863` (*el cierre (censo 459, 1172, 1, 20, 0 al abrir y al cerrar; 3 PUENTE marcados y 0 que entraran; huellas de las 20; gate,
guiones, suite y cierre estricto en verde; R5 en cero; ninguna insertada)*). **Los lei antes de medir nada.** Es el mismo hueco de
`d146` que declararon las aperturas de la `65` a la `77`, y no lo arreglo yo (`D.45`).

**Y LO DEMAS DEL MISMO TIPO:** la cola de `docs/loop/loop.log`, que no se retira (el coste y la hora del turno del extractor); mi
`ACTA 76` entera y mi encargo; un `ls .v78ext`, que me enseno **los nombres** de su carpeta (entre ellos `fidelidad.tsv`,
`aristas_lectura.txt`, `orden.txt`, `grafo_zhuo_scott.txt` y un `vecinos_<id>.json` por ficha), **no su contenido**; la hora de las
fichas de la bandeja, que dice que dos cambiaron hoy; y **dos fichas llevan dentro, en su `resumen_teorico`, la *CORRECCION
DECLARADA DE LA VUELTA 78***, con el texto viejo dentro. **Esas correcciones las lei DESPUES de escribir y contar mi fidelidad paso a
paso**: para leer las lineas que cada ficha cita sin leer su prosa, `.v78aud/citas_ficha.py` imprime solo los `cap_NN` y los `LNN` que
el resumen nombra antes de la primera correccion, y cuantas correcciones trae; lo que dicen, en la seccion `3`, separado.

**LO QUE HAGO CON ELLO:** ninguna cifra de esta pagina sale de esos asuntos; todas salen de un instrumento corrido en esta fase, y
donde coinciden lo digo como coincidencia y no como fuente. **No he abierto nada de `.v78ext/` por dentro**, **ni
`bitacora/VEREDICTOS.jsonl` por dentro**: de ella solo cuento lineas. **Y ESTO SI PESA SOBRE MI LECTURA, Y LO DIGO:** el asunto de
`cc46a0da` me dijo *52 pares*, *52 veredictos SANO* y *1 arista por lectura* antes de barrer y de leer. Mis pares salen de mi barrido y
mis clases y aristas de las secciones `5` y `6` con su linea del libro, y son las que son; **pero no puedo probar que no me
empujaron**, y por eso lo escribo aqui. **Donde mi lectura puede no coincidir con lo que ese asunto dice es en el par de su arista
por lectura**, que el asunto no nombra: la mia lleva veredicto de la lectura `CONTINUA` (secciones `5` y `6`), y no la he movido por
eso.

## 2. **EL ALCANCE, Y EL CENSO QUE LO SOSTIENE**

Mi lista es la bandeja entera, leida del directorio, y su reparto por capitulo y por pasos lo da el instrumento de la `ACTA 76`
`76.11`, corrido hoy sin copiarlo:

    $ wc -l < .v78aud/las20.txt; ls cuarentena/marquet_turn_the_ship | grep "\.json$" | sed 's/\.json$//' | diff - .v78aud/las20.txt && echo "las20.txt es la bandeja de Marquet entera, fichero a fichero"
    20
    las20.txt es la bandeja de Marquet entera, fichero a fichero
    $ python .v77aud/normal/bandeja_marquet.py | diff - .v77aud/normal/bandeja_marquet.txt && echo "bandeja_marquet.py de hoy: IDENTICO a su salida de la ACTA 76 76.11"; tail -2 .v77aud/normal/bandeja_marquet.txt
    bandeja_marquet.py de hoy: IDENTICO a su salida de la ACTA 76 76.11
    fichas por capitulo: {'cap_01': 1, 'cap_02': 2, 'cap_03': 6, 'cap_04': 1, 'cap_06': 2, 'cap_07': 1, 'cap_08': 1, 'cap_09': 1, 'cap_10': 1, 'cap_11': 1, 'cap_12': 1, 'cap_13': 1, 'cap_14': 1} | suma: 20
    pasos por capitulo: {'cap_01': 6, 'cap_02': 10, 'cap_03': 53, 'cap_04': 5, 'cap_06': 8, 'cap_07': 3, 'cap_08': 5, 'cap_09': 2, 'cap_10': 3, 'cap_11': 3, 'cap_12': 8, 'cap_13': 2, 'cap_14': 2} | suma: 110

**El censo de hoy**, sin `git` (grafo, bitacora, pares mutuos; la bandeja de Marquet y sus insertados, la de Gerber y sus insertados,
y `procesos/`), la poblacion de la aduana y el `gate`:

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        459 dataset/nodos.jsonl
       1172 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1632 total
    $ for d in cuarentena/marquet_turn_the_ship cuarentena/_insertados/marquet_turn_the_ship cuarentena/gerber_emyth cuarentena/_insertados/gerber_emyth; do echo "$d $(find $d -maxdepth 1 -name '*.json' 2>/dev/null | wc -l)"; done; echo "procesos $(ls -A procesos/ | wc -l)"
    cuarentena/marquet_turn_the_ship 20
    cuarentena/_insertados/marquet_turn_the_ship 0
    cuarentena/gerber_emyth 0
    cuarentena/_insertados/gerber_emyth 22
    procesos 0
    $ python .v70aud/poblacion.py
    poblacion: 479 | por sede: {'grafo': 459, 'bandeja': 20} | suma: 479
    $ python forja.py gate | head -2
    GATE VERDE.
      nodos verificados: 459

**Lo que es mas nuevo que mi encargo** en las carpetas de dato, de codigo y de libro; la hora de la ultima ficha; y **las fichas de
Marquet contra mis huellas de la `76`**, tomadas antes de mi barrido de entonces:

    $ find cuarentena dataset bitacora censos config fuentes esquema src scripts tests forja.py -type f -newer docs/loop/PROMPT_SIGUIENTE.md | sed 's|/[^/]*\.json$|/*.json|' | sort | uniq -c
          2 cuarentena/marquet_turn_the_ship/*.json
    $ ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, substr($7,1,8), $9}'; ls -l --time-style=full-iso cuarentena/marquet_turn_the_ship/*.json | awk '{print $6, substr($7,1,8)}' | sort | sed -n '$p'
    2026-09-26 13:19:12 docs/loop/PROMPT_SIGUIENTE.md
    2026-09-26 13:40:35
    $ python .v78aud/huellas_contra_76.py
    fichas hoy: {'marquet_turn_the_ship': 20} | suma: 20
    contra mis huellas de la 76: {'gerber_emyth, NO ESTA': 22, 'marquet_turn_the_ship, CAMBIA': 2, 'marquet_turn_the_ship, igual': 18} | suma: 42
      CAMBIA: cuarentena/marquet_turn_the_ship/informar_cierre_jornada_conservar_propiedad_trabajo.json
      CAMBIA: cuarentena/marquet_turn_the_ship/seguir_frustrado_preguntar_implantacion_ideas.json

**LECTURA:**

1. `459`, `1172`, `1`, `20` en la bandeja de Marquet y `0` en sus insertados, y `22` insertados de Gerber con su bandeja vacia, son los
   de mi `ACTA 76` `76.1` al cerrar la `77`: **la vuelta no inserto nada ni movio nada de sede**, que es lo que el encargo pedia, y
   `procesos/` esta vacio. La poblacion del barrido sigue en `479`.
2. **Lo unico de dato mas nuevo que mi encargo son `2` fichas de Marquet, y son las `2` cuyas huellas cambiaron contra las mias de la
   `76`** (`informar_cierre_jornada_conservar_propiedad_trabajo` y `seguir_frustrado_preguntar_implantacion_ideas`); las otras `18`
   son byte a byte las de entonces. **Ningun fichero de `src/`, `scripts/`, `tests/`, `config/` ni del grafo es mas nuevo que mi encargo.**
   (Las `22` de Gerber salen `NO ESTA` porque viven en `_insertados` desde la `77`.)
3. **Lo que no puedo decir sin `git`**: si alguna linea de la bitacora o algun byte del grafo cambio sin cambiar la cuenta ni la
   fecha. Eso lo mido en mi turno normal, con el hash del reporte delante.

## 3. **LA FIDELIDAD DE LAS `20`, LEIDA ENTERA** (`D.30`, `D.58`, `8`)

Lei **enteros** los trece capitulos que las fichas citan (`cap_01`, `cap_02`, `cap_03`, `cap_04`, `cap_06` a `cap_14`), y cada paso
contra su linea, con los pasos delante por `pasos_ciego.py` (`.v78aud/pasos_20.txt`). Las citas que cada ficha nombra, sin su prosa:

    $ wc -l fuentes/marquet_turn_the_ship/cap_{01,02,03,04,06,07,08,09,10,11,12,13,14}.md | tail -1
      1433 total
    $ python .v78aud/citas_ficha.py
    acoger_inspectores_externos_fuente_aprendizaje          correcciones 0 | citas antes de la primera: cap_10 L45 L49
    aplicar_ejercicio_codigo_genetico_control               correcciones 1 | citas antes de la primera: cap_06
    asignar_responsable_unico_evolucion_planificada         correcciones 0 | citas antes de la primera: cap_06
    auditar_formacion_premios_ultima_fila                   correcciones 0 | citas antes de la primera: cap_03 L55 L57
    cambiar_forma_trabajar_conservar_plantilla              correcciones 2 | citas antes de la primera: cap_02 L25 L29
    ceder_control_reforzar_competencia_claridad             correcciones 0 | citas antes de la primera: cap_01
    contar_firmas_cadena_tramite_parado                     correcciones 0 | citas antes de la primera: cap_03
    declarar_intencion_reemplazar_peticion_permiso          correcciones 1 | citas antes de la primera: cap_07 L55 L73 L93
    eliminar_seguimiento_descendente_responsabilizar_dueno  correcciones 0 | citas antes de la primera: cap_09
    encargar_meta_especifica_dejar_libre_metodo             correcciones 1 | citas antes de la primera: cap_02 L49 L33
    identificar_temas_formacion_tarjetas_decision           correcciones 0 | citas antes de la primera: cap_12
    informar_cierre_jornada_conservar_propiedad_trabajo     correcciones 1 | citas antes de la primera: cap_04 cap_03
    inspeccionar_reparto_informacion_notas_jefe             correcciones 0 | citas antes de la primera: cap_03
    observar_reunion_rutinaria_senales_plantilla            correcciones 0 | citas antes de la primera: cap_03
    recorrer_organizacion_escuchar_plantilla                correcciones 0 | citas antes de la primera: cap_03
    reforzar_principios_guia_lenguaje_prueba_conocimiento   correcciones 0 | citas antes de la primera: cap_14 L89 L99 L91 L93 L95
    repetir_mensaje_invariable_diario_reunion_evento        correcciones 0 | citas antes de la primera: cap_13
    resistir_dar_solucion_clasificar_decision_urgencia      correcciones 0 | citas antes de la primera: cap_08 L107 L115 L121
    seguir_frustrado_preguntar_implantacion_ideas           correcciones 1 | citas antes de la primera: cap_03
    tomar_accion_deliberada_pausar_vocalizar_gesticular     correcciones 0 | citas antes de la primera: cap_11 L75 L95

Una fila por paso en `.v78aud/fidelidad.tsv`: `T` transcripcion, `P` puente (**la clausula reescrita cuenta como `P`**, `ACTA 62`
`62.5`), `D` mi duda, con su linea y **el tramo literal del libro**. El contador es copia de `.v76aud/contar_fidelidad.py` con las rutas
cambiadas, **una fila por capitulo** (`8.2`) y la suma de cada reparto (`R7`); cruza cada fila con los pasos de la ficha de la bandeja
de hoy, **y comprueba que el tramo que copio esta en la linea que cito**:

    $ python .v78aud/contar_fidelidad.py
    candidato                                                    ficha filas   T   P  DUDA  suma
    acoger_inspectores_externos_fuente_aprendizaje                   3     3   3   0     0     3
    aplicar_ejercicio_codigo_genetico_control                        6     6   6   0     0     6
    asignar_responsable_unico_evolucion_planificada                  2     2   2   0     0     2
    auditar_formacion_premios_ultima_fila                           11    11  10   0     1    11
    cambiar_forma_trabajar_conservar_plantilla                       5     5   5   0     0     5
    ceder_control_reforzar_competencia_claridad                      6     6   6   0     0     6
    contar_firmas_cadena_tramite_parado                             10    10  10   0     0    10
    declarar_intencion_reemplazar_peticion_permiso                   3     3   3   0     0     3
    eliminar_seguimiento_descendente_responsabilizar_dueno           2     2   2   0     0     2
    encargar_meta_especifica_dejar_libre_metodo                      5     5   5   0     0     5
    identificar_temas_formacion_tarjetas_decision                    8     8   8   0     0     8
    informar_cierre_jornada_conservar_propiedad_trabajo              5     5   5   0     0     5
    inspeccionar_reparto_informacion_notas_jefe                      8     8   8   0     0     8
    observar_reunion_rutinaria_senales_plantilla                     9     9   9   0     0     9
    recorrer_organizacion_escuchar_plantilla                         7     7   7   0     0     7
    reforzar_principios_guia_lenguaje_prueba_conocimiento            2     2   2   0     0     2
    repetir_mensaje_invariable_diario_reunion_evento                 2     2   2   0     0     2
    resistir_dar_solucion_clasificar_decision_urgencia               5     5   5   0     0     5
    seguir_frustrado_preguntar_implantacion_ideas                    8     8   7   0     1     8
    tomar_accion_deliberada_pausar_vocalizar_gesticular              3     3   3   0     0     3
    cap_10: candidatos 1 | pasos en ficha 3 | filas 3 | T 3 | P 0 | DUDA 0 | suma: 3 | PUENTE 0 de 3 = 0.00 por ciento | si las DUDA cayesen: 0 de 3 = 0.00 por ciento
    cap_06: candidatos 2 | pasos en ficha 8 | filas 8 | T 8 | P 0 | DUDA 0 | suma: 8 | PUENTE 0 de 8 = 0.00 por ciento | si las DUDA cayesen: 0 de 8 = 0.00 por ciento
    cap_03: candidatos 6 | pasos en ficha 53 | filas 53 | T 51 | P 0 | DUDA 2 | suma: 53 | PUENTE 0 de 53 = 0.00 por ciento | si las DUDA cayesen: 2 de 53 = 3.77 por ciento
    cap_02: candidatos 2 | pasos en ficha 10 | filas 10 | T 10 | P 0 | DUDA 0 | suma: 10 | PUENTE 0 de 10 = 0.00 por ciento | si las DUDA cayesen: 0 de 10 = 0.00 por ciento
    cap_01: candidatos 1 | pasos en ficha 6 | filas 6 | T 6 | P 0 | DUDA 0 | suma: 6 | PUENTE 0 de 6 = 0.00 por ciento | si las DUDA cayesen: 0 de 6 = 0.00 por ciento
    cap_07: candidatos 1 | pasos en ficha 3 | filas 3 | T 3 | P 0 | DUDA 0 | suma: 3 | PUENTE 0 de 3 = 0.00 por ciento | si las DUDA cayesen: 0 de 3 = 0.00 por ciento
    cap_09: candidatos 1 | pasos en ficha 2 | filas 2 | T 2 | P 0 | DUDA 0 | suma: 2 | PUENTE 0 de 2 = 0.00 por ciento | si las DUDA cayesen: 0 de 2 = 0.00 por ciento
    cap_12: candidatos 1 | pasos en ficha 8 | filas 8 | T 8 | P 0 | DUDA 0 | suma: 8 | PUENTE 0 de 8 = 0.00 por ciento | si las DUDA cayesen: 0 de 8 = 0.00 por ciento
    cap_04: candidatos 1 | pasos en ficha 5 | filas 5 | T 5 | P 0 | DUDA 0 | suma: 5 | PUENTE 0 de 5 = 0.00 por ciento | si las DUDA cayesen: 0 de 5 = 0.00 por ciento
    cap_14: candidatos 1 | pasos en ficha 2 | filas 2 | T 2 | P 0 | DUDA 0 | suma: 2 | PUENTE 0 de 2 = 0.00 por ciento | si las DUDA cayesen: 0 de 2 = 0.00 por ciento
    cap_13: candidatos 1 | pasos en ficha 2 | filas 2 | T 2 | P 0 | DUDA 0 | suma: 2 | PUENTE 0 de 2 = 0.00 por ciento | si las DUDA cayesen: 0 de 2 = 0.00 por ciento
    cap_08: candidatos 1 | pasos en ficha 5 | filas 5 | T 5 | P 0 | DUDA 0 | suma: 5 | PUENTE 0 de 5 = 0.00 por ciento | si las DUDA cayesen: 0 de 5 = 0.00 por ciento
    cap_11: candidatos 1 | pasos en ficha 3 | filas 3 | T 3 | P 0 | DUDA 0 | suma: 3 | PUENTE 0 de 3 = 0.00 por ciento | si las DUDA cayesen: 0 de 3 = 0.00 por ciento
    los trece: candidatos 20 | pasos en ficha 110 | filas 110 | T 108 | P 0 | DUDA 2 | suma: 110
    citas: filas 110 | el tramo esta en su linea: 110 | no esta: 0 | suma: 110

**LECTURA: Marquet es un libro de relato**, y las fichas convierten en mandato lo que el autor cuenta que hizo o vio: *Mira si...*,
*Pregunta...*, *Quedate con...*, cada una con el contenido de su linea. **Esa figura es `T`** (el aviso o el relato vuelto mandato con
el contenido del libro, la que la `ACTA 70` `70.4` adjudico `T`), y solo es `P` cuando el mandato **anade** lo que la linea no da. Los
tramos donde el libro ya habla en mandato o en lista (`cap_06` L101 a L111, `cap_07` L75 a L93, `cap_08` L107 y L117 a L121, `cap_12`
L125 a L139, `cap_13` L119 y `cap_14` L89 y L99) **los transcriben casi frase a frase**, con la cita inglesa en el propio paso. **No encuentro ningun PUENTE en
el texto de hoy de las fichas.** Las figuras que mire y dejo en `T`, para que se juzguen:

- `informar_cierre_jornada_conservar_propiedad_trabajo` paso `1`: *no le preguntes que mas necesita de ti* es el contraejemplo de L31
  (*asked the XO if he had anything more for him that day*), el mismo capitulo; y paso `5`, *Cierra el reporte dejando la propiedad de
  la tarea donde corresponde*, que es la conclusion de L35 y no una frase mas del guion.
- `cambiar_forma_trabajar_conservar_plantilla` paso `1`, *Cuenta el plazo que tienes antes de decidir nada sobre la gente*: el
  argumento de L25 es el plazo contra el tiempo de encontrar sustitutos.
- `contar_firmas_cadena_tramite_parado` paso `5`: traduce *department chief* y *department head* los dos por *jefe de departamento*;
  la cadena es la de L39 puesto por puesto, y la cuenta de siete tambien.
- `auditar_formacion_premios_ultima_fila`: reordena la escena (L55 da los premios antes de que el autor se vaya a la periferia en L57);
  el orden no es fidelidad de paso.

**MIS DOS DUDAS, las dos de `cap_03` y las dos la misma figura, y me inclino a `T`:** `auditar_formacion_premios_ultima_fila` paso `6`
(*Escucha la respuesta entera, tambien su segunda mitad*) y `seguir_frustrado_preguntar_implantacion_ideas` paso `3` (*escuchale hasta
el final*): el libro registra la respuesta entera y escucha, pero **no manda** oirla entera. **Si cayesen las dos, `cap_03` queda en
`2` de `53`, el `3,77` por ciento**, por debajo del `10`.

**`PASOS INVENTADOS` por mi instrumento, sobre el texto de hoy: `0` en los trece capitulos.** Es preparacion y no entrada.

**`d150`, CON SU TEXTO DELANTE** (mi encargo, TAREA `2` punto `5`): la fila de `cap_03`, contada entera paso a paso, es la de mi
instrumento de arriba, y la vuelvo a pegar sola:

    $ grep '"id": "d150"' docs/loop/DEUDA.jsonl | grep -o '"que": "[^"]*"'
    "que": "La TAREA 2 y la TAREA 3 del reporte de la vuelta 1 del frente marquet siguen sin escribirse desde los papeles de .vm01/, que estan intactos con 47 ficheros, y la fila de cap_03 sigue publicada en 0,00 donde la ACTA M2 la recontro."
    $ python .v78aud/contar_fidelidad.py | grep "^cap_03:"
    cap_03: candidatos 6 | pasos en ficha 53 | filas 53 | T 51 | P 0 | DUDA 2 | suma: 53 | PUENTE 0 de 53 = 0.00 por ciento | si las DUDA cayesen: 2 de 53 = 3.77 por ciento

**Y LO QUE LEI DESPUES, EN LAS FICHAS:** seis de las `20` traen en su `resumen_teorico` alguna *CORRECCION DECLARADA*; **cuatro son
del frente de Marquet** (vueltas `1`, `3` y `4` del frente y la `27` de la serial, con su texto viejo dentro), y **dos son de la vuelta `78`**, las de las
dos fichas cuyas huellas cambiaron (seccion `2`). Leido de su propia prosa (`.v78aud/correcciones.py`, salida en
`.v78aud/correcciones.txt`):

    $ grep -c "CORRECCION DECLARADA DE LA VUELTA 78" .v78aud/correcciones.txt; grep -o "decia: [^.]*\." .v78aud/correcciones.txt
    2
    decia: Reporta primero el estado de un trabajo en curso con signo positivo, nombrando el propio trabajo.
    decia: Si algo quedo sin hacer, dilo sin disculpa vacia y da el plan de cuando se hara.
    decia: Nombrale lo que viste, sin pregunta y sin acusacion.

**Leo sus textos viejos y los clasifico yo:**

- `informar_cierre_jornada_conservar_propiedad_trabajo` paso `2`, *con signo positivo*: **`P`**. L35 da el ejemplo *coming along fine*
  y no pide que el estado que se reporta sea bueno. Paso `4`, *sin disculpa vacia*: **`P`**. Ninguna linea de `cap_04` habla de
  disculpas.
- `seguir_frustrado_preguntar_implantacion_ideas` paso `2`, *sin pregunta y sin acusacion*: **`P`**. L25 da solo la frase.

**LECTURA:** sobre el texto viejo, **mi lectura da `P` a las tres lineas *decia* del bloque de arriba**: dos de la ficha de `cap_04`, cuyos
`5` pasos cuenta mi instrumento, y una de `cap_03`, de `53`. **`cap_04`
pasa del `10`, y por eso se relee entero antes de seguir** (`D.58`); **coincide con el *cap_04 releido entero* y los *3 PUENTE* del
asunto de `d19671a1`**, y lo digo como coincidencia. **Los tres pasos corregidos los lei yo `T` en su texto de hoy**: las correcciones
se sostienen. **Lo que no puedo decir** es si mi lectura ciega habria cazado esos puentes, porque cuando lei ya no estaban. **Y ME
DEJA UNA PREGUNTA QUE LLEVO AL TURNO NORMAL:** su vara retira *sin pregunta y sin acusacion*, una clausula de modo que la linea no da;
**mis dos dudas son la misma figura en positivo** (*entera, tambien su segunda mitad*; *hasta el final*). Si por su vara son `P`,
`cap_03` queda en `2` de `53` y se corrigen en la bandeja antes de entrar.

## 4. **MI BARRIDO DE LAS `20`, SOBRE GRAFO MAS BANDEJAS** (`D.38.4`, `D.38.5`)

Copia de `.v76aud/barrido_uno.py` (la ficha normalizada como la aduana, contra `dataset/nodos.jsonl` mas
`aduana.poblacion_de_bandejas`, con `buscar_vecinos` de `src/aduana.py`) y de `.v76aud/barrer.sh` con la lista cambiada a
`.v78aud/las20.txt`, **cinco a la vez, recogido entero dentro de este turno**, lanzado **despues** de que las fichas cambiasen por
ultima vez (seccion `2`: la ultima es de las `13:40:35`). Antes de lanzarlo guarde la huella de cada ficha de la bandeja y del grafo,
y al recogerlo las comprobe:

    $ head -1 .v78aud/barrido.log; tail -1 .v78aud/barrido.log; grep -c "rc=0" .v78aud/barrido.log; grep -c "rc=" .v78aud/barrido.log
    INICIO 2026-09-26 15:05:11
    TODOS TERMINADOS 2026-09-26 16:05:25
    20
    20
    $ wc -l < .v78aud/huellas_al_barrer.txt; sha1sum -c --quiet .v78aud/huellas_al_barrer.txt && echo "las 20 fichas de la bandeja y el grafo: mismas huellas que al barrer"
    21
    las 20 fichas de la bandeja y el grafo: mismas huellas que al barrer

**Poblacion y vecinos por candidato, cada fila de vecino con su senial, y los pares sin orden:**

    $ python .v78aud/vecinos_tabla.py | tee .v78aud/vecinos_tabla.txt
    (1) candidato | poblacion | vecinos | en grafo | en bandeja
        acoger_inspectores_externos_fuente_aprendizaje           479   6   0   6
        aplicar_ejercicio_codigo_genetico_control                479   1   0   1
        asignar_responsable_unico_evolucion_planificada          479   0   0   0
        auditar_formacion_premios_ultima_fila                    479   2   0   2
        cambiar_forma_trabajar_conservar_plantilla               479   2   1   1
        ceder_control_reforzar_competencia_claridad              479   1   0   1
        contar_firmas_cadena_tramite_parado                      479   2   0   2
        declarar_intencion_reemplazar_peticion_permiso           479   4   0   4
        eliminar_seguimiento_descendente_responsabilizar_dueno   479   0   0   0
        encargar_meta_especifica_dejar_libre_metodo              479   3   0   3
        identificar_temas_formacion_tarjetas_decision            479   0   0   0
        informar_cierre_jornada_conservar_propiedad_trabajo      479   6   5   1
        inspeccionar_reparto_informacion_notas_jefe              479   2   0   2
        observar_reunion_rutinaria_senales_plantilla             479   3   0   3
        recorrer_organizacion_escuchar_plantilla                 479   3   0   3
        reforzar_principios_guia_lenguaje_prueba_conocimiento    479   3   0   3
        repetir_mensaje_invariable_diario_reunion_evento         479   0   0   0
        resistir_dar_solucion_clasificar_decision_urgencia       479   5   0   5
        seguir_frustrado_preguntar_implantacion_ideas            479   6   4   2
        tomar_accion_deliberada_pausar_vocalizar_gesticular      479   3   0   3
    sin fichero de vecinos: 0 []
    (2) vecino levantado | senial | texto familia paso
        acoger_inspectores_externos_fuente_aprendizaje         > tomar_accion_deliberada_pausar_vocalizar_gesticular    bandeja similitud_texto  0.457 0.000 0.399
        acoger_inspectores_externos_fuente_aprendizaje         > resistir_dar_solucion_clasificar_decision_urgencia     bandeja similitud_texto  0.412 0.000 0.410
        acoger_inspectores_externos_fuente_aprendizaje         > declarar_intencion_reemplazar_peticion_permiso         bandeja similitud_texto  0.406 0.000 0.393
        acoger_inspectores_externos_fuente_aprendizaje         > reforzar_principios_guia_lenguaje_prueba_conocimiento  bandeja similitud_texto  0.397 0.000 0.376
        acoger_inspectores_externos_fuente_aprendizaje         > seguir_frustrado_preguntar_implantacion_ideas          bandeja similitud_texto  0.356 0.000 0.294
        acoger_inspectores_externos_fuente_aprendizaje         > recorrer_organizacion_escuchar_plantilla               bandeja similitud_texto  0.353 0.000 0.327
        aplicar_ejercicio_codigo_genetico_control              > resistir_dar_solucion_clasificar_decision_urgencia     bandeja similitud_texto  0.366 0.000 0.432
        auditar_formacion_premios_ultima_fila                  > observar_reunion_rutinaria_senales_plantilla           bandeja similitud_texto  0.370 0.000 0.489
        auditar_formacion_premios_ultima_fila                  > recorrer_organizacion_escuchar_plantilla               bandeja similitud_texto  0.353 0.000 0.462
        cambiar_forma_trabajar_conservar_plantilla             > escuchar_entender_critica_dominar_defensa              grafo   paso_contra_nodo 0.201 0.000 0.612
        cambiar_forma_trabajar_conservar_plantilla             > encargar_meta_especifica_dejar_libre_metodo            bandeja similitud_texto  0.441 0.000 0.455
        ceder_control_reforzar_competencia_claridad            > encargar_meta_especifica_dejar_libre_metodo            bandeja similitud_texto  0.372 0.000 0.486
        contar_firmas_cadena_tramite_parado                    > seguir_frustrado_preguntar_implantacion_ideas          bandeja similitud_texto  0.354 0.000 0.463
        contar_firmas_cadena_tramite_parado                    > inspeccionar_reparto_informacion_notas_jefe            bandeja similitud_texto  0.360 0.000 0.405
        declarar_intencion_reemplazar_peticion_permiso         > resistir_dar_solucion_clasificar_decision_urgencia     bandeja similitud_texto  0.422 0.000 0.439
        declarar_intencion_reemplazar_peticion_permiso         > acoger_inspectores_externos_fuente_aprendizaje         bandeja similitud_texto  0.404 0.000 0.350
        declarar_intencion_reemplazar_peticion_permiso         > informar_cierre_jornada_conservar_propiedad_trabajo    bandeja similitud_texto  0.352 0.000 0.391
        declarar_intencion_reemplazar_peticion_permiso         > reforzar_principios_guia_lenguaje_prueba_conocimiento  bandeja similitud_texto  0.355 0.000 0.353
        encargar_meta_especifica_dejar_libre_metodo            > ceder_control_reforzar_competencia_claridad            bandeja similitud_texto  0.381 0.000 0.473
        encargar_meta_especifica_dejar_libre_metodo            > cambiar_forma_trabajar_conservar_plantilla             bandeja similitud_texto  0.436 0.000 0.459
        encargar_meta_especifica_dejar_libre_metodo            > recorrer_organizacion_escuchar_plantilla               bandeja similitud_texto  0.412 0.000 0.416
        informar_cierre_jornada_conservar_propiedad_trabajo    > seguir_frustrado_preguntar_implantacion_ideas          bandeja similitud_texto  0.412 0.000 0.391
        informar_cierre_jornada_conservar_propiedad_trabajo    > operar_modelo_gente_destreza_minima                    grafo   similitud_texto  0.364 0.000 0.399
        informar_cierre_jornada_conservar_propiedad_trabajo    > cuantificar_impacto_innovacion_6_pasos                 grafo   similitud_texto  0.392 0.000 0.294
        informar_cierre_jornada_conservar_propiedad_trabajo    > dictar_ritmo_crecimiento_preguntas_escritas            grafo   similitud_texto  0.361 0.000 0.390
        informar_cierre_jornada_conservar_propiedad_trabajo    > interrogar_negocio_cinco_preguntas                     grafo   similitud_texto  0.360 0.000 0.390
        informar_cierre_jornada_conservar_propiedad_trabajo    > usar_banco_nueve_preguntas_entrevista                  grafo   similitud_texto  0.351 0.000 0.329
        inspeccionar_reparto_informacion_notas_jefe            > observar_reunion_rutinaria_senales_plantilla           bandeja similitud_texto  0.358 0.000 0.452
        inspeccionar_reparto_informacion_notas_jefe            > contar_firmas_cadena_tramite_parado                    bandeja similitud_texto  0.379 0.000 0.428
        observar_reunion_rutinaria_senales_plantilla           > auditar_formacion_premios_ultima_fila                  bandeja similitud_texto  0.361 0.000 0.463
        observar_reunion_rutinaria_senales_plantilla           > recorrer_organizacion_escuchar_plantilla               bandeja similitud_texto  0.414 0.125 0.435
        observar_reunion_rutinaria_senales_plantilla           > inspeccionar_reparto_informacion_notas_jefe            bandeja similitud_texto  0.367 0.000 0.406
        recorrer_organizacion_escuchar_plantilla               > observar_reunion_rutinaria_senales_plantilla           bandeja similitud_texto  0.420 0.125 0.437
        recorrer_organizacion_escuchar_plantilla               > encargar_meta_especifica_dejar_libre_metodo            bandeja similitud_texto  0.401 0.000 0.426
        recorrer_organizacion_escuchar_plantilla               > inspeccionar_reparto_informacion_notas_jefe            bandeja similitud_texto  0.352 0.000 0.383
        reforzar_principios_guia_lenguaje_prueba_conocimiento  > acoger_inspectores_externos_fuente_aprendizaje         bandeja similitud_texto  0.401 0.000 0.372
        reforzar_principios_guia_lenguaje_prueba_conocimiento  > tomar_accion_deliberada_pausar_vocalizar_gesticular    bandeja similitud_texto  0.358 0.000 0.326
        reforzar_principios_guia_lenguaje_prueba_conocimiento  > resistir_dar_solucion_clasificar_decision_urgencia     bandeja similitud_texto  0.355 0.000 0.329
        resistir_dar_solucion_clasificar_decision_urgencia     > aplicar_ejercicio_codigo_genetico_control              bandeja similitud_texto  0.356 0.000 0.452
        resistir_dar_solucion_clasificar_decision_urgencia     > declarar_intencion_reemplazar_peticion_permiso         bandeja similitud_texto  0.411 0.000 0.434
        resistir_dar_solucion_clasificar_decision_urgencia     > acoger_inspectores_externos_fuente_aprendizaje         bandeja similitud_texto  0.428 0.000 0.402
        resistir_dar_solucion_clasificar_decision_urgencia     > tomar_accion_deliberada_pausar_vocalizar_gesticular    bandeja similitud_texto  0.402 0.000 0.382
        resistir_dar_solucion_clasificar_decision_urgencia     > reforzar_principios_guia_lenguaje_prueba_conocimiento  bandeja similitud_texto  0.369 0.000 0.346
        seguir_frustrado_preguntar_implantacion_ideas          > interrogar_negocio_cinco_preguntas                     grafo   similitud_texto  0.363 0.000 0.477
        seguir_frustrado_preguntar_implantacion_ideas          > contar_firmas_cadena_tramite_parado                    bandeja similitud_texto  0.375 0.000 0.441
        seguir_frustrado_preguntar_implantacion_ideas          > dictar_ritmo_crecimiento_preguntas_escritas            grafo   similitud_texto  0.389 0.000 0.436
        seguir_frustrado_preguntar_implantacion_ideas          > informar_cierre_jornada_conservar_propiedad_trabajo    bandeja similitud_texto  0.411 0.000 0.399
        seguir_frustrado_preguntar_implantacion_ideas          > pedir_critica_anonima_curso_entrenamiento_dictado      grafo   similitud_texto  0.357 0.000 0.405
        seguir_frustrado_preguntar_implantacion_ideas          > cambiar_saludo_cliente_dos_ramas                       grafo   similitud_texto  0.366 0.000 0.355
        tomar_accion_deliberada_pausar_vocalizar_gesticular    > acoger_inspectores_externos_fuente_aprendizaje         bandeja similitud_texto  0.464 0.000 0.391
        tomar_accion_deliberada_pausar_vocalizar_gesticular    > resistir_dar_solucion_clasificar_decision_urgencia     bandeja similitud_texto  0.411 0.000 0.372
        tomar_accion_deliberada_pausar_vocalizar_gesticular    > reforzar_principios_guia_lenguaje_prueba_conocimiento  bandeja similitud_texto  0.366 0.000 0.349
    filas de vecino: 52
    (3) pares sin orden | levantado desde
        acoger_inspectores_externos_fuente_aprendizaje         ~ tomar_accion_deliberada_pausar_vocalizar_gesticular    tanda-tanda los dos
        acoger_inspectores_externos_fuente_aprendizaje         ~ resistir_dar_solucion_clasificar_decision_urgencia     tanda-tanda los dos
        acoger_inspectores_externos_fuente_aprendizaje         ~ declarar_intencion_reemplazar_peticion_permiso         tanda-tanda los dos
        acoger_inspectores_externos_fuente_aprendizaje         ~ reforzar_principios_guia_lenguaje_prueba_conocimiento  tanda-tanda los dos
        acoger_inspectores_externos_fuente_aprendizaje         ~ seguir_frustrado_preguntar_implantacion_ideas          tanda-tanda solo acoger_inspectores_externos_fuente_aprendizaje
        acoger_inspectores_externos_fuente_aprendizaje         ~ recorrer_organizacion_escuchar_plantilla               tanda-tanda solo acoger_inspectores_externos_fuente_aprendizaje
        aplicar_ejercicio_codigo_genetico_control              ~ resistir_dar_solucion_clasificar_decision_urgencia     tanda-tanda los dos
        auditar_formacion_premios_ultima_fila                  ~ observar_reunion_rutinaria_senales_plantilla           tanda-tanda los dos
        auditar_formacion_premios_ultima_fila                  ~ recorrer_organizacion_escuchar_plantilla               tanda-tanda solo auditar_formacion_premios_ultima_fila
        cambiar_forma_trabajar_conservar_plantilla             ~ escuchar_entender_critica_dominar_defensa              con fuera   solo cambiar_forma_trabajar_conservar_plantilla
        cambiar_forma_trabajar_conservar_plantilla             ~ encargar_meta_especifica_dejar_libre_metodo            tanda-tanda los dos
        ceder_control_reforzar_competencia_claridad            ~ encargar_meta_especifica_dejar_libre_metodo            tanda-tanda los dos
        contar_firmas_cadena_tramite_parado                    ~ seguir_frustrado_preguntar_implantacion_ideas          tanda-tanda los dos
        contar_firmas_cadena_tramite_parado                    ~ inspeccionar_reparto_informacion_notas_jefe            tanda-tanda los dos
        declarar_intencion_reemplazar_peticion_permiso         ~ resistir_dar_solucion_clasificar_decision_urgencia     tanda-tanda los dos
        declarar_intencion_reemplazar_peticion_permiso         ~ informar_cierre_jornada_conservar_propiedad_trabajo    tanda-tanda solo declarar_intencion_reemplazar_peticion_permiso
        declarar_intencion_reemplazar_peticion_permiso         ~ reforzar_principios_guia_lenguaje_prueba_conocimiento  tanda-tanda solo declarar_intencion_reemplazar_peticion_permiso
        encargar_meta_especifica_dejar_libre_metodo            ~ recorrer_organizacion_escuchar_plantilla               tanda-tanda los dos
        informar_cierre_jornada_conservar_propiedad_trabajo    ~ seguir_frustrado_preguntar_implantacion_ideas          tanda-tanda los dos
        informar_cierre_jornada_conservar_propiedad_trabajo    ~ operar_modelo_gente_destreza_minima                    con fuera   solo informar_cierre_jornada_conservar_propiedad_trabajo
        cuantificar_impacto_innovacion_6_pasos                 ~ informar_cierre_jornada_conservar_propiedad_trabajo    con fuera   solo informar_cierre_jornada_conservar_propiedad_trabajo
        dictar_ritmo_crecimiento_preguntas_escritas            ~ informar_cierre_jornada_conservar_propiedad_trabajo    con fuera   solo informar_cierre_jornada_conservar_propiedad_trabajo
        informar_cierre_jornada_conservar_propiedad_trabajo    ~ interrogar_negocio_cinco_preguntas                     con fuera   solo informar_cierre_jornada_conservar_propiedad_trabajo
        informar_cierre_jornada_conservar_propiedad_trabajo    ~ usar_banco_nueve_preguntas_entrevista                  con fuera   solo informar_cierre_jornada_conservar_propiedad_trabajo
        inspeccionar_reparto_informacion_notas_jefe            ~ observar_reunion_rutinaria_senales_plantilla           tanda-tanda los dos
        observar_reunion_rutinaria_senales_plantilla           ~ recorrer_organizacion_escuchar_plantilla               tanda-tanda los dos
        inspeccionar_reparto_informacion_notas_jefe            ~ recorrer_organizacion_escuchar_plantilla               tanda-tanda solo recorrer_organizacion_escuchar_plantilla
        reforzar_principios_guia_lenguaje_prueba_conocimiento  ~ tomar_accion_deliberada_pausar_vocalizar_gesticular    tanda-tanda los dos
        reforzar_principios_guia_lenguaje_prueba_conocimiento  ~ resistir_dar_solucion_clasificar_decision_urgencia     tanda-tanda los dos
        resistir_dar_solucion_clasificar_decision_urgencia     ~ tomar_accion_deliberada_pausar_vocalizar_gesticular    tanda-tanda los dos
        interrogar_negocio_cinco_preguntas                     ~ seguir_frustrado_preguntar_implantacion_ideas          con fuera   solo seguir_frustrado_preguntar_implantacion_ideas
        dictar_ritmo_crecimiento_preguntas_escritas            ~ seguir_frustrado_preguntar_implantacion_ideas          con fuera   solo seguir_frustrado_preguntar_implantacion_ideas
        pedir_critica_anonima_curso_entrenamiento_dictado      ~ seguir_frustrado_preguntar_implantacion_ideas          con fuera   solo seguir_frustrado_preguntar_implantacion_ideas
        cambiar_saludo_cliente_dos_ramas                       ~ seguir_frustrado_preguntar_implantacion_ideas          con fuera   solo seguir_frustrado_preguntar_implantacion_ideas
    pares sin orden: 34 | {'tanda-tanda': 24, 'con fuera': 10} | suma: 34

**Y las cifras que la lectura de abajo cita, contadas sobre los mismos ficheros y no a ojo** (`D.38.3`):

    $ python .v78aud/cifras_barrido.py
    filas por senial: {'similitud_texto': 51, 'paso_contra_nodo': 1} | suma: 52
    nodos de fuera: 8 | por libro: {'scott_radical_candor': 1, 'gerber_emyth': 5, 'grove_high_output': 2} | suma: 8
    fichas que no levantan a nadie: 4 ['asignar_responsable_unico_evolucion_planificada', 'eliminar_seguimiento_descendente_responsabilizar_dueno', 'identificar_temas_formacion_tarjetas_decision', 'repetir_mensaje_invariable_diario_reunion_evento']
    fichas a las que no levanta nadie: 4 ['asignar_responsable_unico_evolucion_planificada', 'eliminar_seguimiento_descendente_responsabilizar_dueno', 'identificar_temas_formacion_tarjetas_decision', 'repetir_mensaje_invariable_diario_reunion_evento']
    similitud_texto en las filas que levanta solo esa senial: filas 51 | menor 0.351 | mayor 0.464

**LECTURA:**

1. **Las `20` dan `52` filas de vecino en `34` pares sin orden**, `24` entre dos de la tanda y `10` con uno de fuera, todos del
   grafo. **Coincide con los *52 pares* del asunto de `cc46a0da`**, que ahi llama *pares* a mis filas dirigidas, como en la `73` y la
   `76`; y lo digo como coincidencia.
2. **Todo menos una fila lo levanta `similitud_texto`, casi siempre entre fichas del mismo libro, entre `0,351` y `0,464`**: las fichas de Marquet
   comparten la forma (*El texto lo dice asi*, la cita inglesa en el paso) mas que el procedimiento. La unica fila de otra senial es
   `cambiar_forma_trabajar_conservar_plantilla` contra `escuchar_entender_critica_dominar_defensa` de Scott, por `paso_contra_nodo`.
3. **Cuatro fichas no levantan a nadie, y son las mismas cuatro a las que no levanta nadie**: `asignar_responsable_unico_evolucion_planificada`,
   `eliminar_seguimiento_descendente_responsabilizar_dueno`, `identificar_temas_formacion_tarjetas_decision` y
   `repetir_mensaje_invariable_diario_reunion_evento`.
4. **Los de fuera son `8` nodos del grafo**: de Gerber, `operar_modelo_gente_destreza_minima`, `cuantificar_impacto_innovacion_6_pasos`,
   `dictar_ritmo_crecimiento_preguntas_escritas`, `interrogar_negocio_cinco_preguntas` y `cambiar_saludo_cliente_dos_ramas`; de Grove,
   `usar_banco_nueve_preguntas_entrevista` y `pedir_critica_anonima_curso_entrenamiento_dictado`; de Scott,
   `escuchar_entender_critica_dominar_defensa`. **De Zhuo, ninguno.** Los levantan `cambiar_forma_trabajar_conservar_plantilla`,
   `informar_cierre_jornada_conservar_propiedad_trabajo` o `seguir_frustrado_preguntar_implantacion_ideas`, siempre desde un solo lado.
5. **El par de mi `CONTINUA` de la seccion `5` NO lo levanta el barrido en ningun sentido**
   (`observar_reunion_rutinaria_senales_plantilla` con `seguir_frustrado_preguntar_implantacion_ideas`): es arista por lectura
   (seccion `6`).
6. **`D.36`, lo que un solo lado levanta dentro de la tanda**: va a la seccion `7`, y no obliga.

**EL RELOJ, medido y no techo:** de punta a punta en el log de arriba, con fichas de estos segundos (la menor y la mayor):

    $ grep "rc=" .v78aud/barrido.log | sed 's/.*segundos=//' | sort -n | sed -n '1p;$p'
    483
    1144

## 5. **MI LECTURA CIEGA DE LOS PARES** (`1.2`, `6.1`, y solo la vara `6.1`)

**Leidos con los pasos de los dos delante**, todos con `pasos_ciego.py` (`R6`): `.v78aud/pasos_20.txt` para las `20` y
`.v78aud/pasos_fuera.txt` para los ocho de fuera. **Una fila por par** en `.v78aud/mis_clases.tsv`, con su razon. **De donde sale cada
fila:** los pares posibles dentro de un mismo capitulo los escribi **antes de recoger ninguna ficha del barrido**, en
`.v78aud/clases_intra.txt`, **salvo uno que me faltaba** (`recorrer` con `seguir`, que el barrido no levanta) y que anadi al recogerlo,
con su nota dentro del fichero; **por eso la hora de ese fichero es de despues**, y lo que queda de la hora de antes es la de
`.v78aud/aristas_lectura.tsv`, que escribi despues de las clases de dentro y antes de que cerrara la primera ficha. **Esa secuencia
no la prueba ningun instrumento: la declaro.** Los de entre capitulos y los de fuera, al recogerlo, en `.v78aud/clases_fuera.txt`:

    $ ls -l --time-style=full-iso .v78aud/aristas_lectura.tsv .v78aud/clases_intra.txt .v78aud/clases_fuera.txt | awk '{print $6, substr($7,1,8), $9}'; ls -l --time-style=full-iso .v78aud/vecinos_*.json | awk '{print substr($7,1,8)}' | sort | head -3
    2026-09-26 15:13:15 .v78aud/aristas_lectura.tsv
    2026-09-26 16:06:31 .v78aud/clases_fuera.txt
    2026-09-26 16:06:45 .v78aud/clases_intra.txt
    15:13:23
    15:15:42
    15:22:50

`armar_clases.py` los junta, y el cruce comprueba que cada par del barrido tiene su fila y cada fila su par:

    $ python .v78aud/armar_clases.py
    pares del barrido: 34 | filas escritas: 34 | sin clase: 0 []
    de donde sale cada fila: {'fuera': 26, 'intra': 8} | suma: 34
    filas de clases_intra.txt: 17 | por el barrido: {'no levantada': 9, 'levantada': 8} | suma: 17
    $ python .v78aud/cruce_clases.py
    pares del barrido: 34 | filas de clase: 34
    pares sin fila: []
    filas sin par: []
    clases: {'SANO': 34} | suma: 34
    con DUDA escrita: 3

**LECTURA: LOS `34` PARES QUE EL BARRIDO LEVANTA SON `SANO`, LOS `34`.** Ninguno es `REPITE`: en todos hay procedimiento fuera del
solape en los dos lados, y en casi todos no hay solape de procedimiento sino de forma (seccion `4`, punto `2`). **Ninguno es
`CONTINUA`**: ningun hijo arranca del producto del otro. **Coincide con los *52 veredictos SANO* del asunto de `cc46a0da`** en la clase
de todas las filas del barrido, y lo digo como coincidencia.

**MI UNICO `CONTINUA` ES DE UN PAR QUE EL BARRIDO NO LEVANTA**, y por eso no es linea de veredicto sino arista por lectura con su
veredicto de la lectura (`D.53`; asi entro `fingir` a `recorrer` en la `77`, `ACTA 76` `76.3`):
`observar_reunion_rutinaria_senales_plantilla` **madre de** `seguir_frustrado_preguntar_implantacion_ideas`. Los pasos de los dos:

    $ python .v67aud/normal/pasos_ciego.py observar_reunion_rutinaria_senales_plantilla seguir_frustrado_preguntar_implantacion_ideas | cut -c1-200
    ===== observar_reunion_rutinaria_senales_plantilla | cuarentena\marquet_turn_the_ship\observar_reunion_rutinaria_senales_plantilla.json
      titulo: Sentarse en una reunion rutinaria que ya existe y leerla por sus senales de gente en vez de por su asunto tecnico
      fuente: ['marquet_turn_the_ship']
      cond: Cuando entras nuevo en una organizacion y tienes delante una de sus reuniones de repaso rutinarias, de las que ya existen y no convocas tu.
      P1. Asiste a una reunion rutinaria de repaso de la organizacion. La del texto es una reunion de jefes de departamento, un repaso rutinario de asuntos de mantenimiento.
      P2. No atiendas al asunto tecnico: observa a la gente de la sala. El texto lo escribe como eleccion deliberada, y dice incluso que probablemente deberia haber atendido a lo tecnico porque ese sistem
      P3. Mira quien llega tarde y como llega. En el texto los asistentes iban entrando tarde.
      P4. Mira si el jefe se queda fuera hasta que estan todos reunidos y entra despues, invitado. Es lo que el texto describe.
      P5. Mira si la reunion empieza tarde.
      P6. Mira a quien esta esperando cada uno. En esa reunion, dice el texto, todos estaban esperando a algun otro.
      P7. Mira como esta el que expone. El texto describe al suyo serio y directo, pero frustrado y a la defensiva ante todas las preguntas que tenia que contestar.
      P8. Mira como estan los demas. Los otros jefes de departamento y los suboficiales estaban aburridos.
      P9. Lee la falta de puntualidad con la regla que el texto escribe: puede parecer una cosa pequena, pero a bordo de un submarino nuclear las cosas pequenas como la falta de puntualidad son indicativa
    ===== seguir_frustrado_preguntar_implantacion_ideas | cuarentena\marquet_turn_the_ship\seguir_frustrado_preguntar_implantacion_ideas.json
      titulo: Seguir al que viste frustrado en una reunion y preguntarle, idea por idea, como la implanto
      fuente: ['marquet_turn_the_ship']
      cond: Cuando acabas de ver en una reunion a un responsable frustrado o a la defensiva y quieres saber si la causa esta en el o en el sistema en que trabaja.
      P1. Al acabar la reunion, siguelo a su sitio de trabajo. El texto lo dice asi: despues de la reunion segui a Dave a su camarote.
      P2. Nombrale lo que viste. La frase del texto es que parecias un poco frustrado.
      P3. Dejale contar la vision que tiene de como quiere que funcione lo suyo, y escuchale hasta el final. El texto registra que al escucharle se fue poniendo cada vez mas entusiasmado e impresionado, y
      P4. Segun vaya desgranando las ideas que tiene para mejorar su area, pregunta por cada una como la implanto.
      P5. Fijate en si la respuesta es siempre la misma. En el texto lo fue todas las veces: alguien mas arriba en la cadena de mando no habia apoyado la iniciativa, asi que no paso nada.
      P6. Mira si lo mismo pasa un piso mas abajo. El texto registra que los suboficiales que trabajaban para el tampoco parecian dispuestos a salir con ideas propias.
      P7. Quedate con el ejemplo concreto que salga de ahi. El del texto es el adiestramiento de ataque con misiles Tomahawk que habia querido dar a los oficiales varias veces, con el examen de enero por
      P8. Lee el resultado como el texto lo lee: en esencia te estaba describiendo un problema propio del modelo de lider a seguidores, aunque no usara esas palabras.

**La condicion del hijo es lo que el paso `7` de la madre deja visto** (*haber visto en una reunion a un responsable frustrado o a la
defensiva*; L21, *frustrated and defensive*), y **el hijo arranca al acabar esa misma reunion** (L23, *After the meeting I followed
Dave*). El hijo trae procedimiento propio y ningun paso de la madre: no es `REPITE`.

**MIS DUDAS, escritas antes de saber, y si alguna me cae, cae dentro de lo que marco aqui:**

- **Ese `CONTINUA` puede leerse `SANO` con la misma arista `D.29`** si el paso `7` se lee como una senial entre ocho y no como el
  producto del nodo. La arista la sostengo en las dos lecturas; lo que cambia es el veredicto de la lectura.
- **`encargar_meta_especifica_dejar_libre_metodo` con `cambiar_forma_trabajar_conservar_plantilla`**, que el barrido levanta por los
  dos lados: `SANO`, las dos caras de la misma conversacion; si el reto de `cambiar` paso `5` se lee como la consecuencia que
  `encargar` paso `4` saca, seria `CONTINUA` con madre `encargar`.
- **`contar_firmas_cadena_tramite_parado` con `seguir_frustrado_preguntar_implantacion_ideas`**, el par mas cercano del capitulo: sus
  condiciones hacen la misma pregunta (la gente o el sistema) y los dos acaban en el mismo veredicto (falla el sistema). `SANO`: fuera
  de esa pregunta, procedimiento en los dos lados y ningun paso comun.
- **`auditar_formacion_premios_ultima_fila` con `observar_reunion_rutinaria_senales_plantilla`**: la misma familia (leer una rutina
  por sus seniales de gente), `SANO` por `6.1` sin bascula.

**Las madres del grafo que busque por asunto y el barrido no levanta**, leidas con sus pasos y descartadas: Scott
`pasear_organizacion_hallar_problemas_pequenios` (la hora semanal de paseo del jefe de jefes) contra `recorrer`; Scott
`repartir_decision_cercanos_hechos` (su paso `7`, *mira a la sala, no al que habla*) contra `observar`; Zhuo
`comunicar_valores_diez_formas` (*decirlo de diez formas distintas*) contra `repetir_mensaje` (*No cambies el mensaje*); Scott
`ceder_autoridad_unilateral_equipo` contra `ceder_control`; Grove `decidir_nivel_competente_inferior` contra el ejercicio de `cap_06`.
**Dos doctrinas legitimas en cada par, con procedimiento propio en los dos lados, y ninguna es la condicion de la otra**: sin linea,
porque no los levanta el barrido, y sin arista, porque no son madre e hijo. **El de mas peso es el de Zhuo con `repetir_mensaje`**: no
lo leo contradiccion (Zhuo varia la forma y la via; Marquet no cambia el contenido), y lo dejo escrito por si alguien lo lee frontera.

## 6. **LAS ARISTAS POR LECTURA** (`D.29`, `D.37`, `D.53`)

**Las que mi lectura sostiene o descarta**, una fila cada una en `.v78aud/aristas_lectura.tsv`, con su tramo de madre, de hijo y su
linea del libro, **escritas antes de que cerrara la primera ficha del barrido** (seccion `5`), **mirando tambien madres que viven en el
grafo** (la busqueda por asunto, abajo). El cruce dice si el barrido levanto el par y donde vive hoy cada extremo:

    $ python .v78aud/cruce_aristas.py
    SOSTENGO D.29  observar_reunion_rutinaria_senales_plantilla       (bandeja) > seguir_frustrado_preguntar_implantacion_ideas          (bandeja) | levantado por el barrido: no
    DESCARTO D.29, DUDA informar_cierre_jornada_conservar_propiedad_trabajo (bandeja) > eliminar_seguimiento_descendente_responsabilizar_dueno (bandeja) | levantado por el barrido: no
    DESCARTO D.29, DUDA recorrer_organizacion_escuchar_plantilla           (bandeja) > contar_firmas_cadena_tramite_parado                    (bandeja) | levantado por el barrido: no
    DESCARTO D.29, DUDA encargar_meta_especifica_dejar_libre_metodo        (bandeja) > cambiar_forma_trabajar_conservar_plantilla             (bandeja) | levantado por el barrido: SI
    DESCARTO D.29, DUDA aplicar_ejercicio_codigo_genetico_control          (bandeja) > identificar_temas_formacion_tarjetas_decision          (bandeja) | levantado por el barrido: no
    DESCARTO D.37  ceder_control_reforzar_competencia_claridad        (bandeja) > NINGUNO (competencia tecnica y claridad organizativa)  (NINGUNA) | levantado por el barrido: no
    filas: 6 | por lo que queda: {'SOSTENGO': 1, 'DESCARTO': 5} | suma: 6
    filas con DUDA escrita: 4 de 6
    por el barrido: {'no levantada': 5, 'levantada': 1} | suma: 6

**La busqueda por asunto**, por id y titulo sobre grafo mas bandejas:

    $ python .v78aud/temas.py | grep -v "^    "
    poblacion: 479 | por sede: grafo 459, bandeja 20 | suma: 479
    delegar decisiones y autoridad: 28
    control: 5
    intencion y permiso: 5
    recorrer, caminar, escuchar: 22
    reunion: 58
    inspectores, auditores, inspeccion: 7
    formacion, entrenamiento, aprendizaje: 21
    principios y valores: 11
    mensaje y repeticion: 4
    seguimiento y pendientes: 10
    cierre de jornada, reporte, informar: 8
    meta, objetivo, metodo: 20
    premios, reconocimiento, elogio: 18
    errores y accion deliberada: 6
    solucion y urgencia: 4
    plantilla, despedir, rotacion, contratar: 27
    frustracion, ideas, iniciativa: 11
    firmas, tramite, burocracia: 2
    informacion y su reparto: 10
    responsable, a cargo, dueno: 17
    liderazgo y lider: 2
    tarjetas y retiro: 10

(La salida entera, un id por linea con su sede y su libro, en `.v78aud/temas.txt`.)

**LECTURA:**

- **MI UNICO `SOSTENGO` ES `observar_reunion_rutinaria_senales_plantilla` A `seguir_frustrado_preguntar_implantacion_ideas`, POR
  `D.29`**, citando el paso `7` de la madre (`cap_03` L21 y L23), con veredicto de la lectura `CONTINUA` (seccion `5`). El barrido no la
  levanta en ningun sentido: **es arista por lectura, no linea** (`D.53`). **El asunto de `cc46a0da` dice *1 arista por lectura***:
  coincide en la cuenta, y **si no es la misma, difiere de la mia en el par**; lo cruzo par a par en mi turno normal.
- **CUATRO `D.29` DESCARTADAS CON DUDA ESCRITA**, las cuatro por la misma razon: el libro las pone una detras de otra o por analogia,
  pero el hijo no usa el producto de la madre. **`informar_cierre` a `eliminar_seguimiento`** (`cap_09` L43: el tickler se suprime
  *modelado* sobre el cierre de jornada); **`recorrer` a `contar_firmas`** (el paseo es la ocasion, `cap_03` L37); **`encargar_meta` a
  `cambiar_forma`** (la consecuencia de `cap_02` L49 es el reto de L29; este par el barrido si lo levanta, y es su linea `SANO`); y
  **`aplicar_ejercicio` a `identificar_temas_formacion`** (dos ejercicios hermanos de tarjetas; el segundo ataca la preocupacion de
  competencia que `cap_06` L113 nombra, pero sin usar las tarjetas del primero).
- **`D.37` NO DISPARA EN ESTA TANDA.** La unica ficha cuyo texto cuenta partes y las nombra es `ceder_control_reforzar_competencia_claridad`
  (su paso `5`, *las dos cosas*: competencia tecnica y claridad organizativa, `cap_01` L97), y **ninguna de las dos partes existe como
  nodo**: los mecanismos de la bandeja que el libro pone bajo cada pilar son ejemplares del pilar, no el pilar (`D68.7`; la `76` leyo
  asi los tres tipos de sistemas de Gerber). Las listas del libro que si cuentan o enumeran (las frases de `cap_07`, los tres casos de
  urgencia de `cap_08`, los pasos de los dos ejercicios) **son los propios pasos de su ficha**, y ninguna parte vive como nodo aparte.
- **Ninguna madre del grafo para las `20`**, por mi lectura (seccion `5`, ultimo parrafo).

## 7. **EL ORDEN QUE MI LECTURA OBLIGA** (`D.36`)

**No es un orden: son las restricciones**, escritas antes de ver el del extractor. Madre antes que hijo por mis `CONTINUA` y mis
`SOSTENGO` con los dos extremos en la tanda, y cuantas cumple el orden de pieza del libro, **que saco de mi fidelidad** (capitulo y
primera linea), porque `.v78aud/las20.txt` va alfabetica:

    $ python .v78aud/restricciones_orden.py
    orden de pieza del libro (capitulo y primera linea de mi fidelidad): 20
       1 cap_01 L97 ceder_control_reforzar_competencia_claridad
       2 cap_02 L25 cambiar_forma_trabajar_conservar_plantilla
       3 cap_02 L33 encargar_meta_especifica_dejar_libre_metodo
       4 cap_03 L11 recorrer_organizacion_escuchar_plantilla
       5 cap_03 L17 observar_reunion_rutinaria_senales_plantilla
       6 cap_03 L23 seguir_frustrado_preguntar_implantacion_ideas
       7 cap_03 L37 contar_firmas_cadena_tramite_parado
       8 cap_03 L45 inspeccionar_reparto_informacion_notas_jefe
       9 cap_03 L55 auditar_formacion_premios_ultima_fila
      10 cap_04 L35 informar_cierre_jornada_conservar_propiedad_trabajo
      11 cap_06 L101 aplicar_ejercicio_codigo_genetico_control
      12 cap_06 L127 asignar_responsable_unico_evolucion_planificada
      13 cap_07 L55 declarar_intencion_reemplazar_peticion_permiso
      14 cap_08 L107 resistir_dar_solucion_clasificar_decision_urgencia
      15 cap_09 L71 eliminar_seguimiento_descendente_responsabilizar_dueno
      16 cap_10 L45 acoger_inspectores_externos_fuente_aprendizaje
      17 cap_11 L75 tomar_accion_deliberada_pausar_vocalizar_gesticular
      18 cap_12 L125 identificar_temas_formacion_tarjetas_decision
      19 cap_13 L119 repetir_mensaje_invariable_diario_reunion_evento
      20 cap_14 L89 reforzar_principios_guia_lenguaje_prueba_conocimiento
    restricciones: 7
      observar_reunion_rutinaria_senales_plantilla               antes que seguir_frustrado_preguntar_implantacion_ideas                arista por lectura     el orden del libro la cumple
      seguir_frustrado_preguntar_implantacion_ideas              antes que acoger_inspectores_externos_fuente_aprendizaje               D.36, solo lo levanta acoger_inspectores_externos_fuente_aprendizaje el orden del libro la cumple
      recorrer_organizacion_escuchar_plantilla                   antes que acoger_inspectores_externos_fuente_aprendizaje               D.36, solo lo levanta acoger_inspectores_externos_fuente_aprendizaje el orden del libro la cumple
      recorrer_organizacion_escuchar_plantilla                   antes que auditar_formacion_premios_ultima_fila                        D.36, solo lo levanta auditar_formacion_premios_ultima_fila el orden del libro la cumple
      informar_cierre_jornada_conservar_propiedad_trabajo        antes que declarar_intencion_reemplazar_peticion_permiso               D.36, solo lo levanta declarar_intencion_reemplazar_peticion_permiso el orden del libro la cumple
      reforzar_principios_guia_lenguaje_prueba_conocimiento      antes que declarar_intencion_reemplazar_peticion_permiso               D.36, solo lo levanta declarar_intencion_reemplazar_peticion_permiso EL ORDEN DEL LIBRO LA VIOLA
      inspeccionar_reparto_informacion_notas_jefe                antes que recorrer_organizacion_escuchar_plantilla                     D.36, solo lo levanta recorrer_organizacion_escuchar_plantilla EL ORDEN DEL LIBRO LA VIOLA
    que obligan (madre antes que hijo): 1 | violadas por el orden del libro: 0
    D.36 de un solo lado, informativas: 6
    $ python .v78aud/restricciones_orden.py | grep -c "LA VIOLA"
    2

**LECTURA:** **la unica que obliga** (`observar` antes que `seguir`, por la arista de la seccion `6`) **la cumple ya el orden de pieza
del libro**. De las `6` de `D.36` de un solo lado, **dos no las cumple** (`reforzar_principios_guia_lenguaje_prueba_conocimiento` antes
que `declarar_intencion_reemplazar_peticion_permiso`, e `inspeccionar_reparto_informacion_notas_jefe` antes que
`recorrer_organizacion_escuchar_plantilla`); **son informativas y no obligan**, porque la aduana de `insertar` mide grafo mas bandejas
(`D.38.5`) y el par se levanta igual desde el lado que entre despues. **Su orden, contra estas siete, lo compruebo en mi turno normal.**


## 8. **`R8` MEDIDO SOBRE MI ENCARGO DE LA `78`, CON EL MISMO INSTRUMENTO** (`ACTA 76` `76.12` y `76.13`)

`R8` dice: *toda cifra de medida que escriba en `PROMPT_SIGUIENTE.md` (un reloj, una banda, una cuenta que solo se comprueba abriendo
un fichero, en digito o en letra) va DENTRO de un bloque `$` con su salida, o lleva EN SU MISMA LINEA la seccion del acta donde esta
pegada: ni la de la linea de al lado, ni una ruta de fichero*. El fichero es el encargo que escribi al cerrar la `ACTA 76`, y el
instrumento es el de la `76.13`, corrido sin copiarlo, con su salida de hoy contra la que guardo aquella acta:

    $ head -1 docs/loop/PROMPT_SIGUIENTE.md | cut -c1-100; ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, $7, $9}'
    # ENCARGO DE LA VUELTA 78: **LAS FICHAS DE MARQUET DEJADAS LISTAS PARA INSERTAR: SU FIDELIDAD LEIDA
    2026-09-26 13:19:12.123204000 docs/loop/PROMPT_SIGUIENTE.md
    $ python .v77aud/normal/r8_encargo78.py | diff - .v77aud/normal/r8_encargo78.txt && echo "IDENTICO a .v77aud/normal/r8_encargo78.txt, la salida de la ACTA 76 76.13"; python .v77aud/normal/r8_encargo78.py | tail -1
    IDENTICO a .v77aud/normal/r8_encargo78.txt, la salida de la ACTA 76 76.13
    lineas del encargo: {'linea de bloque sangrado': 13, 'prosa con numero, con seccion de la ACTA 76': 14, 'prosa con numero, sin seccion de la ACTA 76': 57, 'prosa sin digito ni palabra de numero': 69} | suma: 153

(Cada linea con numero, con sus digitos y sus palabras de numero, en `.v77aud/normal/r8_encargo78.txt`.) **LECTURA, que es mia y no
del instrumento: volvi a leer una a una las `57` lineas de prosa con numero sin seccion** (las de la salida de arriba, con sus numeros
de linea en ese fichero) **y llego al mismo reparto que la `76.13`**: numeros de vuelta, de acta, de mundo, de fecha o de carpeta de la
casa; secciones, reglas, deudas, remedios y numeros de tarea o de punto; identificadores de capitulo y de fichero; umbrales y topes de
regla (*cinco a la vez como mucho*, el `10` por ciento); y palabras de numero que no son cuenta de fichero (*los dos delante*, *en
cero*, *cero guiones*). **Las cifras de medida** van dentro de un bloque `$` (el reloj del barrido de la `76`, la clase, el tablero y el
texto de `d150`, los cuatro que `R10` compara arriba) o llevan su seccion de la `ACTA 76` en la misma linea. **Ninguna cuenta de fichero
suelta.**

**`R8` CUMPLIDO EN EL ENCARGO DE LA `78`, medido otra vez aqui.**

## 9. **LO QUE DEJO PARA MI TURNO NORMAL, ESCRITO ANTES DE VER EL REPORTE**

1. **`R5`** en su reporte, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` sacados otra vez de los originales y con la
   cabecera cambiada a la `78`; **y `R9`** en su cuenta de PUENTE, con su patron contra el mio.
2. **El censo con su hash**: que la vuelta no movio el grafo, la bitacora, los censos ni la bandeja de Gerber, y que en la de Marquet
   solo cambiaron las `2` fichas corregidas, **con `git diff`**; y quien escribio que y a que hora.
3. **Mi fidelidad contra la suya, paso a paso**: mis `110` filas contra las suyas; sus tres correcciones contra mi lectura de sus textos
   viejos (seccion `3`); **mis dos dudas de `cap_03`**, que son su misma figura; y **`d150`**, su fila de `cap_03` contra la mia.
4. **Mi barrido contra el suyo, fila dirigida a fila dirigida**, y **mis clases contra sus lineas de veredicto, par a par**, con **mi
   `CONTINUA` de la seccion `5`, que es arista por lectura, contra su *1 arista por lectura***, **por par y no por cuenta**, y mis
   cuatro `D.29` descartadas con duda contra lo que el lea (secciones `4` a `6`).
5. **Su orden contra mis restricciones** (seccion `7`).
6. **La huella de las `20` fichas** que su cierre dice sellar, contra las mias de `.v78aud/huellas_al_barrer.txt`, tomadas antes de
   barrer y comprobadas al recogerlo.
7. **La muestra pineada de los SANO**: esta vuelta no escribe en la bitacora; los `SANO` de las `20` se muestrean cuando entren.
8. **`R8` sobre el encargo de la `79`**, medido antes de cerrarlo, y **`R10`**: toda salida que pegue en el encargo, corrida despues de
   mi ultima escritura en el registro que mide, o vuelta a correr antes del commit y comparada. **La `79` es de saneamiento por
   cadencia** (`ACTA 76` `76.11`), y la insercion de Marquet cae despues.

## 10. **ESTA PAGINA CONTRA `R6`, `R7` Y LOS GUIONES, MEDIDA SOBRE ELLA MISMA**

El generador corre dos veces, y estos bloques de la segunda pasada leen la pagina que escribio la primera, identica salvo estos
bloques. El primero cuenta las lineas de bloque `$` que empiezan por una clave de relacion; el segundo, con la copia de
`.v76aud/r7_pagina.py`, cuenta las lineas de bloque que reparten una cifra en clases y cuantas traen su `suma`; el tercero cuenta
guiones largos y medios:

    $ grep -c -E "^    +(previos|siguientes|nodos_previos|nodos_siguientes)" docs/loop/APERTURA_CIEGA.md
    0
    $ python .v78aud/r7_pagina.py
    lineas de bloque que reparten en clases: 15 | por estado: {'con suma': 15} | suma: 15
    $ grep -c -P "\x{2014}|\x{2013}" docs/loop/APERTURA_CIEGA.md
    0
