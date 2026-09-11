# ENCARGO DE LA VUELTA 11: **EL Cap. 5 DE `zhuo_manager`, Y LA COLA DE ARISTAS QUE DEJA LA 10**

*Escrito por el auditor al cerrar el ACTA 10, con su linea leida del instrumento y pegada
aqui como manda la TAREA 1.a de este mismo encargo:*

    $ grep -n "^# ACTA" docs/loop/ACTA_AUDITOR.md | tail -1
    8536:# ACTA 10. VUELTA 10, lote 3 (zhuo_manager), Cap. 3 (Leading a Small Team) y Cap. 4 (The Art of Feedback)

**El lote 3 sigue ABIERTO: siete ficheros y 42.800 palabras sin tocar**, contadas por mi
fichero a fichero. Esta acta **no cierra lote**, asi que **no hay apertura de lote que
medir** (`D.32`) y esta vuelta es la continuacion del mismo libro.

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO PRIMERO: TUS RACHAS, MEDIDAS Y NO SUPUESTAS

    racha CLASE           : 0 de 2     diez tandas sin ninguna
    racha CIFRA PUBLICADA : 0 de 2     diez tandas sin ninguna
    racha REPORTE         : 2 de 3     LA VUELTA 10 NO SUMO. Sigues a una de parar

    y la mia, que no se mezcla con la tuya:
    racha REMEDIO ROTO del auditor : 2 de 3   la abri yo en la 9 y la sumo yo en la 10

**LA VUELTA 10 ES LA MEJOR QUE HA CORRIDO ESTA CASA, Y LO DIGO CON LAS CIFRAS DELANTE.**

- **44 piezas de frontera recomputadas PALABRA A PALABRA y 44 aciertos al numero.** No
  sume: recompute cada fila. **Cero huecos, cero solapes, cero diferencias.**
- **29 filas de pasos contadas una a una: 29 exactas.** Los denominadores 120, 111 y 231
  los firmo yo.
- **33 punteros de linea con mi propia red: 33 correctos.** Contra los siete rotos de la
  vuelta 9.
- **EL REMEDIO DE LA `1.a` FUNCIONO A LA PRIMERA.** Prometiste nueve sedes y cumpliste
  nueve, **y ademas dejaste un hueco dicho SIN nombre de seccion** cuando el dato aun no
  existia. Eso es el punto 1 del remedio aplicado exactamente donde tenia que aplicarse.
- **Y LO MAS DIFICIL DE CONSEGUIR: tu corte y mi lectura ciega coinciden 27 de 27**, y no
  solo en el total: **en el reparto pieza a pieza, y en las cinco piezas que los dos
  dejamos fuera.** Es la primera vez que pasa aqui.

**Y LO QUE CAE, que son dos cosas y ninguna es de las gordas:**

> **1. TU DISCUTIBLE 1 CAE: LOS TRES VERBOS CUENTAN.** `L127` y `L139` **no mandan nada,
> definen.** Un paso que abre con `Escribe` no cambia el modo de un mandato del libro:
> **mete un mandato donde no habia ninguno y nombra un medio que el libro no nombra.** Tu
> propia razon para corregirlo lo dice. **Si hubo que corregirlo porque anadia un medio,
> anadia contenido, y anadir contenido es puente.** La tasa del Cap. 1 de la vuelta 9 va a
> **6 de 79, el 7,59 por ciento**, que es la cifra que tu mismo publicaste como alternativa.
>
> **NO ES CAIDA DE CREDITO Y NO ACUMULA** (`AUDITOR_FORJA.md` 8.4): *un puente encontrado y
> corregido es la regla funcionando.* **Los tres los viste tu, los corregiste tu y los
> declaraste tu.** Lo que cae es la cuenta, no el trabajo.

> **2. Y UN HALLAZGO QUE NINGUNO DE LOS DOS MARCO COMO TAL, y que yo marque a ciegas por su
> sede: `L283` del `cap_05.md` esta dentro de un candidato y tu frontera lo declara
> descartado.** Tu `4.2` pone `L283` en P19; tu `4.3` descarta P19 y su razon enumera
> `L285`, `L287` y `L289` **y no menciona `L283`**; tu `4.4` dice que el candidato 50 sale
> **solo de P18**; y su **paso 8 es `L283` palabra por palabra.**
>
> **LA CONVENCION QUE ROMPE ES TUYA:** en este mismo reporte, cuando un candidato bebe de
> varias piezas **las listas todas**, seis veces. **La fila 50 es la unica que bebe de una
> pieza y no la nombra.**
>
> **ADJUDICADO: NO ACUMULA, y la adjudicacion entera esta en el ACTA 10 seccion 4.3, con la
> lectura contraria escrita al lado.** La averia vive en `cuarentena/`, **que no es sede de
> ninguna de las tres especies**, y `5.2` dice literal que separar las especies fue lo que
> evito que el bucle parara por una frase mientras los datos estaban intactos. **Y los
> datos estan intactos: 52 nodos, 37 aristas, 60 veredictos, cero inserciones, medido por
> mi.** **Si Alexis lo lee al reves, la racha va a 3 de 3 y esto era una parada.**

---

## TAREA 1. LOS REGISTROS DEL ACTA 10, Y SU PUNTO 1.a ES BLOQUEANTE

### 1.a. **BLOQUEANTE: `L283` FUERA, Y EL CRUCE QUE LO CAZA**

**Tres cosas, y las tres en el mismo commit:**

1. **DECIDE `L283` CON EL TEXTO DELANTE Y DECLARA LO QUE DECIDAS.** O sale del paso 8 de
   `dar_mala_noticia_decision_tomada` porque es el cierre del capitulo entero
   (*what I've learned about giving feedback, **even the most difficult feedback***) y no
   la doctrina del nodo mas estrecho de los doce; **o tu frontera mueve su borde de P18 a
   P19 y lo dice con su razon.** Las dos salidas valen. **La que no vale es que la frontera
   diga una cosa y el nodo haga otra.**
2. **CORRIGE POR CORRECCION DECLARADA Y SIN BORRAR** las tres filas que arrastra: `4.3`
   (la razon de P19), `4.4` (la fila 50 y su columna de piezas) y `5.a` (las palabras
   minadas del Cap. 4, que pasan de 5.635 a hasta 5.904, y el porcentaje de 89,2 a hasta
   93,5). **Por anexion en tu vuelta 11, sin reescribir el tramo de la 10.**
3. **Y AL CERRAR CADA CAPITULO, EL CRUCE PIEZA CONTRA CITA.** Para cada candidato, cada
   linea que sus pasos citan **contra el rango de las piezas que su propia fila declara**.
   Si una linea cae fuera, **o entra la pieza en la fila o sale la linea del paso.**

> **NO ES MAQUINARIA Y NO PROPONGAS UNA GUARDA** (moratoria, `EXTRACTOR.md` 13, y el
> ACTA 10 4.4). **Es la relectura de punteros que YA CORRES** (`C.10.8`), con una
> comparacion mas: hoy comprueba que la linea existe en el fichero; que compruebe tambien
> **de que pieza es.**

### 1.b. Las adjudicaciones que te afectan, para que no las vuelvas a plantear

| # | lo adjudicado | donde |
|---:|---|---|
| 1 | **Tu DISCUTIBLE 1 CAE: los tres verbos cuentan como puentes.** Cap. 1 de la vuelta 9 a 7,59 por ciento. **Sin caida de credito** | ACTA 10, 3.1 |
| 2 | **Tu DISCUTIBLE 2 SOSTENIDO, y aqui cai yo.** Las dos piezas salen, **y tu tenias razon en cual es la fuerte**: la dinamica trae inventario propio y el equilibrio no. **Yo argumente por el disparador con numero, que es una senial, y `D.19` me lo prohibe** | 3.2 |
| 3 | **Y adjudicada la pregunta que marcaste: SI sale a nodo propio una pieza sin inventario propio, en este caso**, porque el modo de fallo que `D.27` caza (*cualquier paso que se escriba lo escribe el extractor*) **no se da**: tus tres pasos son transcripcion de `L87`, `L89` y `L93`, comprobado. **`D.27` no se mueve** | 3.2 |
| 4 | **Tu DISCUTIBLE 3 SOSTENIDO: el `critique` se queda fuera**, y a ciegas lo lei igual y por las mismas dos lineas, `L27` y `L29` | 3.3 |
| 5 | **Tu DISCUTIBLE 4 SOSTENIDO por los dos lados.** Ni encontre puentes que no vieras en el Cap. 4, ni encontre perdida de mandato. **Y tu cifra de 16 pasos con atribucion reproduce al numero** | 3.4 |
| 6 | **`0 CAERIAN` y `0 CHOCAN` son ceros medidos.** Hice caer dos guardas por mutacion, con su control al lado: la de `REGLAS_DE_ID.md` y la del choque dentro del lote | 1.7 |
| 7 | **Tu tabla `5.b` desglosa por capitulo y nombra bien las dos filas. CERO caida de 8.3.3** | 7.1 |

### 1.c. Las correcciones declaradas, sin borrar nada

**No reescribes el tramo de la vuelta 10.** Abres tu vuelta 11 por anexion
(`EXTRACTOR.md` 3) y **en tu apertura pones un bloque que diga:**

- que **los tres verbos de la `2.a.bis` cuentan**, y que la tasa del Cap. 1 de la vuelta 9
  queda en **6 de 79, 7,59 por ciento**;
- que **el residuo del Cap. 3 lo pongo yo**: `mover_rapido_persona_papel_equivocado`
  **paso 1** ordena *deja de considerar que tu papel es ante todo ser el campeon de tu
  equipo* y **`L283` del `cap_04.md` no ordena eso: lo cuenta en primera persona del
  pasado, y `L285` lo RATIFICA**. El propio paso se desdice dentro de si mismo. **Es la
  especie exacta del paso 7 del MISMO nodo, que tu si cazaste ese dia.** Corrigelo como
  corregiste aquel y **sumalo a tu cuenta de `D.30`**: el Cap. 3 queda en **4 de 120, el
  3,33 por ciento**;
- y que **`dar_opinion_especifica_tarea` paso 3 cuenta** (anadia *de las cuatro*, un
  recuento que el libro no hace) **y `elegir_forma_inspirar_cambio_conducta` paso 1 NO
  cuenta** (quitaba un matiz, no anadia nada, y esta casa no tiene casillero para eso).
  **El Cap. 4 queda en 2 de 111, el 1,80 por ciento.**

**LAS TRES CIFRAS DE LA VUELTA 10 QUEDAN ASI, Y SON LAS QUE EL ACTA FIRMA:**

    Cap. 3   4 de 120   3,33 por ciento
    Cap. 4   2 de 111   1,80 por ciento
    vuelta   6 de 231   2,60 por ciento

### 1.d. Dos cifras de `docs/` que **dicte yo mal** y que tu escribiste porque yo te lo mande

**Las dos son mias y las dos se corrigen, por correccion declarada y sin borrar el texto
viejo:**

1. **`ORDEN_DE_LOTES.md`, columna `estado` del lote 3.** Dice *3 de 12 ficheros minados,
   21 candidatos*, que era verdad cuando lo escribiste y es falso desde que cerraste la
   misma vuelta. **Ponlo AL CIERRE: `5 de 12 ficheros minados, 50 candidatos en
   cuarentena, SIN INSERTAR`**, y **esta vuelta corre a UNA unidad.**
   **Y la regla que saco de mi propio fallo, aplicala tu tambien: la columna `estado` lleva
   la cifra AL CIERRE de la vuelta que la escribe, o no lleva cifra.**
2. **`cap_12.md` NO es un `Index`: es el `Epilogue`, `The Journey Is 1% Finished`**, 449
   lineas y 3.511 palabras, y su `L15` abre con `THE MYTH`. **Mi encargo de la vuelta 10 lo
   llamo indice y se equivoco.** No es de esta vuelta; queda dicho para que la vuelta que
   lo abra **lo juzgue y no lo prejuzgue.**

> **NO TOCAS NI EL ORDEN, NI LAS CLAVES, NI LA CUENTA DE CAPITULOS, NI LAS PALABRAS.** Eso
> lo fija `D.24` y **no lo elige el bucle.** Si algo mas de esa tabla te parece falso, **lo
> declaras y no lo tocas**, como hiciste bien con la linea de *El volumen por vuelta*.

---

## EL TRAMO DE ESTA VUELTA: **UNA UNIDAD, Y DIGO DE DONDE SALE**

| unidad | fichero | palabras | lo que es |
|---|---|---:|---|
| **Cap. 5, `Managing Yourself`** | `cap_06.md` | **9.617** | el fichero mas gordo del libro |

**BAJO DE DOS UNIDADES A UNA Y NO MUEVO NINGUNA REGLA. Las tres razones, con su cifra:**

1. **A IGUALDAD DE PALABRAS NO HAY IGUALDAD.** La vuelta 10 abrio 13.555 palabras en dos
   ficheros; **`cap_06.md` solo trae 9.617**, el 71 por ciento de aquello **en una sola
   unidad**. Dos unidades serian 14.902 con el `cap_07`, y **la 10 ya se paso de banda con
   13.555.**
2. **27 CANDIDATOS CONTRA UNA BANDA DE CINCO A QUINCE** (`EXTRACTOR.md` 12.4). Tu propio
   `5.g` lo dejo medido: **si `cap_06.md` mina al 90 por ciento como estos dos, salen unos
   19 candidatos de una sola unidad.** Diecinueve ya es mas que la banda. **La banda no te
   bloquea (ACTA 8), pero el que fija el tramo la mira, y la miro con tu cifra.**
3. **ESTA VUELTA LLEVA CARGA DE ARRASTRE**, aunque menos que la 10: la `1.a` bloqueante y
   tres aristas de lectura.

**LO QUE MEDI YO DEL FICHERO, Y TE REGALO.** Cabecera leida por mi hoy:

    cap_06.md   unidad: Cap. 5   titulo_textual: Managing Yourself   L9: Chapter Five
    cap_07.md   unidad: Cap. 6   titulo_textual: Amazing Meetings    (el borde por el otro lado)
    palabras de cuerpo (de L8 en adelante): 9.617

> **ES UNA NOTA PREVIA Y SE CONTRASTA, NO SE COPIA** (`EXTRACTOR.md` 5). **Comprueba el
> cierre del `cap_06` y el borde del `cap_07` tu, y pega tus salidas.** Y recuerda lo que
> tu mismo dejaste escrito y yo verifique: **las cabeceras de este libro no llevan
> almohadilla; se distinguen porque son las unicas lineas del cuerpo sin sangrado de
> tabulador.**

---

## LAS TAREAS

### TAREA 2. LA COLA DE ARISTAS DE LA VUELTA 10, Y VA ANTES QUE EL LIBRO NUEVO

**Son tres lecturas de `D.29` sobre `cuarentena/zhuo_manager/`, que sigue en 50 ficheros y
sin insertar. Ninguna toca el grafo: CERO inserciones** (`D.26`). **Y a las tres correles
antes el test de `D.37`** (abrir el paso de la madre y ver si ahi se nombra al hijo)
**y di lo que salga**, que es lo que separa una de serie de una de lectura.

#### 2.a. La remision entre capitulos que ni se transcribe ni se cablea

    $ sed -n '181p' fuentes/zhuo_manager/cap_04.md
    181: [...] For specifics on how to master the art of giving feedback, see the next chapter.

**`ser_honesto_transparente_desempenio` tiene 7 pasos y el 7 acaba ANTES de esa frase**,
comprobado por mi. **El libro remite y tu nodo no lo dice.**

**MI CASO, y el corte lo decides tu:** `L181` **nombra el capitulo, no el nodo**, asi que
**por `D.37` no pasa** y no es arista de serie. Es lectura de `D.29`, y su destino correcto
**es la cabeza del capitulo siguiente**, `elegir_forma_inspirar_cambio_conducta`, que es
adonde el libro manda. **Leelo, decide, y escribe tu razon saque arista o no.**

> **LO QUE NO HACES: no tocas `P.19`.** Se lo he pedido a Alexis por segunda vez, ahora con
> dos casos medidos (ACTA 10 seccion 10, punto 3). **Mientras tanto sigue valiendo lo que
> haces: no duplicar.**

#### 2.b. Los dos pasos de dos capitulos con la misma orden y sin cable

`despedir_persona_respeto_franqueza` **paso 2** dice *no lo abras a discusion, porque no lo
es* (`cap_04.md` `L313`), y `dar_mala_noticia_decision_tomada` **paso 2** dice *se firme y
no la abras a discusion* (`cap_05.md` `L273`). **Dos lineas de dos capitulos con la misma
orden, y entre esos dos nodos no hay arista.**

**Y CORRIJO AQUI UNA COSA MIA, sin borrarla:** a ciegas escribi que el racimo del despido
tenia *CERO aristas entre sus cuatro nodos*. **Eran cuatro**, y esta en el ACTA 10 6.3 con
mi nombre. **Lo que si sigue en pie es este par concreto, y solo este.**

#### 2.c. Los cuatro pasos que son el indice de los dos capitulos que acabas de minar

`gestionar_personas_equipo`, que escribiste en la vuelta 9, tiene estos pasos:

    2  Desarrolla relaciones de confianza con ellos.
    3  Entiende las fuerzas y las debilidades de cada uno, y tambien las tuyas.
    4  Toma buenas decisiones sobre quien debe hacer que, y eso incluye contratar y despedir.
    5  Entrena a cada persona para que de lo mejor de si.

**Los cuatro apuntan a nodos que ya existen en la bandeja**, y **ninguno tiene arista.**
**No te digo cuales pasan `D.37` y cuales no: eso lo mide el que corre el test**, y el test
lo corres tu abriendo el paso y viendo si nombra al hijo. **Lo que te digo es que los
mires los cuatro y escribas el resultado, pase o no pase cada uno.**

**Y EL CIERRE DEL `cap_04.md` te da una pista que no es una orden:**

    L321: Great managers are excellent coaches, and the secret sauce to coaching is the
          topic of our next chapter - giving effective feedback.

### TAREA 3. EL Cap. 5, `Managing Yourself` (`cap_06.md`), CON SU FRONTERA ANTES DE CORTAR

**Antes de la primera operacion, las comprobaciones de apertura con su salida pegada**
(`D.35`): **gate, barrido, 72 pruebas y `rancios`. Esperado: 52 nodos, 37 aristas, 72 de
72, 60 veredictos.** Los reconte yo hoy y dan eso. **Si no cuadra, lo declaras y no sigues
hasta explicarlo.**

**Y las palabras del fichero, contadas por ti.** Si `cap_06.md` no da **9.617** de cuerpo,
**declaras la discrepancia y no eliges en silencio.**

**LA FRONTERA SE PUBLICA ANTES Y SE COMMITEA ANTES**, con el metodo que ya te ha funcionado
tres veces: **recorrido por cobertura y no lista de cabeceras**, con huecos, solapes y suma
de palabras impresos. **Recompute tus 44 piezas de la vuelta 10 PALABRA A PALABRA, no solo
la suma, y salieron 44 de 44 exactas.** No cambies nada de ese metodo.

**Despues los candidatos, uno a uno**, con:

- **la aduana en el mismo acto de escribir cada uno** (`EXTRACTOR.md` 16). **Te salvo de
  la caida de la `3.7` de la vuelta 10 y lo dijiste tu: si la hubieras corrido al final del
  capitulo, el mismo fallo te habria costado el lote;**
- **la relectura de fidelidad DENTRO del acto de escribir** (`D.30`), **y con el aviso que
  sale de mi residuo de esta vuelta: el paso 1 y el paso 7 del MISMO nodo tenian la misma
  averia, cazaste el 7 y no el 1.** La relectura que empieza por donde el libro narra en
  primera persona **tiene que llegar hasta el primer paso, que es donde el nodo arranca y
  donde el ojo ya se ha ido**;
- **`D.27` pieza a pieza**, con el fallo publicado y su cita, **tambien para lo que
  descartas**;
- **la comprobacion de ORDEN** sobre los nodos con estructura de *si A, si B, si C*, que en
  la vuelta 10 diste 15 de 15 sin un desorden;
- **y el cruce de la `1.a`**: cada linea citada contra el rango de las piezas de su fila.

**Cuando la aduana levante un vecino: lo lees, escribes el veredicto con su razon y
sigues.** Eso no es una parada, es la aduana funcionando. **Van 50 de 50 sin levantar
ninguno; el primero llegara y no es un problema.** **El choque sigue anunciado para
`cap_08.md`, que es `Hiring Well` y es el Cap. 7 y no el Cap. 8**, leido del campo
`unidad`. **No es de esta vuelta.**

### TAREA 4. EL INFORME, LOS COMMITS Y EL CIERRE CON SUS CUATRO MEDIDAS

    python forja.py informe --carpeta cuarentena/zhuo_manager

**AVISO DE RELOJ, Y ES UNA DISCREPANCIA DECLARADA Y NO RESUELTA:** tu cronometraste **27
minutos** sobre los 50 candidatos. **La misma corrida, sobre los mismos 50 ficheros y en la
misma maquina, paso de mas de 90 minutos sin terminarme a mi** (ACTA 10 9.1). **No se cual de los
dos relojes describe el caso normal y no lo adivino.** **Lanzala lo primero de todo, y si
no llega a tiempo, di lo que tienes, di que no llego, y NO prometas una seccion para ella.**

**Y LO QUE ESTO SIGNIFICA PARA EL SALDO DE LA VUELTA 10: tu `50 / 0 / 0 / 0` queda
A VERIFICAR y lo verifica esta vuelta.** Lo que si pude medir yo y queda firmado: **50 ids
distintos, 50 de 50 con el `id` igual al nombre de fichero, cero colisiones con los 52 del
grafo, y las dos guardas del saldo mordiendo por mutacion con su control.**

**UN COMMIT POR UNIDAD, con los JSON dentro** (`D.25`), y su mensaje con la cifra.
**CERO INSERCIONES** (`D.26`).

**LAS CUATRO MEDIDAS, DESGLOSADAS POR CAPITULO Y NO POR VUELTA** (`AUDITOR_FORJA.md` 8):

1. **candidatos por mil palabras**, con los dos denominadores. **La columna de lo minado
   volvio a decir algo util en la vuelta 10** (94,4 y 89,2 contra el 73,7 del Cap. 1).
   Repitela.
2. **`PASOS INVENTADOS SOBRE PASOS ESCRITOS`, una fila por capitulo y ademas el total**,
   con el capitulo por nombre leido del campo `unidad` y el fichero al lado.
3. **veredictos escritos**, con su origen. Si son cero, **las razones que lo hacen
   imposible**, como has hecho tres veces.
4. **cuanto tardo**, leido de git, **y comparando la misma medida con la misma.** La
   vuelta 10 tardo **1 h 32 min 46 s** de `987dc73` a `2b0c5ab`, medido por mi; tu
   publicaste **1 h 31 min 55 s** midiendo hasta `3080ded`, **y lo declaraste como lo que
   era, una punta que aun no existia.** Esta bien hecho: la diferencia es de 51 segundos y
   de metodo declarado, no de cifra.

**Y LAS DOS CIFRAS A VIGILAR:**

- **la tendencia local de la tasa de puentes.** La serie va **3,09 / 5,00 / 5,56 / 3,80 /
  5,26 / 2,50 / 0,90**, y **con la banda del ACTA 10 las dos ultimas son 3,33 y 1,80.**
  **Escribe la fila nueva con su cociente y sin suavizar**, y di si la bajada es de
  numerador o de denominador, como hiciste bien en tu `5.d`.
- **LA TASA DE ATRIBUCION, que mido yo por primera vez y te paso para que tengas contra
  que comparar**, no como regla: **18,3 por ciento de los pasos del Cap. 3 y 26,1 del
  Cap. 4** llevan dentro una marca de atribucion. **Si el Cap. 5 sube mucho de ahi con la
  tasa de puentes plana, el que se esta moviendo eres tu y no el libro.** **Es una nota, no
  una medida obligatoria**, y si merece serlo lo decide Alexis (se lo he pedido).

---

## LO QUE **NO** ES DE ESTA VUELTA, dicho para que no lo intentes

- **No insertas nada.** Ni los 50 de `zhuo_manager` ni los 15 de `smart_who`. La
  autorizacion es del fundador (`D.26`) y **es la tercera acta que la pide.**
- **No tocas `cuarentena/smart_who/`.** Esta cerrado.
- **No abres `cap_07.md` en adelante**, salvo su cabecera para comprobar el borde del
  Cap. 5.
- **El `cap_12.md` es el `Epilogue` y se juzga antes de cortarse** cuando toque. **No es un
  indice**, y mi encargo anterior se equivoco al llamarlo asi.
- **Ni umbrales, ni reglas de id, ni esquema, ni `D.27`, ni `D.37`, ni `P.19`, ni la vara
  de continua contra repite.** Ninguna vuelta las mueve. **Y `D.27` no se ha movido hoy:
  lo que adjudique en el ACTA 10 3.2 es que su modo de fallo no se daba en ese caso.**
- **Y NO FABRICAS MAQUINARIA** (`EXTRACTOR.md` 13). **En particular no propongas una guarda
  que cruce piezas con citas.** El cruce de la `1.a` es una comparacion mas dentro de la
  relectura que ya corres, **y esa es toda la maquinaria que hay.**

## LAS PARADAS

**Paras, lo declaras en TU REPORTE y te detienes si:**

- una regla de la casa te obliga a algo que rompe otra regla de la casa;
- necesitas mover un umbral, una regla de id, el esquema, `D.27`, `D.37`, `P.19` o la vara;
- alguna comprobacion de apertura de la TAREA 3 falla.

**NO paras por:** que un candidato caiga en la aduana (lo corriges y pegas la salida), que
la aduana levante vecinos (los lees y escribes el veredicto), que la lectura de la TAREA 2
salga en contra de mi caso (la escribes con su razon y se acabo), que `cap_06.md` de mas de
quince candidatos (**eso es un dato del libro y lo quiero escrito con su cifra**), ni por
que no te de tiempo a la unidad entera (**cierras lo que tengas, lo dices con su cifra, y
el disparador de `12.4` hace su trabajo**).

**TU NO ESCRIBES `docs/loop/PARA_ALEXIS.md`** (`D.28`). Eso lo hace el auditor.

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una
regla vigente, paras y lo traes. No adivines.**
