# Auditor, turno normal de la vuelta 72 (ACTA 71). Las 54 lineas nuevas de la bitacora (1028 a 1081), una a una:
#  (1) las de veredicto contra las lineas vivas de .v71ext/veredictos_listos.txt, letra a letra (vecino|clase|[madre=]|razon);
#  (2) par dirigido a par dirigido contra MI barrido sellado de la 71 (.v71aud/vecinos_<id>.json): mismo vecino, mismas
#      tres seniales, mismo levantada_por y mismo detalle_paso;
#  (3) su clase contra mis clases selladas (.v71aud/mis_clases.tsv) con la unica correccion de la ACTA 70 70.5;
#  (4) las de arista declarada por lectura contra mis SOSTENGO sellados (.v71aud/aristas_lectura.tsv);
#  (5) d170: ninguna linea con fijar_frecuencia_reunion_individual_madurez_tarea.
# Toda linea que reparte en clases trae su suma (R7).
import json
from collections import Counter

B = open('bitacora/VEREDICTOS.jsonl', encoding='utf-8').read().splitlines()
nuevas = [json.loads(x) for x in B[1027:]]
print('lineas de la bitacora: %d | nuevas desde la 1028: %d' % (len(B), len(nuevas)))

# (1) lineas vivas preparadas, por candidato
listas = {}
cand = None
for l in open('.v71ext/veredictos_listos.txt', encoding='utf-8').read().splitlines():
    if l.startswith('## '):
        cand = l[3:].strip()
        listas.setdefault(cand, [])
    elif l.strip() and not l.startswith('#'):
        listas[cand].append(l)

ver = [d for d in nuevas if 'operacion' not in d]
ari = [d for d in nuevas if 'operacion' in d]
c = Counter('veredicto' if 'operacion' not in d else d['operacion'] for d in nuevas)
print('nuevas por tipo: %s | suma: %d' % (dict(c), sum(c.values())))


def como_linea(d):
    partes = [d['vecino'], d['veredicto']]
    if d.get('arista'):
        madre = d['arista'].split(' > ')[0]
        partes.append('madre=' + madre)
    partes.append(d['razon'])
    return '|'.join(partes)


usadas = Counter()
e1 = Counter()
for d in ver:
    l = como_linea(d)
    if l in listas.get(d['candidato'], []):
        e1['igual letra a letra a una linea preparada'] += 1
        usadas[(d['candidato'], l)] += 1
    else:
        e1['SIN linea preparada igual'] += 1
        print('  SIN IGUAL:', d['candidato'], l[:160])
print('(1) veredictos contra .v71ext/veredictos_listos.txt: %s | suma: %d' % (dict(e1), sum(e1.values())))
vivas = sum(len(v) for v in listas.values())
repetidas = sum(1 for v in usadas.values() if v > 1)
print('    lineas vivas preparadas: %d | usadas: %d | usadas dos veces: %d' % (vivas, len(usadas), repetidas))

# (2) contra mi barrido sellado
e2 = Counter()
filas_mias = 0
for cid in set(listas):
    try:
        v = json.load(open('.v71aud/vecinos_%s.json' % cid, encoding='utf-8'))
    except FileNotFoundError:
        continue
    filas_mias += len(v['vecinos'])
mias = {}
import glob
for f in glob.glob('.v71aud/vecinos_*.json'):
    v = json.load(open(f, encoding='utf-8'))
    for x in v['vecinos']:
        mias[(v['id'], x['id'])] = x
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
print('(2) veredictos contra mi barrido sellado: %s | suma: %d' % (dict(e2), sum(e2.values())))
vistos = set((d['candidato'], d['vecino']) for d in ver)
faltan = [k for k in mias if k not in vistos]
print('    filas dirigidas de mi barrido: %d | sin linea en la bitacora: %d %s' % (len(mias), len(faltan), faltan))

# (3) clase contra mis clases selladas con la 70.5
clases = {}
for l in open('.v71aud/mis_clases.tsv', encoding='utf-8').read().splitlines()[1:]:
    a, b, cl, madre = l.split('\t')[:4]
    clases[frozenset((a, b))] = (cl, madre)
corr = {frozenset(('cerrar_brecha_dos_preguntas_estrategia', 'determinar_estado_presente_capacidades_proyectos_merma')),
        frozenset(('cerrar_brecha_dos_preguntas_estrategia', 'examinar_demanda_entorno_dos_marcos_temporales'))}
for k in corr:
    clases[k] = ('SANO', '')
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
print('(3) clase contra mis clases selladas, con la 70.5: %s | suma: %d' % (dict(e3), sum(e3.values())))
print('    pares sin orden en la bitacora: %d | en mis clases: %d' % (len(set(frozenset((d['candidato'], d['vecino'])) for d in ver)), len(clases)))

# (4) aristas por lectura contra mis SOSTENGO
sost = {}
for l in open('.v71aud/aristas_lectura.tsv', encoding='utf-8').read().splitlines()[1:]:
    f = l.split('\t')
    if f[2].startswith('SOSTENGO'):
        sost[(f[0], f[1])] = (f[2], f[3])
e4 = Counter()
for d in ari:
    madre, hijo = d['arista'].split(' > ')
    s = sost.get((madre, hijo))
    if s is None:
        e4['arista que NO es un SOSTENGO mio'] += 1
    else:
        e4['un SOSTENGO mio'] += 1
    print('    %s > %s | paso citado %s | mi fila: %s, madre %s' % (madre, hijo, d['paso_citado'], s[0] if s else '-', s[1] if s else '-'))
print('(4) aristas por lectura: %s | suma: %d | mis SOSTENGO: %d' % (dict(e4), sum(e4.values()), len(sost)))
todas = set(d['arista'] for d in nuevas if d.get('arista'))
print('    aristas distintas en las nuevas: %d' % len(todas))

# (5) d170
n = sum(1 for d in nuevas if 'fijar_frecuencia_reunion_individual_madurez_tarea' in (d['candidato'], d['vecino']))
print('(5) lineas nuevas con fijar_frecuencia_reunion_individual_madurez_tarea: %d' % n)
