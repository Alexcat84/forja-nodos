# -*- coding: utf-8 -*-
import re
F = 'fuentes/scott_radical_candor/cap_10.md'
L = open(F, encoding='utf-8').read().split('\n')
for i, l in enumerate(L[7:], start=8):
    if not l.strip():
        continue
    w = len(l.split())
    txt = l.strip()
    txt = (txt[:110] + '...') if len(txt) > 110 else txt
    print("%4d  %5d  %s" % (i, w, txt))
