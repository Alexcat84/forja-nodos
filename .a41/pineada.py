# -*- coding: utf-8 -*-
"""MUESTRA PINEADA DE LOS SANO DE LA TANDA 515..729 (AUDITOR_FORJA.md 7).
Semilla escrita en el acta: 4120260918  (ACTA 41, 2026-09-18)."""
import json, io, random
SEM = 4120260918
L=[json.loads(l) for l in io.open('bitacora/VEREDICTOS.jsonl',encoding='utf-8') if l.strip()]
t=[(i+515,v) for i,v in enumerate(L[514:729]) if v.get('veredicto')=='SANO']
print('SANO en la tanda:',len(t))
n=min(20,max(3,int(len(t)*0.2)))
print('20 por ciento =',len(t)*0.2,'  techo 20  -> muestra =',n)
r=random.Random(SEM)
m=sorted(r.sample(t,n),key=lambda x:x[0])
print('semilla:',SEM)
print('lineas elegidas:',[i for i,_ in m])
for i,v in m:
    print('-'*95)
    print('L%d  %s  contra  %s'%(i,v['candidato'],v['vecino']))
    print('   senales:',v.get('senales'),' arista:',repr(v.get('arista')))
    print('   razon (%d chars): %s'%(len(v['razon']), v['razon'][:420]))
