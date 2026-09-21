# -*- coding: utf-8 -*-
"""LAS ARISTAS ESCRITAS EN LA VUELTA 42, contadas de bitacora/VEREDICTOS.jsonl."""
import json

APERTURA = 514   # lineas al abrir, medido en .v42/estado_apertura.txt

filas = [json.loads(l) for l in open('bitacora/VEREDICTOS.jsonl', encoding='utf-8')
         if l.strip()]
nuevos = filas[APERTURA:]
pares = [v['arista'] for v in nuevos if (v.get('arista') or '').strip()]
distintas = sorted(set(pares))
print('veredictos CONTINUA con arista escrita : %d' % len(pares))
print('ARISTAS DISTINTAS                      : %d' % len(distintas))
print('la diferencia son los pares emitidos DOS VECES, uno por cada lado:')
for p in distintas:
    n = pares.count(p)
    if n > 1:
        print('   %s   (%d veces)' % (p, n))
print()
for p in distintas:
    print('  %s' % p)
