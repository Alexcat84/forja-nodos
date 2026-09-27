# -*- coding: utf-8 -*-
"""ACTA 67: mis clases selladas en la fase ciega (.v68aud/mis_clases.tsv, un par sin orden por fila) contra las lineas del
extractor (.v68ext/veredictos_listos.txt, una por par dirigido candidato > vecino), par a par; y sus pares dirigidos contra
las filas > de mi barrido (.v68aud/vecinos_tabla.txt) sin las dos filas de cap_04."""
import io, re, collections
MIAS = {}
for l in list(io.open('.v68aud/mis_clases.tsv', encoding='utf-8'))[1:]:
    f = l.rstrip('\n').split('\t')
    MIAS[frozenset((f[0], f[1]))] = (f[2], f[3], 'DUDA' in f[4])
SUYAS = collections.defaultdict(list); dirig = set(); cur = None
for l in io.open('.v68ext/veredictos_listos.txt', encoding='utf-8'):
    l = l.rstrip('\n')
    if l.startswith('## '): cur = l[3:].strip(); continue
    if not cur or not l.strip() or l.startswith('#'): continue
    p = l.split('|')
    madre = p[2][6:] if p[1] == 'CONTINUA' else ''
    SUYAS[frozenset((cur, p[0]))].append((p[1], madre, cur, p[0]))
    dirig.add((cur, p[0]))
mio_dirig = set()
for l in io.open('.v68aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +> (\S+) ', l)
    if m and not m.group(1).startswith(('agrupar_interrupciones', 'canalizar_interrupciones')): mio_dirig.add(m.groups())
print('pares dirigidos: suyos %d | mios %d | solo suyos %s | solo mios %s' % (len(dirig), len(mio_dirig), sorted(dirig - mio_dirig), sorted(mio_dirig - dirig)))
print('pares sin orden: suyos %d | mios (sin los 8 de cap_04) %d' % (len(SUYAS), sum(1 for k in MIAS if not any(x.startswith(('agrupar_interrupciones', 'canalizar_interrupciones')) for x in k))))
incoh = [k for k, v in SUYAS.items() if len(set((x[0], x[1]) for x in v)) > 1]
print('pares suyos leidos desde los dos lados con clase o madre distinta: %d %s' % (len(incoh), [sorted(k) for k in incoh]))
cnt = collections.Counter(); dif = []
for k, v in sorted(SUYAS.items(), key=lambda kv: sorted(kv[0])):
    suya = (v[0][0], v[0][1]); mia = MIAS.get(k)
    if mia is None: dif.append(('SIN FILA MIA', sorted(k), suya)); continue
    igual = mia[0] == suya[0] and (mia[0] != 'CONTINUA' or mia[1] == suya[1])
    cnt[('igual' if igual else 'distinta', mia[2])] += 1
    if not igual: dif.append((sorted(k), 'mia %s %s%s' % (mia[0], mia[1], ' DUDA' if mia[2] else ''), 'suya %s %s' % suya))
print('pares con clase igual y madre igual: %d | distintos: %d | (igual/distinta, con duda mia): %s' % (
    sum(v for (a, b), v in cnt.items() if a == 'igual'), sum(v for (a, b), v in cnt.items() if a == 'distinta'), dict(cnt)))
for d in dif: print('  ', d)
print('clases suyas por linea: %s' % dict(collections.Counter(x[0] for v in SUYAS.values() for x in v)))
