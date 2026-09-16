# -*- coding: utf-8 -*-
"""cap_07 de scott_radical_candor por orden de linea del libro. D.38.4.
Lee las DOS grafias con que los candidatos declaran su tramo."""
import json, io, glob, re
RE_CAP = re.compile(r"fuentes/([a-z0-9_]+)/(cap_\d+)\.md")
RE_LIN = re.compile(r"l[ií]neas?\s+(\d+)\s+a\s+(\d+)")
def orig(d):
    r = d.get("resumen_teorico","") or ""
    mc = RE_CAP.search(r)
    todos = [(int(a),int(b)) for a,b in RE_LIN.findall(r)]
    return (mc.group(2) if mc else "?"), (todos[0] if todos else (0,0)), todos
filas=[]
for ln in io.open("dataset/nodos.jsonl",encoding="utf-8"):
    d=json.loads(ln); cap,lin,todos=orig(d)
    if cap=="cap_07" and any(x.get("clave")=="scott_radical_candor" for x in d.get("fuentes",[])):
        filas.append(("GRAFO",lin,d["id"],len(d["pasos_accionables"]),todos))
for f in sorted(glob.glob("cuarentena/scott_radical_candor/*.json")):
    d=json.load(io.open(f,encoding="utf-8")); cap,lin,todos=orig(d)
    if cap=="cap_07":
        filas.append(("BANDEJA",lin,d["id"],len(d["pasos_accionables"]),todos))
filas.sort(key=lambda x:(x[1][0],x[1][1]))
print("%-8s %-10s %-46s %5s" % ("donde","lineas","id","pasos"))
for donde,lin,i,p,todos in filas:
    extra = "" if len(todos)<2 else "  (tramo no contiguo: %s)" % " y ".join("%d-%d"%t for t in todos)
    print("%-8s %-10s %-46s %5d%s" % (donde,"%d-%d"%lin,i,p,extra))
g=sum(1 for f in filas if f[0]=="GRAFO"); b=sum(1 for f in filas if f[0]=="BANDEJA")
print()
print("GRAFO: %d   BANDEJA: %d   TOTAL cap_07: %d" % (g,b,len(filas)))
print("PASOS en el grafo: %d   PASOS en bandeja: %d" % (
    sum(f[3] for f in filas if f[0]=="GRAFO"), sum(f[3] for f in filas if f[0]=="BANDEJA")))
