# -*- coding: utf-8 -*-
"""LA RELECTURA DE FIDELIDAD D.30 DE LA VUELTA 2 DEL FRENTE, PASO A PASO Y CON SU CITA PEGADA.

NINGUNA GUARDA DE ESTA CASA VE UN PASO QUE YO ESCRIBI Y EL LIBRO NO DICE. Este
instrumento no la sustituye: la PUBLICA. La clase de cada paso, TRANSCRIPCION o
PUENTE, la pongo yo leyendo; lo que hace la maquina es pegar al lado la linea del
libro de la que digo que sale (D.35, el remedio mecanico: la cita se pega, no se
promete), y comprobar que la cuenta de pasos de mi tabla es la misma que la del
fichero de la bandeja.

Si un candidato tuviera mas o menos pasos que filas en mi tabla, el instrumento
PARA y no publica cifra, que es la misma disciplina que la frontera.
"""
import io
import json
import sys
import unicodedata

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

RUTA = "fuentes/grove_high_output/cap_03.md"
BANDEJA = "cuarentena/grove_high_output/%s.json"


def llana(texto):
    texto = texto.replace(chr(0x2014), "-").replace(chr(0x2013), "-")
    texto = texto.replace(chr(0x2018), "'").replace(chr(0x2019), "'")
    texto = texto.replace(chr(0x201C), '"').replace(chr(0x201D), '"')
    texto = texto.replace(chr(0x2026), "...")
    return "".join(c for c in unicodedata.normalize("NFD", texto)
                   if unicodedata.category(c) != "Mn")


LINEAS = io.open(RUTA, encoding="utf-8").read().split("\n")

# MI LECTURA: por cada candidato, la linea del libro de la que sale CADA paso, en
# orden, y su clase. T es TRANSCRIPCION, P es PUENTE.
TANDA = [
    ("elegir_cinco_indicadores_diarios_fabrica",
     [(15, "T"), (17, "T"), (19, "T"), (19, "T"), (21, "T"),
      (23, "T"), (25, "T"), (27, "T"), (27, "T"), (29, "T")]),
    ("emparejar_indicadores_efecto_contraefecto",
     [(31, "T"), (31, "T"), (31, "T"), (31, "T"), (31, "T"), (31, "T"), (33, "T")]),
    ("elegir_indicador_salida_trabajo_administrativo",
     [(35, "T"), (35, "T"), (37, "T"), (39, "T"), (37, "T"), (37, "T"), (37, "T")]),
    ("representar_actividad_caja_negra_ventanas",
     [(73, "T"), (73, "T"), (73, "T"), (73, "T"), (73, "T"),
      (73, "T"), (73, "T"), (77, "T"), (79, "T")]),
    ("construir_indicador_linealidad_alerta_temprana",
     [(83, "T"), (83, "T"), (83, "T"), (83, "T"), (83, "T"),
      (83, "T"), (87, "T"), (87, "T"), (87, "T")]),
    ("construir_indicador_tendencia_patron",
     [(89, "T"), (89, "T"), (89, "T"), (89, "T"), (89, "T"), (89, "T")]),
    ("construir_grafico_escalonado_pronosticos",
     [(91, "T"), (91, "T"), (95, "T"), (91, "T"), (93, "T"), (93, "T"), (93, "T"), (93, "T")]),
    ("archivar_indicadores_resolver_problemas",
     [(99, "T"), (99, "T"), (99, "T"), (99, "T")]),
    ("elegir_fabricar_pedido_pronostico",
     [(103, "T"), (103, "T"), (105, "T"), (105, "T"), (105, "T"),
      (107, "T"), (107, "T"), (109, "T"), (109, "T")]),
    ("casar_flujo_fabricacion_flujo_ventas",
     [(111, "T"), (111, "T"), (111, "T"), (117, "T"), (113, "T"), (113, "T"),
      (115, "T"), (119, "T"), (119, "T"), (119, "T"), (119, "T"), (121, "T")]),
    ("dimensionar_plantilla_administrativa_pronostico",
     [(125, "T"), (125, "T"), (125, "T"), (123, "T"), (125, "T"), (125, "T"), (125, "T")]),
    ("decidir_aceptar_rechazar_material_defectuoso",
     [(135, "T"), (135, "T"), (135, "T"), (135, "T"), (135, "T"),
      (135, "T"), (137, "T"), (137, "T")]),
    ("elegir_inspeccion_barrera_monitorizacion",
     [(139, "T"), (139, "T"), (139, "T"), (141, "T"), (141, "T"), (141, "T"),
      (141, "T"), (141, "T"), (141, "T"), (141, "T"), (141, "T"), (141, "T")]),
    ("variar_frecuencia_inspeccion_nivel_calidad",
     [(143, "T"), (143, "T"), (143, "T"), (143, "T"), (143, "T"), (143, "T")]),
    ("simplificar_trabajo_reducir_numero_pasos",
     [(169, "T"), (169, "T"), (169, "T"), (169, "T"), (171, "T"), (171, "T"), (171, "T")]),
]

total_pasos = total_puentes = 0
descuadres = []
print("=" * 78)
print("RELECTURA DE FIDELIDAD D.30, CANDIDATO A CANDIDATO, CON LA LINEA PEGADA")
print("=" * 78)
print("")
for identificador, filas in TANDA:
    datos = json.load(io.open(BANDEJA % identificador, encoding="utf-8"))
    pasos = datos["pasos_accionables"]
    if len(pasos) != len(filas):
        descuadres.append((identificador, len(pasos), len(filas)))
        continue
    puentes = sum(1 for _l, c in filas if c == "P")
    total_pasos += len(pasos)
    total_puentes += puentes
    print("%s   pasos %d | TRANSCRIPCION %d | PUENTE %d"
          % (identificador, len(pasos), len(pasos) - puentes, puentes))
    for indice, (linea, clase) in enumerate(filas, 1):
        print("  paso %2d  L%-4d %-14s %s"
              % (indice, linea,
                 "TRANSCRIPCION" if clase == "T" else "PUENTE",
                 llana(LINEAS[linea - 1])[:78]))
    print("")

if descuadres:
    print("DESCUADRE ENTRE MI TABLA Y LA BANDEJA, NO SE PUBLICA CIFRA:")
    for identificador, en_fichero, en_tabla in descuadres:
        print("  %s: el fichero trae %d pasos y mi tabla %d"
              % (identificador, en_fichero, en_tabla))
    raise SystemExit(1)

print("=" * 78)
print("EL SALDO DE LA RELECTURA, ROTULADO CON LA POBLACION QUE MIDE")
print("=" * 78)
print("poblacion releida : los %d candidatos que esta vuelta escribio de cap_03,"
      % len(TANDA))
print("                    NO el grafo y NO el capitulo entero del libro")
print("pasos releidos    : %d" % total_pasos)
print("PUENTE            : %d" % total_puentes)
print("PASOS INVENTADOS  : %s por ciento"
      % ("%.2f" % (100.0 * total_puentes / total_pasos)).replace(".", ","))
