# ACTA 71: las aristas del grafo que tocan a alguna de las 20 de la tanda, leidas de nodos_siguientes y nodos_previos de
# TODO el grafo, contra las 6 que mi lectura sellada espera (.v72aud/esperado_72.py, fase ciega). Cada arista se cuenta una vez
# por par dirigido, y se comprueba que sus dos lados la declaran (madre la lleva en siguientes, hijo en previos).
import json
N = {d['id']: d for d in (json.loads(l) for l in open('dataset/nodos.jsonl', encoding='utf-8'))}
tanda = [l.strip() for l in open('.v71aud/los20.txt', encoding='utf-8') if l.strip()]
tanda = set(t.split()[-1] for t in tanda)
esperadas = {
    ('definir_entorno_grupo_clientes_proveedores_competidores', 'examinar_demanda_entorno_dos_marcos_temporales'),
    ('definir_entorno_grupo_clientes_proveedores_competidores', 'examinar_entorno_expectativas_tecnologia_proveedores_grupos'),
    ('planificar_tres_pasos_demanda_estado_brecha', 'examinar_demanda_entorno_dos_marcos_temporales'),
    ('planificar_tres_pasos_demanda_estado_brecha', 'determinar_estado_presente_capacidades_proyectos_merma'),
    ('planificar_tres_pasos_demanda_estado_brecha', 'cerrar_brecha_dos_preguntas_estrategia'),
    ('elegir_modo_control_motivacion_factor_cua', 'escalonar_complejidad_puesto_empleado_nuevo'),
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
dos_lados = sum(1 for m, h in toca if h in ids(N.get(m, {}).get('nodos_siguientes')) and m in ids(N.get(h, {}).get('nodos_previos')))
print('de las 20 en el grafo: %d | aristas del grafo que tocan la tanda: %d | declaradas por los dos lados: %d' % (len(tanda & set(N)), len(toca), dos_lados))
print('esperadas: %d | en el grafo: %d | en el grafo y no esperadas: %d | esperadas y no en el grafo: %d' % (
    len(esperadas), len(toca & esperadas), len(toca - esperadas), len(esperadas - toca)))
for p in sorted(toca - esperadas) + sorted(esperadas - toca):
    print('  ', p)
