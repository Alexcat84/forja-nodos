# -*- coding: utf-8 -*-
"""Codigo del AUDITOR. Reproduce la cadencia SOBRE EL REGISTRO DE ANTES DE LA
DECLARACION (git show f38c34e:docs/loop/DEUDA.jsonl), que es el unico estado en el
que la pregunta 'de que clase es la vuelta 6' todavia tiene respuesta: declararla
mueve el ancla, y despues --clase 6 ya dice LIBRE por 0 de 5 desde ella misma."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import scripts.deuda as D

s = D.leer('.g6aud/DEUDA_f38c34e.jsonl')
print("registro: docs/loop/DEUDA.jsonl del commit f38c34e (antes de la declaracion)")
print("  pendientes: %d    pagadas: %d"
      % (len(D.pendientes(s)), len([x for x in s if x.get('tipo') == 'pago'])))
print("  ultima de saneamiento de la linea 'gerber_emyth': %s"
      % D.ultima_saneamiento(s, 'gerber_emyth'))
print("")
for v in (5, 6, 7):
    clase, motivo = D.clase_de_vuelta(v, s, 'gerber_emyth')
    print("  --clase %d  ->  %s" % (v, clase))
    print("      %s" % motivo)
