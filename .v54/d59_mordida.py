# -*- coding: utf-8 -*-
"""LA MORDIDA DE D.59 SOBRE MI PROPIA CELDA, REPRODUCIBLE.

El primer cerrar_reporte.py de la vuelta se sobrescribio al volver a correrlo,
asi que en vez de citar un fichero que ya no dice lo que dijo, reconstruyo la
celda MALA en memoria y le paso la misma guarda. Sale la misma frase.
"""
import os
import sys

sys.path.insert(0, os.path.abspath("scripts"))
import tallar_reporte  # noqa: E402

BUENA = ("| `4` | **la tasa de `d033` que imprime `.v54/d033_tasa.py`**: digo que "
         "no acota la frecuencia por abajo, **y aun asi cierro la deuda** |")
MALA = ("| `4` | **`0` de `12` en `d033`**: digo que no acota la frecuencia por "
        "abajo, **y aun asi cierro la deuda** |")

crudo = open("docs/loop/REPORTE.md", encoding="utf-8").read()

print("CON LA CELDA COMO LA ESCRIBI (la mala):")
sueltas = tallar_reporte.cifras_derivadas_sueltas(crudo.replace(BUENA, MALA))
print("  CIFRAS DERIVADAS SIN INSTRUMENTO (D.59): %d en la vuelta viva" % len(sueltas))
for una in sueltas:
    print("    frase: %s" % una["frase"].strip())
print()
print("CON LA CELDA YA CORREGIDA (la que se publica):")
sueltas = tallar_reporte.cifras_derivadas_sueltas(crudo)
print("  CIFRAS DERIVADAS SIN INSTRUMENTO (D.59): %d en la vuelta viva" % len(sueltas))
