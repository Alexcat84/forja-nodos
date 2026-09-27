# -*- coding: utf-8 -*-
"""Los veredictos que ESTA vuelta escribio en bitacora/VEREDICTOS.jsonl."""
import sys, json, collections
sys.path.insert(0, ".")
from src import comun
v = comun.leer_jsonl(comun.RUTA_VEREDICTOS)
hoy = [x for x in v if x.get("vuelta") == 34 or "2026-09-17" in json.dumps(x)]
print("lineas en bitacora/VEREDICTOS.jsonl : %d" % len(v))
NUEVOS = v[410:]
print("escritas en esta vuelta (de la 411 a la %d): %d" % (len(v), len(NUEVOS)))
c = collections.Counter(x.get("clase") or x.get("veredicto") or x.get("tipo") or "?" for x in NUEVOS)
print("")
print("| clase | cuantos |")
print("|---|---:|")
for k, n in sorted(c.items()):
    print("| `%s` | **%d** |" % (k, n))
print("| **total** | **%d** |" % len(NUEVOS))
