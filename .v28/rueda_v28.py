# -*- coding: utf-8 -*-
"""LA CABEZA DE LA RUEDA DE cap_07 CONTRA SUS PARTES, medido sobre el grafo de hoy.

Cuenta cuantas piezas de cap_07 viven ya en dataset/nodos.jsonl, si la cabeza vive,
y cuantas aristas la tocan. No teclea ninguna celda.

    $ python .v28/rueda_v28.py
"""
import io, json, glob, re
grafo = {}
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    if l.strip():
        n = json.loads(l)
        grafo[n['id']] = n
def tramo(p):
    d = json.load(io.open(p, encoding='utf-8'))
    r = d.get('resumen_teorico', '') or ''
    if 'cap_07.md' not in r:
        return None
    m = re.search(r'lineas?\s+(\d+)\s+a\s+(\d+)', r)
    return (int(m.group(1)), int(m.group(2)), d['id']) if m else None
piezas = []
for p in (glob.glob('cuarentena/scott_radical_candor/*.json')
          + glob.glob('cuarentena/_insertados/scott_radical_candor/*.json')):
    t = tramo(p)
    if t:
        piezas.append(t)
piezas.sort()
cabeza = 'recorrer_rueda_hacer_cosas_equipo'
print("CABEZA DE LA RUEDA : %s" % cabeza)
print("  vive en el grafo : %s" % (cabeza in grafo))
partes = [p for p in piezas if p[2] != cabeza]
print("  piezas de cap_07 que NO son la cabeza : %d" % len(partes))
print("  de ellas, YA EN EL GRAFO             : %d" % len([p for p in partes if p[2] in grafo]))
print("  de ellas, aun en bandeja             : %d" % len([p for p in partes if p[2] not in grafo]))
print("")
print("ARISTAS EN EL GRAFO QUE TOCAN A LA CABEZA : %d" % len([
    1 for n in grafo.values()
    for h in (n.get('nodos_siguientes') or []) + (n.get('nodos_previos') or [])
    if (h.get('id') if isinstance(h, dict) else h) == cabeza]))
print("")
print("LAS PIEZAS DE cap_07 YA EN EL GRAFO, CON SUS ARISTAS:")
for a, b, i in partes:
    if i not in grafo:
        continue
    n = grafo[i]
    pv = [(x.get('id') if isinstance(x, dict) else x) for x in (n.get('nodos_previos') or [])]
    sg = [(x.get('id') if isinstance(x, dict) else x) for x in (n.get('nodos_siguientes') or [])]
    print("   L%-4s %-56s previos=%s siguientes=%s" % (a, i, pv or '[]', sg or '[]'))
