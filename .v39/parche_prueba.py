# -*- coding: utf-8 -*-
"""TAREA 1.A de la vuelta 39: las dos pruebas dejan de clavar el 6 y leen su sede."""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA = os.path.join(RAIZ, "tests", "test_aceptacion.py")

VIEJO = '''    def test_la_cola_del_repo_trae_las_seis_con_su_medida(self):
        from src import tablero
        cola = tablero.cola_de_doctrina()
        self.assertEqual(len(cola), 6)
        for fila in cola:
            self.assertTrue(fila["pregunta"], fila)
            self.assertTrue(fila["medida_en"], fila)

    def test_la_cola_esta_escrita_en_el_tablero_del_arbol(self):
        from src import tablero
        escritas = [f for f in tablero.leer() if f.get("tipo") == "doctrina"]
        self.assertEqual(len(escritas), 6)
'''

NUEVO = '''    def _preguntas_de_la_sede(self):
        """LA CUENTA SALE DE SU SEDE, NO DE UNA CONSTANTE.

        Hasta la vuelta 39 estas dos pruebas clavaban un `6`, y una tarea del propio
        bucle (encargo de la vuelta 38, tarea 4) mando subir la cola a `8`: la suite se
        puso en rojo POR OBEDECER. Lo que la regla exige es que la cola exista, que cada
        pregunta traiga su medida y su `bloquea`, y que lo que el tablero sirve sea lo
        que su sede tiene. **Cuantas hay lo dice `config/frentes.json`.**
        """
        from src import tablero
        return (tablero.comun.leer_json(tablero.RUTA_FRENTES)
                .get("cola_de_doctrina", {})
                .get("preguntas", []))

    def test_la_cola_del_repo_trae_las_de_su_sede_con_su_medida(self):
        from src import tablero
        cola = tablero.cola_de_doctrina()
        preguntas = self._preguntas_de_la_sede()
        self.assertTrue(preguntas, "config/frentes.json no trae cola de doctrina")
        self.assertEqual(len(cola), len(preguntas))
        self.assertEqual([f["n"] for f in cola], [p.get("n") for p in preguntas])
        for fila in cola:
            self.assertTrue(fila["pregunta"], fila)
            self.assertTrue(fila["medida_en"], fila)
            self.assertIsInstance(fila["bloquea"], bool, fila)

    def test_la_cola_esta_escrita_en_el_tablero_del_arbol(self):
        escritas = [f for f in __import__("src.tablero", fromlist=["tablero"]).leer()
                    if f.get("tipo") == "doctrina"]
        self.assertEqual(len(escritas), len(self._preguntas_de_la_sede()))
'''

with io.open(RUTA, encoding="utf-8") as f:
    texto = f.read()

if VIEJO not in texto:
    raise SystemExit("EL BLOQUE VIEJO NO ESTA: no toco nada.")
texto = texto.replace(VIEJO, NUEVO, 1)
with io.open(RUTA, "w", encoding="utf-8", newline="") as f:
    f.write(texto)
print("parche aplicado sobre tests/test_aceptacion.py")
