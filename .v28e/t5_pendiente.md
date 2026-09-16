
## V.6. TAREA 5: **EL HUECO DE TRANSCRIPCION DE `L153`, Y EL RESTO DE LA COLA CON SU CIFRA**

### V.6.a. **`5.a`: EL HUECO ES CIERTO, LO MIDO, Y NO LO ARREGLO PORQUE NO HAY CON QUE**

**LA LINEA, REABIERTA CON MI LECTOR Y PEGADA** (`D.35`, salida en `.v28e/hueco_L153.txt`):

<!-- TALLADO: parcial salida=.v28e/hueco_L153.txt -->

    153: Sometimes creating a culture of listening is simply a matter of managing meetings the
         right way. When just a couple of people were doing all the talking at a meeting, I'd
         stop and go around the table to ensure that everyone got heard. Other times, I would
         stand up in the next meeting and walk around, physically blocking a person who was
         talking too much. Sometimes I'd have a quick conversation with people before a
         meeting, asking some to pipe up and others to pipe down. ...

**LOS TRES MODOS DEL LIBRO, Y LOS DOS QUE EL NODO RECOGE:**

| # | lo que el libro pone en `L153` | en `crear_cultura_escucha_equipo` |
|---:|---|---|
| **1** | parar y dar la vuelta a la mesa | **su paso `16`** |
| **2** | levantarse en la reunion siguiente y pasear, bloqueando fisicamente a quien habla de mas | **NO ESTA** |
| **3** | hablar en corto antes de la reunion, pidiendo a unos que suban la voz y a otros que la bajen | **su paso `17`** |

**EL NODO TIENE `17` PASOS Y NINGUNO ES EL SEGUNDO.** Confirmado leyendo el nodo del grafo, no la
bandeja: el fichero ya esta en `cuarentena/_insertados/`.

> **`LECTURA`: un paso que FALTA no es un paso INVENTADO.** No sube `PASOS INVENTADOS` y no entra en
> la metrica de credito. Es un hueco de transcripcion, y su sitio es la cola.

**Y AHORA LA MITAD QUE EL ENCARGO ME PIDE DECIR CON SU CIFRA EN VEZ DE IMPROVISAR**
(`EXTRACTOR.md` 7), **con el `grep` pegado como manda el remedio bloqueante de la `ACTA 27`:**

<!-- TALLADO: parcial salida=.v28e/grep_operacion_pasos.txt -->

    $ grep -in "pasos_accionables" src/correccion.py src/arista.py src/anotacion.py
    src/arista.py:121:    pasos = nodo_madre.get("pasos_accionables") or []

**Esa unica coincidencia LEE el paso de la madre para citarlo; no lo escribe.** El repaso de las
operaciones que escriben, una a una:

| operacion | que toca | alcanza el hueco |
|---|---|---|
| `forja.py insertar` | mete un nodo NUEVO | **NO**: `crear_cultura_escucha_equipo` ya vive, y la aduana rechaza *el id ya vive en el grafo* |
| `forja.py corregir` | **solo** `resumen_teorico` | **NO**, y lo rechaza por escrito: *los pasos, el titulo y el entregable NO se corrigen por aqui* |
| `forja.py arista` | `nodos_previos` y `nodos_siguientes` | **NO** |
| `forja.py anotar` | la razon de una linea de la bitacora | **NO**, y no toca el dataset |

> ### **NO LO ARREGLO, Y LA CIFRA ES `1` DE `3`**
>
> **NINGUNA OPERACION DE ESTA CASA AÑADE UN PASO A UN NODO QUE YA VIVE**, y `EXTRACTOR.md` 2 prohibe
> escribir a mano en `dataset/nodos.jsonl`, **siempre**. El encargo lo previo con estas palabras: *si
> lo unico que hay para eso es `corregir`, que solo toca `resumen_teorico`, entonces no alcanza y lo
> dices con su cifra en vez de improvisar.* **Asi queda dicho.**
>
> **LA CIFRA:** `1` modo de `3` sin transcribir, en `1` nodo, sobre `1` linea (`L153`). **El nodo
> conserva sus `17` pasos y ninguno se toca.**

### V.6.b. **LO QUE PROPONGO PARA ESTE HUECO, SIN ADJUDICARMELO** (`EXTRACTOR.md` 14)

*Lo escribo como propuesta y sigo, que es lo que la seccion 14 manda, y no como parada: la parada es
para lo que contradice una regla vigente, y aqui **ninguna regla se contradice**. Lo que hay es una
via que no existe.*

| # | lo que propongo | por que, y cual es su vara |
|---:|---|---|
| **7** | **una operacion que AÑADA un paso transcrito a un nodo que ya vive**, con la linea del libro citada y su huella, del mismo corte que `corregir`: solo aniade, nunca sustituye ni borra, y pasa el gate sobre copia | el hueco de `L153` es el **primero medido**, y no sera el ultimo: la vara de `D.30` caza el paso que sobra y **no tiene gemela para el que falta**. Lo que NO propongo es que pueda **cambiar** un paso: cambiar un paso es cambiar el procedimiento y eso entra por la aduana como candidato |

### V.6.c. **`5.b`: EL RESTO DE LA COLA, CON SU CIFRA Y SU SEDE, RECONTADA HOY**

| lo que queda | cifra al abrir | **cifra al cerrar** | estado |
|---|---:|---:|---|
| la arista `recorrer_rueda_conscientemente_cultura_equipo --paso 4--> recorrer_rueda_hacer_cosas_equipo` | **1** | **0** | **CERRADA en `V.5`** |
| la mitad `Burnout` de la serie `D.37` de `aprender_resultados_vencer_dos_presiones` | **1** | **1** | sigue: `cuidarse_agotamiento_centro_rueda` no entro (`V.5.i`) |
| la serie `D.37` de `minimizar_impuesto_colaboracion_equipo` | **3** partes | **3** | sigue: ni la cabeza ni sus tres partes entraron (`V.5.i`) |
| **NUEVA**: la arista en cola `crear_espacio_seguro_madurar_ideas_nuevas > nutrir_ideas_nuevas_reunion_solas` | 0 | **1** | la desbloquea que entre el hijo (`V.5.h`) |
| **NUEVA**: los `12` candidatos de `cap_07` que no cupieron, con su cola de lectura | 0 | **12** candidatos, **77** pares | la vuelta siguiente (`V.5.g`) |
| `cap_04` releido antes que las tres filas de hueco | **6** candidatos, **48** pasos | **6** y **48** | **SIGUE SIN CABER, y lo declaro otra vez con su motivo** |
| la frontera por capitulo con las `QUESTIONS TO CONSIDER` y su clase escrita | **14** de **17** unidades | **14** de **17** | la vuelta que mine un capitulo del lote 5 |
| el lote 5 por su orden | **3** candidatos en bandeja | **3** | **NO TOCADO**, y es deliberado |

**POR QUE `cap_04` TAMPOCO CABE, Y LA CIFRA LO DICE SOLA:** esta vuelta trajo **dos tareas de codigo
bloqueantes** (`2` y `3`) con **seis mitades y sus casos positivos**, y un tramo de insercion que es
**el techo entero** de `EXTRACTOR.md` 12.4. **Releer `6` candidatos y `48` pasos mas es una tarea
sexta**, y el tope son cinco.

**POR QUE EL LOTE 5 NO SE TOCA, Y NO ES QUE SE ME HAYA OLVIDADO:** `D.39` lo dice por su letra, **los
candidatos de un lote ABIERTO se quedan en cuarentena hasta que su lote cierre**, y el encargo lo
repite. Sus `3` candidatos siguen en bandeja, sin una sola insercion.
