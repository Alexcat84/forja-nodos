# -*- coding: utf-8 -*-
"""LA PRUEBA DE ACEPTACION DE LA CALIBRACION: la aduana contra el catalogo limpio.

    python calibracion/aduana_sobre_muestra.py [--cuantos 50]

LA VARA, escrita antes de los numeros:

> **UN CATALOGO AUDITADO QUE LA ADUANA RECHAZARA EN MASA ES LA ADUANA MAL
> CALIBRADA, NO EL CATALOGO.**

Los 3.169 vivos del grafo de referencia pasaron una campaña entera de cribado,
fusion y auditoria integral. Si la aduana de esta forja los tumba, el problema
esta aqui.

LA DISTINCION QUE ESTE INSTRUMENTO NO PUEDE CONFUNDIR, y es la mitad del valor
de la prueba:

  - **CAER** es un RECHAZO: una guarda dice que el nodo no puede entrar. Sobre un
    catalogo auditado, cada caida hay que explicarla.
  - **BLOQUEAR** NO es un rechazo: es la cola de lectura. Un nodo bloqueado entra
    en cuanto alguien escribe su veredicto. Bloquear mucho es caro; bloquear no
    es tumbar.

Y dentro de las caidas hay dos especies que NO se arreglan igual:

  - caida por CALIBRACION (una señal mal puesta): se arregla aqui, moviendo un
    umbral, y es trabajo de esta sesion;
  - caida por DOCTRINA (las reglas de id de esta casa son mas estrictas que las
    que aquella campaña aplico): **no se arregla moviendo un umbral, y no se
    arregla sin el fundador.** Aflojar una regla de id para que entre un lote es
    exactamente lo que el manual llama inventar reglas en caliente.

El instrumento separa las dos y las cuenta por separado.

NO ESCRIBE NADA EN EL REPO: monta un dataset de usar y tirar en un temporal, le
pasa la tabla de fuentes derivada del catalogo por FORJA_FUENTES, y corre el
MODO INFORME, que ya es de solo lectura.
"""

import io
import json
import os
import shutil
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src import comun, informe  # noqa: E402
import referencia  # noqa: E402

SEMILLA = 20260909


def main(argumentos=None):
    comun.salida_utf8()
    argumentos = list(argumentos or sys.argv[1:])
    cuantos = 50
    if "--cuantos" in argumentos:
        cuantos = int(argumentos[argumentos.index("--cuantos") + 1])

    datos_corte = referencia.corte()
    ref = referencia.Referencia()
    muestra = ref.muestra_de_vivos(cuantos, SEMILLA)

    taller = tempfile.mkdtemp(prefix="aduana_muestra_")
    try:
        dataset = os.path.join(taller, "nodos.jsonl")
        comun.escribir_texto(dataset, "")
        tabla = os.path.join(taller, "FUENTES.json")
        comun.escribir_texto(tabla, json.dumps(ref.tabla_de_fuentes(),
                                               ensure_ascii=False))
        rutas = []
        for identificador in muestra:
            ruta = os.path.join(taller, "%s.json" % identificador)
            with io.open(ruta, "w", encoding="utf-8") as f:
                json.dump(ref.nodos[identificador], f, ensure_ascii=False)
            rutas.append(ruta)

        dictamenes, cuantos_nodos, umbrales, _archivados = informe.revisar(
            rutas, ruta_dataset=dataset,
            tabla_fuentes=comun.leer_json(tabla))
    finally:
        shutil.rmtree(taller, ignore_errors=True)

    print("=" * 78)
    print("LA ADUANA CONTRA EL CATALOGO LIMPIO: %d nodos vivos" % len(muestra))
    print("=" * 78)
    print("grafo de referencia : %s (%s)" % (datos_corte["commit"], datos_corte["tag"]))
    print("semilla de la muestra: %d" % SEMILLA)
    print("umbrales de la corrida: similitud %.2f | familia %.2f | paso %.2f"
          % (umbrales["umbral_similitud_texto"], umbrales["umbral_familia_id"],
             umbrales["umbral_paso_contra_nodo"]))
    print("dataset de destino  : vacio y de usar y tirar (los candidatos se miden")
    print("                      entre ellos, que es el caso mas exigente)")
    print("")

    caidas = [d for d in dictamenes if d["salida"] == informe.CAERIA]
    bloqueos = [d for d in dictamenes if d["salida"] == informe.BLOQUEARIA]
    entran = [d for d in dictamenes if d["salida"] == informe.ENTRARIA]
    chocan = [d for d in dictamenes if d["salida"] == informe.CHOCA]

    print("EL SALDO")
    print("  ENTRARIAN sin leer nada         : %d" % len(entran))
    print("  BLOQUEARIAN (cola de lectura)   : %d" % len(bloqueos))
    print("  CHOCAN entre si                 : %d" % len(chocan))
    print("  CAERIAN (RECHAZO)               : %d" % len(caidas))
    print("")
    print("  ACEPTADOS = ENTRARIAN + BLOQUEARIAN = %d de %d  (%.1f por ciento)"
          % (len(entran) + len(bloqueos), len(muestra),
             100.0 * (len(entran) + len(bloqueos)) / len(muestra)))
    print("")

    por_guarda = {}
    for dictamen in caidas:
        por_guarda.setdefault(dictamen["guarda"], []).append(dictamen)
    if por_guarda:
        print("LAS CAIDAS, POR GUARDA Y POR ESPECIE")
        for guarda, lista in sorted(por_guarda.items(), key=lambda x: -len(x[1])):
            especie = ("DOCTRINA (regla de esta casa, no se mueve sin el fundador)"
                       if "REGLAS_DE_ID" in guarda else
                       "CALIBRACION o MAPEO (se arregla midiendo)")
            print("")
            print("  %d  %s" % (len(lista), guarda))
            print("      especie: %s" % especie)
            for dictamen in lista[:8]:
                print("      %s" % dictamen["id"])
                for detalle in dictamen["detalles"][:2]:
                    print("         %s" % detalle)
            if len(lista) > 8:
                print("      ... y %d mas" % (len(lista) - 8))

    if bloqueos:
        largos = sorted(len(d["vecinos"]) for d in bloqueos)
        print("")
        print("LA COLA QUE ABRIRIAN LOS BLOQUEADOS (entre ellos mismos)")
        print("  vecinos por candidato bloqueado: menor %d, mediana %d, mayor %d"
              % (largos[0], largos[len(largos) // 2], largos[-1]))

    print("")
    print("LA VARA: un catalogo auditado que la aduana rechazara en masa seria la")
    print("aduana mal calibrada. Aceptados el %.1f por ciento."
          % (100.0 * (len(entran) + len(bloqueos)) / len(muestra)))

    # ------------------------------------------------------------------------
    # EL BARRIDO ENTERO, porque una muestra de 50 estima y un barrido cuenta.
    # Las dos guardas que tumban son BARATAS (no usan difflib), asi que se
    # pueden correr sobre los 3.169 vivos y dar la cifra exacta en vez de una
    # proyeccion. El fundador decide sobre cifras, no sobre estimaciones.
    # ------------------------------------------------------------------------
    from src import reglas_id
    rotos_id = []
    con_guion = []
    for identificador in ref.vivos:
        nodo = ref.nodos[identificador]
        fallos = reglas_id.validar(nodo.get("id"), "id")
        if fallos:
            rotos_id.append((identificador, fallos[0]))
        for campo, texto in comun.textos_de_nodo(nodo):
            if comun.buscar_guiones(texto):
                con_guion.append((identificador, campo))
                break

    print("")
    print("=" * 78)
    print("EL BARRIDO ENTERO SOBRE LOS %d VIVOS (contado, no estimado)" % len(ref.vivos))
    print("=" * 78)
    print("  ids que rompen docs/REGLAS_DE_ID.md : %d de %d  (%.1f por ciento)"
          % (len(rotos_id), len(ref.vivos), 100.0 * len(rotos_id) / len(ref.vivos)))
    motivos = {}
    for _, fallo in rotos_id:
        clave = ("sufijo numerico" if "sufijo numerico" in fallo else
                 "preposicion o articulo" if "preposicion" in fallo else
                 "fuera del castellano" if "castellano" in fallo else
                 "una sola pieza" if "una palabra suelta" in fallo else
                 "forma (mayusculas, digito inicial, acentos)")
        motivos[clave] = motivos.get(clave, 0) + 1
    for motivo, cuantos in sorted(motivos.items(), key=lambda x: -x[1]):
        print("      %5d  %s" % (cuantos, motivo))
    print("  nodos con guion largo o medio en su texto : %d de %d  (%.1f por ciento)"
          % (len(con_guion), len(ref.vivos), 100.0 * len(con_guion) / len(ref.vivos)))
    limpios = len(ref.vivos) - len(set(i for i, _ in rotos_id) | set(i for i, _ in con_guion))
    print("")
    print("  VIVOS QUE PASARIAN LAS DOS GUARDAS DE DOCTRINA: %d de %d (%.1f por ciento)"
          % (limpios, len(ref.vivos), 100.0 * limpios / len(ref.vivos)))
    print("")
    print("  NINGUNA de estas dos guardas es de CALIBRACION: son reglas de esta")
    print("  casa (D.12 y docs/REGLAS_DE_ID.md), mas estrictas que las que aquella")
    print("  campaña aplico. Moverlas no es medir: es decision del fundador.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
