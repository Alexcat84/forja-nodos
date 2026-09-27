# -*- coding: utf-8 -*-
"""Foto del estado con su hora. Cuenta lineas del grafo y de la bitacora,
candidatos por bandeja y cerrojos vivos en procesos/ (D.53). NO abre ninguna
razon de veredicto: en fase ciega eso seria leer lo que vengo a leer a ciegas."""
import io, os, glob, json, time

def lineas(r):
    return sum(1 for l in io.open(r, encoding='utf-8') if l.strip())

print('HORA DE ESTA FOTO: %s' % time.strftime('%Y-%m-%d %H:%M:%S'))
print('  dataset/nodos.jsonl        : %d lineas' % lineas('dataset/nodos.jsonl'))
print('  bitacora/VEREDICTOS.jsonl  : %d lineas' % lineas('bitacora/VEREDICTOS.jsonl'))
print('  bandeja scott_radical_candor : %d candidatos'
      % len(glob.glob('cuarentena/scott_radical_candor/*.json')))
print('  cuarentena/_insertados/scott_radical_candor : %d ficheros'
      % len(glob.glob('cuarentena/_insertados/scott_radical_candor/*.json')))
cerrojos = glob.glob('procesos/*.cerrojo')
print('  cerrojos vivos en procesos/ : %d' % len(cerrojos))
for c in cerrojos:
    print('    %s -> %s' % (os.path.basename(c), io.open(c, encoding='utf-8').read().strip()))
