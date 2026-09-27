# -*- coding: utf-8 -*-
"""Resumen de lectura de un insertar de la vuelta 67, para decidir antes de mover nada:
    python .v67ext/mirar.py <fila> <id>
Dice si entro, cuantos vecinos levanto, cuales no tenian linea, cuales lineas no tuvieron vecino, y las aristas."""
import io, re, sys
f, cid = sys.argv[1:3]
t = io.open('.v67ext/insertar_%s_%s.txt' % (f, cid), encoding='utf-8').read()
vec = re.findall(r'\n  vecino (\S+)  \[', t)
lin = [a.strip() for a in re.findall(r'\n  --veredicto ([^|]+)\|', t)]
print('INSERTADO' if 'NODO INSERTADO' in t else 'NO INSERTADO', '|', re.search(r'fin .*', t).group(0))
print('vecinos %d | lineas %d | vecinos sin linea %s | lineas sin vecino %s' % (
    len(vec), len(lin), [v for v in vec if v not in lin] or 0, [l for l in lin if l not in vec] or 0))
for l in t.split('\n'):
    if re.search(r'ARISTA|arista madre-hijo|CAERIA|CERROJO|Error|ERROR|Traceback', l):
        print('  ' + l.strip()[:200])
