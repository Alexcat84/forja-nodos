# -*- coding: utf-8 -*-
"""Cuenta las rutas censadas POR DOCUMENTO, y ademas con la APERTURA_CIEGA vieja."""
import io, os, subprocess, sys
sys.path.insert(0, "scripts")
import censar_rutas as C

for doc in C.DOCUMENTOS:
    caidas, pasan = C.censar(documentos=[doc])
    print("%-32s censadas %4d   pasan %4d   caen %d"
          % (doc, len(caidas) + len(pasan), len(pasan), len(caidas)))

# La apertura que el extractor tenia delante al cerrar la vuelta 51
vieja = subprocess.check_output(
    ["git", "show", "b04ac62:docs/loop/APERTURA_CIEGA.md"])
ruta = os.path.join("docs", "loop", "APERTURA_CIEGA_VIEJA_SOLO_MEDIDA.md")
io.open(ruta, "wb").write(vieja)
try:
    caidas, pasan = C.censar(documentos=[ruta.replace("\\", "/")])
    print("%-32s censadas %4d   pasan %4d   caen %d"
          % ("APERTURA_CIEGA de b04ac62", len(caidas) + len(pasan),
             len(pasan), len(caidas)))
finally:
    os.remove(ruta)
