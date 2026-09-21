# -*- coding: utf-8 -*-
"""EL ORDEN DEL LIBRO de los 20 candidatos que quedan (EXTRACTOR.md 12.3)."""
import glob
import json
import os
import re

filas = []
for f in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    r = d.get('resumen_teorico', '')
    cap = sorted(set(re.findall(r'scott_radical_candor/(cap_\d+)\.md', r)))[0]
    anclas = [int(x) for x in re.findall(r'rotulo[^.]*?de la linea (\d+)', r)]
    m = re.search(r'[Ll]ineas?\s+(\d+)\s+a\s+(\d+)', r)
    ancla = anclas[0] if anclas else (int(m.group(1)) if m else 9999)
    filas.append((cap, ancla, os.path.basename(f)[:-5], len(d['pasos_accionables'])))
filas.sort()
print('%-4s %-7s %-6s %-6s %-56s %s' % ('#', 'cap', 'rotulo', 'pasos', 'id', ''))
for i, (cap, ancla, ident, pasos) in enumerate(filas, 1):
    print('%-4d %-7s L%-5d %-6d %s' % (i, cap, ancla, pasos, ident))
print('TOTAL: %d candidatos' % len(filas))
