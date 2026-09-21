RELOJES = [("P6", "infundir_regularidad_reunion_proceso", None, 0, 394),
           ("P7", "usar_tres_clases_reunion_proceso", 253.2, 0, 395),
           ("P11", "fijar_frecuencia_reunion_individual_madurez_tarea", 374.4, 1, 396),
           ("P12", "fijar_duracion_lugar_reunion_individual", 339.8, 1, 397),
           ("P13", "preparar_guion_reunion_individual_subordinado", 317.1, 3, 398),
           ("P14", "cubrir_indicadores_problemas_reunion_individual", 350.7, 4, 399)]
print("    %-5s %-50s %10s %8s %10s" % ("pieza", "id", "reloj s", "vecinos", "poblacion"))
med = [r for _, _, r, _, _ in RELOJES if r is not None]
for pieza, i, r, v, p in RELOJES:
    print("    %-5s %-50s %10s %8d %10d" % (pieza, i, ("%.1f" % r).replace(".", ",") if r is not None else "NO MEDIDO", v, p))
suma = sum(med)
print()
print("    pasadas de aduana corridas            : %d" % len(RELOJES))
print("    pasadas CON reloj                     : %d" % len(med))
print("    suma de los relojes medidos           : %s s" % ("%.1f" % suma).replace(".", ","))
print("    MEDIA POR PASADA, sobre %d y no sobre %d: %s s"
      % (len(med), len(RELOJES), ("%.1f" % (suma / len(med))).replace(".", ",")))
print("    media de la vuelta 50, como contraste : 461,3 s   (sobre 3 pasadas)")
print("    variacion                             : %s por ciento"
      % ("%+.1f" % (100.0 * (suma / len(med) - 461.3) / 461.3)).replace(".", ","))
print("    vecinos por pasada                    : menor 0, mayor 4, suma 9")
