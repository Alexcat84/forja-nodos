# -*- coding: utf-8 -*-
"""LA OPERACION DE ANOTAR UNA LINEA YA ESCRITA DE LA BITACORA.

    python forja.py anotar --linea <n> --anade "CORRECCION DECLARADA ..." --razon "..."
    python forja.py anotar --linea <n> --anade "..." --razon "..." --no-consumada

PARA QUE EXISTE. `EXTRACTOR.md` 14 pone `bitacora/` bajo la aduana y **prohibe
tocarla a mano**; el manual, principio 6, manda **corregir sin borrar**. Entre
esas dos cosas quedaba un hueco: **una linea ya escrita que hay que marcar no
tenia via.** La `ACTA 27` `5.2` lo encargo con estas palabras: *se marcan por
operacion, con su razon, igual que hiciste con `corregir`*.

LOS DOS CASOS QUE LA HICIERON FALTA, y los dos estan contados:

  - **LAS CUATRO LINEAS FANTASMA**, `248` a `251` de `bitacora/VEREDICTOS.jsonl`
    (`ACTA 27` `5.2`). Las escribio una corrida que imprimio `RECHAZADO` y no
    inserto nada, cuando `agregar_jsonl` vivia dentro del bucle por vecino. **No
    se borran: se declaran NO CONSUMADAS.**
  - **LA PREMISA FALSA DE LA LINEA `256`** (`ACTA 27` `2.1` y `6.4`). Su razon
    escribe *la misma etapa de persuadir* y sus dos nodos declaran `CLARIFY` y
    `PERSUADE`. **La clase es correcta y no se toca**: lo que se corrige es la
    premisa, por correccion declarada.
  - **LOS `26` `RANCIO` DE LAS CUATRO CORRECCIONES** (`ACTA 27` `5.3.b`). `D.15`
    da dos salidas y la segunda es **declarar por que la lectura sigue valiendo**.
    La declaracion va en sede duradera y dice **contra que huella se emitio**, que
    es lo que hace `--anade "VIGENCIA DECLARADA ..."`.

LO QUE HACE, Y SOLO ESO:

  - **ANIADE AL FINAL DE LA RAZON. NO BORRA NI SUSTITUYE NADA.** El texto viejo
    se comprueba entero despues de escribir, no se promete.
  - **DEJA LA ANOTACION TAMBIEN EN SU PROPIO CAMPO**, `anotaciones`, con fecha y
    razon. Quien lea la linea maniana ve la marca sin tener que leerse la razon
    entera.
  - **CON `--no-consumada` MARCA LA LINEA COMO NO CONSUMADA**, que es decir que
    la corrida que la escribio **no inserto nada**. El bloque de vigencia deja de
    pedirle huella: **una lectura que nunca se consumo no es una lectura que
    envejecio**.
  - **NO TOCA NI LA CLASE, NI EL CANDIDATO, NI EL VECINO, NI LAS HUELLAS, NI LAS
    SEÑALES, NI EL CAMPO `arista`.** Cambiar un veredicto es volver a juzgar, y
    eso se hace leyendo el par, no anotando una linea.
  - **NO TOCA `dataset/nodos.jsonl`.** Esta operacion no mueve ni un nodo.

LO QUE EXIGE, Y NO ES NEGOCIABLE:

  --anade   TIENE QUE EMPEZAR POR `CORRECCION DECLARADA` o por `VIGENCIA
            DECLARADA`, segun cual de los dos actos sea. Es el mismo remedio
            mecanico de `D.35` que ya lleva `corregir`: **un remedio que se cumple
            acordandose no es un remedio.**
  --razon   la razon escrita. Una anotacion sin razon escrita es una edicion a
            mano con otro nombre (`D.8` aplicado a su propia sede).
"""

from . import aduana
from . import comun

CODIGO_OK = 0
CODIGO_RECHAZO = 1

# LAS DOS MARCAS, Y SON DOS PORQUE SON DOS ACTOS DISTINTOS. `D.35` pide que la
# primera palabra diga al lector que ese tramo es una declaracion; lo que no pide
# es llamar CORRECCION a algo que no corrige nada.
#
#   CORRECCION DECLARADA  algo de esa linea estaba mal y aqui se dice que hay en
#                         su lugar. El texto viejo se queda.
#   VIGENCIA DECLARADA    la lectura de esa linea SIGUE VALIENDO aunque su huella
#                         haya cambiado, y aqui se dice contra que huella se
#                         emitio y por que el cambio no la invalida. Es la SEGUNDA
#                         SALIDA de `D.15`, escrita con estas palabras: *se relee
#                         con el texto de hoy, o se declara por que sigue
#                         valiendo.*
#
# Y LA DECLARACION NO BORRA EL HALLAZGO: la linea sigue saliendo `RANCIO` en
# `forja.py rancios`. Cambiar lo que la guarda considera rancio seria mover la
# vara de `D.15`, y eso se propone a Alexis, no se hace en una vuelta.
MARCA = "CORRECCION DECLARADA"
MARCA_VIGENCIA = "VIGENCIA DECLARADA"
MARCAS = (MARCA, MARCA_VIGENCIA)
MINIMO_TEXTO = 40

# LOS CAMPOS QUE ESTA OPERACION NO PUEDE MOVER. Van escritos aqui y comprobados
# despues de construir la linea nueva, para que la prohibicion sea una medida y
# no un comentario.
CAMPOS_INTOCABLES = ("candidato", "vecino", "veredicto", "arista", "fecha",
                     "huella_candidato", "huella_vecino", "senales",
                     "levantada_por", "detalle_paso")


class Resultado(object):

    def __init__(self):
        self.codigo = CODIGO_OK
        self.lineas = []
        self.registro = None

    def decir(self, linea=""):
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


def anotar(numero, anade, razon, no_consumada=False, ruta_veredictos=None):
    """Anota una linea de la bitacora. Devuelve un Resultado."""
    ruta_veredictos = ruta_veredictos or comun.RUTA_VEREDICTOS
    resultado = Resultado()
    anade = (anade or "").strip()
    razon = (razon or "").strip()

    resultado.decir("ANOTACION DECLARADA SOBRE UNA LINEA YA ESCRITA DE LA BITACORA")
    resultado.decir("  sede : %s" % comun.relativa(ruta_veredictos))
    resultado.decir("  linea: %s" % numero)

    try:
        numero = int(numero)
    except (TypeError, ValueError):
        return resultado.rechazar(
            "--linea no es un numero de linea",
            ["llego: %r" % (numero,)])

    if not razon:
        return resultado.rechazar(
            "la anotacion va sin razon escrita",
            ["Di QUE ESTABA MAL en esa linea y CON QUE MEDICION lo sabes.",
             "Una anotacion sin razon escrita es una edicion a mano con otro nombre."])

    if not anade:
        return resultado.rechazar(
            "no hay texto que aniadir",
            ["--anade lleva el texto de la correccion declarada."])

    if not any(anade.startswith(marca) for marca in MARCAS):
        return resultado.rechazar(
            "el texto aniadido no se declara como lo que es",
            ["--anade tiene que EMPEZAR por una de estas dos: %s."
             % " o ".join("'%s'" % m for m in MARCAS),
             "Es el remedio mecanico de D.35. Quien lea la linea maniana tiene que",
             "ver en la primera palabra si ese tramo CORRIGE lo anterior o si",
             "DECLARA por que una lectura con la huella cambiada sigue valiendo.",
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

    filas = comun.leer_jsonl(ruta_veredictos)
    if not 1 <= numero <= len(filas):
        return resultado.rechazar(
            "esa linea no existe",
            ["%s tiene %d linea(s) y llego la %d."
             % (comun.relativa(ruta_veredictos), len(filas), numero),
             "La linea se cuenta desde 1, como la cuenta el bloque de vigencia."])

    vieja = filas[numero - 1]
    razon_vieja = vieja.get("razon") or ""

    if anade in razon_vieja:
        return resultado.rechazar(
            "esa misma anotacion ya esta escrita en la linea",
            ["El texto de --anade ya figura literal en la razon de la linea %d."
             % numero,
             "Una correccion no se declara dos veces."])

    fecha = aduana._hoy()
    nueva = dict(vieja)
    nueva["razon"] = (razon_vieja + " " + anade).strip() if razon_vieja else anade
    anotaciones = list(nueva.get("anotaciones") or [])
    anotaciones.append({"fecha": fecha, "texto": anade, "razon": razon,
                        "no_consumada": bool(no_consumada)})
    nueva["anotaciones"] = anotaciones
    if no_consumada:
        nueva["consumada"] = False

    # LA RAZON VIEJA SOBREVIVE ENTERA, y se comprueba en vez de prometerse.
    if razon_vieja and razon_vieja not in nueva["razon"]:
        return resultado.rechazar(
            "la anotacion habria borrado texto de la razon",
            ["Esta operacion SOLO aniade. Si esto salta, es un fallo del codigo",
             "y no del que lo llamo."])

    # NINGUN CAMPO DE VEREDICTO SE MUEVE. Medido, no comentado.
    movidos = [campo for campo in CAMPOS_INTOCABLES
               if vieja.get(campo) != nueva.get(campo)]
    if movidos:
        return resultado.rechazar(
            "la anotacion habria movido campos que no le tocan",
            ["campos movidos: %s" % ", ".join(movidos),
             "Cambiar un veredicto es volver a juzgar el par, no anotar su linea."])

    # NINGUNA OTRA LINEA SE TOCA. La bitacora se reescribe entera porque es un
    # JSONL, asi que la prueba de que solo cambio una es una medida.
    futuro = [dict(f) for f in filas]
    futuro[numero - 1] = nueva
    distintas = [i + 1 for i, (a, b) in enumerate(zip(filas, futuro)) if a != b]
    if distintas != [numero]:
        return resultado.rechazar(
            "la escritura habria tocado mas de una linea",
            ["lineas distintas: %s" % distintas])

    comun.escribir_jsonl(ruta_veredictos, futuro)

    resultado.registro = nueva
    resultado.decir("  veredicto: %s (NO se toca)" % vieja.get("veredicto"))
    resultado.decir("  par      : %s contra %s"
                    % (vieja.get("candidato"), vieja.get("vecino")))
    resultado.decir("  la razon vieja SIGUE ENTERA: %d caracteres, ninguno borrado"
                    % len(razon_vieja))
    resultado.decir("  se aniaden %d caracteres al final de la razon"
                    % (len(nueva["razon"]) - len(razon_vieja)))
    if no_consumada:
        resultado.decir("  la linea queda declarada NO CONSUMADA: la corrida que la")
        resultado.decir("  escribio no inserto nada, asi que la vigencia deja de pedirle")
        resultado.decir("  huella (D.15 no mide lecturas que nunca se consumaron).")
    resultado.decir("  lineas de la bitacora tocadas: 1 (la %d). Las otras %d, intactas."
                    % (numero, len(filas) - 1))
    resultado.decir("")
    resultado.decir("ANOTACION ESCRITA en %s, linea %d."
                    % (comun.relativa(ruta_veredictos), numero))
    return resultado


def main(argumentos=None):
    comun.salida_utf8()
    argumentos = list(argumentos or [])
    valores = {"--linea": None, "--anade": None, "--razon": None}
    no_consumada = False
    indice = 0
    while indice < len(argumentos):
        clave = argumentos[indice]
        if clave == "--no-consumada":
            no_consumada = True
        elif clave in valores:
            indice += 1
            if indice >= len(argumentos):
                print("falta el valor de %s" % clave)
                return CODIGO_RECHAZO
            valores[clave] = argumentos[indice]
        else:
            print("opcion desconocida: %s" % clave)
            return CODIGO_RECHAZO
        indice += 1

    if not (valores["--linea"] and valores["--anade"] and valores["--razon"]):
        print('uso: python forja.py anotar --linea <n> '
              '--anade "CORRECCION DECLARADA ..." --razon "que estaba mal" '
              "[--no-consumada]")
        print("")
        print("  SOLO toca la razon de esa linea, SOLO aniade al final, y NO borra nada.")
        print("  --anade tiene que empezar por %s."
              % " o por ".join("'%s'" % m for m in MARCAS))
        print("  --no-consumada declara que la corrida que escribio esa linea no inserto.")
        return CODIGO_RECHAZO

    resultado = anotar(valores["--linea"], valores["--anade"], valores["--razon"],
                       no_consumada=no_consumada)
    print(resultado.texto())
    return resultado.codigo
