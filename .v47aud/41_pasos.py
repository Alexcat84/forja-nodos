# -*- coding: utf-8 -*-
"""Imprime los pasos de un candidato de la bandeja, numerados, sin su resumen."""
import json, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
for ident in sys.argv[1:]:
    d = json.load(open("cuarentena/grove_high_output/%s.json" % ident, encoding="utf-8"))
    print("=== %s  (%s)" % (d["id"], d["titulo"]))
    print("    entregable: %s" % d.get("entregable_esperado", "")[:160])
    for i, p in enumerate(d["pasos_accionables"], 1):
        print("  %2d. %s" % (i, p))
    print()
