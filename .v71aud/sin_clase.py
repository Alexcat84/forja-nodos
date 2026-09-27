# -*- coding: utf-8 -*-
"""Fase ciega de la 71, ayuda de trabajo: las filas de vecino de .v71aud/vecinos_tabla.txt cuyo par todavia no tiene clase mia en
.v71aud/clases_intra.txt ni en .v71aud/clases_fuera.txt. Solo lee."""
import io, re, sys
sys.stdout.reconfigure(encoding="utf-8")
known = set(); ab = {}
for l in io.open('.v71aud/clases_intra.txt', encoding='utf-8'):
    if l.startswith('@'): k, v = l[1:].strip().split('='); ab[k] = v
    elif l.strip() and not l.startswith('#'): a, b = l.split('|')[:2]; known.add(tuple(sorted((ab[a], ab[b]))))
for l in io.open('.v71aud/clases_fuera.txt', encoding='utf-8'):
    if l.strip() and not l.startswith('#'): a, b = l.split('|')[:2]; known.add(tuple(sorted((a, b))))
for l in io.open('.v71aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +> (\S+) ', l)
    if m and tuple(sorted(m.group(1, 2))) not in known: print(l.rstrip())
