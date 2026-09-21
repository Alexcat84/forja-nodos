import json, pathlib
base = pathlib.Path("cuarentena/grove_high_output")
for f in sorted(base.glob("*.json")):
    d = json.loads(f.read_text(encoding="utf-8"))
    rt = d.get("resumen_teorico", "")
    i = rt.find("Sale de la PIEZA")
    if i == -1:
        continue
    tramo = rt[i:i+24]
    if "P34" in tramo or "P38" in tramo:
        print("  %-56s declara: %s" % (d["id"], tramo))
