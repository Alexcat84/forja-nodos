# -*- coding: utf-8 -*-
"""LA FRONTERA DE cap_13 (Afterword to the Revised Edition), CERRADA CONTRA EL
CUERPO ANTES DE CORTAR.

Si la suma de las filas no da el cuerpo medido aparte, no se publica ninguna
cuenta de nodos (ACTA 18 seccion 7.5 orden 1).
"""
import json
import unicodedata

F = 'fuentes/scott_radical_candor/cap_13.md'
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
            return '%d:%s' % (i, llana(LINEAS[i - 1])[:70])
    return '%d:%s' % (desde, llana(LINEAS[desde - 1])[:70])


TRAMOS = [
    ('L17 a L22',   17,  22, 1, 'pieza 1, tramo a: el rotulo YOU, el de las dos practicas y el aviso del cap. 5'),
    ('L35 a L40',   35,  40, 0, 'pieza 1, tramo b: las dos consciencias definidas y las dos practicas con su cuenta'),
    ('L41 a L58',   41,  58, 1, 'pieza 2: la practica de las cuatro historias propias'),
    ('L59 a L72',   59,  72, 1, 'pieza 3: la practica del triangulo de la critica'),
    ('L73 a L86',   73,  86, 1, 'pieza 4, tramo a: el orden de operaciones numerado de cinco pasos'),
    ('L105 a L110', 105, 110, 0, 'pieza 4, tramo b: por que pedir critica va primero, con la seguridad psicologica'),
    ('L111 a L112', 111, 112, 1, 'pieza 10, tramo a: el habito regular, porque verlo una vez no basta'),
    ('L113 a L114', 113, 114, 0, 'pieza 4, tramo c: el anuncio de los cuatro elementos de pedir critica'),
    ('L115 a L120', 115, 120, 1, 'pieza 5, tramo a: la pregunta recurrente y por que no vale la de si o no'),
    ('L129 a L166', 129, 166, 0, 'pieza 5, tramo b: los cuatro atributos, las nueve preguntas de ejemplo y su practica'),
    ('L167 a L186', 167, 186, 1, 'pieza 6: las cuatro dudas frecuentes de pedir critica, con su respuesta'),
    ('L187 a L198', 187, 198, 1, 'pieza 7: abrazar la incomodidad, con la practica de contar hasta seis'),
    ('L199 a L214', 199, 214, 1, 'pieza 8: escuchar para entender, con la practica de escuchar tres minutos'),
    ('L215 a L234', 215, 234, 1, 'pieza 9: hacer tangible la escucha y premiar la franqueza, con sus dos practicas'),
    ('L235 a L246', 235, 246, 0, 'pieza 10, tramo b: meterlo en la rutina que ya tienes, con su practica'),
    ('L247 a L252', 247, 252, 1, 'pieza 11, tramo a: el elogio es el acelerador y la critica el freno'),
    ('L267 a L288', 267, 288, 0, 'pieza 11, tramo b: la disciplina del elogio, su concrecion y su practica'),
    ('L289 a L318', 289, 318, 1, 'pieza 12, tramo a: medir la critica en el oido del otro, con el marco de brujula'),
    ('L319 a L322', 319, 322, 0, 'pieza 12, tramo b: no ir a las consecuencias antes de tiempo, y los varios ejemplares'),
]
RESTO = [
    ('L9 a L16',    9,   16, 'los dos rotulos, los tres autores y por que existe este epilogo'),
    ('L23 a L34',   23,  34, 'EL CASO DEL CAPITALISTA DE RIESGO Y SU ASOCIADO entero: manual 3.5, la '
                             'doctrina que deja (la humildad y las dos consciencias) vive en L35 y L37'),
    ('L87 a L104',  87, 104, 'LA HISTORIA DE KIM Y SU HIJA entera, con el aviso de por que la escribe: '
                             'manual 3.5, es el ejemplar de pedir critica y no doctrina nueva'),
    ('L121 a L128', 121, 128, 'LA HISTORIA DE JASON Y ANN entera: manual 3.5, su doctrina es la '
                              'pregunta recurrente, que ya viaja en la pieza 5'),
    ('L253 a L266', 253, 266, 'LA HISTORIA DE JASON Y DAVE entera: manual 3.5, es el ejemplar de dar '
                              'elogio despues de meter la pata'),
    ('L323 a L332', 323, 332, 'DIVERSIDAD E INCLUSION: la cita de Claudia Rankine, el caso de las '
                              'cenas de ensayo de una participante y el taller que los autores '
                              'montaron con Second City. NO hay procedimiento para el lector: el '
                              'libro cuenta lo que ELLOS hicieron. Va marcado como discutible'),
    ('L333 a L347', 333, 347, 'QUE VIENE AHORA: la hoja de ruta de sus programas, la cita de Mill, la '
                              'peticion de critica, el contacto y la cabecera del capitulo siguiente'),
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
print('3. LOS CANDIDATOS DE cap_13, CON SUS PASOS CONTADOS DEL FICHERO')
print('=' * 78)
IDS = [
    'mejorar_consciencia_propia_relacional_dos_practicas',
    'contar_cuatro_historias_propias_ver_hueco_intencion',
    'practicar_triangulo_critica_tres_papeles',
    'pedir_critica_primero_crear_seguridad_psicologica',
    'elegir_pregunta_recurrente_pedir_critica',
    'resolver_dudas_frecuentes_pedir_critica',
    'abrazar_incomodidad_silencio_contar_seis',
    'escuchar_entender_critica_dominar_defensa',
    'premiar_franqueza_hacer_escucha_tangible',
    'integrar_peticion_critica_rutina_existente',
    'dar_elogio_disciplina_igual_critica',
    'medir_critica_respuesta_oyente_brujula',
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
