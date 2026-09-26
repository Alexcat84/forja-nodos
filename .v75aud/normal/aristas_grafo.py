# ACTA 74: las aristas del grafo que tocan a alguna de las 7 de la tanda, leidas de nodos_siguientes y nodos_previos de
# TODO el grafo, con sus ids, contra las 3 que mi lectura sellada espera (.v75aud/esperado_75.py, fase ciega). Copia de
# .v72aud/normal/aristas_grafo.py con la tanda y las esperadas cambiadas.
import json
N = {d['id']: d for d in (json.loads(l) for l in open('dataset/nodos.jsonl', encoding='utf-8'))}
tanda = set(l.split()[-1] for l in open('.v73aud/los7.txt', encoding='utf-8') if l.strip())
esperadas = {
    ('desarrollar_primer_curso_entrenamiento', 'pedir_critica_anonima_curso_entrenamiento_dictado'),
    ('priorizar_lista_entrenamiento_subordinados', 'desarrollar_primer_curso_entrenamiento'),
    ('responder_primer_aviso_renuncia_subordinado', 'gestionar_retencion_subordinado_valioso_renuncia'),
}
def ids(v):
    return [x if isinstance(x, str) else x.get('id') for x in (v or [])]
pares = set()
for i, d in N.items():
    for s in ids(d.get('nodos_siguientes')):
        pares.add((i, s))
    for p in ids(d.get('nodos_previos')):
        pares.add((p, i))
toca = {p for p in pares if p[0] in tanda or p[1] in tanda}
for m, h in sorted(toca):
    print('  %s > %s | en siguientes de la madre: %s | en previos del hijo: %s' % (m, h,
          'SI' if h in ids(N[m].get('nodos_siguientes')) else 'NO', 'SI' if m in ids(N[h].get('nodos_previos')) else 'NO'))
dos_lados = sum(1 for m, h in toca if h in ids(N.get(m, {}).get('nodos_siguientes')) and m in ids(N.get(h, {}).get('nodos_previos')))
print('de las 7 en el grafo: %d | aristas del grafo que tocan la tanda: %d | declaradas por los dos lados: %d' % (len(tanda & set(N)), len(toca), dos_lados))
print('esperadas: %d | en el grafo: %d | en el grafo y no esperadas: %d | esperadas y no en el grafo: %d' % (
    len(esperadas), len(toca & esperadas), len(toca - esperadas), len(esperadas - toca)))
