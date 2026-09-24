# ACTA 64: las 7 declaraciones de arista de la vuelta 65 en la bitacora contra su fila SOSTENGO de .v64ext/aristas_lectura.txt
import json, sys
sys.stdout.reconfigure(encoding="utf-8")
filas = {}
for n, l in enumerate(open(".v64ext/aristas_lectura.txt", encoding="utf-8"), 1):
    c = [x.strip() for x in l.rstrip("\n").split(" | ")]
    if len(c) >= 6 and c[0] == "SOSTENGO":
        filas[(c[1], c[2])] = (n, c[5], c[3])
B = [json.loads(l) for l in open("bitacora/VEREDICTOS.jsonl", encoding="utf-8")][740:]
ari = [d for d in B if "operacion" in d]
ig = 0
for d in ari:
    k = (d["vecino"], d["candidato"])
    f = filas.get(k)
    same = f is not None and f[1] == d["razon"].strip() and ("linea %d " % f[0]) in d["cita_del_veredicto"]
    ig += same
    print("IGUAL   " if same else "DISTINTA", "%-48s > %-48s paso %-2s | fila %s | tramo de la fila: %s" % (k[0], k[1], d["paso_citado"], f[0] if f else "-", f[2] if f else "-"))
print("filas SOSTENGO:", len(filas), "| declaraciones de arista:", len(ari), "| iguales a su fila (razon y linea citada):", ig)
print("SOSTENGO sin declaracion:", sorted(k for k in filas if k not in {(d["vecino"], d["candidato"]) for d in ari}))
