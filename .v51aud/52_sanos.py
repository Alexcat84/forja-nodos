# -*- coding: utf-8 -*-
import io, json, os, re
BAND = "cuarentena/grove_high_output"
FICHAS = ["infundir_regularidad_reunion_proceso", "usar_tres_clases_reunion_proceso",
          "fijar_frecuencia_reunion_individual_madurez_tarea",
          "fijar_duracion_lugar_reunion_individual",
          "preparar_guion_reunion_individual_subordinado",
          "cubrir_indicadores_problemas_reunion_individual"]
PAT = re.compile(r"VEREDICTO (SANO|CONTINUA|REPITE|MUTUO) sobre el vecino ([a-z0-9_]+),"
                 r"[^:]*?(\d,\d{3})?: ?([A-Za-z ]+)\. RAZON: (.{0,60})")
n = 0
for fid in FICHAS:
    rt = json.load(io.open(os.path.join(BAND, fid + ".json"), encoding="utf-8"))["resumen_teorico"]
    for m in PAT.finditer(rt):
        n += 1
        print("%-46s %-6s %-46s razon: %s..."
              % (fid[:46], m.group(1), m.group(2)[:46], m.group(5)[:50]))
print()
print("veredictos escritos dentro de las seis fichas : %d" % n)
print("SANO                                          : %d"
      % sum(1 for f in FICHAS
            for m in PAT.finditer(json.load(io.open(os.path.join(BAND, f + ".json"),
                                                    encoding="utf-8"))["resumen_teorico"])
            if m.group(1) == "SANO"))
print("con RAZON escrita detras                      : %d" % n)
