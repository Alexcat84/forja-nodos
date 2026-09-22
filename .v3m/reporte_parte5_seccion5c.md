## 5.c. LAS DOS ADUANAS EN SECO, Y LA LECTURA DE LOS VECINOS QUE LEVANTARON (`EXTRACTOR.md` 2)

    $ python forja.py informe cuarentena/marquet_turn_the_ship/declarar_intencion_reemplazar_peticion_permiso.json > .v3m/aduana/c3.txt
    $ python forja.py informe cuarentena/marquet_turn_the_ship/resistir_dar_solucion_clasificar_decision_urgencia.json > .v3m/aduana/c4.txt

```
============================================================================
INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
============================================================================
candidatos revisados        : 1
poblacion del barrido       : 451   (346 del grafo mas 105 que esperan en bandejas)
umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

EL SALDO
  ENTRARIAN sin leer nada          : 0
  BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
  CAERIAN por una guarda           : 0
  CHOCAN entre si dentro del lote  : 0

LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
  vecinos levantados en total      : 2
  por candidato bloqueado          : menor 2, mediana 2, mayor 2
  que señal levanta cada vecindad  : similitud_texto 2

[BLOQUEARIA] declarar_intencion_reemplazar_peticion_permiso   (declarar_intencion_reemplazar_peticion_permiso.json)
    vecino resistir_dar_solucion_clasificar_decision_urgencia  [levantada por: similitud_texto]
      similitud_texto 0.468 | familia_id 0.000 | paso_contra_nodo 0.439
      paso 2 del candidato contra paso 4 de resistir_dar_solucion_clasificar_decision_urgencia
    vecino informar_cierre_jornada_conservar_propiedad_trabajo  [levantada por: similitud_texto]
      similitud_texto 0.383 | familia_id 0.000 | paso_contra_nodo 0.391
      paso 2 del candidato contra paso 3 de informar_cierre_jornada_conservar_propiedad_trabajo
```

```
============================================================================
INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
============================================================================
candidatos revisados        : 1
poblacion del barrido       : 451   (346 del grafo mas 105 que esperan en bandejas)
umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

EL SALDO
  ENTRARIAN sin leer nada          : 0
  BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
  CAERIAN por una guarda           : 0
  CHOCAN entre si dentro del lote  : 0

LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
  vecinos levantados en total      : 2
  por candidato bloqueado          : menor 2, mediana 2, mayor 2
  que señal levanta cada vecindad  : similitud_texto 2

[BLOQUEARIA] resistir_dar_solucion_clasificar_decision_urgencia   (resistir_dar_solucion_clasificar_decision_urgencia.json)
    vecino aplicar_ejercicio_codigo_genetico_control  [levantada por: similitud_texto]
      similitud_texto 0.356 | familia_id 0.000 | paso_contra_nodo 0.452
      paso 3 del candidato contra paso 2 de aplicar_ejercicio_codigo_genetico_control
    vecino declarar_intencion_reemplazar_peticion_permiso  [levantada por: similitud_texto]
      similitud_texto 0.451 | familia_id 0.000 | paso_contra_nodo 0.416
      paso 3 del candidato contra paso 2 de declarar_intencion_reemplazar_peticion_permiso
```

**LAS TRES COLUMNAS DE CADA UNA: `0 ENTRARIA`, `1 BLOQUEARIA`, `0 CAERIA`.** Ninguna cae; las dos quedan
en cola de lectura, que es lo que toca ahora mismo.

### 5.c.1. LA LECTURA DE LOS CUATRO PARES, HECHA EN EL ACTO Y NO APLAZADA

**El par `declarar_intencion` contra `resistir_dar_solucion` pasa de `0,4` en las dos direcciones
(`0,468` y `0,451`), la banda ALTA de la seccion 11 (`donde el catalogo entero no tiene ni un ajeno`),
asi que se lee primero y con todo el cuidado que la regla pide:**

| paso citado | texto |
|---|---|
| `declarar_intencion` P2 | *declara tu intencion con frases activas: tengo la intencion de, planeo, hare, haremos* |
| `resistir_dar_solucion` P3 | *si la decision es urgente, tomala tu mismo y despues haz que el equipo la someta a critica y la evalue* |
| `resistir_dar_solucion` P4 | *si la decision se puede tomar en un plazo razonablemente proximo, pide la opinion del equipo, aunque sea breve, y despues decide* |

**NO SON GEMELOS.** `declarar_intencion` es un mecanismo de VOCABULARIO (que frases decir y que frases
evitar al proponer una accion, con una respuesta de aprobacion simple); `resistir_dar_solucion` es un
mecanismo de CLASIFICACION POR URGENCIA (que tanto delega el responsable segun cuanto tiempo hay para
decidir). Ninguno de los dos pasos citados por el instrumento comparte el medio, la etapa o el objeto de
trabajo del otro: comparten vocabulario de superficie (`decision`, `equipo`, la coletilla `el texto lo
dice asi` que todos los candidatos de esta forja llevan pegada), no procedimiento. **Los dos vienen de
capitulos consecutivos del mismo libro sobre la misma doctrina general (delegar autoridad de decision),
que es exactamente el caso que la seccion 12 ya nombra: `un capitulo entero cae en la misma familia... es
señal de que el libro trata un tema, no de duplicado`,** aplicado aqui entre dos capitulos y no dentro de
uno solo. **Sostengo los dos como nodos distintos, SANOS entre si.**

**Los otros dos pares, en la banda por debajo de `0,4` (seccion 11, ruido o casi):**

| par | similitud | leido | veredicto propuesto |
|---|---:|---|---|
| `declarar_intencion` P2 contra `informar_cierre_jornada_conservar_propiedad_trabajo` P3 | `0,383` | P3 anuncia CUANDO se vera el resultado de un trabajo (*we'll be able to show the rough plan to the captain tomorrow*); no comparte ni el medio ni la etapa con declarar una intencion en vocabulario activo | SANO |
| `resistir_dar_solucion` P3 contra `aplicar_ejercicio_codigo_genetico_control` P2 | `0,356` | P2 identifica que decisiones son candidatas a bajar de nivel (paso 2 de un ejercicio de mapeo de autoridad); P3 de `resistir_dar_solucion` decide QUIEN resuelve una decision urgente ya identificada; son etapas de mecanismos distintos que comparten el tema general de delegar decisiones | SANO |

**NINGUN PAR ES GEMELO.** Los cuatro comparten la doctrina de fondo de este tramo del libro (delegar la
autoridad de decision, capitulos `11` y `12` sobre la base ya sentada en `cap_06`), y eso es exactamente
la señal barata que la regla ya advierte que hay que esperar, no resolver subiendo un umbral. **Marco el
par de la banda ALTA (discutible `4` de la cabecera) para que el auditor lo relea primero, con esta
lectura completa delante.** Ningun veredicto se escribe en `bitacora/VEREDICTOS.jsonl`: esta vuelta no
inserta, y esa bitacora es sede de la aduana en `insertar` (`EXTRACTOR.md` 14), no del extractor en
regimen ligero.
---
