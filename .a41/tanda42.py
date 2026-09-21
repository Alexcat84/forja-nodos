# -*- coding: utf-8 -*-
import json, io, collections
L=[json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl',encoding='utf-8') if l.strip()]
print('lineas totales:', len(L))
t=L[514:729]
print('tanda 515..729:', len(t))
c=collections.Counter(x.get('veredicto') for x in t)
for k,v in sorted(c.items()): print('  ',k,v)
sin=[i+515 for i,x in enumerate(t) if not (x.get('razon') or '').strip()]
print('SIN RAZON ESCRITA:', len(sin), sin)
ar=[i+515 for i,x in enumerate(t) if (x.get('arista') or '').strip()]
print('con arista escrita:', len(ar))
se=[i+515 for i,x in enumerate(t) if x.get('levantada_por')]
print('levantados por SENIAL:', len(se))
print('declarados por LECTURA:', len(t)-len(se))
dis=[i+515 for i,x in enumerate(t) if 'DISCUTIBLE' in (x.get('razon') or '')]
print('razon dice DISCUTIBLE:', len(dis), dis)
# aristas distintas
pares=collections.Counter()
for x in t:
    a=(x.get('arista') or '').strip()
    if a: pares[a]+=1
print('ARISTAS DISTINTAS:', len(pares))
for k,v in pares.items():
    if v>1: print('   DOS VECES:', k, v)
