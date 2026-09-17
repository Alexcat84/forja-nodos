# -*- coding: utf-8 -*-
"""EL TESTIGO DE GUARDAS AL SELLAR: UNA CIFRA VALE EN EL INSTANTE DEL SELLO.

    python scripts/testigo_guardas.py --escribir            corre y deja el testigo
    python scripts/testigo_guardas.py --comprobar <pagina>  cruza la pagina con el

POR QUE EXISTE, Y ES UN CASO EXACTO. La apertura ciega de la vuelta 29 publico
**`guardas en rojo: 2`** y lo sostuvo con la salida literal de su instrumento, que
**era verde cuando corrio**. Entre esa corrida y el sello pasaron **44 minutos**, y
en medio los ficheros de trabajo del propio auditor **metieron cinco guiones largos
en el arbol**. Tres segundos despues del sello, el `pre-commit` los imprimio.

> **LA CIFRA ERA CIERTA AL MEDIRSE Y FALSA AL PUBLICARSE**, y ninguna regla de esta
> casa cubria eso: `D.38.3` exige que la cifra **tenga** instrumento, no que el
> instrumento **siga siendo cierto** al publicar.

LO QUE HACE. Justo antes de sellar, el arnes corre las guardas baratas y deja junto
al sello **la verdad del arbol en ese instante**: la hora, la salida de cada guarda
y el hash del arbol. **No juzga la pagina.** Lo unico que hace imposible es que una
medida caduque **sin que quede constancia de que caduco.**

Y LO QUE SI COMPRUEBA, QUE ES MECANICO Y NO SEMANTICO:

> **SI UNA GUARDA ESTA EN ROJO EN EL INSTANTE DEL SELLO, EL SELLO NO SE ACEPTA, Y
> EL ARNES DICE CUAL.**

**LA PRIMERA VERSION DE ESTO INTENTABA LEER LA PAGINA** (*si el testigo dice rojo y
la pagina no lo dice, se rechaza*) **y no servia**: en una pagina de seiscientas
lineas que habla de las guardas, cualquier heuristica encuentra una linea con
`guion` y `rojo` cerca. **Lo probe contra la pagina de la vuelta 29 y la daba por
buena.** Una guarda que se deja convencer por la prosa no guarda nada.

**ASI QUE NO SE LEE LA PAGINA.** Un rojo en el instante del sello significa que la
pagina cerro sobre un arbol que ya no era el que midio, **y eso vale para cualquier
cifra suya, no solo para las que hablen de guardas.** El remedio que el propio
auditor se escribio dice lo mismo por el otro lado: *la tabla de cierre se escribe
DESPUES de volver a correr las guardas.* **Si al sellar hay un rojo, esa tabla no se
escribio despues.**

Con este testigo, la caida de la vuelta 29 habria sido **verde a las 09:57 y
detenida a las 10:41 por la maquina**, con el nombre de la guarda delante y sin
gastar una racha.

LO QUE NO HACE, y conviene decirlo para no vender de mas: **no comprueba que las
cifras de la pagina sean ciertas.** Comprueba que el estado de las guardas que la
pagina afirma **no contradiga** el que habia al sellar. Lo demas lo caza una lectura.
"""

import io
import json
import os
import re
import subprocess
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_TESTIGO = os.path.join(RAIZ, "docs", "loop", "TESTIGO_GUARDAS.json")

# LAS BARATAS, Y SOLO LAS BARATAS. Esto corre dentro de la fase ciega, justo antes
# del sello: lo que cueste minutos aqui se paga en cada vuelta.
GUARDAS = (
    ("gate", [sys.executable, "forja.py", "gate"]),
    ("guiones", [sys.executable, "forja.py", "guiones"]),
    ("censo_rutas", [sys.executable, os.path.join("scripts", "censar_rutas.py")]),
    # D.53 punto 3 (17 sep 2026): UNA CITA DEL REGISTRO DE CREDITO ES UNA
    # REFERENCIA, NUNCA UN RESULTADO COPIADO. Va al sello y no solo a `anotar`
    # porque `anotar` solo mira lo que se escribe por el instrumento: una linea
    # anadida a mano al fichero no pasaria por ahi, y el sello mide el ARBOL.
    ("citas_de_credito", [sys.executable, "forja.py", "credito", "--citas"]),
)


def _correr(orden):
    proceso = subprocess.Popen(orden, cwd=RAIZ, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    crudo = proceso.communicate()[0]
    return proceso.returncode, crudo.decode("utf-8", "replace")


def _hash_del_arbol():
    """Lo que git ve del arbol AHORA, incluido lo no commiteado."""
    try:
        salida = subprocess.check_output(["git", "status", "--porcelain"], cwd=RAIZ,
                                         stderr=subprocess.DEVNULL)
        cabeza = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=RAIZ,
                                         stderr=subprocess.DEVNULL)
        import hashlib
        return (cabeza.decode().strip()[:12],
                hashlib.sha256(salida).hexdigest()[:16])
    except Exception:
        return ("sin-commit", "sin-arbol")


def escribir(ruta=None):
    """Corre las guardas y deja el testigo. Devuelve lo escrito."""
    ruta = ruta or RUTA_TESTIGO
    commit, arbol = _hash_del_arbol()
    testigo = {"fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
               "commit": commit, "huella_del_arbol": arbol, "guardas": {}}
    for nombre, orden in GUARDAS:
        codigo, texto = _correr(orden)
        testigo["guardas"][nombre] = {
            "estado": "VERDE" if codigo == 0 else "ROJO",
            "codigo": codigo,
            # La cola, que es donde estas guardas ponen su veredicto.
            "salida": chr(10).join(texto.strip().split(chr(10))[-6:]),
        }
    carpeta = os.path.dirname(ruta)
    if carpeta and not os.path.isdir(carpeta):
        os.makedirs(carpeta)
    with io.open(ruta, "w", encoding="utf-8", newline=chr(10)) as f:
        f.write(json.dumps(testigo, ensure_ascii=False, indent=2) + chr(10))
    return testigo


def leer(ruta=None):
    ruta = ruta or RUTA_TESTIGO
    try:
        return json.loads(io.open(ruta, encoding="utf-8").read())
    except (IOError, ValueError):
        return None


def rojas(testigo):
    return sorted(n for n, d in (testigo.get("guardas") or {}).items()
                  if d.get("estado") == "ROJO")


def comprobar(ruta_pagina=None, testigo=None, ruta_testigo=None):
    """Devuelve lo que impide aceptar el sello. Vacia es verde.

    NO SE LEE LA PAGINA, y es deliberado: ver el docstring de arriba. Lo que se
    comprueba es el ARBOL en el instante del sello.
    """
    if testigo is None:
        testigo = leer(ruta_testigo)
    if testigo is None:
        return ["no hay testigo de guardas: el arnes no lo escribio antes de sellar"]
    impiden = []
    for guarda in rojas(testigo):
        primera = (testigo["guardas"][guarda].get("salida") or "").split(chr(10))[0]
        impiden.append(
            "la guarda '%s' estaba en ROJO en el instante del sello (%s). Una cifra "
            "vale en el instante del sello (D.38.3, 16 sep 2026): si al cerrar hay un "
            "rojo, la tabla de cierre no se escribio DESPUES de volver a correr las "
            "guardas. %s" % (guarda, testigo.get("fecha", "sin hora"), primera))
    return impiden


def texto_informe(testigo):
    lineas = ["=" * 76,
              "TESTIGO DE GUARDAS AL SELLAR (D.38.3, 16 sep 2026)",
              "=" * 76,
              "hora            : %s" % testigo["fecha"],
              "commit          : %s" % testigo["commit"],
              "huella del arbol: %s" % testigo["huella_del_arbol"]]
    for nombre in sorted(testigo["guardas"]):
        dato = testigo["guardas"][nombre]
        lineas.append("  %-12s %s" % (nombre, dato["estado"]))
    rojo = rojas(testigo)
    lineas.append("")
    if rojo:
        lineas.append("GUARDAS EN ROJO AL SELLAR: %s" % ", ".join(rojo))
        lineas.append("La pagina sellada TIENE QUE DECIRLO, o el sello no se acepta.")
    else:
        lineas.append("LAS %d GUARDAS EN VERDE EN EL INSTANTE DEL SELLO."
                      % len(testigo["guardas"]))
    return chr(10).join(lineas)


def main(argumentos=None):
    argumentos = list(argumentos if argumentos is not None else sys.argv[1:])
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8")
        except Exception:
            pass
    if "--comprobar" in argumentos:
        impiden = comprobar()
        if not impiden:
            print("EL SELLO SE ACEPTA: las guardas estaban en verde en su instante.")
            return 0
        print("EL SELLO NO SE ACEPTA: %d guarda(s) en rojo al sellar." % len(impiden))
        for cosa in impiden:
            print("  " + cosa)
        return 1
    testigo = escribir()
    print(texto_informe(testigo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
