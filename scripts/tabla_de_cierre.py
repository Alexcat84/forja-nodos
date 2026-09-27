# -*- coding: utf-8 -*-
"""LA TABLA DE CIERRE DE TAREAS SALE DE UN INSTRUMENTO (D.52, 17 sep 2026).

    python scripts/tabla_de_cierre.py              la comprueba y dice que cae
    python scripts/tabla_de_cierre.py --escribir   regenera su fichero de salida
    python scripts/tabla_de_cierre.py --hook       lo mismo, callado si esta verde

POR QUE EXISTE, Y ES LA UNICA GUARDA QUE NACE DE TRES TANDAS MEDIDAS. La racha
`REPORTE` de la linea serial llego a `3 de 3` tres veces seguidas, y **las tres caidas
son la misma figura y la misma tabla**:

    ACTA 32, vuelta 33   13 vecindades levantadas donde se levantaron 11
    ACTA 33, vuelta 34   0 PUENTE de 181 donde la relectura da 1
    ACTA 34, vuelta 35   15 de 15 DEL CAPITULO donde cap_09 son 20 de 20

**LA TABLA DE CIERRE DE TAREAS ES LA UNICA DEL REPORTE QUE NO DECLARA INSTRUMENTO**, y
por eso `D.41` no la mira: el tallado compara tablas contra su fichero de salida, y esta
no tiene ninguno. **Es, literalmente, la tabla donde una cifra tecleada vive tranquila.**

QUE HACE. Lee la tabla de cierre de la ULTIMA vuelta del reporte, **recomputa del dato
cada cifra que sabe medir**, y emite la tabla corregida a su fichero de salida. El reporte
pega esa salida, y a partir de ahi `D.41` la compara celda a celda como a las demas.

LO QUE SABE MEDIR, Y SOLO ESO. Una afirmacion de la forma

    `N` de `M` del capitulo            con un `cap_NN` nombrado en la misma fila

donde `M` es **cuantos nodos del grafo salen de ese capitulo**. Es la caida de la vuelta
35 exactamente: `15 de 15 del capitulo` cuando el capitulo son `20`.

LO QUE NO INVENTA. Una fila sin cifra medible **se copia tal cual y se declara
`SIN COMPROBAR`**. Un instrumento que rellena lo que no sabe no mide: dicta. Y el patron
es **estrecho a proposito**: `de 5 de 5` de un TRAMO no se toca, porque un tramo no es un
capitulo y esta casa ya pago dos veces el precio de una guarda con falsos positivos.
"""

import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)

from src import comun  # noqa: E402

RUTA_REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")
SALIDA_POR_DEFECTO = os.path.join("docs", "loop", "TABLA_DE_CIERRE.txt")

# La cabecera que identifica la tabla, sin depender del titulo de la seccion: los
# titulos cambian de vuelta en vuelta y la cabecera de esta tabla no.
CABECERA = re.compile(r"^\|\s*#\s*\|\s*tarea\s*\|\s*como\s+cerro\s*\|\s*$", re.I)
SEPARADOR = re.compile(r"^\|[\s:|-]+\|$")

# LA AFIRMACION QUE SE MIDE, y nada mas: `N` de `M` del capitulo. El adorno de la casa
# (comillas invertidas, negrita) va contemplado, y `del capitulo` es obligatorio.
AFIRMACION = re.compile(
    r"(\*{0,2}`?(\d+)`?\*{0,2})\s+de\s+(\*{0,2}`?(\d+)`?\*{0,2})\s+del\s+capitulo",
    re.I)
CAPITULO = re.compile(r"cap_(\d+)")


def _celdas(linea):
    trozo = linea.strip()
    if trozo.startswith("|"):
        trozo = trozo[1:]
    if trozo.endswith("|"):
        trozo = trozo[:-1]
    return [c.strip() for c in trozo.split("|")]


def tabla_de(texto):
    """`(numero_de_linea, [lineas de la tabla])` de la ULTIMA tabla de cierre."""
    lineas = (texto or "").split("\n")
    encontrada = None
    for n, linea in enumerate(lineas):
        if not CABECERA.match(linea.strip()):
            continue
        if n + 1 >= len(lineas) or not SEPARADOR.match(lineas[n + 1].strip()):
            continue
        fin = n + 2
        while fin < len(lineas) and lineas[fin].strip().startswith("|"):
            fin += 1
        encontrada = (n + 1, lineas[n:fin])
    return encontrada if encontrada else (0, [])


def nodos_del_capitulo(clave, capitulo, nodos=None):
    """Cuantos nodos del grafo salen de `<clave>/<capitulo>.md`, y sus pasos.

    SE MIDE POR LA RUTA COMPLETA y no por el nombre suelto del capitulo: `cap_09` a
    secas aparece tambien en nodos de OTROS libros y en prosa que lo menciona. Con la
    ruta entera, el `20` de esta casa sale al digito contra el lector del auditor.
    """
    nodos = comun.leer_jsonl(comun.RUTA_DATASET) if nodos is None else nodos
    aguja = "%s/%s.md" % (clave, capitulo)
    cuantos, pasos = 0, 0
    for nodo in nodos:
        if aguja in json.dumps(nodo, ensure_ascii=False):
            cuantos += 1
            pasos += len(nodo.get("pasos_accionables") or [])
    return cuantos, pasos


def _clave_del_libro():
    """El libro de la linea, del tablero. Sin tablero, el del lote abierto."""
    try:
        from src import credito, tablero
        clave, _motivo, _relevo = tablero.siguiente_por_prioridad(
            credito.linea_actual())
        if clave:
            return clave
    except Exception:
        pass
    return ""


def revisar(texto=None, clave=None, nodos=None):
    """`(filas, dictamenes)`. Cada dictamen dice que paso con esa fila."""
    texto = comun.leer_texto(RUTA_REPORTE) if texto is None else texto
    clave = _clave_del_libro() if clave is None else clave
    nodos = comun.leer_jsonl(comun.RUTA_DATASET) if nodos is None else nodos
    numero, lineas = tabla_de(texto)
    if not lineas:
        return [], [{"estado": "SIN OBJETO",
                     "motivo": "el reporte no trae ninguna tabla de cierre de tareas"}]

    dictamenes = []
    corregidas = list(lineas[:2])           # cabecera y separador, intactas
    for cruda in lineas[2:]:
        celdas = _celdas(cruda)
        fila = celdas[0] if celdas else "?"
        capitulos = CAPITULO.findall(cruda)
        encaje = AFIRMACION.search(cruda)
        if not encaje or not capitulos:
            corregidas.append(cruda)
            dictamenes.append({"fila": fila, "estado": "SIN COMPROBAR",
                               "motivo": "ninguna afirmacion de la forma "
                                         "'N de M del capitulo' con su cap_NN"})
            continue
        capitulo = "cap_%s" % capitulos[-1]
        medidos, pasos = nodos_del_capitulo(clave, capitulo, nodos)
        declarado = int(encaje.group(4))
        if medidos == declarado:
            corregidas.append(cruda)
            dictamenes.append({"fila": fila, "estado": "CUADRA",
                               "motivo": "%s son %d en el grafo, y la celda dice %d"
                                         % (capitulo, medidos, declarado)})
            continue
        buena = cruda.replace(encaje.group(0),
                              "%s de **`%d`** del capitulo"
                              % (encaje.group(1), medidos), 1)
        corregidas.append(buena)
        dictamenes.append({
            "fila": fila, "estado": "DIFIERE", "capitulo": capitulo,
            "declarado": declarado, "medido": medidos, "pasos": pasos,
            "motivo": "la celda publica '%s de %s del capitulo' y %s son %d de %d en el "
                      "grafo (%d pasos)"
                      % (encaje.group(2), encaje.group(4), capitulo, medidos, medidos,
                         pasos),
            "linea": numero})
    return corregidas, dictamenes


def texto_salida(corregidas, clave):
    cabeza = [
        "$ python scripts/tabla_de_cierre.py --escribir",
        "poblacion: dataset/nodos.jsonl entero, libro %s" % (clave or "sin declarar"),
        "criterio : un nodo sale de un capitulo si cita %s/<cap>.md" % (clave or "?"),
        "",
    ]
    return "\n".join(cabeza + list(corregidas)) + "\n"


def main(argumentos=None):
    comun.salida_utf8()
    argumentos = list(argumentos if argumentos is not None else sys.argv[1:])
    hook = "--hook" in argumentos
    escribir = "--escribir" in argumentos
    salida = SALIDA_POR_DEFECTO
    if "--salida" in argumentos:
        salida = argumentos[argumentos.index("--salida") + 1]

    if not os.path.exists(RUTA_REPORTE):
        print("TABLA DE CIERRE SIN OBJETO: no hay %s en el arbol."
              % comun.relativa(RUTA_REPORTE))
        return 0

    clave = _clave_del_libro()
    corregidas, dictamenes = revisar(clave=clave)
    difieren = [d for d in dictamenes if d.get("estado") == "DIFIERE"]

    if escribir:
        comun.escribir_texto(os.path.join(RAIZ, salida),
                             texto_salida(corregidas, clave))

    if hook and not difieren:
        return 0

    print("=" * 76)
    print("TABLA DE CIERRE DE TAREAS (D.52): toda tabla del reporte declara su "
          "instrumento")
    print("=" * 76)
    print("  libro de la linea : %s" % (clave or "sin declarar"))
    print("  filas             : %d" % len([d for d in dictamenes if "fila" in d]))
    for dictamen in dictamenes:
        print("  %-14s %s  %s" % (dictamen.get("estado", "?"),
                                  dictamen.get("fila", ""), dictamen.get("motivo", "")))
    if escribir:
        print("")
        print("ESCRITA la tabla regenerada en %s" % salida)
    if not difieren:
        print("")
        print("TABLA DE CIERRE VERDE: ninguna celda medible difiere del dato.")
        return 0
    print("")
    print("TABLA DE CIERRE EN ROJO: %d fila(s) publican una cifra que el dato no da."
          % len(difieren))
    print("NO SE CORRIGE TECLEANDO LA CELDA BUENA: se regenera con --escribir y se "
          "pega.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
