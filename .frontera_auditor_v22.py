# -*- coding: utf-8 -*-
"""MI FRONTERA CIEGA DE cap_11, declarada por mi y CONTADA por el instrumento.

Mismo instrumento que .frontera_auditor_v21.py (ACTA 21), nuevo capitulo.
Cierra contra el cuerpo (ACTA 18 7.5 orden 1): residuo nombrado linea a linea,
0 solapes, y la suma de palabras de las filas igual al cuerpo medido aparte.

Los tramos son los ROTULOS QUE EL PROPIO CAPITULO ESCRIBE. La columna UD es
cuantas unidades doctrinales cuenta MI lectura en ese tramo, antes de decidir
si se funden.
"""
import io
F = 'fuentes/scott_radical_candor/cap_11.md'
src = io.open(F, encoding='utf-8').read().split('\n')

# (desde, hasta, extraigo?, unidades que cuenta mi lectura, rotulo leido)
PIEZAS = [
 (  9,  13,'NO',0,'subtitulo y apertura del capitulo: remite a la rueda del Cap. 4'),
 ( 15,  35,'SI',1,'el mandato de decidir quien se comunica con quien + el indice de DIEZ herramientas'),
 ( 37,  61,'SI',1,'1:1 CONVERSATIONS: Mind-set, Frequency, Show up!'),
 ( 63,  65,'SI',1,"Your direct report's agenda, not yours"),
 ( 67,  97,'SI',1,'Some good follow-up questions: CATORCE preguntas literales'),
 ( 99, 113,'SI',1,'Encourage new ideas in the 1:1: SEIS preguntas literales'),
 (115, 127,'SI',1,'Signs you are failing as a boss: CINCO seniales rotuladas'),
 (129, 143,'SI',1,'STAFF MEETINGS: los tres goles y la agenda de tres bloques con sus tiempos'),
 (145, 145,'SI',1,'Learn: el cuadro de mando de indicadores clave'),
 (147, 157,'SI',1,'Listen: el mecanismo de los apuntes de sala de estudio'),
 (159, 163,'SI',1,'Clarify: identificar decisiones y debates, y delegarlos si el equipo pasa de veinte'),
 (165, 173,'SI',1,'THINK TIME'),
 (175, 193,'SI',1,'BIG DEBATE MEETINGS: tres propositos, logistica, normas y producto unico'),
 (195, 203,'SI',1,'BIG DECISION MEETINGS: decisor, decisiones finales y poder de veto'),
 (205, 221,'SI',1,'ALL-HANDS MEETINGS: los dos cortes de tamanio y las dos partes'),
 (223, 233,'SI',1,'EXECUTION TIME (indice: Meeting-Free Zones): tres remedios que no cuajan y el cuarto'),
 (235, 249,'SI',1,'KANBAN BOARDS: tres columnas, notas de color, y medir actividad'),
 (251, 269,'SI',1,'WALK AROUND: una hora a la semana'),
 (271, 299,'SI',1,'BE CONSCIOUS OF CULTURE: la rueda sobre la cultura, hasta Clarify'),
 (301, 305,'SI',1,'Debate and decide explicitly: SEIS asuntos que se delegan a recursos humanos'),
 (307, 333,'SI',1,'Persuade, Execute, Learn, Listen: el resto de la rueda sobre la cultura'),
]

def palabras(a, b):
    return len(' '.join(src[a-1:b]).split())

si = no = ud = 0
tot = 0
print('%-3s %-15s %3s %8s  %s' % ('cl','tramo','ud','palabras','rotulo leido en el capitulo'))
for a, b, c, u, q in PIEZAS:
    p = palabras(a, b); tot += p; ud += u
    if c == 'SI': si += 1
    else: no += 1
    print('%-3s L%-4d a L%-4d %3d %8d  %s' % (c, a, b, u, p, q))
print('')
print('TRAMOS QUE MI LECTURA CIEGA CUENTA EN cap_11 : %d' % len(PIEZAS))
print('  SI (yo extraeria)      : %d' % si)
print('  NO (yo no extraeria)   : %d' % no)
print('UNIDADES DOCTRINALES QUE MI LECTURA CUENTA   : %d' % ud)
print('')
cub = {}
for a, b, c, u, q in PIEZAS:
    for i in range(a, b + 1):
        cub[i] = cub.get(i, 0) + 1
falta = [i for i, l in enumerate(src, 1) if l.strip() and i > 7 and i not in cub]
solape = [i for i in cub if cub[i] > 1]
print('lineas con contenido de L8 en adelante NO cubiertas : %d %s' % (len(falta), falta))
for i in falta:
    print('    L%-4d %3d palabras | %s' % (i, len(src[i-1].split()), src[i-1][:88]))
print('lineas cubiertas por DOS tramos o mas (solapes)     : %d %s' % (len(solape), solape))
cuerpo = len(' '.join(src[7:]).split())
resid = sum(len(src[i-1].split()) for i in falta)
print('')
print('suma de palabras de mis %d filas : %d' % (len(PIEZAS), tot))
print('cuerpo de cap_11 medido aparte  : %d' % cuerpo)
print('residuo NO cubierto             : %d palabras' % resid)
print('CUADRA' if tot == cuerpo else 'NO CUADRA, diferencia %d' % (cuerpo - tot))
