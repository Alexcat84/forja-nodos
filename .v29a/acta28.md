
---

# ACTA 28. VUELTA 28, lote 4 (`scott_radical_candor`) INSERTANDO `cap_07` mas la cabeza de `cap_11`: la vuelta del extractor sale **limpia de `REPORTE` por primera vez desde la vuelta 25**, sus **diez cifras de apertura y cierre me salen al digito**, sus **quince veredictos los releo y los quince se sostienen**, y **adjudico los siete discutibles, las tres propuestas y los once `POR ADJUDICAR` de mi propia apertura**. Y aun asi: **su caida de dato movio el dataset con el gate en VERDE y la cargo como `CLASE`**, y **mi apertura sellada publica `guardas en rojo: 2` cuando eran `3` y la tercera era mia. MI RACHA PROPIA LLEGA A `3 de 3` Y EL BUCLE SE DETIENE**

| | |
|---|---|
| fecha del acta | **2026-09-16**, leida del instrumento (`date` da `Wed, Sep 16, 2026 11:01:03 AM`; `src.aduana._hoy()` da `2026-09-16`) |
| vueltas que cubre esta acta | **la vuelta 28, y solo ella.** Medido en la seccion 0, no supuesto |
| rama | `extraccion-mundo-11` (`git rev-parse --abbrev-ref HEAD`) |
| hash auditado | **`dd79e01`**, `HEAD` al abrir mi turno. El cierre tallado del extractor declara `5802702` y su apertura `ff30fba` |
| sello de mi apertura ciega | **`2f326b1b60e28a42ed21a96ce2bf967d9d20208b`**, **intacto**: `git hash-object docs/loop/APERTURA_CIEGA.md` lo devuelve hoy, y es el que `SELLOS_APERTURA.jsonl` anoto a las `10:41:02` |
| arbol de trabajo | **ninguna sede de dato modificada por mi turno**: `git status --short dataset/ bitacora/ config/ esquema/ src/ scripts/ cuarentena/ fuentes/ tests/ hooks/` sale **VACIO** despues de mis dos mutaciones, que restaure |
| veredicto general | **REPORTE VERIFICADO AL DIGITO EN LAS DIEZ CIFRAS QUE PUBLICA.** Cero `REPORTE`, cero `CIFRA PUBLICADA`, **una `CLASE`: la caida de dato de `V.5.e`** |
| paradas del extractor | **CERO declaradas**, y lo compruebo: es la primera vuelta sin ninguna desde la 25 |
| **parada mia** | **SI. `CREDITO ROTO` por mi propia racha**, seccion 9. `PARA_ALEXIS.md` escrito y `PROMPT_SIGUIENTE.md` vacio |

---

## 0. HUECO DE ACTA: MEDIDO, Y NO LO HAY

*Va antes que nada porque el protocolo lo pone antes que nada (`AUDITOR_FORJA.md` 1.0).*

    $ grep -n "^# ACTA " docs/loop/ACTA_AUDITOR.md | tail -1
      24413:# ACTA 27. VUELTA 27, lote 4 (scott_radical_candor) INSERTANDO cap_07 ...

    $ git log --oneline -1
      dd79e01 VUELTA 28 CIERRE: cierre verde con la vigencia publicando su cuenta sin tumbarlo ...

**La ultima acta escrita es la `ACTA 27` y cubre la vuelta 27. La vuelta que audito es la 28.** La
vuelta inmediatamente anterior a la 28 es la 27, **y esta cubierta**. No hay hueco, **y esta acta
cubre una sola vuelta y lo dice.**

### 0.1. LA HERENCIA, Y LA HUELLA CUADRA AL CARACTER

    $ git hash-object docs/loop/ACTA_AUDITOR.md      (hoy, antes de aniadir esta acta)
      1f7f256d3dce8bb70708b83f303f8d75953dfa0c

**Es exactamente la huella que mi apertura sellada declara haber leido** (`APERTURA_CIEGA.md` `0`,
bloque `ACTA ANTERIOR LEIDA`). **`HEREDADO 1: CUMPLIDO`**, y su comprobacion la rehago yo en `6.1`
con la cronologia de `git` delante, que es lo que mi fase ciega no tenia.

---

## 1. LO QUE VERIFIQUE, CON MIS PROPIOS COMANDOS

**El estado de verdad es el repo.** Todo lo que sigue se corrio EN ESTA VUELTA y ninguna cifra se
copio del reporte. Salidas en `.v29a/`.

### 1.1. LAS SEIS GUARDAS Y LOS DOS CENSOS, CORRIDOS POR MI

<!-- TALLADO: parcial salida=.v29a/gate.txt -->

    $ python forja.py gate
      GATE VERDE.
        nodos verificados: 243
        guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada,
                 vuelta, cita_incompleta, deprecado_en_superficie, arista_rota,
                 arista_incompleta, guiones

    $ python forja.py resolutor
      nodos vivos: 243
      nodos deprecados (archivo): 0
      alias registrados: 0

    $ python tests/test_aceptacion.py
      total: 176 pruebas, 0 fallos, 0 errores

    $ python scripts/censar_rutas.py
      rutas publicadas y censadas : 434
        pasan                     : 434
        CAEN                      : 0

    $ python scripts/tallar_reporte.py
      TALLADO VERDE: las 42 tabla(s) comprobables son las de su instrumento, celda a celda.

| instrumento | **lo que su salida dice** | contra el reporte |
|---|---|---|
| `gate` | **VERDE**, `243` nodos, `12` guardas | `V.9.a` dice `243`: **al digito** |
| `resolutor` | `243` vivos, `0` deprecados, `0` alias | `V.9.a` dice lo mismo: **al digito** |
| `test_aceptacion` | **`176` pruebas, `0` fallos, `0` errores** | `V.9.a` dice lo mismo: **al digito** |
| `censar_rutas` (`D.42`) | **VERDE**, `434` de `434`, `0` caen | no lo publica; **lo corro yo porque la cosecha `7.B` es mia de vigilar** |
| `tallar_reporte` (`D.41`) | **VERDE**, `42` tablas celda a celda | idem |
| `guiones` | **ROJO, `5` hallazgos, y los `5` son MIOS.** Seccion `8` | `V.9.a` dice VERDE, **y lo era cuando el extractor cerro** |

> **`LECTURA`, en linea aparte (`D.38.3` ensanchada): las seis salidas de arriba miden el repo
> DESPUES de que el arnes devolviera `REPORTE.md` al arbol.** Mi propia apertura sellada midio
> `test_aceptacion` en `1` fallo y `censar_rutas` en `4` caidas de `96`, **y las dos eran de la fase
> ciega y no de la vuelta 28**: con el fichero de vuelta, las dos salen verdes **sin tocar una linea
> de codigo**. Eso confirma el diagnostico de mi `1.1` ciega y es lo que adjudico en `6.2`.

**Y DECLARO UNA DISCREPANCIA EN VEZ DE RESOLVERLA COPIANDO** (`AUDITOR_FORJA.md` 1.1): el censo que
`docs/loop/loop.log` guarda dice `408` rutas y el mio de hoy dice `434`. **No es una discrepancia de
dato: aquel censo es el del cierre de la vuelta 27**, corrido a las `08:19` segun el propio log, **y
la vuelta 28 anexo su seccion al reporte entre medias**. Lo digo porque una cifra de log que no
cuadra con la de hoy hay que explicarla, no ignorarla.

### 1.2. MI PROPIO CONTEO DEL DATASET Y DE LA BITACORA

<!-- TALLADO: parcial salida=.v29a/cuentas.txt -->

    $ python (lector propio, .v29a/cuentas.txt)
      nodos en dataset/nodos.jsonl        : 243
      veredictos en bitacora/VEREDICTOS   : 289
      bandeja lote4 scott                 : 102
      insertados lote4 scott              : 40
      bandeja lote5 marquet               : 3
      ids unicos                          : 243
      clases de veredicto (todas)         : {'CONTINUA': 93, 'SANO': 192, 'CORREGIDO': 4}

### 1.3. LAS DIEZ CIFRAS DEL REPORTE: LAS CINCO DE APERTURA CONTRA `git`, LAS CINCO DE CIERRE CONTRA EL ARBOL

**Las de apertura NO las doy por buenas por venir en el encargo: las saco del arbol de `ff30fba`**,
que es el commit que el propio reporte declara como su apertura.

    $ git show ff30fba:dataset/nodos.jsonl | grep -c '"id"'                        239
    $ git show ff30fba:bitacora/VEREDICTOS.jsonl | grep -c ""                      264
    $ git ls-tree -r --name-only ff30fba cuarentena/scott_radical_candor/          106
    $ git ls-tree -r --name-only ff30fba cuarentena/_insertados/scott_radi...       36
    $ git ls-tree -r --name-only ff30fba cuarentena/marquet_turn_the_ship/           3

| cifra | el reporte dice | **mi comando de hoy** | |
|---|---:|---:|---|
| nodos al abrir (`V.0.b`) | 239 | **239** | **al digito** |
| veredictos al abrir | 264 | **264** | **al digito** |
| bandeja lote 4 al abrir | 106 | **106** | **al digito** |
| archivados lote 4 al abrir | 36 | **36** | **al digito** |
| bandeja lote 5 al abrir | 3 | **3** | **al digito** |
| nodos al cerrar (`V.9.b`) | 243 | **243** | **al digito** |
| veredictos al cerrar | 289 | **289** | **al digito** |
| bandeja lote 4 al cerrar | 102 | **102** | **al digito** |
| archivados lote 4 al cerrar | 40 | **40** | **al digito** |
| bandeja lote 5 al cerrar | 3 | **3** | **al digito** |

**Y LA ARITMETICA QUE `V.9.b` PUBLICA, RECONTADA A MANO:** `239 + 4 = 243`; `106 - 4 = 102`;
`36 + 4 = 40`; **`264 + 15 + 10 = 289`**. Las cuatro cuadran. **Los `4` que salen de la bandeja
incluyen la madre de `cap_11`**, que es del mismo lote 4, y por eso `106 - 4` y no `106 - 3`.

### 1.4. EL REPARTO DE LOS `25` VEREDICTOS NUEVOS, RECONTADO LINEA A LINEA Y NO ACEPTADO

<!-- TALLADO: parcial salida=.v29a/nuevos.txt -->

| lineas | candidato | cuantas | `consumada` | el reporte dice |
|---|---|---:|---|---|
| `265` | `recorrer_rueda_conscientemente_cultura_equipo` | **1** | sin campo | `V.5.g` fila 1: **1** |
| `266` a `268` | `recorrer_rueda_hacer_cosas_equipo` | **3** | sin campo | `V.5.g` fila 2: **3** |
| `269` a `278` | `crear_obligacion_disentir_equipo` (la corrida deshecha) | **10** | **`false`** | `V.5.e`: **10** |
| `279` | `crear_espacio_seguro_madurar_ideas_nuevas` | **1** | sin campo | `V.5.g` fila 3: **1** |
| `280` a `289` | `crear_obligacion_disentir_equipo` (la buena) | **10** | sin campo | `V.5.g` fila 4: **10** |
| | **consumados** | **15** | | **15** |
| | **no consumados** | **10** | | **10** |

**`D.8`, medido sobre TODA la bitacora y no solo sobre el tramo nuevo:** `0` lineas sin razon escrita
en las `289`. **Ningun `SANO` entro por cansancio, ni hoy ni en ninguna de las veintiocho vueltas.**

### 1.5. LA VIGENCIA, RECONTADA CON EL INSTRUMENTO Y CRUZADA CONTRA LA BITACORA

<!-- TALLADO: parcial salida=.v29a/rancios.txt -->

    $ python forja.py rancios
      BLOQUE DE VIGENCIA: 34 hallazgo(s) sobre 275 veredicto(s) y 0 cita(s).
        RANCIO 26, SIN HUELLA 8
        lineas declaradas NO CONSUMADAS y por eso no medidas: 14

| lo que verifico | **mi medida** | el reporte |
|---|---|---|
| hallazgos totales | **34** | `V.9.c`: **34** |
| `RANCIO` | **26** | **26** |
| `SIN HUELLA` | **8**, en las lineas `252, 256, 258, 260, 261, 262, 263, 264` | `V.4.c` nombra **esas ocho** |
| `NODO IDO` | **la especie no aparece: `0`** | `V.9.c`: de `16` a **`0`** |
| no consumadas | **14**: lineas `248` a `251` y `269` a `278` | **14**, `4` mas `10` |
| veredictos medidos | **275** | `289 - 14 = 275`: **al digito** |
| de cuantos nodos salen los `26` `RANCIO` | **`4`**, y los nombro: `delimitar_franqueza_radical_cinco_noes`, `repartir_semana_cuarenta_horas_jefe`, `despedir_persona_franqueza_radical`, `reconocer_recompensar_gente_estable` | `V.4.b`: **los mismos cuatro** |
| los `26` llevan `VIGENCIA DECLARADA` dentro de su razon | **`26` de `26`**, comprobado linea a linea | `V.4.b`: **`26` de `26`** |
| la huella de un nodo vacio | **`e3b0c44298fc1c14`**, sacada llamando yo a `src.comun.huella_de_nodo({})` | `V.4.c` publica **la misma** |
| la linea `256` conserva su clase | **`SANO`**, con `CORRECCION DECLARADA` dentro de la razon | `V.3.e`: **`SANO` (NO se toca)** |

### 1.6. LAS DOS ARISTAS, COMPROBADAS EN LOS DOS EXTREMOS Y NO EN LA PROSA

    $ (lector propio sobre dataset/nodos.jsonl)
      recorrer_rueda_conscientemente_cultura_equipo | previos: [] | siguientes: ['recorrer_rueda_hacer_cosas_equipo']
      recorrer_rueda_hacer_cosas_equipo | previos: ['recorrer_rueda_conscientemente_cultura_equipo'] | siguientes: []

**LA ARISTA QUE LLEVABA DOS VUELTAS ABIERTA ESTA CABLEADA POR LOS DOS EXTREMOS.** Y la segunda,
`crear_espacio_seguro_madurar_ideas_nuevas > nutrir_ideas_nuevas_reunion_solas`, **queda EN COLA con
motivo comprobado**: `nutrir_ideas_nuevas_reunion_solas` sigue en `cuarentena/scott_radical_candor/`
y no en el grafo, **que es exactamente la condicion que `D.29` pone para diferir el cableado.**

**Y EL ORDEN DEL LIBRO, RESTAURADO, MEDIDO POR INDICE DEL DATASET Y NO POR SU PALABRA:**

    240 recorrer_rueda_conscientemente_cultura_equipo
    241 recorrer_rueda_hacer_cosas_equipo
    242 crear_espacio_seguro_madurar_ideas_nuevas      (L177)
    243 crear_obligacion_disentir_equipo               (L231)

**`L177` antes que `L231`**, que es lo que `V.5.e` punto 3 promete y lo unico que prueba que la
reinsercion en serie no dejo el capitulo peor de lo que lo encontro.

### 1.7. **LA GUARDA QUE NO MUERDE ES CIFRA** (cosecha 7.C): MUTE LAS DOS Y LAS DOS MUERDEN

*El reporte declara dos bloques de guardas mordiendo. **Los muto cambiando el CODIGO bajo prueba, no
el valor esperado**, que es la version dura de la regla. Copia de seguridad antes, restauracion y
`git status` despues.*

**MUTACION 1, la atomicidad de `V.3.b`:** devuelvo `comun.agregar_jsonl` DENTRO del bucle por vecino,
que es literalmente el fallo que la `ACTA 27` `5.2` encontro.

    $ python -m unittest tests.test_aceptacion.PruebaInsercionAtomica
      FAIL: test_caso_positivo_una_corrida_RECHAZADA_no_deja_ni_una_linea
      FAIL: test_el_gate_que_muerde_en_la_simulacion_tampoco_deja_linea
      FAIL: test_caso_negativo_una_corrida_QUE_ENTRA_si_escribe_sus_veredictos
      FAIL: test_caso_positivo_CONTINUA_con_el_otro_extremo_EN_BANDEJA_se_escribe
      FAIL: test_un_REPITE_si_se_consuma_porque_no_imprime_rechazado
      Ran 10 tests ... FAILED (failures=5)

**MUTACION 2, la vigencia de `V.4.a`:** devuelvo `("vigencia de los veredictos", ...)` a la lista de
`pasos` de `scripts/cerrar_reporte.py`, que es la linea `61` que la `ACTA 27` `5.3.a` adjudico.

    $ python -m unittest tests.test_aceptacion.PruebaVigenciaNoEsGuarda
      FAIL: test_el_cierre_NO_se_pone_en_rojo_por_ella_Y_SIGUE_publicando_su_cuenta
        AssertionError: 'vigencia' unexpectedly found in
        'CIERRE EN ROJO. No pasa: gate de integridad, prueba de aceptacion, vigencia de los veredictos'
      Ran 3 tests ... FAILED (failures=1)

    $ (restauradas las dos) git status --short src/ scripts/
      (vacio)
    $ las dos suites vuelven a OK

> **LAS DOS MUERDEN Y LO PRUEBO SOBRE EL CODIGO.** Es la primera vez en esta casa que la mutacion
> toca `src/aduana.py`. Lo que mas me importa es la primera: **caen cinco pruebas a la vez**, lo que
> dice que la atomicidad no cuelga de una sola asercion fragil.

### 1.8. LAS RUTAS QUE PROMETEN PRUEBA (cosecha 7.B), CENSADAS POR MI

`censar_rutas.py` lee `REPORTE.md` y `ACTA_AUDITOR.md`, **que es donde vive todo lo que el extractor
publica como sede**: **`434` rutas, `434` pasan, `0` caen, `0` de cero bytes.** Las rutas `.v28e/` de
la vuelta 28 estan dentro de esa cuenta y ninguna promete mas de lo que guarda.

---

## 2. LA RELECTURA, EMPEZANDO POR LOS DISCUTIBLES MARCADOS (`AUDITOR_FORJA.md` 1.2)

### 2.0. **ESTA VUELTA NO MARCA NI UN DISCUTIBLE DE CLASE, Y ESO CAMBIA POR DONDE EMPIEZO**

Los `7` discutibles de `V.7` son **de metodo y de alcance de regla**, ninguno es un par. Lo digo
porque `5.1` manda empezar por los marcados y `6.4` avisa de lo contrario: **una discrepancia en un
tramo sin discutibles de clase no rompe el credito, porque la comparacion que la regla supone no
existe ahi.** Asi que los adjudico primero **como discutibles que son**, y la relectura de clase la
llevo entera a la seccion `3`, **donde releo los `15` y no una muestra.**

### 2.1. **`DISCUTIBLE 1`: aplicar `2.b` tambien al veredicto DECLARADO POR LECTURA. SOSTENIDO**

**Lo que dice:** el encargo nombra el caso del vecino levantado por señal; el extractor lo aplica
tambien al declarado por lectura.

**Mi adjudicacion: SOSTENIDO, y lo adjudico citando y no ensanchando.** `D.29` dice *una arista se
cablea contra ids que ya viven, y en cuarentena todavia no vive ninguno*. **Esa frase no distingue
como se levanto el par**: distingue donde vive el extremo. La salida vieja (*entra la madre primero*)
**no existe cuando los dos extremos esperan**, y esa es exactamente la configuracion que la `ACTA 27`
`5.1` adjudico como cubierta por `D.29`. Dejar una de las dos puertas con la regla vieja seria **la
media regla cableada**, que es la averia que `9ef933b` y esta misma vuelta vinieron a cerrar.

**Y COMPRUEBO QUE NO ENSANCHA MAS DE LO QUE DICE:** `test_un_id_que_no_esta_NI_EN_EL_GRAFO_NI_EN_BANDEJA_se_sigue_rechazando`
sigue en verde en mi corrida de `1.1`. **Un id que no vive en ninguna poblacion sigue cayendo.**

### 2.2. **`DISCUTIBLE 2`: `SIN HUELLA` en vez de `NODO IDO` para la huella de un nodo vacio. SOSTENIDO**

**Mi adjudicacion: SOSTENIDO, y la cita es literal.** `D.15` tiene la casilla escrita: *SIN HUELLA:
incomprobable, y eso se declara en vez de darse por bueno.* **No mueve la vara de `D.15`**, y lo
mido: **los `26` `RANCIO` siguen siendo `26`** antes y despues (`1.5`), y **las `8` siguen saliendo
impresas y contadas**. Lo que cambio es el nombre, **y el nombre viejo era falso**: `NODO IDO` decia
*el nodo se fue* de ocho nodos que estan en la bandeja.

**LO QUE NO ES SOSTENIBLE ES DARLAS POR BUENAS, y no lo hace:** las ocho siguen en la cola.

### 2.3. **`DISCUTIBLE 3`: NO correr `forja.py arista --paso 4`. SOSTENIDO**

**Mi adjudicacion: SOSTENIDO.** `D.29` manda *LA ARISTA SE DECLARA EN EL ACTO DE LA INSERCION, con su
veredicto, y la madre entra primero*, y eso es lo que paso. **La cabecera de `forja.py arista` dice
para que existe**: *para dos nodos que YA viven en el grafo no habia camino*. Aqui lo habia.

**Y LA CITA DEL PASO NO SE PERDIO, que es lo unico que el encargo protegia:** esta dentro de la razon
de las lineas `265` y `267`, que lei en `3.3`, **y el paso `4` de la madre lo comprobe yo contra el
libro** (`L281` de `cap_11`, `1.6` y `6.7`).

### 2.4. **`DISCUTIBLE 4`: la declaracion de los `26` va DENTRO de la linea de la bitacora. SOSTENIDO, y ademas es la lectura buena**

**Mi adjudicacion: SOSTENIDO.** El encargo decia *sede duradera, no el reporte*, y no decia cual. **La
linea del veredicto es donde el siguiente lector va a mirar**, y lo pruebo con el propio instrumento:
`forja.py rancios` imprime las `26` y quien las lea encuentra la declaracion **en la misma linea**,
sin tener que saber que existe un documento aparte. **Un documento aparte se despega del dato que
declara**, que es la enfermedad de `D.35` y de la que salio `anotar`.

### 2.5. **`DISCUTIBLE 5`: `anotar` estrena la marca `VIGENCIA DECLARADA`. SOSTENIDO**

**Mi adjudicacion: SOSTENIDO.** `D.35` pide **una marca que diga al lector que ese tramo es
declarado**, y las dos empiezan por esa palabra. **Llamar `CORRECCION DECLARADA` a una declaracion
que no corrige nada seria una etiqueta falsa**, y la especie *etiqueta mal escrita* es justo la que
`5.2` separa de *veredicto mal puesto*. La marca nueva **no afloja ninguna guarda**: comprobe en
`1.5` que las `26` siguen saliendo `RANCIO` con ella dentro.

### 2.6. **`DISCUTIBLE 6`: cerrar la vuelta en `4` nodos de `16`. SOSTENIDO, Y LA REGLA LE OBLIGABA**

**Mi adjudicacion: SOSTENIDO, y lo que verifico es lo que `AUDITOR_FORJA.md` 8.1 me manda verificar:
que la vuelta DECLARO el cierre corto con su cifra.** Lo declaro con **dos**: `77` pares de cola y
`~4` minutos de aduana por candidato, las dos con su sede. **Una vuelta que cierra corta y no lo dice
es caida de `REPORTE`; esta lo dijo dos veces, en `V.5.g` y en `V.9.e`.**

**Y LA CIFRA DE LA COLA LA TENGO MEDIDA DOS VECES POR SEPARADO:** mi barrido ciego levanto `77` pares
sobre los `12` que esperan, **y la tabla del reporte suma `77` fila a fila** (`10+10+10+9+8+7+7+5+4+3+3+1`),
con `27` del grafo y `50` de bandeja que tambien suman. **Dos instrumentos distintos, la misma cifra.**

### 2.7. **`DISCUTIBLE 7`: no arreglar el hueco de `L153` y decir que no hay via. SOSTENIDO, Y LO COMPRUEBO YO**

**Mi adjudicacion: SOSTENIDO.** Reabri `L153` con mi lector y **los tres modos estan**: parar y dar la
vuelta a la mesa, levantarse y pasear bloqueando fisicamente, y hablar en corto antes de la reunion.
**Y conte los pasos del nodo yo mismo: `crear_cultura_escucha_equipo` tiene `17` y ninguno recoge el
segundo modo** (busque `pasear`, `levantarse`, `bloquear` en los `17`: cero coincidencias).

**LA CIFRA `1` DE `3` ES CIERTA.** Y la conclusion *no hay via* la sostiene su `grep` pegado, que es
la mitad que le costo una caida en la vuelta 27. **Lo que propone para ello lo adjudico en `5`.**

---

## 3. LA RELECTURA DE LOS `15` VEREDICTOS Y LA MUESTRA PINEADA (`AUDITOR_FORJA.md` 7)

### 3.1. LA POBLACION Y EL TAMANIO, CON LA CUENTA DELANTE

| | |
|---|---:|
| `SANO` distintos de la tanda | **12** (lineas `266`, `268` y `280` a `289`; las `269` a `278` son **los mismos diez pares** y estan declaradas no consumadas) |
| lo que `7` exige: **el mayor entre `3` y el `20` por ciento** | `max(3, 2.4)` = **3**, con techo de `20` |
| **lo que relei** | **12 de 12**, o sea **el `100` por ciento de la poblacion**, muy por encima del minimo y por debajo del techo |
| `CONTINUA` de la tanda | **3** (`265`, `267`, `279`), **y relei los tres tambien** |
| **total releido** | **15 de 15** |

### 3.2. **EL ORDEN, QUE ES MI REMEDIO `2` DE LA `ACTA 27` Y ESTA VEZ LO PUEDO PROBAR**

> **`REMEDIO 2`: la relectura destapa UNA RAZON POR VEZ, y DESPUES de imprimir sus pasos. Nunca un
> comando que saque varias razones de golpe.**

    $ ls --time-style=+%H:%M:%S .v29a/pasos_muestra_pineada.txt
      10:51:43  .v29a/pasos_muestra_pineada.txt     (los pasos de los DOS lados de los 12 pares)

**Los pasos de los doce pares estan impresos a las `10:51:43`**, y **cada razon la destape con su
propio comando, uno por linea**, despues de haber firmado mi clase. **Ni un comando saco dos razones.**

**LO QUE NO PUEDO RECLAMAR COMO CIEGO, Y LO DIGO YO:** mi apertura sellada `5.1` ya declaro que el
comando que conto las lineas le enseño la columna `veredicto`, **asi que las clases las sabia**. Lo
que relei hoy **no es la clase: es la RAZON**, que es donde vive el trabajo. **La unica clase que
reclamo como ciega sigue siendo la arista de la rueda**, con la hora de mis ficheros como prueba.

### 3.3. **LOS QUINCE, CON MI CLASE FIRMADA ANTES Y LA SUYA DESPUES**

| linea | par | **mi clase, firmada a las `10:51`** | la suya | |
|---:|---|---|---|---|
| `266` | `recorrer_rueda_hacer_cosas` contra `recorrer_trece_elementos_proceso_evaluacion_formal` | **SANO** | SANO | **coincide** |
| `268` | contra `reconocer_emociones_propias_avisar_equipo` | **SANO** | SANO | **coincide** |
| `280` | `crear_obligacion_disentir` contra `parar_debate_emocion_agotamiento` | **SANO** | SANO | **coincide** |
| `281` | contra `pedir_hechos_decision_evitar_recomendaciones` | **SANO** | SANO | **coincide** |
| `282` | contra `crear_cultura_escucha_equipo` | **SANO** | SANO | **coincide** |
| `283` | contra `proteger_tiempo_equipo_jefe` | **SANO** | SANO | **coincide** |
| `284` | contra `compartir_logica_mostrar_razonamiento` | **SANO** | SANO | **coincide** |
| `285` | contra `reservar_calendario_tiempo_ejecutar` | **SANO** | SANO | **coincide** |
| `286` | contra `cambiar_posicion_hechos_explicar_cambio` | **SANO** | SANO | **coincide** |
| `287` | contra `aprender_resultados_vencer_dos_presiones` | **SANO** | SANO | **coincide** |
| `288` | contra `evitar_presion_social_actos_equipo` | **SANO** | SANO | **coincide** |
| `289` | contra `crear_plan_creible_equipo` | **SANO** | SANO | **coincide** |
| `265` y `267` | la rueda: madre `recorrer_rueda_conscientemente`, hijo `recorrer_rueda_hacer_cosas` | **CONTINUA, madre la de `cap_11`** | CONTINUA, misma direccion | **coincide, y esta la firme A CIEGAS** |
| `279` | `crear_espacio_seguro` madre de `nutrir_ideas_nuevas_reunion_solas` | **CONTINUA, madre `crear_espacio_seguro`** | CONTINUA, misma direccion | **coincide** |

**LOS DOS QUE MAS CERCA ESTUVIERON, y los digo porque una relectura que no dice donde dudo no vale:**

- **`282`, `crear_obligacion_disentir` contra `crear_cultura_escucha_equipo`.** Son las dos sobre
  hacer que la gente hable, y el vecino tiene `17` pasos. **Lo que lo decide no es el tamanio** (`6.1`:
  *no tiene bascula*): **ni uno de sus `17` hace lo que hace ninguno de mis `5`.** El vecino monta un
  SISTEMA de ideas y quejas; el candidato declara una OBLIGACION con un objeto que pasa el turno. **Y
  la `ACTA 27` `2.3` ya lo adjudico en el sentido contrario y lo sostuvo.**
- **`281`, contra `pedir_hechos_decision_evitar_recomendaciones`**, cuya señal es `0.474`, **la mas
  alta de las doce**. Los dos usan la formula *resiste la tentacion*. **Pero uno pide informacion y
  el otro pide disenso**: *ninguno de mis `5` pasos pide informacion y ninguno de sus `5` pide
  disentir*, que es literalmente lo que su razon dice, **y lo comprobe paso a paso antes de leerla.**

### 3.4. **`279`, LA UNICA ARISTA NUEVA, ADJUDICADA CON LOS PASOS DELANTE**

**Mi lectura, escrita antes de abrir su razon:** la madre `crear_espacio_seguro` **NOMBRA** la reunion
a solas como el sitio seguro (su paso `12`), y el hijo `nutrir_ideas_nuevas_reunion_solas` la
**PROCEDIMENTA** con seis preguntas literales, la fragilidad de Jony Ive y las dos cosas que hay que
aclarar, **de las que la madre no trae ni una**. `P.5.1`: **nombrar no es procedimentar.** Lo que
queda fuera es procedimiento en los dos lados (el *plussing* de Pixar y la reunion previa de Susan
Wojcicki en la madre; el encuadre ingeniero contra comercial en el hijo).

**Su razon, destapada despues, dice exactamente eso y ademas cita `L195`.** **Coincide.**

### 3.5. LA TASA Y SU BANDA, PORQUE UNA TASA SIN BANDA ES MEDIA CIFRA

<!-- TALLADO: parcial salida=.v29a/varios.txt -->

    MUESTRA PINEADA: 0 caidas de 12 releidos -> tasa 0,00 por ciento,
                     banda Wilson 95%: 0.0 a 24.3

| | |
|---|---|
| releidos | **12** `SANO` mas **3** `CONTINUA` = **15** |
| se sostienen | **15** |
| caen | **0** |
| **tasa de la muestra pineada** | **`0,00` por ciento** |
| **banda Wilson al 95 por ciento** | **`0,0` a `24,3`** |
| cobertura | **`100` por ciento de los `SANO` de la tanda** |
| `D.8` | **limpio**: ningun `SANO` sin razon escrita |

> **`LECTURA`: la banda sigue siendo ancha y eso no es un defecto de la lectura, es el tamanio de la
> tanda.** Con `12` `SANO` no se puede estrechar mas. **La unica manera de estrechar esa banda es
> tener tandas mas grandes**, y esta vuelta cerro en `4` nodos por el coste del instrumento. **Lo digo
> porque es la cifra que mas se va a repetir si el tramo sigue encogiendo.**

---

## 4. `PASOS INVENTADOS POR CAPITULO` (`AUDITOR_FORJA.md` 8), FIRMADA POR MI Y NO COPIADA

### 4.1. **PRIMERO EL DENOMINADOR, QUE ES LO QUE `8.3` PUNTO 1 ME MANDA CONTAR**

<!-- TALLADO: parcial salida=.v29a/pasos_tramo.txt -->

    POBLACION: cuarentena/scott_radical_candor + cuarentena/_insertados/scott_radical_candor
     1 recorrer_rueda_hacer_cosas_equipo              L65-L77    pasos=12
     2 crear_espacio_seguro_madurar_ideas_nuevas      L177-L195  pasos=14
     3 crear_obligacion_disentir_equipo               L231-L233  pasos=5
     4 parar_debate_emocion_agotamiento               L235-L237  pasos=5
     5 fijar_fecha_cierre_debate_equipo               L245-L257  pasos=11
     6 repartir_decision_cercanos_hechos              L259-L289  pasos=11
     7 pedir_hechos_decision_evitar_recomendaciones   L291-L293  pasos=5
     8 persuadir_emocion_oyente_no_propia             L303-L347  pasos=11
     9 establecer_credibilidad_pericia_humildad       L349-L357  pasos=9
    10 compartir_logica_mostrar_razonamiento          L359-L365  pasos=6
    11 minimizar_impuesto_colaboracion_equipo         L367-L373  pasos=4
    12 proteger_tiempo_equipo_jefe                    L375-L379  pasos=9
    13 mantener_manos_trabajo_real_equipo             L381-L383  pasos=8
    14 reservar_calendario_tiempo_ejecutar            L385-L387  pasos=4
    15 cuidarse_agotamiento_centro_rueda              L409-L419  pasos=7
    TOTAL cap_07 (15 candidatos): 121
    cap_11 recorrer_rueda_conscientemente_cultura_equipo pasos=14
    TOTAL DEL TRAMO: 135

**Los quince renglones y sus quince cifras me salen al digito contra la tabla de `V.5.c`, y los
totales `121`, `14` y `135` contra `V.5.b`.** El denominador esta verificado.

### 4.2. **EL NUMERADOR, QUE ES EL QUE NADIE PUEDE PONER POR MI** (`8.3` punto 2)

**Lei `65` de los `135` contra su parrafo del libro**, y lo digo con su reparto:

| de donde salen | cuantos | cuando |
|---|---:|---|
| las cuatro piezas que entraron | **45**, **uno a uno y no una muestra** | en mi fase ciega (`APERTURA_CIEGA.md` `4.1`) |
| **muestra al azar de los `90` que NO habia leido** | **20** | hoy, seccion `4.3` |
| **total leido por mi** | **65 de 135**, el **`48`** por ciento | |
| **PUENTE que yo leo** | **`0`** | |

### 4.3. **LA MUESTRA, ELEGIDA CON SEMILLA ESCRITA Y NO A OJO**

<!-- TALLADO: parcial salida=.v29a/muestra_pasos.txt -->

    POBLACION DE LA MUESTRA: los pasos de los 12 candidatos de cap_07 que NO entraron
                             y que mi fase ciega NO leyo
    pasos en esa poblacion: 90
    SEMILLA: 280916 (random.Random(280916).sample(poblacion,20))

**Los `20`, leidos contra su linea del libro.** Los cuatro que mas cerca estuvieron de ser puente, y
por eso los nombro con su linea:

| paso | su linea del libro | veredicto |
|---|---|---|
| `mantener_manos` paso `8`: *la rueda entera se para si no entiendes a fondo la cosa que tu equipo esta intentando hacer* | `L383`: *The GSD wheel will grind to a halt if you don't understand intimately the "stuff" your team is trying to get done* | **TRANSCRIPCION** |
| `repartir_decision` paso `10`: las tres cosas del diagnostico | `L283`: *1) his decisions were not grounded in the facts 2) even if his decisions were the right ones, nobody was going to execute on them and 3) he was in danger of losing his team* | **TRANSCRIPCION** |
| `proteger_tiempo` paso `2`: *escucha, asegurate de haberlo entendido, y desactiva las situaciones* | `L377`: *She'd listen, make sure she understood, and then she was like a sapper... She defused some political situations that could have blown up in my face* | **TRANSCRIPCION**, y es la unica del lote que cambia el sujeto de descriptivo a imperativo, **que es el estilo de transcripcion de esta casa y no una invencion** |
| `cuidarse` paso `6`: *no finjas que no pasa nada... dio una charla sobre la dureza mental* | `L417`: *But Dick didn't pretend that nothing was wrong, either... He gave a talk to the company about the "mental toughness"* | **TRANSCRIPCION** |

**`20` de `20` TRANSCRIPCION. `0` PUENTE.**

### 4.4. **MI FILA, FIRMADA, POR CAPITULO Y CON EL TOTAL** (`8.2`)

| capitulo | nodos | **pasos escritos** | **PUENTE** | **PASOS INVENTADOS** |
|---|---:|---:|---:|---:|
| **`cap_07`** (lote 4, `scott_radical_candor`) | 15 | **121** | **0** | **`0,00` por ciento** |
| **`cap_11`** (lote 4, `scott_radical_candor`) | 1 | **14** | **0** | **`0,00` por ciento** |
| **total del tramo** | 16 | **135** | **0** | **`0,00` por ciento** |

**LA FIRMO**, y digo con que cobertura: **`65` de `135` leidos por mi, de los cuales `45` enteros y
`20` al azar con semilla escrita.** No firmo lo que no lei: **los `70` restantes los leyo el
extractor y yo los cubro por muestreo, no por confianza.**

> **`LECTURA`, en linea aparte: el `0,00` no dice que el capitulo sea facil.** `8.3` avisa del error
> contrario, marcar un puente como transcripcion para bajar la cifra y subir el volumen del lote. **Lo
> unico que vale contra eso es haber leido, y yo he leido `65`.** Y **el capitulo ayuda**: comprobe
> `L73`, `L75`, `L233`, `L237` y `L377`, y los cinco son parrafos con **inventario propio** en el
> sentido de `D.27`. **Un parrafo rico no produce puentes.**

### 4.5. LO QUE LA CIFRA DECIDE SOBRE EL VOLUMEN (`8.1`)

| lo que mido | lo que manda |
|---|---|
| el **peor capitulo** es `0,00`, muy por debajo del tope de `10` (`8.1`, 11 sep) | **el freno de fidelidad NO se activa** |
| el freno que **SI** aprieta es el otro: `EXTRACTOR.md` 12.4 y el coste de la aduana | **el tramo no lo decide `PASOS INVENTADOS` esta vez** |

**Y LO MIDO YO EN VEZ DE CREERLO:** cronometre `aduana.buscar_vecinos` sobre un candidato real de la
bandeja (`compartir_logica_mostrar_razonamiento`).

<!-- TALLADO: parcial salida=.v29a/coste.txt -->

    poblacion: 510
    vecinos por encima de umbral: 10
    SEGUNDOS de buscar_vecinos sobre 510: 73.3

> **`LECTURA`: mi cifra y la suya NO son la misma poblacion y lo digo antes de compararlas.** El
> reporte mide `63` segundos sobre la poblacion de la aduana (`348` = grafo mas las bandejas de los
> lotes 4 y 5); yo medi `73,3` sobre `510`, que incluye **todas** las bandejas del repo. **Escalado,
> es la misma cifra**, y **los `10` vecinos que me devuelve coinciden exactamente con la fila
> `compartir_logica_mostrar_razonamiento | 10` de su tabla de cola.** No hay discrepancia: hay dos
> poblaciones y las dos declaradas.

---

## 5. **LAS TRES PROPUESTAS DEL EXTRACTOR, ADJUDICADAS UNA A UNA** (`EXTRACTOR.md` 14)

*El extractor propone en su reporte y no se adjudica nada. La sede de la adjudicacion es esta.*

| # | lo que propone | **mi adjudicacion** |
|---:|---|---|
| **7** | una operacion que **AÑADA un paso transcrito** a un nodo que ya vive | **NO HOY, Y NO ES PARADA.** Ver `5.1` |
| **8** | que la aduana **no deje correr dos inserciones a la vez** sobre la misma sede | **A FAVOR, Y ERA LA ESCALADA.** Ver `5.2` |
| **9** | que el arnes **entregue la cola de vecinos por candidato, sellada**, como ya entrega el informe de lote | **NO ES MIA. VA A `PARA_ALEXIS.md`.** Ver `5.3` |

### 5.1. **PROPUESTA `7`: NO HOY, y el motivo no es que el hueco no exista**

**El hueco existe y lo verifique yo** (`2.7`): `1` modo de `3` en `1` nodo sobre `1` linea. Y el
extractor tiene razon en que **la vara de `D.30` caza el paso que sobra y no tiene gemela para el que
falta**.

**Pero la moratoria de maquinaria me alcanza a mi** (`AUDITOR_FORJA.md` 5.6, cosecha 7.F): *no
encargues arneses, guardas ni lectores nuevos salvo que una caida de dato lo exija con su cita*. **Un
hueco de transcripcion no es una caida de dato**, y el propio reporte lo dice con todas sus letras en
`V.6.a`: *un paso que FALTA no es un paso INVENTADO*.

**Y HAY UNA RAZON MAS FUERTE, que es de metodo:** esta casa lleva **tres vueltas seguidas** creando
operaciones (`corregir`, `arista`, `anotar`). **La cuarta seria la primera que escribe en
`pasos_accionables`, que es el procedimiento mismo.** Un ejemplar no es un patron: **el hueco queda
registrado y medido, no crece, y no bloquea ninguna insercion.** Cuando aparezca el segundo, el caso
tendra dos ejemplares y **entonces se decide con material, no con uno.**

**NO ES PARADA** porque ninguna regla se contradice: lo que hay es una via que no existe, **y
`EXTRACTOR.md` 7 dice expresamente que eso se declara con su cifra y se propone, no que se pare.**

### 5.2. **PROPUESTA `8`: A FAVOR, Y ADEMAS ERA LA ESCALADA QUE HABIA QUE ENCARGAR**

**A FAVOR, y la cita que la habilita es la que la moratoria pide: una caida de dato con su cita.** La
caida es `V.5.e`, la regla rota es `EXTRACTOR.md` 2 primera linea (*uno por vez*), y **la figura es
exactamente la misma que la `TAREA 2` de esta vuelta acaba de cerrar: una regla escrita que no llego
a `src/`.** Esta casa ya la ha adjudicado dos veces asi (`D.29` a la aduana en `2ea68fd`, `D.38.5` a
la aduana en `9ef933b`). **Adjudico por extension citable y no por doctrina nueva.**

**Y LO QUE LA HACE URGENTE ES LO QUE MEDI EN `1.1`: el gate salio VERDE sobre ella.** Un nodo que
entra y desaparece **deja el grafo coherente y mas pequenio**, y ninguna de las `12` guardas lo ve.
**Es `D.30` aplicada a otra sede**, y es la unica caida de esta vuelta que podria haberse quedado
dentro del dato para siempre.

> **VA ESCRITA EN `PARA_ALEXIS.md` COMO LA PRIMERA TAREA DEL RETOMAR**, porque `AUDITOR_FORJA.md` 3
> me prohibe dejar encargo en una parada. **Declararla sin encargarla seria caida mia** (`1.4`), y por
> eso no se queda solo en esta acta.

### 5.3. **PROPUESTA `9`: NO LA ADJUDICO YO, Y DIGO POR QUE**

**Es un arnes.** La moratoria me lo prohibe salvo caida de dato con su cita, **y la caida de dato de
hoy no pide este remedio: pide el `8`.** Lo dice el propio extractor contra si mismo en `V.5.f`: *el
coste del instrumento es un motivo para pedir menos candidatos, no para correr dos a la vez.*

**PERO LA CIFRA QUE LA SOSTIENE ES REAL Y LA HE REPRODUCIDO** (`4.5`): `73,3` segundos solo en
`buscar_vecinos`, `12` candidatos y `77` pares esperando. **`D.43` saco el informe de lote del turno
del extractor por esta misma medicion y con esta misma frase**: *una cifra que no cabe en un turno no
se firma en un turno*. **Extender `D.43` a la cola de vecinos es una decision de arquitectura del
bucle, y esas son de Alexis** (`AUDITOR_FORJA.md` 3, *decision de Alexis*). **Va a `PARA_ALEXIS.md`
con sus dos cifras delante.**

---

## 6. **LOS ONCE `POR ADJUDICAR` DE MI APERTURA SELLADA, ADJUDICADOS UNO A UNO**

*Mi propio `REMEDIO 1` de la `ACTA 27` `10` me obliga a que **cada uno tenga su seccion en el acta**.
Los once la tienen.*

### 6.1. **`POR ADJUDICAR 1` y `8`: EL REMEDIO `HEREDADO 1` NO SE ROMPIO, Y LO PRUEBO CON `git`**

**La pregunta que deje abierta:** las diez lineas `269`-`278` con la forma del fallo, se escribieron
antes o despues de que entrase el arreglo.

    $ git log --format="%h %ad %s" --date=format:"%H:%M:%S" -- src/aduana.py | head -1
      2ea68fd 09:23:24 VUELTA 28 TAREAS 2 y 3: D.29 llega a src/aduana.py con la insercion atomica ...
    $ git log --format="%h %ad %s" --date=format:"%H:%M:%S" -- bitacora/VEREDICTOS.jsonl | head -1
      32fa203 09:50:39 VUELTA 28 TAREAS 4 y 5: entran cuatro nodos ...

**DESPUES: el arreglo entro a las `09:23:24` y las diez lineas a las `09:50:39`.**

> **Y AUN ASI EL REMEDIO NO SE ROMPIO, y la diferencia no es de matiz: es de mecanismo.** El remedio
> cubre **una corrida que imprime `RECHAZADO`**. Esta corrida **no fue rechazada: se consumo, inserto
> su nodo, y otra corrida mia paralela lo borro al escribir su propia copia del dataset.** La prueba
> no es su palabra: **esta dentro de la propia linea `269`**, escrita por operacion:
>
>     "la insercion que escribio esta linea SI se consumo, y una corrida MIA que corria a la vez la
>      deshizo... la segunda habia leido el dataset antes de que la primera escribiera"
>
> **`_consumar_veredictos` solo se llama desde los dos caminos que se consuman**, y lo comprobe
> mutandolo en `1.7`: al devolver la escritura al bucle, **caen cinco pruebas**. **El codigo hace lo
> que el remedio pedia.** Lo que fallo es otra cosa y tiene su propio remedio, que es la propuesta `8`.

**`HEREDADO 1`: CUMPLIDO, y ahora con la cronologia medida y no supuesta.**

### 6.2. **`POR ADJUDICAR 2`: `D.42` y `D.34.2` SI se contradicen en la fase ciega, y la contradiccion se resuelve con reglas existentes**

**Lo confirmo con mi propia medida:** con `REPORTE.md` en el arbol, `censar_rutas` da **`434` de
`434`** y `test_aceptacion` da **`176` de `176`**. **Las dos caidas de mi fase ciega desaparecen sin
tocar codigo.** La contradiccion era real y era mecanica.

**MI ADJUDICACION: NO ES PARADA, y la cubre `D.13` por su letra** (*entre dos reglas fechadas que
chocan gana la mas reciente*) **leida junto con el alcance de cada una**: `D.34.2` (10-11 sep) retira
cuatro ficheros **solo durante la fase ciega y solo del arbol de trabajo**; `D.42` (15 sep) censa
**en cada commit**. **La fase ciega no commitea** (mi apertura lo dice: *no commiteo, el arnes sella
esta pagina y la commitea el*). **Los dos alcances no se solapan en ningun acto real**: lo unico que
se solapa es que **yo corri el censo a mano dentro de la fase ciega**, y esa corrida no la manda
`D.42`, la mande yo.

> **LO QUE SI DEJO ESCRITO PARA QUE NO SE PIERDA:** un auditor ciego que corra `censar_rutas` o
> `test_aceptacion` va a ver rojos que no son suyos **y puede confundirlos con la vuelta que audita**.
> Es un tropiezo de forma del arnes, **no de sustancia de auditoria**, y por `D.38.2` acotada el 12
> sep **eso es tarea del arnes y no un remedio mio**. Va a `PARA_ALEXIS.md` como nota, no como racha.

### 6.3. **`POR ADJUDICAR 3`: el censo de `D.42` no lee `APERTURA_CIEGA.md`, y hoy eso me ha costado la parada**

    $ grep -n "DOCUMENTOS = " -A 2 scripts/censar_rutas.py
      DOCUMENTOS = (os.path.join("docs", "loop", "REPORTE.md"),
                    os.path.join("docs", "loop", "ACTA_AUDITOR.md"))

**Confirmado: la apertura ciega es la unica sede de cifra de esta casa que ninguna guarda lee.**

**MI ADJUDICACION: el hallazgo es cierto y la peticion NO la hago yo.** Ampliar `DOCUMENTOS` es tocar
una guarda, y la moratoria me alcanza. **Pero es la peticion mejor sostenida que puedo llevar**, y
hoy tiene **dos ejemplares y no uno**: la `ACTA 27` `8.1` y **mi propia caida de hoy** (`8.1` de esta
acta), **las dos en esa sede y las dos encontradas a mano.** Va a `PARA_ALEXIS.md`.

### 6.4. **`POR ADJUDICAR 4`: el desorden de `cap_07` NO es de la vuelta 28**

**Lo mido antes de repartir culpa.** De las tres piezas de `cap_07` que entraron, `L65` y `L177`
**rellenan huecos** que dejaron vueltas anteriores y `L231` entra detras de `L177`. **El indice del
dataset lo confirma** (`1.6`): `240`, `241`, `242`, `243` en orden de linea del libro.

**MI ADJUDICACION: esta vuelta CIERRA desorden, no lo abre. NO ES CAIDA DE LA VUELTA 28.** El
desorden heredado (`235-237` detras de `239-243`, `295-301` delante de `245-293`) **se registra y se
queda registrado**: `EXTRACTOR.md` 12.3 pone el orden en el libro, y **ninguna regla manda reordenar
el dataset hacia atras**; reordenarlo seria reescribir una sede sin operacion que lo mande.

### 6.5. **`POR ADJUDICAR 5`: la asimetria de los siete rotulos de la rueda. ADJUDICADA, y es de frontera y no de clase**

**Lo que mi censo ciego midio:** `LISTEN` (`L79`), `CLARIFY` (`L165`) y `DEBATE` (`L213`) **no los
reclama ningun nodo**; `DECIDE` (`L259`), `PERSUADE` (`L303`), `EXECUTE` (`L367`) y `LEARN` (`L389`)
**si**, porque la primera pieza de cada una de esas cuatro secciones **empieza en la linea del rotulo**.

**MI ADJUDICACION, y la hago citando lo que ya esta adjudicado:** la `ACTA 27` `2.2` decidio que **la
cabeza de la lista de `DEBATE` no es nodo**. Aplicada a las siete, esa regla dice que **ninguna
entradilla de seccion es nodo**, y eso es lo que pasa en las tres primeras. **En las otras cuatro el
rotulo no se ha vuelto nodo: se ha quedado DENTRO del tramo de la primera pieza**, que es una
decision de frontera y no de inventario.

**LO QUE LA CONVIERTE EN NO-DEFECTO ES UNA MEDIDA Y NO UN ARGUMENTO: `0` PUENTE sobre `135` pasos**
(`4`). Si la entradilla hubiera producido pasos que el libro no dice, se veria ahi. **No se ve.**

> **LO QUE SI QUEDA, Y NO LO TAPO:** `L85`-`L89`, `L171`-`L175` y `L217`-`L223` **tienen texto y nadie
> los reclama.** Es un hueco de cobertura del mismo genero que `L153`, **medido y no arreglado**, y va
> a `PARA_ALEXIS.md` dentro del estado. **No es caida de nadie: es cola.**

### 6.6. **`POR ADJUDICAR 6`: `cap_07.md` dice `unidad: Cap. 4` y trae la portadilla de `PART II`. ES DEL RECORTE**

**MI ADJUDICACION: cierto, y NO es de la extraccion ni del bucle.** El fichero se llama `cap_07.md` y
su cabecera declara `Cap. 4` porque **los ocho capitulos numerados del libro son `cap_04` a `cap_11`**,
y eso lo fija `ORDEN_DE_LOTES.md` en la fila del lote 4, medido en la vuelta 14. **No hay
contradiccion: hay dos numeraciones, la del fichero y la del libro, y las dos estan escritas.**

Las lineas `L421`-`L433` (la portadilla de `PART II`) **son material del recorte**, y mi propia
cobertura ciega ya las contaba entre las `60` huerfanas. **Tocar `fuentes/` no es del bucle**
(`EXTRACTOR.md` 14). **Se registra y no se toca.**

### 6.7. **`POR ADJUDICAR 7`: la madre omite `Debate and decide`. ES FRONTERA DECLARADA Y ESTA BIEN PUESTA**

**Lo que comprobe hoy, y no en la fase ciega:** el hermano existe.

    $ (lector propio sobre cuarentena/)
      debatir_decidir_asuntos_cultura_evitar_delegar
        | bandeja: cuarentena/scott_radical_candor/debatir_decidir_asuntos_cultura_evitar_delegar.json

**MI ADJUDICACION: FRONTERA DECLARADA, correcta.** El `resumen_teorico` de la madre **declara el
salto, nombra las lineas y nombra al nodo que las recoge**, y ese nodo **existe y espera en la
bandeja**. `6.1` de `AUDITOR_FORJA.md`: *dos doctrinas legitimas no son duplicado, son frontera
declarada*. **Meter `L301`-`L305` tambien en la madre habria sido el duplicado.**

**Y ADJUDICO TAMBIEN LA CIFRA QUE EL REPORTE PONE AL LADO, porque la mire dos veces:** `V.5.b` dice
que el nodo *recorre seis rotulos*. **Mi cuenta da `7` si incluyo `L273` y `6` si no.** La frase
verificable que acompania a la cifra (*los seis rotulos y sus frases estan en `L275` a `L333`*) **es
cierta bajo la lectura de seis**, que es la que deja fuera `L273` por estar fuera del rango que la
propia frase declara. **No la cuento como caida**, y digo por que: **la cifra es de prosa de
acompanamiento dentro de un bloque `LECTURA`, no de TABLA, CABECERA ni CONCLUSION** (`5.2`), **y bajo
su lectura natural es verdadera.** La declaro aqui para que el siguiente lector no la vuelva a contar.

### 6.8. **`POR ADJUDICAR 9`: ninguna linea dice `consumada: true`. CIERTO, Y HOY NO ES UN DEFECTO**

    $ (lector propio) consumada=False -> 14 ; consumada=None -> 275 ; consumada=True -> 0

**MI ADJUDICACION: el campo solo sabe negar, y hoy eso es correcto y no incompleto.** Despues de la
`TAREA 2.a`, **existir en la bitacora ya significa consumada**: la escritura solo ocurre en los dos
caminos que se consuman, **y lo probe mutandolo** (`1.7`). Un `true` explicito seria **redundante**, y
un campo redundante es una segunda verdad que puede desincronizarse.

**LO QUE SI DEJO ESCRITO:** el dia que exista una tercera situacion (*escrita, no consumada, pero
tampoco deshecha*), esta sede no la va a poder expresar. **No lo arreglo hoy: no hay caso.**

### 6.9. **`POR ADJUDICAR 10`: las `8` `SIN HUELLA` no dicen *no puedo comprobarlo*, dicen *guarde mal la huella*. CIERTO, Y ES LO GRAVE**

**Lo verifique yo:** `src.comun.huella_de_nodo({})` da `e3b0c44298fc1c14`, **y es exactamente la
huella que esas ocho lineas guardaron de su vecino.** Un vecino de bandeja **tiene texto**.

**MI ADJUDICACION: mi lectura ciega era correcta, y el reporte dice lo mismo sin adornarlo**
(`V.4.c`: *la aduana guardaba en esas 8 lineas la huella de un diccionario VACIO*, *era un `or {}` que
escribia la huella de nada*). **Los ocho veredictos se emitieron sin dejar constancia comprobable de
contra que texto.**

**Y AUN ASI NO ES CAIDA DE CLASE, y digo por que:** las ocho clases **no estan mal puestas**; lo que
falta es la prueba de contra que texto se emitieron. **`D.15` tiene esa casilla escrita y se llama
`SIN HUELLA`**, la vuelta la uso, **y la cola sigue contandose e imprimiendose.** Lo que la vuelta 28
arreglo es que **de hoy en adelante la aduana guarde la huella de verdad**, y eso es la mitad de
`D.38.5` que faltaba. **Es la regla funcionando, no una caida.**

> **LO QUE QUEDA EN LA COLA Y NO LO TAPO: esas `8` no se van a poder comprobar nunca**, porque la
> huella de entonces no existe. **Se releen o se declaran, que son las dos salidas de `D.15`**, y hoy
> no estan hechas ninguna de las dos. Va al estado de `PARA_ALEXIS.md`.

### 6.10. **`POR ADJUDICAR 11`: `bloquear_tiempo_pensar_calendario` contra `agendar_cuidados_propios_cumplirlos`. ADJUDICO `SANO`**

*Lo publique **sin clase** en la fase ciega, que era lo correcto. Aqui es donde se decide.*

**Los dos, con sus pasos delante** (`.v29a` y el fichero de bandeja de cada uno). Lo que comparten:
poner la cosa en el calendario, no dejar que nadie la pise, defenderla.

| la vara de `6.1` | lo que mide este par |
|---|---|
| **direccion** | **ninguno nombra el procedimiento del otro**, ni en el titulo ni en un paso. No hay madre ni hijo que senialar |
| **sin bascula: que queda fuera** | **procedimiento en LOS DOS lados**, y ese es el criterio entero: el de `bloquear` tiene su paso `6` (*anima a todos los de tu equipo a hacer lo mismo*), que es un acto con su propio destinatario; el de `agendar` tiene sus pasos `2` y `3` (*pon en el calendario tu tiempo de desplazamiento*, *haz como si tuvieras que coger un tren*), que son dos actos con su propio objeto |
| **activacion** | uno se activa cuando **el calendario se te ha llenado de reuniones y no queda hueco para pensar**; el otro cuando **no consigues salir a tiempo para cenar en casa** |
| **entregable** | **tiempo de pensar protegido en el trabajo** contra **tus propias citas cumplidas** |

> **`SANO`, y son dos doctrinas legitimas sobre el mismo instrumento** (el calendario) **aplicadas a
> dos objetos distintos.** `6.1`, ultima fila: **eso es frontera declarada, y una frontera se pierde
> por poda, no por fusion.**

**Y LA MITAD QUE IMPORTA MAS QUE LA CLASE:** los dos **siguen en bandeja**, son de **capitulos
distintos**, y **mi barrido no los cruza ni una vez en las `77` lineas**. `D.19`: *ninguna señal
separa jerarquia de ruido*. **Si nadie escribe esto ahora, entraran en vueltas distintas y nadie los
va a poner uno al lado del otro.** Queda escrito aqui con su clase, **y va al estado de
`PARA_ALEXIS.md` para que la vuelta que inserte al primero lo lea contra el segundo.**

### 6.11. **Y EL PAR QUE VUELVE (`7.4` de mi apertura), QUE NO ES UN `POR ADJUDICAR` PERO CIERRA AQUI**

`fijar_fecha_cierre_debate_equipo` sigue en bandeja y `centrar_debate_ideas_fuera_egos` ya vive.
**Cuando el primero entre, ese par se levanta otra vez.** **La adjudicacion de la `ACTA 27` `2.2` es
`SANO SIN ARISTA` y NO la reabro**, ni aprovechando que perdi aquella. Queda escrito para que no se
discuta desde cero.

---

## 7. LAS CAIDAS DEL EXTRACTOR, CON SU ESPECIE Y SU SEDE

### 7.1. **CERO DE ESPECIE `REPORTE`, Y ES LA PRIMERA VEZ DESDE LA VUELTA 25**

**Recompute las `10` cifras de apertura y cierre, el reparto de los `25` veredictos linea a linea, las
`2` aristas por sus dos extremos, las `6` filas de la vigencia, las `15` filas de pasos por candidato,
los `3` totales de `PASOS INVENTADOS`, las `12` filas de la cola, la suma `77`, el reparto `27` mas
`50`, las `6` cifras de `cap_04`, las `2` series `D.37` y los `3` modos de `L153`. Y ademas los dos
bloques de `git show` de `V.3.a`, pegados al caracter.**

**No encontre ni una falsa.** Lo unico que mire dos veces esta en `6.7`, es de prosa de acompanamiento
y bajo su lectura natural es cierto. **`REPORTE`: cero caidas en esta tanda.**

### 7.2. **UNA CAIDA, Y LA CARGO COMO `CLASE`: LA CAIDA DE DATO DE `V.5.e`**

| | |
|---|---|
| **que paso** | lanzo dos `insertar` a la vez contra `EXTRACTOR.md` 2 (*uno por vez*); la segunda corrida habia leido el dataset antes de que la primera escribiera y, al escribir su copia, **dejo fuera el nodo `crear_obligacion_disentir_equipo`** |
| **que sede movio** | **`dataset/nodos.jsonl`**, que `5.2` nombra como sede de `CLASE` |
| **quien la encontro** | **el extractor**, recontando nodos contra veredictos. **No la encontro ninguna guarda: el `gate` salio VERDE sobre ella** |
| **como la trato** | la midio antes de tocar nada, declaro las `10` lineas NO CONSUMADAS **por operacion y sin borrar**, reinserto en serie y **restauro el orden del libro**. Lo verifique todo en `1.4` y `1.6` |
| **especie** | **`CLASE`** |

**POR QUE `CLASE` Y NO OTRA COSA, Y DECLARO LA TENSION EN VEZ DE RESOLVERLA COPIANDO:**

`5.2` define `CLASE` como *un veredicto mal puesto*, **y aqui ninguno lo estaba: relei los diez y los
diez se sostienen** (`3.3`). Pero `5.2` pone **el dataset** entre las sedes de `CLASE`, y **esta
caida movio el dataset**. **La sede encaja y la definicion no.**

**Elijo la lectura que le cuesta un escalon, y digo mis tres motivos:**

1. **La sede es citable y la definicion es la que se queda corta.** Es la misma figura que el 2 sep
   2026 obligo a escribir *la cifra del codigo cuenta*: **un dano real que no tenia casillero.**
2. **El extractor se cargo a si mismo la especie mas fea que supo nombrar.** Un auditor que rebaja lo
   que el medido declaro contra si mismo **esta absolviendo**, y `5.4` dice de que lado se cae la duda.
3. **Ninguna guarda la vio.** La metrica de credito existe **exactamente para lo que las guardas no
   ven**, y esta es la definicion literal de eso: *un nodo que entro y desaparecio deja el grafo
   coherente y mas pequenio*.

**Y LO QUE NO HAGO:** no escribo la fila que le falta a la tabla de `5.2`. **Eso es doctrina y es de
Alexis** (`6.3`: *ninguna vuelta estrecha ni ensancha esta vara sin correccion declarada de Alexis*).
**Lo propongo en `PARA_ALEXIS.md` y adjudico el caso con la regla que hay.**

**NO ES PARADA DEL EXTRACTOR**, y lo mido: `CLASE` venia en **`0` de `2`** (`ACTA 27` `9.1`), asi que
esta es **la primera y no la segunda**. `5.4` pide **dos tandas seguidas**.

### 7.3. LO QUE REGISTRO CONTRA EL EXTRACTOR Y **NO** ACUMULA

- **`V.3.c` ensancha el alcance de `2.b` mas alla de lo que el encargo nombra.** Lo marco el como
  discutible `1` y **lo adjudico SOSTENIDO** (`2.1`). **Se registra que lo hizo sin mandato explicito
  y se le da la razon**, que son dos cosas distintas y las dos ciertas.
- **`V.9.d` publica `5802702` como *ultimo commit al tallar este cierre*, y la vuelta cerro en
  `dd79e01`.** Lo mire y **no es falso**: la celda esta acotada a *al tallar*, y el tallado corre
  antes del commit que lo escribe. **Registro que la celda solo se entiende con su acotacion.**

### 7.4. **LO QUE LE RECONOZCO, Y NO ES UN CONSUELO**

**Esta vuelta cerro tres cosas que llevaban entre dos y nueve vueltas abiertas**: la arista de la
rueda (dos vueltas), la mitad de `D.38.5` que no llegaba al registro (cuatro dias), y la
contradiccion entre `cerrar_reporte.py` y `D.15` (que mi propia acta anterior adjudico y esta ejecuto).
**Y encontro sola la unica caida de la vuelta**, con el gate en verde encima. **Eso es lo contrario de
un reporte que se cubre.**

---

## 8. **MIS PROPIAS CAIDAS, CON MI NOMBRE Y ANTES DE LAS RACHAS**

### 8.1. **`CIFRA PUBLICADA PROPIA`: mi apertura sellada dice `guardas en rojo: 2` y eran `3`. La tercera era mia**

**LA CIFRA, en la tabla de cierre de mi propia apertura** (`APERTURA_CIEGA.md` seccion `10`):

    | guardas en verde | **gate, guiones, resolutor** |
    | guardas en rojo  | **2**: test_aceptacion (1 de 176) y censar_rutas (4 de 96),
                          **las dos por la retirada de REPORTE.md de mi propia fase** |

**LO QUE ERA CIERTO CUANDO LO MEDI, Y LO DIGO ANTES DE CASTIGARME:**

    $ ls --time-style=+%H:%M:%S .v29/guardas_v29.txt
      09:57:02      (BARRIDO DE GUIONES VERDE, salida literal pegada)

**A las `09:57:02` el barrido ERA verde y su salida esta pegada.** `D.38.3` cumplida por su letra.

**LO QUE PASO DESPUES, Y ES MIO:**

    $ ls --time-style=+%H:%M:%S .v29/
      10:03:46  libro_65_77.txt          (un guion largo del libro, sin transliterar)
      10:19:xx  rotulos_cap07.py         (dos guiones largos dentro de dos literales)
      10:21:xx  libro_cap11_281.txt      (dos guiones largos del libro)
    $ el sello de mi pagina                     10:41:02
    $ docs/loop/loop.log, tres segundos despues 10:41:0x
      BARRIDO DE GUIONES EN ROJO: 5 hallazgo(s)
        .v29/libro_65_77.txt ... .v29/libro_cap11_281.txt ... .v29/rotulos_cap07.py ...
      [pre-commit] COMMIT ABORTADO: hay guiones largos o medios en el repo.

**ME LA CARGO, Y ESTOS SON LOS CUATRO MOTIVOS:**

1. **La celda que cae no es la del instrumento: es la de la CONCLUSION.** La seccion `1` pega la
   salida y esa se defiende. **La seccion `10` es un recuento del estado al cerrar mi fase**, y al
   cerrarla eran **tres** guardas en rojo, no dos.
2. **La conclusion ademas atribuye el rojo al arnes en las dos**, y **excluye por construccion
   justo el rojo que era mio.** Eso no es una cifra que envejecio: es una cifra que se equivoco
   sobre quien la habia roto.
3. **La cifra tenia remedio en un comando y el comando es el mismo que yo le encargue al extractor**
   (`ACTA 27` `9.4`, `D.38.3`: *una cifra que sale de contar una salida se vuelve a contar*). **Mi
   pagina volvio a correr el barrido a las `10:3x`, pero ACOTADO a un solo fichero**
   (`forja.py guiones docs/loop/APERTURA_CIEGA.md`), **y publico con el una conclusion de alcance
   repo.** `AUDITOR_FORJA.md` 0 lo dice con estas palabras: **la fuente hay que elegirla antes de
   contarla.**
4. **No es hipotetica: tumbo el commit de mi propia pagina sellada**, y esta escrito en `loop.log`.

**SEDE:** `docs/loop/APERTURA_CIEGA.md`, que es `docs/` y es **la misma sede que me costo la
`CIFRA PUBLICADA PROPIA` de la `ACTA 27` `8.1`.** **ACUMULA.**

**LO QUE NO ME DESCUENTO:** que los cinco hallazgos esten en `.v29/`, que sea scratch, o que los
guiones vengan del libro. **`.v29/` es el repo** (sus hermanas `.v21` a `.v28` estan commiteadas), el
barrido es repo-entero por su propia frase, **y la casa transliterá los guiones del libro en todas
partes menos donde yo no mire.**

### 8.2. **CAIDA DE METODO, declarada y sin acumular: arregle el rojo antes de escribir el acta**

Sustitui los `5` guiones largos (los de las citas del libro por el guion corto normal, y los
dos del literal del lector por su forma escapada) **con una nota de correccion declarada dentro de cada fichero**, y el barrido volvio a verde.
**Lo hice ANTES de contarlo aqui**, y lo digo porque el orden importa: **si no lo dijera, el acta
publicaria un barrido verde sobre un rojo que yo mismo habia limpiado sin declararlo.**

**Se registra con mi nombre y NO acumula** (`5.4`, correccion del 16 sep: *la caida que no acumula se
sigue registrando con tu nombre*): es de forma de artefacto, no de sustancia de auditoria.

### 8.3. **LAS DOS SON UNA TANDA, Y LA TANDA ES LA UNIDAD**

`ACTA 25` `8.2`: las rachas cuentan tandas, no piezas. **De las dos, solo `8.1` acumula.**

---

## 9. LAS RACHAS AL CERRAR, Y LAS SEIS CONDICIONES DE PARADA

### 9.1. Las cuatro rachas, con su motivo

| especie | de quien | venia en | **queda en** | por que |
|---|---|---|---|---|
| **`CLASE`** | extractor | 0 de 2 | # **1 DE 2** | **la caida de dato de `V.5.e`** (`7.2`). Movio el dataset y el gate salio verde |
| **`CIFRA PUBLICADA`** | extractor | 0 de 2 | **0 de 2** | **no toca `config/`, `esquema/` ni `fuentes/`**, y las cifras que escribe en `src/` son las de las guardas nuevas, **que mute y muerden** (`1.7`) |
| **`REPORTE`** | extractor | 2 de 3 | # **0 DE 3** | **cero caidas de esa especie en esta tanda** (`7.1`). **La reinicia una TANDA LIMPIA**, `D.38.1` y la correccion de `5.4` del 16 sep: *limpia significa sin caidas de la especie que esa racha acumula* |
| **la mia, una sola** | **auditor** | 2 de 3 | # **3 DE 3** | **`CIFRA PUBLICADA PROPIA`** (`8.1`). La de `8.2` se registra y no acumula |

**DIGO CUAL DE LAS DOS COSAS REINICIA LA DE `REPORTE`, porque `5.4` me obliga a citarla:** **una tanda
limpia**, no una decision del fundador. **Y no reinicio ninguna por mi cuenta: `5.2` dice literalmente
*ninguna de las dos eres tu*, y la que aplico es la primera de las dos, medida en `7.1`.**

### 9.2. La consecutividad, medida contra las actas y no contra mi memoria

| tanda | `CLASE` extr. | `REPORTE` extr. | **la mia** | de donde |
|---|---|---|---|---|
| **vuelta 25** | 0 de 2 | 3 de 3, **parada** | 2 de 3 | `ACTA 25` |
| **reinicio** | | **0 de 3**, decision del fundador del 15 sep, `paradas/2026-09-15-la-ruta-vacia-DECISION.md` | | `ACTA 26` `8.1` |
| **vuelta 26** | 0 de 2 | 1 de 3 | 3 de 3, **parada** | `ACTA 26` |
| **reinicio** | | | **1 de 3**, decision del fundador del 16 sep, `paradas/2026-09-16-la-frase-y-el-instrumento-DECISION.md` | `PROMPT_SIGUIENTE.md` de la vuelta 27 |
| **vuelta 27** | 0 de 2 | 2 de 3 | 2 de 3 | `ACTA 27` |
| **vuelta 28** | # **1 de 2** | # **0 de 3** (tanda limpia) | # **3 de 3, PARADA** | esta acta |

**Mi tanda de la vuelta 28 NO es limpia de mi especie**, asi que no hay nada que reinicie mi racha.
**Tres seguidas: 26 no cuenta porque el fundador la reinicio; cuentan 27 y 28 sobre el `1` con el que
el reinicio me dejo.** `1 + 1 + 1 = 3`.

### 9.3. **LAS SEIS CONDICIONES DE PARADA, UNA A UNA** (`AUDITOR_FORJA.md` 3)

| condicion | mi medida |
|---|---|
| **doctrina NUEVA necesaria** | **NO.** Los `7` discutibles, las `3` propuestas y los `11` `POR ADJUDICAR` se adjudican **citando regla escrita**: `D.29`, `D.15`, `D.13`, `P.5.1`, `6.1`, `ACTA 27` `2.2`, `EXTRACTOR.md` 7 y 14, y la moratoria 5.6 |
| **contradiccion con regla vigente o cifra publicada** | **HAY UNA Y SE RESUELVE**: `D.42` contra `D.34.2` en la fase ciega (`6.2`). **La resuelve `D.13` leida con el alcance de cada una**, y el efecto medido es cero: con el fichero de vuelta, las dos guardas salen verdes |
| **decision de Alexis** | **SI, y por eso hay cosas que dejo sin hacer y no sin decir**: la fila que le falta a `5.2`, que `D.42` lea `APERTURA_CIEGA.md`, y extender `D.43` a la cola de vecinos. **Las tres van a `PARA_ALEXIS.md` y ninguna la hago yo** |
| **fallo tecnico repetido** | **NO.** `gate`, `resolutor`, `test_aceptacion` (`176` de `176`), `censar_rutas` y `tallar_reporte` **en verde hoy**. El unico rojo fue el barrido de guiones, **fue mio, fue de una sola vuelta y esta arreglado** |
| **credito roto** | # **SI. MI PROPIA RACHA LLEGA A `3 de 3`** (`8.1`, `9.1`). El extractor no: `CLASE` `1 de 2`, `CIFRA PUBLICADA` `0 de 2`, `REPORTE` `0 de 3` |
| **campania consumada** | **NO.** Lote 4 al **`40` de `142`** insertados, lote 5 sin abrir |

> ### **HAY PARADA, Y ES MIA. `PARA_ALEXIS.md` se escribe y `PROMPT_SIGUIENTE.md` queda VACIO.**
>
> **Lo digo con la palabra que me corresponde: el bucle no se detiene porque el extractor fallara.**
> El extractor firma **la mejor vuelta verificada de la campania**: diez cifras al digito, quince
> veredictos sostenidos, dos guardas que muerden bajo mutacion y **la unica caida de la vuelta
> encontrada por el mismo con el gate en verde encima**. **Se detiene porque yo publique `2` donde
> habia `3`, en la unica sede de esta casa que ninguna guarda lee, y la tercera la habia roto yo.**

### 9.4. **LA ESCALADA SE ENCARGA, NO SOLO SE DECLARA** (`1.4`, `5.5`)

**`5.5` es literal: tres actas seguidas con la misma caida propia obligan a que el acta siguiente ABRA
con su remedio como tarea bloqueante del propio auditor.** Las mias (`ACTA 26` `8.1`, `ACTA 27` `8.1`,
`ACTA 28` `8.1`) **son las tres de la misma familia: una cifra de la fase ciega.**

**Y COMO NO HAY ENCARGO SIGUIENTE QUE ESCRIBIR, el remedio va a `PARA_ALEXIS.md`**, que es la unica
sede que sobrevive a una parada. **Declararlo sin llevarlo a una sede que alguien vaya a leer seria la
caida propia que `1.4` me prohibe.**

---

## 10. **TAREA BLOQUEANTE DEL AUDITOR**, para el auditor que retome

*Va escrita aqui Y en `PARA_ALEXIS.md`, con su comprobacion mecanica.*

| # | **REMEDIO** | como se comprueba que se cumplio |
|---:|---|---|
| **1** | **LA TABLA DE CIERRE DE LA APERTURA CIEGA SE ESCRIBE DESPUES DE VOLVER A CORRER LAS GUARDAS, Y EL BARRIDO SE CORRE SIN ACOTAR.** Ninguna celda de recuento de esa pagina se rellena con una medida anterior a la ultima escritura de la pagina | que la apertura publique **dos** corridas de `forja.py gate`, `guiones`, `resolutor`, `test_aceptacion` y `censar_rutas`, **la segunda sin argumento de ruta**, con la hora de sus dos ficheros de salida, **y la ultima posterior a todo fichero de `.vNN/`** |
| **2** | **LO QUE LA FASE CIEGA ESCRIBE EN `.vNN/` PASA EL BARRIDO ANTES DE SELLAR.** Una cita del libro se translitera al escribirla, no al descubrirla | `python forja.py guiones` **VERDE** en la ultima linea de la apertura, con su salida pegada |
| **3** | **LOS `POR ADJUDICAR` SE ADJUDICAN TODOS, CADA UNO CON SU SECCION.** Se mantiene de la `ACTA 27` `10` remedio `1`, **porque esta vez SI se cumplio** (`11` de `11`, seccion `6`) y lo que funciona no se retira | `grep -c "POR ADJUDICAR" docs/loop/APERTURA_CIEGA.md` contra las secciones del acta |
| **4** | **LA RELECTURA DESTAPA UNA RAZON POR VEZ, DESPUES DE IMPRIMIR LOS PASOS.** Se mantiene de la `ACTA 27` `10` remedio `2`, **cumplido hoy y comprobable** (`3.2`) | el fichero de pasos con **fecha anterior** a la primera consulta de la bitacora |

**LAS CUATRO SON DE SUSTANCIA DE AUDITORIA** (cifras y lecturas), **asi que si se rompen, acumulan**
(`D.38.2` acotada el 12 sep). **Ninguna es de formato de artefacto.**

---

## 11. `D.32`: ESTA ACTA NO CIERRA NINGUN LOTE, LUEGO NO ABRE NINGUNO

*Mido si cierra alguno en vez de suponerlo.*

| | mi medida |
|---|---|
| **lote 4** (`scott_radical_candor`) | **cerrado en extraccion** desde la `ACTA 24`; **ABIERTO en insercion**: `102` en bandeja y `40` insertados de `142`, o sea **el `28` por ciento**. **Lo que cierra un lote es insertarlo entero** |
| **lote 5** (`marquet_turn_the_ship`) | **abierto** en la vuelta 25: `3` candidatos en bandeja. **Sin tocar en esta vuelta, y es deliberado** (`D.39`) |
| **lo que SI cierra esta vuelta** | **nada**: `cap_07` se queda con `12` en bandeja |
| **conclusion** | **no hay lote que cerrar, luego no hay lote que abrir.** `ORDEN_DE_LOTES.md` no se toca y **las condiciones del lote 6 no se miden hoy**, porque medirlas seria fingir que el 5 esta cerrado |

---

## 12. LA VUELTA 28 Y MI TURNO, EN UNA TABLA

| | |
|---|---|
| **vuelta auditada** | **28**, sin hueco de acta, huella de la herencia **cuadrada al caracter** |
| **cifras del reporte recomputadas** | **`10` de `10` al digito** (cinco de apertura contra `git`, cinco de cierre contra el arbol), mas el reparto de los `25` veredictos linea a linea, las `15` filas de pasos por candidato, las `12` de la cola y sus tres sumas, las `6` de la vigencia y los dos `git show` al caracter |
| **guardas y censos corridos por mi** | **`6`**: `gate`, `guiones`, `resolutor`, `test_aceptacion`, `censar_rutas`, `tallar_reporte` |
| **guardas mutadas** | **`2`, y las dos MUERDEN**, mutando el codigo y no el valor esperado (`1.7`) |
| **relecturas** | **`15` de `15`**: los `12` `SANO` y los `3` `CONTINUA` |
| **caidas de `CLASE` en la relectura** | **`0`.** Los quince se sostienen |
| **tasa de la muestra pineada** | **`0,00` por ciento**, banda Wilson **`0,0` a `24,3`** al 95 por ciento, cobertura **`100` por ciento** |
| **`PASOS INVENTADOS`** | **`cap_07` `0,00`, `cap_11` `0,00`, total `0,00`.** Firmada con `65` de `135` pasos leidos por mi, `45` enteros y `20` al azar con **semilla `280916`** escrita |
| **discutibles adjudicados** | **`7` de `7`, los `7` SOSTENIDOS** |
| **propuestas adjudicadas** | **`3` de `3`**: una a favor, una que no y una que no es mia |
| **`POR ADJUDICAR` de mi apertura** | **`11` de `11`**, cada uno con su seccion (`6`) |
| **paradas del extractor** | **`0` declaradas.** La primera vuelta sin ninguna desde la 25 |
| **caidas del extractor** | **`1`, de especie `CLASE`**, la caida de dato de `V.5.e`. **Cero de `REPORTE` y cero de `CIFRA PUBLICADA`** |
| **caidas propias** | **`2`, una tanda**: una `CIFRA PUBLICADA PROPIA` que acumula y una de metodo que se registra |
| **rachas al cerrar** | `CLASE` **1 de 2**, `CIFRA PUBLICADA` **0 de 2**, `REPORTE` **0 de 3** (reiniciada por tanda limpia), **la mia 3 de 3** |
| **CREDITO ROTO** | # **SI, Y ES EL MIO.** `PARA_ALEXIS.md` escrito, `PROMPT_SIGUIENTE.md` vacio |
