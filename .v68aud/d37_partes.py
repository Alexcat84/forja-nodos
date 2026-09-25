# -*- coding: utf-8 -*-
"""Fase ciega de la 68, D.37: para los dos titulos de la tanda que dicen cuantas partes tienen y las nombran
(usar_tres_clases_reunion_proceso y zanjar_seis_preguntas_decision_adelantado), busca en GRAFO MAS BANDEJAS (D.38.4, la
poblacion de aduana.poblacion_de_bandejas) los ids cuyo id o titulo contiene la palabra de cada parte. Imprime id y
libro, nunca claves de relacion (R6). No escribe nada."""
import io, json, re, sys
sys.path.insert(0, '.')
from src import aduana, comun
nodos = list(comun.leer_jsonl(comun.RUTA_DATASET))
bandejas = list(aduana.poblacion_de_bandejas(fecha=aduana._hoy()))
print('poblacion: %d' % (len(nodos) + len(bandejas)))
partes = [
    ('tres clases: uno a uno', r'uno_a_uno|uno a uno|reunion_individual|reunion individual'),
    ('tres clases: reunion de personal', r'reunion_personal|reunion de personal|reunion_equipo|reunion de equipo'),
    ('tres clases: revision de operaciones', r'revision_operaciones|revision de operaciones'),
    ('seis preguntas: que decision', r'que_decision|que decision'),
    ('seis preguntas: cuando', r'cuando_decid|plazo_decision|cuando tiene que estar'),
    ('seis preguntas: quien decide', r'quien_decide|quien decide|decisor'),
    ('seis preguntas: a quien consultar', r'consultar|consulta'),
    ('seis preguntas: quien ratifica o veta', r'ratific|vet[ao]'),
    ('seis preguntas: a quien informar', r'informar_decision|informar de la decision|comunicar_decision|comunicar la decision'),
]
for nombre, pat in partes:
    hs = []
    for d in nodos + bandejas:
        t = (d.get('id', '') + ' | ' + (d.get('titulo') or '')).lower()
        if re.search(pat, t):
            hs.append((d.get('id'), [f.get('clave') for f in d.get('fuentes', [])][:1]))
    print('%s: %d' % (nombre, len(hs)))
    for h in hs: print('    %-60s %s' % h)
