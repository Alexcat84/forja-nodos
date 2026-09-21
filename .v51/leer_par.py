import json, pathlib, sys
base = pathlib.Path("cuarentena/grove_high_output")
a = json.loads((base / (sys.argv[1] + ".json")).read_text(encoding="utf-8"))
b = json.loads((base / (sys.argv[2] + ".json")).read_text(encoding="utf-8"))
for d, rol in ((a, "CANDIDATO"), (b, "VECINO")):
    print()
    print("    [%s] %s" % (rol, d["id"]))
    print("      ENTREGABLE : %s" % d["entregable_esperado"])
    for i, p in enumerate(d["pasos_accionables"], 1):
        print("       %2d. %s" % (i, p))
print()
print("    PASOS LITERALMENTE COMUNES A LOS DOS : %d"
      % len(set(a["pasos_accionables"]) & set(b["pasos_accionables"])))
