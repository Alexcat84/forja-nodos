# -*- coding: utf-8 -*-
"""LA MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO, CON SU SEMILLA ESCRITA (D.58).

    python scripts/muestra_fidelidad.py --libro grove_high_output --capitulos cap_06,cap_07,cap_08
    python scripts/muestra_fidelidad.py --libro X --capitulos ... --semilla v53

POR QUE EXISTE. En `MODO_INSERCION=cuarentena` **nada toca el grafo**: los candidatos se
quedan en su bandeja hasta que el lote cierre (`D.39`). Releer al digito los pasos de tres
capitulos en cada vuelta cuesta lo mismo que releerlos cuando entran, **y solo uno de los
dos momentos protege un dato**. `D.58` mueve la relectura entera al momento en que el dato
existe, y deja aqui **una muestra que sirve de alarma, no de certificado**.

LO QUE REPARTE, Y NO LO ELIGE NADIE:

  UNO de cada TRES capitulos se relee ENTERO. Cual, lo decide la semilla.
  Los otros DOS llevan una MUESTRA FIJA DE 15 PASOS cada uno.

LA SEMILLA SE ESCRIBE Y LA MUESTRA SE REPRODUCE. Quien audite vuelve a correr esto con la
misma semilla y **tiene que salirle la misma lista**. Una muestra que no se puede
reproducir no es una muestra: **es una eleccion**, y el que elige sus pasos elige su
resultado.

EL DISPARADOR, Y ES LO QUE LA HACE ALARMA Y NO ADORNO:

    si la muestra de un capitulo pasa del 10 por ciento de pasos inventados,
    ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.

**El tope de `D.30` sigue siendo `10` y no se toca.** Lo que cambia es que aqui se mide
sobre `15` pasos en vez de sobre todos, **y por eso el resultado escala a relectura entera
en vez de a veredicto**.
"""

import hashlib
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)

from src import comun  # noqa: E402

PASOS_DE_MUESTRA = 15
TOPE_DE_ESCALADA = 10.0     # por ciento de pasos inventados en la muestra


def _orden(semilla, clave):
    """Un numero estable para (semilla, clave). Sin `random`: el mismo texto da
    siempre el mismo numero, en cualquier maquina y en cualquier version."""
    crudo = ("%s|%s" % (semilla, clave)).encode("utf-8")
    return int(hashlib.sha1(crudo).hexdigest()[:12], 16)


def candidatos_de(libro, capitulo, raiz=None):
    """Los candidatos de ese capitulo, en la bandeja y en el archivo, por su id."""
    raiz = raiz or RAIZ
    encontrados = []
    for carpeta in (os.path.join(raiz, "cuarentena", libro),
                    os.path.join(raiz, "cuarentena", "_insertados", libro)):
        if not os.path.isdir(carpeta):
            continue
        for nombre in sorted(os.listdir(carpeta)):
            if not nombre.endswith(".json"):
                continue
            ruta = os.path.join(carpeta, nombre)
            crudo = comun.leer_texto(ruta)
            if "%s/%s.md" % (libro, capitulo) not in crudo:
                continue
            try:
                encontrados.append(json.loads(crudo))
            except ValueError:
                continue
    return encontrados


def repartir(capitulos, semilla):
    """`(entero, [muestreados])`: cual se relee entero y cuales van por muestra."""
    if not capitulos:
        return None, []
    elegido = min(capitulos, key=lambda c: _orden(semilla, c))
    return elegido, [c for c in capitulos if c != elegido]


def muestra_de(libro, capitulo, semilla, cuantos=PASOS_DE_MUESTRA, raiz=None):
    """`[(id_del_nodo, numero_de_paso, texto)]`, estable para esa semilla."""
    pasos = []
    for nodo in candidatos_de(libro, capitulo, raiz):
        identificador = nodo.get("id", "?")
        for numero, texto in enumerate(nodo.get("pasos_accionables") or [], 1):
            pasos.append((identificador, numero, texto))
    pasos.sort(key=lambda p: _orden(semilla, "%s#%d" % (p[0], p[1])))
    return sorted(pasos[:cuantos], key=lambda p: (p[0], p[1]))


def texto(libro, capitulos, semilla, raiz=None):
    entero, muestreados = repartir(capitulos, semilla)
    partes = [
        "MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO (D.58)",
        "  libro    : %s" % libro,
        "  semilla  : %s" % semilla,
        "  capitulos: %s" % ", ".join(capitulos),
        "",
        "  RELEIDO ENTERO : %s" % entero,
        "  POR MUESTRA    : %s, %d pasos cada uno"
        % (", ".join(muestreados) or "ninguno", PASOS_DE_MUESTRA),
        "",
        "  EL DISPARADOR: si la muestra de un capitulo pasa del %.0f por ciento de"
        % TOPE_DE_ESCALADA,
        "  pasos inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.",
    ]
    for capitulo in muestreados:
        pasos = muestra_de(libro, capitulo, semilla, raiz=raiz)
        partes.append("")
        partes.append("  --- %s: %d paso(s) en la muestra" % (capitulo, len(pasos)))
        for identificador, numero, cuerpo in pasos:
            partes.append("    %-46s P%-3d %s"
                          % (identificador[:46], numero,
                             " ".join((cuerpo or "").split())[:60]))
    entero_pasos = sum(len(n.get("pasos_accionables") or [])
                       for n in candidatos_de(libro, entero, raiz)) if entero else 0
    partes.append("")
    partes.append("  --- %s: ENTERO, %d paso(s), no hay muestra que elegir"
                  % (entero, entero_pasos))
    return "\n".join(partes)


def main(argumentos=None):
    comun.salida_utf8()
    argumentos = list(argumentos if argumentos is not None else sys.argv[1:])

    def valor(bandera, defecto=None):
        return (argumentos[argumentos.index(bandera) + 1]
                if bandera in argumentos else defecto)

    libro = valor("--libro")
    capitulos = [c.strip() for c in (valor("--capitulos") or "").split(",") if c.strip()]
    semilla = valor("--semilla")
    if not (libro and capitulos and semilla):
        print('uso: python scripts/muestra_fidelidad.py --libro <clave> '
              '--capitulos cap_06,cap_07,cap_08 --semilla <texto>')
        print("")
        print("  LA SEMILLA SE ESCRIBE EN EL REPORTE, y sin ella la muestra no se")
        print("  puede reproducir. Una muestra que no se reproduce no es una muestra:")
        print("  es una eleccion, y el que elige sus pasos elige su resultado.")
        return 2
    print(texto(libro, capitulos, semilla))
    return 0


if __name__ == "__main__":
    sys.exit(main())
