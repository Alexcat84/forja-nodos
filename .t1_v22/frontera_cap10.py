# -*- coding: utf-8 -*-
"""LA FRONTERA DE cap_10 RECOMPUTADA CON LA PIEZA 14 DENTRO (ACTA 21 seccion 4.1).

No copio la tabla de la vuelta 21: la vuelvo a cerrar contra el cuerpo, porque la
pieza 14 saca TRES lineas del resto y las mete en un tramo de nodo. Si la suma no
cierra, no se publica ninguna cuenta de nodos (ACTA 18 seccion 7.5 orden 1).
"""
import json
import unicodedata

F = 'fuentes/scott_radical_candor/cap_10.md'
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
    return '%d:%s' % (desde, llana(LINEAS[desde - 1])[:78])


# TRAMOS QUE DAN NODO. La pieza 14 es NO CONTIGUA y va en tres filas de linea.
TRAMOS = [
    ('L19',         19,  19, 0, 'pieza 14, tramo a: con quien y para que'),
    ('L21',         21,  21, 0, 'pieza 14, tramo b: cuando y donde caben'),
    ('L43',         43,  43, 1, 'pieza 14, tramo c: la cadencia y el encargo a los jefes'),
    ('L47 a L87',   47,  87, 3, 'las tres conversaciones de carrera'),
    ('L93 a L125',  93, 125, 1, 'el plan anual de gestion del crecimiento'),
    ('L127 a L163', 127, 163, 1, 'el proceso de contratacion, con el acto de L129 dentro'),
    ('L165 a L201', 165, 201, 5, 'despedir: cabeza, tres partes y coda'),
    ('L203 a L223', 203, 223, 1, 'la calibracion de ascensos, con el caso de Google dentro'),
    ('L225 a L251', 225, 251, 2, 'recompensar sin ascender'),
]
# EL RESTO, NOMBRADO LINEA A LINEA (ACTA 19 seccion 7.4 ORDEN A).
RESTO = [
    ('L9 a L18',    9,  18, 'subtitulo, resumen del cap. 3 y los dos rotulos de seccion'),
    ('L20',        20,  20, 'linea en blanco entre L19 y L21'),
    ('L22 a L42',  22,  42, 'EL CASO DE RUSS LARAWAY entero: Google, Todd, Sarah y el plan de Sarah'),
    ('L44 a L45',  44,  45, 'linea en blanco y el cierre del caso: la encuesta interna de Google'),
    ('L88 a L92',  88,  92, 'cierre de seccion que remite a una web y a un libro de otro'),
    ('L253 a L263', 253, 263, 'el cuadro que no esta en el recorte, el resumen y la cabecera del cap siguiente'),
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
print('la pieza 14, sus tres lineas           : %d palabras' % (palabras(19, 19) + palabras(21, 21) + palabras(43, 43)))
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
print('| tramo de resto | palabras | nodos | que es, nombrado |')
print('|---|---:|---:|---|')
for nombre, desde, hasta, razon in RESTO:
    print('| `%s` | %d | **0** | %s |' % (nombre, palabras(desde, hasta), razon))
print('| | **%d** | **0** | |' % sum(palabras(d, h) for _n, d, h, _r in RESTO))

print('')
print('=' * 78)
print('3. LOS CATORCE CANDIDATOS DE cap_10, CON SUS PASOS CONTADOS DEL FICHERO')
print('=' * 78)
IDS = [
    'desplegar_tres_conversaciones_carrera',
    'conversar_historia_vida_descubrir_motivadores',
    'conversar_suenios_cruzar_habilidades',
    'trazar_plan_dieciocho_meses_aprendizaje',
    'armar_plan_anual_crecimiento_equipo',
    'montar_proceso_contratacion_reducir_sesgo',
    'facilitar_despido_tres_cosas',
    'admitir_pronto_mal_desempenio_cuatro_razones',
    'calibrar_decision_despido_documentarla',
    'sopesar_consejo_legal_despedir_humildad',
    'contactar_despedido_mes_despues',
    'calibrar_ascensos_evitar_politica',
    'evitar_obsesion_ascenso_estatus',
    'reconocer_excelencia_trayectoria_gradual',
]
print('| # | id | pasos |')
print('|---:|---|---:|')
total = 0
for i, ident in enumerate(IDS, 1):
    d = json.load(open('cuarentena/scott_radical_candor/%s.json' % ident, encoding='utf-8'))
    assert d['id'] == ident
    total += len(d['pasos_accionables'])
    print('| %d | `%s` | **%d** |' % (i, ident, len(d['pasos_accionables'])))
print('| | **catorce candidatos** | **%d** |' % total)
