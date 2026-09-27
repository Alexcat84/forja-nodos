# -*- coding: utf-8 -*-
"""Las aristas EN COLA de la bitacora cuya madre es la cabeza de cap_12, contadas
del dato y no del encargo."""
import io
import json

CABEZA = "desplegar_plan_orden_operaciones_franqueza_radical"
todas = []
mias = []
for n, linea in enumerate(io.open("bitacora/VEREDICTOS.jsonl", encoding="utf-8"), 1):
    registro = json.loads(linea)
    if not registro.get("arista_en_cola"):
        continue
    todas.append(n)
    if (registro.get("arista") or "").startswith(CABEZA + " >"):
        mias.append((n, registro["arista"]))
print("aristas EN COLA en toda la bitacora : %d" % len(todas))
print("de ellas, con la cabeza de cap_12 por madre : %d" % len(mias))
for n, arista in mias:
    print("  linea %-4d %s" % (n, arista))
