# -*- coding: utf-8 -*-
"""LA SUSTITUCION DECLARADA DE UN FRAGMENTO DE UN NODO YA INSERTADO.

    python forja.py sustituir --nodo <id> --campo <campo> [--indice N]
                              --viejo "fragmento exacto" --nuevo "texto" (o "")
                              --regla "la regla que lo pide" --razon "que incumple y con que lo sabes"
                              --decision "la decision del fundador que lo ordena"

POR QUE EXISTE. Esta casa tiene dos vias sobre un nodo ya insertado, y ninguna sirve para esto:
  - `corregir` (src/correccion.py) solo ANIADE al `resumen_teorico`: es la regla para una frase falsa, el texto viejo
    se queda y debajo se declara que estaba mal;
  - `scripts/retirar_paso.py` (D.54) saca un PASO ENTERO de `pasos_accionables`.
Ninguna quita un fragmento de dentro de un paso o de un resumen. El fundador lo ordeno por su decision del 26 sep 2026
(archivada en docs/loop/paradas/2026-09-26-cierre-de-la-forja-DECISION.md), antes de fundir el mundo 11, con la
politica marco contra pais de My-idea: la CIFRA DE MERCADO sale (una cifra que sigue escrita no ha salido, por mucho
que debajo se declare que no vale) y el EMPLEO va como METODO (un paso que manda como universal la lista de un pais la
sigue mandando aunque el resumen avise). `EXTRACTOR.md` 2 dice como nace una via asi: una operacion escrita, con su
simulacion y su caso positivo, no una edicion a mano.

LO QUE HACE, Y SOLO ESO:
  - SUSTITUYE UN FRAGMENTO EXACTO que aparece UNA sola vez en el campo (o en el paso `--indice`) por el texto nuevo, o
    lo quita con `--nuevo ""`. El resto del campo queda byte a byte: no normaliza espacios, y si la costura dejaria un
    espacio doble o un borde con espacio, rechaza (el fragmento se da con sus espacios).
  - SOLO campos de contenido: resumen_teorico, pasos_accionables, condiciones_activacion, entregable_esperado,
    escala_minima y marco_pais. El id, el titulo, las fuentes y las aristas no se tocan por aqui; un paso entero sale
    por `retirar_paso.py`, y por eso aqui un campo o un paso no puede quedar vacio.
  - SOLO POR DECISION ESCRITA DEL FUNDADOR (`--decision`), con la regla que lo pide y la razon.
  - DEJA RASTRO EN EL PROPIO NODO: aniade al `resumen_teorico` una CORRECCION DECLARADA que dice que campo se sustituyo,
    por que regla y donde queda el texto anterior, sin repetir lo que salio (D.35: la marca la pone la operacion, no la
    memoria de quien la corre). El texto anterior queda LITERAL y entero en la bitacora, con el fragmento viejo y el
    nuevo, la regla, la razon, la decision y la huella del nodo antes y despues.
  - ESCRIBE BAJO CERROJO (D.44), y dentro de el lee, simula sobre copia en memoria y pasa el gate antes de escribir. Si
    la copia futura no pasa, no se escribe nada.
"""

from . import aduana
from . import cerrojo
from . import comun
from . import config as modulo_config
from . import gate
from . import reglas_id
from .resolutor import Resolutor

CODIGO_OK = 0
CODIGO_RECHAZO = 1
CAMPOS = ("resumen_teorico", "pasos_accionables", "condiciones_activacion", "entregable_esperado", "escala_minima",
          "marco_pais")
MINIMO_RAZON = 20
MARCA = "CORRECCION DECLARADA"


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


def _fecha_legible(iso):
    meses = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
    try:
        a, m, d = iso.split("-")
        return "%d %s %s" % (int(d), meses[int(m) - 1], a)
    except (ValueError, IndexError):
        return iso


def marca_de(campo, indice, regla, fecha):
    donde = "%s, paso %d" % (campo, indice + 1) if indice is not None else campo
    return ("%s (%s, %s): el campo %s se sustituyo por decision del fundador; el texto anterior queda literal en "
            "bitacora/VEREDICTOS.jsonl." % (MARCA, _fecha_legible(fecha), regla, donde))


def sustituir(nodo_id, campo, viejo, nuevo, regla, razon, decision, indice=None, ruta_dataset=None,
              ruta_veredictos=None, ruta_pares_mutuos=None):
    ruta_dataset = ruta_dataset or comun.RUTA_DATASET
    ruta_veredictos = ruta_veredictos or comun.RUTA_VEREDICTOS
    resultado = Resultado()
    nodo_id = reglas_id.normalizar(nodo_id or "")
    viejo = viejo or ""
    nuevo = nuevo or ""
    regla = (regla or "").strip()
    razon = (razon or "").strip()
    decision = (decision or "").strip()

    resultado.decir("SUSTITUCION DECLARADA SOBRE UN NODO YA INSERTADO")
    resultado.decir("  nodo : %s" % nodo_id)
    resultado.decir("  campo: %s%s" % (campo, "" if indice is None else "[%d]" % indice))

    if campo not in CAMPOS:
        return resultado.rechazar(
            "el campo '%s' no se sustituye por aqui" % campo,
            ["Solo los campos de contenido: %s." % ", ".join(CAMPOS),
             "El id, el titulo, las fuentes y las aristas tienen su propia via."])
    if len(razon) < MINIMO_RAZON:
        return resultado.rechazar("la sustitucion va sin razon escrita",
                                  ["Di QUE incumple y con que lo sabes (%d caracteres como minimo)." % MINIMO_RAZON])
    if not regla:
        return resultado.rechazar("la sustitucion no nombra la regla que la pide",
                                  ["--regla va en la marca que queda en el nodo."])
    if not decision:
        return resultado.rechazar(
            "la sustitucion va sin decision del fundador",
            ["Esta operacion quita un fragmento del nodo (lo guarda la bitacora). Solo corre por",
             "una decision escrita del fundador: --decision la cita."])
    if not viejo.strip():
        return resultado.rechazar("no hay fragmento que sustituir", ["--viejo lleva el fragmento exacto."])
    hallazgos = comun.buscar_guiones(nuevo) + comun.buscar_guiones(razon) + comun.buscar_guiones(regla)
    if hallazgos:
        return resultado.rechazar("el texto nuevo, la regla o la razon traen guiones largos o medios",
                                  [str(h) for h in hallazgos[:5]])

    with cerrojo.tomar(ruta_dataset, avisar=lambda m: resultado.decir("  " + m)):
        nodos = comun.leer_jsonl(ruta_dataset)
        resuelto = Resolutor(nodos).resolver(nodo_id)
        if resuelto is None:
            return resultado.rechazar("'%s' no vive en el grafo" % nodo_id,
                                      ["Esta operacion sustituye en nodos YA INSERTADOS."])
        por_id = dict((n["id"], n) for n in nodos if n.get("id"))
        nodo = por_id[resuelto]
        valor = nodo.get(campo)
        if isinstance(valor, list):
            if indice is None or not 0 <= indice < len(valor):
                return resultado.rechazar("el campo es una lista y falta un --indice valido",
                                          ["'%s' tiene %d elementos." % (campo, len(valor))])
            antes = valor[indice]
        else:
            if indice is not None:
                return resultado.rechazar("el campo no es una lista: sobra --indice", [])
            antes = valor or ""
        veces = antes.count(viejo)
        if veces != 1:
            return resultado.rechazar(
                "el fragmento aparece %d veces en el campo, y tiene que aparecer una" % veces,
                ["Un fragmento que no esta no se sustituye, y uno repetido es ambiguo.",
                 "fragmento: %r" % viejo[:120]])
        despues = antes.replace(viejo, nuevo)
        if not despues.strip():
            return resultado.rechazar("la sustitucion dejaria el campo o el paso vacio",
                                      ["Un paso entero sale por scripts/retirar_paso.py (D.54)."])
        if despues.count("  ") > antes.count("  ") or (despues != despues.strip() and antes == antes.strip()):
            return resultado.rechazar("la costura dejaria un espacio doble o un borde con espacio",
                                      ["Da el fragmento con sus espacios: el resto del campo no se toca."])

        fecha = aduana._hoy()
        marca = marca_de(campo, indice, regla, fecha)
        huella_antes = comun.huella_de_nodo(nodo)
        futuro = [dict(n) for n in nodos]
        futuro_por_id = dict((n["id"], n) for n in futuro if n.get("id"))
        objetivo = futuro_por_id[resuelto]
        if isinstance(valor, list):
            lista = list(valor)
            lista[indice] = despues
            objetivo[campo] = lista
        else:
            objetivo[campo] = despues
        resumen = objetivo.get("resumen_teorico") or ""
        objetivo["resumen_teorico"] = (resumen.rstrip() + " " + marca).strip()
        fallos = gate.verificar(futuro, pares_mutuos=modulo_config.cargar_pares_mutuos(ruta_pares_mutuos))
        if fallos:
            resultado.codigo = CODIGO_RECHAZO
            resultado.decir("")
            resultado.decir("RECHAZADO POR EL GATE en la simulacion sobre copia en memoria.")
            resultado.decir("  NADA SE ESCRIBIO.")
            for fallo in fallos[:10]:
                resultado.decir("  %s" % fallo)
            return resultado
        huella_despues = comun.huella_de_nodo(objetivo)
        registro = {
            "fecha": fecha,
            "candidato": resuelto,
            "vecino": resuelto,
            "huella_candidato": huella_despues,
            "huella_vecino": huella_antes,
            "senales": {},
            "levantada_por": ["sustitucion declarada"],
            "veredicto": "SUSTITUIDO",
            "regla": regla,
            "razon": razon,
            "decision": decision,
            "campo": campo,
            "indice": indice,
            "fragmento_viejo": viejo,
            "fragmento_nuevo": nuevo,
            "texto_anterior": antes,
            "texto_nuevo": despues,
            "marca_en_el_nodo": marca,
            "operacion": "sustitucion declarada de un fragmento (src/sustitucion.py)",
        }
        comun.escribir_jsonl(ruta_dataset, futuro)
        comun.agregar_jsonl(ruta_veredictos, registro)
    resultado.registro = registro
    resultado.decir("  el texto anterior queda LITERAL en %s" % comun.relativa(ruta_veredictos))
    resultado.decir("  marca en el nodo: %s" % marca)
    resultado.decir("  huella antes  : %s" % huella_antes)
    resultado.decir("  huella despues: %s" % huella_despues)
    resultado.decir("")
    resultado.decir("GATE VERDE sobre la simulacion. SUSTITUCION ESCRITA EN: %s" % resuelto)
    return resultado


def main(argumentos=None):
    comun.salida_utf8()
    argumentos = list(argumentos or [])
    valores = {"--nodo": None, "--campo": None, "--indice": None, "--viejo": None, "--nuevo": None,
               "--regla": None, "--razon": None, "--decision": None}
    i = 0
    while i < len(argumentos):
        clave = argumentos[i]
        if clave not in valores:
            print("opcion desconocida: %s" % clave)
            return CODIGO_RECHAZO
        i += 1
        if i >= len(argumentos):
            print("falta el valor de %s" % clave)
            return CODIGO_RECHAZO
        valores[clave] = argumentos[i]
        i += 1
    if not (valores["--nodo"] and valores["--campo"] and valores["--viejo"] is not None and valores["--nuevo"] is not None):
        print('uso: python forja.py sustituir --nodo <id> --campo <campo> [--indice N] --viejo "..." '
              '--nuevo "..." --regla "..." --razon "..." --decision "..."')
        return CODIGO_RECHAZO
    indice = None
    if valores["--indice"] is not None:
        try:
            indice = int(valores["--indice"])
        except ValueError:
            print("--indice tiene que ser un numero")
            return CODIGO_RECHAZO
    resultado = sustituir(valores["--nodo"], valores["--campo"], valores["--viejo"], valores["--nuevo"],
                          valores["--regla"], valores["--razon"], valores["--decision"], indice=indice)
    print(resultado.texto())
    return resultado.codigo
