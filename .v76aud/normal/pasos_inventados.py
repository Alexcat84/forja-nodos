# ACTA 75: PASOS INVENTADOS POR CAPITULO de las 22 de Gerber, una fila por capitulo (8.2), por los dos lados: su marca sobre el texto
# de AL ABRIR (.v76ext/fidelidad.tsv) y la mia sobre el texto de HOY, despues de sus correcciones (.v76aud/fidelidad.tsv, con mi
# unica D adjudicada T en la 75.3). El capitulo sale de mi columna capitulo. Solo lee. Suma en cada reparto (R7).
import collections, io, re, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
cap = {}; mia = {}
for l in io.open(".v76aud/fidelidad.tsv", encoding="utf-8"):
    c = l.rstrip("\r\n").split("\t")
    if c[0] == "id" or len(c) < 4: continue
    cap[(c[0], int(c[1]))] = c[3]; mia[(c[0], int(c[1]))] = "T" if c[2] == "D" else c[2]
suya = {}
for l in io.open(".v76ext/fidelidad.tsv", encoding="utf-8"):
    if l.startswith("#") or not l.strip(): continue
    c = [x.strip() for x in l.split("|")]
    suya[(c[0], int(c[1]))] = c[2]
pas = collections.Counter(); ps = collections.Counter(); pm = collections.Counter(); cand = collections.defaultdict(set)
for k, ch in cap.items():
    pas[ch] += 1; cand[ch].add(k[0])
    ps[ch] += suya[k] == "P"; pm[ch] += mia[k] == "P"
for ch in sorted(pas):
    t = [l for l in io.open("fuentes/gerber_emyth/%s.md" % ch, encoding="utf-8") if l.startswith("titulo_textual")]
    print("%s | %s | candidatos %d | pasos %d | PUENTE sobre el texto de al abrir %d = %s por ciento | PUENTE en el texto de hoy %d" % (
        ch, t[0].split(":", 1)[1].strip() if t else "-", len(cand[ch]), pas[ch], ps[ch], ("%.2f" % (100.0 * ps[ch] / pas[ch])).replace(".", ","), pm[ch]))
print("lote: pasos %d | PUENTE al abrir %d = %s por ciento | PUENTE hoy %d | suma de pasos por capitulo: %d" % (
    len(cap), sum(ps.values()), ("%.2f" % (100.0 * sum(ps.values()) / len(cap))).replace(".", ","), sum(pm.values()), sum(pas.values())))
