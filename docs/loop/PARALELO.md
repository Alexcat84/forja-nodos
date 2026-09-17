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

## 5. EL PROCEDIMIENTO DE COSECHA

*Cuando un frente cierra su libro en extraccion, su rama se funde a la de insercion.*

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
| `dataset/`, `bitacora/`, `censos/`, `config/pares_mutuos.jsonl` | **NO DEBERIA HABER NINGUNO.** Un frente que los toco **inserto**, y eso es una caida de dato: **se para la cosecha y se mira antes de seguir** |
| `src/`, `docs/BANCO_DE_REGLAS.md`, `orquestador_forja.sh` | **NO DEBERIA HABER NINGUNO.** La moratoria lo prohibe. Si lo hay, **ese frente rompio `D.45`** |

> **LA REGLA DE RESOLUCION, EN UNA LINEA: EN LOS REGISTROS SE CONSERVAN LOS DOS; EN LAS
> SEDES DE DATO NO DEBERIA HABER NADA QUE RESOLVER.** Si hay que elegir en una sede de
> dato, **la cosecha se para**: eso no es un conflicto, es un sintoma.

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
