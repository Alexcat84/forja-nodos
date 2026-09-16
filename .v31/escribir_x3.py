# -*- coding: utf-8 -*-
import io

RUTA = "docs/loop/REPORTE.md"
s = io.open(RUTA, encoding="utf-8").read()


def sangrado(ruta):
    texto = io.open(ruta, encoding="utf-8").read().rstrip()
    return "\n".join(("    " + l) if l.strip() else "" for l in texto.split("\n"))


def solo_tabla(ruta):
    lineas = io.open(ruta, encoding="utf-8").read().rstrip().split("\n")
    return "\n".join(l for l in lineas if l.startswith("|")).strip()


nuevo = """## X.3. **TAREA 3**: la arista `D.29` que existe, que nadie juzgo y que hoy se cablea

**LA CLASE LA PONE EL AUDITOR Y YO LA EJECUTO** (`ACTA 29` `6.2`: *adjudicar no es medir, asi que la
clase la pongo yo y tu la ejecutas*). Lo que si es mio es comprobar que los dos extremos viven y que
el paso citado nombra al hijo, **antes** de cablear.

### X.3.a. LOS DOS EXTREMOS Y EL PASO CITADO, LEIDOS DEL DATO ANTES DE TOCAR NADA

<!-- TALLADO: parcial salida=.v31/extremos_t3.txt -->

    LOS DOS EXTREMOS, LEIDOS DE dataset/nodos.jsonl
      bloquear_tiempo_pensar_calendario          en el grafo: SI
      cuidarse_agotamiento_centro_rueda          en el grafo: SI

    === cuidarse_agotamiento_centro_rueda (7 pasos)
        paso  7: Bloquea en tu calendario tiempo de pensar todos los dias. El texto dice
                 que buena parte de esa dureza mental venia de hacer cosas como bloquear
                 dos horas de tiempo de pensar al dia.
        nodos_siguientes: []

    === bloquear_tiempo_pensar_calendario (6 pasos)
        paso  3: Agenda entonces algo de tiempo para pensar, y manten ese tiempo sagrado.
        paso  4: Hazle saber a la gente que no pueden agendar nada encima de el, nunca.
        paso  5: Enfadate de verdad, y en serio, si lo intentan.
        paso  6: Y anima a todos los de tu equipo a hacer lo mismo.
        nodos_previos   : []

**EL PASO `7` DE LA MADRE NOMBRA A LA HIJA EN UNA FRASE Y LA HIJA LA DESPLIEGA EN SEIS PASOS QUE LA
CABEZA NO TIENE.** Es la figura de `D.29` al pie de la letra.

### X.3.b. **ES `D.29` Y NO `D.37`, Y LO DIGO PORQUE LA DIFERENCIA CUESTA UNA RAZON ESCRITA**

`EXTRACTOR.md` 15.6, con la correccion del titular del 11 sep 2026: **la cuenta es condicion, no un
adorno del ejemplo.** *Si el texto solo enumera sin decir cuantas, esto NO es `D.37`: es `D.29`*, y
entonces la arista se declara igual **pero con razon escrita que la sostenga**, porque ahi si hay algo
que argumentar.

**LA MADRE NO DICE CUANTAS PARTES TIENE.** Su paso `7` manda bloquear el tiempo y se acaba ahi: no hay
*con sus seis vias* ni *los cuatro pasos*. **Asi que la razon la escribo yo y no me la ahorra
ninguna cuenta.**

### X.3.c. LA DECLARACION, CON SU SALIDA PEGADA (`EXTRACTOR.md` 15.6: *la cita se pega, no se promete*)

<!-- TALLADO: parcial salida=.v31/arista_t3.txt -->

""" + sangrado(".v31/arista_t3.txt") + """

> **Y LA LINEA QUE HACE VERIFICABLE LA ARISTA ES LA DE LAS SEIS SEÑALES QUE NO LA LEVANTAN**:
> `familia_id 0.0`, `paso_contra_nodo 0.407`, `similitud_texto 0.296`. **Las tres por debajo de su
> umbral** (`0,30`, `0,60` y `0,35`). **Es `D.19` con el numero delante:** la aduana levanto `5`
> vecinos para la hija y la madre no estaba entre ellos, asi que **no hubo veredicto que poner mal**,
> y por eso el auditor escribio en `7.2` que esto **no acumula contra mi**. La cazo su fase ciega
> leyendo.

### X.3.d. **COMPROBADA POR LOS DOS EXTREMOS EN EL DATO, NO POR LA PROSA DE LA SALIDA**

*Es lo que la vuelta 30 hizo bien en su `W.2.h` y el encargo me manda repetir.*

<!-- TALLADO: salida=.v31/arista_t3_comprobada.txt -->

""" + solo_tabla(".v31/arista_t3_comprobada.txt") + """

**Y LAS TRES CIFRAS DEL GRAFO SE MUEVEN LAS TRES, en el mismo acto:**

| | al abrir la vuelta (`X.0`) | **tras la `TAREA 3`** |
|---|---:|---:|
| aristas por `nodos_siguientes` | 92 | **93** |
| aristas por `nodos_previos` | 92 | **93** |
| lineas de `bitacora/VEREDICTOS.jsonl` | 375 | **376** |

**`+1` en las tres, que es lo que una arista declarada tiene que mover: los dos extremos y su razon.**
La linea nueva de la bitacora es la de esta declaracion, **y no pasa por `insertar`**, asi que no
aparecera en la tabla de la tanda de `X.4`.

"""

viejo = """## X.3. **TAREA 3**: la arista `D.29` que existe, que nadie juzgo y que hoy se cablea

PENDIENTE

"""
assert s.count(viejo) == 1
io.open(RUTA, "w", encoding="utf-8", newline="").write(s.replace(viejo, nuevo))
print("ok")
