# -*- coding: utf-8 -*-
"""LA TANDA DE cap_04 DE LA VUELTA 47, CONTADA DE SUS PROPIOS FICHEROS.

Mismo instrumento que el de la vuelta 46 (.v46/tanda.py), con su tanda dentro y con
dos anadidos que esta vuelta necesita:

  (a) la fila de la vuelta 46 al lado de la de la vuelta 47 en la tabla de PASOS
      INVENTADOS, que es lo que la TAREA 3 del encargo pide, y la de la 46 no se
      teclea: se cuenta de sus ocho fichas, que viven en la misma bandeja.
  (b) el reloj compara su media contra la que la vuelta 46 midio, contada tambien
      de los ficheros de la 46 y no copiada de su reporte.

Ninguna celda se teclea: el id, el tramo y los pasos salen del JSON del candidato; el
saldo y los vecinos salen del informe de la aduana de ESE candidato; los segundos salen
de su reloj. La cifra de fidelidad sale de la linea RELECTURA DE FIDELIDAD del propio
resumen_teorico, que es donde D.30 manda escribirla en el acto.

Y SE PARA SIN PUBLICAR LA TABLA si una ficha declara mas pasos de los que tiene, que es
el remedio barato que la vuelta 46 propuso en HH.5.e y aqui se vuelve a usar.
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
    ("01", "P21 y P24", "detectar_palanca_negativa_actividad_mando"),
    ("02", "P27", "delegar_tarea_base_comun_seguimiento"),
    ("03", "P29", "supervisar_tarea_delegada_etapa_menor_valor"),
    ("04", "P30", "supervisar_decision_delegada_preguntas_concretas"),
    ("05", "P32", "identificar_paso_limitante_jornada_desfases"),
    ("06", "P33", "agrupar_tareas_semejantes_aprovechar_preparacion"),
]
# LOS DOS QUE EL ENCARGO PEDIA Y NO CORRIERON (P34a y P34b) NO ESTAN EN ESTA LISTA, y no
# estan porque NO HAY FICHA: un candidato no esta escrito hasta que ha pasado la aduana
# (EXTRACTOR.md 16), y el reloj de la tanda paso el techo de 67 minutos en el sexto.
# Sus borradores quedan en .v47/borrador_sin_aduana_c07.py y .v47/borrador_sin_aduana_c08.py.

# LA TANDA DE LA VUELTA 46, para el contraste que pide la TAREA 3. Solo los ids: sus
# cifras se cuentan de las mismas fichas y de los mismos relojes, no de su reporte.
TANDA_46 = [
    ("01", "reunir_informacion_gerencial_vias_variadas"),
    ("02", "escalonar_fuentes_informacion_gerencial"),
    ("03", "programar_visita_area_observar_despachar"),
    ("04", "transmitir_objetivos_prioridades_preferencias"),
    ("05", "empujar_persona_reunion_direccion_preferida"),
    ("06", "subir_productividad_gerencial_tres_vias"),
    ("07", "buscar_actividad_alta_palanca_tres_vias"),
    ("08", "elegir_momento_actividad_palanca_maxima"),
]

FID = re.compile(r"RELECTURA DE FIDELIDAD D\.30 EN EL ACTO: (\d+) pasos, (\d+) "
                 r"TRANSCRIPCION, (\d+) PUENTE")
SALDO = re.compile(r"^\[(ENTRARIA|BLOQUEARIA|CAERIA)\]", re.M)
VECINO = re.compile(r"^    vecino (\S+)\s+\[levantada por: (\S+)\]", re.M)
SIM = re.compile(r"similitud_texto ([\d.]+) \| familia_id ([\d.]+) \| paso_contra_nodo ([\d.]+)")
SEG = re.compile(r"segundos=(\d+)")
POB = re.compile(r"poblacion del barrido\s+: (\d+)\s+\((\d+) del grafo mas (\d+)")


def ficha_de(ident):
    return json.load(io.open(os.path.join("cuarentena", "grove_high_output", ident + ".json"),
                             encoding="utf-8"))


def fidelidad_de(ident):
    """(pasos, transcripcion, puente), y SE PARA si la ficha declara de mas."""
    ficha = ficha_de(ident)
    m = FID.search(ficha["resumen_teorico"])
    if m is None:
        print("LA TABLA NO SE PUBLICA: %s no declara su RELECTURA DE FIDELIDAD D.30" % ident)
        raise SystemExit(1)
    pasos, trans, puente = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if pasos != len(ficha["pasos_accionables"]) - 1:
        print("LA TABLA NO SE PUBLICA: %s declara %d pasos y tiene %d"
              % (ident, pasos, len(ficha["pasos_accionables"])))
        raise SystemExit(1)
    if trans + puente != pasos:
        print("LA TABLA NO SE PUBLICA: %s declara %d mas %d y sus pasos son %d"
              % (ident, trans, puente, pasos))
        raise SystemExit(1)
    return pasos, trans, puente


filas = []
tot_pasos = tot_trans = tot_puente = 0
tot_seg = 0
pares = []
poblaciones = []
for n, tramo, ident in TANDA:
    informe = io.open(os.path.join(".v47", "informe_%s.txt" % n), encoding="utf-8").read()
    reloj = io.open(os.path.join(".v47", "reloj_c%s.txt" % n), encoding="utf-8").read()

    pasos, trans, puente = fidelidad_de(ident)
    saldo = SALDO.search(informe).group(1)
    vecinos = VECINO.findall(informe)
    sims = SIM.findall(informe)
    segundos = int(SEG.search(reloj).group(1))
    mp = POB.search(informe)
    if mp:
        poblaciones.append(int(mp.group(1)))

    tot_pasos += pasos
    tot_trans += trans
    tot_puente += puente
    tot_seg += segundos
    for (v, senial), (s, f, p) in zip(vecinos, sims):
        pares.append((ident, v, senial, s, f, p))
    filas.append((n, tramo, ident, pasos, trans, puente, saldo, len(vecinos), segundos))

print("=" * 78)
print("1. LA TANDA DE cap_04 DE LA VUELTA 47, CANDIDATO POR CANDIDATO")
print("=" * 78)
print("| # | tramo | candidato | pasos | TRANSCRIPCION | PUENTE | la aduana, en el acto | vecinos | s |")
print("|---:|---|---|---:|---:|---:|---|---:|---:|")
for n, tramo, ident, pasos, trans, puente, saldo, nv, seg in filas:
    print("| %s | `%s` | `%s` | %d | %d | **%d** | `%s` | %d | %d |"
          % (n.lstrip("0"), tramo, ident, pasos, trans, puente, saldo, nv, seg))
print("| | | **%d candidatos** | **%d** | **%d** | **%d** | | **%d** | **%d** |"
      % (len(filas), tot_pasos, tot_trans, tot_puente, len(pares), tot_seg))
print("")
cuenta = {}
for f in filas:
    cuenta[f[6]] = cuenta.get(f[6], 0) + 1
print("EL SALDO DE LA TANDA: " + ", ".join("%s %d" % (k, cuenta[k]) for k in sorted(cuenta)))
if poblaciones:
    print("POBLACION DEL BARRIDO, del primer informe al ultimo: de %d a %d"
          % (poblaciones[0], poblaciones[-1]))
print("")

# ---------------------------------------------------------------- PASOS INVENTADOS
p46 = t46 = pu46 = 0
for n, ident in TANDA_46:
    pasos, trans, puente = fidelidad_de(ident)
    p46 += pasos
    t46 += trans
    pu46 += puente

print("=" * 78)
print("2. PASOS INVENTADOS DE cap_04 (D.30), CON SU DENOMINADOR Y CON SU CONTRASTE")
print("=" * 78)
print("| capitulo y vuelta | PUENTE | pasos escritos | por ciento | tope |")
print("|---|---:|---:|---:|---:|")
print("| `cap_04`, vuelta 47, los %d de hoy | **%d** | **%d** | **%.2f** | 10 |"
      % (len(filas), tot_puente, tot_pasos, 100.0 * tot_puente / tot_pasos))
print("| `cap_04`, vuelta 46, los %d anteriores | **%d** | **%d** | **%.2f** | 10 |"
      % (len(TANDA_46), pu46, p46, 100.0 * pu46 / p46))
print("| **`cap_04` entero hasta hoy, las dos tandas** | **%d** | **%d** | **%.2f** | 10 |"
      % (tot_puente + pu46, tot_pasos + p46,
         100.0 * (tot_puente + pu46) / (tot_pasos + p46)))
print("")
print("EL DENOMINADOR SE ESCRIBE AUNQUE EL NUMERADOR SEA CERO: %d pasos escritos hoy,"
      " %d en la vuelta 46, %d en total." % (tot_pasos, p46, tot_pasos + p46))
print("")

# ---------------------------------------------------------------- COLA DE LECTURA
print("=" * 78)
print("3. LA COLA DE LECTURA QUE ESTA TANDA ABRE, PAR A PAR")
print("=" * 78)
# LA PRIMERA CELDA LLEVA EL NUMERO DE PAR, y es un remedio, no un adorno: el tallado
# de D.41 casa las filas por su PRIMERA celda, y un candidato con varios vecinos repite
# la misma clave. Numerado, cada fila tiene clave propia. Es d029.
print("| par | candidato | vecino | senial | sim | fam | paso |")
print("|---:|---|---|---|---:|---:|---:|")
for i, (ident, v, senial, s, f, p) in enumerate(pares, 1):
    print("| %d | `%s` | `%s` | %s | %s | %s | %s |" % (i, ident, v, senial, s, f, p))
print("| | | | **%d pares** | | | |" % len(pares))
print("")
if pares:
    altas = [x for x in pares if float(x[3]) >= 0.4]
    print("PARES CON similitud_texto POR ENCIMA DE 0,40 (EXTRACTOR.md 11: se leen antes que"
          " ningun otro): %d" % len(altas))
    for x in altas:
        print("   %s  contra  %s   sim %s" % (x[0], x[1], x[3]))
    menor = min(float(x[3]) for x in pares)
    mayor = max(float(x[3]) for x in pares)
    print("BANDA DE similitud_texto DE ESTA TANDA: de %.3f a %.3f" % (menor, mayor))
    seniales = {}
    for x in pares:
        seniales[x[2]] = seniales.get(x[2], 0) + 1
    print("QUE SENIAL LEVANTA CADA VECINDAD: "
          + ", ".join("%s %d" % (k, seniales[k]) for k in sorted(seniales)))
else:
    print("ESTA TANDA NO ABRE COLA DE LECTURA: cero pares.")

# ---------------------------------------------------------------- RELOJ
print("")
print("=" * 78)
print("4. EL RELOJ DE LA ADUANA EN SECO, QUE ES LO QUE DECIDE EL TRAMO")
print("=" * 78)
segs = [f[8] for f in filas]
media = 1.0 * sum(segs) / len(segs)
print("candidatos pasados por la aduana en esta vuelta : %d" % len(segs))
print("segundos por candidato, menor y mayor           : %d y %d" % (min(segs), max(segs)))
print("media por candidato                             : %.1f s" % media)
print("total de la tanda                               : %d s  (%.1f min)"
      % (sum(segs), sum(segs) / 60.0))
print("techo en minutos que el encargo escribio (d011) : 67 min")
print("DENTRO DEL TECHO DE MINUTOS                     : %s"
      % ("SI" if sum(segs) / 60.0 <= 67 else "NO"))

segs46 = []
for n, ident in TANDA_46:
    reloj = io.open(os.path.join(".v46", "reloj_c%s.txt" % n), encoding="utf-8").read()
    segs46.append(int(SEG.search(reloj).group(1)))
media46 = 1.0 * sum(segs46) / len(segs46)
print("")
print("CONTRASTE CONTRA LA VUELTA 46, contado de sus propios relojes y no de su reporte:")
print("  media de la vuelta 46                         : %.1f s" % media46)
print("  media de la vuelta 47                         : %.1f s" % media)
print("  subida                                        : %+.1f s por candidato (%+.1f por ciento)"
      % (media - media46, 100.0 * (media - media46) / media46))
print("")
quedan = 22 - 8 - len(filas)
print("LO QUE COSTARIA EL RESTO DE cap_04 A ESTA MEDIA:")
print("  los %d que quedan de los 22 de la frontera     : %.0f s  (%.1f min)"
      % (quedan, quedan * media, quedan * media / 60.0))
print("")
print("POR QUE LA MEDIA SUBIO, MEDIDO Y NO SUPUESTO:")
pasos46 = 0
for n, ident in TANDA_46:
    pasos46 += len(ficha_de(ident)["pasos_accionables"])
pasos47 = sum(f[3] for f in filas)
print("  pasos por candidato, vuelta 46                : %.2f" % (1.0 * pasos46 / len(TANDA_46)))
print("  pasos por candidato, vuelta 47                : %.2f" % (1.0 * pasos47 / len(filas)))
print("  segundos por PASO, vuelta 46                  : %.1f s" % (1.0 * sum(segs46) / pasos46))
print("  segundos por PASO, vuelta 47                  : %.1f s" % (1.0 * sum(segs) / pasos47))
