import json
target = ["mejorar_consciencia_propia_relacional_dos_practicas",
          "practicar_triangulo_critica_tres_papeles",
          "resolver_dudas_frecuentes_pedir_critica"]
nodos = {}
for line in open("dataset/nodos.jsonl", encoding="utf-8"):
    d = json.loads(line)
    if d.get("id") in target:
        nodos[d["id"]] = d

total = 0
for tid in target:
    n = len(nodos[tid].get("pasos_accionables") or [])
    total += n
    print("%-55s %2d pasos" % (tid, n))
print("TOTAL RELEIDO HOY: %d pasos" % total)
