# -*- coding: utf-8 -*-
"""LOS ROTULOS QUE LA CABEZA DE cap_11 ENUMERA, Y CUAL DE ELLOS ES NODO HOY.

VERSION 2, 17 sep 2026, REMEDIO DE LA `TAREA 2` DE LA VUELTA 32.

La version 1 (`.v31/cabeza.py`) llevaba **el mapeo de rotulo a nodo TECLEADO en una
constante**, y por eso pudo publicar una fila mala y salir VERDE en el tallado: lo
tecleado estaba DENTRO del instrumento. Aqui **no queda ni un nodo tecleado**:

  - los rotulos salen del bloque de indice del propio `cap_11.md`;
  - los titulares del cuerpo salen del propio `cap_11.md`;
  - cada rotulo se casa con su titular POR DOS VIAS INDEPENDIENTES, por el nombre
    y por la posicion, y **si las dos no coinciden el instrumento lo dice**;
  - el nodo que lo procedimenta se casa por el RANGO DE LINEAS QUE CADA
    `resumen_teorico` DECLARA DE SI MISMO, que es el que sigue a la formula
    literal `Sale de las lineas`. Un rango que el resumen cite de un VECINO no
    cuenta, y esa es la trampa que costo la primera version de esta cuenta.
"""
import glob
import io
import json
import os
import re
import sys
import unicodedata

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

CABEZA = "decidir_quien_comunica_cada_cuanto"
LIBRO = "scott_radical_candor"
CAPITULO = "cap_11"
FUENTE = "fuentes/%s/%s.md" % (LIBRO, CAPITULO)
BANDEJA = "cuarentena/%s" % LIBRO

# ---------------------------------------------------------------- el libro

with open(FUENTE, encoding="utf-8") as f:
    LINEAS = f.read().split("\n")


def normaliza(texto):
    """Sube a mayusculas y tira comillas, acentos y espacios de mas."""
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    for comilla in ("“", "”", "‘", "’", '"', "'"):
        texto = texto.replace(comilla, "")
    return " ".join(texto.upper().split())


def es_titular(texto):
    """Un titular del cuerpo: linea corta, sin minusculas y con al menos una letra."""
    limpio = texto.strip()
    if not limpio or len(limpio) > 60:
        return False
    if not any(c.isalpha() for c in limpio):
        return False
    return limpio == limpio.upper()


TITULARES = [(n, t.strip()) for n, t in enumerate(LINEAS, 1) if es_titular(t)]
PRIMER_TITULAR = TITULARES[0][0] if TITULARES else len(LINEAS)

# El bloque de indice: las lineas no vacias entre el ultimo parrafo largo y el
# primer titular del cuerpo. Ni el principio ni el final se teclean.
ULTIMO_PARRAFO = 0
for numero, texto in enumerate(LINEAS, 1):
    if numero >= PRIMER_TITULAR:
        break
    if len(texto.strip()) >= 200:
        ULTIMO_PARRAFO = numero

ROTULOS = [(n, LINEAS[n - 1].strip())
           for n in range(ULTIMO_PARRAFO + 1, PRIMER_TITULAR)
           if LINEAS[n - 1].strip()]

# ---------------------------------------------------------------- el dato

FORMULA = "Sale de las lineas "
TRAMO = re.compile(r"^(\d+)\s+a\s+(?:las\s+)?(\d+)")
ENLACE = re.compile(r"^,?\s*y\s+de\s+(?:las\s+)?lineas\s+")


def rangos_propios(resumen):
    """SOLO los tramos que el resumen declara DE SI MISMO: los que cuelgan de la
    formula `Sale de las lineas`, encadenados por `y de las lineas`. Se para en
    cuanto el texto deja de ser un tramo, asi que un rango citado de un vecino
    mas adelante en la prosa NO entra."""
    posicion = (resumen or "").find(FORMULA)
    if posicion < 0:
        return []
    resto = resumen[posicion + len(FORMULA):]
    tramos = []
    while True:
        casa = TRAMO.match(resto)
        if not casa:
            break
        tramos.append((int(casa.group(1)), int(casa.group(2))))
        resto = resto[casa.end():]
        enlace = ENLACE.match(resto)
        if not enlace:
            break
        resto = resto[enlace.end():]
    return tramos


GRAFO = {}
for linea in open("dataset/nodos.jsonl", encoding="utf-8"):
    datos = json.loads(linea)
    GRAFO[datos["id"]] = datos

EN_BANDEJA = {}
for ruta in sorted(glob.glob(os.path.join(BANDEJA, "*.json"))):
    with open(ruta, encoding="utf-8") as f:
        datos = json.load(f)
    EN_BANDEJA[datos["id"]] = datos

TRAMOS = []  # (desde, hasta, id, donde)
for origen, poblacion in (("en el grafo", GRAFO), ("en bandeja", EN_BANDEJA)):
    for identificador, datos in sorted(poblacion.items()):
        resumen = datos.get("resumen_teorico") or ""
        if FUENTE not in resumen:
            continue
        for a, b in rangos_propios(resumen):
            TRAMOS.append((a, b, identificador, origen))

HIJOS = set(GRAFO[CABEZA].get("nodos_siguientes") or [])

# ---------------------------------------------------------------- el casado


def por_nombre(rotulo):
    objetivo = normaliza(rotulo)
    for numero, texto in TITULARES:
        if normaliza(texto) == objetivo:
            return numero
    return None


def nodo_en(linea):
    dentro = [t for t in TRAMOS if t[0] <= linea <= t[1]]
    if not dentro:
        return None
    dentro.sort(key=lambda t: (t[1] - t[0], t[2]))
    return dentro[0]


print("LOS ROTULOS DEL INDICE DE cap_11 QUE EL PASO 6 DE LA CABEZA ENUMERA")
print("AVISO: cero nodos tecleados en este instrumento. El rotulo sale del indice de")
print("       %s, el titular sale del cuerpo del" % FUENTE)
print("       mismo fichero, y el nodo se casa por el rango que su propio resumen declara.")
print("cabeza  : %s" % CABEZA)
print("indice  : %d rotulos, entre las lineas %d y %d"
      % (len(ROTULOS), ROTULOS[0][0], ROTULOS[-1][0]))
print("cuerpo  : %d titulares en mayuscula" % len(TITULARES))
print("tramos  : %d declarados por %d nodos de este capitulo"
      % (len(TRAMOS), len(set(t[2] for t in TRAMOS))))
if len(ROTULOS) == len(TITULARES):
    print("LAS DOS LISTAS TIENEN EL MISMO LARGO, asi que el casado por POSICION es una")
    print("       segunda via independiente y se publica al lado de la del nombre.")
else:
    print("AVISO: las dos listas NO tienen el mismo largo, asi que el casado por POSICION")
    print("       no se publica.")
print()
print("| # | rotulo del indice | linea | titular del cuerpo | linea | las dos vias | nodo que lo procedimenta | donde esta | arista cabeza a parte |")
print("|---:|---|---|---|---|---|---|---|---|")

filas = []
discrepan = 0
for indice, (linea_indice, rotulo) in enumerate(ROTULOS, 1):
    nombre = por_nombre(rotulo)
    posicion = TITULARES[indice - 1] if len(ROTULOS) == len(TITULARES) else None
    if nombre is not None and posicion is not None and nombre == posicion[0]:
        via, linea_cuerpo, titular = "las dos", nombre, posicion[1]
    elif nombre is not None:
        via, linea_cuerpo, titular = "solo el nombre", nombre, LINEAS[nombre - 1].strip()
    elif posicion is not None:
        via, linea_cuerpo, titular = "**SOLO LA POSICION**", posicion[0], posicion[1]
        discrepan += 1
    else:
        filas.append((rotulo, None, None, None))
        print("| %d | %s | `L%d` | **no lo hay** | | **ninguna** | (ninguno) | **no hay nodo** | **no se declara** |"
              % (indice, rotulo, linea_indice))
        continue
    encontrado = nodo_en(linea_cuerpo)
    if encontrado is None:
        filas.append((rotulo, linea_cuerpo, None, None))
        print("| %d | %s | `L%d` | %s | `L%d` | %s | (ninguno) | **ningun tramo lo cubre** | **no se puede** |"
              % (indice, rotulo, linea_indice, titular, linea_cuerpo, via))
        continue
    _a, _b, identificador, donde = encontrado
    if donde == "en el grafo":
        arista = "**CABLEADA**" if identificador in HIJOS else "**NO, y se dice por que**"
    else:
        arista = "espera a que entre"
    filas.append((rotulo, linea_cuerpo, identificador, donde))
    print("| %d | %s | `L%d` | %s | `L%d` | %s | `%s` | %s | %s |"
          % (indice, rotulo, linea_indice, titular, linea_cuerpo, via, identificador, donde, arista))

con_nodo = [f for f in filas if f[2]]
print()
print("| | |")
print("|---|---:|")
print("| rotulos que el indice enumera | **%d** |" % len(ROTULOS))
print("| **de ellos, con nodo dentro del grafo hoy** | **%d** |"
      % sum(1 for f in con_nodo if f[3] == "en el grafo"))
print("| **de ellos, con la arista cabeza a parte cableada** | **%d** |"
      % sum(1 for f in con_nodo if f[2] in HIJOS))
print("| de ellos, con su nodo todavia en bandeja | **%d** |"
      % sum(1 for f in con_nodo if f[3] == "en bandeja"))
print("| de ellos, sin nodo ninguno | **%d** |" % sum(1 for f in filas if not f[2]))
print("| **rotulos donde las dos vias de casado NO coinciden** | **%d** |" % discrepan)
print("| hijos que la cabeza declara en `nodos_siguientes` | **%d** |" % len(HIJOS))
