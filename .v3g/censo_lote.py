# -*- coding: utf-8 -*-
# Censo del lote en bandeja: una fila por candidato, todo leido del fichero.
import io, json, glob, os, sys

carpeta = sys.argv[1] if len(sys.argv) > 1 else 'cuarentena/grove_high_output'
filas = []
for p in sorted(glob.glob(carpeta + '/*.json')):
    d = json.load(io.open(p, encoding='utf-8'))
    pasos = d.get('pasos_accionables', [])
    filas.append((
        d.get('id', ''),
        len(pasos),
        len(d.get('nodos_previos', [])),
        len(d.get('nodos_siguientes', [])),
        d.get('dominio', ''),
        ','.join(sorted(set(f.get('clave', '') for f in d.get('fuentes', [])))),
        os.path.getmtime(p),
    ))
print('candidatos en %s : %d' % (carpeta, len(filas)))
print('%-52s %5s %4s %4s  %s' % ('id', 'pasos', 'prev', 'sig', 'dominio'))
tot = 0
for f in sorted(filas, key=lambda x: x[6]):
    tot += f[1]
    print('%-52s %5d %4d %4d  %s' % (f[0], f[1], f[2], f[3], f[4]))
print('TOTAL PASOS EN LA BANDEJA: %d' % tot)
