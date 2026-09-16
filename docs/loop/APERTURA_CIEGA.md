# APERTURA CIEGA DE LA VUELTA 27, auditor del bucle del extractor

*Escrita ANTES de que el arnes me exponga `docs/loop/REPORTE.md`. Los cuatro ficheros
que `D.34.2` retira (`REPORTE.md`, `loop.log`, `ultimo_extractor.json`,
`ultimo_auditor.json`) **no estan en el arbol y no los he recuperado de git ni por
ninguna otra via**. Lo que si he abierto, y la regla lo autoriza expresamente, es
`docs/loop/ACTA_AUDITOR.md`, que es obra mia.*

> **`D.38.3` MANDA EN ESTE FICHERO: toda cifra sale de un instrumento de la casa
> corrido en esta misma fase, con su salida literal pegada al lado.** Las
> clasificaciones son lecturas mias y van nombradas como tales.

---

## 0. LA DECLARACION QUE EL ARNES EXIGE

    ACTA ANTERIOR LEIDA: 4adfa30e9d4fc5a15f370795e0124fe98c394356
    HEREDADO 1: CUMPLIDO
    HEREDADO 2: CUMPLIDO
    HEREDADO 3: CUMPLIDO

### 0.1. La huella, comprobada y no copiada

No me creo la huella porque el prompt me la de: la mido contra el fichero que tengo
delante.

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    4adfa30e9d4fc5a15f370795e0124fe98c394356

    $ git cat-file -t 4adfa30e9d4fc5a15f370795e0124fe98c394356
    blob

    $ git log --all --oneline --find-object=4adfa30e... -- docs/loop/ACTA_AUDITOR.md
    f52f77e D.42: la unidad de la ruta es la celda. El censo corre en el commit, y la cifra 2 de la vuelta 25 es 4 por regeneracion

**Es la misma acta, al byte.** La ultima cabecera que escribe es `ACTA 25`, y la vuelta
que voy a auditar es la 26:

    $ grep -c "^# ACTA " docs/loop/ACTA_AUDITOR.md
    25

**NO HAY HUECO DE ACTA** (`AUDITOR_FORJA.md` 1.0): la ultima acta escrita cubre la
vuelta inmediatamente anterior a la que audito.

### 0.2. `HEREDADO 1: CUMPLIDO`

`HEREDADO 1` es la tabla `7.5` de la `ACTA 25`, la de los remedios que aguantaron. Se
hereda para que se declare otra vez, y la declaro fila por fila, con lo que he hecho en
ESTA fase:

| remedio de la fila | como queda hoy |
|---|---|
| **el orden del turno** (`4.1`) | **AGUANTA.** Los pasos de los ids de la tanda estaban impresos en disco (`.v27/lee_par.py`, corrido desde el fichero) **antes** de que adjudicara una sola clase o nombrara una sola arista |
| **remedir toda cifra propia** (`4.2`) | **AGUANTA, y cazo una lectura mia antes de publicarla.** Lei un caracter roto en los pasos de `bajar_detalle_organizacion_fuente_hechos` y estuve a punto de escribir que el grafo tenia texto estropeado. Lo remedi con instrumento y **el grafo esta limpio**: lo roto era la consola de mi impresor. La salida literal esta en `2.4` |
| **ninguna arista sin el paso de la madre** (`4.3`) | **AGUANTA, y hoy va con el ensanche de `HEREDADO 3.1`**: de cada arista que nombro imprimo los pasos ENTEROS **de la madre Y del hijo**. Van en `4` |
| **barrido y herencia una a una** (`4.4`) | **AGUANTA**, cero `NO APLICA` en la herencia: los tres se declaran arriba y se razonan aqui |
| **la muestra con su banda** (`4.5`) | **NO APLICA EN ESTA FASE, y el motivo es que la muestra pineada se paga contra `bitacora/VEREDICTOS.jsonl` destapado, que es turno normal y no fase ciega.** Lo que si hago hoy, y es la mitad que si puede hacerse a ciegas, es **escribir la semilla y el tamanio ANTES de ver nada** (`7`) |
| **la cola del hueco** (`HEREDADO 5`) | **AGUANTA y se remidio: la cola heredada de `decidir_momento_despedir_persona` era `4` y son `4`, y son los cuatro nombres escritos.** La salida esta en `5.2` |

### 0.3. `HEREDADO 2: CUMPLIDO`

`HEREDADO 2` es la cabecera de la seccion `11` de la `ACTA 25`, y lo que afirma es
comprobable: que los remedios van en el acta y no en `PROMPT_SIGUIENTE.md`, y que
**`src/herencia.py` los saca de esa acta**. Lo corro:

    $ python forja.py herencia
    REMEDIOS PENDIENTES QUE HEREDAS
    ...
      acta anterior : ACTA 25. VUELTA 25, lote 4 (`scott_radical_candor`) INSERTANDO Y ...
      su huella     : 4adfa30e9d4fc5a15f370795e0124fe98c394356
      heredados     : 3
    HEREDADO 1   [REMEDIO, linea 23451 del acta]
    HEREDADO 2   [REMEDIO, linea 23559 del acta]
    HEREDADO 3   [TAREA BLOQUEANTE, linea 23564 del acta]

**El instrumento de la casa reproduce el bloque que el arnes me dio, con la misma huella
y los mismos tres heredados.** `D.40` esta cableada y muerde.

La otra mitad de la cabecera decia *`PROMPT_SIGUIENTE.md`, que hoy queda vacio por la
parada*. **Hoy ya no esta vacio**, y eso es correcto: lo reescribio la decision del
fundador del 15 sep (`docs/loop/paradas/2026-09-15-la-ruta-vacia-DECISION.md`), que
levanta la parada. **Pero al comprobarlo he encontrado lo que se cuenta en `6`, y no es
menor.**

### 0.4. `HEREDADO 3: CUMPLIDO`, punto por punto

| punto | como queda | donde |
|---|---|---|
| **1. una arista se decide con los DOS lados impresos** | **CUMPLIDO.** Ninguna arista se nombra en este fichero sin los pasos enteros de madre e hijo impresos antes | `4` |
| **2. un instrumento mio que vuelca texto del libro al arbol sanea los guiones al escribir** | **NO APLICA, y el motivo es que en esta fase ninguno de mis instrumentos escribe en el arbol.** Todos leen e imprimen; lo unico que escribo es este fichero. Y la guarda queda comprobada igual: `python forja.py guiones` sale **VERDE** (`1.2`) | `1.2` |
| **3. el instrumento se guarda en disco y se corre DESDE EL FICHERO** | **CUMPLIDO, sin una sola excepcion.** Los instrumentos de esta fase estan en `.v27/`, se corren con `python .v27/<fichero>` y su salida se guarda al lado con `tee` | `1.4` |
| **4. todo `LO QUE SI ENCARGO` de mi acta se busca con `grep` en mi propio `PROMPT_SIGUIENTE.md`** | **CUMPLIDO, y ES EL QUE CAZA ALGO.** Corrido desde fichero, sobre los ocho puntos de `ACTA 25` `11.1`: **siete de los ocho NO estan** | `6` |
| **5. la muestra pineada sube a su techo cuando la poblacion lo permite** | **CUMPLIDO en la mitad que es ciega:** mido la poblacion de la tanda con instrumento y **escribo aqui la semilla y el tamanio antes de ver una sola clase** | `7` |

---

## 1. LO QUE MIDO AL ABRIR, CON EL INSTRUMENTO AL LADO

### 1.1. El gate y el resolutor

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 234
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones

    $ python forja.py resolutor
    nodos vivos: 234
    nodos deprecados (archivo): 0
    alias registrados: 0

### 1.2. Guiones y vigencia

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python forja.py rancios
    BLOQUE DE VIGENCIA VERDE.
      veredictos comprobados: 240
      citas de enlace mutuo comprobadas: 0
      todos siguen emitidos contra el texto que leyeron

### 1.3. La prueba de aceptacion, que sale en ROJO, y el rojo es de la propia fase ciega

    $ python tests/test_aceptacion.py
    Ran 130 tests in 11.252s
    FAILED (failures=1)
    ...
      total: 130 pruebas, 1 fallos, 0 errores

    FAIL: test_e_guion_largo_rompe_el_hook (__main__.PruebaE.test_e_guion_largo_rompe_el_hook)
    AssertionError: 1 != 0 : el repo ha de estar limpio antes de ensuciarlo:
    ...
    [pre-commit] tallado del reporte (D.41) y censo de rutas (D.42)
    Traceback (most recent call last):
      File "...\scripts\tallar_reporte.py", line 315, in revisar
        texto = io.open(ruta_reporte, encoding="utf-8").read()
    FileNotFoundError: [Errno 2] No such file or directory: '...\docs\loop\REPORTE.md'

**LO CLASIFICO Y NO SE LO CUELGO A LA VUELTA 26: este rojo lo produce la fase ciega
misma.** `D.34.2` retira `REPORTE.md` del arbol para que yo lea a ciegas, y
`scripts/tallar_reporte.py` **revienta con `FileNotFoundError` en vez de declarar que no
hay reporte que tallar**. `PruebaE` exige repo limpio, corre el hook, el hook corre el
tallado, y el tallado muere.

**Es un choque entre dos reglas de la casa, las dos vigentes:** `D.34.2` (el arnes retira
cuatro ficheros) y `D.41` (el tallado corre en el hook). **Mientras las dos esten
escritas, TODA apertura ciega de TODO auditor vera esta prueba en rojo**, y un rojo que
sale siempre deja de informar. Lo traigo al turno normal con esta clase: **no es caida de
la vuelta 26, es una arista suelta entre dos reglas mias.**

### 1.4. Mis instrumentos de esta fase, todos guardados y corridos desde fichero

| fichero | que hace | su salida |
|---|---|---|
| `.v27/barrido_v27.py` | barrido de vecinos sobre los 348 de grafo mas bandejas, con `aduana.buscar_vecinos` | **VACIA A PROPOSITO: la corrida entera sigue en marcha al cerrar esta fase y su fichero esta en CERO BYTES. NINGUNA CIFRA DE ESTE DOCUMENTO SALE DE AHI**, y por eso la celda se marca en vez de citarse |
| `.v27/lee_par.py` | imprime los pasos ENTEROS de los dos lados de un par | a pantalla, pegado en `4` |
| `.v27/frontera_cap07_v27b.py` | mi corte ciego de `cap_07` | `.v27/frontera_cap07_v27b.txt` |
| `.v27/frontera_cap06_v27.py` | mi corte ciego de `cap_06` | `.v27/frontera_cap06_v27.txt` |
| `.v27/medida_dirigida_v27.py` | la senial de la casa sobre una poblacion declarada | `.v27/medida_dirigida_v27.txt` |
| `.v27/medida_gemelo_v27.py` | la senial de la casa sobre diez pares grafo contra bandeja | `.v27/medida_gemelo_v27.txt` |
| `.v27/grep_encargos_v27.sh` | `HEREDADO 3` punto 4, encargo por encargo | `.v27/grep_encargos_v27.txt` |

> ### **Y LA PRIMERA FILA ES LA LECCION DE LA PARADA DE LA VUELTA 25, APLICADA A MI MISMO**
>
> **El barrido entero sobre los 348 es caro y no ha terminado dentro de esta fase**, asi
> que su fichero esta en **cero bytes**. La vuelta 25 paro por exactamente esto: **una
> cifra sostenida por una ruta vacia.** Asi que **no cito ese fichero como sede de nada**
> y marco la celda con su motivo, que es la forma `(b)` de `D.42`.
>
> **Lo que si esta medido, y por eso el hallazgo de `5` no depende de ese barrido, es:**
> el instrumento de la casa `python forja.py informe` corrido entero sobre un candidato
> (`348` de poblacion, salida en `.v27/informe_cuidarse.txt`), y **dos medidas dirigidas
> con `aduana.medir`** sobre poblaciones que declaro (`.v27/medida_dirigida_v27.txt` y
> `.v27/medida_gemelo_v27.txt`). **Los tres ficheros tienen contenido.**

---

## 2. EL ESTADO QUE ENCUENTRO, MEDIDO

### 2.1. Las cuatro cuentas

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
      234 dataset/nodos.jsonl
      240 bitacora/VEREDICTOS.jsonl
        1 config/pares_mutuos.jsonl

    $ ls cuarentena/scott_radical_candor/*.json | wc -l
    111
    $ ls cuarentena/marquet_turn_the_ship/*.json | wc -l
    3
    $ ls cuarentena/_insertados/scott_radical_candor/*.json | wc -l
    31

**La poblacion de mi barrido (`D.38.4`) es 348**, y la mide el instrumento de la casa,
no yo:

    $ python forja.py informe cuarentena/scott_radical_candor/cuidarse_agotamiento_centro_rueda.json
    poblacion del barrido       : 348   (234 del grafo mas 114 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

### 2.2. Lo que entro en la vuelta 26, contado contra el arbol y no contra su palabra

Comparo el grafo de hoy con el grafo del ultimo commit anterior a la vuelta (`f52f77e`):

    antes: 222
    ahora: 234
    NUEVOS EN LA VUELTA 26: 12
      despedir_persona_franqueza_radical
      decidir_momento_despedir_persona
      reconocer_recompensar_gente_estable
      retar_superestrellas_equipo_constantemente
      retirar_etiquetas_permanentes_equipo
      revisar_cinco_causas_mal_desempenio
      subir_vara_calidad_equipo
      abrir_debate_humor_explicar_proposito
      adaptar_escucha_cultura_ajena
      aprender_resultados_vencer_dos_presiones
      bajar_detalle_organizacion_fuente_hechos
      cambiar_posicion_hechos_explicar_cambio

**Cuadra por los cuatro lados y al digito:** grafo `222` mas `12` es `234`; insertados
`19` mas `12` es `31`; bandeja `123` menos `12` es `111`.

### 2.3. Las aristas, contadas de los dos campos y no de una lista

    aristas al cerrar la vuelta 25 : 81
    aristas al cerrar la vuelta 26 : 84
    NUEVAS EN LA VUELTA 26         : 3
       acompaniar_mejores_equipo_socio > reconocer_recompensar_gente_estable
       acompaniar_mejores_equipo_socio > retar_superestrellas_equipo_constantemente
       cambiar_potencial_trayectoria_crecimiento > retirar_etiquetas_permanentes_equipo
    RETIRADAS                      : 0

### 2.4. Una cifra mia que NO publico, porque la remedi antes (`HEREDADO 1`, `4.2`)

Mi impresor escribio un caracter de reemplazo donde el nodo
`bajar_detalle_organizacion_fuente_hechos` lleva una letra acentuada, y la lectura obvia
era *el grafo tiene texto roto*. **La medi antes de escribirla:**

    $ python -c "cuenta nodos del grafo con el caracter de reemplazo U+FFFD"
    TOTAL NODOS DEL GRAFO CON U+FFFD: 0

    $ python -c "mismo nodo, stdout reconfigurado a utf-8"
    Hacer espeleologia en tu organizacion: meterse de vez en cuando en los detalles de una
    decision pequena, e ir al que hace el trabajo cuando el que decide eres tu

**El grafo esta limpio y lo roto era la consola de mi propio impresor.** Lo dejo escrito
porque un remedio que solo se declara cuando falla no informa: hoy ha impedido que
publicara una caida de dato que no existe.

---

## 3. MI CLASIFICACION DE LOS PARES DE LA TANDA, ANTES DE DESTAPAR NINGUNA RAZON

### 3.1. La tanda, medida sin leer clase ni razon

Saco los pares nuevos de `bitacora/VEREDICTOS.jsonl` **proyectando solo candidato,
vecino, `detalle_paso` y seniales**: el instrumento no imprime `razon` ni `veredicto`.

    veredictos antes de la vuelta 26: 197
    veredictos nuevos de la vuelta 26: 37

    CANDIDATO cambiar_posicion_hechos_explicar_cambio  (1 pares)
    CANDIDATO decidir_momento_despedir_persona  (4 pares)
    CANDIDATO despedir_persona_franqueza_radical  (7 pares)
    CANDIDATO reconocer_recompensar_gente_estable  (3 pares)
    CANDIDATO retar_superestrellas_equipo_constantemente  (9 pares)
    CANDIDATO retirar_etiquetas_permanentes_equipo  (4 pares)
    CANDIDATO revisar_cinco_causas_mal_desempenio  (1 pares)
    CANDIDATO subir_vara_calidad_equipo  (8 pares)

`1 + 4 + 7 + 3 + 9 + 4 + 1 + 8 = 37`. **Los otros CUATRO de los doce entraron con CERO
pares levantados**, y eso es lo que miro de cerca en `5`.

### 3.2. UNA CONTAMINACION MIA, DECLARADA ANTES DE QUE SE NOTE

Al inspeccionar la FORMA de `bitacora/VEREDICTOS.jsonl` con `tail -3` **lei la `razon` y
el `veredicto` de tres pares de esta misma tanda**:

- `subir_vara_calidad_equipo` contra `delimitar_franqueza_radical_cinco_noes`
- `subir_vara_calidad_equipo` contra `pedir_critica_equipo_premiarla`
- `cambiar_posicion_hechos_explicar_cambio` contra `abrir_debate_humor_explicar_proposito`

**Esos tres pares quedan FUERA de mi muestra ciega y no cuentan como relectura mia**, ni
a favor ni en contra del extractor. Lo digo yo, que soy el unico que lo sabe, y va en la
sede sellada para que no pueda retirarse despues.

### 3.3. Mis adjudicaciones ciegas, con la vara de `6.1`

**Cada una se escribio con los pasos ENTEROS de los dos lados delante** (`HEREDADO 3.1`).

| par | mi clase ciega | por que, con la vara |
|---|---|---|
| `despedir_persona_franqueza_radical` contra `despedir_persona_respeto_franqueza` (`fam 0.600`, la senial de familia mas alta de la tanda) | **SANO** | Son **dos actos consecutivos y distintos**: el vecino (`zhuo`) ejecuta la salida ya decidida (directa, sin abrir discusion, sin alargar la ruptura); el candidato (`scott`) **prepara tu cabeza antes de la reunion** con dos recordatorios. Lo que queda fuera del solape **es procedimiento en los dos lados**: el vecino tiene `no lo abras a discusion` y `no alargues la ruptura`; el candidato tiene `imagina concretamente cual podria ser ese trabajo`, `ofrece una presentacion` y el coste sobre los que mas rinden. **Ninguno despliega una linea nombrada del otro.** La familia de id `0.600` es la mas alta que he visto y **no decide nada**: `D.19`, ninguna senial separa jerarquia de ruido |
| `decidir_momento_despedir_persona` contra `elegir_recolocar_despedir_persona` | **SANO**, y por poco no es frontera | El candidato decide **si ha llegado el momento** (tres preguntas, cuatro mentiras); el vecino decide **que haces cuando ya has concluido que no encaja** (recolocar o dejar ir). Estuve a punto de declarar **FRONTERA**: el `paso 11` del candidato llama *tercera mentira: un traslado es la solucion*, y el `paso 2` del vecino dice *considera siempre la primera, ayudar a la persona a encontrar un papel nuevo dentro de tu organizacion*. **No es frontera, y lo que lo cierra es el `paso 4` del propio vecino**: *evita ir barajando por ahi a gente que no tiene las habilidades adecuadas*. **El vecino se pone su propio limite y las dos doctrinas caben.** Lo dejo escrito porque si alguien lee solo el `paso 2` la declara frontera |
| `decidir_momento_despedir_persona` contra `despedir_persona_franqueza_radical` | **SANO de clase, Y ARISTA POR LECTURA que nadie ha cableado** | Ver `4.3` |
| `cambiar_potencial_trayectoria_crecimiento` contra `retirar_etiquetas_permanentes_equipo` | **CONTINUA** | Ver `4.1` |
| `acompaniar_mejores_equipo_socio` contra `reconocer_recompensar_gente_estable` | **CONTINUA** | Ver `4.2` |
| `acompaniar_mejores_equipo_socio` contra `retar_superestrellas_equipo_constantemente` | **CONTINUA** | Ver `4.2` |
| `aprender_resultados_vencer_dos_presiones` contra `cambiar_posicion_hechos_explicar_cambio` | **CONTINUA, y la arista NO esta cableada** | Ver `4.4`. **Este par no tiene veredicto en la bitacora y ninguna senial lo levanta** |
| `reconocer_recompensar_gente_estable` contra `reconocer_excelencia_trayectoria_gradual` (bandeja) | **CONTINUA, y el hijo sigue en la bandeja** | Ver `4.5` |

**Mis tres CONTINUA cableadas coinciden EXACTAMENTE con las tres aristas que la vuelta 26
escribio** (`2.3`), sin haber visto su reporte. **Las otras dos CONTINUA que leo no estan
cableadas.**

---

## 4. LAS ARISTAS, CON LOS DOS LADOS IMPRESOS (`HEREDADO 3` PUNTO 1)

### 4.1. `cambiar_potencial_trayectoria_crecimiento` (madre) contra `retirar_etiquetas_permanentes_equipo` (hijo): **CONTINUA**

**MADRE, 14 pasos, su ultimo:**

    14. No pongas etiquetas permanentes: el texto dice que estas preguntas sirven
        justo para recordarte que las trayectorias cambian.

**HIJO, 10 pasos, los diez:**

     1. cuesta no fijar tus percepciones ... esta persona es de tal manera y siempre lo sera
     2. No uses los nombres de las dos fases como etiquetas permanentes
     3. la gente cambia de verdad: gradual que se pone inquieto, empinada que ansia estabilidad
     4. una razon mas para dirigir de verdad: ajustarse a la realidad nueva
     5. la condicion del ajuste: no puedes ajustarte si no has estado prestando atencion
     6. No etiquetes tampoco por desempenio: todo el mundo tiene un trimestre malo
     7. refiere la puntuacion al periodo y no a la persona: flojo, solido, excepcional
     8. el ajuste mas dificil: mover a quien te hacia la vida facil
     9. Habla con la persona de que esta impulsando su grado de trayectoria
    10. Usa el marco pero no abuses de el ... no metas a la gente en cajas

**LA MADRE NOMBRA EN UNA LINEA LO QUE EL HIJO PROCEDIMENTA EN DIEZ.** Es `P.5.1` en su
forma limpia: *nombrar no es procedimentar*. Y lo que el hijo trae y la madre no tiene en
ningun paso son **las tres puntuaciones de Jared Smith**, **la condicion de atencion** y
**la prohibicion de etiquetar por desempenio**. **CONTINUA.**

### 4.2. `acompaniar_mejores_equipo_socio` (madre) y sus DOS hijos: **CONTINUA las dos**

**MADRE, su `paso 1`:**

    1. ANTES DE DISTINGUIR entre estrellas de rock y superestrellas, atiende a lo que
       las dos necesitan de ti por igual ...

**La madre NOMBRA las dos fases y aplaza.** Cada hijo despliega una:

- `reconocer_recompensar_gente_estable`, 12 pasos, es la **gradual**: puntuacion justa, el
  mecanismo del racionamiento de notas altas, experto de referencia, premios de
  antiguedad, rechazo de `jugador de segunda`, las dos promociones malas.
- `retar_superestrellas_equipo_constantemente`, 13 pasos, es la **empinada**: retos
  nuevos, mentores de fuera, sucesor pensado, las dos salvaguardas del comite y del
  traslado, la via de experto mas prestigiosa que la de jefe.

**Ninguno repite al otro y ninguno repite a la madre. CONTINUA las dos.**

### 4.3. `decidir_momento_despedir_persona` y `despedir_persona_franqueza_radical`: **UNA ARISTA QUE LOS DOS NODOS ESCRIBEN EN SU PROPIA CABECERA Y QUE NADIE CABLEO**

No hace falta leer el libro para verla: **esta en las condiciones de activacion de los
dos ficheros del grafo.**

    decidir_momento_despedir_persona
      activacion : Cuando alguien de tu equipo lo hace mal, no mejora o incluso empeora,
                   y te preguntas si ha llegado el momento de despedirle.
      entregable : ... y LA DECISION TOMADA sabiendo cual de las cuatro mentiras estabas
                   a punto de creerte.
      previos    : []
      siguientes : []

    despedir_persona_franqueza_radical
      activacion : CUANDO YA HAS DECIDIDO que tienes que despedir a alguien y te toca
                   preparar y tener esa conversacion.
      previos    : []
      siguientes : []

**El entregable del primero es la condicion de activacion del segundo, escrito con esas
palabras en los dos ficheros, y los cuatro campos de arista de los dos estan VACIOS.**
Los dos entraron en la misma vuelta 26. La clase del par es **SANO** (son dos actos, no
uno), **y la arista `decidir_momento_despedir_persona > despedir_persona_franqueza_radical`
la levanta la lectura y no la senial.** La traigo adjudicada al turno normal.

### 4.4. `aprender_resultados_vencer_dos_presiones` (madre) contra `cambiar_posicion_hechos_explicar_cambio` (hijo): **CONTINUA, y el libro la escribe con rotulo**

**MADRE, 6 pasos, el sexto:**

    6. Vence LAS DOS ENORMES PRESIONES que el texto dice que tentaban a la autora a
       dejar de aprender cuando dirigia un equipo grande: LA PRESION DE SER COHERENTE,
       y EL AGOTAMIENTO.

**HIJO, 9 pasos, los nueve:** veleta, erratico o sin principios; Keynes; la comunicacion
es la clave; la queja razonable de los dos meses; no cambies de rumbo a la ligera; prepara
la explicacion clara y convincente; vuelve a pasar por escuchar, clarificar, debatir y
decidir con un circulo cercano; persuade otra vez con paciencia; **nombra el cambio de
direccion explicitamente**.

**Y EL LIBRO LO ESCRIBE CON ROTULO**, que es `D.37` en su forma mas fuerte:

    $ sed -n '399,410p' fuentes/scott_radical_candor/cap_07.md
    ... I found there were TWO ENORMOUS PRESSURES that tempted me to quit learning.

    Pressure to be consistent
    ...
    Burnout

**La madre nombra DOS, el libro imprime DOS rotulos, y hay DOS candidatos: el hijo que
entro (`cambiar_posicion_hechos_explicar_cambio`, rotulo `Pressure to be consistent`) y el
que sigue en la bandeja (`cuidarse_agotamiento_centro_rueda`, rotulo `Burnout`).** La
arista de la primera **esta vencida hoy y no esta escrita**; la de la segunda vence cuando
entre su nodo.

### 4.5. `reconocer_recompensar_gente_estable` (madre, grafo) contra `reconocer_excelencia_trayectoria_gradual` (hijo, bandeja): **CONTINUA**

**MADRE, su `paso 2`:**

    2. Reconoce su aportacion POR OTRAS VIAS, y el texto NOMBRA VARIAS UNA A UNA: un
       bono o una subida; si les gusta hablar en publico, que presenten en la reunion
       general; si les gusta ensenar, que ayuden a la gente nueva; y si son timidos,
       asegurate de que tu y otros del equipo les DAIS LAS GRACIAS en privado.

**HIJO, 13 pasos**, que procedimentan TRES de las vias que ese paso solo nombra: el
agradecimiento (`1` a `5`, con la distincion elogio contra agradecimiento y el caso de Jim
Ottaway), el experto de referencia (`6` a `11`, con los dos meses para preparar una clase),
y la presentacion a los colegas para quien se siente invisible (`12` y `13`).

**Hay solape real y lo digo: el experto de referencia y `honor y no obligacion` estan en
los dos.** Pero lo que queda fuera **es procedimiento en los dos lados**: la madre tiene
las notas justas, el racionamiento, los premios de antiguedad y las dos promociones malas;
el hijo tiene el agradecimiento entero y la presentacion. **No es gemelo: es CONTINUA.**

---

## 5. LO QUE NINGUNA SENIAL LEVANTO, Y POR QUE ESO TIENE UNA CAUSA DE CODIGO

### 5.1. Mi medida dirigida, con la senial de la casa

`.v27/medida_dirigida_v27.py` corre **`aduana.medir`, la funcion de la casa**, con los
umbrales de `config/umbrales.json`, sobre una poblacion que declaro: los vecinos que mi
lectura del capitulo senala. **Recortar la poblacion mide menos, no distinto: lo que
supera umbral, supera umbral.**

    umbrales: similitud 0.35 | familia 0.30 | paso_contra_nodo 0.60

    adaptar_escucha_cultura_ajena
       crear_cultura_escucha_equipo          [BANDEJA] fam 0.333 -> LEVANTA (familia_id)       sin veredicto
    abrir_debate_humor_explicar_proposito
       parar_debate_emocion_agotamiento      [BANDEJA] sim 0.392 -> LEVANTA (similitud_texto)  sin veredicto
       fijar_fecha_cierre_debate_equipo      [BANDEJA] sim 0.372 -> LEVANTA (similitud_texto)  sin veredicto
    bajar_detalle_organizacion_fuente_hechos
       repartir_decision_cercanos_hechos     [BANDEJA] pxn 0.664 -> LEVANTA (paso_contra_nodo) sin veredicto
    cambiar_posicion_hechos_explicar_cambio
       cuidarse_agotamiento_centro_rueda     [BANDEJA] sim 0.365 -> LEVANTA (similitud_texto)  sin veredicto
       abrir_debate_humor_explicar_proposito [GRAFO  ] sim 0.377 -> LEVANTA (similitud_texto)  con veredicto

    PARES MEDIDOS QUE SUPERAN ALGUN UMBRAL: 6

**CINCO pares por encima de umbral SIN veredicto, y los cinco tienen un extremo en la
bandeja.** El sexto, el unico con los dos extremos en el grafo, **si tiene veredicto**.
El patron no es casual, y su causa esta en `5.3`.

### 5.2. La cola heredada, remedida al digito (`HEREDADO 1`, cola del hueco)

Mi encargo decia que `decidir_momento_despedir_persona` debia **4** pares con cuatro
nombres. El instrumento de `3.1`, que no lee razon ni clase, saca exactamente:

    CANDIDATO decidir_momento_despedir_persona  (4 pares)
       vs despedir_persona_franqueza_radical
       vs pedir_critica_equipo_premiarla
       vs despedir_persona_respeto_franqueza
       vs elegir_recolocar_despedir_persona

**Cuatro, y los cuatro nombres.** La cifra que costo la parada de la vuelta 25 esta
pagada al digito.

### 5.3. **LA CAUSA: `D.38.5` DICE `TAMBIEN PARA LA ADUANA` Y LA ADUANA NO LA CUMPLE**

Esto no lo deduzco: lo leo en las dos sedes y lo corro.

**LO QUE LA REGLA MANDA**, `docs/BANCO_DE_REGLAS.md` linea 1573:

    ### D.38.5. LA POBLACION DEL BARRIDO ES GRAFO MAS BANDEJAS **TAMBIEN PARA LA ADUANA**
    ...
    | **el barrido de vecinos** (las tres seniales) | **grafo mas bandejas** |
    | **la guarda `el id ya vive en el grafo`**     | **solo el grafo.** ...

**LO QUE EL CODIGO HACE.** El informe en seco, `src/informe.py`:

    222:    poblacion = list(nodos) + list(bandejas)

    $ python forja.py informe cuarentena/scott_radical_candor/cuidarse_agotamiento_centro_rueda.json
    poblacion del barrido       : 348   (234 del grafo mas 114 que esperan en bandejas)

**La insercion de verdad, `src/aduana.py`**, que es la que corre `python forja.py insertar`:

    785:    nodos = comun.leer_jsonl(ruta_dataset)
    797:    vecinos = buscar_vecinos(candidato, nodos, umbrales)
    799:    resultado.decir("  blocking multi senial contra %d nodo(s) del dataset" % len(nodos))

**No hay ni una llamada a `poblacion_de_bandejas` en `src/aduana.py`:**

    $ grep -n "poblacion_de_bandejas" src/aduana.py
    (cero coincidencias)

> **EL INFORME MIDE 348 Y LA INSERCION MIDE 234.** La mitad de `D.38.5` que llego al
> arbol es la del informe; **la mitad que da titulo a la regla, la aduana, no llego.**

**EL EJEMPLAR CONCRETO Y DE ESTA VUELTA:** cuando `cambiar_posicion_hechos_explicar_cambio`
entro, la aduana lo midio contra `234` y no vio a `cuidarse_agotamiento_centro_rueda`,
que estaba en la bandeja. Con los `348` que `D.38.5` manda, **lo habria levantado**: la
senial da `0.365` en un sentido y el informe de la casa da `0.402` en el otro:

    $ python forja.py informe .../cuidarse_agotamiento_centro_rueda.json
    [BLOQUEARIA] cuidarse_agotamiento_centro_rueda
        vecino cambiar_posicion_hechos_explicar_cambio  [levantada por: similitud_texto]
          similitud_texto 0.402 | familia_id 0.000 | paso_contra_nodo 0.456

**LO CLASIFICO ASI, y la adjudicacion va al turno normal:** el par **no se pierde**, se
**aplaza** hasta que entre el segundo, porque entonces el primero ya vive en el grafo.
Pero `D.38.5` nacio precisamente para que un par no dependa de que alguien se acuerde, y
su propio texto lo dice: *un par que solo se ve si alguien se acuerda de mirarlo no esta
guardado*. **Y esto no es caida de la vuelta 26: lleva sin cumplirse desde que la regla se
escribio, el 12 sep.**

### 5.4. Lo que mi lectura levanta y NINGUNA senial ve, y lo digo para no inflar el hallazgo

Medi diez pares mas, grafo contra bandeja, con la misma funcion de la casa:

    DE LOS 10 PARES MEDIDOS, SUPERAN UMBRAL: 0

Entre ellos **el `CONTINUA` de `4.5`**: `reconocer_recompensar_gente_estable` contra
`reconocer_excelencia_trayectoria_gradual` mide `fam 0.143 pxn 0.462 sim 0.201` y **no
levanta**. **Esa arista es de lectura pura (`D.19`, `D.29`) y no tiene nada que ver con
`5.3`.** Separo las dos cosas a proposito: la primera es una regla que el codigo no
cumple, la segunda es el trabajo normal de leer.

---

## 6. `HEREDADO 3` PUNTO 4, CORRIDO: **SIETE DE LOS OCHO ENCARGOS DE LA `ACTA 25` NO ESTAN EN EL ENCARGO QUE LA VUELTA 26 RECIBIO**

Es el remedio del que mi propia acta dice que *es la unica de las cuatro que ya fallo una
vez sin que nadie la viera, y se comprueba con un comando, no con la memoria*. Lo corro
desde fichero, contra los ocho puntos de `ACTA 25` `11.1`:

    $ sh .v27/grep_encargos_v27.sh
    fichero: docs/loop/PROMPT_SIGUIENTE.md   (127 lineas)

    1   ESTA     grep -c -i "tallado" -> 1
    2   ESTA     grep -c -i "despedir_persona_franqueza_radical" -> 1
    2b  NO ESTA  grep -c -i "reconocer_recompensar_gente_estable" -> 0
    3   NO ESTA  grep -c -i "resumen_teorico" -> 0
    4   NO ESTA  grep -c -i "cambiar_forma_trabajar_conservar_plantilla" -> 0
    5   NO ESTA  grep -c -i "cap_04" -> 0
    6   NO ESTA  grep -c -i "QUESTIONS TO CONSIDER" -> 0
    7   NO ESTA  grep -c -i "recorrer_rueda" -> 0
    8   ESTA     grep -c -i "decidir_momento_despedir_persona" -> 1

**Y LAS DOS QUE `ESTAN` HAY QUE MIRARLAS, PORQUE UN `grep` QUE ACIERTA POR CASUALIDAD ES
PEOR QUE UNO QUE FALLA:**

    $ grep -n -i "tallado" docs/loop/PROMPT_SIGUIENTE.md
    51:**Al cerrar la vuelta:** `python scripts/cerrar_reporte.py`, que corre el tallado

    $ grep -n "despedir_persona_franqueza_radical" docs/loop/PROMPT_SIGUIENTE.md
    85:`despedir_persona_franqueza_radical`, `pedir_critica_equipo_premiarla`,

**Ninguna de las dos es su encargo.** La linea `51` manda correr el cierre, **no** manda
que la celda del tallado diga contra que version se corrio (punto 1). La linea `85` es la
lista de la cola heredada, **no** el encargo de corregir el candidato del ancla en la
bandeja (punto 2).

> **ASI QUE LA CUENTA DE VERDAD ES: DE LOS OCHO PUNTOS ADJUDICADOS, UNO SOLO VIAJO
> (`el 8`, la cola que es `4` y no `2`). SIETE NO.**

**Y NO ES QUE EL FUNDADOR LOS RETIRARA.** Su decision del 15 sep los nombra uno a uno y
dice lo contrario:

    $ sed -n '250,254p' docs/loop/paradas/2026-09-15-la-ruta-vacia-DECISION.md
    3. **El trabajo adjudicado ya esta decidido y no hay que rehacerlo.** Los ocho puntos
       estan escritos y listos para pegar en `ACTA 25` `11.1`: la celda del tallado con su
       version, los dos candidatos del ancla que se corrigen en la bandeja, la operacion
       escrita para los dos que ya viven en el grafo, el puente `Pide`, `cap_04` releido
       antes que el hueco, las `QUESTIONS TO CONSIDER` que no son nodo, la correccion 9 al
       reves, y la cola de `decidir_momento_despedir_persona` que es `4` y no `2`.

**`PROMPT_SIGUIENTE.md` ES SEDE MIA** (`AUDITOR_FORJA.md` `5.6`) **y su propia cabecera
dice que la reescribi yo**. Asi que esto no se lo cuelgo a nadie: **lo clasifico como
caida propia candidata a `REMEDIO ROTO`**, y su adjudicacion exacta (si cuenta, y contra
que tanda) la escribo en el acta, con la regla delante. **Lo que queda cerrado aqui es
que el remedio se corrio y que caza lo que vino a cazar.**

**Y HAY UN AGRAVANTE QUE ME TOCA DECIR:** el punto 2 mandaba corregir en la bandeja
`despedir_persona_franqueza_radical` y `reconocer_recompensar_gente_estable`. **Los dos
entraron al grafo en la vuelta 26** (`2.2`). Si la correccion no viajo al encargo, **entro
sin ella**, y comprobarlo es lo primero de mi turno normal.

---

## 7. LA MUESTRA PINEADA: SEMILLA Y TAMANIO ESCRITOS AHORA, ANTES DE VER UNA SOLA CLASE

`HEREDADO 3` punto 5 manda subir la muestra a su techo cuando la poblacion lo permite. La
poblacion de la tanda esta medida en `3.1` y es **37 pares**. La regla de `7` es *el mayor
entre TRES y el 20 por ciento, con techo de VEINTE*.

| | |
|---|---:|
| pares de la tanda (`3.1`) | **37** |
| menos los tres que contamine yo (`3.2`) | **34** |
| 20 por ciento de 34 | **6,8**, que subo a **7** |
| el mayor entre 3 y 7 | **7** |
| techo de `7` del protocolo | 20, no muerde |
| **semilla, escrita aqui y sellada** | **`27`** |

La eleccion sera `random.Random(27).sample(<los 34 pares ordenados por candidato y luego
por vecino>, 7)`, y ese orden lo fija el mismo instrumento de `3.1`. **Escribir la semilla
en la sede sellada es lo que impide que la muestra mida lo que yo ya sospecho.**

---

## 8. MIS CORTES CIEGOS DE `cap_06` Y `cap_07`

Los dos capitulos que la vuelta 26 inserto se minaron en vueltas anteriores, asi que su
frontera no es trabajo de esta vuelta. **Los corto igual**, porque es lo que me deja decir
si los doce que entraron cubren lo que el libro pone.

### 8.1. `cap_07` (`Cap. 4, Drive Results Collaboratively`)

    $ python .v27/frontera_cap07_v27b.py
    cuerpo del capitulo : L8 a L420
    palabras del cuerpo : 13390
    palabras del fichero: 13706
    A. ROTULOS DE SECCION EN MAYUSCULAS: 9
    B. ROTULOS DE RETORICA (cascara): 3
    C. TITULILLOS DE CUERPO, que son las piezas que pueden dar nodo: 26
    MI CORTE: 26 piezas de cuerpo (C), bajo 9 rotulos de seccion (A).

**Los nueve rotulos son los siete pasos de la rueda** (`LISTEN`, `CLARIFY`, `DEBATE`,
`DECIDE`, `PERSUADE`, `EXECUTE`, `LEARN`) **mas las dos cabeceras de apertura.** De las
**26** piezas, **tres son cascara** que solo presentan a la siguiente (`Be clear in your
own mind`, `Be clear to others`, `The rock tumbler`), asi que **mi corte es 23 piezas con
nodo posible**.

Los **cinco** de `cap_07` que entraron en la vuelta 26 caen asi:

| pieza del libro | nodo |
|---|---|
| `L155 Adapt to a culture of listening` | `adaptar_escucha_cultura_ajena` |
| `L239 Use humor and have fun` | `abrir_debate_humor_explicar_proposito` |
| `L295 Go spelunking` mas `L291 The decider should get facts` | `bajar_detalle_organizacion_fuente_hechos` |
| `L389 LEARN` (el rotulo, no un titulillo) | `aprender_resultados_vencer_dos_presiones` |
| `L403 Pressure to be consistent` | `cambiar_posicion_hechos_explicar_cambio` |

### 8.2. `cap_06` (`Cap. 3, Understand What Motivates Each Person on Your Team`)

    $ python .v27/frontera_cap06_v27.py
    palabras del cuerpo : 11587
    A. ROTULOS DE SECCION EN MAYUSCULAS: 14
    C. TITULILLOS DE CUERPO: 28

**Mi corte limpia esas 28:** `L25`, `L47` y `L193` son separadores `* * *`; `L31` a `L41`
son las **seis palabras de las dos columnas** del ejercicio, no piezas; `L359` ya es el
capitulo siguiente. **Quedan 18 piezas de cuerpo.**

Los **siete** de `cap_06` que entraron caen en las **siete ultimas**, que es lo que hace
creible que el capitulo cierre:

| pieza del libro | nodo |
|---|---|
| `L133 Recognize, reward, but don't promote` (mas `L155`, `L161`, `L177`, `L185`) | `reconocer_recompensar_gente_estable` |
| `L199 Keep superstars challenged` (mas `L219`, `L229`) | `retar_superestrellas_equipo_constantemente` |
| `L245 Raise the bar, there's no such thing as a B-player` | `subir_vara_calidad_equipo` |
| `L263 Part ways` | `decidir_momento_despedir_persona` |
| `L293 Be Radically Candid with the person you're firing` | `despedir_persona_franqueza_radical` |
| `L311`, `L323`, `L331`, `L337` (las cuatro causas) | `revisar_cinco_causas_mal_desempenio` |
| `L345 People change, and you have to change with them` | `retirar_etiquetas_permanentes_equipo` |

**El `nombre_largo` de `despedir_persona_franqueza_radical` lleva el rotulo del libro
dentro**, y eso es una comprobacion gratis:

    "otros_idiomas": [{"idioma": "ingles",
                       "termino": "be Radically Candid with the person you are firing"}]

---

## 9. `PASOS INVENTADOS`: LO QUE FIRMO A CIEGAS, LEIDO CONTRA SU PARRAFO

`AUDITOR_FORJA.md` `8.3` me manda **releer una muestra de los pasos marcados
TRANSCRIPCION contra su parrafo**, porque *el error que esta metrica invita a cometer es
marcar un puente como transcripcion*. Lo hago con cuatro nodos de los doce, paso a paso
contra la linea del libro:

| nodo | pasos | PUENTE que encuentro | linea del libro |
|---|---:|---:|---|
| `retirar_etiquetas_permanentes_equipo` | 10 | **0** | `cap_06` `L347` a `L355` |
| `abrir_debate_humor_explicar_proposito` | 7 | **0** | `cap_07` `L241` y `L243` |
| `aprender_resultados_vencer_dos_presiones` | 6 | **0** | `cap_07` `L395` a `L401` |
| `cambiar_posicion_hechos_explicar_cambio` | 9 | **0** | `cap_07` `L405` y `L407` |
| **total de mi muestra** | **32** | **0** | **0,00 por ciento** |

**Los cuatro los he leido paso por paso contra su parrafo, no por encima.** Dos ejemplos
del calce, que es lo que sostiene la cifra:

    paso 7 de retirar_etiquetas ... refiere la puntuacion al periodo y no a la persona:
      trimestre flojo, trimestre solido y trimestre excepcional
    cap_06 L349 ... Jared Smith came up with the performance ratings "off quarter,"
      "solid quarter," and "exceptional quarter."

    paso 9 de cambiar_posicion ... Nombra el cambio de direccion explicitamente en vez de
      dejar que se note
    cap_07 L407 ... and to call out the change in direction explicitly.

**NO FIRMO LA CIFRA DEL LOTE NI LA DE LOS CAPITULOS ENTEROS**, porque no he leido los doce
nodos paso a paso. **Firmo esta: 32 pasos releidos contra su parrafo, 0 puentes.**

---

## 10. UNA COSA QUE NO ENCUENTRO, Y QUE AFECTA A UNA CIFRA QUE TENGO QUE FIRMAR

`AUDITOR_FORJA.md` `8` me obliga a publicar `PASOS INVENTADOS` **con una fila por
capitulo**. Al buscar de que capitulo es cada nodo, me encuentro con esto:

    $ censo de campos sobre los 234 nodos del grafo
    condiciones_activacion 234 | denominaciones 234 | dominio 234 | entregable_esperado 234
    estado 234 | fuentes 234 | id 234 | ids_alias 234 | nodos_previos 234
    nodos_siguientes 234 | pasos_accionables 234 | resumen_teorico 234 | titulo 234
    escala_minima 132 | atribuciones 59 | marco_pais 2
    nodos con citas o registro_citas: 0

    $ el mismo censo sobre un candidato de la bandeja
    CLAVES: condiciones_activacion, denominaciones, dominio, entregable_esperado, estado,
            fuentes, id, ids_alias, nodos_previos, nodos_siguientes, pasos_accionables,
            resumen_teorico, titulo

**Ningun nodo del grafo y ningun candidato de la bandeja dice de que capitulo sale.** Lo
unico que hay es `fuentes[].clave` y `fuentes[].fecha`, y la fecha no sirve de sustituto:

    FECHA DE LECTURA DE LOS 142 CANDIDATOS DEL LOTE 4 (campo fuentes[].fecha)
    fecha           grafo  bandeja    total
    2026-09-11          8        0        8
    2026-09-12         23       82      105
    2026-09-13          0       29       29
    TOTAL              31      111      142

**105 de 142 comparten fecha.** Asi que la atribucion de capitulo **vive solo en la prosa
del reporte y de mis actas**, y una cifra por capitulo que solo se puede recomponer
leyendo prosa **no se puede re verificar despues por nadie**. Lo clasifico y lo traigo:
**no es caida de la vuelta 26, es un hueco de sede que me afecta a mi, porque `8.3` dice
que la cifra me la da el extractor y la FIRMO YO.**

---

## 11. RESUMEN DE MI CLASIFICACION CIEGA

| lo que clasifico | mi lectura |
|---|---|
| **los 12 que entraron** | **12**, contados del arbol contra `f52f77e`, cuadrando por los cuatro lados |
| **las 3 aristas cableadas** | **las TRES son `CONTINUA` y coinciden con mi lectura ciega**, sin haber visto el reporte |
| **aristas que leo y NO estan cableadas** | **2**: `aprender_resultados > cambiar_posicion` (`4.4`) y `decidir_momento > despedir_persona` (`4.3`). Una tercera vence cuando entre su nodo (`4.5`) |
| **mis clases ciegas de par** | **8 adjudicadas**, 3 excluidas por contaminacion propia declarada (`3.2`) |
| **pares sobre umbral sin veredicto** | **5**, los cinco con un extremo en bandeja (`5.1`) |
| **la causa de esos 5** | **`src/aduana.py` mide 234 donde `D.38.5` manda 348** (`5.3`) |
| **la cola heredada** | **4 y los cuatro nombres. Pagada al digito** (`5.2`) |
| **`PASOS INVENTADOS` de mi muestra** | **32 pasos releidos, 0 puentes, 0,00 por ciento** (`9`) |
| **mi corte de `cap_07`** | **26 piezas de cuerpo, 23 con nodo posible, 13.390 palabras** (`8.1`) |
| **mi corte de `cap_06`** | **18 piezas de cuerpo, 11.587 palabras** (`8.2`) |
| **guardas** | gate, guiones, resolutor y vigencia **en VERDE**; `test_aceptacion` en **ROJO por la propia fase ciega** (`1.3`) |
| **`HEREDADO 3` punto 4** | **corrido, y caza 7 de 8 encargos perdidos** (`6`) |
| **caida propia que declaro** | **contaminacion de 3 pares** (`3.2`) y **candidata a `REMEDIO ROTO`** por `6` |

**NO HE ABIERTO `REPORTE.md`, `loop.log`, `ultimo_extractor.json` NI `ultimo_auditor.json`,
y no los he recuperado de git.** Lo que sigue lo comparo en el turno normal.

    ACTA ANTERIOR LEIDA: 4adfa30e9d4fc5a15f370795e0124fe98c394356
    HEREDADO 1: CUMPLIDO
    HEREDADO 2: CUMPLIDO
    HEREDADO 3: CUMPLIDO
