# -*- coding: utf-8 -*-
"""Verificacion del auditor de la vuelta 21 sobre lo que el REPORTE de la
vuelta 20 publica. Cero escrituras: solo mide y compara."""
import io, json, os, re, subprocess, sys

RAIZ = os.path.dirname(os.path.abspath(__file__))
LOTE = os.path.join(RAIZ, "cuarentena", "scott_radical_candor")
FUENTES = os.path.join(RAIZ, "fuentes", "scott_radical_candor")

def leer(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return f.read()

def cuerpo_palabras(cap):
    """sed -n '8,$p' <fichero> | wc -w, reproducido en python."""
    lineas = leer(os.path.join(FUENTES, cap)).split("\n")
    return len(" ".join(lineas[7:]).split())

print("=== 1. CUERPOS POR CAPITULO (sed -n '8,$p' | wc -w) ===")
caps = sorted(f for f in os.listdir(FUENTES) if f.startswith("cap_"))
total_hasta_09 = 0
total_10_14 = 0
for c in caps:
    w = cuerpo_palabras(c)
    n = c[4:6]
    if n <= "09":
        total_hasta_09 += w
    else:
        total_10_14 += w
    print("  %s  %6d" % (c, w))
print("  cap_00 a cap_09 : %d" % total_hasta_09)
print("  cap_10 a cap_14 : %d" % total_10_14)
print("  libro entero    : %d" % (total_hasta_09 + total_10_14))

print()
print("=== 2. LA BANDEJA DEL LOTE 4: candidatos y pasos ===")
fichs = sorted(f for f in os.listdir(LOTE) if f.endswith(".json"))
por_cap = {}
pasos_por_id = {}
for f in fichs:
    d = json.loads(leer(os.path.join(LOTE, f)))
    pasos = len(d.get("pasos", []))
    pasos_por_id[d.get("id", f)] = pasos
    txt = leer(os.path.join(LOTE, f))
    m = re.search(r"UNIDAD DE ORIGEN:[^\n]*?(cap_\d\d)\.md", txt)
    if not m:
        m = re.search(r"(cap_\d\d)", txt)
    cap = m.group(1) if m else "SIN"
    por_cap.setdefault(cap, [0, 0, []])
    por_cap[cap][0] += 1
    por_cap[cap][1] += pasos
    por_cap[cap][2].append(d.get("id", f))
tc = tp = 0
for cap in sorted(por_cap):
    c, p, ids = por_cap[cap]
    tc += c; tp += p
    print("  %s  cand=%-3d pasos=%-4d" % (cap, c, p))
print("  TOTAL cand=%d pasos=%d   (ficheros en la carpeta: %d)" % (tc, tp, len(fichs)))
print("  fila de residuo SIN: %d %s" % (por_cap.get("SIN", [0,0,[]])[0], por_cap.get("SIN", [0,0,[]])[2]))

print()
print("=== 3. LOS CINCO DE HOY, SUS PASOS Y SUS ATRIBUCIONES ===")
cinco = ["revisar_critica_mujer_agresiva_cuatro_tacticas",
         "responder_critica_abrasiva_cuatro_reglas",
         "entregar_evaluacion_formal_desempenio_nueve_consejos",
         "conducir_reuniones_salto_nivel_diez_reglas",
         "resolver_dudas_frecuentes_reuniones_salto_nivel"]
suma = 0
for cid in cinco:
    d = json.loads(leer(os.path.join(LOTE, cid + ".json")))
    npas = len(d.get("pasos", []))
    natr = len(d.get("atribuciones", []))
    suma += npas
    print("  %-55s pasos=%-3d atribuciones=%d" % (cid, npas, natr))
print("  suma de pasos de los cinco: %d" % suma)

print()
print("=== 4. LOS TRES CANDIDATOS CON MAS PASOS DEL LOTE ===")
for cid, n in sorted(pasos_por_id.items(), key=lambda x: -x[1])[:4]:
    print("  %-55s %d" % (cid, n))

print()
print("=== 5. EL GRAFO: aristas, extremos, cruces de libro, nodos de scott ===")
nodos = [json.loads(l) for l in leer(os.path.join(RAIZ, "dataset", "nodos.jsonl")).splitlines() if l.strip()]
libro_de = {}
for n in nodos:
    fs = n.get("fuentes") or []
    clave = fs[0].get("clave") if fs and isinstance(fs[0], dict) else None
    libro_de[n["id"]] = clave
extremos = 0
pares = set()
cruzan = 0
for n in nodos:
    for a in (n.get("aristas") or []):
        destino = a.get("hacia") if isinstance(a, dict) else a
        extremos += 1
        pares.add(tuple(sorted([n["id"], destino])))
        if libro_de.get(destino) and libro_de.get(n["id"]) != libro_de.get(destino):
            cruzan += 1
print("  nodos                                   : %d" % len(nodos))
print("  nodos con fuente scott_radical_candor   : %d" % sum(1 for v in libro_de.values() if v == "scott_radical_candor"))
print("  extremos de arista (ida y vuelta)       : %d" % extremos)
print("  aristas distintas (pares)               : %d" % len(pares))
print("  extremos que cruzan de libro            : %d" % cruzan)
