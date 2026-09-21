# PARADA DEL FRENTE `marquet_turn_the_ship`, VUELTA 1

*Escrita por el auditor el 16 sep 2026, al cerrar su turno. Rama
`extraccion-marquet_turn_the_ship`, carpeta `../forja-marquet_turn_the_ship`.*

> **LA VUELTA EN SI SALIO BIEN.** Lo que para el bucle **no es el trabajo de la vuelta**: son
> cuatro cosas que no puedo decidir yo, y **dos de ellas ocurrieron mientras yo auditaba.**

---

## LO PRIMERO, PORQUE ES LO QUE MAS CORRE: **HAY DOS TURNOS DE AUDITOR VIVOS SOBRE ESTE ARBOL**

    [2026-09-16 21:55:07] auditor ciego: fallo instantaneo (probable limite de uso), 3664s, intento 1 de 7
    [2026-09-16 21:55:08] fallo "instantaneo"; espero 1800 segundos y reintento
    [2026-09-16 22:30:51] auditor ciego listo (USD 10.33), 2776s, intento 1 de 7
    [2026-09-16 22:30:55]   apertura ciega sellada: bfa62878d2f6a94e525aab413bf34ba1a798a934
    [2026-09-16 22:31:01] VUELTA 1 : AUDITOR (claude-opus-5)          <-- ESE SOY YO
    [2026-09-16 22:37:37] auditor ciego listo (USD 2.76), 749s, intento 2 de 7
    [2026-09-16 22:37:38] APERTURA CIEGA ROTA en la vuelta 1: REAPARECIERON REPORTE.md loop.log ...
    [2026-09-16 22:37:41]   apertura ciega sellada: 4a0f7cfec6392179961b023062f0a7eb2ec0a4e9
    [2026-09-16 22:37:45] VUELTA 1 : AUDITOR (claude-opus-5)          <-- Y ESE ES OTRO

**El arnes dio por muerto el intento 1 a las `21:55:07` y lanzo el intento 2 a las `22:25`. El
intento 1 no estaba muerto:** termino a las `22:30:51`, escribio su apertura, **se la sellaron**
(`bfa62878`) y **a las `22:31:01` me lanzaron a mi** para auditar con ella delante. Seis minutos
despues el intento 2 escribio **otra apertura encima**, se la sellaron tambien (`4a0f7cfe`) y a
las `22:37:45` **lanzaron un segundo auditor**, que a esta hora corre en paralelo conmigo.

**Y esa es la contradiccion que me para, motivo 1 de los cuatro.**

---

## LOS CUATRO MOTIVOS

### MOTIVO 1. **MI SELLO ESTA ROTO Y NO LO ROMPI YO** (contradiccion con regla vigente)

`AUDITOR_FORJA.md` 1: *no toques `APERTURA_CIEGA.md` despues, porque **el sello se verifica al
terminar tu turno y un sello roto detiene la corrida***.

| | |
|---|---|
| el sello con el que se me lanzo | `bfa62878d2f6a94e525aab413bf34ba1a798a934` |
| lo que el fichero vale ahora | `4a0f7cfec6392179961b023062f0a7eb2ec0a4e9` |
| quien lo cambio | **el intento 2 del arnes, a las 22:37:41**; yo no lo abri para escribir |
| donde esta el mio | commiteado en `e084bcc`, intacto y recuperable |
| donde esta el otro | commiteado en `3b33091`, encima del mio |

**No es una caida de nadie de los que trabajan: es el arnes.** Y `D.45` me prohibe tocarlo.

### MOTIVO 2. **LA RESTAURACION DEL ARNES BORRO DEL ARBOL LAS 171 LINEAS PUBLICADAS DE ESTA VUELTA** (dato)

A las `22:37` el arnes devolvio al arbol los cuatro ficheros de `D.34.2` **desde una copia de las
`20:47`, anterior al turno del extractor**. Resultado medido con `git diff` contra `HEAD`:

    docs/loop/REPORTE.md | 171 ---------------------------------------------------
    1 file changed, 171 deletions(-)      (171 borradas, 0 anadidas)

Era **la TAREA 1 entera de la vuelta**: la frontera de `cap_03`. **Lo recupere** con
`git checkout -- docs/loop/REPORTE.md`, porque estaba commiteada en `669524a` y el borrado era
solo del arbol. **Cero contenido perdido, y lo digo con su cifra: el diff no tenia ni una linea
anadida.**

**Lo que NO se recupera:** `docs/loop/ultimo_extractor.json` quedo en **0 bytes**, y **nunca
estuvo en ningun commit de este frente** (lo comprobe en los cinco: `dbff694`, `669524a`,
`4138f53`, `e084bcc`, `3b33091`). El mensaje final del extractor lo lei del fichero a las `22:34`,
antes del borrado, y de el salen dos frases que estan en mi acta: que dejo **en vuelo** el
informe de un candidato y el del lote entero, y que **el auditor ciego corria a la vez sobre el
mismo arbol**.

### MOTIVO 3. **QUE REGISTRO Y QUE RACHA HEREDA UN FRENTE** (doctrina, y ya es tuya)

**Tu propio `DICTAMEN` de las `22:28` de hoy** (commit `17d673f` de `extraccion-mundo-11`) la
plantea y dice que no la resuelves por tu cuenta porque es doctrina. **A mi me llega en forma de
cifra obligatoria:** `AUDITOR_FORJA.md` 5.3 me manda publicar *la racha viva de cada especie con
su cuenta*, y esta vuelta **tiene una caida de especie `REPORTE` que acumula** (el reporte se
quedo en la TAREA 1, seccion 5.1 de mi acta).

| si la racha de la linea de insercion **NO** se hereda | si **SI** se hereda |
|---|---|
| este frente abre en `1 de 3`. **No hay parada por credito** | esta tanda cierra en `3 de 3`. **Parada por credito** |

**La abri en `1 de 3` y dije por que** (`5.2`: *una racha mezclada no dice de quien es el
problema*; las tres tandas heredadas son de `cap_11` de `scott_radical_candor`). **Pero no me
adjudico la lectura que me conviene**, y `5.4` dice que un auditor que pone una racha a cero se
esta absolviendo. **Decidelo tu y yo lo aplico.**

### MOTIVO 4. **UNA FASE CIEGA CITADA POR DENTRO DEL MATERIAL QUE VIENE A LEER A CIEGAS** (doctrina nueva)

El candidato `cambiar_forma_trabajar_conservar_plantilla` **lleva escrito dentro que el hallazgo
de su paso 4 lo cazo la apertura ciega del auditor, con su seccion y su punto**. Los tiempos:

| | |
|---|---|
| el candidato se toco | `21:33:20` |
| los papeles del auditor `.marquet_v1/` se escribieron | `21:15` a `21:36` |
| el turno del extractor corrio | `20:55` a `21:44` |
| **mi fase ciega no se abrio hasta** | **`21:44:27`** |

**Un proceso de auditor estuvo escribiendo en el arbol del extractor durante su turno, y el
extractor leyo su apertura ciega.** No le cargo nada al extractor: **declaro el credito en vez de
quedarselo**, que es lo unico que podia hacer bien. **Ninguna regla escrita cubre esto**, y
`D.45` me prohibe tocar el arnes ni los protocolos.

---

## EL ESTADO EXACTO

| | |
|---|---|
| rama | `extraccion-marquet_turn_the_ship` |
| `HEAD` cuando escribo | `3b33091` (mas mi commit de `docs/loop/` encima) |
| fase | **vuelta 1 del frente cerrada por el auditor, con parada** |
| `dataset/nodos.jsonl` | **270 nodos**, los mismos que al abrir |
| `bitacora/VEREDICTOS.jsonl` | **396 lineas**, **ninguna de este frente** |
| bandeja `cuarentena/marquet_turn_the_ship/` | **9 candidatos** (3 heredados y 6 nuevos) |
| inserciones | **CERO.** `MODO_INSERCION=cuarentena` sin tocar |
| `gate` | **VERDE**, 270 nodos |
| `guiones` | **VERDE** |
| `tests/test_aceptacion.py` | **201 pruebas, 0 fallos, 0 errores** |
| `PASOS INVENTADOS POR CAPITULO` | **0,00** en `cap_01`, `cap_02` y `cap_03`. Tope 10. **Freno no activado** |

**LO QUE LA VUELTA ENTREGO Y YO VERIFIQUE:** la frontera de `cap_03` cierra al digito (`1978`
contra `1978`, **las 16 celdas talladas una a una contra el fichero**), los **6 candidatos** con
su aduana en seco por candidato y **0 CAERIA**, **8 puentes escritos y retirados en el acto** que
comprobe uno a uno en la bandeja, **2 fronteras incompletas** declaradas y corregidas sin borrar,
y los **3 discutibles marcados se sostienen los tres**.

**LO QUE FALTA:** el reporte de la vuelta. Se quedo en la TAREA 1 con las otras dos declaradas
`ABIERTA` en su propia tabla, y **`PASOS INVENTADOS` no aparece en el**. El turno acabo esperando
dos corridas de aduana que no llegaron: el informe de `cambiar_forma_trabajar_conservar_plantilla`
y el del lote entero. **El material para escribirlo esta entero en `.vm01/`, sin perderse.**

---

## LO QUE NECESITO DE TI

1. **El arnes: un turno por arbol.** Que un intento dado por muerto que sigue vivo no pueda
   sellar, y que un segundo intento no pueda sellar encima de un sello ya emitido ni lanzar un
   segundo auditor. **Hoy hay dos corriendo.**
2. **El arnes, segunda mitad: que la restauracion de `D.34.2` no devuelva una copia mas vieja que
   el ultimo commit.** Lo de hoy costo 171 lineas del arbol y un `ultimo_extractor.json` que
   nunca llego a ningun commit.
3. **La decision del motivo 3:** si un frente hereda el registro y la racha de la linea de
   insercion. Tu recomendacion escrita en el `DICTAMEN` (*que cada linea escriba en su propio
   fichero*) resolveria esto y la colision de numero de acta a la vez.
4. **La decision del motivo 4:** que hacer cuando la fase ciega y el turno del extractor se
   solapan en un arbol.
5. **Una respuesta pequenia que no es doctrina, pero que te toca:** mi caida propia de la seccion
   `5.3` del acta **no tiene casillero** en las dos especies que `5.2` me da. No me la cargue y
   dije por que. **Si la lees como `CIFRA PUBLICADA PROPIA`, mi racha de este frente va a `1 de
   3`** y no cambia nada mas.

## COMO RETOMAR

1. Arregla el arnes (puntos 1 y 2). **Sin eso, relanzar produce el mismo cruce.**
2. Escribe tu decision de los puntos 3 y 4 en `docs/loop/paradas/`, con su fecha.
3. **Borra este fichero** y escribe el encargo de la vuelta 2 en `docs/loop/PROMPT_SIGUIENTE.md`.
   La vuelta 2 **abre con una tarea bloqueante**: *escribir en el reporte las TAREAS 2 y 3 de la
   vuelta 1 desde los papeles de `.vm01/`, que estan intactos*, y cerrar las dos corridas de
   aduana que quedaron en vuelo. **Despues, `cap_04`.**
4. **El bucle no funde ramas.** La insercion de estos 9 candidatos se pide aparte y **no bloquea**
   la extraccion de este frente.

> **NADA DE ESTO PIDE DESHACER TRABAJO.** Los 9 candidatos estan bien y verificados, el grafo no
> se movio, y las guardas estan en verde. **Lo que esta roto es la tuberia, no el dato.**

---

# ANEXO DEL SEGUNDO AUDITOR DE LA MISMA VUELTA. **NO BORRA NADA DE LO DE ARRIBA**

*Escrito el 16 sep 2026 por el otro turno de auditor de la vuelta 1 de este frente, el que el arnes
lanzo a las `22:37:45` con el sello `4a0f7cfe`. **Mi acta es la `ACTA M1`**, anexada detras de la que
firma la pagina de arriba. `PARALELO.md` 5.2: en los registros **se conservan los dos**.*

> **LOS CUATRO MOTIVOS DE ARRIBA SE SOSTIENEN Y NO LOS REPITO.** Los verifique con mis propios
> comandos y coinciden con lo que yo medi por separado. **Este anexo anade UN motivo mas y CIERRA
> una de las preguntas abiertas de arriba.**

## MOTIVO 5, QUE ARRIBA QUEDO SIN DECIDIR: **`REPORTE` LLEGA A `3 de 3`. CREDITO ROTO**

**El `MOTIVO 3` de arriba deja la racha en manos del fundador y dice la verdad al decir que no se la
adjudica.** Yo si la adjudico, **y no por valiente: porque la alternativa exige un reinicio, y
`AUDITOR_FORJA.md` 5.4 dice que los reinicios no son del auditor.**

    5.4: La racha NO se reinicia sola. La reinicia una decision de Alexis escrita en
         docs/loop/paradas/, y el acta lo dice citandola. Un auditor que pone su propia
         racha a cero se esta absolviendo.

**Abrir este frente en `1 de 3` es poner a cero con otro nombre.** Asi que aplico la racha heredada:

| tanda | acta | caida de `REPORTE` | racha |
|---|---|---|---:|
| vuelta 31 | `ACTA 30` | la fila `10` de la tabla de la cabeza de `cap_11` pone un nodo que no es | `2 de 3` |
| vuelta 32 | `ACTA 31` (otra rama) | `167` pasos publicados de `cap_11` donde el grafo tiene `187` | `3 de 3` |
| **vuelta 1 de este frente** | **`ACTA M1`** | **ver abajo** | **`3 de 3`. TOPE** |

### La caida de esta vuelta, con su medida y no con su adjetivo

**Lo que el reporte publica**, en la celda `3` de su tabla de discutibles y otra vez en la prosa de
su `1.a`:

    | 3 | la vuelta mina UNA unidad cuando el tramo vigente del lote eran DOS, y el motivo es el coste de la aduana, no la cosecha | 1.a y 1.c |

**Lo que dicen las sedes, leidas por mi en esta vuelta:**

    $ grep -n "EL TRAMO DEL LOTE 5" docs/loop/ACTA_AUDITOR.md
    24062:> **EL TRAMO DEL LOTE 5 SE QUEDA EN TRES CAPITULOS**, y el techo de candidatos de `EXTRACTOR.md`
    $ grep -n "el tramo del lote 5" docs/loop/ACTA_AUDITOR.md
    24403:| **el tramo del lote 5** | **se queda en TRES**, razonado en `4.4`

Y `docs/loop/ORDEN_DE_LOTES.md` **no tiene fila de lote 5**: su ultima es `lote 4   TRES capitulos por
vuelta`. **Ninguna acta posterior lo movio.** El `DOS` no sale de ninguna sede: sale de lo que hizo la
vuelta 25, que mino dos unidades, **y el propio parrafo lo delata al escribir *las DOS minadas en la
vuelta 25* dos lineas antes.**

**LO QUE NO CAE, para que esto no se lea mas grande de lo que es:** la decision de minar UNA unidad
**es correcta** (`EXTRACTOR.md` 17, *un capitulo por vuelta*, y el encargo de este frente en singular),
los `6` candidatos estan dentro del techo de `5` a `15`, y el cierre corto va declarado con su cifra.
**Lo que cae es el numero, no el acto.** Y cae **dentro del marcado**: el extractor marco esa duda
antes de saber si acertaba.

## LO QUE ESTE ANEXO CAMBIA Y LO QUE NO

| | |
|---|---|
| **la parada** | **no cambia.** Arriba para por cuatro motivos; abajo por cinco. **Y si el fundador decide que cada frente lleva su propia racha, sigue parando por los cuatro de arriba** |
| **lo que se te pide** | **una cosa mas, y es la que desbloquea:** el `MOTIVO 3` de arriba pide decidir **si un frente hereda la racha**. **Si decides que SI, esta parada ya tiene su motivo escrito y lo unico que falta es tu reinicio en `docs/loop/paradas/`.** Si decides que NO, este motivo 5 cae y los otros cuatro siguen en pie |

## LO QUE YO VERIFIQUE POR SEPARADO, Y SALE IGUAL

*Corrido por mi, no copiado de la pagina de arriba.*

    $ python forja.py gate                      GATE VERDE. nodos verificados: 270
    $ python forja.py guiones                   BARRIDO DE GUIONES VERDE
    $ python tests/test_aceptacion.py           total: 201 pruebas, 0 fallos, 0 errores
    $ python scripts/tallar_reporte.py --estricto   TALLADO VERDE: 70 tablas
    $ python scripts/censar_rutas.py                CENSO VERDE: 531 rutas
    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl    270    396
    $ lineas de bitacora que nombran un id de este frente    0
    $ nodos del grafo con fuente marquet_turn_the_ship       0

**Las dieciseis filas de la frontera de `cap_03`, comprobadas una a una contra el fichero: `0` filas
que no coinciden, suma `1978`, cuerpo `1978`, cero solapes, cero lineas con contenido sin cubrir.**
**`PASOS INVENTADOS`: `0,00` en `cap_01` (7 pasos), `cap_02` (10) y `cap_03` (53), firmado tras releer
los `70` a ciegas y `10` mas al azar con semilla `916` en mi turno normal.** **Los tres discutibles se
sostienen los tres**, y el `2` lo adjudico citando la restriccion 1 de `D.27` y su ejemplar del banco.

## Y UN HALLAZGO QUE NO ES PARADA NI CAIDA, PERO QUE TE TOCA SABER ANTES DE INSERTAR

**RETIRAR UN PUENTE DE ONCE PASOS BORRO TRES PARES DE LA COLA DE LECTURA.** El extractor corrigio el
paso `2` de `auditar_formacion_premios_ultima_fila` a las `21:24`, tres minutos despues de que la
aduana midiera `contar_firmas` contra el. Medido por mi:

    ANTES de la correccion, auditar_formacion levantaba CINCO vecinos:
      observar 0.391 | recorrer 0.388 | contar_firmas 0.359 | seguir_frustrado 0.356 | encargar_meta 0.355
    DESPUES, levanta DOS:
      observar 0.370 | recorrer 0.353
    Y hoy, medido con src.aduana.medir sobre el par:
      contar_firmas -> auditar_formacion : similitud_texto 0.31, levantada_por []

**No es de poblacion:** la señal de texto es `difflib.SequenceMatcher` (`src/aduana.py:266`), que no
mira el corpus. **Es la consecuencia de dos reglas buenas juntas** (*un candidato por vez, en el acto
de escribirlo* y *el puente se retira en el mismo acto*), **y nadie la habia escrito.** Lo que deja:
**los informes de aduana de `c1` a `c5` que hay en `.vm01/` nombran una vecindad que ya no existe**, y
**el unico barrido que describe la bandeja tal como esta hoy es el que se corre al final.**

> **NADA DE ESTE ANEXO PIDE DESHACER TRABAJO, igual que la pagina de arriba.** Los `9` candidatos
> estan bien y verificados por dos auditores por separado, el grafo no se movio, y las cinco guardas
> estan en verde. **El bucle no funde ramas y el bucle no crea remotos.**

---

# SEGUNDO ANEXO. **EL TERCER AUDITOR DE LA MISMA VUELTA. NO BORRA NADA DE LO DE ARRIBA**

*Escrito el 16 sep 2026 por el TERCER turno de auditor de la vuelta 1 de este frente. **Mi acta es la
`ACTA M2`**, anexada detras de la `ACTA M1`. `PARALELO.md` 5.2: en los registros **se conservan los
tres**. **Mi turno no tuvo fase ciega**: el arnes me invoco con el reporte ya expuesto, y por eso
ninguna de mis lecturas se publica como ciega.*

> **LOS CINCO MOTIVOS DE ARRIBA SE SOSTIENEN Y NO LOS REPITO.** Los recomprobe con mis propios
> comandos. **Este anexo anade UNO mas, y es el unico hallazgo de esta vuelta que CAMBIA UNA
> DECISION.**

## MOTIVO 6. **`PASOS INVENTADOS` DE `cap_03` NO ES `0,00`. ES `15,09`, Y EL FRENO DE VOLUMEN SE ACTIVA**

**Las dos actas de arriba publicaron `0,00` en las tres filas y *el freno NO SE ACTIVA*. Las dos se
equivocaron en el mismo sitio, y por eso hizo falta un tercero.**

**LAS DOS DECLARARON LOS OCHO PUENTES**, con su fichero, su especie y su cuenta, en seccion propia.
**Nadie escondio nada.** Lo que fallo fue **donde pusieron el ocho**: en la prosa, y no en el
numerador. Y para justificarlo citaron `8.4` (*un puente corregido no es una caida*), que es cierto
**y contesta a otra pregunta**: dice si hay culpa, no si el puente cuenta.

**QUIEN SI CONTESTA A ESA PREGUNTA ES LA PROPIA CASA, Y HACE DOCE VUELTAS:**

    ACTA 4, seccion 3.6 (docs/loop/ACTA_AUDITOR.md L2841):
    > ADJUDICO: SE CUENTAN PASOS ESCRITOS, Y LA CORRECCION NO BORRA EL PUENTE. El
    > denominador es "pasos que el extractor escribio"; el numerador, "de esos, cuantos
    > el libro no decia". Cuando se corrigio es irrelevante para la cifra y decisivo
    > para el dato, que es justo por lo que D.30 manda corregir en el acto.

    ACTA 5, seccion 7.2 (L4427):
    > El denominador son pasos ESCRITOS y el puente corregido se cuenta ... y lo aplico
    > igual en las dos formas de correccion, la que retira y la que reescribe.

    y su tabla de aquella vuelta, que es el ejemplar exacto del caso de hoy (L4404):
    | Cap. 2 | pasos escritos 35 | transcripcion 34 | PUENTE 1 | 2,86 |
    (aquel puente se habia REESCRITO, y conto igual, con el denominador sin tocar)

**Y LA LINEA BASE LO EXIGE:** el `36,11` del lote 1 son **13 puentes de 36 pasos ESCRITOS**, y **los
13 se corrigieron tambien** (`CALIBRACION_D4.md` 9.1: *el lote quedo en 32 pasos*). Si un lote cuenta
escritos y el siguiente cuenta supervivientes, **la serie entera es falsa**.

### La cifra corregida, firmada por mi, con el numerador leido uno a uno contra el libro

| unidad | nodos | pasos escritos | transcripcion | **PUENTE** | **PASOS INVENTADOS** |
|---|---:|---:|---:|---:|---:|
| `cap_01` | 1 | **7** | 7 | **0** | **0,00 por ciento** |
| `cap_02` | 2 | **10** | 10 | **0** | **0,00 por ciento** |
| `cap_03` | 6 | **53** | 45 | **8** | **15,09 por ciento** |
| **el lote 5, lo minado hasta hoy** | **9** | **70** | 62 | **8** | **11,43 por ciento** |

**LA FILA QUE DECIDE ES LA PEOR** (`AUDITOR_FORJA.md` 8.2): `cap_03` con **`15,09`** contra un tope de
**`10,00`**. **El freno SE ACTIVA y el tramo baja un escalon.**

**LOS OCHO PUENTES LOS FIRMO YO**: abri los cuatro mas dudosos con `sed` contra su linea del libro y
comprobe que el texto original decia lo que el libro no dice. **Y relei una muestra propia de los
marcados transcripcion**, `10` de `70` con semilla `20260916`: **`10` de `10` TRANSCRIPCION**.

### Lo que cambia y lo que no

| | |
|---|---|
| **ningun trabajo se deshace** | esta vuelta mino **UNA** unidad, por debajo de `DOS` y de `TRES`. **Los nueve candidatos no se tocan.** El grafo no se movio |
| **no es caida del extractor** | `8.4` es explicita: **un puente cazado y corregido por quien lo escribio es `D.30` funcionando** |
| **si es caida nuestra** | `0,00` es **una cifra falsa en sede duradera**, y vive en las dos actas y en la apertura sellada. **`CIFRA PUBLICADA PROPIA`**, y por ella **la racha del auditor de esta tanda pasa de `0 de 3` a `1 de 3`** |
| **lo que costaba** | `8.3`: *una cifra de volumen mal firmada no cuesta una discusion: cuesta un lote entero corriendo al tamanio equivocado*. **Con `0,00` el lote subia un escalon; con `15,09` baja uno.** El doble de material por vuelta entre las dos lecturas |

## Y UNA CORRECCION QUE SI PUDE HACER YO, PORQUE VIVE EN MI SEDE

**El `MOTIVO 3` de arriba y el `MOTIVO 5` giran sobre la celda del reporte que dice *el tramo vigente
del lote eran `DOS`*. La `ACTA M1` la cargo diciendo que ese `DOS` no salia de ninguna sede. Salia de
dos**, y las dos son sede del auditor (`5.6`):

    22356 y 22597  ACTA 24 : "el lote 5 corre a DOS capitulos por vuelta"
    23532          ACTA 25 : "Tramo: DOS capitulos"
    24062          ACTA 26 : "EL TRAMO DEL LOTE 5 SE QUEDA EN TRES CAPITULOS"

**LA CAIDA DEL EXTRACTOR SE SOSTIENE IGUAL**, por `D.13` (entre dos reglas fechadas que chocan gana la
mas reciente): el tramo vigente era `TRES`. **Lo que cambia es de que fue la caida:** no se invento un
numero, **copio el de dos actas que nadie habia marcado como corregidas**, y fallo al llamarlo
*vigente*.

**Y LA MITAD QUE ES NUESTRA:** la `ACTA 26` movio el tramo de `DOS` a `TRES` escribiendo *se queda*,
como si `TRES` ya fuese lo vigente, **y `6.2` manda que la perdedora se corrija por correccion
declarada, sin borrar. Esa correccion no se escribio nunca.** La he escrito yo en la `ACTA M2`
seccion `3.2`, que es mi sede y no toca el banco ni `src/` ni el arnes. **No he movido ninguna racha
de tandas ya cerradas: la casa no aplica retroactividad.**

## UNA COLUMNA QUE FALTABA EN LAS DOS PAGINAS DE ARRIBA, Y QUE TE TOCA ANTES DE INSERTAR

**`0 CAERIA` es cierto. Lo que ninguna de las dos publico es que NINGUNO ENTRARIA SOLO.** Leido por mi
de los informes del propio extractor (`PATRON: .vm01/aduana/c*.txt`), los siete candidatos con
informe en esta corrida:

    ENTRARIAN 0    BLOQUEARIAN 7    CAERIAN 0

**Los siete esperan veredicto**, que es cola de lectura y no rechazo. **Hoy no bloquea nada porque
este frente no inserta.** Bloquea el dia que se pida la insercion de los nueve.

**Y LAS DOS CORRIDAS EN VUELO SIGUEN EN CERO BYTES**, medido por mi: el informe del lote entero y el
de `cambiar_forma_trabajar_conservar_plantilla`. **Ninguna de las dos actas las publico como ruta de
prueba**, asi que no hay caida de `7.B`; lo digo porque lo comprobe.

## LO QUE VERIFIQUE POR SEPARADO, Y SALE IGUAL QUE ARRIBA

    $ python forja.py gate                    GATE VERDE. nodos verificados: 270
    $ python forja.py guiones                 BARRIDO DE GUIONES VERDE
    $ python tests/test_aceptacion.py         total: 201 pruebas, 0 fallos, 0 errores
    $ python forja.py resolutor               nodos vivos 270, deprecados 0, alias 0
    $ wc -l dataset/nodos.jsonl bitacora/VEREDICTOS.jsonl config/pares_mutuos.jsonl   270  396  1
    $ ls cuarentena/marquet_turn_the_ship/*.json | wc -l                              9
    $ grep -c marquet_turn_the_ship dataset/nodos.jsonl                               0
    lineas de bitacora que nombran uno de los nueve ids, buscadas una a una           0

**La frontera de `cap_03` contada por tercera vez con contador propio: `16` filas, `0` que no
coinciden, suma `1978`, cuerpo `1978`, `0` solapes, `0` lineas con contenido sin cubrir.** **Las
cuatro celdas de apertura cuadran** (`270`, `3`, `17`, `dbff694`). **Los tres discutibles se sostienen
los tres.**

**Y UNA COLA `D.15` QUE NINGUNA DE LAS DOS ACTAS REGISTRO:** `python forja.py rancios` da **6 filas**
(`2` sin huella y `4` rancias), **las seis de `scott_radical_candor` y ninguna de este frente**. **No
pone nada en rojo** y el gate lo confirma; va escrito porque una cola sin registrar se pierde.

## LO QUE ESTE ANEXO ANIADE A LO QUE SE TE PIDE

1. **Lo de arriba, intacto:** el arnes (un turno por arbol, y que la restauracion de `D.34.2` no
   devuelva copias mas viejas que el ultimo commit), y tus decisiones de los motivos 3 y 4.
2. **Nuevo, y es el unico que cambia trabajo:** **el tramo del lote 5 baja a `DOS` capitulos por
   vuelta.** Es mecanico y esta escrito (`8.1`), pero **lo firma un auditor cuya racha acaba de subir
   por este mismo asunto**, asi que **lo dejo medido delante de ti y no lo escondo en una celda.**
3. **Nuevo, pequenio, y tuyo:** las dos actas de arriba se declararon **limpias de la especie del
   auditor**. **No lo estaban.** La racha del auditor de esta tanda queda en **`1 de 3`**. No para
   nada por si sola; cambia el punto de partida de la siguiente.

## COMO RETOMAR, CON LO QUE ESTE ANEXO AGREGA A LA LISTA DE ARRIBA

La vuelta 2 abre con la tarea bloqueante que ya dice la pagina de arriba, **mas estas cuatro**:

1. **Correr el lote a `DOS` capitulos por vuelta**, no a tres.
2. **Escribir `TAREA 2` y `TAREA 3` del reporte desde los papeles de `.vm01/`, publicando `cap_03` en
   `15,09` y NO en `0,00`.** Si se copia `.vm01/fidelidad_lote.txt` tal cual **vuelve a salir
   `0,00`**: ese fichero describe la bandeja **despues** de las correcciones y los ocho puentes no
   estan dentro.
3. **Cerrar las dos corridas de aduana en cero bytes** antes de que nadie pida insertar estos nueve.
4. **Reescribir o retirar el paso `1` de `ceder_control_reforzar_competencia_claridad`** antes de que
   ese nodo entre al grafo.

> **NADA DE ESTE ANEXO PIDE DESHACER TRABAJO, igual que las dos paginas de arriba.** Los nueve
> candidatos estan bien y verificados ahora por tres auditores por separado, el grafo no se movio, y
> las guardas estan en verde. **Lo unico que se corrige es una cifra nuestra, y lo que esa cifra
> decide es el tamanio de la vuelta que viene.**
