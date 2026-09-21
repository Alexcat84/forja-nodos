# -*- coding: utf-8 -*-
"""CENSO PARTIDO POR DOCUMENTO: de donde salen las rutas que el censo cuenta."""
import os, sys, subprocess
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
sys.path.insert(0, RAIZ)
import censar_rutas as C

DOCS = [os.path.join("docs", "loop", "REPORTE.md"),
        os.path.join("docs", "loop", "ACTA_AUDITOR.md"),
        os.path.join("docs", "loop", "APERTURA_CIEGA.md")]

def cuenta(doc):
    caidas, pasan = C.censar([doc])
    formas = {}
    for p in pasan:
        k = p["forma"].split(" (")[0].split(":")[0]; formas[k] = formas.get(k, 0) + 1
    return len(pasan), len(caidas), formas

total = 0
for d in DOCS:
    n, c, f = cuenta(d)
    total += n
    print("%-32s pasan %4d  caen %d   %s" % (d.replace("\\", "/"), n, c, f))
print("SUMA DE LOS TRES                 %4d" % total)

# Y LA APERTURA CIEGA QUE ESTABA EN EL ARBOL CUANDO EL EXTRACTOR CERRO
vieja = os.path.join(RAIZ, ".v49aud", "apertura_v48.md")
if os.path.exists(vieja):
    n, c, f = cuenta(os.path.join(".v49aud", "apertura_v48.md"))
    print(".v49aud/apertura_v48.md          pasan %4d  caen %d   %s" % (n, c, f))
