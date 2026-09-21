# -*- coding: utf-8 -*-
"""Tabla del libro gerber_emyth entero, cap_01 a cap_22, fundiendo tres fuentes
medidas en esta vuelta: docs/loop/TABLERO.jsonl (grafo+bandejas), config/frentes.json
(minados_en_cero, firmado por el auditor via acta) y cuarentena/gerber_emyth/*.json
(candidatos por su UNIDAD DE ORIGEN). No inserta ni modifica nada: solo lee e imprime."""
import json, glob, os, re

minados = set()
with open('docs/loop/TABLERO.jsonl', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        d = json.loads(line)
        if d.get('clave') == 'gerber_emyth':
            minados = set(d['capitulos_minados'])

frentes = json.load(open('config/frentes.json', encoding='utf-8'))
cero = frentes['minados_en_cero']['gerber_emyth']
cero_caps = set(cero['capitulos'])
cero_cita = cero['cita']

cands = glob.glob('cuarentena/gerber_emyth/*.json')
por_cap = {}
for c in cands:
    txt = open(c, encoding='utf-8').read()
    m = re.search(r'UNIDAD DE ORIGEN:\s*fuentes/gerber_emyth/(cap_\d+)\.md', txt)
    cap = m.group(1) if m else 'SIN_DECLARAR'
    por_cap.setdefault(cap, []).append(os.path.basename(c))

VUELTA9 = {'cap_01', 'cap_02', 'cap_03'}

print('| capitulo | estado | candidatos | firma |')
print('|---|---|---:|---|')
for i in range(1, 23):
    cap = 'cap_%02d' % i
    n = len(por_cap.get(cap, []))
    if cap in VUELTA9:
        estado = 'MINADO EN CERO'
        firma = 'vuelta 9, este reporte (G9.2/G9.3/G9.4), sin acta todavia'
    elif cap in cero_caps:
        estado = 'MINADO EN CERO'
        firma = cero_cita
    elif cap in minados:
        estado = 'MINADO CON CANDIDATOS'
        firma = 'TABLERO.jsonl, grafo+bandejas'
    else:
        estado = 'SIN MINAR'
        firma = 'ninguna'
    print('| `%s` | %s | %d | %s |' % (cap, estado, n, firma))

total_cand = sum(len(v) for v in por_cap.values())
print()
print('total capitulos: 22   minados: %d   candidatos en bandeja: %d'
      % (len(minados) + len(VUELTA9), total_cand))
