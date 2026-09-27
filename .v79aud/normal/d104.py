# -*- coding: utf-8 -*-
"""ACTA 78, d104 (D79.3): las aristas de los cuatro nodos de la puerta D.29 que la 79 trae, y las lineas de la bitacora de
distinguir_tres_tipos_sistemas_negocio por si tocan a alguno de los otros tres. En el turno normal ya puedo ver relaciones (R6
es de mi fase ciega). Solo lee."""
import io, json, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
M = 'distinguir_tres_tipos_sistemas_negocio'
H = ('cuantificar_impacto_innovacion_6_pasos', 'cambiar_saludo_cliente_dos_ramas', 'probar_traje_azul_seis_semanas')
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    d = json.loads(l)
    if d['id'] in (M,) + H:
        print('  %-40s previos %s | siguientes %s' % (d['id'], d.get('nodos_previos'), d.get('nodos_siguientes')))
c = collections.Counter()
for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8'):
    if M in l:
        d = json.loads(l)
        otro = d['vecino'] if d['candidato'] == M else d['candidato']
        c['con uno de los tres' if otro in H else 'con otro nodo'] += 1
print('lineas de la bitacora con %s: %s | suma: %d' % (M, dict(c), sum(c.values())))
