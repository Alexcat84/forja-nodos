
## G7.3. TAREA 2: `cap_18`, LA FRONTERA PUBLICADA ANTES DE CORTAR, Y TRES CANDIDATOS

### G7.3.a. El borde de arriba, comparado contra `wc -l` (`d109`, la caida que la `ACTA G5` cargo)

    $ wc -l fuentes/gerber_emyth/cap_18.md
    413 fuentes/gerber_emyth/cap_18.md

**`413` lineas, al digito con las `413` que el encargo cuenta en su cabecera.** La frontera de abajo
cierra tambien en `L413`: no hay borde de arriba que la guarda no vea (`d109` sigue en pie como
moratoria de maquinaria, pero esta vuelta lo comprueba a mano igual que la `6`).

### G7.3.b. La frontera, publicada antes de cortar

Salida de `python .gerber_v5/frontera.py fuentes/gerber_emyth/cap_18.md .gerber_v7/piezas_cap18.txt`,
guardada en `.gerber_v7/frontera_cap18.txt`:

<!-- TALLADO: salida=.gerber_v7/frontera_cap18.txt -->

    AVISO: cero celdas tecleadas en este instrumento. El arranque del cuerpo NO
    es una constante mia: sale de fuentes/gerber_emyth/cap_18.md, linea 8, que es la siguiente al segundo
    --- de la cabecera yaml (cierres en L1 y L7). El cuerpo va de L8 a L413.

    | pieza | lineas | palabras | que es | clase |
    |---|---|---:|---|---|
    | `R1` | L8 a L20 | **18** | el numero del capitulo, el rotulo YOUR PEOPLE STRATEGY y el epigrafe de Robert S. DeRopp (Life games reflect life aims) | **RESIDUO: rotulo y epigrafe** |
    | `R2` | L21 a L102 | **1432** | la escena del hotel Venetia continuada literalmente desde donde cap_17 se corto en L221 | **CASO: continuacion de la escena de cap_17** |
    | `R3` | L103 a L116 | **187** | la reflexion del autor que generaliza lo que el Manager conto | **POSTURA** |
    | `C1` | L117 a L120 | **51** | Your People Strategy con sus cuatro componentes | **CANDIDATO: construir_estrategia_gente_cuatro_componentes** |
    | `R4` | L121 a L136 | **189** | el juego tiene que vivirse, no solo escribirse | **POSTURA** |
    | `C2` | L137 a L166 | **787** | The Rules of the Game: ocho reglas numeradas | **CANDIDATO: aplicar_ocho_reglas_juego_personas** |
    | `R5` | L167 a L228 | **477** | The Logic of the Game: proposito y comunidad | **POSTURA** |
    | `R6` | L229 a L246 | **188** | Playing the Game: el mapa mental y el medio de comunicacion | **POSTURA: bridge** |
    | `C3` | L247 a L272 | **266** | el proceso de contratacion en cinco componentes | **CANDIDATO: aplicar_cinco_pasos_proceso_contratacion** |
    | `R7` | L273 a L288 | **123** | preguntas retoricas de cierre y regreso a Sarah | **POSTURA** |
    | `R8` | L289 a L413 | **1678** | dialogo con Sarah, delegacion, y la Hierarchy of Systems de cuatro componentes sin desarrollo propio | **CASO: dialogo con Sarah, discutible 2** |
    | **el cuerpo entero** | **L8 a L413** | **5396** | **suma de las piezas: 5396** | **residuo sin asignar: 0** |

    piezas: 11   lineas solapadas: 0   lineas sin cubrir: 0   cuerpo 5396   suma 5396   residuo 0

**`5396` PALABRAS, AL DIGITO CON LAS `5396` QUE EL ENCARGO CUENTA EN SU CABECERA. `11` PIEZAS, `0`
SOLAPES, `0` LINEAS SIN CUBRIR, RESIDUO `0`.** El fichero de piezas completo, con su razon una a una,
queda en `.gerber_v7/piezas_cap18.txt` (contenido identico al tallado de arriba, D.42).

### G7.3.c. Los tres candidatos, cada uno con su aduana en el acto

**`C1`, `construir_estrategia_gente_cuatro_componentes`** (`L117` a `L120`, `5` pasos): es el candidato que
paga `d110` (`G7.2`), el que nace en `cap_18` y no en `cap_17`. Informe corrido en el acto. Salida de
`python forja.py informe cuarentena/gerber_emyth/construir_estrategia_gente_cuatro_componentes.json`,
guardada en `.gerber_v7/informe_C1.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/informe_C1.txt -->

    ENTRARIAN sin leer nada          : 0
    BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [BLOQUEARIA] construir_estrategia_gente_cuatro_componentes
        vecino recorrer_siete_pasos_programa_desarrollo_negocio  [levantada por: paso_contra_nodo]
          similitud_texto 0.238 | familia_id 0.000 | paso_contra_nodo 0.698
          paso 3 del candidato contra paso 5 de recorrer_siete_pasos_programa_desarrollo_negocio

**`0 CAERIA`. El unico vecino, leido:** mi paso `3` (*sigue con tu Strategic Objective*, un componente
DENTRO de Your People Strategy) contra el paso `5` de la cabeza de serie (*Paso 5: Your People Strategy*,
el nombre del paso completo de la serie de siete). Parecido lexico de frases cortas *Your X*, no
conceptual: uno es un componente interno, el otro es el nombre del paso entero de otra serie.
**VEREDICTO DE LECTURA: `SANO`.** No se escribe en `bitacora/VEREDICTOS.jsonl` porque esta vuelta no
inserta (`D.39`).

**`C2`, `aplicar_ocho_reglas_juego_personas`** (`L137` a `L166`, `9` pasos). Informe corrido en el acto.
Salida guardada en `.gerber_v7/informe_C2.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/informe_C2.txt -->

    ENTRARIAN sin leer nada          : 1
    BLOQUEARIAN esperando veredicto  : 0
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [ENTRARIA] aplicar_ocho_reglas_juego_personas

**`0 CAERIA`, cero vecinos que leer.**

**`C3`, `aplicar_cinco_pasos_proceso_contratacion`** (`L247` a `L272`, `12` pasos). Informe corrido en el
acto. Salida guardada en `.gerber_v7/informe_C3.txt`:

<!-- TALLADO: parcial salida=.gerber_v7/informe_C3.txt -->

    ENTRARIAN sin leer nada          : 0
    BLOQUEARIAN esperando veredicto  : 1
    CAERIAN por una guarda           : 0
    CHOCAN entre si dentro del lote  : 0

    [BLOQUEARIA] aplicar_cinco_pasos_proceso_contratacion
        vecino construir_estrategia_gente_cuatro_componentes  [levantada por: similitud_texto]
          similitud_texto 0.375 | familia_id 0.000 | paso_contra_nodo 0.532
          paso 11 del candidato contra paso 4 de construir_estrategia_gente_cuatro_componentes
        vecino fingir_prototipo_cinco_mil_replicas  [levantada por: similitud_texto]
          similitud_texto 0.355 | familia_id 0.111 | paso_contra_nodo 0.512
          paso 10 del candidato contra paso 10 de fingir_prototipo_cinco_mil_replicas

**`0 CAERIA`. Los dos vecinos, leidos**, los dos en la banda `0,35` a `0,4` que la seccion `11` ya avisa
que es ruido: el primero comparte vocabulario del propio libro (*Organizational Strategy*, *Position
Contract*) entre revisar el manual de UN empleado (mi paso) y construir la estrategia entera (el otro
candidato); el segundo comparte solo la palabra *uniforme* entre entregar un uniforme el primer dia y
una regla de codigo de color y vestuario del prototipo entero. **LOS DOS `SANO`.** No se escriben en
`bitacora/VEREDICTOS.jsonl` porque esta vuelta no inserta (`D.39`).

**`cap_18` cierra con TRES candidatos, `0 CAERIA` en las tres aduanas, `26` pasos escritos entre los
tres, `26` TRANSCRIPCION y `0` PUENTE.** Cero inserciones al grafo (`MODO_INSERCION=cuarentena`).

### G7.3.d. Los dos discutibles, marcados antes de saber si acierto (tope `2`, `D.61`)

| # | discutible | como se cierra en esta misma vuelta |
|---:|---|---|
| 1 | `C2` (`aplicar_ocho_reglas_juego_personas`): `cap_18` `L141` dice que trae solo unas pocas reglas a modo de muestra y que las demas hay que descubrirlas por cuenta propia, lo que podria leerse como el adjetivo de adecuacion de la restriccion `2` de `9.1` si eso declara las ocho reglas opcionales | **EJECUTADO, no solo cerrado:** escribo el candidato entero (no lo retiro), leyendo que la frase es sobre si HAY MAS reglas por descubrir, no sobre si estas ocho son opcionales, apoyado en que las ocho traen verbo en imperativo y dos traen medida concreta (regla `5`: al menos una vez por semana; regla `7`: no mas de una vez cada seis meses), y en el precedente ya adjudicado `SANO` de la misma frase tipo en `cap_14` (`ACTA G4` `G4.3.c` discutible `3`). Razon completa en `resumen_teorico` de `C2` |
| 2 | `cap_18` `L373` a `L383` (pieza `R8`): el libro dice que la Hierarchy of Systems tiene cuatro componentes distintos y los nombra uno a uno, un inventario con conteo explicito que podria pedir su propio candidato bajo `D.27`/`D.37` | **CERRADO, no ejecutado:** no escribo candidato. Cada componente queda nombrado en una sola linea, sin desarrollo propio EN ESTE CAPITULO (a diferencia de los siete pasos de `cap_13`, donde cada paso corresponde a un capitulo entero que el libro SI desarrolla en otro sitio, manual seccion `9.1`, fila tres de la tabla SI es un nodo). No hay tabla que se desarrolle en otro sitio conocido de este libro: es una taxonomia nombrada sin instruccion de que hacer con cada nivel, mas cerca de una definicion o un concepto sin nada que hacer (`9`, tabla NO es un nodo) que de una serie numerada. Si el auditor lee lo contrario, la linea queda citada (`cap_18` `L373` a `L383`) para que la relectura ciega la encuentre primero |

**`D.61` REPASADA: DOS DISCUTIBLES, LOS DOS CERRADOS EN ESTA MISMA VUELTA CON SU MOTIVO Y SU LINEA. `0`
ABIERTOS, POR DEBAJO DEL TOPE DE `2`.**
