# -*- coding: utf-8 -*-
import json, glob, re, os

F = 'fuentes/scott_radical_candor/cap_09.md'
L = open(F, encoding='utf-8').read().split('\n')

CINCO = [
    ("P22", 301, 313, "revisar_critica_mujer_agresiva_cuatro_tacticas"),
    ("P23", 315, 329, "responder_critica_abrasiva_cuatro_reglas"),
    ("P24", 331, 361, "entregar_evaluacion_formal_desempenio_nueve_consejos"),
    ("P27", 383, 413, "conducir_reuniones_salto_nivel_diez_reglas"),
    ("P28", 415, 425, "resolver_dudas_frecuentes_reuniones_salto_nivel"),
]

print("LAS CINCO, REMEDIDAS Y CON SUS PASOS")
tw = tp = 0
for n, a, b, i in CINCO:
    w = sum(len(L[k - 1].split()) for k in range(a, b + 1))
    d = json.load(open('cuarentena/scott_radical_candor/%s.json' % i, encoding='utf-8'))
    p = len(d['pasos_accionables'])
    tw += w; tp += p
    print("  %-4s L%-3d a L%-3d  %5d palabras  %3d pasos  %6.1f palabras por paso  %s"
          % (n, a, b, w, p, w / p, i))
print("  SUMA %28d palabras  %3d pasos  %6.1f palabras por paso" % (tw, tp, tw / tp))

# densidad de los 20 de cap_09, y del lote entero
cap09 = []
todos = 0
for f in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    todos += len(d['pasos_accionables'])
    m = re.search(r'cap_(\d\d)', d['resumen_teorico'])
    if m and m.group(1) == '09':
        cap09.append((d['id'], len(d['pasos_accionables'])))
cuerpo = sum(len(l.split()) for l in L[7:])
print()
print("cap_09 AL CERRAR: %d candidatos, %d pasos" % (len(cap09), sum(p for _, p in cap09)))
print("  cuerpo de cap_09: %d palabras  ->  %.1f palabras por candidato"
      % (cuerpo, cuerpo / len(cap09)))
print("  el nodo con mas pasos del capitulo: %s"
      % max(cap09, key=lambda t: t[1]).__repr__())
print("LOTE 4 AL CERRAR cap_09: %d candidatos, %d pasos"
      % (len(glob.glob('cuarentena/scott_radical_candor/*.json')), todos))
