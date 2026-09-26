# -*- coding: utf-8 -*-
"""Fase ciega de la 77, sin git (copia libre de .v75aud/entra_lo_leido.py con la tanda de la 76): para las 22 de
.v76aud/las22.txt, (1) donde estan hoy: grafo, bandeja de Gerber, _insertados; (2) que el nodo del grafo trae lo que se
leyo: titulo, condiciones, pasos, entregable y resumen, contra su ficha de _insertados (cuya huella es la de mi barrido
de la 76, .v77aud/huellas_hoy.py); (3) PASOS INVENTADOS de lo que ENTRO, por capitulo (8.2), desde MI lectura sellada
de la 76 (.v76aud/fidelidad.tsv, una fila T, P o D por paso, leida sobre el texto de la bandeja ya corregido), con su
suma (R7). Mi unica D (cuantificar_impacto_innovacion_6_pasos paso 4, cap_12 L95) la adjudique T en la ACTA 75 75.3.
El capitulo de cada fila es la columna capitulo de ese mismo fichero. NO imprime ninguna clave de relacion (R6). Solo lee."""
import io, os, json, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
las22 = io.open('.v76aud/las22.txt', encoding='utf-8').read().split()
grafo = {}
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l); grafo[d['id']] = d
CAMPOS = ['titulo', 'condiciones_activacion', 'pasos_accionables', 'entregable_esperado', 'resumen_teorico']
M = collections.defaultdict(list)
for l in list(io.open('.v76aud/fidelidad.tsv', encoding='utf-8'))[1:]:
    if l.strip(): f = l.rstrip('\n').split('\t'); M[f[0]].append(f)
sede = collections.Counter(); ig = collections.Counter(); desc = []
tot = collections.defaultdict(collections.Counter)
for i in las22:
    s = []
    if i in grafo: s.append('grafo')
    if os.path.exists('cuarentena/gerber_emyth/%s.json' % i): s.append('bandeja')
    if os.path.exists('cuarentena/_insertados/gerber_emyth/%s.json' % i): s.append('_insertados')
    sede[' y '.join(s) or 'NINGUNA'] += 1
    if i not in grafo: continue
    ficha = json.load(io.open('cuarentena/_insertados/gerber_emyth/%s.json' % i, encoding='utf-8'))
    dif = [k for k in CAMPOS if grafo[i].get(k) != ficha.get(k)]
    ig['distinto' if dif else 'igual'] += 1
    if dif: print('  DISTINTO de su ficha: %s %s' % (i, dif))
    n = len(grafo[i]['pasos_accionables']); fs = M[i]
    if n != len(fs) or [int(f[1]) for f in fs] != list(range(1, n + 1)): desc.append(i)
    caps = set(f[3] for f in fs)
    t = tot['/'.join(sorted(caps))]; t['cand'] += 1; t['pasos'] += n
    for f in fs: t[f[2]] += 1
print('las 22 por sede hoy: %s | suma: %d' % (dict(sede), sum(sede.values())))
print('nodos del grafo contra su ficha, cinco campos: %s | suma: %d' % (dict(ig), sum(ig.values())))
print('nodos con descuadre entre sus pasos en el grafo y mis filas selladas: %d %s' % (len(desc), desc))
T = collections.Counter()
for k in sorted(tot):
    t = tot[k]; m = dict((c, t[c]) for c in ('T', 'P', 'D'))
    for c in ('cand', 'pasos', 'T', 'P', 'D'): T[c] += t[c]
    print('%s lo que ENTRO: candidatos %d | pasos %d | mis marcas: %s | suma: %d | PUENTE %d de %d = %.2f por ciento' % (
        k, t['cand'], t['pasos'], m, sum(m.values()), t['P'], t['pasos'], 100.0 * t['P'] / t['pasos']))
m = dict((c, T[c]) for c in ('T', 'P', 'D'))
print('los diez: candidatos %d | pasos %d | mis marcas: %s | suma: %d | PUENTE %d de %d | con la D adjudicada T (ACTA 75 75.3): T %d, P %d, suma %d' % (
    T['cand'], T['pasos'], m, sum(m.values()), T['P'], T['pasos'], T['T'] + T['D'], T['P'], T['T'] + T['D'] + T['P']))
