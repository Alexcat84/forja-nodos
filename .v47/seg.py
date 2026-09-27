# -*- coding: utf-8 -*-
"""DERIVA segundos= DE LA LINEA real DE time, QUE ES EL INSTRUMENTO.

El candidato 1 de esta vuelta se cronometro con `time` porque se lanzo en segundo
plano tras pasarse del tope de una corrida en primer plano. Los candidatos 2 en
adelante llevan el formato de reloj de la vuelta 46 (inicio, fin, segundos), que es
el que .v47/tanda.py lee. Este script escribe esa misma linea para el candidato 1
SIN TECLEAR LA CIFRA: la saca de la linea `real` que imprimio `time`.

    python .v47/seg.py .v47/reloj_c01.txt
"""
import io
import re
import sys

ruta = sys.argv[1]
s = io.open(ruta, encoding="utf-8").read()
m = re.search(r"real\s+(\d+)m([\d.]+)s", s)
seg = int(round(int(m.group(1)) * 60 + float(m.group(2))))
if "segundos=" not in s:
    io.open(ruta, "a", encoding="utf-8", newline="\n").write(
        "codigo=0\nsegundos=%d   (derivado por .v47/seg.py de la linea real de time,"
        " que es el instrumento)\n" % seg)
print("segundos=%d" % seg)
