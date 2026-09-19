# APERTURA CIEGA DE LA VUELTA 47, lote 7 (`grove_high_output`), `cap_04`

**Fase ciega del auditor.** No he abierto `docs/loop/REPORTE.md`, ni
`ultimo_extractor.json`, ni `ultimo_auditor.json`, ni `CREDITO_serial.jsonl`, ni los he
sacado de `git`. Lo que sigue es MI lectura del material, hecha contra el libro y contra
el arbol, para poder compararla despues con la del extractor.

**LA LINEA DE LECTURA QUE EL ARNES EXIGE, ANTES QUE NADA:**

    ACTA ANTERIOR LEIDA: d0255b4e685a777102c0c116f69dab7d23af2db2

Y la compruebo en vez de copiarla del prompt:

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    d0255b4e685a777102c0c116f69dab7d23af2db2

## 0. LA HERENCIA (`D.40`), Y UNA DISCREPANCIA QUE DECLARO EN VEZ DE CALLARME

El arnes me entrega **`heredados: 0`**, y lo pego:

    $ python forja.py herencia
      acta anterior : ACTA 45. VUELTA 46, lote 7 (`grove_high_output`), `cap_04`: ...
      su huella     : d0255b4e685a777102c0c116f69dab7d23af2db2
      heredados     : 0

    AVISO: esta acta MENCIONA remedios en 2 encabezado(s) y no ESCRIBE ninguna tabla de
    remedios fuera de cita. No se entrega ninguno, y se dice en voz alta: un arnes que
    entrega cero sin avisar es el defecto que la TAREA 2 de la vuelta 31 vino a cerrar.

**PERO MI ACTA ANTERIOR SI ME ESCRIBIO UN REMEDIO, Y LO LEI PORQUE EL PROTOCOLO ME
AUTORIZA A LEER MI PROPIA ACTA EN ESTA FASE.** Esta en `ACTA_AUDITOR.md` `45.9.b`:

> **`REMEDIO DEL AUDITOR, VUELTA 47`: todo barrido que corra en mi fase ciega escribe su
> guion y su salida en `.v47aud/`, los dos dentro del arbol, y TODA cifra de distancia que
> publique se lee de esa salida pegada. NINGUN SUPERLATIVO MIO (*el mas alto*, *el mas
> proximo*) se publica si la salida pegada no ensena la lista ordenada que lo sostiene.**

    HEREDADO 1: CUMPLIDO

**POR QUE EL ARNES ENTREGO CERO, MEDIDO Y NO SUPUESTO.** `src/herencia.py` entrega las
FILAS de una tabla markdown cuya cabecera nombre `REMEDIO` **y que este FUERA DE CITA**,
y lo dice en su propia linea `174`: *una tabla copiada dentro de un bloque de cita se esta
CITANDO, y citar es justo lo que no se entrega*. Mi `45.9.b` escribio el remedio **como
parrafo dentro de un bloque `>`**, que es exactamente la forma que el instrumento no puede
llevar.

`LECTURA`: **la maquina funciono y quien escribio mal fui yo.** El aviso de `D.40` salto,
dijo en voz alta que habia menciones y ninguna tabla, y la red que me salvo fue la otra:
**leer mi propia acta en la fase ciega**, que es lo que `AUDITOR_FORJA.md` autoriza por
escrito tras la racha de las actas `14`, `15` y `16`. **Sin esa segunda red habria perdido
mi propio remedio por la forma del parrafo.** Es caida mia y la llevo al acta.

## 1. LO QUE EL ARNES RETIRO, COMPROBADO EN EL LOG Y NO AFIRMADO DE MEMORIA

    $ tail -n 1 docs/loop/loop.log
    [2026-09-19 05:35:01] VUELTA 3 : APERTURA CIEGA (claude-opus-5), retirados:
    REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl

    $ git status --short
     D docs/loop/APERTURA_CIEGA.md
     D docs/loop/CREDITO_serial.jsonl
     D docs/loop/REPORTE.md
     M docs/loop/loop.log
     M docs/loop/ultimo_apertura.json
     D docs/loop/ultimo_auditor.json
     D docs/loop/ultimo_extractor.json

**`loop.log` NO esta retirado en esta corrida y por eso lo abro.** La numeracion del log
es la de la corrida del arnes (`VUELTA 3`); la del repo es `VUELTA 47`, la que auditare.

## 2. MI REMEDIO, CUMPLIDO Y COMPROBABLE ABRIENDO UN DIRECTORIO

Todo lo que mido aqui tiene su guion y su salida en `.v47aud/`, dentro del arbol. Los
guiones son mios y estan escritos en esta fase; las salidas son las que pego.

## 3. EL MATERIAL DE ESTA VUELTA, MEDIDO Y NO CONTADO A OJO

**Que candidatos NACEN en esta vuelta**, contra el commit de apertura del arnes:

    $ git log --diff-filter=A --name-only --format='' 327d969..HEAD -- cuarentena/ | sort -u
    cuarentena/grove_high_output/agrupar_tareas_semejantes_aprovechar_preparacion.json
    cuarentena/grove_high_output/delegar_tarea_base_comun_seguimiento.json
    cuarentena/grove_high_output/detectar_palanca_negativa_actividad_mando.json
    cuarentena/grove_high_output/identificar_paso_limitante_jornada_desfases.json
    cuarentena/grove_high_output/supervisar_decision_delegada_preguntas_concretas.json
    cuarentena/grove_high_output/supervisar_tarea_delegada_etapa_menor_valor.json

**Cuantos pasos trae cada uno**, contados por mi con la clave buena
(`pasos_accionables`, y digo que mi primer contador pregunto por `pasos`, que no existe,
y devolvio seis ceros):

    $ python .v47aud/05_pasos.py
      6  agrupar_tareas_semejantes_aprovechar_preparacion
     10  delegar_tarea_base_comun_seguimiento
      9  detectar_palanca_negativa_actividad_mando
      5  identificar_paso_limitante_jornada_desfases
      6  supervisar_decision_delegada_preguntas_concretas
      9  supervisar_tarea_delegada_etapa_menor_valor
    ---
     45  TOTAL de 6 candidatos

**Lo que esta vuelta NO movio**, que es la otra mitad de la medida:

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl

    $ git log --diff-filter=M --name-only --format='' 327d969..HEAD -- dataset/ bitacora/ config/ censos/
    (ninguna linea)

`LECTURA`: **esta vuelta no inserto ni un nodo y no escribio ni un veredicto.** `346` y
`740` son los mismos numeros con los que mi `ACTA 45` cerro la vuelta `46`. El unico
fichero de cuarentena MODIFICADO y no nacido es
`transmitir_objetivos_prioridades_preferencias.json`, de la vuelta anterior.

## 4. MI RELECTURA DE FIDELIDAD (`D.30`): LOS `45` PASOS CONTRA EL LIBRO

**Lei el capitulo entero** (`fuentes/grove_high_output/cap_04.md`, `323` lineas, unidad
`Cap. 3`, *Managerial Leverage*) **antes de abrir ninguna ficha**, y despues case cada
paso con el renglon que la ficha dice. Los renglones los saque con mi propio guion
(`.v47aud/07_renglon.sh`), no de la ficha.

| candidato | pasos | renglones que dice | los case | mi veredicto |
|---|---|---|---|---|
| `detectar_palanca_negativa_actividad_mando` | `9` | `L219`, `L231`, `L233`, `L235` | `9` de `9` | `9` TRANSCRIPCION, `0` PUENTE |
| `delegar_tarea_base_comun_seguimiento` | `10` | `L245`, `L247`, `L249` | `10` de `10` | `10` TRANSCRIPCION, `0` PUENTE |
| `supervisar_tarea_delegada_etapa_menor_valor` | `9` | `L253`, `L255` | `9` de `9` | `9` TRANSCRIPCION, `0` PUENTE |
| `supervisar_decision_delegada_preguntas_concretas` | `6` | `L257` | `6` de `6` | `6` TRANSCRIPCION, `0` PUENTE |
| `identificar_paso_limitante_jornada_desfases` | `5` | `L267` | `5` de `5` | `5` TRANSCRIPCION, `0` PUENTE |
| `agrupar_tareas_semejantes_aprovechar_preparacion` | `6` | `L269`, `L271` | `6` de `6` | `6` TRANSCRIPCION, `0` PUENTE |
| **TOTAL** | **`45`** | | **`45`** | **`45` TRANSCRIPCION, `0` PUENTE** |

**FIRMO EL `0` PUENTE DE `cap_04` EN ESTA VUELTA**, y lo firmo habiendo leido los `45`
uno a uno, no por muestra.

**LAS TRES CONTENCIONES QUE MIRE UNA A UNA, PORQUE SON DONDE UN PUENTE SE COLARIA:**

1. **El periodo que el libro no da.** `L253` manda frecuencia *variable* y da su criterio
   (*his experience with a specific task and his prior performance with it*) **y ninguna
   cifra**. Los pasos `4` y `5` de `supervisar_tarea_delegada_etapa_menor_valor` dicen
   *sube o baja* y **no dicen cada cuanto**. No hay periodo inventado.
2. **La lista que el libro no enumera.** `L257` dice *quite specific questions* y no las
   escribe. El paso `4` de `supervisar_decision_delegada_preguntas_concretas` dice
   *preguntas bastante concretas* y **no despliega ninguna lista**.
3. **El renglon extraido dos veces.** `L249` contiene *Monitoring is not meddling*.
   Lo lleva **solo** `delegar_tarea_base_comun_seguimiento` en su paso `8`;
   `detectar_palanca_negativa_actividad_mando` declara por escrito que **no** se lo lleva,
   **y comprobe que en efecto no esta en ninguno de sus `9` pasos.**

**Y LO MEDI ADEMAS A MAQUINA, AL NIVEL DEL PASO**, que es donde un gemelo se ve aunque los
titulos difieran:

    $ python .v47aud/22_pasos_repetidos.py
    pasos comparados: 95 (de los 14 candidatos de cap_04)
      de ellos, nacidos en esta vuelta: 45

    LOS 12 PARES DE PASOS MAS PARECIDOS, LISTA ORDENADA ENTERA:
      0.3333  delegar_tarea_base_comun_seguimiento#1  <->  subir_productividad_gerencial_tres_vias#1
      0.3182  detectar_palanca_negativa_actividad_mando#1  <->  elegir_momento_actividad_palanca_maxima#1
      0.3030  agrupar_tareas_semejantes_aprovechar_prepara#2  <->  delegar_tarea_base_comun_seguimiento#1
      0.3000  delegar_tarea_base_comun_seguimiento#1  <->  transmitir_objetivos_prioridades_preferencia#5
      0.2683  buscar_actividad_alta_palanca_tres_vias#3  <->  delegar_tarea_base_comun_seguimiento#1
      0.2667  subir_productividad_gerencial_tres_vias#1  <->  supervisar_tarea_delegada_etapa_menor_valor#1
      0.2609  detectar_palanca_negativa_actividad_mando#1  <->  subir_productividad_gerencial_tres_vias#3
      0.2581  delegar_tarea_base_comun_seguimiento#1  <->  supervisar_tarea_delegada_etapa_menor_valor#7
      0.2500  delegar_tarea_base_comun_seguimiento#8  <->  elegir_momento_actividad_palanca_maxima#1
      0.2439  delegar_tarea_base_comun_seguimiento#8  <->  programar_visita_area_observar_despachar#6
      0.2381  delegar_tarea_base_comun_seguimiento#1  <->  detectar_palanca_negativa_actividad_mando#8
      0.2368  delegar_tarea_base_comun_seguimiento#1  <->  detectar_palanca_negativa_actividad_mando#4

    pares con solape 1.0 (paso identico): 0

`LECTURA`: **ningun paso se repite entre los `14` candidatos de `cap_04`.** El par mas
alto es `0,3333` y son dos aperturas del tipo *Cuenta con que...*, o sea **forma de
redaccion y no material del libro**: los dos renglones de origen son distintos y los lei.
El solape maximo que mide este instrumento es **de estilo, no de contenido**.

## 5. LA POBLACION DEL BARRIDO (`D.38.4`), CON LA ADJUDICACION DE MI ACTA ANTERIOR PUESTA

Mi primer contador dio la cifra ancha, la misma que mi `ACTA 45` ya adjudico como mala:

    $ python .v47aud/08_poblacion.py
    POBLACION DEL BARRIDO (grafo + bandejas):  548

**Y ESA ES LA CIFRA EQUIVOCADA, Y LO SE PORQUE ME LO DEJE ESCRITO.** `ACTA 45` `45.5.a`
adjudico que los `163` de `cuarentena/ensayo_referencia_163/` **no son poblacion**: su
clave no esta en la tabla canonica y `src/aduana.py:465` los descarta, *un ensayo no es un
libro*. Aplico el mismo filtro que la aduana:

    $ python .v47aud/09_poblacion_buena.py
    grafo                                :  346
    bandeja ensayo_referencia_163     :    0 cuentan,  163 fuera de la tabla canonica
    bandeja grove_high_output         :   36 cuentan,    0 fuera de la tabla canonica
    bandeja marquet_turn_the_ship     :    3 cuentan,    0 fuera de la tabla canonica
    --------------------------------------------------------------
    POBLACION DEL BARRIDO, la buena      :  385

**`385` es mi poblacion de esta vuelta: `346` de grafo mas `39` de bandejas.** Es la
primera vez que esta cifra sale ya corregida de mi propia fase ciega, y sale asi **porque
la adjudicacion estaba escrita en mi acta y la lei**.

## 6. LAS ARISTAS QUE LAS FICHAS DECLARAN: UNA APUNTA A UN NODO QUE NO EXISTE

    $ python .v47aud/14_aristas_citadas.py
    === identificar_paso_limitante_jornada_desfases
        bandeja/grove_high_output subir_productividad_gerencial_tres_vias
        bandeja/grove_high_output agrupar_tareas_semejantes_aprovechar_preparacion
        NO EXISTE    usar_calendario_herramienta_planificacion_produccion
        bandeja/grove_high_output construir_flujo_produccion_paso_limitante
    ---
    aristas declaradas hacia un id que NO existe en ninguna sede: 1

Y no existe bajo otro nombre, que es lo que hay que comprobar antes de decirlo
(`AUDITOR_FORJA.md` 1.1: una busqueda negativa no se puede citar):

    $ python .v47aud/15_calendario.py
    buscado en 548 nodos (grafo + TODAS las bandejas, sin filtro)
      calendar               -> [('grafo', 'auditar_calendario_reuniones_semana'),
                                 ('grafo', 'reservar_calendario_tiempo_ejecutar'),
                                 ('grafo', 'bloquear_tiempo_pensar_calendario'),
                                 ('grafo', 'pelear_proliferacion_reuniones_bloquear_ejecucion'),
                                 ('grafo', 'agendar_cuidados_propios_cumplirlos')]
      slack                  -> CERO
      inventario_proyectos   -> CERO

`LECTURA`: los cinco de `calendario` del grafo son **de otro libro** y tratan de reuniones,
no del calendario como herramienta de planificacion de `L275` a `L283`. **La arista de
`identificar_paso_limitante_jornada_desfases` apunta a un nodo que todavia no esta escrito
en ninguna sede.**

**NO LA LLAMO CAIDA, Y DIGO POR QUE.** Esta casa ya declara aristas hacia nodos futuros:
`buscar_actividad_alta_palanca_tres_vias` se declaro madre *del que sale de `L231` a
`L235`* cuando ese nodo no existia, y hoy existe y es
`detectar_palanca_negativa_actividad_mando`. **La diferencia que si marco** es que aquella
se declaro **por su tramo** (*el nodo de `L231` a `L235`*) y esta se declara **por un id
inventado de antemano**. Un id que nadie ha escrito puede no coincidir con el que se
escriba, **y entonces la arista queda colgada sin que ninguna guarda lo cante**. Lo llevo
al turno normal como cuestion a adjudicar, no como caida.

## 7. LO QUE DESENTIERRO: EL BANCO DE PRUEBAS NO PUEDE ESTAR VERDE EN MI FASE CIEGA

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python tests/test_aceptacion.py
      total: 318 pruebas, 3 fallos, 1 errores

**`318` pruebas, `3` fallos y `1` error.** Mi `ACTA 45` corrio `318` con `0` y `0`.
**Los cuatro rojos son de la retirada del propio arnes, y lo PRUEBO en vez de suponerlo:**

    ERROR test_el_reporte_vivo_pasa_su_propia_guarda
      FileNotFoundError: docs/loop/REPORTE.md              <- fichero retirado
    FAIL  test_la_linea_serial_del_repo_tiene_su_registro_escrito
      docs/loop/CREDITO_serial.jsonl sin tandas            <- fichero retirado
    FAIL  test_caso_positivo_un_frente_recien_nacido_hereda_cero
    FAIL  test_el_aviso_nombra_la_linea_y_su_registro

Los dos ultimos no nombran ningun fichero retirado, asi que los mido:

    $ python .v47aud/13_causa_rojos.py
    === ANTES: como esta el arbol AHORA, en mi fase ciega ===
    credito.lineas_con_registro() : []
    credito.nacida(LINEA_SERIAL)  : False

    === DESPUES: con un registro de JUGUETE escrito por mi ===
    credito.lineas_con_registro() : ['serial']
    credito.nacida(LINEA_SERIAL)  : True
    items para una linea RECIEN NACIDA : 0 (el banco espera 0)
    avisos dicen RECIEN NACIDA         : True
    el aviso nombra la linea           : True

**NO RECUPERE NADA:** fabrique una tanda de juguete en un directorio temporal y apunte
`credito.DIR_LOOP` ahi, que es lo que hace el propio banco en su prueba de la linea `4739`.
No abri `CREDITO_serial.jsonl` ni lo saque de `git`.

`LECTURA`: al retirar `CREDITO_serial.jsonl`, `credito.lineas_con_registro()` devuelve
vacio; entonces `herencia` entra en su rama *en este arbol el credito no se usa* y deja de
distinguir una linea recien nacida, **que es justo lo que esas dos pruebas comprueban**.
Con un registro cualquiera delante, las tres vuelven a verde. **Los cuatro rojos son
artefactos de la fase ciega y ninguno es un defecto del arbol.**

**Y LA CONSECUENCIA QUE SI PESA, Y LA DEJO DICHA:** `D.38.3` me manda correr instrumentos
de la casa en esta fase, y **uno de los cuatro que `AUDITOR_FORJA.md` 1.1 nombra no puede
salir verde aqui por construccion**. Un auditor que publique *banco de pruebas en rojo*
sin medir la causa estaria cargandole al extractor una averia del arnes; uno que lo pase
por alto se perderia un rojo de verdad el dia que lo haya. **Lo llevo al turno normal como
cuestion de arnes, no como caida de nadie.**

## 8. LA TRAMPA DEL TABLERO SIGUE VIVA, Y AHORA SE COBRARIA `8` NODOS

Mi `ACTA 45` `45.6` la desenterro. **La vuelvo a medir hoy y no se ha movido:**

    $ python forja.py tablero --puedo grove_high_output
    LINEA 'serial', LIBRO 'grove_high_output': SI
      'grove_high_output' esta COSECHADO y sin dueno: su trabajo ya llego a esta rama, asi
      que se continua desde el capitulo siguiente al ultimo minado (cap_04), citando su
      frontera. D.50.

    $ (docs/loop/TABLERO.jsonl, fila de grove_high_output)
      "capitulos_minados": ["cap_01","cap_02","cap_03","cap_04"],
      "ultimo_capitulo": "cap_04",

Y cuantos de `cap_04` hay minados de verdad, contado por mi de las propias fichas:

    $ python .v47aud/16_cap04.py
    cap_02           7
    cap_03          15
    cap_04          14
    ---
    total bandeja grove_high_output: 36

`LECTURA`: **`14` nodos de `cap_04` minados hoy** (`8` de la vuelta `46` mas los `6` de
esta), contra los **`22`** que mi `ACTA 45` `45.2.a` firmo al recomponer su frontera tramo
a tramo. **Quedan `8`.** El `22` no lo remido hoy y lo digo: **es cifra citada de mi acta
anterior, no de un instrumento corrido en esta fase.** Lo que si mido hoy es el `14`.
**El tablero sigue mandando saltar a `cap_05`, y hacerlo dejaria `8` nodos atras** en vez
de los `14` de la vuelta pasada. La trampa no se ha cerrado: se ha encogido.

## 9. QUE QUEDA SIN MINAR EN `cap_04`, LEIDO EN EL LIBRO

**EL LIMITE DE ESTE INSTRUMENTO, DICHO ANTES QUE SU CONCLUSION.** Mi guion saca los
rangos `L<n> a L<m>` del `resumen_teorico` de cada ficha, **y una ficha nombra rangos por
tres motivos distintos**: porque los extrae, porque declara una arista hacia ellos, o
porque declara que NO se los lleva. Lo comprobe con un caso:
`buscar_actividad_alta_palanca_tres_vias` nombra `L231 a L235` **para declararse madre**
del nodo que saldria de ahi, no porque los extraiga (`.v47aud/21_solape_L231.out`).
**Asi que mi contador atribuye cobertura DE MAS, y por tanto el `26` que sigue es un
suelo, no un techo.** No publico la cifra global de renglones sin citar que el guion
tambien da: esa si estaria inflada por los tramos que la frontera declaro en cero a
proposito.

    $ python .v47aud/20_cola.py
    L273  What makes running a factory different from running a job shop? ...
    L275  What is the medium of a manager's forecast? It is something very simple: his calendar. ...
    L277  Another production principle can be applied here. Because manufacturing people trust ...
    L279  To use your calendar as a production-planning tool, you must accept responsibility for two things:
    L281  1. You should move toward the active use of your calendar, taking the initiative to fill ...
    L283  2. You should say "no" at the outset to work beyond your capacity to handle.
    L285  It is important to say "no" earlier rather than later ...
    L287  The next production principle you can apply is to allow slack ...
    L289  Another production principle is very nearly the opposite. A manager should carry a raw ...
    L291  A final principle. Most production practices follow well-established procedures ...
    L293  Built-In Leverage: How Many Subordinates Should You Have...
    L295  An important component of managerial leverage is the number of subordinates a manager has. ...
    L297  The six to eight rule is right for the classically hierarchical manager ...
    L299  Sometimes a business is organized in a way that makes the ideal fan-out ...
    L301  This arrangement will avoid forcing the plant manager either into on-the-job retirement ...
    L303  Interruptions, The Plague of Managerial Work
    L305  The next important production concept ... is to strive toward regularity. ...
    L307  But because you must coordinate your work with that of other managers ...
    L309  About twenty middle managers at Intel were once asked to be part of an experiment. ...
    L311  The most common problem cited was uncontrolled interruptions ...
    L313  The most frequently proposed solutions were not very practical. ...
    L315  There are better ways. Let's apply a production concept. ...
    L317  Also, if you use the production principle of batching ...
    L319  The use of indicators, especially the bank of indicators kept over time ...
    L321  If the people who interrupt you knew how much they were disturbing you ...
    L323  The point is to impose a pattern on the way a manager copes with problems. ...
    ---
    renglones de cuerpo SIN CITAR de L273 al final: 26

`LECTURA`: **la cola del capitulo, de `L273` al final, no la toca ninguna ficha**, y
leyendo el libro esa cola no es prosa: `L279` a `L283` es **un procedimiento numerado por
el propio autor** (*you must accept responsibility for two things*), y detras vienen la
holgura (`L287`), el inventario de proyectos de materia prima (`L289`), la consistencia
(`L291`), la regla de seis a ocho subordinados (`L295` a `L299`) y **la seccion entera de
las interrupciones** (`L305` a `L323`) con sus remedios nombrados uno a uno: respuestas
estandar, agrupar en reuniones regulares, el banco de indicadores y la hora de puerta
abierta. **Ahi es donde viven los `8` que faltan.**

## 10. MI CLASIFICACION CIEGA, CANDIDATO A CANDIDATO

La vara es la de `AUDITOR_FORJA.md` `6.1`: **el candidato CONTINUA el trabajo del
existente o lo REPITE**, con direccion y sin bascula.

| # | candidato | mi clase | lo que la sostiene |
|---|---|---|---|
| 1 | `detectar_palanca_negativa_actividad_mando` | **CONTINUA**, hijo | su madre `buscar_actividad_alta_palanca_tres_vias` enumera las tres vias de palanca ALTA (`L203` a `L213`); este despliega la palanca NEGATIVA (`L219`, `L231` a `L235`), material que la madre no tiene. **Las dos fichas declaran la misma arista, en los dos sentidos.** |
| 2 | `delegar_tarea_base_comun_seguimiento` | **CONTINUA**, hijo | su madre `transmitir_objetivos_prioridades_preferencias` dice en UNA linea que transmitir objetivos es la llave de la delegacion; este la despliega en `10` pasos de `L245` a `L249`. |
| 3 | `supervisar_tarea_delegada_etapa_menor_valor` | **CONTINUA**, hijo del `2` | el paso `7` del `2` nombra el seguimiento en una linea; este pone sus **tres decisiones** con criterio propio cada una: etapa (`L253`), frecuencia (`L253`) y detalle (`L255`). |
| 4 | `supervisar_decision_delegada_preguntas_concretas` | **CONTINUA**, hermano del `3` | mismo seguimiento, **objeto distinto**: una DECISION delegada (`L257`), no una tarea. El libro los separa en tramos consecutivos. `6.1`: *dos doctrinas legitimas no son duplicado*. |
| 5 | `identificar_paso_limitante_jornada_desfases` | **CONTINUA**, parte de cabeza | `subir_productividad_gerencial_tres_vias` dice cuantas vias hay y las nombra; este es el primer principio de produccion aplicado al tiempo (`L267`). |
| 6 | `agrupar_tareas_semejantes_aprovechar_preparacion` | **CONTINUA**, hermano del `5` | el libro los encadena expresamente (*First, we must identify our limiting step* / *A second production principle*). Material propio: `L269` a `L271`. |

**NINGUNO DE LOS SEIS ES REPITE, Y NINGUNO ES GEMELO DE OTRO DE LOS SEIS.** Lo sostengo
con tres cosas medidas y no con una impresion: **los `45` pasos casan con renglones
distintos del libro** (seccion 4), **cero pasos identicos entre los `14` de `cap_04`**
(seccion 4), y **el barrido de vecinos de la seccion 11**.

**EL PAR QUE MAS MIRE, porque es donde un gemelo se esconderia**, es el `3` contra el `4`.
Los sostengo separados: el `3` responde *donde, cada cuanto y cuanto detalle miro una
TAREA*, y el `4` responde *como apruebo una DECISION sin rehacer la reflexion*. Sus
entregables no se solapan y sus renglones de origen son distintos (`L253` a `L255` contra
`L257`). **Si alguien los funde, pierde la frontera que el propio libro escribio.**

**LOS DISCUTIBLES QUE LAS FICHAS SE MARCAN A SI MISMAS, ANTES DE SABER SI ACIERTAN**, que
son los que la relectura conjunta tiene que abrir primero: `1` (pasos `6` y `9` son
consecuencias, no actos), `2` (paso `1` es razon, no acto), `3` (paso `9` es comparacion),
`4` (**pasos `3`, `4` y `5` salen del caso de Intel, y si caen cae el nodo entero**),
`5` (paso `5` es el resumen que el propio libro hace), `6` (pasos `4` y `5` son los dos
ejemplos del libro). **Son seis, uno por candidato.** El mas caro es el del `4` y lo digo
aqui: **es el unico cuyo marcado se lleva el nodo por delante si cae.**

## 12. LO QUE NO PUEDO COMPROBAR EN ESTA FASE, DICHO COMO LIMITACION Y NO COMO AFIRMACION

`AUDITOR_FORJA.md` 1.1: **una busqueda negativa no se puede citar.** Estas cinco cosas
las dejo escritas como pendientes de mi turno normal, y **no escribo ninguna conclusion
sobre ellas aqui**:

1. **Si el reporte declaro el cierre corto con su cifra** (`EXTRACTOR.md` 12.4, y es caida
   de especie `REPORTE` si cierra en un capitulo y no lo dice). La vuelta cerro en `6`
   candidatos con `8` nodos de `cap_04` sin minar, asi que **la pregunta esta viva**;
   pero la declaracion vive en `REPORTE.md`, que esta retirado. **No afirmo ni que este
   ni que falte.**
2. **Si el reporte desglosa `PASOS INVENTADOS POR CAPITULO`** con su fila y su
   denominador (`AUDITOR_FORJA.md` 8.3). Mi denominador ya lo tengo medido y es `45`;
   el numerador que yo firmo es `0`. **Lo que no puedo ver todavia es si el reporte
   publica la misma fila.**
3. **Los relojes y el coste del turno** (`D.55`, declarar el desglose si el turno pasa de
   `10` USD). El dato vive en `ultimo_extractor.json`, retirado.
4. **Las guardas que el reporte declare mordiendo**, que tengo que volver a morder por
   mutacion (cosecha 7.C). No se cuales declara hasta que lo abra.
5. **La tabla de cierre `D.52` y sus instrumentos declarados.** Su guarda propia es la
   que revienta hoy con `FileNotFoundError` por la retirada, asi que **no la puedo correr
   en esta fase ni verde ni roja**.

**Y UNA MAS, QUE ES MIA Y LA DIGO AQUI PARA QUE NO SE PIERDA:** el `22` de la frontera de
`cap_04` lo cito de mi `ACTA 45` y **no lo he recompuesto hoy**. En mi turno normal lo
recompongo contra el fichero antes de usarlo para nada que decida volumen.
