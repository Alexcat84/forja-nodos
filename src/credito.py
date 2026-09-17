# -*- coding: utf-8 -*-
"""LA RACHA ES DE SU LINEA, Y VIVE EN UN FICHERO POR LINEA (D.48).

    python forja.py credito                      el estado de la racha de ESTA linea
    python forja.py credito --linea gerber_emyth el de otra
    python forja.py credito --lineas             que lineas tienen registro
    python forja.py credito --revisar            replay contra lo declarado
    python forja.py credito --anotar --especie REPORTE --vuelta 33 --tanda "ACTA 32"
                            --racha "0 de 3" [--cae] --cita "ACTA 32 seccion 9.1"
    python forja.py credito --citas          comprueba que las citas sean REFERENCIA

POR QUE EXISTE. El 16 sep 2026 corrieron cuatro sesiones a la vez: la de insercion y
tres frentes de libro. Los tres frentes nacieron de una rama de la serial, **se llevaron
su `ACTA_AUDITOR.md` entero**, y el auditor del primero paro citando como suyas **tres
tandas que no eran suyas**, de un libro que no era el suyo. El auditor de `gerber_emyth`
levanto el hueco y **se nego a elegir para no absolverse**:

    "seguidas significa consecutivas: cuatro sesiones simultaneas no tienen orden entre
    si, asi que la palabra que sostiene la regla no tiene referente aqui. No es una regla
    que se pueda extender: es un hueco."

**`D.48` cierra el hueco:** una racha cuenta tandas SEGUIDAS, y una secuencia solo existe
dentro de una linea de trabajo. Fuera de su linea la palabra no tiene referente.

LO QUE HACE. Cada linea escribe en `docs/loop/CREDITO_<linea>.jsonl`, la serial incluida.
Una linea por suceso, y hay tres:

    {"tipo": "nacimiento", "linea": "...", "cita": "..."}
    {"tipo": "tanda", "linea": "...", "vuelta": 32, "tanda": "ACTA 31",
     "especie": "REPORTE", "cae": true, "racha": "3 de 3", "cita": "ACTA 31 9.1"}
    {"tipo": "reinicio", "linea": "...", "especie": "REPORTE", "racha": "0 de 3",
     "cita": "docs/loop/paradas/2026-09-17-...md"}

LA CIFRA DECLARADA MANDA, Y EL REPLAY SE PUBLICA APARTE. `estado()` devuelve lo que la
ultima linea de cada especie DECLARA, porque eso es lo que el acta adjudico y lo que la
decision del fundador escribio. `revisar()` vuelve a sumar `cae` desde el principio y
**dice donde las dos cuentas discrepan, en vez de elegir una en silencio**. Las dos
existen porque el historial migrado trae adjudicaciones posteriores que cambiaron una
tanda ya cerrada (la `ACTA 31` deshizo la limpieza de la `ACTA 30`), y una cuenta que
tapa eso no es una cuenta: es un adorno.

LO QUE NO HACE. **No reinicia nada por su cuenta.** Un reinicio es una linea `reinicio`
con su cita a un fichero de `docs/loop/paradas/`, que es lo que `AUDITOR_FORJA.md` 5.4
manda desde siempre: *un auditor que pone su propia racha a cero se esta absolviendo.*
"""

import json
import os
import subprocess
import sys

from . import comun

DIR_LOOP = os.path.join(comun.RAIZ, "docs", "loop")

# La rama de insercion se declara igual que en el arnes, y por el mismo motivo: el
# codigo no sabe que es un libro ni que es un frente, solo donde esta parado.
RAMA_DE_INSERCION = os.environ.get("RAMA_DE_INSERCION", "extraccion-mundo-11")
LINEA_SERIAL = "serial"

PREFIJO_DE_FRENTE = "extraccion-"

# Las especies de AUDITOR_FORJA.md 5.2 mas la del auditor (D.38). El tope va con la
# especie porque la regla de parada es distinta para cada una.
TOPES = {
    "CLASE": 2,
    "DATO MOVIDO": 2,
    "CIFRA PUBLICADA": 2,
    "REPORTE": 3,
    "AUDITOR": 3,
}

TIPOS = ("nacimiento", "tanda", "reinicio")


class CreditoMalEscrito(Exception):
    """Una linea del registro que no se puede leer. Nunca se salta en silencio."""


# EL VOCABULARIO DE LA CONCLUSION (D.53 punto 3, 17 sep 2026).
#
# UNA `cita` ES UNA REFERENCIA: ruta y linea del acta. NUNCA un resultado copiado.
# El motivo lo midio el auditor de la ACTA 32 contra el instrumento: la fase ciega
# leia el registro de credito, y el `cita` de una tanda ajena le dijo `11 SANO`
# ANTES de que contara los suyos. El arnes retiraba cuatro ficheros por una puerta
# y D.48 abrio otra.
#
# SE CAZA POR VOCABULARIO Y NO POR DIGITOS, y esa es la decision que importa: una
# referencia legitima lleva numeros por todas partes (`ACTA 33, seccion 9.1`,
# `docs/loop/paradas/2026-09-17-....md, punto 3`), asi que contar digitos daria
# falso positivo en casi todas. Lo que una referencia NO lleva nunca es el
# vocabulario con el que esta casa dice un veredicto o una medida.
PALABRAS_DE_CONCLUSION = (
    "sano", "continua", "repite", "mutuo", "puente", "transcripcion",
    "inventados", "por ciento", "al digito", "coinciden", "se sostienen",
    "verde", "rojo", "releidos", "discutibles", "caidas", "bloquearian",
    "entrarian", "tope",
)

# LO QUE SE QUEDO FUERA A PROPOSITO: `de 2` y `de 3`, que son la forma de una racha.
# Cazarian `punto 2 de 3` en una referencia legitima, y esta casa ya pago dos veces el
# precio de una guarda con falsos positivos: se aprende a no mirarla. La racha ya vive
# en su propio campo, asi que repetirla en la cita es redundante, no contaminante.


def cita_es_referencia(texto):
    """`(True, "")` si esa `cita` es una REFERENCIA; `(False, palabra)` si no.

    **Caso positivo:** `"ACTA 32, 11 SANO releidos"` cae y nombra `sano`.
    **Negativo:** `"ACTA 33, seccion 9.1"` pasa, con sus dos numeros dentro.
    """
    plano = comun.sin_acentos((texto or "").lower())
    for palabra in PALABRAS_DE_CONCLUSION:
        if palabra in plano:
            return False, palabra
    return True, ""


def rama_actual():
    """La rama de este arbol, o cadena vacia si aqui no hay git que responda."""
    try:
        salida = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=comun.RAIZ, stderr=subprocess.STDOUT)
    except (subprocess.CalledProcessError, OSError):
        return ""
    return salida.decode("utf-8", "replace").strip()


def linea_actual(rama=None):
    """EL NOMBRE DE LA LINEA DE TRABAJO EN LA QUE ESTE ARBOL ESTA PARADO.

    `FORJA_LINEA` manda sobre todo, que es lo que deja probar esto sin cambiar de rama.
    Despues, **la rama de insercion es `serial`** y se comprueba ANTES que el prefijo,
    porque `extraccion-mundo-11` tambien empieza por `extraccion-` y sin ese orden la
    serial se llamaria `mundo-11` y seria una linea mas.
    """
    declarada = os.environ.get("FORJA_LINEA", "").strip()
    if declarada:
        return declarada
    if rama is None:
        rama = rama_actual()
    if not rama:
        return LINEA_SERIAL
    if rama == RAMA_DE_INSERCION:
        return LINEA_SERIAL
    if rama.startswith(PREFIJO_DE_FRENTE):
        return rama[len(PREFIJO_DE_FRENTE):]
    return rama


def ruta(linea=None):
    return os.path.join(DIR_LOOP, "CREDITO_%s.jsonl" % (linea or linea_actual()))


def lineas_con_registro():
    """Las lineas que tienen fichero de credito, por nombre y ordenadas."""
    if not os.path.isdir(DIR_LOOP):
        return []
    nombres = []
    for nombre in sorted(os.listdir(DIR_LOOP)):
        if nombre.startswith("CREDITO_") and nombre.endswith(".jsonl"):
            nombres.append(nombre[len("CREDITO_"):-len(".jsonl")])
    return nombres


def _normalizar_especie(texto):
    return " ".join((texto or "").strip().upper().replace("`", "").split())


def _partir_racha(texto):
    """`"3 de 3"` da `(3, 3)`. Un `"0"` suelto da `(0, None)`, que es lo que la ACTA 1
    escribia antes de que la tabla llevara tope."""
    piezas = (texto or "").replace("`", "").strip().lower().split(" de ")
    try:
        cuenta = int(piezas[0].strip())
    except (ValueError, IndexError):
        raise CreditoMalEscrito("no se lee la racha %r" % texto)
    tope = None
    if len(piezas) > 1:
        try:
            tope = int(piezas[1].strip())
        except ValueError:
            tope = None
    return cuenta, tope


def leer(linea=None, ruta_registro=None):
    """Los sucesos del registro de una linea, en orden, con su numero de linea."""
    destino = ruta_registro or ruta(linea)
    if not os.path.exists(destino):
        return []
    sucesos = []
    with open(destino, "rb") as mano:
        for numero, cruda in enumerate(mano.read().decode("utf-8").splitlines(), 1):
            if not cruda.strip():
                continue
            try:
                suceso = json.loads(cruda)
            except ValueError as roto:
                raise CreditoMalEscrito(
                    "%s linea %d: %s" % (comun.relativa(destino), numero, roto))
            if suceso.get("tipo") not in TIPOS:
                raise CreditoMalEscrito(
                    "%s linea %d: tipo %r, y los tipos son %s"
                    % (comun.relativa(destino), numero, suceso.get("tipo"),
                       ", ".join(TIPOS)))
            suceso["_linea_del_fichero"] = numero
            sucesos.append(suceso)
    return sucesos


def nacida(linea=None, sucesos=None):
    """UNA LINEA SIN NINGUNA TANDA NO HA DICTADO NADA TODAVIA (D.48).

    Es la mitad de la regla que el arnes usa: un frente recien nacido **no hereda los
    remedios de la linea de la que salio**, porque esos remedios son de otra secuencia.
    """
    if sucesos is None:
        sucesos = leer(linea)
    return any(s.get("tipo") == "tanda" for s in sucesos)


def estado(linea=None, sucesos=None):
    """LO QUE CADA ESPECIE DECLARA HOY EN ESTA LINEA.

    Devuelve `{especie: {"racha", "cuenta", "tope", "cita", "de", "tipo"}}`. Lo que
    manda es **la ultima linea escrita de esa especie**, que es lo que el acta adjudico
    o lo que la decision del fundador escribio.
    """
    if sucesos is None:
        sucesos = leer(linea)
    vivo = {}
    for suceso in sucesos:
        if suceso.get("tipo") == "nacimiento":
            continue
        especie = _normalizar_especie(suceso.get("especie"))
        if not especie:
            raise CreditoMalEscrito(
                "linea %d del registro: un suceso %s sin especie"
                % (suceso.get("_linea_del_fichero", 0), suceso.get("tipo")))
        cuenta, tope = _partir_racha(suceso.get("racha"))
        vivo[especie] = {
            "racha": suceso.get("racha"),
            "cuenta": cuenta,
            "tope": tope if tope is not None else TOPES.get(especie),
            "cita": suceso.get("cita", ""),
            "de": suceso.get("tanda") or suceso.get("cita", ""),
            "tipo": suceso.get("tipo"),
        }
    return vivo


def en_tope(linea=None, sucesos=None):
    """Las especies cuya racha declarada llego a su tope. Es lo que para el bucle."""
    tocadas = []
    for especie, dato in sorted(estado(linea, sucesos).items()):
        if dato["tope"] and dato["cuenta"] >= dato["tope"]:
            tocadas.append((especie, dato))
    return tocadas


def revisar(linea=None, sucesos=None):
    """EL REPLAY, QUE SE PUBLICA APARTE Y NO PISA LO DECLARADO.

    Vuelve a sumar desde el principio: una tanda con `cae` suma uno, una tanda sin `cae`
    pone a cero (`D.38.1`, seguidas significa consecutivas), un reinicio pone a cero.
    Devuelve la lista de discrepancias contra la cifra declarada, **cada una con su
    numero de linea del fichero**.

    LO QUE NO VIGILA, Y POR QUE. **Las tandas `migrado` no se comprueban.** Su historia
    es anterior al registro, y **sus reinicios viven en `docs/loop/paradas/`**, que es
    donde `AUDITOR_FORJA.md` 5.4 siempre mando escribirlos: el replay de un tramo cuyos
    ceros no estan en el fichero no mide al auditor, mide al migrador. Una guarda que
    acusa de lo que no puede saber **no es una guarda: es ruido que se aprende a
    ignorar**, y esta casa ya pago eso una vez con el falso positivo de `D.40`.

    Lo que si vigila es **lo que se escriba a partir de ahora**, que es donde la cuenta
    y el dictado tienen que coincidir. Y las tandas sin `cae` se declaran como no
    replayables, porque el instrumento no sabe lo que no esta escrito.
    """
    if sucesos is None:
        sucesos = leer(linea)
    contador = {}
    discrepancias = []
    for suceso in sucesos:
        tipo = suceso.get("tipo")
        if tipo == "nacimiento":
            continue
        especie = _normalizar_especie(suceso.get("especie"))
        declarada, _ = _partir_racha(suceso.get("racha"))
        if tipo == "reinicio":
            contador[especie] = 0
            continue
        if "cae" not in suceso or suceso.get("migrado"):
            # historia migrada, o tanda sin el dato: el declarado pasa a ser el punto
            # de partida y no se acusa a nadie de lo que el registro no vio.
            contador[especie] = declarada
            continue
        contador[especie] = contador.get(especie, 0) + 1 if suceso["cae"] else 0
        if contador[especie] != declarada:
            discrepancias.append({
                "linea_del_fichero": suceso.get("_linea_del_fichero", 0),
                "especie": especie,
                "tanda": suceso.get("tanda", ""),
                "declarada": declarada,
                "replay": contador[especie],
                "cita": suceso.get("cita", ""),
            })
            contador[especie] = declarada
    return discrepancias


def citas_con_conclusion(linea=None, sucesos=None):
    """Las lineas del registro cuya `cita` trae una conclusion dentro (`D.53`)."""
    malas = []
    for suceso in (sucesos if sucesos is not None else leer(linea)):
        vale, palabra = cita_es_referencia(suceso.get("cita"))
        if not vale:
            malas.append({
                "linea_del_fichero": suceso.get("_linea_del_fichero", 0),
                "especie": _normalizar_especie(suceso.get("especie")),
                "tanda": suceso.get("tanda", ""),
                "cita": suceso.get("cita", ""),
                "palabra": palabra,
            })
    return malas


def anotar(suceso, linea=None, ruta_registro=None):
    """Aniade un suceso al registro de una linea, comprobandolo antes de escribir."""
    # los campos con guion bajo los pone `leer` al vuelo (el numero de linea del
    # fichero) y no son del suceso: se caen aqui y no viajan al registro.
    suceso = dict((k, v) for k, v in suceso.items() if not k.startswith("_"))
    suceso.setdefault("linea", linea or linea_actual())
    if suceso.get("tipo") not in TIPOS:
        raise CreditoMalEscrito(
            "tipo %r, y los tipos son %s" % (suceso.get("tipo"), ", ".join(TIPOS)))
    if suceso["tipo"] != "nacimiento":
        if not _normalizar_especie(suceso.get("especie")):
            raise CreditoMalEscrito("un suceso %s sin especie" % suceso["tipo"])
        _partir_racha(suceso.get("racha"))
        if not (suceso.get("cita") or "").strip():
            raise CreditoMalEscrito(
                "un suceso %s sin cita. Una racha sin cita no se puede releer"
                % suceso["tipo"])
        vale, palabra = cita_es_referencia(suceso.get("cita"))
        if not vale:
            raise CreditoMalEscrito(
                "la cita %r trae la palabra %r dentro, y eso es una CONCLUSION, no "
                "una referencia (D.53). Una cita es la ruta y la linea del acta: "
                "'ACTA 33, seccion 9.1'. La fase ciega lee este registro, y un "
                "resultado copiado aqui es contaminacion."
                % (suceso.get("cita"), palabra))
    destino = ruta_registro or ruta(suceso["linea"])
    comun.agregar_jsonl(destino, suceso)
    return destino


# --------------------------------------------------------------------- la voz

def texto_estado(linea=None):
    linea = linea or linea_actual()
    sucesos = leer(linea)
    partes = []
    partes.append("CREDITO DE LA LINEA '%s' (D.48)" % linea)
    partes.append("  registro: %s" % comun.relativa(ruta(linea)))
    if not sucesos:
        partes.append("")
        partes.append("  LINEA SIN REGISTRO: no hay ningun suceso escrito.")
        partes.append("  Una linea sin tandas NACE CON SU RACHA EN CERO y no hereda")
        partes.append("  la de nadie (D.48). Lo que herede el arnes sera CERO remedios.")
        return "\n".join(partes)
    if not nacida(linea, sucesos):
        partes.append("")
        partes.append("  LINEA RECIEN NACIDA: registro escrito, ninguna tanda cerrada.")
        partes.append("  Todas sus rachas estan en CERO y no hereda nada (D.48).")
        return "\n".join(partes)
    vivo = estado(linea, sucesos)
    tandas = sorted(set(s.get("tanda") for s in sucesos
                        if s.get("tipo") == "tanda" and s.get("tanda")))
    partes.append("  tandas: %d, en %d suceso(s) de especie"
                  % (len(tandas),
                     len([s for s in sucesos if s.get("tipo") == "tanda"])))
    partes.append("")
    partes.append("  %-18s %-10s %s" % ("especie", "racha", "de donde sale"))
    partes.append("  " + "-" * 70)
    for especie in sorted(vivo):
        dato = vivo[especie]
        marca = "  TOPE" if dato["tope"] and dato["cuenta"] >= dato["tope"] else ""
        partes.append("  %-18s %-10s %s%s"
                      % (especie, dato["racha"], dato["de"] or dato["cita"], marca))
    tope = en_tope(linea, sucesos)
    partes.append("")
    if tope:
        partes.append("  CREDITO ROTO: %s en su tope."
                      % ", ".join(e for e, _ in tope))
    else:
        partes.append("  CREDITO ENTERO: ninguna especie en su tope.")
    return "\n".join(partes)


def texto_revision(linea=None):
    linea = linea or linea_actual()
    sucesos = leer(linea)
    migradas = len([s for s in sucesos if s.get("migrado")])
    vigiladas = len([s for s in sucesos
                     if s.get("tipo") == "tanda" and not s.get("migrado")
                     and "cae" in s])
    cola = ("  %d suceso(s) migrado(s) quedan FUERA del replay: sus reinicios viven "
            "en docs/loop/paradas/, no en el registro." % migradas
            if migradas else "")
    discrepancias = revisar(linea, sucesos)
    if not discrepancias:
        cabeza = ("REPLAY VERDE en la linea '%s': las %d tanda(s) vigilables suman lo "
                  "que declaran." % (linea, vigiladas))
        return (cabeza + ("\n" + cola if cola else ""))
    partes = ["REPLAY CON %d DISCREPANCIA(S) en la linea '%s':"
              % (len(discrepancias), linea)]
    for caso in discrepancias:
        partes.append(
            "  linea %d del registro, %s en %s: declara %d, el replay da %d (%s)"
            % (caso["linea_del_fichero"], caso["especie"], caso["tanda"] or "?",
               caso["declarada"], caso["replay"], caso["cita"]))
    partes.append("")
    partes.append("LO DIGO Y NO LO ARREGLO: una adjudicacion posterior puede cambiar "
                  "una tanda ya cerrada, y eso es legitimo. Lo que no es legitimo es "
                  "que no se vea.")
    return "\n".join(partes)


def main(argumentos):
    comun.salida_utf8()
    linea = None
    modo = "estado"
    campos = {}
    resto = list(argumentos)
    while resto:
        pieza = resto.pop(0)
        if pieza == "--linea":
            linea = resto.pop(0)
        elif pieza == "--lineas":
            modo = "lineas"
        elif pieza == "--revisar":
            modo = "revisar"
        elif pieza == "--citas":
            modo = "citas"
        elif pieza == "--anotar":
            modo = "anotar"
        elif pieza == "--cae":
            campos["cae"] = True
        elif pieza == "--limpia":
            campos["cae"] = False
        elif pieza.startswith("--"):
            campos[pieza[2:]] = resto.pop(0) if resto else ""
        else:
            print("no entiendo %r" % pieza)
            return 2

    try:
        if modo == "lineas":
            registradas = lineas_con_registro()
            if not registradas:
                print("NINGUNA LINEA TIENE REGISTRO DE CREDITO todavia (D.48).")
                return 0
            print("LINEAS CON REGISTRO DE CREDITO (D.48), y la de este arbol es '%s':"
                  % linea_actual())
            for nombre in registradas:
                sucesos = leer(nombre)
                tandas = len([s for s in sucesos if s.get("tipo") == "tanda"])
                print("  %-28s %3d tanda(s)   %s"
                      % (nombre, tandas, comun.relativa(ruta(nombre))))
            return 0
        if modo == "citas":
            malas = citas_con_conclusion(linea)
            objetivo = linea or linea_actual()
            if not malas:
                print("CITAS VERDES en la linea '%s': todas son referencia, ninguna "
                      "trae una conclusion dentro (D.53)." % objetivo)
                return 0
            print("CITAS EN ROJO en la linea '%s': %d con conclusion dentro (D.53)"
                  % (objetivo, len(malas)))
            for mala in malas:
                print("  linea %d, %s en %s: %r trae %r"
                      % (mala["linea_del_fichero"], mala["especie"],
                         mala["tanda"] or "?", mala["cita"], mala["palabra"]))
            print("")
            print("UNA CITA ES LA RUTA Y LA LINEA DEL ACTA, nunca su resultado. La "
                  "fase ciega lee este registro.")
            return 1
        if modo == "revisar":
            print(texto_revision(linea))
            return 0
        if modo == "anotar":
            campos.setdefault("tipo", "tanda")
            if "vuelta" in campos:
                campos["vuelta"] = int(campos["vuelta"])
            destino = anotar(campos, linea)
            print("ANOTADO en %s:" % comun.relativa(destino))
            print("  " + json.dumps(campos, ensure_ascii=False, sort_keys=True))
            return 0
        print(texto_estado(linea))
        return 0
    except CreditoMalEscrito as roto:
        print("CREDITO MAL ESCRITO: %s" % roto)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
