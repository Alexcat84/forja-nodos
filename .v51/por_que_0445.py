import json, pathlib, sys
sys.path.insert(0, ".")
from src import aduana, comun
base = pathlib.Path("cuarentena/grove_high_output")
a = json.loads((base / "fijar_duracion_lugar_reunion_individual.json").read_text(encoding="utf-8"))
b = json.loads((base / "fijar_frecuencia_reunion_individual_madurez_tarea.json").read_text(encoding="utf-8"))

def senal(x, y):
    return aduana.senal_similitud_texto(comun.texto_comparable(x), comun.texto_comparable(y))

print("  PAR                                  : %s  contra  %s" % (a["id"], b["id"]))
print("  senial 1 TAL COMO LA ADUANA LA MIDE  : %.3f   (umbral 0,35; banda alta desde 0,40)" % senal(a, b))
sin = lambda d: dict(d, resumen_teorico="")
print("  senial 1 SIN el resumen_teorico      : %.3f" % senal(sin(a), sin(b)))
solo = lambda d: {"id": d["id"], "titulo": "", "resumen_teorico": "", "pasos_accionables": d["pasos_accionables"],
                  "condiciones_activacion": "", "entregable_esperado": "", "denominaciones": {}}
print("  senial 1 SOLO con los pasos          : %.3f" % senal(solo(a), solo(b)))
print()
print("  caracteres de resumen_teorico        : %d y %d" % (len(a["resumen_teorico"]), len(b["resumen_teorico"])))
print("  caracteres de los pasos              : %d y %d" % (sum(map(len, a["pasos_accionables"])), sum(map(len, b["pasos_accionables"]))))
print("  el resumen es el  %.0f y el %.0f por ciento del texto que la senial 1 compara"
      % (100.0*len(a["resumen_teorico"])/len(comun.texto_comparable(a)),
         100.0*len(b["resumen_teorico"])/len(comun.texto_comparable(b))))
print()
print("  PASOS LITERALMENTE COMUNES A LOS DOS : %d" % len(set(a["pasos_accionables"]) & set(b["pasos_accionables"])))
print("  LINEAS DEL LIBRO QUE COMPARTEN       : 0   (candidato L37 y L39, vecino L33 y L35)")
