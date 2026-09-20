# -*- coding: utf-8 -*-
"""MORDIDA A MI PROPIA AFIRMACION: estaban VERDES esas dos antes de declarar?

No lo afirmo: lo mido. Saco el DEUDA.jsonl del commit ANTERIOR a mi declaracion
(4365888, la apertura de la vuelta) y le pregunto lo mismo que preguntan las
dos pruebas.
"""
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("scripts"))

ANTES = "4365888"
crudo = subprocess.check_output(
    ["git", "show", "%s:docs/loop/DEUDA.jsonl" % ANTES], text=True, errors="replace")

carpeta = tempfile.mkdtemp()
ruta = os.path.join(carpeta, "DEUDA.jsonl")
with open(ruta, "w", encoding="utf-8") as mano:
    mano.write(crudo)

import deuda  # noqa: E402

print("LA PREGUNTA DE LA PRUEBA 3733: deuda.ultima_saneamiento()")
print("  sobre el registro de %s (antes de mi declaracion) : %s"
      % (ANTES, deuda.ultima_saneamiento(deuda.leer(ruta))))
print("  sobre el registro VIVO de hoy                     : %s"
      % deuda.ultima_saneamiento())
print("  lo que la prueba exige                            : 49")
