# -*- coding: utf-8 -*-
"""CORRE `.t1_v21/cuentas21.py` SOBRE cap_00 A cap_09. NO ES UN INSTRUMENTO NUEVO.

TAREA 4 de la vuelta 22 y moratoria de maquinaria (EXTRACTOR.md 13): el
instrumento ancho YA EXISTE y lo escribi yo en la vuelta 21. Lo que se encarga es
CORRERLO sobre otra poblacion, no escribir otro.

COMO SE GARANTIZA QUE ES EL MISMO Y NO UNO PARECIDO, que es lo unico que hace
verificable esta tarea: este guion NO reescribe la lista de numerales ni la
expresion regular. Ejecuta el fichero de la vuelta 21 y le SACA su propia
variable `CUENTAS` del espacio de nombres resultante. Si aquel fichero cambiara,
este cambiaria con el.

LO QUE PUBLICA, Y LO DICE CON SU NOMBRE: OCURRENCIAS, no numerador. Una ocurrencia
es un numeral dentro de un paso. Solo se vuelve numerador cuando alguien la lee
contra la linea del libro y decide si la cuenta la escribe el libro o la escribi
yo. Por eso el encargo acota la lectura a DOS capitulos.
"""
import io
import json
import glob
import os
import re
import sys

FICHERO_V21 = '.t1_v21/cuentas21.py'

# 1. EJECUTO EL DE LA VUELTA 21 Y ME QUEDO CON SU LISTA, sin copiarla.
_salida = io.StringIO()
_stdout = sys.stdout
sys.stdout = _salida
_ns = {'__name__': '__cuentas21__', '__file__': FICHERO_V21}
try:
    exec(compile(io.open(FICHERO_V21, encoding='utf-8').read(), FICHERO_V21, 'exec'), _ns)
finally:
    sys.stdout = _stdout
CUENTAS = _ns['CUENTAS']
CONTROL = _salida.getvalue().strip().split('\n')[-1]

print('=' * 78)
print('0. DE DONDE SALE EL CRITERIO: DEL FICHERO DE LA VUELTA 21, NO DE AQUI')
print('=' * 78)
print('fichero corrido      : %s' % FICHERO_V21)
print('numerales que caza   : %d  %s' % (len(CUENTAS), ', '.join(CUENTAS)))
print('su corrida de control sobre cap_10, HOY: %s' % CONTROL)
print('')
print('  LO QUE ESA LINEA ES Y LO QUE NO, y lo escribo aqui porque casi la publico')
print('  mal: son OCURRENCIAS de numeral en los 13 candidatos de cap_10 que el')
print('  fichero de la vuelta 21 lleva codificados, DESPUES de que aquella vuelta')
print('  retirase sus 22 cuentas atribuidas. El 22 de la vuelta 21 NO era esta')
print('  cifra: era el NUMERADOR que salio de leer estas ocurrencias una a una.')
print('  Una ocurrencia no es un puente hasta que alguien la lee contra la linea.')

# 2. REPARTO LOS CANDIDATOS POR CAPITULO, leyendo la marca de su resumen.
POR_CAP = {}
SIN_MARCA = []
NUEVOS_DE_HOY = set()
for ruta in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
    d = json.load(io.open(ruta, encoding='utf-8'))
    # PRIMERO la forma de RUTA DE ORIGEN (cap_NN.md), que es la marca fuerte.
    # Si no esta, la mencion suelta (cap_NN). LA SEGUNDA RAMA HACE FALTA Y LO
    # DIGO: `invitar_desafio_reciproco_equipo` nombra su cap_04 sin el `.md`, y
    # un patron con `.md` obligatorio pierde ese candidato y sus 7 pasos. Es la
    # misma especie de fallo que me cace en la vuelta 21, cazada hoy ANTES de
    # publicar la cifra porque la contraste con la ACTA 21 seccion 1.3.
    caps = re.findall(r'cap_(\d\d)\.md', d['resumen_teorico'])
    if not caps:
        caps = re.findall(r'cap_(\d\d)', d['resumen_teorico'])
    if not caps:
        SIN_MARCA.append(d['id'])
        continue
    POR_CAP.setdefault('cap_' + caps[0], []).append(d)

print('')
print('=' * 78)
print('1. EL REPARTO DE LA BANDEJA, CONTADO DEL FICHERO')
print('=' * 78)
total_c = total_p = 0
for cap in sorted(POR_CAP):
    n_c = len(POR_CAP[cap])
    n_p = sum(len(d['pasos_accionables']) for d in POR_CAP[cap])
    total_c += n_c
    total_p += n_p
    print('  %-8s candidatos=%3d  pasos=%4d' % (cap, n_c, n_p))
print('  %-8s candidatos=%3d  pasos=%4d' % ('TOTAL', total_c, total_p))
print('  SIN MARCA DE CAPITULO: %d  %s' % (len(SIN_MARCA), SIN_MARCA))

# 3. LA MEDIDA ENCARGADA: cap_00 a cap_09, OCURRENCIAS por capitulo.
ALCANCE = ['cap_%02d' % i for i in range(0, 10)]
print('')
print('=' * 78)
print('2. OCURRENCIAS DE NUMERAL POR CAPITULO, cap_00 A cap_09')
print('   (ES UNA MEDIDA DE OCURRENCIAS, NO UN NUMERADOR)')
print('=' * 78)
print('| unidad | candidatos | pasos | **ocurrencias** | ocurrencias por 100 pasos |')
print('|---|---:|---:|---:|---:|')
detalle = {}
gran_total = gran_pasos = 0
for cap in ALCANCE:
    ds = POR_CAP.get(cap, [])
    n_p = sum(len(d['pasos_accionables']) for d in ds)
    filas = []
    for d in ds:
        for j, paso in enumerate(d['pasos_accionables'], 1):
            for pal in CUENTAS:
                for m in re.finditer(r'\b' + pal + r'\b', paso.lower()):
                    ini = max(0, m.start() - 45)
                    fin = min(len(paso), m.end() + 60)
                    filas.append((d['id'], j, pal, paso[ini:fin]))
    detalle[cap] = filas
    gran_total += len(filas)
    gran_pasos += n_p
    tasa = ('%.2f' % (100.0 * len(filas) / n_p)) if n_p else 'sin definir'
    print('| `%s` | %d | %d | **%d** | %s |' % (cap, len(ds), n_p, len(filas), tasa))
print('| | **%d** | **%d** | **%d** | **%.2f** |'
      % (sum(len(POR_CAP.get(c, [])) for c in ALCANCE), gran_pasos, gran_total,
         100.0 * gran_total / gran_pasos))

peor = max(ALCANCE, key=lambda c: len(detalle[c]))
print('')
print('CAPITULO CON MAS OCURRENCIAS: %s con %d' % (peor, len(detalle[peor])))
print('EL OTRO QUE EL ENCARGO FIJA  : cap_04 con %d' % len(detalle['cap_04']))

# 4. EL DETALLE DE LOS DOS QUE SE LEEN A MANO.
for cap in [peor, 'cap_04']:
    print('')
    print('=' * 78)
    print('3. DETALLE PARA LEER A MANO: %s  (%d ocurrencias)' % (cap, len(detalle[cap])))
    print('=' * 78)
    for ident, j, pal, frag in detalle[cap]:
        print('%-46s paso %2d  [%s]  ...%s...' % (ident, j, pal, frag))
