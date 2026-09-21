# -*- coding: utf-8 -*-
"""RELECTURA DE FIDELIDAD D.30 HECHA POR MI: cada paso de cada ficha al lado del
RENGLON del libro que su propia ficha cita. No adjudico con esto: lo imprimo para
poder leer los dos textos juntos y decidir TRANSCRIPCION o PUENTE con la vista.

El renglon se lee de fuentes/grove_high_output/cap_04.md, que no es ninguno de los
cuatro ficheros que D.34.2 retira."""
import json, re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
L = open('fuentes/grove_high_output/cap_04.md', encoding='utf-8').read().split('\n')
rutas = [l.strip() for l in open('.v48aud/02_candidatos_nuevos.out', encoding='utf-8') if l.strip()]
tot = 0
for r in rutas:
    c = json.load(open(r, encoding='utf-8'))
    rt = c['resumen_teorico']
    print('=' * 78)
    print('FICHA: %s' % c['id'])
    for i, p in enumerate(c['pasos_accionables'], 1):
        m = re.search(r'paso %d \(L(\d+)' % i, rt)
        cit = m.group(1) if m else None
        ren = L[int(cit) - 1] if cit else ''
        print('  PASO %2d  cita L%s' % (i, cit or '??'))
        print('     ficha : %s' % p)
        print('     libro : %s' % (ren[:400] + ('...' if len(ren) > 400 else '')))
        tot += 1
    print()
print('pasos impresos junto a su renglon: %d' % tot)
