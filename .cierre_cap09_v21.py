# -*- coding: utf-8 -*-
"""Comprueba por mi cuenta el cierre de cap_09: las 20 piezas que dan nodo,
cuales son las CINCO nuevas de esta vuelta y cuales las 15 de la anterior.
La frontera de 30 piezas esta ADJUDICADA en la ACTA 19 y no se reabre.
"""
import json, os, re
DIR = 'cuarentena/scott_radical_candor'
LAS_CINCO = ['revisar_critica_mujer_agresiva_cuatro_tacticas',
             'responder_critica_abrasiva_cuatro_reglas',
             'entregar_evaluacion_formal_desempenio_nueve_consejos',
             'conducir_reuniones_salto_nivel_diez_reglas',
             'resolver_dudas_frecuentes_reuniones_salto_nivel']
piezas = {}
for n in sorted(os.listdir(DIR)):
    if not n.endswith('.json'):
        continue
    crudo = open(os.path.join(DIR, n), encoding='utf-8').read()
    if not re.search(r'UNIDAD DE ORIGEN:[^,]*?cap_09\.md', crudo):
        continue
    d = json.loads(crudo)
    m = re.search(r'PIEZA (P\d+) DE LA FRONTERA', d['resumen_teorico'])
    piezas[int(m.group(1)[1:])] = (n[:-5], len(d['pasos_accionables']))

nuevas = {k: v for k, v in piezas.items() if v[0] in LAS_CINCO}
viejas = {k: v for k, v in piezas.items() if v[0] not in LAS_CINCO}
print('piezas de cap_09 con nodo en la bandeja : %d' % len(piezas))
print('  de la vuelta anterior                 : %d  %s'
      % (len(viejas), sorted('P%d' % k for k in viejas)))
print('  escritas en esta vuelta               : %d  %s'
      % (len(nuevas), sorted(('P%d' % k for k in nuevas), key=lambda s: int(s[1:]))))
print('')
print('LAS CINCO, CON SUS PASOS:')
tot = 0
for k in sorted(nuevas):
    print('  P%-3d %-52s pasos=%d' % (k, nuevas[k][0], nuevas[k][1]))
    tot += nuevas[k][1]
print('  pasos de las cinco: %d' % tot)
print('  pasos de las veinte: %d' % sum(v[1] for v in piezas.values()))
print('')
todas = set(range(1, 31))
print('numeros de pieza de la frontera de 30 que NO dan nodo: %d  %s'
      % (len(todas - set(piezas)), sorted(todas - set(piezas))))
print('')
n10 = [n for n in sorted(os.listdir(DIR)) if n.endswith('.json')
       and re.search(r'cap_10', open(os.path.join(DIR, n), encoding='utf-8').read())]
print('candidatos de la bandeja que nombran cap_10 en cualquier campo: %d %s' % (len(n10), n10))
