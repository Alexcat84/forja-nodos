# -*- coding: utf-8 -*-
"""FRONTERA DE cap_14 MEDIDA POR EL AUDITOR, sin mirar la del extractor.
Los cortes son MI lectura del capitulo (los trece rotulos numerados del libro,
mas la cabeza de la serie, mas la pieza que monta el equipo, mas dos residuos).
El instrumento solo CUENTA: comprueba que las piezas cubren el cuerpo entero,
que no se solapan y que la suma cuadra al digito con wc -w del cuerpo.
"""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
RUTA = 'fuentes/scott_radical_candor/cap_14.md'
lineas = io.open(RUTA, encoding='utf-8').read().split('\n')
CUERPO_DESDE, CUERPO_HASTA = 8, 243

PIEZAS = [
    ('RESIDUO A', 8, 19, 'titulo y cinco parrafos de doctrina: separar desarrollo de gestion del desempenio'),
    ('P1', 21, 33, 'montar el equipo de gestion del desempenio y arrancar la revision'),
    ('P2', 35, 63, 'CABEZA DE SERIE: los trece elementos nombrados uno por linea'),
    ('P3', 65, 71, 'elemento 1, poner nota o no'),
    ('P4', 73, 93, 'elemento 2, categorias de la nota'),
    ('P5', 95, 97, 'elemento 3, escaleras de puesto'),
    ('P6', 99, 115, 'elemento 4, numero de notas'),
    ('P7', 117, 123, 'elemento 5, lenguaje de la nota'),
    ('P8', 125, 141, 'elemento 6, consecuencias de la nota'),
    ('P9', 143, 151, 'elemento 7, reparto de notas'),
    ('P10', 153, 169, 'elemento 8, curva forzada o no'),
    ('P11', 171, 185, 'elemento 9, calibracion'),
    ('P12', 187, 195, 'elemento 10, frecuencia'),
    ('P13', 197, 203, 'elemento 11, trescientos sesenta grados'),
    ('P14', 205, 219, 'elemento 12, transparente o confidencial'),
    ('P15', 221, 239, 'elemento 13, ligero o pesado'),
    ('RESIDUO B', 240, 243, 'CONCLUSION: no encarga nada, pide correo'),
]

def pal(a, b):
    return sum(len(lineas[i-1].split()) for i in range(a, b+1))

print('FRONTERA DE cap_14 MEDIDA POR EL AUDITOR')
print('fichero: %s' % RUTA)
print('cuerpo medido: lineas %d a %d' % (CUERPO_DESDE, CUERPO_HASTA))
print()
print('%-11s %-12s %8s  %s' % ('pieza', 'lineas', 'palabras', 'que es'))
total = 0
for n, a, b, q in PIEZAS:
    c = pal(a, b)
    total += c
    print('%-11s %-12s %8d  %s' % (n, '%d a %d' % (a, b), c, q))
cuerpo = pal(CUERPO_DESDE, CUERPO_HASTA)
print()
print('piezas                      : %d  (%d nodos y 2 residuos)' % (len(PIEZAS), len(PIEZAS)-2))
print('suma de las piezas          : %d' % total)
print('cuerpo entero (wc -w)       : %d' % cuerpo)
print('residuo sin cubrir          : %d' % (cuerpo - total))

cubiertas = set()
solapes = []
for n, a, b, q in PIEZAS:
    for i in range(a, b+1):
        if i in cubiertas:
            solapes.append(i)
        cubiertas.add(i)
fuera = [i for i in range(CUERPO_DESDE, CUERPO_HASTA+1) if i not in cubiertas]
no_vacias = [i for i in fuera if lineas[i-1].strip()]
print('lineas solapadas            : %d' % len(solapes))
print('lineas fuera de toda pieza  : %d, y de ellas NO vacias: %d' % (len(fuera), len(no_vacias)))
if no_vacias:
    print('  LAS NO VACIAS:', no_vacias)
print()
print('CIERRA AL DIGITO' if (cuerpo == total and not solapes and not no_vacias)
      else 'NO CIERRA')
