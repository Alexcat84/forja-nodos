# -*- coding: utf-8 -*-
"""Palabras de cada tramo de cap_05 que la vuelta 51 mino, con sed mas wc -w
por debajo (subprocess), corrido por el auditor en la APERTURA CIEGA."""
import io,sys,subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
RANGOS=[(21,21),(23,23),(33,35),(37,39),(41,41),(43,43)]
F='fuentes/grove_high_output/cap_05.md'
print("%-16s %8s"%("tramo","palabras"))
tot=0
for a,b in RANGOS:
    txt=subprocess.check_output(['sed','-n','%d,%dp'%(a,b),F])
    n=len(txt.decode('utf-8').split()); tot+=n
    print("%-16s %8d"%("L%d a L%d"%(a,b),n))
print("%-16s %8d"%("suma de los seis",tot))
