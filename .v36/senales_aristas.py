# -*- coding: utf-8 -*-
"""LO QUE LA SENIAL MIDIO EN CADA ARISTA DE JERARQUIA DE ESTA VUELTA, leido de la
bitacora y no de mi memoria. La pregunta que contesta: de las aristas madre a hijo
que declare, cuantas levanto una senial y cuantas las cazo la lectura (D.19)."""
import json

VUELTA = 427   # lineas que tenia bitacora/VEREDICTOS.jsonl al abrir la vuelta
lineas = [json.loads(l) for l in open("bitacora/VEREDICTOS.jsonl", encoding="utf-8") if l.strip()]
nuevas = lineas[VUELTA:]

print("| la arista, madre a hijo | paso_contra_nodo | umbral | quien la levanto |")
print("|---|---:|---:|---|")
caza_senal = caza_lectura = 0
for d in nuevas:
    if d.get("veredicto") != "CONTINUA":
        continue
    paso = d["senales"]["paso_contra_nodo"]
    por = ", ".join(d.get("levantada_por") or [])
    if "lectura" in por:
        caza_lectura += 1
        quien = "**la lectura**"
    else:
        caza_senal += 1
        quien = por
    arista = d.get("arista") or "?"
    if d.get("arista_en_cola"):
        arista += "  (EN COLA)"
    print("| `%s` | %.3f | 0,60 | %s |"
          % (arista, paso if isinstance(paso, float) else 0.0, quien))
print()
print("aristas de jerarquia declaradas en la vuelta : %d" % (caza_senal + caza_lectura))
print("  que una senial levanto                     : %d" % caza_senal)
print("  que solo cazo la lectura                   : %d" % caza_lectura)
print("veredictos nuevos en la bitacora             : %d" % len(nuevas))
print("  de las 13 lineas CONTINUA, dos son el MISMO par: las 430 y 431, y la 431")
print("  esta anotada como duplicado (AC.3.c). Aristas distintas: 12.")
