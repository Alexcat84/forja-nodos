# -*- coding: utf-8 -*-
"""Dos afirmaciones de mi apertura, comprobadas a maquina en vez de de memoria:
(a) el renglon L249 'Monitoring is not meddling' lo lleva UN solo nodo;
(b) cada una de las 6 fichas marca EXACTAMENTE UN discutible."""
import json, sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
NUEVOS = [l.strip() for l in open('.v47aud/02_candidatos_nuevos.out', encoding='utf-8') if l.strip()]
print('(a) que PASOS contienen la doctrina de "monitoring is not meddling":')
n = 0
for r in NUEVOS:
    d = json.load(open(r, encoding='utf-8'))
    for i, p in enumerate(d.get('pasos_accionables', []), 1):
        b = p.lower()
        if ('no es entrometerse' in b or 'no es intromision' in b
                or ('supervisar' in b and 'entrometer' in b)):
            n += 1
            print('    %s paso %d' % (d['id'], i))
print('    pasos que la llevan: %d' % n)
print()
print('(b) discutibles marcados por ficha:')
tot = 0
for r in NUEVOS:
    d = json.load(open(r, encoding='utf-8'))
    c = len(re.findall(r'DISCUTIBLE QUE MARCO', d.get('resumen_teorico', '')))
    tot += c
    print('    %-52s %d' % (d['id'][:52], c))
print('    TOTAL de discutibles marcados: %d' % tot)
