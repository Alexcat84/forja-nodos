# -*- coding: utf-8 -*-
# PASOS ESCRITOS POR CAPITULO. La unidad de origen NO se teclea: se lee del
# propio resumen_teorico de cada candidato, casando la ruta fuentes/<libro>/cap_NN.md
# que el fichero declara. Si un candidato declarase dos, el instrumento lo dice.
import io, json, glob, os, re, collections

RUTA = re.compile(r'fuentes/([a-z0-9_]+)/(cap_\d\d)\.md')
libro = 'grove_high_output'
filas = []
for p in sorted(glob.glob('cuarentena/%s/*.json' % libro), key=os.path.getmtime):
    d = json.load(io.open(p, encoding='utf-8'))
    caps = sorted(set(m.group(2) for m in RUTA.finditer(d.get('resumen_teorico', ''))
                      if m.group(1) == libro))
    filas.append((d['id'], len(d.get('pasos_accionables', [])), caps))

print('candidatos leidos de cuarentena/%s : %d' % (libro, len(filas)))
print('%-52s %5s  %s' % ('id', 'pasos', 'cap_NN citados en su resumen'))
for i, n, caps in filas:
    print('%-52s %5d  %s' % (i, n, ','.join(caps) if caps else 'NINGUNO'))

por_cap = collections.Counter()
nodos_cap = collections.Counter()
ambiguos = []
for i, n, caps in filas:
    if len(caps) == 1:
        por_cap[caps[0]] += n
        nodos_cap[caps[0]] += 1
    else:
        ambiguos.append((i, caps))
print()
print('PASOS ESCRITOS POR CAPITULO (solo los de unidad unica):')
for c in sorted(por_cap):
    print('  %s  nodos %2d  pasos %3d' % (c, nodos_cap[c], por_cap[c]))
print('  TOTAL           nodos %2d  pasos %3d' % (sum(nodos_cap.values()), sum(por_cap.values())))
print('candidatos que citan mas de un cap_NN o ninguno: %d' % len(ambiguos))
for i, caps in ambiguos:
    print('    %s -> %s' % (i, caps))
