# -*- coding: utf-8 -*-
"""MI conteo, esta vez sin contar dos veces el nodo que ya entro al grafo."""
import io, json, os, re, collections

vistos = {}
for carpeta in ("cuarentena/grove_high_output",
                "cuarentena/_insertados/grove_high_output"):
    for n in sorted(os.listdir(carpeta)):
        if n.endswith(".json"):
            d = json.load(io.open(os.path.join(carpeta, n), encoding="utf-8"))
            vistos[d["id"]] = d
en_grafo = []
for linea in io.open("dataset/nodos.jsonl", encoding="utf-8"):
    nodo = json.loads(linea)
    if any("grove_high_output" in json.dumps(f) for f in nodo.get("fuentes", [])):
        en_grafo.append(nodo["id"])
        if nodo["id"] not in vistos:
            vistos[nodo["id"]] = nodo

print("ids del libro en dataset/nodos.jsonl        :", len(en_grafo), en_grafo)
print("ids del libro en las dos carpetas mas grafo :", len(vistos))

por_cap = collections.defaultdict(lambda: [0, 0])
for d in vistos.values():
    crudo = json.dumps(d, ensure_ascii=False)
    m = re.search(r"grove_high_output/(cap_\d+)\.md", crudo)
    cap = m.group(1) if m else "SIN CAPITULO"
    por_cap[cap][0] += 1
    por_cap[cap][1] += len(d.get("pasos_accionables") or [])
print()
print("%-14s %8s %8s" % ("capitulo", "fichas", "pasos"))
tf = tp = 0
for cap in sorted(por_cap):
    f, p = por_cap[cap]
    tf += f; tp += p
    print("%-14s %8d %8d" % (cap, f, p))
print("%-14s %8d %8d" % ("TOTAL", tf, tp))
