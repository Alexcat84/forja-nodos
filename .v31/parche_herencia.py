# -*- coding: utf-8 -*-
"""El parche de la TAREA 2 sobre src/herencia.py, aplicado por trozos exactos.

Se escribe como parche y no a mano para que quede el registro de QUE trozo
sustituye a QUE trozo: la TAREA 2 es bloqueante y su prueba es reproducible.
"""
import io

RUTA = "src/herencia.py"
s = io.open(RUTA, encoding="utf-8").read()

# ---------------------------------------------------------------- 1. docstring
viejo = """LO QUE HACE. Lee la ULTIMA acta de `docs/loop/ACTA_AUDITOR.md` (de su ultimo
encabezado `# ACTA` hasta el final) y saca de ahi:

  - cada bloque en cita cuyo titulo diga `TAREA BLOQUEANTE DEL AUDITOR`
  - cada seccion cuyo encabezado nombre un `REMEDIO`

y los numera."""
nuevo = """LO QUE HACE. Lee la ULTIMA acta de `docs/loop/ACTA_AUDITOR.md` (de su ultimo
encabezado `# ACTA` hasta el final) y saca de ahi:

  - cada bloque en cita cuyo titulo diga `TAREA BLOQUEANTE DEL AUDITOR`
  - **cada FILA de la tabla de remedios que esa acta ESCRIBE**

y los numera.

ENTREGA LOS REMEDIOS QUE EL ACTA ESCRIBE, NO LOS QUE CITA (16 sep 2026, TAREA 2 de
la vuelta 31, encargada por la `ACTA 29` `8.1` con su caida delante). **Hasta hoy
cogia cada seccion cuyo encabezado nombrara un REMEDIO, y eso es otra cosa.** Un
auditor escribe sus remedios UNA vez, en su tabla, y despues los MENCIONA muchas:
para decir que se cumplieron, para contarse una caida, hasta en el titulo del acta.
La regla vieja se quedaba con las menciones y perdia la tabla.

    LO QUE MEDIA LA REGLA VIEJA, corrido contra la ACTA 28:
      HEREDADO 1  -> ACTA 28 seccion 3.2   (CITA el remedio 2 de la ACTA 27)
      HEREDADO 2  -> ACTA 28 seccion 6.1   (CITA el heredado 1 para decir que aguanto)
    y su tabla de remedios, la de su seccion 10, NO SALIA.

    Y CONTRA LA ACTA 29 era peor: el HEREDADO 1 era **el titulo del acta**, que
    lleva la palabra remedio dentro de la frase `rompiendo el remedio que yo mismo
    escribi`.

**EL COSTE ESTA MEDIDO Y NO ES HIPOTETICO:** el auditor de la `ACTA 29` rompio en su
apertura sellada el `REMEDIO 1` que el mismo habia escrito, **porque el arnes no se lo
entrego** (`ACTA 29` `8.1`). Se lo cargo igualmente, citando `D.40`: *el fallo era de
arquitectura, y la arquitectura es del arnes.*

LA FORMA QUE SE RECONOCE, Y ES LA QUE ESTA CASA YA ESCRIBE: una tabla markdown cuya
CABECERA nombre `REMEDIO`, **fuera de cita**. Cada fila de datos es un remedio.

    | # | **REMEDIO** | como se comprueba que se cumplio |
    |---:|---|---|
    | **1** | **NINGUNA CELDA DE MI APERTURA SELLADA ...** | que ninguna celda ... |

**FUERA DE CITA es la mitad que hace el trabajo:** un acta que copia la tabla de la
anterior dentro de un bloque de cita la esta CITANDO, y eso es justo lo que no se
entrega.

**Y SI EL ACTA NOMBRA REMEDIOS Y NO PONE TABLA, EL INSTRUMENTO LO DICE EN VOZ ALTA**
en vez de callarse: un arnes que entrega cero remedios sin avisar es el mismo defecto
por la puerta de atras."""
assert s.count(viejo) == 1
s = s.replace(viejo, nuevo)

# ------------------------------------------------------- 2. constantes nuevas
viejo = '''TITULO_TAREA = "TAREA BLOQUEANTE DEL AUDITOR"
ENCABEZADO = re.compile(r"^>?\\s*#{1,6}\\s")
TOPE_DE_CUERPO = 40          # lineas por item: el resto se cita por su linea
'''
nuevo = '''TITULO_TAREA = "TAREA BLOQUEANTE DEL AUDITOR"
ENCABEZADO = re.compile(r"^>?\\s*#{1,6}\\s")
TOPE_DE_CUERPO = 40          # lineas por item: el resto se cita por su linea

# LA TABLA DE REMEDIOS: una tabla markdown, FUERA DE CITA, cuya cabecera nombre
# REMEDIO. Lo que se entrega son sus FILAS, una por remedio.
FILA = re.compile(r"^\\s*\\|")
SEPARADOR = re.compile(r"^\\s*\\|[\\s:|-]+\\|?\\s*$")
EN_CITA = re.compile(r"^\\s*>")
PALABRA_REMEDIO = "REMEDIO"
'''
assert s.count(viejo) == 1
s = s.replace(viejo, nuevo)

# ------------------------------------------------- 3. helpers de tabla y acta
viejo = '''def extraer(ruta_acta=None):
    """Devuelve el diccionario de lo que la vuelta hereda."""
    ruta_acta = ruta_acta or RUTA_ACTA
    if not os.path.exists(ruta_acta):
        return {"huella": "sin-acta", "acta": "(no hay acta todavia)", "items": []}
    lineas = comun.leer_texto(ruta_acta).split("\\n")
    inicio, titulo = _ultima_acta(lineas)
    items = []

    numero = inicio
    while numero < len(lineas):
        linea = lineas[numero]
        # 1. EL BLOQUE EN CITA con el titulo de la tarea bloqueante.
        if linea.lstrip().startswith(">") and TITULO_TAREA in linea:
            cuerpo = []
            while numero < len(lineas) and lineas[numero].lstrip().startswith(">"):
                cuerpo.append(lineas[numero])
                numero += 1
            items.append({"clase": "TAREA BLOQUEANTE", "linea": numero - len(cuerpo) + 1,
                          "cuerpo": _recortar(cuerpo, numero - len(cuerpo) + 1)})
            continue
        # 2. LA SECCION cuyo encabezado nombra un remedio.
        if ENCABEZADO.match(linea) and "REMEDIO" in linea.upper():
            primera = numero
            cuerpo = [linea]
            numero += 1
            while numero < len(lineas) and not ENCABEZADO.match(lineas[numero]):
                cuerpo.append(lineas[numero])
                numero += 1
            items.append({"clase": "REMEDIO", "linea": primera + 1,
                          "cuerpo": _recortar(cuerpo, primera + 1)})
            continue
        numero += 1

    return {"huella": huella(ruta_acta), "acta": titulo, "items": items}
'''
nuevo = '''def _es_cabecera_de_remedios(linea):
    """Cierto si esa fila de tabla es la CABECERA de una tabla de remedios.

    Se mira celda a celda y sin adorno: esta casa escribe `| # | **REMEDIO** | ... |`
    y la negrita no es parte del nombre de la columna.
    """
    if EN_CITA.match(linea) or not FILA.match(linea):
        return False
    for celda in linea.strip().strip("|").split("|"):
        if PALABRA_REMEDIO in ADORNO.sub("", celda).strip().upper():
            return True
    return False


def _seccion_de(lineas, numero):
    """El encabezado bajo el que vive esa linea, para que la fila no llegue desnuda."""
    for atras in range(numero, -1, -1):
        if ENCABEZADO.match(lineas[atras]) and not MARCA_ACTA.match(lineas[atras]):
            return lineas[atras].strip()
    return ""


def _acta_pedida(lineas, seleccion):
    """(inicio, fin, titulo) del acta pedida. Sin seleccion, la ULTIMA."""
    marcas = [n for n, l in enumerate(lineas) if MARCA_ACTA.match(l)]
    if not marcas:
        return 0, len(lineas), "(sin encabezado de acta)"
    elegida = marcas[-1]
    if seleccion:
        busca = seleccion.strip().upper()
        candidatas = [n for n in marcas if busca in lineas[n].upper()]
        if not candidatas:
            raise ValueError("ninguna acta encaja con %r" % (seleccion,))
        elegida = candidatas[-1]
    siguientes = [n for n in marcas if n > elegida]
    fin = siguientes[0] if siguientes else len(lineas)
    return elegida, fin, lineas[elegida].strip().lstrip("# ").strip()


def extraer(ruta_acta=None, seleccion=None):
    """Devuelve el diccionario de lo que la vuelta hereda.

    `seleccion` es un trozo del encabezado del acta (`"ACTA 28"`), y existe para el
    CASO POSITIVO: una guarda que solo se puede probar contra el acta de hoy no se
    puede probar (cosecha 7.C). Sin ella se lee la ULTIMA, que es lo que hace el arnes.
    """
    ruta_acta = ruta_acta or RUTA_ACTA
    if not os.path.exists(ruta_acta):
        return {"huella": "sin-acta", "acta": "(no hay acta todavia)", "items": [],
                "avisos": []}
    lineas = comun.leer_texto(ruta_acta).split("\\n")
    inicio, fin, titulo = _acta_pedida(lineas, seleccion)
    items, avisos = [], []
    menciones = 0

    numero = inicio
    while numero < fin:
        linea = lineas[numero]
        # 1. EL BLOQUE EN CITA con el titulo de la tarea bloqueante.
        if linea.lstrip().startswith(">") and TITULO_TAREA in linea:
            cuerpo = []
            while numero < fin and lineas[numero].lstrip().startswith(">"):
                cuerpo.append(lineas[numero])
                numero += 1
            items.append({"clase": "TAREA BLOQUEANTE", "linea": numero - len(cuerpo) + 1,
                          "cuerpo": _recortar(cuerpo, numero - len(cuerpo) + 1)})
            continue
        # 2. LA TABLA DE REMEDIOS QUE EL ACTA ESCRIBE: se entregan sus FILAS.
        if _es_cabecera_de_remedios(linea):
            cabecera, seccion = linea, _seccion_de(lineas, numero)
            numero += 1
            if numero < fin and SEPARADOR.match(lineas[numero]):
                numero += 1
            while (numero < fin and FILA.match(lineas[numero])
                   and not EN_CITA.match(lineas[numero])):
                items.append({"clase": "REMEDIO", "linea": numero + 1,
                              "cuerpo": _recortar([seccion, "", cabecera,
                                                   lineas[numero]], numero + 1)})
                numero += 1
            continue
        # 3. LO QUE SOLO MENCIONA LA PALABRA SE CUENTA, PARA PODER AVISAR.
        if ENCABEZADO.match(linea) and PALABRA_REMEDIO in linea.upper():
            menciones += 1
        numero += 1

    if menciones and not any(i["clase"] == "REMEDIO" for i in items):
        avisos.append(
            "AVISO: esta acta MENCIONA remedios en %d encabezado(s) y no ESCRIBE "
            "ninguna tabla de remedios fuera de cita. No se entrega ninguno, y se "
            "dice en voz alta: un arnes que entrega cero sin avisar es el defecto "
            "que la TAREA 2 de la vuelta 31 vino a cerrar." % menciones)

    return {"huella": huella(ruta_acta), "acta": titulo, "items": items,
            "avisos": avisos}
'''
assert s.count(viejo) == 1
s = s.replace(viejo, nuevo)

# ------------------------------------------------- 4. los avisos, en el prompt
viejo = '''    if not herencia["items"]:
        lineas.append("El acta anterior no dejo ninguna tarea bloqueante ni ningun "
                      "remedio escrito. Aun asi tienes que declarar la linea de lectura.")
'''
nuevo = '''    for aviso in herencia.get("avisos") or []:
        lineas.extend([aviso, ""])
    if not herencia["items"]:
        lineas.append("El acta anterior no dejo ninguna tarea bloqueante ni ningun "
                      "remedio escrito. Aun asi tienes que declarar la linea de lectura.")
'''
assert s.count(viejo) == 1
s = s.replace(viejo, nuevo)

# ------------------------------------------------------------- 5. el main y --acta
viejo = '''def main(argumentos=None):
    comun.salida_utf8()
    argumentos = list(argumentos or [])
    herencia = extraer()
'''
nuevo = '''def main(argumentos=None):
    comun.salida_utf8()
    argumentos = list(argumentos or [])
    seleccion = None
    if "--acta" in argumentos:
        donde = argumentos.index("--acta")
        if donde + 1 >= len(argumentos):
            print("forja.py herencia --acta necesita un trozo del encabezado del "
                  "acta, por ejemplo: --acta ACTA 28")
            return 2
        seleccion = argumentos[donde + 1]
    try:
        herencia = extraer(seleccion=seleccion)
    except ValueError as fallo:
        print("forja.py herencia: %s" % fallo)
        return 2
'''
assert s.count(viejo) == 1
s = s.replace(viejo, nuevo)

io.open(RUTA, "w", encoding="utf-8", newline="").write(s)
print("parche aplicado sobre " + RUTA)
