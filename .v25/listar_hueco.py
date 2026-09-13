# -*- coding: utf-8 -*-
"""LOS CANDIDATOS DE LAS TRES FILAS DE HUECO ENCARGADAS, CON SU UNIDAD Y SUS PASOS."""
import glob, io, json, os, re, sys
CITA = re.compile(r'cap_(\d+)')
QUIERO = set(sys.argv[1:]) or {'cap_01', 'cap_03', 'cap_05'}
filas = []
for ruta in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')
                   + glob.glob('cuarentena/_insertados/scott_radical_candor/*.json')):
    d = json.load(io.open(ruta, encoding='utf-8'))
    r = d.get('resumen_teorico', '')
    m = CITA.findall(r)
    cap = 'cap_%s' % m[0] if m else 'SIN CITA'
    if cap not in QUIERO:
        continue
    i = r.find('UNIDAD DE ORIGEN')
    filas.append((cap, os.path.basename(ruta)[:-5], len(d['pasos_accionables']),
                  'bandeja' if '_insertados' not in ruta else 'INSERTADO',
                  r[i:i + 190].replace('\n', ' ') if i >= 0 else r[:190].replace('\n', ' ')))
filas.sort()
tot = 0
for cap, ident, n, donde, orig in filas:
    tot += n
    print('%s  %-58s %2d pasos  [%s]' % (cap, ident, n, donde))
    print('        %s' % orig)
print('')
print('candidatos: %d    pasos: %d' % (len(filas), tot))
