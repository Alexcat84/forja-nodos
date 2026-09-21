import json
import glob
import re

libro = "grove_high_output"
vistos = set()

for c in sorted(glob.glob(f"cuarentena/{libro}/*.json")):
    with open(c, encoding="utf-8") as f:
        data = json.load(f)
    m = re.search(r"cap_\d\d", data.get("resumen_teorico", ""))
    if m:
        vistos.add(m.group())

with open("dataset/nodos.jsonl", encoding="utf-8") as f:
    for line in f:
        n = json.loads(line)
        claves = [fu.get("clave") for fu in n.get("fuentes", [])]
        if libro in claves:
            m = re.search(r"cap_\d\d", n.get("resumen_teorico", ""))
            if m:
                vistos.add(m.group())

todos = {f"cap_{i:02d}" for i in range(1, 19)}
sin_candidato = sorted(todos - vistos)
print(f"capitulos con al menos un candidato: {len(vistos)}  {sorted(vistos)}")
print(f"capitulos sin ningun candidato (dieron cero): {len(sin_candidato)}  {sin_candidato}")
