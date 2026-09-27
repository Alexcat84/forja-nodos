# Fase ciega de la 66: vuelca los 22 de cap_04 de la bandeja (pasos numerados y el tramo DE DONDE SALE de su
# resumen_teorico) para leerlos contra fuentes/grove_high_output/cap_04.md. Solo lee.
import json, re, sys
sys.stdout.reconfigure(encoding="utf-8")
ids = [l.strip() for l in open(".v66aud/los22_cap04.txt", encoding="utf-8") if l.strip()]
tot = 0
for n, i in enumerate(ids, 1):
    d = json.load(open("cuarentena/grove_high_output/%s.json" % i, encoding="utf-8"))
    r = d.get("resumen_teorico", "")
    m = re.search(r"PIEZA (P\d+)[^.]*?(L\d+(?: a L\d+)?)", r)
    ps = d.get("pasos_accionables", [])
    tot += len(ps)
    print("=" * 100)
    print("%d. %s | %s | pasos %d" % (n, i, m.group(1) + " " + m.group(2) if m else "?", len(ps)))
    print("TITULO:", d.get("titulo"))
    print("ACTIVA:", d.get("condiciones_activacion"))
    for k, p in enumerate(ps, 1):
        print("  %d. %s" % (k, p))
    s = re.search(r"DE DONDE SALE(.*?)(RELECTURA DE FIDELIDAD|LO QUE NO ESCRIBO|$)", r, re.S)
    print("ORIGEN:", s.group(1).strip()[:3000] if s else "(sin tramo DE DONDE SALE)")
print("=" * 100)
print("fichas %d | pasos %d" % (len(ids), tot))
