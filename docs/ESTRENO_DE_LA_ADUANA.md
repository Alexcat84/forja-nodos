# EL ESTRENO DE LA ADUANA, EN SECO

**9 sep 2026.** Primera vez que la aduana de la forja mira un lote entero por su
puerta real. **Cero inserciones**, y esta probado mas abajo con huellas.

    python forja.py informe --carpeta cuarentena/<lote>

---

## 1. LOS 167 DEL MUNDO 11 NO SON CANDIDATOS: SON LIBRO CRUDO

El encargo decia *"el mundo 11 son 167 candidatos ya extraidos: van a la bandeja
(b)"*. Se fue a buscarlos antes de correr nada. **No existen como candidatos.**

Lo que hay en `c:/Users/AlexDesk/Documents/OCR/fuentes/`, contado (el mundo 11 y
su hermano el mundo 10, que se encontro despues y va en 1.1):

| | |
|---|---:|
| recortes de capitulo en markdown, de diez libros | **163** |
| insumos auxiliares del apendice de Bananas | 2 |
| documentos del propio recorte (MANIFIESTO, INDICE_REAL, CENSO_DE_CUERPOS, LISTADO_ARCHIVOS_AUDITORIA) | 4 |
| **ficheros JSON de nodo** | **0** |
| ficheros de la carpeta hermana `mundo_10_reservado/` (ver 1.1) | 1 |
| ficheros con el campo `pasos_accionables` en cualquier formato | **0** |

Los diez libros: `bernerslee_bananas` (21), `gerber_emyth` (22),
`grove_high_output` (18), `marquet_turn_the_ship` (17), `onu_consumidor` (4),
`openstax_business_ethics` (17), `openstax_org_behavior` (32),
`scott_radical_candor` (15), `smart_who` (7), `zhuo_manager` (12).

Su propio `MANIFIESTO.md` lo dice: es **"este proyecto de recorte y
verificacion"**, cerrado y verificado contra los PDF de origen. **Recortar un
libro no es extraer un nodo.** El trabajo esta hecho y esta bien hecho, pero es
**BANDEJA (a)**, libro crudo listo para que el extractor lo lea.

**LA CONSECUENCIA, dicha sin adorno: la primera insercion real todavia no tiene
material que autorizar.** Lo que falta entre esos 163 recortes y la bandeja (b)
es una vuelta de extraccion, que es exactamente el trabajo que
`docs/loop/EXTRACTOR.md` acaba de dejar escrito.

**DONDE VAN CUANDO EXISTAN, y con que se leen** (ruta exacta, que era lo pedido):

    cuarentena/mundo_11/<id_propuesto>.json
    python forja.py informe --carpeta cuarentena/mundo_11

### 1.1. EL MUNDO 10, QUE ESTABA AL LADO Y NO SE MIRO

**AÑADIDO EL MISMO 9 sep 2026, a pregunta del fundador.** El primer barrido
busco `mundo_11` por su nombre y luego `*mundo*` a cuatro niveles desde
`Documents`, que **no alcanza a los hermanos de `OCR/fuentes/`**. Habia otro:

    OCR/fuentes/mundo_10_reservado/gerber_emyth/17_cap_17_your_marketing_strategy.md

**UN SOLO FICHERO.** El capitulo 17 de Gerber, verbatim, 3.845 palabras, con su
cabecera de edicion y su ISBN. Y **no es un olvido de nadie: esta apartado a
proposito.** El `CENSO_DE_CUERPOS.md` del mundo 11 lo registra en su tabla,
`(a mundo_10_reservado)`, el `INDICE_REAL.md` dice que es *"exactamente el titulo
a apartar para mundo_10_reservado"*, y el `MANIFIESTO.md` da su ruta de destino.
**La prueba mas limpia esta en la numeracion del propio recorte:** en
`mundo_11/gerber_emyth/` la serie salta de `17_cap_15` a `18_cap_16` a
`19_cap_18`. **El 17 no falta: se fue.**

**NO CAMBIA NADA DE LO ANTERIOR, y por eso lo refuerza:** tambien es BANDEJA (a).
En **todo** `OCR/fuentes/`, los dos mundos juntos, hay **170 ficheros y CERO
ficheros JSON de nodo**. El arbol entero es libro crudo por construccion.

**Y DE PASO EXPLICA EL 167 DEL ENCARGO, que es aritmetica exacta y no una cifra
aproximada:**

| | |
|---|---:|
| recortes de capitulo de `mundo_11/` | 163 |
| documentos del propio recorte (MANIFIESTO, INDICE_REAL, CENSO_DE_CUERPOS, LISTADO_ARCHIVOS_AUDITORIA) | 4 |
| **suma** | **167** |
| insumos auxiliares del apendice, que quedan fuera de esa cuenta | 2 |
| **ficheros de `mundo_11/`, todos** | **169** |

**LOS 167 SON EL RECUENTO DE FICHEROS DE LA CARPETA**, no un recuento de
candidatos. La cifra del encargo era correcta; lo que nombraba era otra cosa.

---

## 2. ENTONCES EL ESTRENO SE CORRIO IGUAL, ROTULADO

Correr la aduana por primera vez sobre un lote entero **no depende del mundo
11**, y la pieza que el encargo pedia probar es la aduana, no el mundo 11. Asi
que se estreno a la misma escala con material rotulado:

| | |
|---|---|
| lote | `cuarentena/ensayo_referencia_163/` |
| que son | **163 nodos VIVOS del catalogo limpio de referencia**, tag `catalogo-limpio-v1`, commit `1b128323` |
| cuantos | **163**, la escala exacta de los recortes del mundo 11 |
| semilla | `20260909`, escrita en `calibracion/preparar_ensayo.py` |
| **lo que NO es** | **NO es el mundo 11**, y lo dice el nombre de la carpeta, su `LEEME.md` y la cabecera del preparador |

**POR QUE ESE MATERIAL Y NO OTRO.** Son nodos auditados por humanos, con la
forma exacta que la aduana espera. Miden lo unico que un estreno puede medir
antes de que exista extraccion propia: **como se comporta el instrumento con un
lote entero delante.**

**LO QUE ESTE ENSAYO NO MIDE, y se dice para que nadie lo cite de mas:** no mide
la calidad de la extraccion del mundo 11, porque esa extraccion no se ha hecho.

La tabla de fuentes se derivo del catalogo y se paso por `FORJA_FUENTES`, porque
esos libros todavia no estan en `fuentes/FUENTES_CANONICAS.json`. Sin eso los 163
caerian por la guarda `fuentes` y el informe seria ruido, no medida.

---

## 3. EL SALDO

**Salida entera en `calibracion/SALIDA_ESTRENO.txt`, 452 lineas, candidato por
candidato.**

| | | |
|---|---:|---|
| candidatos revisados | **163** | |
| nodos en el grafo de destino | **2** | el dataset real de la forja, hoy |
| **ENTRARIAN** sin leer nada | **114** | 69,9 por ciento |
| **BLOQUEARIAN** esperando veredicto | **0** | no es rechazo: es cola de lectura |
| **CAERIAN** por una guarda | **49** | 30,1 por ciento |
| **CHOCAN** entre si dentro del lote | **0** | ningun id repetido en 163 |

**POR QUE GUARDA CAEN LOS 49:**

| guarda | cuantos | desglose |
|---|---:|---|
| rompe `docs/REGLAS_DE_ID.md` | **45** | 35 preposicion o articulo, 6 palabra fuera del castellano, 5 sufijo numerico (algunos acumulan) |
| guiones prohibidos en el texto | **4** | `estrategia_multicanal_bienvenida`, `metas_vs_proposito`, `restricciones_extremas_como_innovacion`, `sistemas_alta_confiabilidad_hro` |

**NINGUNA DE LAS DOS ES UNA GUARDA DE CALIBRACION.** Son reglas de esta casa
(`docs/REGLAS_DE_ID.md` y D.12), deliberadamente **mas estrictas** que las que
aquella campaña aplico. Que el 30 por ciento de un catalogo auditado caiga por
ellas **no dice que la aduana este mal calibrada: dice que esta casa pide mas.**
La prueba de calibracion es otra y ya paso: **cero** de los 163 cayo por una
señal, por un umbral, ni por el esquema.

**LOS 0 BLOQUEOS SON UN ARTEFACTO DEL GRAFO VACIO, no un merito.** Con dos nodos
de destino no hay con quien parecerse. La cifra que importa al fundador es la
otra: cuanta lectura cuesta el mismo lote cuando el grafo esta lleno. Va en la
seccion 5.

---

## 4. CERO INSERCIONES, PROBADO CON HUELLA

*La ruta que promete prueba es cifra (cosecha 7.C): una promesa de que no se
escribio nada se comprueba, no se firma.*

Huella `sha256` de **todas** las sedes de escritura, antes y despues de la
corrida:

    dataset/nodos.jsonl        5036693b1b7a9518...  IDENTICA
    bitacora/VEREDICTOS.jsonl  eca458894984b54b...  IDENTICA
    censos/atribuciones.md     0e021a532d2b0438...  IDENTICA
    censos/casos.md            91b7ec1df6fc36b9...  IDENTICA
    censos/denominaciones.md   de5d1c959d820d4a...  IDENTICA
    censos/herramientas.md     9cf30c0ca2e2694c...  IDENTICA
    censos/marco_pais.md       35a55fef9cde9607...  IDENTICA
    censos/series_y_cabezas.md 70299df7cb2a94c5...  IDENTICA
    censos/vigencia.md         45bd36eb2692d83f...  IDENTICA

`config/pares_mutuos.jsonl` no existe ni antes ni despues: **el modo informe no
lo crea**, que es justamente lo que habria que vigilar.

**LAS NUEVE IDENTICAS.** El modo informe no escribio ni un byte.

---

## 5. CUANTA LECTURA COSTARA CUANDO EL GRAFO ESTE LLENO

Los **0 bloqueos** de la seccion 3 son ciertos y **no valen para planificar**:
con dos nodos de destino no hay con quien parecerse. Asi que se midio
**directamente** lo otro: los mismos candidatos contra **3.157 vivos** del
catalogo limpio, cada uno retirado de su propio destino para que no se encuentre
a si mismo. Salida en `calibracion/SALIDA_COLA_LOTE.txt`.

**12 candidatos del lote, 1.081 segundos de medida.**

    accion_correctiva_2                         0 vecinos  [CAERIA]
    butterfly_test_convergencia                 2 vecinos  [BLOQUEARIA]
    consejo_calidad_informacion                17 vecinos  [BLOQUEARIA]
    customer_retention_tactics                  2 vecinos  [BLOQUEARIA]
    diamante_decision_tres_partes               0 vecinos  [ENTRARIA]
    enfoque_proyecto_por_proyecto               0 vecinos  [CAERIA]
    fuentes_contratacion_ejecutivos             1 vecinos  [BLOQUEARIA]
    just_in_time_manufacturing                 10 vecinos  [BLOQUEARIA]
    medicion_resultados_marketing_franquicia    7 vecinos  [BLOQUEARIA]
    no_jugar_con_probabilidades                 0 vecinos  [CAERIA]
    programa_proteccion_denunciantes            2 vecinos  [BLOQUEARIA]
    second_wind_energia_mental                  0 vecinos  [ENTRARIA]

**LOS TRES CEROS DE LOS `CAERIA` NO SON MEDIDA, SON CORTOCIRCUITO**, y decirlo
cambia la cifra: `informe.revisar_candidato` devuelve el dictamen **antes** de
llamar a `buscar_vecinos` cuando una guarda rechaza. Un candidato que cae nunca
llega a las señales. **El denominador honesto son los NUEVE que si llegaron.**

| sobre los 9 que llegaron a las señales | |
|---|---:|
| vecinos totales levantados | **41** |
| **media por candidato** | **4,6** |
| mediana | **2** |
| maximo | **17** (`consejo_calidad_informacion`) |
| candidatos con la cola vacia | **2 de 9** |

**CONTRA LA ESTIMACION ANALITICA DE `docs/CALIBRACION_D4.md`, que era 2,4 por
candidato:** la medida directa da **4,6**, casi el doble. **Manda la medida.** La
estimacion salia de la tasa de disparo sobre pares al azar, y un lote real no es
al azar: trae capitulos enteros del mismo tema, que es exactamente el caso que
`EXTRACTOR.md` seccion 12 avisa. **La estimacion era un suelo, no un centro.**

**LO QUE ESO PROYECTA SOBRE UN LOTE ENTERO, y es la cifra que hay que mirar
antes de abrir la puerta:**

| | |
|---|---:|
| candidatos de un lote | 163 |
| que llegan a las señales (al 69,9 por ciento del estreno) | ~114 |
| **veredictos que habria que escribir** | **~520** |

**A tramos de cinco a quince por vuelta, un lote de 163 no es una sesion: son
decenas.** No es una averia de la aduana, es el precio de entrar en un grafo
grande, y **se sabe ANTES en vez de descubrirlo a la mitad**, que es justo para
lo que servia esta medida.

**Y NO SE PAGA ENTERO EL PRIMER DIA:** hoy la forja tiene 2 nodos, asi que el
primer lote entra casi sin cola. La cifra de 4,6 es el **estado estacionario**,
lo que costara cuando el grafo se parezca al de referencia. La cola crece con el
grafo, y por eso el orden de entrada importa (`EXTRACTOR.md` seccion 12: el
primero que entra cambia lo que el segundo mide).

---

## 6. LO QUE EL ESTRENO ENCONTRO EN EL PROPIO INSTRUMENTO

**Un estreno sirve para eso.** Encontro dos cosas: una se arreglo aqui mismo con
su prueba, la otra es doctrina y sube al fundador.

### 6.1. EL BARRIDO DE GUIONES ENTRABA EN LA BANDEJA. ARREGLADO

Al depositar el primer lote, **el pre-commit se puso en rojo**: el barrido
recorria el arbol entero y denunciaba los guiones largos de material AJENO que
todavia esperaba juicio (dos nodos del catalogo, con guiones que les puso su
editor).

**La averia barata era que tener un lote depositado rompe todos los commits.**
La grave era otra: **empuja a limpiar un candidato ANTES de que la aduana lo
mida**, y un candidato retocado para que el barrido calle es un candidato del
que ya no se sabe como llego. Eso es falsificar la medida en la puerta.

**LA LINEA QUEDA DONDE LA TRAZA `.gitignore`:** se barre la raiz de cada bandeja
(`cuarentena/LEEME.md`, `fuentes/FUENTES_CANONICAS.json`), que es doctrina de
esta casa; no sus subcarpetas, que son material de otro. **Se barre lo que esta
casa escribe, ni un fichero mas.**

**Y NO BARRER LA BANDEJA NO ES INDULTAR:** la guarda `guiones` del gate sigue
mordiendo candidato a candidato en la puerta, y en este mismo estreno mordio a
cuatro de los 163.

Escrito como **D.20** en `docs/BANCO_DE_REGLAS.md`. Implementado en
`comun.BANDEJAS_DE_ENTRADA`, con dos pruebas (`PruebaBandejas`): una para la
linea, y **su caso positivo** para que la puerta siga mordiendo.

### 6.2. UNA GUARDA QUE NO MUERDE. SUBE AL FUNDADOR

*La guarda que no muerde es cifra (cosecha 7.D).*

El estreno dejo pasar `variance_analysis`, `work_breakdown_structure`,
`butterfly_test_convergencia` y `brief_competitivo`. Y `wizard_of_oz_testing`
cayo, **pero solo por la palabra `of`**: `wizard`, `oz` y `testing` pasaron.

**EL MOTIVO, leido en el codigo:** la regla 1 de `docs/REGLAS_DE_ID.md` esta
implementada en `src/reglas_id.py` como `LEXICO_AJENO`, **una lista negra de 37
palabras**, cuya propia cabecera dice que es *"lexico ajeno al castellano que
aparece con mas frecuencia en esta forja"*. **No es una prueba de idioma: es un
diccionario corto.**

**LA CIFRA, contada a mano sobre los 3.169 vivos, sin heuristica y con cero
falsos positivos** (63 piezas verificadas una a una como ajenas al castellano):

| | |
|---|---:|
| ids vivos que llevan ingles que la lista NO caza | **269 de 3.169** |
| | **8,5 por ciento** |
| palabras en la lista vigente | **37** |

Las que mas pegan: `customer` (30), `marketing` (22), `benchmarking` (21),
`startup` (17), `business` (14), `management` (14), `lean` (13), `roadmap` (13),
`testing` (10), `getting` (10).

**SE INTENTO UNA MEDIDA MAS AMBICIOSA Y SE DESCARTO, y se dice:** un barrido por
ortografia imposible en castellano daba 1.045 de 3.169, pero marcaba `control`,
`estrategia` e `inspeccion` por sus grupos consonanticos. **Una cifra con falsos
positivos no es una cifra**, asi que vale solo la contada a mano, que es un
SUELO: el numero real esta por encima de 269, no por debajo.

**Y UN SEGUNDO AGUJERO, contado:** la regla 2 mira `_\d+$`, **solo el final del
id**. Una pieza puramente numerica en el MEDIO pasa entera. **14 ids vivos** la
llevan, y varios son legitimos (`iso_31000_gestion_riesgo`,
`los_14_puntos_deming`), lo que hace la decision menos obvia, no mas.

> **NO SE TOCA NINGUNA DE LAS DOS.** `docs/REGLAS_DE_ID.md` es doctrina de la
> casa y moverla es del fundador. Lo que corresponde aqui es lo que se ha hecho:
> **nombrar la guarda floja y ponerle su cifra.** Va a la seccion 7 como decision.

---

## 7. LAS DECISIONES QUE QUEDAN PARA EL FUNDADOR

**7.1. La regla 1 es una lista negra de 37 palabras y deja pasar al menos el 8,5
por ciento.** Tres salidas, y ninguna es obviamente la buena:

- **dejarla como esta** y aceptar que la regla 1 caza lo comun y no mas, con la
  cifra escrita para que nadie la crea completa;
- **engordar la lista** con las piezas medidas arriba, que sube la caza sin
  cambiar la naturaleza del instrumento;
- **cambiarla por una prueba de idioma de verdad**, que es maquinaria nueva y
  cae bajo la moratoria: solo por encargo expreso.

**7.2. La regla 2 solo mira el final del id.** 14 vivos llevan cifra en medio y
varios son legitimos. Si se extiende, hace falta decir que hace con `iso_31000`.

**7.3. El 30 por ciento de caida sobre catalogo auditado.** No es averia, es que
esta casa pide mas. Pero **si el mundo 11 se extrae con esa misma mano, tres de
cada diez candidatos caeran en la puerta.** O el extractor aprende las reglas de
id antes de escribir el primer id, que es lo barato y ya esta escrito en
`EXTRACTOR.md` seccion 12, o las reglas se relajan. **Lo caro es descubrirlo
candidato a candidato.**

**7.4. Si los lotes de cuarentena deben viajar en el repo.** Hoy `.gitignore` los
ignora. Ver la decision abierta al final de `cuarentena/LEEME.md`.

**7.5. Un lote de 163 en un grafo lleno cuesta unos 520 veredictos escritos.** No
es decision de la aduana, es aritmetica: 4,6 vecinos medidos por candidato que
llega a las señales. A tramos de cinco a quince por vuelta **son decenas de
sesiones**. Hoy no se paga, porque la forja tiene dos nodos; se pagara. Lo que el
fundador decide es si el mundo 11 entra **entero** o **por libros**, y en que
orden, porque el primero que entra cambia lo que el segundo mide. **La cifra esta
ahora y no a la mitad del lote, que es para lo que servia este estreno.**

---

## 8. COMO SE REPRODUCE ESTO ENTERO

    python calibracion/preparar_ensayo.py
    FORJA_FUENTES=cuarentena/_derivadas/FUENTES_DEL_ensayo_referencia_163.json python forja.py informe --carpeta cuarentena/ensayo_referencia_163
    python calibracion/cola_del_lote.py --cuantos 12

La carpeta `cuarentena/` esta ignorada por git: **el lote no viaja, la semilla
si.** Con la semilla escrita el lote se reconstruye identico.
