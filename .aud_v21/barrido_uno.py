# BARRIDO D.38.4 DEL AUDITOR, VUELTA 21, DE UN SOLO CANDIDATO.
# Se invoca con el id del candidato. La poblacion es grafo MAS bandejas,
# descartando _insertados, _derivadas y el catalogo de control
# ensayo_referencia_163 (sin clave en la tabla canonica). Mismo medidor que la
# aduana y mismos umbrales que carga la casa.
import json
import sys
import glob
import os
import time
sys.path.insert(0, '.')
from src import aduana

FUERA = ('_insertados', '_derivadas', 'ensayo_referencia_163')
cual = sys.argv[1]

umbrales = json.load(open('config/umbrales.json', encoding='utf-8'))
grafo = [json.loads(l) for l in open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
bandeja = []
for ruta in sorted(glob.glob(os.path.join('cuarentena', '*', '*.json'))):
    if os.path.basename(os.path.dirname(ruta)) in FUERA:
        continue
    bandeja.append(json.load(open(ruta, encoding='utf-8')))
poblacion = grafo + bandeja
cand = [n for n in poblacion if n.get('id') == cual][0]

t0 = time.time()
filas = []
ranking = []
for otro in poblacion:
    if otro.get('id') == cual:
        continue
    m = aduana.medir(cand, otro, umbrales)
    s = m['senales']
    ranking.append((s['similitud_texto'], s['familia_id'], s['paso_contra_nodo'], otro.get('id')))
    if m['levantada_por']:
        filas.append((otro.get('id'), s, m['levantada_por']))

print('%s   (%d pasos)   poblacion %d = %d grafo + %d bandejas'
      % (cual, len(cand.get('pasos_accionables', [])), len(poblacion), len(grafo), len(bandeja)))
print('  vecinos POR ENCIMA de umbral: %d' % len(filas))
for vid, s, porque in filas:
    print('    %-52s sim=%.3f fam=%.3f paso=%.3f  <- %s'
          % (vid, s['similitud_texto'], s['familia_id'], s['paso_contra_nodo'], ','.join(porque)))
ranking.sort(reverse=True)
print('  los 5 mas altos por similitud_texto, esten o no por encima:')
for sim, fam, pas, vid in ranking[:5]:
    print('    %-52s sim=%.3f fam=%.3f paso=%.3f' % (vid, sim, fam, pas))
print('  segundos: %.1f' % (time.time() - t0))
