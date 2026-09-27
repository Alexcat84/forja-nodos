# -*- coding: utf-8 -*-
import io, json, os, re
for carpeta in ("cuarentena/grove_high_output",
                "cuarentena/_insertados/grove_high_output"):
    if not os.path.isdir(carpeta):
        continue
    for n in sorted(os.listdir(carpeta)):
        if not n.endswith(".json"):
            continue
        d = json.load(io.open(os.path.join(carpeta, n), encoding="utf-8"))
        crudo = json.dumps(d, ensure_ascii=False)
        m = re.search(r"grove_high_output/(cap_\d+)\.md", crudo)
        if m and m.group(1) == "cap_01":
            print("%-22s %-52s pasos %d" % (carpeta.split("/")[-2] if "_insertados" in carpeta else "bandeja",
                                            d.get("id"), len(d.get("pasos_accionables") or [])))
            for f in d.get("fuentes", []):
                print("      fuente:", json.dumps(f, ensure_ascii=False)[:200])
