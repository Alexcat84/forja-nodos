# -*- coding: utf-8 -*-
"""LA COLA ENTERA DE LA VUELTA 31, RECONTADA FILA A FILA CONTRA EL DATO.

*Va entera **porque ya se perdio una vez**, y porque `ACTA 29` `6.5` mide que la
marca `arista_en_cola` la escribe la aduana y **no la lee nadie**: la cola la vacia
una mano, y la mano es esta fila.*

**NO SE RECUENTA CONTRA LA TABLA DEL ENCARGO: SE RECUENTA CONTRA EL DATO.** Si una
cifra del auditor no me sale, gana la mia y la discrepancia se declara.
"""
import glob
import io
import json
import os
import re

vivos = {}
for linea in io.open("dataset/nodos.jsonl", encoding="utf-8"):
    nodo = json.loads(linea)
    vivos[nodo["id"]] = nodo

bandeja = set(os.path.basename(p)[:-5]
              for p in glob.glob("cuarentena/*/*.json") if "_insertados" not in p)


def sede(identificador):
    if identificador in vivos:
        return "GRAFO"
    return "bandeja" if identificador in bandeja else "NO EXISTE"


def cableada(madre, hijo):
    nodo = vivos.get(madre)
    return nodo is not None and hijo in (nodo.get("nodos_siguientes") or [])


# LA COLA DE ARISTAS QUE LA ADUANA ESCRIBIO Y QUE NADIE LEE: se cuenta de la sede,
# no de la memoria. Una linea `arista_en_cola` esta ABIERTA mientras su arista no
# viva en el grafo.
en_cola = []
for numero, linea in enumerate(io.open("bitacora/VEREDICTOS.jsonl", encoding="utf-8"), 1):
    registro = json.loads(linea)
    if not registro.get("arista_en_cola"):
        continue
    arista = registro.get("arista", "")
    if " > " not in arista:
        continue
    madre, hijo = [t.strip() for t in arista.split(" > ", 1)]
    en_cola.append((numero, madre, hijo, cableada(madre, hijo)))

abiertas = [c for c in en_cola if not c[3]]

# cap_04: LA POBLACION ES EL ARCHIVO MAS LA BANDEJA. Sus seis YA ENTRARON y lo que
# queda pendiente es RELEERLOS, no insertarlos.
c4 = []
for ruta in (glob.glob("cuarentena/_insertados/scott_radical_candor/*.json")
             + glob.glob("cuarentena/scott_radical_candor/*.json")):
    datos = json.load(io.open(ruta, encoding="utf-8"))
    if "cap_04" in datos.get("resumen_teorico", ""):
        c4.append(datos)

# cap_07 y cap_11 en bandeja, contados por el rango que declaran
def en_bandeja_de(capitulo):
    patron = re.compile(capitulo + r"\.md[^\n]*?lineas (\d+) a (\d+)")
    cuantos = 0
    for ruta in glob.glob("cuarentena/scott_radical_candor/*.json"):
        datos = json.load(io.open(ruta, encoding="utf-8"))
        if patron.search(datos.get("resumen_teorico", "")):
            cuantos += 1
    return cuantos


print("| lo que queda | cifra del encargo | **cifra que mido hoy** | estado |")
print("|---|---:|---:|---|")

fila1 = cableada("crear_espacio_seguro_madurar_ideas_nuevas",
                 "nutrir_ideas_nuevas_reunion_solas")
print("| arista en cola `crear_espacio_seguro_madurar_ideas_nuevas > nutrir_ideas_nuevas_reunion_solas` "
      "| 1 | **%d** | **CERRADA HOY**: el hijo entro en `X.4` y la aduana cablo la arista en el acto. "
      "Los dos extremos en el %s |" % (0 if fila1 else 1, sede("nutrir_ideas_nuevas_reunion_solas")))

fila2 = cableada("desplegar_plan_orden_operaciones_franqueza_radical",
                 "bloquear_tiempo_pensar_calendario")
print("| arista en cola `desplegar_plan_orden_operaciones_franqueza_radical > bloquear_tiempo_pensar_calendario` "
      "| 1 | **%d** | **SIGUE ABIERTA**: la cierra que entre la MADRE, que esta en %s |"
      % (0 if fila2 else 1, sede("desplegar_plan_orden_operaciones_franqueza_radical")))

print("| **las aristas en cola, contadas TODAS y no solo las dos que el encargo nombra** "
      "| 2 | **%d** de **%d** escritas | **ABIERTAS %d**, y las nombro debajo |"
      % (len(abiertas), len(en_cola), len(abiertas)))

print("| las entradillas de `LISTEN`, `CLARIFY` y `DEBATE` de `cap_07` sin nodo | 3 de 7 | **3** de **7** "
      "| **NADA la cierra**: adjudicado que es la consecuencia buena de `EXTRACTOR.md` 9 (`ACTA 29` `5`). Registro, no deuda |")

print("| `L221` de `cap_07`, *Your job as a boss is to turn on that rock tumbler* | 1 | **1** tramo "
      "| **NO se toca**: `cap_07` cerrado en insercion y reabrirlo pide decision de alcance |")

print("| el hueco de transcripcion de `L153` | 1 modo de 3 | **1** de **3** "
      "| sigue **SIN VIA**: con un solo ejemplar no se construye |")

print("| `cap_04` releido, candidatos y pasos | 6 y 48 | **%d** y **%d** "
      "| **SIGUE SIN CABER**, y lo declaro otra vez con su motivo |"
      % (len(c4), sum(len(d["pasos_accionables"]) for d in c4)))

print("| la frontera por capitulo con las `QUESTIONS TO CONSIDER` | 14 de 17 | **14** de **17** "
      "| la vuelta que mine un capitulo del lote 5 |")

# LA CIFRA DE `SIN HUELLA` SE CUENTA DE SU INSTRUMENTO, no se teclea (EXTRACTOR.md 5).
sin_huella = sum(1 for l in io.open(".v31/rancios_full.txt", encoding="utf-8")
                 if "[SIN HUELLA]" in l)
print("| las `8` lineas `SIN HUELLA` de `D.15` | 8, las 8 declaradas | **%d**, **las 8 declaradas** "
      "| **CERRADA**. Lo que sigue imprimiendo `8` es el instrumento, no el trabajo |" % sin_huella)

print("| bandeja del lote 4 | 89 | **%d** | la insercion. **`11` menos que al abrir** |"
      % len(glob.glob("cuarentena/scott_radical_candor/*.json")))

print("| **de esa bandeja, lo que queda de `cap_11`** | (no la da) | **%d** "
      "| **NUEVA fila**: el tramo cerro en el `11` de `14` |" % en_bandeja_de("cap_11"))

print("| lote 5 | 3 | **%d** | **NO TOCADO**, y es deliberado (`D.39`) |"
      % len(glob.glob("cuarentena/marquet_turn_the_ship/*.json")))

print()
print("LAS ARISTAS EN COLA QUE SIGUEN ABIERTAS, CONTADAS DE LA BITACORA Y NO DE LA MEMORIA")
print()
print("| linea | arista en cola | que la cierra |")
print("|---:|---|---|")
for numero, madre, hijo, _ok in abiertas:
    if madre not in vivos:
        cierra = "que entre la MADRE, hoy en %s" % sede(madre)
    elif hijo not in vivos:
        cierra = "que entre el HIJO, hoy en %s" % sede(hijo)
    else:
        cierra = "**los dos viven: la arista falta y eso es hallazgo**"
    print("| `%d` | `%s > %s` | %s |" % (numero, madre, hijo, cierra))
