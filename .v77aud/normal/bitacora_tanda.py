# -*- coding: utf-8 -*-
"""Turno normal de la ACTA 76. Las lineas nuevas de la bitacora de la vuelta 77, una a una:
(1) cuantas hay desde la 1112 y de que tipo (veredicto de insertar o arista por lectura), con su suma (R7);
(2) las de veredicto contra la sede de lineas del extractor (.v77ext/veredictos_listos.txt, sin las #): vecino, clase y razon
    letra a letra; y contra las filas dirigidas de MI barrido de la 76 (.v76aud/vecinos_tabla.txt);
(3) su clase contra MIS clases selladas (.v76aud/mis_clases.tsv) con la adjudicacion (i) de la ACTA 75 75.4 (recorrer con
    construir es SANO por D.53) y la conjunta como mi lectura la mantiene (contratacion CONTINUA, madre construir);
(4) las de arista por lectura contra las filas SOSTENGO de .v77ext/aristas_lectura.txt y contra mis aristas esperadas
    (.v77aud/esperado_77.py), con su paso citado y su veredicto. Solo lee."""
import io, re, sys, json, collections
sys.stdout.reconfigure(encoding="utf-8")
L = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8')]
nuevas = L[1111:]
tipo = collections.Counter('arista por lectura' if 'operacion' in d else 'veredicto de insertar' for d in nuevas)
print('(1) lineas desde la 1112: %d | por tipo: %s | suma: %d' % (len(nuevas), dict(tipo), sum(tipo.values())))
# sede del extractor
listos = {}; cand = None
for l in io.open('.v77ext/veredictos_listos.txt', encoding='utf-8'):
    l = l.rstrip('\n')
    if l.startswith('## '): cand = l[3:].strip(); continue
    if not l.strip() or l.startswith('#'): continue
    f = l.split('|')
    madre = f[2][6:] if f[2].startswith('madre=') else ''
    razon = '|'.join(f[3:]) if madre else '|'.join(f[2:])
    listos[(cand, f[0])] = (f[1], madre, razon)
ver = [d for d in nuevas if 'operacion' not in d]
cmp = collections.Counter(); malas = []
for d in ver:
    k = (d['candidato'], d['vecino'])
    if k not in listos: cmp['sin linea en la sede'] += 1; malas.append(k); continue
    c, madre, razon = listos[k]
    ok = c == d['veredicto'] and razon.strip() == d['razon'].strip()
    if c == 'CONTINUA':
        ok = ok and d['arista'] in ('', '%s > %s' % (madre, d['vecino'] if madre == d['candidato'] else d['candidato']))
    cmp['igual en clase y razon' if ok else 'DISTINTA'] += 1
    if not ok: malas.append(k)
print('(2) lineas de veredicto contra su sede: %s | suma: %d | distintas: %s' % (dict(cmp), sum(cmp.values()), malas))
print('    lineas de la sede sin linea en la bitacora: %d' % len(set(listos) - set((d['candidato'], d['vecino']) for d in ver)))
barr = set()
las22 = set(io.open('.v76aud/las22.txt', encoding='utf-8').read().split())
for l in io.open('.v76aud/vecinos_tabla.txt', encoding='utf-8'):
    m = re.match(r'^    (\S+) +> (\S+) ', l)
    if m and m.group(1) in las22: barr.add(m.groups())
vk = [(d['candidato'], d['vecino']) for d in ver]
print('    filas dirigidas: bitacora %d (distintas %d) | mi barrido %d | iguales: %s' % (len(vk), len(set(vk)), len(barr), 'SI' if set(vk) == barr else 'NO'))
# mis clases
RC = tuple(sorted(('recorrer_siete_pasos_programa_desarrollo_negocio', 'construir_estrategia_gente_cuatro_componentes')))
cl = {}
for l in list(io.open('.v76aud/mis_clases.tsv', encoding='utf-8'))[1:]:
    f = l.rstrip('\n').split('\t'); p = tuple(sorted((f[0], f[1])))
    cl[p] = ('SANO', '') if p == RC else (f[2], f[3])
cc = collections.Counter(); dif = []
for d in ver:
    p = tuple(sorted((d['candidato'], d['vecino']))); c, madre = cl.get(p, ('SIN FILA', ''))
    ok = c == d['veredicto']
    if ok and c == 'CONTINUA':
        hijo = p[1] if p[0] == madre else p[0]
        ok = d['arista'] in ('', '%s > %s' % (madre, hijo))
    cc['mi clase y madre' if ok else 'DISTINTA'] += 1
    if not ok: dif.append((d['candidato'], d['vecino'], d['veredicto'], c))
print('(3) contra mis clases selladas (con 75.4 (i) y la conjunta como la mantengo): %s | suma: %d | distintas: %s' % (dict(cc), sum(cc.values()), dif))
cv = collections.Counter(d['veredicto'] for d in ver)
print('    lineas de veredicto por clase: %s | suma: %d' % (dict(cv), sum(cv.values())))
con = [d for d in ver if d['veredicto'] == 'CONTINUA']
for d in con: print('      CONTINUA %s ~ %s | arista: %s' % (d['candidato'], d['vecino'], d['arista'] or '(vacia)'))
# aristas por lectura
sost = {}
for l in io.open('.v77ext/aristas_lectura.txt', encoding='utf-8'):
    if l.startswith('SOSTENGO |'):
        f = [x.strip() for x in l.split('|')]
        m = re.match(r'madre paso (\d+)', f[3]); sost[(f[1], f[2])] = int(m.group(1)) if m else None
ar = [d for d in nuevas if 'operacion' in d]
ca = collections.Counter()
for d in ar:
    m_, h_ = [x.strip() for x in d['arista'].split('>')]
    ok = (m_, h_) in sost and sost[(m_, h_)] == d['paso_citado'] and d['candidato'] == h_ and d['vecino'] == m_
    ca['con su fila SOSTENGO y su paso' if ok else 'DISTINTA'] += 1
    print('    %-9s paso %2s | %s > %s | fila SOSTENGO paso %s' % (d['veredicto'], d['paso_citado'], m_, h_, sost.get((m_, h_))))
print('(4) aristas por lectura: %d | %s | suma: %d | filas SOSTENGO en la sede: %d' % (len(ar), dict(ca), sum(ca.values()), len(sost)))
