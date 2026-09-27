# -*- coding: utf-8 -*-
"""CANDIDATO 9 DE LA VUELTA 53: cap_07 P5, L19, LOS TRES PASOS DEL PROCESO DE PLANIFICACION.

Se escribe y se pasa por la aduana EN EL MISMO ACTO (EXTRACTOR.md 16).
"""
import io
import json
import os

ID = "planificar_tres_pasos_demanda_estado_brecha"
DESTINO = "cuarentena/grove_high_output/%s.json" % ID

NODO = {
    "id": ID,
    "titulo": "Planificar en los tres pasos del libro: la demanda del entorno, el estado presente, y lo que hay que hacer para conciliarlos",
    "dominio": "gestion_equipos",
    "estado": "vivo",
    "ids_alias": [],
    "nodos_previos": [],
    "nodos_siguientes": [],
    "atribuciones": [],
    "fuentes": [{"clave": "grove_high_output", "fecha": "2026-09-19"}],
    "denominaciones": {
        "nombre_largo": "El proceso general de planificacion con sus tres pasos contados y nombrados: establecer la necesidad o demanda proyectada, establecer el estado presente, y comparar y conciliar los dos",
        "sigla": "",
        "otros_idiomas": [
            {"idioma": "ingles", "termino": "environmental demand"},
            {"idioma": "ingles", "termino": "present status"},
        ],
    },
    "condiciones_activacion": "Cuando tienes que planificar el trabajo de tu grupo y no sabes por donde empezar, o cuando lo que llamas plan es una lista de intenciones y no una comparacion entre lo que te van a pedir y lo que vas a producir.",
    "entregable_esperado": "Los tres pasos contestados por escrito: lo que el entorno va a demandar de ti, lo que vas a producir si no cambias nada, y lo que tienes que hacer de mas o de menos para que lo segundo cubra lo primero.",
    "pasos_accionables": [
        "Monta tu proceso general de planificacion sobre un razonamiento analogo al de la fabrica, y no sobre otra cosa.",
        "Da el paso 1 estableciendo la necesidad o demanda proyectada: que va a demandar de ti el entorno, de tu negocio o de tu organizacion.",
        "Da el paso 2 estableciendo tu estado presente: que estas produciendo ahora, y que vas a estar produciendo cuando se completen los proyectos que ya tienes en marcha.",
        "Formula ese paso 2 tambien de la otra manera, que es la que obliga a contestarlo: donde va a estar tu negocio si no haces nada distinto de lo que estas haciendo.",
        "Da el paso 3 comparando y conciliando los pasos 1 y 2.",
        "Convierte esa conciliacion en la pregunta concreta: que mas, o que menos, necesitas hacer para producir lo que tu entorno va a demandar.",
    ],
    "resumen_teorico": (
        "UNIDAD DE ORIGEN: fuentes/grove_high_output/cap_07.md, unidad Cap. 6, titulo textual de la planificacion como accion de hoy para la salida de manana. "
        "Sale de la PIEZA P5 de la frontera publicada hoy en OO.2.b, L19, 103 palabras, y de ningun otro tramo. "
        "POR QUE ES PROCEDIMIENTO Y ADEMAS CABEZA, por la prueba del inventario de EXTRACTOR.md 9.1 y por la vara de D.37: el libro DICE CUANTOS PASOS SON "
        "numerandolos el mismo (Step 1 is to establish projected need or demand; Step 2 is to establish your present status; Step 3 is to compare and "
        "reconcile steps 1 and 2) y pone bajo cada uno la pregunta que hay que contestar. Inventario de ETAPAS, no de fines. "
        "POR QUE NO CABLEO NINGUNA ARISTA DE D.37 HOY: las partes de esta cabeza son las piezas P8, P9, P10, P12 y P14 de la misma frontera, que son las "
        "secciones STEP 1, STEP 2 y STEP 3 del propio capitulo, y NINGUNA DE ELLAS EXISTE TODAVIA COMO NODO: el reloj de aduana de esta vuelta cerro antes. "
        "D.37 pide que las partes existan, y lo que hago en su lugar es dejar la arista ANUNCIADA aqui y en el reporte para la vuelta que escriba esas "
        "piezas, que es la que tiene que cablearla en su mismo acto. "
        "POR QUE P4 (L17) NO ES NODO Y ESTE SI, que es la frontera que mas me jugaba en este capitulo: L17 recapitula los tres pasos EN LA FABRICA y lo "
        "declara el mismo (As we learned in Chapter 2), y L19 los generaliza (Your general planning process should consist of analogous thinking). Dar nodo "
        "a los dos fabricaria el gemelo de su propio donante, que es lo que P.19 prohibe, asi que el nodo se queda en la version general, que es la que el "
        "libro despliega en el resto del capitulo. "
        "DE DONDE SALE CADA PASO, uno a uno, todos de L19: paso 1 (Your general planning process should consist of analogous thinking); paso 2 (Step 1 is to "
        "establish projected need or demand: What will the environment demand from you, your business, or your organization?); paso 3 (Step 2 is to establish "
        "your present status: What are you producing now? What will you be producing as your projects in the pipeline are completed?); paso 4 (Put another "
        "way, where will your business be if you do nothing different from what you are now doing?); paso 5 (Step 3 is to compare and reconcile steps 1 and "
        "2); paso 6 (Namely, what more or less do you need to do to produce what your environment will demand?). "
        "RELECTURA DE FIDELIDAD D.30 EN EL ACTO: 6 pasos, 6 TRANSCRIPCION, 0 PUENTE. "
        "LOS SITIOS DE TENTACION QUE DECLARO, y en los que NO escribi: NO escribo COMO se establece la demanda del entorno ni COMO se determina el estado "
        "presente, porque eso lo despliega el propio capitulo en sus piezas siguientes y meterlo aqui seria comprimir dos veces la misma numeracion, que es "
        "lo que el manual 3.4 prohibe. NO escribo cada cuanto se repite el ciclo: el periodo es la segunda especie de PUENTE del lote 1, y ademas vive en "
        "P22, que es su propio nodo. NO escribo quien planifica: el responsable es la tercera especie, y ademas el libro lo trata aparte en P23. "
        "NI UNA CIFRA A atribuciones: el tramo no trae ninguna. "
        "DISCUTIBLE QUE MARCO ANTES DE SABER SI ACIERTO: una cabeza de tres pasos cuyos pasos son las tres secciones siguientes del capitulo puede leerse "
        "como un indice y no como un procedimiento. Lo sostengo porque el libro no se limita a anunciarlos: pone la pregunta que cada paso contesta y cierra "
        "el paso 3 con la comparacion que produce la salida del proceso. Si cae, cae DENTRO de mi marcado."
    ),
}

if os.path.exists(DESTINO):
    raise SystemExit("YA EXISTE: %s" % DESTINO)
io.open(DESTINO, "w", encoding="utf-8", newline="\n").write(
    json.dumps(NODO, ensure_ascii=False, indent=1) + "\n")
print("ESCRITO: %s" % DESTINO)
print("pasos: %d" % len(NODO["pasos_accionables"]))
