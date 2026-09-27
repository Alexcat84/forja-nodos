# -*- coding: utf-8 -*-
"""CANDIDATO 7 DE LA VUELTA 53: cap_06 P25, L65, LAS SEIS PREGUNTAS ZANJADAS POR ADELANTADO.

Se escribe y se pasa por la aduana EN EL MISMO ACTO (EXTRACTOR.md 16).
"""
import io
import json
import os

ID = "zanjar_seis_preguntas_decision_adelantado"
DESTINO = "cuarentena/grove_high_output/%s.json" % ID

NODO = {
    "id": ID,
    "titulo": "Zanjar por adelantado las seis preguntas de una decision: que, cuando, quien decide, a quien se consulta, quien ratifica y a quien se informa",
    "dominio": "gestion_equipos",
    "estado": "vivo",
    "ids_alias": [],
    "nodos_previos": [],
    "nodos_siguientes": [],
    "atribuciones": [],
    "fuentes": [{"clave": "grove_high_output", "fecha": "2026-09-19"}],
    "denominaciones": {
        "nombre_largo": "Las seis preguntas importantes que el mando zanja antes de que empiece la decision, porque la toma de decisiones tiene una salida y se le pide calidad y plazo como a cualquier otro proceso de mando",
        "sigla": "",
        "otros_idiomas": [
            {"idioma": "ingles", "termino": "six important questions"},
            {"idioma": "ingles", "termino": "ratify or veto"},
        ],
    },
    "condiciones_activacion": "Cuando va a empezar un proceso de decision y todavia nadie ha dicho que se decide, quien decide, a quien se consulta, quien puede vetarlo y a quien hay que contarselo despues.",
    "entregable_esperado": "Las seis preguntas contestadas por escrito antes de empezar: la decision que hay que tomar, su plazo, quien decide, a quien se consulta antes, quien ratifica o veta, y a quien se informa despues.",
    "pasos_accionables": [
        "Cuenta con que la toma de decisiones, como las demas cosas que hace un mando, lleva asociada una salida, y en este caso esa salida es la decision misma.",
        "Di con claridad desde el principio que esperas exactamente eso, una salida de alta calidad y en plazo, porque es entonces cuando el proceso tiene mas probabilidades de darla, igual que los demas procesos de mando.",
        "Zanja por adelantado las seis preguntas importantes, que es una de las tareas clave del mando.",
        "Pregunta primero que decision hay que tomar.",
        "Pregunta cuando tiene que estar tomada.",
        "Pregunta quien va a decidir.",
        "Pregunta a quien hay que consultar antes de tomar la decision.",
        "Pregunta quien va a ratificar o vetar la decision.",
        "Pregunta a quien hay que informar de la decision.",
    ],
    "resumen_teorico": (
        "UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_06.md, unidad Cap. 5, titulo textual Decisions, Decisions. "
        "Sale de la PIEZA P25 de la frontera publicada hoy en OO.2.a, L65, 65 palabras. "
        "FRONTERA DENTRO DEL NODO, PUBLICADA ANTES DE CORTAR (EXTRACTOR.md 10): los pasos 1, 2 y 3 salen de L65, que es la cabeza; los pasos 4 a 9 salen de "
        "la PIEZA P26, L67 a L77, que es la lista de las seis preguntas, una por linea. POR ESO P26 LLEVA CERO NODOS EN LA FRONTERA: sus seis lineas son "
        "partes de esta cabeza y ninguna de las seis trae procedimiento propio, cada una es una sola pregunta. "
        "POR QUE ES PROCEDIMIENTO, por la prueba del inventario de EXTRACTOR.md 9.1: el libro DICE CUANTAS SON (six important questions), las nombra una a "
        "una en su propia linea, y las pone como tarea clave del mando a resolver in advance. Inventario de OBJETOS DE TRABAJO, no de fines. "
        "POR QUE NO DECLARO NINGUNA ARISTA DE D.37 PESE A SER CABEZA CONTADA: D.37 pide que las partes EXISTAN COMO NODOS, y en mi frontera de hoy las seis "
        "preguntas dan cero nodos precisamente porque no tienen procedimiento propio. No hay hijo al que apuntar, asi que no hay arista que cablear. Si una "
        "vuelta posterior encontrara procedimiento propio para alguna, la arista se declara entonces. "
        "DE DONDE SALE CADA PASO, uno a uno: paso 1 de L65 (Basically, like other things managers do, decision-making has an output associated with it, which "
        "in this case is the decision itself); paso 2 de L65 (Like other managerial processes, decision-making is likelier to generate high-quality output in "
        "a timely fashion if we say clearly at the outset that we expect exactly that); paso 3 de L65 (In other words, one of the manager's key tasks is to "
        "settle six important questions in advance); paso 4 de L67 (What decision needs to be made?); paso 5 de L69 (When does it have to be made?); paso 6 "
        "de L71 (Who will decide?); paso 7 de L73 (Who will need to be consulted prior to making the decision?); paso 8 de L75 (Who will ratify or veto the "
        "decision?); paso 9 de L77 (Who will need to be informed of the decision?). "
        "RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 9 pasos, 9 TRANSCRIPCION, 0 PUENTE. "
        "AQUI LA TENTACION ERA LA PEOR DE TODAS Y LA DECLARO ENTERA: este nodo trata justo de destinatarios, responsables y plazos, que son las TRES especies "
        "de PUENTE que el lote 1 pago. La diferencia es que aqui el libro las pone como PREGUNTAS que el mando tiene que contestar, no como respuestas. Por "
        "eso los pasos 4 a 9 preguntan y no contestan: NO escribo quien debe decidir, ni a quien hay que consultar, ni cuanto plazo se da, ni a quien se "
        "informa, porque eso lo contesta cada caso y el libro no lo contesta aqui. Convertir estas seis preguntas en seis respuestas seria escribir el nodo "
        "entero yo. NO escribo tampoco donde se anotan ni quien las custodia. "
        "EL CASO DE FILIPINAS NO ENTRA (manual 3.5): L79 a L89 aplican estas seis preguntas a la ampliacion de la planta de Filipinas, y ese caso es el "
        "EJEMPLO NOMBRADO de esta doctrina, no su casa. Por eso ni el entregable ni ningun paso llevan un dato de aquel caso, ni el plazo de un mes, ni el "
        "nombre de Gordon Moore, ni las cuatro plantas. "
        "NI UNA CIFRA A atribuciones: el seis es denominacion de la serie, no una medicion del autor con fecha de corte. "
        "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO: los pasos 4 a 9 son preguntas y no imperativos de accion, y un lector estricto puede decir que un "
        "nodo cuyos pasos preguntan no ejecuta nada. Lo sostengo porque el propio libro los llama key task del mando y manda settle, zanjar, y porque lo "
        "ejecutable aqui es exactamente obtener las seis respuestas antes de empezar. Si cae, cae DENTRO de mi marcado."
    ),
}

if os.path.exists(DESTINO):
    raise SystemExit("YA EXISTE: %s" % DESTINO)
io.open(DESTINO, "w", encoding="utf-8", newline="\n").write(
    json.dumps(NODO, ensure_ascii=False, indent=1) + "\n")
print("ESCRITO: %s" % DESTINO)
print("pasos: %d" % len(NODO["pasos_accionables"]))
