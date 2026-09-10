# -*- coding: utf-8 -*-
"""EL GRAFO DE REFERENCIA: el catalogo limpio de My-idea, en SOLO LECTURA.

Contra este catalogo se calibra la forja (D.4, tanda B). Es el resultado de la
campaña consumada: 3.853 nodos, 3.169 vivos y 684 deprecados, auditados par a
par, con sus fusiones ejecutadas y su integral pasada.

    clon:   ../my-idea-lectura
    tag:    catalogo-limpio-v1
    commit: 1b12832392469afd2ac42775d606e4dfd443ab43

COMO SE RECREA, y va escrito aqui porque una medicion que no se puede recomputar
no es una medicion (EJECUTOR.md regla 5):

    cd ..
    git clone --branch catalogo-limpio-v1 --depth 1 \\
        https://github.com/Alexcat84/My-idea.git my-idea-lectura

NADA DE ESTE MODULO ESCRIBE EN EL CLON. Lee `dataset/metadata/master_graph.json`
y nada mas.

POR QUE EL CATALOGO ES LA VERDAD CONOCIDA QUE LA CALIBRACION NECESITA. No es
solo un corpus grande: es un corpus ADJUDICADO, y trae dentro las dos clases
que el 9.19 separa:

  - GEMELOS REALES: cada nodo vivo con `ids_alias` o `merged_originals` nombra
    a los nodos que absorbio. Ese par (superviviente contra absorbido) es un
    duplicado que una persona leyo y adjudico REPITE. No es un gemelo plantado
    por quien calibra: es un gemelo que la casa pago.
  - JERARQUIA REAL: cada arista declarada entre dos vivos es un par madre-hijo
    que una persona cableo en vez de fundir.

Sin esas dos clases, la banda del 9.19 (la similitud alta caza duplicados, la
media caza jerarquias) seria una frase y no una medicion.
"""

import io
import json
import os
import sys

RAIZ_FORJA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLON = os.environ.get("FORJA_REFERENCIA") or os.path.join(
    os.path.dirname(RAIZ_FORJA), "my-idea-lectura")
RUTA_GRAFO = os.path.join(CLON, "dataset", "metadata", "master_graph.json")

TAG_DECLARADO = "catalogo-limpio-v1"
COMMIT_DECLARADO = "1b12832392469afd2ac42775d606e4dfd443ab43"

sys.path.insert(0, RAIZ_FORJA)


def corte():
    """El corte del grafo de referencia, leido de git en ESTA corrida."""
    import subprocess
    def git(*args):
        try:
            salida = subprocess.run(["git"] + list(args), cwd=CLON,
                                    stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            return salida.stdout.decode("utf-8", "replace").strip()
        except Exception:
            return ""
    return {"clon": CLON, "commit": git("rev-parse", "HEAD"),
            "tag": git("describe", "--tags"),
            "fecha": git("log", "-1", "--format=%ad", "--date=short")}


def cargar_crudo():
    if not os.path.exists(RUTA_GRAFO):
        raise SystemExit(
            "NO ENCUENTRO EL GRAFO DE REFERENCIA en %s.\n"
            "Recrea el clon como dice el docstring de calibracion/referencia.py, o\n"
            "apunta FORJA_REFERENCIA a donde viva." % RUTA_GRAFO)
    with io.open(RUTA_GRAFO, "r", encoding="utf-8") as f:
        return json.load(f)


# ------------------------------------------------------------------ el mapeo
#
# El catalogo de My-idea y el esquema de la forja nombran los mismos campos de
# otra manera. El mapeo se escribe aqui, en un solo sitio, y se declara en
# docs/GRAFO_DE_REFERENCIA.md: traducir en cada instrumento su propia version
# es como nacieron las dos grafias del mismo libro.
CAMPOS = {
    "node_id": "id",
    "titulo_concepto": "titulo",
    "resumen_teorico": "resumen_teorico",
    "pasos_accionables": "pasos_accionables",
    "condiciones_activacion": "condiciones_activacion",
    "entregable_esperado": "entregable_esperado",
    "dominio": "dominio",
    "nodos_previos": "nodos_previos",
    "nodos_siguientes": "nodos_siguientes",
}


def a_forma_de_forja(crudo, fecha_fuente="2026-09-09"):
    """Traduce un nodo del catalogo a la forma del esquema de la forja.

    LO QUE ESTE MAPEO NO HACE, y se dice para que nadie lo lea como una
    conversion: no arregla ids, no parte fuentes y no inventa denominaciones.
    Traduce nombres de campo y nada mas. Si el id del catalogo rompe
    docs/REGLAS_DE_ID.md, LLEGA ROTO A PROPOSITO: esa diferencia entre las dos
    casas es justo una de las cosas que la calibracion tiene que medir, no
    tapar.
    """
    nodo = {}
    for origen, destino in CAMPOS.items():
        if origen in crudo:
            nodo[destino] = crudo[origen]
    # `condiciones_activacion` es LISTA en My-idea (3.853 de 3.853, contado) y
    # TEXTO en el esquema de la forja. Se unen con punto y espacio. Es la unica
    # diferencia de FORMA entre los dos esquemas, y se arregla en el mapeo
    # porque el esquema no se toca: cambiar el esquema para que entre un lote
    # importado seria la casa reescribiendo su ley por conveniencia.
    condiciones = nodo.get("condiciones_activacion")
    if isinstance(condiciones, list):
        nodo["condiciones_activacion"] = ". ".join(
            str(c).strip().rstrip(".") for c in condiciones if str(c).strip()) + "."
    nodo.setdefault("pasos_accionables", [])
    nodo.setdefault("nodos_previos", [])
    nodo.setdefault("nodos_siguientes", [])
    nodo["ids_alias"] = [a for a in (crudo.get("ids_alias") or []) if isinstance(a, str)]
    nodo["estado"] = "deprecado" if crudo.get("deprecado") else "vivo"
    nodo["denominaciones"] = {"nombre_largo": "", "sigla": "", "otros_idiomas": []}
    nodo["fuentes"] = [{"clave": clave_de_fuente(crudo.get("fuente") or ""),
                        "fecha": fecha_fuente}]
    return nodo


def clave_de_fuente(titulo):
    """Clave canonica en snake_case a partir del titulo del libro.

    Es la forma que `fuentes/FUENTES_CANONICAS.json` pide (una sola grafia por
    libro). Se deriva del titulo y se declara: la tabla de verdad la escribe
    una persona antes del primer nodo del libro (manual seccion 7.1).
    """
    import re
    import unicodedata
    texto = unicodedata.normalize("NFD", titulo or "")
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn").lower()
    texto = re.sub(r"[^a-z0-9]+", "_", texto).strip("_")
    piezas = [p for p in texto.split("_") if p and not p.isdigit()]
    return "_".join(piezas[:4]) or "fuente_sin_titulo"


class Referencia(object):
    """El catalogo limpio, cargado una vez y medido con instrumento propio."""

    def __init__(self):
        crudo = cargar_crudo()
        self.version = crudo.get("version")
        self.total_declarado = crudo.get("total_nodos")
        self.crudos = crudo["nodos"]
        self.nodos = {}
        self.vivos = []
        self.deprecados = []
        for identificador, ficha in self.crudos.items():
            nodo = a_forma_de_forja(ficha)
            self.nodos[identificador] = nodo
            if nodo["estado"] == "vivo":
                self.vivos.append(identificador)
            else:
                self.deprecados.append(identificador)
        self.vivos.sort()
        self.deprecados.sort()

    # -------------------------------------------------------- verdad conocida

    def pares_gemelos(self):
        """Pares (superviviente, absorbido) que una persona adjudico REPITE.

        El superviviente esta VIVO y nombra al absorbido en `ids_alias` o en
        `merged_originals`. Solo cuentan los pares cuyos DOS textos existen en
        el catalogo: un absorbido sin ficha no se puede medir, y una medicion
        sobre un nodo que no esta es una medicion inventada.
        """
        pares = []
        for identificador in self.vivos:
            ficha = self.crudos[identificador]
            absorbidos = set(a for a in (ficha.get("ids_alias") or [])
                             if isinstance(a, str))
            for entrada in ficha.get("merged_originals") or []:
                if isinstance(entrada, dict) and entrada.get("node_id"):
                    absorbidos.add(entrada["node_id"])
                elif isinstance(entrada, str):
                    absorbidos.add(entrada)
            for absorbido in sorted(absorbidos):
                if absorbido in self.nodos and absorbido != identificador:
                    pares.append((identificador, absorbido))
        return pares

    def pares_jerarquia(self):
        """Pares madre-hijo DECLARADOS entre dos vivos: alguien los cableo en
        vez de fundirlos, asi que son jerarquia leida, no duplicado."""
        vivos = set(self.vivos)
        pares = set()
        for identificador in self.vivos:
            nodo = self.nodos[identificador]
            for destino in nodo.get("nodos_siguientes") or []:
                if destino in vivos and destino != identificador:
                    pares.add((identificador, destino))
            for origen in nodo.get("nodos_previos") or []:
                if origen in vivos and origen != identificador:
                    pares.add((origen, identificador))
        return sorted(pares)

    def pares_ajenos(self, cuantos, semilla):
        """Pares de vivos SIN arista declarada y SIN relacion de absorcion.

        El catalogo esta auditado par a par, asi que dos vivos sin arista son
        dos procedimientos distintos: eso es lo que una señal NO deberia
        levantar. Es la clase que mide el otro lado del umbral.
        """
        import random
        azar = random.Random(semilla)
        emparentados = set()
        for a, b in self.pares_jerarquia():
            emparentados.add((a, b)); emparentados.add((b, a))
        for a, b in self.pares_gemelos():
            emparentados.add((a, b)); emparentados.add((b, a))
        pares = []
        vistos = set()
        intentos = 0
        while len(pares) < cuantos and intentos < cuantos * 40:
            intentos += 1
            a = azar.choice(self.vivos)
            b = azar.choice(self.vivos)
            if a == b or (a, b) in emparentados or (a, b) in vistos:
                continue
            vistos.add((a, b))
            pares.append((a, b))
        return pares

    def muestra_de_vivos(self, cuantos, semilla):
        import random
        azar = random.Random(semilla)
        return sorted(azar.sample(self.vivos, min(cuantos, len(self.vivos))))

    def tabla_de_fuentes(self):
        """La tabla canonica derivada del catalogo, para correr la aduana sobre
        el. No se escribe en fuentes/FUENTES_CANONICAS.json: se da a la aduana
        por FORJA_FUENTES, porque la tabla de verdad la escribe una persona
        antes del primer nodo del libro."""
        tabla = {"_derivada": "Derivada del grafo de referencia por "
                              "calibracion/referencia.py. NO es la tabla canonica de "
                              "la forja: existe para poder correr la aduana sobre el "
                              "catalogo limpio sin tocar la tabla de verdad."}
        for identificador, ficha in self.crudos.items():
            clave = clave_de_fuente(ficha.get("fuente") or "")
            if clave not in tabla:
                tabla[clave] = {"titulo_completo": ficha.get("fuente") or "",
                                "autor": "", "anio": ""}
        return tabla


def main(argumentos=None):
    from src import comun
    comun.salida_utf8()
    datos = corte()
    referencia = Referencia()
    gemelos = referencia.pares_gemelos()
    jerarquia = referencia.pares_jerarquia()
    print("GRAFO DE REFERENCIA, corte leido de git en esta corrida")
    print("  clon    : %s" % datos["clon"])
    print("  commit  : %s" % datos["commit"])
    print("  tag     : %s" % datos["tag"])
    print("  fecha   : %s" % datos["fecha"])
    print("  declarado en calibracion/referencia.py: %s / %s"
          % (TAG_DECLARADO, COMMIT_DECLARADO))
    print("  coincide: %s" % ("SI" if datos["commit"] == COMMIT_DECLARADO else "NO"))
    print("")
    print("CENSO, contado del fichero por este instrumento")
    print("  total_nodos que declara el grafo : %s" % referencia.total_declarado)
    print("  nodos contados                   : %d" % len(referencia.nodos))
    print("  vivos                            : %d" % len(referencia.vivos))
    print("  deprecados (archivo)             : %d" % len(referencia.deprecados))
    print("")
    print("VERDAD CONOCIDA que el catalogo trae dentro")
    print("  pares GEMELOS (superviviente contra absorbido, adjudicados REPITE): %d"
          % len(gemelos))
    print("  pares JERARQUIA (arista declarada entre dos vivos)               : %d"
          % len(jerarquia))
    print("  libros distintos (clave derivada del titulo)                     : %d"
          % (len(referencia.tabla_de_fuentes()) - 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
