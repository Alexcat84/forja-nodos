# -*- coding: utf-8 -*-
"""IMPRIME EL PASO CITADO DE CADA MADRE, DE SU FICHERO, Y DICE DONDE VIVE CADA EXTREMO.

La condicion de una arista declarable no es la linea del libro: es el PASO de la
madre, porque `forja.py arista` rechaza por construccion un paso que la madre no
tiene. Asi que esto abre el fichero de cada madre, cuenta sus pasos e imprime el
citado entero, y ademas dice si cada extremo vive en el grafo o en la bandeja.
"""
import glob, io, json, os, sys

def cargar():
    donde, datos = {}, {}
    for linea in io.open('dataset/nodos.jsonl', encoding='utf-8'):
        linea = linea.strip()
        if not linea:
            continue
        d = json.loads(linea)
        donde[d['id']] = 'GRAFO'
        datos[d['id']] = d
    for ruta in glob.glob('cuarentena/*/*.json') + glob.glob('cuarentena/_insertados/*/*.json'):
        if os.sep + '_insertados' + os.sep in ruta:
            continue
        d = json.load(io.open(ruta, encoding='utf-8'))
        i = d.get('id') or os.path.basename(ruta)[:-5]
        if i not in donde:
            donde[i] = 'bandeja'
            datos[i] = d
    return donde, datos

DONDE, DATOS = cargar()

OCHO = [
    ('fijar_cuatro_notas_calcular_nota_global', 8, 'elegir_categorias_nota_palabras_propias_empresa', 'L109'),
    ('repartir_notas_publicar_reparto_esperado', 3, 'calibrar_notas_reunion_jefes_pares', 'L145 y L151'),
    ('presionar_curva_notas_evitar_forzarla', 11, 'calibrar_notas_reunion_jefes_pares', 'L169'),
    ('evaluar_desempenio_dos_veces_anio', 6, 'montar_evaluacion_360_grados_ligera_pares', 'L191'),
    ('hacer_critica_pares_transparente_ensenar_escribirla', 1, 'montar_evaluacion_360_grados_ligera_pares', 'L207'),
    ('mantener_proceso_evaluacion_ligero_vigilar_crecimiento', 6, 'montar_evaluacion_360_grados_ligera_pares', 'L231'),
    ('mantener_proceso_evaluacion_ligero_vigilar_crecimiento', 5, 'hacer_critica_pares_transparente_ensenar_escribirla', 'L231'),
    ('montar_evaluacion_360_grados_ligera_pares', 6, 'elegir_categorias_nota_palabras_propias_empresa', 'L201'),
]

print('=' * 78)
print('LAS OCHO ARISTAS ADJUDICADAS, CONTRA EL FICHERO DE SU MADRE')
print('=' * 78)
for madre, paso, hijo, linea in OCHO:
    dm, dh = DONDE.get(madre, 'NO EXISTE'), DONDE.get(hijo, 'NO EXISTE')
    pasos = DATOS.get(madre, {}).get('pasos_accionables', [])
    tiene = 'SI' if 1 <= paso <= len(pasos) else 'NO'
    print('')
    print('madre : %s   [%s, %d pasos]' % (madre, dm, len(pasos)))
    print('hijo  : %s   [%s]' % (hijo, dh))
    print('paso  : %d de %d  ->  EXISTE: %s     libro: %s' % (paso, len(pasos), tiene, linea))
    if tiene == 'SI':
        print('  P%d: %s' % (paso, pasos[paso - 1]))
    print('  CABLEABLE HOY: %s' % ('SI' if dm == 'GRAFO' and dh == 'GRAFO' else
                                   'NO, madre %s e hijo %s' % (dm, dh)))
print('')
print('=' * 78)
print('RESUMEN')
print('=' * 78)
ok = len([1 for m, p, h, _l in OCHO
          if 1 <= p <= len(DATOS.get(m, {}).get('pasos_accionables', []))])
viv = len([1 for m, p, h, _l in OCHO if DONDE.get(m) == 'GRAFO' and DONDE.get(h) == 'GRAFO'])
print('aristas con el paso de la madre EXISTENTE : %d de %d' % (ok, len(OCHO)))
print('aristas con LOS DOS extremos en el grafo  : %d de %d' % (viv, len(OCHO)))
