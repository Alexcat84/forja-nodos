# -*- coding: utf-8 -*-
"""LA MEDIDA DE FORMA QUE REGISTRE EN LA ACTA 46 (46.7) Y QUE D.56 ME MANDA REGISTRAR
Y NO ADJUDICAR: cuantos pasos de la tanda ABREN DECLARANDO en vez de ejecutando.
Verbos de apertura que no ordenan un acto sino que piden contar con algo."""
import json, re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
DECLARA = ('cuenta con', 'ten en cuenta', 'recuerda', 'acepta', 'comprueba lo que',
           'cuenta con lo que', 'toma el ejemplo', 'preguntate')
rutas = [l.strip() for l in open('.v48aud/02_candidatos_nuevos.out', encoding='utf-8') if l.strip()]
tot = dec = 0
for r in rutas:
    c = json.load(open(r, encoding='utf-8'))
    marcados = []
    for i, p in enumerate(c['pasos_accionables'], 1):
        b = p.lower()
        if any(b.startswith(v) for v in DECLARA):
            marcados.append((i, p[:90])); dec += 1
        tot += 1
    print('%-52s %d de %2d pasos abren declarando' % (c['id'][:52], len(marcados), len(c['pasos_accionables'])))
    for i, p in marcados: print('      paso %2d: %s...' % (i, p))
print()
print('TOTAL de la tanda de la vuelta 48: %d de %d pasos abren declarando y no ejecutando' % (dec, tot))
