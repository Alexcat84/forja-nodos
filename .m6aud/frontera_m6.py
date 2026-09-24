import re,sys
def rango(s):
    m=re.findall(r'L(\d+)',s)
    if not m: return None
    a=int(m[0]); b=int(m[-1]) if len(m)>1 else a
    return a,b
def check(tabla_lines, cap, etiqueta):
    src=open(f'fuentes/marquet_turn_the_ship/{cap}.md',encoding='utf-8').read().split('\n')
    wl=[len(l.split()) for l in src]
    cubierto={}
    filas=0; malas=[]
    for l in tabla_lines:
        cols=[c.strip() for c in l.strip().strip('|').split('|')]
        if len(cols)<3 or cols[0] in('pieza','---') or 'cuerpo entero' in cols[0]: continue
        r=rango(cols[1]);
        if not r: continue
        try: w=int(cols[2].strip('*'))
        except: continue
        filas+=1
        real=sum(wl[r[0]-1:r[1]])
        if real!=w: malas.append((cols[0],cols[1],w,real))
        for n in range(r[0],r[1]+1): cubierto.setdefault(n,[]).append(cols[0])
    sol=[(n,v) for n,v in cubierto.items() if len(v)>1 and wl[n-1]>0]
    sincubrir=[n for n in range(9,len(wl)+1) if wl[n-1]>0 and n not in cubierto]
    print(f'{etiqueta} {cap}: filas {filas}, discrepancias de palabras {len(malas)}, lineas con palabras solapadas {len(sol)}, lineas con palabras sin cubrir {len(sincubrir)}')
    for m in malas: print('   DISCREPA',m)
    for s in sol: print('   SOLAPE L%d'%s[0],s[1])
    for s in sincubrir: print('   SIN CUBRIR L%d'%s)
rep=open('docs/loop/REPORTE.md',encoding='utf-8').read().split('\n')
start=[i for i,l in enumerate(rep) if l.startswith('# VUELTA 5 DEL FRENTE')][0]
for cap in ['cap_12','cap_13','cap_14','cap_15']:
    bruta=open(f'.v5m/frontera/{cap}_bruta.txt',encoding='utf-8').read().split('\n')
    check([l for l in bruta if l.startswith('|')],cap,'BRUTA  ')
    i=[k for k in range(start,len(rep)) if rep[k].startswith('<!-- TALLADO') and cap+'_bruta' in rep[k]][0]
    t=[]; k=i+2
    while rep[k].startswith('|'): t.append(rep[k]); k+=1
    check(t,cap,'REPORTE')
