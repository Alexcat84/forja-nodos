# -*- coding: utf-8 -*-
"""MI PROPIO conteo de pasos por capitulo del libro grove_high_output.

Recorre TODA la poblacion del libro (bandeja + insertados + grafo), saca de cada
ficha su capitulo de origen del campo de fuentes, y suma sus pasos_accionables.
No lee el reporte ni el instrumento del extractor.
"""
import io, json, os, re, collections

def fichas():
    for carpeta in ("cuarentena/grove_high_output",
                    "cuarentena/_insertados/grove_high_output"):
        if not os.path.isdir(carpeta):
            continue
        for nombre in sorted(os.listdir(carpeta)):
            if nombre.endswith(".json"):
                yield os.path.join(carpeta, nombre), json.load(
                    io.open(os.path.join(carpeta, nombre), encoding="utf-8"))
    for linea in io.open("dataset/nodos.jsonl", encoding="utf-8"):
        nodo = json.loads(linea)
        if any("grove_high_output" in json.dumps(f) for f in nodo.get("fuentes", [])):
            yield "dataset/nodos.jsonl", nodo

por_cap = collections.defaultdict(lambda: [0, 0])
for ruta, nodo in fichas():
    crudo = json.dumps(nodo, ensure_ascii=False)
    m = re.search(r"grove_high_output/(cap_\d+)\.md", crudo)
    cap = m.group(1) if m else "SIN CAPITULO"
    por_cap[cap][0] += 1
    por_cap[cap][1] += len(nodo.get("pasos_accionables") or [])

print("%-14s %8s %8s" % ("capitulo", "fichas", "pasos"))
tf = tp = 0
for cap in sorted(por_cap):
    f, p = por_cap[cap]
    tf += f
    tp += p
    print("%-14s %8d %8d" % (cap, f, p))
print("%-14s %8d %8d" % ("TOTAL", tf, tp))
