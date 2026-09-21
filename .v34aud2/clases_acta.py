# -*- coding: utf-8 -*-
"""MI TABLA CIEGA CONTRA LA BITACORA DE HOY, COMPROBADA Y NO RECOPIADA.

Lee la tabla de la seccion 7 de docs/loop/APERTURA_CIEGA.md (que el arnes SELLO antes
de exponerme el reporte) y la enfrenta linea a linea con bitacora/VEREDICTOS.jsonl.
NO reproduce la tabla: la comprueba. D.47 dice que lo que el registro ya dice no se
repite, y esa tabla ya esta sellada.
"""
import io, json, re, sys
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

FILA = re.compile(r"^\|\s*(\d+)\s*\|(.+)$")
apertura = io.open("docs/loop/APERTURA_CIEGA.md", encoding="utf-8").read().split("\n")
ver = [json.loads(l) for l in io.open("bitacora/VEREDICTOS.jsonl", encoding="utf-8") if l.strip()]

mias, coinciden, discrepan, faltan = 0, 0, [], []
for linea in apertura:
    m = FILA.match(linea.strip())
    if not m:
        continue
    numero = int(m.group(1))
    if not 411 <= numero <= 423:
        continue
    celdas = [c.strip().strip("*").strip("`") for c in m.group(2).split("|")]
    candidato, vecino, mi_clase = celdas[0], celdas[1], celdas[3].strip("*").strip()
    fila = ver[numero - 1]
    mias += 1
    if fila["candidato"] != candidato or fila["vecino"] != vecino:
        faltan.append(numero)
    elif fila["veredicto"] == mi_clase:
        coinciden += 1
    else:
        discrepan.append((numero, mi_clase, fila["veredicto"]))

print("lineas de mi tabla ciega sellada  : %d" % mias)
print("el par (candidato, vecino) cuadra : %d de %d" % (mias - len(faltan), mias))
print("MI CLASE es la de la bitacora     : %d" % coinciden)
print("DISCREPAN                         : %d  %s" % (len(discrepan), discrepan or ""))
sin_razon = [i for i in range(411, 424) if not (ver[i - 1].get("razon") or "").strip()]
print("lineas de la tanda SIN razon escrita (D.8): %d  %s" % (len(sin_razon), sin_razon or ""))
sanos = [i for i in range(411, 424) if ver[i - 1]["veredicto"] == "SANO"]
print("SANO de la tanda                  : %d" % len(sanos))
print("la regla 7 pide el mayor entre 3 y el 20 por ciento: %d" % max(3, int(round(0.2 * len(sanos)))))
