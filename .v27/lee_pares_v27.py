# -*- coding: utf-8 -*-
"""Imprime los pasos ENTEROS de los dos lados de un par. NO imprime razon ni veredicto."""
import io, json, glob, sys
sys.stdout.reconfigure(encoding="utf-8")
idx = {}
for l in io.open("dataset/nodos.jsonl",encoding="utf-8"):
    if l.strip():
        d = json.loads(l); idx[d["id"]] = ("GRAFO", d)
for r in glob.glob("cuarentena/*/*.json") + glob.glob("cuarentena/_insertados/*/*.json"):
    if "_derivadas" in r: continue
    d = json.load(io.open(r,encoding="utf-8"))
    idx.setdefault(d["id"], ("BANDEJA", d))

def pinta(i):
    if i not in idx: print("   [NO EXISTE: %s]" % i); return
    donde, d = idx[i]
    print("  === %s   [%s]" % (i, donde))
    print("      activacion: %s" % (d.get("condiciones_activacion","") or "")[:300])
    print("      entregable: %s" % (d.get("entregable_esperado","") or "")[:300])
    print("      previos   : %s   siguientes: %s" % (d.get("nodos_previos"), d.get("nodos_siguientes")))
    for k,p in enumerate(d.get("pasos_accionables",[]) or [],1):
        t = p if isinstance(p,str) else (p.get("texto") or p.get("paso") or json.dumps(p,ensure_ascii=False))
        print("      %2d. %s" % (k,t))

for linea in sys.argv[1:]:
    a,b = linea.split("|")
    print("\n" + "="*100)
    print("PAR: %s  CONTRA  %s" % (a,b))
    print("="*100)
    pinta(a); print(); pinta(b)
