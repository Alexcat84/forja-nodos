# ACTA 70: PASOS INVENTADOS POR CAPITULO desde la fidelidad del extractor (.v71ext/fidelidad.tsv), con los 4 PUENTE que
# la ACTA 70 70.4 sostiene, una fila por capitulo y su suma (R7). El capitulo sale de la ficha de la bandeja. Solo lee.
import io, json, collections
cap = {}
for l in io.open('.v71ext/los20.txt', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    c, i, n = l.split(); cap[i] = c
cnt = collections.defaultdict(collections.Counter); cands = collections.defaultdict(set)
for l in io.open('.v71ext/fidelidad.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    f = [x.strip() for x in l.split('|')]
    cnt[cap[f[0]]][f[2]] += 1; cands[cap[f[0]]].add(f[0])
tot = collections.Counter()
for c in sorted(cnt):
    t = cnt[c]; s = sum(t.values()); tot.update(t)
    print('%s: candidatos %d | por marca: %s | suma: %d | PUENTE %d de %d = %.2f por ciento' % (c, len(cands[c]), dict(sorted(t.items())), s, t['P'], s, 100.0 * t['P'] / s))
s = sum(tot.values())
print('los seis: por marca: %s | suma: %d | PUENTE %d de %d = %.2f por ciento' % (dict(sorted(tot.items())), s, tot['P'], s, 100.0 * tot['P'] / s))
