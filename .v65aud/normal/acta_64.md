

# ACTA 64. VUELTA 65, lote 7 (`grove_high_output`), **CLASE INSERCION**: **LAS `20` FILAS ENTRARON UNA POR VEZ, SIN SOLAPARSE, CON LOS BYTES QUE SE LEYERON Y CON LAS `48` LINEAS DE VEREDICTO QUE LA `ACTA 63` DEJO ADJUDICADAS, LETRA A LETRA. SE LO FIRMO ENTERO: CERO CAIDAS SUYAS, `R5` CUMPLIDO Y `REPORTE` VUELVE A `0 de 3`. LO UNICO ROJO QUE ENCUENTRO ES MIO: UNA TABLA DE MI APERTURA SELLADA QUE EL CIERRE ESTRICTO NO PUEDE TALLAR**

*Auditor `claude-opus-5-5`, esfuerzo alto, 24 sep 2026 (el turno arranco el 23 a las `23:54`), turno
normal de la vuelta que el arnes numera `1` en la corrida que arranco a las `21:50`. Linea **serial**,
rama `extraccion-mundo-11`, hash auditado `d122a40` (cierre del extractor), arbol en `55e3452` con mi
apertura sellada (`0a8eff4`). Modo austero (`D.47`): lo que el `loop.log`, la `ACTA 63` y el reporte ya
dicen no se repite. Toda mi evidencia de este turno esta en `.v65aud/normal/`.*

## 64.0. **HUECO DE ACTA Y HERENCIA** (`1.0`, `D.40`)

**NO HAY HUECO.** La `ACTA 63` cubre la vuelta `64`; esta cubre la `65` entera: el turno del extractor
(`11:37` a `20:04` del 23, `42` commits de `90028c0` a `d122a40`), la pausa segura del reinicio del equipo
(`0715cba`, fase ciega anulada sin sello, archivada en `docs/loop/archivo/interrumpidas/`), la cosecha de
Marquet que llego a esta rama despues (`f770c8c`) y mi segunda fase ciega, sellada en `55e3452`.

    $ python forja.py herencia | sed -n '6,7p'
      su huella     : 37ecde5c2c542fb52426e7fac85127efb5e226d7
      heredados     : 1

**La huella es la que mi apertura declaro** sin recomputarla (`APERTURA_CIEGA.md` `0`). Salida entera en
`.v65aud/normal/herencia.txt`.

| heredado | estado | donde lo mido |
|---|---|---|
| `R5` (del extractor): un bloque `$` contiene lo que el comando imprimio y nada mas; si se corta, por el final y dentro del bloque `(recortado, entero en <fichero>)`; y un comando que imprime algo no queda sin ninguna linea debajo | **CUMPLIDO**, medido con los dos instrumentos | `64.2` |

## 64.1. **LO QUE VERIFICO, CON MIS PROPIOS COMANDOS** (`1.1`)

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 366
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python forja.py resolutor
    nodos vivos: 366
    nodos deprecados (archivo): 0
    alias registrados: 0
    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        366 dataset/nodos.jsonl
        795 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1162 total
    $ ls cuarentena/grove_high_output/*.json | wc -l
    71
    $ ls cuarentena/_insertados/grove_high_output/*.json | wc -l
    21
    $ git diff --stat d122a40 HEAD -- dataset/ bitacora/ censos/ config/pares_mutuos.jsonl | wc -l
    0

    $ grep 'total:' .v65aud/normal/suite.txt; tail -1 .v65aud/normal/suite.txt
      total: 379 pruebas, 0 fallos, 0 errores
    rc=0

(Salidas enteras en `.v65aud/normal/gate.txt`, `guiones.txt`, `resolutor.txt` y `suite.txt`.) **`366`,
`795`, `1`, `71` y `21`, las del reporte `65.4.a`**, y cero lineas de diff en el dato desde el cierre del
extractor.

**LO QUE REPRODUZCO DE SU TRAMO**, corriendo sus instrumentos contra sus salidas guardadas:

    $ python .v65ext/relojes.py | diff - .v65ext/relojes.txt && echo IDENTICO
    IDENTICO
    $ python .v65ext/pasos_inventados.py | diff - .v65ext/pasos_inventados.txt && echo IDENTICO
    IDENTICO
    $ python .v65ext/aristas_vuelta.py | diff - .v65ext/aristas_vuelta.txt && echo IDENTICO
    IDENTICO
    $ python .v64ext/orden.py | diff - .v65ext/orden.txt && echo IDENTICO
    IDENTICO

(`.v65aud/normal/reproducciones.txt`.)

**EL TABLERO YA CUENTA LO QUE ENTRO.** La fila de Grove del `TABLERO.jsonl` que el arnes dejo sin
commitear dice `21` insertados y `21` en el grafo, y lo mido por el otro lado:

    $ python .v65aud/normal/grove_en_grafo.py
    TABLERO marquet_turn_the_ship | insertados 0 | nodos_en_grafo 0 | bandeja 20
    TABLERO grove_high_output | insertados 21 | nodos_en_grafo 21 | bandeja 71
    TABLERO gerber_emyth | insertados 0 | nodos_en_grafo 0 | bandeja 22
    MEDIDO  grove_high_output | nodos del grafo con esa fuente 21 | en _insertados 21 | en bandeja 71
    MEDIDO  gerber_emyth | nodos del grafo con esa fuente 0 | en _insertados 0 | en bandeja 22
    MEDIDO  marquet_turn_the_ship | nodos del grafo con esa fuente 0 | en _insertados 0 | en bandeja 20

(`.v65aud/normal/grove_en_grafo.txt`.)

**EL CIERRE ESTRICTO, CORRIDO POR MI, SALE EN ROJO, Y EL ROJO ES MIO:**

    $ grep -nE '^(CIERRE|CENSO|TALLADO) |^SIN COMPROBAR' .v65aud/normal/cerrar_reporte.txt; tail -1 .v65aud/normal/cerrar_reporte.txt
    2:TALLADO DEL REPORTE (D.41): la tabla que dice ser de instrumento
    175:SIN COMPROBAR  docs/loop/APERTURA_CIEGA.md linea 270
    178:TALLADO EN ROJO (estricto): 1 tabla(s) declaran instrumento y no se pueden comprobar.
    181:CENSO DE RUTAS (D.42): la unidad de la ruta es la celda
    191:CENSO VERDE: las 928 rutas publicadas sostienen lo que dicen sostener.
    982:CIERRE EN ROJO. No pasa: tallado del reporte (D.41)
    rc=1

**El reporte del extractor pasa entero** (su `.v65ext/cierre_reporte.txt`, corrido antes de que existiera
mi apertura, da `CIERRE VERDE`). Lo que no se puede tallar es **la tabla de la seccion `7` de mi apertura
sellada**, la de *lo que la sostiene*, que es una tabla de LECTURA y lleva en la frase de encima la ruta
`.v65aud/mis_clases.tsv`: el tallador lee esa frase como declaracion de instrumento (`scripts/tallar_reporte.py`
`_declaracion`) y no encuentra la tabla en el `.tsv`. **Sus celdas son ciertas** (el `0,460` es la primera
linea de `.v65aud/sim_ciegas.txt`, y las citas del libro estan en su linea: `cap_02` L69 y `cap_03` L27,
comprobadas con `grep -o` en `.v65aud/normal/citas_linea270.txt`), asi que no es cifra: **es la forma de mi
pagina, y tiene consecuencia para el siguiente**, que va en `64.9` y en el encargo.

## 64.2. **EL REPORTE, AFIRMACION POR AFIRMACION** (`5.2`)

| afirmacion del reporte | sale | sede | especie |
|---|---|---|---|
| `65.0`: `346`/`740`/`1`/`91`/`1` al abrir, el cerrojo `679b2259` del dataset | **cierta**, reproducida contra `90028c0` (el bloque de `64.2` debajo) | bloque | |
| `65.2.1`: `22` fichas iguales al commit de su lectura entera, `0` distintas | **cierta**, y mi fase ciega lo midio del lado del grafo: `20` nodos iguales y `20` blobs iguales (`APERTURA_CIEGA.md` `3`) | bloque | |
| `65.2.2`: el orden, identico al de la `64` | **cierta** (`64.1`) | bloque | |
| `65.3`: `20` filas, cada una con su aduana de hoy, sus vecinos y sus lineas | **cierta, fila a fila**: los vecinos por fila son los de mi barrido completo (`APERTURA_CIEGA.md` `6`, `48` pares) y las lineas son las adjudicadas (`64.3`) | tablas | |
| `65.3`, cierre de `T3`: *cero `CAERIA`, cero vecinos sin linea, cero lineas cuyo vecino ya no se levantara* | **cierta** (`64.3`) | conclusion | |
| `65.4.a`: `+55` en la bitacora, `48` lineas y `7` aristas | **cierta** (`64.3`), y confirma la hipotesis que mi apertura dejo escrita sin cifra (`APERTURA_CIEGA.md` `6`, punto `3`) | tabla | |
| `65.4.b`: `15` registros con arista, `12` distintas, `11` en el grafo, `1` en cola | **cierta**: mi apertura mide `12` esperadas, `11` viven, `1` no (`APERTURA_CIEGA.md` `5`) | bloque | |
| `65.4.c`: `cap_02` `4` de `50`, `cap_03` `2` de `108` | **cierta** (`64.5`) | tabla | |
| `65.4.d`: `7,68` h, de `13,6` a `39,6` minutos por ficha | **cierta**: `816,3` y `2378,6` s | bloque | |
| `65.4.g`: `R5` con sus dos instrumentos | **cierta**, y la adjudico debajo | bloque | |
| `65.4.g`: *en `procesos/` solo quedan los dos cerrojos que no son de este dataset* | **cierta en su instante** (`.v65ext/censo_cierre.txt`); hoy `procesos/` esta vacio y ninguno de los dos era de este arbol | prosa | |

**`R5`, MEDIDO CON LOS DOS INSTRUMENTOS**, en mis copias con la cabecera cambiada a la `65`
(`.v65aud/normal/pegado65_aud.py` y `.v65aud/normal/bloques_mudos65_aud.py`, sacadas con `sed` de
`.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py`, no de las copias del extractor):

    $ python .v65aud/normal/pegado65_aud.py
    bloques abiertos con `$` en el tramo de la vuelta 65 : 29
    bloques que ROMPEN R1 (ACTA 60 60.15)                : 1
       $ wc -l bitacora/VEREDICTOS.jsonl dataset/nodos.jsonl config/pares_mutuos.jsonl
           NO ES LA SALIDA DEL COMANDO: 3 de 4 lineas pegadas que el comando no imprime
    $ python .v65aud/normal/bloques_mudos65_aud.py
    bloques abiertos con `$`: 20 | comandos `$`: 29 | comandos sin ninguna linea de salida en su bloque: 0

**EL BLOQUE MARCADO NO ROMPE `R5`, Y LO ADJUDICO POR SU LETRA.** Es el `wc -l` de la apertura de `65.0`: el
instrumento lo vuelve a correr **hoy, despues de las `20` inserciones**, y compara contra lo que la
apertura midio **antes de la primera**. Lo pegado es literal de `.v65ext/apertura.txt` y es lo que ese
comando imprime contra el commit de apertura:

    $ for f in bitacora/VEREDICTOS.jsonl dataset/nodos.jsonl config/pares_mutuos.jsonl; do echo "$f $(git show 90028c0:$f | wc -l)"; done
    bitacora/VEREDICTOS.jsonl 740
    dataset/nodos.jsonl 346
    config/pares_mutuos.jsonl 1

**El bloque contiene lo que el comando imprimio y nada mas**, que es lo que `R5` pide; el instrumento no
sabe que el estado se movio, y **el reporte lo declaro en vez de esconderlo**. Los comandos sin salida
debajo son `0`. **`R5` CUMPLIDO.**

**NINGUNA AFIRMACION FALSA EN TABLA, CABECERA NI CONCLUSION: TANDA LIMPIA DE `REPORTE`.**

## 64.3. **LA BITACORA CONTRA LO ADJUDICADO** (`D.29`, `D.53`, encargo TAREA 3: *no se reescriben*)

**Las `55` lineas nuevas, una a una, contra `.v64ext/veredictos_listos.txt` y `.v63ext/cmd_02_detectar.sh`:**

    $ python .v65aud/normal/bitacora_contra_listos.py
    tanda leida de .v65ext/orden.txt, filas 1 a 20: 20
    lineas nuevas en la bitacora: 55 | veredictos de aduana: 48 | declaraciones de arista: 7
    veredictos iguales a su linea adjudicada (clase y razon): 48 | distintos o sin linea: 0
    lineas adjudicadas de los 20: 48 | sin registro en la bitacora: []
    candidatos de la bitacora fuera de la tanda: []
    clases de los veredictos: {'SANO': 40, 'CONTINUA': 8} | de las aristas: {'CONTINUA': 7}

**Y las `7` aristas por lectura contra su fila `SOSTENGO` de `.v64ext/aristas_lectura.txt`:**

    $ python .v65aud/normal/aristas_contra_lectura.py
    IGUAL    rehacer_flujo_paso_limitante_capacidad           > equilibrar_capacidad_personal_inventario_plazo   paso 4  | fila 12 | tramo de la fila: madre pasos 2 a 4, hijo paso 1
    IGUAL    representar_actividad_caja_negra_ventanas        > construir_indicador_linealidad_alerta_temprana   paso 8  | fila 9 | tramo de la fila: madre paso 8, hijo paso 2
    IGUAL    representar_actividad_caja_negra_ventanas        > construir_indicador_tendencia_patron             paso 8  | fila 10 | tramo de la fila: madre paso 8, hijo paso 1
    IGUAL    elegir_fabricar_pedido_pronostico                > casar_flujo_fabricacion_flujo_ventas             paso 4  | fila 7 | tramo de la fila: madre pasos 4 a 7, hijo paso 1
    IGUAL    construir_grafico_escalonado_pronosticos         > casar_flujo_fabricacion_flujo_ventas             paso 1  | fila 8 | tramo de la fila: madre pasos 1 a 8, hijo paso 12
    IGUAL    elegir_indicador_salida_trabajo_administrativo   > dimensionar_plantilla_administrativa_pronostico  paso 4  | fila 5 | tramo de la fila: madre pasos 1 a 7, hijo paso 1
    IGUAL    dimensionar_inventario_materia_prima_reposicion  > decidir_aceptar_rechazar_material_defectuoso     paso 3  | fila 11 | tramo de la fila: madre paso 3, hijo paso 1
    filas SOSTENGO: 8 | declaraciones de arista: 7 | iguales a su fila (razon y linea citada): 7
    SOSTENGO sin declaracion: [('construir_indicador_tendencia_patron', 'dimensionar_plantilla_administrativa_pronostico')]

**LECTURA:** los `48` veredictos son los adjudicados **letra a letra**, la de `detectar` incluida (la de
`cmd_02_detectar.sh`, `D65.4`), y las siete aristas llevan la razon de su fila y citan su linea. La octava
`SOSTENGO` es la que iba como `CONTINUA` en los veredictos y entro por ahi, **una sola vez** (`65.4.b`).
**`48` mas `7` son los `55`: la diferencia que mi apertura dejo abierta esta cerrada.** Y el `--paso` de las
cuatro con tramo cae **dentro** del tramo de su fila en las cuatro (`D65.3`).

## 64.4. **LA RELECTURA** (`1.2`, `5.1`, `6.1`, `7`)

### 64.4.a. **SUS CUATRO DISCUTIBLES**

| | el suyo | adjudico | por que |
|---|---|---|---|
| `D65.1` | cada `insertar` lanzado por `.v65ext/insertar.py` como un proceso, y el extractor bloqueado en `.v65ext/esperar.py` hasta su `.fin` | **SE SOSTIENE. ES PRIMER PLANO EN LO QUE LA REGLA PROTEGE** | el mandato del arnes da su motivo: *una insercion que sobrevive a su turno muere a medias*. Medido: las `20` en fila, **ninguna arranca antes de que acabe la anterior**, las `20` con su `.fin` en `0`, y el cerrojo del dataset suelto al cerrar (debajo). El tope de `10` minutos de la herramienta no deja otra manera de esperar `39` |
| `D65.2` | las siete aristas con `--veredicto CONTINUA` y su cita | **SE SOSTIENE** | `forja.py arista` exige los dos campos, y el cruce con el que la `ACTA 63` adjudico las filas lee `SOSTENGO` como `CONTINUA` (`.v64aud/normal/cruce_clases.py` linea `59`) |
| `D65.3` | el `--paso` de las cuatro filas con tramo | **SE SOSTIENE** | las cuatro eligen dentro del tramo de su fila (`64.3`) el paso cuyo producto usa el hijo, y pegan el texto del paso elegido |
| `D65.4` | la linea de `detectar` tomada de `cmd_02_detectar.sh` | **SE SOSTIENE** | la manda el encargo, y el texto que entro es el adjudicado (`64.3`) |

    $ python .v65aud/normal/solape.py | tail -1
    insertar: 20 | que arrancan antes de que acabe el anterior: 0
    $ ls .v65ext/insertar_*.fin | wc -l; cat .v65ext/insertar_*.fin | sort | uniq -c
    20
         20 0

(Fila a fila, con inicio, fin y hueco, en `.v65aud/normal/solape.txt`.) **`4` de `4` SE SOSTIENEN. CERO
CAIDAS SUYAS, DENTRO NI FUERA DEL MARCADO.**

### 64.4.b. **MIS `17` FILAS CIEGAS CONTRA LO QUE ENTRO EN LA BITACORA**

Mi apertura publico `17` filas (`14` ciegas de verdad y tres con la clase sabida, `APERTURA_CIEGA.md` `7`),
todas SANO, y **ninguna afirmacion sobre lo que la bitacora dice**. Solo clases primero:

    $ python .v65aud/normal/ciega_contra_bitacora.py | tail -1
    filas ciegas: 17 | coinciden con la bitacora: 17 | discrepan: 0

**Y SOLO DESPUES LAS RAZONES DE MIS DOS DUDAS** (`python` sobre las lineas de la bitacora, sin fichero):

| par | mi duda | su razon | queda |
|---|---|---|---|
| `emparejar_indicadores` con `elegir_cinco_indicadores` | el paso `8` de los cinco es semilla de lo que L31 hace principio, pero no lo procedimenta | *parrafos seguidos, L29 y L31, y objetos distintos... El vecino no empareja nada ni el candidato elige los datos del dia* | **SANO, las dos lecturas por el mismo sitio.** No hay discrepancia |
| `dimensionar_plantilla` con `elegir_cinco_indicadores` | el paso `1` de la plantilla es el procedimiento de `elegir_indicador_salida`, no el de los cinco | *el paso 1 del candidato pide los indicadores de una unidad ADMINISTRATIVA, que es lo que despliega elegir_indicador_salida_trabajo_administrativo y no este vecino* | **SANO, y la razon es la mia casi palabra a palabra**, escrita por el sin verla |

**CERO DISCREPANCIAS ENTRE MI PAGINA SELLADA Y LA BITACORA.** El dentro contra fuera del marcado no tiene
casos: ni una caida en ningun lado.

### 64.4.c. **LA MUESTRA PINEADA DE LOS SANO** (`7`), con la semilla que registre en la fase ciega

    $ python .v65aud/muestra_sano.py
    lineas de la 65: 55 | SANO: 40 | muestra: 8 | semilla 65
    linea 761  emparejar_indicadores_efecto_contraefecto | elegir_fabricar_pedido_pronostico
    linea 767  construir_indicador_tendencia_patron | construir_grafico_escalonado_pronosticos
    linea 777  archivar_indicadores_resolver_problemas | construir_indicador_tendencia_patron
    linea 779  archivar_indicadores_resolver_problemas | vencer_sindrome_grupo_pares_autoconfianza
    linea 780  archivar_indicadores_resolver_problemas | cerrar_brecha_dos_preguntas_estrategia
    linea 785  dimensionar_plantilla_administrativa_pronostico | elegir_fabricar_pedido_pronostico
    linea 788  dimensionar_plantilla_administrativa_pronostico | emparejar_indicadores_efecto_contraefecto
    linea 794  elegir_inspeccion_barrera_monitorizacion | construir_grafico_escalonado_pronosticos

**Releidos con los pasos de los dos delante** (`python .v64aud/pasos.py <a> <b>`, salidas en
`.v65aud/normal/pasos_muestra_a.txt` y `pasos_muestra_b.txt`) **y solo despues su razon.** Lo digo con su
limite: la `767` es `D64.5`, ya adjudicada en la `ACTA 63`; la `767`, la `777`, la `779` y la `780` estan en los
bloques de `veredictos_listos.txt` que abri antes de leer en la fase ciega (`APERTURA_CIEGA.md` `7`), y la `761`
tambien, leida desde el otro lado en el bloque de `elegir_fabricar`; la `788` es una de mis `17`. **Solo la `785`
y la `794` las leo sin haber visto su clase: el resto es relectura.**

| linea | lo que decide, por `6.1` | queda |
|---|---|---|
| `761` | empareja indicadores con su contraefecto contra elegir como se controla la salida; el inventario es ejemplo en los dos y procedimiento en ninguno | **SANO** |
| `767` | el escalonado compara pronosticos sucesivos entre si; la tendencia mide la salida real contra el tiempo y un patron. El paso `4` del escalonado **compara** con el grafico de tendencia, no lo usa | **SANO, hermanos** |
| `777` | archivar todos los indicadores para repasarlos cuando algo falla contra montar una ventana concreta | **SANO** |
| `779`, `780` | ajenos: autoconfianza del grupo de pares, y las dos preguntas de la estrategia | **SANO** |
| `785` | el paso `4` de la plantilla pronostica y ajusta la salida administrativa; el vecino elige entre fabricar contra pedido o contra pronostico. **Su paso `9` (contratar titulados contra necesidad prevista) es lo mas cercano, y es otra decision**: cuando contratar, no cuanta gente cabe en una unidad. Nombrar el pronostico no es usar el procedimiento del vecino | **SANO**, la mas delgada de las ocho |
| `788` | plantilla contra emparejar efecto y contraefecto: ningun paso compartido | **SANO** |
| `794` | inspeccion de barrera o de monitorizacion contra pronosticos sucesivos | **SANO** |

    $ python .v65aud/normal/banda_muestra.py
    SANO de la vuelta: 40 | sin razon escrita: 0
    releidos 8 | se sostienen 8 | caen 0 | tasa 0.0 por ciento | banda Wilson 95: 0.0 a 32.4 por ciento

**`8` de `8` SE SOSTIENEN, TASA `0` CON BANDA DE `0` A `32,4` POR CIENTO**, y **ningun SANO sin razon escrita**
(`D.8`). La banda es ancha porque la muestra es de ocho, y se publica asi.

## 64.5. **`PASOS INVENTADOS POR CAPITULO`, SOBRE LO QUE ENTRO** (`8`, `8.2`, `8.3`)

**Los pasos los conte yo del lado del grafo** (`.v65aud/entra_lo_leido.py`, `APERTURA_CIEGA.md` `3`), y su
tabla coincide con la del extractor en las dos filas; **la relectura de los TRANSCRIPCION no es muestra**:
son las lecturas enteras ya adjudicadas (`ACTA 62` `62.5` y `62.6`, `ACTA 63` `63.3.a` y `63.5`) sobre los
mismos bytes que entraron, mas mi relectura de corrido de los `158` pasos en la fase ciega, que no encontro
ningun PUENTE en la version que entro.

    $ python .v65aud/entra_lo_leido.py | tail -4
    capitulo  cand pasos    P   por100
    cap_02       7    50    4     8.00
    cap_03      13   108    2     1.85
    tanda       20   158    6     3.80

| capitulo | que es | pasos que entraron | PUENTE | por ciento |
|---|---|---:|---:|---:|
| `cap_02` | Cap. 1, *The Basics of Production*: el flujo de la fabrica de desayunos, el paso limitante y la inspeccion | `50` | `4` | **`8,00`** |
| `cap_03` | Cap. 2, *Managing the Breakfast Factory*: indicadores, pronosticos, inspeccion; sin las filas `21` y `22` | `108` | `2` | **`1,85`** |

**LOS DOS POR DEBAJO DEL `10`: no se baja escalon** (`8.1`). El peor capitulo es `cap_02`, y sus cuatro PUENTE
son los de `equilibrar`, de clausula, **reescritos antes de entrar**: ninguno entro al grafo sin corregir
(`8.4`).

**LA APERTURA DE LOTE (`D.32`) YA NO APLICA:** el cierre de la campania (`docs/loop/paradas/2026-09-24-cierre-de-la-campania-DECISION.md`,
punto `3`) fija que despues de Marquet no hay libro siguiente. **No mido condiciones de apertura de nada.**

## 64.6. **LAS CUATRO GUARDAS DE DATO** (`D.55`)

| guarda | estado | medida |
|---|---|---|
| `gate` | **VERDE** | `366`, `13` guardas (`64.1`) |
| el cerrojo (`D.44`) | **VERDE**: el huerfano del dataset lo rompio y lo declaro el primer `insertar` (linea `7` de su salida), cada `insertar` solto el suyo, y hoy `procesos/` esta vacio | `64.2`, `64.4.a`, `APERTURA_CIEGA.md` `9`. **El reporte no publica ninguna guarda mordiendo**, asi que no hay mutacion que re correr (`5.5`) |
| censo no decreciente | **VERDE** | dentro del gate, `366` contra `346` |
| fidelidad `D.30` con puente | **VERDE** | los seis PUENTE entraron reescritos (`64.5`) |

**NO DEJO NINGUNA TAREA BLOQUEANTE.** El rojo de `64.1` es del tallado (`D.41`), que no es guarda de dato.

## 64.7. **EL CREDITO DE LA LINEA `serial`** (`5.3`, `D.48`)

| especie | tanda `ACTA 64` | racha | el motivo, medido |
|---|---|---|---|
| **`CLASE`** | **LIMPIA** | `0 de 2` | `48` veredictos iguales a los adjudicados (`64.3`), mis `17` filas coinciden (`64.4.b`), la muestra `8` de `8` (`64.4.c`) |
| **`CIFRA PUBLICADA`** | **LIMPIA** | `0 de 2` | lo que escribio en sede duradera son `20` nodos con los bytes de su lectura entera, `55` lineas de bitacora y las `84` filas de `censos/denominaciones.md` que escribe la aduana; ninguna cifra suya en `docs/` fuera del reporte |
| **`DATO MOVIDO`** | **LIMPIA** | `0 de 2` | el dato se movio por `20` inserciones con veredictos bien puestos, y desde `d122a40` cero lineas de diff (`64.1`) |
| **`REPORTE`** | **LIMPIA** | **de `1 de 3` a `0 de 3`** | `64.2`: `R5` cumplido y ninguna afirmacion falsa |
| **`AUDITOR`** | **LIMPIA** | `0 de 3` | `64.9` |

    $ python forja.py credito | sed -n '5,13p'
      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA 64
      CIFRA PUBLICADA    0 de 2     ACTA 64
      CLASE              0 de 2     ACTA 64
      DATO MOVIDO        0 de 2     ACTA 64
      REPORTE            0 de 3     ACTA 64

      CREDITO ENTERO: ninguna especie en su tope.

**LAS CINCO RACHAS DE LA SERIAL EN CERO.**

## 64.8. **EL COSTE** (`D.55`)

    $ grep -n 'listo (USD' docs/loop/loop.log | tail -2
    5233:[2026-09-23 20:04:02] extractor listo (USD 9.115550599999999), 30381s, intento 1 de 7
    5254:[2026-09-23 23:53:36] auditor ciego listo (USD 7.321725999999996), 7398s, intento 1 de 7

**Ninguno pasa de `10` USD.** El reloj si es la cifra que pesa: **`30381` s de extractor, `27644` de ellos de
aduana** (`65.4.d`), y `7398` s de mi fase ciega, casi todo el barrido de los `20` cinco a la vez.

## 64.9. **MI PROPIA TANDA** (`D.38.2`)

**Mi apertura sellada no pierde ninguna discrepancia**: las `17` filas coinciden, la hipotesis de los `48`
contra `55` era cierta, y todas sus cifras salen de un instrumento corrido en la fase ciega y cuadran con
las del extractor (`20`/`20` iguales, `8,00` y `1,85`, `12`/`11`/`1` aristas, `48` pares).

**LO QUE SI ES MIO, Y LO DECLARO CON MI NOMBRE: LA TABLA DE LA LINEA `270` DE MI APERTURA TUMBA EL CIERRE
ESTRICTO** (`64.1`). **No es cifra falsa**: sus celdas son ciertas y su ruta existe. **Es la forma**: escribi
la ruta del `.tsv` en la frase que precede a una tabla de lectura, y el tallador la toma por declaracion de
instrumento. **Por eso no la cuento en mi racha**: un remedio sobre formato de artefactos es tarea del
arnes (`5.5` acotado el `12` sep, y `D.33`), no sustancia de auditoria. **Pero tiene coste para el
siguiente, y lo pago yo con dos cosas:**

1. **`d167`** en `docs/loop/DEUDA.jsonl`: el cierre estricto del extractor talla la apertura del auditor
   anterior, porque en una vuelta de insercion el extractor cierra antes de que haya apertura nueva.
2. **El encargo de la `66` avisa al extractor** de que su `cerrar_reporte.py` saldra en rojo por esa linea y
   solo por esa, y que se pega y se declara **sin tocar `APERTURA_CIEGA.md`**, cuyo sello no es suyo.

**Y UN REGISTRO MIO QUE REHICE ANTES DE COMMITEARLO:** mi primer intento de escribir el credito de esta tanda
llevaba en las citas el resultado y no la referencia; el instrumento rechazo la de `CLASE` por `D.56` y
dejo pasar las otras cuatro. **Borre mis cuatro lineas sin commitear y escribi las cinco con la cita
desnuda** (`ACTA 64, seccion ...`), porque la fase ciega lee ese registro y un resultado copiado ahi la
contamina. No habia texto publicado que corregir.

**`AUDITOR` SIGUE EN `0 de 3` POR TANDA LIMPIA** (`5.4`, correccion del `16` sep), no por indulto mio.

## 64.10. **LAS CONDICIONES DE PARADA, UNA A UNA** (`3`)

| condicion | se cumple | como lo mido |
|---|---|---|
| doctrina nueva | **NO** | los cuatro discutibles los deciden el motivo escrito del mandato de insercion, `forja.py arista` y la `ACTA 63`; los pares, `6.1`. Nada abre cola (`D.55`) |
| contradiccion | **NO** | ninguna cifra publicada queda desmentida |
| decision de Alexis | **NO** | la insercion de Grove esta autorizada (`DOS SEMANAS` punto `4`, cierre de la campania punto `4`) |
| fallo tecnico repetido | **NO** | gate, guiones y `379` pruebas en verde; el rojo del cierre estricto es de mi pagina y es la primera vez (`d167`) |
| credito roto | **NO** | las cinco rachas en cero (`64.7`) |
| campania consumada | **NO** | Grove tiene `71` en la bandeja, Gerber `22` y Marquet `20` (`64.1`) |

    $ python scripts/deuda.py --clase 66
    LIBRE
      van 2 de 5 desde la ultima de saneamiento (la 64), con 57 deuda(s) esperando

(Las `57` ya cuentan la `d167` de `64.9`.)

**NO ESCRIBO `PARA_ALEXIS.md`.** La `66` es **LIBRE**, y la uso para las dos filas que Grove tiene listas y para
dejar listo lo siguiente del libro, que es `cap_04` entero:

    $ python .v65aud/normal/cola_grove.py | head -1
    en la bandeja: 71 | por capitulo de UNIDAD DE ORIGEN: cap_03 2, cap_04 22, cap_05 12, cap_06 8, cap_07 9, cap_10 1, cap_11 2, cap_12 3, cap_13 2, cap_14 3, cap_15 3, cap_16 1, cap_17 3

**POR QUE PREPARAR Y NO INSERTAR `cap_04` EN LA `66`:** es el mismo camino que llevo a la `65` a entrar limpia
(la `64` dejo la fidelidad leida y los veredictos escritos, la `ACTA 63` los adjudico, la `65` inserto sin una
sola sorpresa), y **una fidelidad que se adjudica despues de insertar deja un PUENTE en el grafo si cae.**
Con `22` en el capitulo, **la tanda de insercion de la `67` son las `20` primeras de su orden** y las dos que
queden pasan a la `68`.

## 64.11. **LOS REMEDIOS**

| # | de quien | remedio | donde se comprueba |
|---|---|---|---|
| `R5` | del extractor | **Sigue vivo con su letra**, porque se cumplio una vez despues de romperse una: un bloque `$` contiene lo que el comando imprimio y nada mas; si se corta, por el final y dentro del bloque `(recortado, entero en <fichero>)`; un comando que imprime algo no queda sin ninguna linea debajo. **Y un bloque de apertura que el instrumento marque porque el estado se movio despues se declara reproducido contra el commit de apertura, como hizo la `65`** | el reporte de la `66`, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py`, los dos con la cabecera del tramo cambiada a la `66` |

**No me escribo remedio**: mi tanda es limpia y lo de la linea `270` es forma, anotado en `d167`.

## 64.12. **LO QUE ANOTO AL CERRAR**

- **`docs/loop/DEUDA.jsonl`**: `d167`, el cierre estricto que talla la apertura del auditor anterior.
- **`docs/loop/CREDITO_serial.jsonl`**: las cinco lineas de la tanda `ACTA 64`, todas `--limpia`.
- **`docs/loop/PROMPT_SIGUIENTE.md`**: el encargo de la vuelta `66`, **INSERCION** de las filas `21` y `22` y
  preparacion de `cap_04` entero.
- **`.v65aud/`**: mi evidencia de las dos fases, commiteada con `docs/loop/`.
