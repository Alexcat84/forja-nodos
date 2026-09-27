# -*- coding: utf-8 -*-
"""Que cambio EXACTAMENTE en practicar_triangulo_critica_tres_papeles entre la
huella contra la que se emitieron las lineas 484 y 485 y el texto de hoy.

La huella vieja es eec451c2e48944c6 (la que imprime forja.py rancios) y sale del
arbol a41fc11, que es el commit anterior a 0dda2e3, donde la correccion de la
vuelta 39 la movio a 5aebf76b97831357. Los dos hashes salen de forja.py rancios y de
src/comun.py huella_de_nodo, que cubre titulo mas resumen_teorico mas pasos.
"""
import json
import os
import subprocess
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ID = 'practicar_triangulo_critica_tres_papeles'
CAMPOS = ('titulo', 'pasos_accionables', 'entregable_esperado',
          'condiciones_activacion', 'dominio', 'fuentes', 'denominaciones',
          'nodos_siguientes', 'nodos_previos', 'resumen_teorico')


def del_arbol(ref):
    if ref == 'HOY':
        crudo = io.open('dataset/nodos.jsonl', encoding='utf-8').read()
    else:
        crudo = subprocess.run(['git', 'show', '%s:dataset/nodos.jsonl' % ref],
                               capture_output=True).stdout.decode('utf-8')
    for linea in crudo.split('\n'):
        linea = linea.strip()
        if not linea:
            continue
        d = json.loads(linea)
        if d['id'] == ID:
            return d
    return None


viejo = del_arbol('a41fc11')
hoy = del_arbol('HOY')

print('  nodo: %s' % ID)
print('  arbol viejo: a41fc11 (el de la huella eec451c2e48944c6 con la que se emitieron 484 y 485)')
print('  arbol de hoy: el de trabajo')
print()
print('  %-24s %-9s %s' % ('campo', 'cambia?', 'que pasa'))
print('  ' + '-' * 96)
for c in CAMPOS:
    a, b = viejo.get(c), hoy.get(c)
    if a == b:
        detalle = 'identico'
        if isinstance(a, list):
            detalle = 'identico, %d elemento(s)' % len(a)
        elif isinstance(a, str):
            detalle = 'identico, %d caracter(es)' % len(a)
        print('  %-24s %-9s %s' % (c, 'NO', detalle))
    else:
        if isinstance(a, str) and isinstance(b, str):
            detalle = '%d -> %d caracteres, prefijo comun de %d' % (
                len(a), len(b),
                len(os.path.commonprefix([a, b])))
        else:
            detalle = '%s -> %s' % (a, b)
        print('  %-24s %-9s %s' % (c, 'SI', detalle))
print()
print('  los 15 pasos, uno a uno, viejo contra hoy:')
for i, (pa, pb) in enumerate(zip(viejo['pasos_accionables'], hoy['pasos_accionables']), 1):
    print('    P%-3d %s' % (i, 'IDENTICO' if pa == pb else 'CAMBIA'))
