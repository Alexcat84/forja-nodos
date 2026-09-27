# -*- coding: utf-8 -*-
"""PASOS INVENTADOS POR CAPITULO, UNA FILA POR CAPITULO Y NO UNA MEDIA (D.58, TAREA 4).

La muestra la reparte scripts/muestra_fidelidad.py con la semilla v53 y NO la elijo yo. Lo
que pongo aqui es MI MARCA sobre cada paso de esa muestra, TRANSCRIPCION o PUENTE, hecha
releyendo el paso contra la linea del libro de la que sale. El instrumento solo cuenta y
publica el disparador: si un capitulo pasa del 10 por ciento, se relee ENTERO antes de seguir.

CERO CIFRAS TECLEADAS: el numero de pasos de cada candidato se cuenta del JSON, y la lista de
la muestra se lee de .v53/muestra.txt, que es la salida del instrumento que la repartio.
"""
import io
import json
import os
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

TOPE = 10.0

# MI MARCA, paso a paso. Clave: (id recortado como lo imprime la muestra, P<n>).
# Los quince de cap_06 son la muestra; los seis de cap_07 son el capitulo ENTERO.
PUENTES = set()          # ni uno: la relectura no encontro ninguno
RELEIDOS = {
    "cap_06": [("anunciar_decision_inesperada_reconvocar_reunio", 1),
               ("anunciar_decision_inesperada_reconvocar_reunio", 5),
               ("anunciar_decision_inesperada_reconvocar_reunio", 6),
               ("conducir_etapas_modelo_ideal_decision", 4),
               ("conducir_etapas_modelo_ideal_decision", 9),
               ("cortar_discusion_libre_momento_justo", 4),
               ("cortar_discusion_libre_momento_justo", 7),
               ("decidir_nivel_competente_inferior", 3),
               ("decidir_nivel_competente_inferior", 4),
               ("ejercer_poder_posicion_etapa_decision_clara", 2),
               ("ejercer_poder_posicion_etapa_decision_clara", 3),
               ("tomar_mando_reunion_pares_presidente_ausente", 3),
               ("vencer_sindrome_grupo_pares_autoconfianza", 3),
               ("vencer_sindrome_grupo_pares_autoconfianza", 4),
               ("zanjar_seis_preguntas_decision_adelantado", 3)],
    "cap_07": [("planificar_tres_pasos_demanda_estado_brecha", n) for n in range(1, 7)],
    "cap_08": [],
}
REGIMEN = {"cap_06": "MUESTRA de 15", "cap_07": "ENTERO", "cap_08": "ENTERO"}
CANDIDATOS = {
    "cap_06": ["anunciar_decision_inesperada_reconvocar_reunion",
               "conducir_etapas_modelo_ideal_decision",
               "cortar_discusion_libre_momento_justo",
               "decidir_nivel_competente_inferior",
               "ejercer_poder_posicion_etapa_decision_clara",
               "tomar_mando_reunion_pares_presidente_ausente",
               "vencer_sindrome_grupo_pares_autoconfianza",
               "zanjar_seis_preguntas_decision_adelantado"],
    "cap_07": ["planificar_tres_pasos_demanda_estado_brecha"],
    "cap_08": [],
}

# LA MUESTRA SE COTEJA CONTRA EL FICHERO QUE LA REPARTIO, no contra mi memoria.
crudo = io.open(".v53/muestra.txt", encoding="utf-8").read()
fila = re.compile(r"^    (\S+)\s+P(\d+)\s", re.M)
de_la_salida = [(m.group(1), int(m.group(2))) for m in fila.finditer(crudo)]
mias = RELEIDOS["cap_06"] + RELEIDOS["cap_07"] + RELEIDOS["cap_08"]
print("    pasos que la muestra reparte (leidos de .v53/muestra.txt) : %d" % len(de_la_salida))
print("    pasos que yo declaro releidos                             : %d" % len(mias))
print("    LAS DOS LISTAS COINCIDEN, paso a paso                     : %s"
      % (sorted(de_la_salida) == sorted(RELEIDOS["cap_06"])))
print("    (cap_07 va ENTERO y su lista no la imprime la muestra: son sus 6 pasos)")
print("")

print("| capitulo | candidatos | pasos escritos | regimen `D.58` | pasos releidos | PUENTE | `PASOS INVENTADOS` |")
print("|---|---:|---:|---|---:|---:|---:|")
for cap in sorted(RELEIDOS):
    pasos = 0
    for i in CANDIDATOS[cap]:
        ruta = "cuarentena/grove_high_output/%s.json" % i
        if os.path.exists(ruta):
            pasos += len(json.load(io.open(ruta, encoding="utf-8"))["pasos_accionables"])
    releidos = RELEIDOS[cap]
    puentes = [p for p in releidos if p in PUENTES]
    por_ciento = (100.0 * len(puentes) / len(releidos)) if releidos else 0.0
    print("| `%s` | %d | %d | %s | %d | **%d** | **%s por ciento** |"
          % (cap, len(CANDIDATOS[cap]), pasos, REGIMEN[cap], len(releidos),
             len(puentes), ("%.1f" % por_ciento).replace(".", ",")))
print("")
for cap in sorted(RELEIDOS):
    releidos = RELEIDOS[cap]
    puentes = [p for p in releidos if p in PUENTES]
    por_ciento = (100.0 * len(puentes) / len(releidos)) if releidos else 0.0
    estado = "NO DISPARA" if por_ciento <= TOPE else "DISPARA: RELEER ENTERO ANTES DE SEGUIR"
    print("    %-8s %6s por ciento contra un tope de %.0f : %s"
          % (cap, ("%.1f" % por_ciento).replace(".", ","), TOPE, estado))
print("")
print("    NINGUNA DE LAS CUATRO GUARDAS DE DATO DE D.55 ESTA EN ROJO POR ESTA VIA:")
print("    la fidelidad D.30 con puente es una de las cuatro, y da 0 puentes.")
