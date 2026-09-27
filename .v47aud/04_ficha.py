# -*- coding: utf-8 -*-
"""Ficha desnuda de cada candidato NACIDO en esta vuelta: id, titulo, unidad de
origen, cuantos pasos, cuantas fuentes, cuantas aristas. Cero interpretacion."""
import json, sys, io, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
NUEVOS = [l.strip() for l in open('.v47aud/02_candidatos_nuevos.out', encoding='utf-8') if l.strip()]
for ruta in NUEVOS:
    d = json.load(open(ruta, encoding='utf-8'))
    rt = d.get('resumen_teorico','')
    m = re.search(r'UNIDAD DE ORIGEN:\s*([^\n\.]+)', rt)
    print('=' * 78)
    print('fichero      :', os.path.basename(ruta))
    print('id           :', d.get('id'))
    print('titulo       :', d.get('titulo'))
    print('unidad origen:', m.group(1).strip() if m else '(NO LA DICE)')
    print('pasos        :', len(d.get('pasos', [])))
    print('fuentes      :', d.get('fuentes'))
    ar = d.get('aristas') or d.get('relaciones') or []
    print('aristas      :', len(ar), ar if ar else '')
    print('claves       :', sorted(d.keys()))
