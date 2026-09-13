# -*- coding: utf-8 -*-
"""EL ESTADO AL CIERRE, RECOMPUTADO AL CIERRE (EXTRACTOR.md 4).

Toda cifra que describa el estado al cerrar se RECOMPUTA si algo de la propia
vuelta pudo haberla movido. Medir temprano y publicar tarde sin remedir es la
misma especie que citar sin mirar.
"""
import glob
import io
import os
import subprocess

APERTURA = {
    'nodos en el grafo': '203',
    'veredictos en bitacora': '148',
    'candidatos en cuarentena del lote 4': '113',
    'ficheros en cuarentena/_insertados': '201',
    'unidades en la bandeja del lote 4': '15',
}


def salida(orden):
    return subprocess.check_output(orden, shell=True).decode('utf-8', 'replace').strip()


AHORA = [
    ('nodos en el grafo', salida('wc -l < dataset/nodos.jsonl')),
    ('veredictos en bitacora', salida('wc -l < bitacora/VEREDICTOS.jsonl')),
    ('candidatos en cuarentena del lote 4',
     str(len(glob.glob('cuarentena/scott_radical_candor/*.json')))),
    ('ficheros en cuarentena/_insertados',
     str(len(glob.glob('cuarentena/_insertados/*/*.json')))),
    ('unidades en la bandeja del lote 4',
     str(len(glob.glob('fuentes/scott_radical_candor/*.md')))),
]

print('=' * 78)
print('1. EL ESTADO AL CIERRE CONTRA LA APERTURA')
print('=' * 78)
print('| medida | al abrir | al cerrar | se movio |')
print('|---|---:|---:|---|')
for nombre, ahora in AHORA:
    antes = APERTURA[nombre]
    movio = ('**SI, +%d**' % (int(ahora) - int(antes))) if ahora != antes else 'NO'
    print('| %s | %s | **%s** | %s |' % (nombre, antes, ahora, movio))

print('')
print('=' * 78)
print('2. LO QUE ESTA VUELTA ESCRIBIO EN CUARENTENA, CONTADO DE GIT')
print('=' * 78)
tocados = salida('git diff --name-only b05d040..HEAD -- cuarentena/ | wc -l')
nuevos = salida('git diff --diff-filter=A --name-only b05d040..HEAD -- cuarentena/ | wc -l')
print('ficheros de cuarentena tocados desde la apertura b05d040 : %s' % tocados)
print('de ellos NUEVOS                                          : %s' % nuevos)

print('')
print('=' * 78)
print('3. LAS SEDES QUE ESTA VUELTA NO TOCA, MEDIDO Y NO SUPUESTO')
print('=' * 78)
print('| sede | ficheros tocados desde `b05d040` |')
print('|---|---:|')
for sede in ('dataset/', 'bitacora/', 'censos/', 'config/', 'src/', 'esquema/', 'fuentes/'):
    n = salida('git diff --name-only b05d040..HEAD -- %s | wc -l' % sede)
    print('| `%s` | **%s** |' % (sede, n))
print('| `docs/` | **%s** |' % salida('git diff --name-only b05d040..HEAD -- docs/ | wc -l'))
