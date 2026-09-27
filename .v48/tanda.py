# -*- coding: utf-8 -*-
"""LA TANDA DE cap_04 DE LA VUELTA 48, CONTADA DE SUS PROPIOS FICHEROS.

Mismo instrumento que el de la vuelta 47 (.v47/tanda.py), con dos cambios que el
encargo de hoy obliga:

  (a) la TAREA 3 pide TRES filas y no dos: la de los cinco de hoy, la de los 14 ya
      minados (las tandas de las vueltas 46 y 47 juntas) y la de cap_04 entero. La de
      los 14 no se teclea: se cuenta de sus catorce fichas, que viven en la bandeja.
  (b) el techo que muerde ya no es el de minutos sino el de PASOS (46.5.c), asi que el
      reloj publica los dos y dice cual se paso primero.

Ninguna celda se teclea: el id, el tramo y los pasos salen del JSON del candidato; el
saldo y los vecinos salen del informe de la aduana de ESE candidato; los segundos salen
de su reloj. La cifra de fidelidad sale de la linea RELECTURA DE FIDELIDAD del propio
resumen_teorico, que es donde D.30 manda escribirla en el acto.

Y SE PARA SIN PUBLICAR LA TABLA si una ficha declara mas pasos de los que tiene.
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
    ("01", "P34a", "usar_calendario_herramienta_planificacion_produccion"),
    ("02", "P34b", "decir_no_trabajo_excede_capacidad"),
    ("03", "P36", "llevar_inventario_proyectos_discrecionales"),
    ("04", "P38", "dimensionar_numero_subordinados_medio_dia_semanal"),
    ("05", "P39", "buscar_regularidad_bloques_iguales_trabajo_mando"),
]

# LOS 14 YA MINADOS EN cap_04 ANTES DE HOY: los 8 de la vuelta 46 y los 6 de la 47.
# Solo los ids: sus cifras se cuentan de las mismas fichas, no de sus reportes.
YA_MINADOS = [
    ("46", "reunir_informacion_gerencial_vias_variadas"),
    ("46", "escalonar_fuentes_informacion_gerencial"),
    ("46", "programar_visita_area_observar_despachar"),
    ("46", "transmitir_objetivos_prioridades_preferencias"),
    ("46", "empujar_persona_reunion_direccion_preferida"),
    ("46", "subir_productividad_gerencial_tres_vias"),
    ("46", "buscar_actividad_alta_palanca_tres_vias"),
    ("46", "elegir_momento_actividad_palanca_maxima"),
    ("47", "detectar_palanca_negativa_actividad_mando"),
    ("47", "delegar_tarea_base_comun_seguimiento"),
    ("47", "supervisar_tarea_delegada_etapa_menor_valor"),
    ("47", "supervisar_decision_delegada_preguntas_concretas"),
    ("47", "identificar_paso_limitante_jornada_desfases"),
    ("47", "agrupar_tareas_semejantes_aprovechar_preparacion"),
]

TECHO_PASOS = 44
TECHO_MIN = 67

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
    if pasos != len(ficha["pasos_accionables"]):
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
    ruta_inf = os.path.join(".v48", "informe_%s.txt" % n)
    if not os.path.exists(ruta_inf):
        break
    informe = io.open(ruta_inf, encoding="utf-8").read()
    reloj = io.open(os.path.join(".v48", "reloj_c%s.txt" % n), encoding="utf-8").read()

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
print("1. LA TANDA DE cap_04 DE LA VUELTA 48, CANDIDATO POR CANDIDATO")
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
pY = tY = puY = 0
for v, ident in YA_MINADOS:
    pasos, trans, puente = fidelidad_de(ident)
    pY += pasos
    tY += trans
    puY += puente

print("=" * 78)
print("2. PASOS INVENTADOS DE cap_04 (D.30), CON SU DENOMINADOR Y SUS TRES FILAS")
print("=" * 78)
print("| capitulo y tanda | PUENTE | pasos escritos | por ciento | tope |")
print("|---|---:|---:|---:|---:|")
print("| `cap_04`, vuelta 48, los %d de hoy | **%d** | **%d** | **%.2f** | 10 |"
      % (len(filas), tot_puente, tot_pasos, 100.0 * tot_puente / tot_pasos))
print("| `cap_04`, los %d ya minados antes de hoy (vueltas 46 y 47) | **%d** | **%d** | **%.2f** | 10 |"
      % (len(YA_MINADOS), puY, pY, 100.0 * puY / pY))
print("| **`cap_04` entero hasta hoy, los %d nodos minados** | **%d** | **%d** | **%.2f** | 10 |"
      % (len(YA_MINADOS) + len(filas), tot_puente + puY, tot_pasos + pY,
         100.0 * (tot_puente + puY) / (tot_pasos + pY)))
print("")
print("EL DENOMINADOR SE ESCRIBE AUNQUE EL NUMERADOR SEA CERO: %d pasos escritos hoy,"
      " %d en los 14 ya minados, %d en cap_04 entero." % (tot_pasos, pY, tot_pasos + pY))
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
print("4. EL RELOJ DE LA ADUANA EN SECO, Y EL TECHO QUE YA SE CUENTA EN PASOS")
print("=" * 78)
segs = [f[8] for f in filas]
media = 1.0 * sum(segs) / len(segs)
print("candidatos pasados por la aduana en esta vuelta : %d" % len(segs))
print("segundos por candidato, menor y mayor           : %d y %d" % (min(segs), max(segs)))
print("media por candidato                             : %.1f s" % media)
print("total de la tanda                               : %d s  (%.1f min)"
      % (sum(segs), sum(segs) / 60.0))
print("")
print("EL TECHO EN PASOS, que es la mitad que muerde (46.5.c) : %d pasos" % TECHO_PASOS)
print("  pasos escritos por esta tanda                       : %d" % tot_pasos)
print("  DENTRO DEL TECHO DE PASOS                           : %s"
      % ("SI" if tot_pasos <= TECHO_PASOS else "NO"))
print("EL TECHO EN MINUTOS, para poder cruzarlo (d011)       : %d min" % TECHO_MIN)
print("  minutos de aduana de esta tanda                     : %.1f min" % (sum(segs) / 60.0))
print("  DENTRO DEL TECHO DE MINUTOS                         : %s"
      % ("SI" if sum(segs) / 60.0 <= TECHO_MIN else "NO"))

segs47 = []
for n in ("01", "02", "03", "04", "05", "06"):
    reloj = io.open(os.path.join(".v47", "reloj_c%s.txt" % n), encoding="utf-8").read()
    segs47.append(int(SEG.search(reloj).group(1)))
media47 = 1.0 * sum(segs47) / len(segs47)
pasos47 = 0
for v, ident in YA_MINADOS:
    if v == "47":
        pasos47 += len(ficha_de(ident)["pasos_accionables"])
print("")
print("CONTRASTE CONTRA LA VUELTA 47, contado de sus propios relojes y no de su reporte:")
print("  media de la vuelta 47                         : %.1f s" % media47)
print("  media de la vuelta 48                         : %.1f s" % media)
print("  subida                                        : %+.1f s por candidato (%+.1f por ciento)"
      % (media - media47, 100.0 * (media - media47) / media47))
print("")
print("Y LA MISMA MEDIDA EN LA UNIDAD QUE 46.5.c ADJUDICO, QUE ES EL PASO:")
print("  pasos por candidato, vuelta 47                : %.2f" % (1.0 * pasos47 / 6))
print("  pasos por candidato, vuelta 48                : %.2f" % (1.0 * tot_pasos / len(filas)))
print("  segundos por PASO, vuelta 47                  : %.1f s" % (1.0 * sum(segs47) / pasos47))
print("  segundos por PASO, vuelta 48                  : %.1f s" % (1.0 * sum(segs) / tot_pasos))
print("")
quedan = 22 - 14 - len(filas)
print("LO QUE COSTARIA EL RESTO DE cap_04 A LA CIFRA POR PASO DE HOY:")
print("  nodos que quedan de los 22 de la frontera     : %d" % quedan)
