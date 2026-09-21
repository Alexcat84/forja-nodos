# -*- coding: utf-8 -*-
"""LA TANDA DE cap_04 DE LA VUELTA 46, CONTADA DE SUS PROPIOS FICHEROS.

Ninguna celda se teclea: el id, el tramo y los pasos salen del JSON del candidato; el
saldo y los vecinos salen del informe de la aduana de ESE candidato; los segundos salen
de su reloj. La cifra de fidelidad sale de la linea RELECTURA DE FIDELIDAD del propio
resumen_teorico, que es donde D.30 manda escribirla en el acto.
"""
import io
import json
import os
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

# EL ORDEN ES EL ORDEN DEL LIBRO, que es el orden en que se escribieron.
TANDA = [
    ("01", "P7", "reunir_informacion_gerencial_vias_variadas"),
    ("02", "P9", "escalonar_fuentes_informacion_gerencial"),
    ("03", "P10", "programar_visita_area_observar_despachar"),
    ("04", "P11", "transmitir_objetivos_prioridades_preferencias"),
    ("05", "P13", "empujar_persona_reunion_direccion_preferida"),
    ("06", "P18", "subir_productividad_gerencial_tres_vias"),
    ("07", "P19", "buscar_actividad_alta_palanca_tres_vias"),
    ("08", "P20", "elegir_momento_actividad_palanca_maxima"),
]

FID = re.compile(r"RELECTURA DE FIDELIDAD D\.30 EN EL ACTO: (\d+) pasos, (\d+) "
                 r"TRANSCRIPCION, (\d+) PUENTE")
SALDO = re.compile(r"^\[(ENTRARIA|BLOQUEARIA|CAERIA)\]", re.M)
VECINO = re.compile(r"^    vecino (\S+)\s+\[levantada por: (\S+)\]", re.M)
SIM = re.compile(r"similitud_texto ([\d.]+) \| familia_id ([\d.]+) \| paso_contra_nodo ([\d.]+)")
SEG = re.compile(r"segundos=(\d+)")

filas = []
tot_pasos = tot_trans = tot_puente = 0
tot_seg = 0
pares = []
for n, tramo, ident in TANDA:
    ficha = json.load(io.open(os.path.join("cuarentena", "grove_high_output", ident + ".json"),
                              encoding="utf-8"))
    informe = io.open(os.path.join(".v46", "informe_%s.txt" % n), encoding="utf-8").read()
    reloj = io.open(os.path.join(".v46", "reloj_c%s.txt" % n), encoding="utf-8").read()

    m = FID.search(ficha["resumen_teorico"])
    pasos, trans, puente = (int(m.group(1)), int(m.group(2)), int(m.group(3)))
    if pasos != len(ficha["pasos_accionables"]):
        print("LA TABLA NO SE PUBLICA: %s declara %d pasos y tiene %d"
              % (ident, pasos, len(ficha["pasos_accionables"])))
        raise SystemExit(1)
    saldo = SALDO.search(informe).group(1)
    vecinos = VECINO.findall(informe)
    sims = SIM.findall(informe)
    segundos = int(SEG.search(reloj).group(1))

    tot_pasos += pasos
    tot_trans += trans
    tot_puente += puente
    tot_seg += segundos
    for (v, senial), (s, f, p) in zip(vecinos, sims):
        pares.append((ident, v, senial, s, f, p))
    filas.append((n, tramo, ident, pasos, trans, puente, saldo, len(vecinos), segundos))

print("=" * 78)
print("1. LA TANDA DE cap_04, CANDIDATO POR CANDIDATO")
print("=" * 78)
print("| # | tramo | candidato | pasos | TRANSCRIPCION | PUENTE | la aduana, en el acto | vecinos | s |")
print("|---:|---|---|---:|---:|---:|---|---:|---:|")
for n, tramo, ident, pasos, trans, puente, saldo, nv, seg in filas:
    print("| %s | `%s` | `%s` | %d | %d | **%d** | `%s` | %d | %d |"
          % (n.lstrip("0"), tramo, ident, pasos, trans, puente, saldo, nv, seg))
print("| | | **%d candidatos** | **%d** | **%d** | **%d** | | **%d** | **%d** |"
      % (len(filas), tot_pasos, tot_trans, tot_puente, len(pares), tot_seg))
print("")

print("=" * 78)
print("2. PASOS INVENTADOS DE cap_04 (D.30), CON SU DENOMINADOR")
print("=" * 78)
print("| capitulo | PUENTE | pasos escritos | por ciento | tope |")
print("|---|---:|---:|---:|---:|")
print("| `cap_04` | **%d** | **%d** | **%.2f** | 10 |" % (tot_puente, tot_pasos,
                                                          100.0 * tot_puente / tot_pasos))
print("| **total de la vuelta** | **%d** | **%d** | **%.2f** | 10 |"
      % (tot_puente, tot_pasos, 100.0 * tot_puente / tot_pasos))
print("")
print("EL DENOMINADOR SE ESCRIBE AUNQUE EL NUMERADOR SEA CERO: %d pasos escritos." % tot_pasos)
print("")

print("=" * 78)
print("3. LA COLA DE LECTURA QUE ESTA TANDA ABRE, PAR A PAR")
print("=" * 78)
# LA PRIMERA CELDA LLEVA EL NUMERO DE PAR, y es un remedio, no un adorno: el tallado
# de D.41 casa las filas por su PRIMERA celda, y un candidato con cinco vecinos repite
# cinco veces la misma clave. Numerado, cada fila tiene clave propia.
print("| par | candidato | vecino | senial | sim | fam | paso |")
print("|---:|---|---|---|---:|---:|---:|")
for i, (ident, v, senial, s, f, p) in enumerate(pares, 1):
    print("| %d | `%s` | `%s` | %s | %s | %s | %s |" % (i, ident, v, senial, s, f, p))
print("| | | | **%d pares** | | | |" % len(pares))
print("")
altas = [x for x in pares if float(x[3]) >= 0.4]
print("PARES CON similitud_texto POR ENCIMA DE 0,40 (EXTRACTOR.md 11: se leen antes que"
      " ningun otro): %d" % len(altas))
for x in altas:
    print("   %s  contra  %s   sim %s" % (x[0], x[1], x[3]))
menor = min(float(x[3]) for x in pares)
mayor = max(float(x[3]) for x in pares)
print("BANDA DE similitud_texto DE ESTA TANDA: de %.3f a %.3f" % (menor, mayor))

print("")
print("=" * 78)
print("4. EL RELOJ DE LA ADUANA EN SECO, QUE ES LO QUE DECIDE EL TRAMO")
print("=" * 78)
segs = [f[8] for f in filas]
print("candidatos pasados por la aduana en esta vuelta : %d" % len(segs))
print("segundos por candidato, menor y mayor           : %d y %d" % (min(segs), max(segs)))
print("media por candidato                             : %.1f s" % (1.0 * sum(segs) / len(segs)))
print("total de la tanda                               : %d s  (%.1f min)"
      % (sum(segs), sum(segs) / 60.0))
print("lo que costarian los 22 de la frontera          : %.0f s  (%.1f min)"
      % (22.0 * sum(segs) / len(segs), 22.0 * sum(segs) / len(segs) / 60.0))
print("lo que costaria el techo de 15                  : %.0f s  (%.1f min)"
      % (15.0 * sum(segs) / len(segs), 15.0 * sum(segs) / len(segs) / 60.0))
