# -*- coding: utf-8 -*-
"""ACTA 65: las restricciones de mi apertura sellada (.v66aud/restricciones_orden.txt) contra el orden del extractor
(.v66ext/orden.txt), y mis SOSTENGO contra sus SOSTENGO (.v66ext/aristas_lectura.txt), por par y con tramo."""
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')
orden = []
for l in io.open('.v66ext/orden.txt', encoding='utf-8'):
    m = re.match(r'^(\d+)\s+(\S+)\s+cap_04', l)
    if m: orden.append(m.group(2))
pos = {c: i + 1 for i, c in enumerate(orden)}
print('filas del orden: %d | tope 20, fuera: %s' % (len(orden), orden[20:]))
for l in io.open('.v66aud/restricciones_orden.txt', encoding='utf-8'):
    m = re.match(r'^\s+(\S+)\s+antes que (\S+)\s+(CONTINUA|arista por lectura|D\.36.*?)\s{2,}', l)
    if not m: continue
    a, b, por = m.groups()
    print('  %-53s (fila %2d) antes que %-54s (fila %2d) | %-18s | %s' % (a, pos[a], b, pos[b], por[:18], 'LA CUMPLE' if pos[a] < pos[b] else 'LA VIOLA'))
mias = {}
for f in [l.rstrip('\n').split('\t') for l in io.open('.v66aud/aristas_lectura.tsv', encoding='utf-8')][1:]:
    mias[(f[0], f[1])] = (f[2], f[3], f[4])
suyas = {}
for l in io.open('.v66ext/aristas_lectura.txt', encoding='utf-8'):
    if l.startswith('#') or '|' not in l: continue
    c = [x.strip() for x in l.split(' | ')]
    suyas[(c[1], c[2])] = (c[0], c[3])
print('mis filas: %d (SOSTENGO %d) | sus filas: %d (SOSTENGO %d)' % (len(mias), sum(v[0].startswith('SOSTENGO') for v in mias.values()), len(suyas), sum(v[0] == 'SOSTENGO' for v in suyas.values())))
for k in sorted(set(mias) | set(suyas)):
    m, s = mias.get(k), suyas.get(k)
    ms = m[0] if m else '(sin fila)'; ss = s[0] if s else '(sin fila)'
    igual = (ms.startswith('SOSTENGO') == (ss == 'SOSTENGO')) if (m and s) else False
    print('  %-4s %-50s > %-54s | mia %-14s | suya %-12s | tramo suyo: %s' % ('=' if igual else 'DIF', k[0], k[1], ms, ss, s[1] if s else '-'))
