# -*- coding: utf-8 -*-
"""FRONTERA DE cap_07 DEL LOTE 4, corte ciego del auditor (vuelta 27).

Regla del corte, escrita ANTES de contar: en este fichero una PIEZA es una
linea suelta que no es parrafo (menos de 62 caracteres, sin punto final, sin
cabecera yaml) y que el libro imprime como titulillo. Se separan en dos clases:
  RUEDA  : el paso de la rueda, en mayusculas enteras
  PIEZA  : el titulillo de dentro de un paso
Se descartan las lineas de cita de autor (empiezan por comilla o por guion bajo)
y las lineas de dialogo (llevan comillas y signo de interrogacion).
"""
import io, re, sys
sys.stdout.reconfigure(encoding="utf-8")
RUTA = "fuentes/scott_radical_candor/cap_07.md"
lineas = io.open(RUTA, encoding="utf-8").read().split("\n")

def es_cita(t):
    return t.startswith("-") or t.startswith("“") or t.startswith('"')

ruedas, piezas, descartadas = [], [], []
dentro_yaml = False
for n, cruda in enumerate(lineas, 1):
    t = cruda.strip()
    if t == "---":
        dentro_yaml = not dentro_yaml; continue
    if dentro_yaml or not t or len(t) >= 62:
        continue
    if t.endswith(".") or t.endswith("!") or t.endswith("?"):
        descartadas.append((n, t, "acaba en signo: es prosa o dialogo")); continue
    if es_cita(t):
        descartadas.append((n, t, "cita de autor")); continue
    letras = [c for c in t if c.isalpha()]
    if letras and all(c.isupper() for c in letras):
        ruedas.append((n, t))
    else:
        piezas.append((n, t))

print("CORTE CIEGO DE cap_07 (%s)" % RUTA)
print()
print("PASOS DE LA RUEDA (linea en mayusculas): %d" % len(ruedas))
for n, t in ruedas: print("   L%-4d %s" % (n, t))
print()
print("PIEZAS (titulillo dentro de un paso): %d" % len(piezas))
for n, t in piezas: print("   L%-4d %s" % (n, t))
print()
print("DESCARTADAS: %d" % len(descartadas))
for n, t, m in descartadas: print("   L%-4d %-52s <- %s" % (n, t[:52], m))
print()
print("TOTAL DE UNIDADES DE CORTE: %d rueda + %d piezas = %d"
      % (len(ruedas), len(piezas), len(ruedas) + len(piezas)))
palabras = sum(len(l.split()) for l in lineas)
print("PALABRAS DEL FICHERO (mi cuenta): %d" % palabras)
