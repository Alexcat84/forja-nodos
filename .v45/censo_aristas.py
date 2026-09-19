# -*- coding: utf-8 -*-
"""CENSO DE LAS LINEAS DE ARISTA DECLARADA POR LECTURA, por veredicto (D.53).

    poblacion: bitacora/VEREDICTOS.jsonl entero, sin filtrar
    criterio : operacion que empieza por 'arista declarada por lectura'
"""
import collections
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
from src import comun  # noqa: E402

lineas = comun.leer_jsonl(comun.RUTA_VEREDICTOS)
print("poblacion: %s, %d lineas, SIN filtrar"
      % (comun.relativa(comun.RUTA_VEREDICTOS), len(lineas)))
aristas = [l for l in lineas
           if str(l.get("operacion", "")).startswith("arista declarada por lectura")]
print("lineas de arista declarada por lectura : %d" % len(aristas))
por_veredicto = collections.Counter(l.get("veredicto") for l in aristas)
for clase, cuantas in sorted(por_veredicto.items(), key=lambda x: str(x[0])):
    print("  %-12s %d" % (clase, cuantas))
con_cita = len([l for l in aristas if l.get("cita_del_veredicto")])
print("  con cita_del_veredicto : %d" % con_cita)
corregidas = len([l for l in aristas if "CORRECCION DECLARADA" in str(l.get("razon", ""))])
print("  ya con correccion declarada dentro : %d" % corregidas)
