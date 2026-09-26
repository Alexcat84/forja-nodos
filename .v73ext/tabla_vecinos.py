# -*- coding: utf-8 -*-
"""COPIA DE LA VUELTA 73 de .v71ext/tabla_vecinos.py, con las rutas cambiadas a .v73ext/ y la lista a .v73ext/las7.txt, y nada
mas. Lo que decia la de la 71: Vuelta 71, TAREA 3: una tabla por candidato de sus vecinos, leida de .v71ext/vecinos_<id>.json (el barrido de hoy), en
el orden de .v71ext/los20.txt. Solo lee. Por vecino: su sede, las tres seniales y cual lo levanto. Como las tablas que .v68ext/
dejo para la 70 (cada .v68ext/barrido_<id>.txt con su vecinos_<id>.json al lado), aqui impresas en un solo fichero."""
import io, json
for l in io.open('.v73ext/las7.txt', encoding='utf-8').read().split('\n')[1:]:
    if not l.strip(): continue
    cap, i, n = l.split()
    try:
        d = json.load(io.open('.v73ext/vecinos_%s.json' % i, encoding='utf-8'))
    except IOError:
        print('## %s (%s): SIN BARRIDO TODAVIA' % (i, cap)); print(); continue
    print('## %s (%s), poblacion %d (%d grafo mas %d bandejas), vecinos %d' % (i, cap, d['grafo'] + d['bandejas'], d['grafo'], d['bandejas'], len(d['vecinos'])))
    print('| vecino | sede | similitud | familia | paso | levantada por |')
    print('|---|---|---:|---:|---:|---|')
    for v in d['vecinos']:
        s = v['senales']
        f = lambda k: ('%.3f' % s[k]) if isinstance(s.get(k), float) else str(s.get(k))
        ks = list(s.keys())
        print('| `%s` | %s | %s | %s | %s | %s |' % (v['id'], v['sede'], f(ks[0]), f(ks[1]), f(ks[2]), ', '.join(v['levantada_por']) if isinstance(v['levantada_por'], list) else v['levantada_por']))
    print()
