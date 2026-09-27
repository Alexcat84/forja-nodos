# -*- coding: utf-8 -*-
"""Turno normal de la 70: las lineas que la vuelta escribio en la bitacora (905 a 1027), una a una, contra
(a) las lineas vivas de .v68ext/veredictos_listos.txt (sin las #), por par dirigido, clase, madre y razon letra a letra;
(b) mi barrido sellado de la 68 (.v68aud/vecinos_tabla.txt): el mismo conjunto de pares dirigidos;
(c) mis clases selladas (.v68aud/mis_clases.tsv) por par sin orden;
(d) las lineas de arista por lectura contra las SOSTENGO de .v68ext/aristas_lectura.txt (madre, hijo, paso) y contra
    mis SOSTENGO selladas de .v68aud/aristas_lectura.tsv, con la ACTA 67 67.4.d aplicada (agrupar_tareas > infundir).
Todo reparto en clases con su suma (R7). Solo lee."""
import io, re, sys, json, collections
sys.stdout.reconfigure(encoding="utf-8")
L = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8')][904:]
ver = [r for r in L if r.get('operacion') is None]
ari = [r for r in L if r.get('operacion') is not None]
k = collections.Counter('veredicto' if r.get('operacion') is None else r['operacion'] for r in L)
print('lineas nuevas: %d | por tipo: %s | suma: %d' % (len(L), dict(k), sum(k.values())))
# (a) lineas vivas
viva, cand = {}, None
for l in io.open('.v68ext/veredictos_listos.txt', encoding='utf-8'):
    l = l.rstrip('\n')
    if l.startswith('## '): cand = l[3:].strip(); continue
    if not l.strip() or l.startswith('#'): continue
    p = l.split('|')
    madre = p[2][6:] if len(p) > 3 and p[2].startswith('madre=') else ''
    viva[(cand, p[0])] = (p[1], madre, p[-1] if not madre else '|'.join(p[3:]))
est = collections.Counter(); malos = []
for r in ver:
    key = (r['candidato'], r['vecino']); v = viva.get(key)
    if v is None: est['sin linea viva'] += 1; malos.append(key); continue
    arista_esp = ('%s > %s' % (v[1], r['vecino'] if v[1] == r['candidato'] else r['candidato'])) if v[1] else ''
    ok = (r['veredicto'] == v[0] and r['razon'] == v[2] and r['arista'] == arista_esp)
    est['igual en clase, madre y razon' if ok else 'distinta'] += 1
    if not ok: malos.append((key, r['veredicto'], v[0], r['arista'], arista_esp, r['razon'] == v[2]))
print('(a) lineas de veredicto: %d | lineas vivas preparadas: %d | por estado: %s | suma: %d' % (len(ver), len(viva), dict(est), sum(est.values())))
print('    pares vivos sin linea en la bitacora: %s | lineas de la bitacora repetidas: %d' % (sorted(set(viva) - set((r['candidato'], r['vecino']) for r in ver)), len(ver) - len(set((r['candidato'], r['vecino']) for r in ver))))
for m in malos: print('    DISTINTA', m)
kc = collections.Counter(r['veredicto'] for r in ver)
print('    por clase: %s | suma: %d' % (dict(kc), sum(kc.values())))
# (b) mi barrido
los20 = set(io.open('.v68aud/los20.txt', encoding='utf-8').read().split())
mb = set()
for l in io.open('.v68aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +> (\S+) ', l)
    if m and m.group(1) in los20: mb.add(m.groups())
bi = set((r['candidato'], r['vecino']) for r in ver)
print('(b) pares dirigidos de mi barrido: %d | de la bitacora: %d | iguales: %d | solo mios: %s | solo suyos: %s' % (len(mb), len(bi), len(mb & bi), sorted(mb - bi), sorted(bi - mb)))
# (c) mis clases selladas
cl = {}
for l in list(io.open('.v68aud/mis_clases.tsv', encoding='utf-8'))[1:]:
    f = l.rstrip('\n').split('\t'); cl[tuple(sorted((f[0], f[1])))] = (f[2], f[3])
ec = collections.Counter(); dis = []
for r in ver:
    c = cl.get(tuple(sorted((r['candidato'], r['vecino']))))
    if c is None: ec['sin fila sellada'] += 1; continue
    madre_b = r['arista'].split(' > ')[0] if r['arista'] else ''
    if c[0] == r['veredicto'] and c[1] == madre_b: ec['igual clase y madre'] += 1
    else: ec['distinta'] += 1; dis.append((r['candidato'], r['vecino'], r['veredicto'], madre_b, c))
print('(c) lineas contra mis clases selladas: %s | suma: %d' % (dict(ec), sum(ec.values())))
for d in dis: print('    DISTINTA', d)
# (d) aristas por lectura
sost = {}
for l in io.open('.v68ext/aristas_lectura.txt', encoding='utf-8'):
    if l.startswith('SOSTENGO |'):
        p = [x.strip() for x in l.split('|')]
        sost[(p[1], p[2])] = int(re.search(r'madre paso (\d+)', p[3]).group(1))
mias = set()
for l in list(io.open('.v68aud/aristas_lectura.tsv', encoding='utf-8'))[1:]:
    f = l.rstrip('\n').split('\t')
    if f[2].startswith('SOSTENGO'): mias.add((f[0], f[1]))
mias.add(('agrupar_tareas_semejantes_aprovechar_preparacion', 'infundir_regularidad_reunion_proceso'))  # ACTA 67 67.4.d
ea = collections.Counter()
for r in ari:
    m, h = r['arista'].split(' > ')
    ok = (m, h) in sost and sost[(m, h)] == r['paso_citado'] and (m, h) in mias and r['veredicto'] == 'CONTINUA'
    ea['SOSTENGO suya y mia, mismo paso' if ok else 'distinta'] += 1
    print('    %-56s > %-45s paso %s | suya: %s | mia sellada: %s' % (m, h, r['paso_citado'], sost.get((m, h)), 'SI' if (m, h) in mias else 'NO'))
print('(d) lineas de arista por lectura: %d | por estado: %s | suma: %d | SOSTENGO suyas: %d | mias con 67.4.d: %d' % (len(ari), dict(ea), sum(ea.values()), len(sost), len(mias)))
