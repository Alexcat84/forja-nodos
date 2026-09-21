# -*- coding: utf-8 -*-
"""Anexa AA.3 y AA.4 al REPORTE, pegando las tablas de sus instrumentos (D.41)."""
import io

fid = io.open(".v2g/fidelidad_tanda.txt", encoding="utf-8").read().split("\n")


def bloque(nombre):
    i = [k for k, l in enumerate(fid) if l.startswith(nombre + "   ")][0]
    j = i
    while j + 1 < len(fid) and fid[j + 1].strip():
        j += 1
    return "\n".join("      " + l for l in fid[i:j + 1])


k0 = [k for k, l in enumerate(fid) if l.startswith("poblacion releida")][0]
saldo = "\n".join("      " + l for l in fid[k0:] if l.strip())

tabla = io.open(".v2g/pasos_inventados_v2g.txt", encoding="utf-8").read().split("\n")
t0 = [i for i, l in enumerate(tabla) if l.startswith("| capitulo")][0]
t1 = [i for i, l in enumerate(tabla) if l.startswith("| **total")][0]
tabla_md = "\n".join(tabla[t0:t1 + 1])
cierre = "\n".join("      " + l for l in tabla[t1 + 1:] if l.strip())

ar = io.open(".v2g/aristas_cola.txt", encoding="utf-8").read().split("\n")
a0 = [i for i, l in enumerate(ar) if l.startswith("| # | madre")][0]
afin = a0 + 1
while afin + 1 < len(ar) and ar[afin + 1].startswith("| "):
    afin += 1
aristas_md = "\n".join(ar[a0:afin + 1])
d0 = [i for i, l in enumerate(ar) if l.startswith("| par que considere")][0]
dfin = d0 + 1
while dfin + 1 < len(ar) and ar[dfin + 1].startswith("| "):
    dfin += 1
descartadas_md = "\n".join(ar[d0:dfin + 1])
recuento = "\n".join("      " + l for l in ar[dfin + 1:] if l.strip())

texto = u"""
> **EL REPORTE CRECE EN EL ORDEN EN QUE LAS TAREAS CIERRAN, NO EN EL ORDEN EN QUE ESTAN
> NUMERADAS** (`EXTRACTOR.md` 3: cada tarea anexa su fila al cerrarse). `AA.3` y `AA.4` cierran
> antes que `AA.2` y `AA.5` porque las dos de la aduana dependen de un instrumento que **sigue
> corriendo**: el informe de un solo candidato tardo **`610` segundos** en esta maquina. Se anexan
> ya para que una vuelta cortada deje reporte parcial y no vacio.

## AA.3. **TAREA 3**: LA FIDELIDAD `D.30`, PASO A PASO Y CON SU CITA PEGADA

**LOS `121` PASOS DE LOS `15` CANDIDATOS, RELEIDOS UNO A UNO CONTRA SU LINEA DEL LIBRO.** Ninguna
guarda de esta casa ve un paso que yo escribiera y el libro no diga: la aduana compara el candidato
con el grafo y consigo mismo, **no tiene el libro delante**. Esta seccion es lo que la aduana no
puede hacer.

### AA.3.a. UNA MUESTRA DE LA RELECTURA, PEGADA DEL INSTRUMENTO

<!-- TALLADO: parcial salida=.v2g/fidelidad_tanda.txt -->

    $ python .v2g/fidelidad.py   (2 de los 15 bloques)
%s

%s

**Y EL SALDO DE LA RELECTURA ENTERA, DEL MISMO INSTRUMENTO:**

<!-- TALLADO: parcial salida=.v2g/fidelidad_tanda.txt -->

%s

### AA.3.b. `PASOS INVENTADOS`, CON EL ROTULO DE LA POBLACION QUE MIDE

<!-- TALLADO: script=.v2g/pasos_inventados.py salida=.v2g/pasos_inventados_v2g.txt -->

%s

<!-- TALLADO: parcial salida=.v2g/pasos_inventados_v2g.txt -->

%s

**EL ROTULO ES LA MITAD DE LA CIFRA, Y ESTA VUELTA LO HEREDA COMO REMEDIO BLOQUEANTE.** `121` son
**los pasos de los 15 candidatos que esta vuelta escribio de `cap_03`**. No son los de la bandeja
del libro, que hoy tiene `23` ficheros porque arrastra los `8` de la vuelta 1; no son los del grafo;
y no son los del capitulo entero en ningun sentido que incluya lo ya insertado, porque **de este
libro no hay ni un nodo insertado**. Es exactamente la distincion cuya ausencia paro el bucle.

### AA.3.c. **LOS DOS PUENTES QUE ESCRIBI Y RETIRE EN EL ACTO**, que es lo que el cero no cuenta

Un `0` sin su historia no dice si hubo trabajo o si no hubo mirada, asi que los dos van con nombre:

| candidato | lo que iba a escribir | por que es puente | como quedo |
|---|---|---|---|
| `construir_indicador_linealidad_alerta_temprana` | *revisa el indicador de linealidad cada semana* | **especie PERIODO**. El libro no pone ritmo de lectura en ningun sitio del tramo: pone **un momento dentro de un ejemplo** (`by April`) y nada mas | el paso dice *lee a media carrera* y cita el abril del libro **como lo que es, el ejemplo** |
| `elegir_inspeccion_barrera_monitorizacion` | *fija de antemano cuando paras la linea* | el libro pone la condicion **como ejemplo** (`if, for example, three successive samples fail`), y *de antemano* era una obligacion que anadia yo | el paso dice *para la linea cuando el seguimiento lo pida*, con el ejemplo detras y sin volverlo norma |

**Y UNO MAS QUE NI SIQUIERA LLEGO A PASO**, y lo digo porque es el que mas me costo dejar fuera: en
`variar_frecuencia_inspeccion_nivel_calidad` iba a generalizar la salida que el libro da **para la
embajada** (*sustituye la comprobacion del cien por cien por un muestreo con criterios fijados de
antemano*) a cualquier proceso. **El libro lo dice de la embajada, no de cualquier proceso**, y
generalizar el caso es justo la senal barata del manual 3.5: *el entregable del caso lleva un dato
del caso*.

### AA.3.d. **EL AVISO DE `D.30` SOBRE EL PARRAFO POBRE, CONTRASTADO OTRA VEZ CONTRA MI TANDA**

`D.30` mide que el parrafo pobre produce el puente (el mas rico del lote 1 dio `0` por ciento y el
mas pobre `83`). **En mi tanda los dos parrafos mas pobres que dan nodo, `L89` con `94` palabras y
`L99` con `88`, dieron `0` puentes los dos.** Lo que si se cumplio es la otra mitad: **los dos
puentes que si escribi salieron de dos de los tramos mas largos de la unidad**, `L83` con `352`
palabras y `L141` con `356`.

> **LO QUE MI TANDA ANADE AL AVISO, y lo escribo como propuesta y no como regla** (`EXTRACTOR.md`
> 14, el extractor propone y no se adjudica): **el puente no aparecio donde el inventario era
> escaso, sino donde el inventario era TAN largo que yo estaba ordenandolo.** En `L141`, doce pasos
> seguidos salidos de un solo parrafo de `356` palabras, el puente fue una palabra de orden (*de
> antemano*) colada entre dos transcripciones buenas. **La pobreza del parrafo no es la unica puerta
> del puente: la abundancia que obliga a ordenar tambien lo es**, y esa no esta en la tabla de las
> tres especies. Es el segundo aviso seguido que este frente le pone a la misma regla, porque la
> vuelta 1 ya publico el suyo (la afirmacion en vez del encargo), y **dos avisos no son una
> correccion: son material para que el auditor decida si hay que medirlo.**

**`TAREA 3` CERRADA: `121` pasos, `0` puentes, `0,00` por ciento, contra un tope de escalada de `10`.**

## AA.4. **TAREA 4**: LAS ARISTAS QUE LEVANTA MI LECTURA Y NO LEVANTO NINGUNA SENAL (`D.29`, `EXTRACTOR.md` 11)

**SEIS DECLARADAS, TRES CONSIDERADAS Y RECHAZADAS, CERO CABLEADAS.** `forja.py arista` escribe en
`bitacora/` y en `dataset/`, y este frente no inserta (`D.45`). Quedan escritas con su razon y con
**el paso de la madre pegado de su propio fichero**.

<!-- TALLADO: script=.v2g/aristas.py salida=.v2g/aristas_cola.txt -->

%s

### AA.4.a. **LAS TRES QUE CONSIDERE Y NO DECLARO**, que valen tanto como las que si

**`EXTRACTOR.md` 15.6 lo dice al reves de como apetece leerlo:** *lo que no autoriza es declarar una
arista porque dos nodos compartan familia o tema*, y *una cabeza de seis vias y un vecino que no es
ninguna de las seis son hermanos*. Las tres siguientes comparten seccion, vocabulario y hasta verbo
con su pareja, **y ninguna tiene la linea que la sostenga**.

<!-- TALLADO: script=.v2g/aristas.py salida=.v2g/aristas_cola.txt -->

%s

<!-- TALLADO: parcial salida=.v2g/aristas_cola.txt -->

%s

**LA QUE MAS ME COSTO DEJAR FUERA ES LA PRIMERA**, y por eso la explico: el grafico escalonado esta
en la misma seccion que las otras dos ventanas, hace lo mismo que ellas y yo lo habria declarado sin
pensarlo. **Lo que lo tumba es una comprobacion de una linea:** `L83` dice literalmente
`a "window" cut into the black box` y `L89` dice `another window in our black box`; **`L91` no dice
ventana en ningun sitio.** Las dos que declaro llevan la palabra escrita y la tercera no, y esa es
toda la diferencia.

**`TAREA 4` CERRADA.**
""" % (bloque("construir_indicador_tendencia_patron"),
       bloque("archivar_indicadores_resolver_problemas"),
       saldo, tabla_md, cierre, aristas_md, descartadas_md, recuento)

with io.open("docs/loop/REPORTE.md", "a", encoding="utf-8", newline="\n") as f:
    f.write(texto)

s = io.open("docs/loop/REPORTE.md", encoding="utf-8").read()
s = s.replace(
    "| 3 | la fidelidad `D.30` paso a paso, `PASOS INVENTADOS` fila por unidad mas total | **ABIERTA** |",
    "| 3 | la fidelidad `D.30` paso a paso, `PASOS INVENTADOS` fila por unidad mas total | "
    "**CERRADA** en `AA.3`: `121` pasos releidos, `0` puentes, `0,00` por ciento, y los `2` que "
    "retire en el acto con nombre |")
s = s.replace(
    "| 4 | las aristas que levante mi lectura y no levanto ninguna senal | **ABIERTA** |",
    "| 4 | las aristas que levante mi lectura y no levanto ninguna senal | **CERRADA** en `AA.4`: "
    "`6` declaradas con el paso de la madre pegado, `3` consideradas y rechazadas con su motivo, "
    "`0` cableadas |")
io.open("docs/loop/REPORTE.md", "w", encoding="utf-8", newline="\n").write(s)
print("AA.3 y AA.4 ANEXADAS, filas 3 y 4 cerradas")
