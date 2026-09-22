# -*- coding: utf-8 -*-
"""RECOMPONE LAS TRES FRONTERAS DE LA VUELTA 4 FILA A FILA CONTRA EL FICHERO.

No estima: parsea la tabla que el reporte publica, cuenta las palabras de cada
linea citada con el mismo criterio que `awk NF`, y compara fila a fila. Publica
piezas, cuerpo, suma, filas mal contadas, solapes y lineas sin cubrir.
"""

import io
import re

REPORTE = 'docs/loop/REPORTE.md'
FUENTE = 'fuentes/marquet_turn_the_ship/%s.md'


def tramo_de_la_vuelta():
    lineas = io.open(REPORTE, encoding='utf-8').read().splitlines()
    ini = 0
    for numero, texto in enumerate(lineas):
        if texto.startswith('# VUELTA 4 DEL FRENTE'):
            ini = numero
    return lineas[ini:]


def filas_de(cap, tramo):
    """Las filas de la tabla de frontera de ese capitulo."""
    dentro = False
    actual = ''
    filas = []
    for linea in tramo:
        cabeza = re.match(r'^## 3\.([abc])\. `(cap_\d+)`', linea)
        if cabeza:
            actual = cabeza.group(2)
        if re.match(r'^### 3\.[abc]\.2\.', linea):
            dentro = (actual == cap)
        elif re.match(r'^### 3\.[abc]\.3\.', linea):
            dentro = False
        if dentro and linea.startswith('|'):
            filas.append(linea)
    return filas


def palabras_por_linea(cap):
    fuente = io.open(FUENTE % cap, encoding='utf-8').read().splitlines()
    cuenta = {}
    for numero, texto in enumerate(fuente, 1):
        if numero >= 8 and texto.split():
            cuenta[numero] = len(texto.split())
    return cuenta


def revisar(cap, tramo):
    piezas = []
    declarado = None
    for fila in filas_de(cap, tramo):
        celdas = [c.strip().strip('*').strip() for c in fila.strip('|').split('|')]
        if len(celdas) < 3:
            continue
        if celdas[0].startswith('---') or celdas[0] == 'pieza':
            continue
        if 'cuerpo entero' in celdas[0]:
            declarado = celdas[2]
            continue
        numeros = [int(x) for x in re.findall(r'L(\d+)', celdas[1])]
        try:
            palabras = int(re.sub(r'[^0-9]', '', celdas[2]))
        except ValueError:
            continue
        piezas.append((celdas[0], numeros, palabras))

    cuenta = palabras_por_linea(cap)
    cubiertas = []
    malas = []
    suma = 0
    for nombre, numeros, palabras in piezas:
        real = sum(cuenta.get(x, 0) for x in numeros)
        suma += palabras
        if real != palabras:
            malas.append((nombre, numeros, palabras, real))
        cubiertas.extend(numeros)
    solapes = sorted(x for x in set(cubiertas) if cubiertas.count(x) > 1)
    sin_cubrir = sorted(set(cuenta) - set(cubiertas))
    print('== %s' % cap)
    print('   piezas de su tabla            : %d' % len(piezas))
    print('   cuerpo L8+ medido por mi      : %d   (declarado: %s)'
          % (sum(cuenta.values()), declarado))
    print('   suma de sus filas             : %d' % suma)
    print('   filas con palabras mal        : %s' % (malas if malas else 0))
    print('   lineas solapadas              : %s' % (solapes if solapes else 0))
    print('   lineas con palabras sin cubrir: %s' % (sin_cubrir if sin_cubrir else 0))
    return len(piezas), sum(cuenta.values()), suma


def main():
    tramo = tramo_de_la_vuelta()
    total_piezas = total_cuerpo = total_suma = 0
    for cap in ('cap_09', 'cap_10', 'cap_11'):
        piezas, cuerpo, suma = revisar(cap, tramo)
        total_piezas += piezas
        total_cuerpo += cuerpo
        total_suma += suma
    print('== LAS TRES')
    print('   piezas %d   cuerpo %d   suma %d' % (total_piezas, total_cuerpo, total_suma))


main()
