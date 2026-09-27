# APERTURA CIEGA DE LA VUELTA 64 (SANEAMIENTO, `grove_high_output`), LA QUE EL ARNES NUMERA `2` EN ESTA CORRIDA

*Auditor `claude-opus-5-5`, 23 sep 2026, fase ciega. Linea **serial**, rama `extraccion-mundo-11`.
Modo austero (`D.47`). Toda cifra de esta pagina sale de un instrumento corrido en esta fase y lleva
su salida pegada al lado (`D.38.3`); toda conclusion sobre contenido va en linea aparte marcada
`LECTURA`.*

## 0. LA HERENCIA (`D.40`)

    ACTA ANTERIOR LEIDA: 291e816f205a74483056cffaf06038e3dc242b6b
    HEREDADO 1: NO APLICA: R5 es del extractor y se comprueba en su reporte de la 64, retirado en esta fase
    HEREDADO 2: CUMPLIDO

**HEREDADO 1 (`R5`, del extractor): NO APLICA en esta fase.** `R5` es un remedio **del extractor** y
su sitio de comprobacion, escrito en la `ACTA 62` `62.13`, es *el reporte de la `64`*. **Ese reporte
esta retirado del arbol en esta fase** (`D.34.2`) y no lo recupero, asi que no hay nada que medir
aqui: se mide en mi turno normal, con `.v63aud/pegado63.py` apuntado al tramo de la `64`.

    $ ls docs/loop/REPORTE.md
    ls: cannot access 'docs/loop/REPORTE.md': No such file or directory

**Y aun asi me aplico su letra**: cada bloque `$` de esta pagina lleva lo que el comando imprimio y
nada mas; si alguno va cortado, se corta por el final y lo dice dentro del bloque con
`(recortado, entero en <fichero>)`.

**HEREDADO 2 (`R8`, mio): CUMPLIDO.** Mi metrica de fidelidad (seccion `3`) va con su **poblacion
escrita en el rotulo**: *los pasos de las seis fichas TAL COMO EL EXTRACTOR LAS ESCRIBIO, en su
version al abrir la vuelta `64` (`067c9df`)*, que es la poblacion que cuenta `PASOS INVENTADOS POR
CAPITULO` (`8`: pasos escritos). **No he medido el material corregido por la `64`**, y ninguna cifra
de esta pagina lleva el rotulo de la metrica encima de otra poblacion. Donde mido otra cosa (el
barrido de vecinos sobre las fichas de HOY, seccion `5`), el rotulo dice cual.

## 1. LO QUE ESTE TURNO NO VE, Y LO QUE SI VIO SIN BUSCARLO (`D.57`)

**La linea del arnes esta en el `loop.log` y la compruebo ahi:**

    $ grep -n '2026-09-23 10:40:19. VUELTA 2 : APERTURA CIEGA' docs/loop/loop.log
    5014:[2026-09-23 10:40:19] VUELTA 2 : APERTURA CIEGA (claude-opus-5-5), retirados: REPORTE.md ultimo_extractor.json ultimo_auditor.json CREDITO_serial.jsonl

    $ ls docs/loop/REPORTE.md docs/loop/ultimo_extractor.json docs/loop/ultimo_auditor.json docs/loop/CREDITO_serial.jsonl
    ls: cannot access 'docs/loop/REPORTE.md': No such file or directory
    ls: cannot access 'docs/loop/ultimo_extractor.json': No such file or directory
    ls: cannot access 'docs/loop/ultimo_auditor.json': No such file or directory
    ls: cannot access 'docs/loop/CREDITO_serial.jsonl': No such file or directory

**Los cuatro que la linea nombra estan fuera. `loop.log` esta dentro**, como dice la linea y en contra
del parrafo `AVISO` del prompt, que lo cuenta entre los retirados. **Manda la linea del arnes** (`D.57`),
y lo digo para que la contradiccion del prompt no viaje.

**TRES COSAS QUE ESTE TURNO VIO SIN BUSCARLAS, Y LAS DECLARO PORQUE UNA LECTURA CIEGA QUE LAS CALLA NO
ES CIEGA:**

1. **Los asuntos de los dos commits del extractor de la `64`.** Me llegaron en la foto de `git status`
   que el propio entorno pone al principio de mi contexto, y los volvi a ver al correr `git log` para
   fechar las fichas. El de `6e42f06` resume su fidelidad de `d005` con una cifra, y el de `997054d`
   resume su cierre. **No los busque, pero los he leido antes de clasificar**, asi que mi seccion `3`
   **no puede certificar que sea independiente de esa cifra**. Lo que si puedo decir es como la hice:
   paso a paso contra `cap_03`, con la linea al lado en `.v64aud/fidelidad.tsv`, y las dos dudas que
   me quedan las dejo como DUDA en vez de resolverlas hacia ningun numero. **LECTURA:** la foto de
   `git status` del entorno es una fuga de `D.34.2` que el arnes no controla; el asunto de un commit
   del extractor es un resumen de su reporte.
2. **La carpeta `.v64ext/` del extractor esta en el arbol, y dentro hay `reporte_t1_t2.md`,
   `reporte_t3.md`, `reporte_t3b.md`, `reporte_t4.md` y `reporte_t5.md`.** Lo se porque liste la raiz y
   esa carpeta **por nombre**; **no he abierto ningun fichero de `.v64ext/`**. **LECTURA:** son el
   reporte en trozos, y `D.34.2` retira `REPORTE.md` pero no sus borradores. Lo dejo escrito para el
   dueno del arnes, **sin doctrina nueva** (`D.55`): es un hueco de la retirada, no una regla.
3. **`python forja.py herencia` corrido en esta fase dice `heredados : 0` y *LINEA RECIEN NACIDA***,
   porque lee `CREDITO_serial.jsonl` y ese fichero esta retirado. **El prompt me entrega `2`**, y los
   declaro los dos arriba. **LECTURA:** el instrumento y el prompt no miden lo mismo en la fase ciega;
   el prompt lo calculo antes de retirar. No es mio arreglarlo (`D.45`).

## 2. EL ESTADO, MEDIDO EN ESTA FASE

    $ wc -l dataset/nodos.jsonl
    346 dataset/nodos.jsonl

    $ for b in cuarentena/*/; do echo "$b $(ls $b*.json 2>/dev/null | wc -l)"; done
    cuarentena/_derivadas/ 2
    cuarentena/_insertados/ 0
    cuarentena/ensayo_referencia_163/ 163
    cuarentena/gerber_emyth/ 22
    cuarentena/grove_high_output/ 91
    cuarentena/marquet_turn_the_ship/ 3
    cuarentena/onu_consumidor/ 0
    cuarentena/scott_radical_candor/ 0
    cuarentena/smart_who/ 0
    cuarentena/zhuo_manager/ 0

**`346` en el grafo y `91` en la bandeja de Grove**, los del encargo. La poblacion del barrido
(`D.38.4`) la escribe la propia aduana en la cabecera de cada informe de la seccion `5`.

**EL ALCANCE DE MI LECTURA ES EL DEL ENCARGO DE LA `64`** (`PROMPT_SIGUIENTE.md`, que es mio): la
fidelidad de los seis de `d005` (`T2.a`), sus vecinos (`T2.b`), los pares de los nueve `BLOQUEARIA` de
`d140` (`T3`) y los pares de `d141` (`T4`). **Las seis fichas las leo en su version al abrir la
vuelta**, sacada de git, **y no la de hoy**, para no ver en ellas la clase que el extractor les puso:

    $ for id in archivar_indicadores_resolver_problemas construir_grafico_escalonado_pronosticos construir_indicador_tendencia_patron elegir_fabricar_pedido_pronostico elegir_indicador_salida_trabajo_administrativo emparejar_indicadores_efecto_contraefecto; do echo "$id: $(git log --format='%h' -- cuarentena/grove_high_output/$id.json | tr '\n' ' ')"; done
    archivar_indicadores_resolver_problemas: a84b84e 
    construir_grafico_escalonado_pronosticos: 6e42f06 a84b84e 
    construir_indicador_tendencia_patron: 6e42f06 a84b84e 
    elegir_fabricar_pedido_pronostico: 6e42f06 a84b84e 
    elegir_indicador_salida_trabajo_administrativo: 6e42f06 a84b84e 
    emparejar_indicadores_efecto_contraefecto: 6e42f06 a84b84e 

    $ git diff --stat a84b84e 067c9df -- $(for id in archivar_indicadores_resolver_problemas construir_grafico_escalonado_pronosticos construir_indicador_tendencia_patron elegir_fabricar_pedido_pronostico elegir_indicador_salida_trabajo_administrativo emparejar_indicadores_efecto_contraefecto; do echo cuarentena/grove_high_output/$id.json; done) | wc -l
    0

**`067c9df` es el commit de apertura de la `64` y las seis fichas estan ahi igual que el `16` sep**:
esa es la version que escribio el extractor que las extrajo. `archivar_indicadores_resolver_problemas`
**no tiene commit de la `64`**; las otras cinco si (`6e42f06`). Las copias que leo estan en
`.v64aud/antes_<id>.json`.

## 3. LA FIDELIDAD DE LOS SEIS DE `d005`, ENTERA Y SIN MUESTRA (`D.30`, encargo `T2.a`)

**Cada paso contra su linea de `fuentes/grove_high_output/cap_03.md`**, una fila por paso en
`.v64aud/fidelidad.tsv` con la linea y la frase del libro que lo sostiene. **TRANSCRIPCION** si el libro
pone el medio, la etapa o el objeto; **PUENTE** si lo escribio el extractor.

### 3.1. **`PASOS INVENTADOS POR CAPITULO`, `cap_03`, POBLACION: LOS `41` PASOS DE LAS SEIS FICHAS TAL COMO LAS ESCRIBIO EL EXTRACTOR (version de `067c9df`, antes de cualquier correccion de la `64`). MI LECTURA CIEGA**

    $ python .v64aud/contar_fidelidad.py
    candidato                                        ficha filas   T   P  DUDA
    archivar_indicadores_resolver_problemas              4     4   4   0     0
    construir_grafico_escalonado_pronosticos             8     8   8   0     0
    construir_indicador_tendencia_patron                 6     6   6   0     0
    elegir_fabricar_pedido_pronostico                    9     9   9   0     0
    elegir_indicador_salida_trabajo_administrativo       7     7   7   0     0
    emparejar_indicadores_efecto_contraefecto            7     7   6   1     2
    total cap_03, seis de d005                          41    41  40   1     2
    PUENTE sobre pasos escritos: 1 de 41 = 2.44 por ciento
    si las 2 DUDA cayesen a PUENTE: 3 de 41 = 7.32 por ciento

**El instrumento cuenta los pasos de cada ficha de `067c9df` y comprueba que mi tabla trae una fila
por paso, ni mas ni menos: cero `DESCUADRE`.** Sale **`1` PUENTE de `41`**, y **`3` de `41` si las dos
dudas caen**. Las dos cifras quedan por debajo del `10` de `8.1`, asi que **el escalon no se mueve con
ninguna de las dos lecturas**.

**Y NO ES LA METRICA DE LA VUELTA:** la vuelta `64` es de saneamiento y mide seis fichas de `cap_03`, no
un capitulo entero. **El rotulo dice lo que medi y nada mas**, que es lo que `R8` me pide.

### 3.2. **EL PUENTE Y LAS DOS DUDAS, LOS TRES EN `emparejar_indicadores_efecto_contraefecto`**

| paso | mi clase | la linea del libro, y por que |
|---|---|---|
| `1`, *Antes de soltar un indicador, mira hacia donde va a dirigir la atencion, porque el indicador dirige la atencion... bicicleta* | **PUENTE de clausula** | L31 da **una propiedad** (*Indicators tend to direct your attention toward what they are monitoring... you will probably steer it where you are looking*) y **su remedio** (*you should guard against overreacting. This you can do by pairing indicators*). **La inspeccion previa, *antes de soltar... mira*, no la manda el libro**: el acto que manda es emparejar. El porque del paso si es del libro, y por eso es de clausula y no de paso entero |
| `2`, *Nombra el efecto que ese indicador va a empujar* | **TRANSCRIPCION, con DUDA** | *nombrar* no esta como orden; **pero el libro hace ese razonamiento en su ejemplo** (*you are likely to take action to drive your inventory levels down, which is good up to a point*) **y pone el objeto**, *effect*. Por `D.30` (*el libro pone el objeto*) va a TRANSCRIPCION. El lector estricto lo llama PUENTE, y por eso esta la segunda cifra |
| `3`, *Nombra el contraefecto, que es lo que se estropea si ese empuje se pasa de largo* | **TRANSCRIPCION, con la misma DUDA** | *your inventories could become so lean that you can't react to changes in demand without creating shortages*, y el objeto *counter-effect* |

**LECTURA:** los tres primeros pasos de `emparejar` montan un procedimiento de entrada (mirar, nombrar,
nombrar) sobre un parrafo que da una propiedad, un ejemplo y un remedio. **Es el reparto de `D.30`**: el
puente aparece donde el parrafo es mas pobre en actos. Los pasos `4` a `7` son del libro frase a frase
(L31 y L33).

**LOS OTROS CINCO, LIMPIOS, Y LO QUE MIRE DE CERCA PARA DECIRLO:** `archivar` paso `1` (*en vez de dejar
que se pierdan segun pasan los dias*) es la negacion del mismo acto de L99 (*If you do not
systematically collect and maintain an archive*), no un acto nuevo; `construir_grafico` paso `3`
(*marca con un asterisco*) sale de la leyenda de la figura, L95 (*\* means the actual number for that
month*); `construir_grafico` paso `5` convierte en orden el ejemplo de L93, que el propio libro abre
diciendo que ahi es donde el grafico rinde mas; `elegir_fabricar` paso `3` (*compara tu plazo con el de
tu competencia*) es la condicional de L105 puesta como etapa. **Los cuatro: TRANSCRIPCION.**

## 4. LA CLASE DE CADA UNO DE LOS SEIS COMO NODO, CON SUS LINEAS

| candidato | lineas | mi clase |
|---|---|---|
| `archivar_indicadores_resolver_problemas` | L99 | **nodo**, delgado: `4` pasos de un solo parrafo, pero con su inventario (recoger, banco, repasar, buscar desviaciones) |
| `construir_grafico_escalonado_pronosticos` | L91 a L97 | **nodo**, inventario rico |
| `construir_indicador_tendencia_patron` | L89 | **nodo**; un solo parrafo con cinco actos |
| `elegir_fabricar_pedido_pronostico` | L103 a L109 | **nodo**, inventario rico |
| `elegir_indicador_salida_trabajo_administrativo` | L35 a L67 | **nodo**; el paso `4` es la tabla de L39 a L67 entera |
| `emparejar_indicadores_efecto_contraefecto` | L31 a L33 | **nodo**, con el puente de `3.2` |

## 5. EL BARRIDO DE VECINOS DE LOS SEIS DE `d005`, SOBRE GRAFO MAS BANDEJAS Y CORRIDO EN ESTA FASE (`D.38.4`)

**POBLACION DE ESTA MEDIDA, Y NO ES LA DE LA SECCION `3`:** los seis informes corren sobre las fichas
**tal como estan HOY en la bandeja**, cinco de ellas con commit de la `64`. **El informe no imprime
pasos, solo ids, seniales y numero de paso**, asi que correrlo no me ensenia que corrigio el extractor.
Lo corri porque `d031` dice que retocar una ficha mueve su senial, y la lista de pares del encargo es
de las fichas de `067c9df`.

    $ cat .v64aud/barrido.log
    INICIO 2026-09-23 10:42:57
    archivar_indicadores_resolver_problemas rc=0 segundos=826
    construir_indicador_tendencia_patron rc=0 segundos=1326
    emparejar_indicadores_efecto_contraefecto rc=0 segundos=1519
    elegir_indicador_salida_trabajo_administrativo rc=0 segundos=1656
    construir_grafico_escalonado_pronosticos rc=0 segundos=1789
    elegir_fabricar_pedido_pronostico rc=0 segundos=1979
    TODOS TERMINADOS 2026-09-23 11:15:56

    $ python .v64aud/vecinos_hoy.py
    BLOQUEARIA  archivar_indicadores_resolver_problemas  hoy poblacion 462 | archivo: BLOQUEARIA poblacion 462
        SIGUE             cerrar_brecha_dos_preguntas_estrategia           similitud_texto            texto 0.353 familia 0.000 paso 0.393  paso 4 del candidato contra paso 6
        SIGUE             construir_indicador_tendencia_patron             similitud_texto            texto 0.361 familia 0.143 paso 0.420  paso 2 del candidato contra paso 3
        SIGUE             revisar_tres_preguntas_valor_carrera             similitud_texto            texto 0.369 familia 0.000 paso 0.414  paso 2 del candidato contra paso 1
        SIGUE             vencer_sindrome_grupo_pares_autoconfianza        similitud_texto            texto 0.364 familia 0.000 paso 0.405  paso 1 del candidato contra paso 5
    BLOQUEARIA  construir_grafico_escalonado_pronosticos  hoy poblacion 462 | archivo: BLOQUEARIA poblacion 462
        SIGUE             construir_indicador_tendencia_patron             similitud_texto            texto 0.365 familia 0.143 paso 0.453  paso 4 del candidato contra paso 5
        SIGUE             elegir_fabricar_pedido_pronostico                similitud_texto            texto 0.393 familia 0.143 paso 0.453  paso 7 del candidato contra paso 4
        SIGUE             emparejar_indicadores_efecto_contraefecto        similitud_texto            texto 0.378 familia 0.000 paso 0.434  paso 1 del candidato contra paso 3
    BLOQUEARIA  construir_indicador_tendencia_patron  hoy poblacion 462 | archivo: BLOQUEARIA poblacion 462
        SIGUE             archivar_indicadores_resolver_problemas          similitud_texto            texto 0.365 familia 0.143 paso 0.427  paso 2 del candidato contra paso 1
        SIGUE             construir_grafico_escalonado_pronosticos         similitud_texto            texto 0.362 familia 0.143 paso 0.461  paso 5 del candidato contra paso 4
        NUEVO             dimensionar_plantilla_administrativa_pronostico  similitud_texto            texto 0.373 familia 0.000 paso 0.405  paso 5 del candidato contra paso 6
        NUEVO             elegir_indicador_salida_trabajo_administrativo   similitud_texto            texto 0.378 familia 0.125 paso 0.378  paso 5 del candidato contra paso 3
        NUEVO             emparejar_indicadores_efecto_contraefecto        similitud_texto            texto 0.393 familia 0.143 paso 0.427  paso 5 del candidato contra paso 2
        NUEVO             equilibrar_capacidad_personal_inventario_plazo   similitud_texto            texto 0.353 familia 0.000 paso 0.424  paso 1 del candidato contra paso 4
    BLOQUEARIA  elegir_fabricar_pedido_pronostico  hoy poblacion 462 | archivo: BLOQUEARIA poblacion 462
        SIGUE             construir_grafico_escalonado_pronosticos         similitud_texto            texto 0.387 familia 0.143 paso 0.440  paso 4 del candidato contra paso 7
        NUEVO             emparejar_indicadores_efecto_contraefecto        similitud_texto            texto 0.362 familia 0.000 paso 0.419  paso 2 del candidato contra paso 3
    BLOQUEARIA  elegir_indicador_salida_trabajo_administrativo  hoy poblacion 462 | archivo: BLOQUEARIA poblacion 462
        NUEVO             construir_indicador_tendencia_patron             similitud_texto            texto 0.374 familia 0.125 paso 0.403  paso 6 del candidato contra paso 3
        SIGUE             emparejar_indicadores_efecto_contraefecto        similitud_texto            texto 0.394 familia 0.125 paso 0.489  paso 3 del candidato contra paso 4
        SIGUE             evaluar_directivo_resultados_fortaleza           paso_contra_nodo           texto 0.170 familia 0.000 paso 0.766  paso 2 del candidato contra paso 1
    BLOQUEARIA  emparejar_indicadores_efecto_contraefecto  hoy poblacion 462 | archivo: BLOQUEARIA poblacion 462
        SIGUE             construir_grafico_escalonado_pronosticos         similitud_texto            texto 0.384 familia 0.000 paso 0.446  paso 3 del candidato contra paso 1
        SIGUE             construir_indicador_tendencia_patron             similitud_texto            texto 0.397 familia 0.143 paso 0.453  paso 3 del candidato contra paso 5
        NUEVO             dimensionar_plantilla_administrativa_pronostico  similitud_texto            texto 0.355 familia 0.000 paso 0.396  paso 4 del candidato contra paso 2
        NUEVO             elegir_cinco_indicadores_diarios_fabrica         similitud_texto            texto 0.359 familia 0.125 paso 0.445  paso 4 del candidato contra paso 8
        SIGUE             elegir_fabricar_pedido_pronostico                similitud_texto            texto 0.367 familia 0.000 paso 0.408  paso 4 del candidato contra paso 1
        NUEVO             elegir_indicador_salida_trabajo_administrativo   similitud_texto            texto 0.383 familia 0.125 paso 0.468  paso 4 del candidato contra paso 3
        DEJA DE LEVANTAR  revisar_tres_preguntas_valor_carrera             similitud_texto            texto 0.354 familia 0.000 paso 0.386  paso 2 del candidato contra paso 2
    pares que siguen: 15 | dejan de levantar: 1 | nuevos: 9

**Las cifras de esas filas son las de HOY**; la fila `DEJA DE LEVANTAR` lleva las del archivo, porque hoy
no hay. **El `15`, `1` y `9` cuentan filas candidato a vecino**, no pares: un par visto desde los dos
lados cuenta dos veces ahi. **Los pares distintos los cuenta otro instrumento:**

    $ python .v64aud/pares_d005.py
    pares distintos: archivo 12 | hoy 16 | en los dos 11 | solo archivo 1 | solo hoy 5
       SOLO ARCHIVO   emparejar_indicadores_efecto_contraefecto | revisar_tres_preguntas_valor_carrera
       SOLO HOY       construir_indicador_tendencia_patron | dimensionar_plantilla_administrativa_pronostico
       SOLO HOY       construir_indicador_tendencia_patron | elegir_indicador_salida_trabajo_administrativo
       SOLO HOY       construir_indicador_tendencia_patron | equilibrar_capacidad_personal_inventario_plazo
       SOLO HOY       dimensionar_plantilla_administrativa_pronostico | emparejar_indicadores_efecto_contraefecto
       SOLO HOY       elegir_cinco_indicadores_diarios_fabrica | emparejar_indicadores_efecto_contraefecto

**Los seis siguen en `BLOQUEARIA` y la poblacion sigue en `462`.** `archivar...` **no tiene commit de la
`64` y aun asi sus cifras se mueven** (`0.384` en el archivo, `0.361` hoy, contra `construir_indicador_tendencia`):
**LECTURA:** es `d031` desde el otro lado, porque el que cambio es el vecino.

**MI CLASE DE LOS SEIS PARES QUE CAMBIAN** (los once que siguen van en la seccion `6.1`):

| par | estado | mi clase | lo que la sostiene |
|---|---|---|---|
| `emparejar...` con `revisar_tres_preguntas_valor_carrera` | **deja de levantar** | **SANO** (sin cambios) | ya lo leia SANO en `6.1`. **Si hay un veredicto escrito sobre este par, esta escrito sobre un vecino que la senial ya no levanta**, y eso se tiene que decir (encargo `2.c`) |
| `construir_indicador_tendencia_patron` con `dimensionar_plantilla_administrativa_pronostico` | **nuevo** | **CONTINUA, madre `construir_indicador_tendencia...`, hijo `dimensionar_plantilla...`** | **es uno de los pares de `d141` que la seccion `7` lee sin senial**: L125, *de facto standards, inferred from the trend data*. **LECTURA:** la senial lo levanta hoy y no lo levantaba el `23` a primera hora; la arista que leia sin senial ahora tiene tambien senial |
| `construir_indicador_tendencia...` con `elegir_indicador_salida_trabajo_administrativo` | **nuevo** | **SANO** | los dos hablan de salida (*vouchers processed* sale en L37 a L45 y en L89), pero la condicion del indicador de tendencia es *cuando ya tienes nombrada la salida de tu caja*, que es la caja negra de L73 y no la tabla administrativa. Ninguno toma lo que el otro produce |
| `construir_indicador_tendencia...` con `equilibrar_capacidad_personal_inventario_plazo` | **nuevo** | **SANO** | la tendencia de la salida contra los cuatro costes del tostador (`cap_02` L57 a L61): nada en comun |
| `emparejar...` con `dimensionar_plantilla...` | **nuevo** | **SANO** | emparejar indicadores contra ajustar la plantilla a la carga pronosticada |
| `emparejar...` con `elegir_cinco_indicadores_diarios_fabrica` | **nuevo** | **SANO** | ya lo miraba en la seccion `7` sin senial: el quinto dato de `elegir_cinco` pone calidad junto a cantidad (L27), **pero el libro no lo presenta como par de efecto y contraefecto**; eso llega en L31 |

## 6. MI CLASE DE CADA PAR, POR LA VARA `6.1` Y SOLO ESA (`R7`), CON LOS PASOS DE LOS DOS DELANTE

*La senial dijo donde mirar y ahi acabo su trabajo (`D.19`). Los pasos los imprime `.v64aud/pasos.py`,
que busca cada id en el grafo y en las bandejas y dice de donde lo saca. Un par levantado desde los
dos lados va en una sola fila. **Las fichas de la tanda de la `63` las leo en su version de hoy**,
porque la `64` no las toca; **las seis de `d005`, en su version de `067c9df`** (seccion `2`).*

### 6.1. **LOS PARES DE LOS SEIS DE `d005`** (encargo `T2.b`; la lista de pares es la de `.v63aud/vecinos_d005.txt`, poblacion `462`, y el barrido de hoy de la seccion `5` dice si sigue en pie)

| par | mi clase | lo que la sostiene |
|---|---|---|
| `emparejar_indicadores_efecto_contraefecto` con `elegir_indicador_salida_trabajo_administrativo` | **CONTINUA, madre `emparejar...`, hijo `elegir_indicador...`** | L35 abre el tramo del hijo con *Nowhere can indicators, and paired indicators, be of more help than in administrative work*: el libro lleva el emparejamiento de L31 al trabajo administrativo. **El paso `5` del hijo** (*emparejalos con una pareja que insista en la calidad*) **es el paso `4` de la madre** (*empareja el indicador con un segundo que mida ese contraefecto*) **aplicado a indicadores de cantidad**, y los pasos `6` y `7` son sus dos ejemplos (L37). Lo que el hijo trae y la madre no: salida y no actividad, lo fisico y contable, la tabla de L39 a L67. **No REPITE: lo que queda fuera es procedimiento en los dos lados** |
| `construir_grafico_escalonado_pronosticos` con `construir_indicador_tendencia_patron` | **SANO, hermanos** | L91 abre el grafico con *Another sound way to anticipate the future*, y lo compara con *a simple trend chart*: **son dos ventanas distintas**. El grafico trabaja sobre pronosticos sucesivos; el indicador de tendencia, sobre la salida real contra el tiempo y un patron. Ninguno toma lo que el otro produce |
| `construir_grafico...` con `elegir_fabricar_pedido_pronostico` | **SANO** | los dos hablan de pronostico, pero el grafico lee como se mueve un pronostico y `elegir_fabricar` decide si se fabrica contra el. **El puente entre los dos lo pone `casar_flujo...` (L121), no ninguno de ellos** (seccion `7`) |
| `construir_grafico...` con `emparejar...` | **SANO** | vocabulario de indicador; procedimientos sin paso comun |
| `construir_indicador_tendencia_patron` con `archivar_indicadores_resolver_problemas` | **SANO** | el archivo guarda indicadores para cuando algo falla (L99); la tendencia mira la salida contra el tiempo (L89). Ningun paso de uno desarrolla uno del otro |
| `construir_indicador_tendencia_patron` con `emparejar...` | **SANO** | lo mismo |
| `elegir_fabricar...` con `emparejar...` | **SANO** | fabricar contra pronostico contra emparejar indicadores: nada que continuar |
| `archivar...` con `revisar_tres_preguntas_valor_carrera` (grafo) | **SANO** | un archivo de indicadores contra tres preguntas sobre tu carrera. La senial sale del vocabulario (*repasa*, *preguntate*) |
| `archivar...` con `vencer_sindrome_grupo_pares_autoconfianza` (bandeja) | **SANO** | nada en comun |
| `archivar...` con `cerrar_brecha_dos_preguntas_estrategia` (bandeja) | **SANO** | nada en comun |
| `emparejar...` con `revisar_tres_preguntas_valor_carrera` (grafo) | **SANO** | nada en comun |
| `elegir_indicador_salida_trabajo_administrativo` con `evaluar_directivo_resultados_fortaleza` (grafo, `zhuo_manager`) | **SANO, con frontera declarada** | **comparten un paso casi palabra por palabra**: el `2` del candidato y el `1` del vecino son la regla de Grove, *salida y no actividad, al vendedor por los pedidos y no por las visitas* (L35; Zhuo la toma de Grove). **Sin bascula** (`6.1`): lo que queda fuera es procedimiento en los dos lados, la tabla y la pareja de calidad en uno, las dos mitades del juicio y los dos casos que enganan en el otro. **No REPITE y no CONTINUA**: ninguno toma lo que el otro produce; los dos aplican la misma regla a objetos distintos, una unidad administrativa y un directivo |

### 6.2. **LOS PARES DE LOS NUEVE `BLOQUEARIA` DE `d140`** (encargo `T3`; la lista es la de `python .v63aud/vecinos.py`, poblacion `462`)

    $ python .v63aud/vecinos.py 2>&1 | grep -v '^ENTRARIA' | awk '/^ENTRARIA/{skip=1} /^BLOQUEARIA/{skip=0} !skip'
    BLOQUEARIA  clasificar_trabajo_proceso_montaje_prueba  poblacion 462  
        preferir_inspeccion_proceso_prueba_destructiva       similitud_texto              texto 0.372 familia 0.250 paso 0.461  paso 5 del candidato contra paso 6
    BLOQUEARIA  construir_flujo_produccion_paso_limitante  poblacion 462  
        retirar_barreras_politicas_metodo                    paso_contra_nodo             texto 0.108 familia 0.000 paso 0.614  paso 4 del candidato contra paso 1
        rehacer_flujo_paso_limitante_capacidad               similitud_texto, familia_id  texto 0.412 familia 0.429 paso 0.430  paso 9 del candidato contra paso 5
        preferir_inspeccion_proceso_prueba_destructiva       similitud_texto              texto 0.397 familia 0.000 paso 0.421  paso 8 del candidato contra paso 6
    BLOQUEARIA  detectar_arreglar_fallo_etapa_menor_valor  poblacion 462  
        supervisar_tarea_delegada_etapa_menor_valor          familia_id                   texto 0.242 familia 0.333 paso 0.459  paso 2 del candidato contra paso 1
    BLOQUEARIA  dimensionar_inventario_materia_prima_reposicion  poblacion 462  
        preferir_inspeccion_proceso_prueba_destructiva       similitud_texto              texto 0.391 familia 0.000 paso 0.403  paso 2 del candidato contra paso 2
        detectar_arreglar_fallo_etapa_menor_valor            similitud_texto              texto 0.357 familia 0.000 paso 0.401  paso 1 del candidato contra paso 2
    BLOQUEARIA  preferir_inspeccion_proceso_prueba_destructiva  poblacion 462  
        clasificar_trabajo_proceso_montaje_prueba            similitud_texto              texto 0.366 familia 0.250 paso 0.461  paso 6 del candidato contra paso 5
        rehacer_flujo_paso_limitante_capacidad               similitud_texto              texto 0.445 familia 0.000 paso 0.384  paso 1 del candidato contra paso 6
        construir_flujo_produccion_paso_limitante            similitud_texto              texto 0.410 familia 0.000 paso 0.442  paso 6 del candidato contra paso 8
        dimensionar_inventario_materia_prima_reposicion      similitud_texto              texto 0.384 familia 0.000 paso 0.417  paso 5 del candidato contra paso 6
    BLOQUEARIA  rehacer_flujo_paso_limitante_capacidad  poblacion 462  
        preferir_inspeccion_proceso_prueba_destructiva       similitud_texto              texto 0.460 familia 0.000 paso 0.378  paso 3 del candidato contra paso 2
        construir_flujo_produccion_paso_limitante            similitud_texto, familia_id  texto 0.419 familia 0.429 paso 0.430  paso 5 del candidato contra paso 9
        dimensionar_inventario_materia_prima_reposicion      similitud_texto              texto 0.357 familia 0.000 paso 0.387  paso 2 del candidato contra paso 3
    BLOQUEARIA  decidir_aceptar_rechazar_material_defectuoso  poblacion 462  
        dimensionar_plantilla_administrativa_pronostico      similitud_texto              texto 0.372 familia 0.000 paso 0.364  paso 4 del candidato contra paso 2
    BLOQUEARIA  dimensionar_plantilla_administrativa_pronostico  poblacion 462  
        elegir_cinco_indicadores_diarios_fabrica             similitud_texto              texto 0.351 familia 0.000 paso 0.434  paso 6 del candidato contra paso 3
        simplificar_trabajo_reducir_numero_pasos             similitud_texto              texto 0.351 familia 0.000 paso 0.388  paso 6 del candidato contra paso 6
        decidir_aceptar_rechazar_material_defectuoso         similitud_texto              texto 0.367 familia 0.000 paso 0.359  paso 2 del candidato contra paso 3
    BLOQUEARIA  simplificar_trabajo_reducir_numero_pasos  poblacion 462  
        dimensionar_plantilla_administrativa_pronostico      similitud_texto              texto 0.351 familia 0.000 paso 0.439  paso 4 del candidato contra paso 5

**Los pares distintos los cuenta un instrumento**, no mi ojo sobre el bloque: un par levantado desde
los dos lados cuenta una vez.

    $ python .v64aud/pares_d140.py
    candidatos BLOQUEARIA: 9 | pares distintos: 12
        clasificar_trabajo_proceso_montaje_prueba | preferir_inspeccion_proceso_prueba_destructiva
        construir_flujo_produccion_paso_limitante | preferir_inspeccion_proceso_prueba_destructiva
        construir_flujo_produccion_paso_limitante | rehacer_flujo_paso_limitante_capacidad
        construir_flujo_produccion_paso_limitante | retirar_barreras_politicas_metodo
        decidir_aceptar_rechazar_material_defectuoso | dimensionar_plantilla_administrativa_pronostico
        detectar_arreglar_fallo_etapa_menor_valor | dimensionar_inventario_materia_prima_reposicion
        detectar_arreglar_fallo_etapa_menor_valor | supervisar_tarea_delegada_etapa_menor_valor
        dimensionar_inventario_materia_prima_reposicion | preferir_inspeccion_proceso_prueba_destructiva
        dimensionar_inventario_materia_prima_reposicion | rehacer_flujo_paso_limitante_capacidad
        dimensionar_plantilla_administrativa_pronostico | elegir_cinco_indicadores_diarios_fabrica
        dimensionar_plantilla_administrativa_pronostico | simplificar_trabajo_reducir_numero_pasos
        preferir_inspeccion_proceso_prueba_destructiva | rehacer_flujo_paso_limitante_capacidad

**La tabla de abajo lleva una fila por cada uno de esos pares**, en otro orden.

| par | mi clase | lo que la sostiene |
|---|---|---|
| `construir_flujo_produccion_paso_limitante` con `rehacer_flujo_paso_limitante_capacidad` | **CONTINUA, madre `construir_flujo...`, hijo `rehacer_flujo...`** | la condicion del hijo es *cuando ya tienes un flujo construido*; su paso `4` rehace el flujo de la madre alrededor del paso limitante nuevo, **calculando otra vez hacia atras** (madre pasos `5`, `7` y `8`), y su paso `5` cambia solo los desfases (madre paso `9`). Lo que el hijo trae: la capacidad infinita supuesta, la cola, la espera dentro del flujo. L51 a L55 sobre L23 a L27 (`cap_02`) |
| `detectar_arreglar_fallo_etapa_menor_valor` con `supervisar_tarea_delegada_etapa_menor_valor` (bandeja) | **CONTINUA, madre `detectar...`, hijo `supervisar...`** | el paso `2` del hijo es la regla del paso `3` de la madre aplicada a la delegacion, y el hijo trae procedimiento propio (los borradores, la frecuencia por madurez, el detalle al azar). **Coincide con lo que la `ACTA 62` `62.5` sostuvo** y con los veredictos que el encargo manda reutilizar de `.v63ext/cmd_02_detectar.sh` |
| `construir_flujo...` con `retirar_barreras_politicas_metodo` (grafo, `smart_who`) | **SANO** | contratar sin barreras de politica contra construir un flujo. La senial (`paso_contra_nodo` `0.614`) sale de la muletilla *que es por donde el libro dice* contra *que es con quien el libro dice* |
| `construir_flujo...` con `preferir_inspeccion_proceso_prueba_destructiva` | **SANO** | la misma fabrica de desayunos; ningun paso de uno desarrolla uno del otro |
| `rehacer_flujo...` con `preferir_inspeccion...` | **SANO** | lo mismo |
| `clasificar_trabajo_proceso_montaje_prueba` con `preferir_inspeccion...` | **SANO** | las pruebas de `clasificar` (unitaria, del sistema, L45) no son la eleccion entre prueba funcional e inspeccion dentro del proceso de L67 |
| `dimensionar_inventario_materia_prima_reposicion` con `preferir_inspeccion...` | **SANO, hermanos** | los dos cuelgan de la maquina continua (L67 y L69, *What else could go wrong*): uno vigila el proceso, el otro la entrada y el inventario |
| `dimensionar_inventario...` con `detectar_arreglar_fallo...` | **SANO, y lo sigo marcando DISCUTIBLE** | lo comun es un ejemplo, el huevo podrido rechazado al recibirlo (paso `4` de `detectar` contra pasos `1` a `3` de `dimensionar`). Lo que `dimensionar` anade, el inventario por el tiempo de reposicion y la oportunidad en riesgo (L69), **no desarrolla la regla del menor valor**: desarrolla otra cosa. Lo que queda fuera es procedimiento en los dos lados |
| `rehacer_flujo...` con `dimensionar_inventario...` | **SANO** | vocabulario comun (parar, esperar), procedimientos distintos |
| `decidir_aceptar_rechazar_material_defectuoso` con `dimensionar_plantilla_administrativa_pronostico` | **SANO** | material que no llega a especificacion contra plantilla administrativa. La senial sale de *grupo equilibrado de mandos* contra *patrones de hecho* |
| `dimensionar_plantilla...` con `elegir_cinco_indicadores_diarios_fabrica` | **SANO** | los cinco datos del dia de la fabrica contra la plantilla por pronostico |
| `dimensionar_plantilla...` con `simplificar_trabajo_reducir_numero_pasos` | **SANO** | quitar pasos de un flujo contra ajustar la plantilla a la carga |

## 7. LOS PARES QUE LEO Y LA SENIAL NO LEVANTA (`D.29`, encargo `T4`, `d141`)

| madre | hijo | lo que lo sostiene | mi confianza |
|---|---|---|---|
| `elegir_indicador_salida_trabajo_administrativo` (`d005`) | `dimensionar_plantilla_administrativa_pronostico` | L125, *if we have carefully chosen indicators that characterize an administrative unit and watch them closely*: **el paso `1` del hijo presupone el producto de la madre**, y los pasos `3` a `7` siguen donde ella acaba | **alta: la sostengo** |
| `construir_indicador_tendencia_patron` (`d005`) | `dimensionar_plantilla...` | L125, *de facto standards, inferred from the trend data*: **el paso `2` del hijo sale de la serie y el patron que la madre mide** en sus pasos `3` y `4` | **alta: la sostengo**. **Hoy la senial si lo levanta** (seccion `5`, fila `NUEVO`); en la lista de poblacion `462` no |
| `elegir_fabricar_pedido_pronostico` (`d005`) | `casar_flujo_fabricacion_flujo_ventas` | L111, *Delivering a product that was built to forecast*: **la condicion del hijo** (*cuando fabricas contra pronostico*) **es la decision que la madre toma** en su paso `4` | **alta: la sostengo** |
| `construir_grafico_escalonado_pronosticos` (`d005`) | `casar_flujo...` | L121, *It is a good idea to use stagger charts in both the manufacturing and sales forecasts. As noted...*: el paso `12` del hijo usa el grafico de la madre en los dos pronosticos | **baja**: es un paso de doce, y lo que ese paso hace (mirar la variacion de un pronostico a otro) **es el paso `4` de la madre, no procedimiento nuevo**. Nombrar no es procedimentar. **No la sostengo como arista**; la dejo escrita para que conste que la mire |
| `dimensionar_inventario_materia_prima_reposicion` | `decidir_aceptar_rechazar_material_defectuoso` | el paso `1` del hijo (*cuando rechaces material en la inspeccion de recepcion*) abre la decision que la madre cierra con una sola salida en su paso `3` (*devuelve*); L135 anade la segunda (usar lo que no llega) y el grupo que decide | **alta: la sostengo**. No es de `d141`, pero es de la tanda y la senial tampoco lo levanta |
| `emparejar_indicadores_efecto_contraefecto` (`d005`) | `elegir_indicador_salida_trabajo_administrativo` (`d005`) | **este si lo levanta la senial** (seccion `6.1`): lo pongo aqui solo para que el orden lo tenga | **alta** |

**Y DOS QUE LEO COMO NO CONTINUA**, para que conste que las mire: `casar_flujo...` paso `11` nombra la
regla de `detectar_arreglar_fallo...` (L119, *as we've learned before*) y la aplica al inventario en una
sola linea: SANO, nombrar no es procedimentar. Y `elegir_cinco_indicadores_diarios_fabrica` con
`emparejar...`: el paso `8` de `elegir_cinco` (*no te quedes en contar cuantas unidades sirve cada
persona*) es un indicador de calidad junto a uno de cantidad (L27), **pero el libro no lo presenta como
par de efecto y contraefecto**; eso llega despues, en L31. SANO. **Hoy la senial lo levanta** (seccion `5`), y la clase no cambia.

## 8. LO QUE EL ORDEN TIENE QUE RESPETAR, LEIDO (encargo `T4`)

**No fijo el orden** (`D.36`: lo fija quien autoriza). **Lo que si leo son las madres que tienen que ir
delante**, con las aristas de `6` y `7`:

| hijo | madre que tiene que ir delante | capitulo de cada uno |
|---|---|---|
| `rehacer_flujo_paso_limitante_capacidad` | `construir_flujo_produccion_paso_limitante` | `cap_02` y `cap_02` |
| `decidir_aceptar_rechazar_material_defectuoso` | `dimensionar_inventario_materia_prima_reposicion` | `cap_03` y `cap_02` |
| `elegir_indicador_salida_trabajo_administrativo` | `emparejar_indicadores_efecto_contraefecto` | `cap_03` y `cap_03` |
| `dimensionar_plantilla_administrativa_pronostico` | `elegir_indicador_salida_trabajo_administrativo` **y** `construir_indicador_tendencia_patron` | `cap_03`, los tres |
| `casar_flujo_fabricacion_flujo_ventas` | `elegir_fabricar_pedido_pronostico` | `cap_03` y `cap_03` |

**LECTURA:** la cadena mas larga es de tres: `emparejar`, despues `elegir_indicador`, despues
`dimensionar_plantilla`. **Si la tanda de la `65` tiene tope, `dimensionar_plantilla` no puede entrar
sin sus dos madres de `d005` delante.** `supervisar_tarea_delegada...` es hijo de `detectar...` y vive en
`cap_04`: queda fuera de los `22`, pero su veredicto se escribe cuando entre el.

## 9. LO QUE ESTA PAGINA NO HACE, Y LO QUE DEJA PARA EL TURNO NORMAL

- **No compara con el extractor.** Su reporte, sus fichas corregidas de la `64` y su carpeta `.v64ext/`
  quedan sin abrir hasta que el arnes selle esta pagina.
- **No escribe veredictos en `bitacora/` ni aristas en el dataset**: son clases leidas, no insertadas.
- **Lo que queda para el turno normal:** `R5` sobre el reporte de la `64`; la fidelidad de las cinco
  fichas corregidas **contra mi tabla de `067c9df`**, para ver si lo que el extractor reescribio es el
  paso `1` de `emparejar` y que hizo con mis dos dudas; y cada par de `6` y `7` contra sus veredictos
  listos.
- **Mi evidencia se queda en `.v64aud/`**: `antes_<id>.json`, `fidelidad.tsv`, `contar_fidelidad.py` y
  su salida, `pasos.py`, `pares_d140.py`, `vecinos_hoy.py` con su salida, los seis `informe_<id>.txt` y
  `barrido.log`.

## 10. LAS GUARDAS AL CERRAR ESTA PAGINA

    $ python forja.py gate 2>&1 | tail -3
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones docs/loop/APERTURA_CIEGA.md .v64aud/
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

**Gate y guiones en VERDE al cerrar la pagina. Ningun proceso mio queda vivo**: el barrido de la seccion `5` termino a las `11:15:56` con los seis `rc=0`, y lo recogi dentro del turno. **No commiteo**: sella y commitea el arnes.
