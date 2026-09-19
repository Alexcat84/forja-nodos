# ENCARGO DE LA VUELTA 45: **VUELTA DE INSERCION, LOTE 7 (`grove_high_output`)**

*Linea **serial** (`extraccion-mundo-11`), la unica que inserta. Escrito al aplicar la
decision del fundador del 18 sep 2026, archivada en
`docs/loop/paradas/2026-09-18-arista-py-y-la-ciega-sin-registro-DECISION.md`.*

> # **LIBRO DE ESTA VUELTA: `grove_high_output`**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## **ESTA ES UNA VUELTA DE INSERCION** (`D.55`)

**ABRE SIN UNA SOLA TAREA DE REPARACION.** Tu trabajo es meter candidatos por la aduana.

**NO tienes tarea bloqueante.** Lo que hay que reparar esta en `docs/loop/DEUDA.jsonl` con
su cita, y se paga junto en una vuelta de saneamiento.

    python scripts/deuda.py        lo pendiente, y que clase de vuelta toca

**LO UNICO QUE TE BLOQUEA ES UNA GUARDA DE DATO EN ROJO**: `gate`, el cerrojo, el censo no
decreciente, o la fidelidad `D.30` con puente. **Eso no es deuda: es averia.**

---

## LO QUE CAMBIO BAJO TUS PIES MIENTRAS NO CORRIAS, Y TE AFECTA AL ESCRIBIR

| | |
|---|---|
| **`D.53` YA ESTA EN EL CODIGO** | `forja.py arista` **exige** `--veredicto` y `--cita-veredicto`. **Ya no teclea `CONTINUA`**: el veredicto lo emite TU lectura y viaja con su cita |
| **las `93` lineas viejas, re adjudicadas** | `1` era `CONTINUA` de verdad, `13` eran `SANO` y **`79` no tenian ninguna lectura detras**: quedaron en `SIN LECTURA PROPIA`. No las toques |
| **`D.57`, la ciega sabe que no ve** | `loop.log` **ya no se retira** en la fase ciega, y el prompt del ciego trae su linea de `retirados:`. **Si no puedes comprobar algo, escribe la limitacion, no la afirmacion** |
| **tu racha propia vuelve a `0 de 3`** | por decision escrita del fundador, **con esa condicion mecanica puesta**. Lo lees con `python forja.py credito` y lo citas |

> ### **COMO SE DECLARA UNA ARISTA DESDE HOY**
>
>     python forja.py arista --madre <id> --hijo <id> --paso <n> \
>            --razon "que añade el hijo a la madre" \
>            --veredicto SANO|CONTINUA|REPITE \
>            --cita-veredicto "de donde sale esa lectura"
>
> **El veredicto es el de TU lectura del par, no el de la arista.** Un `SANO` puede llevar
> arista declarada: si no pudiera, **toda cabeza de serie devoraria sus partes y `D.37`
> seria imposible.**

---

## LA TAREA: **INSERTAR DE `grove_high_output`, Y LEER LA DEUDA ANTES DE ELEGIR**

    $ python .v45/estado.py
    poblacion: el arbol entero, sin filtrar
    dataset/nodos.jsonl                      : 346 nodos
    bitacora/VEREDICTOS.jsonl                : 740 lineas
    cuarentena/grove_high_output             : 22
    cuarentena/_insertados/grove_high_output : 1
    la bandeja de grove por capitulo         : cap_02 7, cap_03 15

**`1` de `23` dentro. Quedan `22`, y los mino otra mano.**

> **`d005` DE LA DEUDA DECIDE CUALES NO ENTRAN HOY:** *de los `15` candidatos de `cap_03`
> de grove, su aduana en seco dijo `9` ENTRARIAN y `6` BLOQUEARIAN: esos `6` se reparan
> antes de insertarse.* **Leela entera antes de elegir**, y **nombra los seis** en tu
> reporte.

- **El techo de esta vuelta es `15` candidatos** (`EXTRACTOR.md` 12.4). Si la bandeja util
  se acaba antes, cierras ahi y lo declaras.
- **Un candidato por vez y en el orden del libro.** El orden no lo eliges tu: lo elige el
  libro, y el primero que entra cambia lo que el segundo mide.
- **Las aristas `D.29` se cablean en el mismo acto en que entra su nodo**, con el paso de
  la madre citado **y su `--veredicto` con su cita**.
- **La seccion de la insercion crece UNA FILA CADA VEZ QUE UNO ENTRA, en su propio commit.**

### LO QUE SIGUE SIENDO OBLIGATORIO, PORQUE ES GUARDA DE DATO

| | |
|---|---|
| **la fidelidad `D.30`** | **ANTES de la primera insercion**, y **vale doble**: estos pasos los escribio otra mano |
| **el cerrojo** | una sola corrida escribe el dataset. `INSERCION NO INTENTADA` significa que hay otra viva: **no la esquives** |
| **el censo y el tallado** | corren en cada commit y no se negocian |

### EL METODO, CON LA MEDIDA DE LA VUELTA 42 DELANTE

> **NINGUNA CORRIDA SOBREVIVE A TU TURNO.** Esperala bloqueado hasta leer su codigo de
> salida, sin avanzar al siguiente y sin hacer nada en medio. **Y si tu arnes no puede
> esperar tanto en una sola llamada, dilo con la medida al lado.**

## AL CERRAR

    python forja.py gate
    python forja.py guiones
    python tests/test_aceptacion.py
    python scripts/cerrar_reporte.py
    python scripts/tabla_de_cierre.py --escribir      y se pega su salida
    python forja.py tablero --escribir
    python forja.py credito                           lo lees; NO anotes tu propia vuelta

**Y ESCRIBE LA LINEA DEL TRAMO, sea cual sea el numero, incluido `0`:**

> *la vuelta cierra en el candidato `N` de `M`; los que quedaban pasan a la vuelta
> siguiente.*

**Si un turno tuyo pasa de `10` USD y la vuelta no es de saneamiento, el acta lo declara
con el desglose de en que se fue** (`D.55`).

## LO QUE NO SE TOCA

- **El banco no gana reglas nuevas** salvo que una guarda de DATO lo exija con su cita.
  **La cola de doctrina sigue congelada en `11`.**
- **`config/frentes.json` y `config/umbrales.json`** se leen, no se editan.
- **El bucle no funde ramas y el bucle no crea remotos.**
