# ORDEN 1 de la TAREA BLOQUEANTE de la ACTA 18 seccion 7.5:
# la frontera se cierra contra el cuerpo o no se publica.
import io, sys

RUTA = 'fuentes/scott_radical_candor/cap_09.md'
lineas = io.open(RUTA, encoding='utf-8').read().split(chr(10))

filas = []
for l in io.open('.barrido_v20/frontera_cap09.tsv', encoding='utf-8'):
    l = l.rstrip(chr(10)).rstrip(chr(13))
    if not l.strip():
        continue
    a, b, clase, texto = l.split(chr(9), 3)
    filas.append((int(a), int(b), clase, texto))

CUERPO_DESDE = 8
CUERPO_HASTA = len(lineas)
while not (lineas[CUERPO_HASTA-1].strip() if CUERPO_HASTA <= len(lineas) else ''):
    CUERPO_HASTA -= 1

cubierto = {}
solapes = []
for a, b, clase, texto in filas:
    for n in range(a, b+1):
        if n in cubierto:
            solapes.append(n)
        cubierto[n] = clase

sin_cubrir = [n for n in range(CUERPO_DESDE, CUERPO_HASTA+1)
              if lineas[n-1].strip() and n not in cubierto]

def palabras(a, b):
    return sum(len(lineas[n-1].split()) for n in range(a, b+1))

suma_filas = sum(palabras(a, b) for a, b, _, _ in filas)
cuerpo = palabras(CUERPO_DESDE, CUERPO_HASTA)

print('CIERRE DE LA FRONTERA CONTRA EL CUERPO (ORDEN 1, ACTA 18 seccion 7.5)')
print('  cuerpo medido        : lineas %d a %d' % (CUERPO_DESDE, CUERPO_HASTA))
print('  lineas con contenido NO cubiertas      : %d   %s' % (len(sin_cubrir), sin_cubrir or ''))
print('  SOLAPES                                : %d   %s' % (len(solapes), solapes or ''))
print('  suma de las filas                      : %d palabras' % suma_filas)
print('  cuerpo medido aparte (sed 8,$ | wc -w) : %d palabras' % cuerpo)
print('  LOS DOS N SON EL MISMO                 : %s' % ('SI' if suma_filas == cuerpo else 'NO, faltan %d' % (cuerpo - suma_filas)))
print('')
si = [f for f in filas if f[2] == 'SI']
no = [f for f in filas if f[2] == 'NO']
print('  piezas de la frontera (wc -l del tsv)  : %d' % len(filas))
print('  piezas que DAN NODO                    : %d' % len(si))
print('  piezas que NO dan nodo                 : %d' % len(no))
print('  %d + %d = %d' % (len(si), len(no), len(si)+len(no)))
