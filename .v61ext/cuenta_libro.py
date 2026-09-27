import json
import glob

libro = "grove_high_output"

capitulos = sorted(glob.glob(f"fuentes/{libro}/cap_*.md"))
print(f"capitulos del libro {libro}: {len(capitulos)}")

candidatos = sorted(glob.glob(f"cuarentena/{libro}/*.json"))
total_pasos_bandeja = 0
for c in candidatos:
    with open(c, encoding="utf-8") as f:
        data = json.load(f)
    total_pasos_bandeja += len(data.get("pasos_accionables", []))
print(f"candidatos en la bandeja de cuarentena: {len(candidatos)}")
print(f"pasos accionables sumados en la bandeja: {total_pasos_bandeja}")

insertados = []
with open("dataset/nodos.jsonl", encoding="utf-8") as f:
    for line in f:
        n = json.loads(line)
        claves = [fu.get("clave") for fu in n.get("fuentes", [])]
        if libro in claves:
            insertados.append(n)
total_pasos_insertados = sum(len(n.get("pasos_accionables", [])) for n in insertados)
print(f"candidatos ya insertados en el dataset: {len(insertados)}")
for n in insertados:
    print(f"  {n['id']}: {len(n.get('pasos_accionables', []))} pasos")
print(f"pasos accionables sumados en los insertados: {total_pasos_insertados}")

print(f"total candidatos cosechados del libro (bandeja + insertados): {len(candidatos) + len(insertados)}")
print(f"total pasos accionables cosechados del libro: {total_pasos_bandeja + total_pasos_insertados}")
