# -*- coding: utf-8 -*-
"""LA FECHA QUE UN ACTO DEL BUCLE SE ESCRIBE A SI MISMO, CONTRA EL SELLO DE LA MAQUINA.

QUE CUENTA Y QUE NO, que es lo unico que hace comparable la cifra:

  POBLACION   toda fecha en castellano (`<d> <mes> <aaaa>`) escrita DENTRO de
              `dataset/nodos.jsonl` o de `bitacora/VEREDICTOS.jsonl` precedida, en su
              misma celda, por el rotulo con el que un acto del bucle se firma:
              `... DECLARAD[AO]` o `ESCRITA EN LA VUELTA <n>`. Es la fecha que el acto
              dice DE SI MISMO, y por eso es la unica que se puede cuadrar con un sello.
  FUERA       toda fecha citada como dato de otro (la firma del fundador, la fecha de
              una decision del banco, la de un fichero de fuente): la maquina no las
              estampa y no hay sello contra el que cuadrarlas.

  EL SELLO, y hay que buscarlo donde esta y no donde es comodo:
    - dentro de `anotaciones[i]`      : el campo `fecha` de ESA anotacion, que es lo
                                        que `src/anotacion.py:185` escribe. **NO el de
                                        la linea**: el de la linea es del veredicto
                                        original y puede ser de dias antes.
    - en `razon`, texto que una anotacion tambien lleva : el de esa anotacion, porque
                                        `anotar` lo pega en los dos sitios a la vez.
    - resto de la bitacora            : el campo `fecha` de la linea.
    - `dataset/nodos.jsonl`           : NO HAY sello, el nodo no lleva fecha de
                                        escritura. El de una correccion del
                                        `resumen_teorico` es el de la linea de la
                                        bitacora que registro esa misma correccion,
                                        buscada por `candidato` mas el TROZO de texto
                                        que rodea a la propia fecha: el `resumen_teorico`
                                        de un nodo arranca con el texto viejo, asi que
                                        casar por su primer renglon no casa nada.

  Y LA COLUMNA `remedio`, que hace falta porque `D.13` corrige SIN BORRAR: la fecha
  mala sigue ahi despues de arreglarla, asi que contarla como caida viva seria contar
  dos veces. Una celda que choca sale **CORREGIDA** cuando en su propio texto, o en la
  anotacion pegada a su linea, hay un `CORRECCION DECLARADA` que **escribe el sello que
  la maquina estampo** (`2026-09-16` y tambien `16 sep 2026`). Esa es la prueba
  mecanica de que alguien no solo la vio, sino que dejo escrito cual era la buena.

Cero ids tecleados dentro: todo sale de recorrer los dos ficheros.
"""
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MESES = {"ene": "01", "feb": "02", "mar": "03", "abr": "04", "may": "05", "jun": "06",
         "jul": "07", "ago": "08", "sep": "09", "oct": "10", "nov": "11", "dic": "12"}
FECHA = r"\b(\d{1,2})\s+(ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)\s+(\d{4})\b"
ACTO = re.compile(r"(?:DECLARAD[AO]|ESCRITA EN LA VUELTA\s+\d+)[^.]{0,24}?" + FECHA)


def celdas(obj, camino=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            for c in celdas(v, camino + "/" + k):
                yield c
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            for c in celdas(v, camino + "[%d]" % i):
                yield c
    elif isinstance(obj, str):
        yield camino, obj


def leer(sede):
    for n, linea in enumerate(open(os.path.join(RAIZ, sede), encoding="utf-8"), 1):
        if linea.strip():
            yield n, json.loads(linea)


correcciones = []
for _, v in leer("bitacora/VEREDICTOS.jsonl"):
    t = v.get("texto_anadido")
    if t and v.get("candidato") and v.get("fecha"):
        correcciones.append((v["candidato"], t, v["fecha"]))


def sello_dataset(id_nodo, trozo):
    """el sello de la correccion de la bitacora que trajo ESTE trozo al nodo."""
    for candidato, texto, fecha in correcciones:
        if candidato == id_nodo and trozo in texto:
            return fecha
    return None


MESES_INV = {"01": "ene", "02": "feb", "03": "mar", "04": "abr", "05": "may",
             "06": "jun", "07": "jul", "08": "ago", "09": "sep", "10": "oct",
             "11": "nov", "12": "dic"}


def remediada(textos, iso):
    """hay un CORRECCION DECLARADA que escribe el sello bueno, en ISO o en castellano."""
    anio, mes, dia = iso.split("-")
    castellano = "%d %s %s" % (int(dia), MESES_INV[mes], anio)
    for t in textos:
        if not t or "CORRECCION DECLARADA" not in t:
            continue
        trozo = t[t.index("CORRECCION DECLARADA"):]
        if iso in trozo or castellano in trozo:
            return True
    return False


def sello_bitacora(obj, campo, texto):
    m = re.match(r"^/anotaciones\[(\d+)\]", campo)
    if m:
        return (obj.get("anotaciones") or [])[int(m.group(1))].get("fecha")
    for a in (obj.get("anotaciones") or []):
        if a.get("texto") and a["texto"].strip()[:60] in texto:
            return a.get("fecha")
    return obj.get("fecha")


tot = 0
chocan = []
sin_sello = []
for sede in ("dataset/nodos.jsonl", "bitacora/VEREDICTOS.jsonl"):
    n_sede = 0
    for nlinea, obj in leer(sede):
        for campo, texto in celdas(obj):
            for m in ACTO.finditer(texto):
                d, mes, anio = m.groups()
                n_sede += 1
                mano = "%s-%s-%02d" % (anio, MESES[mes], int(d))
                if sede.startswith("bitacora"):
                    maq, sujeto = sello_bitacora(obj, campo, texto), obj.get("candidato")
                else:
                    sujeto = obj.get("id")
                    maq = sello_dataset(sujeto, texto[m.start():m.end() + 60])
                if maq and mano != maq:
                    vecinos = [texto] + [a.get("texto") for a in (obj.get("anotaciones") or [])]
                    marca = "**CORREGIDA**" if remediada(vecinos, maq) else "**SIN CORREGIR**"
                    chocan.append((sede, nlinea, campo, "%s %s %s" % (d, mes, anio),
                                   maq, sujeto, marca))
                if maq is None:
                    sin_sello.append((sede, nlinea, campo, sujeto))
    print("%-30s fechas que un acto se escribe a si mismo: %3d" % (sede, n_sede))
    tot += n_sede
print("%-30s fechas que un acto se escribe a si mismo: %3d" % ("LAS DOS SEDES", tot))
print("")
print("fechas SIN sello con el que cuadrarlas (no se juzgan, y se dice): %d" % len(sin_sello))
vivas = [c for c in chocan if "SIN CORREGIR" in c[6]]
print("CELDAS QUE CHOCAN CON EL SELLO DE LA MAQUINA: %d" % len(chocan))
print("   de ellas, con su CORRECCION DECLARADA al lado : %d" % (len(chocan) - len(vivas)))
print("   de ellas, VIVAS y sin remedio escrito         : %d" % len(vivas))
print("")
print("| sede | linea | celda | la mano escribio | la maquina estampo | sujeto | remedio |")
print("|---|---:|---|---|---|---|---|")
for sede, nl, campo, mano, maq, sujeto, marca in chocan:
    print("| `%s` | %d | `%s` | `%s` | `%s` | `%s` | %s |"
          % (sede, nl, campo, mano, maq, sujeto, marca))
print("")
print("LAS %d SIN SELLO, UNA A UNA, para que nadie tenga que fiarse del recuento:" % len(sin_sello))
for sede, nl, campo, sujeto in sin_sello:
    print("   %-26s linea %4d  %-22s %s" % (sede, nl, campo, sujeto))
