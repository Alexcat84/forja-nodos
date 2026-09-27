# -*- coding: utf-8 -*-
"""El tallado sobre el REPORTE y la APERTURA tal como estaban en 3061fc2,
para comprobar el 234 / 129 / 105 que MM.4.k publica como base."""
import io, os, subprocess, sys, tempfile
sys.path.insert(0, "scripts")
import tallar_reporte as T

COMMIT = "3061fc2"
tmp = tempfile.mkdtemp(prefix="tallado_base_")
os.makedirs(os.path.join(tmp, "docs", "loop"))
totales = [0, 0, 0]
for rel in ("docs/loop/REPORTE.md", "docs/loop/APERTURA_CIEGA.md"):
    crudo = subprocess.check_output(["git", "show", "%s:%s" % (COMMIT, rel)])
    destino = os.path.join(tmp, rel.replace("/", os.sep))
    io.open(destino, "wb").write(crudo)
    dictamenes = T.revisar(ruta_reporte=destino, raiz=T.RAIZ)
    talladas = [d for d in dictamenes if d.get("estado") == "TALLADA"]
    parcial = [d for d in dictamenes if d.get("estado") == "CITA"]
    difiere = [d for d in dictamenes if d.get("estado") == "DIFIERE"]
    otras = [d.get("estado") for d in dictamenes
             if d.get("estado") not in ("TALLADA", "CITA", "DIFIERE")]
    print("%-30s declaran %4d  talladas %4d  PARCIAL %4d  DIFIEREN %d  otras %s"
          % (rel, len(dictamenes), len(talladas), len(parcial), len(difiere),
             sorted(set(otras))))
    totales[0] += len(dictamenes); totales[1] += len(talladas); totales[2] += len(parcial)
    os.remove(destino)
print("%-30s declaran %4d  talladas %4d  PARCIAL %4d"
      % ("TOTAL en " + COMMIT, totales[0], totales[1], totales[2]))
