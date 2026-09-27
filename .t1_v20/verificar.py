# -*- coding: utf-8 -*-
"""Las dos cifras heredadas que mi cierre repite, remedidas por mi (EXTRACTOR.md 5)."""
import json

n_scott = 0
aristas = 0
cruzan = 0
total = 0
fuente_por_id = {}
nodos = []
for linea in open('dataset/nodos.jsonl', encoding='utf-8'):
    linea = linea.strip()
    if not linea:
        continue
    d = json.loads(linea)
    nodos.append(d)
    total += 1
    claves = [f.get('clave') for f in d.get('fuentes', [])]
    fuente_por_id[d['id']] = claves
    if 'scott_radical_candor' in claves:
        n_scott += 1
for d in nodos:
    for campo in ('nodos_previos', 'nodos_siguientes'):
        for otro in d.get(campo, []):
            oid = otro if isinstance(otro, str) else otro.get('id')
            aristas += 1
            a = set(fuente_por_id.get(d['id'], []))
            b = set(fuente_por_id.get(oid, []))
            if a and b and not (a & b):
                cruzan += 1
print("nodos del grafo                              :", total)
print("nodos con fuente scott_radical_candor        :", n_scott)
print("extremos de arista contados (ida y vuelta)   :", aristas)
print("  de esos, los que cruzan de libro           :", cruzan)
print("aristas distintas (los extremos entre dos)   :", aristas // 2)
