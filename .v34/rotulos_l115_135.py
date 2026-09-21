# -*- coding: utf-8 -*-
"""LOS SEIS ROTULOS DE LAS LINEAS 115 A 135, contados uno a uno del libro.
Pasa por la misma limpia() de .v34/fidelidad.py: el libro trae guion medio y comillas
tipograficas, y en este repo no entra ni un guion medio (manual seccion 2)."""
import io, sys
sys.path.insert(0, ".v34")
from fidelidad import LINEAS, limpia
for n in (123, 127, 129, 131, 133, 135):
    print("%d: %s" % (n, limpia(LINEAS[n - 1])[:72]))
