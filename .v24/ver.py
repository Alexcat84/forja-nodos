# -*- coding: utf-8 -*-
"""Imprime lo que hace falta para juzgar un par: titulo, activacion y el paso citado."""
import glob, io, json, os, sys

def cargar(i):
    for r in glob.glob('cuarentena/*/%s.json' % i) + glob.glob('cuarentena/_insertados/*/%s.json' % i):
        return json.load(io.open(r, encoding='utf-8'))
    for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
        d = json.loads(l)
        if d['id'] == i:
            return d
    raise SystemExit('no encuentro ' + i)

for arg in sys.argv[1:]:
    if ':' in arg:
        i, paso = arg.split(':')
        paso = int(paso)
    else:
        i, paso = arg, None
    d = cargar(i)
    print('### %s  (%d pasos)' % (d['id'], len(d['pasos_accionables'])))
    print('   TIT: %s' % d['titulo'])
    print('   ACT: %s' % d['condiciones_activacion'])
    print('   ENT: %s' % d['entregable_esperado'][:200])
    if paso:
        print('   P%d: %s' % (paso, d['pasos_accionables'][paso-1]))
    print('')
