# -*- coding: utf-8 -*-
"""LECTOR DE LA COLA DE VECINOS, para preparar los veredictos antes de la aduana.

NO DECIDE NADA Y NO ESCRIBE NADA EN NINGUNA SEDE. Llama a `aduana.buscar_vecinos`,
que es el mismo codigo que corre la aduana de verdad, y me imprime la cola que voy
a tener que leer. **La aduana sigue siendo la que decide, y cada candidato pasa por
ella igual** (`EXTRACTOR.md` 2 y 16): esto solo me ahorra una pasada en seco por
candidato, que cuesta cuatro minutos cada una.

POR QUE EXISTE Y POR QUE NO ES MAQUINARIA: es un LECTOR, de la misma especie que
los que cada vuelta escribe en su carpeta de trabajo. No es una guarda, no es un
arnes y no sustituye a ningun instrumento de la casa.
"""
import sys, io, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import aduana, comun
from src import config as modulo_config

def main():
    salida = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    nodos = comun.leer_jsonl(comun.RUTA_DATASET)
    ids_grafo = set(n["id"] for n in nodos if n.get("id"))
    poblacion = list(nodos) + list(aduana.poblacion_de_bandejas())
    umbrales = modulo_config.cargar()
    for ruta in sys.argv[1:]:
        bruto = comun.leer_json(ruta)
        candidato, _ = aduana.normalizar_candidato(bruto, "2026-09-16")
        vecinos = aduana.buscar_vecinos(candidato, poblacion, umbrales)
        salida.write("=== %s  (%d vecinos)\n" % (candidato["id"], len(vecinos)))
        for v in vecinos:
            donde = "GRAFO" if v["id"] in ids_grafo else "bandeja"
            salida.write("  %-46s [%s]  por %s\n"
                         % (v["id"], donde, ", ".join(v["levantada_por"])))
            salida.write("      similitud %.3f  familia %.3f  paso %.3f   %s\n"
                         % (v["senales"]["similitud_texto"], v["senales"]["familia_id"],
                            v["senales"]["paso_contra_nodo"], v["detalle_paso"] or ""))
        salida.flush()

main()
