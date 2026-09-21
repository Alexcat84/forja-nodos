# -*- coding: utf-8 -*-
"""LA CUENTA DEL LIBRO (`D.59`), CONTADA POR EL AUDITOR Y NO COPIADA (`8.3.1`).

La poblacion es la bandeja MAS lo que ya vive en el grafo: un capitulo que
produjo un candidato ya insertado SI dio candidato, y contar solo la bandeja lo
dejaria fuera. Es el error que esta acta declara en `60.13`.
"""
import glob
import io
import json
import re

LIB = 'grove_high_output'


def cap_de(resumen):
    m = re.search(r'fuentes/%s/(cap_\d\d)\.md' % LIB, resumen or '')
    return m.group(1) if m else None


caps = {}
band = sorted(glob.glob('cuarentena/%s/*.json' % LIB))
pasos_band = 0
sin_pasos = 0
for p in band:
    d = json.load(io.open(p, encoding='utf-8'))
    n = len(d.get('pasos_accionables') or [])
    pasos_band += n
    if n == 0:
        sin_pasos += 1
    c = cap_de(d.get('resumen_teorico'))
    caps.setdefault(c, [0, 0, 0])
    caps[c][0] += 1
    caps[c][1] += n

ins = []
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l)
    if any(f.get('clave') == LIB for f in d.get('fuentes', [])):
        n = len(d.get('pasos_accionables') or [])
        ins.append((d['id'], n))
        c = cap_de(d.get('resumen_teorico'))
        caps.setdefault(c, [0, 0, 0])
        caps[c][0] += 1
        caps[c][1] += n
        caps[c][2] += 1

print('LA CUENTA DEL LIBRO %s, CONTADA POR EL AUDITOR (D.59)' % LIB)
print('  capitulos del libro (ficheros cap_*.md) : %d'
      % len(glob.glob('fuentes/%s/cap_*.md' % LIB)))
print('  candidatos en la bandeja                : %d' % len(band))
print('  pasos_accionables en la bandeja         : %d' % pasos_band)
print('  fichas de la bandeja con CERO pasos     : %d' % sin_pasos)
print('  insertados en el grafo                  : %d' % len(ins))
for i, n in ins:
    print('     %s: %d pasos' % (i, n))
print('  pasos en los insertados                 : %d' % sum(n for _, n in ins))
print('  TOTAL cosechado del libro               : %d' % (len(band) + len(ins)))
print('  TOTAL pasos cosechados del libro        : %d'
      % (pasos_band + sum(n for _, n in ins)))
print()
print('  POR CAPITULO (bandeja MAS insertados), el capitulo leido del resumen_teorico:')
todos = ['cap_%02d' % i for i in range(1, 19)]
for c in todos:
    v = caps.get(c)
    if v:
        extra = '   [%d en el grafo]' % v[2] if v[2] else ''
        print('     %s: %2d candidato(s), %3d paso(s)%s' % (c, v[0], v[1], extra))
    else:
        print('     %s:  0 candidato(s),   0 paso(s)   <- DIO CERO' % c)
con = [c for c in todos if caps.get(c)]
sin = [c for c in todos if not caps.get(c)]
print()
print('  capitulos CON al menos un candidato: %d' % len(con))
print('  capitulos que DIERON CERO          : %d  %s' % (len(sin), sin))
print('  suma de control (por capitulo)     : %d candidatos, %d pasos'
      % (sum(v[0] for v in caps.values()), sum(v[1] for v in caps.values())))
print('  fichas sin capitulo legible        : %d'
      % (caps[None][0] if None in caps else 0))
