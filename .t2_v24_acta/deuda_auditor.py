"""Instrumento del auditor, vuelta 24, ACTA 24 seccion 1.5.

Cuenta las filas numeradas de la deuda de aristas que el reporte publica en tabla
madre/hijo, y cruza cada extremo contra dataset/nodos.jsonl para saber cuantas de
ellas SE PODRIAN cablear hoy.

    python .t2_v24_acta/deuda_auditor.py
"""
import io, re, json

grafo = set()
prev = sig = 0
for l in io.open("dataset/nodos.jsonl", encoding="utf-8"):
    if l.strip():
        d = json.loads(l)
        grafo.add(d["id"])
        prev += len(d.get("nodos_previos", []))
        sig += len(d.get("nodos_siguientes", []))
print("nodos en el grafo:", len(grafo), "| extremos previos:", prev, "siguientes:", sig)

lineas = io.open("docs/loop/REPORTE.md", encoding="utf-8").read().split("\n")
pares = {}
vistos = {}
for i, l in enumerate(lineas, 1):
    m = re.match(r"^\|\s*\**(\d{1,3})\**\s*\|\s*`([a-z0-9_]+)`\s*\|\s*`([a-z0-9_]+)`\s*\|", l)
    if not m:
        continue
    n = int(m.group(1))
    if 1 <= n <= 90:
        vistos.setdefault(n, []).append((i, m.group(2), m.group(3)))
    if 36 <= n <= 71:
        pares[n] = (m.group(2), m.group(3))

dentro = [n for n in sorted(pares) if pares[n][0] in grafo and pares[n][1] in grafo]
uno = [n for n in sorted(pares) if (pares[n][0] in grafo) != (pares[n][1] in grafo)]
print("aristas 36..71 leidas:", len(pares))
print("con LOS DOS extremos ya en el grafo:", len(dentro), dentro)
print("con UN solo extremo en el grafo:", len(uno))
print("con NINGUN extremo en el grafo:", len(pares) - len(dentro) - len(uno))
print("rango 36..71 presentes:", [n for n in range(36, 72) if n in vistos])
print("faltan en 36..71:", [n for n in range(36, 72) if n not in vistos])
