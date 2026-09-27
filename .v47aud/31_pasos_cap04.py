import json, glob, os
tot = {}
for p in sorted(glob.glob("cuarentena/grove_high_output/*.json")):
    d = json.load(open(p, encoding="utf-8"))
    rt = d.get("resumen_teorico", "")
    cap = None
    for tok in ("cap_01","cap_02","cap_03","cap_04","cap_05"):
        if tok in rt or tok in json.dumps(d, ensure_ascii=False):
            cap = tok; break
    n = len(d.get("pasos_accionables", []))
    tot.setdefault(cap, []).append((os.path.basename(p)[:-5], n))
for cap in sorted(tot, key=lambda x: (x is None, x)):
    filas = tot[cap]
    print(f"== {cap}: {len(filas)} fichas, {sum(n for _, n in filas)} pasos")
    if cap == "cap_04":
        for nom, n in filas: print(f"   {n:3}  {nom}")
