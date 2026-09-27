# -*- coding: utf-8 -*-
"""ACTA 77: su orden (.v78ext/orden.txt, filas 1 a 20) contra las restricciones que mi fase ciega sello
(python .v78aud/restricciones_orden.py, APERTURA_CIEGA.md 7). Cuenta todas las clases con el mismo predicado y dice su suma (R7). Solo lee."""
import io, re, subprocess, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
pos = {}
for l in io.open('.v78ext/orden.txt', encoding='utf-8'):
    m = re.match(r'^(\d+)\s+(\S+)\s+cap_', l)
    if m: pos[m.group(2)] = int(m.group(1))
out = subprocess.run([sys.executable, '.v78aud/restricciones_orden.py'], capture_output=True, text=True, encoding='utf-8').stdout
c = collections.Counter()
for l in out.splitlines():
    m = re.match(r'^\s+(\S+)\s+antes que (\S+)\s+(arista por lectura|D\.36)', l)
    if not m: continue
    a, b, t = m.groups()
    ok = pos[a] < pos[b]
    c['%s, %s' % ('obliga' if t.startswith('arista') else 'D.36 de un lado', 'la cumple' if ok else 'LA VIOLA')] += 1
    print('  %-52s (fila %2d) antes que %-52s (fila %2d) | %s' % (a, pos[a], b, pos[b], 'la cumple' if ok else 'LA VIOLA'))
print('filas del orden: %d | restricciones: %s | suma: %d' % (len(pos), dict(c), sum(c.values())))
