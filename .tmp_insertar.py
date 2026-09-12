# -*- coding: utf-8 -*-
"""Conductor de la insercion del lote 3.

NO ES UNA CARGA MASIVA Y NO EMITE NI UN VEREDICTO. Corre
`python forja.py insertar <candidato>.json --sin-preguntas`, UNA VEZ POR
CANDIDATO, en el orden de `.orden_insercion_lote3.txt`, y SE DETIENE EN EL
PRIMER CODIGO DISTINTO DE CERO. Cuando la aduana bloquea, el que lee a los
vecinos y escribe el veredicto con su razon es el extractor, a mano, y el
candidato se reintenta con `--veredicto` desde la linea de ordenes.

Cada candidato que entra se archiva en cuarentena/_insertados/<libro>/ EN EL
MISMO ACTO (D.31).
"""
import io, os, subprocess, sys

ORDEN = '.orden_insercion_lote3.txt'
BANDEJA = 'cuarentena/zhuo_manager'
ARCHIVO = 'cuarentena/_insertados/zhuo_manager'
LOG = '.insercion_lote3_vuelta15.log'

lineas = [l.split() for l in io.open(ORDEN, encoding='utf-8').read().splitlines() if l.strip()]
log = io.open(LOG, 'a', encoding='utf-8')
hechos = 0
for num, cap, nodo in lineas:
    origen = os.path.join(BANDEJA, nodo + '.json')
    if not os.path.exists(origen):
        continue
    cmd = [sys.executable, 'forja.py', 'insertar', origen, '--sin-preguntas']
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    salida = (r.stdout or '') + (r.stderr or '')
    log.write('\n$ %s\n' % ' '.join(cmd))
    log.write(salida)
    log.write('[codigo %d]\n' % r.returncode)
    log.flush()
    if r.returncode != 0:
        print('PARADA en #%s %s   codigo %d' % (num, nodo, r.returncode))
        print(salida[-3000:])
        print('insertados en esta corrida:', hechos)
        sys.exit(r.returncode)
    subprocess.run(['git', 'mv', origen, os.path.join(ARCHIVO, nodo + '.json')], check=True)
    hechos += 1
    print('#%s %s OK y archivado' % (num, nodo), flush=True)
print('CORRIDA COMPLETA. insertados en esta corrida:', hechos)
