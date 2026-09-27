# -*- coding: utf-8 -*-
"""LA OPERACION DE CORREGIR EL `resumen_teorico` DE UN NODO YA INSERTADO.

    python forja.py corregir --nodo <id> --anade "CORRECCION DECLARADA ..." --razon "..."

PARA QUE EXISTE. `EXTRACTOR.md` 2 dice dos cosas a la vez: que **no se escribe a
mano en `dataset/nodos.jsonl`, nunca**, y que **si hace falta tocar el dataset
por otra via, eso es una operacion escrita con su simulacion y su caso positivo,
no una edicion**. Hasta hoy existia la primera mitad y no la segunda: `insertar`
rechaza un id que ya vive, `arista` solo toca los dos campos de arista, y
**ningun comando podia corregir una frase falsa dentro de un nodo que ya entro**.
La vuelta 25 se paro por eso (`REPORTE.md` `S.9`) y la `ACTA 25` `3.1` adjudico
que la casa ya tenia escrito que se hace: **esta es esa via.**

EL CASO QUE LA HIZO FALTA, y esta contado: el metodo del ancla textual unica de
la vuelta 19 dejo **4 de 24** candidatos con una frase verificable y FALSA dentro
de su `resumen_teorico` (el ancla que dicen no es unica, o no esta en la unidad
declarada, o no esta en el libro). Los cuatro viven hoy en el grafo.

LO QUE HACE, Y SOLO ESO:

  - **ANIADE AL FINAL. NO BORRA NI SUSTITUYE NADA.** Es correccion declarada, que
    es como corrige esta casa: el texto viejo se queda, y debajo se escribe que
    estaba mal y que hay en su lugar. Un borrado no deja rastro de la caida, y
    una caida sin rastro se repite.
  - **SOLO `resumen_teorico`.** Los pasos, el titulo, el entregable y las fuentes
    NO se tocan por aqui: cambiar un paso es cambiar el procedimiento, y eso
    entra por la aduana como candidato, no por una correccion de prosa.
  - **SIMULA SOBRE COPIA EN MEMORIA Y PASA EL GATE ANTES DE ESCRIBIR.** Si la
    copia futura no pasa el gate, no se escribe nada.
  - **DEJA SU RAZON EN LA BITACORA**, con la huella del nodo antes y despues. Una
    correccion sin razon escrita es una edicion a mano con otro nombre.

LO QUE EXIGE, Y NO ES NEGOCIABLE:

  --anade   TIENE QUE EMPEZAR POR `CORRECCION DECLARADA`. No es ceremonia: es el
            mismo remedio mecanico de `D.35`. **Un remedio que se cumple
            acordandose no es un remedio**, asi que la marca se teclea o la
            operacion no corre.
  --razon   la razon escrita, que va a la bitacora.
"""

from . import aduana
from . import comun
from . import config as modulo_config
from . import gate
from . import reglas_id
from .resolutor import Resolutor

CODIGO_OK = 0
CODIGO_RECHAZO = 1

CAMPO_UNICO = "resumen_teorico"
MARCA = "CORRECCION DECLARADA"
MINIMO_TEXTO = 40


class Resultado(object):

    def __init__(self):
        self.codigo = CODIGO_OK
        self.lineas = []
        self.registro = None

    def decir(self, linea):
        self.lineas.append(linea)

    def rechazar(self, titulo, detalles):
        self.codigo = CODIGO_RECHAZO
        self.decir("")
        self.decir("RECHAZADO: %s" % titulo)
        for detalle in detalles:
            self.decir("  " + detalle)
        self.decir("  NADA SE ESCRIBIO.")
        return self

    def texto(self):
        return "\n".join(self.lineas)


def corregir(nodo_id, anade, razon, campo=None, ruta_dataset=None,
             ruta_veredictos=None, ruta_pares_mutuos=None):
    """Aniade una correccion declarada al resumen_teorico. Devuelve un Resultado."""
    ruta_dataset = ruta_dataset or comun.RUTA_DATASET
    ruta_veredictos = ruta_veredictos or comun.RUTA_VEREDICTOS
    campo = campo or CAMPO_UNICO
    resultado = Resultado()

    nodo_id = reglas_id.normalizar(nodo_id or "")
    anade = (anade or "").strip()
    razon = (razon or "").strip()

    resultado.decir("CORRECCION DECLARADA SOBRE UN NODO YA INSERTADO")
    resultado.decir("  nodo : %s" % nodo_id)
    resultado.decir("  campo: %s" % campo)

    if campo != CAMPO_UNICO:
        return resultado.rechazar(
            "esta operacion solo toca '%s'" % CAMPO_UNICO,
            ["llego el campo '%s'." % campo,
             "Los pasos, el titulo y el entregable NO se corrigen por aqui:",
             "cambiar un paso es cambiar el procedimiento, y eso entra por la",
             "aduana como candidato (EXTRACTOR.md 2)."])

    if not razon:
        return resultado.rechazar(
            "la correccion va sin razon escrita",
            ["Una correccion sin razon escrita es una edicion a mano con otro",
             "nombre. Di QUE ERA FALSO y CON QUE MEDICION lo sabes."])

    if not anade:
        return resultado.rechazar(
            "no hay texto que aniadir",
            ["--anade lleva el texto de la correccion declarada."])

    if not anade.startswith(MARCA):
        return resultado.rechazar(
            "el texto aniadido no se declara como correccion",
            ["--anade tiene que EMPEZAR por '%s'." % MARCA,
             "Es el remedio mecanico de D.35: un remedio que se cumple",
             "acordandose no es un remedio. Quien lea el nodo maniana tiene que",
             "ver en la primera palabra que ese tramo corrige al anterior.",
             "llego: %r" % anade[:60]])

    if len(anade) < MINIMO_TEXTO:
        return resultado.rechazar(
            "el texto aniadido no dice nada",
            ["trae %d caracteres y el minimo son %d." % (len(anade), MINIMO_TEXTO),
             "Una correccion dice que estaba mal Y que hay en su lugar."])

    hallazgos = comun.buscar_guiones(anade)
    if hallazgos:
        return resultado.rechazar(
            "el texto aniadido trae guiones largos o medios",
            [str(hallazgo) for hallazgo in hallazgos[:5]])

    nodos = comun.leer_jsonl(ruta_dataset)
    resolutor = Resolutor(nodos)
    resuelto = resolutor.resolver(nodo_id)
    if resuelto is None:
        return resultado.rechazar(
            "'%s' no vive en el grafo" % nodo_id,
            ["Esta operacion corrige nodos YA INSERTADOS.",
             "Si el candidato sigue en cuarentena, se corrige su fichero por la",
             "via ordinaria y se le vuelve a correr la aduana (EXTRACTOR.md 16)."])

    por_id = dict((n["id"], n) for n in nodos if n.get("id"))
    nodo = por_id[resuelto]
    viejo = nodo.get(CAMPO_UNICO) or ""

    if anade in viejo:
        return resultado.rechazar(
            "esa misma correccion ya esta escrita en el nodo",
            ["El texto de --anade ya figura literal en el %s de '%s'."
             % (CAMPO_UNICO, resuelto),
             "Una correccion no se declara dos veces."])

    nuevo = (viejo + " " + anade).strip() if viejo else anade

    # EL TEXTO VIEJO SOBREVIVE ENTERO. Se comprueba, no se promete.
    if viejo and viejo not in nuevo:
        return resultado.rechazar(
            "la correccion habria borrado texto",
            ["Esta operacion SOLO aniade. Si esto salta, es un fallo del codigo",
             "y no del que lo llamo."])

    huella_antes = comun.huella_de_nodo(nodo)

    # LA SIMULACION, sobre copia en memoria y antes de escribir nada.
    futuro = [dict(n) for n in nodos]
    futuro_por_id = dict((n["id"], n) for n in futuro if n.get("id"))
    futuro_por_id[resuelto][CAMPO_UNICO] = nuevo

    fallos = gate.verificar(futuro, pares_mutuos=modulo_config.cargar_pares_mutuos(
        ruta_pares_mutuos))
    if fallos:
        resultado.codigo = CODIGO_RECHAZO
        resultado.decir("")
        resultado.decir("RECHAZADO POR EL GATE en la simulacion sobre copia en memoria.")
        resultado.decir("  NADA SE ESCRIBIO.")
        for fallo in fallos[:10]:
            resultado.decir("  %s" % fallo)
        return resultado

    huella_despues = comun.huella_de_nodo(futuro_por_id[resuelto])

    registro = {
        "fecha": aduana._hoy(),
        "candidato": resuelto,
        "vecino": resuelto,
        "huella_candidato": huella_despues,
        "huella_vecino": huella_antes,
        "senales": {},
        "levantada_por": ["correccion declarada"],
        "veredicto": "CORREGIDO",
        "razon": razon,
        "campo": CAMPO_UNICO,
        "caracteres_antes": len(viejo),
        "caracteres_despues": len(nuevo),
        "texto_anadido": anade,
        "operacion": "correccion declarada del resumen_teorico (EXTRACTOR.md 2)",
    }
    comun.escribir_jsonl(ruta_dataset, futuro)
    comun.agregar_jsonl(ruta_veredictos, registro)

    resultado.registro = registro
    resultado.decir("  el texto viejo SIGUE ENTERO: %d caracteres, ninguno borrado"
                    % len(viejo))
    resultado.decir("  se aniaden %d caracteres al final" % (len(nuevo) - len(viejo)))
    resultado.decir("  huella antes  : %s" % huella_antes)
    resultado.decir("  huella despues: %s" % huella_despues)
    resultado.decir("")
    resultado.decir("GATE VERDE sobre la simulacion. CORRECCION ESCRITA EN: %s" % resuelto)
    resultado.decir("  razon en %s" % comun.relativa(ruta_veredictos))
    return resultado


def main(argumentos=None):
    comun.salida_utf8()
    argumentos = list(argumentos or [])
    valores = {"--nodo": None, "--anade": None, "--razon": None, "--campo": None}
    indice = 0
    while indice < len(argumentos):
        clave = argumentos[indice]
        if clave in valores:
            indice += 1
            if indice >= len(argumentos):
                print("falta el valor de %s" % clave)
                return CODIGO_RECHAZO
            valores[clave] = argumentos[indice]
        else:
            print("opcion desconocida: %s" % clave)
            return CODIGO_RECHAZO
        indice += 1

    if not (valores["--nodo"] and valores["--anade"] and valores["--razon"]):
        print('uso: python forja.py corregir --nodo <id> '
              '--anade "CORRECCION DECLARADA ..." --razon "que era falso"')
        print("")
        print("  SOLO toca resumen_teorico, SOLO aniade al final, y NO borra nada.")
        print("  --anade tiene que empezar por '%s'." % MARCA)
        return CODIGO_RECHAZO

    resultado = corregir(valores["--nodo"], valores["--anade"], valores["--razon"],
                         campo=valores["--campo"])
    print(resultado.texto())
    return resultado.codigo
