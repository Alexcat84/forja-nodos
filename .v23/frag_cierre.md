
---

# Q.12. EL CIERRE DE LA VUELTA 23

## Q.12.a. LAS TRES GUARDAS, CORRIDAS AL CERRAR Y NO AL EMPEZAR

Salida de `python forja.py gate`, guardada en `.t1_v23/salida_gate_cierre.txt`:

PEGAR_GATE_AQUI

Salida de `python forja.py guiones`, guardada en `.t1_v23/salida_guiones_cierre.txt`:

PEGAR_GUIONES_AQUI

Salida de `python tests/test_aceptacion.py`, guardada en `.t1_v23/salida_aceptacion_cierre.txt`:

PEGAR_ACEPTACION_AQUI

**Y EL HOOK NO SE SALTO NI UNA VEZ.** Cada commit de esta vuelta paso por `gate`, `guiones` y el
**tallado de `D.41`**, y el tallado **aborto un commit** cuando dos marcadores mios cayeron sobre las
tablas de la vuelta 22 (`Q.9` caida 4). **Se arreglo moviendo el marcador, no tecleando la celda.**

## Q.12.b. EL ESTADO AL CIERRE, **RECOMPUTADO AL CIERRE** (`EXTRACTOR.md` 4)

Salida de `python .t1_v23/cierre_v23.py`, guardada en `.t1_v23/salida_cierre_v23.txt`:

PEGAR_CIERRE_AQUI

## Q.12.c. LOS PARES LEIDOS Y SUS VEREDICTOS, **IMPRESOS DE LOS INFORMES**

*`EXTRACTOR.md` 2: si la aduana bloquea, **lees a los vecinos antes de escribir el veredicto**, y
todo veredicto lleva su razon escrita. **Su sede propia es `bitacora/VEREDICTOS.jsonl` y hoy no puede
serlo**, porque a la bitacora se escribe por `forja.py insertar` y esta vuelta no inserta. **Lo digo
en vez de esconderlo: hoy su sede es este reporte.***

Salida de `python .t1_v23/veredictos_v23.py`, guardada en `.t1_v23/salida_veredictos_v23.txt`:

PEGAR_VEREDICTOS_AQUI

**LAS RAZONES ENTERAS, UNA POR PAR, ESTAN EN LA SECCION 2 DE ESE MISMO FICHERO**
(`.t1_v23/salida_veredictos_v23.txt`), y el guion **sale en rojo si un solo par levantado se queda
sin razon escrita**. Hoy sale en verde.

## Q.12.d. LAS RUTAS QUE PUBLICO COMO PRUEBA, **CON SU ALCANCE DICHO**

| ruta | que guarda | alcance |
|---|---|---|
| `.t1_v23/` | **mis instrumentos de esta vuelta y su salida guardada** | 9 guiones y sus ficheros de salida. **Es lo que el tallador compara celda a celda** |
| `.aduana_v23/` | **un informe de la aduana por candidato**, 20 en total | **solo informes de UN candidato**. El del lote entero no existe en esta corrida (`Q.0.2`) |
| `.v23/` | los fragmentos con los que arme este reporte | andamio, no prueba |
| `cuarentena/scott_radical_candor/` | **los 127 candidatos del lote 4** | **los 14 nuevos y los 6 corregidos viajan dentro del commit** (`D.25`), asi que quien lea *de `cap_13` salieron 12 candidatos* **puede abrir los doce** |

## Q.12.e. LO QUE PASA A LA VUELTA SIGUIENTE

| que | cifra | quien lo desbloquea |
|---|---|---|
| **`cap_14`**, la ultima unidad sin minar del lote 4 | **7.638** palabras | **y con el, el cierre del lote 4** |
| **las 52 aristas declaradas y no cableadas** | **52** | el mismo acto: la insercion del lote cerrado |
| **los veredictos sin sede propia** | **12 de la vuelta 22 mas 14 pares de hoy** | idem |
| **la relectura ancha de cinco filas del freno** | **96 ocurrencias** sin adjudicar | una tarea propia, que propongo en `Q.11.b` |
| **la pregunta del rotulo de `cap_14`** | 1 | Alexis o el auditor, y va en `Q.11.a` |

## Q.12.f. LA IDENTIDAD DE LA VUELTA, **LEIDA DE GIT** (`EXTRACTOR.md` 5)

Salida de los comandos, guardada en `.t1_v23/identidad_v23.txt`:

PEGAR_IDENTIDAD_AQUI

## Q.12.g. LA VUELTA 23, EN UNA TABLA

| | |
|---|---|
| **tareas encargadas** | **4**, el tope es 5. **Las cuatro CERRADAS**, una de ellas (la 4) **cerrada declarando que no se hace y por que**. Cero cola por techo de tareas |
| **la cola de siete** | **CERRADA ENTERA Y PRIMERA**, como el encargo mandaba. Seis tocan fichero y **las seis vuelven a pasar la aduana**; la septima es encargo para el dia de la insercion y queda escrita dos veces |
| **unidades minadas** | **`cap_12` (`Getting Started`) y `cap_13` (`Afterword`), las dos ENTERAS**, con su frontera cerrada contra el cuerpo al digito (**2.118** y **9.298** palabras) |
| **candidatos nuevos** | **14** (2 mas 12), **bajo el techo de 15**. Hueco que queda: **1** |
| **`cap_14`** | # **NO ENTRA, y se declara con su cuenta**: 7.638 palabras no caben en un hueco de un candidato, y `EXTRACTOR.md` 12.4 prohibe repartir un capitulo en dos vueltas |
| **aduana** | **20 informes de un candidato, uno por candidato y en su acto.** Saldo en `Q.5.d`. # **CERO `CAERIA`** |
| **insercion** | # **CERO, por sexta vez con la puerta abierta**, y la razon medida: **al lote 4 le falta `cap_14` y solo `cap_14`**. Grafo `203` a `203`, bitacora `148` a `148`, `_insertados` `201` a `201` |
| **veredictos** | **14 pares distintos leidos, 15 filas con su razon escrita.** **Su sede hoy es este reporte y lo digo**; `bitacora/` lo sera el dia de la insercion |
| **aristas** | **52 declaradas y no cableadas** (`35` heredadas, `2` de la correccion 6, `15` nuevas), **repetidas enteras en `Q.7`** con su paso impreso del fichero |
| **`PASOS INVENTADOS`** | **peor fila firmada `cap_04` `16,67` contra tope `10`**. # **EL FRENO SIGUE DISPARADO Y EL TRAMO SIGUE EN DOS CAPITULOS, que son los dos que esta vuelta mino.** Lote 4 **`2,32` (35 de 1.511)**, **declarado INCOMPLETO**: cinco filas sin releer con el ancho |
| **discutibles** | **11, marcados antes de saber si acierto**, y en siete escribo el argumento contra mi propia decision |
| **caidas mias** | **5, las cinco cazadas ANTES de publicar**, y **dos de las cinco las cazo un instrumento y no mi cuidado** |
| **guardas** | `gate`, `guiones` y `test_aceptacion` **corridas al cerrar**. Hook verde en todos los commits, **ninguno saltado**, y el tallado **aborto uno y se arreglo regenerando** |
| **tablas de instrumento** | **todas pegadas de su fichero, ninguna tecleada**, comprobadas celda a celda por el hook en cada commit |
| **paradas** | # **CERO.** Nada contradijo una regla vigente ni una cifra publicada con su corte |

> # **LA VUELTA 23 CIERRA `cap_12` Y `cap_13` ENTEROS, PAGA LA COLA DE SIETE DEL AUDITOR COMPLETA, Y DEJA EL LOTE 4 A UN SOLO CAPITULO DE CERRAR.**
>
> **Y LA COSA QUE MAS ME IMPORTA DE ESTA VUELTA NO ES LA CIFRA DE CANDIDATOS: ES QUE NINGUNA TABLA
> SE TECLEO.** Mi racha `REPORTE` se reinicio contra `D.41` despues de **cuatro caidas en cuatro
> vueltas que eran la misma cosa**. Esta vuelta el tallador **me cazo dos veces en el acto** (`Q.9`
> caidas 4 y 5) y **las dos se arreglaron regenerando**, no tecleando la celda buena.
>
> **LO QUE ESO PRUEBA, Y NO ES UN MERITO MIO:** *un remedio que se cumple acordandose no es un
> remedio.* La diferencia entre la vuelta 22 y esta **no es que yo tenga mas cuidado: es que hay
> codigo mirando.**
