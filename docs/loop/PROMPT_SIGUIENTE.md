# ENCARGO DE LA VUELTA 7. Lote 2, `smart_who`: Cap. 5 (`Sell`) y Cap. 6 (`Your Greatest Opportunity`)

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO PRIMERO, Y NO ES UNA TAREA: **ESTA VUELTA PUEDE CERRAR EL LOTE 2**

Quedan **dos unidades de siete**, y son las dos ultimas del libro. Si las dos caben,
`smart_who` queda **leido entero** y el acta que venga detras decide el volumen del
lote 3. **Si solo cabe la primera, la segunda no se empieza**, que es exactamente lo
que funciono en la vuelta 6 y no es un fallo.

### Tu material, nombrado por LINEA y no por fichero

**Las cifras de esta tabla las midio el auditor con `awk` en la vuelta 6 (ACTA 6
seccion 1.8) y reproducen contra las tuyas.** La del Cap. 5 **lleva la correccion**
que tu discutible 3 gano:

| unidad | titulo | donde vive | bloques | palabras |
|---|---|---|---:|---:|
| **Cap. 5** | `Sell: The Top Five Ways to Seal the Deal` | **`cap_05.md` L363 a L365** mas **`cap_06.md` L9 a L455** | 226 | **11.339** |
| **Cap. 6** | `Your Greatest Opportunity` | **`cap_07.md` L9 a L429** | por medir | **3.849** |
| | **el tramo abierto de la vuelta** | | | **15.188** |

**`cap_06.md` MUERE EN L455 y eso esta medido**, no heredado: tu cuarta comprobacion
de la vuelta 6 lo probo y el auditor lo repitio. **El Cap. 5 no se derrama a
`cap_07.md`.**

**LO QUE NO SE SABE Y NO SE ADIVINA: donde empieza y acaba el Cap. 6 dentro de
`cap_07.md`.** El `L9 a L429` es el rango que tu propia cola declaro. **Lo
compruebas tu con las cuatro lineas de apertura y mandas tu medida**, como en 0.c.

## LAS COMPROBACIONES DE APERTURA, LAS CUATRO, SOBRE `cap_06.md` Y `cap_07.md`

**Su resultado va como fila propia y ANTES de la TAREA 1.**

1. `ls fuentes/smart_who/`
2. que `smart_who` este en `fuentes/FUENTES_CANONICAS.json`
3. `head -8` de **los dos** ficheros: que `unidad` y `titulo_textual` sean los que
   esta tabla anuncia
4. **la cuarta, que es tuya y ya se adjudico a favor dos veces:**
   `grep -n '[^[:space:]]' <fichero> | tail -1` sobre **los dos**, para saber donde
   muere de verdad cada uno

**Si alguna sale en rojo, mandas TU medida, no este parrafo.**

## EL ESTADO CONTRA EL QUE ABRES, MEDIDO POR EL AUDITOR EN `1788173`

| medida | cifra |
|---|---:|
| nodos vivos en el dataset | **8** (43 pasos, 2 relaciones, 4 extremos) |
| veredictos en `bitacora/VEREDICTOS.jsonl` | **2** |
| candidatos en `cuarentena/smart_who/` | **32** |
| pasos en la bandeja | **197** |
| informe del lote en seco | **32 revisados, 32 ENTRARIAN**, 0 bloquean, 0 caen, 0 chocan |
| pares que levantarian sobre los 32 | **44 de 992**: 0 similitud, 36 familia, 14 paso contra nodo, **8 solo señal 3** |
| fuentes canonicas registradas / en uso | **13 / 2** |
| unidades del lote 2 leidas | **5 de 7** |

**Las nueve filas estan remedidas por el auditor con sus propios comandos y todas
reproducen contra tu C.6.2. Si alguna no te reproduce, la declaras: no la copias.**

---

## TAREA 1. LOS REGISTROS DEL ACTA 6, Y SU PRIMERA MITAD ES BLOQUEANTE

### 1.a. **BLOQUEANTE: EL COMPARATIVO SE DIVIDE ANTES DE ESCRIBIRSE**

**Esto no es un consejo y va antes que ninguna lectura del libro. Es la escalada de
una racha, encargada y no solo declarada** (`AUDITOR_FORJA.md` seccion 1 punto 4).

**LA RACHA, CON SU CIFRA:**

    CLASE                  0 de 2 tandas seguidas
    CIFRA PUBLICADA        0 de 2 tandas seguidas
    REPORTE que acumula    2 de 3 tandas seguidas   <-- la vuelta 6 lo puso en 2

> **UNA SOLA CIFRA FALSA EN TABLA, CABECERA O CONCLUSION EN ESTA VUELTA PARA EL
> BUCLE.**

**LAS DOS CAIDAS DE LA VUELTA 6, para que sepas exactamente contra que es el
remedio.** Las dos son **cifras correctas con un comparativo que no reproduce**:

| # | lo que escribiste | lo que sale al dividir |
|---:|---|---|
| 1 | *"97 pasos, **casi el doble** que los 104 de las tres tandas anteriores JUNTAS"* (4.b) | **97 es MENOR que 104.** Era *casi tantos como las tres juntas* |
| 2 | *"la densidad de vecinos por par **CAYO a la mitad**: 13,97 a 4,44"* (2.i y otra vez en 4.e) | **4,44 es el 31,8 por ciento de 13,97: cayo a menos de un TERCIO.** A la mitad seria 6,99 |

**LAS DOS VIVEN EN CONCLUSION Y POR ESO ACUMULAN** (5.2). **Ninguna movio un dato**,
y la segunda incluso **subestima** tu propio resultado. **No es tu metodo: de los
once comparativos del tramo, el auditor verifico NUEVE correctos uno a uno**
(*casi duplico* 17 a 32 = 1,88; *un 16 por ciento* 38 a 44; *mas del doble de
palabras y poco mas del doble de nodos* = 2,07 y 2,14; *un 14 por ciento*; *un 59
por ciento*; *un 0,13 por ciento*; *la mitad de capitulos*; *menos puentes que el
Cap. 3*). **Es cuidado que se afloja donde la frase suena bien.**

> **EL REMEDIO, y es la gemela exacta del que ya te funciono:** antes de teclear
> **doble, mitad, triple, un tercio, casi** o cualquier comparativo, **haces la
> division y escribes el cociente al lado**. Si el cociente no sale, **el
> comparativo no se escribe: se ponen las dos cifras a secas.**

**Y LA BUENA NOTICIA, QUE TE GANASTE Y SE DICE PRIMERO PARA QUE SE SEPA QUE ESTO
FUNCIONA:** el remedio de la vuelta 5 (*una cita de linea se reabre antes de
publicarse*) **lo aplicaste y funciono**. El auditor abrio con `sed -n` **unas
cuarenta citas de linea** de tu tramo, incluidas las catorce preguntas de L147, las
diez banderas de L275 a L293 y los ocho descarriladores de L301 a L315. **Cero
punteros rotos.** La caida de especie de la vuelta 5 **no se repitio.**

**ESTO ES UNA LINEA DE DISCIPLINA, NO UN PROGRAMA. NO escribas una guarda para
esto** (moratoria de maquinaria, `EXTRACTOR.md` 13).

### 1.b. LA CORRECCION DECLARADA, y esta vez el fallo era del auditor

**Se anota junto a la tabla de unidades del encargo de la vuelta 6, sin borrar el
texto viejo**, en tu reporte, donde la cites:

> **CORRECCION DECLARADA (auditor, ACTA 6 seccion 3.3, 10 sep 2026).** El encargo de
> la vuelta 6 publica **Cap. 5 = 11.370 palabras**. **La cifra correcta es 11.339.**
> El 11.370 incluye la **cabecera YAML L1 a L7 de `cap_06.md`**, 31 palabras que no
> son del libro. **La celda mala era del auditor: la fila del Cap. 4 se conto por
> RANGO y la del Cap. 5 por FICHERO, dos varas en la misma tabla.** Tu discutible 3
> queda **SOSTENIDO** y tu medida es la que manda.

**No la copias: la reabres.** Corre tu `awk` sobre los dos rangos antes de anotarla.

### 1.c. LAS ARISTAS PENDIENTES, EN BLOQUE PROPIO Y TITULADO

*`D.29`: una arista que solo vive en la prosa de un reporte se pierde. Este bloque
se reescribe entero cada vuelta hasta que la insercion las cablee.*

**Van las NUEVE que dejaste declaradas** (las tres de tu 1.b mas las seis de tu 2.h)
**y las que el Cap. 5 y el Cap. 6 abran.** Ninguna se cablea: una arista se cablea
contra ids que ya viven.

**Y LA QUE ESTE CAPITULO CIERRA, que es la que mas importa:** `Sell` es el **CUARTO
y ultimo hijo** de `aplicar_metodo_ghsmart_contratacion`, y tu
`decidir_contratacion_final` **ya apunta a el** por su paso 7 sin nombrar un id que
no existia. **Ahora existira.** Escribelo con la cabeza nombrada en su prosa o en
sus `condiciones_activacion`, para que se cablee por lectura y no por memoria.

### 1.d. LAS SEIS ADJUDICACIONES DEL ACTA 6, recogidas y no reabiertas

| # | tu discutible | como quedo |
|---:|---|---|
| 1 | los pares **cabeza contra hijo** son cola util | **SOSTENIDO EN LA MEDIDA, ACOTADO EN LA RAZON.** Ver 1.e, porque es el unico que te cambia algo |
| 2 | **la tactica 4 no da nodo** | **SOSTENIDO.** El manual 3.4 dice **como se corta** una serie; `EXTRACTOR.md` 9 dice **que es un nodo**. Dos reglas sobre dos cosas, y el arbitro es el escrito. **Una serie numerada PUEDE dar menos hijos que numeros** |
| 3 | **la unidad son 11.339 y no 11.370** | **SOSTENIDO, y la celda mala era del auditor** (1.b) |
| 4 | **la remision interna de L195 vale** | **SOSTENIDO**, y con su linea escrita en 1.f |
| 5 | **el id en castellano sin `who`** | **SOSTENIDO.** `who` es NEGRA **por criterio**: tiene equivalente corriente (*quien*), no es apellido y no es sigla. Y `mitos_stage_gate` (`EXTRACTOR.md` 15.1) cierra la defensa del nombre de metodo. **Aplicaste el criterio donde el modulo no tiene la pieza, y eso es lo que la Regla 1 del 10 sep autoriza** |
| 6 | **editar `ultimo_auditor.json`** | **NO FUE INVASION DE SEDE.** Ver 1.g |

**Ninguna se reabre.** Se recogen y se sigue.

### 1.e. LA ACOTACION DEL DISCUTIBLE 1, que es la unica que te cambia como trabajas

**El auditor sostiene tu MEDIDA: los cuatro pares cabeza contra hijo son cola UTIL,
no cola falsa.** Una señal cuyo producto es un CONTINUA y una arista que el grafo
necesita ha hecho trabajo.

**Y te tumba UNA FRASE, la de *"el veredicto se sabe antes de abrir el par, es
CONTINUA por construccion"*.** Va contra `D.19` (*una discrepancia NUNCA se adjudica
citando una señal*) y contra la vara (*LA ARISTA NO EXCULPA*).

**La prueba esta en tu propio par B:** los pasos 1 y 5 de
`calificar_tarjeta_puntuacion_habilidad_voluntad` son **transcripcion literal del
punto 4 del recuadro**, lo mismo que comprime el paso 4 de la cabeza. **Si ese hijo
se hubiera quedado en esos dos pasos, el veredicto correcto seria REPITE.** Es
CONTINUA **porque existen sus pasos 2, 3, 4 y 6** (el umbral del noventa por ciento
resultado a resultado y competencia a competencia, la diana con sus dos condiciones
y la definicion de jugador A, verificados contra `cap_05.md` L259 a L265). **Y eso
solo se sabe leyendo.**

> **QUEDA ADJUDICADO ASI, Y LO APLICAS EN ESTE CAPITULO:** *cabeza contra hijo* es
> una clasificacion legitima **para medir el coste de la cola** y se publica. **NO
> es un veredicto anticipado y NO autoriza a saltarse la lectura de un solo par.**
>
> **Y ES UN AVISO CONCRETO PARA EL Cap. 5:** el riesgo de gemelo **es mayor en los
> hijos CORTOS de una serie numerada**. Si `Sell` trae otro recuadro de cinco, sus
> hijos de tres pasos son donde hay que mirar. **Un hijo que solo repite el paso que
> la cabeza comprime no es un hijo: es un duplicado con cable.**

**Lo que NO se adjudica y no afirmas:** si la calibracion del 9 sep queda tocada.
**Es una medida sobre 3.169 nodos que esta casa no ha corrido.** Lo mides en tu
bandeja y lo dices; no lo extiendes.

### 1.f. LA LINEA DE LA REMISION INTERNA, que sale de tu discutible 4

**No es *"falta el recuadro, sirve la prosa"*, que seria una puerta abierta:**

> **UNA REMISION INTERNA DEL LIBRO VALE COMO INVENTARIO SI, Y SOLO SI, EL TEXTO AL
> QUE REMITE ESTA EN LA FUENTE.** Si esta, leerla es leer. **Si no esta, la remision
> es una promesa que la fuente no cumple, y transcribirla es INVENTAR.**

**No es doctrina nueva:** es `D.30` aplicado a una remision en vez de a un parrafo.

**Y SE TE CUENTA A FAVOR QUE YA LA APLICABAS SIN TENERLA ESCRITA:** en L105 (*"see
box above"*) el recuadro **no esta** y te negaste a escribir las preguntas de la
entrevista enfocada; en L195 el texto remitido **si esta** (`cap_04.md` L71 y L75) y
lo transcribiste. **Las dos decisiones son la misma regla saliendo al reves.**

### 1.g. EL ARTEFACTO DEL ARNES, con su limite escrito

**Tu sexto discutible queda SOSTENIDO: no invadiste ninguna sede.**
`docs/loop/ultimo_auditor.json` **no esta en la lista de sedes del auditor**
(`AUDITOR_FORJA.md` 5.6) ni en la tabla de `EXTRACTOR.md` 14, el arnes lo reescribe
cada turno, **hoy mide 0 bytes**, y `EXTRACTOR.md` 6 te ordena no saltarte el hook.
**Hiciste lo que se te mando.**

> **Y SU LIMITE, para que no crezca: un ARTEFACTO DEL ARNES se puede corregir en lo
> MINIMO para que el hook pase, y la correccion se declara en el reporte. Nunca se
> vuelve un sitio donde escribir contenido.**

---

## TAREA 2. EL Cap. 5 ENTERO, `Sell: The Top Five Ways to Seal the Deal`

**`cap_05.md` L363 a L365 mas `cap_06.md` L9 a L455. 11.339 palabras, 226 bloques.**
El ciclo completo, en el orden de siempre y **sin intercambiar el paso 2 con el 3**:

1. **LA FRONTERA, PUBLICADA ANTES DE CORTAR NADA**, pieza a pieza y con su rango de
   linea, **cada linea reabierta con `sed -n` antes de teclearse**. Con la prueba del
   inventario de `D.27` pasada a cada pieza, y **la razon de las que NO entran, una
   por una y sin agruparlas** si no es la misma razon.
2. **LOS CANDIDATOS, uno a uno**, con el ciclo de cinco pasos y **la aduana EN SECO
   en el mismo acto** (`python forja.py informe cuarentena/smart_who/<id>.json`).
3. **LA TABLA DE MARCADO VA EN TU REPORTE**, no dentro del JSON, con **el parrafo
   citado en cada puente**. Ver la TAREA 4 para lo que tiene que traer el saldo.
4. **LAS ARISTAS QUE EL CAPITULO ABRE**, todas, y **ninguna se cablea**.
5. **LOS VECINOS, REMEDIDOS AL CIERRE DEL CAPITULO** sobre la bandeja entera con
   `src.aduana.medir`. **Remedidos, no arrastrados**, que es el remedio de la vuelta
   4 y lleva dos vueltas funcionando.

### Lo que este capitulo tiene de especial, y conviene saberlo antes

- **`Sell` cierra el metodo A.** Es el cuarto paso, y sus tres hermanos ya estan en
  la bandeja. **Es el capitulo con mas familia delante de toda la campaña**, asi que
  la señal 2 puede comportarse distinto que en el Cap. 4, donde solo subio 2 pares
  sobre 720 comparaciones nuevas. **Lo mides, no lo predices.**
- **El titulo promete una serie de CINCO.** Si la trae, se corta por manual 3.4: **un
  nodo por paso mas UNA cabeza, jamas dos compresiones de la misma numeracion.** Y
  con la adjudicacion del discutible 2 delante: **si uno de los cinco no es
  procedimiento, no da nodo, y se dice por que.**
- **Y con 1.e delante:** si sale esa serie, **sus hijos cortos son donde hay que
  mirar el gemelo.**

### LA QUINTA ESPECIE, que sigues llevando delante

**El caso ascendido a doctrina: el libro cuenta lo que alguien HIZO y el paso lo
escribe como lo que TU tienes que hacer. El detector no es la ausencia, es el
EJECUTOR:** ante cada paso en tercera persona, **quien lo ejecuta**. Si la respuesta
es un nombre propio del libro y no el lector, es caso.

**La vuelta 6 midio algo con esto y conviene que lo sepas al empezar:** llevarla
nombrada **no cambio cuantos puentes escribiste, cambio CUANDO los viste** (los tres
se cazaron en el acto, no al releer). **Los tres fueron de esta especie, tres de
tres.** Y **los tres salieron de tramos de caso CORTOS y pegados al mandato**
(Sharpe una frase, Haugen dos bloques, Jordan un bloque), **mientras que del caso de
26 bloques no salio ninguno.**

> **NO ES EL VOLUMEN DE CASO LO QUE FABRICA PUENTES: ES SU ENTRETEJIDO CON EL
> MANDATO.** Esa lectura es tuya, la sostuvo el auditor, y **el sitio donde mirar en
> el Cap. 5 es la frase de caso metida dentro de un parrafo de instrucciones**, no
> la anecdota larga.

**Y LA LINEA DEL PARTICULAR, que sigue vigente:** un particular de un caso entra en
un paso **solo si (a) el libro lo manda fuera del caso y (b) el paso lo atribuye en
su propio texto.** Si falta cualquiera de las dos, va al `resumen_teorico` con su
dueño delante.

---

## TAREA 3. EL Cap. 6, `Your Greatest Opportunity` (`cap_07.md` L9 a L429)

**Mismo ciclo entero que la TAREA 2.**

> **SI EL Cap. 5 SOLO YA LLENA EL TRAMO, EL Cap. 6 NO SE EMPIEZA. Eso no es un
> fallo: es el tramo funcionando**, y la vuelta 6 lo demostro con el Cap. 4.

**El techo sigue siendo el de `EXTRACTOR.md` 12.4: entre cinco y quince candidatos
por vuelta.** Y la adjudicacion 8 del ACTA 4 sigue en pie: **que una vuelta llene el
techo con un solo capitulo no baja el tramo, igual que llenarlo con dos no lo
subia. El disparador no se lee en los dos sentidos.**

**SI NO LO EMPIEZAS, LO MIDES IGUAL:** palabras que quedan sin minar, cola declarada
con su rango, y **la fila de la TAREA 4 diciendo *sin denominador*, no *cero por
ciento***. **No estimes cuantos candidatos habria dado: estimar un capitulo sin
leerlo es adivinar.**

---

## TAREA 4. LAS CUATRO MEDIDAS DEL CIERRE, DESGLOSADAS POR CAPITULO

**Las dos primeras con una fila por capitulo, y todas recomputadas al cierre.**

| medida | como la das |
|---|---|
| **candidatos por mil palabras** | una fila por capitulo mas el total. **Denominador por CAPITULO. Y NO des la tabla por fichero**: tu propuesta 3 queda adjudicada a favor de la tabla por capitulo, que ya se declaro el denominador honesto. **Hiciste bien en no inventar un reparto que no tenias** |
| **pasos inventados sobre pasos escritos** | **una fila por capitulo.** Ver el bloque de abajo: **el denominador cambia de forma** |
| **veredictos escritos** | del lote |
| **cuanto tardo y si el tramo fue el correcto** | de la vuelta, diciendo si el segundo capitulo cupo, **y con tus dos marcas propias leidas de `git log --date=format:%H:%M:%S`.** El auditor las cruza con `loop.log`: en la vuelta 6 los dos relojes cuadraron (45,0 minutos del arnes contra 44,7 tuyos) |

### EL DENOMINADOR DE PUENTES SE DESGLOSA EN TRES, y esto es nuevo

**Tu 2.g cierra con *"97 escritos = 94 transcripcion + 3 puentes"*, y a la vez dice
que el puente 3 quedo *RETIRADO entero* y que la retirada del biografo *se fue
entera al `resumen_teorico`*. Las dos cosas no caben juntas.** El auditor conto tus
**97 pasos finales candidato a candidato y cuadran exacto con tu tabla 2.f**, pero
**un paso escrito y retirado sigue siendo un paso escrito**, y el precedente de esta
casa es el Cap. 3 (**53 escritos contra 49 finales**, ACTA 5).

**No se te pide que cambies la cifra. Se te pide que la fila sea auditable:**

    pasos escritos = pasos FINALES en los JSON
                   + pasos retirados por PUENTE
                   + pasos retirados por LA VARA (seccion 9)

**Las tres cifras, por separado, y la tasa calculada sobre la suma.** El auditor
dejo publicados los tres denominadores posibles del Cap. 4 (97, 98 y 99, con 3,09,
3,06 y 3,03) y **ninguno cambiaba ninguna decision**. **La agregada no se desglosa
despues: por eso se pide ahora.**

### LA SERIE QUE LLEVAS, para que la fila nueva se lea contra ella

    lote 1               36 pasos   13 puentes   36,11 por ciento
    lote 2, cap_02       16 pasos    1 puente     6,25
    lote 2, Cap. 2        35 pasos    1 puente     2,86
    lote 2, Cap. 3        53 pasos    4 puentes    7,55
    lote 2, Cap. 4        97 pasos    3 puentes    3,09
    lote 2 acumulado     201 pasos    9 puentes    4,48

**LA REGLA DE VOLUMEN MIRA EL PEOR CAPITULO, NO EL PROMEDIO.** El peor del lote 2 es
el Cap. 3 con 7,55, muy por debajo del 36,11 de la linea base.

---

## TAREA 5. EL INFORME DE CIERRE DEL LOTE 2, **si las dos unidades quedan leidas**

**Solo si el Cap. 6 se abre y se cierra.** Si el Cap. 5 llena el tramo, esta tarea
no se hace y se dice.

| que trae | como |
|---|---|
| **la cuenta de unidades** | 7 de 7, una a una, con sus rangos de linea y sus palabras |
| **el informe del lote entero** | `python forja.py informe --carpeta cuarentena/smart_who`, pegado con su saldo |
| **la medicion de vecinos final** | sobre la bandeja entera, con las cuatro filas de señal y **los pares de señal 3 sola separados en sus dos especies** (cabeza contra hijo, hermano contra hermano), que es tu propuesta 1 adjudicada a favor |
| **las filas de la metrica de volumen** | las seis del lote juntas, **por capitulo**, que es lo que el acta necesita para dimensionar el lote 3 |
| **las aristas sin cablear** | todas, en una sola lista |

**LO QUE NO HACES: no pides la insercion y no la haces.** `MODO_INSERCION=cuarentena`
y `D.26`: **la insercion es una autorizacion del fundador, no un default.** Un lote
cerrado y sin insertar **no bloquea nada** (`D.32`).

---

## LO QUE ESTA VUELTA TIENE QUE DEJAR MEDIDO

1. **Cuantos vecinos levanta la aduana cuando los CUATRO hermanos del metodo A estan
   en la bandeja.** Al cierre de la vuelta 6 eran **44 de 992**, con la densidad por
   par en **4,44 por ciento** (era 13,97 sobre 17 candidatos). **Con `Sell` dentro,
   la cabeza `aplicar_metodo_ghsmart_contratacion` tiene por fin sus cuatro hijos.**
   Lo mides con `src.aduana.medir` y lo das con su tabla.
2. **Si los pares de señal 3 sola siguen siendo de dos especies o aparece una
   tercera.** Llevas ocho, cuatro de cada. **Dilos con su detalle de paso**, que es
   lo que hace la medida verificable.
3. **La tasa de puentes de un capitulo de CIERRE**, que es un genero que esta casa no
   ha medido: los cinco anteriores eran de metodo o narrativos. **Y con el
   denominador desglosado en tres.**
4. **Si el lote 2 entero cabe en siete vueltas**, con su reloj delante.

---

## LO QUE EL AUDITOR TE PIDE QUE NO REPITAS

**SEIS VUELTAS SEGUIDAS FALLANDO EN LO QUE RODEA AL DATO, Y NI UNA EN EL DATO:**

| vuelta | donde cayo |
|---|---|
| 1 | la lectura |
| 2 | la aritmetica de acompañamiento |
| 3 | el recuento de acompañamiento |
| 4 | una señal medida antes de una correccion |
| 5 | un puntero de linea |
| **6** | **dos comparativos que no reproducen contra sus propias cifras** |

**El remedio esta en la TAREA 1.a y es BLOQUEANTE.** Y lo que lo vuelve accionable
es la cifra: **REPORTE que acumula esta en 2 de 3.**

**LA DIFERENCIA ENTRE PARAR EL BUCLE Y NO PARARLO ESTA EN DONDE PONES LA CIFRA.** En
tabla, cabecera o conclusion, acumula. En prosa de acompañamiento o en lista de
rutas, no. **Ponla donde puedas defenderla, y divide antes de compararla.**

---

## UNA LINEA DE DISCIPLINA QUE SALE DE UNA MEDICION DEL AUDITOR

**Medido en el ACTA 6 seccion 1.3, con su comando:** `python forja.py guiones
<ruta que no existe>` devuelve **VERDE y salida 0**. **No es caida de nadie**: tu
C.6.1 cita el barrido **sin argumentos**, que es el uso correcto.

> **Si alguna vez citas el barrido sobre una RUTA CONCRETA como prueba, imprime
> antes el tamaño del fichero.** Una ruta publicada como evidencia es cifra
> (cosecha 7.B), y un verde sobre un fichero que no existe no prueba nada.

**No escribas una guarda para esto.** Va a Alexis como observacion.

---

## LAS PARADAS

**Paras, lo declaras en TU REPORTE y te detienes si:**

- **alguna de las cuatro comprobaciones de apertura falla.** **Manda tu medida, no
  este parrafo**;
- **una lectura te pide mover la frontera de la vara** (`AUDITOR_FORJA.md` 6.3:
  ninguna vuelta la estrecha ni la ensancha sin correccion declarada de Alexis);
- **una decision necesita doctrina NUEVA**, sin regla escrita que la cubra ni por
  extension citable. **Si hay arbitro escrito, se cita el arbitro y se sigue**, que
  es lo que hiciste bien con la tactica 4;
- **el gate, el hook o la prueba de aceptacion se ponen en rojo y no sabes por que.**

**Lo que NO es parada, y lo tienes medido:** una discrepancia con una celda de este
encargo **se declara, se desglosa y mandas la tuya**; el hook tumbandote un commit
**se corrige y se reintenta**; y un artefacto del arnes con un guion largo **se
corrige en lo minimo y se declara** (1.g).

**Tu no escribes `PARA_ALEXIS.md`** (`EXTRACTOR.md` 14: propones en tu reporte y no
te adjudicas a ti mismo).

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice
una regla vigente, paras y lo traes. No adivines.**
