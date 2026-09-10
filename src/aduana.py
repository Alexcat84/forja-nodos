# -*- coding: utf-8 -*-
"""LA ADUANA DE INSERCION (manual seccion 3).

La aduana no juzga: OBLIGA A JUZGAR. Ningun nodo entra sin pasar por aqui.

    python forja.py insertar candidato.json

Paso a paso, como manda la seccion 3 del manual:
  1. NORMALIZA id, fuentes y denominaciones, y valida contra el esquema.
  2. BLOQUEA con varias señales a la vez, porque se solapan poco.
  3. Si algun vecino supera umbral, la insercion SE BLOQUEA hasta que quien
     inserta escriba un veredicto por vecino citando su id: CONTINUA cablea
     la arista madre-hijo, REPITE deja el nodo fuera, SANO lo deja pasar sin
     arista, y MUTUO (adjudicacion A.1, docs/BANCO_DE_REGLAS.md) declara el
     UNICO enlace bidireccional legitimo, con su procedimiento de ida y de
     vuelta, y queda ademas en la lista blanca config/pares_mutuos.jsonl.
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

CLASES = ("CONTINUA", "REPITE", "SANO", "MUTUO")

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

def normalizar_candidato(bruto, fecha=None):
    """Paso 1 de la aduana. Devuelve (nodo, avisos).

    Normaliza lo que es forma (mayusculas, acentos en el id, espacios,
    siglas, claves de fuente sin duplicados). No normaliza lo que es
    doctrina: si el id sigue rompiendo una regla, o si el ORDEN de las
    fuentes no respeta su fecha, se rechaza en vez de maquillarse (lo
    comprueba el gate en la simulacion, no este paso).

    `fecha` es la fecha de hoy, para completar una entrada de `fuentes`
    que llega sin la suya: no es doctrina, es la fecha en la que la fuente
    de verdad entro al nodo.
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
        claves_vistas = set()
        for entrada in fuentes:
            if not isinstance(entrada, dict):
                # forma ajena al esquema: se deja tal cual y el esquema la
                # rechaza con su propio mensaje, mas claro que uno de aqui.
                limpias.append(entrada)
                continue
            vale = dict(entrada)
            clave = vale.get("clave")
            if isinstance(clave, str):
                clave = clave.strip().lower()
            vale["clave"] = clave
            if isinstance(vale.get("fecha"), str):
                vale["fecha"] = vale["fecha"].strip()
            if not vale.get("fecha") and fecha:
                vale["fecha"] = fecha
                avisos.append("fuente '%s' sin fecha: se le puso la fecha de hoy (%s)"
                              % (clave, fecha))
            if clave and clave in claves_vistas:
                avisos.append("fuente repetida descartada: %s" % clave)
                continue
            if clave:
                claves_vistas.add(clave)
            limpias.append(vale)
        nodo["fuentes"] = limpias

    if isinstance(nodo.get("dominio"), str):
        nodo["dominio"] = reglas_id.normalizar(nodo["dominio"])

    # Un nodo nace VIVO. Deprecar es un acto de fusion, con su plantilla y su
    # simulacion (D.17): no es algo que un candidato pueda declarar al entrar.
    if not nodo.get("estado"):
        nodo["estado"] = "vivo"
    elif nodo.get("estado") == "deprecado":
        avisos.append("el candidato llega declarandose deprecado: entra VIVO. "
                      "Deprecar es un acto de fusion, no una linea del candidato (D.17)")
        nodo["estado"] = "vivo"

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
    for entrada in nodo.get("fuentes") or []:
        clave = entrada.get("clave") if isinstance(entrada, dict) else entrada
        if clave not in claves:
            fallos.append("fuente '%s' fuera de fuentes/FUENTES_CANONICAS.json. "
                          "La fuente canonica se registra ANTES del primer nodo del "
                          "libro (manual seccion 7.1)" % clave)
    for atribucion in nodo.get("atribuciones") or []:
        fuente = (atribucion or {}).get("fuente")
        if fuente and fuente not in claves:
            fallos.append("atribucion con fuente '%s' fuera de la tabla canonica" % fuente)
    if fallos:
        raise Rechazo("LA FUENTE ES UN CAMPO SAGRADO (manual principio 8)", fallos)

    fallos = []
    for campo, texto in comun.textos_de_nodo(nodo):
        for _, columna, caracter, nombre in comun.buscar_guiones(texto):
            fallos.append("%s columna %d: %s"
                          % (campo, columna, comun.nombrar_guion(caracter)))
    if fallos:
        raise Rechazo("guiones prohibidos en el texto del candidato", fallos)


# -------------------------------------------------------------------- señales
#
# Tres señales que se corren SIEMPRE a la vez, porque se solapan poco (la
# casa midio entre 3 y 6 por ciento de solape entre similitud y barrido
# paso contra nodo). Ninguna decide: todas ordenan.

class NoAplica(object):
    """La salida de una señal FUERA DE SU DOMINIO DE APLICACION (D.16).

    REGLA MADRE, medida en My-idea el 15 ago 2026 y corregida por decision
    del fundador el mismo dia: la señal de bloque de `costuras_internas.py`
    recorria un rango que con cinco pasos quedaba VACIO, y devolvia 0,0
    dijera lo que dijera el texto. Y los dos nodos de calibracion tenian
    cinco pasos, porque la propia campaña los habia destejido.

        El 0,0 no era un nodo sin bloque: ERA LA SEÑAL MUERTA.

    Un cero de señal muerta es indistinguible de un cero de vecino ajeno, y
    esa confusion se lee como salud. Por eso esta clase REVIENTA si alguien
    la compara con un umbral, en vez de dejarse leer como "no se parece".
    """

    def __init__(self, motivo):
        self.motivo = motivo

    def __repr__(self):
        return "NO APLICA (%s)" % self.motivo

    def __str__(self):
        return "NO APLICA: %s" % self.motivo

    def _revienta(self, otro):
        raise TypeError(
            "una señal que NO APLICA no se compara con un umbral. Motivo: %s. "
            "Un cero silencioso de señal muerta se lee como salud, y esa es "
            "exactamente la averia que D.16 existe para impedir." % self.motivo)

    __lt__ = _revienta
    __le__ = _revienta
    __gt__ = _revienta
    __ge__ = _revienta

    def __float__(self):
        self._revienta(None)


def _ratio(a, b):
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()


def _ordenable_de_senal(valor):
    """Para ordenar la cola de lectura. Un NO APLICA ya declarado (que en el
    informe viaja como texto) va al fondo. Ordenar no es comparar con un
    umbral: es poner en fila, y eso una señal muerta si lo aguanta."""
    if isinstance(valor, str):
        return -1.0
    return float(valor)


def senal_similitud_texto(texto_a, texto_b):
    """Señal 1: titulo mas resumen mas pasos, contra lo mismo del vecino.

    Dos lecturas del mismo par: la de caracteres (aguanta el cambio de
    palabra por sinonimo, que es como se disfraza un gemelo) y la de
    secuencia de palabras (aguanta el relleno intercalado). Se toma la mas
    alta: la señal ordena la cola, y una cola corta de mas es barata al
    lado de un gemelo que entra.
    """
    if not texto_a or not texto_b:
        return NoAplica("uno de los dos nodos no tiene texto comparable "
                        "(titulo, resumen ni pasos)")
    directa = _ratio(texto_a, texto_b)
    por_palabras = _ratio(texto_a.split(), texto_b.split())
    return max(directa, por_palabras)


def senal_familia_id(id_a, id_b):
    """Señal 2: familia de id, normalizando sufijos, preposiciones,
    articulos, plurales y orden de palabras."""
    if not reglas_id.familia(id_a) or not reglas_id.familia(id_b):
        return NoAplica("uno de los dos ids no deja ninguna pieza tras "
                        "normalizar su familia")
    return reglas_id.similitud_familia(id_a, id_b)


def senal_paso_contra_nodo(candidato, vecino):
    """Señal 3: el texto de un paso contra el nodo del otro lado, en los DOS
    sentidos. El sentido inverso es el que descubre a un hijo: un hijo
    despliega en siete pasos una linea que la madre nombra en una."""
    mejor = 0.0
    detalle = ""
    pasos_candidato = [comun.normalizar_texto(p) for p in candidato.get("pasos_accionables") or []]
    pasos_vecino = [comun.normalizar_texto(p) for p in vecino.get("pasos_accionables") or []]
    if not pasos_candidato or not pasos_vecino:
        return (NoAplica("uno de los dos nodos no tiene pasos que barrer"), "")
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

    # NINGUNA SEÑAL SE COMPARA CON SU UMBRAL SI NO APLICA (D.16). Una señal
    # fuera de su dominio no vota: se declara, y su declaracion viaja al
    # reporte para que el lector sepa que esa señal no miro.
    levantada_por = []
    senales = {}
    for nombre, valor, umbral in (
            ("similitud_texto", similitud, umbrales["umbral_similitud_texto"]),
            ("familia_id", familia, umbrales["umbral_familia_id"]),
            ("paso_contra_nodo", paso, umbrales["umbral_paso_contra_nodo"])):
        if isinstance(valor, NoAplica):
            senales[nombre] = str(valor)
            continue
        senales[nombre] = round(valor, 3)
        if valor >= umbral:
            levantada_por.append(nombre)

    return {
        "id": vecino.get("id"),
        "titulo": vecino.get("titulo"),
        "dominio": vecino.get("dominio"),
        "senales": senales,
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
        # EL DEPRECADO NO SE OFRECE (D.17). Es archivo: bloquear un candidato
        # contra un nodo que ya no es superficie mandaria a leer una ficha
        # muerta, y su material vivo ya esta en el superviviente.
        if nodo.get("id") in resolutor.deprecados:
            continue
        if umbrales.get("solo_dominio_y_nucleo"):
            permitidos = set(umbrales.get("dominios_nucleo") or [])
            permitidos.add(candidato.get("dominio"))
            if nodo.get("dominio") not in permitidos:
                continue
        medicion = medir(candidato, nodo, umbrales)
        if medicion["levantada_por"]:
            vecinos.append(medicion)
    vecinos.sort(key=lambda v: max(_ordenable_de_senal(x) for x in v["senales"].values()),
                 reverse=True)
    # SE DEVUELVEN TODOS. El tope de config/umbrales.json es de IMPRESION, no de
    # exigencia: recorta cuantos se DETALLAN en la salida, jamas cuantos piden
    # veredicto.
    #
    # Antes de la tanda B esta linea era `return vecinos[:tope]`, y era un
    # defecto de la especie que esta casa mas persigue: el propio
    # config/umbrales.json promete que "se reportan TODOS los vecinos que
    # superen umbral", y el codigo se quedaba con veinticinco SIN DECIRLO. Y la
    # mitad grave no era el recorte: era que `faltan` se computaba sobre la
    # lista recortada, asi que un vecino numero veintiseis dejaba de necesitar
    # veredicto. Un recorte silencioso no ordenaba la cola: le bajaba el
    # liston. Cazado midiendo la cola contra el catalogo de referencia
    # (docs/CALIBRACION_D4.md).
    return vecinos


# ----------------------------------------------------------------- veredictos

def parsear_veredicto(texto):
    """Formato general: vecino|CLASE|clave=valor|razon libre

    MUTUO es distinto: NUNCA lleva razon libre, y CITA LA LINEA. Exige DOS
    claves, ida= y vuelta=, y cada una empieza por el NUMERO DEL PASO que el
    otro nodo despliega:

        ida=<n>:<razon>       n es el paso DEL CANDIDATO que el vecino despliega
        vuelta=<m>:<razon>    m es el paso DEL VECINO que el candidato despliega

    Por que la linea y no solo la razon (adjudicacion A.4, banco de textos
    9.22 de My-idea): LA VARA ES UNA RELACION ENTRE LINEAS, NO ENTRE NODOS.
    Dos nodos pueden ser cada uno hijo del otro sin que ninguno repita al
    otro, porque la linea que uno expande no es la linea que el otro expande.
    Y su comprobacion: si las dos direcciones apuntan a LA MISMA LINEA no es
    esta figura, es un solape, y se rechaza nombrando el paso.

    Ejemplos:
      "extraer_nodos|CONTINUA|madre=extraer_nodos|el candidato despliega su paso 3"
      "extraer_nodos|REPITE|no añade procedimiento nuevo en ningun lado"
      "extraer_nodos|SANO|comparten vocabulario, no procedimiento"
      "extraer_nodos|MUTUO|ida=2:el vecino despliega entero mi paso 2|"
      "vuelta=5:yo despliego entero su paso 5"
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

    if clase == "MUTUO":
        crudo_ida = opciones.get("ida", "").strip()
        crudo_vuelta = opciones.get("vuelta", "").strip()
        if not crudo_ida or not crudo_vuelta:
            raise Rechazo(
                "veredicto MUTUO sin los dos procedimientos declarados",
                ["MUTUO exige ida=<n>:<razon> y vuelta=<m>:<razon>",
                 "n es el paso DEL CANDIDATO que el vecino despliega",
                 "m es el paso DEL VECINO que el candidato despliega",
                 "un enlace mutuo declarado es la unica vuelta legitima "
                 "(adjudicacion A.1, docs/BANCO_DE_REGLAS.md)"])
        paso_ida, ida = _partir_cita_de_linea(crudo_ida, "ida")
        paso_vuelta, vuelta = _partir_cita_de_linea(crudo_vuelta, "vuelta")
        return {"vecino": vecino, "clase": clase, "madre": "",
                "ida": ida, "vuelta": vuelta,
                "paso_ida": paso_ida, "paso_vuelta": paso_vuelta,
                "razon": "ida (paso %d del candidato): %s | vuelta (paso %d del vecino): %s"
                         % (paso_ida, ida, paso_vuelta, vuelta)}

    if "razon" in opciones and opciones["razon"]:
        razon.insert(0, opciones.pop("razon"))
    return {"vecino": vecino, "clase": clase, "madre": opciones.get("madre", ""),
            "ida": "", "vuelta": "", "paso_ida": 0, "paso_vuelta": 0,
            "razon": " ".join(razon).strip()}


def _partir_cita_de_linea(crudo, sentido):
    """Parte '<n>:<razon>' en (n, razon). Lanza Rechazo si falta la linea.

    La cita de la linea no es un adorno del formato: es la comprobacion que
    separa el enlace mutuo del solape (banco de textos 9.22). Sin numero de
    paso no hay nada que comparar, y sin comparacion la clase MUTUO seria
    una firma en blanco.
    """
    cabeza, separador, cola = crudo.partition(":")
    cabeza = cabeza.strip()
    if not separador or not cabeza.isdigit():
        raise Rechazo(
            "el sentido '%s' del MUTUO no cita su linea" % sentido,
            ["llego: %r" % crudo,
             "formato: %s=<numero de paso>:<razon escrita>" % sentido,
             "LA VARA ES UNA RELACION ENTRE LINEAS, NO ENTRE NODOS (9.22): sin el "
             "numero del paso no se puede comprobar que los dos sentidos expanden "
             "lineas DISTINTAS, que es lo unico que separa un enlace mutuo de un solape"])
    razon = cola.strip()
    if not razon:
        raise Rechazo(
            "el sentido '%s' del MUTUO cita su linea pero no escribe su razon" % sentido,
            ["llego: %r" % crudo,
             "formato: %s=<numero de paso>:<razon escrita>" % sentido])
    numero = int(cabeza)
    if numero < 1:
        raise Rechazo(
            "el sentido '%s' del MUTUO cita el paso %d" % (sentido, numero),
            ["los pasos se cuentan desde 1"])
    return numero, razon


def validar_lineas_mutuo(candidato, vecino_nodo, veredicto):
    """Comprueba que el MUTUO cita DOS LINEAS DISTINTAS. Lanza Rechazo.

    Regla madre: banco de textos 9.22 de My-idea, LA VARA EN LOS DOS
    SENTIDOS, y su comprobacion literal:

        La figura exige dos lineas distintas, una en cada nodo. Si las dos
        direcciones apuntan a LA MISMA LINEA, no es esta figura: es un
        solape y se juzga por las reglas de siempre.

    Fundirlos seria el error caro, porque borraria los dos procedimientos
    para dejar un nodo con dos lineas sueltas. Pero blanquear un solape como
    si fuera enlace mutuo es el error barato y silencioso, y es el que esta
    guarda caza.
    """
    pasos_candidato = candidato.get("pasos_accionables") or []
    pasos_vecino = vecino_nodo.get("pasos_accionables") or []
    paso_ida = veredicto.get("paso_ida") or 0
    paso_vuelta = veredicto.get("paso_vuelta") or 0

    if not 1 <= paso_ida <= len(pasos_candidato):
        raise Rechazo(
            "el MUTUO con %s cita un paso que el candidato no tiene" % vecino_nodo.get("id"),
            ["ida cita el paso %d y el candidato '%s' tiene %d paso(s)"
             % (paso_ida, candidato.get("id"), len(pasos_candidato)),
             "ida cita un paso DEL CANDIDATO: es la linea que el vecino despliega"])
    if not 1 <= paso_vuelta <= len(pasos_vecino):
        raise Rechazo(
            "el MUTUO con %s cita un paso que el vecino no tiene" % vecino_nodo.get("id"),
            ["vuelta cita el paso %d y el vecino '%s' tiene %d paso(s)"
             % (paso_vuelta, vecino_nodo.get("id"), len(pasos_vecino)),
             "vuelta cita un paso DEL VECINO: es la linea que el candidato despliega"])

    texto_ida = pasos_candidato[paso_ida - 1]
    texto_vuelta = pasos_vecino[paso_vuelta - 1]
    if comun.normalizar_texto(texto_ida) == comun.normalizar_texto(texto_vuelta):
        raise Rechazo(
            "SOLAPE DISFRAZADO DE ENLACE MUTUO: los dos sentidos apuntan a la misma linea",
            ["ida cita el paso %d de '%s': %s" % (paso_ida, candidato.get("id"), texto_ida),
             "vuelta cita el paso %d de '%s': %s"
             % (paso_vuelta, vecino_nodo.get("id"), texto_vuelta),
             "las dos lineas dicen lo mismo, asi que no hay dos procedimientos que "
             "expandir: hay uno solo, repetido en los dos nodos",
             "la figura del enlace mutuo EXIGE dos lineas distintas, una en cada nodo "
             "(banco de textos 9.22 de My-idea). Esto no es MUTUO: se juzga con la vara "
             "de siempre, CONTINUA o REPITE"])
    return {"paso_ida": paso_ida, "texto_ida": texto_ida,
            "paso_vuelta": paso_vuelta, "texto_vuelta": texto_vuelta}


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
        % ", ".join("%s (%s)" % (f.get("clave"), f.get("fecha"))
                    for f in candidato.get("fuentes") or [] if isinstance(f, dict)),
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
    primeras_fuentes = candidato.get("fuentes") or []
    fuente = (primeras_fuentes[0].get("clave", "")
             if primeras_fuentes and isinstance(primeras_fuentes[0], dict) else "")

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
        self.mutuos = []
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
             ruta_pares_mutuos=None, umbrales=None, entrada=None):
    """Corre la aduana entera. Devuelve un Resultado con su codigo de salida."""
    ruta_dataset = ruta_dataset or comun.RUTA_DATASET
    ruta_veredictos = ruta_veredictos or comun.RUTA_VEREDICTOS
    ruta_pares_mutuos = ruta_pares_mutuos or comun.RUTA_PARES_MUTUOS
    umbrales = umbrales or modulo_config.cargar()
    entrada = entrada or (lambda pregunta: input(pregunta))
    resultado = Resultado()
    fecha = _hoy()

    # 1. NORMALIZA y valida
    candidato, avisos = normalizar_candidato(candidato_bruto, fecha)
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

    # ------------------------------------------------------------------
    # LA ARISTA QUE LA SEÑAL NO LEVANTA SE DECLARA POR LECTURA (D.19, D.29).
    #
    # Un veredicto puede nombrar a un nodo que las tres señales NO levantaron.
    # Eso no es un error del lector: es EL CASO NORMAL de la jerarquia, y esta
    # casa lo tiene medido. La aduana caza duplicados; la jerarquia la caza la
    # LECTURA, y la señal 3 solo levanta el 3 por ciento de las aristas
    # declaradas (docs/CALIBRACION_D4.md seccion 7).
    #
    # HASTA EL 10 SEP 2026 ESTE CODIGO PARSEABA ESE VEREDICTO Y LO TIRABA. El
    # bucle que escribe aristas y bitacora iteraba `for vecino in vecinos`, asi
    # que un veredicto sobre un no vecino se quedaba en este diccionario sin que
    # nadie lo leyera: la insercion decia que todo fue bien, el nodo entraba, y
    # NI LA ARISTA NI LA RAZON ESCRITA SE ESCRIBIAN EN NINGUNA PARTE. Un
    # veredicto aceptado en silencio es peor que uno rechazado, porque el
    # rechazo se ve.
    #
    # Lo encontro el fundador al autorizar la primera insercion real, sobre el
    # primer par madre e hijo de esta casa: `formular_codigo...` a
    # `verificar_afirmaciones...`, que mide 0,572 contra un umbral de 0,60.
    #
    # LO QUE ESTO NO HACE, y es la mitad que importa: no relaja nada. Un
    # veredicto declarado AÑADE una obligacion, jamas retira otra. `faltan` se
    # sigue computando sobre los vecinos que las señales levantaron, asi que
    # declarar una lectura no exime de juzgar un vecino real.
    # ------------------------------------------------------------------
    ids_vecinos = set(v["id"] for v in vecinos)
    declarados = []
    for vecino_id in sorted(veredictos):
        if vecino_id in ids_vecinos:
            continue
        nodo_declarado = resolutor.canonicos.get(vecino_id)
        if nodo_declarado is None:
            resultado.codigo = CODIGO_RECHAZO
            resultado.decir("")
            resultado.decir("RECHAZADO: el veredicto nombra a '%s' y ese nodo no vive "
                            "en el grafo." % vecino_id)
            resultado.decir("  Una arista se cablea contra un id que YA existe. Si la "
                            "madre todavia esta en cuarentena, entra ella primero.")
            return resultado
        medicion = medir(candidato, nodo_declarado, umbrales)
        # SE DECLARA COMO LO QUE ES. La bitacora guarda las señales REALES, que
        # es la prueba de que ninguna la levanto, y dice quien la levanto: un
        # lector.
        medicion["levantada_por"] = ["lectura declarada"]
        declarados.append(medicion)

    if declarados:
        resultado.decir("")
        resultado.decir("DECLARADOS POR LECTURA: %d. Ninguna señal los levanto."
                        % len(declarados))
        for declarado in declarados:
            resultado.decir("  %s  [%s]" % (declarado["id"], declarado["titulo"]))
            resultado.decir("    señales: %s"
                            % ", ".join("%s %s" % (nombre, valor)
                                        for nombre, valor in sorted(declarado["senales"].items())))
            resultado.decir("    umbrales: similitud %.2f, familia %.2f, paso %.2f"
                            % (umbrales["umbral_similitud_texto"],
                               umbrales["umbral_familia_id"],
                               umbrales["umbral_paso_contra_nodo"]))
        resultado.decir("  LA JERARQUIA LA CAZA LA LECTURA, NO LA SEÑAL (D.19, D.29).")

    if vecinos:
        resultado.decir("")
        resultado.decir("VECINOS POR ENCIMA DE UMBRAL: %d. LA INSERCION QUEDA BLOQUEADA."
                        % len(vecinos))
        resultado.decir("  Las señales ordenan, nunca deciden (manual principio 4):")
        resultado.decir("  esta cola es para leer, no un veredicto.")
        tope = int(umbrales.get("maximo_vecinos_reportados", 25))
        if len(vecinos) > tope:
            # EL RECORTE SE DECLARA, NUNCA SE APLICA EN SILENCIO. Solo recorta
            # cuantos se DETALLAN: los %d de arriba siguen pidiendo veredicto.
            resultado.decir("")
            resultado.decir("  AVISO: esta salida DETALLA los %d primeros de %d. Los %d "
                            "restantes van nombrados al final, y TODOS piden veredicto: "
                            "el tope de config/umbrales.json es de impresion, no de "
                            "exigencia." % (tope, len(vecinos), len(vecinos) - tope))
        for vecino in vecinos[:tope]:
            resultado.decir("")
            resultado.decir("  vecino %s  [%s]" % (vecino["id"], vecino["titulo"]))
            resultado.decir("    levantada por: %s" % ", ".join(vecino["levantada_por"]))
            for nombre, clave_umbral in (
                    ("similitud_texto", "umbral_similitud_texto"),
                    ("familia_id", "umbral_familia_id"),
                    ("paso_contra_nodo", "umbral_paso_contra_nodo")):
                medida = vecino["senales"][nombre]
                if isinstance(medida, str):
                    # D.16: una señal que no aplica se DECLARA, no se imprime
                    # como cero. El lector tiene que saber que no miro.
                    resultado.decir("    %-18s %s" % (nombre, medida))
                else:
                    resultado.decir("    %-18s %.3f (umbral %.2f)"
                                    % (nombre, medida, umbrales[clave_umbral]))
            if vecino["detalle_paso"]:
                resultado.decir("    %s" % vecino["detalle_paso"])

        if len(vecinos) > tope:
            resultado.decir("")
            resultado.decir("  LOS %d QUE ESTA SALIDA NO DETALLA, nombrados uno a uno "
                            "porque tambien piden veredicto:" % (len(vecinos) - tope))
            for vecino in vecinos[tope:]:
                resultado.decir("    %s  [levantada por: %s]"
                                % (vecino["id"], ", ".join(vecino["levantada_por"])))

        # LA EXIGENCIA CUBRE A TODOS LOS VECINOS, no a los que se imprimieron.
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
                resultado.decir('    --veredicto "%s|MUTUO|ida=<procedimiento de ida>|'
                                'vuelta=<procedimiento de vuelta>"' % vecino_id)
            return resultado

    # 3. Veredictos escritos: se registran TODOS en la bitacora
    #
    # LOS DECLARADOS POR LECTURA PASAN POR EL MISMO SITIO. No hay un camino
    # corto para ellos: se les exige la misma razon escrita, se les cablea la
    # arista igual, y guardan la misma huella de vigencia. Lo unico distinto es
    # quien los levanto, y eso queda escrito en el registro.
    aristas = []
    repite = []
    mutuos = []
    for vecino in vecinos + declarados:
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
        elif veredicto["clase"] == "MUTUO":
            # La cita de las DOS LINEAS DISTINTAS se comprueba contra los nodos
            # de verdad, no contra el texto del veredicto (adjudicacion A.4).
            vecino_nodo = resolutor.canonicos.get(vecino["id"])
            if vecino_nodo is None:
                resultado.codigo = CODIGO_RECHAZO
                resultado.decir("RECHAZADO: no encuentro al vecino %s para comprobar "
                                "las lineas del enlace mutuo" % vecino["id"])
                return resultado
            try:
                lineas = validar_lineas_mutuo(candidato, vecino_nodo, veredicto)
            except Rechazo as rechazo:
                resultado.codigo = CODIGO_RECHAZO
                resultado.decir("")
                resultado.decir("RECHAZADO: %s" % rechazo.titulo)
                for detalle in rechazo.detalles:
                    resultado.decir("  " + detalle)
                return resultado
            mutuos.append({"vecino": vecino["id"], "ida": veredicto["ida"],
                           "vuelta": veredicto["vuelta"],
                           "paso_ida": lineas["paso_ida"],
                           "texto_ida": lineas["texto_ida"],
                           "paso_vuelta": lineas["paso_vuelta"],
                           "texto_vuelta": lineas["texto_vuelta"]})
        # BLOQUE DE VIGENCIA (D.15): el veredicto guarda la huella del texto
        # contra el que se emitio, en los dos lados. Sin esto, dentro de tres
        # cirugias nadie sabra si esta lectura sigue siendo de este texto.
        vecino_nodo = resolutor.canonicos.get(vecino["id"]) or {}
        registro = {
            "fecha": fecha,
            "candidato": candidato["id"],
            "vecino": vecino["id"],
            "huella_candidato": comun.huella_de_nodo(candidato),
            "huella_vecino": comun.huella_de_nodo(vecino_nodo),
            "senales": vecino["senales"],
            "levantada_por": vecino["levantada_por"],
            "detalle_paso": vecino["detalle_paso"],
            "veredicto": veredicto["clase"],
            "razon": veredicto["razon"],
            "arista": ("%s > %s" % (veredicto["madre"], candidato["id"]))
                      if veredicto["clase"] == "CONTINUA"
                      else ("%s <> %s" % (candidato["id"], vecino["id"]))
                      if veredicto["clase"] == "MUTUO" else "",
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

    # ENLACE MUTUO DECLARADO (adjudicacion A.1): la unica vuelta legitima.
    # Se cablea en los DOS sentidos a la vez, porque ninguno de los dos es
    # madre exclusiva del otro.
    for mutuo in mutuos:
        vecino_id = mutuo["vecino"]
        nodo_vecino = por_id.get(vecino_id)
        if nodo_vecino is None:
            resultado.codigo = CODIGO_RECHAZO
            resultado.decir("RECHAZADO: no encuentro al vecino %s para el enlace mutuo"
                            % vecino_id)
            return resultado
        for campo in ("nodos_siguientes", "nodos_previos"):
            lista_candidato = list(nuevo.get(campo) or [])
            if vecino_id not in resolutor_futuro.resolver_lista(lista_candidato):
                lista_candidato.append(vecino_id)
            nuevo[campo] = lista_candidato
            lista_vecino = list(nodo_vecino.get(campo) or [])
            if candidato["id"] not in resolutor_futuro.resolver_lista(lista_vecino):
                lista_vecino.append(candidato["id"])
            nodo_vecino[campo] = lista_vecino
        # LA CITA SE CONSTRUYE UNA SOLA VEZ y se usa para las dos cosas: la
        # simulacion del gate y la escritura del registro. Si la simulacion
        # viera una cita distinta de la que se escribe, estaria probando otro
        # dato: el gate rechazaria una cita completa por incompleta, o peor,
        # dejaria pasar una incompleta por haber simulado una completa.
        resultado.mutuos.append({
            "par": [candidato["id"], vecino_id],
            "fecha": fecha,
            "declarado_por": candidato["id"],
            "paso_ida": mutuo["paso_ida"],
            "razon_ida": mutuo["ida"],
            "huella_ida": comun.huella_de_texto(mutuo["texto_ida"]),
            "paso_vuelta": mutuo["paso_vuelta"],
            "razon_vuelta": mutuo["vuelta"],
            "huella_vuelta": comun.huella_de_texto(mutuo["texto_vuelta"])})
        resultado.decir("  enlace mutuo declarado y cableado en los dos sentidos: %s <> %s"
                        % (candidato["id"], vecino_id))
        resultado.decir("    cita: ida es el paso %d de %s, vuelta es el paso %d de %s"
                        % (mutuo["paso_ida"], candidato["id"],
                           mutuo["paso_vuelta"], vecino_id))

    # 4 a 6. Censos AL ENTRAR
    respuestas = dict(respuestas_censo or {})
    if interactivo:
        for clave, pregunta in _preguntas_censo(candidato):
            if clave in respuestas:
                continue
            respuestas[clave] = entrada(pregunta + ": ")

    # Simulacion obligatoria sobre copia en memoria antes de escribir. Los
    # enlaces mutuos que este nodo declara AHORA tienen que entrar tambien
    # a la simulacion, o el gate veria una vuelta sin blanquear y la
    # rechazaria en su propia insercion.
    dataset_futuro = nodos_nuevos + [nuevo]
    pares_mutuos_existentes = modulo_config.cargar_pares_mutuos(ruta_pares_mutuos)
    pares_mutuos_simulacion = list(pares_mutuos_existentes) + list(resultado.mutuos)
    fallos = gate.verificar(dataset_futuro, pares_mutuos=pares_mutuos_simulacion)
    if fallos:
        resultado.codigo = CODIGO_RECHAZO
        resultado.decir("")
        resultado.decir("RECHAZADO POR EL GATE en la simulacion sobre copia en memoria.")
        resultado.decir("  El dataset NO se toco. Fallos:")
        for fallo in fallos:
            resultado.decir("    " + str(fallo))
        return resultado

    comun.escribir_jsonl(ruta_dataset, dataset_futuro)
    # REGISTRO DE CITAS, no lista blanca (D.14). Cada par lleva su ida, su
    # vuelta, las DOS lineas que cita, la fecha, quien lo declaro y la huella
    # del texto de cada linea. Un par sin cita completa es rojo en el gate.
    for mutuo in resultado.mutuos:
        comun.agregar_jsonl(ruta_pares_mutuos, mutuo)
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
    if resultado.mutuos:
        resultado.decir("  enlaces mutuos en %s: %d"
                        % (comun.relativa(ruta_pares_mutuos), len(resultado.mutuos)))
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
