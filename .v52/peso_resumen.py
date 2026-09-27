import json, sys
sys.path.insert(0, ".")
from src import comun
for i in ("fijar_duracion_lugar_reunion_individual", "fijar_frecuencia_reunion_individual_madurez_tarea"):
    d = json.load(open("cuarentena/grove_high_output/%s.json" % i, encoding="utf-8"))
    tc = len(comun.texto_comparable(d))
    print("    %-50s resumen %6d   texto comparable %6d   el resumen es el %.0f por ciento"
          % (i[:50], len(d["resumen_teorico"]), tc, 100.0 * len(d["resumen_teorico"]) / tc))
