# ACTA 64: la cola de Grove que queda en la bandeja, por capitulo y pieza, leida de la UNIDAD DE ORIGEN de cada
# resumen_teorico (el mismo criterio que .v64ext/los22.txt). Solo cuenta: el orden de insercion lo fija el extractor.
import json, glob, re, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
filas = []
for f in glob.glob("cuarentena/grove_high_output/*.json"):
    d = json.load(open(f, encoding="utf-8")); r = d.get("resumen_teorico", "")
    cap = re.search(r"UNIDAD DE ORIGEN: fuentes/grove_high_output/(cap_\d\d)\.md", r)
    pza = re.search(r"PIEZA (P\d+)", r)
    filas.append((cap.group(1) if cap else "?", int(pza.group(1)[1:]) if pza else 999, d["id"], len(d.get("pasos_accionables", []))))
filas.sort()
por = collections.Counter(c for c, _, _, _ in filas)
print("en la bandeja: %d | por capitulo de UNIDAD DE ORIGEN: %s" % (len(filas), ", ".join("%s %d" % kv for kv in sorted(por.items()))))
acum = 0
for n, (c, p, i, k) in enumerate(filas, 1):
    print("%3d  %-6s P%-3s %-55s pasos %d" % (n, c, p if p != 999 else "?", i, k))
