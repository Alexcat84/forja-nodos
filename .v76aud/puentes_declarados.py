# -*- coding: utf-8 -*-
"""Fase ciega de la 76: de cada CORRECCION DECLARADA DE LA VUELTA 76 en las fichas de la bandeja de Gerber, la cifra que ella misma
publica (N TRANSCRIPCION y M PUENTE sobre el texto viejo) y los pasos que dice que cambian (El paso N decia / Los pasos N, M y K).
Suma los PUENTE que las fichas declaran, con su suma (R7). Solo lee."""
import io, json, glob, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
tot = 0; filas = []
for f in sorted(glob.glob('cuarentena/gerber_emyth/*.json')):
    r = json.load(io.open(f, encoding='utf-8')).get('resumen_teorico', '')
    for m in re.finditer(r'CORRECCION DECLARADA DE LA VUELTA 76', r):
        t = r[m.start():]
        p = re.search(r'(\d+) TRANSCRIPCION y (\d+) PUENTE sobre el texto viejo', t)
        n = int(p.group(2)) if p else 0; tot += n
        filas.append((os.path.basename(f)[:-5], n, ' '.join(re.findall(r'EL PASO \d+|LOS PASOS [\d, Y]+|EL ENTREGABLE|LA CONDICION', t[:400]))))
for i, n, q in filas: print('%-50s PUENTE sobre el texto viejo: %d | %s' % (i, n, q))
print('fichas con correccion de la 76: %d | PUENTE que declaran, suma: %d' % (len(filas), tot))
