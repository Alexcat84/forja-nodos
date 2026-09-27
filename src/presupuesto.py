# -*- coding: utf-8 -*-
"""PRESUPUESTO UNICO DE PROCESOS DE CALCULO PARA TODA LA MAQUINA (decision del fundador, 25 sep 2026).

LA CAIDA QUE LO OBLIGO. El reparto de la señal 1 de la aduana tomaba, en cada
aduana, tantos procesos como nucleos menos uno. Con el barrido de cinco candidatos
a la vez eran cinco aduanas por diecinueve procesos: la cola del procesador paso de
cuarenta y el equipo se trabo (el arranque de PowerShell subio de 2 a 26 segundos).

LA REGLA. Entre todos los barridos y aduanas que corran a la vez en la maquina, el
total de procesos de calculo NUNCA pasa de nucleos menos uno, y el reparto se
ajusta solo segun cuantos corran. NUCLEOS FISICOS, no hilos (ver `nucleos_fisicos`).

COMO. El presupuesto son PLAZAS: un fichero por plaza en un directorio comun a toda
la maquina. Un proceso de calculo solo arranca con una plaza tomada, y la plaza se
toma con un cerrojo del sistema operativo sobre su fichero. Por construccion, nunca
hay mas procesos de calculo que plazas. El cerrojo del sistema se suelta solo si el
proceso que lo tiene muere: no hay plazas huerfanas que romper.

EL CALCULO EN SERIE TAMBIEN CUENTA. Lo que un proceso calcula el mismo, sin
repartir (la señal 3 de la aduana, vecino a vecino), ocupa un nucleo igual que un
proceso del reparto: lo hace con una plaza tomada (`PlazaPropia`), esperando si no
hay ninguna libre.

EL AJUSTE. Cada reparto en curso deja una PRESENCIA (otro fichero con cerrojo). Su
cuota es la parte justa, plazas entre presencias redondeando hacia arriba, y se
vuelve a mirar antes de cada trozo de trabajo: cuando entra un barrido los demas
ceden plazas al acabar su trozo, y cuando uno termina los demas las recogen.

    FORJA_PRESUPUESTO_PROCESOS  baja el total de plazas (las pruebas lo usan)
    FORJA_PRESUPUESTO_DIR       otro directorio de plazas (las pruebas lo usan)
"""

import functools
import itertools
import os
import tempfile
import threading
import time

VARIABLE_TOTAL = "FORJA_PRESUPUESTO_PROCESOS"
VARIABLE_DIR = "FORJA_PRESUPUESTO_DIR"
ESPERA = 0.2                 # segundos entre intentos de tomar plaza

if os.name == "nt":
    import msvcrt

    def _bloquear(fichero):
        fichero.seek(0)
        msvcrt.locking(fichero.fileno(), msvcrt.LK_NBLCK, 1)

    def _soltar(fichero):
        fichero.seek(0)
        msvcrt.locking(fichero.fileno(), msvcrt.LK_UNLCK, 1)
else:
    import fcntl

    def _bloquear(fichero):
        fcntl.flock(fichero.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)

    def _soltar(fichero):
        fcntl.flock(fichero.fileno(), fcntl.LOCK_UN)


@functools.lru_cache(maxsize=1)
def nucleos_fisicos():
    """Los NUCLEOS de la maquina, no sus hilos. Medido el 25 sep 2026 en el equipo
    de la serial (i9-12900HK: 14 nucleos, 20 hilos): con 19 procesos de calculo, uno
    por hilo menos uno, los 20 hilos quedaban al 100% y abrir una terminal tardaba
    hasta 27 s. Dos hilos de un mismo nucleo comparten el nucleo: contar hilos como
    nucleos no deja ninguno libre. En Windows se cuentan con
    GetLogicalProcessorInformationEx; si eso falla, o en otro sistema, los hilos."""
    if os.name == "nt":
        try:
            import ctypes
            from ctypes import wintypes
            kernel = ctypes.windll.kernel32
            largo = wintypes.DWORD(0)
            kernel.GetLogicalProcessorInformationEx(0, None, ctypes.byref(largo))  # 0: un registro por nucleo
            memoria = ctypes.create_string_buffer(largo.value)
            if kernel.GetLogicalProcessorInformationEx(0, memoria, ctypes.byref(largo)):
                cuenta, desplazamiento = 0, 0
                while desplazamiento < largo.value:
                    cuenta += 1
                    desplazamiento += int.from_bytes(memoria.raw[desplazamiento + 4:desplazamiento + 8], "little")
                if cuenta > 0:
                    return cuenta
        except (OSError, AttributeError, ValueError):
            pass
    return os.cpu_count() or 1


def total():
    """Las plazas de la maquina: nucleos menos uno, o menos si la variable lo baja."""
    plazas = max(1, nucleos_fisicos() - 1)
    try:
        tope = int(os.environ.get(VARIABLE_TOTAL, "0") or "0")
    except ValueError:
        tope = 0
    if tope > 0:
        plazas = min(plazas, tope)
    return plazas


def directorio():
    ruta = os.environ.get(VARIABLE_DIR) or os.path.join(tempfile.gettempdir(), "forja_presupuesto_procesos")
    os.makedirs(ruta, exist_ok=True)
    return ruta


def _tomar(ruta):
    """El fichero abierto y con su cerrojo, o None si otro lo tiene."""
    try:
        fichero = open(ruta, "a+b")
    except OSError:
        return None
    try:
        _bloquear(fichero)
    except OSError:
        fichero.close()
        return None
    return fichero


def _devolver(fichero):
    try:
        _soltar(fichero)
    except OSError:
        pass
    fichero.close()


_contador = itertools.count()


class Presencia:
    """Un reparto en curso. Mientras dura, cuenta en la cuota de todos."""

    def __enter__(self):
        ruta = os.path.join(directorio(), "presencia_%d_%d.lock" % (os.getpid(), next(_contador)))
        self._ruta = ruta
        self._fichero = _tomar(ruta)
        return self

    def __exit__(self, *_):
        if self._fichero is not None:
            _devolver(self._fichero)
            try:
                os.remove(self._ruta)
            except OSError:
                pass


def presencias():
    """Los repartos vivos en la maquina. Una presencia sin cerrojo es de un proceso
    que murio: se borra y no cuenta."""
    vivas = 0
    for nombre in os.listdir(directorio()):
        if not nombre.startswith("presencia_"):
            continue
        ruta = os.path.join(directorio(), nombre)
        fichero = _tomar(ruta)
        if fichero is None:
            vivas += 1
            continue
        _devolver(fichero)
        try:
            os.remove(ruta)
        except OSError:
            pass
    return max(1, vivas)


def cuota():
    """La parte justa de un reparto: plazas entre repartos vivos, hacia arriba."""
    return -(-total() // presencias())


class Plazas:
    """Las plazas de UN reparto: toma una plaza libre solo si el reparto esta por
    debajo de su cuota, y la devuelve al acabar cada trozo."""

    def __init__(self):
        self._candado = threading.Lock()
        self.en_uso = 0
        self.maximo = 0

    def tomar(self):
        """Una plaza (el fichero con cerrojo) o None si ahora no toca."""
        with self._candado:
            if self.en_uso >= cuota():
                return None
            carpeta = directorio()
            for i in range(total()):
                fichero = _tomar(os.path.join(carpeta, "plaza_%02d.lock" % i))
                if fichero is not None:
                    self.en_uso += 1
                    self.maximo = max(self.maximo, self.en_uso)
                    return fichero
            return None

    def devolver(self, fichero):
        with self._candado:
            self.en_uso -= 1
        _devolver(fichero)


class PlazaPropia:
    """El calculo en serie de ESTE proceso, con su plaza tomada mientras dura:

        with presupuesto.PlazaPropia():
            ...calculo...

    Espera a que haya plaza. Si el directorio de plazas no se puede usar, calcula
    sin plaza antes que no calcular."""

    def __enter__(self):
        self._plaza = None
        self._presencia = None
        try:
            self._presencia = Presencia().__enter__()
            self._plazas = Plazas()
            while True:
                self._plaza = self._plazas.tomar()
                if self._plaza is not None:
                    return self
                time.sleep(ESPERA)
        except OSError:
            return self

    def __exit__(self, *_):
        if self._plaza is not None:
            self._plazas.devolver(self._plaza)
        if self._presencia is not None:
            self._presencia.__exit__()
