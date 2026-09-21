# -*- coding: utf-8 -*-
"""Codigo del AUDITOR: recuenta la apertura del frente sin usar el script del extractor."""
import io, json, glob
unidades = sorted(glob.glob('fuentes/gerber_emyth/cap_*.md'))
def cuerpo(ruta):
    ls = io.open(ruta, encoding='utf-8').read().splitlines()
    c = [i + 1 for i, l in enumerate(ls) if l.strip() == '---']
    return sum(len(l.split()) for l in ls[c[1]:])
print('nodos en el grafo          : %d' % sum(1 for _ in io.open('dataset/nodos.jsonl', encoding='utf-8')))
print('veredictos escritos        : %d' % sum(1 for _ in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8')))
print('unidades de gerber_emyth   : %d' % len(unidades))
print('palabras de cuerpo del libro: %d' % sum(cuerpo(u) for u in unidades))
print('candidatos en bandeja      : %d' % len(glob.glob('cuarentena/gerber_emyth/*.json')))
canon = json.load(io.open('fuentes/FUENTES_CANONICAS.json', encoding='utf-8'))
print('clave gerber_emyth en canon: %s' % ('SI' if 'gerber_emyth' in canon else 'NO'))
