# CIERRE DEL LOTE 1: `onu_consumidor`

**10 sep 2026.** El primer lote de la forja esta cerrado y **sus seis nodos estan
en el grafo**. Era un lote de calibracion (`D.24`): se hizo para medir el
instrumento con trabajo de verdad delante, barato. **Esto es lo que midio.**

---

## 1. LO QUE ENTRO, Y EN QUE ORDEN

**Autorizacion del fundador del 10 sep 2026.** Seis inserciones, en el orden
medido, con `MODO_INSERCION` autorizado a mano por primera vez.

| # | id | pasos | resultado |
|---|---|---:|---|
| 1 | `formular_codigo_comercializacion_empresarial` | 5 | **MADRE**, entra primero |
| 2 | `verificar_afirmaciones_ambientales_publicidad` | 5 | **HIJO**, con la arista declarada |
| 3 | `detectar_abusos_contractuales_consumo` | 5 | sin vecinos |
| 4 | `examinar_normas_pesos_medidas` | 5 | sin vecinos |
| 5 | `informar_efectos_ambientales_productos` | 7 | sin vecinos |
| 6 | `vigilar_practicas_comerciales_perjudiciales` | 5 | sin vecinos |

**LA MADRE PRIMERO NO ERA UNA PREFERENCIA:** si entra antes el hijo, en el momento
de su veredicto **no hay madre en el grafo** contra la que declarar la arista, y
habria que cablearla despues a mano en una sede que solo escribe la aduana.

**El censo nuevo del dataset:**

| | antes | **despues** |
|---|---:|---:|
| nodos vivos | 2 | **8** |
| deprecados | 0 | **0** |
| alias registrados | 0 | **0** |
| aristas declaradas | 1 | **2** |
| veredictos en bitacora | 1 | **2** |
| fuentes canonicas en uso | 1 | **2** |

Gate **VERDE** sobre 8 nodos y 12 guardas. Resolutor **VERDE**. Bloque de vigencia
**VERDE**, 2 veredictos comprobados. Suite **61 de 61**. Barrido **VERDE**.

---

## 2. LAS DOS ARISTAS DE LA CASA, UNA AL LADO DE OTRA

**Es la tabla mas util que deja este lote**, porque cuenta entera la doctrina de
`D.19` con datos propios:

| arista | señal que la levanto | `paso_contra_nodo` | umbral |
|---|---|---:|---:|
| `registrar_fuente_canonica > elegir_grafia_clave` (4 sep) | `paso_contra_nodo` | **0,658** | 0,60 |
| `formular_codigo... > verificar_afirmaciones...` (10 sep) | **`lectura declarada`** | **0,572** | 0,60 |

**La primera la vio el instrumento. La segunda la vio un lector, y el instrumento
no la habria visto nunca.** Ochenta y seis milesimas separan las dos.

**LA RAZON ESCRITA DE LA SEGUNDA, tal como quedo en `bitacora/VEREDICTOS.jsonl`:**

> El hijo despliega el paso 2 de la madre (escribe el codigo de comercializacion)
> para UNA materia concreta, las afirmaciones ambientales, y añade lo que la madre
> no tiene en ningun paso: recoger las afirmaciones hechas, verificar cada una
> contra la prueba que el codigo exige, y adoptar la medida sobre la que quede
> probada como capciosa. La madre escribe y publica la regla; el hijo la aplica
> contra un caso y actua.

**EL UMBRAL NO SE TOCO.** Que la señal mida 0,572 con el umbral en 0,60 **es la
razon por la que la lectura no delega en la señal**, no un argumento para bajarlo.
Bajarlo a 0,55 abriria 14,3 vecinos falsos por candidato (`D.18`,
`CALIBRACION_D4.md`).

### Y un defecto del instrumento que esta autorizacion descubrio

**La arista no se podia declarar.** El bucle que escribe aristas y bitacora
iteraba solo sobre los vecinos que las señales levantaron, asi que **un veredicto
sobre un no vecino se parseaba y se tiraba**: la insercion decia GATE VERDE, el
nodo entraba, y ni la arista ni la razon escrita se escribian en ninguna parte.

**Un veredicto aceptado en silencio es peor que uno rechazado, porque el rechazo
se ve.** Y no era un caso raro: la señal 3 levanta el **3 por ciento** de las
aristas declaradas, asi que **el 97 por ciento de las aristas que esta forja
llegue a declarar pasaba por ese agujero.**

Arreglado en `2ca9442`, con cuatro pruebas y su caso positivo.

---

## 3. LAS CIFRAS DE CALIBRACION, Y QUE SE PUEDE HACER CON ELLAS

### 3.1. El libro, contando sus cuatro ficheros

| fichero | palabras | estado | candidatos |
|---|---:|---|---:|
| `cap_00.md` | 171 | portada, **no minable** | 0 |
| `cap_01.md` | 376 | **no minado** por la marca `FRONTERA` | 0 |
| `cap_02.md` | 819 | minado y corregido | **6** |
| `cap_03.md` | 389 | minado, **resultado cero**: 0 procedimientos, 5 posturas | 0 |
| **total** | **1755** | | **6** |

### 3.2. Las cuatro medidas que el fundador pidio

| medida | cifra del lote 1 |
|---|---|
| **candidatos por mil palabras** | **4,97** sobre las 1.208 palabras minadas. **3,42** sobre el libro entero |
| **pasos inventados por lote** | **13 de 36, el 36 por ciento.** Cuatro de los seis candidatos llevaban al menos uno. El lote quedo en 32 pasos |
| **veredictos escritos** | **1** en seis inserciones. **Y el unico que hubo fue invisible para las tres señales**: 1 de 1 |
| **coste** | **29,20 USD** y **86,5 minutos** de reloj, en dos vueltas de dos asientos |

**El desglose del coste, leido de los testigos del arnes:**

    vuelta 1   extractor  7,01 USD  1178 s      vuelta 2   extractor  7,41 USD  1305 s
               auditor    6,63 USD  1317 s                 auditor    8,15 USD  1393 s

### 3.3. LO QUE QUEDA, y por que la proyeccion no es una

**Los nueve libros restantes, medidos hoy uno a uno:**

| libro | capitulos | palabras |
|---|---:|---:|
| `smart_who` **(lote 2)** | 7 | 44.324 |
| `zhuo_manager` | 12 | 70.452 |
| `scott_radical_candor` | 15 | 108.587 |
| `marquet_turn_the_ship` | 17 | 34.217 |
| `openstax_business_ethics` | 17 | 55.179 |
| `grove_high_output` | 18 | 64.862 |
| `bernerslee_bananas` | 19 | 22.365 |
| `gerber_emyth` | 22 | 63.434 |
| `openstax_org_behavior` | 32 | 95.348 |
| `mundo_10_reservado` | 1 | 3.880 |
| **total** | **160** | **562.648** |

> **EL LOTE 1 ES EL 0,3 POR CIENTO DE LO QUE QUEDA.** Sus tasas se publican, y se
> publican con este aviso delante.

**LAS DOS PROYECCIONES DEL COSTE NO COINCIDEN, Y SU DESACUERDO ES EL HALLAZGO:**

| base | cuenta | proyeccion sobre lo que queda |
|---|---|---:|
| por capitulo tocado | 9,73 USD x 160 capitulos | **~1.560 USD** |
| por mil palabras | 16,64 USD x 562,6 mil | **~9.360 USD** |

**SEIS VECES DE DIFERENCIA, y la causa esta medida:** los capitulos del lote 1
promedian **439 palabras**; los que quedan promedian **3.517**. **Ocho veces mas
grandes.** Un capitulo de Grove no es un apartado de la ONU, y una vuelta no le va
a caber.

**LA CIFRA POR PALABRA ES LA MENOS MALA, y aun asi esta inflada**, porque las dos
vueltas del lote 1 gastaron mucho en doctrina que no se repite: adjudicar la
prueba del inventario, resolver una contradiccion de sedes, reparar trece puentes.

**Y LA TASA DE CANDIDATOS NO SE PROYECTA EN ABSOLUTO.** A 4,97 por mil palabras
saldrian **2.796 candidatos**, y esa cifra no es creible: el texto normativo es
denso y terso, y un libro de gestion gasta muchas mas palabras por procedimiento.
**El lote 2 (`smart_who`, 44.324 palabras, 25 veces el lote 1) es lo que va a
dejar esa tasa medida de verdad.**

### 3.4. La tasa que SI se transfiere

**El 36 por ciento de pasos inventados no es una propiedad del libro: es una
propiedad de la mano que escribe.** Por eso se transfiere, y por eso `D.30` la
convierte en regla. La otra que se transfiere es el reparto:

| parrafo | inventario | puentes |
|---|---|---:|
| 29, cinco medios nombrados | rico | **0 por ciento** |
| 32, una frase | pobre | **83 por ciento** |

> **UN PARRAFO POBRE NO PRODUCE UN NODO POBRE: PRODUCE UN NODO INVENTADO.**

---

## 4. EL HUECO QUE SIGUE ABIERTO, y ahora por fin se puede medir

**EL ERROR DE DEJAR PASAR SIGUE SIN MEDIR.** Las dos vueltas del bucle corrieron
con cero inserciones, asi que no hubo veredictos, sin veredictos no hubo `SANO`, y
sin `SANO` no hubo muestra pineada: **dos tandas con poblacion cero**
(`AUDITOR_FORJA.md` seccion 7).

**Hoy eso cambia.** Con seis nodos dentro y un veredicto escrito, **la vuelta
siguiente es la primera que puede medirlo**. Y sigue habiendo poblacion menor que
la muestra minima, asi que se cumple releyendo todos y diciendolo con su cifra,
que es lo que la seccion 7 manda.

**Una nota de dato que este lote deja sin recoger, y se dice para que no se
pierda:** el parrafo 22 de `cap_02` remite a la resolucion 35/63 de 5 diciembre
1980, y esa vigencia **no quedo en `censos/vigencia.md`** porque ningun candidato
la llevo como campo. No es una caida: es material que el proximo paso por este
libro puede recoger.

---

## 5. LO QUE ESTE LOTE DEJA ESCRITO EN EL BANCO

| regla | que dice |
|---|---|
| **`D.27`** | la prueba del inventario, con sus tres restricciones |
| **`D.28`** | `PARA_ALEXIS.md` es del auditor, y un encargo no mueve una sede |
| **`D.29`** | la arista que la señal no levanta se declara por lectura, en el acto de la insercion |
| **`D.30`** | **la aduana caza la forma; la fidelidad la caza otro lector** |

**Cuatro reglas y seis nodos.** Para un lote de calibracion, las cuatro reglas
valen mas que los seis nodos.
