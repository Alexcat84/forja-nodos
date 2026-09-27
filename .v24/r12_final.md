
## R.12.b. LAS GUARDAS, **CORRIDAS AL CERRAR**

| guarda | comando | resultado |
|---|---|---|
| gate de integridad | `python forja.py gate` | **GATE VERDE**, 214 nodos verificados, 12 guardas |
| barrido de guiones | `python forja.py guiones` | **BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.** |
| prueba de aceptacion | `python tests/test_aceptacion.py` | **total: 111 pruebas, 0 fallos, 0 errores** |
| tallado del reporte (`D.41`) | `python scripts/tallar_reporte.py` | **TALLADO VERDE**, 36 tablas comprobadas celda a celda, **0 que difieren**, 0 sin comprobar |

**Y EL HOOK CORRIO EN TODOS LOS COMMITS DE ESTA VUELTA, sin saltarse ninguno.** El tallado **aborto
uno** (`R.9` caida 7) y **se arreglo regenerando**, no tecleando la celda buena.

## R.12.c. LAS PARADAS, REPASADAS UNA A UNA (`EXTRACTOR.md` 7)

| condicion | hubo? |
|---|---|
| algo contradice una regla vigente | **SI, UNA**, y va entera en `R.2.d`: el remedio 3 de mi encargo me manda escribir en `docs/BANCO_DE_REGLAS.md`, que `EXTRACTOR.md` 14 asigna a Alexis. **La declaro y no la arreglo yo**, y dejo el texto escrito y listo para pegar |
| algo contradice una cifra publicada con su corte | **NO** |
| una operacion cuyo texto no alcanza para ejecutarse sin decidir | **NO.** Las cinco tareas traian texto suficiente |
| **PARA_ALEXIS.md** | **no lo escribo yo**, y no lo he tocado |

## R.12.d. LO QUE PASA A LA VUELTA SIGUIENTE

| que | cifra | de donde sale |
|---|---|---|
| **la tanda de insercion sin terminar** | **131** candidatos en cuarentena de 142 (`R.6.d`) | `python .v24/tanda_v24.py` |
| **los pares que los 7 candidatos parados abren** | **24** por leer (`R.6.d`) | idem |
| **las aristas declaradas y no cableadas** | **71** (`R.7.a`) | `python .v24/deuda_v24.py` |
| **los 19 veredictos de insercion ya escritos y no gastados** | **19** en `.v24/veredictos_insercion.json` (`R.8`) | se pasan a `forja.py insertar` en el intento siguiente |
| **la relectura ancha de las filas de hueco del freno** | **5 filas** (`R.10`) | ya encargada por la `ACTA 23` `11.1` como primera tarea de la vuelta 25 |
| **la correccion 9 de la vuelta 22** | 1, viva y escrita por tercera vez (`R.7.c`) | su acto es el cableado |
| **la PARADA de la sede del banco** | 1 (`R.2.d`) | la resuelve quien tenga la sede |

## R.12.e. LA IDENTIDAD DE LA VUELTA, **LEIDA DE GIT** (`EXTRACTOR.md` 5)

    $ git rev-parse --abbrev-ref HEAD
    extraccion-mundo-11
    $ git log --oneline 74134e0..HEAD | wc -l
    7

## R.12.f. LA VUELTA 24, EN UNA TABLA

| | |
|---|---|
| **tareas encargadas** | **5**, que es el tope. **Las cinco CERRADAS**, y la quinta **cerrada declarando lo que no cupo con su cifra** |
| **unidades minadas** | **`cap_14` (`Bonus Chapter`), ENTERA**, con su frontera de **17 piezas** cerrada al digito contra el cuerpo (**7.638** igual a **7.638**, residuo **0**) |
| **candidatos nuevos** | **15**, que es **exactamente el techo** de `EXTRACTOR.md` 12.4. Hueco que queda: **0** |
| **el lote 4** | # **CIERRA EN EXTRACCION: `0` unidades sin minar**, medido con mi instrumento y no supuesto. Llevaba seis vueltas sin poder cerrar |
| **aduana de escritura** | **17 corridas del informe de un candidato**, una por candidato en su acto mas dos repeticiones por correccion. **1 `CAERIA`**, corregido y declarado dentro del fichero |
| **insercion** | # **`11` de `142`. LA TANDA NO CUPO Y LO DIGO CON SU CIFRA.** Grafo **203** a **214**, bitacora **148** a **156**, `_insertados` **201** a **212** |
| **veredictos** | **25 pares** leidos al escribir (sede: este reporte) mas **19** escritos para la insercion, de los cuales **8 ya viven en `bitacora/VEREDICTOS.jsonl`**, escritos por la aduana y no a mano. # **Es la primera vez en la campania que un veredicto mio llega a su sede** |
| **aristas** | **71 declaradas y no cableadas** (53 heredadas, 4 de la TAREA 3, 14 de `cap_14`), **cero cableadas** y la razon medida: ninguna tiene sus dos extremos dentro del grafo |
| **`PASOS INVENTADOS`** | peor fila firmada `cap_04` **`16,67`** contra tope **`10`**. # **EL FRENO SIGUE DISPARADO.** Lote 4 **`2,07` (35 de 1.688)**, **declarado INCOMPLETO** |
| **discutibles** | **8, marcados antes de saber si acierto**, y en seis escribo el argumento contra mi propia decision |
| **caidas mias** | **7, las siete cazadas ANTES de publicar**, y **cinco de las siete las cazo un instrumento y no mi cuidado** |
| **paradas** | # **UNA**, declarada y no arreglada por mi (`R.2.d`) |

> # **LA VUELTA 24 CIERRA EL LOTE 4 EN EXTRACCION Y ABRE LA INSERCION QUE LLEVABA SEIS VUELTAS SIN PODER OCURRIR. ENTRARON 11 DE 142.**
>
> **LO QUE MAS ME IMPORTA DE ESTA VUELTA NO ES EL 11: ES QUE POR PRIMERA VEZ HAY VEREDICTOS MIOS EN
> SU SEDE.** Ocho lineas nuevas en `bitacora/VEREDICTOS.jsonl`, escritas por `forja.py insertar` en
> el acto, con la razon que yo escribi leyendo a los dos vecinos. **Hasta hoy mis veredictos vivian
> en este reporte, que no es sede de esa especie**, y el encargo me lo dijo antes y no despues.
>
> **Y LO QUE ESTA VUELTA MIDE Y NADIE HABIA MEDIDO, que es lo que le sirve a quien planifique la
> siguiente:** la cola de lectura de una insercion **no es fija: crece mientras se paga**. El mismo
> candidato levanto **1** vecino contra 205 nodos y **3** contra 214. **Cualquier estimacion de
> cuanto queda que yo diera hoy seria inventada**, y por eso no la doy.
