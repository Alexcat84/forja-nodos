import json, glob, os, sys
print("INSTRUMENTO .vg01a/cuentas.py  SIN CONSTANTES TECLEADAS: lee dataset/nodos.jsonl, bitacora/ y cuarentena/ del disco")
nodos=[json.loads(l) for l in open('dataset/nodos.jsonl',encoding='utf-8') if l.strip()]
sig=sum(len(n.get('nodos_siguientes') or []) for n in nodos)
prev=sum(len(n.get('nodos_previos') or []) for n in nodos)
ver=[json.loads(l) for l in open('bitacora/VEREDICTOS.jsonl',encoding='utf-8') if l.strip()]
print("nodos                :", len(nodos))
print("aristas siguientes   :", sig)
print("aristas previos      :", prev)
print("veredictos           :", len(ver))
print("de ellos no_consumada:", sum(1 for v in ver if v.get('no_consumada') is True))
f={}
for n in nodos:
    for fu in (n.get('fuentes') or []):
        f[fu.get('clave','?')]=f.get(fu.get('clave','?'),0)+1
print("FUENTES EN EL GRAFO:")
for k,v in sorted(f.items(), key=lambda x:-x[1]): print("   %-32s %4d"%(k,v))
def cuenta(d): return len(glob.glob(os.path.join(d,'*.json')))
print("BANDEJAS (descartando _insertados y _derivadas, D.38.4):")
tot=0
for d in sorted(glob.glob(os.path.join('cuarentena','*'))):
    b=os.path.basename(d)
    if not os.path.isdir(d) or b.startswith('_'): continue
    c=cuenta(d); tot+=c
    print("   %-32s %4d"%(b,c))
print("   %-32s %4d"%('TOTAL BANDEJAS',tot))
print("   %-32s %4d"%('POBLACION D.38.4 grafo+bandejas',len(nodos)+tot))
print("ARCHIVADOS EN _insertados:")
for d in sorted(glob.glob(os.path.join('cuarentena','_insertados','*'))):
    if os.path.isdir(d): print("   %-32s %4d"%(os.path.basename(d),cuenta(d)))
