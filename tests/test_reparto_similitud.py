# -*- coding: utf-8 -*-
"""PRUEBA DEL REPARTO DE LA SEÑAL 1 (decision del fundador, 25 sep 2026).

La aduana reparte entre procesos las comparaciones de `senal_similitud_texto` de un
candidato contra la poblacion. El cambio es de RENDIMIENTO y de nada mas: esta
prueba exige que el reparto de EXACTAMENTE lo mismo que el calculo en serie.

    python tests/test_reparto_similitud.py

  1. similitudes_repartidas == la señal 1 en serie, par a par, sobre nodos reales
     del grafo y un texto vacio (que da NO APLICA).
     caso positivo: la misma lista en otro orden NO es igual, o sea, la
     comparacion distingue.
  2. buscar_vecinos con reparto == buscar_vecinos sin reparto (un solo proceso),
     serializado a JSON, byte a byte.
  3. Si los procesos del reparto no pueden lanzarse, el resultado sigue siendo el
     mismo: el trozo se calcula en serie.

La equivalencia sobre la aduana y el barrido enteros (seis filas de la vuelta 70 y
cinco candidatos pendientes, identicos byte a byte) se midio antes de aplicar el
cambio y va en el mensaje de su commit.
"""
import json
import os
import sys
import unittest
from unittest import mock

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
os.chdir(RAIZ)

from src import aduana, comun  # noqa: E402
from src import config as modulo_config  # noqa: E402


def _poblacion(n):
    nodos = comun.leer_jsonl(comun.RUTA_DATASET)
    nodos = sorted(nodos, key=lambda x: len(comun.texto_comparable(x)))
    return nodos[:n]


def _igual(a, b):
    if isinstance(a, aduana.NoAplica) or isinstance(b, aduana.NoAplica):
        return isinstance(a, aduana.NoAplica) and isinstance(b, aduana.NoAplica) and a.motivo == b.motivo
    return type(a) is type(b) and a == b


class PruebaReparto(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.poblacion = _poblacion(60)
        cls.candidato = cls.poblacion[-1]
        cls.texto_a = comun.texto_comparable(cls.candidato)
        cls.textos_b = [comun.texto_comparable(n) for n in cls.poblacion[:-1]] + [""]

    def test_1_el_reparto_da_lo_mismo_que_la_serie(self):
        with mock.patch.dict(os.environ, {aduana.VARIABLE_PROCESOS_SIMILITUD: "4"}):
            repartidas = aduana.similitudes_repartidas(self.texto_a, self.textos_b)
        serie = [aduana.senal_similitud_texto(self.texto_a, b) for b in self.textos_b]
        self.assertEqual(len(repartidas), len(serie))
        for i, (r, s) in enumerate(zip(repartidas, serie)):
            self.assertTrue(_igual(r, s), "par %d distinto: %r frente a %r" % (i, r, s))
        self.assertIsInstance(repartidas[-1], aduana.NoAplica)
        # caso positivo: la comparacion distingue un orden cambiado
        cambiado = list(reversed(serie))
        self.assertFalse(all(_igual(r, s) for r, s in zip(repartidas, cambiado)))

    def test_2_buscar_vecinos_igual_con_y_sin_reparto(self):
        umbrales = modulo_config.cargar()
        with mock.patch.dict(os.environ, {aduana.VARIABLE_PROCESOS_SIMILITUD: "1"}):
            sin = aduana.buscar_vecinos(self.candidato, self.poblacion, umbrales)
        with mock.patch.dict(os.environ, {aduana.VARIABLE_PROCESOS_SIMILITUD: "4"}):
            con = aduana.buscar_vecinos(self.candidato, self.poblacion, umbrales)
        a = json.dumps(sin, ensure_ascii=False, sort_keys=True).encode("utf-8")
        b = json.dumps(con, ensure_ascii=False, sort_keys=True).encode("utf-8")
        self.assertEqual(a, b)

    def test_3_si_no_se_pueden_lanzar_procesos_el_resultado_no_cambia(self):
        serie = [aduana.senal_similitud_texto(self.texto_a, b) for b in self.textos_b]
        with mock.patch.dict(os.environ, {aduana.VARIABLE_PROCESOS_SIMILITUD: "4"}), \
                mock.patch.object(aduana.sys, "executable", os.path.join(RAIZ, "no_existe", "python.exe")):
            repartidas = aduana.similitudes_repartidas(self.texto_a, self.textos_b)
        self.assertTrue(all(_igual(r, s) for r, s in zip(repartidas, serie)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
