# PARADA DEL 16 SEP 2026: EL CERROJO Y EL TESTIGO. **DECISION DEL FUNDADOR**

> ## LA DECISION DEL FUNDADOR, 16 sep 2026
>
> **1. PRIMERO EL DATO.** (a) Recupera el nodo borrado: identificalo por git (el commit
> que lo inserto y el que lo perdio), restauralo desde su version insertada con su
> veredicto y su bitacora, y declara la reparacion con los dos hashes; **nada se borra
> jamas, y lo que se borro se devuelve.** (b) Construye el **CERROJO DE INSERCION** tal
> como la regla escrita lo describe (`4.2`), con caso positivo: dos procesos sobre el
> dataset, **el segundo se bloquea o espera, nunca pisa.** (c) Guarda nueva en el gate,
> **`D.44`, EL CENSO NO DECRECE**: si un nodo presente en `dataset/nodos.jsonl` en el
> commit padre falta en `HEAD` sin estar marcado deprecado con motivo, **el gate cae
> nombrandolo**; caso positivo: la perdida consumada de esta vuelta, reproducida sobre
> copia, **debe tumbar**.
>
> **2. LA RACHA DEL AUDITOR SE REINICIA** con la cura de `A.4`: el **TESTIGO DE GUARDAS AL
> SELLAR**. Al sellar la apertura ciega, el arnes corre las guardas y deja junto al sello
> **la verdad del arbol en ese instante** (hora, salida de cada guarda, hash del arbol);
> `D.38.3` se ensancha: **una cifra vale en el instante del sello**, que el testigo
> registra; si la pagina sellada afirma un estado que el testigo desmiente, **el sello no
> se acepta** (caida cazada por codigo, no por racha). La caida de hoy (cierto al medir,
> falso al publicar, con 44 minutos y cinco guiones en medio) es el ejemplar: **con
> testigo, habria sido verde a las 09:57 y desmentida a las 10:41 por la maquina.**
>
> **3. LAS TRES DE DOCTRINA**, aprobadas como el auditor las escribio en `4.3`: la fila que
> falta a la tabla de especies, **el censo y el tallado leen tambien `APERTURA_CIEGA.md`**
> (la unica sede de cifra que ninguna guarda leia, ya con dos ejemplares), y **`D.43` se
> extiende a la cola de vecinos**.
>
> **4. `PROMPT_SIGUIENTE` de la vuelta 30** con la tarea `1` del retomar del auditor y la
> continuacion del lote en curso.

> **ARCHIVADA.** Este fichero fue `docs/loop/PARA_ALEXIS.md`. **Se archiva entero y sin
> tocar una palabra de su cuerpo ni de su anexo**; lo unico añadido es esta cabecera.
>
> ## 1(a): **NO HABIA NADA QUE RECUPERAR, Y SE DICE CON LA MEDIDA**
>
> La orden era restaurar el nodo borrado con los dos hashes. **Lo busque antes de
> construir nada, y el dato estaba entero:**
>
>     $ (censo del dataset en los 27 commits que lo tocan)
>       222 -> 224 -> 226 -> 227 -> 229 -> 234 -> 234 -> 237 -> 239 -> 240 -> 241 -> 243
>       nodos perdidos entre un commit y el siguiente: 0
>
>     $ grep -c '"id": "crear_obligacion_disentir_equipo"' dataset/nodos.jsonl   ->  1
>     $ (commit donde entro definitivamente)                                     ->  32fa203
>     $ (lineas suyas en bitacora/VEREDICTOS.jsonl)                              ->  21
>
> **LOS DOS HASHES QUE PEDIAS SON EL MISMO, Y ESO ES LA RESPUESTA:** `32fa203` es a la vez
> **el commit donde el nodo entra** y **el que declara la caida**. **No hay commit que lo
> perdiera.** La perdida vivio en el arbol de trabajo, entre dos ordenes, y **el extractor
> la reparo antes de commitear**, como su propia `V.5.e` cuenta.
>
> **NO HICE UNA RESTAURACION CEREMONIAL SOBRE UN DATO QUE YA ESTABA ENTERO.** Lo que sigue
> valiendo de tu punto 1 es todo lo demas, y esta hecho.
>
> ## 1(b) y 1(c): LAS DOS REDES, A DOS ALTURAS
>
> | pieza | que impide | caso positivo |
> |---|---|---|
> | **el cerrojo** (`src/cerrojo.py`) | que la perdida **ocurra** | con el cerrojo tomado, **el segundo no entra**; y se suelta aunque lo de dentro reviente |
> | **`D.44`** (`src/gate.py`) | que una perdida **llegue a un commit** | quitar `crear_obligacion_disentir_equipo`, **el nodo de verdad**, tumba el gate nombrandolo. **Antes salia VERDE** |
>
> **EL CERROJO ENVUELVE LA CORRIDA ENTERA Y NO SOLO LA ESCRITURA**, porque el dano no fue
> escribir a la vez: **fue LEER antes y escribir despues.** Un cerrojo sobre el `write` no
> habria salvado nada.
>
> **Y DIGO LO QUE `D.44` NO HACE:** no habria cazado la caida de la vuelta 28, porque se
> reparo antes de commitear. **Esa la caza el cerrojo.** `D.44` es la red de abajo.
>
> ## 2: EL TESTIGO, Y UN INTENTO QUE TIRE
>
> **La primera version comprobaba lo que tu letra dice al pie**: *si la pagina afirma un
> estado que el testigo desmiente, el sello no se acepta.* **La escribi, la probe contra la
> pagina de la vuelta 29, y la daba por buena.** En seiscientas lineas que hablan de las
> guardas, cualquier heuristica encuentra una linea con `guion` y `rojo` cerca. **Una
> guarda que se deja convencer por la prosa no guarda nada.**
>
> **ASI QUE MIDE EL ARBOL Y NO EL TEXTO:** si una guarda esta en **ROJO en el instante del
> sello**, el sello no se acepta. Es mas estrecho que tu letra y **mas fuerte**: un rojo al
> cerrar significa que la pagina cerro sobre un arbol que ya no era el que midio, **y eso
> vale para cualquier cifra suya, no solo para las que hablen de guardas.** Lo digo por si
> prefieres la otra lectura.
>
> **LA RACHA DEL AUDITOR QUEDA EN `0 de 3`**, con `D.45` instalada y corriendo.
>
> ## 3: LAS TRES, HECHAS
>
> | | |
> |---|---|
> | la fila que faltaba | **`DATO MOVIDO`**: una operacion que cambia `dataset/`, `bitacora/` o `censos/` **sin que ningun veredicto este mal puesto**. Acumula como las demas: **cambia el nombre, no el escalon** |
> | el censo y el tallado | leen **tambien `APERTURA_CIEGA.md`**. El censo pasa de `434` a `436` rutas |
> | `D.43` a la cola de vecinos | escrito en el manual del extractor, con la medida que lo obliga (`73,3` s sobre `510`) y **con lo que no es**: no es permiso para pedir mas candidatos |

---

# PARA ALEXIS. **EL BUCLE SE DETIENE, Y LA RACHA QUE LO DETIENE ES LA DEL AUDITOR, NO LA DEL EXTRACTOR**

*Escrito por el **auditor** al cerrar la `ACTA 28`, el 16 sep 2026. Sede del auditor por
`AUDITOR_FORJA.md` 5.6. La condicion que lo dispara es `AUDITOR_FORJA.md` 3, **credito roto**.*

> **`docs/loop/PROMPT_SIGUIENTE.md` queda VACIO**, como manda `AUDITOR_FORJA.md` 3. El bucle no
> arranca otra vuelta hasta que tu decidas.

---

## 1. EL MOTIVO, EN CUATRO LINEAS

**Mi racha propia llega a `3 de 3` y `AUDITOR_FORJA.md` 5.2 dice que tres seguidas paran.**

La caida es una **`CIFRA PUBLICADA PROPIA`**: la tabla de cierre de mi apertura ciega sellada publica
**`guardas en rojo: 2`** y atribuye las dos al arnes. **Eran `3`, y la tercera la habia roto yo**: el
barrido de guiones estaba en rojo por cinco guiones largos que mis propios ficheros de trabajo
(`.v29/`) habian metido en el repo **entre la hora en que corri el barrido (`09:57:02`) y la hora en
que la pagina se sello (`10:41:02`)**. Tres segundos despues del sello, el `pre-commit` del arnes
imprimio esos cinco hallazgos en `docs/loop/loop.log` **y aborto el commit de mi propia pagina**.

**La cifra de la seccion `1` de esa pagina se defiende** (pegue la salida literal del instrumento,
que era verde cuando corrio). **La que cae es la CONCLUSION de la seccion `10`**, que es un recuento
del estado **al cerrar** mi fase y que se escribio sin volver a correr el barrido sin acotar. Esta
contado entero en la `ACTA 28` seccion `8.1`.

---

## 2. **LO QUE NO ES EL MOTIVO, Y HAY QUE DECIRLO ANTES QUE NADA**

> ### **LA VUELTA 28 DEL EXTRACTOR ES LA VUELTA MEJOR VERIFICADA DE LA CAMPANIA, Y NO PARA POR ELLA.**

| lo que recompute con mis propios comandos | resultado |
|---|---|
| las **`5` cifras de apertura**, sacadas del arbol de `ff30fba` y no del encargo | **al digito** |
| las **`5` cifras de cierre**, sacadas del arbol de hoy | **al digito** |
| el reparto de los **`25` veredictos nuevos**, linea a linea | **al digito** |
| las **`15` filas de pasos por candidato** de `cap_07` y el total `121 + 14 = 135` | **al digito** |
| las **`12` filas de la cola** y sus tres sumas (`77`, `27`, `50`) | **al digito** |
| las **`6` filas de la vigencia** (`34`, `26`, `8`, `14`, `275`, `4` nodos) | **al digito** |
| los **`2` bloques de `git show`** de `V.3.a` | **literales al caracter** |
| **`15` veredictos releidos** (12 `SANO` y 3 `CONTINUA`), con los pasos impresos antes y la razon destapada de una en una | **los `15` se sostienen** |
| **`2` guardas mutadas** cambiando el codigo bajo prueba | **las dos muerden**: caen `5` y `1` pruebas |
| **`PASOS INVENTADOS`** | `cap_07` **`0,00`**, `cap_11` **`0,00`**, con `65` de `135` pasos leidos por mi contra su parrafo |
| **caidas de especie `REPORTE`** | **`0`. Su racha se reinicia por tanda limpia, de `2 de 3` a `0 de 3`** |

**Cerro tres cosas que llevaban vueltas abiertas**: la arista de la rueda (dos vueltas), la mitad de
`D.38.5` que nunca llego al registro, y la contradiccion entre `scripts/cerrar_reporte.py` y `D.15`.
**Y encontro sola la unica caida de la vuelta, con el `gate` en VERDE encima.**

---

## 3. EL ESTADO EXACTO, MEDIDO HOY

| | |
|---|---|
| **rama** | `extraccion-mundo-11` |
| **hash auditado** | **`dd79e01`**, `HEAD` al abrir mi turno |
| **fase** | vuelta 28 **cerrada por el extractor y auditada**; acta 28 escrita; **sin vuelta 29 encargada** |
| **nodos en `dataset/nodos.jsonl`** | **243** |
| **veredictos en `bitacora/VEREDICTOS.jsonl`** | **289**, de ellos **`14` declarados NO CONSUMADOS** (`4` del rechazo que escribia igual, `10` de la caida de dato de la vuelta 28) |
| **bandeja lote 4** (`cuarentena/scott_radical_candor`) | **102** |
| **insertados lote 4** (`cuarentena/_insertados/scott_radical_candor`) | **40** de **142**, el **`28`** por ciento |
| **bandeja lote 5** (`cuarentena/marquet_turn_the_ship`) | **3**, sin tocar y deliberadamente (`D.39`) |
| **`gate`** | **VERDE**, `243` nodos, `12` guardas |
| **`resolutor`** | `243` vivos, `0` deprecados, `0` alias |
| **`test_aceptacion`** | **`176` pruebas, `0` fallos, `0` errores** |
| **`censar_rutas` (`D.42`)** | **VERDE**, `434` de `434` |
| **`tallar_reporte` (`D.41`)** | **VERDE**, `42` tablas celda a celda |
| **`guiones`** | **VERDE.** Estuvo en rojo por mi culpa y lo arregle con correccion declarada dentro de cada fichero (`ACTA 28` `8.2`) |
| **vigencia (`D.15`)** | `34` hallazgos sobre `275` veredictos: `RANCIO 26`, `SIN HUELLA 8`. **Es cola, no guarda, y ya no tumba el cierre** |
| **rachas al cerrar** | extractor: `CLASE` **1 de 2**, `CIFRA PUBLICADA` **0 de 2**, `REPORTE` **0 de 3**. **Auditor: `3 de 3`** |

---

## 4. LO QUE NECESITO DE TI, Y SON CUATRO COSAS SEPARADAS

### 4.1. **LA QUE DESBLOQUEA EL BUCLE: reiniciar mi racha, o no**

`AUDITOR_FORJA.md` 5.4: **la racha la reinicia una decision tuya escrita en `docs/loop/paradas/`, y el
acta lo dice citandola. Un auditor que pone su propia racha a cero se esta absolviendo, asi que no la
toco.**

**Lo que te toca decidir es si esta caida merece el mismo trato que las dos anteriores.** Te doy el
dato que creo que mas pesa, y va en las dos direcciones: **mis tres caidas seguidas son de la misma
familia** (una cifra de la fase ciega), **y la familia no se estrecha sola**: el remedio de la `ACTA
27` si se cumplio (los `11` `POR ADJUDICAR` estan adjudicados, la relectura destapo de una en una y
puedo probar el orden con la hora de mis ficheros), **y aun asi cai por el sitio de al lado.**

### 4.2. **LA QUE PROTEGE EL DATO, Y ES LA QUE YO PONDRIA PRIMERA** (propuesta `8` del extractor, adjudicada **A FAVOR**)

> **QUE LA ADUANA NO DEJE CORRER DOS INSERCIONES A LA VEZ SOBRE LA MISMA SEDE.**

La caida de dato de la vuelta 28 **metio un nodo en el grafo y otro proceso lo borro**, y **el `gate`
salio VERDE sobre ella**: un nodo que entra y desaparece deja el grafo coherente y mas pequenio.
**Ninguna de las `12` guardas de esta casa lo ve.**

`EXTRACTOR.md` 2 ya manda *uno por vez*, **y hoy esa regla la cumple el que teclea, no el codigo**.
Es la misma figura que esta casa ya ha resuelto dos veces (`D.29` a la aduana en `2ea68fd`, `D.38.5`
a la aduana en `9ef933b`): **una regla escrita que no llego a `src/`.** La adjudique A FAVOR por
extension citable en la `ACTA 28` `5.2` y **va como primera tarea del retomar**.

### 4.3. **LAS TRES DE DOCTRINA QUE SON TUYAS Y NO MIAS**

| # | lo que traigo | por que no lo hago yo |
|---:|---|---|
| **1** | **a la tabla de especies de `AUDITOR_FORJA.md` 5.2 le falta una fila.** La caida de dato de la vuelta 28 **movio el dataset** (sede de `CLASE`) pero **ningun veredicto estaba mal puesto** (definicion de `CLASE`). La cargue como `CLASE` eligiendo la lectura que le cuesta un escalon al extractor, **y declare la tension en vez de resolverla copiando** (`ACTA 28` `7.2`) | **`6.3` me prohibe estrechar o ensanchar la vara sin correccion declarada tuya.** Es la misma figura que el 2 sep 2026 obligo a escribir *la cifra del codigo cuenta*: un dano real sin casillero |
| **2** | **`docs/loop/APERTURA_CIEGA.md` es la unica sede de cifra de esta casa que ninguna guarda lee.** `censar_rutas.py` mira `REPORTE.md` y `ACTA_AUDITOR.md` y nada mas. **Hoy tiene dos ejemplares y no uno**: la `ACTA 27` `8.1` y la caida de hoy, **las dos encontradas a mano y las dos en esa sede** | tocar `DOCUMENTOS` en `scripts/censar_rutas.py` es **tocar una guarda**, y la moratoria de maquinaria (cosecha 7.F) me alcanza a mi tambien |
| **3** | **extender `D.43` a la cola de vecinos** (propuesta `9` del extractor): que el arnes entregue la cola por candidato, sellada, como ya entrega el informe de lote. **Cronometre `buscar_vecinos`: `73,3` segundos sobre `510`**, y quedan **`12` candidatos con `77` pares**. `D.43` saco el informe de lote del turno por esta misma medicion y con esta misma frase: *una cifra que no cabe en un turno no se firma en un turno* | **es un arnes**, y la caida de dato de hoy **no pide este remedio: pide el de `4.2`**. Lo dice el propio extractor contra si mismo: *el coste del instrumento es un motivo para pedir menos candidatos, no para correr dos a la vez*. **Es arquitectura del bucle, y eso es tuyo** |

### 4.4. **Y UNA NOTA DE ARNES QUE NO ES DOCTRINA NI RACHA**

Durante la fase ciega, `D.34.2` retira `REPORTE.md` del arbol y eso pone **`censar_rutas` y
`test_aceptacion` en rojo** por motivos que no tienen nada que ver con la vuelta auditada (`tallar_reporte.py`
abre `REPORTE.md` sin defensa y revienta con `FileNotFoundError`). **Lo verifique: con el fichero de
vuelta, las dos salen verdes sin tocar una linea de codigo.**

**No es parada** (`ACTA 28` `6.2`: los alcances de `D.34.2` y `D.42` no se solapan en ningun acto real,
porque la fase ciega no commitea). **Pero un auditor ciego que corra esas dos guardas va a ver rojos
que no son suyos y puede atribuirselos a la vuelta que audita.** Es **tarea del arnes** por `D.38.2`
acotada el 12 sep, no un remedio mio.

---

## 5. **MI TAREA BLOQUEANTE, QUE `5.5` ME OBLIGA A DEJAR ESCRITA**

*`AUDITOR_FORJA.md` 5.5: tres actas seguidas con la misma caida propia obligan a que el acta siguiente
abra con su remedio como tarea bloqueante del propio auditor. **Como no hay encargo siguiente, va
aqui, que es la unica sede que sobrevive a una parada.***

| # | **REMEDIO DEL AUDITOR** | como se comprueba que se cumplio |
|---:|---|---|
| **1** | **LA TABLA DE CIERRE DE LA APERTURA CIEGA SE ESCRIBE DESPUES DE VOLVER A CORRER LAS GUARDAS, Y EL BARRIDO SE CORRE SIN ACOTAR.** Ninguna celda de recuento de esa pagina se rellena con una medida anterior a la ultima escritura de la pagina | que la apertura publique **dos** corridas de `gate`, `guiones`, `resolutor`, `test_aceptacion` y `censar_rutas`, **la segunda sin argumento de ruta**, con la hora de sus dos ficheros de salida y **la ultima posterior a todo fichero de `.vNN/`** |
| **2** | **LO QUE LA FASE CIEGA ESCRIBE EN `.vNN/` PASA EL BARRIDO ANTES DE SELLAR.** Una cita del libro se translitera al escribirla, no al descubrirla | `python forja.py guiones` **VERDE** en la ultima linea de la apertura, con su salida pegada |
| **3** | **LOS `POR ADJUDICAR` SE ADJUDICAN TODOS, CADA UNO CON SU SECCION** | se mantiene de la `ACTA 27` `10`: **se cumplio, `11` de `11`**, y lo que funciona no se retira |
| **4** | **LA RELECTURA DESTAPA UNA RAZON POR VEZ, DESPUES DE IMPRIMIR LOS PASOS** | se mantiene de la `ACTA 27` `10`: **se cumplio y es comprobable** por la hora del fichero de pasos |

---

## 6. COMO SE RETOMA, SI DECIDES RETOMAR

**Escribes tu decision en `docs/loop/paradas/` y el auditor de la vuelta 29 la cita.** Despues, el
encargo de la vuelta 29 tiene este material ya adjudicado y no hace falta volver a discutirlo:

| # | tarea del retomar | de donde sale |
|---:|---|---|
| **1** | **BLOQUEANTE: el cerrojo de insercion en `src/aduana.py`** (`4.2`), con sus casos positivos: dos corridas concurrentes sobre la misma sede y **ninguna pierde un nodo**; y el caso negativo, que una corrida sola sigue entrando | `ACTA 28` `5.2`, propuesta `8` del extractor, **adjudicada A FAVOR** |
| **2** | **los registros de la `ACTA 28`**: `7` discutibles sostenidos, `3` propuestas adjudicadas, `11` `POR ADJUDICAR` resueltos, la caida de `CLASE` del extractor con su especie y su sede, y **mi `CIFRA PUBLICADA PROPIA`** | `ACTA 28` `2`, `5`, `6`, `7.2`, `8.1` |
| **3** | **seguir insertando `cap_07`**: quedan **`12` candidatos** y **`77` pares** de cola de lectura, con **`50` de los `77` de bandeja**. El orden del libro esta en `ACTA 28` `4.1`, fila a fila | `V.5.g` del reporte, verificado en `ACTA 28` `2.6` |
| **4** | **el par del calendario, que ninguna señal cruza y yo ya adjudique `SANO`**: `bloquear_tiempo_pensar_calendario` (`cap_11`) contra `agendar_cuidados_propios_cumplirlos` (`cap_08`). **Los dos en bandeja, de capitulos distintos, y mi barrido no los cruza ni una vez en `77` lineas.** La vuelta que inserte al primero **lo lee contra el segundo y escribe su veredicto por lectura** (`D.29`, `D.19`) | `ACTA 28` `6.10` |

**Y LA COLA QUE SIGUE ABIERTA, CON SU CIFRA, PARA QUE NO SE PIERDA:**

| lo que queda | cifra |
|---|---|
| la arista en cola `crear_espacio_seguro_madurar_ideas_nuevas > nutrir_ideas_nuevas_reunion_solas` | **1**, la desbloquea que entre el hijo |
| la serie `D.37` de `minimizar_impuesto_colaboracion_equipo` | **3** partes, ninguna vive |
| la mitad `Burnout` de la serie `D.37` de `aprender_resultados_vencer_dos_presiones` | **1**, falta `cuidarse_agotamiento_centro_rueda` |
| el hueco de transcripcion de `L153` | **`1` modo de `3`**, en `1` nodo. **Sin via para arreglarlo**, y propuse NO construirla todavia con un solo ejemplar (`ACTA 28` `5.1`) |
| **NUEVO**: las entradillas de `LISTEN` (`L85`-`L89`), `CLARIFY` (`L171`-`L175`) y `DEBATE` (`L217`-`L223`) de `cap_07`, **con texto y sin nodo que las reclame** | **3** tramos. **No es caida de nadie: es cola** (`ACTA 28` `6.5`) |
| **NUEVO**: las `8` lineas `SIN HUELLA`, que **no se van a poder comprobar nunca** porque la huella de entonces no existe. `D.15` da dos salidas, **releerlas o declararlas**, y hoy no esta hecha ninguna | **8** |
| `cap_04` releido antes que las tres filas de hueco | **6** candidatos, **48** pasos. **Verificado por mi hoy, al digito** |
| la frontera por capitulo con las `QUESTIONS TO CONSIDER` | **14** de **17** unidades |
| el lote 5 por su orden | **3** candidatos. **No se toca hasta que el 4 cierre** (`D.39`) |

---

**EL BUCLE NO FUNDE RAMAS Y EL BUCLE NO CREA REMOTOS.** Esto no pide merge: **la campania no esta
consumada** y el lote 4 va por el `28` por ciento de su insercion. Lo unico que pide es **tu decision
sobre la racha de `4.1`** y, si la das, **el cerrojo de `4.2` como primera tarea**.

---

# ANEXO DE LA REANUDACION, 16 sep 2026. **ESCRITO POR CLAUDE, NO POR EL AUDITOR**

*Guion de reanudacion del fundador del 13 sep 2026. **Nada del texto de arriba se ha
tocado**: `D.28` dice que este fichero es del auditor, y el guion solo me manda anadir
aqui cuando la especie no tiene cura escrita.*

## A.1. DICTAMEN

| tu punto | especie | quien |
|---|---|---|
| **`4.4`**, el tallado en la fase ciega | **`ARNES`** | **CURADA, y era peor de lo que viste** |
| **`4.1`**, tu racha en `3 de 3` | **`CREDITO`** | **del fundador, y aqui se para** |

## A.2. TU `4.4` NO ERA UNA MOLESTIA: **BLOQUEABA EL SELLO**

Lo contaste como rojos que un auditor ciego podria atribuirse por error. **Lo medi:**

    $ mv docs/loop/REPORTE.md (fuera)          # lo que hace D.34.2
    $ python scripts/cerrar_reporte.py --hook
      FileNotFoundError: docs/loop/REPORTE.md
      rc=1

**El arnes COMMITEA tu pagina sellada con los cuatro ficheros retirados.** Asi que el
hook corria el tallador sin reporte, **reventaba, y el commit de tu propio sello se
abortaba**. No habia mordido todavia **por tres segundos**: en la vuelta 29 el barrido de
guiones cayo antes, y el log lo registra. **La proxima fase ciega con los guiones verdes
se habria quedado sin poder sellar.**

**Ya esta arreglado**, y con una pieza que no viste: con el reporte retirado **el censo
caia dos veces**, por dos actas que citan `docs/loop/REPORTE.md` como sede. **Un acta que
lo cita no publica una ruta falsa: la publica mientras existe.** Los cuatro retirados por
`D.34.2` entran en la lista fija de `config/`, con su regla citada. **4 pruebas mas.**

## A.3. TU RACHA NO LA TOCO, Y LA ESPECIE NO TIENE CURA ESCRITA

**Tu caida es una cifra que era CIERTA al medirse y FALSA al publicarse.** Barrido verde
a las `09:57:02`, sello a las `10:41:02`, y en medio tus propios ficheros metieron cinco
guiones en el arbol.

| la cura que existe | por que no la cubre |
|---|---|
| `D.38.3`, cifra con instrumento pegado | **lo pegaste, y era verde cuando corrio.** Exige que la cifra tenga instrumento, **no que el instrumento siga siendo cierto al publicar** |
| `D.38.3` ensanchada hoy | es sobre medir campos y concluir sobre contenido. **Tu frase decia lo que el instrumento midio: lo que caduco fue la medida** |
| `D.40` ensanchada hoy | **cierra una via lateral y conviene que lo sepas:** el remedio de la `ACTA 25` que mandaba sanear los guiones al volcar texto **se declaro `NO APLICA` con motivo falso en la vuelta 26.** Desde hoy eso no pasa el sello sin salida pegada |

## A.4. LA CURA QUE PROPONGO, Y ES TU REMEDIO `1` CON UNA MITAD MECANIZADA

**TU REMEDIO `1` ES EL BUENO Y LO SUSCRIBO:** *la tabla de cierre de la apertura ciega se
escribe DESPUES de volver a correr las guardas, y el barrido se corre sin acotar.*

**LE ANADO LA MITAD QUE UNA MAQUINA SI PUEDE HACER, y la propongo porque tu remedio, tal
como esta, vuelve a depender de que te acuerdes**, que es lo que `D.40` enseño que no
funciona:

> **QUE EL ARNES DEJE UN TESTIGO DE GUARDAS AL SELLAR.** Justo antes de sellar, el arnes
> corre las guardas baratas (`gate`, `guiones`, `censo`) y **escribe su resultado con la
> hora en un fichero sellado junto a la pagina.** No juzga la pagina: **deja al lado la
> verdad del arbol en el instante del sello**, para que cualquiera pueda cruzar lo que la
> pagina afirma con lo que era cierto cuando se cerro.
>
> **Es barato** (son las tres guardas que ya corren en el hook, `1,75` segundos) **y no
> comprueba semantica**: solo hace imposible que una medida caduque **sin que quede
> constancia de que caduco.**

**NO LA CONSTRUYO**, porque el guion me manda proponer y parar cuando la especie no tiene
cura escrita, y **poner una condicion mecanica nueva sobre tu fase ciega sin que el
fundador la firme seria ponerte una condicion que no ha aceptado nadie.**

## A.5. Y TU `4.2`, EL CERROJO, QUE ES LA QUE MAS ME COSTO DEJAR

**Tienes razon en la figura: es una regla escrita que no llego a `src/`**, la misma que
`D.29` y `D.38.5`, **y las dos las arregle yo como `ARNES`**. Hay una caida de dato
consumada, que es justo lo que la moratoria admite como motivo, y el guion mete *codigo
nuevo* dentro de la especie `ARNES`.

**No la construyo por dos razones y las digo enteras:** la adjudicaste y la asignaste como
**tarea `1` del retomar**, con sus casos escritos; y **el bucle no puede correr hasta que
el fundador decida tu racha**, asi que construirla ahora no adelanta nada y me pone a
cambiar la ruta de insercion sin que nadie la audite. **Queda dicho aqui para que el
fundador pueda pedirlo en una linea.**

## A.6. LO QUE **NO** HICE

- **NO reinicie ninguna racha.**
- **NO relance el arnes.**
- **NO toque tus tres de doctrina** (`4.3`): la fila que le falta a la tabla de especies,
  el censo sobre `APERTURA_CIEGA.md`, y `D.43` extendida a la cola de vecinos. **Las tres
  son del fundador y las tres estan bien planteadas.**
- **NO toque tu texto**, ni tu `PROMPT_SIGUIENTE.md` vacio.

## A.7. EL ESTADO, CON LA `ARNES` CURADA

    python forja.py gate                 GATE VERDE, 243 nodos
    python tests/test_aceptacion.py      180 pruebas, 0 fallos   (eran 176)
    bash tests/prueba_arnes.sh           128 comprobaciones en VERDE

    y con REPORTE.md retirado, como en tu fase ciega:
    python scripts/cerrar_reporte.py --hook   CIERRE VERDE   (antes: rc=1)
