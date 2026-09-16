# ENCARGO DE LA VUELTA 30: **SEGUIR INSERTANDO `cap_07`**, CON EL CERROJO Y EL TESTIGO YA PUESTOS

*Escrito por el **auditor** al cerrar la **ACTA 28** y reescrito con la decision del
fundador del 16 sep 2026, archivada en
`docs/loop/paradas/2026-09-16-el-cerrojo-y-el-testigo-DECISION.md`. Sede del auditor por
`AUDITOR_FORJA.md` 5.6.*

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO QUE LA DECISION DEJA HECHO, ANTES DE QUE EMPIECES

- **PRIMERO SE MIRO EL DATO, Y EL DATO ESTABA ENTERO.** El nodo que la vuelta 28 perdio
  **esta en el grafo** (`crear_obligacion_disentir_equipo`, commit `32fa203`, `21` lineas
  en la bitacora), y **ningun commit de esta casa ha perdido nunca un nodo**: el censo de
  los `27` commits del dataset **solo sube, de `222` a `243`**. La perdida vivio **en el
  arbol de trabajo** y el extractor la reparo antes de commitear. **No habia nada que
  restaurar, y se dice con la medida en vez de con una ceremonia.**
- **YA EXISTE EL CERROJO DE INSERCION** (`src/cerrojo.py`). **Dos `insertar` a la vez ya no
  se pisan**: el segundo **espera**, y si no puede, **no escribe nada**.
- **YA EXISTE `D.44`, EL CENSO NO DECRECE.** Si un nodo del commit anterior falta en el
  arbol sin estar `deprecado`, **el gate cae nombrandolo**. Antes salia verde.
- **YA EXISTE EL TESTIGO DE GUARDAS AL SELLAR** (`D.45`). **Una cifra vale en el instante
  del sello.** Es del auditor, pero te lo digo porque el arnes puede detenerse ahi.
- **EL CENSO Y EL TALLADO LEEN TAMBIEN `APERTURA_CIEGA.md`**, que era la unica sede de
  cifra que ninguna guarda leia.

---

## TAREA 1: **SEGUIR INSERTANDO `cap_07`, QUE ES DONDE SE PARO**

| | |
|---|---:|
| bandeja del lote 4 | **102** de 142 |
| ya insertados | **40**, el **28** por ciento |
| nodos en el grafo | **243** |
| veredictos en bitacora | **289**, de ellos **14** declarados NO CONSUMADOS |

**DONDE SE PARO:** en `centrar_debate_ideas_fuera_egos`. **El orden del libro esta en la
`ACTA 28` `4.1`, fila a fila**, y quedan **`12` candidatos** con **`77` pares** de cola de
lectura, **`50` de los `77` con un extremo en bandeja**.

> ### **Y LA CABEZA DE LA RUEDA VA POR DELANTE DE SUS PARTES**
>
> `recorrer_rueda_hacer_cosas_equipo` **antes** que sus partes: si entran antes que la
> cabeza, **sus aristas `D.37` no las va a poder cablear la aduana.**

**UN CANDIDATO POR VEZ, Y AHORA LO CUMPLE EL CODIGO.** Si lanzas dos, **el segundo espera**
y te lo dice en su salida. **No lo fuerces:** eso es exactamente lo que perdio un nodo con
el gate en verde.

---

## TAREA 2: **EL PAR DEL CALENDARIO, QUE NINGUNA SEÑAL CRUZA**

`bloquear_tiempo_pensar_calendario` (`cap_11`) contra `agendar_cuidados_propios_cumplirlos`
(`cap_08`). **Los dos en bandeja, de capitulos distintos, y el barrido del auditor no los
cruza ni una vez en `77` lineas.** Ya esta adjudicado **`SANO`** (`ACTA 28` `6.10`).

> **La vuelta que inserte al primero lo lee contra el segundo y escribe su veredicto por
> lectura** (`D.29`, `D.19`). **No esperes a que una señal lo levante: no lo va a hacer.**

---

## TAREA 3: **LA COLA QUE SIGUE ABIERTA, PARA QUE NO SE PIERDA**

*Va entera porque ya se perdio una vez: el remedio de la fase ciega cazo que siete de ocho
encargos de la `ACTA 25` no llegaron al encargo siguiente.*

| lo que queda | cifra |
|---|---|
| la arista en cola `crear_espacio_seguro_madurar_ideas_nuevas > nutrir_ideas_nuevas_reunion_solas` | **1**, la desbloquea que entre el hijo |
| la serie `D.37` de `minimizar_impuesto_colaboracion_equipo` | **3** partes, **ninguna vive** |
| la mitad `Burnout` de la serie de `aprender_resultados_vencer_dos_presiones` | **1**, falta `cuidarse_agotamiento_centro_rueda` |
| el hueco de transcripcion de `L153` | **1** modo de `3`, en `1` nodo. **Sin via, y con un solo ejemplar no se construye** |
| las entradillas de `LISTEN`, `CLARIFY` y `DEBATE` de `cap_07`, con texto y sin nodo | **3** tramos. **No es caida de nadie: es cola** |
| las `8` lineas `SIN HUELLA` | **8**. `D.15` da dos salidas, **releerlas o declararlas**, y hoy no hay ninguna hecha |
| `cap_04` releido antes que las tres filas de hueco | **6** candidatos, **48** pasos |
| la frontera por capitulo con las `QUESTIONS TO CONSIDER` | **14** de **17** unidades |
| el lote 5 por su orden | **3** candidatos. **No se toca hasta que el 4 cierre** (`D.39`) |

---

## LO QUE MANDA EN COMO ESCRIBES

**`D.41`** (la tabla se anexa desde su fichero), **`D.42`** (toda ruta publicada como sede
sostiene su cifra) y **`D.38.3` ensanchada** (la frase es la del instrumento, y la
conclusion sobre contenido va en linea aparte marcada `LECTURA`).

**Y DESDE HOY, `D.45`:** una cifra vale **en el instante del sello**. Si al cerrar tu turno
una guarda esta en rojo, **lo que publicaste sobre el estado ya no vale**, aunque fuera
cierto cuando lo mediste. **Deja el arbol limpio antes de cerrar.**

**Al cerrar la vuelta:** `python scripts/cerrar_reporte.py`.

## SON TRES TAREAS Y EL TOPE SON CINCO

**Si la insercion se come la vuelta, la vuelta se cierra ahi y lo declaras con su cifra.**
El lote 4 va por el `28` por ciento: **lo que cierra un lote es insertarlo entero.**
