# -*- coding: utf-8 -*-
"""LA FRONTERA DE cap_12 (`Getting Started`), CERRADA CONTRA EL CUERPO ANTES DE CORTAR.

Si la suma de las filas no da el cuerpo medido aparte, no se publica ninguna
cuenta de nodos (ACTA 18 seccion 7.5 orden 1).
"""
import json
import unicodedata

F = 'fuentes/scott_radical_candor/cap_12.md'
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


def primera(desde, hasta=None):
    for i in range(desde, (hasta or desde) + 1):
        if LINEAS[i - 1].strip() and LINEAS[i - 1].strip() != '* * *':
            return '%d:%s' % (i, llana(LINEAS[i - 1])[:74])
    return '%d:%s' % (desde, llana(LINEAS[desde - 1])[:74])


TRAMOS = [
    ('L13',        13, 13, 1, 'pieza 1, tramo a: el plan se anuncia y su pregunta, el orden de operaciones'),
    ('L15',        15, 15, 0, 'pieza 1, tramo b: el rotulo de la primera etapa, que la cabeza nombra'),
    ('L17',        17, 17, 1, 'pieza 2: contar tus propias historias para explicar la idea'),
    ('L19 a L49',  19, 49, 0, 'pieza 1, tramo c: las etapas del plan, una a una y en su orden'),
]
RESTO = [
    ('L9 a L11',   9,  11, 'el rotulo y la felicitacion de apertura: no hay nada que ejecutar'),
    ('L14',        14, 14, 'linea en blanco entre L13 y L15'),
    ('L16',        16, 16, 'linea en blanco entre L15 y L17'),
    ('L18',        18, 18, 'linea en blanco entre L17 y L19'),
    ('L50',        50, 50, 'linea en blanco entre L49 y L51'),
    ('L51 a L53',  51, 53, 'EL REPARTO DE LA SEMANA DEL JEFE: ya extraido de cap_03 en '
                           'repartir_semana_cuarenta_horas_jefe, leido contra el y declarado REPITE'),
    ('L55',        55, 55, 'remite a la comunidad y a las preguntas de seguimiento: promocion'),
    ('L57 a L65',  57, 65, 'el cierre exhortativo del libro: postura, no procedimiento'),
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

print('tramos que dan nodo                    : %d' % len(TRAMOS))
print('tramos de resto                        : %d' % len(RESTO))
print('lineas con contenido de L8 en adelante : %d' % len(con_contenido))
print('lineas NO cubiertas                    : %d  %s' % (len(sin_cubrir), sin_cubrir))
print('SOLAPES                                : %d  %s' % (len(solapes), solapes))
print('suma de las filas                      : %d palabras' % suma)
print("cuerpo medido aparte (sed 8,$ | wc -w) : %d palabras" % cuerpo)
print('IGUALES                                : %s' % (suma == cuerpo))
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
          % (nombre, palabras(desde, hasta), n, razon, primera(desde, hasta)))
print('| | **%d** | **%d** | **los tramos que dan nodo** | |'
      % (sum(palabras(d, h) for _n, d, h, _x, _r in TRAMOS),
         sum(n for _n, _d, _h, n, _r in TRAMOS)))
print('')
print('| tramo de resto | palabras | nodos | que es, nombrado |')
print('|---|---:|---:|---|')
for nombre, desde, hasta, razon in RESTO:
    print('| `%s` | %d | **0** | %s |' % (nombre, palabras(desde, hasta), razon))
print('| | **%d** | **0** | |' % sum(palabras(d, h) for _n, d, h, _r in RESTO))

print('')
print('=' * 78)
print('3. LOS CANDIDATOS DE cap_12, CON SUS PASOS CONTADOS DEL FICHERO')
print('=' * 78)
IDS = [
    'desplegar_plan_orden_operaciones_franqueza_radical',
    'contar_historias_propias_explicar_franqueza_radical',
]
print('| # | id | pasos |')
print('|---:|---|---:|')
total = 0
for i, ident in enumerate(IDS, 1):
    try:
        d = json.load(open('cuarentena/scott_radical_candor/%s.json' % ident, encoding='utf-8'))
    except IOError:
        print('| %d | `%s` | **SIN ESCRIBIR** |' % (i, ident))
        continue
    assert d['id'] == ident
    total += len(d['pasos_accionables'])
    print('| %d | `%s` | **%d** |' % (i, ident, len(d['pasos_accionables'])))
print('| | **%d candidatos** | **%d** |' % (len(IDS), total))
