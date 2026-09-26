# Auditor, turno normal de la vuelta 75 (ACTA 74), copia adaptada de .v72aud/normal/cruce_bitacora.py.
# Las lineas nuevas de la bitacora (1082 en adelante: la ACTA 73 73.1 cerro en 1081), una a una:
#  (0) la de corregir de la TAREA 2, aparte;
#  (1) las de veredicto contra las lineas vivas de .v73ext/veredictos_listos.txt, letra a letra (vecino|clase|[madre=]|razon);
#  (2) par dirigido a par dirigido contra MI barrido sellado de la 73 (.v73aud/vecinos_<id>.json): mismo vecino, mismas
#      tres seniales, mismo levantada_por y mismo detalle_paso;
#  (3) su clase contra mis clases selladas (.v73aud/mis_clases.tsv) con la unica correccion de la ACTA 72 72.5 (D73.9).
# Toda linea que reparte en clases trae su suma (R7).
import json, glob
from collections import Counter

B = open('bitacora/VEREDICTOS.jsonl', encoding='utf-8').read().splitlines()
nuevas = [json.loads(x) for x in B[1081:]]
print('lineas de la bitacora: %d | nuevas desde la 1082: %d' % (len(B), len(nuevas)))
ver = [d for d in nuevas if 'operacion' not in d]
ope = [d for d in nuevas if 'operacion' in d]
c = Counter('veredicto' if 'operacion' not in d else d['operacion'] for d in nuevas)
print('nuevas por tipo: %s | suma: %d' % (dict(c), sum(c.values())))
for d in ope:
    print('(0) linea de operacion: candidato %s | caracteres %d > %d | huellas %s > %s | la razon cita 73.5 y 73.6: %s | texto_anadido %d caracteres' % (
        d['candidato'], d['caracteres_antes'], d['caracteres_despues'], d['huella_vecino'], d['huella_candidato'],
        'SI' if ('73.5' in d['razon'] and '73.6' in d['razon']) else 'NO', len(d.get('texto_anadido', ''))))

listas = {}
cand = None
for l in open('.v73ext/veredictos_listos.txt', encoding='utf-8').read().splitlines():
    if l.startswith('## '):
        cand = l[3:].strip()
        listas.setdefault(cand, [])
    elif l.strip() and not l.startswith('#'):
        listas[cand].append(l)


def como_linea(d):
    partes = [d['vecino'], d['veredicto']]
    if d.get('arista'):
        partes.append('madre=' + d['arista'].split(' > ')[0])
    partes.append(d['razon'])
    return '|'.join(partes)


usadas = Counter(); e1 = Counter()
for d in ver:
    l = como_linea(d)
    if l in listas.get(d['candidato'], []):
        e1['igual letra a letra a una linea preparada'] += 1
        usadas[(d['candidato'], l)] += 1
    else:
        e1['SIN linea preparada igual'] += 1
        print('  SIN IGUAL:', d['candidato'], l[:160])
print('(1) veredictos contra .v73ext/veredictos_listos.txt: %s | suma: %d' % (dict(e1), sum(e1.values())))
vivas = sum(len(v) for v in listas.values())
print('    lineas vivas preparadas: %d | usadas: %d | usadas dos veces: %d' % (vivas, len(usadas), sum(1 for v in usadas.values() if v > 1)))

mias = {}
for f in glob.glob('.v73aud/vecinos_*.json'):
    v = json.load(open(f, encoding='utf-8'))
    for x in v['vecinos']:
        mias[(v['id'], x['id'])] = x
e2 = Counter()
for d in ver:
    m = mias.get((d['candidato'], d['vecino']))
    if m is None:
        e2['par que mi barrido NO levanta'] += 1
        print('  NUEVO:', d['candidato'], d['vecino'])
    elif (m['senales'] == d['senales'] and sorted(m['levantada_por']) == sorted(d['levantada_por'])
          and m['detalle_paso'] == d['detalle_paso']):
        e2['par de mi barrido, seniales, levantada_por y detalle iguales'] += 1
    else:
        e2['par de mi barrido con algo distinto'] += 1
        print('  DISTINTO:', d['candidato'], d['vecino'], m['senales'], d['senales'])
print('(2) veredictos contra mi barrido sellado de la 73: %s | suma: %d' % (dict(e2), sum(e2.values())))
vistos = set((d['candidato'], d['vecino']) for d in ver)
faltan = [k for k in mias if k not in vistos]
print('    filas dirigidas de mi barrido: %d | sin linea en la bitacora: %d %s' % (len(mias), len(faltan), faltan))

clases = {}
for l in open('.v73aud/mis_clases.tsv', encoding='utf-8').read().splitlines()[1:]:
    a, b, cl, madre = l.split('\t')[:4]
    clases[frozenset((a, b))] = (cl, madre)
clases[frozenset(('priorizar_lista_entrenamiento_subordinados', 'pedir_critica_anonima_curso_entrenamiento_dictado'))] = ('SANO', '')
e3 = Counter()
for d in ver:
    k = frozenset((d['candidato'], d['vecino']))
    mia = clases.get(k)
    madre = d['arista'].split(' > ')[0] if d.get('arista') else ''
    if mia is None:
        e3['par fuera de mis clases'] += 1
        print('  FUERA:', sorted(k))
    elif mia == (d['veredicto'], madre):
        e3['igual clase y madre'] += 1
    else:
        e3['DISTINTA'] += 1
        print('  DISTINTA:', sorted(k), mia, d['veredicto'], madre)
print('(3) clase contra mis clases selladas, con la 72.5 (D73.9): %s | suma: %d' % (dict(e3), sum(e3.values())))
print('    pares sin orden en la bitacora: %d | en mis clases: %d' % (len(set(frozenset((d['candidato'], d['vecino'])) for d in ver)), len(clases)))
print('    aristas distintas en las nuevas: %d' % len(set(d['arista'] for d in nuevas if d.get('arista'))))
