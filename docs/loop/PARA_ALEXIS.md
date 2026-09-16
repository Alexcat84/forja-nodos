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
