# desnudo.py: imprime cada candidato de una bandeja SIN su resumen_teorico.
# CONSTANTES TECLEADAS DENTRO: ninguna lista de ids. La bandeja se lee del disco.
# Sirve para clasificar a ciegas antes de destapar la razon escrita del extractor.
import json, sys, pathlib

bandeja = pathlib.Path(sys.argv[1])
for f in sorted(bandeja.glob("*.json")):
    d = json.loads(f.read_text(encoding="utf-8"))
    print("=" * 70)
    print("ID      :", d["id"])
    print("TITULO  :", d["titulo"])
    print("ACTIVA  :", d["condiciones_activacion"])
    print("ENTREGA :", d["entregable_esperado"])
    print("PASOS   :", len(d["pasos_accionables"]))
    for i, p in enumerate(d["pasos_accionables"], 1):
        print("  %2d. %s" % (i, p))
    print("PREVIOS :", d.get("nodos_previos"), " SIGUIENTES:", d.get("nodos_siguientes"))
    print("DOMINIO :", d.get("dominio"), " ESTADO:", d.get("estado"))
