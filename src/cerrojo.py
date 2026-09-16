# -*- coding: utf-8 -*-
"""EL CERROJO DE INSERCION: UNA SOLA CORRIDA ESCRIBE EL DATASET A LA VEZ.

`EXTRACTOR.md` 2 manda **un candidato por vez** desde que existe. Hasta hoy esa
regla **la cumplia el que teclea, no el codigo**, y es la tercera vez que esta casa
descubre la misma figura: una regla escrita que no llego a `src/` (`D.29` a la
aduana, `D.38.5` a la aduana, y esta).

LA CAIDA QUE LA OBLIGO, medida por el extractor de la vuelta 28 y contada por el
en `V.5.e` antes de arreglarla:

    mande a insertar `crear_espacio_seguro_madurar_ideas_nuevas` y, mientras
    seguia corriendo, mande `crear_obligacion_disentir_equipo`. El segundo termino
    antes y escribio su nodo. El primero habia leido el dataset ANTES de eso, y al
    escribir su propia copia en memoria dejo fuera el nodo del segundo.

**UN NODO ENTRO Y DESAPARECIO, Y EL `gate` SALIO VERDE ENCIMA**: un grafo al que le
quitan un nodo entero sigue siendo coherente, solo que mas pequenio. **Ninguna de
las doce guardas lo veia.**

COMO FUNCIONA, Y POR QUE ASI. Un fichero de cerrojo creado con `O_EXCL`, que es
atomico en todos los sistemas donde corre esta casa. Quien no lo consigue **espera
y reintenta**; no pisa, no falla en silencio, y **no se salta el turno de nadie**.

    with cerrojo.tomar(ruta_dataset):
        nodos = leer(...)
        ...
        escribir(...)

EL CERROJO GUARDA QUIEN LO TIENE Y DESDE CUANDO, y por eso puede distinguir un
proceso vivo de un cadaver. **Un cerrojo huerfano de un proceso que murio no
bloquea la casa para siempre**: se declara, se rompe y se dice en voz alta. Lo que
NO se hace nunca es romperlo en silencio.
"""

import errno
import io
import json
import os
import time

ESPERA = 0.25                # segundos entre intentos
TOPE_DE_ESPERA = 120.0       # un minuto no basta: la aduana mide minutos por candidato
TOPE_DE_HUERFANO = 900.0     # 15 min sin que su proceso exista: se declara y se rompe


class CerrojoOcupado(Exception):
    """Nadie escribe el dataset mientras otro lo escribe."""


def ruta_de(ruta_dataset):
    return ruta_dataset + ".cerrojo"


def _dueno(ruta):
    try:
        return json.loads(io.open(ruta, encoding="utf-8").read())
    except Exception:
        return {}


def _vive(pid):
    """True / False / None (no se puede saber en este sistema).

    ANTE LA DUDA NO SE ROMPE POR EL PID: decir que si de mas solo cuesta una
    espera; decir que no de mas rompe un cerrojo vivo, **que es justo la caida que
    este fichero existe para impedir.** Por eso la duda se devuelve como duda y la
    resuelve la EDAD, no una adivinanza.
    """
    if not pid:
        return None
    try:
        os.kill(int(pid), 0)
        return True
    except OSError as error:
        if error.errno == errno.ESRCH:
            return False
        if error.errno == errno.EPERM:
            return True          # existe y es de otro usuario
        return None              # Windows no contesta a esto: es duda, no un no
    except Exception:
        return None


class tomar(object):
    """Contexto que toma el cerrojo del dataset y lo suelta pase lo que pase."""

    def __init__(self, ruta_dataset, espera=None, tope=None, avisar=None):
        self.ruta = ruta_de(ruta_dataset)
        self.espera = ESPERA if espera is None else espera
        self.tope = TOPE_DE_ESPERA if tope is None else tope
        self.avisar = avisar or (lambda mensaje: None)
        self.mio = False

    def _intentar(self):
        descriptor = os.open(self.ruta, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        with os.fdopen(descriptor, "w") as f:
            f.write(json.dumps({"pid": os.getpid(), "desde": time.time()}))
        self.mio = True

    def __enter__(self):
        arranque = time.time()
        aviso_dado = False
        while True:
            try:
                self._intentar()
                return self
            except OSError as error:
                if error.errno != errno.EEXIST:
                    raise
            dueno = _dueno(self.ruta)
            edad = time.time() - float(dueno.get("desde") or 0)
            vivo = _vive(dueno.get("pid"))
            if vivo is not True and edad > TOPE_DE_HUERFANO:
                # SE ROMPE, PERO NUNCA EN SILENCIO, y se dice cual de las dos cosas
                # se supo: que el proceso no existe, o que no se pudo saber.
                self.avisar("CERROJO HUERFANO: el proceso %s %s y el cerrojo lleva "
                            "%d s. Se rompe y se declara."
                            % (dueno.get("pid"),
                               "no existe" if vivo is False
                               else "no se puede comprobar en este sistema", edad))
                try:
                    os.unlink(self.ruta)
                except OSError:
                    pass
                continue
            if not aviso_dado:
                self.avisar("EL DATASET ESTA OCUPADO por el proceso %s. Espero: "
                            "EXTRACTOR.md 2 manda UN CANDIDATO POR VEZ."
                            % dueno.get("pid"))
                aviso_dado = True
            if time.time() - arranque > self.tope:
                raise CerrojoOcupado(
                    "el dataset lleva %d s ocupado por el proceso %s. NO se escribe "
                    "nada: una insercion que pisa a otra pierde un nodo con el gate "
                    "en verde, y eso ya paso una vez (vuelta 28)."
                    % (self.tope, dueno.get("pid")))
            time.sleep(self.espera)

    def __exit__(self, *_lo_que_sea):
        if self.mio:
            try:
                os.unlink(self.ruta)
            except OSError:
                pass
            self.mio = False
        return False
