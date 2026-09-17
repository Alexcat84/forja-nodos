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

Mas las adjudicaciones del auditor (docs/BANCO_DE_REGLAS.md):
  A.1 MUTUO: una vuelta declarada como enlace mutuo, con ida y vuelta
      escritas, pasa el gate; la MISMA vuelta sin declarar lo pone en rojo.
  A.2 fuentes con fecha: un nodo con mas de una fuente fuera de orden de
      fecha lo pone en rojo; en orden, pasa.

Y la TANDA A de la v0.3 (decision del fundador del 4 sep 2026 al final de
docs/COSECHA_2026-09.md), cada pieza con su caso positivo:
  C.1 el MUTUO cita DOS LINEAS DISTINTAS: el legitimo pasa, el solape
      disfrazado cae nombrando el paso.
  C.2 el registro de citas se verifica ENTERO: un par sin cita, o con cita
      incompleta, es rojo que lo nombra.
  C.3 el bloque de vigencia: un veredicto contra texto que cambio es RANCIO.
  C.4 ninguna señal devuelve cero silencioso: fuera de su dominio devuelve
      NO APLICA, y NO APLICA revienta si se compara con un umbral.
  D.17 el deprecado es archivo, no superficie.
"""

import io
import json
import os
import re
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

from src import comun, gate, herencia  # noqa: E402

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
        "fuentes": [{"clave": "manual_sistema_conocimiento", "fecha": "2026-08-12"}],
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
        self.pares_mutuos = os.path.join(self.taller, "pares_mutuos.jsonl")
        # LA BANDEJA DEL TALLER, desde que D.38.5 llego a la aduana: sin esto la
        # prueba mediria contra los candidatos del repo de verdad y su resultado
        # cambiaria de una vuelta a otra.
        self.bandeja = os.path.join(self.taller, "cuarentena")
        os.makedirs(self.bandeja)
        self.fuentes_tabla = os.path.join(self.taller, "FUENTES_CANONICAS.json")
        os.makedirs(self.censos)
        comun.escribir_texto(self.dataset, "")
        # Tabla de fuentes aislada, con una clave extra para poder probar el
        # orden por fecha (guarda orden_fuentes) sin tocar la tabla real.
        comun.escribir_texto(self.fuentes_tabla, json.dumps({
            "manual_sistema_conocimiento": {
                "titulo_completo": "MANUAL DEL SISTEMA DE CONOCIMIENTO",
                "autor": "Casa My Idea", "anio": "2026"},
            "segundo_libro_de_prueba": {
                "titulo_completo": "Segundo libro de prueba",
                "autor": "Prueba", "anio": "2026"},
        }, ensure_ascii=False))
        self.entorno = dict(os.environ)
        self.entorno.update({
            "FORJA_DATASET": self.dataset,
            "FORJA_VEREDICTOS": self.veredictos,
            "FORJA_CENSOS": self.censos,
            "FORJA_PARES_MUTUOS": self.pares_mutuos,
            "FORJA_CUARENTENA": self.bandeja,
            "FORJA_FUENTES": self.fuentes_tabla,
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

    def pares(self):
        return comun.leer_jsonl(self.pares_mutuos)

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
        candidato["fuentes"] = [{"clave": "manual_sistema_conocimiento", "fecha": "2026-08-12"}]
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
        # El texto de la regla 1 y de la regla 2 cambio el 10 sep 2026 con la
        # decision del fundador. La guarda es la misma; lo que dice, no.
        for identificador, marca in (("registrar_de_fuentes", "preposicion"),
                                     ("registrar_fuentes_2", "sufijo numerico de VERSION"),
                                     ("extraer_nodes", "palabra inglesa con equivalente")):
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

    def test_a2_orden_de_fuentes_por_fecha(self):
        """A.2: en un nodo con mas de una fuente, la fecha no puede
        retroceder de una posicion a la siguiente."""
        nodo = nodo_base("sanear_grafo", fuentes=[
            {"clave": "manual_sistema_conocimiento", "fecha": "2026-08-12"},
            {"clave": "segundo_libro_de_prueba", "fecha": "2026-08-01"},
        ])
        self.escribir_dataset([nodo])
        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("orden_fuentes", salida)
        # caso positivo: la misma pareja, en orden de fecha, verde
        nodo["fuentes"][1]["fecha"] = "2026-08-13"
        self.escribir_dataset([nodo])
        self.assertEqual(self.forja("gate")[0], 0)

    def test_a1_vuelta_declarada_en_lista_blanca_pasa(self):
        """A.1: la unica vuelta legitima es el enlace mutuo declarado. Sin
        blanquearla, la vuelta pone el gate en rojo (control); declarada,
        pasa."""
        a = nodo_base("sanear_grafo", nodos_siguientes=["podar_ramas"],
                      nodos_previos=["podar_ramas"])
        b = nodo_base("podar_ramas", nodos_siguientes=["sanear_grafo"],
                      nodos_previos=["sanear_grafo"])
        self.escribir_dataset([a, b])
        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("vuelta", salida)

        # La cita entera, como la exige C.2 desde la v0.3: sin paso_ida ni
        # paso_vuelta seria pertenencia, no cita, y el gate la rechaza.
        comun.agregar_jsonl(self.pares_mutuos, {
            "par": ["sanear_grafo", "podar_ramas"], "fecha": "2026-08-12",
            "declarado_por": "sanear_grafo",
            "paso_ida": 1, "razon_ida": "el vecino despliega mi paso 1",
            "paso_vuelta": 2, "razon_vuelta": "yo despliego su paso 2"})
        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 0, salida)


class PruebaMutuo(BaseForja):
    """Adjudicacion A.1 (docs/BANCO_DE_REGLAS.md): la unica vuelta legitima
    es el ENLACE MUTUO DECLARADO, con su procedimiento de ida y de vuelta
    escritos por separado, a traves de la aduana entera (no solo del gate)."""

    def test_mutuo_declarado_cablea_los_dos_sentidos(self):
        self.sembrar_ejemplo()
        codigo, salida = self.forja(
            "insertar", HIJO, "--sin-preguntas",
            "--veredicto",
            "registrar_fuente_canonica|MUTUO|"
            "ida=3:el vecino despliega entero mi paso 3|"
            "vuelta=2:yo despliego entero su paso 2")
        self.assertEqual(codigo, 0, salida)

        nodos = dict((n["id"], n) for n in self.nodos())
        self.assertIn("elegir_grafia_clave", nodos["registrar_fuente_canonica"]["nodos_siguientes"])
        self.assertIn("elegir_grafia_clave", nodos["registrar_fuente_canonica"]["nodos_previos"])
        self.assertIn("registrar_fuente_canonica", nodos["elegir_grafia_clave"]["nodos_siguientes"])
        self.assertIn("registrar_fuente_canonica", nodos["elegir_grafia_clave"]["nodos_previos"])

        codigo, salida_gate = self.forja("gate")
        self.assertEqual(codigo, 0, salida_gate)

        pares = self.pares()
        self.assertEqual(len(pares), 1)
        self.assertEqual(sorted(pares[0]["par"]),
                         sorted(["registrar_fuente_canonica", "elegir_grafia_clave"]))
        self.assertEqual(pares[0]["declarado_por"], "elegir_grafia_clave")

        bitacora = comun.leer_jsonl(self.veredictos)
        self.assertEqual(bitacora[0]["veredicto"], "MUTUO")
        # la razon del MUTUO nombra las DOS lineas, cada una con su paso
        self.assertIn("ida (paso 3 del candidato)", bitacora[0]["razon"])
        self.assertIn("vuelta (paso 2 del vecino)", bitacora[0]["razon"])

    def test_caso_negativo_mutuo_sin_las_dos_razones_es_rechazado(self):
        """Caso positivo de la guarda inversa: sin ida Y vuelta, MUTUO no
        se acepta a medias."""
        self.sembrar_ejemplo()
        codigo, salida = self.forja(
            "insertar", HIJO, "--sin-preguntas",
            "--veredicto", "registrar_fuente_canonica|MUTUO|ida=3:solo la ida, falta la vuelta")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("MUTUO", salida)
        self.assertEqual(len(self.nodos()), 1)

    def test_caso_control_sin_declarar_el_gate_lo_rechaza(self):
        """Control: la MISMA vuelta escrita a mano, sin pasar por la aduana
        ni por MUTUO, pone el gate en rojo. Confirma que el verde de arriba
        viene del enlace declarado, no de la forma del dato."""
        a = nodo_base("sanear_grafo", nodos_siguientes=["podar_ramas"],
                      nodos_previos=["podar_ramas"])
        b = nodo_base("podar_ramas", nodos_siguientes=["sanear_grafo"],
                      nodos_previos=["sanear_grafo"])
        self.escribir_dataset([a, b])
        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("vuelta", salida)


class PruebaCitaDeLinea(BaseForja):
    """C.1 y C.2 de la TANDA A: el MUTUO cita DOS LINEAS DISTINTAS, y el
    registro de citas se verifica entero. Reglas madre: banco de textos 9.22
    de My-idea y la parada del 2 sep 2026."""

    def _madre_e_hijo(self):
        self.sembrar_ejemplo()
        return json.loads(comun.leer_texto(HIJO))

    def test_c1_mutuo_legitimo_con_dos_lineas_distintas(self):
        self._madre_e_hijo()
        codigo, salida = self.forja(
            "insertar", HIJO, "--sin-preguntas",
            "--veredicto",
            "registrar_fuente_canonica|MUTUO|"
            "ida=5:el vecino despliega entero mi paso 5|"
            "vuelta=2:yo despliego entero su paso 2")
        self.assertEqual(codigo, 0, salida)
        self.assertIn("cita: ida es el paso 5", salida)

        citas = self.pares()
        self.assertEqual(len(citas), 1)
        cita = citas[0]
        for campo in ("fecha", "declarado_por", "paso_ida", "razon_ida",
                      "paso_vuelta", "razon_vuelta", "huella_ida", "huella_vuelta"):
            self.assertIn(campo, cita)
        self.assertEqual(cita["paso_ida"], 5)
        self.assertEqual(cita["paso_vuelta"], 2)
        self.assertEqual(self.forja("gate")[0], 0)

    def test_c1_caso_positivo_solape_disfrazado_cae(self):
        """La misma linea en los dos sentidos NO es enlace mutuo: es solape,
        y se rechaza NOMBRANDO el paso."""
        self._madre_e_hijo()
        hijo = json.loads(comun.leer_texto(HIJO))
        # el paso 7 del hijo pasa a ser LITERALMENTE el paso 4 de la madre
        madre = json.loads(comun.leer_texto(EJEMPLO))
        hijo["pasos_accionables"][6] = madre["pasos_accionables"][3]
        ruta = os.path.join(self.taller, "hijo_disfrazado.json")
        comun.escribir_texto(ruta, json.dumps(hijo, ensure_ascii=False))

        codigo, salida = self.forja(
            "insertar", ruta, "--sin-preguntas",
            "--veredicto",
            "registrar_fuente_canonica|MUTUO|"
            "ida=7:mi paso 7 lo despliega el vecino|"
            "vuelta=4:su paso 4 lo despliego yo")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("SOLAPE DISFRAZADO DE ENLACE MUTUO", salida)
        self.assertIn("ida cita el paso 7", salida)
        self.assertIn("vuelta cita el paso 4", salida)
        self.assertEqual(len(self.nodos()), 1)
        self.assertEqual(self.pares(), [])

    def test_c1_caso_positivo_sin_citar_la_linea_cae(self):
        self._madre_e_hijo()
        codigo, salida = self.forja(
            "insertar", HIJO, "--sin-preguntas",
            "--veredicto",
            "registrar_fuente_canonica|MUTUO|ida=el vecino me despliega|vuelta=yo lo despliego")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("no cita su linea", salida)

    def test_c1_caso_positivo_paso_que_el_nodo_no_tiene(self):
        self._madre_e_hijo()
        codigo, salida = self.forja(
            "insertar", HIJO, "--sin-preguntas",
            "--veredicto",
            "registrar_fuente_canonica|MUTUO|ida=99:no existe|vuelta=2:su paso 2")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("cita un paso que el candidato no tiene", salida)

    def test_c2_par_bidireccional_sin_cita_es_rojo(self):
        """C.2: el gate verifica LA CITA, no la pertenencia."""
        a = nodo_base("sanear_grafo", nodos_siguientes=["podar_ramas"],
                      nodos_previos=["podar_ramas"])
        b = nodo_base("podar_ramas", nodos_siguientes=["sanear_grafo"],
                      nodos_previos=["sanear_grafo"])
        self.escribir_dataset([a, b])
        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("NO TIENE CITA en el registro", salida)
        self.assertIn("UN PAR SIN CITA ES ROJO", salida)

    def test_c2_cita_incompleta_es_rojo_y_la_nombra(self):
        a = nodo_base("sanear_grafo", nodos_siguientes=["podar_ramas"],
                      nodos_previos=["podar_ramas"])
        b = nodo_base("podar_ramas", nodos_siguientes=["sanear_grafo"],
                      nodos_previos=["sanear_grafo"])
        self.escribir_dataset([a, b])
        # la cita de la v0.2: pertenencia con razones, SIN citar linea
        comun.agregar_jsonl(self.pares_mutuos, {
            "par": ["sanear_grafo", "podar_ramas"], "fecha": "2026-09-04",
            "razon_ida": "de prueba", "razon_vuelta": "de prueba",
            "declarado_por": "sanear_grafo"})
        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("cita_incompleta", salida)
        self.assertIn("le falta el campo 'paso_ida'", salida)
        self.assertIn("le falta el campo 'paso_vuelta'", salida)

        # caso positivo: con la cita COMPLETA, el mismo dataset queda verde
        comun.escribir_jsonl(self.pares_mutuos, [{
            "par": ["sanear_grafo", "podar_ramas"], "fecha": "2026-09-04",
            "declarado_por": "sanear_grafo",
            "paso_ida": 1, "razon_ida": "el vecino despliega mi paso 1",
            "paso_vuelta": 2, "razon_vuelta": "yo despliego su paso 2"}])
        self.assertEqual(self.forja("gate")[0], 0)

    def test_c2_cita_que_apunta_hoy_a_la_misma_linea_es_rojo(self):
        """Una cita que era buena deja de serlo si el texto se movio debajo."""
        a = nodo_base("sanear_grafo", nodos_siguientes=["podar_ramas"],
                      nodos_previos=["podar_ramas"])
        b = nodo_base("podar_ramas", nodos_siguientes=["sanear_grafo"],
                      nodos_previos=["sanear_grafo"])
        # hoy el paso 1 de los dos dice lo mismo
        b["pasos_accionables"][0] = a["pasos_accionables"][0]
        self.escribir_dataset([a, b])
        comun.agregar_jsonl(self.pares_mutuos, {
            "par": ["sanear_grafo", "podar_ramas"], "fecha": "2026-09-04",
            "declarado_por": "sanear_grafo",
            "paso_ida": 1, "razon_ida": "x", "paso_vuelta": 1, "razon_vuelta": "y"})
        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("apuntan HOY a la misma linea", salida)


class PruebaVigencia(BaseForja):
    """C.3 de la TANDA A: el bloque de vigencia. Regla madre: los cinco pares
    rancios de OP-D-03 en My-idea (15 ago 2026)."""

    def test_c3_un_veredicto_contra_texto_que_cambio_es_rancio(self):
        self.sembrar_ejemplo()
        codigo, salida = self.forja(
            "insertar", HIJO, "--sin-preguntas",
            "--veredicto",
            "registrar_fuente_canonica|CONTINUA|madre=registrar_fuente_canonica|"
            "el candidato despliega su paso 2")
        self.assertEqual(codigo, 0, salida)

        # caso positivo primero: sin tocar nada, el bloque esta VERDE
        codigo, salida = self.forja("rancios")
        self.assertEqual(codigo, 0, salida)
        self.assertIn("BLOQUE DE VIGENCIA VERDE", salida)

        # ahora una cirugia mueve el texto de la madre bajo los pies
        nodos = self.nodos()
        for nodo in nodos:
            if nodo["id"] == "registrar_fuente_canonica":
                nodo["pasos_accionables"][1] = "Elige la grafia por otro camino distinto."
        self.escribir_dataset(nodos)

        codigo, salida = self.forja("rancios")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("RANCIO", salida)
        self.assertIn("el texto de su vecino 'registrar_fuente_canonica' cambio", salida)
        self.assertIn("NO SE CITA COMO VIGENTE", salida)

    def test_c3_un_veredicto_sin_huella_se_declara_no_se_da_por_bueno(self):
        """Un veredicto de antes del bloque de vigencia no es vigente ni
        rancio: es INCOMPROBABLE, y eso se dice."""
        self.sembrar_ejemplo()
        comun.agregar_jsonl(self.veredictos, {
            "fecha": "2026-08-12", "candidato": "registrar_fuente_canonica",
            "vecino": "registrar_fuente_canonica", "veredicto": "SANO",
            "razon": "escrito antes de que existiera la huella"})
        codigo, salida = self.forja("rancios")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("SIN HUELLA", salida)
        self.assertIn("NO SE PUEDE COMPROBAR", salida)

    def test_c3_la_cita_de_un_mutuo_tambien_envejece(self):
        self.sembrar_ejemplo()
        codigo, salida = self.forja(
            "insertar", HIJO, "--sin-preguntas",
            "--veredicto",
            "registrar_fuente_canonica|MUTUO|ida=5:despliega mi paso 5|"
            "vuelta=2:despliego su paso 2")
        self.assertEqual(codigo, 0, salida)
        self.assertEqual(self.forja("rancios")[0], 0)

        nodos = self.nodos()
        for nodo in nodos:
            if nodo["id"] == "registrar_fuente_canonica":
                nodo["pasos_accionables"][1] = "Otra cosa completamente distinta aqui."
        self.escribir_dataset(nodos)
        codigo, salida = self.forja("rancios")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("linea de vuelta", salida)


class PruebaNoAplica(BaseForja):
    """C.4 de la TANDA A: ninguna señal devuelve cero silencioso. Regla madre:
    la señal muerta de costuras_internas.py que devolvia 0,0 (15 ago 2026)."""

    def test_c4_una_senal_que_no_aplica_revienta_si_se_compara(self):
        from src.aduana import NoAplica, senal_similitud_texto
        medida = senal_similitud_texto("", "un texto cualquiera")
        self.assertIsInstance(medida, NoAplica)
        for comparacion in (lambda: medida >= 0.45, lambda: medida > 0.0,
                            lambda: medida < 1.0, lambda: medida <= 0.5,
                            lambda: float(medida)):
            self.assertRaises(TypeError, comparacion)

    def test_c4_las_tres_senales_declaran_su_dominio(self):
        from src.aduana import NoAplica, senal_familia_id, senal_paso_contra_nodo
        self.assertIsInstance(senal_familia_id("de", "registrar_fuentes"), NoAplica)
        medida, _ = senal_paso_contra_nodo({"pasos_accionables": []},
                                           {"pasos_accionables": ["uno"]})
        self.assertIsInstance(medida, NoAplica)

    def test_c4_medir_declara_en_vez_de_votar(self):
        from src import aduana
        candidato = nodo_base("sanear_grafo")
        vecino = nodo_base("podar_ramas", pasos_accionables=[])
        medicion = aduana.medir(candidato, vecino)
        self.assertIn("NO APLICA", str(medicion["senales"]["paso_contra_nodo"]))
        self.assertNotIn("paso_contra_nodo", medicion["levantada_por"])

    def test_c4_caso_positivo_una_senal_que_si_aplica_sigue_votando(self):
        from src import aduana
        candidato = nodo_base("sanear_grafo")
        vecino = nodo_base("sanear_grafo_gemelo")
        medicion = aduana.medir(candidato, vecino)
        self.assertIsInstance(medicion["senales"]["paso_contra_nodo"], float)
        self.assertIn("paso_contra_nodo", medicion["levantada_por"])


class PruebaDeprecado(BaseForja):
    """D.17 de la TANDA A: EL DEPRECADO ES ARCHIVO, NO SUPERFICIE. Regla
    madre: la decision del fundador de My-idea del 15 ago 2026."""

    def _grafo_con_deprecado(self):
        superviviente = nodo_base("sanear_grafo", ids_alias=["podar_ramas"])
        archivo = nodo_base("podar_ramas", estado="deprecado",
                            nodos_siguientes=["sanear_grafo"])
        return superviviente, archivo

    def test_d17_el_resolutor_camina_del_deprecado_al_superviviente(self):
        from src.resolutor import Resolutor
        superviviente, archivo = self._grafo_con_deprecado()
        resolutor = Resolutor([superviviente, archivo])
        self.assertEqual(resolutor.errores, [])
        self.assertEqual(resolutor.resolver("podar_ramas"), "sanear_grafo")
        self.assertFalse(resolutor.esta_vivo("podar_ramas"))
        self.assertTrue(resolutor.esta_vivo("sanear_grafo"))
        self.assertEqual(resolutor.ids_vivos(), ["sanear_grafo"])

    def test_d17_las_aristas_del_archivo_no_se_reciprocan(self):
        """El deprecado conserva su cableado y eso NO abre un hueco: si sus
        aristas contaran, el superviviente tendria que declararlas de vuelta."""
        superviviente, archivo = self._grafo_con_deprecado()
        self.escribir_dataset([superviviente, archivo])
        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 0, salida)

        # caso positivo: la MISMA arista, con el nodo VIVO, si abre el hueco
        archivo_vivo = dict(archivo)
        archivo_vivo["estado"] = "vivo"
        superviviente_sin_alias = dict(superviviente)
        superviviente_sin_alias["ids_alias"] = []
        self.escribir_dataset([superviviente_sin_alias, archivo_vivo])
        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("arista_incompleta", salida)

    def test_d17_ningun_vivo_nombra_a_un_deprecado(self):
        superviviente, archivo = self._grafo_con_deprecado()
        superviviente["nodos_siguientes"] = ["podar_ramas"]
        self.escribir_dataset([superviviente, archivo])
        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("deprecado_en_superficie", salida)
        self.assertIn("El deprecado es archivo, no participante", salida)

    def test_d17_el_deprecado_no_se_ofrece_como_vecino(self):
        """Un gemelo del candidato que esta DEPRECADO no bloquea: su material
        vivo ya esta en el superviviente."""
        self.sembrar_ejemplo()
        nodos = self.nodos()
        nodos[0]["estado"] = "deprecado"
        nodos.append(nodo_base("sanear_grafo", ids_alias=["registrar_fuente_canonica"]))
        self.escribir_dataset(nodos)
        codigo, salida = self.forja("insertar", self.fixture("gemelo_plantado.json"),
                                    "--sin-preguntas")
        self.assertEqual(codigo, 0, salida)
        self.assertIn("NODO INSERTADO", salida)

    def test_d17_caso_positivo_vivo_si_bloquea(self):
        """El mismo gemelo contra el mismo nodo VIVO si bloquea: la guarda
        distingue el archivo de la superficie, no apaga el bloqueo."""
        self.sembrar_ejemplo()
        codigo, salida = self.forja("insertar", self.fixture("gemelo_plantado.json"),
                                    "--sin-preguntas")
        self.assertEqual(codigo, 2, salida)
        self.assertIn("LA INSERCION QUEDA BLOQUEADA", salida)

    def test_d17_un_candidato_no_puede_declararse_deprecado(self):
        candidato = json.loads(comun.leer_texto(EJEMPLO))
        candidato["estado"] = "deprecado"
        ruta = os.path.join(self.taller, "candidato_deprecado.json")
        comun.escribir_texto(ruta, json.dumps(candidato, ensure_ascii=False))
        codigo, salida = self.forja("insertar", ruta, "--sin-preguntas")
        self.assertEqual(codigo, 0, salida)
        self.assertIn("entra VIVO", salida)
        self.assertEqual(self.nodos()[0]["estado"], "vivo")


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


class PruebaBandejas(BaseForja):
    """El barrido de guiones NO entra en las bandejas de entrada.

    Lo encontro el estreno del 9 sep 2026: al depositar el primer lote, el
    pre-commit se puso en rojo por los guiones del material AJENO que esperaba
    juicio. Barrer la bandeja rompe todo commit mientras hay trabajo en curso, y
    peor, empuja a limpiar un candidato ANTES de que la aduana lo mida.

    La linea es exacta: se barre la raiz de la bandeja, que es doctrina de esta
    casa y viaja en git, y no sus subcarpetas, que son material de otro. Es la
    misma que traza `.gitignore` con `cuarentena/*/` y `fuentes/*/`.
    """

    def _arbol(self, raiz):
        for pieza in ("docs/loop/loop.log", "docs/loop/ultimo_extractor.json",
                      "docs/loop/ultimo_auditor.json", "docs/loop/ACTA_AUDITOR.md",
                      "docs/loop/ultimo_apertura.json",
                      "docs/loop/ultimo_que_nazca_manana.json",
                      "docs/loop/REPORTE.md", "docs/ultimo_disfrazado.json",
                      "cuarentena/LEEME.md", "cuarentena/un_lote/candidato.json",
                      "cuarentena/un_lote/LEEME.md",
                      "cuarentena/_insertados/un_lote/LEEME.md",
                      "cuarentena/_insertados/un_lote/entrado.json",
                      "fuentes/FUENTES_CANONICAS.json", "fuentes/un_libro/cap_01.md",
                      "docs/UN_DOC.md"):
            ruta = os.path.join(raiz, *pieza.split("/"))
            if not os.path.isdir(os.path.dirname(ruta)):
                os.makedirs(os.path.dirname(ruta))
            comun.escribir_texto(ruta, u"texto con guion largo: %s aqui" % GUION_LARGO)

    def test_las_subcarpetas_de_bandeja_no_se_barren(self):
        taller = tempfile.mkdtemp(prefix="bandejas_")
        try:
            self._arbol(taller)
            barridos = set(os.path.relpath(r, taller).replace("\\", "/")
                           for r in comun.archivos_del_repo(taller))
            self.assertIn("docs/UN_DOC.md", barridos)
            # LA RAIZ DE CADA BANDEJA SI: es lo que esta casa escribe.
            self.assertIn("cuarentena/LEEME.md", barridos)
            self.assertIn("fuentes/FUENTES_CANONICAS.json", barridos)
            # EL MATERIAL AJENO NO, aunque este lleno de guiones prohibidos.
            self.assertNotIn("cuarentena/un_lote/candidato.json", barridos)
            self.assertNotIn("fuentes/un_libro/cap_01.md", barridos)
            self.assertNotIn("cuarentena/_insertados/un_lote/entrado.json", barridos)
            # Y EL LEEME DE UN LOTE SI, ESTE DONDE ESTE (D.31): es doctrina de
            # esta casa, viaja en git, y sin esto D.20 tendria una grieta con
            # forma de excusa, un documento propio librandose de la regla por
            # vivir en una carpeta que se salta.
            self.assertIn("cuarentena/un_lote/LEEME.md", barridos)
            self.assertIn("cuarentena/_insertados/un_lote/LEEME.md", barridos)
            # LOS ARTEFACTOS DEL ARNES NO SE BARREN (D.33): son registro de
            # maquina, y el arnes los escribe DESPUES del ultimo commit, asi
            # que son la unica escritura del repo que no pasa por su hook. En
            # la vuelta 7 un guion largo dentro de ultimo_extractor.json puso
            # en rojo la prueba de aceptacion entera.
            for artefacto in ("docs/loop/loop.log", "docs/loop/ultimo_extractor.json",
                              "docs/loop/ultimo_auditor.json"):
                self.assertNotIn(artefacto, barridos)
            # CASO POSITIVO: la prosa del auditor, en la MISMA carpeta, SI se
            # barre. Sin esto, la exclusion podria haberse tragado docs/loop/.
            self.assertIn("docs/loop/ACTA_AUDITOR.md", barridos)
        finally:
            shutil.rmtree(taller, ignore_errors=True)

    def test_d33_se_ensancha_por_patron_y_no_por_lista(self):
        """12 sep 2026, decision del fundador, punto 1.

        La lista cerrada tenia una grieta con forma de fecha:
        `ultimo_apertura.json` nacio con `D.34`, despues de la lista, y en la
        vuelta 20 tres guiones largos del mensaje final de la fase ciega
        tumbaron el barrido Y la prueba de aceptacion. **Formatear la salida de
        un modelo es tarea del arnes, no del modelo.**
        """
        taller = tempfile.mkdtemp(prefix="artefactos_")
        try:
            self._arbol(taller)
            barridos = set(os.path.relpath(r, taller).replace("\\", "/")
                           for r in comun.archivos_del_repo(taller))
            # EL QUE CAUSO LA PARADA, y el que nazca manana sin tocar ninguna lista.
            self.assertNotIn("docs/loop/ultimo_apertura.json", barridos)
            self.assertNotIn("docs/loop/ultimo_que_nazca_manana.json", barridos)
            # CASO POSITIVO, Y ES LA MITAD QUE IMPORTA: la exencion es de CAPA,
            # no de contenido. La prosa de la casa en la MISMA carpeta se barre.
            self.assertIn("docs/loop/ACTA_AUDITOR.md", barridos)
            self.assertIn("docs/loop/REPORTE.md", barridos)
            # Y EL PATRON NO VIAJA: un fichero que solo SE LLAMA asi, fuera de
            # docs/loop/, es prosa de esta casa como cualquier otra.
            self.assertIn("docs/ultimo_disfrazado.json", barridos)
        finally:
            shutil.rmtree(taller, ignore_errors=True)

    def test_el_patron_mira_el_nombre_y_la_carpeta(self):
        self.assertTrue(comun.es_artefacto_de_maquina("ultimo_apertura.json", "docs/loop"))
        self.assertTrue(comun.es_artefacto_de_maquina("loop.log", "docs/loop"))
        self.assertTrue(comun.es_artefacto_de_maquina("ultimo_x.json",
                                                      os.path.join("docs", "loop")))
        # CASO POSITIVO por los dos lados: el nombre solo no basta, y la
        # carpeta sola tampoco.
        self.assertFalse(comun.es_artefacto_de_maquina("ultimo_x.json", "docs"))
        self.assertFalse(comun.es_artefacto_de_maquina("ACTA_AUDITOR.md", "docs/loop"))
        self.assertFalse(comun.es_artefacto_de_maquina("ultimo_x.txt", "docs/loop"))

    def test_la_guarda_del_gate_si_muerde_al_candidato(self):
        """No barrer la bandeja NO es indultar: la puerta sigue mordiendo."""
        from src import guiones
        hallazgos = guiones.barrer_texto(u"un guion largo %s dentro" % GUION_LARGO, "candidato")
        self.assertEqual(len(hallazgos), 1)
        self.assertIn("U+2014", hallazgos[0])


class PruebaReglasDeId(BaseForja):
    """Las dos reglas de id que el fundador reescribio el 10 sep 2026.

    Cada una con su caso positivo, porque una regla que dice siempre que si, o
    siempre que no, no distingue nada.
    """

    def _fallos(self, identificador):
        from src import reglas_id
        return reglas_id.validar(identificador)

    def _texto(self, identificador):
        return " | ".join(self._fallos(identificador))

    # ---- REGLA 1: la negra, la blanca, y los nombres propios ----

    def test_regla1_ingles_con_equivalente_cae(self):
        self.assertIn("palabra inglesa con equivalente",
                      self._texto("customer_retention_tactics"))
        # Y nombra LAS DOS piezas, no solo la primera que encuentra.
        texto = self._texto("customer_retention_tactics")
        self.assertIn("customer", texto)
        self.assertIn("retention", texto)

    def test_regla1_prestamo_asentado_pasa(self):
        """CASO POSITIVO: la blanca indulta, o la regla seria un candado."""
        for identificador in ("plan_marketing_contenidos", "medir_benchmarking_costes",
                              "valorar_startup_temprana", "aplicar_lean_produccion"):
            self.assertEqual(self._fallos(identificador), [],
                             "%s deberia pasar: %s" % (identificador,
                                                       self._texto(identificador)))

    def test_regla1_nombre_propio_no_es_palabra_ajena(self):
        """Un apellido no tiene equivalente en castellano: no se caza."""
        for identificador in ("los_14_puntos_deming", "grafico_shewhart_control",
                              "auditoria_osha_seguridad"):
            self.assertNotIn("palabra inglesa", self._texto(identificador))

    def test_regla1_las_dos_listas_no_se_solapan(self):
        """Si chocan, la regla dejo de tener criterio."""
        from src import reglas_id
        self.assertEqual(reglas_id.INGLES_CON_EQUIVALENTE
                         & reglas_id.PRESTAMOS_ASENTADOS, set())
        self.assertEqual(reglas_id.INGLES_CON_EQUIVALENTE
                         & reglas_id.NOMBRES_Y_SIGLAS, set())

    # ---- REGLA 2: version prohibida, denominacion permitida ----

    def test_regla2_sufijo_de_version_cae(self):
        for identificador in ("accion_correctiva_2", "consejo_calidad_3",
                              "cultura_justa_9"):
            self.assertIn("sufijo numerico de VERSION", self._texto(identificador),
                          identificador)

    def test_regla2_numero_de_denominacion_pasa(self):
        """CASO POSITIVO: los cuatro vivos que la regla vieja tumbaba mal."""
        for identificador in ("familia_normas_iso_9000", "canales_traccion_19",
                              "riesgo_split_51_49"):
            self.assertNotIn("VERSION", self._texto(identificador), identificador)

    def test_regla2_numero_en_medio_nunca_fue_version(self):
        for identificador in ("los_14_puntos_deming", "benchmarking_7_pasos_juran",
                              "programa_mejora_calidad_14_pasos"):
            self.assertNotIn("VERSION", self._texto(identificador), identificador)

    def test_regla2_la_version_cuya_base_vive_la_caza_tambien_la_señal(self):
        """La puerta y la cola dicen lo mismo por caminos distintos.

        `familia()` normaliza los digitos finales, asi que un `_2` y su base
        comparten clave de familia ENTERA. Si la regla 2 alguna vez se
        relajara, la señal 2 seguiria levantando el par.
        """
        from src import reglas_id
        self.assertEqual(reglas_id.familia("accion_correctiva_2"),
                         reglas_id.familia("accion_correctiva"))
        self.assertEqual(
            reglas_id.similitud_familia("accion_correctiva_2", "accion_correctiva"),
            1.0)
        # CASO POSITIVO: dos ids de verdad distintos NO comparten familia.
        self.assertNotEqual(reglas_id.familia("accion_correctiva"),
                            reglas_id.familia("auditoria_producto"))


class PruebaAristaDeclarada(BaseForja):
    """D.29: la arista que la señal NO levanta se declara POR LECTURA.

    Encontrado el 10 sep 2026 al autorizar la primera insercion real. El bucle
    que escribia aristas y bitacora iteraba solo sobre los vecinos que las
    señales levantaron, asi que un veredicto sobre un no vecino se PARSEABA Y SE
    TIRABA: la insercion decia que todo fue bien, el nodo entraba, y ni la arista
    ni la razon escrita se escribian en ninguna parte.

    UN VEREDICTO ACEPTADO EN SILENCIO ES PEOR QUE UNO RECHAZADO, porque el
    rechazo se ve.
    """

    def _pareja_lejana(self):
        """Dos nodos que NINGUNA de las tres señales relaciona."""
        madre = nodo_base(
            "redactar_codigo_comercializacion",
            titulo="Redactar el codigo de comercializacion de la empresa",
            resumen_teorico="La empresa escribe su propio codigo de conducta comercial "
                            "y lo publica para que cualquiera pueda exigirlo.",
            pasos_accionables=[
                "Reune las practicas comerciales que la empresa ya aplica.",
                "Escribe cada practica como una regla que se pueda incumplir.",
                "Publica el codigo donde el comprador pueda leerlo.",
            ])
        hijo = nodo_base(
            "comprobar_veracidad_anuncios",
            titulo="Comprobar la veracidad de un anuncio antes de publicarlo",
            resumen_teorico="Antes de publicar una pieza publicitaria se contrasta cada "
                            "afirmacion suya contra la evidencia que la sostiene.",
            pasos_accionables=[
                "Separa del anuncio cada afirmacion verificable.",
                "Pide para cada una la evidencia que la respalda.",
                "Retira la afirmacion que se quede sin evidencia.",
            ])
        return madre, hijo

    def _insertar(self, nodo, *extra):
        ruta = os.path.join(self.taller, "%s.json" % nodo["id"])
        with io.open(ruta, "w", encoding="utf-8") as fichero:
            json.dump(nodo, fichero, ensure_ascii=False)
        return self.forja("insertar", ruta, "--sin-preguntas", *extra)

    def test_ninguna_señal_levanta_la_pareja(self):
        """El supuesto de la prueba, comprobado y no supuesto."""
        from src import aduana
        madre, hijo = self._pareja_lejana()
        self.assertEqual(aduana.buscar_vecinos(hijo, [madre]), [])

    def test_la_arista_declarada_se_cablea_y_deja_su_razon(self):
        madre, hijo = self._pareja_lejana()
        codigo, salida = self._insertar(madre)
        self.assertEqual(codigo, 0, salida)
        codigo, salida = self._insertar(
            hijo,
            "--veredicto",
            "redactar_codigo_comercializacion|CONTINUA|"
            "madre=redactar_codigo_comercializacion|"
            "el hijo despliega en tres pasos la comprobacion que la madre nombra")
        self.assertEqual(codigo, 0, salida)
        self.assertIn("DECLARADOS POR LECTURA", salida)
        self.assertIn("arista madre-hijo cableada", salida)

        # LA ARISTA, en el dataset y RESUELTA por los dos lados.
        por_id = dict((n["id"], n) for n in self.nodos())
        self.assertIn("comprobar_veracidad_anuncios",
                      por_id["redactar_codigo_comercializacion"]["nodos_siguientes"])
        self.assertIn("redactar_codigo_comercializacion",
                      por_id["comprobar_veracidad_anuncios"]["nodos_previos"])

        # LA RAZON ESCRITA Y LAS SEÑALES REALES, en la bitacora.
        registros = comun.leer_jsonl(self.veredictos)
        declarado = [r for r in registros
                     if r["vecino"] == "redactar_codigo_comercializacion"]
        self.assertEqual(len(declarado), 1, registros)
        registro = declarado[0]
        self.assertEqual(registro["veredicto"], "CONTINUA")
        self.assertEqual(registro["levantada_por"], ["lectura declarada"])
        self.assertIn("despliega", registro["razon"])
        # Y la prueba de que ninguna señal la levanto va DENTRO del registro.
        umbrales = {"similitud_texto": 0.35, "familia_id": 0.30,
                    "paso_contra_nodo": 0.60}
        for nombre, umbral in umbrales.items():
            valor = registro["senales"][nombre]
            self.assertLess(valor, umbral,
                            "%s = %s deberia estar por debajo de %s"
                            % (nombre, valor, umbral))
        self.assertEqual(self.forja("gate")[0], 0)

    def test_caso_positivo_sin_veredicto_no_hay_arista_ni_registro(self):
        """La arista la crea la LECTURA, no la insercion.

        Sin este caso, la prueba de arriba solo demostraria que insertar dos
        nodos los cablea, que seria un defecto y no una virtud.
        """
        madre, hijo = self._pareja_lejana()
        self.assertEqual(self._insertar(madre)[0], 0)
        codigo, salida = self._insertar(hijo)
        self.assertEqual(codigo, 0, salida)
        self.assertNotIn("DECLARADOS POR LECTURA", salida)
        por_id = dict((n["id"], n) for n in self.nodos())
        self.assertEqual(por_id["redactar_codigo_comercializacion"]["nodos_siguientes"], [])
        self.assertEqual(por_id["comprobar_veracidad_anuncios"]["nodos_previos"], [])
        self.assertEqual(comun.leer_jsonl(self.veredictos), [])

    def test_un_veredicto_sobre_un_id_que_no_vive_es_rechazo(self):
        """Antes se tiraba en silencio. Ahora se rechaza nombrandolo."""
        madre, hijo = self._pareja_lejana()
        self.assertEqual(self._insertar(madre)[0], 0)
        codigo, salida = self._insertar(
            hijo, "--veredicto",
            "nodo_que_no_existe|CONTINUA|madre=nodo_que_no_existe|una razon cualquiera")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("no vive", salida)
        self.assertIn("nodo_que_no_existe", salida)
        # Y NO ENTRO: un rechazo no deja mitad del trabajo hecho.
        self.assertEqual([n["id"] for n in self.nodos()],
                         ["redactar_codigo_comercializacion"])

    def test_el_campo_arista_dice_madre_a_hijo_cuando_el_candidato_es_la_MADRE(self):
        """ACTA 16 seccion 8.1: el campo `arista` escribia `X > X`.

        La aduana daba por hecho que el candidato es siempre el HIJO. Cuando el
        candidato es la MADRE, el campo decia `madre > madre` y PERDIA EL NOMBRE
        DEL HIJO, que es justo lo que la guarda `auto_arista` del gate prohibe
        en el dataset. Doce lineas de bitacora quedaron asi (vueltas 12 a 15).

        La prueba mete al candidato en el sitio de la MADRE, que es el caso que
        nadie cubria: la prueba de arriba lo mete siempre de HIJO y por eso
        salia verde con el defecto dentro.
        """
        madre, hijo = self._pareja_lejana()
        # El HIJO entra primero, asi que en la segunda insercion el CANDIDATO
        # es la madre y el VECINO es el hijo. Ese es el caso invertido.
        self.assertEqual(self._insertar(hijo)[0], 0)
        codigo, salida = self._insertar(
            madre,
            "--veredicto",
            "comprobar_veracidad_anuncios|CONTINUA|"
            "madre=redactar_codigo_comercializacion|"
            "la madre nombra en un paso la comprobacion que el hijo despliega")
        self.assertEqual(codigo, 0, salida)

        # LA ARISTA EN EL GRAFO, que es la verdad contra la que se mide.
        por_id = dict((n["id"], n) for n in self.nodos())
        self.assertIn("comprobar_veracidad_anuncios",
                      por_id["redactar_codigo_comercializacion"]["nodos_siguientes"])
        self.assertIn("redactar_codigo_comercializacion",
                      por_id["comprobar_veracidad_anuncios"]["nodos_previos"])

        registros = comun.leer_jsonl(self.veredictos)
        declarado = [r for r in registros
                     if r["vecino"] == "comprobar_veracidad_anuncios"]
        self.assertEqual(len(declarado), 1, registros)
        campo = declarado[0]["arista"]

        # LO QUE CAE CON EL CODIGO VIEJO: escribia
        # `redactar_codigo_comercializacion > redactar_codigo_comercializacion`.
        self.assertEqual(
            campo,
            "redactar_codigo_comercializacion > comprobar_veracidad_anuncios",
            "el campo arista ha de decir madre a hijo, y llego '%s'" % campo)

        # Y LA REGLA GENERAL DETRAS DEL CASO: ningun CONTINUA de la bitacora
        # puede declarar una arista de un nodo a si mismo.
        for registro in registros:
            if registro["veredicto"] != "CONTINUA":
                continue
            extremos = registro["arista"].split(" > ")
            self.assertNotEqual(extremos[0], extremos[-1],
                                "auto arista en la bitacora: %s" % registro["arista"])

    def test_caso_positivo_con_el_candidato_de_HIJO_el_campo_sigue_bien(self):
        """El sentido que ya funcionaba, para que el arreglo no lo rompa.

        Sin este caso, la prueba de arriba solo demostraria que el campo cambio,
        no que cambio en el sentido correcto.
        """
        madre, hijo = self._pareja_lejana()
        self.assertEqual(self._insertar(madre)[0], 0)
        codigo, salida = self._insertar(
            hijo,
            "--veredicto",
            "redactar_codigo_comercializacion|CONTINUA|"
            "madre=redactar_codigo_comercializacion|"
            "el hijo despliega en tres pasos la comprobacion que la madre nombra")
        self.assertEqual(codigo, 0, salida)
        registros = comun.leer_jsonl(self.veredictos)
        declarado = [r for r in registros
                     if r["vecino"] == "redactar_codigo_comercializacion"]
        self.assertEqual(len(declarado), 1, registros)
        self.assertEqual(
            declarado[0]["arista"],
            "redactar_codigo_comercializacion > comprobar_veracidad_anuncios")


class PruebaArchivoDeInsertados(BaseForja):
    """D.31: un candidato insertado se archiva, y el informe deja de contarlo.

    UN CANDIDATO INSERTADO NO SE BORRA: su fichero es el registro de COMO entro.
    Pero deja de ser un candidato, y si el informe lo siguiera contando diria
    CAERIA sobre un nodo que entro bien: un lote recien insertado se leeria como
    un lote entero rechazado.
    """

    def _lote(self, carpeta):
        ruta = os.path.join(self.taller, *carpeta.split("/"))
        os.makedirs(ruta)
        for identificador in ("sanear_grafo", "podar_ramas"):
            with io.open(os.path.join(ruta, "%s.json" % identificador),
                         "w", encoding="utf-8") as fichero:
                json.dump(nodo_base(identificador), fichero, ensure_ascii=False)
        return ruta

    def test_la_carpeta_archivada_no_se_cuenta(self):
        ruta = self._lote("cuarentena/_insertados/un_libro")
        codigo, salida = self.forja("informe", "--carpeta", ruta)
        self.assertEqual(codigo, 0, salida)
        self.assertIn("2 ficheros ARCHIVADOS", salida)
        self.assertNotIn("EL SALDO", salida)

    def test_caso_positivo_la_misma_carpeta_sin_archivar_si_se_cuenta(self):
        """Sin esto, la prueba de arriba solo probaria que el informe calla."""
        ruta = self._lote("cuarentena/un_libro")
        codigo, salida = self.forja("informe", "--carpeta", ruta)
        self.assertEqual(codigo, 0, salida)
        self.assertIn("candidatos revisados        : 2", salida)
        self.assertIn("EL SALDO", salida)

    def test_un_lote_mezclado_declara_cuantos_no_conto(self):
        """Lo peligroso no es no contarlos: es no contarlos EN SILENCIO."""
        from src import informe
        vivos = self._lote("cuarentena/un_libro")
        archivados = self._lote("cuarentena/_insertados/un_libro")
        rutas = ([os.path.join(vivos, f) for f in sorted(os.listdir(vivos))]
                 + [os.path.join(archivados, f) for f in sorted(os.listdir(archivados))])
        # bandejas=[] porque esta prueba mide el RECORTE de _insertados, no la
        # poblacion: sin esto miraria las bandejas del repo de verdad y su
        # resultado dependeria de en que vuelta se corra.
        dictamenes, cuantos, umbrales, fuera = informe.revisar(
            rutas, ruta_dataset=self.dataset, bandejas=[],
            tabla_fuentes=comun.leer_json(self.fuentes_tabla))
        self.assertEqual(len(dictamenes), 2)
        self.assertEqual(len(fuera), 2)
        texto = informe.texto_informe(dictamenes, cuantos, umbrales, archivados=fuera)
        self.assertIn("archivados, NO contados     : 2", texto)

    def test_la_marca_es_el_segmento_de_ruta_no_el_nombre(self):
        from src import informe
        self.assertTrue(informe.esta_archivado("cuarentena/_insertados/libro/x.json"))
        self.assertTrue(informe.esta_archivado(
            "cuarentena" + os.sep + "_insertados" + os.sep + "libro" + os.sep + "x.json"))
        # CASO POSITIVO: un fichero que solo SE LLAMA asi no esta archivado.
        self.assertFalse(informe.esta_archivado("cuarentena/libro/_insertados.json"))
        self.assertFalse(informe.esta_archivado("cuarentena/libro/x.json"))


class PruebaAristaDeclarada37(BaseForja):
    """D.37: la serie declarada por el titulo es arista POR LECTURA.

    La aduana solo cablea aristas EN EL ACTO DE INSERTAR. Para dos nodos que ya
    viven no habia camino, y escribir a mano en el dataset esta prohibido
    siempre. Esta es la operacion, con su simulacion sobre copia en memoria y su
    caso positivo (manual seccion 5).
    """

    def _cabeza_y_parte(self):
        # LOS DOS TEXTOS SE SEPARAN A PROPOSITO. El caso que D.37 existe para
        # cubrir es aquel en que NINGUNA señal levanta el par: si la cabeza y la
        # parte se parecieran, la aduana ya los habria juntado sola y esta
        # operacion no haria falta.
        cabeza = nodo_base(
            "abastecer_flujo_candidatos",
            titulo="Abastecerse de candidatos, con sus tres vias",
            resumen_teorico="El flujo se llena antes de que haya plazas abiertas, "
                            "y el libro abre tres puertas distintas para llenarlo.",
            condiciones_activacion="Cuando el embudo esta vacio y todavia no urge.",
            entregable_esperado="Una lista viva de nombres con su procedencia.",
            pasos_accionables=[
                "Referencias de tus redes: haz una lista de las personas mas talentosas.",
                "Referencias de tus empleados: pide a tu equipo que traiga nombres.",
                "Contratar reclutadores: usa el metodo para contratar reclutadores.",
            ])
        parte = nodo_base(
            "pedir_referencias_empleados",
            titulo="Pedir referencias a tus propios empleados",
            resumen_teorico="Convertir a la plantilla en antena permanente exige "
                            "premiar el gesto y pedirle cuentas, no solo animarlo.",
            condiciones_activacion="Cuando el equipo ya conoce gente que vale.",
            entregable_esperado="Nombres traidos por la plantilla, con su prima pagada.",
            pasos_accionables=[
                "Mete el abastecimiento como resultado en la tarjeta del equipo.",
                "Anima a tus empleados a preguntar en sus redes.",
                "Ofrece una prima por referencia.",
            ])
        return cabeza, parte

    def _declarar(self, *extra):
        return self.forja("arista", *extra)

    def test_la_arista_se_declara_y_deja_su_paso_citado(self):
        cabeza, parte = self._cabeza_y_parte()
        self.escribir_dataset([cabeza, parte])
        codigo, salida = self._declarar(
            "--madre", "abastecer_flujo_candidatos",
            "--hijo", "pedir_referencias_empleados",
            "--paso", "2",
            "--razon", "el paso 2 de la madre nombra la via en una linea y el hijo "
                       "la despliega en tres pasos")
        self.assertEqual(codigo, 0, salida)
        self.assertIn("ARISTA ESCRITA RESUELTA", salida)
        self.assertIn("NINGUNA SEÑAL LA LEVANTA", salida)

        por_id = dict((n["id"], n) for n in self.nodos())
        self.assertIn("pedir_referencias_empleados",
                      por_id["abastecer_flujo_candidatos"]["nodos_siguientes"])
        self.assertIn("abastecer_flujo_candidatos",
                      por_id["pedir_referencias_empleados"]["nodos_previos"])

        registro = comun.leer_jsonl(self.veredictos)[-1]
        self.assertEqual(registro["veredicto"], "CONTINUA")
        self.assertEqual(registro["levantada_por"], ["lectura declarada"])
        self.assertEqual(registro["paso_citado"], 2)
        # LA LINEA CITADA VIAJA ENTERA: es lo que el auditor abre para verificar.
        self.assertIn("Referencias de tus empleados", registro["texto_citado"])
        self.assertEqual(self.forja("gate")[0], 0)

    def test_caso_positivo_un_paso_que_la_madre_no_tiene_es_rechazo(self):
        """Sin esto, la prueba de arriba solo probaria que el comando escribe."""
        cabeza, parte = self._cabeza_y_parte()
        self.escribir_dataset([cabeza, parte])
        codigo, salida = self._declarar(
            "--madre", "abastecer_flujo_candidatos",
            "--hijo", "pedir_referencias_empleados",
            "--paso", "9",
            "--razon", "una razon cualquiera")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("el paso citado no existe", salida)
        # Y NO ESCRIBIO NADA: un rechazo no deja media arista.
        por_id = dict((n["id"], n) for n in self.nodos())
        self.assertEqual(por_id["abastecer_flujo_candidatos"]["nodos_siguientes"], [])
        self.assertEqual(comun.leer_jsonl(self.veredictos), [])

    def test_sin_razon_escrita_no_se_declara(self):
        cabeza, parte = self._cabeza_y_parte()
        self.escribir_dataset([cabeza, parte])
        codigo, salida = self._declarar(
            "--madre", "abastecer_flujo_candidatos",
            "--hijo", "pedir_referencias_empleados",
            "--paso", "2", "--razon", "   ")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("sin razon escrita", salida)

    def test_un_extremo_que_no_vive_es_rechazo(self):
        cabeza, parte = self._cabeza_y_parte()
        self.escribir_dataset([cabeza, parte])
        codigo, salida = self._declarar(
            "--madre", "abastecer_flujo_candidatos",
            "--hijo", "nodo_que_no_existe", "--paso", "2",
            "--razon", "una razon cualquiera")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("no vive en el grafo", salida)

    def test_la_auto_arista_es_rechazo(self):
        cabeza, parte = self._cabeza_y_parte()
        self.escribir_dataset([cabeza, parte])
        codigo, salida = self._declarar(
            "--madre", "abastecer_flujo_candidatos",
            "--hijo", "abastecer_flujo_candidatos", "--paso", "1",
            "--razon", "una razon cualquiera")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("auto arista", salida)

    def test_declararla_dos_veces_es_rechazo(self):
        cabeza, parte = self._cabeza_y_parte()
        self.escribir_dataset([cabeza, parte])
        argumentos = ("--madre", "abastecer_flujo_candidatos",
                      "--hijo", "pedir_referencias_empleados", "--paso", "2",
                      "--razon", "el paso 2 la nombra y el hijo la despliega")
        self.assertEqual(self._declarar(*argumentos)[0], 0)
        codigo, salida = self._declarar(*argumentos)
        self.assertEqual(codigo, 1, salida)
        self.assertIn("ya esta declarada", salida)
        # Y NO SE DUPLICO en el dataset.
        por_id = dict((n["id"], n) for n in self.nodos())
        self.assertEqual(por_id["abastecer_flujo_candidatos"]["nodos_siguientes"],
                         ["pedir_referencias_empleados"])

    def test_la_simulacion_del_gate_manda_y_no_escribe_si_sale_roja(self):
        """La vuelta que el gate no admite no llega al dataset.

        Se declara A > B y despues B > A: la segunda cierra una vuelta, el gate
        la caza sobre la copia en memoria, y el dataset queda como estaba.
        """
        cabeza, parte = self._cabeza_y_parte()
        self.escribir_dataset([cabeza, parte])
        self.assertEqual(self._declarar(
            "--madre", "abastecer_flujo_candidatos",
            "--hijo", "pedir_referencias_empleados", "--paso", "2",
            "--razon", "el paso 2 la nombra y el hijo la despliega")[0], 0)
        antes = self.nodos()
        codigo, salida = self._declarar(
            "--madre", "pedir_referencias_empleados",
            "--hijo", "abastecer_flujo_candidatos", "--paso", "1",
            "--razon", "la vuelta que el gate tiene que cazar")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("RECHAZADO POR EL GATE", salida)
        self.assertIn("NADA SE ESCRIBIO", salida)
        self.assertEqual(self.nodos(), antes)


class PruebaSedeVacia(BaseForja):
    """5.7: la sede de los pares mutuos NACE VACIA, con su cabecera.

    Una sede que NO EXISTE y una sede VACIA se parecen demasiado, y no son lo
    mismo: la primera hace dudar de si el protocolo la lee. El fichero nace con
    una linea que dice que es, y esa linea NO es una cita.
    """

    def _cabecera(self):
        return ('{"_lea_esto": "registro de citas de enlace mutuo", '
                '"_estado": "VACIO, ninguna cita declarada todavia"}')

    def test_la_cabecera_no_cuenta_como_cita(self):
        from src import config as modulo_config
        comun.escribir_texto(self.pares_mutuos, self._cabecera() + "\n")
        self.assertEqual(modulo_config.cargar_pares_mutuos(self.pares_mutuos), [])

    def test_caso_positivo_una_cita_de_verdad_SI_cuenta(self):
        """Sin esto, el salto podria estarse tragando el fichero entero."""
        from src import config as modulo_config
        cita = ('{"par": ["uno", "otro"], "paso_ida": 2, "paso_vuelta": 5, '
                '"huella_ida": "aa", "huella_vuelta": "bb"}')
        comun.escribir_texto(self.pares_mutuos,
                             self._cabecera() + "\n" + cita + "\n")
        citas = modulo_config.cargar_pares_mutuos(self.pares_mutuos)
        self.assertEqual(len(citas), 1)
        self.assertEqual(citas[0]["par"], ["uno", "otro"])

    def test_el_gate_y_la_vigencia_no_tropiezan_con_la_cabecera(self):
        """La averia que este salto evita: un fallo cantado sobre una linea
        que no es un par."""
        comun.escribir_texto(self.pares_mutuos, self._cabecera() + "\n")
        self.escribir_dataset([nodo_base("sanear_grafo")])
        codigo, salida = self.forja("gate")
        self.assertEqual(codigo, 0, salida)
        codigo, salida = self.forja("rancios")
        self.assertEqual(codigo, 0, salida)
        self.assertIn("citas de enlace mutuo comprobadas: 0", salida)


class PruebaHerencia(BaseForja):
    """D.40: lo que un auditor le deja al siguiente lo entrega el arnes.

    Tres actas seguidas perdieron el mismo remedio por tener que ir a buscarlo a un
    fichero de dieciseis mil lineas. Un remedio que hay que acordarse de ir a buscar
    no esta entregado: esta archivado.
    """

    # EL FIXTURE LLEVA LAS CUATRO TRAMPAS QUE EL ACTA REAL LLEVA, y es deliberado
    # (16 sep 2026, TAREA 2 de la vuelta 31): una acta VIEJA con su tabla, una
    # seccion que solo MENCIONA la palabra, una tabla CITADA dentro de un bloque de
    # cita, y una tabla que HABLA de remedios sin escribirlos. Solo la tabla que el
    # acta ESCRIBE se hereda.
    ACTA = """# ACTA 8. una vuelta vieja

### 7.3. MI REMEDIO DE LA VUELTA VIEJA
Esto no se hereda: no es la ultima acta.

| # | **REMEDIO** | como se comprueba que se cumplio |
|---:|---|---|
| **1** | EL REMEDIO DE LA VUELTA VIEJA, QUE NO VIAJA | de una acta que ya no es la ultima |

# ACTA 9. la ultima

## 7. MIS CAIDAS

> ### **TAREA BLOQUEANTE DEL AUDITOR DE LA VUELTA 10, ESCRITA POR EL AUDITOR DE LA 9**
>
> Pega el instrumento al lado de cada cifra.

### 7.4. EL REMEDIO QUE SI CUMPLI, Y AQUI SOLO LO CITO
Esta seccion MENCIONA el remedio de la ACTA 8 para decir que aguanto. Citar no es
escribir, asi que NO SE HEREDA: es la caida que costo la ACTA 29 8.1.

> | # | **REMEDIO** | como se comprueba que se cumplio |
> |---:|---|---|
> | **1** | LA TABLA COPIADA DENTRO DE UNA CITA ESTA CITADA, NO ESCRITA | y por eso no se entrega |

## 8. MIS REMEDIOS PARA EL SIGUIENTE

| # | **REMEDIO** | como se comprueba que se cumplio |
|---:|---|---|
| **1** | PEGA EL INSTRUMENTO AL LADO DE CADA CIFRA | que cada cifra lleve su salida debajo |

## 9. LA ESCALADA SE ENCARGA

| lo que detecto | el remedio autorizado | donde lo encargo |
|---|---|---|
| una tabla que HABLA de remedios | D.40, ya escrita | TAREA 2 |

## 10. OTRA COSA
Esto ya no pertenece al remedio anterior.
"""

    ACTA_SIN_TABLA = """# ACTA 11. la que nombra remedios y no escribe ninguno

### 8.1. EL REMEDIO QUE ROMPI
Solo lo menciono. No pongo tabla.

### 8.2. OTRO REMEDIO QUE CITO
Tampoco.
"""

    def _acta(self, texto=None):
        ruta = os.path.join(self.taller, "ACTA_AUDITOR.md")
        comun.escribir_texto(ruta, texto if texto is not None else self.ACTA)
        return ruta

    def _apertura(self, texto):
        ruta = os.path.join(self.taller, "APERTURA_CIEGA.md")
        comun.escribir_texto(ruta, texto)
        return ruta

    def test_hereda_solo_de_la_ultima_acta(self):
        datos = herencia.extraer(self._acta())
        self.assertEqual([i["clase"] for i in datos["items"]],
                         ["TAREA BLOQUEANTE", "REMEDIO"])
        cuerpos = "\n".join("\n".join(i["cuerpo"]) for i in datos["items"])
        self.assertIn("VUELTA 10", cuerpos)
        # CASO POSITIVO DEL CORTE: el remedio de la acta VIEJA no viaja, y la
        # seccion que no nombra ningun remedio tampoco. Un extractor que se
        # trajese el fichero entero no estaria entregando nada.
        self.assertNotIn("vuelta vieja", cuerpos)
        self.assertNotIn("OTRA COSA", cuerpos)
        self.anotar("D40", "herencia: 2 items de la ultima acta, 0 de las viejas")

    def test_el_prompt_lleva_el_texto_y_lo_que_exige(self):
        datos = herencia.extraer(self._acta())
        texto = herencia.texto_para_prompt(datos)
        self.assertIn("REMEDIOS PENDIENTES QUE HEREDAS", texto)
        self.assertIn("TAREA BLOQUEANTE DEL AUDITOR DE LA VUELTA 10", texto)
        self.assertIn("Pega el instrumento", texto)
        self.assertIn("ACTA ANTERIOR LEIDA: %s" % datos["huella"], texto)
        self.assertIn("HEREDADO 1:", texto)
        self.assertIn("HEREDADO 2:", texto)

    def test_una_apertura_completa_pasa(self):
        datos = herencia.extraer(self._acta())
        ruta = self._apertura(
            "clases y lecturas, sin cifras contadas a mano (D.38.3)\n"
            "ACTA ANTERIOR LEIDA: %s\n"
            "HEREDADO 1: CUMPLIDO\n"
            "HEREDADO 2: NO APLICA porque esta vuelta no publica cifras ajenas\n"
            "    $ el comando que lo sostiene   ->  (su salida)\n"
            % datos["huella"])
        self.assertEqual(herencia.comprobar(datos, ruta), [])

    def test_caso_positivo_la_apertura_que_no_declara_se_caza(self):
        """Sin esto, la guarda podria estar diciendo siempre que si."""
        datos = herencia.extraer(self._acta())
        faltan = herencia.comprobar(datos, self._apertura("clases y lecturas, y nada mas\n"))
        self.assertEqual(len(faltan), 3)
        self.assertIn("ACTA ANTERIOR LEIDA", faltan[0])
        self.assertIn("HEREDADO 1", faltan[1])
        self.assertIn("HEREDADO 2", faltan[2])
        self.anotar("D40_positivo", "apertura sin declarar: 3 faltas nombradas")

    def test_otra_huella_no_cuela(self):
        """Decir que se leyo OTRA version del acta no es haberla leido."""
        datos = herencia.extraer(self._acta())
        faltan = herencia.comprobar(datos, self._apertura(
            "ACTA ANTERIOR LEIDA: 0000000000000000000000000000000000000000\n"
            "HEREDADO 1: CUMPLIDO\nHEREDADO 2: CUMPLIDO\n"))
        self.assertEqual(len(faltan), 1)
        self.assertIn("otra huella", faltan[0])

    def test_no_aplica_sin_motivo_es_lo_mismo_que_perderlo(self):
        datos = herencia.extraer(self._acta())
        faltan = herencia.comprobar(datos, self._apertura(
            "ACTA ANTERIOR LEIDA: %s\nHEREDADO 1: NO APLICA\nHEREDADO 2: CUMPLIDO\n"
            % datos["huella"]))
        self.assertEqual(len(faltan), 1)
        self.assertIn("SIN MOTIVO", faltan[0])

    # ---------------------------------------------------------------- 12 sep 2026
    # LA GUARDA ERA MAS ESTRICTA QUE LA LETRA, y la vuelta 19 lo pago: su apertura
    # declaro las dos lineas, con la huella exacta, y cayo por escribirlas en el
    # markdown de la casa. Lo que sigue fija que se comprueba PRESENCIA.

    APERTURA_DE_LA_19 = """## 0. LO QUE HEREDO

> ### **ACTA ANTERIOR LEIDA: `%s`**

### `HEREDADO 1`: **CUMPLIDO**

El arnes me entrega como `HEREDADO 1` la seccion 7.6 del acta anterior.

| **herencia `D.40`** | **`HEREDADO 1`: CUMPLIDO**, fila a fila |
"""

    def test_la_apertura_escrita_en_markdown_de_la_casa_pasa(self):
        """CASO NEGATIVO. Es la apertura real de la vuelta 19, que la guarda tumbo."""
        datos = herencia.extraer(self._acta())
        ruta = self._apertura((self.APERTURA_DE_LA_19 % datos["huella"])
                              + "\nHEREDADO 2: NO APLICA porque no hay cifras ajenas\n"
                              + "    $ el comando que lo sostiene -> (su salida)\n")
        self.assertEqual(herencia.comprobar(datos, ruta), [])

    def test_citar_dos_veces_la_linea_que_declaras_no_tumba_la_vuelta(self):
        """CASO NEGATIVO. El remedio viejo pedia `grep -c` igual a 1, y la propia
        apertura lo rompia al repetir su declaracion en la tabla de cierre."""
        datos = herencia.extraer(self._acta())
        ruta = self._apertura(
            "ACTA ANTERIOR LEIDA: %s\nHEREDADO 1: CUMPLIDO\n"
            "HEREDADO 2: NO APLICA porque esta vuelta no publica cifras ajenas\n"
            "    $ el comando que lo sostiene   ->  (su salida)\n"
            "\n## tabla de cierre\n"
            "| herencia | ACTA ANTERIOR LEIDA: %s, HEREDADO 1: CUMPLIDO |\n"
            % (datos["huella"], datos["huella"]))
        self.assertEqual(herencia.comprobar(datos, ruta), [])

    def test_una_huella_corta_sigue_siendo_la_misma_huella(self):
        datos = herencia.extraer(self._acta())
        ruta = self._apertura("ACTA ANTERIOR LEIDA: `%s`\nHEREDADO 1: CUMPLIDO\n"
                              "HEREDADO 2: CUMPLIDO\n" % datos["huella"][:10])
        self.assertEqual(herencia.comprobar(datos, ruta), [])

    def test_caso_positivo_el_adorno_no_es_una_puerta_trasera(self):
        """Quitar el adorno afloja el FORMATO, no la EXIGENCIA: sin declaracion,
        por muy bien maquetada que este la apertura, sigue cayendo."""
        datos = herencia.extraer(self._acta())
        ruta = self._apertura(
            "## 0. LO QUE HEREDO\n\n> ### **LEI EL ACTA, DE VERDAD**\n\n"
            "### `HEREDADO 1`: **lo mire por encima**\n")
        faltan = herencia.comprobar(datos, ruta)
        self.assertEqual(len(faltan), 3)
        self.assertIn("ACTA ANTERIOR LEIDA", faltan[0])

    def test_caso_positivo_una_huella_ajena_decorada_tampoco_cuela(self):
        datos = herencia.extraer(self._acta())
        ruta = self._apertura("> **ACTA ANTERIOR LEIDA: `deadbeefdeadbeef`**\n"
                              "### `HEREDADO 1`: **CUMPLIDO**\n"
                              "### `HEREDADO 2`: **CUMPLIDO**\n")
        faltan = herencia.comprobar(datos, ruta)
        self.assertEqual(len(faltan), 1)
        self.assertIn("otra huella", faltan[0])

    def test_no_aplica_sin_motivo_en_una_cita_y_con_motivo_en_otra_pasa(self):
        """PRESENCIA: basta con que UNA de las veces este bien puesta."""
        datos = herencia.extraer(self._acta())
        ruta = self._apertura(
            "ACTA ANTERIOR LEIDA: %s\n"
            "| resumen | HEREDADO 1: NO APLICA |\n"
            "HEREDADO 1: NO APLICA porque esta vuelta no toca esa sede\n"
            "    $ el comando que lo sostiene   ->  (su salida)\n"
            "HEREDADO 2: CUMPLIDO\n" % datos["huella"])
        self.assertEqual(herencia.comprobar(datos, ruta), [])

    def test_caso_positivo_un_NO_APLICA_sin_salida_pegada_no_lo_acepta_el_sello(self):
        """D.40 ensanchada el 16 sep 2026, punto 2.a de la decision.

        La vuelta 26 declaro `NO APLICA` un heredado con el motivo de que ninguno de
        sus instrumentos escribia en el arbol. **Seis escribian, su propia tabla los
        listaba, y el barrido de guiones estaba en ROJO con ocho hallazgos suyos.**
        `D.40` exigia motivo y el motivo estaba escrito: exigia que lo hubiera, **no
        que fuera cierto.**
        """
        datos = herencia.extraer(self._acta())
        ruta = self._apertura(
            "ACTA ANTERIOR LEIDA: %s" % datos["huella"] + chr(10) +
            "HEREDADO 1: NO APLICA porque ninguno de mis instrumentos escribe" + chr(10) +
            "HEREDADO 2: CUMPLIDO" + chr(10))
        faltan = herencia.comprobar(datos, ruta)
        self.assertEqual(len(faltan), 1)
        self.assertIn("SIN LA SALIDA DEL INSTRUMENTO PEGADA", faltan[0])
        self.anotar("D40_salida", "NO APLICA sin salida pegada: cazado")

    def test_caso_negativo_con_la_salida_pegada_debajo_pasa(self):
        datos = herencia.extraer(self._acta())
        ruta = self._apertura(
            "ACTA ANTERIOR LEIDA: %s" % datos["huella"] + chr(10) +
            "HEREDADO 1: NO APLICA porque ninguno de mis instrumentos escribe" + chr(10) +
            "    $ grep -l open( .v27/*.py    ->  (ninguno)" + chr(10) +
            "HEREDADO 2: CUMPLIDO" + chr(10))
        self.assertEqual(herencia.comprobar(datos, ruta), [])

    def test_la_salida_pegada_se_busca_en_el_markdown_de_la_casa(self):
        """El auditor escribe en markdown, con cita y negrita."""
        datos = herencia.extraer(self._acta())
        ruta = self._apertura(
            "> ### **ACTA ANTERIOR LEIDA: `%s`**" % datos["huella"] + chr(10) +
            "> ### `HEREDADO 1`: **NO APLICA**, porque esta vuelta no toca esa sede" + chr(10) +
            ">" + chr(10) +
            ">     $ ls .v27/*.py    ->  (ninguno)" + chr(10) +
            "### `HEREDADO 2`: **CUMPLIDO**" + chr(10))
        self.assertEqual(herencia.comprobar(datos, ruta), [])

    def test_caso_positivo_una_salida_lejos_no_cuenta_como_suya(self):
        """Pegada quiere decir DEBAJO, no en algun sitio del documento."""
        datos = herencia.extraer(self._acta())
        lejos = chr(10).join(["relleno que separa"] * 20)
        ruta = self._apertura(
            "ACTA ANTERIOR LEIDA: %s" % datos["huella"] + chr(10) +
            "HEREDADO 1: NO APLICA porque no toca" + chr(10) + lejos + chr(10) +
            "    $ un comando que no es suyo" + chr(10) +
            "HEREDADO 2: CUMPLIDO" + chr(10))
        faltan = herencia.comprobar(datos, ruta)
        self.assertEqual(len(faltan), 1)
        self.assertIn("SIN LA SALIDA", faltan[0])

    def test_un_CUMPLIDO_no_necesita_salida_pegada(self):
        """La exigencia es del NO APLICA: es la excusa, no el cumplimiento."""
        datos = herencia.extraer(self._acta())
        ruta = self._apertura(
            "ACTA ANTERIOR LEIDA: %s" % datos["huella"] + chr(10) +
            "HEREDADO 1: CUMPLIDO" + chr(10) + "HEREDADO 2: CUMPLIDO" + chr(10))
        self.assertEqual(herencia.comprobar(datos, ruta), [])

    # ------------------------------------------------------------ 16 sep 2026
    # EL ARNES ENTREGA LOS REMEDIOS QUE EL ACTA ESCRIBE, NO LOS QUE CITA.
    # TAREA 2 de la vuelta 31, encargada por la ACTA 29 8.1 con su caida delante:
    # el auditor rompio en su apertura sellada el REMEDIO 1 que el mismo habia
    # escrito **porque el arnes no se lo entrego**, y se lo cargo igualmente.

    def test_caso_positivo_una_seccion_que_solo_menciona_la_palabra_no_se_hereda(self):
        """LA PRUEBA QUE CAZA A LA REGLA VIEJA. Falla si el extractor vuelve a
        quedarse con una seccion cuyo encabezado nombra un remedio sin escribirlo.
        """
        datos = herencia.extraer(self._acta())
        cuerpos = chr(10).join(chr(10).join(i["cuerpo"]) for i in datos["items"])
        self.assertNotIn("SOLO LO CITO", cuerpos)
        self.assertNotIn("Citar no es", cuerpos)
        remedios = [i for i in datos["items"] if i["clase"] == "REMEDIO"]
        self.assertEqual(len(remedios), 1)
        self.assertIn("PEGA EL INSTRUMENTO AL LADO DE CADA CIFRA",
                      chr(10).join(remedios[0]["cuerpo"]))
        self.anotar("D40_escribe", "herencia: la seccion que solo cita no se hereda")

    def test_caso_positivo_una_tabla_citada_no_se_entrega(self):
        """Un acta que copia la tabla de la anterior dentro de una cita la esta
        CITANDO, que es justo lo que no se entrega."""
        datos = herencia.extraer(self._acta())
        cuerpos = chr(10).join(chr(10).join(i["cuerpo"]) for i in datos["items"])
        self.assertNotIn("DENTRO DE UNA CITA", cuerpos)

    def test_caso_positivo_una_tabla_que_habla_de_remedios_no_es_la_que_los_escribe(self):
        """La ACTA 29 9.4 pone `| lo que detecto | el remedio autorizado | ... |`.
        Es una tabla SOBRE remedios, no la que los escribe."""
        datos = herencia.extraer(self._acta())
        cuerpos = chr(10).join(chr(10).join(i["cuerpo"]) for i in datos["items"])
        self.assertNotIn("el remedio autorizado", cuerpos)
        self.assertNotIn("LA ESCALADA SE ENCARGA", cuerpos)

    def test_la_tabla_de_una_acta_vieja_no_viaja(self):
        datos = herencia.extraer(self._acta())
        cuerpos = chr(10).join(chr(10).join(i["cuerpo"]) for i in datos["items"])
        self.assertNotIn("QUE NO VIAJA", cuerpos)

    def test_si_el_acta_nombra_remedios_y_no_escribe_tabla_se_dice_en_voz_alta(self):
        """Un arnes que entrega cero sin avisar es el mismo defecto por detras."""
        datos = herencia.extraer(self._acta(self.ACTA_SIN_TABLA))
        self.assertEqual([i for i in datos["items"] if i["clase"] == "REMEDIO"], [])
        self.assertTrue(datos["avisos"])
        self.assertIn("MENCIONA remedios", datos["avisos"][0])
        self.assertIn("MENCIONA remedios", herencia.texto_para_prompt(datos))

    def test_el_acta_se_elige_por_su_numero_y_no_por_los_que_su_titulo_cita(self):
        """Cazado al probar la TAREA 2: el titulo de la ACTA 29 nombra dentro a la
        28 y a la 27, asi que buscar el texto suelto devolvia siempre la ultima."""
        ruta = self._acta("# ACTA 12. una que cita a la ACTA 13 en su titulo" + chr(10)
                          + chr(10) + "## 1. nada" + chr(10) + chr(10)
                          + "# ACTA 13. la ultima" + chr(10) + chr(10)
                          + "## 1. nada" + chr(10))
        self.assertIn("ACTA 12", herencia._acta_pedida(
            comun.leer_texto(ruta).split(chr(10)), "ACTA 12")[2])
        self.assertIn("ACTA 13", herencia._acta_pedida(
            comun.leer_texto(ruta).split(chr(10)), "ACTA 13")[2])

    def test_caso_positivo_sobre_el_acta_real_de_esta_casa(self):
        """CASO POSITIVO OBLIGATORIO de la TAREA 2.c, sobre el acta de verdad.

        Una guarda que solo se prueba contra un fixture que yo mismo escribo no
        esta probada contra el caso que la hizo falta.
        """
        if not os.path.exists(herencia.RUTA_ACTA):
            self.skipTest("esta casa todavia no tiene acta")
        esperado = {"ACTA 27": 2, "ACTA 28": 4, "ACTA 29": 3}
        for nombre, cuantos in sorted(esperado.items()):
            datos = herencia.extraer(seleccion=nombre)
            remedios = [i for i in datos["items"] if i["clase"] == "REMEDIO"]
            self.assertEqual(len(remedios), cuantos,
                             "%s tendria que entregar %d remedios y entrega %d"
                             % (nombre, cuantos, len(remedios)))
            cuerpos = chr(10).join(chr(10).join(i["cuerpo"]) for i in remedios)
            # LAS DOS SECCIONES QUE LA REGLA VIEJA ENTREGABA, NOMBRADAS.
            self.assertNotIn("### 3.2.", cuerpos)
            self.assertNotIn("### 6.1.", cuerpos)
        self.anotar("D40_real", "herencia sobre el acta real: 2, 4 y 3 remedios")

    def test_sin_acta_no_revienta_y_la_linea_de_lectura_sigue_en_pie(self):
        """La primera vuelta de una casa no tiene acta anterior."""
        datos = herencia.extraer(os.path.join(self.taller, "no_existe.md"))
        self.assertEqual(datos["items"], [])
        self.assertIn("no dejo ninguna tarea bloqueante",
                      herencia.texto_para_prompt(datos))
        # No hay heredados, pero la declaracion de haber mirado el acta no se
        # ahorra: es la unica prueba de que se miro.
        self.assertEqual(len(herencia.comprobar(datos, self._apertura("clases\n"))), 1)


class PruebaPoblacionDelInforme(BaseForja):
    """LA POBLACION DEL INFORME ES GRAFO MAS BANDEJAS (12 sep 2026, punto 3).

    `D.38.4` ya lo mandaba para el barrido del auditor desde el 11 sep, y el
    informe seguia cargando solo el grafo. **Un par cuyos dos extremos viven en
    cuarentena no lo levantaba nadie**, y la `ACTA 20` tuvo que clasificar a mano
    el de `cap_10` `L225` a `L251` contra `reconocer_recompensar_gente_estable`
    porque la maquina no podia verlo.
    """

    def _taller_bandejas(self):
        base = os.path.join(self.taller, "cuarentena")
        for sub in ("un_lote", "_insertados/un_lote", "_derivadas",
                    "catalogo_ajeno"):
            ruta = os.path.join(base, *sub.split("/"))
            if not os.path.isdir(ruta):
                os.makedirs(ruta)
        return base

    def _candidato(self, identificador, fuente="manual_sistema_conocimiento",
                   texto="medir la cola de lectura del lote entero"):
        return {
            "id": identificador,
            "titulo": identificador.replace("_", " "),
            "resumen_teorico": texto,
            "condiciones_activacion": "cuando hay un lote en la bandeja",
            "entregable_esperado": "un informe con su saldo",
            "pasos_accionables": ["Correr el informe.", "Leer el saldo."],
            "dominio": "gestion",
            "estado": "vivo",
            "fuentes": [{"clave": fuente, "fecha": "2026-09-12"}],
            "denominaciones": {"nombre_largo": identificador.replace("_", " ")},
        }

    def _poner(self, carpeta, nombre, datos):
        ruta = os.path.join(carpeta, nombre)
        comun.escribir_texto(ruta, json.dumps(datos, ensure_ascii=False))
        return ruta

    def test_la_poblacion_suma_las_bandejas_y_descarta_lo_archivado(self):
        from src import informe
        base = self._taller_bandejas()
        self._poner(os.path.join(base, "un_lote"), "espera.json",
                    self._candidato("esperar_turno_bandeja"))
        self._poner(os.path.join(base, "_insertados", "un_lote"), "ya_entro.json",
                    self._candidato("archivar_candidato_insertado"))
        esperando = informe.poblacion_de_bandejas(
            raiz=self.taller,
            tabla_fuentes=comun.leer_json(self.fuentes_tabla))
        ids = [c["id"] for c in esperando]
        self.assertIn("esperar_turno_bandeja", ids)
        # CASO POSITIVO: lo archivado NO se cuenta dos veces. Ya vive en el
        # grafo (D.31), y contarlo aqui seria medir un nodo contra si mismo.
        self.assertNotIn("archivar_candidato_insertado", ids)

    def test_caso_positivo_lo_que_no_puede_entrar_no_es_poblacion(self):
        """`cuarentena/` tambien aloja un CATALOGO DE REFERENCIA ajeno.

        163 nodos puestos ahi para calibrar la aduana. No esperan juicio: no van
        a entrar nunca. Y el criterio no es una lista de nombres de carpeta, que
        es el error que la decision 1 de este mismo dia acaba de corregir un piso
        mas abajo: **entra el candidato cuyas fuentes estan en la tabla vigente.**
        """
        from src import informe
        base = self._taller_bandejas()
        self._poner(os.path.join(base, "un_lote"), "propio.json",
                    self._candidato("medir_candidato_propio"))
        self._poner(os.path.join(base, "catalogo_ajeno"), "ajeno.json",
                    self._candidato("medir_nodo_ajeno",
                                    fuente="libro_que_nadie_registro"))
        ids = [c["id"] for c in informe.poblacion_de_bandejas(
            raiz=self.taller,
            tabla_fuentes=comun.leer_json(self.fuentes_tabla))]
        self.assertIn("medir_candidato_propio", ids)
        self.assertNotIn("medir_nodo_ajeno", ids)

    def test_un_par_con_los_dos_extremos_en_cuarentena_se_levanta(self):
        """Es el ejemplar exacto que obligo a esta decision."""
        from src import informe
        base = self._taller_bandejas()
        texto = ("reconocer y recompensar a la gente estable del equipo, la que "
                 "sostiene el trabajo sin querer ascender cada trimestre")
        vecino = self._candidato("reconocer_recompensar_gente_estable", texto=texto)
        self._poner(os.path.join(base, "un_lote"), "vecino.json", vecino)
        gemelo = self._candidato("reconocer_gente_estable_equipo", texto=texto)
        ruta = self._poner(os.path.join(base, "un_lote"), "gemelo.json", gemelo)

        tabla = comun.leer_json(self.fuentes_tabla)
        # CON LA POBLACION VIEJA (solo grafo, que esta vacio) NADIE LO VE.
        d_viejo, pob_vieja, _u, _a = informe.revisar(
            [ruta], ruta_dataset=self.dataset, tabla_fuentes=tabla, bandejas=[])
        self.assertEqual(d_viejo[0]["salida"], informe.ENTRARIA)
        self.assertEqual(pob_vieja.bandejas, 0)

        # CON LA POBLACION NUEVA, SI.
        esperando = informe.poblacion_de_bandejas(raiz=self.taller, tabla_fuentes=tabla)
        d_nuevo, pob, _u, _a = informe.revisar(
            [ruta], ruta_dataset=self.dataset, tabla_fuentes=tabla,
            bandejas=esperando)
        self.assertEqual(d_nuevo[0]["salida"], informe.BLOQUEARIA)
        self.assertTrue(any(v["id"] == "reconocer_recompensar_gente_estable"
                            for v in d_nuevo[0]["vecinos"]))
        self.assertEqual(pob.bandejas, 2)
        self.anotar("D40_pob", "par con los dos extremos en cuarentena: levantado")

    def test_el_candidato_no_se_mide_contra_si_mismo(self):
        """La errata de metodo de `D.38.4`, corregida en la `ACTA 18`: menos el
        propio candidato, y por eso se barre uno por vez."""
        from src import informe
        base = self._taller_bandejas()
        solo = self._candidato("medir_unico_candidato_bandeja")
        ruta = self._poner(os.path.join(base, "un_lote"), "solo.json", solo)
        tabla = comun.leer_json(self.fuentes_tabla)
        esperando = informe.poblacion_de_bandejas(raiz=self.taller, tabla_fuentes=tabla)
        self.assertEqual(len(esperando), 1)
        dictamenes, pob, _u, _a = informe.revisar(
            [ruta], ruta_dataset=self.dataset, tabla_fuentes=tabla,
            bandejas=esperando)
        # ESTA EN LA POBLACION Y AUN ASI ENTRA LIMPIO: su propio id lo excluye.
        self.assertEqual(pob.bandejas, 1)
        self.assertEqual(dictamenes[0]["salida"], informe.ENTRARIA)
        self.assertEqual(dictamenes[0]["vecinos"], [])

    def test_el_resolutor_no_se_ensancha_con_las_bandejas(self):
        """'el id ya vive en el grafo' es sobre el GRAFO.

        Un id que espera en la bandeja NO vive en el grafo todavia, y tumbarlo
        por eso convertiria toda la bandeja en un lote rechazado.
        """
        from src import informe
        base = self._taller_bandejas()
        datos = self._candidato("esperar_veredicto_bandeja")
        ruta = self._poner(os.path.join(base, "un_lote"), "c.json", datos)
        tabla = comun.leer_json(self.fuentes_tabla)
        dictamenes, _pob, _u, _a = informe.revisar(
            [ruta], ruta_dataset=self.dataset, tabla_fuentes=tabla,
            bandejas=informe.poblacion_de_bandejas(raiz=self.taller,
                                                   tabla_fuentes=tabla))
        self.assertNotEqual(dictamenes[0]["salida"], informe.CAERIA)

    def test_el_informe_publica_la_poblacion_con_su_reparto(self):
        """Un numero solo miente: 286 no dice lo mismo que 203 mas 83."""
        from src import informe
        base = self._taller_bandejas()
        ruta = self._poner(os.path.join(base, "un_lote"), "c.json",
                           self._candidato("publicar_poblacion_barrido"))
        tabla = comun.leer_json(self.fuentes_tabla)
        dictamenes, pob, umbrales, fuera = informe.revisar(
            [ruta], ruta_dataset=self.dataset, tabla_fuentes=tabla,
            bandejas=informe.poblacion_de_bandejas(raiz=self.taller,
                                                   tabla_fuentes=tabla))
        texto = informe.texto_informe(dictamenes, pob, umbrales, archivados=fuera)
        self.assertIn("poblacion del barrido", texto)
        self.assertIn("del grafo mas", texto)
        self.assertIn("que esperan en bandejas", texto)
        # Y LA CIFRA QUE JUSTIFICA QUE ESTO VIVA EN EL ARNES Y NO EN UN TURNO.
        self.assertIn("CHOCAN entre si dentro del lote", texto)


class PruebaTallado(BaseForja):
    """D.41: LA TABLA QUE DICE SER DE INSTRUMENTO ES LA DEL INSTRUMENTO.

    Cuatro caidas de la racha `REPORTE` en cuatro vueltas fueron la misma cosa: una
    tabla presentada como salida de un instrumento y tecleada. En la vuelta 22 el
    mismo reporte llevaba una tabla **pegada** (`cap_10`, al digito) y una
    **tecleada** (`cap_11`, 14 de 18 filas falsas), y el fichero del instrumento ya
    tenia la buena impresa. **La diferencia no fue el cuidado: fue el metodo.**
    """

    TABLA = ("| tramo | palabras | nodos |\n"
             "|---|---:|---:|\n"
             "| `L15 a L35` | 88 | **1** |\n"
             "| `L37 a L65` | 1083 | **1** |\n"
             "| `L67 a L97` | 226 | **1** |\n")

    def _instrumento(self, tabla=None, cabecera=True):
        ruta = os.path.join(self.taller, "salida_frontera.txt")
        cuerpo = "LA COMPROBACION\n  suma de las filas : 1397\n\n" if cabecera else ""
        comun.escribir_texto(ruta, cuerpo + (tabla or self.TABLA))
        return ruta

    def _reporte(self, cuerpo):
        ruta = os.path.join(self.taller, "REPORTE.md")
        comun.escribir_texto(ruta, cuerpo)
        return ruta

    def _declarado(self, tabla=None, entremedio=""):
        """Un reporte con la declaracion que esta casa escribe de verdad."""
        return ("## P.4.b. LA FRONTERA\n\n"
                "*Salida de `python .t1/frontera.py`, guardada en "
                "`salida_frontera.txt`.*\n\n" + entremedio + (tabla or self.TABLA))

    def _revisar(self, cuerpo):
        from scripts import tallar_reporte
        self._instrumento()
        return tallar_reporte.revisar(self._reporte(cuerpo), raiz=self.taller)

    def test_una_tabla_pegada_de_su_instrumento_pasa(self):
        dictamenes = self._revisar(self._declarado())
        self.assertEqual(len(dictamenes), 1)
        self.assertEqual(dictamenes[0]["estado"], "TALLADA")
        self.assertEqual(dictamenes[0]["diferencias"], [])

    def test_caso_positivo_una_celda_tecleada_cae_y_nombra_su_fila(self):
        """Sin esto, la guarda podria estar diciendo siempre que si.

        Es la caida de la vuelta 22 en pequenio: el instrumento dice 1083 y la
        tabla publicada dice 1198.
        """
        tecleada = self.TABLA.replace("| 1083 |", "| 1198 |")
        dictamenes = self._revisar(self._declarado(tecleada))
        self.assertEqual(dictamenes[0]["estado"], "DIFIERE")
        self.assertEqual(len(dictamenes[0]["diferencias"]), 1)
        diferencia = dictamenes[0]["diferencias"][0]
        self.assertEqual(diferencia["fila"], "`L37 a L65`")
        self.assertEqual(diferencia["columna"], "palabras")
        self.assertEqual(diferencia["reporte"], "1198")
        self.assertEqual(diferencia["instrumento"], "1083")
        self.anotar("D41", "una celda tecleada: cazada, con su fila y su columna")

    def test_el_informe_nombra_la_fila_y_manda_regenerar(self):
        from scripts import tallar_reporte
        dictamenes = self._revisar(
            self._declarado(self.TABLA.replace("| 1083 |", "| 1198 |")))
        texto = tallar_reporte.texto_informe(dictamenes)
        self.assertIn("TALLADO EN ROJO", texto)
        self.assertIn("`L37 a L65`", texto)
        self.assertIn("--arreglar", texto)

    def test_una_fila_que_falta_y_una_que_sobra_se_nombran(self):
        sin_una = ("| tramo | palabras | nodos |\n"
                   "|---|---:|---:|\n"
                   "| `L15 a L35` | 88 | **1** |\n"
                   "| `L37 a L65` | 1083 | **1** |\n"
                   "| `L99 a L113` | 218 | **1** |\n")
        dictamenes = self._revisar(self._declarado(sin_una))
        notas = " ".join(d["nota"] for d in dictamenes[0]["diferencias"])
        self.assertIn("NO esta en la salida del instrumento", notas)
        self.assertIn("el instrumento la imprime y el reporte NO la lleva", notas)

    def test_un_reflujo_de_espacios_no_es_una_cifra_falsa(self):
        """El instrumento alinea con dos espacios y el markdown con uno.

        Hacer caer una vuelta por eso enseñaria a desconfiar de la guarda, que es
        la unica forma segura de que nadie la mire.
        """
        reflujo = self.TABLA.replace("| `L15 a L35` | 88 |",
                                     "|  `L15 a L35`  |  88  |")
        dictamenes = self._revisar(self._declarado(reflujo))
        self.assertEqual(dictamenes[0]["estado"], "TALLADA")

    def test_la_declaracion_vale_aunque_haya_un_bloque_en_medio(self):
        """La casa declara, luego pega la comprobacion, y solo despues la tabla.

        Una ventana fija dejo fuera justo la tabla de `cap_11`, que es el caso
        que obligo a esta guarda a existir.
        """
        medio = ("    tramos que dan nodo : 18\n    lineas NO cubiertas : 0\n"
                 "    IGUALES             : True\n\n" * 4)
        dictamenes = self._revisar(self._declarado(entremedio=medio))
        self.assertEqual(len(dictamenes), 1)
        self.assertEqual(dictamenes[0]["estado"], "TALLADA")

    def test_caso_positivo_una_tabla_sin_declaracion_no_se_mira(self):
        """El reporte tiene 705 tablas y 8 declaran instrumento.

        Una guarda que midiera las 705 contra nada convertiria el commit en un
        campo de minas, y la regla es sobre las que DICEN venir de un instrumento.
        """
        dictamenes = self._revisar("## Una seccion cualquiera\n\n" + self.TABLA)
        self.assertEqual(dictamenes, [])

    def test_citar_un_fichero_no_es_declarar_que_la_tabla_sale_de_el(self):
        """La primera version marco ocho tablas por nombrar `loop.log` cerca."""
        cuerpo = ("## El coste de la vuelta\n\n"
                  "Los tiempos estan en `docs/loop/loop.log` y en `salida_frontera.txt`, "
                  "por si alguien quiere mirarlos.\n\n" + self.TABLA)
        self.assertEqual(self._revisar(cuerpo), [])

    def test_una_tabla_declarada_PARCIAL_cita_y_no_reproduce(self):
        """Una tabla de resumen puede traer DOS filas de instrumento y diez que no."""
        cuerpo = ("## P.9.3. EL RESUMEN\n\n"
                  "<!-- TALLADO: parcial salida=salida_frontera.txt -->\n"
                  "*Salida de `salida_frontera.txt` en dos de sus filas.*\n\n"
                  "| | |\n|---|---|\n| **tareas** | **5** |\n| **paradas** | **0** |\n")
        dictamenes = self._revisar(cuerpo)
        self.assertEqual(dictamenes[0]["estado"], "CITA")
        self.assertEqual(dictamenes[0]["diferencias"], [])

    def test_un_instrumento_sin_tabla_no_se_puede_comprobar_y_no_es_diferencia(self):
        from scripts import tallar_reporte
        comun.escribir_texto(os.path.join(self.taller, "salida_frontera.txt"),
                             "EL SALDO\n  ENTRARIAN : 9\n  BLOQUEARIAN : 8\n")
        dictamenes = tallar_reporte.revisar(
            self._reporte(self._declarado()), raiz=self.taller)
        self.assertEqual(dictamenes[0]["estado"], "SIN COMPROBAR")
        self.assertIn("la resume, no la reproduce", dictamenes[0]["motivo"])

    def test_una_salida_que_no_esta_es_SIN_COMPROBAR_y_lo_dice(self):
        from scripts import tallar_reporte
        dictamenes = tallar_reporte.revisar(
            self._reporte(self._declarado()), raiz=self.taller)
        self.assertEqual(dictamenes[0]["estado"], "SIN COMPROBAR")
        self.assertIn("salida_frontera.txt", dictamenes[0]["motivo"])

    def test_caso_positivo_una_ruta_de_CERO_BYTES_es_caida_de_cifra(self):
        """Cosecha `7.B`: una ruta publicada como prueba que apunta a un fichero
        vacio es caida de cifra.

        **ESTE HUECO ESTUVO ABIERTO Y LO PAGO LA VUELTA 25.** Un fichero vacio
        existe, asi que se leia sin error, no traia tabla, y la guarda lo
        despachaba con la lectura mas generosa posible (*esta tabla resume su
        salida*) y devolvia VERDE.
        """
        from scripts import tallar_reporte
        vacia = os.path.join(self.taller, "salida_frontera.txt")
        comun.escribir_texto(vacia, "")
        dictamenes = tallar_reporte.revisar(
            self._reporte(self._declarado()), raiz=self.taller)
        self.assertEqual(dictamenes[0]["estado"], "RUTA VACIA")
        self.assertIn("cero bytes", dictamenes[0]["motivo"])
        texto = tallar_reporte.texto_informe(dictamenes)
        self.assertIn("TALLADO EN ROJO", texto)
        self.assertIn("salida_frontera.txt", texto)
        self.anotar("D41_vacia", "ruta de cero bytes: cazada, y antes daba verde")

    def test_caso_negativo_una_salida_con_contenido_sin_tabla_no_es_ruta_vacia(self):
        """VACIA no es lo mismo que SIN TABLA, y la diferencia tiene que aguantar.

        Un instrumento que imprime un saldo y no una tabla esta cumpliendo: lo que
        la tabla del reporte hace es resumirlo. Confundir las dos cosas volveria a
        llenar la guarda de falsos positivos.
        """
        from scripts import tallar_reporte
        comun.escribir_texto(os.path.join(self.taller, "salida_frontera.txt"),
                             "EL SALDO" + chr(10) + "  ENTRARIAN : 9" + chr(10))
        dictamenes = tallar_reporte.revisar(
            self._reporte(self._declarado()), raiz=self.taller)
        self.assertEqual(dictamenes[0]["estado"], "SIN COMPROBAR")

    def test_caso_negativo_los_espacios_en_blanco_tampoco_son_una_salida(self):
        from scripts import tallar_reporte
        comun.escribir_texto(os.path.join(self.taller, "salida_frontera.txt"),
                             "   " + chr(10) + chr(10) + "  " + chr(10))
        dictamenes = tallar_reporte.revisar(
            self._reporte(self._declarado()), raiz=self.taller)
        self.assertEqual(dictamenes[0]["estado"], "RUTA VACIA")

    def test_caso_positivo_sin_reporte_el_tallado_no_revienta_y_no_bloquea(self):
        """`D.34.2` RETIRA `REPORTE.md` durante la fase ciega, a proposito.

        Y esto no era cosmetico: **el arnes COMMITEA la pagina sellada con los cuatro
        ficheros retirados**, asi que el hook corria el tallador sin reporte, este
        reventaba con `FileNotFoundError`, y **el commit del propio sello se
        abortaba**. No habia mordido todavia solo porque en la vuelta 29 el barrido
        de guiones cayo tres segundos antes. **Una guarda que impide sellar la fase
        ciega no protege el dato: bloquea el bucle.**
        """
        from scripts import tallar_reporte
        ausente = os.path.join(self.taller, "no_existe_REPORTE.md")
        self.assertEqual(tallar_reporte.revisar(ausente, raiz=self.taller), [])
        self.anotar("D41_ciega", "sin reporte el tallado calla, no revienta")

    def test_caso_negativo_con_reporte_presente_sigue_tumbando(self):
        """La exencion es por AUSENCIA, no un indulto general."""
        from scripts import tallar_reporte
        self._instrumento()
        ruta = self._reporte(self._declarado(
            self.TABLA.replace("| 1083 |", "| 1198 |")))
        dictamenes = tallar_reporte.revisar(ruta, raiz=self.taller)
        self.assertEqual(dictamenes[0]["estado"], "DIFIERE")

    def test_el_estricto_tumba_lo_que_el_hook_deja_pasar(self):
        """El cierre de vuelta es el momento en que los instrumentos siguen ahi."""
        from scripts import tallar_reporte
        dictamenes = tallar_reporte.revisar(
            self._reporte(self._declarado()), raiz=self.taller)
        blando = tallar_reporte.texto_informe(dictamenes, estricto=False)
        duro = tallar_reporte.texto_informe(dictamenes, estricto=True)
        self.assertNotIn("EN ROJO", blando)
        self.assertIn("EN ROJO (estricto)", duro)

    def test_arreglar_regenera_la_tabla_desde_su_instrumento(self):
        """La correccion es por regeneracion, NUNCA tecleando la celda buena."""
        from scripts import tallar_reporte
        self._instrumento()
        ruta = self._reporte(self._declarado(
            self.TABLA.replace("| 1083 |", "| 1198 |")))
        arregladas = tallar_reporte.arreglar(ruta, regenerar=False, raiz=self.taller)
        self.assertEqual(len(arregladas), 1)
        self.assertIn("1083", comun.leer_texto(ruta))
        self.assertNotIn("1198", comun.leer_texto(ruta))
        # Y DESPUES DE ARREGLAR, EL TALLADO PASA.
        self.assertEqual(
            tallar_reporte.revisar(ruta, raiz=self.taller)[0]["estado"], "TALLADA")


class PruebaCensoDeRutas(BaseForja):
    """D.42: LA UNIDAD DE LA RUTA ES LA CELDA.

    `D.41` ata un instrumento a una TABLA entera. La vuelta 25 no cayo asi: cayo
    publicando una ruta **por fila**, en una columna titulada *de donde sale*, que
    apuntaba a un fichero de **cero bytes** mientras la cifra decia `2` donde el
    instrumento da `4`. **La unidad de `D.41` es la tabla; aqui es la celda.**
    """

    def _doc(self, cuerpo, nombre="REPORTE.md"):
        carpeta = os.path.join(self.taller, "docs", "loop")
        if not os.path.isdir(carpeta):
            os.makedirs(carpeta)
        comun.escribir_texto(os.path.join(carpeta, nombre), cuerpo)
        return [os.path.join("docs", "loop", nombre)]

    def _fichero(self, ruta, cuerpo="una salida con algo dentro"):
        entera = os.path.join(self.taller, *ruta.split("/"))
        carpeta = os.path.dirname(entera)
        if carpeta and not os.path.isdir(carpeta):
            os.makedirs(carpeta)
        comun.escribir_texto(entera, cuerpo)
        return entera

    def _censar(self, cuerpo, nombre="REPORTE.md"):
        from scripts import censar_rutas
        docs = self._doc(cuerpo, nombre)
        return censar_rutas.censar(documentos=docs, raiz=self.taller)

    TABLA = ("## S.10. LO QUE PASA A LA VUELTA SIGUIENTE, CON SU CIFRA Y SU SEDE\n\n"
             "| que | cifra | de donde sale |\n|---|---|---|\n"
             "| los pares del candidato parado | **2** por leer | `%s` |\n")

    # ------------------------------------------------------------- forma (a)
    def test_una_ruta_con_contenido_pasa(self):
        self._fichero(".v25/cola_lectura.txt")
        caidas, pasan = self._censar(self.TABLA % ".v25/cola_lectura.txt")
        self.assertEqual(caidas, [])
        self.assertEqual(pasan[0]["forma"], "con contenido")

    # ------------------------------------------------------------- forma (b)
    def test_caso_positivo_la_ruta_de_cero_bytes_tumba_y_nombra_la_celda(self):
        """Es la caida de la vuelta 25, entera y en pequenio."""
        self._fichero(".v25/cola_lectura.txt", "")
        caidas, _pasan = self._censar(self.TABLA % ".v25/cola_lectura.txt")
        self.assertEqual(len(caidas), 1)
        self.assertEqual(caidas[0]["ruta"], ".v25/cola_lectura.txt")
        # LA CELDA, NOMBRADA: sin esto la guarda diria "algo falla" y no donde.
        self.assertEqual(caidas[0]["sitio"], "celda 3")
        self.assertIn("esta y esta VACIA", caidas[0]["motivo"])
        self.anotar("D42", "ruta de cero bytes en una celda: cazada, con su celda")

    def test_una_ruta_que_no_esta_tumba_igual(self):
        caidas, _pasan = self._censar(self.TABLA % ".v25/no_existe.txt")
        self.assertEqual(len(caidas), 1)
        self.assertIn("NO esta en el arbol", caidas[0]["motivo"])

    def test_caso_negativo_la_marca_en_la_misma_celda_la_deja_pasar(self):
        """`.barrido_C_con_ensayo_v16.txt` con su marca y su cita de la ACTA 15."""
        self._fichero(".barrido_C_con_ensayo_v16.txt", "")
        caidas, pasan = self._censar(
            "| testigo | que es |\n|---|---|\n"
            "| `.barrido_C_con_ensayo_v16.txt` VACIA A PROPOSITO: adjudicado en la "
            "ACTA 15 1.9 | su testigo lo prueba |\n")
        self.assertEqual(caidas, [])
        self.assertIn("VACIA A PROPOSITO", pasan[0]["forma"])

    def test_caso_positivo_la_marca_SIN_MOTIVO_no_vale(self):
        """Una excusa sin motivo escrito es una excusa que se concede siempre."""
        self._fichero(".v25/cola_lectura.txt", "")
        caidas, _pasan = self._censar(
            (self.TABLA % ".v25/cola_lectura.txt").replace(
                "| `.v25", "| VACIA A PROPOSITO: | `.v25"))
        self.assertEqual(len(caidas), 1)

    def test_la_marca_de_OTRA_celda_no_cubre_esta(self):
        """La marca va en LA MISMA celda: es lo que la hace visible junto a la cifra."""
        self._fichero(".v25/cola_lectura.txt", "")
        caidas, _pasan = self._censar(
            "| que | cifra | de donde sale |\n|---|---|---|\n"
            "| VACIA A PROPOSITO: lo digo aqui al lado | **2** | `.v25/cola_lectura.txt` |\n")
        self.assertEqual(len(caidas), 1)

    # ------------------------------------------------------------- forma (c)
    def test_caso_negativo_un_patron_declarado_con_coincidencias_pasa(self):
        self._fichero(".aduana_v22/A_uno.txt")
        self._fichero(".aduana_v22/B_dos.txt")
        caidas, pasan = self._censar(
            "| los informes | 17 | PATRON: `.aduana_v22/*.txt` |\n"
            "|---|---|---|\n| otra | fila | para que sea tabla |\n")
        self.assertEqual(caidas, [])
        self.assertIn("PATRON", pasan[0]["forma"])

    def test_caso_positivo_un_patron_sin_declarar_tumba(self):
        self._fichero(".aduana_v22/A_uno.txt")
        caidas, _pasan = self._censar(
            "| los informes | 17 | `.aduana_v22/*.txt` |\n"
            "|---|---|---|\n| otra | fila | para que sea tabla |\n")
        self.assertEqual(len(caidas), 1)
        self.assertIn("no lo declara", caidas[0]["motivo"])

    def test_caso_positivo_un_patron_sin_NI_UNA_coincidencia_tumba(self):
        caidas, _pasan = self._censar(
            "| los cinco | 5 | PATRON: `.frag_*.md` |\n"
            "|---|---|---|\n| otra | fila | para que sea tabla |\n")
        self.assertEqual(len(caidas), 1)
        self.assertIn("NI UNA coincidencia", caidas[0]["motivo"])

    def test_cero_coincidencias_puede_ser_la_cifra_si_se_declara(self):
        """`cuarentena/_insertados/*.json` da 0 porque ahi no cuelga ningun JSON
        suelto, y eso es exactamente lo que la fila publica."""
        caidas, pasan = self._censar(
            "| sueltos en la raiz | 0 | PATRON: `cuarentena/_insertados/*.json` "
            "VACIA A PROPOSITO: cero coincidencias ES la cifra |\n"
            "|---|---|---|\n| otra | fila | para que sea tabla |\n")
        self.assertEqual(caidas, [])

    # ------------------------------------------- lo que el censo NO cuenta
    def test_caso_positivo_una_ruta_NOMBRADA_no_es_una_ruta_publicada(self):
        """*el barrido tumbo `.c9/mk.py`* no ofrece nada como origen de una cifra.

        Censar toda mencion daria 42 celdas que marcar en dos documentos de treinta
        mil lineas, y **una marca que se pone cuarenta veces deja de leerse.**
        """
        caidas, pasan = self._censar(
            "El barrido de guiones tumbo `.c9/mk.py`, el guion de un solo uso con el "
            "que escribo, y por eso lo borre en esa misma vuelta sin mas.\n")
        self.assertEqual(caidas, [])
        self.assertEqual(pasan, [])

    def test_pero_la_celda_que_ES_la_ruta_si_se_cuenta(self):
        """Es la forma de la columna *de donde sale*, y es donde cayo la vuelta 25."""
        caidas, _pasan = self._censar(
            "| que | cifra | de donde sale |\n|---|---|---|\n"
            "| lo que sea | **9** | `.v25/no_existe.txt` |\n")
        self.assertEqual(len(caidas), 1)

    def test_un_comando_no_es_una_ruta_pero_su_fichero_si(self):
        """Lo que va en comillas suele ser la ORDEN entera."""
        from scripts import censar_rutas
        self.assertIsNone(censar_rutas.parece_ruta("sed -n '8,$p' cap_07.md"))
        self.assertEqual(censar_rutas.parece_ruta("wc -l dataset/nodos.jsonl"),
                         "dataset/nodos.jsonl")
        self.assertEqual(censar_rutas.parece_ruta("python .t1/frontera.py"),
                         ".t1/frontera.py")
        # CASO POSITIVO: un molde no es una ruta.
        self.assertIsNone(censar_rutas.parece_ruta("cuarentena/<lote>/<id>.json"))

    def test_una_ruta_relativa_al_documento_resuelve(self):
        """Un acta que vive en docs/loop/ y escribe `paradas/x.md` no miente."""
        self._fichero("docs/loop/paradas/2026-09-13-algo.md", "una parada archivada")
        caidas, pasan = self._censar(
            "| la parada | 1 | `paradas/2026-09-13-algo.md` |\n"
            "|---|---|---|\n| otra | fila | para que sea tabla |\n",
            nombre="ACTA_AUDITOR.md")
        self.assertEqual(caidas, [])

    def test_un_candidato_insertado_resuelve_en_su_archivo(self):
        """`D.31` lo archiva en `_insertados` en el mismo acto de insertarlo."""
        self._fichero("cuarentena/_insertados/un_lote/entrado.json", "{}")
        caidas, _pasan = self._censar(
            "| el candidato | 1 | `cuarentena/un_lote/entrado.json` |\n"
            "|---|---|---|\n| otra | fila | para que sea tabla |\n")
        self.assertEqual(caidas, [])

    def test_los_retirados_por_D342_estan_exentos_por_protocolo(self):
        """La fase ciega retira cuatro ficheros y commitea mientras no estan.

        Un acta que cita `REPORTE.md` como sede no publica una ruta falsa: la
        publica mientras existe, y la fase ciega la esconde a proposito.
        """
        from scripts import censar_rutas
        exentas = censar_rutas._sedes_exentas()
        for retirado in ("docs/loop/REPORTE.md", "docs/loop/ultimo_extractor.json",
                         "docs/loop/ultimo_auditor.json"):
            self.assertIn(retirado, exentas)

    def test_la_lista_de_exentos_cubre_LOS_CUATRO_que_el_arnes_retira(self):
        """La lista de `config/` duplica la del arnes, y una copia se desincroniza.

        **Paso el 16 sep 2026 y paro el bucle:** meti en la lista `REPORTE.md` y los
        dos testigos, **y me deje `loop.log`**, que es el cuarto. La fase ciega sello
        con el censo en rojo por una ruta ausente **por protocolo**, y el arnes se
        detuvo por una caida que no existia.

        **UNA LISTA QUE HAY QUE ACORDARSE DE COMPLETAR NO ESTA COMPLETA.** Esta prueba
        lee los cuatro del propio arnes y exige que la lista los cubra.
        """
        from scripts import censar_rutas
        arnes = comun.leer_texto(os.path.join(RAIZ, "orquestador_forja.sh"))
        encaje = re.search(r'retirar="([^"]+)"', arnes)
        self.assertIsNotNone(encaje, "el arnes ya no declara que retira")
        exentas = censar_rutas._sedes_exentas()
        for fichero in encaje.group(1).split():
            self.assertIn("docs/loop/" + fichero, exentas,
                          "D.34.2 retira %s y el censo no lo exime" % fichero)

    def test_un_artefacto_de_maquina_esta_exento_POR_SU_FAMILIA(self):
        """`D.33` lo resolvio por PATRON el 12 sep, y el censo usa la misma funcion.

        **Tercera vez que aparece la misma leccion.** Meti en `config/` los cuatro
        ficheros que `D.34.2` retira y el hook me cazo con un quinto,
        `docs/loop/ultimo_apertura.json`, **que esta vacio unos segundos mientras el
        arnes lo escribe.** Un nombre que hay que acordarse de anadir protege hasta
        el dia en que nace otro fichero.
        """
        from scripts import censar_rutas
        self.assertTrue(censar_rutas._es_artefacto("docs/loop/ultimo_apertura.json"))
        self.assertTrue(censar_rutas._es_artefacto("docs/loop/ultimo_manana.json"))
        self.assertTrue(censar_rutas._es_artefacto("docs/loop/loop.log"))
        # CASO POSITIVO: la prosa de la casa NO es un artefacto, ni en esa carpeta.
        self.assertFalse(censar_rutas._es_artefacto("docs/loop/ACTA_AUDITOR.md"))
        self.assertFalse(censar_rutas._es_artefacto("docs/ultimo_disfrazado.json"))

    def test_caso_positivo_otro_fichero_ausente_sigue_cayendo(self):
        """La exencion es de los cuatro que D.34.2 nombra, no de todo lo que falte."""
        caidas, _pasan = self._censar(self.TABLA % ".v29/no_existe.txt")
        self.assertEqual(len(caidas), 1)

    def test_la_lista_fija_de_config_exime_por_protocolo(self):
        from scripts import censar_rutas
        self.assertIn("docs/loop/PROMPT_SIGUIENTE.md", censar_rutas._sedes_exentas())


class PruebaAduanaMideBandejas(BaseForja):
    """D.38.5 EN LA ADUANA, que es donde se decide (16 sep 2026).

    La regla lleva **TAMBIEN PARA LA ADUANA** en su propio titular desde el 12 sep,
    y durante cuatro dias solo estuvo cableada en `informe.py`, que corre EN SECO.
    La `ACTA 26` lo levanto con su coste medido: **cinco pares por encima de umbral
    sin veredicto, los cinco con un extremo en la bandeja.** No era perdida, era
    aplazamiento; pero la regla nacio para que un par **no dependa de que alguien se
    acuerde.**
    """

    TEXTO = ("bloquear en el calendario dos horas de pensar cada dia y tratarlas "
             "como una reunion sagrada que no se mueve por nadie")

    def _en_bandeja(self, identificador, texto=None, lote="un_lote", pasos=None):
        datos = {
            "id": identificador,
            "titulo": identificador.replace("_", " "),
            "resumen_teorico": texto or self.TEXTO,
            "condiciones_activacion": "cuando el calendario se llena de reuniones",
            "entregable_esperado": "dos horas de pensar bloqueadas",
            "pasos_accionables": pasos or ["Abrir el calendario.",
                                           "Bloquear dos horas.",
                                           "Tratarlas como sagradas."],
            "dominio": "gestion", "estado": "vivo",
            "fuentes": [{"clave": "manual_sistema_conocimiento", "fecha": "2026-09-16"}],
            "denominaciones": {"nombre_largo": identificador.replace("_", " ")},
        }
        carpeta = os.path.join(self.bandeja, lote)
        if not os.path.isdir(carpeta):
            os.makedirs(carpeta)
        ruta = os.path.join(carpeta, identificador + ".json")
        comun.escribir_texto(ruta, json.dumps(datos, ensure_ascii=False))
        return ruta

    def test_caso_positivo_un_vecino_que_vive_en_la_bandeja_BLOQUEA(self):
        """Antes del 16 sep esto entraba limpio, y el par se aplazaba."""
        self._en_bandeja("bloquear_tiempo_pensar_calendario")
        candidato = self._en_bandeja("reservar_horas_pensar_agenda")
        codigo, salida = self.forja("insertar", candidato, "--sin-preguntas")
        self.assertIn("que esperan en bandejas", salida)
        self.assertIn("bloquear_tiempo_pensar_calendario", salida)
        self.assertNotEqual(codigo, 0, salida)
        self.anotar("D385", "vecino en bandeja: la aduana lo bloquea, ya no lo aplaza")

    def test_caso_negativo_sin_vecino_en_la_bandeja_entra_limpio(self):
        """Una aduana que bloquea todo es un candado, no una guarda."""
        self._en_bandeja(
            "revisar_presupuesto_compras_trimestre",
            texto=("reunir al equipo cada trimestre para repasar el presupuesto de "
                   "compras y firmar las desviaciones que encuentre"),
            pasos=["Convocar al equipo de compras.",
                   "Repasar las partidas del trimestre.",
                   "Firmar cada desviacion encontrada."])
        candidato = self._en_bandeja("reservar_horas_pensar_agenda")
        codigo, salida = self.forja("insertar", candidato, "--sin-preguntas")
        self.assertEqual(codigo, 0, salida)
        self.assertIn("que esperan en bandejas", salida)

    def test_la_poblacion_va_con_su_reparto_y_no_con_un_numero_solo(self):
        """`348` no dice lo mismo que `234 del grafo mas 114 que esperan`."""
        self._en_bandeja("revisar_presupuesto_compras_trimestre",
                         pasos=["Convocar al equipo.", "Repasar partidas."])
        candidato = self._en_bandeja("reservar_horas_pensar_agenda")
        _codigo, salida = self.forja("insertar", candidato, "--sin-preguntas")
        self.assertIn("del grafo mas", salida)
        self.assertIn("que esperan en bandejas", salida)

    def test_caso_positivo_el_id_ya_vive_en_el_grafo_SIGUE_MIRANDO_SOLO_EL_GRAFO(self):
        """Lo dice la propia tabla de `D.38.5`.

        Un id que espera en la bandeja NO vive en el grafo todavia, y tumbarlo por
        eso **convertiria la bandeja entera en un lote rechazado.**
        """
        self._en_bandeja("reservar_horas_pensar_agenda")
        candidato = self._en_bandeja("reservar_horas_pensar_agenda", lote="otro_lote")
        _codigo, salida = self.forja("insertar", candidato, "--sin-preguntas")
        self.assertNotIn("el id ya vive en el grafo", salida)

    def test_el_candidato_no_se_mide_contra_si_mismo(self):
        """Esta EN la bandeja mientras se le mide: lo excluye su propio id."""
        candidato = self._en_bandeja("reservar_horas_pensar_agenda")
        codigo, salida = self.forja("insertar", candidato, "--sin-preguntas")
        self.assertEqual(codigo, 0, salida)

    def test_lo_archivado_no_se_cuenta_dos_veces(self):
        """`D.31` lo archiva al insertarlo: ya vive en el grafo."""
        self._en_bandeja("bloquear_tiempo_pensar_calendario",
                         lote=os.path.join("_insertados", "un_lote"))
        candidato = self._en_bandeja("reservar_horas_pensar_agenda")
        codigo, salida = self.forja("insertar", candidato, "--sin-preguntas")
        self.assertEqual(codigo, 0, salida)


class PruebaCorreccionDeclarada(BaseForja):
    """La operacion que corrige el `resumen_teorico` de un nodo YA INSERTADO.

    Nace de la parada de la vuelta 25 (`REPORTE.md` `S.9`), adjudicada por la
    `ACTA 25` `3.1`: `EXTRACTOR.md` 2 prohibe escribir a mano en el dataset Y
    dice como nace la via que falta, *una operacion escrita con su simulacion y
    su caso positivo*. Estas son la simulacion y los casos positivos.
    """

    MARCA = "CORRECCION DECLARADA"

    def _un_nodo(self, resumen=None):
        return nodo_base(
            "declarar_ancla_textual_unidad",
            resumen_teorico=resumen or (
                "UNIDAD DE ORIGEN: cap_06, con el ancla textual unica que la "
                "sostiene, 'level of incompetence'."))

    def _corregir(self, *extra):
        return self.forja("corregir", *extra)

    def test_la_correccion_se_escribe_y_el_texto_viejo_sigue_entero(self):
        nodo = self._un_nodo()
        viejo = nodo["resumen_teorico"]
        self.escribir_dataset([nodo])
        codigo, salida = self._corregir(
            "--nodo", "declarar_ancla_textual_unidad",
            "--anade", self.MARCA + " del 16 sep 2026: el ancla que esta frase "
                       "llama unica no esta en ninguna unidad del libro.",
            "--razon", "grep del ancla contra las quince unidades: cero coincidencias")
        self.assertEqual(codigo, 0, salida)
        self.assertIn("CORRECCION ESCRITA EN", salida)

        nuevo = dict((n["id"], n) for n in self.nodos())[
            "declarar_ancla_textual_unidad"]["resumen_teorico"]
        # LO QUE HABIA SIGUE LITERAL: esto es correccion declarada, no edicion.
        self.assertIn(viejo, nuevo)
        self.assertIn("no esta en ninguna unidad del libro", nuevo)
        self.assertTrue(len(nuevo) > len(viejo))

        registro = comun.leer_jsonl(self.veredictos)[-1]
        self.assertEqual(registro["veredicto"], "CORREGIDO")
        self.assertEqual(registro["campo"], "resumen_teorico")
        self.assertEqual(registro["levantada_por"], ["correccion declarada"])
        self.assertNotEqual(registro["huella_vecino"], registro["huella_candidato"])
        self.assertEqual(self.forja("gate")[0], 0)

    def test_caso_positivo_sin_la_marca_no_se_escribe_nada(self):
        """Sin esto, la prueba de arriba solo probaria que el comando escribe."""
        nodo = self._un_nodo()
        viejo = nodo["resumen_teorico"]
        self.escribir_dataset([nodo])
        codigo, salida = self._corregir(
            "--nodo", "declarar_ancla_textual_unidad",
            "--anade", "El ancla de esta frase no esta en ninguna unidad del libro.",
            "--razon", "una razon cualquiera")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("no se declara como correccion", salida)
        self.assertEqual(dict((n["id"], n) for n in self.nodos())[
            "declarar_ancla_textual_unidad"]["resumen_teorico"], viejo)
        self.assertEqual(comun.leer_jsonl(self.veredictos), [])

    def test_caso_positivo_el_gate_muerde_en_la_simulacion(self):
        """Un guion largo en el texto aniadido tumba la copia en memoria."""
        nodo = self._un_nodo()
        viejo = nodo["resumen_teorico"]
        self.escribir_dataset([nodo])
        codigo, salida = self._corregir(
            "--nodo", "declarar_ancla_textual_unidad",
            # EL GUION LARGO SE CONSTRUYE, NO SE TECLEA: el barrido de esta casa
            # es sobre el repo entero y tumbaria el propio fichero de pruebas.
            "--anade", self.MARCA + " del 16 sep 2026: el ancla " + chr(0x2014)
                       + " esa no esta en ninguna unidad del libro.",
            "--razon", "una razon cualquiera")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("guiones largos", salida)
        self.assertEqual(dict((n["id"], n) for n in self.nodos())[
            "declarar_ancla_textual_unidad"]["resumen_teorico"], viejo)
        self.assertEqual(comun.leer_jsonl(self.veredictos), [])

    def test_sin_razon_escrita_no_se_corrige(self):
        self.escribir_dataset([self._un_nodo()])
        codigo, salida = self._corregir(
            "--nodo", "declarar_ancla_textual_unidad",
            "--anade", self.MARCA + " del 16 sep 2026: el ancla no esta en el libro.",
            "--razon", "   ")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("sin razon escrita", salida)

    def test_un_nodo_que_no_vive_es_rechazo(self):
        self.escribir_dataset([self._un_nodo()])
        codigo, salida = self._corregir(
            "--nodo", "nodo_que_sigue_en_cuarentena",
            "--anade", self.MARCA + " del 16 sep 2026: el ancla no esta en el libro.",
            "--razon", "una razon cualquiera")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("no vive en el grafo", salida)

    def test_ningun_otro_campo_se_corrige_por_aqui(self):
        """Cambiar un paso es cambiar el procedimiento, y eso entra por la aduana."""
        self.escribir_dataset([self._un_nodo()])
        codigo, salida = self._corregir(
            "--nodo", "declarar_ancla_textual_unidad", "--campo", "pasos_accionables",
            "--anade", self.MARCA + " del 16 sep 2026: el ancla no esta en el libro.",
            "--razon", "una razon cualquiera")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("solo toca 'resumen_teorico'", salida)

    def test_la_misma_correccion_no_se_declara_dos_veces(self):
        self.escribir_dataset([self._un_nodo()])
        texto = (self.MARCA + " del 16 sep 2026: el ancla que esta frase llama "
                 "unica no esta en ninguna unidad del libro.")
        primera = self._corregir(
            "--nodo", "declarar_ancla_textual_unidad", "--anade", texto,
            "--razon", "grep del ancla: cero coincidencias")
        self.assertEqual(primera[0], 0, primera[1])
        segunda = self._corregir(
            "--nodo", "declarar_ancla_textual_unidad", "--anade", texto,
            "--razon", "grep del ancla: cero coincidencias")
        self.assertEqual(segunda[0], 1, segunda[1])
        self.assertIn("ya esta escrita", segunda[1])


class PruebaInsercionAtomica(BaseForja):
    """LA INSERCION ES ATOMICA: una corrida que imprime `RECHAZADO` no escribe nada.

    `EXTRACTOR.md` 14 pone `bitacora/` bajo la aduana, y **la bitacora registra lo
    que la aduana HIZO.** Una corrida que no inserto no hizo nada, luego no tiene
    nada que registrar.

    LA CAIDA QUE LO HIZO FALTA, medida por la `ACTA 27` `5.2` y reproducida por el
    auditor sobre copia: `comun.agregar_jsonl` se llamaba DENTRO del bucle por
    vecino y el rechazo llegaba DESPUES. **Cuatro lineas asi en la bitacora de esta
    casa**, las `248` a `251`: tres veredictos sobre un nodo que no vive y una arista
    declarada dos veces que no existe, con `NADA SE INSERTO` en la misma corrida.
    """

    TEXTO = ("bloquear en el calendario dos horas de pensar cada dia y tratarlas "
             "como una reunion sagrada que no se mueve por nadie")

    def _nodo(self, identificador, texto=None, pasos=None):
        return {
            "id": identificador,
            "titulo": identificador.replace("_", " "),
            "resumen_teorico": texto or self.TEXTO,
            "condiciones_activacion": "cuando el calendario se llena de reuniones",
            "entregable_esperado": "dos horas de pensar bloqueadas",
            "pasos_accionables": pasos or ["Abrir el calendario.",
                                           "Bloquear dos horas.",
                                           "Tratarlas como sagradas."],
            "dominio": "gestion", "estado": "vivo",
            "fuentes": [{"clave": "manual_sistema_conocimiento", "fecha": "2026-09-16"}],
            "denominaciones": {"nombre_largo": identificador.replace("_", " "),
                               "otros_idiomas": [], "sigla": ""},
            "ids_alias": [], "nodos_previos": [], "nodos_siguientes": [],
            "atribuciones": [],
        }

    def _en_bandeja(self, identificador, texto=None, pasos=None, lote="un_lote"):
        carpeta = os.path.join(self.bandeja, lote)
        if not os.path.isdir(carpeta):
            os.makedirs(carpeta)
        ruta = os.path.join(carpeta, identificador + ".json")
        comun.escribir_texto(ruta, json.dumps(
            self._nodo(identificador, texto, pasos), ensure_ascii=False))
        return ruta

    # ----------------------------------------------------------- 2.a atomica

    def test_caso_positivo_una_corrida_RECHAZADA_no_deja_ni_una_linea(self):
        """El vecino 1 ya tenia su veredicto escrito cuando el 2 tumbo la corrida."""
        self.escribir_dataset([self._nodo("bloquear_tiempo_pensar_calendario"),
                               self._nodo("reservar_horas_pensar_agenda")])
        candidato = self._en_bandeja("apartar_ratos_pensar_semana")
        codigo, salida = self.forja(
            "insertar", candidato, "--sin-preguntas",
            "--veredicto", "bloquear_tiempo_pensar_calendario|SANO|"
                           "no son el mismo trabajo y sus entregables no se parecen",
            # LA MADRE NO ES NI EL VECINO NI EL CANDIDATO: tumba la corrida, y lo
            # hace DESPUES de que el primer veredicto se haya construido.
            "--veredicto", "reservar_horas_pensar_agenda|CONTINUA|"
                           "madre=un_tercero_que_no_pinta_nada|"
                           "el hijo despliega en tres pasos lo que la madre nombra")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("RECHAZADO", salida)
        self.assertEqual(comun.leer_jsonl(self.veredictos), [], salida)
        self.anotar("ATOMICA", "una corrida RECHAZADA deja la bitacora intacta")

    def test_caso_negativo_una_corrida_QUE_ENTRA_si_escribe_sus_veredictos(self):
        """Una aduana que no escribe nunca es un cajon, no una bitacora."""
        self.escribir_dataset([self._nodo("bloquear_tiempo_pensar_calendario")])
        candidato = self._en_bandeja("apartar_ratos_pensar_semana")
        codigo, salida = self.forja(
            "insertar", candidato, "--sin-preguntas",
            "--veredicto", "bloquear_tiempo_pensar_calendario|SANO|"
                           "no son el mismo trabajo y sus entregables no se parecen")
        self.assertEqual(codigo, 0, salida)
        lineas = comun.leer_jsonl(self.veredictos)
        self.assertEqual(len(lineas), 1, salida)
        self.assertEqual(lineas[0]["veredicto"], "SANO")

    def test_un_REPITE_si_se_consuma_porque_no_imprime_rechazado(self):
        """La aduana juzgo y devolvio el candidato a su reparto: eso SI lo hizo."""
        self.escribir_dataset([self._nodo("bloquear_tiempo_pensar_calendario")])
        candidato = self._en_bandeja("apartar_ratos_pensar_semana")
        codigo, salida = self.forja(
            "insertar", candidato, "--sin-preguntas",
            "--veredicto", "bloquear_tiempo_pensar_calendario|REPITE|"
                           "no aniade ni un paso que la madre no tenga ya escrito")
        self.assertNotIn("RECHAZADO", salida)
        self.assertNotEqual(codigo, 0, salida)
        lineas = comun.leer_jsonl(self.veredictos)
        self.assertEqual(len(lineas), 1, salida)
        self.assertEqual(lineas[0]["veredicto"], "REPITE")
        self.assertEqual(self.nodos(), [self._nodo("bloquear_tiempo_pensar_calendario")])

    def test_el_gate_que_muerde_en_la_simulacion_tampoco_deja_linea(self):
        """El ultimo rechazo del camino, que es el mas tardio de todos."""
        madre = self._nodo("bloquear_tiempo_pensar_calendario")
        # Una arista rota deja el gate rojo en la simulacion sobre copia.
        madre["nodos_siguientes"] = ["un_nodo_que_no_existe_en_ninguna_parte"]
        self.escribir_dataset([madre])
        candidato = self._en_bandeja("apartar_ratos_pensar_semana")
        codigo, salida = self.forja(
            "insertar", candidato, "--sin-preguntas",
            "--veredicto", "bloquear_tiempo_pensar_calendario|SANO|"
                           "no son el mismo trabajo y sus entregables no se parecen")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("RECHAZADO POR EL GATE", salida)
        self.assertEqual(comun.leer_jsonl(self.veredictos), [], salida)

    # ------------------------------------------------ 2.b la arista en cola

    def test_caso_positivo_CONTINUA_con_el_otro_extremo_EN_BANDEJA_se_escribe(self):
        """`D.29`: el veredicto se escribe AHORA y la arista se cablea DESPUES."""
        self._en_bandeja("bloquear_tiempo_pensar_calendario")
        candidato = self._en_bandeja("reservar_horas_pensar_agenda")
        codigo, salida = self.forja(
            "insertar", candidato, "--sin-preguntas",
            "--veredicto", "bloquear_tiempo_pensar_calendario|CONTINUA|"
                           "madre=bloquear_tiempo_pensar_calendario|"
                           "el hijo despliega en tres pasos lo que la madre nombra "
                           "en una sola linea de su paso 2")
        self.assertEqual(codigo, 0, salida)
        self.assertIn("ARISTA EN COLA", salida)
        lineas = comun.leer_jsonl(self.veredictos)
        self.assertEqual(len(lineas), 1, salida)
        self.assertEqual(lineas[0]["veredicto"], "CONTINUA")
        self.assertEqual(lineas[0]["arista_en_cola"], True)
        # EL GRAFO NO SE CABLEA CONTRA UN ID QUE NO VIVE, que es la mitad que
        # `D.29` protege: la linea no miente y el grafo no se rompe.
        entrado = dict((n["id"], n) for n in self.nodos())
        self.assertEqual(entrado["reservar_horas_pensar_agenda"]["nodos_previos"], [])
        self.assertEqual(entrado["reservar_horas_pensar_agenda"]["nodos_siguientes"], [])
        self.anotar("COLA", "CONTINUA con el otro extremo en bandeja: veredicto escrito, "
                            "arista en cola")

    def test_caso_negativo_si_el_otro_extremo_VIVE_la_arista_se_cablea_igual(self):
        """Lo que se difiere es el cableado imposible, no todos los cableados."""
        self.escribir_dataset([self._nodo("bloquear_tiempo_pensar_calendario")])
        candidato = self._en_bandeja("reservar_horas_pensar_agenda")
        codigo, salida = self.forja(
            "insertar", candidato, "--sin-preguntas",
            "--veredicto", "bloquear_tiempo_pensar_calendario|CONTINUA|"
                           "madre=bloquear_tiempo_pensar_calendario|"
                           "el hijo despliega en tres pasos lo que la madre nombra")
        self.assertEqual(codigo, 0, salida)
        self.assertNotIn("ARISTA EN COLA", salida)
        self.assertIn("arista madre-hijo cableada", salida)
        lineas = comun.leer_jsonl(self.veredictos)
        self.assertNotIn("arista_en_cola", lineas[0])
        entrado = dict((n["id"], n) for n in self.nodos())
        self.assertEqual(entrado["reservar_horas_pensar_agenda"]["nodos_previos"],
                         ["bloquear_tiempo_pensar_calendario"])

    def test_la_clase_sigue_siendo_CONTINUA_y_no_se_degrada_a_SANO(self):
        """La vara de `6.1` no se mueve: escribir `SANO` seria caida de CLASE."""
        self._en_bandeja("bloquear_tiempo_pensar_calendario")
        candidato = self._en_bandeja("reservar_horas_pensar_agenda")
        self.forja("insertar", candidato, "--sin-preguntas",
                   "--veredicto", "bloquear_tiempo_pensar_calendario|CONTINUA|"
                                  "madre=bloquear_tiempo_pensar_calendario|"
                                  "el hijo despliega lo que la madre nombra")
        lineas = comun.leer_jsonl(self.veredictos)
        self.assertEqual(lineas[0]["veredicto"], "CONTINUA")
        self.assertEqual(lineas[0]["arista"],
                         "bloquear_tiempo_pensar_calendario > reservar_horas_pensar_agenda")

    def test_la_guarda_de_D8_SIGUE_MORDIENDO_un_CONTINUA_sin_razon(self):
        """Y al morder tampoco deja linea: las dos mitades a la vez."""
        self._en_bandeja("bloquear_tiempo_pensar_calendario")
        candidato = self._en_bandeja("reservar_horas_pensar_agenda")
        codigo, salida = self.forja(
            "insertar", candidato, "--sin-preguntas",
            "--veredicto", "bloquear_tiempo_pensar_calendario|CONTINUA|"
                           "madre=bloquear_tiempo_pensar_calendario|   ")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("sin razon escrita", salida)
        self.assertEqual(comun.leer_jsonl(self.veredictos), [], salida)

    def test_un_id_que_no_esta_NI_EN_EL_GRAFO_NI_EN_BANDEJA_se_sigue_rechazando(self):
        """Una arista en cola tiene los dos extremos escritos en alguna parte."""
        self.escribir_dataset([self._nodo("bloquear_tiempo_pensar_calendario")])
        candidato = self._en_bandeja("reservar_horas_pensar_agenda")
        codigo, salida = self.forja(
            "insertar", candidato, "--sin-preguntas",
            "--veredicto", "bloquear_tiempo_pensar_calendario|SANO|"
                           "no son el mismo trabajo ni se solapan en su entregable",
            "--veredicto", "nodo_que_nadie_escribio_nunca|CONTINUA|"
                           "madre=nodo_que_nadie_escribio_nunca|"
                           "el hijo despliega lo que la madre nombra")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("ni en el grafo ni en las bandejas", salida)
        self.assertEqual(comun.leer_jsonl(self.veredictos), [], salida)

    def test_una_lectura_declarada_contra_un_candidato_de_bandeja_entra_en_cola(self):
        """`D.37` y `D.29` a la vez: la serie se declara aunque la parte espere."""
        self._en_bandeja("revisar_presupuesto_compras_trimestre",
                         texto=("reunir al equipo cada trimestre para repasar el "
                                "presupuesto de compras y firmar las desviaciones"),
                         pasos=["Convocar al equipo de compras.",
                                "Repasar las partidas del trimestre.",
                                "Firmar cada desviacion encontrada."])
        candidato = self._en_bandeja("reservar_horas_pensar_agenda")
        codigo, salida = self.forja(
            "insertar", candidato, "--sin-preguntas",
            "--veredicto", "revisar_presupuesto_compras_trimestre|CONTINUA|"
                           "madre=reservar_horas_pensar_agenda|"
                           "la madre nombra el repaso trimestral en su paso 2 y el hijo "
                           "lo despliega en tres pasos que ella no tiene")
        self.assertEqual(codigo, 0, salida)
        self.assertIn("DECLARADOS POR LECTURA", salida)
        self.assertIn("ARISTA EN COLA", salida)
        lineas = comun.leer_jsonl(self.veredictos)
        self.assertEqual(lineas[0]["levantada_por"], ["lectura declarada"])
        self.assertEqual(lineas[0]["arista_en_cola"], True)



class PruebaAnotacionDeclarada(BaseForja):
    """La operacion que anota una linea YA ESCRITA de la bitacora.

    `EXTRACTOR.md` 14 pone `bitacora/` bajo la aduana y prohibe tocarla a mano; el
    manual, principio 6, manda corregir sin borrar. **Entre las dos quedaba un
    hueco: una linea ya escrita que hay que marcar no tenia via.** La `ACTA 27`
    `5.2` lo encargo con estas palabras: *se marcan por operacion, con su razon,
    igual que hiciste con `corregir`*.
    """

    MARCA = "CORRECCION DECLARADA"

    def _una_linea(self, candidato="recorrer_rueda_hacer_cosas_equipo",
                   vecino="recorrer_rueda_conscientemente_cultura_equipo",
                   clase="CONTINUA", razon="la madre lo nombra en su paso 4"):
        return {"fecha": "2026-09-16", "candidato": candidato, "vecino": vecino,
                "huella_candidato": "aaaa", "huella_vecino": "bbbb",
                "senales": {}, "levantada_por": ["lectura declarada"],
                "veredicto": clase, "razon": razon,
                "arista": "%s > %s" % (vecino, candidato)}

    def _un_nodo_vivo(self, identificador):
        return {"id": identificador, "titulo": identificador.replace("_", " "),
                "resumen_teorico": "un texto cualquiera de " + identificador,
                "condiciones_activacion": "cuando toque", "entregable_esperado": "algo",
                "pasos_accionables": ["Uno.", "Dos."], "dominio": "gestion",
                "estado": "vivo",
                "fuentes": [{"clave": "manual_sistema_conocimiento",
                             "fecha": "2026-09-16"}],
                "denominaciones": {"nombre_largo": identificador.replace("_", " "),
                                   "otros_idiomas": [], "sigla": ""},
                "ids_alias": [], "nodos_previos": [], "nodos_siguientes": [],
                "atribuciones": []}

    def _anotar(self, *argumentos):
        return self.forja("anotar", *argumentos)

    def test_la_anotacion_se_escribe_y_la_razon_vieja_sigue_entera(self):
        vieja = self._una_linea()
        comun.escribir_jsonl(self.veredictos, [self._una_linea(clase="SANO"), vieja])
        texto = (self.MARCA + " del 16 sep 2026: esta linea la escribio una corrida "
                 "que imprimio RECHAZADO y no inserto nada.")
        codigo, salida = self._anotar(
            "--linea", "2", "--anade", texto,
            "--razon", "la corrida imprimio NADA SE INSERTO en la misma salida")
        self.assertEqual(codigo, 0, salida)
        filas = comun.leer_jsonl(self.veredictos)
        self.assertEqual(len(filas), 2)
        self.assertIn(vieja["razon"], filas[1]["razon"])
        self.assertIn(texto, filas[1]["razon"])
        self.assertEqual(filas[1]["anotaciones"][0]["texto"], texto)
        self.anotar("ANOTAR", "una linea de la bitacora se marca por operacion, "
                              "con su razon y sin borrar")

    def test_caso_positivo_ninguna_otra_linea_se_toca(self):
        """La bitacora se reescribe entera: que solo cambie una es una medida."""
        primera = self._una_linea(clase="SANO", razon="no son el mismo trabajo")
        tercera = self._una_linea(candidato="otro_nodo", clase="SANO",
                                  razon="tampoco son el mismo trabajo")
        comun.escribir_jsonl(self.veredictos, [primera, self._una_linea(), tercera])
        codigo, salida = self._anotar(
            "--linea", "2",
            "--anade", self.MARCA + " del 16 sep 2026: corrida no consumada, no inserto.",
            "--razon", "la corrida imprimio NADA SE INSERTO")
        self.assertEqual(codigo, 0, salida)
        filas = comun.leer_jsonl(self.veredictos)
        self.assertEqual(filas[0], primera)
        self.assertEqual(filas[2], tercera)
        self.assertIn("Las otras 2, intactas", salida)

    def test_caso_positivo_ni_la_clase_ni_el_par_ni_las_huellas_se_mueven(self):
        """Cambiar un veredicto es volver a juzgar el par, no anotar su linea."""
        vieja = self._una_linea()
        comun.escribir_jsonl(self.veredictos, [vieja])
        codigo, salida = self._anotar(
            "--linea", "1",
            "--anade", self.MARCA + " del 16 sep 2026: corrida no consumada, no inserto.",
            "--razon", "la corrida imprimio NADA SE INSERTO")
        self.assertEqual(codigo, 0, salida)
        nueva = comun.leer_jsonl(self.veredictos)[0]
        for campo in ("candidato", "vecino", "veredicto", "arista", "fecha",
                      "huella_candidato", "huella_vecino", "senales", "levantada_por"):
            self.assertEqual(nueva.get(campo), vieja.get(campo), campo)

    def test_no_consumada_saca_la_linea_de_la_vigencia_y_deja_su_cuenta(self):
        """`ACTA 27` `5.3.b`: las cuatro fantasma desaparecen al declararse."""
        comun.escribir_jsonl(self.veredictos, [self._una_linea()])
        self.escribir_dataset([])
        antes = self.forja("rancios")
        self.assertIn("NODO IDO", antes[1])
        codigo, salida = self._anotar(
            "--linea", "1",
            "--anade", self.MARCA + " del 16 sep 2026: corrida no consumada, no inserto.",
            "--razon", "la corrida imprimio NADA SE INSERTO",
            "--no-consumada")
        self.assertEqual(codigo, 0, salida)
        despues = self.forja("rancios")
        self.assertNotIn("NODO IDO", despues[1])
        # LA GUARDA QUE NO MUERDE ES CIFRA: la linea sale de la medida pero NO
        # sale de la cuenta.
        self.assertIn("NO CONSUMADAS y por eso no medidas: 1", despues[1])

    def test_caso_positivo_una_linea_SIN_marcar_sigue_mordiendo(self):
        """Una guarda que se afloja para todos no es una guarda."""
        comun.escribir_jsonl(self.veredictos, [self._una_linea()])
        self.escribir_dataset([])
        codigo, salida = self.forja("rancios")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("NODO IDO", salida)
        self.assertNotIn("NO CONSUMADAS", salida)

    def test_sin_la_marca_de_D35_la_anotacion_no_corre(self):
        comun.escribir_jsonl(self.veredictos, [self._una_linea()])
        codigo, salida = self._anotar(
            "--linea", "1",
            "--anade", "esta linea no se consumo, la escribio una corrida rechazada",
            "--razon", "la corrida imprimio NADA SE INSERTO")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("no se declara como lo que es", salida)
        self.assertEqual(comun.leer_jsonl(self.veredictos), [self._una_linea()])

    def test_la_marca_de_VIGENCIA_DECLARADA_tambien_vale_y_no_borra_el_hallazgo(self):
        """`D.15` segunda salida: se declara por que sigue valiendo.

        **Y la declaracion NO retira el hallazgo.** Cambiar lo que la guarda
        considera `RANCIO` seria mover la vara de `D.15`, y eso se propone a
        Alexis, no se hace en una vuelta.
        """
        linea = self._una_linea(clase="SANO", razon="no son el mismo trabajo")
        linea["huella_vecino"] = "una_huella_vieja"
        comun.escribir_jsonl(self.veredictos, [linea])
        self.escribir_dataset([self._un_nodo_vivo("recorrer_rueda_hacer_cosas_equipo"),
                               self._un_nodo_vivo(
                                   "recorrer_rueda_conscientemente_cultura_equipo")])
        antes = self.forja("rancios")
        self.assertIn("RANCIO", antes[1])
        codigo, salida = self._anotar(
            "--linea", "1",
            "--anade", "VIGENCIA DECLARADA del 16 sep 2026: sigue valiendo porque el "
                       "unico cambio fue prosa aniadida al resumen_teorico.",
            "--razon", "la operacion corregir solo toca resumen_teorico")
        self.assertEqual(codigo, 0, salida)
        despues = self.forja("rancios")
        self.assertIn("RANCIO", despues[1])
        self.assertIn("VIGENCIA DECLARADA",
                      comun.leer_jsonl(self.veredictos)[0]["razon"])

    def test_la_vigencia_mide_GRAFO_MAS_BANDEJAS_y_no_solo_el_grafo(self):
        """`D.38.4` y `D.38.5`: un vecino de bandeja no se fue, aun no ha llegado."""
        nodo = self._un_nodo_vivo("recorrer_rueda_hacer_cosas_equipo")
        vecino = self._un_nodo_vivo("recorrer_rueda_conscientemente_cultura_equipo")
        linea = self._una_linea(clase="SANO", razon="no son el mismo trabajo")
        linea["huella_candidato"] = comun.huella_de_nodo(nodo)
        linea["huella_vecino"] = comun.huella_de_nodo(vecino)
        comun.escribir_jsonl(self.veredictos, [linea])
        self.escribir_dataset([nodo])
        carpeta = os.path.join(self.bandeja, "un_lote")
        os.makedirs(carpeta)
        comun.escribir_texto(os.path.join(carpeta, vecino["id"] + ".json"),
                             json.dumps(vecino, ensure_ascii=False))
        codigo, salida = self.forja("rancios")
        self.assertEqual(codigo, 0, salida)
        self.assertIn("BLOQUE DE VIGENCIA VERDE", salida)

    def test_caso_positivo_un_vecino_que_NO_esta_en_ninguna_de_las_dos_sigue_IDO(self):
        """Ensanchar la poblacion no es dejar de mirar."""
        nodo = self._un_nodo_vivo("recorrer_rueda_hacer_cosas_equipo")
        linea = self._una_linea(clase="SANO", razon="no son el mismo trabajo")
        linea["huella_candidato"] = comun.huella_de_nodo(nodo)
        linea["huella_vecino"] = "lo_que_sea"
        comun.escribir_jsonl(self.veredictos, [linea])
        self.escribir_dataset([nodo])
        codigo, salida = self.forja("rancios")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("NODO IDO", salida)

    def test_la_huella_de_un_nodo_VACIO_no_es_una_huella(self):
        """`D.15` ya tiene su casilla: SIN HUELLA, incomprobable y declarado."""
        nodo = self._un_nodo_vivo("recorrer_rueda_hacer_cosas_equipo")
        vecino = self._un_nodo_vivo("recorrer_rueda_conscientemente_cultura_equipo")
        linea = self._una_linea(clase="SANO", razon="no son el mismo trabajo")
        linea["huella_candidato"] = comun.huella_de_nodo(nodo)
        linea["huella_vecino"] = comun.huella_de_nodo({})
        comun.escribir_jsonl(self.veredictos, [linea])
        self.escribir_dataset([nodo, vecino])
        codigo, salida = self.forja("rancios")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("SIN HUELLA", salida)
        self.assertIn("es la de un nodo VACIO", salida)

    def test_sin_razon_escrita_no_se_anota(self):
        comun.escribir_jsonl(self.veredictos, [self._una_linea()])
        codigo, salida = self._anotar(
            "--linea", "1",
            "--anade", self.MARCA + " del 16 sep 2026: corrida no consumada, no inserto.",
            "--razon", "   ")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("sin razon escrita", salida)

    def test_una_linea_que_no_existe_es_rechazo(self):
        comun.escribir_jsonl(self.veredictos, [self._una_linea()])
        codigo, salida = self._anotar(
            "--linea", "9",
            "--anade", self.MARCA + " del 16 sep 2026: corrida no consumada, no inserto.",
            "--razon", "la corrida imprimio NADA SE INSERTO")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("esa linea no existe", salida)

    def test_la_misma_anotacion_no_se_declara_dos_veces(self):
        comun.escribir_jsonl(self.veredictos, [self._una_linea()])
        texto = self.MARCA + " del 16 sep 2026: corrida no consumada, no inserto nada."
        primera = self._anotar("--linea", "1", "--anade", texto,
                               "--razon", "la corrida imprimio NADA SE INSERTO")
        self.assertEqual(primera[0], 0, primera[1])
        segunda = self._anotar("--linea", "1", "--anade", texto,
                               "--razon", "la corrida imprimio NADA SE INSERTO")
        self.assertEqual(segunda[0], 1, segunda[1])
        self.assertIn("ya esta escrita", segunda[1])

    def test_el_guion_largo_tumba_la_anotacion(self):
        comun.escribir_jsonl(self.veredictos, [self._una_linea()])
        codigo, salida = self._anotar(
            "--linea", "1",
            # EL GUION LARGO SE CONSTRUYE, NO SE TECLEA: el barrido de esta casa
            # es sobre el repo entero y tumbaria el propio fichero de pruebas.
            "--anade", self.MARCA + " del 16 sep 2026: corrida " + chr(0x2014)
                       + " no consumada, no inserto nada.",
            "--razon", "la corrida imprimio NADA SE INSERTO")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("guiones largos", salida)

    def test_esta_operacion_no_toca_el_dataset(self):
        nodo = {"id": "recorrer_rueda_hacer_cosas_equipo",
                "titulo": "recorrer la rueda", "resumen_teorico": "un texto",
                "condiciones_activacion": "cuando toque", "entregable_esperado": "algo",
                "pasos_accionables": ["Uno.", "Dos."], "dominio": "gestion",
                "estado": "vivo",
                "fuentes": [{"clave": "manual_sistema_conocimiento",
                             "fecha": "2026-09-16"}],
                "denominaciones": {"nombre_largo": "recorrer la rueda",
                                   "otros_idiomas": [], "sigla": ""},
                "ids_alias": [], "nodos_previos": [], "nodos_siguientes": [],
                "atribuciones": []}
        self.escribir_dataset([nodo])
        self.assertEqual(comun.leer_jsonl(self.veredictos), [])
        comun.escribir_jsonl(self.veredictos, [self._una_linea()])
        codigo, salida = self._anotar(
            "--linea", "1",
            "--anade", self.MARCA + " del 16 sep 2026: corrida no consumada, no inserto.",
            "--razon", "la corrida imprimio NADA SE INSERTO")
        self.assertEqual(codigo, 0, salida)
        self.assertEqual(self.nodos(), [nodo])



class PruebaVigenciaNoEsGuarda(BaseForja):
    """`D.15` DICE QUE LA VIGENCIA NO PONE NADA EN ROJO, Y EL CIERRE LA TENIA DENTRO.

    `scripts/cerrar_reporte.py` metia `forja.py rancios` entre las guardas cuyo
    fallo devuelve `CIERRE EN ROJO`. `D.15` dice lo contrario con estas palabras:
    *se relee con el texto de hoy, o se declara por que sigue valiendo. Las dos
    cosas las hace una persona, y por eso esto NO pone el gate en rojo.*

    **ENTRE UNA REGLA ESCRITA Y UN CODIGO QUE LA CONTRADICE MANDA LA REGLA**
    (`ACTA 27` `5.3.a`).

    Y NO SE AFLOJA: `rancios` sigue corriendo, sigue imprimiendo sus hallazgos y
    **el cierre sigue publicando su cuenta.** *La guarda que no muerde es cifra*
    (cosecha `7.C`). Lo unico que cambia es que **contar una cola no es caerse.**

    EL FRENO DE RECURSION, y va dicho porque se nota al leer: el cierre de vuelta
    corre `tests/test_aceptacion.py`, que es ESTE fichero. Estas dos pruebas lo
    llaman, asi que marcan el entorno del hijo y **se saltan a si mismas cuando
    ven la marca puesta.** Un nivel de anidamiento, no infinitos, y el cierre que
    se mide por dentro sigue siendo el de verdad.
    """

    MARCA_ANIDADA = "FORJA_PRUEBA_DE_CIERRE"

    def _un_nodo(self, identificador="recorrer_rueda_hacer_cosas_equipo"):
        return {"id": identificador, "titulo": identificador.replace("_", " "),
                "resumen_teorico": "un texto cualquiera de " + identificador,
                "condiciones_activacion": "cuando toque", "entregable_esperado": "algo",
                "pasos_accionables": ["Uno.", "Dos."], "dominio": "gestion",
                "estado": "vivo",
                "fuentes": [{"clave": "manual_sistema_conocimiento",
                             "fecha": "2026-09-16"}],
                "denominaciones": {"nombre_largo": identificador.replace("_", " "),
                                   "otros_idiomas": [], "sigla": ""},
                "ids_alias": [], "nodos_previos": [], "nodos_siguientes": [],
                "atribuciones": []}

    def _con_un_rancio(self, nodo=None):
        nodo = nodo or self._un_nodo()
        self.escribir_dataset([nodo])
        comun.escribir_jsonl(self.veredictos, [{
            "fecha": "2026-09-13", "candidato": nodo["id"], "vecino": nodo["id"],
            "huella_candidato": "una_huella_que_ya_no_es",
            "huella_vecino": "una_huella_que_ya_no_es",
            "senales": {}, "levantada_por": ["lectura declarada"],
            "veredicto": "SANO", "razon": "no son el mismo trabajo", "arista": ""}])

    def _cerrar(self):
        entorno = dict(self.entorno)
        entorno[self.MARCA_ANIDADA] = "1"
        proceso = subprocess.Popen(
            [sys.executable, os.path.join("scripts", "cerrar_reporte.py")],
            cwd=RAIZ, env=entorno,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        crudo = proceso.communicate()[0]
        return proceso.returncode, crudo.decode("utf-8", "replace")

    def test_la_vigencia_en_rojo_por_su_cuenta_SIGUE_devolviendo_1(self):
        """La guarda no se afloja: sigue mordiendo cuando se la llama sola."""
        self._con_un_rancio()
        codigo, salida = self.forja("rancios")
        self.assertEqual(codigo, 1, salida)
        self.assertIn("RANCIO", salida)
        self.anotar("VIGENCIA", "la vigencia muerde sola y NO tumba el cierre (D.15)")

    def test_el_cierre_NO_se_pone_en_rojo_por_ella_Y_SIGUE_publicando_su_cuenta(self):
        """Si el arreglo hace que la cuenta deje de imprimirse, esta mal hecho."""
        if os.environ.get(self.MARCA_ANIDADA):
            self.skipTest("corriendo DENTRO del cierre: freno de recursion")
        self._con_un_rancio()
        _codigo, salida = self._cerrar()
        # LA CUENTA SIGUE SALIENDO, que es la mitad que no se puede perder.
        self.assertIn("vigencia de los veredictos (D.15)", salida)
        self.assertIn("BLOQUE DE VIGENCIA", salida)
        self.assertIn("LA VIGENCIA TIENE COLA", salida)
        # Y NO ENTRA EN LA LISTA DE LOS QUE TUMBAN, que es lo que se mide aqui.
        #
        # NO se mide `codigo == 0`, y va dicho: el cierre que esta prueba lanza
        # corre contra el taller de usar y tirar, donde el gate tiene un dataset
        # de un solo nodo y la prueba de aceptacion anidada se salta la mitad de
        # sus casos. Esos dos pueden caerse por el taller y no por la vigencia.
        # **La afirmacion exacta es que la vigencia NO figura entre los caidos.**
        for linea in salida.splitlines():
            if linea.startswith("CIERRE EN ROJO. No pasa:"):
                self.assertNotIn("vigencia", linea)

    def test_caso_positivo_el_gate_en_rojo_SI_tumba_el_cierre(self):
        """Una vigencia que no tumba no puede volver blando a todo lo demas."""
        if os.environ.get(self.MARCA_ANIDADA):
            self.skipTest("corriendo DENTRO del cierre: freno de recursion")
        roto = self._un_nodo()
        roto["nodos_siguientes"] = ["un_nodo_que_no_existe_en_ninguna_parte"]
        self._con_un_rancio(roto)
        codigo, salida = self._cerrar()
        self.assertNotEqual(codigo, 0, salida)
        self.assertIn("CIERRE EN ROJO", salida)
        self.assertIn("gate de integridad", salida)


class PruebaCerrojoYCenso(BaseForja):
    """LAS DOS REDES QUE LA CAIDA DE LA VUELTA 28 DEJO AL DESCUBIERTO.

    Un nodo entro y desaparecio **con el gate en VERDE**: una corrida leyo el
    dataset, otra escribio el suyo, y la primera volco su copia en memoria dejando
    fuera lo que la segunda habia metido. **Un grafo al que le quitan un nodo entero
    sigue siendo coherente, solo que mas pequenio.**

    Son dos redes a dos alturas: **el cerrojo impide que pase**; **`D.44` impide que
    una perdida llegue a un commit.**
    """

    def test_el_cerrojo_es_exclusivo(self):
        from src import cerrojo
        ruta = os.path.join(self.taller, "nodos.jsonl")
        with cerrojo.tomar(ruta):
            self.assertTrue(os.path.exists(cerrojo.ruta_de(ruta)))
            # CASO POSITIVO: el segundo NO entra. Con tope corto para no esperar.
            segundo = cerrojo.tomar(ruta, espera=0.01, tope=0.05)
            self.assertRaises(cerrojo.CerrojoOcupado, segundo.__enter__)
        # Y AL SALIR SE SUELTA, pase lo que pase.
        self.assertFalse(os.path.exists(cerrojo.ruta_de(ruta)))
        self.anotar("cerrojo", "el segundo espera y nunca pisa")

    def test_el_cerrojo_se_suelta_aunque_reviente_lo_de_dentro(self):
        """Un cerrojo que se queda puesto bloquea la casa para siempre."""
        from src import cerrojo
        ruta = os.path.join(self.taller, "nodos.jsonl")
        try:
            with cerrojo.tomar(ruta):
                raise ValueError("algo revienta dentro")
        except ValueError:
            pass
        self.assertFalse(os.path.exists(cerrojo.ruta_de(ruta)))

    def test_un_cerrojo_huerfano_se_rompe_pero_nunca_en_silencio(self):
        from src import cerrojo
        import json as _json
        ruta = os.path.join(self.taller, "nodos.jsonl")
        # Un proceso que no existe y un cerrojo viejo.
        comun.escribir_texto(cerrojo.ruta_de(ruta),
                             _json.dumps({"pid": 999999999, "desde": 0}))
        dichos = []
        with cerrojo.tomar(ruta, espera=0.01, tope=2, avisar=dichos.append):
            pass
        self.assertTrue(any("HUERFANO" in d for d in dichos), dichos)

    def test_caso_positivo_dos_inserciones_a_la_vez_y_ninguna_pisa(self):
        """Es la caida de la vuelta 28, reproducida contra la aduana de verdad."""
        import subprocess
        self.sembrar_ejemplo()
        uno = self.fixture("hijo_valido.json")
        if not os.path.exists(uno):
            self.skipTest("sin fixture de candidato")
        antes = len(self.nodos())
        procesos = [subprocess.Popen(
            [sys.executable, "forja.py", "insertar", uno, "--sin-preguntas"],
            cwd=RAIZ, env=self.entorno, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT) for _ in range(2)]
        for proceso in procesos:
            proceso.communicate()
        # NINGUNA PIERDE NADA: o entra uno, o entra uno y el otro choca por id.
        self.assertGreaterEqual(len(self.nodos()), antes)

    # ------------------------------------------------------------------ D.44
    def test_caso_positivo_un_nodo_que_desaparece_tumba_el_gate(self):
        """`D.44`, con el nodo de verdad que la vuelta 28 perdio.

        Antes de esta guarda, quitar un nodo entero dejaba el gate **VERDE**.
        """
        from src import gate
        nodos = comun.leer_jsonl(comun.RUTA_DATASET)
        if not nodos:
            self.skipTest("sin dataset de verdad")
        sin_uno = nodos[1:]
        fallos = gate.censo_no_decrece(sin_uno)
        self.assertTrue(fallos)
        self.assertIn(nodos[0]["id"], str(fallos[0]))
        self.anotar("D44", "un nodo que desaparece: el gate ya lo ve")

    def test_caso_negativo_el_arbol_tal_como_esta_pasa(self):
        from src import gate
        nodos = comun.leer_jsonl(comun.RUTA_DATASET)
        if not nodos:
            self.skipTest("sin dataset de verdad")
        self.assertEqual(gate.censo_no_decrece(nodos), [])

    def test_caso_negativo_un_nodo_deprecado_sigue_estando_y_pasa(self):
        """`D.17`: un nodo que sale de superficie NO se borra, se marca."""
        from src import gate
        nodos = comun.leer_jsonl(comun.RUTA_DATASET)
        if not nodos:
            self.skipTest("sin dataset de verdad")
        copia = [dict(n) for n in nodos]
        copia[0]["estado"] = "deprecado"
        self.assertEqual(gate.censo_no_decrece(copia), [])

    def test_sin_commit_anterior_no_hay_nada_que_comparar(self):
        """Un repo recien nacido, o un dataset de usar y tirar, no es un fallo."""
        from src import gate
        self.assertEqual(
            gate.censo_no_decrece([], ruta_dataset=os.path.join(
                self.taller, "no_commiteado.jsonl")), [])


class PruebaTableroDeFrentes(BaseForja):
    """UN LIBRO, UN DUEÑO A LA VEZ (D.49) Y EL RELEVO (D.50), 17 sep 2026.

    D.32 abre el lote siguiente SIN PARADA en cuanto uno cierra. El siguiente por orden
    era `marquet_turn_the_ship`, **que se estaba extrayendo en otra rama con 9
    candidatos dentro**, y lo unico que lo impedia era una frase escrita a mano en el
    encargo. D.35: un remedio que se cumple acordandose no es un remedio.
    """

    def _filas(self):
        return [
            {"lote": 4, "clave": "scott_radical_candor", "rama": "",
             "estado": "CERRADO EN EXTRACCION", "dueno": "serial",
             "candidatos_en_bandeja": 75, "ultimo_capitulo": "cap_14"},
            {"lote": 5, "clave": "marquet_turn_the_ship",
             "rama": "extraccion-marquet_turn_the_ship", "estado": "PAUSADO",
             "dueno": "NINGUNO", "candidatos_en_bandeja": 9,
             "bandeja_medida_en": "C:/Users/x/forja-marquet_turn_the_ship/cuarentena",
             "ultimo_capitulo": "cap_03"},
            {"lote": 6, "clave": "openstax_business_ethics", "rama": "",
             "estado": "SIN EMPEZAR", "dueno": "NINGUNO",
             "candidatos_en_bandeja": 0, "ultimo_capitulo": ""},
            {"lote": 7, "clave": "grove_high_output",
             "rama": "extraccion-grove_high_output", "estado": "EN CURSO",
             "dueno": "grove_high_output", "candidatos_en_bandeja": 23,
             "ultimo_capitulo": "cap_03"},
            {"lote": 9, "clave": "gerber_emyth", "rama": "extraccion-gerber_emyth",
             "estado": "COSECHADO", "dueno": "NINGUNO",
             "candidatos_en_bandeja": 10, "ultimo_capitulo": "cap_11"},
        ]

    # ------------------------------------------------------- D.49, el dueño manda

    def test_caso_positivo_un_libro_con_dueno_ajeno_no_se_abre(self):
        """Es grove: EN CURSO en otra rama. La serial no lo toca."""
        from src import tablero
        vale, motivo = tablero.puede_abrir("grove_high_output", "serial", self._filas())
        self.assertFalse(vale)
        self.assertIn("TIENE DUEÑO Y NO ERES TU", motivo)
        self.assertIn("grove_high_output", motivo)

    def test_caso_positivo_pausado_sin_cosechar_tampoco_se_abre(self):
        """Es marquet, y es la caida que D.49 vino a impedir: dueño NINGUNO, pero sus
        9 candidatos no han llegado a esta rama."""
        from src import tablero
        vale, motivo = tablero.puede_abrir("marquet_turn_the_ship", "serial",
                                           self._filas())
        self.assertFalse(vale)
        self.assertIn("PAUSADO y NO COSECHADO", motivo)
        self.assertIn("9 candidato", motivo)

    def test_caso_negativo_sin_empezar_y_sin_dueno_si_se_abre(self):
        from src import tablero
        vale, motivo = tablero.puede_abrir("openstax_business_ethics", "serial",
                                           self._filas())
        self.assertTrue(vale)

    def test_caso_negativo_cosechado_y_sin_dueno_si_se_continua(self):
        """D.50 (d): se continua desde el capitulo SIGUIENTE al ultimo minado."""
        from src import tablero
        vale, motivo = tablero.puede_abrir("gerber_emyth", "serial", self._filas())
        self.assertTrue(vale)
        self.assertIn("cap_11", motivo)

    def test_su_propio_dueno_si_lo_continua(self):
        from src import tablero
        vale, _ = tablero.puede_abrir("grove_high_output", "grove_high_output",
                                      self._filas())
        self.assertTrue(vale)

    def test_un_libro_sin_fila_no_se_abre(self):
        """Un libro sin fila no se abre: primero se mide. Nunca por omision."""
        from src import tablero
        vale, motivo = tablero.puede_abrir("libro_que_no_existe", "serial",
                                           self._filas())
        self.assertFalse(vale)
        self.assertIn("no tiene fila", motivo)

    # -------------------------------------------------- el orden, y a quien saltar

    def test_el_siguiente_libre_salta_los_que_tienen_trabajo_en_otra_rama(self):
        """La serial NO va al lote 5: va al 6, que es el primero que puede tomar."""
        from src import tablero
        clave, _ = tablero.siguiente_libre("serial", self._filas())
        self.assertEqual(clave, "openstax_business_ethics")

    def test_los_relevables_salen_en_orden_de_lote(self):
        from src import tablero
        claves = [f["clave"] for f in tablero.relevables(self._filas())]
        self.assertEqual(claves, ["marquet_turn_the_ship", "grove_high_output"])

    # ------------------------------------------ lo declarado, que va con su cita

    def test_una_declaracion_sin_cita_detiene_el_instrumento(self):
        from src import tablero
        ruta = os.path.join(self.taller, "frentes.json")
        comun.escribir_texto(ruta, json.dumps(
            {"alcance": {"lineas_a_la_vez": 2}, "frente_activo": {"clave": "x"}}))
        anterior = tablero.RUTA_FRENTES
        tablero.RUTA_FRENTES = ruta
        self.addCleanup(lambda: setattr(tablero, "RUTA_FRENTES", anterior))
        with self.assertRaises(tablero.TableroMalDeclarado):
            tablero.declaraciones()

    def test_el_config_del_repo_lleva_todas_sus_citas(self):
        from src import tablero
        datos = tablero.declaraciones()
        self.assertTrue(datos["frente_activo"]["cita"])

    # ------------------------------------------------- lo medido contra el arbol

    def test_el_tablero_del_repo_tiene_una_fila_por_lote(self):
        """Si esto cae, D.49 deja de poder decidir sobre algun libro del orden."""
        from src import tablero
        claves_del_orden = [c for _, c in tablero.lotes()]
        escrito = [f["clave"] for f in tablero.leer()]
        self.assertEqual(sorted(escrito), sorted(claves_del_orden))

    def test_ningun_estado_del_tablero_esta_fuera_de_los_seis(self):
        from src import tablero
        for fila in tablero.leer():
            self.assertIn(fila["estado"], tablero.ESTADOS,
                          "%s tiene un estado que D.49 no define" % fila["clave"])


class PruebaOrdenDePrioridad(BaseForja):
    """EL ORDEN LO DA EL TABLERO (D.51, 17 sep 2026, decision del fundador).

    D.49 y D.50 sabian decir que NO. Lo que ninguna sabia decir es cual SI, y ese hueco
    lo llenaba el orden de ORDEN_DE_LOTES.md, que es el orden en que los libros
    LLEGARON y no el orden en que VALEN.
    """

    def _filas(self, **cambios):
        base = [
            {"lote": 4, "clave": "scott_radical_candor", "rama": "",
             "estado": "CERRADO EN EXTRACCION", "dueno": "serial", "prioridad": None,
             "fuera_de_campania": False, "candidatos_en_bandeja": 75,
             "ultimo_capitulo": "cap_14"},
            {"lote": 7, "clave": "grove_high_output",
             "rama": "extraccion-grove_high_output", "estado": "EN CURSO",
             "dueno": "grove_high_output", "prioridad": 1, "fuera_de_campania": False,
             "candidatos_en_bandeja": 23, "ultimo_capitulo": "cap_03"},
            {"lote": 9, "clave": "gerber_emyth", "rama": "extraccion-gerber_emyth",
             "estado": "PAUSADO", "dueno": "NINGUNO", "prioridad": 2,
             "fuera_de_campania": False, "candidatos_en_bandeja": 10,
             "bandeja_medida_en": "otro arbol", "ultimo_capitulo": "cap_11"},
            {"lote": 5, "clave": "marquet_turn_the_ship",
             "rama": "extraccion-marquet_turn_the_ship", "estado": "PAUSADO",
             "dueno": "NINGUNO", "prioridad": 3, "fuera_de_campania": False,
             "candidatos_en_bandeja": 9, "bandeja_medida_en": "otro arbol",
             "ultimo_capitulo": "cap_03"},
            {"lote": 8, "clave": "bernerslee_bananas", "rama": "",
             "estado": "SIN EMPEZAR", "dueno": "NINGUNO", "prioridad": 4,
             "fuera_de_campania": True, "candidatos_en_bandeja": 0,
             "ultimo_capitulo": ""},
            {"lote": 6, "clave": "openstax_business_ethics", "rama": "",
             "estado": "SIN EMPEZAR", "dueno": "NINGUNO", "prioridad": 5,
             "fuera_de_campania": True, "candidatos_en_bandeja": 0,
             "ultimo_capitulo": ""},
        ]
        for fila in base:
            if fila["clave"] in cambios:
                fila.update(cambios[fila["clave"]])
        return base

    # ------------------------------------------- mientras tiene libro, lo continua

    def test_con_libro_propio_en_curso_le_toca_ese(self):
        """D.50 releva AL CERRAR, no a mitad."""
        from src import tablero
        clave, _, _ = tablero.siguiente_por_prioridad("serial", self._filas())
        self.assertEqual(clave, "scott_radical_candor")

    # ------------------------------------- sin libro, manda la prioridad y no el lote

    def test_caso_positivo_sin_libro_no_elige_y_nombra_el_relevo_que_falta(self):
        """Es la parada util: NINGUNO, y dice cual necesita y que le falta."""
        from src import tablero
        filas = self._filas(scott_radical_candor={"estado": "INSERTADO",
                                                  "dueno": "NINGUNO"})
        clave, motivo, relevo = tablero.siguiente_por_prioridad("serial", filas)
        self.assertIsNone(clave)
        self.assertIsNotNone(relevo)
        self.assertEqual(relevo["clave"], "gerber_emyth")
        self.assertIn("no esta cosechada", motivo)

    def test_caso_negativo_con_el_de_prioridad_2_cosechado_le_toca_ese(self):
        from src import tablero
        filas = self._filas(
            scott_radical_candor={"estado": "INSERTADO", "dueno": "NINGUNO"},
            gerber_emyth={"estado": "COSECHADO"})
        clave, motivo, _ = tablero.siguiente_por_prioridad("serial", filas)
        self.assertEqual(clave, "gerber_emyth")
        self.assertIn("cap_11", motivo)

    def test_la_prioridad_manda_sobre_el_numero_de_lote(self):
        """marquet es el lote 5 y gerber el 9, y gerber va ANTES por prioridad."""
        from src import tablero
        filas = self._filas(
            scott_radical_candor={"estado": "INSERTADO", "dueno": "NINGUNO"},
            gerber_emyth={"estado": "COSECHADO"},
            marquet_turn_the_ship={"estado": "COSECHADO"})
        clave, _, _ = tablero.siguiente_por_prioridad("serial", filas)
        self.assertEqual(clave, "gerber_emyth")

    def test_caso_positivo_un_libro_fuera_de_campania_no_se_elige_nunca(self):
        """Estan SIN EMPEZAR y sin dueño, asi que D.49 los dejaria pasar. D.51 no."""
        from src import tablero
        filas = self._filas(
            scott_radical_candor={"estado": "INSERTADO", "dueno": "NINGUNO"},
            grove_high_output={"estado": "INSERTADO", "dueno": "NINGUNO"},
            gerber_emyth={"estado": "INSERTADO"},
            marquet_turn_the_ship={"estado": "INSERTADO"})
        clave, motivo, _ = tablero.siguiente_por_prioridad("serial", filas)
        self.assertIsNone(clave)
        self.assertIn("CIERRE DEL MUNDO 11", motivo)

    # ------------------------------------------------- el cierre del mundo 11

    def test_el_mundo_11_no_esta_completo_mientras_falte_uno(self):
        from src import tablero
        filas = self._filas(grove_high_output={"estado": "INSERTADO",
                                               "dueno": "NINGUNO"},
                            gerber_emyth={"estado": "INSERTADO"})
        completo, del_mundo, faltan = tablero.mundo_11_completo(filas)
        self.assertFalse(completo)
        self.assertEqual(len(del_mundo), 3)
        self.assertEqual([f["clave"] for f in faltan], ["marquet_turn_the_ship"])

    def test_el_mundo_11_completo_son_los_tres_del_corte_y_no_los_seis(self):
        from src import tablero
        filas = self._filas(grove_high_output={"estado": "INSERTADO",
                                               "dueno": "NINGUNO"},
                            gerber_emyth={"estado": "INSERTADO"},
                            marquet_turn_the_ship={"estado": "INSERTADO"})
        completo, del_mundo, _ = tablero.mundo_11_completo(filas)
        self.assertTrue(completo, "los del corte no cuentan para el mundo 11")
        self.assertEqual(len(del_mundo), 3)

    # --------------------------------------------- la guarda del arnes lo exige

    def test_caso_positivo_la_guarda_tumba_un_encargo_que_elige_otro_libro(self):
        from scripts import guarda_tablero
        filas = self._filas(
            scott_radical_candor={"estado": "INSERTADO", "dueno": "NINGUNO"},
            gerber_emyth={"estado": "COSECHADO"})
        impiden = guarda_tablero.comprobar(
            texto="LIBRO DE ESTA VUELTA: bernerslee_bananas",
            linea="serial", filas=filas)
        self.assertTrue(any("D.51" in m for m in impiden))
        self.assertTrue(any("gerber_emyth" in m for m in impiden))

    def test_caso_negativo_el_encargo_que_declara_el_que_toca_pasa(self):
        from scripts import guarda_tablero
        filas = self._filas(
            scott_radical_candor={"estado": "INSERTADO", "dueno": "NINGUNO"},
            gerber_emyth={"estado": "COSECHADO"})
        self.assertEqual(guarda_tablero.comprobar(
            texto="LIBRO DE ESTA VUELTA: gerber_emyth",
            linea="serial", filas=filas), [])

    # ----------------------------------------- lo declarado, contra el repo real

    def test_el_orden_del_repo_lleva_los_seis_libros_con_su_motivo(self):
        from src import tablero
        libros = tablero.declaraciones()["orden_de_prioridad"]["libros"]
        self.assertEqual(len(libros), 6)
        for clave, dato in libros.items():
            self.assertTrue(dato.get("motivo"), "%s sin motivo" % clave)

    def test_el_tablero_del_repo_publica_la_prioridad_de_los_seis(self):
        from src import tablero
        con_prioridad = [f for f in tablero.leer() if f.get("prioridad")]
        self.assertEqual(len(con_prioridad), 6)
        fuera = [f["clave"] for f in con_prioridad if f.get("fuera_de_campania")]
        self.assertEqual(len(fuera), 3)


class PruebaGuardaDelTablero(BaseForja):
    """EL ARNES COMPRUEBA AL ABRIR VUELTA, CONTRA EL TABLERO (D.49).

    Y NO ADIVINA: exige que el encargo DECLARE su libro. Buscar la clave suelta dentro
    del texto es la trampa que el tallado ya pago dos veces, porque un encargo nombra a
    los frentes en su seccion de *lo que no se toca* y una guarda que lee menciones
    **tumbaria la vuelta por decir que no los toca**.
    """

    def _filas(self):
        return [
            {"lote": 4, "clave": "scott_radical_candor", "rama": "",
             "estado": "CERRADO EN EXTRACCION", "dueno": "serial",
             "candidatos_en_bandeja": 75, "ultimo_capitulo": "cap_14"},
            {"lote": 5, "clave": "marquet_turn_the_ship",
             "rama": "extraccion-marquet_turn_the_ship", "estado": "PAUSADO",
             "dueno": "NINGUNO", "candidatos_en_bandeja": 9,
             "bandeja_medida_en": "otro arbol", "ultimo_capitulo": "cap_03"},
            {"lote": 7, "clave": "grove_high_output",
             "rama": "extraccion-grove_high_output", "estado": "EN CURSO",
             "dueno": "grove_high_output", "candidatos_en_bandeja": 23,
             "ultimo_capitulo": "cap_03"},
        ]

    def test_caso_positivo_un_encargo_que_declara_libro_de_otro_dueno_no_abre(self):
        from scripts import guarda_tablero
        impiden = guarda_tablero.comprobar(
            texto="LIBRO DE ESTA VUELTA: grove_high_output",
            linea="serial", filas=self._filas())
        # Se mira POR REGLA y no por cuenta: desde D.51 un mismo encargo puede caer
        # por dos motivos distintos (ese libro no es tuyo, y no es el que te toca), y
        # una prueba que cuenta impedimentos se rompe cada vez que nace una regla.
        self.assertTrue(any("D.49" in m and "grove_high_output" in m for m in impiden),
                        impiden)

    def test_caso_positivo_pausado_sin_cosechar_tampoco_abre(self):
        from scripts import guarda_tablero
        impiden = guarda_tablero.comprobar(
            texto="LIBRO DE ESTA VUELTA: marquet_turn_the_ship",
            linea="serial", filas=self._filas())
        self.assertTrue(any("RELEVARLO ENTERO" in m for m in impiden), impiden)

    def test_caso_negativo_el_libro_de_esta_linea_abre(self):
        from scripts import guarda_tablero
        self.assertEqual(guarda_tablero.comprobar(
            texto="LIBRO DE ESTA VUELTA: scott_radical_candor",
            linea="serial", filas=self._filas()), [])

    def test_mencionar_un_frente_no_tumba_la_vuelta(self):
        """El encargo dice que NO los toca, y eso no puede ser lo que lo tumbe."""
        from scripts import guarda_tablero
        texto = (chr(10).join([
            "LIBRO DE ESTA VUELTA: scott_radical_candor",
            "",
            "## LO QUE NO SE TOCA",
            "grove_high_output esta EN CURSO en su frente y marquet_turn_the_ship",
            "y gerber_emyth quedan PAUSADOS. Ninguno es asunto de esta linea."]))
        self.assertEqual(guarda_tablero.comprobar(
            texto=texto, linea="serial", filas=self._filas()), [])

    def test_la_declaracion_se_lee_con_la_decoracion_de_la_casa(self):
        from scripts import guarda_tablero
        for escrito in ("**LIBRO DE ESTA VUELTA:** `scott_radical_candor`",
                        "> LIBRO DE ESTA VUELTA: scott_radical_candor",
                        "libro de esta vuelta: scott_radical_candor"):
            self.assertEqual(guarda_tablero.libro_declarado(escrito),
                             "scott_radical_candor", escrito)

    def test_caso_positivo_un_encargo_que_no_declara_libro_no_abre(self):
        """Un silencio no es una declaracion: para eso existe NINGUNO."""
        from scripts import guarda_tablero
        impiden = guarda_tablero.comprobar(
            texto="una vuelta cualquiera, sin decir sobre que trabaja",
            linea="serial", filas=self._filas())
        self.assertEqual(len(impiden), 1)
        self.assertIn("NO DECLARA su libro", impiden[0])

    def test_caso_negativo_ninguno_es_una_declaracion_valida(self):
        from scripts import guarda_tablero
        self.assertEqual(guarda_tablero.comprobar(
            texto="LIBRO DE ESTA VUELTA: NINGUNO",
            linea="serial", filas=self._filas()), [])

    def test_el_encargo_vivo_del_repo_declara_su_libro(self):
        """Si esto cae, la proxima vuelta del principal se detiene antes de abrir."""
        from scripts import guarda_tablero
        self.assertIsNotNone(
            guarda_tablero.libro_declarado(),
            "docs/loop/PROMPT_SIGUIENTE.md sin 'LIBRO DE ESTA VUELTA:'")


class PruebaCreditoPorLinea(BaseForja):
    """LA RACHA ES DE SU LINEA (D.48, 17 sep 2026, decision del fundador).

    El 16 sep corrieron cuatro sesiones a la vez. Tres frentes nacieron de la rama
    serial, se llevaron su `ACTA_AUDITOR.md` entero, y **el arnes les entrego cuatro
    remedios de otra secuencia a cada uno**. El auditor del primero paro citando como
    suyas **tres tandas de un libro que no era el suyo**.
    """

    def _registro(self, nombre="frente_de_prueba"):
        return os.path.join(self.taller, "CREDITO_%s.jsonl" % nombre)

    # ---------------------------------------------- de que linea es este arbol

    def test_la_rama_de_insercion_es_la_linea_serial(self):
        """Y se comprueba ANTES que el prefijo: `extraccion-mundo-11` tambien empieza
        por `extraccion-`, y sin ese orden la serial seria un frente `mundo-11`."""
        from src import credito
        self.assertEqual(credito.linea_actual(rama=credito.RAMA_DE_INSERCION),
                         credito.LINEA_SERIAL)

    def test_una_rama_de_libro_es_su_libro(self):
        from src import credito
        self.assertEqual(
            credito.linea_actual(rama="extraccion-gerber_emyth"), "gerber_emyth")

    # ------------------------------------------------ nacer con la racha en cero

    def test_caso_positivo_registro_sin_tandas_es_linea_recien_nacida(self):
        """Un `nacimiento` escrito NO es una tanda: la linea no ha dictado todavia."""
        from src import credito
        sucesos = [{"tipo": "nacimiento", "linea": "x", "cita": "D.48"}]
        self.assertFalse(credito.nacida(sucesos=sucesos))

    def test_caso_positivo_sin_ningun_suceso_tampoco_ha_dictado_nada(self):
        from src import credito
        self.assertFalse(credito.nacida(sucesos=[]))

    def test_caso_negativo_una_tanda_escrita_ya_es_una_linea_con_historia(self):
        from src import credito
        sucesos = [{"tipo": "tanda", "linea": "x", "especie": "REPORTE",
                    "racha": "1 de 3", "cita": "ACTA 1"}]
        self.assertTrue(credito.nacida(sucesos=sucesos))

    # ------------------------------------------- la racha que cada especie declara

    def test_la_ultima_linea_de_la_especie_es_la_que_manda(self):
        from src import credito
        sucesos = [
            {"tipo": "tanda", "especie": "REPORTE", "racha": "2 de 3", "cita": "A"},
            {"tipo": "tanda", "especie": "REPORTE", "racha": "3 de 3", "cita": "B"},
        ]
        self.assertEqual(credito.estado(sucesos=sucesos)["REPORTE"]["cuenta"], 3)

    def test_caso_positivo_la_especie_en_su_tope_es_lo_que_para_el_bucle(self):
        from src import credito
        sucesos = [{"tipo": "tanda", "especie": "REPORTE", "racha": "3 de 3",
                    "cita": "ACTA 31"}]
        self.assertEqual([e for e, _ in credito.en_tope(sucesos=sucesos)], ["REPORTE"])

    def test_caso_negativo_por_debajo_del_tope_no_para(self):
        from src import credito
        sucesos = [{"tipo": "tanda", "especie": "REPORTE", "racha": "2 de 3",
                    "cita": "ACTA 30"}]
        self.assertEqual(credito.en_tope(sucesos=sucesos), [])

    def test_un_reinicio_del_fundador_pone_la_especie_a_cero(self):
        """5.4 sigue entera: la reinicia una decision escrita, y va con su cita."""
        from src import credito
        sucesos = [
            {"tipo": "tanda", "especie": "REPORTE", "racha": "3 de 3",
             "cita": "ACTA 31"},
            {"tipo": "reinicio", "especie": "REPORTE", "racha": "0 de 3",
             "cita": "docs/loop/paradas/2026-09-17-de-quien-es-la-racha-DECISION.md"},
        ]
        self.assertEqual(credito.estado(sucesos=sucesos)["REPORTE"]["cuenta"], 0)
        self.assertEqual(credito.en_tope(sucesos=sucesos), [])

    # ------------------------------------------------- el replay, que no se calla

    def test_caso_positivo_el_replay_caza_una_racha_que_no_suma(self):
        """Dos tandas con caida seguidas dan 2, y la que declare 1 se publica."""
        from src import credito
        sucesos = [
            {"tipo": "tanda", "especie": "REPORTE", "racha": "1 de 3", "cae": True,
             "cita": "ACTA 1", "_linea_del_fichero": 1},
            {"tipo": "tanda", "especie": "REPORTE", "racha": "1 de 3", "cae": True,
             "cita": "ACTA 2", "_linea_del_fichero": 2},
        ]
        discrepancias = credito.revisar(sucesos=sucesos)
        self.assertEqual(len(discrepancias), 1)
        self.assertEqual(discrepancias[0]["replay"], 2)
        self.assertEqual(discrepancias[0]["declarada"], 1)

    def test_caso_negativo_una_tanda_limpia_pone_el_contador_a_cero(self):
        """D.38.1: seguidas significa consecutivas."""
        from src import credito
        sucesos = [
            {"tipo": "tanda", "especie": "REPORTE", "racha": "1 de 3", "cae": True,
             "cita": "ACTA 1", "_linea_del_fichero": 1},
            {"tipo": "tanda", "especie": "REPORTE", "racha": "0 de 3", "cae": False,
             "cita": "ACTA 2", "_linea_del_fichero": 2},
            {"tipo": "tanda", "especie": "REPORTE", "racha": "1 de 3", "cae": True,
             "cita": "ACTA 3", "_linea_del_fichero": 3},
        ]
        self.assertEqual(credito.revisar(sucesos=sucesos), [])

    def test_el_replay_no_acusa_a_la_historia_migrada(self):
        """Sus reinicios viven en docs/loop/paradas/, no en el registro. Una guarda
        que acusa de lo que no puede saber es ruido que se aprende a ignorar."""
        from src import credito
        sucesos = [
            {"tipo": "tanda", "especie": "REPORTE", "racha": "1 de 3", "cae": True,
             "cita": "ACTA 1", "migrado": True, "_linea_del_fichero": 1},
            {"tipo": "tanda", "especie": "REPORTE", "racha": "1 de 3", "cae": True,
             "cita": "ACTA 2", "migrado": True, "_linea_del_fichero": 2},
        ]
        self.assertEqual(credito.revisar(sucesos=sucesos), [])

    # ------------------------------------------- lo que no se escribe sin su cita

    def test_una_racha_sin_cita_no_se_escribe(self):
        from src import credito
        with self.assertRaises(credito.CreditoMalEscrito):
            credito.anotar({"tipo": "tanda", "especie": "REPORTE", "racha": "1 de 3"},
                           ruta_registro=self._registro())

    def test_una_linea_ilegible_del_registro_no_se_salta_en_silencio(self):
        from src import credito
        comun.escribir_texto(self._registro(), "{esto no es json}" + chr(10))
        with self.assertRaises(credito.CreditoMalEscrito):
            credito.leer(ruta_registro=self._registro())

    def test_lo_escrito_se_vuelve_a_leer_igual(self):
        from src import credito
        credito.anotar({"tipo": "tanda", "especie": "CLASE", "racha": "1 de 2",
                        "cae": True, "cita": "ACTA 9", "vuelta": 9},
                       linea="frente_de_prueba", ruta_registro=self._registro())
        sucesos = credito.leer(ruta_registro=self._registro())
        self.assertEqual(len(sucesos), 1)
        self.assertEqual(sucesos[0]["especie"], "CLASE")
        self.assertEqual(sucesos[0]["linea"], "frente_de_prueba")


class PruebaHerenciaPorLinea(BaseForja):
    """LA HERENCIA DE D.40 ES LA DE SU LINEA (D.48).

    Esta es la caida entera: el arnes le entrego a cada frente `4 remedio(s)` del acta
    de la linea de la que salio, y el auditor de `grove` paro por una racha que su
    frente no habia corrido.
    """

    def setUp(self):
        BaseForja.setUp(self)
        self.acta = os.path.join(self.taller, "ACTA_AUDITOR.md")
        comun.escribir_texto(self.acta, chr(10).join([
            "# ACTA 31. VUELTA 32, la de la linea de la que sale el frente",
            "",
            "## 9.3. MIS REMEDIOS PARA EL SIGUIENTE",
            "",
            "| # | **REMEDIO** | como se comprueba |",
            "|---:|---|---|",
            "| **1** | **UNA COSA DE LA LINEA SERIAL** | mirandola |",
            "| **2** | **OTRA COSA DE LA LINEA SERIAL** | mirandola |",
            ""]))

    def _con_linea(self, nombre):
        anterior = os.environ.get("FORJA_LINEA")

        def devolver():
            if anterior is None:
                os.environ.pop("FORJA_LINEA", None)
            else:
                os.environ["FORJA_LINEA"] = anterior

        os.environ["FORJA_LINEA"] = nombre
        self.addCleanup(devolver)

    def test_caso_positivo_un_frente_recien_nacido_hereda_cero(self):
        """Con las dos filas de remedios delante, y por eso lo dice en voz alta."""
        from src import herencia
        self._con_linea("libro_que_nunca_dicto_nada")
        recibido = herencia.extraer(ruta_acta=self.acta)
        self.assertEqual(recibido["items"], [])
        self.assertTrue(any("RECIEN NACIDA" in a for a in recibido["avisos"]))

    def test_el_aviso_nombra_la_linea_y_su_registro(self):
        """Un arnes que entrega cero sin avisar es el defecto por la puerta de atras."""
        from src import herencia
        self._con_linea("libro_que_nunca_dicto_nada")
        aviso = " ".join(herencia.extraer(ruta_acta=self.acta)["avisos"])
        self.assertIn("libro_que_nunca_dicto_nada", aviso)
        self.assertIn("CREDITO_libro_que_nunca_dicto_nada.jsonl", aviso)

    def test_caso_negativo_la_linea_serial_sigue_heredando_lo_suyo(self):
        """La serial tiene 31 tandas escritas: para ella no cambia nada."""
        from src import credito, herencia
        self._con_linea(credito.LINEA_SERIAL)
        recibido = herencia.extraer(ruta_acta=self.acta)
        self.assertEqual(len(recibido["items"]), 2)
        self.assertFalse(any("RECIEN NACIDA" in a for a in recibido["avisos"]))

    def test_la_linea_serial_del_repo_tiene_su_registro_escrito(self):
        """Si esto cae, la serial se comporta como un frente recien nacido y deja de
        heredar sus propios remedios, que es peor que el defecto que D.48 arregla."""
        from src import credito
        self.assertTrue(credito.nacida(credito.LINEA_SERIAL),
                        "docs/loop/CREDITO_serial.jsonl sin tandas: la migracion de "
                        "D.48 no esta en el arbol")


class PruebaTestigoDeGuardas(BaseForja):
    """UNA CIFRA VALE EN EL INSTANTE DEL SELLO (D.38.3 ensanchada, 16 sep 2026).

    La apertura de la vuelta 29 publico `guardas en rojo: 2` **sostenido con la
    salida literal de su instrumento, que era VERDE cuando corrio**. Entre esa
    corrida y el sello pasaron **44 minutos** y cinco guiones largos entraron en el
    arbol. **Cierto al medirse, falso al publicarse**, y ninguna regla cubria eso.
    """

    def _testigo(self, **guardas):
        return {"fecha": "2026-09-16 10:41:02", "commit": "abc123",
                "huella_del_arbol": "def456",
                "guardas": dict((n, {"estado": e, "codigo": 0 if e == "VERDE" else 1,
                                     "salida": "la salida de %s" % n})
                                for n, e in guardas.items())}

    def test_caso_negativo_todo_verde_el_sello_se_acepta(self):
        from scripts import testigo_guardas
        testigo = self._testigo(gate="VERDE", guiones="VERDE", censo_rutas="VERDE")
        self.assertEqual(testigo_guardas.comprobar(testigo=testigo), [])

    def test_caso_positivo_una_guarda_en_rojo_al_sellar_no_acepta_el_sello(self):
        """Es la vuelta 29: `guiones` en rojo en el instante del sello."""
        from scripts import testigo_guardas
        testigo = self._testigo(gate="VERDE", guiones="ROJO", censo_rutas="VERDE")
        impiden = testigo_guardas.comprobar(testigo=testigo)
        self.assertEqual(len(impiden), 1)
        self.assertIn("guiones", impiden[0])
        self.assertIn("instante del sello", impiden[0])
        self.anotar("testigo", "guarda en rojo al sellar: el sello no se acepta")

    def test_sin_testigo_tampoco_se_acepta(self):
        """Un sello sin testigo es un sello sin nada detras."""
        from scripts import testigo_guardas
        impiden = testigo_guardas.comprobar(
            ruta_testigo=os.path.join(self.taller, "no_existe.json"))
        self.assertEqual(len(impiden), 1)
        self.assertIn("no hay testigo", impiden[0])

    def test_el_testigo_registra_el_instante_y_el_arbol(self):
        """Sin hora y sin huella, el testigo no prueba CUANDO fue cierto."""
        from scripts import testigo_guardas
        escrito = testigo_guardas.escribir(os.path.join(self.taller, "testigo.json"))
        for clave in ("fecha", "commit", "huella_del_arbol", "guardas"):
            self.assertIn(clave, escrito)
        self.assertTrue(escrito["guardas"])


def main():
    comun.salida_utf8()
    orden = [PruebaA, PruebaB, PruebaC, PruebaD, PruebaE, PruebaF,
             PruebaGate, PruebaMutuo, PruebaCitaDeLinea, PruebaVigencia,
             PruebaNoAplica, PruebaDeprecado, PruebaResolutor,
             PruebaBandejas, PruebaReglasDeId, PruebaAristaDeclarada,
             PruebaArchivoDeInsertados,
             PruebaAristaDeclarada37,
             PruebaSedeVacia,
             PruebaHerencia,
             PruebaPoblacionDelInforme,
             PruebaTallado,
             PruebaCensoDeRutas,
             PruebaAduanaMideBandejas,
             PruebaCorreccionDeclarada,
             PruebaInsercionAtomica,
             PruebaAnotacionDeclarada,
             PruebaVigenciaNoEsGuarda,
             PruebaCerrojoYCenso,
             PruebaTestigoDeGuardas, PruebaCreditoPorLinea,
             PruebaHerenciaPorLinea, PruebaTableroDeFrentes,
             PruebaGuardaDelTablero, PruebaOrdenDePrioridad]
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
    print("  adjudicaciones del auditor (A.1 MUTUO, A.2 fuentes con fecha): %d pruebas mas"
          % len(cargador.loadTestsFromTestCase(PruebaMutuo)._tests))
    print("  TANDA A de la v0.3 (C.1 cita de linea, C.2 registro de citas, C.3 vigencia, "
          "C.4 no aplica, D.17 deprecado): %d pruebas mas"
          % sum(len(cargador.loadTestsFromTestCase(c)._tests)
                for c in (PruebaCitaDeLinea, PruebaVigencia, PruebaNoAplica, PruebaDeprecado)))
    print("  el barrido NO entra en las bandejas de entrada (estreno del 9 sep 2026): "
          "%d pruebas mas" % len(cargador.loadTestsFromTestCase(PruebaBandejas)._tests))
    print("  reglas de id 1 y 2, reescritas por el fundador (10 sep 2026): "
          "%d pruebas mas" % len(cargador.loadTestsFromTestCase(PruebaReglasDeId)._tests))
    print("  D.29, la arista que la señal no levanta se declara por lectura: "
          "%d pruebas mas" % len(cargador.loadTestsFromTestCase(PruebaAristaDeclarada)._tests))
    print("  D.31, el candidato insertado se archiva y el informe no lo cuenta: "
          "%d pruebas mas" % len(cargador.loadTestsFromTestCase(PruebaArchivoDeInsertados)._tests))
    print("  D.37, la serie declarada por el titulo es arista por lectura: "
          "%d pruebas mas" % len(cargador.loadTestsFromTestCase(PruebaAristaDeclarada37)._tests))
    print("  la sede de los pares mutuos nace vacia con su cabecera (5.7): "
          "%d pruebas mas" % len(cargador.loadTestsFromTestCase(PruebaSedeVacia)._tests))
    print("  D.40, lo que un auditor le deja al siguiente lo entrega el arnes: "
          "%d pruebas mas" % len(cargador.loadTestsFromTestCase(PruebaHerencia)._tests))
    print("  la poblacion del informe es grafo mas bandejas (12 sep 2026, punto 3): "
          "%d pruebas mas"
          % len(cargador.loadTestsFromTestCase(PruebaPoblacionDelInforme)._tests))
    print("  D.41, la tabla que dice ser de instrumento es la del instrumento: "
          "%d pruebas mas" % len(cargador.loadTestsFromTestCase(PruebaTallado)._tests))
    print("  D.42, la unidad de la ruta es la celda: %d pruebas mas"
          % len(cargador.loadTestsFromTestCase(PruebaCensoDeRutas)._tests))
    print("  D.38.5 en la aduana, que es donde se decide: %d pruebas mas"
          % len(cargador.loadTestsFromTestCase(PruebaAduanaMideBandejas)._tests))
    print("  D.29 en la aduana: la insercion es atomica y la arista espera en cola: "
          "%d pruebas mas" % len(cargador.loadTestsFromTestCase(PruebaInsercionAtomica)._tests))
    print("  la linea ya escrita de la bitacora se marca por operacion, sin borrar: "
          "%d pruebas mas" % len(cargador.loadTestsFromTestCase(PruebaAnotacionDeclarada)._tests))
    print("  D.15: la vigencia es COLA DE TRABAJO y no guarda que tumbe el cierre: "
          "%d pruebas mas" % len(cargador.loadTestsFromTestCase(PruebaVigenciaNoEsGuarda)._tests))
    print("  el cerrojo de insercion y D.44, el censo no decrece: %d pruebas mas"
          % len(cargador.loadTestsFromTestCase(PruebaCerrojoYCenso)._tests))
    print("  el testigo de guardas al sellar (D.38.3, 16 sep): %d pruebas mas"
          % len(cargador.loadTestsFromTestCase(PruebaTestigoDeGuardas)._tests))
    print("  D.48, la racha es de su linea, y el credito vive por linea: %d pruebas mas"
          % len(cargador.loadTestsFromTestCase(PruebaCreditoPorLinea)._tests))
    print("  D.48, la herencia de D.40 es la de SU linea: %d pruebas mas"
          % len(cargador.loadTestsFromTestCase(PruebaHerenciaPorLinea)._tests))
    print("  D.49 y D.50, un libro un dueño a la vez y el relevo: %d pruebas mas"
          % len(cargador.loadTestsFromTestCase(PruebaTableroDeFrentes)._tests))
    print("  D.49, la guarda del tablero al abrir vuelta: %d pruebas mas"
          % len(cargador.loadTestsFromTestCase(PruebaGuardaDelTablero)._tests))
    print("  D.51, el orden lo da el tablero, y el corte del mundo 11: %d pruebas mas"
          % len(cargador.loadTestsFromTestCase(PruebaOrdenDePrioridad)._tests))
    print("")
    print("  total: %d pruebas, %d fallos, %d errores"
          % (resultado.testsRun, len(resultado.failures), len(resultado.errors)))
    print("=" * 72)
    return 0 if resultado.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
