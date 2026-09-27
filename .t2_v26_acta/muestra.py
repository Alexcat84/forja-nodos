# -*- coding: utf-8 -*-
"""LA MUESTRA PINEADA DE LOS SANO (AUDITOR_FORJA.md 7).
Elige con semilla escrita, NO a ojo, e imprime SOLO el par: la razon se destapa despues."""
import json,io,random,sys
SEMILLA=20260913
ver=[json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl',encoding='utf-8')]
tanda=ver[156:]
sanos=[v for v in tanda if v.get('veredicto')=='SANO']
pares=[]
vistos=set()
for v in sanos:
    k=(v['candidato'],v['vecino'])
    if k in vistos: continue
    vistos.add(k); pares.append(k)
print('LINEAS DE LA TANDA          :',len(tanda))
print('de ellas SANO               :',len(sanos))
print('pares SANO distintos        :',len(pares))
n=max(3,-(-len(pares)*20//100))
n=min(n,20)
print('tamanio de muestra (max(3, 20%%), techo 20): %d'%n)
print('SEMILLA ESCRITA EN EL ACTA  :',SEMILLA)
random.seed(SEMILLA)
muestra=sorted(random.sample(pares,n))
print()
for i,(a,b) in enumerate(muestra,1):
    print('%2d. %s  ||  %s'%(i,a,b))
