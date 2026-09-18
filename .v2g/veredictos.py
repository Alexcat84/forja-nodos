# -*- coding: utf-8 -*-
"""LOS VEREDICTOS DE LOS PARES QUE LA ADUANA LEVANTO, CON SUS TRES SENALES PEGADAS.

LAS SENALES LAS PEGA LA MAQUINA de mis propios informes (.v2g/informe_<id>.txt); EL
VEREDICTO Y SU RAZON LOS PONGO YO LEYENDO AL VECINO, que es lo que EXTRACTOR.md 2 manda
cuando la aduana bloquea y lo que el manual llama principio 4: las senales ordenan, nunca
deciden.

ESTOS VEREDICTOS NO VAN HOY A bitacora/VEREDICTOS.jsonl: esa sede la escribe la aduana con
insertar, y este frente NO inserta (D.45). Viajan en el reporte y se escriben el dia de la
insercion.

El instrumento REVIENTA si juzgo un par que la aduana no levanto, o si dejo sin juzgar uno
que si, asi que la tabla no puede tener ni una fila de mas ni una de menos.
"""
import io
import os
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

BLOQUE = re.compile(r"^\[(?:BLOQUEARIA|ENTRARIA|CAERIA)\]\s+(\S+)", re.M)
PAR = re.compile(r"^\s+vecino (\S+)\s+\[levantada por: ([^\]]+)\]\s*\n"
                 r"\s+similitud_texto ([\d.]+) \| familia_id ([\d.]+) \| paso_contra_nodo ([\d.]+)\s*\n"
                 r"\s+paso (\d+) del candidato contra paso (\d+) de (\S+)", re.M)

medidos = {}
for fichero in sorted(os.listdir(".v2g")):
    if not fichero.startswith("informe_") or not fichero.endswith(".txt"):
        continue
    if fichero.startswith("informe_lote") or fichero in ("informe_01.txt", "informe_02.txt"):
        continue
    texto = io.open(os.path.join(".v2g", fichero), encoding="utf-8").read()
    cabeza = BLOQUE.search(texto)
    if not cabeza:
        raise SystemExit("EL INFORME %s NO TRAE SU VEREDICTO DE PUERTA" % fichero)
    for vecino, senal, s1, s2, s3, pc, pv, _otro in PAR.findall(texto):
        medidos[(cabeza.group(1), vecino)] = (senal.strip(), s1, s2, s3, pc, pv, fichero)

SANO = "**SANO**"
CONTINUA = "**CONTINUA**"

MIOS = [
    ("emparejar_indicadores_efecto_contraefecto", "revisar_tres_preguntas_valor_carrera", SANO,
     "AJENOS. Lei los siete pasos del vecino: son las tres preguntas con las que te examinas a ti "
     "mismo en la carrera, de `cap_01`, y no tocan ni un indicador. Lo unico que comparten con mi "
     "nodo es EL ARMAZON CON EL QUE YO ESCRIBO el `resumen_teorico`. Medido: quitando el resumen, "
     "la senal 1 de este par cae de `0,354` a `0,225`, o sea por debajo del umbral"),
    ("elegir_indicador_salida_trabajo_administrativo", "evaluar_directivo_resultados_fortaleza", SANO,
     "EL UNICO PAR DE MI TANDA CON UNA COINCIDENCIA DE VERDAD, y el unico levantado por la senal 3 "
     "(`0,766`, la mas alta de las 12). Mi paso 2 dice medir al vendedor por los pedidos que "
     "consigue y no por las visitas que hace; el paso 1 del vecino dice lo mismo con las mismas "
     "piezas. NO son gemelos: el vecino es de `zhuo_manager` y su procedimiento es juzgar a un "
     "directivo por resultados y fortaleza del equipo, con nueve pasos que no tienen nada que ver "
     "con elegir el indicador de una unidad administrativa. Lo que comparten es UNA MAXIMA, no un "
     "procedimiento. Y ese par es la prueba al reves de lo que digo en las otras filas: aqui, "
     "quitando el resumen, la senal 1 SUBE de `0,184` a `0,267`, porque la coincidencia esta en los "
     "PASOS y mi armazon la estaba diluyendo"),
    ("elegir_indicador_salida_trabajo_administrativo", "emparejar_indicadores_efecto_contraefecto",
     CONTINUA,
     "ESTE ES EL PAR QUE ME HACE CORREGIR LO QUE YA HABIA PUBLICADO EN `AA.4`, y la correccion va "
     "declarada y sin borrar nada (`P.17`). Alli lo rechace como hermanos. La aduana me mando "
     "releer, y releyendo encontre la linea que no habia pesado: `L35` abre la seccion "
     "administrativa diciendo `Nowhere can indicators-and paired indicators-be of more help than in "
     "administrative work`, o sea que **usa `paired indicators` como concepto YA INTRODUCIDO**, que "
     "es el de `L31`. Mi paso 5 nombra emparejar en una linea y el vecino lo despliega en siete "
     "pasos. Es `D.29` con su linea, y la arista se anade en `AA.5.c`. Que la pareja concreta sea "
     "de calidad aqui y de contraefecto alli es diferencia del EJEMPLO, no del procedimiento que el "
     "paso nombra"),
    ("construir_indicador_tendencia_patron", "construir_grafico_escalonado_pronosticos", SANO,
     "HERMANOS QUE EL LIBRO CONTRASTA EL MISMO, y por eso cae mi propia marca previa. En la ficha "
     "del grafico escalonado yo habia escrito que si la aduana los levantaba mi veredicto seria "
     "`CONTINUA`. La aduana los levanto y la relectura dice `SANO`: `L91` los pone uno frente a "
     "otro con todas las letras, `which can help you anticipate future trends better than if you "
     "used a simple trend chart`. Mejor QUE, no parte DE. `EXTRACTOR.md` 15.6: un vecino que no es "
     "una de las partes de la cabeza es un hermano, y su veredicto es `SANO`. **CAIDA DENTRO DE MI "
     "PROPIO MARCADO**"),
    ("construir_indicador_tendencia_patron", "archivar_indicadores_resolver_problemas", SANO,
     "AJENOS DE OBJETO Y DE DISPARADOR. El de tendencia se monta para mirar hacia delante y se lee "
     "de continuo; el del archivo se usa el dia que algo se rompe. Ni un paso del uno aparece en el "
     "otro. Quitando el resumen, la senal 1 cae de `0,384` a `0,289`"),
    ("construir_indicador_tendencia_patron", "equilibrar_capacidad_personal_inventario_plazo", SANO,
     "AJENOS, y este es el par mas instructivo contra mi manera de escribir: el vecino es de "
     "`cap_02` y trata de intercambiar equipo, personal e inventario contra el plazo. Lo que la "
     "senal esta viendo es que sus pasos empiezan por `Considera` y `apunta su coste` y los mios "
     "por `Pon` y `Mide`, mas el armazon del resumen. Quitando el resumen cae de `0,352` a `0,232`"),
    ("construir_grafico_escalonado_pronosticos", "elegir_fabricar_pedido_pronostico", SANO,
     "AJENOS EN PROCEDIMIENTO, y comparten la palabra `pronostico` porque el capitulo entero habla "
     "de pronosticar: uno elige COMO se controla la salida de una fabrica y el otro monta UN "
     "GRAFICO. **Pero releer este par me encontro una arista que yo no habia visto**, y no es con "
     "este vecino sino con otro: `L121` dice `It is a good idea to use stagger charts in both the "
     "manufacturing and sales forecasts. As noted...`, y ese `As noted` remite a `L91`. La arista "
     "va en `AA.5.c` y el veredicto de ESTE par sigue siendo `SANO`"),
    ("construir_grafico_escalonado_pronosticos", "emparejar_indicadores_efecto_contraefecto", SANO,
     "AJENOS. Montar un grafico escalonado de pronosticos y emparejar un indicador con su "
     "contraefecto no comparten ni objeto ni disparador ni entregable. Es la senal 1 leyendo mi "
     "armazon: quitando el resumen cae de `0,363` a `0,291`"),
    ("archivar_indicadores_resolver_problemas", "revisar_tres_preguntas_valor_carrera", SANO,
     "AJENOS, Y ES LA CAIDA MAS GRANDE DE LAS NUEVE. Guardar el historico de los indicadores de una "
     "operacion no tiene nada que ver con las tres preguntas con las que te examinas la carrera. "
     "Quitando el resumen, la senal 1 cae de `0,369` a `0,179`, **medio punto de umbral de "
     "distancia**, que es la medida mas limpia de que aqui no habia nada que leer"),
]

juzgados = set((a, b) for a, b, _v, _r in MIOS)
levantados = set(medidos)
if juzgados - levantados:
    print("JUZGO UN PAR QUE LA ADUANA NO LEVANTO, NO SE PUBLICA:")
    for par in sorted(juzgados - levantados):
        print("  %s con %s" % par)
    raise SystemExit(1)
sin_juzgar = set()
for (candidato, vecino) in levantados:
    if (candidato, vecino) not in juzgados and (vecino, candidato) not in juzgados:
        sin_juzgar.add((candidato, vecino))
if sin_juzgar:
    print("LA ADUANA LEVANTO UN PAR QUE NO JUZGO, NO SE PUBLICA:")
    for par in sorted(sin_juzgar):
        print("  %s con %s" % par)
    raise SystemExit(1)

print("| # | candidato | vecino | senal que lo levanta | las tres senales, pegadas | el paso contra el paso | veredicto | la razon, leida |")
print("|---:|---|---|---|---|---|---|---|")
for numero, (candidato, vecino, veredicto, razon) in enumerate(MIOS, 1):
    senal, s1, s2, s3, pc, pv, _f = medidos[(candidato, vecino)]
    print("| %d | `%s` | `%s` | `%s` | similitud `%s`, familia `%s`, paso contra nodo `%s` | paso `%s` del candidato contra paso `%s` del vecino | %s | %s |"
          % (numero, candidato, vecino, senal,
             s1.replace(".", ","), s2.replace(".", ","), s3.replace(".", ","),
             pc, pv, veredicto, razon))
print("")
print("PARES LEVANTADOS POR LA ADUANA, contando los dos sentidos : %d" % len(medidos))
print("PARES DISTINTOS, que son los que se juzgan               : %d" % len(MIOS))
print("  SANO                                                   : %d"
      % sum(1 for m in MIOS if m[2] == SANO))
print("  CONTINUA                                               : %d"
      % sum(1 for m in MIOS if m[2] == CONTINUA))
print("ESCRITOS EN bitacora/VEREDICTOS.jsonl HOY                : 0   (D.45: este frente no inserta)")
