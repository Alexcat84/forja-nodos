"""ACTA 79: los pagos de d104 y d183 de la vuelta 80 en docs/loop/DEUDA.jsonl, contra el fichero del que el extractor dice que salio
cada como (.v80ext/como_<id>.txt). Imprime el como entero para leerlo contra la ACTA 78 78.3. Solo lee."""
import json, collections
L = [json.loads(l) for l in open('docs/loop/DEUDA.jsonl', encoding='utf-8') if l.strip()]
c = collections.Counter()
for d in ('d104', 'd183'):
    p = [x for x in L if x.get('id') == d and str(x.get('vuelta')) == '80']
    f = open('.v80ext/como_%s.txt' % d, encoding='utf-8').read().strip()
    for x in p:
        ok = x.get('como', '').strip() == f
        c['igual a su fichero' if ok else 'distinto de su fichero'] += 1
        print('%s | pago de la 80: SI | %s' % (d, 'igual a su fichero' if ok else 'DISTINTO de su fichero'))
        print('  como: %s' % x.get('como'))
print('pagos de la 80: %d | %s | suma: %d' % (sum(c.values()), dict(c), sum(c.values())))
