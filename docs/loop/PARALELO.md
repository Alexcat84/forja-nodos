# EL PARALELO: TRES FRENTES QUE EXTRAEN, UNA SESION QUE INSERTA

*Decision del fundador del 16 sep 2026, `D.45` y `D.47` del banco. **Este fichero es el
manual de operacion del paralelo**: los comandos, la regla que nadie puede saltarse, y el
procedimiento de cosecha.*

> ## **EL PARALELO EXTRAE. EL SERIAL INSERTA. NINGUN FRENTE INSERTA NUNCA.**

---

## 1. POR QUE SE PUEDE PARALELIZAR LA EXTRACCION Y NO LA INSERCION

| acto | donde escribe | en paralelo |
|---|---|---|
| **extraer** | `cuarentena/<libro>/`, **ficheros nuevos, uno por candidato, disjuntos entre libros** | **SI** |
| **insertar** | `dataset/nodos.jsonl`, `bitacora/`, `censos/`, `config/pares_mutuos.jsonl`: **sedes unicas** | **NO** |

**Y NO ES UNA PRECAUCION TEORICA.** La vuelta 28 lanzo dos `insertar` a la vez y **un nodo
entro en el grafo y desaparecio, con el `gate` en VERDE encima.** De ahi salieron el
cerrojo y `D.44`.

**PERO EL CERROJO NO BASTA PARA AUTORIZAR EL PARALELO DE INSERCION, y conviene decirlo:**
el cerrojo impide que dos escrituras se pisen, **no hace que dos lecturas del grafo midan
lo mismo.** Cada insercion cambia lo que la siguiente mide (`D.36`, el orden que lee).
**Dos inserciones en paralelo no son la misma campania mas deprisa: son dos campanias
distintas.**

---

## 1.b. **EL ALCANCE DE HOY: DOS LINEAS Y NO MAS** (17 sep 2026, `D.50`)

> **La principal SIEMPRE ACTIVA, y UN SOLO frente de extraccion**, hoy
> `grove_high_output` **hasta cerrar su libro**.
>
> **`gerber_emyth` y `marquet_turn_the_ship` quedan `PAUSADOS` con dueño `NINGUNO`**, su
> trabajo parcial declarado en el tablero (**`10` y `9` candidatos**). **No se lanzan**, y
> **seran relevados por el principal cuando le toquen por el orden** (`D.50`).

**LO QUE SIGUE DE ESTE DOCUMENTO DESCRIBE TRES FRENTES PORQUE ASI SE MONTO EL 16 SEP.**
Los comandos siguen siendo buenos y por eso no se borran: **lo que cambia es cuantos
corren a la vez**, y hoy es **uno**.

---

## 2. LOS TRES FRENTES, EN ORDEN DE VALOR

| # | libro | unidades | palabras | rama | carpeta |
|---:|---|---:|---:|---|---|
| **1** | `grove_high_output` | **18** | **64.862** | `extraccion-grove_high_output` | `../forja-grove_high_output` |
| **2** | `gerber_emyth` | **22** | **63.434** | `extraccion-gerber_emyth` | `../forja-gerber_emyth` |
| **3** | `marquet_turn_the_ship` | **17** | **34.217** | `extraccion-marquet_turn_the_ship` | `../forja-marquet_turn_the_ship` |

*Las tres claves estan **registradas en `fuentes/FUENTES_CANONICAS.json`** y los tres libros
estan **en `fuentes/<clave>/`**. `marquet_turn_the_ship` ya tiene **3 candidatos en
bandeja** de la vuelta 25: **su frente continua, no abre.***

### Por que `git worktree` y no tres clones

**UN SOLO ALMACEN DE OBJETOS Y TRES ARBOLES DE TRABAJO.** Un clon aparte duplicaria el
repo entero por frente y **dejaria las ramas invisibles desde aqui**; con worktree,
`git worktree list` las ensenia todas y **la cosecha se hace en local, sin remoto de por
medio.**

**Y TRAE UNA GUARDA GRATIS QUE AQUI VALE ORO:** git **no deja tener la misma rama
registrada en dos worktrees a la vez.** Dos sesiones sobre el mismo libro **no pueden
ocurrir por accidente.**

---

## 3. LOS COMANDOS

### 3.1. Preparar los tres arboles (ya hecho, se deja escrito por si hay que rehacerlo)

    cd /c/Users/AlexDesk/Documents/forja-nodos
    git worktree add ../forja-grove_high_output        extraccion-grove_high_output
    git worktree add ../forja-gerber_emyth             extraccion-gerber_emyth
    git worktree add ../forja-marquet_turn_the_ship    extraccion-marquet_turn_the_ship

### 3.1.b. **COPIAR EL CORPUS, QUE NO VIAJA EN GIT** (paso obligatorio)

**`fuentes/<clave>/` ESTA EN `.gitignore` A PROPOSITO**: son libros con derechos y pesan,
y lo unico que entra al repo es `fuentes/FUENTES_CANONICAS.json`. **Un worktree recien
creado NO tiene los libros**, y sin ellos el frente no puede minar **ni pasar el censo**:
el reporte que hereda cita rutas como `fuentes/smart_who/cap_01.md`, y ahi no estarian.

**Esto lo descubrio el censo `D.42` al preparar los frentes**, abortando el primer commit
de un worktree. **Se deja escrito porque es justo lo que habria reventado en el
lanzamiento:**

    cd /c/Users/AlexDesk/Documents/forja-nodos
    for k in grove_high_output gerber_emyth marquet_turn_the_ship; do
      cp -r fuentes/*/ "../forja-$k/fuentes/" 2>/dev/null
    done

**Se copia el corpus ENTERO y no solo su libro**, y por dos motivos: el reporte heredado
cita capitulos de libros ya minados, **y un auditor de frente tiene derecho a recontar una
ruta que su propio reporte publica.**

### 3.1.c. **QUE REGISTRO HEREDA UN FRENTE: DECIDIDO EL 17 SEP 2026** (`D.48`)

> #### ESTUVO ABIERTO UN DIA, Y ASI ESTABA PLANTEADO
>
> **UN FRENTE HEREDA EL REGISTRO DE LA LINEA DE INSERCION, Y ESO LE HACE AUDITAR TRABAJO
> AJENO.** Al crear la rama, el frente se lleva `REPORTE.md` y `ACTA_AUDITOR.md` enteros,
> **con las actas y las rachas de otra campania.**
>
> **Medido el 16 sep:** el frente `grove` paro citando como suyas **tres tandas de la
> linea principal**, todas sobre `cap_11` de `scott_radical_candor`, **que no es su
> libro**. Y `D.40` le entrego **cuatro remedios** del acta de otra linea.

**LA DECISION DEL FUNDADOR DEL 17 SEP 2026 LO CIERRA, Y ES `D.48`:**

> **CADA LINEA LLEVA SU PROPIA RACHA. UN FRENTE NACE CON LA SUYA EN CERO.** La racha de
> la serial **no viaja** a los frentes ni al reves, y **al cosechar, la racha del frente
> muere con el frente**: sus caidas quedan como registro en sus actas archivadas.
>
> **EL CREDITO VIVE EN `docs/loop/CREDITO_<linea>.jsonl`**, la serial incluida
> (`CREDITO_serial.jsonl`), **y la herencia de `D.40` es la de SU linea.**

**QUE SIGNIFICA AL LANZAR UN FRENTE, EN UNA LINEA:** el frente no tiene fichero de
credito, asi que **no ha cerrado ninguna tanda, hereda CERO remedios y arranca con todas
sus rachas en cero**, aunque tenga las `31` actas de la serial delante en el arbol. El
arnes lo dice en voz alta en su log, y `python forja.py credito` lo dice antes de lanzar.

**LO QUE EL FRENTE TIENE QUE HACER A CAMBIO:** escribir su tanda al cerrar cada acta,
con `python forja.py credito --anotar`. Una linea que no escribe su credito **sigue
naciendo cada vuelta**, y eso no es una racha en cero: es una racha que no existe.

### 3.2. LANZAR CADA FRENTE

**Los tres son el mismo comando con tres nombres cambiados**, y los tres llevan
`MODO_INSERCION=cuarentena`, que es lo que los hace frentes y no campanias.

    cd /c/Users/AlexDesk/Documents/forja-grove_high_output && \
      RAMA=extraccion-grove_high_output MODO_INSERCION=cuarentena MAX_VUELTAS=20 \
      bash orquestador_forja.sh

    cd /c/Users/AlexDesk/Documents/forja-gerber_emyth && \
      RAMA=extraccion-gerber_emyth MODO_INSERCION=cuarentena MAX_VUELTAS=20 \
      bash orquestador_forja.sh

    cd /c/Users/AlexDesk/Documents/forja-marquet_turn_the_ship && \
      RAMA=extraccion-marquet_turn_the_ship MODO_INSERCION=cuarentena MAX_VUELTAS=20 \
      bash orquestador_forja.sh

> ### **SI ALGUIEN ESCRIBE `MODO_INSERCION=insertar` EN UN FRENTE, EL ARNES SE DETIENE**
>
> `comprobar_arranque()` compara la rama activa con `RAMA_DE_INSERCION`
> (`extraccion-mundo-11`) y **para antes de gastar un turno, nombrando las dos ramas**.
> No es una recomendacion escrita en un manual: **es codigo**, con su caso positivo y su
> negativo en `tests/prueba_arnes.sh` (escenarios `16` y `16b`).

### 3.3. LA SESION DE INSERCION, que corre SOLA

    cd /c/Users/AlexDesk/Documents/forja-nodos && \
      RAMA=extraccion-mundo-11 MODO_INSERCION=insertar MAX_VUELTAS=20 \
      bash orquestador_forja.sh

**Mientras esta corre, ningun frente inserta.** Y mientras un frente corre, **esta puede
correr igual**: lo que no puede haber es **dos inserciones**.

---

## 4. LO QUE RIGE EN TODOS LOS FRENTES MIENTRAS DURE EL PARALELO

| | |
|---|---|
| **`MODO_INSERCION=cuarentena`, siempre** | un frente **escribe candidatos y los pasa por la aduana EN SECO**. Nunca inserta |
| **MORATORIA DE MAQUINARIA Y DOCTRINA** (`D.45`) | ninguna sesion toca `src/`, el banco, el arnes ni los protocolos. **Ni con una caida de dato**: se declara, **se para y sube** |
| **MODO AUSTERO** (`D.47`) | reporte y acta encogidos, lotes al techo de candidatos, cero instrumentos nuevos |
| **LAS GUARDAS DE DATO, INTACTAS** | cerrojo, `D.44`, la aduana entera, la fidelidad `D.30`. **El austero recorta tinta, no control** |

**UNA PREGUNTA DE DOCTRINA ES PARADA.** Tres sesiones que corrigen la misma regla a la vez
**producen tres doctrinas**, y el banco es una sede unica igual que el dataset. **Una regla
escrita dos veces en paralelo es peor que una regla que falta: la que falta se nota.**

---

## 4.b. **EL ORDEN DE PRIORIDAD DEL MUNDO 11** (`D.51`, 17 sep 2026)

> **NINGUNA LINEA ELIGE LIBRO.** Toma el primero de esta lista **cuyo `ESTADO` lo permita
> por `D.49`**, y **al cerrar uno pasa al siguiente por `D.50`.**

    python forja.py tablero --siguiente     que libro le toca a ESTA linea, y por que

### Los tres del mundo 11, con el motivo literal de la decision

| | libro | estado al escribirse | por que ahi |
|---:|---|---|---|
| **1** | `grove_high_output` | `EN CURSO`, dueño grove | **Operaciones y apalancamiento gerencial: cubre el hueco de la campania**, que tiene mucho trato con la gente y poco produccion de la maquina. **Densidad de procedimiento la mas alta del lote, medida:** `0,00` por ciento de pasos inventados en su ultimo capitulo, **porque el autor escribe en pasos** |
| **2** | `gerber_emyth` | `PAUSADO`, `10` candidatos hechos | **Sistematizacion del negocio, manual de operaciones, trabajar SOBRE el negocio y no EN el**: es el libro que **habla directo al usuario final** y el unico del lote que aporta esa materia. Al minarlo entero **se completa ademas el capitulo 17 reservado al mundo 10** |
| **3** | `marquet_turn_the_ship` | `PAUSADO`, `9` candidatos hechos | **Delegacion real y control distribuido con practicas concretas.** Solapa en parte con Zhuo y Scott, ya insertados, **pero es barato de cerrar y cierra el cuerpo** |

> # **=== CORTE DEL MUNDO 11 ===**

### Los tres que NO se extraen en esta campania

| | libro | por que |
|---:|---|---|
| **4** | `bernerslee_bananas` | `19` cap. **Mas analisis que procedimiento** |
| **5** | `openstax_business_ethics` | `17` cap. **Manual academico, densidad de procedimiento baja, mucho marco conceptual** |
| **6** | `openstax_org_behavior` | `32` cap. **El mas caro del lote y el de mayor solape con lo ya insertado** (Zhuo, Scott, Grove): **el peor candidato por costo y beneficio de los diez** |

**Quedan en la bandeja, con su ficha**, para **entrar por la aduana de a uno y sin
campania cuando el fundador lo decida.** El tablero los marca con un asterisco, y
`--siguiente` **nunca los devuelve.**

---

## 4.c. **EL CIERRE DEL MUNDO 11** (17 sep 2026, punto `c`)

> **CUANDO LOS TRES PRIMEROS ESTEN `INSERTADOS`**, la linea serial **escribe un
> `PARA_ALEXIS` de `MUNDO 11 COMPLETO` y SE DETIENE.** **El fundador decide que sigue.**

**Lo que ese `PARA_ALEXIS` lleva, y son tres cosas medidas, no tres parrafos:**

| | que va | como se mide |
|---|---|---|
| **1** | **el censo POR LIBRO** | nodos del grafo por su fuente, uno por libro, **mas el total**, con el instrumento pegado (`D.41`) |
| **2** | **las aristas ENTRE libros** | las que cruzan de una clave a otra, **contadas y nombradas**: son lo que prueba que los siete libros son **un grafo** y no siete grafos |
| **3** | **los tres libros que quedan en bandeja** | `bernerslee_bananas`, `openstax_business_ethics` y `openstax_org_behavior`, **con su ficha y su motivo de corte** |

**Y SE DETIENE.** No abre el `4` por orden, no propone un mundo 12, **no decide su propio
alcance.** El tablero lo dice solo cuando llega:

    MUNDO 11 COMPLETO: los tres libros del corte estan INSERTADOS.
    Lo que toca es el CIERRE (PARALELO.md): PARA_ALEXIS de MUNDO 11
    COMPLETO con el censo por libro, y parar.

---

## 4.d. **EL CORTE DEFINITIVO DE ESTA CAMPANIA** (21 sep 2026, decision del fundador)

> # **EL MUNDO 11 CIERRA CON CINCO LIBROS.**
>
> Los **cuatro insertados** (`onu_consumidor`, `smart_who`, `zhuo_manager`,
> `scott_radical_candor`) **mas `grove_high_output` entero.**

| libro | como queda |
|---|---|
| **`gerber_emyth`** | **`10` candidatos en bandeja, enteros y SIN INSERTAR** |
| **`marquet_turn_the_ship`** | **`9` candidatos en bandeja, enteros y SIN INSERTAR** |

**POR QUE NO ENTRAN, Y NO ES UN DESCARTE:** `D.39` dice que **un libro entra cuando su
extraccion cierra**. Los dos estan **abiertos** (`gerber` va por `4` de `22` capitulos,
`marquet` por `3` de `17`), asi que **insertar sus `19` obligaria a minar los dos libros
enteros**, y **eso es lo que esta campania decide no pagar**.

> **QUEDAN COMO MATERIAL, no como basura.** Estan medidos, pasados por la aduana en seco y
> con sus fronteras cerradas. **Entran el dia que la aduana trabaje sin campania**, de a
> uno, como el fundador decida.

**LO QUE CAMBIA RESPECTO DE `D.51`:** aquel orden los ponia en prioridad `2` y `3` **para
esta campania**. El corte **no los borra del orden**: los saca **de esta campania**. Su
prioridad sigue escrita para el dia que se retomen.

---

## 5. EL PROCEDIMIENTO DE COSECHA Y RELEVO (`D.49`, `D.50`)

*Cuando un frente cierra su libro en extraccion, su rama se funde a la de insercion. **Y
desde el 17 sep 2026 eso tiene una sede y un orden obligatorio.***

### 5.0. **PRIMERO SE MIRA EL TABLERO, SIEMPRE** (`D.49`)

**`docs/loop/TABLERO.jsonl` es la sede unica del estado de la campania**, y **ninguna
linea abre ni continua un libro sin consultarlo.**

    python forja.py tablero                        el tablero entero, medido hoy
    python forja.py tablero --puedo <clave>         si ESTA linea puede tomar ese libro
    python forja.py tablero --escribir              lo vuelve a medir y lo vuelca

> **LA REGLA, LITERAL:** ninguna linea abre ni continua un libro cuyo `ESTADO` no sea
> **`SIN EMPEZAR` con dueño `NINGUNO`**, o **`PAUSADO` con dueño `NINGUNO` y ya
> `COSECHADO`**. **El arnes lo comprueba al abrir vuelta y se detiene nombrando al
> dueño.**

**LO QUE ESTO IMPIDE, Y NO ES HIPOTETICO:** `D.32` abre el lote siguiente **sin parada
entre medias** en cuanto uno cierra. El siguiente por orden era el lote `5`,
`marquet_turn_the_ship`, **con `9` candidatos ya minados en otra rama**. La serial habria
vuelto a minar `cap_01`, `cap_02` y `cap_03`.

### 5.0.b. **EL RELEVO, Y SUS CUATRO PASOS EN ORDEN** (`D.50`)

**Cuando la principal CIERRA un libro**, consulta el tablero; si hay un libro `EN CURSO` o
`PAUSADO` en otra rama, **lo releva ENTERO**:

| | paso | quien | como se comprueba |
|---|---|---|---|
| **(a)** | el frente **detenido y sin proceso vivo** | el fundador | `ps` sin su `orquestador_forja.sh`, y su `PARA_ALEXIS.md` en el arbol |
| **(b)** | **su rama se COSECHA** a la de insercion, **una por vez**, gate y suite detras | **el fundador**: *el bucle no funde ramas* | `5.1` a `5.3` de este documento |
| **(c)** | el tablero pasa ese libro a **dueño `NINGUNO`, estado `PAUSADO COSECHADO`** | quien coseche | `python forja.py tablero --escribir` |
| **(d)** | **solo entonces** la principal lo toma y **continua desde el capitulo SIGUIENTE al ultimo minado, citando la frontera heredada** | la principal | `--puedo <clave>` da `SI` y nombra el ultimo capitulo |

> # **NUNCA SE RELEVAN CAPITULOS SUELTOS: SE RELEVA EL LIBRO ENTERO.**
>
> **Un libro medio relevado tiene dos fronteras que nadie casa.** El frente cerro las
> suyas contra el cuerpo, al digito; un relevo por capitulos obligaria a **volver a cerrar
> la frontera del tramo partido**. **El libro entero tiene una sola frontera que heredar.**

**Y EL PASO `(b)` NO LO HACE EL BUCLE.** *El bucle no funde ramas y el bucle no crea
remotos.* Lo que el bucle hace es **pedirlo, nombrando la rama y el estado, y detenerse
hasta que llegue.**

### 5.1. Una por vez, y en este orden

**NUNCA DOS A LA VEZ.** No por miedo al conflicto: porque **entre fusion y fusion hay que
poder decir cual de las dos rompio algo.**

    cd /c/Users/AlexDesk/Documents/forja-nodos
    git checkout extraccion-mundo-11
    git pull --rebase origin extraccion-mundo-11

    # UNA. La que este lista, empezando por la de mas valor.
    git merge --no-ff extraccion-grove_high_output

### 5.2. Que conflictos esperar, y cuales NO son normales

| donde | que esperar |
|---|---|
| `cuarentena/<libro>/*.json` | **NINGUNO.** Son ficheros **nuevos y disjuntos**: cada frente escribe en su propia carpeta y nadie toca la del otro |
| `docs/loop/REPORTE.md`, `ACTA_AUDITOR.md`, `loop.log`, `ultimo_*.json` | **CONFLICTO SEGURO Y ESPERADO.** Cada frente escribe su propio registro. **Se resuelven conservando LOS DOS**, uno detras del otro, y **nunca eligiendo uno** |
| `docs/loop/CREDITO_<linea>.jsonl` | **CERO CONFLICTO, y es la fila que `D.48` vino a crear.** Cada linea escribe SOLO su fichero, asi que al fundir **no se tocan**. **La racha del frente muere con el frente** (`D.48`): su fichero se conserva como registro y **sus caidas no se suman a la serial** |
| `dataset/`, `bitacora/`, `censos/`, `config/pares_mutuos.jsonl` | **NO DEBERIA HABER NINGUNO.** Un frente que los toco **inserto**, y eso es una caida de dato: **se para la cosecha y se mira antes de seguir** |
| `src/`, `docs/BANCO_DE_REGLAS.md`, `orquestador_forja.sh` | **NO DEBERIA HABER NINGUNO.** La moratoria lo prohibe. Si lo hay, **ese frente rompio `D.45`** |

> **LA REGLA DE RESOLUCION, EN UNA LINEA: EN LOS REGISTROS SE CONSERVAN LOS DOS; EN LAS
> SEDES DE DATO NO DEBERIA HABER NADA QUE RESOLVER.** Si hay que elegir en una sede de
> dato, **la cosecha se para**: eso no es un conflicto, es un sintoma.

### 5.2.b. **Y EL TABLERO SE VUELVE A MEDIR** (`D.49`)

    python forja.py tablero --escribir

**En el cierre de cada vuelta de CUALQUIER linea**, y **detras de cada fusion**. Un
tablero que se actualiza cuando alguien se acuerda **es la frase escrita a mano que
`D.49` vino a sustituir.**

### 5.3. Detras de CADA fusion, sin excepcion

    python forja.py gate                 # el censo no decrece (D.44) muerde aqui
    python forja.py guiones
    python tests/test_aceptacion.py
    python scripts/cerrar_reporte.py     # tallado (D.41) y censo de rutas (D.42)

**Si algo cae, se arregla ANTES de fundir la siguiente.** Fundir dos y depurar despues es
perder la unica ventaja de ir de una en una.

### 5.4. Y despues, la insercion serial

**Con los libros ya en `cuarentena/` de la rama de insercion**, corre **una sola sesion**,
**un libro por vez**, con `gate` entre libros:

    RAMA=extraccion-mundo-11 MODO_INSERCION=insertar MAX_VUELTAS=20 bash orquestador_forja.sh

**`D.39` sigue mandando:** solo se inserta un lote **CERRADO en extraccion** cuyo informe
certifique el acta. **`D.36`** (el orden que lee) **y `D.31`** (el archivado en el mismo
acto) siguen enteros, y **el cerrojo garantiza que no haya dos escrituras**, aunque con una
sola sesion no deberia hacer falta: **esta ahi para el dia en que alguien se despiste.**

---

## 6. COMO SE DESMONTA UN FRENTE CUANDO ACABA

    cd /c/Users/AlexDesk/Documents/forja-nodos
    git worktree remove ../forja-grove_high_output
    # la rama NO se borra: es el registro de como entro ese libro

**LA RAMA SE QUEDA.** Un `git log` sobre ella cuenta la extraccion entera de ese libro,
y eso vale mas cuanto mas viejo es (`D.31`, el mismo motivo por el que un candidato
insertado no se borra).

---

## 7. **UNA CARPETA, UN ACTOR DE GIT** (decision del fundador del 24 sep 2026)

*Archivada en `docs/loop/paradas/2026-09-24-una-carpeta-un-actor-DECISION.md`, con el
dictamen de las muertes del 23 sep.*

> ## **MIENTRAS UNA LINEA CORRE, SU CARPETA ES SOLO DEL ARNES.**

- **La sesion de chat vigila SOLO LEYENDO**: `ps`, `tail`, `cat`, y `kill -0` sobre el pid del
  envoltorio. **Ni siquiera `git status`**, que refresca el indice. **Nunca `pull`, `checkout`
  ni `commit`, y nunca escribir ficheros** en una carpeta con una linea a mitad de turno: el
  arnes hace `git add -A` al commitear y se llevaria lo ajeno dentro de su commit.
- **Los arreglos de ARNES se commitean con la linea parada.** Si hay que pararla para
  arreglarla, se para **entre turnos**, en una espera, sin ningun `claude` vivo.
- **NADIE MAS USA ESTAS CARPETAS.** Cualquier otra sesion que necesite leer la forja **hace su
  propio `git clone` en una carpeta aparte**, y no empuja a las ramas de las lineas. **El 23 sep
  a las `06:30:38` otro actor hizo un `git fetch` de las cinco ramas dentro de la carpeta de la
  serial**, y el fundador encontro la otra sesion.

### 7.a. **EL LANZADOR VIGENTE: tarea programada con la ventana oculta**

    powershell -File scripts/lanzar_linea.ps1 -Nombre serial `
        -Arbol C:\Users\AlexDesk\Documents\forja-nodos `
        -Variables "RAMA=extraccion-mundo-11 MODO_INSERCION=insertar MODELO_EXTRACTOR=claude-opus-5-5 MODELO_AUDITOR=claude-opus-5-5 MAX_VUELTAS=20" `
        -Log /tmp/serial.log

Registra la tarea `forja_linea_<nombre>`, que corre `wscript` con un `.vbs` que arranca el Git
Bash **oculto y sin esperarlo**. **Los dos que fallaron, para no volver a ellos:**

| lanzador | que paso |
|---|---|
| `nohup ... &` desde la sesion | murio con el reinicio de Windows Update del 23 a las `00:29:59` |
| WMI, `Win32_Process.Create` | **abria una ventana de consola por linea**, vacia porque la salida va al log; las dos murieron a los `90` segundos |

**SU PRUEBA DE VIDA:** un trabajo de `150` segundos el 23 a las `06:29`, y las dos lineas
lanzadas a las `06:32:31`, vivas pasada la marca de los `90` segundos. **Sus condiciones,
medidas:** no se para por bateria, sin limite de duracion (`PT0S`), no depende de inactividad.

**EL PID QUE SE VIGILA** es el del bash envoltorio, en `<log>.pid`, con `kill -0` desde Git
Bash. **Los pids de Windows NO sirven**: Git Bash cambia de proceso de Windows en cada `exec`, y
eso dio una falsa alarma el 23 a las `06:26`. **Y `bash.exe` a secas es el de WSL**: el script
usa la ruta del Git Bash.

> ### **NINGUN LANZADOR SOBREVIVE A UN REINICIO NI A UNA SUSPENSION.**
>
> El 23 sep a las `00:29:59` Windows Update reinicio el equipo dos veces (`KB5124010`) y las dos
> lineas murieron. **El fundador pauso las actualizaciones el 23 por la manana.** Antes de una
> corrida larga, comprobar que siguen pausadas. **Y tras un reinicio a mitad de una fase
> ciega, sus cuatro ficheros apartados quedan en `/tmp/tmp.*`** y hay que devolverlos a mano:
> el dictamen del 23 sep, seccion `2.a`, dice como.

---

## 8. **EL CIERRE DE LA CAMPANIA DE NODOS** (decision del fundador del 24 sep 2026)

*Archivada en `docs/loop/paradas/2026-09-24-cierre-de-la-campania-DECISION.md`.*

1. **EL MUNDO `10` NO ENTRA.** La extraccion de `gerber_emyth_cap17_reservado` queda **ANULADA**
   (declarada en `config/frentes.json`, clave `anulados`, y el tablero la publica asi). Su
   capitulo queda sin extraer, **y los `6` nodos de ONU se quedan en el grafo** fuera de todo
   pack, como semilla guardada. **Nada se borra.**
2. **EL MUNDO SIGUE SIENDO EL `11`, Primer Equipo.** No se renumera nada.
3. **EL FRENTE DE EXTRACCION SE CIERRA PARA SIEMPRE al cosechar `marquet_turn_the_ship`.**
   Despues de Marquet no hay siguiente libro, y **`D.32` ya no abre lote**.
4. **LA SERIAL INSERTA GROVE, GERBER Y MARQUET**, en ese orden. Con `gate`, `guiones`, la suite y
   `cerrar_reporte.py` en verde, **se crea y se empuja el tag `primer-equipo-completo`**, y el
   reporte de la sesion abre con **`PRIMER EQUIPO COMPLETO`, el hash y el censo por libro**.
5. **DESPUES LA SERIAL SE DETIENE.** La campania de nodos queda **CERRADA**, con su acta final en
   `docs/loop/`. El encargo de la ultima tanda lo dice: al cerrar, `PARA_ALEXIS` de cierre y
   `PROMPT_SIGUIENTE` vacio.
