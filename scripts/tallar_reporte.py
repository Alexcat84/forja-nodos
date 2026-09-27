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
# Y LA APERTURA CIEGA, desde el 16 sep 2026 (decision del fundador, punto 3): era
# la unica sede de cifra que ninguna guarda leia, con dos ejemplares ya encontrados
# a mano. Una tabla suya que diga venir de un instrumento se talla igual que las
# del reporte.
RUTA_APERTURA = os.path.join(RAIZ, "docs", "loop", "APERTURA_CIEGA.md")
DOCUMENTOS = (RUTA_REPORTE, RUTA_APERTURA)

VENTANA = 12                 # lineas por encima de la tabla donde se busca
TOPE_DE_SEGUNDOS = 900       # un instrumento que no acaba en 15 min se declara
MARCADOR = re.compile(r"<!--\s*TALLADO:(.*?)-->", re.S)

# ---------------------------------------------------------------------------
# LA CIFRA DERIVADA LA CALCULA EL INSTRUMENTO (D.59, 20 sep 2026).
#
# LA CAIDA QUE LA OBLIGA, y es la tercera seguida de la misma familia: el reporte de
# la vuelta 53 publico **media por pasada CON reloj: 517,7 s** con `11` pasadas en el
# numerador y `9` en el denominador. Los `4659,0` s incluian una pasada de `600` s que
# la celda de al lado marcaba **sin fichero de reloj**. La cifra era cierta de algo;
# **la frase decia otra cosa**, y de ahi salia un `-29,2` por ciento donde la caida real
# por pasada es `-42,1`.
#
# LAS TRES CAIDAS DE LA RACHA SON LA MISMA FIGURA: *una frase sobre una cifra cierta que
# el propio instrumento desmiente dos lineas abajo.*
#
# SE MIDE SOLO EN LA VUELTA VIVA, Y ESO NO ES UNA CONCESION: es lo que separa una guarda
# de un grito. Sobre el reporte entero caerian `591` lineas de `53` vueltas de historia;
# sobre la vuelta viva cayeron `2`, **y las dos eran de verdad**. Una guarda con
# quinientos noventa y un avisos se aprende a no mirar, y esta casa ya pago ese precio
# dos veces.
#
# Y LA PALABRA TIENE QUE IR JUNTO AL NUMERO, no solo en la misma linea: sin eso, un
# encabezado que dice *UNA FILA POR CAPITULO Y NO UNA MEDIA* caia por la palabra `media`
# y por el digito de su numero de seccion.
# LA CABECERA DE UN FRENTE TAMBIEN ABRE UNA VUELTA (d134, 21 sep 2026).
#
# La serial escribe `# VUELTA 62, ...` y un frente escribe
# `# FRENTE `gerber_emyth`, VUELTA 9`. El regex solo conocia la primera, asi
# que en un frente la "vuelta viva" de D.59 **no empezaba en su ultima vuelta**:
# empezaba en la ultima cabecera de la SERIAL que el arbol heredo, y se tragaba
# las vueltas del frente enteras. Medido el 21 sep en gerber_emyth: 4783 lineas
# de ventana en vez de 683, o sea las vueltas 2 a 9 juntas.
#
# Y ESO ROMPE LA RAZON DE SER DE LA VENTANA. D.59 mira solo la vuelta viva
# porque una guarda con quinientos avisos se aprende a no mirar; una ventana de
# ocho vueltas es el primer paso de vuelta a ese sitio.
CABEZA_DE_VUELTA = re.compile(
    r"^#{1,2}[ \t]+(?:FRENTE[ \t]+[^,\r\n]+,[ \t]*)?VUELTA[ \t]+\d+", re.M)
CIFRA_DERIVADA = re.compile(
    r"(?:(media|promedio|variacion|variaci\u00f3n|tasa)\D{0,40}`?\d"
    r"|\d[^`]{0,40}?(por\s+ciento|porcentaje))", re.I)
# Una linea se salva si NOMBRA su instrumento: un fichero de salida o una carpeta .vNN/
NOMBRA_INSTRUMENTO = re.compile(
    r"`[^`]*\.(txt|py|log|json|jsonl|md)`|\.v\d+\w*/")


def cifras_derivadas_sueltas(texto=None, ruta_reporte=None):
    """Las frases de la VUELTA VIVA que publican una cifra derivada sin instrumento.

    Devuelve `[{"linea", "frase"}]`. **Vacia es verde.**

    LO QUE NO MIRA, Y CADA EXCLUSION TIENE SU MOTIVO:

      - **lo que va dentro de un bloque de tallado**: ya lo imprime un instrumento y el
        tallado lo compara celda a celda;
      - **lo sangrado**: es salida pegada de un instrumento, no una frase del reporte;
      - **lo que nombra su instrumento en la misma linea**: eso es justo lo que la regla
        pide, y castigarlo seria castigar el cumplimiento;
      - **todo lo anterior a la vuelta viva**: es historia, y una regla nueva no se
        aplica hacia atras sobre `53` vueltas ya auditadas.
    """
    if texto is None:
        texto = io.open(ruta_reporte or RUTA_REPORTE,
                        encoding="utf-8").read()
    lineas = texto.split(chr(10))
    marcas = [n for n, l in enumerate(lineas) if CABEZA_DE_VUELTA.match(l)]
    inicio = marcas[-1] if marcas else 0

    # LA UNIDAD ES EL PARRAFO, NO LA LINEA, y esto lo corrigio un falso positivo mio el
    # mismo dia en que nacio la guarda: la CORRECCION DECLARADA que repara la caida de
    # la vuelta 53 cita su instrumento con su marca de tallado, pero dos lineas por
    # debajo de la cifra. Por linea, la guarda tumbaba el arreglo que ella misma pedia.
    #
    # **Una frase se publica dentro de un parrafo**, y si el parrafo nombra su
    # instrumento, la cifra esta sostenida.
    sueltas, dentro = [], False
    parrafo, primera = [], inicio + 1

    def cerrar():
        if not parrafo:
            return
        if NOMBRA_INSTRUMENTO.search(" ".join(parrafo)):
            return
        for salto, linea in enumerate(parrafo):
            if CIFRA_DERIVADA.search(linea):
                sueltas.append({"linea": primera + salto,
                                "frase": " ".join(linea.split())[:110]})
                return

    for numero in range(inicio, len(lineas)):
        linea = lineas[numero]
        if "<!-- TALLADO:" in linea:
            cerrar()
            del parrafo[:]
            dentro = True
            continue
        if dentro and linea.strip() and not linea.startswith("    ") \
                and not linea.startswith("|"):
            dentro = False
        if dentro or linea.startswith("    "):
            continue
        if not linea.strip():
            cerrar()
            del parrafo[:]
            continue
        if not parrafo:
            primera = numero + 1
        parrafo.append(linea)
    cerrar()
    return sueltas

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


def comun_relativa(ruta):
    try:
        return os.path.relpath(ruta, RAIZ).replace(chr(92), "/")
    except ValueError:
        return ruta


def revisar_todos(regenerar=False, raiz=None):
    """Los dictamenes de las DOS sedes de cifra que publican tablas."""
    todos = []
    for documento in DOCUMENTOS:
        todos.extend(revisar(documento, regenerar=regenerar, raiz=raiz))
    return todos


def revisar(ruta_reporte=None, regenerar=False, raiz=None):
    """Devuelve la lista de dictamenes, uno por tabla declarada."""
    raiz = raiz or RAIZ
    ruta_reporte = ruta_reporte or RUTA_REPORTE
    # EL REPORTE PUEDE NO ESTAR, Y NO ES UN ERROR: `D.34.2` LO RETIRA DEL ARBOL
    # DURANTE LA FASE CIEGA, a proposito, para que el auditor clasifique sin verlo.
    #
    # Y ESTO NO ERA COSMETICO: el arnes COMMITEA la pagina sellada con los cuatro
    # ficheros retirados, asi que el hook corria este tallador sin reporte, este
    # reventaba con FileNotFoundError, y **el commit del propio sello se abortaba**.
    # No habia mordido todavia solo porque en la vuelta 29 el barrido de guiones
    # cayo tres segundos antes. **Una guarda que impide sellar la fase ciega no
    # protege el dato: bloquea el bucle.**
    if not os.path.exists(ruta_reporte):
        return []
    texto = io.open(ruta_reporte, encoding="utf-8").read()
    dictamenes = []
    for tabla in declaradas(texto, ruta_reporte):
        tabla["documento"] = comun_relativa(ruta_reporte)
        if tabla.get("parcial"):
            dictamenes.append({"tabla": tabla, "estado": "CITA", "motivo":
                               "declarada PARCIAL: cita a su instrumento en alguna "
                               "fila, no reproduce su tabla", "diferencias": [],
                               "aviso": None})
            continue
        instrumento, motivo = _texto_del_instrumento(tabla, regenerar, raiz)
        # UNA RUTA QUE PROMETE PRUEBA Y NO LA TIENE ES CAIDA DE CIFRA (cosecha
        # 7.B, AUDITOR_FORJA.md 5.5, literal: si apunta a un fichero inexistente o
        # de CERO BYTES, es caida de cifra).
        #
        # ESTE HUECO LO ABRI YO Y LO PAGO LA VUELTA 25. Un fichero vacio existe,
        # asi que se leia sin error, no traia ninguna tabla, y la guarda lo
        # despachaba con la lectura mas generosa posible: "esta tabla resume su
        # salida, no la reproduce". VERDE. La cifra que sostenia era `2` donde el
        # instrumento da `4`, y la sede que la probaba tenia cero bytes.
        #
        # VACIA NO ES LO MISMO QUE AUSENTE, y por eso muerde distinto: un fichero
        # que esta y esta vacio es de una vuelta viva; uno que no esta puede ser un
        # andamio borrado hace tres vueltas, y eso no es una mentira sobre hoy
        # (queda SIN COMPROBAR, y el cierre en estricto si lo tumba).
        if instrumento is not None and not instrumento.strip():
            dictamenes.append({
                "tabla": tabla, "estado": "RUTA VACIA",
                "motivo": ("la salida declarada existe y esta VACIA (cero bytes). "
                           "Una ruta publicada como prueba que no prueba nada es "
                           "caida de cifra (cosecha 7.B)"),
                "diferencias": [], "aviso": None})
            continue
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
    vacias = [d for d in dictamenes if d["estado"] == "RUTA VACIA"]

    lineas.append("=" * 76)
    lineas.append("TALLADO DEL REPORTE (D.41): la tabla que dice ser de instrumento")
    lineas.append("=" * 76)
    lineas.append("tablas que declaran instrumento : %d" % len(dictamenes))
    lineas.append("  talladas, celda a celda       : %d" % len(talladas))
    lineas.append("  que DIFIEREN de su instrumento: %d" % len(difieren))
    lineas.append("  con la ruta VACIA             : %d   (cero bytes, 7.B)"
                  % len(vacias))
    lineas.append("  sin poder comprobar           : %d" % len(sin))
    lineas.append("  que CITAN y no reproducen     : %d   (declaradas PARCIAL)"
                  % len(citas))
    for dictamen in citas:
        lineas.append("      linea %d de %s"
                      % (dictamen["tabla"]["inicio"] + 1,
                         dictamen["tabla"].get("documento", "docs/loop/REPORTE.md")))

    for dictamen in difieren:
        tabla = dictamen["tabla"]
        filas = []
        for diferencia in dictamen["diferencias"]:
            if diferencia["fila"] not in filas:
                filas.append(diferencia["fila"])
        lineas.append("")
        lineas.append("DIFIERE  %s linea %d"
                      % (tabla.get("documento", "docs/loop/REPORTE.md"), tabla["inicio"] + 1))
        lineas.append("  declara: %s" % (tabla.get("salida") or tabla.get("script")))
        lineas.append("  %d fila(s) distintas de su instrumento:" % len(filas))
        for diferencia in dictamen["diferencias"]:
            if diferencia["nota"]:
                lineas.append("    %-22s %s" % (diferencia["fila"], diferencia["nota"]))
            else:
                lineas.append("    %-22s %-14s reporte '%s'  instrumento '%s'"
                              % (diferencia["fila"], diferencia["columna"],
                                 diferencia["reporte"], diferencia["instrumento"]))

    for dictamen in vacias:
        tabla = dictamen["tabla"]
        lineas.append("")
        lineas.append("RUTA VACIA  %s linea %d"
                      % (tabla.get("documento", "docs/loop/REPORTE.md"), tabla["inicio"] + 1))
        lineas.append("  declara: %s" % (tabla.get("salida") or tabla.get("script")))
        lineas.append("  %s" % dictamen["motivo"])

    for dictamen in sin:
        tabla = dictamen["tabla"]
        lineas.append("")
        lineas.append("SIN COMPROBAR  %s linea %d"
                      % (tabla.get("documento", "docs/loop/REPORTE.md"), tabla["inicio"] + 1))
        lineas.append("  %s" % dictamen["motivo"])

    lineas.append("")
    if vacias:
        lineas.append("TALLADO EN ROJO: %d ruta(s) publicadas como prueba apuntan a un "
                      "fichero VACIO." % len(vacias))
        lineas.append("Corre el instrumento y guarda su salida, o quita la ruta: una "
                      "ruta que promete prueba y no la trae es una cifra sin sede.")
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
    # SI NINGUNA SEDE ESTA EN EL ARBOL, NO HAY NADA QUE TALLAR Y NO ES UN FALLO:
    # la fase ciega retira el reporte a proposito (D.34.2). La comprobacion va AQUI
    # y no en `texto_informe`, porque ese recibe los dictamenes de quien sea (una
    # prueba en su taller, por ejemplo) y no tiene por que mirar el arbol de verdad.
    if not any(os.path.exists(d) for d in DOCUMENTOS):
        print("TALLADO SIN OBJETO: ninguna sede de tablas esta en el arbol.")
        print("La fase ciega retira docs/loop/REPORTE.md A PROPOSITO (D.34.2), asi que")
        print("no hay ninguna tabla que tallar y esto NO es un fallo.")
        return 0
    dictamenes = revisar_todos(regenerar=regenerar)
    print(texto_informe(dictamenes, estricto))

    # LA CIFRA DERIVADA LA CALCULA EL INSTRUMENTO (D.59, 20 sep 2026).
    sueltas = cifras_derivadas_sueltas()
    if sueltas:
        print("")
        print("=" * 76)
        print("CIFRAS DERIVADAS SIN INSTRUMENTO (D.59): %d en la vuelta viva"
              % len(sueltas))
        print("=" * 76)
        for suelta in sueltas:
            print("  linea %d de docs/loop/REPORTE.md" % suelta["linea"])
            print("     %s" % suelta["frase"])
        print("")
        print("UNA MEDIA, UN PORCENTAJE, UNA RAZON O UNA DIFERENCIA LAS IMPRIME UN")
        print("INSTRUMENTO, con su numerador y su denominador nombrados. Una cifra")
        print("derivada a mano de dos celdas no se publica: la vuelta 53 dividio 11")
        print("pasadas entre 9 y de ahi salio un 29,2 por ciento donde la caida real")
        print("es 42,1. Nombra el instrumento en el mismo parrafo, o regenera la cifra.")
        return 1

    if any(d["estado"] in ("DIFIERE", "RUTA VACIA") for d in dictamenes):
        return 1
    if estricto and any(d["estado"] == "SIN COMPROBAR" for d in dictamenes):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
