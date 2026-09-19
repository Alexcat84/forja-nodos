RELOJES = [("P15", "facilitar_expresion_subordinado_pregunta_mas", 1045.6, 5, 400),
           ("P16", "tomar_notas_copia_guion_reunion_individual", 601.3, 4, 401),
           ("P17", "acumular_asuntos_importantes_fichero_espera", 636.2, 4, 402),
           ("P18", "alentar_asuntos_corazon_vigilar_final_reunion", 774.9, 5, 403),
           ("P19", "conducir_reunion_individual_telefono_distancia", 567.5, 6, 404),
           ("P20", "programar_reunion_individual_cadena", 761.9, 10, 405)]
print("    %-5s %-48s %10s %8s %10s" % ("pieza", "id", "reloj s", "vecinos", "poblacion"))
for pieza, i, r, v, p in RELOJES:
    print("    %-5s %-48s %10s %8d %10d" % (pieza, i[:48], ("%.1f" % r).replace(".", ","), v, p))
med = [r for _, _, r, _, _ in RELOJES]
vec = [v for _, _, _, v, _ in RELOJES]
suma = sum(med)
print()
print("    pasadas de aduana corridas            : %d" % len(RELOJES))
print("    pasadas CON reloj                     : %d   (las seis, ninguna estimada)" % len(med))
print("    suma de los relojes medidos           : %s s" % ("%.1f" % suma).replace(".", ","))
print("    MEDIA POR PASADA, sobre %d y sobre %d   : %s s"
      % (len(med), len(RELOJES), ("%.1f" % (suma / len(med))).replace(".", ",")))
print("    media de la vuelta 51, como contraste : 327,0 s   (sobre 5 pasadas de 6)")
print("    variacion                             : %s por ciento"
      % ("%+.1f" % (100.0 * (suma / len(med) - 327.0) / 327.0)).replace(".", ","))
print("    veces la media de la vuelta 51        : %s" % ("%.2f" % (suma / len(med) / 327.0)).replace(".", ","))
print("    vecinos por pasada                    : menor %d, mayor %d, suma %d" % (min(vec), max(vec), sum(vec)))
print("    poblacion del barrido                 : de %d a %d" % (RELOJES[0][4], RELOJES[-1][4]))
print("    suma de relojes en minutos            : %s min" % ("%.1f" % (suma / 60.0)).replace(".", ","))
