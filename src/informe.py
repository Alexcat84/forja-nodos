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


CARPETA_ARCHIVO = "_insertados"
# LA POBLACION DEL BARRIDO ES GRAFO MAS BANDEJAS, TAMBIEN PARA LA ADUANA
# (12 sep 2026, decision del fundador, punto 3). `D.38.4` ya lo manda para el
# auditor desde el 11 sep, y el informe seguia cargando solo el grafo: **un par
# cuyos dos extremos viven en cuarentena no lo levantaba nadie.**
#
# EL EJEMPLAR QUE LO OBLIGO: `cap_10` `L225` a `L251` contra
# `reconocer_recompensar_gente_estable` de `cap_06`, los dos en la bandeja. La
# `ACTA 20` lo leyo y lo clasifico a mano porque la maquina no podia verlo.
#
# SE DESCARTAN `_insertados` (ya viven en el grafo, D.31, y contarlos dos veces
# seria medir el mismo nodo contra si mismo) y `_derivadas`.
#
# Y SE DESCARTA LO QUE NO PUEDE ENTRAR, QUE NO ES LO MISMO QUE LO QUE NO HA
# ENTRADO. `cuarentena/` tambien aloja `ensayo_referencia_163/`, que son 163
# nodos de un CATALOGO DE REFERENCIA ajeno puestos ahi para calibrar la aduana
# (`docs/ESTRENO_DE_LA_ADUANA.md`). Esos no esperan juicio: no van a entrar
# nunca en este grafo, y medir el trabajo de hoy contra ellos seria abrir cola
# de lectura contra material que la puerta rechazaria de todas formas.
#
# EL CRITERIO NO ES UNA LISTA DE NOMBRES, que es el error que la decision 1 de
# este mismo dia acaba de corregir un piso mas abajo: **entra en la poblacion el
# candidato cuyas fuentes estan TODAS en la tabla canonica vigente.** Una fuente
# fuera de la tabla ya lo tumbaria en la puerta (guarda `fuentes`), asi que lo
# que la poblacion deja fuera es exactamente lo que no podria entrar.
#
# Y ES SIMETRICO: el ensayo se corre con `FORJA_FUENTES` apuntando a su tabla
# derivada, y ese dia los 163 son los canonicos y los 83 del lote 4 no. El
# criterio sigue a la tabla que mande, no a una carpeta.
#
# Y EL PROPIO CANDIDATO NO SE MIDE CONTRA SI MISMO: lo excluye `buscar_vecinos`
# por su id, que es la errata de metodo de `D.38.4` corregida en la `ACTA 18`.
CARPETAS_FUERA_DE_POBLACION = ("_insertados", "_derivadas")


class Poblacion(object):
    """Lo que el barrido tuvo delante, con sus dos mitades a la vista.

    Se publican las dos porque una sola miente: `286` no dice lo mismo que
    `203 del grafo mas 83 que esperan`, y la segunda es la que permite leer por
    que un candidato levanto vecino (`D.38.3`, toda cifra con su reparto).
    """

    def __init__(self, grafo=0, bandejas=0):
        self.grafo = grafo
        self.bandejas = bandejas

    @property
    def total(self):
        return self.grafo + self.bandejas

    def __int__(self):
        return self.total

    def __str__(self):
        return "%d   (%d del grafo mas %d que esperan en bandejas)" % (
            self.total, self.grafo, self.bandejas)


def _fuentes_canonicas(candidato, tabla_fuentes):
    """Cierto si TODAS las fuentes del candidato estan en la tabla vigente."""
    claves = [f.get("clave") for f in (candidato.get("fuentes") or [])
              if isinstance(f, dict)]
    return bool(claves) and all(c in tabla_fuentes for c in claves)


def poblacion_de_bandejas(raiz=None, fecha=None, tabla_fuentes=None):
    """Los candidatos que ESPERAN juicio en las bandejas, listos para medir."""
    raiz = raiz or comun.RAIZ
    if tabla_fuentes is None:
        tabla_fuentes = comun.leer_json(comun.RUTA_FUENTES)
    base = os.path.join(raiz, "cuarentena")
    esperando = []
    if not os.path.isdir(base):
        return esperando
    for carpeta, subcarpetas, ficheros in os.walk(base):
        subcarpetas[:] = [s for s in subcarpetas
                          if s not in CARPETAS_FUERA_DE_POBLACION
                          and not s.startswith(".")]
        for fichero in sorted(ficheros):
            if not fichero.lower().endswith(".json"):
                continue
            ruta = os.path.join(carpeta, fichero)
            if esta_archivado(ruta):
                continue
            try:
                bruto = comun.leer_json(ruta)
            except (IOError, ValueError):
                # UN CANDIDATO ILEGIBLE NO SE CUENTA Y NO REVIENTA EL BARRIDO:
                # su propio dictamen ya lo dice con su guarda (CAERIA).
                continue
            candidato, _avisos = aduana.normalizar_candidato(bruto, fecha)
            if candidato.get("id") and _fuentes_canonicas(candidato, tabla_fuentes):
                esperando.append(candidato)
    return esperando


def esta_archivado(ruta):
    """Cierto si la ruta cuelga de `cuarentena/_insertados/` (D.31).

    UN CANDIDATO INSERTADO NO SE BORRA: su fichero es el registro de COMO
    entro, y ese registro vale mas cuanto mas viejo es. Pero deja de ser un
    candidato, asi que el informe no lo cuenta.

    SIN ESTO LA CIFRA MENTIRIA EN LA DIRECCION MAS FEA: el informe diria
    `CAERIA: el id ya vive en el grafo` sobre un nodo que entro bien, y un
    lote recien insertado se leeria como un lote entero rechazado.
    """
    piezas = os.path.normpath(ruta).replace("\\", "/").split("/")
    return CARPETA_ARCHIVO in piezas


def revisar(rutas, ruta_dataset=None, umbrales=None, tabla_fuentes=None,
            bandejas=None):
    """Corre el informe sobre una lista de ficheros de candidato.

    `bandejas=None` descubre la poblacion que espera en `cuarentena/` (punto 3
    de la decision del 12 sep 2026). `bandejas=[]` mide solo contra el grafo, y
    es lo que piden los instrumentos de calibracion, que miden la aduana contra
    un catalogo de referencia y no contra las bandejas de hoy.
    """
    ruta_dataset = ruta_dataset or comun.RUTA_DATASET
    umbrales = umbrales or modulo_config.cargar()
    if tabla_fuentes is None:
        tabla_fuentes = comun.leer_json(comun.RUTA_FUENTES)
    esquema_nodo = modulo_esquema.cargar()
    nodos = comun.leer_jsonl(ruta_dataset)
    # EL RESOLUTOR SE QUEDA EN EL GRAFO Y NO SE ENSANCHA: la guarda que muerde
    # con el es 'el id ya vive en el grafo', y un id que espera en la bandeja NO
    # vive en el grafo todavia. Lo que se ensancha es la POBLACION del barrido.
    resolutor = Resolutor(nodos)
    fecha = aduana._hoy()
    if bandejas is None:
        bandejas = poblacion_de_bandejas(fecha=fecha, tabla_fuentes=tabla_fuentes)
    poblacion = list(nodos) + list(bandejas)

    dictamenes = []
    ids_del_lote = {}
    archivados = [r for r in rutas if esta_archivado(r)]
    rutas = [r for r in rutas if not esta_archivado(r)]
    for ruta in rutas:
        try:
            bruto = comun.leer_json(ruta)
        except (IOError, ValueError) as error:
            dictamenes.append({"ruta": ruta, "id": None, "salida": CAERIA,
                               "guarda": "el fichero no se puede leer",
                               "detalles": [str(error)], "vecinos": [], "avisos": []})
            continue
        dictamen, candidato = revisar_candidato(
            bruto, poblacion, resolutor, umbrales, tabla_fuentes, esquema_nodo,
            ids_del_lote, fecha)
        dictamen["ruta"] = ruta
        dictamenes.append(dictamen)
        if dictamen["id"] and dictamen["salida"] != CHOCA:
            ids_del_lote.setdefault(dictamen["id"], os.path.basename(ruta))
    return (dictamenes, Poblacion(len(nodos), len(bandejas)), umbrales,
            archivados)


def texto_informe(dictamenes, cuantos_nodos, umbrales, detalle=True,
                  archivados=None):
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
    if archivados:
        # EL RECORTE SE DECLARA, NUNCA SE APLICA EN SILENCIO. Quien pide un
        # informe sobre una carpeta tiene que saber cuantos ficheros habia y
        # por que no se contaron.
        lineas.append("archivados, NO contados     : %d   (ya viven en el grafo, "
                      "cuarentena/_insertados/)" % len(archivados))
    # LA POBLACION SE PUBLICA CON SU REPARTO (D.38.3 y punto 3 del 12 sep 2026).
    # Un numero solo no deja leer por que un candidato levanto vecino.
    if isinstance(cuantos_nodos, Poblacion):
        lineas.append("poblacion del barrido       : %s" % cuantos_nodos)
    else:
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

    dictamenes, cuantos, umbrales, archivados = revisar(rutas)
    if not dictamenes and archivados:
        print('%s ARCHIVADO%s en cuarentena/_insertados: ya vive%s en el grafo, '
              'y el informe no lo%s cuenta (D.31).'
              % ('1 fichero' if len(archivados) == 1 else '%d ficheros' % len(archivados),
                 '' if len(archivados) == 1 else 'S',
                 '' if len(archivados) == 1 else 'n',
                 '' if len(archivados) == 1 else 's'))
        return 0
    print(texto_informe(dictamenes, cuantos, umbrales,
                        detalle=not resumen_solo, archivados=archivados))
    return 0
