# -*- coding: utf-8 -*-
"""EL MODO INFORME: la aduana en seco, CERO INSERCIONES.

    python forja.py informe candidato.json [otro.json ...]
    python forja.py informe --carpeta cuarentena/mundo_11

Corre las mismas validaciones y las mismas tres señales que
`python forja.py insertar`, contra el mismo dataset, y dice que PASARIA con cada
candidato. **No escribe en dataset/, ni en bitacora/, ni en censos/, ni en
config/pares_mutuos.jsonl.** Ni una linea.

PARA QUE EXISTE. Antes de la primera insercion real de un mundo, el fundador
tiene que poder leer cuantos pasarian, cuantos caerian y por que guarda, con la
lista completa delante. **Un informe no es una insercion con los ojos cerrados:
es lo que se lee ANTES de abrir la puerta.**

LO QUE EL INFORME NO HACE, y se dice para que nadie lo confunda con un veredicto:
no juzga si un vecino es gemelo o hijo. Eso lo decide una lectura, y su razon
escrita (manual principio 4). El informe dice DONDE hay que leer.

LAS CUATRO SALIDAS POSIBLES de un candidato:

  ENTRARIA      pasa las validaciones y ninguna señal levanta vecino: entra sin
                que nadie tenga que leer nada.
  BLOQUEARIA    pasa las validaciones y levanta vecinos: NO es un rechazo, es la
                cola de lectura. Entraria con su veredicto escrito por vecino.
  CAERIA        una guarda lo rechaza (esquema, reglas de id, fuente fuera de la
                tabla, guiones, o el id ya vive en el grafo). Esto SI es un
                rechazo, y el informe nombra la guarda.
  CHOCA         dos candidatos del mismo lote traen el mismo id. El informe lo
                dice antes de que el segundo pise al primero.
"""

import os
import sys

from . import aduana
from . import comun
from . import config as modulo_config
from . import esquema as modulo_esquema
from .resolutor import Resolutor

ENTRARIA = "ENTRARIA"
BLOQUEARIA = "BLOQUEARIA"
CAERIA = "CAERIA"
CHOCA = "CHOCA"


def revisar_candidato(bruto, nodos, resolutor, umbrales, tabla_fuentes,
                      esquema_nodo, ids_del_lote, fecha):
    """Devuelve el dictamen de UN candidato. No escribe nada."""
    dictamen = {"salida": None, "guarda": "", "detalles": [], "vecinos": [],
                "avisos": [], "id": None}
    candidato, avisos = aduana.normalizar_candidato(bruto, fecha)
    dictamen["id"] = candidato.get("id")
    dictamen["avisos"] = avisos

    try:
        aduana.validar_candidato(candidato, tabla_fuentes, esquema_nodo)
    except aduana.Rechazo as rechazo:
        dictamen["salida"] = CAERIA
        dictamen["guarda"] = rechazo.titulo
        dictamen["detalles"] = rechazo.detalles
        return dictamen, candidato

    if resolutor.existe(candidato["id"]):
        dictamen["salida"] = CAERIA
        dictamen["guarda"] = "el id ya vive en el grafo"
        dictamen["detalles"] = [
            "'%s' resuelve a '%s'. UN CONCEPTO, UN NODO (manual principio 1)"
            % (candidato["id"], resolutor.resolver(candidato["id"]))]
        return dictamen, candidato

    if candidato["id"] in ids_del_lote:
        dictamen["salida"] = CHOCA
        dictamen["guarda"] = "dos candidatos del lote traen el mismo id"
        dictamen["detalles"] = [
            "'%s' ya lo trae %s de este mismo lote"
            % (candidato["id"], ids_del_lote[candidato["id"]])]
        return dictamen, candidato

    vecinos = aduana.buscar_vecinos(candidato, nodos, umbrales)
    dictamen["vecinos"] = vecinos
    dictamen["salida"] = BLOQUEARIA if vecinos else ENTRARIA
    return dictamen, candidato


def revisar(rutas, ruta_dataset=None, umbrales=None, tabla_fuentes=None):
    """Corre el informe sobre una lista de ficheros de candidato."""
    ruta_dataset = ruta_dataset or comun.RUTA_DATASET
    umbrales = umbrales or modulo_config.cargar()
    if tabla_fuentes is None:
        tabla_fuentes = comun.leer_json(comun.RUTA_FUENTES)
    esquema_nodo = modulo_esquema.cargar()
    nodos = comun.leer_jsonl(ruta_dataset)
    resolutor = Resolutor(nodos)
    fecha = aduana._hoy()

    dictamenes = []
    ids_del_lote = {}
    for ruta in rutas:
        try:
            bruto = comun.leer_json(ruta)
        except (IOError, ValueError) as error:
            dictamenes.append({"ruta": ruta, "id": None, "salida": CAERIA,
                               "guarda": "el fichero no se puede leer",
                               "detalles": [str(error)], "vecinos": [], "avisos": []})
            continue
        dictamen, candidato = revisar_candidato(
            bruto, nodos, resolutor, umbrales, tabla_fuentes, esquema_nodo,
            ids_del_lote, fecha)
        dictamen["ruta"] = ruta
        dictamenes.append(dictamen)
        if dictamen["id"] and dictamen["salida"] != CHOCA:
            ids_del_lote.setdefault(dictamen["id"], os.path.basename(ruta))
    return dictamenes, len(nodos), umbrales


def texto_informe(dictamenes, cuantos_nodos, umbrales, detalle=True):
    lineas = []
    cuenta = {ENTRARIA: 0, BLOQUEARIA: 0, CAERIA: 0, CHOCA: 0}
    por_guarda = {}
    for dictamen in dictamenes:
        cuenta[dictamen["salida"]] += 1
        if dictamen["salida"] in (CAERIA, CHOCA):
            por_guarda[dictamen["guarda"]] = por_guarda.get(dictamen["guarda"], 0) + 1

    lineas.append("=" * 76)
    lineas.append("INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.")
    lineas.append("=" * 76)
    lineas.append("candidatos revisados        : %d" % len(dictamenes))
    lineas.append("nodos en el grafo de destino: %d" % cuantos_nodos)
    lineas.append("umbrales de esta corrida    : similitud %.2f | familia %.2f | "
                  "paso contra nodo %.2f"
                  % (umbrales["umbral_similitud_texto"], umbrales["umbral_familia_id"],
                     umbrales["umbral_paso_contra_nodo"]))
    lineas.append("")
    lineas.append("EL SALDO")
    lineas.append("  ENTRARIAN sin leer nada          : %d" % cuenta[ENTRARIA])
    lineas.append("  BLOQUEARIAN esperando veredicto  : %d   (no es rechazo: es cola de lectura)"
                  % cuenta[BLOQUEARIA])
    lineas.append("  CAERIAN por una guarda           : %d" % cuenta[CAERIA])
    lineas.append("  CHOCAN entre si dentro del lote  : %d" % cuenta[CHOCA])
    if por_guarda:
        lineas.append("")
        lineas.append("POR QUE GUARDA CAEN")
        for guarda, cuantos in sorted(por_guarda.items(), key=lambda x: -x[1]):
            lineas.append("  %4d  %s" % (cuantos, guarda))

    bloqueados = [d for d in dictamenes if d["salida"] == BLOQUEARIA]
    if bloqueados:
        largos = sorted(len(d["vecinos"]) for d in bloqueados)
        lineas.append("")
        lineas.append("LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA")
        lineas.append("  vecinos levantados en total      : %d"
                      % sum(len(d["vecinos"]) for d in bloqueados))
        lineas.append("  por candidato bloqueado          : menor %d, mediana %d, mayor %d"
                      % (largos[0], largos[len(largos) // 2], largos[-1]))
        senal = {}
        for d in bloqueados:
            for vecino in d["vecinos"]:
                for nombre in vecino["levantada_por"]:
                    senal[nombre] = senal.get(nombre, 0) + 1
        lineas.append("  que señal levanta cada vecindad  : %s"
                      % ", ".join("%s %d" % (n, c) for n, c in sorted(senal.items())))

    if detalle:
        lineas.append("")
        lineas.append("=" * 76)
        lineas.append("LA LISTA COMPLETA, candidato por candidato")
        lineas.append("=" * 76)
        for dictamen in dictamenes:
            lineas.append("")
            lineas.append("[%s] %s   (%s)"
                          % (dictamen["salida"], dictamen["id"] or "sin id",
                             os.path.basename(dictamen["ruta"])))
            if dictamen["guarda"]:
                lineas.append("    guarda: %s" % dictamen["guarda"])
            for detalle_linea in dictamen["detalles"]:
                lineas.append("      %s" % detalle_linea)
            for vecino in dictamen["vecinos"]:
                medidas = []
                for nombre in ("similitud_texto", "familia_id", "paso_contra_nodo"):
                    valor = vecino["senales"][nombre]
                    medidas.append("%s %s" % (nombre, valor if isinstance(valor, str)
                                              else "%.3f" % valor))
                lineas.append("    vecino %s  [levantada por: %s]"
                              % (vecino["id"], ", ".join(vecino["levantada_por"])))
                lineas.append("      %s" % " | ".join(medidas))
                if vecino["detalle_paso"]:
                    lineas.append("      %s" % vecino["detalle_paso"])
    lineas.append("")
    lineas.append("NADA SE INSERTO. Este informe es de SOLO LECTURA: para que un nodo")
    lineas.append("entre hace falta python forja.py insertar, uno por vez, con su")
    lineas.append("veredicto escrito por vecino.")
    return "\n".join(lineas)


def main(argumentos=None):
    comun.salida_utf8()
    argumentos = list(argumentos or [])
    rutas = []
    resumen_solo = False
    indice = 0
    while indice < len(argumentos):
        argumento = argumentos[indice]
        if argumento == "--carpeta":
            indice += 1
            carpeta = argumentos[indice]
            if not os.path.isdir(carpeta):
                print("no existe la carpeta: %s" % carpeta)
                return 1
            rutas.extend(sorted(os.path.join(carpeta, f) for f in os.listdir(carpeta)
                                if f.lower().endswith(".json")))
        elif argumento == "--resumen":
            resumen_solo = True
        elif argumento.startswith("--"):
            print("opcion desconocida: %s" % argumento)
            return 1
        else:
            rutas.append(argumento)
        indice += 1

    if not rutas:
        print("uso: python forja.py informe candidato.json [...]")
        print("     python forja.py informe --carpeta cuarentena/mundo_11 [--resumen]")
        return 1

    dictamenes, cuantos, umbrales = revisar(rutas)
    print(texto_informe(dictamenes, cuantos, umbrales, detalle=not resumen_solo))
    return 0
