# -*- coding: utf-8 -*-
"""PASOS INVENTADOS de cap_12 y cap_13 (D.30, AUDITOR_FORJA.md 8). La cuenta de
pasos se lee del fichero; la columna PUENTE es el veredicto de mi relectura, uno
por paso, contra su linea del libro."""
import io
import json

# (id, lineas del libro, PUENTE de mi relectura, defectos de transcripcion)
CAP12 = [
    ("desplegar_plan_orden_operaciones_franqueza_radical", "L13-L49", 1, 0),
    ("contar_historias_propias_explicar_franqueza_radical", "L17", 0, 0),
]
CAP13 = [
    ("mejorar_consciencia_propia_relacional_dos_practicas", "L17-L22,L35-L40", 0, 0),
    ("contar_cuatro_historias_propias_ver_hueco_intencion", "L41-L58", 0, 1),
    ("practicar_triangulo_critica_tres_papeles", "L59-L72", 0, 0),
    ("pedir_critica_primero_crear_seguridad_psicologica", "L73-L86,L105-L114", 0, 0),
    ("elegir_pregunta_recurrente_pedir_critica", "L115-L120,L129-L166", 0, 0),
    ("resolver_dudas_frecuentes_pedir_critica", "L167-L186", 0, 0),
    ("abrazar_incomodidad_silencio_contar_seis", "L187-L198", 0, 0),
    ("escuchar_entender_critica_dominar_defensa", "L199-L214", 0, 0),
    ("premiar_franqueza_hacer_escucha_tangible", "L215-L234", 0, 0),
    ("integrar_peticion_critica_rutina_existente", "L111-L112,L235-L246", 0, 0),
    ("dar_elogio_disciplina_igual_critica", "L247-L252,L267-L288", 0, 1),
    ("medir_critica_respuesta_oyente_brujula", "L289-L322", 0, 0),
]


def ruta(nid):
    for carpeta in ("cuarentena/scott_radical_candor",
                    "cuarentena/_insertados/scott_radical_candor"):
        try:
            return json.load(io.open("%s/%s.json" % (carpeta, nid), encoding="utf-8"))
        except IOError:
            continue
    raise SystemExit("no encuentro %s" % nid)


def coma(x):
    return ("%.2f" % x).replace(".", ",")


print("| unidad | lineas | pasos | TRANSCRIPCION | PUENTE | por ciento |")
print("|---|---:|---:|---:|---:|---:|")
gp = gt = gb = gd = 0
for nombre, tramo in (("cap_12", CAP12), ("cap_13", CAP13)):
    tp = tt = tb = td = 0
    for nid, linea, puentes, defectos in tramo:
        d = ruta(nid)
        n = len(d["pasos_accionables"])
        tp += n
        tb += puentes
        td += defectos
        tt += n - puentes
        print("| `%s` | %s | %d | %d | **%d** | %s |"
              % (nid, linea, n, n - puentes, puentes, coma(puentes * 100.0 / n)))
    print("| **TOTAL de `%s`** | | **%d** | **%d** | **%d** | **%s** |"
          % (nombre, tp, tt, tb, coma(tb * 100.0 / tp)))
    gp += tp
    gt += tt
    gb += tb
    gd += td
print("| **TOTAL del tramo, `cap_12` mas `cap_13`** | | **%d** | **%d** | **%d** | **%s** |"
      % (gp, gt, gb, coma(gb * 100.0 / gp)))
print()
print("defectos de TRANSCRIPCION corregidos, que NO cuento como PUENTE: %d" % gd)
print("  si el auditor los lee como PUENTE, cap_13 pasa de 0 de 212 a 2 de 212, o sea %s por ciento"
      % coma(2 * 100.0 / 212))
