# ACTA 64: las lineas nuevas de la bitacora (desde la 741) contra lo adjudicado en la ACTA 63.
# Veredictos: .v64ext/veredictos_listos.txt y, para detectar, .v63ext/cmd_02_detectar.sh.
# Aristas por lectura: .v64ext/aristas_lectura.txt (solo se cuentan, el texto lo compara la razon).
import json, re, sys
sys.stdout.reconfigure(encoding="utf-8")
listos = {}
cand = None
for l in open(".v64ext/veredictos_listos.txt", encoding="utf-8"):
    l = l.rstrip("\n")
    if l.startswith("## "):
        cand = l[3:].strip(); continue
    if not l.strip() or l.startswith("#"):
        continue
    listos[(cand, l.split("|")[0].strip())] = l
det = "detectar_arreglar_fallo_etapa_menor_valor"
for m in re.finditer(r'--veredicto "([^"]+)"', open(".v63ext/cmd_02_detectar.sh", encoding="utf-8").read()):
    listos[(det, m.group(1).split("|")[0].strip())] = m.group(1)
tanda = [l.split()[1] for l in open(".v65ext/orden.txt", encoding="utf-8") if re.match(r"^\s*\d+\s", l) and int(l.split()[0]) <= 20]
print("tanda leida de .v65ext/orden.txt, filas 1 a 20:", len(tanda))
B = [json.loads(l) for l in open("bitacora/VEREDICTOS.jsonl", encoding="utf-8")][740:]
ver = [d for d in B if "operacion" not in d]
ari = [d for d in B if "operacion" in d]
iguales = distintas = 0
vistos = set()
for d in ver:
    k = (d["candidato"], d["vecino"])
    vistos.add(k)
    l = listos.get(k)
    if l is None:
        print("SIN LINEA ADJUDICADA", k, d["veredicto"]); distintas += 1; continue
    clase = l.split("|")[1].strip().upper()
    razon_l = [x.strip() for x in l.split("|")[2:] if not re.match(r"^\w+=", x.strip())]
    ok = clase == d["veredicto"] and d["razon"].strip() == "|".join(razon_l).strip()
    if ok: iguales += 1
    else:
        distintas += 1; print("DISTINTA", k, clase, d["veredicto"]); print("  listo :", "|".join(razon_l)[:200]); print("  bitac.:", d["razon"][:200])
de_tanda = {k for k in listos if k[0] in tanda}
print("lineas nuevas en la bitacora:", len(B), "| veredictos de aduana:", len(ver), "| declaraciones de arista:", len(ari))
print("veredictos iguales a su linea adjudicada (clase y razon):", iguales, "| distintos o sin linea:", distintas)
print("lineas adjudicadas de los 20:", len(de_tanda), "| sin registro en la bitacora:", sorted(de_tanda - vistos))
print("candidatos de la bitacora fuera de la tanda:", sorted({d["candidato"] for d in B} - set(tanda)))
from collections import Counter
print("clases de los veredictos:", dict(Counter(d["veredicto"] for d in ver)), "| de las aristas:", dict(Counter(d["veredicto"] for d in ari)))
