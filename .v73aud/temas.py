# -*- coding: utf-8 -*-
"""Fase ciega de la 73, D.29, D.37 y D.53 (copia de .v71aud/d37_partes.py con los temas cambiados): para los asuntos de las 7
fichas (la entrevista, la renuncia y la retencion, el reciclaje de un ascendido, y el entrenamiento: la lista, el curso,
la critica) y para las partes que nombran los dos titulos de la tanda que dicen cuantas tienen (el curso en siete pasos,
las nueve preguntas), busca en GRAFO MAS BANDEJAS (D.38.4, la poblacion de aduana.poblacion_de_bandejas) los ids cuyo id
o titulo contiene la palabra. Imprime id, sede y libro, nunca claves de relacion (R6). No escribe nada."""
import io, json, re, sys
sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding="utf-8")
from src import aduana, comun
nodos = list(comun.leer_jsonl(comun.RUTA_DATASET))
bandejas = list(aduana.poblacion_de_bandejas(fecha=aduana._hoy()))
ids_grafo = set(d['id'] for d in nodos)
print('poblacion: %d | por sede: grafo %d, bandeja %d | suma: %d' % (len(nodos) + len(bandejas), len(nodos), len(bandejas), len(nodos) + len(bandejas)))
temas = [
    ('la entrevista a un candidato', r'entrevist|candidato|contrata'),
    ('la renuncia y la retencion', r'renunci|retener|retencion|dimision|irse de la empresa'),
    ('el ascenso y el reciclaje', r'recicl|ascen|degrad|principio de peter|promocion|promover'),
    ('el entrenamiento', r'entrena|formacion|curso|ensen|capacit|clase'),
    ('la critica y la retroalimentacion del curso', r'critica anonima|formulario|encuesta'),
    ('el jefe del mando como ayuda', r'tu_jefe|tu propio jefe|propio_jefe|escalar al'),
    ('curso en siete pasos: el calendario', r'calendario'),
    ('curso en siete pasos: el esquema', r'esquema'),
    ('curso en siete pasos: los instructores', r'instructor'),
    ('nueve preguntas: debilidades, logros, fracasos', r'debilidad|logro|fracaso'),
]
for nombre, pat in temas:
    hs = []
    for d in nodos + bandejas:
        t = (d.get('id', '') + ' | ' + (d.get('titulo') or '')).lower()
        if re.search(pat, t):
            hs.append((d.get('id'), 'grafo' if d.get('id') in ids_grafo else 'bandeja', [f.get('clave') for f in d.get('fuentes', [])][:1]))
    print('%s: %d' % (nombre, len(hs)))
    for h in hs: print('    %-66s %-7s %s' % h)
