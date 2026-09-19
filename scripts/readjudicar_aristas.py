# -*- coding: utf-8 -*-
"""RE ADJUDICA LAS LINEAS DE ARISTA QUE LLEVAN UN VEREDICTO TECLEADO (D.53).

    python scripts/readjudicar_aristas.py --ver       que haria, sin escribir
    python scripts/readjudicar_aristas.py --aplicar   lo escribe, con correccion declarada

EL DEFECTO. Hasta el 18 sep 2026, `src/arista.py` tecleaba `"veredicto": "CONTINUA"` en
**toda** arista declarada por lectura. Eso escribio **`93` lineas** de
`bitacora/VEREDICTOS.jsonl`, que es **la sede de `CLASE`**, contra una regla que la casa ya
tenia escrita desde el `17 sep`:

    D.53: UN SANO PUEDE LLEVAR ARISTA DECLARADA, Y DECLARARLA NO LO CONVIERTE
          EN CONTINUA.

**La vuelta 44 gasto una tarea entera re adjudicando dos pares a `SANO` citando `D.53` y,
en el mismo turno, escribio ocho `CONTINUA` nuevos por esa linea de codigo.**

COMO SE RE ADJUDICA CADA UNA, Y NO ES POR CRITERIO MIO. **Contra la lectura que la
origino**: se busca en la misma bitacora otra linea **del mismo par** que NO sea de arista
y que traiga un veredicto de lectura. Eso es lo que alguien leyo de ese par.

    leida CONTINUA ....... se queda. Era cierta, y ahora lleva su cita
    leida SANO ........... se corrige a SANO: la arista no lo convertia en CONTINUA
    sin lectura propia ... se corrige a SIN LECTURA PROPIA

**`SIN LECTURA PROPIA` NO ES UN VEREDICTO NUEVO: ES LA AUSENCIA DE UNO, DICHA.** Poner
`SANO` ahi seria inventar una lectura que nadie hizo, que es exactamente el defecto que
esto repara, cometido en la otra direccion.

NO BORRA NADA. El valor viejo queda en `veredicto_original` y la correccion se escribe
dentro de `razon`, con su cita, como manda `D.13`.
"""

import collections
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)

from src import cerrojo, comun  # noqa: E402

MARCA = "arista declarada por lectura"
DE_LECTURA = ("SANO", "CONTINUA", "REPITE")
SIN_LECTURA = "SIN LECTURA PROPIA"
COMMIT_DEL_DEFECTO = "src/arista.py linea 182, vigente hasta el 18 sep 2026"


def _par(linea):
    return tuple(sorted([str(linea.get("candidato", "")),
                         str(linea.get("vecino", ""))]))


def es_arista(linea):
    return str(linea.get("operacion", "")).startswith(MARCA)


def lecturas_por_par(lineas):
    """Lo que alguien leyo de cada par, FUERA de las lineas de arista."""
    mapa = collections.defaultdict(list)
    for linea in lineas:
        if es_arista(linea):
            continue
        if linea.get("veredicto") in DE_LECTURA:
            mapa[_par(linea)].append(linea)
    return mapa


def revisar(lineas=None):
    """`[(numero, linea, veredicto_nuevo, origen)]` para cada linea de arista."""
    lineas = comun.leer_jsonl(comun.RUTA_VEREDICTOS) if lineas is None else lineas
    mapa = lecturas_por_par(lineas)
    plan = []
    for numero, linea in enumerate(lineas, 1):
        if not es_arista(linea):
            continue
        lecturas = mapa.get(_par(linea), [])
        clases = [l["veredicto"] for l in lecturas]
        if "CONTINUA" in clases:
            nuevo, origen = "CONTINUA", "leida CONTINUA"
        elif "SANO" in clases:
            nuevo, origen = "SANO", "leida SANO"
        elif clases:
            nuevo, origen = clases[0], "leida %s" % clases[0]
        else:
            nuevo, origen = SIN_LECTURA, "sin lectura propia del par"
        plan.append((numero, linea, nuevo, origen))
    return plan


def aplicar(plan, lineas):
    """Escribe la re adjudicacion. Devuelve cuantas cambiaron."""
    cambiadas = 0
    for numero, linea, nuevo, origen in plan:
        viejo = linea.get("veredicto")
        linea["cita_del_veredicto"] = origen
        if viejo == nuevo:
            continue
        linea["veredicto_original"] = viejo
        linea["veredicto"] = nuevo
        linea["razon"] = (str(linea.get("razon", "")).rstrip()
                          + " CORRECCION DECLARADA (18 sep 2026, D.53): el veredicto de "
                            "esta linea decia %r porque %s lo tecleaba en TODA arista "
                            "declarada por lectura. La lectura de este par dice %r, y "
                            "D.53 manda que el veredicto y la arista sean puertas "
                            "distintas. El valor viejo queda en veredicto_original y no "
                            "se borra." % (viejo, COMMIT_DEL_DEFECTO, origen))
        cambiadas += 1
    return cambiadas


def texto(plan):
    cuenta = collections.Counter(origen for _n, _l, _v, origen in plan)
    partes = ["RE ADJUDICACION DE ARISTAS (D.53)",
              "  poblacion: %s, sin filtrar" % comun.relativa(comun.RUTA_VEREDICTOS),
              "  lineas de arista declarada por lectura: %d" % len(plan), ""]
    for origen, cuantas in sorted(cuenta.items(), key=lambda x: -x[1]):
        partes.append("  %-26s %d" % (origen, cuantas))
    cambian = len([1 for _n, l, v, _o in plan if l.get("veredicto") != v])
    partes.append("")
    partes.append("  cambian de veredicto : %d" % cambian)
    partes.append("  se quedan como estan : %d" % (len(plan) - cambian))
    return "\n".join(partes)


def main(argumentos=None):
    comun.salida_utf8()
    argumentos = list(argumentos if argumentos is not None else sys.argv[1:])
    lineas = comun.leer_jsonl(comun.RUTA_VEREDICTOS)
    plan = revisar(lineas)
    print(texto(plan))

    if "--aplicar" not in argumentos:
        print("")
        print("NADA ESCRITO: esto fue --ver. Con --aplicar se escribe.")
        return 0

    with cerrojo.tomar(comun.RUTA_VEREDICTOS, avisar=lambda m: print("  " + m)):
        cambiadas = aplicar(plan, lineas)
        comun.escribir_jsonl(comun.RUTA_VEREDICTOS, lineas)
    print("")
    print("ESCRITAS: %d lineas re adjudicadas, %d ya estaban bien."
          % (cambiadas, len(plan) - cambiadas))
    print("Ninguna se borro: el valor viejo vive en veredicto_original.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
