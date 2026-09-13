# -*- coding: utf-8 -*-
"""LA TABLA `PASOS INVENTADOS POR CAPITULO`, CON EL DENOMINADOR REMEDIDO ENTERO POR MI.

El encargo la pide fila por capitulo mas total del lote, y dice que la escalada se
decide sobre el PEOR capitulo. El numerador de `cap_04` y `cap_05` es HEREDADO: lo
cito y no lo firmo, que es lo que la ACTA 20 6.2 hizo con el mismo numerador.

El reparto de los candidatos por capitulo NO se teclea: se deduce del propio
`resumen_teorico` de cada fichero, que es donde la casa escribe la unidad de
origen desde la vuelta 19. La fila de residuo `SIN` va publicada aunque sea cero,
que es la ORDEN A de la `ACTA 19` 7.4.
"""
import glob
import json
import os
import re
import subprocess

CUERPOS = {}
for ruta in sorted(glob.glob('fuentes/scott_radical_candor/cap_*.md')):
    cap = os.path.basename(ruta)[:-3]
    lineas = open(ruta, encoding='utf-8').read().split('\n')
    CUERPOS[cap] = len(' '.join(lineas[7:]).split())
    rotulo = ''
    for l in lineas[:7]:
        if l.startswith('unidad:'):
            rotulo = l.split(':', 1)[1].strip()
    CUERPOS[cap] = (CUERPOS[cap], rotulo)

# NUMERADORES HEREDADOS, citados y NO firmados por mi (ACTA 20 6.2).
HEREDADOS = {'cap_04': 3, 'cap_05': 2}

reparto = {}
sin_unidad = []
for ruta in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
    d = json.load(open(ruta, encoding='utf-8'))
    # EL PATRON ES `cap_NN` Y NO `cap_NN.md`, Y LO DIGO PORQUE MI PRIMERA
    # CORRIDA DE HOY FALLO POR AHI: `invitar_desafio_reciproco_equipo` nombra
    # su `cap_04` en prosa y sin extension, asi que con `.md` caia al residuo y
    # se me perdian 7 pasos de `cap_04`. Es la misma anchura que el instrumento
    # de la vuelta 20, que ya habia resuelto este caso (REPORTE O.2.e).
    m = re.search(r'cap_(\d+)', d.get('resumen_teorico', ''))
    if not m:
        sin_unidad.append(os.path.basename(ruta))
        continue
    cap = 'cap_' + m.group(1)
    reparto.setdefault(cap, []).append((d['id'], len(d['pasos_accionables'])))

print('| unidad | rotulo | cuerpo | candidatos | numerador | denominador | **tasa** | quien la firma |')
print('|---|---|---:|---:|---:|---:|---:|---|')
tot_cuerpo = tot_num = tot_den = tot_cand = 0
peor = (None, -1.0)
for cap in sorted(CUERPOS):
    if cap > 'cap_10':
        continue
    cuerpo, rotulo = CUERPOS[cap]
    ficha = reparto.get(cap, [])
    den = sum(n for _i, n in ficha)
    num = HEREDADOS.get(cap, 0)
    tot_cuerpo += cuerpo
    tot_num += num
    tot_den += den
    tot_cand += len(ficha)
    if den:
        tasa = '%.2f' % (100.0 * num / den)
        if float(tasa) > peor[1]:
            peor = (cap, float(tasa))
    else:
        tasa = 'sin definir'
    firma = 'denominador **mio**'
    if cap in HEREDADOS:
        firma += '; **numerador heredado, lo cito y no lo firmo**'
    if cap == 'cap_10':
        firma = '**numerador y denominador LOS FIRMO YO** (`O.3`)'
    print('| `%s` | `%s` | %s | %d | **%d** | **%d** | **%s** | %s |'
          % (cap, rotulo, '{:,}'.format(cuerpo).replace(',', '.'),
             len(ficha), num, den, tasa, firma))
print('| | **lote 4 hasta `cap_10`** | **%s** | **%d** | **%d** | **%d** | **%.2f** | denominador remedido entero por mi |'
      % ('{:,}'.format(tot_cuerpo).replace(',', '.'), tot_cand, tot_num, tot_den,
         100.0 * tot_num / tot_den))
print('')
print('| fila de residuo | valor | los nombres |')
print('|---|---:|---|')
print('| `SIN` unidad deducible del `resumen_teorico` | **%d** | %s |'
      % (len(sin_unidad), sin_unidad if sin_unidad else 'lista vacia'))
print('')
print('PEOR UNIDAD (la que decide la escalada) : %s con %.2f contra tope 10'
      % (peor[0], peor[1]))
print('candidatos repartidos                   : %d' % tot_cand)
print('candidatos en la bandeja                : %d'
      % len(glob.glob('cuarentena/scott_radical_candor/*.json')))
print('pasos del lote 4                        : %d' % tot_den)
print('')
print('MEDIDAS DEL CIERRE, recomputadas al cierre (EXTRACTOR.md 4)')
print('  nodos en el grafo        : %d'
      % sum(1 for l in open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()))
print('  veredictos en bitacora   : %d'
      % sum(1 for l in open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()))
print('  ficheros en _insertados  : %d'
      % len(glob.glob('cuarentena/_insertados/**/*.json', recursive=True)))
nodos = [json.loads(l) for l in open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
scott = sum(1 for n in nodos if 'scott_radical_candor'
            in [f.get('clave') for f in n.get('fuentes', [])])
extremos = sum(len(n.get('nodos_previos') or []) + len(n.get('nodos_siguientes') or [])
               for n in nodos)
print('  nodos con fuente scott   : %d de %d' % (scott, len(nodos)))
print('  extremos de arista       : %d   (aristas distintas: %d)'
      % (extremos, extremos // 2))
print('  unidades del libro       : %d'
      % len(glob.glob('fuentes/scott_radical_candor/cap_*.md')))
print('  cuerpo cap_11 a cap_14   : %d palabras'
      % sum(CUERPOS[c][0] for c in CUERPOS if c > 'cap_10'))
