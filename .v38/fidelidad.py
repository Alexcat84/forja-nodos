# -*- coding: utf-8 -*-
"""La relectura de fidelidad D.30 de la vuelta 38: la tabla por candidato y la fila por capitulo.

El veredicto paso a paso lo pone el extractor leyendo cada paso contra su linea; este
instrumento cuenta los pasos del dato y talla la tabla, para que la celda no se teclee (D.41).
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# por candidato: (id, capitulo, [numeros de paso marcados PUENTE], [pasos releidos por la
# clase que el encargo manda releer entera: persona, cuenta, escalon, adjetivo de sentimiento])
LOTE = [
    ("mejorar_consciencia_propia_relacional_dos_practicas", "cap_13", [], [5, 7, 10]),
    ("contar_cuatro_historias_propias_ver_hueco_intencion", "cap_13", [], [2, 3, 5, 7, 8, 11, 14, 17]),
    ("practicar_triangulo_critica_tres_papeles", "cap_13", [], [1, 7, 10, 13]),
    ("pedir_critica_primero_crear_seguridad_psicologica", "cap_13", [6, 15],
     [1, 2, 3, 4, 5, 6, 8, 9, 11, 13, 15, 17]),
    ("elegir_pregunta_recurrente_pedir_critica", "cap_13", [], [4, 5, 12, 13, 22]),
    ("resolver_dudas_frecuentes_pedir_critica", "cap_13", [], [3, 9, 10, 14, 15]),
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

print("RELECTURA DE FIDELIDAD D.30, VUELTA 38, ANTES DE LA PRIMERA INSERCION")
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
      % ("LA FILA DEL CAPITULO", "cap_13", tot_pasos, tot_p, tot_r, coma(100.0 * tot_p / tot_pasos)))
print()
print("  un solo capitulo en el tramo: la fila por capitulo y el total son la misma fila.")
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
