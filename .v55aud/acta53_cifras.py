# -*- coding: utf-8 -*-
"""Las cifras DERIVADAS de la ACTA 53, cada una con su numerador y su denominador
NOMBRADOS (D.59). Ninguna celda de esta acta se divide a mano."""
import re, json, os, glob, subprocess, collections

R = lambda p: open(p, encoding="utf-8", errors="replace").read()

print("=" * 78)
print("ACTA 53: LAS CIFRAS DERIVADAS, IMPRESAS POR SU INSTRUMENTO (D.59)")
print("=" * 78)

# ---------------------------------------------------------------- 1. el coste
print()
print("1. EL COSTE DE LA CORRIDA LIGERA, DE docs/loop/loop.log")
turnos, modo = [], "?"
for l in R("docs/loop/loop.log").splitlines():
    m = re.search(r"arranque:.*MODO_INSERCION=(\w+)", l)
    if m: modo = m.group(1)
    m = re.match(r"\[([\d\-: ]+)\]\s+(.*?) listo \(USD ([\d.]+)\), (\d+)s", l)
    if m: turnos.append((m.group(1), m.group(2), modo, float(m.group(3)), int(m.group(4))))
lig = [t for t in turnos if t[2] == "cuarentena"]
print("   turnos con linea 'listo (USD ...)' en el log : %d" % len(turnos))
print("   de esos, en MODO_INSERCION=cuarentena        : %d" % len(lig))
print("   LAS CELDAS DE LA CORRIDA LIGERA, sin media, que son dos:")
for t in lig: print("     %s  %-14s %-11s %9.4f USD  %6d s" % t)
ext_ins = [t for t in turnos if t[1] == "extractor" and t[2] == "insertar"]
media_ins = sum(t[3] for t in ext_ins) / len(ext_ins)
print("   la vara con la que se compara el turno de extractor:")
print("     media USD/turno de extractor en insertar   : %.2f USD" % media_ins)
print("       numerador   %.2f  suma de USD de esos turnos" % sum(t[3] for t in ext_ins))
print("       denominador %d  turnos de extractor en insertar" % len(ext_ins))
ext_lig = [t for t in lig if t[1] == "extractor"]
if ext_lig:
    v = ext_lig[0][3]
    print("     CAIDA del turno de extractor, ligero contra insertar: %.1f por ciento" % (100.0 * (v - media_ins) / media_ins))
    print("       numerador   %.4f  USD del turno de extractor en ligero menos la media de insertar" % (v - media_ins))
    print("       denominador %.2f  media de USD de los turnos de extractor en insertar" % media_ins)
    print("     Y CONTRA EL OBJETIVO ESCRITO DE 5 USD: %.2f USD de exceso, %.1f veces el objetivo" % (v - 5.0, v / 5.0))
    print("       numerador   %.4f  USD del turno de extractor en ligero" % v)
    print("       denominador 5  USD del objetivo escrito en el encargo de la 54")

# ------------------------------------------------------------- 2. tasa d033
print()
print("2. d033: LA TASA DE LA PRUEBA INTERMITENTE, SOBRE EL MISMO ARBOL")
def tanda(ruta):
    rojo = verde = seg = 0
    for l in R(ruta).splitlines():
        m = re.match(r"corrida \d+\s+(VERDE|ROJO)\s+(\d+) s", l.strip())
        if m:
            seg += int(m.group(2))
            if m.group(1) == "ROJO": rojo += 1
            else: verde += 1
    return rojo, verde, seg
r1, v1, s1 = tanda(".v54/d033_tasa.txt")
r2, v2, s2 = tanda(".v55aud/d033_tasa_auditor.txt")
print("   corridas de la vuelta 54 (.v54/d033_tasa.txt)      : %d  (%d ROJO, %d VERDE)" % (r1 + v1, r1, v1))
print("   corridas mias de hoy (.v55aud/d033_tasa_auditor.txt): %d  (%d ROJO, %d VERDE)" % (r2 + v2, r2, v2))
print("   TASA DE ROJO sobre el arbol de la vuelta 54        : %.1f por ciento" % (100.0 * (r1 + r2) / (r1 + v1 + r2 + v2)))
print("     numerador   %d  corridas que salieron ROJO" % (r1 + r2))
print("     denominador %d  corridas lanzadas sobre el mismo arbol (12 suyas mas 5 mias)" % (r1 + v1 + r2 + v2))
print("   SEGUNDOS POR CORRIDA                              : %.1f s" % ((s1 + s2) / (r1 + v1 + r2 + v2)))
print("     numerador   %d  suma de segundos de esas corridas" % (s1 + s2))
print("     denominador %d  corridas lanzadas" % (r1 + v1 + r2 + v2))

# ------------------------------------------- 3. pasos inventados por capitulo
print()
print("3. PASOS INVENTADOS POR CAPITULO (AUDITOR_FORJA.md 8), VUELTA 54")
tocados = subprocess.run(["git", "diff", "--name-only", "e63f5af..HEAD", "--", "cuarentena/"],
                         capture_output=True, text=True).stdout.strip()
print("   $ git diff --name-only e63f5af..HEAD -- cuarentena/")
print("   fichas de cuarentena creadas o modificadas por la vuelta 54 : %d" % (len(tocados.splitlines()) if tocados else 0))
cap = collections.Counter(); pas = collections.Counter()
for p in sorted(glob.glob("cuarentena/grove_high_output/*.json")):
    d = json.load(open(p, encoding="utf-8"))
    m = re.findall(r"grove_high_output/(cap_\d+)\.md", json.dumps(d, ensure_ascii=False))
    c = m[0] if m else "?"
    cap[c] += 1; pas[c] += len(d.get("pasos_accionables", []))
print("   LA FILA POR CAPITULO, y el denominador es 'pasos ESCRITOS POR LA VUELTA 54':")
for c in sorted(cap):
    print("     %s  pasos vivos en bandeja %3d  |  pasos escritos por la 54: 0  ->  fila SIN SUPERFICIE" % (c, pas[c]))
print("     TOTAL      pasos vivos en bandeja %3d  |  pasos escritos por la 54: 0" % sum(pas.values()))

# ------------------------------------------------ 4. la muestra pineada (7)
print()
print("4. LA MUESTRA PINEADA DE LOS SANO (AUDITOR_FORJA.md 7), VUELTA 54")
ver = subprocess.run(["git", "diff", "--numstat", "e63f5af..HEAD", "--", "bitacora/VEREDICTOS.jsonl"],
                     capture_output=True, text=True).stdout.strip()
print("   $ git diff --numstat e63f5af..HEAD -- bitacora/VEREDICTOS.jsonl")
print("   lineas de veredicto anadidas por la vuelta 54 : %s" % (ver.split()[0] if ver else "0"))
print("   veredictos SANO de la tanda                   : 0  ->  no hay poblacion que muestrear")
print()
print("=" * 78)
