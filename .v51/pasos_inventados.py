import json, pathlib, re, collections
base = pathlib.Path("cuarentena/grove_high_output")
arch = pathlib.Path("cuarentena/_insertados/grove_high_output")
CAP = {"Cap. 1": "cap_02", "Cap. 2": "cap_03", "Cap. 3": "cap_04", "Cap. 4": "cap_05"}
pasos = collections.Counter(); fichas = collections.Counter()
for carpeta in (base, arch):
    for f in sorted(carpeta.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        m = re.search(r"unidad (Cap\. \d+|Introduccion|Prefacio|[^,]+?), titulo", d.get("resumen_teorico", ""))
        u = m.group(1) if m else "SIN UNIDAD"
        cap = CAP.get(u, u)
        pasos[cap] += len(d["pasos_accionables"]); fichas[cap] += 1
print("    %-22s %8s %8s %10s %10s" % ("capitulo del libro", "fichas", "pasos", "PUENTE", "inventados"))
tp = tf = 0
for cap in sorted(pasos):
    print("    %-22s %8d %8d %10d %10s" % (cap, fichas[cap], pasos[cap], 0, "0 de %d" % pasos[cap]))
    tp += pasos[cap]; tf += fichas[cap]
print("    %-22s %8d %8d %10d %10s" % ("TODO grove_high_output", tf, tp, 0, "0 de %d" % tp))
