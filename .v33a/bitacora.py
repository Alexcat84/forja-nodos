# PRIMERA LINEA (HEREDADO 4): CERO IDS TECLEADOS. La tanda sale de .v33a/tanda_ids.txt
# (del git diff del dataset) y las lineas nuevas del git diff de bitacora/VEREDICTOS.jsonl.
# ESTE INSTRUMENTO NO IMPRIME NI UNA RAZON: solo cuenta clases y campos.
import json, io, subprocess, collections
ANTES = 'ef3e7f9'
def carga(ref):
    t = subprocess.check_output(['git','show','%s:bitacora/VEREDICTOS.jsonl'%ref]).decode('utf-8')
    return [json.loads(l) for l in t.splitlines() if l.strip()]
a = carga(ANTES); b = carga('HEAD')
print("bitacora/VEREDICTOS.jsonl   antes de la vuelta 33: %d lineas   ahora: %d   ENTRAN: %d"
      % (len(a), len(b), len(b)-len(a)))
nuevas = b[len(a):]
print()
print("CAMPOS QUE TRAEN LAS LINEAS NUEVAS (sin imprimir ni una razon):")
print("  claves distintas: %s" % sorted({k for o in nuevas for k in o}))
c = collections.Counter(o.get('clase') or o.get('veredicto') or '(sin clase)' for o in nuevas)
for k, v in sorted(c.items()):
    print("  clase %-14s %d" % (k, v))
print()
sin_razon = [o for o in nuevas if not (o.get('razon') or '').strip()]
print("  lineas nuevas SIN razon escrita (D.8): %d de %d" % (len(sin_razon), len(nuevas)))
print()
ids = set(l.strip() for l in io.open('.v33a/tanda_ids.txt',encoding='utf-8') if l.strip())
por = collections.Counter()
for o in nuevas:
    for k in ('id','candidato','hijo','nodo'):
        if o.get(k) in ids: por[o[k]] += 1; break
print("VEREDICTOS NUEVOS POR CANDIDATO DE LA TANDA:")
for i in io.open('.v33a/tanda_ids.txt',encoding='utf-8'):
    i = i.strip()
    if i: print("  %-46s %d" % (i, por.get(i,0)))
print("  suma: %d" % sum(por.values()))
