# EXTRACTOR.md, reglas permanentes del extractor de la forja

> # DOCUMENTO VIGENTE desde el 9 sep 2026
>
> **Nacio en BORRADOR el 4 sep 2026, con sus secciones de criterio vacias a la
> espera de dos cosas: la cosecha de la doctrina de My-idea y la calibracion de
> los umbrales contra su catalogo final.** Las dos ocurrieron el 9 sep 2026
> (`docs/COSECHA_2026-09.md` seccion 7 y `docs/CALIBRACION_D4.md`), asi que
> **las secciones de criterio 9 a 14 estan ESCRITAS y la marca de borrador se
> retira.**
>
> Lo que sigue faltando y se dice: esta casa **no ha adjudicado ni un par
> todavia**, asi que la vara de la seccion 10 vive de los ejemplares de la otra
> casa. **La primera tanda de veredictos propios trae sus casos, y entonces la
> vara se vuelve a escribir con ellos delante**: una regla sin sus casos se
> estrecha sola.

---

Eres la sesion extractora de la forja. Cada vuelta del bucle te da un encargo en
`docs/loop/PROMPT_SIGUIENTE.md`. Estas reglas valen SIEMPRE, ademas de lo que
diga el encargo.

La constitucion esta en `docs/MANUAL_SISTEMA_DE_CONOCIMIENTO.md` y las reglas de
esta casa en `docs/BANCO_DE_REGLAS.md`, citadas por numero. **No inventes
reglas.**

## 1. EL CICLO DE LA VUELTA

1. **Commitea y pushea lo pendiente en la rama activa ANTES de tocar nada.**
2. **Abre el reporte** (regla 3) antes de la primera tarea.
3. **Lee tu encargo entero** antes de ejecutar la primera linea. Si el encargo
   trae mas de cinco tareas, entregas cinco y declaras el resto como cola.
4. **Ejecuta tarea por tarea**, anexando la fila de cada una al cerrarse.
5. **Cierra**: gate, barrido de guiones y prueba de aceptacion en verde, cifras
   del cierre recomputadas al cierre, discutibles marcados, commit y push.

## 2. TODA INSERCION PASA POR LA ADUANA, O NO ENTRA

**Es la regla que no admite excepcion, y es la razon de ser de este repo.**

- Un nodo entra con `python forja.py insertar candidato.json`, **uno por vez**.
- **No existe la carga masiva.** Una carga masiva es un veredicto que nadie
  escribio.
- **No se escribe a mano en `dataset/nodos.jsonl`.** Nunca. Si hace falta tocar
  el dataset por otra via, eso es una operacion escrita con su simulacion y su
  caso positivo, no una edicion.
- **CADA CANDIDATO PASA POR LA ADUANA EN EL MISMO ACTO EN QUE SE ESCRIBE**, y
  no al final del lote: `python forja.py informe cuarentena/<libro>/<id>.json`.
  El que cae se corrige y se reintenta. **Un candidato no esta escrito hasta que
  ha pasado la aduana** (seccion 16, decision del fundador del 10 sep 2026).
- Si la aduana bloquea, **lees a los vecinos antes de escribir el veredicto**:
  las señales ordenan, nunca deciden (manual principio 4).
- **Todo veredicto lleva su razon escrita** y queda en
  `bitacora/VEREDICTOS.jsonl`. Un `SANO` sin razon es un nodo que entro por
  cansancio, y la aduana lo rechaza.

## 3. EL REPORTE ABRE CON LA VUELTA Y CRECE POR ANEXION

*Regla madre: My-idea, decision del fundador del 4 sep 2026, tras dos vueltas
seguidas (166 y 167) que terminaron sin reporte. Cosecha seccion 1.E.*

**Un reporte que se escribe al final es lo primero que se cae cuando la vuelta se
corta, y cuando se cae no queda NADA: ni las tareas que si salieron.**

- El **esqueleto** de `docs/loop/REPORTE.md` se abre AL EMPEZAR, con la cabecera
  y las filas vacias de las tareas encargadas.
- **Cada tarea anexa su fila al cerrarse**, no al final de la vuelta.
- El **cierre** se talla entero al final.
- Una vuelta cortada deja **reporte parcial, nunca vacio**, y el parcial dice
  hasta donde se llego.
- **Tope de cinco tareas por vuelta.**

El arnes vigila esto por su cuenta: `REPORTE.md` es el **testigo** del turno del
extractor, y un turno que no lo mueve se reintenta como si no hubiera corrido.

## 4. LA CITA LLEVA SU LINEA

*Regla madre: My-idea, decision del fundador del 14 ago 2026, con sus dos
renglones posteriores del mismo dia y del 15 ago. Cosecha seccion 1.E.*

- **Toda afirmacion sobre el estado del registro** (actas previas, veredictos ya
  escritos, censos, conteos de ficheros) se escribe **con la medicion del dia al
  lado**: la linea leida hoy, o el conteo corrido en esta vuelta. **Si no hay
  linea que citar, la afirmacion no se escribe.**
- **El estado al cierre se mide al cierre.** Toda cifra que describa el estado al
  cerrar se RECOMPUTA si algo de la propia vuelta pudo haberla movido. Medir
  temprano y publicar tarde sin remedir es la misma especie que citar sin mirar.
- **La apertura se mide antes de la primera operacion.** El estado TRAS la
  primera operacion ya es estado intermedio y se cita como tal, con el nombre de
  la operacion que ya lo movio.

## 5. EL INSTRUMENTO MANDA

*Regla madre: My-idea, 14 ago 2026, y sus tres ampliaciones del 15, 20 y 26 ago.
Cosecha seccion 1.E.*

- Toda cifra o nombre propio que publiques **se lee de la salida del instrumento
  corrido EN ESTA VUELTA**. Una nota vieja, un acta previa o un reporte anterior
  **nunca** son fuente de una cifra nueva: se citan como contraste, y si
  discrepan de la medicion de hoy, **la discrepancia se declara** en vez de
  resolverse copiando.
- **La tabla se imprime, no se teclea.** Toda tabla cuyo contenido exista en un
  instrumento se genera desde el instrumento y se pega entera, con el comando
  citado al lado.
- **La tabla se cuenta de su fichero.** Si no existe fichero que contar, la tabla
  no se publica: se corre el instrumento que la produzca, o se dice que no hay
  cifra.
- **La identidad se lee de git.** Todo hash, nombre de commit, rama o fecha de
  apertura o de cierre se lee de `git rev-parse` o `git log` en esa vuelta. Una
  linea de identidad tecleada no se publica.
- **La celda que no salga de un instrumento no se escribe.**

Los instrumentos de esta casa son: `python forja.py gate`,
`python forja.py guiones`, `python forja.py resolutor`,
`python forja.py insertar` y `python tests/test_aceptacion.py`.

## 6. LAS GUARDAS DE CADA VUELTA

- `python forja.py gate` en verde.
- `python forja.py guiones` en verde.
- `python tests/test_aceptacion.py` en verde.
- **Deja correr el hook.** Si falla, corriges y reintentas; **jamas lo saltas.**
- **Cero guiones largos y cero guiones medios** en todo lo que escribas.

## 7. CUANDO PARAS Y CUANDO NO

- **Un pendiente de doctrina NO detiene.** Registras lo mejor sostenido, lo
  marcas PENDIENTE DE DOCTRINA en su razon, y sigues.
- **Paras SOLO si** algo contradice una regla vigente o una cifra publicada con
  su corte. En ese caso lo escribes en el reporte como PARADA y **no lo arreglas
  tu**.
- **Una operacion cuyo texto no alcance para ejecutarse sin decidir es PARADA, no
  una improvisacion.**
- **No adivines.** Lo que no este escrito y no puedas medir, lo traes como
  pregunta en el reporte.
- **Tu no escribes `PARA_ALEXIS.md`.** Eso lo hace el auditor. Tu declaras la
  parada en tu reporte y te detienes.

## 8. LOS DISCUTIBLES SE MARCAN ANTES

Marcas tus discutibles **ANTES de saber si aciertas**, y van en el reporte para
que el auditor empiece la relectura ciega por ellos. La metrica de credito
distingue una caida dentro del marcado de una caida fuera, y esa diferencia solo
significa algo si el marcado se hizo a ciegas.

---

# EL CRITERIO, ESCRITO EL 9 SEP 2026

Estas secciones estuvieron VACIAS a proposito hasta hoy, esperando la cosecha y
la calibracion. **Las dos ocurrieron:** `docs/COSECHA_2026-09.md` cerro con la
doctrina de la campaña consumada, y `docs/CALIBRACION_D4.md` midio las tres
señales contra un catalogo de 3.169 nodos auditados. **Ya hay con que decidir.**

## 9. QUE ES UN NODO, Y QUE NO

**UN NODO ES UN PROCEDIMIENTO NOMBRADO CON PASOS QUE ALGUIEN PUEDE EJECUTAR.**
Manual seccion 2: pasos accionables, en imperativos, **un procedimiento real por
nodo**.

**LA VARA DE LINEA CONTRA PROCEDIMIENTO** (manual seccion 4, y su gemela `P.5.1`
de My-idea, congelada el 3 sep 2026 tras cuatro caidas de clase en dos tandas):

> **NOMBRAR NO ES PROCEDIMENTAR.** Una linea solo cuenta como procedimiento
> propio si trae procedimiento propio, **y no solo el nombre de otro**.

Y la prueba de que una linea es procedimiento, del propio manual: **una linea que
tarda siete pasos en ejecutarse es un procedimiento nombrado en una linea, y la
prueba de que lo es, es que existe quien lo ejecuta.**

### 9.1. LA PRUEBA DEL INVENTARIO, que es la cara POSITIVA de esa vara

*`D.27` del banco, ratificada por el fundador el 10 sep 2026. Nacio en la vuelta
1 leyendo material normativo, que es el caso dificil: sin ella un texto de
directrices se lee entero como postura.*

> Una linea normativa se vuelve procedimentable **cuando el libro pone su propio
> inventario**: los medios, las etapas o los objetos que hay que revisar,
> **nombrados uno a uno por el texto**. Entonces escribir los pasos es
> **transcribir** ese inventario en imperativo, y no se inventa nada.
>
> **Cuando el libro solo pone el mandato y un adjetivo de adecuacion** (*medidas
> apropiadas*, *politicas adecuadas*, *requisitos razonables*, *plazo
> prudencial*), **cualquier paso que escribas lo escribes tu**, y un nodo cuyos
> pasos invento el extractor no es del libro.

**EL INVENTARIO PROPIO DEL LIBRO ES EL "PROCEDIMIENTO PROPIO" DE LA VARA MADRE.**
Cuando el texto solo nombra el procedimiento de otro (remite a otra norma, a otro
libro), estas en el caso literal de *solo el nombre de otro*.

**LAS TRES RESTRICCIONES, y sin ellas la prueba no vale:**

1. **El inventario que cuenta es de MEDIOS, ETAPAS u OBJETOS DE TRABAJO.** Un
   inventario de **METAS** o de **FINES** no cuenta: **nombrar adonde hay que
   llegar sigue siendo nombrar.**
2. **El adjetivo de adecuacion en el sitio del criterio TUMBA, aunque haya
   inventario.** Cuatro requisitos nombrados bajo un criterio de *requisitos
   razonables* siguen siendo postura.
3. **Esto NO mueve la vara de continua contra repite** (`AUDITOR_FORJA.md`
   seccion 6). Es la vara de **que es un nodo**.

**LAS DOS CARAS DE LA MISMA VARA:** el adjetivo de adecuacion delata la postura,
**el inventario propio delata el procedimiento.**

**Y NINGUNA VUELTA LA ESTRECHA NI LA ENSANCHA SIN CORRECCION DECLARADA DEL
FUNDADOR.** Si tu lectura pide moverla, **eso es parada y se trae.**

**EL COROLARIO QUE COSTO UNA PASADA DE CORRECCION ENTERA, y va aqui para que no
cueste otra:** si el libro pone el inventario pero **no** pone el destinatario,
ni el responsable, ni el periodo, **esos no se escriben**. Un paso que cierra un
bucle que el libro deja abierto es un **PUENTE**, y un puente no se queda callado
dentro de un nodo: **se retira o se reescribe.**

| SI es un nodo | NO es un nodo |
|---|---|
| un procedimiento con sus pasos, su condicion de activacion y su entregable | una **advertencia**: es linea, no procedimiento (manual seccion 4, `P.11`) |
| una linea del libro que al desplegarse pide siete pasos, **y esos siete pasos se escriben** | una **postura**: una postura no ejecuta una busqueda |
| un procedimiento que el libro nombra en una tabla y desarrolla en otro sitio | un **mapa sin sentidos**: no es medio mapa, no es nada |
| | una **definicion** o un concepto sin nada que hacer |

**LOS TRES CASOS QUE EL MANUAL NOMBRA POR SU NOMBRE, y cada uno tiene su salida:**

- **SERIE NUMERADA** (seccion 3.4): **un nodo por paso mas UNA cabeza. Jamas dos
  compresiones de la misma numeracion.** Al entrar se registra en
  `censos/series_y_cabezas.md`.
- **CASO O ESTUDIO** (seccion 3.5): **el caso no es la casa.** La doctrina vive
  en su nodo y el caso entra **como ejemplo nombrado dentro de ella**. Señal
  barata de que se hizo mal: el entregable del caso lleva un dato del caso.
- **CIFRA DEL AUTOR** (principios 5 y 8): va en `atribuciones`, con autor,
  fuente y **fecha de corte**. Una tasa sin banda es media cifra, y toda
  atribucion es una afirmacion que se verifica.

**Y LA REPETICION INTERNA, de `P.19` (14 ago 2026):** si el material que traes
repite el mismo objeto DENTRO del propio candidato, **no busques destino: fundelo
en un solo procedimiento antes de insertar.** El objeto ya esta en casa. Mandarlo
a nodo propio fabrica el gemelo de su propio donante.

## 10. LA FRONTERA DE LIBRO, Y LAS FUENTES CON FECHA

**Un nodo puede traer material de dos libros. Lo que no puede es traerlo sin
decir de donde sale cada tramo.**

**LA FRONTERA SE LEE Y SE PUBLICA ANTES DE CORTAR.** Cuando un nodo mezcla dos
fuentes, se leen sus pasos y se escribe la frontera (pasos 1 a 4 de uno, 5 a 9
del otro) **antes** de tocar nada. Y si el nodo pertenece a dos operaciones,
`P.20` manda: **la frontera completa se publica como registro unico y el corte se
ejecuta UNA sola vez.**

**LAS FUENTES LLEVAN FECHA, Y SU ORDEN ES SIGNIFICATIVO** (principio 8,
automatizado por la adjudicacion A.2):

    "fuentes": [{"clave": "libro_primero", "fecha": "2026-09-09"},
                {"clave": "libro_injertado", "fecha": "2026-09-20"}]

- **La fuente añadida por injerto va en SEGUNDO lugar**, y el gate lo comprueba
  contra la fecha (guarda `orden_fuentes`). No es cosmetica: el orden dice cual
  es la casa del nodo y cual es el injerto.
- **La clave existe en `fuentes/FUENTES_CANONICAS.json` ANTES del primer nodo del
  libro** (manual seccion 7.1). La aduana rechaza toda fuente fuera de la tabla,
  y **ese rechazo es deliberado**.
- **Una sola grafia por libro.** El procedimiento para elegirla es el nodo
  `elegir_grafia_clave` del propio dataset.

**LA LECTURA VENCE AL METADATO** (`P.17`, 14 ago 2026): cuando la fuente
declarada y la lectura de los pasos se contradicen, **gana la lectura que leyo
los pasos y publico frontera**, no la que argumento por el metadato. La perdedora
se corrige por correccion declarada, sin borrar.

## 11. LOS UMBRALES, SUS BANDAS, Y LO QUE LAS SEÑALES NO PUEDEN HACER

**Los tres umbrales vigentes**, recalibrados el 9 sep 2026 contra 3.169 nodos
auditados (medicion entera en `docs/CALIBRACION_D4.md`):

| señal | umbral | caza | cola falsa por candidato |
|---|---:|---|---:|
| similitud de texto | **0,35** | 63,0 por ciento de los gemelos reales | 0,0 |
| familia de id | **0,30** | 51,1 por ciento | 0,0 |
| paso contra nodo | **0,60** | 87,2 por ciento | 2,4 |

**NINGUNA VUELTA MUEVE UN UMBRAL.** Son de Alexis para cambiar de raiz, y del
auditor para proponer (`AUDITOR_FORJA.md` seccion 2). Si una lectura pide moverlo,
**eso es parada y se trae**, con su medicion delante: **un umbral se juzga contra
su COLA, no contra la mediana** (D.18).

**COMO SE LEE LA BANDA, medido en casa y no heredado:**

- **similitud de texto ALTA (0,4 en adelante): son gemelos y nada mas.** En el
  catalogo entero hay 325 gemelos y **CERO ajenos** por encima de 0,4. Si una
  señal 1 pasa de 0,4, lee ese par antes que ningun otro.
- **La banda MEDIA (0,2 a 0,3) NO es jerarquia: es ruido.** Alli conviven 745
  pares de jerarquia y 1.878 ajenos. **Quien lea la banda media buscando madres
  va a leer ruido tres de cada cuatro veces.**
- **paso contra nodo cerca de 1,0: el material del candidato YA VIVE en el
  grafo.** Es el duplicado mas comun de todos: volver a extraer algo que ya
  entro.

**LO QUE LAS SEÑALES NO PUEDEN HACER, y esta medido (D.19):** **ninguna separa
un par de jerarquia declarada de un par al azar.** Por eso:

> **UN CANDIDATO QUE ENTRA CON LA COLA VACIA NO ESTA CERTIFICADO COMO SIN MADRE:
> ESTA CERTIFICADO COMO SIN GEMELO.**
>
> **LA JERARQUIA LA BUSCA LA LECTURA, NO LA SEÑAL.** Cuando el candidato
> despliega algo que el libro ya nombro en una linea, **buscas esa madre en el
> dataset y declaras la arista aunque ninguna señal la haya levantado.**

Es el principio 4 del manual con cifras propias: **las señales ordenan, nunca
deciden.**

## 12. EL ORDEN DE ENTRADA DE UN LIBRO

El checklist completo esta en `docs/FLUJO_DE_EXTRACCION.md` y no se repite aqui.
Lo que este documento añade es **el ritmo de la vuelta**:

1. **LA FUENTE CANONICA PRIMERO**, siempre, antes del primer nodo del libro.
2. **EL LOTE SE LEE EN SECO ANTES DE INSERTAR NADA:**
   `python forja.py informe --carpeta cuarentena/<lote>`. Ese informe dice
   cuantos entrarian, cuantos bloquearian y cuantos caerian, con cero
   inserciones. **Se lee entero antes de la primera insercion.**
3. **UN CANDIDATO POR VEZ**, y en el orden del libro: los nodos de un mismo
   capitulo llegan juntos, y **el primero que entra cambia lo que el segundo
   mide**. Por eso no hay carga masiva y por eso el orden importa.
4. **TRAMO POR VUELTA: entre cinco y quince candidatos**, no un capitulo entero.
   La cifra no es sagrada; **el disparador si**: si una vuelta no cierra su
   reporte, la siguiente baja el tramo. Regla madre: la parada de la bateria sin
   techo (5 sep 2026), donde el bucle producia trabajo bueno que no cabia en una
   vuelta.
5. **AL CERRAR EL LIBRO**, los cuatro barridos de la fase 3 del flujo, y la
   auditoria ciega de la fase 4 antes de darlo por integrado.

**CUANDO UN CAPITULO ENTERO CAE EN LA MISMA FAMILIA**, que es el caso que la
seccion vieja dejaba sin escribir: **eso no es una señal de duplicado, es una
señal de que el libro trata un tema.** Se extraen igual, uno a uno, y **se
espera que la cola de lectura sea larga**: es el precio de un capitulo
monotematico, no un fallo de la aduana. Lo que NO se hace es subir un umbral
para que la cola se acorte.

## 13. LA MORATORIA DE MAQUINARIA

*Regla madre: My-idea, decision del fundador del 7 sep 2026, la parada llamada
EL BUCLE SE VOLVIO EL BUCLE. Cosecha seccion 7.F.*

> **NINGUNA VUELTA FABRICA ARNESES, GUARDAS NI LECTORES NUEVOS.** El trabajo de
> una vuelta de extraccion es EXTRAER NODOS.

Un instrumento nuevo solo nace si:

- una **tarea del encargo** lo ordena expresamente, o
- una **caida de dato** lo exige, **con su cita**.

Y ningun documento de esta forja pone un tope numerico a la longitud de un
reporte. **La vara es cualitativa:** nada que el registro ya diga, toda cifra
tallada, las secciones obligatorias mandan. El motivo, que es doctrina por si
solo: **una regla que todos violan por obligacion de otras reglas enseña a violar
reglas.**

## 14. LAS SEDES: DONDE ESCRIBE EL EXTRACTOR Y DONDE NO

*Regla madre: My-idea, ratificacion del fundador del 9 sep 2026. Cosecha 7.E.*

| sede | quien escribe |
|---|---|
| `docs/loop/REPORTE.md` | **el extractor**. Es su sede, y ahi PROPONE |
| `dataset/`, `bitacora/`, `censos/`, `config/pares_mutuos.jsonl` | **la aduana**, por `forja.py insertar`. Nunca a mano |
| `docs/loop/PROMPT_SIGUIENTE.md`, `docs/loop/ACTA_AUDITOR.md`, `docs/loop/PARA_ALEXIS.md` | **el auditor**, y solo el |
| `config/umbrales.json`, `docs/BANCO_DE_REGLAS.md` | **Alexis** |

**EL EXTRACTOR PROPONE EN SU REPORTE; NO SE ADJUDICA A SI MISMO.** Si crees que
una regla debe cambiar, lo escribes como propuesta en tu reporte y sigues. **Tu
no escribes `PARA_ALEXIS.md`**: eso lo hace el auditor.

---

# LAS REGLAS DE ID Y EL PROTOCOLO DE LOTE, ESCRITOS EL 10 SEP 2026

*Las cinco decisiones del fundador del 10 sep 2026 estan en
`docs/BANCO_DE_REGLAS.md`, D.21 a D.25. Esta parte es lo que a ti te toca.*

## 15. LAS REGLAS DE ID, CON SUS DOS LISTAS Y SUS EJEMPLARES

**ESTAN AQUI DENTRO Y NO EN UN ENLACE, y es deliberado (D.23).** El estreno de
la aduana midio que **cuatro de cada diez** candidatos escritos sin estas reglas
delante caen en la puerta. **Un id mal puesto no cuesta un rechazo: cuesta una
arista.** Se leen antes de escribir el primer id, no despues del primer rechazo.

La ley completa esta en `docs/REGLAS_DE_ID.md`. Lo que sigue es lo que mas se
rompe.

### 15.1. Regla 1: un solo idioma, y son DOS listas

| lista | que es | que haces |
|---|---|---|
| **NEGRA** | palabra inglesa **con equivalente corriente en castellano** | usas el castellano. El ingles va a `denominaciones.otros_idiomas` |
| **BLANCA** | **prestamo asentado** en el castellano de negocios | lo escribes tal cual, sin traducir |
| **nombre propio y sigla** | un apellido, una norma, un organismo | ni se traduce ni se caza |

**LA NEGRA, lo que mas aparece:** `customer`, `management`, `development`,
`quality`, `supply`, `performance`, `framework`, `process`, `variance`,
`breakdown`, `procurement`, `stakeholders`, `convention`, `hypothesis`,
`pricing`, `revenue`, `simulation`, `learning`, `manufacturing`, y desde el
10 sep 2026 tambien `equity` (capital, participacion) y `feedback`
(retroalimentacion).

**LA BLANCA, y no la amplias tu:** `marketing`, `benchmarking`, `startup`,
`lean`, `coaching`, `scrum`, `engagement`, `stock`, `software`, `web`,
`ranking`, `escrow`, `backlog`, `branding`, `crowdfunding`, `outsourcing`,
`onboarding`, `storytelling`, `freemium`, `bootstrapping`, `pivot`, `kanban`,
`kaizen`, `leasing`, `coworking`, `networking`, `retargeting`, `greenwashing`,
`crossdocking`, `marketplace`.

**NOMBRES Y SIGLAS:** `deming`, `shewhart`, `juran`, `crosby`, `wallas`,
`weibull`, `westrum`, `hawthorne`, `pugh`, `osha`, `niosh`, `leed`, `swot`,
`wbs`, `ooda`, `ewma`.

**LOS EJEMPLARES, tal como el estreno los tumbo:**

| lo que no vale | por que | como se escribe |
|---|---|---|
| `work_breakdown_structure` | `work`, `breakdown` | `estructura_descomposicion_trabajo`, con `work breakdown structure` en denominaciones |
| `paris_convention_prioridad` | `convention` | `convenio_paris_prioridad`. Un nombre propio traducido no es traduccion libre: **es el nombre** |
| `customer_retention_tactics` | `customer`, `retention` | `tacticas_retencion_clientes` |
| `mitos_stage_gate` | `gate` | **la regla no hace excepciones por prestigio del termino**, aunque `Stage-Gate` sea el nombre de un metodo |
| `plan_marketing_contenidos` | **VALE** | `marketing` esta en la blanca |
| `aplicar_14_puntos_deming` | **VALE** | `deming` es un apellido, y el 14 es denominacion |
| `los_14_puntos_deming` | **CAE, y enseña dos cosas** | es un id VIVO del catalogo, cosa juzgada (D.21), **y hoy caeria** por la regla 3: `los` es un articulo. Ninguna regla indulta a otra |

**POR QUE NO ES PURISMO, y conviene que lo sepas para no pelearte con la
regla:** dos grafias del mismo concepto **parten la familia**.
`retencion_clientes` y `customer_retention` tienen clave de familia **disjunta**,
asi que la señal 2 **no los ve juntos y entran los dos**. Escribir en un solo
idioma es lo que deja trabajar a la señal que te protege del duplicado.

### 15.2. Regla 2: prohibido el numero de VERSION, permitido el de denominacion

| | |
|---|---|
| **NO** | `accion_correctiva_2`, `consejo_calidad_3`, `elegir_grafia_clave_final` |
| **SI** | `aplicar_14_puntos_deming`, `benchmarking_7_pasos_juran`, `iso_31000_gestion_riesgo`, `familia_normas_iso_9000`, `canales_traccion_19`, `riesgo_split_51_49` |

**El corte esta contado: un numero final de UNA CIFRA es version; mayor, es
denominacion. Nadie hace una version 436.** Y el numero en medio nunca fue
version.

**SI TE SALE UN `_2`, PARA:** no estas ante un id mal puesto, estas ante un
**segundo nodo con el nombre del primero**. O continua al primero, y entonces
pide arista y nombre propio, o lo repite, y entonces no entra.

### 15.3. Las otras cuatro, en una linea cada una

- **Regla 3:** sin preposiciones ni articulos. `de`, `del`, `en`, `con`, `por`,
  `para`. **Es la que mas cae de todas** (35 de los 65 del estreno).
- **Regla 4:** sin traducciones paralelas ni familias repetidas.
- **Regla 5:** verbo mas objeto, minimo dos piezas.
- **Regla 6:** `snake_case` estricto, minusculas y sin acentos.

## 15.4. LA RELECTURA DE FIDELIDAD, que la aduana NO puede hacer por ti

*`D.30` del banco, ratificada por el fundador el 10 sep 2026. Es la leccion mas
cara que ha comprado esta casa: costo una vuelta entera de reparacion.*

> **NINGUNA GUARDA DE ESTA CASA VE UN PASO QUE TU ESCRIBISTE Y EL LIBRO NO DICE.**

**LA CIFRA DEL LOTE 1: 13 de 36 pasos, el 36 por ciento, los habia puesto el
extractor y no el libro. Y la aduana dio 6 de 6 verdes ANTES y DESPUES de
corregirlos.** El mismo informe, el mismo saldo, trece defectos en medio.

**No es que la puerta este abierta:** mordida a proposito, la misma puerta tumba
una fuente mutada y un candidato con los pasos vacios. **Es que mide otra cosa.**
La aduana compara tu candidato con el grafo y consigo mismo; **no tiene el libro
delante**, y no puede tenerlo.

> **LA RELECTURA DE FIDELIDAD ES OBLIGATORIA EN TODA VUELTA, ANTES DE CUALQUIER
> INSERCION. NINGUNA MEDIDA DE LA ADUANA LA SUSTITUYE.** Un informe verde
> certifica que la ficha esta bien construida, **no que sus pasos sean del libro.**

**COMO SE HACE, EN EL ACTO DE ESCRIBIR CADA CANDIDATO:**

1. **Marca cada paso contra su parrafo:** **TRANSCRIPCION** (el libro pone el
   medio, la etapa o el objeto) o **PUENTE** (lo escribiste tu).
2. **Cada PUENTE se retira o se reescribe**, y **citas el parrafo que NO lo
   dice**, con su fichero y su linea. **Un puente no se queda callado dentro de
   un nodo.**
3. **En el mismo acto**, no en una vuelta posterior. El lote 1 gasto una vuelta
   entera reparando trece puentes; aplicada al escribir, habria salido sin deuda.

**LAS TRES ESPECIES DE PUENTE QUE EL LOTE 1 PAGO, y son las que volveras a
escribir sin darte cuenta:**

| especie | ejemplar del lote 1 |
|---|---|
| **el destinatario** | *traslada el expediente a la autoridad que puede hacer efectiva esa norma*. El parrafo alienta a vigilar y **no encarga ningun traslado** |
| **el periodo** | *fija por escrito cada cuanto se examina*. El parrafo dice *periodicamente* y **el periodo lo pusiste tu** |
| **el responsable** | *escribe quien responde de cada regla*. El parrafo pone tres etapas y **ningun responsable** |

**Y EL AVISO QUE DICE DONDE MIRAR:** el parrafo mas rico del lote (cinco medios
nombrados) dio **0 por ciento** de puentes; el mas pobre (una frase) dio **83 por
ciento**.

> **UN PARRAFO POBRE NO PRODUCE UN NODO POBRE: PRODUCE UN NODO INVENTADO.**

**Cuando el inventario del libro sea delgado, desconfia de tus propios pasos.** La
tentacion de completarlo no se nota mientras se escribe, y **ninguna guarda la
nota despues.**

## 16. CADA CANDIDATO PASA POR LA ADUANA EN EL MISMO ACTO EN QUE SE ESCRIBE

*Regla madre: decision del fundador del 10 sep 2026, D.23. La aduana NO se
relaja: las reglas no bajan, el extractor aprende.*

> **UN CANDIDATO NO ESTA ESCRITO HASTA QUE HA PASADO LA ADUANA.**

El ciclo por candidato, y **no es opcional**:

    1. escribes el candidato en cuarentena/<libro>/<id>.json
    2. python forja.py informe cuarentena/<libro>/<id>.json
    3. si CAERIA, lo corriges y vuelves al 2
    4. solo entonces cuenta como escrito

**LO QUE ESTO PROHIBE, dicho por su nombre:** escribir doce candidatos y pasar
la aduana al final. **El que cae al final cuesta el lote; el que cae en el minuto
en que se escribio cuesta un minuto.**

**Y UN LOTE NO SE CIERRA CON CANDIDATOS QUE TU SABES QUE CAERIAN.** Si uno cae y
no sabes como corregirlo, **eso es un discutible y se marca** (seccion 8), no un
candidato que se publica esperando que alguien lo arregle.

**EL INFORME DE LOTE SIGUE HACIENDOSE IGUAL**, al cerrar el capitulo:
`python forja.py informe --carpeta cuarentena/<libro>`. Los dos no se pisan: el
de candidato es tu correccion, el de lote es la prueba que lee el fundador.

## 17. EL PROTOCOLO DE LOTE: UN LIBRO, CAPITULO A CAPITULO

*Regla madre: decision del fundador del 10 sep 2026, D.24.*

**UN LIBRO POR LOTE. NO ENTRA EL MUNDO ENTERO.** El orden esta escrito en D.24 y
no lo eliges tu.

| | |
|---|---|
| **la bandeja de entrada** | `fuentes/<clave>/cap_NN.md`, un fichero por capitulo, **fuera de git** |
| **la bandeja de salida** | `cuarentena/<libro>/<id_propuesto>.json`, **DENTRO de git desde el 10 sep 2026** (D.25) |
| **el ritmo** | **un capitulo por vuelta**, no el libro |
| **el commit** | **uno por capitulo**, y su mensaje dice que capitulo y cuantos candidatos |
| **el reporte** | `docs/loop/REPORTE.md`, **por anexion** (seccion 3): el capitulo nuevo se añade, no reescribe el anterior |

**POR QUE UN COMMIT POR CAPITULO Y NO UNO POR LOTE:** un capitulo es la unidad
que se puede revisar de una sentada y revertir sin arrastrar trabajo bueno. Un
commit de libro entero obliga a aceptar o tirar diez capitulos juntos.

**LOS CANDIDATOS VIAJAN AHORA (D.25),** asi que el commit del capitulo lleva
dentro los JSON. Eso es lo que convierte tu reporte en prueba: quien lee
*"del capitulo 2 salieron 7 candidatos y 1 caeria"* **puede abrir los siete**.

**LA FUENTE CANONICA, ANTES DEL PRIMER NODO DEL LIBRO.** Sin su clave en
`fuentes/FUENTES_CANONICAS.json` la aduana rechaza el primer candidato, y ese
rechazo es deliberado.
