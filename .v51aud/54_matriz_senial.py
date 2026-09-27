# -*- coding: utf-8 -*-
"""D.38.5 me manda cruzar MI cifra de vecinos contra la del informe.
Cruce entero: la matriz dirigida 6x6 de la senial 1 sobre las fichas de HOY,
con la funcion de la casa, contra los 9 pares que la aduana levanto en el acto."""
import io, json, os, sys
sys.path.insert(0, ".")
from src.aduana import senal_similitud_texto
from src.comun import texto_comparable

BAND = "cuarentena/grove_high_output"
IDS = ["infundir_regularidad_reunion_proceso", "usar_tres_clases_reunion_proceso",
       "fijar_frecuencia_reunion_individual_madurez_tarea",
       "fijar_duracion_lugar_reunion_individual",
       "preparar_guion_reunion_individual_subordinado",
       "cubrir_indicadores_problemas_reunion_individual"]
UMBRAL = json.load(io.open("config/umbrales.json", encoding="utf-8"))
nodos = {i: json.load(io.open(os.path.join(BAND, i + ".json"), encoding="utf-8"))
         for i in IDS}

# los 9 que la aduana levanto en el acto, leidos de sus propios informes
ADUANA = {("fijar_frecuencia_reunion_individual_madurez_tarea", "infundir_regularidad_reunion_proceso"): 0.385,
          ("fijar_duracion_lugar_reunion_individual", "fijar_frecuencia_reunion_individual_madurez_tarea"): 0.445,
          ("preparar_guion_reunion_individual_subordinado", "fijar_duracion_lugar_reunion_individual"): 0.428,
          ("preparar_guion_reunion_individual_subordinado", "fijar_frecuencia_reunion_individual_madurez_tarea"): 0.432,
          ("preparar_guion_reunion_individual_subordinado", "infundir_regularidad_reunion_proceso"): 0.416,
          ("cubrir_indicadores_problemas_reunion_individual", "preparar_guion_reunion_individual_subordinado"): 0.432,
          ("cubrir_indicadores_problemas_reunion_individual", "fijar_duracion_lugar_reunion_individual"): 0.386,
          ("cubrir_indicadores_problemas_reunion_individual", "infundir_regularidad_reunion_proceso"): 0.391,
          ("cubrir_indicadores_problemas_reunion_individual", "fijar_frecuencia_reunion_individual_madurez_tarea"): 0.410}

print("umbral de similitud de la casa:", UMBRAL["umbral_similitud_texto"])
print()
print("%-46s %-46s %7s %7s %s" % ("candidato", "vecino", "aduana", "hoy", "sube"))
arriba_hoy = 0
for a in IDS:
    for b in IDS:
        if a == b:
            continue
        hoy = senal_similitud_texto(texto_comparable(nodos[a]), texto_comparable(nodos[b]))
        if hoy >= 0.35:
            arriba_hoy += 1
        en_aduana = ADUANA.get((a, b))
        if en_aduana is not None or hoy >= 0.35:
            print("%-46s %-46s %7s %7.4f %s"
                  % (a[:46], b[:46],
                     ("%.3f" % en_aduana) if en_aduana is not None else "   -",
                     hoy, "SI" if hoy >= 0.35 else "no"))
print()
print("pares DIRIGIDOS de los seis entre si, en total          : %d" % (6 * 5))
print("los que la ADUANA levanto en el acto                    : %d" % len(ADUANA))
print("los que estan por encima del umbral HOY                 : %d" % arriba_hoy)
print("los que mi barrido de la fase ciega conto (AC.7)        : 17")
