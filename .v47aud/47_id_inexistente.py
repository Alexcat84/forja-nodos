# -*- coding: utf-8 -*-
"""El id que la ficha de identificar_paso_limitante_jornada_desfases declara como
destino de una arista: existe en alguna sede o no. Barre el GRAFO entero y TODAS las
bandejas sin filtro, y mira tambien los ids_alias, que es donde un id puede estar
viviendo bajo otro nombre. AUDITOR_FORJA.md 1.1: una busqueda negativa no se puede
citar si no se ha corrido."""
import json, glob, io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ID = "usar_calendario_herramienta_planificacion_produccion"
sedes = []
grafo = 0

for linea in open("dataset/nodos.jsonl", encoding="utf-8"):
    d = json.loads(linea)
    grafo += 1
    if d.get("id") == ID or ID in (d.get("ids_alias") or []):
        sedes.append("grafo")

fichas = sorted(set(glob.glob("cuarentena/*/*.json") + glob.glob("cuarentena/*/*/*.json")))
for ruta in fichas:
    d = json.load(open(ruta, encoding="utf-8"))
    if d.get("id") == ID or ID in (d.get("ids_alias") or []):
        sedes.append(ruta)

print("sedes donde vive '%s': %s" % (ID, sedes or "NINGUNA"))
print("nodos del grafo barridos:", grafo)
print("fichas de cuarentena barridas:", len(fichas))
