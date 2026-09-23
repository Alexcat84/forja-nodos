# pares.py: saca los pares (candidato, vecino) de un informe de aduana.
# CERO CONSTANTES TECLEADAS: todo sale del texto que se le pasa.
import sys, re
def pares(rutas):
    out = []
    actual = None
    for r in rutas:
        for linea in open(r, encoding='utf-8', errors='replace'):
            m = re.match(r'^\[(ENTRARIA|BLOQUEARIA|CAERIA)\]\s+(\S+)', linea)
            if m:
                actual = m.group(2); continue
            m = re.match(r'^\s+vecino (\S+)\s', linea)
            if m and actual:
                out.append((actual, m.group(1)))
    return out
a = pares(sys.argv[1:2])
b = pares(sys.argv[2:])
sa, sb = set(a), set(b)
print("fichero A :", sys.argv[1], " pares:", len(a), " distintos:", len(sa))
print("fichero B :", " ".join(sys.argv[2:]), " pares:", len(b), " distintos:", len(sb))
print("solo en A :", len(sa - sb))
for p in sorted(sa - sb): print("   ", p[0], "->", p[1])
print("solo en B :", len(sb - sa))
for p in sorted(sb - sa): print("   ", p[0], "->", p[1])
