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
