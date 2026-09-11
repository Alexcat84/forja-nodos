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
        dictamenes, cuantos, umbrales, fuera = informe.revisar(
            rutas, ruta_dataset=self.dataset,
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


def main():
    comun.salida_utf8()
    orden = [PruebaA, PruebaB, PruebaC, PruebaD, PruebaE, PruebaF,
             PruebaGate, PruebaMutuo, PruebaCitaDeLinea, PruebaVigencia,
             PruebaNoAplica, PruebaDeprecado, PruebaResolutor,
             PruebaBandejas, PruebaReglasDeId, PruebaAristaDeclarada,
             PruebaArchivoDeInsertados,
             PruebaAristaDeclarada37,
             PruebaSedeVacia]
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
    print("")
    print("  total: %d pruebas, %d fallos, %d errores"
          % (resultado.testsRun, len(resultado.failures), len(resultado.errors)))
    print("=" * 72)
    return 0 if resultado.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
