# -*- coding: utf-8 -*-
"""LA RELECTURA DE FIDELIDAD D.30 DE LA VUELTA 43, PASO A PASO Y CON SU CITA PEGADA.

NINGUNA GUARDA DE ESTA CASA VE UN PASO QUE OTRA MANO ESCRIBIO Y EL LIBRO NO DICE.
Estos quince candidatos los mino la linea 'grove' y yo los inserto, asi que la
relectura vale doble: la clase de cada paso, TRANSCRIPCION o PUENTE, la pongo yo
leyendo el parrafo de hoy; lo que hace la maquina es pegar al lado la linea del
libro de la que digo que sale (D.35), y PARAR si mi tabla no tiene tantas filas
como pasos tiene la ficha de la bandeja.

La forma es la de .v2g/fidelidad.py, el instrumento con el que la linea 'grove'
publico la suya. Lo que cambia es que esta tanda cruza TRES capitulos.
"""
import io
import json
import sys
import unicodedata

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

BANDEJA = "cuarentena/grove_high_output/%s.json"
FUENTE = "fuentes/grove_high_output/%s.md"


def llana(texto):
    texto = texto.replace(chr(0x2014), "-").replace(chr(0x2013), "-")
    texto = texto.replace(chr(0x2018), "'").replace(chr(0x2019), "'")
    texto = texto.replace(chr(0x201C), '"').replace(chr(0x201D), '"')
    texto = texto.replace(chr(0x2026), "...")
    return "".join(c for c in unicodedata.normalize("NFD", texto)
                   if unicodedata.category(c) != "Mn")


_cache = {}


def linea(cap, n):
    if cap not in _cache:
        _cache[cap] = io.open(FUENTE % cap, encoding="utf-8").read().split("\n")
    return llana(_cache[cap][n - 1])


# MI LECTURA: por cada candidato, su capitulo y la linea del libro de la que sale
# CADA paso, en orden, con su clase. T es TRANSCRIPCION, P es PUENTE.
TANDA = [
    ("cap_01", "revisar_tres_preguntas_valor_carrera",
     [(103, "T"), (103, "T"), (103, "T"), (105, "T"), (105, "T"),
      (107, "T"), (107, "T")]),
    ("cap_02", "construir_flujo_produccion_paso_limitante",
     [(19, "T"), (19, "T"), (21, "T"), (21, "T"), (23, "T"),
      (23, "T"), (25, "T"), (25, "T"), (27, "T"), (27, "T")]),
    ("cap_02", "clasificar_trabajo_proceso_montaje_prueba",
     [(39, "T"), (39, "T"), (39, "T"), (45, "T"), (45, "T"), (45, "T"), (45, "T")]),
    ("cap_02", "rehacer_flujo_paso_limitante_capacidad",
     [(51, "T"), (51, "T"), (51, "T"), (51, "T"), (53, "T"), (51, "T")]),
    ("cap_02", "equilibrar_capacidad_personal_inventario_plazo",
     [(57, "T"), (57, "T"), (59, "T"), (59, "T"), (59, "T"),
      (59, "T"), (61, "T"), (61, "T")]),
    ("cap_02", "preferir_inspeccion_proceso_prueba_destructiva",
     [(67, "T"), (67, "T"), (67, "T"), (67, "T"), (67, "T"), (67, "T")]),
    ("cap_02", "dimensionar_inventario_materia_prima_reposicion",
     [(69, "T"), (69, "T"), (69, "T"), (69, "T"), (69, "T"), (69, "T"), (69, "T")]),
    ("cap_02", "detectar_arreglar_fallo_etapa_menor_valor",
     [(73, "T"), (73, "T"), (75, "T"), (75, "T"), (75, "T"), (75, "T")]),
    ("cap_03", "elegir_cinco_indicadores_diarios_fabrica",
     [(15, "T"), (17, "T"), (19, "T"), (19, "T"), (21, "T"),
      (23, "T"), (25, "T"), (27, "T"), (27, "T"), (29, "T")]),
    ("cap_03", "representar_actividad_caja_negra_ventanas",
     [(73, "T"), (73, "T"), (73, "T"), (73, "T"), (73, "T"),
      (73, "T"), (73, "T"), (77, "T"), (79, "T")]),
    ("cap_03", "construir_indicador_linealidad_alerta_temprana",
     [(83, "T"), (83, "T"), (83, "T"), (83, "T"), (83, "T"),
      (83, "T"), (87, "T"), (87, "T"), (87, "T")]),
    ("cap_03", "casar_flujo_fabricacion_flujo_ventas",
     [(111, "T"), (111, "T"), (111, "T"), (111, "T"), (113, "T"), (113, "T"),
      (115, "T"), (119, "T"), (119, "T"), (119, "T"), (119, "T"), (121, "T")]),
    ("cap_03", "dimensionar_plantilla_administrativa_pronostico",
     [(125, "T"), (125, "T"), (125, "T"), (123, "T"), (125, "T"),
      (125, "T"), (125, "T")]),
    ("cap_03", "decidir_aceptar_rechazar_material_defectuoso",
     [(135, "T"), (135, "T"), (135, "T"), (135, "T"), (135, "T"),
      (135, "T"), (137, "T"), (137, "T")]),
    ("cap_03", "elegir_inspeccion_barrera_monitorizacion",
     [(139, "T"), (139, "T"), (139, "T"), (141, "T"), (141, "T"), (141, "T"),
      (141, "T"), (141, "T"), (141, "T"), (141, "T"), (141, "T"), (141, "T")]),
]

print("=" * 78)
print("RELECTURA DE FIDELIDAD D.30, CANDIDATO A CANDIDATO, CON LA LINEA PEGADA")
print("=" * 78)
print()

tot = trans = puente = 0
for cap, ident, clases in TANDA:
    ficha = json.load(io.open(BANDEJA % ident, encoding="utf-8"))
    pasos = ficha["pasos_accionables"]
    if len(pasos) != len(clases):
        print("PARADA: %s tiene %d pasos y mi tabla %d filas."
              % (ident, len(pasos), len(clases)))
        raise SystemExit(1)
    t = sum(1 for _, c in clases if c == "T")
    p = len(clases) - t
    tot += len(clases)
    trans += t
    puente += p
    print("%s   %s   pasos %d | TRANSCRIPCION %d | PUENTE %d"
          % (ident, cap, len(pasos), t, p))
    for n, (ln, c) in enumerate(clases, 1):
        print("  paso %2d  L%-4d %-14s %s"
              % (n, ln, "TRANSCRIPCION" if c == "T" else "PUENTE",
                 linea(cap, ln)[:76]))
    print()

print("=" * 78)
print("LA TANDA ENTERA")
print("  candidatos releidos : %d" % len(TANDA))
print("  pasos releidos      : %d" % tot)
print("  TRANSCRIPCION       : %d" % trans)
print("  PUENTE              : %d" % puente)
print("  PASOS INVENTADOS    : %.2f por ciento" % (100.0 * puente / tot))
print("=" * 78)
