# -*- coding: utf-8 -*-
"""PASOS INVENTADOS POR CAPITULO (AUDITOR_FORJA.md 8) para un lote.
La tabla SE IMPRIME desde el instrumento, no se teclea (D.41)."""
import json, glob, io, re, sys, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
lote = sys.argv[1]
filas = {}
for pat in ('cuarentena/%s/*.json' % lote, 'cuarentena/_insertados/%s/*.json' % lote):
    for f in glob.glob(pat):
        d = json.load(open(f, encoding='utf-8'))
        caps = sorted(set(re.findall(r'cap_\d+', json.dumps(d, ensure_ascii=False))))
        cap = caps[0] if caps else 'SIN_UNIDAD'
        n = len(d.get('pasos_accionables') or [])
        filas.setdefault(cap, {'cand': 0, 'pasos': 0, 'ids': []})
        filas[cap]['cand'] += 1; filas[cap]['pasos'] += n; filas[cap]['ids'].append(d['id'])
        if len(caps) > 1: filas[cap]['ids'][-1] += '  (!! nombra %s)' % ','.join(caps)
print('LOTE:', lote)
print('%-10s %5s %6s   %s' % ('unidad', 'cand', 'pasos', 'ids'))
tc = tp = 0
for cap in sorted(filas):
    v = filas[cap]; tc += v['cand']; tp += v['pasos']
    print('%-10s %5d %6d   %s' % (cap, v['cand'], v['pasos'], ', '.join(sorted(v['ids']))))
print('%-10s %5d %6d' % ('TOTAL', tc, tp))
