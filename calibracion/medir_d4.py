# -*- coding: utf-8 -*-
"""LA MEDICION DE D.4: los umbrales contra la distribucion, no contra sus casos.

    python calibracion/medir_d4.py

QUE EXIGE D.4 Y LA COSECHA SECCION 4, y esta lista es el indice de lo que este
instrumento imprime:

  1. la distribucion de las tres señales sobre los pares del catalogo
     (p50, p90, p99)
  2. la banda por tramo de cada una
  3. la tasa de acierto por tramo separando GEMELO de JERARQUIA por el 9.19

LAS DOS AVERIAS DE `costuras_internas.py` QUE LA COSECHA DOCUMENTA, y que este
instrumento mide a proposito:

  (a) EL CERO SILENCIOSO. Ya cubierto por `NoAplica` (D.16) desde la tanda A.
      Aqui se CUENTA cuantos pares caen fuera del dominio de cada señal, porque
      una señal que no aplica en la mitad del corpus es una señal que no mide lo
      que dice medir, aunque no devuelva cero.

  (b) EL UMBRAL POR DEBAJO DE LA MEDIANA. *El p50 de la señal nueva es 45,8, o
      sea que el umbral quedo POR DEBAJO DE LA MEDIANA. Disparar deja de ser
      noticia.* Por eso aqui no se publica un umbral sin su p50 al lado, y por
      eso la vara de aceptacion no es solo que cace a los gemelos: es **cuantos
      vecinos levanta por candidato**. Un umbral que levanta trescientos vecinos
      no ordena una cola: la entierra.

POR QUE SE MUESTREA, declarado antes de los numeros: 3.169 vivos son 5.019.696
pares, y las señales 1 y 3 usan difflib sobre textos de miles de caracteres. La
distribucion se estima sobre una MUESTRA AZAROSA CON SU SEMILLA, y el tamaño va
impreso en la salida. La señal 2 (familia de id) es barata y se mide sobre
TODOS los pares de la muestra de ajenos mas las dos clases enteras.

NINGUNA CIFRA DE ESTE FICHERO SE TECLEA EN NINGUN DOCUMENTO: se pega de su
salida, `calibracion/SALIDA_D4.txt`.
"""

import os
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src import aduana, comun  # noqa: E402
import referencia  # noqa: E402

SEMILLA = 20260909
MUESTRA_AJENOS = 4000
MUESTRA_GEMELOS = 671
MUESTRA_JERARQUIA = 800

# LA COLA SE MIDE DE DOS MANERAS, Y LAS DOS VAN PUBLICADAS.
#
# (1) POR ESTIMACION, que es la buena: la tasa de disparo de los AJENOS, medida
#     sobre MUESTRA_AJENOS pares, multiplicada por los vivos del catalogo. Sale
#     de 4.000 pares medidos y estima la cola falsa con precision.
# (2) POR CONTEO DIRECTO sobre MUESTRA_COLA candidatos contra TODOS los vivos.
#     Es carisima (cada candidato son 3.168 pares) y por eso la muestra es
#     corta: existe como CONTROL de la estimacion, no como su sustituto. Si las
#     dos no se parecen, la que manda es la directa y la discrepancia se declara.
MUESTRA_COLA = 10

NOMBRES = ("similitud_texto", "familia_id", "paso_contra_nodo")


def medir_par(nodo_a, nodo_b):
    """Las tres señales de la aduana de verdad, sin copia ni reimplementacion."""
    similitud = aduana.senal_similitud_texto(comun.texto_comparable(nodo_a),
                                             comun.texto_comparable(nodo_b))
    familia = aduana.senal_familia_id(nodo_a.get("id") or "", nodo_b.get("id") or "")
    paso, _ = aduana.senal_paso_contra_nodo(nodo_a, nodo_b)
    return {"similitud_texto": similitud, "familia_id": familia,
            "paso_contra_nodo": paso}


def percentil(valores, p):
    if not valores:
        return None
    ordenados = sorted(valores)
    indice = int(round((p / 100.0) * (len(ordenados) - 1)))
    return ordenados[indice]


def resumen(valores, no_aplica):
    if not valores:
        return "sin dato (NO APLICA en los %d pares)" % no_aplica
    return ("n %5d  NO_APLICA %4d  p50 %.3f  p75 %.3f  p90 %.3f  p95 %.3f  "
            "p99 %.3f  max %.3f"
            % (len(valores), no_aplica, percentil(valores, 50), percentil(valores, 75),
               percentil(valores, 90), percentil(valores, 95), percentil(valores, 99),
               max(valores)))


def medir_clase(nombre_clase, pares, nodos):
    """Mide las tres señales sobre una clase de pares. Devuelve dict por señal."""
    datos = dict((n, {"valores": [], "no_aplica": 0}) for n in NOMBRES)
    for a, b in pares:
        medidas = medir_par(nodos[a], nodos[b])
        for nombre, valor in medidas.items():
            if isinstance(valor, aduana.NoAplica):
                datos[nombre]["no_aplica"] += 1
            else:
                datos[nombre]["valores"].append(valor)
    return datos


def tasa_por_tramo(datos_gemelos, datos_jerarquia, datos_ajenos, nombre):
    """LA BANDA DEL 9.19: que clase vive en cada tramo de la señal.

    Por cada tramo de 0,1, cuantos pares de cada clase caen ahi. Es la
    medicion de la frase: la similitud alta caza duplicados, la media caza
    jerarquias.
    """
    tramos = [(i / 10.0, (i + 1) / 10.0) for i in range(10)]
    lineas = []
    lineas.append("  tramo        GEMELO  JERARQ   AJENO   | que domina el tramo")
    total = {}
    for clase, datos in (("GEMELO", datos_gemelos), ("JERARQ", datos_jerarquia),
                         ("AJENO", datos_ajenos)):
        total[clase] = len(datos[nombre]["valores"]) or 1
    for bajo, alto in tramos:
        cuenta = {}
        porcentaje = {}
        for clase, datos in (("GEMELO", datos_gemelos), ("JERARQ", datos_jerarquia),
                             ("AJENO", datos_ajenos)):
            valores = datos[nombre]["valores"]
            n = sum(1 for v in valores if bajo <= v < alto or (alto == 1.0 and v == 1.0))
            cuenta[clase] = n
            porcentaje[clase] = 100.0 * n / total[clase]
        manda = max(porcentaje, key=lambda c: porcentaje[c])
        if sum(cuenta.values()) == 0:
            veredicto = "vacio"
        else:
            veredicto = "%s (%.1f por ciento de su clase)" % (manda, porcentaje[manda])
        lineas.append("  %.1f a %.1f  %7d %7d %7d   | %s"
                      % (bajo, alto, cuenta["GEMELO"], cuenta["JERARQ"],
                         cuenta["AJENO"], veredicto))
    return lineas


def cobertura(datos, nombre, umbral):
    """Que parte de una clase levanta un umbral dado."""
    valores = datos[nombre]["valores"]
    if not valores:
        return 0.0, 0, 0
    levantados = sum(1 for v in valores if v >= umbral)
    return 100.0 * levantados / len(valores), levantados, len(valores)


def medir_cola(ref, candidatos, umbrales):
    """LA VARA OPERATIVA: cuantos vecinos levanta UN candidato contra el
    catalogo entero. Es la cifra que dice si disparar sigue siendo noticia."""
    colas = []
    for identificador in candidatos:
        candidato = ref.nodos[identificador]
        levantados = 0
        for otro in ref.vivos:
            if otro == identificador:
                continue
            medicion = aduana.medir(candidato, ref.nodos[otro], umbrales)
            if medicion["levantada_por"]:
                levantados += 1
        colas.append((identificador, levantados))
    return colas


def main():
    comun.salida_utf8()
    inicio = time.time()
    datos_corte = referencia.corte()
    ref = referencia.Referencia()

    print("=" * 78)
    print("MEDICION DE D.4: LOS UMBRALES CONTRA LA DISTRIBUCION")
    print("=" * 78)
    print("grafo de referencia : %s" % datos_corte["commit"])
    print("tag                 : %s" % datos_corte["tag"])
    print("vivos               : %d" % len(ref.vivos))
    print("semilla de muestreo : %d" % SEMILLA)
    print("instrumento         : calibracion/medir_d4.py")
    print("")

    gemelos = ref.pares_gemelos()[:MUESTRA_GEMELOS]
    jerarquia = ref.pares_jerarquia()
    ajenos = ref.pares_ajenos(MUESTRA_AJENOS, SEMILLA)
    import random
    azar = random.Random(SEMILLA)
    if len(jerarquia) > MUESTRA_JERARQUIA:
        jerarquia = azar.sample(jerarquia, MUESTRA_JERARQUIA)

    print("LAS TRES CLASES MEDIDAS, con su tamaño")
    print("  GEMELOS   (adjudicados REPITE por una persona) : %d pares" % len(gemelos))
    print("  JERARQUIA (arista declarada entre dos vivos)   : %d pares de 7282" % len(jerarquia))
    print("  AJENOS    (sin arista ni absorcion, azar)      : %d pares" % len(ajenos))
    print("")

    datos = {}
    for nombre_clase, pares in (("GEMELO", gemelos), ("JERARQUIA", jerarquia),
                                ("AJENO", ajenos)):
        print("midiendo %s ..." % nombre_clase)
        datos[nombre_clase] = medir_clase(nombre_clase, pares, ref.nodos)

    print("")
    print("-" * 78)
    print("1. LA DISTRIBUCION DE LAS TRES SEÑALES, POR CLASE")
    print("-" * 78)
    for nombre in NOMBRES:
        print("")
        print("SEÑAL %s" % nombre.upper())
        for clase in ("GEMELO", "JERARQUIA", "AJENO"):
            print("  %-10s %s" % (clase, resumen(datos[clase][nombre]["valores"],
                                                 datos[clase][nombre]["no_aplica"])))

    print("")
    print("-" * 78)
    print("2. LA BANDA POR TRAMO (9.19): que clase vive en cada tramo")
    print("-" * 78)
    for nombre in NOMBRES:
        print("")
        print("SEÑAL %s" % nombre.upper())
        for linea in tasa_por_tramo(datos["GEMELO"], datos["JERARQUIA"],
                                    datos["AJENO"], nombre):
            print(linea)

    print("")
    print("-" * 78)
    print("3. QUE CAZA Y QUE DEJA PASAR CADA UMBRAL CANDIDATO")
    print("-" * 78)
    print("La vara: un umbral tiene que levantar a los GEMELOS (son los que la")
    print("aduana existe para cazar) y a la JERARQUIA (que pide arista, no fusion),")
    print("y NO levantar a los AJENOS (que son la cola que nadie deberia leer).")
    candidatos_umbral = [0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80]
    for nombre in NOMBRES:
        print("")
        print("SEÑAL %s" % nombre.upper())
        print("  umbral |  GEMELO caza  | JERARQ caza  |  AJENO levanta (falsa cola)")
        for umbral in candidatos_umbral:
            g, gn, gt = cobertura(datos["GEMELO"], nombre, umbral)
            j, jn, jt = cobertura(datos["JERARQUIA"], nombre, umbral)
            a, an, at = cobertura(datos["AJENO"], nombre, umbral)
            print("   %.2f   |  %5.1f (%4d) |  %5.1f (%4d) |  %5.1f (%4d)"
                  % (umbral, g, gn, j, jn, a, an))

    print("")
    print("-" * 78)
    print("4. LA AVERIA (b): EL UMBRAL CONTRA LA MEDIANA")
    print("-" * 78)
    print("Regla madre: el p50 de la señal nueva quedo por encima del umbral y")
    print("disparar dejo de ser noticia. Se comprueba contra los AJENOS, que son")
    print("la poblacion que NO deberia disparar.")
    from src import config as modulo_config
    vigentes = modulo_config.cargar()
    for nombre in NOMBRES:
        clave = "umbral_" + nombre
        umbral = vigentes[clave]
        valores = datos["AJENO"][nombre]["valores"]
        p50 = percentil(valores, 50)
        print("  %-18s umbral vigente %.2f  contra p50 de los AJENOS %.3f  -> %s"
              % (nombre, umbral, p50,
                 "SANO (el umbral esta por encima de la mediana ajena)"
                 if umbral > p50 else
                 "ROTO (el umbral esta por debajo de la mediana ajena)"))

    print("")
    print("-" * 78)
    print("5. LA VARA OPERATIVA: CUANTOS VECINOS LEVANTA UN CANDIDATO")
    print("-" * 78)
    print("Un umbral que levanta trescientos vecinos no ordena una cola: la entierra.")
    print("")
    print("5.1 POR ESTIMACION, de la tasa de disparo de los AJENOS por %d vivos"
          % len(ref.vivos))
    print("    (la cola FALSA que cada umbral abriria por candidato)")
    print("  umbral |  similitud_texto |    familia_id    | paso_contra_nodo")
    for umbral in candidatos_umbral:
        celdas = []
        for nombre in NOMBRES:
            tasa, _, _ = cobertura(datos["AJENO"], nombre, umbral)
            celdas.append("%16.1f" % (tasa / 100.0 * len(ref.vivos)))
        print("   %.2f   |%s |%s |%s" % (umbral, celdas[0], celdas[1], celdas[2]))
    print("  (la cola de un candidato es la UNION de las tres, y una vecindad")
    print("   levantada por dos señales se cuenta una vez: la union es menor que")
    print("   la suma)")

    print("")
    print("5.2 POR CONTEO DIRECTO, el control: %d candidatos contra los %d vivos"
          % (MUESTRA_COLA, len(ref.vivos)))
    muestra = ref.muestra_de_vivos(MUESTRA_COLA, SEMILLA)
    colas = medir_cola(ref, muestra, vigentes)
    largos = sorted(n for _, n in colas)
    print("  con los umbrales VIGENTES (%.2f / %.2f / %.2f)"
          % (vigentes["umbral_similitud_texto"], vigentes["umbral_familia_id"],
             vigentes["umbral_paso_contra_nodo"]))
    print("  candidatos medidos : %d" % len(colas))
    print("  cola por candidato : min %d  p50 %d  p90 %d  max %d"
          % (min(largos), percentil(largos, 50), percentil(largos, 90), max(largos)))
    print("  uno a uno          : %s"
          % ", ".join("%d" % n for _, n in sorted(colas, key=lambda x: -x[1])))
    print("  con cola VACIA (entrarian sin leer nada): %d"
          % sum(1 for _, n in colas if n == 0))
    print("")
    print("corrida en %.1f segundos" % (time.time() - inicio))
    return 0


if __name__ == "__main__":
    sys.exit(main())
