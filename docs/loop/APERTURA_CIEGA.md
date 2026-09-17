# APERTURA CIEGA DE LA VUELTA 34, lote 4 (`scott_radical_candor`), tramo de `cap_09`

*Escrita ANTES de ver `docs/loop/REPORTE.md`, que el arnes retiro del arbol junto con
`loop.log`, `ultimo_extractor.json`, `ultimo_auditor.json` y, desde `D.52`, tambien
`CREDITO_serial.jsonl`. **No he recuperado ninguno de ellos de `git` ni por ninguna otra
via.*** Lo que si he abierto, y `AUDITOR_FORJA.md` 1.5 lo autoriza por su nombre, es
`docs/loop/ACTA_AUDITOR.md`, que es obra mia.

---

## 0. LA LINEA DE LECTURA (`D.40`)

**ACTA ANTERIOR LEIDA: 3b176db2f9bbb25f92a76a0cfff0a365c30d5822**

**HEREDADOS: `0`.** No hay `HEREDADO 1` que declarar porque el instrumento de la casa
entrega **cero**, y esa cuenta no la pongo yo:

    $ python forja.py herencia
      acta anterior : ACTA 32. VUELTA 33, lote 4 (`scott_radical_candor`), **`cap_08` CERRADO
                      EN INSERCION, `12` de `12`**: ...
      su huella     : 3b176db2f9bbb25f92a76a0cfff0a365c30d5822
      heredados     : 0

      El acta anterior no dejo ninguna tarea bloqueante ni ningun remedio escrito. Aun asi
      tienes que declarar la linea de lectura.

**LA HUELLA QUE DECLARO ES LA QUE EL PROMPT ME ENTREGA Y LA QUE EL INSTRUMENTO IMPRIME, Y
SON LA MISMA.** Y he leido la `ACTA 32` en el arbol, no de memoria: su cabecera, su
seccion `6` (mi caida propia de aquella tanda) y su seccion `9`, que es donde mi antecesor
dejo escrito que **no dejaba remedio ninguno**.

> **LO QUE ESTO NO ES:** no es que la vuelta anterior no me encargase nada **a mi**. Es que
> el acta no escribio ninguna fila de `REMEDIO`, y por eso `forja.py herencia` entrega `0`.
> **Lo que si heredo, y no por la via de `D.40`, es una racha propia en `1 de 3`** (`ACTA 32`
> `9.1`, fila `AUDITOR`). Eso pesa sobre la seccion `8` de este documento.

---

## 1. HUECO DE ACTA (`AUDITOR_FORJA.md` 1.0): **MEDIDO, Y NO LO HAY**

    $ grep -n "^# ACTA " docs/loop/ACTA_AUDITOR.md | tail -1
      28473:# ACTA 32. VUELTA 33, lote 4 (scott_radical_candor), cap_08 CERRADO EN INSERCION,
             12 de 12 ...

    $ git log --oneline -8
      3dbc901 V.34 CIERRE: cap_09 entra 15 de 15 del tramo, las tres tareas cerradas, ...
      1a356dd V.34 TAREA 2 (3 de 3): cierra el tramo de cap_09 con 15 de 15 insertados, 282 a 297
      2cce7b5 V.34 TAREA 2 (2 de N): entran cuatro mas de cap_09, ...
      e484b6e V.34 TAREA 2 (1 de N): entran los siete primeros de cap_09 por el orden del libro
      0fc22c9 V.34 TAREA 3: la relectura de fidelidad de los 15 de cap_09 corrida ANTES de insertar
      1054e06 V.34 TAREA 1: el nodo que declaraba tres capitulos sin minar, corregido por D.13 ...
      b698aef Apertura de la vuelta 34: el esqueleto del reporte abierto antes de la primera tarea
      6315b30 Apertura de la vuelta 34: el registro del arnes de la vuelta previa entra antes de
              tocar nada

**La `ACTA 32` cubre la vuelta 33 y la que audito es la 34, que es la inmediatamente
siguiente. CERO vueltas sin acta.**

---

## 2. LAS GUARDAS DE LA CASA, CORRIDAS POR MI EN ESTA FASE

*`D.46`: una cifra vale en el instante en que se sella. Estas son de ahora.*

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 297
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python forja.py resolutor
    nodos vivos: 297
    nodos deprecados (archivo): 0
    alias registrados: 0

    $ python forja.py rancios | head -3      (los 48 hallazgos, enteros, en .v34aud/rancios_completo.txt)
    BLOQUE DE VIGENCIA: 48 hallazgo(s) sobre 409 veredicto(s) y 0 cita(s).
      RANCIO 40, SIN HUELLA 8
      lineas declaradas NO CONSUMADAS y por eso no medidas: 14

**`gate`, `guiones` y `resolutor` en VERDE sobre `297` nodos.** El bloque de vigencia
(`rancios`) da `48` hallazgos sobre `409` veredictos medidos, y **`D.15` dice literalmente
que la vigencia NO pone nada en rojo**: se cita aqui como estado, no como caida. Los `409`
mas los `14` declarados NO CONSUMADOS son las `423` lineas del fichero, y esa suma la
comprueba la tabla de la seccion 3.

### 2.1. **LAS PRUEBAS DE ACEPTACION DAN `3` FALLOS, Y NO LOS PUBLICO COMO CAIDA DE LA VUELTA**

    $ python tests/test_aceptacion.py   (cola)
      D.52, dataset es el catalogo y el cerrojo vive fuera: 7 pruebas mas
      D.52, la cita del credito es referencia y no resultado: 10 pruebas mas
      D.52, la cola de doctrina vive en el tablero: 5 pruebas mas

      total: 274 pruebas, 3 fallos, 0 errores
    ========================================================================

    $ grep -n 'FAIL:' .v34aud/aceptacion_full.txt
    433:FAIL: test_caso_positivo_un_frente_recien_nacido_hereda_cero (__main__.PruebaHerenciaPorLinea.test_caso_positivo_un_frente_recien_nacido_hereda_cero)
    460:FAIL: test_el_aviso_nombra_la_linea_y_su_registro (__main__.PruebaHerenciaPorLinea.test_el_aviso_nombra_la_linea_y_su_registro)
    469:FAIL: test_la_linea_serial_del_repo_tiene_su_registro_escrito (__main__.PruebaHerenciaPorLinea.test_la_linea_serial_del_repo_tiene_su_registro_escrito)

**LA MEDIDA ES ESA: `274` pruebas, `3` fallos, `0` errores.** Y ahora la conclusion, aparte
y marcada, porque `D.38.3` ensanchada manda separarlas:

> **`LECTURA`: LOS TRES FALLOS SON DE LA FASE, NO DE LA VUELTA.** Los tres viven en
> `PruebaHerenciaPorLinea` y los tres se resuelven por `src/credito.lineas_con_registro()`
> y `src/credito.nacida()`, que leen `docs/loop/CREDITO_*.jsonl`. **El arnes retira ese
> fichero durante mi fase ciega (`D.52`)**, y con el fuera la serial se comporta como una
> linea recien nacida, que es justo lo que las tres pruebas comprueban que NO pase.

    $ git ls-tree --name-only HEAD docs/loop/ | grep CREDITO
    docs/loop/CREDITO_serial.jsonl

    $ git status --short docs/loop/
     D docs/loop/APERTURA_CIEGA.md
     D docs/loop/CREDITO_serial.jsonl
     D docs/loop/REPORTE.md
     D docs/loop/loop.log
     M docs/loop/ultimo_apertura.json
     D docs/loop/ultimo_auditor.json
     D docs/loop/ultimo_extractor.json

    $ python -c "from src import credito; print(credito.lineas_con_registro()); print(credito.nacida(credito.LINEA_SERIAL))"
    lineas_con_registro(): []
    nacida(serial): False

    $ ls docs/loop/CREDITO_serial.jsonl
    ls: cannot access 'docs/loop/CREDITO_serial.jsonl': No such file or directory

**EL FICHERO ESTA EN `HEAD` Y NO ESTA EN EL ARBOL: lo quito el arnes, no la vuelta. NO LO
RECUPERO**, y por eso **no firmo la suite ni en verde ni en rojo en esta fase**: la vuelvo
a correr en mi turno normal con el registro devuelto, y esa sera la cifra que publique. Lo
digo aqui para que nadie lea ese `274 / 3` como un resultado de la vuelta 34.

---

## 3. MI RECUENTO DEL DATO, ANTES Y DESPUES, HECHO SOBRE EL FICHERO

*Base `b698aef`, que es el ultimo commit antes de la primera tarea. Las dos columnas son
recuentos mios, no lecturas de ninguna tabla ajena.*

*Salida de `python .v34aud/tabla_cifras.py`, guardada en `.v34aud/tabla_cifras.txt`.*

| pieza | **yo, sobre `b698aef`** | **yo, sobre el arbol de hoy** |
|---|---:|---:|
| nodos en `dataset/nodos.jsonl` | **282** | **297** |
| pasos del grafo entero | **2283** | **2464** |
| lineas en `bitacora/VEREDICTOS.jsonl` | **410** | **423** |
| veredictos con `consumada == False` | **14** | **14** |
| aristas por `nodos_siguientes` | **107** | **108** |
| aristas por `nodos_previos` | **107** | **108** |
| candidatos en bandeja, lote 4 | **63** | **48** |
| archivados en `_insertados`, lote 4 | **79** | **94** |
| candidatos en bandeja, lote 5 | **3** | **3** |
| nodos que citan `cap_09.md` | **0** | **15** |
| pasos de los nodos de `cap_09` | **0** | **181** |
| lote 4 insertado sobre `142`, por ciento | **55.63** | **66.20** |

    $ python .v34aud/cifras.py
      TANDA DE LA VUELTA AUDITADA, del dato: 15 ficheros
      pasos de la tanda: 181
      ids NUEVOS en el grafo: 15
      ids QUE DESAPARECEN del grafo: 0 []
      nodos PREEXISTENTES que cambiaron: 1
        ~ construir_confianza_equipo_tiempo_solas
            campo nodos_siguientes
            campo resumen_teorico

**LA TANDA LA SACA `git diff --name-only b698aef HEAD -- cuarentena/_insertados/`, NO UNA
LISTA QUE YO TECLEE.** `2283` mas `181` da los `2464` pasos, entran `15` nodos, `13` lineas
de bitacora y `1` arista por los dos extremos; **cero nodos desaparecidos** y **un solo
nodo preexistente tocado**, que es el de la `TAREA 1`.

### 3.1. LAS SEDES DE DATO, Y QUIEN LAS TOCO

    $ git ls-files procesos/
    (vacio = nada versionado)

    $ grep -n procesos .gitignore
    32:# Commiteado, un checkout entrega un cerrojo de un proceso que ya no existe y la
    34:*.cerrojo
    39:procesos/

    $ git log --oneline --name-only b698aef..HEAD -- dataset/ procesos/ bitacora/ censos/ | head -40
    3dbc901 V.34 CIERRE: cap_09 entra 15 de 15 del tramo, las tres tareas cerradas, y una PARADA en el cierre de D.41 que no es de mi sede
    bitacora/VEREDICTOS.jsonl
    dataset/nodos.jsonl
    1a356dd V.34 TAREA 2 (3 de 3): cierra el tramo de cap_09 con 15 de 15 insertados, 282 a 297 nodos
    bitacora/VEREDICTOS.jsonl
    censos/atribuciones.md
    censos/denominaciones.md
    dataset/nodos.jsonl
    2cce7b5 V.34 TAREA 2 (2 de N): entran cuatro mas de cap_09, con el par que la senial 3 levanta a 0,867 leido y juzgado SANO
    bitacora/VEREDICTOS.jsonl
    censos/denominaciones.md
    dataset/nodos.jsonl
    e484b6e V.34 TAREA 2 (1 de N): entran los siete primeros de cap_09 por el orden del libro, con tres veredictos SANO razonados
    bitacora/VEREDICTOS.jsonl
    censos/denominaciones.md
    dataset/nodos.jsonl
    1054e06 V.34 TAREA 1: el nodo que declaraba tres capitulos sin minar, corregido por D.13 contra la medicion del dia, y la especie barrida entera en los 282 nodos
    bitacora/VEREDICTOS.jsonl
    dataset/nodos.jsonl

> **`LECTURA`, y va marcada:** **el cerrojo de `D.44` ya NO vive dentro de `dataset/`**
> (`D.52`), `procesos/` esta ignorado y `git ls-files dataset/` devuelve **un solo
> fichero**. El ejemplar de `DATO MOVIDO` que la `ACTA 32` cargo en su `5.1` **no se ha
> repetido en esta vuelta**, y lo digo con el listado delante y no de memoria. Lo que
> **queda por mirar en mi turno normal** es el commit de CIERRE `3dbc901`, que toca las dos
> sedes de dato: **un cierre que mueve `dataset/` merece que yo lea su diff**, y lo leo alli.

---

## 4. EL MATERIAL, LEIDO POR MI: **`cap_09` ES `Cap. 6, Guidance`, Y SE REPARTE EN `20` PIEZAS**

    $ for f in fuentes/scott_radical_candor/cap_*.md; do sed -n '2,6p' $f | grep -E "^(unidad|titulo_textual):"; done
      cap_08.md   unidad: Cap. 5   titulo_textual: Relationships
      cap_09.md   unidad: Cap. 6   titulo_textual: Guidance
      cap_10.md   unidad: Cap. 7   titulo_textual: Team
      cap_11.md   unidad: Cap. 8   titulo_textual: Results

*Salida de `python .v34aud/cobertura.py`, guardada en `.v34aud/cobertura.txt`.*

| linea | rotulo del libro | quien lo tiene | donde |
|---:|---|---|---|
| L9 | Ideas for getting/giving/encouraging praise & criticism | **NADIE** | **.** |
| L15 | SOLICITING IMPROMPTU GUIDANCE | **NADIE** | **.** |
| L17 | Embrace the discomfort | `abrazar_incomodidad_arrancar_critica_equipo` (L17 a L53) | **GRAFO** |
| L27 | Here are some tips/techniques I’ve seen work to get the conversation f | dentro de un nodo | . |
| L55 | ORANGE BOX | `organizar_sistema_recoger_quejas_equipo` (L55 a L63) | **GRAFO** |
| L57 | Make it not just safe but natural to criticize you | dentro de un nodo | . |
| L65 | MANAGEMENT “FIX-IT” WEEKS | `correr_semana_arreglo_averias_gestion` (L65 a L71) | **GRAFO** |
| L73 | GIVING IMPROMPTU GUIDANCE | **NADIE** | **.** |
| L77 | Be humble | `dar_guia_humilde_tres_tecnicas` (L77 a L95) | **GRAFO** |
| L81 | Here are some techniques I’ve found helpful to make sure I’m being hum | dentro de un nodo | . |
| L97 | Be helpful | `dar_guia_util_cuatro_recordatorios` (L97 a L113) | **GRAFO** |
| L115 | Give feedback immediately | `dar_guia_acto_seis_consejos` (L115 a L135) | **GRAFO** |
| L137 | In person (if possible) | `elegir_medio_dar_guia_jerarquia_modos` (L137 a L153) | **GRAFO** |
| L155 | Praise in public, criticize in private | `elogiar_publico_criticar_privado_sus_tres_matices` (L155 a L163) | **GRAFO** |
| L165 | Don’t personalize | `evitar_personalizar_guia_aceptar_personal` (L165 a L177) | **GRAFO** |
| L179 | GAUGE YOUR IMPROMPTU GUIDANCE, GET A BASELINE, TRACK YOUR IMPROVEMENTS | `medir_guia_propia_pegatinas_marco` (L179 a L203) | **GRAFO** |
| L205 | BEING RADICALLY CANDID WITH YOUR BOSS | `practicar_franqueza_radical_jefe_propio` (L205 a L221) | **GRAFO** |
| L223 | GENDER AND GUIDANCE | **NADIE** | **.** |
| L227 | Why Radical Candor may be harder for men managing women | **NADIE** | **.** |
| L249 | We must stop gender politics. | **NADIE** | **.** |
| L251 | Why gender bias makes Radical Candor harder for women | **NADIE** | **.** |
| L253 | Gender bias makes it difficult for women to be Radically Candid with b | **NADIE** | **.** |
| L255 | One common bias women often fall prey to: the “Abrasive Trap.” | **NADIE** | **.** |
| L271 | “Jessica is really talented, but I wish she’d be less abrasive. She co | **NADIE** | **.** |
| L273 | “Steve is smart and great to work with. He needs to learn to be a litt | **NADIE** | **.** |
| L285 | What can you do? | **NADIE** | **.** |
| L291 | Men: don’t “pull punches” with women | `comprobar_criticas_hombre_mujeres_equipo` (L291 a L293) | **GRAFO** |
| L295 | Women: demand criticism | `exigir_critica_jefe_reticente` (L295 a L299) | **GRAFO** |
| L301 | Men and women: things to think about when you feel a woman is being “t | `revisar_critica_mujer_agresiva_cuatro_tacticas` (L301 a L313) | **GRAFO** |
| L315 | Things to think about if you’re a woman who’s being told, “You’re abra | `responder_critica_abrasiva_cuatro_reglas` (L315 a L329) | **GRAFO** |
| L331 | FORMAL PERFORMANCE REVIEWS | `entregar_evaluacion_formal_desempenio_nueve_consejos` (L331 a L361) | **BANDEJA** |
| L363 | PREVENT BACKSTABBING | `impedir_punialadas_espalda_equipo` (L363 a L367) | **BANDEJA** |
| L365 | You are a boss, not a diplomat. Shuttle diplomacy won’t work for you. | dentro de un nodo | . |
| L369 | PEER GUIDANCE | `fomentar_guia_reciproca_companieros` (L369 a L381) | **BANDEJA** |
| L383 | SPEAKING TRUTH TO “POWER” | `conducir_reuniones_salto_nivel_diez_reglas` (L383 a L413) | **BANDEJA** |
| L415 | Skip level meeting FAQs | `resolver_dudas_frecuentes_reuniones_salto_nivel` (L415 a L425) | **BANDEJA** |
| L427 | * * * | **NADIE** | **.** |
| L431 | 7. | **NADIE** | **.** |
| L433 | TEAM | **NADIE** | **.** |

lineas del fichero          : 434
lineas dentro de algun nodo : 318
rotulos con nodo propio     : 20  (GRAFO 15, BANDEJA 5)
tramos SIN nodo ninguno, con texto dentro:
  L9 a L9
  L11 a L11
  L13 a L13
  L15 a L15
  L73 a L73
  L75 a L75
  L223 a L223
  L225 a L225
  L227 a L227
  L229 a L229
  L231 a L231
  L233 a L233
  L235 a L235
  L237 a L237
  L239 a L239
  L241 a L241
  L243 a L243
  L245 a L245
  L247 a L247
  L249 a L249
  L251 a L251
  L253 a L253
  L255 a L255
  L257 a L257
  L259 a L259
  L261 a L261
  L263 a L263
  L265 a L265
  L267 a L267
  L269 a L269
  L271 a L271
  L273 a L273
  L275 a L275
  L277 a L277
  L279 a L279
  L281 a L281
  L283 a L283
  L285 a L285
  L287 a L287
  L289 a L289
  L427 a L427
  L429 a L429
  L431 a L431
  L433 a L433

**`20` rotulos con nodo propio: `15` en el grafo y `5` en bandeja.** El corte es el rotulo
de linea, que es el que esta casa lleva usando desde `cap_05`, y **no hay ni un rotulo con
dos nodos ni un nodo a caballo de dos rotulos.**

### 4.1. **EL TRAMO CIERRA EN `L329` POR EL TECHO DE CANDIDATOS, Y LOS `5` QUE QUEDAN TIENEN NOMBRE**

*Salida de `python .v34aud/bandeja_restante.py`, guardada en `.v34aud/bandeja_restante.txt`.*

| # | candidato de `cap_09` que SIGUE EN BANDEJA | lineas del libro | pasos |
|---:|---|---|---:|
| 1 | `entregar_evaluacion_formal_desempenio_nueve_consejos` | L331 a L361 | 22 |
| 2 | `impedir_punialadas_espalda_equipo` | L363 a L367 | 9 |
| 3 | `fomentar_guia_reciproca_companieros` | L369 a L381 | 13 |
| 4 | `conducir_reuniones_salto_nivel_diez_reglas` | L383 a L413 | 31 |
| 5 | `resolver_dudas_frecuentes_reuniones_salto_nivel` | L415 a L425 | 16 |

candidatos de cap_09 en bandeja : 5
candidatos de cap_09 insertados : 15
total del capitulo              : 20   techo de EXTRACTOR.md 12.4: 15

**`20` contra un techo de `15`** (`EXTRACTOR.md` 12.4: *si un solo capitulo pasa del techo
de candidatos, la vuelta cierra en ese capitulo y lo declara*). **Los `15` que entran son
exactamente los `15` primeros por el orden del libro**, de `L17` a `L329`, y **los `5` que
quedan son exactamente los `5` ultimos**, de `L331` a `L425`. **No hay ni un salto de orden.**

> **LO QUE ME TOCA COMPROBAR EN MI TURNO NORMAL** (`AUDITOR_FORJA.md` 8.1, ultimo bloque):
> que el **REPORTE** declare el cierre corto con su cifra. *Una vuelta que cierra en un
> capitulo y no lo dice no esta aplicando esta regla*, y eso seria caida de `REPORTE`. **El
> asunto de un commit NO es sede** (`5.6`), asi que lo que haya leido en `git log` no vale
> como declaracion.

### 4.2. **EL UNICO TRAMO DE `cap_09` QUE NO PRODUCE NI UN CANDIDATO: `L223` a `L289`**

Son treinta y cuatro parrafos bajo `GENDER AND GUIDANCE`. **Los lei enteros.** Lo que hay
dentro:

| linea | que es | procedimiento? |
|---|---|---|
| `L225` a `L247` | el diagnostico de por que a los hombres les cuesta, con el caso de la ecuacion cuadratica y dos anecdotas nominales | **no**: es diagnostico |
| `L249` | *We must stop gender politics.* | **no**: es postura, y la vara dice que **una advertencia es linea, no nodo** |
| `L253` a `L281` | la trampa de lo abrasivo, el estudio de Kieran Snyder y la simulacion de promociones | **no**: es evidencia |
| `L283` | *We must stop this madness, too.* | **no**: postura otra vez |
| `L285` a `L289` | *What can you do?* y su entradilla | **no**: es el anuncio de los cuatro rotulos que SI se extraen (`L291`, `L295`, `L301`, `L315`) |

> **`LECTURA`, marcada aparte: dejarlo fuera es lo que yo habria hecho, y por la misma
> razon.** Todo lo accionable de ese bloque vive en los cuatro rotulos siguientes, y uno de
> sus avisos (*no te creas a salvo por ser mujer*, `L303`) **ya esta dentro** como paso `2`
> de `revisar_critica_mujer_agresiva_cuatro_tacticas`. **Queda `POR ADJUDICAR` contra el
> reporte** si lo declaro como frontera o si simplemente no lo miro.

---

## 5. MI RELECTURA DE FIDELIDAD (`D.30`): **`181` PASOS CONTRA SU LINEA DEL LIBRO**

*Los lei uno a uno con el parrafo delante, no por muestra. Cada nodo se imprimio con sus
lineas de `fuentes/scott_radical_candor/cap_09.md` al lado, con `python .v34aud/leer.py`.*

*Salida de `python .v34aud/fidelidad.py`, guardada en `.v34aud/fidelidad.txt`.*

| # | nodo | lineas del libro | pasos | **TRANSCRIPCION (yo)** | **PUENTE (yo)** | paso |
|---:|---|---|---:|---:|---:|---|
| 1 | `abrazar_incomodidad_arrancar_critica_equipo` | L17 a L53 | 20 | 20 | **0** | . |
| 2 | `organizar_sistema_recoger_quejas_equipo` | L55 a L63 | 9 | 9 | **0** | . |
| 3 | `correr_semana_arreglo_averias_gestion` | L65 a L71 | 8 | 8 | **0** | . |
| 4 | `dar_guia_humilde_tres_tecnicas` | L77 a L95 | 15 | 15 | **0** | . |
| 5 | `dar_guia_util_cuatro_recordatorios` | L97 a L113 | 10 | 10 | **0** | . |
| 6 | `dar_guia_acto_seis_consejos` | L115 a L135 | 14 | 14 | **0** | . |
| 7 | `elegir_medio_dar_guia_jerarquia_modos` | L137 a L153 | 13 | 13 | **0** | . |
| 8 | `elogiar_publico_criticar_privado_sus_tres_matices` | L155 a L163 | 9 | 9 | **0** | . |
| 9 | `evitar_personalizar_guia_aceptar_personal` | L165 a L177 | 12 | 12 | **0** | . |
| 10 | `medir_guia_propia_pegatinas_marco` | L179 a L203 | 13 | 13 | **0** | . |
| 11 | `practicar_franqueza_radical_jefe_propio` | L205 a L221 | 17 | 16 | **1** | P13 |
| 12 | `comprobar_criticas_hombre_mujeres_equipo` | L291 a L293 | 6 | 6 | **0** | . |
| 13 | `exigir_critica_jefe_reticente` | L295 a L299 | 9 | 9 | **0** | . |
| 14 | `revisar_critica_mujer_agresiva_cuatro_tacticas` | L301 a L313 | 12 | 12 | **0** | . |
| 15 | `responder_critica_abrasiva_cuatro_reglas` | L315 a L329 | 14 | 14 | **0** | . |
| | **cap_09, total** | **L17 a L329** | **181** | **180** | **1** | |

PASOS INVENTADOS POR CAPITULO (AUDITOR_FORJA.md 8), leido por mi:
  cap_09 : 1 de 181 = 0.55 por ciento
  tope de la regla 8.1: 10 por ciento

### 5.1. **EL UNICO PASO QUE NO ME SALE `TRANSCRIPCION`, CON LAS DOS LINEAS ENFRENTADAS**

`practicar_franqueza_radical_jefe_propio`, paso `13`. **El libro, linea `215`:**

    If they react well and reward the candor, keep going. If they don't, give up
    immediately or assume ill intent. Try again, carefully, but if you get the same
    reaction the next time, it may be time to move on. You deserve a better boss.

**El paso que entro en el grafo:**

    13. Si reacciona bien y premia la franqueza, sigue. Si no, para inmediatamente, y no
        des por supuesta la mala intencion: vuelve a intentarlo con cuidado, y si la
        segunda vez la reaccion es la misma, puede que sea momento de irse.

**LO QUE NO CUADRA, DICHO EN UNA LINEA: el libro escribe `or assume ill intent` y el paso
escribe `y NO des por supuesta la mala intencion`.** La negacion no esta en `L215`.

> **`LECTURA`, marcada aparte, y con la tension dicha en vez de escondida:** **la frase del
> libro se contradice a si misma.** *Give up immediately* y *Try again, carefully* no pueden
> ser las dos, asi que `L215` es casi con seguridad una errata por *don't give up
> immediately or assume ill intent*, que es la unica lectura que deja el parrafo coherente y
> que ademas concuerda con `L211`, *assume good intent*. **El paso no elige ninguna de las
> dos lecturas: se queda con la primera mitad literal y niega la segunda.**
>
> **POR ESO LO CUENTO COMO `PUENTE` Y NO COMO ERROR DE MATIZ:** `D.30` pregunta si el libro
> lo dice, y el libro no dice *no des por supuesta la mala intencion* en `L215`. **No hace
> falta doctrina nueva para esto**, asi que no es parada: es una discrepancia que adjudico
> en mi turno normal con el reporte delante.
>
> **Y DIGO DONDE PUEDO ESTAR EQUIVOCADO YO:** si la casa lee que reconstruir una errata
> evidente del original es transcripcion y no puente, mi cifra baja a `0` de `181` y la suya
> es la buena. **Lo que no puede quedarse es sin mirar**, porque `8.3` dice que el error que
> esta metrica invita a cometer es justo marcar un puente como transcripcion.

### 5.2. LAS CIFRAS QUE LOS NODOS SE PONEN EN EL TITULO, CONTADAS POR MI EN EL LIBRO

*La `pregunta 3` de la cola de doctrina es una cifra en `nombre_largo` que el libro no
escribe. Conte las de esta tanda contra los rotulos del fichero fuente.*

| nodo | cifra que se pone | lo que cuento yo en el libro | |
|---|---|---|---|
| `abrazar_incomodidad_arrancar_critica_equipo` | **seis** consejos | `L29`, `L37`, `L39`, `L45`, `L49`, `L53` = **6** | **cuadra** |
| `dar_guia_humilde_tres_tecnicas` | **tres** tecnicas | `L83`, `L91`, `L95` = **3** | **cuadra** |
| `dar_guia_util_cuatro_recordatorios` | **cuatro** recordatorios | `L103`, `L105`, `L109`, `L113` = **4** | **cuadra** |
| `dar_guia_acto_seis_consejos` | **seis** consejos | `L123`, `L127`, `L129`, `L131`, `L133`, `L135` = **6** | **cuadra** |
| `elogiar_publico_criticar_privado_sus_tres_matices` | **tres** matices | `L159`, `L161`, `L163` = **3** | **cuadra** |
| `revisar_critica_mujer_agresiva_cuatro_tacticas` | **cuatro** tacticas | `L305`, `L309`, `L311`, `L313` = **4** | **cuadra** |
| `responder_critica_abrasiva_cuatro_reglas` | **cuatro** reglas | `L317` **anuncia cuatro** y despues el libro rotula **CINCO** (`L319`, `L321`, `L323`, `L325`, `L327`) | **ver abajo** |

**EN EL ULTIMO, LA CIFRA DEL NODO ES LA DEL LIBRO, Y EL DESCUADRE ES DEL LIBRO.** Y el nodo
**no lo esconde**: su `nombre_largo` nombra las cuatro y despues escribe *mas no descartar a
los hombres*, que es el quinto rotulo dejado fuera de la cuenta a proposito. **Eso es lo que
yo habria hecho.** Lo unico que dejo marcado, y es de matiz: su paso `1` dice *las cuatro
reglas generales que el texto anuncia **y enumera***, y el texto **anuncia cuatro y enumera
cinco**. **No es la figura de la `pregunta 3`**, porque alli la cifra no estaba en el libro
y aqui si.

---

## 6. MI BARRIDO DE VECINOS (`D.38.4` y `D.38.5`): **GRAFO MAS BANDEJAS, `347`**

*Uno por vez, con la poblacion recortada por mi (el nodo ya vive dentro del grafo, asi que
le quito su propia linea) y las bandejas puestas por la aduana, que es el metodo vigente.*

*Salida de `python .v34aud/resumen_barrido.py`, guardada en `.v34aud/resumen_barrido.txt`.*

| # | candidato | poblacion | saldo de la aduana | vecinos | cuales |
|---:|---|---:|---|---:|---|
| 1 | `abrazar_incomodidad_arrancar_critica_equipo` | 347 | ENTRA | 0 | . |
| 2 | `comprobar_criticas_hombre_mujeres_equipo` | 347 | BLOQUEA | 3 | `exigir_critica_jefe_reticente`, `revisar_critica_mujer_agresiva_cuatro_tacticas`, `correr_semana_arreglo_averias_gestion` |
| 3 | `correr_semana_arreglo_averias_gestion` | 347 | BLOQUEA | 1 | `comprobar_criticas_hombre_mujeres_equipo` |
| 4 | `dar_guia_acto_seis_consejos` | 347 | ENTRA | 0 | . |
| 5 | `dar_guia_humilde_tres_tecnicas` | 347 | BLOQUEA | 1 | `elogiar_publico_criticar_privado_sus_tres_matices` |
| 6 | `dar_guia_util_cuatro_recordatorios` | 347 | ENTRA | 0 | . |
| 7 | `elegir_medio_dar_guia_jerarquia_modos` | 347 | ENTRA | 0 | . |
| 8 | `elogiar_publico_criticar_privado_sus_tres_matices` | 347 | BLOQUEA | 1 | `dar_guia_humilde_tres_tecnicas` |
| 9 | `evitar_personalizar_guia_aceptar_personal` | 347 | BLOQUEA | 1 | `manejar_enfado_persona_desafiada` |
| 10 | `exigir_critica_jefe_reticente` | 347 | BLOQUEA | 2 | `comprobar_criticas_hombre_mujeres_equipo`, `bloquear_tiempo_pensar_calendario` |
| 11 | `medir_guia_propia_pegatinas_marco` | 347 | ENTRA | 0 | . |
| 12 | `organizar_sistema_recoger_quejas_equipo` | 347 | BLOQUEA | 1 | `elogiar_publico_criticar_privado_sus_tres_matices` |
| 13 | `practicar_franqueza_radical_jefe_propio` | 347 | ENTRA | 0 | . |
| 14 | `responder_critica_abrasiva_cuatro_reglas` | 347 | ENTRA | 0 | . |
| 15 | `revisar_critica_mujer_agresiva_cuatro_tacticas` | 347 | BLOQUEA | 1 | `comprobar_criticas_hombre_mujeres_equipo` |
| | **total** | | | **11** | |

poblaciones distintas vistas: 1
  poblacion del barrido       : 347   (296 del grafo mas 51

**`296` del grafo mas `51` de bandeja da `347`, la misma poblacion en las quince corridas.**
Las bandejas son `48` de `scott_radical_candor` mas `3` de `marquet_turn_the_ship`.

**`11` VECINDADES LEVANTADAS.** `D.38.5` dice que desde que la aduana carga las bandejas
**mi cifra y la del informe ya son comparables**: si no cuadran, es discrepancia de verdad y
no de metodo. La comparo en la seccion 7, y **los once ids son los once de la bitacora.**

---

## 7. MIS CLASES, ADJUDICADAS A CIEGAS ANTES DE DESTAPAR NI UNA RAZON

*`AUDITOR_FORJA.md` 1.2: imprimir primero los pasos de los dos nodos, adjudicar con la vara,
**y solo despues** destapar la razon escrita. Lo hice en ese orden: mis clases se fijaron con
`python .v34aud/mis_clases.py` delante, que es el lector que **oculta a proposito** el campo
`veredicto` y el campo `razon`.*

*Salida de `python .v34aud/tabla_clases.py`, guardada en `.v34aud/tabla_clases.txt`.*

| # | candidato | vecino | senial que la levanta | **MI CLASE, a ciegas** | la de la vuelta | |
|---:|---|---|---|---|---|---|
| 411 | `construir_confianza_equipo_tiempo_solas` | `construir_confianza_equipo_tiempo_solas` | correccion declarada (txt ., pcn .) | **CORREGIDO** | CORREGIDO | COINCIDE |
| 412 | `organizar_sistema_recoger_quejas_equipo` | `elogiar_publico_criticar_privado_sus_tres_matices` | similitud_texto (txt 0.357, pcn 0.470) | **SANO** | SANO | COINCIDE |
| 413 | `correr_semana_arreglo_averias_gestion` | `comprobar_criticas_hombre_mujeres_equipo` | similitud_texto (txt 0.356, pcn 0.431) | **SANO** | SANO | COINCIDE |
| 414 | `dar_guia_humilde_tres_tecnicas` | `elogiar_publico_criticar_privado_sus_tres_matices` | similitud_texto (txt 0.350, pcn 0.393) | **SANO** | SANO | COINCIDE |
| 415 | `elogiar_publico_criticar_privado_sus_tres_matices` | `dar_guia_humilde_tres_tecnicas` | similitud_texto (txt 0.352, pcn 0.405) | **SANO** | SANO | COINCIDE |
| 416 | `evitar_personalizar_guia_aceptar_personal` | `manejar_enfado_persona_desafiada` | paso_contra_nodo (txt 0.234, pcn 0.867) | **SANO** | SANO | COINCIDE |
| 417 | `comprobar_criticas_hombre_mujeres_equipo` | `exigir_critica_jefe_reticente` | similitud_texto (txt 0.402, pcn 0.555) | **SANO** | SANO | COINCIDE |
| 418 | `comprobar_criticas_hombre_mujeres_equipo` | `revisar_critica_mujer_agresiva_cuatro_tacticas` | similitud_texto (txt 0.382, pcn 0.436) | **SANO** | SANO | COINCIDE |
| 419 | `comprobar_criticas_hombre_mujeres_equipo` | `correr_semana_arreglo_averias_gestion` | similitud_texto (txt 0.366, pcn 0.431) | **SANO** | SANO | COINCIDE |
| 420 | `exigir_critica_jefe_reticente` | `comprobar_criticas_hombre_mujeres_equipo` | similitud_texto (txt 0.382, pcn 0.577) | **SANO** | SANO | COINCIDE |
| 421 | `exigir_critica_jefe_reticente` | `bloquear_tiempo_pensar_calendario` | similitud_texto (txt 0.357, pcn 0.435) | **SANO** | SANO | COINCIDE |
| 422 | `revisar_critica_mujer_agresiva_cuatro_tacticas` | `comprobar_criticas_hombre_mujeres_equipo` | similitud_texto (txt 0.381, pcn 0.430) | **SANO** | SANO | COINCIDE |
| 423 | `abrazar_incomodidad_arrancar_critica_equipo` | `construir_confianza_equipo_tiempo_solas` | lectura declarada (txt 0.219, pcn 0.430) | **CONTINUA** | CONTINUA | COINCIDE |

lineas comparadas: 13   COINCIDEN: 13   DISCREPAN: 0
lineas nuevas SIN razon escrita (D.8): 0 de 13

> **ESTA TABLA SI LA IMPRIME SU INSTRUMENTO, Y ES A PROPOSITO.** La de mi apertura anterior
> decia venir de un fichero que no imprimia ninguna tabla, y `D.41` en estricto la puso en
> rojo con razon. La seccion 8 lo cuenta entero.

### 7.1. LAS TRES QUE MERECEN UNA LINEA, Y LAS DEMAS NO

- **`L416`, `evitar_personalizar_guia_aceptar_personal` contra `manejar_enfado_persona_desafiada`, senial `3` a `0,867`.** Los dos pasos dicen casi lo mismo porque **el libro lo dice dos veces**: `cap_04` `L131` y `cap_09` `L175`. Fuera de esa linea le quedan al candidato once pasos de procedimiento propio (el error fundamental de atribucion de Lee Ross, *eso esta mal* y no *tu estas mal*, el concurso de egos, el caso del olor corporal) y al vecino los suyos. **La vara no tiene bascula: decide si lo que queda fuera es procedimiento en los dos lados, y lo es. SANO.**
- **`L417` y `L420`, el mismo par por los dos extremos, `0,402` de ida y `0,382` de vuelta.** La similitud sale de que **el libro escribe los dos parrafos en paralelo a proposito**: `L293` abre *If you're a man and worried that...* y `L297` abre ***Similarly**, if you're a woman and worried that...*. Actor opuesto, direccion opuesta, entregable opuesto. **SANO los dos.**
- **`L423`, la arista `construir_confianza_equipo_tiempo_solas > abrazar_incomodidad_arrancar_critica_equipo`.** No la levanto ninguna senial (`0,219` de texto, por debajo del umbral): la levanto una lectura. **Y la lectura esta en el libro, literal:** `cap_08` `L95` escribe *(See "Soliciting Impromptu Guidance," chapter six.)*, y `cap_09` **es** `Cap. 6`. La madre **nombra** y el hijo **despliega en veinte pasos**: **NOMBRAR NO ES PROCEDIMENTAR**, asi que la direccion es la correcta. **CONTINUA.**

### 7.2. LA MUESTRA PINEADA DE LOS `SANO` (`AUDITOR_FORJA.md` 7)

| | |
|---|---:|
| `SANO` de la tanda | **11** |
| lo que la regla pide | el mayor entre `3` y el `20` por ciento de `11`, que es **`3`** |
| releidos por mi | **`11` de `11`**, la poblacion entera |
| caen | **`0`** |
| `SANO` sin razon escrita (`D.8`) | **`0`**, y la cuenta la da el instrumento de arriba |

**MIENTRAS LA POBLACION QUEPA, LA RELEO ENTERA Y NO INVENTO UNA MUESTRA.**

### 7.3. LO QUE COMPROBE DE LA `TAREA 1`, QUE ES LA UNICA LINEA `CORREGIDO`

*Es una correccion que entra en `dataset/`, asi que su cifra es cifra publicada. La
recompongo del dato, no de su texto.*

    nodos del dataset: 297
    capitulo    nodos    pasos
    cap_01          1        9
    cap_03          1       10
    cap_04          5       41
    cap_05          8       76
    cap_06         10      117
    cap_07         25      225
    cap_08         12      102
    cap_09         15      181
    cap_11         16      187
    suma 93 nodos, 948 pasos

    paso 6 de construir_confianza_equipo_tiempo_solas:
      Cuida como pides critica y como reaccionas cuando te la dan, porque eso construye confianza o la destruye.
    paso 7:
      Y manten conversaciones anuales de carrera, que el texto llama una manera excelente de reforzar tu relacion con cada persona que te reporta directamente.
    nodos_siguientes: ['montar_reuniones_solas_mentalidad_frecuencia', 'abrazar_incomodidad_arrancar_critica_equipo']

    $ awk 'NR==95' fuentes/scott_radical_candor/cap_08.md
      ... (See "1:1 Conversations," chapter eight.) ... (See "Soliciting Impromptu
      Guidance," chapter six.) ... (see chapter seven).

**LAS TRES REMISIONES DE `L95` SON `Cap. 8`, `Cap. 6` Y `Cap. 7`, QUE SON LOS FICHEROS
`cap_11.md`, `cap_09.md` Y `cap_10.md`**, y el mapa de unidades de la seccion 4 lo sostiene
sin que yo tenga que creerme nada. **`cap_11` tiene `16` nodos y `187` pasos**, que es lo
que mi propio recuento de hoy imprime, **asi que la frase vieja era falsa en uno de los tres
el dia en que se escribio.** La correccion la retira en vez de sustituirla por la cifra de
hoy, **y eso es lo correcto**: la cifra de hoy habria envejecido dentro de la misma vuelta,
porque `cap_09` acaba de pasar de `0` a `15` en esta misma tabla.

---

## 8. **LO QUE ENCUENTRO CONTRA MI, Y LO ENCUENTRO YO: MI TABLA DE LA VUELTA 33 ESTA EN ROJO POR `D.41`**

*Va aqui, en mi propia apertura, porque `5.3` dice que los errores del auditor se declaran
con su nombre igual que los del extractor, y porque una caida propia guardada hasta el acta
es exactamente lo que `D.38.2` vino a cerrar.*

**LA LINEA `498` DE MI APERTURA CIEGA DE LA VUELTA 33 DICE ESTO, Y LA TABLA QUE ANUNCIA
EMPIEZA EN LA `500`, QUE ES LA QUE EL INSTRUMENTO NOMBRA:**

    **MI TABLA, PEGADA DE `.v33a/mis_clases.txt` SIN TOCARLA, Y LA SUYA AL LADO:**

**Y `.v33a/mis_clases.txt` NO IMPRIME NINGUNA TABLA.** Lo reproduzco con el instrumento de
la casa, **sobre una copia fuera del repo** para no tocar ninguna sede:

    $ python -c "tallar_reporte.revisar + texto_informe(estricto=True)" sobre una COPIA de git show 6315b30:docs/loop/APERTURA_CIEGA.md
    ============================================================================
    TALLADO DEL REPORTE (D.41): la tabla que dice ser de instrumento
    ============================================================================
    tablas que declaran instrumento : 1
      talladas, celda a celda       : 0
      que DIFIEREN de su instrumento: 0
      con la ruta VACIA             : 0   (cero bytes, 7.B)
      sin poder comprobar           : 1
      que CITAN y no reproducen     : 0   (declaradas PARCIAL)

    SIN COMPROBAR  ../../AppData/Local/Temp/claude/C--Users-AlexDesk-Documents-forja-nodos/111462d1-d2ac-44e9-9b8f-9e168265d865/scratchpad/APERTURA_CIEGA_v33.md linea 500
      el instrumento no imprime ninguna tabla: esta la resume, no la reproduce

    TALLADO EN ROJO (estricto): 1 tabla(s) declaran instrumento y no se pueden comprobar.
    Una tabla que dice venir de un instrumento y no puede enseñarlo no esta declarando su origen: lo esta prometiendo.

    $ head -12 .v33a/mis_clases.txt
    MIS CLASES, ESCRITAS A CIEGAS Y ANTES DE DESTAPAR NI UNA RAZON DE bitacora/VEREDICTOS.jsonl
    (HEREDADO 3 de la ACTA 31: este fichero es anterior a la primera corrida que IMPRIMA UNA
    RAZON. En esta fase no he corrido ninguna, y la hora de este fichero queda publicada.)

    TANDA: los 12 ids que .v33a/tanda.py saca del git diff de dataset/nodos.jsonl entre
    ef3e7f9 (commit anterior a la apertura de la vuelta 33) y HEAD. DEL DATO, no de una lista.
    POBLACION DEL BARRIDO: dataset/nodos.jsonl de 282 nodos menos el propio candidato, mas las
    bandejas de cuarentena/, que las pone la aduana sola (D.38.4 con el metodo de D.38.5).

    PRIMER BLOQUE: LO QUE DIGO LEYENDO fuentes/scott_radical_candor/cap_08.md Y LOS 12 NODOS,
    ANTES DE SABER QUE VECINO LEVANTA LA ADUANA.

**ASI EMPIEZA EL FICHERO QUE MI TABLA DECIA PEGAR: una lista de `id` y clase, una por
linea. Ni una barra vertical.**

**LA CELDA NO ERA FALSA: LA PROCEDENCIA SI.** La `ACTA 32` seccion `2` comprobo que aquellas
trece clases coincidian trece de trece, asi que **lo que la tabla dice es cierto**; lo que es
falso es la frase **`PEGADA ... SIN TOCARLA`**, porque la tabla la compuse yo a mano leyendo
el fichero. **Es la misma familia que `7.B` de la cosecha, *la ruta que promete prueba es
cifra*: una tabla que promete un instrumento y no puede ensenarlo esta prometiendo, no
declarando.**

> **NO ME ADJUDICO LA ESPECIE EN ESTA FASE**, porque adjudicar con el reporte retirado seria
> decidir a medias. **La adjudico en mi turno normal**, y digo ya cual es mi lectura de
> partida: **`CIFRA PUBLICADA PROPIA`**, en sede duradera mia, con mi racha viniendo de
> `1 de 3` (`ACTA 32` `9.1`). Si se sostiene, **queda en `2 de 3`, que es el penultimo
> escalon, y entonces `5.5` obliga a que el remedio vaya ENCARGADO y no solo declarado.**
>
> **EL REMEDIO YA ESTA PUESTO EN ESTE MISMO DOCUMENTO Y NO ESPERA AL ACTA:** las tablas de
> instrumento de esta apertura (secciones `3`, `4`, `4.1`, `5`, `6`, `7`) **las imprime su
> instrumento en markdown**, y este fichero se monta con `python .v34aud/armar.py`, que las
> **lee del `.txt`** en vez de dejar que mi mano las escriba.

---

## 9. LO QUE DEJO `POR ADJUDICAR` PARA MI TURNO NORMAL

| # | que | por que no lo cierro ahora |
|---:|---|---|
| **1** | **el paso `13` de `practicar_franqueza_radical_jefe_propio`**: yo leo `PUENTE`, y el `resumen_teorico` del nodo declara `17 TRANSCRIPCION, 0 PUENTE` | es una discrepancia de lectura, y quiero ver **si la marco como discutible** antes de decidir quien la paga |
| **2** | **`L223` a `L289` sin ni un candidato** | hay que ver si el reporte lo **declara** como frontera o si simplemente no lo miro |
| **3** | **el cierre corto de `cap_09` en `15` de `20`** | `EXTRACTOR.md` 12.4 exige que se declare **en el reporte**, y el asunto de un commit no es sede (`5.6`) |
| **4** | **el diff de `dataset/` y `bitacora/` dentro del commit de CIERRE `3dbc901`** | un cierre que toca sedes de dato se lee entero, por el ejemplar de la `ACTA 32` `5.1` |
| **5** | **la suite de aceptacion** | la vuelvo a correr con `CREDITO_serial.jsonl` devuelto, y esa sera la cifra que firme |
| **6** | **mi propia tabla de la vuelta 33 en rojo por `D.41`** | seccion 8: la especie la adjudico con el reporte delante |
| **7** | **el par `L416` como posible `D.29`** | lei la misma duda que el barrido levanta: la madre seria el nodo pequenio de otro capitulo y la jerarquia saldria al reves de como el libro ordena su material. **No la adjudico a ciegas** |

**NINGUNA DE LAS SIETE ES UNA DE LAS `6` DE LA COLA DE DOCTRINA DEL TABLERO**, y ninguna me
bloquea, asi que ninguna sube sola.

---

## 10. EL TABLERO, CITADO EN LA APERTURA COMO `D.49` MANDA

    $ python forja.py tablero
    TABLERO DE FRENTES (D.49, D.50): sede unica del estado de la campania
      registro: docs/loop/TABLERO.jsonl

      prio lote clave                          estado                 dueno                 band ult cap
      --------------------------------------------------------------------------------------------------------
      .    1    onu_consumidor                 INSERTADO              NINGUNO                  0  cap_02
      .    2    smart_who                      INSERTADO              NINGUNO                  0  cap_05
      .    3    zhuo_manager                   INSERTADO              NINGUNO                  0       .
      .    4    scott_radical_candor           CERRADO EN EXTRACCION  serial                  48  cap_14
      .    11   gerber_emyth_cap17_reservado   SIN EMPEZAR            NINGUNO                  0       .
      1    7    grove_high_output              EN CURSO               grove_high_output       23  cap_03
      2    9    gerber_emyth                   PAUSADO                NINGUNO                 10  cap_11
      3    5    marquet_turn_the_ship          PAUSADO                NINGUNO                  9  cap_03
      4*   8    bernerslee_bananas             SIN EMPEZAR            NINGUNO                  0       .
      5*   6    openstax_business_ethics       SIN EMPEZAR            NINGUNO                  0       .
      6*   10   openstax_org_behavior          SIN EMPEZAR            NINGUNO                  0       .

      prioridad: el orden del mundo 11 (D.51). El asterisco es FUERA DE
      CAMPANIA: no se extrae, queda en bandeja para la aduana de a uno.
      Sin prioridad: ya dentro del mundo 11, no hay nada que elegir.

      libros CON DUEÑO ahora mismo: 2
        scott_radical_candor           lo trabaja 'serial' (CERRADO EN EXTRACCION)
        grove_high_output              lo trabaja 'grove_high_output' (EN CURSO)

      MUNDO 11: faltan 3 de 3 libros del corte (grove_high_output, gerber_emyth, marquet_turn_the_ship)

      COLA DE DOCTRINA (D.52): 6 pregunta(s), 0 bloquea(n)
                1  EXTRACTOR.md 11 y la banda de 0,4: dice que por encima hay gemelos y cero ajen
                2  src/arista.py:187 teclea (D.37) en toda arista declarada por lectura, y se est
                3  Una cifra en denominaciones.nombre_largo que el libro no escribe: 'las cuatro
                4  Un resumen_teorico del dataset que cita EL REPORTE DE ESTA VUELTA: sede durade
                5  Un orden roto no tiene casillero: el extractor corrio la relectura de fidelida
                6  La regla de la busqueda negativa vale para el extractor? 'Una busqueda negativ

      PENDIENTES DE RELEVO (D.50), en orden de lote:
        lote 5   marquet_turn_the_ship           9 candidato(s) en extraccion-marquet_turn_the_ship
        lote 7   grove_high_output              23 candidato(s) en extraccion-grove_high_output
        lote 9   gerber_emyth                   10 candidato(s) en extraccion-gerber_emyth

    $ python forja.py tablero --puedo scott_radical_candor
    LINEA 'serial', LIBRO 'scott_radical_candor': SI
      'scott_radical_candor' ya es de esta linea ('serial'): continuarlo es lo que toca.

**MI LIBRO ES `scott_radical_candor` Y ME TOCA A MI PORQUE YA ES DE MI LINEA.** Esta
`CERRADO EN EXTRACCION` con `48` en bandeja, asi que lo que corre es insercion. **`D.50`
releva al CERRAR y no a mitad**, y este no cierra: quedan `48`, de los cuales `5` son del
propio `cap_09`.

> **Y LO DIGO AHORA PORQUE LLEGA PRONTO:** cuando `scott_radical_candor` cierre, el que toca
> por el orden del mundo 11 es `grove_high_output`, que el tablero da **`EN CURSO`** en
> `extraccion-grove_high_output`. **`D.50`: se releva ENTERO y el paso de fundir es del
> fundador**, asi que eso sera **parada con peticion escrita**, no apertura de lote. **No es
> de esta vuelta**, pero el encargo que escriba tendra que decirlo.

---

## 11. EL ESTADO DEL ARBOL AL SELLAR

    $ git rev-parse HEAD
    3dbc9017cd7056efb83a7c9c9c40472588a7010c

    $ git rev-parse --abbrev-ref HEAD
    extraccion-mundo-11

    $ git status --short
     D docs/loop/APERTURA_CIEGA.md
     D docs/loop/CREDITO_serial.jsonl
     D docs/loop/REPORTE.md
     D docs/loop/loop.log
     M docs/loop/ultimo_apertura.json
     D docs/loop/ultimo_auditor.json
     D docs/loop/ultimo_extractor.json
    ?? .v34aud/

    $ git log -1 --format=%h %ad --date=iso
    3dbc901 2026-09-17 12:22:49 -0400

### 11.1. LAS GUARDAS QUE MIRAN ESTE MISMO FICHERO, CORRIDAS SOBRE EL

*`D.41` mira mis tablas de instrumento, `D.42` mis rutas publicadas y `D.40` mi linea de
lectura. Las tres corridas enteras estan en `.v34aud/cierre_apertura.txt`; aqui van sus
cuatro lineas de veredicto **tal cual las imprime cada instrumento**, sacadas de esa misma
salida con un `grep`, para no reescribir ni una.*

    $ grep -E 'VERDE|COMPLETA' .v34aud/cierre_apertura.txt      (la corrida entera esta en ese fichero)
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    TALLADO VERDE: las 6 tabla(s) comprobables son las de su instrumento, celda a celda.
    CENSO VERDE: las 143 rutas publicadas sostienen lo que dicen sostener.
    CIERRE VERDE: el tallado y el censo de rutas.
    APERTURA CIEGA COMPLETA: el acta anterior va leida por su huella y los 0 heredados van declarados.

**EL TALLADO EN VERDE ES LA PRUEBA DE QUE EL REMEDIO DE LA SECCION 8 MUERDE**, y es el
mismo instrumento que puso en rojo mi tabla de la vuelta anterior.

**NO HE COMMITEADO NADA Y NO HE TOCADO NINGUNA SEDE DE DATO.** Lo unico que mi turno escribe
en el arbol es `.v34aud/`, que son mis instrumentos y sus salidas, y este fichero. **Mi unica
corrida sobre contenido que no es mio** fue el tallado de la seccion 8, y corrio **sobre una
copia en el temporal de la sesion**, fuera del repo.

**ACTA ANTERIOR LEIDA: 3b176db2f9bbb25f92a76a0cfff0a365c30d5822**
