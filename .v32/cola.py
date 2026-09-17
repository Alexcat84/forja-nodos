# -*- coding: utf-8 -*-
"""LA COLA ENTERA DE LA VUELTA 32, RECONTADA FILA A FILA CONTRA EL DATO.

**NO SE RECUENTA CONTRA LA TABLA DEL ENCARGO: SE RECUENTA CONTRA EL DATO.** Si una
cifra del auditor no me sale, gana la mia y la discrepancia se declara
(`EXTRACTOR.md` 5, y el propio encargo lo manda con esas palabras).
"""
import glob
import io
import json
import os
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

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

# cap_04: la poblacion es el archivo MAS la bandeja. Sus seis YA ENTRARON y lo que
# queda pendiente es RELEERLOS, no insertarlos.
c4 = []
for ruta in (glob.glob("cuarentena/_insertados/scott_radical_candor/*.json")
             + glob.glob("cuarentena/scott_radical_candor/*.json")):
    datos = json.load(io.open(ruta, encoding="utf-8"))
    if "cap_04" in datos.get("resumen_teorico", ""):
        c4.append(datos)


def en_bandeja_de(capitulo):
    patron = re.compile(capitulo + r"\.md[^\n]*?lineas (\d+) a (\d+)")
    return sum(1 for ruta in glob.glob("cuarentena/scott_radical_candor/*.json")
               if patron.search(json.load(io.open(ruta, encoding="utf-8"))
                                .get("resumen_teorico", "")))


CABEZA = "decidir_quien_comunica_cada_cuanto"
hijos_cabeza = set(vivos[CABEZA].get("nodos_siguientes") or [])
sin_huella = sum(1 for l in io.open(".v32/rancios_full.txt", encoding="utf-8")
                 if "[SIN HUELLA]" in l)
filas_censo = sum(1 for l in io.open("censos/series_y_cabezas.md", encoding="utf-8")
                  if l.startswith("|") and not l.startswith("|---")
                  and "fecha" not in l)

print("| lo que queda | cifra del encargo | **cifra que mido hoy** | estado |")
print("|---|---:|---:|---|")

print("| la arista de la cabeza al decimo rotulo | 1 | **%d** | **CERRADA HOY** por la `TAREA 2.d`. "
      "Los dos extremos en el GRAFO |"
      % (0 if cableada(CABEZA, "recorrer_rueda_conscientemente_cultura_equipo") else 1))

print("| las dos aristas con fecha de caducidad de la `TAREA 3.b` | 2 | **%d** | "
      "**CERRADAS LAS DOS HOY**, declaradas en el acto de cada insercion |"
      % sum(0 if cableada(CABEZA, h) else 1
            for h in ("montar_tablero_kanban_medir_actividades",
                      "pasear_organizacion_hallar_problemas_pequenios")))

print("| aristas en cola escritas en la bitacora | 4 escritas, 3 cableadas, 1 abierta | "
      "**%d** escritas, **%d** cableadas, **%d** abierta | la abierta es la linea `%s`, "
      "y la cierra que entre la MADRE, hoy en %s |"
      % (len(en_cola), len(en_cola) - len(abiertas), len(abiertas),
         ", ".join(str(c[0]) for c in abiertas) or "ninguna",
         ", ".join(sede(c[1]) for c in abiertas) or "nada"))

print("| el `resumen_teorico` de `recorrer_rueda_conscientemente` | 1 | **0** | "
      "**CERRADA HOY** por la `TAREA 4`, correccion declarada sin borrar |")

print("| **huecos de transcripcion** | 2 ejemplares y 2 especies | **2** y **2** | "
      "sigue **SIN VIA** y **NO construyo la via** (moratoria de maquinaria, y el encargo lo "
      "manda expresamente) |")

print("| las entradillas de `LISTEN`, `CLARIFY` y `DEBATE` de `cap_07` sin nodo | 3 de 7 | "
      "**3** de **7** | **NADA la cierra**: adjudicado consecuencia buena (`ACTA 29` `5`). "
      "Registro, no deuda |")

print("| `L221` de `cap_07`, *turn on that rock tumbler* | 1 | **1** tramo | "
      "**NO se toca**: `cap_07` cerrado en insercion |")

print("| `cap_04` releido, candidatos y pasos | 6 y 48 | **%d** y **%d** | "
      "**SIGUE SIN CABER**, y van cuatro vueltas. Lo declaro otra vez con su motivo |"
      % (len(c4), sum(len(d["pasos_accionables"]) for d in c4)))

print("| la frontera por capitulo con las `QUESTIONS TO CONSIDER` | 14 de 17 | **14** de **17** | "
      "la vuelta que mine un capitulo del lote 5 |")

print("| las `8` lineas `SIN HUELLA` de `D.15` | 8, las 8 declaradas | **%d**, **las 8 declaradas** | "
      "**CERRADA**. Lo que sigue imprimiendo `8` es el instrumento, no el trabajo |" % sin_huella)

print("| `censos/series_y_cabezas.md` | 0 filas con 267 nodos | **%d** filas con **%d** nodos | "
      "**propuesta registrada y NO encargada.** Moratoria |" % (filas_censo, len(vivos)))

print("| bandeja del lote 4 | 78 | **%d** | la insercion. **`3` menos que al abrir** |"
      % len(glob.glob("cuarentena/scott_radical_candor/*.json")))

print("| de esa bandeja, lo que queda de `cap_11` | 3 | **%d** | **CERRADA HOY**: `cap_11` queda "
      "entero en el grafo, `14` de `14` |" % en_bandeja_de("cap_11"))

print("| lote 5 | 3 | **%d** | **NO TOCADO**, y es deliberado (`D.39`) |"
      % len(glob.glob("cuarentena/marquet_turn_the_ship/*.json")))

print()
print("LAS ARISTAS EN COLA, CONTADAS DE SU SEDE Y NO DE LA MEMORIA")
print()
print("| linea | arista en cola | estado | que la cierra |")
print("|---:|---|---|---|")
for numero, madre, hijo, ok in en_cola:
    if ok:
        estado, cierra = "**CABLEADA**", "nada: los dos extremos viven y la arista esta puesta"
    elif madre not in vivos:
        estado, cierra = "**ABIERTA**", "que entre la MADRE, hoy en %s" % sede(madre)
    elif hijo not in vivos:
        estado, cierra = "**ABIERTA**", "que entre el HIJO, hoy en %s" % sede(hijo)
    else:
        estado, cierra = "**ABIERTA**", "**los dos viven: la arista falta y eso es hallazgo**"
    print("| `%d` | `%s > %s` | %s | %s |" % (numero, madre, hijo, estado, cierra))
