# ACTA 75: las cifras de prosa de su 76.3 sobre su barrido (.v76ext/vecinos_<id>.json), contadas. Solo lee. Suma en cada reparto (R7).
import collections, io, json, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
L = [l.strip() for l in open(".v76aud/las22.txt", encoding="utf-8") if l.strip()]
sede = collections.Counter(); fuera = collections.Counter(); sube04 = 0; sin = []; solo3 = []
bandeja_de = collections.Counter()
for c in L:
    j = json.load(open(f".v76ext/vecinos_{c}.json", encoding="utf-8"))
    if not j["vecinos"]: sin.append(c)
    for v in j["vecinos"]:
        sede[v["sede"]] += 1
        if v["sede"] == "grafo": fuera[v["id"]] += 1
        else: bandeja_de["de las 22" if v["id"] in L else "de otra bandeja"] += 1
        if v["senales"]["similitud_texto"] > 0.4: sube04 += 1
        if v["levantada_por"] == ["paso_contra_nodo"] and v["sede"] == "grafo": solo3.append(v["id"])
print("filas dirigidas por sede:", dict(sede), "| suma:", sum(sede.values()))
print("las de bandeja:", dict(bandeja_de), "| suma:", sum(bandeja_de.values()))
print("vecinos del grafo por veces:", dict(fuera), "| suma:", sum(fuera.values()))
print("candidatos sin vecinos:", sin, "| filas dirigidas con similitud_texto > 0,4:", sube04, "| del grafo levantadas solo por la senial 3:", solo3)
