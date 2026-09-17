# piezas.py -- suma palabras por rango de lineas.
# PRIMERA LINEA DE SALIDA (heredado 4): LOS RANGOS LOS TECLEO YO, salen de MI
# LECTURA y no del dato. Lo que el instrumento aporta son las PALABRAS y la
# COBERTURA; ni una cifra de este fichero la cuento a ojo.
import sys, io
ruta = sys.argv[1]
lineas = io.open(ruta, encoding='utf-8').read().split('\n')
marcas = [i for i, l in enumerate(lineas) if l.strip() == '---']
ini = marcas[1] + 1
print('INSTRUMENTO piezas.py  CONSTANTE TECLEADA DENTRO: SI, los RANGOS de linea, que son MI LECTURA. Las palabras y la cobertura las mide el fichero.')
print('fichero=%s' % ruta)
cubierto = set()
total_p = 0
for arg in sys.argv[2:]:
    nombre, rango = arg.split('=')
    a, b = rango.split(':')
    a, b = int(a), int(b)
    p = 0
    n = 0
    for i in range(a - 1, b):
        t = lineas[i].strip()
        if not t:
            continue
        p += len(t.split())
        n += 1
        cubierto.add(i)
    total_p += p
    print('%-6s L%-4d a L%-4d  lineas=%2d  palabras=%5d' % (nombre, a, b, n, p))
sin = []
for i, l in enumerate(lineas):
    if i < ini or not l.strip():
        continue
    if i not in cubierto:
        sin.append(i + 1)
cuerpo = sum(len(l.strip().split()) for i, l in enumerate(lineas) if i >= ini and l.strip())
print('SUMA DE LAS PIEZAS: %d palabras' % total_p)
print('CUERPO ENTERO:      %d palabras' % cuerpo)
print('LINEAS DE CUERPO SIN PIEZA: %d  ->  %s' % (len(sin), sin))
print('SOLAPES: %s' % ('NO' if total_p == sum(len(lineas[i].strip().split()) for i in cubierto) else 'SI'))
