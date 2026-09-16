# APERTURA CIEGA DE LA VUELTA 28, lote 4 (`scott_radical_candor`), `cap_07` mas la cabeza de `cap_11`

*Escrita por el **auditor** en su fase ciega, antes de que el arnes le exponga
`docs/loop/REPORTE.md`. Sede del auditor por `AUDITOR_FORJA.md` 5.6.*

> **LO QUE MANDA EN ESTA PAGINA.** `D.38.3`: aqui se publican **clases y lecturas**, y toda
> cifra sale de **un instrumento corrido en esta misma fase, con su salida literal pegada al
> lado**. `D.38.3` ensanchada: **la linea que acompania a una cifra dice lo que el instrumento
> MIDIO**, y toda conclusion sobre contenido va en linea aparte marcada **`LECTURA`**.
> `D.38.4`: mi barrido es sobre **grafo mas bandejas**.
>
> **Y MANDA UNA COSA MAS, QUE ES MIA Y ME LA ENCARGUE YO** (`ACTA 27` seccion `10`, remedio `1`):
> **ninguna celda de esta pagina publica como cifra cerrada el resultado de una lectura que mi
> turno normal todavia tiene que adjudicar.** Eso va marcado **`POR ADJUDICAR`**, y la seccion `9`
> los reune todos.
>
> **DOS AVISOS DE FORMA, PARA QUE NADIE COTEJE CONTRA UNA COPIA MAL LEIDA:**
>
> 1. **Las citas del libro llevan sus guiones largos cambiados por coma**, porque esta casa prohibe
>    el guion largo y el medio en todo lo que escribe y **el barrido me mide a mi tambien**
>    (`$ python forja.py guiones docs/loop/APERTURA_CIEGA.md` sale **VERDE**). **El fichero fuente no
>    se ha tocado**, y publico su huella en la seccion `3` para que se pueda comprobar.
> 2. **Donde recorto una fila larga de una salida escribo `...`**, y **ninguna cifra ni ningun id va
>    abreviado dentro de un bloque que se presente como salida de instrumento**: eso lo comprueba un
>    lector, no mi buena intencion (seccion `8.1`).

---

## 0. LA DECLARACION QUE EL ARNES EXIGE (`D.40`)

    ACTA ANTERIOR LEIDA: 1f7f256d3dce8bb70708b83f303f8d75953dfa0c
    HEREDADO 1: CUMPLIDO

### 0.1. LA HUELLA, COMPROBADA CON EL INSTRUMENTO Y NO DADA POR BUENA

**No me basta con copiar la huella que el prompt me da: compruebo que el fichero que tengo
delante es ese.**

    $ git hash-object docs/loop/ACTA_AUDITOR.md
      1f7f256d3dce8bb70708b83f303f8d75953dfa0c

    $ git rev-parse HEAD:docs/loop/ACTA_AUDITOR.md
      1f7f256d3dce8bb70708b83f303f8d75953dfa0c

    $ git diff --stat HEAD -- docs/loop/ACTA_AUDITOR.md
      (vacio)

    $ wc -l docs/loop/ACTA_AUDITOR.md
      25204 docs/loop/ACTA_AUDITOR.md

**Las tres salidas dicen lo mismo: el acta del arbol, la del ultimo commit y la huella heredada
son el mismo objeto al caracter.** He leido la `ACTA 27` entera, de la linea `24413` a la `25204`,
**y con ella la seccion `10`, que es la que me encargue a mi mismo** y que el arnes no me entrego
porque su extractor de herencia se quedo con el `REMEDIO` de `5.2`.

### 0.2. `HEREDADO 1`: **CUMPLIDO**, y lo digo con las DOS mitades medidas

**Lo que el heredado pedia** (`ACTA 27` `5.2`, encargado como `TAREA 2` de la vuelta 28): que una
insercion rechazada **no escriba nada**, y que las cuatro lineas ya escritas **se declaren NO
CONSUMADAS en su sitio, por una operacion y no a mano, sin borrarlas.**

**MITAD A, LA ATOMICIDAD. Comprobada sobre el codigo, que es donde vive:**

    $ grep -rn "agregar_jsonl\|escribir_jsonl" src/ | grep -i "veredicto"
      src/aduana.py:905:        comun.agregar_jsonl(ruta_veredictos, registro)
      src/anotacion.py:217:    comun.escribir_jsonl(ruta_veredictos, futuro)
      src/arista.py:190:    comun.agregar_jsonl(ruta_veredictos, registro)
      src/correccion.py:204:    comun.agregar_jsonl(ruta_veredictos, registro)

    $ grep -n "_consumar_veredictos" src/aduana.py
      890:def _consumar_veredictos(ruta_veredictos, registros):
      1242:        # corrida se consuma. Ver `_consumar_veredictos`.
      1251:        _consumar_veredictos(ruta_veredictos, registros)
      1369:    _consumar_veredictos(ruta_veredictos, registros)

    $ sed -n '1240,1243p' src/aduana.py
      # LA INSERCION ES ATOMICA (D.29 llegando al codigo, ACTA 27 5.2). El
      # registro se GUARDA, no se escribe: la escritura llega abajo, cuando la
      # corrida se consuma. Ver `_consumar_veredictos`.
      registros.append(registro)

    $ sed -n '1366,1369p' src/aduana.py
      # LA CORRIDA SE CONSUMA AQUI, Y NO ANTES. Desde este punto no hay ningun
      # camino que devuelva `RECHAZADO`, asi que es el sitio donde la bitacora
      # puede decir la verdad sobre lo que la aduana hizo.
      _consumar_veredictos(ruta_veredictos, registros)

**LO QUE LA SALIDA MIDE:** la unica escritura de `aduana.py` a la bitacora es la linea `905`,
**que esta dentro de `_consumar_veredictos`**, y a esa funcion se la llama **desde dos sitios y
solo dos**: el `1251` (el camino `REPITE`, que si se consuma) y el `1369`, **detras del gate de la
simulacion y de todos los `RECHAZADO`**. El bucle por vecino ya no escribe: **acumula** (`1243`).

**MITAD B, LAS CUATRO LINEAS. Comprobada sobre el dato:**

    $ python -c "... consumada de cada linea de bitacora/VEREDICTOS.jsonl ..."
      lineas totales            : 289
        consumada=False  -> 14
        consumada=None   -> 275
      linea 248  SANO                         recorrer_rueda_hacer_cosas_equipo              recorrer_trece_elementos_proceso_evaluacion_formal
      linea 249  CONTINUA                     recorrer_rueda_hacer_cosas_equipo              recorrer_rueda_conscientemente_cultura_equipo
      linea 250  SANO                         recorrer_rueda_hacer_cosas_equipo              reconocer_emociones_propias_avisar_equipo
      linea 251  CONTINUA                     recorrer_rueda_conscientemente_cultura_equipo  recorrer_rueda_hacer_cosas_equipo

    $ sed -n '248,251p' bitacora/VEREDICTOS.jsonl     (lo que cada una lleva dentro)
      "anotaciones": [{"fecha": "2026-09-16", "no_consumada": true, "razon": "la corrida que
      escribio esta linea imprimio RECHAZADO y dejo el grafo intacto; la aduana registra lo que
      HIZO (EXTRACTOR.md 14) y esta corrida no hizo nada", "texto": "CORRECCION DECLARADA del
      16 sep 2026 (ACTA 27 5.2, TAREA 2.c de la vuelta 28): esta linea NO SE CONSUMO. ..."}]
      ..., "consumada": false, ...

    $ python forja.py | grep -A2 anotar
      python forja.py anotar --linea <n> --anade "CORRECCION DECLARADA ..." --razon R
                             [--no-consumada]
                                        correccion declarada sobre una linea ya
                                        escrita de bitacora/VEREDICTOS.jsonl

**LO QUE LA SALIDA MIDE:** las cuatro lineas `248` a `251` **siguen ahi**, llevan `consumada:
false`, llevan un bloque `anotaciones` con su razon y su fecha, **y el texto viejo sigue literal
delante del nuevo** (la razon original de cada linea se lee entera antes de la marca). **Y existe
una operacion, `forja.py anotar --no-consumada`**, o sea que no se hizo a mano.

**Y LA VIGENCIA YA LAS DESCUENTA, que es la prueba de que la marca sirve para algo:**

    $ python forja.py rancios
      BLOQUE DE VIGENCIA: 34 hallazgo(s) sobre 275 veredicto(s) y 0 cita(s).
        RANCIO 26, SIN HUELLA 8
        lineas declaradas NO CONSUMADAS y por eso no medidas: 14
          (las escribio una corrida que no inserto nada; ver su razon en la propia linea)

**`289` lineas menos las `14` no consumadas son los `275` que la vigencia mide.** Cuadra.

> **`LECTURA`: doy `HEREDADO 1` por `CUMPLIDO` en sus dos mitades, pero el remedio de la
> atomicidad se cumplio DESPUES de que la propia vuelta lo rompiera diez veces mas**, y eso no lo
> adjudico aqui: va a la seccion `9` como **`POR ADJUDICAR 1`**, con sus cifras en la `6.3`.

---

## 1. LAS GUARDAS DE LA CASA, CORRIDAS POR MI EN ESTA FASE

<!-- salida: .v29/guardas_v29.txt y .v29/pruebas_v29.txt -->

    $ python forja.py gate
      GATE VERDE.
        nodos verificados: 243
        guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada,
                 vuelta, cita_incompleta, deprecado_en_superficie, arista_rota,
                 arista_incompleta, guiones

    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python forja.py resolutor
      nodos vivos: 243
      nodos deprecados (archivo): 0
      alias registrados: 0

    $ python forja.py rancios
      BLOQUE DE VIGENCIA: 34 hallazgo(s) sobre 275 veredicto(s) y 0 cita(s).
        RANCIO 26, SIN HUELLA 8

    $ python tests/test_aceptacion.py
      total: 176 pruebas, 1 fallos, 0 errores

    $ python scripts/censar_rutas.py
      rutas publicadas y censadas : 96
        pasan                     : 92
        CAEN                      : 4
      CENSO EN ROJO: 4 ruta(s) publicadas como sede de una cifra no sostienen nada.

| instrumento | **lo que su salida dice** |
|---|---|
| `gate` | **VERDE**, `243` nodos verificados, `12` guardas |
| `guiones` | **VERDE** |
| `resolutor` | `243` vivos, `0` deprecados, `0` alias |
| `rancios` | `34` hallazgos sobre `275` veredictos: `RANCIO 26`, `SIN HUELLA 8` |
| `test_aceptacion` | `176` pruebas, **`1` fallo**, `0` errores |
| `censar_rutas` | **ROJO**, `4` de `96` |

### 1.1. **LAS DOS EN ROJO SON LA MISMA COSA, Y LA CAUSA ES MI PROPIA FASE CIEGA**

**La prueba que cae y el censo que cae tienen un solo motivo, y lo mido en vez de suponerlo.**

    $ python tests/test_aceptacion.py   (el traceback de la unica que cae)
      FAIL: test_e_guion_largo_rompe_el_hook (__main__.PruebaE.test_e_guion_largo_rompe_el_hook)
      AssertionError: 1 != 0 : el repo ha de estar limpio antes de ensuciarlo:
        [pre-commit] gate de integridad          GATE VERDE. nodos verificados: 243
        [pre-commit] barrido de guiones          BARRIDO DE GUIONES VERDE
        [pre-commit] tallado del reporte (D.41) y censo de rutas (D.42)
        File "scripts/tallar_reporte.py", line 315, in revisar
          texto = io.open(ruta_reporte, encoding="utf-8").read()
        FileNotFoundError: [Errno 2] No such file or directory:
          'C:\\Users\\AlexDesk\\Documents\\forja-nodos\\docs\\loop\\REPORTE.md'
        CIERRE EN ROJO. No pasa: tallado del reporte (D.41)
        [pre-commit] COMMIT ABORTADO

    $ python scripts/censar_rutas.py   (las cuatro que caen, por su ruta)
      CAE  docs\loop\ACTA_AUDITOR.md linea 2583, celda 1   ruta : docs/loop/loop.log
      CAE  docs\loop\ACTA_AUDITOR.md linea 5765, celda 2   ruta : docs/loop/REPORTE.md
      CAE  docs\loop\ACTA_AUDITOR.md linea 14622, celda 1  ruta : docs/loop/ultimo_apertura.json
           esta y esta VACIA, y la celda no lleva la marca 'VACIA A PROPOSITO'
      CAE  docs\loop\ACTA_AUDITOR.md linea 22372, celda 2  ruta : docs/loop/REPORTE.md

    $ for f in REPORTE.md loop.log ultimo_extractor.json ultimo_auditor.json ultimo_apertura.json
      AUSENTE   (retirado del arbol)  docs/loop/REPORTE.md
      AUSENTE   (retirado del arbol)  docs/loop/loop.log
      AUSENTE   (retirado del arbol)  docs/loop/ultimo_extractor.json
      AUSENTE   (retirado del arbol)  docs/loop/ultimo_auditor.json
      PRESENTE  0 bytes  docs/loop/ultimo_apertura.json

    $ grep -n "DOCUMENTOS = " -A 2 scripts/censar_rutas.py
      DOCUMENTOS = (os.path.join("docs", "loop", "REPORTE.md"),
                    os.path.join("docs", "loop", "ACTA_AUDITOR.md"))

**LO QUE LAS SALIDAS MIDEN:** las **cuatro** rutas que el censo tumba son **tres ficheros que el
arnes retira del arbol por `D.34.2` para que yo escriba a ciegas**, mas uno que el arnes deja en
**cero bytes**. Y la prueba que cae, `test_e`, **no prueba los guiones: comprueba antes que el
repo este limpio**, y lo comprueba corriendo el hook, **que llama a `tallar_reporte.py`, que abre
`docs/loop/REPORTE.md` sin defensa y revienta con `FileNotFoundError`**.

> **`LECTURA`: los dos rojos no son de la vuelta 28. Son de la fase en la que estoy escribiendo.**
> `D.42` manda que toda ruta publicada sostenga su cifra; `D.34.2` manda retirar cuatro ficheros
> del arbol antes de mi turno. **Las dos reglas son vigentes y en esta fase se contradicen**, y la
> contradiccion no es de las que se arreglan leyendo mejor: **es mecanica y se repite en cada
> apertura ciega en la que cualquier acta haya citado `REPORTE.md` o `loop.log` en una celda.**
>
> **NO LO ADJUDICO AQUI Y NO LO ARREGLO AQUI**, por dos motivos que digo: `config/sedes_vacias.json`
> dice de si mismo *ESTA LISTA LA ESCRIBE EL FUNDADOR. Ni el extractor ni el auditor la tocan*, y
> `D.42` no me deja marcar `VACIA A PROPOSITO` en celdas de actas viejas que eran ciertas cuando se
> escribieron. **Va a la seccion `9` como `POR ADJUDICAR 2`.**

### 1.2. **Y UNA COSA QUE MIDO PORQUE ME TOCA A MI, NO AL EXTRACTOR**

    $ grep -n "DOCUMENTOS = " -A 2 scripts/censar_rutas.py
      DOCUMENTOS = (os.path.join("docs", "loop", "REPORTE.md"),
                    os.path.join("docs", "loop", "ACTA_AUDITOR.md"))

**LO QUE LA SALIDA MIDE: el censo de `D.42` lee dos ficheros, y `docs/loop/APERTURA_CIEGA.md` no es
ninguno de los dos.**

> **`LECTURA`: la pagina que estas leyendo NO la vigila el censo de rutas.** Y es una sede donde ya
> se publico una cifra falsa: **mi propia `ACTA 27` `8.1` la cuenta como `CIFRA PUBLICADA PROPIA`
> en esta misma sede sellada.** Lo digo porque es contra mi. **`POR ADJUDICAR 3`.**

---

## 2. LAS SEDES CONTADAS, Y LA POBLACION DEL BARRIDO (`D.38.4`, `D.38.5`)

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        243 dataset/nodos.jsonl
        289 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl

    $ python .v29/barrido_v29.py ...   (cabecera del instrumento)
      poblacion del barrido : 348   (243 del grafo mas 105 que esperan en bandejas)
      umbrales              : {"umbral_familia_id": 0.3, "umbral_paso_contra_nodo": 0.6,
                               "umbral_similitud_texto": 0.35}

    $ for d in cuarentena/*/ ; do contar *.json de nivel 1 ; done
      cuarentena/_derivadas/  -> 2 en bandeja (nivel 1)
      cuarentena/_insertados/  -> 0 en bandeja (nivel 1)
      cuarentena/ensayo_referencia_163/  -> 163 en bandeja (nivel 1)
      cuarentena/marquet_turn_the_ship/  -> 3 en bandeja (nivel 1)
      cuarentena/onu_consumidor/  -> 0 en bandeja (nivel 1)
      cuarentena/scott_radical_candor/  -> 102 en bandeja (nivel 1)
      cuarentena/smart_who/  -> 0 en bandeja (nivel 1)
      cuarentena/zhuo_manager/  -> 0 en bandeja (nivel 1)

**`_derivadas` y `_insertados` quedan FUERA de la poblacion por `D.38.4`, y esa columna la anade mi
lectura: el instrumento solo cuenta los ficheros.**

| cifra | **mi comando de hoy** |
|---|---:|
| nodos en `dataset/nodos.jsonl` | **243** |
| lineas en `bitacora/VEREDICTOS.jsonl` | **289** |
| de ellas, declaradas **NO CONSUMADAS** | **14** |
| pares mutuos | **1** (la cabecera; la sede sigue sin par adjudicado) |
| candidatos del lote 4 en bandeja | **102** |
| candidatos del lote 5 en bandeja | **3** |
| ficheros en `cuarentena/ensayo_referencia_163/` | **163** |
| **poblacion de mi barrido** | **348** |

### 2.1. POR QUE `348` Y NO `511`: LA POBLACION LA DECIDE EL INSTRUMENTO DE LA CASA, NO YO

    $ grep -n "def poblacion_de_bandejas" -A 26 src/aduana.py   (la linea que decide)
      463:            if candidato.get("id") and _fuentes_canonicas(candidato, tabla_fuentes):
      464:                esperando.append(candidato)

    $ grep -c "ensayo_referencia_163" fuentes/FUENTES_CANONICAS.json
      0

    $ una muestra de esa carpeta
      fichero: cuarentena/ensayo_referencia_163/accion_correctiva_2.json
        id = 'accion_correctiva_2'
        fuente = None
        libro = None

**LO QUE LA SALIDA MIDE:** `aduana.poblacion_de_bandejas` **exige fuente canonica** (linea `463`),
`ensayo_referencia_163` **no esta en la tabla canonica** (`grep -c` da `0`) y sus ficheros no traen
fuente. **Por eso los `163` no entran en los `348`: los descarta el instrumento de la casa, no mi
criterio.** `243 + 102 + 3 = 348`.

**Y ESTO ES LO QUE `D.38.5` HACE COMPARABLE:** mi poblacion es la que la aduana usa **porque es la
misma funcion**, no porque las dos den el mismo numero por casualidad.

---

## 3. EL MATERIAL DEL LOTE, MEDIDO ANTES DE CLASIFICAR NADA

    $ ls fuentes/scott_radical_candor/*.md | wc -l
      15
    $ wc -l fuentes/scott_radical_candor/cap_07.md fuentes/scott_radical_candor/cap_11.md
        433 fuentes/scott_radical_candor/cap_07.md
        333 fuentes/scott_radical_candor/cap_11.md
    $ wc -w fuentes/scott_radical_candor/cap_07.md
      13706
    $ sha256sum fuentes/scott_radical_candor/cap_07.md
      2048f3bae4f787582d4eb6542087de391a22c0306889ffd1d13cca15f8fe43ba
    $ sha256sum fuentes/scott_radical_candor/cap_11.md
      7b42d1a8e29e2dff05a218a9812afb9121b56998a819b46afdf25fedb34d06ab

### 3.1. EL REPARTO POR CAPITULO, CON MI PROPIO LECTOR

<!-- salida: .v29/mapa_capitulos.txt, lector .v29/mapa_capitulos.py -->

    $ python .v29/mapa_capitulos.py scott_radical_candor
      LIBRO: scott_radical_candor
      capitulo          GRAFO  BANDEJA
      (sin unidad)          1        0
      cap_01                1        0
      cap_03                1        0
      cap_04                5        0
      cap_05                8        0
      cap_06               10        0
      cap_07               13       12
      cap_08                0       12
      cap_09                0       20
      cap_10                0       14
      cap_11                1       15
      cap_12                0        2
      cap_13                0       12
      cap_14                0       15
      TOTAL                40      102

**LO QUE LA SALIDA MIDE:** del lote 4, `40` piezas viven en el grafo y `102` esperan. **`cap_07`
esta partido: `13` dentro y `12` fuera.** Y **`cap_11` tiene `1` dentro y `15` fuera**, que es la
unica pieza de ese capitulo que ha entrado.

### 3.2. `cap_07` ENTERO POR ORDEN DE LINEA DEL LIBRO

<!-- salida: .v29/cap07_estado.txt, lector .v29/cap07_estado.py -->

    $ python .v29/cap07_estado.py
      donde    lineas     id                                             pasos
      GRAFO    65-77      recorrer_rueda_hacer_cosas_equipo                 12
      GRAFO    91-111     escuchar_callado_equipo_tranquilizar_incomodo     11
      GRAFO    113-129    escuchar_ruidoso_opinion_fuerte_pedir_agujeros    13
      GRAFO    131-153    crear_cultura_escucha_equipo                      17
      GRAFO    155-163    adaptar_escucha_cultura_ajena                      9  (tramo no contiguo: 155-163 y 131-153)
      GRAFO    177-195    crear_espacio_seguro_madurar_ideas_nuevas         14
      GRAFO    197-211    explicar_idea_facil_comprender_oyente             13
      GRAFO    225-229    centrar_debate_ideas_fuera_egos                   10
      GRAFO    231-233    crear_obligacion_disentir_equipo                   5
      BANDEJA  235-237    parar_debate_emocion_agotamiento                   5
      GRAFO    239-243    abrir_debate_humor_explicar_proposito              7
      BANDEJA  245-257    fijar_fecha_cierre_debate_equipo                  11
      BANDEJA  259-289    repartir_decision_cercanos_hechos                 11
      BANDEJA  291-293    pedir_hechos_decision_evitar_recomendaciones       5
      GRAFO    295-301    bajar_detalle_organizacion_fuente_hechos           9
      BANDEJA  303-347    persuadir_emocion_oyente_no_propia                11  (tramo no contiguo: 303-347 y 309-313 y 333-339)
      BANDEJA  349-357    establecer_credibilidad_pericia_humildad           9
      BANDEJA  359-365    compartir_logica_mostrar_razonamiento              6
      BANDEJA  367-373    minimizar_impuesto_colaboracion_equipo             4
      BANDEJA  375-379    proteger_tiempo_equipo_jefe                        9
      BANDEJA  381-383    mantener_manos_trabajo_real_equipo                 8
      BANDEJA  385-387    reservar_calendario_tiempo_ejecutar                4
      GRAFO    389-401    aprender_resultados_vencer_dos_presiones           6
      GRAFO    403-407    cambiar_posicion_hechos_explicar_cambio            9
      BANDEJA  409-419    cuidarse_agotamiento_centro_rueda                  7

      GRAFO: 13   BANDEJA: 12   TOTAL cap_07: 25
      PASOS en el grafo: 135   PASOS en bandeja: 90

> **`LECTURA`: el capitulo no esta entrando en el orden del libro, y la columna `donde` lo dice
> sola.** `239-243` esta dentro y `235-237` fuera; `295-301` esta dentro y `245` a `293` fuera;
> `389-407` esta dentro y `303` a `387` fuera. **`EXTRACTOR.md` 12.3 pone el orden en el libro.**
>
> **NO SE LO CUENTO A LA VUELTA 28 SIN MEDIR CUALES SON SUYAS**, porque de las tres piezas de
> `cap_07` que entraron en esta vuelta (seccion `4`), **las de `177-195` y `65-77` rellenan huecos
> que dejaron vueltas anteriores**, y esa es la direccion contraria: **cierran desorden, no lo
> abren.** Quien dejo `235-237` detras de `239-243` no es esta vuelta. **`POR ADJUDICAR 4`.**

### 3.3. EL CENSO DE ROTULOS DEL CAPITULO, Y EL UNICO HALLAZGO QUE ME PARECE DE VERDAD

<!-- salida: .v29/rotulos_cap07.txt, lector .v29/rotulos_cap07.py -->

    $ python .v29/rotulos_cap07.py
      ROTULOS DETECTADOS: 49
      ...
      9      NADIE    -     Telling people what to do doesn't work
      11     NADIE    -     TELLING PEOPLE WHAT TO DO DIDN'T WORK AT GOOGLE
      45     NADIE    -     TELLING PEOPLE WHAT TO DO DIDN'T WORK FOR STEVE JOBS EITHER
      79     NADIE    -     LISTEN
      81     NADIE    -     "Give the quiet ones a voice."
      165    NADIE    -     CLARIFY
      213    NADIE    -     DEBATE
      215    NADIE    -     The rock tumbler
      421    NADIE    -     PART II
      423    NADIE    -     TOOLS & TECHNIQUES
      433    NADIE    -     RELATIONSHIPS

      ROTULOS SIN NODO QUE LOS RECLAME: 11 de 49

**LO QUE LA SALIDA MIDE:** de los `49` rotulos que mi lector detecta en `cap_07`, **`11` no los
reclama ningun nodo**, ni del grafo ni de la bandeja.

> **`LECTURA`, y es la pieza de esta apertura que mas me interesa: los siete pasos de la rueda no
> estan tratados igual.** El propio censo lo pone en columna:
>
> | paso de la rueda | su rotulo | **quien lo reclama** |
> |---|---|---|
> | `LISTEN` | `L79` | **NADIE** |
> | `CLARIFY` | `L165` | **NADIE** |
> | `DEBATE` | `L213` | **NADIE** |
> | `DECIDE` | `L259` | `repartir_decision_cercanos_hechos` |
> | `PERSUADE` | `L303` | `persuadir_emocion_oyente_no_propia` |
> | `EXECUTE` | `L367` | `minimizar_impuesto_colaboracion_equipo` |
> | `LEARN` | `L389` | `aprender_resultados_vencer_dos_presiones` |
>
> **Cuatro de los siete rotulos de paso los absorbe la primera pieza de su seccion; tres no.** Y no
> es que a `LISTEN`, `CLARIFY` y `DEBATE` les falte cuerpo: `L85` a `L89`, `L171` a `L175` y `L217`
> a `L223` tienen texto, **y ese texto es el que dice para que sirve el paso.**
>
> **NO DIGO QUE FALTEN TRES NODOS.** Digo que **el mismo material esta tratado de dos maneras dentro
> del mismo capitulo**, y que la asimetria la miden `11` rotulos huerfanos. `L221`-`L223` ya esta
> adjudicado (`ACTA 27` `2.2`: la cabeza de la lista de `DEBATE` **no es nodo**), **y esa
> adjudicacion es exactamente la que, aplicada a los otros seis, deberia haber dejado a `DECIDE`,
> `PERSUADE`, `EXECUTE` y `LEARN` tambien sin nodo.** **`POR ADJUDICAR 5`.**

### 3.4. LA COBERTURA DE LINEA, CON EL AVISO DE COMO CUENTA MI LECTOR

<!-- salida: .v29/cobertura_cap07.txt, lector .v29/cobertura_cap07.py -->

    $ python .v29/cobertura_cap07.py
      fichero            : fuentes/scott_radical_candor/cap_07.md
      lineas totales     : 434
      lineas NO vacias   : 220
      lineas reclamadas  : 160
      lineas HUERFANAS   : 60
      lineas reclamadas por MAS DE UN nodo: 35

**LO QUE LA SALIDA MIDE:** `220` lineas con texto, `160` reclamadas por algun nodo, `60` sin nadie.

**Y DIGO COMO CUENTA MI LECTOR, PORQUE SI NO LA CIFRA ENGANIA:** recoge **toda** expresion
`lineas A a B` del `resumen_teorico`, **y algunas de esas no son lo que el nodo reclama sino una
remision**. Las `35` solapadas son de esa especie y las he mirado una a una:

    $ python .v29/cobertura_cap07.py | grep -E "^ (131|153|309|313|333|339):"
       131: GRAFO adaptar_escucha_cultura_ajena | GRAFO crear_cultura_escucha_equipo
       153: GRAFO adaptar_escucha_cultura_ajena | GRAFO crear_cultura_escucha_equipo
       309: BANDEJA persuadir_emocion_oyente_no_propia | BANDEJA persuadir_emocion_oyente_no_propia
       313: BANDEJA persuadir_emocion_oyente_no_propia | BANDEJA persuadir_emocion_oyente_no_propia
       333: BANDEJA persuadir_emocion_oyente_no_propia | BANDEJA persuadir_emocion_oyente_no_propia
       339: BANDEJA persuadir_emocion_oyente_no_propia | BANDEJA persuadir_emocion_oyente_no_propia

**MI CUENTA SOBRE ESA SALIDA, y la firmo como mia y no como del instrumento:** el tramo `131`-`153`
son **`23`** lineas y el tramo `309`-`313` mas `333`-`339` son **`12`**. **`23 + 12 = 35`**, que es
el total que la cabecera del instrumento da.

**Las `23` primeras son una remision de `adaptar_escucha_cultura_ajena` al tramo del vecino, no un
reclamo; las `12` segundas son subtramos de `persuadir_emocion_oyente_no_propia` DENTRO de su propio
`303-347`.** **Ninguna de las `35` es un solape de verdad entre dos nodos distintos.**

> **`LECTURA`: de las `60` huerfanas, `7` son la cabecera YAML (`L1`-`L7`), `7` son la portadilla de
> `PART II` que el recorte dejo pegada al final (`L421`-`L433`) y el resto se reparte entre la
> narracion de apertura del capitulo (`L9`-`L63`), los epigrafes y las tres entradillas de paso de
> `3.3`.** **Ni una de las `60` me parece un procedimiento perdido**, y la que mas cerca esta es la
> entradilla de `DEBATE`, **que ya esta adjudicada como no-nodo.**
>
> **Y UNA QUE NO ES DE CONTENIDO PERO SI ES UN HALLAZGO:** la cabecera del fichero dice
> `unidad: Cap. 4` y `titulo_textual: Drive Results Collaboratively`, **y el fichero se llama
> `cap_07.md`.** Mas `L421`-`L433`, que es material de **la parte siguiente del libro** dentro del
> fichero del capitulo. **Las dos cosas son del recorte, no de la extraccion. `POR ADJUDICAR 6`.**

---

## 4. MI CLASIFICACION DE LAS CUATRO PIEZAS QUE ENTRARON, LEIDA CONTRA EL LIBRO

    $ grep -E "^(ID|PASOS|PREVIOS) " .v29/cuatro_nuevos.txt
      ID       : recorrer_rueda_conscientemente_cultura_equipo
      PASOS    : 14
      PREVIOS  : []
      ID       : recorrer_rueda_hacer_cosas_equipo
      PASOS    : 12
      PREVIOS  : ['recorrer_rueda_conscientemente_cultura_equipo']
      ID       : crear_espacio_seguro_madurar_ideas_nuevas
      PASOS    : 14
      PREVIOS  : []
      ID       : crear_obligacion_disentir_equipo
      PASOS    : 5
      PREVIOS  : []

| pieza | capitulo y tramo | pasos | **mi clase** |
|---|---|---:|---|
| `recorrer_rueda_conscientemente_cultura_equipo` | `cap_11` `271-299` y `307-333` | **14** | **PROCEDIMIENTO. Cabeza, y MADRE de la siguiente** |
| `recorrer_rueda_hacer_cosas_equipo` | `cap_07` `65-77` | **12** | **PROCEDIMIENTO. HIJA de la anterior** |
| `crear_espacio_seguro_madurar_ideas_nuevas` | `cap_07` `177-195` | **14** | **PROCEDIMIENTO. Pieza propia** |
| `crear_obligacion_disentir_equipo` | `cap_07` `231-233` | **5** | **PROCEDIMIENTO. Pieza propia, la mas corta** |

**`3` de las `4` son de `cap_07` y `1` es de `cap_11`.** La de `cap_11` **entra fuera del tramo del
capitulo, y entra porque yo lo autorice por escrito** en el encargo de la vuelta 28 (`TAREA 4`: *la
cabeza de la rueda y su madre entran antes que el resto*). **No es una desviacion suya: es mi
excepcion.**

### 4.1. `PASOS INVENTADOS`: LEI LOS `45` CONTRA SU PARRAFO, NO UNA MUESTRA

<!-- salida: .v29/pasos_rueda.txt .v29/pasos_espacio.txt .v29/pasos_disentir.txt .v29/pasos_cabeza.txt -->

**`D.30`: el numerador lo pone quien lee, porque ninguna maquina tiene el libro delante.** El
denominador lo cuenta el dataset:

    $ los cuatro nodos, pasos_accionables contados del dataset
      12 + 14 + 5 + 14 = 45

**`recorrer_rueda_hacer_cosas_equipo`, `12` pasos contra `cap_07` `L65`-`L77`:**

    $ awk 'NR>=63 && NR<=79' fuentes/scott_radical_candor/cap_07.md
      71: The process, which I call the "Get Stuff Done" (GSD) wheel ... is to avoid the impulse
          to dive right in, as I did in the example that begins this chapter. Instead, you have
          to first lay the groundwork for collaboration.
      73: ... First, you have to listen to the ideas that people on your team have and create a
          culture in which they listen to each other. Next, you have to create space in which
          ideas can be sharpened and clarified, to make sure these ideas don't get crushed
          before everyone fully understands their potential usefulness. But just because an idea
          is easy to understand doesn't mean it's a good one. Next, you have to debate ideas and
          test them more rigorously. Then you need to decide, quickly, but not too quickly. ...
          You have to persuade those who weren't involved in a decision that it was a good one,
          so that everyone can execute it effectively. Then, having executed, you have to learn
          from the results, whether or not you did the right thing, and start the whole process
          over again.
      75: That's a lot of steps. Remember, they are designed to be cycled through quickly. Not
          skipping a step and not getting stuck on one are equally important. If you skip a
          step, you'll waste time in the end. If you allow any part of the process to drag out,
          working on your team will feel like paying a collaboration tax, not making a
          collaboration investment.
      77: You may very well be in a situation where your boss is skipping steps and just telling
          you what to do. ... You can put these ideas into practice with the people who report
          to you even if your boss doesn't subscribe to this method ...

| paso | su linea | |
|---:|---|---|
| `1` | `L71`, *avoid the impulse to dive right in* mas *first lay the groundwork* | TRANSCRIPCION |
| `2` a `8` | `L73`, los siete pasos de la rueda **en el mismo orden y con las mismas clausulas** | TRANSCRIPCION |
| `9` | `L75`, *that's a lot of steps ... designed to be cycled through quickly* | TRANSCRIPCION |
| `10` | `L75`, *if you skip a step, you'll waste time in the end* | TRANSCRIPCION |
| `11` | `L75`, *not getting stuck* mas *collaboration tax, not ... investment* | TRANSCRIPCION |
| `12` | `L77`, *even if your boss doesn't subscribe to this method* | TRANSCRIPCION |

**`12` de `12` TRANSCRIPCION. `0` PUENTE.** Y `L67` y `L69` (el genio de Steve, Google contra
Apple) **no produjeron paso**, que es lo correcto: son narracion.

**`crear_espacio_seguro_madurar_ideas_nuevas`, `14` pasos contra `cap_07` `L177`-`L195`:**

    $ sed -n '185p;187p;195p' fuentes/scott_radical_candor/cap_07.md
      185: Part of your job as the boss is to help people think through their ideas before
           submitting them to the rough-and-tumble of debate. Russ Laraway explained that I was
           doing this all wrong when I told my team at Google not to bring me problems; instead,
           I told them, bring me three solutions and a recommendation. "But then you're not
           helping people innovate," Russ explained. ... "When do they get to just talk,
           brainstorm with you?" ...
      187: Susan Wojcicki ... Debate in those meetings could be brutal, and they started to feel
           like the place where new ideas went to die. Susan ... created a pre-EMG meeting where
           new ideas could be developed. ...
      195: ... your weekly 1:1s ... These meetings should be a safe place for your direct reports
           to come and talk to you about new ideas. In this context, you shouldn't judge the
           ideas but rather help your direct reports clarify their thinking. This is a form of
           "plussing." You can point out problems but with the aim of figuring a way around
           those problems, not killing ideas.

    $ sed -n '193p' fuentes/scott_radical_candor/cap_07.md
      193: Brainstorming sessions ... These sessions are not just random conversations where
           nobody is allowed to say anything negative, though. There are plenty of bad ideas,
           and they need to be recognized as such. Poking holes in new ideas doesn't necessarily
           kill them, it can push people to clarify their thinking. There are also great ideas
           that look bad at first blush. ... Pixar has a technique called "plussing." Rather
           than saying, "No, that is a bad idea," people must offer a solution to the problem
           they are pointing out.

| paso | su linea | |
|---:|---|---|
| `1`, `2`, `3` | `L185`: el trabajo del jefe, las *tres soluciones y una recomendacion* de Russ Laraway, y *when do they get to just talk* | TRANSCRIPCION |
| `4`, `5` | `L177`: *I don't have time* mas *will save you time in the long run* mas *help ... explain what they mean* | TRANSCRIPCION |
| `6` | `L179`: *push ... to clarify their thinking* mas *squish their best thinking* | TRANSCRIPCION |
| `7` | `L187`: Susan Wojcicki, *the place where new ideas went to die*, la reunion previa | TRANSCRIPCION |
| `8`, `9`, `10`, `11` | `L193`: la lluvia de ideas, los agujeros, *great ideas that look bad at first blush*, **`plussing` de Pixar con sus palabras** | TRANSCRIPCION |
| `12`, `13`, `14` | `L195`: las reuniones a solas, *you shouldn't judge*, *not killing ideas* | TRANSCRIPCION |

**`14` de `14` TRANSCRIPCION. `0` PUENTE.**

> **UNA CAIDA DE METODO MIA, DECLARADA DONDE OCURRIO Y NO ESCONDIDA:** al buscar `plussing` mi
> primer comando fue `grep -n "plussing\|Pixar" ... | cut -c1-200`, **y salio vacio de `plussing`
> porque la palabra vive pasado el caracter `200` de `L193`**. Estuve a un paso de publicar un
> `PUENTE` que no existe. **Lo cace volviendo a correr el comando sin `cut`**, y lo dejo escrito
> porque `AUDITOR_FORJA.md` 1.1 dice que **una busqueda negativa no se puede citar**: el motivo de
> esa regla es exactamente este, y hoy me ha tocado a mi.

**`crear_obligacion_disentir_equipo`, `5` pasos contra `cap_07` `L231`-`L233`:**

    $ sed -n '231p;233p' fuentes/scott_radical_candor/cap_07.md
      231: Create an obligation to dissent
      233: I once interned at McKinsey ... McKinsey had very consciously created an "obligation
           to dissent." If everyone around the table agreed, that was a red flag. Somebody had
           to take up the dissenting voice. ... One ex-McKinsey executive at Apple ... had a
           bunch of gavels made up with "duty to dissent" written in Japanese on them. If there
           wasn't a robust enough argument in a meeting, he'd slide the gavel across the table
           to someone, as a sign to take up the opposite point of view. This simple prop was
           surprisingly effective.

**Los `5` pasos son las `5` clausulas de `L233` en su orden**: la obligacion de McKinsey, la bandera
roja del acuerdo unanime, la voz discrepante, los mazos con el deber de disentir en japones, y el
objeto que se desliza. **`5` de `5` TRANSCRIPCION. `0` PUENTE.**

**`recorrer_rueda_conscientemente_cultura_equipo`, `14` pasos contra `cap_11` `L271`-`L299` y
`L307`-`L333`:**

    $ sed -n '275p;281p;285p;293p;297p' fuentes/scott_radical_candor/cap_11.md
      275: "CULTURE EATS STRATEGY for lunch." A team's culture has an enormous impact on its
           results, and a leader's personality has a huge impact on a team's culture. Who you
           are as a human being impacts your team's culture enormously.
      281: Fortunately, as with all things, it's not just about you. As with your evaluations of
           others, focus on behavior rather than on character, on actions rather than
           "essentials." If you are regularly and genuinely soliciting feedback, the most
           egregious of these qualities will inevitably come to light. ... You will influence
           other aspects of your culture as well, simply by moving consciously through the steps
           of the GSD wheel.
      285: When you become the boss, you are under the microscope. People do listen to you in an
           intense way ... They attribute meaning, sometimes accurately, sometimes not, to what
           you say, to the clothes you wear, to the car you drive. ...
      293: Often when you're the boss you might say or do something you expect to be blown off,
           whereas in fact you've moved way further out on the "challenge directly" axis than
           you had intended to.
      297: Given the level of scrutiny you're under as the boss, it's important to clarify what
           you're saying, even when you think you're not saying anything.

    $ sed -n '311p;313p;317p;323p;329p' fuentes/scott_radical_candor/cap_11.md
      311: When you pay attention to seemingly small details, it can have a big impact on
           persuading people that your culture is worth understanding and adapting to. The
           office environment is part of setting a tone and culture. ... But even if you can't
           afford this kind of largesse, you can make sure the coffee in the kitchen is what
           people like to drink, and offer some green tea bags, too.
      313: The office environment affects culture. Do you want a Zen-like orderly, well-lit
           environment or a stuff-everywhere frenetic environment? The small choices you make
           will persuade people to act in accordance with the culture you want to build ...
      317: It's surprising how a small action from you can impact your team's culture, even
           after you're no longer around.
      323: Shit happens. When you're the boss and shit happens, it's your responsibility to
           learn from it and make a change. If you don't, you create a culture that doesn't
           learn from its mistakes.
      329: The most amazing thing about a culture is that once it's strong, it's self-
           replicating. ... you'll know you've succeeded when it truly is no longer about you.

| paso | su linea | |
|---:|---|---|
| `1` | `L275` entera, **clausula por clausula** | TRANSCRIPCION |
| `2`, `3`, `4` | `L281`: *not just about you*, *focus on behavior rather than character*, *soliciting feedback*, **y su clausula de cierre** | TRANSCRIPCION |
| `5`, `6`, `7` | `L285`, `L293`, `L297` | TRANSCRIPCION |
| `8` | `L299`, la manera de aparcar contra la cultura que empujaba | TRANSCRIPCION |
| `9`, `10`, `11` | `L311` (incluido *green tea bags*) y `L313` | TRANSCRIPCION |
| `12`, `13`, `14` | `L317`, `L323`, `L329` | TRANSCRIPCION |

**`14` de `14` TRANSCRIPCION. `0` PUENTE.**

### 4.2. MI FILA DE `PASOS INVENTADOS`, POR CAPITULO Y NO POR VUELTA (`AUDITOR_FORJA.md` 8.2)

| capitulo | nodos que entraron | **pasos escritos** | **PUENTE que yo leo** | **PASOS INVENTADOS** |
|---|---:|---:|---:|---:|
| **`cap_07`** | 3 | **31** | **0** | **0,00 por ciento** |
| **`cap_11`** | 1 | **14** | **0** | **0,00 por ciento** |
| **total de la vuelta** | 4 | **45** | **0** | **0,00 por ciento** |

**El denominador sale del dataset** (`12 + 14 + 5` y `14`). **El numerador sale de haber leido los
`45` contra su parrafo, uno a uno y no una muestra.**

> **`LECTURA`: el `0,00` no dice que estos capitulos sean faciles. Dice que estos cuatro nodos se
> minaron pegados al texto**, hasta el punto de que en tres de los cuatro **el orden de los pasos es
> el orden de las clausulas del parrafo**. El riesgo que `8.3` avisa es el contrario, marcar un
> puente como transcripcion para bajar la cifra y agrandar el lote; **contra eso lo unico que vale es
> haber leido los cuarenta y cinco, que es lo que hice.**

### 4.3. **LA ARISTA DE LA RUEDA, ADJUDICADA CON EL LIBRO Y ANTES DE ABRIR LA BITACORA**

*Esto es lo que mi remedio `2` de la `ACTA 27` seccion `10` me manda hacer en este orden, y esta vez
puedo probar el orden con las fechas de mis propios ficheros.*

    $ ls --time-style=full-iso .v29/    (el orden de mis instrumentos, recortado)
      2026-09-16 10:03:40  .v29/pasos_rueda.txt         (los pasos del hijo)
      2026-09-16 10:03:46  .v29/libro_65_77.txt         (su tramo del libro)
      2026-09-16 10:05:36  .v29/pasos_disentir.txt
      2026-09-16 10:05:43  .v29/pasos_cabeza.txt        (los pasos de la madre)
      2026-09-16 10:19:21  .v29/barrido_v29.txt         (mi barrido de vecinos)
      2026-09-16 10:20:09  .v29/bitacora_v29.txt        (LA BITACORA, la ultima)

**Los pasos de los dos lados y sus tramos del libro estan impresos a las `10:03` y `10:05`. La
bitacora no la abri hasta las `10:20`.** El orden que `1.2` manda esta cumplido **y es
comprobable**, no declarado.

**MI CLASE, escrita desde el libro: `CONTINUA`, con `recorrer_rueda_conscientemente_cultura_equipo`
MADRE y `recorrer_rueda_hacer_cosas_equipo` HIJO, y el paso que la sostiene es el `4` de la madre.**

| la vara de `6.1` | lo que mide este par |
|---|---|
| **direccion** | **`L281` de `cap_11` cierra asi: *You will influence other aspects of your culture as well, simply by moving consciously through the steps of the GSD wheel.*** La madre **NOMBRA** la rueda en una clausula. El hijo la **PROCEDIMENTA** en `12` pasos sacados de `L71`-`L77` de `cap_07` |
| **NOMBRAR NO ES PROCEDIMENTAR** (`P.5.1`) | es literalmente este caso: **una clausula contra doce pasos**. Ninguno de los `14` pasos de la madre dice como se recorre la rueda; ninguno de los `12` del hijo habla de cultura |
| **sin bascula: que queda fuera** | **procedimiento en los dos lados.** Lo de la madre es la cultura bajo el microscopio (conducta y no caracter, lo que comunicas sin hablar, el entorno, aprender de lo que pasa); lo del hijo es la rueda (no saltarse un paso, no atascarse, el impuesto de colaboracion) |
| **el entregable** | el de la madre es *los pasos de la rueda recorridos a sabiendas sobre tu propia cultura*; el del hijo es *una vuelta entera de la rueda dada deprisa* |

**Y EL DATO DICE LO MISMO QUE MI LECTURA:**

    $ grep -E "^(ID|PREVIOS|SIGUIENTS) " .v29/cuatro_nuevos.txt | head -6
      ID       : recorrer_rueda_conscientemente_cultura_equipo
      PREVIOS  : []
      SIGUIENTS: ['recorrer_rueda_hacer_cosas_equipo']
      ID       : recorrer_rueda_hacer_cosas_equipo
      PREVIOS  : ['recorrer_rueda_conscientemente_cultura_equipo']
      SIGUIENTS: []

**La arista esta cableada por los dos extremos, en la direccion que mi lectura da, y la cola que
llevaba dos vueltas abierta se cierra.** Es la primera arista **entre dos capitulos distintos del
mismo libro** de esta casa.

> **Y DIGO LO QUE ESTO SIGNIFICA PARA MI PROPIA RACHA, porque es lo contrario de la vuelta pasada:**
> en la `ACTA 27` mi apertura publico una arista **que la adjudicacion me retiro**, y me costo una
> `CIFRA PUBLICADA PROPIA`. **Hoy la arista que publico es una que el dato ya tiene cableada y que
> mi lectura confirma por su paso**, no una que yo levante y nadie mas vea.

### 4.4. **EL HUECO DE LA MADRE, QUE ES LO UNICO QUE ME CHIRRIA DE LAS CUATRO PIEZAS**

    $ python .v29/mapa_capitulos.py scott_radical_candor | grep cap_11
      cap_11                1       15

    (y el tramo de la madre, leido literal de su propio `resumen_teorico` en el dataset)
      UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_11.md, unidad Cap. 8, Results. Sale de
      las lineas 271 a 299 y de las lineas 307 a 333, bajo el rotulo BE CONSCIOUS OF CULTURE y
      sus rotulos interiores. ES LA PIEZA P15 DE LA FRONTERA DE cap_11, Y SU TRAMO ES NO
      CONTIGUO: entre sus dos mitades viven las lineas 301 a 305, que son el rotulo Debate and
      decide explicitly y salen en su propio nodo, debatir_decidir_asuntos_cultura_evitar_delegar.
      Lo digo aqui para que la frontera se pueda comprobar.

    $ sed -n '301p;303p;305p' fuentes/scott_radical_candor/cap_11.md
      301: Debate and decide explicitly. Don't let things that pervert your culture "just happen"
      303: There are a number of debates and decisions that you are going to be tempted to
           "delegate to HR." ...
      305: Believe me, it's tempting to punt on these decisions. But if you do, the decisions
           that do get made by HR/employment lawyers without your humanizing influence will
           push your culture in a "the law is an ass" direction. ...

**LO QUE LA SALIDA MIDE:** el tramo de la madre **salta las lineas `301` a `305` a proposito** (su
propio `resumen_teorico` lo declara y nombra al nodo que las recoge), **y sus `14` pasos van de
`Clarify` (`7`, `8`) a `Persuade` (`9`, `10`, `11`) sin pasar por `Debate` ni por `Decide`.**

> **`LECTURA`: un nodo cuyo entregable es *los pasos de la rueda recorridos a sabiendas* y que
> **omite dos de los siete pasos** porque esos dos se fueron a un hermano **puede ser correcto y
> puede ser una frontera mal puesta**, y los dos casos se parecen desde fuera. **No lo decido en la
> fase ciega.** **`POR ADJUDICAR 7`.**

---

## 5. MI BARRIDO DE VECINOS CONTRA EL DE LA ADUANA (`D.38.5`)

<!-- salida: .v29/barrido_v29.txt, lector .v29/barrido_v29.py -->

    $ python .v29/barrido_v29.py <los cuatro que entraron>
      poblacion del barrido : 348   (243 del grafo mas 105 que esperan en bandejas)

      CANDIDATO : recorrer_rueda_conscientemente_cultura_equipo   (14 pasos)
      VECINOS QUE SUPERAN UMBRAL : 1   sobre una poblacion de 347
         - recorrer_rueda_hacer_cosas_equipo                    GRAFO    [familia_id=0.429]

      CANDIDATO : recorrer_rueda_hacer_cosas_equipo   (12 pasos)
      VECINOS QUE SUPERAN UMBRAL : 3   sobre una poblacion de 347
         - recorrer_trece_elementos_proceso_evaluacion_formal   BANDEJA  [paso_contra_nodo=0.61]
         - recorrer_rueda_conscientemente_cultura_equipo        GRAFO    [familia_id=0.429]
         - reconocer_emociones_propias_avisar_equipo            BANDEJA  [similitud_texto=0.353]

      CANDIDATO : crear_espacio_seguro_madurar_ideas_nuevas   (14 pasos)
      VECINOS QUE SUPERAN UMBRAL : 1   sobre una poblacion de 347
         - nutrir_ideas_nuevas_reunion_solas                    BANDEJA  [paso_contra_nodo=0.617]

      CANDIDATO : crear_obligacion_disentir_equipo   (5 pasos)
      VECINOS QUE SUPERAN UMBRAL : 10   sobre una poblacion de 347
         - parar_debate_emocion_agotamiento                     BANDEJA  [similitud_texto=0.411]
         - pedir_hechos_decision_evitar_recomendaciones         BANDEJA  [similitud_texto=0.474]
         - crear_cultura_escucha_equipo                         GRAFO    [familia_id=0.333]
         - proteger_tiempo_equipo_jefe                          BANDEJA  [similitud_texto=0.357]
         - compartir_logica_mostrar_razonamiento                BANDEJA  [similitud_texto=0.368]
         - reservar_calendario_tiempo_ejecutar                  BANDEJA  [similitud_texto=0.393]
         - cambiar_posicion_hechos_explicar_cambio              GRAFO    [similitud_texto=0.399]
         - aprender_resultados_vencer_dos_presiones             GRAFO    [similitud_texto=0.402]
         - evitar_presion_social_actos_equipo                   BANDEJA  [similitud_texto=0.393]
         - crear_plan_creible_equipo                            GRAFO    [familia_id=0.333]

**`1 + 3 + 1 + 10 = 15` pares levanta mi barrido.**

    $ python .v29/bitacora_v29.py | grep -E "^(265|266|267|268|279|28[0-9]) "
      265   CONTINUA  None       recorrer_rueda_conscientemente_cultura_equipo recorrer_rueda_hacer_cosas_equipo
      266   SANO      None       recorrer_rueda_hacer_cosas_equipo            recorrer_trece_elementos_proceso_evaluacion_formal
      267   CONTINUA  None       recorrer_rueda_hacer_cosas_equipo            recorrer_rueda_conscientemente_cultura_equipo
      268   SANO      None       recorrer_rueda_hacer_cosas_equipo            reconocer_emociones_propias_avisar_equipo
      279   CONTINUA  None       crear_espacio_seguro_madurar_ideas_nuevas    nutrir_ideas_nuevas_reunion_solas
      280   SANO      None       crear_obligacion_disentir_equipo             parar_debate_emocion_agotamiento
      281   SANO      None       crear_obligacion_disentir_equipo             pedir_hechos_decision_evitar_recomendaciones
      282   SANO      None       crear_obligacion_disentir_equipo             crear_cultura_escucha_equipo
      283   SANO      None       crear_obligacion_disentir_equipo             proteger_tiempo_equipo_jefe
      284   SANO      None       crear_obligacion_disentir_equipo             compartir_logica_mostrar_razonamiento
      285   SANO      None       crear_obligacion_disentir_equipo             reservar_calendario_tiempo_ejecutar
      286   SANO      None       crear_obligacion_disentir_equipo             cambiar_posicion_hechos_explicar_cambio
      287   SANO      None       crear_obligacion_disentir_equipo             aprender_resultados_vencer_dos_presiones
      288   SANO      None       crear_obligacion_disentir_equipo             evitar_presion_social_actos_equipo
      289   SANO      None       crear_obligacion_disentir_equipo             crear_plan_creible_equipo

**La columna del medio es `consumada`, y en estas quince dice `None`: el campo no esta escrito.
Las que si lo llevan, con `False`, son las de la seccion `6`.**

| | |
|---|---:|
| pares que levanta **mi** barrido sobre `348` | **15** |
| pares **consumados** que la aduana escribio | **15** |
| **coinciden por nombre de par, uno a uno** | **los quince** |

**Es la segunda vuelta seguida en que las dos poblaciones son la misma y las dos medidas cuadran al
digito.** En la `ACTA 14` fueron `135` contra `203`.

### 5.1. LO QUE NO PUEDO LLAMAR CIEGO, Y LO DIGO YO

**El mismo comando que cuenta las lineas me ensenio su columna `veredicto`.** No he abierto ni una
sola `razon` de las lineas `265` a `289`, **pero he visto las clases**, asi que:

> **NINGUNA de las `15` clases de esta seccion la publico como relectura ciega mia.** La unica
> adjudicacion de clase que reclamo como ciega es la de `4.3`, **y la reclamo porque puedo ensenar la
> hora de los ficheros** (`10:03`, `10:05` contra `10:20`). Las otras catorce las releo en el turno
> normal, con su razon destapada de una en una, **que es lo que mi remedio `2` manda.**

---

## 6. LAS LINEAS QUE LA VUELTA ESCRIBIO DOS VECES

    $ python .v29/bitacora_v29.py
      lineas totales            : 289
        consumada=False  -> 14
        consumada=None   -> 275
      nuevas (de la 265 en adelante): 25
        de ellas consumadas: 0   no consumadas: 10
      veredictos de las nuevas: {'CONTINUA': 3, 'SANO': 22}

      --- LAS DECLARADAS NO CONSUMADAS, con su numero de linea --- (el tramo de esta vuelta)
        linea 269  SANO                         crear_obligacion_disentir_equipo               parar_debate_emocion_agotamiento
        linea 270  SANO                         crear_obligacion_disentir_equipo               pedir_hechos_decision_evitar_recomendaciones
        linea 271  SANO                         crear_obligacion_disentir_equipo               crear_cultura_escucha_equipo
        linea 272  SANO                         crear_obligacion_disentir_equipo               proteger_tiempo_equipo_jefe
        linea 273  SANO                         crear_obligacion_disentir_equipo               compartir_logica_mostrar_razonamiento
        linea 274  SANO                         crear_obligacion_disentir_equipo               reservar_calendario_tiempo_ejecutar
        linea 275  SANO                         crear_obligacion_disentir_equipo               cambiar_posicion_hechos_explicar_cambio
        linea 276  SANO                         crear_obligacion_disentir_equipo               aprender_resultados_vencer_dos_presiones
        linea 277  SANO                         crear_obligacion_disentir_equipo               evitar_presion_social_actos_equipo
        linea 278  SANO                         crear_obligacion_disentir_equipo               crear_plan_creible_equipo

| lo que la salida mide | cifra |
|---|---:|
| lineas nuevas de la vuelta (`265` a `289`) | **25** |
| de ellas, **declaradas NO CONSUMADAS** | **10** |
| de ellas, consumadas | **15** |
| **lineas `269`-`278` contra lineas `280`-`289`** | **los mismos `10` pares, en el mismo orden** |
| lineas NO CONSUMADAS en toda la bitacora | **14** (`4` de la vuelta 27 mas `10` de esta) |

**LO QUE LA SALIDA MIDE, y es aritmetica, no interpretacion:** los `10` pares de
`crear_obligacion_disentir_equipo` **estan escritos dos veces**, una tanda marcada `consumada:
false` (`269`-`278`) y una tanda buena (`280`-`289`), **con la linea `279` de otro candidato metida
entre las dos.** Esa linea `279` fecha el orden: **primero se escribieron las diez que no se
consumaron, despues entro `crear_espacio_seguro`, y despues entraron las diez buenas.**

> **`LECTURA`, y es la que mas me importa de toda la apertura.** `HEREDADO 1` pedia que **una
> insercion rechazada no escribiese nada**. La seccion `0.2` mide que **el codigo hoy lo cumple por
> construccion**. Y esta seccion mide que **en esta misma vuelta la bitacora se ensucio diez veces
> mas con la forma exacta del fallo que el remedio venia a cerrar.**
>
> **LAS DOS COSAS PUEDEN SER CIERTAS A LA VEZ**, y de cual sea depende algo serio:
>
> - **si las `269`-`278` se escribieron ANTES de que el arreglo entrase**, el remedio esta cumplido
>   y esas diez son escombro heredado, tratado por su via (`2.c`) y bien tratado;
> - **si se escribieron DESPUES**, el remedio se rompio el mismo dia que se escribio.
>
> **NO TENGO LA CRONOLOGIA EN ESTA FASE y no la voy a adivinar.** Lo que si tengo medido es que la
> vuelta **las declaro por su nombre y por operacion**, y que el mensaje de su propio commit dice
> *se declara una caida de dato mia*. **`POR ADJUDICAR 8`, y es el primero que pienso mirar.**

### 6.1. Y UNA COSA DEL CAMPO `consumada` QUE MIDO Y QUE NO ES DEL EXTRACTOR

    $ python .v29/bitacora_v29.py
        consumada=False  -> 14
        consumada=None   -> 275

**LO QUE LA SALIDA MIDE: ninguna linea de la bitacora dice `consumada: true`.** El campo solo se
escribe para negar.

> **`LECTURA`: un campo que solo sabe decir `false` no distingue *se consumo* de *nadie lo ha
> mirado*.** Hoy da igual, porque la atomicidad de `0.2` hace que **existir ya signifique
> consumada**. Pero la marca de `2.c` se puso justamente porque una linea escrita puede no valer, **y
> el dia que haya una tercera situacion esta sede no la va a poder expresar.** **`POR ADJUDICAR 9`.**

### 6.2. LA VIGENCIA CAMBIO DE ESPECIE, Y LAS `8` NUEVAS NO SON LO QUE ERAN

    $ python forja.py rancios   (la cabecera y las ocho de la especie nueva)
      BLOQUE DE VIGENCIA: 34 hallazgo(s) sobre 275 veredicto(s) y 0 cita(s).
        RANCIO 26, SIN HUELLA 8
      [SIN HUELLA] veredicto crear_cultura_escucha_equipo contra crear_obligacion_disentir_equipo
        (linea 252, 2026-09-16): la huella que guarda de su vecino
        'crear_obligacion_disentir_equipo' es la de un nodo VACIO, asi que NO SE PUEDE COMPROBAR
        contra que texto se emitio
      ... y siete mas de la misma forma, lineas 256, 258, 260, 261, 262, 263, 264

| especie | **la ACTA 27 midio** | **mi comando de hoy** |
|---|---:|---:|
| hallazgos totales | `42` | **34** |
| veredictos medidos | `264` | **275** |
| `RANCIO` | `26` | **26** |
| `NODO IDO` | `16` | **la especie ya no existe** |
| `SIN HUELLA` | no existia | **8** |

**LO QUE LA SALIDA MIDE:** `NODO IDO` desaparecio como especie y aparecio `SIN HUELLA` con `8`, y la
vigencia ahora **descuenta las no consumadas**. Eso es la `TAREA 3.c` que yo encargue.

> **`LECTURA`: `SIN HUELLA` no dice lo mismo que `NODO IDO`, y el cambio me parece una mejora, pero
> las ocho lineas dicen ahora una cosa nueva que antes no decian: que la huella guardada del vecino
> es la de un nodo VACIO.** Un vecino de bandeja tiene texto (`cuarentena/` lo guarda), **asi que una
> huella de vacio no es *no puedo comprobarlo*: es *guarde mal la huella cuando emiti el
> veredicto*.** Si eso es cierto, **los ocho veredictos se emitieron sin dejar constancia
> comprobable de contra que texto**, y eso es mas grave que un rancio. **`POR ADJUDICAR 10`.**

---

## 7. LOS `12` DE `cap_07` QUE SIGUEN ESPERANDO, CLASIFICADOS POR MI

<!-- salida: .v29/fichas_bandeja.txt, lector .v29/fichas_bandeja.py -->

**Estos si los classifico a ciegas de verdad, porque ninguno tiene veredicto escrito todavia.**

| # | candidato | tramo | pasos | **mi clase** | lo que la sostiene |
|---:|---|---|---:|---|---|
| 1 | `parar_debate_emocion_agotamiento` | `235-237` | 5 | **PROCEDIMIENTO**, pieza propia | rotulo propio `Pause for emotion/exhaustion`; acto (aplazar) con condicion y entregable |
| 2 | `fijar_fecha_cierre_debate_equipo` | `245-257` | 11 | **PROCEDIMIENTO. FUSION declarada `P.19`** de dos rotulos | `L245` y `L251` son dos rotulos y **el remedio de `L257` es el mismo objeto del primero**: la fecha de decidir |
| 3 | `repartir_decision_cercanos_hechos` | `259-289` | 11 | **PROCEDIMIENTO. Absorbe el rotulo de paso `DECIDE`** | `L259` `DECIDE`, `L261` y `L265` cuelgan de el |
| 4 | `pedir_hechos_decision_evitar_recomendaciones` | `291-293` | 5 | **PROCEDIMIENTO**, pieza corta con rotulo propio | `L291` `The decider should get facts, not recommendations` |
| 5 | `persuadir_emocion_oyente_no_propia` | `303-347` | 11 | **PROCEDIMIENTO. Absorbe el rotulo de paso `PERSUADE`** | `L303`, `L305`, `L323`, `L325`, `L337`: cinco rotulos en un nodo |
| 6 | `establecer_credibilidad_pericia_humildad` | `349-357` mas `313` | 9 | **PROCEDIMIENTO**, con cabecera ya corregida en la vuelta 18 | `L349` `Credibility`, `L351` `Demonstrate expertise and humility` |
| 7 | `compartir_logica_mostrar_razonamiento` | `359-365` | 6 | **PROCEDIMIENTO**, la tercera de la triada retorica | `L359` `Logic`, `L361` `Show your work` |
| 8 | `minimizar_impuesto_colaboracion_equipo` | `367-373` | 4 | **PROCEDIMIENTO. CABEZA DE SERIE `D.37` con TRES partes nombradas** | `L373`, medido abajo |
| 9 | `proteger_tiempo_equipo_jefe` | `375-379` | 9 | **PROCEDIMIENTO. Parte `1` de `3` de la serie del `8`** | `L375` |
| 10 | `mantener_manos_trabajo_real_equipo` | `381-383` | 8 | **PROCEDIMIENTO. Parte `2` de `3`** | `L381` |
| 11 | `reservar_calendario_tiempo_ejecutar` | `385-387` | 4 | **PROCEDIMIENTO. Parte `3` de `3`** | `L385` |
| 12 | `cuidarse_agotamiento_centro_rueda` | `409-419` | 7 | **PROCEDIMIENTO. Mitad `2` de `2` de la serie `D.37` de `aprender_resultados_...`** | `L401` y `L409`, medido abajo |

**Los `12` me salen PROCEDIMIENTO y ninguno POSTURA.** `D.27` pide inventario de medios, y los doce
lo traen: acto, condicion de activacion y entregable.

### 7.1. LAS DOS SERIES `D.37`, COMPROBADAS EN EL LIBRO Y NO EN SU PALABRA

*`D.37` en su forma fuerte pide que el texto diga CUANTAS partes hay y las NOMBRE. Lo compruebo.*

    $ sed -n '373p' fuentes/scott_radical_candor/cap_07.md
      Here are the three things I've learned about getting this balance right: Don't waste your
      team's time; Keep the "dirt under your fingernails"; and Block time to execute.

    $ sed -n '375p;381p;385p' fuentes/scott_radical_candor/cap_07.md
      Don't waste your team's time
      Keep the "dirt under your fingernails"
      Block time to execute

    $ sed -n '401p' fuentes/scott_radical_candor/cap_07.md
      ... When managing a large team, I found there were two enormous pressures that tempted me
      to quit learning.

**LO QUE LA SALIDA MIDE:** `L373` dice **`three`** y nombra los tres, **y los tres nombres son
exactamente los rotulos de `L375`, `L381` y `L385`, al caracter.** `L401` dice **`two`** y sus dos
mitades son `L403` (`Pressure to be consistent`, ya en el grafo) y `L409` (`Burnout`, en bandeja).

**`D.37` en su forma fuerte se cumple en las dos series, medido y no citado de memoria.** Es
exactamente lo que mi encargo de la vuelta 28 daba por bueno, **y hoy lo he comprobado yo.**

### 7.2. EL BARRIDO DE LOS QUE ESPERAN, PARA QUE LA VUELTA SIGUIENTE SEPA LO QUE LE VIENE

<!-- salida: .v29/barrido_bandeja_v29.txt, lector .v29/barrido_v29.py -->

*El mismo lector, la misma poblacion de `348`, los mismos umbrales sin tocar. **Esto no lo pide
ninguna regla: lo corro porque la cola de lectura de la vuelta siguiente sale de aqui.***

    $ python .v29/barrido_v29.py <los 12 de cap_07 que esperan>
      poblacion del barrido : 348   (243 del grafo mas 105 que esperan en bandejas)

| candidato de la bandeja | **vecinos que superan umbral** | su senial mas alta |
|---|---:|---|
| `parar_debate_emocion_agotamiento` | **9** | `similitud_texto=0.476` contra `pedir_hechos_decision_evitar_recomendaciones` |
| `fijar_fecha_cierre_debate_equipo` | **4** | **`paso_contra_nodo=0.61`** contra `explicar_idea_facil_comprender_oyente` |
| `repartir_decision_cercanos_hechos` | **1** | `similitud_texto=0.352` contra `centrar_debate_ideas_fuera_egos` |
| `pedir_hechos_decision_evitar_recomendaciones` | **7** | `similitud_texto=0.472` contra `parar_debate_emocion_agotamiento` |
| `persuadir_emocion_oyente_no_propia` | **3** | `similitud_texto=0.371` contra `explicar_idea_facil_comprender_oyente` |
| `establecer_credibilidad_pericia_humildad` | **3** | `similitud_texto=0.368` contra `compartir_logica_mostrar_razonamiento` |
| `compartir_logica_mostrar_razonamiento` | **10** | `similitud_texto=0.381` contra `minimizar_impuesto_colaboracion_equipo` |
| `minimizar_impuesto_colaboracion_equipo` | **10** | **`similitud_texto=0.501`** contra `aprender_resultados_vencer_dos_presiones` |
| `proteger_tiempo_equipo_jefe` | **10** | **`paso_contra_nodo=0.625`** contra `bloquear_tiempo_pensar_calendario` |
| `mantener_manos_trabajo_real_equipo` | **8** | `similitud_texto=0.404` contra `proteger_tiempo_equipo_jefe` |
| `reservar_calendario_tiempo_ejecutar` | **7** | `similitud_texto=0.409` contra `proteger_tiempo_equipo_jefe` |
| `cuidarse_agotamiento_centro_rueda` | **5** | `similitud_texto=0.402` contra `cambiar_posicion_hechos_explicar_cambio` |

**LO QUE LA SALIDA MIDE, y la cuenta la hace un comando y no yo:**

    $ grep -c "^CANDIDATO" .v29/barrido_bandeja_v29.txt
      candidatos con salida: 12
    $ grep -c "^   - " .v29/barrido_bandeja_v29.txt
      vecinos por encima de umbral: 77

**Los `12` terminaron, y levantan `77` vecinos por encima de umbral.** Escribi esta seccion cuando el
lector llevaba `10` y `65`, **con los dos que faltaban declarados por su nombre en vez de estimados**;
los dos entraron antes de cerrar la pagina **y la cifra que publico es la del comando de ahora, no la
de entonces.** `12` de `12`.

> **`LECTURA`: `cap_07` se va a leer caro.** El nodo mas corto de los doce,
> `minimizar_impuesto_colaboracion_equipo` con `4` pasos, **levanta `10` vecinos**, y
> `compartir_logica_mostrar_razonamiento` con `6` levanta otros `10`. **Un nodo corto levanta mas
> vecinos que uno largo**, que es al reves de lo que parece razonable, **y el motivo esta en que
> `similitud_texto` sobre poco texto sube.** `CALIBRACION_D4.md` ya documenta la banda alta del
> ruido, asi que **esto no es un hallazgo nuevo: es esa banda, sobre un capitulo lleno de piezas
> de cuatro y cinco pasos.**
>
> **LO QUE SI ES UNA CIFRA PARA EL ENCARGO:** la cabeza de la serie `D.37` levanta `10` y sus tres
> partes levantan **`10`, `8` y `7`**, **y las cuatro tienen que entrar en la misma vuelta** para que
> la serie no quede partida. **`35` lecturas de par solo por esa serie**, cabeza incluida. Y el que
> menos levanta de los doce es `repartir_decision_cercanos_hechos` con **`1`**, que es el mas largo
> de tramo (`259`-`289`): **el tramo largo da nodo limpio y el corto da cola de lectura.**

### 7.3. **UN PAR QUE MI LECTURA LEVANTA Y QUE NINGUNA SENIAL DE MI BARRIDO LEVANTO**

*Y lo publico **sin clase**, que es la mitad que me costo una caida en la `ACTA 27`.*

<!-- salida: .v29/cluster_tiempo.txt -->

    $ los cuatro nodos del calendario, con su capitulo y sus pasos
      bloquear_tiempo_pensar_calendario     [cap_11]  6 pasos
      reservar_calendario_tiempo_ejecutar   [cap_07]  4 pasos
      proteger_tiempo_equipo_jefe           [cap_07]  9 pasos
      agendar_cuidados_propios_cumplirlos   [cap_08]  5 pasos

    $ y los tres que me interesan, ninguno vive todavia en el grafo
      bloquear_tiempo_pensar_calendario          grafo:0  bandeja:1
      agendar_cuidados_propios_cumplirlos        grafo:0  bandeja:1
      reservar_calendario_tiempo_ejecutar        grafo:0  bandeja:1

**EL PAR: `bloquear_tiempo_pensar_calendario` (`cap_11`) contra `agendar_cuidados_propios_cumplirlos`
(`cap_08`).** Lo que sus pasos dicen, uno al lado del otro:

| | `bloquear_tiempo_pensar_calendario` | `agendar_cuidados_propios_cumplirlos` |
|---|---|---|
| ponerlo en el calendario | paso `3`: *agenda algo de tiempo para pensar, y manten ese tiempo sagrado* | paso `1`: *pon en tu calendario las cosas que necesitas hacer para ti, igual que pondrias una reunion importante* |
| que nadie lo pise | paso `4`: *hazle saber a la gente que no pueden agendar nada encima de el, nunca* | paso `5`: *no dejes que otros te pongan cosas encima de ellas* |
| defenderlo | paso `5`: *enfadate de verdad, y en serio, si lo intentan* | paso `4`: *no te saltes esas reuniones contigo mismo* |
| **lo que queda fuera** | pasos `1` y `2`: el diagnostico del calendario lleno; paso `6`: animar al equipo a hacer lo mismo | pasos `2` y `3`: **el tiempo de desplazamiento y hacer como si tuvieras que coger un tren** |

    $ grep -c agendar_cuidados_propios_cumplirlos .v29/barrido_bandeja_v29.txt
      1
    $ grep -B20 agendar_cuidados_propios_cumplirlos .v29/barrido_bandeja_v29.txt | grep '^CANDIDATO' | tail -1
      CANDIDATO : minimizar_impuesto_colaboracion_equipo   (4 pasos)

**LO QUE LAS DOS SALIDAS MIDEN:** en las `77` lineas de vecinos de mi barrido,
`agendar_cuidados_propios_cumplirlos` **aparece UNA sola vez**, y aparece como vecino de
`minimizar_impuesto_colaboracion_equipo`. **No aparece ni una vez frente a
`bloquear_tiempo_pensar_calendario`**, que es el par que mi lectura levanta.

**Y lo que el barrido SI cruza, para no dar a entender que no cruza nada:**
`reservar_calendario_tiempo_ejecutar` contra `bloquear_tiempo_pensar_calendario` por
`familia_id=0.333`, y `proteger_tiempo_equipo_jefe` contra `bloquear_tiempo_pensar_calendario` por
`paso_contra_nodo=0.625`, **que es la senial mas alta de las `77`.** **El cluster del calendario esta
medio levantado por la maquina: lo que falta es justo la pareja que mas se parece leyendola.**

> **`LECTURA`, y me paro justo antes de la clase: los dos nodos comparten TRES movimientos de
> procedimiento** (ponerlo en el calendario, no dejar que nadie lo pise, defenderlo), **y lo que
> queda fuera es procedimiento en un lado** (el tren, el desplazamiento) **y diagnostico en el otro.**
> Eso es exactamente el sitio donde `6.1` dice que se decide, **y es exactamente el sitio donde no me
> corresponde decidir en la fase ciega.**
>
> **NO ESCRIBO NI `CONTINUA` NI `SANO` NI `MUTUO`, y digo por que:** en la `ACTA 27` `8.1` me conte
> una `CIFRA PUBLICADA PROPIA` por publicar en esta misma sede sellada **el resultado de una lectura
> discutible como si fuera una cifra**, y la adjudicacion me la retiro. **El remedio que me encargue
> es este: publicar la duda, no el resultado.**
>
> **`POR ADJUDICAR 11.`** Y lo que sostiene que merece mirarse no es una senial: **es que los dos
> nodos son de capitulos distintos, ninguno vive aun en el grafo, y el barrido no los cruza**, asi
> que si nadie lo escribe ahora **entraran en vueltas distintas y nadie los va a poner uno al lado
> del otro.** Eso es lo que `D.19` avisa: **la senial dijo donde mirar y ahi acabo su trabajo.**

### 7.4. EL PAR QUE VUELVE, Y LO DEJO DICHO ANTES DE QUE VUELVA

**`fijar_fecha_cierre_debate_equipo` (`245-257`) sigue en la bandeja, y `centrar_debate_ideas_fuera_egos`
(`225-229`) ya vive en el grafo.** Cuando el primero entre, **ese par se va a levantar otra vez**: es
el `DISCUTIBLE 3` de la vuelta 27, **el que mi apertura anterior publico como arista y mi propia
`ACTA 27` `2.2` retiro con el libro abierto.**

> **`LECTURA`: la adjudicacion de la `ACTA 27` `2.2` es `SANO SIN ARISTA`, y no la reabro.** El
> procedimiento del cambio de papeles esta en `L229`, **que es el parrafo del propio hijo**, y `L257`
> es una remision hacia atras veintiocho lineas despues. **Lo digo aqui para que cuando ese par
> aparezca no se vuelva a discutir desde cero**, y para dejar constancia de que **no estoy
> aprovechando una apertura nueva para reabrir la que perdi.**

---

## 8. LO QUE MIDO SOBRE MI PROPIA HERENCIA Y NO SOBRE LA VUELTA

**El arnes me entrego `1` heredado. Mi propia `ACTA 27` seccion `10` se encargo `2` remedios.** Los
dos son de sustancia de auditoria (`D.38.2`) y los dos los cumplo en esta pagina:

| # | **el remedio que me encargue** | **como lo cumplo hoy** |
|---:|---|---|
| **1** | ninguna celda publica como cifra el resultado de una lectura que el turno normal aun tiene que adjudicar; va como `POR ADJUDICAR` | **la seccion `9` trae `11`**, y `grep -c` lo cuenta abajo |
| **2** | la relectura ciega destapa **una razon por vez** y **despues** de imprimir sus pasos | **la bitacora es el ultimo fichero que abri** (`10:20` contra `10:03`), **y no he abierto ni una razon**. La unica clase que reclamo ciega es la de `4.3` |

    $ grep -c "POR ADJUDICAR" docs/loop/APERTURA_CIEGA.md
      18      (los 11 numerados de la seccion 9, mas las menciones que los anuncian)

### 8.1. **MI PROPIO `D.41` PARA ESTA PAGINA, PORQUE NADIE MAS LA MIDE**

*La seccion `1.2` mide que el censo de `D.42` no lee este fichero y que el tallado de `D.41` solo
lee `REPORTE.md`. **Una sede que ninguna guarda mide es justo donde una celda falsa sobrevive**, y en
esta sede ya sobrevivio una (`ACTA 27` `8.1`). Asi que la mido yo.*

<!-- salida: .v29/verificar_apertura.txt, .v29/verificar_apertura2.txt, .v29/verificar_pegados.txt -->

    $ python .v29/verificar_apertura.py     (las 25 filas de cap_07 contra su instrumento)
      filas en el instrumento : 25
      filas pegadas en el doc : 25
      en el doc y NO en el instrumento (celdas inventadas) : 0
      en el instrumento y NO en el doc (filas que me deje) : 0
      VERDE

    $ python .v29/verificar_apertura2.py    (los 15 vecinos contra su instrumento)
      vecinos en el instrumento : 15
      vecinos pegados en el doc : 15
      INVENTADOS en el doc      : 0
      que me deje sin pegar     : 0

    $ python .v29/verificar_pegados.py      (toda fila de bitacora pegada como salida)
      filas de bitacora presentadas como salida : 29
      las que NO viven literales en .v29/       : 0
      VERDE: toda fila pegada vive literal en su instrumento

    $ python .v29/verificar_estricto.py     (TODA linea de salida con un id de nodo)
      lineas de salida con id de nodo : 102
      las que NO viven literales      : 0
      VERDE: ninguna linea de salida esta tecleada

    $ python forja.py guiones docs/loop/APERTURA_CIEGA.md
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

**El lector estricto compara las `102` contra `.v29/*.txt` **y contra el `resumen_teorico` de los
nodos**, porque tambien cito de ahi, y compara sin contar el espaciado.**

> ### **Y LO DIGO PORQUE ME CAZO A MI: LA PRIMERA VERSION DE ESTA PAGINA NO PASABA SU PROPIO LECTOR**
>
> El lector encontro **`28` lineas** que yo habia tecleado dentro de bloques presentados como salida
> de instrumento. Las cuatro que de verdad decian algo que la salida no dice:
>
> 1. **le quite la columna `consumada` al bloque de las lineas `265` a `289`**;
> 2. **le aniadi un `[False]` de mi mano al bloque de `269` a `278`**;
> 3. **comprimi veintitres lineas de solapadas en una sola fila con un `(23)` al lado**, y esa fila
>    el instrumento no la imprime: la sumaba yo;
> 4. **me deje las dos anotaciones `(tramo no contiguo: ...)`** que el lector de `cap_07` si imprime,
>    justo en las dos filas donde mas falta hacen.
>
> **Ninguna cifra era falsa. Lo falso era decir que la salida decia eso.** Es la especie exacta que
> `D.41` existe para cazar y que la `ACTA 24` conto con `14` celdas en una tabla mia.
>
> **Lo arregle pegando la salida literal y separando mi cuenta de la del instrumento con una linea
> que dice que es mia.** Y dejo escrito lo que mas me importa de todo esto: **esta pagina no la mide
> ninguna guarda de la casa** (`1.2`), **asi que el lector que la midio lo tuve que escribir yo, y
> hasta que lo escribi la pagina estaba mal.** Eso es un argumento a favor de que `D.42` la lea, y va
> con el `POR ADJUDICAR 3`.

---

## 9. LOS ONCE `POR ADJUDICAR`, REUNIDOS

*Cada uno tendra su seccion en el acta. Ninguno es una cifra cerrada.*

| # | **POR ADJUDICAR** | donde lo mido |
|---:|---|---|
| **1** | el remedio de `HEREDADO 1` esta en el codigo, **y la misma vuelta escribio diez lineas mas con la forma del fallo**. Cual de las dos cosas paso primero | `0.2` y `6` |
| **2** | `D.42` y `D.34.2` se contradicen en la fase ciega: el censo cae por tres ficheros **que el arnes retira** y uno **que deja en cero bytes** | `1.1` |
| **3** | el censo de `D.42` **no lee `APERTURA_CIEGA.md`**, que es sede de una `CIFRA PUBLICADA PROPIA` ya contada | `1.2` |
| **4** | `cap_07` no esta entrando en el orden del libro. **Cuales de esos desordenes son de esta vuelta y cuales heredados** | `3.2` |
| **5** | `LISTEN`, `CLARIFY` y `DEBATE` no los reclama nadie; `DECIDE`, `PERSUADE`, `EXECUTE` y `LEARN` si. **La misma clase de material tratada de dos maneras** | `3.3` |
| **6** | `cap_07.md` dice `unidad: Cap. 4` en su cabecera y trae la portadilla de `PART II` pegada al final. **Es del recorte** | `3.4` |
| **7** | la madre de la rueda **omite `Debate` y `Decide`** de los siete pasos, porque esos dos se fueron a un hermano | `4.4` |
| **8** | los `10` pares de `crear_obligacion_disentir_equipo` **escritos dos veces**, con la linea `279` fechando el orden | `6` |
| **9** | **ninguna linea dice `consumada: true`**: el campo solo sabe negar | `6.1` |
| **10** | las `8` de `SIN HUELLA` dicen que **la huella guardada del vecino es la de un nodo VACIO**, y un vecino de bandeja tiene texto | `6.2` |
| **11** | `bloquear_tiempo_pensar_calendario` contra `agendar_cuidados_propios_cumplirlos`: **tres movimientos de procedimiento compartidos, de dos capitulos distintos, y mi barrido no los cruza.** Lo publico **sin clase** | `7.3` |

---

## 10. MI APERTURA CIEGA EN UNA TABLA

**Todas estas cifras tienen su instrumento y su salida pegada arriba. Ninguna esta contada a ojo.**

| | |
|---|---:|
| **ACTA ANTERIOR LEIDA** | `1f7f256d3dce8bb70708b83f303f8d75953dfa0c`, **comprobada con `git hash-object`** |
| **HEREDADO 1** | **CUMPLIDO**, las dos mitades medidas (`0.2`) |
| nodos en el grafo | **243** |
| lineas en la bitacora | **289**, de ellas **14** NO CONSUMADAS |
| poblacion de mi barrido (`D.38.4`) | **348** = `243` grafo mas `105` bandejas |
| guardas en verde | **`gate`, `guiones`, `resolutor`** |
| guardas en rojo | **2**: `test_aceptacion` (`1` de `176`) y `censar_rutas` (`4` de `96`), **las dos por la retirada de `REPORTE.md` de mi propia fase** |
| piezas de `cap_07` | **25**: `13` en el grafo, `12` en bandeja |
| rotulos de `cap_07` | **49**, de ellos **11 sin nodo** |
| cobertura de linea de `cap_07` | **160** de **220** lineas con texto |
| piezas que entraron en la vuelta | **4**: `3` de `cap_07` y `1` de `cap_11` |
| pasos que lei contra su parrafo | **45 de 45**, no una muestra |
| **PUENTE que yo leo** | **0** |
| **`PASOS INVENTADOS`** | `cap_07` **0,00 por ciento**, `cap_11` **0,00 por ciento** |
| pares que levanta mi barrido | **15** |
| pares consumados que escribio la aduana | **15**, **coinciden uno a uno por nombre** |
| clases que reclamo como **ciegas** | **1**, la arista de la rueda de `4.3`, **con la hora de mis ficheros como prueba del orden** |
| clases que **NO** reclamo como ciegas, y lo digo yo | **14** (`5.1`) |
| candidatos de bandeja clasificados a ciegas | **12**, **los 12 PROCEDIMIENTO y ninguno POSTURA** |
| barrido de los que esperan | **12 de 12**, y levantan **77** vecinos por encima de umbral |
| pares que mi lectura levanta y mi barrido no | **1**, y lo publico **SIN CLASE** (`7.3`) |
| series `D.37` comprobadas en el libro | **2**: `three` en `L373` y `two` en `L401` |
| **`POR ADJUDICAR`** | **11** |
| caidas de metodo mias declaradas en esta pagina | **2**: el `grep` truncado por `cut` que casi me hace publicar un `PUENTE` inexistente (`4.1`), y las **`28`** lineas que teclee dentro de bloques de salida y que mi propio lector me tumbo (`8.1`) |
| lectores que escribi para medirme a mi mismo | **4**, y **los cuatro en VERDE** solo despues de arreglar lo que cazaron (`8.1`) |

**No commiteo. El arnes sella esta pagina y la commitea el, y no la vuelvo a tocar** (`D.34`).
