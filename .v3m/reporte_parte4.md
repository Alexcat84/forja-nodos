# TAREA 4. `cap_06` SE RELEE ENTERO CONTRA SUS 51 FILAS ANTES DE ABRIR `cap_07` (`D.58`)

*Disparador: la muestra de `cap_06` dio `11,11` por ciento de pasos inventados, por encima del `10` por
ciento (seccion 1.b). Por ser barato (la frontera de `51` piezas ya esta publicada y verificada al
digito por el auditor, `ACTA M3` `M3.4`), lo que se relee son sus `9` pasos escritos contra sus `51`
filas, no el capitulo desde cero.*

    $ sed -n '8,139p' fuentes/marquet_turn_the_ship/cap_06.md    (las 132 lineas del cuerpo, leidas enteras)

## 4.a. Las `49` filas `R`: ninguna era nodo

Releida la frontera fila a fila contra el fichero (seccion 3.b de la vuelta 2, `ACTA M3` `M3.4`
verificada al digito con `121` filas y `0` discrepancias sobre las tres unidades del tramo), **ninguna
de las `49` filas `R` de `cap_06` es procedimiento**. Los dos tramos que el encargo pide revisar por su
nombre:

| tramo | contenido | por que no es nodo |
|---|---|---|
| `L83` a `L95` (`R33` a `R39`) | el caso de Santa Fe: los jefes quieren estar a cargo de las licencias, el cambio de una palabra de XO a COB, el alcance del cambio ("Chiefs in Charge"), la delegacion simetrica de las licencias de oficiales al XO | **CASO**: es el origen narrativo del que Marquet generaliza el ejercicio de `P1` y el mecanismo de `P2`; ninguna de estas siete lineas trae su propio inventario de etapas, son la historia concreta de una nave, con sus cargos y su cifra (`de catorce pasos a ocho`) que no se repite en ninguna otra organizacion |
| `L115` a `L125` (`R41` a `R45`) | el cierre del mecanismo: "FIND THE GENETIC CODE AND REWRITE IT is a mechanism for CONTROL", la clarity organizacional como barrera, por que los programas de empoderamiento dirigido fracasan, la sintesis de que se buscaron practicas y no discursos | **POSTURA**: es la reflexion del autor sobre por que el mecanismo funciona, sin ningun medio, etapa u objeto de trabajo nombrado que no este ya en `P1`; `D.27` cae del lado de la postura por ausencia de inventario propio, no por adjetivo de adecuacion |

    $ sed -n '83,95p;115,125p' fuentes/marquet_turn_the_ship/cap_06.md | wc -l
    13

Las `13` lineas de contenido (siete del primer tramo, seis del segundo, contando solo las lineas con
texto) confirman lo ya publicado en la frontera de la vuelta 2: **CASO** y **POSTURA**, respectivamente,
sin ningun paso propio que extraer. Releidas las otras `36` filas `R` restantes contra la misma
frontera, ninguna cambia de clase: el reparto entero sigue siendo `40` `CASO`, `8` `POSTURA` y `1`
`PENDIENTE DE DOCTRINA` repartido en cuatro preguntas de cierre (contando cada rotulo y separador como
`RESIDUO`, ya clasificados en la tabla original).

## 4.b. Los `8` pasos que sobreviven: TRANSCRIPCION uno a uno, tras pagar el puente

*Tras la `TAREA 2`, `aplicar_ejercicio_codigo_genetico_control` tiene `6` pasos (no `7`) y
`asignar_responsable_unico_evolucion_planificada` sigue con `2`. El total del capitulo baja de `9` a
`8` pasos escritos.*

| paso | linea | la salida de `sed`, pegada | veredicto |
|---|---|---|---|
| P1.1 | L101 | `Identify in the organization's policy documents where decision-making authority is specified. (You can do this ahead of time if you want.)` | TRANSCRIPCION |
| P1.2 | L103 | `Identify decisions that are candidates for being pushed to the next lower level in the organization.` | TRANSCRIPCION |
| P1.3 | L105 | `For the easiest decisions, first draft language that changes the person who will have decision-making authority. In some cases, large decisions may need to...` | TRANSCRIPCION |
| P1.4 | L107 | `Next, ask each participant in the group to complete the following sentence on the five-by-eight card provided: "When I think about delegating this decisio...` | TRANSCRIPCION |
| P1.5 | L109 | `Post those cards on the wall, go on a long break, and let the group mill around the comments posted on the wall.` | TRANSCRIPCION |
| P1.6 | L111 | `Last, when the group reconvenes, sort and rank the worries and begin to attack them.` | TRANSCRIPCION |
| P2.1 | L127 | `...The mechanism was to add a line to our planning documents that listed the "Chief in Charge" next to each event.` | TRANSCRIPCION |
| P2.2 | L127 | `I learned that focusing on who was put in charge was more important than trying to evaluate all the ways the event could go wrong.` | TRANSCRIPCION |

**LOS `8` PASOS SON TRANSCRIPCION, `0` PUENTE.** El unico paso que no sobrevivio a la relectura (el
`7` de `aplicar_ejercicio`, `L113`) ya salio del campo en la `TAREA 2`.

## 4.c. `PASOS INVENTADOS` de `cap_06`, publicado otra vez tras la relectura

| capitulo | nodos | pasos escritos | PUENTE | PASOS INVENTADOS |
|---|---:|---:|---:|---:|
| `cap_06` (antes de la `TAREA 2`, `ACTA M3` `M3.7.3`) | 2 | 9 | 1 | 11,11 por ciento (1 / 9) |
| `cap_06` (tras pagar el puente y releer sus `51` filas) | 2 | 8 | 0 | **0,00 por ciento (0 / 8)** |

**BAJA A `0,00`, Y SE DICE:** el freno de `8.1` que se activo en la seccion 1.b sigue siendo el hecho
de la vuelta 2 (el tramo con el que corrio, tres capitulos, sigue siendo el que produjo el `11,11` de
entonces), pero el estado de `cap_06` HOY, con su puente pagado, es `0` de `8`. **Las dos cifras se
publican las dos**, por `EXTRACTOR.md` 4: la de ayer no se corrige por la de hoy, se cita como lo que
era antes de la correccion.
---
