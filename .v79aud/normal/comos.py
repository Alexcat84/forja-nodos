# -*- coding: utf-8 -*-
"""ACTA 78: los cinco pagos de la 79 en DEUDA.jsonl contra sus ficheros de .v79ext/como_<id>.txt. Solo lee."""
import json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
pagos = {}
for l in io.open('docs/loop/DEUDA.jsonl', encoding='utf-8'):
    d = json.loads(l)
    if d.get('tipo') == 'pago' and str(d.get('vuelta')) == '79': pagos[d['id']] = d['como']
res = {}
for i in ('d150', 'd180', 'd098', 'd099', 'd135'):
    f = io.open('.v79ext/como_%s.txt' % i, encoding='utf-8').read().rstrip('\n')
    k = 'igual a su fichero' if pagos.get(i) == f else 'DISTINTO'
    res[k] = res.get(k, 0) + 1
    print('%s | pago de la 79: %s | %s' % (i, 'SI' if i in pagos else 'NO', k))
print('pagos de la 79: %d | %s | suma: %d' % (len(pagos), res, sum(res.values())))
