import json, pathlib, sys
sys.path.insert(0, ".")
from src import aduana, comun

base = pathlib.Path("cuarentena/grove_high_output")
TRAMO = {
 "infundir_regularidad_reunion_proceso": "P6  L21",
 "usar_tres_clases_reunion_proceso": "P7  L23",
 "fijar_frecuencia_reunion_individual_madurez_tarea": "P11 L33 a L35",
 "fijar_duracion_lugar_reunion_individual": "P12 L37 a L39",
 "preparar_guion_reunion_individual_subordinado": "P13 L41",
 "cubrir_indicadores_problemas_reunion_individual": "P14 L43",
}
PARES = [
 ("fijar_frecuencia_reunion_individual_madurez_tarea", "infundir_regularidad_reunion_proceso"),
 ("fijar_duracion_lugar_reunion_individual", "fijar_frecuencia_reunion_individual_madurez_tarea"),
 ("preparar_guion_reunion_individual_subordinado", "fijar_duracion_lugar_reunion_individual"),
 ("preparar_guion_reunion_individual_subordinado", "fijar_frecuencia_reunion_individual_madurez_tarea"),
 ("preparar_guion_reunion_individual_subordinado", "infundir_regularidad_reunion_proceso"),
 ("cubrir_indicadores_problemas_reunion_individual", "preparar_guion_reunion_individual_subordinado"),
 ("cubrir_indicadores_problemas_reunion_individual", "fijar_duracion_lugar_reunion_individual"),
 ("cubrir_indicadores_problemas_reunion_individual", "infundir_regularidad_reunion_proceso"),
 ("cubrir_indicadores_problemas_reunion_individual", "fijar_frecuencia_reunion_individual_madurez_tarea"),
]
cargar = lambda i: json.loads((base / ("%s.json" % i)).read_text(encoding="utf-8"))
senal = lambda x, y: aduana.senal_similitud_texto(comun.texto_comparable(x), comun.texto_comparable(y))
sin_resumen = lambda d: dict(d, resumen_teorico="")

print("  LOS 9 PARES DE LA COLA, MEDIDOS UNO A UNO. Los dos extremos de cada par son de ESTA MISMA TANDA.")
print()
print("  %-38s %-38s %6s %6s %6s %6s" % ("candidato", "vecino", "sen1", "sin_rt", "pasos", "lineas"))
print("  %s" % ("-" * 104))
altos = 0
for a_id, b_id in PARES:
    a, b = cargar(a_id), cargar(b_id)
    s_todo = senal(a, b)
    s_sin = senal(sin_resumen(a), sin_resumen(b))
    comunes = len(set(a["pasos_accionables"]) & set(b["pasos_accionables"]))
    if s_todo >= 0.40:
        altos += 1
    print("  %-38s %-38s %6.3f %6.3f %6d %6d"
          % (a_id[:38], b_id[:38], s_todo, s_sin, comunes, 0))
print()
print("  pares medidos                                   : %d" % len(PARES))
print("  pares POR ENCIMA de 0,40 tal como la aduana mide: %d" % altos)
print("  pares POR ENCIMA de 0,40 sin el resumen_teorico : %d"
      % sum(1 for a, b in PARES if senal(sin_resumen(cargar(a)), sin_resumen(cargar(b))) >= 0.40))
print("  PASOS literalmente comunes en los 9 pares       : %d"
      % sum(len(set(cargar(a)["pasos_accionables"]) & set(cargar(b)["pasos_accionables"])) for a, b in PARES))
print("  LINEAS del libro compartidas en los 9 pares     : 0   (los seis tramos son disjuntos por LL.4.b)")
print()
print("  TRAMO DE CADA UNO, para que se vea que son disjuntos:")
for i, t in TRAMO.items():
    print("    %-50s %s" % (i, t))
