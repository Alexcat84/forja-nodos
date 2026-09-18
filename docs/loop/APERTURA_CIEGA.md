# APERTURA CIEGA DEL AUDITOR, VUELTA 40, lote 4 (`scott_radical_candor`), `cap_13`

*Escrita antes de que el arnes me exponga `docs/loop/REPORTE.md`. Los cuatro ficheros que
`D.34.2` retira NO estan en el arbol y NO los he recuperado de git ni por ninguna otra via.
Lo que si he abierto, y `AUDITOR_FORJA.md` 1.5 dice con todas sus letras que puedo, es
`docs/loop/ACTA_AUDITOR.md`, que es obra mia, y `docs/loop/PROMPT_SIGUIENTE.md`, que es mi
propia sede (`5.6`).*

## 0. LO QUE EL ARNES EXIGE QUE TRAIGA, Y VA PRIMERO

    ACTA ANTERIOR LEIDA: 933e92c4bb7d7d4ed1424eb9593a89fa67ae0706
    HEREDADO 1: CUMPLIDO

**LA HUELLA NO LA COPIO DEL PROMPT: LA MIDO** (`D.38.3`), y sale la que el prompt me
entrega:

    $ git hash-object docs/loop/ACTA_AUDITOR.md
      933e92c4bb7d7d4ed1424eb9593a89fa67ae0706

    $ python forja.py herencia | grep -E "su huella|heredados"
      su huella     : 933e92c4bb7d7d4ed1424eb9593a89fa67ae0706
      heredados     : 1

### 0.1. `HEREDADO 1`, CUMPLIDO, Y CUMPLIDO CORRIENDO EL INSTRUMENTO Y NO ACORDANDOME

> **TAREA BLOQUEANTE DEL AUDITOR, para la `ACTA 39`: toda poblacion de barrido que yo publique
> en la apertura ciega se compara contra la linea `blocking multi señal contra N` del registro
> de insercion de ese mismo candidato ANTES de escribir la frase del cruce, y esa linea va
> pegada al lado de la mia. Si en esa fase no puedo leer el registro, escribo que NO la he
> cruzado, en vez de escribir que cuadra.**

**LO CUMPLO POR LA VIA MAS CORTA QUE EXISTE: CORRIENDO YO EL INSTRUMENTO QUE ESCRIBE ESA
LINEA**, en esta misma fase y sobre este mismo arbol, uno por candidato, que es el metodo
vigente de `D.38.4` despues de su correccion declarada del 16 sep. Asi las dos cifras salen
del mismo instante y el cruce no depende de ningun registro ajeno.

    $ for c in <los cuatro>; do python forja.py informe cuarentena/scott_radical_candor/$c.json; done
      poblacion del barrido       : 348   (324 del grafo mas 24 que esperan en bandejas)
      poblacion del barrido       : 348   (324 del grafo mas 24 que esperan en bandejas)
      poblacion del barrido       : 348   (324 del grafo mas 24 que esperan en bandejas)
      poblacion del barrido       : 348   (324 del grafo mas 24 que esperan en bandejas)

**Y LA MIA, CONTADA APARTE Y CON SUS DOS MITADES A LA VISTA:**

    $ wc -l dataset/nodos.jsonl
        324 dataset/nodos.jsonl
    $ ls cuarentena/*/*.json | grep -v _insertados | grep -v _derivadas | grep -v ensayo_referencia_163 | wc -l
        24
    $ python -c "from src import aduana; print(len(aduana.poblacion_de_bandejas()))"
        24

**EL CRUCE, ESCRITO DESPUES DE LEER LAS DOS Y NO ANTES: CUADRAN EN `348`**, y la unica
diferencia es la que la casa tiene escrita. **`348` es lo que la maquina publica; `347` es
contra lo que cada candidato se mide**, porque un nodo no es vecino de si mismo y el barrido
se hace uno por vez (`D.38.4`, correccion declarada de la `ACTA 18`). **No es discrepancia: es
la exclusion que esa correccion ordena, y la digo en vez de dejar que se lea como un
descuadre de uno.**

> **LECTURA:** esto es lo que mi caida de la `ACTA 38` `7.1` no hizo. **Alli publique `345`,
> `346` y `347` contra `348`, `348` y `348` y escribi que cuadraban sin haber leido la linea
> de la maquina.** Hoy la linea esta pegada arriba, la mia debajo, y la frase del cruce va
> escrita detras de las dos.

## 1. LOS INSTRUMENTOS DE ESTA FASE, CON SU SALIDA

| instrumento | salida |
|---|---|
| `gate` | **VERDE**, 324 nodos |
| `guiones` | **VERDE**, cero largos y cero medios |
| `tests/test_aceptacion.py` | **ROJO: 294 pruebas, 3 fallos, 1 errores** |
| `rancios` (`D.15`) | **64** `RANCIO`, **8** `SIN HUELLA` |
| `credito` | **NO MIDE: su sede no esta en el arbol** (seccion 4.1) |

    $ python forja.py gate
      GATE VERDE.
        nodos verificados: 324

    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python tests/test_aceptacion.py | tail -2
      total: 294 pruebas, 3 fallos, 1 errores

    $ python forja.py rancios | grep -c "\[RANCIO\]"
      64
    $ python forja.py rancios | grep "BLOQUE DE VIGENCIA" -A 1
      BLOQUE DE VIGENCIA: 72 hallazgo(s) sobre 493 veredicto(s) y 0 cita(s).
        RANCIO 64, SIN HUELLA 8

**EL COMANDO DE LOS RANCIOS ES EL BUENO Y ESO ES UN REMEDIO MIO CUMPLIDO:** mi `ACTA 38`
`7.2` registro que `grep -c "RANCIO"` daba `52` donde el instrumento declara `51`, porque la
linea de resumen tambien lleva la palabra. **Hoy corro `grep -c "\[RANCIO\]"`, da `64`, y la
propia linea de resumen del instrumento dice `RANCIO 64`. Las dos cifras salen iguales.**

    $ python -c "(cuenta de nodos_previos y nodos_siguientes de dataset/nodos.jsonl)"
      nodos_previos  : 134
      nodos_siguientes: 134
    $ python -c "(veredictos por clase de bitacora/VEREDICTOS.jsonl)"
      CONTINUA      154
      CORREGIDO      10
      SANO          343
      TOTAL         507

## 2. MI TRAMO, CONTADO ANTES DE LEERLO

    $ python -c "(pasos_accionables por candidato, y el denominador de cap_13)"
      abrazar_incomodidad_silencio_contar_seis              12
      escuchar_entender_critica_dominar_defensa             13
      premiar_franqueza_hacer_escucha_tangible              20
      integrar_peticion_critica_rutina_existente            13
      MI TRAMO                                              58

      cap_13 en bandeja    :  6 candidatos, 111 pasos
      cap_13 ya insertados :  6 candidatos, 101 pasos
      cap_13 ENTERO        : 12 candidatos, 212 pasos

**Y LOS CUATRO ROTULOS, CONTRA EL FICHERO FUENTE Y NO CONTRA LA FICHA:**

    $ grep -nE "^(EMBRACE THE DISCOMFORT|LISTEN WITH THE INTENT|MAKE LISTENING TANGIBLE|BUILD IT INTO YOUR EXISTING SCHEDULE)" fuentes/scott_radical_candor/cap_13.md
      187:EMBRACE THE DISCOMFORT
      199:LISTEN WITH THE INTENT TO UNDERSTAND, NOT TO REPLY
      215:MAKE LISTENING TANGIBLE: REWARD THE CANDOR
      235:BUILD IT INTO YOUR EXISTING SCHEDULE

> **LECTURA:** las cuatro lineas que las fichas declaran como su rotulo son las cuatro lineas
> que el fichero tiene. **Los cuatro cortes de frontera estan donde dicen que estan.**

## 3. MIS `20` CLASES CIEGAS, PAR A PAR

**LAS ADJUDICO ANTES DE ABRIR `bitacora/VEREDICTOS.jsonl`**, que es lo que `AUDITOR_FORJA.md`
1.2 manda: primero los pasos de los dos nodos, despues mi clase, y la razon escrita del
extractor se destapa DESPUES. **En esta fase no he abierto la bitacora.**

**LO QUE SI HE TENIDO DELANTE, Y LO DIGO PORQUE NO PUEDO EVITARLO:** el campo
`resumen_teorico` de cada candidato lleva escrita la lectura del propio extractor. **La ficha
es lo que el arnes me manda abrir.** Asi que para cada par he impreso los pasos del candidato
y los del vecino y los he leido contra la linea del libro **antes** de darle la razon o
quitarsela.

### 3.1. La tabla

| # | candidato | vecino | quien lo levanta | **mi clase** |
|---:|---|---|---|---|
| 1 | `abrazar_incomodidad` | `escuchar_entender` (bandeja) | `similitud_texto 0.449` | **`SANO`** |
| 2 | `abrazar_incomodidad` | `premiar_franqueza` (bandeja) | `similitud_texto 0.353` | **`SANO`** |
| 3 | `abrazar_incomodidad` | `contar_historias_propias_explicar_franqueza_radical` | `similitud_texto 0.376` | **`SANO`** |
| 4 | `abrazar_incomodidad` | `pedir_critica_primero_crear_seguridad_psicologica` | **ninguna**, lectura `D.37` | **`CONTINUA`** |
| 5 | `abrazar_incomodidad` | `abrazar_incomodidad_arrancar_critica_equipo` (`cap_09`) | **ninguna**, lectura mia | **`CONTINUA`**, MI `DISCUTIBLE 1` |
| 6 | `escuchar_entender` | `cambiar_forma_trabajar_conservar_plantilla` (bandeja marquet) | `paso_contra_nodo 0.634` | **`SANO`** |
| 7 | `escuchar_entender` | `contar_historias_propias_explicar_franqueza_radical` | `similitud_texto 0.393` | **`SANO`** |
| 8 | `escuchar_entender` | `abrazar_incomodidad` (bandeja) | `similitud_texto 0.446` | **`SANO`** |
| 9 | `escuchar_entender` | `premiar_franqueza` (bandeja) | `similitud_texto 0.363` | **`SANO`** |
| 10 | `escuchar_entender` | `pedir_critica_primero_crear_seguridad_psicologica` | **ninguna**, lectura `D.37` | **`CONTINUA`** |
| 11 | `escuchar_entender` | `abrazar_incomodidad_arrancar_critica_equipo` (`cap_09`) | **ninguna**, lectura mia | **`CONTINUA`**, MI `DISCUTIBLE 2` |
| 12 | `escuchar_entender` | `crear_cultura_escucha_equipo` (`cap_07`) | **ninguna** | **`SANO`** |
| 13 | `escuchar_entender` | `escuchar_callado_equipo_tranquilizar_incomodo` (`cap_07`) | **ninguna** | **`SANO`** |
| 14 | `premiar_franqueza` | `escuchar_entender` (bandeja) | `similitud_texto 0.375` | **`SANO`** |
| 15 | `premiar_franqueza` | `pedir_critica_primero_crear_seguridad_psicologica` | **ninguna**, lectura `D.37` | **`CONTINUA`** |
| 16 | `premiar_franqueza` | `abrazar_incomodidad_arrancar_critica_equipo` (`cap_09`) | **ninguna**, lectura mia | **`CONTINUA`**, MI `DISCUTIBLE 3` |
| 17 | `premiar_franqueza` | `pedir_critica_equipo_premiarla` (`cap_05`) | **ninguna** | **`SANO`**, MI `DISCUTIBLE 4` |
| 18 | `integrar_peticion` | `pedir_critica_primero_crear_seguridad_psicologica` | `paso_contra_nodo 0.733` | **`SANO`** |
| 19 | `integrar_peticion` | `abrazar_incomodidad` (bandeja) | `similitud_texto 0.356` | **`SANO`** |
| 20 | `integrar_peticion` | `montar_reuniones_solas_mentalidad_frecuencia` (`cap_11`) | **ninguna** | **`SANO`** |

**`14` `SANO` y `6` `CONTINUA`.** De los `20` pares, **`10` los levanta una señal y `10` los
traigo yo por lectura.** Las cifras de la columna de la señal salen del informe y no de mi
cabeza:

    $ (los cuatro informes, la cola de lectura de cada uno)
      abrazar_incomodidad : vecinos levantados en total : 3   (similitud_texto 3)
      escuchar_entender   : vecinos levantados en total : 4   (paso_contra_nodo 1, similitud_texto 3)
      premiar_franqueza   : vecinos levantados en total : 1   (similitud_texto 1)
      integrar_peticion   : vecinos levantados en total : 2   (paso_contra_nodo 1, similitud_texto 1)

### 3.2. Los `14` `SANO`, y por que ninguno me hace dudar

**LOS SEIS DE LA MISMA SERIE ENTRE SI** (pares `1`, `2`, `8`, `9`, `14`, `19`): son partes
distintas de los cuatro elementos que la `L113` enumera, con entregable y condicion de
activacion propios cada una. **`D.37`, apartado *lo que NO autoriza*: dos partes de la misma
cabeza son hermanas, no madre e hijo.**

**EL PAR `18`, QUE ES EL DE LA SEÑAL MAS ALTA DE TODO EL TRAMO** (`paso_contra_nodo 0.733`,
paso `6` del candidato contra paso `17` de la cabeza): **`SANO`**. El `P17` de la cabeza
enumera los cuatro elementos y el `P06` de `integrar_peticion` los vuelve a nombrar, pero
**nombrar no es procedimentar** (`P.5.1`, congelada): `integrar_peticion` no es ninguno de los
cuatro, es lo que la `L237` manda hacer **despues** de los cuatro, y `D.37` dice que eso es
hermano. **Y no lo decido hoy por primera vez: lo adjudique igual en mi apertura sellada de la
vuelta 39, y una vara no da dos respuestas a la misma figura.**

**EL PAR `6`, QUE ES EL QUE MAS ME ENSENIA Y NO ES DE CONTENIDO:**

    paso 4 del candidato contra paso 2 de cambiar_forma_trabajar_conservar_plantilla
    similitud_texto 0.215 | familia_id 0.000 | paso_contra_nodo 0.634

> **LECTURA, y va marcada aparte de la cifra:** el paso `4` de `escuchar_entender` dice *y
> sobre todo practica con otros, que es lo que el texto pone por encima de lo demas*, y el
> paso `2` del de Marquet dice *centrate en trabajar con lo que tienes, que es lo que el texto
> recomienda por encima de mucha rotacion*. **Son dos libros distintos, dos dominios que no se
> tocan, y lo unico que comparten es el molde de redaccion de esta casa: `que es lo que el
> texto pone por encima de`.** La señal `paso_contra_nodo` cruzo el umbral por la frase de
> andamiaje que el extractor escribe en todos sus pasos, no por lo que los pasos dicen.
> **`SANO` sin reparo, y la observacion sube a mi acta porque toca a la pregunta `8` de la
> cola de doctrina, que es justo esta.**

### 3.3. **LOS TRES `CONTINUA` QUE NINGUNA SEÑAL LEVANTA, Y ES LO QUE TRAIGO A ESTA VUELTA**

**HAY UN NODO YA EN EL GRAFO QUE ES CABEZA DE SERIE `D.37` Y QUE EL BARRIDO NO NOMBRA NI UNA
VEZ EN LOS CUATRO INFORMES.** Es `abrazar_incomodidad_arrancar_critica_equipo`, de `cap_09`:

    $ python -c "(su titulo y su nombre_largo, leidos de dataset/nodos.jsonl)"
      TITULO: Abrazar la incomodidad para arrancarle la critica a tu equipo, con los
              seis consejos que el texto nombra uno a uno
      NOMBRE LARGO: Como se consigue que el equipo critique al jefe: la excepcion
              publica, la pregunta de cabecera, el silencio contado, la escucha que
              no debate, el premio visible y la cuenta semanal

**DICE CUANTAS PARTES TIENE (`seis`) Y LAS NOMBRA UNA A UNA.** Eso es exactamente lo que
`D.37` pide de una cabeza, con su correccion declarada del 11 sep delante, que es la lectura
estrecha: *dice cuantas partes hay Y las nombra*. **Y cuatro de esas seis son nodos de
`cap_13`:**

| el consejo de `cap_09` | su paso en la madre | el nodo |
|---|---|---|
| **la pregunta de cabecera** | `P07` | `elegir_pregunta_recurrente_pedir_critica`, **ya en el grafo desde la vuelta 39** |
| **el silencio contado** | `P09` y `P10` | `abrazar_incomodidad_silencio_contar_seis`, candidato `1` |
| **la escucha que no debate** | `P12` | `escuchar_entender_critica_dominar_defensa`, candidato `2` |
| **el premio visible** | `P14` y `P15` | `premiar_franqueza_hacer_escucha_tangible`, candidato `3` |

**Y LA `L113` DEL PROPIO LIBRO ESCRIBE LA DIRECCION, QUE ES LO QUE `6.1` PIDE:**

    L113  We'd like to go into more detail on each of the four tips for soliciting
          criticism offered in the book.

> **LECTURA:** el Afterword **declara por escrito que despliega lo que el libro ya dijo**. La
> direccion no la pongo yo por parecido: la pone la fuente. **Y no es `REPITE`**, porque lo
> que queda fuera del solape es procedimiento en los dos lados (`6.1`, sin bascula): la madre
> se queda con la excepcion publica, la pregunta de cabecera, el lenguaje corporal, la goma
> elastica, la cuenta semanal y el marco impreso; cada hijo trae un ejercicio rotulado
> `Practice:` con su montaje, sus actos y su resultado observable, **que la madre no tiene en
> ninguna forma.**

**MI CLASE PARA LOS TRES: `CONTINUA`, madre `abrazar_incomodidad_arrancar_critica_equipo`,
hijo el candidato, citando `P09`, `P12` y `P14`.**

**Y VAN MARCADOS DISCUTIBLES LOS TRES, CON LOS DOS REPAROS ESCRITOS Y NO ESCONDIDOS:**

1. **ES UNA SEGUNDA MADRE.** Los tres traen ya su arista `D.37` desde la cabeza de `cap_13`
   (`pedir_critica_primero_crear_seguridad_psicologica`, su `P17`). **Dos madres no estan
   prohibidas en este grafo** y la propia cabeza de `cap_13` tiene dos (`empezar_cultura` y
   `desplegar_plan`), pero el reparo lo deje escrito yo en la `ACTA 38` y no lo entierro aqui.
2. **LA MADRE DECLARO EN SU DIA QUE SUS SEIS CONSEJOS ERAN PASOS Y NO NODOS.** Su propio
   `resumen_teorico` lo dice: *los seis consejos van de pasos y no de nodos sueltos, porque la
   condicion es la misma para los seis*. **Eso era cierto dentro de `cap_09`**, donde los seis
   comparten una condicion de activacion; **el Afterword le da a cuatro de ellos condicion de
   activacion propia y ejercicio propio**, y por eso alli si son nodos. **No lo leo como
   contradiccion sino como el mismo material a dos alturas, pero es el punto por el que estos
   tres se caen si el extractor trae una razon mejor.**

> **Y LO QUE ESTO ARRASTRA, QUE NO ES DE MI TRAMO Y LO DIGO IGUAL:**
> `elegir_pregunta_recurrente_pedir_critica` **ya vive en el grafo** y es la pregunta de
> cabecera, el `P07` de esa misma madre. **Entro en la vuelta 39 sin esa arista.**
>
>     $ python -c "(previos y siguientes de elegir_pregunta_recurrente_pedir_critica)"
>       previos: ['pedir_critica_primero_crear_seguridad_psicologica']
>       siguientes: []
>
> **No lo encargo aqui, porque una apertura ciega no encarga.** Lo mido, lo escribo, y si la
> lectura se sostiene en mi turno normal sube al acta.

### 3.4. `DISCUTIBLE 4`: el par que el propio extractor llama el mas caro de fallar

`premiar_franqueza` contra `pedir_critica_equipo_premiarla` (`cap_05`). **Ninguna señal lo
levanta**, y no aparece en el informe del candidato `3`, que solo levanta uno.

**MI CLASE: `SANO`.** El `P10` de `cap_05` premia **la primera** franqueza y su caso es el te
de Tokio; el candidato entrega **la lista de las tres o cuatro criticas recientes contada en
publico** y el protocolo de la critica con la que no estas de acuerdo, que aquel no tiene en
ningun paso. **Ninguno de los dos despliega al otro y los entregables son distintos.**

> **LECTURA, y por eso va discutible aunque mi clase sea `SANO`:** el `P10` de `cap_05` cuenta
> que la autora dio las gracias en publico, mando una nota a mano y se aseguro de que todo el
> mundo supiera por que habia mejor te. **Eso es hacer tangible la escucha, que es el titulo
> mismo del candidato.** Lo que me hace quedarme en `SANO` es que aquello es **un caso
> narrado** y esto es **un ejercicio con etapas**, pero el solape existe y lo dejo a la vista
> en vez de enterrarlo bajo la palabra `SANO`.

## 4. LO QUE ME ENCUENTRO Y NADIE ME HA CONTADO

### 4.1. **FALTA UN QUINTO FICHERO EN EL ARBOL, Y NO ES NINGUNO DE LOS CUATRO QUE `D.34.2` RETIRA**

    $ git status --short docs/loop/
      D docs/loop/APERTURA_CIEGA.md
      D docs/loop/CREDITO_serial.jsonl
      D docs/loop/REPORTE.md
      D docs/loop/loop.log
      M docs/loop/ultimo_apertura.json
      D docs/loop/ultimo_auditor.json
      D docs/loop/ultimo_extractor.json

**`docs/loop/CREDITO_serial.jsonl` NO ESTA.** El prompt del arnes me nombra cuatro ficheros
retirados y ese no es uno de ellos. **NO LO RECUPERO**, ni de git ni de ninguna otra via, y lo
declaro aqui porque su ausencia **le hace decir a un instrumento de la casa una cosa falsa**:

    $ python forja.py credito
      CREDITO DE LA LINEA 'serial' (D.48)
        registro: docs/loop/CREDITO_serial.jsonl

        LINEA SIN REGISTRO: no hay ningun suceso escrito.
        Una linea sin tandas NACE CON SU RACHA EN CERO y no hereda
        la de nadie (D.48). Lo que herede el arnes sera CERO remedios.

> **LECTURA, y es la razon de que esto abra seccion propia:** **esa racha en cero es falsa y
> NO la publico como cifra.** Mi `ACTA 38` `9` cerro con `DATO MOVIDO` en **`1 de 2`** y con mi
> propia racha `AUDITOR` en **`1 de 3`**, y las dos siguen vivas: **ninguna tanda limpia ha
> pasado en medio y ninguna decision del fundador las ha reiniciado** (`5.4`, y `D.38.1`).
> **Un auditor que copiase ese cero de la maquina se estaria absolviendo con la mano de otro.**

### 4.2. LA SUITE DE ACEPTACION ABRE EN **ROJO**, Y LAS CUATRO CAIDAS SON DE ESTA FASE

**Las cuatro, sin excepcion, son ficheros que no estan en el arbol. Ninguna toca una regla de
dato.** Las nombro una a una porque un rojo sin desglosar se lee como un rojo cualquiera:

    $ python tests/test_aceptacion.py
      ERROR: test_el_reporte_vivo_pasa_su_propia_guarda
        FileNotFoundError: docs\loop\REPORTE.md
      FAIL: test_la_linea_serial_del_repo_tiene_su_registro_escrito
        AssertionError: docs/loop/CREDITO_serial.jsonl sin tandas: la migracion de D.48 no esta en el arbol
      FAIL: test_caso_positivo_un_frente_recien_nacido_hereda_cero
      FAIL: test_el_aviso_nombra_la_linea_y_su_registro
      total: 294 pruebas, 3 fallos, 1 errores

| la caida | su causa |
|---|---|
| el `ERROR` | `REPORTE.md`, **retirado por el arnes**, que es `D.34.2` haciendo su trabajo |
| **los TRES `FAIL`** | `CREDITO_serial.jsonl`, que **no** es uno de los cuatro de `D.34.2` (`4.1`) |

> **LECTURA:** la casa ya tiene el instrumento para esto y esta probado:
> `PruebaExencionDeMomento`, *la exencion del censo es de MOMENTO y no de fichero*, con su caso
> `test_caso_positivo_exenta_mientras_la_fase_ciega_esta_abierta` **en verde en esta misma
> corrida**. **Existe la exencion y estas cuatro no la tienen.** No adjudico aqui si eso es
> caida de nadie ni de que especie: lo mido, lo dejo escrito con la fecha de esta fase, y lo
> resuelvo en mi turno normal. **Lo que si digo hoy es que ninguna de las cuatro nace de una
> mano que haya tocado `dataset/`, `bitacora/` ni `censos/`.**

### 4.3. LA CORRECCION DE LA `TAREA 1.A` CAMBIA LA CIFRA QUE ELLA MISMA PUBLICA

**Es la caida `DATO MOVIDO` de mi `ACTA 38` `6`, y su remedio esta encargado en mi `TAREA
1.A`.** Mido el resultado hoy, sobre el arbol de esta fase:

    $ grep -o -iE "\bceo\b" dataset/nodos.jsonl | wc -l
      9
    $ grep -o -iE "consejero delegado" dataset/nodos.jsonl | wc -l
      45
    $ python -c "(los 9 hallazgos de \bceo\b, por nodo)"
      pedir_critica_primero_crear_seguridad_psicologica       9

> **LECTURA:** **los `9` estan los `9` dentro del mismo nodo que la correccion anexo**, y son
> el texto de la correccion citandose a si misma. La cifra que mi encargo publica (`ceo` como
> palabra da `0`, *consejero delegado* da `39`) **estaba medida sobre `e3950c6` y sus `321`
> nodos**, y sobre este arbol de `324` los mismos comandos dan `9` y `45`. **No digo que la
> cifra vieja sea falsa: digo que una correccion declarada escrita con su propio comando
> dentro mueve el comando.** No lo adjudico en esta fase.

### 4.4. LOS RANCIOS SUBEN DE `51` A `64`, Y ESTABA PREVISTO

**`51` al cierre de la `ACTA 38`, `64` hoy.** Mi propia `TAREA 1.A` lo escribio antes de que
pasara: *cuenta con que esta correccion vuelve a dejar rancios los veredictos emitidos contra
la huella vieja de ese nodo*. **Es `D.15`, cola de trabajo y no gate en rojo**, y el gate esta
en verde encima. **Lo dejo medido aqui para no tener que fiarme al cierre.**

## 5. MI RELECTURA DE FIDELIDAD `D.30`, PASO A PASO CONTRA SU LINEA

**LA HAGO YO Y CONTRA EL LIBRO, no contra el grafo y no contra la ficha** (`8.3`). Los `58`
pasos, uno por uno, contra la linea que su ficha declara:

| candidato | pasos | el reparto que declara | **lo que me sale a mi** |
|---|---:|---|---|
| `abrazar_incomodidad` | 12 | `P1` a `P6` de `L191`, `P7` a `P10` de `L195`, `P11` y `P12` de `L197` | **cuadra, 12 `TRANSCRIPCION`, 0 `PUENTE`** |
| `escuchar_entender` | 13 | `P1` y `P2` de `L203`, `P3` y `P4` de `L205`, `P5` a `P8` de `L209`, `P9` a `P12` de `L211`, `P13` de `L213` | **cuadra, 13 `TRANSCRIPCION`, 0 `PUENTE`** |
| `premiar_franqueza` | 20 | `P1` y `P2` de `L217`, `P3` y `P4` de `L219`, `P5` a `P7` de `L221`, `P8` a `P10` de `L225`, `P11` a `P13` de `L227`, `P14` y `P15` de `L229`, `P16` a `P20` de `L233` | **cuadra, 20 `TRANSCRIPCION`, 0 `PUENTE`** |
| `integrar_peticion` | 13 | `P1` a `P5` de `L111`, `P6` de `L237`, `P7` a `P10` de `L239`, `P11` de `L241`, `P12` y `P13` de `L245` | **cuadra, 13 `TRANSCRIPCION`, 0 `PUENTE`** |

> **LECTURA, y el `0` de hoy vale mas que el de la vuelta 39:** aquel `0` de `56` salio de tres
> candidatos que venian ya releidos de dos vueltas anteriores, y lo dije. **Estos cuatro no
> venian releidos**, traen la cuenta hasta seis, los tres minutos, las tres o cuatro criticas,
> el nueve de cada diez, las primeras veinte veces y dos nombres propios con su empresa y su
> cancion, **y aun asi los `58` estan en su linea.**

**LOS PASOS QUE RELEO POR LA CLAUSULA DE NOMBRE, CUENTA, ESCALON O SENTIMIENTO**, que el
encargo manda declarar aunque sean cero, **son `17` y van nombrados para que se puedan
comprobar uno a uno**: `abrazar_incomodidad` `P07`, `P08`, `P09`, `P10`; `escuchar_entender`
`P01`, `P06`, `P09`, `P11`, `P13`; `premiar_franqueza` `P03`, `P04`, `P05`, `P08`, `P14`;
`integrar_peticion` `P04`, `P06`, `P11`. **Ninguno sube a `PUENTE`.**

### 5.1. Las dos unicas cosas que apunto de los `58`, y ninguna es `PUENTE`

**`abrazar_incomodidad` `P06`** escribe *cuenta con lo que el texto ha medido en sus talleres*.
La `L191` dice *In our workshops participants often look puzzled... It sounds easy, but it
takes enormous discipline*. **El contenido esta entero en la linea y por eso no es `PUENTE`**;
lo que no esta es la palabra **medido**: el libro **observa** en sus talleres, no mide.
**Apunto el verbo, no el paso.**

**`premiar_franqueza` `P05`** escribe *la directora de Spanx, Sara Blakely*. La `L221` dice
*Spanx CEO Sara Blakely*. **Es una traduccion y no contenido inventado**, asi que
`TRANSCRIPCION`.

    $ grep -c "directora de Spanx" cuarentena/scott_radical_candor/premiar_franqueza_hacer_escucha_tangible.json
      1

> **LECTURA:** la casa acaba de dedicar su `TAREA 1.A` entera a como se escribe `CEO` en un
> campo, y hoy el catalogo dice *consejero delegado* `45` veces. **Este paso, que entra en la
> misma vuelta, dice *directora*.** No es caida de ninguna especie de `5.2` y no la cargo:
> **la dejo escrita porque una grafia que dos vueltas seguidas resuelven distinto se convierte
> en la pregunta de la tercera.**

## 6. LO QUE MIDO DEL ESTADO, Y LO QUE NO MIDO

| | |
|---|---|
| rama y commit | `extraccion-mundo-11`, `bc42b1c` |
| grafo | **324** nodos, **134** aristas dirigidas |
| bitacora | **507** veredictos: `SANO` **343**, `CONTINUA` **154**, `CORREGIDO` **10** |
| bandeja del lote 4 | **21** en `cuarentena/scott_radical_candor/`, **121** en `_insertados/` |
| poblacion del barrido | **348** = **324** del grafo mas **24** de bandejas, **347** contra cada candidato |
| guardas | gate **VERDE**, guiones **VERDE**, suite **ROJA** por `4.2` |
| vigencia (`D.15`) | **64** `RANCIO`, **8** `SIN HUELLA` |
| credito | **NO MEDIDO: su sede no esta en el arbol** (`4.1`) |

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl
        324 dataset/nodos.jsonl
        507 bitacora/VEREDICTOS.jsonl
    $ ls cuarentena/scott_radical_candor/*.json | wc -l
        21
    $ ls cuarentena/_insertados/scott_radical_candor/*.json | wc -l
        121
    $ git rev-parse HEAD
        bc42b1c8ecaeac46d24cd8173f7a1592f0b9cbf0

**LO QUE NO MIDO EN ESTA FASE Y POR ESO NO PUBLICO:** la cola de aristas recontada, la fila de
`PASOS INVENTADOS` firmada y el credito de la tanda. **Los tres necesitan el reporte delante o
la sede que `4.1` dice que falta**, y `D.38.3` no me deja publicar una cifra sin su
instrumento. **Van en mi turno normal.**

## 7. LO QUE LLEVO AL TURNO NORMAL, EN UNA LISTA Y SIN ARGUMENTO REABIERTO

1. Mis **`20`** clases contra las suyas, y mis **cuatro discutibles** (`3.3` y `3.4`).
2. La segunda madre `D.37` de `cap_09` para los tres, y la arista que
   `elegir_pregunta_recurrente_pedir_critica` **ya deberia tener** si esa lectura se sostiene.
3. `docs/loop/CREDITO_serial.jsonl` fuera del arbol, sin declarar por el arnes, **con tres
   pruebas de aceptacion colgando de el** (`4.1`, `4.2`).
4. La `TAREA 1.A` y su comando que se mueve a si mismo (`4.3`).
5. Los `58` pasos releidos y firmados por mi, `0` `PUENTE`, **con el denominador de `cap_13`
   dicho y sin firmar** (`212`, de los que no he releido `154`).

---

**Escrito en la fase ciega, sin `REPORTE.md` delante y sin recuperarlo. No commiteo: el arnes
sella este fichero.**
