# -*- coding: utf-8 -*-
"""LA TANDA DE INSERCION, UNO POR VEZ Y EN EL ORDEN DEL LIBRO.

NO ES CARGA MASIVA Y NO LA SUSTITUYE: llama a `python forja.py insertar` una vez
por candidato, con su veredicto escrito cuando el par ya tiene veredicto mio, y
SE PARA en el primer candidato cuyo bloqueo traiga un par que no he leido. Un
veredicto que este guion no tenga escrito NO se inventa: para la tanda y lo
escribo yo.

Uso:
    python .v24/insertar_tanda.py            corre hasta el primer par sin veredicto
"""
import io
import json
import os
import re
import subprocess
import sys

ORDEN = '.v24/orden_insercion.txt'
SALIDAS = '.insercion_v24'
VEREDICTOS = '.v24/veredictos_insercion.json'
BANDEJA = 'cuarentena/scott_radical_candor'
INSERTADOS = 'cuarentena/_insertados/scott_radical_candor'

BLOQUEO = re.compile(r'^\s+vecino (\S+)', re.M)


def cargar_veredictos():
    if os.path.exists(VEREDICTOS):
        return json.load(io.open(VEREDICTOS, encoding='utf-8'))
    return {}


def main():
    veredictos = cargar_veredictos()
    pendientes = [l.split() for l in io.open(ORDEN, encoding='utf-8').read().split('\n') if l.strip()]
    hechos, parados = [], []
    for cap, identificador in pendientes:
        destino = os.path.join(INSERTADOS, identificador + '.json')
        if os.path.exists(destino):
            continue
        ruta = os.path.join(BANDEJA, identificador + '.json')
        if not os.path.exists(ruta):
            continue
        orden = [sys.executable, 'forja.py', 'insertar', ruta, '--sin-preguntas']
        for clave, valor in sorted(veredictos.items()):
            cand, vecino = clave.split('>')
            if cand == identificador:
                orden += ['--veredicto', '%s|%s' % (vecino, valor)]
        salida = subprocess.run(orden, capture_output=True, text=True)
        texto = (salida.stdout or '') + (salida.stderr or '')
        io.open(os.path.join(SALIDAS, identificador + '.txt'), 'w',
                encoding='utf-8', newline='').write(texto)
        if salida.returncode == 0 and 'NODO INSERTADO' in texto:
            # D.31: el insertado va a cuarentena/_insertados/<libro>/ EN EL MISMO
            # ACTO. La aduana no lo mueve: lo mueve quien inserta.
            if not os.path.isdir(INSERTADOS):
                os.makedirs(INSERTADOS)
            os.rename(ruta, destino)
            hechos.append((cap, identificador))
            print('OK   %s  %s' % (cap, identificador))
        else:
            vecinos = sorted(set(BLOQUEO.findall(texto)))
            parados.append((cap, identificador, vecinos))
            print('COLA %s  %s   vecinos por leer: %s'
                  % (cap, identificador, ', '.join(vecinos) or '(ver salida)'))
    print('')
    print('insertados en esta corrida : %d' % len(hechos))
    print('en cola de lectura         : %d' % len(parados))
    with io.open('.v24/cola_lectura.txt', 'w', encoding='utf-8', newline='') as f:
        for c, i, v in parados:
            f.write('%s %s %s' % (c, i, ','.join(v)) + chr(10))


if __name__ == '__main__':
    main()
