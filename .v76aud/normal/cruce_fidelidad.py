# ACTA 75: mi fidelidad sellada (.v76aud/fidelidad.tsv, sobre el texto de HOY) contra la suya (.v76ext/fidelidad.tsv, marcada
# sobre el texto de AL ABRIR), paso a paso. Solo lee. Toda linea que reparte trae su suma (R7).
import collections, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
def suyas():
    d = {}
    for l in open(".v76ext/fidelidad.tsv", encoding="utf-8"):
        if l.startswith("#") or not l.strip():
            continue
        c = [x.strip() for x in l.split("|")]
        d[(c[0], int(c[1]))] = (c[2], c[3], " | ".join(c[4:]))
    return d
def mias():
    d = {}
    for l in open(".v76aud/fidelidad.tsv", encoding="utf-8"):
        c = l.rstrip("\r\n").split("\t")
        if c[0] == "id" or l.startswith("#") or len(c) < 4:
            continue
        d[(c[0], int(c[1]))] = (c[2], c[4] if len(c) > 4 else "")
    return d
S, M = suyas(), mias()
print("filas suyas:", len(S), "| mias:", len(M), "| en las dos:", len(set(S) & set(M)),
      "| solo suyas:", sorted(set(S) - set(M)), "| solo mias:", sorted(set(M) - set(S)))
par = collections.Counter()
for k in sorted(set(S) & set(M)):
    par[(S[k][0], M[k][0])] += 1
print("marca suya, marca mia:", dict(par), "| suma:", sum(par.values()))
for k in sorted(set(S) & set(M)):
    if S[k][0] != M[k][0]:
        print("  DIFIEREN", k[0], "paso", k[1], "| suya", S[k][0], S[k][1], "| mia", M[k][0], M[k][1])
P = collections.Counter()
for k, v in S.items():
    if v[0] == "P":
        P[k[0]] += 1
print("sus P por ficha:", dict(P), "| suma:", sum(P.values()))
