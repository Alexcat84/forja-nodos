# -*- coding: utf-8 -*-
"""Vuelta 78, lectura de trabajo: vuelca las fichas de cuarentena/marquet_turn_the_ship/ (titulo, condicion, entregable, pasos numerados,
resumen y aristas) para leerlas contra su capitulo. Con un argumento cap_NN, solo las de esa UNIDAD DE ORIGEN. Solo lee."""
import io, json, glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')
cap = sys.argv[1] if len(sys.argv) > 1 else None
for f in sorted(glob.glob('cuarentena/marquet_turn_the_ship/*.json')):
    d = json.load(io.open(f, encoding='utf-8'))
    c = re.search(r'fuentes/marquet_turn_the_ship/(cap_\d+)\.md', d['resumen_teorico']).group(1)
    if cap and c != cap:
        continue
    print('=== %s (%s)' % (d['id'], c))
    print('TITULO:', d['titulo'])
    print('COND:', d['condiciones_activacion'])
    print('ENTREGABLE:', d['entregable_esperado'])
    for i, p in enumerate(d['pasos_accionables'], 1):
        print('  %d. %s' % (i, p))
    print('RESUMEN:', d['resumen_teorico'])
    print('NS:', d.get('nodos_siguientes'), 'NP:', d.get('nodos_previos'), 'ATR:', d.get('atribuciones'))
    print()
