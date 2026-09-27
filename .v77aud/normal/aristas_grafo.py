# -*- coding: utf-8 -*-
"""Turno normal de la ACTA 76. Las aristas del grafo con algun extremo en las 22, CON SUS IDS (R6 ya no manda en esta fase),
leidas de las dos listas de relacion de cada nodo, contra las 10 que mi apertura sellada esperaba (APERTURA_CIEGA.md 4). Y los
437 nodos viejos: el grafo de la apertura de la 77 (git show 70a827c9, que es el de mi ACTA 75) contra el de hoy, linea a linea.
Solo lee."""
import io, sys, json, subprocess
sys.stdout.reconfigure(encoding="utf-8")
las22 = set(io.open('.v76aud/las22.txt', encoding='utf-8').read().split())
ESP = {
 ('aplicar_seis_pasos_sistema_venta', 'medir_sistema_venta_trece_indicadores_benchmark'),
 ('cambiar_saludo_cliente_dos_ramas', 'cuantificar_impacto_innovacion_6_pasos'),
 ('construir_estrategia_gente_cuatro_componentes', 'aplicar_cinco_pasos_proceso_contratacion'),
 ('construir_estrategia_gente_cuatro_componentes', 'documentar_trabajo_manual_operaciones'),
 ('fingir_prototipo_cinco_mil_replicas', 'dar_valor_constante_cuatro_publicos'),
 ('fingir_prototipo_cinco_mil_replicas', 'documentar_trabajo_manual_operaciones'),
 ('fingir_prototipo_cinco_mil_replicas', 'operar_modelo_gente_destreza_minima'),
 ('fingir_prototipo_cinco_mil_replicas', 'recorrer_siete_pasos_programa_desarrollo_negocio'),
 ('fingir_prototipo_cinco_mil_replicas', 'unificar_color_forma_vestuario_modelo'),
 ('recorrer_siete_pasos_programa_desarrollo_negocio', 'construir_estrategia_gente_cuatro_componentes')}
hoy = [l for l in io.open('dataset/nodos.jsonl', encoding='utf-8', newline='')]
G = dict((json.loads(l)['id'], json.loads(l)) for l in hoy)
dm = set((m, h) for m in G for h in G[m].get('nodos_siguientes', []) if m in las22 or h in las22)
dh = set((m, h) for h in G for m in G[h].get('nodos_previos', []) if m in las22 or h in las22)
for a in sorted(dm | dh):
    print('  %-48s > %-54s | en la madre: %s | en el hijo: %s | esperada: %s' % (a[0], a[1], 'SI' if a in dm else 'NO', 'SI' if a in dh else 'NO', 'SI' if a in ESP else 'NO'))
print('aristas con extremo en las 22: %d | por los dos lados: %d | esperadas: %d | esperadas presentes: %d | no esperadas: %d' % (
    len(dm | dh), len(dm & dh), len(ESP), len(ESP & dm & dh), len((dm | dh) - ESP)))
antes = subprocess.run(['git', 'show', '70a827c9:dataset/nodos.jsonl'], capture_output=True).stdout.decode('utf-8').splitlines(True)
A = dict((json.loads(l)['id'], l) for l in antes)
H = dict((json.loads(l)['id'], l) for l in hoy)
viejos = [i for i in A]
cambian = [i for i in viejos if A[i].rstrip('\r\n') != H.get(i, '').rstrip('\r\n')]
nuevos = [i for i in H if i not in A]
print('grafo al abrir la 77: %d | hoy: %d | viejos que faltan hoy: %d | viejos que cambian: %d %s | nuevos: %d | nuevos que son las 22: %s' % (
    len(A), len(H), sum(1 for i in viejos if i not in H), len(cambian), cambian, len(nuevos), 'SI' if set(nuevos) == las22 else 'NO'))
orden = [json.loads(l)['id'] for l in hoy][-22:]
print('las 22 ultimas filas del fichero, en su orden:', ' '.join('%d:%s' % (k + 1, i[:18]) for k, i in enumerate(orden)))
