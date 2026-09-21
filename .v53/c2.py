# -*- coding: utf-8 -*-
"""CANDIDATO 2 DE LA VUELTA 53: cap_06 P9, L33, EL NIVEL COMPETENTE MAS BAJO.

Se escribe y se pasa por la aduana EN EL MISMO ACTO (EXTRACTOR.md 16).
"""
import io
import json
import os

ID = "decidir_nivel_competente_inferior"
DESTINO = "cuarentena/grove_high_output/%s.json" % ID

NODO = {
    "id": ID,
    "titulo": "Llevar la decision al nivel competente mas bajo y templar el conocimiento tecnico con el criterio que dan los golpes",
    "dominio": "gestion_equipos",
    "estado": "vivo",
    "ids_alias": [],
    "nodos_previos": [],
    "nodos_siguientes": [],
    "atribuciones": [],
    "fuentes": [{"clave": "grove_high_output", "fecha": "2026-09-19"}],
    "denominaciones": {
        "nombre_largo": "La segunda caracteristica del modelo ideal: que la decision se trabaje y se alcance en el nivel competente mas bajo, en el terreno intermedio entre el conocimiento tecnico y la experiencia",
        "sigla": "",
        "otros_idiomas": [
            {"idioma": "ingles", "termino": "lowest competent level"},
            {"idioma": "ingles", "termino": "best possible mix of participants"},
            {"idioma": "ingles", "termino": "status differentials"},
        ],
    },
    "condiciones_activacion": "Cuando tienes que decidir quien compone el grupo que va a tomar una decision, y el que mas sabe del asunto y el que tiene mas experiencia de carrera no son la misma persona.",
    "entregable_esperado": "El grupo que decide, compuesto con la mejor mezcla disponible de conocimiento tecnico y de experiencia, trabajando en el nivel competente mas bajo y con las diferencias de rango apartadas durante la discusion libre.",
    "pasos_accionables": [
        "Haz que cualquier decision se trabaje y se alcance en el nivel competente mas bajo.",
        "Cuenta con el motivo que el libro le pone: ahi la toma gente que esta mas cerca de la situacion y que es la que mas sabe de ella.",
        "No entiendas saber como entender tecnicamente y nada mas: esa clase de pericia tiene que templarse con criterio.",
        "Cuenta con que ese criterio se desarrolla con la experiencia y aprendiendo de los muchos errores que uno ha cometido en su carrera.",
        "Situa idealmente la toma de la decision en el terreno intermedio: entre apoyarse en el conocimiento tecnico por un lado, y en los golpes que uno se ha llevado al intentar implantar y aplicar ese conocimiento por el otro.",
        "Si para tomar la decision no encuentras personas que reunan las dos cualidades, busca la mejor mezcla posible de participantes disponibles.",
        "Para poner la experiencia, pide que venga a la reunion una persona de la direccion con rango superior al de los demas miembros del grupo.",
        "Exige que alli todos expresen opiniones y creencias como iguales durante toda la etapa de discusion libre, olvidando o ignorando las diferencias de rango.",
    ],
    "resumen_teorico": (
        "UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_06.md, unidad Cap. 5, titulo textual Decisions, Decisions. "
        "Sale de la PIEZA P9 de la frontera publicada hoy en OO.2.a, L33, 193 palabras, y de ningun otro tramo. "
        "POR QUE ES PROCEDIMIENTO, por la prueba del inventario de EXTRACTOR.md 9.1: el libro no se queda en el mandato con adjetivo, "
        "pone el MEDIO con que se cumple y lo nombra pieza a pieza (the best possible mix of participants available; we at Intel are likely to ask a "
        "person in management senior to the other members of the group to come to the meeting; everybody there voice opinions and beliefs as equals "
        "throughout the free discussion stage, forgetting or ignoring status differentials), y define el terreno donde tiene que caer la decision con "
        "sus dos extremos nombrados (between reliance on technical knowledge on the one hand, and on the bruises one has received). "
        "DE DONDE SALE CADA PASO, uno a uno, todos de L33: paso 1 (Another desirable and important feature of the model is that any decision be worked "
        "out and reached at the lowest competent level); paso 2 (The reason is that this is where it will be made by people who are closest to the "
        "situation and know the most about it); paso 3 (And by know I don't just mean understand technically. That kind of expertise must be tempered "
        "with judgment); paso 4 (which is developed through experience and learning from the many errors one has made in one's career); paso 5 (Thus, "
        "ideally, decision-making should occur in the middle ground, between reliance on technical knowledge on the one hand, and on the bruises one has "
        "received from having tried to implement and apply such knowledge on the other); paso 6 (To make a decision, if you can't find people with both "
        "qualities, you should aim to get the best possible mix of participants available); paso 7 (For experience, we at Intel are likely to ask a person "
        "in management senior to the other members of the group to come to the meeting); paso 8 (But it is very important that everybody there voice "
        "opinions and beliefs as equals throughout the free discussion stage, forgetting or ignoring status differentials). "
        "RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 8 pasos, 8 TRANSCRIPCION, 0 PUENTE. "
        "LOS SITIOS DE TENTACION QUE DECLARO, y en los que NO escribi: NO escribo como se averigua cual es el nivel competente mas bajo, ni que se hace si "
        "dos niveles se declaran competentes, porque el libro pone el criterio y no pone la prueba. NO escribo cuantos participantes componen la mezcla ni "
        "en que proporcion, porque best possible mix no trae numero. NO escribo quien compone el grupo ni quien convoca: el responsable es la tercera "
        "especie de PUENTE que este libro me ha costado, y el texto dice we at Intel are likely to ask sin encargarselo a nadie. NO escribo periodo ninguno. "
        "NI UNA CIFRA A atribuciones: el tramo no trae ninguna. "
        "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO: este nodo va a levantar vecindad con repartir_decision_cercanos_hechos, que es de otro libro y dice "
        "tambien que decidan los mas cercanos a los hechos. Sostengo que son HERMANOS y no gemelos: aquel reparte el poder de decidir y desmonta el ego del "
        "jefe, y este compone el grupo mezclando conocimiento tecnico y experiencia de carrera y manda apartar el rango durante la discusion libre. Si cae, "
        "cae DENTRO de mi marcado."
    ),
}

if os.path.exists(DESTINO):
    raise SystemExit("YA EXISTE: %s" % DESTINO)
io.open(DESTINO, "w", encoding="utf-8", newline="\n").write(
    json.dumps(NODO, ensure_ascii=False, indent=1) + "\n")
print("ESCRITO: %s" % DESTINO)
print("pasos: %d" % len(NODO["pasos_accionables"]))
