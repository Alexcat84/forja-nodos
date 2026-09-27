# -*- coding: utf-8 -*-
"""EL SALDO DE LA ADUANA, CANDIDATO A CANDIDATO, LEIDO DE MIS PROPIOS INFORMES.

Cada fila sale de `.v1g/informe_NN.txt`, que es la salida literal de
`python forja.py informe cuarentena/grove_high_output/<id>.json` corrida EN EL ACTO de
escribir ese candidato (`EXTRACTOR.md` 16). **Ninguna celda se teclea:** el veredicto de
puerta, la poblacion y los vecinos se sacan del fichero con expresiones regulares, y el
instrumento revienta si un informe no trae su linea.
"""
import glob
import io
import os
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

ORDEN = [
    ("informe_01.txt", "revisar_tres_preguntas_valor_carrera", "cap_01", "P12"),
    ("informe_02b.txt", "construir_flujo_produccion_paso_limitante", "cap_02", "P2"),
    ("informe_03.txt", "clasificar_trabajo_proceso_montaje_prueba", "cap_02", "P5"),
    ("informe_04.txt", "rehacer_flujo_paso_limitante_capacidad", "cap_02", "P6"),
    ("informe_05.txt", "equilibrar_capacidad_personal_inventario_plazo", "cap_02", "P7"),
    ("informe_06.txt", "preferir_inspeccion_proceso_prueba_destructiva", "cap_02", "P9"),
    ("informe_07.txt", "dimensionar_inventario_materia_prima_reposicion", "cap_02", "P10"),
    ("informe_08.txt", "detectar_arreglar_fallo_etapa_menor_valor", "cap_02", "P11"),
]

POBLACION = re.compile(r"poblacion del barrido\s*:\s*(\d+)\s*\((\d+) del grafo mas (\d+)")
VEREDICTO = re.compile(r"^\[(ENTRARIA|BLOQUEARIA|CAERIA)\]\s+(\S+)", re.M)
VECINO = re.compile(r"^\s+vecino (\S+)\s+\[levantada por: ([^\]]+)\]", re.M)
SENALES = re.compile(r"similitud_texto ([\d.]+) \| familia_id ([\d.]+) \| paso_contra_nodo ([\d.]+)")

filas = []
for fichero, identificador, unidad, pieza in ORDEN:
    ruta = os.path.join(".v1g", fichero)
    if not os.path.exists(ruta):
        raise SystemExit("FALTA EL INFORME %s: sin el, este candidato no esta escrito" % ruta)
    texto = io.open(ruta, encoding="utf-8").read()
    pob = POBLACION.search(texto)
    ver = VEREDICTO.search(texto)
    if not pob or not ver:
        raise SystemExit("EL INFORME %s NO TRAE SU LINEA: %s" % (ruta, "poblacion" if not pob else "veredicto"))
    if ver.group(2) != identificador:
        raise SystemExit("EL INFORME %s ES DE OTRO CANDIDATO: %s" % (ruta, ver.group(2)))
    vecinos = VECINO.findall(texto)
    senales = SENALES.findall(texto)
    detalle = "cola vacia"
    if vecinos:
        piezas = []
        for (nombre, senal), (s1, s2, s3) in zip(vecinos, senales):
            piezas.append("`%s` por `%s`, similitud %s, familia %s, paso contra nodo %s"
                          % (nombre, senal.strip(), s1.replace(".", ","),
                             s2.replace(".", ","), s3.replace(".", ",")))
        detalle = "; ".join(piezas)
    filas.append((identificador, unidad, pieza, ver.group(1), pob.group(1), pob.group(2),
                  pob.group(3), len(vecinos), detalle))

print("| # | candidato | unidad | pieza | puerta | poblacion del barrido | vecinos | la cola, nombrada |")
print("|---:|---|---|---|---|---|---:|---|")
for numero, (identificador, unidad, pieza, puerta, total, grafo, bandejas, cuantos, detalle) in enumerate(filas, 1):
    print("| %d | `%s` | `%s` | `%s` | **%s** | %s (%s mas %s) | %d | %s |"
          % (numero, identificador, unidad, pieza, puerta, total, grafo, bandejas,
             cuantos, detalle))

entrarian = sum(1 for f in filas if f[3] == "ENTRARIA")
bloquearian = sum(1 for f in filas if f[3] == "BLOQUEARIA")
caerian = sum(1 for f in filas if f[3] == "CAERIA")
vecinos = sum(f[7] for f in filas)
print("| | **%d candidatos** | | | **%d ENTRARIAN, %d BLOQUEARIAN, %d CAERIAN** | | **%d** | |"
      % (len(filas), entrarian, bloquearian, caerian, vecinos))
print("")
print("EL SALDO, RECONTADO DE LAS FILAS DE ARRIBA")
print("  candidatos escritos y pasados por la aduana en el acto : %d" % len(filas))
print("  ENTRARIAN                                             : %d" % entrarian)
print("  BLOQUEARIAN (cola de lectura, no rechazo)              : %d" % bloquearian)
print("  CAERIAN al escribir esta tabla                         : %d" % caerian)
print("  vecinos levantados en total                            : %d" % vecinos)
print("  ficheros en la bandeja del libro                       : %d"
      % len(glob.glob("cuarentena/grove_high_output/*.json")))
print("")
print("AVISO DE LA FILA 2: su informe es el de DESPUES de la correccion de fidelidad del paso 6")
print("  (.v1g/informe_02b.txt). El de ANTES esta en .v1g/informe_02.txt y no se borra.")
