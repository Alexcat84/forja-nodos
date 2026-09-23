# ENCARGO DE LA VUELTA 63: **LA PRIMERA TANDA DE INSERCION DE GROVE. `16` CANDIDATOS: `cap_02` ENTERO Y LOS `9` DE `cap_03` QUE ENTRAN**

*Linea **serial** (`extraccion-mundo-11`). **Escrito por la sesion de chat del 22 sep 2026**,
no por un auditor, al aplicar la decision del fundador `DOS SEMANAS` (punto `4`), archivada en
`docs/loop/paradas/2026-09-22-dos-semanas-DECISION.md`. La serial vuelve despues de dos dias
aparcada por cuota, y **el encargo de insercion lo escribe quien no adjudica**: una vuelta de
insercion decide veredictos, y el que mide no adjudica (manual principio `10`).*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**
> # **CLASE DE ESTA VUELTA: INSERCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. LO QUE CAMBIO MIENTRAS LA SERIAL ESTUVO PARADA, Y TE TOCA

| | |
|---|---|
| **regimen** | **COMPLETO**: `MODO_INSERCION=insertar`. **La fase ciega VUELVE**: en insercion el dato existe y se protege (`D.58`) |
| **modelos** | **`claude-opus-5-5` en los dos asientos, esfuerzo ALTO en los dos.** Es la unica fase que toca el grafo y la unica que no se deshace leyendo |
| **el mundo `11`** | **cierra con SIETE libros** (`D.60`, y el corte lo fijo el fundador el `22` sep). Faltan tres: `grove_high_output`, `gerber_emyth` y `marquet_turn_the_ship` |
| **gerber** | **COSECHADO el `22` sep** (fusion `95f6929`): sus `22` candidatos estan en `cuarentena/gerber_emyth/` y **van DESPUES de Grove** |
| **marquet** | **sigue extrayendo en su frente**, en otro arbol. **Tiene dueno: no lo toques** (`D.49`) |
| **el orden** | **Grove, despues Gerber, despues Marquet si cierra.** En tandas de hasta `20` por vuelta |

**Y LO QUE LLEGO A LA MAQUINARIA Y TE AFECTA:** `D.61` (un discutible publicado se ejecuta o se
cierra en la misma vuelta), el registro de credito que **ya no acepta una fila que se contradice
a si misma** (`src/credito.py`, `incoherencias`), y el tablero que lee el capitulo de un
candidato de su `UNIDAD DE ORIGEN` declarada.

---

## 1. TAREA `1`: **LA ADUANA, RECONCILIADA ANTES DE INSERTAR NADA**

La decision manda: *primero reconcilia los informes de aduana ya corridos y corre solo los que
falten*. **La reconciliacion esta hecha y publicada**, y no se rehace:

    docs/CIERRE_LOTE_7_GROVE.md          seccion 4
    .v63rec/veredictos_de_aduana.txt     los 91, uno por uno, con su veredicto, su poblacion y su fichero
    .v63rec/rec2.py                      el instrumento que la mide

    CON VEREDICTO DE ADUANA YA CORRIDO : 91
    SIN VEREDICTO, HAY QUE CORRERLOS   : 0

**POR ESA REGLA NO FALTA NINGUNO, asi que NO SE CORRE NINGUN INFORME PREVIO.** Y por eso esta
corrida va **sin informe de lote** (`INFORME_DE_LOTE` vacio): el arnes lo registra en su log, y
**es una decision, no un descuido**.

> ### **LA ADUANA QUE DECIDE SI UN CANDIDATO ENTRA ES LA DE `forja.py insertar`, Y ESA NO ES VIEJA**
>
> Todos los veredictos de la lista se corrieron contra poblaciones de `423` a `440`, y **hoy la
> poblacion es mayor**: entraron los `22` de Gerber. **No importa para entrar**, y conviene
> saber por que: `python forja.py insertar` **corre la aduana de ese candidato en el acto,
> contra el grafo y las bandejas de ESE momento.** Ningun candidato entra con un veredicto
> viejo. **La lista vieja sirve para ordenar la cola y prever cuantos bloquearan; no es la
> puerta.**

**Publica, al principio del reporte, la fila de la lista de cada uno de los `16` de esta tanda**
(su veredicto previo y su poblacion), y al lado **lo que `insertar` dijo HOY**. Si alguno cambia
de `ENTRARIA` a `BLOQUEARIA`, **eso es informacion, no un fallo**: es la poblacion nueva viendo un
vecino nuevo, y se lee como cualquier bloqueo.

---

## 2. TAREA `2`: **LA TANDA. `16` CANDIDATOS, POR ORDEN DE CAPITULO**

| capitulo | candidatos | entran hoy | por que |
|---|---:|---:|---|
| `cap_02` | `7` | **`7`** | el capitulo entero |
| `cap_03` | `15` | **`9`** | **`d005`**: su aduana en seco dijo `9` ENTRARIAN y `6` BLOQUEARIAN, y esos `6` **se reparan antes de insertarse y NO entran en esta vuelta** |
| **total** | | **`16`** | por debajo del tope de `20`, y **sin cortar un capitulo por la mitad** salvo el corte que `d005` ya declara |

**POR QUE NO SE LLENA HASTA `20` con cuatro de `cap_04`:** `cap_04` tiene `22` y no cabe entero;
partirlo en una vuelta y seguir en otra obliga a mantener su orden de lectura (`D.36`) a traves de
dos turnos. **Mejor una tanda de `16` limpia que una de `20` cortada.**

**Y LA VUELTA SIGUIENTE, LA `64`, ES DE SANEAMIENTO** por la cadencia de `D.58`, medida:

    $ python scripts/deuda.py --clase 63     LIBRE, van 4 de 5 desde la ultima de saneamiento (la 59)
    $ python scripts/deuda.py --clase 64     SANEAMIENTO

**Es el sitio natural para reparar los `6` de `d005`**, y conviene que el acta de esta vuelta lo
deje encargado asi.

### 2.a. **Lo que cada candidato lleva EN SU VUELTA DE INSERCION, y no es negociable**

1. **SU LECTURA DE FIDELIDAD ENTERA** (`D.30`): **todos sus pasos** contra el parrafo del libro del
   que dicen salir, **no una muestra**. En insercion no hay muestreo: es la ultima vez que alguien
   lee ese nodo antes de que viva en el grafo. **Un paso PUENTE no entra**: se retira con
   `scripts/retirar_paso.py` o se reescribe sin imperativo, y se declara.
2. **EL ORDEN QUE LEE** (`D.36`): **la madre antes que el hijo**. Si entra antes el hijo, en su
   veredicto no hay madre en el grafo contra la que declarar la arista.
3. **LAS SERIES POR TITULO** (`D.37`): si un texto nombra y cuenta sus partes y esas partes existen
   como nodos, la arista cabeza a parte se declara.
4. **VEREDICTO Y ARISTA SON PUERTAS DISTINTAS** (`D.53`): `src/arista.py` **no escribe una arista
   sin un veredicto con su cita**. Si la aduana bloquea, **lees a los vecinos y escribes el
   veredicto con su razon ANTES de insertar**.
5. **UNO POR VEZ**, con `python forja.py insertar`. **No existe la carga masiva.**
6. **Los veredictos a `bitacora/VEREDICTOS.jsonl` y los insertados a
   `cuarentena/_insertados/grove_high_output/`, en el mismo acto.**

> ### **EL RELOJ, MEDIDO Y NO PROMETIDO**
>
> El auditor del frente Marquet midio el `21` sep **`9` minutos y `19` segundos por informe con la
> poblacion en `449`**. Hoy es mayor. **Dieciseis candidatos son del orden de dos horas y media solo
> de aduana.** No es un techo: es para que sepas que no cabe correr y leer despues. **Y NUNCA des un
> candidato por insertado hasta que `insertar` haya vuelto**: el cerrojo (`D.44`) existe porque una
> insercion a medias perdio un nodo.

---

## 3. LO QUE NO HACES

- **NO TOCAS `cuarentena/gerber_emyth/`.** Va despues de Grove, y no en esta vuelta.
- **NO TOCAS LOS `6` DE `d005`.** Se reparan en la `64`.
- **NO ABRES `gerber_emyth_cap17_reservado`**, ni ningun libro nuevo. El mundo `11` cierra con
  siete.
- **NO FUNDES RAMAS.** La cosecha de Marquet la hace la sesion de chat cuando su frente cierre.

---

## 4. AL CERRAR

- **`PASOS INVENTADOS POR CAPITULO`**, una fila por capitulo, **sobre la lectura ENTERA**: `cap_02`
  y `cap_03`.
- **El censo antes y despues**: nodos del grafo, veredictos, pares mutuos, y bandeja de Grove.
  Hoy: **`346` nodos, `740` veredictos, `1` par mutuo, `91` en bandeja.** Si entran los `16`, la
  bandeja queda en `75` y el grafo en `362`.
- **Escribe tu tanda** en el credito: `python forja.py credito --anotar`, **con `cae` verdadero o
  falso**. Una tanda que no dice si cae **ya no se escribe**.
- **Repasa `D.61`** contra tu reporte: cada discutible ejecutado o cerrado. Ninguno abierto.
- **Commitea `docs/loop/` y tu carpeta de evidencia.** Si nada te obliga a parar, **no escribas
  `PARA_ALEXIS.md`**, y deja escrito el encargo de la `64`, **que es de SANEAMIENTO**.
