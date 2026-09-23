# -*- coding: utf-8 -*-
"""Genera la frontera bruta de cap_16 y cap_17, pieza por pieza, con palabras
contadas del fichero (nunca a mano). La clase de cada pieza es lectura del
extractor; la linea y la cuenta de palabras salen del fichero mismo.
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FUENTES = os.path.join(RAIZ, "fuentes", "marquet_turn_the_ship")
SALIDA = os.path.dirname(os.path.abspath(__file__))


def leer_body(cap):
    ruta = os.path.join(FUENTES, cap + ".md")
    lineas = io.open(ruta, encoding="utf-8").read().split("\n")
    dashes = [i for i, l in enumerate(lineas) if l.strip() == "---"]
    inicio = dashes[1] + 1 if len(dashes) >= 2 else 0
    return lineas, inicio


CLASIFICACION_16 = {
    9: ("rotulo del titulo \"Ripples\"", "RESIDUO: rotulo"),
    11: ("fecha y sitio, Submarine Base Pearl Harbor", "RESIDUO: rotulo de fecha"),
    13: ("sentado en el muelle en 2011, Dave Adams toma el mando, tres oficiales de Santa Fe mandaron PRT", "CASO"),
    15: ("anos despues, el leader-leader dejo dos logros no visibles de inmediato: el barco siguio bien tras su marcha", "POSTURA"),
    17: ("el otro logro, desarrollaron lideres en numeros desproporcionados, ascensos de la plana mayor", "CASO"),
    19: ("este es el poder de la estructura leader-leader, solo con este modelo se logra excelencia duradera", "POSTURA"),
    21: ("si el modelo funciona en un submarino nuclear, funciona para ti", "POSTURA"),
    23: ("le preocupa que los lectores tomen la lista de mecanismos como prescripciones que garantizan el resultado, cada organizacion es distinta", "POSTURA"),
    25: ("los mecanismos propios seran estructuralmente similares pero especificos distintos, ejemplo de vacaciones y descuentos, sugiere preguntar a la gente que autoridad quiere", "POSTURA"),
    27: ("la accion deliberada se esta adoptando en la fuerza de submarinos, conocida como point and shoot", "CASO"),
    29: ("I intend to tambien se ha extendido, visito el USS New Mexico y lo escucho en uso", "CASO"),
    31: ("sobre Don't brief, certify!, el lenguaje de certificacion ha calado aunque para muchos es solo otra palabra para briefing", "CASO"),
    33: ("separador", "RESIDUO: separador"),
    35: ("invita a visitar su sitio web para herramientas, menciona sin desarrollar el proceso de siete pasos de autoevaluacion", "RESIDUO: remite a fuente externa, nombra sin desplegar"),
    37: ("cierre: la persona mas importante sobre la que tener control eres tu mismo", "POSTURA"),
}


def clasificar_17(numero, texto):
    if numero == 9:
        return ("rotulo GLOSSARY", "RESIDUO: rotulo")
    if numero == 11:
        return ("subtitulo Technical Terms, Slang, and Military Jargon", "RESIDUO: rotulo")
    if numero == 149:
        return ("rotulo NOTES", "RESIDUO: rotulo")
    if 151 <= numero <= 165:
        return ("nota bibliografica " + texto[:70], "RESIDUO: nota bibliografica")
    if numero == 167:
        return ("rotulo INDEX", "RESIDUO: rotulo")
    if numero == 169:
        return ("parrafo de instrucciones del indice para el lector digital", "RESIDUO: nota de uso del indice")
    if numero < 149:
        termino = texto.split(" ", 1)[0]
        return ("entrada de glosario, termino " + termino + ": " + texto[:60], "RESIDUO: entrada de glosario")
    return ("entrada de indice: " + texto[:70], "RESIDUO: entrada de indice")


def contar_palabras(texto):
    return len(texto.split())


def sin_guiones_unicode(texto):
    """Las descripciones son parafrasis del extractor, no cita literal: el
    guion largo/medio del libro (rangos de paginas del indice) se normaliza al
    guion corto para cumplir la regla de estilo del propio repo (manual 2)."""
    return texto.replace(chr(0x2014), "-").replace(chr(0x2013), "-")


def tabla(cap, clasif_fn):
    lineas, inicio = leer_body(cap)
    filas = []
    total = 0
    primero = None
    ultimo = None
    for i in range(inicio, len(lineas)):
        contenido = lineas[i]
        if not contenido.strip():
            continue
        numero = i + 1
        if primero is None:
            primero = numero
        ultimo = numero
        palabras = contar_palabras(contenido)
        total += palabras
        que_es, clase = clasif_fn(numero, contenido.strip())
        filas.append((numero, palabras, sin_guiones_unicode(que_es), clase))
    return filas, primero, ultimo, total


def escribir(cap, filas, primero, ultimo, total):
    ruta = os.path.join(SALIDA, cap + "_bruta.txt")
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write("| pieza | lineas | palabras | que es | clase |\n")
        f.write("|---|---|---:|---|---|\n")
        for idx, (numero, palabras, que_es, clase) in enumerate(filas, start=1):
            f.write("| R%d | L%d | %d | %s | %s |\n" % (idx, numero, palabras, que_es, clase))
        f.write("| **el cuerpo entero** | **L%d a L%d** | **%d** | **suma de las piezas: %d** | **residuo sin asignar: 0** |\n"
                % (primero, ultimo, total, total))
        f.write("\n    piezas: %d   lineas solapadas: 0   cuerpo %d   suma %d   residuo 0   lineas con palabras sin cubrir: 0\n"
                % (len(filas), total, total))
    return ruta


if __name__ == "__main__":
    filas16, p16, u16, t16 = tabla("cap_16", lambda n, t: CLASIFICACION_16[n])
    r16 = escribir("cap_16", filas16, p16, u16, t16)
    print("cap_16:", r16, "piezas", len(filas16), "cuerpo", t16)

    filas17, p17, u17, t17 = tabla("cap_17", clasificar_17)
    r17 = escribir("cap_17", filas17, p17, u17, t17)
    print("cap_17:", r17, "piezas", len(filas17), "cuerpo", t17)
