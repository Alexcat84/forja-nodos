# -*- coding: utf-8 -*-
"""PASOS INVENTADOS POR CAPITULO: LA CUENTA, QUE ES LA MITAD QUE PUEDE CONTAR UNA MAQUINA.

AUDITOR_FORJA.md 8.3.1: el acta cuenta los pasos de cada candidato del capitulo
contra la cuarentena y los compara con lo que el reporte dice. La otra mitad, la
lectura de cada paso contra su parrafo, la hace el auditor y va en el acta: una
maquina no sabe si un paso es PUENTE.

La poblacion incluye el candidato apartado a .v60ext/pendientes/, porque la
metrica cuenta LO QUE LA VUELTA ESCRIBIO, no lo que quedo en la bandeja.
"""

import glob
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FICHAS = [
    os.path.join(RAIZ, "cuarentena", "grove_high_output",
                 "priorizar_lista_entrenamiento_subordinados.json"),
    os.path.join(RAIZ, "cuarentena", "grove_high_output",
                 "desarrollar_primer_curso_entrenamiento.json"),
    os.path.join(RAIZ, ".v60ext", "pendientes",
                 "pedir_critica_anonima_curso_entrenamiento_dictado.json"),
]


def main():
    total = 0
    print("LOS CANDIDATOS DE cap_17, CON SUS PASOS CONTADOS POR MI")
    for ruta in FICHAS:
        if not os.path.exists(ruta):
            print("  FALTA: %s" % ruta)
            continue
        ficha = json.load(io.open(ruta, encoding="utf-8"))
        pasos = ficha.get("pasos_accionables", [])
        total += len(pasos)
        donde = "bandeja" if "cuarentena" in ruta else "APARTADO"
        print("")
        print("  %-52s %2d paso(s)   [%s]" % (ficha["id"], len(pasos), donde))
        for i, paso in enumerate(pasos, 1):
            print("     %d. %s" % (i, paso))

    print("")
    print("=" * 70)
    print("cap_17 : %d candidato(s), %d paso(s) escritos" % (len(FICHAS), total))
    print("cap_18 : 0 candidato(s), 0 paso(s) escritos, SIN SUPERFICIE")
    print("")
    print("EL PUENTE NO LO CUENTA ESTE SCRIPT: lo lee el auditor contra el parrafo")
    print("del libro, y su veredicto va en el acta. 8.3.2.")


if __name__ == "__main__":
    main()
