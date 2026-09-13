# -*- coding: utf-8 -*-
"""MI LECTURA DE LA FRONTERA DE cap_11 (Cap. 8, Results), PUBLICADA ANTES DE CORTAR.

ACTA 18 seccion 7.5 orden 1: la frontera se cierra contra el cuerpo o no se publica.
ACTA 19 seccion 7.4 ORDEN A: la fila de residuo es CERO o trae sus lineas nombradas
UNA A UNA. Esa orden cazo la pieza 14 de cap_10, y por eso aqui el resto va troceado.
"""
import unicodedata

F = 'fuentes/scott_radical_candor/cap_11.md'
LINEAS = open(F, encoding='utf-8').read().split('\n')


def llana(texto):
    texto = texto.replace(chr(0x2014), '-').replace(chr(0x2013), '-')
    texto = texto.replace(u'‘', "'").replace(u'’', "'")
    texto = texto.replace(u'“', '"').replace(u'”', '"')
    texto = texto.replace(u'…', '...')
    return ''.join(c for c in unicodedata.normalize('NFD', texto)
                   if unicodedata.category(c) != 'Mn')


def palabras(desde, hasta):
    return len(' '.join(LINEAS[desde - 1:hasta]).split())


def primera(desde):
    return '%d:%s' % (desde, llana(LINEAS[desde - 1])[:76])


TRAMOS = [
    ('L15 a L35',   15,  35, 1, 'P1  la cabeza: quien se comunica con quien y las herramientas nombradas'),
    ('L37 a L65',   37,  65, 1, 'P2  el 1:1: mentalidad, frecuencia, presentarse y la agenda del reportado'),
    ('L67 a L97',   67,  97, 1, 'P3  las preguntas de seguimiento que buscan los huecos'),
    ('L99 a L113',  99, 113, 1, 'P4  nutrir en el 1:1 las ideas nuevas, que son fragiles'),
    ('L115 a L127', 115, 127, 1, 'P5  las seniales del 1:1 de que estas fallando como jefe'),
    ('L129 a L145', 129, 145, 1, 'P6a la reunion de equipo y su agenda de tres bloques'),
    ('L147 a L157', 147, 157, 1, 'P7  los apuntes de sala de estudio'),
    ('L159 a L163', 159, 163, 0, 'P6b el bloque de aclarar de esa misma agenda'),
    ('L165 a L173', 165, 173, 1, 'P8  el tiempo para pensar, bloqueado y sagrado'),
    ('L175 a L193', 175, 193, 1, 'P9  la reunion de gran debate'),
    ('L195 a L203', 195, 203, 1, 'P10 la reunion de gran decision'),
    ('L205 a L221', 205, 221, 1, 'P11 la reunion general'),
    ('L223 a L233', 223, 233, 1, 'P12 pelear la proliferacion de reuniones con tiempo de ejecutar'),
    ('L235 a L249', 235, 249, 1, 'P13 el tablero kanban'),
    ('L251 a L269', 251, 269, 1, 'P14 pasear por la organizacion'),
    ('L271 a L299', 271, 299, 1, 'P15a la rueda recorrida sobre tu propia cultura'),
    ('L301 a L305', 301, 305, 1, 'P16 debatir y decidir lo que te tienta delegar a recursos humanos'),
    ('L307 a L333', 307, 333, 0, 'P15b persuadir, ejecutar, aprender y escuchar, de esa misma rueda'),
]
RESTO = [
    ('L9 a L13', 9, 13, 'subtitulo, la meta de la franqueza radical, las protesis mentales de Kosslyn, '
                        'la rueda de hacer cosas (ya extraida de cap_07 en recorrer_rueda_hacer_cosas_equipo) '
                        'y el formador de New Jersey Transit'),
]

print('=' * 78)
print('1. LA COMPROBACION, ANTES DE LA TABLA')
print('=' * 78)
cubiertas, solapes = {}, []
for nombre, desde, hasta, _n, _r in TRAMOS:
    for i in range(desde, hasta + 1):
        if i in cubiertas:
            solapes.append((i, cubiertas[i], nombre))
        cubiertas[i] = nombre
for nombre, desde, hasta, _r in RESTO:
    for i in range(desde, hasta + 1):
        if i in cubiertas:
            solapes.append((i, cubiertas[i], nombre))
        cubiertas[i] = nombre

con_contenido = [i for i in range(8, len(LINEAS) + 1)
                 if i - 1 < len(LINEAS) and LINEAS[i - 1].strip()]
sin_cubrir = [i for i in con_contenido if i not in cubiertas]
suma = sum(palabras(d, h) for _n, d, h, _x, _r in TRAMOS)
suma += sum(palabras(d, h) for _n, d, h, _r in RESTO)
cuerpo = len(' '.join(LINEAS[7:]).split())

print('tramos que dan nodo (contando los dos partidos): %d' % len(TRAMOS))
print('tramos de resto                        : %d' % len(RESTO))
print('lineas con contenido de L8 en adelante : %d' % len(con_contenido))
print('lineas NO cubiertas                    : %d  %s' % (len(sin_cubrir), sin_cubrir))
print('SOLAPES                                : %d  %s' % (len(solapes), solapes))
print('suma de las filas                      : %d palabras' % suma)
print("cuerpo medido aparte (sed 8,$ | wc -w) : %d palabras" % cuerpo)
print('IGUALES                                : %s' % (suma == cuerpo))
print('')
print('NODOS QUE LA FRONTERA DA               : %d' % sum(n for _a, _b, _c, n, _d in TRAMOS))
print('TECHO DE 12.4                          : 15')
print('palabras de resto                      : %d  (%.1f por ciento del cuerpo)'
      % (sum(palabras(d, h) for _n, d, h, _r in RESTO),
         100.0 * sum(palabras(d, h) for _n, d, h, _r in RESTO) / cuerpo))
if suma != cuerpo or sin_cubrir or solapes:
    print('\nLA CUENTA DE NODOS NO SE PUBLICA. Diferencia: %d palabras.' % (suma - cuerpo))
    raise SystemExit(1)

print('')
print('=' * 78)
print('2. LA TABLA, IMPRESA Y NO TECLEADA')
print('=' * 78)
print('| tramo | palabras | nodos | que es | la salida, pegada |')
print('|---|---:|---:|---|---|')
for nombre, desde, hasta, n, razon in TRAMOS:
    print('| `%s` | %d | **%d** | %s | `%s` |'
          % (nombre, palabras(desde, hasta), n, razon, primera(desde)))
print('| | **%d** | **%d** | **los tramos que dan nodo** | |'
      % (sum(palabras(d, h) for _n, d, h, _x, _r in TRAMOS),
         sum(n for _n, _d, _h, n, _r in TRAMOS)))
print('')
print('| tramo de resto | palabras | nodos | que es, nombrado linea a linea |')
print('|---|---:|---:|---|')
for nombre, desde, hasta, razon in RESTO:
    print('| `%s` | %d | **0** | %s |' % (nombre, palabras(desde, hasta), razon))
print('| | **%d** | **0** | |' % sum(palabras(d, h) for _n, d, h, _r in RESTO))
