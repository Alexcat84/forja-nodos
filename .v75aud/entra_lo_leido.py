# -*- coding: utf-8 -*-
"""Fase ciega de la 75, sin git (copia de .v72aud/entra_lo_leido.py con la tanda de la 73): para las 7 de
.v73aud/los7.txt, (1) donde estan hoy: grafo, bandeja de Grove, _insertados; (2) que el nodo del grafo trae lo que se
leyo: titulo, condiciones, pasos, entregable y resumen, contra su ficha de _insertados (cuya huella es la de mi barrido
de la 73, .v75aud/huellas_hoy.py); (3) PASOS INVENTADOS de lo que ENTRO, por capitulo (8.2), desde MI lectura sellada
de la 73 (.v73aud/fidelidad_fuente.txt, una fila T, P o D por paso, leida sobre el texto ya corregido), con su suma (R7).
Mi unica D (gestionar_retencion paso 6, L121) la adjudico T la ACTA 72 72.5. El capitulo de cada una sale de
.v72aud/normal/siete.txt. NO imprime ninguna clave de relacion (R6). Solo lee."""
import io, os, json, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
los7 = io.open('.v73aud/los7.txt', encoding='utf-8').read().split()
cap = dict((l.split()[1], l.split()[0]) for l in io.open('.v72aud/normal/siete.txt', encoding='utf-8') if l.startswith('cap_'))
grafo = {}
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l); grafo[d['id']] = d
CAMPOS = ['titulo', 'condiciones_activacion', 'pasos_accionables', 'entregable_esperado', 'resumen_teorico']
sede = collections.Counter(); ig = collections.Counter(); desc = []
M = collections.defaultdict(list)
for l in io.open('.v73aud/fidelidad_fuente.txt', encoding='utf-8'):
    if l.strip(): f = l.rstrip('\n').split('|', 4); M[f[0]].append(f)
tot = collections.defaultdict(collections.Counter)
for i in los7:
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
print('las 7 por sede hoy: %s | suma: %d' % (dict(sede), sum(sede.values())))
print('nodos del grafo contra su ficha, cinco campos: %s | suma: %d' % (dict(ig), sum(ig.values())))
print('nodos con descuadre entre sus pasos en el grafo y mis filas selladas: %d %s' % (len(desc), desc))
T = collections.Counter()
for k in sorted(tot):
    t = tot[k]; m = dict((c, t[c]) for c in ('T', 'P', 'D'))
    for c in ('cand', 'pasos', 'T', 'P', 'D'): T[c] += t[c]
    print('%s lo que ENTRO: candidatos %d | pasos %d | mis marcas: %s | suma: %d | PUENTE %d de %d = %.2f por ciento | con la D adjudicada T (ACTA 72 72.5): T %d, P %d, suma %d' % (
        k, t['cand'], t['pasos'], m, sum(m.values()), t['P'], t['pasos'], 100.0 * t['P'] / t['pasos'], t['T'] + t['D'], t['P'], t['T'] + t['D'] + t['P']))
m = dict((c, T[c]) for c in ('T', 'P', 'D'))
print('los tres: candidatos %d | pasos %d | mis marcas: %s | suma: %d | PUENTE %d de %d' % (T['cand'], T['pasos'], m, sum(m.values()), T['P'], T['pasos']))
