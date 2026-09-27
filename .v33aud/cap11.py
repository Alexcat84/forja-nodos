# LOS PASOS DE cap_11 QUE VIVEN EN EL GRAFO, contados del dato y no de una nota vieja.
import io, json, re
nodos = [json.loads(l) for l in io.open("dataset/nodos.jsonl", encoding="utf-8") if l.strip()]
c11 = []
for n in nodos:
    m = re.search(r"UNIDAD DE ORIGEN:\s*(\S+)", n.get("resumen_teorico") or "")
    if m and "cap_11" in m.group(1):
        c11.append((n["id"], len(n.get("pasos_accionables") or [])))
print("nodos del GRAFO con unidad de origen cap_11 : %d" % len(c11))
print("sus pasos                                   : %d" % sum(p for _, p in c11))
v31 = set(io.open(".v31/orden_cap11.txt", encoding="utf-8").read().split())
print()
print("los que .v31/orden_cap11.txt NO cuenta en sus 14:")
for i, p in sorted(c11):
    if ("`%s`" % i) not in v31:
        print("   %-50s %2d pasos" % (i, p))
