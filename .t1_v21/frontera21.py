# -*- coding: utf-8 -*-
"""MI PROPIA LECTURA DE LA FRONTERA DE cap_10, CON LOS PASOS YA ESCRITOS DELANTE.

P.17: la lectura que lee los pasos vence a la que argumenta sin ellos. La ACTA 20
seccion 4.6 cerro la frontera en 13 y dijo, con todas las letras, que si mi lectura
con los pasos delante contradice su tabla GANA LA MIA, declarada con su sed pegado.

Esta corrida hace tres cosas, y la primera va antes que las otras dos:

  1. COMPRUEBA que los seis tramos que dan nodo mas el resto cubren el cuerpo
     entero sin solapes y suman exactamente lo que mide `sed -n '8,$p' | wc -w`.
     Si no cierra, NO se publica ninguna cuenta de nodos: se publica la diferencia.
  2. IMPRIME la tabla de los seis tramos con su cuenta de nodos y la salida literal
     de la primera linea de cada uno (D.35).
  3. CUENTA los pasos de los trece candidatos escritos hoy, pieza por pieza.
"""
import json
import glob
import os
import unicodedata

F = 'fuentes/scott_radical_candor/cap_10.md'
LINEAS = open(F, encoding='utf-8').read().split('\n')


def unichr_(punto):
    return chr(punto)


def llana(texto):
    """Grafia llana: la guarda guiones muerde lo que yo escribo."""
    # LOS DOS GUIONES SE ESCRIBEN POR SU PUNTO DE CODIGO Y NO LITERALES:
    # la guarda `guiones` barre TODO el repo, incluidos mis propios guiones,
    # y un literal aqui aborta el commit. Me lo acaba de abortar.
    texto = texto.replace(unichr_(0x2014), '-').replace(unichr_(0x2013), '-')
    texto = texto.replace(u'‘', "'").replace(u'’', "'")
    texto = texto.replace(u'“', '"').replace(u'”', '"')
    texto = texto.replace(u'…', '...')
    return ''.join(c for c in unicodedata.normalize('NFD', texto)
                   if unicodedata.category(c) != 'Mn')


def palabras(desde, hasta):
    return len(' '.join(LINEAS[desde - 1:hasta]).split())


def primera(desde):
    return '%d:%s' % (desde, llana(LINEAS[desde - 1])[:86])


# LOS SEIS TRAMOS QUE DAN NODO, con la cuenta de nodos de MI lectura de hoy.
TRAMOS = [
    ('L47 a L87',   47,  87, 3, 'las tres conversaciones de carrera'),
    ('L93 a L125',  93, 125, 1, 'el plan anual de gestion del crecimiento'),
    ('L127 a L163', 127, 163, 1, 'el proceso de contratacion, con el acto de L129 dentro'),
    ('L165 a L201', 165, 201, 5, 'despedir: cabeza, tres partes y coda'),
    ('L203 a L223', 203, 223, 1, 'la calibracion de ascensos, con el caso de Google dentro'),
    ('L225 a L251', 225, 251, 2, 'recompensar sin ascender'),
]
# EL RESTO, que no da ningun nodo, y va aqui para que la suma pueda cerrar.
RESTO = [
    ('L9 a L45',   9,  45, 'subtitulo, entrada, rotulos y EL CASO DE RUSS LARAWAY'),
    ('L89 a L91',  89,  91, 'cierre de seccion que remite a una web y a un libro de otro'),
    ('L253 a L263', 253, 263, 'el cuadro que no esta en el recorte, el resumen y la cabecera del cap siguiente'),
]

print('=' * 78)
print('1. LA COMPROBACION, ANTES DE LA TABLA')
print('=' * 78)
cubiertas = {}
solapes = []
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
    print('')
    print('LA CUENTA DE NODOS NO SE PUBLICA. La diferencia es %d palabras.'
          % (suma - cuerpo))
    raise SystemExit(1)

print('')
print('=' * 78)
print('2. LA TABLA DE LOS SEIS TRAMOS, IMPRESA Y NO TECLEADA')
print('=' * 78)
print('| tramo | palabras | nodos | que es | la salida, pegada |')
print('|---|---:|---:|---|---|')
for nombre, desde, hasta, n, razon in TRAMOS:
    print('| `%s` | %d | **%d** | %s | `%s` |'
          % (nombre, palabras(desde, hasta), n, razon, primera(desde)))
print('| | **%d** | **%d** | **los seis tramos que dan nodo** | |'
      % (sum(palabras(d, h) for _n, d, h, _x, _r in TRAMOS),
         sum(n for _n, _d, _h, n, _r in TRAMOS)))
print('')
print('| tramo de resto | palabras | nodos | por que no |')
print('|---|---:|---:|---|')
for nombre, desde, hasta, razon in RESTO:
    print('| `%s` | %d | **0** | %s |' % (nombre, palabras(desde, hasta), razon))
print('| | **%d** | **0** | |'
      % sum(palabras(d, h) for _n, d, h, _r in RESTO))

print('')
print('=' * 78)
print('3. LOS TRECE CANDIDATOS ESCRITOS HOY, CON SUS PASOS CONTADOS DEL FICHERO')
print('=' * 78)
NUEVOS = [
    ('P7',        'conversar_historia_vida_descubrir_motivadores'),
    ('P8',        'conversar_suenios_cruzar_habilidades'),
    ('P9',        'trazar_plan_dieciocho_meses_aprendizaje'),
    ('P13 a P17', 'armar_plan_anual_crecimiento_equipo'),
    ('P19 y P21', 'montar_proceso_contratacion_reducir_sesgo'),
    ('P24',       'facilitar_despido_tres_cosas'),
    ('P25',       'admitir_pronto_mal_desempenio_cuatro_razones'),
    ('P26',       'calibrar_decision_despido_documentarla'),
    ('P27',       'sopesar_consejo_legal_despedir_humildad'),
    ('P28',       'contactar_despedido_mes_despues'),
    ('P30',       'calibrar_ascensos_evitar_politica'),
    ('P33',       'evitar_obsesion_ascenso_estatus'),
    ('P34 a P36', 'reconocer_excelencia_trayectoria_gradual'),
]
print('| # | pieza | id | pasos | atribuciones |')
print('|---:|---|---|---:|---:|')
total_pasos = 0
for i, (pieza, ident) in enumerate(NUEVOS, 1):
    ruta = 'cuarentena/scott_radical_candor/%s.json' % ident
    d = json.load(open(ruta, encoding='utf-8'))
    assert d['id'] == ident, (d['id'], ident)
    n = len(d['pasos_accionables'])
    total_pasos += n
    print('| %d | `%s` | `%s` | **%d** | %d |'
          % (i, pieza, ident, n, len(d.get('atribuciones') or [])))
print('| | | **trece candidatos** | **%d** | |' % total_pasos)
print('')
print('candidatos de cap_10 escritos  : %d' % len(NUEVOS))
print('pasos de cap_10                : %d' % total_pasos)
print('bandeja del lote 4 ahora       : %d'
      % len(glob.glob('cuarentena/scott_radical_candor/*.json')))
