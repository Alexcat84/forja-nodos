# -*- coding: utf-8 -*-
"""Vuelta 64, TAREA 2.c y TAREA 4: mide pares sueltos con aduana.medir, sin correr
ningun informe entero ni tocar nada. La poblacion de donde se sacan las fichas es la
de la aduana (grafo mas bandejas, D.38.5). Cada par se mide en el sentido en que lo
levanto su informe (candidato, vecino), y con --ambos tambien al reves.

Los pares salen de los informes guardados, no se teclean:
  d005 : docs/loop/archivo/interrumpidas/2026-09-23-v63-fase-ciega-2/v63ciega/informe_<id>.txt
  d140 : .v63aud/informe_<id>.txt
y los de d141 se pasan con --par a,b.

Uso: python .v64ext/medir_pares.py [--ambos] [--par a,b ...] [d005] [d140]
"""
import io, os, re, sys
sys.path.insert(0, os.getcwd())
from src import aduana, comun
from src import config as modulo_config

A = 'docs/loop/archivo/interrumpidas/2026-09-23-v63-fase-ciega-2/v63ciega'
D005 = ['archivar_indicadores_resolver_problemas', 'construir_grafico_escalonado_pronosticos',
        'construir_indicador_tendencia_patron', 'elegir_fabricar_pedido_pronostico',
        'elegir_indicador_salida_trabajo_administrativo', 'emparejar_indicadores_efecto_contraefecto']
D140 = ['construir_flujo_produccion_paso_limitante', 'clasificar_trabajo_proceso_montaje_prueba',
        'rehacer_flujo_paso_limitante_capacidad', 'preferir_inspeccion_proceso_prueba_destructiva',
        'dimensionar_inventario_materia_prima_reposicion', 'detectar_arreglar_fallo_etapa_menor_valor',
        'decidir_aceptar_rechazar_material_defectuoso', 'dimensionar_plantilla_administrativa_pronostico',
        'simplificar_trabajo_reducir_numero_pasos']
PAT = re.compile(r'vecino (\S+)\s+\[levantada por: ([^\]]+)\]\n\s+similitud_texto ([\d.]+) \| familia_id ([\d.]+) \| paso_contra_nodo ([\d.]+)')


def pares_de_informe(ruta, cand):
    t = io.open(ruta, encoding='utf-8').read()
    return [(cand, m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)) for m in PAT.finditer(t)]


def main(argv):
    ambos = '--ambos' in argv
    pares = []
    if 'd005' in argv:
        for c in D005:
            pares += [('d005',) + p for p in pares_de_informe('%s/informe_%s.txt' % (A, c), c)]
    if 'd140' in argv:
        for c in D140:
            pares += [('d140',) + p for p in pares_de_informe('.v63aud/informe_%s.txt' % c, c)]
    for k, a in enumerate(argv):
        if a == '--par':
            x, y = argv[k + 1].split(',')
            pares.append(('lectura', x, y, '', '', '', ''))
    umbrales = modulo_config.cargar()
    grafo = comun.leer_jsonl(comun.RUTA_DATASET)
    bandejas = aduana.poblacion_de_bandejas()
    fichas = dict((n['id'], n) for n in list(grafo) + list(bandejas))
    donde = dict([(n['id'], 'grafo') for n in grafo] + [(n['id'], 'bandeja') for n in bandejas])
    print('poblacion: grafo %d + bandejas %d = %d' % (len(grafo), len(bandejas), len(grafo) + len(bandejas)))
    print('%-6s %-48s %-48s %-7s %-34s %-26s %s' % ('deuda', 'candidato', 'vecino', 'vecino', 'informe: texto/familia/paso', 'HOY: texto/familia/paso', 'HOY levanta'))
    for deuda, c, v, lev, t0, f0, p0 in pares:
        sentidos = [(c, v)] + ([(v, c)] if ambos else [])
        for x, y in sentidos:
            m = aduana.medir(fichas[x], fichas[y], umbrales)
            s = m['senales']
            hoy = '%s/%s/%s' % (s['similitud_texto'], s['familia_id'], s['paso_contra_nodo'])
            antes = ('%s/%s/%s' % (t0, f0, p0)) if (x, y) == (c, v) and t0 else '(no en informe)'
            print('%-6s %-48s %-48s %-7s %-34s %-26s %s' % (deuda, x, y, donde[y], antes, hoy,
                                                           ', '.join(m['levantada_por']) or 'NO LEVANTA'))


if __name__ == '__main__':
    main(sys.argv[1:])
