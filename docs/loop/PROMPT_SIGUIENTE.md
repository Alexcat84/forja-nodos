# ENCARGO DE LA VUELTA 9: **ABRE EL LOTE 3, `zhuo_manager`**

*Escrito por el auditor al cerrar el ACTA 8, con su linea leida del instrumento y
pegada aqui como manda la TAREA 1.a de este mismo encargo:*

    $ grep -n "^# ACTA 8" docs/loop/ACTA_AUDITOR.md
    6520:# ACTA 8. VUELTA 8, lote 2 (smart_who), cierre del libro: cola del cap_06.md...

**El lote 2 quedo cerrado en extraccion y sus dos condiciones de apertura del lote 3
estan medidas en verde** (ACTA 8 seccion 10). `D.32`: el acta que cierra un lote escribe
el encargo del siguiente, sin parada entre medias.

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO PRIMERO: TUS RACHAS, MEDIDAS Y NO SUPUESTAS

    racha CLASE           : 0 de 2     ocho tandas sin ninguna
    racha CIFRA PUBLICADA : 0 de 2     ocho tandas sin ninguna
    racha REPORTE         : 1 de 3     LA VUELTA 8 SUMO UNA

**LA VUELTA 8 FUE UNA BUENA VUELTA Y AUN ASI SUMO.** Diez discutibles marcados y **los
diez sostenidos**: acertaste en las diez dudas que te pusiste, incluida la unica en la
que mi lectura ciega te contradijo. **Las tres caidas estan donde no miraste**, las tres
en tablas de la TAREA 5, y las tres son **la misma averia**:

> **UNA CIFRA DE UNA VUELTA ANTERIOR, TECLEADA DE MEMORIA EN VEZ DE RELEIDA.**

**`D.35` te salvo en lo suyo: reabri tus 65 punteros de linea con `sed` y no habia ni
uno roto.** Lo que fallo es el caso de al lado, que ningun remedio cubria. Las tres, con
su nombre, en el ACTA 8 seccion 4.1:

1. **Cuatro cifras que nunca se publicaron** en la tabla de discrepancias de palabras
   (5.g): `936`, `3.888`, `10.916` y `6.301`. **Las busque en `docs/` entero y ninguna
   aparece.** Lo publicado fue 961, 3.863, 10.696 y 6.250. **Y las tres discrepancias
   que declaraste inexplicadas no existen:** dos son la cabecera de siete lineas, la
   misma causa que ya habias explicado para `cap_04` y `cap_05`, y la tercera no es una
   diferencia.
2. **El capitulo esta mal nombrado en la metrica que el capitulo decide.** `cap_06.md`
   L247 a L455 **no es la cola del Cap. 5: es el cuerpo del Cap. 6.** Adjudicado en el
   ACTA 8 seccion 4.1 caida 2, con la doctrina que descubriste tu en la vuelta 5.
3. **La tabla que decide el volumen del lote 3 cuenta cinco capitulos y el lote tiene
   seis** (5.f pierde el `cap_02`, Cap. 1, al 6,25 por ciento).

**NINGUNA MOVIO UN DATO NI UNA DECISION**, por eso son especie REPORTE y por eso el
bucle sigue. **Pero las tres viven en TABLA y las tres acumulan.**

---

## TAREA 1. LOS REGISTROS DEL ACTA 8, Y SU PUNTO 1.a ES BLOQUEANTE

### 1.a. **BLOQUEANTE: EL REMEDIO, Y ES `D.35` UN PASO AL LADO**

*Se encarga aqui y no se declara y ya, porque mi seccion 1.4 dice que la escalada se
encarga. **No es doctrina nueva y no es maquinaria** (moratoria, `EXTRACTOR.md` 13): es
pegar una salida que ya corres, que es el mismo argumento con el que `D.35` nacio. Si
entra en el banco lo decide Alexis, no yo, y se lo he pedido.*

> **NINGUNA CIFRA QUE PRESENTES COMO PUBLICADA EN UNA VUELTA ANTERIOR SE TECLEA SIN LA
> SALIDA DE `grep -n` SOBRE `docs/loop/REPORTE.md` PEGADA AL LADO.**

    | unidad | antes | hoy | la salida, pegada |
    |---|---:|---:|---|
    | cap_03 | 10.696 | 10.669 | `3086:| *fichero* cap_03.md | entero | 10.696 |` |

**Y SU HERMANA, que es la que habria cazado la tercera caida:** **si la comparacion sale
CERO, se escribe CERO y no se borra la fila.** Una tabla de discrepancias sin sus filas
iguales no se puede auditar.

**Y LA TERCERA, que es la que habria cazado la caida del recuento de capitulos:**
**toda tabla que compara N filas dice de donde salen las N**, y si sale de una serie
publicada arriba, **se cuentan las filas de la serie y se escribe la cuenta.**

### 1.b. Las adjudicaciones que te afectan, para que no las vuelvas a plantear

| # | lo adjudicado | donde |
|---:|---|---|
| 1 | **Tus tres aristas de `organizar_jornada...` NO se declaran. SOSTENIDO.** Un horario no enumera partes | ACTA 8, 3.1 |
| 2 | **`seleccionar_jugador...` no apunta a `profundizar_respuestas...`. SOSTENIDO** | 3.2 |
| 3 | **`conducir_entrevista_cronologica...` paso 12 no apunta a la tactica. SOSTENIDO** | 3.3 |
| 4 | **28 contra un suelo de 13: SOSTENIDO.** Rehice tu barrido con filtro propio y no falta ni una cabeza | 3.4 |
| 5 | **P5, guepardos y corderos, ES minable. SOSTENIDO**, y a ciegas yo lo lei igual | 3.5 |
| 6 | **Los tres pasos que no dan hijo se quedan dentro. SOSTENIDO. Y aqui cai yo**, que sostuve lo contrario a ciegas argumentando por bascula, que mi propia vara prohibe | 3.6 |
| 7 | **`formar_equipo_practicas_metodo` con tres pasos: SOSTENIDO** | 3.7 |
| 8 | **La cabeza de las cautelas abre bien, y sus numeros de paso 3, 5 y 6 son correctos**, verificados contra el JSON | 3.8 |
| 9 | **Contar los cinco puentes aunque los reescribieras: SOSTENIDO**, y era la decision honesta de las dos | 3.9 |
| 10 | **Leer la regla del lote 3 contra el 36,11: SOSTENIDO** | 3.10 |
| 11 | **TU AVISO 2 RESUELTO: `tres capitulos por vuelta` NO CHOCA con `EXTRACTOR.md` 12.4**, porque 12.4 declara su propia cifra *no sagrada* y pone lo vinculante en el disparador. **El disparador sigue vivo y esta abajo** | 3.11 |

### 1.c. Las correcciones declaradas, sin borrar nada

**No reescribes el tramo de la vuelta 8 del reporte.** Abres tu vuelta 9 por anexion
(`EXTRACTOR.md` 3) y **en tu apertura pones un bloque de tres lineas** que diga:

- que las cuatro cifras de la tabla 5.g quedan **corregidas por el ACTA 8 4.1**, con las
  publicadas de verdad al lado;
- que la fila *cola del Cap. 5* se llama **Cap. 6, `Your Greatest Opportunity`**, y que
  la fila *Cap. 6* de 370 palabras es **la cola de ese mismo capitulo**;
- que el lote 2 tuvo **SEIS** capitulos minados y no cinco.

**Y NO CAMBIA NI UNA TASA:** las 90 y las 5 y el 5,56 por ciento sobreviven intactas,
comprobado en el ACTA 8 seccion 7. **Cambian los nombres, y los nombres son la mitad de
la regla** (`AUDITOR_FORJA.md` 8.2 y 8.4).

---

## EL LOTE 3: `zhuo_manager`, Y LO QUE YA ESTA MEDIDO POR MI

**No lo eliges tu: lo dice `docs/loop/ORDEN_DE_LOTES.md`.** Julie Zhuo,
*The Making of a Manager*, 2019. **12 ficheros, 70.041 palabras de cuerpo**, contadas
por mi hoy y cuadran exacto con la tabla del orden de lotes. **La clave ya esta en
`fuentes/FUENTES_CANONICAS.json` con su ficha completa** (titulo, autor, ano y tres
ISBN), asi que **no hay ficha que abrir**: es el primer lote de la campana que arranca
con la fuente ya cerrada.

### LO QUE MEDI YO Y TE REGALO, porque el lote 2 lo pago caro

**El recorte de `smart_who` NO era un fichero por capitulo**, y eso costo una
discrepancia entera en la vuelta 5 y el mal nombre de capitulo de la vuelta 8.

    L9 de cada fichero de zhuo_manager, leida por mi:
      cap_01 -> "Introduction"    cap_05 -> "Chapter Four"   cap_09 -> "Chapter Eight"
      cap_02 -> "Chapter One"     cap_06 -> "Chapter Five"   cap_10 -> "Chapter Nine"
      cap_03 -> "Chapter Two"     cap_07 -> "Chapter Six"    cap_11 -> "Chapter Ten"
      cap_04 -> "Chapter Three"   cap_08 -> "Chapter Seven"  cap_12 -> "Epilogue"

**AQUI EL FICHERO SI PARECE SER EL CAPITULO**, y ademas comprobe que `cap_02`, `cap_03`
y `cap_04` **cierran su propio capitulo en su ultima linea con texto**:

    cap_03 L229: In the chapters ahead, we'll look at all the major aspects of a manager's job...
    cap_04 L321: ...the secret sauce to coaching is the topic of our next chapter.

> **LO QUE MEDI SON TRES CIERRES DE DOCE. NO DES POR HECHO LOS OTROS NUEVE.** La
> adjudicacion del ACTA 5 sigue mandando: **LA UNIDAD ES EL CAPITULO**, y la cabecera
> nombra la unidad con la que el fichero EMPIEZA. **Comprueba el cierre de cada fichero
> que abras, y si uno no cierra donde acaba, lo declaras antes de cortar.**

### EL VOLUMEN: **TRES UNIDADES POR VUELTA**, y de donde sale

**`AUDITOR_FORJA.md` 8.1 y `ORDEN_DE_LOTES.md`:** los **seis** capitulos del lote 2
bajan respecto al 36,11 por ciento de la linea base y **el peor esta en una quinta
parte** (7,55). El criterio se cumple y **el lote 3 sube a tres.**

**LAS TRES DE ESTA VUELTA, en el orden del libro:**

| unidad | fichero | palabras | lo que es |
|---|---|---:|---|
| **Introduction, `Great Managers Are Made, Not Born`** | `cap_01.md` | **2.917** | |
| **Cap. 1, `What Is Management?`** | `cap_02.md` | **6.477** | |
| **Cap. 2, `Your First Three Months`** | `cap_03.md` | **4.292** | |
| | | **13.686** | |

**LA INTRODUCCION CUENTA COMO UNA DE LAS TRES, y digo por que:** sin ella la vuelta
serian 20.923 palabras, que es mas del doble de lo que la vuelta 8 abrio. **Si Alexis
lee la regla de otro modo, la diferencia es de una unidad y el disparador de abajo la
absorbe.** Lo digo aqui en vez de dejarlo implicito.

### EL DISPARADOR DE `EXTRACTOR.md` 12.4, QUE SIGUE VIVO Y ES LO QUE MUERDE

> *La cifra no es sagrada; **el disparador si**: si una vuelta no cierra su reporte, la
> siguiente baja el tramo.*

**Adjudicado en el ACTA 8 3.11: la banda de cinco a quince candidatos NO te bloquea, y
tres capitulos por vuelta no la contradice.** Pero:

> **SI NO CIERRAS TU REPORTE, CIERRA LO QUE TENGAS Y DILO CON SU CIFRA. Eso arma el
> disparador y la vuelta 10 baja el tramo. NO es una caida: es la regla funcionando.**
> **Lo que si seria caida es dejar una unidad a medias sin declararlo.**

---

## LAS TAREAS

### TAREA 2. LAS COMPROBACIONES DE APERTURA Y EL MAPA DEL LIBRO, ANTES DE CORTAR NADA

**Corridas por ti y con su salida pegada** (`D.35`), sobre los tres ficheros que vas a
abrir **y sobre los doce para el mapa**:

1. **El gate, el barrido, las 72 pruebas y `rancios`**, antes de la primera operacion.
   **Esperado: 52 nodos, 37 aristas, 72 de 72, 60 veredictos.** Si no cuadra, lo
   declaras y **no sigues hasta explicarlo.**
2. **La cabecera de los tres ficheros** (`unidad`, `titulo_textual`) y **su ultima linea
   con texto**, para comprobar que cada uno cierra su capitulo. **Los tres, aunque yo ya
   haya medido esos tres: mi medida es una nota previa y `EXTRACTOR.md` 5 dice que la
   nota previa se contrasta, no se copia.**
3. **Las palabras de cada uno**, contadas del fichero. Si no dan 2.917, 6.477 y 4.292,
   **declaras la discrepancia y no eliges en silencio.**
4. **`zhuo_manager` en `fuentes/FUENTES_CANONICAS.json`**, leida y pegada.

### TAREA 3. LA INTRODUCTION Y EL Cap. 1, cada uno con su frontera publicada ANTES de cortar

**LA FRONTERA SE PUBLICA ANTES, Y SE COMMITEA ANTES.** La vuelta 8 lo hizo con
`227085a` y por eso su coincidencia de siete piezas se puede comprobar contra un fichero
anterior al trabajo. **Repitelo.**

**Y EL METODO DE LA FRONTERA ES EL QUE FUNCIONO, no el que fallo:**

> **RECORRE EL FICHERO COMPROBANDO COBERTURA, no una lista de cabeceras.** En la vuelta
> 8 una lista de cabeceras se dejo **tres piezas** fuera (un titulo con interrogacion y
> dos bloques de publicidad, **1.130 palabras**, y de una salio un nodo). **Lo que las
> cazo fue comprobar que las piezas cubren el rango sin hueco y sin solape**, y esa
> comprobacion se escribe en el reporte, no se promete.

**Despues los candidatos, uno a uno**, con:

- **la aduana en el mismo acto de escribir cada uno** (`EXTRACTOR.md` 16). No se escriben
  quince y se pasa la aduana al final;
- **la relectura de fidelidad DENTRO del acto de escribir** (`D.30`, `EXTRACTOR.md`
  15.4). En la vuelta 8 cazo cinco puentes de una especie nueva, **el verbo de
  instrumentacion**, y los cinco se corrigieron antes de commitear. **Vigila esa
  especie: el libro manda un resultado y tu escribes el gesto.**
- **`D.27` pieza a pieza**, con el fallo publicado y su cita, tambien para lo que
  descartas. **Un tramo descartado con su razon escrita es trabajo hecho.**

### TAREA 4. EL Cap. 2, igual, y los vecinos que la aduana levante

**Es la segunda vez que escribes contra un grafo con material propio dentro, y la
primera contra un libro DISTINTO.** El lote 2 levanto vecinos por `familia_id` porque el
libro era monotematico. **Este habla de gestion y el otro de contratar, y el Cap. 7 de
Zhuo se llama `Hiring Well`: espera solapes de verdad cuando llegues ahi, y no todavia.**

**Cuando la aduana levante un vecino: lo lees, escribes el veredicto con su razon y
sigues.** Eso no es una parada, es la aduana funcionando.

**`D.37`, y ojo con lo que NO puedes hacer:** si un capitulo trae una serie que el
titulo enumera, **la arista se declara en la misma vuelta en que se insertan las
partes**. Como `MODO_INSERCION=cuarentena` y **no vas a insertar nada**, la condicion no
se cumple: **dejas la lista escrita en tu reporte con madre, paso e hijo**, como hizo la
vuelta 8 en su 1.i con once aristas. **No fuerces `python forja.py arista` sobre lo que
esta en cuarentena: lo rechaza, y con razon.**

### TAREA 5. EL INFORME, LOS COMMITS Y EL CIERRE CON SUS CUATRO MEDIDAS

    python forja.py informe --carpeta cuarentena/zhuo_manager

**UN COMMIT POR UNIDAD, con los JSON dentro** (`D.25`), y su mensaje con la cifra:
*del Cap. 1 salieron N candidatos.* **CERO INSERCIONES:** `MODO_INSERCION=cuarentena`, y
la insercion es autorizacion del fundador (`D.26`).

**LAS CUATRO MEDIDAS, DESGLOSADAS POR CAPITULO Y NO POR VUELTA** (`AUDITOR_FORJA.md` 8):

1. **candidatos por mil palabras**, con los dos denominadores si el capitulo no se mina
   entero (el total y lo minado), como hiciste bien en la vuelta 8;
2. **`PASOS INVENTADOS SOBRE PASOS ESCRITOS`, una fila por capitulo y ademas el total.**
   **Nombra cada fila con el CAPITULO, no con el fichero**, y si los dos no coinciden,
   **dilo en la propia fila**. Esta es la caida 2 de la vuelta 8 y es la que mas caro
   sale, porque **de esta cifra sale el volumen del lote 4**;
3. **veredictos escritos**, con su origen;
4. **cuanto tardo**, leido de git. **Y si comparas con otra vuelta, compara la misma
   medida:** la vuelta 8 comparo su apertura-a-ultimo-tramo contra la
   apertura-a-cierre de la vuelta 7 y le salio 0,704 donde era 0,934 (ACTA 8, 4.1
   caida 4).

**Y LA CIFRA A VIGILAR, que me quedo de tu propio aviso y hago mia:** la tasa de puentes
**subio tres medidas seguidas** en el lote 2 (3,09 / 5,00 / 5,56). **Contra la linea base
todo baja holgadamente y la regla solo mira eso**, pero **escribe la tendencia local en
tu cierre** con su cociente. Si sigue subiendo al mismo ritmo, deja de ser una nota.

---

## LO QUE **NO** ES DE ESTA VUELTA, dicho para que no lo intentes

- **Los 15 candidatos de `cuarentena/smart_who/` no se insertan.** Su autorizacion es del
  fundador y esta pedida en el ACTA 8 seccion 11. **Y no los toques**: estan cerrados.
- **Las 11 aristas de serie y los 3 veredictos de vecino del lote 2** esperan al acto de
  insertar. **Estan escritos en el reporte de la vuelta 8, 1.i y 1.g. No los declares
  hoy.**
- **No abras `cap_04.md` en adelante** de `zhuo_manager`. Tres unidades, y el `cap_12.md`
  (`Epilogue` mas `Acknowledgments`, `Notes` e `Index`) **se juzgara antes de cortarse**
  cuando toque, como el tramo C del lote 2.
- **Ni umbrales, ni reglas de id, ni esquema, ni `D.27`, ni la vara de continua contra
  repite.** Ninguna vuelta las mueve.
- **Y NO FABRICAS MAQUINARIA** (`EXTRACTOR.md` 13). En particular **no propongas una
  guarda que compruebe cifras citadas.** El remedio de 1.a es pegar una salida que ya
  corres, y esa es toda la maquinaria que hay.

## LAS PARADAS

**Paras, lo declaras en TU REPORTE y te detienes si:**

- una regla de la casa te obliga a algo que rompe otra regla de la casa;
- necesitas mover un umbral, una regla de id, el esquema, `D.27` o la vara;
- alguna comprobacion de apertura de la TAREA 2 falla.

**NO paras por:** que un candidato caiga en la aduana (lo corriges y pegas la salida),
que la aduana levante vecinos (los lees y escribes el veredicto), que una unidad no de
ni un procedimiento (se dice con su razon), ni por que no te de tiempo a las tres
unidades (cierras lo que tengas, lo dices, y el disparador de `12.4` hace su trabajo).

**TU NO ESCRIBES `docs/loop/PARA_ALEXIS.md`** (`D.28`). Eso lo hace el auditor.

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una
regla vigente, paras y lo traes. No adivines.**
