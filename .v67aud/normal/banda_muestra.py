# ACTA 66: la muestra pineada de los SANO de la 67 (semilla 67, .v67aud/normal/muestra_sano.py), su tasa y su banda de Wilson al 95.
# Y D.8: ningun SANO de la vuelta sin razon escrita.
import json, math
L = [json.loads(l) for l in open("bitacora/VEREDICTOS.jsonl", encoding="utf-8")][796:]
sano = [d for d in L if d.get("veredicto") == "SANO"]
print("SANO de la vuelta: %d | sin razon escrita: %d" % (len(sano), sum(1 for d in sano if not d.get("razon", "").strip())))
n, caen, z = 17, 0, 1.96
p = caen / n; c = (p + z * z / (2 * n)) / (1 + z * z / n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
print("releidos %d | se sostienen %d | caen %d | tasa %.1f por ciento | banda Wilson 95: %.1f a %.1f por ciento" % (n, n - caen, caen, 100 * p, 100 * max(0, c - h), 100 * (c + h)))
