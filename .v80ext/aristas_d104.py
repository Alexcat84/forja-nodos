# -*- coding: utf-8 -*-
"""Vuelta 80, TAREA 1: las aristas de hoy de los cuatro nodos de d104 (ACTA 78 78.3), leidas de dataset/nodos.jsonl. Solo lee."""
import io, json
g = dict((d['id'], d) for d in (json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()))
for k in ['distinguir_tres_tipos_sistemas_negocio', 'cuantificar_impacto_innovacion_6_pasos', 'cambiar_saludo_cliente_dos_ramas', 'probar_traje_azul_seis_semanas']:
    print('  %-40s previos %s | siguientes %s' % (k, g[k].get('nodos_previos'), g[k].get('nodos_siguientes')))
