# -*- coding: utf-8 -*-
"""ACTA 68: la correccion declarada de la vuelta 69 en .v68ext/, par a par.
(1) veredictos_listos.txt en 08eb797 (commit de la ACTA 67) contra HEAD: que pares dirigidos cambian de clase o madre,
    cuales solo de razon, y que cada linea quitada sigue letra a letra dentro de un comentario '# vuelta 69'.
(2) sus clases de hoy contra las mias selladas en la 68 (.v68aud/mis_clases.tsv), par sin orden.
(3) aristas_lectura.txt igual, fila a fila, y sus SOSTENGO mas sus CONTINUA de hoy contra las 7 de .v69aud/aristas_70.py.
Toda linea que reparte en clases trae su suma (R7). Solo lee."""
import io, sys, subprocess, collections
sys.stdout.reconfigure(encoding='utf-8')
def show(rev, path):
    return subprocess.run(['git', 'show', '%s:%s' % (rev, path)], capture_output=True).stdout.decode('utf-8')
def now(path): return io.open(path, encoding='utf-8').read()
def ver(txt):
    d = {}; cur = None
    for l in txt.split('\n'):
        l = l.rstrip('\r')
        if l.startswith('## '): cur = l[3:].strip(); continue
        if not cur or not l.strip() or l.startswith('#'): continue
        p = l.split('|')
        d[(cur, p[0])] = (p[1], p[2][6:] if p[1] == 'CONTINUA' else '', l)
    return d
V = '.v68ext/veredictos_listos.txt'; A = '.v68ext/aristas_lectura.txt'
vo, vn = ver(show('08eb797', V)), ver(now(V))
print('(1) veredictos: pares dirigidos antes %d | hoy %d | nuevos %d | desaparecidos %d' % (len(vo), len(vn), len(set(vn) - set(vo)), len(set(vo) - set(vn))))
cambio = collections.Counter(); filas = []
for k in sorted(vo):
    a, b = vo[k], vn.get(k)
    if b is None: continue
    if (a[0], a[1]) != (b[0], b[1]): cambio['clase o madre'] += 1; filas.append('  %-48s > %-48s %s %s -> %s' % (k[0], k[1], a[0], a[1], b[0]))
    elif a[2] != b[2]: cambio['solo razon'] += 1
    else: cambio['igual'] += 1
print('    por estado: %s | suma: %d' % (dict(cambio), sum(cambio.values())))
for f in filas: print(f)
madres = collections.Counter(v[1] for v in vn.values() if v[0] == 'CONTINUA')
print('    CONTINUA de hoy por madre: %s | suma: %d' % (dict(madres), sum(madres.values())))
def quitadas(old, new):
    o = [l.rstrip('\r') for l in old.split('\n')]; n = [l.rstrip('\r') for l in new.split('\n')]
    ns = set(n); q = [l for l in o if l.strip() and l not in ns]
    com = [l for l in n if l.startswith('# vuelta 69')]
    dentro = [l for l in q if any(c.endswith(': ' + l) for c in com)]
    return len(q), len(dentro), len(com)
q, d, c = quitadas(show('08eb797', V), now(V))
print('    lineas quitadas: %d | presentes enteras al final de un comentario # vuelta 69: %d | comentarios # vuelta 69: %d' % (q, d, c))
# (2)
MIAS = {}
for l in list(io.open('.v68aud/mis_clases.tsv', encoding='utf-8'))[1:]:
    f = l.rstrip('\n').split('\t'); MIAS[frozenset((f[0], f[1]))] = (f[2], f[3])
SUY = collections.defaultdict(set)
for (c_, v_), (cl, m, _) in vn.items(): SUY[frozenset((c_, v_))].add((cl, m))
inc = [k for k, v in SUY.items() if len(v) > 1]
r = collections.Counter(); dis = []
for k, v in SUY.items():
    s = next(iter(v)); mia = MIAS.get(k)
    if mia is None: r['sin fila mia'] += 1; dis.append(sorted(k)); continue
    ok = mia[0] == s[0] and (s[0] != 'CONTINUA' or mia[1] == s[1])
    r['igual' if ok else 'distinta'] += 1
    if not ok: dis.append((sorted(k), mia, s))
print('(2) pares sin orden suyos hoy: %d | leidos desde los dos lados con clase distinta: %d | contra mis clases selladas: %s | suma: %d' % (len(SUY), len(inc), dict(r), sum(r.values())))
for x in dis: print('   ', x)
# (3)
def ari(txt):
    d = {}
    for l in txt.split('\n'):
        l = l.rstrip('\r')
        if l.startswith('#') or ' | ' not in l: continue
        p = l.split(' | ')
        for h in p[2].split(', '): d[(p[1], h)] = p[0]
    return d
ao, an = ari(show('08eb797', A)), ari(now(A))
ch = [(k, ao[k], an.get(k)) for k in sorted(ao) if ao[k] != an.get(k)]
cl = collections.Counter(an.values())
print('(3) aristas por lectura: pares antes %d | hoy %d | que cambian de clase: %d' % (len(ao), len(an), len(ch)))
for k, a, b in ch: print('  %-48s > %-48s %s -> %s' % (k[0], k[1], a, b))
print('    pares de hoy por clase: %s | suma: %d' % (dict(cl), sum(cl.values())))
q, d, c = quitadas(show('08eb797', A), now(A))
print('    lineas quitadas: %d | presentes enteras al final de un comentario # vuelta 69: %d | comentarios # vuelta 69: %d' % (q, d, c))
suyas = set((v[1], k[0] if v[1] != k[0] else k[1]) for k, v in vn.items() if v[0] == 'CONTINUA') | set(k for k, v in an.items() if v == 'SOSTENGO')
out = subprocess.run([sys.executable, '.v69aud/aristas_70.py'], capture_output=True).stdout.decode('utf-8')
mias = set(tuple(x.split()[1::2][:2]) for x in out.split('\n') if x.startswith(('  CONTINUA', '  SOSTENGO')))
print('    aristas esperadas en la 70: suyas %d | mias selladas %d | iguales %d | solo suyas %s | solo mias %s' % (len(suyas), len(mias), len(suyas & mias), sorted(suyas - mias), sorted(mias - suyas)))
