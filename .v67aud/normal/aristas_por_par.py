# -*- coding: utf-8 -*-
"""ACTA 66: las aristas del grafo de HOY menos las del commit de la ACTA 65 (4648cbc), por par, contra mi lista de
.v67aud/esperado_67.txt (fase ciega); y la simetria previos/siguientes de cada una."""
import io, json, subprocess
def aristas(lineas):
    N = {}; E = set(); S = set()
    for l in lineas:
        if not l.strip(): continue
        d = json.loads(l); N[d['id']] = d
    for i, d in N.items():
        for s in d.get('nodos_siguientes', []): E.add((i, s))
        for p in d.get('nodos_previos', []): S.add((p, i))
    return N, E, S
N0, E0, S0 = aristas(subprocess.run(['git', 'show', '4648cbc:dataset/nodos.jsonl'], capture_output=True).stdout.decode('utf-8').splitlines())
N1, E1, S1 = aristas(io.open('dataset/nodos.jsonl', encoding='utf-8').read().splitlines())
print('aristas por siguientes: 4648cbc %d | hoy %d | por previos: 4648cbc %d | hoy %d' % (len(E0), len(E1), len(S0), len(S1)))
print('asimetricas hoy (siguientes sin previos o al reves): %d' % len(E1 ^ S1))
nuevas = sorted(E1 - E0); perdidas = sorted(E0 - E1)
print('nuevas: %d | perdidas: %d' % (len(nuevas), len(perdidas)))
esp = set()
for l in io.open('.v67aud/esperado_67.txt', encoding='utf-8'):
    c = l.split()
    if c and c[0] == 'ESPERADA': esp.add((c[1], c[3]))
for m, h in nuevas: print('  %-9s %s > %s' % ('ESPERADA' if (m, h) in esp else 'NO ESPER', m, h))
print('esperadas por mi lectura: %d | nuevas que lo son: %d | esperadas que no estan: %s' % (len(esp), len(esp & set(nuevas)), sorted(esp - set(nuevas))))
print('C3 buscar > detectar en el grafo: %s' % (('buscar_actividad_alta_palanca_tres_vias', 'detectar_palanca_negativa_actividad_mando') in E1))
