# -*- coding: utf-8 -*-
"""Fase ciega de la 65: las aristas del dataset que tocan a las 20 filas de la tanda, contra las que
mi lectura adjudicada espera: las 8 SOSTENGO de .v64ext/aristas_lectura.txt y los CONTINUA con madre
de .v64ext/veredictos_listos.txt cuyos dos extremos estan en las 20 (ACTA 63 63.3). Mira tambien que
cada arista este escrita en los dos extremos (siguientes de la madre y previos del hijo)."""
import io, json, re
tanda = [l.split()[1] for l in io.open('.v64ext/orden.txt', encoding='utf-8') if l[:1].isdigit() and 1 <= int(l.split()[0]) <= 20]
T = set(tanda)
n = {json.loads(l)['id']: json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8')}
hay = set()
for i, x in n.items():
    for h in x.get('nodos_siguientes') or []:
        if i in T or h in T: hay.add((i, h))
    for m in x.get('nodos_previos') or []:
        if i in T or m in T: hay.add((m, i))
espera = {}
for l in io.open('.v64ext/aristas_lectura.txt', encoding='utf-8'):
    if l.startswith('SOSTENGO'):
        c = [x.strip() for x in l.split('|')]; espera[(c[1], c[2])] = 'lectura SOSTENGO'
cand = None
for l in io.open('.v64ext/veredictos_listos.txt', encoding='utf-8'):
    if l.startswith('## '): cand = l[3:].strip(); continue
    m = re.match(r'(\w+)\|CONTINUA\|madre=(\w+)\|', l)
    if m and cand:
        v, madre = m.group(1), m.group(2); hijo = v if madre == cand else cand
        if madre in T and hijo in T: espera.setdefault((madre, hijo), 'veredicto CONTINUA')
        else: print('FUERA DE LA TANDA (no se espera en el grafo): %s > %s' % (madre, hijo))
for a in sorted(hay | set(espera)):
    m, h = a
    dos = (h in (n.get(m, {}).get('nodos_siguientes') or [])) and (m in (n.get(h, {}).get('nodos_previos') or []))
    print('%-11s %-48s > %-48s %s%s' % ('ESTA' if a in hay else 'NO ESTA', m, h, espera.get(a, 'SIN LECTURA MIA'),
                                        '' if a not in hay else (' | en los dos extremos' if dos else ' | EN UN SOLO EXTREMO')))
print('aristas que tocan la tanda: %d | esperadas por mi lectura: %d | esperadas y presentes: %d | esperadas y ausentes: %d | presentes sin lectura mia: %d'
      % (len(hay), len(espera), len(hay & set(espera)), len(set(espera) - hay), len(hay - set(espera))))
