# PARADA DEL 10 SEP 2026: LOTE 1 CONSUMADO

> **DECISION DEL FUNDADOR (10 sep 2026): insercion autorizada y ejecutada en
> 762e31d, grafo de 2 a 8, D.30 firmada.**

> **ARCHIVADA.** Este fichero fue `docs/loop/PARA_ALEXIS.md` hasta que el fundador
> resolvio lo que pedia. **Se archiva entero y sin tocar una palabra de su
> cuerpo**, porque una parada resuelta sigue siendo el mejor registro de por que
> el bucle se detuvo y con que estado. Lo unico añadido es esta cabecera.
>
> **El bucle ya NO esta detenido por este fichero:** vive en `docs/loop/paradas/`
> y el arnes solo mira `docs/loop/PARA_ALEXIS.md`.

---


> **Escrito por el auditor del bucle del extractor, el 10 sep 2026, al cerrar la
> vuelta 2.** Sede del auditor (`AUDITOR_FORJA.md` 5.6, **`D.28`**). El extractor
> no escribe aqui.
>
> **EL BUCLE ESTA DETENIDO.** `docs/loop/PROMPT_SIGUIENTE.md` esta vacio, y este
> fichero existe: el arnes se detiene por cualquiera de las dos cosas.

---

## 1. EL MOTIVO: CAMPAÑA CONSUMADA. ES LA PARADA FELIZ

**El lote 1 de calibracion esta cerrado, y el bucle no tiene nada mas que pueda
hacer sin ti.** No es un tropiezo, no es un rojo y no es una contradiccion: es la
condicion de parada que `AUDITOR_FORJA.md` seccion 3 llama **campaña consumada**,
con el reporte final delante.

**Las tres cosas que lo cierran, medidas hoy y no supuestas:**

**1. El libro `onu_consumidor` esta resuelto entero, contando sus cuatro
ficheros uno a uno:**

| # | fichero | palabras | estado | candidatos |
|---|---|---:|---|---:|
| 1 | `cap_00.md` | 171 | **no minable**, es la portada de la que sale la ficha de la fuente | 0 |
| 2 | `cap_01.md` | 376 | **no minado por la marca** `FRONTERA` de su linea 9 | 0 |
| 3 | `cap_02.md` | 819 | **minado** en la vuelta 1 y **corregido** en la vuelta 2 | **6** |
| 4 | `cap_03.md` | 389 | **minado con resultado cero**: 0 procedimientos y 5 posturas | 0 |
| | **total** | **1755** | **ninguno en cola** | **6** |

**2. El bucle no puede insertar, y no es decision suya.** El arnes arranco con
`MODO_INSERCION=cuarentena`, que es el default, y **la insercion es una
autorizacion tuya, no un default** (`D.26`). Los seis candidatos estan escritos,
corregidos, medidos y en cuarentena. **Falta tu permiso, y solo eso.**

**3. El bucle no tiene material para el lote 2.** `D.24` dice que el siguiente es
`smart_who`, de 7 capitulos:

    ls fuentes/
      FUENTES_CANONICAS.json    onu_consumidor/

    .gitignore, bandeja (a):
      fuentes/*/     <- los libros crudos son texto con derechos y NO entran al repo

**`fuentes/smart_who/` no esta en el arbol y por diseño no puede llegar por git.**
Una vuelta 3 abriria el repo, buscaria su libro y escribiria que no lo hay.

---

## 2. EL ESTADO EXACTO

| | |
|---|---|
| rama | **`extraccion-mundo-11`** (el bucle no funde ramas) |
| hash auditado | **`54a20ee`**, mas el commit de esta acta encima |
| nodos en el dataset | **2** (`registrar_fuente_canonica`, `elegir_grafia_clave`), 0 deprecados, 0 alias |
| **inserciones en todo el bucle** | **CERO**, verificado con `git diff --stat 757870d..HEAD -- dataset/ bitacora/ censos/ config/`, que sale **vacio** |
| candidatos en cuarentena | **6**, en `cuarentena/onu_consumidor/`, con **32 pasos** en total |
| veredictos | **1**, de 2026-09-04, **anterior al bucle**. Las dos vueltas escribieron **cero** |
| fase | **lote 1 cerrado en cuarentena, esperando autorizacion de insercion** |
| gate | **VERDE**, 2 nodos verificados, 12 guardas |
| barrido de guiones | **VERDE** |
| prueba de aceptacion | **57 de 57, 0 fallos, 0 errores** |
| resolutor | **VERDE**: 2 vivos, 0 deprecados, 0 alias |
| credito | **CLASE 0, CIFRA PUBLICADA 0, REPORTE que acumula 0.** Ninguna racha rota |

**Las cuatro guardas estan corridas por mi en esta vuelta, no copiadas del
reporte.** Una salio en rojo al empezar y la deje en verde: esta contado en el
ACTA 2 seccion 1.1, y es el punto 5.1 de mas abajo.

---

## 3. LO QUE NECESITO DE TI, POR ORDEN

### 3.1. LA DECISION GRANDE: autorizar o no la insercion de los seis

**Los seis candidatos estan listos y medidos.** El informe de la aduana en seco,
corrido al cierre:

    python forja.py informe --carpeta cuarentena/onu_consumidor
      ENTRARIAN sin leer nada          : 6
      BLOQUEARIAN esperando veredicto  : 0
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0

**Y ese cero esta leido contra una puerta que muerde, mordida a proposito por mi
hoy** (ACTA 2 seccion 1.5): mutando la fuente de uno y vaciando los pasos de otro,
el mismo informe da **4 entrarian y 2 caerian**, con las dos guardas nombradas por
separado. **No es un cero de puerta abierta.**

**LO QUE TIENES QUE SABER ANTES DE DECIDIR, Y ES LO IMPORTANTE DE ESTA CAMPAÑA:**

> **13 de los 36 pasos del lote (el 36 por ciento) los habia escrito el extractor
> y no el libro.** Se cazaron en la vuelta 2, leyendo parrafo a parrafo, y se
> resolvieron: 4 pasos retirados enteros y 9 clausulas reescritas, cada una con su
> fichero, su linea y la frase que si esta en el texto. **El lote paso de 36 a 32
> pasos.**
>
> **Y la aduana dio 6 de 6 verdes ANTES y DESPUES de esa correccion.** Es decir:
> **ninguna guarda de esta casa ve esa especie de defecto.** Lo cazo una lectura
> con el libro delante, y nada mas.

**Si autorizas, el orden importa y esta medido:**

    formular_codigo_comercializacion_empresarial    (parrafo 31)   MADRE
        baja a
    verificar_afirmaciones_ambientales_publicidad   (parrafo 30)   HIJO

**LA MADRE ENTRA PRIMERO.** Si entra antes el hijo, en el momento de su veredicto
no hay madre en el grafo contra la que declarar la arista, y habria que cablearla
despues a mano en una sede que solo escribe la aduana.

**Y ESA ARISTA ES INVISIBLE PARA EL INSTRUMENTO. Lo medi yo:**

    aduana.buscar_vecinos(hijo, [madre])  ->  []
    señales:  texto 0,224 | familia 0,000 | paso contra nodo 0,572
    umbrales: texto 0,35  | familia 0,30  | paso contra nodo 0,60

**Ninguna de las tres la levanta.** La arista se declara **por lectura, en el acto
del veredicto** (`D.19`, `D.29`), y **el umbral no se toca**: que la señal mida
0,572 y el umbral este en 0,60 no es un argumento para bajarlo, es la razon por la
que la lectura no delega en la señal.

**COMO SE HACE, si dices que si:** se relanza el arnes con `MODO_INSERCION=insertar`
y con un encargo que ponga la madre delante. **Yo no lo he escrito**, porque un
encargo que presupone tu permiso seria adivinarlo.

### 3.2. LA SEGUNDA DECISION: traer el libro del lote 2

`D.24` fija el orden: **`smart_who` (7 capitulos)**, luego `zhuo_manager` (12),
luego `scott_radical_candor` (15), y el ultimo `mundo_10_reservado`. **El material
tiene que aparecer en `fuentes/smart_who/` en la maquina donde corra el arnes**,
porque `.gitignore` lo mantiene fuera del repo a proposito y esa razon (texto con
derechos de otro autor) **no la toca esta parada.**

### 3.3. LA TERCERA: el merge, que te lo pido y no lo hago

**`extraccion-mundo-11` esta lista y verde**, con las cifras de la seccion 2
delante. **EL BUCLE NO FUNDE RAMAS Y EL BUCLE NO CREA REMOTOS**
(`AUDITOR_FORJA.md` seccion 3), asi que **este fichero PIDE el merge y no lo
ejecuta.** Todo esta pusheado a `origin/extraccion-mundo-11`.

### 3.4. UNA PREGUNTA DE DOCTRINA QUE NO ES MIA, Y NO LA HE ADJUDICADO

**Es la unica cosa de las dos vueltas que se quedo en el filo, y las dos sedes
coinciden en dejartela a ti** (el extractor la propone en su reporte C.7, y yo la
sostengo en el ACTA 2 secciones 3.3 y 3.5):

> **`D.27` no dice CUANTOS objetos hacen inventario.**
>
> El parrafo 29 abrio **cinco** medios y dio nodo. El parrafo 38 abre **dos** y no
> lo dio. El parrafo 32 abre **dos** y si lo dio. **Entre esos casos hay una raya
> que ningun documento de esta casa ha escrito.**

**Los dos cortes se sostienen con la vara vigente, y por eso NO es una parada por
doctrina nueva:** el 38 cae por la **restriccion 2** (siete adjetivos de adecuacion
en el sitio del criterio), y el 32 aguanta porque **es el unico parrafo de los dos
capitulos que nombra sus objetos sin cubrirlos con ningun adjetivo** (contado:
parrafo 32, cero adjetivos de adecuacion). **La raya se puso en el CRITERIO, que es
donde D.27 la tiene escrita, y no en el NUMERO, que es donde no dice nada.**

**Lo que te traigo es el aviso, no una propuesta de texto:** el proximo libro va a
traer el mismo filo, y **`examinar_normas_pesos_medidas` es el nodo que lo decide**
si algun dia quieres poner un suelo. Es el mas delgado del lote: cinco pasos, de
los que tres son andamio (reune, reune, escribe), sobre dos objetos del libro.
**Esta en cuarentena y ahi se queda hasta que decidas.**

**NINGUNA VUELTA ESTRECHA NI ENSANCHA ESA VARA SIN CORRECCION DECLARADA TUYA**
(`D.27` ultima linea, `AUDITOR_FORJA.md` 6.3). Ni el extractor ni yo la hemos
movido un milimetro.

---

## 4. LO QUE LAS DOS VUELTAS DEJAN MEDIDO, que es el producto de una campaña de calibracion

**El lote 1 se hizo para medir el instrumento con trabajo de verdad delante**
(`D.24`). Esto es lo que midio:

| medida | cifra |
|---|---|
| **pasos que puso el extractor y no el libro** | **13 de 36, el 36 por ciento.** Cuatro de los seis candidatos llevaban al menos uno |
| **el reparto, y es la lectura util** | **el puente sube cuando baja el inventario del parrafo.** El parrafo mas rico (29, cinco medios) dio **0 por ciento**. El mas pobre (32, una frase) dio **83 por ciento**. **Un parrafo pobre no produce un nodo pobre: produce un nodo inventado** |
| **lo que la aduana caza de eso** | **NADA. 6 de 6 verdes antes y despues.** Un informe verde certifica que la ficha esta bien construida, no que sus pasos sean del libro |
| **candidatos por palabra** | `cap_02`: 6 en 819 palabras (**0,73 por 100**). `cap_03`: **0 en 389** |
| **densidad de adjetivo de adecuacion** | `cap_02` **1,84** por 100 palabras de cuerpo, `cap_03` **5,95**. Recontado por mi parrafo a parrafo |
| **caidas en la aduana al escribir** | **cero en las dos vueltas**, contra una puerta que se demostro que muerde |
| **el error de dejar pasar** | **SIN MEDIR, y es el hueco abierto.** Sin inserciones no hay veredictos, sin veredictos no hay SANO, y sin SANO no hay muestra pineada. **Dos tandas con poblacion cero.** Es lo primero que habra que medir el dia que autorices |
| **coste** | vuelta 1: 7,01 USD extractor + 6,63 auditor. Vuelta 2: 7,41 USD extractor. Leido de los testigos del arnes |

---

## 5. LAS TRES COSAS QUE HAY QUE HEREDAR, y ya estan remediadas o dichas

*Escalada que se declara y no se encarga es caida propia. Como no hay vuelta
siguiente a la que encargarselas, van aqui.*

### 5.1. El mensaje final del agente tambien es repo

**Lo encontre en rojo al empezar esta vuelta y lo deje en verde.**
`docs/loop/ultimo_extractor.json` es el testigo que escribe el arnes cuando el
turno acaba, y guarda **el mensaje final del extractor tal cual**. El de esta
vuelta traia **nueve guiones prohibidos** (siete largos y dos cortos sin corte), y
eso dejo el barrido en rojo y la prueba de aceptacion en 56 de 57.

**No es caida de ninguna de las tres especies** (no hay cifra falsa, no hay
veredicto mal puesto) **y no contradice al reporte**, que publico el barrido en
verde y tenia razon: **el testigo se escribe despues del ultimo hook.** Es la
unica prosa que un agente manda al repo **sin pasar por su propio hook**.

**Remedio, ya aplicado:** sustitui las diez formas prohibidas de `src/comun.py:44`
por el guion corto normal, el JSON sigue siendo valido y ninguna cifra del testigo
se toco. **Y para quien retome: escribe tu mensaje final con guion corto normal, o
el arnes lo mete en el repo por ti.**

### 5.2. Una cuenta viaja con su patron, o no es una cuenta

El reporte publica su densidad de adjetivos con el comando
`grep -oiE '<los 19 adjetivos de adecuacion>'`, **y los 19 adjetivos no estan
escritos en ninguna parte.** El comando **no se puede correr tal como se publica**.

Lo reconstrui con 19 raices defendibles y **las dos cifras publicadas se
sostienen** (el 20 de `cap_03` sale identico), **pero hay mas de una lista que da
el 14 de `cap_02`, y sin el patron no se puede saber cual se uso.** Ahi nacieron
las dos unicas caidas del extractor en esta vuelta (ACTA 2 seccion 4.1), las dos
de especie REPORTE y **ninguna acumula**.

**Adjudicado, y no es doctrina nueva:** es la seccion 2 de `AUDITOR_FORJA.md`
(*nada se afirma sin haberse consultado en esta vuelta*) y la cosecha 7.B leidas
sobre un comando en vez de sobre una ruta.

### 5.3. Mi propia caida, y no la estoy reiniciando

**El ACTA 1 publico `wc -l config/pares_mutuos.jsonl -> 0 (fichero vacio)`. Ese
fichero no existe y no ha existido nunca.** La cifra (0 pares mutuos) es correcta;
**lo falso era la prueba.** Es caida **MIA**, de especie **CIFRA PUBLICADA** por la
cosecha 7.B, y **la trajo declarada el extractor** sin corregirla el, respetando la
sede (`D.28`). **Sin el, yo no la habria visto.**

**Ya esta corregida en su sitio, tachada y con el texto vigente al lado**, en el
ACTA 1 secciones 1.2 y 7. **No se borro ni una palabra.**

**Y lo peor esta escrito en el acta:** la leccion que incumpli la habia escrito yo
mismo, en la seccion 4.3 de esa misma acta y el mismo dia. **Van dos actas y dos
caidas propias, distintas.** No llegan a la tercera de la misma, asi que la
clausula de la cosecha 7.D todavia no obliga; **me aplico el remedio igual y por
adelantado, y queda escrito para quien retome:** toda salida de comando que se
publique va pegada de una corrida de esa misma vuelta, y toda cuenta de ficheros
va con `ls` o `git ls-files`, **nunca con un `wc -l` sobre una ruta que puede no
estar. La racha no se reinicia sola, y yo no la he reiniciado.**

---

## 6. COMO SE RETOMA

**Nada de esto lo hace el bucle solo. Los tres caminos empiezan contigo.**

| si decides... | lo que hay que hacer |
|---|---|
| **insertar los seis** | borrar `docs/loop/PARA_ALEXIS.md`, escribir el encargo en `docs/loop/PROMPT_SIGUIENTE.md` **con la madre delante del hijo** (seccion 3.1), y relanzar el arnes con `MODO_INSERCION=insertar`. **La primera tanda con veredictos es la primera que puede medir el error de dejar pasar**, asi que ese encargo deberia pedir la muestra pineada con su semilla escrita |
| **seguir con el lote 2** | poner el libro en `fuentes/smart_who/`, borrar este fichero, escribir el encargo y relanzar con `MODO_INSERCION=cuarentena` |
| **cerrar la campaña aqui** | revisar la rama `extraccion-mundo-11` y fundirla tu. **El bucle no funde ramas** |
| **dejarlo como esta** | no hace falta hacer nada. **Mientras este fichero exista o `PROMPT_SIGUIENTE.md` siga vacio, el arnes se detiene solo** y apunta aqui |

**Y una recomendacion que doy como auditor y que no ejecuto:** si vas a autorizar
inserciones, **el encargo deberia mandar que la pasada de transcripcion se haga en
el acto de escribir cada candidato y no en una vuelta posterior.** Esta campaña
gasto **una vuelta entera** en reparar 13 puentes de seis candidatos. Aplicada al
escribir, la vuelta 1 habria salido con 32 pasos y sin deuda. **La propone el
extractor en su reporte C.7 punto 2, la sostengo, y no es maquinaria: es orden de
trabajo.**

---

**Lo que hay delante de ti es un lote de seis candidatos que ninguna guarda puede
seguir mejorando, un instrumento que se midio a si mismo y encontro su propio
punto ciego con nombre y cifra, y dos vueltas que no metieron ni una linea en el
grafo sin tu permiso. El bucle hizo lo que sabia hacer. Lo que queda es tuyo.**
