# -*- coding: utf-8 -*-
"""Fase ciega de la 70, sin git (copia libre de .v67aud/entra_lo_leido.py): para las 20 de .v68aud/los20.txt,
(1) donde estan hoy: grafo, bandeja de Grove, _insertados; (2) que el nodo del grafo trae lo que se leyo: titulo,
condiciones, pasos, entregable y resumen, contra su ficha de _insertados (cuya huella es la de mi barrido de la 68,
.v70aud/huellas_hoy.py); (3) PASOS INVENTADOS de lo que ENTRO, por capitulo (8.2), desde MI lectura sellada de la 68
(.v68aud/fidelidad_fuente.txt, una fila T, P o D por paso), con su suma (R7). Las D las adjudique T en la ACTA 67
67.4.a. NO imprime ninguna clave de relacion (R6). Solo lee."""
import io, os, json, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
los20 = io.open('.v68aud/los20.txt', encoding='utf-8').read().split()
cap = dict((i, 'cap_05' if n < 12 else 'cap_06') for n, i in enumerate(los20))
grafo = {}
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l); grafo[d['id']] = d
CAMPOS = ['titulo', 'condiciones_activacion', 'pasos_accionables', 'entregable_esperado', 'resumen_teorico']
sede = collections.Counter(); ig = collections.Counter(); desc = []
M = collections.defaultdict(list)
for l in io.open('.v68aud/fidelidad_fuente.txt', encoding='utf-8'):
    if l.strip(): f = l.rstrip('\n').split('|', 4); M[f[0]].append(f)
tot = collections.defaultdict(collections.Counter)
for i in los20:
    s = []
    if i in grafo: s.append('grafo')
    if os.path.exists('cuarentena/grove_high_output/%s.json' % i): s.append('bandeja')
    if os.path.exists('cuarentena/_insertados/grove_high_output/%s.json' % i): s.append('_insertados')
    sede[' y '.join(s) or 'NINGUNA'] += 1
    if i not in grafo: continue
    ficha = json.load(io.open('cuarentena/_insertados/grove_high_output/%s.json' % i, encoding='utf-8'))
    dif = [k for k in CAMPOS if grafo[i].get(k) != ficha.get(k)]
    ig['distinto' if dif else 'igual'] += 1
    if dif: print('  DISTINTO de su ficha: %s %s' % (i, dif))
    n = len(grafo[i]['pasos_accionables']); fs = M[i]
    if n != len(fs) or [int(f[1]) for f in fs] != list(range(1, n + 1)): desc.append(i)
    t = tot[cap[i]]; t['cand'] += 1; t['pasos'] += n
    for f in fs: t[f[2]] += 1
print('las 20 por sede hoy: %s | suma: %d' % (dict(sede), sum(sede.values())))
print('nodos del grafo contra su ficha, cinco campos: %s | suma: %d' % (dict(ig), sum(ig.values())))
print('nodos con descuadre entre sus pasos en el grafo y mis filas selladas: %d %s' % (len(desc), desc))
for k in ('cap_05', 'cap_06'):
    t = tot[k]; m = dict((c, t[c]) for c in ('T', 'P', 'D'))
    print('%s lo que ENTRO: candidatos %d | pasos %d | mis marcas: %s | suma: %d | PUENTE %d de %d = %.2f por ciento | con las D adjudicadas T: T %d, P %d, suma %d' % (
        k, t['cand'], t['pasos'], m, sum(m.values()), t['P'], t['pasos'], 100.0 * t['P'] / t['pasos'], t['T'] + t['D'], t['P'], t['T'] + t['D'] + t['P']))
