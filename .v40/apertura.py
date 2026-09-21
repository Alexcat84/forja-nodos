# -*- coding: utf-8 -*-
"""Apertura de la vuelta 40. Mide el estado ANTES de la primera operacion."""
import json, os, glob, subprocess, io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def sh(c):
    return subprocess.run(c, shell=True, capture_output=True, text=True).stdout.strip()

nodos = [json.loads(l) for l in open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
vers  = [json.loads(l) for l in open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()]

sig = sum(len(n.get('nodos_siguientes', [])) for n in nodos)
prev = sum(len(n.get('nodos_previos', [])) for n in nodos)
no_cons = sum(1 for v in vers if any(a.get('no_consumada') is True for a in v.get('anotaciones', [])))
band4 = len(glob.glob('cuarentena/scott_radical_candor/*.json'))
ins4  = len(glob.glob('cuarentena/_insertados/scott_radical_candor/*.json'))
band5 = len(glob.glob('cuarentena/marquet_turn_the_ship/*.json'))
instotal = len(glob.glob('cuarentena/_insertados/*/*.json'))
rama = sh('git rev-parse --abbrev-ref HEAD')
commit = sh('git rev-parse --short HEAD')

filas = [
    ('rama', rama, '`git rev-parse --abbrev-ref HEAD`'),
    ('commit al abrir mi turno', '`%s`' % commit, '`git rev-parse --short HEAD`'),
    ('nodos en `dataset/nodos.jsonl`', '**%d**' % len(nodos), '`dataset/nodos.jsonl`'),
    ('veredictos en `bitacora/VEREDICTOS.jsonl`', '**%d**' % len(vers), '`bitacora/VEREDICTOS.jsonl`'),
    ('de ellos, con alguna anotacion `no_consumada: true`', '**%d**' % no_cons, '`bitacora/VEREDICTOS.jsonl`'),
    ('aristas por `nodos_siguientes`', '**%d**' % sig, '`dataset/nodos.jsonl`'),
    ('aristas por `nodos_previos`', '**%d**' % prev, '`dataset/nodos.jsonl`'),
    ('candidatos en bandeja, lote 4', '**%d**' % band4, 'PATRON: `cuarentena/scott_radical_candor/*.json`'),
    ('insertados y archivados, lote 4', '**%d**' % ins4, 'PATRON: `cuarentena/_insertados/scott_radical_candor/*.json`'),
    ('candidatos en bandeja, lote 5', '**%d**' % band5, 'PATRON: `cuarentena/marquet_turn_the_ship/*.json`'),
    ('insertados y archivados, los cuatro lotes', '**%d**' % instotal, 'PATRON: `cuarentena/_insertados/*/*.json`'),
    ('lote 4 insertado sobre `142`, por ciento', '**%s**' % ('%.1f' % (100.0*ins4/142)).replace('.', ','), '`cuarentena/_insertados/scott_radical_candor/`'),
]
out = ['| pieza | valor | de donde sale |', '|---|---:|---|']
for a, b, c in filas:
    out.append('| %s | %s | %s |' % (a, b, c))
open('.v40/apertura_tabla.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('\n'.join(out))
