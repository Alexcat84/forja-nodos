# -*- coding: utf-8 -*-
"""MI RECUENTO DEL DATO, ANTES Y DESPUES, IMPRESO EN MARKDOWN (D.41).

BASE = b698aef, el arbol con el que el arnes abrio la vuelta 34 (el ultimo
commit antes de la primera tarea). HOY = el arbol de trabajo.
CERO CIFRAS TECLEADAS: todas salen de leer los ficheros y de `git show`.
"""
import io, json, os, subprocess
BASE = 'b698aef'

def jl_t(t): return [json.loads(l) for l in t.split('\n') if l.strip()]
def jl(r): return [json.loads(l) for l in io.open(r, encoding='utf-8') if l.strip()]
def show(ref, r): return subprocess.check_output(['git', 'show', '%s:%s' % (ref, r)]).decode('utf-8')
def lst(ref, r):
    s = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', ref, r]).decode('utf-8')
    return len([x for x in s.split('\n') if x.strip().endswith('.json')])
def dsk(r): return len([f for f in os.listdir(r) if f.endswith('.json')])

nb, vb = jl_t(show(BASE, 'dataset/nodos.jsonl')), jl_t(show(BASE, 'bitacora/VEREDICTOS.jsonl'))
nh, vh = jl('dataset/nodos.jsonl'), jl('bitacora/VEREDICTOS.jsonl')
B4, I4, B5 = ('cuarentena/scott_radical_candor',
              'cuarentena/_insertados/scott_radical_candor',
              'cuarentena/marquet_turn_the_ship')
tot = dsk(B4) + dsk(I4)
filas = [
    ('nodos en `dataset/nodos.jsonl`', len(nb), len(nh)),
    ('pasos del grafo entero', sum(len(x['pasos_accionables']) for x in nb),
                              sum(len(x['pasos_accionables']) for x in nh)),
    ('lineas en `bitacora/VEREDICTOS.jsonl`', len(vb), len(vh)),
    ('veredictos con `consumada == False`', sum(1 for x in vb if x.get('consumada') is False),
                                           sum(1 for x in vh if x.get('consumada') is False)),
    ('aristas por `nodos_siguientes`', sum(len(x.get('nodos_siguientes') or []) for x in nb),
                                      sum(len(x.get('nodos_siguientes') or []) for x in nh)),
    ('aristas por `nodos_previos`', sum(len(x.get('nodos_previos') or []) for x in nb),
                                   sum(len(x.get('nodos_previos') or []) for x in nh)),
    ('candidatos en bandeja, lote 4', lst(BASE, B4), dsk(B4)),
    ('archivados en `_insertados`, lote 4', lst(BASE, I4), dsk(I4)),
    ('candidatos en bandeja, lote 5', lst(BASE, B5), dsk(B5)),
    ('nodos que citan `cap_09.md`',
     sum(1 for x in nb if 'scott_radical_candor/cap_09.md' in (x.get('resumen_teorico') or '')),
     sum(1 for x in nh if 'scott_radical_candor/cap_09.md' in (x.get('resumen_teorico') or ''))),
    ('pasos de los nodos de `cap_09`',
     sum(len(x['pasos_accionables']) for x in nb if 'scott_radical_candor/cap_09.md' in (x.get('resumen_teorico') or '')),
     sum(len(x['pasos_accionables']) for x in nh if 'scott_radical_candor/cap_09.md' in (x.get('resumen_teorico') or ''))),
]
print('| pieza | **yo, sobre `%s`** | **yo, sobre el arbol de hoy** |' % BASE)
print('|---|---:|---:|')
for n, a, b in filas:
    print('| %s | **%s** | **%s** |' % (n, a, b))
print('| lote 4 insertado sobre `%d`, por ciento | **%.2f** | **%.2f** |'
      % (tot, 100.0 * lst(BASE, I4) / tot, 100.0 * dsk(I4) / tot))
