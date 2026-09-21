# -*- coding: utf-8 -*-
"""EL TRAMO DE cap_09 INSERTADO. La cuenta de pasos y el id se leen del fichero
archivado en _insertados; las columnas de nodos, vecinos y veredictos son la
salida de las cinco corridas de `forja.py insertar` de esta vuelta."""
import json

ORDEN = [
    ("entregar_evaluacion_formal_desempenio_nueve_consejos", "L331", 298, 0, "sin cola"),
    ("impedir_punialadas_espalda_equipo",                    "L363", 299, 0, "sin cola"),
    ("fomentar_guia_reciproca_companieros",                  "L369", 300, 0, "sin cola"),
    ("conducir_reuniones_salto_nivel_diez_reglas",           "L383", 301, 1,
     "1 CONTINUA, arista EN COLA"),
    ("resolver_dudas_frecuentes_reuniones_salto_nivel",      "L415", 302, 2,
     "1 CONTINUA (cablea) y 1 SANO"),
]
RUTA = "cuarentena/_insertados/scott_radical_candor/%s.json"


def pasos(nid):
    return len(json.load(open(RUTA % nid, encoding="utf-8"))["pasos_accionables"])


print("| # | candidato | linea | pasos | nodos tras entrar | vecinos | veredictos |")
print("|---:|---|---:|---:|---:|---:|---|")
for i, (nid, linea, nodos, vec, ver) in enumerate(ORDEN, 1):
    print("| %d | `%s` | %s | %d | **%d** | %d | %s |"
          % (i, nid, linea, pasos(nid), nodos, vec, ver))
print("| | **TOTAL del tramo** | | **%d** | | **%d** | **3 escritos** |"
      % (sum(pasos(n) for n, _, _, _, _ in ORDEN),
         sum(v for _, _, _, v, _ in ORDEN)))
