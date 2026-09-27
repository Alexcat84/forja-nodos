# -*- coding: utf-8 -*-
"""El reporte de la vuelta 59 pega, bajo un `$ python scripts/cerrar_reporte.py`,
la linea `LA VIGENCIA TIENE COLA (71 RANCIO, fechados 2026-09-18, ajenos a esta
vuelta)`. El instrumento NO imprime ese parentesis. Cuento las fechas de los 71."""
import re, collections

txt = open('.v60aud/cerrar_reporte_60aud.txt', encoding='utf-8', errors='replace').read()
fechas = re.findall(r'\[RANCIO\][^\n]*?\(linea \d+, (\d{4}-\d{2}-\d{2})\)', txt)
print(r'$ grep -c "\[RANCIO\]" .v60aud/cerrar_reporte_60aud.txt')
print(len(re.findall(r'\[RANCIO\]', txt)))
print()
print('la linea de cuenta que el instrumento SI imprime:')
for l in txt.split('\n'):
    if 'RANCIO' in l and 'SIN HUELLA' in l:
        print('   ' + l.strip())
print()
print('fechas de esos hallazgos, contadas por mi:')
for f, n in sorted(collections.Counter(fechas).items()):
    print('   %s : %3d' % (f, n))
print('   %-10s : %3d' % ('TOTAL', len(fechas)))
