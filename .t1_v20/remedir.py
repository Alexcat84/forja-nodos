import subprocess, sys
tramos = [("P22",301,313),("P23",315,329),("P24",331,361),("P27",383,413),("P28",415,425)]
f='fuentes/scott_radical_candor/cap_09.md'
L=open(f,encoding='utf-8').read().split('\n')
tot=0
for n,a,b in tramos:
    w=sum(len(L[i-1].split()) for i in range(a,b+1))
    tot+=w
    print(f"  {n}  L{a} a L{b}  {w:5d} palabras")
print(f"  SUMA de las cinco: {tot} palabras")
cuerpo=sum(len(l.split()) for l in L[7:])
print(f"  cuerpo de cap_09 (sed -n '8,$p' | wc -w): {cuerpo}")
print(f"  las cinco sobre el cuerpo: {100*tot/cuerpo:.1f} por ciento")
