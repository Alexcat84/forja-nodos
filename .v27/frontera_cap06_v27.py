# -*- coding: utf-8 -*-
"""CORTE CIEGO DE cap_06, segunda pasada: el cuerpo del capitulo y sus piezas.

Lo que la primera pasada enseño y esta corrige, escrito ANTES de recontar:
  1. `PART II`, `TOOLS & TECHNIQUES` y `RELATIONSHIPS` (L421 en adelante) NO son
     del capitulo: son la portadilla de la parte siguiente. El CUERPO acaba en
     la ultima linea antes de L421.
  2. `L9` es el subtitulo del capitulo, no una pieza de dentro.
  3. `L305` es la cita de Aristoteles con comillas tipograficas de cierre, que
     la regla de la primera pasada no cazo por empezar en comilla de cierre.
  4. En PERSUADE el libro pone TRES rotulos de retorica (Emotion, Credibility,
     Logic) y cuelga de cada uno UN titulillo. Se publican las dos cuentas: con
     los rotulos y sin ellos.
"""
import io, sys
sys.stdout.reconfigure(encoding="utf-8")
RUTA = "fuentes/scott_radical_candor/cap_06.md"
lineas = io.open(RUTA, encoding="utf-8").read().split("\n")
FIN_CUERPO = 999          # L421 = "PART II"
INICIO_CUERPO = 8         # tras el yaml
ROTULOS_RETORICA = {"Emotion", "Credibility", "Logic"}

cuerpo = lineas[INICIO_CUERPO - 1:FIN_CUERPO - 1]
palabras_cuerpo = sum(len(l.split()) for l in cuerpo)
palabras_fichero = sum(len(l.split()) for l in lineas)

def es_titulillo(t):
    if not t or len(t) >= 62: return False
    if t.endswith(".") or t.endswith("!") or t.endswith("?"): return False
    if t[0] in "-“”\"": return False
    return True

rueda, piezas, rotulos = [], [], []
for n, cruda in enumerate(lineas, 1):
    if n < INICIO_CUERPO or n >= FIN_CUERPO: continue
    t = cruda.strip()
    if not es_titulillo(t): continue
    letras = [c for c in t if c.isalpha()]
    if letras and all(c.isupper() for c in letras):
        rueda.append((n, t))
    elif t in ROTULOS_RETORICA:
        rotulos.append((n, t))
    else:
        piezas.append((n, t))

sub = [x for x in rueda if x[0] == 9]
rueda = [x for x in rueda if x[0] != 9]
piezas = [x for x in piezas if x[0] != 9]

print("CORTE CIEGO DE cap_06, SEGUNDA PASADA")
print("  cuerpo del capitulo : L%d a L%d" % (INICIO_CUERPO, FIN_CUERPO - 1))
print("  palabras del cuerpo : %d" % palabras_cuerpo)
print("  palabras del fichero: %d" % palabras_fichero)
print()
print("A. ROTULOS DE SECCION EN MAYUSCULAS: %d" % len(rueda))
for n, t in rueda: print("   L%-4d %s" % (n, t))
print()
print("B. ROTULOS DE RETORICA (cascara, cuelgan un titulillo cada uno): %d" % len(rotulos))
for n, t in rotulos: print("   L%-4d %s" % (n, t))
print()
print("C. TITULILLOS DE CUERPO, que son las piezas que pueden dar nodo: %d" % len(piezas))
for n, t in piezas: print("   L%-4d %s" % (n, t))
print()
print("MI CORTE: %d piezas de cuerpo (C), bajo %d rotulos de seccion (A)."
      % (len(piezas), len(rueda)))
print("          con los %d rotulos de retorica contados aparte serian %d."
      % (len(rotulos), len(piezas) + len(rotulos)))
