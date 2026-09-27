# -*- coding: utf-8 -*-
"""UNA de las tres senales de la casa, la barata: familia_id (src.aduana.senal_familia_id)
de los 22 candidatos de grove contra GRAFO MAS BANDEJAS (D.38.4). Las otras dos van en
el barrido completo, que corre aparte."""
import json, os, sys, time
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
from src import aduana, comun, config as mc
t0 = time.time()
u = mc.cargar()
grafo = comun.leer_jsonl(comun.RUTA_DATASET)
bandejas = aduana.poblacion_de_bandejas()
pob = list(grafo) + list(bandejas)
print("poblacion D.38.4: grafo %d + bandejas %d = %d" % (len(grafo), len(bandejas), len(pob)))
print("umbral_familia_id: %s" % u["umbral_familia_id"])
print()
BAND = os.path.join(RAIZ, "cuarentena", "grove_high_output")
levantados = 0
for n in sorted(os.listdir(BAND)):
    if not n.endswith(".json"):
        continue
    d = json.load(open(os.path.join(BAND, n), encoding="utf-8"))
    mio = d["id"]
    altos = []
    for otro in pob:
        oid = otro.get("id")
        if oid == mio:
            continue
        val = float(aduana.senal_familia_id(mio, oid))
        if val >= u["umbral_familia_id"]:
            altos.append((val, oid))
    altos.sort(reverse=True)
    levantados += len(altos)
    print("%-48s levanta %d" % (mio, len(altos)))
    for val, oid in altos:
        print("      %.3f  %s" % (val, oid))
print()
print("familia_id levanta %d pares sobre %d candidatos, poblacion %d, en %.1f s"
      % (levantados, 22, len(pob), time.time() - t0))
