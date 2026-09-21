# cierre_frontera.py -- cierra la frontera contra el cuerpo SIN constantes:
# palabras del fichero = palabras del frontmatter + palabras del cuerpo.
import sys, io
for ruta in sys.argv[1:]:
    lineas = io.open(ruta, encoding='utf-8').read().split('\n')
    marcas = [i for i, l in enumerate(lineas) if l.strip() == '---']
    ini = marcas[1] + 1
    cab = sum(len(l.split()) for l in lineas[:ini])
    cue = sum(len(l.split()) for l in lineas[ini:])
    tot = sum(len(l.split()) for l in lineas)
    print('%-38s cabecera=%5d cuerpo=%5d suma=%6d fichero=%6d  CIERRA=%s'
          % (ruta, cab, cue, cab + cue, tot, 'SI' if cab + cue == tot else 'NO'))
