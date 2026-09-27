# -*- coding: utf-8 -*-
"""Cuenta de pasos_accionables por candidato NACIDO en esta vuelta, y el total.
La clave es 'pasos_accionables', no 'pasos' (mi instrumento 04 preguntaba la mala)."""
import json, sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
NUEVOS = [l.strip() for l in open('.v47aud/02_candidatos_nuevos.out', encoding='utf-8') if l.strip()]
tot = 0
for ruta in NUEVOS:
    d = json.load(open(ruta, encoding='utf-8'))
    n = len(d.get('pasos_accionables', []))
    tot += n
    print('%3d  %s' % (n, d['id']))
print('---')
print('%3d  TOTAL de %d candidatos' % (tot, len(NUEVOS)))
