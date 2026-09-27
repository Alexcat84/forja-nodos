# -*- coding: utf-8 -*-
"""Cada ficha de cap_04 declara dentro de su resumen_teorico su PIEZA, su rango de
lineas y sus palabras. Aqui se recuenta el rango declarado contra el texto fuente.
Instrumento de la APERTURA CIEGA de la vuelta 49: lee las fichas y el libro, ningun reporte."""
import io,sys,json,glob,os,re
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
L=open('fuentes/grove_high_output/cap_04.md',encoding='utf-8').read().split('\n')
def pal(a,b): return sum(len(L[i-1].split()) for i in range(a,b+1))
print("%-52s %-6s %-14s %8s %8s %s" % ("ficha","pieza","rango declarado","dice","cuento","cuadra"))
malos=0; tot=0
for f in sorted(glob.glob('cuarentena/grove_high_output/*.json')):
    d=json.load(open(f,encoding='utf-8')); r=d.get('resumen_teorico','')
    if 'cap_04.md' not in r: continue
    m=re.search(r'PIEZA (P\d+[a-z]?)[^.]*?L(\d+) a L(\d+),\s*([\d.]+)\s*palabras',r)
    if not m:
        print("%-52s  (no declara pieza, rango y palabras en el molde buscado)" % os.path.basename(f)[:-5][:52]); continue
    pz,a,b,w=m.group(1),int(m.group(2)),int(m.group(3)),int(m.group(4).replace('.',''))
    c=pal(a,b); tot+=1
    ok = "SI" if c==w else "NO  <-- discrepa en %d" % (w-c)
    if c!=w: malos+=1
    print("%-52s %-6s L%-4d a L%-4d %8d %8d %s" % (os.path.basename(f)[:-5][:52],pz,a,b,w,c,ok))
print()
print("fichas de cap_04 con pieza, rango y palabras declarados: %d ; cuadran %d ; discrepan %d" % (tot,tot-malos,malos))
