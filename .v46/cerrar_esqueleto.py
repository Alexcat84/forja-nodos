# -*- coding: utf-8 -*-
"""Cierra las cinco filas del esqueleto de la vuelta 46, que se abrieron vacias."""
import io

R = "docs/loop/REPORTE.md"
t = io.open(R, encoding="utf-8").read()

PARES = [
    (u"| `HH.1` | los registros de la `ACTA 44`: `d021` y `d023` por correccion declarada, "
     u"`d024` y la doctrina `D.55` dichas | |",
     u"| `HH.1` | los registros de la `ACTA 44`: `d021` y `d023` por correccion declarada, "
     u"`d024` y la doctrina `D.55` dichas | **CERRADA en `HH.1`**: las tres patas reparadas "
     u"y **registradas** |"),
    (u"| `HH.2` | la frontera de `cap_04` cerrada contra el cuerpo, y la heredada de `cap_03` "
     u"citada por su sede | |",
     u"| `HH.2` | la frontera de `cap_04` cerrada contra el cuerpo, y la heredada de `cap_03` "
     u"citada por su sede | **CERRADA en `HH.2`**: `8846` contra `8846`, `22` nodos contra un "
     u"techo de `15` |"),
    (u"| `HH.3` | minar `cap_04` con el techo por delante, cada candidato por su aduana en el "
     u"acto, **cero inserciones** | |",
     u"| `HH.3` | minar `cap_04` con el techo por delante, cada candidato por su aduana en el "
     u"acto, **cero inserciones** | **CERRADA en `HH.3`**: `8` candidatos, `0` `CAERIA`, `13` "
     u"pares de cola, cero inserciones |"),
    (u"| `HH.4` | `PASOS INVENTADOS` de `cap_04`, con la fila del capitulo, el total y **su "
     u"denominador** | |",
     u"| `HH.4` | `PASOS INVENTADOS` de `cap_04`, con la fila del capitulo, el total y **su "
     u"denominador** | **CERRADA en `HH.4`**: `0` PUENTE de `50` pasos, `0,00` por ciento |"),
    (u"| `HH.5` | el cierre: las guardas, la tabla `D.52`, el tablero, el credito y **la linea "
     u"del tramo** | |",
     u"| `HH.5` | el cierre: las guardas, la tabla `D.52`, el tablero, el credito y **la linea "
     u"del tramo** | **CERRADA en `HH.5`**: cierre verde, tabla `D.52` verde y la linea del "
     u"tramo con su reloj |"),
]

for viejo, nuevo in PARES:
    assert viejo in t, viejo[:60]
    t = t.replace(viejo, nuevo)

io.open(R, "w", encoding="utf-8", newline="\n").write(t)
print("las cinco filas del esqueleto, cerradas")
