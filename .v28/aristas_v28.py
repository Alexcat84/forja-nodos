# -*- coding: utf-8 -*-
"""ARISTAS Y NODOS NUEVOS DE LA VUELTA 27, contados del arbol y no de su palabra.

Compara dataset/nodos.jsonl de hoy contra el de `360f941`, que es el commit del
arnes al ABRIR la vuelta 27. No teclea ninguna celda.

    $ git show 360f941:dataset/nodos.jsonl > .v28/grafo_pre27.jsonl
    $ python .v28/aristas_v28.py
"""
import io, json
def carga(f):
    return [json.loads(l) for l in io.open(f, encoding='utf-8') if l.strip()]
def aristas(nodos):
    s = set()
    for n in nodos:
        for h in (n.get('nodos_siguientes') or []):
            s.add((n['id'], h.get('id') if isinstance(h, dict) else h))
        for m in (n.get('nodos_previos') or []):
            s.add((m.get('id') if isinstance(m, dict) else m, n['id']))
    return s
hoy = carga('dataset/nodos.jsonl')
pre = carga('.v28/grafo_pre27.jsonl')
a_hoy, a_pre = aristas(hoy), aristas(pre)
print("nodos al abrir la v27 : %d" % len(pre))
print("nodos hoy             : %d" % len(hoy))
print("aristas al abrir v27  : %d" % len(a_pre))
print("aristas hoy           : %d" % len(a_hoy))
print("NUEVAS                : %d" % len(a_hoy - a_pre))
for a in sorted(a_hoy - a_pre): print("   + %s > %s" % a)
print("RETIRADAS             : %d" % len(a_pre - a_hoy))
for a in sorted(a_pre - a_hoy): print("   - %s > %s" % a)
ids_pre = {n['id'] for n in pre}
print("")
print("NODOS NUEVOS          : %d" % len([n for n in hoy if n['id'] not in ids_pre]))
for n in hoy:
    if n['id'] not in ids_pre:
        print("   * %s   (%d pasos)" % (n['id'], len(n.get('pasos_accionables') or [])))
