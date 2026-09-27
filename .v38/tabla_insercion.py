# -*- coding: utf-8 -*-
"""La tabla de la TAREA 3, tallada de los informes de la propia aduana (D.41).

Una fila por candidato: los vecinos que la aduana levanto, como los juzgue y cuantos
nodos habia en el grafo al salir. NADA de esto se teclea: se lee de .v38/informes/.
"""
import glob
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORDEN = [
    ("1", "i01_mejorar_consciencia.txt", "mejorar_consciencia_propia_relacional_dos_practicas", "L17"),
    ("2", "i02_contar_cuatro.txt", "contar_cuatro_historias_propias_ver_hueco_intencion", "L41"),
    ("3", "i03_triangulo.txt", "practicar_triangulo_critica_tres_papeles", "L59"),
    ("4", "i04_pedir_critica_primero.txt", "pedir_critica_primero_crear_seguridad_psicologica", "L73"),
    ("5", "i05_elegir_pregunta.txt", "elegir_pregunta_recurrente_pedir_critica", "L115"),
    ("6", "i06_resolver_dudas.txt", "resolver_dudas_frecuentes_pedir_critica", "L167"),
]

print("| # | candidato | linea | vecinos | veredictos escritos | nodos al salir | codigo |")
print("|---:|---|---:|---:|---|---:|---|")
for n, fichero, cid, linea in ORDEN:
    ruta = os.path.join(RAIZ, ".v38", "informes", fichero)
    if not os.path.exists(ruta):
        print("| %s | `%s` | `%s` | . | **NO CORRIO** | . | . |" % (n, cid, linea))
        continue
    texto = open(ruta, encoding="utf-8", errors="replace").read()
    m = re.search(r"VECINOS POR ENCIMA DE UMBRAL: (\d+)", texto)
    vecinos = m.group(1) if m else "0"
    clases = []
    for vid, clase in re.findall(r"\n  vecino (\S+)", texto), []:
        pass
    vecs = re.findall(r"\n  vecino (\S+)", texto)
    m2 = re.search(r"nodos en el grafo: (\d+)", texto)
    nodos = m2.group(1) if m2 else "."
    m3 = re.search(r"CODIGO DE SALIDA: (\d+)", texto)
    cod = m3.group(1) if m3 else "."
    m4 = re.search(r"veredictos en bitacora/VEREDICTOS\.jsonl: (\d+)", texto)
    nver = m4.group(1) if m4 else "0"
    cola = re.findall(r"ARISTAS EN COLA, sin cablear: (\d+)", texto)
    extra = (", %s en cola" % cola[0]) if cola else ""
    print("| %s | `%s` | `%s` | %s | %s%s | %s | %s |"
          % (n, cid, linea, vecinos, nver, extra, nodos,
             "**VERDE**" if cod == "0" else "**%s**" % cod))
