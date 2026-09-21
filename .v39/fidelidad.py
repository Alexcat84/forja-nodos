# -*- coding: utf-8 -*-
"""La relectura de fidelidad D.30 de la vuelta 39: la tabla por candidato y la fila por capitulo.

El veredicto paso a paso lo pone el extractor leyendo cada paso contra su linea; este
instrumento cuenta los pasos del dato y talla la tabla, para que la celda no se teclee (D.41).
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# por candidato: (id, capitulo, [pasos marcados PUENTE], [pasos releidos enteros por caer en
# la clase que el encargo manda releer: persona, cuenta, escalon o adjetivo de sentimiento])
LOTE = [
    ("pedir_critica_primero_crear_seguridad_psicologica", "cap_13", [], list(range(1, 18))),
    ("elegir_pregunta_recurrente_pedir_critica", "cap_13", [],
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 19, 20, 21, 22, 23, 24]),
    ("resolver_dudas_frecuentes_pedir_critica", "cap_13", [],
     [1, 3, 4, 6, 9, 10, 11, 12, 13, 14, 15]),
]


def coma(x):
    return ("%.2f" % x).replace(".", ",")


filas = []
for cid, cap, puentes, releidos in LOTE:
    ruta = os.path.join(RAIZ, "cuarentena", "scott_radical_candor", "%s.json" % cid)
    with io.open(ruta, encoding="utf-8") as f:
        d = json.load(f)
    n = len(d["pasos_accionables"])
    for p in puentes + releidos:
        assert 1 <= p <= n, (cid, p)
    filas.append((cid, cap, n, len(puentes), len(releidos), puentes))

print("RELECTURA DE FIDELIDAD D.30, VUELTA 39, ANTES DE LA PRIMERA INSERCION")
print("  %-52s %-7s %6s %7s %8s %s" % ("candidato", "cap", "pasos", "PUENTE", "releidos", "por ciento"))
print("  " + "-" * 104)
for cid, cap, n, np_, nr, _ in filas:
    print("  %-52s %-7s %6d %7d %8d %10s"
          % (cid[:52], cap, n, np_, nr, coma(100.0 * np_ / n)))

tot_pasos = sum(f[2] for f in filas)
tot_p = sum(f[3] for f in filas)
tot_r = sum(f[4] for f in filas)
print("  " + "-" * 104)
print("  %-52s %-7s %6d %7d %8d %10s"
      % ("LA FILA DEL TRAMO", "cap_13", tot_pasos, tot_p, tot_r, coma(100.0 * tot_p / tot_pasos)))
print()
print("  EL DENOMINADOR, DICHO (python .v39/denominador.py): cap_13 entero son 12")
print("  candidatos y 212 pasos, 9 en bandeja y 3 insertados. Mi tramo son 3 de esos 12")
print("  y %d de esos 212 pasos. La fila de arriba es la del TRAMO y por eso se llama asi;" % tot_pasos)
print("  la del capitulo NO la firmo, porque 156 de sus 212 pasos no los he releido yo.")
print("  techo de PASOS INVENTADOS (AUDITOR_FORJA.md 8.1): 10 por ciento. Medido: %s." % coma(100.0 * tot_p / tot_pasos))
print("  pasos releidos enteros por nombrar persona, cuenta, escalon o adjetivo de")
print("  sentimiento (lo que el encargo manda declarar aunque sea cero): %d de %d." % (tot_r, tot_pasos))
print()
print("  LOS PUENTE, UNO A UNO:")
for cid, cap, n, np_, nr, puentes in filas:
    for p in puentes:
        print("    %s paso %d" % (cid, p))
if not tot_p:
    print("    ninguno")
