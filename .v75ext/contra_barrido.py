# -*- coding: utf-8 -*-
"""Compara los vecinos que levanta HOY la aduana de un insertar de la vuelta 75 (.v75ext/insertar_<fila>_<id>.txt) con los del
barrido de la 73 (.v73ext/vecinos_<id>.json); COPIA DE LA VUELTA 75 de .v72ext/contra_barrido.py con las rutas y el rotulo cambiados: cuantos, nuevos, caidos, seniales distintas y la poblacion. Solo lee.
    python .v75ext/contra_barrido.py <fila> <id>"""
import io, json, re, sys
f, cid = sys.argv[1:3]
t = io.open('.v75ext/insertar_%s_%s.txt' % (f, cid), encoding='utf-8').read()
hoy = dict((v, (float(a), float(b), float(c))) for v, a, b, c in re.findall(r'\n  vecino (\S+)  \[.*?\]\n    levantada por: .*?\n    similitud_texto\s+([\d.]+).*?\n    familia_id\s+([\d.]+).*?\n    paso_contra_nodo\s+([\d.]+)', t))
j = json.load(io.open('.v73ext/vecinos_%s.json' % cid, encoding='utf-8'))
ayer = dict((v['id'], (v['senales']['similitud_texto'], v['senales']['familia_id'], v['senales']['paso_contra_nodo'])) for v in j['vecinos'])
pob = re.search(r'contra (\d+)\s+\((\d+) del grafo mas (\d+)', t).groups()
print('hoy %d vecinos, barrido de la 73 %d | nuevos hoy: %s | que ya no levantan: %s | con senial distinta: %s | poblacion hoy %s (%s grafo, %s bandejas), en la 73 %d (%d, %d)' % (
  len(hoy), len(ayer), sorted(set(hoy)-set(ayer)) or 0, sorted(set(ayer)-set(hoy)) or 0,
  [v for v in hoy if v in ayer and hoy[v] != ayer[v]] or 0, pob[0], pob[1], pob[2], j['grafo']+j['bandejas'], j['grafo'], j['bandejas']))
