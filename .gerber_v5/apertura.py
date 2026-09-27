# -*- coding: utf-8 -*-
"""LA APERTURA DEL FRENTE gerber_emyth, MEDIDA ANTES DE LA PRIMERA OPERACION
(EXTRACTOR.md 4). Cero celdas tecleadas: cada fila sale de contar su fichero."""
import io, json, os, glob, subprocess

def g(*a):
    return subprocess.check_output(['git'] + list(a)).decode('utf-8', 'replace').strip()

nodos = sum(1 for _ in io.open('dataset/nodos.jsonl', encoding='utf-8'))
ver = sum(1 for _ in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8'))
unidades = sorted(glob.glob('fuentes/gerber_emyth/cap_*.md'))
reservado = sorted(glob.glob('fuentes/gerber_emyth_cap17_reservado/*.md'))
bandeja = sorted(glob.glob('cuarentena/gerber_emyth/*.json'))
canon = json.load(io.open('fuentes/FUENTES_CANONICAS.json', encoding='utf-8'))

def cuerpo(ruta):
    ls = io.open(ruta, encoding='utf-8').read().splitlines()
    c = [i + 1 for i, l in enumerate(ls) if l.strip() == '---']
    return sum(len(l.split()) for l in ls[c[1]:])

print('AVISO: cero celdas tecleadas. Cada fila cuenta su propio fichero, y el')
print('cuerpo de cada unidad arranca en la linea siguiente al segundo --- de su')
print('cabecera yaml, derivado del fichero y no puesto por mi.')
print('')
print('| pieza | al abrir | de donde sale |')
print('|---|---:|---|')
print('| nodos en el grafo | **%d** | `dataset/nodos.jsonl` |' % nodos)
print('| veredictos escritos | **%d** | `bitacora/VEREDICTOS.jsonl` |' % ver)
print('| unidades de `gerber_emyth` | **%d** | `PATRON: fuentes/gerber_emyth/cap_*.md` |' % len(unidades))
print('| palabras de cuerpo del libro | **%d** | `PATRON: fuentes/gerber_emyth/cap_*.md` |'
      % sum(cuerpo(u) for u in unidades))
print('| unidades apartadas del `cap. 17` | **%d** | `PATRON: fuentes/gerber_emyth_cap17_reservado/*.md` |' % len(reservado))
print('| candidatos en bandeja de `gerber_emyth` | **%d** | `PATRON: cuarentena/gerber_emyth/*.json` |' % len(bandeja))
print('| clave `gerber_emyth` en la tabla canonica | **%s** | `fuentes/FUENTES_CANONICAS.json` |'
      % ('SI' if 'gerber_emyth' in canon else 'NO'))
print('| claves en la tabla canonica | **%d** | `fuentes/FUENTES_CANONICAS.json` |'
      % sum(1 for k in canon if not k.startswith('_')))
print('| rama activa | `%s` | `git rev-parse --abbrev-ref HEAD` |' % g('rev-parse', '--abbrev-ref', 'HEAD'))
print('| commit de apertura | `%s` | `git rev-parse --short HEAD` |' % g('rev-parse', '--short', 'HEAD'))
print('')
print('| unidad | fichero | rotulo | palabras de cuerpo |')
print('|---|---|---|---:|')
for u in unidades:
    ls = io.open(u, encoding='utf-8').read().splitlines()
    rot = [l.split(':', 1)[1].strip() for l in ls[:7] if l.startswith('unidad:')][0]
    tit = [l.split(':', 1)[1].strip() for l in ls[:7] if l.startswith('titulo_textual:')][0]
    print('| %s | `%s` | %s | **%d** |' % (rot, os.path.basename(u), tit, cuerpo(u)))
