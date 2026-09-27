# -*- coding: utf-8 -*-
"""EL RELOJ DE ADUANA DE LA VUELTA 53, PASADA A PASADA, CONTRA EL TECHO DE 90 MINUTOS.

Cada cifra se lee de su fichero .v53/reloj_cN.txt, que es el que el propio comando escribio al
terminar. NINGUNA SE TECLEA AQUI. La pasada perdida no tiene fichero porque el comando se corto
antes de escribirlo, y por eso es la unica que va con su segundero puesto a mano y declarada
como tal en su fila.
"""
import io
import os
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

TECHO_MIN = 90.0
MEDIA_V52 = 731.2

PASADAS = [
    ("c0", "conducir_etapas_modelo_ideal_decision", None, "PERDIDA: cortada a los 600 s sin informe"),
    ("c1", "conducir_etapas_modelo_ideal_decision", ".v53/reloj_c1.txt", "ENTRARIA, 0 vecinos"),
    ("c2", "decidir_nivel_competente_mas_bajo", None, "CAERIA por la regla 3 de id, 0 s medidos"),
    ("c2b", "decidir_nivel_competente_inferior", ".v53/reloj_c2b.txt", "ENTRARIA, 0 vecinos"),
    ("c3", "vencer_sindrome_grupo_pares_autoconfianza", ".v53/reloj_c3.txt", "BLOQUEARIA, 4 vecinos"),
    ("c4", "tomar_mando_reunion_pares_presidente_ausente", ".v53/reloj_c4.txt", "BLOQUEARIA, 3 vecinos"),
    ("c5", "ejercer_poder_posicion_etapa_decision_clara", ".v53/reloj_c5.txt", "ENTRARIA, 0 vecinos"),
    ("c6", "cortar_discusion_libre_momento_justo", ".v53/reloj_c6.txt", "BLOQUEARIA, 3 vecinos"),
    ("c7", "zanjar_seis_preguntas_decision_adelantado", ".v53/reloj_c7.txt", "ENTRARIA, 0 vecinos"),
    ("c8", "anunciar_decision_inesperada_reconvocar_reunion", ".v53/reloj_c8.txt", "BLOQUEARIA, 6 vecinos"),
    ("c9", "planificar_tres_pasos_demanda_estado_brecha", ".v53/reloj_c9.txt", "BLOQUEARIA, 1 vecino"),
]
PERDIDA = 600.0          # el tope del corte, no una medicion del comando
CAIDA = 0.0


def leido(ruta):
    crudo = io.open(ruta, encoding="utf-8").read()
    return float(re.search(r"RELOJ:\s*([0-9.]+)\s*s", crudo).group(1))


print("    %-4s %-48s %10s  %s" % ("pase", "candidato", "reloj s", "de donde sale la cifra"))
suma = 0.0
medidas = 0
for nombre, ident, ruta, nota in PASADAS:
    if ruta and os.path.exists(ruta):
        segundos = leido(ruta)
        sede = ruta
        medidas += 1
    elif nombre == "c0":
        segundos = PERDIDA
        sede = "tope del corte, no hay fichero: el comando no llego a escribirlo"
    else:
        segundos = CAIDA
        sede = "la puerta tumba antes del barrido, sin fichero de reloj"
    suma += segundos
    print("    %-4s %-48s %10s  %s" % (nombre, ident[:48],
                                       ("%.1f" % segundos).replace(".", ","), sede))
print("")
print("    pasadas de aduana lanzadas             : %d" % len(PASADAS))
print("    pasadas CON fichero de reloj           : %d" % medidas)
print("    suma del reloj de aduana               : %s s" % ("%.1f" % suma).replace(".", ","))
print("    en minutos                             : %s min" % ("%.1f" % (suma / 60.0)).replace(".", ","))
print("    TECHO DEL ENCARGO                      : %.0f min" % TECHO_MIN)
print("    consumido del techo                    : %s por ciento"
      % ("%.1f" % (100.0 * suma / (TECHO_MIN * 60.0))).replace(".", ","))
print("    margen que quedaba al cortar           : %s min"
      % ("%.1f" % (TECHO_MIN - suma / 60.0)).replace(".", ","))
print("    media por pasada CON reloj             : %s s"
      % ("%.1f" % (suma / medidas)).replace(".", ","))
print("    media de la vuelta 52, como contraste  : %s s   (la que el encargo usa para presupuestar)"
      % ("%.1f" % MEDIA_V52).replace(".", ","))
print("    variacion                              : %s por ciento"
      % ("%+.1f" % (100.0 * (suma / medidas - MEDIA_V52) / MEDIA_V52)).replace(".", ","))
print("")
print("    LO QUE EL PRESUPUESTO DEL ENCARGO PREDECIA : 7,4 candidatos en 90 min a 731,2 s")
print("    LO QUE SALIO                               : %d candidatos escritos en %s min"
      % (9, ("%.1f" % (suma / 60.0)).replace(".", ",")))
