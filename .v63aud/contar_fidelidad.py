# -*- coding: utf-8 -*-
"""Cuenta la lectura de fidelidad de la fase ciega (.v63aud/fidelidad.tsv) contra los
candidatos de la bandeja: cada paso del candidato tiene que tener su fila, y ninguna
fila puede sobrar. Imprime por capitulo T (transcripcion), P (puente) y D (duda).
El separador del tsv es la barra vertical."""
import io, json, re, collections
RUTA = '.v63aud/fidelidad.tsv'
filas = [[c.strip() for c in l.rstrip('\n').split('|')]
         for l in io.open(RUTA, encoding='utf-8')
         if l.strip() and not l.startswith('#')]
por_id = collections.defaultdict(dict)
for f in filas:
    por_id[f[0]][int(f[1])] = f[2]
cap = {}
faltan, sobran = [], []
for i in sorted(por_id):
    d = json.load(io.open('cuarentena/grove_high_output/%s.json' % i, encoding='utf-8'))
    n = len(d['pasos_accionables'])
    cap[i] = re.search(r'fuentes/grove_high_output/(cap_\d+)\.md', d['resumen_teorico']).group(1)
    faltan += ['%s paso %d' % (i, k) for k in range(1, n + 1) if k not in por_id[i]]
    sobran += ['%s paso %d' % (i, k) for k in por_id[i] if k > n]
print('candidatos leidos : %d' % len(por_id))
print('filas de lectura  : %d' % len(filas))
print('pasos sin fila    : %d %s' % (len(faltan), faltan))
print('filas sin paso    : %d %s' % (len(sobran), sobran))
print('%-8s %5s %5s %4s %4s %4s' % ('capitulo', 'cand', 'pasos', 'T', 'P', 'D'))
tot = collections.Counter()
for c in sorted(set(cap.values())):
    ids = [i for i in cap if cap[i] == c]
    k = collections.Counter(v for i in ids for v in por_id[i].values())
    n = sum(len(por_id[i]) for i in ids)
    tot.update(k); tot['n'] += n; tot['c'] += len(ids)
    print('%-8s %5d %5d %4d %4d %4d' % (c, len(ids), n, k['T'], k['P'], k['D']))
print('%-8s %5d %5d %4d %4d %4d' % ('total', tot['c'], tot['n'], tot['T'], tot['P'], tot['D']))
