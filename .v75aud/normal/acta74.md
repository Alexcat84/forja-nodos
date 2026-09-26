
# ACTA 74. VUELTA 75, lote 7 (`grove_high_output`), **CLASE INSERCION**: **LA BLOQUEANTE SE CUMPLE EN SU LETRA Y EN SU ORDEN: LOS PASOS `8` Y `17` DE `dar_elogio` FUERA DEL CAMPO, CON SU CORRECCION DECLARADA, Y LA GUARDA `D.30` VUELVE A VERDE. LAS `7` ULTIMAS DE GROVE ENTRAN UNA POR VEZ, SIN SOLAPE, EN SU ORDEN Y CON LOS BYTES QUE SE LEYERON; SUS `29` LINEAS SON LAS PREPARADAS LETRA A LETRA, LOS PARES DE MI BARRIDO Y MIS CLASES SELLADAS, Y SUS `3` ARISTAS SON MIS `3`, POR LOS DOS LADOS. GROVE QUEDA ENTERO EN EL GRAFO. SUS CUATRO DISCUTIBLES SE SOSTIENEN, LA MUESTRA TAMBIEN, CERO CAIDAS SUYAS Y `REPORTE` VUELVE A CERO. UNA CIFRA MIA FALSA EN EL ENCARGO DE LA `75`: `AUDITOR` SUBE A `1 de 3`. LA `76` PREPARA GERBER**

*Auditor `claude-opus-5-5`, 26 sep 2026, turno normal de la vuelta que el arnes numera `4` en la corrida que arranco el 25 a
las `21:43`. Linea **serial**, rama `extraccion-mundo-11`, hash auditado `d02ed21` (cierre del extractor, mas `7a8cd24` con la
salida del hook, sin trabajo nuevo), arbol en `34427e3` con mi apertura sellada. Modo austero (`D.47`). Toda mi evidencia de
este turno esta en `.v75aud/normal/`, y la de mi fase ciega en `.v75aud/`.*

## 74.0. **HUECO DE ACTA Y HERENCIA** (`1.0`, `D.40`)

**NO HAY HUECO.** La `ACTA 73` cubre la vuelta `74`; esta cubre la `75` entera: el turno del extractor (de `9a5151a` a `7a8cd24`,
`04:30` a `06:03` del 26) y mi fase ciega, sellada en `34427e3`, que solo toca sus dos ficheros:

    $ git diff --name-only 7a8cd241 34427e31
    docs/loop/APERTURA_CIEGA.md
    docs/loop/SELLOS_APERTURA.jsonl

(Sale de `.v75aud/normal/censo_git.txt`, con el resto de lo que la vuelta movio, en `74.1`.)

**HEREDADO 1, la TAREA BLOQUEANTE de mi `ACTA 73` `73.6`: CUMPLIDA.** Por el dato en mi fase ciega (`APERTURA_CIEGA.md` `0` y `3`),
y ahora **con `git`**, que es lo que aquella fase no pudo medir: el grafo antes de la TAREA `2` (`3253122`) contra su commit
(`4a5d2b2`), nodo a nodo:

    $ python .v75aud/normal/t2_git.py
    nodos antes: 430 | despues: 430 | nuevos: 0 | que desaparecen: 0 | que cambian: 1 {'dar_elogio_disciplina_igual_critica': ['pasos_accionables', 'resumen_teorico']}
    pasos antes 20 | despues 18 | el resumen viejo entero al principio del nuevo: True | caracteres 5382 > 9390
    los de despues son los de antes sin el 8 y sin el 17: True

**Es lo que su `75.2.3` publica y no se podia volver a correr** (lo dice el mismo al final de `75.5.f`). El `gate` despues de cada
una de las tres operaciones esta en sus tres salidas guardadas, una por operacion:

    $ grep -c -F "GATE VERDE." .v75ext/t2_op1_corregir.txt .v75ext/t2_op2_retirar17.txt .v75ext/t2_op3_retirar8.txt
    .v75ext/t2_op1_corregir.txt:1
    .v75ext/t2_op2_retirar17.txt:1
    .v75ext/t2_op3_retirar8.txt:1

**LECTURA:** los intermedios no los reproduzco yo (un solo commit cubre las tres operaciones); lo que si mido es que el grafo del
commit es el de antes con solo esos dos pasos fuera y el resumen alargado, y que **el orden fue `corregir`, `17`, `8`** (mi fase
ciega, `APERTURA_CIEGA.md` `3`, punto `(3)`). **La TAREA `2` se commiteo a las `04:37:58` y el primer `insertar` arranco a las
`04:42:30`** (`74.3`): ninguno antes de cerrarla. **La `--razon` de `corregir`** es la linea `1082` de la bitacora, y cita `73.5` y
`73.6` (`74.3`, punto `(0)`).

**HEREDADO 2, `R5` del extractor: CUMPLIDO.** Con mis copias sacadas con `sed` de los originales `.v64ext/pegado64.py` y
`.v64aud/normal/bloques_mudos.py`, no de las suyas, con la cabecera cambiada a la `75` (`3` y `2` lineas nuevas contra el original
con `diff --strip-trailing-cr`):

    $ cat .v75aud/normal/r5.txt
    bloques abiertos con `$` en el tramo de la vuelta 75 : 60
    bloques que ROMPEN R1 (ACTA 60 60.15)                : 0
    bloques abiertos con `$`: 28 | comandos `$`: 60 | comandos sin ninguna linea de salida en su bloque: 0

**Es lo que su `75.5.f` publica, al digito.** **HEREDADO 3, `R6`, y HEREDADO 4, `R7`, mios: CUMPLIDOS** en la fase ciega
(`APERTURA_CIEGA.md` `0` y `9`) **y `R7` en esta acta**. **HEREDADO 5, `R8`, mio: CUMPLIDO en el encargo de la `75`**
(`APERTURA_CIEGA.md` `7`) **y medido sobre el de la `76`** en `74.12`. **HEREDADO 6, `R9` del extractor: CUMPLIDO en su letra**:
su `grep` sobre los `18` pasos que quedan, con cada coincidencia y su tramo literal (`75.2.4`); **el cruce con el mio, en `74.4`.**

## 74.1. **LO QUE VERIFICO, CON MIS PROPIOS COMANDOS** (`1.1`)

    $ cat .v75aud/normal/gate.txt .v75aud/normal/guiones.txt .v75aud/normal/resolutor.txt
    GATE VERDE.
      nodos verificados: 437
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece
    rc=0
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    rc=0
    nodos vivos: 437
    nodos deprecados (archivo): 0
    alias registrados: 0
    rc=0
    $ grep 'total:' .v75aud/normal/suite.txt; tail -1 .v75aud/normal/suite.txt
      total: 379 pruebas, 0 fallos, 0 errores
    rc=0
    $ cat .v75aud/normal/censo.txt
    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        437 dataset/nodos.jsonl
       1111 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1549 total
    $ for d in cuarentena/grove_high_output cuarentena/_insertados/grove_high_output cuarentena/gerber_emyth cuarentena/marquet_turn_the_ship; do echo "$d $(find $d -maxdepth 1 -name "*.json" | wc -l)"; done; echo "procesos $(ls -A procesos/ | wc -l)"
    cuarentena/grove_high_output 0
    cuarentena/_insertados/grove_high_output 92
    cuarentena/gerber_emyth 22
    cuarentena/marquet_turn_the_ship 20
    procesos 0
    $ python .v70aud/poblacion.py
    poblacion: 479 | por sede: {'grafo': 437, 'bandeja': 42} | suma: 479

**Y CON `git`**, desde mi encargo de la `75` (`702ee04`) hasta el ultimo commit del extractor, las fichas agrupadas por carpeta:

    $ cat .v75aud/normal/censo_git.txt
    $ git diff --name-only 702ee04d 7a8cd241 | grep -v "^\.v75ext/" | sed "s|/[^/]*\.json$|/*.json|" | sort | uniq -c
          1 bitacora/VEREDICTOS.jsonl
          1 censos/denominaciones.md
          7 cuarentena/_insertados/grove_high_output/*.json
          1 dataset/nodos.jsonl
          2 docs/loop/*.json
          1 docs/loop/loop.log
          1 docs/loop/REPORTE.md
    $ git diff --name-only 7a8cd241 34427e31
    docs/loop/APERTURA_CIEGA.md
    docs/loop/SELLOS_APERTURA.jsonl
    $ git log --format=%h 702ee04d..7a8cd241 -- dataset/nodos.jsonl | wc -l
    8
    $ git status --short -- dataset bitacora censos config esquema fuentes src scripts tests cuarentena forja.py | wc -l
    0

**LECTURA:** **el censo de su `75.5.a` al digito** (`437`, `1111`, `1`, `0`, `92`; poblacion `479`, `437` mas `42`), **y el de mi
apertura sellada**. **Ni `src/`, ni `scripts/`, ni `config/`, ni `esquema/`, ni `fuentes/`, ni `tests/`**, ni las bandejas de Gerber
y de Marquet cambian; **ocho commits tocan el grafo, la TAREA `2` y las siete filas**; nada queda sin commitear en el dato.

**EL CIERRE ESTRICTO, CORRIDO POR MI:**

    $ grep -nE '^(CIERRE|CENSO|TALLADO|TABLA DE CIERRE)|DIFIEREN|CAEN  ' .v75aud/normal/cerrar_reporte.txt; tail -1 .v75aud/normal/cerrar_reporte.txt
    2:TALLADO DEL REPORTE (D.41): la tabla que dice ser de instrumento
    6:  que DIFIEREN de su instrumento: 0
    263:TALLADO VERDE: las 157 tabla(s) comprobables son las de su instrumento, celda a celda.
    265:CENSO DE RUTAS (D.42): la unidad de la ruta es la celda
    269:  CAEN                      : 0
    275:CENSO VERDE: las 1049 rutas publicadas sostienen lo que dicen sostener.
    277:TABLA DE CIERRE DE TAREAS (D.52): toda tabla del reporte declara su instrumento
    287:TABLA DE CIERRE VERDE: ninguna celda medible difiere del dato.
    1075:CIERRE VERDE: las cuatro guardas que muerden, el tallado y el censo. La vigencia corrio y publico su cuenta arriba: es cola, no guarda (D.15).
    rc=0

**VERDE, `rc=0`**, y `procesos/` vacio despues de mi suite y de mi cierre (bloque de arriba). Cuenta `1049` rutas contra `1045` de su
corrida y `1050` de su hook: **no descompongo la diferencia**, el arbol no es el mismo (despues entro mi apertura), y ninguna cae.

**LO QUE REPRODUZCO DE SU TRAMO**, corriendo sus instrumentos contra sus salidas guardadas con `diff`:

    $ cat .v75aud/normal/reproduce.txt
    aristas_vuelta.py: IDENTICO a .v75ext/aristas_vuelta.txt
    nodos_viejos.py: IDENTICO a .v75ext/nodos_viejos.txt
    veredictos_vuelta.py: IDENTICO a .v75ext/veredictos_vuelta.txt
    pasos_inventados.py: IDENTICO a .v75ext/pasos_inventados.txt
    cap13_scott.py: IDENTICO a .v75ext/cap13_scott.txt
    r9.py: IDENTICO a .v75ext/r9.txt
    contra_barrido.py 01 usar_banco_nueve_preguntas_entrevista: IDENTICO a .v75ext/contra_01.txt
    contra_barrido.py 02 responder_primer_aviso_renuncia_subordinado: IDENTICO a .v75ext/contra_02.txt
    contra_barrido.py 03 gestionar_retencion_subordinado_valioso_renuncia: IDENTICO a .v75ext/contra_03.txt
    contra_barrido.py 04 reciclar_empleado_ascendido_mas_alla_capacidad: IDENTICO a .v75ext/contra_04.txt
    contra_barrido.py 05 priorizar_lista_entrenamiento_subordinados: IDENTICO a .v75ext/contra_05.txt
    contra_barrido.py 06 desarrollar_primer_curso_entrenamiento: IDENTICO a .v75ext/contra_06.txt
    contra_barrido.py 07 pedir_critica_anonima_curso_entrenamiento_dictado: IDENTICO a .v75ext/contra_07.txt

## 74.2. **EL REPORTE, AFIRMACION POR AFIRMACION** (`5.2`)

| afirmacion del reporte | sale | sede | especie |
|---|---|---|---|
| `75.0`: el censo de apertura, `procesos/` vacio, `LIBRE`, poblacion `479`, huellas identicas; **y la discrepancia `51` contra `52` deudas, declarada con su causa** | **cierta, y la discrepancia es mia** (`74.9`) | bloque | |
| `75.1`: los registros de la `ACTA 73` | **cierta** | tabla | |
| `75.D`: `D75.1` y `D75.2`, marcados antes de ejecutar | **cierta** (`74.5`) | tabla | |
| `75.2.1` y `75.2.2`: `corregir` una vez y antes, despues el `17` y el `8`, `gate` verde tras cada una, el `8` seguia siendo el `8` | **cierta** (`74.0`; mi fase ciega, `APERTURA_CIEGA.md` `3`) | bloques | |
| `75.2.3`: un solo nodo cambia, en dos campos; `18` pasos; la tabla de numeros; bitacora `1081` a `1082` | **cierta** (`t2_git.py`, `74.0`; `74.3`) | bloque | |
| `75.2.4`: `R9`, `6` pasos casan y los `6` traen su tramo literal; `D75.3` | **cierta** (`r9.py` reproducido, `74.1`; cruce en `74.4`) | bloque y tabla | |
| `75.3`: las `7` fichas con la huella de la `73`; `dar_elogio` no es vecino de ninguna | **cierta** (mi fase ciega, `APERTURA_CIEGA.md` `2`: las `7` con la huella de mi barrido) | bloque | |
| `75.4`, filas `1` a `7`: su aduana, sus vecinos, sus lineas, sus aristas y sus commits | **cierta, fila a fila** (`74.3`, y los `7` `contra_barrido.py` reproducidos) | tablas | |
| `75.4.a`: `3` aristas esperadas en el grafo, `0` en cola, `30` lineas con razon, ningun viejo cambiado fuera de la TAREA `2` | **cierta** (`74.3`; y mi fase ciega, `APERTURA_CIEGA.md` `2`, `(c)`) | bloques | |
| `75.5.a`: el censo antes y despues de cada tarea | **cierta** (`74.1`) | tabla | |
| `75.5.b`: `0` PUENTE que entro en los tres capitulos; `cap_13` de Scott en `2` marcados y `0` vivos | **cierta** (`74.4`) | tablas | |
| `75.5.c` a `75.5.f`: `D.61` sin abiertos, guardas, cierre estricto verde a la primera, `R5` | **cierta** (`74.0`, `74.1`, `74.5`) | bloques y tabla | |
| cabecera y tabla de cierre: `T1` a `T5` `CERRADA` con sus cifras | **cierta, celda a celda** contra `74.1`, `74.3` y `74.4` | **CABECERA y TABLA** | |

**Ninguna caida.** Y una cosa que hizo bien y se dice: **la discrepancia de `75.0` la cazo el, con su causa y su hora**, y era mia.

## 74.3. **LAS `30` LINEAS NUEVAS, LAS ARISTAS Y EL ORDEN, PAR A PAR** (`APERTURA_CIEGA.md` `8`, puntos `3`, `4` y `6`)

Cada linea nueva de la bitacora contra las lineas vivas preparadas de `.v73ext/veredictos_listos.txt`, contra **mi** barrido
sellado de la `73` (`.v73aud/vecinos_<id>.json`) con sus seniales, y contra **mis** clases selladas con la correccion de la `ACTA 72`
`72.5` (`D73.9`):

    $ python .v75aud/normal/cruce_bitacora.py
    lineas de la bitacora: 1111 | nuevas desde la 1082: 30
    nuevas por tipo: {'correccion declarada del resumen_teorico (EXTRACTOR.md 2)': 1, 'veredicto': 29} | suma: 30
    (0) linea de operacion: candidato dar_elogio_disciplina_igual_critica | caracteres 5382 > 7719 | huellas e61505b50710934d > 6bdd3603854e9f2b | la razon cita 73.5 y 73.6: SI | texto_anadido 2336 caracteres
    (1) veredictos contra .v73ext/veredictos_listos.txt: {'igual letra a letra a una linea preparada': 29} | suma: 29
        lineas vivas preparadas: 29 | usadas: 29 | usadas dos veces: 0
    (2) veredictos contra mi barrido sellado de la 73: {'par de mi barrido, seniales, levantada_por y detalle iguales': 29} | suma: 29
        filas dirigidas de mi barrido: 29 | sin linea en la bitacora: 0 []
    (3) clase contra mis clases selladas, con la 72.5 (D73.9): {'igual clase y madre': 29} | suma: 29
        pares sin orden en la bitacora: 20 | en mis clases: 20
        aristas distintas en las nuevas: 3

Las aristas del grafo que tocan la tanda, **con sus ids y por los dos lados**, contra las `3` de mi fase ciega (`APERTURA_CIEGA.md` `5`):

    $ python .v75aud/normal/aristas_grafo.py
      desarrollar_primer_curso_entrenamiento > pedir_critica_anonima_curso_entrenamiento_dictado | en siguientes de la madre: SI | en previos del hijo: SI
      priorizar_lista_entrenamiento_subordinados > desarrollar_primer_curso_entrenamiento | en siguientes de la madre: SI | en previos del hijo: SI
      responder_primer_aviso_renuncia_subordinado > gestionar_retencion_subordinado_valioso_renuncia | en siguientes de la madre: SI | en previos del hijo: SI
    de las 7 en el grafo: 7 | aristas del grafo que tocan la tanda: 3 | declaradas por los dos lados: 3
    esperadas: 3 | en el grafo: 3 | en el grafo y no esperadas: 0 | esperadas y no en el grafo: 0

Los `7` `insertar`, por sus ficheros, y el orden de los commits de la vuelta:

    $ python .v75aud/normal/solape.py
    insertar: 7 | con codigo 0: 7 | con otro codigo: 0 | suma: 7
    solapes entre consecutivos: 0 | primer inicio 2026-09-26 04:42:30 | ultimo fin 2026-09-26 05:48:32
    $ sed -n '1,4p;17,19p' .v75aud/normal/orden_commits.txt | cut -c1-100
    4a5d2b2d 2026-09-26T04:37:58-04:00 Vuelta 75, T2 (bloqueante D.55): dar_elogio_disciplina_igual_critica, corr
    c6eddc1f 2026-09-26T04:39:55-04:00 Vuelta 75, T3: las 7 fichas con la huella de la 73, y las copias del metodo
    3f83d062 2026-09-26T04:52:55-04:00 Vuelta 75, fila 1: usar_banco_nueve_preguntas_entrevista insertado por la
    5d394322 2026-09-26T04:53:17-04:00 Vuelta 75, fila 1: su fila en el reporte
    4f3f21a3 2026-09-26T05:50:51-04:00 Vuelta 75, T4: las 7 de Grove insertadas, las 3 aristas esperadas en el gra
    d02ed219 2026-09-26T06:02:07-04:00 Vuelta 75, T5: el cierre (censo 430/1081/1/7/85 al abrir y 437/1111/1/0/92
    7a8cd241 2026-09-26T06:03:07-04:00 Vuelta 75: la salida del hook del commit del cierre

**LECTURA:** **las `29` lineas de veredicto son las `29` preparadas, letra a letra y sin repetir ninguna, sobre los `29` pares
dirigidos de mi barrido con sus seniales al digito, y con mis clases selladas**: ninguna aduana levanto un vecino fuera de mi barrido
ni dejo uno sin linea. **La de `corregir` alarga el resumen de `5382` a `7719`** (la cuenta de `2337` de su salida es esa resta;
el `texto_anadido` guarda `2336`, y el que falta es el separador que `src/correccion.py` pone delante, bloque de abajo), y **las dos retiradas lo
llevan a `9390`**, que es lo que mide `t2_git.py` (`74.0`). **Las `3` aristas son mis `3`, par a par y por los dos lados**, cada
una entre dos nodos de la tanda. **Los `7` `insertar` volvieron en `0` y ninguno arranco antes de que acabara el anterior**; el
orden de entrada es el de `.v73ext/orden.txt` (mi fase ciega, `APERTURA_CIEGA.md` `5`), y el `.fin` de los siete dice `0`.

    $ grep -n 'nuevo = ' src/correccion.py; cat .v75ext/*.fin | tr '\n' ' '
    158:    nuevo = (viejo + " " + anade).strip() if viejo else anade
    0 0 0 0 0 0 0 

## 74.4. **LA FIDELIDAD, `R9` CRUZADO, Y `PASOS INVENTADOS POR CAPITULO`** (`D.30`, `D.58`, `8`, `8.2`, `8.3`)

**`R9` sobre `dar_elogio`, SU PATRON Y EL MIO SOBRE LOS MISMOS `18` PASOS**, leidos de sus ficheros y no copiados:

    $ python .v75aud/normal/r9_cruce.py
    paso  1 | suyo: mas que / y si no / mas seguro pisando el acelerador si sabes que | mio: mas que / y si no
    paso  2 | suyo: - | mio: demostrar
    paso  4 | suyo: en vez de | mio: comparaciones
    paso  9 | suyo: mas partido centrandote en las fuerzas que / en vez de | mio: -
    paso 10 | suyo: no solo / demuestra / mas de lo que | mio: no solo / demuestra
    paso 12 | suyo: igual de / lo contrario | mio: -
    paso 13 | suyo: el texto dice | mio: -
    paso 15 | suyo: - | mio: compartid
    pasos: 18 | por patron que casa: {'suyo+mio': 3, 'mio': 2, 'ninguno': 10, 'suyo': 3} | suma: 18

**LECTURA:** **entre los dos casan `8` pasos, y los `8` tienen su tramo literal pegado**: los `6` suyos en su `75.2.4`, los `2` que
solo ve el mio (el `2`, *not to prove how smart you are*, `L267`, y el `15`, *share*, `L283`) en mi `APERTURA_CIEGA.md` `3`. **No hay
puente nuevo en `dar_elogio`.** Su patron es mas ancho en comparaciones (ve el `9`, el `12` y el `13`, que el mio no); **el mio ve
*demostrar*, que el suyo no** (su `demuestr` no casa la raiz con `o`). No es caida: el paso `2` no califica ninguna prueba. **Va al
encargo de la `76`**, que marca la fidelidad de un lote entero. Los pasos de los otros dos nodos de `cap_13`, sin cambio desde la
`74`, los cubre mi `APERTURA_CIEGA.md` `3`.

**`PASOS INVENTADOS POR CAPITULO`, de lo que ENTRO**, contado por los dos lados: su instrumento reproducido (`74.1`) y **mi lectura
sellada de la `73`** en mi fase ciega (`APERTURA_CIEGA.md` `4`, `.v75aud/entra_lo_leido.py`: cada nodo del grafo igual a su ficha y
cada paso con su fila):

    $ sed -n '11,15p' .v75ext/pasos_inventados.txt
    | capitulo | candidatos que entraron | pasos | PUENTE marcados | por ciento | corregidos en la ficha | PUENTE que entro |
    |---|---:|---:|---:|---:|---:|---:|
    | `cap_15` | 3 | 22 | 5 | 22,73 | 5 | 0 |
    | `cap_16` | 1 | 4 | 0 | 0,00 | 0 | 0 |
    | `cap_17` | 3 | 16 | 1 | 6,25 | 1 | 0 |
    $ python .v75aud/entra_lo_leido.py | sed -n '4,6p' | cut -c1-110
    cap_15 lo que ENTRO: candidatos 3 | pasos 22 | mis marcas: {'T': 21, 'P': 0, 'D': 1} | suma: 22 | PUENTE 0 de 
    cap_16 lo que ENTRO: candidatos 1 | pasos 4 | mis marcas: {'T': 4, 'P': 0, 'D': 0} | suma: 4 | PUENTE 0 de 4 =
    cap_17 lo que ENTRO: candidatos 3 | pasos 16 | mis marcas: {'T': 16, 'P': 0, 'D': 0} | suma: 16 | PUENTE 0 de 
    $ for f in fuentes/grove_high_output/cap_15.md fuentes/grove_high_output/cap_16.md fuentes/grove_high_output/cap_17.md fuentes/scott_radical_candor/cap_13.md; do grep -m1 titulo_textual $f; done
    titulo_textual: Two Difficult Tasks
    titulo_textual: Compensation as Task-Relevant Feedback
    titulo_textual: Why Training Is the Boss's Job
    titulo_textual: Afterword to the Revised Edition: Rolling Out Radical Candor

| capitulo | que es | nodos que entraron | pasos | PUENTE que entro | por ciento |
|---|---|---:|---:|---:|---:|
| `cap_15` de `grove_high_output` | *Two Difficult Tasks*: la entrevista y el aviso de renuncia | `3` | `22` | `0` | `0,00` |
| `cap_16` de `grove_high_output` | *Compensation as Task-Relevant Feedback*: el ascenso que supera a la persona | `1` | `4` | `0` | `0,00` |
| `cap_17` de `grove_high_output` | *Why Training Is the Boss's Job* | `3` | `16` | `0` | `0,00` |
| `cap_13` de `scott_radical_candor`, los tres de `d084`, despues de la TAREA `2` | *Afterword to the Revised Edition: Rolling Out Radical Candor* | `3` | `68` | `0` | `0,00` |

**LECTURA:** **ningun capitulo por encima del `10`**, y **no queda lote de extraccion en el mundo `11`** (`PARALELO.md` `8` punto
`3`): la cifra no dimensiona nada. El `22,73` de `cap_15` es de la **marca** de la preparacion, **corregida en la ficha antes del
barrido** (`ACTA 72` `72.4`): es la regla funcionando (`8.4`), no una caida. Mi unica `D` de `cap_15` la adjudico `T` la `72.5`, y
es la figura de `R9` que mi fase ciega dejo escrita (`APERTURA_CIEGA.md` `4`, *el segundo pesa mas*), **ya adjudicada**: no la
reabro (`D.47`). **Los titulos de capitulo de la tabla son el `titulo_textual` de cada fichero, del bloque de arriba**; lo que va detras de los dos
puntos es LECTURA mia de lo que entro.

## 74.5. **LA RELECTURA** (`1.2`, `5.1`, `6.1`, `7`)

**SUS CUATRO DISCUTIBLES, POR NUMERO** (`D.47`):

| | su marca | adjudico |
|---|---|---|
| `D75.1` | la correccion escribe *`20` pasos, `18` y `2`* y no la cuenta de despues de retirar | **SE SOSTIENE**: es lo que el encargo pedia, y la cuenta de despues la dice el propio nodo sin afirmacion nueva: `18` pasos en el campo y los dos retirados escritos con su literal. **No hace falta una segunda correccion** |
| `D75.2` | las comillas tipograficas de las lineas pegadas | **SE SOSTIENE**: es la salida literal de `grep -n -o` (`D.35`); `gate` y `guiones` verdes (`74.1`) |
| `D75.3` | el `demuestra` del paso `10` de `dar_elogio`, leido como *shows* | **SE SOSTIENE**: `L273` dice *Praise shows that you care personally*; el paso afirma lo que el libro afirma del elogio, no califica la prueba del libro. **Lo lei igual a ciegas** (`APERTURA_CIEGA.md` `3`) |
| `D75.4` | el metodo de espera de la `72` | **SE SOSTIENE**: `7` `.fin` en `0`, `0` solapes (`74.3`), `procesos/` vacio al cerrar (`74.1`), y ningun proceso suyo vivo: el arnes abrio mi fase ciega sin nada en `procesos/` |

**DENTRO CONTRA FUERA DEL MARCADO:** cuatro marcados, **cuatro se sostienen**. **Fuera del marcado, ninguna caida**: las `29` lineas
son mis clases selladas (`74.3`), la muestra de abajo se sostiene entera, y `R9` no levanta puente (`74.4`).

**LA MUESTRA PINEADA DE LOS SANO** (`7`), semilla `75` registrada en mi fase ciega (`APERTURA_CIEGA.md` `8`, punto `5`); el tamanio es
el mayor entre `3` y el `20` por ciento redondeado hacia arriba, con techo de `20`:

    $ python .v75aud/normal/muestra_sano.py
    lineas de la 75: 30 | SANO: 23 | muestra: 5 | semilla 75
    linea 1084  usar_banco_nueve_preguntas_entrevista | responder_primer_aviso_renuncia_subordinado
    linea 1098  gestionar_retencion_subordinado_valioso_renuncia | usar_banco_nueve_preguntas_entrevista
    linea 1099  reciclar_empleado_ascendido_mas_alla_capacidad | priorizar_lista_entrenamiento_subordinados
    linea 1102  priorizar_lista_entrenamiento_subordinados | reciclar_empleado_ascendido_mas_alla_capacidad
    linea 1106  pedir_critica_anonima_curso_entrenamiento_dictado | priorizar_lista_entrenamiento_subordinados

**PRIMERO LOS PASOS, DESPUES SU RAZON.** Los de `usar_banco` y `reciclar`, en `.v75aud/normal/pasos_muestra.txt` por `pasos_ciego.py`;
los de los otros tres, en mi `APERTURA_CIEGA.md` `6`. **Mi lectura, escrita antes de destapar:**

- `1084` y `1098`: **SANO los dos.** Entrevistar a un candidato con un banco de preguntas contra atender el primer aviso de renuncia o
  retener a quien se va: condiciones distintas, y ningun paso de uno usa el producto del otro.
- `1099` y `1102`, el mismo par por sus dos lados: **SANO.** Devolver a su puesto a quien fue ascendido de mas no es entrenar; ni la
  lista ni sus prioridades aparecen en los cuatro pasos de `reciclar`, ni la vuelta atras en los de `priorizar`.
- `1106`: **SANO**, abuela y nieta: la condicion de `pedir_critica` es el curso dictado, que es producto de `desarrollar`, no de la
  lista. Es `D73.9`, adjudicado en la `ACTA 72` `72.5`.

Destapadas despues (`.v75aud/normal/razones_muestra.txt`): **las cinco razones dicen lo mismo con el libro citado.**

    $ python .v75aud/normal/banda_muestra.py
    SANO de la vuelta: 23 | sin razon escrita: 0
    releidos 5 | se sostienen 5 | caen 0 | tasa 0.0 por ciento | banda Wilson 95: 0.0 a 43.4 por ciento

**LA RELECTURA AL DOBLE** no aplica: ninguna caida de `REPORTE` en el tramo (`74.2`).

## 74.6. **LAS CUATRO GUARDAS DE DATO** (`D.55`)

| guarda | estado | medida |
|---|---|---|
| `gate` | **VERDE** | `74.1` |
| el cerrojo (`D.44`) | **VERDE**: `7` `insertar` sin solape, `procesos/` vacio | `74.1`, `74.3` |
| censo no decreciente | **VERDE**: el grafo de `430` a `437`, la bitacora de `1081` a `1111` | `74.1` |
| fidelidad `D.30` con puente | **VERDE**: los dos puentes de `dar_elogio` fuera del campo; `0` PUENTE que entro | `74.0`, `74.4` |

**Ninguna en rojo: esta acta no deja tarea bloqueante** (`D.55`).

## 74.7. **EL CREDITO DE LA LINEA `serial`** (`5.3`, `D.48`)

    $ sed -n '5,12p' .v75aud/normal/credito_abrir.txt
      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA 73
      CIFRA PUBLICADA    0 de 2     ACTA 73
      CLASE              0 de 2     ACTA 73
      DATO MOVIDO        0 de 2     ACTA 73
      REPORTE            2 de 3     ACTA 73

| especie | tanda `ACTA 74` | racha | el motivo, medido |
|---|---|---|---|
| **`CLASE`** | **LIMPIA** | `0 de 2` | las `29` lineas son mis clases selladas y la de `corregir` es la adjudicada (`74.3`); la muestra `5` de `5` (`74.5`) |
| **`CIFRA PUBLICADA`** | **LIMPIA** | `0 de 2` | no escribio en `docs/` fuera de `docs/loop/`, ni en `config/`, `esquema/` ni `src/` (`74.1`) |
| **`DATO MOVIDO`** | **LIMPIA** | `0 de 2` | movio el grafo, la bitacora, `censos/` y la bandeja **por mandato y como se esperaba**, byte a byte (`74.0`, `74.1`, `74.3`) |
| **`REPORTE`** | **LIMPIA** | **`0 de 3`** | ninguna afirmacion falsa (`74.2`): **la racha vuelve a cero** por `5.4` (*limpia* es sin caidas de la especie) |
| **`AUDITOR`** | **CAE** | **`1 de 3`** | `74.9`: una cifra mia falsa en el encargo de la `75` |

(Una linea por especie en `docs/loop/CREDITO_serial.jsonl`, al cerrar esta acta.)

## 74.8. **EL COSTE** (`D.55`)

    $ sed -n '8044p;8048p' docs/loop/loop.log
    [2026-09-26 06:03:52] extractor listo (USD 5.9120888), 5572s, intento 1 de 7
    [2026-09-26 06:17:37] auditor ciego listo (USD 5.5686724), 824s, intento 1 de 7

**Por debajo de `10` USD los dos turnos**: no hay desglose que declarar.

## 74.9. **MI PROPIA TANDA** (`D.38.2`)

**LAS CIFRAS DE MI APERTURA SELLADA, CONTRA LO MEDIDO HOY:** el censo, la poblacion y las huellas (`74.1`); las `29` lineas, `6`
`CONTINUA` y `23` `SANO` (`74.3`); las `3` aristas (`74.3`); `cap_13` en `0` de `68` y Grove en `0` de `42` (`74.4`). **Todas cuadran.**

**MI CAIDA, CON MI NOMBRE: EL ENCARGO DE LA `75` PEGO *`51` deuda(s) esperando* Y AL PUBLICARSE ERAN `52`.** La salida era literal
de su corrida, pero despues anote `d180` en el mismo cierre, y el encargo se commiteo con la cifra ya vieja. **Lo cazo el extractor
en su `75.0`**, con la hora de la anotacion. El encargo es sede mia y la cifra estaba en su bloque de clase:

    $ git show 702ee04d:docs/loop/PROMPT_SIGUIENTE.md | grep -n "deuda(s) esperando"; git show 702ee04d:docs/loop/DEUDA.jsonl | grep -c '"id": "d180"'
    18:      van 1 de 5 desde la ultima de saneamiento (la 74), con 51 deuda(s) esperando
    1

**LA CARGO COMO `CIFRA PUBLICADA PROPIA`: `AUDITOR` SUBE A `1 de 3`.** **La lectura contraria, escrita**: el bloque es la salida
literal del instrumento en su momento, y `D.38.3` pide eso. **No la elijo**: lo que la regla protege es la cifra que el lector
encuentra al abrir el encargo, y el lector encontro una falsa. **Es la misma figura que la `ACTA 72` le cobro al extractor** (una celda
cuyo orden temporal no era el que decia), y no me la perdono con otra vara.

**REMEDIO NUEVO, MIO, `R10`** (`74.11`): toda salida pegada en el encargo se corre **despues de la ultima escritura** del auditor en
el registro que esa salida mide. **En esta acta**: no anoto ninguna deuda, y la clase de la `76` se vuelve a correr justo antes del
commit y se compara con la pegada (`74.13`).

**Y UN DESLIZ DE MI FASE CIEGA, DECLARADO ALLI** (`APERTURA_CIEGA.md`, cabecera): un `git --version` en la cola de un comando. **No lee
el repositorio ni recupera nada**, y el arnes no registro recuperacion alguna:

    $ sed -n '8045,8352p' docs/loop/loop.log | grep -ci "git\|recuper"
    0

**Sin especie**: no es un remedio roto ni una cifra.

**LO QUE MI APERTURA DIJO QUE HARIA EN EL TURNO NORMAL** (su seccion `8`, ocho puntos) **esta todo aqui**: `R5` y `R9` en `74.0` y
`74.4`; la TAREA `2` con `git` en `74.0`; las lineas nuevas una a una en `74.3`; los `insertar` y su orden en `74.3`; la muestra en
`74.5`; las aristas con ids en `74.3`; el censo, las guardas, el cierre y el coste en `74.1`, `74.6` y `74.8`; `R8` en `74.12`.

## 74.10. **LAS CONDICIONES DE PARADA, UNA A UNA** (`3`)

| condicion | se cumple | como lo mido |
|---|---|---|
| doctrina nueva | **NO** | los cuatro discutibles los cubren `D.35`, `D.54`, `6.1` y el encargo (`74.5`) |
| contradiccion | **NO** | ninguna cifra publicada queda sin corregir: la mia, cargada (`74.9`) |
| decision de Alexis | **NO** | insertar Gerber esta ordenado (`PARALELO.md` `8` punto `4`) |
| fallo tecnico repetido | **NO** | gate, guiones, suite y cierre estricto en verde (`74.1`) |
| credito roto | **NO** | `AUDITOR` en `1 de 3`, las demas en cero (`74.7`) |
| campania consumada | **NO**: quedan Gerber y Marquet, abajo | |

    $ sed -n '11,13p;24p' .v75aud/normal/tablero.txt
      1    7    grove_high_output              COSECHADO              NINGUNO                  0  cap_18
      2    9    gerber_emyth                   COSECHADO              NINGUNO                 22  cap_22
      3    5    marquet_turn_the_ship          COSECHADO              NINGUNO                 20  cap_17
      MUNDO 11: faltan 3 de 7 libros del corte (grove_high_output, gerber_emyth, marquet_turn_the_ship)
    $ cat .v75aud/normal/clase76.txt
    LIBRE
      van 2 de 5 desde la ultima de saneamiento (la 74), con 52 deuda(s) esperando
    $ python .v75aud/normal/bandeja_gerber.py | tail -2
    fichas por capitulo: {'cap_04': 1, 'cap_07': 1, 'cap_08': 2, 'cap_11': 6, 'cap_12': 3, 'cap_13': 1, 'cap_14': 1, 'cap_15': 1, 'cap_18': 3, 'cap_19': 3} | suma: 22
    pasos por capitulo: {'cap_04': 7, 'cap_07': 8, 'cap_08': 17, 'cap_11': 57, 'cap_12': 12, 'cap_13': 10, 'cap_14': 9, 'cap_15': 5, 'cap_18': 26, 'cap_19': 25} | suma: 176

(Las `22` fichas, una por linea con su capitulo y sus pasos, en `.v75aud/normal/bandeja_gerber.txt`; el capitulo sale de la primera
cita de capitulo de cada ficha, que en las `22` es el de su `UNIDAD DE ORIGEN`.)

**LECTURA:** **Grove tiene la bandeja en `0` y el tablero lo sigue llamando `COSECHADO`**, que es exactamente lo que `d180` anoto
(`ACTA 73` `73.10`): **se confirma con el dato**, y la deuda ya esta escrita; no se toca (`D.45`, `7.F`). **NO ESCRIBO
`PARA_ALEXIS.md`.** **La `76` es LIBRE y prepara Gerber**, como la `71` y la `73` prepararon Grove: fidelidad entera, barrido,
veredictos, aristas con `d111`, `d108` y `d098` delante, y orden. **Sin bloqueante.**

## 74.11. **LOS REMEDIOS**

| # | de quien | remedio | donde se comprueba |
|---|---|---|---|
| `R5` | del extractor | **Sigue vivo con su letra**, cumplido de la `65` a la `75` | el reporte de la `76`, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la cabecera cambiada a la `76` |
| `R6` | del auditor | **Sigue vivo con su letra** | la apertura ciega de la `76` |
| `R7` | del auditor | **Sigue vivo con su letra** | la apertura ciega de la `76` y la `ACTA 75` |
| `R8` | del auditor | **Sigue vivo con su letra y su criterio**; instrumento de esta vuelta, `.v75aud/normal/r8_encargo76.py` | mi fase ciega de la `76`, sobre el encargo de la `76` (`74.12`); y el encargo de la `77` |
| `R9` | del extractor | **Sigue vivo con su letra** aunque `REPORTE` vuelva a cero: la `76` marca la fidelidad de un lote entero, que es donde nacio | el reporte de la `76`, en cada fila de fidelidad y en cada cuenta de PUENTE |
| **`R10`** | **del auditor, NUEVO** (`74.9`) | **Toda salida pegada en `PROMPT_SIGUIENTE.md` se corre despues de la ultima escritura del auditor en el registro que esa salida mide** (`DEUDA.jsonl`, `CREDITO_serial.jsonl`, el tablero), **o se vuelve a correr antes del commit y se compara** | esta acta (`74.13`) y la `ACTA 75` |

## 74.12. **`R8` MEDIDO SOBRE MI ENCARGO DE LA `76`, ANTES DE CERRARLO** (`74.11`)

    $ python .v75aud/normal/r8_encargo76.py | tail -1
    lineas del encargo: {'linea de bloque sangrado': 14, 'prosa con numero, con seccion de la ACTA 74': 12, 'prosa con numero, sin seccion de la ACTA 74': 55, 'prosa sin digito ni palabra de numero': 65} | suma: 146

(Las lineas con numero, cada una con sus digitos y sus palabras de numero, en `.v75aud/normal/r8_encargo76.txt`.) **LECTURA, grupo a
grupo, de las que no traen seccion, leidas una a una:**

- **Numeros de vuelta, de acta, de rama, de mundo o de carpeta de la casa** (`76`, `75`, `74`, `73`, `72`, `71`, `62`, `11`, y
  `.v73ext/`, `.v75ext/`, `.v75aud/`, `.v76ext/`, `.v64ext/`, `.v64aud/`, `.v70aud/`).
- **Secciones, reglas, deudas y numeros de tarea, de punto o de lista** (`1.4`, `0`, `D.29`, `D.30`, `D.36`, `D.37`, `D.38.4`,
  `D.47`, `D.53`, `D.55`, `D.58`, `D.61`, `D68.7`, `7.F`, `6.1`, `8.2`, `4.2`, `d031`, `d098`, `d108`, `d111`, `R5`, `R8`, `R9`, el
  `8` punto `3` y `4` de `PARALELO.md`, y los `1` a `5` de tareas y puntos).
- **Identificadores de capitulo, de linea del libro o de fecha**: `cap_05`, `cap_13`, `cap_14`, `cap_18`, `cap_19`, `cap_22`; `L27`,
  `L29`, `L117`; el `23` sep de la frase fija de los asientos que no volvieron.
- **Umbrales de la casa**: el `10` por ciento de `8.1`, que es regla y no medida.
- **Palabras de numero sin seccion**: *cinco a la vez* (un tope de la casa, dos veces), *tres asientos* (la frase fija), *los dos
  delante* (los dos nodos de un par, dos veces), *las tres fases* (lo que dice `cap_05` `L29`, citada en la misma linea), *en cero*
  (la meta de las comprobaciones de `orden.py`) y *cero guiones* (la frase fija). **Ninguna es una cuenta de fichero.** Los numeros
  en letra de los ids de Gerber (`aplicar_cinco_pasos_...` y los demas) son **identificadores**, no cuentas.
- **Las cifras de medida** van dentro de un bloque `$` (el reloj de la `73`, la clase, el tablero) o llevan su seccion de la `ACTA 74`
  en la misma linea (la bandeja de Gerber, `74.10`; la poblacion y el censo de apertura, `74.1`; el patron de `R9`, `74.4`; los
  registros de la TAREA `1`).

**`R8` CUMPLIDO EN EL ENCARGO DE LA `76`, medido.** Lo vuelve a medir mi fase ciega (`74.11`).

## 74.13. **LO QUE ANOTO AL CERRAR**

- **`docs/loop/CREDITO_serial.jsonl`**: las lineas de la tanda `ACTA 74`: `CLASE`, `CIFRA PUBLICADA`, `DATO MOVIDO` y `REPORTE` con
  `--limpia`, y `AUDITOR` con `--cae`.
- **`docs/loop/DEUDA.jsonl`**: **nada**, a proposito (`R10`). La clase de la `76`, vuelta a correr antes del commit contra la pegada
  en el encargo, en `.v75aud/normal/r10.txt`.
- **`docs/loop/PROMPT_SIGUIENTE.md`**: el encargo de la vuelta `76`, **LIBRE**: la preparacion de Gerber, sin bloqueante.
- **`.v75aud/`**: mi evidencia de las dos fases, commiteada con `docs/loop/`.
