# -*- coding: utf-8 -*-
# CERO IDS TECLEADOS. La tanda sale de `git diff --name-only <base> HEAD -- cuarentena/_insertados/`
# y del diff de ids de dataset/nodos.jsonl. El resto se recorre por carpeta.
import io, json, os, subprocess, sys

BASE = sys.argv[1] if len(sys.argv) > 1 else 'b698aef'

def jl_texto(t):
    return [json.loads(l) for l in t.split('\n') if l.strip()]

def jl(ruta):
    return [json.loads(l) for l in io.open(ruta, encoding='utf-8') if l.strip()]

def show(ref, ruta):
    return subprocess.check_output(['git', 'show', '%s:%s' % (ref, ruta)]).decode('utf-8')

def cuenta(nodos, ver):
    return dict(
        nodos=len(nodos),
        pasos=sum(len(n.get('pasos_accionables') or []) for n in nodos),
        sig=sum(len(n.get('nodos_siguientes') or []) for n in nodos),
        prev=sum(len(n.get('nodos_previos') or []) for n in nodos),
        ver=len(ver),
        no_consumada=sum(1 for v in ver if v.get('consumada') is False),
    )

hoy = cuenta(jl('dataset/nodos.jsonl'), jl('bitacora/VEREDICTOS.jsonl'))
base = cuenta(jl_texto(show(BASE, 'dataset/nodos.jsonl')),
              jl_texto(show(BASE, 'bitacora/VEREDICTOS.jsonl')))

def ls_tree(ref, ruta):
    s = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', ref, ruta]).decode('utf-8')
    return [x for x in s.split('\n') if x.strip().endswith('.json')]

for nom, ruta in (('bandeja lote 4', 'cuarentena/scott_radical_candor'),
                  ('archivados lote 4', 'cuarentena/_insertados/scott_radical_candor'),
                  ('bandeja lote 5', 'cuarentena/marquet_turn_the_ship')):
    base[nom] = len(ls_tree(BASE, ruta))
    hoy[nom] = len([f for f in os.listdir(ruta) if f.endswith('.json')])

print('BASE = %s' % BASE)
print('%-28s %10s %10s' % ('pieza', 'BASE', 'HOY'))
for k in ('nodos', 'pasos', 'sig', 'prev', 'ver', 'no_consumada',
          'bandeja lote 4', 'archivados lote 4', 'bandeja lote 5'):
    print('%-28s %10s %10s' % (k, base[k], hoy[k]))
tot4 = hoy['bandeja lote 4'] + hoy['archivados lote 4']
print('%-28s %10s %10s' % ('lote 4 total', base['bandeja lote 4'] + base['archivados lote 4'], tot4))
print('%-28s %9.2f%% %9.2f%%' % ('lote 4 insertado', 100.0 * base['archivados lote 4'] / tot4,
                                 100.0 * hoy['archivados lote 4'] / tot4))

sal = subprocess.check_output(['git', 'diff', '--name-only', BASE, 'HEAD', '--',
                               'cuarentena/_insertados/']).decode('utf-8')
tanda = [r for r in sal.split('\n') if r.strip()]
io.open('.v34aud/tanda.txt', 'w', encoding='utf-8').write('\n'.join(tanda) + '\n')
print('\nTANDA DE LA VUELTA AUDITADA, del dato: %d ficheros' % len(tanda))
tp = 0
for ruta in tanda:
    d = json.load(io.open(ruta, encoding='utf-8'))
    tp += len(d['pasos_accionables'])
    print('  %-54s %3d pasos' % (d['id'], len(d['pasos_accionables'])))
print('pasos de la tanda: %d' % tp)

ab = {n['id']: n for n in jl_texto(show(BASE, 'dataset/nodos.jsonl'))}
ho = {n['id']: n for n in jl('dataset/nodos.jsonl')}
nuevos = [i for i in ho if i not in ab]
print('\nids NUEVOS en el grafo: %d' % len(nuevos))
faltan = [i for i in ab if i not in ho]
print('ids QUE DESAPARECEN del grafo: %d %s' % (len(faltan), faltan))
cambiados = [i for i in sorted(ab) if i in ho and
             json.dumps(ab[i], sort_keys=True) != json.dumps(ho[i], sort_keys=True)]
print('nodos PREEXISTENTES que cambiaron: %d' % len(cambiados))
for i in cambiados:
    print('  ~ %s' % i)
    for c in sorted(set(list(ab[i]) + list(ho[i]))):
        if ab[i].get(c) != ho[i].get(c):
            print('      campo %s' % c)
