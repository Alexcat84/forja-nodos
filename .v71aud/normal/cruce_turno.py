# ACTA 70, turno normal: mis clases selladas (.v71aud/mis_clases.tsv) contra las lineas del extractor
# (.v71ext/veredictos_listos.txt), par a par; y mi fidelidad sellada (.v71aud/fidelidad.tsv) contra la suya
# (.v71ext/fidelidad.tsv), paso a paso. Solo lee.
import collections, csv
def norm(p): return tuple(sorted(p))
# --- sus lineas
suyas = []  # (candidato, vecino, clase, madre)
cand = None
for l in open('.v71ext/veredictos_listos.txt', encoding='utf-8'):
    l = l.rstrip('\n')
    if l.startswith('## '): cand = l[3:].strip(); continue
    if not l or l.startswith('#'): continue
    c = l.split('|')
    madre = c[2][6:] if len(c) > 3 and c[2].startswith('madre=') else ''
    suyas.append((cand, c[0], c[1], madre))
print('sus lineas:', len(suyas), '| por clase:', dict(collections.Counter(s[2] for s in suyas)), '| suma:', len(suyas))
por_par = collections.defaultdict(list)
for s in suyas: por_par[norm((s[0], s[1]))].append(s)
print('sus pares sin orden:', len(por_par))
# --- mis clases
mias = {}
for r in csv.DictReader(open('.v71aud/mis_clases.tsv', encoding='utf-8'), delimiter='\t'):
    mias[norm((r['a'], r['b']))] = (r['clase'], r['madre'])
print('mis filas:', len(mias), '| pares solo suyos:', sorted(set(por_par) - set(mias)), '| solo mios:', sorted(set(mias) - set(por_par)))
est = collections.Counter(); dif = []
for p in sorted(por_par):
    cl = {s[2] for s in por_par[p]}; md = {s[3] for s in por_par[p]}
    cl_s = cl.pop() if len(cl) == 1 else '/'.join(sorted(cl)); md_s = '/'.join(sorted(md))
    mc, mm = mias[p]
    if cl_s == mc and md_s == mm: est['igual clase y madre'] += 1
    else: est['distinto'] += 1; dif.append((p, cl_s, md_s, mc, mm, len(por_par[p])))
print('pares:', dict(est), '| suma:', sum(est.values()))
for p, cs, ms, mc, mm, n in dif:
    print('  DISTINTO', p[0], '~', p[1], '| suya:', cs, ms or '-', '(%d lineas)' % n, '| mia sellada:', mc, mm or '-')
# --- fidelidad
def leer(ruta, sep):
    out = {}
    for l in open(ruta, encoding='utf-8'):
        if l.startswith('#') or not l.strip() or l.startswith('id\t'): continue
        c = [x.strip() for x in l.split(sep)]
        out[(c[0], int(c[1]))] = c[2]
    return out
su = leer('.v71ext/fidelidad.tsv', '|'); mi = leer('.v71aud/fidelidad.tsv', '\t')
print('fidelidad: sus filas', len(su), '| mis filas', len(mi), '| solo suyas', sorted(set(su) - set(mi)), '| solo mias', sorted(set(mi) - set(su)))
cr = collections.Counter((su[k], mi[k]) for k in su if k in mi)
print('fidelidad (suya, mia):', dict(sorted(cr.items())), '| suma:', sum(cr.values()))
for k in sorted(su):
    if k in mi and su[k] != mi[k]: print('  ', k[0], 'paso', k[1], '| suya', su[k], '| mia', mi[k])
