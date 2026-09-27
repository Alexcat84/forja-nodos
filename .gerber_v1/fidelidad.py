# -*- coding: utf-8 -*-
"""LA RELECTURA DE FIDELIDAD `D.30` DE LOS DIEZ CANDIDATOS DE ESTA VUELTA.

Es el instrumento de `.v32/fidelidad.py` con la unica diferencia de que lee VARIAS
unidades del libro en vez de una, porque esta vuelta mina cuatro. **La TAREA 3 del
encargo lo pide expresamente** (`PASOS INVENTADOS POR CAPITULO`, fila por unidad
mas total), que es lo que `EXTRACTOR.md` 13 llama una tarea del encargo que ordena
un instrumento.

`D.35`: **el trozo del libro lo saca la maquina** del propio fichero de la unidad.
Lo que pongo yo leyendo es **la linea que sostiene cada paso y el veredicto
TRANSCRIPCION o PUENTE**, que es el numerador que `D.30` dice que ninguna guarda
de esta casa puede poner.

El instrumento **comprueba que el ancla existe en esa linea** y revienta si no,
asi que una linea mal apuntada no puede salir publicada como buena. Tambien
revienta si el numero de filas releidas no es el numero de pasos escritos, para
que no se pueda firmar una relectura parcial como si fuera entera.
"""
import io
import json
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

BANDEJA = "cuarentena/gerber_emyth/%s.json"
LIBRO = "fuentes/gerber_emyth/%s.md"
CACHE = {}

MAPA = [(chr(0x2014), "-"), (chr(0x2013), "-"), (chr(0x2019), "'"), (chr(0x2018), "'"),
        (chr(0x201c), '"'), (chr(0x201d), '"'), (chr(0x2026), "..."), (chr(0xa0), " ")]


def limpia(texto):
    for viejo, nuevo in MAPA:
        texto = texto.replace(viejo, nuevo)
    return texto.replace("|", "/")


def lineas(unidad):
    if unidad not in CACHE:
        CACHE[unidad] = io.open(LIBRO % unidad, encoding="utf-8").read().split("\n")
    return CACHE[unidad]


def cita(unidad, numero, ancla, largo=105):
    texto = limpia(lineas(unidad)[numero - 1])
    donde = texto.find(ancla)
    if donde < 0:
        raise SystemExit("EL ANCLA NO ESTA EN %s L%d: %r" % (unidad, numero, ancla))
    antes = "..." if donde > 0 else ""
    trozo = texto[donde:donde + largo]
    despues = "..." if donde + largo < len(texto) else ""
    return "%d: %s%s%s" % (numero, antes, trozo, despues)


T = "**TRANSCRIPCION**"

# LO QUE PONGO YO LEYENDO: (unidad, id, [(paso, linea, ancla, veredicto, nota)])
TANDA = [
    ("cap_04", "hacer_trabajo_futuro_imaginar_negocio", [
        (1, 285, "An Entrepreneur does the work of envisioning the business as something apart from you", T, ""),
        (2, 285, "The work of asking all the right questions about why this business", T, ""),
        (3, 285, "you would leave your pie-baking experience behind you", T, ""),
        (4, 287, "It's time for me to create a new life", T, ""),
        (5, 287, "One that can give me everything that I want", T,
         "**mi discutible 1.** Los cuatro rasgos son FINES, y van aqui porque son el contenido "
         "del dialogo que el libro transcribe, no el criterio del nodo"),
        (6, 289, "The dreaming question, I call it", T, ""),
        (7, 291, "I call it Future Work", T, ""),
    ]),
    ("cap_07", "dictar_ritmo_crecimiento_preguntas_escritas", [
        (1, 279, "understanding the key processes that need to be performed", T, ""),
        (2, 279, "the key objectives that need to be achieved", T, ""),
        (3, 279, "the key position you are aiming your business to hold in the marketplace", T, ""),
        (4, 281, "By asking the right questions, such as: Where do I wish to be?", T,
         "**el inventario de preguntas es del libro**, transcrito entero y con sus tres marcas"),
        (5, 283, "you will also have contingency plans in place. Best case, worst case", T, ""),
        (6, 285, "the key is to plan, envision, and articulate what you see in the future", T, ""),
        (7, 285, "write it down, clearly, so others can understand it", T, ""),
        (8, 287, "any plan is better than no plan", T, ""),
    ]),
    ("cap_08", "construir_empresa_plantilla_vision_diaria", [
        (1, 39, "I had a very clear picture of what the company would look like when it was finally done", T,
         "**el fundador de IBM lo nombra `L37`**, que es la linea que abre la historia"),
        (2, 41, "I then asked myself how a company which looked like that would have to act", T, ""),
        (3, 43, "unless we began to act that way from the very beginning, we would never get there", T, ""),
        (4, 45, "it would have to act like a great company long before it ever became one", T, ""),
        (5, 47, "each and every day we attempted to model the company after that template", T, ""),
        (6, 47, "we asked ourselves how well we did, discovered the disparity", T, ""),
        (7, 47, "at the start of the following day, set out to make up for the difference", T, ""),
        (8, 49, "Every day at IBM was a day devoted to business development", T,
         "**y `L51` la remata**: we didn't do business at IBM, we built one"),
    ]),
    ("cap_08", "trazar_modelo_negocio_cliente_primero", [
        (1, 109, "a model of a business that fulfills the perceived needs of a specific segment", T, ""),
        (2, 115, "he surveys the world and asks", T, ""),
        (3, 115, "he then goes back to the drawing board", T, ""),
        (4, 115, "constructs a solution to the frustrations he finds among a certain group of customers", T, ""),
        (5, 115, "the way the customer needs it to look and act, not The Entrepreneur", T, ""),
        (6, 117, "How will my business look to the customer?", T, ""),
        (7, 117, "How will my business stand out from all the rest?", T, ""),
        (8, 119, "does not start with a picture of the business to be created but of the customer", T, ""),
        (9, 121, "without a clear picture of that customer, no business can succeed", T, ""),
    ]),
    ("cap_11", "fingir_prototipo_cinco_mil_replicas", [
        (1, 35, "Pretend that the business you own", T, "**y `L37`**: the model for 5,000 more just like it"),
        (2, 39, "Not almost like it, but just like it. Perfect replicates. Clones", T, ""),
        (3, 41, "pretend that you are going to franchise your business", T, ""),
        (4, 43, "there are rules to follow if you are to win", T,
         "**la cuenta es condicion de `D.37`**, y aqui el libro la escribe numerando del 1 al 6"),
        (5, 45, "The model will provide consistent value to your customers", T, ""),
        (6, 47, "The model will be operated by people with the lowest possible level of skill", T, ""),
        (7, 49, "The model will stand out as a place of impeccable order", T,
         "**se transcribe como regla de la cabeza**, y NO se le hace nodo propio: ver `R3` de la frontera"),
        (8, 51, "All work in the model will be documented in Operations Manuals", T, ""),
        (9, 53, "The model will provide a uniformly predictable service to the customer", T,
         "**igual que la 3**: se transcribe aqui y no tiene nodo propio, ver `R4` de la frontera"),
        (10, 55, "The model will utilize a uniform color, dress, and facilities code", T, ""),
        (11, 57, "Let's take a look at each of these rules in turn", T, ""),
    ]),
    ("cap_11", "dar_valor_constante_cuatro_publicos", [
        (1, 63, "value is what people perceive it to be, and nothing more", T, ""),
        (2, 65, "So what could your Prototype do that would not only provide consistent value", T, ""),
        (3, 71, "as it impacts every person with whom your business comes into contact", T, ""),
        (4, 73, "Value can be a word said at the door of the business", T, ""),
        (5, 75, "Value can be an unexpected gift from the business arriving in the mail", T, ""),
        (6, 77, "Value can be a word of recognition to a new recruit", T, ""),
        (7, 79, "Value can be the reasonable price of your products", T, ""),
        (8, 81, "Value can be a simple word of thanks to your banker", T, ""),
    ]),
    ("cap_11", "operar_modelo_gente_destreza_minima", [
        (1, 87, "if your model depends on highly skilled people, it's going to be impossible to replicate", T, ""),
        (2, 89, "I mean the lowest possible level necessary to fulfill the functions", T,
         "**el libro DEFINE su propio adjetivo de adecuacion**, y eso es lo que salva la regla de "
         "caer por la restriccion 2 de `EXTRACTOR.md` 9.1"),
        (3, 89, "if yours is a legal firm, you must have attorneys", T, ""),
        (4, 89, "You need to create the very best system through which good attorneys", T, ""),
        (5, 91, "How can I give my customer the results he wants systematically rather than personally?", T, ""),
        (6, 93, "How can I create an expert system rather than hire one?", T, ""),
        (7, 103, "the system becomes the tools your people use to increase their productivity", T, ""),
        (8, 105, "to develop those tools and to teach your people how to use them", T,
         "**el responsable lo pone el libro y no yo**, asi que no es puente de la especie responsable"),
        (9, 107, "It's your people's job to use the tools you've developed", T, ""),
        (10, 113, "prefers Management by Abdication to Management by Delegation", T,
         "**es comprobacion y no advertencia**: el libro nombra la conducta concreta que hay que mirar"),
    ]),
    ("cap_11", "documentar_trabajo_manual_operaciones", [
        (1, 155, "Documentation says", T, ""),
        (2, 157, "Without documentation, all routinized work turns into exceptions", T, ""),
        (3, 159, "Documentation provides your people with the structure they need", T, ""),
        (4, 159, "It communicates to the new employees, as well as to the old", T, ""),
        (5, 163, "The operative word here is clear", T, ""),
        (6, 167, "structure is reduced to specific means rather than generalized ends", T, ""),
        (7, 169, "best described as a company's How-to-Do-It Guide", T, ""),
        (8, 171, "It designates the purpose of the work", T, ""),
        (9, 171, "specifies the steps needed to be taken while doing that work", T, ""),
        (10, 171, "summarizes the standards associated with both the process and the result", T,
         "**los tres contenidos van en tres pasos** porque el libro los cuenta como tres"),
    ]),
    ("cap_11", "unificar_color_forma_vestuario_modelo", [
        (1, 215, "all consumers are moved to act by the colors and shapes they find in the marketplace", T, ""),
        (2, 229, "The colors you show your customer must be scientifically determined", T, ""),
        (3, 229, "on the walls, the floors, the ceiling, the vehicles, the invoices", T,
         "**los ocho sitios son del libro**, nombrados uno a uno: es la cara positiva de `D.27`"),
        (4, 231, "The model must be thought of as a package for your one and only product", T, ""),
        (5, 233, "there are shapes that work and shapes that don't, on your business card", T, ""),
        (6, 235, "Cheskin showed that a triangle produced far fewer sales than a circle", T,
         "**es la cifra que va a `atribuciones`**, y es cualitativa: el libro no da muestra ni banda"),
        (7, 239, "The shape of your sign, your logo, the type style used on your business cards", T, ""),
        (8, 241, "Your Prototype must be packaged as carefully as any box of cereal", T, ""),
    ]),
    ("cap_11", "interrogar_negocio_cinco_preguntas", [
        (1, 245, "Go to work on your business rather than in it", T, ""),
        (2, 247, "as if it were the pre-production prototype of a mass-produceable product", T, ""),
        (3, 249, "Think of your business as something apart from yourself", T, ""),
        (4, 251, "Think of your business as anything but a job", T, ""),
        (5, 255, "How can I get my business to work, but without me", T, ""),
        (6, 257, "How can I get my people to work, but without my constant interference", T, ""),
        (7, 259, "How can I systematize my business in such a way that it could be replicated 5,000 times", T,
         "**mi discutible 4 vive aqui**: esta pregunta repite la cifra de la cabeza, y aun asi el "
         "acto y el entregable son otros"),
        (8, 261, "How can I own my business, and still be free of it", T, ""),
        (9, 263, "How can I spend my time doing the work I love to do", T, ""),
        (10, 265, "you'll eventually come face-to-face with the real problem", T, ""),
    ]),
]

print("LA RELECTURA DE FIDELIDAD D.30 DE LOS DIEZ CANDIDATOS DE LA VUELTA 1 DE gerber_emyth")
print("AVISO: el trozo del libro lo saca la maquina de fuentes/gerber_emyth/<unidad>.md y")
print("       revienta si el ancla no esta en esa linea. LA LINEA Y EL VEREDICTO LOS PONGO")
print("       YO LEYENDO: es el numerador que D.30 dice que ninguna guarda puede poner.")
print()

por_unidad = {}
for unidad, identificador, filas in TANDA:
    datos = json.load(io.open(BANDEJA % identificador, encoding="utf-8"))
    escritos = len(datos["pasos_accionables"])
    if escritos != len(filas):
        raise SystemExit("%s tiene %d pasos y la relectura cubre %d"
                         % (identificador, escritos, len(filas)))
    puentes = sum(1 for f in filas if "PUENTE" in f[3])
    acumulado = por_unidad.setdefault(unidad, [0, 0, 0])
    acumulado[0] += 1
    acumulado[1] += escritos
    acumulado[2] += puentes
    print("### `%s`, unidad `%s`, %d pasos, todos releidos" % (identificador, unidad, escritos))
    print()
    print("| paso de `%s` | la salida del libro, pegada por `.gerber_v1/fidelidad.py` | veredicto |"
          % identificador)
    print("|---:|---|---|")
    for numero, linea, ancla, veredicto, nota in filas:
        cuerpo = veredicto + (", " + nota if nota else "")
        print("| `%d` | `%s` | %s |" % (numero, cita(unidad, linea, ancla), cuerpo))
    print()

print("## PASOS INVENTADOS POR CAPITULO (`D.30`), FILA POR UNIDAD MAS TOTAL")
print()
print("| unidad | nodos | pasos escritos | pasos releidos | **PUENTE** | **PASOS INVENTADOS, por ciento** |")
print("|---|---:|---:|---:|---:|---:|")
tn = tp = tb = 0


def pct(parte, total):
    return ("%.2f" % (100.0 * parte / total)).replace(".", ",")


for unidad in sorted(por_unidad):
    nodos, pasos, puentes = por_unidad[unidad]
    tn += nodos
    tp += pasos
    tb += puentes
    print("| `%s` | %d | %d | %d | **%d** | **%s** |"
          % (unidad, nodos, pasos, pasos, puentes, pct(puentes, pasos)))
print("| **el lote entero** | **%d** | **%d** | **%d** | **%d** | **%s** |"
      % (tn, tp, tp, tb, pct(tb, tp)))
print()
print("peor capitulo: %s por ciento   tope: 10   total: %s por ciento"
      % (max(pct(b, p) for _n, p, b in por_unidad.values()), pct(tb, tp)))
