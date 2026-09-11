# APERTURA CIEGA DEL AUDITOR, vuelta 13 del bucle

**Fecha: 11 sep 2026.** Escrita bajo `D.34` (`AUDITOR_FORJA.md` seccion 1.5,
ampliada el 11 sep). El arnes retiro del arbol `docs/loop/REPORTE.md`,
`docs/loop/loop.log`, `docs/loop/ultimo_extractor.json` y
`docs/loop/ultimo_auditor.json`. **No los he recuperado por ninguna via**: no he
corrido `git show`, ni `git checkout`, ni `git cat-file` sobre ninguno de los
cuatro, y los unicos comandos de git que he corrido son `git log --oneline`,
`git show --stat --format=%s` sobre seis hashes y `git log -- bitacora/VEREDICTOS.jsonl`.
De los tres `git show --stat` que tocaron el reporte solo vi **el nombre del
fichero y su numero de lineas**, nunca su contenido.

---

## 0. UNA CONTAMINACION MIA, Y LA DECLARO ANTES DE NADA

**Vi los ocho nombres de fichero de los candidatos ANTES de leer el capitulo
fuente.** Los vi en el `ls` de `cuarentena/zhuo_manager/` y en el
`git show --stat` del commit `b7aadb2`, que los lista uno a uno. Cuando abri
`fuentes/zhuo_manager/cap_11.md` **ya sabia como se llamaban las ocho piezas que
el extractor habia cortado.**

**Asi que mi troceo del capitulo NO es independiente de su nomenclatura**, y
cualquier coincidencia entre su lista y la mia hay que leerla con ese descuento
delante. Lo digo yo, que soy el que pierde con decirlo.

**Lo que SI queda independiente, y es la mayor parte de este fichero:**

| sigue siendo ciego | por que |
|---|---|
| **PUENTE contra TRANSCRIPCION de los 57 pasos** | el nombre del fichero no dice que pone dentro; cada paso lo he contrastado con su linea del libro |
| **los huecos del capitulo** | ver ocho nombres no me dice que material se quedo fuera: eso lo he barrido yo linea a linea |
| **las colisiones con el grafo de 135** | la busqueda de vecinos la he corrido yo contra `dataset/nodos.jsonl` |
| **la frontera de doctrina** | la he encontrado yo persiguiendo la palanca, no el nombre |
| **el juicio de `cap_12`** | ahi no habia ningun nombre que ver, porque no produjo ninguno |

**Como se evita la proxima vez, y es un encargo para mi mismo:** leer la fuente
ANTES de listar la cuarentena. El orden de dos comandos es toda la diferencia
entre una apertura ciega y una apertura informada, y el orden lo elegi yo mal.

---

## 1. EL MATERIAL QUE ABRO, MEDIDO

    ls cuarentena/zhuo_manager/*.json | wc -l              ->  68
    ls cuarentena/_insertados/zhuo_manager/*.json | wc -l  ->  68
    wc -l dataset/nodos.jsonl                             -> 135 nodos
    wc -l bitacora/VEREDICTOS.jsonl                       -> 100 veredictos

De los 68 de la bandeja, **ocho son de esta vuelta** y son los que juzgo. Los
identifico por el commit `b7aadb2`, que es el unico de la vuelta que aniade
ficheros a la cuarentena:

    actuar_conducta_contraria_valores       comunicar_valores_diez_formas
    contrastar_cultura_actual_aspirada      inventar_tradiciones_celebrar_valores
    juzgar_cultura_renuncias_equipo         reconocer_decision_dificil_valores
    revisar_incentivos_trampas_equipo       vivir_primero_valor_declarado

Fuente: `fuentes/zhuo_manager/cap_11.md`, 191 lineas, cabecera `unidad: Cap. 10`,
`titulo_textual: Nurturing Culture`, `fidelidad: verbatim`.

**Y una novena operacion de la vuelta que NO es un candidato nuevo:** el commit
`79cecc2` modifico `cambiar_formato_reunion_favorecer_participacion.json` (2
lineas, una de ellas de cambio). Es un candidato de una vuelta anterior corregido
en esta. Lo anoto y no lo juzgo aqui, porque su capitulo no es el mio.

**Los ocho pasan la comprobacion de forma**, corrida por mi contra
`esquema/nodo.schema.json`: los doce campos requeridos estan en los ocho, **el
`id` de dentro coincide con el nombre del fichero en los ocho**, y ninguno trae
guion largo ni guion medio.

---

## 2. MI TROCEO DEL CAPITULO, PIEZA A PIEZA

Barrido linea a linea de las 191. **Diez piezas, ocho con nodo.**

| # | pieza | lineas | encabezado | da nodo? |
|---:|---|---|---|---|
| 1 | Caption `AVOID` / `ASPIRE` | 13-15 | no | **NO** |
| 2 | Que es la cultura y por que se lee en lo que se cede | 17-29 | **no** | **SI** |
| 3 | `KNOW THE KIND OF TEAM YOU WANT TO BE A PART OF` | 31-79 | si | **SI** |
| 4 | `NEVER STOP TALKING ABOUT WHAT'S IMPORTANT` | 81-97 | si | **SI** |
| 5 | `ALWAYS WALK THE WALK` | 99-123 | si | **SI** |
| 6 | `CREATE THE RIGHT INCENTIVES`, cuerpo | 125-153 | si | **SI** |
| 7 | La conducta fuera de linea cuando no es estructural | 155 | no (dentro de 6) | **SI** |
| 8 | El reconocimiento de la decision dificil | 157 | no (dentro de 6) | **SI** |
| 9 | `INVENT TRADITIONS THAT CELEBRATE YOUR VALUES` | 159-187 | si | **SI** |
| 10 | Cierre, la suma de millones de acciones | 189-191 | **no** | **NO** |

**Cobertura: de la 13 a la 191 sin hueco y sin solape.** Las lineas 1-7 son la
cabecera de recorte, y 8, 9, 10, 12 y 16 son blancos o el rotulo del capitulo.

### Las dos piezas que NO dan nodo, y por que

**Pieza 1, el caption (13-15).** `AVOID` y `ASPIRE` son el pie de la vineta del
capitulo. Dos palabras sueltas sin procedimiento: **nombrar no es
procedimentar** (`P.5.1`). Cero nodos, y correcto.

**Pieza 10, el cierre (189-191).** Es resumen, no procedimiento. Lo que dice
ejecutable ya esta escrito dos veces en el propio capitulo: *"Pay attention to
your own actions"* (191) es la pieza 5, y *"what behaviors you are rewarding or
discouraging"* (191) es la pieza 6. **Extraerlo habria sido un REPITE de dos
candidatos de su misma vuelta.** No extraerlo es la lectura correcta.

### La particion de la pieza 6 en tres, que es la unica decision discutible del troceo

`CREATE THE RIGHT INCENTIVES` corre de 125 a 157 bajo un solo encabezado y sale
en **tres** candidatos. La sostengo, y la razon esta escrita en el propio libro:
**la linea 153 cierra con una regla de decision** (*"If you learn the issue is
primarily structural, make changes to your incentives"*) y **las lineas 155 y 157
son las dos ramas que cuelgan de ella**, la de la conducta que se sale y la del
acto dificil que merece reconocimiento. Cada rama trae disparador propio,
entregable propio y pasos propios: **es procedimiento en los dos lados**, que es
la vara de 6.1, y **no decide el tamanio del solape.**

**Lo que NO sostendria, y lo digo por si el reporte lo propone:** partir la pieza
3 en sus tres bloques impresos. Los tres bloques (`UNDERSTANDING YOUR CURRENT
TEAM`, `YOUR ASPIRATIONS`, `THE DIFFERENCE`) son **un solo ejercicio con una sola
caja de tiempo** (*"When you have an hour or so"*, linea 35) y **un solo
entregable**: el bloque tercero no se puede contestar sin los dos primeros
delante (linea 69, *"Where are the biggest gaps"*). Partirlo daria tres nodos que
nadie puede ejecutar por separado.

---

## 3. MI CLASIFICACION DE CADA CANDIDATO, CON SUS LINEAS

**El eje que mido aqui es `D.30`: TRANSCRIPCION (el paso esta en el libro) contra
PUENTE (el paso lo puso el extractor).** Los 57 pasos van uno a uno contra su
linea.

### 3.1. `juzgar_cultura_renuncias_equipo` -- 8 pasos, pieza 2

| paso | linea | veredicto |
|---:|---:|---|
| 1 preguntas que salen siempre de los candidatos | 17 | TRANSCRIPCION |
| 2 no la web corporativa sino lo que cede | 19 | TRANSCRIPCION |
| 3 el valor que nadie declararia al reves | 19 | TRANSCRIPCION |
| 4 las tres preguntas de contrapartida | 21 | TRANSCRIPCION |
| 5 el cartel de `Nothing at Facebook Is Somebody Else's Problem` | 21 | TRANSCRIPCION |
| 6 el becario, el servicio caido y el repaso posterior | 23-25 | TRANSCRIPCION |
| 7 cultura son normas y valores, y no va solo de tu relacion | 27 | TRANSCRIPCION |
| 8 a mas gente, mas papel; aunque no seas el consejero delegado | 29 | TRANSCRIPCION |

**Cero puentes.** Las cuatro preguntas del paso 1 estan las cuatro en la linea
17, y las tres del paso 4 estan las tres en la 21: **contadas, no estimadas.**

**Mi clase: SANO con arista pendiente.** El paso 6 arrastra el *postmortem* de la
linea 25, que es el procedimiento del nodo ya vivo `hacer_repaso_posterior_proyecto`.
**Entra como narracion de un caso, no como paso ejecutable**, asi que no es
REPITE; pero **el cable merece ponerse.**

### 3.2. `contrastar_cultura_actual_aspirada` -- 9 pasos, pieza 3

| paso | linea | veredicto |
|---:|---:|---|
| 1 la cultura como personalidad, exista o no la pienses | 33 | TRANSCRIPCION |
| 2 el mismo ejercicio del Cap. Cinco, y la interseccion | 35 | TRANSCRIPCION |
| 3 una hora y un boligrafo | 35 | TRANSCRIPCION |
| 4 **las siete** preguntas del equipo actual | 39,41,43,45,47,49,51 | TRANSCRIPCION |
| 5 **las cuatro** de las aspiraciones | 55,57,59,61 | TRANSCRIPCION |
| 6 **las cinco** de la diferencia | 65,67,69,71,73 | TRANSCRIPCION |
| 7 aspiraciones posibles y poco realistas, con el caso de la zona apartada | 75 | TRANSCRIPCION |
| 8 las subculturas, con sus tres casos | 77 | TRANSCRIPCION |
| 9 el paso siguiente es el plan de juego | 79 | TRANSCRIPCION |

**Cero puentes.** **He contado las preguntas del libro yo: 7 + 4 + 5 = 16**, y el
candidato reproduce las dieciseis. Ninguna inventada, ninguna caida.

**Mi clase: CONTINUA sobre `evaluar_cultura_empresa_adjetivos`** (`smart_who`,
ya en el grafo), que es **el vecino real de este candidato y el par mas serio de
la vuelta**. Lo adjudico leyendo los pasos de los dos, que es lo que manda `D.19`:

|  | `evaluar_cultura_empresa_adjetivos` (madre) | `contrastar_cultura_actual_aspirada` (hijo) |
|---|---|---|
| **quien lo hace** | el equipo de direccion reunido en una sala | tu solo, con un boligrafo |
| **que produce** | competencias para las tarjetas de puntuacion de todos los puestos | los huecos entre la cultura actual y la aspirada, y los obstaculos |
| **para que** | contratar por encaje cultural | cambiar la cultura de tu equipo |

**El solape es UNA pregunta** (los adjetivos que describen la cultura) **y fuera
del solape hay procedimiento en los dos lados**: la madre tiene la traduccion a
competencias, que el hijo no tiene; el hijo tiene el bloque de aspiraciones y el
de la diferencia, que la madre no tiene. **La bascula no decide, y aqui no haria
falta que decidiera** (6.1). **CONTINUA, con arista.**

### 3.3. `comunicar_valores_diez_formas` -- 9 pasos, pieza 4

| paso | linea | veredicto |
|---:|---:|---|
| 1 repetirse parecia de mal estilo | 83 | TRANSCRIPCION |
| 2 no rehuyas hablar de ello | 91 | TRANSCRIPCION |
| 3 diez veces y diez formas | 91 | TRANSCRIPCION |
| 4 recluta a otros | 91 | TRANSCRIPCION |
| 5 las cuatro vias | 93 | TRANSCRIPCION, **con un desvio, abajo** |
| 6 mete tus propios traspies | 95 | TRANSCRIPCION |
| 7 el metodo de Sheryl Sandberg | 85-87 | **DESVIO DE ATRIBUCION, abajo** |
| 8 lo que eso produce | 95 | TRANSCRIPCION |
| 9 lo que NO le ha pasado ni una vez | 97 | TRANSCRIPCION |

**Cero puentes de procedimiento, y DOS desvios de fidelidad que levanto yo:**

**(a) Paso 7, quien es el que no se acuerda.** El candidato escribe *"fijate en
que ella misma no recuerda cuando empezo, que es justamente el punto"*, y en un
paso cuyo sujeto es Sheryl Sandberg **"ella misma" se lee como Sheryl**. La linea
87 dice **`"I can't recall exactly when Sheryl started talking about hard
conversations, and that's precisely the point."`** La que no se acuerda es **la
autora**, no Sheryl. **Y el desvio se come el argumento**, que es justamente que
el mensaje calo tanto que quien lo recibio perdio el rastro de cuando empezo: si
la que no se acuerda es la emisora, no queda argumento ninguno. **Es una
atribucion cambiada en un fichero con `fidelidad: verbatim`**, y pido que se
corrija.

**(b) Paso 5, `top priorities`.** El candidato traduce *"notes to my entire staff
on our top priorities"* (linea 93) por **"notas a todo su equipo sobre las
prioridades de arriba"**. `top priorities` es **las prioridades principales**, no
las prioridades de la direccion: "de arriba" mete en el paso una jerarquia que la
linea no tiene. Menor, pero en un verbatim se corrige.

**Ninguno de los dos es PUENTE**: no aniaden un paso que no este, tuercen uno que
si esta. **Los cuento aparte y no en la metrica de la seccion 8**, y digo por que:
la metrica de volumen mide procedimiento inventado, y meter aqui un error de
traduccion inflaria la cifra que dimensiona el lote siguiente con algo que no es
lo que esa cifra mide.

**Mi clase: SANO.** No he encontrado vecino: la busqueda por `mensaje`, `repetir`
y `valor` sobre los 135 devuelve nodos de opinion (`asegurar_opinion_llega_persona`,
`dar_opinion_especifica_tarea`), cuyo objeto es **la opinion sobre el trabajo de
otro**, no la difusion repetida de un valor propio.

### 3.4. `vivir_primero_valor_declarado` -- 7 pasos, pieza 5

| paso | linea | veredicto |
|---:|---:|---|
| 1 los radares afinados, y la confianza que se pierde rapido | 101 | TRANSCRIPCION |
| 2 **los cinco** ejemplos de decir una cosa y hacer otra | 103,105,107,109,111 | TRANSCRIPCION |
| 3 si no vas a cambiar tu conducta, no lo saques a colacion | 113 | TRANSCRIPCION |
| 4 el caso de la revision de 360 grados | 115-119 | TRANSCRIPCION |
| 5 la leccion: hablaba de ello y no lo vivia | 121 | TRANSCRIPCION |
| 6 seguir practicando hasta que sea costumbre | 121 | TRANSCRIPCION |
| 7 se el primero en vivir el valor | 123 | TRANSCRIPCION |

**Cero puentes.** **Los cinco ejemplos son cinco** y estan los cinco, contados
contra las lineas 103 a 111.

**Mi clase: SANO.** El vecino que la busqueda levanta, `recoger_opinion_360_grados`,
comparte **el instrumento** (la revision de 360 grados) pero no el objeto: alli es
el procedimiento de recoger opinion, aqui es un caso narrado de como se descubrio
una brecha. **Una senial compartida no es un par** (`D.19`). Arista, no fusion.

### 3.5. `revisar_incentivos_trampas_equipo` -- 9 pasos, pieza 6

| paso | linea | veredicto |
|---:|---:|---|
| 1 la pieza final: premiar a quien se comporta y pedir cuentas a quien no | 127 | TRANSCRIPCION |
| 2 si no casan, cava mas hondo; el caso de la transparencia | 129 | TRANSCRIPCION |
| 3 las dos preguntas que cavan | 129 | TRANSCRIPCION |
| 4 desconfia de la regla simple; el caso de las tres exploraciones | 141 + 131-137 | TRANSCRIPCION |
| 5 lineas de codigo y pagar por palabra | 139 | TRANSCRIPCION |
| 6 la discusion franca, con sus dos preguntas | 141 | TRANSCRIPCION |
| 7 **las cuatro** trampas, con su caso cada una | 145,147,149,151 | TRANSCRIPCION |
| 8 reflexiona con regularidad; pregunta por que | 153 | TRANSCRIPCION |
| 9 si es estructural, cambia los incentivos | 153 | TRANSCRIPCION |

**Cero puentes.** **Las cuatro trampas son cuatro** y estan las cuatro con su
caso. El paso 4 cose la leccion de la linea 141 con la historia de las lineas
131-137, que es un reordenamiento del libro, **no un aniadido**: las dos partes
estan escritas.

**Mi clase: SANO frente al grafo, pero con una FRONTERA DE DOCTRINA que levanto
yo y que pido que se declare.** Es lo mas serio que encuentro en esta vuelta.

> #### FRONTERA: `revisar_incentivos_trampas_equipo` (Zhuo) contra `reconocer_recompensar_uso_metodo` (Smart, `Who`)
>
> **Los dos libros tiran de la misma palanca: atar premio o dinero a una conducta
> medida para instalar un valor. Y dicen lo contrario.**
>
> **`Who` lo prescribe**, y lo prescribe con numero. Sus pasos 3 y 4, ya en el
> grafo: *"Recompensa ademas a los directivos que consiguen una tasa de exito en
> contratacion del noventa por ciento o mejor"*, *"Ata esa recompensa ligando una
> parte sustancial de su retribucion variable a ese resultado concreto, y no a una
> valoracion general"*.
>
> **Zhuo lo desaconseja**, y desaconseja exactamente esa forma. Linea 141:
> *"These days, I'm wary of seemingly simple incentive rules that promise amazing
> results. They are rarely simple, and often leave collateral damage."* Y su
> trampa segunda, linea 147, es el caso de manual: **una prima decidida cada seis
> meses por una cifra de produccion empuja a elegir lo de poco impacto.** La
> recompensa de `Who` es una cifra unica de produccion atada a retribucion
> variable: **cae dentro de la descripcion de la trampa que Zhuo escribe.**
>
> **No es un duplicado y no se resuelve fundiendo.** `6.1`: *"DOS DOCTRINAS
> LEGITIMAS NO SON DUPLICADO: son FRONTERA DECLARADA, se escriben las dos
> posiciones con sus fuentes. Una frontera se pierde por poda, no por fusion."*
> **Se declara con sus dos citas y las dos se quedan.**

### 3.6. `actuar_conducta_contraria_valores` -- 5 pasos, pieza 7

Los cinco salen de **la linea 155**, entera y sin sobras:

| paso | ancla en la linea 155 | veredicto |
|---:|---|---|
| 1 aun asi tienes que actuar | `you must still take action` | TRANSCRIPCION |
| 2 el ambiente de respeto y el que grita | `an atmosphere of respect` / `shouting rudely at a teammate` | TRANSCRIPCION |
| 3 si no haces nada, mandas el mensaje de que lo toleras | `you risk sending the message that you tolerate` | TRANSCRIPCION |
| 4 las dos formas de rebajar la tension | `asking the shouter to calm down or help them leave the room` | TRANSCRIPCION |
| 5 despues, en privado, que es inaceptable | `Later, in private, tell them that what they did is unacceptable` | TRANSCRIPCION |

**Cero puentes.** El corte entre el momento y el despues en privado **lo escribe
el libro**, no el extractor: la palabra `Later` esta en la linea.

**Mi clase: CONTINUA sobre `resolver_desencaje_valores_persona_equipo`** (Zhuo,
capitulo anterior, ya en el grafo). Con la vara y con direccion, que es lo que
pide 6.1, **preguntando que aniade el hijo a la madre**:

|  | `resolver_desencaje_valores_persona_equipo` (madre) | `actuar_conducta_contraria_valores` (hijo) |
|---|---|---|
| **disparador** | un desalineamiento **repetido** con lo que el equipo valora | **un acto suelto** que se sale de linea |
| **plazo** | meses, cuatro reuniones, un movimiento interno | el momento, y "despues, en privado" |
| **salidas** | mover dentro de la organizacion, o separar caminos | rebajar la tension, y decirlo en privado |

**Lo que queda fuera del solape es procedimiento en los dos lados**, y es
procedimiento distinto: la madre no tiene nada que hacer en el momento en que se
oye el grito, y el hijo no llega nunca a la separacion de caminos. **CONTINUA,
con arista.**

### 3.7. `reconocer_decision_dificil_valores` -- 4 pasos, pieza 8

Los cuatro salen de **la linea 157**:

| paso | ancla en la linea 157 | veredicto |
|---:|---|---|
| 1 reconocele el acto dificil en el espiritu de los valores | `recognize them for it` | TRANSCRIPCION |
| 2 los tres casos nombrados | `passing up a lucrative sales deal` / `firing a star performer` / `admitting openly` | TRANSCRIPCION |
| 3 admitele que fue dificil | `Acknowledge that it was hard` | TRANSCRIPCION |
| 4 dale las gracias | `thank them for doing the right thing` | TRANSCRIPCION |

**Cero puentes.** **Los tres casos son tres.**

**Es el candidato mas fino de la vuelta y el unico que yo habria marcado
discutible por tamanio**, con cuatro pasos de los que uno es un inventario de
ejemplos. **Y aun asi lo sostengo, por `D.30`:** *un parrafo pobre no produce un
nodo pobre, produce un nodo inventado*. El libro escribe cuatro actos; el
candidato escribe cuatro pasos; **engordarlo habria sido puente.** La delgadez
del nodo es la delgadez del parrafo, y esa es la lectura honesta.

**Mi clase: SANO.** El vecino que levanta la busqueda,
`reconocer_recompensar_uso_metodo` (`Who`), **reconoce por usar un metodo de
contratacion**, no por sostener un valor a costa propia: disparador distinto y
entregable distinto. Arista, no par.

### 3.8. `inventar_tradiciones_celebrar_valores` -- 6 pasos, pieza 9

| paso | linea | veredicto |
|---:|---:|---|
| 1 hay poder en los ritos, unicos y divertidos como tu equipo | 169 | TRANSCRIPCION |
| 2 el hackathon | 165 | TRANSCRIPCION |
| 3 lo que el rito hizo concreto: `Be Bold` y `Move Fast` | 167 | TRANSCRIPCION |
| 4 **los seis** ejemplos de tradiciones | 173,175,177,179,181,183 | TRANSCRIPCION |
| 5 el turno de preguntas de los viernes, mas de diez anios | 185 | TRANSCRIPCION |
| 6 la razon: la apertura, y si el no da ejemplo, por que nadie mas | 187 | TRANSCRIPCION |

**Cero puentes.** **Los seis ejemplos son seis**, contados contra las lineas 173
a 183, y cada uno conserva **su valor asociado**, que es lo que los hace
utilizables: la creatividad y la mentalidad del principiante en las noches de
pintar, la autenticidad y el aprendizaje en el fallo de la semana.

**Nota de forma, sin consecuencia de clase:** los pasos 5 y 6 escriben *"el
fundador de la casa"* donde la linea 185 dice **`Mark Zuckerberg`** por su nombre.
Es una perifrasis, no un error: **no cambia ni el hecho ni la atribucion**, y el
libro esta citado en `fuentes`. Lo anoto y no pido corregirlo.

**Mi clase: SANO.** Sin vecino en los 135. Es el unico candidato del capitulo
cuyo entregable es **un objeto nuevo** y no la revision de algo que ya existe.

---

## 4. `PASOS INVENTADOS POR CAPITULO`, MEDIDO POR MI (seccion 8)

**La firmo yo sobre el artefacto que tengo delante, y digo exactamente que
artefacto es.**

| capitulo | unidad del libro | candidatos | pasos escritos | pasos PUENTE | por ciento |
|---|---|---:|---:|---:|---:|
| `cap_11` | Cap. 10, `Nurturing Culture` | 8 | **57** | **0** | **0,00** |
| `cap_12` | Epilogo | 0 | 0 | -- | **no aplica** |

Los 57 salen de contar yo los `pasos_accionables` de los ocho ficheros:
8 + 9 + 9 + 7 + 9 + 5 + 4 + 6 = **57**. Los cero puentes salen de las ocho tablas
de la seccion 3, paso por linea.

> ### PERO ESTA CIFRA TIENE UNA SEGUNDA LECTURA Y NO LA PUEDO CERRAR A CIEGAS
>
> **Mi 0,00 por ciento mide el fichero commiteado.** El asunto del commit `b7aadb2`
> dice *"dos puentes mios cazados y corregidos"*. **Si esos dos puentes se
> escribieron y se corrigieron antes de commitear, la seccion 8 los cuenta**: la
> formula dice *"de todos los pasos que el extractor ESCRIBIO en un capitulo,
> cuantos RESULTARON ser PUENTE"*, y un paso corregido antes del commit se
> escribio igual. **Esa lectura da 2 / 57 = 3,51 por ciento.**
>
> **Las dos lecturas quedan por debajo del freno del 10 por ciento** (8.1,
> decision del fundador del 11 sep), **asi que el lote 4 corre a CUATRO capitulos
> por vuelta en cualquiera de las dos.** La eleccion entre 0,00 y 3,51 no mueve
> el volumen de nada, y por eso la dejo abierta en vez de firmarla a ciegas.
>
> **Lo que cierro sin depender del reporte:** el artefacto que viaja en el repo
> **no contiene ni un paso inventado**, y eso lo he verificado paso por linea.
> **Y el asunto de un commit no es sede de cifra** (5.6), asi que el "dos" lo
> traigo como afirmacion a verificar, no como medida.

**Verificacion de 8.3, punto 2, que es la que esta metrica pide de verdad:**
*"relee una muestra de los pasos marcados TRANSCRIPCION contra su parrafo,
porque el error que esta metrica invita a cometer es marcar un puente como
transcripcion, porque baja la cifra y sube el volumen del lote siguiente."*
**No he releido una muestra: he releido los 57.** El capitulo es corto, 191
lineas, y con ocho candidatos la muestra habria costado mas de explicar que de
correr. **Y el resultado es lo que hace creible la cifra**: cuando conte los
inventarios del libro uno a uno (16 preguntas, 5 ejemplos, 4 trampas, 6
tradiciones, 3 casos, 3 preguntas de contrapartida), **todos cuadraron con el
libro y ninguno sobraba.** Un extractor que inventa pasos infla los inventarios,
y aqui no hay ninguno inflado.

---

## 5. `cap_12`: MI JUICIO PROPIO DE QUE NO DA NINGUN NODO

El commit `e14b208` no aniade ningun fichero a la cuarentena. Lo verifico yo
abriendo las 449 lineas:

| lineas | que hay | da nodo? |
|---:|---|---|
| 1-7 | cabecera de recorte, `unidad: Epilogue`, `titulo_textual: The Journey Is 1% Finished` | no |
| 9-15 | rotulo y caption `THE MYTH` / `THE REALITY` | no |
| **17-33** | **el epilogo entero**, 8 parrafos | **NO** |
| 35-55 | `Acknowledgments` | no |
| 57-194 | `Notes`, la bibliografia por capitulos | no |
| 195-449 | `Index` | no |

**El epilogo no da nodo, y es un juicio de lectura y no de formato.** Los ocho
parrafos son **recuerdo en pasado y deseo en futuro**, y no hay un solo
imperativo ejecutable. La unica frase con forma de instruccion es la ultima,
linea 33: *"Go out with your team and make something wonderful together."* **Una
exhortacion no ejecuta nada**: es exactamente el caso de `6.1`, *una advertencia
es linea, una postura no ejecuta una busqueda.* Y lo mas cercano a un metodo,
linea 27 (*"with time, will, and a growth mindset"*), **es el nombre de un nodo ya
vivo**, `cambiar_mentalidad_fija_crecimiento`: nombrarlo no es procedimentarlo
(`P.5.1`), asi que extraerlo habria sido un REPITE.

**Cero candidatos de `cap_12` es la lectura correcta, y la firmo.**

**Y con eso el lote 3 queda en 12 de 12 ficheros minados.**

---

## 6. LO QUE MIDO YO Y NO ME HA PEDIDO NADIE

### 6.1. Los once veredictos de `cap_11` no tienen sede duradera ahora mismo

El asunto de `b7aadb2` habla de *"once veredictos que la aduana no pidio"*.
**Busque los ocho ids en la bitacora y no hay ninguno:**

    busqueda de los 8 ids en bitacora/VEREDICTOS.jsonl  ->  0 coincidencias
    git log --oneline -- bitacora/VEREDICTOS.jsonl      ->  ultimo toque 3ad8998

`3ad8998` es anterior a la vuelta 12. **La busqueda negativa esta corrida y la
cito con su comando** (seccion 1). **No lo llamo caida**, y digo por que: el
`LEEME.md` de la cuarentena dice que el veredicto **lo escribe la aduana en la
insercion**, y estos ocho no se han insertado. **Es coherente con `D.26`.**

**Pero lo dejo dicho igual, porque es un riesgo y no un fallo:** once
adjudicaciones de un auditor que hoy **solo viven en `REPORTE.md`**, que es la
sede que se reescribe cada vuelta (5.2). **Si el lote 3 se inserta dentro de tres
vueltas, esos once razonamientos ya no estaran en ningun sitio.** Lo traigo a mi
acta como candidato a encargo.

### 6.2. Los ocho llegan con `nodos_previos` y `nodos_siguientes` vacios

Los ocho traen las dos listas en `[]`. **Verifique que eso es lo normal de esta
casa y no un olvido**: los 135 nodos del grafo **tambien** las traen vacias, y
las aristas viven en el campo `arista` de `bitacora/VEREDICTOS.jsonl` (59 de 100
veredictos la traen). **Asi que no es una caida.** Pero vale lo mismo que 6.1:
las aristas que yo levanto en la seccion 3 (con `hacer_repaso_posterior_proyecto`,
con `evaluar_cultura_empresa_adjetivos`, con `resolver_desencaje_valores_persona_equipo`
y con `recoger_opinion_360_grados`) **no tienen donde escribirse hasta la
insercion.**

### 6.3. La contabilidad de la bandeja cuadra, y la verifique contra el grafo

| carpeta | ficheros | de ellos en el grafo |
|---|---:|---:|
| `cuarentena/zhuo_manager/` | 68 | **0** |
| `cuarentena/_insertados/zhuo_manager/` | 68 | **68** |
| `cuarentena/smart_who/` | 0 | 0 |
| `cuarentena/_insertados/smart_who/` | 59 | **59** |
| `cuarentena/_insertados/onu_consumidor/` | 6 | **6** |

**`D.31` se cumple en los tres lotes: ningun insertado sigue en la bandeja**, asi
que el informe del lote no va a dar ni un `CAERIA: el id ya vive en el grafo` por
esa causa. Y la suma cierra: 68 + 59 + 6 = 133, mas los dos semilla = **135**, que
es el conteo del dataset.

**Los 60 de `ORDEN_DE_LOTES.md` son ahora 68**, y esta bien: aquella cifra esta
fechada *"AL CIERRE DE LA VUELTA 12"* y los ocho de `cap_11` son de la 13. **Se
actualiza, no se corrige.**

**Y una ambiguedad de redaccion en esa misma linea**, que senialo sin llamarla
caida: dice *"60 candidatos en `cuarentena/zhuo_manager/` **y 68 archivados en
`cuarentena/_insertados/zhuo_manager/`, SIN INSERTAR**"*. **Los 68 archivados SI
estan insertados**, los 68 contra el grafo lo dicen. El "SIN INSERTAR" solo puede
referirse a los de la bandeja, y asi leido es verdad; pegado al final de la frase
se lee de la otra manera. **Merece una coma o un punto.**

### 6.4. Las dos condiciones de apertura del lote 4, medidas (`D.32`)

Si el lote 3 cierra su extraccion, `D.32` manda medir las dos condiciones del
lote siguiente y publicarlas. **Segun `ORDEN_DE_LOTES.md` el lote 4 es
`scott_radical_candor`.** Las mido ahora:

| condicion | comando | medida | |
|---|---|---|---|
| el material esta en `fuentes/<clave>/` | `ls fuentes/scott_radical_candor/ \| wc -l` | **15 ficheros**, `cap_00.md` a `cap_14.md` | **VERDE** |
| la clave esta en la tabla canonica | lectura de `fuentes/FUENTES_CANONICAS.json` | **`scott_radical_candor` presente** | **VERDE** |

**Las dos en verde.** La tabla de lotes da 15 capitulos para ese libro y la
carpeta trae 15 ficheros: **cuadran**. Lo dejo medido aqui para no tener que
medirlo despues de haber visto el reporte.

### 6.5. El informe de los 68 arranco y no consta terminado

`.informe_lote.txt` esta sin seguir por git (`??`) y contiene **una sola linea**:

    ARRANQUE: 2026-09-11T14:06:55

El commit `06122d6`, de las 14:06:47, dice que commitea la prediccion **antes** de
correr el informe. **El arranque esta escrito ocho segundos despues y no hay
linea de cierre**, asi que **el informe de los 68 no consta terminado en el arbol
que yo leo.** Lo anoto como estado medido; **no lo interpreto**, porque la razon
de que el turno se cortara ahi no esta en ningun fichero que yo pueda abrir sin
romper la ceguera.

---

## 7. RESUMEN DE MI CLASIFICACION, PARA COMPARARLO CON EL REPORTE

| candidato | mi clase | mi vecino | puentes |
|---|---|---|---:|
| `juzgar_cultura_renuncias_equipo` | **SANO** | arista a `hacer_repaso_posterior_proyecto` | 0 |
| `contrastar_cultura_actual_aspirada` | **CONTINUA** | `evaluar_cultura_empresa_adjetivos` (`Who`) | 0 |
| `comunicar_valores_diez_formas` | **SANO** | -- | 0 (+2 desvios de fidelidad) |
| `vivir_primero_valor_declarado` | **SANO** | arista a `recoger_opinion_360_grados` | 0 |
| `revisar_incentivos_trampas_equipo` | **SANO + FRONTERA** | `reconocer_recompensar_uso_metodo` (`Who`) | 0 |
| `actuar_conducta_contraria_valores` | **CONTINUA** | `resolver_desencaje_valores_persona_equipo` | 0 |
| `reconocer_decision_dificil_valores` | **SANO** (fino, y lo sostengo) | -- | 0 |
| `inventar_tradiciones_celebrar_valores` | **SANO** | -- | 0 |

**Piezas: 10. Con nodo: 8. Huecos: 0. Solapes: 0.**
**`cap_12`: 0 candidatos, y firmado que es lo correcto.**
**Pasos: 57. Puentes en el artefacto: 0. Lectura alternativa con los dos
declarados en el commit: 3,51 por ciento. Las dos por debajo del freno de 10.**

**Lo que traigo pedido cuando se me destape el reporte:**

1. **La correccion del paso 7 de `comunicar_valores_diez_formas`**, que cambia
   quien no se acuerda. Es el unico hallazgo mio que toca el contenido de un
   candidato.
2. **La frontera Zhuo contra `Who` sobre atar premio a cifra**, declarada con sus
   dos citas y sin fundir ninguno de los dos nodos.
3. **Los dos pares CONTINUA** de 3.2 y 3.6, por si el reporte los clasifico de
   otra manera o no los vio.
4. **Donde van a vivir los once veredictos y las aristas** hasta que el lote se
   inserte.

---

**Fin de la apertura ciega. No he abierto `REPORTE.md`, `loop.log`,
`ultimo_extractor.json` ni `ultimo_auditor.json`. No commiteo: el arnes sella
este fichero, y no vuelvo a tocarlo.**
