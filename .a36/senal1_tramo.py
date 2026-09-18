# -*- coding: utf-8 -*-
"""Los 91 pares del tramo entre si, con la senial 1 de la casa y con la misma
funcion sobre solo titulo+pasos. Mide CUANTOS pares cruzan el umbral por el
resumen_teorico y no por el procedimiento."""
import json, glob, sys, os, itertools
sys.path.insert(0, os.getcwd())
from src import aduana, comun
U = comun.leer_json('config/umbrales.json')['umbral_similitud_texto']

tramo = []
for f in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')
                + glob.glob('cuarentena/_insertados/scott_radical_candor/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    r = d.get('resumen_teorico', '')
    if 'cap_12.md' in r or 'cap_13.md' in r:
        tramo.append(d)
print('candidatos del tramo leidos (bandeja mas _insertados de esta vuelta): %d' % len(tramo))
print('umbral de la senial 1: %s' % U)

def solo(n):
    return comun.normalizar_texto(' '.join([n.get('titulo') or ''] + list(n.get('pasos_accionables') or [])))

pares = list(itertools.combinations(tramo, 2))
c_casa = c_pasos = c_solo_resumen = 0
for a, b in pares:
    casa = aduana.senal_similitud_texto(comun.texto_comparable(a), comun.texto_comparable(b))
    pas = aduana.senal_similitud_texto(solo(a), solo(b))
    if casa >= U:
        c_casa += 1
    if pas >= U:
        c_pasos += 1
    if casa >= U and pas < U:
        c_solo_resumen += 1
print('pares del tramo entre si: %d' % len(pares))
print('  cruzan el umbral con la senial 1 DE LA CASA (titulo+resumen+pasos): %d' % c_casa)
print('  cruzan el umbral con SOLO titulo+pasos                           : %d' % c_pasos)
print('  cruzan SOLO por el resumen_teorico                               : %d' % c_solo_resumen)
