# -*- coding: utf-8 -*-
"""LAS CIFRAS DEL CIERRE DE LA VUELTA 40, RECOMPUTADAS AL CIERRE.

`EXTRACTOR.md` 4: el estado al cierre se mide al cierre, y toda cifra que la propia
vuelta pudo mover se RECOMPUTA. Ninguna celda de aqui se copia de la apertura: la
columna `al abrir` sale de `.v40/apertura_tabla.txt`, que es un fichero, y la
columna `al cerrar` sale de contar el dato otra vez.
"""
import glob
import io
import json
import os
import re
import subprocess
import sys

if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def sh(c):
    return subprocess.run(c, shell=True, capture_output=True, text=True).stdout.strip()


def apertura():
    """Lee la columna de la apertura de su fichero, no de mi memoria."""
    valores = {}
    for linea in io.open('.v40/apertura_tabla.txt', encoding='utf-8'):
        if not linea.startswith('|') or linea.startswith('|---'):
            continue
        celdas = [c.strip() for c in linea.strip().strip('|').split('|')]
        if len(celdas) < 2 or celdas[0] == 'pieza':
            continue
        valores[celdas[0]] = celdas[1].replace('*', '').replace('`', '')
    return valores


ap = apertura()
nodos = [json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
vers = [json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()]

sig = sum(len(n.get('nodos_siguientes', [])) for n in nodos)
prev = sum(len(n.get('nodos_previos', [])) for n in nodos)
no_cons = sum(1 for v in vers
              if any(a.get('no_consumada') is True for a in v.get('anotaciones', [])))
band4 = len(glob.glob('cuarentena/scott_radical_candor/*.json'))
ins4 = len(glob.glob('cuarentena/_insertados/scott_radical_candor/*.json'))
band5 = len(glob.glob('cuarentena/marquet_turn_the_ship/*.json'))
instotal = len(glob.glob('cuarentena/_insertados/*/*.json'))

RX13 = re.compile(r'scott_radical_candor/cap_13\.md')
cap13_band = 0
for f in glob.glob('cuarentena/scott_radical_candor/*.json'):
    if RX13.search(io.open(f, encoding='utf-8').read()):
        cap13_band += 1
cap13_ins = 0
for f in glob.glob('cuarentena/_insertados/scott_radical_candor/*.json'):
    if RX13.search(io.open(f, encoding='utf-8').read()):
        cap13_ins += 1

filas = [
    ('nodos en `dataset/nodos.jsonl`', ap.get('nodos en `dataset/nodos.jsonl`'), len(nodos), '`dataset/nodos.jsonl`'),
    ('veredictos en `bitacora/VEREDICTOS.jsonl`', ap.get('veredictos en `bitacora/VEREDICTOS.jsonl`'), len(vers), '`bitacora/VEREDICTOS.jsonl`'),
    ('de ellos, con anotacion `no_consumada: true`', ap.get('de ellos, con alguna anotacion `no_consumada: true`'), no_cons, '`bitacora/VEREDICTOS.jsonl`'),
    ('aristas por `nodos_siguientes`', ap.get('aristas por `nodos_siguientes`'), sig, '`dataset/nodos.jsonl`'),
    ('aristas por `nodos_previos`', ap.get('aristas por `nodos_previos`'), prev, '`dataset/nodos.jsonl`'),
    ('candidatos en bandeja, lote 4', ap.get('candidatos en bandeja, lote 4'), band4, 'PATRON: `cuarentena/scott_radical_candor/*.json`'),
    ('de ellos, de `cap_13`', '6', cap13_band, 'PATRON: `cuarentena/scott_radical_candor/*.json`'),
    ('insertados y archivados, lote 4', ap.get('insertados y archivados, lote 4'), ins4, 'PATRON: `cuarentena/_insertados/scott_radical_candor/*.json`'),
    ('de ellos, de `cap_13`', '6', cap13_ins, 'PATRON: `cuarentena/_insertados/scott_radical_candor/*.json`'),
    ('candidatos en bandeja, lote 5', ap.get('candidatos en bandeja, lote 5'), band5, 'PATRON: `cuarentena/marquet_turn_the_ship/*.json`'),
    ('insertados y archivados, los cuatro lotes', ap.get('insertados y archivados, los cuatro lotes'), instotal, 'PATRON: `cuarentena/_insertados/*/*.json`'),
]

print('| pieza | al abrir | al cerrar | de donde sale |')
print('|---|---:|---:|---|')
for nombre, antes, ahora, sede in filas:
    antes = antes if antes is not None else '.'
    print('| %s | %s | **%s** | %s |' % (nombre, antes, ahora, sede))

print('')
print('LA SERIE D.37 DE LOS CUATRO ELEMENTOS, RECONTADA DEL GRAFO AL CERRAR')
CABEZA = 'pedir_critica_primero_crear_seguridad_psicologica'
PARTES = ['elegir_pregunta_recurrente_pedir_critica',
          'abrazar_incomodidad_silencio_contar_seis',
          'escuchar_entender_critica_dominar_defensa',
          'premiar_franqueza_hacer_escucha_tangible']
por_id = dict((n['id'], n) for n in nodos)
cabeza = por_id.get(CABEZA, {})
dentro = 0
cableadas = 0
for i, p in enumerate(PARTES, 1):
    esta = p in por_id
    cable = p in (cabeza.get('nodos_siguientes') or [])
    dentro += 1 if esta else 0
    cableadas += 1 if cable else 0
    print('  parte %d de 4  %-52s en el grafo: %-3s  cable desde la cabeza: %s'
          % (i, p[:52], 'SI' if esta else 'NO', 'SI' if cable else 'NO'))
print('  LA SERIE: %d de 4 partes en el grafo, %d de 4 aristas cableadas desde la cabeza'
      % (dentro, cableadas))
