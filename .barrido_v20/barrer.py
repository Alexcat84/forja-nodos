# BARRIDO DE VECINOS, D.38.4 con la correccion declarada de la ACTA 18.
# Instrumento de la casa: src.aduana.buscar_vecinos, el mismo que usa
# forja.py informe. La poblacion es grafo + bandejas MENOS el propio candidato.
import io, json, glob, os, sys
sys.path.insert(0, os.getcwd())
from src import aduana, config as modulo_config

umbrales = modulo_config.cargar()

grafo = [json.loads(l) for l in io.open('dataset/nodos.jsonl', encoding='utf-8') if l.strip()]
rutas_band = sorted(p for p in glob.glob(os.path.join('cuarentena', '*', '*.json'))
                    if '_insertados' not in p and '_derivadas' not in p)
bandeja = [(p, json.load(io.open(p, encoding='utf-8'))) for p in rutas_band]
poblacion_total = grafo + [n for _, n in bandeja]
print('POBLACION: grafo %d + bandejas %d = %d' % (len(grafo), len(bandeja), len(poblacion_total)))

objetivo = [l.strip() for l in io.open(sys.argv[1], encoding='utf-8') if l.strip()]
print('CANDIDATOS BARRIDOS: %d' % len(objetivo))
print('')
total_vecinos = 0
con_vecino = 0
for ruta in objetivo:
    ruta = ruta.replace('/', os.sep)
    cand = json.load(io.open(ruta, encoding='utf-8'))
    pob = [n for n in poblacion_total if n is not dict(cand)]
    pob = [n for (p, n) in bandeja if os.path.abspath(p) != os.path.abspath(ruta)]
    pob = grafo + pob
    vec = aduana.buscar_vecinos(cand, pob, umbrales)
    print('### %s   [poblacion %d]' % (cand['id'], len(pob)))
    if not vec:
        print('    SIN VECINO')
    for v in vec:
        con = v.get('contra') or v.get('nodo') or v.get('id') or ''
        if isinstance(con, dict):
            con = con.get('id', '?')
        sen = ', '.join('%s=%s' % (k, (round(x, 3) if isinstance(x, float) else x))
                        for k, x in sorted(v.get('senales', {}).items()) if x)
        print('    VECINO %s  |  %s' % (con, sen))
        total_vecinos += 1
    if vec:
        con_vecino += 1
    print('')
print('TOTAL: %d vecinos levantados sobre %d candidatos; %d candidatos con vecino, %d sin ninguno'
      % (total_vecinos, len(objetivo), con_vecino, len(objetivo) - con_vecino))
