# -*- coding: utf-8 -*-
"""AVISO EN LA PRIMERA LINEA DE SALIDA (REMEDIO 4 de la ACTA 30): este instrumento
SI lleva una constante tecleada dentro, y es MI CLASE por pieza. No puede salir del
dato porque es un juicio y no una medida. Lo que NO esta teclado y sale del fichero:
los numeros de linea, el reparto de palabras, la suma y la comprobacion de cobertura.

MI FRONTERA CIEGA DE cap_03, antes de ver ninguna frontera del extractor.
    P = pieza con procedimiento propio, yo escribiria nodo de ella
    R = residuo, yo NO escribiria nodo de ella
CERO ESCRITURAS sobre el arbol.

    python .marquet_v1/mi_frontera_cap03.py
"""
import io, os, sys
sys.path.insert(0, os.path.abspath('.'))
from src import comun

comun.salida_utf8()


def sanear(texto):
    """Los guiones prohibidos del libro no se vuelcan al arbol: la lista es la de
    la casa (comun.GUIONES_PROHIBIDOS), no una mia tecleada aqui."""
    for caracter in comun.GUIONES_PROHIBIDOS:
        texto = texto.replace(caracter, '-')
    return texto
F = 'fuentes/marquet_turn_the_ship/cap_03.md'

# LA UNICA CONSTANTE TECLEADA, Y VA DECLARADA ARRIBA: mi clase por linea de cuerpo.
MI_CLASE = {
    9: 'R', 11: 'P', 13: 'R', 15: 'P', 17: 'R', 19: 'P', 21: 'P', 23: 'P',
    25: 'P', 27: 'P', 29: 'R', 31: 'R', 33: 'R', 35: 'R', 37: 'P', 39: 'P',
    41: 'P', 43: 'P', 45: 'P', 47: 'P', 49: 'P', 51: 'P', 53: 'P', 55: 'P',
    57: 'P', 59: 'R', 61: 'R', 63: 'R', 65: 'R', 67: 'R', 69: 'R', 71: 'R',
    73: 'R', 75: 'R', 77: 'R', 79: 'R', 81: 'R',
}

print("AVISO: este instrumento LLEVA UNA CONSTANTE TECLEADA DENTRO, y es MI CLASE")
print("       por pieza (el diccionario MI_CLASE). Los numeros de linea, las palabras")
print("       y la cobertura salen del fichero. REMEDIO 4 de la ACTA 30, clausula 'si")
print("       la tienen, lo dicen en su primera linea'.")
print("")

lineas = io.open(F, encoding='utf-8').read().split('\n')
# EL CUERPO EMPIEZA TRAS EL SEGUNDO '---' DEL PREAMBULO: se busca, no se teclea.
guiones = [n for n, l in enumerate(lineas, 1) if l.strip() == '---']
inicio = guiones[1] + 1 if len(guiones) >= 2 else 1
conCuerpo = [n for n, l in enumerate(lineas, 1) if n >= inicio and l.strip()]

print("fichero                        : %s" % F)
print("primera linea de cuerpo        : L%d (tras el segundo --- del preambulo)" % inicio)
print("lineas con contenido en cuerpo : %d" % len(conCuerpo))
print("")

palabrasP = palabrasR = 0
sinClase = []
print("%-6s %-3s %6s  %s" % ('linea', 'cls', 'palab', 'primeras palabras'))
for n in conCuerpo:
    texto = lineas[n - 1].strip()
    p = len(texto.split())
    c = MI_CLASE.get(n)
    if c is None:
        sinClase.append(n)
        c = '?'
    elif c == 'P':
        palabrasP += p
    else:
        palabrasR += p
    # EL EXTRACTO SE SANEA ANTES DE SALIR: el libro es verbatim y trae guion largo,
    # y volcarlo tal cual pone la guarda de guiones en ROJO. Lo cazo yo con
    # `python forja.py guiones` en esta misma fase, no al cerrar.
    print("L%-5d %-3s %6d  %s" % (n, c, p, sanear(texto[:70])))

cuerpo = ' '.join(lineas[n - 1] for n in conCuerpo)
print("")
print("SUMA DE LAS FILAS            : %d palabras" % (palabrasP + palabrasR))
print("wc -w DEL CUERPO (L%d en adelante, lineas con contenido) : %d"
      % (inicio, len(cuerpo.split())))
print("CIERRA                       : %s"
      % ('SI' if palabrasP + palabrasR == len(cuerpo.split()) else 'NO'))
print("LINEAS DE CUERPO SIN CLASE MIA : %d %s" % (len(sinClase), sinClase))
print("")
print("MI REPARTO")
print("  piezas P (yo escribiria nodo) : %d, %d palabras"
      % (sum(1 for n in conCuerpo if MI_CLASE.get(n) == 'P'), palabrasP))
print("  piezas R (residuo)            : %d, %d palabras"
      % (sum(1 for n in conCuerpo if MI_CLASE.get(n) == 'R'), palabrasR))
