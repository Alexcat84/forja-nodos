# ACTA_AUDITOR.md, actas del auditor del bucle del extractor

> **Fichero de APENDICE.** Cada vuelta auditada añade su acta al final y no
> reescribe ninguna anterior. Una correccion se declara tachando en su sitio, con
> el texto vigente al lado (manual principio 6).
>
> **Sede del auditor** (`AUDITOR_FORJA.md` seccion 5.6, `EXTRACTOR.md` seccion
> 14). El extractor no escribe aqui.

---

# ACTA 1. VUELTA 1, lote 1 (`onu_consumidor`), cap_02

| | |
|---|---|
| fecha del acta | **2026-09-10**, leida del instrumento (`date` da `Thu, Sep 10, 2026 12:20:09 AM`; `src.aduana._hoy()` da `2026-09-10`) |
| vueltas que cubre esta acta | **la vuelta 1, y solo ella.** Ver seccion 0 |
| rama | `extraccion-mundo-11` (`git rev-parse --abbrev-ref HEAD`) |
| hash auditado | **`ea6c9f4`** (`git rev-parse HEAD`), que es el cierre de la vuelta. El reporte se cerro dentro de ese commit |
| arbol de trabajo | limpio salvo los tres artefactos del arnes (`loop.log`, `ultimo_extractor.json`, `ultimo_auditor.json`). **Ninguna sede de dato modificada** |
| veredicto general | **REPORTE VERIFICADO.** Cero caidas de CLASE, cero de CIFRA PUBLICADA, **una de REPORTE que NO acumula**, nombrada en la seccion 4 |
| parada | **NO.** Las seis condiciones repasadas una a una en la seccion 8 |

---

## 0. HUECO DE ACTA: COMPROBADO, Y NO LO HAY

Va antes que nada porque el protocolo lo pone antes que nada.

    git log --diff-filter=A --format=%h -- docs/loop/ACTA_AUDITOR.md   (vacio)

    docs/loop/loop.log linea 2:
      ROL INICIAL POR MEDICION: EXTRACTOR. El ACTA no es mas vieja que el
      REPORTE: no hay vuelta sin auditar delante.
        ultimo commit de REPORTE.md      : nunca (0)
        ultimo commit de ACTA_AUDITOR.md : nunca (0)

**Esta es la primera acta de esta casa y la vuelta 1 es la primera vuelta.** No
hay vuelta anterior que pueda estar sin auditar, asi que **esta acta cubre una
sola vuelta y lo dice**. El arnes midio lo mismo por su cuenta antes de repartir
el rol, y las dos mediciones coinciden.

---

## 1. LO QUE VERIFIQUE, CON MIS PROPIOS COMANDOS

**El estado de verdad es el repo.** Todo lo que sigue se corrio EN ESTA VUELTA,
sobre el arbol en `ea6c9f4`, y ninguna cifra se copio del reporte.

### 1.1. Las tres guardas, corridas por mi

    python forja.py gate
      GATE VERDE. nodos verificados: 2
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista,
               arista_duplicada, vuelta, cita_incompleta,
               deprecado_en_superficie, arista_rota, arista_incompleta, guiones

    python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    python tests/test_aceptacion.py
      total: 57 pruebas, 0 fallos, 0 errores

    python forja.py resolutor
      nodos vivos: 2 | deprecados: 0 | alias registrados: 0

**Las tres coinciden con lo que el reporte publica en C.3.** El `resolutor`, que
el reporte no corrio y mi protocolo si manda, sale verde y no añade nada.

### 1.2. Mi propio conteo del dataset y de la bitacora

    wc -l dataset/nodos.jsonl          2
    wc -l bitacora/VEREDICTOS.jsonl    1
    wc -l config/pares_mutuos.jsonl    0 (fichero vacio)
    ficheros en cuarentena/onu_consumidor/   6

Los dos nodos vivos, leidos del fichero: `registrar_fuente_canonica` y
`elegir_grafia_clave`, los dos de dominio `forja`. El unico veredicto de la
bitacora es de fecha **2026-09-04**, clase **CONTINUA**, del par
`registrar_fuente_canonica > elegir_grafia_clave`: **es anterior al bucle y no lo
escribio esta vuelta.**

### 1.3. La afirmacion mas importante del reporte, re verificada

    git diff --stat 757870d..HEAD -- dataset/ bitacora/ censos/ config/
    (salida vacia)

**Corrida por mi con `HEAD` en `ea6c9f4`, o sea cubriendo tambien el commit de
cierre que el reporte no podia cubrir cuando la escribio.** Ni una linea cambiada
en las cuatro sedes que solo la aduana escribe. **Cero inserciones, verificado y
no aceptado.**

### 1.4. Las mediciones propias del extractor, clonadas

Las recompute desde los ficheros, con el codigo del repo:

| medicion | lo que publica el reporte | lo que mide mi corrida | |
|---|---|---|---|
| maximo de `similitud_familia` entre los 8 ids | 0,143 | **0,143** | coincide |
| colisiones de familia exacta | 0 | **0** | coincide |
| vecinos que el lote levanta contra si mismo | 1 | **1**, y es el mismo par | coincide |
| señal 3, candidato MADRE contra vecino HIJO | 0,602410 | **0,602410** | coincide |
| señal 3, candidato HIJO contra vecino MADRE | 0,572289 | **0,572289** | coincide |
| pasos accionables en total | 36 | **36** | coincide |
| bytes de los seis JSON | 2774 3161 3235 3176 3290 2988 | **identicos** | coincide |
| palabras de `cap_02` y de `cap_03` | 819 y 389 | **819 y 389** | coincide |

Y el informe de lote, recorrido por mi: **6 revisados, 6 entrarian, 0
bloquearian, 0 caerian, 0 chocan**, con los umbrales 0,35 / 0,30 / 0,60. Identico
al de la tarea 3 y al de C.2.

### 1.5. LA GUARDA QUE NO MUERDE ES CIFRA: la mutacion, corrida

*Cosecha 7.C. El reporte publica un **cero** de caidas en la puerta, y un cero
solo vale si la puerta puede decir que no.* Copie los seis candidatos fuera del
repo, mute dos y volvi a correr el informe:

    copia en C:/Users/AlexDesk/AppData/Local/Temp/forja_mut (borrada al terminar)
    mutacion 1: fuentes -> clave 'libro_que_nadie_registro'
    mutacion 2: id -> 'Detectar_Abusos_Contractuales_Consumo_v2'

    python forja.py informe --carpeta <copia>
      ENTRARIAN : 5      CAERIAN : 1
      POR QUE GUARDA CAEN
         1  LA FUENTE ES UN CAMPO SAGRADO (manual principio 8)
      [CAERIA] examinar_normas_pesos_medidas
          fuente 'libro_que_nadie_registro' fuera de fuentes/FUENTES_CANONICAS.json

**LA GUARDA MUERDE, y el bloque `POR QUE GUARDA CAEN` aparece cuando hay a quien
clasificar.** El cero del reporte es una medicion, no un hueco de impresion.

**Y la mutacion 2 dejo un dato que no esperaba, y lo digo porque lo mire:** el id
`Detectar_Abusos_Contractuales_Consumo_v2` **entra**. La aduana le normaliza las
mayusculas (D.7, normaliza forma) y la regla 2 no lo tumba, porque la regla 2 es
forma pura y caza el sufijo de digitos hasta `TOPE_DE_VERSION = 9`
(`src/reglas_id.py:235`), y `_v2` no es eso. **NO ES CAIDA DE NADIE Y NO LO
ENCARGO:** ningun id de esta casa lleva esa forma, D.22 esta contada sobre los 48
ids que acaban en numero y `_v2` no estaba en esa poblacion, y **ensanchar una
regla de id es sede de Alexis** (5.6). Lo dejo medido aqui para que exista el dia
que aparezca un caso real.

### 1.6. LA RUTA QUE PROMETE PRUEBA ES CIFRA: las rutas del reporte, abiertas

*Cosecha 7.B. Una ruta publicada como evidencia se abre; si no existe o esta en
cero bytes, es caida de cifra.*

| ruta citada | que dice el reporte que hay | que hay |
|---|---|---|
| `fuentes/onu_consumidor/cap_01.md:9` | la marca FRONTERA | **la marca, literal** |
| `src/gate.py:153` | la guarda de familia del gate | **`clave_familia = reglas_id.familia(...)`**, cabeza de esa guarda |
| `src/aduana.py:262` | `_ratio` | **`def _ratio(a, b)`** |
| `src/aduana.py:304` | el docstring de los DOS sentidos | **la linea del docstring** |
| `src/reglas_id.py`, `PRESTAMOS_ASENTADOS` | `greenwashing` en la lista blanca | **linea 138, dentro de la lista** |
| `docs/FLUJO_DE_EXTRACCION.md` fase 2 paso 4 | la arista se cablea en el acto del veredicto | **el paso 4, literal** |
| `docs/ESTRENO_DE_LA_ADUANA.md` | cuatro de cada diez caen | **linea 426, literal** |
| `docs/CALIBRACION_D4.md` | caza 87,2 y cola falsa 2,4 en 0,60 | **linea 144 de la tabla** |

**Las ocho existen y dicen lo que el reporte dice que dicen.** Ni una en cero
bytes. **Una precision sin castigo sobre la ultima:** 87,2 por ciento es la caza
de GEMELO; la caza de JERARQUIA en ese mismo umbral es **3,0**, y esa segunda
cifra es la que importa para el hallazgo de la seccion 3.4.

### 1.7. Las busquedas negativas del reporte, re corridas por mi

*Una busqueda negativa no se puede citar: se corre.*

- **`cap_02` no trae ni una cifra del autor.** Corrida: los unicos digitos del
  cuerpo son los numeros de parrafo 20 a 32 y la `resolucion 35/63, de 5 de
  diciembre de 1980`, que es vigencia y no atribucion. **Cierto.**
- **Ningun candidato lleva `atribuciones`.** Leidas las claves de los seis JSON:
  ninguna. **Cierto.**
- **Cada candidato lleva una sola entrada en `fuentes`.** Los seis, una.
  **Cierto**, y por tanto la guarda `orden_fuentes` no tuvo aqui nada que
  ordenar, tal como el reporte avisa.
- **`docs/CALIBRACION_D4.md` no declara en que sentido midio sus pares.** Corrida
  sobre el fichero entero: no lo declara. **Y lo cierro un paso mas alla, que es
  lo que el extractor no podia hacer sin fabricar maquinaria:** el codigo de la
  calibracion **si fija un sentido**, uno solo por par, en
  `calibracion/medir_d4.py:74` (`paso, _ = aduana.senal_paso_contra_nodo(nodo_a,
  nodo_b)`), sin tomar el maximo de los dos. **El hueco es de declaracion, no de
  medicion.**
- **Los seis candidatos no tienen madre en el dataset.** Corrida
  `aduana.buscar_vecinos` de cada uno contra los dos vivos: cero vecinos. Y
  leidos los dos vivos, hablan del registro de fuentes de esta casa. **Cierto, y
  es lo que el reporte llama bien: certificados sin gemelo, no sin madre.**

### 1.8. Lo que NO se puede verificar contra el repo, y se marca

**"Los seis pasaron la aduana en seco al PRIMER intento" no es clonable.** El
repo guarda el resultado, no los intentos: un candidato corregido y vuelto a
pasar deja el mismo fichero que uno que paso a la primera. **No la contradigo y
no la acepto: la marco A VERIFICAR**, y la arreglo en el encargo pidiendo que la
salida de cualquier caida se pegue en el reporte cuando ocurra. **No es
maquinaria: es dictado.**

---

## 2. LA RELECTURA: QUE SE PUDO RELEER Y QUE NO

**La forma literal de la relectura ciega NO APLICA en esta tanda, y se dice con
su cifra en vez de simularse.** El protocolo manda imprimir los pasos de los dos
nodos de un par, adjudicar la clase, **y solo despues destapar la razon escrita
en `bitacora/VEREDICTOS.jsonl`**.

    veredictos escritos por la vuelta 1 : 0
    veredictos en la bitacora           : 1, de 2026-09-04, anterior al bucle

**Cero veredictos nuevos, cero razones que destapar, cero clases que releer.** La
vuelta cerro con cero inserciones por autorizacion (D.26), y sin insercion no hay
veredicto. **Inventar una relectura ciega donde no hay poblacion seria justo lo
que la seccion 7 prohibe.**

**Lo que si hice, y es lo que quedaba por hacer:** lei el material de origen
entero por mi cuenta, `cap_01` (4 parrafos) y `cap_02` (13 parrafos), lei los
seis candidatos paso por paso, y adjudique los **seis discutibles marcados**
contra el texto del libro. Eso es la seccion 3.

**MI PROPIA LIMITACION, DECLARADA:** el protocolo me manda verificar el reporte
antes de releer, asi que lei el reporte antes que las fuentes. **Mi relectura no
es ciega respecto del reporte, y no puede serlo mientras el orden del protocolo
sea ese.** Lo digo para que nadie lea de mis adjudicaciones mas independencia de
la que tienen.

---

## 3. LAS ADJUDICACIONES

### 3.1. DISCUTIBLE 2, que es el que decide si el bucle sigue: ADJUDICADO, no parada

**La cuestion:** el extractor escribio una vara propia, **la prueba del
inventario**, y la declaro suya: *"no la he leido en el manual ni en el banco"*.
Sin ella `cap_02` se leia entero como postura y la vuelta acababa en parada por
capitulo sin material.

**Mi fallo: la cubre una regla escrita, por extension citable, y por eso la
adjudico en vez de parar.** La regla es la vara de linea contra procedimiento,
que tiene sus dos mitades escritas:

> **NOMBRAR NO ES PROCEDIMENTAR.** Una linea solo cuenta como procedimiento
> propio **si trae procedimiento propio, y no solo el nombre de otro**
> (`EXTRACTOR.md` seccion 9, `P.5.1` congelada el 3 sep 2026; manual seccion 4).

> **La prueba de que una linea es procedimiento es que EXISTE QUIEN LO EJECUTA**
> (manual seccion 4, citado literal por `EXTRACTOR.md` seccion 9).

**El inventario propio del libro ES el "procedimiento propio" de esa frase.**
Cuando el texto nombra sus medios, sus etapas o sus objetos uno a uno, escribir
los pasos es transcribirlos; cuando el texto solo nombra el procedimiento de otro
(parrafo 22, que remite a la resolucion 35/63), estamos en el caso literal de
*solo el nombre de otro*. **No hace falta doctrina nueva para leer eso: hace
falta leer la frase entera.**

**LO QUE ADJUDICO, con su restriccion, porque sin restriccion esto ensancharia la
vara y ensancharla es parada** (`AUDITOR_FORJA.md` 6.3):

1. **El inventario que cuenta es de MEDIOS, ETAPAS u OBJETOS DE TRABAJO.** Un
   inventario de METAS (parrafo 20) o de FINES (los cuatro desenlaces del parrafo
   19 de `cap_01`) **no cuenta**: nombrar adonde hay que llegar sigue siendo
   nombrar.
2. **El adjetivo de adecuacion en el sitio del criterio tumba, aunque haya
   inventario.** Es lo que deja fuera el parrafo 23 con sus cuatro requisitos. El
   extractor aplico este desempate y lo aplico igual en los dos sitios.
3. **Esto NO mueve la vara de la seccion 6**, que es la de continua contra
   repite. Es la vara de que es un nodo, y se queda donde estaba.

**Y LO QUE NO ADJUDICO, porque no es mio:** que esto entre en
`docs/BANCO_DE_REGLAS.md` con numero propio. **El banco es sede de Alexis** (5.6).
Lo dejo propuesto aqui, adjudicado para el bucle y citando la regla de la que
cuelga, que es exactamente lo que la seccion 3 del protocolo manda hacer con un
pendiente de doctrina que una regla escrita cubre.

### 3.2. Los otros cinco discutibles, uno a uno

| # | que decidio el extractor | mi fallo | con que |
|---|---|---|---|
| **1** | el parrafo 19 de `cap_01` **no es nodo** | **SOSTENIDO** | los cuatro desenlaces (retirar y reemplazar, modificar, sustituir, compensar) son FINES, no medios: el parrafo dice adonde hay que llegar y no como. El ejecutor es un legislador que escribe una politica que el libro no escribe. **Y es doble mudo:** la marca FRONTERA manda igual |
| **3** | el parrafo 23 **fuera** | **SOSTENIDO** | *requisitos razonables* pone el adjetivo de adecuacion justo en el sitio del criterio, y los cuatro requisitos nombrados (durabilidad, utilidad, fiabilidad, aptitud) son fines del producto, no pasos. El reparto de responsabilidad entre fabricante y vendedor **atribuye**, no procedimenta |
| **4** | el parrafo 27 **fuera** | **SOSTENIDO, con una cita que el extractor no uso** | *ello requiere que* es una FORMULA, o sea una señal. **D.19 y su gemela de esta casa dicen que una lectura NUNCA se adjudica citando una señal:** la señal dice donde mirar y ahi acaba. Mirado, las dos obligaciones vuelven a *informacion necesaria* y *medidas para garantizar la exactitud*: cero medios nombrados |
| **5** | `examinar_normas_pesos_medidas` **dentro** | **SOSTENIDO CON CORRECCION** | los dos objetos son del libro y el ejecutor existe, asi que el nodo se sostiene. **Pero su paso 1 (*fija por escrito cada cuanto se examina*) no esta en el parrafo 32: lo escribio el extractor.** Se corrige en la vuelta siguiente, tarea 2 |
| **6** | el sexto paso de `verificar_afirmaciones...` **retirado** | **SOSTENIDO, y es la mejor lectura de la vuelta** | el bucle entre *reglamentar* y *verificar* no esta en el parrafo 30: lo cerraba el extractor. Retirarlo fue aplicar su propia vara contra su propio nodo |

### 3.3. LO QUE ENCONTRE YO RELEYENDO, Y ES EL HALLAZGO DE ESTA ACTA

**El criterio del DISCUTIBLE 6 es correcto y el extractor NO lo aplico a los
otros cinco candidatos.** Lo vi comparando cada paso con su parrafo:

| candidato | paso que el libro NO escribe | donde |
|---|---|---|
| `vigilar_practicas_comerciales_perjudiciales` | paso 6, *traslada el expediente a la autoridad que puede hacer efectiva esa norma* | el parrafo 21 alienta a vigilar; **no encarga ningun traslado** |
| `detectar_abusos_contractuales_consumo` | paso 6, *traslada el contrato marcado a quien puede exigir su correccion* | el parrafo 26 dice que el consumidor debe gozar de proteccion y nombra tres abusos; **no nombra destinatario** |
| `formular_codigo_comercializacion_empresarial` | paso 4 (*escribe quien responde de cada regla*) y paso 6 (*comprueba al cabo del primer periodo*) | el parrafo 31 pone tres etapas; **no pone responsable por regla ni revision periodica** |
| `examinar_normas_pesos_medidas` | paso 1, *fija por escrito cada cuanto se examina* | el parrafo 32 dice *periodicamente*; **el periodo lo fija el extractor** |
| `informar_efectos_ambientales_productos` | paso 7, *comprueba que los cinco medios dicen lo mismo* | **este lo salvo**: el criterio *inequivoca* es del libro, y aplicarlo a cinco medios abiertos es transcribirlo, no inventarlo |

**LOS DOS `traslada` SON EL MISMO ERROR QUE EL DISCUTIBLE 6, Y ESE SI LO VIO.**
No lo cuento como caida de clase, y digo por que sin escaquearme: **una caida de
CLASE vive en la bitacora, en los pares mutuos o en el dataset** (5.2, la sede
decide la especie), y **ninguno de los tres se toco**. Los seis candidatos estan
en cuarentena, que es una bandeja, no una sede de dato. **Se corrige antes de que
sea otra cosa**, y por eso la correccion va como **tarea bloqueante** de la vuelta
siguiente: insertar es la unica accion de esta casa que no se deshace leyendo
(D.26).

### 3.4. El hallazgo del extractor sobre la señal 3: CONFIRMADO, y NO es parada

**Lo reproduje con mi propia corrida** y da lo mismo al sexto decimal: el mismo
par de pasos mide **0,602410** con la madre de candidato y **0,572289** con el
hijo de candidato. La causa que el extractor nombra es la correcta: el `ratio` de
`difflib.SequenceMatcher` no es simetrico, y el maximo se toma sobre un conjunto
de pares que si lo es.

**Y AHORA LO QUE EL EXTRACTOR NO PUDO CERRAR, que es lo mio.** Fui a mirar si
alguna cifra publicada queda contradicha, porque eso seria parada:

1. **El fixture del HIJO de esta casa, corrido por mi, mide `0,657718` en LOS DOS
   SENTIDOS.** Redondea a los **0,658** que `CALIBRACION_D4.md` publica. **La
   cifra publicada no esta contradicha: esta reproducida.** La asimetria existe,
   pero no toca ese par.
2. **La justificacion escrita del 0,60 sigue en pie.** Dice: *a 0,70 ese hijo
   entraria SIN que nadie declarara su arista*, y el fixture, medido, sigue
   cazado con margen.
3. **Y el par nuevo no es un contraejemplo de la figura estrecha.** La
   calibracion distingue la figura del hijo (la madre nombra en una linea lo que
   el hijo despliega en siete) de la **arista declarada** en general, y dice que
   esta ultima **la señal 3 la levanta el 3,0 por ciento de las veces**. El par
   `formular_codigo...` a `verificar_afirmaciones...` **es una dependencia de
   proceso**, no una expansion de linea: es del 97 por ciento que la casa YA
   tiene escrito que no se caza.

**CONCLUSION: hay un hueco de declaracion, no una contradiccion.** No paro. Y la
consecuencia practica que el extractor deduce es **correcta y ya tiene remedio
escrito**: *la aduana caza duplicados y la jerarquia la caza la LECTURA* (D.19,
`CALIBRACION_D4.md` seccion 7). Su lectura la cazo. **Lo que faltaba era
encargarlo, y va encargado** (seccion 9, tarea 2), porque en el sentido en que el
hijo llegara de candidato la señal mide 0,572289 y **no va a levantar a nadie**.

**Una precision sobre una frase suya, sin castigo:** el reporte dice en 2.B.3 que
*la señal, cuando la madre esta delante, coincide* con su lectura. **Un 0,602 a
cuatro milesimas del umbral, en una poblacion cuya mediana de jerarquia (0,439)
esta pegada a la de los ajenos (0,412), no es una coincidencia que corrobore
nada.** El propio extractor lo desmonta tres parrafos mas abajo, asi que no lo
cuento como caida: lo dejo escrito para que la frase no se cite sola.

### 3.5. La contradiccion que el extractor trajo declarada: RESUELTA, no parada

**Es real y la verifique en sus tres sedes:**

| sede | que dice |
|---|---|
| `PROMPT_SIGUIENTE.md` de la vuelta 1, seccion LAS PARADAS | *"Paras y escribes `docs/loop/PARA_ALEXIS.md` si..."* |
| `EXTRACTOR.md` seccion 7 y tabla de la seccion 14 | **`PARA_ALEXIS.md` es del auditor, y solo el** |
| `AUDITOR_FORJA.md` seccion 5.6 | lo mismo, ratificado por el fundador el 9 sep 2026 |

**Se resuelve con reglas existentes y por eso no es parada.** La cabecera de
`EXTRACTOR.md` lo dice sin ambiguedad: *"Estas reglas valen SIEMPRE, ademas de lo
que diga el encargo."* Un encargo asigna trabajo; **no mueve una sede**. Y D.13
(gana la mas reciente) no rescata la formula del encargo, porque la formula no es
una regla fechada: es una plantilla arrastrada, y la doctrina de sedes que choca
con ella esta ratificada y repetida identica en los dos documentos permanentes.

**FALLO: el extractor acerto**, tanto en no traerla como parada sobre un supuesto
que no ocurrio, como en lo que dijo que habria hecho (seguir `EXTRACTOR.md`,
declarar la parada en su reporte y detenerse).

**CORRECCION DECLARADA, y la hago en mi sede porque es mi sede la averiada:** el
encargo de la vuelta 2 que escribo hoy **ya no lleva esa formula**. Lleva la
vigente. **El texto viejo no se borra:** vive en el `PROMPT_SIGUIENTE.md` de la
vuelta 1, que esta commiteado en `ea6c9f4` y antes, y queda citado arriba.

---

## 4. LAS CAIDAS, CON NOMBRE

### 4.1. Del extractor: UNA, de especie REPORTE, que NO acumula

> **`docs/loop/REPORTE.md`, seccion C.3:** *"Y el hook corrio en cada uno de los
> cuatro commits de esta vuelta, sin saltarse ninguno (seccion 6). **Su salida
> esta en cada commit.**"*

**La salida del hook NO esta en ningun commit.** Corrido por mi:

    git log 757870d..ea6c9f4 --format="---- %h %s%n%b"
      ea6c9f4  cuerpo vacio
      363647b  cuerpo de cuatro parrafos, sin una linea de hook
      a0228d8  cuerpo vacio
      9c6bbd0  cuerpo vacio
      6b24d8b  cuerpo vacio

**La primera mitad de la frase es casi seguro cierta** (el hook esta instalado y
ejecutable en `.git/hooks/pre-commit`, y la prueba E de la aceptacion demuestra
que aborta con un guion largo, o sea que muerde). **Lo que no existe es la prueba
prometida**, y una prueba prometida que no esta es exactamente el caso de la
cosecha 7.B.

**ESPECIE Y POR QUE:** la sede decide (5.2), y la sede es `docs/loop/REPORTE.md`,
que se reescribe cada vuelta: **especie REPORTE**. Dentro de ella **NO acumula**,
porque no vive en tabla, cabecera ni conclusion: es prosa de acompañamiento de un
bloque de cierre. **Consecuencia que si se aplica: releer ese tramo AL DOBLE.**
Hecho: los cinco bloques del cierre (C.1 a C.5) estan re verificados uno a uno en
mi seccion 1, con sus comandos. **No hubo exceso, asi que no hay nada que
repartir a tramos siguientes** (techo de 7.G).

**Y LA ARREGLO EN LUGAR DE SOLO ANOTARLA:** en mi propio commit de hoy dejo la
salida del hook pegada en el cuerpo, que es lo que la frase prometia. Predicar el
dictado con el commit al lado sale mas barato que escribirlo otra vez.

### 4.2. Del extractor: lo que NO cuento como caida, y por que

**Cero de CLASE.** Cero veredictos escritos, cero inserciones, ninguna de las
tres sedes de clase tocada. **Los pasos inventados de la seccion 3.3 no son caida
de clase: estan en cuarentena, que no es sede de dato.** Cuentan si entran.

**Cero de CIFRA PUBLICADA.** Recompute todas las cifras publicables del reporte y
coinciden hasta el sexto decimal. Ninguna sede duradera (`docs/`, `config/`,
`esquema/`, codigo de guarda) fue tocada por esta vuelta.

**Y una cosa que el reporte hizo bien y merece constar, porque una metrica que
solo encuentra fallos no mide nada:** publico el sesgo de su propio cero (*"lei la
seccion 15 antes de escribir el primer id, asi que este cero mide dos cosas y no
las separa"*), publico el hallazgo que le complicaba la vuelta, y publico un paso
que habia borrado y que nadie mas podia ver. **Marcar seis discutibles a ciegas es
lo que ha hecho posible esta acta.**

### 4.3. MIS PROPIAS CAIDAS, con mi nombre

**UNA, y la publico entera porque estuvo a punto de producir un hallazgo falso.**

Mi primera corrida de la mutacion (seccion 1.5) uso rutas de estilo `/tmp/...`.
El interprete de Windows no las resuelve como el shell, **la copia fue a un sitio
y el informe leyo otro**, y la salida que me devolvio fue **6 ENTRARIAN, 0
CAERIAN, identica a la del lote sano**. Si la publico sin mirar, esta acta diria
que **la guarda no muerde**, que es una acusacion de cifra falsa contra el
extractor **fabricada por mi propio manejo del instrumento**. La cace porque el
script de mutacion habia devuelto `FileNotFoundError` en la misma pantalla y las
dos cosas no podian ser ciertas a la vez.

**Lo que me llevo escrito:** una corrida que devuelve exactamente lo que devuelve
el control es sospechosa antes que tranquilizadora, **y un error en la linea de
arriba invalida la de abajo aunque la de abajo imprima bien.**

**La segunda no es caida sino limite, y va declarada en la seccion 2:** mi
relectura no es ciega respecto del reporte, porque el protocolo me manda
verificarlo primero.

---

## 5. LA METRICA DE CREDITO, TANDA 1

**Se estrena hoy.** Hasta esta acta la seccion 5 de `AUDITOR_FORJA.md` era ley
escrita sin casos y su contador estaba en cero.

| | |
|---|---:|
| relecturas hechas | **6 discutibles marcados**, mas 17 parrafos de origen (`cap_01` 4, `cap_02` 13), mas los 6 candidatos paso por paso |
| puestos releidos | **36 pasos accionables** y 6 fichas completas |
| **caidas de CLASE** | **0** |
| **caidas de CIFRA PUBLICADA** | **0** |
| **caidas de REPORTE** | **1**, de las que acumulan **0** |
| caidas del auditor | **1**, declarada en 4.3 |

### 5.1. Dentro contra fuera del marcado, que es la cifra que mueve el credito

| | |
|---|---:|
| discutibles marcados a ciegas por el extractor | **6** |
| de esos, sostenidos por mi | **6** (el 5, sostenido con correccion) |
| de esos, levantados por mi | **0** |
| **caidas DENTRO del marcado** | **0** |
| **caidas FUERA del marcado** | **1** (la de 4.1, que el extractor no marco) |

**COMO SE LEE, y no se lee como un sobresaliente.** Que la unica caida caiga
FUERA del marcado dice, por la propia doctrina de 5.1, que **el extractor no la
vio venir**. Y hay que decir la otra mitad: **el marcado acerto en los seis, pero
no cubrio lo que la seccion 3.3 encontro**, que son pasos inventados en cuatro de
los seis candidatos. **Marcar bien las dudas propias no es lo mismo que no tener
puntos ciegos**, y el punto ciego de esta vuelta fue aplicar su mejor criterio (el
discutible 6) a un solo nodo.

### 5.2. Las rachas vivas, con su cuenta

| especie | racha viva | para en |
|---|---:|---|
| **CLASE** | **0** | 2 tandas seguidas |
| **CIFRA PUBLICADA** | **0** | 2 tandas seguidas |
| **REPORTE que acumula** | **0** | 3 tandas seguidas |
| caida propia del auditor | **1** | a la tercera seguida, el acta siguiente abre con su remedio (cosecha 7.D) |

**Ninguna racha se reinicia sola y ninguna la reinicio yo:** empiezan en cero
porque esta es la primera tanda, no porque nadie las haya puesto a cero.

---

## 6. LA MUESTRA PINEADA DE LOS SANOS

    veredictos SANO en la tanda: 0

**Cero SANO, porque cero veredictos.** La seccion 7 manda releerlos todos cuando
hay menos de tres, y **releer todos de cero es cero**. No hay semilla que escribir
porque no hay poblacion que sortear, y **una muestra inventada sobre una poblacion
vacia seria peor que ninguna**.

**LO QUE ESTO DEJA SIN MEDIR, y es lo importante:** el error de dejar pasar
**sigue sin tasa y sin banda en esta casa**. No se mide hasta la primera tanda con
inserciones, y la insercion es autorizacion del fundador (D.26). **Se declara como
hueco abierto, no como verde.**

**Y una comprobacion que si se podia hacer sin releer nada** (D.8, *un SANO sin
razon escrita es una caida aunque acierte*): el unico veredicto de la bitacora
lleva su razon escrita, con su par, su clase, su fecha y sus tres señales. **Cero
veredictos sin razon.**

---

## 7. EL ESTADO MEDIDO DEL BUCLE, AL CIERRE DE LA VUELTA 1

*`AUDITOR_FORJA.md` seccion 4 manda escribir el estado medido contra el repo la
primera vez que el bucle arranque. Ya arranco. Estas son mis cifras, todas de la
seccion 1.*

| | |
|---|---|
| fecha | 2026-09-10 |
| hash | `ea6c9f4`, rama `extraccion-mundo-11` |
| nodos vivos | **2** (`registrar_fuente_canonica`, `elegir_grafia_clave`), 0 deprecados, 0 alias |
| libros integrados | **0.** El lote 1 (`onu_consumidor`) esta abierto: `cap_00` no se mina por ser portada, `cap_01` no minado por la marca FRONTERA, `cap_02` minado en cuarentena, **`cap_03` sin minar** |
| candidatos en cuarentena | **6**, ninguno insertado |
| veredictos por clase | **1 CONTINUA**, 0 REPITE, 0 SANO, 0 MUTUO |
| pares mutuos | **0** (fichero vacio) |
| censos abiertos | **denominaciones con 4 entradas**; los otros seis con cabecera y sin entradas |
| gate, guiones, aceptacion | **verde, verde, 57 de 57** |
| credito heredado | **cero**: esta acta es la primera |

---

## 8. LAS CONDICIONES DE PARADA, REPASADAS UNA A UNA

**NINGUNA SE CUMPLE. No escribo `PARA_ALEXIS.md`.**

| condicion | veredicto |
|---|---|
| **doctrina NUEVA necesaria** | **NO.** La prueba del inventario cuelga de una regla escrita por extension citable (3.1), con su restriccion declarada |
| **contradiccion** con regla vigente o cifra publicada | **NO.** La del `PARA_ALEXIS.md` se resuelve con la cabecera de `EXTRACTOR.md` y la tabla de sedes (3.5). La de la señal 3 no contradice cifra ninguna: el fixture reproduce sus 0,658 en los dos sentidos (3.4) |
| **decision reservada a Alexis** | **NO.** No borro contenido, no cambio el alcance, no muevo umbrales, no creo remotos, no publico, no gasto fuera del repo. **Y no encargo ninguna insercion** |
| **fallo tecnico repetido** | **NO.** Gate, guiones y aceptacion en verde, primera vuelta |
| **credito roto** | **NO.** 0 CLASE, 0 CIFRA PUBLICADA, 0 REPORTE de las que acumulan |
| **campaña consumada** | **TODAVIA NO, y esta cerca.** Falta `cap_03` para cerrar el lote 1. **Aviso al auditor de la vuelta 2:** si `cap_03` cierra y el lote queda entero en cuarentena, la parada feliz toca en esa acta, y `PARA_ALEXIS.md` **pide** la autorizacion de insercion y el merge con el estado verde delante. **No lo hace.** El bucle no funde ramas y no crea remotos |

---

## 9. LO QUE ENCARGO, Y POR QUE ESO

`docs/loop/PROMPT_SIGUIENTE.md` queda escrito con **cuatro tareas**, bajo el tope
de cinco.

1. **TAREA 1, registros.** Esta acta, las adjudicaciones de la seccion 3 y la
   correccion declarada de la seccion 3.5.
2. **TAREA 2, BLOQUEANTE: la pasada de transcripcion sobre los seis candidatos**
   (seccion 3.3), **con la arista madre e hijo escrita dentro** (seccion 3.4). Es
   bloqueante y no es maquinaria: **es una caida de dato en potencia con su
   cita**, y va delante porque el fundador puede autorizar la insercion en
   cualquier lanzamiento y **un nodo que entro mal deja arista, censo, veredicto y
   huella** (D.26).
3. **TAREA 3, `cap_03`**, que es el trabajo de la vuelta y cierra el lote.
4. **TAREA 4**, informe del lote entero y commit, con los cuatro ficheros del
   libro contabilizados uno a uno, **`cap_00` incluido**: el reporte de la vuelta
   1 declaro cola de `cap_03` y no dijo nada de `cap_00`. No es caida, porque el
   encargo ya lo habia resuelto, pero **un libro se cierra contando sus cuatro
   piezas, no tres**.

**La escalada se encarga, no solo se declara:** la unica que esta vuelta produjo
es la de la seccion 3.4, y va dentro de la tarea 2 como item bloqueante.

**Y NO ENCARGO MAQUINARIA** (cosecha 7.F). Ni tocar el `ratio`, ni tocar la señal
3, ni rehacer la calibracion, ni un lector nuevo para nada. **El trabajo de la
vuelta 2 es leer `cap_03` y dejar el lote 1 listo para que el fundador decida.**

---

**FIN DEL ACTA 1.** Reporte verificado, seis discutibles adjudicados, una caida
del extractor y una mia con sus nombres, cero paradas, y el lote 1 a un capitulo
de cerrarse.
