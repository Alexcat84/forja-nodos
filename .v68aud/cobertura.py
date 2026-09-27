# -*- coding: utf-8 -*-
"""Fase ciega de la 68: que material de Grove dice venir de cap_05 o cap_06 por su UNIDAD DE ORIGEN, en el grafo, en la
bandeja, en _insertados y en _derivadas, ademas de los 20 de .v68aud/los20.txt. Solo imprime ids y sede, no claves de
relacion (R6). No escribe nada."""
import io, json, glob, re, collections
los20 = set(io.open('.v68aud/los20.txt', encoding='utf-8').read().split())
def unidad(d):
    r = json.dumps(d.get('resumen_teorico', ''), ensure_ascii=False)
    m = re.search(r'UNIDAD DE ORIGEN[^c]{0,80}(cap_\d+)', r)
    return m.group(1) if m else None
hits = []
for f in sorted(glob.glob('cuarentena/**/*.json', recursive=True)):
    f = f.replace(chr(92), '/')
    if 'grove_high_output' not in f: continue
    d = json.load(io.open(f, encoding='utf-8'))
    u = unidad(d)
    if u in ('cap_05', 'cap_06'):
        sede = f.split('/')[1] if f.split('/')[1].startswith('_') else 'bandeja'
        hits.append((sede, u, d.get('id')))
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l)
    if 'grove_high_output' in json.dumps(d.get('fuentes', [])) and unidad(d) in ('cap_05', 'cap_06'):
        hits.append(('grafo', unidad(d), d['id']))
print('por sede y capitulo:', dict(collections.Counter((h[0], h[1]) for h in hits)))
fuera = [h for h in hits if h[2] not in los20]
print('de cap_05 o cap_06 y fuera de los 20: %d' % len(fuera))
for h in fuera: print('  %-10s %s %s' % h)
