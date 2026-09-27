# -*- coding: utf-8 -*-
"""CRIBA MECANICA PREVIA A LA LECTURA A MANO. NO DECIDE NADA: ORDENA.

Para cada ocurrencia de numeral que `.t1_v21/cuentas21.py` lista, mira si el
NUMERAL EQUIVALENTE EN INGLES (o su digito) aparece dentro del tramo del libro
del que sale ese candidato, que el propio candidato declara en su resumen.

POR QUE NO BASTA Y LO DIGO ANTES DE ENSENIAR LA SALIDA: que `three` aparezca en
el tramo NO prueba que cuente lo mismo que mi `tres`. Ese es exactamente el falso
positivo que la vuelta 21 describio al escribir `cuentas21.py`. Por eso esta
criba solo sirve para ORDENAR la lectura: las que NO aparecen se leen primero
porque son las sospechosas, y las que aparecen se leen igual pero sabiendo que
hay un candidato a coincidencia en el tramo.
"""
import io
import json
import glob
import re
import sys

ING = {
    'dos': ['two', 'both', 'second', '2'],
    'tres': ['three', 'third', '3'],
    'cuatro': ['four', 'fourth', '4'],
    'cinco': ['five', 'fifth', '5'],
    'seis': ['six', 'sixth', '6'],
    'siete': ['seven', '7'],
    'ocho': ['eight', '8'],
    'nueve': ['nine', '9'],
    'diez': ['ten', '10'],
    'once': ['eleven', '11'],
    'doce': ['twelve', '12'],
    'quince': ['fifteen', '15'],
    'veinte': ['twenty', '20'],
    'treinta': ['thirty', '30'],
    'cuarenta': ['forty', '40'],
    'cincuenta': ['fifty', '50'],
    'cien': ['hundred', '100'],
    'ambas': ['both'],
    'ambos': ['both'],
    'sendas': ['each', 'both'],
}

CAP = sys.argv[1] if len(sys.argv) > 1 else 'cap_09'
LINEAS = open('fuentes/scott_radical_candor/%s.md' % CAP, encoding='utf-8').read().split('\n')

_ns = {'__name__': '__c21__'}
_out = io.StringIO()
_so = sys.stdout
sys.stdout = _out
try:
    exec(compile(io.open('.t1_v21/cuentas21.py', encoding='utf-8').read(),
                 '.t1_v21/cuentas21.py', 'exec'), _ns)
finally:
    sys.stdout = _so
CUENTAS = _ns['CUENTAS']

filas = []
for ruta in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
    d = json.load(io.open(ruta, encoding='utf-8'))
    r = d['resumen_teorico']
    caps = re.findall(r'cap_(\d\d)\.md', r) or re.findall(r'cap_(\d\d)', r)
    if not caps or 'cap_' + caps[0] != CAP:
        continue
    m = re.search(r'lineas?\s+(\d+)\s+a\s+(\d+)', r)
    if m:
        desde, hasta = int(m.group(1)), int(m.group(2))
    else:
        desde, hasta = 1, len(LINEAS)
    tramo = ' '.join(LINEAS[desde - 1:hasta]).lower()
    for j, paso in enumerate(d['pasos_accionables'], 1):
        for pal in CUENTAS:
            for mm in re.finditer(r'\b' + pal + r'\b', paso.lower()):
                hay = [w for w in ING[pal] if re.search(r'\b' + w + r'\b', tramo)]
                ini = max(0, mm.start() - 50)
                fin = min(len(paso), mm.end() + 70)
                filas.append((bool(hay), d['id'], j, pal, desde, hasta,
                              ','.join(hay) or 'NADA', paso[ini:fin]))

sosp = [f for f in filas if not f[0]]
ok = [f for f in filas if f[0]]
print('=' * 78)
print('CRIBA DE %s: %d ocurrencias' % (CAP, len(filas)))
print('=' * 78)
print('  el equivalente ingles NO aparece en el tramo : %d  <- se leen primero' % len(sosp))
print('  el equivalente ingles SI aparece en el tramo : %d' % len(ok))
print('')
print('--- LAS SOSPECHOSAS, UNA A UNA ---')
for _h, i, j, pal, a, b, _w, frag in sosp:
    print('%-50s paso %2d  [%s]  L%d-%d  ...%s...' % (i, j, pal, a, b, frag))
print('')
print('--- LAS QUE TIENEN CANDIDATO EN EL TRAMO (se leen igual) ---')
for _h, i, j, pal, a, b, w, frag in ok:
    print('%-50s paso %2d  [%s -> %s]  L%d-%d  ...%s...' % (i, j, pal, w, a, b, frag))
