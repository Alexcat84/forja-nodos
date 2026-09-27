# -*- coding: utf-8 -*-
"""PASOS INVENTADOS POR CAPITULO (AUDITOR_FORJA.md 8.3), vuelta 28.

EL DENOMINADOR SALE DEL DATO: cuenta `pasos_accionables` de cada candidato del
tramo, leyendolo del fichero, este en la bandeja o ya archivado en `_insertados`.

EL NUMERADOR LO PONE LA LECTURA, porque ninguna maquina lo puede poner (`D.30`):
la aduana no tiene el libro delante. Los PUENTE de `PUENTES` los marque yo leyendo
cada paso contra su parrafo, con el libro reabierto por `.v28e/leer.py`.

UN DICCIONARIO VACIO DICE CERO, Y ESO ES UNA AFIRMACION, NO UNA OMISION.
"""
import sys, io, json, re, os

PUENTES = {}

ORDEN = ["recorrer_rueda_conscientemente_cultura_equipo",
         "recorrer_rueda_hacer_cosas_equipo",
         "crear_espacio_seguro_madurar_ideas_nuevas",
         "crear_obligacion_disentir_equipo",
         "parar_debate_emocion_agotamiento",
         "fijar_fecha_cierre_debate_equipo",
         "repartir_decision_cercanos_hechos",
         "pedir_hechos_decision_evitar_recomendaciones",
         "persuadir_emocion_oyente_no_propia",
         "establecer_credibilidad_pericia_humildad",
         "compartir_logica_mostrar_razonamiento",
         "minimizar_impuesto_colaboracion_equipo",
         "proteger_tiempo_equipo_jefe",
         "mantener_manos_trabajo_real_equipo",
         "reservar_calendario_tiempo_ejecutar",
         "cuidarse_agotamiento_centro_rueda"]


def cargar(nid):
    for base in ("cuarentena/scott_radical_candor",
                 "cuarentena/_insertados/scott_radical_candor"):
        ruta = os.path.join(base, nid + ".json")
        if os.path.isfile(ruta):
            return json.load(io.open(ruta, encoding="utf-8"))
    raise SystemExit("no encuentro %s" % nid)


def main():
    salida = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    por_cap = {}
    salida.write("| nodo | capitulo | pasos escritos | PUENTE |\n")
    salida.write("|---|---|---:|---:|\n")
    for nid in ORDEN:
        d = cargar(nid)
        cap = re.search(r"cap_(\d+)\.md", d["resumen_teorico"]).group(0).replace(".md", "")
        n = len(d["pasos_accionables"])
        p = PUENTES.get(nid, 0)
        por_cap.setdefault(cap, [0, 0, 0])
        por_cap[cap][0] += 1
        por_cap[cap][1] += n
        por_cap[cap][2] += p
        salida.write("| `%s` | `%s` | %d | %d |\n" % (nid, cap, n, p))
    salida.write("\n")
    salida.write("| capitulo | nodos | pasos escritos | PUENTE | PASOS INVENTADOS |\n")
    salida.write("|---|---:|---:|---:|---:|\n")
    tn = tp = tb = 0
    for cap in sorted(por_cap):
        nodos, pasos, puentes = por_cap[cap]
        tn += nodos; tp += pasos; tb += puentes
        salida.write("| **`%s`** (lote 4, `scott_radical_candor`) | %d | **%d** | **%d** "
                     "| **%s por ciento** |\n"
                     % (cap, nodos, pasos, puentes,
                        ("%.2f" % (100.0 * puentes / pasos)).replace(".", ",")))
    salida.write("| **total del tramo de esta vuelta** | %d | **%d** | **%d** "
                 "| **%s por ciento** |\n"
                 % (tn, tp, tb, ("%.2f" % (100.0 * tb / tp)).replace(".", ",")))
    salida.flush()


main()
