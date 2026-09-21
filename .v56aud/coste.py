# -*- coding: utf-8 -*-
"""El coste de esta corrida, leido de docs/loop/loop.log y de ningun otro sitio."""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
L = open('docs/loop/loop.log', encoding='utf-8').read().split('\n')
inicio = max(n for n, l in enumerate(L) if 'arranque: rama' in l)
print('ARRANQUE DE LA CORRIDA : %s' % L[inicio].strip())
pat = re.compile(r'^\[(\S+ \S+)\]\s+(extractor|auditor ciego|auditor) listo \(USD ([0-9.]+)\), (\d+)s')
vuelta = None
filas = []
for l in L[inicio:]:
    m = re.match(r'^\[\S+ \S+\] VUELTA (\d+) : (EXTRACTOR|AUDITOR|APERTURA CIEGA)', l)
    if m:
        vuelta = m.group(1)
    m = pat.match(l)
    if m:
        filas.append((vuelta, m.group(2), float(m.group(3)), int(m.group(4)), m.group(1)))
print()
print('%-7s %-14s %10s %8s  %s' % ('vuelta', 'turno', 'USD', 'seg', 'cerrado'))
pasan8 = pasan10 = 0
total = 0.0
for v, t, usd, seg, cu in filas:
    total += usd
    if usd > 8: pasan8 += 1
    if usd > 10: pasan10 += 1
    print('%-7s %-14s %10.4f %8d  %s' % (v, t, usd, seg, cu))
print()
print('TURNOS CERRADOS EN ESTA CORRIDA                 : %d' % len(filas))
print('TURNOS POR ENCIMA DE 8 USD                      : %d' % pasan8)
print('TURNOS POR ENCIMA DE 10 USD (D.56)              : %d' % pasan10)
print('GASTO SUMADO DE LA CORRIDA, SIN MI TURNO         : %.4f USD' % total)
ext = [f for f in filas if f[1] == 'extractor']
print()
print('EL TURNO DE EXTRACTOR, VUELTA A VUELTA, QUE ES LO QUE EL DISPARADOR MIDE:')
for v, t, usd, seg, cu in ext:
    print('  VUELTA %s (serial %s): %.4f USD   %s de 8' % (
        v, {'1': '54', '2': '55'}.get(v, '?'), usd, 'PASA' if usd > 8 else 'no pasa'))
print('  VUELTAS SEGUIDAS DE EXTRACTOR POR ENCIMA DE 8 USD: %d' % sum(1 for f in ext if f[2] > 8))
