# -*- coding: utf-8 -*-
"""LA DEUDA DE ARISTAS DE LA VUELTA 37, RECOMPUTADA Y NO HEREDADA.

MISMO INSTRUMENTO que la vuelta 25 y la 26, corrido otra vez: la vuelta mete
CATORCE nodos y eso da los dos extremos a filas que antes solo tenian uno.

Mismo instrumento que la vuelta 25 (.v25/deuda_v25.py), corrido otra vez al cerrar
porque la vuelta metio DOCE nodos y eso puede haber dado los dos extremos a filas
que antes solo tenian uno. Una cifra de deuda envejece dentro de su propia vuelta.

Las 36 filas numeradas de la 36 a la 71 se leen del REPORTE.md, que es su sede, y
las 8 de la vuelta 25 (72 a 79) van escritas aqui con su paso, que es como el acta
las adjudico. Las 35 primeras se CITAN y no se remiden: viven en formatos viejos
sin numeracion corrida, igual que hizo el auditor en ACTA 24 1.5.
"""
import io, json, re, sys

OCHO_V25 = [
    (72, 'fijar_cuatro_notas_calcular_nota_global', 8, 'elegir_categorias_nota_palabras_propias_empresa'),
    (73, 'repartir_notas_publicar_reparto_esperado', 3, 'calibrar_notas_reunion_jefes_pares'),
    (74, 'presionar_curva_notas_evitar_forzarla', 11, 'calibrar_notas_reunion_jefes_pares'),
    (75, 'evaluar_desempenio_dos_veces_anio', 6, 'montar_evaluacion_360_grados_ligera_pares'),
    (76, 'hacer_critica_pares_transparente_ensenar_escribirla', 1, 'montar_evaluacion_360_grados_ligera_pares'),
    (77, 'mantener_proceso_evaluacion_ligero_vigilar_crecimiento', 6, 'montar_evaluacion_360_grados_ligera_pares'),
    (78, 'mantener_proceso_evaluacion_ligero_vigilar_crecimiento', 5, 'hacer_critica_pares_transparente_ensenar_escribirla'),
    (79, 'montar_evaluacion_360_grados_ligera_pares', 6, 'elegir_categorias_nota_palabras_propias_empresa'),
    (80, 'empezar_cultura_franqueza_radical', 3, 'pedir_critica_equipo_premiarla'),
]

grafo, aristas = {}, 0
fuera = []
for linea in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    linea = linea.strip()
    if not linea:
        continue
    d = json.loads(linea)
    grafo[d['id']] = d
    aristas += len(d.get('nodos_siguientes') or [])

# LAS 36 FILAS DE LA DEUDA CORRIDA, LEIDAS DE SU SEDE
FILA = re.compile(r'^\|\s*(\d{2})\s*\|\s*`([a-z0-9_]+)`\s*\|\s*`([a-z0-9_]+)`\s*\|')
vistas = {}
for l in io.open('docs/loop/REPORTE.md', encoding='utf-8'):
    m = FILA.match(l.strip())
    if m and 36 <= int(m.group(1)) <= 71:
        vistas.setdefault(int(m.group(1)), (m.group(2), m.group(3)))

filas = [(n, ma, None, hi) for n, (ma, hi) in sorted(vistas.items())] + OCHO_V25
print('nodos en el grafo                       : %d' % len(grafo))
print('aristas YA vivas en el grafo            : %d' % aristas)
print('filas de deuda contables leidas         : %d   (36 a 71 de su sede, mas las de la v25)'
      % len(filas))
listas, faltan = [], 0
for n, madre, paso, hijo in filas:
    vm, vh = madre in grafo, hijo in grafo
    if vm and vh:
        pasos = len(grafo[madre]['pasos_accionables'])
        ya = hijo in (grafo[madre].get('nodos_siguientes') or [])
        listas.append((n, madre, paso, hijo, pasos, ya))
    else:
        faltan += 1
        fuera.append((n, madre, hijo, 'madre' if not vm else 'hijo'))
print('')
print('con LOS DOS extremos DENTRO del grafo   : %d' % len(listas))
print('con algun extremo fuera                 : %d' % faltan)
if listas:
    print('')
    for n, madre, paso, hijo, pasos, ya in listas:
        print('  %2d  %-54s --%s--> %-54s  madre tiene %d pasos   %s'
              % (n, madre, ('paso %s' % paso) if paso else 'paso ?', hijo, pasos,
                 'YA CABLEADA' if ya else 'POR CABLEAR'))

print('')
print('LAS FILAS QUE SIGUEN CON UN EXTREMO FUERA, con su nombre:')
for n, madre, hijo, cual in fuera:
    print('  %2d  %-54s --> %-54s  falta el %s' % (n, madre, hijo, cual))
