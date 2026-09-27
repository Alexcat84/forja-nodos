# -*- coding: utf-8 -*-
"""LA TANDA DE INSERCION, UNO POR VEZ Y EN EL ORDEN PUBLICADO EN S.3.a.

NO ES CARGA MASIVA Y NO LA SUSTITUYE. Llama a `python forja.py insertar` UNA VEZ
POR CANDIDATO, con los veredictos que YO he escrito leyendo a los dos vecinos, y
cuando la aduana bloquea con un par que no tengo leido NO se inventa el veredicto:
ese candidato queda en cola, se sigue con el siguiente (D.36), y los pares nuevos
salen listados para que yo los lea y escriba su razon.

LO QUE ESTE GUION NO HACE, Y ES DELIBERADO:
  - no escribe ni una linea en bitacora/VEREDICTOS.jsonl: eso lo hace la aduana
  - no decide ningun veredicto: los lee de un fichero que escribo yo a mano
  - no mueve un candidato al grafo saltandose forja.py insertar

LO QUE SI HACE, Y LO MANDA D.31: mover el insertado a cuarentena/_insertados/<libro>/
EN EL MISMO ACTO en que entra. La aduana no lo mueve: lo mueve quien inserta.

Uso:
    python .v25/insertar_tanda.py <cuantos>    intenta como mucho <cuantos>
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ORDEN = '.v25/orden.txt'
SALIDAS = '.insercion_v25'
VEREDICTOS = ['.v24/veredictos_insercion.json', '.v25/veredictos_insercion.json']
BANDEJA = 'cuarentena/scott_radical_candor'
INSERTADOS = 'cuarentena/_insertados/scott_radical_candor'
COLA = '.v25/cola_lectura.txt'

BLOQUEO = re.compile(r'^\s+vecino (\S+)', re.M)


def cargar_veredictos():
    total = {}
    for ruta in VEREDICTOS:
        if os.path.exists(ruta):
            total.update(json.load(io.open(ruta, encoding='utf-8')))
    return total


def main():
    tope = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    veredictos = cargar_veredictos()
    if not os.path.isdir(SALIDAS):
        os.makedirs(SALIDAS)
    pendientes = [l.split() for l in io.open(ORDEN, encoding='utf-8').read().split('\n')
                  if l.strip()]
    hechos, parados = [], []
    intentados = 0
    for cap, ident in pendientes:
        if intentados >= tope:
            break
        destino = os.path.join(INSERTADOS, ident + '.json')
        ruta = os.path.join(BANDEJA, ident + '.json')
        if os.path.exists(destino) or not os.path.exists(ruta):
            continue
        intentados += 1
        orden = [sys.executable, 'forja.py', 'insertar', ruta, '--sin-preguntas']
        puestos = 0
        for clave, valor in sorted(veredictos.items()):
            cand, vecino = clave.split('>')
            if cand == ident:
                orden += ['--veredicto', '%s|%s' % (vecino, valor)]
                puestos += 1
        t0 = time.time()
        salida = subprocess.run(orden, capture_output=True, text=True)
        seg = time.time() - t0
        texto = (salida.stdout or '') + (salida.stderr or '')
        io.open(os.path.join(SALIDAS, ident + '.txt'), 'w',
                encoding='utf-8', newline='').write(texto)
        if salida.returncode == 0 and 'NODO INSERTADO' in texto:
            if not os.path.isdir(INSERTADOS):
                os.makedirs(INSERTADOS)
            os.rename(ruta, destino)                      # D.31, en el mismo acto
            hechos.append((cap, ident))
            print('OK   %-6s %-58s %3d veredictos  %5.1fs' % (cap, ident, puestos, seg))
        else:
            vecinos = sorted(set(BLOQUEO.findall(texto)))
            nuevos = [v for v in vecinos if ('%s>%s' % (ident, v)) not in veredictos]
            parados.append((cap, ident, vecinos, nuevos))
            print('COLA %-6s %-58s %5.1fs   pares SIN veredicto mio: %s'
                  % (cap, ident, seg, ', '.join(nuevos) or '(ninguno, ver salida)'))
        sys.stdout.flush()
    print('')
    print('intentados en esta corrida : %d' % intentados)
    print('INSERTADOS                 : %d' % len(hechos))
    print('en cola de lectura         : %d' % len(parados))
    with io.open(COLA, 'w', encoding='utf-8', newline='\n') as f:
        for c, i, v, n in parados:
            f.write('%s %s %s\n' % (c, i, ','.join(n)))


if __name__ == '__main__':
    main()
