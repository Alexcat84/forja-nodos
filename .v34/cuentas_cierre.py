# -*- coding: utf-8 -*-
"""La tabla de apertura contra cierre, RECOMPUTADA AL CIERRE (EXTRACTOR.md 4)."""
import io, re
def leer(ruta):
    d = {}
    for l in io.open(ruta, encoding="utf-8"):
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) == 3 and not c[0].startswith("-") and c[0] != "pieza":
            d[c[0]] = c[1].replace("*", "").replace("`", "")
    return d
a, c = leer(".v34/apertura_tabla.txt"), leer(".v34/cierre_tabla.txt")
print("| pieza | al abrir | **al cerrar** | delta |")
print("|---|---:|---:|---:|")
for k in a:
    if k.startswith(("rama", "commit")):
        continue
    va, vc = a[k], c.get(k, "")
    try:
        na, nc = float(va.replace(",", ".")), float(vc.replace(",", "."))
        d = nc - na
        ds = ("%+.1f" % d).replace(".", ",") if "," in va or "," in vc else "%+d" % int(d)
        if d == 0:
            ds = "0"
    except ValueError:
        ds = "."
    print("| %s | %s | **%s** | %s |" % (k, va, vc, ds if ds == "0" else "**%s**" % ds))
