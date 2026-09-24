# ENCARGO DE LA VUELTA 67: **LA RELECTURA CONJUNTA DE DOS PARES Y UNA ARISTA DE `cap_04`, Y DESPUES LAS `20` PRIMERAS FILAS DE SU ORDEN DENTRO, UNA POR VEZ**

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 65`, que audito la vuelta `66`.
`AUDITOR_FORJA.md` seccion `1.4`.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: INSERCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **LA REGLA DEL TURNO, Y EL METODO QUE LA `ACTA 65` TE SOSTUVO**

> **UN `insertar` POR VEZ, Y NINGUNO EN VUELO CUANDO TU TURNO TERMINE.** Cada candidato entra entero o no entra.
> **Al volver cada `insertar`: su fila en el reporte, commit y push.**

**El metodo de la `65` y la `66` vale** (`ACTA 65` `65.4.a`, `D66.1` sostenido): cada `insertar` lanzado como un proceso por
una copia de `.v66ext/insertar.py`, y tu bloqueado en primer plano con una copia de `.v66ext/esperar.py` hasta su `.fin`,
**sin lanzar el siguiente ni tocar el dataset ni la bandeja en medio**. **NO LANZAS NADA EN SEGUNDO PLANO QUE SIGA VIVO AL
CERRAR TU TURNO.** Si algo no te cabe, no lo lances: lo dices en el reporte con lo que falta.

**EL RELOJ, MEDIDO:** la `65` metio `20` filas en `30381` s de turno, `27644` de ellos de aduana; la `66`, de `1271` a `1637` s
por `insertar` contra poblacion `479`. **No son techos: son lo que costo.**

## LA CLASE Y EL LIBRO, DICHOS POR EL INSTRUMENTO

    $ python scripts/deuda.py --clase 67
    LIBRE
      van 3 de 5 desde la ultima de saneamiento (la 64), con 57 deuda(s) esperando

    $ python forja.py tablero --puedo grove_high_output
    LINEA 'serial', LIBRO 'grove_high_output': SI
      'grove_high_output' esta COSECHADO y sin dueño: su trabajo ya llego a esta rama, asi que se continua desde el capitulo siguiente al ultimo minado (cap_18), citando su frontera. D.50.

(Las `57` son de antes de que la `ACTA 65` anotara `d168`.) **El orden de la campania es Grove, Gerber, Marquet** (`PARALELO.md`
`8` punto `4`). **La frase de *continuar desde `cap_18`* es de extraccion y no aplica: Grove esta minado entero**, y lo que se
hace es insertar su bandeja por capitulo (`d028`).

---

## TAREA 1: **REGISTROS DE LA `ACTA 65`**

En una tabla corta y sin reabrir el argumento (`D.47`):

| que | donde |
|---|---|
| **Tus ocho discutibles de fidelidad y de metodo se sostienen**, `D66.1` a `D66.7`: `cap_04` queda en `0` de `156`, firmado. `D66.8`, `D66.10` y `D66.11` coinciden con la ciega del auditor y se sostienen | `ACTA 65` `65.4.a` y `65.4.b` |
| **`decir_no` con `usar_calendario`: SANO, gana tu lectura**, y tu orden queda como esta | `65.4.b` |
| **Dos pares y una arista van a relectura conjunta**: es tu TAREA 2 | `65.4.b` |
| **Una caida de `REPORTE` que no acumula**: en `66.2` la frase de la fila `22` es la linea `7` de su salida y no la `6` | `65.2` |
| **`R5` cumplido**, las cinco rachas de la serial en cero, y **el cierre estricto vuelve a verde**: la apertura de la `66` no tiene tablas, asi que **en la `67` un rojo del cierre estricto es tuyo** | `65.1`, `65.2`, `65.7` |

## TAREA 2: **LA RELECTURA CONJUNTA** (`AUDITOR_FORJA.md` `1.3`), **ANTES DEL PRIMER `insertar`**

El caso del auditor, con su evidencia, esta en la `ACTA 65` `65.4.b`, en la tabla de las cuatro discrepancias. **Tu verificas
contra el grafo y la bandeja y decides con la vara `6.1`, y solo esa.** Imprime primero los pasos de los dos
(`python .v64aud/pasos.py <a> <b>`), lee su caso, y decide:

| | par | tu linea hoy | la del auditor |
|---|---|---|---|
| `C1` | `subir_productividad_gerencial_tres_vias` con `buscar_actividad_alta_palanca_tres_vias` (tu `D66.9`) | `SANO` en los dos bloques | `CONTINUA`, madre `subir` |
| `C2` | `buscar_actividad_alta_palanca_tres_vias` con `elegir_momento_actividad_palanca_maxima` | `SANO` en los dos bloques | `CONTINUA`, madre `buscar` |
| `C3` | arista por lectura `buscar_actividad_alta_palanca_tres_vias` a `detectar_palanca_negativa_actividad_mando` | **sin fila**: tu lectura no miro el par | `SOSTENGO` |

1. **En `C1` hay una tension que tienes que resolver por escrito**, porque tu razon usa `EXTRACTOR.md` `9.1` restriccion `1`
   y la restriccion `3` de ese mismo `9.1` dice que no mueve la vara de continua contra repite: **si las tres vias de `subir`
   son metas, `subir` no pasa `9.1`; si son medios, `buscar` despliega el segundo.** Si decides que son metas, `subir` no entra
   en esta tanda, **se queda en la bandeja con su razon escrita y se dice**: no se borra nada.
2. **Lo que decidas se escribe por correccion declarada, sin borrar el texto viejo**: si una linea de
   `.v66ext/veredictos_listos.txt` cambia, la vieja queda encima como comentario `#` con la vuelta y el motivo; si `C3` se
   sostiene, su fila va en `.v66ext/aristas_lectura.txt` con su tramo de madre y de hijo y su linea del libro, y si no, su fila
   `NO SOSTENGO` con la razon. **Si dudas, marcalo discutible.**
3. **Despues, vuelve a correr las copias** `.v66ext/comprobar_veredictos.py` y `.v66ext/orden.py`, y pega las dos salidas: cero
   vecinos sin linea, cero lineas sin vecino y **las tres comprobaciones del orden en cero**. `subir`, `buscar`, `elegir` y
   `detectar` son las filas `6` a `9`, asi que madre antes que hijo se cumple se decida lo que se decida; **si el orden cambia
   por lo que sea, se dice con su salida delante.**

## TAREA 3: **LO QUE ENTRA ES LO QUE SE LEYO**

Antes del primer `insertar`, con una copia de `.v66ext/pasos_y_huellas.py` con la lista cambiada a las filas `1` a `20` de
`.v66ext/orden.txt` y el commit cambiado a `d8f4e2a` (el cierre de la `66`: sobre esas fichas se leyo la fidelidad entera, se
barrio y se escribieron los veredictos, y ninguna cambio en la vuelta, `ACTA 65` `65.4.a`): **las `20` fichas de la bandeja
iguales a su blob en `d8f4e2a`.** Si una sale distinta, no entra, se relee entera contra `cap_04` y se dice.

## TAREA 4: **LAS `20` PRIMERAS FILAS DEL ORDEN DE `cap_04`, UNA POR VEZ**

**En el orden de `.v66ext/orden.txt`** tal como quede tras la TAREA 2, **filas `1` a `20`**;
`agrupar_interrupciones_subordinados_reuniones_regulares` y `canalizar_interrupciones_cartel_hora_oficina` pasan a la `68`.

1. **Las lineas `--veredicto` son las del bloque de cada candidato en `.v66ext/veredictos_listos.txt`, tal cual**, las que la
   TAREA 2 haya corregido incluidas. Las `CONTINUA` con `madre=` cablean su arista en el acto: `reunir` a `escalonar` en la fila
   `2`, y **`detectar_arreglar_fallo_etapa_menor_valor` a `supervisar_tarea_delegada_etapa_menor_valor` en la fila `11`**, que es
   la arista EN COLA de la `65`.
2. **Las aristas por lectura, con `python forja.py arista` en el acto de insertar el hijo**, con `--veredicto CONTINUA`, su cita y
   su `--paso` dentro del tramo de su fila, como la `65` (`D65.2`, `D65.3`). **Son siete en esta tanda**, mas `C3` si se sostiene:
   `construir_flujo_produccion_paso_limitante` a `identificar_paso_limitante_jornada_desfases` (fila `13`, **es `d072`**: al
   cablearla la pagas con `python scripts/deuda.py --pagar d072 --vuelta 67 --como "..."`, citando su commit);
   `transmitir_objetivos_prioridades_preferencias` a `delegar_tarea_base_comun_seguimiento` (fila `10`);
   `delegar_tarea_base_comun_seguimiento` a `supervisar_tarea_delegada_etapa_menor_valor` (fila `11`);
   `variar_frecuencia_inspeccion_nivel_calidad` a `supervisar_tarea_delegada_etapa_menor_valor` (fila `11`);
   `delegar_tarea_base_comun_seguimiento` a `supervisar_decision_delegada_preguntas_concretas` (fila `12`);
   `identificar_paso_limitante_jornada_desfases` a `usar_calendario_herramienta_planificacion_produccion` (fila `16`); y
   `representar_actividad_caja_negra_ventanas` a `buscar_regularidad_bloques_iguales_trabajo_mando` (fila `18`). **Las dos de
   `agrupar_interrupciones` y `canalizar` son de la `68`.**
3. **La puerta es la aduana de `insertar`, no la lista** (`d031`). Si levanta un vecino sin linea, lo lees con los pasos de los
   dos delante, escribes su veredicto por la vara `6.1` y solo esa, **y lo marcas en el reporte como lectura tuya de esta
   vuelta**, discutible si dudas. Si levanta `CAERIA` o un error, no fuerces: no entra, y se declara.
4. **Al volver cada `insertar`, su fila en el reporte** como las de la `66`: la aduana de hoy con sus vecinos, las lineas que
   pasaste, las aristas que cableaste y su commit. Cada insertado a `cuarentena/_insertados/grove_high_output/` (`D.31`).

## TAREA 5: **EL CIERRE**

- **El censo antes y despues**: nodos, veredictos, pares mutuos, bandeja de Grove e insertados. Si entran las `20`, el grafo
  queda en `388`, la bandeja en `49` y `_insertados` en `43`.
- **Las aristas de la tanda, contadas por instrumento**: cuantas se esperaban, cuantas viven en el grafo y ninguna sin adjudicar.
- **`PASOS INVENTADOS POR CAPITULO`, una fila por capitulo, de lo que ENTRO**: `cap_04`, contado desde `.v66ext/fidelidad.tsv`,
  que la `ACTA 65` `65.5` firmo en `0` de `156`, no a ojo.
- **`D.61`**: cada discutible ejecutado o cerrado. Ninguno abierto.
- **`R5`** en cada bloque `$` de tu tramo, medido con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` con la
  cabecera cambiada a la `67`, y pegado.
- `python forja.py gate`, `python forja.py guiones`, `python tests/test_aceptacion.py` y `python scripts/cerrar_reporte.py`,
  **pegados**. **El cierre estricto tiene que salir en verde: cualquier rojo es tuyo.**
- Commitea `docs/loop/`, `dataset/`, `bitacora/`, `censos/`, los movidos a `_insertados`, las correcciones de la TAREA 2 y tu
  carpeta `.v67ext/`. **Si nada te obliga a parar, no escribas `PARA_ALEXIS.md`.**

---

## LO QUE NO HACES

- **NO LANZAS NADA EN SEGUNDO PLANO QUE TOQUE EL DATASET**, y **NO TERMINAS TU TURNO CON NADA VIVO**, ni un `insertar` ni un
  barrido.
- **NO INSERTAS `agrupar_interrupciones` NI `canalizar`**: son de la `68`, con sus dos aristas.
- **NO TOCAS `cuarentena/gerber_emyth/` NI `cuarentena/marquet_turn_the_ship/`**: van despues de Grove, en ese orden.
- **NO TOCAS `src/`, `scripts/`, el banco, el arnes ni los protocolos** (`7.F`, `D.55`), **ni `APERTURA_CIEGA.md`**.
- **NO REORDENAS LA COLA A MANO.**
- **NO ABRES NINGUN LIBRO.** El mundo `11` cierra con siete.

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla vigente, paras y lo traes. No
adivines.**
