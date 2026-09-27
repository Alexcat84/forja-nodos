# -*- coding: utf-8 -*-
"""IMPRIME LOS PASOS DE UN CANDIDATO Y DE SUS VECINOS, ENTEROS Y ANTES DE JUZGAR.

Las seniales ordenan, nunca deciden (manual principio 4). Esto es lo que se lee
antes de escribir un veredicto: los dos lados, enteros, sin resumir.
"""
import glob, io, json, os, sys

def buscar(ident):
    for linea in io.open('dataset/nodos.jsonl', encoding='utf-8'):
        linea = linea.strip()
        if linea and json.loads(linea)['id'] == ident:
            return json.loads(linea), 'GRAFO'
    for ruta in glob.glob('cuarentena/*/*.json') + glob.glob('cuarentena/_insertados/*/*.json'):
        if os.path.basename(ruta)[:-5] == ident:
            return json.load(io.open(ruta, encoding='utf-8')), \
                   ('INSERTADO' if '_insertados' in ruta else 'bandeja')
    return None, 'NO EXISTE'

for ident in sys.argv[1:]:
    d, donde = buscar(ident)
    print('=' * 78)
    print('%s   [%s]' % (ident, donde))
    print('=' * 78)
    if not d:
        continue
    print('TITULO    : %s' % d.get('titulo', ''))
    print('ACTIVACION: %s' % d.get('condicion_activacion', ''))
    print('ENTREGABLE: %s' % d.get('entregable', ''))
    for i, p in enumerate(d['pasos_accionables'], 1):
        print('  P%-2d %s' % (i, p))
    print('')
