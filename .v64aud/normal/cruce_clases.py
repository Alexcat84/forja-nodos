# -*- coding: utf-8 -*-
"""Cruza, par a par, las clases de mi apertura sellada (docs/loop/APERTURA_CIEGA.md, filas de tabla de
las secciones 5, 6 y 7) contra las lineas de .v64ext/veredictos_listos.txt y las filas de
.v64ext/aristas_lectura.txt. Un par es no ordenado. Clases: CONTINUA, SANO, NO SOSTENIDA (arista leida y
no sostenida, que para el cruce cuenta igual que SANO). Las abreviaturas de la apertura (`emparejar...`)
se resuelven por prefijo contra los ids que aparecen en las dos sedes del extractor."""
import io, re

CONOCIDOS = set()
for f in ('.v64ext/veredictos_listos.txt', '.v64ext/aristas_lectura.txt'):
    CONOCIDOS |= set(re.findall(r'\b([a-z0-9]+(?:_[a-z0-9]+){2,})\b', io.open(f, encoding='utf-8').read()))


def resuelve(t):
    if t in CONOCIDOS:
        return t
    c = [k for k in CONOCIDOS if k.startswith(t)]
    return c[0] if len(c) == 1 else None


def ids(s):
    return [x for x in (resuelve(t) for t in re.findall(r'`([a-z0-9]+(?:_[a-z0-9]+)*)(?:\.\.\.)?`', s)) if x]


def clase(t):
    if 'CONTINUA' in t:
        return 'CONTINUA'
    if 'SANO' in t:
        return 'SANO'
    return None


ciega = {}
for l in io.open('docs/loop/APERTURA_CIEGA.md', encoding='utf-8'):
    if not l.startswith('| `'):
        continue
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) < 3:
        continue
    a, b = ids(c[0]), ids(c[1])
    if len(a) >= 2:                                   # secciones 5 y 6: par | [estado |] clase | ...
        cl = clase(c[1]) or clase(c[2])
        if cl:
            ciega[frozenset(a[:2])] = cl
    elif len(a) == 1 and len(b) == 1:                 # seccion 7: madre | hijo | ... | confianza
        conf = c[-1]
        ciega[frozenset([a[0], b[0]])] = 'NO SOSTENIDA' if ('No la sostengo' in conf or 'baja' in conf) else 'CONTINUA'

ext, cur = {}, None
for l in io.open('.v64ext/veredictos_listos.txt', encoding='utf-8'):
    if l.startswith('## '):
        cur = l[3:].strip()
    elif cur and '|' in l and not l.startswith('#'):
        v, cl = l.split('|')[:2]
        ext.setdefault(frozenset([cur, v.strip()]), set()).add(cl.strip())
for l in io.open('.v64ext/aristas_lectura.txt', encoding='utf-8'):
    m = re.match(r'(SOSTENGO|NO SOSTENGO)\s*\|\s*(\S+)\s*\|\s*(\S+)', l.strip())
    if m:
        ext.setdefault(frozenset([m.group(2), m.group(3)]), set()).add('CONTINUA' if m.group(1) == 'SOSTENGO' else 'NO SOSTENIDA')

coinc = disc = solo = 0
for p in sorted(ext, key=lambda s: sorted(s)):
    e = ext[p]
    e = 'CONTINUA' if 'CONTINUA' in e else ('SANO' if 'SANO' in e else 'NO SOSTENIDA')
    c = ciega.get(p)
    if c is None:
        solo += 1
        print('SIN LECTURA CIEGA  %-12s %s' % (e, ' | '.join(sorted(p))))
    elif c == e or {c, e} <= {'SANO', 'NO SOSTENIDA'}:
        coinc += 1
    else:
        disc += 1
        print('DISCREPA  ciega %-12s extractor %-12s %s' % (c, e, ' | '.join(sorted(p))))
print('pares del extractor (veredictos listos y aristas): %d | con lectura ciega mia: %d | coinciden: %d | discrepan: %d | sin lectura ciega: %d'
      % (len(ext), coinc + disc, coinc, disc, solo))
print('pares en tablas de la apertura sellada: %d | de ellos sin par en las sedes del extractor: %d' % (len(ciega), len(set(ciega) - set(ext))))
for p in sorted(set(ciega) - set(ext), key=lambda s: sorted(s)):
    print('   SOLO EN LA APERTURA  %-12s %s' % (ciega[p], ' | '.join(sorted(p))))
