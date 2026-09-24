import json
import re
import glob

CEROS = {
    "cap_05": "ACTA M3, seccion M3.5, docs/loop/ACTA_AUDITOR.md linea 45334",
    "cap_15": "ACTA M6, seccion M6.4, docs/loop/ACTA_AUDITOR.md linea 47097",
    "cap_16": "ACTA M7, secciones M7.4 y M7.5, docs/loop/ACTA_AUDITOR.md linea 47319",
    "cap_17": "ACTA M7, secciones M7.4 y M7.5, docs/loop/ACTA_AUDITOR.md linea 47327",
}

candidatos_por_cap = {}
pasos_por_cap = {}

for ruta in sorted(glob.glob("cuarentena/marquet_turn_the_ship/*.json")):
    with open(ruta, encoding="utf-8") as fh:
        d = json.load(fh)
    rt = d.get("resumen_teorico", "")
    m = re.search(r"UNIDAD DE ORIGEN: fuentes/marquet_turn_the_ship/(cap_\d+)\.md", rt)
    cap = m.group(1) if m else "DESCONOCIDO"
    n = len(d.get("pasos_accionables", []))
    candidatos_por_cap.setdefault(cap, []).append(d["id"])
    pasos_por_cap[cap] = pasos_por_cap.get(cap, 0) + n

total_candidatos = 0
total_pasos = 0
capitulos_en_cero = []
print("cap    | candidatos | pasos | ids")
print("-------|-----------:|------:|----")
for i in range(1, 18):
    cap = "cap_%02d" % i
    ids = candidatos_por_cap.get(cap, [])
    pasos = pasos_por_cap.get(cap, 0)
    total_candidatos += len(ids)
    total_pasos += pasos
    if not ids:
        capitulos_en_cero.append(cap)
        marca = "CERO, firmado: " + CEROS.get(cap, "SIN SEDE CITADA")
        print("%s |          0 |     0 | %s" % (cap, marca))
    else:
        print("%s | %10d | %5d | %s" % (cap, len(ids), pasos, ", ".join(ids)))

print("-------|-----------:|------:|----")
print("TOTAL  | %10d | %5d |" % (total_candidatos, total_pasos))
print()
print("capitulos en cero: %d de 17 (%s)" % (len(capitulos_en_cero), ", ".join(capitulos_en_cero)))
print("capitulos con candidatos: %d de 17" % (17 - len(capitulos_en_cero)))
sin_sede = [c for c in capitulos_en_cero if c not in CEROS]
print("capitulos en cero SIN sede citada: %d (%s)" % (len(sin_sede), ", ".join(sin_sede) if sin_sede else "ninguno"))
