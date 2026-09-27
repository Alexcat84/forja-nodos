# -*- coding: utf-8 -*-
"""LA CADENA DE MI RACHA PROPIA, leida de las cabeceras de seccion 8 de cada acta."""
import io, re, sys
sys.stdout.reconfigure(encoding="utf-8")
t = io.open("docs/loop/ACTA_AUDITOR.md", encoding="utf-8").read().split("\n")
cortes = [(i, l) for i, l in enumerate(t) if l.startswith("# ACTA ")]
for k,(i,l) in enumerate(cortes):
    fin = cortes[k+1][0] if k+1 < len(cortes) else len(t)
    if k+1 < 19: continue
    tramo = t[i:fin]
    print("\n--- %s" % l[:90])
    for j,ln in enumerate(tramo):
        if re.search(r"(la mia|auditor).{0,140}\d de 3", ln) or re.search(r"\d de 3.{0,80}(mia|auditor)", ln):
            print("    L%d: %s" % (i+j+1, ln.strip()[:300]))
