# -*- coding: utf-8 -*-
"""LA RELECTURA DE FIDELIDAD `D.30` DEL TRAMO DE `cap_09`, CON SU CITA PEGADA.

Es el mismo instrumento de la vuelta 33 (`.v33/fidelidad.py`) apuntado a otro capitulo:
`D.47` manda cero instrumentos nuevos, y este no lo es.

`D.35`: ninguna cita de linea se teclea sin que la salida literal del libro quede pegada
al lado. Aqui **el trozo del libro lo saca la maquina** del propio `cap_09.md`; lo que
pongo yo leyendo es **la linea que sostiene cada paso y el veredicto TRANSCRIPCION o
PUENTE**, que es el numerador que `D.30` dice que ninguna guarda puede poner.

El instrumento **comprueba que el ancla existe en esa linea** y revienta si no, y
comprueba que la relectura cubre **todos** los pasos del fichero: no se puede releer
medio nodo y publicarlo como entero.

Y VA ANTES DE QUE LOS NODOS ENTREN, que es la letra de `D.30` que la vuelta 33 rompio.
"""
import io
import json
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

LIBRO = "fuentes/scott_radical_candor/cap_09.md"
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
    ("abrazar_incomodidad_arrancar_critica_equipo", [
        (2, 25, "it's important to work so hard to earn your team's trust", T, ""),
        (3, 29, 'You are the exception to the "criticize in private" rule of thumb', T, ""),
        (4, 31, "Once I figured out who on my team was most comfortable criticizing me", T, ""),
        (5, 33, "If you have more than sixty or so people working for you", T, ""),
        (6, 35, "Too many managers fear that public challenge will undermine their authority", T, ""),
        (7, 37, "Have a go-to question", T, ""),
        (8, 39, "Embrace the discomfort", T, ""),
        (9, 41, "One technique is to count to six before saying anything else", T, ""),
        (10, 41, "If counting to six doesn't do the trick, ask the question again", T, ""),
        (11, 43, "point out when people's body language is at odds with what they're saying", T, ""),
        (12, 45, "Listen with the intent to understand, not to respond", T, ""),
        (13, 47, "Manage your feelings rather than letting them manage you", T, ""),
        (14, 49, "Reward criticism to get more of it", T, ""),
        (15, 51, "first, find something in the criticism you can agree with", T, ""),
        (16, 51, "It is never enough to simply acknowledge the other person's feelings", T, ""),
        (17, 53, "Gauge the guidance you get. Try keeping a tally", T, ""),
        (18, 53, "Try teaching the people on your team about the idea of Radical Candor", T, ""),
        (19, 53, "Print out the Radical Candor framework", T, ""),
        (20, 53, "In the first edition I mentioned a software gauge", T, ""),
    ]),
    ("organizar_sistema_recoger_quejas_equipo", [
        (1, 59, "JOHNSON & JOHNSON'S ORIGINAL credo had an interesting line", T, ""),
        (2, 59, "If you're the boss, you have to do much better than announce how employees", T, ""),
        (3, 59, "Employees won't feel free if you don't take specific actions", T, ""),
        (4, 59, "You have to organize a system. But it needn't be elaborate", T, ""),
        (5, 61, "He put an orange box with a slit on the top in a high-traffic area", T, ""),
        (6, 61, "At his all-hands meeting he'd reach into the box and answer off the cuff", T, ""),
        (7, 61, "always amazingly respectful and took on each question thoughtfully", T, ""),
        (8, 63, "he would fix problems when people pointed them out rather than shoot the messenger", T, ""),
        (9, 63, "Over time the orange box emptied out", T, ""),
    ]),
    ("correr_semana_arreglo_averias_gestion", [
        (1, 67, "Everyone will stop working on new features for a week and fix bugs", T, ""),
        (2, 67, "A bug fix-it week is sort of the opposite of a Hack Week", T, ""),
        (3, 69, "it would be good hygiene to have regular management fix-it weeks", T, ""),
        (4, 69, "a system was created where people could log annoying management issues", T, ""),
        (5, 71, "The management bug tracking system was public, so people could vote to set priorities", T, ""),
        (6, 71, "Somebody was assigned the job of reading through them all and grouping duplicates", T, ""),
        (7, 71, "during management fix-it week, managers would have bugs assigned to them", T, ""),
        (8, 71, "They'd cancel all regularly scheduled activities", T, ""),
    ]),
    ("dar_guia_humilde_tres_tecnicas", [
        (1, 79, "I start with being humble because it's absolutely essential", T, ""),
        (2, 79, "a common concern that people raise about giving feedback is", T, ""),
        (3, 83, "Situation, behavior, impact", T, ""),
        (4, 83, "This helps you avoid making judgments about the person's intelligence", T, ""),
        (5, 87, "Situation, behavior, and impact applies to praise as well as to criticism", T, ""),
        (6, 91, "Left-hand column", T, ""),
        (7, 93, "Think of a conversation you had that was frustrating", T, ""),
        (8, 93, "Take out a clean sheet of paper and draw a line down the middle", T, ""),
        (9, 93, "Write down what you actually said in the right-hand column", T, ""),
        (10, 93, "Write down what you thought in the left-hand column", T, ""),
        (11, 93, "Now think about when the conversation went sideways", T, ""),
        (12, 93, "The point is not just to say whatever is in your left-hand column", T, ""),
        (13, 95, '"Ontological Humility."', T, ""),
        (14, 95, "Broccoli is yucky", T, ""),
        (15, 95, "when you are mindful that your subjective experience is not objective truth", T, ""),
    ]),
    ("dar_guia_util_cuatro_recordatorios", [
        (1, 101, "being helpful doesn't mean you have to be omniscient", T, ""),
        (2, 103, "Stating your intention to be helpful can lower defenses", T, ""),
        (3, 103, "Try a little preamble", T, ""),
        (4, 105, "Show, don't tell", T, ""),
        (5, 105, "retreating to abstractions is a prime example of Ruinous Empathy", T, ""),
        (6, 107, "the same principle goes for praise", T, ""),
        (7, 109, "Finding help is better than offering it yourself", T, ""),
        (8, 111, "you will have a colleague or acquaintance who can help", T, ""),
        (9, 113, "Guidance is a gift, not a whip or a carrot", T, ""),
        (10, 113, "Don't let the fact that you can't offer a solution make you reluctant", T, ""),
    ]),
]

TANDA += [
    ("dar_guia_acto_seis_consejos", [
        (1, 117, "Giving guidance as quickly and as informally as possible", T, ""),
        (2, 119, "If you wait too long to give guidance, everything about it gets harder", T, ""),
        (3, 121, "if either you or the other person is hungry, angry, or tired", T,
         "**la excepcion es del libro y va de paso, no de comentario**"),
        (4, 121, "there is a difference between saying it right away and nitpicking", T, ""),
        (5, 123, "Say it in 2-3 minutes between meetings", T, ""),
        (6, 123, "Try thinking of it as brushing your teeth instead", T, ""),
        (7, 125, "If you have five direct reports", T,
         "**las cifras son del libro**: cinco personas, tres elogios, una critica, sesenta minutos"),
        (8, 127, "keep slack time in your calendar", T, ""),
        (9, 127, "simply be willing to be late to your next meeting", T, ""),
        (10, 129, 'Don\'t "save up" guidance for a 1:1 or a performance review', T, ""),
        (11, 131, "Guidance has a short half-life", T, ""),
        (12, 133, "Unspoken criticism explodes like a dirty bomb", T,
         "**es el rotulo que la cuenta vieja se dejaba fuera**, y el paso ya lo transcribia"),
        (13, 135, "Avoid black holes", T, ""),
        (14, 135, "is to let people present their own work whenever possible", T, ""),
    ]),
    ("elegir_medio_dar_guia_jerarquia_modos", [
        (1, 139, "the clarity of your guidance gets measured at the other person's ear", T, ""),
        (2, 139, "When you see a person's body language and facial expression", T, ""),
        (3, 141, "you are trying to avoid seeing the other person's emotional reaction", T, ""),
        (4, 141, "When somebody is blowing you off", T, ""),
        (5, 145, "Immediate vs. in person", T, ""),
        (6, 145, "If the person is down the hall", T, ""),
        (7, 147, "Hierarchy of modes", T, ""),
        (8, 147, "It always feels faster to fire off an email or text", T, ""),
        (9, 149, "Multiple modes", T, ""),
        (10, 151, "If you must criticize or correct somebody over email, do not Reply All", T, ""),
        (11, 151, "reply just to the person who made the factual error", T, ""),
        (12, 151, "For praise on small things", T, ""),
        (13, 153, "If you are in a remote office", T, ""),
    ]),
    ("elogiar_publico_criticar_privado_sus_tres_matices", [
        (1, 157, "A good rule of thumb for guidance is praise in public, criticize in private", T, ""),
        (2, 157, "this is a rule of thumb, not a hard and fast rule", T, ""),
        (3, 159, "Corrections, factual observations, disagreements, and debates are different", T, ""),
        (4, 159, "There's a typo on slide six", T, ""),
        (5, 159, "Here is an example of criticizing the person", T, ""),
        (6, 161, "Adapt to an individual's preferences", T, ""),
        (7, 161, "your goal is to let them know what they did well as clearly as possible", T, ""),
        (8, 163, "Group learning", T, ""),
        (9, 163, "When I wanted to encourage public criticism", T, ""),
    ]),
    ("evitar_personalizar_guia_aceptar_personal", [
        (1, 167, "Caring personally is good. Personalizing is bad", T, ""),
        (2, 169, 'The "fundamental attribution error" will harm the effectiveness', T, ""),
        (3, 169, "1) it's generally inaccurate and 2) it renders an otherwise solvable problem", T, ""),
        (4, 169, 'Try to catch yourself when you think or say, "You are', T, ""),
        (5, 169, "Use situation, behavior, impact, or the left-hand column techniques", T, ""),
        (6, 171, 'Say "that\'s wrong" not "you\'re wrong."', T, ""),
        (7, 171, '"I think" was humbler', T, ""),
        (8, 173, "When an argument is about an issue, keep it about the issue", T, ""),
        (9, 175, 'The phrase "don\'t take it personally" is worse than useless', T, ""),
        (10, 175, "Most of us pour more time and energy into our work", T, ""),
        (11, 175, "is to acknowledge and deal with emotional responses", T, ""),
        (12, 177, "How not to personalize even when it really is personal", T, ""),
    ]),
    ("medir_guia_propia_pegatinas_marco", [
        (1, 181, "The bad news is, yes. The good news is that it can take fifteen seconds", T, ""),
        (2, 183, "explain the framework to your team and then ask them to gauge your guidance each week", T, ""),
        (3, 183, "Track your progress over time", T, ""),
        (4, 185, "A low-tech way to do this is to put a copy of the framework near your desk", T, ""),
        (5, 185, "Leave some stickers by it", T, ""),
        (6, 185, "Ask people to put stickers in the quadrant they feel best describes", T, ""),
        (7, 185, "If somebody feels you were unnecessarily harsh", T, ""),
        (8, 189, "One, it exposes people daily to the Radical Candor framework", T, ""),
        (9, 189, "You'll need to start proving to your team that you won't punish them", T, ""),
        (10, 191, "if you saw that a number of people were tagging both your praise", T, ""),
        (11, 193, "sometimes people have to overcorrect to get it right", T, ""),
        (12, 197, "you'll have good weeks and bad weeks", T, ""),
        (13, 203, "The most important thing is figuring out how others experience your guidance", T, ""),
    ]),
]

TANDA += [
    ("practicar_franqueza_radical_jefe_propio", [
        (1, 209, "It is not your moral obligation to criticize your boss if it will cost you your job", T, ""),
        (2, 209, "I recommend that you consider finding a new job with a new boss", T, ""),
        (3, 211, "Do you have to get permission to start trying it?", T, ""),
        (4, 211, "Once you start rolling out Radical Candor with your team", T, ""),
        (5, 211, "Give your boss a chance to challenge you, but assume good intent", T, ""),
        (6, 211, "If you get some positive signals", T, ""),
        (7, 213, "Start by asking for guidance before you give it", T, ""),
        (8, 213, "don't offer a critique of the criticism, and don't accept bland praise", T, ""),
        (9, 213, "that's an exception to the don't-critique-the-criticism rule of thumb", T, ""),
        (10, 215, "ask permission to give guidance", T, ""),
        (11, 215, "If your boss says no, or that's not your job", T, ""),
        (12, 215, "start with something pretty small and benign", T, ""),
        (13, 215, "If they react well and reward the candor, keep going", T,
         "**DISCUTIBLE 1**: el libro escribe *give up immediately or assume ill intent* y el paso "
         "lo traduce como *no des por supuesta la mala intencion*. El paso existe en el libro; lo "
         "que elige el candidato es una de las dos lecturas de una frase ambigua"),
        (14, 217, "use the same tips above", T, ""),
        (15, 221, "If you are able to tell your boss that you disagree with a decision", T, ""),
        (16, 221, "And once you understand the rationale more deeply", T, ""),
        (17, 221, "If they insist on knowing whether you agree", T, ""),
    ]),
    ("comprobar_criticas_hombre_mujeres_equipo", [
        (1, 293, "it can be helpful to become aware of how the woman feels about your guidance", T, ""),
        (2, 293, "Try explaining the Radical Candor framework", T, ""),
        (3, 293, "I'm trying to be Radically Candid", T, ""),
        (4, 293, "Ask her to gauge your praise and criticism", T, ""),
        (5, 293, "Even if you're not worried about gender politics", T, ""),
        (6, 293, "You may not even be aware you're going easy on some people and not others", T, ""),
    ]),
    ("exigir_critica_jefe_reticente", [
        (1, 297, "it can be helpful to make him aware that you want more feedback", T, ""),
        (2, 299, "What can I do or stop doing to make it easier for you to be Radically Candid", T, ""),
        (3, 299, "I'm worried you're so concerned about my feelings", T, ""),
        (4, 299, "The thing that I most need from you is to tell me what you really think", T, ""),
        (5, 299, "Then, pause", T, ""),
        (6, 299, "Count to six in your head", T, ""),
        (7, 299, "Embrace the discomfort", T, ""),
        (8, 299, "Do whatever it takes to drag a candid assessment out of your male colleagues", T, ""),
        (9, 299, "Review the section above on getting guidance, and double down", T, ""),
    ]),
    ("revisar_critica_mujer_agresiva_cuatro_tacticas", [
        (1, 303, "try these tactics to make sure you're not falling into the competence/likeability trap", T, ""),
        (2, 303, "don't imagine you won't fall into the trap just because you're a woman", T, ""),
        (3, 305, "Switch genders", T, ""),
        (4, 305, "Really imagine a man on your team doing exactly the same thing", T, ""),
        (5, 305, "If you'd react differently, you're about to fall into the trap", T, ""),
        (6, 309, "Be more specific", T, ""),
        (7, 309, "If you describe specific examples of how this manifests itself", T, ""),
        (8, 311, "Don't use gendered language", T, ""),
        (9, 311, "Do you use words like", T, ""),
        (10, 311, "he challenged the use of words like", T, ""),
        (11, 313, 'Never just say, "Be more likeable."', T, ""),
        (12, 313, "it's your job as the boss not to advise women how to navigate around it", T, ""),
    ]),
    ("responder_critica_abrasiva_cuatro_reglas", [
        (1, 317, "consider the following four rules of thumb", T,
         "**la cuenta CUATRO es del libro**, escrita en esta linea"),
        (2, 319, "Never stop challenging directly", T, ""),
        (3, 319, "the advice to women who are perceived as abrasive", T, ""),
        (4, 321, "Care personally-but kill the angel in the office", T, ""),
        (5, 321, "women expend too much energy picking up the office housework", T, ""),
        (6, 321, "Self-abnegation is never an effective way to show you care", T, ""),
        (7, 321, "You don't have to bake cookies or get coffee", T, ""),
        (8, 323, "The competence/likeability research has not concluded that you weren't out of line", T, ""),
        (9, 323, "Don't be the angel in the office, but remain open to the possibility", T, ""),
        (10, 325, "Just because it's wrong to kiss up and kick down", T, ""),
        (11, 325, "They are Radically Candid with their teams, but obnoxiously aggressive", T, ""),
        (12, 327, "Don't write men off", T, ""),
        (13, 329, "I might have been tempted to commit the fundamental attribution error", T, ""),
        (14, 329, "Just keep challenging directly and showing you care personally", T, ""),
    ]),
]


def main():
    print("RELECTURA DE FIDELIDAD D.30 DEL TRAMO DE cap_09, ANTES DE INSERTAR")
    print("  libro: %s" % LIBRO)
    print("  la maquina saca el trozo del libro y comprueba el ancla; el veredicto lo pongo yo")
    print("")
    tp = tv = 0
    for identificador, filas in TANDA:
        datos = ficha(identificador)
        if len(filas) != len(datos["pasos_accionables"]):
            raise SystemExit("RELECTURA INCOMPLETA en %s: %d pasos y %d releidos"
                             % (identificador, len(datos["pasos_accionables"]), len(filas)))
        print("### %s  (%d pasos)" % (identificador, len(filas)))
        print("")
        print("| paso | veredicto | la linea del libro, pegada |")
        print("|---:|---|---|")
        for paso, numero, ancla, veredicto, nota in filas:
            texto = cita(numero, ancla)
            if nota:
                texto = "%s  %s" % (texto, nota)
            print("| P%d | %s | `%s` |" % (paso, veredicto, texto))
            tp += 1
            tv += 1 if "PUENTE" in veredicto else 0
        print("")
    print("TOTAL DEL TRAMO: %d pasos releidos, %d PUENTE, %d TRANSCRIPCION" % (tp, tv, tp - tv))


if __name__ == "__main__":
    main()
