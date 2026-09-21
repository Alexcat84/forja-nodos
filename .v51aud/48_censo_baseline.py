# -*- coding: utf-8 -*-
"""El censo sobre los TRES documentos tal como estaban en el commit de apertura
de la vuelta 51 (3061fc2), para comprobar el 803 que MM.4.k publica como base."""
import io, os, subprocess, sys
sys.path.insert(0, "scripts")
import censar_rutas as C

COMMIT = "3061fc2"
copias = []
try:
    total = 0
    for doc in C.DOCUMENTOS:
        rel = doc.replace("\\", "/")
        crudo = subprocess.check_output(["git", "show", "%s:%s" % (COMMIT, rel)])
        tmp = rel + ".BASE_SOLO_MEDIDA.md"
        io.open(tmp, "wb").write(crudo)
        copias.append(tmp)
        caidas, pasan = C.censar(documentos=[tmp])
        print("%-32s censadas %4d   pasan %4d   caen %d"
              % (rel, len(caidas) + len(pasan), len(pasan), len(caidas)))
        total += len(caidas) + len(pasan)
    print("%-32s censadas %4d" % ("TOTAL en " + COMMIT, total))
finally:
    for t in copias:
        if os.path.exists(t):
            os.remove(t)
