# -*- coding: utf-8 -*-
"""Comprueba cada cita de la tabla SS.3.b del reporte de la vuelta 59 contra
la linea que dice citar, en fuentes/scott_radical_candor/cap_13.md.
No lee nada de .v59ext/: lee el REPORTE publicado y el libro."""
import re, unicodedata

LIBRO = 'fuentes/scott_radical_candor/cap_13.md'
libro = open(LIBRO, encoding='utf-8').read().split('\n')

# comillas tipograficas, guiones y puntos suspensivos, por su punto de codigo:
# el hook de esta casa prohibe escribirlos literales (manual seccion 2).
SIGNOS = [(chr(0x2018), "'"), (chr(0x2019), "'"), (chr(0x201c), '"'),
          (chr(0x201d), '"'), (chr(0x2014), '-'), (chr(0x2013), '-')]

def norm(t):
    t = unicodedata.normalize('NFKD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c))
    for a, b in SIGNOS:
        t = t.replace(a, b)
    return re.sub(r'[^a-z0-9]+', ' ', t.lower()).strip()

norm_libro = [norm(x) for x in libro]

rep = open('docs/loop/REPORTE.md', encoding='utf-8').read().split('\n')
ini = next(i for i, l in enumerate(rep) if l.startswith('### SS.3.b.'))
fin = next(i for i, l in enumerate(rep) if l.startswith('### SS.3.c.'))

nodo, filas = None, []
for l in rep[ini:fin]:
    m = re.match(r'\*\*`([a-z0-9_]+)` \(`(\d+)` pasos', l)
    if m:
        nodo = m.group(1)
    m = re.match(r'\|\s*`(P\d+)`\s*\|(.*?)\|\s*`L(\d+)`(.*)', l)
    if m:
        filas.append((nodo, m.group(1), int(m.group(3)), m.group(4)))

ok_n = malas = sin_cita = 0
print('%-52s %-4s %-6s %s' % ('nodo', 'paso', 'cita', 'donde esta de verdad'))
print('-' * 100)
for nodo, paso, ln, resto in filas:
    trozos = re.findall(r'\*(.+?)\*', resto)
    if not trozos:
        sin_cita += 1
        print('%-52s %-4s L%-5s SIN CITA LITERAL' % (nodo[:52], paso, ln))
        continue
    frag = norm(trozos[0].split('...')[0].split(chr(0x2026))[0])[:40]
    linea = norm_libro[ln - 1] if 0 < ln <= len(libro) else ''
    if frag and frag in linea:
        ok_n += 1
        continue
    malas += 1
    donde = [i + 1 for i, x in enumerate(norm_libro) if frag and frag in x]
    print('%-52s %-4s L%-5s %s' % (nodo[:52], paso, ln, donde or 'NINGUNA LINEA'))

print()
print('filas de cita leidas de SS.3.b        : %d' % len(filas))
print('citas que SI estan en la linea citada : %d' % ok_n)
print('citas que NO estan en la linea citada : %d' % malas)
print('filas sin cita literal comprobable    : %d' % sin_cita)
