# -*- coding: utf-8 -*-
"""Resume los 16 informes de aduana de la fase ciega (.v63aud/informe_<id>.txt):
por candidato, su poblacion, su veredicto de aduana y cada vecino con la senial que
lo levanto y el par de pasos. Un informe que no trae su linea de cierre se dice."""
import io, re
ids = io.open('.v63aud/tanda.txt', encoding='utf-8').read().split()
for i in ids:
    t = io.open('.v63aud/informe_%s.txt' % i, encoding='utf-8').read()
    cerrado = 'NADA SE INSERTO' in t
    pob = re.search(r'poblacion del barrido\s*:\s*(\d+)', t)
    ver = re.search(r'^\[(\w+)\] %s' % re.escape(i), t, re.M)
    print('%s  %s  poblacion %s  %s' % (ver.group(1) if ver else 'SIN VEREDICTO', i,
                                         pob.group(1) if pob else '?',
                                         '' if cerrado else 'SIN LINEA DE CIERRE'))
    for m in re.finditer(r'vecino (\S+)\s+\[levantada por: ([^\]]+)\]\n\s+similitud_texto ([\d.]+) \| familia_id ([\d.]+) \| paso_contra_nodo ([\d.]+)\n\s+(paso \d+ del candidato contra paso \d+) de', t):
        print('    %-52s %-28s texto %s familia %s paso %s  %s' % m.groups()[:6])
