# PRIMERA LINEA (HEREDADO 4): CERO IDS TECLEADOS. Los vecinos salen del campo 'vecino' de las
# lineas nuevas de bitacora/VEREDICTOS.jsonl. LA POBLACION DONDE LOS BUSCO ES GRAFO MAS
# BANDEJAS (D.38.4): dataset/nodos.jsonl mas cuarentena/<libro>/*.json. CERO razones impresas.
import json, io, glob, os, subprocess
ANTES = 'ef3e7f9'
def carga(ref):
    t = subprocess.check_output(['git','show','%s:bitacora/VEREDICTOS.jsonl'%ref]).decode('utf-8')
    return [json.loads(l) for l in t.splitlines() if l.strip()]
nuevas = carga('HEAD')[len(carga(ANTES)):]
tanda = set(l.strip() for l in io.open('.v33a/tanda_ids.txt',encoding='utf-8') if l.strip())
vec = []
for o in nuevas:
    for k in ('vecino','candidato'):
        v = o.get(k)
        if v and v not in tanda and v not in vec: vec.append(v)
d = {}; donde = {}
for l in io.open('dataset/nodos.jsonl',encoding='utf-8'):
    if l.strip():
        o = json.loads(l); d[o['id']] = o; donde[o['id']] = 'GRAFO'
for p in glob.glob('cuarentena/*/*.json'):
    if os.sep + '_' in p: continue
    try: o = json.load(io.open(p, encoding='utf-8'))
    except Exception: continue
    if isinstance(o, dict) and o.get('id') and o['id'] not in d:
        d[o['id']] = o; donde[o['id']] = 'BANDEJA ' + p.split(os.sep)[1]
sal = io.open('.v33a/vecinos.txt','w',encoding='utf-8')
sal.write("LOS %d VECINOS DISTINTOS QUE LA TANDA LEVANTA FUERA DE ELLA MISMA, CON SUS PASOS\n" % len(vec))
sal.write("poblacion donde los busco: GRAFO (dataset, 282) MAS BANDEJAS (cuarentena, D.38.4)\n")
for i in vec:
    o = d[i]
    sal.write("\n===== %s  [%s]  (%d pasos) =====\n" % (i, donde[i], len(o['pasos_accionables'])))
    sal.write("TITULO: %s\n" % o['titulo'])
    sal.write("ACTIVA: %s\n" % o['condiciones_activacion'])
    for k,p in enumerate(o['pasos_accionables'],1):
        sal.write("  %2d. %s\n" % (k,p))
sal.close()
for i in vec: print("  %-48s %s" % (i, donde[i]))
print("escrito .v33a/vecinos.txt con %d vecinos" % len(vec))
