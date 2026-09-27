import json
import glob
import re

libro = "grove_high_output"

capitulos = sorted(glob.glob(f"fuentes/{libro}/cap_*.md"))

por_capitulo = {}

candidatos = sorted(glob.glob(f"cuarentena/{libro}/*.json"))
total_pasos_bandeja = 0
for c in candidatos:
    with open(c, encoding="utf-8") as f:
        data = json.load(f)
    n_pasos = len(data.get("pasos_accionables", []))
    total_pasos_bandeja += n_pasos
    m = re.search(r"cap_\d\d", data.get("resumen_teorico", ""))
    cap = m.group() if m else "SIN_CAPITULO_LEGIBLE"
    por_capitulo.setdefault(cap, {"candidatos": 0, "pasos": 0, "en_grafo": 0})
    por_capitulo[cap]["candidatos"] += 1
    por_capitulo[cap]["pasos"] += n_pasos

insertados = []
with open("dataset/nodos.jsonl", encoding="utf-8") as f:
    for line in f:
        n = json.loads(line)
        claves = [fu.get("clave") for fu in n.get("fuentes", [])]
        if libro in claves:
            insertados.append(n)
total_pasos_insertados = sum(len(n.get("pasos_accionables", [])) for n in insertados)
for n in insertados:
    m = re.search(r"cap_\d\d", n.get("resumen_teorico", ""))
    cap = m.group() if m else "SIN_CAPITULO_LEGIBLE"
    n_pasos = len(n.get("pasos_accionables", []))
    por_capitulo.setdefault(cap, {"candidatos": 0, "pasos": 0, "en_grafo": 0})
    por_capitulo[cap]["candidatos"] += 1
    por_capitulo[cap]["pasos"] += n_pasos
    por_capitulo[cap]["en_grafo"] += 1

print(f"LA CUENTA DEL LIBRO {libro}, CONTADA POR EL EXTRACTOR (D.59)")
print(f"  capitulos del libro (ficheros cap_*.md) : {len(capitulos)}")
print(f"  candidatos en la bandeja                : {len(candidatos)}")
print(f"  pasos_accionables en la bandeja         : {total_pasos_bandeja}")
print(f"  insertados en el grafo                  : {len(insertados)}")
for n in insertados:
    print(f"     {n['id']}: {len(n.get('pasos_accionables', []))} pasos")
print(f"  pasos en los insertados                 : {total_pasos_insertados}")
print(f"  TOTAL cosechado del libro               : {len(candidatos) + len(insertados)}")
print(f"  TOTAL pasos cosechados del libro        : {total_pasos_bandeja + total_pasos_insertados}")
print()
print("  POR CAPITULO (bandeja MAS insertados), el capitulo leido del resumen_teorico:")
con_candidato = 0
sin_candidato = []
for i in range(1, 19):
    cap = f"cap_{i:02d}"
    d = por_capitulo.get(cap, {"candidatos": 0, "pasos": 0, "en_grafo": 0})
    marca = f"   <- DIO CERO" if d["candidatos"] == 0 else ""
    grafo = f"   [{d['en_grafo']} en el grafo]" if d["en_grafo"] else ""
    print(f"     {cap}: {d['candidatos']:2d} candidato(s), {d['pasos']:3d} paso(s){grafo}{marca}")
    if d["candidatos"] > 0:
        con_candidato += 1
    else:
        sin_candidato.append(cap)

sin_capitulo_legible = por_capitulo.get("SIN_CAPITULO_LEGIBLE", {"candidatos": 0, "pasos": 0})

print()
print(f"  capitulos CON al menos un candidato: {con_candidato}")
print(f"  capitulos que DIERON CERO          : {len(sin_candidato)}  {sin_candidato}")
suma_candidatos = sum(d["candidatos"] for d in por_capitulo.values())
suma_pasos = sum(d["pasos"] for d in por_capitulo.values())
print(f"  suma de control (por capitulo)     : {suma_candidatos} candidatos, {suma_pasos} pasos")
print(f"  fichas sin capitulo legible        : {sin_capitulo_legible['candidatos']}")
