# -*- coding: utf-8 -*-
"""Fase ciega de la 78, D.29, D.37 y D.53 (copia de .v76aud/temas.py con los temas cambiados): para los asuntos de las 20
fichas de Marquet (el control y sus dos pilares, competencia y claridad, que nombra cap_01), busca en GRAFO MAS BANDEJAS
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
    ('delegar decisiones y autoridad', r'delega|autoridad|decisi'),
    ('control', r'control'),
    ('intencion y permiso', r'intencion|intend|permiso'),
    ('recorrer, caminar, escuchar', r'recorr|escuch|camin|pasea'),
    ('reunion', r'reunion'),
    ('inspectores, auditores, inspeccion', r'inspec|auditor|regulador'),
    ('formacion, entrenamiento, aprendizaje', r'formacion|entrena|capacit|aprend'),
    ('principios y valores', r'principio|valores'),
    ('mensaje y repeticion', r'mensaje|repet'),
    ('seguimiento y pendientes', r'seguimiento|pendiente|monitor|vigil'),
    ('cierre de jornada, reporte, informar', r'cierre|jornada|informar|reporte'),
    ('meta, objetivo, metodo', r'meta|objetivo|metodo'),
    ('premios, reconocimiento, elogio', r'premi|reconoc|elogi'),
    ('errores y accion deliberada', r'error|deliberad|pausa'),
    ('solucion y urgencia', r'soluci|urgen'),
    ('plantilla, despedir, rotacion, contratar', r'despid|plantilla|rotacion|contrat'),
    ('frustracion, ideas, iniciativa', r'frustr|idea|iniciativa'),
    ('firmas, tramite, burocracia', r'firma|tramite|burocra'),
    ('informacion y su reparto', r'informacion|reparto'),
    ('responsable, a cargo, dueno', r'responsab|a cargo|dueno|propiedad'),
    ('liderazgo y lider', r'lider'),
    ('tarjetas y retiro', r'tarjeta|retiro|offsite'),
]
for nombre, pat in temas:
    hs = []
    for d in nodos + bandejas:
        t = (d.get('id', '') + ' | ' + (d.get('titulo') or '')).lower()
        if re.search(pat, t):
            hs.append((d.get('id'), 'grafo' if d.get('id') in ids_grafo else 'bandeja', [f.get('clave') for f in d.get('fuentes', [])][:1]))
    print('%s: %d' % (nombre, len(hs)))
    for h in hs: print('    %-66s %-7s %s' % h)
