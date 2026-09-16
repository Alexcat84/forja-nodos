# -*- coding: utf-8 -*-
"""La prueba de la TAREA 2 en tests/test_aceptacion.py: una guarda que no muerde
es cifra (cosecha 7.C), asi que la que caza a la regla vieja va escrita.
"""
import io

RUTA = "tests/test_aceptacion.py"
s = io.open(RUTA, encoding="utf-8").read()

# ------------------------------------------------------------ 1. el fixture
viejo = '''    ACTA = """# ACTA 8. una vuelta vieja

### 7.3. MI REMEDIO DE LA VUELTA VIEJA
Esto no se hereda: no es la ultima acta.

# ACTA 9. la ultima

## 7. MIS CAIDAS

> ### **TAREA BLOQUEANTE DEL AUDITOR DE LA VUELTA 10, ESCRITA POR EL AUDITOR DE LA 9**
>
> Pega el instrumento al lado de cada cifra.

### 7.4. EL REMEDIO QUE SI CUMPLI
Su cuerpo, que tambien se hereda porque el encabezado nombra un remedio.

## 8. OTRA COSA
Esto ya no pertenece al remedio anterior.
"""
'''
nuevo = '''    # EL FIXTURE LLEVA LAS CUATRO TRAMPAS QUE EL ACTA REAL LLEVA, y es deliberado
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
'''
assert s.count(viejo) == 1
s = s.replace(viejo, nuevo)

# ------------------------------------------- 2. el caso positivo de la TAREA 2
viejo = '''    def test_sin_acta_no_revienta_y_la_linea_de_lectura_sigue_en_pie(self):'''
nuevo = '''    # ------------------------------------------------------------ 16 sep 2026
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

    def test_sin_acta_no_revienta_y_la_linea_de_lectura_sigue_en_pie(self):'''
assert s.count(viejo) == 1
s = s.replace(viejo, nuevo)

io.open(RUTA, "w", encoding="utf-8", newline="").write(s)
print("parche aplicado sobre " + RUTA)
