import json, glob, os, re, collections
raiz = "."
pat = []
pat += glob.glob("cuarentena/scott_radical_candor/*.json")
pat += glob.glob("cuarentena/_insertados/scott_radical_candor/*.json")
filas = collections.defaultdict(lambda: [0,0])
sinu = []
for r in sorted(pat):
    d = json.load(open(r, encoding="utf-8"))
    txt = json.dumps(d, ensure_ascii=False)
    m = re.search(r"UNIDAD DE ORIGEN:\s*(cap_\d+)", txt)
    if not m:
        m = re.search(r"(cap_\d+)\.md", txt)
    if not m:
        m = re.search(r"(cap_\d+)", txt)
    u = m.group(1) if m else "SIN_UNIDAD"
    if u == "SIN_UNIDAD": sinu.append(r)
    filas[u][0] += 1
    filas[u][1] += len(d.get("pasos_accionables", []))
tc = tp = 0
print("unidad      candidatos   pasos")
for u in sorted(filas):
    c,p = filas[u]; tc += c; tp += p
    print("%-10s %10d %7d" % (u,c,p))
print("%-10s %10d %7d" % ("TOTAL", tc, tp))
print("ficheros leidos:", len(pat))
print("sin unidad:", sinu)
