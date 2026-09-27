
---

## 7. EL ESTADO DEL ARBOL, MEDIDO POR MI EN ESTA MISMA FASE

**Cuatro instrumentos de la casa, corridos por mi, con su salida pegada. Uno de ellos salio
ROJO por culpa mia y lo digo en el primer renglon, que es donde se dice.**

### 7.1. El gate: VERDE, y su cuenta cuadra con la del testigo del arnes

    $ python forja.py gate
      GATE VERDE.
        nodos verificados: 256
        guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada,
                 vuelta, cita_incompleta, deprecado_en_superficie, arista_rota,
                 arista_incompleta, guiones, censo_no_decrece

    $ (docs/loop/TESTIGO_GUARDAS.json, escrito por el arnes a las 12:37:12 sobre 97584af)
      "gate": { "estado": "VERDE", "salida": "GATE VERDE. nodos verificados: 243" }

**LECTURA:** `243` antes de la vuelta y `256` despues son **trece nodos**, que son
exactamente los trece ficheros que la vuelta movio a `_insertados` (`0.3`, primer comando).
**Las dos cuentas y el conteo de renombrados dicen trece por tres caminos distintos.**

### 7.2. El barrido de guiones: **SALIO EN ROJO Y LOS 27 HALLAZGOS ERAN MIOS**

    $ python forja.py guiones
      BARRIDO DE GUIONES EN ROJO: 27 hallazgo(s)
        .v30a/pob_cuidarse_agotamiento_centro_rueda.jsonl linea 327 columna 1687: guion largo (U+2014)
        ... (27 en total)
    $ (de que fichero es cada hallazgo)
           9   .v30a/pob_cuidarse_agotamiento_centro_rueda.jsonl
           9   .v30a/pob_sin.jsonl
           9   .v30a/poblacion.jsonl

**LECTURA, Y ES LA CAIDA QUE `D.45` NACIO PARA CAZAR:** los veintisiete estan en **ficheros
de trabajo mios**, creados en esta fase por la receta de la seccion 2. Los guiones largos los
traen los nodos de `ensayo_referencia_163`, que la receta mete en la poblacion. **Ni uno solo
esta en el arbol de la casa.** Retire los tres ficheros, que ya no me hacian falta al corregir
la receta, y volvi a medir:

    $ rm -f .v30a/poblacion.jsonl .v30a/pob_sin.jsonl .v30a/pob_cuidarse_agotamiento_centro_rueda.jsonl
    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

**LO DIGO ENTERO Y NO SOLO EL VERDE:** la vuelta 28 me costo un escalon por publicar
`guardas en rojo: 2` cuando eran `3` **y la tercera era mia**. Hoy fue `1` en rojo, la mia,
y **no la descubro al cerrar: la descubro midiendo, la nombro, la quito y vuelvo a medir.**

### 7.3. La vigencia (`D.15`): 26 RANCIO y 8 SIN HUELLA, y las ocho tienen una forma

    $ python forja.py rancios
      BLOQUE DE VIGENCIA: 34 hallazgo(s) sobre 361 veredicto(s) y 0 cita(s).
        RANCIO 26, SIN HUELLA 8
        lineas declaradas NO CONSUMADAS y por eso no medidas: 14

    $ wc -l bitacora/VEREDICTOS.jsonl
      375 bitacora/VEREDICTOS.jsonl

**LECTURA 1:** `361` mas `14` es `375`, asi que el bloque de vigencia **mide toda la bitacora
y no una parte**.

    $ (los vecinos que nombran las 8 lineas SIN HUELLA)
      2 compartir_logica_mostrar_razonamiento
      1 crear_obligacion_disentir_equipo
      1 fijar_fecha_cierre_debate_equipo
      1 mantener_manos_trabajo_real_equipo
      1 minimizar_impuesto_colaboracion_equipo
      1 parar_debate_emocion_agotamiento
      1 proteger_tiempo_equipo_jefe
    $ (cruce contra los trece de la vuelta)
      lineas SIN HUELLA     : 8
      nombran uno de los 13 : 7
      nombran otro          : ['crear_obligacion_disentir_equipo']

> **LECTURA 2, y es de mecanismo:** las ocho lineas `SIN HUELLA` **nombran, sin excepcion, a
> un nodo que hoy vive en el grafo y que el dia en que se escribio el veredicto estaba en la
> BANDEJA.** Siete de los ocho entraron en esta misma vuelta; el octavo,
> `crear_obligacion_disentir_equipo`, es el nodo que la vuelta 28 perdio y recupero.
> **`D.38.5` hizo que la aduana midiera contra la bandeja, que era lo que faltaba, pero la
> huella que guarda de un vecino de bandeja es la de un nodo VACIO**, asi que esos veredictos
> **no se pueden comprobar nunca contra el texto con el que se emitieron.** No es una caida
> de nadie de esta vuelta: **es el precio que `D.38.5` dejo sin pagar**, y sale a ocho lineas
> en una sola tanda.

### 7.4. **EL CENSO DE RUTAS (`D.42`) ESTA EN ROJO, Y CON EL EL SELLO DE ESTA PAGINA**

**Es la medida mas importante de esta apertura y por eso va con todo lo que hace falta para
reproducirla.** El testigo de `D.45` corre tres guardas antes de sellar, y la tercera es esta:

    $ grep -n "censo_rutas" scripts/testigo_guardas.py
      65:    ("censo_rutas", [sys.executable, os.path.join("scripts", "censar_rutas.py")]),

    $ python scripts/censar_rutas.py
      rutas publicadas y censadas : 96
        pasan                     : 94
        CAEN                      : 2

      CAE  docs/loop/ACTA_AUDITOR.md linea 2583, celda 1
           ruta : docs/loop/loop.log
           NO esta en el arbol, y la celda no lleva la marca 'VACIA A PROPOSITO: motivo'

      CAE  docs/loop/ACTA_AUDITOR.md linea 14622, celda 1
           ruta : docs/loop/ultimo_apertura.json
           esta y esta VACIA, y la celda no lleva la marca 'VACIA A PROPOSITO: motivo'

      CENSO EN ROJO: 2 ruta(s) publicadas como sede de una cifra no sostienen nada.
      EXIT=1

> **LECTURA, Y LA ESCRIBO SABIENDO QUE ME PERJUDICA:** las dos celdas que caen son **de mi
> propia acta**, y las dos caen **por lo que esta fase le hace al arbol**. `loop.log` no
> esta porque `D.34.2` lo retira para que yo lea a ciegas. `ultimo_apertura.json` esta a
> **cero bytes** porque el arnes lo vacia antes de invocarme. **Las dos rutas sostenian su
> cifra cuando se escribieron y las dos dejan de sostenerla mientras dura mi turno.**
>
> **LO QUE ESO SIGNIFICA PARA ESTA PAGINA, dicho por `D.45` y no por mi:** *si una guarda
> esta en rojo en el instante del sello, el sello no se acepta, y el arnes se detiene
> nombrandola.* **Asi que esta apertura, medida como esta el arbol ahora mismo, no se puede
> sellar.**
>
> **Y NO LO ARREGLO YO, y digo por que en vez de arreglarlo:**
>
> 1. **Regenerar el fichero** es la primera salida que el censo ofrece, y en mi caso seria
>    recuperar `loop.log`. **Eso es exactamente lo que el prompt me prohibe** y lo que
>    invalida mi apertura. La salida existe y no la puedo usar.
> 2. **Escribir `VACIA A PROPOSITO` en la celda** seria escribir en una sede duradera una
>    frase **que es cierta durante hora y media y falsa el resto del tiempo**: los dos
>    ficheros vuelven en cuanto mi turno acaba. **Eso es una cifra publicada falsa a plazo**,
>    y la pondria yo con mi mano en mi propia acta.
> 3. **Es la misma averia que el arnes ya se arreglo un piso mas arriba**, y esta medido:
>
>        $ git log --format="%h %ad %s" --date=format:"%H:%M" -1 97584af
>          97584af 11:29 ARNES: el tallado reventaba en la fase ciega y habria dejado al
>                        arnes sin poder sellar
>
>    `tallar_reporte.py` aprendio a decir `TALLADO SIN OBJETO: docs/loop/REPORTE.md no esta
>    en el arbol. La fase ciega lo retira A PROPOSITO (D.34.2)`. **`censar_rutas.py` no lo
>    aprendio.** Y `AUDITOR_FORJA.md` es explicito en que esto **es tarea del arnes y no
>    remedio mio**: *un remedio sobre formato de artefactos no existe como remedio.*
>
> **LO DEJO MEDIDO, NOMBRADO Y CON SU CAUSA, que es lo unico que esta fase me deja hacer.**

### 7.5. La prueba de aceptacion: **192 pruebas, 4 fallos**, y los cuatro son de esta fase

    $ python tests/test_aceptacion.py
      total: 192 pruebas, 4 fallos, 0 errores
      FAIL: test_caso_positivo_una_ruta_de_CERO_BYTES_es_caida_de_cifra (PruebaTallado)
      FAIL: test_el_estricto_tumba_lo_que_el_hook_deja_pasar (PruebaTallado)
      FAIL: test_el_informe_nombra_la_fila_y_manda_regenerar (PruebaTallado)
      FAIL: test_e_guion_largo_rompe_el_hook (PruebaE)

    $ (el motivo que imprimen los tres primeros, literal)
      AssertionError: 'TALLADO EN ROJO' not found in 'TALLADO SIN OBJETO:
      docs/loop/REPORTE.md no esta en el arbol. La fase ciega lo retira A PROPOSITO (D.34.2)'

    $ (el motivo del cuarto, literal)
      AssertionError: 1 != 0 : el repo ha de estar limpio antes de ensuciarlo
      [pre-commit] COMMIT ABORTADO: ... una ruta publicada como sede de una cifra no sostiene nada

> **LECTURA:** los tres primeros fallan **porque el arreglo de las `11:29` funciono**: el
> tallado ya no revienta, devuelve `SIN OBJETO`, **y sus tres pruebas siguen esperando el
> `ROJO` de antes.** El arreglo entro sin que sus pruebas aprendieran la fase nueva, asi que
> **la suite de aceptacion queda en rojo durante TODAS las fases ciegas a partir de hoy.**
> El cuarto no es una prueba distinta: es la misma piedra de `7.4` vista desde el hook.
>
> **NINGUNO DE LOS CUATRO TOCA UN NODO, UN VEREDICTO NI UNA CIFRA DEL GRAFO.** Lo digo
> entero para que nadie lea *cuatro fallos* y piense que la tanda esta rota: **la tanda pasa
> el gate con sus 256 nodos y sus trece guardas.**

### 7.6. Lo que mire de la bitacora sin destapar una sola razon

    $ (cuenta sobre bitacora/VEREDICTOS.jsonl, campos 'veredicto' y longitud de 'razon')
      veredictos antes de la vuelta 30 : 289
      veredictos ahora                 : 375
      escritos por la vuelta 30        : 86
      por veredicto                    : SANO 80, CONTINUA 6
      con arista                       : 6
      candidatos distintos             : 13
      SIN razon escrita (D.8)          : 0
      largo minimo de razon            : 125 caracteres

**LECTURA:** `D.8` dice que un `SANO` sin razon escrita es una caida **aunque acierte, y que
se ve en la bitacora sin releer nada**. **Las 86 lineas traen razon, y la mas corta tiene 125
caracteres.** De esa cuenta sale tambien el tamaño de mi muestra pineada para el acta:
`80` SANO, el veinte por ciento, **16 relecturas**, por debajo del techo de veinte que fija
la seccion 7 del protocolo.
