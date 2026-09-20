# -*- coding: utf-8 -*-
"""Mi recuento propio del peso del resumen sobre la bandeja entera de grove,
para contrastar la relectura de d058 que la vuelta 54 publico en PP.4.h."""
import json, glob, sys
sys.path.insert(0, ".")
from src import comun
tot_r = tot_c = 0; band = []
files = sorted(glob.glob("cuarentena/grove_high_output/*.json"))
for p in files:
    d = json.load(open(p, encoding="utf-8"))
    c = len(comun.normalizar_texto(comun.texto_comparable(d)))
    r = len(comun.normalizar_texto(d.get("resumen_teorico", "")))
    tot_r += r; tot_c += c
    if c: band.append((100.0 * r / c, d["id"]))
band.sort()
print("  fichas medidas                        : %d" % len(files))
print("  funcion usada                         : src.comun.texto_comparable")
print("  EL PESO DEL RESUMEN SOBRE LA BANDEJA ENTERA : %.1f por ciento" % (100.0 * tot_r / tot_c))
print("    numerador   %d  caracteres normalizados de resumen_teorico, sumados" % tot_r)
print("    denominador %d  caracteres normalizados de texto_comparable, sumados" % tot_c)
print("  LA BANDA (minimo y maximo, no media):")
print("    menor %% de resumen : %.1f  (%s)" % band[0])
print("    mayor %% de resumen : %.1f  (%s)" % band[-1])
