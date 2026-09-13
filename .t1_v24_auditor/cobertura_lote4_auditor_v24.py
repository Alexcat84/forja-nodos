# -*- coding: utf-8 -*-
"""COBERTURA DEL LOTE 4 MEDIDA POR EL AUDITOR.
Reparte los 142 candidatos del libro (bandeja mas insertados) por su UNIDAD DE
ORIGEN declarada en el resumen_teorico, y NO por cualquier mencion del rotulo:
una cita cruzada a otro capitulo no es una unidad minada.
"""
import io, os, glob, sys, re, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

LIBRO = 'scott_radical_candor'
unidades = sorted(os.path.basename(p)[:-3] for p in glob.glob('fuentes/%s/*.md' % LIBRO))
en_bandeja = sorted(glob.glob('cuarentena/%s/*.json' % LIBRO))
insertados = sorted(glob.glob('cuarentena/_insertados/%s/*.json' % LIBRO))
ficheros = en_bandeja + insertados

por_unidad = {u: [] for u in unidades}
sin_origen = []
# DOS LECTURAS, y publico las dos porque discrepan y la discrepancia es de
# METODO y no de dato: la ESTRICTA solo cuenta el rotulo UNIDAD DE ORIGEN, que
# las vueltas viejas no escribian; la ANCHA toma el primer cap_XX.md que el
# resumen nombra. La pregunta que las dos contestan igual es cual unidad esta
# a cero, que es la unica que decide si el lote cierra.
PAT = re.compile(r'UNIDAD DE ORIGEN:\s*fuentes/%s/(cap_\d+)\.md' % LIBRO)
PAT_ANCHA = re.compile(r'(cap_\d+)\.md')
por_unidad_ancha = {u: [] for u in unidades}
sin_ancha = []
for f in ficheros:
    d = json.load(io.open(f, encoding='utf-8'))
    m = PAT.search(d.get('resumen_teorico') or '')
    if m and m.group(1) in por_unidad:
        por_unidad[m.group(1)].append(d['id'])
    else:
        sin_origen.append(d['id'])
    ma = PAT_ANCHA.search(d.get('resumen_teorico') or '')
    if ma and ma.group(1) in por_unidad_ancha:
        por_unidad_ancha[ma.group(1)].append(d['id'])
    else:
        sin_ancha.append(d['id'])

print('unidades del lote 4                   : %d' % len(unidades))
print('candidatos leidos                     : %d  (bandeja %d + insertados %d)'
      % (len(ficheros), len(en_bandeja), len(insertados)))
print('candidatos sin UNIDAD DE ORIGEN legible: %d' % len(sin_origen))
if sin_origen:
    print('  ', sin_origen)
print()
print('%-9s %10s %10s' % ('unidad', 'estricta', 'ancha'))
sin = []
for u in unidades:
    n, na = len(por_unidad[u]), len(por_unidad_ancha[u])
    if na == 0:
        sin.append(u)
    print('%-9s %10d %10d' % (u, n, na))
print()
print('suma estricta / ancha                  : %d / %d'
      % (sum(len(v) for v in por_unidad.values()),
         sum(len(v) for v in por_unidad_ancha.values())))
print('sin rotulo estricto / sin cap_XX.md    : %d / %d' % (len(sin_origen), len(sin_ancha)))
print('unidades A CERO por las dos lecturas   : %d  %s' % (len(sin), sin))
