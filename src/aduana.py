# -*- coding: utf-8 -*-
"""LA ADUANA DE INSERCION (manual seccion 3).

La aduana no juzga: OBLIGA A JUZGAR. Ningun nodo entra sin pasar por aqui.

    python forja.py insertar candidato.json

Paso a paso, como manda la seccion 3 del manual:
  1. NORMALIZA id, fuentes y denominaciones, y valida contra el esquema.
  2. BLOQUEA con varias señales a la vez, porque se solapan poco.
  3. Si algun vecino supera umbral, la insercion SE BLOQUEA hasta que quien
     inserta escriba un veredicto por vecino citando su id.
  4 a 6. Serie numerada, caso, marco de pais, vigencia y herramienta con URL
     se registran en su censo AL ENTRAR, no en una auditoria posterior.
  Y solo con el gate verde sobre la copia en memoria el nodo se escribe.

AVISO DEL MANUAL, PRINCIPIO 4, QUE ESTE ARCHIVO NO PUEDE DESOBEDECER:
    LAS SEÑALES DE SUPERFICIE ORDENAN, NUNCA DECIDEN.
    Vocabulario compartido midio 3 por ciento de precision y familia de id
    50,8 por ciento. Las tres señales de aqui sirven para priorizar una cola
    de lectura; ninguna emite veredicto. Decide la lectura de una persona,
    y su razon escrita queda en bitacora/VEREDICTOS.jsonl.
"""

import datetime
import difflib
import os
import sys

from . import censos
from . import comun
from . import config as modulo_config
from . import esquema as modulo_esquema
from . import gate
from . import reglas_id
from .resolutor import Resolutor

CLASES = ("CONTINUA", "REPITE", "SANO")

CODIGO_OK = 0
CODIGO_RECHAZO = 1
CODIGO_BLOQUEO = 2
CODIGO_REPITE = 3


class Rechazo(Exception):

    def __init__(self, titulo, detalles):
        Exception.__init__(self, titulo)
        self.titulo = titulo
        self.detalles = list(detalles)


# ---------------------------------------------------------------- normalizar

def normalizar_candidato(bruto):
    """Paso 1 de la aduana. Devuelve (nodo, avisos).

    Normaliza lo que es forma (mayusculas, acentos en el id, espacios,
    siglas, orden de fuentes sin duplicados). No normaliza lo que es
    doctrina: si el id sigue rompiendo una regla, se rechaza en vez de
    maquillarse.
    """
    nodo = dict(bruto)
    avisos = []

    # Las claves que empiezan por guion bajo son notas del archivo candidato,
    # no campos del nodo: se descartan antes de mirar el esquema.
    for clave in sorted(nodo.keys()):
        if clave.startswith("_"):
            nodo.pop(clave)
            avisos.append("nota '%s' descartada: no es un campo del nodo" % clave)

    id_original = nodo.get("id")
    if isinstance(id_original, str):
        id_normalizado = reglas_id.normalizar(id_original)
        if id_normalizado != id_original:
            avisos.append("id normalizado: '%s' pasa a '%s'" % (id_original, id_normalizado))
        nodo["id"] = id_normalizado

    for campo in ("ids_alias", "nodos_previos", "nodos_siguientes"):
        valores = nodo.get(campo)
        if isinstance(valores, list):
            limpios = []
            for valor in valores:
                if isinstance(valor, str):
                    valor = reglas_id.normalizar(valor)
                if valor and valor not in limpios:
                    limpios.append(valor)
            nodo[campo] = limpios
        elif valores is None:
            nodo[campo] = []

    fuentes = nodo.get("fuentes")
    if isinstance(fuentes, list):
        limpias = []
        for fuente in fuentes:
            if isinstance(fuente, str):
                fuente = fuente.strip().lower()
            if fuente and fuente not in limpias:
                limpias.append(fuente)
            elif fuente in limpias:
                avisos.append("fuente repetida descartada: %s" % fuente)
        if limpias != fuentes:
            avisos.append("fuentes normalizadas (el orden se conserva: la fuente "
                          "añadida va en segundo lugar)")
        nodo["fuentes"] = limpias

    if isinstance(nodo.get("dominio"), str):
        nodo["dominio"] = reglas_id.normalizar(nodo["dominio"])

    denominaciones = dict(nodo.get("denominaciones") or {})
    denominaciones.setdefault("nombre_largo", "")
    denominaciones.setdefault("sigla", "")
    denominaciones.setdefault("otros_idiomas", [])
    if isinstance(denominaciones.get("nombre_largo"), str):
        denominaciones["nombre_largo"] = denominaciones["nombre_largo"].strip()
    if isinstance(denominaciones.get("sigla"), str):
        sigla = denominaciones["sigla"].strip()
        if sigla and sigla != sigla.upper():
            avisos.append("sigla normalizada a mayusculas: %s" % sigla.upper())
        denominaciones["sigla"] = sigla.upper()
    otros = []
    for entrada in denominaciones.get("otros_idiomas") or []:
        if isinstance(entrada, dict):
            otros.append({
                "idioma": (entrada.get("idioma") or "").strip().lower(),
                "termino": (entrada.get("termino") or "").strip(),
            })
        else:
            otros.append(entrada)
    denominaciones["otros_idiomas"] = otros
    nodo["denominaciones"] = denominaciones

    for campo in ("titulo", "resumen_teorico", "condiciones_activacion",
                  "entregable_esperado", "escala_minima", "marco_pais", "vigencia"):
        if isinstance(nodo.get(campo), str):
            nodo[campo] = nodo[campo].strip()
    if isinstance(nodo.get("pasos_accionables"), list):
        nodo["pasos_accionables"] = [p.strip() if isinstance(p, str) else p
                                     for p in nodo["pasos_accionables"]]
    return nodo, avisos


def validar_candidato(nodo, tabla_fuentes=None, esquema_nodo=None):
    """Esquema, reglas de id, fuentes canonicas y guiones. Lanza Rechazo."""
    esquema_nodo = esquema_nodo or modulo_esquema.cargar()
    tabla_fuentes = tabla_fuentes if tabla_fuentes is not None else comun.leer_json(comun.RUTA_FUENTES)

    fallos = modulo_esquema.validar(nodo, esquema_nodo)
    if fallos:
        raise Rechazo("el candidato no cumple esquema/nodo.schema.json", fallos)

    fallos = reglas_id.validar(nodo.get("id"), "id")
    for alias in nodo.get("ids_alias") or []:
        fallos.extend(reglas_id.validar(alias, "ids_alias '%s'" % alias, es_alias=True))
    if fallos:
        raise Rechazo("el candidato rompe docs/REGLAS_DE_ID.md", fallos)

    claves = set(k for k in tabla_fuentes.keys() if not k.startswith("_"))
    fallos = []
    for fuente in nodo.get("fuentes") or []:
        if fuente not in claves:
            fallos.append("fuente '%s' fuera de fuentes/FUENTES_CANONICAS.json. "
                          "La fuente canonica se registra ANTES del primer nodo del "
                          "libro (manual seccion 7.1)" % fuente)
    for atribucion in nodo.get("atribuciones") or []:
        fuente = (atribucion or {}).get("fuente")
        if fuente and fuente not in claves:
            fallos.append("atribucion con fuente '%s' fuera de la tabla canonica" % fuente)
    if fallos:
        raise Rechazo("LA FUENTE ES UN CAMPO SAGRADO (manual principio 8)", fallos)

    fallos = []
    for campo, texto in comun.textos_de_nodo(nodo):
        for _, columna, caracter, nombre in comun.buscar_guiones(texto):
            fallos.append("%s columna %d: %s (%s)" % (campo, columna, nombre, repr(caracter)))
    if fallos:
        raise Rechazo("guiones prohibidos en el texto del candidato", fallos)


# -------------------------------------------------------------------- señales
#
# Tres señales que se corren SIEMPRE a la vez, porque se solapan poco (la
# casa midio entre 3 y 6 por ciento de solape entre similitud y barrido
# paso contra nodo). Ninguna decide: todas ordenan.

def _ratio(a, b):
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()


def senal_similitud_texto(texto_a, texto_b):
    """Señal 1: titulo mas resumen mas pasos, contra lo mismo del vecino.

    Dos lecturas del mismo par: la de caracteres (aguanta el cambio de
    palabra por sinonimo, que es como se disfraza un gemelo) y la de
    secuencia de palabras (aguanta el relleno intercalado). Se toma la mas
    alta: la señal ordena la cola, y una cola corta de mas es barata al
    lado de un gemelo que entra.
    """
    directa = _ratio(texto_a, texto_b)
    por_palabras = _ratio(texto_a.split(), texto_b.split())
    return max(directa, por_palabras)


def senal_familia_id(id_a, id_b):
    """Señal 2: familia de id, normalizando sufijos, preposiciones,
    articulos, plurales y orden de palabras."""
    return reglas_id.similitud_familia(id_a, id_b)


def senal_paso_contra_nodo(candidato, vecino):
    """Señal 3: el texto de un paso contra el nodo del otro lado, en los DOS
    sentidos. El sentido inverso es el que descubre a un hijo: un hijo
    despliega en siete pasos una linea que la madre nombra en una."""
    mejor = 0.0
    detalle = ""
    pasos_candidato = [comun.normalizar_texto(p) for p in candidato.get("pasos_accionables") or []]
    pasos_vecino = [comun.normalizar_texto(p) for p in vecino.get("pasos_accionables") or []]
    cuerpo_candidato = comun.normalizar_texto(
        "%s. %s" % (candidato.get("titulo") or "", candidato.get("resumen_teorico") or ""))
    cuerpo_vecino = comun.normalizar_texto(
        "%s. %s" % (vecino.get("titulo") or "", vecino.get("resumen_teorico") or ""))

    for indice, paso in enumerate(pasos_candidato):
        for otro_indice, otro in enumerate(pasos_vecino):
            valor = _ratio(paso, otro)
            if valor > mejor:
                mejor = valor
                detalle = ("paso %d del candidato contra paso %d de %s"
                           % (indice + 1, otro_indice + 1, vecino.get("id")))
        valor = _ratio(paso, cuerpo_vecino)
        if valor > mejor:
            mejor = valor
            detalle = "paso %d del candidato contra el cuerpo de %s" % (indice + 1, vecino.get("id"))

    for indice, paso in enumerate(pasos_vecino):
        valor = _ratio(paso, cuerpo_candidato)
        if valor > mejor:
            mejor = valor
            detalle = ("paso %d de %s desplegado por el cuerpo del candidato"
                       % (indice + 1, vecino.get("id")))
    return mejor, detalle


def medir(candidato, vecino, umbrales=None):
    umbrales = umbrales or modulo_config.cargar()
    similitud = senal_similitud_texto(comun.texto_comparable(candidato),
                                      comun.texto_comparable(vecino))
    familia = senal_familia_id(candidato.get("id") or "", vecino.get("id") or "")
    paso, detalle_paso = senal_paso_contra_nodo(candidato, vecino)
    levantada_por = []
    if similitud >= umbrales["umbral_similitud_texto"]:
        levantada_por.append("similitud_texto")
    if familia >= umbrales["umbral_familia_id"]:
        levantada_por.append("familia_id")
    if paso >= umbrales["umbral_paso_contra_nodo"]:
        levantada_por.append("paso_contra_nodo")
    return {
        "id": vecino.get("id"),
        "titulo": vecino.get("titulo"),
        "dominio": vecino.get("dominio"),
        "senales": {
            "similitud_texto": round(similitud, 3),
            "familia_id": round(familia, 3),
            "paso_contra_nodo": round(paso, 3),
        },
        "detalle_paso": detalle_paso,
        "levantada_por": levantada_por,
    }


def buscar_vecinos(candidato, nodos, umbrales=None):
    """Paso 2 de la aduana: BLOQUEA (busca vecinos) multi señal.

    Reporta TODOS los vecinos que superen umbral, con la señal que los
    levanto y su valor. Ordena por la señal mas alta; el orden es una cola
    de lectura, nunca un ranking de culpables.
    """
    umbrales = umbrales or modulo_config.cargar()
    resolutor = Resolutor(nodos)
    vecinos = []
    for nodo in nodos:
        if resolutor.mismo(nodo.get("id"), candidato.get("id")):
            continue
        if umbrales.get("solo_dominio_y_nucleo"):
            permitidos = set(umbrales.get("dominios_nucleo") or [])
            permitidos.add(candidato.get("dominio"))
            if nodo.get("dominio") not in permitidos:
                continue
        medicion = medir(candidato, nodo, umbrales)
        if medicion["levantada_por"]:
            vecinos.append(medicion)
    vecinos.sort(key=lambda v: max(v["senales"].values()), reverse=True)
    return vecinos[:int(umbrales.get("maximo_vecinos_reportados", 25))]


# ----------------------------------------------------------------- veredictos

def parsear_veredicto(texto):
    """Formato: vecino|CLASE|clave=valor|razon libre

    Ejemplos:
      "extraer_nodos|CONTINUA|madre=extraer_nodos|el candidato despliega su paso 3"
      "extraer_nodos|REPITE|no añade procedimiento nuevo en ningun lado"
      "extraer_nodos|SANO|comparten vocabulario, no procedimiento"
    """
    partes = [p.strip() for p in (texto or "").split("|")]
    if len(partes) < 3:
        raise Rechazo("veredicto ilegible: %r" % texto,
                      ["formato: vecino|CLASE|[madre=<id>|]razon escrita",
                       "CLASE es una de: %s" % ", ".join(CLASES)])
    vecino = reglas_id.normalizar(partes[0])
    clase = partes[1].upper()
    if clase not in CLASES:
        raise Rechazo("clase de veredicto desconocida: %s" % partes[1],
                      ["las clases son: %s (manual seccion 4)" % ", ".join(CLASES)])
    opciones = {}
    razon = []
    for parte in partes[2:]:
        if "=" in parte and " " not in parte.split("=")[0]:
            clave, valor = parte.split("=", 1)
            opciones[clave.strip().lower()] = valor.strip()
        elif parte:
            razon.append(parte)
    if "razon" in opciones and opciones["razon"]:
        razon.insert(0, opciones.pop("razon"))
    return {"vecino": vecino, "clase": clase, "madre": opciones.get("madre", ""),
            "razon": " ".join(razon).strip()}


def _plantilla_de_reparto(candidato, vecino_id):
    ruta = comun.relativa(os.path.join(comun.RAIZ, "plantillas", "OPERACION_DE_FUSION.md"))
    lineas = [
        "",
        "EL NODO NO ENTRA. Veredicto REPITE contra %s." % vecino_id,
        "El material propio del candidato viaja al nodo existente como PERDIDAS",
        "REPARTIDAS (manual seccion 5). Rellena esta plantilla y ejecutala; la",
        "version completa, con simulacion y caso positivo, esta en %s" % ruta,
        "",
        "OPERACION DE FUSION",
        "  superviviente: %s" % vecino_id,
        "  absorbido:     %s (candidato, nunca llego a existir)" % candidato.get("id"),
        "  fuentes:       %s (orden significativo: la añadida va en segundo lugar)"
        % ", ".join(candidato.get("fuentes") or []),
        "",
        "  Los seis motivos, todos invisibles para la vara. Escribe QUE viaja y",
        "  A DONDE, o escribe 'nada' con razon. Un motivo en blanco es una perdida.",
        "",
        "  | motivo            | que se pierde del candidato | a donde viaja en %s |" % vecino_id,
        "  |---|---|---|",
        "  | NOMBRE            |  | denominacion en el texto (sigla y termino traducido, aparte) |",
        "  | ALCANCE           |  | a la enumeracion |",
        "  | DESTINO           |  | paso final |",
        "  | METODO ALTERNATIVO|  | variante condicional dentro del paso |",
        "  | DIRECCION         |  | dentro del paso |",
        "  | SALVAGUARDA       |  | adosada al paso de decision que protege |",
        "",
        "  persuasion (benchmarks, casos, cifras del autor con su atribucion):",
        "  escala (quien conserva la version ejecutable a escala minima):",
        "",
        "  ids_alias que gana el superviviente: %s" % (candidato.get("id") or ""),
        "  simulacion obligatoria antes de escribir: entradas redirigidas, duplicadas",
        "  nuevas, auto-aristas nacientes. Toda arista nueva se escribe RESUELTA.",
        "  caso positivo de la guarda: la prueba que falla si la fusion se hace mal.",
        "",
    ]
    return "\n".join(lineas)


# --------------------------------------------------------------------- censos

def _preguntas_censo(candidato):
    """Paso 4 a 6 de la aduana. Lo que la aduana PREGUNTA al insertar."""
    return [
        ("serie", "¿Es parte de una SERIE NUMERADA de un libro? "
                  "(un nodo por paso mas UNA cabeza, jamas dos compresiones). "
                  "Escribe el nombre de la serie, o 'no'"),
        ("caso", "¿Es un CASO O ESTUDIO? (el caso no es la casa: la doctrina vive en "
                 "su nodo). Escribe el nombre del caso, o 'no'"),
        ("marco_pais", "¿Cablea MARCO LEGAL DE UN PAIS? Escribe el pais, o 'no'"),
        ("vigencia", "¿Trae NORMA CON VERSION o cifra con fecha de corte? "
                     "Escribe la norma o cifra, o 'no'"),
        ("herramienta", "¿Nombra una HERRAMIENTA CON URL? Escribe la herramienta, o 'no'"),
    ]


def _partir_respuesta(valor):
    partes = [p.strip() for p in str(valor).split(";") if p.strip()]
    if not partes:
        return "", {}
    principal = partes[0]
    extra = {}
    for parte in partes[1:]:
        if "=" in parte:
            clave, sub = parte.split("=", 1)
            extra[clave.strip().lower()] = sub.strip()
    if "=" in principal:
        clave, sub = principal.split("=", 1)
        if clave.strip().lower() in ("serie", "caso", "pais", "norma", "herramienta", "valor"):
            extra[clave.strip().lower()] = sub.strip()
            principal = sub.strip()
    return principal, extra


def registrar_censos(candidato, respuestas, fecha):
    """Escribe en censos/*.md todo lo que corresponda. Devuelve lo escrito."""
    censos.crear_plantillas()
    escrito = []
    nodo_id = candidato.get("id")
    fuente = (candidato.get("fuentes") or [""])[0]

    for clave, valor in sorted((respuestas or {}).items()):
        principal, extra = _partir_respuesta(valor)
        if not principal or principal.lower() in ("no", "n", "ninguna", "ninguno", "-"):
            continue
        if clave == "serie":
            censos.registrar("series_y_cabezas", {
                "fecha": fecha, "nodo": nodo_id, "serie": principal,
                "papel": extra.get("papel", "paso"), "cabeza": extra.get("cabeza", ""),
                "fuente": fuente, "nota": extra.get("nota", "")})
            escrito.append("series_y_cabezas")
        elif clave == "caso":
            censos.registrar("casos", {
                "fecha": fecha, "nodo": nodo_id, "caso": principal,
                "nodo_de_doctrina": extra.get("doctrina", ""), "fuente": fuente,
                "nota": extra.get("nota", "")})
            escrito.append("casos")
        elif clave == "marco_pais":
            censos.registrar("marco_pais", {
                "fecha": fecha, "nodo": nodo_id, "pais": principal,
                "marco": extra.get("marco", candidato.get("marco_pais", "")),
                "fuente": fuente, "nota": extra.get("nota", "")})
            escrito.append("marco_pais")
        elif clave == "vigencia":
            censos.registrar("vigencia", {
                "fecha": fecha, "nodo": nodo_id, "norma_o_cifra": principal,
                "version": extra.get("version", ""),
                "fecha_corte": extra.get("corte", ""), "fuente": fuente,
                "nota": extra.get("nota", "")})
            escrito.append("vigencia")
        elif clave == "herramienta":
            censos.registrar("herramientas", {
                "fecha": fecha, "nodo": nodo_id, "herramienta": principal,
                "url": extra.get("url", ""), "fuente": fuente,
                "nota": extra.get("nota", "")})
            escrito.append("herramientas")

    respuestas = respuestas or {}
    if candidato.get("marco_pais") and "marco_pais" not in escrito:
        censos.registrar("marco_pais", {
            "fecha": fecha, "nodo": nodo_id, "pais": candidato["marco_pais"],
            "marco": candidato["marco_pais"], "fuente": fuente,
            "nota": "registrado desde el campo marco_pais del nodo"})
        escrito.append("marco_pais")
    if candidato.get("vigencia") and "vigencia" not in escrito:
        censos.registrar("vigencia", {
            "fecha": fecha, "nodo": nodo_id, "norma_o_cifra": candidato["vigencia"],
            "version": "", "fecha_corte": candidato["vigencia"], "fuente": fuente,
            "nota": "registrado desde el campo vigencia del nodo"})
        escrito.append("vigencia")

    for atribucion in candidato.get("atribuciones") or []:
        censos.registrar("atribuciones", {
            "fecha": fecha, "nodo": nodo_id, "cifra": atribucion.get("cifra"),
            "autor": atribucion.get("autor"), "fuente": atribucion.get("fuente"),
            "fecha_corte": atribucion.get("fecha_corte")})
        escrito.append("atribuciones")

    # Nombre largo, sigla y termino en otro idioma son TRES denominaciones
    # aparte, y cada una se registra (manual seccion 3.1).
    denominaciones = candidato.get("denominaciones") or {}
    if denominaciones.get("nombre_largo"):
        censos.registrar("denominaciones", {
            "fecha": fecha, "nodo": nodo_id, "clase": "nombre_largo",
            "denominacion": denominaciones["nombre_largo"], "idioma": "castellano", "nota": ""})
        escrito.append("denominaciones")
    if denominaciones.get("sigla"):
        censos.registrar("denominaciones", {
            "fecha": fecha, "nodo": nodo_id, "clase": "sigla",
            "denominacion": denominaciones["sigla"], "idioma": "castellano", "nota": ""})
        escrito.append("denominaciones")
    for otro in denominaciones.get("otros_idiomas") or []:
        censos.registrar("denominaciones", {
            "fecha": fecha, "nodo": nodo_id, "clase": "otro_idioma",
            "denominacion": otro.get("termino"), "idioma": otro.get("idioma"), "nota": ""})
        escrito.append("denominaciones")
    return escrito


# ------------------------------------------------------------------ insercion

class Resultado(object):

    def __init__(self):
        self.codigo = CODIGO_OK
        self.lineas = []
        self.vecinos = []
        self.veredictos = []
        self.aristas = []
        self.censos_escritos = []
        self.nodo = None

    def decir(self, texto=""):
        self.lineas.append(texto)

    def texto(self):
        return "\n".join(self.lineas)


def _hoy():
    return datetime.date.today().isoformat()


def insertar(candidato_bruto, veredictos_crudos=None, respuestas_censo=None,
             interactivo=False, ruta_dataset=None, ruta_veredictos=None,
             umbrales=None, entrada=None):
    """Corre la aduana entera. Devuelve un Resultado con su codigo de salida."""
    ruta_dataset = ruta_dataset or comun.RUTA_DATASET
    ruta_veredictos = ruta_veredictos or comun.RUTA_VEREDICTOS
    umbrales = umbrales or modulo_config.cargar()
    entrada = entrada or (lambda pregunta: input(pregunta))
    resultado = Resultado()
    fecha = _hoy()

    # 1. NORMALIZA y valida
    candidato, avisos = normalizar_candidato(candidato_bruto)
    resultado.nodo = candidato
    resultado.decir("ADUANA DE INSERCION, candidato '%s'" % candidato.get("id"))
    for aviso in avisos:
        resultado.decir("  normalizacion: %s" % aviso)
    try:
        validar_candidato(candidato)
    except Rechazo as rechazo:
        resultado.codigo = CODIGO_RECHAZO
        resultado.decir("")
        resultado.decir("RECHAZADO: %s" % rechazo.titulo)
        for detalle in rechazo.detalles:
            resultado.decir("  " + detalle)
        return resultado
    resultado.decir("  esquema, reglas de id, fuentes canonicas y guiones: verde")

    nodos = comun.leer_jsonl(ruta_dataset)
    resolutor = Resolutor(nodos)
    if resolutor.existe(candidato["id"]):
        resuelto = resolutor.resolver(candidato["id"])
        resultado.codigo = CODIGO_RECHAZO
        resultado.decir("")
        resultado.decir("RECHAZADO: el id ya vive en el grafo")
        resultado.decir("  '%s' resuelve a '%s'. UN CONCEPTO, UN NODO (manual principio 1)"
                        % (candidato["id"], resuelto))
        return resultado

    # 2. BLOQUEA: busca vecinos con las tres señales a la vez
    vecinos = buscar_vecinos(candidato, nodos, umbrales)
    resultado.vecinos = vecinos
    resultado.decir("  blocking multi señal contra %d nodo(s) del dataset" % len(nodos))

    veredictos = {}
    for crudo in veredictos_crudos or []:
        try:
            veredicto = parsear_veredicto(crudo)
        except Rechazo as rechazo:
            resultado.codigo = CODIGO_RECHAZO
            resultado.decir("")
            resultado.decir("RECHAZADO: %s" % rechazo.titulo)
            for detalle in rechazo.detalles:
                resultado.decir("  " + detalle)
            return resultado
        resuelto = resolutor.resolver(veredicto["vecino"]) or veredicto["vecino"]
        veredictos[resuelto] = veredicto

    if vecinos:
        resultado.decir("")
        resultado.decir("VECINOS POR ENCIMA DE UMBRAL: %d. LA INSERCION QUEDA BLOQUEADA."
                        % len(vecinos))
        resultado.decir("  Las señales ordenan, nunca deciden (manual principio 4):")
        resultado.decir("  esta cola es para leer, no un veredicto.")
        for vecino in vecinos:
            resultado.decir("")
            resultado.decir("  vecino %s  [%s]" % (vecino["id"], vecino["titulo"]))
            resultado.decir("    levantada por: %s" % ", ".join(vecino["levantada_por"]))
            resultado.decir("    similitud_texto %.3f (umbral %.2f) | familia_id %.3f "
                            "(umbral %.2f) | paso_contra_nodo %.3f (umbral %.2f)"
                            % (vecino["senales"]["similitud_texto"],
                               umbrales["umbral_similitud_texto"],
                               vecino["senales"]["familia_id"],
                               umbrales["umbral_familia_id"],
                               vecino["senales"]["paso_contra_nodo"],
                               umbrales["umbral_paso_contra_nodo"]))
            if vecino["detalle_paso"]:
                resultado.decir("    %s" % vecino["detalle_paso"])

        faltan = [v["id"] for v in vecinos if v["id"] not in veredictos]
        if faltan and interactivo:
            for vecino_id in faltan:
                resultado.decir("")
                resultado.decir("  LA VARA (manual seccion 4): ¿el candidato CONTINUA el "
                                "trabajo de %s o lo REPITE?" % vecino_id)
                resultado.decir("  Tiene direccion: se pregunta que añade el HIJO a la MADRE. "
                                "No tiene bascula.")
                bruto = entrada("veredicto para %s (%s): " % (vecino_id, "/".join(CLASES)))
                clase = (bruto or "").strip().upper()
                razon = entrada("razon escrita (queda en la bitacora): ")
                madre = ""
                if clase == "CONTINUA":
                    madre = entrada("¿cual es la MADRE, %s o %s?: "
                                    % (vecino_id, candidato["id"]))
                veredictos[vecino_id] = {"vecino": vecino_id, "clase": clase,
                                         "madre": reglas_id.normalizar(madre or ""),
                                         "razon": (razon or "").strip()}
            faltan = [v["id"] for v in vecinos if v["id"] not in veredictos
                      or veredictos[v["id"]]["clase"] not in CLASES]

        if faltan:
            resultado.codigo = CODIGO_BLOQUEO
            resultado.decir("")
            resultado.decir("BLOQUEADO: faltan veredictos para %s" % ", ".join(faltan))
            resultado.decir("  La aduana no juzga: obliga a juzgar (manual seccion 3).")
            resultado.decir("  Vuelve a correr el comando con un veredicto por vecino:")
            for vecino_id in faltan:
                resultado.decir('    --veredicto "%s|CONTINUA|madre=%s|que añade el hijo a la madre"'
                                % (vecino_id, vecino_id))
                resultado.decir('    --veredicto "%s|REPITE|por que no añade procedimiento"' % vecino_id)
                resultado.decir('    --veredicto "%s|SANO|por que no son el mismo trabajo"' % vecino_id)
            return resultado

    # 3. Veredictos escritos: se registran TODOS en la bitacora
    aristas = []
    repite = []
    for vecino in vecinos:
        veredicto = veredictos[vecino["id"]]
        if veredicto["clase"] not in CLASES:
            resultado.codigo = CODIGO_RECHAZO
            resultado.decir("RECHAZADO: clase de veredicto desconocida para %s: %s"
                            % (vecino["id"], veredicto["clase"]))
            return resultado
        if not veredicto["razon"]:
            resultado.codigo = CODIGO_RECHAZO
            resultado.decir("")
            resultado.decir("RECHAZADO: el veredicto %s sobre %s va sin razon escrita."
                            % (veredicto["clase"], vecino["id"]))
            resultado.decir("  La razon escrita es el activo mas reutilizable del sistema "
                            "entero (manual seccion 2).")
            return resultado
        if veredicto["clase"] == "CONTINUA":
            madre = resolutor.resolver(veredicto["madre"]) or veredicto["madre"]
            if madre not in (vecino["id"], candidato["id"]):
                resultado.codigo = CODIGO_RECHAZO
                resultado.decir("")
                resultado.decir("RECHAZADO: CONTINUA exige declarar la arista madre-hijo.")
                resultado.decir("  La madre ha de ser %s o %s, y llego '%s'."
                                % (vecino["id"], candidato["id"], veredicto["madre"]))
                return resultado
            hijo = candidato["id"] if madre == vecino["id"] else vecino["id"]
            aristas.append({"madre": madre, "hijo": hijo, "vecino": vecino["id"]})
        elif veredicto["clase"] == "REPITE":
            repite.append(vecino["id"])
        registro = {
            "fecha": fecha,
            "candidato": candidato["id"],
            "vecino": vecino["id"],
            "senales": vecino["senales"],
            "levantada_por": vecino["levantada_por"],
            "detalle_paso": vecino["detalle_paso"],
            "veredicto": veredicto["clase"],
            "razon": veredicto["razon"],
            "arista": ("%s > %s" % (veredicto["madre"], candidato["id"]))
                      if veredicto["clase"] == "CONTINUA" else "",
        }
        comun.agregar_jsonl(ruta_veredictos, registro)
        resultado.veredictos.append(registro)

    if repite:
        resultado.codigo = CODIGO_REPITE
        resultado.decir("")
        for vecino_id in repite:
            resultado.decir(_plantilla_de_reparto(candidato, vecino_id))
        resultado.decir("Los veredictos quedaron en %s." % comun.relativa(ruta_veredictos))
        return resultado

    # Aristas escritas RESUELTAS al dia de su escritura (manual seccion 5)
    nodos_nuevos = [dict(n) for n in nodos]
    por_id = dict((n["id"], n) for n in nodos_nuevos if n.get("id"))
    nuevo = dict(candidato)
    nuevo["nodos_previos"] = list(nuevo.get("nodos_previos") or [])
    nuevo["nodos_siguientes"] = list(nuevo.get("nodos_siguientes") or [])
    resolutor_futuro = Resolutor(nodos_nuevos + [nuevo])
    nuevo["nodos_previos"] = resolutor_futuro.resolver_lista(nuevo["nodos_previos"])
    nuevo["nodos_siguientes"] = resolutor_futuro.resolver_lista(nuevo["nodos_siguientes"])

    for arista in aristas:
        madre, hijo = arista["madre"], arista["hijo"]
        nodo_madre = nuevo if madre == candidato["id"] else por_id.get(madre)
        nodo_hijo = nuevo if hijo == candidato["id"] else por_id.get(hijo)
        if nodo_madre is None or nodo_hijo is None:
            resultado.codigo = CODIGO_RECHAZO
            resultado.decir("RECHAZADO: no encuentro los dos extremos de la arista %s > %s"
                            % (madre, hijo))
            return resultado
        siguientes = list(nodo_madre.get("nodos_siguientes") or [])
        if hijo not in resolutor_futuro.resolver_lista(siguientes):
            siguientes.append(hijo)
        nodo_madre["nodos_siguientes"] = siguientes
        previos = list(nodo_hijo.get("nodos_previos") or [])
        if madre not in resolutor_futuro.resolver_lista(previos):
            previos.append(madre)
        nodo_hijo["nodos_previos"] = previos
        resultado.aristas.append("%s > %s" % (madre, hijo))
        resultado.decir("  arista madre-hijo cableada y escrita RESUELTA: %s > %s" % (madre, hijo))

    # 4 a 6. Censos AL ENTRAR
    respuestas = dict(respuestas_censo or {})
    if interactivo:
        for clave, pregunta in _preguntas_censo(candidato):
            if clave in respuestas:
                continue
            respuestas[clave] = entrada(pregunta + ": ")

    # Simulacion obligatoria sobre copia en memoria antes de escribir
    dataset_futuro = nodos_nuevos + [nuevo]
    fallos = gate.verificar(dataset_futuro)
    if fallos:
        resultado.codigo = CODIGO_RECHAZO
        resultado.decir("")
        resultado.decir("RECHAZADO POR EL GATE en la simulacion sobre copia en memoria.")
        resultado.decir("  El dataset NO se toco. Fallos:")
        for fallo in fallos:
            resultado.decir("    " + str(fallo))
        return resultado

    comun.escribir_jsonl(ruta_dataset, dataset_futuro)
    resultado.censos_escritos = registrar_censos(nuevo, respuestas, fecha)
    resultado.decir("")
    resultado.decir("GATE VERDE sobre la simulacion. NODO INSERTADO en %s."
                    % comun.relativa(ruta_dataset))
    resultado.decir("  nodos en el grafo: %d" % len(dataset_futuro))
    if resultado.censos_escritos:
        resultado.decir("  censos escritos: %s"
                        % ", ".join(sorted(set(resultado.censos_escritos))))
    if resultado.veredictos:
        resultado.decir("  veredictos en %s: %d"
                        % (comun.relativa(ruta_veredictos), len(resultado.veredictos)))
    return resultado


# ------------------------------------------------------------------------ cli

def main(argumentos=None):
    comun.salida_utf8()
    argumentos = list(argumentos or sys.argv[1:])
    ruta_candidato = None
    veredictos = []
    respuestas = {}
    interactivo = None

    indice = 0
    while indice < len(argumentos):
        argumento = argumentos[indice]
        if argumento == "--veredicto":
            indice += 1
            veredictos.append(argumentos[indice])
        elif argumento.startswith("--veredicto="):
            veredictos.append(argumento.split("=", 1)[1])
        elif argumento == "--censo":
            indice += 1
            clave, valor = argumentos[indice].split("=", 1)
            respuestas[clave.strip()] = valor
        elif argumento.startswith("--censo="):
            clave, valor = argumento.split("=", 1)[1].split("=", 1)
            respuestas[clave.strip()] = valor
        elif argumento == "--sin-preguntas":
            interactivo = False
        elif argumento == "--preguntar":
            interactivo = True
        elif argumento.startswith("--"):
            print("opcion desconocida: %s" % argumento)
            return CODIGO_RECHAZO
        else:
            ruta_candidato = argumento
        indice += 1

    if not ruta_candidato:
        print("uso: python forja.py insertar candidato.json "
              '[--veredicto "vecino|CLASE|madre=<id>|razon"] [--censo clave=valor] '
              "[--sin-preguntas]")
        return CODIGO_RECHAZO

    if interactivo is None:
        interactivo = sys.stdin is not None and sys.stdin.isatty()

    bruto = comun.leer_json(ruta_candidato)
    resultado = insertar(bruto, veredictos, respuestas, interactivo=interactivo)
    print(resultado.texto())
    return resultado.codigo
