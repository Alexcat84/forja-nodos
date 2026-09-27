# -*- coding: utf-8 -*-
"""Vuelta 80, TAREA 4: comprueba que la linea 1226 de bitacora/VEREDICTOS.jsonl es la de corregir, que su texto_anadido y su razon
son, byte a byte, las lineas de ANADE y RAZON de .v79ext/frontera_grove.txt, y que el resumen_teorico del nodo de hoy acaba con ese
texto y conserva entero el de su ficha de _insertados. Solo lee."""
import io, json
L = io.open('.v79ext/frontera_grove.txt', encoding='utf-8').read().split('\n')
anade, razon = L[L.index('ANADE:') + 1], L[L.index('RAZON:') + 1]
B = [l for l in io.open('bitacora/VEREDICTOS.jsonl', encoding='utf-8') if l.strip()]
d = json.loads(B[1225])
n = [json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip() and '"eliminar_seguimiento_descendente_responsabilizar_dueno"' in l]
n = [x for x in n if x['id'] == 'eliminar_seguimiento_descendente_responsabilizar_dueno'][0]
f = json.load(io.open('cuarentena/_insertados/marquet_turn_the_ship/eliminar_seguimiento_descendente_responsabilizar_dueno.json', encoding='utf-8'))
print('linea 1226: veredicto %s | candidato %s | campo %s' % (d.get('veredicto'), d.get('candidato'), d.get('campo')))
print('texto_anadido igual a la linea ANADE: %s | razon igual a la linea RAZON: %s' % (d.get('texto_anadido') == anade, d.get('razon') == razon))
print('resumen_teorico de hoy empieza por el de la ficha: %s | acaba con la linea ANADE: %s | caracteres %d = %d + %d + %d' % (
    n['resumen_teorico'].startswith(f['resumen_teorico']), n['resumen_teorico'].endswith(anade), len(n['resumen_teorico']),
    len(f['resumen_teorico']), len(n['resumen_teorico']) - len(f['resumen_teorico']) - len(anade), len(anade)))
print('pasos_accionables iguales a los de la ficha: %s | fuentes %s' % (n['pasos_accionables'] == f['pasos_accionables'], [x['clave'] for x in n['fuentes']]))
