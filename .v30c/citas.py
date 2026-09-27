import re
txt=open('docs/loop/ACTA_AUDITOR.md',encoding='utf-8').read().split('\n')
# indice de actas
actas={}
cur=None
for i,l in enumerate(txt,1):
    m=re.match(r'^# ACTA (\d+)\.',l)
    if m: cur=int(m.group(1)); actas[cur]=[i,None]
    if cur and actas[cur][1] is None: pass
ks=sorted(actas)
for a,b in zip(ks,ks[1:]): actas[a][1]=actas[b][0]-1
actas[ks[-1]][1]=len(txt)
def sec(acta,s):
    ini,fin=actas[acta]
    pat=re.compile(r'^#+\s+\*?\*?`?'+re.escape(s)+r'[\.\:]')
    for i in range(ini,fin+1):
        if pat.match(txt[i-1]): return i,txt[i-1]
    return None,None
for acta,s in [(28,'2.2'),(28,'4.3'),(28,'4.4'),(28,'6.10'),(27,'2.2'),(25,'')]:
    if not s: continue
    i,h=sec(acta,s)
    print(f"ACTA {acta} seccion {s}: ", (str(i)+' -> '+h[:130]) if i else "NO EXISTE")
