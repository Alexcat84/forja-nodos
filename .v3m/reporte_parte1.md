# VUELTA 3 DEL FRENTE `marquet_turn_the_ship`: **PAGAR EL PUENTE DE `cap_06`, CERRAR SU ADUANA, Y MINAR `cap_07` Y `cap_08`**

*Tercer turno de este frente, en **MODO AUSTERO** (`D.47`) y **REGIMEN LIGERO** (`D.58`,
`MODO_INSERCION=cuarentena`). El encargo esta en `docs/loop/PROMPT_SIGUIENTE.md`, escrito por el
auditor del bucle al cerrar la `ACTA M3`. **Este frente no inserta nunca.***

## Apertura, medida antes de la primera operacion (`EXTRACTOR.md` 4)

| | | de donde sale |
|---|---|---|
| fecha | **2026-09-21** | `date "+%Y-%m-%d"`, corrida en esta vuelta |
| rama | `extraccion-marquet_turn_the_ship` | `git rev-parse --abbrev-ref HEAD` |
| commit de apertura | `9656eba` | `git rev-parse HEAD`, tras commitear el estado de arnes pendiente (`TABLERO.jsonl`, `loop.log`, `ultimo_auditor.json`, `ultimo_extractor.json`) |
| nodos en el dataset al empezar | **346** | `python forja.py gate`, linea 2 |
| candidatos en bandeja del lote al empezar | **12** | `ls cuarentena/marquet_turn_the_ship/*.json \| wc -l` |
| unidades en la bandeja de entrada | **17** | `ls fuentes/marquet_turn_the_ship/*.md \| wc -l` |
| inserciones autorizadas en esta vuelta | **CERO** | `docs/loop/PROMPT_SIGUIENTE.md`: `MODO_INSERCION=cuarentena` |
| credito de esta linea al abrir | `AUDITOR` `0 de 3`, `CIFRA PUBLICADA` `0 de 2`, `CLASE` `0 de 2`, `DATO MOVIDO` `0 de 2`, `REPORTE` `1 de 3` | `python forja.py credito` |
| deuda de esta linea al abrir | `LIBRE`, `1 de 5` desde la vuelta `2`, `32` deuda(s) esperando | `python scripts/deuda.py --clase 3` |

**DISCREPANCIA DECLARADA CONTRA LA CIFRA DEL ENCARGO** (`EXTRACTOR.md` 5): la seccion `2.4` del
encargo cita `python scripts/deuda.py --clase 3` dando *van 2 de 5... con 27 deuda(s) esperando*, y mi
propia corrida de hoy da **`1 de 5`, con `32` deuda(s) esperando**. No copio la del encargo: entre que
el auditor cerro su acta y esta vuelta abrio, el conteo de deuda avanzo (el instrumento manda, no la
nota vieja). No lo investigo mas: es exactamente el caso que `EXTRACTOR.md` 5 pide declarar y no
resolver copiando.

### La tarea

| # | capitulo / bloque | estado | candidatos |
|---|---|---|---:|
| 1 | Registros: correccion declarada, `PASOS INVENTADOS`, credito, deuda | **CERRADA** | |
| 2 | Bloqueante: pagar el puente vivo de `cap_06` | **CERRADA** | |
| 3 | Cerrar la aduana que la vuelta 2 dejo abierta | **CERRADA** | |
| 4 | Releer `cap_06` entero contra sus 51 filas | **CERRADA** | |
| 5 | `cap_07` | **CERRADA** | **1** (`declarar_intencion_reemplazar_peticion_permiso`, ver aduana) |
| 5 | `cap_08` | **CERRADA** | **1** (`resistir_dar_solucion_clasificar_decision_urgencia`, ver aduana) |

### Discutibles marcados ANTES de saber si acierto

*(se anexan aqui segun aparecen, por numero y linea, sin reabrir el argumento: `D.47`)*

| # | discutible | donde |
|---:|---|---|
| 1 | `declarar_intencion_reemplazar_peticion_permiso` junta dos tramos NO contiguos de `cap_07` (`L55` y `L73` a `L93`) en una sola pieza, porque nombran el mismo mecanismo de `L57` | seccion 5.a.4 |
| 2 | la extension del mecanismo de `cap_07` (`L97` a `L107`, pedir el razonamiento completo para responder solo aprobacion) se sostiene como POSTURA y no se mina, por no traer rotulo propio ni inventario | seccion 5.a.4 |
| 3 | `resistir_dar_solucion_clasificar_decision_urgencia` junta dos tramos NO contiguos de `cap_08` (`L107` y `L115` a `L121`) en una sola pieza, por el mismo motivo, mecanismo de `L103` | seccion 5.b.4 |
---

# TAREA 1. LOS REGISTROS AL DIA (`ACTA M3` `M3.17`, `M3.18`)

## 1.a. CORRECCION DECLARADA sobre tres cifras de la vuelta 2, sin borrar el texto viejo (`EXTRACTOR.md` 5)

*`ACTA M3` `M3.4.a` recompuso las `121` filas de las tres fronteras de la vuelta 2 fila a fila contra
el fichero y encontro que la cuenta de piezas pegada como si fuera salida de instrumento **no incluia
las piezas `P` que se minan**, solo las filas `R`.*

| donde | dice (vuelta 2) | es (`ACTA M3` `M3.4.a`) |
|---|---|---|
| `docs/loop/REPORTE.md:57515` (`1.b` pegado) y `docs/loop/REPORTE.md:57576` (`1.g` tabla) | `piezas: 24`, *unidades leidas (piezas) `24`*, *postura/caso/residuo/pendiente `23`* | **`25`** piezas (`24` filas `R` mas `P1`), **`25`** unidades leidas, **`24`** de residuo/postura/caso/pendiente |
| `docs/loop/REPORTE.md:57784` (`3.b` pegado) | `piezas: 49` | **`51`** piezas (`49` filas `R` mas `P1` y `P2`) |
| `docs/loop/REPORTE.md` seccion `2.d` (prosa, `TAREA 2` de `cap_05`) | *la enumeracion de los ocho mecanismos de la Parte II son capitulos por delante de este tramo* | **`cap_06` YA ES de este tramo**, y el primer mecanismo de esa lista (el codigo genetico del control) **lo mine yo mismo en la propia `TAREA 3` de esa vuelta** |

**LA FRONTERA EN SI NO ESTABA MAL** (`M3.4.a`): su suma cerraba al digito con las piezas `P` dentro,
que es lo que la guarda de frontera mide. Lo que estaba mal era el rotulo de cuantas piezas hay, y
eso es lo que esta correccion repara. No recompute yo mismo las `121` filas: cito la recomposicion del
auditor, que es el instrumento de esta casa para esa cifra (`EXTRACTOR.md` 5, la cita lleva su fecha
de la sesion que la corrio).

## 1.b. `PASOS INVENTADOS POR CAPITULO`, la cifra que la vuelta 2 no publico y el auditor firmo

*`ACTA M3` `M3.7.3`, salida pegada por el auditor de `.m2/aud/pasos_inventados_auditor.txt`.*

| capitulo | nodos | pasos escritos | PUENTE | PASOS INVENTADOS |
|---|---:|---:|---:|---:|
| `cap_04` | 1 | 5 | 0 | **0,00 por ciento** (0 / 5) |
| `cap_05` | 0 | 0 | 0 | **SIN SUPERFICIE** (0 / 0) |
| `cap_06` | 2 | 9 | 1 | **11,11 por ciento** (1 / 9) |
| EL TRAMO | 3 | 14 | 1 | **7,14 por ciento** (1 / 14) |

**LA FILA DE `cap_06` NO ES `0,00`**: el motivo es el paso `7` de
`aplicar_ejercicio_codigo_genetico_control`, adjudicado PUENTE por el auditor (`ACTA M3` `M3.7.2`)
contra `sed -n '113p' fuentes/marquet_turn_the_ship/cap_06.md`, y pagado en la `TAREA 2` de esta misma
vuelta. **`11,11` esta por encima del tope de `10,00` (`8.1`), asi que el freno de volumen se activa**
y el tramo de esta linea baja a **DOS** capitulos por vuelta (seccion 6).

## 1.c. El credito, leido y no tocado

    $ python forja.py credito
    CREDITO DE LA LINEA 'marquet_turn_the_ship' (D.48)
      registro: docs/loop/CREDITO_marquet_turn_the_ship.jsonl
      tandas: 1, en 5 suceso(s) de especie

      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA M3
      CIFRA PUBLICADA    0 de 2     ACTA M3
      CLASE              0 de 2     ACTA M3
      DATO MOVIDO        0 de 2     ACTA M3
      REPORTE            1 de 3     ACTA M3

      CREDITO ENTERO: ninguna especie en su tope.

**`REPORTE` esta en `1 de 3`, penultimo escalon.** Esta vuelta no anade una tanda de esa especie salvo
que algo de lo que publico caiga en la misma sede que la vuelta 2 (reporte parado, aduana afirmada sin
correr, tabla de discutibles vacia). Anoto la tanda de esta vuelta al cerrar, en la seccion 7.

## 1.d. La deuda, leida y NO pagada esta vuelta

*`docs/loop/DEUDA.jsonl`, filas `d094` a `d098`, anotadas por la `ACTA M3` el `2026-09-21 19:02:15`.*

| id | especie | que dice |
|---|---|---|
| `d094` | maquinaria | `forja.py herencia` entrega CERO remedios a esta linea porque lee `ACTA_AUDITOR.md` y la `ACTA M2` vive archivada; `D.45` impide arreglarlo desde un frente |
| `d095` | aduana | `forja.py informe` tarda `9` min `19` s por candidato con la poblacion en `449`; es el motivo mecanico de que dos aduanas se quedaran sin correr en la vuelta 2 |
| `d096` | maquinaria | `forja.py informe` no guarda su salida por su cuenta: hay que redirigirla a mano, y un turno que se acaba deja el fichero en cero bytes; tres ejemplares ya en este frente |
| `d097` | relectura | las `TAREA 2` y `TAREA 3` del reporte de la vuelta 1 siguen sin escribirse desde `.vm01/`, y la fila de `cap_03` sigue publicada en `0,00` |
| `d098` | aduana | el paso 1 de `ceder_control_reforzar_competencia_claridad` se reescribe o se retira antes de que ese nodo entre al grafo; hoy no vence porque el nodo sigue en bandeja |

**NO SE PAGAN ESTA VUELTA**, por instruccion expresa del encargo y porque el instrumento mismo dice
`LIBRE` (seccion apertura): `1 de 5` desde la vuelta 2, sin obligacion de saneamiento todavia.
---
