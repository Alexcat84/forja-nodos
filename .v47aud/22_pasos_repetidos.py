# -*- coding: utf-8 -*-
"""D.30 / P.19 al nivel del PASO: dos nodos que escriben el mismo renglon del
libro son gemelos aunque sus titulos difieran. Comparo los 45 pasos nuevos
entre si y contra los 30 pasos de los otros 8 candidatos de cap_04, por
solape de palabras normalizado. Publico la lista ordenada entera de los 12
pares mas altos: sin lista no se publica superlativo (mi ACTA 45 45.9.b)."""
import json, glob, re, sys, io, itertools
sys.path.insert(0, '.')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from src import comun
NUEVOS = set(l.strip().split('/')[-1] for l in open('.v47aud/02_candidatos_nuevos.out', encoding='utf-8') if l.strip())
pasos = []
for f in sorted(glob.glob('cuarentena/grove_high_output/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    if 'cap_04' not in d.get('resumen_teorico', ''):
        continue
    nuevo = f.split('/')[-1].replace(chr(92), '/').split('/')[-1] in NUEVOS
    for i, p in enumerate(d.get('pasos_accionables', []), 1):
        pasos.append((d['id'], i, nuevo, set(comun.normalizar_texto(p).split())))
print('pasos comparados: %d (de los %d candidatos de cap_04)'
      % (len(pasos), len(set(p[0] for p in pasos))))
print('  de ellos, nacidos en esta vuelta: %d' % sum(1 for p in pasos if p[2]))
pares = []
for (ia, na, va, sa), (ib, nb, vb, sb) in itertools.combinations(pasos, 2):
    if ia == ib or not (va or vb):
        continue
    j = len(sa & sb) / float(len(sa | sb)) if (sa | sb) else 0.0
    pares.append((j, ia, na, ib, nb))
pares.sort(reverse=True)
print()
print('LOS 12 PARES DE PASOS MAS PARECIDOS, LISTA ORDENADA ENTERA:')
for j, ia, na, ib, nb in pares[:12]:
    print('  %.4f  %s#%d  <->  %s#%d' % (j, ia[:44], na, ib[:44], nb))
print()
print('pares con solape 1.0 (paso identico): %d' % sum(1 for p in pares if p[0] >= 0.999))
