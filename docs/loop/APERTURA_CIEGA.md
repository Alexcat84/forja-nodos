# APERTURA CIEGA de la vuelta que el arnes rotula `VUELTA 1`, linea `serial`, rama `extraccion-mundo-11`

> **Fase ciega.** Escrita ANTES de ver `docs/loop/REPORTE.md`. Cada cifra de esta
> pagina sale de un instrumento corrido en ESTA fase y lleva su salida literal
> debajo, con la linea del comando empezando por `$` (`D.38.3`). Toda conclusion
> sobre contenido va en linea aparte marcada **`LECTURA`**.

---

## 0. LA DECLARACION QUE EL ARNES EXIGE (`D.40`)

    ACTA ANTERIOR LEIDA: d5f4eb832cb0ffd11ddaf35a5bf406e4e2b5f231

**HEREDADOS: `0`.** No declaro `CUMPLIDO` ni `NO APLICA` de ningun remedio porque
no hay ninguno que declarar, y eso **no lo afirmo de memoria: lo corro**.

    $ python forja.py herencia

    REMEDIOS PENDIENTES QUE HEREDAS
    ...
      acta anterior : ACTA 52. VUELTA 53, lote 7 (`grove_high_output`), `cap_06` y la
                      cabeza de `cap_07` ...
      su huella     : d5f4eb832cb0ffd11ddaf35a5bf406e4e2b5f231
      heredados     : 0

    AVISO: esta acta MENCIONA remedios en 1 encabezado(s) y no ESCRIBE ninguna
    tabla de remedios fuera de cita. No se entrega ninguno, y se dice en voz alta:
    un arnes que entrega cero sin avisar es el defecto que la TAREA 2 de la vuelta
    31 vino a cerrar.

    El acta anterior no dejo ninguna tarea bloqueante ni ningun remedio escrito.
    Aun asi tienes que declarar la linea de lectura.

La huella que el instrumento devuelve es **la misma** que el prompt me entrego, y
por eso la escribo tal cual: `d5f4eb832cb0ffd11ddaf35a5bf406e4e2b5f231`.

**Y LO COMPRUEBO CONTRA MI PROPIA SEDE**, que en esta fase si puedo abrir
(`ACTA_AUDITOR.md` no es ninguno de los cuatro que `D.34.2` retira):

    $ awk '/^# ACTA 52/,0' docs/loop/ACTA_AUDITOR.md | grep -n "BLOQUEANTE\|REMEDIO\|^## "

    7:## 52.0. **HUECO DE ACTA Y HERENCIA, Y VAN ANTES QUE NADA** (`1.0`, `D.40`)
    22:## 52.1. **LO QUE VERIFICO AL DIGITO, CON MIS COMANDOS, SOBRE `33010e6`**
    75:## 52.2. **LAS TRES FRONTERAS, RECOMPUESTAS POR MI Y SIN CORRER SU INSTRUMENTO**
    96:## 52.3. **`PASOS INVENTADOS POR CAPITULO`, UNA FILA POR CAPITULO Y NO UNA MEDIA**
    164:## 52.4. **LA RELECTURA CIEGA: SUS QUINCE DISCUTIBLES MARCADOS** (`5.1`)
    211:## 52.5. **LA ADJUDICACION QUE TRAIGO DE MI FASE CIEGA, Y NO ES CAIDA DE NADIE**
    246:## 52.6. **LA CAIDA DE `REPORTE`, Y SUBE A `3 de 3`: LA MEDIA DEL RELOJ**
    300:## 52.7. **LA CAIDA DE `CIFRA PUBLICADA`: LA CORRELACION DE `d058`**
    341:## 52.8. **`CLASE` Y `DATO MOVIDO`, LIMPIAS, CON SU MOTIVO MEDIDO**
    355:## 52.9. **MI PROPIA TANDA, MEDIDA CONTRA MI PAGINA YA SELLADA**
    383:## 52.10. **EL CREDITO AL CERRAR**
    400:## 52.11. **LA PARADA, Y SE CUMPLEN DOS CONDICIONES, NO UNA**
    446:## 52.12. **LO QUE REGISTRO Y NO ADJUDICO**
    461:## 52.13. **EL COSTE DE MI TURNO**

**`LECTURA`:** ninguna de las catorce secciones de la `ACTA 52` es una tarea
bloqueante ni un remedio dirigido a mi. **Las dos fuentes coinciden en `0`**, y una
de ellas es obra mia: no hay herencia perdida por el camino.

---

## 0.b. LO QUE NO VEO, COMPROBADO EN EL LOG Y NO AFIRMADO DE MEMORIA

    $ tail -n 5 docs/loop/loop.log

    [2026-09-20 12:08:07] VUELTA 1 : EXTRACTOR (claude-opus-5)
    [2026-09-20 13:06:30] extractor listo (USD 20.691080999999993), 3503s, intento 1 de 7
    [2026-09-20 13:06:31] VUELTA 1 : APERTURA CIEGA (claude-opus-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl
    [2026-09-20 13:06:31]   hereda 0 remedio(s) del acta anterior, entregados en el prompt (D.40)
    [2026-09-20 13:06:31]   y solo eso: remedios con su motivo, sin cifras ni conclusiones (D.52)

    $ ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl

    ls: cannot access 'docs/loop/REPORTE.md': No such file or directory
    ls: cannot access 'docs/loop/ultimo_extractor.json': No such file or directory
    ls: cannot access 'docs/loop/ultimo_auditor.json': No such file or directory
    ls: cannot access 'docs/loop/CREDITO_serial.jsonl': No such file or directory

Los cuatro **siguen fuera del arbol al cerrar esta pagina**, que es como tienen que
estar. **No recupere ninguno de `git` ni por ninguna otra via.**

---

## 0.c. LO QUE SI LEI Y ROZA EL BORDE, DICHO POR MI ANTES DE QUE ME LO CACEN

**No es una confesion de cortesia: es lo unico que deja saber cuanto vale la lectura
que viene despues.**

| lo que abri | por que no es ninguno de los cuatro | lo que aun asi me contamino |
|---|---|---|
| `docs/loop/ACTA_AUDITOR.md` | obra mia, y el prompt y `D.40` me mandan leerla | nada: es mi propia sede |
| `docs/loop/DEUDA.jsonl` | `D.55` la hace registro de la linea, y el arnes no la retira | **SI, y es lo serio de esta tabla**: sus lineas `60` a `70` son de la vuelta que vengo a auditar, citan rotulos de su REPORTE (`PP.2.b`, `PP.4`, `LL.5.c`) y traen cifras suyas ya masticadas |
| `loop.log`, `TABLERO.jsonl`, `TABLA_DE_CIERRE.txt` | ninguno esta retirado | registro, no clasificacion |
| `AUDITOR_FORJA.md`, `docs/BANCO_DE_REGLAS.md`, `src/aduana.py` | protocolo y codigo | ninguna |
| **`.v54/`** | **es el cuaderno de la vuelta auditada** | **vi sus `72` NOMBRES DE FICHERO en `git show --stat`. NO ABRI NI UNO.** |

    $ ls .v54/ | wc -l
    72

**`LECTURA`, Y ES CONTRA MI:** de los nombres de `.v54/` deduje cuales son los siete
candidatos que la vuelta toco con su `d024`, y eso es informacion del turno auditado
que se me colo por un listado. **Lo compenso diciendolo, no escondiendolo.** Mi
adjudicacion de la seccion `5` la hice leyendo los pasos y el libro, y **solo
despues** abri el `resumen_teorico` de las fichas; lo repito en `5.b`, donde importa.

**Y LO QUE NO HAGO CON `DEUDA.jsonl`:** no repito ni una sola de sus cifras en esta
pagina. Lo que de ahi salga, sale nombrado como suyo, o no sale.

---

## 1. LA PRIMERA MEDIDA, Y CAMBIA LO QUE ESTA FASE PUEDE SER: **LA VUELTA QUE VENGO A AUDITAR NO TRAE LOTE**

    $ find . -path ./.git -prune -o -newermt "2026-09-20 12:08:07" -type f -print | grep -c '^./cuarentena/'
    0

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        346 dataset/nodos.jsonl
        740 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1087 total

    $ ls cuarentena/grove_high_output/*.json | wc -l
    65

    $ python scripts/deuda.py | tail -n 2

      ultima vuelta de saneamiento: 54

    $ git diff --stat e63f5af..HEAD -- dataset/ bitacora/ censos/ config/ esquema/ src/ scripts/ tests/ hooks/ docs/BANCO_DE_REGLAS.md docs/MANUAL_SISTEMA_DE_CONOCIMIENTO.md docs/loop/AUDITOR_FORJA.md docs/loop/EXTRACTOR.md
    (sin salida: cero ficheros tocados)

    $ git status --porcelain -- dataset/ bitacora/ censos/ config/ esquema/ src/ cuarentena/
    (sin salida: cero ficheros tocados)

`e63f5af` es el commit de las `12:07:47`, **diecinueve segundos antes de que el arnes
abriera el turno del extractor a las `12:08:07`**, asi que el diff mide exactamente
el turno que vengo a auditar y nada mas.

**`LECTURA`:** la vuelta auditada es **de SANEAMIENTO, no de extraccion**. No
escribio ni un candidato nuevo en `cuarentena/`, no movio `dataset/`, `bitacora/`
ni `censos/`, y no toco `src/`, `scripts/`, `tests/`, el banco ni los protocolos,
que es lo que `D.45` le veda. El estado `346 / 740 / 1 / 65` es **identico** al que
la `ACTA 52` midio para la vuelta `53`.

**`LECTURA`, Y ES LA QUE MAS VALE DE ESTA PAGINA:** `D.58` dice que en una vuelta de
extraccion **no hay fase ciega, ni sello, ni testigo**, porque no hay cifra sobre el
grafo que proteger. Una vuelta de **saneamiento** protege todavia menos: su producto
entero vive en `DEUDA.jsonl`, `TABLERO.jsonl` y `TABLA_DE_CIERRE.txt`, y **el arnes
no retira ninguno de los tres**. Retirar cuatro ficheros no ciega una fase cuyo
material de trabajo esta en los que se quedan. **Lo registro y no lo adjudico**:
`D.56` tiene la doctrina congelada en `11` preguntas, y esta no abre parada ni entra
en la cola.

---

## 2. LA LIMITACION QUE ESCRIBO EN VEZ DE LA AFIRMACION (`AUDITOR_FORJA.md` `1.1`)

    $ python forja.py credito

    CREDITO DE LA LINEA 'serial' (D.48)
      registro: docs/loop/CREDITO_serial.jsonl

      LINEA SIN REGISTRO: no hay ningun suceso escrito.
      Una linea sin tandas NACE CON SU RACHA EN CERO y no hereda
      la de nadie (D.48). Lo que herede el arnes sera CERO remedios.

**NO PUBLICO NINGUNA RACHA EN ESTA PAGINA, Y ESTE ES EL MOTIVO.** El instrumento
dice `LINEA SIN REGISTRO` porque **el arnes retiro `CREDITO_serial.jsonl` para esta
fase**, no porque la linea no tenga sucesos. Copiar ese `cero` a mi acta seria
reiniciarme la racha yo mismo, que es justo lo que `5.4` prohibe: *un auditor que
pone su propia racha a cero se esta absolviendo*. **La racha viva la mido en mi
turno normal, con el registro repuesto, y no antes.**

**`LECTURA`:** el retiro de `CREDITO_serial.jsonl` hace que `forja.py credito`
devuelva en fase ciega una frase **cierta en su letra y enganosa en su efecto**.
Tambien lo registro y no lo adjudico.

---

## 3. LAS GUARDAS, CORRIDAS POR MI EN ESTA FASE

    $ python forja.py gate

    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada,
               vuelta, cita_incompleta, deprecado_en_superficie, arista_rota,
               arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones

    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python forja.py resolutor

    nodos vivos: 346
    nodos deprecados (archivo): 0
    alias registrados: 0

    $ python forja.py rancios

      [RANCIO] veredicto dar_elogio_disciplina_igual_critica contra elogiar_trabajo_especifico_contexto (linea 533, 2026-09-18) ...
      [RANCIO] veredicto dar_elogio_disciplina_igual_critica contra equilibrar_elogio_critica_equipo (linea 534, 2026-09-18) ...
      [RANCIO] veredicto dar_elogio_disciplina_igual_critica contra pedir_critica_primero_crear_seguridad_psicologica (linea 535, 2026-09-18) ...
      [RANCIO] veredicto dar_elogio_disciplina_igual_critica contra dar_elogio_disciplina_igual_critica (linea 732, 2026-09-18) ...

**`LECTURA`:** `gate` y `guiones` en VERDE. `resolutor` da `346` vivos, que es el
mismo numero que `gate` verifica y el mismo que cuenta `wc -l`: **tres instrumentos
y una sola cifra.** Los `4` rancios llevan fecha `2026-09-18`, **anterior a la vuelta
que audito**, y `D.15` dice que un rancio no pone el gate en rojo. **No se los cargo
a esta vuelta**, y lo digo porque cargarselos seria facil y seria falso.

**LO QUE NO CORRO AQUI Y POR ESO NO AFIRMO:** `python tests/test_aceptacion.py`. La
`ACTA 52` paro el bucle citando esa prueba en rojo, asi que su estado de hoy es
**materia del turno normal**: sin el reporte delante, una cifra suelta sobre ella
solo serviria para prejuzgarlo.

---

## 4. LA POBLACION DEL BARRIDO (`D.38.4`), MEDIDA Y CONTRASTADA CON SU PROPIA LETRA

    $ python forja.py informe cuarentena/grove_high_output/decidir_nivel_competente_inferior.json

    INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
    candidatos revisados        : 1
    poblacion del barrido       : 414   (346 del grafo mas 68 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

    EL SALDO
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0

    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 3
      por candidato bloqueado          : menor 3, mediana 3, mayor 3
      que señal levanta cada vecindad  : similitud_texto 3

    [BLOQUEARIA] decidir_nivel_competente_inferior
        vecino anunciar_decision_inesperada_reconvocar_reunion  [levantada por: similitud_texto]
          similitud_texto 0.364 | familia_id 0.000 | paso_contra_nodo 0.472
        vecino vencer_sindrome_grupo_pares_autoconfianza  [levantada por: similitud_texto]
          similitud_texto 0.368 | familia_id 0.000 | paso_contra_nodo 0.462
        vecino tomar_mando_reunion_pares_presidente_ausente  [levantada por: similitud_texto]
          similitud_texto 0.354 | familia_id 0.000 | paso_contra_nodo 0.460

`D.38.5` dice que la aduana ya mide mi misma poblacion, **asi que la cruce**: `414`
son `346` del grafo mas `68` de bandejas, y los `68` son `65` mas `3`.

    $ ls cuarentena/grove_high_output/*.json | wc -l
    65
    $ ls cuarentena/marquet_turn_the_ship/*.json | wc -l
    3
    $ ls cuarentena/ensayo_referencia_163/*.json | wc -l
    163

**LA DISCREPANCIA QUE PERSEGUI Y QUE NO ES UNA, Y LA ESCRIBO PORQUE LA PERSEGUI.**
`D.38.4` dice que la poblacion es el grafo **mas todo lo que espera en
`cuarentena/<libro>/`, descartando `_insertados` y `_derivadas`**. Por esa letra, las
`163` de `ensayo_referencia_163/` contarian y la poblacion seria `577` y no `414`.
**Fui a ver si el instrumento se apartaba de su regla, y la regla esta escrita mas
fina en el codigo:**

    $ sed -n '385,400p' src/aduana.py

    # Y SE DESCARTA LO QUE NO PUEDE ENTRAR, QUE NO ES LO MISMO QUE LO QUE NO HA
    # ENTRADO. `cuarentena/` tambien aloja `ensayo_referencia_163/`, que son 163
    # nodos de un CATALOGO DE REFERENCIA ajeno puestos ahi para calibrar la aduana
    # (`docs/ESTRENO_DE_LA_ADUANA.md`). Esos no esperan juicio: no van a entrar
    # nunca en este grafo, y medir el trabajo de hoy contra ellos seria abrir cola
    # de lectura contra material que la puerta rechazaria de todas formas.
    #
    # EL CRITERIO NO ES UNA LISTA DE NOMBRES ... **entra en la poblacion el
    # candidato cuyas fuentes estan TODAS en la tabla canonica vigente.** Una fuente
    # fuera de la tabla ya lo tumbaria en la puerta (guarda `fuentes`), asi que lo
    # que la poblacion deja fuera es exactamente lo que no podria entrar.

**`LECTURA`: NO HAY HALLAZGO AQUI, y esa es la conclusion.** El criterio del codigo
no es la carpeta sino la tabla canonica de fuentes, y por ese criterio las `163`
quedan fuera con razon. **`414` es la cifra correcta.** Lo dejo escrito porque una
busqueda que sale limpia vale lo mismo que una que caza algo, **siempre que se diga
que se corrio**.

---

## 5. MI CLASIFICACION A CIEGAS: `cap_02` de `grove_high_output`, SIETE CANDIDATOS Y SUS `50` PASOS

### 5.a. Por que `cap_02`, medido y no elegido a ojo

La vuelta auditada **no trajo lote** (seccion `1`), asi que no hay material nuevo que
clasificar. **Elijo el tramo de la bandeja que nadie ha adjudicado nunca**, y lo
compruebo en vez de suponerlo: ninguno de los siete vive en el grafo.

    $ for n in clasificar_trabajo_proceso_montaje_prueba construir_flujo_produccion_paso_limitante \
               detectar_arreglar_fallo_etapa_menor_valor dimensionar_inventario_materia_prima_reposicion \
               equilibrar_capacidad_personal_inventario_plazo preferir_inspeccion_proceso_prueba_destructiva \
               rehacer_flujo_paso_limitante_capacidad; do
        b=""; g=""
        [ -f "cuarentena/grove_high_output/$n.json" ] && b="BANDEJA"
        grep -q "\"id\": \"$n\"" dataset/nodos.jsonl && g="GRAFO"
        echo "$n : ${b:-.} ${g:-.}"
      done

    clasificar_trabajo_proceso_montaje_prueba : BANDEJA .
    construir_flujo_produccion_paso_limitante : BANDEJA .
    detectar_arreglar_fallo_etapa_menor_valor : BANDEJA .
    dimensionar_inventario_materia_prima_reposicion : BANDEJA .
    equilibrar_capacidad_personal_inventario_plazo : BANDEJA .
    preferir_inspeccion_proceso_prueba_destructiva : BANDEJA .
    rehacer_flujo_paso_limitante_capacidad : BANDEJA .

**Y EL TAMANO DEL TRAMO LO FIJA EL INSTRUMENTO DE `D.58`, NO YO:**

    $ python scripts/muestra_fidelidad.py --libro grove_high_output --capitulos cap_02 --semilla v54-ciega-auditor

    MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO (D.58)
      libro    : grove_high_output
      semilla  : v54-ciega-auditor
      capitulos: cap_02

      RELEIDO ENTERO : cap_02
      POR MUESTRA    : ninguno, 15 pasos cada uno

      EL DISPARADOR: si la muestra de un capitulo pasa del 10 por ciento de
      pasos inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.

      --- cap_02: ENTERO, 50 paso(s), no hay muestra que elegir

**El propio instrumento dice que `cap_02` NO se muestrea: se relee ENTERO**, sus `50`
pasos. Es lo que hice. Y los `50` los confirmo por una segunda via, porque una cifra
con un solo instrumento detras es media cifra:

    $ grep -l 'fuentes/grove_high_output/cap_02.md' cuarentena/grove_high_output/*.json | wc -l
    7

    $ for f in $(grep -l 'fuentes/grove_high_output/cap_02.md' cuarentena/grove_high_output/*.json); do
        python -c "import json,sys;d=json.load(open(sys.argv[1],encoding='utf-8'));print(len(d['pasos_accionables']), d['id'])" $f; done

    7 clasificar_trabajo_proceso_montaje_prueba
    10 construir_flujo_produccion_paso_limitante
    6 detectar_arreglar_fallo_etapa_menor_valor
    7 dimensionar_inventario_materia_prima_reposicion
    8 equilibrar_capacidad_personal_inventario_plazo
    6 preferir_inspeccion_proceso_prueba_destructiva
    6 rehacer_flujo_paso_limitante_capacidad

    $ ... | awk '{s+=$1} END {print "SUMA:", s}'
    SUMA: 50

**Las dos vias dan `50`.** La segunda no es un instrumento nuevo (`D.47`): es un
contador de longitud de lista, de la especie del `wc -l` que `D.38.3` autoriza por su
nombre. **La que manda es `muestra_fidelidad.py`; la otra esta ahi para que se vea si
se separan.**

    $ wc -l fuentes/grove_high_output/cap_02.md
    79 fuentes/grove_high_output/cap_02.md

Lei el fichero fuente entero, sus `79` lineas.

### 5.b. EL ORDEN EN QUE LO HICE, QUE ES LO QUE HACE VALER LO QUE SIGUE

**Primero** imprimi los `50` pasos, las condiciones de activacion y los entregables de
los siete. **Segundo** lei `cap_02.md` entero. **Tercero** adjudique con la vara de la
seccion `6`. **Y SOLO CUARTO** abri el `resumen_teorico`, que es donde el extractor
escribe su propio razonamiento.

Lo digo porque el `resumen_teorico` **viaja dentro del candidato que el prompt me
manda abrir**, y quien lo lea primero ya no esta adjudicando a ciegas: **esta
corrigiendo un examen con la solucion al lado.** No es una trampa del extractor ni del
arnes; es una consecuencia del formato, y no la habia visto escrita en ningun sitio.
**Tambien la registro y no la adjudico.**

### 5.c. LAS SIETE PIEZAS, Y NINGUNA ES REPITE

| pieza | candidato | pasos | mi clase |
|---|---|---|---|
| `P2` | `construir_flujo_produccion_paso_limitante` | `10` | **procedimiento propio** |
| `P5` | `clasificar_trabajo_proceso_montaje_prueba` | `7` | **procedimiento propio** |
| `P6` | `rehacer_flujo_paso_limitante_capacidad` | `6` | **CONTINUA de `P2`** |
| `P7` | `equilibrar_capacidad_personal_inventario_plazo` | `8` | **procedimiento propio** |
| `P9` | `preferir_inspeccion_proceso_prueba_destructiva` | `6` | **procedimiento propio** |
| `P10` | `dimensionar_inventario_materia_prima_reposicion` | `7` | **procedimiento propio** |
| `P11` | `detectar_arreglar_fallo_etapa_menor_valor` | `6` | **CONTINUA de `P5` y de `P10`** |

**`P6` CONTINUA DE `P2`, adjudicado con la vara `6.1` y sin bascula.** `P2` construye
el flujo desde el paso limitante; `P6` lo **rehace** cuando aparece una cola. Su paso
`4` repite el calculo hacia atras de `P2` paso `7`, y ahi acaba el solape. **Lo que
queda fuera es procedimiento en los dos lados:** en `P6`, detectar el supuesto de
capacidad infinita, buscar donde hay cola, **contar el tiempo de espera dentro del
flujo** (*tu huevo de tres minutos se convierte facilmente en uno de seis*), dejar
iguales los ciclos que la cola no toca y **no cambiar de componente el que manda la
calidad**; en `P2`, los cuatro requisitos basicos, el descarte de la carta blanca, el
tiempo total de paso y el escalonado. **Condiciones de activacion distintas** (`P2`:
todavia no sabes por cual empezar; `P6`: ya tienes flujo y aparece un turno de
espera). **No es duplicado.**

**`P11` CONTINUA DE `P5` Y DE `P10`, y las dos las levanta la lectura, no una senial.**
`P11` paso `6` nombra la prueba unitaria, que es `P5` paso `4`; `P11` paso `4` nombra
la inspeccion del material que entra, que es `P10` paso `1`. Pero `P11` trae
procedimiento que no esta en ninguno de los dos: **ordenar las etapas por el valor que
el material lleva encima** y poner la comprobacion en la de menor valor, con el valor
percibido de la ultima etapa contado dentro. **Eso no es nombrar: es procedimentar**
(`P.5.1`).

**`P9` CONTRA `P10`, Y NO SON EL MISMO NODO AUNQUE LOS DOS HABLEN DE INSPECCION.** `P9`
elige **entre prueba funcional que destruye producto e inspeccion dentro del proceso**;
`P10` pone la inspeccion **en la recepcion** y dimensiona el inventario. Decisiones
distintas, alternativas distintas, entregables distintos.

**`P7` Y `P5` NO ROZAN A NADIE** del capitulo: `P7` es el intercambio entre capacidad,
mano de obra e inventario contra el plazo; `P5` es el reparto en las tres operaciones
de produccion.

### 5.d. LA FIDELIDAD `D.30` DE LOS `50`, LEIDA Y NO CONTADA A OJO

**`LECTURA`: segui los `50` pasos uno a uno hasta una frase de `cap_02.md` y NO
ENCONTRE NINGUN PUENTE.** No lo publico como porcentaje: el porcentaje es la metrica
de la seccion `8`, y esa **la firmo en el acta con el desglose del reporte delante**,
no aqui. Lo que publico es la lectura con sus anclas:

| paso | lo que dice la ficha | lo que dice `cap_02.md` |
|---|---|---|
| `P2`.`10` | *el mas largo, o el mas dificil, o el mas sensible, o el mas caro* | *starting with the longest (or most difficult, or most sensitive, or most expensive) step* |
| `P2`.`6` | *no solo es el que mas tarda, es tambien el componente mas importante* | *Not only does that component take the longest to prepare, the egg is also for most customers the most important feature* |
| `P5`.`2` | *una sola presentacion con sus folletos, sus hojas y sus laminas* | *into one presentation, along with such things as brochures, handouts, and flip charts* |
| `P6`.`3` | *tu huevo de tres minutos se convierte facilmente en uno de seis* | *your three-minute egg could easily become a six-minute egg* |
| `P6`.`6` | *el huevo sigue determinando la calidad general del desayuno* | *The egg still determines the overall quality of the breakfast* |
| `P7`.`7` | *hay una respuesta correcta: el mejor plazo y la mejor calidad al coste mas bajo* | *there is a right answer, the one that can give you the best delivery time and product quality at the lowest possible cost* |
| `P9`.`2` | *se pierde todo el pan tostado porque no hay huevos que servir con el* | *All the toast is also wasted because you don't have any eggs to serve with it* |
| `P9`.`5` | *un aviso en cuanto el parametro varie un grado o dos* | *set off bells anytime the temperature varied by a degree or two* |
| `P10`.`2` | *de tamano mayor o menor del que toca, porque eso cambia lo rapido que se procesa* | *over- or undersized, which would affect how fast they cook* |
| `P11`.`2` | *cuando entra en el aparcamiento y ve el rotulo* | *when he drives into the parking lot after seeing the sign* |

**MI UNICA RESERVA, Y LA MARCO YO:** varios pasos convierten en imperativo lo que el
libro escribe en descriptivo (*process manufacturing, an activity that...* pasa a
*Senala en tu trabajo el paso de proceso, que es...*). **Eso no lo cuento como
puente**, porque el contenido es del libro y el propio libro generaliza (*Process,
assembly, and test operations can be readily applied to other very different kinds of
productive work*). **Lo dejo marcado para que el que discrepe pueda discrepar con la
frase delante**, que es lo que `D.38.3` pide de una conclusion.

### 5.e. LO QUE `cap_02.md` TIENE Y NINGUN CANDIDATO COGE, COMPROBADO ANTES DE LLAMARLO HUECO

El capitulo cierra con el sistema de justicia penal leido como proceso de produccion
(el millon de dolares por condena, la celda de `80.000` como paso limitante
equivocado) y con la fabrica de desayunos en continuo. **Ninguno de los siete los
toca.** Antes de llamarlo hueco mire la numeracion de las piezas de origen:

    P2, P5, P6, P7, P9, P10, P11

**`LECTURA`: NO LO PUBLICO COMO HUECO.** Faltan `P1`, `P3`, `P4` y `P8`: la frontera de
`cap_02` **declaro mas piezas de las que hizo nodo**, que es exactamente lo que tiene
que pasar con el tramo que no es procedimiento. **El motivo de cada una vive en el
REPORTE de la vuelta que la publico, y ese no lo puedo abrir en esta fase.** Queda
escrito como lo que es: **una comprobacion que no pude cerrar**, no un hallazgo.

---

## 6. LOS DOS PARES QUE LEVANTO LEYENDO Y QUE CRUZAN DE CAPITULO

**Esto es lo que traigo de la fase ciega.** `D.38.4` manda barrer sobre grafo mas
bandejas, y **los cuatro extremos de estos dos pares estan en la bandeja**: son la
figura que el comentario de `src/aduana.py` dice que **antes del 12 sep no levantaba
nadie**, y que desde entonces la aduana si mide.

**ADJUDICO PRIMERO Y CONTRASTO DESPUES.** Las dos clases que siguen las escribi
leyendo los pasos, **antes de leer la salida del barrido de la seccion `7`**. Lo digo porque de
los dos pares **la maquina levanta uno y no levanta el otro**, y si hubiera mirado
primero su salida no podria demostrar que mi lectura no la siguio.

### 6.a. `detectar_arreglar_fallo_etapa_menor_valor` (`cap_02`) contra `supervisar_tarea_delegada_etapa_menor_valor` (`cap_04`)

**Comparten la frase dentro del propio id.** Madre `cap_02`, hijo `cap_04`, y la
pregunta se hace **del hijo a la madre y nunca al reves** (`6.1`).

**MI CLASE: CONTINUA.** El hijo toma de la madre **un solo paso** (su paso `2`,
*supervisa en la etapa del proceso de menor valor anadido*) y trae seis propios que la
madre no tiene: **frecuencia variable con esquemas de muestreo distintos**, **madurez
relativa a la tarea y no capacidad general**, **bajar la intensidad segun mejora el
trabajo**, y **entrar en el detalle solo al azar**, con su limite escrito (*entrar en
todos los detalles seria como probar el cien por cien de lo que fabricacion saco*).
Eso es **procedimiento propio, no el nombre de otro**. Y lo que queda fuera en la madre
tambien es procedimiento: ordenar las etapas por valor y sus tres aplicaciones. **No es
duplicado, y la arista madre a hijo esta justificada por ese paso `2`.**

### 6.b. `construir_flujo_produccion_paso_limitante` (`cap_02`) contra `identificar_paso_limitante_jornada_desfases` (`cap_04`)

**ESTE ES MI DISCUTIBLE MARCADO, y lo marco ANTES de saber si acierto** (`5.1`).

**MI CLASE: CONTINUA, pero es la mas delgada de toda la pagina y digo por que.** De los
`5` pasos del hijo: el `1` es encuadre (*aplicales los principios de produccion*), el
`2` es la madre (*identifica tu paso limitante*), el `4` es la madre (*crea desfases*),
y el `5` empieza por *En resumen* y resume los anteriores. **Queda UN paso propio, el
`3`**, y es un criterio de seleccion **distinto** del de la madre: la madre elige el
paso limitante por **cual tarda mas**; el hijo, por **cual no tiene holgura en un
calendario absoluto**. Su condicion de activacion tambien es otra: ordenar tu jornada
de mando contra las recomendaciones corrientes de gestion del tiempo.

**LO QUE SOSTIENE MI CLASE:** un criterio de seleccion nuevo es procedimiento.
**LO QUE LA PONE EN DUDA, Y LO ESCRIBO YO:** con `P.5.1` aplicado estricto (*una segunda
linea solo cuenta como expansion si trae procedimiento propio, no solo el nombre de
otro*), **un paso propio de cinco** es el borde exacto de esa regla. **Un lector
estricto lo llama REPITE con etiqueta nueva, y tendria con que.** Si esta pagina cae en
algun sitio, cae aqui, **y prefiero que caiga marcada.**

**Y NO LA ADJUDICO CITANDO UNA SENIAL** (`D.19`): la leo por los pasos.

---

## 7. LO QUE LA MAQUINA DICE DE ESOS DOS PARES, Y NO DICE LO MISMO DE LOS DOS

Corri el barrido sobre los dos **hijos** para ver **si alguna senial los levanta contra
su madre de `cap_02`**. Es lo que decide si mi lectura anade algo o solo repite lo que
el instrumento ya veia. **Los dos resultados salen distintos, y el que me corrige a mi
va primero.**

### 7.a. EL PAR `6.a` SI LO LEVANTA LA MAQUINA, Y NO POR DONDE YO HABRIA APOSTADO

    $ python forja.py informe cuarentena/grove_high_output/supervisar_tarea_delegada_etapa_menor_valor.json

    poblacion del barrido       : 414   (346 del grafo mas 68 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

      vecinos levantados en total      : 3
      que señal levanta cada vecindad  : familia_id 1, similitud_texto 2

    [BLOQUEARIA] supervisar_tarea_delegada_etapa_menor_valor
        vecino detectar_arreglar_fallo_etapa_menor_valor  [levantada por: familia_id]
          similitud_texto 0.226 | familia_id 0.333 | paso_contra_nodo 0.435
          paso 1 del candidato contra paso 2 de detectar_arreglar_fallo_etapa_menor_valor
        vecino supervisar_decision_delegada_preguntas_concretas  [levantada por: similitud_texto]
          similitud_texto 0.356 | familia_id 0.222 | paso_contra_nodo 0.429
        vecino identificar_paso_limitante_jornada_desfases  [levantada por: similitud_texto]
          similitud_texto 0.362 | familia_id 0.000 | paso_contra_nodo 0.361

**`LECTURA`: mi par `6.a` esta levantado, y lo levanta `familia_id` con `0,333`, no la
similitud de texto, que se queda en `0,226` y no habria llegado al umbral `0.35`.**
La senial de id caza aqui lo que la de prosa no ve, porque los dos ids comparten
`etapa_menor_valor` mientras uno habla de borradores de informes y el otro de huevos
podridos. **Mi lectura de `6.a` coincide con la maquina y no la mejora**, y lo escribo
asi en vez de vender el par como hallazgo mio.

### 7.b. EL PAR `6.b` NO LO LEVANTA NINGUNA SENIAL

    $ python forja.py informe cuarentena/grove_high_output/identificar_paso_limitante_jornada_desfases.json

    poblacion del barrido       : 414   (346 del grafo mas 68 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

      vecinos levantados en total      : 6
      que señal levanta cada vecindad  : similitud_texto 6

    [BLOQUEARIA] identificar_paso_limitante_jornada_desfases
        vecino agrupar_tareas_semejantes_aprovechar_preparacion
          similitud_texto 0.410 | familia_id 0.000 | paso_contra_nodo 0.450
        vecino llevar_inventario_proyectos_discrecionales
          similitud_texto 0.401 | familia_id 0.000 | paso_contra_nodo 0.392
        vecino supervisar_decision_delegada_preguntas_concretas
          similitud_texto 0.398 | familia_id 0.000 | paso_contra_nodo 0.406
        vecino supervisar_tarea_delegada_etapa_menor_valor
          similitud_texto 0.379 | familia_id 0.000 | paso_contra_nodo 0.398
        vecino agrupar_interrupciones_subordinados_reuniones_regulares
          similitud_texto 0.371 | familia_id 0.000 | paso_contra_nodo 0.404
        vecino decir_no_trabajo_excede_capacidad
          similitud_texto 0.369 | familia_id 0.000 | paso_contra_nodo 0.413

**`LECTURA`, Y ES EL HALLAZGO DE ESTA PAGINA.** El barrido le levanta **`6` vecinos, y
los `6` son de `cap_04` y `cap_05`**. **`construir_flujo_produccion_paso_limitante` NO
esta entre ellos**, y es el nodo del que este candidato toma dos de sus cinco pasos.
Como no aparece en la lista, **ninguna de las tres seniales llego a su umbral**: ni la
similitud de texto a `0.35` ni `familia_id` a `0.30`. **Y `familia_id` es la que aqui
sorprende**, porque los dos ids comparten las palabras `paso_limitante` y los dos
entregables nombran los `desfases`; **no puedo publicar su valor, porque el informe
solo imprime los vecinos que levanta**, y eso mismo es lo que declaro.

**El contraste con `7.a` es lo que hace informativo a este par:** alli `familia_id`
cazo con `0,333` lo que la prosa no veia con `0,226`; aqui **no caza ninguna de las
dos**. El hijo habla de jornada de mando y calendario, la madre de huevos, tostadas y
cafe.

**ES `D.19` CON UN EJEMPLAR VIVO Y MEDIDO HOY:** *ninguna senial separa jerarquia de
ruido, asi que una discrepancia NUNCA se adjudica citando una senial.* Aqui la senial
no es que adjudique mal: **es que no levanta el par**. Si `identificar_paso_limitante`
entrase por esta cola de lectura, **sus seis veredictos se escribirian contra seis
vecinos que no son su madre**, y la unica relacion que de verdad tiene quedaria sin
cablear.

**LO QUE NO AFIRMO:** no digo que la aduana este rota. Su `umbral 0.35` esta puesto por
`config/umbrales.json`, **que no es mio para mover** (`AUDITOR_FORJA.md` `2`), y un
umbral mas bajo levantaria mas ruido del que quita. **Lo que digo es lo medido: este
par existe, la lectura lo ve y el barrido no**, que es exactamente para lo que `D.38.4`
me manda barrer a mano.

---

## 8. LO QUE ESTA PAGINA NO PUDO COMPROBAR, Y POR ESO NO AFIRMA

| lo que queria mirar | por que no pude | donde se cierra |
|---|---|---|
| la racha viva de la linea `serial` | `CREDITO_serial.jsonl` esta retirado en esta fase (seccion `2`) | mi turno normal |
| `tests/test_aceptacion.py`, que la `ACTA 52` dejo en rojo | sin reporte delante, la cifra solo serviria para prejuzgar | mi turno normal |
| el motivo de que `P1`, `P3`, `P4` y `P8` de `cap_02` no hicieran nodo | vive en el REPORTE de la vuelta que publico esa frontera | mi turno normal |
| los seis pagos de la vuelta auditada | su comprobacion es la materia del acta, no de la fase ciega | mi turno normal |

**Y UNA ULTIMA, QUE ES LA MAS INCOMODA:** esta pagina clasifica material de `cap_02`
que **la vuelta auditada no produjo**. Es la lectura mas util que la fase ciega admitia
sobre una vuelta de saneamiento, **pero no es la comparacion que `5.1` describe**: no
hay discutibles marcados de esta vuelta contra los que medirme, porque **esta vuelta no
marco ninguno**. Lo digo aqui y no en una nota al pie.

---

## 9. LA TABLA DE CIERRE DE MI APERTURA

| | |
|---|---|
| **ACTA ANTERIOR LEIDA** | `d5f4eb832cb0ffd11ddaf35a5bf406e4e2b5f231` |
| **HEREDADOS** | `0`, comprobado con `python forja.py herencia` y contra la `ACTA 52` |
| **los cuatro retirados** | siguen fuera del arbol; no recupere ninguno |
| **estado medido** | `346` nodos, `740` veredictos, `1` par mutuo, `65` en la bandeja de `grove_high_output` |
| **poblacion del barrido** | `414` (`346` del grafo mas `68` de bandejas) |
| **guardas corridas por mi** | `gate` VERDE, `guiones` VERDE, `resolutor` `346`, `rancios` `4` y todos anteriores a esta vuelta |
| **candidatos clasificados** | `7` de `cap_02`, sus `50` pasos releidos enteros contra las `79` lineas del fuente |
| **clases que adjudico** | `5` procedimiento propio, `2` CONTINUA; **cero REPITE, cero gemelo** |
| **pares que cruzan de capitulo y adjudico** | `2`, los dos con un extremo en `cap_02` y el otro en `cap_04`, los dos **CONTINUA** |
| **de esos, los que ninguna senial levanta** | `1`, el `6.b`. El `6.a` lo levanta `familia_id` con `0,333` y lo digo (`7.a`) |
| **mi discutible marcado** | `1`: `construir_flujo_produccion_paso_limitante` contra `identificar_paso_limitante_jornada_desfases` |
| **fidelidad `D.30` de los `50`** | ningun puente encontrado por mi lectura; la cifra de la seccion `8` la firmo en el acta, no aqui |
| **cifras sin instrumento** | ninguna |
| **preguntas de doctrina** | `3`, registradas y no adjudicadas (`D.56`): secciones `1`, `2` y `5.b` |
