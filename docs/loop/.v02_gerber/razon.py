# razon.py: destapa el resumen_teorico de UN candidato, uno por vez (REMEDIO 2).
# Sin listas tecleadas: el id llega por argumento y el fichero se busca en la bandeja.
import json, sys, pathlib
b, cual = pathlib.Path(sys.argv[1]), sys.argv[2]
d = json.loads((b / (cual + ".json")).read_text(encoding="utf-8"))
print(d["resumen_teorico"])
