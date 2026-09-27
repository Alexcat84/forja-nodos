# -*- coding: utf-8 -*-
"""Fase ciega de la 67. La poblacion de la aduana (grafo mas bandejas, D.38.4 y D.38.5) HOY contra la del commit de
la ACTA 65 (4648cbc), que es la que mi barrido de la 66 midio (479). Si el conjunto de ids es el mismo y cada id tiene
el mismo contenido fuera de las claves de relacion, el barrido de la 66 vale para la aduana de la 67 sin re correrlo.
Compara titulo, condiciones, pasos, entregable y resumen; NO imprime las claves de relacion (la fase es ciega)."""
import io, json, os, shutil, subprocess, sys, tarfile, tempfile
sys.path.insert(0, '.')
from src import aduana
CAMPOS = ['titulo', 'condiciones_activacion', 'pasos_accionables', 'entregable_esperado', 'resumen_teorico']
def pob(raiz):
    g = {}
    for l in io.open(os.path.join(raiz, 'dataset', 'nodos.jsonl'), encoding='utf-8'):
        d = json.loads(l); g[d['id']] = ('grafo', d)
    b = {}
    for c in aduana.poblacion_de_bandejas(raiz=raiz):
        b[c['id']] = ('bandeja', c)
    return g, b
tmp = tempfile.mkdtemp(prefix='pob65_')
arch = os.path.join(tmp, 'a.tar')
subprocess.run(['git', 'archive', '-o', arch, '4648cbc', 'dataset', 'cuarentena'], check=True)
tarfile.open(arch).extractall(tmp, filter='data')
g0, b0 = pob(tmp)
g1, b1 = pob('.')
p0 = dict(b0); p0.update(g0)
p1 = dict(b1); p1.update(g1)
print('en 4648cbc: %d del grafo mas %d de bandejas = %d | ids distintos: %d' % (len(g0), len(b0), len(g0) + len(b0), len(p0)))
print('hoy       : %d del grafo mas %d de bandejas = %d | ids distintos: %d' % (len(g1), len(b1), len(g1) + len(b1), len(p1)))
print('ids solo en 4648cbc: %s | ids solo hoy: %s' % (sorted(set(p0) - set(p1)), sorted(set(p1) - set(p0))))
mov = sorted(i for i in p1 if p0.get(i, ('',))[0] == 'bandeja' and p1[i][0] == 'grafo')
print('de la bandeja al grafo: %d' % len(mov))
dist = []
for i in sorted(set(p0) & set(p1)):
    a, b = p0[i][1], p1[i][1]
    k = [c for c in CAMPOS if a.get(c) != b.get(c)]
    if k: dist.append((i, p0[i][0], p1[i][0], k))
print('ids con contenido distinto fuera de las claves de relacion: %d' % len(dist))
for d in dist: print('  DISTINTO %s (%s -> %s) %s' % d)
REL = ('nodos_previos', 'nodos_siguientes')
gg = [i for i in sorted(set(g0) & set(g1))]
cambia_rel = 0; cambia_otra = []
for i in gg:
    a, b = g0[i][1], g1[i][1]
    if a == b: continue
    otras = sorted(k for k in set(a) | set(b) if k not in REL and a.get(k) != b.get(k))
    if otras: cambia_otra.append((i, otras))
    else: cambia_rel += 1
print('nodos del grafo en los dos commits: %d | reescritos solo en claves de relacion: %d | con otra clave cambiada: %d' % (
    len(gg), cambia_rel, len(cambia_otra)))
for x in cambia_otra: print('  OTRA CLAVE %s %s' % x)
shutil.rmtree(tmp)
