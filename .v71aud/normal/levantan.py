# ACTA 70: cuantas de las 20 levantan algun vecino en el barrido del extractor (.v71ext/vecinos_*.json), con la lista de .v71ext/los20.txt (columna del id). Solo lee.
import json, io, collections
ids = [l.split()[1] for l in io.open('.v71ext/los20.txt', encoding='utf-8') if l.strip() and not l.startswith('#')]
n = {c: len(json.load(io.open('.v71ext/vecinos_%s.json' % c, encoding='utf-8'))['vecinos']) for c in ids}
est = collections.Counter('levanta alguno' if v else 'no levanta ninguno' for v in n.values())
print('candidatos: %d | por estado: %s | suma: %d' % (len(n), dict(est), sum(est.values())))
print('no levantan:', sorted(c for c, v in n.items() if not v))
print('filas de vecino: %d' % sum(n.values()))
