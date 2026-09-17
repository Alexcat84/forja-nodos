# -*- coding: utf-8 -*-
"""La prueba vivia dentro del propio nodo: su unica arista de salida apunta al
capitulo que su texto declaraba sin minar."""
import re, sys
sys.path.insert(0, ".")
from src import comun
RX = re.compile(r"fuentes/scott_radical_candor/(cap_\d\d)\.md")
ix = {n["id"]: n for n in comun.leer_jsonl(comun.RUTA_DATASET)}
m = ix["construir_confianza_equipo_tiempo_solas"]
print("  madre : %s   (de %s)" % (m["id"], ",".join(sorted(set(RX.findall(m["resumen_teorico"]))))))
for h in m["nodos_siguientes"]:
    hijo = ix[h]
    print("  hijo  : %s" % h)
    print("     capitulo del hijo, por la ruta que cita: %s"
          % ",".join(sorted(set(RX.findall(hijo.get("resumen_teorico") or "")))))
