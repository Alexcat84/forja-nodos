"""ACTA 79: la linea de la arista por lectura de la vuelta 80 (la 1188 de la bitacora) contra mi fila SOSTENGO sellada en la 78
(.v78ext/aristas_lectura.txt linea 28, que la ACTA 77 77.4 cruzo) y contra el paso 7 de la madre en el grafo. Solo lee."""
import json
L = [json.loads(l) for l in open('bitacora/VEREDICTOS.jsonl', encoding='utf-8')]
con = [(k + 1, d) for k, d in enumerate(L) if k >= 1172 and 'lectura declarada' in (d.get('levantada_por') or [])]
print('lineas de arista por lectura de la vuelta 80: %d | en la linea: %s' % (len(con), [k for k, _ in con]))
k, a = con[0]
fila = open('.v78ext/aristas_lectura.txt', encoding='utf-8').read().split('\n')[27]
print('linea %d: veredicto %s | paso_citado %s | arista %s' % (k, a['veredicto'], a['paso_citado'], a['arista']))
print('la fila 28 de .v78ext/aristas_lectura.txt empieza por SOSTENGO con los mismos extremos: %s' % fila.startswith(
    'SOSTENGO | observar_reunion_rutinaria_senales_plantilla | seguir_frustrado_preguntar_implantacion_ideas | madre paso 7'))
print('su razon esta tal cual en esa fila: %s' % (a['razon'] in fila))
N = {json.loads(l)['id']: json.loads(l) for l in open('dataset/nodos.jsonl', encoding='utf-8')}
print('texto_citado igual al paso 7 de la madre en el grafo: %s' % (a['texto_citado'] == N['observar_reunion_rutinaria_senales_plantilla']['pasos_accionables'][6]))
