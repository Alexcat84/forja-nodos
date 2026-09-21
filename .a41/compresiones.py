# -*- coding: utf-8 -*-
"""Manual 3.4 prohibe DOS compresiones de la misma numeracion. Busco en el grafo
cualquier nodo que diga ser cabeza de serie y cuantos elementos comprime, para
ver si la numeracion de los trece de cap_14 la comprime alguien mas."""
import json, io, re, collections
cab = []
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    if not l.strip(): continue
    d = json.loads(l)
    r = d.get('resumen_teorico', '') or ''
    if 'CABEZA DE UNA SERIE' in r.upper() or 'ES LA CABEZA' in r.upper():
        sig = len(d.get('nodos_siguientes') or [])
        cab.append((d['id'], sig, len(d.get('pasos_accionables', []))))
print('nodos que se declaran CABEZA DE SERIE: %d' % len(cab))
print('%-58s %5s %6s' % ('id', 'hijos', 'pasos'))
for i, s_, p in sorted(cab):
    print('%-58s %5d %6d' % (i, s_, p))
print()
n = 0
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    if not l.strip(): continue
    d = json.loads(l)
    r = d.get('resumen_teorico', '') or ''
    if 'cap_14' in r and ('trece' in r.lower() or 'thirteen' in r.lower()):
        n += 1
        print('cita los trece de cap_14: %s' % d['id'])
print('nodos que citan la numeracion de los trece de cap_14: %d' % n)
