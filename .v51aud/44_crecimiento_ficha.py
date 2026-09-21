# -*- coding: utf-8 -*-
"""Que parte del resumen_teorico de las dos fichas del par 0,445 es POSTERIOR
a la pasada de aduana, medido por sus propios marcadores de bloque."""
import io, json, re
for fid in ("fijar_duracion_lugar_reunion_individual",
            "fijar_frecuencia_reunion_individual_madurez_tarea"):
    d = json.load(io.open("cuarentena/grove_high_output/%s.json" % fid,
                          encoding="utf-8"))
    rt = d["resumen_teorico"]
    print("%s" % fid)
    print("   caracteres de resumen_teorico hoy : %d" % len(rt))
    for marca in ("VEREDICTO", "ARISTA", "CORRECCION DECLARADA", "COLA DE LECTURA",
                  "similitud de texto"):
        pos = rt.find(marca)
        print("      primer '%-22s' en el caracter %s" % (marca, pos))
    corte = min([p for p in (rt.find("VEREDICTO"),) if p >= 0] or [-1])
    if corte > 0:
        print("   texto ANTES del primer bloque VEREDICTO : %d caracteres" % corte)
        print("   texto DESPUES                           : %d caracteres" % (len(rt) - corte))
    print()
