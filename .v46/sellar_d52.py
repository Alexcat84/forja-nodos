# -*- coding: utf-8 -*-
"""Declara el instrumento de la tabla D.52 y escribe por que su fila 3 no publica N de M."""
import io

R = "docs/loop/REPORTE.md"
t = io.open(R, encoding="utf-8").read()

VIEJO = u"""### HH.5.g. **LA TABLA DE CIERRE DE TAREAS** (`D.52`)

| # | tarea | como cerro |"""

NUEVO = u"""### HH.5.g. **LA TABLA DE CIERRE DE TAREAS** (`D.52`)

*Salida de `python scripts/tabla_de_cierre.py --escribir`, pegada de
`docs/loop/TABLA_DE_CIERRE.txt`.*

> **POR QUE LA FILA `3` NO PUBLICA SU `N de M del capitulo`, Y LO DIGO EN VEZ DE ESCONDERLO.**
> La escribi asi en el primer tallado y el instrumento la puso en ROJO con esta salida, que pego
> tal cual antes de tocar nada:
>
>     filas             : 5
>     DIFIERE        3  la celda publica '8 de 22 del capitulo' y cap_04 son 0 de 0 en el grafo (0 pasos)
>     TABLA DE CIERRE EN ROJO: 1 fila(s) publican una cifra que el dato no da.
>
> **Y EL INSTRUMENTO TIENE RAZON, aunque mi cifra sea cierta:** `8 de 22` son **candidatos
> minados**, y la forma `N de M del capitulo` esta reservada a **nodos del grafo que citan ese
> capitulo**, que hoy son `0` porque esta vuelta **no inserta**. **No teclee la celda buena: le
> quite la forma que no me corresponde**, y la fila dice ahora *`8` candidatos de los `22` que da
> la frontera*. Es la misma correccion que la vuelta 42 escribio en `ED.8` para `cap_13`.

<!-- TALLADO: parcial salida=docs/loop/TABLA_DE_CIERRE.txt -->

| # | tarea | como cerro |"""

assert VIEJO in t
io.open(R, "w", encoding="utf-8", newline="\n").write(t.replace(VIEJO, NUEVO))
print("sellada")
