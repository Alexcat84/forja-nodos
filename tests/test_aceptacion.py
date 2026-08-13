# -*- coding: utf-8 -*-
"""PRUEBA DE ACEPTACION de forja-nodos.

El repo NO esta terminado sin esta prueba en verde.

    python tests/test_aceptacion.py

Seis pruebas, una por guarda, y CADA GUARDA CON SU CASO POSITIVO (manual
seccion 2: "toda guarda con caso positivo: una prueba que no puede fallar no
guarda nada"). El caso positivo no es un adorno: es lo que demuestra que la
guarda distingue, en vez de decir siempre lo mismo.

  A. Un nodo ejemplo valido entra limpio y el gate queda verde.
     caso positivo: un candidato que rompe el esquema es rechazado.
  B. Un gemelo plantado del ejemplo (mismos pasos, otras palabras) es
     BLOQUEADO por la aduana citando al vecino y la señal.
     caso positivo: un nodo del mismo dominio y la misma fuente que hace otro
     trabajo entra limpio. Una aduana que bloquea todo es un candado.
  C. Un hijo (que despliega un paso del ejemplo) solo entra tras declarar la
     arista, y la arista queda RESUELTA.
     caso positivo: la arista se declara citando a la madre POR UN ALIAS y en
     el dataset queda escrito el id canonico.
  D. Un nodo con auto-arista VIA ALIAS pone el gate en rojo.
     caso positivo: la propia prueba comprueba que una comparacion literal NO
     lo veria, y que el mismo nodo sin el alias deja el gate verde.
  E. Un archivo con un guion largo hace fallar el hook.
     caso positivo: el mismo repo sin ese archivo pasa el hook en verde.
  F. Un candidato con fuente fuera de la tabla canonica es rechazado.
     caso positivo: el mismo candidato con fuente canonica entra limpio.
"""

import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURES = os.path.join(RAIZ, "tests", "fixtures")
EJEMPLO = os.path.join(RAIZ, "ejemplos", "registrar_fuente_canonica.json")
HIJO = os.path.join(RAIZ, "ejemplos", "elegir_grafia_clave.json")

sys.path.insert(0, RAIZ)

from src import comun, gate  # noqa: E402

# Con escape unicode: si esta prueba llevara el caracter literal, el barrido
# de guiones tendria que perdonar al archivo que lo comprueba.
GUION_LARGO = "\u2014"

RESULTADOS = {}


def nodo_base(identificador, **campos):
    nodo = {
        "id": identificador,
        "titulo": "Titulo de prueba de %s" % identificador,
        "resumen_teorico": "Resumen teorico de prueba, suficientemente largo para el esquema.",
        "pasos_accionables": [
            "Ejecuta el primer paso de prueba con su objeto.",
            "Ejecuta el segundo paso de prueba con su objeto.",
        ],
        "condiciones_activacion": "Cuando corre la prueba de aceptacion.",
        "entregable_esperado": "Un resultado comprobable por la prueba.",
        "fuentes": ["manual_sistema_conocimiento"],
        "ids_alias": [],
        "nodos_previos": [],
        "nodos_siguientes": [],
        "denominaciones": {"nombre_largo": "", "sigla": "", "otros_idiomas": []},
        "dominio": "prueba",
    }
    nodo.update(campos)
    return nodo


class BaseForja(unittest.TestCase):
    """Cada prueba corre la forja ENTERA contra un dataset de usar y tirar."""

    def setUp(self):
        self.taller = tempfile.mkdtemp(prefix="forja_prueba_")
        self.dataset = os.path.join(self.taller, "nodos.jsonl")
        self.veredictos = os.path.join(self.taller, "VEREDICTOS.jsonl")
        self.censos = os.path.join(self.taller, "censos")
        os.makedirs(self.censos)
        comun.escribir_texto(self.dataset, "")
        self.entorno = dict(os.environ)
        self.entorno.update({
            "FORJA_DATASET": self.dataset,
            "FORJA_VEREDICTOS": self.veredictos,
            "FORJA_CENSOS": self.censos,
            "PYTHONIOENCODING": "utf-8",
        })

    def tearDown(self):
        shutil.rmtree(self.taller, ignore_errors=True)

    def forja(self, *argumentos):
        proceso = subprocess.Popen(
            [sys.executable, "forja.py"] + list(argumentos),
            cwd=RAIZ, env=self.entorno,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        crudo = proceso.communicate()[0]
        return proceso.returncode, crudo.decode("utf-8", "replace")

    def nodos(self):
        return comun.leer_jsonl(self.dataset)

    def escribir_dataset(self, nodos):
        comun.escribir_jsonl(self.dataset, nodos)

    def sembrar_ejemplo(self):
        codigo, salida = self.forja("insertar", EJEMPLO, "--sin-preguntas")
        self.assertEqual(codigo, 0, salida)
        return salida

    def fixture(self, nombre):
        return os.path.join(FIXTURES, nombre)

    def anotar(self, clave, texto):
        RESULTADOS[clave] = texto


class PruebaA(BaseForja):
    """A. El nodo ejemplo valido entra limpio y el gate queda verde."""

    def test_a_nodo_ejemplo_entra_limpio(self):
        codigo, salida = self.forja("insertar", EJEMPLO, "--sin-preguntas",
                                    "--censo", "herramienta=forja.py;url=repo local",
                                    "--censo", "serie=no")
        self.assertEqual(codigo, 0, salida)
        self.assertIn("NODO INSERTADO", salida)

        nodos = self.nodos()
        self.assertEqual(len(nodos), 1)
        self.assertEqual(nodos[0]["id"], "registrar_fuente_canonica")

        codigo, salida_gate = self.forja("gate")
        self.assertEqual(codigo, 0, salida_gate)
        self.assertIn("GATE VERDE", salida_gate)

        # Los censos se escriben AL ENTRAR (manual seccion 3.6), y nombre
        # largo, sigla y termino en otro idioma son TRES denominaciones aparte.
        clases = self._clases_de_denominacion()
        self.assertEqual(sorted(clases), ["nombre_largo", "otro_idioma", "sigla"])
        herramientas = comun.leer_texto(os.path.join(self.censos, "herramientas.md"))
        self.assertIn("forja.py", herramientas)

        self.anotar("A", "VERDE: el nodo ejemplo entro limpio, el gate quedo verde y "
                         "los censos registraron las tres denominaciones por separado")

    def test_a_caso_positivo_esquema_roto(self):
        """Caso positivo: la guarda de esquema puede fallar, y falla."""
        roto = nodo_base("nodo_sin_pasos", pasos_accionables=[])
        ruta = os.path.join(self.taller, "roto.json")
        comun.escribir_texto(ruta, json.dumps(roto, ensure_ascii=False))
        codigo, salida = self.forja("insertar", ruta, "--sin-preguntas")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("no cumple esquema", salida)
        self.assertEqual(self.nodos(), [])

    def _clases_de_denominacion(self):
        ruta = os.path.join(self.censos, "denominaciones.md")
        clases = []
        for linea in comun.leer_texto(ruta).split("\n"):
            celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
            if len(celdas) == 6 and celdas[0] not in ("fecha", "---"):
                clases.append(celdas[2])
        return clases


class PruebaB(BaseForja):
    """B. El gemelo plantado es bloqueado citando al vecino y la señal."""

    def test_b_gemelo_bloqueado(self):
        self.sembrar_ejemplo()
        codigo, salida = self.forja("insertar", self.fixture("gemelo_plantado.json"),
                                    "--sin-preguntas")
        self.assertEqual(codigo, 2, salida)
        self.assertIn("LA INSERCION QUEDA BLOQUEADA", salida)
        # cita al vecino por su id
        self.assertIn("registrar_fuente_canonica", salida)
        # y cita la señal que lo levanto
        self.assertIn("levantada por:", salida)
        self.assertTrue("similitud_texto" in salida or "paso_contra_nodo" in salida, salida)
        # el gemelo NO entro
        self.assertEqual([n["id"] for n in self.nodos()], ["registrar_fuente_canonica"])

        señales = [linea for linea in salida.split("\n") if "levantada por:" in linea]
        self.anotar("B", "VERDE: gemelo bloqueado (codigo 2) citando a "
                         "registrar_fuente_canonica y la señal (%s)"
                    % señales[0].split("levantada por:")[1].strip())

    def test_b_senal_2_familia_de_id_sola(self):
        """La señal 2 aislada: mismo trabajo NO, id de la misma familia SI.

        Sin esto, la familia de id seria codigo que ninguna prueba ejerce, y
        una señal que nadie ejerce no ordena nada.
        """
        self.sembrar_ejemplo()
        codigo, salida = self.forja("insertar", self.fixture("familia_parecida.json"),
                                    "--sin-preguntas")
        self.assertEqual(codigo, 2, salida)
        linea = [l for l in salida.split("\n") if "levantada por:" in l][0]
        self.assertIn("familia_id", linea)
        self.assertNotIn("similitud_texto", linea)
        self.assertNotIn("paso_contra_nodo", linea)

    def test_b_caso_positivo_vecino_legitimo_entra(self):
        """Caso positivo: un nodo del mismo dominio y la misma fuente, que hace
        otro trabajo, ENTRA. Un bloqueador que bloquea todo no guarda nada."""
        self.sembrar_ejemplo()
        codigo, salida = self.forja("insertar", self.fixture("nodo_ajeno.json"),
                                    "--sin-preguntas")
        self.assertEqual(codigo, 0, salida)
        self.assertIn("NODO INSERTADO", salida)
        self.assertIn("medir_credito_relectura", [n["id"] for n in self.nodos()])


class PruebaC(BaseForja):
    """C. El hijo solo entra tras declarar la arista, que queda resuelta."""

    def sembrar_madre_con_alias(self):
        madre = json.loads(comun.leer_texto(EJEMPLO))
        madre["ids_alias"] = ["registro_fuentes_canonicas"]
        ruta = os.path.join(self.taller, "madre.json")
        comun.escribir_texto(ruta, json.dumps(madre, ensure_ascii=False))
        codigo, salida = self.forja("insertar", ruta, "--sin-preguntas")
        self.assertEqual(codigo, 0, salida)

    def test_c_hijo_bloqueado_y_luego_cableado(self):
        self.sembrar_madre_con_alias()

        # Sin veredicto, el hijo NO entra.
        codigo, salida = self.forja("insertar", HIJO,
                                    "--sin-preguntas")
        self.assertEqual(codigo, 2, salida)
        self.assertIn("paso_contra_nodo", salida)
        self.assertEqual(len(self.nodos()), 1)

        # Con el veredicto CONTINUA y la arista declarada, entra.
        # La madre se cita POR SU ALIAS: la arista ha de quedar RESUELTA.
        codigo, salida = self.forja(
            "insertar", HIJO, "--sin-preguntas",
            "--veredicto",
            "registro_fuentes_canonicas|CONTINUA|madre=registro_fuentes_canonicas|"
            "el candidato despliega en siete pasos el paso 2 de la madre: elegir la "
            "grafia de la clave es un procedimiento nombrado en una linea, y la prueba "
            "de que es procedimiento es que existe quien lo ejecuta")
        self.assertEqual(codigo, 0, salida)

        nodos = dict((n["id"], n) for n in self.nodos())
        self.assertIn("elegir_grafia_clave", nodos)

        # La arista esta escrita en los DOS extremos y con el id CANONICO,
        # no con el alias por el que se declaro (manual seccion 5).
        self.assertEqual(nodos["registrar_fuente_canonica"]["nodos_siguientes"],
                         ["elegir_grafia_clave"])
        self.assertEqual(nodos["elegir_grafia_clave"]["nodos_previos"],
                         ["registrar_fuente_canonica"])
        self.assertNotIn("registro_fuentes_canonicas",
                         nodos["elegir_grafia_clave"]["nodos_previos"])

        codigo, salida_gate = self.forja("gate")
        self.assertEqual(codigo, 0, salida_gate)

        # El veredicto y su razon quedaron en la bitacora.
        bitacora = comun.leer_jsonl(self.veredictos)
        self.assertEqual(len(bitacora), 1)
        self.assertEqual(bitacora[0]["veredicto"], "CONTINUA")
        self.assertIn("despliega", bitacora[0]["razon"])

        self.anotar("C", "VERDE: el hijo quedo bloqueado sin veredicto y entro tras "
                         "declarar CONTINUA; la arista se declaro por el alias "
                         "'registro_fuentes_canonicas' y quedo escrita resuelta como "
                         "registrar_fuente_canonica > elegir_grafia_clave")

    def test_c_caso_positivo_continua_sin_arista_es_rechazado(self):
        """Caso positivo: CONTINUA exige declarar la arista madre-hijo, y con
        una madre que no es ninguno de los dos, la aduana rechaza."""
        self.sembrar_madre_con_alias()
        codigo, salida = self.forja(
            "insertar", HIJO, "--sin-preguntas",
            "--veredicto", "registro_fuentes_canonicas|CONTINUA|madre=un_tercero|razon")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("CONTINUA exige declarar la arista", salida)
        self.assertEqual(len(self.nodos()), 1)

    def test_c_caso_positivo_veredicto_sin_razon_es_rechazado(self):
        """Caso positivo: la razon escrita no es opcional."""
        self.sembrar_madre_con_alias()
        codigo, salida = self.forja(
            "insertar", HIJO, "--sin-preguntas",
            "--veredicto", "registro_fuentes_canonicas|SANO|")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("sin razon escrita", salida)


class PruebaD(BaseForja):
    """D. Auto-arista VIA ALIAS: el gate en rojo donde lo literal no ve nada."""

    def test_d_auto_arista_via_alias(self):
        nodo = nodo_base("sanear_grafo",
                         ids_alias=["saneo_grafo"],
                         nodos_siguientes=["saneo_grafo"])
        self.escribir_dataset([nodo])

        # Primero, el control: una comparacion LITERAL no ve nada.
        literales = [d for d in nodo["nodos_siguientes"] if d == nodo["id"]]
        self.assertEqual(literales, [],
                         "el fixture ha de ser invisible para una comparacion literal")

        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("GATE EN ROJO", salida)
        self.assertIn("auto_arista", salida)
        self.assertIn("resuelve por alias al propio nodo", salida)

        self.anotar("D", "VERDE: la auto-arista via alias (saneo_grafo apunta a "
                         "sanear_grafo) puso el gate en rojo, y la comparacion literal "
                         "no la veia: cero coincidencias literales en el mismo dato")

    def test_d_caso_positivo_sin_alias_queda_verde(self):
        """Caso positivo: el mismo dataset, con la arista hacia otro nodo de
        verdad, deja el gate en VERDE. La guarda distingue."""
        madre = nodo_base("sanear_grafo", nodos_siguientes=["podar_ramas"])
        hijo = nodo_base("podar_ramas", nodos_previos=["sanear_grafo"])
        self.escribir_dataset([madre, hijo])
        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 0, salida)
        self.assertIn("GATE VERDE", salida)

    def test_d_caso_positivo_arista_a_alias_ajeno_si_resuelve(self):
        """Caso positivo del otro lado: una arista hacia el ALIAS de OTRO nodo
        resuelve y NO es fallo. Un chequeo literal inventaria enfermedad."""
        madre = nodo_base("sanear_grafo", nodos_siguientes=["poda_ramas"])
        hijo = nodo_base("podar_ramas", ids_alias=["poda_ramas"],
                         nodos_previos=["sanear_grafo"])
        self.escribir_dataset([madre, hijo])
        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 0, salida)


class PruebaE(BaseForja):
    """E. Un archivo con un guion largo hace fallar el hook."""

    def setUp(self):
        BaseForja.setUp(self)
        self.sucio = os.path.join(RAIZ, "tests", "tmp_archivo_con_guion.md")

    def tearDown(self):
        if os.path.exists(self.sucio):
            os.remove(self.sucio)
        BaseForja.tearDown(self)

    def correr_hook(self):
        """Corre el hook de verdad si hay sh; si no, su barrido, que es lo que
        el hook ejecuta. Se declara cual de los dos corrio."""
        interprete = shutil.which("sh") or shutil.which("bash")
        entorno = dict(os.environ)
        entorno["PYTHONIOENCODING"] = "utf-8"
        if interprete:
            proceso = subprocess.Popen([interprete, "hooks/pre-commit"], cwd=RAIZ,
                                       env=entorno, stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT)
            crudo = proceso.communicate()[0]
            return proceso.returncode, crudo.decode("utf-8", "replace"), "hooks/pre-commit"
        proceso = subprocess.Popen([sys.executable, "forja.py", "guiones"], cwd=RAIZ,
                                   env=entorno, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        crudo = proceso.communicate()[0]
        return proceso.returncode, crudo.decode("utf-8", "replace"), "forja.py guiones"

    def test_e_guion_largo_rompe_el_hook(self):
        # Caso positivo primero: sin el archivo sucio, el hook esta VERDE.
        codigo, salida, quien = self.correr_hook()
        self.assertEqual(codigo, 0,
                         "el repo ha de estar limpio antes de ensuciarlo:\n%s" % salida)

        comun.escribir_texto(
            self.sucio,
            "# Archivo temporal de la prueba E\n\n"
            "Esta linea lleva un guion largo %s y por eso el hook tiene que abortar.\n"
            % GUION_LARGO)

        codigo, salida, quien = self.correr_hook()
        self.assertNotEqual(codigo, 0, salida)
        self.assertIn("tmp_archivo_con_guion.md", salida)
        self.assertIn("guion largo", salida)

        os.remove(self.sucio)
        codigo, salida, quien = self.correr_hook()
        self.assertEqual(codigo, 0, salida)

        self.anotar("E", "VERDE: %s aborto con el guion largo (rojo con el archivo, "
                         "verde sin el, verde de nuevo al quitarlo)" % quien)


class PruebaF(BaseForja):
    """F. Fuente fuera de la tabla canonica: rechazado."""

    def test_f_fuente_fuera_de_tabla(self):
        codigo, salida = self.forja("insertar", self.fixture("fuente_invento.json"),
                                    "--sin-preguntas")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("CAMPO SAGRADO", salida)
        self.assertIn("libro_que_nadie_registro", salida)
        self.assertEqual(self.nodos(), [])

        self.anotar("F", "VERDE: el candidato con la fuente 'libro_que_nadie_registro' "
                         "fue rechazado y no toco el dataset")

    def test_f_caso_positivo_con_fuente_canonica_entra(self):
        """Caso positivo: el MISMO candidato con una fuente de la tabla entra
        limpio. Lo unico que cambio es la fuente."""
        candidato = json.loads(comun.leer_texto(self.fixture("fuente_invento.json")))
        candidato["fuentes"] = ["manual_sistema_conocimiento"]
        ruta = os.path.join(self.taller, "con_fuente_canonica.json")
        comun.escribir_texto(ruta, json.dumps(candidato, ensure_ascii=False))
        codigo, salida = self.forja("insertar", ruta, "--sin-preguntas")
        self.assertEqual(codigo, 0, salida)
        self.assertEqual([n["id"] for n in self.nodos()], ["podar_ramas_muertas"])


class PruebaGate(BaseForja):
    """Guardas del gate que no tienen prueba con letra propia, cada una con su
    caso positivo. Sin esto, tres de las guardas del gate no guardarian nada."""

    def test_arista_duplicada_tras_resolver(self):
        madre = nodo_base("sanear_grafo", nodos_siguientes=["podar_ramas", "poda_ramas"])
        hijo = nodo_base("podar_ramas", ids_alias=["poda_ramas"],
                         nodos_previos=["sanear_grafo"])
        self.escribir_dataset([madre, hijo])
        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("arista_duplicada", salida)
        # caso positivo: sin la entrada repetida, verde
        madre["nodos_siguientes"] = ["podar_ramas"]
        self.escribir_dataset([madre, hijo])
        self.assertEqual(self.forja("gate")[0], 0)

    def test_vuelta_en_par_madre_hijo(self):
        madre = nodo_base("sanear_grafo", nodos_siguientes=["podar_ramas"],
                          nodos_previos=["podar_ramas"])
        hijo = nodo_base("podar_ramas", nodos_previos=["sanear_grafo"],
                         nodos_siguientes=["sanear_grafo"])
        self.escribir_dataset([madre, hijo])
        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("vuelta", salida)
        # caso positivo: en un solo sentido, verde
        madre["nodos_previos"] = []
        hijo["nodos_siguientes"] = []
        self.escribir_dataset([madre, hijo])
        self.assertEqual(self.forja("gate")[0], 0)

    def test_arista_hacia_id_inexistente(self):
        madre = nodo_base("sanear_grafo", nodos_siguientes=["nodo_fantasma"])
        self.escribir_dataset([madre])
        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("arista_rota", salida)

    def test_familia_de_id_repetida(self):
        """Misma familia: cambia el orden y el plural, nada mas."""
        uno = nodo_base("registro_fuentes")
        dos = nodo_base("fuente_registro")
        self.escribir_dataset([uno, dos])
        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("misma familia de id", salida)
        # caso positivo: dos ids de familias distintas conviven en verde
        self.escribir_dataset([nodo_base("registro_fuentes"),
                               nodo_base("podar_ramas")])
        self.assertEqual(self.forja("gate")[0], 0)

    def test_reglas_de_id_en_el_gate(self):
        for identificador, marca in (("registrar_de_fuentes", "preposicion"),
                                     ("registrar_fuentes_2", "sufijo numerico"),
                                     ("extraer_nodes", "fuera del castellano")):
            self.escribir_dataset([nodo_base(identificador)])
            codigo, salida = self.forja("gate")
            self.assertEqual(codigo, 1, salida)
            self.assertIn(marca, salida)
        # caso positivo: el id bien puesto deja el gate verde
        self.escribir_dataset([nodo_base("registrar_fuentes")])
        self.assertEqual(self.forja("gate")[0], 0)

    def test_guion_largo_en_un_nodo(self):
        sucio = nodo_base("sanear_grafo")
        sucio["resumen_teorico"] = "Un resumen con un guion largo %s dentro." % GUION_LARGO
        self.escribir_dataset([sucio])
        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("guion largo", salida)


class PruebaResolutor(BaseForja):
    """El resolutor camina cadenas: sin esto, el principio 3 es una frase."""

    def test_cadena_de_alias(self):
        from src.resolutor import Resolutor
        nodos = [nodo_base("sanear_grafo", ids_alias=["saneo_grafo"]),
                 nodo_base("podar_ramas", ids_alias=["sanear_grafo_viejo"])]
        # cadena: alias -> alias -> canonico
        nodos[0]["ids_alias"] = ["saneo_grafo"]
        nodos[1]["ids_alias"] = ["poda_ramas"]
        nodos.append(nodo_base("limpiar_grafo", ids_alias=["podar_ramas_antiguo"]))
        resolutor = Resolutor(nodos)
        self.assertEqual(resolutor.resolver("saneo_grafo"), "sanear_grafo")
        self.assertEqual(resolutor.resolver("poda_ramas"), "podar_ramas")
        self.assertEqual(resolutor.resolver("no_existe_esto"), None)
        self.assertTrue(resolutor.mismo("saneo_grafo", "sanear_grafo"))
        self.assertFalse(resolutor.mismo("saneo_grafo", "podar_ramas"))

    def test_alias_que_es_id_vivo_es_fallo(self):
        nodos = [nodo_base("sanear_grafo", ids_alias=["podar_ramas"]),
                 nodo_base("podar_ramas")]
        self.escribir_dataset(nodos)
        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("dos cosas con un nombre", salida)


def main():
    comun.salida_utf8()
    orden = [PruebaA, PruebaB, PruebaC, PruebaD, PruebaE, PruebaF,
             PruebaGate, PruebaResolutor]
    conjunto = unittest.TestSuite()
    cargador = unittest.TestLoader()
    for clase in orden:
        conjunto.addTests(cargador.loadTestsFromTestCase(clase))
    resultado = unittest.TextTestRunner(verbosity=2).run(conjunto)

    print("")
    print("=" * 72)
    print("PRUEBA DE ACEPTACION DE forja-nodos")
    print("=" * 72)
    for letra in ("A", "B", "C", "D", "E", "F"):
        print("  %s. %s" % (letra, RESULTADOS.get(letra, "sin resultado registrado")))
    print("")
    print("  guardas del gate y resolutor: %d pruebas mas, cada una con su caso positivo"
          % (len(cargador.loadTestsFromTestCase(PruebaGate)._tests)
             + len(cargador.loadTestsFromTestCase(PruebaResolutor)._tests)))
    print("")
    print("  total: %d pruebas, %d fallos, %d errores"
          % (resultado.testsRun, len(resultado.failures), len(resultado.errors)))
    print("=" * 72)
    return 0 if resultado.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
