# -*- coding: utf-8 -*-
"""Espera en PRIMER PLANO a que un insertar de .v75ext/insertar.py (COPIA DE LA VUELTA 75 de .v72ext/esperar.py, ruta cambiada; la de la 72 era COPIA de .v70ext/esperar.py) deje su marcador .fin.
    python .v75ext/esperar.py <fila> <id> [tope_s]
Sale 0 si termino (e imprime el codigo), 3 si agoto el tope y el insertar sigue vivo."""
import os, sys, time
base = '.v75ext/insertar_%s_%s' % (sys.argv[1], sys.argv[2])
tope = float(sys.argv[3]) if len(sys.argv) > 3 else 570
t0 = time.time()
while time.time() - t0 < tope:
    if os.path.exists(base + '.fin'):
        print('TERMINADO, codigo %s' % open(base + '.fin').read().strip()); sys.exit(0)
    time.sleep(5)
print('SIGUE EN VUELO tras %d s de espera (%s)' % (tope, time.strftime('%H:%M:%S'))); sys.exit(3)
