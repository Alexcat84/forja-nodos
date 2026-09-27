# -*- coding: utf-8 -*-
"""CONTROL INDEPENDIENTE DEL REMEDIO DEL SUPERLATIVO: patrones que el 17 NO barria."""
import io, re, os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATRONES = [
    ("unico/unica", r"\b[uU]nic[oa]s?\b"),
    ("mejor/peor", r"\b(mejor|peor)e?s?\b"),
    ("mayor/maximo/minimo", r"\b(mayor|maxim[oa]|minim[oa])s?\b"),
    ("nunca/siempre/jamas", r"\b(nunca|siempre|jamas)\b"),
    ("todos/todas", r"\b[Tt]od[oa]s\b"),
    ("el que mas", r"\bel que mas\b"),
    ("mas <palabra>", r"\bmas [a-zaeiounN]+\b"),
]
for nombre in sys.argv[1:] or ["docs/loop/APERTURA_CIEGA.md"]:
    texto = io.open(os.path.join(RAIZ, nombre), encoding="utf-8").read().split("\n")
    print("== %s" % nombre)
    for etiqueta, patron in PATRONES:
        golpes = []
        for n, linea in enumerate(texto, 1):
            if linea.startswith("    "):
                continue
            for m in re.finditer(patron, linea):
                golpes.append((n, m.group(0), linea.strip()[:90]))
        print("   %-22s %3d golpes en prosa" % (etiqueta, len(golpes)))
        for g in golpes[:40]:
            print("      linea %-5d %-16s %s" % g)
