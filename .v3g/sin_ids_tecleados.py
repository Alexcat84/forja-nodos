# -*- coding: utf-8 -*-
# HEREDADO 4: comprueba que NINGUN instrumento de .v3g/ lleva un id de nodo
# tecleado dentro. La lista de ids NO se teclea: se casa contra el dato, que es
# justo lo que el remedio pide.
import io, json, glob, os

ids = set()
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    if l.strip():
        ids.add(json.loads(l)['id'])
for p in glob.glob('cuarentena/*/*.json'):
    q = p.replace(os.sep, '/')
    if '_insertados' in q or '_derivadas' in q:
        continue
    ids.add(json.load(io.open(p, encoding='utf-8'))['id'])

print('ids del grafo mas las bandejas, casados del dato: %d' % len(ids))
guiones = sorted(glob.glob('.v3g/*.py'))
print('instrumentos de .v3g/ barridos              : %d' % len(guiones))
hallazgos = 0
for g in guiones:
    texto = io.open(g, encoding='utf-8').read()
    dentro = sorted(i for i in ids if i in texto)
    print('  %-34s ids tecleados dentro: %d' % (os.path.basename(g), len(dentro)))
    for i in dentro:
        print('      TECLEADO: %s' % i)
        hallazgos += 1
print('TOTAL DE IDS TECLEADOS EN MIS INSTRUMENTOS: %d' % hallazgos)
