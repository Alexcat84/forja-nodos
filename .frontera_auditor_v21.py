# -*- coding: utf-8 -*-
"""MI FRONTERA CIEGA DE cap_10, declarada por mi y CONTADA por el instrumento.

Cierra contra el cuerpo (ACTA 18 7.5 orden 1): 0 lineas sin cubrir,
0 solapes, y la suma de palabras de las filas igual al cuerpo medido aparte.
"""
import io
F = 'fuentes/scott_radical_candor/cap_10.md'
src = io.open(F, encoding='utf-8').read().split('\n')

PIEZAS = [
 ( 9, 13,'NO','subtitulo del capitulo y apertura, remite al Cap. 3'),
 ( 15, 21,'NO','CAREER CONVERSATIONS: rotulo, subtitulo y encuadre'),
 ( 23, 45,'NO','el caso de Russ Laraway: Todd, Sarah, el off site y la encuesta'),
 ( 47, 59,'SI','Conversation one: life story'),
 ( 61, 75,'SI','The second conversation: dreams'),
 ( 77, 87,'SI','Conversation three: eighteen-month plan'),
 ( 89, 91,'NO','cierre de seccion tras el asterisco'),
 ( 93,125,'SI','GROWTH MANAGEMENT: el plan anual y sus CUATRO pasos rotulados'),
 (127,135,'NO','HIRING: rotulo, mentalidad rock star/superstar y encuadre'),
 (137,163,'SI','el proceso de contratacion: CINCO piezas rotuladas'),
 (165,171,'NO','FIRING: rotulo, subtitulo y encuadre de las dos empresas'),
 (173,201,'SI','despedir: las TRES cosas que el texto anuncia, mas Follow up de coda'),
 (203,213,'NO','PROMOTIONS: rotulo, subtitulo y el caso de los comites de Google'),
 (215,223,'SI','la reunion de calibracion de ascensos: CUATRO consejos rotulados'),
 (225,251,'SI','REWARD YOUR ROCK STARS: CUATRO vias de recompensa sin ascenso'),
 (253,255,'NO','AVOID ABSENTEE MANAGEMENT: remite a una tabla, sin procedimiento propio'),
 (257,259,'NO','SUMMARY'),
 (261,263,'NO','marcador del capitulo siguiente (8. RESULTS)'),
]

def palabras(a, b):
    return len(' '.join(src[a-1:b]).split())

si = no = 0
tot = 0
print('%-3s %-13s %7s  %s' % ('cl', 'tramo', 'palabras', 'rotulo leido en la linea de cabecera'))
for a, b, c, q in PIEZAS:
    p = palabras(a, b)
    tot += p
    if c == 'SI': si += 1
    else: no += 1
    print('%-3s L%-4d a L%-4d %7d  %s' % (c, a, b, p, q))
print('')
print('PIEZAS QUE MI LECTURA CIEGA CUENTA EN cap_10: %d' % len(PIEZAS))
print('  SI (yo escribiria nodo): %d' % si)
print('  NO (yo no extraeria)   : %d' % no)
print('')
cub = {}
for a, b, c, q in PIEZAS:
    for i in range(a, b + 1):
        cub[i] = cub.get(i, 0) + 1
falta = [i for i, l in enumerate(src, 1) if l.strip() and i > 7 and i not in cub]
solape = [i for i in cub if cub[i] > 1]
print('lineas con contenido de L8 en adelante NO cubiertas : %d %s' % (len(falta), falta))
print('lineas cubiertas por DOS piezas o mas (solapes)     : %d %s' % (len(solape), solape))
cuerpo = len(' '.join(src[7:]).split())
print('')
print('suma de palabras de mis 18 filas : %d' % tot)
print('cuerpo de cap_10 medido aparte   : %d' % cuerpo)
print('CUADRA' if tot == cuerpo else 'NO CUADRA, diferencia %d' % (cuerpo - tot))
