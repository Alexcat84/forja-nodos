# -*- coding: utf-8 -*-
"""D.8: un SANO sin razon escrita es una caida, aunque acierte.
Cuento, ficha a ficha, cuantos bloques de veredicto lleva dentro y si cada uno
nombra a su vecino y trae razon (texto detras de la clase)."""
import io, json, os, re
BAND = "cuarentena/grove_high_output"
FICHAS = ["infundir_regularidad_reunion_proceso",
          "usar_tres_clases_reunion_proceso",
          "fijar_frecuencia_reunion_individual_madurez_tarea",
          "fijar_duracion_lugar_reunion_individual",
          "preparar_guion_reunion_individual_subordinado",
          "cubrir_indicadores_problemas_reunion_individual"]
total = 0
for fid in FICHAS:
    rt = json.load(io.open(os.path.join(BAND, fid + ".json"),
                           encoding="utf-8"))["resumen_teorico"]
    bloques = re.findall(r"VEREDICTO[^.]{0,200}?(SANO|CONTINUA|REPITE|MUTUO)", rt)
    sanos = rt.count("SANO")
    # la razon: caracteres entre la palabra SANO y el siguiente VEREDICTO
    trozos = rt.split("VEREDICTO")[1:]
    con_razon = 0
    for t in trozos:
        clase = re.search(r"(SANO|CONTINUA|REPITE|MUTUO)", t)
        if not clase:
            continue
        cola = t[clase.end():]
        if len(cola.strip()) >= 80:
            con_razon += 1
    print("%-52s bloques VEREDICTO %d   con razon de 80+ caracteres detras %d"
          % (fid[:52], len(trozos), con_razon))
    total += len(trozos)
print()
print("bloques VEREDICTO en las seis fichas: %d" % total)
