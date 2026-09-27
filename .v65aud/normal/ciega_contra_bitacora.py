# ACTA 64: mis 17 filas leidas en la fase ciega (.v65aud/clases_48.txt, las CIEGA) contra la clase que la
# vuelta 65 escribio en la bitacora para ese par y sentido. Solo clases: la razon se destapa despues, aparte.
import json, sys
sys.stdout.reconfigure(encoding="utf-8")
B = {}
for d in [json.loads(l) for l in open("bitacora/VEREDICTOS.jsonl", encoding="utf-8")][740:]:
    if "operacion" not in d:
        B[(d["candidato"], d["vecino"])] = d["veredicto"]
n = igual = 0
for l in open(".v65aud/clases_48.txt", encoding="utf-8"):
    c = l.split()
    if len(c) < 6 or c[0] != "CIEGA": continue
    a, b = c[3], c[5]; mia = c[1]; conf = c[2]; n += 1
    suya = B.get((a, b), "SIN LINEA")
    igual += mia == suya
    print("%-8s mia %-5s (%s) bitacora %-9s %s -> %s" % ("COINCIDE" if mia == suya else "DISCREPA", mia, conf, suya, a, b))
print("filas ciegas: %d | coinciden con la bitacora: %d | discrepan: %d" % (n, igual, n - igual))
