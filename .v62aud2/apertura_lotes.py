# -*- coding: utf-8 -*-
"""D.32: las dos condiciones de apertura de cada lote que podria seguir."""
import glob, io
canon = io.open("fuentes/FUENTES_CANONICAS.json", encoding="utf-8").read()
for k in ("gerber_emyth", "marquet_turn_the_ship", "bernerslee_bananas",
          "openstax_business_ethics", "openstax_org_behavior"):
    n = len(glob.glob("fuentes/%s/*.md" % k))
    print("%-26s: material en fuentes/%s/ = %d fichero(s) .md | clave en la tabla canonica = %s"
          % (k, k, n, "SI" if ('"%s"' % k) in canon else "NO"))
