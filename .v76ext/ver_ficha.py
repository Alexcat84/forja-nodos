# -*- coding: utf-8 -*-
"""Vuelta 76, solo lee: imprime de una ficha de cuarentena/gerber_emyth/ su condicion, su entregable, sus pasos numerados y las
citas de capitulo y linea que trae su resumen_teorico, para leerla contra su capitulo. python .v76ext/ver_ficha.py <id> [...]"""
import io, json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
for i in sys.argv[1:]:
    d = json.load(io.open('cuarentena/gerber_emyth/%s.json' % i, encoding='utf-8'))
    print('=' * 100); print(i, '|', d['titulo'])
    print('CONDICION:', d['condiciones_activacion']); print('ENTREGABLE:', d['entregable_esperado'])
    for k, p in enumerate(d['pasos_accionables'], 1):
        print('  %2d. %s' % (k, p))
    print('CITAS:', sorted(set(re.findall(r'cap_\d\d(?:\.md)?|L\d+', d['resumen_teorico'])), key=lambda x: (x[0], x)))
