# -*- coding: utf-8 -*-
"""Compara el bloque del informe pegado en 62.4 contra el fichero guardado."""
import io
lineas = io.open("docs/loop/REPORTE.md", encoding="utf-8").read().split("\n")
i = [k for k, l in enumerate(lineas) if l.startswith("# VUELTA 62,")][0]
t = lineas[i:]
ini = next(k for k, l in enumerate(t) if "INFORME DE LA ADUANA EN SECO" in l) - 1
fin = next(k for k, l in enumerate(t) if "veredicto escrito por vecino." in l)
peg = [l[4:] if l.startswith("    ") else l for l in t[ini:fin + 1]]
fil = io.open(".v62ext/informe_detectar_arreglar_fallo.txt", encoding="utf-8").read().rstrip("\n").split("\n")[:len(peg)]
mal = [(k, a, b) for k, (a, b) in enumerate(zip(fil, peg)) if a.rstrip() != b.rstrip()]
print("lineas comparadas: %d" % len(peg))
print("lineas que difieren: %d" % len(mal))
for k, a, b in mal:
    print("  %d  %r  |  %r" % (k, a, b))
