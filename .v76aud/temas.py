# -*- coding: utf-8 -*-
"""Fase ciega de la 76, D.29, D.37 y D.53 (copia de .v73aud/temas.py con los temas cambiados): para los asuntos de las 22
fichas de Gerber y para las partes que nombran los titulos que dicen cuantas tienen (las seis reglas del prototipo, los siete
pasos del programa, los cuatro componentes, los tres tipos de sistemas, las tres fases de d098), busca en GRAFO MAS BANDEJAS
(D.38.4, la poblacion de aduana.poblacion_de_bandejas) los ids cuyo id o titulo contiene la palabra. Imprime id, sede y libro,
nunca claves de relacion (R6). No escribe nada."""
import io, json, re, sys
sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding="utf-8")
from src import aduana, comun
nodos = list(comun.leer_jsonl(comun.RUTA_DATASET))
bandejas = list(aduana.poblacion_de_bandejas(fecha=aduana._hoy()))
ids_grafo = set(d['id'] for d in nodos)
print('poblacion: %d | por sede: grafo %d, bandeja %d | suma: %d' % (len(nodos) + len(bandejas), len(nodos), len(bandejas), len(nodos) + len(bandejas)))
temas = [
    ('regla 3: orden impecable', r'orden impecable|impecable|orden_imp'),
    ('regla 5: servicio uniforme y predecible', r'predecible|uniforme'),
    ('Primary Aim y proposito de vida', r'primary|proposito de vida|vida que quieres|objetivo primario'),
    ('Strategic Objective y estandares', r'strategic|objetivo estrategico|estandar'),
    ('Organizational Strategy: organigrama y contrato de puesto', r'organiza|organigrama|position contract|contrato de puesto'),
    ('Management Strategy y Marketing Strategy', r'management|marketing|gestion estrategica'),
    ('franquicia y prototipo', r'franquic|prototipo|replica'),
    ('contratacion', r'contrata|entrevist|candidato'),
    ('juego y reglas del juego', r'juego'),
    ('sistema de venta, guion y benchmark', r'venta|vender|guion|benchmark|script'),
    ('innovacion, cuantificacion y orquestacion', r'innova|cuantific|orquest'),
    ('sistemas', r'sistema'),
    ('manual de operaciones y documentacion', r'manual|document'),
    ('color, forma y vestuario', r'color|vestua|traje|ropa'),
    ('el emprendedor y el tecnico', r'emprend|tecnico|entrepreneur'),
    ('crecimiento y fases del negocio (d098)', r'crecim|infancia|adolescen|madurez|fase'),
    ('valor al cliente', r'valor'),
    ('plan escrito', r'plan'),
]
for nombre, pat in temas:
    hs = []
    for d in nodos + bandejas:
        t = (d.get('id', '') + ' | ' + (d.get('titulo') or '')).lower()
        if re.search(pat, t):
            hs.append((d.get('id'), 'grafo' if d.get('id') in ids_grafo else 'bandeja', [f.get('clave') for f in d.get('fuentes', [])][:1]))
    print('%s: %d' % (nombre, len(hs)))
    for h in hs: print('    %-66s %-7s %s' % h)
