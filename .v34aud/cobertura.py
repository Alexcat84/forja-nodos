# -*- coding: utf-8 -*-
"""QUE TROZO DE cap_09 ESTA EN EL GRAFO, QUE TROZO EN BANDEJA Y QUE TROZO EN NADIE.

Los rotulos salen del propio fichero del libro (lineas cortas no vacias, que es
como este libro marca sus cabeceras). La adscripcion sale del resumen_teorico de
cada nodo y de cada candidato. CERO LISTAS TECLEADAS.
"""
import io, json, os, re
RUTA = 'fuentes/scott_radical_candor/cap_09.md'
lineas = io.open(RUTA, encoding='utf-8').read().split('\n')
rot = [(i, l.strip()) for i, l in enumerate(lineas, 1)
       if l.strip() and len(l.strip()) < 110 and i > 7]

def donde(carpetas, grafo):
    d = {}
    for n in grafo:
        m = re.search(r'l[ií]neas? (\d+)\s*(?:a|-|hasta)\s*(\d+)', n.get('resumen_teorico') or '')
        if m and 'cap_09.md' in (n.get('resumen_teorico') or ''):
            d[int(m.group(1))] = (n['id'], int(m.group(2)), 'GRAFO')
    for c in carpetas:
        for f in sorted(os.listdir(c)):
            if not f.endswith('.json'): continue
            n = json.load(io.open(os.path.join(c, f), encoding='utf-8'))
            m = re.search(r'l[ií]neas? (\d+)\s*(?:a|-|hasta)\s*(\d+)', n.get('resumen_teorico') or '')
            if m and 'cap_09.md' in (n.get('resumen_teorico') or ''):
                d.setdefault(int(m.group(1)), (n['id'], int(m.group(2)), 'BANDEJA'))
    return d

grafo = [json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
d = donde(['cuarentena/scott_radical_candor'], grafo)
cubierto = set()
for a, (i, b, s) in d.items():
    cubierto |= set(range(a, b + 1))

print('| linea | rotulo del libro | quien lo tiene | donde |')
print('|---:|---|---|---|')
for i, txt in rot:
    if i in d:
        print('| L%d | %s | `%s` (L%d a L%d) | **%s** |' % (i, txt[:70], d[i][0], i, d[i][1], d[i][2]))
    elif i in cubierto:
        print('| L%d | %s | dentro de un nodo | . |' % (i, txt[:70]))
    else:
        print('| L%d | %s | **NADIE** | **.** |' % (i, txt[:70]))
print()
tot = len(lineas)
print('lineas del fichero          : %d' % tot)
print('lineas dentro de algun nodo : %d' % len(cubierto))
print('rotulos con nodo propio     : %d  (GRAFO %d, BANDEJA %d)'
      % (len(d), sum(1 for v in d.values() if v[2] == 'GRAFO'),
         sum(1 for v in d.values() if v[2] == 'BANDEJA')))
huecos = []
ini = None
for i in range(8, tot + 1):
    if i not in cubierto and lineas[i-1].strip():
        if ini is None: ini = i
    else:
        if ini is not None: huecos.append((ini, i - 1)); ini = None
if ini is not None: huecos.append((ini, tot))
print('tramos SIN nodo ninguno, con texto dentro:')
for a, b in huecos: print('  L%d a L%d' % (a, b))
