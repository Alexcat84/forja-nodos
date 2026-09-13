# -*- coding: utf-8 -*-
"""LA TABLA QUE DICE SER DE INSTRUMENTO ES LA DEL INSTRUMENTO (D.41).

    python scripts/tallar_reporte.py              comprueba y no toca nada
    python scripts/tallar_reporte.py --estricto   ademas exige que TODA tabla
                                                  declarada se pueda comprobar
    python scripts/tallar_reporte.py --regenerar  corre los instrumentos que no
                                                  tengan su salida guardada
    python scripts/tallar_reporte.py --arreglar   REESCRIBE en el reporte las
                                                  tablas que difieren, desde su
                                                  instrumento

POR QUE EXISTE. Cuatro caidas de la racha `REPORTE` en cuatro vueltas son la misma
cosa: **una tabla que el reporte presenta como salida de un instrumento y que se
tecleo.** En la vuelta 22, el mismo reporte llevaba una tabla **pegada** (la de
`cap_10`, al digito) y una **tecleada** (la de `cap_11`, con 14 de 18 filas
falsas), y el fichero del instrumento ya tenia la buena impresa bajo el titulo
`LA TABLA, IMPRESA Y NO TECLEADA`. **La diferencia no fue el cuidado: fue el
metodo.** Y lo que fallaba no era invisible: quien sumara la columna publicada
obtenia `7345` y concluia que la frontera NO cierra, que es lo contrario de lo
que pasa.

> **UNA REGLA QUE SE CUMPLE TECLEANDO CON CUIDADO NO ES UNA REGLA: ES UNA
> INTENCION.** Esta la comprueba codigo, celda a celda.

COMO SABE QUE UNA TABLA DICE SER DE INSTRUMENTO. Mira las lineas de encima de
cada tabla (una ventana corta) y busca la declaracion que esta casa ya escribe:

    *Salida de `python .t1_v22/frontera_cap11.py`, guardada en `.t1_v22/salida_frontera_cap11.txt`.*

o, si se prefiere explicito y sin prosa:

    <!-- TALLADO: script=.t1_v22/frontera_cap11.py salida=.t1_v22/salida_frontera_cap11.txt -->

**NO SE INVENTO UN FORMATO NUEVO A PROPOSITO:** la unica forma de que una regla
muerda hoy es que lea lo que el reporte ya dice. El marcador explicito existe
para quien lo quiera, y gana sobre la prosa cuando los dos estan.

DE DONDE REGENERA, Y POR QUE NO CORRE NADA POR SU CUENTA. **Compara contra el
FICHERO DE SALIDA guardado**, no re ejecutando. Es deliberado y hay dos motivos,
los dos medidos en este repo: los instrumentos de una vuelta **escriben**
(`.t1_v22/lote_a.py` crea candidatos en `cuarentena/`) y **llaman a la aduana**,
que cuesta minutos por candidato. **Un hook que re ejecuta lo que encuentra
escrito en un documento no es una guarda: es una bomba.** Correr el instrumento
es una orden aparte y explicita (`--regenerar`), y el hook nunca la da.
"""

import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")

VENTANA = 12                 # lineas por encima de la tabla donde se busca
TOPE_DE_SEGUNDOS = 900       # un instrumento que no acaba en 15 min se declara
MARCADOR = re.compile(r"<!--\s*TALLADO:(.*?)-->", re.S)
CAMPO = re.compile(r"(script|salida)\s*=\s*([^\s]+)")
EN_COMILLAS = re.compile(r"`([^`]+)`")
EXT_SALIDA = (".txt", ".out")

# LA DECLARACION TIENE QUE AFIRMAR, NO SOLO CITAR. Un parrafo que menciona un
# fichero al lado de una tabla no esta diciendo que la tabla salga de ahi, y
# tratarlo como si lo dijera llena la guarda de falsos positivos: la primera
# corrida marco ocho tablas por nombrar `docs/loop/loop.log` cerca. Una guarda
# que grita donde no hay nada enseña a no mirarla.
AFIRMA = re.compile(r"salida de|guardad[ao] en|impres[ao]|pegad[ao]|tallad[ao]|"
                    r"generad[ao] por|producid[ao] por", re.I)

# Y LOS ARTEFACTOS DE MAQUINA NO SON INSTRUMENTOS (D.33): `loop.log` es el
# testigo del arnes, no genera ninguna tabla.
NO_SON_INSTRUMENTO = ("loop.log",)


# ---------------------------------------------------------------------------
# LEER TABLAS
# ---------------------------------------------------------------------------

def _normalizar(celda):
    """Colapsa espacios dentro de la celda y quita los de los bordes.

    UN RE FLUJO NO ES UNA CIFRA FALSA. Que el instrumento imprima `P1  la cabeza`
    con dos espacios y el reporte `P1 la cabeza` con uno no cambia ningun dato, y
    hacer caer una vuelta por eso enseñaria a desconfiar de la guarda. Lo que se
    compara es el CONTENIDO de la celda.
    """
    return re.sub(r"\s+", " ", (celda or "").strip())


def _filas(linea):
    """Las celdas de una fila markdown, sin las barras de los extremos."""
    recorte = linea.strip()
    if recorte.startswith("|"):
        recorte = recorte[1:]
    if recorte.endswith("|"):
        recorte = recorte[:-1]
    return [_normalizar(c) for c in recorte.split("|")]


def _es_separador(celdas):
    return bool(celdas) and all(re.match(r"^:?-{2,}:?$", c) for c in celdas if c)


def tablas_de(texto):
    """Todas las tablas markdown de un texto: (primera, ultima, cabecera, filas)."""
    lineas = texto.split("\n")
    encontradas = []
    indice = 0
    while indice < len(lineas):
        if lineas[indice].lstrip().startswith("|"):
            inicio = indice
            bloque = []
            while indice < len(lineas) and lineas[indice].lstrip().startswith("|"):
                bloque.append(lineas[indice])
                indice += 1
            celdas = [_filas(l) for l in bloque]
            cuerpo = [c for c in celdas if not _es_separador(c)]
            if len(cuerpo) >= 2:
                encontradas.append({"inicio": inicio, "fin": indice,
                                    "cabecera": cuerpo[0], "filas": cuerpo[1:],
                                    "crudo": bloque})
        else:
            indice += 1
    return encontradas


# ---------------------------------------------------------------------------
# QUIEN DICE SER DE INSTRUMENTO
# ---------------------------------------------------------------------------

def _declaracion(lineas, inicio, hasta=None):
    """Devuelve {'script':..., 'salida':...} leido del texto que precede."""
    ventana = "\n".join(lineas[max(0, inicio - (hasta or VENTANA)):inicio])
    marca = MARCADOR.search(ventana)
    if marca:
        campos = dict(CAMPO.findall(marca.group(1)))
        # O REPRODUCE SU INSTRUMENTO, O LO CITA, Y TIENE QUE DECIR CUAL.
        # Una tabla de resumen puede traer DOS filas que salen de un instrumento
        # y otras diez que no, y tratarla entera como la tabla del instrumento
        # marca en rojo las diez que nunca prometieron serlo. La primera version
        # de esta guarda se lo hizo a si misma con su propia correccion.
        parcial = "parcial" in marca.group(1)
        if campos or parcial:
            return {"script": campos.get("script"), "salida": campos.get("salida"),
                    "parcial": parcial, "como": "marcador"}
    # LA AFIRMACION Y LA RUTA VAN EN LA MISMA LINEA, y se busca de abajo arriba.
    # Sin esto, la guarda cogia el primer `.py` de la ventana aunque estuviera
    # tres parrafos mas arriba y hablara de otra cosa: marco `src/comun.py`, que
    # el reporte citaba como referencia de doctrina, como si generase una tabla.
    # UNA DECLARACION ES UNA FRASE QUE AFIRMA, NO DOS PALABRAS QUE COINCIDEN CERCA.
    for linea in reversed(ventana.split("\n")):
        if not AFIRMA.search(linea):
            continue
        script = salida = None
        for cita in EN_COMILLAS.findall(linea):
            limpia = cita.replace("python ", "").strip()
            if os.path.basename(limpia) in NO_SON_INSTRUMENTO:
                continue
            if limpia.endswith(".py") and script is None:
                script = limpia
            elif limpia.lower().endswith(EXT_SALIDA) and salida is None:
                salida = limpia
        if script or salida:
            return {"script": script, "salida": salida, "como": "prosa"}
    return None


def declaradas(texto=None, ruta_reporte=None):
    """Las tablas del reporte que dicen ser salida de un instrumento."""
    ruta_reporte = ruta_reporte or RUTA_REPORTE
    texto = texto if texto is not None else io.open(
        ruta_reporte, encoding="utf-8").read()
    lineas = texto.split("\n")
    salida = []
    anterior = 0
    for tabla in tablas_de(texto):
        # LA DECLARACION VALE desde donde acabo la tabla anterior, o desde el
        # ultimo encabezado, hasta esta tabla. Asi el bloque de comprobacion que
        # la casa pega EN MEDIO no rompe el vinculo: entre la frase que declara
        # el instrumento y la tabla hay a veces veinte lineas, y una ventana fija
        # dejo fuera justo la de `cap_11`, que es el caso que obligo a esto.
        desde = anterior
        for numero in range(tabla["inicio"] - 1, anterior - 1, -1):
            if lineas[numero].startswith("#"):
                desde = numero
                break
        firma = _declaracion(lineas, tabla["inicio"], tabla["inicio"] - desde)
        anterior = tabla["fin"]
        if firma:
            tabla = dict(tabla)
            tabla.update(firma)
            salida.append(tabla)
    return salida


# ---------------------------------------------------------------------------
# EL INSTRUMENTO
# ---------------------------------------------------------------------------

def correr_instrumento(script, destino, raiz=None):
    """Corre el instrumento y guarda su salida. SOLO bajo --regenerar."""
    raiz = raiz or RAIZ
    proceso = subprocess.Popen([sys.executable, script], cwd=raiz,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    try:
        crudo = proceso.communicate(timeout=TOPE_DE_SEGUNDOS)[0]
    except Exception:
        proceso.kill()
        return None, "el instrumento no acabo en %d segundos" % TOPE_DE_SEGUNDOS
    if proceso.returncode != 0:
        return None, "el instrumento salio con codigo %d" % proceso.returncode
    texto = crudo.decode("utf-8", "replace")
    if destino:
        completa = os.path.join(raiz, destino)
        carpeta = os.path.dirname(completa)
        if carpeta and not os.path.isdir(carpeta):
            os.makedirs(carpeta)
        with io.open(completa, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
    return texto, None


def _texto_del_instrumento(tabla, regenerar, raiz=None):
    """El texto contra el que se compara, o (None, motivo)."""
    raiz = raiz or RAIZ
    salida = tabla.get("salida")
    script = tabla.get("script")
    if salida:
        completa = os.path.join(raiz, salida)
        if os.path.exists(completa):
            return io.open(completa, encoding="utf-8").read(), None
    if regenerar and script and os.path.exists(os.path.join(raiz, script)):
        return correr_instrumento(script, salida, raiz)
    if salida and script:
        return None, ("declara la salida '%s', que NO esta en el arbol. Corre "
                      "`python scripts/tallar_reporte.py --regenerar` para "
                      "tallarla desde '%s'" % (salida, script))
    if salida:
        return None, "declara la salida '%s', que NO esta en el arbol" % salida
    if script:
        if not os.path.exists(os.path.join(raiz, script)):
            return None, "declara el instrumento '%s', que ya no esta" % script
        return None, ("declara '%s' y no guarda su salida: sin fichero no hay "
                      "nada contra que comparar" % script)
    return None, "no nombra ni salida ni instrumento"


# ---------------------------------------------------------------------------
# LA COMPARACION, CELDA A CELDA
# ---------------------------------------------------------------------------

def _pareja(tabla, candidatas):
    """La tabla del instrumento que corresponde a la del reporte."""
    for otra in candidatas:
        if otra["cabecera"] == tabla["cabecera"]:
            return otra, None
    if len(candidatas) == 1:
        return candidatas[0], ("la cabecera no coincide, pero el instrumento "
                               "imprime una sola tabla y se usa esa")
    return None, ("el instrumento imprime %d tablas y ninguna lleva la cabecera "
                  "de esta" % len(candidatas))


def comparar(tabla, texto_instrumento):
    """Devuelve (diferencias, aviso). Lista vacia es verde."""
    candidatas = tablas_de(texto_instrumento)
    if not candidatas:
        # NO ES UNA CIFRA FALSA Y NO SE DECLARA COMO TAL. Una tabla que RESUME la
        # salida de un instrumento (el saldo de diecisiete informes, por ejemplo)
        # no es la tabla del instrumento, y D.41 habla de las que dicen SER la
        # suya. Gritar aqui seria enseñar a no mirar la guarda.
        return None, ("el instrumento no imprime ninguna tabla: esta la resume, "
                      "no la reproduce")
    buena, aviso = _pareja(tabla, candidatas)
    if buena is None:
        return [{"fila": "(toda la tabla)", "columna": "", "reporte": "",
                 "instrumento": "", "nota": aviso}], None

    diferencias = []
    suyas = {}
    for fila in buena["filas"]:
        suyas.setdefault(fila[0], fila)
    vistas = set()
    for fila in tabla["filas"]:
        clave = fila[0]
        vistas.add(clave)
        gemela = suyas.get(clave)
        if gemela is None:
            diferencias.append({"fila": clave or "(fila sin rotulo)", "columna": "",
                                "reporte": " | ".join(fila), "instrumento": "",
                                "nota": "esta fila NO esta en la salida del instrumento"})
            continue
        for indice in range(max(len(fila), len(gemela))):
            mia = fila[indice] if indice < len(fila) else ""
            suya = gemela[indice] if indice < len(gemela) else ""
            if mia != suya:
                columna = (tabla["cabecera"][indice]
                           if indice < len(tabla["cabecera"]) else "columna %d" % indice)
                diferencias.append({"fila": clave, "columna": columna,
                                    "reporte": mia, "instrumento": suya, "nota": ""})
    for clave, fila in suyas.items():
        if clave not in vistas:
            diferencias.append({"fila": clave, "columna": "", "reporte": "",
                                "instrumento": " | ".join(fila),
                                "nota": "el instrumento la imprime y el reporte NO la lleva"})
    return diferencias, aviso


def revisar(ruta_reporte=None, regenerar=False, raiz=None):
    """Devuelve la lista de dictamenes, uno por tabla declarada."""
    raiz = raiz or RAIZ
    ruta_reporte = ruta_reporte or RUTA_REPORTE
    texto = io.open(ruta_reporte, encoding="utf-8").read()
    dictamenes = []
    for tabla in declaradas(texto, ruta_reporte):
        if tabla.get("parcial"):
            dictamenes.append({"tabla": tabla, "estado": "CITA", "motivo":
                               "declarada PARCIAL: cita a su instrumento en alguna "
                               "fila, no reproduce su tabla", "diferencias": [],
                               "aviso": None})
            continue
        instrumento, motivo = _texto_del_instrumento(tabla, regenerar, raiz)
        if instrumento is None:
            dictamenes.append({"tabla": tabla, "estado": "SIN COMPROBAR",
                               "motivo": motivo, "diferencias": [], "aviso": None})
            continue
        diferencias, aviso = comparar(tabla, instrumento)
        if diferencias is None:
            dictamenes.append({"tabla": tabla, "estado": "SIN COMPROBAR",
                               "motivo": aviso, "diferencias": [], "aviso": None})
            continue
        dictamenes.append({"tabla": tabla,
                           "estado": "DIFIERE" if diferencias else "TALLADA",
                           "motivo": "", "diferencias": diferencias,
                           "aviso": aviso, "texto_instrumento": instrumento})
    return dictamenes


# ---------------------------------------------------------------------------
# ARREGLAR POR REGENERACION, NUNCA A MANO
# ---------------------------------------------------------------------------

def arreglar(ruta_reporte=None, regenerar=True, raiz=None):
    """Reescribe en el reporte las tablas que difieren, desde su instrumento."""
    ruta_reporte = ruta_reporte or RUTA_REPORTE
    dictamenes = revisar(ruta_reporte, regenerar=regenerar, raiz=raiz)
    lineas = io.open(ruta_reporte, encoding="utf-8").read().split("\n")
    arregladas = []
    # De abajo arriba, para que los indices de las de arriba sigan valiendo.
    for dictamen in sorted(dictamenes, key=lambda d: -d["tabla"]["inicio"]):
        if dictamen["estado"] != "DIFIERE":
            continue
        tabla = dictamen["tabla"]
        candidatas = tablas_de(dictamen["texto_instrumento"])
        buena, _aviso = _pareja(tabla, candidatas)
        if buena is None:
            continue
        lineas[tabla["inicio"]:tabla["fin"]] = buena["crudo"]
        arregladas.append((tabla["inicio"] + 1, len(dictamen["diferencias"])))
    if arregladas:
        with io.open(ruta_reporte, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lineas))
    return arregladas


# ---------------------------------------------------------------------------

def texto_informe(dictamenes, estricto=False):
    lineas = []
    difieren = [d for d in dictamenes if d["estado"] == "DIFIERE"]
    sin = [d for d in dictamenes if d["estado"] == "SIN COMPROBAR"]
    talladas = [d for d in dictamenes if d["estado"] == "TALLADA"]
    citas = [d for d in dictamenes if d["estado"] == "CITA"]

    lineas.append("=" * 76)
    lineas.append("TALLADO DEL REPORTE (D.41): la tabla que dice ser de instrumento")
    lineas.append("=" * 76)
    lineas.append("tablas que declaran instrumento : %d" % len(dictamenes))
    lineas.append("  talladas, celda a celda       : %d" % len(talladas))
    lineas.append("  que DIFIEREN de su instrumento: %d" % len(difieren))
    lineas.append("  sin poder comprobar           : %d" % len(sin))
    lineas.append("  que CITAN y no reproducen     : %d   (declaradas PARCIAL)"
                  % len(citas))
    for dictamen in citas:
        lineas.append("      linea %d de docs/loop/REPORTE.md"
                      % (dictamen["tabla"]["inicio"] + 1))

    for dictamen in difieren:
        tabla = dictamen["tabla"]
        filas = []
        for diferencia in dictamen["diferencias"]:
            if diferencia["fila"] not in filas:
                filas.append(diferencia["fila"])
        lineas.append("")
        lineas.append("DIFIERE  docs/loop/REPORTE.md linea %d" % (tabla["inicio"] + 1))
        lineas.append("  declara: %s" % (tabla.get("salida") or tabla.get("script")))
        lineas.append("  %d fila(s) distintas de su instrumento:" % len(filas))
        for diferencia in dictamen["diferencias"]:
            if diferencia["nota"]:
                lineas.append("    %-22s %s" % (diferencia["fila"], diferencia["nota"]))
            else:
                lineas.append("    %-22s %-14s reporte '%s'  instrumento '%s'"
                              % (diferencia["fila"], diferencia["columna"],
                                 diferencia["reporte"], diferencia["instrumento"]))

    for dictamen in sin:
        tabla = dictamen["tabla"]
        lineas.append("")
        lineas.append("SIN COMPROBAR  docs/loop/REPORTE.md linea %d"
                      % (tabla["inicio"] + 1))
        lineas.append("  %s" % dictamen["motivo"])

    lineas.append("")
    if difieren:
        lineas.append("TALLADO EN ROJO: %d tabla(s) dicen venir de un instrumento y no "
                      "coinciden con el." % len(difieren))
        lineas.append("Se arreglan REGENERANDO, no tecleando:")
        lineas.append("  python scripts/tallar_reporte.py --arreglar")
    elif estricto and sin:
        lineas.append("TALLADO EN ROJO (estricto): %d tabla(s) declaran instrumento y "
                      "no se pueden comprobar." % len(sin))
        lineas.append("Una tabla que dice venir de un instrumento y no puede enseñarlo "
                      "no esta declarando su origen: lo esta prometiendo.")
    else:
        lineas.append("TALLADO VERDE: las %d tabla(s) comprobables son las de su "
                      "instrumento, celda a celda." % len(talladas))
        if sin:
            lineas.append("Quedan %d sin comprobar, y no tumban el commit: el reporte "
                          "es acumulativo y un andamio borrado hace tres vueltas no es "
                          "una mentira sobre hoy. En el cierre de vuelta si tumban "
                          "(--estricto)." % len(sin))
    return "\n".join(lineas)


def main(argumentos=None):
    argumentos = list(argumentos if argumentos is not None else sys.argv[1:])
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8")
        except Exception:
            pass
    estricto = "--estricto" in argumentos
    regenerar = "--regenerar" in argumentos
    if "--arreglar" in argumentos:
        arregladas = arreglar(regenerar=True)
        if not arregladas:
            print("No habia ninguna tabla que difiriera de su instrumento.")
        for linea, cuantas in arregladas:
            print("TALLADA de nuevo: docs/loop/REPORTE.md linea %d, %d celda(s) "
                  "que estaban tecleadas" % (linea, cuantas))
        print("")
        print("CORRECCION DECLARADA: escribe al lado de la tabla de que caida sale "
              "y con que orden se regenero. Una correccion silenciosa vuelve a ser "
              "una tabla sin origen.")
        return 0
    dictamenes = revisar(regenerar=regenerar)
    print(texto_informe(dictamenes, estricto))
    if any(d["estado"] == "DIFIERE" for d in dictamenes):
        return 1
    if estricto and any(d["estado"] == "SIN COMPROBAR" for d in dictamenes):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
