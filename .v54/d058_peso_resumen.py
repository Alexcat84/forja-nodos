# -*- coding: utf-8 -*-
"""d058 RELEIDA SOBRE LA BANDEJA ENTERA, NO SOBRE NUEVE (D.59).

Mide, con la MISMA funcion que usa la aduana (src.comun.texto_comparable), que
proporcion del texto que compara la senial 1 es resumen_teorico y que
proporcion son los pasos. Cada media lleva su numerador y su denominador
NOMBRADOS.

    python .v54/d058_peso_resumen.py [carpeta]
"""
import json
import os
import sys

sys.path.insert(0, os.path.abspath("."))
from src import comun  # noqa: E402

CARPETA = sys.argv[1] if len(sys.argv) > 1 else "cuarentena/grove_high_output"


def trozo(texto):
    return len(comun.normalizar_texto(texto or ""))


def main():
    filas = []
    for nombre in sorted(os.listdir(CARPETA)):
        if not nombre.endswith(".json"):
            continue
        o = json.load(open(os.path.join(CARPETA, nombre), encoding="utf-8"))
        entero = len(comun.texto_comparable(o))
        if not entero:
            continue
        resumen = trozo(o.get("resumen_teorico"))
        pasos = sum(trozo(p) for p in (o.get("pasos_accionables") or []))
        filas.append((o.get("id"), entero, resumen, pasos,
                      100.0 * resumen / entero, 100.0 * pasos / entero))

    filas.sort(key=lambda f: -f[4])
    print("d058 RELEIDA: peso del resumen_teorico en el texto que compara la senial 1")
    print("  carpeta                               : %s" % CARPETA)
    print("  fichas medidas                        : %d" % len(filas))
    print("  funcion usada                         : src.comun.texto_comparable")
    print()
    print("  %-56s %7s %7s %7s" % ("id", "total", "% resu", "% pasos"))
    for f in filas:
        print("  %-56s %7d %7.1f %7.1f" % (f[0], f[1], f[4], f[5]))
    print()
    if filas:
        num_r = sum(f[2] for f in filas)
        num_p = sum(f[3] for f in filas)
        den = sum(f[1] for f in filas)
        print("  EL PESO DEL RESUMEN SOBRE LA BANDEJA ENTERA : %.1f por ciento"
              % (100.0 * num_r / den))
        print("    numerador   %8d  caracteres normalizados de resumen_teorico, sumados" % num_r)
        print("    denominador %8d  caracteres normalizados de texto_comparable, sumados" % den)
        print("  EL PESO DE LOS PASOS SOBRE LA BANDEJA ENTERA: %.1f por ciento"
              % (100.0 * num_p / den))
        print("    numerador   %8d  caracteres normalizados de pasos_accionables, sumados" % num_p)
        print("    denominador %8d  caracteres normalizados de texto_comparable, sumados" % den)
        print()
        print("  LA BANDA, que es lo que d058 publica (minimo y maximo, no media):")
        print("    menor %% de resumen : %.1f  (%s)" % (filas[-1][4], filas[-1][0]))
        print("    mayor %% de resumen : %.1f  (%s)" % (filas[0][4], filas[0][0]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
