# ENCARGO DE LA VUELTA 64: **SANEAMIENTO QUE DESBLOQUEA LA INSERCION DE GROVE. `d005`, `d140` Y `d141`, CON LOS VEREDICTOS ESCRITOS Y LISTOS, Y SIN INSERTAR NADA**

*Linea **serial** (`extraccion-mundo-11`). Escrito por el auditor al cerrar la `ACTA 62`, que audito
la vuelta `63`. `AUDITOR_FORJA.md` seccion `1.4`.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: SANEAMIENTO**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. **LA REGLA DEL TURNO VA PRIMERO, PORQUE ES LO QUE TUMBO LA `63`**

**La vuelta `63` no inserto ni un nodo.** Su extractor lanzo `insertar` en segundo plano y **cerro su
turno a los `880` s** con este mensaje final: *Both background jobs are still running; I'll pick up as
soon as the insertion 1 result lands.* **Nadie lo recogio** (`ACTA 62` `62.2`).

> **NINGUN PROCESO TUYO VIVE CUANDO TU TURNO TERMINA.** Si lanzas algo en paralelo, lo recoges dentro
> del turno, vigilandolo si tarda. **Si algo no cabe, NO lo lances: dilo en el reporte.**

**En esta vuelta no se corre `python forja.py insertar` ni una vez.** El cerrojo huerfano de la `63`
(`procesos/nodos.jsonl.679b2259.cerrojo`) **no se toca**: lo rompe y lo declara el primer `insertar`
de la `65` (`D.44`).

---

## LA CLASE Y EL LIBRO, DICHOS POR EL INSTRUMENTO

    $ python scripts/deuda.py --clase 64
    SANEAMIENTO
      han pasado 5 vuelta(s) desde la ultima de saneamiento (la 59) y la cadencia es 5, con 54 deuda(s) pendientes

    $ python forja.py tablero --puedo grove_high_output
    LINEA 'serial', LIBRO 'grove_high_output': SI
      'grove_high_output' esta COSECHADO y sin dueño: su trabajo ya llego a esta rama, asi que se continua desde el capitulo siguiente al ultimo minado (cap_18), citando su frontera. D.50.

**Las `54` son las `52` que habia al abrir mi turno mas `d140` y `d141`, que anote yo.** Grove no tiene
capitulo siguiente que minar: lo que le queda es insertar. La guarda del
tablero no deja que esta vuelta se declare de otra clase (`D.58`). **Se usa para pagar justo lo que
frena la insercion de Grove**, y la insercion vuelve en la `65` con los veredictos ya escritos.

---

## TAREA 1: **REGISTROS DE LA `ACTA 62`**

Recoge en tu reporte, en una tabla corta y sin reabrir el argumento (`D.47`):

| que | donde |
|---|---|
| **`D1` CAE, dentro del marcado**: los `4` pasos de `equilibrar` con *y apunta su coste* cuentan como PUENTE por el ejemplar de `D.30` (los `13` de `36` del lote `1` son `4` retirados y `9` clausulas reescritas). **`cap_02` queda en `4` de `50`, `8,0` por ciento**; `cap_03` en `0` de `80` | `ACTA 62` `62.5` y `62.6` |
| *el ultimo commit que los toca es del `16` sep* es falso para `5` de `16` (`4` del `18`, `1` del `19`); la conclusion sigue en pie. Prosa, no acumula | `62.3` |
| `R5` sigue vivo **con su letra**: si cortas un bloque `$`, **por el final y dentro del bloque** `(recortado, entero en <fichero>)` | `62.4`, `62.13` |
| **`REPORTE` baja a `0 de 3`** | `62.9` |

## TAREA 2: **`d005`, LOS SEIS DE `cap_03` QUE NO ENTRARON: FIDELIDAD ENTERA Y VEREDICTOS LISTOS**

**Los seis, por su id** (el alcance es este y ningun otro):

    archivar_indicadores_resolver_problemas
    construir_grafico_escalonado_pronosticos
    construir_indicador_tendencia_patron
    elegir_fabricar_pedido_pronostico
    elegir_indicador_salida_trabajo_administrativo
    emparejar_indicadores_efecto_contraefecto

**2.a. SU LECTURA DE FIDELIDAD ENTERA (`D.30`)**, cada paso contra la linea de `cap_03` de la que dice
salir, **todos, sin muestra**. Cada PUENTE se retira o se reescribe con su `CORRECCION DECLARADA de la
vuelta 64` y el texto viejo dentro, como hizo la `63`. **Una clausula reescrita CUENTA como paso
PUENTE en la metrica** (`ACTA 62` `62.5`): corregirla es la regla funcionando, no que deje de contar.

**2.b. SUS VECINOS YA ESTAN MEDIDOS, Y NO SE VUELVEN A MEDIR.** La fase ciega anulada de la `63` corrio
los seis informes contra **poblacion `462`**, y los dejo en
`docs/loop/archivo/interrumpidas/2026-09-23-v63-fase-ciega-2/v63ciega/informe_<id>.txt`. **El
instrumento que los resume es `.v63aud/vecinos_d005.py`, y su salida de hoy esta guardada entera en
`.v63aud/vecinos_d005.txt`**, con el control de determinismo al pie: `15` de `15` informes identicos
linea a linea entre el archivo y mi fase sellada. **Los seis bloquean**, sobre todo entre si, mas
cuatro vecinos de fuera (`ACTA 62` `62.7`).

**Por cada candidato, un bloque titulado `VEREDICTOS LISTOS DE <id>`** con una linea por vecino en el
formato exacto de `--veredicto` (`src/aduana.py`, `parsear_veredicto`):

    vecino|CONTINUA|madre=<id>|razon con el paso de cada lado
    vecino|SANO|razon
    vecino|REPITE|razon

**Leyendo los pasos de los dos delante y por la vara `6.1` de `AUDITOR_FORJA.md`, y solo esa.** La senial
dijo donde mirar y ahi acabo su trabajo (`D.19`).

**2.c. SI UNA CORRECCION DE 2.a CAMBIA UNA FICHA, SU SENIAL SE MUEVE** (`d031`, medido otra vez en la
`63`: cuatro de dieciseis cambiaron de veredicto). **No re corras el informe entero**: mide cada par de
esa ficha con `aduana.medir` (segundos por par) y **declara si alguno deja de levantar**. Un veredicto
escrito sobre un vecino que la senial ya no levanta **se dice**, no se esconde.

## TAREA 3: **`d140`, LOS NUEVE BLOQUEARIA DE LA TANDA DE LA `63`: VEREDICTOS LISTOS**

**El alcance, con su instrumento:** los `16` de la `63` tienen hoy informe en
`.v63aud/informe_<id>.txt` (poblacion `462`, `23` sep). **Los nueve que bloquean** los lista
`.v63aud/veredictos462.txt`, que sale de `python .v63aud/vecinos.py`, y son:

    construir_flujo_produccion_paso_limitante         clasificar_trabajo_proceso_montaje_prueba
    rehacer_flujo_paso_limitante_capacidad            preferir_inspeccion_proceso_prueba_destructiva
    dimensionar_inventario_materia_prima_reposicion   detectar_arreglar_fallo_etapa_menor_valor
    decidir_aceptar_rechazar_material_defectuoso      dimensionar_plantilla_administrativa_pronostico
    simplificar_trabajo_reducir_numero_pasos

**Lo mismo que en 2.b**: un bloque `VEREDICTOS LISTOS DE <id>` por candidato, una linea por vecino. **Los
de `detectar_arreglar_fallo...` ya estan escritos** en `.v63ext/cmd_02_detectar.sh` por el extractor de
la `63`, y la `ACTA 62` `62.5` los sostiene: **reutilizalos citandolos**, no los reescribas.

> **LA RELECTURA CONJUNTA (`1.3`), EN SU ORDEN:** **escribe primero tu lectura**, y solo despues abre la
> de mi apertura sellada de la `63` (`git show 53e573e:docs/loop/APERTURA_CIEGA.md`, secciones `5.1` y
> `5.2`). **Publica una tabla con cada par donde discrepemos**, con la linea del libro de cada lado.
> Decides tu con la vara y lo declaras; **no te pido que me des la razon**.

## TAREA 4: **`d141` Y EL ORDEN DE `cap_02` Y `cap_03` PARA LA `65`**

**`d141`:** mi lectura ciega dice que `dimensionar_plantilla_administrativa_pronostico` y
`casar_flujo_fabricacion_flujo_ventas` son **hijos por lectura** de candidatos de `d005` (`cap_03` L111,
L121 y L125), con pares que la senial **no levanta en ningun sentido**. **Leelos tu con los pasos de los
dos delante** y escribe cada par que sostengas en un bloque titulado `ARISTAS POR LECTURA (D.29)`, con
madre, hijo, la linea del libro y la razon. **Y los que no sostengas, tambien**, con su motivo: un
discutible se ejecuta o se cierra en la misma vuelta (`D.61`).

**EL ORDEN:** publica una tabla con los `22` candidatos de `cap_02` y `cap_03` (**`7` mas `15`**) en el
orden en que entrarian, **madre antes que hijo** (encargo de la `63`, punto `2.a.2`, escrito bajo la
decision del fundador) y respetando las series de `D.37`. Por fila: id, capitulo, su madre si la tiene,
**su informe vigente con su poblacion** (`.v63aud/` o el archivo de la fase `2`), y si sus veredictos
estan listos. **Propon la tanda de la `65`** (tope `20`, `DOS SEMANAS` punto `4`) **sin dejar un hijo
delante de su madre**. **Proponer no es fijar**: el orden lo fija quien autoriza (`D.36`), y lo recoge el
encargo de la `65`.

## TAREA 5: **EL CIERRE**

- **Declara la vuelta de saneamiento en el registro**, que se olvido en la `49` y en la `59` (`d085`):

      python scripts/deuda.py --saneamiento --vuelta 64

- **Paga solo lo que pagaste**, con `python scripts/deuda.py --pagar <id> --vuelta 64 --como "..."`:
  `d005` si los seis tienen fidelidad leida y veredictos listos; `d140` si los nueve los tienen; `d141`
  si los pares estan escritos o cerrados y la tabla del orden publicada. **Lo que quede a medias se
  queda pendiente y se dice.**
- **`PASOS INVENTADOS POR CAPITULO`** de los seis de `d005` (todos de `cap_03`), una fila, **con los pasos
  contados por un instrumento y no a ojo**.
- **`D.61`**: cada discutible, ejecutado o cerrado. Ninguno abierto.
- **`R5`** en cada bloque `$` de tu reporte.
- `python forja.py gate`, `python forja.py guiones`, `python tests/test_aceptacion.py` y
  `python scripts/cerrar_reporte.py`, **en verde y pegados**.
- **El censo antes y despues** tiene que salir igual, porque esta vuelta no inserta: **`346` nodos, `740`
  veredictos, `1` par mutuo, `91` en la bandeja de Grove.**
- Commitea `docs/loop/`, las seis fichas si las corregiste, y tu carpeta `.v64ext/`. **Si nada te obliga a
  parar, no escribas `PARA_ALEXIS.md`.**

---

## LO QUE NO HACES

- **NO INSERTAS.** Ni un `insertar`, ni un veredicto en `bitacora/`, ni una arista en el dataset.
- **NO TOCAS `cuarentena/gerber_emyth/`** ni el frente `marquet_turn_the_ship`, que tiene dueno (`D.49`).
- **NO TOCAS `src/`, el banco, el arnes ni los protocolos** mientras corra el frente de Marquet (`D.45`).
- **NO ABRES NINGUN LIBRO.** El mundo `11` cierra con siete y la campania con el tag
  `primer-equipo-completo` (decision del fundador del `24` sep).

---

**Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.**
