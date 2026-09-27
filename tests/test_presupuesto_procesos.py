# -*- coding: utf-8 -*-
"""PRUEBA DEL PRESUPUESTO UNICO DE PROCESOS (decision del fundador, 25 sep 2026).

Entre todos los barridos y aduanas que corran a la vez, el total de procesos de
calculo nunca pasa de nucleos menos uno, y el reparto se ajusta solo segun cuantos
corran (src/presupuesto.py).

    python tests/test_presupuesto_procesos.py

  1. Tres repartos a la vez con un presupuesto de 3 plazas: nunca hay mas de 3
     procesos de calculo vivos, y cada resultado es el de la serie.
     caso positivo: con un presupuesto de 9, los mismos tres repartos SI pasan de 3
     procesos a la vez, o sea, el contador distingue.
  2. Un reparto solo toma todas las plazas (el reparto se ajusta hacia arriba).
  3. Las plazas son de la MAQUINA: si otro proceso las tiene, aqui no se toma
     ninguna.
  4. Una presencia de un proceso muerto (fichero sin cerrojo) no cuenta y se borra.
  5. El calculo EN SERIE tambien toma plaza: PlazaPropia espera mientras otro proceso
     tiene todas las plazas y entra en cuanto quedan libres; y buscar_vecinos hace su
     parte en serie (la señal 3) dentro de una PlazaPropia.
  6. Las plazas son NUCLEOS menos uno, no hilos: nunca mas que nucleos fisicos menos uno.
"""
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from unittest import mock

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
os.chdir(RAIZ)

from src import aduana, comun, presupuesto  # noqa: E402


class Contador:
    """Envuelve subprocess.Popen de la aduana y cuenta los procesos vivos."""

    def __init__(self):
        self.vivos = 0
        self.maximo = 0
        self.candado = threading.Lock()
        original = subprocess.Popen
        contador = self

        class Contado(original):
            def __init__(self, *a, **k):
                super().__init__(*a, **k)
                with contador.candado:
                    contador.vivos += 1
                    contador.maximo = max(contador.maximo, contador.vivos)

            def communicate(self, *a, **k):
                try:
                    return super().communicate(*a, **k)
                finally:
                    with contador.candado:
                        contador.vivos -= 1

        self.clase = Contado


def _igual(a, b):
    if isinstance(a, aduana.NoAplica) or isinstance(b, aduana.NoAplica):
        return isinstance(a, aduana.NoAplica) and isinstance(b, aduana.NoAplica) and a.motivo == b.motivo
    return type(a) is type(b) and a == b


class PruebaPresupuesto(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        nodos = sorted(comun.leer_jsonl(comun.RUTA_DATASET), key=lambda x: len(comun.texto_comparable(x)))[:61]
        cls.textos_a = [comun.texto_comparable(n) for n in nodos[-3:]]
        cls.textos_b = [comun.texto_comparable(n) for n in nodos[:58]]
        cls.serie = [[aduana.senal_similitud_texto(a, b) for b in cls.textos_b] for a in cls.textos_a]

    def setUp(self):
        self.dir = tempfile.mkdtemp(prefix="presupuesto_")

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def _tres_a_la_vez(self, plazas):
        contador = Contador()
        resultados = [None] * 3
        entorno = {presupuesto.VARIABLE_TOTAL: str(plazas), presupuesto.VARIABLE_DIR: self.dir,
                   aduana.VARIABLE_PROCESOS_SIMILITUD: "0"}
        with mock.patch.dict(os.environ, entorno), mock.patch.object(aduana.subprocess, "Popen", contador.clase):
            def uno(i):
                resultados[i] = aduana.similitudes_repartidas(self.textos_a[i], self.textos_b)
            hilos = [threading.Thread(target=uno, args=(i,)) for i in range(3)]
            for h in hilos:
                h.start()
            for h in hilos:
                h.join()
        return contador.maximo, resultados

    def test_1_tres_repartos_nunca_pasan_del_presupuesto(self):
        maximo, resultados = self._tres_a_la_vez(3)
        self.assertLessEqual(maximo, 3)
        self.assertGreaterEqual(maximo, 1)
        for serie, repartida in zip(self.serie, resultados):
            self.assertEqual(len(serie), len(repartida))
            self.assertTrue(all(_igual(a, b) for a, b in zip(serie, repartida)))
        # caso positivo: con mas plazas, los mismos tres repartos pasan de 3 a la vez
        maximo_holgado, _ = self._tres_a_la_vez(9)
        self.assertGreater(maximo_holgado, 3)

    def test_2_un_reparto_solo_toma_todas_las_plazas(self):
        entorno = {presupuesto.VARIABLE_TOTAL: "3", presupuesto.VARIABLE_DIR: self.dir,
                   aduana.VARIABLE_PROCESOS_SIMILITUD: "0"}
        with mock.patch.dict(os.environ, entorno):
            aduana.similitudes_repartidas(self.textos_a[0], self.textos_b)
        self.assertEqual(aduana.similitudes_repartidas.maximo_de_plazas, 3)

    def test_3_las_plazas_son_de_la_maquina(self):
        codigo = ("import os, sys, time; sys.path.insert(0, %r); from src import presupuesto; "
                  "t = [presupuesto._tomar(os.path.join(presupuesto.directorio(), 'plaza_%%02d.lock' %% i)) for i in range(2)]; "
                  "print(sum(x is not None for x in t), flush=True); time.sleep(30)" % RAIZ)
        entorno = dict(os.environ, **{presupuesto.VARIABLE_TOTAL: "2", presupuesto.VARIABLE_DIR: self.dir})
        otro = subprocess.Popen([sys.executable, "-c", codigo], env=entorno, stdout=subprocess.PIPE, text=True)
        try:
            self.assertEqual(otro.stdout.readline().strip(), "2")
            with mock.patch.dict(os.environ, {presupuesto.VARIABLE_TOTAL: "2", presupuesto.VARIABLE_DIR: self.dir}):
                self.assertIsNone(presupuesto.Plazas().tomar())
        finally:
            otro.kill()
            otro.wait()
            otro.stdout.close()
        # muerto el otro proceso, sus plazas quedan libres sin que nadie las rompa
        time.sleep(0.5)
        with mock.patch.dict(os.environ, {presupuesto.VARIABLE_TOTAL: "2", presupuesto.VARIABLE_DIR: self.dir}):
            plazas = presupuesto.Plazas()
            plaza = plazas.tomar()
            self.assertIsNotNone(plaza)
            plazas.devolver(plaza)

    def test_4_una_presencia_muerta_no_cuenta(self):
        with mock.patch.dict(os.environ, {presupuesto.VARIABLE_TOTAL: "4", presupuesto.VARIABLE_DIR: self.dir}):
            muerta = os.path.join(self.dir, "presencia_999999_0.lock")
            open(muerta, "wb").close()
            with presupuesto.Presencia(), presupuesto.Presencia():
                self.assertEqual(presupuesto.presencias(), 2)
                self.assertEqual(presupuesto.cuota(), 2)
            self.assertFalse(os.path.exists(muerta))
            self.assertEqual(presupuesto.cuota(), 4)

    def test_5_el_calculo_en_serie_tambien_toma_plaza(self):
        codigo = ("import os, sys, time; sys.path.insert(0, %r); from src import presupuesto; "
                  "t = [presupuesto._tomar(os.path.join(presupuesto.directorio(), 'plaza_%%02d.lock' %% i)) for i in range(2)]; "
                  "print(sum(x is not None for x in t), flush=True); time.sleep(3)" % RAIZ)
        entorno = dict(os.environ, **{presupuesto.VARIABLE_TOTAL: "2", presupuesto.VARIABLE_DIR: self.dir})
        otro = subprocess.Popen([sys.executable, "-c", codigo], env=entorno, stdout=subprocess.PIPE, text=True)
        try:
            self.assertEqual(otro.stdout.readline().strip(), "2")
            t0 = time.time()
            with mock.patch.dict(os.environ, {presupuesto.VARIABLE_TOTAL: "2", presupuesto.VARIABLE_DIR: self.dir}):
                with presupuesto.PlazaPropia() as propia:
                    esperado = time.time() - t0
                    self.assertIsNotNone(propia._plaza)
            self.assertGreater(esperado, 1.0)
        finally:
            otro.wait()
            otro.stdout.close()
        # buscar_vecinos: su parte en serie entra en una PlazaPropia
        entradas = []
        original = presupuesto.PlazaPropia.__enter__

        def contado(yo):
            entradas.append(1)
            return original(yo)
        nodos = comun.leer_jsonl(comun.RUTA_DATASET)[:50]
        with mock.patch.dict(os.environ, {presupuesto.VARIABLE_DIR: self.dir}),                 mock.patch.object(presupuesto.PlazaPropia, "__enter__", contado):
            aduana.buscar_vecinos(nodos[0], nodos)
        self.assertEqual(len(entradas), 1)

    def test_6_las_plazas_son_nucleos_no_hilos(self):
        self.assertLessEqual(presupuesto.nucleos_fisicos(), os.cpu_count())
        with mock.patch.dict(os.environ, {presupuesto.VARIABLE_TOTAL: "0"}):
            self.assertEqual(presupuesto.total(), max(1, presupuesto.nucleos_fisicos() - 1))


if __name__ == "__main__":
    unittest.main(verbosity=2)
