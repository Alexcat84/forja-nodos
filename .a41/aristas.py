# -*- coding: utf-8 -*-
"""Las OCHO aristas que la ACTA 24 seccion 3.1 adjudico DECLARABLES entre los
elementos de cap_14, comprobadas una a una contra dataset/nodos.jsonl de hoy."""
import json, io
N = {}
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    if l.strip():
        d = json.loads(l); N[d['id']] = d
OCHO = [
 ('a','fijar_cuatro_notas_calcular_nota_global',8,'elegir_categorias_nota_palabras_propias_empresa'),
 ('b','repartir_notas_publicar_reparto_esperado',3,'calibrar_notas_reunion_jefes_pares'),
 ('c','presionar_curva_notas_evitar_forzarla',11,'calibrar_notas_reunion_jefes_pares'),
 ('d','evaluar_desempenio_dos_veces_anio',6,'montar_evaluacion_360_grados_ligera_pares'),
 ('e','hacer_critica_pares_transparente_ensenar_escribirla',1,'montar_evaluacion_360_grados_ligera_pares'),
 ('f','mantener_proceso_evaluacion_ligero_vigilar_crecimiento',6,'montar_evaluacion_360_grados_ligera_pares'),
 ('g','mantener_proceso_evaluacion_ligero_vigilar_crecimiento',5,'hacer_critica_pares_transparente_ensenar_escribirla'),
 ('h','montar_evaluacion_360_grados_ligera_pares',6,'elegir_categorias_nota_palabras_propias_empresa'),
]
def extremos(n, campo):
    out = []
    for e in (n.get(campo) or []):
        out.append(e.get('id') if isinstance(e, dict) else e)
    return out
print('%-3s %-54s %-5s %-50s %s' % ('#','madre','paso','hijo','en el grafo'))
dentro = 0
for k, m, p, h in OCHO:
    nm, nh = N.get(m), N.get(h)
    if nm is None or nh is None:
        print('%-3s %-54s %-5s %-50s FALTA EL NODO' % (k, m, p, h)); continue
    ok = (h in extremos(nm, 'nodos_siguientes')) or (m in extremos(nh, 'nodos_previos'))
    dentro += 1 if ok else 0
    print('%-3s %-54s %-5s %-50s %s' % (k, m, p, h, 'SI' if ok else 'NO'))
print()
print('DE LAS OCHO DE LA ACTA 24 SECCION 3.1: %d CABLEADAS, %d NO' % (dentro, 8 - dentro))
