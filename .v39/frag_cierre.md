
### CC.6.g. **EL SALDO DE LA INSERCION, TALLADO DE LOS TRES INFORMES DE LA ADUANA**

<!-- TALLADO: script=.v39/tabla_insercion.py salida=.v39/tabla_insercion.txt -->

| # | candidato | linea | vecinos | declarados | aristas cableadas | en cola | nodos al salir | codigo |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | `pedir_critica_primero_crear_seguridad_psicologica` | `L73` | 1 | 7 | 2 | 5 | 322 | **VERDE** |
| 2 | `elegir_pregunta_recurrente_pedir_critica` | `L115` | 0 | 5 | 1 | 0 | 323 | **VERDE** |
| 3 | `resolver_dudas_frecuentes_pedir_critica` | `L167` | 2 | 2 | 0 | 0 | 324 | **VERDE** |

**EL RELOJ DE CADA CADENA, LEIDO DE SU PROPIO REGISTRO** y no estimado, porque es la cifra con la que
la vuelta siguiente dimensionara su tramo:

    $ grep -E "INICIO|FIN" .v39/informes/_cadena[123]_log.txt
    INICIO 04:24:16  FIN 04:45:16    cadena 1, candidato 1 mas sus dos aristas: 1.260 s
    INICIO 04:45:24  FIN 04:59:45    cadena 2, candidato 2                    :   861 s
    INICIO 04:59:52  FIN 05:09:18    cadena 3, candidato 3                    :   566 s

**`2.687` segundos de insercion para tres candidatos, `896` de media**, mas los `1.187` de la aduana en
seco del `1`. **El encargo dimensiono el tramo con `483` segundos por candidato y la media real es
`896`**, casi el doble; con la aduana en seco delante, **el candidato `1` costo `2.447` segundos el
solo**. **Y el coste NO es parejo:** baja de `1.260` a `566` segun cuantos veredictos declara cada uno,
asi que **lo que predice el reloj no es el numero de candidatos, es el numero de vecinos que hay que
juzgar.**

## CC.7. EL CIERRE DE LA VUELTA 39

### CC.7.a. **LAS TRES GUARDAS, EN VERDE Y CON SU SALIDA PEGADA**

<!-- TALLADO: parcial salida=.v39/guardas_cierre.txt -->

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 324
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python tests/test_aceptacion.py
      total: 294 pruebas, 0 fallos, 0 errores

**LA TERCERA ES LA `TAREA 1.A` Y ERA CONDICION DE CIERRE**: la vuelta abrio con `2` fallos y cierra con
`0`, y la reparacion esta comprobada por mutacion en `CC.2.a`.

### CC.7.b. **LAS CIFRAS DEL CIERRE, RECOMPUTADAS AL CIERRE** (`EXTRACTOR.md` 4)

*Ninguna se copia de `CC.0`: las que esta vuelta pudo mover se vuelven a medir del dato.*

<!-- TALLADO: script=.v39/cierre.py salida=.v39/cierre_tabla.txt -->

| pieza | al abrir | al cerrar | movimiento | de donde sale |
|---|---:|---:|---:|---|
| rama | extraccion-mundo-11 | extraccion-mundo-11 | . | `git rev-parse --abbrev-ref HEAD` |
| commit al cerrar | `1d6b07b` | `1d6b07b` | . | `git rev-parse --short HEAD` |
| nodos en `dataset/nodos.jsonl` | 321 | **324** | +3 | `dataset/nodos.jsonl` |
| veredictos en `bitacora/VEREDICTOS.jsonl` | 486 | **506** | +20 | `bitacora/VEREDICTOS.jsonl` |
| de ellos, con anotacion `no_consumada: true` | 14 | **14** | 0 | `bitacora/VEREDICTOS.jsonl` |
| aristas por `nodos_siguientes` | 129 | **134** | +5 | `dataset/nodos.jsonl` |
| aristas por `nodos_previos` | 129 | **134** | +5 | `dataset/nodos.jsonl` |
| candidatos en bandeja, lote 4 | 24 | **21** | -3 | PATRON: `cuarentena/scott_radical_candor/*.json` |
| insertados y archivados, lote 4 | 118 | **121** | +3 | PATRON: `cuarentena/_insertados/scott_radical_candor/*.json` |
| candidatos en bandeja, lote 5 | 3 | **3** | 0 | PATRON: `cuarentena/marquet_turn_the_ship/*.json` |
| lote 4 insertado sobre `142`, por ciento | 83,1 | **85,2** | +2,1 | `cuarentena/_insertados/scott_radical_candor/` |

**LOS `+20` VEREDICTOS, DESGLOSADOS, porque `3` nodos no explican `20`:** `1` de la correccion declarada
de la `TAREA 1.B`, `8` del candidato `1`, `2` de sus dos aristas por `forja.py arista`, `5` del
candidato `2` y `4` del candidato `3`. **`1 + 8 + 2 + 5 + 4 = 20`.**

**LOS `+5` DE ARISTA, UNA A UNA:** `empezar_cultura_franqueza_radical > pedir_critica_primero`,
`desplegar_plan... > pedir_critica_primero` (`P03`, la que la `ACTA 36` `3.6` dejo encargada),
`pedir_critica_primero > criticar_trabajo_evitar_desanimo` (la `50`),
`pedir_critica_primero > fomentar_guia_reciproca_companieros` (la `52`) y
`pedir_critica_primero > elegir_pregunta_recurrente_pedir_critica` (la `D.37`).

### CC.7.c. **LA COLA DE ARISTAS, RECONTADA ENTERA AL CIERRE. SIGUE SALIENDO `0`**

<!-- TALLADO: parcial salida=.v39/cola_cierre.txt -->

    LA COLA DE ARISTAS ENTERA, de bitacora/VEREDICTOS.jsonl
      lineas con arista_en_cola: true            : 16
      de ellas, YA CABLEADAS en el grafo         : 11
      esperan a un extremo que no ha entrado     : 5
      con LOS DOS extremos dentro y SIN cable    : 0   <-- tiene que salir 0
    

**La cifra que el encargo pide que salga `0` sale `0`**, y es la tercera cosa que no se negociaba. **La
cola sube de `11` a `16` y eso es trabajo hecho, no deuda nueva:** las `5` que aniado son aristas que
**antes no existian en ningun sitio**, y ahora estan escritas con su razon en `bitacora/VEREDICTOS.jsonl`
esperando a que su hijo entre. **`0` con los dos extremos dentro y sin cable** es lo que dice que ninguna
de las `16` esta rota.

### CC.7.d. **LA FILA DE `PASOS INVENTADOS`, CON SU DENOMINADOR DICHO** (cierre, punto 4)

<!-- TALLADO: parcial salida=.v39/denominador.txt -->

      --------------------------------------------------------------------------------------------
      candidatos de cap_13          : 12   (6 en bandeja, 6 insertados)
      pasos de cap_13, todos        : 212
      candidatos de MI TRAMO        : 3
      pasos de MI TRAMO             : 56

| la fila | `PUENTE` | pasos | por ciento | techo |
|---|---:|---:|---:|---:|
| **MI TRAMO** (`3` candidatos de `cap_13`) | **`0`** | **`56`** | **`0,00`** | `10` |
| `cap_13` entero, **que NO firmo** | `4` | `212` | `1,89` | `10` |

**LA DE ABAJO NO ES MIA Y POR ESO VA EN CURSIVA DE ADVERTENCIA:** los `4` son los que la `ACTA 37`
re firmo (`contar_cuatro` `P08`, `dar_elogio` `P13`, `pedir_critica_primero` `P06` y `P15`), y **sigue
siendo un SUELO**, porque de los `212` pasos del capitulo **yo he releido `56`** y los otros `156`
los ha releido quien los escribio o nadie. **Publicarla como la fila del capitulo seria exactamente la
holgura que la `ACTA 37` me corrigio**, asi que la publico con las dos cifras separadas.

### CC.7.e. **LO QUE ESTA VUELTA DEJA ABIERTO, DICHO EN UNA TABLA Y NO ESCONDIDO**

| | |
|---|---|
| **`cap_13` queda con `6` en bandeja** | `abrazar_incomodidad`, `escuchar_entender`, `premiar_franqueza`, `dar_elogio`, `medir_critica` e `integrar_peticion`. **Cinco de los seis tienen ya su arista escrita y en cola**, y se cablea sola en el acto en que entren |
| **la cola de doctrina sigue en `10` y `0` bloquean** | no subo ninguna y no adjudico ninguna. **La figura de mi `DISCUTIBLE 7` es la tercera aparicion de la pregunta `3`** y la registro ahi en vez de duplicarla |
| **el coste del instrumento** | medido y publicado en `CC.6.e` y `CC.6.g`: `1.187` s la aduana en seco de uno, `896` s de media la insercion. **No propongo cambiar nada: propongo que la cifra este escrita**, porque el tramo se dimensiono con `483` |
| **lo que NO reparo y digo por que** | la prueba que clavaria un minimo en la cola de doctrina (`DISCUTIBLE 2`). **Seria guarda nueva y `7.F` la veda** |

### CC.7.f. **EL TURNO CIERRA SIN NINGUNA CADENA VIVA** (`TAREA 4`)

*La vuelta 38 cerro su turno a las `02:27` con `cadena 2` viva y un nodo entro al grafo a las `02:34:42`,
dentro de la fase ciega del auditor. **La tercera vez se mira de otra manera**, dice el encargo, asi que
lo compruebo en vez de prometerlo:*

    $ tail -2 .v39/informes/_cadena.txt
    OK resolver_dudas_frecuentes_pedir_critica  (324 nodos, bandeja 21)
    cadena 3 terminada

**Las tres cadenas escribieron su linea `terminada` ANTES de que yo empezara a tallar este cierre**, y
**no arranque una cuarta**: los tres candidatos del tramo eran tres y no hay un `4` que arrancar. **El
grafo queda quieto en `324` desde las `05:09:18`.**
