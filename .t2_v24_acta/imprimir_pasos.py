import json, io, sys, glob, os
def cargar(idn):
    for l in io.open("dataset/nodos.jsonl", encoding="utf-8"):
        if not l.strip(): continue
        d = json.loads(l)
        if d.get("id") == idn: return d, "grafo"
    for r in glob.glob("cuarentena/*/*.json") + glob.glob("cuarentena/_insertados/*/*.json"):
        try: d = json.load(open(r, encoding="utf-8"))
        except Exception: continue
        if d.get("id") == idn: return d, r
    return None, None
for idn in sys.argv[1:]:
    d, sede = cargar(idn)
    if d is None:
        print("NO ENCONTRADO:", idn); continue
    print("="*100)
    print(idn, " [", sede, "]  fuentes:", [f.get("clave") if isinstance(f,dict) else f for f in d.get("fuentes",[])])
    print("  TITULO   :", d.get("titulo"))
    print("  CONDICION:", d.get("condiciones_activacion"))
    print("  ENTREGABLE:", d.get("entregable_esperado"))
    for i, p in enumerate(d.get("pasos_accionables", []), 1):
        t = p if isinstance(p, str) else json.dumps(p, ensure_ascii=False)
        print("   %2d. %s" % (i, t))
