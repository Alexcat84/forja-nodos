# -*- coding: utf-8 -*-
"""Ficha de cada candidato de cap_07 que espera en la bandeja, por orden de linea."""
import json, io, glob, re
RE_CAP = re.compile(r"fuentes/([a-z0-9_]+)/(cap_\d+)\.md")
RE_LIN = re.compile(r"l[ií]neas?\s+(\d+)\s+a\s+(\d+)")
fichas=[]
for f in sorted(glob.glob("cuarentena/scott_radical_candor/*.json")):
    d=json.load(io.open(f,encoding="utf-8"))
    r=d.get("resumen_teorico","") or ""
    mc=RE_CAP.search(r)
    if not mc or mc.group(2)!="cap_07": continue
    t=[(int(a),int(b)) for a,b in RE_LIN.findall(r)]
    fichas.append((t[0] if t else (0,0), d, r))
fichas.sort(key=lambda x:x[0])
for (a,b),d,r in fichas:
    print("="*88)
    print("%s   [L%d-%d]  %d pasos" % (d["id"], a, b, len(d["pasos_accionables"])))
    print("  TITULO    : %s" % d["titulo"])
    print("  ACTIVACION: %s" % d["condiciones_activacion"])
    print("  ENTREGABLE: %s" % d["entregable_esperado"])
    print("  ROTULO/POR QUE (primeras 2 frases del resumen):")
    for frase in r.split(". ")[:2]:
        print("     %s." % frase.strip()[:300])
