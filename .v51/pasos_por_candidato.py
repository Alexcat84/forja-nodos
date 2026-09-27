import json, pathlib
base = pathlib.Path("cuarentena/grove_high_output")
orden = [("P6", "infundir_regularidad_reunion_proceso"), ("P7", "usar_tres_clases_reunion_proceso"),
         ("P11", "fijar_frecuencia_reunion_individual_madurez_tarea"), ("P12", "fijar_duracion_lugar_reunion_individual"),
         ("P13", "preparar_guion_reunion_individual_subordinado"), ("P14", "cubrir_indicadores_problemas_reunion_individual")]
tot = 0
print("    %-5s %-50s %6s %14s %7s" % ("pieza", "id", "pasos", "TRANSCRIPCION", "PUENTE"))
for pieza, i in orden:
    d = json.loads((base / ("%s.json" % i)).read_text(encoding="utf-8"))
    n = len(d["pasos_accionables"]); tot += n
    print("    %-5s %-50s %6d %14d %7d" % (pieza, i, n, n, 0))
print("    %-5s %-50s %6d %14d %7d" % ("", "TOTAL DE LA TANDA", tot, tot, 0))
