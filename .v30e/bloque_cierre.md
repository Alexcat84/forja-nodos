
## W.5. **LAS ARISTAS EN COLA AL CERRAR, EN SU BLOQUE PROPIO Y TITULADO** (`D.29`)

*Van en bloque propio porque `D.29` lo manda asi y porque la `ACTA 25` midio que siete de ocho
encargos se pierden cuando no tienen sede.*

| arista en cola | que la desbloquea | desde |
|---|---|---|
| `crear_espacio_seguro_madurar_ideas_nuevas > nutrir_ideas_nuevas_reunion_solas` | que entre el HIJO, que espera en la bandeja del lote 4 | vuelta 28 (`V.5.h`) |
| `desplegar_plan_orden_operaciones_franqueza_radical > bloquear_tiempo_pensar_calendario` | que entre la MADRE, que espera en la bandeja del lote 4 | **esta vuelta** (`W.3.a`) |

**SON `2`, Y NINGUNA SE PUEDE CABLEAR HOY** sin insertar antes a un candidato que no es de esta tanda.
**Las dos tienen su veredicto escrito en `bitacora/VEREDICTOS.jsonl`**, que es la mitad que `D.29`
protege: lo que se difiere es el cableado, no la lectura.

## W.6. **LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO** (`EXTRACTOR.md` 8)

*Van marcados a ciegas para que el auditor empiece la relectura por ellos, y para que la metrica de
credito distinga una caida dentro del marcado de una fuera.*

| # | el discutible | por que lo marco |
|---:|---|---|
| **1** | **la arista `D.29` nueva**: `desplegar_plan_orden_operaciones_franqueza_radical` MADRE de `bloquear_tiempo_pensar_calendario` | **es el mas fragil de la vuelta y lo pongo el primero.** La `ACTA 28` `2.2` adjudico que **una remision hacia atras no es una cabeza**, y el paso `30` del plan (`cap_12`) remite a un procedimiento de `cap_11`. **Mi lectura es que aquella era una remision suelta dentro de una anecdota y esta es un ITEM de un inventario ordenado**, que es la cara positiva de `D.27`, y que la propia madre se declara cabeza y parte en su `resumen_teorico`. **Si el auditor lee lo contrario, la arista sobra y la caida es mia** |
| **2** | `persuadir_emocion_oyente_no_propia` contra `establecer_credibilidad_pericia_humildad`, `SANO` sin arista | **los dos citan la MISMA linea `L313` en sus pasos**, y son dos de las tres piezas de la retorica que el libro reparte. Firmo `SANO` porque `D.37` exige que **la cuenta este escrita en un paso** y ninguno de los dos dice cuantas piezas son ni nombra al otro, asi que **no hay `--paso n` que citar**. Pero una cabeza existe en el libro (`L321`) y **no es nodo**, asi que estos dos quedan hermanos por un hueco y no por el texto |
| **3** | `establecer_credibilidad_pericia_humildad` contra `compartir_logica_mostrar_razonamiento`, `SANO` | **el mismo caso que el `2` y por eso va aparte**: es el tercer lado del mismo triangulo. Si el auditor decide que `L321` pide nodo, **caen los tres pares de golpe y no uno** |
| **4** | `calibrar_ascensos_evitar_politica` contra `bloquear_tiempo_pensar_calendario`, `SANO` con `paso_contra_nodo = 0.911` | **es la señal mas alta que he visto en toda la campania** y `EXTRACTOR.md` 11 dice de esa banda que **el material del candidato YA VIVE en el grafo**. Firmo falso positivo porque las dos frases son casi identicas (*anima a todo tu equipo a hacer lo mismo*) y **el LO MISMO es cosa distinta en cada una**. **Si me equivoco, es un duplicado que entro con la señal en rojo** |
| **5** | **haber insertado un candidato numero `13` que no es de `cap_07`** | el encargo dice *seguir insertando `cap_07`* en su `TAREA 1` y *la vuelta que inserte al primero* en la `TAREA 2`. **Lei que la `TAREA 2` no se puede hacer sin insertar `bloquear_tiempo_pensar_calendario`**, que es de `cap_11`, y lo meti **despues** de cerrar `cap_07` entero. **Si el auditor lee que la `TAREA 2` era solo para cuando ese candidato tocara por orden, esta insercion se adelanto** |
| **6** | **haber cerrado las `8` lineas `SIN HUELLA` con `anotar` y no volviendolas a juzgar** | `D.15` da **dos** salidas y elegi la segunda. La primera (releer contra el texto de hoy) habria sido **volver a pasar `8` pares por la aduana**, y `anotar` **no toca las huellas**, asi que el instrumento las sigue contando. **Si el auditor lee que declarar sin re estampar la huella no cierra la fila, esta fila sigue abierta y yo la publique como cerrada** |
| **7** | `explicar_idea_facil_comprender_oyente` contra `fijar_fecha_cierre_debate_equipo`, `SANO` con `paso_contra_nodo = 0.610` | es la **unica** señal `3` del tramo que pasa su umbral por lectura y no por ruido de texto corto, y la firmo falso positivo. **Si me equivoco, hay una arista `CLARIFY` a `DEBATE` que no declare** |
| **8** | **haber usado dos vias distintas para las tres aristas de la MISMA serie `D.37`** | la aduana cablea una (`proteger_tiempo`) y `forja.py arista` cablea las otras dos, **segun si la señal levanto a la madre**. El resultado en el dataset es identico y lo compruebo en `W.2.h`, pero **el registro de la bitacora las guarda con `levantada_por` distinto**, y eso es visible. **Si el auditor prefiere una sola via, la eleccion fue mia** |

## W.7. **LO QUE PROPONGO, SIN ADJUDICARME NADA** (`EXTRACTOR.md` 14)

| # | propuesta | su medicion de hoy |
|---:|---|---|
| **1** | que **`python forja.py rancios` distinga un hallazgo DECLARADO de uno que nadie ha mirado** | hoy imprime `RANCIO 26, SIN HUELLA 8` **igual antes y despues de declarar las ocho**, y la distincion **ya existe en el dato**: `34` de `34` llevan `VIGENCIA DECLARADA` en su campo `anotaciones` (`.v30e/vigencia_declarada.txt`). **Sin esa distincion, la fila de la cola va a publicar `8` para siempre** y la vuelta siguiente no sabra si ya se hizo |
| **2** | que se adjudique **que hacer con una entradilla que es cabeza de lista y no trae procedimiento propio** | **`3` de `7` rotulos de etapa de `cap_07` no tienen nodo** (`.v30e/entradillas.txt`), y **esta vuelta ha tenido que escribir tres veces en tres veredictos distintos la frase *su cabeza seria X, que no es nodo***. No propongo crearlos: `EXTRACTOR.md` 9 dice que una cabeza de lista sin procedimiento propio **no es un nodo**, y esto es pedir que se diga si esa consecuencia (piezas hermanas sin madre) es la buscada |
| **3** | que el arnes entregue **la cola de vecinos sellada**, que `D.43` extendida manda desde el 16 sep y esta corrida no trajo | medido hoy: **`26` corridas de la aduana** para `13` candidatos, entre `63` y `136` segundos cada una. **`D.43` saco el informe de lote del turno por exactamente este motivo**, y la extension lo dice de la cola. Hoy la produje yo, una por candidato, porque no habia otra via |

## W.8. EL CIERRE DE LA VUELTA 30

### W.8.a. LAS CUATRO GUARDAS AL CERRAR, CORRIDAS AL CIERRE Y NO AL EMPEZAR (`EXTRACTOR.md` 4)

| guarda | salida | de donde sale |
|---|---|---|
| `python forja.py gate` | `GATE VERDE`, **256** nodos verificados | `.v30e/gate_cierre.txt` |
| `python forja.py guiones` | `BARRIDO DE GUIONES VERDE` | `.v30e/guiones_cierre.txt` |
| `python forja.py resolutor` | **256** vivos, `0` deprecados, `0` alias | `.v30e/resolutor_cierre.txt` |
| `python tests/test_aceptacion.py` | **192** pruebas, `0` fallos, `0` errores | `.v30e/test_cierre.txt` |

### W.8.b. LAS CIFRAS DEL CIERRE, RECOMPUTADAS AL CIERRE Y NO COPIADAS DE LA APERTURA

<!-- TALLADO: salida=.v30e/cuentas_cierre.txt -->

FILA_CUENTAS_CIERRE

### W.8.c. **Y LAS `86` LINEAS NUEVAS DE LA BITACORA, CUADRADAS POR QUIEN LAS ESCRIBIO**

*La tabla de la tanda (`W.2.e`) suma `83`. La bitacora dice `86`. **La diferencia no es un error y la
mido en vez de explicarla.***

<!-- TALLADO: parcial salida=.v30e/cuadre_veredictos.txt -->

FILA_CUADRE_VEREDICTOS

**`82` mas `3` mas `1` igual a `86`.** Las `82` y la `1` son las de la tabla de la tanda (`83`); **las
`3` que faltaban son las declaraciones de arista `D.37`**, que escriben su linea en la bitacora y **no
pasan por `insertar`**, asi que no aparecen en la columna de esa tabla. **Y las `8` anotaciones de
`D.15` no suman ninguna linea**, porque `anotar` escribe DENTRO de la linea que ya existe.

### W.8.d. LA VIGENCIA AL CERRAR, QUE HOY ES COLA Y NO GUARDA (`D.15`)

| | al abrir | **al cerrar** |
|---|---:|---:|
| hallazgos del bloque de vigencia | **34** | **34** |
| `RANCIO` | **26** | **26** |
| `SIN HUELLA` | **8** | **8** |
| **de los `34`, con `VIGENCIA DECLARADA` escrita** | **26** | **34** |
| **sin declarar** | **8** | **0** |
| lineas `no_consumada` y por eso no medidas | **14** | **14** |

**LA CIFRA DEL INSTRUMENTO NO SE MUEVE Y LA DE LA DECLARACION SI**, y las dos filas van juntas a
proposito: es el hallazgo de `W.4.c` puesto donde se ve. **`D.15` dice que este bloque NO pone el gate
en rojo**, y la vuelta 27 adjudico que la vigencia **no tumba** (`ACTA 27`, *`D.15` diciendo
literalmente que la vigencia NO pone nada en rojo*). **No es parada.**

### W.8.e. LA IDENTIDAD, LEIDA DE GIT (`EXTRACTOR.md` 5)

<!-- TALLADO: salida=.v30e/identidad_cierre.txt -->

FILA_IDENTIDAD_CIERRE

### W.8.f. LAS TRES TAREAS, CON SU ESTADO AL CERRAR

| # | tarea | estado | donde |
|---:|---|---|---|
| **1** | seguir insertando `cap_07`, que es donde se paro | **CERRADA, 12 de 12** | `W.2` |
| **2** | el par del calendario, que ninguna señal cruza | **CERRADA**, su veredicto esta en la bitacora | `W.3` |
| **3** | la cola que sigue abierta, para que no se pierda | **CERRADA como tarea**, y **4 de sus filas se cierran como cola** | `W.4` |

**Son TRES y el tope son cinco** (`EXTRACTOR.md` 1.3). **Ninguna queda a medias y ninguna se declara
como cola de esta vuelta.**

> ### **Y LA VUELTA NO CIERRA CORTA: CIERRA EN EL TECHO** (`EXTRACTOR.md` 12.4)
>
> **`13` candidatos contra un tramo de entre `5` y `15`.** El encargo preveia el caso (*si la
> insercion se come la vuelta, la vuelta se cierra ahi y lo declaras con su cifra*) **y esta vez la
> insercion cupo entera**, con las tres tareas dentro.
>
> **EL COSTE, MEDIDO Y NO ESTIMADO:** `26` corridas de la aduana (una para leer la cola de cada
> candidato y otra para insertarlo con sus veredictos escritos), **entre `63` y `136` segundos cada
> una**. Eso es lo que impidio la cuarta tarea de `cap_04`, y va dicho en `W.4.e` con su fila.

### W.8.g. **LAS SEIS CONDICIONES DE PARADA, REPASADAS UNA A UNA** (`EXTRACTOR.md` 7)

| condicion | lo que mido | veredicto |
|---|---|---|
| algo contradice una regla vigente | ninguna regla se contradijo; los dos casos dudosos (`D.37` sin cuenta escrita, la remision de `cap_12`) **se resolvieron dentro de la regla y van marcados como discutibles**, que es lo que `EXTRACTOR.md` 8 manda | **NO ES PARADA** |
| algo contradice una cifra publicada con su corte | **cero discrepancias**: las `6` de apertura, los `77` pares, los `12` candidatos, los `90` pasos, los `6` y `48` de `cap_04` y los `3` tramos de entradilla **salen todos al digito** contra el encargo y contra `APERTURA_CIEGA.md` | **NO ES PARADA** |
| una operacion cuyo texto no alcanza para ejecutarse sin decidir | la `TAREA 2` pedia decidir **cuando** entra `bloquear_tiempo_pensar_calendario`, y el propio encargo lo resuelve (*la vuelta que inserte al primero*). **Lo ejecute y marque la decision como discutible `5`** | **NO ES PARADA** |
| un pendiente de doctrina | **hay dos** (la entradilla sin nodo, y si `rancios` debe distinguir lo declarado). **`EXTRACTOR.md` 7 dice que un pendiente de doctrina NO detiene**: van a `W.7` como propuestas y la vuelta sigue | **NO ES PARADA** |
| una guarda en rojo al sellar (`D.45`) | las cuatro en verde al cerrar (`W.8.a`), **corridas al cierre y no al empezar**, y el arbol queda limpio | **NO ES PARADA** |
| una caida de dato | **ninguna**. `13` inserciones, `13` incrementos consecutivos del censo de `244` a `256`, **el cerrojo sin avisar una sola vez**, y la bitacora con `8` lineas tocadas y `367` intactas, comprobado por diferencia | **NO ES PARADA** |

**NINGUNA DE LAS SEIS SE CUMPLE. LA VUELTA 30 CIERRA SIN PARADA Y SIN CAIDA DE DATO DECLARADA.**
