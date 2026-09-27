# -*- coding: utf-8 -*-
"""RESUMEN DE MI BARRIDO DE VECINOS (D.38.4, D.38.5), IMPRESO EN MARKDOWN.

Poblacion de cada corrida: GRAFO MENOS EL PROPIO CANDIDATO MAS LAS BANDEJAS.
El grafo lo recorto yo (el nodo ya vive dentro); las bandejas las pone la aduana.
Lee los .v34aud/vec_<id>.txt que escribio .v34aud/uno.sh. CERO IDS TECLEADOS.
"""
import io, os, re
filas = []
pob = set()
for f in sorted(os.listdir('.v34aud')):
    if not (f.startswith('vec_') and f.endswith('.txt')): continue
    ident = f[4:-4]
    t = io.open(os.path.join('.v34aud', f), encoding='utf-8').read()
    m = re.search(r'poblacion del barrido\s*:\s*(\d+)\s*\((\d+) del grafo mas (\d+)', t)
    fin = 'Este informe es de SOLO LECTURA' in t
    if not (m and fin):
        filas.append((ident, None, None, None, 'SIN TERMINAR')); continue
    pob.add(m.group(0))
    v = re.search(r'vecinos levantados en total\s*:\s*(\d+)', t)
    saldo = re.search(r'BLOQUEARIAN esperando veredicto\s*:\s*(\d+)', t)
    entra = re.search(r'ENTRARIAN sin leer nada\s*:\s*(\d+)', t)
    caen = re.search(r'CAERIAN por una guarda\s*:\s*(\d+)', t)
    vecinos = re.findall(r'vecino (\S+)\s+\[levantada por: ([^\]]+)\]', t)
    filas.append((ident, int(m.group(1)), int(v.group(1)) if v else 0, vecinos,
                  'ENTRA' if entra.group(1) == '1' else ('BLOQUEA' if saldo.group(1) == '1' else 'CAE')))
print('| # | candidato | poblacion | saldo de la aduana | vecinos | cuales |')
print('|---:|---|---:|---|---:|---|')
tot = 0
for k, (i, p, v, ve, s) in enumerate(sorted(filas), 1):
    if p is None:
        print('| %d | `%s` | . | %s | . | . |' % (k, i, s)); continue
    tot += v
    print('| %d | `%s` | %d | %s | %d | %s |'
          % (k, i, p, s, v, ', '.join('`%s`' % x[0] for x in ve) if ve else '.'))
print('| | **total** | | | **%d** | |' % tot)
print()
print('poblaciones distintas vistas: %d' % len(pob))
for x in sorted(pob): print('  %s' % x)
