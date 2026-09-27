# -*- coding: utf-8 -*-
"""Los 17 pasos que el barrido de las tres especies levanta, cada uno contra la
linea del libro que lo sostiene, con la salida literal pegada (D.35)."""
import re, subprocess

CASOS = [
 ("periodo", "admitir_pronto_mal_desempenio_cuatro_razones", 7,  179, "months of painful legal documentation"),
 ("periodo", "admitir_pronto_mal_desempenio_cuatro_razones", 8,  179, "takes a lot more time"),
 ("periodo", "armar_plan_anual_crecimiento_equipo",           2,  99,  "Once a year"),
 ("periodo", "armar_plan_anual_crecimiento_equipo",           9,  103, "twenty minutes, maximum"),
 ("periodo", "armar_plan_anual_crecimiento_equipo",          20,  113, "five to fifteen minutes"),
 ("periodo", "calibrar_ascensos_evitar_politica",             3,  209, "one day twice a year"),
 ("periodo", "calibrar_decision_despido_documentarla",       10,  185, "another three or six months"),
 ("periodo", "contactar_despedido_mes_despues",               1,  199, "about a month after"),
 ("periodo", "conversar_historia_vida_descubrir_motivadores",15,  59,  "in forty-five minutes"),
 ("periodo", "desplegar_tres_conversaciones_carrera",         9,  43,  "three to six weeks"),
 ("destinat","montar_proceso_contratacion_reducir_sesgo",    10,  137, "go to all interviewers"),
 ("periodo", "montar_proceso_contratacion_reducir_sesgo",    26,  157, "schedule an hour"),
 ("periodo", "montar_proceso_contratacion_reducir_sesgo",    31,  163, "one-hour meeting with a fifteen-minute"),
 ("destinat","montar_proceso_contratacion_reducir_sesgo",    32,  163, "powers that be at your company"),
 ("periodo", "reconocer_excelencia_trayectoria_gradual",      8,  247, "a couple of months"),
 ("periodo", "trazar_plan_dieciocho_meses_aprendizaje",       6,  79,  "six to eighteen months"),
 ("destinat","trazar_plan_dieciocho_meses_aprendizaje",       8,  81,  "make a list of how"),
]

RUTA = "fuentes/scott_radical_candor/cap_10.md"
lineas = open(RUTA, encoding="utf-8").read().split("\n")

print("| especie | unidad y paso | linea | la salida de `grep -n`, pegada | veredicto |")
print("|---|---|---:|---|---|")
vivos = 0
for especie, nid, paso, n, frag in CASOS:
    texto = lineas[n - 1]
    i = texto.find(frag)
    trozo = texto[max(0, i - 28):i + len(frag) + 28] if i >= 0 else "NO ENCONTRADO"
    for codigo, llano in ((8212, ", "), (8220, chr(34)), (8221, chr(34)),
                            (8217, chr(39)), (8211, ", ")):
        trozo = trozo.replace(chr(codigo), llano)
    if i < 0:
        vivos += 1
    print("| %s | `%s` P%d | L%d | `%d: ...%s...` | %s |"
          % (especie, nid, paso, n, n, trozo,
             "**TRANSCRIPCION**" if i >= 0 else "**PUENTE**"))
print()
print("levantados por el barrido : 17 de 206")
print("sostenidos por su linea   : %d" % (17 - vivos))
print("PUENTE                    : %d" % vivos)
