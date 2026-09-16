# -*- coding: utf-8 -*-
"""Lee el campo UNIDAD DE ORIGEN de cada candidato y lo agrupa por capitulo.
Poblacion: cuarentena/<libro>/ (bandeja) mas dataset/nodos.jsonl (grafo). D.38.4."""
import json, io, glob, os, re, collections, sys

RE_CAP = re.compile(r"fuentes/([a-z0-9_]+)/(cap_\d+)\.md")
RE_LIN = re.compile(r"Sale de las lineas (\d+) a (\d+)")

def leer(ruta):
    return json.load(io.open(ruta, encoding="utf-8"))

def origen(d):
    r = d.get("resumen_teorico", "") or ""
    mc = RE_CAP.search(r); ml = RE_LIN.search(r)
    cap = mc.group(2) if mc else "(sin unidad)"
    lib = mc.group(1) if mc else "(sin libro)"
    lin = (int(ml.group(1)), int(ml.group(2))) if ml else None
    return lib, cap, lin

libro = sys.argv[1] if len(sys.argv) > 1 else "scott_radical_candor"

bandeja = collections.defaultdict(list)
for f in sorted(glob.glob("cuarentena/%s/*.json" % libro)):
    d = leer(f)
    lib, cap, lin = origen(d)
    bandeja[cap].append((d["id"], lin, len(d.get("pasos_accionables", []))))

grafo = collections.defaultdict(list)
for ln in io.open("dataset/nodos.jsonl", encoding="utf-8"):
    d = json.loads(ln)
    if not any(x.get("clave") == libro for x in d.get("fuentes", [])):
        continue
    lib, cap, lin = origen(d)
    grafo[cap].append((d["id"], lin, len(d.get("pasos_accionables", []))))

print("LIBRO: %s" % libro)
print("%-14s %8s %8s" % ("capitulo", "GRAFO", "BANDEJA"))
for cap in sorted(set(list(bandeja) + list(grafo))):
    print("%-14s %8d %8d" % (cap, len(grafo.get(cap, [])), len(bandeja.get(cap, []))))
print("%-14s %8d %8d" % ("TOTAL", sum(len(v) for v in grafo.values()),
                         sum(len(v) for v in bandeja.values())))
