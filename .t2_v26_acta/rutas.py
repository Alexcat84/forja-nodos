# -*- coding: utf-8 -*-
"""5.5 / cosecha 7.B: LA RUTA QUE PROMETE PRUEBA ES CIFRA.
Censo COMPLETO de las rutas que el tramo de la vuelta 25 publica, no solo las .v25."""
import re,io,os
txt=io.open('docs/loop/REPORTE.md',encoding='utf-8').read()
ini=txt.index('# VUELTA 25, la tarea bloqueante')
tramo=txt[ini:]
pat=re.compile(r'[`\s(]((?:\.[A-Za-z0-9_]+|scripts|tests|src|docs|config|esquema|censos)/[A-Za-z0-9_./-]+\.[A-Za-z0-9_]+)')
rutas=sorted(set(m.group(1) for m in pat.finditer(tramo)))
faltan=[];cero=[];ok=[]
for r in rutas:
    if not os.path.exists(r): faltan.append(r)
    elif os.path.getsize(r)==0: cero.append(r)
    else: ok.append(r)
print('rutas distintas publicadas en el tramo de la vuelta 25 : %d'%len(rutas))
print('  existen y NO estan en cero bytes                     : %d'%len(ok))
print('  INEXISTENTES                                         : %d'%len(faltan))
for r in faltan: print('      %s'%r)
print('  DE CERO BYTES                                        : %d'%len(cero))
for r in cero: print('      %s   (%d bytes)'%(r,os.path.getsize(r)))
