# -*- coding: utf-8 -*-
# PRIMERA LINEA, D.40 HEREDADO 4: CERO IDS TECLEADOS. La tanda sale de
# `git diff --name-only 74ddc8c HEAD -- cuarentena/_insertados/`; el resto se
# recorre por carpeta. Ninguna lista de nodos escrita a mano.
import io, json, os, subprocess, sys

def jl(ruta):
    return [json.loads(l) for l in io.open(ruta, encoding='utf-8') if l.strip()]

nodos = jl('dataset/nodos.jsonl')
print('nodos en dataset/nodos.jsonl            : %d' % len(nodos))
print('pasos totales del grafo                 : %d'
      % sum(len(n.get('pasos_accionables') or []) for n in nodos))
por_fuente = {}
for n in nodos:
    for f in (n.get('fuentes') or []):
        por_fuente[f.get('clave')] = por_fuente.get(f.get('clave'), 0) + 1
for k in sorted(por_fuente):
    print('  nodos con fuente %-24s: %d' % (k, por_fuente[k]))

band = sorted(f for f in os.listdir('cuarentena/scott_radical_candor') if f.endswith('.json'))
pb = 0
for f in band:
    pb += len(jl_ := json.load(io.open('cuarentena/scott_radical_candor/' + f, encoding='utf-8'))['pasos_accionables'])
print('bandeja cuarentena/scott_radical_candor : %d ficheros, %d pasos' % (len(band), pb))
ins = sorted(f for f in os.listdir('cuarentena/_insertados/scott_radical_candor') if f.endswith('.json'))
print('archivados _insertados/scott_radical_candor: %d ficheros' % len(ins))

salida = subprocess.check_output(
    ['git', 'diff', '--name-only', '74ddc8c', 'HEAD', '--', 'cuarentena/_insertados/'])
tanda = [r for r in salida.decode('utf-8').split('\n') if r.strip()]
print('TANDA DE LA VUELTA AUDITADA (del dato)  : %d ficheros' % len(tanda))
total = 0
for ruta in tanda:
    d = json.load(io.open(ruta, encoding='utf-8'))
    total += len(d['pasos_accionables'])
    print('  %-52s %2d pasos' % (d['id'], len(d['pasos_accionables'])))
print('pasos de la tanda                       : %d' % total)

ver = jl('bitacora/VEREDICTOS.jsonl')
print('lineas en bitacora/VEREDICTOS.jsonl     : %d' % len(ver))
