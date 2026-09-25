# -*- coding: utf-8 -*-
"""Vuelta 71: imprime titulo, condicion, entregable, pasos numerados y el DE DONDE SALE de las fichas de un capitulo de
.v71ext/los20.txt, para la relectura de fidelidad. Solo lee. python .v71ext/ver_fichas.py cap_10"""
import io, json, sys
cap = sys.argv[1]
for l in io.open('.v71ext/los20.txt', encoding='utf-8').read().split('\n')[1:]:
    if not l.startswith(cap + ' '): continue
    i = l.split()[1]
    d = json.load(io.open('cuarentena/grove_high_output/%s.json' % i, encoding='utf-8'))
    print('=====', i); print('T:', d['titulo']); print('C:', d['condiciones_activacion']); print('E:', d['entregable_esperado'])
    for k, p in enumerate(d['pasos_accionables'], 1): print(k, p)
    r = d['resumen_teorico']; j = r.find('DE DONDE SALE'); print('DS:', r[j:j + 2200] if j >= 0 else r[:2200])
    print('A:', d['atribuciones'])
