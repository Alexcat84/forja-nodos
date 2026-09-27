# -*- coding: utf-8 -*-
"""Vuelta 64, TAREA 4: la matriz de senial entre los 22 candidatos de cap_02 y cap_03 de
grove, en los dos sentidos, con aduana.medir y las fichas de HOY (ya corregidas). Es lo que
el orden que lee (D.36) necesita: un par que levanta en un solo sentido se inserta de modo
que el que lo levanta entre DESPUES. Solo imprime los pares que levantan en algun sentido.
Uso: python .v64ext/matriz22.py <desde> <hasta>   (filas del candidato, 0 a 22)"""
import io, os, sys, time
sys.path.insert(0, os.getcwd())
from src import aduana, comun
from src import config as modulo_config
IDS = [l.split()[0] for l in io.open('.v64ext/los22.txt', encoding='utf-8') if l.strip() and not l.startswith('#')]
umbrales = modulo_config.cargar()
F = {}
for i in IDS:
    F[i], _ = aduana.normalizar_candidato(comun.leer_json('cuarentena/grove_high_output/%s.json' % i))
desde, hasta = int(sys.argv[1]), int(sys.argv[2])
t0 = time.time()
for a in IDS[desde:hasta]:
    for b in IDS:
        if a == b:
            continue
        m = aduana.medir(F[a], F[b], umbrales)
        if m['levantada_por']:
            s = m['senales']
            print('LEVANTA  %-48s -> %-48s texto %s familia %s paso %s  %s' % (
                a, b, s['similitud_texto'], s['familia_id'], s['paso_contra_nodo'], ', '.join(m['levantada_por'])))
    sys.stdout.flush()
print('FIN filas %d a %d de %d, %d pares medidos, %.0f s' % (desde, hasta, len(IDS), (hasta - desde) * (len(IDS) - 1), time.time() - t0))
