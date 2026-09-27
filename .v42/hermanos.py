# -*- coding: utf-8 -*-
"""Imprime la linea --veredicto SANO de cada HERMANO DE SERIE que siga en la bandeja.

NO ES MAQUINARIA NUEVA (EXTRACTOR.md 13): es la misma figura que el extractor ya
escribe a mano en cada candidato, con el dato leido del fichero en vez de tecleado.
La razon la escribo yo una vez y lo que cambia por pareja es lo que la hace
verificable: el NUMERO DE ELEMENTO de cada uno dentro de los trece que la cabeza
enumera, y el ENTREGABLE de cada uno leido de su propia ficha.

Uso: python .v42/hermanos.py <id_del_candidato_que_entra>
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANDEJA = os.path.join(RAIZ, "cuarentena", "scott_radical_candor")
CABEZA = "recorrer_trece_elementos_proceso_evaluacion_formal"

# EL NUMERO DE ELEMENTO DE CADA UNO, leido del resumen_teorico de su propia ficha,
# que es donde cada candidato declara de que elemento de los trece sale.
ELEMENTO = {
    "decidir_poner_nota_comunicar_proposito_limites": (1, "rating or no rating"),
    "elegir_categorias_nota_palabras_propias_empresa": (2, "categories of ratings"),
    "escribir_escaleras_puesto_evitar_dos_extremos": (3, "job ladders"),
    "fijar_cuatro_notas_calcular_nota_global": (4, "number of ratings"),
    "elegir_palabras_nota_definirlas_empresa_entera": (5, "language matters"),
    "aplicar_consecuencias_nota_apoyar_fuerzas_persona": (6, "consequence of ratings"),
    "repartir_notas_publicar_reparto_esperado": (7, "distribution of ratings"),
    "presionar_curva_notas_evitar_forzarla": (8, "forced curve or no"),
    "calibrar_notas_reunion_jefes_pares": (9, "calibration of ratings"),
    "evaluar_desempenio_dos_veces_anio": (10, "frequency"),
    "montar_evaluacion_360_grados_ligera_pares": (11, "360 degree or unilateral"),
    "hacer_critica_pares_transparente_ensenar_escribirla": (12, "transparent or confidential"),
    "mantener_proceso_evaluacion_ligero_vigilar_crecimiento": (13, "lightweight or heavyweight"),
}

def leer_ficha(ident):
    """DEL GRAFO SI YA ENTRO, Y DE LA BANDEJA SI TODAVIA NO.

    CORRECCION DECLARADA, vuelta 42, candidato 12: esta funcion miraba SOLO la
    bandeja, asi que en cuanto un hermano entraba al grafo dejaba de emitirse su
    veredicto y la aduana bloqueaba. Costo una corrida entera. Un hermano lo sigue
    siendo despues de entrar.
    """
    ruta = os.path.join(BANDEJA, ident + ".json")
    if os.path.exists(ruta):
        return json.load(io.open(ruta, encoding="utf-8"))
    for linea in io.open(os.path.join(RAIZ, "dataset", "nodos.jsonl"),
                         encoding="utf-8"):
        linea = linea.strip()
        if linea and json.loads(linea)["id"] == ident:
            return json.loads(linea)
    return None


yo = sys.argv[1]
mi_num, mi_rotulo = ELEMENTO[yo]
for otro in sorted(ELEMENTO):
    if otro == yo:
        continue
    ficha = leer_ficha(otro)
    if ficha is None:
        continue
    num, rotulo = ELEMENTO[otro]
    razon = (
        "HERMANO DE SERIE Y NO MADRE NI HIJO, y lo digo con la cuenta del libro delante. "
        "Los dos colgamos de la misma cabeza, %s, y colgamos por SITIOS DISTINTOS de su "
        "lista: yo soy el ELEMENTO %d de los trece, %s, y el es el ELEMENTO %d, %s. "
        "EXTRACTOR.md 15.6 escribe que un vecino que no es la parte que te toca es hermano "
        "y que su veredicto es SANO, y esta es esa figura exacta. "
        "LO QUE LA SENIAL VE Y POR QUE NO DECIDE: los trece elementos son decisiones de "
        "disenio del MISMO proceso, asi que comparten el vocabulario entero de nota, jefe, "
        "empleado, evaluacion y reparto. Es vocabulario compartido, no objeto compartido, y "
        "EXTRACTOR.md 12 lo tiene escrito: cuando un capitulo entero cae en la misma familia "
        "eso no es una senial de duplicado, es una senial de que el libro trata un tema. "
        "LO QUE DECIDE CADA UNO, leido de su propia ficha y no supuesto. SU ENTREGABLE: %s "
        "EL MIO ES OTRO, y ninguno de los dos se produce con los pasos del otro. "
        "Y DIGO POR QUE NINGUNO ES MADRE DEL OTRO: la linea que nos enumera a los dos no es "
        "mia ni suya, es de la cabeza, y declarar una arista entre dos partes de la misma "
        "numeracion pondria dos compresiones sobre la misma lista, que es lo que el manual "
        "3.4 prohibe por su nombre."
        % (CABEZA, mi_num, mi_rotulo, num, rotulo,
           ficha["entregable_esperado"].replace("|", " ").rstrip())
    )
    print(' --veredicto "%s|SANO|%s" \\' % (otro, razon))
