# -*- coding: utf-8 -*-
"""MI FRONTERA DE cap_07, declarada por mi y contada por el instrumento."""
import io
F='fuentes/scott_radical_candor/cap_07.md'
src=io.open(F,encoding='utf-8').read().split('\n')
# (linea_rotulo, ultima_linea, mi_clase)   SI = yo lo extraeria, NO = no
PIEZAS=[
 (9,43,'NO'),(45,63,'NO'),(65,77,'SI'),(79,89,'NO'),(91,111,'SI'),(113,129,'SI'),
 (131,153,'SI'),(155,163,'SI'),(165,179,'NO'),(181,195,'SI'),(197,211,'SI'),
 (213,223,'NO'),(225,229,'SI'),(231,233,'SI'),(235,237,'SI'),(239,243,'SI'),
 (245,249,'SI'),(251,257,'SI'),(259,289,'SI'),(291,293,'SI'),(295,301,'SI'),
 (303,321,'NO'),(323,347,'SI'),(349,357,'SI'),(359,365,'SI'),(367,373,'SI'),
 (375,379,'SI'),(381,383,'SI'),(385,387,'SI'),(389,401,'SI'),(403,407,'SI'),
 (409,419,'SI'),(421,429,'NO'),(431,433,'NO'),
]
si=no=0
for a,b,c in PIEZAS:
    if c=='SI': si+=1
    else: no+=1
    print('%-3s L%-3d a L%-3d | sed -n %dp -> %s'%(c,a,b,a,src[a-1][:66]))
print()
print('PIEZAS QUE MI LECTURA CUENTA EN cap_07: %d'%len(PIEZAS))
print('  SI (yo escribiria nodo): %d'%si)
print('  NO (yo no extraeria)   : %d'%no)
cub=set()
for a,b,c in PIEZAS: cub.update(range(a,b+1))
falta=[i for i,l in enumerate(src,1) if l.strip() and i>7 and i not in cub]
print('lineas con contenido de L8 en adelante NO cubiertas por mi frontera: %d %s'%(len(falta),falta))
