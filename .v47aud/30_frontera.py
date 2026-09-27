import re, sys
REP = "docs/loop/REPORTE.md"
SRC = "fuentes/grove_high_output/cap_04.md"
lines = open(REP, encoding="utf-8").read().split("\n")
# tabla HH.2.c: desde la fila L9 a L13 (indice 43935-1) hasta la fila total
start = 43935 - 1
filas = []
i = start
while True:
    l = lines[i]
    if l.startswith("| | **8846**"):
        total_row = l
        break
    m = re.match(r"^\| `L(\d+) a L(\d+)` \| (\d+) \| \*\*(\d+)\*\* \|", l)
    if not m:
        print("NO CASA la linea", i+1, l[:80]); sys.exit(1)
    filas.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))))
    i += 1

src = open(SRC, encoding="utf-8").read().split("\n")  # src[n-1] es la linea n
def palabras(a, b):
    return sum(len(src[n-1].split()) for n in range(a, b+1))

print("filas de la tabla                      :", len(filas))
print("suma de la columna de palabras         :", sum(f[2] for f in filas))
print("suma de la columna de nodos            :", sum(f[3] for f in filas))
print("filas que dan cero nodos               :", sum(1 for f in filas if f[3] == 0))
dif = [(f[0], f[1], f[2], palabras(f[0], f[1])) for f in filas if palabras(f[0], f[1]) != f[2]]
print("filas cuya cuenta de palabras DIFIERE  :", len(dif), dif[:5])
# cobertura
cubiertas = set()
solapes = []
for a, b, _, _ in filas:
    for n in range(a, b+1):
        if n in cubiertas: solapes.append(n)
        cubiertas.add(n)
cuerpo = [n for n in range(9, len(src)+1) if src[n-1].strip()]
sin_cubrir = [n for n in cuerpo if n not in cubiertas]
print("lineas con contenido tras la cabecera  :", len(cuerpo))
print("lineas con contenido NO cubiertas      :", len(sin_cubrir), sin_cubrir[:10])
print("SOLAPES                                :", len(solapes), solapes[:10])
print("cuerpo medido aparte (L9 al final)     :", palabras(9, len(src)))
print("cabecera (L1 a L7)                     :", palabras(1, 7))
print("fichero entero                         :", sum(len(l.split()) for l in src))
print("--- la fila de total que la tabla publica:")
print(total_row[:110])
