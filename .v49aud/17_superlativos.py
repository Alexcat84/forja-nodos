# -*- coding: utf-8 -*-
"""BARRIDO DE SUPERLATIVOS sobre docs/loop/APERTURA_CIEGA.md.

Es la comprobacion que el REMEDIO DEL AUDITOR, VUELTA 49, primero (ACTA 47, 47.9.d)
me obliga a correr sobre mi propia pagina ANTES de declarar HEREDADO 1: CUMPLIDO.
El remedio que comprueba es el REMEDIO 1 de la ACTA 46: todo superlativo mio lleva
debajo la LISTA ORDENADA ENTERA que lo sostiene.

QUE MIRA Y QUE NO, dicho para que el recorte no sea callado: mira MI PROSA, o sea
las lineas que no van sangradas con cuatro espacios. Las sangradas son salidas de
instrumento pegadas, que no son frases mias, y van contadas aparte al final.

Los golpes NO son caidas: son sitios que tengo que contestar uno a uno en la propia
pagina. Un golpe sin contestar es el remedio roto."""
import io, re, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PATRONES = [
    (r'\b(el|la|los|las|lo)\s+(que\s+)?(mas|menos)\b', 'superlativo con articulo'),
    (r'\b(el|la|los|las)\b[\w\s,`0-9]{1,30}\b(mas|menos)\b', 'superlativo con nombre en medio'),
    (r'\b(mayor|menor|mejor|peor|maximo|maxima|minimo|minima)\b', 'comparativo de una palabra'),
    (r'\b(unico|unica|unicos|unicas)\b', 'unicidad'),
    (r'\b(el|la)\s+(primer|primera|primero|ultimo|ultima)\b', 'primero o ultimo'),
]
UNIVERSALES = [
    (r'\b(ninguno|ninguna|ningun)\b', 'negativa universal'),
    (r'\b(siempre|nunca|jamas|todos|todas)\b', 'universal afirmativa'),
]

texto = io.open('docs/loop/APERTURA_CIEGA.md', encoding='utf-8').read().split('\n')

def barrer(patrones, rotulo):
    golpes = []
    sangradas = 0
    for n, linea in enumerate(texto, 1):
        if linea.startswith('    '):
            for p, _ in patrones:
                if re.search(p, linea, re.I):
                    sangradas += 1
                    break
            continue
        for p, clase in patrones:
            for m in re.finditer(p, linea, re.I):
                a, b = max(0, m.start() - 28), min(len(linea), m.end() + 28)
                golpes.append((n, clase, m.group(0), linea[a:b].strip()))
    print('%s: %d golpes en mi prosa, %d lineas sangradas (salida de instrumento) descartadas'
          % (rotulo, len(golpes), sangradas))
    for n, clase, cual, ctx in golpes:
        print('   linea %-4d [%-26s] %-14s ...%s...' % (n, clase, cual, ctx))
    print()
    return golpes

barrer(PATRONES, 'SUPERLATIVOS, que es lo que el remedio obliga a contestar')
barrer(UNIVERSALES, 'AFIRMACIONES UNIVERSALES, que no las pide el remedio y las barro igual')
