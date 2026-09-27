# -*- coding: utf-8 -*-
"""LA TANDA DE VEREDICTOS DE LA VUELTA 42, contada de bitacora/VEREDICTOS.jsonl."""
import collections
import json

APERTURA = 514   # lineas al abrir, medido en .v42/estado_apertura.txt

filas = [json.loads(l) for l in open('bitacora/VEREDICTOS.jsonl', encoding='utf-8')
         if l.strip()]
nuevos = filas[APERTURA:]
clases = collections.Counter(v.get('veredicto') or 'sin clase' for v in nuevos)
sin_razon = [v for v in nuevos if not (v.get('razon') or '').strip()]
aristas = [v for v in nuevos if (v.get('arista') or '').strip()]
senial = [v for v in nuevos if 'lectura declarada' not in str(v.get('levantada_por'))]
print('lineas al abrir                    : %d' % APERTURA)
print('lineas al cerrar                   : %d' % len(filas))
print('veredictos escritos en esta vuelta : %d' % len(nuevos))
for c, n in sorted(clases.items()):
    print('  %-28s : %d' % (c, n))
print('con arista escrita                 : %d' % len(aristas))
print('levantados por una SENIAL          : %d' % len(senial))
print('declarados por LECTURA             : %d' % (len(nuevos) - len(senial)))
print('SIN RAZON ESCRITA                  : %d   <-- tiene que salir 0' % len(sin_razon))
