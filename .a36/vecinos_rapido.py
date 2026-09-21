# -*- coding: utf-8 -*-
"""Mismo barrido D.38.4, con las DOS seniales baratas de la casa
(senal_similitud_texto y senal_familia_id, las mismas funciones de src/aduana.py
y los mismos config/umbrales.json). La tercera senial, paso contra nodo, es la
cara y corre aparte en .a36/vecinos.py: lo que esta lista NO trae va dicho."""
import json, glob, os, sys, io
sys.path.insert(0, os.getcwd())
from src import aduana, comun, config as modulo_config

umbrales = modulo_config.cargar()
u_texto = umbrales['umbral_similitud_texto']
u_fam = umbrales['umbral_familia_id']
tabla = comun.leer_json(comun.RUTA_FUENTES)
nodos = [json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
bandejas = aduana.poblacion_de_bandejas(tabla_fuentes=tabla)
print('POBLACION (D.38.4): %s' % aduana.Poblacion(len(nodos), len(bandejas)))
print('umbrales: texto %s, familia_id %s' % (u_texto, u_fam))
print()

def texto_de(n):
    return ' '.join([n.get('titulo', '')] + list(n.get('pasos_accionables', [])))

ids_grafo = set(n['id'] for n in nodos)
poblacion = nodos + bandejas
tramo = []
for f in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    r = d.get('resumen_teorico', '')
    if 'cap_12.md' in r or 'cap_13.md' in r:
        c, _ = aduana.normalizar_candidato(d)
        tramo.append(c)
print('CANDIDATOS DEL TRAMO: %d' % len(tramo))
print()
total = 0
for c in tramo:
    tc = texto_de(c)
    levantados = []
    for v in poblacion:
        if v['id'] == c['id']:
            continue
        st = aduana.senal_similitud_texto(tc, texto_de(v))
        sf = aduana.senal_familia_id(c['id'], v['id'])
        cuales = []
        if not isinstance(st, aduana.NoAplica) and st >= u_texto:
            cuales.append('texto=%.3f' % st)
        if not isinstance(sf, aduana.NoAplica) and sf >= u_fam:
            cuales.append('familia_id=%.3f' % sf)
        if cuales:
            levantados.append((v['id'], 'GRAFO' if v['id'] in ids_grafo else 'BANDEJA', cuales))
    total += len(levantados)
    print('%-52s %d vecino(s)' % (c['id'], len(levantados)))
    for i, d_, s in sorted(levantados):
        print('    %-8s %-52s %s' % (d_, i, ', '.join(s)))
    sys.stdout.flush()
print()
print('TOTAL DE PARES LEVANTADOS POR LAS DOS SENIALES BARATAS: %d' % total)
