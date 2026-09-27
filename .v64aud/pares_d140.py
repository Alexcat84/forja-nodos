# -*- coding: utf-8 -*-
"""Pares distintos (sin orden) que levantan los candidatos BLOQUEARIA de la salida de
.v63aud/vecinos.py (poblacion 462). Un par levantado desde los dos lados cuenta una vez."""
import subprocess, sys
sal = subprocess.run([sys.executable, '.v63aud/vecinos.py'], capture_output=True, text=True, encoding='utf-8').stdout
pares, cand, bloq = set(), None, 0
for l in sal.splitlines():
    if l.startswith('BLOQUEARIA'): cand = l.split()[1]; bloq += 1
    elif l.startswith('ENTRARIA') or l.startswith('SIN'): cand = None
    elif cand and l.startswith('    '): pares.add(tuple(sorted((cand, l.split()[0]))))
print('candidatos BLOQUEARIA: %d | pares distintos: %d' % (bloq, len(pares)))
for a, b in sorted(pares): print('   ', a, '|', b)
