# -*- coding: utf-8 -*-
"""CADA INFORME DE ADUANA CONTRA EL RELOJ DE SU CANDIDATO.

EXTRACTOR.md 16 pide el informe EN EL MISMO ACTO en que se escribe el candidato.
Esta vuelta lo corrio en tandas y ya lo declaro (G1.7, caida 3). Lo que este
instrumento comprueba es lo que de ahi queda en pie: que NINGUN candidato se
toco DESPUES de su informe, o sea que el saldo publicado describe los bytes que
hoy estan en la bandeja y no una version anterior. Cero celdas tecleadas."""
import glob, os, time

def reloj(r):
    return time.strftime('%H:%M:%S', time.localtime(os.path.getmtime(r)))

cands = sorted(glob.glob('cuarentena/gerber_emyth/*.json'))
aduanas = sorted(glob.glob('.gerber_v1/aduana_*.txt'))
ultimo_cand = max(os.path.getmtime(c) for c in cands)
primer_aduana = min(os.path.getmtime(a) for a in aduanas)

print('candidatos en la bandeja            : %d' % len(cands))
print('ficheros de aduana corridos         : %d' % len(aduanas))
print('el candidato tocado MAS TARDE       : %s  (%s)'
      % (reloj(max(cands, key=os.path.getmtime)),
         os.path.basename(max(cands, key=os.path.getmtime))))
print('el informe de aduana MAS TEMPRANO   : %s  (%s)'
      % (reloj(min(aduanas, key=os.path.getmtime)),
         os.path.basename(min(aduanas, key=os.path.getmtime))))
print('')
print('candidatos tocados DESPUES de su informe mas temprano : %d'
      % sum(1 for c in cands if os.path.getmtime(c) > primer_aduana))
print('')
if ultimo_cand < primer_aduana:
    print('VERDE: los %d candidatos estaban escritos y quietos antes del primer' % len(cands))
    print('informe. El saldo publicado es el de los bytes que hoy estan en la bandeja.')
else:
    print('ROJO: algun candidato se movio despues de un informe. El saldo no es suyo.')
