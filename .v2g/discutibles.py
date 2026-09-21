# -*- coding: utf-8 -*-
"""LOS DISCUTIBLES DE LA VUELTA, IMPRESOS DE LAS PROPIAS FICHAS Y NO TECLEADOS.

EXTRACTOR.md 8: los discutibles se marcan ANTES de saber si aciertas, y van en el reporte
para que el auditor empiece la relectura ciega por ellos. La metrica de credito distingue
una caida DENTRO del marcado de una FUERA, y esa diferencia solo significa algo si el
marcado se hizo a ciegas.

CADA FILA SE SACA DEL resumen_teorico DEL PROPIO CANDIDATO, del tramo que empieza por
DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO. Si un candidato no lo trae, el instrumento
lo dice en su fila en vez de callarlo: un discutible que no se escribio no se puede
inventar despues.
"""
import io
import json
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

BANDEJA = "cuarentena/grove_high_output/%s.json"

ORDEN = ["elegir_cinco_indicadores_diarios_fabrica",
         "emparejar_indicadores_efecto_contraefecto",
         "elegir_indicador_salida_trabajo_administrativo",
         "representar_actividad_caja_negra_ventanas",
         "construir_indicador_linealidad_alerta_temprana",
         "construir_indicador_tendencia_patron",
         "construir_grafico_escalonado_pronosticos",
         "archivar_indicadores_resolver_problemas",
         "elegir_fabricar_pedido_pronostico",
         "casar_flujo_fabricacion_flujo_ventas",
         "dimensionar_plantilla_administrativa_pronostico",
         "decidir_aceptar_rechazar_material_defectuoso",
         "elegir_inspeccion_barrera_monitorizacion",
         "variar_frecuencia_inspeccion_nivel_calidad",
         "simplificar_trabajo_reducir_numero_pasos"]

# LA MARCA SE BUSCA SIN LOS DOS PUNTOS, y eso lo aprendi de este mismo instrumento: en su
# primera corrida dio 1 SIN MARCAR, y era falso. La ficha de la caja negra escribe
# "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO, y es el mas gordo de mi tanda:", o sea
# que el rotulo esta y lleva un inciso antes de los dos puntos. Publicar aquel 1 habria
# sido una cifra cierta con rotulo falso, que es justo la especie que paro el bucle.
MARCA = "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO"
SEGUNDA = "SEGUNDO DISCUTIBLE"

print("| # | candidato | lo que marco como discutible, sacado de su propia ficha | segundo discutible |")
print("|---:|---|---|---|")
sin_marca = []
con_segundo = 0
for numero, identificador in enumerate(ORDEN, 1):
    datos = json.load(io.open(BANDEJA % identificador, encoding="utf-8"))
    resumen = datos["resumen_teorico"]
    if MARCA not in resumen:
        sin_marca.append(identificador)
        print("| %d | `%s` | **SIN MARCAR, y se dice en vez de callarlo** | |"
              % (numero, identificador))
        continue
    trozo = resumen.split(MARCA, 1)[1]
    # lo que sigue a la marca puede traer un inciso antes de los dos puntos
    if ":" in trozo[:120]:
        trozo = trozo.split(":", 1)[1]
    segundo = ""
    if SEGUNDA in trozo:
        trozo, resto = trozo.split(SEGUNDA, 1)
        con_segundo += 1
        segundo = re.split(r"(?<=\.)\s+[A-Z]{4,}", resto.lstrip(", ").lstrip(":").strip())[0]
        segundo = segundo.split(". ")[0].strip()
        if len(segundo) > 320:
            segundo = segundo[:317] + "..."
    corte = re.split(r"(?<=\.)\s+(?=[A-Z]{4,})", trozo.strip())[0].strip()
    if len(corte) > 420:
        corte = corte[:417] + "..."
    print("| %d | `%s` | %s | %s |" % (numero, identificador, corte, segundo or "(ninguno)"))

print("")
print("CANDIDATOS DE LA TANDA                       : %d" % len(ORDEN))
print("CON DISCUTIBLE MARCADO ANTES DE SABER        : %d" % (len(ORDEN) - len(sin_marca)))
print("SIN MARCAR                                   : %d" % len(sin_marca))
print("CON UN SEGUNDO DISCUTIBLE, de familia        : %d" % con_segundo)
