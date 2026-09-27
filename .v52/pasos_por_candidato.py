import json, pathlib, re
base = pathlib.Path("cuarentena/grove_high_output")
orden = [("P15", "facilitar_expresion_subordinado_pregunta_mas"),
         ("P16", "tomar_notas_copia_guion_reunion_individual"),
         ("P17", "acumular_asuntos_importantes_fichero_espera"),
         ("P18", "alentar_asuntos_corazon_vigilar_final_reunion"),
         ("P19", "conducir_reunion_individual_telefono_distancia"),
         ("P20", "programar_reunion_individual_cadena")]
TENT = re.compile(r"SITIO DE TENTACION|ESTUVE A PUNTO DE ESCRIBIR UN PUENTE")
tot = tent = 0
print("    %-5s %-48s %6s %14s %7s %11s" % ("pieza", "id", "pasos", "TRANSCRIPCION", "PUENTE", "tentaciones"))
for pieza, i in orden:
    d = json.loads((base / ("%s.json" % i)).read_text(encoding="utf-8"))
    n = len(d["pasos_accionables"])
    t = len(TENT.findall(d["resumen_teorico"]))
    tot += n; tent += t
    print("    %-5s %-48s %6d %14d %7d %11d" % (pieza, i[:48], n, n, 0, t))
print("    %-5s %-48s %6d %14d %7d %11d" % ("", "TOTAL DE LA TANDA", tot, tot, 0, tent))
