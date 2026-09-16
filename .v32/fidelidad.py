# -*- coding: utf-8 -*-
"""LA RELECTURA DE FIDELIDAD `D.30` DE LOS TRES QUE CIERRAN cap_11, CON SU CITA PEGADA.

`D.35`: ninguna cita de linea se teclea en una tabla sin que la salida literal del
libro quede pegada al lado. Aqui **el trozo del libro lo saca la maquina** del
propio `cap_11.md`; lo que pongo yo leyendo es **la linea que sostiene cada paso y
el veredicto TRANSCRIPCION o PUENTE**, que es el numerador que `D.30` dice que
ninguna guarda puede poner.

El instrumento **comprueba que el ancla existe en esa linea** y revienta si no,
asi que una linea mal apuntada no puede salir publicada como buena.
"""
import io
import json
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

LIBRO = "fuentes/scott_radical_candor/cap_11.md"
BANDEJA = "cuarentena/scott_radical_candor/%s.json"
LINEAS = io.open(LIBRO, encoding="utf-8").read().split("\n")

MAPA = [(chr(0x2014), "-"), (chr(0x2013), "-"), (chr(0x2019), "'"), (chr(0x2018), "'"),
        (chr(0x201c), '"'), (chr(0x201d), '"'), (chr(0x2026), "..."), (chr(0xa0), " ")]


def limpia(texto):
    for viejo, nuevo in MAPA:
        texto = texto.replace(viejo, nuevo)
    return texto.replace("|", "/")


def cita(numero, ancla, largo=110):
    texto = limpia(LINEAS[numero - 1])
    donde = texto.find(ancla)
    if donde < 0:
        raise SystemExit("EL ANCLA NO ESTA EN LA LINEA %d: %r" % (numero, ancla))
    antes = "..." if donde > 0 else ""
    trozo = texto[donde:donde + largo]
    despues = "..." if donde + largo < len(texto) else ""
    return "%d: %s%s%s" % (numero, antes, trozo, despues)


# LO QUE PONGO YO LEYENDO: (paso, linea del libro, ancla, veredicto, nota)
TRANSCRIPCION = "**TRANSCRIPCION**"

TANDA = [
    ("montar_tablero_kanban_medir_actividades", [
        (1, 239, "you put up a board with three columns", TRANSCRIPCION, ""),
        (2, 239, "Then you buy a bunch of Post-its", TRANSCRIPCION, ""),
        (3, 239, "They write their tasks on their color", TRANSCRIPCION, ""),
        (4, 239, "You can quickly see who's the bottleneck", TRANSCRIPCION, ""),
        (5, 239, "A Kanban board is different from a dashboard", TRANSCRIPCION, ""),
        (6, 241, "Making progress visible to everyone", TRANSCRIPCION, ""),
        (7, 243, "Another reason why measuring activities", TRANSCRIPCION, ""),
        (8, 245, "Measuring activities and visualizing workflows will push", TRANSCRIPCION,
         "y se para en la primera frase: **lo que sigue en `L245` es el caso de AdSense**, "
         "y un caso no es la casa (manual 3.5)"),
        (9, 247, "Measuring activities will also create more respect", TRANSCRIPCION, ""),
        (10, 249, "Measuring activities and displaying them publicly", TRANSCRIPCION,
         "**el que mire dos veces.** La frase de cabecera de `L249` es general; el *porque* "
         "del paso lo saca de la ultima frase del parrafo, que esta dicha sobre el equipo de "
         "Rivkin. **No lleva ni una cifra del caso** (ni el quince, ni el cuatro, ni el uno, "
         "ni los anios), asi que no es la senial barata de `3.5`"),
    ]),
    ("pasear_organizacion_hallar_problemas_pequenios", [
        (1, 255, "LISTENING TO THE people who report directly", TRANSCRIPCION, ""),
        (2, 259, "Schedule an hour a week of walking-around time", TRANSCRIPCION,
         "**el periodo lo escribe el libro**, asi que no es la especie *el periodo* de `D.30`"),
        (3, 259, "Management by walking around is a tried-and-true", TRANSCRIPCION, ""),
        (4, 261, "Notice the things you don't notice", TRANSCRIPCION, ""),
        (5, 261, "Ask people who catch your attention", TRANSCRIPCION, ""),
        (6, 261, "Find some small problems and treat them", TRANSCRIPCION, ""),
        (7, 263, "First they'll help you find the devil in the details", TRANSCRIPCION, ""),
        (8, 265, "Second, being aware of small problems", TRANSCRIPCION, ""),
        (9, 267, "Third, when you show that you care", TRANSCRIPCION, ""),
    ]),
    ("debatir_decidir_asuntos_cultura_evitar_delegar", [
        (1, 303, "There are a number of debates and decisions", TRANSCRIPCION, ""),
        (2, 303, "Are you going to call it a \"holiday party\"", TRANSCRIPCION,
         "**es el inventario propio del libro** (`D.27`), nombrado uno a uno: fiesta, arbol, "
         "candelabro, alcohol, la ropa interior sobre la mesa y la patada"),
        (3, 303, "Who's going to decide how to deal with it?", TRANSCRIPCION, ""),
        (4, 305, "But if you do, the decisions that do get made by HR", TRANSCRIPCION, ""),
        (5, 305, "If nobody makes a decision", TRANSCRIPCION, ""),
        (6, 305, "Neither is the culture you want", TRANSCRIPCION, ""),
    ]),
]

print("LA RELECTURA DE FIDELIDAD D.30 DE LOS TRES QUE CIERRAN cap_11")
print("AVISO: el trozo del libro lo saca la maquina de %s y" % LIBRO)
print("       revienta si el ancla no esta en esa linea. LA LINEA Y EL VEREDICTO LOS PONGO")
print("       YO LEYENDO: es el numerador que D.30 dice que ninguna guarda puede poner.")
print()

total_pasos = 0
total_puentes = 0
for identificador, filas in TANDA:
    datos = json.load(io.open(BANDEJA % identificador, encoding="utf-8"))
    escritos = len(datos["pasos_accionables"])
    if escritos != len(filas):
        raise SystemExit("%s tiene %d pasos y la relectura cubre %d"
                         % (identificador, escritos, len(filas)))
    total_pasos += escritos
    total_puentes += sum(1 for f in filas if "PUENTE" in f[3])
    print("### `%s`, %d pasos, todos releidos" % (identificador, escritos))
    print()
    print("| paso de `%s` | la salida del libro, pegada por `.v32/fidelidad.py` | veredicto |"
          % identificador)
    print("|---:|---|---|")
    for numero, linea, ancla, veredicto, nota in filas:
        cuerpo = veredicto + (", " + nota if nota else "")
        print("| `%d` | `%s` | %s |" % (numero, cita(linea, ancla), cuerpo))
    print()

print("| | |")
print("|---|---:|")
print("| nodos releidos | **%d** |" % len(TANDA))
print("| pasos escritos | **%d** |" % total_pasos)
print("| pasos releidos contra su parrafo | **%d** |" % sum(len(f) for _i, f in TANDA))
print("| **PUENTE** | **%d** |" % total_puentes)
