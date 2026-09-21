# -*- coding: utf-8 -*-
"""El coste de la corrida en curso, leido del loop.log (D.56)."""
import re, io
L = io.open("docs/loop/loop.log", encoding="utf-8").read().split("\n")
k = max(i for i, l in enumerate(L) if "arranque: rama" in l)
print("arranque:", L[k])
tot = ext = aud = 0.0; n = 0
for l in L[k:]:
    m = re.search(r"(extractor|auditor) listo \(USD ([0-9.]+)\), (\d+)s", l)
    if m:
        c = float(m.group(2)); tot += c; n += 1
        if m.group(1) == "extractor": ext += c
        else: aud += c
        print("  %-9s %8.4f USD  %5s s" % (m.group(1), c, m.group(3)))
print("  turnos: %d | TOTAL %.4f USD | extractor %.4f | auditor %.4f | media %.4f"
      % (n, tot, ext, aud, tot / n))
