# -*- coding: utf-8 -*-
"""Retira de las celdas la forma 'N de M del capitulo', que D.52 reserva para el grafo."""
import io

R = "docs/loop/REPORTE.md"
t = io.open(R, encoding="utf-8").read()

VIEJO = u"**CERRADA EN `8` DE `22`**"
NUEVO = u"**CERRADA EN `8` candidatos de los `22` que da la frontera**"
VIEJO2 = u"**CERRADA EN `8` DE `22` del capitulo**"
NUEVO2 = u"**CERRADA EN `8` candidatos de los `22` que da la frontera**"

assert VIEJO2 in t
t = t.replace(VIEJO2, NUEVO2)
assert VIEJO in t
t = t.replace(VIEJO, NUEVO)

io.open(R, "w", encoding="utf-8", newline="\n").write(t)
print("celdas reescritas")
