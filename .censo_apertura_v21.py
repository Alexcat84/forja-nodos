# -*- coding: utf-8 -*-
"""Censo de la bandeja del lote 4, VERSION 3, la que publico.

REMEDIO de mi caida de la ACTA 19 7.1. Alli mi rotulo prometia 'la unidad
que cada uno declara' y mi instrumento miraba UNA sola cabecera, asi que
un candidato cayo en 'SIN' y una fila salio corta. Este instrumento:

  NIVEL 1  la declaracion textual 'UNIDAD DE ORIGEN: .../cap_NN.md'
  NIVEL 2  si no la hay, el PRIMER 'cap_NN' que aparezca en el fichero,
           y la fila se marca NIVEL 2, que es deducida y no declarada
  SIN      si no hay ninguna de las dos

Y publica la cuenta de cada nivel, para que nadie tenga que fiarse.
"""
import json, os, re

DIR = "cuarentena/scott_radical_candor"
filas = []
for nombre in sorted(os.listdir(DIR)):
    if not nombre.endswith(".json"):
        continue
    crudo = open(os.path.join(DIR, nombre), encoding="utf-8").read()
    d = json.loads(crudo)
    m1 = re.search(r"UNIDAD DE ORIGEN:[^,]*?(cap_\d\d)\.md", crudo)
    if m1:
        cap, nivel = m1.group(1), 1
    else:
        m2 = re.search(r"cap_\d\d", crudo)
        cap, nivel = (m2.group(0), 2) if m2 else ("SIN", 0)
    rt = d.get("resumen_teorico", "")
    mp = re.search(r"PIEZA (P\d+) DE LA FRONTERA", rt)
    filas.append((cap, nivel, nombre[:-5], len(d.get("pasos_accionables", [])),
                  mp.group(1) if mp else "-",
                  d.get("fuentes", [{}])[0].get("fecha", "")))

filas.sort()
print("--- POR CAPITULO (bandeja entera del lote 4) ---")
caps = {}
for f in filas:
    caps.setdefault(f[0], [0, 0])
    caps[f[0]][0] += 1
    caps[f[0]][1] += f[3]
for c in sorted(caps):
    print("%s\tcandidatos=%d\tpasos=%d" % (c, caps[c][0], caps[c][1]))
print("TOTAL\tcandidatos=%d\tpasos=%d" % (len(filas), sum(f[3] for f in filas)))
print("")
print("--- NIVEL QUE RESPONDIO ---")
niv = {}
for f in filas:
    niv[f[1]] = niv.get(f[1], 0) + 1
for k in sorted(niv):
    print("nivel %d\t%d" % (k, niv[k]))
print("filas nivel 2 (deducidas, no declaradas):")
for f in filas:
    if f[1] == 2:
        print("   %s -> %s" % (f[2], f[0]))
print("")
print("--- cap_09 ENTERO, ORDENADO POR PIEZA ---")
n9 = [f for f in filas if f[0] == "cap_09"]
n9.sort(key=lambda f: int(f[4][1:]) if f[4] != "-" else 999)
for f in n9:
    print("%s\tpasos=%2d\tfecha=%s\t%s" % (f[4], f[3], f[5], f[2]))
print("cap_09: candidatos=%d  pasos=%d" % (len(n9), sum(f[3] for f in n9)))
