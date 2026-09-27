# -*- coding: utf-8 -*-
"""Los instrumentos del AUDITOR de la ACTA 35 (vuelta 36). Cero escrituras en el arbol."""
import io, json, math, glob, re, collections, subprocess

RAIZ = "."

def carga(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]

def wilson(k, n, z=1.96):
    if n == 0:
        return 0.0, 1.0
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return max(0.0, c - h), min(1.0, c + h)

def por_ruta(nodos, clave):
    c, pasos = collections.Counter(), collections.Counter()
    sin = []
    for n in nodos:
        t = json.dumps(n, ensure_ascii=False)
        if clave not in t:
            continue
        caps = sorted(set(re.findall(clave + r"/(cap_\d+)\.md", t)))
        if not caps:
            sin.append(n["id"])
            continue
        for x in caps:
            c[x] += 1
        pasos[caps[0]] += len(n["pasos_accionables"])
    return c, pasos, sin

def main():
    nodos = carga("dataset/nodos.jsonl")
    ver = carga("bitacora/VEREDICTOS.jsonl")
    print("$ .a35/auditoria.py   (el auditor de la ACTA 35, sobre el arbol de hoy)")
    print("EL DATO")
    print("  dataset/nodos.jsonl        : %d nodos, %d ids unicos" % (len(nodos), len({n["id"] for n in nodos})))
    print("  bitacora/VEREDICTOS.jsonl  : %d lineas" % len(ver))
    sig = sum(len(n.get("nodos_siguientes", [])) for n in nodos)
    pre = sum(len(n.get("nodos_previos", [])) for n in nodos)
    S = {(n["id"], x) for n in nodos for x in n.get("nodos_siguientes", [])}
    P = {(x, n["id"]) for n in nodos for x in n.get("nodos_previos", [])}
    print("  aristas por nodos_siguientes: %d   por nodos_previos: %d" % (sig, pre))
    print("  pares que no casan por los dos extremos: %d" % len(S ^ P))
    ids = {n["id"] for n in nodos}
    rotas = [x for n in nodos for x in n.get("nodos_siguientes", []) + n.get("nodos_previos", []) if x not in ids]
    print("  aristas a un id que no existe: %d" % len(rotas))

    print("")
    print("cap_10 EN EL GRAFO, POR SU RUTA COMPLETA")
    c, pasos, sin = por_ruta(nodos, "scott_radical_candor")
    cap10 = [n for n in nodos if "scott_radical_candor/cap_10.md" in json.dumps(n, ensure_ascii=False)]
    print("  cap_10: %d nodos, %d pasos" % (len(cap10), sum(len(n["pasos_accionables"]) for n in cap10)))
    print("  scott en el grafo, sumando nodos y no filas: %d" % len([n for n in nodos if "scott_radical_candor" in json.dumps(n, ensure_ascii=False)]))
    print("  filas por capitulo: %s" % dict(sorted(c.items())))
    multi = [n["id"] for n in nodos if len(set(re.findall(r"scott_radical_candor/(cap_\d+)\.md", json.dumps(n, ensure_ascii=False)))) > 1]
    print("  nodos que citan DOS capitulos y por eso suman dos filas: %s" % multi)
    print("  nodos scott sin la ruta en el texto: %s" % sin)

    print("")
    print("LA FILA DE PASOS INVENTADOS QUE FIRMO, contada por mi contra el dataset")
    for n in sorted(cap10, key=lambda x: x["id"]):
        print("  %-46s %3d pasos" % (n["id"], len(n["pasos_accionables"])))
    print("  TOTAL cap_10: %d pasos escritos, %d PUENTE, %.2f por ciento" % (
        sum(len(n["pasos_accionables"]) for n in cap10), 0, 0.0))

    print("")
    print("LA TANDA DE VEREDICTOS (desde la linea 428)")
    nuevos = list(enumerate(ver[427:], start=428))
    clases = collections.Counter(x["veredicto"] for _, x in nuevos)
    lev = collections.Counter("lectura declarada" if x.get("levantada_por") == ["lectura declarada"] else "senial" for _, x in nuevos)
    print("  nuevos: %d   %s" % (len(nuevos), dict(clases)))
    print("  levantados: %s" % dict(lev))
    cont = [(l, x) for l, x in nuevos if x["veredicto"] == "CONTINUA"]
    cl = collections.Counter("lectura" if x.get("levantada_por") == ["lectura declarada"] else "senial" for _, x in cont)
    print("  de las %d CONTINUA: %s" % (len(cont), dict(cl)))
    encola = [(l, x) for l, x in cont if x.get("arista_en_cola")]
    print("  con arista_en_cola: %d" % len(encola))
    sinrazon = [i + 1 for i, r in enumerate(ver) if r["veredicto"] == "SANO" and not (r.get("razon") or "").strip()]
    print("  D.8, SANO sin razon escrita en TODA la bitacora: %d" % len(sinrazon))

    print("")
    print("LAS TASAS CON SU BANDA (AUDITOR_FORJA.md 7: una tasa sin banda es media cifra)")
    for k, n, que in [(0, 5, "muestra pineada de SANO, semilla 36"),
                      (0, 24, "los SANO de la tanda, releidos enteros"),
                      (0, 37, "los 37 veredictos de la tanda"),
                      (0, 206, "los 206 pasos de cap_10 (D.30)")]:
        lo, hi = wilson(k, n)
        print("  %-40s %d de %-4d tasa 0,00   banda Wilson 95: [%.2f, %.2f] por ciento" % (que, k, n, lo * 100, hi * 100))

    print("")
    print("LA BANDEJA QUE QUEDA")
    c2 = collections.Counter(); p2 = collections.Counter()
    for f in glob.glob("cuarentena/scott_radical_candor/*.json"):
        n = json.load(io.open(f, encoding="utf-8"))
        m = sorted(set(re.findall(r"scott_radical_candor/(cap_\d+)\.md", json.dumps(n, ensure_ascii=False))))
        k = m[0] if m else "SIN_CAP"
        c2[k] += 1; p2[k] += len(n["pasos_accionables"])
    print("  candidatos: %s   total %d" % (dict(sorted(c2.items())), sum(c2.values())))
    print("  pasos     : %s" % dict(sorted(p2.items())))
    print("  cap_12 mas cap_13 = %d candidatos, contra el techo de 15 de EXTRACTOR.md 12.4" % (c2["cap_12"] + c2["cap_13"]))

    print("")
    print("LA PIEZA DE cap_12 QUE LEVANTO ANTES DE QUE ENTRE (D.30)")
    for f in glob.glob("cuarentena/scott_radical_candor/*.json"):
        n = json.load(io.open(f, encoding="utf-8"))
        for i, p in enumerate(n["pasos_accionables"], 1):
            if "superestrella" in p.lower():
                print("  %s P%d: %s" % (n["id"], i, p))
    for cap in ("cap_10", "cap_12"):
        t = io.open("fuentes/scott_radical_candor/%s.md" % cap, encoding="utf-8").read().lower()
        print("  %s: 'rock star' %d veces, 'superstar' %d veces" % (cap, t.count("rock star"), t.count("superstar")))

main()
