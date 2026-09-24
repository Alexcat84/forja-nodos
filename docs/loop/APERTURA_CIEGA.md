# APERTURA CIEGA DE LA VUELTA 66, lote 7 (`grove_high_output`), **CLASE INSERCION**

*Auditor `claude-opus-5-5`, fase ciega, 24 sep 2026, la que el arnes numera `VUELTA 2` en la corrida que
arranco el 23 a las `21:50`. Linea **serial**, rama `extraccion-mundo-11`, arbol en `7f31919` (el ultimo commit
del extractor). Modo austero (`D.47`). Todo lo de esta pagina sale de `.v66aud/`, escrito y corrido en esta
fase; cada bloque `$` lo pega `.v66aud/generar_apertura.py` corriendo el comando en el momento de escribirla.
**No hay ninguna tabla en esta pagina**, a proposito: la de la `65` tumbo el cierre estricto (`d167`).*

## 0. **LA HERENCIA** (`D.40`)

ACTA ANTERIOR LEIDA: a375d366bc277ac09d60d69b980e2e8173a345c3

HEREDADO 1: NO APLICA en esta fase. **Motivo:** `R5` es un remedio **del extractor** y se mide **sobre su
reporte de la `66`** (`ACTA 64` `64.11`: *el reporte de la `66`, con `.v64ext/pegado64.py` y
`.v64aud/normal/bloques_mudos.py`, los dos con la cabecera del tramo cambiada a la `66`*), y el reporte **no
esta en el arbol**: el arnes lo retiro para esta fase (`D.34.2`) y no lo recupero por ninguna via. **Se mide en
mi turno normal**, con los dos instrumentos y la cabecera cambiada a la `66`, sacados otra vez de los
originales y no de las copias del extractor. Lo que si esta en mi mano lo cumplo en mi propia pagina: cada
bloque `$` de aqui lleva la salida del comando que abre, y nada mas.

    $ ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl
    ls: cannot access 'docs/loop/REPORTE.md': No such file or directory
    ls: cannot access 'docs/loop/ultimo_extractor.json': No such file or directory
    ls: cannot access 'docs/loop/ultimo_auditor.json': No such file or directory
    ls: cannot access 'docs/loop/CREDITO_serial.jsonl': No such file or directory
    $ grep -n "VUELTA 2 : APERTURA CIEGA" docs/loop/loop.log | tail -1
    5490:[2026-09-24 03:48:10] VUELTA 2 : APERTURA CIEGA (claude-opus-5-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl

**LA HUELLA** es la que el prompt me entrega, y la he comprobado solo contra el propio prompt; **no la he
recomputado**, porque `forja.py herencia` lee en esta fase un fichero retirado (`d146`) y no lo corro aqui.

## 1. **LO QUE VI SIN BUSCARLO, Y LO DIGO ANTES DE MEDIR** (`d146`)

**La foto de `git status` que el entorno me pone delante, y un `git log --oneline -12` que corri para saber en
que commit estaba el arbol, traen los asuntos de los commits del extractor**, y dos son cifras de su cierre:
`15d51d8` *Vuelta 66, T3: cap_04 listo para la 67 (fidelidad 0 de 156, barrido de los 22 recogido, 99 veredictos
comprobados, 9 aristas por lectura, orden con las tres comprobaciones en cero)* y `d8f4e2a` *Vuelta 66, T4: el
cierre (368 nodos, bandeja de Grove en 69, cap_03 0 de 13 y cap_04 0 de 156, R5 en cero, guardas verdes y el
rojo estricto de d167 declarado)*. **Los lei antes de medir nada.** Es el mismo hueco de `d146` que ya declaro la
apertura de la `65`, y no lo arreglo yo (`D.45`).

**LO QUE HAGO CON ELLO:** ninguna cifra de esta pagina sale de esos asuntos. Todas salen de un instrumento
corrido en esta fase, y donde coinciden lo digo como coincidencia y no como fuente. **Las clases no las tocan**:
los asuntos no nombran ni un veredicto ni un par. **No he abierto nada de `.v66ext/`** (ni su fidelidad, ni sus
veredictos, ni sus aristas, ni su orden), **ni `bitacora/VEREDICTOS.jsonl` por dentro**: de ella solo cuento
lineas.

## 2. **EL ALCANCE, Y EL CENSO QUE LO SOSTIENE**

La vuelta tenia dos trabajos (encargo de la `66`): **insertar las filas `21` y `22`** de Grove
(`variar_frecuencia_inspeccion_nivel_calidad` y `simplificar_trabajo_reducir_numero_pasos`), y **dejar `cap_04`
listo sin insertar ninguno**: fidelidad entera, barrido, veredictos, aristas por lectura y orden.

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        368 dataset/nodos.jsonl
        796 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1165 total
    $ ls cuarentena/grove_high_output/*.json | wc -l
    69
    $ ls cuarentena/_insertados/grove_high_output/*.json | wc -l
    23
    $ git diff --stat 3174c73 HEAD -- dataset/ bitacora/ censos/ config/pares_mutuos.jsonl
     bitacora/VEREDICTOS.jsonl | 1 +
     censos/atribuciones.md    | 2 ++
     censos/denominaciones.md  | 7 +++++++
     dataset/nodos.jsonl       | 2 ++
     4 files changed, 12 insertions(+)
    $ git diff --name-status 3174c73 HEAD -- cuarentena/
    R100	cuarentena/grove_high_output/simplificar_trabajo_reducir_numero_pasos.json	cuarentena/_insertados/grove_high_output/simplificar_trabajo_reducir_numero_pasos.json
    R100	cuarentena/grove_high_output/variar_frecuencia_inspeccion_nivel_calidad.json	cuarentena/_insertados/grove_high_output/variar_frecuencia_inspeccion_nivel_calidad.json
    $ ls -A procesos/ | wc -l
    0
    $ git status --short -- dataset bitacora censos cuarentena config | wc -l
    0

**LECTURA:** contra el censo de la `ACTA 64` `64.1` (`366`, `795`, `1`, `71`, `21`), el grafo sube `2`, la
bitacora gana `1` linea, los pares mutuos no se mueven, la bandeja baja `2` y `_insertados` sube `2`. **Desde el
commit de la `ACTA 64` (`3174c73`) lo unico que se movio en `cuarentena/` son los dos `git mv` de las filas `21` y
`22`, al cien por cien de similitud: ninguna ficha de `cap_04` cambio en la bandeja**, asi que la vuelta no
corrigio ningun paso de `cap_04`. `procesos/` esta vacio: ningun cerrojo quedo cogido. De quien es la linea
nueva de la bitacora no lo miro aqui: seria abrirla.

## 3. **LAS FILAS `21` Y `22`: LO QUE ENTRO ES LO QUE SE LEYO** (`D.58`)

Copia de `.v65aud/entra_lo_leido.py` con la tanda cambiada a las filas `21` y `22` de `.v64ext/los22.txt`:
compara titulo, condiciones, pasos y entregable del nodo del grafo con la ficha en el commit de su lectura
entera (`b63405c`), y el blob de `_insertados` con ese mismo commit.

    $ python .v66aud/entra_lo_leido.py
    variar_frecuencia_inspeccion_nivel_calidad         cap_03 P19  leida en b63405c pasos  6 P 0
    simplificar_trabajo_reducir_numero_pasos           cap_03 P23  leida en b63405c pasos  7 P 0
    nodos de la tanda en el grafo iguales a su lectura entera: 2 | distintos: 0
    fichas de _insertados con el mismo blob que su lectura entera: 2 | distintas: 0
    capitulo  cand pasos    P   por100
    cap_03       2    13    0     0.00
    tanda        2    13    0     0.00

**LECTURA:** las dos viven en el grafo con los bytes que se leyeron, y sus `13` pasos son los de la lectura
entera que adjudico la `ACTA 62` `62.6` (`cap_03`, `0` PUENTE en esas dos). **La fila de `cap_03` de lo que entra
es `0` de `13`.**

**SU BARRIDO DE HOY, sobre GRAFO MAS BANDEJAS** (`D.38.4`), con la copia de `.v65aud/barrido_uno.py` que lee de
`_insertados` para estas dos (poblacion `479`: `368` del grafo, que ya las contiene, y `111` de bandejas; cada
una se excluye a si misma por id):

    $ cat .v66aud/barrido_variar_frecuencia_inspeccion_nivel_calidad.txt .v66aud/barrido_simplificar_trabajo_reducir_numero_pasos.txt
    variar_frecuencia_inspeccion_nivel_calidad poblacion 479 (368 grafo mas 111 bandejas) vecinos 0
    simplificar_trabajo_reducir_numero_pasos poblacion 479 (368 grafo mas 111 bandejas) vecinos 1
    $ grep -E "^    (variar|simplificar)" .v66aud/vecinos_tabla.txt | grep ">"
        simplificar_trabajo_reducir_numero_pasos               > dimensionar_plantilla_administrativa_pronostico        grafo   similitud_texto  0.351 0.000 0.439

**LECTURA:** la `21` no levanta a nadie, que es lo que el encargo esperaba (*entraba sin vecinos contra
`462`*), y ahora contra `479`, con la cosecha de Marquet ya en la bandeja. La `22` levanta **un solo vecino, del grafo**,
`dimensionar_plantilla_administrativa_pronostico`: es el par de su bloque de `.v64ext/veredictos_listos.txt`
(adjudicado en la `ACTA 63`), no uno nuevo. **Mi clase, leyendo los pasos de los dos**
(`.v66aud/pasos_fila22.txt`): **SANO**. Diagrama de flujo, contar pasos y tirar los que no aguantan la pregunta
por que, contra dimensionar la plantilla de una unidad administrativa por el pronostico de su carga: ni un paso
compartido. **Cero vecinos nuevos que la aduana de las dos haya podido levantar sin linea lista.**

## 4. **LA FIDELIDAD DE `cap_04`, LEIDA ENTERA** (`D.30`, `D.58`, `8`)

Lei `fuentes/grove_high_output/cap_04.md` entero (Cap. 3, *Managerial Leverage*) y cada paso de los `22` contra
su linea.

    $ wc -l fuentes/grove_high_output/cap_04.md
    323 fuentes/grove_high_output/cap_04.md

Una fila por paso en `.v66aud/fidelidad.tsv`: `T` transcripcion, `P` puente (**la
clausula reescrita cuenta como `P`**, `ACTA 62` `62.5`), `D` mi duda. El contador es copia de
`.v64aud/contar_fidelidad.py` con las rutas cambiadas, y cruza cada fila con los pasos de la ficha de la bandeja
de hoy:

    $ python .v66aud/contar_fidelidad.py
    candidato                                        ficha filas   T   P  DUDA
    reunir_informacion_gerencial_vias_variadas           8     8   8   0     0
    escalonar_fuentes_informacion_gerencial              7     7   7   0     0
    programar_visita_area_observar_despachar             8     8   8   0     0
    transmitir_objetivos_prioridades_preferencias        5     5   5   0     0
    empujar_persona_reunion_direccion_preferida          7     7   7   0     0
    subir_productividad_gerencial_tres_vias              4     4   4   0     0
    buscar_actividad_alta_palanca_tres_vias              4     4   3   0     1
    elegir_momento_actividad_palanca_maxima              7     7   7   0     0
    detectar_palanca_negativa_actividad_mando            9     9   6   0     3
    delegar_tarea_base_comun_seguimiento                10    10  10   0     0
    supervisar_tarea_delegada_etapa_menor_valor          9     9   9   0     0
    supervisar_decision_delegada_preguntas_concretas     6     6   6   0     0
    identificar_paso_limitante_jornada_desfases          5     5   5   0     0
    agrupar_tareas_semejantes_aprovechar_preparacion     6     6   6   0     0
    decir_no_trabajo_excede_capacidad                   10    10  10   0     0
    usar_calendario_herramienta_planificacion_produccion     7     7   7   0     0
    llevar_inventario_proyectos_discrecionales           5     5   5   0     0
    dimensionar_numero_subordinados_medio_dia_semanal    11    11  11   0     0
    buscar_regularidad_bloques_iguales_trabajo_mando     9     9   9   0     0
    preparar_respuestas_estandar_interrupciones_repetidas     6     6   6   0     0
    agrupar_interrupciones_subordinados_reuniones_regulares     5     5   5   0     0
    canalizar_interrupciones_cartel_hora_oficina         8     8   8   0     0
    total cap_04                                       156   156 152   0     4
    PUENTE sobre pasos escritos: 0 de 156 = 0.00 por ciento
    si las 4 DUDA cayesen a PUENTE: 4 de 156 = 2.56 por ciento

**LECTURA: `cap_04` es un capitulo de inventario rico**, casi todo frases con mandato propio (*you should*,
*we should*, *you must*) o con el medio nombrado, y los pasos lo transcriben pieza a pieza. **No encuentro ningun
PUENTE.** Mis cuatro dudas son **la misma figura**, un verbo de marco que el extractor pone y el libro no:

- `buscar_actividad_alta_palanca_tres_vias` paso `1`, *Repasa tus actividades buscando...*: L205 y L207 dan las
  tres vias, no el repaso. Me inclino a `T`, porque L193 (*being sensitive to the leverage of what you do during
  the day*) y L241 (*select from the many activities*) si piden mirar las propias actividades, aunque fuera de la
  pieza.
- `detectar_palanca_negativa_actividad_mando` pasos `3`, `5` y `7`, *Revisa si estas desanimado / dando largas /
  entrometiendote*: el contenido es de L231 a L235. **La del paso `3` es la mas delgada**: el libro dice del
  mando desanimado que *didn't realize it* y que salio *only when someone on his staff finally told him*, o sea
  que no lo ve desde dentro. Me inclino a `T` por ser el marco del propio nodo, **y un lector estricto lo leeria
  PUENTE de clausula como el de la `ACTA 62` `62.5`**.

**Y lo que NO marco duda, para que se vea el criterio:** `delegar_tarea_base_comun_seguimiento` paso `2`
(*comprueba que comparten una base comun*) traslada el *must share* de un requisito de L245, y su paso `4`
(*Revisa que tareas no quieres soltar*) lo sostiene *be sure to know exactly what you're doing* de L247.

**`PASOS INVENTADOS` de `cap_04`, por mi instrumento: `0` de `156`, y `4` de `156` si mis cuatro dudas cayesen
a PUENTE.** Por debajo del `10` en las dos lecturas. Es preparacion y no entrada.

## 5. **MI BARRIDO DE `cap_04`, SOBRE GRAFO MAS BANDEJAS** (`D.38.4`, `D.38.5`)

Copia de `.v65aud/barrido_uno.py` que lee la ficha de `cuarentena/grove_high_output/` y la normaliza como la
aduana, contra `dataset/nodos.jsonl` mas `aduana.poblacion_de_bandejas`, con `buscar_vecinos` de `src/aduana.py`;
y copia de `.v65aud/barrer.sh` con la lista cambiada, **cinco a la vez**. Las `24` fichas (las dos filas y los
`22`) en un solo barrido, **recogido entero dentro de este turno**. Antes de lanzarlo guarde la huella de cada
ficha de la bandeja, y al recogerlo las comprobe:

    $ head -1 .v66aud/barrido.log; tail -1 .v66aud/barrido.log; grep -c "rc=0" .v66aud/barrido.log; grep -c "rc=" .v66aud/barrido.log
    INICIO 2026-09-24 03:49:49
    TODOS TERMINADOS 2026-09-24 06:04:00
    24
    24
    $ sha1sum -c --quiet .v66aud/huellas_bandeja_al_barrer.txt && echo "bandeja de grove: mismas huellas que al barrer"
    bandeja de grove: mismas huellas que al barrer
    $ cat .v66aud/head_al_barrer.txt; git rev-parse HEAD
    7f31919c0963f1db9565101762618db376f5c16c
    7f31919c0963f1db9565101762618db376f5c16c

**Poblacion y vecinos por candidato:**

    $ python .v66aud/vecinos_tabla.py | sed -n '1,/^sin fichero/p'
    (1) candidato | poblacion | vecinos | en grafo | en bandeja
        variar_frecuencia_inspeccion_nivel_calidad               479   0   0   0
        simplificar_trabajo_reducir_numero_pasos                 479   1   1   0
        reunir_informacion_gerencial_vias_variadas               479   7   0   7
        escalonar_fuentes_informacion_gerencial                  479   7   0   7
        programar_visita_area_observar_despachar                 479   7   0   7
        transmitir_objetivos_prioridades_preferencias            479   7   0   7
        empujar_persona_reunion_direccion_preferida              479   7   0   7
        subir_productividad_gerencial_tres_vias                  479   7   0   7
        buscar_actividad_alta_palanca_tres_vias                  479   7   0   7
        elegir_momento_actividad_palanca_maxima                  479   7   0   7
        detectar_palanca_negativa_actividad_mando                479   0   0   0
        delegar_tarea_base_comun_seguimiento                     479   0   0   0
        supervisar_tarea_delegada_etapa_menor_valor              479   3   1   2
        supervisar_decision_delegada_preguntas_concretas         479   3   0   3
        identificar_paso_limitante_jornada_desfases              479   6   0   6
        agrupar_tareas_semejantes_aprovechar_preparacion         479   5   0   5
        decir_no_trabajo_excede_capacidad                        479   4   0   4
        usar_calendario_herramienta_planificacion_produccion     479   1   0   1
        llevar_inventario_proyectos_discrecionales               479   6   0   6
        dimensionar_numero_subordinados_medio_dia_semanal        479   0   0   0
        buscar_regularidad_bloques_iguales_trabajo_mando         479   4   0   4
        preparar_respuestas_estandar_interrupciones_repetidas    479   2   0   2
        agrupar_interrupciones_subordinados_reuniones_regulares  479   8   3   5
        canalizar_interrupciones_cartel_hora_oficina             479   1   0   1
    sin fichero de vecinos: 0 []
    $ grep ">" .v66aud/vecinos_tabla.txt | grep -Ev "^    (variar|simplificar)" | wc -l
    99
    $ grep ">" .v66aud/vecinos_tabla.txt | grep -Ev "^    (variar|simplificar)" | grep -c " grafo "
    4
    $ tail -1 .v66aud/vecinos_tabla.txt
    pares sin orden: 53 | {'con fuera': 5, 'cap04-cap04': 48}
    $ grep ">" .v66aud/vecinos_tabla.txt | grep -E "^    (reunir|escalonar|programar|transmitir|empujar|subir|buscar_actividad|elegir_momento)" | wc -l
    56
    $ grep ">" .v66aud/vecinos_tabla.txt | grep -E "^    (reunir|escalonar|programar|transmitir|empujar|subir|buscar_actividad|elegir_momento)" | awk '{print $6}' | sort -n | sed -n '1p;$p'
    0.391
    0.544
    $ grep ">" .v66aud/vecinos_tabla.txt | grep " grafo "
        simplificar_trabajo_reducir_numero_pasos               > dimensionar_plantilla_administrativa_pronostico        grafo   similitud_texto  0.351 0.000 0.439
        supervisar_tarea_delegada_etapa_menor_valor            > detectar_arreglar_fallo_etapa_menor_valor              grafo   familia_id       0.226 0.333 0.435
        agrupar_interrupciones_subordinados_reuniones_regulares > sostener_contacto_oferta_aceptacion                    grafo   paso_contra_nodo 0.094 0.000 0.700
        agrupar_interrupciones_subordinados_reuniones_regulares > agendar_cuidados_propios_cumplirlos                    grafo   paso_contra_nodo 0.129 0.000 0.615
        agrupar_interrupciones_subordinados_reuniones_regulares > nombrar_delegados_amigos_casa                          grafo   paso_contra_nodo 0.127 0.000 0.609
    $ cat .v66aud/detalle_paso_notables.txt
    agrupar_tareas_semejantes_aprovechar_preparacion > buscar_regularidad_bloques_iguales_trabajo_mando | paso 1 del candidato contra paso 1 de buscar_regularidad_bloques_iguales_trabajo_mando
    elegir_momento_actividad_palanca_maxima > subir_productividad_gerencial_tres_vias | paso 1 del candidato contra paso 3 de subir_productividad_gerencial_tres_vias
    transmitir_objetivos_prioridades_preferencias > reunir_informacion_gerencial_vias_variadas | paso 1 del candidato contra paso 4 de reunir_informacion_gerencial_vias_variadas
    supervisar_tarea_delegada_etapa_menor_valor > detectar_arreglar_fallo_etapa_menor_valor | paso 1 del candidato contra paso 2 de detectar_arreglar_fallo_etapa_menor_valor
    sostener_contacto_oferta_aceptacion | paso 4 del candidato contra paso 3 de sostener_contacto_oferta_aceptacion
    agendar_cuidados_propios_cumplirlos | paso 4 del candidato contra paso 4 de agendar_cuidados_propios_cumplirlos
    nombrar_delegados_amigos_casa | paso 4 del candidato contra paso 4 de nombrar_delegados_amigos_casa

**LECTURA:** el barrido de los `22` da **`99` filas de vecino**, `4` de ellas con el vecino en el grafo y el resto
dentro de la bandeja, y **`53` pares sin orden** contando el de la fila `22`: `48` entre dos candidatos de
`cap_04` y `5` con uno de fuera. **Coincide con el `99` del asunto de `15d51d8`, y lo digo como coincidencia.**
Tres cosas que se ven en la tabla y pesan para la `67`:

1. **Los ocho primeros de la pieza (`P7` a `P20`) se levantan todos entre si, siete vecinos cada uno**: `56`
   filas, todas por `similitud_texto`, entre `0,391` y `0,544`. **LECTURA, sin medirla:** supongo que lo que
   las junta es el texto comun de su `resumen_teorico` y la tipologia de actividades de L145 a L217; lo que si
   leo es que casi todo es SANO (seccion `6`).
2. **`detectar_palanca_negativa_actividad_mando`, `delegar_tarea_base_comun_seguimiento` y
   `dimensionar_numero_subordinados_medio_dia_semanal` no levantan a nadie**, contra `479`. Las relaciones de
   `delegar` son por lectura (seccion `7`).
3. **Los cuatro vecinos del grafo:** `detectar_arreglar_fallo_etapa_menor_valor` levantado por
   `supervisar_tarea_delegada_etapa_menor_valor` (**por `familia_id`, `0.333`**, paso `1` del candidato contra
   paso `2` de la madre: la arista EN COLA de la `65`
   **si la levanta el barrido**, y va entre los veredictos con `madre=`, no entre las aristas por lectura), y tres
   ajenos de otros libros que `agrupar_interrupciones_subordinados_reuniones_regulares` levanta por
   `paso_contra_nodo` en su paso `4` (*Manten esas reuniones con regularidad*).

**EL RELOJ, medido y no techo:** de `929` a `3767` s por ficha, de las `03:49:49` a las `06:04:00`.

    $ grep "rc=" .v66aud/barrido.log | sed 's/.*segundos=//' | sort -n | sed -n '1p;$p'
    929
    3767

## 6. **MI LECTURA CIEGA DE LOS PARES** (`1.2`, `6.1`, y solo la vara `6.1`)

**Leidos con los pasos de los dos delante** (`.v66aud/volcar22.txt` para los `22`, y `python .v64aud/pasos.py`
para los de fuera: `.v66aud/pasos_graf_a.txt`, `.v66aud/pasos_graf_b.txt`, `.v66aud/pasos_fila22.txt`), y el
paso que cruza cada senial en `.v66aud/detalle_paso_notables.txt`. **Una fila por par** en `.v66aud/mis_clases.tsv`,
con su razon. El cruce, que comprueba que cada par del barrido tiene su fila y cada fila su par:

    $ python .v66aud/cruce_clases.py
    pares del barrido: 53 | filas de clase: 53
    pares sin fila: []
    filas sin par: []
    clases: {'SANO': 48, 'CONTINUA': 5}
    con DUDA escrita: 2
      CONTINUA  escalonar_fuentes_informacion_gerencial ~ reunir_informacion_gerencial_vias_variadas | madre reunir_informacion_gerencial_vias_variadas
      CONTINUA  buscar_actividad_alta_palanca_tres_vias ~ subir_productividad_gerencial_tres_vias | madre subir_productividad_gerencial_tres_vias
      CONTINUA  buscar_actividad_alta_palanca_tres_vias ~ elegir_momento_actividad_palanca_maxima | madre buscar_actividad_alta_palanca_tres_vias
      CONTINUA  detectar_arreglar_fallo_etapa_menor_valor ~ supervisar_tarea_delegada_etapa_menor_valor | madre detectar_arreglar_fallo_etapa_menor_valor
      CONTINUA  decir_no_trabajo_excede_capacidad ~ usar_calendario_herramienta_planificacion_produccion | madre usar_calendario_herramienta_planificacion_produccion

**LECTURA, los cinco `CONTINUA`**, y en los cinco el hijo trae procedimiento propio, asi que ninguno es
`REPITE`:

- `reunir_informacion_gerencial_vias_variadas` madre de `escalonar_fuentes_informacion_gerencial`: la condicion
  de escalonar (*ya tienes abiertas varias vias*) es el producto de reunir, y escalonar pone la jerarquia y la
  redundancia de L153. Cruzan un solo paso (la verbal por delante, reunir `7` contra escalonar `2`).
- `subir_productividad_gerencial_tres_vias` madre de `buscar_actividad_alta_palanca_tres_vias`: la condicion de
  buscar (*ya sabes que quieres subir la palanca*) es subir `3` y `4`.
- `buscar_actividad_alta_palanca_tres_vias` madre de `elegir_momento_actividad_palanca_maxima`: la condicion de
  elegir (*la actividad que tienes delante es de las de alta palanca*) es el producto de buscar; elegir anade el
  cuando de L215 y L217.
- `detectar_arreglar_fallo_etapa_menor_valor` madre de `supervisar_tarea_delegada_etapa_menor_valor`: el paso `2`
  del hijo es el paso `3` de la madre aplicado a la tarea delegada. **Es lo que ya adjudicaron la `ACTA 61`
  `61.5` y la `ACTA 62` `62.5`**, y lo sostengo.
- `usar_calendario_herramienta_planificacion_produccion` madre de `decir_no_trabajo_excede_capacidad`: L279,
  *to use your calendar as a production-planning tool, you must accept responsibility for two things*, y la
  segunda es decir que no (L283).

**MIS DOS DUDAS, escritas antes de saber:** el `CONTINUA` de `decir_no` con `usar_calendario` **puede leerse
SANO de hermanos** (son dos principios de produccion, L273 a L275 y L277, que L279 junta); y el `SANO` de
`elegir_momento` con `subir_productividad` **puede leerse `CONTINUA` con madre `subir`**, porque el cuando es una
manera de subir la palanca. Si alguna de las dos me cae, cae dentro de lo que marco aqui.

**Y el par con la cifra mas alta del barrido**, `agrupar_tareas_semejantes_aprovechar_preparacion` con
`buscar_regularidad_bloques_iguales_trabajo_mando` a `paso_contra_nodo` `0,718`, es **paso `1` contra paso `1`**,
el mismo marco (*Aplica a tu trabajo de mando el ... de produccion*), y lo leo **SANO**: la tanda ahorra
preparacion (L269, L271), la regularidad da prevision y se coordina con otros (L305, L307).

## 7. **LAS ARISTAS POR LECTURA** (`D.29`, `D.37`, `D.53`)

**Las que el barrido NO levanta y la lectura si sostiene**, una fila cada una en `.v66aud/aristas_lectura.tsv`
con su tramo de madre, de hijo y su linea del libro. El cruce dice si el barrido levanto el par (entonces no
seria arista por lectura sino linea de veredicto) y donde vive hoy cada extremo:

    $ python .v66aud/cruce_aristas.py
    SOSTENGO       construir_flujo_produccion_paso_limitante          (grafo) > identificar_paso_limitante_jornada_desfases            (bandeja) | levantado por el barrido: no
    SOSTENGO, DUDA variar_frecuencia_inspeccion_nivel_calidad         (grafo) > supervisar_tarea_delegada_etapa_menor_valor            (bandeja) | levantado por el barrido: no
    SOSTENGO       delegar_tarea_base_comun_seguimiento               (bandeja) > supervisar_tarea_delegada_etapa_menor_valor            (bandeja) | levantado por el barrido: no
    SOSTENGO       delegar_tarea_base_comun_seguimiento               (bandeja) > supervisar_decision_delegada_preguntas_concretas       (bandeja) | levantado por el barrido: no
    SOSTENGO, DUDA transmitir_objetivos_prioridades_preferencias      (bandeja) > delegar_tarea_base_comun_seguimiento                   (bandeja) | levantado por el barrido: no
    SOSTENGO       identificar_paso_limitante_jornada_desfases        (bandeja) > usar_calendario_herramienta_planificacion_produccion   (bandeja) | levantado por el barrido: no
    SOSTENGO       agrupar_tareas_semejantes_aprovechar_preparacion   (bandeja) > agrupar_interrupciones_subordinados_reuniones_regulares (bandeja) | levantado por el barrido: no
    SOSTENGO       buscar_regularidad_bloques_iguales_trabajo_mando   (bandeja) > canalizar_interrupciones_cartel_hora_oficina           (bandeja) | levantado por el barrido: no
    SOSTENGO, DUDA buscar_actividad_alta_palanca_tres_vias            (bandeja) > detectar_palanca_negativa_actividad_mando              (bandeja) | levantado por el barrido: no
    SOSTENGO, DUDA representar_actividad_caja_negra_ventanas          (grafo) > buscar_regularidad_bloques_iguales_trabajo_mando       (bandeja) | levantado por el barrido: no
    NO             elegir_fabricar_pedido_pronostico                  (grafo) > usar_calendario_herramienta_planificacion_produccion   (bandeja) | levantado por el barrido: no
    NO             subir_productividad_gerencial_tres_vias            (bandeja) > identificar_paso_limitante_jornada_desfases            (bandeja) | levantado por el barrido: no
    NO             reunir_informacion_gerencial_vias_variadas         (bandeja) > programar_visita_area_observar_despachar               (bandeja) | levantado por el barrido: SI
    filas: 13 | SOSTENGO: 10 | NO: 3 | levantadas por el barrido: 1

**LECTURA:**

- **`d072`: SOSTENGO.** `construir_flujo_produccion_paso_limitante` (grafo) madre de
  `identificar_paso_limitante_jornada_desfases`, madre pasos `5` y `9`, hijo pasos `2` y `4`, L267 (*what is the
  "egg" in our work?* y *create offsets*). El hijo trae criterio propio para elegir el paso limitante (su paso
  `3`: lo que tiene calendario absoluto, no lo que mas tarda), asi que es continuacion y no repeticion. **Mi barrido
  mide un solo lado, el del candidato: `identificar` no levanta a `construir_flujo`**. El otro lado, con
  `construir_flujo` de candidato, no lo mido, porque ya vive en el grafo; la deuda dice que tampoco lo levanta, y
  eso no lo he comprobado yo (`.v66aud/pasos_d072.txt`).
- **La arista EN COLA de la `65`, `detectar_arreglar` a `supervisar_tarea`: NO va aqui**, porque el barrido de
  `supervisar_tarea` la levanta (seccion `5`); va en sus veredictos como `CONTINUA` con `madre=` (seccion `6`).
- **Mis cuatro `SOSTENGO, DUDA`**, dichas antes de saber: `variar_frecuencia_inspeccion_nivel_calidad`, **la fila
  `21` que acaba de entrar**, madre de `supervisar_tarea` (L253, *a variable approach*: la misma figura que
  `detectar`, con la duda de que el hijo mueve la frecuencia por la madurez y no por la calidad);
  `transmitir_objetivos` madre de `delegar` (L159 dice *key to successful delegation*, y L245 no remite a L159 con
  palabras); `buscar_actividad` madre de `detectar_palanca` (**descansa en el paso `1` que marco `D` en la
  fidelidad**); y `representar_actividad_caja_negra_ventanas` (grafo) madre de `buscar_regularidad` (L305,
  *cutting windows into the black box*, que puede leerse como nombrar sin procedimentar).
- **Tres que NO sostengo**, para que se vea el criterio: el contraste taller contra fabrica de
  `usar_calendario` no usa la decision de `elegir_fabricar_pedido_pronostico`; los principios de produccion de
  L267 a L291 no presuponen la decision de `subir_productividad` en ninguna condicion, y no declaro ese abanico;
  y `programar_visita` es otra via, hermana de `reunir`, no su hija.

**`D.37`, LOS TITULOS QUE DICEN CUANTAS PARTES TIENEN:** dos, y los dos dicen cuantas **y** las nombran:
`subir_productividad_gerencial_tres_vias` (el ritmo, la palanca y la mezcla) y
`buscar_actividad_alta_palanca_tres_vias` (mucha gente, un acto breve de efecto largo, el saber unico).

    $ cat .v66aud/d37_partes.txt
    poblacion: 479
    ritmo 1
        gerber_emyth             dictar_ritmo_crecimiento_preguntas_escritas
    mezcla 0
    acelerar 0
    palanca 3
        grove_high_output        buscar_actividad_alta_palanca_tres_vias
        grove_high_output        detectar_palanca_negativa_actividad_mando
        grove_high_output        elegir_momento_actividad_palanca_maxima
    saber_unico 0

**LECTURA: ninguna de las seis partes existe como nodo**: el unico `ritmo` es de Gerber y es otra cosa (el ritmo
del crecimiento), y los tres `palanca` son los propios candidatos de `cap_04`, ninguno de los cuales **es** una de
las partes. **`D.37` no dispara**, y la relacion de `subir` con `buscar` va por `D.29` como `CONTINUA` (seccion `6`).

**Y DOS PARA CUANDO ENTREN SUS HIJOS, no para esta tanda:** `elegir_momento_actividad_palanca_maxima` paso `5`
nombra el caso del subordinado valioso que se va, que la bandeja de Grove tiene en
`responder_primer_aviso_renuncia_subordinado`; y `supervisar_tarea_delegada_etapa_menor_valor` paso `6` nombra la
madurez relativa a la tarea que `fijar_frecuencia_reunion_individual_madurez_tarea` (`cap_05`) procedimenta.
**Me inclino a SANO sin arista en las dos, porque nombrar no es procedimentar**, y las dejo escritas aqui porque
ninguno de los dos pares lo levanta el barrido de `cap_04`.

## 8. **EL ORDEN QUE MI LECTURA OBLIGA** (`D.36`)

**No es un orden: son las restricciones**, escritas antes de ver el del extractor. Madre antes que hijo por mis
`CONTINUA` y mis `SOSTENGO` con los dos extremos en la bandeja, y cuantas cumple el orden de pieza del libro:

    $ python .v66aud/restricciones_orden.py
    restricciones: 12
      reunir_informacion_gerencial_vias_variadas           antes que escalonar_fuentes_informacion_gerencial                  CONTINUA               el orden del libro la cumple
      subir_productividad_gerencial_tres_vias              antes que buscar_actividad_alta_palanca_tres_vias                  CONTINUA               el orden del libro la cumple
      buscar_actividad_alta_palanca_tres_vias              antes que elegir_momento_actividad_palanca_maxima                  CONTINUA               el orden del libro la cumple
      usar_calendario_herramienta_planificacion_produccion antes que decir_no_trabajo_excede_capacidad                        CONTINUA               EL ORDEN DEL LIBRO LA VIOLA
      delegar_tarea_base_comun_seguimiento                 antes que supervisar_tarea_delegada_etapa_menor_valor              arista por lectura     el orden del libro la cumple
      delegar_tarea_base_comun_seguimiento                 antes que supervisar_decision_delegada_preguntas_concretas         arista por lectura     el orden del libro la cumple
      transmitir_objetivos_prioridades_preferencias        antes que delegar_tarea_base_comun_seguimiento                     arista por lectura     el orden del libro la cumple
      identificar_paso_limitante_jornada_desfases          antes que usar_calendario_herramienta_planificacion_produccion     arista por lectura     el orden del libro la cumple
      agrupar_tareas_semejantes_aprovechar_preparacion     antes que agrupar_interrupciones_subordinados_reuniones_regulares  arista por lectura     el orden del libro la cumple
      buscar_regularidad_bloques_iguales_trabajo_mando     antes que canalizar_interrupciones_cartel_hora_oficina             arista por lectura     el orden del libro la cumple
      buscar_actividad_alta_palanca_tres_vias              antes que detectar_palanca_negativa_actividad_mando                arista por lectura     el orden del libro la cumple
      preparar_respuestas_estandar_interrupciones_repetidas antes que llevar_inventario_proyectos_discrecionales               D.36, solo lo levanta llevar_inventario_proyectos_discrecionales EL ORDEN DEL LIBRO LA VIOLA
    que obligan (madre antes que hijo): 11 | violadas por el orden del libro: 1
    D.36 de un solo lado, informativas: 1
    ultimas dos del orden del libro: ['agrupar_interrupciones_subordinados_reuniones_regulares', 'canalizar_interrupciones_cartel_hora_oficina']

**LECTURA:** el orden de pieza solo viola una, **`usar_calendario` tiene que entrar antes que `decir_no`**, porque
los dos son de la pieza `P34` y el volcado de `cola_grove.py`, que desempata por id, pone `decir_no` primero. La fila `D.36` de un solo lado **no obliga**: la
aduana de `insertar` mide grafo mas bandejas (`D.38.5`), asi que el par `llevar_inventario` con
`preparar_respuestas` se lee entre en el orden que entre. **Con el tope en `20`, las dos ultimas del orden de
pieza, `agrupar_interrupciones` y `canalizar_interrupciones`, son hijas cuyas madres (`agrupar_tareas`,
`buscar_regularidad`) entran antes**, asi que dejarlas para la `68` no deja ningun hijo dentro con su madre fuera.
Eso lo compruebo contra el orden que el extractor haya escrito, en mi turno normal.

## 9. **LO QUE DEJO PARA MI TURNO NORMAL, ESCRITO ANTES DE VER EL REPORTE**

1. **`R5`** en su reporte, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` sacados otra vez de los
   originales y con la cabecera cambiada a la `66`.
2. **Mi fidelidad contra la suya, paso a paso**: `156` filas mias contra las suyas. Si mis cuatro `D` se
   quedan en `T`, la cifra de `cap_04` sigue en `0`; si alguna cae a PUENTE, cae dentro de lo que marque aqui;
   **y si el marca PUENTE un paso que yo lei `T` sin duda, y gana, la caida de lectura es mia.**
3. **Mis `53` clases contra sus lineas de veredicto**, y mis `10` `SOSTENGO` contra sus aristas por lectura
   (**el asunto de `15d51d8` dice `9`**: lo miro por par y no por cuenta).
4. **La linea `CONTINUA` de `detectar_arreglar` a `supervisar_tarea`** en sus veredictos y no en sus aristas.
5. **Su orden contra mis `11` restricciones**, y las dos que pasan a la `68`.
6. **La linea nueva de la bitacora** (`796` contra `795`) contra el bloque de la fila `22` de
   `.v64ext/veredictos_listos.txt`, letra a letra.
7. **La muestra pineada de los SANO**, si la `66` escribio alguno en la bitacora, con semilla `66`.

**Y UNA COSA DEL ARNES QUE VI EN ESTA FASE, sin arreglarla** (`D.45`): corri el tallador estricto sobre esta
pagina antes de cerrarla, para no repetir `d167`. **No encuentra ninguna tabla que declare instrumento**, que es
lo que buscaba; y despues se cae, porque `cifras_derivadas_sueltas` abre `docs/loop/REPORTE.md` sin mirar si
esta, y en esta fase no esta. Salida entera en `.v66aud/tallado_apertura.txt`:

    $ grep -E "^TALLADO|^tablas que declaran|Error" .v66aud/tallado_apertura.txt
    TALLADO DEL REPORTE (D.41): la tabla que dice ser de instrumento
    tablas que declaran instrumento : 0
    TALLADO VERDE: las 0 tabla(s) comprobables son las de su instrumento, celda a celda.
    FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\AlexDesk\\Documents\\forja-nodos\\docs\\loop\\REPORTE.md'

**LECTURA:** no toca a esta pagina ni al cierre del extractor, que corre con el reporte en el arbol; solo al que
corra el tallador en una fase ciega. Lo anoto en mi acta como deuda, no aqui.
