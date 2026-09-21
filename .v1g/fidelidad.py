# -*- coding: utf-8 -*-
"""LA RELECTURA DE FIDELIDAD `D.30` DE LOS OCHO CANDIDATOS DE LA VUELTA 1, CON SU CITA PEGADA.

`D.35`: ninguna cita de linea se teclea sin que la salida literal del libro quede pegada al
lado. Aqui **el trozo del libro lo saca la maquina** del propio fichero de la unidad; lo que
pongo yo leyendo es **la linea que sostiene cada paso y el veredicto TRANSCRIPCION o PUENTE**,
que es el numerador que `D.30` dice que ninguna guarda puede poner.

El instrumento **comprueba que el ancla existe en esa linea y revienta si no**, asi que una
linea mal apuntada no puede salir publicada como buena. Y **comprueba que cada paso escrito del
candidato tiene al menos una fila**, asi que un paso sin releer tampoco puede colarse.
"""
import io
import json
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

BANDEJA = "cuarentena/grove_high_output/%s.json"
MAPA = [(chr(0x2014), "-"), (chr(0x2013), "-"), (chr(0x2019), "'"), (chr(0x2018), "'"),
        (chr(0x201c), '"'), (chr(0x201d), '"'), (chr(0x2026), "..."), (chr(0xa0), " ")]
LIBROS = {}


def limpia(texto):
    for viejo, nuevo in MAPA:
        texto = texto.replace(viejo, nuevo)
    return texto.replace("|", "/")


def lineas_de(unidad):
    if unidad not in LIBROS:
        LIBROS[unidad] = io.open("fuentes/grove_high_output/%s.md" % unidad,
                                 encoding="utf-8").read().split("\n")
    return LIBROS[unidad]


def cita(unidad, numero, ancla, largo=104):
    texto = limpia(lineas_de(unidad)[numero - 1])
    donde = texto.find(ancla)
    if donde < 0:
        raise SystemExit("EL ANCLA NO ESTA EN %s L%d: %r" % (unidad, numero, ancla))
    antes = "..." if donde > 0 else ""
    trozo = texto[donde:donde + largo]
    despues = "..." if donde + largo < len(texto) else ""
    return "%d: %s%s%s" % (numero, antes, trozo, despues)


T = "**TRANSCRIPCION**"

# LO QUE PONGO YO LEYENDO: (etiqueta de paso, linea, ancla, veredicto, nota)
TANDA = [
    ("revisar_tres_preguntas_valor_carrera", "cap_01", [
        ("1", 103, "Are you adding real value or merely passing information along", T, ""),
        ("2", 103, "By continually looking for ways to make things truly better in your department", T, ""),
        ("3", 103, "every hour of your day should be spent increasing the output", T, ""),
        ("4", 105, "Are you plugged into what's happening around you", T, ""),
        ("5", 105, "Or do you wait for a supervisor or others to interpret whatever is happening", T, ""),
        ("6", 107, "Are you trying new ideas, new techniques, and new technologies", T, ""),
        ("7", 107, "Or are you waiting for others to figure out how they can re-engineer your workplace", T, ""),
    ]),
    ("construir_flujo_produccion_paso_limitante", "cap_02", [
        ("1", 19, "These are to build and deliver products in response to the demands of the customer", T, ""),
        ("2", 19, "Production's charter cannot be to deliver whatever the customer wants whenever he wants it", T, ""),
        ("3", 21, "a manufacturer should accept the responsibility of delivering a product at the time committed to", T, ""),
        ("4", 21, "We start by looking at our production flow", T, ""),
        ("5", 23, "The first thing we must do is to pin down the step in the flow", T, ""),
        ("6a", 23, "we should plan the entire job around the time needed to boil it", T, ""),
        ("6b", 23, "the egg is also for most customers the most important feature of the breakfast", T, "**el que mire dos veces.** El paso 6 decia antes mira si ademas es el componente mas importante, y eso era un acto que el libro no encarga: hoy transcribe la afirmacion. Es la correccion de fidelidad de esta vuelta"),
        ("7", 25, "To work back from the time of delivery", T, ""),
        ("8", 25, "defines the length of the entire process", T, ""),
        ("9", 27, "Using the egg time as your base", T, ""),
        ("10", 27, "starting with the longest (or most difficult, or most sensitive, or most expensive) step", T, ""),
    ]),
    ("clasificar_trabajo_proceso_montaje_prueba", "cap_02", [
        ("1a", 39, "process manufacturing, an activity that physically or chemically changes material", T, ""),
        ("1b", 41, "is a process step, which transforms data into strategies", T, "la segunda mitad del paso, del caso de la fuerza de ventas"),
        ("2a", 39, "assembly, in which components are put together to constitute a new entity", T, ""),
        ("2b", 41, "are made to flow into one presentation", T, "la segunda mitad del paso"),
        ("3a", 39, "test, which subjects the components or the total to an examination of its characteristics", T, ""),
        ("3b", 39, "visual tests made at points in the breakfast production process", T, "las pruebas visuales, que el libro cuenta como prueba"),
        ("4a", 45, "Each piece then undergoes an individual operation called a", T, ""),
        ("4b", 41, "presentation with a selected group of field sales personnel", T, "la forma que la prueba toma en un trabajo de personas"),
        ("5a", 45, "the defective portion of the software is returned to the process phase for", T, ""),
        ("5b", 41, "to meet the concerns and objections of the test audience", T, "contra que se rehace"),
        ("6", 45, "After all the pieces pass their respective unit tests, they are assembled to form the compiler", T, ""),
        ("7", 45, "is performed on the complete product before it is shipped to the customer", T, ""),
    ]),
    ("rehacer_flujo_paso_limitante_capacidad", "cap_02", [
        ("1", 51, "our breakfast operation assumed infinite capacity", T, ""),
        ("2", 51, "What would happen if you had to stand in a line of waiters, waiting for your turn to use the toaster", T, ""),
        ("3", 51, "your three-minute egg could easily become a six-minute egg", T, ""),
        ("4a", 51, "you have to redo your flow around the new limiting step", T, ""),
        ("4b", 53, "Working back from the time of breakfast delivery", T, ""),
        ("4c", 53, "Toaster capacity has become the limiting step", T, "y el pie de la figura de L55 lo repite"),
        ("5a", 53, "The egg cycle remains the same, as does the one for coffee", T, ""),
        ("5b", 51, "but your time offsets must be altered", T, ""),
        ("6", 51, "The egg still determines the overall quality of the breakfast", T, ""),
    ]),
    ("equilibrar_capacidad_personal_inventario_plazo", "cap_02", [
        ("1", 57, "Your conflict is seemingly irreconcilable, but it really isn't", T, ""),
        ("2a", 57, "you could turn your personnel into specialists by hiring one egg-cooker", T, ""),
        ("2b", 57, "that, of course, creates an immense amount of overhead", T, "el coste de esa salida, escrito por el libro"),
        ("3a", 59, "you could ask the waiter in line next to you to help out", T, ""),
        ("3b", 59, "when you have to depend on someone else, the results are likely to be less predictable", T, "el coste de esa salida"),
        ("4", 59, "you could add another toaster, but this becomes an expensive addition of capital equipment", T, ""),
        ("5a", 59, "You could run the toaster continuously and build up an inventory of hot toast", T, ""),
        ("5b", 59, "That means waste, which can also become too expensive for the operation", T, "el coste de esa salida"),
        ("6", 59, "equipment capacity, manpower, and inventory can be traded off against each other", T, ""),
        ("7a", 61, "your task is to find the most cost-effective way to deploy your resources", T, ""),
        ("7b", 61, "the one that can give you the best delivery time and product quality at the lowest possible cost", T, "la vara de la respuesta correcta"),
        ("8a", 61, "you must reduce the understanding to a quantifiable set of relationships", T, ""),
        ("8b", 61, "What is important is the thinking you force yourself to go through", T, "el freno que el propio libro pone al calculo"),
    ]),
    ("preferir_inspeccion_proceso_prueba_destructiva", "cap_02", [
        ("1a", 67, "all the eggs in the boiler", T, ""),
        ("1b", 67, "to the time the malfunction was discovered becomes unusable", T, ""),
        ("2", 67, "All the toast is also wasted because you don't have any eggs to serve with it", T, ""),
        ("3a", 67, "Performing a functional test is one way", T, ""),
        ("3b", 67, "But you will have to throw away the egg tested", T, ""),
        ("4a", 67, "A second way involves in-process inspection, which can take many forms", T, ""),
        ("4b", 67, "insert a thermometer into the water so that the temperature could be easily and frequently checked", T, ""),
        ("5", 67, "connect an electronic gadget to it that would set off bells anytime the temperature varied by a degree or two", T, ""),
        ("6", 67, "whenever possible, you should choose in-process tests over those that destroy product", T, ""),
    ]),
    ("dimensionar_inventario_materia_prima_reposicion", "cap_02", [
        ("1", 69, "you will want to look at the eggs at the time of receipt, something called incoming or receiving inspection", T, ""),
        ("2", 69, "The eggs going into it could be cracked or rotten, or they could be over- or undersized", T, ""),
        ("3", 69, "you are going to have to send them back, leaving you with none. Now you have to shut down", T, ""),
        ("4", 69, "To avoid that, you need a raw material inventory", T, ""),
        ("5a", 69, "you should have enough to cover your consumption rate for the length of time it takes to replace your raw material", T, ""),
        ("5b", 69, "if your egg man comes by and delivers once a day, you want to keep a day's worth of inventory on hand", T, "el ejemplo del propio libro, que es lo unico que fija un numero"),
        ("6", 69, "you have to weigh the advantage of carrying a day's supply against the cost of carrying it", T, ""),
        ("7a", 69, "you should also try to gauge the opportunity at risk", T, ""),
        ("7b", 69, "How many customers would you lose? How much would it cost to lure them back?", T, "las otras dos preguntas de las tres"),
    ]),
    ("detectar_arreglar_fallo_etapa_menor_valor", "cap_02", [
        ("1a", 73, "the material becomes more valuable as it moves through the process", T, ""),
        ("1b", 73, "A boiled egg is more valuable than a raw one", T, ""),
        ("2", 73, "The last carries the perceived value the customer associates with the establishment", T, "**el que mire dos veces.** El libro AFIRMA que la ultima etapa lleva ese valor percibido; el paso manda contarlo dentro del orden por valor del paso 1, que es el uso que el propio tramo le da"),
        ("3", 75, "A common rule we should always try to heed is to detect and fix any problem in a production process at the lowest-value stage possible", T, ""),
        ("4", 75, "we should find and reject the rotten egg as it's being delivered from our supplier", T, ""),
        ("5", 75, "if we can decide that we don't want a college candidate at the time of the campus interview", T, ""),
        ("6", 75, "we should also try to find any performance problem at the time of the unit test", T, ""),
    ]),
]

print("LA RELECTURA DE FIDELIDAD D.30 DE LOS OCHO CANDIDATOS DE LA VUELTA 1 DEL FRENTE")
print("AVISO: el trozo del libro lo saca la maquina de fuentes/grove_high_output/<unidad>.md y")
print("       revienta si el ancla no esta en esa linea. LA LINEA Y EL VEREDICTO LOS PONGO YO")
print("       LEYENDO: es el numerador que D.30 dice que ninguna guarda puede poner.")
print("")

total_pasos = total_filas = total_puentes = 0
for identificador, unidad, filas in TANDA:
    datos = json.load(io.open(BANDEJA % identificador, encoding="utf-8"))
    pasos = len(datos["pasos_accionables"])
    vistos = set(e.rstrip("abc") for e, _l, _a, _v, _n in filas)
    faltan = [str(n) for n in range(1, pasos + 1) if str(n) not in vistos]
    if faltan:
        raise SystemExit("PASOS SIN RELEER en %s: %s" % (identificador, faltan))
    total_pasos += pasos
    total_filas += len(filas)
    total_puentes += sum(1 for _e, _l, _a, v, _n in filas if v != T)
    print("### `%s`, %d pasos escritos, %d filas releidas, unidad `%s`"
          % (identificador, pasos, len(filas), unidad))
    print("")
    print("| paso de `%s` | la salida del libro, pegada por `.v1g/fidelidad.py` | veredicto |"
          % identificador)
    print("|---:|---|---|")
    for etiqueta, numero, ancla, veredicto, nota in filas:
        print("| `%s` | `%s` | %s%s |"
              % (etiqueta, cita(unidad, numero, ancla), veredicto,
                 (", " + nota) if nota else ""))
    print("")

print("=" * 78)
print("EL SALDO DE LA RELECTURA")
print("=" * 78)
print("candidatos releidos      : %d" % len(TANDA))
print("pasos escritos en total  : %d" % total_pasos)
print("filas de relectura       : %d" % total_filas)
print("PUENTE                   : %d" % total_puentes)
print("PASOS INVENTADOS         : %s por ciento"
      % ("%.2f" % (100.0 * total_puentes / total_pasos)).replace(".", ","))
