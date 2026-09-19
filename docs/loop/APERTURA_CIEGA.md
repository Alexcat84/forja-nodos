# APERTURA CIEGA, VUELTA 46, lote 7 (`grove_high_output`), `cap_04`

> **Fase ciega del auditor** (`D.34`, `D.34.2`). Escrito ANTES de que el arnes me
> exponga `docs/loop/REPORTE.md`. Lo que va aqui es **mi** lectura del material,
> hecha sobre `cuarentena/` y `fuentes/`, para que despues pueda compararse con la
> del extractor.
>
> **`D.38.3` manda en este fichero: clases y lecturas, no cifras contadas a mano.**
> Toda cifra de abajo lleva pegado el comando que la produjo, con su linea `$`. Y
> toda conclusion sobre contenido va en linea aparte marcada `LECTURA`.

---

## 0. LA DECLARACION QUE EL ARNES EXIGE (`D.40`)

    ACTA ANTERIOR LEIDA: 8f293bd5ea02070c5be66db963120cb836fc08ed

**HEREDADOS: CERO.** No declaro ningun `HEREDADO n`, y no por olvido: el
instrumento de la casa dice que no hay ninguno, y su salida va pegada.

    $ python forja.py herencia
      acta anterior : ACTA 44. VUELTA 45, lote 7 (`grove_high_output`): ...
      su huella     : 8f293bd5ea02070c5be66db963120cb836fc08ed
      heredados     : 0

    El acta anterior no dejo ninguna tarea bloqueante ni ningun remedio escrito.
    Aun asi tienes que declarar la linea de lectura.

**La huella que declaro es la que el prompt y el instrumento me dan, y las dos son
la misma.** No es la huella del fichero: el fichero de hoy mide otra cosa, y lo digo
para que nadie confunda las dos.

    $ sha256sum docs/loop/ACTA_AUDITOR.md
    2e398e450b7d885036a4049af7a33049f3e054f25974e4d5b70b99b4272d2f9f *docs/loop/ACTA_AUDITOR.md

## 0.1. LO QUE EL ARNES ME RETIRO, COMPROBADO EN EL UNICO SITIO QUE NO RETIRA

    $ tail -3 docs/loop/loop.log
    [2026-09-19 03:01:10] VUELTA 2 : APERTURA CIEGA (claude-opus-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl
    [2026-09-19 03:01:10]   hereda 0 remedio(s) del acta anterior, entregados en el prompt (D.40)
    [2026-09-19 03:01:10]   y solo eso: remedios con su motivo, sin cifras ni conclusiones (D.52)

**No he recuperado ninguno de los cuatro.** Lo que si leo, y el protocolo lo
autoriza por escrito, es `docs/loop/ACTA_AUDITOR.md`, que es obra mia y no del
extractor.

---

## 1. LA CONTAMINACION QUE ME CAUSE YO, Y LA DECLARO ANTES DE NADA

**Para saber QUE OCHO candidatos son el lote corri `git show --stat --name-status`
sobre los commits de la vuelta, y con el listado de ficheros me vino el MENSAJE DE
COMMIT entero.** Los mensajes de commit no son ninguno de los cuatro ficheros que
`D.34.2` retira y nadie me los habia retirado, pero **contienen cifras del
extractor**, y esta fase existe para que yo llegue sin ellas. **Era evitable**:
`git show --name-status --format=` me habria dado los nombres sin el cuerpo.

**LO QUE VI, DICHO ENTERO PARA QUE NADIE TENGA QUE ADIVINARLO**: que declara `8`
candidatos minados en `cap_04`; que declara `2 ENTRARIAN`, `6 BLOQUEARIAN`,
`0 CAERIA` y `13` pares de cola de lectura; que declara **cero inserciones** por la
puerta de `D.39`; que declara `505,5` s de aduana por candidato contra `385`
estimados; que declara la poblacion del barrido pasando de `372` a `379`; que
declara `0 PUENTE` de `50` pasos escritos; y que declara `22` nodos de frontera
contra un techo de `15`.

**QUE LE HACE ESTO A LO QUE ESCRIBO ABAJO, dicho cifra a cifra:**

| cifra mia de abajo | sigue siendo ciega? |
|---|---|
| **identidad de los 8 candidatos** | **SI.** Sale de `--name-status`, que es mecanico |
| **`50` pasos** | **NO ES CIEGA.** La cuento yo con mi contador, pero ya habia visto el `50`. **Coincide, y aun asi no la publico como confirmacion independiente** |
| **`0 PUENTE`** | **NO ES CIEGA DE EXPECTATIVA.** El mapeo paso a paso contra la fuente lo hago yo y renglon a renglon, pero llegue a el sabiendo que el esperaba cero |
| **poblacion `542` y `379`** | **SI.** El `542` lo mido yo; el `379` lo derivo al descontar `ensayo_referencia_163` y **solo entonces** cae encima del suyo |
| **la clase de cada candidato** | **SI.** El mensaje no dice de ningun candidato si continua o repite: dice cuantos entrarian y cuantos bloquearian, que es la puerta y no la clase |
| **mis tres discutibles de la seccion 6** | **SI.** Ninguno de los tres aparece en nada de lo que vi |

**No me absuelvo con la tabla: la escribo para que el acta pueda pesarlo.** Si la
seccion de credito de mi acta decide que esto es una caida mia, **que la cargue con
mi nombre**, que es lo que el protocolo manda hacer con los errores propios.

---

## 2. LOS INSTRUMENTOS QUE CORRI EN ESTA FASE

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada,
               vuelta, cita_incompleta, deprecado_en_superficie, arista_rota,
               arista_incompleta, guiones, censo_no_decrece

    $ wc -l dataset/nodos.jsonl
    346 dataset/nodos.jsonl

    $ wc -l fuentes/grove_high_output/cap_04.md
    323 fuentes/grove_high_output/cap_04.md

    $ wc -w fuentes/grove_high_output/cap_04.md
    8871 fuentes/grove_high_output/cap_04.md

    $ python scripts/deuda.py
    DEUDA DE LA LINEA (D.55): la deuda no bloquea la produccion
      pendientes: 9    pagadas: 8
      ultima vuelta de saneamiento: 44

### 2.1. UN INSTRUMENTO QUE EN ESTA FASE NO PUEDE MEDIR, Y ESCRIBO LA LIMITACION

    $ python forja.py credito
    CREDITO DE LA LINEA 'serial' (D.48)
      registro: docs/loop/CREDITO_serial.jsonl
      LINEA SIN REGISTRO: no hay ningun suceso escrito.

**ESA SALIDA ES CIERTA Y SU LECTURA SERIA FALSA.** `CREDITO_serial.jsonl` es uno de
los cuatro ficheros que el arnes retiro para mi turno, y esta nombrado en la linea
del `loop.log` que copie arriba. **El instrumento no dice que la racha este en cero:
dice que no encuentra el fichero.**

`LECTURA`: **en esta fase no puedo medir ninguna racha de credito**, ni la mia ni la
del extractor, y por eso **no publico ninguna aqui**. Va entera al turno normal.

---

## 3. LA POBLACION DEL BARRIDO DE VECINOS (`D.38.4`)

`D.38.4` manda barrer **grafo mas bandejas**, descartando `_insertados` y
`_derivadas`. Eso es lo que mide mi barrido, y su cabecera lo dice:

    $ python barrido.py <los 8 candidatos>
    POBLACION D.38.4 (grafo + bandejas, sin _insertados ni _derivadas): 542
      grafo dataset/nodos.jsonl : 346
      BANDEJA/ensayo_referencia_163     : 163
      BANDEJA/grove_high_output         : 30
      BANDEJA/marquet_turn_the_ship     : 3

`LECTURA`: **`542` y `379` no son una discrepancia: son dos poblaciones distintas.**
`542` menos los `163` de `ensayo_referencia_163` da exactamente `379`, que es el
numero con el que la aduana trabaja. **Lo dejo medido aqui y lo llevo al turno
normal como pregunta de una linea**: si `ensayo_referencia_163` es bandeja a efectos
de `D.38.4`, el vecino mas cercano de un candidato puede vivir en un sitio donde la
aduana no mira. **No lo resuelvo en la fase ciega y no lo convierto en cifra.**

---

## 4. LA CLASIFICACION, CANDIDATO A CANDIDATO

**Los ocho son de `cap_04`, y los ocho lo dicen ellos mismos**, que es justo la
caida que el protocolo me pone delante con mi propio ejemplar del acta anterior:

    $ python - (UNIDAD DE ORIGEN declarada por cada uno de los 8)
      subir_productividad_gerencial_tres_vias        SI  fuentes/grove_high_output/cap_04
      buscar_actividad_alta_palanca_tres_vias        SI  fuentes/grove_high_output/cap_04
      elegir_momento_actividad_palanca_maxima        SI  fuentes/grove_high_output/cap_04
      reunir_informacion_gerencial_vias_variadas     SI  fuentes/grove_high_output/cap_04
      escalonar_fuentes_informacion_gerencial        SI  fuentes/grove_high_output/cap_04
      programar_visita_area_observar_despachar       SI  fuentes/grove_high_output/cap_04
      transmitir_objetivos_prioridades_preferencias  SI  fuentes/grove_high_output/cap_04
      empujar_persona_reunion_direccion_preferida    SI  fuentes/grove_high_output/cap_04
      declaran unidad: 8 de 8

**LA VARA CON LA QUE CLASIFICO ES LA DE LA SECCION 6.1 DE MI PROTOCOLO**, y la
aplico con su direccion: que anade el HIJO a la MADRE, sin bascula, y mirando si lo
que queda fuera del solape es procedimiento **en los dos lados**.

### 4.1. `subir_productividad_gerencial_tres_vias`

**MI CLASE: `SANO`, y es la CABEZA de la serie.** Sale de `L195` a `L201`, el unico
tramo del capitulo que enumera las tres vias de la productividad del mando. Vecino
mas proximo del barrido: `buscar_actividad_alta_palanca_tres_vias`, a `0.1167`, que
es **su propia hija declarada**. Fuera de la bandeja de `grove`, su vecino mas alto
es `minimizar_impuesto_colaboracion_equipo` a `0.0536`.

`LECTURA`: **ningun nodo del grafo enumera esas tres vias**, asi que no hay a quien
repetir.

### 4.2. `buscar_actividad_alta_palanca_tres_vias`

**MI CLASE: `CONTINUA` de `subir_productividad_gerencial_tres_vias` por su paso 3,
con arista `D.37`.** Y la sostengo con la vara, no con una senial: el paso 3 de la
madre es **una linea que NOMBRA** (`Sube la palanca asociada a las distintas
actividades de mando que haces`), y la hija trae **cuatro pasos propios que la madre
no tiene**. La regla `NOMBRAR NO ES PROCEDIMENTAR` (`P.5.1`) corta justo por aqui, y
corta **a favor de la hija**.

La cuenta que `D.37` exige **esta escrita en el libro**, no la puso el extractor:

    $ grep -n -i -E "three basic ways|three ways" fuentes/grove_high_output/cap_04.md
    195:Managerial productivity ... can be increased in three ways:
    207:These can be achieved in three basic ways:

### 4.3. `elegir_momento_actividad_palanca_maxima`

**MI CLASE: `SANO`.** Sale de `L215` y `L217`. Su asunto es **cuando** se ejerce una
actividad; el de su vecino `buscar_actividad_alta_palanca_tres_vias` (a `0.1058`) es
**cual** es. La oportunidad del momento no es ninguna de las tres vias que la otra
enumera: el libro la introduce mientras ilustra la primera, pero lo que afirma
(`leverage that depends, however, on when it is performed`, `L215`) es doctrina
aparte.

`LECTURA`: **hermanos, y no madre e hija.** Por eso `SANO` y no `CONTINUA`.

### 4.4. `reunir_informacion_gerencial_vias_variadas`

**MI CLASE: `SANO`.** Sale de `L145` y `L147`. Los dos vecinos del grafo que mas se
le acercan por asunto los abri enteros antes de decidir, y **ninguno hace lo que
este hace**: `pedir_hechos_decision_evitar_recomendaciones` (Scott) manda **que**
pedir, no **por donde**; `bajar_detalle_organizacion_fuente_hechos` (Scott) manda
saltarse las capas de mando. **Procedimiento propio en los dos lados: FRONTERA, y no
duplicado.**

### 4.5. `escalonar_fuentes_informacion_gerencial`

**MI CLASE: `SANO`, con frontera declarada contra `4.4`.** Los dos salen del mismo
capitulo y son vecinos entre si a `0.0763`, que es **el par mas alto del barrido que
no es madre e hija**. **Y comparten una afirmacion**: que lo verbal va primero. La
sostiene el libro dos veces, en `L147` y en `L153`, asi que **la repeticion es del
libro y no del extractor**.

Lo que queda fuera del solape es procedimiento en los dos lados: `4.4` **enumera
canales**; este **los ordena por escalones y manda solaparlos para verificar**
(`L153`: `Your information sources should complement one another, and also be
redundant because that gives you a way to verify what you have learned`).

Su vecino mas alto fuera de `grove` es
`montar_reunion_general_presentaciones_preguntas` a `0.0515`, que no es del asunto.

### 4.6. `programar_visita_area_observar_despachar`

**MI CLASE: `SANO`.** Sale de `L155` y `L157`. El candidato a duplicado era
`bajar_detalle_organizacion_fuente_hechos` del grafo, y **lo abri entero antes de
decidir**: aquel manda ir a la fuente de los hechos y no dejar que lleguen por capas
de mando; este manda ir a un area, **despachar alli lo de dos minutos**, y vencer el
reparo con una visita programada que lleve una tarea formal. **Nada del inventario de
uno esta en el otro.** El barrido lo respalda: su vecino mas alto del grafo es
`revisar_tres_preguntas_valor_carrera` a `0.0625`, que no es del asunto.

### 4.7. `transmitir_objetivos_prioridades_preferencias`

**MI CLASE: `SANO`.** Sale entero de `L159`. Abri
`alinear_prioridades_reporte_directivo` (Zhuo) por si repetia: aquel es la mecanica
de la reunion individual con las tres pes; este dice **por que** hay que impartir
objetivos y preferencias, con su propia razon escrita en el renglon (`only if the
manager imparts these will his subordinates know how to make decisions themselves
that will be acceptable`). **Frontera.**

### 4.8. `empujar_persona_reunion_direccion_preferida`

**MI CLASE: `SANO`.** Sale entero de `L167`. Su vecino mas alto en todo el barrido de
`542` es `comprobar_equipo_ejecuta_bien` a `0.0531`, que no es del asunto.

`LECTURA`: **el empujon del libro es una clase de acto que el grafo no tiene**: mas
que informar y menos que ordenar. `persuadir_emocion_oyente_no_propia` (Scott)
trabaja **despues** de una decision tomada; este trabaja donde **todavia no hay**
decision.

### 4.9. EL RESUMEN DE MI CLASIFICACION

| mi clase | cuantos | cuales |
|---|---|---|
| **`SANO`** | **7** | `4.1`, `4.3`, `4.4`, `4.5`, `4.6`, `4.7`, `4.8` |
| **`CONTINUA` con arista `D.37`** | **1** | `4.2`, hija de `4.1` por su paso 3 |
| **`REPITE`** | **0** | ninguno |

**CERO `REPITE`, y digo con que lo sostengo**: el par de solape mas alto de todo el
barrido de `542` es `0.1167`, y es **madre e hija declaradas**. El par mas alto que
NO es madre e hija es `0.1058`, y el mas alto de un candidato contra el grafo es
`0.0748`.

---

## 5. FIDELIDAD `D.30`, LEIDA POR MI PASO A PASO

    $ python - (contador de pasos sobre los 8 candidatos de cap_04)
      subir_productividad_gerencial_tres_vias           4 pasos
      buscar_actividad_alta_palanca_tres_vias           4 pasos
      elegir_momento_actividad_palanca_maxima           7 pasos
      reunir_informacion_gerencial_vias_variadas        8 pasos
      escalonar_fuentes_informacion_gerencial           7 pasos
      programar_visita_area_observar_despachar          8 pasos
      transmitir_objetivos_prioridades_preferencias     5 pasos
      empujar_persona_reunion_direccion_preferida       7 pasos
                                                       50 TOTAL

    $ python - (mapa paso -> linea fuente, verificado contra el fichero)
      subir_productividad_gerencial_tres_vias        4 pasos -> lineas [195, 197, 199, 201]
      buscar_actividad_alta_palanca_tres_vias        4 pasos -> lineas [207, 209, 211, 213]
      elegir_momento_actividad_palanca_maxima        7 pasos -> lineas [215, 217]
      reunir_informacion_gerencial_vias_variadas     8 pasos -> lineas [145, 147]
      escalonar_fuentes_informacion_gerencial        7 pasos -> lineas [153]
      programar_visita_area_observar_despachar       8 pasos -> lineas [155, 157]
      transmitir_objetivos_prioridades_preferencias  5 pasos -> lineas [159]
      empujar_persona_reunion_direccion_preferida    7 pasos -> lineas [167]
      TOTAL pasos mapeados: 50 ; lineas fuente distintas usadas: 17
      todas las lineas existen y no estan vacias: True

`LECTURA`: **los `50` pasos los case uno a uno con su renglon y NO ENCUENTRO NINGUN
`PUENTE`.** Cada paso dice algo que esta en esas `17` lineas.

**Y lo digo con su limite, que es la seccion 1**: no llegue a esta lectura sin saber
que el extractor esperaba cero. **El mapeo es mio y es verificable renglon a
renglon; la expectativa con la que lo hice no era ciega.**

---

## 6. MIS TRES DISCUTIBLES, MARCADOS AQUI ANTES DE VER EL REPORTE

Los marco para que despues se pueda medir si acerte, que es lo unico que hace
informativa a la metrica (`5.1` de mi protocolo).

### 6.1. `reunir_informacion_gerencial_vias_variadas` DICE `SEIS` Y EL LIBRO DICE `MANY`

Es el mas serio de los tres, y **no esta en un paso: esta en el
`entregable_esperado`**, que dice `Las vias por las que te llega la informacion,
nombradas una a una y las seis en uso`.

    $ grep -n -i "many ways" fuentes/grove_high_output/cap_04.md
    145:... And as you can also see, I use many ways to get it. ...

    $ grep -c -i "six ways" fuentes/grove_high_output/cap_04.md
    0

`LECTURA`: **el libro dice `many`, y nunca dice `six`.** El `seis` es el numero de
pasos que el propio candidato escribio, elevado a cuenta del libro. Es exactamente la
distincion que otro candidato de esta misma tanda cuida con nombre y apellido
(`D.37` frente a `D.29`): **`D.37` pide que el texto diga CUANTAS partes tiene, y
aqui el texto dice que son muchas.**

**NO lo llamo `PUENTE` de paso**, porque no esta en un paso y `D.30` cuenta pasos.
**Lo llamo cifra inventada dentro de la ficha**, y lo llevo al turno normal.

### 6.2. `escalonar_fuentes_informacion_gerencial`, PASOS 3 Y 4: LA ANALOGIA SE CAE

El paso 2 conserva la analogia del libro (`igual que el titular de un periodico`),
pero el 3 y el 4 la sueltan: `Baja despues al articulo entero` y `Termina en la
reiteracion y la perspectiva, que es lo que dan una revista de actualidad o incluso
un libro`.

`LECTURA`: **leidos como procedimiento, esos dos pasos mandan leer periodicos y
revistas**, y en `L153` el periodico es **la comparacion**, no la fuente. El propio
libro resbala ahi (`So you then read the newspaper article itself`), asi que **lo
sostengo como `TRANSCRIPCION` y lo marco igual**: si cae, cae DENTRO de mi marcado.

### 6.3. `elegir_momento_actividad_palanca_maxima`, PASO 2: UN CASO VUELTO PRECEPTO

El paso 2 manda `define con antelacion exactamente que informacion hay que reunir y
presentar en cada etapa del proceso`. En `L215` eso **lo hace Robin**, y es un CASO
(manual 3.5).

`LECTURA`: **lo sostengo como `TRANSCRIPCION`** porque el mismo renglon generaliza
(`Work done in advance of the planning meeting obviously has great leverage`) y
porque `L217` cierra con el precepto (`a manager must keep timeliness, which is often
critical, firmly in mind`), que es el paso 7. **Pero la generalizacion la hizo el
extractor y no el libro, y por eso la marco.**

---

## 7. LA PUERTA DE `D.39`, MEDIDA EN EL ARBOL Y NO SUPUESTA

    $ python -c (config/frentes.json, clave cerrados_en_extraccion)
    {
     "smart_who":            { "cita": "ACTA 8 seccion 10" },
     "zhuo_manager":         { "cita": "ACTA 13 seccion 8.1" },
     "scott_radical_candor": { "cita": "ACTA 24" }
    }

    $ ls cuarentena/grove_high_output/*.json | wc -l
    30

`LECTURA`: **`grove_high_output` NO esta en esa lista.** El lote 7 sigue ABIERTO, asi
que `D.39` **no deja entrar nada** aunque la aduana lo bendiga. Cualquier cifra de
`ENTRARIAN` de esta vuelta es **una medida en seco y no una insercion**, y asi la voy
a leer cuando se me exponga el reporte.

---

## 8. LO QUE ESTA FASE NO PUEDE COMPROBAR, DICHO COMO LIMITACION

1. **Ninguna racha de credito**, por la seccion `2.1`: el registro esta retirado.
2. **Nada de `REPORTE.md`**: ni sus cifras, ni su esqueleto, ni sus rutas. Retirado.
3. **La frontera de `22` nodos y el techo de `15`**: son cifras del turno del
   extractor que viven en el reporte retirado. **Aqui no las publico como mias.**
4. **El veredicto de la aduana candidato a candidato.** Deje corriendo
   `python forja.py informe` sobre `escalonar_fuentes_informacion_gerencial` y **al
   cerrar esta fase no habia terminado**: su fichero de salida seguia en cero bytes.
   **Lo declaro en vez de publicar un numero que no medi**, y la corrida entera va al
   turno normal.

---

## 9. LO QUE LLEVO AL TURNO NORMAL

| # | que | de donde sale |
|---|---|---|
| 1 | **el `seis` contra el `many`** de `4.4` | seccion `6.1`, con sus dos `grep` |
| 2 | **`ensayo_referencia_163`: bandeja para mi y no para la aduana** | seccion `3`, `542` contra `379` |
| 3 | **mi propia contaminacion por mensaje de commit** | seccion `1`, para que el acta la pese |
| 4 | **mis `7 SANO` y `1 CONTINUA`** contra lo que el reporte diga | seccion `4.9` |
| 5 | **`0 PUENTE` de `50`, con su limite escrito** | seccion `5` |
| 6 | **la aduana por candidato, sin correr** | seccion `8` punto 4 |

    ACTA ANTERIOR LEIDA: 8f293bd5ea02070c5be66db963120cb836fc08ed
