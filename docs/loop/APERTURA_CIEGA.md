# APERTURA CIEGA DEL AUDITOR, vuelta 41, lote 4 (`scott_radical_candor`), `cap_13`

*Escrita ANTES de que el arnes me exponga el reporte. Lo que hay aqui es mi lectura,
no la suya. `D.38.3`: toda cifra sale de un instrumento corrido EN ESTA FASE y va con
su salida literal al lado. `D.38.4`: el barrido de vecinos es sobre GRAFO MAS BANDEJAS.*

---

## 0. LAS DECLARACIONES QUE EL ARNES EXIGE (`D.40`)

    ACTA ANTERIOR LEIDA: 266e5197978cc8a83ca859b5b75e9c7d3444e6fd
    HEREDADO 1: CUMPLIDO

**Y NO LO DECLARO DE MEMORIA: LO MIDO.** La huella que el prompt me entrega es la del
fichero que tengo abierto, y lo compruebo con el instrumento antes de escribir la linea:

    $ git hash-object docs/loop/ACTA_AUDITOR.md
      266e5197978cc8a83ca859b5b75e9c7d3444e6fd

**Coincide al digito con la que el prompt me da.** `AUDITOR_FORJA.md` 1.5 dice *decir que
leiste otra version no es haberla leido*, y esta es la unica manera de que esa frase
signifique algo.

---

## 1. `HEREDADO 1`, CUMPLIDO, Y CUMPLIDO CON LAS DOS MITADES QUE PEDIA

> **TAREA BLOQUEANTE DEL AUDITOR, para la `ACTA 40`: antes de escribir en mi apertura
> ciega que un nodo es cabeza de serie `D.37`, corro el `grep` de la cuenta sobre EL
> FICHERO FUENTE de su unidad de origen y pego su salida al lado; si el `grep` da `0`,
> escribo `D.29` y la razon que la sostiene. Y antes de publicar la clase de un par,
> corro `grep -n "<id del vecino>" docs/loop/ACTA_AUDITOR.md` para ver si ese par ya
> esta adjudicado, y si lo esta, lo cito en vez de volver a decidirlo.**

**ME LO ENCARGUE YO A MI MISMO EN LA `ACTA 39` PORQUE ME CAI EN LAS DOS MITADES.**
Lo cumplo aqui, y lo cumplo antes de escribir una sola clase.

### 1.1. LA MITAD DEL `grep` DE LA CUENTA. EL INSTRUMENTO DISCRIMINA, Y LO PRUEBO CON UN CONTROL

**Corro el mismo patron sobre los dos capitulos**, el que la casa tiene por cabeza `D.37`
y el que yo converti en cabeza `D.37` leyendolo de un TITULO de esta casa:

    $ grep -c -i -E "the (two|three|four|five|six) (tips|elements|things|ways|steps|parts)" cap_13.md
      2
    $ grep -n -i -E "the (two|three|four|five|six) (tips|elements|things|ways|steps|parts)" cap_13.md
      113:...We'd like to go into more detail on each of the four tips for soliciting criticism offered in the book.
      237:Now that you've practiced the four elements of soliciting criticism...

    $ grep -c -i -E "the (two|three|four|five|six) (tips|elements|things|ways|steps|parts)" cap_09.md
      0

**Y NO ME QUEDO EN EL PATRON QUE ME CONVIENE.** El `TITULO` que me enganio decia *seis
consejos*, asi que busco el seis a pelo en el fichero fuente, que es lo que un `NO APLICA`
perezoso no habria hecho:

    $ grep -n -i -E "\bsix\b|\bseis\b" cap_09.md
      41:One technique is to count to six before saying anything else, forcing them to endure the silence...
      159:Corrections, factual observations, disagreements, and debates are different from criticism...
      299:Try saying, "What can I do or stop doing to make it easier for you to be Radically Candid with me?"...
    $ grep -c -i -E "\bsix\b" cap_09.md
      3

> **`LECTURA`, y va marcada aparte de la cifra como manda `D.38.3` ensanchada:** los `3`
> aciertos de `six` en `cap_09` **no son ninguno una cuenta de serie**. El de `L41` es la
> tecnica de *contar hasta seis* dentro de una conversacion, y los otros dos son la palabra
> suelta. **`cap_09` no escribe en ningun sitio cuantos consejos trae.**

| cabeza | unidad | el `grep` de la cuenta | especie de sus aristas |
|---|---|---:|---|
| `pedir_critica_primero_crear_seguridad_psicologica` | `cap_13` | **`2`** (`L113`, `L237`) | **`D.37`**, la cuenta esta escrita |
| `abrazar_incomodidad_arrancar_critica_equipo` | `cap_09` | **`0`** | **`D.29`**, la sostiene la lectura y no una cuenta |

**ESCRIBO `D.29` PARA `cap_09` PORQUE EL `grep` DIO `0`**, que es literalmente lo que el
remedio ordena. **Y el `2` de `cap_13` no es adorno: es el control que prueba que el
instrumento sabe distinguir**, porque un patron que diera `0` en los dos sitios no habria
medido nada y me habria dejado escribir lo mismo por casualidad.

### 1.2. LA MITAD DEL `grep` CONTRA EL ACTA. LOS TRES PARES YA ESTABAN ADJUDICADOS

**Antes de clasificar nada, busco si la casa ya decidio:**

    $ grep -c "abrazar_incomodidad_silencio_contar_seis" docs/loop/ACTA_AUDITOR.md
      14
    $ grep -c "escuchar_entender_critica_dominar_defensa" docs/loop/ACTA_AUDITOR.md
      8
    $ grep -c "premiar_franqueza_hacer_escucha_tangible" docs/loop/ACTA_AUDITOR.md
      6
    $ grep -c "cambiar_forma_trabajar_conservar_plantilla" docs/loop/ACTA_AUDITOR.md
      3
    $ grep -c "contar_historias_propias_explicar_franqueza_radical" docs/loop/ACTA_AUDITOR.md
      7

**LOS CINCO TIENEN HISTORIAL, Y LA `ACTA 24` ADJUDICO LOS TRES QUE ME IMPORTAN.** Los cito
por linea en la seccion 7 en vez de volver a decidirlos, **que es exactamente la mitad del
remedio que la vuelta pasada no corri.**

---

## 2. LA POBLACION SE MOVIO DENTRO DE MI FASE SELLADA. TERCERA VUELTA SEGUIDA, Y ESTA VEZ CON LA MEDIDA DEL RELOJ

**ESTO NO LO BUSQUE: ME SALIO AL CORRER LA PRIMERA GUARDA.** Corri `forja.py gate` como
primera operacion de mi turno y despues `forja.py resolutor`, y **no midieron la misma
poblacion**:

    $ python forja.py gate            (primera operacion de mi turno)
      GATE VERDE.
        nodos verificados: 324

    $ python forja.py resolutor       (la operacion siguiente)
      nodos vivos: 325
    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl
          325 dataset/nodos.jsonl
          514 bitacora/VEREDICTOS.jsonl

    $ date -u +%H:%M:%S; python forja.py gate | head -3
      12:54:07
      GATE VERDE.
        nodos verificados: 325

**Y LA HORA DEL CAMBIO ESTA EN EL SISTEMA DE FICHEROS, NO EN MI RECUERDO:**

    $ stat -c "%y  %n" dataset/nodos.jsonl censos/series_y_cabezas.md censos/denominaciones.md bitacora/VEREDICTOS.jsonl .v41/informes/_cadena.txt
      2026-09-18 08:53:27.971582500 -0400  dataset/nodos.jsonl
      2026-09-18 08:53:27.977017100 -0400  censos/series_y_cabezas.md
      2026-09-18 08:53:27.992878500 -0400  censos/denominaciones.md
      2026-09-18 08:53:28.720861200 -0400  bitacora/VEREDICTOS.jsonl
      2026-09-18 08:53:29.736250800 -0400  .v41/informes/_cadena.txt

    $ git status --short
       M bitacora/VEREDICTOS.jsonl
       M censos/denominaciones.md
       M censos/series_y_cabezas.md
      R  cuarentena/scott_radical_candor/abrazar_incomodidad_silencio_contar_seis.json -> cuarentena/_insertados/scott_radical_candor/abrazar_incomodidad_silencio_contar_seis.json
       M dataset/nodos.jsonl

    $ git diff --stat censos/
      censos/denominaciones.md   | 3 +++
      censos/series_y_cabezas.md | 1 +
      2 files changed, 4 insertions(+)

    $ Get-Process python              (PowerShell, al medir)
      (ninguno)

**EL MOVIMIENTO TOCA LAS CUATRO SEDES DE DATO A LA VEZ, Y ESO NO LO DICE LA CUENTA DE
NODOS:** `dataset/`, `bitacora/`, **`censos/`** y `cuarentena/`, **las cuatro dentro de un
segundo y medio y las cuatro sin commitear**. Las tres primeras son sede de `CLASE` y de
`DATO MOVIDO` por la tabla de `5.2`. **Lo compruebo antes de escribirlo**, porque un
`git status` acotado a `dataset/ bitacora/ cuarentena/` me habria escondido `censos/`
entero: la primera vez que mire, mire acotado, **y por eso lo mire otra vez sin acotar.**

> **`LECTURA`:** `12:54:07` UTC son las `08:54:07` locales. **El dato se escribio a las
> `08:53:27`, cuarenta segundos antes de mi segunda medida y despues de mi primera.** Un
> candidato entero paso de bandeja a grafo **dentro de mi fase ciega**, sin commitear, y
> cuando fui a mirar **ya no quedaba ningun proceso de python vivo**: la cadena termino
> sola, encabalgada sobre mi turno.

**ES LA PREGUNTA `9` DE LA COLA DE DOCTRINA, Y HOY TIENE SU TERCER EJEMPLAR:**

    $ python forja.py tablero        (pregunta 9 de la cola, leida del TABLERO.jsonl)
      "Puede el arnes abrir la fase ciega del auditor con un proceso del extractor
       todavia vivo? Dos vueltas seguidas la poblacion se movio dentro de la fase
       sellada, y en la vuelta 38 con la pagina abierta: el mismo forja.py gate dio
       320 y despues 321 dentro del mismo turno."

**LA FIGURA ES LA MISMA HASTA EN EL NUMERO: `320` y `321` alli, `324` y `325` aqui.** No
la adjudico, porque `D.45` me prohibe tocar el arnes con `grove_high_output` `EN CURSO` en
otra rama y porque la pregunta ya esta en la cola sin bloquear. **Lo que si hago es dejar
medido que ya son TRES vueltas y no dos**, y dejar dicho el coste concreto: **la cifra de
apertura de esta acta depende del segundo en que la mida**, y eso es justo lo que `D.38.3`
vino a impedir.

**NO LE CARGO ESTO A NADIE EN ESTA FASE.** Es maquinaria del arnes, la parada de `D.45`
protege al arnes, y el extractor no elige cuando su cadena termina.

---

## 3. LO QUE EL ARNES RETIRA SON CINCO Y NO CUATRO, Y ESTA VEZ TRAIGO EL COSTE MEDIDO

**La `ACTA 39` lo declaro sin cargarselo a nadie. Hoy lo mido entero.**

    $ git status --short docs/loop/
       D docs/loop/APERTURA_CIEGA.md
       D docs/loop/CREDITO_serial.jsonl
       D docs/loop/REPORTE.md
       D docs/loop/loop.log
       M docs/loop/ultimo_apertura.json
       D docs/loop/ultimo_auditor.json
       D docs/loop/ultimo_extractor.json

`APERTURA_CIEGA.md` es mia y la reescribo yo, asi que no cuenta. **Los retirados son
CINCO:** `REPORTE.md`, `loop.log`, `ultimo_extractor.json`, `ultimo_auditor.json` **y
`CREDITO_serial.jsonl`**. El prompt nombra cuatro y `AUDITOR_FORJA.md` 1.5 nombra cuatro.
**El quinto no lo nombra nadie.**

### 3.1. EL COSTE: EL INSTRUMENTO DEL CREDITO PUBLICA UN CERO FALSO

    $ python forja.py credito
      CREDITO DE LA LINEA 'serial' (D.48)
        registro: docs/loop/CREDITO_serial.jsonl

        LINEA SIN REGISTRO: no hay ningun suceso escrito.
        Una linea sin tandas NACE CON SU RACHA EN CERO y no hereda
        la de nadie (D.48). Lo que herede el arnes sera CERO remedios.

    $ python forja.py credito --lineas
      NINGUNA LINEA TIENE REGISTRO DE CREDITO todavia (D.48).

> **`LECTURA`, y es la que hace que esto pase de anecdota a hallazgo:** el instrumento de
> la casa **no dice *no puedo medir*: dice *racha en CERO***. Y la racha de esta linea **no
> esta en cero**: la `ACTA 39` la cerro en `REPORTE 1 de 3` y `AUDITOR 2 de 3`
> (`ACTA_AUDITOR.md` `L32134` y `L32147`). **Un fichero retirado por el arnes convierte un
> instrumento de la casa en una fuente de cifra falsa**, y la cifra que falsea es
> exactamente la que decide si el bucle para.

**POR ESO NO PUBLICO NINGUNA RACHA MEDIDA EN ESTA FASE.** La leo del acta, que es sede
duradera y esta en el arbol, y digo de donde la saco.

### 3.2. Y CUESTA TRES PRUEBAS DE ACEPTACION MAS UN ERROR

    $ python tests/test_aceptacion.py
      total: 294 pruebas, 3 fallos, 1 errores
      FAILED (failures=3, errors=1, skipped=1)

    ERROR: test_el_reporte_vivo_pasa_su_propia_guarda
      FileNotFoundError: ...docs\loop\REPORTE.md
    FAIL: test_la_linea_serial_del_repo_tiene_su_registro_escrito
      AssertionError: False is not true : docs/loop/CREDITO_serial.jsonl sin tandas:
                      la migracion de D.48 no esta en el arbol
    FAIL: test_caso_positivo_un_frente_recien_nacido_hereda_cero
    FAIL: test_el_aviso_nombra_la_linea_y_su_registro
      AssertionError: 'libro_que_nunca_dicto_nada' not found in ''

**LOS CUATRO SON DE FICHERO AUSENTE Y NINGUNO ES DE CODIGO.** Uno por `REPORTE.md` y
**TRES por el quinto retirado**. La `ACTA 39` ya adjudico que el rojo de la suite en la
fase ciega **no es parada**, porque *la exencion es de MOMENTO y no de fichero* lo cubre
por extension natural. **Esa adjudicacion sigue sirviendo y no la reabro** (`D.47`, modo
austero: lo que el registro ya dice no se repite).

**LO QUE SI ES NUEVO Y LO DEJO ESCRITO:** la vuelta pasada el rojo era de `1` prueba y hoy
es de `4`, y las `3` nuevas salen del fichero que nadie declaro retirar. **`D.45` me
prohibe arreglarlo yo.** Sube al fundador como esta.

---

## 4. EL ESTADO AL ABRIR, CIFRA POR CIFRA Y CON SU INSTRUMENTO

**Medido a las `13:05:06` UTC, cuando la poblacion ya estaba quieta** (seccion 2).

    $ python forja.py gate
      GATE VERDE.
        nodos verificados: 325
    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python forja.py resolutor
      nodos vivos: 325
      nodos deprecados (archivo): 0
      alias registrados: 0
    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl
          325 dataset/nodos.jsonl
          514 bitacora/VEREDICTOS.jsonl
    $ python -c "suma de nodos_previos sobre dataset/nodos.jsonl"
      aristas dirigidas (suma de nodos_previos): 138
    $ python -c "conteo del campo veredicto sobre bitacora/VEREDICTOS.jsonl"
      SANO 346 | CONTINUA 158 | CORREGIDO 10
    $ python forja.py rancios
      BLOQUE DE VIGENCIA: 72 hallazgo(s) sobre 500 veredicto(s) y 0 cita(s).
        RANCIO 64, SIN HUELLA 8
        lineas declaradas NO CONSUMADAS y por eso no medidas: 14

| | al cerrar la `ACTA 39` | **al abrir mi fase** | delta |
|---|---:|---:|---:|
| nodos | `324` | **`325`** | **`+1`** |
| aristas dirigidas | `134` | **`138`** | **`+4`** |
| veredictos | `507` | **`514`** | **`+7`** |
| `SANO` | `343` | **`346`** | `+3` |
| `CONTINUA` | `154` | **`158`** | `+4` |
| `CORREGIDO` | `10` | **`10`** | `0` |
| `RANCIO` / `SIN HUELLA` | `64` / `8` | **`64`** / **`8`** | `0` / `0` |
| gate | VERDE `324` | **VERDE `325`** | |
| guiones | VERDE | **VERDE** | |
| suite | `294 / 0 / 0` | **`294 / 3 fallos / 1 error`** | seccion `3.2` |

**LAS DOS CIFRAS DE LA BITACORA CUADRAN ENTRE SI Y LO COMPRUEBO:** `rancios` dice medir
sobre `500` veredictos y `wc -l` da `514`; la diferencia son las `14` lineas declaradas
**NO CONSUMADAS** que el propio instrumento nombra. `500 + 14 = 514`. **No hay cifra
suelta.**

### 4.1. LA BANDEJA, POR CAPITULO

    $ ls cuarentena/scott_radical_candor/*.json | wc -l
      20
    $ grep -l "cap_13.md" cuarentena/scott_radical_candor/*.json | wc -l
      5
    $ grep -l "cap_14.md" cuarentena/scott_radical_candor/*.json | wc -l
      15
    $ ls cuarentena/_insertados/scott_radical_candor/*.json | wc -l
      122
    $ python -c "suma de len(pasos_accionables) sobre la bandeja"
      TOTAL PASOS EN BANDEJA: 273

**Bandeja `20`** (`cap_13` **`5`**, `cap_14` **`15`**), **insertados `122`**. La `ACTA 39`
cerro en `21` (`6` y `15`) con `121` insertados: **la diferencia es el candidato que entro
dentro de mi fase sellada**, y cuadra por las tres cuentas a la vez.

> **UNA TRAMPA DE INSTRUMENTO QUE ME SALIO AL PASO Y LA DIGO PARA QUE NADIE LA REPITA:**
> `grep -o "cap_1[34].md" | uniq -c` me daba **`5` y `16`**, que suman `21` sobre `20`
> ficheros. **`grep -o` cuenta APARICIONES y `grep -l` cuenta FICHEROS**, y un candidato
> nombra su capitulo dos veces. **La cifra buena es la de `grep -l`.**

### 4.2. LAS BANDEJAS ENTERAS, QUE ES LA POBLACION QUE MANDA `D.38.4`

    $ for d in cuarentena/*/; do printf "%-45s %s\n" "$d" "$(ls $d*.json 2>/dev/null | wc -l)"; done
      cuarentena/_derivadas/                          2
      cuarentena/_insertados/                         0
      cuarentena/ensayo_referencia_163/             163
      cuarentena/marquet_turn_the_ship/               3
      cuarentena/onu_consumidor/                      0
      cuarentena/scott_radical_candor/               20
      cuarentena/smart_who/                           0
      cuarentena/zhuo_manager/                        0

**`20` de `scott` mas `3` de `marquet` son `23`**, descartando `_insertados`, `_derivadas`
y el control `ensayo_referencia_163`. **Y eso es exactamente lo que la aduana dice medir**
(seccion 6), asi que mi poblacion y la suya **son la misma** y `D.38.5` se cumple sin
tener que creerselo.

---

## 5. LA COLA DE ARISTAS, RECONTADA POR MI

    $ python -c "cola por el campo arista_en_cola, resolviendo arista_corregida antes que arista"
      lineas con arista_en_cola: 16
        CABLEADA          linea 489  pedir_critica_primero... > abrazar_incomodidad_silencio_contar_seis
        ESPERA EXTREMO    linea 490  pedir_critica_primero... > dar_elogio_disciplina_igual_critica
        ESPERA EXTREMO    linea 492  pedir_critica_primero... > escuchar_entender_critica_dominar_defensa
        ESPERA EXTREMO    linea 494  pedir_critica_primero... > medir_critica_respuesta_oyente_brujula
        ESPERA EXTREMO    linea 495  pedir_critica_primero... > premiar_franqueza_hacer_escucha_tangible
      COLA arista_en_cola: 16 / 12 cableadas / 4 esperando / 0 dentro y sin cable

**`16 / 12 / 4 / 0`.** La `ACTA 39` cerro en `16 / 11 / 5 / 0`, y el encargo pide cerrar
hoy en `16 / 14 / 2 / 0`. **La `489` paso de esperando a cableada** cuando entro el
candidato `1`, que es exactamente el movimiento previsto. **La cifra que tiene que salir
`0` sale `0`**, y es la ultima.

**Y LA MIDO TAMBIEN SOBRE LA BITACORA ENTERA, NO SOLO SOBRE LA COLA**, porque una cola
limpia con el resto sucio no dice nada:

    $ python -c "misma cuenta sobre TODA linea que declare arista"
      lineas que declaran arista: 158 / 154 cableadas / 4 esperando extremo / 0 dentro y sin cable

**`0` tambien ahi, y las `4` que esperan son las mismas `4`.** No hay ninguna arista
declarada con los dos extremos dentro del grafo y sin cablear.

---

## 6. EL BARRIDO DE VECINOS (`D.38.4` y `D.38.5`), CORRIDO POR MI CON EL INSTRUMENTO DE LA CASA

**Corro `forja.py informe`, que es de SOLO LECTURA por construccion y no inserta nada.**

    $ python forja.py informe cuarentena/scott_radical_candor/escuchar_entender_critica_dominar_defensa.json
      poblacion del barrido       : 348   (325 del grafo mas 23 que esperan en bandejas)
      umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60
      vecinos levantados en total : 4
      que senal levanta cada vecindad : paso_contra_nodo 1, similitud_texto 3

      [BLOQUEARIA] escuchar_entender_critica_dominar_defensa
          vecino cambiar_forma_trabajar_conservar_plantilla  [levantada por: paso_contra_nodo]
            similitud_texto 0.215 | familia_id 0.000 | paso_contra_nodo 0.634
            paso 4 del candidato contra paso 2 de cambiar_forma_trabajar_conservar_plantilla
          vecino contar_historias_propias_explicar_franqueza_radical  [similitud_texto]
            similitud_texto 0.393 | familia_id 0.000 | paso_contra_nodo 0.549
            paso 4 del candidato contra paso 3 de contar_historias_propias...
          vecino abrazar_incomodidad_silencio_contar_seis  [similitud_texto]
            similitud_texto 0.446 | familia_id 0.000 | paso_contra_nodo 0.507
            paso 4 del candidato contra paso 1 de abrazar_incomodidad_silencio_contar_seis
          vecino premiar_franqueza_hacer_escucha_tangible  [similitud_texto]
            similitud_texto 0.363 | familia_id 0.000 | paso_contra_nodo 0.484
            paso 5 del candidato contra paso 8 de premiar_franqueza_hacer_escucha_tangible

    $ python forja.py informe cuarentena/scott_radical_candor/premiar_franqueza_hacer_escucha_tangible.json
      poblacion del barrido       : 348   (325 del grafo mas 23 que esperan en bandejas)
      vecinos levantados en total : 1
      [BLOQUEARIA] premiar_franqueza_hacer_escucha_tangible
          vecino escuchar_entender_critica_dominar_defensa  [similitud_texto]
            similitud_texto 0.375 | familia_id 0.000 | paso_contra_nodo 0.465
            paso 8 del candidato contra paso 5 de escuchar_entender_critica_dominar_defensa

**MI POBLACION Y LA SUYA SON LA MISMA: `348`.** Lo comprueba mi propio barrido de la
seccion `4.2` (`325 + 20 + 3`), y lo dice su cabecera. **`D.38.5` cumplido por las dos
puntas**, y por eso las dos cifras son comparables sin nota al pie.

### 6.1. DOS COSAS QUE EL INSTRUMENTO PUBLICA Y QUE NADIE ME PIDIO MIRAR

**UNA: LA SENIAL NO ES SIMETRICA, Y SE VE EN EL MISMO PAR.** El par
`escuchar_entender` contra `premiar_franqueza` sale **`0.363`** cuando el candidato es uno
y **`0.375`** cuando el candidato es el otro. **Es el mismo par y son dos numeros.** No lo
adjudico: lo dejo medido, porque una banda que se cita al tercer decimal
(`EXTRACTOR.md` 11, la pregunta `1` de la cola) **cambia segun cual de los dos nodos
escribas primero.**

**DOS: LAS CIFRAS NO SE MOVIERON AUNQUE EL GRAFO SI.** El encargo me advirtio, con razon
escrita, que *el primero que entra cambia lo que el segundo mide* y que las cifras que me
daba eran de **antes** de la primera insercion. Las he remedido **despues**, con el
candidato `1` ya dentro del grafo:

| par | lo que el encargo daba (grafo de `324`) | lo que mido yo (grafo de `325`) |
|---|---:|---:|
| `escuchar_entender` contra `cambiar_forma_trabajar` | `0.634` | **`0.634`** |
| `escuchar_entender` contra `contar_historias` | `0.393` | **`0.393`** |
| `escuchar_entender` contra `abrazar_incomodidad` | `0.446` | **`0.446`** |
| `escuchar_entender` contra `premiar_franqueza` | `0.363` | **`0.363`** |
| `premiar_franqueza` contra `escuchar_entender` | `0.375` | **`0.375`** |

**Los cinco al digito.** `escuchar_entender` sigue con `4` vecinos y `premiar_franqueza`
con `1`. **La advertencia era correcta como doctrina y no se materializo en este caso**, y
lo digo en los dos sentidos porque la mitad util es la segunda: **el candidato que entro
era ya vecino declarado de los dos, asi que pasar de bandeja a grafo no le cambio el peso
a nadie.** Eso es `D.38.5` funcionando.

---

## 7. MI CLASIFICACION DE LOS PARES, A CIEGAS Y CON LOS PASOS DELANTE

**Metodo, y lo digo antes de la tabla:** imprimi los pasos de los dos nodos de cada par
**antes** de escribir la clase, corri el `grep` del `HEREDADO 1` sobre el acta, y donde la
casa ya tenia adjudicado **cito en vez de volver a decidir**.

### 7.1. LOS TRES PARES QUE LA `ACTA 24` YA ADJUDICO, CITADOS Y NO REABIERTOS

| par | mi clase | donde ya estaba adjudicado |
|---|---|---|
| `abrazar_incomodidad_arrancar_critica_equipo` (`cap_09`, 20 pasos) contra `abrazar_incomodidad_silencio_contar_seis` (`cap_13`, 12 pasos) | **`CONTINUA`**, arista **`D.29`**, madre la de `cap_09` | `ACTA_AUDITOR.md` **`L21081`**, discutible `8`: *lei los 12 pasos contra los 20. Aquel entrega la primera critica arrancada a un equipo entero con sus seis consejos; este entrega un ensayo con un companiero amistoso y la cuenta de cuantos segundos aguanta, que aquel no tiene. Procedimiento en los dos lados: no es gemelo* |
| `abrazar_incomodidad_arrancar_critica_equipo` contra `escuchar_entender_critica_dominar_defensa` | **`CONTINUA`**, arista **`D.29`**, paso `12` de la madre | `ACTA_AUDITOR.md` **`L21243`** y siguientes: la tabla de los cuatro elementos pone *escuchar con intencion de entender* en `P12` y `P13` de la madre |
| `abrazar_incomodidad_arrancar_critica_equipo` contra `premiar_franqueza_hacer_escucha_tangible` | **`CONTINUA`**, arista **`D.29`**, paso `14` de la madre | misma tabla, `L21243`: *hacer tangible la escucha premiando la franqueza* vive en `P14`, `P15` y `P17` de la madre |

**Y LO COMPRUEBO EN LOS PASOS EN VEZ DE FIARME DE LA CITA**, que es lo que la vara pide:

- **Madre `P09`:** *Cuenta hasta seis antes de decir nada mas, obligando a la otra persona
  a aguantar el silencio*. **Hijo `P07` a `P10`:** *hazle tu pregunta a un companiero
  amistoso y cuenta hasta seis; no te permitas decir nada; fijate en cuantos segundos
  aguanta tu companiero*. **La madre NOMBRA la tecnica dentro de una conversacion real; el
  hijo monta un ENSAYO con otra persona, otro proposito y un observable propio.** Eso es
  `NOMBRAR NO ES PROCEDIMENTAR` (`P.5.1`) con la direccion bien puesta: **lo que el hijo
  le aniade a la madre**, no al reves.
- **Madre `P12`:** *Escucha con intencion de entender y no de responder... repite lo que
  dijo... aclara la critica sin debatirla*. **Hijo `P03` a `P13`:** el inventario de
  medios (respiracion, trago de agua) **mas** el ejercicio de los tres minutos con sus
  turnos, sus prohibiciones y su medida. **La madre da una frase; el hijo da un ejercicio
  con etapas.** `CONTINUA`.
- **Madre `P14` y `P15`:** *Premia la critica... haz el cambio cuanto antes... si no estas
  de acuerdo, primero busca algo con lo que si*. **Hijo `P08` a `P20`:** la lista de tres
  o cuatro criticas recientes, la reunion donde se cuenta, y **un segundo ejercicio
  rotulado** para la critica con la que no estas de acuerdo. **Aqui el solape es el mayor
  de los tres y lo digo:** el `P15` de la madre y el `P16` a `P19` del hijo hacen el mismo
  movimiento. **Pero la vara `6.1` dice que el tamanio del solape no decide**, y lo que
  queda fuera es procedimiento en los dos lados: la madre no tiene la lista ni la reunion,
  y el hijo no tiene la goma elastica ni el agendar y volver. `CONTINUA`.

**LOS TRES SE SOSTIENEN CON MI LECTURA DE HOY.** No aporto clase nueva: **aporto que la
volvi a leer y que sale donde ya estaba**, que es lo unico que una segunda lectura puede
aportar honestamente.

### 7.2. LA ARISTA `D.37` DESDE LA CABEZA DE `cap_13`, QUE ES OTRA FAMILIA

| par | mi clase | lo que la sostiene |
|---|---|---|
| `pedir_critica_primero_crear_seguridad_psicologica` contra los tres | **`CONTINUA`**, arista **`D.37`** | **la cuenta escrita**, `L113` *the four tips* y `L237` que los nombra uno a uno. `grep` de la seccion `1.1`: **`2`** |

**NO CONFUNDO LAS DOS FAMILIAS, QUE ES DONDE ME CAI LA VUELTA PASADA.** La misma pareja de
nodos puede tener **dos madres de dos especies distintas**: la de `cap_09` por lectura
(`D.29`, `grep` `0`) y la de `cap_13` por cuenta escrita (`D.37`, `grep` `2`). **Las dos
son ciertas a la vez y ninguna sustituye a la otra.**

### 7.3. EL PAR DE `0.446`: `escuchar_entender` CONTRA `abrazar_incomodidad`

**MI CLASE, ADJUDICADA CON LOS `13` PASOS CONTRA LOS `12` DELANTE: `SANO`. SON DOS NODOS.**

| | `abrazar_incomodidad_silencio_contar_seis` | `escuchar_entender_critica_dominar_defensa` |
|---|---|---|
| **cuando** | **antes** de que exista respuesta: aguantas el silencio | **mientras** la critica llega: dominas tu defensa |
| **ejercicio** | contar hasta seis con un companiero amistoso | hablar y escuchar tres minutos sin interrumpir |
| **entregable** | el silencio aguantado, con la respuesta salida del otro | la critica escuchada entera sin respuesta defensiva |

**Ninguno de los dos ejercicios sirve para lo del otro.** Y `L237` **los enumera por
separado**, como elementos segundo y tercero de los cuatro, comprobado por mi en el
fichero (seccion `1.1`).

**Y ESTO YA ESTABA ADJUDICADO, ASI QUE LO CITO:** `ACTA_AUDITOR.md` discutible `12` de la
`ACTA 24`, *el par de `0,449` son dos nodos y no uno, SE SOSTIENE*. **Salgo al mismo sitio
y lo firmo.**

> **UNA CIFRA QUE SE MOVIO Y NO LA DEJO PASAR:** alli el par media **`0,449`** y hoy mide
> **`0,446`**. **No es una discrepancia: es la misma senial sobre una poblacion mayor.** La
> escribo porque `AUDITOR_FORJA.md` 1.1 manda declarar la discrepancia en vez de resolverla
> copiando, y porque **una cita que arrastra la cifra vieja acaba publicando una cifra
> falsa tres actas despues.**

### 7.4. EL PAR DE `0.634`, QUE ES LA SENIAL MAS ALTA DE TODA LA COLA Y NO ES UN PAR

    $ python -c "pasos de cambiar_forma_trabajar_conservar_plantilla"
      P02. Centrate en trabajar con lo que tienes, que es lo que el texto
           recomienda por encima de mucha rotacion.

    $ python -c "paso 4 de escuchar_entender_critica_dominar_defensa"
      P04. Y sobre todo practica con otros, que es lo que el texto pone
           por encima de lo demas.

**MI CLASE: `SANO`. NI GEMELO, NI `CONTINUA`, NI ARISTA.** Y no por poco:

| | `escuchar_entender` `P04` | `cambiar_forma_trabajar` `P02` |
|---|---|---|
| **libro** | `scott_radical_candor`, `cap_13` | **`marquet_turn_the_ship`**, otro libro |
| **de que habla** | con quien ensayar a escuchar critica | no renovar la plantilla de un barco |
| **lo que comparten** | `que es lo que el texto ... por encima de ...` | lo mismo, **palabra por palabra de la formula** |

> **`LECTURA`, y es el hallazgo que traigo yo a esta apertura:** la senial mas alta de toda
> la cola de lectura, **la unica que cruza el umbral de `0.60`**, **no mide contenido: mide
> la formula con la que esta casa escribe sus pasos.** Los dos pasos comparten la cascara
> `que es lo que el texto [verbo] por encima de [X]` y **no comparten ni libro, ni dominio,
> ni acto.**

**Y NO ES UNA IMPRESION MIA: LA MIDO SOBRE LA POBLACION ENTERA.**

    $ python -c "censo de formula sobre grafo mas bandejas"
      poblacion barrida: 348   (grafo 325 + bandejas 23)
        'que es lo que el texto'     :  57 nodos    76 pasos
        'Cuenta con lo que el texto' :  50 nodos    57 pasos
        'Parte de lo que'            :  14 nodos    14 pasos
        pasos totales de la poblacion: 3213

**`57` nodos de `348` llevan la misma cascara en algun paso, y `50` llevan la otra.** Con
esa densidad, **dos nodos cualesquiera de esta casa comparten texto sin compartir nada**.

**ES UN CONTRAEJEMPLAR MEDIDO PARA LA PREGUNTA `8` DE LA COLA DE DOCTRINA**, que dice
*la senial 1 compara titulo mas resumen_teorico mas pasos, y en un lote escrito de una
sentada eso mide la formula del extractor tanto como el contenido del nodo*. **Lo que
aniado hoy es que tambien le pasa a `paso_contra_nodo`, que es la otra senal**, y que le
pasa **por encima del umbral** y **cruzando dos libros distintos**.

**NO TOCO NINGUN UMBRAL Y NO PIDO QUE SE TOQUE** (`AUDITOR_FORJA.md` 2: los umbrales son
de Alexis para cambiar de raiz, y ninguna vuelta los mueve). **Lo dejo medido en la cola,
que es donde vive.**

### 7.5. EL PAR DE `0.393`: LA MISMA FIGURA, OTRA VEZ

    P04 de escuchar_entender : Y sobre todo practica con otros, que es lo que el texto
                               pone por encima de lo demas.
    P03 de contar_historias  : Pero explicala sobre todo con tus propias palabras, que es
                               lo que el texto dice que sale mejor.

**MI CLASE: `SANO`.** Uno ensaya a escuchar critica con una pareja; el otro explica la
franqueza radical al equipo con historias propias. **Ni el mismo momento, ni el mismo
acto, ni el mismo entregable.**

> **Y AQUI VA LA CIFRA QUE CIERRA EL ARGUMENTO DE `7.4`:** de los `4` vecinos que la aduana
> levanta para `escuchar_entender`, **`3` los levanta el MISMO paso, el `P04`**, que es
> **el paso mas corto del nodo y el que menos contenido propio tiene**. El cuarto lo
> levanta el `P05`. **Un solo paso de formula abre tres cuartas partes de la cola de
> lectura de un candidato.**

### 7.6. EL PAR DE `0.363` Y `0.375`: DOS HERMANOS DE LA MISMA CABEZA

**MI CLASE: `SANO`, y ademas HERMANOS declarados.** Son el elemento `3` y el elemento `4`
de la enumeracion de `L237`, los dos cuelgan por `D.37` de
`pedir_critica_primero_crear_seguridad_psicologica`, **y una arista entre hermanos no la
pide ninguna regla**. `L237` los separa en el propio texto.

---

## 8. FIDELIDAD `D.30`: MI LECTURA PASO A PASO CONTRA SUS LINEAS

**Releo los `33` pasos de los dos candidatos que siguen en bandeja contra el fichero
fuente.** **NO releo los `12` del candidato que entro**: el encargo declara que su
fidelidad ya se corrio dos veces, por el extractor y por mi, y `D.47` (modo austero) dice
que lo que el registro ya dice no se repite.

    $ awk 'NR>=199 && NR<=214 && NF' fuentes/scott_radical_candor/cap_13.md | wc -l
      8
    $ awk 'NR>=215 && NR<=234 && NF' fuentes/scott_radical_candor/cap_13.md | wc -l
      10
    $ grep -n "^Practice:" fuentes/scott_radical_candor/cap_13.md
      193:Practice: Count to six in your head
      207:Practice: Listening
      223:Practice: Make Listening Tangible
      231:Practice: Reward criticism you disagree with

### 8.1. `escuchar_entender_critica_dominar_defensa`, `13` pasos, `L199` a `L214`

| pasos | linea que los sostiene |
|---|---|
| `P01`, `P02` | `L203` *fight, flight, or freeze... Unjust criticism is hard, but fair criticism... is also hard* |
| `P03`, `P04` | `L205` *a breathing exercise can help; so can taking a long sip from a bottle of water. Most of all, practice with others* |
| `P05` a `P08` | `L209` *Find a partner... One person speaks for three minutes... whatever you want* |
| `P09` a `P12` | `L211` *the gift of your full attention... not the time for questions... your favorite Hawaii vacation story... Your job is not to give advice* |
| `P13` | `L213` *more than ten years learned more about each other in three minutes than they did in a decade* |

> # **`13` de `13` TRANSCRIPCION. `0` `PUENTE`.**

### 8.2. `premiar_franqueza_hacer_escucha_tangible`, `20` pasos, `L215` a `L234`

| pasos | linea que los sostiene |
|---|---|
| `P01`, `P02` | `L217` *they are taking a risk... address the problem quickly or explain clearly why you can't* |
| `P03`, `P04` | `L219` *negativity bias... nine times out of ten... Rick Hanson... Velcro... Teflon* |
| `P05` a `P07` | `L221` *Spanx CEO Sara Blakely played the song Oops! I Did It Again... a gift, not a kick in the shins* |
| `P08` a `P10` | `L225` *the three to four times... go on a fishing expedition! And fish for criticism not praise!* |
| `P11` a `P13` | `L227` *At a team meeting or standup... Ask for help from the team... welcome it with relish* |
| `P14`, `P15` | `L229` *two good things happen... Show your work!... gone too far, or not far enough... calibrate your response* |
| `P16` a `P20` | `L233` *find some element... open to a longer conversation... Pretending to listen... A respectful disagreement can strengthen a relationship* |

> # **`20` de `20` TRANSCRIPCION. `0` `PUENTE`.**

**Y DIGO LO QUE HE VISTO QUE FALTA, PORQUE UNA OMISION NO ES UN PUENTE PERO SI ES UNA
LECTURA:** el `P14` se come el ejemplar de `L229` (*aiming to avoid interrupting people,
you've allowed meetings to become free-for-alls*). **La `ACTA 39` ya sostuvo ese mismo
discutible**, asi que lo registro y no lo reabro.

### 8.3. `PASOS INVENTADOS`: LA FILA QUE FIRMO Y LA QUE NO

| tramo | denominador | `PUENTE` | por ciento | firma |
|---|---:|---:|---:|---|
| los `2` que he releido hoy entero, paso a paso | **`33`** | **`0`** | **`0,00`** | **LA FIRMO** |
| los `3` del tramo, con los `12` que no he releido | `45` | `0` que declara el registro | `0,00` | **NO LA FIRMO HOY**: `12` de esos pasos los firme en la `ACTA 39` y hoy no los he vuelto a abrir |
| `cap_13` entero | `212` | pendiente | pendiente | **NO LA FIRMO**: siguen sin releer por mi los pasos de `dar_elogio` (`20`), `integrar_peticion` (`13`) y `medir_critica` (`33`) |

**LAS TRES CIFRAS DE PASOS DE LA ULTIMA FILA SON MIAS Y SALEN DEL INSTRUMENTO**, no del
reporte:

    $ python -c "len(pasos_accionables) por candidato de la bandeja"
      cap_13    20  dar_elogio_disciplina_igual_critica
      cap_13    13  escuchar_entender_critica_dominar_defensa
      cap_13    13  integrar_peticion_critica_rutina_existente
      cap_13    33  medir_critica_respuesta_oyente_brujula
      cap_13    20  premiar_franqueza_hacer_escucha_tangible

**EL `212` DE `cap_13` ENTERO LO ARRASTRO DEL REGISTRO Y NO LO HE REMEDIDO**, y por eso va
sin negrita y con la firma en NO: **`D.38.3` me deja citarlo, no publicarlo como mio.**

> **`0,00` POR CIENTO ESTA MUY POR DEBAJO DEL TOPE DE `10`** (`8.1`), asi que **por
> volumen el tramo pediria SUBIR**. No lo encargo aqui: la apertura ciega publica clases y
> lecturas, y el volumen se decide en el acta con el reporte delante.

---

## 9. LO QUE VI Y NO DEBIA VER, DECLARADO ANTES DE QUE ME LO ENCUENTRE OTRO

**ES UNA CAIDA MIA Y LA ESCRIBO YO.** Al inspeccionar el formato de
`bitacora/VEREDICTOS.jsonl` corri un `tail -8` para ver que campos trae, **y esas ocho
lineas son las que la cadena de esta vuelta acababa de escribir a las `08:53`**. Vi:

- las **tres aristas** que la vuelta declaro para el candidato `1`, con sus madres.
- el **arranque de la `razon`** de tres de sus veredictos, truncado a unos cien caracteres.
- que sus tres lineas de vecino llevan `arista` vacia.

**LO QUE ESO CONTAMINA, EXACTAMENTE, Y LO QUE NO:**

| | |
|---|---|
| **contaminado** | los pares del candidato `1` contra `escuchar_entender`, `premiar_franqueza` y `contar_historias`. **Mi clase de esos tres no la publico como ciega**, y donde la doy (seccion `7.3`) **la doy citando la `ACTA 24`, que es anterior a esta vuelta y no es del extractor** |
| **NO contaminado** | **todo lo de los candidatos `2` y `3`**, y lo mido en vez de afirmarlo |

    $ python -c "conteo por candidato sobre toda la bitacora, sin leer razones"
      escuchar_entender_critica_dominar_defensa   como candidato en toda la bitacora: 0
      premiar_franqueza_hacer_escucha_tangible    como candidato en toda la bitacora: 0
      abrazar_incomodidad_silencio_contar_seis    como candidato en toda la bitacora: 6

**CERO Y CERO.** No existe ni una linea de veredicto sobre los candidatos `2` y `3` en toda
la bitacora, asi que **no habia nada que ver y mi lectura de ellos es ciega entera**. **La
del candidato `1` no, y por eso lleva esta nota encima en vez de una firma.**

**NO ME ABSUELVO Y TAMPOCO ME CARGO DE MAS.** `bitacora/VEREDICTOS.jsonl` es fuente de
verdad `3` de mi protocolo y no es ninguno de los ficheros que `D.34.2` retira, asi que
**abrirlo no esta prohibido**; lo que hace `1.2` es ordenar el ORDEN: primero los pasos,
la clase despues, **y la razon escrita la ultima**. **Yo lei los pasos primero en los tres
casos**, pero destape razon ajena antes de cerrar mi clase de esos tres pares. **La
diferencia entre declararlo y callarlo es todo lo que esta fase vale.**

**Y LO QUE ME LLEVO PARA NO REPETIRLO:** en una fase ciega **el formato de un fichero se
mira por su cabeza y no por su cola**. `head` no me habria ensenado nada de hoy.

---

## 10. LO QUE NO PUBLICO, Y POR QUE NO LO PUBLICO

**`D.38.3` dice que una cifra sin instrumento no se publica. Estas son las que me callo:**

| lo que no publico | por que |
|---|---|
| **la racha viva de la linea, medida** | el instrumento esta roto por retirada de fichero (seccion `3.1`) y **publica un cero falso**. La leo del acta: `REPORTE 1 de 3`, `CLASE 0 de 2`, `CIFRA PUBLICADA 0 de 2`, `DATO MOVIDO 0 de 2`, `AUDITOR 2 de 3` (`ACTA_AUDITOR.md` `L32134`, `L32147`) |
| **cuantos candidatos entraron en la vuelta 41** | lo sabria por el reporte, que no tengo. **Lo que mido es el estado del arbol AHORA**: `1` de los `3` del tramo esta en `_insertados` y `2` siguen en bandeja, y eso es una foto de un momento, no un cierre de vuelta |
| **`PASOS INVENTADOS` de `cap_13` entero** | `66` de sus pasos de bandeja siguen sin releer por mi (seccion `8.3`) |
| **si la vuelta cerro su reporte** | no tengo el reporte. **Esa es la pieza que el acta juzga, no la apertura** |

---

## 11. EL TABLERO Y EL LIBRO (`D.49`)

    $ python forja.py tablero --puedo scott_radical_candor
      LINEA 'serial', LIBRO 'scott_radical_candor': SI
        'scott_radical_candor' ya es de esta linea ('serial'): continuarlo es lo que toca.

    $ cat docs/loop/TABLERO.jsonl        (leido, no recontado)
      scott_radical_candor : lote 4, dueno 'serial', CERRADO EN EXTRACCION, 13 capitulos minados
      grove_high_output    : lote 7, EN CURSO,  rama extraccion-grove_high_output
      marquet_turn_the_ship: lote 5, PAUSADO,   rama extraccion-marquet_turn_the_ship
      gerber_emyth         : lote 9, PAUSADO,   rama extraccion-gerber_emyth
      cola de doctrina     : 11 preguntas, 0 bloquean

> # **LIBRO DE ESTA VUELTA: scott_radical_candor**

**`D.45` SIGUE MANDANDO EN LO QUE PUEDO TOCAR:** con `grove_high_output` `EN CURSO` en otra
rama, **no toco `src/`, ni el banco, ni el arnes, ni los protocolos**, ni siquiera para
arreglar el quinto fichero retirado de la seccion `3`.

**Y APUNTO UNA COSA DE LA SECCION `7.4` QUE NO ES DOCTRINA SINO OPERACION:** el vecino mas
alto de un candidato de `scott` **es un candidato de `marquet`, un frente PAUSADO cuya
bandeja vive en este mismo repo**. Sea cual sea el veredicto, **la vuelta que inserte
`escuchar_entender` tendra que escribir un veredicto que cruza dos libros y dos lineas.**
Lo dejo dicho aqui porque es el tipo de cosa que se descubre a las `07:12`, cuando la
cadena ya fallo.

---

## 12. LO QUE HE HECHO EN ESTA FASE Y LO QUE NO

| | |
|---|---|
| **he corrido** | `gate` (dos veces, y por eso vi la seccion `2`), `guiones`, `resolutor`, `rancios`, `credito`, `credito --lineas`, `tablero --puedo`, `herencia --comprobar`, la suite entera, **dos `forja.py informe` de SOLO LECTURA**, y mis propios `grep`, `wc`, `awk`, `stat` y conteos de `python -c`, **todos declarados con su salida al lado** |
| **he leido** | `AUDITOR_FORJA.md` entero, `ACTA_AUDITOR.md` (permitido y necesario, `D.40`), `PROMPT_SIGUIENTE.md` (sede mia), `ORDEN_DE_LOTES.md`, `TABLERO.jsonl`, `fuentes/scott_radical_candor/cap_13.md` y `cap_09.md`, y los `json` de los candidatos y de sus vecinos |
| **NO he abierto** | `docs/loop/REPORTE.md`, `loop.log`, `ultimo_extractor.json`, `ultimo_auditor.json` **ni los he recuperado de git por ninguna via**. Tampoco he abierto **`PARA_ALEXIS.md`**, que **si esta en el arbol y no me esta vedado**, porque lo escribio la vuelta que vengo a auditar y leerlo en esta fase seria leer su conclusion. Tampoco he abierto el contenido de `.v41/`: **de esos ficheros solo he mirado fecha y tamanio**, que es metadato y no afirmacion suya |
| **NO he escrito** | nada fuera de este fichero. **Ni `dataset/`, ni `bitacora/`, ni `cuarentena/`, ni `config/`, ni `censos/`, ni `src/`, ni `tests/`.** Los `informe` son de solo lectura por construccion y su propia salida lo dice: *NADA SE INSERTO* |
| **NO he commiteado** | el arnes sella este fichero y lo commitea el |

**Y LA COMPROBACION DEL `D.40` LA CORRO YO, ANTES Y DESPUES**, porque el instrumento mide
el fichero que estoy escribiendo y una sola de las dos salidas no probaria nada:

    $ python forja.py herencia --comprobar        (antes de escribir este fichero)
      APERTURA CIEGA INCOMPLETA: 1 cosa(s) que faltan (D.40).
        docs/loop/APERTURA_CIEGA.md no existe

    $ python forja.py herencia --comprobar        (con este fichero ya escrito)
      APERTURA CIEGA COMPLETA: el acta anterior va leida por su huella y el heredado
      va declarado.

**Las dos juntas son la prueba: el instrumento SABE fallar y hoy no falla.** Un `CUMPLIDO`
de la seccion `0` sin nada corrido detras seria exactamente el `NO APLICA` sin salida que
`D.40` prohibe.

    $ python forja.py guiones docs/loop/APERTURA_CIEGA.md
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

---

## 13. LA FOTO, EN UNA TABLA

| | |
|---|---|
| rama y commit | `extraccion-mundo-11`, `94ecb9f82c7eae0cd112951c1c23d4ba00913253` |
| **acta anterior leida** | **`266e5197978cc8a83ca859b5b75e9c7d3444e6fd`**, verificada con `git hash-object` |
| **`HEREDADO 1`** | **CUMPLIDO**, secciones `1.1` y `1.2` |
| grafo | **`325`** nodos, **`138`** aristas dirigidas, **`514`** veredictos (`SANO` `346`, `CONTINUA` `158`, `CORREGIDO` `10`) |
| bandeja lote 4 | **`20`** (`cap_13` **`5`**, `cap_14` **`15`**), insertados **`122`** |
| poblacion del barrido | **`348`** (`325` grafo mas `23` bandejas), **mia y la de la aduana coinciden** |
| cola de aristas | **`16`** lineas, **`12`** cableadas, **`4`** esperando extremo, **`0`** con los dos dentro y sin cable |
| guardas | gate **VERDE** sobre `325`, guiones **VERDE**, suite **`294 / 3 fallos / 1 error`**, los `4` por ficheros que el arnes retira |
| vigencia (`D.15`) | **`64`** `RANCIO`, **`8`** `SIN HUELLA`, `14` lineas no consumadas |
| mis clases de esta fase | **`3` `CONTINUA`** (`D.29`, los tres de la `ACTA 24`), **`1` `CONTINUA`** (`D.37`, desde la cabeza de `cap_13`), **`4` `SANO`** |
| fidelidad que FIRMO | **`33` de `33` TRANSCRIPCION, `0` `PUENTE`, `0,00` por ciento** |
| lo que declaro contra mi | **la contaminacion de la seccion `9`**, en los tres pares del candidato `1` |
| lo que subo sin adjudicar | **la poblacion movida en fase sellada** (tercer ejemplar, seccion `2`), **el quinto fichero retirado y su cero falso** (seccion `3`), **la senial de `0.634` que mide formula y no contenido** (seccion `7.4`) |

---

*Escrito sin haber visto `docs/loop/REPORTE.md`. Cada cifra de arriba lleva su instrumento
pegado al lado y cada conclusion va marcada como `LECTURA` y separada de su cifra, como
mandan `D.38.3` y su ensanche del 16 sep 2026. No commiteo: el arnes sella.*
