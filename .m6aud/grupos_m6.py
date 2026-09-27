import re
rep=open('docs/loop/REPORTE.md',encoding='utf-8').read().split('\n')
start=[i for i,l in enumerate(rep) if l.startswith('# VUELTA 5 DEL FRENTE')][0]
for cap in ['cap_12','cap_13','cap_14','cap_15']:
    bruta=[l for l in open(f'.v5m/frontera/{cap}_bruta.txt',encoding='utf-8').read().split('\n') if l.startswith('| R') or l.startswith('| P')]
    bd={}
    for l in bruta:
        c=[x.strip() for x in l.strip().strip('|').split('|')]
        bd[c[0]]=(c[1],int(c[2]))
    i=[k for k in range(start,len(rep)) if rep[k].startswith('<!-- TALLADO') and cap+'_bruta' in rep[k]][0]
    k=i+2; tot=0
    while rep[k].startswith('|'):
        c=[x.strip() for x in rep[k].strip().strip('|').split('|')]
        m=re.match(r'R(\d+) a R(\d+)$',c[0])
        if m:
            a,b=int(m.group(1)),int(m.group(2))
            names=['R%d'%n for n in range(a,b+1)]
            s=sum(bd[n][1] for n in names if n in bd)
            print(f'{cap} {c[0]:10} reporte {c[1]:12} {c[2]:>5} | bruta {bd.get(names[0],("?",))[0]} a {bd.get(names[-1],("?",))[0]} suma {s}')
        if 'cuerpo' not in c[0]:
            try: tot+=int(c[2])
            except: pass
        k+=1
    print(f'{cap} SUMA DE LA COLUMNA palabras de la tabla del reporte: {tot}')
