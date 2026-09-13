# -*- coding: utf-8 -*-
"""D.38.4: barrido de vecinos del AUDITOR sobre GRAFO MAS BANDEJAS.
Poblacion = dataset/nodos.jsonl + cuarentena/<libro>/*.json, descartando
_insertados y _derivadas. Mide con un instrumento MIO y distinto del de la
aduana: solape de palabras de contenido de (titulo + condiciones + entregable)
y solape de los conjuntos de pasos. Imprime el top-N por candidato INCLUYENDO
los que se quedan por debajo de cualquier umbral, que es lo que un informe de
aduana no imprime.
"""
import json, glob, os, re, sys, io, unicodedata
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

VACIAS = set('''de la el los las un una unos unas y o a en con por para que se su sus
lo al del es son ser estar esta este esto como mas menos no si te tu tus me mi
mis le les nos ya pero cuando donde quien cual cuanto todo toda todos todas
otro otra otros otras hay he ha han haber sobre entre sin hasta desde tras
cada ante bajo cabe contra hacia segun so tambien aun asi'''.split())

def norm(s):
    s = unicodedata.normalize('NFKD', s or '').encode('ascii','ignore').decode()
    return s.lower()

def bolsa(s):
    return set(w for w in re.findall(r'[a-z]{4,}', norm(s)) if w not in VACIAS)

def jac(a,b):
    return len(a&b)/len(a|b) if (a or b) else 0.0

TABLA = json.load(open('fuentes/FUENTES_CANONICAS.json',encoding='utf-8'))

def canonicas(c):
    # MISMO CRITERIO QUE src/informe.py: entra el candidato cuyas fuentes estan
    # TODAS en la tabla canonica vigente. Deja fuera ensayo_referencia_163, que
    # es catalogo ajeno de calibracion y no espera juicio.
    claves = [f.get('clave') for f in (c.get('fuentes') or []) if isinstance(f,dict)]
    return bool(claves) and all(k in TABLA for k in claves)

def cargar():
    graf=[]
    for l in open('dataset/nodos.jsonl',encoding='utf-8'):
        l=l.strip()
        if l: graf.append(json.loads(l))
    band=[]; fuera=0
    for f in glob.glob('cuarentena/*/*.json'):
        p=f.replace(chr(92),'/')
        if '/_insertados/' in p or '/_derivadas/' in p: continue
        try: c=json.load(open(f,encoding='utf-8'))
        except Exception: continue
        if canonicas(c): band.append(c)
        else: fuera+=1
    return graf, band, fuera

graf, band, fuera = cargar()
pob = [('grafo',n) for n in graf] + [('bandeja',n) for n in band]
print('POBLACION DEL BARRIDO: %d = %d del grafo + %d de las bandejas' % (len(pob), len(graf), len(band)))
print('  (bandejas: cuarentena/*/*.json, fuera _insertados y _derivadas, y fuera')
print('   los %d cuyas fuentes NO estan todas en FUENTES_CANONICAS.json, que es el' % fuera)
print('   mismo criterio que src/informe.py aplica desde el 12 sep 2026)')
print()

DE_LA_VUELTA = sys.argv[1:]
idx = {}
for sede,n in pob:
    idx[n['id']] = (sede, bolsa('%s %s %s' % (n.get('titulo',''), n.get('condiciones_activacion',''), n.get('entregable_esperado',''))),
                    set(bolsa(' '.join(n.get('pasos_accionables') or []))))

for cid in DE_LA_VUELTA:
    if cid not in idx: print('NO ESTA EN LA POBLACION:', cid); continue
    sede_c, cab_c, pas_c = idx[cid]
    filas=[]
    for oid,(sede_o, cab_o, pas_o) in idx.items():
        if oid==cid: continue
        c = jac(cab_c, cab_o); p = jac(pas_c, pas_o)
        filas.append((max(c,p), c, p, sede_o, oid))
    filas.sort(reverse=True)
    print('='*94)
    print('CANDIDATO %s   [%s]' % (cid, sede_c))
    print('  %-6s %-7s %-9s %s' % ('maximo','cabecera','pasos','vecino'))
    for m,c,p,s,o in filas[:6]:
        print('  %.3f  %.3f    %.3f     %-9s %s' % (m,c,p,s,o))
