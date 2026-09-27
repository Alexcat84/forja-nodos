# -*- coding: utf-8 -*-
"""Talla la fila del reporte de un insertar de la vuelta 67 desde su salida guardada.
    python .v67ext/fila.py <fila> <id> <commit_de_insercion>"""
import io, re, sys
fila, cid, commit = sys.argv[1:4]
t = io.open('.v67ext/insertar_%s_%s.txt' % (fila, cid), encoding='utf-8').read()
vec = re.findall(r'\n  vecino (\S+)  \[.*?\]\n    levantada por: (.*?)\n    similitud_texto\s+([\d.]+).*?\n    familia_id\s+([\d.]+).*?\n    paso_contra_nodo\s+([\d.]+)', t)
lin = re.findall(r'\n  --veredicto ([^|]+)\|([A-Z ]+)\|', t)
fin = re.search(r'fin .*? \| codigo de salida (\d+) \| ([\d.]+) s', t)
cola = re.findall(r'\n    (\S+ > \S+)\n    D\.29', t) or re.findall(r'ARISTAS EN COLA, sin cablear: \d+\n((?:    \S+ > \S+\n)+)', t)
res = 'INSERTADO' if 'NODO INSERTADO' in t else 'NO INSERTADO'
estado = 'BLOQUEARIA' if 'LA INSERCION QUEDA BLOQUEADA' in t else ('ENTRARIA' if res == 'INSERTADO' else '?')
print('### Fila `%s`: `%s`, **%s** en `%s` s, codigo `%s`, commit `%s`' % (int(fila), cid, res, fin.group(2), fin.group(1), commit))
print('')
print('La aduana de hoy: **%s** con `%d` vecino(s) contra `%s`; lineas `--veredicto` pasadas: `%d`. Salida entera en `.v67ext/insertar_%s_%s.txt`.' % (
    estado, len(vec), re.search(r'blocking multi señal contra (\d+)', t).group(1), len(lin), fila, cid))
print('')
print('<!-- TALLADO: parcial salida=.v67ext/insertar_%s_%s.txt -->' % (fila, cid))
print('')
print('| vecino que levanta hoy | levantada por | texto | familia | paso | linea pasada |')
print('|---|---|---:|---:|---:|---|')
dl = dict((a.strip(), b.strip()) for a, b in lin)
for v, por, s1, s2, s3 in vec:
    print('| `%s` | %s | %s | %s | %s | %s |' % (v, por, s1, s2, s3, dl.get(v, '**SIN LINEA**')))
for a, b in lin:
    if a.strip() not in [v[0] for v in vec]:
        print('| `%s` | **no levanta hoy** | | | | %s |' % (a.strip(), b.strip()))
m = re.search(r'ARISTAS EN COLA, sin cablear: \d+\n((?:    \S+ > \S+\n)+)', t)
if m:
    print('')
    print('**Arista en cola (`D.29`)**: ' + ', '.join('`%s`' % x.strip() for x in m.group(1).strip().split('\n')))
cab = re.findall(r'arista madre-hijo cableada[^:]*: (\S+ > \S+)', t)
if cab:
    print('')
    print('**Arista cableada por la aduana en el acto**: ' + ', '.join('`%s`' % x for x in cab))
