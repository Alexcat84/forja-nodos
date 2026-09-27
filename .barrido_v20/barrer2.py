import io, json, glob, os, sys, time
sys.path.insert(0, os.getcwd())
from src import aduana, config as mc
u = mc.cargar()
grafo = [json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
rut = sorted(p for p in glob.glob(os.path.join('cuarentena', '*', '*.json'))
             if '_insertados' not in p and '_derivadas' not in p)
band = [(p, json.load(io.open(p, encoding='utf-8'))) for p in rut]
obj = [l.strip() for l in io.open(sys.argv[1], encoding='utf-8') if l.strip()]
obj = list(reversed(obj))
sal = io.open(sys.argv[2], 'a', encoding='utf-8')
sal.write('POBLACION: grafo %d + bandejas %d = %d' % (len(grafo), len(band), len(grafo)+len(band)) + chr(10))
sal.flush()
for ruta in obj:
    ruta = ruta.replace('/', os.sep)
    c = json.load(io.open(ruta, encoding='utf-8'))
    pob = grafo + [n for (p, n) in band if os.path.abspath(p) != os.path.abspath(ruta)]
    t = time.time()
    v = aduana.buscar_vecinos(c, pob, u)
    sal.write('### %s   [poblacion %d]   [%.0fs]' % (c['id'], len(pob), time.time()-t) + chr(10))
    if not v:
        sal.write('    SIN VECINO' + chr(10))
    for x in v:
        con = x.get('contra') or x.get('nodo') or x.get('id') or '?'
        if isinstance(con, dict):
            con = con.get('id', '?')
        sen = ', '.join('%s=%s' % (k, (round(y, 3) if isinstance(y, float) else y))
                        for k, y in sorted(x.get('senales', {}).items()) if y)
        sal.write('    VECINO %s  |  %s' % (con, sen) + chr(10))
    sal.flush()
sal.write('FIN' + chr(10))
sal.flush()
