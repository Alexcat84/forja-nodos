# -*- coding: utf-8 -*-
"""Ordena los pares de la tanda por solape MIO, para que la eleccion de cuales
releo a ciegas sea de instrumento y no a ojo (AUDITOR_FORJA.md 7)."""
import json, glob, io, re, sys, unicodedata
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
VACIAS = set('''de la el los las un una unos unas y o a en con por para que se su sus
lo al del es son ser estar esta este esto como mas menos no si te tu tus me mi
mis le les nos ya pero cuando donde quien cual cuanto todo toda todos todas
otro otra otros otras hay he ha han haber sobre entre sin hasta desde tras
cada ante bajo cabe contra hacia segun so tambien aun asi'''.split())
def norm(s):
    return unicodedata.normalize('NFKD', s or '').encode('ascii','ignore').decode().lower()
def bolsa(s):
    return set(w for w in re.findall(r'[a-z]{4,}', norm(s)) if w not in VACIAS)
def jac(a,b): return len(a&b)/len(a|b) if (a or b) else 0.0
N={}
for l in io.open('dataset/nodos.jsonl',encoding='utf-8'):
    if l.strip():
        d=json.loads(l); N[d['id']]=d
for f in glob.glob('cuarentena/*/*.json')+glob.glob('cuarentena/_insertados/*/*.json'):
    p=f.replace(chr(92),'/')
    if '/_derivadas/' in p: continue
    try: d=json.load(open(f,encoding='utf-8'))
    except Exception: continue
    N.setdefault(d.get('id'), d)
def perfil(d):
    return (bolsa('%s %s %s'%(d.get('titulo',''),d.get('condiciones_activacion',''),d.get('entregable_esperado',''))),
            bolsa(' '.join(d.get('pasos_accionables') or [])))
filas=[]
for l in io.open('.t1_v26_auditor/pares_hoy.txt',encoding='utf-8'):
    p=l.rstrip('\n').split('\t')
    if len(p)!=3: continue
    n,a,b=int(p[0]),p[1],p[2]
    if a not in N or b not in N: print('FALTA',a,b); continue
    ca,pa=perfil(N[a]); cb,pb=perfil(N[b])
    c,ps=jac(ca,cb),jac(pa,pb)
    filas.append((max(c,ps),c,ps,n,a,b))
filas.sort(reverse=True)
print('PARES DE LA TANDA ORDENADOS POR SOLAPE DEL AUDITOR:', len(filas))
print('%-6s %-8s %-7s %-5s %s'%('max','cabecera','pasos','linea','par'))
for m,c,ps,n,a,b in filas:
    print('%.3f  %.3f    %.3f   L%-4d %s  ||  %s'%(m,c,ps,n,a,b))
