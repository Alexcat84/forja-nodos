# ACTA 64, D65.1: los 20 insertar de la vuelta 65, en fila y sin solaparse. Lee inicio y fin de cada .v65ext/insertar_NN_*.txt
import glob, re, sys, datetime as dt
sys.stdout.reconfigure(encoding="utf-8")
F = lambda s: dt.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
prev = None; solapes = 0; n = 0
for p in sorted(glob.glob(".v65ext/insertar_[0-9][0-9]_*.txt")):
    t = open(p, encoding="utf-8").read()
    i = F(re.search(r"^inicio (\S+ \S+)", t, re.M).group(1)); f = F(re.search(r"^fin (\S+ \S+) \| codigo de salida (\d+)", t, re.M).group(1))
    rc = re.search(r"codigo de salida (\d+)", t).group(1); n += 1
    hueco = (i - prev).total_seconds() if prev else None
    if prev and i < prev: solapes += 1
    print("%s inicio %s fin %s rc %s | desde el fin anterior %s s" % (p.split("insertar_")[1][:2], i.time(), f.time(), rc, hueco))
    prev = f
print("insertar:", n, "| que arrancan antes de que acabe el anterior:", solapes)
