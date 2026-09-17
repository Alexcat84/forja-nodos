# contar.py: cuenta pasos por candidato de una bandeja. Sin listas tecleadas dentro:
# la bandeja se lee del disco y el nombre de campo es el del esquema.
import json, sys, pathlib
b = pathlib.Path(sys.argv[1])
total = 0
for f in sorted(b.glob("*.json")):
    d = json.loads(f.read_text(encoding="utf-8"))
    n = len(d["pasos_accionables"])
    total += n
    print("%-45s %3d" % (d["id"], n))
print("%-45s %3d" % ("TOTAL", total))
print("%-45s %3d" % ("CANDIDATOS", len(list(b.glob("*.json")))))
