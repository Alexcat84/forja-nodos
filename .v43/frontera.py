# -*- coding: utf-8 -*-
"""La frontera de la vuelta 43: que hay en la bandeja, que aparta d005, y en
que orden manda el libro. Cuenta de los ficheros, no de ninguna pagina."""
import json, glob, re, io

APARTA = set()
for l in io.open('docs/loop/DEUDA.jsonl', encoding='utf-8'):
    l = l.strip()
    if not l:
        continue
    d = json.loads(l)
    if d.get('id') == 'd005':
        D005 = d['que']

# los seis del d005 se leen de los informes en seco de la linea grove, uno por fichero
for f in sorted(glob.glob('.v2g/informe_*.txt')):
    txt = io.open(f, encoding='utf-8', errors='replace').read()
    m = re.search(r'\[BLOQUEARIA\] (\w+)\s', txt)
    if m:
        APARTA.add(m.group(1))
APARTA = set(i for i in APARTA if glob.glob('cuarentena/grove_high_output/%s.json' % i))

filas = []
for p in sorted(glob.glob('cuarentena/grove_high_output/*.json')):
    d = json.load(io.open(p, encoding='utf-8'))
    rt = d.get('resumen_teorico', '')
    cap = re.search(r'fuentes/grove_high_output/(cap_\d+)\.md', rt)
    cap = cap.group(1) if cap else 'SIN CAP'
    pz = re.search(r'PIEZAS? (P\d+)', rt)
    pz = pz.group(1) if pz else '?'
    ln = re.findall(r'L(\d+) a L(\d+)', rt)
    l0 = int(ln[0][0]) if ln else 0
    filas.append({'id': d['id'], 'cap': cap, 'pieza': pz,
                  'orden': int(pz[1:]) if pz[1:].isdigit() else 999,
                  'L': l0, 'pasos': len(d['pasos_accionables'])})
# EL ORDEN LO MANDA EL LIBRO, Y SU UNIDAD ES LA PIEZA DE LA FRONTERA: las piezas
# estan numeradas en el orden del texto, asi que P2 va antes que P11 aunque dos
# fichas no citen su linea. La linea desempata dentro de una misma pieza.
filas.sort(key=lambda f: (f['cap'], f['orden'], f['L']))

print("LA BANDEJA DE cuarentena/grove_high_output, CONTADA DE SUS FICHEROS")
print()
print("| # | cap | pieza | candidato | pasos | d005 |")
print("|---:|---|---|---|---:|---|")
for n, f in enumerate(filas, 1):
    marca = "**APARTADO**" if f['id'] in APARTA else "entra"
    print("| %d | `%s` | `%s` | `%s` | %d | %s |"
          % (n, f['cap'], f['pieza'], f['id'], f['pasos'], marca))
print()
caps = {}
for f in filas:
    caps.setdefault(f['cap'], []).append(f)
print("| capitulo | en bandeja | apartados por `d005` | utiles |")
print("|---|---:|---:|---:|")
for c in sorted(caps):
    ap = sum(1 for f in caps[c] if f['id'] in APARTA)
    print("| `%s` | %d | %d | %d |" % (c, len(caps[c]), ap, len(caps[c]) - ap))
print("| **TOTAL** | **%d** | **%d** | **%d** |"
      % (len(filas), len(APARTA), len(filas) - len(APARTA)))
print()
utiles = [f for f in filas if f['id'] not in APARTA]
TECHO = 15
print("EL ORDEN DEL LIBRO, Y EL TECHO DE %d CORTA DONDE CORTA" % TECHO)
print()
print("| turno | cap | pieza | candidato | esta vuelta |")
print("|---:|---|---|---|---|")
for n, f in enumerate(utiles, 1):
    print("| %d | `%s` | `%s` | `%s` | %s |"
          % (n, f['cap'], f['pieza'], f['id'],
             "**SI**" if n <= TECHO else "pasa a la vuelta siguiente"))
