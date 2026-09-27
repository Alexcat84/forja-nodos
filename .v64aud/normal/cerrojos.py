# -*- coding: utf-8 -*-
"""Cual de los cerrojos de procesos/ es el del dataset de este arbol (src/cerrojo.py, ruta_de)."""
import glob, os, sys
sys.path.insert(0, os.getcwd())
from src import cerrojo
mio = os.path.basename(cerrojo.ruta_de('dataset/nodos.jsonl'))
print('cerrojo de dataset/nodos.jsonl en este arbol: %s' % mio)
for f in sorted(glob.glob('procesos/*.cerrojo')):
    b = os.path.basename(f)
    print('  %s  %s' % (b, 'ES EL DE ESTE DATASET' if b == mio else 'no es el de este dataset'))
