# -*- coding: utf-8 -*-
import io

RUTA = "docs/loop/REPORTE.md"
s = io.open(RUTA, encoding="utf-8").read()


def pegar(ruta, desde=None):
    lineas = io.open(ruta, encoding="utf-8").read().rstrip().split("\n")
    if desde is not None:
        for numero, linea in enumerate(lineas):
            if linea.startswith(desde):
                lineas = lineas[numero:]
                break
    return "\n".join(lineas).strip()


nuevo = """## X.4. **TAREA 4**: seguir insertando el lote 4 por `cap_11` y por el orden del libro

### X.4.a. **EL ORDEN DE LA TANDA, GENERADO DEL PROPIO DATO Y NO TECLEADO** (`D.36`, `EXTRACTOR.md` 12.3)

`.v31/orden.py` lee el rango de `cap_11.md` del `resumen_teorico` de cada fichero de la bandeja y
ordena por el. **Es la tabla del instrumento entera, no un resumen suyo:**

<!-- TALLADO: script=.v31/orden.py salida=.v31/orden_cap11.txt -->

""" + pegar(".v31/orden_cap11.txt", "| # |") + """

> ### **Y LA PRIMERA CORRIDA ME DIO `0` CANDIDATOS, QUE ES EL MOTIVO POR EL QUE EL ORDEN SE GENERA Y NO SE TECLEA**
>
> **Copie el instrumento de la vuelta 30 cambiando `cap_07` por `cap_11` y salio la tabla vacia.**
> No es que no hubiera candidatos: **es que `cap_11` no escribe el rango como lo escribia `cap_07`.**
>
>     cap_07:  fuentes/.../cap_07.md, lineas 231 a 293
>     cap_11:  fuentes/.../cap_11.md, unidad Cap. 8, Results. Sale de las lineas 15 a 35
>
> **Si esta tabla se tecleara, el error no habria existido y tampoco existiria la comprobacion.** Es
> `D.41` por su cara buena: **un instrumento que se equivoca lo dice; una celda tecleada, no.**

**Y EL QUE NOMBRA `cap_11` SIN SALIR DE EL, que el instrumento separa en vez de colarlo:**
`integrar_peticion_critica_rutina_existente` **es de `cap_13`** (`Afterword`, `L235`), y cita `cap_11`
dentro de un veredicto sobre `montar_reuniones_solas_mentalidad_frecuencia`. **No entra en esta tanda
porque no es de este capitulo.**

**EL HUECO ENTRE `L157` Y `L175` NO ES UN HUECO:** es `THINK TIME` (`L165` a `L173`), y de ahi salio
`bloquear_tiempo_pensar_calendario`, **que ya vive en el grafo desde la vuelta 30** y que hoy ha
recibido su madre en `X.3`.

### X.4.b. **LA RELECTURA DE FIDELIDAD, HECHA ANTES DE LA PRIMERA INSERCION** (`D.30`, `EXTRACTOR.md` 15.4)

> **NINGUNA GUARDA DE ESTA CASA VE UN PASO QUE TU ESCRIBISTE Y EL LIBRO NO DICE.**

**LEI LOS `142` PASOS DE LOS ONCE CONTRA SU PARRAFO, NO UNA MUESTRA.** El libro reabierto con
`.v31/leer.py`, que imprime el rango con su numero de linea delante, y **cada paso marcado
`TRANSCRIPCION` o `PUENTE`**. Los rangos leidos de `fuentes/scott_radical_candor/cap_11.md`:
`L15` a `L65`, `L67` a `L157`, `L159` a `L173` y `L175` a `L233`.

**Y LOS LEI ANTES DE LA PRIMERA INSERCION, no despues**, que es lo que `15.4` manda con esas
palabras: *en el mismo acto, no en una vuelta posterior*.

#### **`PASOS INVENTADOS POR CAPITULO`, QUE ES LA CIFRA QUE YO DOY Y EL AUDITOR FIRMA** (`AUDITOR_FORJA.md` 8.3)

<!-- TALLADO: script=.v31/pasos_inventados.py salida=.v31/pasos_inventados_v31.txt -->

""" + pegar(".v31/pasos_inventados_v31.txt") + """

**EL DENOMINADOR SALE DEL DATO**: `.v31/pasos_inventados.py` cuenta `pasos_accionables` fichero a
fichero. **EL NUMERADOR LO PONGO YO LEYENDO**, porque ninguna maquina lo puede poner.

#### **LOS CINCO PASOS QUE MIRE DOS VECES, CON SU LINEA PEGADA** (`D.35`)

<!-- TALLADO: script=.v31/cita.py salida=.v31/citas_fidelidad.txt -->

""" + pegar(".v31/citas_fidelidad.txt") + """

> **`LECTURA`: el `0,00` no dice que el capitulo sea facil, y digo donde estuvo el filo.**
>
> **`cap_11` es el capitulo mas rico en inventario propio de todo el lote**, y eso es exactamente lo
> que `D.27` predice: *el parrafo mas rico del lote dio `0` por ciento de puentes; el mas pobre dio
> `83`*. Aqui el libro pone **listas enteras**: diez rotulos uno por linea (`L17` a `L35`), quince
> preguntas literales (`L71` a `L97`), seis mas (`L103` a `L113`), cinco seniales con su nombre
> (`L119` a `L127`), tres bloques con sus minutos (`L139` a `L143`). **Escribir los pasos es
> transcribir el inventario, y no se inventa nada.**
>
> **EL UNICO SITIO DONDE MIRE DOS VECES fue `escribir_apuntes_sala_estudio_equipo` paso `10`**, que
> dice *el texto nombra los sitios donde vale hacerlo* **sin nombrarlos**, cuando `L155` los nombra
> los tres. **Lo marco `TRANSCRIPCION` y digo el criterio, porque el criterio es lo que se puede
> discutir: un `PUENTE` es un paso que dice lo que el libro NO dice, y este dice MENOS.** Va a mis
> discutibles (`X.6`).
>
> **Y EL SEGUNDO SITIO, que digo aunque salga a favor:** `pelear_proliferacion` paso `7` manda
> bloquear tiempo **sin escribir las dos horas**, y las dos horas estan en `L171`, dentro del caso del
> CEO. **Es la regla del caso cumplida por su lado dificil** (`EXTRACTOR.md` 9: *el entregable del
> caso lleva un dato del caso* es la senial barata de que se hizo mal). El auditor de la `ACTA 29`
> midio que el nodo hermano de `cap_07` si escribio las dos horas y por eso las leyo como puente;
> **este no las escribe.**

**Y EL FRENO DE VOLUMEN NO SE ACTIVA**: `0,00` esta por debajo del tope de `10`. **Lo que manda hoy es
el reloj de la aduana**, y vuelvo a el al cerrar la tanda.

### X.4.c. **EL TRAMO, DECLARADO ANTES DE INSERTAR Y CON SU CIFRA** (`EXTRACTOR.md` 12.4, `4.c` del encargo)

| | |
|---|---:|
| candidatos de `cap_11` en bandeja | **14** |
| **tramo de esta vuelta** | **11**, del `1` al `11` del orden del libro |
| pasos del tramo | **142** |
| lo que queda de `cap_11` para la vuelta siguiente | **3** (`montar_tablero_kanban_medir_actividades`, `pasear_organizacion_hallar_problemas_pequenios`, `debatir_decidir_asuntos_cultura_evitar_delegar`) |

**POR QUE `11` Y NO `14`, con la cifra que el encargo me manda dar:**

    $ (una sola corrida en seco de la aduana, cronometrada hoy)
      python forja.py informe cuarentena/scott_radical_candor/decidir_quien_comunica_cada_cuanto.json
      real  1m48.965s          poblacion del barrido: 348   (256 del grafo mas 92 en bandejas)

**`109` segundos por corrida, y cada candidato pide DOS** (una para leer su cola de vecinos y otra
para insertarlo con el veredicto escrito): **unos `220` segundos por candidato.** Once candidatos son
**unos `40` minutos solo de aduana**, y ese es el techo que cabe con las otras cuatro tareas dentro.
**`14` serian `51`.**

**Y EL CORTE NO ES ARBITRARIO: el `11` es `pelear_proliferacion_reuniones_bloquear_ejecucion`**, que
es el que el encargo marca con fecha de caducidad en su `4.d`. **El tramo se corta justo despues de la
obligacion que no se puede aplazar, no antes.**

> **EL TRAMO NO SUBE, como el encargo manda.** La vuelta 30 hizo `13`; esta hace `11`. **Lo que baja
> no es la fidelidad** (`0,00` por ciento las dos veces) **sino el peso: `142` pasos contra `90`.**

"""

viejo = """## X.4. **TAREA 4**: seguir insertando el lote 4 por `cap_11` y por el orden del libro

PENDIENTE

"""
assert s.count(viejo) == 1
io.open(RUTA, "w", encoding="utf-8", newline="").write(s.replace(viejo, nuevo))
print("ok")
