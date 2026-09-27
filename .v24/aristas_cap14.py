# -*- coding: utf-8 -*-
"""LAS ARISTAS DE cap_14: LA CABEZA CONTRA SUS TRECE PARTES.

Manual 3.4 (serie numerada: un nodo por paso mas una cabeza) y D.37 (la serie que
el titulo enumera se cablea en la misma vuelta). La tabla se imprime del fichero:
el paso de la cabeza que nombra a cada parte sale de su JSON, no de mi cabeza.
"""
import io
import json
import os

BANDEJA = 'cuarentena/scott_radical_candor'
CABEZA = 'recorrer_trece_elementos_proceso_evaluacion_formal'

# (paso de la cabeza, hijo). El paso 1 es la advertencia de que no hay talla
# unica; los trece elementos van del paso 2 al paso 14, en el orden del libro.
PARTES = [
    (2, 'decidir_poner_nota_comunicar_proposito_limites'),
    (3, 'elegir_categorias_nota_palabras_propias_empresa'),
    (4, 'escribir_escaleras_puesto_evitar_dos_extremos'),
    (5, 'fijar_cuatro_notas_calcular_nota_global'),
    (6, 'elegir_palabras_nota_definirlas_empresa_entera'),
    (7, 'aplicar_consecuencias_nota_apoyar_fuerzas_persona'),
    (8, 'repartir_notas_publicar_reparto_esperado'),
    (9, 'presionar_curva_notas_evitar_forzarla'),
    (10, 'calibrar_notas_reunion_jefes_pares'),
    (11, 'evaluar_desempenio_dos_veces_anio'),
    (12, 'montar_evaluacion_360_grados_ligera_pares'),
    (13, 'hacer_critica_pares_transparente_ensenar_escribirla'),
    (14, 'mantener_proceso_evaluacion_ligero_vigilar_crecimiento'),
]


def cargar(identificador):
    return json.load(io.open(os.path.join(BANDEJA, identificador + '.json'),
                             encoding='utf-8'))


cabeza = cargar(CABEZA)

print('| # | madre | hijo | `--paso` | especie | el paso de la cabeza, impreso del fichero | pasos del hijo |')
print('|---:|---|---|---:|---|---|---:|')
for indice, (paso, hijo_id) in enumerate(PARTES, start=58):
    hijo = cargar(hijo_id)
    print('| %d | `%s` | `%s` | **%d** | `D.37` | `%s` | **%d** |'
          % (indice, CABEZA, hijo_id, paso,
             cabeza['pasos_accionables'][paso - 1], len(hijo['pasos_accionables'])))

# Y LA QUE NO ES DE LA SERIE: el P5 de la pieza que monta el equipo remite a la
# cabeza por lectura, no por numeracion. D.29, con su razon escrita.
print('')
print('| # | madre | hijo | `--paso` | especie | el paso de la madre, impreso del fichero | pasos del hijo |')
print('|---:|---|---|---:|---|---|---:|')
madre = cargar('montar_equipo_gestion_desempenio_revisar_sistema')
print('| 71 | `montar_equipo_gestion_desempenio_revisar_sistema` | `%s` | **5** | `D.29` | `%s` | **%d** |'
      % (CABEZA, madre['pasos_accionables'][4], len(cabeza['pasos_accionables'])))
