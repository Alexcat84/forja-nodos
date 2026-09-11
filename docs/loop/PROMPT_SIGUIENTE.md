# ENCARGO DE LA VUELTA 10: **EL Cap. 3 Y EL Cap. 4 DE `zhuo_manager`, Y LA COLA QUE DEJA LA 9**

*Escrito por el auditor al cerrar el ACTA 9, con su linea leida del instrumento y pegada
aqui como manda la TAREA 1.a de este mismo encargo:*

    $ grep -n "^# ACTA" docs/loop/ACTA_AUDITOR.md | tail -1
    7659:# ACTA 9. VUELTA 9, lote 3 (`zhuo_manager`), apertura del libro: Introduction, Cap. 1 y Cap. 2

**El lote 3 sigue ABIERTO: nueve ficheros y 56.355 palabras sin tocar.** Esta acta no
cierra lote, asi que **no hay apertura de lote que medir** (`D.32`) y esta vuelta es la
continuacion del mismo libro.

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO PRIMERO: TUS RACHAS, MEDIDAS Y NO SUPUESTAS

    racha CLASE           : 0 de 2     nueve tandas sin ninguna
    racha CIFRA PUBLICADA : 0 de 2     nueve tandas sin ninguna
    racha REPORTE         : 2 de 3     LA VUELTA 9 SUMO LA SEGUNDA. ESTAS A UNA DE PARAR

    y la mia, que no se mezcla con la tuya:
    racha REMEDIO ROTO del auditor : 1 de 3   la vuelta 9 la abri yo, y esta en mi ACTA 9 seccion 6.1

**LA VUELTA 9 FUE UNA VUELTA MUY BUENA Y AUN ASI SUMO, y las dos mitades se dicen juntas.**

**Lo que salio bien, medido por mi y no dicho por cortesia:**

- **Cuatro discutibles marcados y los cuatro SOSTENIDOS.** Tercera tanda seguida con cero
  caidas dentro del marcado.
- **Las fronteras reproducen EXACTO.** Recompute tus 39 rangos con codigo mio: 142 de 142
  y 111 de 111 lineas cubiertas, cero huecos, cero solapes, y las sumas de palabras dan
  6.477 y 4.292 al numero. **Publicar la frontera antes de cortar y commitearla funciono.**
- **El mapa de los doce da 70.041 contado por mi.** Diferencia cero.
- **El remedio 1.a se cazo el solo siete punteros desfasados** (tu 5.c.bis), y lo
  declaraste en vez de callarlo. **Eso es exactamente para lo que nacio.**
- **En la unica comparacion directa que hubo entre tu lectura y la mia a ciegas, cayo la
  mia.** El DISCUTIBLE 4 esta bien resuelto y la vara que usaste es textual.

**Y LA CAIDA, que esta donde no miraste y es la segunda seguida de esa forma:**

> **PROMETISTE UNA PRUEBA EN UNA SEDE QUE NUNCA ESCRIBISTE.** La ultima linea de tu
> reporte dice *"el bloque `EL SALDO` de la segunda corrida se pega en 5.g.bis"*, y
> **`5.g.bis` no existe**: `grep -n "5.g.bis"` da una sola linea, la de la promesa.

**LA CIFRA ERA VERDAD.** Re corri el informe entero yo mismo, sin recorte, y da
**21 ENTRARIAN, 0 BLOQUEARIAN, 0 CAERIAN, 0 CHOCAN**, con la lista de 21 identica a la
tuya. **Lo que faltaba era la prueba, no el numero.** Pero **una cifra cierta sin su
prueba sigue siendo una cifra que nadie puede auditar**, y por 7.B de la cosecha
(*la ruta que promete prueba es cifra*) **acumula**. La adjudicacion entera, con el cruce
de reglas declarado y con la puerta abierta a que Alexis la revoque, esta en el ACTA 9
seccion 4.1.

---

## TAREA 1. LOS REGISTROS DEL ACTA 9, Y SU PUNTO 1.a ES BLOQUEANTE

### 1.a. **BLOQUEANTE: EL REMEDIO, Y ES `D.35` OTRO PASO AL LADO**

*Se encarga aqui y no se declara y ya, porque mi seccion 1.4 dice que la escalada se
encarga cuando la racha llega al penultimo escalon, y **declararla sin encargarla seria
una caida propia mia.** **No es doctrina nueva y no es maquinaria** (moratoria,
`EXTRACTOR.md` 13): es un `grep` sobre un fichero que ya escribes.*

> **1. NINGUNA PROMESA DE PEGAR UNA SALIDA MAS ABAJO SE ESCRIBE SIN CUMPLIRLA EN EL MISMO
> COMMIT.** Si la salida todavia no esta, **no se anuncia la sede: se deja el hueco dicho
> sin nombre de seccion**, o se espera.
>
> **2. Y AL CERRAR EL REPORTE, UN `grep -n` DE CADA ANCLA PROMETIDA CONTRA EL PROPIO
> REPORTE, CON SU SALIDA PEGADA.** Una tabla de dos columnas basta:

    | lo que prometi | la salida de `grep -n`, pegada |
    |---|---|
    | <el ancla> | <la linea que la promete> y <la linea que la cumple> |

**La tabla de arriba es la FORMA, no un ejemplo con cifras: no teclees numeros de linea
inventados ni siquiera de muestra.** Las dos columnas se llenan con lo que salga.

**Y LOS TRES DEL ENCARGO ANTERIOR SIGUEN VIVOS, porque los tres funcionaron y ninguno se
retira:** la cifra de vuelta anterior con su `grep` pegado al lado; la comparacion que sale
CERO se escribe CERO y no se borra la fila; y toda tabla que compara N filas dice de donde
salen las N con la cuenta hecha. **Los usaste bien en la vuelta 9 y se nota.**

### 1.b. Las adjudicaciones que te afectan, para que no las vuelvas a plantear

| # | lo adjudicado | donde |
|---:|---|---|
| 1 | **El racimo de `cap_01.md` L97 se queda fuera. SOSTENIDO**, y a ciegas lo lei igual | ACTA 9, 3.1 |
| 2 | **Las cinco condiciones de Hackman se quedan fuera. SOSTENIDO** por `P.5.1`, y a ciegas lo lei igual | 3.2 |
| 3 | **Un nodo para los motivos y cabeza mas tres para las preguntas. SOSTENIDO.** Partir por la riqueza de las partes y no por la forma **es leer, y `D.19` manda leer** | 3.3 |
| 4 | **Las cuatro listas de preguntas a nodo propio y las dos del pionero dentro. SOSTENIDO. Y aqui cai yo**, que a ciegas sostuve lo contrario argumentando por forma, que `D.19` me prohibe. **Tu vara es textual: `in preparation` y `ask yourself` contra `ask your reports` y `Questions to discuss`** | 3.4 |
| 5 | **`P.19` no cubre la remision entre capitulos, y tienes razon en tu PROPUESTA 2.** Pero **lo que `P.19` si decide, lo decide bien: no fabricaste gemelos, y fabricarlos habria sido la averia gorda** | 3.7 |
| 6 | **`0 CAERIAN` es un cero medido.** Hice caer la guarda por mutacion (un campo de `fuentes`) y muerde, con su control al lado | 1.6 |
| 7 | **Tu tabla 5.b desglosa por capitulo y nombra bien las tres filas. CERO caida de 8.3.3**, y en este libro el nombre se lee del campo `unidad` | 7.1 y 7.3 |

### 1.c. Las correcciones declaradas, sin borrar nada

**No reescribes el tramo de la vuelta 9.** Abres tu vuelta 10 por anexion
(`EXTRACTOR.md` 3) y **en tu apertura pones un bloque que diga:**

- que **`5.g.bis` nunca se escribio**, que el auditor re corrio el informe y que el saldo
  es **21 / 0 / 0 / 0**, con su bloque pegado ahora en tu vuelta 10;
- que **las quince aristas de serie de la vuelta 9 son DIEZ por `D.37`**, y que las otras
  cinco **no pasan el test de `D.37`** y quedan como candidatas a `D.29` (TAREA 2.c);
- que **la tasa del Cap. 2 lleva banda**: 4 de 76 declarados, **hasta 6 de 76 contando el
  residuo que el auditor sostiene y el quinto que tu corregiste por precaucion**, es decir
  **de 5,26 a 7,89 por ciento**. **Ninguna lectura cambia la decision de volumen.**

### 1.d. Un registro de `docs/`, y solo la columna que digo

`docs/loop/ORDEN_DE_LOTES.md` tiene el `estado` del lote 2 en **`ABIERTO. Dos capitulos
por vuelta`** y el del lote 3 **vacio**, y los dos son falsos hoy. **Actualiza SOLO la
columna `estado`**, por correccion declarada y **sin borrar el texto viejo**, con su
commit de respaldo:

- lote 2, `smart_who`: **cerrado en extraccion** (ACTA 8 seccion 10), **15 candidatos en
  cuarentena sin insertar**, seis capitulos minados;
- lote 3, `zhuo_manager`: **ABIERTO**, 3 de 12 ficheros minados, 21 candidatos en
  cuarentena, **esta vuelta corre a dos unidades**.

> **NO TOCAS NI EL ORDEN, NI LAS CLAVES, NI LA CUENTA DE CAPITULOS, NI LAS PALABRAS.** Eso
> lo fija `D.24` y **no lo elige el bucle.** Si algo mas de esa tabla te parece falso, **lo
> declaras y no lo tocas.**

---

## EL TRAMO DE ESTA VUELTA: **DOS UNIDADES, Y DIGO DE DONDE SALE**

| unidad | fichero | palabras | lo que es |
|---|---|---:|---|
| **Cap. 3, `Leading a Small Team`** | `cap_04.md` | **7.237** | |
| **Cap. 4, `The Art of Feedback`** | `cap_05.md` | **6.318** | |
| | | **13.555** | |

**BAJO DE TRES UNIDADES A DOS Y NO MUEVO NINGUNA REGLA. Las tres razones, con su cifra:**

1. **A IGUALDAD DE PALABRAS.** La vuelta 9 abrio **13.686** palabras y esta abre **13.555**:
   **131 menos.** El tramo se fijo en unidades y **lo que produce candidatos son palabras y
   densidad, no la cuenta de ficheros.** Las tres siguientes habrian sido 23.172, un 69 por
   ciento mas.
2. **21 CANDIDATOS CONTRA UNA BANDA DE CINCO A QUINCE** (`EXTRACTOR.md` 12.4). El ACTA 8
   ya adjudico que **la banda no te bloquea**, y sigue sin bloquearte. Pero la regla madre
   de esa banda es **la parada de la bateria sin techo del 5 sep 2026**, *donde el bucle
   producia trabajo bueno que no cabia en una vuelta*, **y eso es literalmente lo que
   describiste tu en tu 5.h.** Lo recojo.
3. **ESTA VUELTA LLEVA CARGA DE ARRASTRE.** La TAREA 2 entera es cola de la vuelta 9.

**EL DISPARADOR DE 12.4 NO SE ARMO:** tu reporte cerro con sus cuatro medidas. **Esta
bajada no es un castigo y no la escribas como tal:** es el que fija el tramo usando el dato
que tu le diste.

**LO QUE MEDI YO DE LOS DOS FICHEROS, Y TE REGALO.** Cabecera y ultima linea con texto,
leidas por mi hoy:

    cap_04.md   unidad: Cap. 3   titulo_textual: Leading a Small Team   L9: Chapter Three
                ultima con texto: L321 de 321, y cierra anunciando el capitulo siguiente
    cap_05.md   unidad: Cap. 4   titulo_textual: The Art of Feedback    L9: Chapter Four
                ultima con texto: L289 de 289, y cierra con la frase de los posteres
    cap_06.md   unidad: Cap. 5   (el borde por el otro lado: abre unidad nueva)

> **ES UNA NOTA PREVIA Y SE CONTRASTA, NO SE COPIA** (`EXTRACTOR.md` 5). **Comprueba los
> dos cierres tu, y el borde del `cap_06`, y pega tus salidas.** Y recuerda el aviso de tu
> propia vuelta 9: **las cabeceras de este libro no llevan almohadilla; se distinguen
> porque son las unicas lineas del cuerpo sin sangrado de tabulador.**

---

## LAS TAREAS

### TAREA 2. LA COLA DE LA VUELTA 9, Y VA ANTES QUE EL LIBRO NUEVO

**Son cuatro cosas sobre `cuarentena/zhuo_manager/`, que sigue en 21 ficheros y sin
insertar.** Ninguna toca el grafo: **CERO inserciones** (`D.26`).

#### 2.a. El puente residual, corregido

`acordar_plan_conjunto_jefe` **paso 8**. El paso ordena *cuenta con tu jefe como caja de
resonancia constante*, y `L47` **cuenta lo que Rebekah fue para la autora, en primera
persona del pasado, y no manda nada.** **Es la especie exacta de tus puentes 5 y 7, que
cazaste y corregiste en el mismo capitulo.** Corrigelo como corregiste aquellos: **dejando
dentro de quien es la experiencia.** Y **suma el caso a tu cuenta de `D.30` de la vuelta 9
en tu bloque de correccion**, que es lo que la metrica pide (`D.30` cuenta lo escrito, no
lo que sobrevive).

**Y RELEE ESTOS DOS, que declaro y no cuento**, porque son decision tuya y no mia:
`alinear_equipo_proposito_comun` paso 1 y `fijar_proceso_trabajo_equipo` paso 1 abren los
dos con **`Escribe`**, y `L127` y `L139` **definen** sin mandar escribir nada. **Mi
lectura es que cambian el modo verbal y no el contenido, y que una definicion que entra en
un nodo sale en imperativo por construccion.** **Leelos con tu vara y declara lo que
decidas, cuentes o no cuentes.**

#### 2.b. La cita colgada del motivo equivocado

`contrastar_motivos_querer_gestionar` **paso 7** dice *la leccion con la que el libro
cierra **este motivo***, y va detras del paso 6, que es *me lo han pedido*. **Esa frase es
`L259` y cierra `I Want Freedom to Call the Shots`, que es tu paso 5.**

**No es puente: la frase existe y esta bien traducida. Es el ORDEN.** Y lo notable es que
**tu propio reporte la atribuye bien** en la tabla del DISCUTIBLE 3. **Mueve el paso 7
detras del paso 5, o ancla la leccion en su motivo dentro del propio texto del paso.**

> **Y ESCRIBE LA LECCION EN TU CIERRE, porque vale para todo el libro:** en un nodo cuya
> estructura es *si la respuesta es A, si la respuesta es B, si la respuesta es C*, **una
> pasada de fidelidad paso a paso NO caza este fallo**, porque cada paso por separado es
> fiel. **Lo que falla es el orden, y el orden se comprueba leyendo el nodo entero de un
> tiron contra la seccion entera.**

#### 2.c. Las cinco aristas que no pasan el test de `D.37`

`D.37` le da su test al auditor: **abrir el paso `n` de la madre y comprobar que ahi se
nombra al hijo.** Lo corri sobre las quince. **Diez pasan. Cinco no:**

| madre, paso | hijo | lo que dice el paso |
|---|---|---|
| `contrastar_motivos_querer_gestionar` 6 | `probar_gestion_antes_decidir` | *si de verdad quieres*. No nombra el probar |
| `transitar_aprendiz_primeros_meses` 1 | `acordar_plan_conjunto_jefe` | *vas a tener mas guia*. No nombra el plan conjunto |
| `transitar_aprendiz_primeros_meses` 2 | `listar_bueno_mejorable_equipo` | *sabes lo que funciona*. No nombra las dos listas |
| `transitar_jefe_nuevo_equipo_establecido` 7 | `preguntar_jefe_sonado_persona_cargo` | nombra la clase de relacion. No enumera las preguntas |
| `transitar_jefe_nuevo_equipo_establecido` 9 | `calibrar_normalidad_preguntas_jefe` | *escuchar, preguntar y aprender*. No nombra la calibracion |

**NO LAS BORRES.** Marca las cinco en tu reporte como **no declarables por `D.37`** y, si
sostienes alguna, **reescribela como lectura de `D.29`, con su razon escrita**, para el
acto de insertar. **Diez de serie mas cinco de lectura no es lo mismo que quince de
serie**, y la diferencia es la que el auditor de la insercion tendra que leer.

**ESTO NO ES UNA CAIDA TUYA Y ESTA DICHO EN EL ACTA 9 seccion 3.6:** tu nombraste la
debilidad de las cinco antes que yo, una a una, y de la primera escribiste *si el auditor
la tumba, es la que yo tumbaria.* **Acertaste.**

#### 2.d. LA RELECTURA CONJUNTA: **dos piezas del aprendiz que el libro cita por su nombre**

*Mi seccion 1.3: la discrepancia va a relectura conjunta, mi caso escrito con evidencia,
**tu verificas contra el libro y el grafo y decides con la vara**, y la correccion se
declara sin borrar.* **Yo adjudico el criterio; el corte lo decides tu con el libro
delante.**

**MI CASO, en cuatro lineas y con sus citas:**

1. **El libro las invoca por su titulo desde otras dos secciones**, que es lo que un id
   es: `L135` y `L207`, las dos *See description from "The Apprentice"*.
2. **Por el criterio que tu mismo sostuviste en el DISCUTIBLE 4** (encargo propio mas
   entregable propio), **las dos lo cumplen**, y la del equilibrio con mas derecho que
   tres de las cuatro listas que si sacaste: `L93` trae **disparador numerico**
   (*at the point in which your team becomes four or five people*), **acto** (*you should
   have a plan*) **y entregable** (*el plan*).
3. **Hoy esa invocacion vive como prosa**: `transitar_pionero_equipo_nuevo` paso 10 y
   `transitar_sucesor_equipo_entero` paso 3 **remiten y no accionan**. Con id propio serian
   **dos aristas**, que es su forma correcta. (El paso 2 del sucesor **si acciona**:
   transcribe las dos ventajas ademas de remitir. **Son dos, no tres**, y esa es una
   correccion de mi propia apertura.)
4. **La del equilibrio es la fuerte y la sostengo sin matices. La de la dinamica con
   antiguos pares es mas arguable y lo digo**: es una serie de tres con cabeza, y sacarla
   reabre el DISCUTIBLE 3 en su peor forma. **No inflo mi caso.**

**LO QUE HACES:** las relees contra `cap_03.md` L71 a L93, **decides con la vara, y lo
declaras con su razon, saquen o no saquen id propio.** Si salen, son **dos candidatos
nuevos** mas las aristas correspondientes escritas y no declaradas, y
`transitar_aprendiz_primeros_meses` pierde los pasos que se van. **Si no salen, escribes
por que y se acabo: una frontera decidida con el texto delante es trabajo hecho.**

> **LO QUE NO HACES: no tocas `P.19`.** Mi adjudicacion es por `D.27` mas el criterio del
> DISCUTIBLE 4. **Si `P.19` necesita una linea para la remision entre capitulos lo decide
> Alexis, y se lo he pedido** (ACTA 9 seccion 10, punto 2). **Mientras tanto sigue valiendo
> lo que hiciste: no duplicar.**

### TAREA 3. EL Cap. 3, `Leading a Small Team` (`cap_04.md`), CON SU FRONTERA ANTES DE CORTAR

**Antes de la primera operacion, las comprobaciones de apertura con su salida pegada**
(`D.35`): **gate, barrido, 72 pruebas y `rancios`. Esperado: 52 nodos, 37 aristas, 72 de
72, 60 veredictos.** Los reconte yo hoy y dan eso. **Si no cuadra, lo declaras y no sigues
hasta explicarlo.**

**Y las palabras del fichero, contadas por ti.** Si `cap_04.md` no da **7.237** de cuerpo,
**declaras la discrepancia y no eliges en silencio.**

**LA FRONTERA SE PUBLICA ANTES Y SE COMMITEA ANTES**, con el metodo que ya te funciono dos
veces: **recorrido por cobertura y no lista de cabeceras**, con huecos, solapes y suma de
palabras impresos. **Yo recompute tus 39 rangos de la vuelta 9 y salieron exactos**, asi
que no cambies nada de ese metodo.

**Despues los candidatos, uno a uno**, con:

- **la aduana en el mismo acto de escribir cada uno** (`EXTRACTOR.md` 16);
- **la relectura de fidelidad DENTRO del acto de escribir** (`D.30`, `EXTRACTOR.md` 15.4),
  **y con el aviso que sale de tu propia vuelta 9 y del residuo que yo encontre:**
  **los siete puentes y el residuo son todos de la misma especie y del mismo sitio, donde
  el libro habla en primera persona del pasado o cita a un tercero.** Ese es el sitio.
- **`D.27` pieza a pieza**, con el fallo publicado y su cita, **tambien para lo que
  descartas**;
- **y la comprobacion de ORDEN de la 2.b**: cada nodo con estructura de *si A, si B, si C*
  se lee entero de un tiron contra su seccion entera, no solo paso a paso.

### TAREA 4. EL Cap. 4, `The Art of Feedback` (`cap_05.md`), IGUAL, Y CON UN AVISO

**Mismo procedimiento entero.** Y dos avisos que te doy antes y no cuando estorben:

1. **ES EL CAPITULO CON MAS NARRACION EN PRIMERA PERSONA QUE HAS ABIERTO DE ESTE LIBRO**,
   por su asunto: dar opinion se ensenia contando casos. **Ahi es donde tus siete puentes y
   mi residuo aparecieron.** No te pido que bajes la tasa: **te pido que la mires donde
   sabemos que vive.**
2. **`cap_08.md` es `Hiring Well` y va a chocar con las 44 fichas de `smart_who` del
   grafo.** **No es de esta vuelta.** Va escrito para que la vuelta que lo abra lo sepa
   antes y no despues, como ya dejaste tu escrito en tu 5.i.

**Cuando la aduana levante un vecino: lo lees, escribes el veredicto con su razon y
sigues.** Eso no es una parada, es la aduana funcionando. **Van 21 de 21 sin levantar
ninguno; el primero llegara y no es un problema.**

**`D.37` otra vez, y con el filtro de la 2.c ya puesto:** si un capitulo trae una serie que
el titulo enumera, **la arista se escribe en tu reporte con madre, paso e hijo, y NO se
declara** (`MODO_INSERCION=cuarentena`). **Y antes de escribirla, correle el test: abre el
paso de la madre y comprueba que ahi se nombra al hijo.** Si no lo nombra, **no la llames
de serie: llamala lectura de `D.29` y escribe su razon.**

### TAREA 5. EL INFORME, LOS COMMITS Y EL CIERRE CON SUS CUATRO MEDIDAS

    python forja.py informe --carpeta cuarentena/zhuo_manager

**AVISO DE RELOJ, medido por mi hoy:** esa corrida sobre 21 candidatos **tardo mas de
treinta minutos**. Con los del Cap. 3 y el Cap. 4 dentro seran mas. **Lanzala pronto y no
al final**, y **si su salida no llega a tiempo, NO prometas una seccion para ella**: esa es
exactamente la caida de la vuelta 9 (TAREA 1.a). **Di lo que tienes y donde esta.**

**UN COMMIT POR UNIDAD, con los JSON dentro** (`D.25`), y su mensaje con la cifra.
**CERO INSERCIONES** (`D.26`).

**LAS CUATRO MEDIDAS, DESGLOSADAS POR CAPITULO Y NO POR VUELTA** (`AUDITOR_FORJA.md` 8):

1. **candidatos por mil palabras**, con los dos denominadores. **La columna de lo minado de
   tu vuelta 9 fue util y se nota: dijo por que el Cap. 1 descarta mas.** Repitela.
2. **`PASOS INVENTADOS SOBRE PASOS ESCRITOS`, una fila por capitulo y ademas el total**,
   con el capitulo por nombre y el fichero al lado. **En este libro el nombre se lee del
   campo `unidad`**, asi que aqui no hay excusa.
3. **veredictos escritos**, con su origen. Si son cero, **las razones que lo hacen
   imposible**, como hiciste.
4. **cuanto tardo**, leido de git, **y comparando la misma medida con la misma medida.**

**Y LAS DOS CIFRAS A VIGILAR:**

- **la tendencia local de la tasa de puentes.** La serie va **3,09 / 5,00 / 5,56 / 3,80 /
  5,26**: **la racha de tres subidas se rompio** y lo que queda es oscilacion entre 3 y
  5,6. **Escribe las filas nuevas con su cociente y sin suavizar.**
- **cuantos candidatos salen de 13.555 palabras.** Si vuelven a salir mas de quince,
  **eso es un dato del libro y no un fallo tuyo**, y lo quiero escrito con su cifra para
  fijar la vuelta 11.

---

## LO QUE **NO** ES DE ESTA VUELTA, dicho para que no lo intentes

- **No insertas nada.** Ni los 21 de `zhuo_manager` ni los 15 de `smart_who`. La
  autorizacion es del fundador (`D.26`) y esta pedida en el ACTA 9 seccion 10.
- **No tocas `cuarentena/smart_who/`.** Esta cerrado.
- **No abres `cap_06.md` en adelante**, salvo su cabecera para comprobar el borde del
  Cap. 4.
- **El `cap_12.md` se juzga antes de cortarse** cuando toque: 449 lineas para 3.511
  palabras es un `Index`, como tu mismo mediste.
- **Ni umbrales, ni reglas de id, ni esquema, ni `D.27`, ni `D.37`, ni `P.19`, ni la vara
  de continua contra repite.** Ninguna vuelta las mueve.
- **Y NO FABRICAS MAQUINARIA** (`EXTRACTOR.md` 13). **En particular no propongas una guarda
  que compruebe anclas prometidas.** El remedio de 1.a es un `grep` sobre un fichero que ya
  escribes, y esa es toda la maquinaria que hay.

## LAS PARADAS

**Paras, lo declaras en TU REPORTE y te detienes si:**

- una regla de la casa te obliga a algo que rompe otra regla de la casa;
- necesitas mover un umbral, una regla de id, el esquema, `D.27`, `D.37`, `P.19` o la vara;
- alguna comprobacion de apertura de la TAREA 3 falla.

**NO paras por:** que un candidato caiga en la aduana (lo corriges y pegas la salida), que
la aduana levante vecinos (los lees y escribes el veredicto), que la relectura conjunta de
la 2.d salga en contra de mi caso (la escribes con su razon y se acabo), que una unidad no
de ni un procedimiento (se dice con su razon), ni por que no te de tiempo a las dos
unidades (**cierras lo que tengas, lo dices con su cifra, y el disparador de `12.4` hace su
trabajo**).

**TU NO ESCRIBES `docs/loop/PARA_ALEXIS.md`** (`D.28`). Eso lo hace el auditor.

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una
regla vigente, paras y lo traes. No adivines.**
