# -*- coding: utf-8 -*-
"""Mide la eleccion del candidato de la TAREA 4 por los dos alcances."""
import json, glob, os, re
cap = {}
for p in sorted(glob.glob("cuarentena/grove_high_output/*.json")):
    d = json.load(open(p, encoding="utf-8"))
    m = re.search(r"UNIDAD DE ORIGEN:\s*fuentes/grove_high_output/(cap_\d{2})\.md",
                  d.get("resumen_teorico", "") or "")
    cap[os.path.basename(p)[:-5]] = m.group(1) if m else "?"
def car(fn):
    return set(x.strip() for x in open(fn, encoding="utf-8") if x.strip())
print("LA ELECCION DE LA TAREA 4, MEDIDA POR LOS DOS ALCANCES\n")
for etq, fn in (("alcance del reporte (.v55 a .v62 + REPORTE.md + ACTA_AUDITOR.md)",
                 ".v62aud2/con_informe_v55_v62.txt"),
                ("alcance de la LINEA ENTERA (todas las .vNN* de este arbol)",
                 ".v62aud2/con_informe_pre62.txt")):
    con = car(fn)
    c2 = sorted(k for k, c in cap.items() if c == "cap_02" and k not in con)
    prim = sorted(set(cap[k] for k in cap if k not in con))
    print(etq)
    print("   candidatos de la bandeja CON salida guardada : %d de 91" % len([k for k in cap if k in con]))
    print("   capitulo mas temprano con alguno sin medir   : %s" % (prim[0] if prim else "NINGUNO"))
    print("   de cap_02, sin medir                         : %d  %s" % (len(c2), c2))
    print()
print("el elegido: detectar_arreglar_fallo_etapa_menor_valor, cap_02")
print("   ya tenia salida guardada en .v54/d024_detectar_arreglar_fallo_etapa_menor_valor.txt")
