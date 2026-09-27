# -*- coding: utf-8 -*-
"""Abre la seccion DC.6 (la insercion) ANTES de que entre el primer candidato."""
import io

bloque = u"""
## DC.6. **LA SECCION DE LA INSERCION, ABIERTA ANTES DE QUE ENTRE EL PRIMER CANDIDATO** (`TAREA 4`)

**Se abre aqui, con el grafo todavia en `324` nodos y `507` lineas de bitacora, y crece UNA FILA CADA VEZ
QUE UNO ENTRA**, en su propio commit y con el candidato ya dentro. **Si el reloj me corta en el `2`, lo
que falta es una linea y no una seccion**, que es lo que costo la racha `REPORTE` dos vueltas seguidas.

**EL PREFIJO ES `DC` Y ES ELECCION MIA**, con la salida del `grep` pegada en `DC.1`: la serie va `AA`,
`AB`, `AC`, `BC`, `CC`, y `CC` es la vuelta 39. **La seccion es la `.6`, que es lo que el encargo compra.**

**LAS CUATRO COSAS QUE YA ESTAN HECHAS ANTES DE ESTA LINEA, y por eso la insercion puede empezar:**

| | |
|---|---|
| la fidelidad `D.30` de los `58` pasos | **`DC.5`: `58` `TRANSCRIPCION`, `0` `PUENTE`** |
| mis discutibles marcados a ciegas | **`DC.5.e`: `9`, escritos antes de que entre nada** |
| la caida de dato de la `TAREA 1.A` | **`DC.2`: corregida por anexion, barrido a `4` y `4`** |
| los `2` rancios que son pares de candidatos de hoy | **`DC.3`: releidos por medicion; la anotacion baja en el acto de cada entrada** |

### DC.6.a. **EL ORDEN, Y POR QUE ES ESE** (`D.36`, `EXTRACTOR.md` 12.3)

**El orden del libro, que es el que manda**, y el primero que entra cambia lo que el segundo mide:

| # | candidato | rotulo y linea | pasos | lo que trae escrito |
|---:|---|---|---:|---|
| `1` | `abrazar_incomodidad_silencio_contar_seis` | `EMBRACE THE DISCOMFORT`, `L187` | `12` | arista `D.37` en cola, linea `489`; rancio `484` que anotar |
| `2` | `escuchar_entender_critica_dominar_defensa` | `LISTEN WITH THE INTENT TO UNDERSTAND`, `L199` | `13` | arista `D.37` en cola, linea `492`; rancio `485` que anotar |
| `3` | `premiar_franqueza_hacer_escucha_tangible` | `MAKE LISTENING TANGIBLE`, `L215` | `20` | arista `D.37` en cola, linea `495`. **Con el cierra la serie** |
| `4` | `integrar_peticion_critica_rutina_existente` | `BUILD IT INTO YOUR EXISTING SCHEDULE`, `L235` | `13` | `SANO` ya razonado en `488` y en `500`. **No es parte de la serie** |

### DC.6.b. **LO QUE `D.37` CIERRA CON EL CANDIDATO `3`, ESCRITO ANTES DE SABER SI LLEGO** (`TAREA 3.A`)

`L113` escribe *each of the four tips for soliciting criticism offered in the book* y **`L237` los nombra
uno a uno**. `elegir_pregunta_recurrente_pedir_critica` entro en la vuelta 39 y es **el primero de los
cuatro**. **Cuando entren los candidatos `1`, `2` y `3`, las CUATRO partes de la serie estan en el grafo
con sus CUATRO aristas cableadas desde la cabeza**, y la serie deja de estar a medias, que es su estado
fragil. **La frase con su cifra se vuelve a escribir en `DC.6.f` cuando el `3` este dentro, y no antes.**

### DC.6.c. **LOS DOS QUE NO ENTRAN HOY, Y NO LOS DECLARO CERRADOS** (`TAREA 3.C`)

`dar_elogio_disciplina_igual_critica` (`20` pasos, arista `49`, linea `490`) y
`medir_critica_respuesta_oyente_brujula` (`33` pasos, arista `51`, linea `494`) **siguen en bandeja con su
arista en cola**. **No los toco.** `cap_13` **queda con `2`** si los cuatro entran. **No estiro el tramo
a seis**, y el motivo esta medido en el encargo: `896` segundos de media por insercion.

### DC.6.d. **LAS FILAS, UNA POR CANDIDATO, CADA UNA CON SU CANDIDATO YA DENTRO**
"""

with io.open('docs/loop/REPORTE.md', 'a', encoding='utf-8') as f:
    f.write(bloque)
print('OK, DC.6 abierta')
