import ast, sys, io, re

def cuerpo_inicio(path):
    lineas = io.open(path, encoding='utf-8').read().split('\n')
    cierres = [i+1 for i,l in enumerate(lineas) if l.strip() == '---']
    return cierres, len(io.open(path, encoding='utf-8').readlines())

def palabras(path, a, b):
    lineas = io.open(path, encoding='utf-8').readlines()
    trozo = ''.join(lineas[a-1:b])
    return len(trozo.split())

def mide(path, piezas_path):
    txt = io.open(piezas_path, encoding='utf-8').read()
    piezas = ast.literal_eval(txt)
    cierres, nlineas = cuerpo_inicio(path)
    ini = cierres[1] + 1
    fin = nlineas
    print('fichero            :', path)
    print('cierres yaml en    :', cierres[:2], ' -> cuerpo arranca en L%d' % ini)
    print('wc -l (mio)        :', nlineas)
    cubiertas = set()
    solapes = 0
    suma = 0
    print()
    print('%-5s %-12s %8s' % ('pieza','lineas','palabras'))
    for p in piezas:
        nom, a, b = p[0], p[1], p[2]
        w = palabras(path, a, b)
        suma += w
        for L in range(a, b+1):
            if L in cubiertas:
                solapes += 1
            cubiertas.add(L)
        print('%-5s L%-4d a L%-4d %8d' % (nom, a, b, w))
    cuerpo = palabras(path, ini, fin)
    sin_cubrir = [L for L in range(ini, fin+1) if L not in cubiertas]
    print()
    print('cuerpo L%d a L%d  palabras: %d' % (ini, fin, cuerpo))
    print('suma de piezas          : %d' % suma)
    print('residuo                 : %d' % (cuerpo - suma))
    print('lineas solapadas        : %d' % solapes)
    print('lineas sin cubrir       : %d' % len(sin_cubrir))
    print('piezas                  : %d' % len(piezas))
    print('primera linea de pieza  : L%d   ultima: L%d' % (piezas[0][1], piezas[-1][2]))

mide(sys.argv[1], sys.argv[2])
