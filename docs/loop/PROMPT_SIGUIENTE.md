# ENCARGO DE LA VUELTA 46: **MINAR `grove_high_output` DESDE `cap_04`**

*Linea **serial** (`extraccion-mundo-11`). Escrito por la sesion de chat el 19 sep 2026,
**corrigiendo el encargo de la vuelta 45, que era mio y estaba mal.***

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO PRIMERO: **LA VUELTA 45 NO FALLO. TENIA RAZON, Y EL ENCARGO ESTABA MAL**

**Mi encargo te dijo `LA TAREA: INSERTAR de grove_high_output`. Era falso, y lo mediste
tu:**

    grove_high_output no esta en cerrados_en_extraccion de config/frentes.json,
    3 de 18 capitulos minados, y el cruce de bandejas contra esa lista da 0
    candidatos insertables en todo el arbol. Cero inserciones.

**`D.39` dice que solo entra un lote CERRADO EN EXTRACCION**, y que *los candidatos de un
lote ABIERTO siguen en cuarentena hasta que su lote cierre*. **Mediste la puerta, la
encontraste cerrada y te negaste, con las citas pegadas.** Eso es exactamente lo que se
espera de esta sede.

> **LO QUE YO LEI MAL:** `D.50` dice que la serial toma el libro *continuando desde el
> capitulo siguiente al ultimo minado, citando su frontera heredada*. **Eso es MINAR, no
> insertar.** Los `22` candidatos de grove **esperan en cuarentena hasta que el libro este
> minado entero**, y eso son `15` capitulos mas.

---

## Y LO SEGUNDO: **TU SELLO NO SE ACEPTO, Y LA CULPA ERA DEL CENSO**

Tu apertura ciega escribio, cumpliendo `D.57` al pie de la letra:

> *3. Si el reporte publica `.v45/informe_d021.txt` como prueba de una corrida. Mido que
> tiene `0` bytes; no puedo saber si esta publicada como ruta de evidencia.*

**El censo `D.42` leyo el nombre del fichero como una sede publicada y tumbo el sello.**
Cumpliste la regla de ayer y la guarda de anteayer te castigo por ello.

**ARREGLADO, Y NO POR TU LADO:** el censo tiene desde hoy **una cuarta forma**, que se
declara en la misma celda igual que las otras tres:

    NO ES SEDE: <motivo>

**Usala cuando nombres un fichero para decir que NO puedes comprobarlo.** La cifra es
SOBRE el fichero, no ESTA EN el, y eso no es publicar evidencia.

---

## LA TAREA: **MINAR `cap_04`, Y LA FRONTERA ANTES DE CORTAR**

    minados hasta hoy : cap_01 (1 candidato), cap_02 (7), cap_03 (15)
    el libro entero   : 18 unidades en fuentes/grove_high_output/
    el siguiente      : cap_04

**Los `23` que ya hay los mino OTRA MANO** (el frente `grove`, cosechado el 18 sep).

### 1. LA FRONTERA, ANTES DE CORTAR NADA

**Publica la frontera de `cap_04` y cierrala contra el cuerpo**: la suma de las filas tiene
que dar el `wc -w` del cuerpo, con **cero lineas sin cubrir y cero solapes**. **Si no
cierra, no se publica ninguna cuenta de nodos.**

**Y CITA LA FRONTERA HEREDADA** (`D.50`): la de `cap_03`, que cerro el frente al digito.
**No la recomputes: citala**, y di de donde sale.

**LA TABLA VA PEGADA DE SU INSTRUMENTO** (`D.41`), y el tallado la compara celda a celda.

### 2. MINAR, CON EL TECHO POR DELANTE

**Entre cinco y quince candidatos** (`EXTRACTOR.md` 12.4). Si `cap_04` solo da tres, cierras
en tres y lo declaras con su cifra; si pasa de quince, **la vuelta cierra en esa unidad**.

- **Un candidato por vez y en el orden del libro.**
- **Cada uno pasa por `python forja.py informe <candidato>` en el acto de escribirlo**, y
  el que caeria se corrige y se reintenta.
- **CERO INSERCIONES.** El lote 7 esta ABIERTO: `D.39` no deja entrar nada hasta que
  cierre. **Los candidatos van a `cuarentena/grove_high_output/` y ahi se quedan.**
- **Las aristas que la señal no levanta se declaran por lectura** (`D.29`) **con su razon
  escrita**, y **se cablean el dia de la insercion**, no hoy.

### 3. LA FIDELIDAD, ANTES DE CERRAR

**`PASOS INVENTADOS` de `cap_04`** (`D.30`), releyendo los pasos contra su parrafo. **La
escalada se decide sobre el peor capitulo.** Tope `10`.

---

## LO QUE NO ES TAREA TUYA ESTA VUELTA

| | |
|---|---|
| **la deuda** | `9` pendientes en `docs/loop/DEUDA.jsonl`. **No la pagues hoy**: se paga junta en una vuelta de saneamiento (`D.55`) |
| **los `6` de `d005`** | son de `cap_03` y se reparan antes de insertar, **no antes de minar `cap_04`** |
| **la doctrina** | congelada en `11`. Si encuentras una pregunta nueva, **registrala con su medida y dejala ahi** |

> **LO UNICO QUE TE BLOQUEA ES UNA GUARDA DE DATO EN ROJO**: `gate`, el cerrojo, el censo
> no decreciente, o la fidelidad `D.30` con puente. **Eso no es deuda: es averia.**

## AL CERRAR

    python forja.py gate
    python forja.py guiones
    python tests/test_aceptacion.py
    python scripts/cerrar_reporte.py
    python scripts/tabla_de_cierre.py --escribir      y se pega su salida
    python forja.py tablero --escribir
    python forja.py credito                           lo lees; NO anotes tu propia vuelta

**Y ESCRIBE LA LINEA DEL TRAMO, sea cual sea el numero, incluido `0`.**

**Si un turno tuyo pasa de `10` USD y la vuelta no es de saneamiento, el acta lo declara
con el desglose de en que se fue** (`D.55`).

## LO QUE NO SE TOCA

- **El banco no gana reglas nuevas** salvo que una guarda de DATO lo exija con su cita.
- **`config/frentes.json` y `config/umbrales.json`** se leen, no se editan.
- **El bucle no funde ramas y el bucle no crea remotos.**
