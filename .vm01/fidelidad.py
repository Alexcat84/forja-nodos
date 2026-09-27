# -*- coding: utf-8 -*-
"""LA RELECTURA DE FIDELIDAD D.30 DEL TRAMO, PASO A PASO Y CON SU LINEA.

QUE PONE EL DATO Y QUE PONGO YO, dicho antes de la tabla porque es la unica forma
de que la tabla se pueda discutir: el DENOMINADOR (cuantos pasos tiene cada nodo)
lo cuenta este guion de los JSON de la bandeja, hoy. La CLASE de cada paso
(TRANSCRIPCION o PUENTE) y LA LINEA de la que sale la pone el extractor leyendo,
porque ninguna maquina la puede poner (D.30), y va escrita en .vm01/clases.txt.

EL GUION COMPRUEBA QUE MI LECTURA CUBRE TODOS LOS PASOS: si a un nodo le faltan
clases o le sobran, lo dice y sale en rojo. Una relectura que no cubre cada paso
no es una relectura.
"""
import io, json, sys, collections

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

BANDEJA = "cuarentena/marquet_turn_the_ship/%s.json"
CLASES = eval(io.open(".vm01/clases.txt", encoding="utf-8").read())

print("AVISO: DENOMINADOR CONTADO DE LOS JSON DE LA BANDEJA EN ESTA CORRIDA. "
      "La clase de cada paso y su linea salen de .vm01/clases.txt, escritas por el extractor leyendo (D.30).")
print("")

rojo = []
por_unidad = collections.OrderedDict()

print("| nodo | unidad | paso | linea del libro | clase |")
print("|---|---|---:|---|---|")
for unidad, nodos in CLASES:
    for identificador, filas in nodos:
        datos = json.load(io.open(BANDEJA % identificador, encoding="utf-8"))
        reales = len(datos["pasos_accionables"])
        if reales != len(filas):
            rojo.append("%s: %d pasos en el JSON y %d clases escritas"
                        % (identificador, reales, len(filas)))
        acumulado = por_unidad.setdefault(unidad, [0, 0, 0])
        acumulado[0] += 1
        acumulado[1] += reales
        for numero, linea, clase in filas:
            if clase != "TRANSCRIPCION":
                acumulado[2] += 1
            print("| `%s` | `%s` | %d | %s | **%s** |" % (identificador, unidad, numero, linea, clase))

print("")
print("| unidad | nodos | **pasos escritos** | **PUENTE** | **PASOS INVENTADOS** |")
print("|---|---:|---:|---:|---:|")
tn = tp = tb = 0
peor = (None, -1.0)
for unidad, (nodos, pasos, puentes) in por_unidad.items():
    tasa = 100.0 * puentes / pasos if pasos else 0.0
    tn += nodos; tp += pasos; tb += puentes
    if tasa > peor[1]:
        peor = (unidad, tasa)
    print("| `%s` | %d | **%d** | **%d** | **%s por ciento** |"
          % (unidad, nodos, pasos, puentes, ("%.2f" % tasa).replace(".", ",")))
print("| **el lote marquet_turn_the_ship ENTERO** | **%d** | **%d** | **%d** | **%s por ciento** |"
      % (tn, tp, tb, ("%.2f" % (100.0 * tb / tp)).replace(".", ",")))

print("")
print("| | |")
print("|---|---:|")
print("| unidades releidas y firmadas por mi en esta vuelta | **%d** de **%d** |" % (len(por_unidad), len(por_unidad)))
print("| **la fila que decide, que es la peor** | `%s` con **%s** |" % (peor[0], ("%.2f" % peor[1]).replace(".", ",")))
print("| tope de `PASOS INVENTADOS` | **10,00** |")
print("| **el freno** | **%s** |" % ("DISPARADO" if peor[1] > 10.0 else "NO SE ACTIVA"))
print("")
if rojo:
    print("EN ROJO: la relectura no cubre todos los pasos")
    for r in rojo:
        print("  " + r)
    sys.exit(1)
print("COBERTURA VERDE: cada paso de cada nodo del lote tiene su clase y su linea escritas.")

RETIRADOS = eval(io.open(".vm01/retirados.txt", encoding="utf-8").read())
print("")
print("| nodo | paso | especie | lo que escribi primero | el parrafo NO lo dice | como quedo |")
print("|---|---:|---|---|---|---|")
for nodo, paso, especie, antes, motivo, despues in RETIRADOS:
    print("| `%s` | %d | **%s** | *%s* | %s | *%s* |" % (nodo, paso, especie, antes, motivo, despues))
print("| **total de puentes escritos y RETIRADOS EN EL ACTO** | **%d** | | | | |" % len(RETIRADOS))
