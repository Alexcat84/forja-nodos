# -*- coding: utf-8 -*-
# Poblacion del barrido segun D.38.4 + D.38.5, criterio literal:
# "ENTRA EN LA POBLACION EL CANDIDATO CUYAS FUENTES ESTAN TODAS EN LA TABLA
#  CANONICA VIGENTE. Se descartan ademas _insertados y _derivadas."
# NINGUNA LISTA DE CARPETAS TECLEADA: la pertenencia se casa contra el dato.
import io, json, glob, os, collections

canon = json.load(io.open('fuentes/FUENTES_CANONICAS.json', encoding='utf-8'))
claves = set(k for k in canon if not k.startswith('_'))
grafo = [json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
todos = sorted(glob.glob('cuarentena/*/*.json'))
print('claves canonicas                      : %d' % len(claves))
print('nodos en dataset/nodos.jsonl          : %d' % len(grafo))
print('ficheros .json bajo cuarentena/       : %d' % len(todos))

dentro = []
fuera = collections.Counter()
for p in todos:
    q = p.replace(os.sep, '/')
    carpeta = q.split('/')[1]
    if '_insertados' in q or '_derivadas' in q:
        fuera['descartado por _insertados / _derivadas'] += 1
        continue
    d = json.load(io.open(p, encoding='utf-8'))
    fs = set(f.get('clave') for f in d.get('fuentes', []))
    if fs and fs <= claves:
        dentro.append((carpeta, d.get('id')))
    else:
        fuera['fuente FUERA de la tabla canonica en cuarentena/' + carpeta] += 1

for k in sorted(fuera):
    print('  EXCLUIDO %5d  %s' % (fuera[k], k))
print('candidatos de bandeja que ENTRAN      : %d' % len(dentro))
porb = collections.Counter(c for c, _ in dentro)
for k in sorted(porb):
    print('    bandeja %-26s %d' % (k, porb[k]))
print('POBLACION DEL BARRIDO (grafo+bandejas): %d' % (len(grafo) + len(dentro)))
print('   menos el propio candidato (ACTA 18): %d' % (len(grafo) + len(dentro) - 1))
