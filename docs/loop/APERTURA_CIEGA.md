# APERTURA CIEGA DE LA VUELTA 72, lote 7 (`grove_high_output`), **CLASE INSERCION**

*Auditor `claude-opus-5-5`, fase ciega, 26 sep 2026, la que el arnes numera `VUELTA 1` en la corrida que arranco el 25 a
las `21:43`. Linea **serial**, rama `extraccion-mundo-11`. Modo austero (`D.47`). Todo lo de esta pagina sale de `.v72aud/`,
escrito y corrido en esta fase; cada bloque `$` lo pega `.v72aud/generar_apertura.py` corriendo el comando en el momento de
escribirla. **No hay ninguna tabla en esta pagina**, a proposito, como en la `70` y la `71`.*

**UNA CAIDA DE METODO MIA, DICHA ANTES DE NADA: EN ESTA FASE CORRI `git` UNA VEZ.** Al abrir, para saber el tamaño del acta,
corri en la carpeta viva `git -C . log -1 --format=%H`, que imprimio **solo** el hash del ultimo commit
(`f5bba45a2edb332bb597b71dd0b943274cbe56f8`), ningun asunto, ningun fichero y nada retirado. **Va contra lo que yo mismo
escribi en la `71`** (*la carpeta de una linea viva es solo del arnes*, `PARALELO.md` `7`), y lo digo aqui para que se juzgue.
**No recupere nada**: los cuatro retirados siguen sin estar (seccion `0`). Despues, el commit lo leo de los ficheros de
`.git/` sin correr `git`, y da el mismo:

    $ cat .git/HEAD; cat .git/refs/heads/extraccion-mundo-11
    ref: refs/heads/extraccion-mundo-11
    f5bba45a2edb332bb597b71dd0b943274cbe56f8

## 0. **LA HERENCIA** (`D.40`)

ACTA ANTERIOR LEIDA: 99aaf1437e0189f273b01c6c1f1d9c0d24f78706

**Comprobada sin git**: es el blob de `docs/loop/ACTA_AUDITOR.md` tal como esta hoy en el arbol, calculado a mano como lo
calcula git. La `ACTA 70` la lei entera, de su linea de cabecera a la ultima del fichero:

    $ python .v72aud/huella_acta.py
    sha1 del blob tal cual: 99aaf1437e0189f273b01c6c1f1d9c0d24f78706
    lineas con CRLF en el arbol: 0 | sha1 del blob normalizado a LF: 99aaf1437e0189f273b01c6c1f1d9c0d24f78706
    lineas del fichero: 48490 | la ACTA 70 empieza en la linea: [48075]

HEREDADO 1: NO APLICA en esta fase. **Motivo:** `R5` es un remedio **del extractor** y se mide **sobre su reporte de la
`72`** (`ACTA 70` `70.12`: *el reporte de la `72`, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py`, los dos con
la cabecera del tramo cambiada a la `72`*), y el reporte **no esta en el arbol**: el arnes lo retiro para esta fase (`D.34.2`)
y no lo he recuperado por ninguna via. **Se mide en mi turno normal**, con los dos instrumentos sacados otra vez de los
originales y no de las copias del extractor. Lo que si esta en mi mano lo cumplo en mi pagina: cada bloque `$` lleva la salida
del comando que abre, y nada mas.

    $ ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl
    ls: cannot access 'docs/loop/REPORTE.md': No such file or directory
    ls: cannot access 'docs/loop/ultimo_extractor.json': No such file or directory
    ls: cannot access 'docs/loop/ultimo_auditor.json': No such file or directory
    ls: cannot access 'docs/loop/CREDITO_serial.jsonl': No such file or directory
    $ grep -n "VUELTA 1 : APERTURA CIEGA" docs/loop/loop.log | tail -1
    7116:[2026-09-26 01:28:04] VUELTA 1 : APERTURA CIEGA (claude-opus-5-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl

HEREDADO 2: CUMPLIDO. **`R6`, mio** (`ACTA 70` `70.12`): en esta fase los pasos de cualquier nodo los imprime
`.v67aud/normal/pasos_ciego.py`, que no enseña `previos` ni `siguientes`, y **el unico bloque de pasos de esta pagina lo corre**
(seccion `5`). Ningun instrumento mio de esta fase nombra esas claves:

    $ grep -l -E "previos|siguientes" .v72aud/*.py | wc -l
    0

**Y DIGO LO UNICO QUE SE ACERCA, para que se juzgue:** `.v72aud/grafo_sin_tanda.py` (seccion `2`), copia del de la `70`, quita
los ids de las `20` de **cualquier lista** de los nodos viejos, sin nombrar ninguna clave, y **cuenta** cuantos nodos viejos
tenian alguno: imprime una cuenta y un `SI` o un `NO`, **ninguna clave ni ningun id de relacion**. Y `.v72aud/r8_encargo.py`
(seccion `6`) imprime lineas de mi encargo, que nombra una clave de relacion en su linea `99`: esa linea **no la imprime**,
porque no trae cifra. El cumplimiento de la pagina entera lo mide un `grep` sobre ella al cerrarla (seccion `8`).

HEREDADO 3: CUMPLIDO. **`R7`, mio** (`ACTA 70` `70.12`): toda linea de esta pagina que reparte un total en clases la imprime un
instrumento que cuenta **todas** las clases con el mismo predicado y **dice su `suma`**: los de `.v72aud/` la traen desde que
nacen, y el que reuso de la `70` (`poblacion.py`) ya la traia. **Medido sobre la pagina misma** en la seccion `8`, con la copia
de `.v70aud/r7_pagina.py`.

HEREDADO 4: NO APLICA a lo que esta fase escribe, porque no escribe ningun encargo; Y NO LO DOY POR CUMPLIDO: medido sobre su primera sede, mi encargo de la `72`, lo rompo en tres cifras (seccion `6`). **Motivo del `NO APLICA`:** `R8`
(`ACTA 70` `70.12`) manda sobre las cifras de medida que escribo en `docs/loop/PROMPT_SIGUIENTE.md`, y se comprueba en *el
encargo de la `72` (este mismo turno) y el de la `73`*. **El de la `73` lo escribo en mi turno normal, y esta fase no toca ese
fichero.** Pero el de la `72` ya esta escrito, es mio y lo puedo medir aqui, **y lo mido**: la salida entera y la lectura, cifra
por cifra, en la seccion `6`. El bloque que sostiene el motivo, que el fichero es el que escribi al cerrar la `ACTA 70`:

    $ head -3 docs/loop/PROMPT_SIGUIENTE.md | cut -c1-120; ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, $7, $9}'
    # ENCARGO DE LA VUELTA 72: **LAS `20` FILAS DE `.v71ext/orden.txt` DENTRO, UNA POR VEZ, CON LAS `50` LINEAS Y LAS `6` AR

    *Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 70`, que audito la vuelta `71`.
    2026-09-25 21:34:30.963461300 docs/loop/PROMPT_SIGUIENTE.md

## 1. **LO QUE VI SIN BUSCARLO, Y LO DIGO ANTES DE MEDIR** (`d146`)

**La foto de `git status` que el entorno me pone delante trae los asuntos de los cinco ultimos commits del extractor, y dos
traen conclusiones de esta vuelta**, que lei antes de medir nada:

- `4b6382a0` *Vuelta 72, T5: el cierre (censo 430/1081/1/7/85, PASOS INVENTADOS 0 que entraron, D.61 sin abiertos, R5, guardas
  y cierre estricto en verde)*;
- `b9d02af4` *Vuelta 72, T4: las 6 aristas de la tanda en el grafo, adjudicadas; ningun nodo viejo cambia*;
- y `f5bba45a`, `25856653` y `d81a1b91`, sin cifras (*la salida del hook*, *R5 con el reporte entero*, *fila 20: su fila en el
  reporte*).

**Tambien lei la cola de `docs/loop/loop.log`**, que no se retira (el turno del extractor: `13455` s y `7,03` USD), **mi propio
encargo** (`docs/loop/PROMPT_SIGUIENTE.md`, que es mio), la ultima linea de `.v71ext/orden.txt` (la cifra `6` que mi encargo
cita, seccion `6`; es de la vuelta que ya audite), y del codigo, para saber que cambio (seccion `2`), el docstring de
`src/presupuesto.py` y las lineas de `src/aduana.py` que lo nombran. Las lineas del `loop.log` que lei y cito:

    $ grep -n "VUELTA 1 : EXTRACTOR\|extractor listo" docs/loop/loop.log | tail -2
    7114:[2026-09-25 21:43:48] VUELTA 1 : EXTRACTOR (claude-opus-5-5, esfuerzo high)
    7115:[2026-09-26 01:28:03] extractor listo (USD 7.030318799999997), 13455s, intento 1 de 7

**LO QUE ESO LE HACE A ESTA PAGINA, SIN REBAJARLO:**

1. **Mis clases de la tanda no las decido hoy**: son las de mis ficheros sellados de la `71` (`.v71aud/mis_clases.tsv` y
   `.v71aud/aristas_lectura.tsv`), mas la unica correccion que la `ACTA 70` `70.5` adjudico (mis dos `CONTINUA` de
   `cerrar_brecha_dos_preguntas_estrategia` caen a `SANO`), declarada dentro de `.v72aud/esperado_72.py`.
2. **Ninguna cifra de esta pagina sale de esos asuntos**; todas salen de un instrumento corrido en esta fase, y **donde
   coinciden lo digo como coincidencia y no como fuente**.
3. **No he abierto nada de `.v72ext/`**, ni `bitacora/VEREDICTOS.jsonl` ni `docs/loop/DEUDA.jsonl` por dentro: de la bitacora
   solo cuento lineas.

## 2. **EL CENSO, Y QUE LA POBLACION DE LA ADUANA ES LA DE MI BARRIDO DE LA `71`** (`D.38.4`, `D.38.5`)

La vuelta es **de insercion** (mi encargo): las `20` filas de `.v71ext/orden.txt`, una por vez.

    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl
        430 dataset/nodos.jsonl
       1081 bitacora/VEREDICTOS.jsonl
          1 config/pares_mutuos.jsonl
       1512 total
    $ for d in cuarentena/grove_high_output cuarentena/_insertados/grove_high_output cuarentena/gerber_emyth cuarentena/marquet_turn_the_ship; do echo "$d $(ls $d/*.json | wc -l)"; done; echo "procesos $(ls -A procesos/ | wc -l)"
    cuarentena/grove_high_output 7
    cuarentena/_insertados/grove_high_output 85
    cuarentena/gerber_emyth 22
    cuarentena/marquet_turn_the_ship 20
    procesos 0
    $ python forja.py gate | head -2
    GATE VERDE.
      nodos verificados: 430

**Sin `git`, lo que cambio desde mi barrido de la `71`, por tres instrumentos.** Primero, **cualquier fichero** del dato, de las
bandejas, del codigo o de la configuracion con fecha de escritura posterior a las huellas que tome al lanzarlo (las fichas de
una misma carpeta, juntas):

    $ ls -l --time-style=full-iso .v71aud/huellas_al_barrer.txt | awk '{print $6, $7, $9}'
    2026-09-25 19:57:12.172169900 .v71aud/huellas_al_barrer.txt
    $ find cuarentena dataset bitacora censos config fuentes esquema src scripts -type f -newer .v71aud/huellas_al_barrer.txt | sed 's|/[^/]*\.json$|/*.json|' | sort | uniq -c
          1 bitacora/VEREDICTOS.jsonl
          1 censos/atribuciones.md
          1 censos/denominaciones.md
          1 dataset/nodos.jsonl
          1 scripts/lanzar_linea.ps1
          1 scripts/prioridad_baja.ps1
          1 src/__pycache__/aduana.cpython-312.pyc
          1 src/__pycache__/presupuesto.cpython-312.pyc
          1 src/aduana.py
          1 src/presupuesto.py
    $ ls -l --time-style=full-iso src/aduana.py src/presupuesto.py scripts/lanzar_linea.ps1 scripts/prioridad_baja.ps1 | awk '{print $6, $7, $9}'
    2026-09-25 21:43:35.857803000 scripts/lanzar_linea.ps1
    2026-09-25 21:43:35.871902200 scripts/prioridad_baja.ps1
    2026-09-25 21:43:35.871902200 src/aduana.py
    2026-09-25 21:43:35.871902200 src/presupuesto.py

Segundo, **las `70` huellas de entonces** (las fichas de las tres bandejas y el grafo) contra los ficheros de hoy, buscando en
`_insertados` la ficha que ya no esta en la bandeja:

    $ python .v72aud/huellas_hoy.py
    huellas: 70 | suma: 70
      gerber_emyth, en su sitio, misma huella: 22
      grafo, aparte: 1
      grove_high_output, en su sitio, misma huella: 7
      grove_high_output, movida a _insertados, misma huella: 20
      marquet_turn_the_ship, en su sitio, misma huella: 20
    movidas a _insertados: 20 | son las 20 de .v71aud/los20.txt: SI | fuera de ellas: []
    ficheros que no cuadran: []

Tercero, **el grafo**: si al de hoy le quito las `20` filas de la tanda, y ademas los ids de las `20` de las listas de los nodos
viejos, sale el fichero que barri, byte a byte:

    $ python .v72aud/grafo_sin_tanda.py
    filas del grafo hoy: 430 | la reconstruccion reproduce el fichero de hoy: SI
    de las 20 de la tanda en el grafo: 20 | filas que quedan sin ellas: 410
    las 20 son las ultimas filas del fichero: SI
    (a) sin las 20 filas, sha1 igual a la huella de mi barrido de la 71: SI
    (b) nodos viejos con algun id de las 20 en alguna lista: 0 | sin esos ids, sha1 igual a la huella: SI
    $ python .v70aud/poblacion.py
    poblacion: 479 | por sede: {'grafo': 430, 'bandeja': 49} | suma: 479

**LECTURA:**

- **El grafo tiene `430` filas, la bandeja de Grove `7`, sus insertados `85`, los pares mutuos `1`, la bitacora `1081` lineas,
  y `procesos/` esta vacio.** Coincide con el `430/1081/1/7/85` del asunto de `4b6382a0`, y lo digo como coincidencia. Gerber y
  Marquet siguen en `22` y `20`, con la huella de mi barrido.
- **Las `20` fichas movidas a `_insertados` son las `20` de mi lista, con la huella que tenian cuando las barri**, y las `7`
  que quedan en la bandeja, tambien.
- **Los `410` nodos viejos son byte a byte los que barri, SIN QUITAR NINGUN ID**: ningun nodo viejo tiene un id de la tanda en
  ninguna lista, y el fichero sin las `20` filas ya tiene la huella de mi barrido. **Es lo que mi lectura espera**: ninguna de
  mis `6` aristas tiene un extremo fuera de las `20` (seccion `4`). Coincide con el *ningun nodo viejo cambia* de `b9d02af4`.
  Las `20` son las ultimas filas del fichero.
- **La poblacion de hoy es `479`**, la de mi barrido, con `20` en otra sede.
- **LO QUE CAMBIO Y NO PUEDO MEDIR SIN `git`: `src/aduana.py`, `src/presupuesto.py` y dos guiones de `scripts/` se escribieron el
  25 a las `21:43:35`, despues de mi barrido** (`19:57`) y trece segundos antes de que el arnes abriera el turno del extractor
  (`21:43:48` en `docs/loop/loop.log`, seccion `1`), y `src/presupuesto.py` se presenta en su docstring como *decision del
  fundador, 25 sep 2026* (el bloque de abajo). **LECTURA, y es lectura:** por el
  docstring de `src/presupuesto.py` y las lineas de `src/aduana.py` que lo nombran (`from . import presupuesto`, el reparto de
  procesos y la `PlazaPropia` de la senial `3`), el cambio reparte **cuantos procesos** calculan, no **que** se mide; y la `ACTA
  70` `70.1` ya midio que repartir la senial `1` no cambia ni pares ni cifras. **Pero no he visto el diff**, y por eso lo que la
  aduana de hoy levanto no lo doy por igual a mi barrido por el codigo: lo compruebo **por el dato**, par a par, en mi turno
  normal (seccion `7`). El indicio de aqui es solo de cuenta: la bitacora tiene las lineas que mi barrido espera (seccion `4`).

    $ sed -n 2p src/presupuesto.py; grep -c "presupuesto" src/aduana.py
    """PRESUPUESTO UNICO DE PROCESOS DE CALCULO PARA TODA LA MAQUINA (decision del fundador, 25 sep 2026).
    10
- **Lo que se escribio despues de mis huellas en el dato** es el grafo, la bitacora y dos censos (`atribuciones.md` y
  `denominaciones.md`), que es lo que escribe una insercion; **nada en `config/`, `esquema/`, `fuentes/` ni en las bandejas**.

## 3. **LAS `20`: LO QUE ENTRO ES LO QUE SE LEYO** (`D.58`), **Y SUS PASOS INVENTADOS** (`8`, `8.2`)

Cada nodo del grafo contra su ficha de `_insertados` (cuya huella es la leida, seccion `2`) en titulo, condiciones, pasos,
entregable y resumen; y sus pasos contra **mi** lectura entera sellada en la `71`, `.v71aud/fidelidad_fuente.txt`, una fila por
paso:

    $ python .v72aud/entra_lo_leido.py
    las 20 por sede hoy: {'grafo y _insertados': 20} | suma: 20
    nodos del grafo contra su ficha, cinco campos: {'igual': 20} | suma: 20
    nodos con descuadre entre sus pasos en el grafo y mis filas selladas: 0 []
    cap_07 lo que ENTRO: candidatos 9 | pasos 53 | mis marcas: {'T': 48, 'P': 0, 'D': 5} | suma: 53 | PUENTE 0 de 53 = 0.00 por ciento | con las D adjudicadas T (ACTA 70 70.4): T 53, P 0, suma 53
    cap_10 lo que ENTRO: candidatos 1 | pasos 8 | mis marcas: {'T': 8, 'P': 0, 'D': 0} | suma: 8 | PUENTE 0 de 8 = 0.00 por ciento | con las D adjudicadas T (ACTA 70 70.4): T 8, P 0, suma 8
    cap_11 lo que ENTRO: candidatos 2 | pasos 17 | mis marcas: {'T': 16, 'P': 0, 'D': 1} | suma: 17 | PUENTE 0 de 17 = 0.00 por ciento | con las D adjudicadas T (ACTA 70 70.4): T 17, P 0, suma 17
    cap_12 lo que ENTRO: candidatos 3 | pasos 11 | mis marcas: {'T': 11, 'P': 0, 'D': 0} | suma: 11 | PUENTE 0 de 11 = 0.00 por ciento | con las D adjudicadas T (ACTA 70 70.4): T 11, P 0, suma 11
    cap_13 lo que ENTRO: candidatos 2 | pasos 14 | mis marcas: {'T': 14, 'P': 0, 'D': 0} | suma: 14 | PUENTE 0 de 14 = 0.00 por ciento | con las D adjudicadas T (ACTA 70 70.4): T 14, P 0, suma 14
    cap_14 lo que ENTRO: candidatos 3 | pasos 18 | mis marcas: {'T': 18, 'P': 0, 'D': 0} | suma: 18 | PUENTE 0 de 18 = 0.00 por ciento | con las D adjudicadas T (ACTA 70 70.4): T 18, P 0, suma 18
    los seis: candidatos 20 | pasos 121 | mis marcas: {'T': 115, 'P': 0, 'D': 6} | suma: 121 | PUENTE 0 de 121

**LECTURA:** las `20` viven en el grafo **con los textos que se leyeron**, y cada una con tantos pasos como filas tiene mi
lectura. **`PASOS INVENTADOS` de lo que ENTRO: `0` en los seis capitulos** (`cap_07` `0` de `53`, `cap_10` `0` de `8`, `cap_11`
`0` de `17`, `cap_12` `0` de `11`, `cap_13` `0` de `14` y `cap_14` `0` de `18`), que son las cifras que la `ACTA 70` `70.6` firmo
como *PUENTE que entrara*: los `4` PUENTE de la preparacion se corrigieron en la bandeja **antes** de mi barrido, y mis `6` `D` las
adjudico `T` la `ACTA 70` `70.4`, que no reabro (`D.47`). **Por debajo del `10`: no se baja escalon** (`8.1`), y de todos modos no
queda lote de extraccion en el mundo `11`. Coincide con el *PASOS INVENTADOS 0 que entraron* de `4b6382a0`, y lo digo como
coincidencia.

## 4. **LO QUE MI LECTURA ESPERA QUE LA TANDA DEJE, Y EL ORDEN EN QUE ENTRO**

Sacado **solo** de mis ficheros sellados de la `71`, con la correccion de la `ACTA 70` `70.5` aplicada y declarada dentro del
instrumento; la bitacora, solo contada:

    $ python .v72aud/esperado_72.py
    pares con la correccion de la ACTA 70 70.5 aplicada: 2
    filas dirigidas de mi barrido con candidato de las 20: 50 | por vecino: {'vecino fuera de la tanda': 12, 'vecino en la tanda': 38} | suma: 50
    lineas de veredicto esperadas, por la clase de su par: {'SANO': 46, 'CONTINUA': 4} | suma: 50
    aristas esperadas: 6 | por origen: {'CONTINUA': 2, 'SOSTENGO': 4} | suma: 6
      CONTINUA      definir_entorno_grupo_clientes_proveedores_competidores > examinar_demanda_entorno_dos_marcos_temporales
      CONTINUA      definir_entorno_grupo_clientes_proveedores_competidores > examinar_entorno_expectativas_tecnologia_proveedores_grupos
      SOSTENGO D.37 planificar_tres_pasos_demanda_estado_brecha > examinar_demanda_entorno_dos_marcos_temporales
      SOSTENGO D.37 planificar_tres_pasos_demanda_estado_brecha > determinar_estado_presente_capacidades_proyectos_merma
      SOSTENGO D.37 planificar_tres_pasos_demanda_estado_brecha > cerrar_brecha_dos_preguntas_estrategia
      SOSTENGO D.29 elegir_modo_control_motivacion_factor_cua > escalonar_complejidad_puesto_empleado_nuevo
    extremos de esas aristas que no son de las 20: 0
    bitacora esperada: 1027 + 50 + 4 = 1081 | hoy (lineas): 1081 | IGUAL

**LECTURA, y lo que se compara en el turno normal, no aqui:**

- **Lineas de bitacora.** Si cada `insertar` escribio una linea por vecino que su aduana levanto, y la aduana levanto lo que mi
  barrido, son `50`: `4` `CONTINUA` y `46` `SANO` por la clase de su par; y `python forja.py arista` escribe su propia linea, asi
  que con mis `4` por lectura son `1027` mas `50` mas `4`. **La bitacora tiene `1081`.** **Es coincidencia de cuenta y no de
  contenido**: no he abierto ni una linea. **Mi lectura no espera ningun vecino sin linea preparada**, porque la poblacion es la
  del barrido; uno que apareciera seria un hallazgo, y con el cambio de `src/aduana.py` delante (seccion `2`) lo busco par a par.
- **Aristas: `6`**, las `2` `CONTINUA` de `definir_entorno_grupo_clientes_proveedores_competidores` y `4` por lectura, **las
  seis con los dos extremos dentro de las `20`**. Coincide con el *6 aristas* de `b9d02af4`; **par a par lo cruzo en el turno
  normal**, que es donde un `6` igual con pares distintos se veria.

**El orden en que entraron, leido del grafo** (`src/aduana.py` escribe `nodos_nuevos + [nuevo]`, asi que cada fila nueva va al
final y el orden de las filas es el de entrada), **contra mis `12` restricciones selladas** de `.v71aud/restricciones_orden.py`:

    $ python .v72aud/orden_grafo.py
    orden de entrada leido del grafo: 20 filas
       1 planificar_tres_pasos_demanda_estado_brecha
       2 fijar_periodo_direccion_objetivos_retroalimentacion
       3 fijar_horizonte_ventana_replanificacion
       4 definir_entorno_grupo_clientes_proveedores_competidores
       5 examinar_entorno_expectativas_tecnologia_proveedores_grupos
       6 examinar_demanda_entorno_dos_marcos_temporales
       7 determinar_estado_presente_capacidades_proyectos_merma
       8 cerrar_brecha_dos_preguntas_estrategia
       9 contestar_dos_preguntas_direccion_objetivos
      10 repartir_supervision_puesto_funcional_mision
      11 elegir_modo_control_motivacion_factor_cua
      12 escalonar_complejidad_puesto_empleado_nuevo
      13 diagnosticar_capacidad_motivacion_prueba_vida
      14 fijar_meta_direccion_objetivos_mitad_probabilidad
      15 diagnosticar_nivel_motivacion_reaccion_aumento_salario
      16 elegir_estilo_direccion_madurez_relevante_tarea
      17 decidir_amistad_subordinado_prueba_revision_dificil
      18 entregar_evaluacion_desempeno_tres_claves
      19 preparar_resena_mixta_hoja_trabajo
      20 guiar_subordinado_etapas_resistencia_desempeno
      cumple     6 examinar_demanda_entorno_dos_marcos_temporales             antes que  8 cerrar_brecha_dos_preguntas_estrategia                       caida a SANO en la ACTA 70 70.5
      cumple     7 determinar_estado_presente_capacidades_proyectos_merma     antes que  8 cerrar_brecha_dos_preguntas_estrategia                       caida a SANO en la ACTA 70 70.5
      cumple     4 definir_entorno_grupo_clientes_proveedores_competidores    antes que  5 examinar_entorno_expectativas_tecnologia_proveedores_grupos  obliga
      cumple     4 definir_entorno_grupo_clientes_proveedores_competidores    antes que  6 examinar_demanda_entorno_dos_marcos_temporales               obliga
      cumple     1 planificar_tres_pasos_demanda_estado_brecha                antes que  6 examinar_demanda_entorno_dos_marcos_temporales               obliga
      cumple     1 planificar_tres_pasos_demanda_estado_brecha                antes que  7 determinar_estado_presente_capacidades_proyectos_merma       obliga
      cumple     1 planificar_tres_pasos_demanda_estado_brecha                antes que  8 cerrar_brecha_dos_preguntas_estrategia                       obliga
      cumple    11 elegir_modo_control_motivacion_factor_cua                  antes que 12 escalonar_complejidad_puesto_empleado_nuevo                  obliga
      cumple     6 examinar_demanda_entorno_dos_marcos_temporales             antes que  9 contestar_dos_preguntas_direccion_objetivos                  D.36 de un solo lado
      cumple     3 fijar_horizonte_ventana_replanificacion                    antes que  4 definir_entorno_grupo_clientes_proveedores_competidores      D.36 de un solo lado
      cumple     4 definir_entorno_grupo_clientes_proveedores_competidores    antes que  7 determinar_estado_presente_capacidades_proyectos_merma       D.36 de un solo lado
      cumple     2 fijar_periodo_direccion_objetivos_retroalimentacion        antes que  3 fijar_horizonte_ventana_replanificacion                      D.36 de un solo lado
    restricciones: {'caida a SANO en la ACTA 70 70.5, la cumple': 2, 'obliga, la cumple': 6, 'D.36 de un solo lado, la cumple': 4} | suma: 12

**LECTURA:** **las `12` se cumplen**, las `6` que obligan (`planificar_tres_pasos` antes que sus tres partes, `definir_entorno`
antes que sus dos hijas y `elegir_modo` antes que `escalonar`), las `2` que salian de mis `CONTINUA` caidos y ya no obligan, y las
`4` `D.36` de un solo lado, que son informativas. **`elegir_estilo_direccion_madurez_relevante_tarea` entro en la fila `16`**, la
que mi encargo le daba para `d170`. Que el orden de entrada sea el de `.v71ext/orden.txt` fila a fila lo miro en mi turno normal:
aqui solo lo mido contra lo mio.

## 5. **MI CLASIFICACION DE CADA CANDIDATO, Y LAS SEIS ARISTAS RELEIDAS** (`6.1`, y solo la vara `6.1`)

**Las `20`, una por una**, de mis ficheros sellados: las lineas del libro que sus pasos transcriben, las filas dirigidas de mi
barrido en las que es candidata, sus pares sin orden por clase con la correccion de la `70.5` (cuenta los pares en los que esta
de cualquiera de los dos lados, y por eso puede pasar de sus filas), y las aristas que mi lectura le espera como hija y cuantas
como madre:

    $ python .v72aud/clasificacion_20.py
     1 cap_07 cerrar_brecha_dos_preguntas_estrategia                     NODO | L39 a L39 | filas 10 | pares {'SANO': 10} suma 10 | hija: SOSTENGO D.37 de planificar_tres_pasos_demanda_estado_brecha | madre de: 0
     2 cap_07 contestar_dos_preguntas_direccion_objetivos                NODO | L71 a L75 | filas 6 | pares {'SANO': 6} suma 6 | hija: ninguna | madre de: 0
     3 cap_07 definir_entorno_grupo_clientes_proveedores_competidores    NODO | L25 a L25 | filas 6 | pares {'SANO': 5, 'CONTINUA': 2} suma 7 | hija: ninguna | madre de: 2
     4 cap_07 determinar_estado_presente_capacidades_proyectos_merma     NODO | L35 a L35 | filas 5 | pares {'SANO': 5} suma 5 | hija: SOSTENGO D.37 de planificar_tres_pasos_demanda_estado_brecha | madre de: 0
     5 cap_07 examinar_demanda_entorno_dos_marcos_temporales             NODO | L29 a L31 | filas 4 | pares {'SANO': 4, 'CONTINUA': 1} suma 5 | hija: CONTINUA de definir_entorno_grupo_clientes_proveedores_competidores; SOSTENGO D.37 de planificar_tres_pasos_demanda_estado_brecha | madre de: 0
     6 cap_07 examinar_entorno_expectativas_tecnologia_proveedores_grupos NODO | L27 a L27 | filas 6 | pares {'SANO': 5, 'CONTINUA': 1} suma 6 | hija: CONTINUA de definir_entorno_grupo_clientes_proveedores_competidores | madre de: 0
     7 cap_07 fijar_horizonte_ventana_replanificacion                    NODO | L61 a L61 | filas 3 | pares {'SANO': 4} suma 4 | hija: ninguna | madre de: 0
     8 cap_07 fijar_periodo_direccion_objetivos_retroalimentacion        NODO | L79 a L79 | filas 2 | pares {'SANO': 3} suma 3 | hija: ninguna | madre de: 0
     9 cap_07 planificar_tres_pasos_demanda_estado_brecha                NODO | L19 a L19 | filas 1 | pares {'SANO': 1} suma 1 | hija: ninguna | madre de: 3
    10 cap_10 repartir_supervision_puesto_funcional_mision               NODO | L43 a L43 | filas 0 | pares {} suma 0 | hija: ninguna | madre de: 0
    11 cap_11 elegir_modo_control_motivacion_factor_cua                  NODO | L57 a L61 | filas 0 | pares {} suma 0 | hija: ninguna | madre de: 1
    12 cap_11 escalonar_complejidad_puesto_empleado_nuevo                NODO | L63 a L63 | filas 0 | pares {} suma 0 | hija: SOSTENGO D.29 de elegir_modo_control_motivacion_factor_cua | madre de: 0
    13 cap_12 diagnosticar_capacidad_motivacion_prueba_vida              NODO | L17 a L17 | filas 2 | pares {'SANO': 2} suma 2 | hija: ninguna | madre de: 0
    14 cap_12 diagnosticar_nivel_motivacion_reaccion_aumento_salario     NODO | L85 a L85 | filas 1 | pares {'SANO': 1} suma 1 | hija: ninguna | madre de: 0
    15 cap_12 fijar_meta_direccion_objetivos_mitad_probabilidad          NODO | L75 a L75 | filas 1 | pares {'SANO': 1} suma 1 | hija: ninguna | madre de: 0
    16 cap_13 decidir_amistad_subordinado_prueba_revision_dificil        NODO | L75 a L77 | filas 1 | pares {'SANO': 1} suma 1 | hija: ninguna | madre de: 0
    17 cap_13 elegir_estilo_direccion_madurez_relevante_tarea            NODO | L19 a L27 | filas 0 | pares {} suma 0 | hija: ninguna | madre de: 0
    18 cap_14 entregar_evaluacion_desempeno_tres_claves                  NODO | L109 a L119 | filas 1 | pares {'SANO': 1} suma 1 | hija: ninguna | madre de: 0
    19 cap_14 guiar_subordinado_etapas_resistencia_desempeno             NODO | L167 a L179 | filas 0 | pares {} suma 0 | hija: ninguna | madre de: 0
    20 cap_14 preparar_resena_mixta_hoja_trabajo                         NODO | L129 a L131 | filas 1 | pares {'SANO': 1} suma 1 | hija: ninguna | madre de: 0

**LECTURA: LAS `20` SON NODO**, con la clase de cada par que selle en la `71` y la unica correccion adjudicada en la `ACTA 70`.
**No cambio ninguna**: la vuelta no trae material nuevo, y lo que entro es byte a byte lo que lei (secciones `2` y `3`).

**Las seis aristas son las que el extractor cablea en el acto**, las dos `CONTINUA` con `madre=` y las cuatro por lectura con
`python forja.py arista`, **y por eso las releo hoy con el libro y los pasos delante**. Las lineas del libro que las sostienen:

    $ python .v72aud/lineas_fuente.py
    cap_07 L19 (587 caracteres): Your general planning process should consist of analogous thinking. Step 1 is to establish projected need or demand: What will the environment demand from you, your business, or your organization? Step 2 is to establish your present status: What are you producing now? What will you be producing as your projects in the pipeline are completed? Put another way, where will your business be if you do nothing different from what you are now doing? Step 3 is to compare and reconcile [...]
    cap_07 L25 (658 caracteres): Just what is your environment? If you look at your own group within an organization as if it were a stand-alone company, you see that your environment is made up of other such groups that directly influence what you do. For example, if you were the manager of the company’s mailroom, your environment would consist of customers who need your services (the rest of the company), vendors who are able to provide you with certain capabilities (postage meters, mail carts), and finall [...]
    cap_07 L27 (556 caracteres): What should you look for when you examine your environment? You should attempt to determine your customers’ expectations and their perception of your performance. You should keep abreast of technological developments like electronic mail and other alternative ways of doing your job. You should evaluate the performance of your vendors. You should also evaluate the performance of other groups in the organization to which you belong. Does some other group (like the traffic depar [...]
    cap_07 L29 (720 caracteres): Once you have established what constitutes your environment, you need to examine it in two time frames (raya) now, and sometime in the future, let’s say in a year. The questions then become: What do my customers want from me now? Am I satisfying them? What will they expect from me one year from now? You need to focus on the difference between what your environment demands from you now and what you expect it to demand from you a year from now. Such a difference analysis is crucial, b [...]
    cap_07 L33 (21 caracteres): STEP 2 (raya) PRESENT STATUS
    cap_07 L37 (34 caracteres): STEP 3 (raya) WHAT TO DO TO CLOSE THE GAP
    cap_07 L39 (500 caracteres): The final step of planning consists of undertaking new tasks or modifying old ones to close the gap between your environmental demand and what your present activities will yield. The first question is, What do you need to do to close the gap? The second is, What can you do to close the gap? Consider each question separately, and then decide what you actually will do, evaluating what effect your actions will have on narrowing the gap, and when. The set of actions you decide up [...]
    cap_11 L61 (940 caracteres): Let’s now conceive a simple chart with four quadrants, shown above. The individual motivation can run from self-interest to group-interest, and the CUA factor of a working environment can vary from low to high. Now look for the best mode of control for each quadrant. When self-interest is high and the CUA factor is low, the most appropriate is the market mode, which governed our tire purchase. As individual motivation moves toward group interest, the contractual mode becomes  [...]
    cap_11 L63 (1204 caracteres): Let’s apply our model to the work of a new employee. What is his motivation? It is very much based on self-interest. So you should give him a clearly structured job with a low CUA factor. If he does well, he will begin to feel more at home, worry less about himself, and start to care more about his team. He learns that if he is on a boat and wants to get ahead, it is better for him to help row than to run to the bow. The employee can then be promoted into a more complex, unce [...]

Y los pasos de sus ocho nodos, por `pasos_ciego.py` (`R6`), que hoy los encuentra en el grafo:

    $ python .v67aud/normal/pasos_ciego.py planificar_tres_pasos_demanda_estado_brecha definir_entorno_grupo_clientes_proveedores_competidores examinar_entorno_expectativas_tecnologia_proveedores_grupos examinar_demanda_entorno_dos_marcos_temporales determinar_estado_presente_capacidades_proyectos_merma cerrar_brecha_dos_preguntas_estrategia elegir_modo_control_motivacion_factor_cua escalonar_complejidad_puesto_empleado_nuevo
    ===== planificar_tres_pasos_demanda_estado_brecha | grafo
      titulo: Planificar en los tres pasos del libro: la demanda del entorno, el estado presente, y lo que hay que hacer para conciliarlos
      fuente: ['grove_high_output']
      cond: Cuando tienes que planificar el trabajo de tu grupo y no sabes por donde empezar, o cuando lo que llamas plan es una lista de intenciones y no una comparacion entre lo que te van a pedir y lo que vas a producir.
      P1. Monta tu proceso general de planificacion sobre un razonamiento analogo al de la fabrica.
      P2. Da el paso 1 estableciendo la necesidad o demanda proyectada: que va a demandar de ti el entorno, de tu negocio o de tu organizacion.
      P3. Da el paso 2 estableciendo tu estado presente: que estas produciendo ahora, y que vas a estar produciendo cuando se completen los proyectos que ya tienes en marcha.
      P4. Formula ese paso 2 tambien de la otra manera: donde va a estar tu negocio si no haces nada distinto de lo que estas haciendo.
      P5. Da el paso 3 comparando y conciliando los pasos 1 y 2.
      P6. Convierte esa conciliacion en la pregunta concreta: que mas, o que menos, necesitas hacer para producir lo que tu entorno va a demandar.
    ===== definir_entorno_grupo_clientes_proveedores_competidores | grafo
      titulo: Definir tu entorno mirando tu grupo como si fuera una empresa independiente: clientes, proveedores y competidores
      fuente: ['grove_high_output']
      cond: Cuando vas a dar el paso 1 de la planificacion, el de la demanda del entorno, y no sabes todavia que cuenta como tu entorno ni donde acaba.
      P1. Mira tu propio grupo dentro de la organizacion como si fuera una empresa independiente.
      P2. Anota como entorno los otros grupos de ese tipo que influyen directamente en lo que haces.
      P3. Lista a tus clientes, que son quienes necesitan tus servicios.
      P4. Lista a tus proveedores, que son quienes pueden darte determinadas capacidades.
      P5. Lista por ultimo a tus competidores.
      P6. Cuenta con que dentro de la organizacion no tienes competidores, y en su lugar compara tu servicio con uno de fuera para juzgar tu desempeno y fijar tus estandares.
    ===== examinar_entorno_expectativas_tecnologia_proveedores_grupos | grafo
      titulo: Examinar tu entorno por los cuatro objetos que el libro nombra: las expectativas del cliente, la tecnologia, tus proveedores y los otros grupos de tu organizacion
      fuente: ['grove_high_output']
      cond: Cuando ya tienes definido que es tu entorno y tienes que examinarlo, y no sabes en que fijarte ni por donde empezar a mirar.
      P1. Determina las expectativas de tus clientes y la percepcion que tienen de tu desempeno.
      P2. Mantente al corriente de los desarrollos tecnologicos y de las maneras alternativas de hacer tu trabajo.
      P3. Evalua el desempeno de tus proveedores.
      P4. Evalua el desempeno de los otros grupos de la organizacion a la que perteneces.
      P5. Contesta para cada uno de esos grupos las dos preguntas que el libro pone: si ese grupo afecta a lo bien que puedes hacer tu trabajo, y si ese grupo puede cubrir lo que necesitas de el.
    ===== examinar_demanda_entorno_dos_marcos_temporales | grafo
      titulo: Examinar la demanda de tu entorno en dos marcos temporales y trabajar sobre la diferencia, sin rebajarla por lo que creas que puedes entregar
      fuente: ['grove_high_output']
      cond: Cuando ya tienes establecido que constituye tu entorno y tienes que convertirlo en demanda, o cuando te sorprendas bajando la demanda que declaras porque no crees que se pueda entregar.
      P1. Examina tu entorno en dos marcos temporales una vez que has establecido que lo constituye: ahora, y en algun momento futuro, digamos dentro de un ano.
      P2. Contesta que quieren de ti tus clientes ahora.
      P3. Contesta si los estas satisfaciendo.
      P4. Contesta que esperaran de ti dentro de un ano.
      P5. Concentrate en la diferencia entre lo que tu entorno te demanda ahora y lo que esperas que te demande dentro de un ano.
      P6. No pases todavia a que medidas practicas puedes tomar para atender el asunto, porque en esta fase eso solo confunde la cuestion.
      P7. No rebajes la demanda que declaras por lo que creas que la otra parte puede entregar: una demanda rebajada asi deja que nunca se prepare la capacidad para la demanda real.
    ===== determinar_estado_presente_capacidades_proyectos_merma | grafo
      titulo: Determinar tu estado presente listando capacidades y proyectos en curso, en la misma moneda de la demanda, con su plazo de salida y su merma descontada
      fuente: ['grove_high_output']
      cond: Cuando tienes que dar el paso 2 de la planificacion y necesitas una cifra de lo que vas a producir que se pueda restar de la demanda, no una lista de intenciones.
      P1. Lista tus capacidades presentes y los proyectos que tienes en marcha.
      P2. Expresalos en los mismos terminos, en la misma moneda, en la que has declarado la demanda.
      P3. Si la demanda esta en disenos de producto terminados, pon el trabajo en curso como disenos de producto parcialmente terminados.
      P4. Mira el plazo, es decir, cuando va a salir cada uno de esos proyectos de tu tuberia.
      P5. Preguntate si todos los proyectos que estan avanzando ahora van a completarse.
      P6. Cuenta con que la respuesta probablemente sea que no, con que algunos se descarten o se aborten, y mete ese hecho en tu produccion prevista.
      P7. Aunque no se pueda ser preciso en cada caso, descuenta tambien un porcentaje de perdida en los proyectos de gestion.
    ===== cerrar_brecha_dos_preguntas_estrategia | grafo
      titulo: Cerrar la brecha entre demanda y rendimiento contestando por separado que necesitas hacer y que puedes hacer, y llamar estrategia al conjunto que decidas
      fuente: ['grove_high_output']
      cond: Cuando ya tienes medida la demanda de tu entorno y tu estado presente, y te queda decidir que vas a hacer con la diferencia entre los dos.
      P1. Emprende tareas nuevas o modifica las que ya tienes para cerrar la brecha entre la demanda de tu entorno y lo que tus actividades presentes van a rendir.
      P2. Contesta la primera pregunta: que necesitas hacer para cerrar la brecha.
      P3. Contesta la segunda pregunta: que puedes hacer para cerrar la brecha.
      P4. Considera cada una de las dos preguntas por separado.
      P5. Decide despues que vas a hacer realmente.
      P6. Evalua al decidirlo que efecto van a tener tus acciones sobre el estrechamiento de la brecha, y cuando lo van a tener.
      P7. Llama estrategia al conjunto de acciones que decidas.
    ===== elegir_modo_control_motivacion_factor_cua | grafo
      titulo: Elegir el modo de control de una conducta de trabajo cruzando la motivacion de la persona (interes propio o de grupo) contra el factor CUA de su entorno (complejidad, incertidumbre y ambiguedad)
      fuente: ['grove_high_output']
      cond: Cuando tienes que decidir con que modo vas a controlar o influir una conducta de trabajo, la tuya o la de tu equipo, y dudas entre dejarla al precio, atarla a un contrato o apoyarte en valores compartidos.
      P1. Cuando tengas que decidir con que modo controlar una conducta de trabajo, mide dos variables: la naturaleza de la motivacion de la persona, que puede ir del interes propio al interes de grupo, y la naturaleza del entorno en el que trabaja.
      P2. Mide ese entorno con un indice compuesto que combine su complejidad, su incertidumbre y su ambiguedad, al que llamaras el factor CUA, y que puede ir de bajo a alto.
      P3. Reconoce que identificar cual de los modos de control conviene en cada caso es tarea tuya como mando.
      P4. Cruza las dos variables en un cuadro de cuatro cuadrantes: motivacion, de interes propio a interes de grupo, contra factor CUA, de bajo a alto.
      P5. Si la motivacion es de interes propio y el factor CUA es bajo, usa el modo de mercado, el mismo que gobierna una compra por el mejor precio.
      P6. Si la motivacion se mueve hacia el interes de grupo con el factor CUA bajo, usa el modo contractual, el mismo que gobierna que todos paren en el semaforo en rojo.
      P7. Si la orientacion de interes de grupo y el factor CUA son ambos altos, usa el modo de valores culturales, el mismo que explica que alguien se detenga a ayudar en un accidente.
      P8. Si el factor CUA es alto y la motivacion sigue siendo de interes propio, no esperes que ningun modo de control funcione bien: esa combinacion, como cada uno por su cuenta en un barco que se hunde, solo produce caos.
    ===== escalonar_complejidad_puesto_empleado_nuevo | grafo
      titulo: Escalonar la complejidad del puesto de un empleado nuevo, partiendo de un factor CUA bajo y subiendolo a medida que gana experiencia compartida con la organizacion
      fuente: ['grove_high_output']
      cond: Cuando incorporas a un empleado nuevo y tienes que decidir que tan estructurado o que tan complejo, incierto y ambiguo debe ser su primer puesto, y como ira cambiando eso con el tiempo.
      P1. Cuando incorpores a un empleado nuevo, cuenta con que su motivacion sera sobre todo de interes propio.
      P2. Dale un puesto claramente estructurado, con un factor CUA bajo.
      P3. Cuenta con que si le va bien, empezara a sentirse mas a gusto, a preocuparse menos por si mismo y a cuidar mas de su equipo.
      P4. Promuevelo despues a un puesto mas complejo, incierto y ambiguo, que ademas suele pagar mas.
      P5. Cuenta con que, a medida que pase el tiempo, ira ganando una cantidad creciente de experiencia compartida con el resto de la organizacion y estara listo para tareas cada vez mas complejas, ambiguas e inciertas.
      P6. Reconoce que esta es la razon por la que la promocion interna es el enfoque que favorecen las empresas con culturas corporativas fuertes.
      P7. Trae gente joven a puestos de nivel relativamente bajo y bien definidos, con factor CUA bajo.
      P8. Cuenta con que, con el tiempo, compartiran experiencias con sus companeros, jefes y subordinados y aprenderan los valores, los objetivos y los metodos de la organizacion.
      P9. Cuenta con que iran aceptando, incluso disfrutando, el mundo complejo de multiples jefes y de las decisiones entre pares.

**LECTURA, UNA POR UNA, Y LAS SEIS LAS SOSTENGO:**

- **`definir_entorno` madre de `examinar_demanda`, `CONTINUA`: SOSTENGO.** L29 remite con palabras a la pieza de la madre (*Once
  you have established what constitutes your environment*), el paso `1` de la hija lo copia (*una vez que has establecido que lo
  constituye*) y su condicion es el producto de la madre; y la hija anade los dos marcos, la diferencia y el no rebajar (pasos
  `1` a `7`), que la madre no trae. No repite.
- **`definir_entorno` madre de `examinar_entorno`, `CONTINUA`: SOSTENGO, con la `DUDA` sellada.** La condicion de la hija (*ya
  tienes definido que es tu entorno*) es el producto de la madre, y la hija anade los cuatro objetos y las dos preguntas sobre
  los otros grupos (L27). La duda sigue escrita: L27 no remite con palabras como L29.
- **`planificar_tres_pasos` a sus tres partes, `D.37`: SOSTENGO LAS TRES.** L19 enumera la serie (*Step 1 is to establish
  projected need or demand ... Step 2 is to establish your present status ... Step 3 is to compare and reconcile*), y los pasos
  `2`, `3` y `5` de la cabeza la copian; cada parte es la pieza de su paso (`STEP 2` en L33, `STEP 3` en L37 y L39; el paso `1`
  en L29, con la `DUDA` sellada de que la pieza `STEP 1` tiene tres nodos y la parte es el que produce la demanda).
- **Y ninguna de las tres partes entre si**: es lo que la `ACTA 70` `70.5` adjudico (`D71.12`, *encadenarse no es
  continuarse*), y hoy lo leo igual con los pasos delante: los siete de `cerrar_brecha` son las dos preguntas, la decision y la
  estrategia, y ninguno prolonga un paso de `examinar_demanda` ni de `determinar_estado`. **No lo reabro** (`D.47`): lo escribo
  para que se vea que lo releo y que se sostiene.
- **`elegir_modo` a `escalonar_complejidad`, `D.29`: SOSTENGO, con la `DUDA` sellada.** L63 remite con palabras al modelo de la
  madre (*Let's apply our model to the work of a new employee*), y los pasos `1` y `2` de la hija usan sus dos variables (interes
  propio, factor CUA bajo), que son el producto de los pasos `1`, `2` y `4` de la madre; la hija anade la promocion escalonada y
  la promocion interna (pasos `3` a `9`). La duda: la hija no elige un modo de control, elige el puesto.

**`d170`, CON LA SALIDA DELANTE:** mi barrido no levanta el par `elegir_estilo_direccion_madurez_relevante_tarea` con
`fijar_frecuencia_reunion_individual_madurez_tarea`, y `elegir_estilo` no levanta a nadie:

    $ grep -c "fijar_frecuencia_reunion_individual_madurez_tarea" .v71aud/vecinos_tabla.txt; grep "^    elegir_estilo" .v71aud/vecinos_tabla.txt
    0
        elegir_estilo_direccion_madurez_relevante_tarea          479   0   0   0

**Por mi lectura, sin linea ni arista** (`D69.3`). Si la aduana de hoy lo levanto, lo vere en la bitacora en mi turno normal.

## 6. **`R8` MEDIDO SOBRE MI ENCARGO DE LA `72`, Y LO ROMPO** (`ACTA 70` `70.12`)

`R8` dice: *toda cifra de medida que escriba en `PROMPT_SIGUIENTE.md` (un reloj, una banda, una cuenta sacada de un fichero)
**lleva al lado su bloque `$` con la salida, o la seccion del acta donde esta pegada***. El instrumento imprime las lineas de
prosa de mi encargo que traen alguna cifra y ninguna seccion de acta:

    $ python .v72aud/r8_encargo.py
      L1 ['20', '50', '6'] | # ENCARGO DE LA VUELTA 72: **LAS `20` FILAS DE `.v71ext/orden.txt` DENTRO, UNA POR VEZ, CON LAS `50` LINEAS Y LAS `6` ARISTAS QUE LAS DOS LECTURAS YA
      L3 ['71'] | *Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 70`, que audito la vuelta `71`.
      L19 ['67', '68', '70'] | **El metodo de la `67`, la `68` y la `70` vale**: cada `insertar` lanzado como un proceso por una copia de `.v68ext/insertar.py`, y tu
      L22 ['73', '23'] | dices en el reporte con las filas que faltan, y entran en la `73`. El `23` sep tres asientos cerraron diciendo que esperaban un
      L25 ['20', '70'] | **EL RELOJ, MEDIDO, Y NO SON TECHOS: SON LO QUE COSTO.** Los `20` `insertar` de la `70`, con la aduana de antes del reparto del
      L31 ['71', '1'] | y el barrido de la `71`, ya con la senial `1` repartida (`68d6946`), cinco fichas a la vez, por ficha y ordenado por valor:
      L47 ['8', '4'] | **El orden de la campania es Grove, Gerber, Marquet** (`PARALELO.md` `8` punto `4`). **La frase de *continuar desde `cap_18`* es de
      L68 ['20'] | iguales a su blob en `682a39c`**, y sus `20` huellas iguales a las de `.v71ext/pasos_y_huellas.txt`. Si una sale distinta, no entra,
      L71 ['20'] | ## TAREA 3: **LAS `20` FILAS DE `.v71ext/orden.txt`, UNA POR VEZ**
      L73 ['1', '20', '9', '1', '2', '3', '2', '3'] | **En su orden, filas `1` a `20`**: las `9` de `cap_07`, `1` de `cap_10`, `2` de `cap_11`, `3` de `cap_12`, `2` de `cap_13` y `3` de
      L78 ['5'] | `examinar_entorno_expectativas_tecnologia_proveedores_grupos` en la fila `5`, y a
      L79 ['6'] | `examinar_demanda_entorno_dos_marcos_temporales` en la fila `6`.
      L80 ['67', '68'] | 2. **Las cuatro aristas por lectura, con `python forja.py arista` en el acto de insertar el hijo**, como en la `67`, la `68` y la
      L81 ['70'] | `70`, con su cita y su `--paso` el de la madre que su fila `SOSTENGO` de `.v71ext/aristas_lectura.txt` cita:
      L82 ['6'] | `planificar_tres_pasos_demanda_estado_brecha` a `examinar_demanda_entorno_dos_marcos_temporales` (fila `6`), a
      L83 ['7', '8'] | `determinar_estado_presente_capacidades_proyectos_merma` (fila `7`) y a `cerrar_brecha_dos_preguntas_estrategia` (fila `8`),
      L84 ['12'] | las tres por `D.37`; y `elegir_modo_control_motivacion_factor_cua` a `escalonar_complejidad_puesto_empleado_nuevo` (fila `12`),
      L86 ['16'] | 3. **`d170`, EN LA FILA `16`**: `elegir_estilo_direccion_madurez_relevante_tarea` entra **sin linea ni arista** con
      L93 ['70'] | 5. **Al volver cada `insertar`, su fila en el reporte** como las de la `70`: la aduana de hoy con sus vecinos, las lineas que
      L98 ['6'] | Al terminar la ultima fila que entre: **cuantas se esperaban (`6`, la ultima linea de `.v71ext/orden.txt`), cuantas viven en el
      L100 ['6'] | entro, la cuenta dice cuales de las `6` quedan pendientes con ella.
      L104 ['410', '1027', '1', '27'] | - **El censo antes y despues**: nodos, veredictos, pares mutuos, bandeja de Grove e insertados. Al abrir son `410`, `1027`, `1`, `27`
      L111 ['72'] | cambiada a la `72`, y pegado.
      L125 ['7'] | - **NO TOCAS LAS `7` FICHAS DE `cap_15`, `cap_16` Y `cap_17`**: se preparan en la vuelta siguiente.
      L130 ['11'] | - **NO ABRES NINGUN LIBRO.** El mundo `11` cierra con siete.
    lineas del encargo: {'prosa con cifra y SIN seccion': 25, 'prosa sin cifra': 84, 'prosa con cifra y con seccion': 15, 'linea de bloque sangrado': 11} | suma: 135

**LECTURA, linea por linea, que es mia y no del instrumento:**

- **Las mas de esas `25` lineas no traen cifra de medida**: numeros de vuelta (`67`, `68`, `70`, `71`, `72`, `73`), la fecha del
  `23` sep, la seccion `8` punto `4` de `PARALELO.md`, la senial `1`, las filas `5` a `16` del orden y el mundo `11`.
- **Otras traen cifra de medida sostenida en la linea de al lado**: `L25` y `L31` abren los dos bloques `$` del reloj; `L68`
  sigue a `L67`, que cita `70.1`; `L73` sigue en `L74`, que cita `70.6`; `L104` sigue en `L105`, que cita `70.1`; y las del
  titulo (`L1`) y de `L71` son, ademas del `6` de abajo, las `20` y las `50` que el cuerpo sostiene con `70.6` y `70.3`.
- **TRES CIFRAS DE MEDIDA SIN BLOQUE `$` Y SIN SECCION, Y ESO ROMPE `R8`:**
  1. **`L125`: *las `7` fichas de `cap_15`, `cap_16` y `cap_17`***, una cuenta de la bandeja, sin nada al lado.
  2. **`L106`: *como en la `70` (`118` mas `5`)***, la cuenta de lineas de bitacora de la `70`, sin seccion. **El instrumento no la
     levanta** porque su linea trae `70.3` para las `50` de su principio; la encuentro leyendo, y lo digo porque es el hueco del
     instrumento.
  3. **`L98` y `L100` (y el `6` del titulo, `L1`, que es la misma cifra): *las `6` aristas*, con *la ultima linea de `.v71ext/orden.txt`* al lado**, que es una ruta y no un bloque
     `$` ni una seccion de acta. Es la mas discutible de las tres: la ruta apunta a la linea exacta.
- **Las tres son CIERTAS**, y aqui esta lo que les faltaba al lado:

    $ for i in $(ls cuarentena/grove_high_output | sed 's/\.json$//'); do awk -v i="$i" '$2 == i {print $1}' .v70aud/normal/bandeja_grove.txt; done | sort | uniq -c
          3 cap_15
          1 cap_16
          3 cap_17
    $ grep -c "" .v71ext/orden.txt; tail -1 .v71ext/orden.txt
    36
      CONTINUA con madre= (aristas distintas): 2 | SOSTENGO por lectura: 4 | solapes entre las dos: 0 | aristas esperadas: 6
    $ grep -n "lineas nuevas: 123" docs/loop/ACTA_AUDITOR.md
    47851:    lineas nuevas: 123 | por tipo: {'veredicto': 118, 'arista declarada por lectura (D.37)': 5} | suma: 123

  (las `7` fichas que quedan hoy son `3`, `1` y `3` de esos tres capitulos; las `6` aristas son la ultima linea del orden; y las
  `118` lineas y las `5` por lectura de la `70` estan pegadas en la `ACTA 69` `69.3`, con su suma). **No hay dano en dato: el extractor tenia las tres cifras donde yo decia.**
- **PERO ES UN REMEDIO MIO, DE CIFRAS, ROTO EN SU PRIMERA SEDE, EL MISMO TURNO EN QUE LO ESCRIBI.** Es sustancia de auditoria
  (`REMEDIO ROTO`, `D.38.2`, acotado el 12 sep a *clases, cifras, lecturas, herencia*), y **lo cargo en mi acta**: mi racha
  `AUDITOR` pasaria de `1 de 3` a `2 de 3`, que es su penultimo escalon, y **eso obliga a que la `ACTA 71` encargue su remedio como
  tarea bloqueante mia** (`5.5`, *la escalada se encarga*). Lo adjudico alli con el reporte delante y sin rebajarlo aqui.

## 7. **LO QUE DEJO PARA MI TURNO NORMAL, ESCRITO ANTES DE VER EL REPORTE**

1. **`R5`** en su reporte, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` sacados otra vez de los originales y con
   la cabecera cambiada a la `72`.
2. **Las `54` lineas nuevas de la bitacora, una a una**: las `50` contra las vivas de `.v71ext/veredictos_listos.txt` y contra mis
   clases selladas con la `70.5`, y **par a par contra las `50` filas de mi barrido**, que es lo que prueba por el dato que el
   cambio de `src/aduana.py` de las `21:43` no movio lo que la aduana levanta; y las `4` de `forja.py arista` contra mis cuatro
   `SOSTENGO` de la seccion `5`, con su paso. Y **`d170`**: ninguna linea del par.
3. **Las `6` aristas, par a par**, contra `.v72aud/esperado_72.py`, y que **ningun nodo viejo cambio** (ya medido por cuenta en la
   seccion `2`; alli, con identidad).
4. **Que cada `insertar` volvio con su `.fin` en `0`, en el orden de `.v71ext/orden.txt`, uno por vez y sin solaparse**, y que
   **ninguna aduana levanto un vecino fuera de mi barrido**.
5. **La muestra pineada de los `SANO`** que la `72` escribio en la bitacora, **con semilla `72`**, el tamaño de la seccion `7` de
   `AUDITOR_FORJA.md` y su banda, releida contra mis clases selladas.
6. **El censo, las guardas y el cierre estricto**, que tallara esta pagina: no tiene tablas, asi que un rojo en el suyo sera
   suyo. Y el coste de su turno, `7,03` USD en `13455` s, contra su clase (`D.55`).
7. **`R8`**: la caida de la seccion `6` en mi tanda, y **el encargo de la `73` escrito con cada cifra de medida con su bloque `$` o
   su seccion**, medido con `.v72aud/r8_encargo.py` antes de cerrarlo y leido a mano donde el instrumento no llega.

## 8. **ESTA PAGINA CONTRA `R6`, `R7` Y LOS GUIONES, MEDIDA SOBRE ELLA MISMA**

El generador corre dos veces, y estos bloques de la segunda pasada leen la pagina que escribio la primera, identica salvo ellos.
El primero cuenta las lineas de bloque `$` que empiezan por una clave de relacion (las que la nombran en mis frases y comandos no
cuentan, porque la nombran para decir que no la imprimo); el segundo, las lineas de bloque que reparten en clases, y cuantas traen
su `suma`; el tercero, las rayas y guiones medios de la pagina:

    $ grep -c -E "^    +(previos|siguientes|nodos_previos|nodos_siguientes)" docs/loop/APERTURA_CIEGA.md
    0
    $ python .v72aud/r7_pagina.py
    lineas de bloque que reparten en clases: 32 | por estado: {'con suma': 32} | suma: 32
    $ grep -c -P "\x{2014}|\x{2013}" docs/loop/APERTURA_CIEGA.md
    0
