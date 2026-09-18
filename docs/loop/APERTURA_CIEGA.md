# APERTURA CIEGA DE LA VUELTA 36, linea `serial`, libro `scott_radical_candor`

Escrita ANTES de ver `docs/loop/REPORTE.md`, que el arnes retira a proposito (`D.34.2`).
Es la lectura que despues se compara con la del extractor. Mi acta de esta vuelta sera la
**`ACTA 35`**.

**MODO AUSTERO (`D.47`) VIGENTE:** lo que el registro ya dice no se repite. Lo que queda
intacto es **la cifra con su instrumento al lado**, y por eso toda cifra de aqui abajo
lleva su salida literal pegada.

---

## 1. LA LINEA DE LECTURA QUE `D.40` EXIGE

    ACTA ANTERIOR LEIDA: 4ec70432816947ebfad797050359b47e537ca7d9
    HEREDADOS: NINGUNO. Heredo CERO, y no es un silencio mio: lo dice el instrumento
               del arnes y ademas lo compruebo yo sobre el texto del acta.

**Y NO ME CREO LA HUELLA DEL PROMPT: LA MIDO CONTRA EL FICHERO QUE TENGO DELANTE.**

    $ git hash-object docs/loop/ACTA_AUDITOR.md
    4ec70432816947ebfad797050359b47e537ca7d9
    $ git cat-file -t 4ec70432816947ebfad797050359b47e537ca7d9
    blob
    $ git cat-file -s 4ec70432816947ebfad797050359b47e537ca7d9
    1898316
    $ git cat-file -p 4ec70432816947ebfad797050359b47e537ca7d9 | tail -1 | cut -c1-120
    **ACTA ANTERIOR LEIDA: d2fa59ef5128507f86f8b1ce095665e9750176bf**

**La huella que el prompt me entrega es la del fichero que yo he leido, al digito.** No es
un commit: es el blob del propio `ACTA_AUDITOR.md`. Y su ultima linea es la declaracion de
lectura de mi predecesor, que es la prueba de que he abierto el acta hasta el final y no un
tramo.

    $ python forja.py herencia | sed -n '5,7p' | cut -c1-92
      acta anterior : ACTA 34. VUELTA 35, lote 4 (`scott_radical_candor`), **`cap_09` cerrado en
      su huella     : 4ec70432816947ebfad797050359b47e537ca7d9
      heredados     : 0

**Y EL CERO LO COMPRUEBO YO CONTRA EL TEXTO, porque un cero entregado tambien se verifica:**

    $ sed -n '29598,29985p' docs/loop/ACTA_AUDITOR.md | grep -n "REMEDIO\|TAREA BLOQUEANTE"
    251:**EL REMEDIO QUE ME ENCARGUE A MI MISMO EN LA `ACTA 33` LO CUMPLI** (la apertura declara

**La unica linea de la `ACTA 34` que dice `REMEDIO` dice que el remedio anterior QUEDO
CUMPLIDO.** No hay ninguna `TAREA BLOQUEANTE DEL AUDITOR` y no hay ningun remedio nuevo
escrito. **El `0` es verdad, y no por ausencia de fichero.**

> **`LECTURA`, marcada aparte** (`D.38.3` ensanchada): el `0` podria ser falso por una via
> que esta misma fase abre, y la cierro antes de pasar. `docs/loop/CREDITO_serial.jsonl`
> **no esta en el arbol ahora mismo**, y si el arnes discriminase por *esta linea no tiene
> fichero* entregaria cero por una ausencia que no significa nada, que es el defecto que
> `D.40` vino a cerrar. **No lo hace**, y la casa tiene la prueba escrita contra si misma:
>
>     $ python forja.py credito --lineas
>     NINGUNA LINEA TIENE REGISTRO DE CREDITO todavia (D.48).
>     $ grep -n "EL DISCRIMINADOR NO ES" tests/test_aceptacion.py
>     4453:        """EL DISCRIMINADOR NO ES 'ESTA LINEA NO TIENE FICHERO', y el banco del arnes
>
> La prueba `test_en_un_arbol_donde_el_credito_NO_SE_USA_la_herencia_sigue_entera` existe y
> **no esta entre los rojos de la seccion 5.1**. Aun asi, **el `0` que declaro lo sostiene
> el TEXTO del acta, no la salida del arnes**, que es lo unico que no depende de eso.

---

## 2. QUE VUELTA ABRO. **LA UNICA AMBIGUEDAD QUE ENCUENTRO, DECLARADA EN VEZ DE RESUELTA CALLANDO**

    $ git log --format="%h %ci %s" -5 | cut -c1-112
    4b74e6e 2026-09-17 20:36:25 -0400 V.36 CIERRE: cap_10 entero en el grafo con 14 de 14
    cf3a2d2 2026-09-17 19:49:38 -0400 V.36 cap_10: siete de los catorce dentro, con sus d
    a8547da 2026-09-17 18:22:07 -0400 V.36 cap_10, los tres primeros de 14 insertados, y
    6a978a5 2026-09-17 17:06:40 -0400 V.36 TAREA 2: la fidelidad de cap_10 corrida ANTES
    8cb6a99 2026-09-17 16:51:07 -0400 Apertura ciega de la vuelta 36, sellada antes de ab
    $ git show --stat 8cb6a99 | tail -3
     docs/loop/loop.log              | 18 ++++++++++++++++++
     docs/loop/ultimo_extractor.json |  1 -
     2 files changed, 18 insertions(+), 1 deletion(-)
    $ git log --format="%h %s" -1 -- docs/loop/APERTURA_CIEGA.md
    0ff87d0 Apertura ciega de la vuelta 2, sellada antes de exponer el reporte
    $ git show HEAD:docs/loop/APERTURA_CIEGA.md | head -1
    # APERTURA CIEGA DE LA VUELTA 35, linea `serial`, libro `scott_radical_candor`

**HAY UN COMMIT TITULADO `Apertura ciega de la vuelta 36` QUE NO TRAE NINGUNA APERTURA
CIEGA.** Toco `loop.log` y retiro `ultimo_extractor.json`, que es la retirada de `D.34.2`, y
**no toco `docs/loop/APERTURA_CIEGA.md`**: el fichero que hay en `HEAD` sigue siendo el de la
**vuelta 35**, el que sostuvo la `ACTA 34`.

| pieza | lo que dice el arbol |
|---|---|
| ultima apertura ciega commiteada | la de la **vuelta 35** |
| ultima acta escrita | la **`ACTA 34`**, que cubre la **vuelta 35** |
| trabajo del extractor CERRADO y todavia sin acta | la **vuelta 36**, `cap_10` |
| lo que el arnes retira hoy para que yo escriba | `APERTURA_CIEGA.md` mas los cuatro de `D.34.2` |

**ASI QUE ABRO LA VUELTA 36 Y MI ACTA SERA LA `ACTA 35`.** La apertura de las `16:51` no
existe como documento, y **lo que no existe no se puede comparar con nada**.

**Y NO ME JUEGO LA VUELTA A ESA LECTURA.** Por si el arnes estuviera abriendo la **37** en
vez de la 36, esta apertura clasifica **las dos poblaciones**: el material que la vuelta 36
metio en el grafo (secciones 6 a 10) **y** la frontera de lo que espera en bandeja, que es
lo que la vuelta siguiente tomara (seccion 11). **Una de las dos sobra; ninguna falta.**

> **NO ENCARGO NINGUN ARREGLO DE ESTO.** Es maquinaria del arnes (`D.33`), `7.F` de la
> cosecha me prohibe encargar arneses nuevos sin caida de dato, y `D.45` me prohibe tocarla
> mientras corran frentes en paralelo. **Sube como propuesta, no como caida de nadie.**

---

## 3. HUECO DE ACTA (`AUDITOR_FORJA.md` 1.0): **NO LO HAY**

    $ grep -c "^# ACTA " docs/loop/ACTA_AUDITOR.md
    34
    $ grep "^# ACTA " docs/loop/ACTA_AUDITOR.md | tail -1 | cut -c1-38
    # ACTA 34. VUELTA 35, lote 4 (`scott_r

**La `ACTA 34` cubre la `VUELTA 35` y yo audito la `36`: la vuelta inmediatamente anterior
esta cubierta y audito una sola vuelta.**

---

## 4. EL TABLERO (`D.49`), LEIDO Y CITADO

    $ python forja.py tablero --puedo scott_radical_candor
    LINEA 'serial', LIBRO 'scott_radical_candor': SI
      'scott_radical_candor' ya es de esta linea ('serial'): continuarlo es lo que toca.
    $ python forja.py tablero | grep -E "scott_radical_candor|COLA DE DOCTRINA|MUNDO 11"
      .    4    scott_radical_candor           CERRADO EN EXTRACCION  serial                  29  cap_14
        scott_radical_candor           lo trabaja 'serial' (CERRADO EN EXTRACCION)
      MUNDO 11: faltan 3 de 3 libros del corte (grove_high_output, gerber_emyth, marquet_turn_the_ship)
      COLA DE DOCTRINA (D.53): 6 pregunta(s), 0 bloquea(n)

**El lote 4 sigue con dueno `serial` y con `29` en bandeja: NO cierra con esta vuelta**, asi
que `D.32` no pide medir apertura de lote y `D.50` no releva a mitad. **La cola de doctrina
sigue en `6` y ninguna bloquea.**

---

## 5. LAS GUARDAS, CORRIDAS POR MI EN ESTA MISMA FASE

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 316
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada,
               vuelta, cita_incompleta, deprecado_en_superficie, arista_rota,
               arista_incompleta, guiones, censo_no_decrece
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python forja.py resolutor
    nodos vivos: 316
    nodos deprecados (archivo): 0
    alias registrados: 0
    $ python forja.py rancios | head -3
    BLOQUE DE VIGENCIA: 50 hallazgo(s) sobre 450 veredicto(s) y 0 cita(s).
      RANCIO 42, SIN HUELLA 8
      lineas declaradas NO CONSUMADAS y por eso no medidas: 14
    $ python forja.py credito --revisar
    REPLAY VERDE en la linea 'serial': las 0 tanda(s) vigilables suman lo que declaran.

> **`LECTURA` sobre el replay:** `0` tandas vigilables **no es una tanda limpia**: es el
> registro retirado por esta fase. **El verde de ahi arriba no dice nada sobre la vuelta 36**
> y no lo voy a citar como si lo dijera.

### 5.1. LA SUITE, Y LOS CUATRO ROJOS QUE **NO SE DE QUIEN SON TODAVIA**

    $ python tests/test_aceptacion.py | tail -1
      total: 294 pruebas, 3 fallos, 1 errores
    $ python tests/test_aceptacion.py > $TEMP/t.out 2>&1     (fuera del repo, no escribe en el arbol)
    $ grep -c "" $TEMP/t.out
    570
    $ grep -E "^(FAIL|ERROR): " $TEMP/t.out | cut -c1-84
    ERROR: test_el_reporte_vivo_pasa_su_propia_guarda (__main__.PruebaTablaDeCierre.test
    FAIL: test_caso_positivo_un_frente_recien_nacido_hereda_cero (__main__.PruebaHerenci
    FAIL: test_el_aviso_nombra_la_linea_y_su_registro (__main__.PruebaHerenciaPorLinea.t
    FAIL: test_la_linea_serial_del_repo_tiene_su_registro_escrito (__main__.PruebaHerenc
    $ grep -E "FileNotFoundError|CREDITO_serial" $TEMP/t.out | cut -c1-100
    FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\AlexDesk\\Documents\\forja-nodos
    AssertionError: False is not true : docs/loop/CREDITO_serial.jsonl sin tandas: la migracion de D.48

> **`LECTURA`, marcada aparte:** **los cuatro nombran un fichero que esta fase retira**, y
> ninguno nombra `dataset/`, `bitacora/`, `config/` ni `src/`. El error cuelga de
> `docs/loop/REPORTE.md` (`D.34.2`) y los tres fallos de `docs/loop/CREDITO_serial.jsonl`.
> **LO QUE NO PUEDO HACER AQUI Y LO DIGO EN VEZ DE DEDUCIRLO:** no puedo recuperar ninguno
> de los dos para comprobarlo, porque recuperarlos invalida mi propia apertura. **Queda
> como `POR ADJUDICAR 1`: se re corre con el arbol entero en mi turno normal, y solo
> entonces se dice si es `0` de `294` o si hay un rojo de verdad debajo.**

---

## 6. EL DATO, CONTADO POR MI Y CON DOS INSTRUMENTOS POR FICHERO

| fichero | `wc -l` | `grep -c ""` | lector de python |
|---|---:|---:|---:|
| `dataset/nodos.jsonl` | **`316`** | **`316`** | **`316`** |
| `bitacora/VEREDICTOS.jsonl` | **`464`** | **`464`** | **`464`** |
| `fuentes/scott_radical_candor/cap_10.md` | **`263`** | **`263`** | **`263`** |
| `docs/loop/ACTA_AUDITOR.md` | **`29985`** | **`29985`** | **`29985`** |

    $ python -c "d=open('fuentes/scott_radical_candor/cap_10.md','rb').read(); print(len(d), repr(d[-1:]))"
    53148 b'\n'

**El ultimo byte de `cap_10.md` es un salto de linea**, asi que los tres instrumentos miden
la misma cosa y no cabe la trampa de la linea final sin cerrar. Es el remedio que mi
predecesor escribio despues de publicar `434` donde habia `433`, **y lo aplico aunque no lo
herede**.

| pieza | cierre de la `ACTA 34` | **hoy, medido por mi** | delta |
|---|---:|---:|---:|
| nodos | `302` | **`316`** | **`+14`** |
| veredictos | `427` | **`464`** | **`+37`** |
| aristas por `nodos_siguientes` | `109` | **`117`** | **`+8`** |
| aristas por `nodos_previos` | `109` | **`117`** | **`+8`** |
| bandeja lote 4 | `43` | **`29`** | **`-14`** |
| archivados lote 4 | `99` | **`113`** | **`+14`** |

    $ (mi lector: los pares de arista por los dos extremos)
    aristas por nodos_siguientes: 117
    aristas por nodos_previos  : 117
    pares que no casan por los dos extremos: []

**CERO NODOS DESAPARECIDOS Y LAS ARISTAS CASAN POR LOS DOS EXTREMOS.** Y el lote 4 sigue
sumando `142`: `113` mas `29`, igual que los `99` mas `43` del cierre anterior.

---

## 7. EL MATERIAL DE LA VUELTA: `cap_10`

    $ (mi lector: nodos scott del grafo por capitulo, buscando la ruta fuentes/.../cap_NN.md
       en el resumen_teorico, y si no aparece, la mencion en prosa)
    cap_01 1   cap_03 1   cap_04 5   cap_04 (por mencion en prosa) 1   cap_05 8
    cap_06 10  cap_07 25  cap_08 12  cap_09 20  cap_10 14  cap_11 16
    total scott: 113   sin ninguna mencion de capitulo: []

> **`LECTURA`, marcada aparte, y es una que me cace a mi mismo antes de publicarla:** mi
> primer patron buscaba solo la ruta `fuentes/scott_radical_candor/cap_NN.md` y me dio **un
> nodo `SIN_CAP`**. **Ese nodo SI dice de que capitulo sale**: `invitar_desafio_reciproco_equipo`
> escribe en su prosa *el segundo de los seis candidatos de cap_04*. **Lo que mi patron media
> era la CONVENCION de escribir la ruta, no el dato**, y publicar *un nodo no dice de que
> capitulo sale* habria sido exactamente la caida de la vuelta 26 que `D.38.3` trae escrita
> en el protocolo. **La convencion de la ruta la llevan `112` de `316` nodos del grafo**
> (`112` de `113` en scott, y ninguno de los libros anteriores), **y eso es lo unico que mi
> primer patron media.**
    $ (mi lector: cap_10)
    nodos cap_10: 14   pasos cap_10: 206
    $ (mi lector: la bandeja por capitulo)
    cap_12 2   cap_13 12   cap_14 15   total 29   pasos 436
    $ head -5 fuentes/scott_radical_candor/cap_10.md | tail -2
    unidad: Cap. 7
    titulo_textual: Team

**`cap_10` esta ENTERO en el grafo: `14` nodos, `206` pasos, `0` en bandeja.** Y la cuenta
cierra por los dos lados:

    $ (mi lector: archivados scott contra nodos scott del grafo)
      archivados: 113   en grafo: 113
      archivados que NO estan en el grafo: []
      en grafo que NO estan archivados: []
      duplicados bandeja/grafo: 0

**CERO DUPLICADOS ENTRE BANDEJA Y GRAFO HOY.** Lo mido y lo digo porque el asunto de un
commit de esta vuelta declara que ese duplicado existio y que el extractor se lo cazo a si
mismo. **Lo que yo firmo es lo de hoy: no queda ninguno.**

### 7.1. LO QUE LA ADUANA LE HIZO A CADA CANDIDATO AL ENTRAR, CAMPO A CAMPO

Comparo el fichero archivado en `cuarentena/_insertados/` (el candidato ANTES) contra el
nodo de `dataset/` (el nodo DESPUES), campo a campo, en los `14`:

| campos que difieren | cuantos nodos |
|---|---:|
| **NINGUNO** | **`5`** |
| solo `nodos_previos` | **`6`** |
| solo `nodos_siguientes` | **`1`** |
| `nodos_previos` y `nodos_siguientes` | **`2`** |

**NINGUNA INSERCION TECLEO UN CAMPO POR EL CAMINO.** Lo unico que la puerta escribio son las
aristas, que es exactamente lo que `D.29` manda que escriba. Ni un `paso`, ni un
`resumen_teorico`, ni un `entregable_esperado`, ni una `condicion_activacion` movida.

---

## 8. LA RELECTURA DE FIDELIDAD `D.30`: **LOS `206` PASOS, UNO A UNO, CONTRA SU LINEA**

**LOS `206` LOS HE LEIDO ENTEROS**, con `cap_10.md` delante. Mi clase ciega: **`206`
TRANSCRIPCION, `0` PUENTE**. Y digo por que camino lo firmo, porque **una afirmacion de
ausencia sin metodo no vale nada**.

### 8.1. EL BARRIDO DE LAS TRES ESPECIES QUE `D.30` NOMBRA. **LAS TRES SALEN LIMPIAS**

**PRIMERA ESPECIE, EL PERIODO.** Barro con mi patron todos los pasos que llevan una cantidad
o un plazo y compruebo cada uno contra su linea:

    $ (mi barrido de cantidades y periodos sobre los 206 pasos de cap_10)
    pasos con expresion de cantidad o periodo: 19

| paso | lo que dice | la linea que lo sostiene |
|---|---|---|
| `desplegar_tres_conversaciones` P6 | `1:1` | `L21` *usual 1:1 slots* |
| `desplegar_tres_conversaciones` P9 | tres de 45 min, en 3 a 6 semanas | `L43` *three forty-five-minute conversations ... three to six weeks* |
| `conversar_historia_vida` P4 | dos anios | `L49` *after two years* |
| `conversar_historia_vida` P15 | 45 minutos | `L59` *in forty-five minutes* |
| `conversar_suenios` P2 | cinco anios | `L63` *five-year plans* |
| `conversar_suenios` P9 | 3 a 5 columnas | `L71` *three to five columns* |
| `trazar_plan_dieciocho_meses` P6 | 6 a 18 meses | `L79` *next six to eighteen months* |
| `armar_plan_anual` P2 | una vez al anio | `L99` *Once a year* |
| `armar_plan_anual` P9 | 20 minutos maximo | `L103` *spend twenty minutes, maximum* |
| `armar_plan_anual` P12 | 3 a 5 puntos | `L109` *three- to five-bullet-point* |
| `armar_plan_anual` P20 | 5 a 15 minutos | `L113` *five to fifteen minutes per direct report* |
| `montar_proceso_contratacion` P7 | 3 o 4 palabras | `L137` *three to four words* |
| `montar_proceso_contratacion` P18 | 3 y 3, ocho personas | `L145` *Bob, Charlene, and Dory ... a waste of eight people's time* |
| `montar_proceso_contratacion` P19 | 4 personas | `L147` *Four people is about the right size* |
| `montar_proceso_contratacion` P26 | una hora, 45 y 15 | `L157` *schedule an hour, interview for forty-five minutes, and write for fifteen* |
| `montar_proceso_contratacion` P31 | una hora, 15 de sala de estudio | `L163` *one-hour meeting with a fifteen-minute study hall* |
| `calibrar_decision_despido` P10 | otros 3 o 6 meses | `L185` *another three or six months* |
| `calibrar_ascensos` P3 | un dia, dos veces al anio | `L209` *off-site for one day twice a year* |
| `evitar_obsesion_ascenso` P1 | diez anios despues | `L231` *Ten years later* |

**`19` DE `19`, Y LAS `19` ESTAN EN EL LIBRO.** Ni un plazo puesto por la mano que escribe.

**SEGUNDA Y TERCERA ESPECIE, EL RESPONSABLE Y EL DESTINATARIO:**

    $ (mi barrido de roles y destinatarios sobre los 206 pasos de cap_10)
    pasos totales: 206   pasos que nombran responsable o destinatario: 28

Los `28` los compruebo uno a uno y **los `28` salen del libro**. Los cinco que mas invitaban
a inventar: `armar_plan_anual` P10 (*tu jefe, un igual o alguien de recursos humanos*) es
`L105` *your boss, a peer, an HR person*; `montar_proceso_contratacion` P6 (*y no alguien de
seleccion de personal*) es `L137` *The hiring person, not a recruiter*;
`montar_proceso_contratacion` P23 (*recepcion y quien organiza las agendas*) es `L151` *the
receptionist and schedulers*; `calibrar_ascensos` P8 (*socio de recursos humanos*) es `L215`
*an HR partner*; y `reconocer_excelencia` P1 (*Jim Ottaway, antiguo vicepresidente y
consejero de Dow Jones*) es `L241` *former SVP and Board Director of Dow Jones*.

**CUENTO TAMBIEN DONDE SALE LIMPIO, que es lo que la metrica pide:** `19` mas `28` son `47`
pasos con una de las tres especies encima, **y los `47` tienen su linea**. Los `159`
restantes son procedimiento sin cifra ni rol, leidos igual contra su tramo.

### 8.2. LA FILA DE `PASOS INVENTADOS POR CAPITULO` QUE VOY A FIRMAR (`AUDITOR_FORJA.md` 8)

| capitulo | pasos escritos | PUENTE | por ciento | de donde sale el denominador |
|---|---:|---:|---:|---|
| **`cap_10` entero** | **`206`** | **`0`** | **`0,00`** | mi lector sobre `dataset/`, no la tabla de nadie |

**`0,00` esta muy por debajo del tope de `10` de `8.1`: por esta metrica el volumen no baja
ningun escalon.** Y `8.4` sigue entero: un `0` aqui no es merito ni demerito de credito.

### 8.3. LO QUE RELEI DE LOS `TRANSCRIPCION`, DONDE ESTA LA TENTACION (`AUDITOR_FORJA.md` 8.3, punto 2)

Cuatro sitios de `cap_10` donde inventar salia barato, y **no se invento**:

1. **`L173` dice `three things` y NO las enumera ahi.** Las tres son los tres rotulos que
   vienen detras: `L175` *Don't wait too long*, `L181` *Don't make the decision
   unilaterally*, `L189` *Give a damn*. El `P11` de `facilitar_despido_tres_cosas` las nombra
   asi, **y las tres aristas del grafo salen a esos tres nodos y a ninguno mas**.
2. **`L197` *Follow up* es el CUARTO rotulo de la misma seccion y se queda FUERA de las
   tres.** `contactar_despedido_mes_despues` entra con `nodos_previos` vacio, que es la forma
   de decirlo sin escribirlo. **Es mi `DISCUTIBLE 2`, y lo sostengo** (seccion 10.2).
3. **La cita de Thoreau de `L85` no se convierte en paso**, y su frase *resultados
   inesperados en las horas comunes* viaja dentro del `P13` de `trazar_plan`, que es donde
   el propio libro la coloca.
4. **El caso de Russ Laraway (`L23` a `L45`) no se extrae como nodo.** Manual 3.5: el caso no
   es la casa. **Google, la encuesta interna de satisfaccion, Todd y Sarah no aparecen en
   ningun paso de los `206`**; Russ si, nombrado, como ejemplo dentro de la doctrina.

### 8.4. LA COBERTURA DE LA FRONTERA, MEDIDA Y NO SUPUESTA

    $ (mi lector de rotulos cortos de cap_10.md)
    rotulos cortos detectados: 29

| seccion en mayusculas de `cap_10` | linea | nodo que la recoge |
|---|---:|---|
| `CAREER CONVERSATIONS` | `L15` | `desplegar_tres_conversaciones_carrera` mas sus tres hijas |
| `GROWTH MANAGEMENT` | `L93` | `armar_plan_anual_crecimiento_equipo` |
| `HIRING: YOUR MENTALITY AND YOUR PROCESS` | `L127` | `montar_proceso_contratacion_reducir_sesgo` |
| `FIRING` | `L165` | `facilitar_despido_tres_cosas`, sus tres hijas y `contactar_despedido_mes_despues` |
| `PROMOTIONS` | `L203` | `calibrar_ascensos_evitar_politica` |
| `REWARD YOUR ROCK STARS` | `L225` | `evitar_obsesion_ascenso_estatus` y `reconocer_excelencia_trayectoria_gradual` |
| **`AVOID ABSENTEE MANAGEMENT AND MICROMANAGEMENT`** | **`L253`** | **NINGUNO, ni en el grafo ni en la bandeja** |
| `SUMMARY` | `L257` | ninguno, y es lo correcto: es un recuento |

> **`LECTURA`, marcada aparte:** **`L253` es la unica seccion nombrada de `cap_10` que no
> tiene nodo.** La leo entera antes de opinar: `L255` dice *I've developed a simple chart* y
> **el cuadro no esta en el texto**; lo que queda es *One of the best ways to keep the people
> on your team engaged is by partnering actively with them*, que es una postura y no un
> procedimiento (`D.27`). **Mi lectura ciega es que esta bien dejada fuera**, y la dejo
> escrita como `POR ADJUDICAR 2` para que el reporte diga si la vio o si se le paso.

**LA TABLA DE ARRIBA NO LA CUENTO A OJO: LA SACO DE UN SEGUNDO INSTRUMENTO**, que busca las
lineas enteramente en mayusculas y devuelve exactamente las ocho filas de la tabla:

    $ (mi lector de secciones en mayusculas de cap_10.md, sin la cabecera ni el titulo
       del capitulo siguiente)
    L15   CAREER CONVERSATIONS
    L93   GROWTH MANAGEMENT
    L127  HIRING: YOUR MENTALITY AND YOUR PROCESS
    L165  FIRING
    L203  PROMOTIONS
    L225  REWARD YOUR ROCK STARS
    L253  AVOID ABSENTEE MANAGEMENT AND MICROMANAGEMENT
    L257  SUMMARY
    secciones en mayusculas de cap_10: 8

**Y DIGO LO QUE MI PRIMER PATRON NO VE, porque una cifra de rotulos es la cifra de MI patron
y no la del libro:** el de `29` rotulos cortos **no detecta** `L17` ni `L95`, que son
subtitulos de mas de doce palabras, ni `L247` de `cap_13`, que acaba en punto. **Ninguno de
los tres es una seccion en mayusculas, asi que no mueven el `8`**, pero el que lea la cifra
de `29` tiene que saber que mide.

---

## 9. EL BARRIDO DE VECINOS `D.38.4`, SOBRE **GRAFO MAS BANDEJAS**

    $ (aduana.poblacion_de_bandejas, que es la regla de la propia casa)
    POBLACION D.38.4: 348  (316 del grafo mas 32 que esperan en bandejas)
    bandejas por lote: marquet_turn_the_ship 3, scott_radical_candor 29

**`348`, con sus dos mitades publicadas**, que es lo que la clase `Poblacion` de
`src/aduana.py` exige que se publique. `cuarentena/ensayo_referencia_163/` **queda fuera, y
digo por que**: la regla de la casa no es una lista de nombres, es que **entra el candidato
cuyas fuentes estan TODAS en la tabla canonica vigente**, y las de ese ensayo no lo estan.
Lo comprobe corriendo `aduana.poblacion_de_bandejas()`, no contando carpetas a mano.

### 9.1. EL INSTRUMENTO, Y POR QUE NO ES EL DE LA CASA TAL CUAL

Corro **las mismas tres seniales de `src/aduana.py` con los mismos umbrales de
`config/umbrales.json`** (`0,35` similitud de texto, `0,30` familia de id, `0,60` paso contra
nodo), con una sola diferencia, **que es de velocidad y no de resultado**: antes de calcular
`difflib.ratio()` calculo **su cota superior** (la de longitud y la de multiconjunto de
caracteres, que son las que `difflib` publica como `real_quick_ratio` y `quick_ratio`). **Si
la cota no llega al umbral, `ratio()` tampoco puede llegar.** Los pares que si levantan se
calculan exactos con el mismo `ratio()`.

**Y NO PIDO QUE SE ME CREA: LO CONTRASTO CONTRA LA BITACORA**, que midio con el instrumento
de la casa sin recorte ninguno. **Mis valores y los suyos coinciden al tercer decimal en las
CATORCE vecindades**, y estos son los de las seniales que levantaron: `0,911`, `0,741`, `0,647`,
`0,641`, `0,608`, `0,500`, `0,374`, `0,371`, `0,367`, `0,365`, `0,362`, `0,356` y `0,333` dos
veces. **Si mi recorte estuviera perdiendo pares, la primera que fallaria seria una de estas.**

### 9.2. LAS `14` VECINDADES DE LAS TRES SENIALES, Y **LAS `14` TIENEN SU VEREDICTO**

    $ (mi barrido, las TRES seniales, los 14 contra los 348)
    admitir_pronto_mal_desempenio_cuatro_razones -> 2   [176s]
       [grafo]   sopesar_consejo_legal_despedir_humildad     similitud_texto 0.374
       [grafo]   trazar_plan_dieciocho_meses_aprendizaje     similitud_texto 0.356
    armar_plan_anual_crecimiento_equipo -> 2   [390s]
       [bandeja] desplegar_plan_orden_operaciones_franqueza_radical  paso_contra_nodo 0.741
       [grafo]   disenar_equipo_plan_anual                   familia_id      0.500
    calibrar_ascensos_evitar_politica -> 2   [270s]
       [grafo]   bloquear_tiempo_pensar_calendario           paso_contra_nodo 0.911
       [grafo]   evitar_obsesion_ascenso_estatus             familia_id      0.333
    calibrar_decision_despido_documentarla -> 1   [154s]
       [grafo]   sopesar_consejo_legal_despedir_humildad     similitud_texto 0.362
    contactar_despedido_mes_despues -> 0   [84s]
    conversar_historia_vida_descubrir_motivadores -> 1   [253s]
       [grafo]   desplegar_tres_conversaciones_carrera       paso_contra_nodo 0.641
    conversar_suenios_cruzar_habilidades -> 0   [291s]
    desplegar_tres_conversaciones_carrera -> 2   [261s]
       [grafo]   conversar_historia_vida_descubrir_motivadores        paso_contra_nodo 0.647
       [bandeja] desplegar_plan_orden_operaciones_franqueza_radical   paso_contra_nodo 0.608
    evitar_obsesion_ascenso_estatus -> 1   [160s]
       [grafo]   calibrar_ascensos_evitar_politica           familia_id      0.333
    facilitar_despido_tres_cosas -> 0   [149s]
    montar_proceso_contratacion_reducir_sesgo -> 0   [362s]
    reconocer_excelencia_trayectoria_gradual -> 0   [178s]
    sopesar_consejo_legal_despedir_humildad -> 2   [113s]
       [grafo]   admitir_pronto_mal_desempenio_cuatro_razones         similitud_texto 0.365
       [grafo]   calibrar_decision_despido_documentarla               similitud_texto 0.367
    trazar_plan_dieciocho_meses_aprendizaje -> 1   [137s]
       [grafo]   calibrar_decision_despido_documentarla      similitud_texto 0.371
    ======================================================================
    TOTAL vecindades levantadas sobre los 14 nodos de cap_10: 14

**`14` VECINDADES, Y LAS `14` TIENEN SU VEREDICTO ESCRITO.** El cruce lo hago **por los dos
lados y con un instrumento, no contando a mano**, que es lo unico que lo prueba:

    $ (mi cruce: cada vecindad mia buscada en la bitacora, y al reves)
    vecindades mias: 14
    lineas encontradas, ordenadas: [428, 429, 430, 431, 434, 438, 439, 444, 445, 448,
                                    452, 453, 457, 458, 460]
    veredictos de la bitacora levantados por senial: [428, 429, 430, 431, 434, 438, 439,
                                    444, 445, 448, 452, 453, 457, 458, 460]
    sobran en la bitacora: []
    faltan en la bitacora: []

**`14` vecindades dan `15` lineas porque una de ellas cae en el par `430` y `431` a la vez**,
que es el duplicado ya declarado (seccion 10.4). **NI UNA VECINDAD DE SENIAL SE QUEDO SIN
LEVANTAR, Y NI UN VEREDICTO DE SENIAL SOBRA.** Y
`2` de las `14` tienen el otro extremo **en la bandeja**, que es justo lo que `D.38.4` existe
para que no se pierda y lo que `D.38.5` cableo en la aduana el 12 sep.

> ### **`LECTURA`, marcada aparte, y es el hallazgo del barrido: LA SENIAL 1 NO ES SIMETRICA**
>
> El par `trazar_plan_dieciocho_meses_aprendizaje` contra
> `calibrar_decision_despido_documentarla` **levanta por un extremo y no por el otro**, y el
> umbral le queda justo en medio. Lo mido a proposito en los dos sentidos:
>
>     $ (mi lector: senal_similitud_texto en los dos sentidos, misma definicion de la casa)
>     trazar_plan_dieciocho_meses_aprendizaje -> calibrar_decision_despido_documentarla  0.371
>     calibrar_decision_despido_documentarla  -> trazar_plan_dieciocho_meses_aprendizaje  0.349
>        largos: 3644 y 3848 caracteres
>     admitir_pronto_mal_desempenio_cuatro_razones -> sopesar_consejo_legal_despedir_humildad  0.374
>     sopesar_consejo_legal_despedir_humildad      -> admitir_pronto_mal_desempenio_cuatro_razones  0.365
>        largos: 3853 y 3337 caracteres
>
> **`0,371` esta por encima del umbral de `0,35` y `0,349` esta por debajo, y son el MISMO
> par.** La causa es del instrumento y no del dato: `difflib.SequenceMatcher(None, a, b).ratio()`
> **no garantiza el mismo valor al cambiar `a` por `b`**, y `senal_similitud_texto` lo llama
> con el candidato siempre en primer lugar.
>
> **QUE SIGNIFICA Y QUE NO.** Significa que **cual de los dos nodos pase por la puerta puede
> decidir si un par se levanta o no**. **NO significa que aqui se haya perdido nada:** la
> vuelta 36 escribio ese veredicto (linea `434`), por el extremo que si levanta, y mi barrido
> de hoy lo confirma. **Lo dejo medido, con sus cuatro cifras, y no lo cargo a nadie: no es
> una cifra falsa ni un veredicto mal puesto, es una propiedad del instrumento que hasta hoy
> no estaba escrita.** Sube a la cola de doctrina en mi acta (`D.53`), **no la resuelvo yo**
> (`D.45`, y `7.F` de la cosecha me prohibe encargar maquinaria).

### 9.3. LA SENIAL MAS ALTA DE LA TANDA **NO MIDE NINGUN PARENTESCO**

> **`LECTURA`, marcada aparte:** el `0,911` de `calibrar_ascensos_evitar_politica` contra
> `bloquear_tiempo_pensar_calendario` es la senial mas alta de toda la tanda **y no mide
> ningun parentesco.** Lo compruebo en las dos puntas y lo dejo escrito:
>
>     $ awk 'NR==219' fuentes/scott_radical_candor/cap_10.md | tail -c 45
>     Encourage your whole team to do the same.
>     $ awk 'NR==173' fuentes/scott_radical_candor/cap_11.md | tail -c 50
>     Encourage everyone on your team to do the same.
>     $ (bitacora, linea 457) detalle_paso: paso 14 del candidato contra paso 6 de
>       bloquear_tiempo_pensar_calendario
>
> **Son DOS lineas distintas del libro que dicen casi lo mismo**, y la traduccion las deja
> casi identicas (*Y anima a todo tu equipo a hacer lo mismo* contra *Y anima a todos los de
> tu equipo a hacer lo mismo*). Una cierra una reunion de calibracion de ascensos (`cap_10`)
> y la otra manda blindar tiempo de pensar en el calendario (`cap_11`). **Es el ejemplar
> limpio de `D.19`: la senial dijo donde mirar y ahi acabo su trabajo.**

---

## 10. MIS CLASES, ADJUDICADAS ANTES DE DESTAPAR NINGUNA `razon`

**LO QUE HE ABIERTO Y LO QUE NO, dicho antes de la tabla:** de `bitacora/VEREDICTOS.jsonl`
he leido `candidato`, `vecino`, `veredicto`, `senales`, `levantada_por`, `arista`,
`arista_en_cola` y `anotaciones`, que son estado y no reporte. **NO he abierto ni un solo
campo `razon`**, que es lo que `AUDITOR_FORJA.md` 1.2 manda destapar despues. **La
comparacion que de verdad mide algo es la de las RAZONES, y esa sigue sellada.**

Cada clase de aqui abajo la adjudico con la vara de la seccion 6: **que anade el hijo a la
madre, sin bascula**, con los pasos de los dos nodos y el tramo del libro delante.

    $ (mi lector: los veredictos nuevos de la tanda)
    total veredictos: 464   nuevos desde la linea 428: 37
    SANO 24, CONTINUA 13
    levantada_por: lectura declarada 22, paso_contra_nodo 6, similitud_texto 6, familia_id 3
    veredictos levantados por SENIAL: 15     por LECTURA DECLARADA: 22

### 10.1. LAS `13` DE CLASE `CONTINUA`: **LAS `13` ME SALEN `CONTINUA`, Y CON LA MISMA DIRECCION**

| # | madre a hija que la bitacora declara | mi lectura |
|---:|---|---|
| `428` y `430` | `desplegar_tres_conversaciones_carrera` a `conversar_historia_vida_descubrir_motivadores` | **`CONTINUA`.** La madre prescribe la serie y su cadencia (`L19`, `L21`, `L43`) y nombra la materia en un paso; la hija despliega la primera conversacion entera (`L47` a `L59`): apertura literal, foco, cuatro ejemplares de motivador, el limite de no insistir y la practica entre jefes. **Lo que queda fuera es procedimiento en los dos lados** |
| `431` | el mismo par, **linea duplicada y declarada** | **`CONTINUA`,** y la linea lleva su `CORRECCION DECLARADA` diciendo que es duplicado de la `430` por bandeja sin archivar (`D.31`). Seccion 10.4 |
| `433` | `desplegar_tres_conversaciones_carrera` a `conversar_suenios_cruzar_habilidades` | **`CONTINUA`.** La hija trae objeto de trabajo propio: el documento de columnas de suenios contra filas de habilidades de `L71` |
| `437` | `desplegar_tres_conversaciones_carrera` a `trazar_plan_dieciocho_meses_aprendizaje` | **`CONTINUA`.** La hija trae las cuatro preguntas literales de `L79` y la lista con plazos de `L81` |
| `464` | `construir_confianza_equipo_tiempo_solas` a `desplegar_tres_conversaciones_carrera` | **`CONTINUA`, y es la mejor fundada de la tanda**: `cap_08` `L95` escribe la remision **literal**, *Having annual career conversations is also an excellent way to strengthen your relationship ... (see chapter seven)*, y `cap_10` **es** el capitulo siete (`unidad: Cap. 7`). Comprobado en el fichero, no supuesto |
| `429` | `desplegar_plan_orden_operaciones_franqueza_radical` a `desplegar_tres_conversaciones_carrera` | **`CONTINUA`,** y la madre esta EN LA BANDEJA: `arista_en_cola: true`. `cap_12` `L41` y su `P14` nombran la ronda anual de conversaciones de carrera en una linea; el nodo de `cap_10` la despliega |
| `438` | `desplegar_plan_orden_operaciones_franqueza_radical` a `armar_plan_anual_crecimiento_equipo` | **`CONTINUA`,** en cola. `cap_12` `L41` *Start doing a growth-management plan for each person on your team* es exactamente el `P2` de la hija |
| `461` | `desplegar_plan_orden_operaciones_franqueza_radical` a `evitar_obsesion_ascenso_estatus` | **`CONTINUA`,** en cola. `cap_12` `L41` *Make sure that you are not creating a promotion-obsessed culture*. **Y aqui esta mi hallazgo de la seccion 11.2, porque la MISMA linea lleva una segunda remision que no se cableo** |
| `443` | `armar_plan_anual_crecimiento_equipo` a `facilitar_despido_tres_cosas` | **`CONTINUA`.** `L111` nombra el arranque del despido dentro de los planes de crecimiento; la hija despliega `L169` a `L173` |
| `447` | `facilitar_despido_tres_cosas` a `admitir_pronto_mal_desempenio_cuatro_razones` | **`CONTINUA`.** Primera de las tres cosas de `L173`, desplegada en `L175` a `L179` |
| `450` | `facilitar_despido_tres_cosas` a `calibrar_decision_despido_documentarla` | **`CONTINUA`.** Segunda, `L181` a `L187` |
| `454` | `facilitar_despido_tres_cosas` a `sopesar_consejo_legal_despedir_humildad` | **`CONTINUA`.** Tercera, `L189` a `L195` |

**LAS `13` LINEAS SON `11` PARES DISTINTOS**, y el reparto lo mido: **`3` los levanto una
senial** (`0,741`, `0,647` mas `0,641` del mismo par por sus dos extremos, y `0,608`) **y `8`
los levanto la lectura declarada, sin senial ninguna por encima de umbral.** **Ninguna de
las `13` la adjudico yo por la senial**: las adjudique leyendo los pasos de los dos nodos
contra su tramo del libro, que es lo que `D.19` manda y lo que `6.2` llama leer los pasos en
vez de argumentar por senial.

### 10.2. LAS `24` DE CLASE `SANO`: **ME SALEN `SANO` LAS `24`. DOS ERAN UNA ELECCION Y LO DIGO**

Las `22` que no discuto caen en tres familias, y las agrupo en vez de repetir el argumento
veinticuatro veces (`D.47`):

| familia | lineas | por que `SANO` |
|---|---|---|
| **hermanas bajo una misma cabeza** | `432`, `435`, `436`, `445`, `446`, `449`, `451`, `452`, `453`, `455`, `456`, `462`, `463` | ninguna es despliegue ni condicion de la otra: cuelgan todas de la misma madre, y lo que queda fuera del solape **es procedimiento en los dos lados** |
| **materia distinta que una senial junto** | `434`, `439`, `441`, `442`, `444`, `448`, `457`, `458`, `460` | la senial mide vocabulario o convencion de nombres, no parentesco. `457` es el ejemplar (seccion 9.2); `458` y `460` levantan por `familia_id` `0,333` sobre la palabra *ascenso*, y una calibra ascensos entre jefes mientras la otra manda no anunciarlos |
| **cruce entre libros** | `439`, `442` | `disenar_equipo_plan_anual` planifica **a quien contratar el anio que viene**; `armar_plan_anual_crecimiento_equipo` planifica **el crecimiento de quien ya esta**, y `montar_proceso_contratacion_reducir_sesgo` monta **como se entrevista**. Tres objetos de trabajo distintos con la palabra *plan anual* encima |

#### `MI DISCUTIBLE 1`, linea `440`: `armar_plan_anual_crecimiento_equipo` contra `desplegar_tres_conversaciones_carrera`. **SOSTENGO EL `SANO`, PERO PROPONGO LA ARISTA**

**NO ES UN GEMELO Y EN ESO NO HAY DUDA**: uno tiene las tres conversaciones de carrera como
entregable y el otro el cuadro de casillas mas los planes de tres a cinco puntos. **Como
clase, `SANO` es correcto.**

**LO QUE SI LEVANTO ES LA ARISTA QUE NO SE CABLEO**, y lo levanto con la linea delante:
`cap_10` `L97` abre la seccion `GROWTH MANAGEMENT` con *YOU'VE HAD YOUR three conversations
and begun the process of lining up opportunities on your team with each person's
aspirations*, **y el `P1` de `armar_plan_anual_crecimiento_equipo` transcribe esa frase
entera**. Es la misma figura que la `464` cableo desde `cap_08` `L95`: **el libro escribe la
remision y la casa la cablea.** Lo dejo como `POR ADJUDICAR 4` y **no lo cargo como caida**,
porque `SANO` no es una clase equivocada y porque la vuelta marco la linea como `lectura
declarada`, es decir, la miro.

#### `MI DISCUTIBLE 2`, linea `455`: `contactar_despedido_mes_despues` contra `facilitar_despido_tres_cosas`. **SOSTENGO EL `SANO` Y DIGO POR QUE ERA UNA ELECCION**

`L173` dice **`three things`** y debajo hay **CUATRO** rotulos imperativos: `L175`, `L181`,
`L189` y `L197` *Follow up*. La vuelta asigno los tres a los tres primeros y dejo `Follow up`
fuera, con `nodos_previos` vacio. **Lo sostengo, y la razon es del propio `L173`:** las tres
cosas son las que *make it far, far easier on the person you are firing*, y el seguimiento de
`L199` ocurre **un mes despues del despido**, cuando ya no puede hacerlo mas facil. **La
cuarta no es una de las tres: es lo que viene despues.**

**Y DIGO LO QUE ME HARIA CAMBIAR DE IDEA**, para que no sea una postura: si el reporte
sostiene la cuarta con una linea del libro que yo no he visto, la adjudico a su favor.

### 10.3. LA MUESTRA PINEADA DE LOS `SANO` (`AUDITOR_FORJA.md` 7): **`5`, SORTEADOS CON SEMILLA ESCRITA**

    $ (mi sorteo)
    SANO de la tanda: 24
    muestra que manda la seccion 7: max(3, 20% de 24) con techo 20 = 5
    semilla escrita: 36     random.Random(36).sample sobre las lineas SANO ordenadas
    lineas elegidas: [432, 434, 435, 445, 446]

**Las cinco las releo enteras en la seccion 10.2 y las cinco se sostienen.** Elegidas al
azar y no a ojo, que es lo que la seccion 7 manda: **elegir a ojo mide lo que el auditor ya
sospecha.**

    $ (mi lector: D.8 sobre la bitacora entera)
    D.8, SANO sin razon escrita en la tanda: 0
    D.8, SANO sin razon en TODA la bitacora: 0
    largo medio del campo razon en los 37 nuevos: 461 caracteres

**`D.8` no tiene nada que cobrar: cero `SANO` sin razon escrita, ni en la tanda ni en las
`464` lineas.** Y lo mido por **longitud del campo**, sin abrir su contenido, que es lo que
me deja comprobarlo sin romper mi propia ceguera.

### 10.4. LA LINEA DUPLICADA, QUE **YA VIENE DECLARADA**

Las lineas `430` y `431` son el mismo par, la misma direccion de arista, las mismas huellas
y las mismas seniales (`0,641`). **La `431` lleva su `CORRECCION DECLARADA` puesta en
`anotaciones`**, con esta razon: *duplicado de la linea 430 por bandeja sin archivar (D.31),
declarado sin borrar*.

> **`LECTURA`, marcada aparte:** el asunto de un commit de la vuelta declara esta caida
> como propia y la sube el mismo. **Yo no la adjudico aqui** y no le pongo especie: la sede
> es `bitacora/`, la figura es una operacion que cambia `bitacora/` **sin que ningun
> veredicto este mal puesto**, y eso tiene nombre desde el 16 sep (`DATO MOVIDO`).
> **Lo que si mido hoy, y es lo que decide si quedo algo suelto, es esto:** cero duplicados
> entre bandeja y grafo, `113` archivados contra `113` en grafo sin huerfanos por ninguno de
> los dos lados, y `117` aristas casando por los dos extremos. **El rastro esta cerrado.**
> Con el reporte delante le pondre su especie y su escalon, no antes.

### 10.5. LOS CINCO HUERFANOS DE `cap_10`, CONTADOS

    $ (mi lector: nodos sin nodos_previos y sin nodos_siguientes)
    HUERFANO: montar_proceso_contratacion_reducir_sesgo
    HUERFANO: contactar_despedido_mes_despues
    HUERFANO: calibrar_ascensos_evitar_politica
    HUERFANO: evitar_obsesion_ascenso_estatus
    HUERFANO: reconocer_excelencia_trayectoria_gradual
    grafo entero: cableado 146, huerfano 170

**`5` de los `14` entran sin arista por ningun extremo**, y `170` de `316` lo estan en el
grafo entero, asi que **no es una anomalia de esta vuelta y no la cargo como tal.** Dos
matices que si son de esta vuelta:

- **`evitar_obsesion_ascenso_estatus` es huerfano en el grafo pero NO en la cola**: su arista
  desde `desplegar_plan_orden_operaciones_franqueza_radical` esta escrita con
  `arista_en_cola: true` y entrara cuando entre la madre. **Huerfano hoy, cableado el dia que
  `cap_12` pase la aduana.**
- **`reconocer_excelencia_trayectoria_gradual` es huerfano y ademas es el destino de la
  arista que propongo en la seccion 11.2.** Si esa remision se cablea, deja de serlo.

### 10.6. LO QUE PREDIGO DEL REPORTE, ESCRITO ANTES DE VERLO Y **PARA QUE SE ME PUEDA TUMBAR**

Una apertura ciega que solo confirma lo que ya sabe no mide nada. **Estas cinco son
falsables y se comprueban abriendo el reporte:**

| # | predigo | por que |
|---:|---|---|
| `1` | que **`facilitar_despido_tres_cosas` `P11` va marcado DISCUTIBLE** | `L173` dice *three things* **y no las enumera ahi**: las tres salen de los tres rotulos siguientes. Es la pieza de `cap_10` que mas se parece a una lectura y menos a una transcripcion |
| `2` | que **`sopesar_consejo_legal_despedir_humildad` `P7` va marcado DISCUTIBLE** | *Deja a la persona despedirse en sus propios terminos* es lo que la autora **hizo** en el caso de Juice (`L193`), puesto en imperativo. Manual 3.5 dice que el caso no es la casa |
| `3` | que **`desplegar_tres_conversaciones_carrera` `P10` y `P11` vuelven a ir marcados**, por transposicion de persona | su propio `resumen_teorico` ya los declara marcados **desde la vuelta 22**, asi que seria un discutible heredado y no nuevo |
| `4` | que **`conversar_suenios_cruzar_habilidades` `P9` va marcado**, por *la conversacion anterior* | el `resumen_teorico` del nodo lo declara como caso limite: `L71` dice *the last conversation* aunque en el orden del texto los suenios se acaban de describir en esta misma |
| `5` | que **`L253` `AVOID ABSENTEE MANAGEMENT AND MICROMANAGEMENT` aparece declarada como dejada fuera con su razon** | seccion 8.4. Si NO aparece, la frontera de `cap_10` se cerro sin decir que hacia con su ultima seccion nombrada |

**Y DIGO LO QUE NO PREDIGO, PORQUE YA ME LO DIERON:** `14 de 14` y `0 PUENTE de 206` vienen
en los asuntos de commit que el prompt me entrega (seccion 12). **Que yo los mida y me
salgan iguales vale; que yo los prediga, no.**

---

## 11. LA FRONTERA DE LO QUE ESPERA EN BANDEJA: `cap_12`, `cap_13` Y `cap_14`

Lo leo ahora **porque es lo que la vuelta siguiente tomara**, y porque si el arnes estuviera
abriendo la 37 en vez de la 36 esta seria la poblacion que me toca clasificar.

    $ (mi lector de rotulos y de las lineas declaradas por cada candidato)
    cap_12: 65 lineas, 2145 palabras, 3 rotulos, 2 candidatos, 50 pasos
    cap_13: 347 lineas, 9331 palabras, 40 rotulos, 12 candidatos, 208 pasos
    cap_14: 243 lineas, 7670 palabras, 29 rotulos, 15 candidatos, 178 pasos

### 11.1. `cap_14` CIERRA AL DIGITO Y LO COMPRUEBO CONTRA EL PROPIO LIBRO

El capitulo enumera **trece elementos** de un proceso formal de evaluacion (`L35` a `L63`) y
luego los desarrolla uno a uno, numerados `1.` a `13.`, de `L65` a `L239`. Los `15`
candidatos se declaran `PIEZA P1` a `PIEZA P15`, y el reparto es exacto: **`P1` la cabeza de
`L21` a `L33`, `P2` la lista de los trece de `L35` a `L63`, y `P3` a `P15` los trece
elementos, uno por elemento.** `2` mas `13` son `15`. **Los tramos declarados son contiguos
y no se pisan**; lo unico que queda fuera son `L9` a `L19` (titulo y entrada) y `L241`
`CONCLUSION`, **y las dos cosas es correcto dejarlas fuera**.

### 11.2. `cap_12` TIENE DOS CANDIDATOS, Y **EN UNO DE ELLOS CAZO UNA PIEZA QUE NO ME GUSTA**

*(En las citas del libro cambio las comillas y los apostrofos tipograficos por los de
teclado, y lo digo en vez de callarlo: es la unica diferencia entre lo que el fichero tiene
y lo que aqui se lee. Ni una palabra cambiada.)*

    $ awk 'NR==41' fuentes/scott_radical_candor/cap_12.md | fold -w 78
    Plan for the future of your team. Start doing a growth-management plan for eac
    h person on your team. (See "Growth Management Plans" in chapter seven.) M
    ake sure that you are not creating a promotion-obsessed culture, and give some
     extra thought to how you're rewarding your rock stars (see chapter seven).
    $ python -c "...print(d['pasos_accionables'][32])" | fold -w 78
    Asegurate de que no estas creando una cultura obsesionada con el ascenso, y de
    dica un pensamiento extra a como estas recompensando a tus superestrellas.
    $ (mi barrido de las dos palabras sobre el libro y sobre la bandeja entera)
    cap_10: rock star(s)=7  superstar(s)=8
    cap_12: rock star(s)=1  superstar(s)=0
    cap_13: rock star(s)=0  superstar(s)=0
    cap_14: rock star(s)=0  superstar(s)=0
    bandeja entera, unica aparicion de cualquiera de las dos:
      desplegar_plan_orden_operaciones_franqueza_radical  P33  superestrellas

> **`LECTURA`, marcada aparte, y es la mia:** **`cap_12` escribe `rock stars` UNA vez y
> `superstar` NINGUNA, y el candidato lo traduce por `superestrellas`.** En este libro las
> dos no son sinonimos: son **las dos mitades opuestas** de su propio marco, la trayectoria
> gradual contra la empinada, y `cap_10` las usa `7` y `8` veces para oponerlas. **Un paso
> que manda recompensar a la mitad contraria de la que el libro nombra dice lo que el libro
> no dice**, que es la definicion de `PUENTE` de `D.30`.
>
> **LO QUE ESTO NO ES:** no toca la fidelidad de `cap_10` ni el `0` de `206` de la seccion
> 8, porque el paso vive en un candidato de `cap_12` **que todavia espera en la bandeja y no
> ha entrado en el grafo**. **Lo dejo levantado antes de que entre**, que es donde sirve de
> algo, como `POR ADJUDICAR 5`.

**Y DE LA MISMA LINEA `L41` SALE MI SEGUNDA PROPUESTA DE ARISTA.** Esa sola frase lleva
**dos** remisiones a *chapter seven*, que es `cap_10`: una a la cultura obsesionada con el
ascenso y otra a **recompensar a los rock stars**. La vuelta cableo la primera (linea `461`,
a `evitar_obsesion_ascenso_estatus`) **y no la segunda**, que apunta derecha a
`reconocer_excelencia_trayectoria_gradual`, el nodo de la seccion `REWARD YOUR ROCK STARS` de
`L225`. **`POR ADJUDICAR 6`.**

### 11.3. `cap_13`: `12` PIEZAS, Y **UNA SOLA SECCION NOMBRADA SIN CANDIDATO**

Los `12` candidatos declaran tramos que cubren de `L17` a `L322` dejando fuera, a proposito,
los relatos (`L23` a `L34`, `L87` a `L104`, `L121` a `L128` y `L253` a `L266`: *Kim's
Soliciting Feedback Story* y las dos *Jason's Story*). **Manual 3.5, el caso no es la casa:
bien dejados fuera.**

**Lo que queda sin candidato y no es un relato es `L323` `DIVERSITY AND INCLUSION` y `L333`
`WHAT'S NEXT?`.** Los leo antes de opinar: **`L333` a `L345` es promocion** (los programas de
la empresa, la direccion web, el correo y el Twitter) y **esta bien fuera**. **`L323` a
`L331` no es tan limpio:** dentro del relato de una participante hay una practica con
periodo y metodo, *spaghetti dinners once a month* donde se comparten las historias y se
ensaya lo que se podria haber dicho. **Mi lectura ciega es que NO es nodo**, porque la
practica se la atribuye el libro a una asistente a un taller y lo que el texto hace con ella
despues es anunciar su propio taller. **Pero es la unica omision de `cap_13` que admite
discusion, y la dejo escrita ahora**, antes de que la vuelta que inserte `cap_13` la decida.
**`POR ADJUDICAR 7`.**

---

## 12. LAS CONTAMINACIONES: LAS QUE NO ELEGI Y LAS QUE SI. **LAS DECLARO TODAS**

| que | de donde | que me dio |
|---|---|---|
| **los asuntos de commit de la vuelta 36** | vienen dentro del propio prompt del arnes, en su `gitStatus` | **cifras suyas**: `14 de 14`, `0 PUENTE de 206`, la remision de `cap_08` `L95` y el duplicado que se cazo. **No lo elegi y no puedo deshacerlo.** Lo que hice fue **medir las tres por mi cuenta antes de citarlas** y publicar las mias: `14` nodos, `206` pasos, `0` PUENTE, `cap_08` `L95` leida en el fichero. **Y lo que ningun asunto de commit me dio, que es lo que de verdad va sellado aqui: ni una sola `razon`, ni cual de los `206` marco el como discutible, ni sus tablas de cierre** |
| **`docs/loop/ACTA_AUDITOR.md`** | lo abri yo, entero | **esta permitido y es obligatorio** (`AUDITOR_FORJA.md` 1.5, *es lo unico que te deja saber que te encargaste a ti mismo*). Es obra mia y no es ninguno de los cuatro de `D.34.2` |
| **`docs/loop/APERTURA_CIEGA.md` de `HEAD`** | lei **su primera linea y nada mas**, con `head -1`, para resolver la ambiguedad de la seccion 2 | la linea dice `VUELTA 35`. **No abri su cuerpo** |
| **`docs/loop/ultimo_apertura.json` de `HEAD`** | lo abri con `git show` | es el mensaje final de **mi propia apertura anterior**, obra mia, y **no es ninguno de los cuatro que `D.34.2` retira**. No contiene ni una linea del extractor. **Lo declaro igual que lo declaro mi predecesor, en vez de callarlo** |

**LO QUE NO TOQUE, Y ES LO QUE MANDA:** de `docs/loop/REPORTE.md`, `docs/loop/loop.log`,
`docs/loop/ultimo_extractor.json` y `docs/loop/ultimo_auditor.json` **no he recuperado ni una
linea de contenido**, ni con `git show`, ni con `git checkout`, ni leyendo un `diff` que los
contenga.

**Y APURO LA DECLARACION HASTA DONDE LLEGA, porque decir *no los toque* a secas seria decir
de mas:** el `git show --stat 8cb6a99` de la seccion 2 imprime **los nombres de dos de ellos
y cuantas lineas cambiaron** (`loop.log` mas `18`, `ultimo_extractor.json` menos `1`).
**Nombre y recuento, cero contenido.** Lo corri para saber que habia commiteado ese commit,
que es la pregunta de la seccion 2, y lo que devolvio es justo lo que la hizo contestable:
que ese commit **no traia ninguna apertura ciega**.

---

## 13. LO QUE DEJO `POR ADJUDICAR` PARA MI TURNO NORMAL

| # | que pregunta | por que no lo cierro aqui |
|---:|---|---|
| `1` | **los `3` fallos y `1` error de la suite**: son de los ficheros retirados o hay un rojo de verdad debajo | no puedo recuperar `REPORTE.md` ni `CREDITO_serial.jsonl` sin invalidar mi apertura. **Se re corre con el arbol entero** |
| `2` | **`L253`, la unica seccion nombrada de `cap_10` sin nodo**: la vio la vuelta y la descarto con su razon, o se le paso | mi lectura es que esta bien fuera (`D.27`), pero **quien lo tiene que haber dicho es el reporte** |
| `3` | **la asimetria de `senal_similitud_texto`**, medida en `0,371` contra `0,349` sobre el mismo par | seccion 9.2. **Aqui no perdio nada** y no la cargo a nadie: es una propiedad del instrumento que sube a la cola de doctrina (`D.53`), y `D.45` me prohibe resolverla yo |
| `4` | **la arista `desplegar_tres_conversaciones_carrera` a `armar_plan_anual_crecimiento_equipo`**, que `cap_10` `L97` escribe y el `P1` de la hija transcribe | es propuesta, no caida: la clase `SANO` de la linea `440` es correcta y la vuelta la marco como leida |
| `5` | **`superestrellas` donde `cap_12` `L41` dice `rock stars`**, en un candidato que todavia espera en bandeja | **levantado antes de que entre**, que es donde sirve. No toca el `0` de `206` de `cap_10` |
| `6` | **la segunda remision de `cap_12` `L41`**, a `reconocer_excelencia_trayectoria_gradual`, que no se cableo mientras la primera si | propuesta de arista, misma linea del libro |
| `7` | **la cena de practica de `cap_13` `L329`**: nodo o caso | lo decide la vuelta que inserte `cap_13`. Lo dejo escrito **antes**, que es la unica forma de que sirva |
| `8` | **la especie y el escalon del duplicado de la linea `431`** | seccion 10.4: con el reporte delante, no antes |
| `9` | **el commit `8cb6a99` titulado `Apertura ciega de la vuelta 36` que no trae ninguna apertura** | maquinaria del arnes (`D.33`), `D.45` me prohibe tocarla. **Sube como propuesta en el acta** |
| `10` | **la convencion `UNIDAD DE ORIGEN: fuentes/<clave>/cap_NN.md`**, que llevan `112` de `316` nodos del grafo y `112` de `113` de scott | **NO es una caida y no la cargo:** el unico scott que no la lleva **si dice su capitulo en prosa** (seccion 7). Lo subo porque es el patron que me habria hecho publicar una frase falsa, y esta escrito para que el siguiente lector no tropiece en el mismo sitio |

---

**NO COMMITEO NADA.** El arnes sella este fichero y lo commitea el, y `AUDITOR_FORJA.md` 1.5
dice que un sello roto detiene la corrida: **no vuelvo a tocarlo despues del sello.**

**ACTA ANTERIOR LEIDA: 4ec70432816947ebfad797050359b47e537ca7d9**
