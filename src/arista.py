# -*- coding: utf-8 -*-
"""LA OPERACION DE DECLARAR UNA ARISTA POR LECTURA (D.37).

    python forja.py arista --madre <id> --hijo <id> --paso <n> --razon "..."

PARA QUE EXISTE. La aduana cablea la arista madre e hijo EN EL ACTO DE INSERTAR,
y solo cuando alguien escribe un veredicto sobre un vecino. Para dos nodos que YA
viven en el grafo no habia camino: `insertar` los rechaza por `el id ya vive`, y
**escribir a mano en `dataset/nodos.jsonl` esta prohibido, siempre**
(`EXTRACTOR.md` seccion 2).

`D.37` manda declarar la arista cabeza a parte cuando el titulo o el texto de un
nodo ENUMERA sus partes y esas partes existen como nodos. Sobre lo ya insertado,
eso no se podia hacer. **Esto es esa via, y es una OPERACION: con su simulacion
sobre copia en memoria antes de escribir, y su caso positivo** (manual seccion 5).

LO QUE EXIGE, Y NO ES NEGOCIABLE:

  --paso <n>   EL NUMERO DEL PASO DE LA MADRE QUE ENUMERA LA PARTE. No es un
               adorno: es lo que hace la arista VERIFICABLE. El auditor abre el
               paso n de la madre y comprueba que ahi se nombra al hijo, igual
               que comprueba las dos lineas de un MUTUO (adjudicacion A.4). Una
               arista sin su linea es una afirmacion sin cita.
  --razon      la razon escrita, que va a la bitacora. Sin ella no se escribe
               nada: es el activo mas reutilizable del sistema (manual seccion 2).

LO QUE NO HACE. No juzga si el par es madre e hijo: eso lo decide la lectura de
una persona, y su razon queda escrita. Esta operacion comprueba la FORMA (que los
dos vivan, que el paso exista, que no haya vuelta ni duplicado) y deja que el
gate diga la ultima palabra sobre la copia en memoria.

LAS SEÑALES SE MIDEN Y SE GUARDAN AUNQUE NO LEVANTEN. Es la prueba de que la
arista la vio un lector y no el instrumento (`D.19`, `D.29`): la bitacora guarda
`levantada_por` con el valor `lectura declarada` y los tres numeros reales al
lado.
"""

import sys

from . import aduana
from . import comun
from . import config as modulo_config
from . import gate
from . import reglas_id
from .resolutor import Resolutor

CODIGO_OK = 0
CODIGO_RECHAZO = 1

LEVANTADA_POR_LECTURA = "lectura declarada"


class Resultado(object):

    def __init__(self):
        self.codigo = CODIGO_OK
        self.lineas = []
        self.arista = ""
        self.registro = None

    def decir(self, linea):
        self.lineas.append(linea)

    def rechazar(self, titulo, detalles):
        self.codigo = CODIGO_RECHAZO
        self.decir("")
        self.decir("RECHAZADO: %s" % titulo)
        for detalle in detalles:
            self.decir("  " + detalle)
        return self

    def texto(self):
        return "\n".join(self.lineas)


def declarar(madre_id, hijo_id, paso, razon, ruta_dataset=None,
             ruta_veredictos=None, umbrales=None, ruta_pares_mutuos=None):
    """Declara la arista y la escribe. Devuelve un Resultado."""
    ruta_dataset = ruta_dataset or comun.RUTA_DATASET
    ruta_veredictos = ruta_veredictos or comun.RUTA_VEREDICTOS
    umbrales = umbrales or modulo_config.cargar()
    resultado = Resultado()

    madre_id = reglas_id.normalizar(madre_id or "")
    hijo_id = reglas_id.normalizar(hijo_id or "")
    razon = (razon or "").strip()

    resultado.decir("DECLARACION DE ARISTA POR LECTURA (D.37)")
    resultado.decir("  madre: %s" % madre_id)
    resultado.decir("  hijo : %s" % hijo_id)

    if not razon:
        return resultado.rechazar(
            "la declaracion va sin razon escrita",
            ["La razon escrita es el activo mas reutilizable del sistema entero "
             "(manual seccion 2).",
             "Di QUE AÑADE EL HIJO A LA MADRE, no que se parecen."])

    nodos = comun.leer_jsonl(ruta_dataset)
    resolutor = Resolutor(nodos)
    madre = resolutor.resolver(madre_id)
    hijo = resolutor.resolver(hijo_id)

    for etiqueta, pedido, resuelto in (("madre", madre_id, madre),
                                       ("hijo", hijo_id, hijo)):
        if resuelto is None:
            return resultado.rechazar(
                "la %s '%s' no vive en el grafo" % (etiqueta, pedido),
                ["Una arista se cablea contra ids que YA existen.",
                 "Si todavia esta en cuarentena, entra por la aduana y declara "
                 "la arista en el acto de insertarla."])
    if madre == hijo:
        return resultado.rechazar(
            "auto arista: la madre y el hijo son el mismo nodo",
            ["'%s' y '%s' resuelven los dos a '%s'." % (madre_id, hijo_id, madre)])

    por_id = dict((n["id"], n) for n in nodos if n.get("id"))
    nodo_madre, nodo_hijo = por_id[madre], por_id[hijo]

    # EL PASO CITADO ES LO QUE HACE LA ARISTA VERIFICABLE.
    pasos = nodo_madre.get("pasos_accionables") or []
    if not isinstance(paso, int) or not 1 <= paso <= len(pasos):
        return resultado.rechazar(
            "el paso citado no existe en la madre",
            ["se cito el paso %r y '%s' tiene %d paso(s)" % (paso, madre, len(pasos)),
             "El paso citado es EL DE LA MADRE: la linea que enumera la parte."])
    texto_citado = pasos[paso - 1]

    ya = resolutor.resolver_lista(list(nodo_madre.get("nodos_siguientes") or []))
    if hijo in ya:
        return resultado.rechazar(
            "esa arista ya esta declarada",
            ["'%s' ya figura en nodos_siguientes de '%s'." % (hijo, madre),
             "Una arista no se declara dos veces: si la razon nueva es mejor, "
             "eso es una correccion declarada y no una segunda arista."])

    # LAS TRES SEÑALES, MEDIDAS AUNQUE NO LEVANTEN. Es la prueba de D.19.
    medicion = aduana.medir(nodo_hijo, nodo_madre, umbrales)
    resultado.decir("  paso citado de la madre: %d" % paso)
    resultado.decir("    %s" % texto_citado[:150])
    resultado.decir("  señales del par: %s"
                    % ", ".join("%s %s" % (nombre, valor)
                                for nombre, valor in sorted(medicion["senales"].items())))
    if medicion["levantada_por"]:
        resultado.decir("    levantada tambien por la señal: %s"
                        % ", ".join(medicion["levantada_por"]))
    else:
        resultado.decir("    NINGUNA SEÑAL LA LEVANTA. La caza la lectura (D.19, D.29).")

    # LA SIMULACION, sobre copia en memoria y antes de escribir nada.
    futuro = [dict(n) for n in nodos]
    futuro_por_id = dict((n["id"], n) for n in futuro if n.get("id"))
    resolutor_futuro = Resolutor(futuro)
    siguientes = list(futuro_por_id[madre].get("nodos_siguientes") or [])
    siguientes.append(hijo)
    futuro_por_id[madre]["nodos_siguientes"] = resolutor_futuro.resolver_lista(siguientes)
    previos = list(futuro_por_id[hijo].get("nodos_previos") or [])
    previos.append(madre)
    futuro_por_id[hijo]["nodos_previos"] = resolutor_futuro.resolver_lista(previos)

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

    fecha = aduana._hoy()
    registro = {
        "fecha": fecha,
        "candidato": hijo,
        "vecino": madre,
        "huella_candidato": comun.huella_de_nodo(nodo_hijo),
        "huella_vecino": comun.huella_de_nodo(nodo_madre),
        "senales": medicion["senales"],
        "levantada_por": [LEVANTADA_POR_LECTURA],
        "detalle_paso": medicion["detalle_paso"],
        "veredicto": "CONTINUA",
        "razon": razon,
        "arista": "%s > %s" % (madre, hijo),
        "paso_citado": paso,
        "texto_citado": texto_citado,
        "operacion": "arista declarada por lectura (D.37)",
    }
    comun.escribir_jsonl(ruta_dataset, futuro)
    comun.agregar_jsonl(ruta_veredictos, registro)
    resultado.arista = "%s > %s" % (madre, hijo)
    resultado.registro = registro
    resultado.decir("")
    resultado.decir("GATE VERDE sobre la simulacion. ARISTA ESCRITA RESUELTA: %s > %s"
                    % (madre, hijo))
    resultado.decir("  razon en %s" % comun.relativa(ruta_veredictos))
    return resultado


def main(argumentos=None):
    comun.salida_utf8()
    argumentos = list(argumentos or [])
    valores = {"--madre": None, "--hijo": None, "--paso": None, "--razon": None}
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

    if not all(valores.values()):
        print('uso: python forja.py arista --madre <id> --hijo <id> --paso <n> '
              '--razon "que añade el hijo a la madre"')
        print("")
        print("  --paso es EL PASO DE LA MADRE que enumera la parte. Es lo que")
        print("  hace la arista verificable: el auditor lo abre y comprueba que")
        print("  ahi se nombra al hijo. Una arista sin su linea es una")
        print("  afirmacion sin cita (D.37).")
        return CODIGO_RECHAZO

    try:
        paso = int(valores["--paso"])
    except ValueError:
        print("--paso ha de ser un numero: llego %r" % valores["--paso"])
        return CODIGO_RECHAZO

    resultado = declarar(valores["--madre"], valores["--hijo"], paso,
                         valores["--razon"])
    print(resultado.texto())
    return resultado.codigo
