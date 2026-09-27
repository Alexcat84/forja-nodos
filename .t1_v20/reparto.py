import json, glob, re, collections
# ROTULO: primer cap_NN que aparece en el resumen_teorico de cada candidato de la bandeja.
# El rotulo y el codigo dicen lo mismo: se busca 'cap_NN' EN EL TEXTO del resumen_teorico.
cand = collections.defaultdict(lambda: [0,0])
resid = []
for f in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    m = re.search(r'cap_(\d\d)', d.get('resumen_teorico',''))
    k = 'cap_'+m.group(1) if m else 'SIN'
    if not m: resid.append(d['id'])
    cand[k][0] += 1
    cand[k][1] += len(d.get('pasos_accionables',[]))
tc = tp = 0
for k in sorted(cand):
    print(f"  {k}: {cand[k][0]:3d} cand, {cand[k][1]:4d} pasos")
    tc += cand[k][0]; tp += cand[k][1]
print(f"  TOTAL: {tc:3d} cand, {tp:4d} pasos")
print(f"  FILA DE RESIDUO 'SIN' -> {len(resid)} ids: {resid}")
