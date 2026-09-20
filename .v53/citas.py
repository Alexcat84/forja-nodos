# -*- coding: utf-8 -*-
"""LA CITA DE LINEA CON SU sed PEGADO AL LADO (D.35).

Imprime, para cada linea que esta vuelta cita, la salida literal de sed -n '<n>p' recortada,
con los guiones largos y las comillas tipograficas pasadas a llanas para que el barrido de
guiones no caiga sobre la cita. LA CITA SE PEGA, NO SE PROMETE.
"""
import io
import subprocess
import sys
import unicodedata

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

RUTA = "fuentes/grove_high_output/cap_06.md"
LINEAS = [23, 25, 27, 29, 33, 41, 49, 51, 61, 63, 65, 67, 69, 71, 73, 75, 77, 93]
ANCHO = 74


def llana(texto):
    texto = texto.replace(chr(0x2014), "-").replace(chr(0x2013), "-")
    texto = texto.replace(chr(0x2018), "'").replace(chr(0x2019), "'")
    texto = texto.replace(chr(0x201C), '"').replace(chr(0x201D), '"')
    texto = texto.replace(chr(0x2026), "...")
    return "".join(c for c in unicodedata.normalize("NFD", texto)
                   if unicodedata.category(c) != "Mn")


print("| pieza y linea | la salida de sed, pegada y recortada a %d caracteres |" % ANCHO)
print("|---|---|")
for n in LINEAS:
    crudo = subprocess.check_output(
        ["sed", "-n", "%dp" % n, RUTA]).decode("utf-8").rstrip("\r\n")
    print("| `sed -n '%dp'` | `%d:%s` |" % (n, n, llana(crudo)[:ANCHO]))
