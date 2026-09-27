# -*- coding: utf-8 -*-
"""Las tres correcciones de la relectura D.30 de la vuelta 38, antes de insertar nada."""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def cargar(cid):
    ruta = os.path.join(RAIZ, "cuarentena", "scott_radical_candor", "%s.json" % cid)
    with io.open(ruta, encoding="utf-8") as f:
        return ruta, json.load(f)


def guardar(ruta, d):
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write(u"\n")


CAMBIOS = [
    ("practicar_triangulo_critica_tres_papeles", 10,
     u"grosería", u"groseria",
     u" CORRECCION DECLARADA 18 sep 2026, vuelta 38, relectura de fidelidad D.30 antes de insertar:"
     u" el paso 10 escribia groseria con tilde en la i, el unico caracter acentuado de los seis"
     u" candidatos de esta vuelta y uno de los dos unicos de todo dataset/nodos.jsonl, que tiene 318"
     u" nodos. Se corrige la grafia contra la de la casa. El paso NO cambia de contenido: cap_13 L65"
     u" escribe the feedback receiver gets mad and responds rudely, y eso es lo que el paso dice."),
    ("pedir_critica_primero_crear_seguridad_psicologica", 6,
     None,
     u"Empieza por el primero y no por otro, y el texto explica por que hace falta decirlo: de las dos"
     u" historias mas memorables y mas repetidas de la primera edicion, una era de una jefa dando"
     u" critica con acierto y la otra de lo que pasa cuando una jefa NO la da; al libro le faltaba una"
     u" historia igual de memorable de una jefa pidiendo critica a un empleado, y por eso muchos"
     u" lectores se quedaron con la impresion de que la franqueza radical va sobre todo de jefes"
     u" criticando a empleados, cuando nada podria estar mas lejos de la verdad.",
     u" CORRECCION DECLARADA 18 sep 2026, vuelta 38, relectura de fidelidad D.30 antes de insertar,"
     u" DOS defectos y los dos en pasos que nombran una persona o un escalon, que es justo la clase"
     u" que el encargo de esta vuelta manda releer entera. EL PRIMERO, paso 6: escribia que las dos"
     u" historias mas repetidas eran las de una jefa dando critica, y cap_13 L87 las contrasta"
     u" expresamente, One was about a boss giving feedback successfully, The other was about what"
     u" happens when a boss fails to give feedback, o sea que la segunda es de una jefa que NO la da."
     u" Y ademas invertia la causa: L89 no dice que la impresion viniera de que hubiera historias de"
     u" dar, dice que venia de que al libro le FALTABA una historia memorable de una jefa pidiendo,"
     u" Unfortunately, the book didn't have a similarly memorable story about a boss soliciting"
     u" feedback from an employee. As a result. El paso se reescribe contra L87 y L89 y su cita pasa"
     u" de la linea 89 sola a las lineas 87 y 89."),
    ("pedir_critica_primero_crear_seguridad_psicologica", 15,
     u"cuando quien manda pide critica",
     u"cuando el consejero delegado pide critica",
     u" EL SEGUNDO, paso 15: escribia quien manda donde cap_13 L109 escribe When the CEO solicits"
     u" criticism, y el escalon importa porque la frase entera va de que la senial baja del CEO a los"
     u" jefes intermedios. Quien manda aplana esa altura. Se escribe consejero delegado, que es la"
     u" grafia de esta casa, 36 apariciones en dataset/nodos.jsonl contra 1 de ceo. Se aniade ademas"
     u" de la organizacion, que L109 escribe, As people at all levels of the organization realize."),
]

for cid, npaso, viejo, nuevo, nota in CAMBIOS:
    ruta, d = cargar(cid)
    p = d["pasos_accionables"][npaso - 1]
    if viejo is None:
        assert p != nuevo, cid
        d["pasos_accionables"][npaso - 1] = nuevo
    else:
        assert viejo in p, (cid, npaso, p)
        d["pasos_accionables"][npaso - 1] = p.replace(viejo, nuevo)
    d["resumen_teorico"] = d["resumen_teorico"].rstrip() + nota
    guardar(ruta, d)
    print(u"%s paso %d: corregido" % (cid, npaso))

# el paso 15 pide ademas 'de todos los niveles de la organizacion'
ruta, d = cargar("pedir_critica_primero_crear_seguridad_psicologica")
p = d["pasos_accionables"][14]
assert u"gente de todos los niveles se da cuenta" in p
d["pasos_accionables"][14] = p.replace(
    u"gente de todos los niveles se da cuenta",
    u"gente de todos los niveles de la organizacion se da cuenta")
guardar(ruta, d)
print(u"pedir_critica_primero_crear_seguridad_psicologica paso 15: niveles de la organizacion")
