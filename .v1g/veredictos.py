# -*- coding: utf-8 -*-
"""LOS VEREDICTOS DE LOS OCHO PARES QUE LA ADUANA LEVANTO, CON SUS TRES SENALES PEGADAS.

**LAS SENALES LAS PEGA LA MAQUINA** de mis propios informes (`.v1g/informe_NN.txt`); **el
veredicto y su razon los pongo yo leyendo al vecino**, que es lo que `EXTRACTOR.md` 2 manda
cuando la aduana bloquea y lo que el manual llama principio 4: las senales ordenan, nunca
deciden.

**ESTOS VEREDICTOS NO VAN HOY A `bitacora/VEREDICTOS.jsonl`**: esa sede la escribe la aduana con
`insertar`, y este frente NO inserta (`D.45`). Viajan en el reporte y se escriben el dia de la
insercion.

El instrumento **revienta si un par que yo juzgo no esta en el informe**, asi que no puedo
juzgar un par que la aduana no levanto, ni dejar sin juzgar uno que si.
"""
import io
import os
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

INFORMES = ["informe_01.txt", "informe_02b.txt", "informe_03.txt", "informe_04.txt",
            "informe_05.txt", "informe_06.txt", "informe_07.txt", "informe_08.txt"]

BLOQUE = re.compile(r"^\[(?:BLOQUEARIA|ENTRARIA|CAERIA)\]\s+(\S+)", re.M)
PAR = re.compile(r"^\s+vecino (\S+)\s+\[levantada por: ([^\]]+)\]\s*\n"
                 r"\s+similitud_texto ([\d.]+) \| familia_id ([\d.]+) \| paso_contra_nodo ([\d.]+)\s*\n"
                 r"\s+paso (\d+) del candidato contra paso (\d+) de (\S+)", re.M)

# LO QUE LEE LA MAQUINA: (candidato, vecino) -> senales
medidos = {}
for fichero in INFORMES:
    ruta = os.path.join(".v1g", fichero)
    texto = io.open(ruta, encoding="utf-8").read()
    candidato = BLOQUE.search(texto)
    if not candidato:
        raise SystemExit("EL INFORME %s NO TRAE SU VEREDICTO DE PUERTA" % ruta)
    for vecino, senal, s1, s2, s3, pc, pv, _otro in PAR.findall(texto):
        medidos[(candidato.group(1), vecino)] = (senal.strip(), s1, s2, s3, pc, pv, fichero)

# LO QUE PONGO YO LEYENDO: (candidato, vecino, veredicto, razon)
SANO = "**SANO**"
MIOS = [
    ("construir_flujo_produccion_paso_limitante", "retirar_barreras_politicas_metodo", SANO,
     "AJENOS, y el par es instructivo contra mi: el vecino es de `smart_who` y trata de quitar "
     "politicas que estorban a un metodo de contratacion. Lei sus cinco pasos. Lo unico que "
     "comparte con mi paso 4 es LA FORMULA CON LA QUE YO ESCRIBO: `que es por donde el libro dice "
     "que se empieza` contra `que es con quien el libro dice que se hace esto`. La senal 3 midio mi "
     "manera de escribir, no el contenido del procedimiento"),
    ("rehacer_flujo_paso_limitante_capacidad", "construir_flujo_produccion_paso_limitante", SANO,
     "HERMANOS EN SECUENCIA, y es el par que yo marque como discutible ANTES de que la aduana lo "
     "levantara. Uno construye el flujo la primera vez y el otro lo rehace cuando una capacidad "
     "limitada mueve el paso que manda. La senal que lo levanta es `familia_id`, que mide que "
     "comparten `flujo` y `paso_limitante` en el id: es exactamente la banda que `D.4` midio como "
     "ruido de jerarquia. **Y de este par sale una arista declarada por lectura** (`D.29`), no un "
     "gemelo"),
    ("construir_flujo_produccion_paso_limitante", "rehacer_flujo_paso_limitante_capacidad", SANO,
     "EL MISMO PAR DE LA FILA DE ARRIBA, VISTO DESDE LA OTRA PUNTA: aparece porque el informe de "
     "este candidato se volvio a correr DESPUES de la correccion de fidelidad, cuando su hermano ya "
     "estaba en la bandeja. La senal cruza ahora su paso 9 contra el paso 5 del otro, que son los "
     "dos pasos de los desfases, y es exactamente el par del que sale la arista 1 de Z.4. **Mismo "
     "veredicto y misma razon: hermanos en secuencia, no gemelos**"),
    ("preferir_inspeccion_proceso_prueba_destructiva", "clasificar_trabajo_proceso_montaje_prueba", SANO,
     "MADRE E HIJO, no gemelos: el paso 3 de la madre nombra la prueba y este despliega QUE CLASE "
     "de prueba se elige. **Tambien sale arista declarada** (`D.29`). El par que la senal cruza es "
     "mi paso 6 contra su paso 7, y los dos dicen `antes de` con sujetos distintos: uno elige "
     "prueba, el otro manda probar el sistema completo antes de enviar"),
    ("preferir_inspeccion_proceso_prueba_destructiva", "equilibrar_capacidad_personal_inventario_plazo", SANO,
     "AJENOS de procedimiento y vecinos de vocabulario: los dos enumeran salidas y les apuntan el "
     "coste, y los dos empiezan sus pasos con `Considera`. Uno decide COMO VIGILAR una operacion "
     "continua y el otro decide COMO DESPLEGAR recursos cuando dos pasos chocan. Ni un objeto de "
     "trabajo en comun"),
    ("dimensionar_inventario_materia_prima_reposicion", "preferir_inspeccion_proceso_prueba_destructiva", SANO,
     "**EL PAR QUE LEO PRIMERO, porque es el unico por encima de `0,4`** y `EXTRACTOR.md` 11 dice "
     "que en esa banda son gemelos y nada mas. Lo leo entero y NO lo son: salen de dos lineas "
     "consecutivas sobre la misma maquina de huevos (`L67` y `L69`), y de ahi el vocabulario "
     "compartido. Uno elige el TIPO DE PRUEBA sobre el producto que sale, y el otro INSPECCIONA EL "
     "MATERIAL QUE ENTRA y dimensiona el inventario que evita el parado. Sus condiciones de "
     "activacion no se solapan y ni un paso de uno cabe en el otro. **Es el caso del capitulo "
     "monotematico de `EXTRACTOR.md` 12, no un duplicado, y va marcado como mi discutible 1**"),
    ("dimensionar_inventario_materia_prima_reposicion", "equilibrar_capacidad_personal_inventario_plazo", SANO,
     "AJENOS, y por la misma via que el par 5 de esta tabla: los dos pesan un coste contra otro, y de "
     "ahi el vocabulario. Uno decide CUANTO MATERIAL guardar contra lo que cuesta guardarlo, y el otro "
     "decide COMO REPARTIR capacidad, personal e inventario cuando dos pasos chocan. El inventario "
     "aparece en los dos porque el libro lo nombra en los dos tramos, pero en uno es materia prima que "
     "entra y en el otro producto terminado que se acumula a proposito"),
    ("detectar_arreglar_fallo_etapa_menor_valor", "construir_flujo_produccion_paso_limitante", SANO,
     "AJENOS: la senal cruza mi paso 3 (la regla de la etapa de menor valor) contra su paso 4 "
     "(mirar el flujo de produccion), y lo que comparten es la palabra `proceso` y la forma de "
     "citar al libro. Uno ordena las etapas por VALOR y el otro las ordena por TIEMPO"),
    ("detectar_arreglar_fallo_etapa_menor_valor", "rehacer_flujo_paso_limitante_capacidad", SANO,
     "AJENOS: mi paso 4 rechaza material en la entrega y su paso 6 dice que el huevo sigue mandando "
     "la calidad. Los dos hablan del mismo caso del libro, que es de donde viene la similitud"),
]

no_medidos = [(c, v) for c, v, _x, _y in MIOS if (c, v) not in medidos]
if no_medidos:
    raise SystemExit("JUZGO PARES QUE LA ADUANA NO LEVANTO: %s" % no_medidos)
sin_juzgar = [par for par in medidos if par not in [(c, v) for c, v, _x, _y in MIOS]]
if sin_juzgar:
    raise SystemExit("PARES LEVANTADOS Y SIN JUZGAR: %s" % sin_juzgar)

print("| # | candidato | vecino | la levanto | similitud | familia | paso contra nodo | pasos cruzados | veredicto y razon |")
print("|---:|---|---|---|---:|---:|---:|---|---|")
for numero, (candidato, vecino, veredicto, razon) in enumerate(MIOS, 1):
    senal, s1, s2, s3, pc, pv, _fichero = medidos[(candidato, vecino)]
    print("| %d | `%s` | `%s` | `%s` | %s | %s | %s | `%s` contra `%s` | %s, %s |"
          % (numero, candidato, vecino, senal,
             s1.replace(".", ","), s2.replace(".", ","), s3.replace(".", ","),
             pc, pv, veredicto, razon))
print("")
print("PARES LEVANTADOS POR LA ADUANA : %d" % len(medidos))
print("PARES JUZGADOS POR MI LECTURA  : %d" % len(MIOS))
print("SANO                           : %d" % sum(1 for m in MIOS if m[2] == SANO))
print("POR ENCIMA DE 0,4 EN SIMILITUD : %d"
      % sum(1 for c, v, _x, _y in MIOS if float(medidos[(c, v)][1]) > 0.4))
print("ESCRITOS EN bitacora/          : 0   (este frente no inserta: D.45)")
