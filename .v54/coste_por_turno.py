# -*- coding: utf-8 -*-
"""EL COSTE POR TURNO, LEIDO DEL LOG Y NO TECLEADO (D.59).

Imprime cada media CON SU NUMERADOR Y SU DENOMINADOR NOMBRADOS. No teclea
ninguna cifra derivada: todas salen de las lineas que el arnes escribio en
docs/loop/loop.log, y el reparto por regimen sale de la linea de arranque
'MODO_INSERCION=<x>' que precede a cada turno.

    python .v54/coste_por_turno.py
"""
import re
import sys

LOG = "docs/loop/loop.log"

ARRANQUE = re.compile(r"^\[([\d\- :]+)\] arranque: rama \S+, MODO_INSERCION=(\w+)")
LISTO = re.compile(r"^\[([\d\- :]+)\] (extractor|auditor ciego|auditor) listo "
                   r"\(USD ([\d.]+)\), (\d+)s")


def leer():
    modo = None
    turnos = []
    with open(LOG, encoding="utf-8", errors="replace") as mano:
        for cruda in mano:
            golpe = ARRANQUE.match(cruda)
            if golpe:
                modo = golpe.group(2)
                continue
            golpe = LISTO.match(cruda)
            if golpe:
                turnos.append({"cuando": golpe.group(1), "rol": golpe.group(2),
                               "usd": float(golpe.group(3)),
                               "s": int(golpe.group(4)), "modo": modo})
    return turnos


def media(nombre, num, num_nombre, den, den_nombre, unidad):
    if not den:
        print("  %-34s SIN DENOMINADOR: %s = 0, no se publica media"
              % (nombre, den_nombre))
        return
    print("  %-34s %8.2f %s" % (nombre, num / den, unidad))
    print("  %-34s   numerador   %10.2f  %s" % ("", num, num_nombre))
    print("  %-34s   denominador %10d  %s" % ("", den, den_nombre))


def main():
    turnos = leer()
    print("COSTE POR TURNO, de %s" % LOG)
    print("  turnos con linea 'listo (USD ...)' en el log : %d" % len(turnos))
    print()
    print("  LOS DIEZ ULTIMOS, UNO POR LINEA (sin media: son las celdas)")
    print("    %-19s  %-14s %-10s %9s %7s" % ("cuando", "rol", "modo", "USD", "s"))
    for t in turnos[-10:]:
        print("    %-19s  %-14s %-10s %9.4f %7d"
              % (t["cuando"], t["rol"], t["modo"] or "?", t["usd"], t["s"]))
    print()
    for modo in ("insertar", "cuarentena"):
        for rol in ("extractor", "auditor", "auditor ciego"):
            faja = [t for t in turnos if t["modo"] == modo and t["rol"] == rol]
            media("%s / %s USD por turno" % (modo, rol),
                  sum(t["usd"] for t in faja), "suma de USD de esos turnos",
                  len(faja), "turnos de ese rol y ese modo en el log", "USD")
    print()
    faja = [t for t in turnos if t["modo"] == "insertar" and t["rol"] == "extractor"]
    if faja:
        print("  EL CONTRASTE QUE PRESUPUESTA EL OBJETIVO DE 5 USD")
        media("extractor en insertar, USD/turno",
              sum(t["usd"] for t in faja), "suma de USD de los turnos de extractor en insertar",
              len(faja), "turnos de extractor en insertar", "USD")
        print("  %-34s %8.4f %s" % ("el mas barato de esos turnos",
                                    min(t["usd"] for t in faja), "USD"))
        print("  %-34s %8.4f %s" % ("el mas caro de esos turnos",
                                    max(t["usd"] for t in faja), "USD"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
