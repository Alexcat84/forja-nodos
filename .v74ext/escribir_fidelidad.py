# -*- coding: utf-8 -*-
"""Vuelta 74, TAREA 3: escribe .v74ext/fidelidad.tsv, una fila por paso de los tres nodos de cap_13 de scott_radical_candor que
nombra d084, en el formato de .v73ext/fidelidad.tsv (id | paso | marca | linea | nota). La nota abre con el arranque literal de la
cita, copiado del capitulo con sus apostrofos curvos, para que la copia de citas.sh lo localice; despues va lo que decide la marca.
Se escribe por un script y no a mano solo para no perder los apostrofos curvos del libro al teclear. Las marcas y los DISCUTIBLE
se escribieron aqui, fila a fila, antes de correr ninguna comprobacion."""
import io
A = '’'
C = 'contar_cuatro_historias_propias_ver_hueco_intencion'
E = 'dar_elogio_disciplina_igual_critica'
M = 'medir_critica_respuesta_oyente_brujula'
F = [
 (C, 1, 'T', 43, 'Storytelling is a great way to develop both self-awareness and relational awareness', 'Y el por que funciona que el paso anuncia es el why it works de la misma linea, que el libro pone antes del ejercicio'),
 (C, 2, 'T', 45, 'First, think of your Radical Candor story', 'Can you remember a time when you were screwing up, someone told you, y el resto del paso es la misma pregunta'),
 (C, 3, 'T', 45, 'If you tell your team your story and what it means to you', 'El libro lo pone en condicional y el paso lo manda: es la premisa del propio ejercicio, que es contar historias al equipo (L43, y el share them with their teams de L55). DISCUTIBLE D74.4'),
 (C, 4, 'T', 45, 'you are doing two important things at once', 'One, self-awareness and humility, Two, genuinely appreciate criticism, y This will make it easier to solicit feedback, en la misma linea'),
 (C, 5, 'T', 47, 'The next three stories', 'Las tres agrupadas, your Obnoxious Aggression, Manipulative Insincerity, and Ruinous Empathy stories, y para que sirven: relational awareness'),
 (C, 6, 'T', 49, 'Think about your Obnoxious Aggression story', 'Las dos preguntas del paso son las dos del libro'),
 (C, 7, 'T', 49, 'Dig deep here', 'What' + A + 's a moment you cringe looking back on, en la misma linea'),
 (C, 8, 'T', 49, 'Your story is by definition better than the story Kim tells', 'El libro compara y el paso manda contar la propia; la orden la escribe el libro para la historia siguiente en L51, Don' + A + 't tell Kim' + A + 's Bob story. DISCUTIBLE D74.5'),
 (C, 9, 'T', 49, 'It will help you understand the impact you have on others', 'Y lo del equipo es el It will also help your team understand you de la misma linea'),
 (C, 10, 'T', 51, 'Next, think about your Ruinous Empathy story', 'La pregunta del paso es la del libro'),
 (C, 11, 'T', 51, 'Don' + A + 't tell Kim' + A + 's Bob story from Chapter Two, tell yours', 'Y la vez en que intentabas ser amable es el When were you trying to be nice de la misma linea'),
 (C, 12, 'T', 51, 'The regret you feel recalling the incident', 'Arrepentimiento y vulnerabilidad construyen la consciencia de la relacion'),
 (C, 13, 'T', 53, 'Finally, and hardest of all, think of your Manipulative Insincerity story', 'Las dos preguntas del paso son las dos del libro'),
 (C, 14, 'T', 53, 'It' + A + 's really hard to see yourself as backstabbing', 'Y we are all guilty of these behaviors from time to time, en la misma linea'),
 (C, 15, 'T', 55, 'When people unpack their own stories, and share them with their teams', 'El gap between their intentions and the impact de la misma linea'),
 (C, 16, 'T', 55, 'Awareness is the first step toward change', 'Y You can make your impact align with your intentions, en la misma linea'),
 (C, 17, 'T', 57, 'Every person is different', 'Y You' + A + 've got to adjust how you talk so that you can be clear and kind, sin sentirte camaleon, en la misma linea'),
 (E, 1, 'T', 251, 'criticism is like your brake and praise is like your accelerator', 'Las cuatro frases del paso son las cuatro de la linea'),
 (E, 2, 'T', 267, 'reluctant to praise others because it' + A + 's much easier to look', 'Y The goal of guidance is to help others succeed, en la misma linea'),
 (E, 3, 'T', 269, 'Other times people use praise as a weapon', 'El ejemplo, el autobus y They will not get a repetition of the success, todo de la misma linea'),
 (E, 4, 'T', 269, 'Good praise is specific and sincere, and inspires others rather than making odious comparisons', 'Transcripcion en imperativo'),
 (E, 5, 'T', 271, 'The focus on praise requires real discipline', 'Y la tentacion de dar critica despues de pedirla, en la misma linea'),
 (E, 6, 'T', 271, 'very often the thing that has been bothering you has been bothering you for so long', 'Y If all you can see is the negative, en la misma linea'),
 (E, 7, 'T', 271, 'So focus on the good stuff', 'Praise first, en la misma linea'),
 (E, 8, 'T', 273, 'praise helps people focus on their strengths', 'Transcripcion'),
 (E, 9, 'T', 273, 'Sometimes, you have to make sure a person gets to a level of proficiency', 'Transcripcion'),
 (E, 10, 'T', 273, 'you get more bang for the buck out of focusing on strengths than weaknesses', 'Transcripcion'),
 (E, 11, 'T', 273, 'Praise reveals what works and makes it usable, repeatable', 'Y it' + A + 's practical, how a strength can lead to success, cares personally y challenges directly, todo de la misma linea'),
 (E, 12, 'T', 277, 'borrowed from Karen Sipprell', 'La pregunta y The answer, typically, is none at all, de la misma linea'),
 (E, 13, 'T', 279, 'When you' + A + 're vague with praise, it is just as likely to leave a person feeling patronized', 'Y An empty great job can sound condescending, en la misma linea'),
 (E, 14, 'T', 279, 'Specific praise helps the person and the team understand what success looks like', 'Y It gives ambitious team members a model to follow'),
 (E, 15, 'T', 279, 'the guidelines for giving Radically Candid feedback work for both praise and criticism', 'Las tres pautas del paso son las tres de la linea'),
 (E, 16, 'T', 283, 'Pair up with a colleague and share one specific piece of praise with each other', 'Transcripcion'),
 (E, 17, 'P', 283, 'We' + A + 've found that people walk away from this exercise feeling seen, connected, and inspired', 'PUENTE de clausula: el paso dice lo que el texto ha medido, y el libro dice We' + A + 've found y We' + A + 've heard, que es lo que vieron en sus talleres y no una medida. Lo demas del paso es transcripcion. Propuesta: Cuenta con lo que el texto dice haber visto en ese ejercicio. DISCUTIBLE D74.6'),
 (E, 18, 'T', 285, 'It' + A + 's actually not hard to find things to praise each other for', 'Y set an intention, get curious, say something really specific, en la misma linea'),
 (E, 19, 'T', 285, 'Thanks for asking that question about being late for meetings', 'Y el de la hija, en la misma linea'),
 (E, 20, 'T', 287, 'While the primary purpose of praise is to show people what direction we' + A + 're headed in', 'Y It' + A + 's a fast, easy way to build the skill of giving voice to the things you appreciate, en la misma linea'),
 (M, 1, 'T', 291, 'Radical Candor gets measured not at your mouth but at the other person' + A + 's ear', 'Transcripcion'),
 (M, 2, 'T', 293, 'there are no words that serve simultaneously as a scalpel and emotional Novocain', 'Y el People often hoped there were some magic words del arranque de la linea'),
 (M, 3, 'T', 293, 'Sometimes Radical Candor will sting a little bit', 'Los dos casos y lo que toca en cada uno, de la misma linea'),
 (M, 4, 'T', 295, 'use the Radical Candor framework like a compass', 'El libro dice You can, however, use: el can es el que se opone a que no haya palabras magicas, y la frase siguiente de la linea ya va en imperativo, Pay close attention. DISCUTIBLE D74.7'),
 (M, 5, 'T', 295, 'Pay close attention to the other person' + A + 's response to what you' + A + 've said', 'Transcripcion'),
 (M, 6, 'T', 297, 'The way you listen is more important than the way you talk', 'Transcripcion'),
 (M, 7, 'T', 297, 'When offering Compassionate Candor, start gently and then gauge the other person' + A + 's response', 'Los cuatro medios del paso son los cuatro de la linea, y las dos preguntas tambien'),
 (M, 8, 'T', 297, 'You cannot do this if you are on your phone or on your computer', 'El parentesis del final de la linea'),
 (M, 9, 'T', 299, 'If the person you' + A + 're talking to seems sad, this is your cue', 'Transcripcion'),
 (M, 10, 'T', 299, 'This is hard because when confronted with someone who seems upset', 'Y Instead, now is your time to show that you care, en la misma linea'),
 (M, 11, 'T', 301, 'Using the framework like a compass can help keep you out of the Ruinous Empathy trap', 'El can help va en el paso como para no caer, que es su fin y no una orden nueva. DISCUTIBLE D74.7'),
 (M, 12, 'T', 303, 'when you get an angry response from the person you' + A + 're talking to', 'Y attend to the emotions in the room, to show that you care personally'),
 (M, 13, 'T', 303, 'This is hard because when the other person is angry', 'Y Nothing will move you down on the Care Personally axis faster than anger'),
 (M, 14, 'T', 305, 'One way to show you care when confronted with negative emotions is to name the emotion', 'El paso dice la via que el texto da donde el libro dice One way, y el guion es el de la linea. DISCUTIBLE D74.8'),
 (M, 15, 'T', 305, 'Don' + A + 't use my phrasing, use your own words', 'Transcripcion'),
 (M, 16, 'T', 305, 'Often just naming an emotion can help a person feel seen', 'Y Ignoring emotions makes the other person feel invisible or invalidated'),
 (M, 17, 'T', 307, 'you might misunderstand the emotion you' + A + 're seeing', 'El ejemplar de Kim y So be humble when naming the emotion, de la misma linea'),
 (M, 18, 'T', 307, 'And whatever you do, don' + A + 't judge the emotion', 'Y Eliminate don' + A + 't take it personally from your vocabulary'),
 (M, 19, 'T', 307, 'When all else fails, a simple response to negative emotions is to ask', 'Transcripcion'),
 (M, 20, 'T', 309, 'They are defensive or oblivious or hopelessly optimistic or overconfident or distracted', 'Y This is your cue to move to the right on the Challenge Directly dimension'),
 (M, 21, 'T', 309, 'Being extremely clear can feel harsh', 'Y el mantra It' + A + 's not mean, it' + A + 's clear'),
 (M, 22, 'T', 311, 'One thing that helps in these moments is to focus on the long term', 'Transcripcion'),
 (M, 23, 'T', 313, 'Sometimes when someone is shutting down it' + A + 's because they disagree', 'Y Your first goal is to get them to tell you if they disagree'),
 (M, 24, 'T', 313, 'There' + A + 's a risk that when you do this, the other person will come back at you aggressively', 'Y If this happens, acknowledge that you are not perfect'),
 (M, 25, 'T', 313, 'A useful mantra for giving criticism is listen-challenge-commit', 'El paso de en medio es el challenge del Don' + A + 't skip over giving them an opportunity to challenge you'),
 (M, 26, 'T', 315, 'Just to make sure we' + A + 're on the same page, can you tell me what you just heard', 'Transcripcion del guion'),
 (M, 27, 'T', 315, 'I don' + A + 't feel like I' + A + 'm being heard', 'Transcripcion del guion'),
 (M, 28, 'T', 315, 'May I be much more direct with you', 'Transcripcion del guion'),
 (M, 29, 'T', 319, 'ONE MISTAKE THAT people often make is to draw attention to consequences for noncompliance', 'Y el ejemplo del puesto en riesgo con su unfair consequence'),
 (M, 30, 'T', 319, 'You' + A + 're trying to engage the person' + A + 's intrinsic desire to improve', 'Y la pregunta del condenado sin juicio, en la misma linea'),
 (M, 31, 'T', 319, 'if the problem is going to cause the person to be put on a performance-improvement plan', 'Y the sooner you tell them the better'),
 (M, 32, 'T', 321, 'It can also help to bring several specific examples of the problem', 'El paso lo manda y conserva el ayuda del libro en su propia letra. DISCUTIBLE D74.7'),
 (M, 33, 'T', 321, 'If you get interrupted after the first one with excuses', 'El guion es el de la linea, con su algo como y su usa tus palabras, As always, use your own words, not ours'),
]
CAB = [
 '# Vuelta 74, TAREA 3: la relectura de fidelidad (D.30) de los tres nodos de cap_13 de scott_radical_candor que d084 nombra',
 '# (contar_cuatro_historias_propias_ver_hueco_intencion, dar_elogio_disciplina_igual_critica, medir_critica_respuesta_oyente_brujula),',
 '# que VIVEN EN EL GRAFO: paso a paso contra fuentes/scott_radical_candor/cap_13.md, leido entero en esta vuelta. Formato de',
 '# .v73ext/fidelidad.tsv. Marca: T transcripcion, P puente (entero o de clausula; la clausula reescrita CUENTA como P, ACTA 62 62.5;',
 '# la posibilidad convertida en orden tambien, D71.9 y D73.3). La nota abre con el arranque literal de la cita, que localiza',
 '# .v74ext/citas.sh. Lo marcado DISCUTIBLE se marco al escribir la fila, antes de ninguna comprobacion. NINGUN NODO SE CORRIGE:',
 '# un P se trae con su texto, su linea y la correccion propuesta (encargo TAREA 3.2).',
 '# id | paso | marca | linea | lo que decide la marca',
]
with io.open('.v74ext/fidelidad.tsv', 'w', encoding='utf-8', newline='\n') as f:
    f.write('\n'.join(CAB) + '\n')
    for i, p, m, l, frag, nota in F:
        f.write('%s | %d | %s | L%d | %s ... %s\n' % (i, p, m, l, frag, nota))
print('filas escritas: %d' % len(F))
