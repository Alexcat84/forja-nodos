# -*- coding: utf-8 -*-
"""ACTA 72, PASOS INVENTADOS POR CAPITULO (8, 8.2, 8.3): lee las marcas del extractor (.v73ext/fidelidad.tsv, barras), que
marca P los seis pasos corregidos leidos sobre su texto viejo, y el capitulo de cada ficha de .v72aud/normal/siete.txt. Una fila
por capitulo con el reparto de marcas y su suma (R7), y cuantos pasos tiene hoy cada ficha, para que la fila cuadre. Solo lee."""
import io, json, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
cap = dict((l.split()[1], l.split()[0]) for l in io.open('.v72aud/normal/siete.txt', encoding='utf-8') if l.startswith('cap_'))
m = collections.defaultdict(collections.Counter); cand = collections.defaultdict(set)
for l in io.open('.v73ext/fidelidad.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    c = [x.strip() for x in l.split('|', 4)]
    m[cap[c[0]]][c[2]] += 1; cand[cap[c[0]]].add(c[0])
for k in sorted(m):
    n = sum(len(json.load(io.open('cuarentena/grove_high_output/%s.json' % i, encoding='utf-8'))['pasos_accionables']) for i in cand[k])
    t = sum(m[k].values())
    print('%s: candidatos %d | pasos en ficha %d | por marca: %s | suma: %d | PUENTE %d de %d = %.2f por ciento' % (k, len(cand[k]), n, dict(sorted(m[k].items())), t, m[k]['P'], t, 100.0 * m[k]['P'] / t))
g = sum(m.values(), collections.Counter())
print('los tres: por marca: %s | suma: %d | PUENTE %d de %d' % (dict(sorted(g.items())), sum(g.values()), g['P'], sum(g.values())))
