# -*- coding: utf-8 -*-
"""LA RELECTURA DE FIDELIDAD `D.30` DE LOS DOCE DE `cap_08`, CON SU CITA PEGADA.

Es el mismo instrumento de la vuelta 32 (`.v32/fidelidad.py`) apuntado a otro capitulo:
`D.47` manda cero instrumentos nuevos, y este no lo es.

`D.35`: ninguna cita de linea se teclea en una tabla sin que la salida literal del libro
quede pegada al lado. Aqui **el trozo del libro lo saca la maquina** del propio
`cap_08.md`; lo que pongo yo leyendo es **la linea que sostiene cada paso y el veredicto
TRANSCRIPCION o PUENTE**, que es el numerador que `D.30` dice que ninguna guarda puede
poner.

El instrumento **comprueba que el ancla existe en esa linea** y revienta si no, asi que
una linea mal apuntada no puede salir publicada como buena. Y comprueba que la relectura
cubre **todos** los pasos del fichero, asi que no se puede releer medio nodo y publicarlo
como entero.
"""
import io
import json
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

LIBRO = "fuentes/scott_radical_candor/cap_08.md"
LINEAS = io.open(LIBRO, encoding="utf-8").read().split("\n")

MAPA = [(chr(0x2014), "-"), (chr(0x2013), "-"), (chr(0x2019), "'"), (chr(0x2018), "'"),
        (chr(0x201c), '"'), (chr(0x201d), '"'), (chr(0x2026), "..."), (chr(0xa0), " ")]


def limpia(texto):
    for viejo, nuevo in MAPA:
        texto = texto.replace(viejo, nuevo)
    return texto.replace("|", "/")


def ficha(identificador):
    """el candidato se lee de la bandeja, y si ya entro, de su archivo (D.31)."""
    for carpeta in ("cuarentena/scott_radical_candor",
                    "cuarentena/_insertados/scott_radical_candor"):
        try:
            return json.load(io.open("%s/%s.json" % (carpeta, identificador),
                                     encoding="utf-8"))
        except IOError:
            continue
    raise SystemExit("NO ENCUENTRO AL CANDIDATO %s en ninguna de las dos sedes"
                     % identificador)


def cita(numero, ancla, largo=104):
    texto = limpia(LINEAS[numero - 1])
    donde = texto.find(ancla)
    if donde < 0:
        raise SystemExit("EL ANCLA NO ESTA EN LA LINEA %d: %r" % (numero, ancla))
    antes = "..." if donde > 0 else ""
    trozo = texto[donde:donde + largo]
    despues = "..." if donde + largo < len(texto) else ""
    return "%d: %s%s%s" % (numero, antes, trozo, despues)


T = "**TRANSCRIPCION**"

# LO QUE PONGO YO LEYENDO: (paso, linea del libro, ancla, veredicto, nota)
TANDA = [
    ("integrar_trabajo_vida_mejor_version", [
        (1, 27, "Be relentlessly insistent on bringing your fullest", T, ""),
        (2, 27, "Don't think of it as work-life balance", T, ""),
        (3, 27, "Instead, think of it as work-life integration", T, ""),
        (4, 27, "If you need to get eight hours of sleep to stay centered", T,
         "**las ocho horas son el condicional del libro y el paso las dice como suyas**: "
         "escritas como regla del lector serian la especie *el periodo* de `D.30`"),
        (5, 27, "Your work and your life can give each other a", T, ""),
    ]),
    ("definir_receta_propia_mantenerse_centrado", [
        (1, 29, 'Figure out your "recipe" to stay centered', T,
         "es el rotulo del libro, y esta escrito en imperativo por el"),
        (2, 31, "The world is full of advice here", T, ""),
        (3, 33, "Do whatever works for you", T, ""),
        (4, 33, "is to prioritize doing it (but not overdoing it) when times get tough", T, ""),
        (5, 33, "It's even more important to focus on making time", T, ""),
        (6, 33, "A very successful entrepreneur I knew went to the gym", T,
         "**la receta ajena va dicha como ajena**: las ocho horas y los cuarenta y cinco "
         "minutos son de la autora, y el propio `L33` escribe *do whatever works for you*"),
        (7, 35, "Also, every so often I need to read a novel", T, ""),
        (8, 35, "If I skip one or two of those things for a day or two", T, ""),
        (9, 35, "If I can manage to do those things, I can usually stay centered", T, ""),
    ]),
    ("agendar_cuidados_propios_cumplirlos", [
        (1, 39, "Put the things you need to do for yourself on your calendar", T, ""),
        (2, 39, "If you are having trouble leaving the office in time", T, ""),
        (3, 39, "Pretend you have a train to catch", T, "el tren es del libro, no imagen mia"),
        (4, 43, "Don't blow off those meetings with yourself", T, ""),
        (5, 43, "or let others schedule over them any more than you would", T, ""),
    ]),
    ("ceder_autoridad_unilateral_equipo", [
        (1, 47, "is to relinquish unilateral authority", T, ""),
        (2, 47, "you're going to have to relinquish it voluntarily", T, ""),
        (3, 47, "It's natural to crave a little control", T, ""),
        (4, 49, "If you have to use someone else's name or authority", T, ""),
        (5, 49, "If you believe something to be correct, focus on showing your work", T, ""),
        (6, 51, "you're creating the conditions for them to bring it out of themselves", T, ""),
        (7, 53, "When you treat people like cogs in a machine", T, ""),
        (8, 55, "the only thing worse than tyranny is anarchy", T, ""),
        (9, 57, "She carefully constructed a hiring process, a promotion process", T,
         "el caso de Google va **nombrado dentro** del paso que lo usa (manual 3.5)"),
        (10, 59, "Managers couldn't just hire people", T, ""),
        (11, 59, "Promotions were decided not by the managers but by a committee of peers", T, ""),
        (12, 59, "Performance ratings were influenced by 360-degree feedback", T, ""),
        (13, 61, "Whether or not Google's extreme approach would work for your company", T,
         "**la reserva es del libro y va dentro del paso**, no puesta por mi"),
        (14, 63, "I'm not recommending abdication or anarchy", T, ""),
        (15, 65, "I recommend that you look for places where you can let go", T, ""),
    ]),
    ("dominar_arte_socializar_trabajo", [
        (1, 69, "While retreats and parties can be productive if people on your team", T, ""),
        (2, 71, "Spending time with people from work in a more relaxed setting", T, ""),
        (3, 71, "It doesn't have to be expensive", T, ""),
        (4, 71, "Meeting each other's families can also have a big impact", T, ""),
        (5, 71, "Inviting your team and their families", T, ""),
        (6, 73, "when these events are introduced by management", T, ""),
        (7, 73, "You already spend a lot of hours every day with your colleagues", T, ""),
        (8, 73, "it's better to use the time after work to keep yourself centered", T, ""),
        (9, 75, "bear these warnings in mind", T,
         "**nombra sus dos advertencias pero NO dice cuantas son**: la arista al hijo es "
         "`D.29`, no `D.37` (correccion del titular del 11 sep 2026)"),
    ]),
    ("evitar_presion_social_actos_equipo", [
        (1, 79, "Fun events can be a good way to get to know the people on your team", T, ""),
        (2, 79, "the social pressure will drag some people into situations", T, ""),
        (3, 79, "You shouldn't have to barf over the side of a boat", T,
         "el caso de Marissa Mayer va **nombrado dentro** del paso"),
        (4, 81, "It's important to avoid those ironic moments", T, ""),
        (5, 81, "I once worked with a leader whose team was working eighty hours a week", T, ""),
        (6, 81, "the greatest gift you can give your team is to let them go home", T, ""),
    ]),
    ("construir_confianza_equipo_tiempo_solas", [
        (1, 95, "Building trust in any relationship takes time", T, ""),
        (2, 95, "It's a big mistake to assume too much trust too quickly", T, ""),
        (3, 95, "If you never ask a single question about a person's life", T, ""),
        (4, 95, "Probably the most important thing you can do to build trust", T,
         "**`on a regular basis` es del libro y el periodo NO se escribe**: es la especie "
         "*el periodo* de `D.30`, y el libro no dice cada cuanto"),
        (5, 95, "Holding regular 1:1s in which your direct report sets the agenda", T, ""),
        (6, 95, "The way you ask for criticism and react when you get it", T, ""),
        (7, 95, 'Having annual "career conversations" is also an excellent way', T,
         "**este si lleva periodo, y lo lleva porque el libro escribe `annual`**"),
    ]),
    ("vivir_valores_propios_evitar_listarlos", [
        (1, 99, "But I'm extremely wary of these kinds of exercises", T, ""),
        (2, 99, "First, developing one's personal values is the work of a lifetime", T, ""),
        (3, 99, "Second, while some people find it helpful to articulate their values", T, ""),
        (4, 99, "Third, and most important, many people feel that their values", T, ""),
        (5, 99, "Others may take the exercise as an invitation to proselytize", T, ""),
        (6, 99, "An exercise that requires people to talk publicly about their values", T,
         "el caso del alumno esta en `L101` y va **nombrado dentro** del paso"),
        (7, 103, "The important thing to do is to stay in touch with your personal values", T, ""),
        (8, 103, "to demonstrate them in how you manage your team", T, ""),
        (9, 103, "Live your values", T, ""),
    ]),
    ("demostrar_apertura_visiones_distintas", [
        (1, 107, "You don't have to share the same deeply personal values", T, ""),
        (2, 107, "it's a terrible idea to try to convince your colleagues", T, ""),
        (3, 107, "But you do need to respect other people's values", T, ""),
        (4, 109, "whether it's the gay man forced to weather anti-gay jokes", T,
         "los dos casos estan **en la misma frase del libro** y por eso van en el mismo paso"),
        (5, 111, "it's crucial to remind people that an important part", T, ""),
        (6, 111, "It's possible to care personally about a person who disagrees", T, ""),
        (7, 111, "The fastest path to artificial relationships at work", T, ""),
        (8, 111, "starts with the basic respect and common decency", T, ""),
        (9, 111, "the work is the bond everybody on a team does share", T, ""),
        (10, 121, "Dick spent real energy training himself to say", T,
         "el caso arranca en `L115`; **el unico acto ejecutable de `L113` a `L121` es este**, "
         "y el Test de Asociacion Implicita de `L113` se deja fuera por ser rasgo del "
         "retratado y no cifra que el libro afirme"),
    ]),
    ("manejar_contacto_fisico_regla_platino", [
        (1, 125, "a super-professional handshake just doesn't cut it", T, ""),
        (2, 131, "before he said anything to me he gave me a great big bear hug", T,
         "el caso arranca en `L127` y va **nombrado dentro** del paso"),
        (3, 141, "hold a hug for at least six seconds", T,
         "**es la unica cifra de autor del capitulo** y va a `atribuciones` (principio 5), "
         "citada en `L139` como de Gretchen Rubin en `The Happiness Project`"),
        (4, 143, "If a hug is sexual or belittling or obviously unwanted", T, ""),
        (5, 143, "If all you ever give is hugs and you never challenge", T, ""),
        (6, 143, "don't feel bad when the other person doesn't want to be hugged", T, ""),
        (7, 145, 'you have to obey the "platinum rule."', T, ""),
        (8, 145, "If most people on your team are comfortable with hugs but a couple are not", T, ""),
        (9, 149, "It's fine to push yourself past your comfort zone", T, ""),
    ]),
    ("reconocer_emociones_propias_avisar_equipo", [
        (1, 153, "I know what kind of day I'm gonna have by the kind of mood", T, ""),
        (2, 155, "But repressing those feelings tends not to work", T, ""),
        (3, 155, "You can't successfully hide how you feel from people", T, ""),
        (4, 155, "You don't want to take your bad days out on your team", T, ""),
        (5, 155, "The best you can do is to own up to how you feel", T, ""),
        (6, 157, "I learned simply to say something along the lines of", T,
         "**es un guion literal del libro**, no una plantilla mia"),
        (7, 159, "If you have a truly terrible emotional upset in your life, stay home for a day", T,
         "**el dia en casa lo escribe el libro**: `stay home for a day`"),
    ]),
    ("dominar_reacciones_emociones_ajenas", [
        (1, 163, "do not try to prevent, control, or manage other people's emotions", T, ""),
        (2, 163, "There are fewer faster paths to Manipulative Insincerity", T, ""),
        (3, 163, "Do acknowledge them and react compassionately", T, ""),
        (4, 167, "Acknowledge emotions", T, ""),
        (5, 169, "Ask questions", T, ""),
        (6, 171, "Adding your guilt to other people's difficult emotions", T, ""),
        (7, 173, "Telling other people how to feel will backfire", T, ""),
        (8, 175, "If you really can't handle emotional outbursts, forgive yourself", T, ""),
        (9, 177, "Keep tissues a short walk away from your desk", T, ""),
        (10, 179, "Keep some closed bottles of water at your desk", T, ""),
        (11, 181, "Walk, don't sit", T,
         "los siete consejos de `L167` a `L181` **no llevan rotulo de linea propia**, que es "
         "el criterio de corte de esta casa: por eso son pasos y no siete nodos. Va marcado "
         "DISCUTIBLE"),
    ]),
]

print("LA RELECTURA DE FIDELIDAD D.30 DE LOS DOCE DE cap_08")
print("AVISO: el trozo del libro lo saca la maquina de %s y" % LIBRO)
print("       revienta si el ancla no esta en esa linea. LA LINEA Y EL VEREDICTO LOS PONGO")
print("       YO LEYENDO: es el numerador que D.30 dice que ninguna guarda puede poner.")
print()

total_pasos = 0
total_puentes = 0
for identificador, filas in TANDA:
    datos = ficha(identificador)
    escritos = len(datos["pasos_accionables"])
    if escritos != len(filas):
        raise SystemExit("%s tiene %d pasos y la relectura cubre %d"
                         % (identificador, escritos, len(filas)))
    total_pasos += escritos
    total_puentes += sum(1 for f in filas if "PUENTE" in f[3])
    print("### `%s`, %d pasos, todos releidos" % (identificador, escritos))
    print()
    print("| paso | la salida del libro, pegada por `.v33/fidelidad.py` | veredicto |")
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
