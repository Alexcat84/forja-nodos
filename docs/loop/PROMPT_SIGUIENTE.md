# ENCARGO DE LA VUELTA 1 DEL FRENTE `gerber_emyth`

*Frente de extraccion en paralelo (`D.45`). **Rama `extraccion-gerber_emyth`, carpeta
`../forja-gerber_emyth`.** Escrito por el fundador al abrir el paralelo el 16 sep 2026.*

> # **ESTE FRENTE NO INSERTA NUNCA.** `MODO_INSERCION=cuarentena`, siempre.
>
> Si alguien lanza este frente con `insertar`, **el arnes se detiene antes de gastar un
> turno** y nombra las dos ramas (`D.45`). No es una recomendacion: es codigo.

---

## LAS CUATRO REGLAS QUE MANDAN EN ESTE FRENTE

| | |
|---|---|
| **NO INSERTAS** | escribes candidatos en `cuarentena/gerber_emyth/` y los pasas por la aduana **EN SECO**, en el mismo acto en que los escribes |
| **MORATORIA DE MAQUINARIA Y DOCTRINA** (`D.45`) | **no tocas `src/`, ni el banco, ni el arnes, ni los protocolos.** Una pregunta de doctrina **es PARADA y sube al fundador**, aunque encuentres una caida de dato |
| **MODO AUSTERO** (`D.47`) | reporte y acta **encogidos**: nada que el registro ya diga, cifras talladas, **los discutibles por numero y linea**. **Lotes al techo de candidatos**, no por encima |
| **LAS GUARDAS DE DATO, INTACTAS** | la aduana entera, la fidelidad `D.30` con su relectura contra el parrafo, `D.41` y `D.42`. **El austero recorta tinta, no control** |

---

## EL LIBRO

| | |
|---|---:|
| clave | `gerber_emyth` |
| titulo | The E-Myth Revisited |
| autor | Michael E. Gerber |
| unidades en `fuentes/gerber_emyth/` | **22** |
| palabras | **63.434** |
| candidatos ya en bandeja | **0** |
| lugar en `ORDEN_DE_LOTES.md` | **9** |

**ABRE EL LIBRO.** La bandeja esta vacia. **Su `cap. 17` esta apartado a proposito** en `gerber_emyth_cap17_reservado` y **no entra en este frente** (`ORDEN_DE_LOTES.md`).

**La clave esta registrada en `fuentes/FUENTES_CANONICAS.json`**, asi que la guarda de
fuentes canonicas no te va a tumbar ningun candidato por ese motivo.

---

## TAREA 1. LA FRONTERA, ANTES DE CORTAR NADA

**Publica la frontera de la unidad que vayas a minar** y **cierrala contra el cuerpo**:
la suma de las filas tiene que dar el `wc -w` del cuerpo, con **cero lineas sin cubrir y
cero solapes**. **Si no cierra, no se publica ninguna cuenta de nodos.**

**LA TABLA VA PEGADA DE SU INSTRUMENTO** (`D.41`): guarda la salida en un fichero y
anexala de ahi. El hook la compara celda a celda en cada commit.

**Y NINGUNA CELDA TECLEADA DENTRO DEL INSTRUMENTO:** si una constante la pones tu leyendo,
**el instrumento lo dice en su primera linea de salida**. Es la caida de la vuelta 31 y no
hace falta repetirla.

## TAREA 2. MINAR, CON EL TECHO POR DELANTE

**El techo de candidatos por vuelta manda sobre el de capitulos** (`EXTRACTOR.md` 12.4):
**entre cinco y quince.** Si una unidad sola lo pasa, **la vuelta cierra en esa unidad y lo
declaras con su cifra.**

**Un candidato por vez y en el orden del libro.** Cada uno pasa por
`python forja.py informe <candidato>` **en el acto de escribirlo**, y el que caeria se
corrige y se reintenta.

**LAS ARISTAS QUE LA SEÑAL NO LEVANTA SE DECLARAN POR LECTURA** (`D.29`, `D.37`) **en la
misma vuelta en que escribes las partes**. Como este frente no inserta, **quedan escritas
en tu reporte con su razon**, y se cablean el dia de la insercion.

## TAREA 3. LA FIDELIDAD, ANTES DE CERRAR

**`PASOS INVENTADOS POR CAPITULO`** (`D.30`), fila por unidad mas total, **releyendo los
pasos contra su parrafo**. **La escalada se decide sobre el peor capitulo, no sobre el
promedio.** Tope **10**.

---

## AL CERRAR LA VUELTA

    python scripts/cerrar_reporte.py

**Y COMMITEA Y PUSHEA A TU RAMA**, `extraccion-gerber_emyth`. **No fundas nada**: la cosecha
la hace el fundador, una rama por vez, con el procedimiento de `docs/loop/PARALELO.md`.

## LO QUE ES PARADA EN ESTE FRENTE

- **una pregunta de doctrina**, cualquiera;
- **una caida de dato**, que se declara y **no se arregla aqui**;
- las de siempre de `AUDITOR_FORJA.md` 3.

**Y NO ES PARADA** que tu libro no tenga nada en comun con los otros frentes: **cada frente
mide su libro y nada mas.** Los vecinos entre libros los ve la insercion, que es la unica
que tiene el grafo entero delante.
